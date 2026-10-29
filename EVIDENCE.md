# Capability evidence matrix

Last verified: **29 October 2026**. Environment: macOS, Python 3.14, ReportLab 5.0.0,
Poppler rendering. Every client observation and financial input is synthetic.

| Capability / status | Implementation | Method / result | Evidence artifact | Limitation |
|---|---|---|---|---|
| Original business case — **Implemented and verified** | `playbook.py` | Original formula, input and prioritisation tests pass | `output/business-case.json`, tests | Immediate benefits assumption retained explicitly |
| Itemised costs / ramp / monthly cash flow — **Implemented and verified** | `financial_model.py`, cost JSON | Reconciliation, ramp, no adoption, sensitivity and output consistency tests pass | `output/investment-case.json`, 15 total tests | No vendor quotes, discounting, tax or seasonality |
| Executive PDF — **Implemented and verified** | `scripts/build_executive_pdf.py` | Generated ten pages; all ten rendered and visually inspected | `deliverables/noordwerk-executive-brief.pdf`, preview | Selectable text, not tagged PDF or editable PPTX |
| Working product illustration — **Implemented and verified** | Hub screenshot included in PDF | Real local browser flow captured in companion repository | `docs/assets/hub-overview.png` | Synthetic local app, not Power Apps screenshot |
| BPMN / architecture — **Implemented and verified locally** | `process/*.bpmn`, SVG source | XML references/layout checked; visual process in PDF inspected | BPMN and `docs/assets/architecture.svg` | Not executable; external BPMN editor not tested |
| Discovery and stakeholder findings — **Simulated** | Case brief, workshop and templates | Document review only | `docs/discovery-workshop.md`, client brief | No actual interviews, workshop or sponsor sign-off |
| Options / risk / roadmap / adoption — **Documented design** | Engagement brief, roadmap, KPI plan | Cross-checked against the working Hub and model release failure | `docs/engagement-decision.md`, PDF | No actual organisational adoption result |
| Financial value — **Simulated** | Explicit scenario inputs | Year-one ramp net -7,695 EUR; payback month 25 | Monthly report and PDF | Released capacity is not realised payroll saving |
| PDF regeneration on other hosts — **Implemented but not externally verified** | Python build source and optional pinned requirement | Executed only on this Mac | Build source, `requirements-docs.txt` | Linux PDF generation not run in CI |
| Microsoft investment choice — **Blocked by unconfirmed licensing / environment / baseline** | Cost drivers and decision gates | No procurement quote or tenant acceptance | `docs/financial-assumptions.md`, Hub handoff | No live deployment or entitlement assertion |
| User study / baseline measurement — **Planned** | Training and measurement plan | Not executed | KPI plan, pilot template | Full user task and accessibility review remain manual |

[Verification](VERIFICATION.md) records executed commands and limitations.
[Transformation report](TRANSFORMATION_REPORT.md) separates finished work from dependencies.
