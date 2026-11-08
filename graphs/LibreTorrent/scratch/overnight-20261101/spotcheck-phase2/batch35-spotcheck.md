# Spot-check — Batch 35 (Stream A Phase 2)

- Work file: `~/workspace/overnight/stream-A/work/batch35-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived from already-fetched local source only (`~/workspace/b353637-src/`, `~/workspace/overnight/stream-A/corpus/java/`). No GitHub connector fetch was needed; no 429 encountered. No edit was made to the work file.
- Phase 1 label changes in this batch: none listed in any dated 2026-11-01 revision note (batch is 40/40 REACHABLE as found). Rows checked = sample rows 1, 6, 11, 16, 21, 26, 31, 36.
- Build / sampler / C1: not run (not this task).

## Per-row verdicts

| Row | Method | Table label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | SessionLogger.applyFilterParams | REACHABLE / INFERRED | PASS | TorrentSessionImpl.java:1419 `sessionLogger.applyFilterParams(new SessionLogger.SessionFilterParams(...))` inside applySessionLoggerFilters (:1416), with Completable.fromRunnable at :1418, subscribeOn at :1426, subscribe at :1427; called from applySettings at :1388 — all exactly as cited. INFERRED is correct because the Rx subscribe dispatch is unprinted. |
| 6 | SessionLogger$SessionLogFilter.<init> | REACHABLE / INFERRED | PASS (label) — citation nit below | Ctor at SessionLogger.java:78–80 (`SessionLogFilter(LogFilter filter) { this.filter = new NewFilter(name(), filter); }`) confirmed. Enum constants are at :66–74 (SESSION, DHT, PEER, PORTMAP, TORRENT), so the row's "(SL:64-77)" range for the constants/NewFilter is imprecise — the NewFilter construction is at :80, not inside 64–77. The mechanism is correct: each constant's initialisation invokes this ctor. Corroborated by printed use at SessionLogger.java:175/180 (`SessionLogFilter.SESSION/DHT.filter()` inside applyFilterParams, row 1's method). INFERRED is correct. |
| 11 | SessionLogger$SessionLogFilter.lambda$static$3 | REACHABLE / INFERRED | PASS (label) — citation nit below | PORTMAP lambda confirmed in SessionLogger.java, but at **:72**, not :71 as the row states (`PORTMAP((entry) -> entry == null || !entry.getTag().equals(SessionLogEntryType.PORTMAP_LOG.name()))`). Same LOG.applyFilters route as row 8 (Logger.java:319 applyFilters). Lambda index is explicitly source-order, NOT bytecode-verified, as the row itself states — that caveat is preserved, not resolved, here. |
| 16 | TorrentCriticalWork.observeStateChanging | REACHABLE / INFERRED | PASS | TorrentDownloadImpl.java:550 `criticalWork.observeStateChanging()` inside requestStop() (:537) — exact; reached via TorrentSessionImpl.requestStop :911–918 and the :924 `.map(TorrentDownload::requestStop)` — both exact. INFERRED (Rx dispatch unprinted) is correct. |
| 21 | TorrentDownloadImpl.<clinit> | REACHABLE / INFERRED | PASS | TorrentSessionImpl.newTask at :1430 constructs `new TorrentDownloadImpl(...)` at :1432 — exact. Class initialisation on first construction is the stated INFERRED convention; convention itself not decided here. |
| 26 | TorrentDownloadImpl.applyFirstLastPiecePriority(boolean,Priority[]) | REACHABLE / SOURCE | PASS | TorrentDownloadImpl.java:740 `applyFirstLastPiecePriority(true, priorities)` inside prioritizeFiles, and :1110 the 1-arg overload calling the 2-arg overload — both exact. |
| 31 | TorrentDownloadImpl.forceRecheck | REACHABLE / SOURCE | PASS | TorrentEngine.java:516 `task.forceRecheck()` and TorrentDownloadImpl.java:664 `forceRecheck()` on the doResume path — both exact. |
| 36 | TorrentDownloadImpl.getConnectedLeechers | REACHABLE / SOURCE | PASS | TorrentEngine.java:857 `task.getConnectedLeechers()` inside makeAdvancedInfoSync — exact. |

## Totals

- Rows checked: 8. **PASS: 8. FAIL: 0.**
- Proposed corrections (citations only, no label change): row 6 — constants at SessionLogger.java:66–74, NewFilter construction at :80 (not ":64-77"); row 11 — PORTMAP lambda at SessionLogger.java:72 (not :71).
