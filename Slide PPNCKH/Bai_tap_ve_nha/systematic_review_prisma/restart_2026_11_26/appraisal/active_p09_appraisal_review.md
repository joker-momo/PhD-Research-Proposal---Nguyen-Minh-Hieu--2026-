# P09 · Active appraisal verification

Completed `2026-11-27T14:35:14+07:00` for HK261 step 12.

| Criterion | Verdict | Evidence |
| --- | --- | --- |
| Locked inputs and source identity | PASS | Historical appraisal files retain their locked SHA-256 values. Active report and study identities match the 46-report P08 lock. |
| Full appraisal coverage | PASS | 25 prior reports/250 domain judgments and 21 supplemental reports/210 judgments. Both tables contain the same 460 distinct decided keys. |
| Original traceability | PASS | 1054 locator rows with physical pages and sections. The supplemental batch reviews retain adopted and rejected findings by task ID and checked source. |
| Scope | PASS | Appraisal uses ten systems/simulation domains to qualify synthesis. Every included report retains its P07 study assignment. Unresolved screening and retrieval dispositions are outside the appraisal. |
| Review model | PASS | Gemini.app supplied structured findings and Codex checked them against the originals. This is one AI-assisted appraisal workflow. |
| Native chat cleanup audit | RECORDED EXCEPTION | 1 unverified cleanup receipts. Readable saved answers, PDF appraisal and cleanup verification are audited separately. |
| Gate | PASS | Formal report-count and study-count reconciliation may begin. |

- [Domain table](active_appraisal_table.csv)
- [Rationale and original locators](active_appraisal_rationale_matrix.csv)
- [SHA-256 lock](active_p09_appraisal_lock.json)
