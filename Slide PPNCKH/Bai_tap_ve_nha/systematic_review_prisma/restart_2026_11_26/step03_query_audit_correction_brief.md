# TASK
Return a corrected complete version of the eight-query audit from parent Task 468fa8b0-d511-4876-b682-812933a3b82d. Its draft malformed JSON must be replaced.

# REQUIRED WORK
1. Read restart_2026_11_26/protocol_restart.md and restart_2026_11_26/step01_inventory.json in the attached project. Read the eight run files indicated by query_evidence and corpus_expansion/acm_record_capture_2026-11-26.json.
2. Reproduce the eight archived local locators, count, observed time, timestamp basis and filters. Keep exact filter values. Distinguish native export from later ACM capture, and retain WoS null.
3. Correct prior C3: separate ACM Anywhere from the observed count without attributing the difference to one cause. Treat ACM access/facet behavior as local unless documented; use official browser documentation for browser claims. Primary documents include https://ieeexplore-custom.ieee.org/search/advanced/command?reload=true , https://libraries.acm.org/binaries/content/assets/libraries/new_acm-digital-library-user-guide.pdf , and https://service.elsevier.com/app/answers/detail/a_id/11365/supporthub/scopus/~/how-can-i-best-use-the-advanced-search%3F/ .
4. Correct prior C4: preserve the OR alternatives in the OpenAlex tail. Do not intersect a fixed tail with a wildcard tail. If REVISE, supply one exact query with original OR alternatives and explicit term forms, or an exact documented union that preserves that logic. No measured recall or observed-loss claim. Use https://help.openalex.org/api/searching/ and https://help.openalex.org/api/filtering/#intersection-and .
5. Correct prior C1: deliver valid JSON. Escape interior quotation marks in strings. Keep prose in each rationale under 55 words. Inspect the JSON for syntax before returning it.

# REQUIRED OUTPUT
One valid JSON object, no Markdown, containing parent_task_id, runs (8), platforms (4), unresolved, wos_reported_total (null), actions, scholarly_records (empty array), scholarly_records_not_applicable. Run fields: platform, variant, local_locator, count, observed_at, timestamp_basis, query_field, filters, verdict, rationale, proposed_edit. Platform fields: platform, official_url, official_support, limitations. actions has formal_queries_executed, project_edits, records_screened (all zero). Each proposed_edit is either null or a JSON object with exact search parameter, query, filters and any union rule. Use explicit N/A for scholarly records.

# ACCEPTANCE CRITERIA
C1. Valid JSON with exactly eight distinct run pairs and four distinct platform entries, original parent ID.
C2. 8/8 locators, counts, times, bases and filters match inventory and run artifacts. ACM later capture is 79 + 325, separate from native export. WoS null.
C3. Zero unsupported or causal claims. Every platform claim has an official section or local/unresolved label.
C4. Every run has a verdict. A revised query retains original OR alternatives, does not change date/source scope, and claims no measured recall. Missing evidence explicit.
C5. Zero formal searches, project edits, screened records, imported old decisions and scholarly records.

# BOUNDARIES
Read only named project files and public official platform documentation. Do not run a formal query, access credentials or unrelated local files, edit the project, draft a paper, or use another backend.
