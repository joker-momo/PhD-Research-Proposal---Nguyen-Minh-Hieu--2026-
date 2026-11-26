# TASK
Correct criterion codes and sharpen evidence for 12 records from parent Gemini.app Task c22d8c48-f9ff-48a1-9489-47135b78d4e6.

# REQUIRED WORK
1. Read P03/P06 of restart_2026_11_26/protocol_restart.md and exactly these 12 IDs in restart_2026_11_26/unique_record_queue.csv: R0001 R0002 R0003 R0006 R0009 R0010 R0014 R0015 R0019 R0022 R0028 R0029. Member locators come from restart_2026_11_26/dedup_map.csv and restart_2026_11_26/records_normalized.csv when needed.
2. The parent returned NONE as the criterion for all twelve RETRIEVE_FULL_TEXT rows. Replace NONE with one E1–E7 code that drove the decision. For RETRIEVE_FULL_TEXT, the code describes the positive evidence to investigate, not an exclusion.
3. For R0002 cite the paper’s proposed migration mechanism, not its motivation sentence. For R0028 reassess E3: distinguish collaborative inference placement/orchestration from UAV data acquisition plus edge annotation for training. Use UNCLEAR if the abstract does not establish which is evaluated. Preserve prior decisions elsewhere unless a direct source contradiction requires correction.
4. Preserve exact evidence locators and use a contiguous source span of 3–18 words. Do not ask for other tasks.

# REQUIRED OUTPUT
Exactly 12 physical lines as plain text. Use exact delimiter space-pipe-space:
FIX | screening_id | RETRIEVE_FULL_TEXT or UNCLEAR or EXCLUDE | primary_E_code | evidence_record_id | evidence_field | exact_evidence_span | reason
The reason is 1–18 words. Keep other bibliographic fields from parent unchanged; do not repeat them. Evidence field is title, abstract, or abstract_snippet.

# ACCEPTANCE CRITERIA
F1 Exactly 12 distinct specified IDs; an explicit missing ID is a shortfall, not a pass; duplicate=0.
F2 12/12 valid decision and criterion values. NONE is invalid.
F3 12/12 exact evidence spans, correct member/field, length 3–18 words. R0002 cites the proposed mechanism. R0028 clearly states the uncertainty or direct E3 evidence. Unsupported factual or quantitative claims=0.
F4 No source edits, new records, full-text decisions, legacy labels, or final prose.

# BOUNDARIES
Only read the named files and exact records; do not browse, read secrets, modify files, find full texts, or guess missing evidence.
