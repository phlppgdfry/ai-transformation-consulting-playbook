# Noordwerk Portfolio v1.0 — closure and merge handoff

Verified 31 October 2026. **Portfolio complete and showcase-ready for its stated local
reference scope. Default-branch publication awaits explicit owner merge approval.**
Noordwerk, its people, operational data and financial assumptions are fictional.
This designation creates no GitHub Release, tag or production-readiness claim.

## Reviewed publication

All three public repositories retain `portfolio/noordwerk-showcase`, with draft PR #1
targeting `main`. Local and remote heads were synchronized before this documentation pass.

| Repository / PR | Reviewed head before this report | Main baseline | Proposed merge |
|---|---|---|---|
| [Automation Hub #1](https://github.com/phlppgdfry/enterprise-ai-automation-hub/pull/1) | `6f5928708f4a98e07a37dc40f1086667945bf0ba` | `09a98a448aed1556f5668dd3cc8702df1c3081c5` | Merge commit |
| [Agent Governance #1](https://github.com/phlppgdfry/enterprise-ai-agent-governance/pull/1) | `39080e094ca3e09f9550af846575b48f009a31ed` | `9452be6d4e294f96fb85b5ade646e873cf44f20c` | Merge commit |
| [Consulting Playbook #1](https://github.com/phlppgdfry/ai-transformation-consulting-playbook/pull/1) | `b8c1d4ee635130cdc393ce349e411a59aa0d1411`; report adds a documentation-only commit | `87fceff16b9e39067d3619cc47a9ffd57af9d9a4` | Squash |

The exact report commit and its completed Actions checks are recorded in PR #1 and the
owner-facing handoff; a document cannot embed its own Git commit hash. Existing candidate
checks passed at the heads above. New report-head checks must complete before approval.
No unexpected newer main commits or merge conflicts were found. No branch protection or
required-check rules are configured: successful checks are an explicit review gate,
not a claim of server enforcement.

Retain Hub history because Agent CI pins Hub commit
`c74fff699e099b0edc7890a8cc4c2e924f847b2b`. Retain Agent history to preserve the auditable
sequence of frozen holdout, implementation and results. Playbook can be squashed;
retain feature branches and historical evidence. Never force-merge or bypass protection.

## Actual verification

| Check | Result and boundary |
|---|---|
| Hub `make verify` | PASS: .NET Release build, 14 HTTP + 2 storage tests, BPMN/SVG, contracts, documentation and limited history/credential checks |
| Agent `make verify` | PASS: 27 model-independent tests, 30 deterministic evaluation cases, report/documentation/history consistency checks |
| Playbook `make verify` | PASS: 17 tests, reproducible financial/scenario outputs, documentation and limited history/credential checks |
| Hub `npm run test:browser` | PASS: isolated Chromium desktop/mobile, submission, human decision/history, Bob isolation, reduced motion and outage message; 31 October run |
| Agent `python3 scripts/verify_hub.py` | PASS: real local HTTP, confirmed submission, same-ID retry, Bob 404, Finance routing, Maria approval |
| Clean checkout and packaging | PASS in preceding consolidation: fresh clones/new Python environment, locked browser installation and .NET package; see linked evidence |
| Final main checks | NOT EXECUTED: no merge authorized or performed |
| Microsoft tenant / production authentication / independent model validation | NOT EXECUTED; outside the local reference scope |

An overlapping verification invocation initially encountered occupied port 5088 and
correctly refused to attach. The subsequent sequential Hub suite passed; no test was
weakened. The browser's only console error was the intentionally injected network failure.
Credential checks inspect tracked files and reachable history using limited patterns;
they are not an exhaustive independent security audit. No material exposure was found.

## Business, demonstration and AI conclusions

Start with [PORTFOLIO_FINAL.md](PORTFOLIO_FINAL.md) and the
[five-/ten-minute walkthrough](docs/portfolio-walkthrough.md). They link requirements,
stakeholders, AS-IS/TO-BE BPMN, RACI, risks, adoption, roadmap and the
[ten-page executive PDF](deliverables/noordwerk-executive-brief.pdf).
The [financial model](output/investment-case.json) retains the fictional base:
**year-one net value −EUR 7,695; payback month 25**, with a 36-month forecast and transparent
[scenarios](output/scenarios.json). Recommend a bounded rules-only pilot with measured
adoption and a go/no-go gate, not an unconditional rollout.

Demonstration: from Hub run `make verify`, then `python3 scripts/start_demo.py`; in a
second terminal run `python3 scripts/seed_demo.py`. Open `http://127.0.0.1:5088/`.
Alice submits EUR 320, Maria decides with a reason, Alice sees history, Bob is denied
access. Stop the server before isolated tests. Seeding does not erase existing data.
The deterministic agent requires no model installation; follow the central walkthrough.

**EXPERIMENTAL — QUALITY GATES NOT PASSED.** Historical Qwen 8B: 10/12 overall but only
2/4 supported questions. Frozen 32-case holdout: v1 4/12 supported, 22/32 overall;
v2 12/12 supported, 21/32 overall. Valid source IDs do not prove answer relevance.
Abstention and ambiguity failures remain visible. No new tuning, dataset changes or
model evaluation was performed in this closure pass. Deterministic authorization and
human decisions are enforced outside the model; model reasoning is not thereby verified.
See the [preserved release report](https://github.com/phlppgdfry/enterprise-ai-agent-governance/blob/portfolio/noordwerk-showcase/eval/RELEASE_REPORT.md).

## Production boundaries and owner actions

Public synthetic tokens are not production identity or tenant isolation. Single-process
JSON persistence is not distributed transactional storage or tamper-proof audit.
Microsoft artifacts are offline contracts/designs, not a tenant deployment. Full
accessibility, independent user/model review and production recovery remain unverified.
These do not block an accurately labelled portfolio. No new feature engineering is needed.

Accurate repository descriptions and suggested additional topics were applied with owner
authorization; useful existing topics and public visibility were retained. No profile pin,
merge, default-branch push, release, package, cloud deployment or paid operation occurred.

1. Approve or decline the exact heads and merge methods in the final handoff. Until then
   all PRs remain draft and unmerged; share candidate links rather than old main READMEs.
2. After approval, refresh heads/bases/checks, mark approved PRs ready, merge Hub → Agent →
   Playbook, retain branches and verify actual main workflows. Changes invalidate approval.
3. After verified publication, replace unnecessary candidate cross-links through reviewed
   PRs, never direct pushes to main. Do not delete branches before link verification.
4. Optionally pin repositories: GitHub profile → Customize your pins → select these three →
   Save pins; order Playbook, Hub, Agent. Profile pinning has not been performed.

**Closure recommendation:** close engineering for Noordwerk Portfolio v1.0. The remaining
publication decision belongs to the owner. Production deployment would require a separate
scope and validation, not another portfolio improvement cycle.
