# LibreTorrent batch 23 helper audit

Membership comes only from batch 23 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; its query printed exactly 40 rows. Printed target source and caller evidence are in `scratch/batch_023_helper_printed.txt`.

OPEN means the candidate route depends on Rx, libtorrent, a session listener, or an incoming server request whose execution was not established with source in this audit. No graph, notes, output, or coverage files were changed.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentEngine.getDownloadSpeedLimit(String)` | REACHABLE | `DetailTorrentViewModel` calls it (`DetailTorrentViewModel.java:377-379`); body queries the running torrent (`TorrentEngine.java:894-903`). |
| 2 | `TorrentEngine.getEncryptInConnectionsMode()` | OPEN | Called only by `handleSettingsChanged` (`TorrentEngine.java:1535-1538`), which is registered as a settings observer (`:240-242`); Rx dispatch route not confirmed. |
| 3 | `TorrentEngine.getEncryptOutConnectionsMode()` | OPEN | Called only by `handleSettingsChanged` (`TorrentEngine.java:1540-1543`), which is registered as a settings observer (`:240-242`); Rx dispatch route not confirmed. |
| 4 | `TorrentEngine.getInstance(Context)` | REACHABLE | App call sites include UI ViewModels, services, and stream server; the method constructs and returns the singleton (`TorrentEngine.java:117-141`). |
| 5 | `TorrentEngine.getPieceSizeList()` | REACHABLE | `CreateTorrentViewModel` reads it (`CreateTorrentViewModel.java:138,335`); body delegates to session (`TorrentEngine.java:949-951`). |
| 6 | `TorrentEngine.getPieces(String)` | REACHABLE | `TorrentInfoProvider` calls it while reading/updating piece info (`TorrentInfoProvider.java:429,442`); body is at `TorrentEngine.java:641-650`. |
| 7 | `TorrentEngine.getSessionLogger()` | REACHABLE | Log UI and `SaveLogWorker` call it (`LogViewModel.java:72,142,153,164,176,183`; `SaveLogWorker.java:86`); body delegates to the session (`TorrentEngine.java:957-959`). |
| 8 | `TorrentEngine.getStream(String,int)` | OPEN | `TorrentStreamServer.handleTorrent` calls it (`TorrentStreamServer.java:136-145`); this requires the HTTP request/server callback route. |
| 9 | `TorrentEngine.getTorrentInputStream(TorrentStream)` | OPEN | `TorrentStreamServer.handleTorrent` calls it on range/full stream paths (`TorrentStreamServer.java:206-209,243-248`); server request route remains open. |
| 10 | `TorrentEngine.getTorrentMetaInfo(String)` | REACHABLE | `observeTorrentMetaInfo` invokes it (`TorrentEngine.java:588-618`), and UI/provider callers also query metadata; body is at `:621-639`. |
| 11 | `TorrentEngine.getTorrentVersionList()` | REACHABLE | `CreateTorrentViewModel` uses it to validate and decode the selected version (`CreateTorrentViewModel.java:145,339`); body at `TorrentEngine.java:953-955`. |
| 12 | `TorrentEngine.getUploadSpeedLimit(String)` | REACHABLE | `DetailTorrentViewModel` calls it (`DetailTorrentViewModel.java:373-375`); body at `TorrentEngine.java:883-892`. |
| 13 | `TorrentEngine.handleAddTorrentError(String,Throwable)` | OPEN | Called in `addTorrent`, `addTorrents`, and `addTorrentCompletable` asynchronous work bodies (`TorrentEngine.java:329-357,374-394`); their Rx execution routes were not established. |
| 14 | `TorrentEngine.handleAutoStop()` | OPEN | Registered as a `downloadsCompleted.listen().subscribe` callback (`TorrentEngine.java:243-251`); Rx delivery not confirmed. |
| 15 | `TorrentEngine.handleOnSessionStarted()` | OPEN | App service calls `engine.doStart()` then registers `engineListener` (`TorrentService.java:130-131`); session `onAfterStart()` schedules `notifyListeners(TorrentEngineListener::onSessionStarted)` in an Rx `Completable` (`TorrentSessionImpl.java:1006-1009`). Delivery still depends on session start reaching this callback. |
| 16 | `TorrentEngine.handleSettingsChanged(String)` | OPEN | Registered with `pref.observeSettingsChanged().subscribe(this::handleSettingsChanged)` (`TorrentEngine.java:240-242`); Rx callback route not confirmed. |
| 17 | `TorrentEngine.isFirstLastPiecePriority(String)` | REACHABLE | `DetailTorrentViewModel` calls it (`DetailTorrentViewModel.java:439-440`); body queries the task (`TorrentEngine.java:721-732`). |
| 18 | `TorrentEngine.isRunning()` | REACHABLE | Called directly throughout app services and ViewModels (for example `FeedDownloaderWorker.java:197-201`); body delegates to session (`TorrentEngine.java:303-305`). |
| 19 | `TorrentEngine.isSequentialDownload(String)` | REACHABLE | `DetailTorrentViewModel` reads it (`DetailTorrentViewModel.java:439-440`); body queries the task (`TorrentEngine.java:938-947`). |
| 20 | `TorrentEngine.lambda$addTorrentCompletable$10(Uri,Uri)` | OPEN | Lambda is the body passed to `Completable.fromRunnable` (`TorrentEngine.java:374-394`); execution depends on Rx subscription. |
| 21 | `TorrentEngine.lambda$addTorrents$9(boolean,AddTorrentParams)` | OPEN | Lambda is the `Observable.subscribe` consumer (`TorrentEngine.java:342-357`); execution depends on Rx delivery. |
| 22 | `TorrentEngine.lambda$createFetchMagnetSingle$11(TorrentEngineListener)` | OPEN | Source corresponds to listener cleanup passed to `Disposables.fromAction` (`TorrentEngine.java:431-458`); disposal path not confirmed. |
| 23 | `TorrentEngine.lambda$createFetchMagnetSingle$12(String,SingleEmitter)` | OPEN | Source is the `Single.create` emitter body (`TorrentEngine.java:431-458`); execution depends on Rx subscription. |
| 24 | `TorrentEngine.lambda$deleteTorrents$16(boolean,String)` | OPEN | Lambda is the `Observable.subscribe` consumer (`TorrentEngine.java:533-541`); execution depends on Rx delivery. |
| 25 | `TorrentEngine.lambda$doStart$5(Throwable)` | OPEN | Error consumer registered in the completed-download subscription (`TorrentEngine.java:243-251`); error callback depends on Rx. |
| 26 | `TorrentEngine.lambda$doStart$6(Logger.DataSetChange)` | OPEN | Consumer registered for logger data changes (`TorrentEngine.java:253-257`); Rx delivery not confirmed. |
| 27 | `TorrentEngine.lambda$forceAnnounceTorrents$15(String)` | OPEN | Lambda is the `Observable.subscribe` consumer (`TorrentEngine.java:520-530`); execution depends on Rx delivery. |
| 28 | `TorrentEngine.lambda$forceRecheckTorrents$14(String)` | OPEN | Lambda is the `Observable.subscribe` consumer (`TorrentEngine.java:507-517`); execution depends on Rx delivery. |
| 29 | `TorrentEngine.lambda$loadTorrents$26()` | OPEN | Lambda is passed to `Completable.fromRunnable` (`TorrentEngine.java:1085-1092`); execution depends on Rx subscription. |
| 30 | `TorrentEngine.lambda$observeEngineRunning$3(TorrentEngineListener)` | OPEN | Lambda removes a listener through `Disposables.fromAction` (`TorrentEngine.java:202-227`); cleanup depends on disposal. |
| 31 | `TorrentEngine.lambda$observeEngineRunning$4(FlowableEmitter)` | OPEN | Lambda is the `Flowable.create` source (`TorrentEngine.java:202-227`); execution depends on Rx subscription. |
| 32 | `TorrentEngine.lambda$observeNeedStartEngine$0(FlowableEmitter)` | OPEN | Lambda is the `Flowable.create` source (`TorrentEngine.java:161-200`); execution depends on Rx subscription. |
| 33 | `TorrentEngine.lambda$observeNeedStartEngine$1(FlowableEmitter,Runnable,Boolean)` | OPEN | Lambda is the `observeEngineRunning().subscribe` consumer (`TorrentEngine.java:182-197`); execution depends on Rx delivery. |
| 34 | `TorrentEngine.lambda$observeNeedStartEngine$2(FlowableEmitter)` | OPEN | Lambda creates the polling `Runnable` (`TorrentEngine.java:161-180`); its execution is submitted to the executor (`:188-191`), but this path depends on Rx subscription and engine state. |
| 35 | `TorrentEngine.lambda$observeTorrentMetaInfo$17(TorrentEngineListener)` | OPEN | Lambda removes a metadata listener through `Disposables.fromAction` (`TorrentEngine.java:588-618`); cleanup depends on disposal. |
| 36 | `TorrentEngine.lambda$observeTorrentMetaInfo$18(String,FlowableEmitter)` | OPEN | Lambda is the `Flowable.create` source (`TorrentEngine.java:588-618`); execution depends on Rx subscription. |
| 37 | `TorrentEngine.lambda$pauseAll$19()` | OPEN | Lambda is passed to `Completable.fromRunnable` (`TorrentEngine.java:652-659`); execution depends on Rx subscription. |
| 38 | `TorrentEngine.lambda$pauseResumeTorrent$13(String)` | OPEN | Lambda is passed to `Completable.fromRunnable` (`TorrentEngine.java:488-505`); execution depends on Rx subscription. |
| 39 | `TorrentEngine.lambda$prioritizeFiles$25(String,Priority[])` | OPEN | Lambda is passed to asynchronous work in `prioritizeFiles` (`TorrentEngine.java:734-746`); execution depends on Rx subscription. |
| 40 | `TorrentEngine.lambda$rescheduleTorrents$7()` | OPEN | Lambda is passed to `Completable.fromRunnable` (`TorrentEngine.java:315-327`); execution depends on Rx subscription. |

Table totals: 40 rows = 11 REACHABLE, 0 UNREACHABLE, 29 OPEN. The OPEN items depend on callback delivery, Rx execution, session listener notification, or inbound HTTP handling that this audit did not independently verify.
