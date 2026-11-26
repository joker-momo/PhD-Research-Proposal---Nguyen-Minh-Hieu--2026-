# TASK
Find lawful full-text access evidence for the exact 20 HK261 records in batch 02.

# REQUIRED WORK
1. Read restart_2026_11_26/fulltext_retrieval/inputs/batch_02.jsonl directly from the attached project and P06 of restart_2026_11_26/protocol_restart.md.
2. Verify bibliographic identity against the DOI landing page, authoritative publisher or Crossref for each record. If DOI_NOT_FOUND, search the exact title and report only a verified DOI or DOI_NOT_FOUND. Flag conflicts instead of substituting a similar title.
3. Check publisher full text first. If unavailable, look for a lawful public copy by exact DOI/title through an index such as OpenAlex/Unpaywall and an institutional repository or arXiv. Check both routes for each of the 20 target records when accessible to you. A file candidate may be a publisher version or accepted manuscript. Label preprints as such and give an explicit linkage locator. A publisher abstract is not readable full text.
4. Give at most two actual public full-text candidate URLs per item, with the version and evidence locator if seen. For every attempted route, distinguish observed availability from search/tool limitations. If no PDF was located, record why and a lawful access route to try.

# REQUIRED OUTPUT
Return 20 plain JSON lines, one object per ID, no Markdown. Keys: id, doi, identity_url, publisher_url, publisher_observation, oa_lookup_url, oa_observation, candidates (array of objects with url, version, format PDF or HTML, evidence_url), reason_if_no_pdf, unresolved (string or empty string). Keep observation strings concise, ideally one sentence each. Use empty strings for unavailable optional URL fields. Use exact IDs and only literal URLs actually identified. The locked local file provides title/authors/year/venue, and Codex will join by ID. A candidate URL remains a lead until Codex opens the file and verifies identity.

# ACCEPTANCE CRITERIA
T1. 20/20 exact IDs, no duplicates, or explicit shortfall. No out-of-batch entries.
T2. Each object supplies DOI or DOI_NOT_FOUND, source URL or explicit access shortfall, and an exact-title/DOI identity check or conflict. Zero invented identifiers.
T3. Every candidate has format, version and evidence_url or an explicit uncertainty. No access claim is inferred from an abstract or search result alone.
T4. Every record without a PDF candidate reports why, and unverifiable routes remain explicitly unresolved. Unsupported numerical claims and file mutations equal zero.

# BOUNDARIES
Read only the named project input and protocol section. Public lawful web research only. No local project edits, downloads into the project by Gemini, paywall bypass, credentials, unrelated records, eligibility decisions, or manuscript prose. If limited by your search tool, say which route you could not check. Never fabricate a URL or state you opened a source you could not inspect.
