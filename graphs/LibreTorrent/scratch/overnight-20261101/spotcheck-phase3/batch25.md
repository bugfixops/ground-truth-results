# Spot-check — batch 25 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 25/1 TorrentEngine.setTorrentName(String,String) — REACHABLE SOURCE — PASS. Fresh: DetailTorrentViewModel.java:488; definition TorrentEngine.java:670-677.
- 25/6 TorrentEngine.stopStreamingServer() — REACHABLE SOURCE — PASS. Private; called by doStop L298 (anchored at TorrentService.stopEngine() L161), by startStreamingServer itself L1064, and by handleSettingsChanged L1596.
- 25/11 TorrentEngine$1.onSessionStarted() — REACHABLE INFERRED — PASS. Definition TorrentEngine.java:209-212; invoked only via session dispatch to the row-10 listener; dispatch INFERRED, registration as row 10.
- 25/16 TorrentEngine$3.onTorrentMetadataLoaded(String,Exception) — REACHABLE INFERRED — PASS. Definition TorrentEngine.java:592-605; invoked only via session dispatch to the row-15 listener; dispatch INFERRED, registration as row 15.
- 25/21 TorrentEngine$5.lambda$onIpFilterParsed$8 — REACHABLE SOURCE-for-subscribe / INFERRED-for-upstream-dispatch — PASS. Completable.fromRunnable inside onIpFilterParsed (L137x); mixed confirmed_by stated in the row.
- 25/26 TorrentEngine$5.lambda$onTorrentFinished$3 — REACHABLE SOURCE-for-subscribe / INFERRED-for-upstream-dispatch — PASS. Error action of the same subscription as row 25 (L1326-1327); runs when row 39's onTorrentFinished fires.
- 25/31 TorrentEngine$5.lambda$onTorrentMoved$6 — REACHABLE SOURCE-for-subscribe / INFERRED-for-upstream-dispatch — PASS. Success action of the repo.getTorrentByIdSingle(id) subscription inside onTorrentMoved (L1349+).
- 25/36 TorrentEngine$5.onNatError(String) — REACHABLE SOURCE-for-registration / INFERRED-for-dispatch — PASS. Definition L1393-1397; registered via constructor L140.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
