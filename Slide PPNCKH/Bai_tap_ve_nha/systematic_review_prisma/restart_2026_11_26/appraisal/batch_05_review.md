# Batch 05 · Appraisal source review

Reviewed at `2026-11-27T01:43:51+07:00`. Native Gemini.app Task `c960ad8f-d8c5-4e8e-8b2e-e3569a96d42f`, context `0bc99028-dbaf-4e1b-bf77-b7c793b98952`. Sent once.

| Criterion | Verdict | Evidence |
| --- | --- | --- |
| Exact scope | PASS | 50/50 unique domain keys, 0 duplicates/extra/malformed rows. |
| Original access | FAIL | 4/5 access probes match source. R0083 p3 substitutes a printed variable. The original PDF is locally readable and its hash matches. |
| Locator and transcription | FAIL | 91/93 non-null per-judgment quotes match. R0083/D04 and R0121/D02 require exact source transcription. |
| Scientific support | FAIL | Seven keys need correction or narrower attribution: R0074 D06/D08, R0089 D03, R0095 D05 and R0121 D03/D05/D07. Corrections separate distinct trials, bound evaluation conditions/latency components, and distinguish analytical assumptions and calculated outputs from tested outcomes. |
| Independent PDF review | PASS | 50/50 keys checked against original evidence; 41 outside the correction are preserved pending the full batch verdict. |
| Receipt and cleanup | PASS | The original task timed out in the bridge. The completed payload was recovered using the same UUID, stored, and the original chat deletion verified. |
