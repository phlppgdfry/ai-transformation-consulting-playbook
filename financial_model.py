"""Auditable monthly cash-flow extension. Assumptions, not investment advice."""
import argparse
import json
from pathlib import Path
from playbook import ROOT, business_case, number


def cash_flow(data, costs):
    upfront=sum(number(costs['implementation'],key) for key in costs['implementation'])
    recurring=sum(number(costs['monthly'],key) for key in costs['monthly'])
    if abs(upfront-data['implementation_cost']) > .001 or abs(recurring-data['monthly_operating_cost']) > .001:
        raise ValueError('Cost breakdown must reconcile to the original business case')
    horizon=costs['horizon_months']
    if isinstance(horizon,bool) or not isinstance(horizon,int) or not 12<=horizon<=120:
        raise ValueError('Horizon must be 12–120 integer months')
    ramp=costs['ramp_adoption']
    if not isinstance(ramp,list) or len(ramp)>horizon:
        raise ValueError('Invalid adoption ramp')
    for adoption in ramp:
        number({'adoption':adoption},'adoption',0,1)
    cumulative=-upfront
    rows=[]
    payback=None
    for month in range(1,horizon+1):
        adoption=ramp[month-1] if month<=len(ramp) else data['adoption']
        result=business_case(data,adoption)
        cumulative+=result['net_benefit_month']
        rows.append(dict(month=month,adoption=adoption,benefit=result['realised_benefit_month'],
                         operating_cost=recurring,net=result['net_benefit_month'],cumulative=round(cumulative,2)))
        if payback is None and cumulative>=0:
            payback=month
    first_year=rows[11]['cumulative']
    sensitivity=[]
    for adoption in (.3,.6,.9):
        for operating in (200,350,600):
            result=business_case(dict(data,monthly_operating_cost=operating),adoption)
            sensitivity.append(dict(adoption=adoption,monthly_operating_cost=operating,
                                    first_year_net=result['first_year_net'],payback_months=result['payback_months']))
    current_hours=data['monthly_volume']*data['minutes_before']/60
    benefit_at_full_adoption=business_case(data,1)['realised_benefit_month']
    return dict(disclaimer=costs['disclaimer'],baseline=business_case(data),
                current_monthly_labour_cost=round(current_hours*data['hourly_cost'],2),
                assumptions=dict(cost_breakdown=costs,horizon_months=horizon,
                 timing='Upfront at month 0; recurring costs from month 1; ramp then steady adoption.',
                 exclusions=['Tax','Discounting','Inflation','Seasonality','Vendor price changes']),
                year_one_net_with_ramp=first_year,
                year_one_roi_pct_with_ramp=round(first_year/(upfront+12*recurring)*100,2) if upfront+12*recurring else None,
                payback_month_with_ramp=payback,
                steady_first_year_break_even_adoption=round((upfront/12+recurring)/benefit_at_full_adoption,4) if benefit_at_full_adoption else None,
                cash_flow=rows,sensitivity=sensitivity,
                recommendation='Fund discovery and a bounded rules-only pilot; do not approve full rollout from this unmeasured scenario.')


def report():
    return cash_flow(json.loads((ROOT/'data/business-case.json').read_text()),
                     json.loads((ROOT/'data/cost-breakdown.json').read_text()))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT/'output/investment-case.json')
    args=parser.parse_args()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report(),indent=2,allow_nan=False)+'\n')
    r=report()
    print(f"Year one with ramp: EUR {r['year_one_net_with_ramp']:,.0f}; payback month: {r['payback_month_with_ramp']}")
