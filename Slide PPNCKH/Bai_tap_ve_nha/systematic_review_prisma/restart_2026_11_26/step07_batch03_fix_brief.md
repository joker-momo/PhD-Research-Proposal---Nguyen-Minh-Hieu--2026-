# TASK
Correct four insufficiently supported exclusions from Gemini.app Task 71612eda-f7ae-407d-b2cd-c42cf080d164, screening batch 03.

# REQUIRED WORK
1. Read P03/P06 in restart_2026_11_26/protocol_restart.md and only R0115, R0116, R0126, R0160 in restart_2026_11_26/unique_record_queue.csv. Use dedup_map.csv and records_normalized.csv in that directory only for exact member evidence.
2. Reassess type exclusions. Publisher/repository URL or native type labels alone cannot establish record type if equivocal. Under the locked local evidence, R0115, R0116 and R0126 lack independent evidence in title/abstract/snippet for the asserted subtype. If no affirmative evidence is available, mark U and identify the unknown. R0160 likewise needs affirmative scope/type evidence from available text, otherwise U.
3. Use exactly one valid E-code, short exact source span, and matching locator. A title span for U is acceptable when its reason identifies missing evidence.

# REQUIRED OUTPUT
Four plain-text lines with exact delimiter space-pipe-space:
screening_id | R/U/X | E1–E7 | REP or member record_id | T/A/S | exact span of 3–15 words | reason of 1–13 words

# ACCEPTANCE CRITERIA
All four exact IDs once; all four decisions and E-codes valid; 4/4 quote and locator matches. Zero exclusion by unsupported label alone; 0 invented evidence. Explicit uncertainty where not resolved. Codex joins bibliographic fields by ID.

# BOUNDARIES
No public search, no edits, no historic labels, no full text, no additional records, no other files or secrets.
