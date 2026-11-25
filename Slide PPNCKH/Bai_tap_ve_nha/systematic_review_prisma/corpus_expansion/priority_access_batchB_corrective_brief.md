## TASK

Correct rejected batch B task01a21246-d006-7dbb-a22a-c3aee0df2978 and verify primary identity plus bounded full-text access for C15,C14,C09,C05,C23.

## REQUIRED WORK

1. Complete project onboarding in /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/AI_AGENT_START_HERE.md and its manifest. Read only public scholarly inputs. Original batchB brief, rejected notes/review and mechanically selected primary metadata are in /Users/joker/.codex/worktrees/hk261-c01-evidence/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma/corpus_expansion/priority_access_batchB_brief_2026-11-25.md, priority_access_batchB_notes.json, priority_access_batchB_review.md and batchB_primary_metadata_compact.json.
2. Fix failed A3: C09 publication.basis mentions an unlinked discovery date2026-11-18. Supply its exact primary source URL and verify it, or remove that unsupported assertion. Never infer online publication from a year-only Crossref date.
3. For all5 candidates use the supplied publisher-deposited Crossref snapshot to verify title, all listed authors, venue, year and DOI. Source each identity to the specific supplied record and original source_url. Preserve date precision:2026-01 is not a complete online date; a year-only2026 record does not prove a pre-cutoff online date.
4. Beyond the prior DOI-only failure, try at least2 distinct additional lawful routes per candidate: one publisher/Crossref identity route and one exact-title author/institutional/arXiv/proceedings full-text search. Return URLs actually opened; a search result/abstract/challenge is not full text. Stop at3 additional routes per candidate and document failures.
5. For each actually opened full text, return at least2 precise body locators spanning methods and evaluation; version/page count only when exposed. No PDF/scratch writes. No full-text claim from abstract. Maintain existing26 exact DOI/title comparison; semantic family remains unresolved unless verified.

## REQUIRED OUTPUT

One JSON object with exactly5 records and the identical per-record schema used in the original batchB brief (candidate_id,title,authors,year,venue,doi,identity_match,metadata_sources,publication,access_attempts,fulltext_url,pdf_url,version,page_count,body_locators,mechanism_notes,duplicate_existing26,study_family,unresolved_items).
summary fields:requested,returned,fulltext_bodies_opened,identity_unresolved,date_unresolved,access_shortfall_ids,duplicates_within_batch,existing26_duplicates,files_written. Add corrections:[{criterion,correction,source_locator}].

## ACCEPTANCE CRITERIA

B1: Exactly5 records with IDs C15,C14,C09,C05,C23; every shortfall explicit; all scholarly fields complete from supplied primary metadata or explicit missing marker.
B2: Every factual claim, including C09 date statements, has primary URL or exact supplied-file locator;0 unsourced discovery-date claims,0 invented metadata,0 unsupported scientific quantities.
B3: Each record has at least2 additional distinct lawful access attempts with URL/outcome; no more than3 additional attempts. Primary snapshot identity check is explicit for all5.
B4: Allowed window2021-01-01..2026-11-25; date precision retained;0 DOI-created/deposited substitutions; unresolved dates=NOT_VERIFIED.
B5: 0 normalized duplicates within batch; existing26 DOI/title check has file locator;0 abstract/challenge pages counted as full text. Each fulltext claim has methods and evaluation body locators.
B6: Exactly1 JSON object, counts agree, unresolved_items arrays present for5 records, files_written=0;0 final manuscript prose or project edits.

## BOUNDARIES

Research/evidence notes only;no manuscript editing,download/scratch writes,credentials/private correspondence,access-control circumvention or fabricated evidence. Supplied metadata is a snapshot,not proof of full text. Missing evidence must remain explicit. Gemini primary; only recognized quota authorizes the identical brief on gpt-5.6-luna/low;no escalation.
