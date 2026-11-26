# TASK
Screen exactly R0091–R0165 (75 records) using HK261 restart protocol restart-1.1 at title/abstract stage.

# REQUIRED WORK
1. Read P03 and P06 of restart_2026_11_26/protocol_restart.md. Read restart_2026_11_26/unique_record_queue.csv as CSV. Select exactly R0091 through R0165 in order. Use all 75 rows, with unique IDs.
2. For each use R (RETRIEVE_FULL_TEXT), U (UNCLEAR, advances to full text for clarification), or X (EXCLUDE). Exclude only for an affirmative incompatibility with the protocol. Missing metadata, title-only evidence that does not establish scope, and ambiguous inference or dates are U, not X. AI used to optimize routing/allocations is not itself the inference workload. Plausible distributed inference should advance.
3. Cite an exact continuous span from the representative's title (T), abstract (A), or snippet (S). If a duplicate member has better evidence, use dedup_map.csv and records_normalized.csv from the same directory and explicitly cite its record_id.
4. Use one E1–E7 code on every row, even when recommending retrieval. For example, if an abstract expressly proposes DNN partitioning in a swarm, use R with E3. If it only mentions a swarm and the inference task is uncertain, use U with E3. NONE is invalid.

# REQUIRED OUTPUT
Plain text, one line per ID, exact delimiter space-pipe-space:
screening_id | R/U/X | E1–E7 | REP or member record_id | T/A/S | exact span of 3–15 words | reason of 1–13 words
No Markdown, wrapping, commentary, summaries, or unrequested rows. Copy the source span verbatim without adding punctuation. ID is the only bibliography join key; Codex attaches title, authors, year, venue, DOI and missing markers from the locked representative.

# ACCEPTANCE CRITERIA
S1 Exactly the 75 expected IDs and zero repeats. Report any read shortfall explicitly with affected IDs; a shortfall fails acceptance.
S2 Decision and criterion permitted on 75/75 rows; each ID resolves unambiguously to its full locked metadata.
S3 75/75 source-member/field locators and exact quotes valid. All X decisions must have affirmative evidence for a specific exclusion reason; no unsupported claims or status from missing data.
S4 Zero manuscript writing, source edits, legacy labels, or outside records. Unresolved evidence marked U with concise reason.

# BOUNDARIES
Read only the four named project files and the batch IDs. Do not browse, search, download papers, edit files, read historical results, or invent facts.
