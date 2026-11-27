# Step 16 source audit, composite acceptance

The linked correction `ee609ba8-1c3d-4d4e-a01a-59425b5fd23a` finished on 2026-11-27 at 15:25:08 +07:00. The primary audit `78bde50a-7fb8-46d6-822f-9cd3cb26147f` remains recorded as FAIL. Only its six independently supported reference rows contribute to the reviewed composite. The correction uses the dated first-party records captured by Codex.

| Criterion | Verdict | Evidence |
| --- | --- | --- |
| Exact scope | PASS | 41/41 expected corrected IDs, six supported primary IDs and zero overlap. 47/47 bibliography keys and 46/46 registered DOIs. R0113 alone carries DOI_NOT_FOUND and has a publisher and original-page locator. |
| Structure and duplicates | PASS | 41 parseable JSONL objects, one matching summary, one standalone completion marker, zero duplicate fields, zero duplicate normalized DOIs and zero undocumented unresolved rows. |
| Source identity | PASS | All 41 corrected titles, ordered full bylines, issue years and venues match the supplied source rows. The six primary rows match the independent records. R0058 retains issue 2026 with online date 2025-12-06. The primary's R0006 and R0009 discrepancies resolved against the registered article data and original PDF. |
| Notice scope | PASS | Each corrected row maps to its DOI work record W, reverse lookup U and Retraction Watch extract RW. The six supported primary rows identify their first-party source. The independent check found zero notices within the recorded scope. The correction explicitly limits findings to supplied first-party snapshots. |
| Independent Codex verification | PASS | All 46 registered DOI works and reverse lookups returned HTTP 200. The official dated dataset scan covered 74,131 rows. R0113's exact title was checked there and its identity was verified on the publisher article record and original physical p. 1. Publisher notice coverage remains non-exhaustive. |
| Task closure | PASS | The exact parent and correction UUIDs and complete raw payloads are saved. The bridge verified matching completed chat deletion for both and restored chat mode. |

[Independent source evidence](active_independent_registry_evidence.json), [primary PASS/FAIL review](active_source_audit_primary_review.md), [correction checks](active_source_audit_correction_checks.json)
