# Batch 07 — interrupted primary, rejected

Task ID: 01a214fe-2fce-723a-a467-83943cc4d44b
Context ID: 01a214fe-2fce-7441-a8bf-3bc8a78a60f1
Reviewer: Codex
Reviewed at: 2026-11-26T06:20:54+07:00
started_at: 2026-11-26T06:15:33+07:00
updated_at: 2026-11-26T06:20:54+07:00
completed_at: 2026-11-26T06:20:54+07:00

| Criterion | Mandatory | Verdict | Objective evidence |
|---|---|---|---|
| A1 records | yes | FAIL | 0/5 records, 0 artifacts returned |
| A2 identities | yes | FAIL | 0/5 identities available |
| A3 source locators | yes | FAIL | 0/40 locators available |
| A4 eligibility | yes | FAIL | 0/5 decisions available |
| A5 evaluation limits | yes | FAIL | 0/5 classifications available |
| A6 output and uncertainty | yes | FAIL | No structured result; mutations not independently established |

Verdict: **REJECTED_TRANSPORT_FAILURE**, not a scientific exclusion.
The supported task-get response explicitly reports server interruption and
TASK_STATE_FAILED. No evidence is adopted and no report counts change.
Server recovery used its existing configuration; no model escalation or fallback.
Source input checks before interruption: 5/5 PDF hashes and 5/5 text files present,
64 PDF pages. Keep this primary transport immutable. Retry the same committed
brief only after this task is committed, merged and cleaned; use distinct retry
artifacts linked to this task. No manuscript changes.
