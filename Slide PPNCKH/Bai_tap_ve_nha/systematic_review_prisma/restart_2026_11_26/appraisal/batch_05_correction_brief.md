# TASK

Correct nine exact Batch 05 appraisal keys plus one R0083 original-PDF access proof, linked to native Gemini.app Task c960ad8f-d8c5-4e8e-8b2e-e3569a96d42f and context 0bc99028-dbaf-4e1b-bf77-b7c793b98952.

# REQUIRED WORK

1. Read only R0074, R0083, R0089, R0095 and R0121 original PDFs under `restart_2026_11_26/fulltext_retrieval/pdf/` in the attached canonical HK261 project directory. P08 and P09 in `restart_2026_11_26/` give identity and domain definitions. Work in the single Gemini.app parent Task, no delegation to workers. Use PyMuPDF if available. Use local MinerU then Marker only where extraction or layout requires it; state which tools are available and actually used. Do not upload PDFs.
2. Return one R0083 PDF access record from physical page 3, with project-relative PDF path and a short exact contiguous body quotation composed of ordinary words. Avoid mathematical symbols or lines crossing columns. The prior probe replaced the printed variable before UAVs with an ordinary letter.
3. Re-read only the relevant original body pages and replace these nine keys:
   - `R0074/D06`: distinguish the separate Monte Carlo experiments, p20 §4.7 and p21 §4.8, from the main comparisons in p16 §4.2. If describing repeat count, cite the corresponding short sentence in each experiment; prefer qualitative language. State expressly when replication/dispersion does not carry over.
   - `R0074/D08`: scope the Introduction p3 70B uniqueness statement, including its memory-constrained context, against §4.2 pp16–17 and p23 §5.5. Cite shared comparison settings and successful comparator evidence, without duplicate performance values or implied hardware trial.
   - `R0083/D04`: repair the p8 §4.2 locator using a short contiguous clause on one printed line and without changing typographic punctuation. Distinguish the behavior under tested memory settings from an imposed disparity.
   - `R0089/D03`: keep the disclosed simulated setup separate from material unspecified rerun details. Check §5 p8 and §5.1 p9 together before discussing bandwidth or radio resources. Do not give a blanket lack-of-bandwidth claim, and cite the actual checked section for each gap.
   - `R0095/D05`: use §5.3 p9, §5.4.2 p10/Fig. 9 and §5.1 p8 if needed. Distinguish measured decision overhead from inference-latency components. Use qualitative rationale and avoid deadline or completion percentages.
   - `R0121/D02`: replace the p6 quotation with a contiguous body clause without apostrophes or formulas. Describe the explicit model assumptions using pp5–6 and §7 pp8–9. Distinguish simplified collision/delivery assumptions from observed collision-free operations.
   - `R0121/D03`: calibrate the reproducibility judgment to the analytical equations and parameter tables. Distinguish core reconstructable estimates from ambiguity between the p7 paragraph discussing Fig. 3 and the p9 conclusion on quorum comparison conditions. The ambiguity does not establish that the model itself cannot be reconstructed. Do not give operational quantitative values.
   - `R0121/D05`: evaluate whether outcomes match the article's actual analytical objectives, cite §3 p3 and §§5–6 pp5–8. If stating an additional missing outcome, distinguish that outcome from the stated objective; do not treat deferred accuracy evaluation as measured.
   - `R0121/D07`: preserve scope as analytical, single-hop numerical calculations and model assumptions. Cite §7 pp8–9. Differentiate averaged medium access and omission of high-density collisions from observed collision-free behavior or tested mobility.
4. Return one replacement per listed key, and check that each complete rationale maps to exact physical page and section. Each locator must support its associated statement. Leave 41 other domain keys and four other access proofs untouched.

# REQUIRED OUTPUT

Return compact JSONL. First one access row, format: {"access":"READ","report_id":"R0083","pdf_path":"restart_2026_11_26/fulltext_retrieval/pdf/R0083.pdf","page":3,"section":"Section number and name","quote":"an exact contiguous body phrase","reason":null}. If inaccessible, return NOT_ACCESSIBLE, the intended path, null page/section/quote and the actual reason. Then one object per domain in this exact shape:
{"report_id":"RTEST","domain":"D03","judgment":"PARTIAL","rationale":"Settings are listed, but initialization details are unavailable in the inspected Setup.","locators":[{"page":4,"section":"Simulation Setup","quote":"the same simulator was used for all runs"},{"page":5,"section":"Simulation Setup, inspected initialization description","quote":null}]}
Use YES / PARTIAL / NO / NOT_REPORTED / NOT_APPLICABLE / NOT_YET_ASSESSED. NO requires directly observed inadequate reporting/evidence or contrary evidence. For inspected absence use null quote with a concrete page/section. End with one summary object with returned_keys (array), unresolved (array with key and reason), tools, workers_used (false). End with `P09_B05_CORRECTION_COMPLETE` alone on a line.

# ACCEPTANCE CRITERIA

Exactly 1 repaired access record and 9 unique requested domain keys. Zero duplicates, extra keys, schema errors or fabricated citations. 100% provided body quotes must match a physical source page. All accepted rationales are supported in scope, including relevant conditions and study designs. Zero unsupported numerical claims. Declare all shortfalls. Use no abstract evidence.

# BOUNDARIES

Read-only access to named canonical project inputs. No external upload, edits, other reports, workers, draft prose, new searches, exclusions or synthesized performance claims. Preserve P08 corpus and earlier decisions. Retain documented evidence limits alongside supported judgments.

Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
