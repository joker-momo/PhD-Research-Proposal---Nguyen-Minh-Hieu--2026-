## TASK

Find up to6 additional readable primary full texts on collaborative DNN inference in multi-UAV systems,excluding the existing27 assessed reports,with an explicit shortfall if fewer than6 can be verified.

## REQUIRED WORK

1. Complete project onboarding at /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/AI_AGENT_START_HERE.md and its manifest. Read protocol.md and Amendments001–002. Existing assessed reports are in /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/interim_27report/eligibility_reaudit.csv. New candidates must be compared to that file by normalized DOI/title.
2. Search primary publisher/proceedings,author/institutional repositories and arXiv for2021-01-01..2026-11-25 primary research with at least2 UAVs or an explicit swarm;DNN/CNN/LLM inference must be partitioned,assigned,migrated,fused or jointly orchestrated. Exclude training-only,generic indivisible offloading,single-UAV-only perception,secondary reviews and incomplete demos.
3. Prioritize SN Computer Science with at least2 distinct focused queries;report if no new eligible readable article is found there. Scientific eligibility takes priority over venue. Pending targets C22,C24,C25,C12,SNCS_01 may be revisited if a new lawful full-text route exists;preserve their candidate IDs. Do not re-add C01 or any existing27 DOI/title.
4. Use no more than12 targeted discovery queries and at most3 full-text routes per proposed record. Return the actual query,platform/source URL and observed outcome for each run;never invent search totals. For each readable full text,verify complete bibliographic identity,source version,publication date,methods and evaluation body locators,architecture/model/partition scope and evaluation modality. Abstract-only or challenge pages cannot satisfy full text.
5. Prefer studies transferable to layer partition/UAV assignment,activation-transfer/network/energy costs,online adaptation or controlled failure comparisons. Distinguish peer-UAV layer execution from multi-UAV edge/cloud request orchestration. No solver/optimality/recovery claim from abstracts.
6. Return exactly6 verified readable records if available;otherwise return verified records plus explicit requested6/returned count and source-located shortfall. Do not fill missing slots with ineligible articles. No downloads or source/project writes.

## REQUIRED OUTPUT

One JSON object:
{"search_log":[{"query":"exact query","platform":"...","source_url":"...","outcome":"observed outcome or unavailable;no invented count"}],"records":[{"candidate_id":"existing ID or NEW_...","title":"...","authors":["all listed authors"],"year":2025,"venue":"...","doi":"...or DOI_NOT_FOUND","identity_sources":["primary URL"],"publication_date":"source-supported precision","publication_date_source":"URL","window_status":"IN_WINDOW|NOT_VERIFIED","fulltext_url":"actually opened body URL","pdf_url":"direct lawful URL or NOT_FOUND","source_version":"publisher|author_manuscript|preprint","body_locators":[{"locator":"method section/page","evidence":"short note"},{"locator":"evaluation section/page","evidence":"short note"}],"architecture_scope":"source-located topology and number/role of UAVs","inference_mechanism":"source-located model and partition/orchestration","evaluation_modality":"source-located simulation/emulation/analysis/prototype/flight boundary","doctoral_fit":"source-located transferable configuration or comparator;no inferred performance","duplicate_existing27":false,"related_study_family":"source-supported relation or NOT_VERIFIED","unresolved_items":[]}],"summary":{"requested":6,"returned":0,"shortfall":6,"sncs_queries":2,"sncs_verified_fulltexts":0,"duplicates":0,"files_written":0},"shortfall_reasons":[]}

## ACCEPTANCE CRITERIA

N1: Exactly6 verified records OR exact documented shortfall with returned+shortfall=6;all returned records have full title,all authors,year,venue,DOI/missing marker;0 duplicated normalized DOI/title and0 existing27 duplicate records.
N2: Every returned record has an actually opened readable full-text URL and at least2 body locators spanning methods/evaluation;0 abstract/challenge-only records in returned verified list.
N3: Publication window2021-01-01..2026-11-25 is source-supported with date precision preserved;unresolved dates explicitly NOT_VERIFIED and not counted as verified eligible additions.
N4: At least2 SNCS-focused queries in actual search log;no more than12 queries;every factual claim has primary URL/body locator;unsupported quantitative effects0.
N5: Source version,architecture,model/inference and evaluation boundaries present for every returned record;0 training-only/single-UAV-only/generic-offloading padding. Study-family uncertainty explicit.
N6: One JSON object,summary arithmetic correct,all unresolved/shortfalls explicit;worker file writes0;no final manuscript prose or project edits.

## BOUNDARIES

Read-only research/evidence notes only. No manuscript drafting,publication tables,downloads/scratch writes,credentials,private correspondence,access-control bypass,unverified references or fabricated results. Missing evidence is reported rather than invented. Gemini primary;only recognized quota authorizes identical brief on gpt-5.6-luna/low;no model/effort escalation.
