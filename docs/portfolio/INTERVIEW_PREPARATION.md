# Interview preparation: explain, reproduce, then claim

Use [the code map](../code-and-practice.md) and [timed walkthrough](../portfolio-walkthrough.md)
for navigation. The statements below describe repository facts, not the owner's employment
history, independent implementation or unverified mastery. Substantial AI assistance was
used. Personal contribution questions require the owner's own answers.

## Automation Hub

**Level 1 — recruiter:** 'A fictional company needs a clearer way to submit and approve
requests. This local application makes ownership, status and reasons visible. Rules route
the work; a person makes the decision. It is a tested prototype using synthetic identities.'

**Level 2 — analyst/product:** Trace expense EUR 320 from BR1/FR1 to Finance, pending status,
Maria's reasoned decision and audit event. Explain rejected requests, duplicate retries and
the difference between a closed dialog and cancelled business request. The objective is
accountable handoffs, not model autonomy. No time saving or adoption was measured.

**Level 3 — engineer/architect:** ASP.NET Core 10 serves same-origin HTML/CSS/JS. `Current`
resolves server-mapped fixtures; `Create` validates input and owner-scoped idempotency;
`Decide` requires approver, pending status, reason and current version. `Commit` persists a
new snapshot before committing memory. A writer lease, atomic replacement and restored
invariant checks bound a single-process JSON demonstration. Describe interrupted temp
writes, failed-write 503, conflicts and restart tests. This is not production auth/audit.

| Topic | Fact / tradeoff / independent exercise |
|---|---|
| Problem and architecture | Email handoffs → one API authority and local store; not a distributed workflow engine |
| Technology choices | Reuse .NET API; authored UI and stdlib tests avoid a replacement frontend/backend stack |
| Components/data flow | UI → request API → routing/validation → JSON snapshot/audit → owner-filtered response |
| Security | Server checks every resource/action; fixture token is public; no real tenant or queue RBAC |
| Tests/gates | 16 HTTP/storage tests, contract/process/docs checks, real browser journey; failing check must remain visible |
| Weakness/improvement | Local administrator can edit audit; production requires genuine identity, transaction/storage/recovery design |

## Agent Governance

**Level 1 — recruiter:** 'A policy assistant should show its sources and know when it
cannot help. The deterministic reference works without a model. The real-model experiments
failed their quality gates, and the case shows why that stops rollout.'

**Level 2 — analyst/product:** Explain allowed policy scope, clarification and escalation.
Separate model answer quality from authorization, explicit user confirmation and a human
approval. Positive-question accuracy alone cannot justify rollout: v2 answered 12/12 supported
holdout cases but only passed 21/32 overall. Show a failed ambiguous/unsupported question.

**Level 3 — engineer/architect:** `Agent.answer` is deterministic. `GovernedAgent` uses a
provider protocol and fixed-loopback Ollama. Source publication/persona filtering precedes
context. V1 validates exact source/summary; `PolicySelector.answer` v2 proposes only an ID,
with code rendering committed evidence. This reduces copying failures but does not solve
relevance or abstention. Validation/timeout failures escalate. No model action tools exist.
The separate `submit_request` boundary validates confirmation, employee identity, fixed
destination, arguments and response; it does not expose human-decision capability.

| Topic | Fact / tradeoff / independent exercise |
|---|---|
| Problem/architecture | Policy evidence selection under controls; deterministic default and experimental model path |
| Technology choice | Python stdlib + small context; all permitted excerpts fit, so embeddings/vector DB/MCP would add needless machinery |
| Components/data flow | Persona-filtered catalog → bounded model proposal → validator → committed source/summary or escalation + trace |
| Security | No action tools, no model-supplied URLs, no token in model context; CLI persona is simulated identity |
| Tests/gates | 27 model-independent tests, 30 deterministic cases; frozen real-model gate separately fails; authored holdout not independent assurance |
| Weakness/improvement | Source validity ≠ relevance. Independent reviewed relevance/abstention data is future work; do not tune on frozen holdout |

## Consulting Playbook

**Level 1 — recruiter:** 'This fictional engagement connects a business problem to
requirements, process design, cost and an investment decision. The base case loses money
in year one, so the recommendation is a small measured pilot rather than a large rollout.'

**Level 2 — analyst/product:** Walk one stakeholder need through BPMN, functional/nonfunctional
requirements, acceptance owner and pilot gate. Explain cost reconciliation, adoption ramp,
capacity versus realised saving, conservative/base/optimistic scenarios and who can stop
the pilot. Synthetic workshop outputs are not evidence of facilitated client workshops.

**Level 3 — engineer/architect:** `playbook.py` retains the immediate-benefit model;
`financial_model.cash_flow` implements the ramp over 36 months; `scenarios.py` publishes
named assumptions. Month-one recurring cost with delayed benefits explains the difference
from the original economics. Committed generated reports are checked against formulas;
test zero adoption and costless denominators rather than memorising ROI. The PDF generator
is optional build tooling; production packages and tenant deployment are absent.

| Topic | Fact / tradeoff / independent exercise |
|---|---|
| Problem/architecture | Separate business decision from a technology demo; documents + executable calculations, no service backend |
| Technology choice | Python standard library for inspectable formulas; optional ReportLab only for PDF regeneration |
| Components/data flow | Synthetic inputs → gated prioritisation → monthly cash flow/scenarios → executive PDF and decision |
| Security | No real client/HR data or integration secrets; no live notifications or financial transactions |
| Tests/gates | 17 tests, committed-output consistency, input validation and hard feasibility gates |
| Weakness/improvement | No actual adoption, baseline or vendor quote; validate with real owners before any enterprise investment |

## Difficult questions and evidence-backed response boundaries

| Question | Defensible response / what to demonstrate |
|---|---|
| Why this architecture? | Show existing API reuse and small deployment footprint; explain one limitation you accepted and an alternative |
| How is unsafe agent execution prevented? | The model has no action tools; separate confirmed submission cannot decide; API authorization remains authoritative |
| Does a cited answer prove reliability? | No. Open a failed v2 case with a permitted but irrelevant source |
| Why not hide the failed model? | Failed evidence is a release decision input. Never substitute deterministic safety results for model accuracy |
| What changes before production? | Real identity/resource permissions, protected transactional audit/storage, recovery, independent model/user review and tenant acceptance |
| What did you personally decide/build? | **Owner confirmation required:** name the decision, commit/change and rationale; do not infer it from AI-authored prose |
| What did AI do? | AI supported implementation, documentation and verification. **Owner confirmation required:** scope of prompts, review, corrections and code you independently reproduced |
| What can you reproduce unaided? | **Owner exercise required:** implement one routing rule/test, trace a model failure and recalculate one cash-flow month |
| What professional experience does this prove? | Portfolio artifact ownership only; client facilitation, production operations and independent delivery need separate truthful evidence |

## Practical learning checklist

- [ ] Explain the API flow from HTTP request to committed state without reading a pitch.
- [ ] Reproduce same-key retry, conflicting decision and Bob's 404; explain each status.
- [ ] Trigger a safe failed write using the existing test and explain why memory stays unchanged.
- [ ] Run deterministic agent answer/refusal and resolve the cited source yourself.
- [ ] Read a failed raw model case, expected evidence and trace; distinguish root-cause hypotheses from observations.
- [ ] Calculate one forecast month by hand; set adoption to zero and explain absent payback.
- [ ] Trace a BPMN exception to an owner, requirement and acceptance test.
- [ ] Explain tenant artifacts as designs; do not claim a live Noordwerk Microsoft build.
- [ ] Write a personal contribution ledger: decision, AI assistance, independent review, evidence, remaining gap.
- [ ] Rehearse five minutes, then answer an unfamiliar change request without a memorised script.

For BA/functional roles prioritise requirements/process/acceptance/value; for automation
consulting add identity, integration and tenant ALM knowledge; for senior AI/cloud roles
independent production delivery, evaluations, observability and operational depth remain
unproven. Practise these gaps against code rather than listing unrelated certifications.
