# TASK
Correct the rejected R0082 LLHR source and appraisal evidence from parent b62a3afe-8942-49e3-acf6-2197062d963e and compare its evaluation with R0019.

# REQUIRED WORK
1. Open only restart_2026_11_26/fulltext_retrieval/pdf/R0082.pdf and restart_2026_11_26/fulltext_retrieval/pdf/R0019.pdf. Verify ability to read each with a short exact body quote before comparing.
2. Recheck TOPOLOGY (R0082 p. 2 and p. 4), EVALUATION (R0082 pp. 5–6) and D01, D03, D07, D08, D09. Distinguish explicit evidence, limited detail and not reported. Use YES, PARTIAL, NO, NOT_REPORTED, NOT_APPLICABLE or NOT_YET_ASSESSED. D01 asks whether system question and model are clear; D03 covers reproducible configuration; D07 mobility/channel detail; D08 generality; D09 artifact availability. Report any absent evidence using the scope examined and one short contiguous context quote, not fabricated evidence of absence.
3. Check the FAMILY key using R0082 §III–IV/Fig. 5 and R0019 physical pp. 9–15/Fig. 16. Report observable shared setup and differences in method/outcome comparisons. Leave common underlying data or run reuse unresolved if neither source documents it. Transcribe figure captions, not numeric estimates from curves. Report actual internal worker use.

# REQUIRED OUTPUT
JSONL with two ACCESS rows (record_id, title, authors, year, venue, DOI or DOI_NOT_FOUND, anchors), and eight evidence rows keyed TOPOLOGY, EVALUATION, D01, D03, D07, D08, D09, FAMILY. Every evidence object has key, finding, status, anchors as entries containing record_id, exact relative PDF path, physical_page, section_or_figure, excerpt. For FAMILY include anchors for both PDFs. Example anchor {"record_id":"R0082","path":"restart_2026_11_26/fulltext_retrieval/pdf/R0082.pdf","physical_page":2,"section_or_figure":"II","excerpt":"contiguous exact substring"}. Final footer has complete, unresolved_keys, workers_used and worker_assignments.

# ACCEPTANCE CRITERIA
Two accessible original files or explicit access failure; eight distinct evidence keys or explicit shortfalls. Every exact excerpt must match the supplied physical PDF page. Zero unsupported quantitative claims, figure-estimated numbers, invented DOI, or inference of independent samples. Every gap names its cause.

# BOUNDARIES
Read-only. No project edits, drafting, external uploads, substitution, eligibility rulings or access outside the two named files. Original PDFs and their physical pages are the only methodological evidence. If tooling cannot return exact contiguous text, mark that anchor unresolved.
Do not invent or guess sources, identifiers, file contents, quotes, locators,
search results, access attempts, decisions or numbers. Report only what you
observed in a source you actually opened. If the source was inaccessible,
missing, ambiguous or contradictory, declare the gap and give its specific
reason. Keep any candidate URL or title separate as an unverified lead.
Never present an abstract or search snippet as full-text evidence.
