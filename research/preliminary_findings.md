# Preliminary findings — Week 1 progress report

**Project:** Lahore Air Intelligence — AI-Driven Analysis and Prediction of Air Pollution in Lahore, Pakistan
**Author:** Syed Aown Raza Naqvi, Lahore, Pakistan
**Date:** November 2026
**Status:** Independent research, early stage. Not peer reviewed.

---

## Why I started this

I live in Lahore. Every winter the city disappears into smog, schools close, and the air is officially hazardous to breathe. I wanted to move from "everyone knows Lahore's air is bad" to understanding *when* and *why* it gets worse, and whether computer science can help warn people before the worst days arrive.

My research question is:

> How do seasonal and meteorological conditions influence PM2.5 concentrations in Lahore, and can machine learning predict short-term changes?

## What I did this week

1. **Read the background literature** on the causes of Lahore's smog (vehicles, brick kilns and industry, crop-residue and waste burning, regional transport, and the winter weather that traps it). Summary: `research/literature_review.md`.
2. **Collected real, open data** and wrote scripts so anyone can re-download it:
   - hourly PM2.5 from the **US Consulate Lahore reference monitor** (May 2019 – Feb 2025, 1,456 valid days after cleaning),
   - a **low-cost sensor** in Lahore (Nov 2023 – Aug 2026) and the **CAMS atmospheric model** (Aug 2022 – Nov 2026) for comparison,
   - **ERA5 weather** for 2019–2026, including boundary layer height,
   - **NASA satellite fire detections** for the Punjab region (2019–2025).
3. **Cleaned and merged** everything into one daily table, with documented quality-control rules (`data/README.md`). One example: the monitor reported ~8 µg/m³ for 1–10 February 2020, in the middle of smog season. That is not physically plausible, so I removed it as a likely sensor fault.
4. **Analysed** seasonal patterns, hour-of-day patterns and weather relationships (`notebooks/01_exploratory_analysis.ipynb`).
5. **Built a first forecasting baseline** for next-day PM2.5 (`notebooks/02_baseline_forecast.ipynb`).

## What I found

All numbers are from the US Consulate monitor unless stated otherwise.

**1. The air is unhealthy most of the year and extreme in winter.**
The average over all valid days was **132 µg/m³** (median 93). Of those 1,456 days, **99.5%** were above the WHO 24-hour guideline (15 µg/m³), **75%** were "Unhealthy" or worse on the US AQI scale (> 55.4 µg/m³), **32%** were "Very Unhealthy" or worse (> 150.4 µg/m³), and **14%** were "Hazardous" (> 250.4 µg/m³). The worst day was **14 November 2024 at 621 µg/m³**, about 41 times the WHO 24-hour guideline. This matches the value reported for the same event in a 2026 *Scientific Reports* study, which gave me confidence the data pipeline is correct.

An earlier draft of this report said 50%, 38% and 7%. That was a calculation error. The merged file is a complete daily calendar (2,876 rows), and the comparison treated a day with no measurement as a day below the threshold. Recomputed on the 1,456 days that actually have a measurement, the shares above are 99.5%, 74.7%, 31.9% and 14.2%. The notebook now drops missing days before the comparison.

**2. There is a strong, repeatable seasonal cycle.**
December (268 µg/m³) and November (254) are the worst months, and August (46) the cleanest — a **5.8× difference**. By season: winter Dec–Feb 223, post-monsoon Oct–Nov 188, spring 79, monsoon Jun–Sep 57 µg/m³.

**3. Winters are not getting better.**
Calendar-year averages are misleading because of gaps, so I compared the core smog season (Nov–Jan) of each winter: **212 µg/m³ (2019–20, 92 days)**, 224 (2020–21), 268 (2021–22, only 51 days), **269 (2023–24)** and **265 (2024–25)**. I can't call this a statistically proven trend with one monitor and six winters, but there is no sign of improvement.

**4. The "lid" is real: pollution builds up at night when the boundary layer collapses.**
In Nov–Jan, PM2.5 peaks around **midnight (~286 µg/m³)** and is lowest around **4 pm (~175 µg/m³)**. ERA5 shows the winter boundary layer is only about **50 m deep at night**, rising to about 850 m in the afternoon (compared with about 1,200 m in the monsoon). Days with a night-time boundary layer below 50 m averaged **191 µg/m³**, while days above 200 m averaged under 50 µg/m³.

**5. Ventilation, not just cold, separates bad days from very bad days.**
Over the whole year, PM2.5 is strongly linked to low minimum temperature (Spearman ρ = −0.71), high surface pressure (+0.71), low night boundary layer (−0.69), low wind (−0.48) and no rain (−0.47). But **within winter (Nov–Jan)**, temperature barely matters (ρ = −0.03) because every day is cold, while **night boundary-layer height (ρ = −0.65)** and **wind speed (ρ = −0.50)** still matter a lot. In winter, days with average wind below 4 km/h averaged **306 µg/m³**, against 134 µg/m³ on days above 10 km/h. In plain words, the weather decides how much of the city's pollution stays trapped near the ground.

**6. The autumn crop-fire season overlaps the smog onset — but fires alone don't explain it.**
Satellite fire detections in the Punjab region peak in **October–November** (rice stubble) and **May** (wheat). Only the autumn peak coincides with high PM2.5. In May, the deep, hot boundary layer disperses the smoke. In Oct–Nov, PM2.5 correlates moderately with the previous day's fire count (ρ = 0.41). Also, Oct–Nov fire detections fell by about **76%** from 2021 (22,180) to 2025 (5,243), while winter PM2.5 did not fall. This is consistent with the literature: fires add to the problem in autumn, but local emissions trapped by weather keep it severe all winter. (Caveat: the satellite misses evening fires, and published work suggests burning has shifted towards the evening.)

**7. Next-day PM2.5 is predictable, and weather information helps.**
Daily PM2.5 is very persistent (lag-1 autocorrelation 0.87), so "tomorrow = today" is already a strong baseline (MAE 35.2 µg/m³ on the 2023–2025 test period). Training only on 2019–2022 and testing on 2023–Feb 2025:
- Random Forest using only data up to today: MAE **31.8** (10% better than persistence).
- Random Forest also given tomorrow's weather: MAE **28.6**, R² = **0.84** (19% better than persistence).
- The most important input was the **change in night-time boundary-layer height from today to tomorrow**.
- My first XGBoost model did *not* beat persistence. It is not tuned yet, and with ~780 training days it probably over-fits.
- As an early-warning test, the model caught **93%** of "Very Unhealthy" days (> 150.4 µg/m³), against 89% for persistence.

Important caveat: "tomorrow's weather" here comes from reanalysis (what actually happened), not a real forecast, so real-world performance will be lower. Testing with archived weather forecasts is my next step.

## What I am *not* claiming

- I am **not** claiming which source (traffic, kilns, crop burning, industry) is the biggest. Weather correlations cannot answer that. It needs emission inventories or chemical source-apportionment studies, which I summarise in the literature review. Even there, results differ depending on which pollutants are counted.
- One monitor does not represent the whole city.
- The forecast results are preliminary, from one train/test split.

## Problems I ran into

- The OpenAQ API now needs a key, and the US State Department download site was unreachable, so I found the same monitor data in OpenAQ's public S3 archive.
- The consulate monitor has large gaps (most of summer 2022) and stops in early 2025.
- The CAMS model gets the timing right (r = 0.82) but **underestimates Lahore's PM2.5 by about half** (mean ratio 0.54). The low-cost sensor tracks the monitor closely (r = 0.98) but reads about 25% low overall.
- Boundary-layer height is missing in the weather archive for Jan–Jun 2024.

## Is this the model to use for the prediction?

Yes, for tomorrow's concentration at this monitor. The model to keep is the **Random Forest** that predicts the day-to-day change in log PM2.5 (`notebooks/02_baseline_forecast.ipynb`). On the 2023–Feb 2025 test period it is the lowest-error model in both feature sets. Untuned XGBoost is tied with "tomorrow = today" at best, so it is not the forecast. Full reasoning, including what this model cannot say about later years or about new controls: [`model_assessment.md`](model_assessment.md).

## What can reduce the smog?

The forecast says how high tomorrow will be if the city keeps emitting as it does now. The machines that can lower the risk, and the physical setting each one needs, are in [`mitigation_options.md`](mitigation_options.md). The size of the cut is in [`technology_risk_reduction.md`](technology_risk_reduction.md).

Short version, using the consulate record: if a person spends 18 hours of each Very Unhealthy day in a room where a purifier removes half the particles, and the Random Forest switches those machines on, about **22%** of their cumulative PM2.5 exposure goes away (about **13–31%** if the purifier removes 30% or 70% instead). The outdoor air is unchanged. The forecast itself adds about **1 percentage point** over the simpler rule "tomorrow = today"; the rest of the 22% is the purifier. At the source, a diesel particulate filter removes about **90%** of that engine's particles, and a zigzag kiln about **35%** of that kiln's PM2.5. Those source cuts are shares of an emissions inventory, not a 22% drop in the city monitor.

## Next steps

- **Week 2 — Machine learning:** walk-forward validation, tune XGBoost, use real archived weather *forecasts* as inputs, and try 2–3 day lead times. Calibrate the low-cost sensor and CAMS against the reference monitor so the record can continue after Feb 2025.
- **Week 3 — Prototype:** a simple public dashboard showing recent PM2.5, the forecast for tomorrow, and a warning level.
- **Week 4 — Write-up:** turn this into a short paper / preprint (e.g. on Zenodo, with a DOI) and share the code and data openly.
