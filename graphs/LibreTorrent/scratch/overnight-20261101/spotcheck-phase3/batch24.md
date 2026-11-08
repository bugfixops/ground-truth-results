# Spot-check — batch 24 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited. Caveat carried in several rows ("caller step not printed", carried from the input proposal rather than freshly re-fetched) is noted per row; it is a stated evidence limitation, not a contradiction of the label.

## Changed rows (0)

None.

## Sample rows (8)

- 24/1 TorrentEngine.lambda$resumeAll$20 — REACHABLE SOURCE-for-subscribe / INFERRED-for-dispatch — PASS. Runnable body inside TE.resumeAll L661-668, subscribed L667; parent resumeAll (row 29) reached via TS handleActions.
- 24/6 TorrentEngine.loadTorrents() — REACHABLE SOURCE-for-printed-calls / INFERRED-for-session-dispatch — PASS. Definition TE L1085-1092; called by handleOnSessionStarted TE L1060, called by engineListener.onSessionStarted.
- 24/11 TorrentEngine.makeMagnet(String,Z) — REACHABLE SOURCE — PASS. Definition TE L577-586; called by DVM makeMagnet L381-382 (row notes the DVM caller step was not freshly printed in this pass; the citation is carried from the input proposal).
- 24/16 TorrentEngine.observeEngineRunning() — REACHABLE SOURCE-for-printed-call / INFERRED-for-subscription — PASS. Definition TE L202-228; called by the observer route cited in the row.
- 24/21 TorrentEngine.pauseResumeTorrent(String) — REACHABLE SOURCE — PASS. Definition TE L488-505; called by DVM pauseResumeTorrent L357-358 (same carried-citation caveat as row 11).
- 24/26 TorrentEngine.requestStop() — REACHABLE SOURCE — PASS. Definition TE L275-280; called by MVM requestStopEngine L166-167 (same carried-citation caveat as row 11).
- 24/31 TorrentEngine.saveTorrentFileIn(Torrent,Uri) — REACHABLE SOURCE-for-printed-calls / INFERRED-for-session-dispatch — PASS. Definition TE L961-971; called by engineListener.onTorrentAdded TE L1274 and onTorrentFinished route.
- 24/36 TorrentEngine.setFirstLastPiecePriority(String,Z) — REACHABLE SOURCE — PASS. Definition TE L709-719; called by DVM checkParamsChanged L515 (branch L512-516) (same carried-citation caveat as row 11, plus a data-binding dispatch caveat stated in the row).

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
