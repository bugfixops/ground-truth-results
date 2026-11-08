# LibreTorrent batch 84 — Phase 2 spot-check — UNVERIFIED (spot-check only, not a merge verdict)

- Batch: 84. Work file checked: `~/workspace/overnight/stream-A/work/batch84-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (9): sample rows 1, 6, 11, 16, 21, 26, 31, 36, plus must-include row 40 (layout-resolved getter standing REACHABLE INFERRED, explicitly not moved by D4a). Phase 1c label flips in this file: 0 (stated in its 2026-11-01 Phase 1c revision note); the OPEN-closing passes also flipped 0 rows.
- Method: re-derived from already-fetched source on disk (`~/workspace/b83-src/`); no GitHub connector fetch was needed, no 429 hit, no file missing.
- No edit was made to the merge-ready file. No push. Build/sampler/C1: not run (not this task).
- Layout-resolved rows (26, 40) rest on the printed layout + inflate + setViewModel chain with generated binding code unprinted; if the merger requires a printed generated binding class, they revert to OPEN. That convention is undecided and NOT decided here.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (file:line, local copy) |
|---|---|---|---|---|
| 1 | CreateTorrentDialog$2.onTextChanged | REACHABLE / INFERRED | PASS | Second (webSeedUrls) TextWatcher registered CreateTorrentDialog.java:212; empty onTextChanged :217; framework dispatch unprinted → INFERRED correct. |
| 6 | CreateTorrentDialog$4.onItemSelected | REACHABLE / INFERRED | PASS | torrentVersion spinner listener registered CreateTorrentDialog.java:242; body :244-248 calls viewModel.setTorrentVersionIndex(...); spinner dispatch unprinted → INFERRED correct. |
| 11 | CreateTorrentMutableParams.getSavePath | REACHABLE / SOURCE | PASS | Called by CreateTorrentDialog.java:382 and CreateTorrentViewModel.java:182/:213/:230/:359/:361/:363; def CreateTorrentMutableParams.java:161-164. |
| 16 | CreateTorrentMutableParams.getTrackerUrls | REACHABLE / SOURCE | PASS | Called by CreateTorrentViewModel.java:268 (getAndValidateTrackers); def CreateTorrentMutableParams.java:77-80. |
| 21 | CreateTorrentMutableParams.setPieceSizeIndex | REACHABLE / SOURCE | PASS | Called by CreateTorrentViewModel.java:141 (setPiecesSizeIndex), itself called by $3.onItemSelected Dialog:233; def CreateTorrentMutableParams.java:106-110. |
| 26 | CreateTorrentMutableParams.setStartSeeding | REACHABLE / INFERRED | PASS | Two-way binding dialog_create_torrent.xml:113 `android:checked="@={viewModel.mutableParams.startSeeding}"`, via Dialog:185 inflate + :187 setViewModel; generated binding unprinted → INFERRED correct. |
| 31 | CreateTorrentViewModel.<clinit> | REACHABLE / INFERRED | PASS | Non-constant TAG CreateTorrentViewModel.java:57 (`class.getSimpleName()`); first use via `provider.get(CreateTorrentViewModel.class)` CreateTorrentDialog.java:178. |
| 36 | CreateTorrentViewModel.downloadTorrent | REACHABLE / SOURCE | PASS | Called by CreateTorrentDialog.java:391 (handleFinish); def CreateTorrentViewModel.java:352-384. |
| 40 | CreateTorrentViewModel.getBuildProgress | REACHABLE / INFERRED | PASS | One-way binding dialog_create_torrent.xml:36 `android:progress="@{viewModel.buildProgress.intValue()}"`, via Dialog:185 inflate + :187 setViewModel; resolves through getBuildProgress() CreateTorrentViewModel.java:131-134; generated binding unprinted → INFERRED correct. Standing REACHABLE INFERRED, not moved by D4a, as filed. |

## Totals

- PASS: 9 / 9. FAIL: 0 / 9.

## Proposed corrections

- None for any row label or confirmed_by. Trivial prose note only (not a row correction): the file's Changes prose says "Dialog:186-188" for the inflate/setViewModel chain, while the row citations correctly give :185 inflate + :187 setViewModel, verified in the local Dialog copy. No row citation needs changing.
