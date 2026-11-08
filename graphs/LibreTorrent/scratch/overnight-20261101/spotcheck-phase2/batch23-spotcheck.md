# LibreTorrent batch 23 — Phase 2 spot-check (UNVERIFIED spot-check, not a merge verdict)

- Source file checked: `~/workspace/overnight/stream-A/work/batch23-merge-ready.md` (UNVERIFIED proposal, not a result).
- Rows checked (8): sample rows 1, 6, 11, 16, 21, 26, 31, 36. This file carries no dated 2026-11-01 Phase 1c revision note listing label changes, so no additional Phase 1 rows were added to the check set; the file's own "UPGRADED in this pass" rows are not Phase 1 changes and were checked only where they fall in the sample.
- Evidence base: already-fetched local files only — `~/workspace/b232425-src/` (TorrentEngine, DetailTorrentViewModel, TorrentInfoProvider, CreateTorrentViewModel) and `~/workspace/overnight/stream-A/corpus/java/service/TorrentService.java` (doStart anchor). No GitHub connector fetch was made, no 429 encountered, no file was missing.
- Build / sampler / C1: not run (not this task). No edit was made to the merge-ready file.

## Per-row verdicts

| Row | Method | Filed label / confirmed_by | Verdict | Printed evidence (re-derived) |
|---|---|---|---|---|
| 1 | TorrentEngine.getDownloadSpeedLimit(String) | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:894-902; caller DetailTorrentViewModel.java:378 (`engine.getDownloadSpeedLimit(torrentId)`). |
| 6 | TorrentEngine.getPieces(String) | REACHABLE / SOURCE | PASS | Callers TorrentInfoProvider.java:429 and :442 (`engine.getPieces(id)`); definition in TorrentEngine.java (getPieces, ~:640). |
| 11 | TorrentEngine.getTorrentVersionList() | REACHABLE / SOURCE | PASS | Def TorrentEngine.java:953-954; callers CreateTorrentViewModel.java:145 and :339. |
| 16 | TorrentEngine.handleSettingsChanged(String) | REACHABLE / mixed SOURCE/INFERRED | PASS (normalisation note) | Def TorrentEngine.java:1456ff; subscribed in doStart at TorrentEngine.java:241 (`.subscribe(this::handleSettingsChanged)`); doStart called from TorrentService.java:131 (`engine.doStart()`). Label REACHABLE correct. Note: confirmed_by as filed is a mixed "SOURCE for subscription; INFERRED for Rx settings emission" value, not a single SOURCE or INFERRED; it needs merge-time normalisation to one value (not decided here). No label correction proposed. |
| 21 | TorrentEngine.lambda$addTorrents$9(boolean,AddTorrentParams) | REACHABLE / INFERRED | PASS | Lambda body inside addTorrents, TorrentEngine.java:342-357; enclosing addTorrents called from FeedDownloaderWorker.java:211. Rx subscribe dispatch unprinted, hence INFERRED. |
| 26 | TorrentEngine.lambda$doStart$6(Logger$DataSetChange) | REACHABLE / mixed SOURCE/INFERRED | PASS (normalisation note) | Body TorrentEngine.java:254-258 (DataSetChanged consumer in doStart, calling printSessionLog for NEW_ENTRIES); doStart anchored at TorrentService.java:131 as row 16. Label REACHABLE correct; confirmed_by is mixed as filed and needs the same merge-time normalisation (not decided here). |
| 31 | TorrentEngine.lambda$observeEngineRunning$4(FlowableEmitter) | REACHABLE / INFERRED | PASS | Flowable.create body of observeEngineRunning, TorrentEngine.java:202-228; enclosing called via observeNeedStartEngine (TorrentEngine.java:182-183) and the row-30 caller set. Rx dispatch unprinted, hence INFERRED. ($n mapping is source-order, not bytecode-verified, as the file itself states; a swap within this flowable would not change the label.) |
| 36 | TorrentEngine.lambda$observeTorrentMetaInfo$18(String,FlowableEmitter) | REACHABLE / INFERRED | PASS | Flowable.create body of observeTorrentMetaInfo, TorrentEngine.java:588-619; caller DetailTorrentViewModel.java:196 (`engine.observeTorrentMetaInfo(torrentId)`). Rx dispatch unprinted, hence INFERRED. |

## Totals

- PASS: 8 / 8 (2 with a confirmed_by-normalisation note only: rows 16, 26). FAIL: 0.
- Proposed corrections: none to any label. Merge-time action owed (not a spot-check fix): normalise rows 16 and 26 to a single confirmed_by value under one project-wide convention.
