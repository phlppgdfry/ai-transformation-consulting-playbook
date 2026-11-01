# Verification record — 29 October 2026

Environment: macOS, Python 3.14, ReportLab 5.0.0, system Poppler. Synthetic scenario.

| Executed command / check | Result |
|---|---|
| Initial `make verify` | 9 tests, committed baseline report and docs passed |
| `python3 financial_model.py` | Produced ramp year-one net EUR -7,695 and payback month 25 |
| Updated `make verify` | 15 tests, baseline report reproducibility and docs passed |
| `python3 scripts/build_executive_pdf.py` | Ten-page landscape executive PDF generated |
| `pdfinfo deliverables/noordwerk-executive-brief.pdf` | Ten pages, 960×540 points, selectable text, untagged |
| `pdftoppm -scale-to 1100 -png ...` | All ten pages rendered; every rendered page visually inspected |
| Cost reconciliation tests | EUR 12,000 implementation and EUR 350 monthly allowances reconcile to original model |
| Limited credential-pattern scan | 0 findings in 44 text files at scan time; not comprehensive secret assurance |
| XML/BPMN layout and ID reference check | Both laid-out models valid locally; external editor not tested |
| Ramp/sensitivity tests | No-benefit months, no-adoption, unfavourable cases and committed-output consistency pass |

The PDF contains the companion Hub's actual synthetic-data screenshot. Process and
architecture are authored technical diagrams, not fabricated Microsoft screenshots.
Charts use committed financial output. The deck shows assumptions and negative economics;
it does not claim workshop attendance, user research, customer savings or sponsor approval.

The original 20.17-month result assumes immediate steady-state benefits. The extension's
month 25 is first non-negative cumulative month after an adoption ramp; do not compare
these as identical measures. No vendor quote, discounting, tax, seasonality or actual
benefit realisation is modelled. PDF generation was not tested on Linux or in PowerPoint.
The PDF is not tagged for full accessible-PDF compliance and is not an editable PPTX.
