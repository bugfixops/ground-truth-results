# Batch 23 source audit

Membership is the 40 rows in `batch_023_plan.txt`. Printed source excerpts and callers are in `batch_023_helper_printed.txt`.

The helper identified 11 direct source caller paths, but none has a complete hand-authored entry path in graph_def.py. The other 29 depend on Rx, session/listener, libtorrent, or inbound HTTP dispatch. All 40 remain OPEN. No graph edit or build was needed; no coverage evidence was used.

| Method | Label | Reason / printed evidence |
|---|---|---|
| `TorrentEngine.getDownloadSpeedLimit(String)` | OPEN | ViewModel caller exists; entry route not handwritten. `DetailTorrentViewModel.java:377-379`; `TorrentEngine.java:894-903`. |
| `TorrentEngine.getEncryptInConnectionsMode` | OPEN | Only settings observer caller depends on Rx delivery. `TorrentEngine.java:1535-1538,240-242`. |
| `TorrentEngine.getEncryptOutConnectionsMode` | OPEN | Only settings observer caller depends on Rx delivery. `TorrentEngine.java:1540-1543,240-242`. |
| `TorrentEngine.getInstance(Context)` | OPEN | Source call sites exist; complete app entry path not handwritten. `TorrentEngine.java:117-141`; service caller in helper print. |
| `TorrentEngine.getPieceSizeList` | OPEN | CreateTorrentViewModel caller exists; UI entry path not handwritten. `CreateTorrentViewModel.java:138,335`; `TorrentEngine.java:949-951`. |
| `TorrentEngine.getPieces(String)` | OPEN | Provider caller exists; complete provider entry path not handwritten. `TorrentInfoProvider.java:429,442`; `TorrentEngine.java:641-650`. |
| `TorrentEngine.getSessionLogger` | OPEN | Log UI/worker callers exist; complete routes not handwritten. `LogViewModel.java` and `SaveLogWorker.java` call sites in helper print. |
| `TorrentEngine.getStream(String,int)` | OPEN | Inbound server request path; callback route remains OPEN. `TorrentStreamServer.java:136-145`. |
| `TorrentEngine.getTorrentInputStream(TorrentStream)` | OPEN | Inbound server request path; callback route remains OPEN. `TorrentStreamServer.java:206-209,243-248`. |
| `TorrentEngine.getTorrentMetaInfo(String)` | OPEN | Engine/provider callers exist; complete entry route not handwritten. `TorrentEngine.java:588-639`. |
| `TorrentEngine.getTorrentVersionList` | OPEN | CreateTorrentViewModel caller exists; UI entry path not handwritten. `CreateTorrentViewModel.java:145,339`; `TorrentEngine.java:953-955`. |
| `TorrentEngine.getUploadSpeedLimit(String)` | OPEN | ViewModel caller exists; entry route not handwritten. `DetailTorrentViewModel.java:373-375`; `TorrentEngine.java:883-892`. |
| `TorrentEngine.handleAddTorrentError(String,Throwable)` | OPEN | Called from Rx work bodies; subscription execution not confirmed. `TorrentEngine.java:329-357,374-394`. |
| `TorrentEngine.handleAutoStop` | OPEN | Registered as Rx completion callback; delivery not confirmed. `TorrentEngine.java:243-251`. |
| `TorrentEngine.handleOnSessionStarted` | OPEN | Depends on session startup callback delivery. `TorrentService.java:130-131`; `TorrentSessionImpl.java:1006-1009`. |
| `TorrentEngine.handleSettingsChanged(String)` | OPEN | Registered Rx settings observer; delivery not confirmed. `TorrentEngine.java:240-242`. |
| `TorrentEngine.isFirstLastPiecePriority(String)` | OPEN | ViewModel caller exists; UI entry path not handwritten. `DetailTorrentViewModel.java:439-440`; `TorrentEngine.java:721-732`. |
| `TorrentEngine.isRunning` | OPEN | App call sites exist; complete source entry paths not handwritten. `FeedDownloaderWorker.java:197-201`; `TorrentEngine.java:303-305`. |
| `TorrentEngine.isSequentialDownload(String)` | OPEN | ViewModel caller exists; UI entry path not handwritten. `DetailTorrentViewModel.java:439-440`; `TorrentEngine.java:938-947`. |
| `TorrentEngine.lambda$addTorrentCompletable$10(Uri,Uri)` | OPEN | Rx Completable body; execution depends on Rx subscription. `TorrentEngine.java:374-394`. |
| `TorrentEngine.lambda$addTorrents$9(boolean,AddTorrentParams)` | OPEN | Rx consumer; delivery depends on external Rx. `TorrentEngine.java:342-357`. |
| `TorrentEngine.lambda$createFetchMagnetSingle$11(TorrentEngineListener)` | OPEN | Disposal action; disposal route not verified. `TorrentEngine.java:431-458`. |
| `TorrentEngine.lambda$createFetchMagnetSingle$12(String,SingleEmitter)` | OPEN | Rx Single source body; execution depends on subscription. `TorrentEngine.java:431-458`. |
| `TorrentEngine.lambda$deleteTorrents$16(boolean,String)` | OPEN | Rx consumer; delivery depends on external Rx. `TorrentEngine.java:533-541`. |
| `TorrentEngine.lambda$doStart$5(Throwable)` | OPEN | Rx error callback; callback delivery not confirmed. `TorrentEngine.java:243-251`. |
| `TorrentEngine.lambda$doStart$6(Logger.DataSetChange)` | OPEN | Rx logger consumer; delivery not confirmed. `TorrentEngine.java:253-257`. |
| `TorrentEngine.lambda$forceAnnounceTorrents$15(String)` | OPEN | Rx consumer; delivery depends on external Rx. `TorrentEngine.java:520-530`. |
| `TorrentEngine.lambda$forceRecheckTorrents$14(String)` | OPEN | Rx consumer; delivery depends on external Rx. `TorrentEngine.java:507-517`. |
| `TorrentEngine.lambda$loadTorrents$26` | OPEN | Rx Completable body; execution depends on subscription. `TorrentEngine.java:1085-1092`. |
| `TorrentEngine.lambda$observeEngineRunning$3(TorrentEngineListener)` | OPEN | Disposal cleanup action; disposal route not verified. `TorrentEngine.java:202-227`. |
| `TorrentEngine.lambda$observeEngineRunning$4(FlowableEmitter)` | OPEN | Rx Flowable source; execution depends on subscription. `TorrentEngine.java:202-227`. |
| `TorrentEngine.lambda$observeNeedStartEngine$0(FlowableEmitter)` | OPEN | Rx Flowable source; execution depends on subscription. `TorrentEngine.java:161-200`. |
| `TorrentEngine.lambda$observeNeedStartEngine$1(FlowableEmitter,Runnable,Boolean)` | OPEN | Rx subscriber; delivery not confirmed. `TorrentEngine.java:182-197`. |
| `TorrentEngine.lambda$observeNeedStartEngine$2(FlowableEmitter)` | OPEN | Polling executor path depends on Rx subscription and state. `TorrentEngine.java:161-191`. |
| `TorrentEngine.lambda$observeTorrentMetaInfo$17(TorrentEngineListener)` | OPEN | Disposal cleanup action; disposal route not verified. `TorrentEngine.java:588-618`. |
| `TorrentEngine.lambda$observeTorrentMetaInfo$18(String,FlowableEmitter)` | OPEN | Rx Flowable source; execution depends on subscription. `TorrentEngine.java:588-618`. |
| `TorrentEngine.lambda$pauseAll$19` | OPEN | Rx Completable body; execution depends on subscription. `TorrentEngine.java:652-659`. |
| `TorrentEngine.lambda$pauseResumeTorrent$13(String)` | OPEN | Rx Completable body; execution depends on subscription. `TorrentEngine.java:488-505`. |
| `TorrentEngine.lambda$prioritizeFiles$25(String,Priority[])` | OPEN | Async/Rx work body; execution depends on subscription. `TorrentEngine.java:734-746`. |
| `TorrentEngine.lambda$rescheduleTorrents$7` | OPEN | Rx Completable body; execution depends on subscription. `TorrentEngine.java:315-327`. |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used.
