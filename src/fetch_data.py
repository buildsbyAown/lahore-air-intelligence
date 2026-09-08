"""Download raw data used in the Lahore Air Intelligence project.

Sources (all open, no API key needed):
  1. OpenAQ public S3 archive  - measured PM2.5 (US Consulate Lahore BAM monitor, location 8664;
                                 Clarity low-cost sensor, location 1894641)
  2. Open-Meteo Historical Weather API (ERA5 reanalysis) - hourly weather incl. boundary layer height

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
OPENAQ_LOCATIONS = {8664: "openaq_us_consulate_lahore_hourly.csv",
                    1894641: "openaq_clarity_lahore_hourly.csv"}

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

def fetch_weather():
    out = os.path.join(RAW, "openmeteo_era5_weather_hourly.csv")
    if os.path.exists(out):
        return
    vars_ = ("temperature_2m,relative_humidity_2m,dew_point_2m,precipitation,surface_pressure,"
             "wind_speed_10m,wind_direction_10m,boundary_layer_height,cloud_cover")
    r = requests.get("https://archive-api.open-meteo.com/v1/archive", timeout=300, params=dict(
        latitude=LAT, longitude=LON, start_date=START, end_date=END, hourly=vars_,
        timezone="Asia/Karachi"))
    r.raise_for_status()
    df = pd.DataFrame(r.json()["hourly"])
    df.to_csv(out, index=False)
    print("  saved", out, len(df), "rows")

if __name__ == "__main__":
    for lid, fn in OPENAQ_LOCATIONS.items():
        fetch_openaq(lid, fn)
    fetch_weather()
    print("done")
