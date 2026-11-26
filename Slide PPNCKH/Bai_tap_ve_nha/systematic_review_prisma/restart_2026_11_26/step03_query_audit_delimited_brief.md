# TASK
Correct the step 03 query audit after Task a6938ff5-c0e4-40bd-94da-807344534581. Deliver a short pipe-delimited audit rather than JSON to avoid escaping failures.

# REQUIRED WORK
1. Read restart_2026_11_26/protocol_restart.md and restart_2026_11_26/step01_inventory.json in the attached project. For each of the eight query_evidence items, read its local run artifact and assess eligibility alignment. Read corpus_expansion/acm_record_capture_2026-11-26.json.
2. Compare the browser/platform behavior to official sources, or mark it local. Sources: IEEE https://ieeexplore-custom.ieee.org/search/advanced/command?reload=true ; Scopus https://service.elsevier.com/app/answers/detail/a_id/11365/supporthub/scopus/~/how-can-i-best-use-the-advanced-search%3F/ ; ACM https://libraries.acm.org/binaries/content/assets/libraries/new_acm-digital-library-user-guide.pdf ; OpenAlex https://help.openalex.org/api/searching/ .
3. For the OpenAlex complementary query, which uses exact mode for wildcards, state whether expansion with explicit multi-UAV or DNN spellings is warranted. If proposing REVISE, give a single exact OpenAlex title-and-abstract query which retains the full original expression, all four wildcards and the existing OR tail. You may add optional term variants inside OR groups. Preserve filters and date scope. Do not claim measured recall or execute it.
4. Explain local downstream limitations: ACM 79 plus 325 positions, zero initial native exports, month-level date bound; IEEE/Scopus export-derived timestamps; OpenAlex supplementary coverage and broad work types. Web of Science unsearched with null count. No causal attribution of counts across platforms.

# REQUIRED OUTPUT
Return plain text, one physical line per record. Use the literal delimiter three ASCII characters space-pipe-space ( | ). Do not use that delimiter inside a field. Leave quoted phrases in the QUERY line as plain text without escaping.
PARENT | a6938ff5-c0e4-40bd-94da-807344534581
RUN | IEEE or SCOPUS or ACM or OPENALEX | high_recall or complementary | exact local path | integer count | archived timestamp | RETAIN or REVISE or UNRESOLVED | rationale under 40 words
DOC | source key | official URL | section | support and local limitations under 45 words
QUERY | complementary | search.title_and_abstract.exact | exact candidate query, or omit whole line if no revision
LIMIT | unresolved item, repeat as needed
ACM | 79 | 325 | native export 0
WOS | null
ACTIONS | 0 | 0 | 0 | 0
Final four zeroes are formal searches, project edits, screened records and scholarly records. Eight RUN, four DOC, one ACM, one WOS and one ACTIONS. No markdown or JSON.

# ACCEPTANCE CRITERIA
D1. Exactly 8 unique RUN and 4 DOC with the expected IDs, valid fixed field counts, exact parent ID.
D2. 8/8 local paths, counts and timestamps match the archive. ACM capture distinct from native export. WoS null.
D3. Zero unsupported material claims or cross-source causal comparisons. Official documentation or clear local/unresolved labeling for all platform assertions.
D4. Verdicts in the three allowed values. Any revision preserves the original query matches by adding OR alternatives, keeping all four wildcards, scope and date.
D5. Four zero actions, explicit unresolved items. No scholarly discovery was requested, so bibliographic fields are N/A.

# BOUNDARIES
Only read the named files and their cited run artifacts. Public official documentation verification allowed. Do not execute queries, edit files, screen articles, read secrets or other folders, or write publication prose.
