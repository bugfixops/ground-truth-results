# Batch 39 helper report

Membership is exactly the 40 rows with `batch==39` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; that TSV is the sole membership source. Session method definitions, local call sites, and handlers are printed/referenced in `scratch/batch_039_helper_printed.txt`. Some targets have clear local callers, but this bounded review did not establish complete routes from an app entry point, so uncertain rows remain OPEN.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `TorrentSessionImpl.enableIpFilter` | OPEN | — | Engine settings callbacks call it; complete settings-to-entry route not established. | `TorrentSessionImpl.java:718-741`; `TorrentEngine.java:1050,1558-1566` |
| `TorrentSessionImpl.enableSessionLogger` | OPEN | — | Called in session lifecycle/settings methods; complete app-entry route not recorded. | `TorrentSessionImpl.java:991-1008,1015-1038,1385-1399` |
| `TorrentSessionImpl.extractTrackers` | OPEN | — | Called while processing decoded torrent metadata; full entry route not established. | `TorrentSessionImpl.java:581-584,590-635` |
| `TorrentSessionImpl.extractUrlSeeds` | OPEN | — | Called while processing decoded torrent metadata; full entry route not established. | `TorrentSessionImpl.java:581-585,637-663` |
| `TorrentSessionImpl.fetchMagnet(String)` | OPEN | — | TorrentEngine delegates magnet lookup here; full UI entry route not traced. | `TorrentSessionImpl.java:427-452`; `TorrentEngine.java:415-424` |
| `TorrentSessionImpl.fetchMagnet(AddTorrentParams)` | OPEN | — | Called by the string overload; full UI entry route not traced. | `TorrentSessionImpl.java:427-435,454-470` |
| `TorrentSessionImpl.getAlertMask` | OPEN | — | Called during onAfterStart and settings packing; complete entry route not recorded. | `TorrentSessionImpl.java:991-1005,1278,1301-1316` |
| `TorrentSessionImpl.getAllowedEncryptLevel` | OPEN | — | Called by settings conversion; complete entry route not established. | `TorrentSessionImpl.java:1270,1330-1340` |
| `TorrentSessionImpl.getDhtNodes` | OPEN | — | Used when building session stats; complete alert-to-entry route not established. | `TorrentSessionImpl.java:712-715,1168-1180` |
| `TorrentSessionImpl.getDownloadSpeed` | OPEN | — | Used when building session stats; complete alert-to-entry route not established. | `TorrentSessionImpl.java:665-669,1168-1180` |
| `TorrentSessionImpl.getDownloadSpeedLimit` | OPEN | — | Definition read; complete app caller route not established. | `TorrentSessionImpl.java:689-695`; usage search |
| `TorrentSessionImpl.getIface` | OPEN | — | Called from settings setup; complete entry route not recorded. | `TorrentSessionImpl.java:1259,1360-1375` |
| `TorrentSessionImpl.getListenPort` | OPEN | — | Used when building session stats; complete alert-to-entry route not established. | `TorrentSessionImpl.java:705-709,1168-1180` |
| `TorrentSessionImpl.getLoadedMagnet` | OPEN | — | Used by engine magnet retrieval; full app-entry route not established. | `TorrentSessionImpl.java:233-237`; `TorrentEngine.java:449` |
| `TorrentSessionImpl.getLogger` | OPEN | — | TorrentEngine obtains it for log updates; complete entry route not recorded. | `TorrentSessionImpl.java:178-182`; `TorrentEngine.java:253,957-959` |
| `TorrentSessionImpl.getPieceSizeList` | OPEN | — | Engine exposes session values; complete UI entry route not recorded. | `TorrentSessionImpl.java:972-975`; `TorrentEngine.java:950` |
| `TorrentSessionImpl.getSettings` | OPEN | — | Called by engine settings observers; complete entry route not established. | `TorrentSessionImpl.java:220-231`; `TorrentEngine.java:1095,1233` |
| `TorrentSessionImpl.getTask` | OPEN | — | Called from many engine and stream methods; complete entry route not recorded. | `TorrentSessionImpl.java:196-200`; `TorrentEngine.java:490-942` |
| `TorrentSessionImpl.getTorrentVersionList` | OPEN | — | Engine exposes session values; complete UI entry route not recorded. | `TorrentSessionImpl.java:977-981`; `TorrentEngine.java:954` |
| `TorrentSessionImpl.getTotalDownload` | OPEN | — | Used when building session stats; full alert-to-entry route not established. | `TorrentSessionImpl.java:677-681,1168-1180` |
| `TorrentSessionImpl.getTotalUpload` | OPEN | — | Used when building session stats; full alert-to-entry route not established. | `TorrentSessionImpl.java:683-687,1168-1180` |
| `TorrentSessionImpl.getUploadSpeed` | OPEN | — | Used when building session stats; full alert-to-entry route not established. | `TorrentSessionImpl.java:671-675,1168-1180` |
| `TorrentSessionImpl.getUploadSpeedLimit` | OPEN | — | Definition read; complete app caller route not established. | `TorrentSessionImpl.java:697-703`; usage search |
| `TorrentSessionImpl.handleMetadataReceived` | OPEN | — | Called from InnerListener alert dispatch; full external alert route not established. | `TorrentSessionImpl.java:1092-1094,1145-1151` |
| `TorrentSessionImpl.handleSaveMetadata` | OPEN | — | Called from InnerListener alert dispatch; full external alert route not established. | `TorrentSessionImpl.java:1098-1100,1153-1166` |
| `TorrentSessionImpl.handleStats` | OPEN | — | Called from session stats alert dispatch; full external alert route not established. | `TorrentSessionImpl.java:1095-1097,1168-1181` |
| `TorrentSessionImpl.handleStoppingTasks` | OPEN | — | Passed as a Completable completion action; complete stop entry route not traced. | `TorrentSessionImpl.java:920-948` |
| `TorrentSessionImpl.isDHTEnabled` | OPEN | — | Definition read; complete app caller route not established. | `TorrentSessionImpl.java:846-852`; usage search |
| `TorrentSessionImpl.isPeXEnabled` | OPEN | — | Definition read; complete app caller route not established. | `TorrentSessionImpl.java:854-859`; usage search |
| `TorrentSessionImpl.isRunning` | OPEN | — | Engine delegates running-state checks here; full app-entry route not recorded. | `TorrentSessionImpl.java:959-963`; `TorrentEngine.java:304` |
| `TorrentSessionImpl.isTorrentAlreadyRunning` | OPEN | — | Called by session torrent addition/loading logic; full entry route not established. | `TorrentSessionImpl.java:402,1475-1478` |
| `TorrentSessionImpl.lambda$applySessionLoggerFilters$8` | OPEN | — | Runnable is scheduled by settings filter application; end-to-end entry route not established. | `TorrentSessionImpl.java:1416-1428` |
| `TorrentSessionImpl.lambda$checkError$5` | OPEN | — | Listener callback created by checkError after alert dispatch; route not established. | `TorrentSessionImpl.java:1109-1143` |
| `TorrentSessionImpl.lambda$deleteTorrent$0` | OPEN | — | Listener callback created in deleteTorrent; complete app entry route not established. | `TorrentSessionImpl.java:377-390` |
| `TorrentSessionImpl.lambda$enableIpFilter$1` | OPEN | — | Listener callback created in IP filter parsing; complete settings entry route not established. | `TorrentSessionImpl.java:718-741` |
| `TorrentSessionImpl.lambda$enableIpFilter$2` | OPEN | — | Background parse thread body; complete settings entry route not established. | `TorrentSessionImpl.java:718-741` |
| `TorrentSessionImpl.lambda$handleSaveMetadata$6` | OPEN | — | Listener callback created by metadata-save handling; external alert route not established. | `TorrentSessionImpl.java:1153-1166` |
| `TorrentSessionImpl.lambda$handleStats$7` | OPEN | — | Listener callback created by stats handler; external alert route not established. | `TorrentSessionImpl.java:1168-1181` |
| `TorrentSessionImpl.lambda$onAfterStart$4` | OPEN | — | Runnable is scheduled after start; full service-to-session start route not traced. | `TorrentSessionImpl.java:991-1010` |
| `TorrentSessionImpl.lambda$stopTasks$3` | OPEN | — | Completable error callback created in stopTasks; full stop entry route not traced. | `TorrentSessionImpl.java:920-935` |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
