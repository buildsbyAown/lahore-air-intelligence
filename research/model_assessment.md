# Is this the right model for future PM2.5 in Lahore?

*Lahore Air Intelligence — model check, November 2026*

The project needs a prediction of how high fine-particle pollution will be in Lahore. This note checks the models already trained in `notebooks/02_baseline_forecast.ipynb` against that job. I did not train a new model. The numbers below are the held-out test results already saved in `models/baseline_results_test_2023_2025.csv` and in the notebook output.

## What "future pollution" means here

Two different questions get mixed together.

1. **Tomorrow's concentration, with emissions like the recent past.** Given today's PM2.5 and the weather, what will the daily mean be at the US Consulate monitor?
2. **A later year, or a year after new controls.** What will the concentration be in 2030, or after exhaust filters and kiln changes are actually in place?

The models in this repository answer question 1. They have no input for a new policy, a new vehicle fleet, or a room purifier, so they cannot answer question 2. Question 2 is taken up separately in [`mitigation_options.md`](mitigation_options.md).

## The model to use

**Use the Random Forest. Predict the change in log PM2.5 from today to tomorrow, then apply that change to today's measured value.**

That is the lowest-error model in the test (trained on May 2019–December 2022, tested on January 2023–February 2025, no shuffling):

| Model | What it is allowed to see | MAE (µg/m³) | RMSE | R² | Better than "tomorrow = today" |
|---|---|---:|---:|---:|---:|
| Tomorrow = today | today's PM2.5 | 35.2 | 55.4 | 0.76 | — |
| Monthly climatology | the calendar month | 48.3 | 73.3 | 0.57 | worse |
| Ridge, observations only [A] | pollution and weather up to today | 33.0 | 53.5 | 0.77 | 6% |
| **Random Forest, observations only [A]** | same | **31.8** | 51.6 | 0.79 | **10%** |
| XGBoost, observations only [A] | same | 34.9 | 55.6 | 0.75 | about 0 |
| Ridge, plus tomorrow's weather [B] | [A] plus the next day's reanalysis weather | 28.7 | 46.7 | 0.83 | 18% |
| **Random Forest, plus tomorrow's weather [B]** | same | **28.6** | 44.5 | 0.84 | **19%** |
| XGBoost, plus tomorrow's weather [B] | same | 35.5 | 54.5 | 0.76 | worse |

Which of the two Random Forests to publish depends on what information exists at the moment of the forecast:

- **A forecast issued tonight, before tomorrow's weather is known, should be Random Forest [A].** It uses only information that already exists: recent PM2.5, today's weather, the day of the year, and recent fire counts. Test error is 31.8 µg/m³, against 35.2 for guessing that tomorrow equals today.
- **Random Forest [B] is the model to move to once a real weather forecast is wired in.** It is the most accurate run in the table (MAE 28.6 µg/m³, R² 0.84). The weather it was given, though, is ERA5 reanalysis: a reconstruction of the weather that *did* happen, including the change in night-time boundary-layer height from today to tomorrow. A forecast issued in advance will not know that change exactly, so 28.6 is an upper bound on skill, not the error a live system would have today.

Untuned XGBoost is not the forecast. On observations only it is tied with "tomorrow = today" (MAE 34.9 against 35.2). When tomorrow's weather is added it is worse than that guess. With about 780 training days it needs a proper tuning pass before it can be reconsidered.

## Why this formulation fits Lahore

Daily PM2.5 at this monitor is very persistent (lag-1 autocorrelation 0.87). Any useful model has to beat "tomorrow = today". The Random Forest does, by a modest amount from observations alone and by more once tomorrow's ventilation is known.

The models are trained on the *change* in the log of PM2.5, not on the level itself. Tree models cannot invent values outside the range they saw in training, and the November 2024 episode (621 µg/m³) was worse than the training years. Modelling the change, then applying it to today's measured value, lets the forecast move with the weather without pretending the tree has seen that extreme before.

The input that matters most in feature set B is the change in night-time boundary-layer height. That matches the exploratory result: inside winter, a shallow night-time layer and weak wind are what separate a bad day from a very bad day. The model is picking up the physical "lid", not a spurious calendar effect. Monthly climatology, which only knows the month, is the worst predictor in the table.

## As a warning, observations-only is enough

On the test set, 216 days were "Very Unhealthy" or worse (PM2.5 > 150.4 µg/m³).

| Rule | Days caught | Days missed | False alarms |
|---|---:|---:|---:|
| Tomorrow = today | 89% | 24 | 23 |
| Random Forest [A] | 93% | 15 | 18 |
| Random Forest [B] | 93% | 15 | 24 |

For a yes/no health warning, Random Forest [A] catches the same share of bad days as [B] and raises fewer false alarms. It also does not depend on tomorrow's weather. For the *number* of micrograms, [B] is better. A dashboard can show the [A] warning now, and replace the concentration with [B] when a genuine weather forecast is available.

## What this model is not

- **It is a one-day forecast at one site.** The target is the next daily mean at the US Consulate monitor. It has not been tested at 2–3 days ahead, at another neighbourhood, or as a city-average.
- **It assumes emissions stay in the range of 2019–2025.** A large, real change in traffic, kilns, burning, or fuel will shift the level, and the model will keep predicting the old regime until it is retrained on the new one.
- **It has no lever for a purifier, an exhaust filter, or a kiln chimney.** Those devices do not appear in the feature list. Putting them into this Random Forest would be theatre. Their expected effect is discussed from the emissions literature in the mitigation note, and it is labelled as that, not as a model output.
- **Feature set B is not yet an operational weather forecast.** Replacing reanalysis with archived forecast weather is the next modelling step, already on the roadmap. Until that test exists, the honest error bar for a live next-day level is the [A] result, about 32 µg/m³ MAE.
- **One chronological split is a preliminary test.** Walk-forward validation is still to do. The ranking (Random Forest ahead of persistence, XGBoost not) is stable enough to choose a model. It is not a final uncertainty estimate.

## Correction that does not change the model

While checking the study I found a separate error in the written shares of unhealthy days. The first draft said 50% of days exceeded the WHO 24-hour guideline and 7% were hazardous. The code had averaged the comparison over the whole calendar, and a missing day counted as a clean day. On the 1,456 days with a real measurement the shares are **99.5%** above 15 µg/m³, **74.7%** above 55.4, **31.9%** above 150.4, and **14.2%** above 250.4. The forecast metrics above were always computed on days that have both today and tomorrow, so this bug did not enter the model scores. The notebook and the Week 1 report are corrected.

## Decision

Keep the Random Forest as the prediction model. Use feature set A for any number released before tomorrow's weather is known. Treat feature set B as the design target for the version that takes a real weather forecast. Leave XGBoost for a later tuning pass. Do not ask this model to estimate air purifiers, exhaust filters, or kiln controls.
