# HK261 RQ5 manuscript verification

Branch `codex/hk261-desk-reject-revision`. The outcome sources were locked in `af6aa3e` before finalizing the manuscript in `6869e63`. The [source review](review.md) records the extraction decisions.

| Acceptance criterion | Verdict | Observed evidence |
|---|---|---|
| Build the Springer Nature LaTeX manuscript and inspect the changed pages. | PASS | Tectonic built the 16-page PDF. All pages were rendered for visual inspection. RQ5 and Tables 2 and 4 were inspected at reading size on physical pp. 8–10. |
| Manuscript and ledgers agree. | PASS | The abstract and §3.6 report 98 entries across 36/46 studies. §3.6 records 51 matched entries from 23 studies and 47 descriptive entries. All five mechanism rows and totals in Table 4 match the ledgers. |
| Method, limitations and supplements expose the same rule. | PASS | Methods detail the post-protocol rule and matched-comparison criteria (pp. 3–4). Limits explain selective representation (p. 10). Supplement S3 points to the four source records (p. 11 and manuscript README). |
| Retain accurate sources and page locators. | PASS | No undefined reference, missing citation or overfull box was detected. The rendered PDF contains 50 numbered references and 49 distinct DOI links. All new supplement links resolve and the active PRISMA checklist retains 27 numbered items. |
| Reconcile the fixed selection ledger. | PASS | Four reconciliation tests passed. Counts remain 136 full texts assessed, 46 included, 87 excluded and three awaiting classification (R0081, R0082 and R0132). R0116 is the sole unretrieved report. The selection ledger, flow PDF and bibliography are byte-identical to their `ff1cf4b` versions. |
| Keep the two revision paths independent. | PASS | The merge base between this branch and the alternative branch remains `7a6675d`. The manuscript commit is local to the requested branch. |

The TeX engine reported underfull-box and input PDF version warnings. Inspection found the revised content visible and the flow diagram readable. Author information and declarations still await confirmation. The earlier coursework ZIP documents its own release checkpoint.

SHA-256 of the build inputs and outputs:

```text
0458317750f4332a896ebcdb3d919803c51726bd7ddae8b659e16bbbd893c817  manuscript/sn_computer_science/main.tex
129acde1e7358ca51b5354d4424c64dc7ec034937c23fe48cc296de33424469e  manuscript/sn_computer_science/main.pdf
0a0bf5f7f6aca955c65ca5ca4944745ad2070174f125f150101c5b3a380cda50  restart_2026_11_26/extraction/rq5_uniform/outcomes.csv
939d9030dc234c92aec97fbddbf1cd4abb4ea11f1b954232bcc95f6820629803  restart_2026_11_26/extraction/rq5_uniform/report_coverage.csv
ce3d4d7355890b41b4534d43fa641dadc5d406d8749eeee9562fbbbb09818bad  restart_2026_11_26/extraction/rq5_uniform/claim_source.csv
```
