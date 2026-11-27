# Gemini.app initial audit · FAIL, quarantined

Task UUID `f60d888e-ce8c-4895-a1de-2322204862d6`, context `9acab103-4d8e-49e8-a8d4-a2515f594d63`. The bridge timed out. A complete 26-row result was independently captured from two identical terminal snapshots. The bridge's automatic recovery refused because the app exposed a stale worker progress row as an additional user turn. No second send or deletion confirmation occurred.

| Criterion | Verdict | Evidence |
|---|---|---|
| 1. Exact coverage | PASS | 26/26 expected ID–DOI pairs and no extra IDs. |
| 2. First-party identity | FAIL | Seven identities marked unresolved. A false author mismatch for R0022 comes from a secondary profile: the Crossref record and original PDF p. 1 give Chen Xu, not Lei Xu. Several other identities rely only on third-party indices or profiles. R0083's third author is supported independently by the original PDF and Crossref. |
| 3. Deduplication | PASS | 0 duplicate ID or DOI pairs and 0 normalized duplicate titles among non-null titles. |
| 4. Notice disposition and limits | FAIL | 21/26 unresolved. Several rows supply only third-party listing or author-profile URLs; these do not document an attempted check of the required first-party notice source. |
| 5. Formal notice traceability and source boundary | FAIL | No claimed formal correction, concern or retraction, but 1 out-of-bound host supplied for R0044 and 1 contradicted author claim for R0022. Neither is used. |
| 6. Outstanding keys and completion | PASS | 26 returned IDs, 21 unresolved ID unions, nonoverlapping allocations from five workers, completion marker within the matching UUID-delimited response. |

The correction is limited to the 21 publication rows associated with failed fields. The five resolved rows are preserved for composite validation. Independent publisher-registered and Retraction Watch evidence in this dossier is separate from the rejected Gemini result.

[Saved terminal payload](source_audit_native_payload.json) · [Recovery receipt](source_audit_recovery.json) · [Cleanup receipt](source_audit_cleanup.json)
