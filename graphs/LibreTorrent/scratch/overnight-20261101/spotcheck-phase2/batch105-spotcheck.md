# LibreTorrent batch 105 — Phase 2 spot-check — UNVERIFIED spot-check, NOT a merge

- Batch: 105. Source checked: already-fetched local copies in ~/workspace/b105-106-src/; no connector fetch needed, no 429. No Phase-1 label-change revision note was found in this file, so samples only.
- Rows checked (8): samples 1, 6, 11, 16, 21, 26, 31, 36.
- Build/sampler/C1: not run (not this task). No edit made to the merge-ready file. No convention decided. Lambda numbering is source-order inferred, not bytecode-verified; labels are unaffected by a swap within a group.

## Per-row verdicts

| # | Method | Filed label | Verdict | Evidence (printed source) |
|---|---|---|---|---|
| 1 | GoToFolderDialog.initAlertDialog | REACHABLE SOURCE | PASS | GoToFolderDialog.java:125 `initAlertDialog(binding.getRoot())` in initLayoutView; def :128-145. |
| 6 | GoToFolderDialog.lambda$onResume$0 | REACHABLE INFERRED | PASS | setOnKeyListener lambda GoToFolderDialog.java:77-86 in onResume (:73); body calls onBackPressed :80; key dispatch, not printed. |
| 11 | GoToFolderDialog.onResume | REACHABLE INFERRED | PASS | Def GoToFolderDialog.java:73-87; dialog shown by FileManagerDialog.java:553 (goToDirectoryDialog, via newInstance :552); DialogFragment dispatch, not printed. |
| 16 | GoToFolderViewModel.<init> | REACHABLE INFERRED | PASS | GoToFolderDialog.java:95-96 `provider.get(GoToFolderViewModel.class)`; def GoToFolderViewModel.java:31-33; ViewModelProvider dispatch, not printed. |
| 21 | LogActivity.lambda$new$5 | REACHABLE INFERRED | PASS | One of the three field runnables LogActivity.java:434/436/438-441 (hideFabUpRunnable, hideFabDownRunnable, handleUpdateAdapter), driven by Handler postDelayed (:412/:425) or the submitList callback (:120); dispatch, not printed. |
| 26 | LogActivity.lambda$onCreate$2 | REACHABLE INFERRED | PASS | fabUp click lambda LogActivity.java:124-132 (pauseLog, hideFabUp, scroll to 0, resumeLog); View-click dispatch, not printed. |
| 31 | LogActivity.onItemClicked | REACHABLE INFERRED | PASS | Via LogAdapter$ViewHolder.lambda$bind$0, LogAdapter.java:102-105 (`listener.onItemClicked(entry)`); def LogActivity.java:461-469. Adapter click dispatch, not printed. |
| 36 | LogActivity.onStop | REACHABLE INFERRED | PASS | Def LogActivity.java:159-165 (disposables.clear, removeOnPropertyChangedCallback); lifecycle dispatch, not printed. |

## Totals

- PASS: 8 / FAIL: 0 (of 8 checked).
- Proposed corrections: none.
