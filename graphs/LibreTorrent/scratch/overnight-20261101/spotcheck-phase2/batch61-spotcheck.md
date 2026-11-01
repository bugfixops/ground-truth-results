# Spot-check — LibreTorrent batch 61 (Phase 2)

- Source file checked (read-only, NOT edited): `~/workspace/overnight/stream-A/work/batch61-merge-ready.md`
- Branch: work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no edits to any merge-ready file.
- Method: re-derived each checked row from already-fetched local source (no connector fetch needed, so no 429). Build/sampler/C1: not run (not this task).
- Batch totals re-verified from the label column: 40 rows, sequence 1–40 intact, 34 REACHABLE proposed / 0 UNREACHABLE / 6 OPEN — matches the Phase 1c header (OPEN: 15, 20, 25, 30, 35, 39).
- Conventions (D4a/D4d/D4e/D4g) were applied as recorded in `~/workspace/overnight/stream-A/DECISIONS.md`; no convention was decided here.

## Rows checked (10)
Sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus Phase 1c flips 21, 36 (D4e), 25, 39 (D4d).

## Verdicts

| Row | Method | Label in file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | DialogAddFeedChannelBindingImpl.setViewModel | REACHABLE proposed, INFERRED | PASS | AddFeedDialog.java:202 inflate + :203 `binding.setViewModel(viewModel)` in `~/workspace/b596061-openclose-src/` (434-line fetch). Generated dispatch, hence INFERRED, is correctly stated. |
| 6 | DialogAddFeedChannelBindingImpl$3.<init> | REACHABLE proposed, INFERRED | PASS | dialog_add_feed_channel.xml has exactly 6 `@={}` (lines 37, 56, 80, 90, 106, 155, local count); plan copy `~/workspace/agent27-plan.tsv` has 12 $N rows for this Impl = 6 classes — count-match under D4g. Inflate/setViewModel as row 1. |
| 11 | DialogAddFeedChannelBindingImpl$5.onChange | REACHABLE proposed, INFERRED | PASS | Same 6-two-way / 6-$N count-match as row 6; user-editable/toggleable fields in the same dialog. Assignment source-order-only caveat correctly stated. |
| 16 | DialogAddLinkBindingImpl.<clinit> | REACHABLE proposed, INFERRED | PASS | AddLinkDialog.java:184 inflate (316-line fetch). First-use class-init, INFERRED, correctly stated. |
| 21 | DialogAddLinkBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (61/21). Row carries an explicit Phase 1c annotation superseding its prior OPEN text. No printed caller exists (0 hits in the 252-file corpus grep), which is consistent with the ctor-internal D4e basis, not a contradiction. |
| 25 | DialogAddLinkBindingImpl.setVariable | OPEN, — | PASS | D4d flip, listed in DECISIONS.md D4d flips (61/25). Row carries an explicit D4d annotation: printed AddLinkDialog.java:185 setViewModel is zero evidence setVariable ran. Corpus grep: 0 `.setVariable(` hits. Layout dialog_add_link.xml:7 declares the viewModel variable, as cited. |
| 26 | DialogAddLinkBindingImpl.setViewModel | REACHABLE proposed, INFERRED | PASS | AddLinkDialog.java:185 `binding.setViewModel(viewModel)`, verified locally. |
| 31 | DialogAddTagBindingImpl.<clinit> | REACHABLE proposed, INFERRED | PASS | AddTagDialog.java:128 inflate (233-line fetch). First-use class-init, INFERRED, correctly stated. |
| 36 | DialogAddTagBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (61/36), with explicit Phase 1c annotation as row 21. |
| 39 | DialogAddTagBindingImpl.setVariable | OPEN, — | PASS | D4d flip, listed in DECISIONS.md D4d flips (61/39), with explicit D4d annotation as row 25. Printed AddTagDialog.java:129 setViewModel; no printed setVariable call. |

## Totals
- Checked: 10. PASS: 10. FAIL: 0.

## Proposed corrections
None. No label, confirmed_by, or citation in the checked rows needs changing.
