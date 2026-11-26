# 46-report coursework release

Updated at: 2026-11-26T11:02:55+07:00

The current manuscript accounts for 46 screened reports: 36 working included, two excluded and eight awaiting classification. This is an interim systematic-review draft with explicit search and adjudication limitations, not a submission-ready package. No submission or email was performed.

- `report_accounting.csv`: all 46 IDs, current working decisions, DOI, reason and accepted source. Identity/date and scope overlays supersede the base ledger; no family merge is assumed.
- `data_extraction_eligible.csv`: 36 rows; 24 historical detailed extractions retained plus 12 minimum source-located extractions from previously accepted Gemini screening. The historical `study_id` column is a report ID. `NOT_EXTRACTED` means the field was not reported in the accepted extraction, not that it is absent from the original paper.
- `delta_extraction_evidence.json`: 12 accepted source records and 24/24 page/quote checks against canonical full text; no new performance effect adopted.
- `quality_appraisal_status.csv`: all 36 IDs; 216 judgments retained for 24 reports and nine domains, domain 9 withheld, and 12 additional reports explicitly NOT_ASSESSED.
- `prisma_counts.json`: report-level arithmetic, extraction depth and unknown unique-study/identification counts.
- `../prisma_2020_checklist_working.md`: 27-item reporting map.
- `../manuscript/sn_computer_science/main.tex` and `main.pdf`: active Springer Nature source and compiled review copy.

The 27-report historical release remains unchanged. The source evidence is not upgraded by the delivery deadline; unknowns remain unknown.

Build logs are retained with trailing whitespace normalized for Git; warning/error text is unchanged. CSV line endings are LF.
