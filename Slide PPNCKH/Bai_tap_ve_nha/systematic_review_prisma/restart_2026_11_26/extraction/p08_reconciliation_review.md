# P08 reconciliation and source review

**Initial gate: FAIL.** This checkpoint retains a quarantined candidate for the two batches. It does not authorize synthesis, a dataset lock, or progression to Step 12.

## Acceptance

| Criterion | Verdict | Evidence |
|---|---|---|
| Exact identity coverage | PASS | 25/25 manifest IDs and 25 distinct DOIs. The candidate contains all 14 required field groups per report (350/350). Batch 01 covers 13 IDs and Batch 02 covers 12. |
| Narrow integration | PASS | 43 targeted Batch 01 keys and four Batch 02 source groups (R0062 and the three R0059 comparators). The candidate incorporates 26 prior reviewed Batch 02 correction rows. All other source entries were compared without differences. Prior inputs and verdicts remain intact. |
| Original PDF integrity | PASS | 25/25 SHA-256 digests verified against the extraction manifest before reading. The source inventory records the digests, physical pages and individual mechanical checks. |
| Locator and text review | FAIL | 455 candidate entries (387 field entries and 68 quantitative entries) inventoried using PyMuPDF 1.26.7. 444 normalized excerpts match the declared page under at least one text order, 8 require layout or quote review, and 3 intentionally withheld R0068 entries have no body locator. Matching is mechanical and does not confer scientific acceptance. |
| Batch 01 semantic acceptance | FAIL | 13/13 PDFs inspected in context for at least one outcome. Confirmed issues include R0006, R0009 and R0044. Remaining fields and compound assertions require source-level adjudication. Full reports accepted: 0/13. |
| Batch 02 semantic acceptance | FAIL | 12/12 PDFs inspected in context for at least one outcome. Confirmed issues include R0068 and R0095. Remaining fields and compound assertions require source-level adjudication. Full reports accepted: 0/12. |
| All assertions verified and lock authorized | FAIL | 25/25 reports received an initial source-context check. This checkpoint does not establish exhaustive semantic verification of the 455 entries. |

## Source-context findings

Physical page numbers are one-based. Each row records the specific outcome or clause inspected. Unmentioned clauses and fields remain pending in this checkpoint, including quantitative denominators, workloads and conditions when those were outside the inspected passage.

| Report | Page and source context | Finding |
|---|---|---|
| R0001 | p. 3, Figs. 2–3 and adjacent text | The reward comparisons support the direction of the CAPRI result under the tested configurations. The count of baselines is outside this clause check. |
| R0002 | p. 8, Fig. 4 discussion | The text links more frequent migrations to extra cost and greater task success. The cost and success comparison is study-specific. |
| R0003 | p. 6, Fig. 2a–b, Table I | Utility drops as request count increases in both pairings. DMS tops the reported utility comparisons. Table I includes faster Small-only rows, so the result cannot be recast as lowest latency. |
| R0006 | p. 7, Fig. 5 and discussion | The text gives 527 ms and 1,239 ms for Two-Stage and its closest listed comparator. The separately stated 37% is inconsistent with their difference divided by 1,239 ms (57.5% rounded). Withhold the 37% assertion pending reconciliation. |
| R0009 | p. 9, Fig. 5 discussion | 1,536.9 J at 50 m is supported. The source lists 22.6%, 35.5%, 17.6% and 54.2% against named baselines. The candidate's 22.6–54.2% range omits the smallest comparator-specific reduction. |
| R0010 | p. 5, discussion of Fig. 5 | In the task-count sweep, the source describes lower total latency and slower growth in latency for the proposed method across the three evaluated models. |
| R0015 | p. 6, Table II and surrounding prose | The text describes similar runtimes for EECIA, Random, Nearest and DistInference and identifies OPT as having the longest runtime. |
| R0019 | p. 12, discussion of the three CNNs | The passage confirms the three reported accuracy percentages. The metric definition and the other latency and comparator results need their own locators. |
| R0022 | p. 6, Fig. 5 discussion | Lowest execution latency is supported within the compared bandwidth settings. This text does not alone establish the separate energy and convergence statements. |
| R0029 | p. 5, evaluation discussion | The 700 ms AlexNet sentence explicitly maps 45.5%, 36.8% and 36.0% to RA, PSO and GA. The poor-environment clause requires its own context. |
| R0044 | p. 7, Figs. 3–4 discussion | The source limits its lowest-delay statement to most classical DNNs. The candidate generalizes across all listed DNNs and performance measures. |
| R0045 | p. 10, Figs. 6–8 discussion | The text supports study-specific energy comparisons for SAC+CVX. It does not independently establish fastest convergence or a universal result across sweeps. |
| R0048 | p. 12, Table III | The body places Table III in the 60-UAV sensitivity analysis. The table does not establish the separate scaling and superiority claims over 40–200 UAVs. |
| R0054 | p. 4, main results and Table I | The main-results paragraph corroborates the four GAT-HSMAO held-out metrics in the outcome field. The dispersion column and evaluation protocol still require their own field-level check. |
| R0059 | pp. 7, 8, 10, overhead and both comparison passages | Confirms three separate outcomes: coordination overhead relative to a layer output, latency against model-switching baselines, and latency against partitioning baselines. Units and comparator groups must stay separate. |
| R0062 | p. 6, stages 2–3 of the prototype experiment | Stage 2 describes continued inference at about 2 FPS. Stage 3 describes a return to the Stage 1 level after communication restoration. The Stage 2 approximation must remain. |
| R0063 | p. 13, evaluation table | The cited table row supports a subset of the listed scenario results. That locator alone does not cover the separate latency and traffic experiments bundled in the field. |
| R0068 | pp. 10–11, Fig. 4 and continued text | The paper defines accuracy in this passage as the percentage satisfying the constraints. The candidate's unqualified “higher accuracy” could be read as model accuracy. Three abstract-only quantitative entries remain withheld. |
| R0071 | p. 6, effect of varying V and timestep | At least 13.8% applies to the weighted sum of task delay and system energy versus MHAPPO, with no implication that it applies separately to both components. |
| R0073 | p. 11, Fig. 6 discussion | The failure sweep cited here uses AlexNet and 15 UAVs. The cases are zero, one and two inoperable UAVs, and the authors report a smaller latency increase for DRL-RLD. The separate across-model clause needs Figs. 4–5. |
| R0074 | pp. 16–17, §4.2 and Fig. 4 | Confirms the distinction between cloud-edge memory failure and successful distributed runs with Orion, Jupiter and EdgeShard at 70B. |
| R0083 | p. 7, Figs. 3–4 discussion | The 88% and 77% maxima concern the 100 m² scenario. Energy maxima apply to distinct battery settings. The candidate outcome omits these distinctions; the separate longevity result requires its own locator. |
| R0089 | p. 9, Fig. 4 discussion | Supports the best accuracy in the limited-bandwidth experiment. The authors describe convergence toward PLUTU as radio resources increase. Other sweeps need separate checks. |
| R0095 | p. 10, Fig. 9(b) discussion | The source reports 100% completion under a 1.5 s limit and says the strategy outperforms baselines by 40–230%. It does not define those percentages as fractional latency reductions relative to baseline. The candidate's “reduces by” interpretation is unsupported. |
| R0121 | pp. 6–8, Tables 3–4 and discussion | The 3.7% traffic change is a modeled single-hop comparison. The (q=3) and (q=4) probabilities on p. 7 need equation-aware visual verification for exact quoting, rather than relying on PDF text order. |

The next P08 pass should adjudicate the discrepancies above, inspect the eight text-order exceptions, and compare each remaining claim and every numeric condition with the source. Withheld rows stay excluded from synthesis. The source inventory is not an extraction acceptance manifest.

## Final decision

Recorded at `2026-11-27T00:33:28+07:00`. **P08 PASS.** Independent verification against hash-checked originals accounted for 455/455 keys from 25 reports, including the remaining 208 at 55023bb. The previous 238 PASS entries and nine dispositions are unchanged. There are 444 retained keys and 11 documented exclusions, with zero pending. Both batches retained 350/350 field groups in total and 58 standalone quantitative rows, each linked to original-page evidence. Reasons for withheld details are in the lock and the ledger. Two newly withheld values have inadequate aggregation or comparator definition.

- [Locked extraction table](p08_extraction_table.json)
- [Quantitative claim-source matrix](p08_quantitative_claim_source_matrix.csv)
- [Lock and exclusions](p08_extraction_lock.json)
- [Batch 01 verification](p08_batch_01_source_review.md)
- [Batch 02 verification](p08_batch_02_source_review.md)

Use only the locked table and matrix downstream. The candidate retains all historical entries, including excluded rows.
