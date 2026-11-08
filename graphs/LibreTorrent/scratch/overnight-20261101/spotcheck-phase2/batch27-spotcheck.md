# LibreTorrent batch 27 — Phase 2 spot-check (UNVERIFIED spot-check, not a merge verdict)

- Source file checked: `~/workspace/overnight/stream-A/work/batch27-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. This file carries no dated 2026-11-01 Phase 1c revision note listing label changes, so no additional Phase 1 rows were added to the check set.
- D12 (owed Rx-error convention — NOT decided here): row 21 in this check set turns on D12 (see its row below). It is re-derived as filed and left unchanged; no D12 decision is made by this spot-check.
- Evidence base: already-fetched local files only — `~/workspace/b262728-src/` (TorrentInfoProvider, DetailTorrentViewModel, MainViewModel, MainActivity) and local fragment copies for the fragment → ViewModel step (flagged as local-only in the merge-ready file itself). No GitHub connector fetch was made, no 429 encountered, no file was missing.
- Build / sampler / C1: not run (not this task). No edit was made to the merge-ready file.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (re-derived) |
|---|---|---|---|---|
| 1 | TorrentInfoProvider.lambda$makeInfoListFlowable$5(AtomicReference,FlowableEmitter) | REACHABLE / INFERRED | PASS | handleInfo Runnable in makeInfoListFlowable, TorrentInfoProvider.java:242-252 (engine.makeInfoListSync() + emit on change); invoked by the $2 listener callbacks (:258, :263, :268, :273, :278, :283 region — onTorrentStateChanged/onTorrentPaused/onTorrentRemoved/onRestoreSessionError/onTorrentError/onSessionStats, each calling handleInfo.run()) and the tag-repo consumer; route via observeInfoList :98-99 ← MainViewModel. Rx dispatch unprinted, hence INFERRED. |
| 6 | TorrentInfoProvider.lambda$makeInfoListSingle$10(SingleEmitter) | REACHABLE / INFERRED | PASS | Single.create body, TorrentInfoProvider.java:311-320 (inner Thread body is the distinct row-7 lambda; both run on the same subscription route, so a swap would not change either label, as the file notes). Route via getInfoListSingle :102-103. |
| 11 | TorrentInfoProvider.lambda$makePeersInfoFlowable$23(String,FlowableEmitter) | REACHABLE / INFERRED | PASS | Flowable.create body of makePeersInfoFlowable, TorrentInfoProvider.java:391-421; route via observePeersInfo :114-115 ← DetailTorrentViewModel.observePeers :183-184. |
| 16 | TorrentInfoProvider.lambda$makeSessionStatsFlowable$30(TorrentEngineListener) | REACHABLE / INFERRED | PASS | Disposables.fromAction dispose action, TorrentInfoProvider.java:492-493 (`engine.removeListener(listener)`); route via makeSessionStatsFlowable :474 ← observeSessionStats :126-127 ← MainActivity.subscribeSessionStats :456-460. |
| 21 | TorrentInfoProvider.lambda$makeTrackersInfoFlowable$17(String,Throwable) | REACHABLE / INFERRED | PASS (D12-flagged, unchanged) | Interval error consumer, TorrentInfoProvider.java:373-374 (`Log.e` on error, inside makeTrackersInfoFlowable's Observable.interval subscription :362ff). It runs only if the interval source errors. D12 flag: under the undecided Rx-error convention this row's verdict turns on whether an observed error trigger is required; this spot-check does NOT decide D12 and leaves the filed REACHABLE (via the printed subscription route) exactly as-is. |
| 26 | TorrentInfoProvider.makeInfoListFlowable() | REACHABLE / SOURCE | PASS | Def TorrentInfoProvider.java:238-308; called by observeInfoList :98-99. |
| 31 | TorrentInfoProvider.makeTorrentsDeletedFlowable() | REACHABLE / SOURCE | PASS | Def TorrentInfoProvider.java:455-472; called by observeTorrentsDeleted :122-123. |
| 36 | TorrentInfoProvider.observePeersInfo(String) | REACHABLE / SOURCE | PASS | Def TorrentInfoProvider.java:114-115 → makePeersInfoFlowable (row 28's method); called by DetailTorrentViewModel.observePeers :183-184. |

## Totals

- PASS: 8 / 8 (1 D12-flagged, row 21, left as filed). FAIL: 0.
- Proposed corrections: none. D12 decision on row 21 (and, by the same convention, the batch's other interval-error rows 9 and 13, which are outside this check set) is owed to the merger and is not made here.
