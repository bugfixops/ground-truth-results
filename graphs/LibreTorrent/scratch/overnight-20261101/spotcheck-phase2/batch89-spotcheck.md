# LibreTorrent batch 89 — Phase 2 spot-check — UNVERIFIED (spot-check only, not a merge verdict)

- Batch: 89. Work file checked: `~/workspace/overnight/stream-A/work/batch89-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. No dated 2026-11-01 revision note in this file lists a Phase 1 label flip, so no extra rows were due.
- Method: re-derived from already-fetched source on disk (`~/workspace/b89-90-src/dvm_fresh.java`, `~/workspace/b89-90-src/DetailTorrentInfoFragment.java`, `~/workspace/b89-90-src/MsgDetailTorrentViewModel.java`, corroborated for Fragment lines by the fresh batch 87/88 print in `~/workspace/b8788-src/DetailTorrentFragment.java`); no GitHub connector fetch was needed, no 429 hit, no file missing.
- No edit was made to the merge-ready file. No push. Build/sampler/C1: not run (not this task).
- Strict-entry caveat: the launcher → DetailTorrentActivity → DetailTorrentFragment step was not printed in this pass; under a strict entry-route rule all rows would revert to OPEN. That convention is undecided and NOT decided here.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (file:line, local copy) |
|---|---|---|---|---|
| 1 | DetailTorrentViewModel.lambda$addTag$0 | REACHABLE / INFERRED | PASS | Runnable inside addTag DetailTorrentViewModel (dvm_fresh.java):151-152 (`Completable.fromRunnable(() -> repo.addTag(...))`); addTag subscribed by DetailTorrentInfoFragment selectTag callback :139-147. Rx dispatch → INFERRED correct. |
| 6 | DetailTorrentViewModel.lambda$startMakeFileTree$5 | REACHABLE / INFERRED | PASS | Subscribe lambda `() -> updateCurDir(fileTree)` in startMakeFileTree dvm_fresh.java:522-526; Rx dispatch → INFERRED correct. |
| 11 | DetailTorrentViewModel.observeAdvancedTorrentInfo | REACHABLE / SOURCE | PASS | Caller DetailTorrentFragment.java:271 (subscribeTorrentInfo, corroborated in the fresh b8788 print); def dvm_fresh.java:171-172. |
| 16 | DetailTorrentViewModel.observeTorrent | REACHABLE / SOURCE | PASS | Called inside observeTorrentInfoPair dvm_fresh.java:192 (`combineLatest(observeTorrent(), observeTorrentInfo(), ...)`), itself called by DetailTorrentFragment :265; def :175-176. |
| 21 | DetailTorrentViewModel.onCleared | REACHABLE / INFERRED | PASS | Def dvm_fresh.java:118-124 (disposable.clear, callback removal); invoked only by ViewModelStore lifecycle dispatch; ViewModel obtained via provider.get DetailTorrentFragment.java:163. |
| 26 | DetailTorrentViewModel.setTorrentId | REACHABLE / SOURCE | PASS | Caller DetailTorrentFragment.java:167 (onViewCreated, corroborated in the fresh b8788 print); def dvm_fresh.java:126-127. |
| 31 | DetailTorrentViewModel.updateFiles | REACHABLE / SOURCE | PASS | Called by infoCallback.onPropertyChanged dvm_fresh.java:473; def :570-596. |
| 36 | DetailTorrentViewModel$1.lambda$onPropertyChanged$0 | REACHABLE / INFERRED | PASS | Completable.fromRunnable lambda inside $1 (mutableParamsCallback).onPropertyChanged dvm_fresh.java:457-464 (setStorageFreeSpace / setDirName); Rx + databinding dispatch → INFERRED correct. |

## Totals

- PASS: 8 / 8. FAIL: 0 / 8.

## Proposed corrections

- None. No row label or confirmed_by needs changing on the evidence checked.
