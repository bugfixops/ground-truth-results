# Spot-check — batch 23 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 23/1 TorrentEngine.getDownloadSpeedLimit(String) — REACHABLE SOURCE — PASS. Fresh: DetailTorrentViewModel.java:378; definition TorrentEngine.java:894-902.
- 23/6 TorrentEngine.getPieces(String) — REACHABLE SOURCE — PASS. Fresh: TorrentInfoProvider.java:429 and :442; definition TorrentEngine.java:641.
- 23/11 TorrentEngine.getTorrentVersionList() — REACHABLE SOURCE — PASS. Fresh: CreateTorrentViewModel.java:145 and :339; definition TorrentEngine.java:953-954.
- 23/16 TorrentEngine.handleSettingsChanged(String) — REACHABLE SOURCE-for-subscription / INFERRED-for-emission — PASS. Definition TE L1456-1658 (key-dispatch chain); mixed confirmed_by is stated in the row itself.
- 23/21 TorrentEngine.lambda$addTorrents$9 — REACHABLE INFERRED — PASS. Lambda body in addTorrents, TorrentEngine.java:342-357; enclosing addTorrents REACHABLE via FeedDownloaderWorker.java:211; Rx subscribe dispatch INFERRED.
- 23/26 TorrentEngine.lambda$doStart$6 — REACHABLE SOURCE-for-subscription / INFERRED-for-emission — PASS. Body TE L254-258, consumer of session.getLogger().observeDataSetChanged(); mixed confirmed_by stated in the row.
- 23/31 TorrentEngine.lambda$observeEngineRunning$4 — REACHABLE INFERRED — PASS. observeEngineRunning Flowable.create, TorrentEngine.java:202-228; callers as row 30; dispatch INFERRED.
- 23/36 TorrentEngine.lambda$observeTorrentMetaInfo$18 — REACHABLE INFERRED — PASS. observeTorrentMetaInfo, TorrentEngine.java:588-619; caller DetailTorrentViewModel.java:196; dispatch INFERRED.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
