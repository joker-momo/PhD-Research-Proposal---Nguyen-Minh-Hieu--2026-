# TASK

Correct only these 16 failed P09 Batch 01 keys from task 54788143-35ba-47eb-9df9-76b6f3609ef9, context 4d2dc4a5-dec8-48d1-835c-453a0732a0bd, after same-UUID recovery. Do not reissue any other keys.

# REQUIRED WORK

1. Stay in this native parent Task within the authorized canonical folder. No workers: they cannot read original PDFs. Only read the five named originals at `restart_2026_11_26/fulltext_retrieval/pdf/R0001.pdf`, `R0002.pdf`, `R0003.pdf`, `R0006.pdf`, and `R0009.pdf` in the same directory, and P09 in `restart_2026_11_26/protocol_restart.md`. Verify locally accessible body text per report using the exact quote in its first output judgment and name any inaccessible report. Read PDF directly or local PyMuPDF if available, then local MinerU/Marker only when layout requires it and available. Report tool limits.
2. For each target check the original page and section. Re-read the requested passages and reply only for these keys:
- R0001/D01: Replace the p.1 paraphrase with a verbatim body anchor from p.1 §II and use p.2 §II.A or §II.D for the partition objective.
- R0001/D02: Judge what the modeled decision variables and constraints document. Do not claim edge selection is unoperationalized without specific evidence in §II.E. Distinguish unpublished numerical settings (D03).
- R0001/D03: Use PARTIAL where node counts and trace settings are positively reported and reproduction details are missing. NO requires affirmative contrary evidence.
- R0001/D06: Use the Greek alpha symbol as printed, or cite the exact short figure captions. If noting gaps, Figure 2 has shaded bands but their uncertainty meaning is not defined.
- R0002/D03: Match alleged gaps to §VII.A and Fig. 2(b). Do not assert all thresholds or battery-related parameters are omitted. Focus on a clear rerun gap.
- R0002/D07: Use a short within-line verbatim p.7 §VII.A body phrase. Do not imply simulation is a flight; qualify energy/failure and topology according to the stated setup.
- R0002/D08: Use a short verbatim p.9 conclusion/future-work quotation and p.7 evaluation scope. If noting migration-cost tradeoff use the authors’ p.8 qualitative account, with no new numbers or baseline count.
- R0002/D09: Use original exact p.7 third-party-dataset anchor only if useful. It is not a release of author artifacts. Record sections examined in p.7 and p.9.
- R0003/D01: Replace typographic trajectory phrase with a short exact within-line excerpt in §III p.2 or switch-model algorithm p.4.
- R0003/D07: Use shorter exact within-line anchors p.2 §III and p.5 §V.A for trace/coordinator evidence. Distinguish model assumptions from a field test.
- R0006/D07: Describe fixed-altitude and simplified transmission assumptions from pp.2–3 and 6 and qualify transfer to dynamic flight. Any claim of field performance must have full-text evidence.
- R0006/D08: Use p.6 §V.B direct narrative anchor for observed coverage versus concluding language. Avoid exact latency reduction numbers because the comparator statements are internally inconsistent. State the scope conflict precisely.
- R0009/D02: Use exact p.3 model and pp.4–5 Eq. 14 constraint passage. Avoid invented C3-C4 range-and-speed quote.
- R0009/D04: State the four baseline definitions and shared scenario settings in §V.A–B. Do not infer identical training steps or tuning from aligned plot axes.
- R0009/D05: Use exact p.4 Eq. 14 neighborhood citation and pp.8–9 §V.B or a figure caption for metric alignment. Avoid paraphrase inside quote.
- R0009/D07: The simulation uses discrete slots and fixed altitude, with a free-space path-loss model. Avoid describing a validated continuous trajectory or static ground users without original support.
3. Use exact short contiguous original text of 4–12 words inside each quote, with printed signs and literal punctuation. If using a table cell, give row and column and only its actual label. For an inspected absence use a separate null quote record with page and section. Choose physical page numbers, 1-based. Cite quantitative details only when source, printed units, scenario and comparator are all explicit. Prefer concise qualitative rationales.

# REQUIRED OUTPUT

Exactly one JSONL judgment per target or explicit shortfall; 25 words max per rationale. Allowed judgments: YES, PARTIAL, NO, NOT_REPORTED, NOT_APPLICABLE, NOT_YET_ASSESSED. Synthetic schema:
{"report_id":"RTEST","domain":"D03","judgment":"PARTIAL","rationale":"Setup specifies workload, but the rerun seeds are unspecified.","locators":[{"page":4,"section":"Methods, Setup","quote":"the type of workload"},{"page":5,"section":"Methods, Setup","quote":null}]}
End with one summary object with returned_keys, unresolved, tools and workers_used=false, then `P09_B01_TARGETED_CORRECTION_COMPLETE` on its own line. Report identity is frozen in the committed batch manifest and P08 extraction.

# ACCEPTANCE CRITERIA

- 16/16 requested keys or documented reason for any shortfall. Zero duplicates/extras, invalid domain statuses, or reissued PASS keys.
- 100% decided keys carry original PDF/physical-page/section evidence supporting the rationale. Every quoted phrase must be verbatim contiguous. Zero undocumented absence claims or unsupported numerical/bias assertions.
- No workers. Explicitly report unavailable source access/tools and any unresolved key, with reason.

# BOUNDARIES

No files written or uploaded, external discovery or alterations to P08, screened counts, manuscript or eligibility. No claims about experimental artifacts, training equivalence, real deployment or measurement values beyond the paper's source. Leave anything unverifiable explicit.
