# Batch 24 source audit

Membership is the exact 40 rows in `batch_024_plan.txt`; the independent source scan is saved in `batch_024_independent_printed.txt`.

The scan locates these methods and their in-class callers in `TorrentEngine.java`. It does not provide complete app entry-to-method paths written as hand edges. Those source-local candidates remain OPEN until those graph routes are added. In particular, Rx listener and work callbacks cannot be upgraded from method presence alone. No app source calls were found that support `no_trigger_in_app`, so no such labels were assigned. No graph edit or build was made.

| # | Method | Label | Evidence / status |
|---:|---|---|---|
| 1 | `TorrentEngine.lambda$resumeAll$20` | OPEN | Source lambda body located in `TorrentEngine.java`; complete route not handwritten. |
| 2 | `TorrentEngine.lambda$setDownloadPath$22` | OPEN | Source lambda body located in `TorrentEngine.java`; complete route not handwritten. |
| 3 | `TorrentEngine.lambda$setFirstLastPiecePriority$24` | OPEN | Source lambda body located in `TorrentEngine.java`; complete route not handwritten. |
| 4 | `TorrentEngine.lambda$setSequentialDownload$23` | OPEN | Source lambda body located in `TorrentEngine.java`; complete route not handwritten. |
| 5 | `TorrentEngine.lambda$setTorrentName$21` | OPEN | Source lambda body located in `TorrentEngine.java`; complete route not handwritten. |
| 6 | `TorrentEngine.loadTorrents` | OPEN | Called by engine startup; full service entry route not handwritten. `TorrentEngine.java:1060,1085-1092`. |
| 7 | `TorrentEngine.makeAdvancedInfoSync(String)` | OPEN | Engine source declaration located; caller route not handwritten. `TorrentEngine.java:832`. |
| 8 | `TorrentEngine.makeInfo(Torrent,List)` | OPEN | Called by in-class sync methods; full engine route not handwritten. `TorrentEngine.java:766-822`. |
| 9 | `TorrentEngine.makeInfoListSync` | OPEN | Source declaration and internal data processing located. `TorrentEngine.java:814-822`. |
| 10 | `TorrentEngine.makeInfoSync(String)` | OPEN | Source declaration and caller references located. `TorrentEngine.java:766-773`. |
| 11 | `TorrentEngine.makeMagnet(String,boolean)` | OPEN | Source declaration and internal task calls located. `TorrentEngine.java:577-585`. |
| 12 | `TorrentEngine.makePeerInfoList(String)` | OPEN | Source declaration located. `TorrentEngine.java:872`. |
| 13 | `TorrentEngine.makeTorrentFileObserver(String)` | OPEN | Called during watch-dir setup; complete service/settings path not handwritten. `TorrentEngine.java:1124-1136`. |
| 14 | `TorrentEngine.makeTrackerInfoList(String)` | OPEN | Source declaration located. `TorrentEngine.java:861`. |
| 15 | `TorrentEngine.markAsHiddenSync(Torrent)` | OPEN | Internal engine call path located. `TorrentEngine.java:1260,1313`. |
| 16 | `TorrentEngine.observeEngineRunning` | OPEN | Rx Flowable and disposal callback paths; execution/entry route not complete. `TorrentEngine.java:182-227`. |
| 17 | `TorrentEngine.observeNeedStartEngine` | OPEN | Rx source, executor, and state path; execution/entry route not complete. `TorrentEngine.java:161-200`. |
| 18 | `TorrentEngine.observeTorrentMetaInfo(String)` | OPEN | Rx Flowable and session listener path; route not complete. `TorrentEngine.java:588-618`. |
| 19 | `TorrentEngine.parseMagnet(String)` | OPEN | Source method delegates to session; complete app route not handwritten. `TorrentEngine.java:427-428`. |
| 20 | `TorrentEngine.pauseAll` | OPEN | Rx work body; subscription path not verified in hand graph. `TorrentEngine.java:652-655`. |
| 21 | `TorrentEngine.pauseResumeTorrent(String)` | OPEN | Rx work body; subscription path not verified in hand graph. `TorrentEngine.java:488`. |
| 22 | `TorrentEngine.printSessionLog(List)` | OPEN | Logger observer callback path; complete route not handwritten. `TorrentEngine.java:253-262`. |
| 23 | `TorrentEngine.prioritizeFiles(String,Priority[])` | OPEN | Asynchronous body; subscription path not verified in hand graph. `TorrentEngine.java:734-741`. |
| 24 | `TorrentEngine.removeListener(TorrentEngineListener)` | OPEN | In-class listener disposal path; complete route not handwritten. `TorrentEngine.java:224,311-312`. |
| 25 | `TorrentEngine.replaceTrackers(String,List)` | OPEN | UI caller path not handwritten. `TorrentEngine.java:554-565`. |
| 26 | `TorrentEngine.requestStop` | OPEN | Service/engine stop path; full lifecycle route not handwritten. `TorrentEngine.java:275-299`. |
| 27 | `TorrentEngine.rescheduleTorrents` | OPEN | Rx work body; execution path not verified in hand graph. `TorrentEngine.java:315-327`. |
| 28 | `TorrentEngine.restartForegroundNotification` | OPEN | Service/engine lifecycle caller route not handwritten. `TorrentEngine.java:155`. |
| 29 | `TorrentEngine.resumeAll` | OPEN | Rx work body; subscription path not verified in hand graph. `TorrentEngine.java:661-664`. |
| 30 | `TorrentEngine.saveTorrentFile(String,Uri,String)` | OPEN | Called by engine file-save paths; complete UI/session route not handwritten. `TorrentEngine.java:961-973`. |
| 31 | `TorrentEngine.saveTorrentFileIn(Torrent,Uri)` | OPEN | In-class save path located; complete route not handwritten. `TorrentEngine.java:961-965,1273-1275`. |
| 32 | `TorrentEngine.scanTorrentsInDir(String)` | OPEN | Called during watch-directory setup; full settings/service route not handwritten. `TorrentEngine.java:1123,1166`. |
| 33 | `TorrentEngine.sendInfoToEmitter(SingleEmitter,byte[])` | OPEN | Called from Single source callback; Rx execution path not verified. `TorrentEngine.java:443-461`. |
| 34 | `TorrentEngine.setDownloadPath(String,Uri)` | OPEN | Source method and UI/settings callbacks located; full entry route not handwritten. `TorrentEngine.java:683-690,1320`. |
| 35 | `TorrentEngine.setDownloadSpeedLimit(String,int)` | OPEN | Source method located; UI route not handwritten. `TorrentEngine.java:905-913`. |
| 36 | `TorrentEngine.setFirstLastPiecePriority(String,boolean)` | OPEN | Source method and async body located; complete route not handwritten. `TorrentEngine.java:709-716`. |
| 37 | `TorrentEngine.setPortRange(int,int)` | OPEN | Settings observer source call exists; observer route remains OPEN. `TorrentEngine.java:1246,1552`. |
| 38 | `TorrentEngine.setProxy` | OPEN | Settings observer call exists; observer route remains OPEN. `TorrentEngine.java:1094,1571`. |
| 39 | `TorrentEngine.setRandomPortRange(boolean)` | OPEN | Settings observer source call exists; observer route remains OPEN. `TorrentEngine.java:1232,1546`. |
| 40 | `TorrentEngine.setSequentialDownload(String,boolean)` | OPEN | Source method and async body located; complete route not handwritten. `TorrentEngine.java:696-703`. |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used.
