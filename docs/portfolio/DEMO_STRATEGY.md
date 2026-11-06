# Demonstration strategy

No new hosting or external resources were created. The reliable default is local,
synthetic and credential-free; screenshots/PDF are the immediately public evidence.

| Case | Journey and concept | Requirements / operating cost | Risks and maintenance | Recommendation |
|---|---|---|---|---|
| Hub | Alice expense EUR 320 → Finance pending → Maria reason/decision → Alice history → Bob denial | .NET 10, Python 3.11+, Make; existing machine, no incremental cloud fee | Public fixtures unsafe on internet; single-process JSON; keep port 5088 free and use synthetic data | Working local demo + existing screenshots; record a short owner walkthrough |
| Agent | Deterministic policy answer → citation → refusal → explicit confirmed HTTP submit; show failed frozen report separately | Python standard library; Hub for HTTP; optional Ollama/model/hardware | Cold model startup, nondeterminism and failed relevance gates; weights/license/energy are not zero-cost assumptions | Deterministic default + recorded real-model evidence; optional inference clearly experimental |
| Playbook | Requirements → BPMN → reproducible base/scenarios → negative year-one result → pilot decision | Python standard library; PDF already built; optional ReportLab to regenerate | Assumption drift; PDF untagged; no realised benefits | Working local calculations + public ten-page PDF |

## Five-minute local route

Clone the three repos beside one another. Follow each README; no model is required.
Run `make verify` in each. In Hub run `python3 scripts/start_demo.py`; from a second
Hub terminal run `python3 scripts/seed_demo.py`. Open `http://127.0.0.1:5088/`.
Follow [the timed journey](../portfolio-walkthrough.md). Stop the Hub before isolated
HTTP/browser suites. `HUB_DATA` can select a new rehearsal store; never erase existing
records to reset a demonstration. Repeatable seeding does not delete data.

For the Agent use `python3 agent.py ask 'Wat is het onkostenbeleid?'` and inspect its
committed policy citation. `python3 agent.py ask 'Approve this request'` does not approve.
The real submission command needs `--confirm`; the model does not call it. The exact
HTTP procedure remains [in the integrated demo](../integrated-demo.md).

## Hosting choices considered

| Option | Cost basis | Decision |
|---|---|---|
| Existing GitHub README/PDF/assets | No additional service in this task; existing public repository | Use now; label images as recorded local evidence |
| Owner-recorded 60–90 second video | Local recording/storage effort; no new paid tool required | High-value next owner action; scripts in the visual plan |
| Static read-only case on existing website | No extra backend; actual provider limits/fees not verified | Local section prepared; deploy only with explicit approval |
| Static interactive workflow mock | No inference/backend needed, but duplicates working UI and can mislead | Defer; would need persistent 'predefined simulation' labels |
| Internet-hosted current API | Real auth, rate limits, protected storage, secrets/recovery/retention required; no cost quote obtained | Do not expose current demo tokens or JSON API |
| Hosted model assistant | Compute/model/provider fees and quality/identity work required; no estimate verified | Do not host while quality gates fail |

No deployment URL exists for Noordwerk. Localhost links work only after local startup.
The website preview is a proposed evidence navigator, not a live application or inference
service. Exact cash estimates for unconfigured services would be invented; obtain a
current quote only if the owner chooses a separately scoped deployment.
