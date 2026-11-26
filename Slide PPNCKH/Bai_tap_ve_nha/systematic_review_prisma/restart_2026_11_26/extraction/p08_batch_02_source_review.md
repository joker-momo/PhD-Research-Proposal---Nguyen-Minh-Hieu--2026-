# P08 Batch 02 independent PDF review

**Verdict: FAIL.** The batch retains all 12 report IDs and 227 candidate entries. The row-level ledger records 56 PASS, 6 WITHHELD, and 165 NOT_YET_ASSESSED. Complete row-level reviews: R0074. Batch adoption remains 0/12 pending the gate.

| Criterion | Verdict | Evidence |
|---|---|---|
| Report and field coverage | PASS | 12/12 report PDFs verified using manifest SHA-256; 168/168 required field groups present in the candidate. |
| Preserve non-target entries | PASS | The parent candidate was compared entry by entry after the bounded repairs. Unchanged entries retain their original objects. |
| Recheck every prior excerpt exception | PASS | 4/4 exceptions reviewed below. Exact numeric data were not inferred from graph coordinates or by combining unmatched excerpts. |
| Account for every claim | PASS | 227/227 entries have a disposition in the ledger; unreviewed entries explicitly say NOT_YET_ASSESSED. |
| Complete the source and conditions review | FAIL | 165 entries still require semantic adjudication. Six entries are withheld. Counts and exact keys are in the ledger. |

## Prior excerpt exceptions

| Key | Source | Result |
|---|---|---|
| R0054 uav_architecture_role_and_topology:2 | p. 4 Fig. 1; p. 5 Fig. 3(c) and Table I | Replaced the stitched excerpt with the Fig. 1 caption and separate locators. An illustrative replay and an out-of-distribution experiment do not establish the Table I baseline counts. The baseline counts remain withheld. |
| R0073 quantity:1 | pp. 10–12, §5.2 and Figs. 4–6 | Moved the excerpt to p. 10. Recorded three distinct sets of conditions; the lost-UAV case uses AlexNet. The graphs provide no labeled exact coordinates for the outcome. Exact latency remains withheld. |
| R0121 outcomes_latency_energy_communication_accuracy_reliability_and_scalability:9 | p. 7, paragraph below Fig. 2 | Visual match. For six neighbors at delivery probability 0.70, modeled quorum probability is 0.93 for q=3 versus 0.74 for q=4. |
| R0121 quantity:4 | p. 7, same paragraph and Eq. (7) callout | Visual match. Subscripts are transcribed inline because PDF text extraction reorders the equation. |

The R0068 results define accuracy as the proportion satisfying constraints. Three outcome percentages still lack the underlying body aggregation; none enters synthesis. R0083 now separates the 100 m² latency experiment, the two battery scenarios and the 19-run result. R0095 now separates Table 2 sensitivity from Fig. 9 partitioning and single-decision metrics. The 40–230% prose comparison lacks a denominator that would support calling it a latency reduction. R0074 keeps latency values and relative percentages in separate units. The R0059 split evidence and R0062 approximate rate from the previous review remain intact.

## Local layout cross-check

MinerU 4.2.3 ran locally at `2026-11-27T00:09:12+07:00` and `2026-11-27T00:09:14+07:00` with `--format middle_json --tier flash --ocr-mode txt --pages 1`. The one-page PDFs were made with PyMuPDF 1.26.7 from SHA-256-verified originals. Split-file physical page 1 maps to the original physical page in the table. Coordinates in the MinerU column are normalized. The inputs and parser output stayed local.

| Source | MinerU regions and result | Original-PDF verification |
|---|---|---|
| `restart_2026_11_26/fulltext_retrieval/pdf/R0059.pdf`, physical p. 10, SHA-256 `9e8c96dbe6c3717efd91c23f02c3c8fcb10b8aa034ab7be150d9da74b85c0957` | Left results paragraph [0.090, 0.343, 0.493, 0.657]; Fig. 5 [0.090, 0.070, 0.924, 0.246]; Table 5 [0.099, 0.714, 0.915, 0.895]. The regions separate the figure comparison and bandwidth table. | Original pp. 9–10, §5.2.2, Fig. 5 and left column: the four percentages are tied to named partitioning baselines and the 10–80-task sweep. Table 5 belongs to a different bandwidth comparison. |
| `restart_2026_11_26/fulltext_retrieval/pdf/R0074.pdf`, physical p. 20, SHA-256 `f9dc09402cc09d3e426cc693458070cee2e480acab8f538da24ecbaa3c93d151` | Fig. 9 [0.280, 0.404, 0.913, 0.682]; results paragraph [0.277, 0.718, 0.943, 0.829]. The text supports 8.94%; the parser did not extract figure labels. | Original §4.7 and rendered Fig. 9: the body states the 8.94% break-even threshold. The figure labels the ordinate in ms and annotates the intersection and tick labels in s. The absolute intersection latency is withheld. |

Marker 1.10.2 independently processed only R0074 split page 1 (zero-based `--page_range 0`, CPU, JSON, no LLM), with exit 0 at `2026-11-27T00:12:36+07:00`. It located Fig. 9 as `/page/0/Figure/5`, bounding box [159.76, 337.13, 549.15, 580.52] pt, and reproduced 8.94% in the body. Its figure block contained no chart-label text. The PyMuPDF original-page render informs the unit decision.

Machine artifacts are recorded by SHA-256. The MinerU JSON hashes are `cdca65579465dfff0f82125a954c74f07afde08a4bbf09d14d47030bd4200acf` (R0059) and `9f44c7bf4f3d63b778a720b56ce64b2b575a73d9dedd2deaea54edc27e96972d` (R0074). The Marker JSON hash is `4661d5bdeab78b3016806c8cd814adc1ebde3c803bb2ea1bab6b948c66f40709` (R0074). These files are local working evidence. The audit ledger retains the physical-page locators and adjudications.
