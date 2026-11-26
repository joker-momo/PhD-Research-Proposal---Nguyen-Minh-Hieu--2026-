# P08 Batch 01 independent PDF review

**Verdict: FAIL.** The batch retains all 13 report IDs and 228 candidate entries. The row-level ledger records 86 PASS, 3 WITHHELD, and 139 NOT_YET_ASSESSED. Complete row-level reviews: R0001, R0002, R0003, R0015. Batch adoption remains 0/13 pending the gate.

| Criterion | Verdict | Evidence |
|---|---|---|
| Report and field coverage | PASS | 13/13 report PDFs verified using manifest SHA-256; 182/182 required field groups present in the candidate. |
| Preserve non-target entries | PASS | The parent candidate was compared entry by entry after the bounded repairs. Unchanged entries retain their original objects. |
| Recheck every prior excerpt exception | PASS | 4/4 exceptions reviewed below. Three table cells are visually verified despite being absent from the text layer. |
| Account for every claim | PASS | 228/228 entries have a disposition in the ledger; unreviewed entries explicitly say NOT_YET_ASSESSED. |
| Complete the source and conditions review | FAIL | 139 entries still require semantic adjudication. Three numeric entries are withheld. Counts and exact keys are in the ledger. |

## Prior excerpt exceptions

| Key | Source | Result |
|---|---|---|
| R0022 compute_and_radio:1 | p. 5, Table I; Figs. 4–5 | Visual match. Preserves the bounds of 1–2 GHz and uses the stated complex-normal coefficient. The figures supply the bandwidth sweep separately. |
| R0048 quantity:1 | p. 12, Table III, efficiency 0.7 row | Visual match for 0.511 s and the separate paragraph identifying 60 UAVs. Retained. |
| R0048 quantity:2 | p. 12, Table III, efficiency 0.7 row | Visual match for 670.8 J in the same row. Retained. |
| R0048 quantity:3 | p. 12, Table III, efficiency 0.7 row | Visual match for 117.4 IPS in the same row. Retained. |

In R0006, the printed 37% conflicts with the comparator latencies and is omitted. The relative reduction from 1,239 ms to 527 ms is about 57.5%, using the comparator as the denominator. The 47% and 87% coverage values were checked separately against Fig. 4 and its text. R0009 now retains all four baseline-specific energy percentages at a coverage radius of 50 m. The 80-user result belongs to Fig. 6(b); the explicit 50-episode statement from the radius sweep was removed from its conditions. R0044 now distinguishes model, bandwidth and reliability comparisons. R0003 preserves the reported Table I values and explicitly flags the inconsistent AlexNet top-k label. Two R0010 introduction-level aggregate percentages lack study-specific conditions in the result passage. The R0045 14.6% abstract figure remains withheld.
