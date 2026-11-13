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

## Prediction is a control signal, not a cure

The Random Forest is a statistical model of a system I cannot fully control. I cannot choose tomorrow's boundary-layer height. I can choose whether a purifier is running when that layer collapses.

On the test set the model is modestly better than "tomorrow = today": about 10% lower error from observations alone, and 15 missed Very Unhealthy days instead of 24. When that warning switches an 18-hour, 50%-effective purifier, about **22%** of cumulative exposure on the measured days is avoided. Replacing the naive warning with the Random Forest adds about **1 percentage point** of that 22%. The particles are removed by the machine. The model chooses the day.

That split matters. A more accurate forecast does not, by itself, lower anyone's dose. It lowers the dose only when a person or a plant acts on it. The error bar also stays in the decision: an MAE of about 32 µg/m³ means a day forecast at 140 µg/m³ can still land above or below the 150 µg/m³ line. The warning is a rule under uncertainty, not a certainty.

## Where the machinery sits in the life of the pollution

Each machine acts at a different point. Putting them in one "technology" bucket hides that.

| Point in the chain | Machine | What it changes | Scale already estimated |
|---|---|---|---|
| In the room, after the pollution exists | HEPA purifier | The air one person breathes, for the hours the machine runs | About 22% of personal exposure in the central case (13–31% across purifier strengths) |
| In the tailpipe, before the pollution spreads | Diesel particulate filter; catalytic converter on petrol engines | That vehicle's exhaust | About 90% of that diesel engine's particles. About 13–26% of Lahore's directly emitted PM2.5 if diesel is 40–80% of transport's primary PM2.5 |
| In the kiln, in the way the bricks are fired | Zigzag conversion | Fuel use and the kiln's own PM2.5 | About 35% less PM2.5 at that kiln, and about 30% less energy per brick, in the UET Lahore study |
| On the kiln chimney | Scrubber, baghouse or electrostatic precipitator | The flue that is still dirty after the firing change | Large for coarse dust; weak for the smallest particles unless the device is a real filter, not a screen |
| Instead of a fire | A seeder that lets farmers sow without burning residue; waste collection | The source itself | Up to the inventory share of that source (about 33% and 29% of primary PM2.5), only if the burning actually stops |

Environmental effect and social effect are not the same cut. The 22% protects people who have a machine and spend the smog hours indoors. People in the street, and people in rooms with no purifier, keep the outdoor concentration. A kiln or an exhaust change is slower and smaller in the city monitor, and it is the change that does not depend on who can buy a purifier. A sustainable design has to count both: the fast protection of exposure, and the slower cut in emissions. It also has to count cost and whether the device stays in service. A filter removed because the fuel is wrong, or a kiln renamed zigzag and not rebuilt, contributes nothing.

I am not claiming a single life-cycle assessment. The zigzag study already compares energy, PM2.5 and CO₂ for two kiln designs. I have not done that for purifiers or for a vehicle fleet. The numbers above are exposure shares and inventory shares, calculated in `src/mitigation_scenarios.py`.
