"""How much PM2.5 exposure machinery and the forecast can cut.

Reads data/processed/lahore_daily_merged.csv and writes
models/technology_risk_reduction.csv.

Personal exposure on a day is the outdoor daily mean, reduced only during the
hours spent in a room with a running purifier:

    exposure = outdoor * (1 - hours/24 * indoor_reduction)

The purifier is switched on only when the day is Very Unhealthy
(PM2.5 > 150.4 µg/m³). A warning misses some of those days, so the
reduction is multiplied by the warning's recall from the test set
(Random Forest 0.931, persistence 0.889; see notebooks/02_baseline_forecast.ipynb).

This is not a chemical-transport forecast of the outdoor concentration.
Source-machinery rows are shares of primary PM2.5 in the Urban Unit
inventory, not shares of the monitor reading.
"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "processed", "lahore_daily_merged.csv")
OUT = os.path.join(ROOT, "models", "technology_risk_reduction.csv")

VERY_UNHEALTHY = 150.4
WHO_ANNUAL = 5.0
# Held-out test, notebook 02: share of days above 150.4 that each rule caught.
RECALL = {"perfect hindsight": 1.0, "Random Forest [A]": 0.931, "persistence": 0.889}
# Urban Unit (2023) Table 3, directly emitted PM2.5, tonnes. See literature review.
PRIMARY_PM25_T = {"transport": 397, "crop-residue burning": 371, "waste burning": 320, "industry": 29}
# Illustrative only. IQAir 2024 annual mean and the AQLI Lahore figure.
IQAIR_ANNUAL_2024 = 102.1
AQLI_YEARS = 5.8


def load_pm25():
    values = []
    with open(DATA) as f:
        for row in csv.DictReader(f):
            if row["pm25_consulate"]:
                values.append(float(row["pm25_consulate"]))
    return values


def exposure_reduction(values, hours, indoor_reduction, recall):
    """Fraction of the sum of daily means removed. Missing days are excluded."""
    total = sum(values)
    saved = 0.0
    for pm in values:
        if pm > VERY_UNHEALTHY:
            saved += pm * (hours / 24.0) * indoor_reduction * recall
    return saved / total


def main():
    values = load_pm25()
    total = sum(values)
    bad = [pm for pm in values if pm > VERY_UNHEALTHY]
    primary_total = sum(PRIMARY_PM25_T.values())
    rows = []

    rooms = [
        ("School day, published classroom result (~32%)", 6, 0.32),
        ("School day, round 40% indoor cut", 6, 0.40),
        ("Home, 12 hours, weak purifier (30%)", 12, 0.30),
        ("Home, 12 hours, typical purifier (50%)", 12, 0.50),
        ("Home, 12 hours, strong purifier (70%)", 12, 0.70),
        ("Home and school, 18 hours, weak purifier (30%)", 18, 0.30),
        ("Home and school, 18 hours, typical purifier (50%)", 18, 0.50),
        ("Home and school, 18 hours, strong purifier (70%)", 18, 0.70),
    ]
    for label, hours, reduction in rooms:
        for warning, recall in RECALL.items():
            frac = exposure_reduction(values, hours, reduction, recall)
            rows.append({
                "kind": "personal exposure",
                "scenario": label,
                "warning": warning,
                "hours_in_treated_room": hours,
                "indoor_reduction": reduction,
                "result_pct": round(100 * frac, 1),
                "unit": "percent of summed daily PM2.5 on measured days",
            })

    # Device-level and inventory-level source controls. Not additive with the rows above.
    source_rows = [
        ("Diesel particulate filter, at that engine", 90, "percent of that engine's particulate matter"),
        ("Zigzag kiln vs fixed-chimney Bull's trench, at that kiln", 35, "percent of that kiln's PM2.5"),
        ("Zigzag applied to the inventory's whole industry line (29 t)", round(100 * 0.35 * 29 / primary_total, 2), "percent of inventory primary PM2.5"),
    ]
    for diesel_share in (0.40, 0.60, 0.80):
        tonnes = 0.90 * diesel_share * PRIMARY_PM25_T["transport"]
        source_rows.append((
            f"DPF at 90% on {int(diesel_share * 100)}% of transport primary PM2.5",
            round(100 * tonnes / primary_total, 1),
            "percent of inventory primary PM2.5",
        ))
    for name, tonnes in PRIMARY_PM25_T.items():
        source_rows.append((
            f"Remove the entire '{name}' primary-PM2.5 line",
            round(100 * tonnes / primary_total, 1),
            "percent of inventory primary PM2.5, a ceiling if that source stopped",
        ))
    for label, result, unit in source_rows:
        rows.append({
            "kind": "source machinery",
            "scenario": label,
            "warning": "",
            "hours_in_treated_room": "",
            "indoor_reduction": "",
            "result_pct": result,
            "unit": unit,
        })

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    mean = total / len(values)
    print(f"measured days: {len(values)}")
    print(f"mean PM2.5: {mean:.1f} µg/m³")
    print(f"days above {VERY_UNHEALTHY}: {len(bad)} ({100 * len(bad) / len(values):.1f}%)")
    print(f"share of summed PM2.5 on those days: {100 * sum(bad) / total:.1f}%")
    print(f"primary PM2.5 in the inventory: {primary_total:.0f} t")
    central = exposure_reduction(values, 18, 0.50, RECALL["Random Forest [A]"])
    # Scale only as an illustration: apply the exposure cut to the IQAir annual mean.
    new_annual = IQAIR_ANNUAL_2024 * (1 - central)
    gap_closed = (IQAIR_ANNUAL_2024 - new_annual) / (IQAIR_ANNUAL_2024 - WHO_ANNUAL)
    print(f"central exposure cut (18 h, 50%, Random Forest): {100 * central:.1f}%")
    print(f"if that percent applied to the 2024 annual mean of {IQAIR_ANNUAL_2024}: {new_annual:.1f} µg/m³")
    print(f"share of the gap from {IQAIR_ANNUAL_2024} down to {WHO_ANNUAL}: {100 * gap_closed:.1f}%")
    print(f"proportional slice of the {AQLI_YEARS}-year AQLI figure: {AQLI_YEARS * gap_closed:.2f} years")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
