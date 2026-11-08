# Spot-check — batch 22 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json, plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). Verdicts D1–D36/R1–R5 are NOT re-decided. No work file edited.

## Changed rows (1)

- 22/4 AddTorrentParams$1.newArray — UNREACHABLE no_trigger_in_app INFERRED — FAIL-prose (label, kind, confirmed_by correct per L2 D19: greps/L2/grep_array_apis.txt 0 lines, grep_array_apis2.txt 0 lines, grep_parcelable_array_type.txt 0 lines, grep_array_fields.txt hits only newArray return types; no Bundle/array path names AddTorrentParams in grep_all_parcel_sites.txt; single-extra dispatch never calls newArray). Stale prose: "stays OPEN under undecided policy (xii) — see conditional flip table in round-2 note above" and "REVISION 2026-11-01 Phase 1c (D5a trio policy kept): stays OPEN — no printed app-side parcel/unparcel site names AddTorrentParams".

## Sample rows (8)

- 22/1 AddTorrentParams.writeToParcel — OPEN — PASS. Definition AddTorrentParams.java:96-107 only; zero marshalling sites naming AddTorrentParams in greps/L2/grep_all_parcel_sites.txt. This row is writeToParcel, NOT a $1.\<init\> row, so D22 does not apply (L2 explicit check). OPEN confirmed_by is —, as required.
- 22/6 DownloadsCompletedListener.lambda$listen$0 — REACHABLE INFERRED — PASS. Body DownloadsCompletedListener.java:47-85; subscribed in TorrentEngine.doStart:243-251; Rx dispatch unprinted, hence INFERRED.
- 22/11 DownloadsCompletedListener$1.onTorrentFinished — REACHABLE INFERRED — PASS. Definition :66-70; registration DownloadsCompletedListener.java:81 → TorrentEngine.addListener:307-309 → session.addListener; session invocation is library dispatch, hence INFERRED.
- 22/16 SessionErrorFilter.skip — REACHABLE SOURCE — PASS. Definition SessionErrorFilter.java:30-32; call site TorrentEngine.java:1386 inside engineListener.onSessionError :1385-1389; listener registered at TorrentEngine.java:140.
- 22/21 TorrentEngine.addTorrent(Uri,Uri) — REACHABLE SOURCE — PASS. Definition TorrentEngine.java:363-367 (delegates :364 to row 23); internal call site TorrentEngine.java:360 (row 20).
- 22/26 TorrentEngine.addTorrents — REACHABLE SOURCE — PASS. Definition TorrentEngine.java:342-356; fresh closure: FeedDownloaderWorker.java:211 (engine.addTorrents(paramsList, true)) after the engine-start retry loop.
- 22/31 TorrentEngine.createFetchMagnetSingle — REACHABLE SOURCE — PASS. Definition TorrentEngine.java:431-479 (private); internal call site TorrentEngine.fetchMagnet:422.
- 22/36 TorrentEngine.fetchMagnet — REACHABLE SOURCE — PASS. Definition TorrentEngine.java:415-429; call site AddTorrentViewModel.java:237.

Totals: checked 9 (1 changed + 8 sample-only) — PASS 8, FAIL-prose 1, FAIL-label 0.
