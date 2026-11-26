# TASK
Verify only the missing identification metadata for three OpenAlex records in the locked restart dataset.

# REQUIRED WORK
1. Read restart_2026_11_26/search_dataset_manifest.json in the attached HK261 review directory. Use the manifest to locate the formula-independent CSV data. CSV record numbers below are 1-based, excluding the column header, and should be verified against the OpenAlex IDs.
2. Check high_recall W7217862547 (record 26), missing DOI; high_recall W4415181609 (record 33), missing venue; revised complementary W7200232308 (record 31), missing DOI. Use a publisher or institutional repository for identity; official DOI registry is allowed. Record source limitations when access is unavailable.
3. Return the documented title, authors, publication year, venue and DOI for each record; report gaps explicitly. For every fact cite URL or CSV path and record number. Label any source disagreement.

# REQUIRED OUTPUT
Return one physical text line per record. Use space-pipe-space delimiter exactly. Do not use it inside fields.
ROW | OpenAlex ID | title | authors | year | venue | DOI | requested field | VERIFIED or UNRESOLVED | local CSV locator | official verification URL or NONE | short evidence note
Use DOI_NOT_FOUND if unavailable; use other forms of FIELD_NOT_FOUND for unknown metadata. Add no records beyond the specified IDs. Plain text, no Markdown.

# ACCEPTANCE CRITERIA
N1. Exactly 3 distinct expected IDs or an explicit row per shortfall. Duplicate IDs or normalized same DOI/title identities equal zero.
N2. Every row has title, authors, year, venue and DOI or the explicit missing marker. CSV locator is exact on all 3.
N3. All nonlocal verified facts have a publisher, institutional repository or DOI registry URL that resolves to matching evidence. Zero unsupported quantitative claims. Unresolved fields have a reason and keep the missing marker.
N4. Zero decisions, source data edits, legacy corpus lookups, or new search-record imports.

# BOUNDARIES
Read only the manifest and CSVs it identifies for these three rows. Use public official sources for targeted verification. No editing local files, eligibility/screening decisions, trend inference, new candidate discovery, login, secrets or manuscript prose. Do not look for abstracts or owners' contact information. Missing evidence must stay unresolved.
