# Spot-check — batch 40 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (1, confirmed_by-only)

- 40/3 TorrentSessionImpl.mergeTrackersAndSeeds — UNREACHABLE branch_never_taken INFERRED — PASS. L4 D28 normalisation (SOURCE → INFERRED); label and kind unchanged and correct. Work prose supports the kind: sole printed call is inside mergeTorrent under `if (false)` (TorrentSessionImpl.java:553-556, TODO "temporary disable due to the bug: https://github.com/aldenml/libtorrent4j/pull/244", call at :556); definition :570-588; its own callees extractTrackers/extractUrlSeeds (batch 39 rows 3-4) are UNREACHABLE for the same reason.

## Sample rows (8)

- 40/1 TorrentSessionImpl.loadSettings — REACHABLE SOURCE — PASS. TorrentSessionImpl.java:867, loadSettings() in start() (:862-908); definition :1192-1226.
- 40/6 TorrentSessionImpl.onAfterStart — REACHABLE INFERRED — PASS. Trigger chain printed: TorrentEngine.doStart :259 session.start() → TorrentSessionImpl.start :907 super.start(params) → library dispatch to onAfterStart (TorrentSessionImpl.java:991-1013) INFERRED; body is printed.
- 40/11 TorrentSessionImpl.operationNotAllowed — REACHABLE SOURCE — PASS. TorrentSessionImpl.java:398 (restoreTorrents guard); :1455 (runNextLoadTorrentTask guard); also in fetchMagnet, addTorrent, deleteTorrent guards (e.g. :260, :330, :379).
- 40/16 TorrentSessionImpl.removeListener — REACHABLE SOURCE — PASS. TorrentEngine.java:312, session.removeListener(listener) (re-grepped fresh: also :453, :616); TorrentSessionImpl.java:1036-1037 removeListener calls in onBeforeStop.
- 40/21 TorrentSessionImpl.resumeAll — REACHABLE SOURCE — PASS. TorrentEngine.java:323, session.resumeAll() in rescheduleTorrents.
- 40/26 TorrentSessionImpl.setAutoManaged — REACHABLE SOURCE — PASS. TorrentEngine.java:1579, session.setAutoManaged(pref.autoManage()) on preference change (pref_key_auto_manage branch, :1578-1579).
- 40/31 TorrentSessionImpl.setSettings(SessionSettings) — REACHABLE SOURCE — PASS. TorrentEngine.java session.setSettings(s) sites re-grepped fresh (:1105, :1476, :1481, :1487, :1498, :1503, :1508, :1513, :1518, :1523, :1528, :1533, :1538, :1543, :1605, :1610, :1615, :1620, :1625, :1630, :1635, :1640, :1645, :1653, plus :139 in the 2-arg form, row 32).
- 40/36 TorrentSessionImpl$1.\<init\> — REACHABLE INFERRED — PASS. Anonymous TorrentEngineListener torrentTaskListener, field initialiser at TorrentSessionImpl.java:1053-1059; field initialisers run when a TorrentSessionImpl is constructed (TorrentEngine constructs it, prior proposal anchor :136); anonymous-class numbering inferred from source order (first anonymous class — stated in row).

Totals: checked 9 (1 changed + 8 sample-only) — PASS 9, FAIL-prose 0, FAIL-label 0.
