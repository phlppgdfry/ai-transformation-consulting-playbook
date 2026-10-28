"""Reproducible consulting calculations. All example values are assumptions."""
import argparse
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def number(data, key, low=0, high=None):
    value = data[key]
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{key} must be a finite number")
    if value < low or (high is not None and value > high):
        raise ValueError(f"{key} outside allowed range")
    return value


def business_case(data, adoption=None):
    monthly_volume = number(data, "monthly_volume")
    before = number(data, "minutes_before")
    after = number(data, "minutes_after")
    rate = number(data, "hourly_cost")
    active = number(data, "adoption", 0, 1) if adoption is None else number({"adoption": adoption}, "adoption", 0, 1)
    realisation = number(data, "realisation", 0, 1)
    upfront = number(data, "implementation_cost")
    recurring = number(data, "monthly_operating_cost")
    if after > before:
        raise ValueError("minutes_after cannot exceed minutes_before in this savings model")
    hours = monthly_volume * (before - after) / 60 * active
    capacity = hours * rate
    benefit = capacity * realisation
    net = benefit - recurring
    first_year = 12 * net - upfront
    year_cost = upfront + 12 * recurring
    return dict(adoption=active, hours_saved_month=round(hours, 2), capacity_value_month=round(capacity, 2),
                realised_benefit_month=round(benefit, 2), net_benefit_month=round(net, 2),
                first_year_net=round(first_year, 2),
                first_year_roi_pct=round(first_year / year_cost * 100, 2) if year_cost else None,
                payback_months=round(upfront / net, 2) if net > 0 else None)


def prioritise(rows):
    results = []
    ids = set()
    for row in rows:
        identity = row["id"].strip()
        if not identity or identity in ids:
            raise ValueError("Use-case IDs must be present and unique")
        ids.add(identity)
        scores = {key: float(row[key]) for key in ("value", "feasibility", "readiness", "risk")}
        for key in scores:
            number(scores, key, 1, 5)
        if row["human_owner"] not in ("yes", "no") or row["data_permission"] not in ("yes", "no"):
            raise ValueError("Gate fields must be yes or no")
        blocked = row["human_owner"] != "yes" or row["data_permission"] != "yes" or scores["risk"] == 5
        score = .4 * scores["value"] + .3 * scores["feasibility"] + .2 * scores["readiness"] + .1 * (6 - scores["risk"])
        results.append(dict(id=identity, name=row["name"], score=round(score, 2),
                            decision="blocked" if blocked else "candidate"))
    return sorted(results, key=lambda r: (r["decision"] == "blocked", -r["score"], r["id"]))


def report():
    assumptions = json.loads((ROOT / "data/business-case.json").read_text())
    with (ROOT / "data/use-cases.csv").open(newline="") as source:
        ranking = prioritise(csv.DictReader(source))
    return dict(disclaimer="Fictional case; assumptions, not client results or vendor quotes.",
                assumptions=assumptions, base=business_case(assumptions),
                sensitivity=[business_case(assumptions, adoption) for adoption in (.3, .6, .9)],
                ranking=ranking)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write JSON; stdout when omitted")
    args = parser.parse_args()
    result = json.dumps(report(), ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result)
    else:
        print(result, end="")


if __name__ == "__main__":
    main()
