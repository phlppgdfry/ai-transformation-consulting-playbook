import copy
import csv
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from playbook import ROOT, business_case, prioritise, report


class BusinessCaseTests(unittest.TestCase):
    def setUp(self):
        self.data = dict(monthly_volume=600, minutes_before=12, minutes_after=5,
            hourly_cost=45, adoption=.6, realisation=.5,
            implementation_cost=12000, monthly_operating_cost=350)

    def test_known_base_case(self):
        result = business_case(self.data)
        self.assertEqual(42, result["hours_saved_month"])
        self.assertEqual(1890, result["capacity_value_month"])
        self.assertEqual(945, result["realised_benefit_month"])
        self.assertEqual(595, result["net_benefit_month"])
        self.assertEqual(-4860, result["first_year_net"])
        self.assertEqual(-30, result["first_year_roi_pct"])
        self.assertEqual(20.17, result["payback_months"])

    def test_no_adoption_means_no_benefit(self):
        result = business_case(self.data, 0)
        self.assertEqual(0, result["hours_saved_month"])
        self.assertEqual(-350, result["net_benefit_month"])
        self.assertIsNone(result["payback_months"])

    def test_no_cash_realisation_still_has_capacity(self):
        self.data["realisation"] = 0
        result = business_case(self.data)
        self.assertEqual(1890, result["capacity_value_month"])
        self.assertEqual(0, result["realised_benefit_month"])

    def test_costless_case_has_no_roi_denominator(self):
        self.data.update(implementation_cost=0, monthly_operating_cost=0)
        self.assertIsNone(business_case(self.data)["first_year_roi_pct"])

    def test_invalid_inputs(self):
        for key, value in [("adoption", 1.01), ("realisation", -1), ("hourly_cost", float("nan")),
                           ("monthly_volume", float("inf")), ("minutes_after", 13),
                           ("implementation_cost", -1), ("adoption", True)]:
            with self.assertRaises(ValueError, msg=f"{key}={value}"):
                business_case(dict(self.data, **{key: value}))

    def test_sensitivity_is_monotonic(self):
        values = [business_case(self.data, a)["net_benefit_month"] for a in (.3, .6, .9)]
        self.assertEqual(values, sorted(values))


class PrioritisationTests(unittest.TestCase):
    def setUp(self):
        with (ROOT / "data/use-cases.csv").open(newline="") as source:
            self.rows = list(csv.DictReader(source))

    def test_gate_cannot_be_overridden_by_high_score(self):
        results = prioritise(self.rows)
        self.assertEqual("UC01", results[0]["id"])
        self.assertEqual({"UC04", "UC05"}, {r["id"] for r in results if r["decision"] == "blocked"})

    def test_duplicate_and_invalid_scores(self):
        with self.assertRaises(ValueError):
            prioritise([self.rows[0], self.rows[0]])
        for value in ("nan", "6", "0"):
            with self.assertRaises(ValueError):
                prioritise([dict(self.rows[0], risk=value)])

    def test_output_is_reproducible(self):
        self.assertEqual(report(), report())


if __name__ == "__main__":
    unittest.main(verbosity=2)
