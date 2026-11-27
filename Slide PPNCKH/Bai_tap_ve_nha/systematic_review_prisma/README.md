# HK261 PRISMA Systematic Review

This directory contains the HK261 systematic review protocol, screening records, synthesis and manuscripts. The dissertation roadmap is maintained separately.

## Current manuscripts

- **IEEE journal draft** · [PDF](manuscript/ieee_journal/main.pdf), [LaTeX source](manuscript/ieee_journal/main.tex), [S4 evidence index](manuscript/ieee_journal/supplement_s4.md) and [companion archive S1–S4](manuscript/ieee_journal/HK261_IEEE_S1-S4.zip).
- **Springer Nature comparison draft** · [PDF](manuscript/sn_computer_science/main.pdf), [LaTeX source](manuscript/sn_computer_science/main.tex) and [evidence index](manuscript/sn_computer_science/supplement_evidence_index.md).
- **Earlier RQ5 manuscript** · [preserved checkpoint](restart_2026_11_26/extraction/rq5_uniform/main_5910b6b_snapshot/README.md).

The [PRISMA restart ledger](restart_2026_11_26/prisma/prisma_counts.json) records **46 included, 90 excluded and zero awaiting classification**. The [author-reviewed S2 record](manuscript/sn_computer_science/supplement_s2_adjudication.md) gives the eligibility and adjudication basis. See [canonical project state](MUST_READ_AI_AGENT/current_state.json) for the current checkpoint and next task.

The IEEE manuscript still awaits confirmation of authorship, contributions, funding and competing interests. Submission is pending.

## Directory map

- `protocol.md`: review question, eligibility criteria, and planned methods.
- `protocol_amendment_001.md`: dated scope amendment and its effect on prior work.
- `protocol_amendment_002.md`: dated publication-window amendment requiring work from 2021 onward.
- `corpus_year_audit_2026-11-24.csv`: year-by-year audit of the 20 priority reports.
- `prior_review_gap_matrix.md`: accepted six-review comparison, direct evidence, and the bounded positioning statement used in the Introduction.
- `coursework_checklist.md`: official HK261 requirements mapped to current evidence and actions.
- `project_plan.md`: sixteen-stage workflow, objective completion rules, and current status.
- `search_strategy.md`: platform-specific queries and search history.
- `final_query_translations.md`: final platform-specific searches after scope amendment.
- `seed_query_coverage_matrix.csv`: expected sensitivity of the eight final queries to the twenty verified seed DOIs; not executed search results.
- `formal_search_log_v0.2.csv`: formal runs, failures, and pending core exports.
- `search_log.csv`: auditable query dates and retrieved counts.
- `screening_log.csv`: record-level eligibility decisions.
- `study_report_map.csv`: links multiple reports to the same underlying study.
- `data_extraction.csv`: structured evidence extraction.
- `data_extraction_first5.md`: verified interim extraction from the first five retrieved full texts.
- `quality_appraisal.csv`: design-appropriate quality judgments.
- `quality_appraisal_first5.csv`: interim appraisal of the same five reports.
- `prisma_counts.csv`: reconciled PRISMA 2020 counts.
- `prisma_2020_checklist_working.md`: item-by-item PRISMA status and completion gate.
- `doi_download_checklist.md`: historical original-priority download checklist; superseded intake status is documented by `interim_20report/README.md`. New candidate DOI links are under `corpus_expansion/`.
- `venue_selection.md`: historical venue comparison and the superseded IEEE Access decision.
- `venue_change_sn_computer_science_2026-11-25.md`: user-directed venue change, official SN Computer Science requirements, and conversion actions.
- `corpus_expansion_30_35_plan_2026-11-25.md`: task split, quantified A2A acceptance gates, and workflow for expanding to 30–35 eligible studies.
- `corpus_expansion/doctoral_foundation_reading_note.md`: doctoral research anchors, reading priorities and conditions for reusing baseline methods.
- `corpus_expansion/phd_alignment_46.csv`: accepted46-record reading map; eligibility remains separate.
- `corpus_expansion/doi_fulltext_priority_queue.md`:20 candidate DOI links ranked for missing full-text acquisition, with unresolved publication dates flagged.
- `venue_research_gemini_accepted.json`: accepted, reviewed A2A research evidence for the venue decision.
- `template/`: official IEEE and Springer Nature archives, extracted sources, provenance and checksums.
- `reporting_guidelines/`: official PRISMA 2020 checklist and flow-diagram templates.
- `sources/raw/`: unmodified provider exports.
- `sources/normalized/`: normalized and deduplicated records.
- `manuscript/sn_computer_science/`: Springer comparison source and PDF. `manuscript/ieee_access/` is historical.
- `interim_27report/`: historical 27-report eligibility log, 24-study extraction, appraisal and audits. Older interim directories,including interim_26report,and root-level tables are historical snapshots.
- `output/`: dated delivery PDF and clean LaTeX source package generated from the audited manuscript.
- `submission_readiness_2026-11-25.md`: exact completed checks and unresolved submission blockers.
- `submission_evidence/`: journal-generated submitted manuscript, manuscript ID, acknowledgement, and forwarded-email evidence.
- `submission_evidence/checklist.md`: exact files and cross-file consistency checks required after submission.
