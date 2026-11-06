# Enterprise AI showcase audit

Baseline inspected 5 November 2026, before showcase implementation. This is a
presentation pass on the published Noordwerk case, not a new engineering programme.

## Current maturity and evidence

| Repository | Published main / PR #1 | Existing evidence | Assessment |
|---|---|---|---|
| Automation Hub | `a2c00b9`; merged | ASP.NET Core 10, authored UI, 16 HTTP/storage tests, real desktop/mobile screenshots and main browser acceptance | Working local reference; no production authentication |
| Agent Governance | `4496767`; merged | 27 tests, 30 deterministic cases, real HTTP integration, frozen model reports | Credible experiment; model quality gates FAILED |
| Consulting Playbook | `cf27ae7`; squash merged | 17 tests, reproducible forecast/scenarios, BPMN, RACI, roadmap, ten-page executive PDF | Business-facing entry with transparent assumptions |

All default branches are main, repositories are public and MIT licensed. Latest
main verification passed; Hub browser and Agent integration passed on their main
commits. See [publication evidence](https://github.com/phlppgdfry/enterprise-ai-automation-hub/actions/runs/42002805199),
[integration evidence](https://github.com/phlppgdfry/enterprise-ai-agent-governance/actions/runs/42002389177)
and [financial checks](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/actions/runs/42002516785).
Source inspected: Hub `src/Program.cs` and UI/architecture; Agent `agent.py`,
`llm_agent.py`, `policy_selector.py`; Playbook formulas, reports and existing guides.

## Strengths to preserve

- One fictional client with synthetic records; human decisions remain in the API.
- Verified agent-to-Hub HTTP submission exists, but there is no three-system runtime.
- Strong source/test/evidence navigation, diagrams, existing interview/code maps.
- Failed real-model results and negative economics are public rather than hidden.
- Credential-free deterministic demonstrations; no paid hosting prerequisite.
- AI assistance disclosed centrally; public demo tokens explicitly bounded.

## Presentation weaknesses and missing evidence

READMEs still use retained candidate-branch links and candidate labels after merging.
The Agent hero chart shows historical supported-question results rather than current
holdout totals. Hub/Agent lack their own explicit AI-assistance paragraphs. First-screen
audience and non-live demo routes can be more direct. Existing interview guides are
substantial; another generic guide would duplicate them unless it addresses ownership,
audience levels and independent learning specifically.

The personal site's source is accessible at local `pgosprive` (React/Vite, clean main,
remote `phlppgdfry/pgosprive`). Its project catalogue has another enterprise AI case but
no Noordwerk entries. Keep the two cases distinct. The public site could not be read by
the web tool; the native browser bridge also failed before navigation. Live visual parity
is therefore unverified; inspect a local preview before proposing publication. Do not
deploy. Existing branding is recoverable from the source.

The public GitHub profile has a substantial personal README and six existing pins:
Logistics-Master, portops-ai, ClickTrack, MirrorMate-App, docurelay-field and
fabric-lottery-data-platform. Preserve that breadth. Noordwerk has no obvious profile
entry. Recommend selective pin changes, not replacing the whole profile. Existing
other-project claims were observed, not independently audited in this task.

## Boundaries

Model v1 holdout 22/32; v2 21/32: both gates fail. Valid source IDs do not ensure
relevance. Deterministic tests do not measure model reasoning. Base year one remains
−EUR 7,695 with payback month 25; all financial inputs fictional. No production login,
protected audit, tenant deployment, user study, measured ROI or autonomous approvals.
Source/PDF/screenshot assets already exist; use them before creating more.

## Prioritised decisions

| Priority | Action | Scope |
|---|---|---|
| P0 Essential | Keep failed gates, financial loss, synthetic identities and AI assistance visible | README/current narrative only |
| P0 Essential | Clearly label conceptual links, verified HTTP integration and absent live service | One overview diagram and demo strategy |
| P1 High value | Current main navigation, short audience routes and current Agent evaluation graphic | Reuse architecture and screenshots |
| P1 High value | Website section as local review branch; profile addition as reviewable draft | No deployment/profile publication |
| P1 High value | Timed recording scripts and contribution-confirmation questions | Link existing detailed guides |
| P2 Optional | Record short demonstrations; observe real recruiter/user sessions | Requires owner participation |
| P2 Optional | Future read-only hosting after separate review | No current infrastructure action |
| P3 Unnecessary | New agents, dashboards, vector database, fourth repository, cloud identity rewrite | Excluded |

Audit complete. Implement only presentation, navigation, documentation and a local
website section. Keep runtime, financial inputs, prompts, frozen evaluation data and
historical evidence unchanged. Review branches must not merge or deploy automatically.
