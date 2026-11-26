# TASK
Correct five criteria in HK261 Batch 03 without repeating the primary task (Gemini.app task 9db9c066-41fa-40b3-8bc3-468274e9711d, context e5ac8613-f91a-4452-92dd-72bd85c2a6e9).

# REQUIRED WORK
1. Re-read P03/P06 in restart_2026_11_26/protocol_restart.md and use the project fulltext_retrieval index/PDFs directly. Correct R0083 E4: on physical p.7, Section 4.2, the PDF extraction matches the exact sentence fragment "our method was able to obtain the lowest e2e latency". Label it as report-level evaluation evidence without reporting a performance advantage in notes.
2. R0108 E1: physical p.2 contains the exact fragment "this paper proposes a Secure and Intelligent Edge Computing Architecture". R0108 E6: cite exact English wording on p.2, excluding any column overlaps (same continuous fragment is acceptable).
3. R0108 E4: inspect pp.4–7 Sections III–IV. System-level metrics evaluating the generic framework do not establish evaluation of an inference method under E4. Check for a defined evaluated inference method and its reported outcomes. If the relevant sections show architecture-level training/offloading metrics only, mark E4 F with p.6 or p.7 exact anchor; retain E3 as primary if no earlier criterion fails. Do not infer E7 from E4 alone.
4. R0081 E5: the Crossref publisher deposit at https://api.crossref.org/works/10.1145/3498361.3538674 gives published date 2022-06-27 (field message.published.date-parts; use exact short literal from the JSON or an ACM publisher field). The conference event range is not the publication date. Leave E7 unresolved because the official demo procedure does not establish full report peer-review status. No other records or fields are requested.

# REQUIRED OUTPUT
Exactly 3 compact JSONL rows with id, decision, primary, reason, e. Exact fields: R0081 E5, R0083 E4, R0108 E1/E4/E6. Criterion schema [T/F/U, 1-based physical PDF page or 0 for verified external, short heading, exact contiguous source words or JSON field fragment, note, PDF or exact HTTPS URL]. Use empty primary code except EXCLUDE. In your reasons, preserve full E1–E7 disposition using the prior task (R0081 AWAITING_CLASSIFICATION E7, R0083 INCLUDE, R0108 EXCLUDE E3 unless supported evidence establishes earlier failure).

# ACCEPTANCE CRITERIA
3/3 exact IDs, 5/5 exact patch fields, 0 duplicates, 0 extra IDs/criteria. Every locator must resolve and the quote match; unsupported quantitative claims zero. Every unresolved item explicit; R0108 E4 explanation must address inference evaluation, not generic framework simulation. A4 requires Codex independent verification.

# BOUNDARIES
Use only those 3 locked reports, approved protocol and publisher metadata for the exact DOI; no research outside this correction, no edits, no manuscript, no tactics, and no invented values, quotes or decisions. An inaccessible or uncertain source must be identified as such. The locked index supplies scholarly metadata.
