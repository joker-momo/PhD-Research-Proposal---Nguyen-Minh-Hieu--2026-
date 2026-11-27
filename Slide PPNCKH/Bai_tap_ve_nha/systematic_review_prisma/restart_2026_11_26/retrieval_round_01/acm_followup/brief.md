# TASK

Find lawful full-text PDF sources and verify document identity for exactly these three public DOI records.

- R0096 · 10.1145/3714394.3756181
- R0221 · 10.1145/3820709.3820744
- R0402 · 10.1145/3842435.3843964

# REQUIRED WORK

1. Open Crossref or publisher metadata for each DOI. Record title, authors, publication year, venue, and DOI.
2. Check legitimate open-access indexes, institutional repositories, and author-posted copies for each DOI. Prior observation supplied by Codex: the three direct ACM PDF links returned HTTP 403/Cloudflare; attribute this observation to Codex unless reproduced. Do not attempt to clear the challenge.
3. Open each authorized PDF candidate if possible. Check that the file is a complete article, count its physical pages, and match its first-page title or DOI. Record the exact visible evidence. Determine version from a specific source field or document label. Use UNVERIFIED for ambiguous versions. Do not summarize the articles or examine operational details.
4. For each unavailable or mismatched PDF, record actual attempted URLs, outcomes, and exact access errors when displayed. Keep untested leads separate. Return durable lawful PDF URLs for Codex to download and independently verify.
5. Report whether workers were used. If used, give an exclusive allocation of all three IDs with no overlap and reconcile the output in this parent task. If unavailable or unconfirmed, handle the entire task in the parent.

# REQUIRED OUTPUT

Return three JSONL objects, one per ID in the order listed. Exact fields: record_id, doi, title, authors, year, venue, status, source_url, source_class, version, physical_page_count, first_page_check, attempts, unverified_leads, evidence, unresolved_reason. Allowed statuses are OPEN_PDF, CANDIDATE_UNVERIFIED, NOT_ACCESSIBLE, OA_NOT_FOUND. Allowed versions are PUBLISHER_VERSION, ACCEPTED_MANUSCRIPT, PREPRINT, UNVERIFIED. Use null for unavailable scalar fields. The first_page_check object has physical_pdf_page (1 or null), field (title, DOI, or null), expected, observed and match (true, false, or null). Each attempt has url, source_class, outcome and exact_error. Each evidence item has record_id, claim_or_decision, source, locator, and excerpt_or_exact_field_value. Use physical PDF pages numbered from 1. Restrict page excerpts to titles, DOI, or a short version label. Finish with one JSON line containing workers_used, worker_assignments, returned_ids, unresolved_ids and complete.

Example row shape: {"record_id":"R0096","doi":"10.1145/3714394.3756181","title":null,"authors":[],"year":null,"venue":null,"status":"NOT_ACCESSIBLE","source_url":null,"source_class":null,"version":"UNVERIFIED","physical_page_count":null,"first_page_check":{"physical_pdf_page":null,"field":null,"expected":null,"observed":null,"match":null},"attempts":[],"unverified_leads":[],"evidence":[],"unresolved_reason":"Explain the observed blocker and give actually checked URLs."}

# ACCEPTANCE CRITERIA

- Exactly 3 records with the given DOI mapping and zero unexpected or duplicate IDs or normalized DOIs/titles. List any shortfall explicitly.
- Title, authors, year, venue and DOI have primary scholarly metadata evidence for every record, or mark each unavailable field and reason.
- Every claimed verified PDF has one lawful source URL, a verified version, integer physical page count and first-page title or DOI match with an exact locator. Every other row has an explicit unresolved reason and attempted URLs with observed outcomes.
- Every adopted claim has a source locator or exact field value checkable independently by Codex. Zero unsupported counts, false positives, or untested links reported as tried.
- Zero project writes, extra DOI searches, undisclosed assignments, or access-control bypasses.

# BOUNDARIES

Only use public publisher pages, lawful OA indexes, institutional repositories, or clearly author/rightsholder-posted copies. Do not bypass CAPTCHA, paywalls, access controls, authentication, or DRM. Do not contact authors or institutions, sign in, buy access, use shadow libraries, change project files, or update PRISMA. No attached project file is needed or authorized for reading for this task. Do not extract or reproduce methods, attack procedures, tactics, or implementation details. These are bibliographic retrieval checks only.

Do not invent or guess sources, identifiers, file contents, quotes, locators,
search results, access attempts, decisions or numbers. Report only what you
observed in a source you actually opened. If the source was inaccessible,
missing, ambiguous or contradictory, declare the gap and give its specific
reason. Keep any candidate URL or title separate as an unverified lead.
Never present an abstract or search snippet as full-text evidence.
