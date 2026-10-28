from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from playbook import ROOT, report
actual = json.loads((ROOT / "output/business-case.json").read_text())
if actual != report():
    raise SystemExit("Stale output: run python3 playbook.py --output output/business-case.json")
print("Committed business-case report: reproducible")
