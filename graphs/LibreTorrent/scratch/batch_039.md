# LibreTorrent batch 39 source audit

Membership is the exact 40-row set in `scratch/batch_039_plan.txt`. I reviewed the helper's printed session method bodies, caller excerpts and callback contexts in `scratch/batch_039_helper_printed.txt`. Local engine/settings/session calls exist, but the complete app-entry chains are not represented by hand-authored edges; alert, worker-thread and completion callbacks add unresolved dispatch steps. All rows remain OPEN.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentSessionImpl.enableIpFilter` | OPEN | Engine settings callers; complete entry route unresolved. |
| 2 | `TorrentSessionImpl.enableSessionLogger` | OPEN | Session lifecycle/settings callers; app entry route unresolved. |
| 3 | `TorrentSessionImpl.extractTrackers` | OPEN | Torrent metadata processing; entry route unresolved. |
| 4 | `TorrentSessionImpl.extractUrlSeeds` | OPEN | Torrent metadata processing; entry route unresolved. |
| 5 | `TorrentSessionImpl.fetchMagnet(String)` | OPEN | TorrentEngine delegate; full UI route unresolved. |
| 6 | `TorrentSessionImpl.fetchMagnet(AddTorrentParams)` | OPEN | Called by string overload; full UI route unresolved. |
| 7 | `TorrentSessionImpl.getAlertMask` | OPEN | Session start/settings callers; entry route unresolved. |
| 8 | `TorrentSessionImpl.getAllowedEncryptLevel` | OPEN | Settings conversion caller; route unresolved. |
| 9 | `TorrentSessionImpl.getDhtNodes` | OPEN | Stats construction caller; alert-to-entry route unresolved. |
| 10 | `TorrentSessionImpl.getDownloadSpeed` | OPEN | Stats construction caller; alert-to-entry route unresolved. |
| 11 | `TorrentSessionImpl.getDownloadSpeedLimit` | OPEN | Definition/use search; full app route unresolved. |
| 12 | `TorrentSessionImpl.getIface` | OPEN | Settings setup caller; entry route unresolved. |
| 13 | `TorrentSessionImpl.getListenPort` | OPEN | Stats construction caller; alert-to-entry route unresolved. |
| 14 | `TorrentSessionImpl.getLoadedMagnet` | OPEN | Engine magnet retrieval caller; app entry route unresolved. |
| 15 | `TorrentSessionImpl.getLogger` | OPEN | Engine obtains logger; entry route unresolved. |
| 16 | `TorrentSessionImpl.getPieceSizeList` | OPEN | Engine wrapper caller; UI entry route unresolved. |
| 17 | `TorrentSessionImpl.getSettings` | OPEN | Engine settings observers; entry route unresolved. |
| 18 | `TorrentSessionImpl.getTask` | OPEN | Engine/stream callers; app entry route unresolved. |
| 19 | `TorrentSessionImpl.getTorrentVersionList` | OPEN | Engine wrapper caller; UI entry route unresolved. |
| 20 | `TorrentSessionImpl.getTotalDownload` | OPEN | Stats construction caller; alert-to-entry route unresolved. |
| 21 | `TorrentSessionImpl.getTotalUpload` | OPEN | Stats construction caller; alert-to-entry route unresolved. |
| 22 | `TorrentSessionImpl.getUploadSpeed` | OPEN | Stats construction caller; alert-to-entry route unresolved. |
| 23 | `TorrentSessionImpl.getUploadSpeedLimit` | OPEN | Definition/use search; full app route unresolved. |
| 24 | `TorrentSessionImpl.handleMetadataReceived` | OPEN | InnerListener alert caller; external alert route unresolved. |
| 25 | `TorrentSessionImpl.handleSaveMetadata` | OPEN | InnerListener alert caller; external alert route unresolved. |
| 26 | `TorrentSessionImpl.handleStats` | OPEN | Stats alert caller; external alert route unresolved. |
| 27 | `TorrentSessionImpl.handleStoppingTasks` | OPEN | Completable completion action; stop entry route unresolved. |
| 28 | `TorrentSessionImpl.isDHTEnabled` | OPEN | Definition/use search; complete app caller route unresolved. |
| 29 | `TorrentSessionImpl.isPeXEnabled` | OPEN | Definition/use search; complete app caller route unresolved. |
| 30 | `TorrentSessionImpl.isRunning` | OPEN | Engine delegate; app-entry route unresolved. |
| 31 | `TorrentSessionImpl.isTorrentAlreadyRunning` | OPEN | Add/load logic callers; full entry route unresolved. |
| 32 | `TorrentSessionImpl.lambda$applySessionLoggerFilters$8` | OPEN | Scheduled Runnable; settings entry route unresolved. |
| 33 | `TorrentSessionImpl.lambda$checkError$5` | OPEN | Listener callback created after alert dispatch; route unresolved. |
| 34 | `TorrentSessionImpl.lambda$deleteTorrent$0` | OPEN | Listener callback in delete flow; app entry route unresolved. |
| 35 | `TorrentSessionImpl.lambda$enableIpFilter$1` | OPEN | Listener callback in parsing flow; settings entry route unresolved. |
| 36 | `TorrentSessionImpl.lambda$enableIpFilter$2` | OPEN | Background parse thread; settings entry route unresolved. |
| 37 | `TorrentSessionImpl.lambda$handleSaveMetadata$6` | OPEN | Listener callback; external alert route unresolved. |
| 38 | `TorrentSessionImpl.lambda$handleStats$7` | OPEN | Listener callback; external alert route unresolved. |
| 39 | `TorrentSessionImpl.lambda$onAfterStart$4` | OPEN | Scheduled after start; service/session startup route unresolved. |
| 40 | `TorrentSessionImpl.lambda$stopTasks$3` | OPEN | Completable error callback; stop entry route unresolved. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
