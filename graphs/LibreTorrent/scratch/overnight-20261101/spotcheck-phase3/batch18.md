# Spot-check — batch 18 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 18/1 libretorrent.DataBinderMapperImpl$InnerBrLookup.\<clinit\> — REACHABLE INFERRED — PASS. The cell's final substantive statement is the applied decision: "REVISION 2026-11-01 Phase 1c (D8, M-dispatch): applied — DataBindingUtil request through the generated mapper counts as a route for mapper load/instantiation/dispatch-entry methods; generated dispatch unprinted, hence INFERRED". Earlier "Still OPEN"/"stays OPEN" sentences are dated revision history superseded by that applied decision (contrast Phase 3 flips, where only a bare "verdict applied" note was appended). The row correctly refuses to copy batch 12's databinding.DataBinderMapperImpl conclusion (different package/class).
- 18/6 MainApplication.lambda$onCreate$0 — REACHABLE INFERRED — PASS. Body at :62-64 (Thread.setDefaultUncaughtExceptionHandler…); dispatch on an uncaught exception is unprinted, hence INFERRED.
- 18/11 FeedParser.getItems — REACHABLE SOURCE — PASS. Definition :89-116; external call FeedFetcherWorker.java:165.
- 18/16 FeedParser.watchGuid — REACHABLE SOURCE — PASS. Definition :254-261; internal call findDownloadUrl :159.
- 18/21 HttpConnection.run — REACHABLE SOURCE — PASS. Direct call Utils.java:512 (not a Thread start, so SOURCE, not INFERRED).
- 18/26 InputFilterRange.getMax — UNREACHABLE no_trigger_in_app INFERRED — PASS. Prior OPEN verdict superseded on a saved full-tree grep (fresh InputFilterRange.java, 115 lines, SHA da75ba2b…).
- 18/31 InputFilterRange$Builder.setMax — REACHABLE SOURCE — PASS. Call at LogSettingsFragment:62 (.setMax(Integer.MAX_VALUE)).
- 18/36 RepositoryHelper.getTorrentRepository — REACHABLE SOURCE — PASS. Definition RepositoryHelper.java:43; call TorrentEngine.java:130.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
