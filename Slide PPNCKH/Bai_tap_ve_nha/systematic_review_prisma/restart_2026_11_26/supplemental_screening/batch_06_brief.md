# TASK
Make the first-pass full-text HK261 P03/P06 decisions for the 13 original reports listed below.

# REQUIRED WORK
1. Use one Gemini.app Task and only the named original HK261 PDFs plus the protocol and official metadata sources named here. Read restart_2026_11_26/protocol_restart.md §§P03/P06. Confirm body-page access first. Use original physical PDF pages via PyMuPDF or Poppler where available, then MinerU/Marker locally only for ambiguous layout if available. If unavailable in your environment use the built-in local file reader and state any access limitation. Use only directly visible contiguous excerpts. Identify unavailable reports.
2. Evaluate E1–E7 per report. E2 is the evaluated or explicitly identified multi-UAV architecture. E3 is explicit neural model inference workload placement, execution, feature flow, or requests as evaluated. Standalone neural inference, federated training, generic computation and a neural optimizer alone do not qualify. E4 should identify actual evaluation. For an absence use the inspected method and evaluation sections. Confirm full-text English on an original body page. For any uncertainty identify the exact missing evidence and checked source. Use E5 date of assessed version and E7 exact article type and review policy, avoid assuming a policy for a different track. Distinguish accession date, print date, event date and first-publication date.
3. Use the ID/title/DOI and DOI-deposited date witnesses listed below. Record edition and page/field. Do not invent a day where the publisher specifies only a month. If a supplied date cannot be re-opened, identify it as Codex-supplied metadata and state the gap. A reference to a DOI alone is not proof of local version or review.
4. Every item needs PDF body locate and evidence. If the original methods and evaluation fall outside the review, report only the high-level eligibility fact. For security/violence-related reports, record only bibliographic and neutral eligibility evidence and no technical attacks, evasion, exploitation or operational details.
5. Give one consolidated output. If local body access fails, do not try web-only extraction. Report the explicit shortfall.

# REQUIRED OUTPUT
13 compact JSONL lines one per ID in the listed order, plus exactly one summary with {"returned_ids":[...],"unresolved_ids":[...],"workers_used":false,"complete":true}. Report schema {"id":"R0239","access":"READ","decision":"AWAITING_CLASSIFICATION","criteria":{"E1":"T","E2":"T","E3":"U","E4":"T","E5":"T","E6":"T","E7":"T"},"primary":"","secondary":[],"reason":"Exact uncertainty","evidence":[["E3","PDF",2,"Exact body section","4–9 contiguous words or exact field value","Short relevance, no unverifiable data"]]}. For each E output exactly one evidence entry, unless unavailable; a second locator is allowed only when needed. Allowed states T/F/U, READ/NOT_ACCESSIBLE, INCLUDE/EXCLUDE/AWAITING_CLASSIFICATION. For external source use exact official URL, page 0, precise field and original excerpt. PDF page index is physical, 1-based. Primary hierarchy E5,E6,E1,E7,E2,E3,E4. If a criterion is U despite another decisive exclusion, explain the specific gap in its own locator note. Do not add numerical outcomes, extra Markdown or unrelated context. The committed batch manifest supplies bibliographic metadata per ID.
# ACCEPTANCE CRITERIA
13 requested IDs with exact coverage or documented ID-specific shortfall. Zero duplicates, unexpected IDs, unsupported quantitative claims, fabricated quotations or wrong pages. Seven criteria and P06 precedence per report. 100% original PDF locators and authoritative external locators independently checked by Codex for adoption. Parent-only and no project writes or uploads.

# BOUNDARIES
Read only these named HK261 inputs. No editing, uploads, submission, exploit or attack information, operational targeting, weapons or evasion details. Do not invent or guess sources, identifiers, file contents, quotes, locators, search results, access attempts, decisions or numbers. Report only what you observed in a source you actually opened. If the source was inaccessible, missing, ambiguous or contradictory, declare the gap and give its specific reason. Keep any candidate URL or title separate as an unverified lead. Never present an abstract or search snippet as full-text evidence.

# Authorized local PDFs
All files below are original bytes in restart_2026_11_26/fulltext_retrieval/pdf.
- R0239.pdf | DOI 10.1145/3620665.3640420 | 2024-04-27 (published-online) https://api.crossref.org/works/10.1145/3620665.3640420 Publisher Main Program accepted title and exact-paper review procedure https://www.asplos-conference.org/asplos2024/cfp/index.html. Distinguish federated policy learning from collaborative evaluated inference.
- R0240.pdf | DOI 10.1145/3842435.3843959 | 2026-10-26 (published-online) https://api.crossref.org/works/10.1145/3842435.3843959 Check poster result completeness and exact track. Do not infer from page count alone.
- R0244.pdf | DOI 10.1145/3842435.3843954 | 2026-10-26 (published-online) https://api.crossref.org/works/10.1145/3842435.3843954
- R0245.pdf | DOI 10.1145/3638884.3638938 | 2024-04-23 (published-online) https://api.crossref.org/works/10.1145/3638884.3638938
- R0246.pdf | DOI 10.1145/3641512.3686384 | 2024 (publisher 2024 proceedings year only) https://doi.org/10.1145/3641512.3686384
- R0248.pdf | DOI 10.1109/tnet.2023.3289172 | 2023-07-12 (IEEE article date of publication, physical p1) https://doi.org/10.1109/tnet.2023.3289172
- R0249.pdf | DOI 10.1145/3637528.3672027 | 2024-08-24 (published-online) https://api.crossref.org/works/10.1145/3637528.3672027
- R0251.pdf | DOI 10.1145/3795154.3795350 | 2026-04 (published-online) https://api.crossref.org/works/10.1145/3795154.3795350
- R0253.pdf | DOI 10.1145/3770651 | 2025-12-02 (published-online) https://api.crossref.org/works/10.1145/3770651
- R0255.pdf | DOI 10.1145/3840749.3841574 | 2026-11-10 (published-online) https://api.crossref.org/works/10.1145/3840749.3841574 Check physical pp1–2 explicit scope and physical micro-UAV evaluation.
- R0257.pdf | DOI 10.1145/3725221 | 2025-11-26 (published-online) https://api.crossref.org/works/10.1145/3725221
- R0259.pdf | DOI 10.1145/3789418.3789446 | 2026-04-25 (published-online) https://api.crossref.org/works/10.1145/3789418.3789446
- R0260.pdf | DOI 10.1145/3769102.3770616 | 2025-12-03 (published-online) https://api.crossref.org/works/10.1145/3769102.3770616
