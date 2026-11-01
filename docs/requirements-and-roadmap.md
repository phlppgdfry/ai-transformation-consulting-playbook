# Requirements and gated transformation roadmap

Noordwerk is fictional. Business-facing entry point: this repository. The Hub is the
application reference; Agent Governance is a separate, experimental policy-quality case.

| Requirement | Owner | Acceptance / evidence |
|---|---|---|
| BR1: know request owner and status | Operations | Employee submits and retrieves only own records; Hub HTTP/browser tests |
| FR1: deterministic routing | Finance / IT | Access €0 → IT; >€250 → Finance; otherwise Operations |
| FR2: accountable human decision | Process owner | Pending → approved/rejected once; separate identity, reason, current version |
| FR3: recover after transport failure | Delivery lead | Retry same owner/key/payload gives same ID; conflicting payload 409 |
| NFR1: local durability | IT | Atomic replacement, corrupt startup rejection, failed-write invariants, restart tests |
| NFR2: usable on desktop/mobile | Change lead | Browser task completion and keyboard checks; full manual accessibility review pending |
| SEC1: no client-granted privilege | IT | Owner/role/status injection cannot set authoritative fields; negative HTTP tests |
| DATA1: synthetic metadata only | Privacy owner | No files, HR records, real email delivery or production credentials |
| AI1: approved relevant evidence | Policy owners | Frozen holdout quality gates; v1/v2 remain experimental until all gates pass |
| VALUE1: economically justified rollout | Sponsor / Finance | Refresh ramp cash flow with measured adoption/time/cost; negative base not concealed |

## Seven delivery phases

| Phase | Accountable / technical owner | Work and dependencies | Decision gate |
|---|---|---|---|
| 0 Discovery | Sponsor / analyst | Observe ten requests, time active work versus waiting; establish rights and licensing | Signed problem, owner and learning budget |
| 1 Process validation | Operations / analyst | Walk AS-IS and TO-BE; identify incomplete, duplicate and disputed cases | Staff and Finance agree rules and exceptions |
| 2 Controlled prototype | IT / engineer | Local synthetic app, negative access tests, frozen model evaluation | Reproducible workflow; model status disclosed |
| 3 Limited pilot | Operations / platform owner | Designated tenant, genuine identity, transactional data and support; five users | IT accepts real negative-access and recovery tests |
| 4 Independent evaluation | Finance / evaluator | Held-out questions reviewed independently, observed user tasks, costs and time | Model/safety gates and value assumptions independently reviewed |
| 5 Go/no-go | Sponsor / IT + Finance | Compare measured value, licensing and risk to approved cap | Scale, simplify to rules-only, defer or stop |
| 6 Conditional gradual rollout | Operations / service owner | Small cohorts, training, monitored incidents, rollback and named deputy | Expand only while KPI/security thresholds remain met |

This supersedes the earlier six-week planning outline as a decision sequence, not a
promise that tenant work fits six weeks. Production/tenant work has not been executed.

## Change and support tied to the request process

Operations demonstrates one request in the existing team meeting and names queue owners.
Finance explains the €250 routing boundary and decision-reason expectation. IT explains
that access approval is not automatic account provisioning. Each of five pilot employees
practises submit/status/error recovery; the reviewer practises stale-version handling.

Before pilot: sponsor explains the problem and spending cap, not a headcount-reduction
promise. During pilot: a champion collects confusing fields and missing policy answers
weekly, without copying confidential conversations. Reviewers report queue overload.
After evaluation: Finance shares actual time/rework and cost; sponsor records the choice.

Resistance is investigated as a process issue: is the form duplicating email, is a queue
unowned, or is review too slow? Remove duplicate work before prescribing extra training.
Support owner and deputy handle failed connections, questionable policy and lost status;
IT owns security incidents. Manual intake remains the contingency until recovery is proven.
Metrics use transaction denominators, active minutes, waiting p90, rework and realised
capacity. Page views and model invocation totals are not adoption or savings measures.
