# Sponsor decision brief

Noordwerk is fictional. These are proposed decisions and synthetic assumptions, not
workshop findings or a customer endorsement. Read the executive PDF alongside the
reproducible financial inputs, not as a deployment approval.

## Recommendation

Authorise discovery and a rules-only pilot, subject to a sponsor-approved spending cap.
Do not authorise a full rollout or autonomous AI decisions. The original steady-state
model is negative in year one (€-4,860). Including two months without benefit and a
staged adoption ramp gives €-7,695 in year one and month 25 payback. Capacity released
is not a reduction in payroll unless a separate plan makes that value real.

## Options and tradeoffs

| Option | Benefit | Cost / delivery risk | Decision |
|---|---|---|---|
| Improve email process | Lowest platform dependency; standard form and named queue owners | Manual follow-up and audit reconciliation remain | Baseline alternative; measure first |
| Rules-only request pilot | Reliable routing, clear ownership and history | Requires supported identity, persistence and a suitable platform | First technical increment |
| Power Platform implementation | Business-maintainable forms/flows; Dataverse permissions and ALM | Licensing, tenant ingress, connection ownership and environment constraints | Choose only after entitlement review |
| Bounded policy assistant | Less policy searching; auditable sources | Model relevance, source ownership and recurrent evaluation effort | Separate experiment; no action authority |
| Bespoke autonomous platform | Broad flexibility | Excessive scope, operational burden and consequential-action risk | Reject for this company |

No option is preferred merely because it uses AI. The local Hub is a reference for
behaviour; production build-versus-buy remains an explicit discovery decision.

## Interview and discovery questions

- Operations: Show the last five delayed requests. How much time was active work versus waiting?
- Finance: Which decisions need independent approval? Which errors cause rework or financial loss?
- Employees: Where do you lose status? What would make the new form harder than email?
- IT: Which environments and entitlements exist? Who owns connection identities and support?
- Policy owners: Who can publish, revoke and review a source? How are restricted documents protected?
- Sponsor: What work will released hours enable? What pilot cost can be written off if it fails?

## Risks and ownership

| Risk | Likelihood / impact | Control | Accountable owner | Exit evidence |
|---|---|---|---|---|
| Savings fail to materialise | High / high | Measure time, adoption and realisation separately | Finance | Recalculated cash flow from observed data |
| Model selects irrelevant policy | Medium / medium | Source checks plus topic evaluation; abstain | Policy owner | At least 90% reviewed supported-question accuracy; proposed gate |
| Employee reads another record | Medium / high | Entra + server/data-layer ACL; real persona tests | IT | Negative access tests in Test |
| Connector identity becomes unavailable | Medium / high | Approved ownership and renewal/runbook | Platform owner | Disable/recover exercise and alternate owner |
| Duplicate action after timeout | Medium / high | Stable owner-scoped idempotency key | Delivery lead | Timeout/retry returns same request |
| Public demo mistaken for production | Medium / high | Persistent labels, evidence statuses, no real data | Portfolio owner | Review README, UI and artifacts |
| Poor adoption or inaccessible UI | Medium / medium | Task observation, keyboard and mobile review | Change lead | Five users complete tasks; manual validation pending |
| Unsafe tenant policy change | Low / high | Scoped environment; no blanket DLP relaxation | Tenant admin | Exported reviewed policy and connector tests |

## Process ownership and exceptions

Operations owns intake; Finance owns monetary review; IT owns access. Current bottleneck
hypotheses are missing fields, uncertain queues and approval waiting. Rules remove the
first handoff search; they do not remove a reviewer's workload. Missing fields return
validation errors. Access requests must be €0. A stale decision must be refreshed.
Timeouts reuse the original submission key. Unknown policy questions go to the policy
owner. Requests older than two working days require manual follow-up until a calendar-aware
escalation flow has been deployed and tested. No request disappears because AI is unavailable.

## Delivery gates and handover

| Stage | Work | Exit / stop criterion |
|---|---|---|
| Discovery | Baseline, data and licensing inventory, owners, option choice | Signed scope and budget; otherwise stop |
| Proof of concept | Local employee-to-approver flow, synthetic policy experiment | Reproducible tests and visible failure paths |
| Pilot preparation | Real identity, queue RBAC, data store, ALM, support | Security acceptance in separate Test environment |
| Pilot | Five employees, training, two-week comparison | Measure denominator, time, errors, adoption and cost |
| Production decision | Refresh ROI; review security and model gates | No rollout on a negative unaccepted case or failed safety gate |
| Handover | Owner and backup, monitoring, restore drill, incident channel | Support can recover without the original maker |
| Continuous improvement | Monthly source, cost and KPI review | Re-evaluate any prompt/model/source/connector change |

The six-week plan in `delivery-roadmap.md` is a planning hypothesis. Dependencies can
extend it. No retrospective, interview, sign-off or user feedback has been fabricated.
