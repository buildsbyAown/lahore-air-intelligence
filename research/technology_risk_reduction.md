# How much of the risk can technology cut?

*Lahore Air Intelligence — quantified mitigation, November 2026*

The forecast predicts tomorrow's PM2.5. The machinery removes particles, either in a room or in a flue. This note puts a number on each, from the consulate record and from published device efficiencies. The arithmetic is in `src/mitigation_scenarios.py` and the full table is `models/technology_risk_reduction.csv`. Device evidence and citations are in [`mitigation_options.md`](mitigation_options.md).

## The figure to quote

**About 22% of cumulative PM2.5 exposure** on the 1,456 measured days, for a person who spends 18 hours of each Very Unhealthy day (above 150.4 µg/m³) in a room where a purifier removes half the particles, with the Random Forest turning the machines on.

The same schedule with a weaker or stronger purifier is **13% to 31%**. A school-only programme, six hours at the classroom result of about 32–40% removal, is **about 5–6%**.

That 22% is personal exposure. It is the share of the summed daily means the person no longer breathes. The outdoor monitor does not fall by 22%, because the particles are still in the street.

## How the 22% is calculated

On the measured days the mean is **132 µg/m³**. Days above 150.4 µg/m³ are 465 of 1,456 days (32%), and they hold **62.5%** of the summed PM2.5. Those are the days the warning switches the purifiers on.

For the hours in the treated room, exposure is the outdoor concentration times one minus the indoor reduction. Other hours stay at the outdoor concentration. The Random Forest caught **93.1%** of Very Unhealthy days in the test set, so 6.9% of those days get no protection.

Central case:

- 18 / 24 of the day in the treated room
- 50% removal while it is running (the US EPA's summary of home studies is about 50% or higher)
- 93.1% of the bad days actually warned
- 62.5% of total PM2.5 sits on those days

18/24 × 0.50 × 0.931 × 0.625 = **0.218**, which is 21.8%, reported above as about 22%.

| Where the purifier runs | Indoor cut | Warning | Share of measured exposure removed |
|---|---:|---|---:|
| School, 6 hours | 32% | Random Forest | 4.7% |
| School, 6 hours | 40% | Random Forest | 5.8% |
| Home, 12 hours | 50% | Random Forest | 14.6% |
| Home and school, 18 hours | 30% | Random Forest | 13.1% |
| Home and school, 18 hours | 50% | Random Forest | **21.8%** |
| Home and school, 18 hours | 70% | Random Forest | 30.6% |
| Home and school, 18 hours | 50% | tomorrow = today | 20.8% |
| Home and school, 18 hours | 50% | every bad day known in advance | 23.5% |

Assumptions, all of which make the 22% an upper-side estimate for a real household:

- Before the purifier runs, the room is as polluted as the outdoor daily mean. A closed room is often already lower, so the machine's extra cut is smaller.
- The machine is the right size, the windows stay mostly shut, and the filter is maintained. Those conditions are the same ones in [`mitigation_options.md`](mitigation_options.md).
- Hours outside the treated room are spent at the full outdoor concentration.
- The 1,456 days are the days the monitor reported. Summers are missing more often than winters, so bad days are a larger share of this sample than of a complete calendar.

## What the computer-science model adds

The Random Forest does not remove particles. Its job is to decide which day the machinery should run, and to say how high the outdoor number will be.

On the central package, "tomorrow = today" already removes **20.8%** of exposure, because pollution is persistent and a bad today is usually a bad tomorrow. The Random Forest removes **21.8%**. The model itself adds **about 1 percentage point**.

That 1 point is real: in the test the model missed 15 Very Unhealthy days and the persistence rule missed 24, out of 216. It is also small next to the 22%. The large computer-science contribution is the warning system existing at all. With no warning, the 22% does not happen, unless the purifiers run blindly every day. The separate gain in the concentration number — 10% lower error than persistence using data up to today, 19% when tomorrow's weather is known — is accuracy of the forecast, not a further cut in exposure. Details are in [`model_assessment.md`](model_assessment.md).
