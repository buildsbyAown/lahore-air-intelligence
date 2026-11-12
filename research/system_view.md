# Lahore's air as a system: monitor, predict, intervene

*Lahore Air Intelligence — systems note, November 2026*

The measurements, the forecast and the machines are three parts of one problem. This note puts them in that order. It does not add a new model. It says what kind of system the project is already building, where a technology helps, and where it stops.

## The system

Lahore's winter smog is not one machine and not one number. It is a chain:

1. **Sources** put particles and gases into the air: vehicles, brick kilns, industry, crop-residue burning, waste burning, and pollution carried in from outside the district.
2. **The atmosphere** decides whether that material stays near the ground. In this dataset the deciding variables are a shallow night-time boundary layer and weak wind. Temperature, by itself, stops mattering once every day is already cold.
3. **Sensors** observe one point. The US Consulate monitor is the reference. A low-cost sensor and the CAMS model extend the record, with known biases.
4. **A forecast** turns today's observation and the weather into tomorrow's PM2.5, with a measured error.
5. **A decision** uses that forecast: run a room purifier, keep windows shut, or — for the outdoor air — change a kiln, an exhaust, or a fire.
6. **People** receive the result. A machine in a closed room protects the person in that room. A change at a chimney or a tailpipe is what can move the outdoor concentration.

A control action has to land on the part of the chain it can actually reach. Filtering the open sky does not reach it. That is why the mitigation note rejects city-scale outdoor purifiers, and why the same filter is useful in a room, a tailpipe or a kiln stack.

## What I have built on each part

| Part of the system | What this project does | Where |
|---|---|---|
| Observe | Clean hourly PM2.5, require 18 valid hours for a daily mean, and drop a sensor fault (1–10 Feb 2020, about 8 µg/m³ in the middle of smog season) | `data/README.md` |
| Explain | Seasonal cycle, night-time boundary layer, wind, fires | `notebooks/01_exploratory_analysis.ipynb` |
| Predict | Random Forest of the day-to-day change in log PM2.5. Test error 31.8 µg/m³ from observations alone, 28.6 µg/m³ if tomorrow's weather is known. Catches 93% of Very Unhealthy days | `notebooks/02_baseline_forecast.ipynb`, `research/model_assessment.md` |
| Decide | Switch exposure protection on when the forecast says the day will exceed 150.4 µg/m³ | `research/technology_risk_reduction.md` |
| Change the hardware | Room purifiers, diesel particulate filters, zigzag kilns and stack devices, each with the physical limit of that device | `research/mitigation_options.md` |

The February 2020 fault is worth naming as a monitoring problem, not only as data cleaning. A system that trusts a sensor without checking it will treat a broken instrument as clean air. The rule I used — a multi-day run below 15 µg/m³ in October–March is not plausible in Lahore — is a simple fault check. It is not yet a predictive-maintenance model of the monitor.
