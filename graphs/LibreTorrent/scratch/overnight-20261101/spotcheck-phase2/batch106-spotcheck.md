# LibreTorrent batch 106 — Phase 2 spot-check — UNVERIFIED spot-check, NOT a merge

- Batch: 106. Source checked: already-fetched local copies in ~/workspace/b105-106-src/; no connector fetch needed, no 429.
- Rows checked (9): samples 1, 6, 11, 16, 21, 26, 31, 36 PLUS row 40 (left OPEN).
- Build/sampler/C1: not run (not this task). No edit made to the merge-ready file. No convention decided. Per task instruction, rows 12-39 were verified as filed under the adopted D2 variant (no downstream propagation): LogActivity's own start is printed (MainActivity menu → showLog, batches 107-108 lead), and no strict launcher-entry revert was re-imposed on samples 16, 21, 26, 31, 36.

## Per-row verdicts

| # | Method | Filed label | Verdict | Evidence (printed source) |
|---|---|---|---|---|
| 1 | LogActivity.showFabDown | REACHABLE SOURCE | PASS | LogActivity.java:349 and :367 scroll callbacks call showFabDown; def :421-426. |
| 6 | LogActivity.updateToolbarSubtitle | REACHABLE SOURCE | PASS | LogActivity.java:102 (onCreate) and :440 (handleUpdateAdapter); def :443-450. |
| 11 | LogActivity$2.onScrolled | REACHABLE INFERRED | PASS | Def LogActivity.java:343-356 (hide/show fabs on dy direction); RecyclerView dispatch, not printed. |
| 16 | LogAdapter$1.<init> | REACHABLE INFERRED | PASS | Anonymous DiffUtil.ItemCallback, static field LogAdapter.java:67; class initialisation runs when the adapter class is first used (`new LogAdapter(this)`, LogActivity.java:116). INFERRED, as filed. |
| 21 | LogAdapter$ViewHolder.lambda$bind$0 | REACHABLE INFERRED | PASS | Click listener LogAdapter.java:102-105 calls listener.onItemClicked(entry); View-click dispatch, not printed. |
| 26 | LogDataSource.loadRange | REACHABLE INFERRED | PASS | Def LogDataSource.java:93-117; Paging dispatch via LogSourceFactory.java:41 `new LogDataSource(logger)` and LogViewModel.java:75 sourceFactory; framework dispatch, not printed. |
| 31 | LogMutableParams.isLogSessionFilter | REACHABLE SOURCE | PASS | LogViewModel.java:122 paramsCallback calls isLogSessionFilter; def LogMutableParams.java:49-52. Anchor chain: LogViewModel.java:56 `mutableParams = new LogMutableParams()`, via LogActivity.java:92 ViewModelProvider. |
| 36 | LogMutableParams.setLogPortmapFilter | REACHABLE SOURCE | PASS | LogViewModel.java:86 initMutableParams calls setLogPortmapFilter; def LogMutableParams.java:90-94. Same anchor chain as row 31. |
| 40 | LogMutableParams.toString | OPEN — | PASS | Def LogMutableParams.java:110-120. No receiver-typed caller in the printed files; the only log-package toString nearby is LogViewModel.java:222 `entry.toString()` (a LogEntry, not LogMutableParams). Correctly left OPEN — not flipped to UNREACHABLE without a saved full-repo grep, as filed. |

## Totals

- PASS: 9 / FAIL: 0 (of 9 checked).
- Proposed corrections: none.
