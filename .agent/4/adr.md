## Architect ADR

**Approach**: Documentation-only, single-character correction. `README.md` line 5 reads `Visit [stampd.io](https;//stampd.io) ...` — the link's URL scheme uses a semicolon (`https;//`) instead of a colon (`https://`), so the link does not resolve. Change the one character so the URL becomes `https://stampd.io`. No code, behavior, or dependency changes.

**Files to touch**:
- `README.md` — replace `https;//stampd.io` with `https://stampd.io` on line 5 (the only occurrence in the repo).

**Tests to add**:
- None warranted. This is a Python repo (`Pipfile`, `apitest.py`) with no test harness for documentation; a unit test for a static doc link is overkill. Verification is a grep: README contains `https://stampd.io` and no remaining `https;//`.

**Risk level**: low
**Rationale for risk**: One-character edit to a prose Markdown file; no external IO, no logic, no untrusted input, ≤ 1 LOC, 1 file.

**Estimated LOC**: 1

**Out of scope**: Don't reflow, restyle, or "modernize" the README; don't touch `apitest.py` or dependencies; don't add a test framework; don't audit other links beyond confirming this is the only `https;//` typo (it is).

— architect (Opus)
