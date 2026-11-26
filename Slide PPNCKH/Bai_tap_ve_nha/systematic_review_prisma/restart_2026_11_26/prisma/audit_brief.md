# TASK

Independently cross-check the restart's PRISMA record/report/study transitions using the named ledgers in the attached project.

# REQUIRED WORK

1. Read `restart_2026_11_26/` only. Count categories from the original ledgers in actions 2–4. Work in one parent Task and do not use workers. Use local deterministic table analysis if available and state the tool actually used.
2. Use `search_dataset_manifest.json`, `records_normalized.csv`, `dedup_map.csv`, and `title_abstract_screening.csv` to reconcile identification, duplicates, and screened records. Distinguish raw record IDs from screening IDs. Preserve the four source counts and the recorded WoS status.
3. Use `title_abstract_screening.csv`, `fulltext_retrieval/retrieval_log.csv`, `fulltext_retrieval/missing_pdf.csv`, and `fulltext_screening/fulltext_screening.csv` to cross-tabulate the two forwarded abstract decisions against retrieval status. Separate assessed reports, not-retrieved reports, exclusions and awaiting classification. Cross-check every pending report ID and the primary exclusion-reason counts in `fulltext_screening/exclusions.csv`.
4. Use `study_linkage/report_study_map.csv` and `study_linkage/pair_evidence.csv` to distinguish included reports and study IDs, and record the number of candidate pairs tested and merged. Confirm P08 and P09 gate labels from their lock JSON files.

# REQUIRED OUTPUT

Compact JSONL, one row per key IDENTIFICATION, TITLE_ABSTRACT, RETRIEVAL, FULL_TEXT, STUDIES. Format example (format placeholder only): {"key":"IDENTIFICATION","values":{"raw":0,"duplicates":0,"sources":{"IEEE":0,"SCOPUS":0,"ACM":0,"OPENALEX":0},"wos_count":null,"wos_status":"not_searched_access_unavailable"},"locators":["restart_2026_11_26/search_dataset_manifest.json#rows_by_source"],"unresolved":[]}. TITLE_ABSTRACT values: screened, excluded, forwarded_full_text, forwarded_unclear. RETRIEVAL: sought, assessed, not_retrieved, retrieved_from_full_text, missing_from_full_text, retrieved_from_unclear, missing_from_unclear. FULL_TEXT: included, excluded, pending_ids (array), primary_exclusion_reasons (map of E codes). STUDIES: reports, studies, candidate_pairs, merged_pairs, p08_gate, p09_gate. End with a summary row containing tools, workers_used (false), missing_keys, and unresolved items with reasons, then `HK261_RESTART_13_AUDIT_COMPLETE`.

# ACCEPTANCE CRITERIA

Exactly five distinct keys, zero duplicates, all listed values present or explicit shortfalls. Every reported count has a relative file/field locator. All four arithmetic differences equal zero, source list exactly IEEE, SCOPUS, ACM, OPENALEX, WoS null, and pending ID set and exclusion reason totals match the accepted ledgers. No unsupported numbers or implicit inclusion of pending reports. Inaccessible files and unverified counts are listed explicitly.

# BOUNDARIES

Read only the named project ledgers and lock files. No PDFs are required for this accounting-only check. No changes to files, exclusions, study groups, or protocol. No old 46-report evidence, new discovery sources, draft prose, submission, or upload.
