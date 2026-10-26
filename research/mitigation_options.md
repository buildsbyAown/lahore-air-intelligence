# What would actually lower Lahore's smog?

*Lahore Air Intelligence — mitigation note, November 2026*

The forecast in this project predicts tomorrow's PM2.5 if the city keeps emitting as it does now. This note is the other half of the study: which of the controls people ask for can reduce the problem, and which physical setting each one needs. I cover the three that were requested — room air purifiers, cleaners on vehicle exhausts, and cleaners at the mouths of brick kilns — and I apply the same test to the other large particle sources already in the literature review.

I only use numbers from the project data or from sources listed at the end. Where a percentage comes from a paper, it is the paper's result for that device or that kiln, not a prediction of Lahore's city-wide concentration.

## The test a control has to pass

A filter removes particles from the air that passes through it. That helps when the air is enclosed long enough for the machine to treat it:

- a room, with the door and windows mostly shut;
- a tailpipe, where all of that vehicle's exhaust goes through one duct;
- a kiln chimney, where the flue gas goes through one stack.

The same filter, stood in a street or a park, treats a trickle of air while the wind replaces the city's air and the sources keep emitting. Outdoor "smog towers" fail that test. Guttikunda and Jawahar (2020) put it directly for Delhi: the airshed has no walls, so vacuuming outdoor air and releasing it back into the same air does not clean the city [1]. Delhi's own pollution-control committee later told the National Green Tribunal that the towers' measured effect was about 13–15% within 200 m, against a design claim of 1 km [2].

Lahore's winter lid does not change this. In the project data, the night-time boundary layer in November–January averages **53 m** (median 38 m, 399 days). Consider a footprint of 40 km by 40 km, which is the order of Lahore District, a 50 m lid, and the winter mean wind in the same data, **6 km/h**:

- air flowing through that box ≈ 40,000 m × 50 m × 6,000 m/h = **1.2 × 10¹⁰ m³ every hour**;
- a large demonstration tower, the 10 million m³/day scale used in the Delhi calculation [1], treats about **4 × 10⁵ m³/h**;
- one such tower therefore treats about **0.003%** of the air moving through the city;
- matching that flow once would take on the order of **30,000** towers, while kilns, vehicles and fires kept adding particles inside the box.

The exact area can be twice as big or half as big and the conclusion is the same. A shallow boundary layer makes each kilogram of emissions *more concentrated*. It does not turn the city into a room that one machine can filter. The forecast's main weather signal — the night-time boundary layer collapsing — is a reason to cut emissions and to protect people indoors on those days. It is not a reason to build outdoor purifiers.

## 1. Room air purifiers (HEPA)

**What they change.** The concentration in the room where the machine runs.

**What they leave alone.** The outdoor air, the street, and every room that does not have a machine.

Portable HEPA cleaners do reduce indoor PM2.5 when they are sized for the room and the room is closed. A review of portable purifiers in homes, schools and offices found indoor PM2.5 reductions between **22.6% and 92%** across the studies it included [3]. A second review of real-world personal filtration found reductions of about **11% to 82%** [4]. The US EPA's summary of home studies is "on the order of approximately 50 percent or higher" for high-efficiency portable cleaners [5]. A classroom trial in Los Angeles measured **39.9%** lower school-year PM2.5 with portable HEPA units, in a year when outdoor PM2.5 was only about 8–10 µg/m³ [6]. Another school trial found a **32%** indoor reduction and fewer absences; the effect on absences was smaller when outdoor pollution was higher [7].

None of those trials is Lahore. This project has no indoor measurements, so I do not claim a Lahore reduction. The honest use of the monitor record is to show the outdoor level a purifier would be fighting.

On the 1,456 valid consulate days (23 May 2019–17 Feb 2025):

| Period | Valid days | Mean PM2.5 | Share above 15 µg/m³ (WHO 24-h) | Share above 150.4 | Share above 250.4 |
|---|---:|---:|---:|---:|---:|
| All measured days | 1,456 | 132 | 99.5% | 32% | 14% |
| November–February | 526 | 230 | 100% | 76% (398 days) | 37% (196 days) |

November–February holds **63%** of the sum of daily means, and **86%** of the days above 150.4 µg/m³. That is the season when a purifier programme would run. On those 398 November–February days above 150.4, the outdoor mean was **266 µg/m³**. If a closed room started at that outdoor level and a purifier then held a reduction in the published range:

| Indoor reduction, if the room starts at 266 | Indoor PM2.5 |
|---:|---:|
| 30% | 186 |
| 50% | 133 |
| 70% | 80 |

All three are still many times the WHO 24-hour guideline of 15 µg/m³. A purifier in a Lahore winter is harm reduction for the people inside that room. It is not a way to make the air safe, and it does nothing for anyone outside. It only holds those reductions if the machine is big enough for the room (the usual rule is a clean-air delivery rate that replaces the room's air several times an hour), the windows stay mostly shut, and the filter is replaced when it loads up. Lahore's winter cold helps the "windows shut" condition. An open window, or a machine that is off, removes the benefit.

**How this connects to the forecast.** Random Forest [A] caught 93% of Very Unhealthy days in the test set and can be issued from data that already exist (see [`model_assessment.md`](model_assessment.md)). That flag is a switch for schools, hospitals and homes: run the purifiers, keep windows closed, move sport indoors. The flag does not lower the outdoor number.
