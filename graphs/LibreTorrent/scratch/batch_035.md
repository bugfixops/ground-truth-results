# LibreTorrent batch 35 source audit

Membership is the exact 40-row set in `scratch/batch_035_plan.txt`. I checked the helper's method definitions and caller excerpts in `scratch/batch_035_helper_printed.txt`. The batch contains many local call chains, but none was closed from a registered app entry point with every callback/session/library hop represented by hand-authored edges. No methods are labeled from generator candidates or coverage.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `SessionLogger.applyFilterParams` | OPEN | Session settings caller (`TorrentSessionImpl.java:1416-1419`); full entry path unresolved. |
| 2 | `SessionLogger.send` | OPEN | Alert/session integration (`SessionLogger.java:117-167`; session listener `:1015-1032`); callback route unresolved. |
| 3 | `SessionLogger$SessionFilterParams.<init>` | OPEN | Constructed during settings application; entry route unresolved. |
| 4 | `SessionLogger$SessionLogEntryType.<clinit>` | OPEN | Enum initialization; full entry route unresolved. |
| 5 | `SessionLogger$SessionLogFilter.<clinit>` | OPEN | Enum static initialization; full entry route unresolved. |
| 6 | `SessionLogger$SessionLogFilter.<init>` | OPEN | Enum constructor; full entry route unresolved. |
| 7 | `SessionLogger$SessionLogFilter.filter` | OPEN | Called by `applyFilterParams`; full entry route unresolved. |
| 8 | `SessionLogger$SessionLogFilter.lambda$static$0` | OPEN | Enum-created predicate; invocation route not traced. |
| 9 | `SessionLogger$SessionLogFilter.lambda$static$1` | OPEN | Enum-created predicate; invocation route not traced. |
| 10 | `SessionLogger$SessionLogFilter.lambda$static$2` | OPEN | Enum-created predicate; invocation route not traced. |
| 11 | `SessionLogger$SessionLogFilter.lambda$static$3` | OPEN | Enum-created predicate; invocation route not traced. |
| 12 | `SessionLogger$SessionLogFilter.lambda$static$4` | OPEN | Enum-created predicate; invocation route not traced. |
| 13 | `TorrentCriticalWork.<init>` | OPEN | TorrentDownloadImpl initializes the field (`TorrentDownloadImpl.java:139,148-180`); class entry route unresolved. |
| 14 | `TorrentCriticalWork.emitChangedEvent` | OPEN | Called by setters; full route from app entry not established. |
| 15 | `TorrentCriticalWork.lambda$emitChangedEvent$0` | OPEN | Executor callback submitted by emitChangedEvent; setter entry route unresolved. |
| 16 | `TorrentCriticalWork.observeStateChanging` | OPEN | Definition/use search; complete route not established. |
| 17 | `TorrentCriticalWork.setMoving` | OPEN | Definition/use search; complete route not established. |
| 18 | `TorrentCriticalWork.setSaveResume` | OPEN | Definition/use search; complete route not established. |
| 19 | `TorrentCriticalWork$State.<init>` | OPEN | BehaviorSubject initial/change state construction; app entry route unresolved. |
| 20 | `TorrentCriticalWork$State.isDuringChange` | OPEN | Definition/use search; complete route not established. |
| 21 | `TorrentDownloadImpl.<clinit>` | OPEN | Class initialization with use; complete entry route not established. |
| 22 | `TorrentDownloadImpl.<init>` | OPEN | Constructor/listener registration read; route to object construction not audited. |
| 23 | `TorrentDownloadImpl.addTrackers` | OPEN | Definition at `TorrentDownloadImpl.java:977-991`; no complete route recorded. |
| 24 | `TorrentDownloadImpl.advancedPeerInfo` | OPEN | Used by peer listing/stats (`:911-947,1522-1527`); entry route unresolved. |
| 25 | `TorrentDownloadImpl.applyFirstLastPiecePriority(boolean)` | OPEN | Constructor/setter callers (`:168-172,1084-1111`); full entry route unresolved. |
| 26 | `TorrentDownloadImpl.applyFirstLastPiecePriority(boolean,Priority[])` | OPEN | Called by priority application paths (`:716-742,1109-1125`); full entry route unresolved. |
| 27 | `TorrentDownloadImpl.checkError` | OPEN | Alert listener route exists (`:205-284,302-337`); entry-to-alert dispatch unresolved. |
| 28 | `TorrentDownloadImpl.doPause` | OPEN | Internal pause implementation (`:594-675`); full app route unresolved. |
| 29 | `TorrentDownloadImpl.doResume` | OPEN | Internal resume implementation (`:594-675`); full app route unresolved. |
| 30 | `TorrentDownloadImpl.doStop` | OPEN | Stop handling (`:537-593`); complete entry route unresolved. |
| 31 | `TorrentDownloadImpl.forceRecheck` | OPEN | Definition at `:1247-1254`; no complete entry path recorded. |
| 32 | `TorrentDownloadImpl.forceStop` | OPEN | Internal stop helper (`:537-593`); complete entry route unresolved. |
| 33 | `TorrentDownloadImpl.getActiveTime` | OPEN | Definition at `:789-794`; complete entry route not recorded. |
| 34 | `TorrentDownloadImpl.getAvailability` | OPEN | TorrentEngine info construction caller (`:1462-1478`; `TorrentEngine.java:840-858`); entry route unresolved. |
| 35 | `TorrentDownloadImpl.getBencode` | OPEN | TorrentEngine/DetailTorrentViewModel callers (`:1650-1675`; `TorrentEngine.java:927-935`; `DetailTorrentViewModel.java:386`); complete route unresolved. |
| 36 | `TorrentDownloadImpl.getConnectedLeechers` | OPEN | Definition at `:825-832`; full route not established. |
| 37 | `TorrentDownloadImpl.getConnectedPeers` | OPEN | Definition at `:812-817`; full route not established. |
| 38 | `TorrentDownloadImpl.getConnectedSeeds` | OPEN | Definition at `:818-823`; full route not established. |
| 39 | `TorrentDownloadImpl.getDownloadSpeed` | OPEN | Definition at `:757-764`; full route not established. |
| 40 | `TorrentDownloadImpl.getDownloadSpeedLimit` | OPEN | Definition at `:1308-1318`; full route not established. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
