# One Noordwerk case, three audiences

**Noordwerk Portfolio v1.0 — Showcase Candidate.** A fictional 140-person technical
services company needs a clearer route for materials, expenses and application-access
requests. This is inspectable portfolio work, not evidence of employment, real workshops,
customer deployment or realised savings. Start at [the completion record](../PORTFOLIO_FINAL.md).

## The story in two minutes

Email intake makes ownership, status and approval reasons hard to follow. The case
maps requirements and stakeholders, then selects deterministic routing because category
and amount rules do not need AI. The .NET application executes the employee-to-reviewer
workflow. A separate Python project tests policy assistance; its real models fail quality
gates. The financial model includes costs and adoption, preserves negative year-one
value and recommends discovery plus a bounded rules-only pilot rather than full rollout.

| Audience | What to inspect | Evidence-backed conclusion |
|---|---|---|
| Business / Functional Analyst | [Requirements and acceptance](requirements-and-roadmap.md), [BPMN](../process/), [stakeholders](case-brief.md), [investment assumptions](financial-assumptions.md), [adoption](adoption-and-measurement.md) | Trace the problem through rules, owner, acceptance test, cost and go/no-go decision |
| AI & Automation Consultant | [Agent evaluation](https://github.com/phlppgdfry/enterprise-ai-agent-governance/blob/portfolio/noordwerk-showcase/eval/RELEASE_REPORT.md), [quality gates](https://github.com/phlppgdfry/enterprise-ai-agent-governance/blob/portfolio/noordwerk-showcase/eval/QUALITY_GATES.md), [Microsoft boundary](https://github.com/phlppgdfry/enterprise-ai-automation-hub/blob/portfolio/noordwerk-showcase/power-platform/README.md) | Explain rules versus AI, poor abstention, human authority and unverified tenant work |
| Technical reviewer | [Hub source](https://github.com/phlppgdfry/enterprise-ai-automation-hub/blob/portfolio/noordwerk-showcase/src/Program.cs), [HTTP/storage tests](https://github.com/phlppgdfry/enterprise-ai-automation-hub/tree/portfolio/noordwerk-showcase/tests), [code map](code-and-practice.md), [reproducibility](reproducibility.md) | Inspect owner checks, idempotency, atomic replacement, conflicts, recovery and exact test boundaries |

## Five-minute demonstration

Prepare using [the tested setup](integrated-demo.md#preparation). Keep port 5088 free for
isolated tests. The walkthrough needs no model installation, account or paid service.

| Time | Show | Say |
|---|---|---|
| 0:00–0:45 | This case and the AS-IS/TO-BE process | The fictional problem is unclear handoffs. Volume and time savings are assumptions |
| 0:45–2:00 | Alice submits an expense for EUR 320 | Category/amount rules choose Finance; the request remains pending |
| 2:00–3:00 | Maria reviews, records a reason and decides; Alice opens history | A human fixture decides; the server validates role and current version |
| 3:00–3:30 | Switch to Bob; Alice's request is absent | This is owner isolation under public fixtures, not production authentication or tenant isolation |
| 3:30–4:15 | Current model evaluation report | Both gates fail. No model action tools are exposed; valid citations can still be irrelevant |
| 4:15–5:00 | Base cash flow and executive recommendation | Year-one net is −EUR 7,695; payback month 25 under assumptions. Start smaller and measure |

If the API is unavailable, show recovery guidance and restart with the same store; do
not pretend a prerecorded result is live. Rehearsal uses synthetic data. For a fresh
rehearsal, set `HUB_DATA` to a new file path rather than deleting existing requests.
Repeated seeding uses stable keys. Closing a form does not cancel a submitted request.

## Ten-minute review

Use the five-minute flow, then spend one minute on each of the following:

1. Requirements: select BR1/FR2 in the acceptance map and trace to a screen and test.
2. Persistence: explain `Commit`, the writer lease and `ValidateRestored`; show the
   failed-write and restart tests. File administrators can still edit history.
3. AI quality: compare supported-question success with abstention/ambiguity failures.
   Pre-model refusals do not demonstrate model reasoning. Optional genuine inference
   is a separate experiment; omit it when Ollama is absent.
4. Delivery: use the seven-phase roadmap, RACI and support/adoption criteria. The
   Power Platform handoff is design plus offline checks, not a verified tenant solution.
5. Decision: explain capacity versus realised value, cost allowances and scenarios.
   A negative result can justify simplifying or stopping. Take one technical question.

## Suggested interview questions and defensible answers

| Question | Answer and evidence |
|---|---|
| Why avoid AI for request routing? | Known category/amount rules are deterministic; the API and routing-boundary tests implement them directly |
| Can someone approve by changing the browser role? | The server maps its public fixture token to identity/role and checks `Decide`. Fixture tokens themselves are not production credentials |
| What happens after a timeout? | The write might already have committed. Reuse the same owner/key/payload; tests prove a retry returns the original ID |
| Is the JSON store production-ready? | No. The local lease, atomic replace and invariant checks support this reference; protected audit, database transactions and recovery acceptance remain future work |
| Did the revised model pass? | No. V2 is 12/12 on supported holdout questions but only 21/32 overall and fails the nonanswer/ambiguity gates. See the unchanged raw reports |
| Are the economics real savings? | No. Synthetic assumptions yield −EUR 7,695 in year one and month-25 payback. Released capacity is not automatic payroll reduction |
| Does the case prove Microsoft delivery experience? | No Noordwerk tenant deployment occurred. It demonstrates contracts, architecture and a handoff that still needs actual licensing, identity, import and acceptance evidence |
| What can I claim personally? | That I can demonstrate and explain this portfolio implementation and reproduce its evidence after practising. Real client facilitation, independent delivery experience and production operations require separate truthful evidence |

Use [the code map and exercises](code-and-practice.md) to practise explaining the files
rather than memorising a pitch. Existing [timed project explanations](interview-guide.md)
and [ten-scene technical demo](integrated-demo.md) remain supporting material.
