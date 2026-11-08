# LibreTorrent batch 25 — Phase 2 spot-check (UNVERIFIED spot-check, not a merge verdict)

- Source file checked: `~/workspace/overnight/stream-A/work/batch25-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. This file carries no dated 2026-11-01 Phase 1c revision note listing label changes, so no additional Phase 1 rows were added to the check set.
- Evidence base: already-fetched local files only — `~/workspace/b232425-src/` (TorrentEngine, DetailTorrentViewModel, MainViewModel) and `~/workspace/overnight/stream-A/corpus/java/service/TorrentService.java`. No GitHub connector fetch was made, no 429 encountered, no file was missing.
- Build / sampler / C1: not run (not this task). No edit was made to the merge-ready file.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (re-derived) |
|---|---|---|---|---|
| 1 | TorrentEngine.setTorrentName(String,String) | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:670-677; caller DetailTorrentViewModel.java:488 (`engine.setTorrentName(torrentId, name)`). |
| 6 | TorrentEngine.stopStreamingServer() | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:1079-1083; callers: doStop :298, startStreamingServer itself :1064, handleSettingsChanged :1596 (streaming-enable key, when disabled). TorrentService.stopEngine path verified (stopEngine :157 calls engine.doStop()). |
| 11 | TorrentEngine$1.onSessionStarted() | REACHABLE / INFERRED | PASS | Def TorrentEngine.java:209-212 (the onSessionStarted override inside the observeEngineRunning listener); invoked only via session dispatch to the row-10 listener, hence INFERRED. Enclosing observeEngineRunning route verified in batch 24 row 16. |
| 16 | TorrentEngine$3.onTorrentMetadataLoaded(String,Exception) | REACHABLE / INFERRED | PASS | Def TorrentEngine.java:592-605 (the listener override inside observeTorrentMetaInfo); invoked only via session dispatch, hence INFERRED. Enclosing observeTorrentMetaInfo caller verified (DetailTorrentViewModel.java:196, batch 23 row 36). |
| 21 | TorrentEngine$5.lambda$onIpFilterParsed$8(int) | REACHABLE / mixed SOURCE/INFERRED | PASS (normalisation note) | Completable.fromRunnable Toast body inside onIpFilterParsed, TorrentEngine.java:1372-1383, subscribed :1381-1382 on the main thread. Label REACHABLE correct; confirmed_by mixed as filed ("SOURCE for the subscribe; INFERRED for session dispatch upstream") and needs merge-time normalisation to one value (not decided here). |
| 26 | TorrentEngine$5.lambda$onTorrentFinished$3(String,Throwable) | REACHABLE / mixed SOURCE/INFERRED | PASS (normalisation note) | Error action of the onTorrentFinished subscription, TorrentEngine.java:1326-1327 (Log.e on repo-lookup error), inside onTorrentFinished :1306-1326. Label REACHABLE correct; confirmed_by mixed as filed, same normalisation note. |
| 31 | TorrentEngine$5.lambda$onTorrentMoved$6(String,Torrent) | REACHABLE / mixed SOURCE/INFERRED | PASS (normalisation note) | Success action of the repo.getTorrentByIdSingle subscription inside onTorrentMoved, TorrentEngine.java:1349-1367. Label REACHABLE correct; confirmed_by mixed as filed, same normalisation note. |
| 36 | TorrentEngine$5.onNatError(String) | REACHABLE / mixed SOURCE/INFERRED | PASS (normalisation note) | Def TorrentEngine.java:1393-1397 (logs, notifies if pref.showNatErrors()); registered via constructor TorrentEngine.java:140. Label REACHABLE correct; confirmed_by mixed as filed ("SOURCE for registration; INFERRED for session dispatch"), same normalisation note. |

## Totals

- PASS: 8 / 8 (4 with a confirmed_by-normalisation note only: rows 21, 26, 31, 36). FAIL: 0.
- Proposed corrections: none to any label. Merge-time action owed (not a spot-check fix): normalise rows 21, 26, 31, 36 to a single confirmed_by value under one project-wide convention.
