## TASK
Correct five named linkage entries from native task ec1e09ea-ba22-4b5f-bda1-3a459cb522c1, using only authorized original HK261 PDFs and the supplied identity records, then stop.

## REQUIRED WORK
1. Read the exact original title/DOI region for R0058. Return the precise p. 1 DOI excerpt (plain printed ASCII DOI is sufficient), title and byline, distinguishing the 2026 PDF imprint and date first published 6 December 2025. The PDF custom font garbles several initial title glyphs in extracted text.
2. Reconcile R0077. Physical PDF p. 1 identifies the accepted manuscript arXiv:2503.16146v3 and says Accepted for publication in Journal of Systems Architecture. The locked queue and registry record at https://api.crossref.org/works/10.1016/j.sysarc.2026.103804 identify the matching publication DOI. Record both identifiers and distinguish their versions. Do not claim the DOI is printed on the PDF.
3. Reconcile R0292. Physical PDF p. 1 gives the printed Tracking title and DOI. The publisher deposit at https://api.crossref.org/works/10.1145/3711875.3737661 gives the Monitoring title. The already accepted batch 07 review links the exact DOI, author list, and PDF. Report both titles with correct source plus venue and year from the deposited record.
4. Recheck pair R0036/R0048. Both bylines list Wen Wu. Establish whether the method and evaluation support DISTINCT or a P07 family without making claims about funding or absence of citations. Add pair R0145/R0223 because both evaluate LLM-backed multi-UAV task planning. For both pairs use separate physical-page setup or results evidence from each original. Do not rely on shared topic or authors alone.

## REQUIRED OUTPUT
Exactly five JSONL objects plus a summary. Identity example {"key":"R0058","title":"...","authors":"...","year":2026,"venue":"...","doi":"...","version":"...","support":[{"source":"restart_2026_11_26/fulltext_retrieval/pdf/R0058.pdf","page":1,"section":"...","quote":"..."}]}. Pair example {"key":"R0036/R0048","decision":"DISTINCT","reason":"...","support":[{"source":"...","page":1,"section":"...","quote":"..."},{"source":"...","page":1,"section":"...","quote":"..."}]}. All PDF pages are physical 1-based. Registry locator may be field name plus exact value. Summary names returned and unresolved keys with reason, reports actual workers/access, and ends on a standalone line with P07_SUPPLEMENT_CORRECTION_COMPLETE.

## ACCEPTANCE CRITERIA
C1. Exactly the five named keys once. Three identities contain title, byline, year, venue, DOI or documented marker, and source and locator for each corrected field. No duplicate or mismatched DOI or title and no collapse of publication identity into PDF version.
C2. The two pair verdicts each have one direct Methods or Evaluation locator and contiguous quote per original, and describe the differing assessment designs if DISTINCT. No unsupported claim of disjoint authors, disjoint grants, or absent citations.
C3. Zero unsupported quantitative outcomes or undocumented gaps. Native parent Task only, no secondary workers with unconfirmed access, no writes or source uploads. Codex checks every accepted locator and rationale.

## BOUNDARIES
Use only the five named keys. Do not re-screen, cite the historical corpus, report performance outcomes, draft prose, or edit files.
Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.
