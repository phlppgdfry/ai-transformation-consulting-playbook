# Noordwerk Portfolio v1.0 — Showcase Candidate

**Portfolio complete for its stated reference scope. Engineering verified locally and
in hosted CI. Model experiments remain experimental; this is not a production deployment.**

Noordwerk is a fictional 140-person technical services company. Materials, expenses and
access requests arrive by email, leaving owners, status and decisions unclear. The case
connects requirements and process analysis to a working application, an honest AI
experiment and an investment decision. All people, operational data and financial inputs
are synthetic; no client engagement or realised saving is claimed.

## One case, three independently maintainable repositories

| Stage / repository | Actual scope | Final classification |
|---|---|---|
| [Decide — Consulting Playbook](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/tree/portfolio/noordwerk-showcase) | Requirements, BPMN, stakeholders, cost/ramp/scenarios, roadmap, adoption and executive PDF | **A — Portfolio-ready** |
| [Deliver — Automation Hub](https://github.com/phlppgdfry/enterprise-ai-automation-hub/tree/portfolio/noordwerk-showcase) | Employee submission, rule routing, human review, owner-filtered status/history and local persistence | **A — Portfolio-ready** |
| [Govern — Agent Governance](https://github.com/phlppgdfry/enterprise-ai-agent-governance/tree/portfolio/noordwerk-showcase) | Deterministic reference, confirmed local HTTP tool and genuine local-model evaluation with preserved failures | **B — Technically verified but model-backed features experimental** |

There is no material blocker to reviewing this as a portfolio. The failed model gates
block business use of the model path, not publication of accurately labelled experiments.

## Review in five or ten minutes

Use the central [audience walkthrough](docs/portfolio-walkthrough.md): one story for a
Business/Functional Analyst, AI & Automation Consultant or technical reviewer. It includes
five- and ten-minute timings, interview questions and evidence-backed answers.

For a live demonstration, clone the three repositories beside one another and check out
`portfolio/noordwerk-showcase`. Requirements: .NET 10 SDK, Python 3.11+ and Make. From the Hub:

```bash
make verify
python3 scripts/start_demo.py
# Second terminal, same repository:
python3 scripts/seed_demo.py
```

Open `http://127.0.0.1:5088/`. Alice submits an expense for EUR 320; Maria records a reason
and decides; Alice views history; Bob cannot access Alice's request. Routing is fixed
business logic and every decision remains human. Stop the server before isolated test
suites. Seeding is repeatable and does not erase data. A fresh `HUB_DATA` path provides
a separate rehearsal store; there is no destructive reset requirement.

No model installation is required. The default agent demonstration is
`python3 agent.py ask 'Wat is het onkostenbeleid?'`. Follow the [full demo and failure
rehearsal](docs/integrated-demo.md) and [runtime/troubleshooting guide](docs/reproducibility.md).

## Technology and verification

The Hub uses ASP.NET Core 10, same-origin HTML/CSS/JavaScript and a single-process JSON
store. The agent and financial calculations use Python's standard library. Ollama/Qwen
are optional local experiments; Playwright is an optional locked browser-test dependency.
ReportLab is optional for PDF regeneration. There is no paid/cloud prerequisite for the
core demonstration and no fourth repository or application.

| Evidence | Verification boundary |
|---|---|
| Hub `make verify` | 14 real HTTP + 2 storage tests; idempotency, ownership, human authority, concurrency, restart, corruption and failed-write recovery; contract/process/docs/history checks |
| Agent `make verify` | 27 model-independent tests and 30 deterministic cases; generated evaluation reports; no model calls |
| Playbook `make verify` | 17 financial/prioritisation/output tests; docs, syntax and limited history/credential checks |
| Hub `npm run test:browser` | Real desktop/mobile, reduced-motion, keyboard table, decision history, owner isolation and network-failure journey |
| Agent `python3 scripts/verify_hub.py` | Real local HTTP submission/retry/Bob denial/Maria decision against the built Hub |
| Clean checkout / package | Fresh clones, new Python environment, lockfile installation and compiled .NET/static-file package; documented in the [evidence dossier](FINAL_REPORT.md) |

Use the [consolidation audit](CONSOLIDATION_AUDIT.md), [detailed prior verification and
hosted evidence](FINAL_REPORT.md#verification-evidence-and-classification) and current PR
checks for exact tested commits. Historical reports retain their dates and must not be
mistaken for the latest run. The audit records this pass's actual checks and limits.

Drafts: [Hub #1](https://github.com/phlppgdfry/enterprise-ai-automation-hub/pull/1),
[Agent #1](https://github.com/phlppgdfry/enterprise-ai-agent-governance/pull/1),
[Playbook #1](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/pull/1).

## Business and AI conclusions

Authoritative business deliverables are the [requirements/roadmap](docs/requirements-and-roadmap.md),
[stakeholders](docs/case-brief.md), [BPMN](process/), [options/risk register](docs/engagement-decision.md),
[RACI](docs/delivery-roadmap.md), [adoption/KPIs](docs/adoption-and-measurement.md) and
[ten-page executive PDF](deliverables/noordwerk-executive-brief.pdf).

The [36-month base case](output/investment-case.json) remains **−EUR 7,695 in year one,
payback month 25**. [Named scenarios](output/scenarios.json) expose conservative and
optimistic assumptions; [cost drivers](docs/financial-assumptions.md) are not vendor quotes.
Capacity released is not automatic payroll saving. Recommend discovery and a bounded
rules-only pilot, with measured adoption, cost and an explicit go/no-go decision.

**EXPERIMENTAL — QUALITY GATES NOT PASSED.** The frozen 32-case holdout records v1 at
4/12 supported questions and 22/32 overall; v2 at 12/12 supported but 21/32 overall.
V2 worsens abstention and ambiguity. Source-ID validity does not guarantee relevance.
[Full failure analysis and raw evidence](https://github.com/phlppgdfry/enterprise-ai-agent-governance/blob/portfolio/noordwerk-showcase/eval/RELEASE_REPORT.md)
remain unchanged. The authored holdout is not independent human validation. Human
permission and decisions remain outside the model; the model has no action tools.

## Production boundary and optional future work

Public fixture tokens and CLI personas are not real authentication or tenant isolation.
The JSON store is adequate for the tested local reference, not replicated production
storage, protected audit or a verified backup system. Full accessibility/user review,
Windows validation and independent model review are not complete. Microsoft components
are [integration designs and offline contracts](https://github.com/phlppgdfry/enterprise-ai-automation-hub/blob/portfolio/noordwerk-showcase/power-platform/README.md),
not a Noordwerk tenant deployment. These are documented limits, not hidden release claims.

Real identity, tenant licensing, transactional storage and recovery acceptance would be
separate production work. Uploads, delivered notifications and scheduling are optional
future use cases. They are not required to close this portfolio; do not expand the scope
merely because they are possible.

## Suggested GitHub presentation and owner actions

Pin these three existing repositories, ordered Playbook → Hub → Agent. Until the owner
merges, use the candidate branch links above when sharing: repository landing pages still
show their unchanged default-branch READMEs. Historical metadata recommendations:

| Repository | Description | Topics |
|---|---|---|
| Playbook | Fictional AI transformation case: requirements, BPMN, reproducible investment scenarios, adoption and executive decision brief. | business-analysis, digital-transformation, change-management, ai-governance, portfolio |
| Hub | Local .NET request and human-approval workspace with tested ownership, safe retries, persistent history and a Microsoft integration handoff. | dotnet, aspnet-core, workflow-automation, business-analysis, power-platform, portfolio |
| Agent | Deterministic policy reference and experimental local-model evaluations with frozen quality gates, safe tool boundaries and preserved failures. | ai-evaluation, ai-governance, ollama, python, portfolio |

The final publication pass applied owner-authorized descriptions and additional topics,
retaining existing topics. Profile pins and visibility were not changed. See the current
[v1 closure and merge handoff](NOORDWERK_V1_CLOSURE.md). No owner action is required
to use the reviewed branches as a portfolio candidate. If incorporating into default
branches later: review each draft and exact-head checks; merge Hub first, then Agent and
Playbook; preserve the reviewed history and pinned Hub integration commit; update candidate
cross-links after merging before deleting branches. Merging and changing draft status
remain owner decisions. Do not infer a tag or GitHub Release from this version label.

## Closure recommendation

**Close Noordwerk Portfolio v1.0 for now.** The stated scope is coherent, demonstrated,
reproducible and honestly bounded. Keep all PRs draft/unmerged in this handoff. Further
engineering needs a concrete new objective rather than an indefinite improvement cycle.
