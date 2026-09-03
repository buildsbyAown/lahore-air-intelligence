"""Download raw data used in the Lahore Air Intelligence project.

Sources (all open, no API key needed):
  1. OpenAQ public S3 archive  - measured PM2.5 (US Consulate Lahore BAM monitor, location 8664)

Run:  python src/fetch_data.py      (takes a few minutes; re-running skips files that exist)
"""
import gzip, io, os, re, sys, urllib.parse
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
os.makedirs(RAW, exist_ok=True)

LAT, LON = 31.5204, 74.3587          # Lahore city centre
START, END = "2019-01-01", "2026-11-15"
S3 = "https://openaq-data-archive.s3.amazonaws.com"
OPENAQ_LOCATIONS = {8664: "openaq_us_consulate_lahore_hourly.csv"}

def s3_keys(location_id):
    keys, token = [], None
    while True:
        url = f"{S3}/?list-type=2&prefix=records/csv.gz/locationid={location_id}/"
        if token:
            url += "&continuation-token=" + urllib.parse.quote(token)
        xml = requests.get(url, timeout=60).text
        keys += re.findall(r"<Key>([^<]+)</Key>", xml)
        m = re.search(r"<NextContinuationToken>([^<]+)", xml)
        if not m:
            return keys
        token = m.group(1)


def fetch_openaq(location_id, fname):
    out = os.path.join(RAW, fname)
    if os.path.exists(out):
        return
    keys = s3_keys(location_id)
    print(f"OpenAQ {location_id}: {len(keys)} daily files")
    def get(k):
        r = requests.get(f"{S3}/{k}", timeout=60)
        return pd.read_csv(io.BytesIO(gzip.decompress(r.content)))
    with ThreadPoolExecutor(16) as ex:
        frames = list(ex.map(get, keys))
    df = pd.concat(frames, ignore_index=True)
    df.to_csv(out, index=False)
    print("  saved", out, len(df), "rows")

if __name__ == "__main__":
    for lid, fn in OPENAQ_LOCATIONS.items():
        fetch_openaq(lid, fn)
    print("done")
