# Visual evidence and 90-second recording scripts

Reuse existing real captures and diagrams. Architecture SVGs are authored technical
illustrations, not application screenshots. Raw model results remain unchanged. No new
Microsoft screenshot, customer metric or successful inference is fabricated.

## Three useful views per case

| Case | Existing asset or reproducible output | Type / purpose |
|---|---|---|
| Hub 1 | [Workspace](https://github.com/phlppgdfry/enterprise-ai-automation-hub/blob/main/docs/assets/hub-overview.png) | Actual Chromium capture, synthetic local records; product overview |
| Hub 2 | [Approval](https://github.com/phlppgdfry/enterprise-ai-automation-hub/blob/main/docs/assets/hub-approval.png) | Actual human decision dialog; authority/history |
| Hub 3 | [Mobile](https://github.com/phlppgdfry/enterprise-ai-automation-hub/blob/main/docs/assets/hub-mobile-reduced-motion.png) | Actual 390px layout; desktop/mobile evidence |
| Agent 1 | [Release report](https://github.com/phlppgdfry/enterprise-ai-agent-governance/blob/main/eval/RELEASE_REPORT.md) | Actual recorded results; capture rendered report, not a fabricated agent UI |
| Agent 2 | `python3 agent.py ask 'Wat is het onkostenbeleid?'` | Real terminal output with evidence ID; capture after execution |
| Agent 3 | `python3 scripts/verify_hub.py` | Real integration summary: confirmation, stable retry ID, Bob 404 and Maria decision; run only with port free |
| Playbook 1 | [Executive cover](../assets/executive-cover.png) | Actual rendered PDF cover |
| Playbook 2 | [Executive PDF](../../deliverables/noordwerk-executive-brief.pdf), financial pages | Actual fictional cost/forecast/scenario presentation, not measured ROI |
| Playbook 3 | [AS-IS](../assets/as-is-process.svg) / [TO-BE](../assets/to-be-process.svg) | Editable process diagrams; show decision/exception ownership |

Agent has no separate graphical application. [Policy output](https://github.com/phlppgdfry/enterprise-ai-agent-governance/blob/showcase/recruiter-evidence/docs/assets/agent-policy.png),
[authority handoff](https://github.com/phlppgdfry/enterprise-ai-agent-governance/blob/showcase/recruiter-evidence/docs/assets/agent-authority.png)
and [real HTTP output](https://github.com/phlppgdfry/enterprise-ai-agent-governance/blob/showcase/recruiter-evidence/docs/assets/agent-integration.png)
were captured from actual commands with matching text files. These review-branch links
are pending publication; inspect the local Agent `docs/assets` until pushed.
Existing diagrams/charts are not screenshots. The local
website preview provides an additional evidence navigator only. Fresh capture results
and paths are recorded in the closure report rather than pretending planned views exist.

## Hub recording — 90 seconds

| Time | Screen / narration |
|---|---|
| 0–10 | Show workspace: 'Fictional Noordwerk loses request ownership in email.' |
| 10–25 | Show source-backed architecture: 'Rules route; the API controls state; a person decides.' |
| 25–60 | Submit Alice EUR 320, switch to Maria, enter a reason, decide, show Alice history and Bob isolation. Say 'public demo identities'. |
| 60–75 | Show 16-test summary/browser report. 'Local JSON and fixture tokens are not production security.' |
| 75–90 | 'A bounded process pilot could test adoption and cost. No realised savings are claimed.' |

## Agent recording — 90 seconds

| Time | Screen / narration |
|---|---|
| 0–10 | 'Policy answers need relevant evidence and clear authority boundaries.' |
| 10–25 | Show architecture: filter before context, validate proposal, answer or escalate; zero model action tools. |
| 25–60 | Execute deterministic policy/refusal commands, show source; open real frozen report. Clearly call this deterministic execution and recorded model evidence. |
| 60–75 | 'v1 22/32, v2 21/32 overall; both gates failed. Allowed source IDs can still be irrelevant.' |
| 75–90 | 'This demonstrates how to reject an unsafe rollout rather than decorate a demo with green tests.' |

## Playbook recording — 90 seconds

| Time | Screen / narration |
|---|---|
| 0–10 | 'What should a fictional company automate, and is it worth the cost?' |
| 10–25 | Show requirements, owners and AS-IS/TO-BE process. |
| 25–60 | Run `make verify`, show forecast/scenarios and the executive PDF; distinguish assumed capacity from cash. |
| 60–75 | 'Base year one −EUR 7,695; payback month 25. Inputs are fictional; model rollout is not justified.' |
| 75–90 | Show pilot gate: measure adoption, reliability and value before a go/no-go decision. |

## Reproducible recording procedure

Use the existing local demo, a synthetic rehearsal store and browser zoom 100%.
On macOS use Shift–Command–5 → Record Selected Portion, select the browser/terminal,
then start; stop from the menu bar. This owner action was not executed by the agent.
Disable personal notifications and keep credentials/private tabs out of frame. Do not
use real inboxes, tenant identities or filesystem paths containing private data.
Record at 1440×900 or comparable readable viewport, then check on a phone. Add captions
and the phrase 'AI-assisted independent portfolio; fictional case'. If a step fails,
show the failure or rerecord and label edits; do not present a cut as uninterrupted live
execution. Export one 60–90 second clip per case and retain the exact tested commit/date.

No finished video is claimed. Recording scripts and source evidence are ready; owner
narration, captions and a final media review remain necessary before publication.
