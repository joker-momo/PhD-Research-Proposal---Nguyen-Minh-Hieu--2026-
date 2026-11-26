# Family phase closure

Task ID: 01a215ee-a956-71fb-9e40-cd6c79a1f26d
Reviewer: Codex
Reviewed at: 2026-11-26T10:50:28+07:00

Provider verdict: **REJECTED_NO_EVIDENCE**. Primary returned quota. Fallback was still working without artifacts when the user approved a reduced critical path; Codex canceled the broad investigation to stop unnecessary work. Supported task-get confirms TASK_STATE_CANCELED at 2026-11-26T10:49:31.640+07:00. This was a scope change, not a claim that an observation timeout meant completion. No redispatch or retry is authorized by this closure.

| Criterion | Mandatory | Verdict | Objective evidence |
|---|---|---|---|
| F1 | yes | FAIL | Provider returned 0/46 structured records. |
| F2 | yes | FAIL | Provider returned 0 source-version observations or checked quotes. |
| F3 | yes | FAIL | Provider returned no pair-screen evidence. |
| F4 | yes | FAIL | Provider supplied no two-sided linkage evidence; no positive linkage adopted. |
| F5 | yes | FAIL | Required final structured declarations absent; no provider artifact available for acceptance. |

The latest user instruction supersedes retry-on-failure for this phase: retain mechanical candidates as UNRESOLVED, do not merge without two-sided locators, and move to the search/export blocker.

| Reduced closure gate | Verdict | Objective evidence |
|---|---|---|
| Account for every report | PASS | Mechanical derivative contains exactly 46 ordered identities copied from accepted inputs. |
| No unsupported merge | PASS | 0 merges and 0 assigned study IDs; final study count null. |
| Preserve unresolved candidates | PASS | All 1,035 metadata pairs compared; 37 candidates retained as UNRESOLVED; 0 duplicate pairs. No exact normalized DOI/title duplicates found. |
| No repeated provider task | PASS | One primary and one quota-authorized fallback; existing fallback canceled after scope reduction; no redispatch. |

## Boundary

`family_01_mechanical_candidates.json` is a deterministic index, not a research conclusion. It uses DOI/title equality, at least two shared normalized author names, and title-token Jaccard at least 0.35. It does not prove that unrelated-looking papers are independent, nor that similar papers share data. No full-text extension search was performed by this derivative. The 37 candidates remain visible for focused scientific adjudication before any final study-level aggregation. Report-level eligibility remains 36 INCLUDE, 2 EXCLUDE, 8 UNCERTAIN; manuscript remains unchanged.

The three old plan/audit documents are synchronized with this evidence boundary in the same phase commit. No new hooks, dependencies or research scripts were introduced.
