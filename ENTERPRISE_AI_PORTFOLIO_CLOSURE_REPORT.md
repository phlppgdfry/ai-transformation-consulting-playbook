# Enterprise AI portfolio showcase — review handoff

Completed locally 6 November 2026. Existing Noordwerk v1 main publication is preserved.
This later presentation pass is prepared on review branches, not merged or deployed.

## Executive summary

Make the existing strengths easier to inspect: business decision → tested automation →
honest model evaluation. The case remains fictional and substantially AI-assisted.
The working local API and confirmed HTTP integration are actual implementations; the
business relationship is conceptual and Microsoft's tenant handoff remains design-only.
No runtime feature, financial assumption, frozen dataset, prompt or model result changed.

## Repository changes

| Repository / branch | Prepared changes |
|---|---|
| Automation Hub / `showcase/recruiter-evidence` | README audience/demo route, main navigation, explicit AI-assistance disclosure; existing functionality/assets preserved |
| Agent Governance / `showcase/recruiter-evidence` | Same README improvements; current failed-holdout graphic derived from committed results; three actual CLI-output captures with matching text |
| Consulting Playbook / `showcase/recruiter-evidence` | Audit, narrative, four-view architecture guide, overview SVG, demo/visual strategies, visitor review, interview guide, profile draft and website handoff; current completion/walkthrough navigation |
| Website / `showcase/noordwerk-portfolio` | Dedicated local worktree `noordwerk-website-review`; localized section, three evidence cards, nav, architecture, explicit financial/AI/identity boundaries, copied existing assets and repaired manifest/lock mismatch |

Website edits were isolated when another workstream changed the original checkout.
Its accounting-case catalogue/image and sitemap edits were preserved and excluded.
No profile repository or unrelated source repository was modified. No new repository,
package, paid resource, outreach, deployment or release was created. New review branches
are local; no new PR or hosted-CI success is claimed for these commits.

## Demonstration status

**Working:** local Hub request/decision/history; deterministic agent; confirmed local
HTTP submission; financial/scenario calculations. **Recorded:** actual Hub screenshots,
three captured Agent command outputs, frozen model results and executive PDF.
**Prepared:** website section, three 90-second recording scripts, profile addition.
**Not implemented/published:** public live Noordwerk application, hosted model, finished
video, new Microsoft deployment or live website/profile updates.

[Demo strategy](docs/portfolio/DEMO_STRATEGY.md) and
[visual/recording plan](docs/portfolio/VISUAL_ASSETS_PLAN.md) explain setup, risks and
operating-cost boundaries. Use existing synthetic fixtures and non-destructive seeding.

## Website and GitHub profile status

[Website handoff](docs/portfolio/WEBSITE_HANDOFF.md) contains implementation paths and
actual [desktop](docs/portfolio/assets/website-desktop.png) /
[mobile](docs/portfolio/assets/website-mobile.png) captures. The public site was read-only
inspected: no Noordwerk section was present. Local preview is not deployed.

Fresh `npm ci --ignore-scripts` initially failed on the pre-existing manifest/lock mismatch.
After lock repair it passed. Production build, all 13 tests and targeted lint passed.
Full lint remains FAIL: three existing errors in unchanged UI/config files (plus warnings).
`npm audit` remains FAIL: **26 findings, 2 critical, 17 high, 7 moderate**; critical
packages include Vitest/tinypool in the development tree. A suggested fix requires a
major Vitest upgrade; no forced/broad upgrade was applied. These findings need scoped
security review before website publication. Build output also warns of a >500kB chunk
and stale Browserslist data; no performance claims were invented.

The [profile addition/pin recommendation](docs/portfolio/GITHUB_PROFILE_DRAFT.md) preserves
the existing profile voice and other evidence. Bio, README and pins are not published
by this pass. Proposed new-document links explicitly require prior branch publication.

## Executed evidence

| Check | Actual result / scope |
|---|---|
| Hub `make verify` | PASS, .NET Release build + 16 tests + process/contract/docs/history checks |
| Agent `make verify` | PASS, 27 tests + 30/30 deterministic cases + frozen-report/docs/history checks |
| Playbook `make verify` | PASS, 17 tests + formula/report/scenario/docs/history consistency |
| Agent `python3 scripts/verify_hub.py` | PASS, real local HTTP; confirmation, same-ID retry, Bob 404, Maria decision |
| Website clean install/build/test | PASS after lock repair; 13 tests; no declared dependency added |
| Website targeted ESLint | PASS for changed component, Home and SiteNav |
| Website full lint / dependency audit | FAIL as described above; not waived |
| Website browser | PASS, Chromium 1440×1000 / 390×844, three cards/assets, visible limitations, no page overflow, Dutch warning; [report](docs/portfolio/assets/website-preview-report.json) |
| Visual review | Existing Hub overview/approval/cover inspected; new website captures, SVG renders and CLI output inspected |
| Markdown/local assets | Existing checkers resolve authored local targets; standard Markdown tables/images; no new Mermaid syntax |
| Entry-document Markdown rendering | PASS: five README/narrative/summary documents rendered through GitHub's non-publishing GFM endpoint |
| Current external navigation | PASS: 18 current public links; four new review-document links classified pending publication, not falsely passed |
| Hosted CI | Published main runs below passed; new local showcase branches NOT EXECUTED on GitHub |
| Real-model evaluation | NOT EXECUTED anew; preserved failed results, no tuning |

Published baseline: Hub [verify](https://github.com/phlppgdfry/enterprise-ai-automation-hub/actions/runs/42002336563)
and [browser](https://github.com/phlppgdfry/enterprise-ai-automation-hub/actions/runs/42002805199);
Agent [verify](https://github.com/phlppgdfry/enterprise-ai-agent-governance/actions/runs/42002389270)
and [integration](https://github.com/phlppgdfry/enterprise-ai-agent-governance/actions/runs/42002389177);
Playbook [verify](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/actions/runs/42002516785).
These exact main runs are historical evidence, not checks on unpushed showcase commits.

## Remaining limitations

Model holdout v1 22/32 and v2 21/32 overall: **both quality gates failed**. Source-ID
validity is not relevance. The financial base remains **−EUR 7,695 year one / month-25
payback**, with fictional assumptions rather than measured savings. Public fixture tokens,
local JSON/audit and Microsoft designs are not production identity, protected storage or
tenant delivery. No full screen-reader review or real recruiter/user study was performed.
Visitor scores are explicit heuristic judgments, not validated hiring outcomes.

## Personal learning requirements and career readiness

Use [interview preparation](docs/portfolio/INTERVIEW_PREPARATION.md), contribution questions
and the existing code map. Independently reproduce request retries, approval/ownership
checks, one model failure and one cash-flow month. Explain AI assistance with specifics;
do not imply an ability solely because a generated artifact exists.

The case supports discussion for business/functional analysis, junior AI implementation,
automation prototyping and AI product analysis. It does not establish senior production
AI engineering, cloud/security architecture, verified consulting delivery or management
experience. Degree, language proficiency, prior employment and availability require owner
confirmation, not inference from repositories.

## Next actions — exactly five, ordered by professional value

1. Rehearse the five-minute business-to-workflow demonstration and answer one unfamiliar change request independently.
2. Complete the personal contribution ledger: decisions, AI assistance, review/corrections and tasks reproducible without AI.
3. Record one captioned flagship clip using the actual application, visible synthetic-data labels and honest limitations.
4. Review/publish the scoped repository/profile proposals through PRs; obtain actual hosted checks and explicit merge approval.
5. Review website lint/security findings separately, then approve any deployment only after the isolated candidate and current main are reconciled.

The showcase preparation is complete for review. Further feature development is not
necessary to begin evidence-based career conversations.
