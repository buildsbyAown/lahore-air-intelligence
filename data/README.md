# Data

All data in this folder comes from open sources that anyone can download without an account or API key.
Re-create everything with:

```bash
python src/fetch_data.py      # downloads data/raw/*
python src/build_dataset.py   # builds data/processed/*
```

Downloaded on 18 November 2026. All dates in the processed files are **local Lahore time (Asia/Karachi, UTC+5)**.

## Sources

| File (data/raw/) | What it is | Source | Coverage | Measured or modelled? |
|---|---|---|---|---|
| `openaq_us_consulate_lahore_hourly.csv` | Hourly PM2.5, US Consulate General Lahore monitor (US State Department AirNow programme), OpenAQ location **8664**, 31.5601° N 74.3359° E | [OpenAQ public archive on AWS S3](https://openaq-data-archive.s3.amazonaws.com/) (`records/csv.gz/locationid=8664/`) | 23 May 2019 – early Mar 2025 (with gaps) | **Measured** – reference-grade monitor. Main ground truth of this project. |
| `openaq_clarity_lahore_hourly.csv` | PM2.5 (plus PM1, PM10, temperature for part of the period) from a Clarity low-cost sensor in Lahore, OpenAQ location **1894641**, 31.548° N 74.344° E | OpenAQ public archive (`locationid=1894641`), licence CC0 1.0 | 28 Nov 2023 – 31 Aug 2026 (with gaps) | **Measured**, but by a **low-cost optical sensor**, not calibrated against a reference monitor. |
| `openmeteo_cams_airquality_hourly.csv` | Hourly PM2.5, PM10, CO, NO2, dust for the grid cell over central Lahore (31.52° N, 74.36° E) | [Open-Meteo Air Quality API](https://open-meteo.com/en/docs/air-quality-api) → Copernicus Atmosphere Monitoring Service (CAMS) global model | 4 Aug 2022 – 15 Nov 2026 | **Modelled** (≈40 km grid). Not a measurement. |
| `openmeteo_era5_weather_hourly.csv` | Hourly temperature, humidity, dew point, rain, surface pressure, wind speed and direction, cloud cover, **boundary layer height** | [Open-Meteo Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api) → ECMWF ERA5 reanalysis | 1 Jan 2019 – 15 Nov 2026 | **Reanalysis** (model + observations). Boundary layer height is missing for Jan–Jun 2024 in the archive. |
| `firms_modis_punjab_fires.csv` | Satellite active-fire detections (MODIS Collection 6.1) inside the box 29.5–32.6° N, 72.0–76.9° E (Pakistani and Indian Punjab around Lahore) | [NASA FIRMS country archives](https://firms.modaps.eosdis.nasa.gov/country/) (Pakistan + India yearly CSVs) | 2019 – 2025 | **Satellite detections**. Counts only fires burning when the satellite passes (≈10:30 and 13:30 local time); misses small, cloud-covered and evening fires. |

### Sources I tried but could not use (yet)
- **OpenAQ API v3** needs an API key, so I used OpenAQ's public S3 archive instead (same data).
- **US State Department historical CSVs** (`dosairnowdata.org`) were unreachable (server/TLS error) when I tried. The same Lahore monitor data is in the OpenAQ archive.
- **Punjab EPD monitoring stations**: I have not found a public, downloadable historical archive yet. To do.

## Processed files (data/processed/)

- `lahore_daily_merged.csv` – one row per day, 1 Jan 2019 – 15 Nov 2026. Columns:
  - `pm25_consulate` – daily mean PM2.5 (µg/m³) from the US Consulate monitor
  - `pm25_clarity_sensor` – daily mean PM2.5 from the low-cost sensor
  - `pm25_cams_model`, `pm10_cams_model`, `co_cams_model`, `no2_cams_model`, `dust_cams_model` – daily means from CAMS (modelled)
  - weather: `temp_mean_c`, `temp_min_c`, `temp_max_c`, `temp_range_c`, `rh_mean_pct`, `dewpoint_mean_c`, `precip_mm` (daily total), `pressure_mean_hpa`, `wind_speed_mean_kmh`, `wind_dir_vector_deg` (vector-averaged direction the wind blows *from*), `cloud_cover_mean_pct`, `blh_mean_m`, `blh_max_m`, `blh_night_mean_m` (mean boundary layer height 22:00–05:00)
  - fires: `fires_pakistani_punjab_region`, `fires_indian_punjab_region`, `fires_punjab_region_total` (daily counts; empty after 2025)
- `us_consulate_pm25_hourly_clean.csv` – cleaned hourly PM2.5 from the consulate monitor (used for the hour-of-day analysis).
