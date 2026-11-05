import copy
import json
import unittest
from financial_model import cash_flow, report
from playbook import ROOT

class CashFlowTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'data/business-case.json').read_text())
        self.costs=json.loads((ROOT/'data/cost-breakdown.json').read_text())

    def test_breakdown_reconciles_and_ramp_reduces_value(self):
        result=cash_flow(self.data,self.costs)
        self.assertEqual(5400,result['current_monthly_labour_cost'])
        self.assertEqual(-350,result['cash_flow'][0]['net'])
        self.assertEqual(0,result['cash_flow'][0]['adoption'])
        self.assertLess(result['year_one_net_with_ramp'],result['baseline']['first_year_net'])
        self.assertGreater(result['payback_month_with_ramp'],20.17)
        self.assertEqual(result['cash_flow'][11]['cumulative'],result['year_one_net_with_ramp'])

    def test_no_ramp_matches_original_year_one(self):
        self.costs['ramp_adoption']=[]
        self.assertEqual(-4860,cash_flow(self.data,self.costs)['year_one_net_with_ramp'])

    def test_no_adoption_has_no_payback(self):
        self.data['adoption']=0
        self.costs['ramp_adoption']=[]
        self.assertIsNone(cash_flow(self.data,self.costs)['payback_month_with_ramp'])

    def test_invalid_ramp_and_unreconciled_costs(self):
        for ramp in [[float('nan')],[1.1],[-.1],[True]]:
            with self.assertRaises(ValueError):cash_flow(self.data,dict(self.costs,ramp_adoption=ramp))
        self.costs['monthly']['ai_consumption_allowance']=999
        with self.assertRaises(ValueError):cash_flow(self.data,self.costs)

    def test_sensitivity_includes_unfavourable_cases(self):
        result=report()
        self.assertEqual(9,len(result['sensitivity']))
        self.assertLess(min(r['first_year_net'] for r in result['sensitivity']),-10000)

    def test_committed_report_matches_inputs(self):
        self.assertEqual(report(),json.loads((ROOT/'output/investment-case.json').read_text()))
