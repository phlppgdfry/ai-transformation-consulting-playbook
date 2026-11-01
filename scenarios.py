"""Named fictional ramp scenarios. Original base inputs and output remain unchanged."""
import copy
import json
from playbook import ROOT
from financial_model import cash_flow

def report():
    original=json.loads((ROOT/'data/business-case.json').read_text())
    original_costs=json.loads((ROOT/'data/cost-breakdown.json').read_text())
    choices=[('conservative',dict(monthly_volume=450,minutes_after=7,adoption=.3,realisation=.35),500,[0,0,0,.1,.2]),
             ('base',{},350,[0,0,.2,.4]),
             ('optimistic',dict(monthly_volume=750,adoption=.85,realisation=.65),300,[0,.2,.4,.6])]
    result=[]
    for name,changes,operating,ramp in choices:
        inputs=dict(original,**changes,monthly_operating_cost=operating)
        costs=copy.deepcopy(original_costs)
        costs['monthly']['maintenance_and_support']+=operating-original['monthly_operating_cost']
        costs['ramp_adoption']=ramp
        r=cash_flow(inputs,costs)
        result.append(dict(name=name,inputs=inputs,costs=costs,
            first_year_net=r['year_one_net_with_ramp'],first_year_roi_pct=r['year_one_roi_pct_with_ramp'],
            payback_month=r['payback_month_with_ramp']))
    return dict(disclaimer='Fictional scenarios, not forecasts, vendor quotes or changed base assumptions.',scenarios=result)
if __name__=='__main__':
    path=ROOT/'output/scenarios.json'
    path.write_text(json.dumps(report(),indent=2,allow_nan=False)+'\n')
    for s in report()['scenarios']:print(s['name'],s['first_year_net'],s['payback_month'])
