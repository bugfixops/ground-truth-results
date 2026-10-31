# LibreTorrent batch 25 helper audit

Membership is taken only from `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the plan contains exactly 40 batch 25 rows. Printed plan rows and source/call-site excerpts are in `scratch/batch_025_helper_printed.txt`.

I mark a row REACHABLE only where the printed app source establishes a route from an app entry or app-triggered construction. OPEN rows need a callback delivery, UI-to-ViewModel/data-binding path, or Rx/session/library dispatch that this pass did not independently close. No UNREACHABLE labels are inferred from absence of call sites.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentEngine.setTorrentName(String,String)` | OPEN | Body schedules work on Rx (`TorrentEngine.java:670-681`); `DetailTorrentViewModel.checkParamsChanged` calls it (`:478-490`), but the UI/data-binding path into that callback was not closed. |
| 2 | `TorrentEngine.setUploadSpeedLimit(String,int)` | OPEN | Body directly updates a running task (`TorrentEngine.java:916-925`); ViewModel call is at `DetailTorrentViewModel.java:393-396`, through the speed dialog (`DetailTorrentFragment.java:766-800`), but full dialog event wiring remains unverified. |
| 3 | `TorrentEngine.start()` | OPEN | App callers include Main and AddTorrent flows (`TorrentEngine.java:148-153` plus call-site search); the launcher subscription path uses Rx in `MainActivity.java:463-468`, so callback delivery is not SOURCE-closed here. |
| 4 | `TorrentEngine.startStreamingServer()` | OPEN | Called from `handleOnSessionStarted` and settings handling (`TorrentEngine.java:1046-1077,1592-1601`); both upstream callback dispatch routes need session/Rx delivery. |
| 5 | `TorrentEngine.startWatchDir()` | OPEN | Called from session-start and settings handling (`TorrentEngine.java:1046-1061,1581-1591`); session/Rx callback route not independently established. |
| 6 | `TorrentEngine.stopStreamingServer()` | OPEN | Called by `startStreamingServer` and settings handling (`TorrentEngine.java:1063-1083,1592-1601`); upstream paths depend on callbacks. |
| 7 | `TorrentEngine.stopWatchDir()` | OPEN | Called by settings handling and watch-dir restart (`TorrentEngine.java:1128-1135,1581-1591`); upstream path depends on settings callback delivery. |
| 8 | `TorrentEngine.switchConnectionReceiver()` | REACHABLE | `TorrentService.init` calls `engine.doStart()` (`TorrentService.java:130-131`), and `doStart` directly calls this method (`TorrentEngine.java:234-241`). |
| 9 | `TorrentEngine.switchPowerReceiver()` | REACHABLE | `TorrentService.init` calls `engine.doStart()` (`TorrentService.java:130-131`), and `doStart` directly calls this method (`TorrentEngine.java:234-241`). |
| 10 | `TorrentEngine$1.<init>(TorrentEngine,FlowableEmitter)` | OPEN | Anonymous listener is created inside `observeEngineRunning`'s `Flowable.create` (`TorrentEngine.java:202-227`); UI subscribers exist, but Rx source invocation is a library dispatch. |
| 11 | `TorrentEngine$1.onSessionStarted()` | OPEN | Listener callback forwards to an emitter (`TorrentEngine.java:207-212`); invocation depends on session listener notification. |
| 12 | `TorrentEngine$1.onSessionStopped()` | OPEN | Listener callback forwards to an emitter (`TorrentEngine.java:214-218`); invocation depends on session listener notification. |
| 13 | `TorrentEngine$2.<init>(TorrentEngine,String,SingleEmitter)` | OPEN | Listener is constructed in `createFetchMagnetSingle` (`TorrentEngine.java:431-458`); entry depends on magnet fetch subscription. |
| 14 | `TorrentEngine$2.onMagnetLoaded(String,byte[])` | OPEN | Callback belongs to the listener registered in `createFetchMagnetSingle` (`TorrentEngine.java:431-458`); session/library event dispatch was not closed. |
| 15 | `TorrentEngine$3.<init>(TorrentEngine,String,FlowableEmitter)` | OPEN | Listener is created inside `observeTorrentMetaInfo` (`TorrentEngine.java:588-618`); route depends on subscriber invoking the Rx source. |
| 16 | `TorrentEngine$3.onTorrentMetadataLoaded(String,Exception)` | OPEN | Callback is on the metadata listener registered in `observeTorrentMetaInfo` (`TorrentEngine.java:588-618`); session event dispatch is not independently confirmed. |
| 17 | `TorrentEngine$4.<init>(TorrentEngine,String,String)` | OPEN | Torrent file observer is created in the watch-directory path (`TorrentEngine.java:1116-1137`); parent setting/session callback path remains open. |
| 18 | `TorrentEngine$4.lambda$onEvent$0(Uri)` | OPEN | Lambda is the Rx completion callback from `addTorrentCompletable` (`TorrentEngine.java:1139-1161`); delivery depends on Rx subscription/completion. |
| 19 | `TorrentEngine$4.onEvent(int,String)` | OPEN | File observer callback body filters and adds a torrent (`TorrentEngine.java:1137-1163`); framework callback delivery and a watched-file event were not verified. |
| 20 | `TorrentEngine$5.<init>(TorrentEngine)` | REACHABLE | The `engineListener` anonymous object is initialized as a `TorrentEngine` field and registered with the session in its constructor (`TorrentEngine.java:130-141,1265-1270`). |
| 21 | `TorrentEngine$5.lambda$onIpFilterParsed$8(int)` | OPEN | Lambda is created in the listener callback (`TorrentEngine.java:1372-1381`); execution depends on the session callback being invoked. |
| 22 | `TorrentEngine$5.lambda$onRestoreSessionError$10(String,Throwable)` | OPEN | Error consumer is registered in `onRestoreSessionError` (`TorrentEngine.java:1400-1416`); Rx error delivery not verified. |
| 23 | `TorrentEngine$5.lambda$onRestoreSessionError$9(String,Torrent)` | OPEN | Success consumer is registered in `onRestoreSessionError` (`TorrentEngine.java:1400-1416`); repository/Rx delivery not verified. |
| 24 | `TorrentEngine$5.lambda$onTorrentAdded$0(String)` | OPEN | Lambda is in the listener callback's asynchronous pause work (`TorrentEngine.java:1272-1287`); Rx execution not verified. |
| 25 | `TorrentEngine$5.lambda$onTorrentFinished$2(String,Torrent)` | OPEN | Success consumer belongs to the `onTorrentFinished` repository subscription (`TorrentEngine.java:1306-1325`); Rx delivery not verified. |
| 26 | `TorrentEngine$5.lambda$onTorrentFinished$3(String,Throwable)` | OPEN | Error consumer belongs to the `onTorrentFinished` repository subscription (`TorrentEngine.java:1306-1325`); Rx delivery not verified. |
| 27 | `TorrentEngine$5.lambda$onTorrentLoaded$1(String)` | OPEN | Lambda is in asynchronous pause work from `onTorrentLoaded` (`TorrentEngine.java:1291-1302`); Rx execution not verified. |
| 28 | `TorrentEngine$5.lambda$onTorrentMetadataLoaded$11(Exception,Torrent)` | OPEN | Success consumer belongs to the metadata listener's repository subscription (`TorrentEngine.java:1420-1440`); Rx delivery not verified. |
| 29 | `TorrentEngine$5.lambda$onTorrentMetadataLoaded$12(String,Throwable)` | OPEN | Error consumer belongs to the metadata listener's repository subscription (`TorrentEngine.java:1420-1440`); Rx delivery not verified. |
| 30 | `TorrentEngine$5.lambda$onTorrentMetadataLoaded$13(String)` | OPEN | Lambda is the nested save-file operation in the metadata callback (`TorrentEngine.java:1426-1437`); callback and Rx delivery remain open. |
| 31 | `TorrentEngine$5.lambda$onTorrentMoved$6(String,boolean,Torrent)` | OPEN | Success consumer belongs to the `onTorrentMoved` repository subscription (`TorrentEngine.java:1348-1368`); Rx delivery not verified. |
| 32 | `TorrentEngine$5.lambda$onTorrentMoved$7(String,Throwable)` | OPEN | Error consumer belongs to the `onTorrentMoved` repository subscription (`TorrentEngine.java:1348-1368`); Rx delivery not verified. |
| 33 | `TorrentEngine$5.lambda$onTorrentMoving$4(String,Torrent)` | OPEN | Success consumer belongs to the `onTorrentMoving` repository subscription (`TorrentEngine.java:1328-1344`); Rx delivery not verified. |
| 34 | `TorrentEngine$5.lambda$onTorrentMoving$5(String,Throwable)` | OPEN | Error consumer belongs to the `onTorrentMoving` repository subscription (`TorrentEngine.java:1328-1344`); Rx delivery not verified. |
| 35 | `TorrentEngine$5.onIpFilterParsed(int)` | OPEN | Registered engine listener callback (`TorrentEngine.java:1372-1381`); session filter event dispatch was not closed. |
| 36 | `TorrentEngine$5.onNatError(String)` | OPEN | Registered engine listener callback (`TorrentEngine.java:1393-1397`); NAT/library event dispatch was not closed. |
| 37 | `TorrentEngine$5.onRestoreSessionError(String)` | OPEN | Registered engine listener callback (`TorrentEngine.java:1400-1417`); restore error dispatch was not closed. |
| 38 | `TorrentEngine$5.onSessionError(String)` | OPEN | Registered engine listener callback (`TorrentEngine.java:1385-1390`); session error dispatch was not closed. |
| 39 | `TorrentEngine$5.onSessionStarted()` | OPEN | Listener forwards to `handleOnSessionStarted` (`TorrentEngine.java:1265-1269`); session notification is asynchronous in `TorrentSessionImpl.java:1006-1009`. |
| 40 | `TorrentEngine$5.onTorrentAdded(String)` | OPEN | Registered engine listener callback (`TorrentEngine.java:1272-1288`); session add-event dispatch was not independently verified. |

Totals: 40 rows = 3 REACHABLE, 0 UNREACHABLE, 37 OPEN. No coverage evidence was used. No graph, AGENT_NOTES, `out/`, or non-helper files were changed.
