"""Clean the raw files and build one daily table: data/processed/lahore_daily_merged.csv

All dates are local Lahore time (Asia/Karachi, UTC+5).
"""
import os
import numpy as np
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
OUT = os.path.join(ROOT, "data", "processed")
os.makedirs(OUT, exist_ok=True)
START, END = "2019-01-01", "2026-11-15"


def local_dates(series):
    # OpenAQ datetimes carry a +05:00 offset; convert to Lahore local time
    return pd.to_datetime(series, utc=True).dt.tz_convert("Asia/Karachi")

def consulate_pm25():
    d = pd.read_csv(os.path.join(RAW, "openaq_us_consulate_lahore_hourly.csv"))
    d["t"] = local_dates(d.datetime)
    n_raw = len(d)
    d = d[(d.value > 0) & (d.value < 1000)]          # -999 = missing flag
    d = d.drop_duplicates("t")
    d.set_index("t")["value"].rename("pm25").to_csv(os.path.join(OUT, "us_consulate_pm25_hourly_clean.csv"))
    g = d.groupby(d.t.dt.date)["value"].agg(["mean", "count"])
    daily = g.loc[g["count"] >= 18, "mean"]          # need >=75% of hours for a valid daily mean
    print(f"US Consulate: {n_raw} raw hours -> {len(d)} valid hours -> {len(daily)} valid days")
    return daily.rename("pm25_consulate"), g["count"].rename("consulate_valid_hours")

if __name__ == "__main__":
    cons, cons_hours = consulate_pm25()
    print(len(cons), "valid consulate days")
