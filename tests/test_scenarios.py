import json
import unittest
from playbook import ROOT
from scenarios import report

class ScenarioTests(unittest.TestCase):
    def test_base_remains_original_and_named_cases_are_ordered(self):
        scenarios=report()['scenarios'];base=scenarios[1]
        self.assertEqual(-7695,base['first_year_net'])
        self.assertEqual(25,base['payback_month'])
        self.assertLess(scenarios[0]['first_year_net'],base['first_year_net'])
        self.assertGreater(scenarios[2]['first_year_net'],base['first_year_net'])
        self.assertEqual(12000,base['inputs']['implementation_cost'])

    def test_generated_output_is_current(self):
        self.assertEqual(report(),json.loads((ROOT/'output/scenarios.json').read_text()))
