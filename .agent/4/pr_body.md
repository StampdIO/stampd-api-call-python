## Summary

- Fix the mistyped URL scheme in the stampd.io link on README.md line 5: `https;//stampd.io` (semicolon) → `https://stampd.io` (colon), so the Markdown link resolves correctly.

Closes #4

## Test plan

- [x] Confirmed README.md no longer contains `https;//` (grep returns no matches)
- [x] Confirmed line 5 now reads `[stampd.io](https://stampd.io)` and the link resolves
- [x] No code, behavior, or dependency changes — docs-only single-character fix

## Notes for reviewer

This is a Python example repo, so the Deno `fmt`/`lint`/`test` toolchain does not apply. Per plan.json, no automated test is warranted for a docs-only single-character correction; verification is the grep checks above.
