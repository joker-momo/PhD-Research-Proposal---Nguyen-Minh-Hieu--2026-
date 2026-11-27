# RQ5 source verification before manuscript revision

The review applies the [locked post-protocol rule](rule.md) to the [frozen manifest](manifest.json). The physical page count, audited results pages, source blocks, and any reasons for withholding an entry are in [report coverage](report_coverage.csv). The [outcome ledger](outcomes.csv) retains the reported quantities, units, comparator, scenario, analysis denominator where reported, and the source excerpt or table transcription.

| Acceptance criterion | Verdict | Observed evidence |
|---|---|---|
| All 46 included reports represent 46 distinct studies, with no duplicate or missing key. PDFs must open and match the pinned SHA-256. | PASS | 46/46 report IDs and 46/46 study IDs. All source files opened with PyMuPDF 1.26.6. All 46 source hashes matched. |
| Every report has an examined, valid physical results page and source block. Each outcome entry points into its report's audited pages. | PASS | 46 report coverage rows. All 106 outcome rows have unique keys, a valid physical page and a section, table, figure or caption locator. |
| Every ledger row retains source evidence and documents comparability. | PASS | 99 rows have a text-verified excerpt and a numerical token check. Seven visually transcribed rows were checked on original-page renders for R0048 p. 12, R0054 p. 5 and R0095 p. 10. Checked units, comparator columns, qualifiers and conditions against the original source. |
| Every report has an explicit disposition. | PASS | 35 with a verified numerical entry. Ten with exact-value gaps recorded in the plot-only category. R0113 has a printed result whose measurement context does not meet the rule. |
| Counts reconcile and held or repeated results stay out of RQ5 totals. | PASS | 106 ledger rows. Retained set: 51 matched within-study entries from 23 studies plus 46 descriptive entries. Excluded from the 97 retained entries: seven held and two cross-references. |
| Every planned numerical comparison in the manuscript is checked on the original PDF. | PASS | R0080 pp. 5–6, Table I and its bandwidth condition. R0092 p. 13, Table V and its all-arrival denominator. R0110 p. 13, Table IV, distinguishing successful-mission latency from all-seed completion. |
| The four outstanding report statuses stay outside the included-review universe. | PASS | R0081, R0082 and R0132 await classification. R0116 remains unretrieved. No selection change. |

## Scope and verification decisions

The ten plot-only reports are R0001, R0002, R0022, R0043, R0044, R0045, R0068, R0073, R0077 and R0145. Original-page plots were checked without estimating values from curves. Some reports give a broader summary elsewhere without the checked metric or evaluation conditions. The report-level category describes availability under this rule. R0113 has an unresolved measurement modality and comparator context and remains an included study.

Recovery-time, tail-latency, inferred transmission time and completed-run latency retain separate definitions. R0080 Table I's bandwidth condition is reported on the following page. R0092 Table V reports energy in Wh. R0110 Table IV conditions per-token latency on completed missions, with unequal completion across the compared methods. R0121 Table 3 contains analytical transmission times for one hop. The coverage inventory is selective within each domain. It does not estimate primary reporting prevalence or support pooling. Source verification is by Codex, with mechanical checks and original-page inspection where required. Reviewers did not perform independent duplicate human extraction in this pass.
