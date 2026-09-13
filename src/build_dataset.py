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
    # QC: implausibly clean "winter" runs (sensor fault). In Oct-Mar, drop runs of >=3 consecutive
    # days whose mean is < 15 µg/m³ (this removes 1-10 Feb 2020, ~8 µg/m³ during peak smog season).
    s = pd.Series(daily.values, index=pd.to_datetime(daily.index))
    low = (s < 15) & s.index.month.isin([10, 11, 12, 1, 2, 3])
    run_id = (low != low.shift()).cumsum()
    run_len = low.groupby(run_id).transform("sum")
    bad = low & (run_len >= 3)
    if bad.any():
        print("  QC removed suspect days:", [d.date().isoformat() for d in s.index[bad]])
    daily = daily[~bad.values]
    print(f"US Consulate: {n_raw} raw hours -> {len(d)} valid hours -> {len(daily)} valid days")
    return daily.rename("pm25_consulate"), g["count"].rename("consulate_valid_hours")

def clarity_pm25():
    d = pd.read_csv(os.path.join(RAW, "openaq_clarity_lahore_hourly.csv"))
    d = d[d.parameter == "pm25"].copy()
    d["t"] = local_dates(d.datetime)
    d = d[(d.value > 0) & (d.value < 1000)]
    hourly = d.set_index("t")["value"].resample("1h").mean().dropna()
    g = hourly.groupby(hourly.index.date).agg(["mean", "count"])
    daily = g.loc[g["count"] >= 18, "mean"]
    print(f"Clarity sensor: {len(daily)} valid days")
    return daily.rename("pm25_clarity_sensor")

if __name__ == "__main__":
    cons, cons_hours = consulate_pm25()
    clarity = clarity_pm25()
    print("consulate", len(cons), "clarity", len(clarity))
