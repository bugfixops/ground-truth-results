# Spot-check — LibreTorrent batch 63 (Phase 2)

- Source file checked (read-only, NOT edited): `~/workspace/overnight/stream-A/work/batch63-merge-ready.md`
- Branch: work-2026-10-31, repo bugfixops/ground-truth-results. No pushes, no edits to any merge-ready file.
- Method: re-derived each checked row from already-fetched local source (no connector fetch needed, so no 429). Build/sampler/C1: not run (not this task).
- Batch totals re-verified from the label column: 40 rows, sequence 1–40 intact, 34 REACHABLE proposed / 0 UNREACHABLE / 6 OPEN — matches the Phase 1c header (OPEN: 1, 6, 10, 15, 20, 24).
- Conventions (D4a/D4d/D4e/D4f/D4g) were applied as recorded in `~/workspace/overnight/stream-A/DECISIONS.md`; no convention was decided here.

## Rows checked (9)
Sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus Phase 1c flips 7, 21 (D4e). (Phase 1c also records D4a/D4d rows in this batch as already-OPEN standing rows, unchanged — rows 1, 10, 15, 24; row 1 of those is in the sample.)

## Verdicts

| Row | Method | Label in file | Verdict | Evidence |
|---|---|---|---|---|
| 1 | DialogGoToFolderBinding.getViewModel | OPEN, — | PASS | OPEN correct per D4a standing list (63/1). GoToFolderDialog.java: 0 `getViewModel` hits, setViewModel at :100 (166-line fetch, verified). No printed getter caller. |
| 6 | DialogGoToFolderBindingImpl.hasPendingBindings | OPEN, — | PASS | OPEN correct per D4f (63/6). 0 hits for hasPendingBindings in the 252-file corpus grep; no printed generated/library rebind body, which is the named resolver. |
| 7 | DialogGoToFolderBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (63/7); Phase 1c header documents it. Row text "No printed caller" is true and consistent with the ctor-internal D4e basis. |
| 11 | DialogGoToFolderBindingImpl.setViewModel | REACHABLE proposed, INFERRED | PASS | GoToFolderDialog.java:100 `binding.setViewModel(viewModel)`, verified locally (inflate at :99). |
| 16 | DialogLogFilterBindingImpl.<clinit> | REACHABLE proposed, INFERRED | PASS | SessionLogFilterDialog.java:98 inflate (120-line fetch), verified locally. |
| 21 | DialogLogFilterBindingImpl.invalidateAll | REACHABLE proposed, INFERRED | PASS | D4e flip, listed in DECISIONS.md D4e flips (63/21); same basis as row 7. |
| 26 | DialogLogFilterBindingImpl$1.<init> | REACHABLE proposed, INFERRED | PASS | D4g count-match: dialog_log_filter.xml has exactly 5 `@={}` (lines 24, 33, 42, 51, 60, local count); plan has 10 $N rows for this Impl = 5 classes. Inflate SessionLogFilterDialog.java:98 verified. |
| 31 | DialogLogFilterBindingImpl$3.onChange | REACHABLE proposed, INFERRED | PASS | Same 5-two-way / 5-$N count-match as row 26; cross-reference to row 27 ("Fires on mutable-params field notify; see row 22") is coherent — row 22 is the onChangeViewModelMutableParams row. |
| 36 | DialogSelectTagBinding.<init> | REACHABLE proposed, INFERRED | PASS | SelectTagDialog.java:128 inflate (195-line fetch), verified locally; abstract ctor via Impl super-call, INFERRED, correctly stated. |

## Totals
- Checked: 9. PASS: 9. FAIL: 0.

## Proposed corrections
None. No label, confirmed_by, or citation in the checked rows needs changing.
