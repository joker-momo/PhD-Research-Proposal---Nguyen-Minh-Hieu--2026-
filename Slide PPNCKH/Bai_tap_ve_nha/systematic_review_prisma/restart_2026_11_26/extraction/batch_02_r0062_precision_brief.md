# TASK
Correct only the remaining R0062 Stage 2 precision in outcomes key T03 from 0ab84741-8608-4189-844b-026fcdc3cd22.

# REQUIRED WORK
1. Parent opens `restart_2026_11_26/fulltext_retrieval/pdf/R0062.pdf` under the attached project. If relative access fails, anchor the same path under the attached host root below.
2. Read physical page 6, Effect of UAV Unavailability, where the paragraph describes Stage 2. Inspect the symbol immediately before the frame rate, including in the rendered PDF if plain text omits it. Existing accepted Stage 2 key C04-06 established an approximate value. Both the claim and the typed value in this outcome must preserve that precision. Use the actual trial condition and a short exact continuous quote.
3. Leave the already verified recovery statement, separate metric keys, unrelated scope and other P08 keys alone. If source access fails, record the reason in the single requested row.

# REQUIRED OUTPUT
One compact JSON object only. Example schema with illustrative placeholders:
{"key":"T03","report_id":"R0062","pdf_path":"restart_2026_11_26/fulltext_retrieval/pdf/R0062.pdf","status":"OBSERVED","page":6,"section":"heading","excerpt":"short literal source fragment","finding":"one scoped Stage 2 finding with approximation","quantitative":{"value":"approximately <printed value>","units":"FPS","baseline":"reference condition","denominator":"per second","workload":"source workload","conditions":"one UAV unavailable"},"reason":"","subagent_status":"UNAVAILABLE"}
Allowed status OBSERVED, NOT_ACCESSIBLE, UNVERIFIED. For unresolved status use quantitative:null, empty finding, specific reason and any verified locator. Allowed subagent_status UNAVAILABLE or UNCONFIRMED. Work in parent.

# ACCEPTANCE CRITERIA
1/1 key T03, 1/1 R0062, 0 duplicates or unrelated keys. For OBSERVED, page is physical 6, excerpt matches a body paragraph and value explicitly preserves approximation, with units, baseline, denominator, workload and conditions. Unsupported claims=0. Correct nonempty reason when unavailable or unresolved.

# BOUNDARIES
Read-only native Task, exactly one PDF, no web, no edits, no estimates, no new metrics or redrafting the separate Stage 3 recovery assertion.
Authorized attached host root: /Volumes/JokerData/PhD/PhD Research Proposal - Nguyen Minh Hieu (2026) (v3)/Slide PPNCKH/Bai_tap_ve_nha/systematic_review_prisma
