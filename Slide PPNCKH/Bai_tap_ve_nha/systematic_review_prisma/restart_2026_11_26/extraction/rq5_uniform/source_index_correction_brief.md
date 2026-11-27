# TASK
Correct two evaluation setting labels from parent Task 5b989d57-74a6-45e0-ba85-f393c60e5cf4 against the original PDFs.

# REQUIRED WORK
1. Handle these two IDs in the parent because the previous workers had no approved local access. First verify access to one body page of each PDF and stop that ID if access fails.
2. For R0062 read physical pp. 5–6 near Fig. 4 and Fig. 6. Distinguish what is measured in the Jetson prototype from the deliberately imposed disconnection. Qualify the measurement setting separately from any failure emulation.
3. For R0125 read physical p. 3, Experimental Results. Distinguish workstation-hosted worker processes and their controlled resources from a simulation of measured hardware execution.
4. Return one corrected row per ID. Report unresolved evidence as such. No other IDs or tasks.

# REQUIRED OUTPUT
Return two JSONL rows with the fields in this example: {"id":"R0062","status":"READ","pdf_page":5,"locator":"Fig. 4 and neighboring body","setting":"physical_prototype","excerpt":"one short exact contiguous body quotation","qualification":"short fact supported by the excerpt and the cited setup"}. Allowed settings physical_prototype, host_emulation, ambiguous. Allowed access statuses READ, NOT_ACCESSIBLE, UNVERIFIED. Use 1-based physical PDF pages, and for inaccessible or ambiguous evidence give the reason. End with RETURNED_COUNT, UNRESOLVED_IDS, WORKER_ASSIGNMENTS and END.

# ACCEPTANCE CRITERIA
Exactly two unique target IDs R0062 and R0125, zero extra IDs; list any unresolved IDs. A READ row has a valid PDF page, section or figure, exact contiguous source quotation and evidence-supported setting. Unsupported claims, values, and new bibliography entries equal zero. Codex independently verifies each source and setting before adoption. Record that the parent read the sources directly or state the actual worker status.

# BOUNDARIES
Read only the two supplied PDF paths in the authorized HK261 project folder. Prefer direct page-level selectable text or original-page rendering when layout breaks. No internet, outcome values, new bibliography, project file changes or manuscript writing.

Do not invent or guess sources, identifiers, file contents, quotes, locators,
search results, access attempts, decisions or numbers. Report only what you
observed in a source you actually opened. If the source was inaccessible,
missing, ambiguous or contradictory, declare the gap and give its specific
reason. Keep any candidate URL or title separate as an unverified lead.
Never present an abstract or search snippet as full-text evidence.

## Authorized input
- R0062 restart_2026_11_26/fulltext_retrieval/pdf/R0062.pdf
- R0125 restart_2026_11_26/fulltext_retrieval/pdf/R0125.pdf
