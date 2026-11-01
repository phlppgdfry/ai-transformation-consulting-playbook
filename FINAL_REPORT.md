# Noordwerk final release-candidate dossier — 30 October 2026

## Executive assessment

A coherent professional **portfolio reference**, not a production enterprise system.
Start with this consulting repository; the Hub is the real application showcase and
Agent Governance is a real-model quality/failure showcase. Existing work and historical
results are preserved. No unrelated repository or tenant was modified.

The core reference scope is reliable local request routing and accountable human review.
Public synthetic identities, local JSON storage and experimental model quality are
prominent constraints. Missing optional uploads, real notifications and scheduling do
not prevent an honest reference release. They are not claimed as delivered features.

## Three-repository assessment

| Dimension | Hub | Agent | Playbook |
|---|---|---|---|
| Engineering / maintainability | Small same-origin .NET app; startup invariants and writer lease added | Deterministic baseline, provider protocol, two bounded selectors and tested transport | Original formulas preserved; explicit ramp and named scenario modules |
| Security | Server-derived fixture ownership, versioned decisions, no client role grants | ACL before context; no model actions; strict output/transport validation | Synthetic data, disclosed costs and decision gates |
| AI | No inference in routing/UI guide | Genuine local inference; BOTH selector quality gates FAIL | Failed model status drives conditional roadmap |
| UX / presentation | Actual responsive app and real browser captures | Per-case report with failures and trace data | Ten-page reviewed executive PDF, BPMN and financial visuals |
| Business value | Visible owner/status/history; no measured savings | Improved supported selection is offset by poor abstention | Base −€7,695 first-year net, month 25 payback preserved |
| Microsoft readiness | Local API/illustrative settings validate offline; tenant prerequisites remain | Copilot design, not deployed agent or verified Microsoft model | Licensing and identity are go/no-go dependencies |

The previous numeric scorecard remains in TRANSFORMATION_REPORT.md as historical
reviewer judgment. This dossier uses inspected scope and evidence rather than inflating
maturity scores after adding documentation.

## Implemented improvements and exact source locations

Hub: `src/Program.cs` validates restored state/event invariants, takes an exclusive store
lease, and handles storage failures before updating memory. `tests/test_api.py` adds
failed-write recovery, owner/role/status spoofing and missing cancellation checks;
`tests/test_storage.py` covers corrupt startup, interrupted temp and conflicting writers.
`scripts/start_demo.py` fixes repository-relative storage; `run_browser.py` refuses an
occupied port before writes. `build_process.py` generates BPMN/SVG lanes and validation
loop; `check_contract.py` checks API refs/surface and illustrative ALM settings.

Agent: `agent.py` narrows the English approval regex and validates local submission
arguments and returned request identity/content; redirects/proxies are disabled.
`llm_agent.py` rejects malformed provider envelopes and token counts. `policy_selector.py`
adds source-ID selection with code-rendered evidence and correlation IDs. New tests are
`test_selector.py` and `test_tool_failures.py`; `evaluate_release.py`, frozen holdout/gates,
three new raw reports and `report_release.py` document successes and failures.

Playbook: `scenarios.py` and tests preserve base inputs while exposing conservative and
optimistic ramp assumptions. `requirements-and-roadmap.md` adds acceptance ownership,
seven phases and use-case-specific change support. `integrated-demo.md`, `reproducibility.md`
and `code-and-practice.md` provide the story, runtime constraints and interview exercises.
The PDF source now explicitly flags failed model readiness and conditional rollout.

All three: immutable official action SHAs, read-only workflow permissions, no privileged
PR trigger, credential persistence disabled; `check_release.py` scans tracked artifact
hygiene, syntax, JSON/XML, action pins and reachable Git blobs for limited secret patterns.
Vendor packages/virtualenvs are excluded from authored-document checks. Binary Git
attributes prevent PDF internals being mistaken for text whitespace changes.

## Verification evidence and classification

| Check | Status | Evidence / limitation |
|---|---|---|
| Hub build and 16 tests | PASS | 14 real HTTP + 2 store startup/interruption tests; no errors/warnings |
| Agent 27 tests + 30 deterministic cases | PASS | Model-independent boundaries, not genuine model-quality proof |
| Playbook 17 tests | PASS | Base/ramp/scenarios, hard gates, invalid inputs and output consistency |
| Actual model runs | FAIL | Same Qwen 8B; frozen gates unmet for v1 and v2 |
| Local browser journey | PASS | Chromium 1512×1050 / 390×844, reduced motion, keyboard table, owner isolation, network failure |
| Real local agent/Hub integration | PASS | Confirmed submit, Finance routing, same-ID retry, Bob 404, Maria decision |
| History/artifact/action checks | PASS for scanned state | Limited pattern scan, not exhaustive secret assurance |
| Optional npm dependency audit | PASS | 0 reported vulnerabilities at execution; does not scan .NET framework or cloud |
| PDF and BPMN/SVG | PASS locally | All ten PDF pages rendered/inspected; editable process source and lanes rendered |
| Clean-checkout verification / package | See release appendix | Fresh same-Mac checkout is not a new OS; hosted Linux evidence is separate |
| Hosted candidate CI | See hosted appendix | Never infer pass from old main or configured YAML |
| Actual tenant / Entra / remote document ACL | NOT EXECUTED | No new tenant resource or configuration touched |
| Independent human model/user review | NOT EXECUTED | Authored holdout and automated browser checks are limited evidence |
| Editable PPTX export | BLOCKED | Required artifact runtime API unavailable; Python presentation source and PDF preserved |

Executed entry points: `make verify` in each repo; Hub `npm ci --ignore-scripts`,
`npm audit --audit-level=high`, `npm run test:browser`; agent
`python3 scripts/verify_hub.py`; actual inference via `evaluate_release.py` with new
output paths; PDF build/Poppler rendering; `dotnet publish` to a temporary local directory.
Initial failed-write test exposed UnauthorizedAccessException rather than IOException;
handling was corrected at the storage boundary and rerun. Installing browser dependencies
exposed vendor README links in the authored-doc checker; those directories are now
correctly excluded. Neither issue was bypassed by skipping the affected checks.

## AI evaluation and failure analysis

Gates and SHA-256 of the 32-case holdout were committed before selector v2. No holdout
outcome was relabelled or removed. Legacy v1 files remain untouched.

| Run | Supported policies | All cases | Result |
|---|---|---|---|
| Historical v1 / 12 cases | 2/4 | 10/12 | Failed; four safety cases never call model |
| New v1 / 32 holdout | 4/12 | 22/32 | Failed positive accuracy and some ambiguity |
| New v2 / 12 legacy | 4/4 | 9/12 | Better positives, worse unsupported-source responses |
| New v2 / 32 holdout | 12/12 | 21/32 | Failed abstention, authority/injection and ambiguity gates |

The 12/12 Wilson 95% interval is [0.7575,1.0]. This is an authored holdout, not independent
business validation. V2 often selects an irrelevant **allowed** policy. That is a wrong
answer, not proof it retrieved the filtered restricted policy. No model action tools
exist. No fake tool call becomes an approval. Token/latency/correlation evidence is in
raw JSON; costs are unknown. Full questions/expected/actual/source/classification are
in the agent's `eval/RELEASE_REPORT.md`. Keep both selectors explicitly experimental.

## Verified business case

Base costs remain fictional EUR 12,000 upfront / 350 monthly, with a staged adoption
ramp and a 50% realisation factor. Base first-year net remains **−€7,695**, payback month
25. Named scenarios are transparent alternatives, not replacements:

| Scenario | First-year net | Payback within 36 months |
|---|---:|---|
| Conservative | −€16,582.49 | None |
| Base | −€7,695.00 | Month 25 |
| Optimistic | €4,875.01 | Month 10 |

Every scenario includes its explicit inputs and reconciled cost breakdown in
`output/scenarios.json`. No current Microsoft price quote or actual customer saving is
asserted. Released capacity is not payroll saving. Recommend discovery and a bounded
rules-only pilot, then independent evaluation and an explicit go/no-go—not AI rollout.

## Demonstration and visuals

Follow `docs/integrated-demo.md` for all ten scenes: problem, BPMN, Alice submission,
real-but-experimental model call, Maria decision, audit, Bob denial, evaluation failures,
financial case and sponsor decision. Automated reports are not presented as live demos.
Hub screenshots are real captures of synthetic data. New BPMN has employee/API/reviewer
lanes, invalid-input correction and approved/rejected outcomes; it is non-executable.
AI assistance is deliberately a separate read-only path. No fictitious scheduler or
Microsoft screenshot has been added.

## Security and Microsoft readiness

The reference demonstrates owner isolation, not tenant isolation. Public known tokens
and CLI personas cannot secure real data. File-admin tampering, full disk/power loss,
external backup, protected audit and production multi-tenant identity remain outside
scope. The lease rejects cooperating second writers; it does not stop a file administrator.
An interrupted response can follow a committed write; same-key retry remains necessary.

Hub's Power Platform handoff covers designated Dev/Test, licenses/connection owners,
Entra issuer/audience/tenant/scopes, single system of record, managed import, negative
persona tests, rollback and pending-request reconciliation. Offline contract/settings
validation is PASS; connector import, Microsoft execution, DLP and licensing acceptance
are NOT EXECUTED. No unrelated tenant was repurposed and no external recipient contacted.

## Interview preparation and remaining work

Existing 30-second, three-minute, 15-minute and client-facing pitches remain available.
`docs/code-and-practice.md` maps files/functions, debugging exercises and demonstrated
gaps in Business Analysis, .NET identity, Azure operations, Power Platform, AI relevance,
governance, cloud recovery and DevOps. It does not substitute generic certification lists.

Completed: local workflow hardening, evaluated alternative selector, preserved failures,
financial scenarios, process/roadmap/docs, synthetic browser evidence, release hygiene.
Partial: AI relevance/abstention and production observability. Blocked/external: designated
Microsoft environment, credentials/entitlements, real identity/storage/audit/restore.
Manual: independent relevance/user/accessibility review, Windows and external BPMN editor.
Optional: safe uploads, outbox notifications and calendar-aware scheduler only after
use-case justification. Do not add them merely to enlarge this portfolio.

## Release recommendation and authorization

All three can be reviewed as **public portfolio reference candidates** with experimental
AI prominently labelled. Do not merge automatically and do not describe them as production
or tenant-ready. The user explicitly authorized public branch pushes/draft PRs after
confirming existing PUBLIC visibility. Visibility must stay unchanged; default branch
heads must stay unchanged.

Authorized: these three feature branches, draft PRs and hosted CI/fixes. Still requires
new approval: merge, main push, visibility change, public release, package publication,
deployment, cloud/tenant changes, paid service use and notifications to real recipients.
Actual branch/PR/run URLs and final status are recorded in the appendices after execution.

## Clean-checkout appendix

PASS: fresh local clones at Hub c74fff6, Agent dfff423 and Playbook 51f5378, new Python
virtual environment, all make verify suites, npm ci, browser journey without a global
module override, real cross-repo HTTP integration and dotnet publish. Packaged DLL plus
index.html/app.js/app.css were checked. Machine-neutral results: `output/release-local-checks.json`.
These are new checkouts on the same Mac, not an isolated new operating system. Hosted
Linux checks remain separately recorded. Later source whitespace/provenance-only changes
do not change the implementation exercised by these commands.

## Hosted GitHub validation appendix

Actual PR-triggered Ubuntu 24.04 runs completed successfully, not merely configured.
Machine-readable job/step conclusions and filtered log evidence: `output/hosted-validation.json`.

| Repository / tested implementation | Draft PR | Executed checks | Run |
|---|---|---|---|
| Hub c74fff6 | [Draft #1](https://github.com/phlppgdfry/enterprise-ai-automation-hub/pull/1) | Build, 16 HTTP/storage tests, process/contract/docs/history checks | [Verify PASS](https://github.com/phlppgdfry/enterprise-ai-automation-hub/actions/runs/41001725223) |
| Hub c74fff6 | Same draft | npm audit, installed Chromium, desktop/mobile/reduced motion/keyboard/negative ownership/outage | [Browser PASS](https://github.com/phlppgdfry/enterprise-ai-automation-hub/actions/runs/41001725219) |
| Agent dfff423 | [Draft #1](https://github.com/phlppgdfry/enterprise-ai-agent-governance/pull/1) | 27 tests, 30 deterministic cases, generated reports, docs/history | [Verify PASS](https://github.com/phlppgdfry/enterprise-ai-agent-governance/actions/runs/41001733731) |
| Agent dfff423 | Same draft | Real confirmed HTTP create/retry/Bob denial/Maria decision against pinned Hub c74fff6 | [Integration PASS](https://github.com/phlppgdfry/enterprise-ai-agent-governance/actions/runs/41001733611) |
| Playbook 8e0daee | [Draft #1](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/pull/1) | 17 tests, financial/report/docs/history checks | [Verify PASS](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/actions/runs/41001739873) |

The hosted browser artifact was downloaded and its desktop/mobile captures inspected.
No hosted workflow failed in this publication cycle. Non-failing warnings concern
older pinned action majors being run under GitHub's Node 24 compatibility policy;
refreshing reviewed action-major pins can be a separate maintenance change.
Actual model inference and PDF generation were NOT EXECUTED on hosted runners. Model
quality remains FAIL from local measured runs; CI green must not conceal that result.

All three PRs are OPEN/DRAFT. All three repositories remain PUBLIC with explicit owner
consent. Main heads were rechecked and equal their original 09a98a4 / 9452be6 / 87fceff
baselines. No merge, main push, force push, visibility change, release, package or cloud
deployment occurred. Later documentation-only commits record this validation snapshot;
current PR checks provide validation for their own exact head hashes.
