# TASK

Repair exactly five locator entries from the independent step 13 ledger audit under original Gemini Task 38e73b37-23c9-415a-8b38-51c7e42b4563, context b82d6127-64a2-4cf4-a988-bb3c1636ece4.

# REQUIRED WORK

1. In a single parent Task, read the actual first CSV header line for each of these five files in the attached HK261 project: `restart_2026_11_26/fulltext_retrieval/retrieval_log.csv`, `restart_2026_11_26/fulltext_retrieval/missing_pdf.csv`, `restart_2026_11_26/fulltext_screening/fulltext_screening.csv`, `restart_2026_11_26/fulltext_screening/exclusions.csv` and `restart_2026_11_26/study_linkage/report_study_map.csv`.
2. Replace only the locator for each of these five files, keeping the actual ID field and the decision, status or reason fields present and relevant in that file. If a cited input does not provide eligibility, family or abstract-stage status, do not attribute it to that file. Refer to the already-accepted companion locator when necessary.

# REQUIRED OUTPUT

Exactly five JSONL rows in this shape: {"file":"restart_2026_11_26/fulltext_retrieval/retrieval_log.csv","fields":["actual_id_column","actual_status_column"],"role":"what these fields anchor","unresolved":null}. If inaccessible, use fields=[] and a concrete unresolved reason. Finish with `HK261_RESTART_13_LOCATOR_CORRECTION_COMPLETE` alone.

# ACCEPTANCE CRITERIA

Five distinct expected files, zero additional rows, zero field names absent from the named CSV's header, and each row includes the actual record/report ID column plus relevant fields. Declare all shortfalls. No numeric claims to validate. Scholarly bibliographic identities are unchanged.

# BOUNDARIES

Use the attached direct project read-only. Keep all 26 accepted value fields unchanged and do not repeat them. Do not inspect other files, send to workers, edit the study decision set, quote PDFs, or perform searches.
