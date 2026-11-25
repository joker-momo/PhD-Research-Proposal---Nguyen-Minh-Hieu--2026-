## TASK
Verify scholarly identity, publication-window evidence and lawful full-text access for exactly five HK261 expansion candidates: C15,C14,C09,C05,C23.

## REQUIRED WORK
1. Inspect only these supplied public scholarly files if needed: corpus_expansion/doi_fulltext_priority_queue.md,corpus_expansion/phd_alignment_framework.md,interim_26report/eligibility_reaudit.csv,protocol.md and its two amendments. Workspace: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma. Do not inspect unrelated private files.
2. Complete the mandatory project onboarding before research: read AI_AGENT_START_HERE.md then every required file in MUST_READ_AI_AGENT/context_manifest.yaml. Independently check each supplied DOI against primary publisher pages or publisher-deposited Crossref metadata. Inputs are unverified search targets,not accepted evidence:
C15 | 10.1109/tits.2025.3629117 | Deep Reinforcement Learning-Based Task Offloading With Collaborative Inference in UAV-Assisted Mobile Edge Computing Networks
C14 | 10.1109/jiot.2026.3746980 | CIDER: Collaborative Inference with Distilled Early-Exit Routing for Multi-UAV Edge Networks
C09 | 10.1109/jiot.2026.3755315 | NetMoE: Joint Trajectory Planning and Distributed Mixture-of-Experts Inference for UAV Swarms
C05 | 10.1109/tcsvt.2026.3745821 | MARL-based Reliability-aware Video Analytics in Multi-UAV-Assisted MEC Systems
C23 | 10.1109/wcnc57260.2024.10570535 | Efficient Pipeline Collaborative DNN Inference in Resource-Constrained UAV Swarm
3. Return verified title,listed authors,year,venue,DOI and identity-match verdict. A mismatch is an unresolved record,not permission to silently substitute a different paper. Every factual field must have a primary URL or an explicit supplied-file locator. Unknown fields use NOT_VERIFIED.
4. Check publication date against2021-01-01 through2026-11-25 inclusive. Distinguish online publication from cover/print date and DOI creation/deposit. Only source-supported publication dates establish eligibility. Do not infer date from DOI year or Crossref creation.
5. Search at most3 lawful full-text access routes per candidate: publisher OA,author/institutional repository,arXiv or official proceedings. Try returned URLs using available read-only web tools. A publisher abstract or challenge is not full text. For an actually opened full text,return identity evidence and at least2 body locators,including a method/model section and evaluation/results section. If PDF page count is exposed,record it;otherwise mark NOT_EXPOSED. Record only HTTP status/content type actually exposed by tools;use NOT_EXPOSED otherwise.
6. Return directly usable fulltext/PDF URLs for Codex-controlled retrieval. Do not save files or create scratch artifacts. Distinguish publisher version from author manuscript. For all records,fulltext-only notes may identify failure mechanisms/comparators with exact locators;abstract-only mechanism claims must remain UNVERIFIED.
7. Compare normalized DOI/title against the supplied26-report eligibility CSV. Preserve explicit uncertainty about study-family overlap. Stop after the bounded routes;return per-record access/date/identity shortfalls.

## REQUIRED OUTPUT
Return exactly one JSON object,with no Markdown prose:
{
 "records":[
  {"candidate_id":"C15","title":"...or NOT_VERIFIED","authors":["...or NOT_VERIFIED"],"year":"...or NOT_VERIFIED","venue":"...or NOT_VERIFIED","doi":"...or DOI_NOT_FOUND","identity_match":"MATCH|MISMATCH|NOT_VERIFIED","metadata_sources":[{"url":"...","fields":["title","authors","year","venue","doi"]}],"publication":{"online_date":"YYYY-MM-DD|NOT_VERIFIED","print_date":"YYYY-MM-DD|YYYY-MM|NOT_VERIFIED","window_status":"IN_WINDOW|OUT_OF_WINDOW|NOT_VERIFIED","basis":"...","source_url":"...or NOT_VERIFIED"},"access_attempts":[{"url":"...","http_status":"observed value|NOT_EXPOSED","content_type":"observed value|NOT_EXPOSED","outcome":"FULLTEXT_BODY_OPENED|ABSTRACT_ONLY|URL_ONLY|BLOCKED|NOT_FOUND","observed_evidence":"..."}],"fulltext_url":"...or NOT_FOUND","pdf_url":"...or NOT_FOUND","version":"PUBLISHER|AUTHOR_MANUSCRIPT|NOT_VERIFIED","page_count":"integer|NOT_EXPOSED","body_locators":[{"source_url":"...","locator":"...","evidence":"short factual note"}],"mechanism_notes":[{"claim":"...","locator":"...","source_url":"...","status":"FULLTEXT_VERIFIED|UNVERIFIED"}],"duplicate_existing26":"YES|NO|NOT_VERIFIED","study_family":"...or NOT_VERIFIED","unresolved_items":["..."]}
 ],
 "summary":{"requested":5,"returned":5,"fulltext_bodies_opened":0,"identity_unresolved":0,"date_unresolved":0,"access_shortfall_ids":[],"duplicates_within_batch":0,"existing26_duplicates":0},
 "criterion_responses":[{"criterion":"...","observed":"..."}]
}

## ACCEPTANCE CRITERIA
A1: Exactly5 records,one each C15,C14,C09,C05,C23;all IDs present even for failures;document the access/identity/date shortfall for every unresolved ID.
A2: All five scholarly identities contain title/authors/year/venue/DOI or explicit missing markers;zero fabricated metadata and zero silent identity substitutions.
A3: Every factual claim has a primary source URL or supplied-file locator;input titles are not evidence of verification. No DOI-created/deposited timestamp treated as publication.
A4: Every publication-window status has source-supported dates or NOT_VERIFIED;allowed window2021-01-01..2026-11-25. Out-of-window papers remain marked,not silently removed.
A5: Zero normalized DOI/title duplicates within the batch;comparison with existing26 documented with uncertainty if it cannot be checked.
A6: Every FULLTEXT_BODY_OPENED claim has at least2 body locators and readable identity evidence;zero abstract/challenge/login pages counted as full text. HTTP/MIME/page counts never guessed.
A7: Unsupported quantitative scientific claims=0. Missing evidence and study-family/version limits explicitly listed. No absence-of-mechanism inference from abstracts.
A8: Return one JSON object only;records and summary counts agree;project_files_changed=0 and files_written=0 by task boundary. No final eligibility/manuscript inclusion decision requested.

## BOUNDARIES
Read-only research and structured evidence only;no final prose,publication tables,LaTeX edits,project writes,scratch downloads,private correspondence,credentials,accounts,purchases or access-control circumvention. Missing evidence must be reported. Gemini3.8 Flash is primary;only the router's recognized provider-quota signal authorizes the identical brief on read-only gpt-5.6-luna at low effort. No other model/provider/effort escalation. Codex alone retrieves accepted files,writes the manuscript and applies the acceptance gate.
