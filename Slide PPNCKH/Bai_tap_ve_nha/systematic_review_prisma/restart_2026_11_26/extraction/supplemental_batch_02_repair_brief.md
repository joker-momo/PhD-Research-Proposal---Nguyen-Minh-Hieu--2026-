# TASK
Resolve exactly three residual P08 extraction keys from the completed HK261 Task 3dabd88f-f3bc-41e2-a833-9127a9933c0d.

# REQUIRED WORK
1. Open only the three original PDFs in restart_2026_11_26/fulltext_retrieval/pdf/ in the native parent; use a local PDF page viewer and preserve physical page numbering. Report actual tools and any access problem. Use PyMuPDF or Poppler if available and local MinerU then Marker only if needed and available. Do not send workers.
2. For R0080/compute_radio, use physical p. 5 §IV.A and p. 6 §IV.B. Keep the cloud GPU, modeled resources and the Table I 100 Mbps condition. Omit the different Fig. 3 bandwidth from this row unless you add an exact supporting locator.
3. For R0090/variability, use physical pp. 5–6 §§V.H and V.K. Describe swarm-load and dropout variations qualitatively. Do not state sweep ranges, effects, or repeat counts. Identify the reporting gap for repeats and uncertainty.
4. For R0110/compute_radio, use physical p. 9 §V.A and, if needed, p. 10 Table III. Qualitatively distinguish parameterized compute and channel models and absent hardware evaluation. Do not use the three-word Table III sentence from the previous response. Every quote must have four to nine words.

# REQUIRED OUTPUT
Exactly three raw JSONL keyed rows, schema {"id":"RTEST","key":"compute_radio","s":"PARTIAL","f":"Brief observed statement.","l":[[9,"V.A Simulation Setup","four to nine exact words"]],"g":"Precisely describe the missing field."}. Follow with exactly this schema as one valid JSON object, with actual tool names and unresolved keys: {"id":"SUMMARY","tools_used":["actual tool"],"key_count":3,"no_workers_used":true,"unresolved":[]}. No prose summary, Markdown or code fences. Finish with P08_SUPPLEMENT_BATCH_02_REPAIR_COMPLETE alone.

# ACCEPTANCE CRITERIA
3/3 named keys; 0 extra keys, duplicates, unsupported measurements or incorrect pages. Each quotation is exact, from one printed line, within four to nine words. Summary is one parseable JSON object and marker appears last. Explicitly document inaccessible or unresolved evidence, if any.

# BOUNDARIES
Read only the three named original PDFs. No workers, web, edits, uploads, shells, numerical synthesis, manuscript text or corpus expansion. R0080 DOI 10.1109/VTC2025-Fall65116.2025.11310097; R0090 DOI 10.1109/ICoEIT63558.2025.11457712; R0110 DOI 10.1109/tvt.2026.3755123. Their title, authors, year and venue are in the report manifest.
Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
