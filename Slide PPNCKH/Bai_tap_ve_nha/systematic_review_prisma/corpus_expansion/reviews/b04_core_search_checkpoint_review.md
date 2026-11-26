# B04 Core Search Checkpoint Review

**Review timestamp:** 2026-11-26T13:51:18+07:00

**Query set:** 1.3

**Status:** `BLOCKED_USER_INSTITUTIONAL_SIGN_IN`

This is a checkpoint review, not B04 acceptance. Four official-interface search
runs produced visible totals. None produced an importable record-level export.
Scopus and Web of Science stopped before query execution at their institutional
sign-in pages. No missing count is inferred.

| Criterion | Verdict | Objective evidence |
|---|---|---|
| Eight exact query variants accounted for | PASS | Eight new ledger rows: two each for IEEE, ACM, Scopus and Web of Science. |
| Official-interface searches executed | FAIL | 4/8 executed: IEEE 2/2, ACM 2/2, Scopus 0/2, Web of Science 0/2. |
| Exact query retained for every executed run | PASS | Four immutable JSON observation records contain the exact pasted query and query-set version 1.3. |
| Search timestamp and filters retained | PASS | All six observation/access records contain RFC 3339 `observed_at`; four completed searches record active filters and limitations. |
| Reported totals recorded without inference | PASS | IEEE 47 and 26; ACM 79 and 325; Scopus and Web of Science totals are null. |
| Record-level exports obtained and parsed | FAIL | 0/8 importable exports. IEEE required personal sign-in; ACM Basic Edition marked export as Premium; Scopus and Web of Science required institutional sign-in before searching. |
| Raw evidence and checksum retained | PASS | Six JSON records plus `sources/raw/core_searches/checksums.sha256`; 6/6 checksums verify. |
| Continuation/cap arithmetic reconciles | PASS | No partial export or continuation was created, so exported totals are 0 and no continuation arithmetic is asserted. |
| Unsupported quantitative claims | PASS | 0; only totals visibly reported by the official interfaces are recorded. |
| B04 completion gate | FAIL | User must sign in to Scopus and Web of Science; authenticated export access is also needed for IEEE and ACM or an explicit lawful export alternative must be documented before B05. |

## Resume point

1. User signs in to Scopus and Web of Science in the local browser.
2. Codex runs both version-1.3 queries on each platform and records collection,
   active editions, filters, count, export count, format, raw file and checksum.
3. Codex revisits IEEE and ACM export after any available authenticated access.
4. B04 is accepted only after every completed export parses and all eight runs
   have no unexplained count difference.
