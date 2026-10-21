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
