# TASK
Extract bounded architecture, evaluation and appraisal evidence for HK261 R0082 from the retained LLHR arXiv v1 PDF.

# REQUIRED WORK
1. In the parent Task, open only restart_2026_11_26/fulltext_retrieval/pdf/R0082.pdf. Verify access before extraction with a short exact body quote, physical page and file path; if unavailable, return an explicit shortfall.
2. Extract topology, workloads, partition/assignment, solver, environment and resilience. Read the evaluation text/figures for exact printed results with conditions; classify graph-only results as PLOT_ONLY without estimating them. Include baselines, units, direction and conditions whenever printed.
3. Propose engineering appraisal judgments D01–D10 in order: system model, assumptions, reproducible configuration, comparator, metric alignment, variability/sensitivity, network/mobility realism, claim bounds, artifact availability, limitations/declarations. Use YES, PARTIAL, NO or UNVERIFIED; provide precise locators and rationale; identify the section checked for absence.
4. Return one parent result, with actual internal worker use and assignments. Use the parent to read the PDF if any worker lacks access. Distinguish physical page index from printed labels.

# REQUIRED OUTPUT
Return compact JSONL. First one identity object with record_id, title, authors, year, venue, doi or DOI_NOT_FOUND, source_version, source, physical_pdf_pages, access, physical_page and exact excerpt. Then six objects keyed topology, workload, partition, solver, evaluation, resilience. Then ten objects keyed D01 through D10. Each fact or judgment object has record_id, key, status, finding, source, physical_page, section, excerpt. Example shape {"record_id":"R0082","key":"topology","status":"VERIFIED","finding":"description","source":"restart_2026_11_26/fulltext_retrieval/pdf/R0082.pdf","physical_page":2,"section":"I","excerpt":"exact contiguous text"}. Then one outcomes object with entries containing exact printed values and explicit unit/condition/locator/excerpt, or an empty list and PLOT_ONLY/NOT_REPORTED/UNVERIFIED with locators. End with one footer containing complete, workers_used, worker_assignments and unresolved_keys. For facts use VERIFIED, NOT_REPORTED, NOT_ACCESSIBLE or UNVERIFIED. Keep excerpts short, contiguous, and without ellipses.

# ACCEPTANCE CRITERIA
Exactly one named record and zero duplicates. One access check, six characterization keys, ten appraisal keys and one outcomes status, or explicit accessible/inaccessible shortfalls. Every proposed factual extract names source, physical page and exact excerpt. Every number has units, conditions and a source. Zero inferred plot values, unsupported numbers, invented DOI, or assertions that arXiv page locators are IEEE pages. Every accepted entry independently verified by Codex against the PDF.

# BOUNDARIES
Read-only. No project edits, drafts, author outreach, credentials, uploads of PDFs or alternate copy substitution. Use the named PDF and, for identity only, https://arxiv.org/abs/2305.15858v1. IEEE publisher PDF is unavailable locally. Record its DOI only if observed in the allowed identity source. Do not infer version equivalence or change eligibility. Use approved PDF reading via local PDF text/rendering if available and say if inaccessible.
Do not invent or guess sources, identifiers, file contents, quotes, locators,
search results, access attempts, decisions or numbers. Report only what you
observed in a source you actually opened. If the source was inaccessible,
missing, ambiguous or contradictory, declare the gap and give its specific
reason. Keep any candidate URL or title separate as an unverified lead.
Never present an abstract or search snippet as full-text evidence.
