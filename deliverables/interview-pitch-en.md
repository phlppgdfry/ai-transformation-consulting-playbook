# Two-minute interview pitch

I built three connected portfolio cases for a fictional technical-services company.
They show how I translate a process problem into an implementation, governance
controls and an adoption plan.

The first case is a running .NET request API. It validates submissions, routes
them to Operations, Finance or IT, and keeps a persistent event history. Retries
are idempotent; conflicting decisions require a refreshed version. Only a separate
approver identity can decide.

The second case is a deterministic reference agent, not an LLM deployment. It
answers from published sources, filters by a simulated role, declines personal
HR questions and asks for explicit confirmation before submitting to the API.
Its evaluation set checks outcomes and citations. I explain separately how to
build and evaluate the real Copilot Studio agent with end-user authentication.

The third case covers discovery, prioritisation, an auditable value model,
training and a pilot decision. The base scenario has a negative first-year result.
That matters: my recommendation is a limited pilot, not an unsupported savings promise.

The new cases run locally. I do not claim they are deployed in Power Platform or
that a real customer has achieved these results. I can show the separate existing
Power Platform lab and distinguish its recorded evidence from these new designs.
