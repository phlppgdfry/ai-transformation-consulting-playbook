# Process transformation and model provenance

The [AS-IS](../process/as-is.bpmn) and [TO-BE](../process/to-be.bpmn) models are copied
from the companion Automation Hub on 29 October 2026 with the same MIT license and
fictional case. They retain BPMN 2.0 semantics and add explicit diagram layout; they are
not executable flows or Power Automate exports. Keep shared rule changes coordinated
across repositories. No private lab material is included.

Current-state bottlenecks are hypotheses: incomplete inputs, queue hunting, approval
waiting and reconciliation of email decisions. The future process validates inputs,
selects a queue deterministically, waits for human review and saves a reason/version.
Operations is accountable for intake and turnaround; Finance owns expense policy and
IT owns access decisions. A status change does not book money or grant permissions.

Exceptions: invalid data returns an actionable error; duplicate submission keeps its
original key; a conflicting decision requires refresh; policy uncertainty goes to an
owner; stale work needs manual follow-up until a calendar-aware scheduler exists.
Dashboard timing in the local app is demo elapsed time, not evidence of the assumed
12-to-5-minute active handling improvement. Measure active work, waiting and rework
separately in the pilot.
