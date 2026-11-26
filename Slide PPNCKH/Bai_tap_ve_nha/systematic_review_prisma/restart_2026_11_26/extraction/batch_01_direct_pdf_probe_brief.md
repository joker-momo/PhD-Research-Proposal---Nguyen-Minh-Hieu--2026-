# TASK
Verify that the Gemini.app Task parent can read one authorized Batch 01 PDF body page directly.

# REQUIRED WORK
1. Open `restart_2026_11_26/fulltext_retrieval/pdf/R0001.pdf` in the attached project. First use the attached folder root; if lookup fails, resolve that relative path under the authorized host root below. Use the Task parent.
2. On physical PDF page 2, select 8–18 consecutive words from a body paragraph after a heading. Preserve words exactly, without ellipses, and return the heading on that physical page.
3. If the PDF cannot be read, return a specific error and identify which in-project path was tried. Do not extract findings.

# REQUIRED OUTPUT
One JSON object only, example shape:
{"report_id":"R0001","status":"OBSERVED","pdf_path":"restart_2026_11_26/fulltext_retrieval/pdf/R0001.pdf","page":2,"section":"actual page heading","excerpt":"exact consecutive body words","reason":""}
Allowed status OBSERVED or NOT_ACCESSIBLE. For NOT_ACCESSIBLE use null page, empty section/excerpt, and nonempty reason.

# ACCEPTANCE CRITERIA
1/1 ID and correct relative PDF path. One nonabstract excerpt at physical page 2, exact and contiguous, and actual body heading verified on that page. 0 extraction results, duplicate IDs or guesses. On failure keep R0001 explicitly unresolved.

# BOUNDARIES
Read-only, one parent Task. No web, extra files, writing, or modification.
Authorized host root: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma
