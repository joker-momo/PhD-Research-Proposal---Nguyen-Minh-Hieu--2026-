# TASK
Verify that the native Gemini.app parent Task can read the body of one authorized HK261 full-text PDF.

# REQUIRED WORK
1. Open only the original project-relative PDF named below in the attached project. Inspect one short, ordinary sentence from the body on physical PDF page 2. Use direct in-app PDF reading or local PyMuPDF if available, with Poppler fallback. If ordinary extraction fails, use only already-available local MinerU or Marker with original-page verification. Report access failure if these tools are unavailable and the page cannot be read.
2. Return one exact contiguous excerpt of 6 to 14 words from the body on that page, with the containing section or region. Use the native parent Task and report workers_used as false. Do not use an external copy.

# REQUIRED OUTPUT
Return one JSON object: {"id":"R0096","pdf":"restart_2026_11_26/fulltext_retrieval/pdf/R0096.pdf","physical_page":2,"section_or_region":"body section or region","exact_quote":"contiguous words","status":"VERIFIED_ACCESS","reason":"","workers_used":false}. Allowed status values: VERIFIED_ACCESS, NOT_ACCESSIBLE. If inaccessible, keep the ID and path, leave quote empty, and give the exact observed reason.

# ACCEPTANCE CRITERIA
A1: Exactly one row, with R0096 and the exact named path. Unexpected or duplicate IDs equal zero.
A2: For VERIFIED_ACCESS, Codex independently verifies the exact quote and region on physical page 2 of the original PDF. Unsupported assertions equal zero. For NOT_ACCESSIBLE, the observed failure is explicit and the access gate remains unmet.
A3: Workers used equals zero. External uploads, edits and invented details equal zero.

# BOUNDARIES
This is an access check only. Read only restart_2026_11_26/fulltext_retrieval/pdf/R0096.pdf. No writing, editing, browsing, or external submission of the PDF. Return no implementation instructions or operational details. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
