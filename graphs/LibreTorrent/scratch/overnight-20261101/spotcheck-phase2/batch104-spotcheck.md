# LibreTorrent batch 104 — Phase 2 spot-check — UNVERIFIED spot-check, NOT a merge

- Batch: 104. Source checked: already-fetched local copies in ~/workspace/b103104-src/; no connector fetch needed, no 429. No Phase-1 label-change revision note was found in this file, so samples only.
- Rows checked (8): samples 1, 6, 11, 16, 21, 26, 31, 36.
- Build/sampler/C1: not run (not this task). No edit made to the merge-ready file. No convention decided.

## Per-row verdicts

| # | Method | Filed label | Verdict | Evidence (printed source) |
|---|---|---|---|---|
| 1 | FileManagerSpinnerAdapter.addItems | REACHABLE SOURCE | PASS | FileManagerDialog.java:210 (onCreate) and :645 (reloadSpinner); def FileManagerSpinnerAdapter.java:110-113. |
| 6 | FileManagerSpinnerAdapter.getItemId | REACHABLE INFERRED | PASS | Def FileManagerSpinnerAdapter.java:128-131; adapter set at FileManagerDialog.java:211; Spinner framework dispatch, not printed. |
| 11 | FileManagerSpinnerAdapter$StorageSpinnerItem.<init> | REACHABLE SOURCE | PASS | FileManagerViewModel.java:367 (internal storage) and :380 (external loop) in getStorageList; def FileManagerSpinnerAdapter.java:57-62. |
| 16 | FileManagerViewModel.checkPermissions | REACHABLE SOURCE | PASS | Callers FileManagerViewModel.java:80 (ctor), :180, :190, :213, :257, :279, :292, :306/:308; def :347-358. |
| 21 | FileManagerViewModel.getBaseSdCardPath | REACHABLE SOURCE | PASS | FileManagerViewModel.java:305 in getExtSdCardPaths; def :320-327. |
| 26 | FileManagerViewModel.getSdCardDataPath | REACHABLE SOURCE | PASS | FileManagerViewModel.java:307 in getExtSdCardPaths fallback; def :329-336. |
| 31 | FileManagerViewModel.refreshCurDirectory | REACHABLE SOURCE | PASS | FileManagerDialog.java:461 (refreshDir) and :649 (reloadSpinner); def FileManagerViewModel.java:96-99. |
| 36 | FileManagerViewModelFactory.create | REACHABLE INFERRED | PASS | Reached from FileManagerDialog.java:140 `new ViewModelProvider(this, factory).get(FileManagerViewModel.class)`; def FileManagerViewModelFactory.java:45-51 (constructs the ViewModel :48); ViewModelProvider dispatch, not printed. |

## Totals

- PASS: 8 / FAIL: 0 (of 8 checked).
- Proposed corrections: none.
