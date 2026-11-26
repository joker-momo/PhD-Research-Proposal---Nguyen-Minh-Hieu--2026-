# P08 Batch 01 independent PDF review

**Verdict: FAIL.** The batch retains all 13 report IDs and 228 candidate entries. The row-level ledger records 198 PASS, 3 WITHHELD, and 27 NOT_YET_ASSESSED. All rows adjudicated for R0001, R0002, R0003, R0006, R0009, R0010, R0015, R0019, R0022, R0029, R0045. Batch adoption remains 0/13 pending the gate.

| Criterion | Verdict | Evidence |
|---|---|---|
| Report and field coverage | PASS | 13/13 report PDFs verified using manifest SHA-256; 182/182 required field groups present in the candidate. |
| Preserve non-target entries | PASS | The parent candidate was compared entry by entry after the bounded repairs. Unchanged entries retain their original objects. |
| Recheck every prior excerpt exception | PASS | 4/4 exceptions reviewed below. Three table cells are visually verified despite being absent from the text layer. |
| Account for every claim | PASS | 228/228 entries have a disposition in the ledger; unreviewed entries explicitly say NOT_YET_ASSESSED. |
| Complete the source and conditions review | FAIL | 27 entries still require semantic adjudication. Three numeric entries are withheld. Counts and exact keys are in the ledger. |

## Prior excerpt exceptions

| Key | Source | Result |
|---|---|---|
| R0022 compute_and_radio:1 | p. 5, Table I; Figs. 4–5 | Visual match. Preserves the bounds of 1–2 GHz and uses the stated complex-normal coefficient. The figures supply the bandwidth sweep separately. |
| R0048 quantity:1 | p. 12, Table III, efficiency 0.7 row | Visual match for 0.511 s and the separate paragraph identifying 60 UAVs. Retained. |
| R0048 quantity:2 | p. 12, Table III, efficiency 0.7 row | Visual match for 670.8 J in the same row. Retained. |
| R0048 quantity:3 | p. 12, Table III, efficiency 0.7 row | Visual match for 117.4 IPS in the same row. Retained. |

In R0006, the printed 37% conflicts with the comparator latencies and is omitted. The relative reduction from 1,239 ms to 527 ms is about 57.5%, using the comparator as the denominator. The 47% and 87% coverage values were checked separately against Fig. 4 and its text. R0009 now retains all four baseline-specific energy percentages at a coverage radius of 50 m. The 80-user result belongs to Fig. 6(b); the explicit 50-episode statement from the radius sweep was removed from its conditions. R0044 now distinguishes model, bandwidth and reliability comparisons. R0003 preserves the reported Table I values and explicitly flags the inconsistent AlexNet top-k label. Two R0010 introduction-level aggregate percentages lack study-specific conditions in the result passage. The R0045 14.6% abstract figure remains withheld.

## Source recheck from d16c167

Recorded at `2026-11-27T00:20:24+07:00`. Prior PASS entries retained. The remaining unresolved review keys are listed as NOT_YET_ASSESSED in the [source ledger](p08_source_inventory.json).

| Key | Disposition | Physical PDF evidence |
|---|---|---|
| R0010 `quantity:1` | EXCLUDE_EXACT_VALUE | Physical p. 2 Introduction gives the AlexNet average. Figure 5(a) and discussion on pp. 5–6 do not specify comparator weights or reconstruct the reported aggregation. Retain the already verified qualitative sweep only. |
| R0010 `quantity:2` | EXCLUDE_EXACT_VALUE | Physical p. 2 Introduction gives the GoogLeNet average. Figure 5(b) and discussion on pp. 5–6 do not specify comparator weights or reconstruct the reported aggregation. Retain the already verified qualitative sweep only. |
| R0045 `quantity:1` | EXCLUDE_EXACT_VALUE | p. 1 Abstract states 14.6%. §IV.B, Figs. 5–8 on pp. 9–10 do not label a matching comparison, denominator and exact value. Use only the scoped qualitative comparisons. |

## Source recheck from 55023bb

Recorded at `2026-11-27T00:25:17+07:00`. Independent review verified original PDF hashes for 25/25 reports. This batch has 198 PASS, 3 previously adjudicated exclusions, and 27 pending entries. Pass/fail evidence by key is in the [source ledger](p08_source_inventory.json). Existing PASS entries and exclusions were preserved. Batch adoption remains zero.
