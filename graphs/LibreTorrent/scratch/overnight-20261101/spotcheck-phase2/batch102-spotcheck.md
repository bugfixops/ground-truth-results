# LibreTorrent batch 102 — Phase 2 spot-check — UNVERIFIED spot-check, NOT a merge

- Batch: 102. Source checked: already-fetched local copies in ~/workspace/b101102-src/ plus saved grep ~/workspace/overnight/stream-A/greps/grep_recheck_selectable_setfilename_complete.txt; no connector fetch needed, no 429.
- Rows checked (10): samples 1, 6, 11, 16, 21, 26, 31, 36 PLUS Phase-1c-changed row 17 (D5c REACHABLE → OPEN) and round-2/grep-flip row 13 (OPEN → UNREACHABLE).
- Build/sampler/C1: not run (not this task). No edit made to the merge-ready file. No convention decided.

## Per-row verdicts

| # | Method | Filed label | Verdict | Evidence (printed source) |
|---|---|---|---|---|
| 1 | FileManagerAdapter.onCreateViewHolder | REACHABLE INFERRED | PASS | Body FileManagerAdapter.java:74-79 (`new ViewHolder(v)` :78); adapter set at FileManagerDialog.java:197; RecyclerView dispatch, not printed. |
| 6 | FileManagerAdapter$ViewHolder.<init> | REACHABLE SOURCE | PASS | FileManagerAdapter.java:78 `new ViewHolder(v)`; def :118-124. |
| 11 | FileManagerConfig.<init>(String,String,int) | REACHABLE SOURCE | PASS | CreateTorrentDialog.java:259-263 (FILE_CHOOSER_MODE), :269-273 (DIR_CHOOSER_MODE), :328-334 (SAVE_FILE_MODE) `new FileManagerConfig(...)` + putExtra + launcher; def FileManagerConfig.java:48-53. |
| 13 | FileManagerConfig.setFileName | UNREACHABLE SOURCE | PASS | Def FileManagerConfig.java:67-71 only. Saved complete-tree grep: F2 `.setFileName(` call sites = zero (exit=1); only the definition and unrelated setFileNameFilter (CreateTorrentViewModel.java:198, TorrentBuilder.java:155); F3 method references = zero. Direct-field bypass corroborated (FeedActivity assigns config.fileName directly). UNREACHABLE on the saved-grep standard, as filed; reverts to OPEN only if the merger rejects that grep standard (recorded in the merge-ready file, not re-decided here). |
| 16 | FileManagerConfig$1.createFromParcel | REACHABLE INFERRED | PASS | Body FileManagerConfig.java:96-99; Parcelable dispatch when FileManagerDialog reads the extra at FileManagerDialog.java:137 (`getParcelableExtra(TAG_CONFIG)`). |
| 17 | FileManagerConfig$1.newArray | OPEN — | PASS | Def FileManagerConfig.java:102-105. D5c array-site requirement correctly applied: corpus grep finds no FileManagerConfig array site (no `new FileManagerConfig[`, no createTypedArray/newArray call for this type; other classes' newArray definitions are unrelated). The printed round trip parcels single objects only (putExtra at CreateTorrentDialog :263/:273/:334; getParcelableExtra at FileManagerDialog :137), which calls createFromParcel, never newArray. OPEN is correct — neither REACHABLE nor UNREACHABLE is claimed. |
| 21 | FileManagerDialog.createFile | REACHABLE SOURCE | PASS | FileManagerDialog.java:348 `createFile(true)` and :508 `createFile(false)`; def :570-591. |
| 26 | FileManagerDialog.lambda$onCreate$0 | REACHABLE INFERRED | PASS | FileManagerDialog.java:172 FAB click lambda `setOnClickListener((v) -> showInputNameDialog())`; View dispatch, not printed. |
| 31 | FileManagerDialog.onDestroy | REACHABLE INFERRED | PASS | Body FileManagerDialog.java:259-262 (unregisterMediaReceiver); Activity lifecycle dispatch, not printed. |
| 36 | FileManagerDialog.onRestoreInstanceState | REACHABLE INFERRED | PASS | Body FileManagerDialog.java:415-419 (restores filesListState saved :405-411); Activity lifecycle dispatch, not printed. |

## Totals

- PASS: 10 / FAIL: 0 (of 10 checked).
- Proposed corrections: none.
