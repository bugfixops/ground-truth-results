# Spot-check — batch 35 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 35/1 SessionLogger.applyFilterParams — REACHABLE INFERRED — PASS. TSI:1419 sessionLogger.applyFilterParams(…) inside applySessionLoggerFilters, Completable.fromRunnable at TSI:1418, subscribeOn :1426, subscribe :1427; called from applySettings route.
- 35/6 SessionLogger$SessionLogFilter.\<init\> — REACHABLE INFERRED — PASS. SL:78 SessionLogFilter(LogFilter) ctor; invoked during \<clinit\> for each constant, each holding a NewFilter(name(), filter) (constants SL:66-74; NewFilter construction SL:80).
- 35/11 SessionLogger$SessionLogFilter.lambda$static$3 — REACHABLE INFERRED — PASS. SL:72 PORTMAP lambda; same LOG.applyFilters route as row 8. Index by source order, NOT bytecode-verified (stated in row).
- 35/16 TorrentCriticalWork.observeStateChanging — REACHABLE INFERRED — PASS. TDI:550 criticalWork.observeStateChanging() inside requestStop (batch 37 row 28), reached via TSI requestStop :911-918 → TSI:924 .map(TorrentDownload::requestStop); Rx subscribe dispatch unprinted.
- 35/21 TorrentDownloadImpl.\<clinit\> — REACHABLE INFERRED — PASS. JVM class initialisation on first construction via TSI newTask :1432.
- 35/26 TorrentDownloadImpl.applyFirstLastPiecePriority(boolean,Priority[]) — REACHABLE SOURCE — PASS. TDI:740 prioritizeFiles calls applyFirstLastPiecePriority(true, priorities); TDI:1110 the 1-arg overload calls the 2-arg overload.
- 35/31 TorrentDownloadImpl.forceRecheck — REACHABLE SOURCE — PASS. TE:516 task.forceRecheck(); also TDI:664 doResume path calls forceRecheck().
- 35/36 TorrentDownloadImpl.getConnectedLeechers — REACHABLE SOURCE — PASS. TE:857 task.getConnectedLeechers() in makeAdvancedInfoSync.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
