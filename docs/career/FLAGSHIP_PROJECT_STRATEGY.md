# Flagship: Enterprise AI Automation Hub

Decision: lead with the **working Hub**, frame it with the Playbook, and use Agent
Governance as supporting evidence about AI reliability. The business-facing portfolio
entry remains this Playbook; the flagship demonstration is the application.

## Readiness verification — 6 November 2026

Main, merged PR #1, public README/source/assets and actual CI were inspected again.
Published heads remain Hub `a2c00b9`, Agent `4496767`, Playbook `cf27ae7`.
The later showcase branches are local proposals, not publicly merged improvements.

| Project | Classification | Employer-facing boundary |
|---|---|---|
| Hub | **READY** | Show as a tested local prototype with public synthetic identities, never production authentication |
| Playbook | **READY** | Show as a fictional business analysis and reproducible financial decision, not real client consulting |
| Agent | **READY WITH CONTEXT** | Show deterministic reference and preserved failed model evaluation; never a release-ready model |
| Proposed website section | **NOT READY for production publication** | Local preview works; full lint and dependency audit fail; no deployment approval |

All three core repos are MIT licensed; deterministic demonstrations require no paid cloud.
Hub/Agent AI-assistance paragraphs are prepared locally; the public central README already
discloses substantial AI support. Always disclose assistance verbally, regardless of entry page.

## Comparison

Scores 0–5 are this reviewer's judgments, not recruiter feedback or measured skill.

| Criterion | Hub | Agent | Playbook | Evidence / reason |
|---|---|---|---|---|
| Business relevance | 5 | 4 | 5 | Request handoffs are concrete; policy quality is a narrower supporting problem |
| Technical substance | 4 | 4 | 3 | Real API/persistence/HTTP tests; genuine model runs; executable formulas respectively |
| Visual demonstration | 5 | 3 | 4 | Actual employee/reviewer UI; Agent is CLI/reports; Playbook has executive PDF |
| Architectural clarity | 4 | 4 | 4 | Small authority boundaries; business decision is not runtime integration |
| Recruiter accessibility | 5 | 3 | 4 | See a request become a human decision in under two minutes |
| Credibility | 4 | 5 | 5 | Fixture/security boundaries explicit; failed gates/negative economics preserved |
| Reproducibility | 4 | 4 | 5 | Hub needs .NET; Agent default stdlib; Playbook stdlib and committed reports |
| Interview usefulness | 5 | 4 | 5 | Hub connects requirement, UX, API, failure, owner and value in one story |

## Business problem, audience and differentiators

Fictional Noordwerk has unclear ownership and reasons for email-based materials, expenses
and access requests. Target audience: functional/business analysts, implementation teams
and technical hiring managers hiring people to translate process needs into working systems.

The differentiator is restraint: rules handle known thresholds; a human retains authority;
negative tests and recoverable writes support the workflow; a separate AI experiment can
fail without corrupting the business decision. This is an AI-enabled transformation case,
but **the Hub's routing does not call an LLM**. Do not say it does.

Most persuasive evidence: [API source](https://github.com/phlppgdfry/enterprise-ai-automation-hub/blob/main/src/Program.cs),
[tests](https://github.com/phlppgdfry/enterprise-ai-automation-hub/tree/main/tests),
[published browser run](https://github.com/phlppgdfry/enterprise-ai-automation-hub/actions/runs/42002805199),
actual [workspace](https://github.com/phlppgdfry/enterprise-ai-automation-hub/blob/main/docs/assets/hub-overview.png)
and [approval](https://github.com/phlppgdfry/enterprise-ai-automation-hub/blob/main/docs/assets/hub-approval.png) captures.

## Reproducible five-minute demonstration

Clone the three public repos side by side and use main. Prerequisites: .NET 10, Python
3.11+, Make; no model or cloud account needed. In each repo run `make verify` while the
Hub is stopped. From Hub start the existing non-destructive demo:

```bash
# POSIX shell; this creates a separate synthetic rehearsal store.
DEMO_STORE_DIR="$(mktemp -d)"
HUB_DATA="$DEMO_STORE_DIR/requests.json" python3 scripts/start_demo.py
# Second terminal, in Hub:
python3 scripts/seed_demo.py
# Open http://127.0.0.1:5088/
```

Use Alice, Maria and Bob fixture identities. Submit title 'Site visit reimbursement',
category expense, EUR 320. Finance routing is deterministic; pending remains pending
until Maria supplies a reason and decides. Alice sees history; Bob cannot retrieve it.
Do not enter real financial/HR information. Existing fixtures are synthetic; seeding
does not erase data. Retain the temporary store if rehearsing restart behavior.

| Time | Show / recording narration |
|---|---|
| 0:00–0:30 | 'This AI-assisted fictional case starts with unclear email handoffs, not a need to add a chatbot.' |
| 0:30–1:00 | Requirements/BPMN: show requester, process owner, approver and one acceptance criterion |
| 1:00–2:15 | Alice submits EUR 320; point out Finance route and pending state; explain deterministic rules |
| 2:15–3:00 | Maria records a reason/decision; show Alice history and Bob's missing record |
| 3:00–3:45 | Show API/test evidence and separate Agent release report: both model gates failed; model has no decision tool |
| 3:45–4:30 | Playbook: −EUR 7,695 year one, payback month 25; recommend bounded pilot with measured adoption |
| 4:30–5:00 | Production boundary and AI support: real identity/storage/tenant acceptance remain; explain only contributions you can substantiate |

Screenshots above are recorded evidence, not proof a current server is live. See
[recording scripts](../portfolio/VISUAL_ASSETS_PLAN.md), [full demo](../integrated-demo.md)
and [code map](../code-and-practice.md). Owner narration/video remains unrecorded.

## Troubleshooting and honest fallback

Port 5088 occupied: stop your own previous rehearsal, never attach tests to an unknown
process. Missing SDK: install documented prerequisite, or show recorded UI and say so.
API outage: show recovery message; restart with the same store, don't assert a write
failed solely because the response was lost. Duplicate title: use another title; stable
keys may return an existing record. No Ollama: omit live inference; the deterministic
workflow and recorded failed evaluation remain usable. No internet: keep source/report/PDF
locally and label the demonstration local. Never replace a failed action with fake success.
