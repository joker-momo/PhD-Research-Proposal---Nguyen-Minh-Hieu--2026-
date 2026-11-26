# TASK
Correct the 1 failed record(s) in batch 04, linked to Task a33d1ae9-0b17-40eb-a677-bef6dac9bc2e and context 26547085-c23a-49d7-ad3f-f00e5d5b793f: R0220.

# REQUIRED WORK
1. Read the named IDs directly in restart_2026_11_26/fulltext_retrieval/inputs/batch_04.jsonl.
2. Verify the exact DOI/title with the publisher or a bibliographic registry, and check a public full-text route. Report the exact HTTPS source if it can be identified. Never repeat a malformed URL or claim to have opened an unavailable page.
3. Explain any publisher, open-access or PDF shortfall. If a source cannot be checked, use an empty URL and explicitly list it in unresolved.

# REQUIRED OUTPUT
Exactly 1 plain JSON lines, one per named ID. Keys: id, doi, identity_url, publisher_url, publisher_observation, oa_lookup_url, oa_observation, candidates (array of objects with url, version, format PDF or HTML, evidence_url), reason_if_no_pdf, unresolved. Use empty strings for unknown URLs. Use short factual observations. Locked source metadata will be joined by ID.

# ACCEPTANCE CRITERIA
T1. 1/1 named IDs and zero duplicate or extra IDs.
T2. Exact locked DOI or DOI_NOT_FOUND; URL fields are exact HTTPS or explicitly unresolved with an empty URL. Zero fabricated identifiers.
T3. All candidate links include exact format and version or an explicit uncertainty.
T4. Every row without a PDF candidate has a reason. Zero unsupported facts or file changes.

# BOUNDARIES
Read the named batch input only. Lawful public web research. No files written by Gemini, no paywall bypass, no eligibility decision or manuscript prose.
