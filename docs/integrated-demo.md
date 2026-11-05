# Noordwerk: ten-scene reproducible demonstration

All people, requests, workshops, costs and policies are synthetic. Start here for the
business story; open the Hub for the application and the agent repository for AI evidence.
No pre-recorded result is presented as live execution.

## Preparation

Clone the three repositories beside one another, check out `portfolio/noordwerk-showcase`
in each, install .NET 10 + Python 3.11+ + Make. From the Hub run `make verify`, then
`python3 scripts/start_demo.py`. In a second terminal run `python3 scripts/seed_demo.py`.
Seeding uses stable keys and never erases local requests. Open `http://127.0.0.1:5088/`.
Stop the server before isolated HTTP/browser/integration suites, which need port 5088.
Browser dependencies are optional: `npm ci --ignore-scripts`, `npx playwright install chromium`,
`npm run test:browser`. The app itself does not need Node or paid credentials.

## Scenes and inspectable evidence

| Scene | Live action / artifact | What to explain |
|---|---|---|
| 1 Business problem | Client brief: email request handoffs | 600/month and 12→5 minutes are assumptions, not observed savings |
| 2 Process transformation | `process/*.bpmn`, `docs/assets/*-process.svg` | Employee confirms; API validates/routes; a person decides; invalid data returns for correction |
| 3 Employee | Alice: new expense, EUR 320, confirm | Finance route is deterministic; no AI approval |
| 4 AI experiment | In agent repo: `python3 policy_selector.py 'How much should an application-access request cost?' --model qwen3:8b` | Actual local inference. Show model ID/tokens/stages; no tools. It may fail or choose irrelevant evidence—do not rehearse it as guaranteed success |
| 5 Manager | Maria: open request, enter review reason, approve/reject | Demo fixture, not real authentication; server rejects employee decisions |
| 6 Audit | Alice opens saved request history | A reason and version persist. File admin can still alter the local store |
| 7 Security | Bob cannot see Alice's request; optional direct HTTP GET using its ID returns 404 | This tests owner isolation, not tenant isolation or production login |
| 8 Evaluation | `eval/RELEASE_REPORT.md` and raw JSON | V1 4/12 supported; v2 12/12 but worse nonanswers. Both gates FAIL |
| 9 Value | `output/scenarios.json`, monthly cash flow, executive PDF | Base first year −€7,695, month 25 payback; no measured cash savings |
| 10 Decision | Requirements/roadmap and risk register | Discovery + bounded rules-only pilot; real-model business rollout deferred |

## Automated evidence path

1. Hub: `make verify` (HTTP, storage and offline contracts/process/release hygiene).
2. Hub: `npm run test:browser` (isolated process; output under `/tmp/noordwerk-browser-evidence`).
3. Agent: `make verify` (fixtures + deterministic cases; no model calls).
4. Agent: `python3 scripts/verify_hub.py` (real local .NET transport; sibling Hub Release build required).
5. Playbook: `make verify` (original/ramp/scenario calculations, outputs, docs and hygiene).
6. Optional actual inference: `python3 scripts/evaluate_release.py --selector v2 --output /tmp/new-model-run.json`.
   Expected gate failures exit nonzero. Choose a new output path; historical results are never overwritten.

## Failure rehearsal and cleanup

API absent: show recovery guidance; restart using the same store. Submission timeout:
retry unchanged details with original key, since the server may already have persisted it.
Decision 409: refresh and review; do not force a second decision. Corrupt store: fail
startup and preserve bytes; do not reseed over it. Ollama absent/malformed: escalate,
no fallback action. No cancellation endpoint exists: closing a form is not cancelling
a submitted request. No email, Teams recipient, cloud resource or payment is touched.

Ctrl+C stops the demo. Its `data/requests.json` remains ignored by Git. Do not delete a
user's existing store; use `HUB_DATA` with a separate path for a disposable rehearsal.
