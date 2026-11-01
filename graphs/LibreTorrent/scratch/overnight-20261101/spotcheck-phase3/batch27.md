# Spot-check — batch 27 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 27/1 TorrentInfoProvider.lambda$makeInfoListFlowable$5 — REACHABLE INFERRED — PASS. Descriptor match: the handleInfo Runnable in makeInfoListFlowable :242-252; invoked by the $2 listener callbacks :258, :263, :268, :273, :278, :283 and the tag-repo consumer row 3; Rx dispatch INFERRED.
- 27/6 TorrentInfoProvider.lambda$makeInfoListSingle$10 — REACHABLE INFERRED — PASS. Descriptor match (by body, same descriptor as row 7): the Single.create body :311-320; route: info-list-single anchor.
- 27/11 TorrentInfoProvider.lambda$makePeersInfoFlowable$23 — REACHABLE INFERRED — PASS. Descriptor match: the Flowable.create body of makePeersInfoFlowable :391-421; Rx dispatch INFERRED.
- 27/16 TorrentInfoProvider.lambda$makeSessionStatsFlowable$30 — REACHABLE INFERRED — PASS. Descriptor match: the Disposables.fromAction dispose action :492-493 (engine.removeListener(listener), captures the $4 listener); route: session-stats anchor.
- 27/21 TorrentInfoProvider.lambda$makeTrackersInfoFlowable$17 — REACHABLE INFERRED — PASS. Descriptor match: the interval error consumer :373-374; runs only if the interval source errors (caveat stated in row).
- 27/26 TorrentInfoProvider.makeInfoListFlowable() — REACHABLE SOURCE — PASS. Definition :238-308; called by observeInfoList :98-99.
- 27/31 TorrentInfoProvider.makeTorrentsDeletedFlowable() — REACHABLE SOURCE — PASS. Definition :455-472; called by observeTorrentsDeleted :122-123.
- 27/36 TorrentInfoProvider.observePeersInfo(String) — REACHABLE SOURCE — PASS. Definition :114-115 → row 28; called by DetailTorrentViewModel.observePeers :183-184 ← DetailTorrentPeersFragment :174.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
