# Batch 25 source audit

Membership is the 40 rows in `batch_025_plan.txt`; full printed app-source evidence is in `batch_025_helper_printed.txt`.

Three helper recommendations have local entry/caller evidence (`switchConnectionReceiver`, `switchPowerReceiver`, and `TorrentEngine$5.<init>`), but the end-to-end entry paths are not yet represented by complete hand-authored edges in graph_def.py. Other candidate methods depend on UI wiring, file observer delivery, Rx execution, or session callbacks. All 40 remain OPEN; no `no_trigger_in_app` labels are supported by this batch audit.

| Method | Label | Evidence / why OPEN |
|---|---|---|
| `TorrentEngine.setTorrentName(String,String)` | OPEN | Rx body and ViewModel call exist; UI path not closed. `TorrentEngine.java:670-681`; `DetailTorrentViewModel.java:478-490`. |
| `TorrentEngine.setUploadSpeedLimit(String,int)` | OPEN | ViewModel/dialog call path exists; full UI route not closed. `TorrentEngine.java:916-925`; `DetailTorrentViewModel.java:393-396`; `DetailTorrentFragment.java:766-800`. |
| `TorrentEngine.start` | OPEN | App call sites exist, but launcher subscription path uses Rx. `TorrentEngine.java:148-153`; `MainActivity.java:463-468`. |
| `TorrentEngine.startStreamingServer` | OPEN | Called through settings/session callbacks not yet closed. `TorrentEngine.java:1046-1077,1592-1601`. |
| `TorrentEngine.startWatchDir` | OPEN | Called through session/settings callbacks not yet closed. `TorrentEngine.java:1046-1061,1581-1591`. |
| `TorrentEngine.stopStreamingServer` | OPEN | Called by other methods whose callback route remains open. `TorrentEngine.java:1063-1083,1592-1601`. |
| `TorrentEngine.stopWatchDir` | OPEN | Settings/watch restart path depends on callback delivery. `TorrentEngine.java:1128-1135,1581-1591`. |
| `TorrentEngine.switchConnectionReceiver` | OPEN | Service/doStart local route exists; complete service entry path is not hand-authored. `TorrentService.java:130-131`; `TorrentEngine.java:234-241`. |
| `TorrentEngine.switchPowerReceiver` | OPEN | Service/doStart local route exists; complete service entry path is not hand-authored. `TorrentService.java:130-131`; `TorrentEngine.java:234-241`. |
| `TorrentEngine$1.<init>(TorrentEngine,FlowableEmitter)` | OPEN | Created inside Rx Flowable source; source invocation depends on library execution. `TorrentEngine.java:202-227`. |
| `TorrentEngine$1.onSessionStarted` | OPEN | Session listener callback dispatch not source-closed. `TorrentEngine.java:207-212`. |
| `TorrentEngine$1.onSessionStopped` | OPEN | Session listener callback dispatch not source-closed. `TorrentEngine.java:214-218`. |
| `TorrentEngine$2.<init>(TorrentEngine,String,SingleEmitter)` | OPEN | Created in magnet-fetch subscription body. `TorrentEngine.java:431-458`. |
| `TorrentEngine$2.onMagnetLoaded(String,byte[])` | OPEN | Session/library callback delivery not closed. `TorrentEngine.java:431-458`. |
| `TorrentEngine$3.<init>(TorrentEngine,String,FlowableEmitter)` | OPEN | Created inside Rx Flowable source. `TorrentEngine.java:588-618`. |
| `TorrentEngine$3.onTorrentMetadataLoaded(String,Exception)` | OPEN | Session listener callback dispatch not closed. `TorrentEngine.java:588-618`. |
| `TorrentEngine$4.<init>(TorrentEngine,String,String)` | OPEN | Created via watch-directory setup whose session/settings entry route remains OPEN. `TorrentEngine.java:1116-1137`. |
| `TorrentEngine$4.lambda$onEvent$0(Uri)` | OPEN | Rx completion callback delivery not established. `TorrentEngine.java:1139-1161`. |
| `TorrentEngine$4.onEvent(int,String)` | OPEN | File observer event callback delivery and event occurrence not established. `TorrentEngine.java:1137-1163`. |
| `TorrentEngine$5.<init>(TorrentEngine)` | OPEN | Engine field/constructor route exists; complete app entry route not handwritten. `TorrentEngine.java:130-141,1265-1270`. |
| `TorrentEngine$5.lambda$onIpFilterParsed$8(int)` | OPEN | Callback body depends on session listener invocation. `TorrentEngine.java:1372-1381`. |
| `TorrentEngine$5.lambda$onRestoreSessionError$10(String,Throwable)` | OPEN | Rx error callback delivery not verified. `TorrentEngine.java:1400-1416`. |
| `TorrentEngine$5.lambda$onRestoreSessionError$9(String,Torrent)` | OPEN | Rx success callback delivery not verified. `TorrentEngine.java:1400-1416`. |
| `TorrentEngine$5.lambda$onTorrentAdded$0(String)` | OPEN | Rx work body execution not verified. `TorrentEngine.java:1272-1287`. |
| `TorrentEngine$5.lambda$onTorrentFinished$2(String,Torrent)` | OPEN | Rx success callback delivery not verified. `TorrentEngine.java:1306-1325`. |
| `TorrentEngine$5.lambda$onTorrentFinished$3(String,Throwable)` | OPEN | Rx error callback delivery not verified. `TorrentEngine.java:1306-1325`. |
| `TorrentEngine$5.lambda$onTorrentLoaded$1(String)` | OPEN | Rx work body execution not verified. `TorrentEngine.java:1291-1302`. |
| `TorrentEngine$5.lambda$onTorrentMetadataLoaded$11(Exception,Torrent)` | OPEN | Rx repository success delivery not verified. `TorrentEngine.java:1420-1440`. |
| `TorrentEngine$5.lambda$onTorrentMetadataLoaded$12(String,Throwable)` | OPEN | Rx repository error delivery not verified. `TorrentEngine.java:1420-1440`. |
| `TorrentEngine$5.lambda$onTorrentMetadataLoaded$13(String)` | OPEN | Nested save-file operation depends on callback/Rx delivery. `TorrentEngine.java:1426-1437`. |
| `TorrentEngine$5.lambda$onTorrentMoved$6(String,boolean,Torrent)` | OPEN | Rx repository success delivery not verified. `TorrentEngine.java:1348-1368`. |
| `TorrentEngine$5.lambda$onTorrentMoved$7(String,Throwable)` | OPEN | Rx repository error delivery not verified. `TorrentEngine.java:1348-1368`. |
| `TorrentEngine$5.lambda$onTorrentMoving$4(String,Torrent)` | OPEN | Rx repository success delivery not verified. `TorrentEngine.java:1328-1344`. |
| `TorrentEngine$5.lambda$onTorrentMoving$5(String,Throwable)` | OPEN | Rx repository error delivery not verified. `TorrentEngine.java:1328-1344`. |
| `TorrentEngine$5.onIpFilterParsed(int)` | OPEN | Session callback delivery not verified. `TorrentEngine.java:1372-1381`. |
| `TorrentEngine$5.onNatError(String)` | OPEN | NAT/session callback delivery not verified. `TorrentEngine.java:1393-1397`. |
| `TorrentEngine$5.onRestoreSessionError(String)` | OPEN | Session restore callback delivery not verified. `TorrentEngine.java:1400-1417`. |
| `TorrentEngine$5.onSessionError(String)` | OPEN | Session error callback delivery not verified. `TorrentEngine.java:1385-1390`. |
| `TorrentEngine$5.onSessionStarted` | OPEN | Session notification is asynchronous and callback route remains open. `TorrentEngine.java:1265-1269`; `TorrentSessionImpl.java:1006-1009`. |
| `TorrentEngine$5.onTorrentAdded(String)` | OPEN | Session add-event dispatch not independently established. `TorrentEngine.java:1272-1288`. |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used.
