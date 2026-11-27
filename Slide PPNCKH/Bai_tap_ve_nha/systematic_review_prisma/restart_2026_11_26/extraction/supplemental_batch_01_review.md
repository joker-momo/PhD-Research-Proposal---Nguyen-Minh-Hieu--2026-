# Supplemental P08 batch 01 original response review

Native Task 15cbc890-5eb8-41d6-ad0a-52686af3dd74. The bridge reported completion and verified chat deletion. The result is quarantined pending an accepted correction and independent semantic review.

| Acceptance criterion | Verdict | Evidence |
|---|---|---|
| Exact scope and JSONL | FAIL | 7/7 access IDs and 89/91 parseable field keys. R0036 workload and code_data and the optional R0058 quantity row fail JSON parsing. No duplicate or additional report IDs observed. |
| Original PDF verification | FAIL | 7/7 attached PDF hashes match. The mechanical audit records 43 exceptions including the three JSON errors, the R0058 access excerpt, and page or quote errors in several fields. Some source claims also combine conditions or use an unwarranted precision. |
| Numerical provenance | FAIL | Five optional quantities parse. R0014 and R0075 fail the quoted-locator test. R0036's improvement lacks a matched denominator in its cited source. Text conditions and numerical labels require separate semantic review. No quantities accepted from this payload. |
| Explicit shortfalls and stable transport | FAIL | The response claims 91 field rows and no unresolved keys, despite two unparseable field rows. Its end marker is present. Read-only parent mode and cleanup passed. |

Correction scope is 47 failed or uncertain keys: 46 field rows (including both malformed keys) and the R0058 access row. The original did not close any report. Already supported excerpts remain available for composite review after the correction. No additional report, status or eligibility decision is requested.
