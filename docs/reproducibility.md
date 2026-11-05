# Supported local scope and reproducibility

Linux/macOS: .NET 10 SDK, Python 3.11+, Make. Node 22+ and locked Playwright are optional
browser-test tools. Windows was NOT TESTED; Python wrappers avoid most shell-specific
startup assumptions, but Make and platform file-lock semantics still need validation.

The CI Python version is 3.12; the Mac verification uses Python 3.14. The default code
uses no third-party Python package. ReportLab 5.0.0 in `requirements-docs.txt` is an
optional PDF build dependency. Model inference needs a separately installed local Ollama
model; weights are not bundled and no cloud fallback or paid provider is configured.

Run from repository roots. The Hub's start_demo.py fixes the default store path relative
to that repository, so it survives restart regardless of the invoking directory. No
Node package outside the Hub lockfile is needed. PLAYWRIGHT_MODULE remains an explicit
advanced override, not an independent-review prerequisite.

Port 5088 must be free for isolated tests; occupied-port checks abort before test writes.
Never stop an unrelated process merely to make tests pass. Default seeding is idempotent
and preserves data. The agent integration accepts `--hub /path/to/Hub` if repositories
are not siblings. The release candidate is tested from fresh temporary checkouts before
push; hosted Linux results are recorded by exact workflow commit/run after execution.

Troubleshooting: SDK missing → install .NET 10; browser missing → install the locked
Chromium build with `npx playwright install chromium`; port busy → stop your own Hub;
corrupt JSON → retain file and follow the recovery runbook; model missing → use the
deterministic reference or install a model manually after reviewing its license.
