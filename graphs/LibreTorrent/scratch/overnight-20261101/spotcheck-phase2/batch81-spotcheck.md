# LibreTorrent batch 81 — Phase 2 spot-check — UNVERIFIED (spot-check only, not a merge verdict)

- Batch: 81. Work file checked: `~/workspace/overnight/stream-A/work/batch81-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. Phase 1c label flips in this file: 0 (stated in its 2026-11-01 Phase 1c revision note), so no extra rows were due.
- Method: re-derived from already-fetched source on disk (`~/workspace/b81-82-src/`); no GitHub connector fetch was needed, no 429 hit, no file missing.
- No edit was made to the merge-ready file. No push. Build/sampler/C1: not run (not this task).
- Strict-entry caveat: all REACHABLE rows below stand under the activity-anchored convention used by the file; under a strict printed-launcher rule they would revert to OPEN. That convention is undecided project-wide and is NOT decided here.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (file:line, local copy) |
|---|---|---|---|---|
| 1 | AddTorrentMutableParams.setStorageFreeSpace | REACHABLE / INFERRED | PASS | Def AddTorrentMutableParams.java:100-104; caller AddTorrentViewModel.java:357 `mutableParams.setStorageFreeSpace(...)` inside $2.onPropertyChanged, reached via data-binding Observable dispatch → INFERRED correct. |
| 6 | AddTorrentViewModel.<clinit> | REACHABLE / INFERRED | PASS | Non-constant TAG AddTorrentViewModel.java:79 (`class.getSimpleName()`); first use via `provider.get(AddTorrentViewModel.class)` AddTorrentActivity.java:104. JVM init → INFERRED correct. |
| 11 | AddTorrentViewModel.checkFreeSpace | REACHABLE / SOURCE | PASS | Called by addTorrent() AddTorrentViewModel.java:495; def :548-556. Direct internal call → SOURCE correct. |
| 16 | AddTorrentViewModel.getDecodeState | REACHABLE / SOURCE | PASS | Caller AddTorrentActivity.java:307 `viewModel.getDecodeState().observe(...)`; def AddTorrentViewModel.java:167-169. |
| 21 | AddTorrentViewModel.lambda$observeFetchedMetadata$3 | REACHABLE / INFERRED | PASS | Success callback AddTorrentViewModel.java:330-333 (info.set + FETCHING_MAGNET_COMPLETED); Rx dispatch unprinted → INFERRED correct. |
| 26 | AddTorrentViewModel.observeTags | REACHABLE / SOURCE | PASS | Caller AddTorrentInfoFragment.java:187 `viewModel.observeTags()` in subscribeTags(); def AddTorrentViewModel.java:153-155. |
| 31 | AddTorrentViewModel.startDecode | REACHABLE / SOURCE | PASS | Caller AddTorrentActivity.java:312 `viewModel.startDecode(uri)`; def AddTorrentViewModel.java:182-195. |
| 36 | AddTorrentViewModel$1.<init> | REACHABLE / SOURCE | PASS | Anonymous infoCallback field AddTorrentViewModel.java:337-346; field initialisers run inside <init> (:128-147), reached via AddTorrentActivity.java:103-104. |

## Totals

- PASS: 8 / 8. FAIL: 0 / 8.

## Proposed corrections

- None. No row label or confirmed_by needs changing on the evidence checked.
