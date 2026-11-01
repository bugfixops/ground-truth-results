# Spot-check — batch 38 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 38/1 TorrentDownloadImpl.setMaxUploads — REACHABLE SOURCE — PASS. TorrentSessionImpl.java:1435 (newTask) and :831 (setMaxUploadsPerTorrent, called from TorrentEngine.java:1493).
- 38/6 TorrentDownloadImpl.torrentRemoved — REACHABLE INFERRED — PASS. TorrentDownloadImpl.java:235, InnerListener.alert TORRENT_REMOVED case; alert dispatch library INFERRED; body :456-461 calls notifyListeners + forceStop().
- 38/11 TorrentDownloadImpl$InnerListener.alert — REACHABLE INFERRED — PASS. Library alert dispatch to InnerListener, registered in the TorrentDownloadImpl ctor (:165-166); switch body TorrentDownloadImpl.java:214-281.
- 38/16 TorrentDownloadImpl$InnerListener.types — REACHABLE INFERRED — PASS. TorrentDownloadImpl.java:208-211, returns INNER_LISTENER_TYPES; library call to types() on the registered listener, dispatch not printed from library source.
- 38/21 TorrentSessionImpl.addTorrent — REACHABLE SOURCE — PASS. TorrentEngine calls session.addTorrent (prior proposal anchors :351/:412); internally calls download(torrent.id, params, bencode) at TorrentSessionImpl.java:310, verified fresh.
- 38/26 TorrentSessionImpl.applySettingsPack — REACHABLE SOURCE — PASS. TorrentSessionImpl.java:1002 (onAfterStart) and :1398 (applySettings, row 25).
- 38/31 TorrentSessionImpl.convertProxyType — REACHABLE SOURCE — PASS. TorrentSessionImpl.java:1286, inside settingsToSettingsPack() (applyProxy, :1284-1286).
- 38/36 TorrentSessionImpl.disableIpFilter — REACHABLE SOURCE — PASS. TorrentEngine.java:1560, `session.disableIpFilter()` (verified fresh in the TorrentEngine print, :1554-1561 preference-change branch).

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
