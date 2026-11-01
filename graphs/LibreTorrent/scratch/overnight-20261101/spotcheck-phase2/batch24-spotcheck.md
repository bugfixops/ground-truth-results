# LibreTorrent batch 24 — Phase 2 spot-check (UNVERIFIED spot-check, not a merge verdict)

- Source file checked: `~/workspace/overnight/stream-A/work/batch24-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. This file carries no dated 2026-11-01 Phase 1c revision note listing label changes, so no additional Phase 1 rows were added to the check set.
- Evidence base: already-fetched local files only — `~/workspace/b232425-src/` (TorrentEngine, DetailTorrentViewModel, MainViewModel) and `~/workspace/overnight/stream-A/corpus/java/service/TorrentService.java`. No GitHub connector fetch was made, no 429 encountered, no file was missing.
- Build / sampler / C1: not run (not this task). No edit was made to the merge-ready file.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (re-derived) |
|---|---|---|---|---|
| 1 | TorrentEngine.lambda$resumeAll$20() | REACHABLE / mixed SOURCE/INFERRED | PASS (normalisation note) | Runnable body inside resumeAll, TorrentEngine.java:661-668; parent resumeAll called from TorrentService.handleActions:221 and :226. Label REACHABLE correct; confirmed_by as filed is mixed ("SOURCE for subscribe; INFERRED for Rx dispatch") and needs merge-time normalisation to one value (not decided here). |
| 6 | TorrentEngine.loadTorrents() | REACHABLE / mixed SOURCE/INFERRED | PASS (normalisation note) | Def TorrentEngine.java:1085-1092; called by handleOnSessionStarted :1046 (which calls loadTorrents), itself called by engineListener.onSessionStarted :1268; listener registered TorrentEngine.java:140. Label REACHABLE correct; confirmed_by mixed as filed, same normalisation note. |
| 11 | TorrentEngine.makeMagnet(String,boolean) | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:577-586; caller DetailTorrentViewModel.java:381-382 (`engine.makeMagnet(torrentId, includePriorities)`). |
| 16 | TorrentEngine.observeEngineRunning() | REACHABLE / mixed SOURCE/INFERRED | PASS (normalisation note) | Def TorrentEngine.java:202-228; called by observeNeedStartEngine :182-183, reached via MainViewModel.java:154-155 (`engine.observeNeedStartEngine()`). Label REACHABLE correct; confirmed_by mixed as filed, same normalisation note. |
| 21 | TorrentEngine.pauseResumeTorrent(String) | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:488-505; caller DetailTorrentViewModel.java:357-358. |
| 26 | TorrentEngine.requestStop() | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:275-280 (early return if pref.keepAlive(), else forceStop()); caller MainViewModel.java:166-167 (`engine.requestStop()`). |
| 31 | TorrentEngine.saveTorrentFileIn(Torrent,Uri) | REACHABLE / mixed SOURCE/INFERRED | PASS (normalisation note) | Def TorrentEngine.java:961-971, calling row 30 (saveTorrentFile) at :965; called by engineListener.onTorrentAdded :1274 and onTorrentMetadataLoaded :1432 (both gated by pref.saveTorrentFiles()); listener registered TorrentEngine.java:140. Label REACHABLE correct; confirmed_by mixed as filed, same normalisation note. |
| 36 | TorrentEngine.setFirstLastPiecePriority(String,boolean) | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:709-719; caller DetailTorrentViewModel.java:515 (inside checkParamsChanged branch). |

## Totals

- PASS: 8 / 8 (4 with a confirmed_by-normalisation note only: rows 1, 6, 16, 31). FAIL: 0.
- Proposed corrections: none to any label. Merge-time action owed (not a spot-check fix): normalise rows 1, 6, 16, 31 to a single confirmed_by value under one project-wide convention.
