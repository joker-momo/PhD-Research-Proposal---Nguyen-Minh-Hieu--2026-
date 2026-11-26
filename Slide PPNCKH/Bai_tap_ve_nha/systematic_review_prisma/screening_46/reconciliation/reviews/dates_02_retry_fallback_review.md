# Dates02 retry fallback review

Task ID: 01a215dc-cc27-73fb-8933-0a471cf3ac32
Context ID: 01a215dc-cc27-7622-85d9-41ed5c597739
Reviewer: Codex
Reviewed at: 2026-11-26T10:22:52+07:00
started_at: 2026-11-26T10:18:30+07:00
updated_at: 2026-11-26T10:22:52+07:00
completed_at: 2026-11-26T10:22:52+07:00
Verdict: REJECTED_D2_D3_D4

| Criterion | Mandatory | Verdict | Objective evidence |
|---|---|---|---|
| D1 | yes | PASS | Exactly6 requested IDs,0 identity changes/normalized duplicates. |
| D2 | yes | FAIL | 25 source entries and13 attempts,0 unresolved source references, but discovery claims lack actual result URLs and attempts are not independently traceable. Historical local timestamps are asserted without precise prior-source pointer. |
| D3 | yes | FAIL | All6 decisions remain UNCERTAIN correctly; however6 Crossref published.date-parts sources are mislabeled non_publication. They are publication evidence with insufficient year precision, not administrative dates. |
| D4 | yes | FAIL | 13/13 new attempts timestamp10:17:33+07 before fallback dispatch10:18:41+07; not actual fetch times. Output admits using a task timestamp. Cannot reconstruct exact historical fetches by guessing. |
| D5 | yes | PASS | No other-gate/corpus change; project_files_changed0;final_prose_writtenfalse;shortfall explicit. |

## Next corrective task

Preserve this raw output; no findings adopted. Prepare a corrective brief requiring
new bounded direct Crossref and publisher reads for all6 IDs with actual start/end
timestamps captured by code for EACH attempt. Retain year-only published fields as
publication evidence, preserving precision; inaccessible dates remain UNCERTAIN.
Do not fabricate old timestamps or Google result URLs. Remove aggregator date
claims unless their original destination URL and observed text are supplied.
Exactly6 records and fixed cutoff remain. No transport retry is needed: this
result is terminal; a targeted evidence correction is required.

CODE_FIRST_DECISION: REUSE_EXISTING -- approved router/task-get and registered
task gate; stdlib JSON assertions found13/13 pre-dispatch times and6 type errors.
