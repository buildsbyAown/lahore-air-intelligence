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

if __name__ == "__main__":
    print("fetch helpers not yet implemented")
