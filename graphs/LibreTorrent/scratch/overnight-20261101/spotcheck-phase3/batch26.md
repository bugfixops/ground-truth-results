# Spot-check — batch 26 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 26/1 TorrentEngine$5.onTorrentFinished(String) — REACHABLE SOURCE — PASS. Override TorrentEngine:1306-1326; notify TorrentDownloadImpl:482-483 inside the TORRENT_FINISHED alert case :231-232; registration TorrentEngine:140; alert dispatch INFERRED (stated in row).
- 26/6 TorrentEngineListener.\<init\> — REACHABLE SOURCE — PASS. Abstract base (73 lines, all callbacks empty); instantiated as part of every printed anonymous `new TorrentEngineListener() {…}` — first via the engineListener field at TorrentEngine:1265 during TorrentEngine construction.
- 26/11 TorrentEngineListener.onReadPiece(String,ReadPieceInfo) — REACHABLE SOURCE — PASS. Notify TorrentDownloadImpl handleReadPiece :452-453; base runs via torrentTaskListener.
- 26/16 TorrentEngineListener.onSessionStopped() — REACHABLE SOURCE — PASS. Notify TorrentSessionImpl onAfterStop :1041-1044; base runs via engineListener (never removed; registered TorrentEngine:140).
- 26/21 TorrentEngineListener.onTorrentMetadataLoaded(String,Exception) — REACHABLE SOURCE — PASS. Notify TorrentDownloadImpl :438-439; base runs via torrentTaskListener (engineListener overrides this one).
- 26/26 TorrentEngineListener.onTorrentResumed(String) — REACHABLE SOURCE — PASS. Notify TorrentDownloadImpl TORRENT_RESUMED case :244-245; base runs via torrentTaskListener.
- 26/31 TorrentInfoProvider.getInstance(Context) — REACHABLE SOURCE — PASS. Definition TorrentInfoProvider:76-87; called from MainViewModel constructor and TorrentService.onCreate:110. (The other overload, getInstance(engine, tagRepo) :63-74, is a batch-3 row, not judged here.)
- 26/36 TorrentInfoProvider.lambda$makeInfoFlowable$0 — REACHABLE INFERRED — PASS. Descriptor match: the handleEvent Consumer in makeInfoFlowable :134-145; invoked from the $1 listener overrides :153, :164, :175, :186, :197 and from row 38, inside makeInfoFlowable, called by observeInfo :94-95 ← DetailTorrentViewModel.observeTorrentInfo :167-168.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
