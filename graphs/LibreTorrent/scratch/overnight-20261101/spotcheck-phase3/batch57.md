# Spot-check — batch 57 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (1, confirmed_by-only)

- 57/5 Utils.buildExactAlarmPermissionRequest(Context) — UNREACHABLE closed_by_api_level INFERRED — PASS. L4 D28 normalisation (SOURCE → INFERRED); label and kind unchanged and correct. Work prose supports the kind (API 27; S = 31): saved 252-file grep confirms exactly two call sites and no other — TorrentNotifier.java :251 inside makeExactAlarmPermissionNotify() (:244), which early-returns when SDK_INT < S (:245-246) — true at API 27, so line :251 is never reached; and Utils :673 inside requestExactAlarmPermission, guarded SDK_INT >= S.

## Sample rows (8)

- 57/1 DateUtils.startOfYesterday — REACHABLE SOURCE — PASS. Fresh DateUtils :135-138; called from TorrentFilterCollection (fresh) :62 inside dateAddedYesterday() lambda (:57-63), returned by Utils :862 getDrawerGroupDateAddedFilter and called from MainActivity (fresh) :596 and :623.
- 57/6 Utils.checkConnectivity — REACHABLE SOURCE — PASS. Fresh Utils :157-162 (calls isNetworkTypeAllowed :161); called internally from fresh Utils :466 inside fetchHttpUrl; upstream fetchHttpUrl route carried from batch 19.
- 57/11 Utils.fetchHttpUrl — REACHABLE SOURCE — PASS. Fresh Utils :462-475 (listener :477-514, connection.run() :512); upstream route carried from batch 19: AddTorrentViewModel.startDecode → TorrentDecodeTask http/https branch → here. Row states "Not re-printed here; merger to re-verify" — a stated evidence limitation, not a contradiction.
- 57/16 Utils.getClipData — REACHABLE SOURCE — PASS. Fresh Utils :290-301; caller carried from batch 77: AddLinkDialog:163-167; not re-printed here (stated in row). Row correctly notes getClipboardText calling getClipData at fresh :305 does not make row 17 reachable.
- 57/21 Utils.getDrawerGroupStatusFilter — REACHABLE SOURCE — PASS. Prior print Utils :837-852; called from MainActivity (fresh) :591 and :615.
- 57/26 Utils.getNavigationDrawerItems — REACHABLE SOURCE — PASS. Prior print Utils :720-802; called from MainActivity (fresh) :248-250 (drawer setup, new DrawerExpandableAdapter(groups, …)).
- 57/31 Utils.getTorrentDownloadPath — REACHABLE SOURCE — PASS. Fresh Utils :638-647; called from FeedDownloaderWorker.java (fresh) :114 inside fetchTorrent() (worker route, batch 23).
- 57/36 Utils.isBatteryCharging — REACHABLE SOURCE — PASS. Fresh Utils :352-360; called from TorrentEngine (fresh) checkPauseTorrents :1037 (onlyCharging branch, negated).

Totals: checked 9 (1 changed + 8 sample-only) — PASS 9, FAIL-prose 0, FAIL-label 0.
