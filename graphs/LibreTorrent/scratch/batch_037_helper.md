# Batch 37 helper report

Membership is exactly the 40 rows with `batch==37` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; that file is the sole membership source. Definitions, call sites, and callback contexts are described in `scratch/batch_037_helper_printed.txt`. Local calls and captured lambdas are present, but this bounded review did not verify complete routes from an app entry point. Uncertain rows remain OPEN.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `TorrentDownloadImpl.isPaused(TorrentStatus)` | OPEN | — | Private status helper is called by isPaused/status conversion; entry route not established. | `TorrentDownloadImpl.java:1392-1401,1351-1358` |
| `TorrentDownloadImpl.isSeeding` | OPEN | — | Called internally and exposed through TorrentDownload; complete entry route not established. | `TorrentDownloadImpl.java:1403-1407`; usage search |
| `TorrentDownloadImpl.isSequentialDownload` | OPEN | — | Engine queries this method, but full app-entry route is not recorded. | `TorrentDownloadImpl.java:1421-1425`; `TorrentEngine.java:938-946` |
| `TorrentDownloadImpl.isStopped` | OPEN | — | Definition read; complete caller route not established. | `TorrentDownloadImpl.java:1635-1639`; usage search |
| `TorrentDownloadImpl.isValid` | OPEN | — | Definition read; complete caller route not established. | `TorrentDownloadImpl.java:1629-1634`; usage search |
| `TorrentDownloadImpl.lambda$checkError$1` | OPEN | — | Captured listener callback in checkError; invocation depends on notifyListeners route, not fully traced. | `TorrentDownloadImpl.java:302-336` |
| `TorrentDownloadImpl.lambda$handleMetadata$2` | OPEN | — | Captured callback in metadata error handling; full alert-to-callback entry route not established. | `TorrentDownloadImpl.java:391-440` |
| `TorrentDownloadImpl.lambda$handleMetadata$3` | OPEN | — | Captured callback in metadata notification; full alert-to-callback entry route not established. | `TorrentDownloadImpl.java:391-440` |
| `TorrentDownloadImpl.lambda$handleReadPiece$4` | OPEN | — | Captured callback in read-piece listener notification; complete stream alert route not established. | `TorrentDownloadImpl.java:442-454` |
| `TorrentDownloadImpl.lambda$handleTorrentFinished$6` | OPEN | — | Captured listener callback; full alert registration and route not established. | `TorrentDownloadImpl.java:478-485` |
| `TorrentDownloadImpl.lambda$onStorageMoved$0` | OPEN | — | Captured listener callback; full alert registration and route not established. | `TorrentDownloadImpl.java:250-255,284-290` |
| `TorrentDownloadImpl.lambda$requestStop$7` | OPEN | — | Captured Rx state callback; stop request entry route is not fully traced. | `TorrentDownloadImpl.java:537-573` |
| `TorrentDownloadImpl.lambda$requestStop$8` | OPEN | — | Captured Rx error callback; stop request entry route is not fully traced. | `TorrentDownloadImpl.java:537-573` |
| `TorrentDownloadImpl.lambda$requestStop$9` | OPEN | — | Captured Completable creation callback; stop request entry route is not fully traced. | `TorrentDownloadImpl.java:537-573` |
| `TorrentDownloadImpl.lambda$setDownloadPath$10` | OPEN | — | Captured listener callback in path update; complete entry route not established. | `TorrentDownloadImpl.java:1215-1237` |
| `TorrentDownloadImpl.lambda$torrentRemoved$5` | OPEN | — | Captured listener callback in removal handling; complete alert route not established. | `TorrentDownloadImpl.java:234-236,456-470` |
| `TorrentDownloadImpl.makeMagnet` | OPEN | — | Called through TorrentEngine and DetailTorrentViewModel; complete app-entry route not recorded. | `TorrentDownloadImpl.java:1006-1021`; `TorrentEngine.java:577-585`; `DetailTorrentViewModel.java:381-382` |
| `TorrentDownloadImpl.notifyListeners` | OPEN | — | Private dispatch helper used by multiple callbacks; complete entry route not recorded. | `TorrentDownloadImpl.java:182-193`; call sites in `205-485` |
| `TorrentDownloadImpl.onStorageMoved` | OPEN | — | Inner alert listener dispatches here; complete framework/library alert route not traced. | `TorrentDownloadImpl.java:250-255,284-290` |
| `TorrentDownloadImpl.operationNotAllowed` | OPEN | — | Widely called helper; complete entry route to any individual target remains unverified. | `TorrentDownloadImpl.java:195-203`; method usages |
| `TorrentDownloadImpl.pause` | OPEN | — | Public interface method calls doPause; complete app-entry route not recorded. | `TorrentDownloadImpl.java:593-600`; interface/source use search |
| `TorrentDownloadImpl.pauseManually` | OPEN | — | Called from TorrentSessionImpl; complete app-entry route not recorded. | `TorrentDownloadImpl.java:616-629`; `TorrentSessionImpl.java:564,790` |
| `TorrentDownloadImpl.pieces` | OPEN | — | Definition read; complete app-entry route not established. | `TorrentDownloadImpl.java:993-1004`; usage search |
| `TorrentDownloadImpl.prioritizeFiles` | OPEN | — | Definition and internal priority logic read; complete app-entry route not recorded. | `TorrentDownloadImpl.java:716-742`; usage search |
| `TorrentDownloadImpl.readPiece` | OPEN | — | Called by TorrentInputStream; complete stream construction and app-entry route not traced. | `TorrentDownloadImpl.java:1559-1565`; `TorrentInputStream.java:242,338` |
| `TorrentDownloadImpl.remove` | OPEN | — | Definition read; complete caller route not established. | `TorrentDownloadImpl.java:773-787`; usage search |
| `TorrentDownloadImpl.replaceTrackers` | OPEN | — | Definition read; full caller route not established. | `TorrentDownloadImpl.java:961-975`; usage search |
| `TorrentDownloadImpl.requestStop` | OPEN | — | Called as part of session stop orchestration; complete app-entry route not recorded. | `TorrentDownloadImpl.java:537-573`; `TorrentSessionImpl.java:911` |
| `TorrentDownloadImpl.requestTrackerAnnounce` | OPEN | — | Definition read; complete caller route not established. | `TorrentDownloadImpl.java:872-878`; usage search |
| `TorrentDownloadImpl.resetTorrentError` | OPEN | — | Called from resumed alert handling; complete alert route not established. | `TorrentDownloadImpl.java:237-246,292-300` |
| `TorrentDownloadImpl.resume` | OPEN | — | Public method includes auto/manual state check; complete caller route not recorded. | `TorrentDownloadImpl.java:602-613`; interface/source use search |
| `TorrentDownloadImpl.resumeManually` | OPEN | — | Called from TorrentSessionImpl; complete app-entry route not recorded. | `TorrentDownloadImpl.java:632-645`; `TorrentSessionImpl.java:566,803` |
| `TorrentDownloadImpl.saveResumeData` | OPEN | — | Multiple internal callers exist, but complete app-entry route not traced. | `TorrentDownloadImpl.java:247-269,492-514` |
| `TorrentDownloadImpl.serializeResumeData` | OPEN | — | Inner alert dispatch calls it; full alert route not established. | `TorrentDownloadImpl.java:247-249,516-528` |
| `TorrentDownloadImpl.setAutoManaged` | OPEN | — | Definition read; complete app-entry route not established. | `TorrentDownloadImpl.java:675-687`; usage search |
| `TorrentDownloadImpl.setDownloadPath` | OPEN | — | Definition read; complete caller route not established. | `TorrentDownloadImpl.java:1215-1237`; usage search |
| `TorrentDownloadImpl.setDownloadSpeedLimit` | OPEN | — | Definition read; complete caller route not established. | `TorrentDownloadImpl.java:1308-1318`; usage search |
| `TorrentDownloadImpl.setFirstLastPiecePriority` | OPEN | — | Definition and helper call read; complete app-entry route not recorded. | `TorrentDownloadImpl.java:1084-1102` |
| `TorrentDownloadImpl.setInterestedPieces` | OPEN | — | Called by TorrentInputStream; complete stream entry route not traced. | `TorrentDownloadImpl.java:1573-1604`; `TorrentInputStream.java:118,217,288,394` |
| `TorrentDownloadImpl.setMaxConnections` | OPEN | — | Definition read; complete app-entry route not established. | `TorrentDownloadImpl.java:1428-1433`; usage search |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
