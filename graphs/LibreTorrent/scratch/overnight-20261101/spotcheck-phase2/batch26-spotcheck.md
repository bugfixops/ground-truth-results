# LibreTorrent batch 26 — Phase 2 spot-check (UNVERIFIED spot-check, not a merge verdict)

- Source file checked: `~/workspace/overnight/stream-A/work/batch26-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. This file carries no dated 2026-11-01 Phase 1c revision note listing label changes, so no additional Phase 1 rows were added to the check set.
- D12 (owed Rx-error convention — NOT decided here): no row in this check set turns on D12. The D12 row in this batch, row 33 (interval error consumer, TorrentInfoProvider.java:337-338), is outside the check set and was NOT judged; it is left exactly as filed and flagged for the coordinator/merger. No sample row's verdict was changed on D12 grounds.
- Evidence base: already-fetched local files only — `~/workspace/b262728-src/` (TorrentEngine, TorrentEngineListener, TorrentInfoProvider, TorrentDownloadImpl, TorrentSessionImpl, DetailTorrentViewModel, DetailTorrentFragment, MainViewModel) and `~/workspace/ruleF-src/service/TorrentService.java`. No GitHub connector fetch was made, no 429 encountered, no file was missing.
- Build / sampler / C1: not run (not this task). No edit was made to the merge-ready file.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (re-derived) |
|---|---|---|---|---|
| 1 | TorrentEngine$5.onTorrentFinished(String) | REACHABLE / SOURCE | PASS | Override TorrentEngine.java:1306-1326; notify TorrentDownloadImpl.java:482-483 (`listener.onTorrentFinished(id)` in handleTorrentFinished), reached from the TORRENT_FINISHED alert case :231-232; registration TorrentEngine.java:140. |
| 6 | TorrentEngineListener.<init>() | REACHABLE / SOURCE | PASS | Abstract base TorrentEngineListener.java, 73 lines, all callbacks empty; instantiated as part of every printed anonymous `new TorrentEngineListener() {...}`, first via the engineListener field at TorrentEngine.java:1265, during TorrentEngine construction (getInstance called from TorrentService.onCreate:109). |
| 11 | TorrentEngineListener.onReadPiece(String,ReadPieceInfo) | REACHABLE / SOURCE | PASS | Notify TorrentDownloadImpl.java:452-453 (`listener.onReadPiece(id, info)` in handleReadPiece); base runs via torrentTaskListener dispatch as the file explains. |
| 16 | TorrentEngineListener.onSessionStopped() | REACHABLE / SOURCE | PASS | Notify TorrentSessionImpl.java:1043 (`notifyListeners(TorrentEngineListener::onSessionStopped)` in onAfterStop); the file's routing note (torrentTaskListener removed in onBeforeStop, so this runs through engineListener, which does not override it) matches the printed removeListener/onAfterStop sequence. |
| 21 | TorrentEngineListener.onTorrentMetadataLoaded(String,Exception) | REACHABLE / SOURCE | PASS | Notify TorrentDownloadImpl.java:438-439; base runs via torrentTaskListener (engineListener overrides this one, as the file notes). |
| 26 | TorrentEngineListener.onTorrentResumed(String) | REACHABLE / SOURCE | PASS | Notify TorrentDownloadImpl.java:244-245 (`listener.onTorrentResumed(id)` in the TORRENT_RESUMED case). |
| 31 | TorrentInfoProvider.getInstance(Context) | REACHABLE / SOURCE | PASS | Def TorrentInfoProvider.java:76-87; called from MainViewModel constructor (`TorrentInfoProvider.getInstance(application)`) and TorrentService.onCreate:110. The other overload (:63-74) is not a batch-26 row and was not judged. |
| 36 | TorrentInfoProvider.lambda$makeInfoFlowable$0(String,AtomicReference,FlowableEmitter,String) | REACHABLE / INFERRED | PASS | handleEvent Consumer in makeInfoFlowable, TorrentInfoProvider.java:134-145, invoked from the $1 listener overrides (:153, :164, :175, :186, :197 region); makeInfoFlowable called by observeInfo :94-95 ← DetailTorrentViewModel.observeTorrentInfo :167-168 ← DetailTorrentFragment.subscribeTorrentInfo :251 (called from onStart :228). Rx dispatch unprinted, hence INFERRED. |

## Totals

- PASS: 8 / 8. FAIL: 0.
- Proposed corrections: none. D12 flag (not a correction): batch 26 row 33 remains D12-owed and unjudged by this spot-check.
