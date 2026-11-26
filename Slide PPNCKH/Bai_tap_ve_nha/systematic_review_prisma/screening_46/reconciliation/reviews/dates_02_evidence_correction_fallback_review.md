# Date evidence correction review

Reviewed at: 2026-11-26T10:34:25+07:00
Primary: `01a215e6-a6fe-7bfa-8d4a-f99344b2ca3d` (quota-only, rejected).
Fallback: `01a215e6-bb3d-7065-a2ef-083a64b05bb6`; context `01a215e6-bb3d-7367-83a6-6edb66a3c098`.
Verdict: **ACCEPTED_ACCESS_LIMITATION_ONLY**. This accepts the documented shortfall, not a newly verified publication date or eligibility promotion.

| Criterion | Mandatory | Verdict | Objective evidence |
|---|---|---|---|
| D1 | yes | PASS | 6/6 exact supplied identities; DOI/title duplicates0;18 unique source IDs;12 unique attempt IDs;0 missing references. |
| D2 | yes | PASS | 12/12 requested routes represented,2 per record;12 tool-unavailable outcomes;6 local identity locators verified;0 remote publication quotations or aggregator dates;6/6 unresolved/manual-action fields. Independent web.open returns the same inaccessible-tool result for12/12 URLs. |
| D3 | yes | PASS | 6 UNCERTAIN decisions;0 new publication date assertions;0 administrative-date substitutions;fixed2021-01-01..2026-11-25 window. Previously accepted year-only publication evidence remains in the prior artifact and is not erased or reclassified. |
| D4 | yes | PASS | 12/12 unavailable clock/HTTP/final-URL fields explicitly null;0 claimed successful HTTP fetches;independent reviewer tool observations saved with runtime start/end. Acceptance uses the brief's explicit unavailable-tool shortfall allowance. Private provider execution trace is not exposed, so this does not certify provider per-request timing or HTTP traffic. |
| D5 | yes | PASS | Read-only structured output;project_files_changed0;final_prose_writtenfalse;explicit2 shortfalls and unresolved array;0 decision promotions,protocol changes,manuscript changes or remote messages. |

## Evidence boundary

Provider raw and parsed artifacts are retained unchanged. Independent source-access verification is in `dates_02_evidence_correction_independent_access.json`; it corroborates the tool limitation only. HTTP status, publication date, and server-side reason were not available. The outcome must not be paraphrased as publisher rejection, nonexistence of the papers, or proof of dates outside the window. The six accepted historical identities/year-level metadata remain controlling until new authoritative evidence is accepted. Overlay remains36 INCLUDE,2 EXCLUDE,8 UNCERTAIN at report level.

## Next action

Stop repeating this unavailable route. Keep six publication-date gates pending authoritative page/export evidence. Prepare report-version/study-family reconciliation from existing accepted full texts and identity evidence; mark missing equivalence as unresolved. Formal database search exports and two scope judgments remain separate gates.

## Process note

The pre-dispatch helper invocation referenced a removed `status_documents_fresh` function and failed. The router command nevertheless started in the same orchestration cell. No dirty state or stale evidence was present: the supported task-gate CLI was immediately run against the clean worktree and returned0 at2026-11-26T10:29:48+07:00. Future dispatch orchestration must check each precondition's exit status before continuing. No dispatch was duplicated.
