# TASK
Screen exactly R0166–R0240 (75 records) at title/abstract stage. This corrects prior Task c4e62a8f-c350-4b05-bdbf-1cba0725d5ec, whose large CSV read was truncated.

# REQUIRED WORK
1. In the attached HK261 project, read P03/P06 of restart_2026_11_26/protocol_restart.md and read restart_2026_11_26/screening_evidence/R0166-R0240.jsonl as JSONL. That small file contains all 75 records and any duplicate members. Do not open the large CSV files.
2. For each screening_id decide R for plausible in-scope inference and retrieve, U if unclear and advance, or X only if the title, abstract or snippet affirmatively establishes an E1–E7 failure. A missing abstract, ambiguous topic, date ambiguity, repository name or database type label is not enough for exclusion. A title explicitly identifying a survey, editorial, or entire proceedings volume can support exclusion. The selector or optimizer is not by itself the inference workload.
3. Use one E1–E7 code even for R (for instance R with E3 for express DNN partitioning in a swarm). Copy a contiguous 3–15 word span verbatim from the cited field. For a U based on missing details, cite the title and name the uncertainty. If several evidence fields disagree, keep U.

# REQUIRED OUTPUT
One plain-text line per ID, in ascending order. Exactly seven fields with the delimiter space-pipe-space:
screening_id | R/U/X | E1–E7 | REP or member record_id | T/A/S | verbatim span | reason of 1–13 words
T=title, A=abstract, S=abstract_snippet. REP means the representative object. Bibliographic fields will be joined by ID from the locked queue. No markdown or headings.

# ACCEPTANCE CRITERIA
S1 All 75 unique requested IDs and zero duplicates; any unavailable ID must be reported as a shortfall.
S2 Every decision and E-code permitted; exact ID join to locked title/authors/year/venue/DOI or missing marker.
S3 75/75 correct locators and quote spans; every exclusion has direct affirmative scope evidence; unsupported claims=0.
S4 Zero external searching, file changes, legacy labels, or out-of-scope records. All unresolved records explicitly U.

# BOUNDARIES
Only read the small named evidence file and the two protocol sections. No browsing, downloads, project writes, legacy screening results, secrets, or manuscript prose.
