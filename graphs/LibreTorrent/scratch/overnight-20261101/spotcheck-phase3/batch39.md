# Spot-check — batch 39 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (2, both confirmed_by-only)

Both are L4 D28 normalisations (SOURCE → INFERRED); label and kind unchanged and correct; no stale-prose sentence found.

- 39/3 TorrentSessionImpl.extractTrackers — UNREACHABLE branch_never_taken INFERRED — PASS. Work prose supports the kind: only printed caller is mergeTrackersAndSeeds at TorrentSessionImpl.java:581, and mergeTrackersAndSeeds is itself only called inside mergeTorrent under `if (false)` at :553-556 (TODO "temporary disable due to the bug: https://github.com/aldenml/libtorrent4j/pull/244", call at :556); definition :590.
- 39/4 TorrentSessionImpl.extractUrlSeeds — UNREACHABLE branch_never_taken INFERRED — PASS. Same basis as row 3: only caller mergeTrackersAndSeeds at TorrentSessionImpl.java:584, itself only under `if (false)` at :553-556.

## Sample rows (8)

- 39/1 TorrentSessionImpl.enableIpFilter — REACHABLE SOURCE — PASS. TorrentEngine.java:1050 in handleOnSessionStarted (gate pref.enableIpFiltering(), path != null); also :1558, :1566 on preference change; definition TorrentSessionImpl.java:718-760.
- 39/6 TorrentSessionImpl.fetchMagnet(AddTorrentParams) — REACHABLE SOURCE — PASS. Private; called inside fetchMagnet(String) at TorrentSessionImpl.java:433; definition :454. (Row notes the prior proposal's table header showed the return as MagnetInfo; the plan descriptor (AddTorrentParams) is reproduced as authoritative — descriptor note, not a label issue.)
- 39/11 TorrentSessionImpl.getDownloadSpeedLimit — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition TorrentSessionImpl.java:690-695; saved full-tree grep §B: zero session-level callers; TorrentEngine.java:894-902 getDownloadSpeedLimit(id) is the PER-TASK version (task.getDownloadSpeedLimit() at :902), not this method — correctly not conflated.
- 39/16 TorrentSessionImpl.getPieceSizeList — REACHABLE SOURCE — PASS. TorrentEngine.java:950 (`return session.getPieceSizeList()`); definition TorrentSessionImpl.java:972-975.
- 39/21 TorrentSessionImpl.getTotalUpload — REACHABLE SOURCE — PASS. TorrentSessionImpl.java:1176, inside handleStats (per-call-site convention stated in row).
- 39/26 TorrentSessionImpl.handleStats — REACHABLE SOURCE — PASS. TorrentSessionImpl.java:1096, handleStats() in InnerListener.alert (SESSION_STATS case) (per-call-site convention stated in row; alert dispatch INFERRED).
- 39/31 TorrentSessionImpl.isTorrentAlreadyRunning — REACHABLE SOURCE — PASS. TorrentSessionImpl.java:402 in restoreTorrents (:396-424); :1511 in LoadTorrentTask.run.
- 39/36 TorrentSessionImpl.lambda$enableIpFilter$2 — REACHABLE INFERRED — PASS. notifyListeners lambda inside the enableIpFilter thread runnable (TorrentSessionImpl.java:737); notify loop printed; thread + notify dispatch INFERRED.

Totals: checked 10 (2 changed + 8 sample-only) — PASS 10, FAIL-prose 0, FAIL-label 0.
