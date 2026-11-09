# AI portfolio interview playbook

> **Owner-review draft.** Not an approved CV, profile, application or outreach message. Personal facts and contribution require owner confirmation. Vacancy observations retain their original 6 November 2026 date; recheck before use.

45 practice questions, grounded in the published Noordwerk reference. These are draft
answers about artifacts, not proof of the owner's personal understanding. **PERSONAL**
requires an owner-supplied truthful answer. Never memorise an invented contribution.
Use [the source map](../code-and-practice.md) and [flagship demo](FLAGSHIP_PROJECT_STRATEGY.md).

## Level 1 — recruiter: 15 questions

| # | Question | Concise evidence-based answer / boundary |
|---|---|---|
| 1 | What is this portfolio? | A fictional transformation case linking requirements, a working request workflow and separate AI evaluation. It is self-directed and substantially AI-assisted. |
| 2 | What can you show in two minutes? | Alice submits an expense, Maria decides with a reason and the application preserves history. Public demo identities are clearly labelled. |
| 3 | Why does this problem matter? | Unclear ownership and approval reasons create handoff friction. No actual Noordwerk company or measured baseline exists. |
| 4 | Which role do you want? | Proposed direction: business/functional analysis or supported AI implementation. **PERSONAL:** confirm preferred title and tradeoffs. |
| 5 | Did AI write the software? | AI materially supported implementation, documentation and verification. **PERSONAL:** describe your prompts, decisions, review/corrections and work reproduced independently. |
| 6 | Was this paid client work? | No. It is an independent synthetic case; it cannot be presented as employment or customer delivery. |
| 7 | What skills does it demonstrate? | Inspectable process/requirements work, API workflow reasoning, test/evaluation evidence and explicit business tradeoffs. Personal mastery needs demonstration. |
| 8 | Why is 'AI' in a rules-based application? | The transformation case evaluates where AI is useful. Known routing rules stay deterministic; separate policy-assistant experiments expose actual model limitations. |
| 9 | Did it save money? | No measured savings. Fictional adoption/cost inputs yield −EUR 7,695 in year one and payback month 25. |
| 10 | What did not work? | Both model holdout gates failed. V2 improved positive questions but passed only 21/32 overall. The failure stays visible. |
| 11 | Why not apply as a senior architect? | These are local reference artifacts, not independent production architecture or leadership evidence. Seek supported delivery first. |
| 12 | What is your education and experience? | **PERSONAL:** supply exact verified qualifications and work history. None is inferred from repositories. |
| 13 | What can you explain without AI? | **PERSONAL:** demonstrate a rehearsed API flow, failure case or calculation unaided; say where help is still needed. |
| 14 | Where can you work and in which languages? | **PERSONAL:** confirm commute radius, hybrid attendance, Dutch/English/French level, licence and availability. West Flanders is the stated base. |
| 15 | Why should we interview you? | The case gives concrete decisions and failures to inspect. **PERSONAL:** demonstrate clarity, learning and contribution rather than claiming a job title the evidence cannot support. |

## Level 2 — business/product manager: 15 questions

| # | Question | Concise evidence-based answer / boundary |
|---|---|---|
| 1 | Who is the user and buyer? | Fictional employees request materials/expenses/access; an approver decides. Sponsor, Operations, Finance and IT have distinct proposed responsibilities. |
| 2 | What is the actual requirement? | Submit, route, retrieve own records and record a single reasoned decision. Trace BR1/FR1/FR2 in the acceptance map to API/browser tests. |
| 3 | Why not just improve email? | That is a legitimate option in the decision brief. A portal needs enough measured coordination/audit benefit to cover adoption and recurring cost. |
| 4 | How did you gather requirements? | Synthetic discovery/workshop artifacts exist. **PERSONAL:** no claim of interviewing real clients; explain how you would validate them. |
| 5 | How do you prioritise? | Hard feasibility/ownership gates precede scoring; attractive impact cannot compensate for missing permission or unacceptable risk. See `playbook.py`. |
| 6 | What is the AS-IS versus TO-BE? | Email handoffs become visible intake/routing/human review/history. Future Microsoft steps are proposed, not executed automation. |
| 7 | How is ROI calculated? | Reconciled upfront/recurring cost and monthly adoption-adjusted benefits over 36 months. Ramp economics differ from the retained immediate-benefit model. |
| 8 | Are time savings cash savings? | No. Released capacity becomes financial value only through explicit realisation assumptions; it is not automatic payroll reduction. |
| 9 | Why is the first year negative? | Upfront and recurring costs occur before full adoption-adjusted benefits. Base first-year net is −EUR 7,695; don't improve the assumptions to sell rollout. |
| 10 | What would make you stop? | Failed security/quality gates, lack of ownership/adoption or poor measured economics. The roadmap includes independent evaluation and go/no-go. |
| 11 | What are the main risks? | Public fixture identity, editable local audit, unverified tenant delivery, model relevance/abstention failures and assumed value. Separate owners and gates address proposed mitigation. |
| 12 | How would you support adoption? | Use role-specific training, observed task success, feedback, support owner and explicit escalation. Existing plan is proposed, not evidence employees adopted it. |
| 13 | How would you handle stakeholder disagreement? | **PERSONAL:** use an actual example if available. Otherwise describe a proposed traceable decision log, conflicting needs and sponsor decision; don't invent facilitation experience. |
| 14 | Which product metric comes first? | For a pilot, measured successful task completion and decision traceability before claimed ROI; define baseline, owner and denominator. No actual KPI improvement is measured here. |
| 15 | What was your product decision? | **PERSONAL:** identify a decision you made, alternatives, AI assistance and evidence. 'The repository keeps rules deterministic' is an artifact fact, not automatically your personal decision. |

## Level 3 — technical hiring manager: 15 questions

| # | Question | Concise evidence-based answer / boundary |
|---|---|---|
| 1 | Walk the architecture. | Same-origin UI → ASP.NET Core API → one-process JSON snapshot/audit. Python agent and financial scripts are separate; only confirmed CLI submission integrates over HTTP. |
| 2 | What is the lifecycle? | Pending → approved or rejected once, with human approver, reason and current version. No cancellation endpoint or autonomous approval is claimed. |
| 3 | How is retry safety handled? | Owner-scoped idempotency key plus payload fingerprint. Same key/payload returns the original record; altered payload conflicts. Never infer write failure from a lost response. |
| 4 | What happens with concurrent decisions? | Server validation/version checks allow one winner; competing decisions conflict. HTTP tests exercise this. It is a local-process boundary, not a distributed transaction claim. |
| 5 | How are failed writes handled? | New state is written before in-memory commit; tests verify storage failure does not silently approve or erase the original store. Explain `Commit` and restart tests. |
| 6 | Authentication versus authorization? | Public fixture token maps identity/role; resource/action checks enforce demo authorization. This is not real login, token issuance or production tenant isolation. |
| 7 | What does the model control? | Evidence proposal only. It cannot choose an action URL, read a token or invoke an approval tool. A separate confirmed CLI has a fixed submission boundary. |
| 8 | Is this RAG? | It is small-context evidence selection from permitted committed excerpts, not vector search/hybrid retrieval. All approved excerpts fit, so a vector DB is unjustified. |
| 9 | Why do structured outputs not solve quality? | A valid allowed source ID can still be irrelevant. V2 positive-question improvement coincides with abstention/ambiguity failures. |
| 10 | What do the test totals mean? | Hub 16; Agent 27 + 30 deterministic; Playbook 17. Fixture tests verify code boundaries; real-model outcomes are separate frozen reports. Never add them into a model-accuracy claim. |
| 11 | How strong is the holdout? | 32 authored regression cases, frozen before v2; v1 22/32, v2 21/32 overall. Small and not independently authored, so not production assurance. Do not tune on it. |
| 12 | How is prompt injection addressed? | Instruction hierarchy/schema validation and deterministic action boundaries reduce exposure. No perfect detector or arbitrary remote document support is claimed; safety rules are not model reasoning. |
| 13 | What observability exists? | Local trace stages/correlation, model identity, timing/tokens and outcomes. No distributed production tracing or measured cloud cost. Avoid logging secrets and unnecessary content. |
| 14 | What changes for production? | Real identity, scoped resource permissions, transactional/protected storage, recovery/retention, operational monitoring, independent model/user evaluation and actual tenant acceptance. No single switch makes it production-ready. |
| 15 | Could you implement or debug this unaided? | **PERSONAL:** demonstrate one scoped change/test with no generated answer. Explain what you can do now and what needs assistance; repository existence is insufficient. |

## Scoring practice without self-deception

Have a reviewer choose five random questions. Score each 0 (cannot explain), 1 (accurate
with notes), 2 (accurate unaided and can locate evidence). Target 8/10 twice, with one
unfamiliar follow-up. This is a learning criterion, not a qualification or hiring guarantee.
Keep unknown personal questions blank until confirmed. Record the gap and next exercise,
not another polished answer you cannot defend.
