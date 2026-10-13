# Lahore Air Intelligence

**AI-Driven Analysis and Prediction of Air Pollution in Lahore, Pakistan**

*An independent research project by [Your Name], Lahore, Pakistan. Started November 2026.*

![Daily PM2.5 in Lahore](visualizations/fig01_daily_pm25_timeseries.png)

## The problem

Lahore is regularly ranked among the most polluted cities on Earth. In 2024 its annual average PM2.5 was 102 µg/m³, about 20 times the WHO guideline ([IQAir](https://www.iqair.com/newsroom/5-most-polluted-major-cities-in-world-2024)), and the Air Quality Life Index estimates that clean air would add **5.8 years** to the life expectancy of people in Lahore ([AQLI](https://aqli.epic.uchicago.edu/files/Pakistan%20FactSheet_2025.pdf)). Every winter the city fills with smog that comes from many sources — vehicles, brick kilns and industry, crop-residue and waste burning, and pollution carried in from the wider region — and is trapped by cold, still air under a temperature inversion.

I live here. My long-term goal is to help Lahore **predict hazardous air before it happens** and give people and decision-makers better information to act on, using data science and machine learning.

## Research question

> How do seasonal and meteorological conditions influence PM2.5 concentrations in Lahore, and can machine learning predict short-term changes?

1. How have PM2.5 concentrations changed over recent years?
2. Which months and seasons are worst?
3. How is PM2.5 related to temperature, humidity, wind, rain and boundary-layer height?
4. Can ML models predict next-day PM2.5 from past pollution and weather?

## Key findings so far (Week 1)

Full report: [`research/preliminary_findings.md`](research/preliminary_findings.md)

- Based on 1,456 valid days of measurements from the US Consulate monitor (2019–2025), **50% of days exceeded the WHO 24-hour guideline**, and **7% were "Hazardous"** (> 250 µg/m³). The worst day was **621 µg/m³ on 14 Nov 2024**.
- **December and November average 268 and 254 µg/m³, compared with 46 in August** (5.8×).
- Winter (Nov–Jan) averages have **not improved**: 212 µg/m³ in 2019–20, 269 in 2023–24 and 265 in 2024–25.
- In winter, the boundary layer collapses to about **50 m at night**. PM2.5 peaks around midnight, and on days with a very shallow night-time layer it averages **191 µg/m³**, compared with under 50 when the layer is deeper than 200 m.
- **Within winter**, the days that turn out worst are separated by low wind and a shallow boundary layer, not by temperature.
- A first **Random Forest** next-day forecast beats the "tomorrow = today" baseline by **10%** using past data only, and by **19%** (R² 0.84) when it is also given the next day's weather.

| | |
|---|---|
| ![Seasonal cycle](visualizations/fig03_monthly_seasonal_cycle.png) | ![Diurnal cycle](visualizations/fig04_diurnal_cycle_blh.png) |
| ![Boundary layer vs PM2.5](visualizations/fig06_boundary_layer_vs_pm25.png) | ![Forecast model comparison](visualizations/fig09_forecast_model_comparison.png) |

> **Scope note:** this analysis shows *when* and *under what weather* pollution builds up. It does **not** identify which emission source is largest. That requires emission inventories or chemical source-apportionment studies (see the [literature review](research/literature_review.md)).

## Project structure

```
lahore-air-intelligence/
├── data/
│   ├── raw/                     # downloaded source files (OpenAQ, Open-Meteo/ERA5, CAMS, NASA FIRMS)
│   ├── processed/               # cleaned daily merged dataset + cleaned hourly PM2.5
│   └── README.md                # sources, coverage, cleaning rules and caveats
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb   # trends, seasons, hour-of-day, weather correlations, fires
│   └── 02_baseline_forecast.ipynb      # persistence vs Ridge / Random Forest / XGBoost, next-day PM2.5
├── src/
│   ├── fetch_data.py            # downloads all raw data (no API keys needed)
│   └── build_dataset.py         # cleaning + daily merge
├── models/                      # model results (test-set metrics)
├── visualizations/              # all figures (PNG)
├── research/
│   ├── literature_review.md     # causes of Lahore's smog, with sources
│   └── preliminary_findings.md  # Week 1 progress report
├── requirements.txt
└── README.md
```

## Data

| Source | Variable | Period | Type |
|---|---|---|---|
| US Consulate Lahore monitor (via [OpenAQ archive](https://openaq.org)) | PM2.5, hourly | May 2019 – Feb 2025 | Measured (reference) |
| Clarity low-cost sensor (via OpenAQ) | PM2.5 | Nov 2023 – Aug 2026 | Measured (low-cost, uncalibrated) |
| [CAMS](https://atmosphere.copernicus.eu/) via [Open-Meteo](https://open-meteo.com/en/docs/air-quality-api) | PM2.5, PM10, CO, NO2, dust | Aug 2022 – Nov 2026 | Modelled |
| [ERA5](https://open-meteo.com/en/docs/historical-weather-api) via Open-Meteo | Temperature, humidity, wind, rain, pressure, boundary layer height | 2019 – Nov 2026 | Reanalysis |
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) MODIS | Active fire detections, Punjab region | 2019 – 2025 | Satellite |

Details and caveats: [`data/README.md`](data/README.md).
