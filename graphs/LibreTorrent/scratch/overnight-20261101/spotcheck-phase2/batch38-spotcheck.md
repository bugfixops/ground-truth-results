# Spot-check — Batch 38 (Stream A Phase 2)

- Work file: `~/workspace/overnight/stream-A/work/batch38-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived from already-fetched local source only (`~/workspace/b383940-src/`, `~/workspace/overnight/stream-A/corpus/java/`). No GitHub connector fetch was needed; no 429 encountered. No edit was made to the work file.
- Phase 1 label changes in this batch: none listed in any dated 2026-11-01 revision note (the 2026-11-01 notes record only corrections that leave labels unchanged, e.g. rows 9 and 35 confirmed_by flags). Rows checked = sample rows 1, 6, 11, 16, 21, 26, 31, 36.
- Build / sampler / C1: not run (not this task).

## Per-row verdicts

| Row | Method | Table label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | TorrentDownloadImpl.setMaxUploads | REACHABLE / SOURCE | PASS | TorrentSessionImpl.java:1435 `task.setMaxUploads(settings.uploadsLimitPerTorrent)` inside newTask, and :831 `task.setMaxUploads(uploads)` inside setMaxUploadsPerTorrent (:822) — both exact; TorrentEngine.java:1493 `session.setMaxUploadsPerTorrent(...)` on the preference-change branch — exact. |
| 6 | TorrentDownloadImpl.torrentRemoved | REACHABLE / INFERRED | PASS | TorrentDownloadImpl.java:235 `case TORRENT_REMOVED: torrentRemoved();` inside InnerListener.alert — exact; body at :456–461 (`notifyListeners(...)` at :458, `forceStop()` at :461) — exact. INFERRED is correct because the library alert dispatch is unprinted. |
| 11 | TorrentDownloadImpl$InnerListener.alert | REACHABLE / INFERRED | PASS | Listener registered in the TorrentDownloadImpl ctor at :165–166 (`listener = new InnerListener(); sessionManager.addListener(listener)`) — exact; switch body at :214–281 (`public void alert(Alert<?> alert)` at :214 through the closing brace at :281) — exact. INFERRED (library dispatch) is correct. |
| 16 | TorrentDownloadImpl$InnerListener.types | REACHABLE / INFERRED | PASS | TorrentDownloadImpl.java:208–211 (`public int[] types()` at :208, `return INNER_LISTENER_TYPES;` at :210) — exact. INFERRED (library call to types() on the registered listener, dispatch not printed from library source) is correct. |
| 21 | TorrentSessionImpl.addTorrent | REACHABLE / SOURCE | PASS | TorrentEngine.java:351 `session.addTorrent(params, removeFile)` confirmed (row's second anchor :412 not re-checked, not needed); internally TorrentSessionImpl.java:310 `download(torrent.id, params, bencode)` — exact. |
| 26 | TorrentSessionImpl.applySettingsPack | REACHABLE / SOURCE | PASS | TorrentSessionImpl.java:1002 `applySettingsPack(sp)` inside onAfterStart and :1398 inside applySettings — both exact. |
| 31 | TorrentSessionImpl.convertProxyType | REACHABLE / SOURCE | PASS | TorrentSessionImpl.java:1286 `int proxyType = convertProxyType(settings.proxyType, settings.proxyRequiresAuth);` inside applyProxy (:1284–1286) — exact. |
| 36 | TorrentSessionImpl.disableIpFilter | REACHABLE / SOURCE | PASS | TorrentEngine.java:1560 `session.disableIpFilter()` inside the enable-ip-filtering preference-change branch (:1554–1561) — exact. |

## Totals

- Rows checked: 8. **PASS: 8. FAIL: 0.**
- Proposed corrections: none.
