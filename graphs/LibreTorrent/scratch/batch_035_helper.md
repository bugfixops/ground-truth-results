# Batch 35 helper report

Membership is exactly the 40 rows with `batch==35` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the plan TSV is the sole membership source. Definitions and local caller evidence are recorded in `scratch/batch_035_helper_printed.txt`. Local call sites are present, but this source review did not finish the complete app-entry route for any method, so uncertain rows remain OPEN.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `SessionLogger.applyFilterParams` | OPEN | — | Called from session settings handling, but full entry route not audited. | `SessionLogger.java:169-201`; `TorrentSessionImpl.java:1416-1419` |
| `SessionLogger.send` | OPEN | — | Alert-to-logger dispatch originates in logger/session integration; full callback route not established. | `SessionLogger.java:117-167`; `TorrentSessionImpl.java:1015-1032` |
| `SessionLogger$SessionFilterParams.<init>` | OPEN | — | Constructed in settings application; full entry route not established. | `SessionLogger.java:89-109`; `TorrentSessionImpl.java:1416-1419` |
| `SessionLogger$SessionLogEntryType.<clinit>` | OPEN | — | Enum initialization is visible, but complete entry route is not established. | `SessionLogger.java:36-62` |
| `SessionLogger$SessionLogFilter.<clinit>` | OPEN | — | Enum static initialization creates filters; full entry route is not established. | `SessionLogger.java:64-87` |
| `SessionLogger$SessionLogFilter.<init>` | OPEN | — | Enum constructor participates in enum initialization; full entry route not established. | `SessionLogger.java:64-81` |
| `SessionLogger$SessionLogFilter.filter` | OPEN | — | Called by applyFilterParams; complete entry route not established. | `SessionLogger.java:83-86,169-201` |
| `SessionLogger$SessionLogFilter.lambda$static$0` | OPEN | — | Lambda is created by enum initializer; invocation depends on logger filtering, route not traced. | `SessionLogger.java:64-68` |
| `SessionLogger$SessionLogFilter.lambda$static$1` | OPEN | — | Lambda is created by enum initializer; invocation depends on logger filtering, route not traced. | `SessionLogger.java:68-70` |
| `SessionLogger$SessionLogFilter.lambda$static$2` | OPEN | — | Lambda is created by enum initializer; invocation depends on logger filtering, route not traced. | `SessionLogger.java:70-72` |
| `SessionLogger$SessionLogFilter.lambda$static$3` | OPEN | — | Lambda is created by enum initializer; invocation depends on logger filtering, route not traced. | `SessionLogger.java:72-74` |
| `SessionLogger$SessionLogFilter.lambda$static$4` | OPEN | — | Lambda is created by enum initializer; invocation depends on logger filtering, route not traced. | `SessionLogger.java:72-74` |
| `TorrentCriticalWork.<init>` | OPEN | — | TorrentDownloadImpl initializes a field with this object; complete app-entry route not established. | `TorrentCriticalWork.java:30-61`; `TorrentDownloadImpl.java:139,148-180` |
| `TorrentCriticalWork.emitChangedEvent` | OPEN | — | Called by its setters; full entry route not established. | `TorrentCriticalWork.java:68-97` |
| `TorrentCriticalWork.lambda$emitChangedEvent$0` | OPEN | — | Executor lambda is submitted by emitChangedEvent; route to setter use not traced. | `TorrentCriticalWork.java:93-97` |
| `TorrentCriticalWork.observeStateChanging` | OPEN | — | Definition read; no complete call route established. | `TorrentCriticalWork.java:88-91`; focused usage search |
| `TorrentCriticalWork.setMoving` | OPEN | — | Definition read; complete call route not established. | `TorrentCriticalWork.java:68-72`; focused usage search |
| `TorrentCriticalWork.setSaveResume` | OPEN | — | Definition read; complete call route not established. | `TorrentCriticalWork.java:79-86`; focused usage search |
| `TorrentCriticalWork$State.<init>` | OPEN | — | Constructed by BehaviorSubject initial value and change emission; complete app-entry route not established. | `TorrentCriticalWork.java:38-61,93-97` |
| `TorrentCriticalWork$State.isDuringChange` | OPEN | — | Definition read; no complete call route established. | `TorrentCriticalWork.java:44-54`; focused usage search |
| `TorrentDownloadImpl.<clinit>` | OPEN | — | Static initialization occurs with class use; full app-entry route not established. | `TorrentDownloadImpl.java:99-129,148-180` |
| `TorrentDownloadImpl.<init>` | OPEN | — | Constructor and listener registration read; caller route into creation not audited. | `TorrentDownloadImpl.java:148-180`; focused construction search |
| `TorrentDownloadImpl.addTrackers` | OPEN | — | No complete hand-written entry route recorded. | `TorrentDownloadImpl.java:977-991`; focused usage search |
| `TorrentDownloadImpl.advancedPeerInfo` | OPEN | — | Called by peer listing and additional stats paths; full entry route not established. | `TorrentDownloadImpl.java:911-947,1522-1527` |
| `TorrentDownloadImpl.applyFirstLastPiecePriority(boolean)` | OPEN | — | Called from constructor and setter; complete entry route not established. | `TorrentDownloadImpl.java:168-172,1084-1111` |
| `TorrentDownloadImpl.applyFirstLastPiecePriority(boolean,Priority[])` | OPEN | — | Called by prioritizeFiles and helper overload; complete entry route not established. | `TorrentDownloadImpl.java:716-742,1109-1125` |
| `TorrentDownloadImpl.checkError` | OPEN | — | Alert listener routes to error handling, but entry-to-alert callback is not traced. | `TorrentDownloadImpl.java:205-284,302-337` |
| `TorrentDownloadImpl.doPause` | OPEN | — | Internal pause implementation is called by pause controls; full entry route not established. | `TorrentDownloadImpl.java:594-675` |
| `TorrentDownloadImpl.doResume` | OPEN | — | Internal resume implementation is called by resume controls; full entry route not established. | `TorrentDownloadImpl.java:594-675` |
| `TorrentDownloadImpl.doStop` | OPEN | — | Called from stop handling; complete entry route not established. | `TorrentDownloadImpl.java:537-593` |
| `TorrentDownloadImpl.forceRecheck` | OPEN | — | No complete entry route recorded. | `TorrentDownloadImpl.java:1247-1254`; focused usage search |
| `TorrentDownloadImpl.forceStop` | OPEN | — | Internal stop helper; complete entry route not established. | `TorrentDownloadImpl.java:537-593` |
| `TorrentDownloadImpl.getActiveTime` | OPEN | — | Definition read; no complete route from app entry recorded. | `TorrentDownloadImpl.java:789-794`; focused usage search |
| `TorrentDownloadImpl.getAvailability` | OPEN | — | Called by TorrentEngine info construction; full entry route not audited. | `TorrentDownloadImpl.java:1462-1478`; `TorrentEngine.java:840-858` |
| `TorrentDownloadImpl.getBencode` | OPEN | — | Called through TorrentEngine and DetailTorrentViewModel; complete entry route not established. | `TorrentDownloadImpl.java:1650-1675`; `TorrentEngine.java:927-935`; `DetailTorrentViewModel.java:386` |
| `TorrentDownloadImpl.getConnectedLeechers` | OPEN | — | Definition read; complete route not established. | `TorrentDownloadImpl.java:825-832`; focused usage search |
| `TorrentDownloadImpl.getConnectedPeers` | OPEN | — | Definition read; complete route not established. | `TorrentDownloadImpl.java:812-817`; focused usage search |
| `TorrentDownloadImpl.getConnectedSeeds` | OPEN | — | Definition read; complete route not established. | `TorrentDownloadImpl.java:818-823`; focused usage search |
| `TorrentDownloadImpl.getDownloadSpeed` | OPEN | — | Definition read; complete route not established. | `TorrentDownloadImpl.java:757-764`; focused usage search |
| `TorrentDownloadImpl.getDownloadSpeedLimit` | OPEN | — | Definition read; complete route not established. | `TorrentDownloadImpl.java:1308-1318`; focused usage search |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
