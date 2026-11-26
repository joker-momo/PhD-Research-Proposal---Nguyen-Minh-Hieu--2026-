# TASK
Screen the first 30 unique records, R0001–R0030, by title and abstract for HK261 restart protocol restart-1.1.

# REQUIRED WORK
1. Read P03 and P06 in restart_2026_11_26/protocol_restart.md. Read exactly IDs R0001 through R0030 inclusive in restart_2026_11_26/unique_record_queue.csv. Parse as CSV so quotation marks and commas inside abstracts stay intact.
2. If the representative lacks decisive information, optionally consult its exact member records via restart_2026_11_26/dedup_map.csv and restart_2026_11_26/records_normalized.csv. Read the corresponding locked raw rows only if needed.
3. Return one record per requested screening ID. Use RETRIEVE_FULL_TEXT for plausible in-scope candidates, UNCLEAR for unresolved information, and EXCLUDE only when affirmative title/abstract evidence clearly shows a protocol failure. UNCLEAR advances for clarification. Use a single primary E1–E7 criterion and quote a short exact evidence span. For missing-information only, cite the available title as locator and describe what is unknown. Do not infer evaluated multi-UAV, collaborative inference or eligibility from a passing mention of terms. Do not exclude solely on missing metadata, a database label, or uncertainty about a cutoff-year date.
4. Use title/authors/year/venue/DOI exactly from the representative, preserving case and order. If absent use AUTHOR_NOT_FOUND, YEAR_NOT_FOUND, VENUE_NOT_FOUND, DOI_NOT_FOUND, as applicable. Cite the metadata locator via screening ID and give a separate field locator for the evidence span.

# REQUIRED OUTPUT
Return plain text only with one physical line per requested record. The delimiter is exactly space-pipe-space. Field order:
ROW | screening_id | title | authors | year | venue | doi | decision | primary_E_code | evidence_record_id | evidence_field | exact_evidence_span | reason
evidence_record_id must be the original record_id of a queue member for this ID. evidence_field must be title, abstract, or abstract_snippet. Copy one contiguous span of 3–18 words verbatim, without adding quote marks or ellipses unless they are already part of the span. The reason is at most 18 words. No Markdown, commentary, counts, or unrequested candidate records.

# ACCEPTANCE CRITERIA
S1 Exactly 30 expected unique IDs and 30 intact physical ROW lines. Any read shortfall must identify each absent ID explicitly; a shortfall does not pass the screening gate. No duplicate IDs, normalized titles or non-missing DOI keys.
S2 Exact title, authors, year, venue and DOI from the representative or a permitted missing marker, 30/30.
S3 All decisions and E-codes valid; evidence record belongs to the same screening ID and every quote matches its field and 3–18 word bound.
S4 All excludes have affirmative evidence of the named protocol criterion failing; unsupported quantitative or eligibility claims = 0; unresolved information explicit.
S5 No records outside the batch, no historic 46 labels, no file edits, no full-text decisions.

# BOUNDARIES
Only read the named project files and cited locked raw rows for these 30 IDs. Do not read previous 46 screening decisions, use a search engine, download full text, write prose for the paper, edit project files, read secrets, or infer missing information.
