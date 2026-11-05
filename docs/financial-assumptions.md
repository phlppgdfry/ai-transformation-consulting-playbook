# Financial assumptions and sensitivities

`financial_model.py` extends, rather than changes, the original `playbook.py` model.
Inputs: `data/business-case.json` plus `data/cost-breakdown.json`. Output:
`output/investment-case.json`. Every amount is fictional, EUR excluding tax.

- Current labour capacity cost: 600 × 12/60 × €45 = €5,400/month.
- Implementation: discovery 1,500; delivery 5,500; security 1,800; adoption 1,200;
  contingency 2,000 = €12,000. These are allowances, not a supplier estimate.
- Recurring: licensing 110; AI 20; hosting 40; maintenance 180 = €350/month.
  Five pilot employees plus reviewers are assumed. Entitlements must be confirmed.
- AI allowance: 200 policy questions × assumed €0.10 = €20. This is not a current
  Microsoft or model-provider price. Local measured tokens cannot establish cloud cost.
- Maintenance: assumed four hours × €45. Hosting is a separate planning allowance.
- Adoption ramp: months 1–2 zero, month 3 20%, month 4 40%, thereafter 60%.
  Recurring cost starts in month 1; benefits only begin as adoption rises.

The extension reports year-one net €-7,695 and payback in month 25. Its 36 monthly
rows show the cumulative balance including upfront cost. Payback is first non-negative
month, not a discounted or fractional result. The original 20.17-month payback assumes
immediate steady benefits and is not directly interchangeable with the ramp result.

Nine steady-state scenarios cross adoption (30/60/90%) with monthly operating cost
(€200/350/600). They deliberately show unfavourable outcomes. First-year break-even
adoption at base costs is approximately 85.71% without a ramp; the ramp raises the hurdle.
No taxes, financing, inflation, seasonality or discounting are modelled. Missing volumes,
realisation and vendor quotes prevent an actual investment decision.
