# LibreTorrent batch 37 source audit

Membership is the exact 40-row set in `scratch/batch_037_plan.txt`. I checked the printed definitions, engine/session callers, and callback contexts in `scratch/batch_037_helper_printed.txt`. Local calls and captured lambdas exist, but complete app-entry routes with all session/library/Rx dispatch represented as hand-authored edges were not established. All rows remain OPEN.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentDownloadImpl.isPaused(TorrentStatus)` | OPEN | Private status helper; internal status path incomplete. |
| 2 | `TorrentDownloadImpl.isSeeding` | OPEN | Internal call and interface exposure; app-entry route unresolved. |
| 3 | `TorrentDownloadImpl.isSequentialDownload` | OPEN | Engine caller shown; complete entry route absent. |
| 4 | `TorrentDownloadImpl.isStopped` | OPEN | Definition/use search; route incomplete. |
| 5 | `TorrentDownloadImpl.isValid` | OPEN | Definition/use search; route incomplete. |
| 6 | `TorrentDownloadImpl.lambda$checkError$1` | OPEN | Captured listener callback; notifyListeners/alert route unresolved. |
| 7 | `TorrentDownloadImpl.lambda$handleMetadata$2` | OPEN | Captured error callback; alert route unresolved. |
| 8 | `TorrentDownloadImpl.lambda$handleMetadata$3` | OPEN | Captured notification callback; alert route unresolved. |
| 9 | `TorrentDownloadImpl.lambda$handleReadPiece$4` | OPEN | Captured callback; stream alert route unresolved. |
| 10 | `TorrentDownloadImpl.lambda$handleTorrentFinished$6` | OPEN | Captured listener callback; alert route unresolved. |
| 11 | `TorrentDownloadImpl.lambda$onStorageMoved$0` | OPEN | Captured callback; alert registration/entry route unresolved. |
| 12 | `TorrentDownloadImpl.lambda$requestStop$7` | OPEN | Rx state callback; stop-request route incomplete. |
| 13 | `TorrentDownloadImpl.lambda$requestStop$8` | OPEN | Rx error callback; stop-request route incomplete. |
| 14 | `TorrentDownloadImpl.lambda$requestStop$9` | OPEN | Completable source callback; stop-request route incomplete. |
| 15 | `TorrentDownloadImpl.lambda$setDownloadPath$10` | OPEN | Captured listener callback; app-entry route unresolved. |
| 16 | `TorrentDownloadImpl.lambda$torrentRemoved$5` | OPEN | Captured callback; alert route unresolved. |
| 17 | `TorrentDownloadImpl.makeMagnet` | OPEN | Engine/DetailTorrentViewModel callers; full UI entry route absent. |
| 18 | `TorrentDownloadImpl.notifyListeners` | OPEN | Called by callbacks (`TorrentDownloadImpl.java:182-193,205-485`); full entry route absent. |
| 19 | `TorrentDownloadImpl.onStorageMoved` | OPEN | Inner alert listener; library alert dispatch unresolved. |
| 20 | `TorrentDownloadImpl.operationNotAllowed` | OPEN | Widely called guard; complete routes to target callers unverified. |
| 21 | `TorrentDownloadImpl.pause` | OPEN | Interface method calls doPause; complete app route absent. |
| 22 | `TorrentDownloadImpl.pauseManually` | OPEN | TorrentSessionImpl caller; app-entry route unresolved. |
| 23 | `TorrentDownloadImpl.pieces` | OPEN | Definition/use search; complete entry route absent. |
| 24 | `TorrentDownloadImpl.prioritizeFiles` | OPEN | Definition/internal priority handling; full entry route absent. |
| 25 | `TorrentDownloadImpl.readPiece` | OPEN | TorrentInputStream caller; stream/server entry route unresolved. |
| 26 | `TorrentDownloadImpl.remove` | OPEN | Definition/use search; complete caller route absent. |
| 27 | `TorrentDownloadImpl.replaceTrackers` | OPEN | Definition/use search; full caller route absent. |
| 28 | `TorrentDownloadImpl.requestStop` | OPEN | Session stop caller; complete app-entry route absent. |
| 29 | `TorrentDownloadImpl.requestTrackerAnnounce` | OPEN | Definition/use search; complete caller route absent. |
| 30 | `TorrentDownloadImpl.resetTorrentError` | OPEN | Resumed-alert handling; complete alert route absent. |
| 31 | `TorrentDownloadImpl.resume` | OPEN | Public method with auto/manual state check; caller route unresolved. |
| 32 | `TorrentDownloadImpl.resumeManually` | OPEN | TorrentSessionImpl caller; app-entry route unresolved. |
| 33 | `TorrentDownloadImpl.saveResumeData` | OPEN | Internal callers exist; complete entry route not traced. |
| 34 | `TorrentDownloadImpl.serializeResumeData` | OPEN | Inner alert dispatch; full alert route unresolved. |
| 35 | `TorrentDownloadImpl.setAutoManaged` | OPEN | Definition/use search; complete app route absent. |
| 36 | `TorrentDownloadImpl.setDownloadPath` | OPEN | Definition/use search; complete route absent. |
| 37 | `TorrentDownloadImpl.setDownloadSpeedLimit` | OPEN | Definition/use search; complete app route absent. |
| 38 | `TorrentDownloadImpl.setFirstLastPiecePriority` | OPEN | Method/helper call printed; complete entry route absent. |
| 39 | `TorrentDownloadImpl.setInterestedPieces` | OPEN | TorrentInputStream calls; stream entry route unresolved. |
| 40 | `TorrentDownloadImpl.setMaxConnections` | OPEN | Definition/use search; complete app route absent. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
