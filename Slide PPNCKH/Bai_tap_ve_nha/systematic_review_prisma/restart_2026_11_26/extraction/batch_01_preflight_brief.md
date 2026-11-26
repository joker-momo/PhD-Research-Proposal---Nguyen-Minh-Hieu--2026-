# TASK
Test whether the native Gemini.app parent can open the body of one authorized Batch 01 PDF. This is one access probe, separate from the retained original task 45ae7459-5ef3-4d84-a315-7fecce8d3dfb.

# REQUIRED WORK
1. Use the attached project folder. Open only restart_2026_11_26/fulltext_retrieval/pdf/R0001.pdf directly.
2. Select one short verbatim continuous excerpt of 8–18 words under a named body section on a physical PDF page numbered 2 or later. Exclude abstract, title, captions and bibliography. If inaccessible, name the failure and do not infer the contents.
3. The single parent handles this probe. No worker is required.

# REQUIRED OUTPUT
One compact JSON object, no fences, with exactly these fields. Example shape only: {"report_id":"R0001","status":"OBSERVED","pdf_path":"restart_2026_11_26/fulltext_retrieval/pdf/R0001.pdf","page":2,"section":"body heading","excerpt":"verbatim body sentence fragment","reason":""}. Allowed status OBSERVED or NOT_ACCESSIBLE. For NOT_ACCESSIBLE use page:null and empty section/excerpt with a specific reason.

# ACCEPTANCE CRITERIA
A1: Exactly one requested report and exact relative path, zero extras.
A2: OBSERVED with one integer physical page >=2, one real body section and exactly one independently matched short excerpt from that page. Access failure is a documented FAIL.
A3: No missing schema fields, invented content, external sources, extraction claims, or source edits.

# BOUNDARIES
Only the named PDF, read-only. No searches, publication metrics, file edits, opening other files, or attempt at full extraction. Do not guess.
