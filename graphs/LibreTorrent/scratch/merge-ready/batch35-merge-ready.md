# LibreTorrent batch 35 — MERGE-READY — UNVERIFIED

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
Status: MERGE-READY PROPOSAL ONLY — UNVERIFIED — NOT MERGED into graph_def.py.
No push was made (pushes held until verified and merged to [L]).
Build: not run. C1: not run (both run on the user's Mac after a push, never claimed passed).
No sampler or full-repo grep was run in this pass. No search_code result was used as
evidence for any row, and no search_code 0 was used as evidence of absence.
No true git clone was attempted: a true git clone fails in this VM (no credential
device) — that check is missing, not passed. Work is via the GitHub connector only.

Membership: exactly the plan rows for batch 35 in handoff/LIBRETORRENT_BATCH_PLAN.tsv
(local copy ~/workspace/agent27-plan.tsv, git blob SHA 0104806dd666c840049b3db52823d4b384fa1c92;
raw sha1 of the same file is afedc8af26f... — the blob SHA is the git hash-object SHA,
verified by the main agent for batches 14-16; the two are the same file, not a mismatch).
Prior proposals (~/workspace/libretorrent-batch35-proposal.md) were leads only; every row
below was re-derived against source freshly fetched in this pass (see "Printed source").

confirmed_by rule used here (per-row, NOT decided project-wide): SOURCE = a printed
app-code line names the method (including an internal call from a REACHABLE method, and
Engine/Session/ViewModel call sites). INFERRED = the route crosses unprinted dispatch:
library alert dispatch (InnerListener registration printed, dispatch body not printed
from library source), Rx/Completable/Observable dispatch, JVM <clinit>/enum
initialisation, thread-pool submit, or listener-interface dispatch. Under a whole-route
INFERRED convention, SOURCE rows crossing unprinted dispatch would read INFERRED;
labels are unaffected.

Strict-entry caveat (undecided convention, NOT decided here): routes in this batch anchor
at TorrentService / TorrentEngine / TorrentSessionImpl / TorrentDownloadImpl /
TorrentInputStream, not at a printed launcher step. The launcher-to-TorrentService step
was NOT printed in this pass. Under a strict printed-launcher-entry rule, all REACHABLE
rows below revert to OPEN. Under the sibling-batch anchor convention they stand as tabled.

Lambda / anonymous $n numbering is source order / plan-signature order, NOT
bytecode-verified; a swap within a group would not change any label, except where a row
is the sole lambda in its method (noted per row).

No UNREACHABLE label is claimed in this batch: no saved full-repo grep was run, so
absence of a caller in the printed files is never treated as evidence of absence.

## Printed source used in this pass (fresh, branch work-2026-10-31, one file at a time
with ~25 s pauses, no fresh HTTP 429, saved in ~/workspace/b353637-src/)

- SessionLogger.java (202 lines, SHA-256 prefix 026218bcf9d1ed9f)
- TorrentCriticalWork.java (98 lines, SHA-256 prefix 03de4d59685388f0)
- TorrentDownloadImpl.java (1,711 lines, SHA-256 prefix 3983914f157b9190)
- TorrentSessionImpl.java (1,720 lines, SHA-256 prefix c2741dabb9100489)
- TorrentEngine.java (1,658 lines, SHA-256 prefix 5845b68c9b83bb6a)
- TorrentInputStream.java (470 lines, SHA-256 prefix 399d13098eee404e)
- Logger.java (538 lines, SHA-256 prefix 4b698cf61c0b9cc7)
All seven files are byte-identical to the prior local copies
(~/workspace/batch35_38/src/ and ~/workspace/agent9/src/TorrentInputStream.java and
~/workspace/batch20_21/src/Logger.java), so prior-proposal line numbers that match these
files are fresh numbers; where a prior number was off, the fresh number is used below
and the correction is noted (batch 35 row 2: TSI send at :1103, gate :1102; batch 35
row 17: TDI setMoving(true) at :1217; batch 37 row 26: TSI task.remove at :391;
batch 37 row 33: TSI task.saveResumeData at :955).
File shorthands in the table: SL=SessionLogger.java, TCW=TorrentCriticalWork.java,
TDI=TorrentDownloadImpl.java, TSI=TorrentSessionImpl.java, TE=TorrentEngine.java,
TIS=TorrentInputStream.java, LOG=Logger.java.

## Table (plan order)

| # | Method | Descriptor | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|---|

| 1 | SessionLogger.applyFilterParams | `(Lorg/proninyaroslav/libretorrent/core/model/session/SessionLogger$SessionFilterParams;)V` | REACHABLE | INFERRED | TSI:1419 sessionLogger.applyFilterParams(new SessionLogger.SessionFilterParams(...)) inside applySessionLoggerFilters, Completable.fromRunnable at TSI:1418, subscribeOn :1426, subscribe :1427; called from applySettings TSI:1388. Rx dispatch unprinted. |
| 2 | SessionLogger.send | `(Lorg/libtorrent4j/alerts/Alert;)V` | REACHABLE | INFERRED | TSI:1103 sessionLogger.send(alert) in InnerListener.alert default case, gate settings.logging TSI:1102; listener registered TSI onBeforeStart :987 (addListener(innerListener)). Alert dispatch is library dispatch, unprinted. |
| 3 | SessionLogger$SessionFilterParams.<init> | `(ZZZZZ)V` | REACHABLE | INFERRED | TSI:1419 new SessionLogger.SessionFilterParams(...) inside the same Rx runnable as row 1 (TSI:1418-1427). |
| 4 | SessionLogger$SessionLogEntryType.<clinit> | `()V` | REACHABLE | INFERRED | SL:36 enum SessionLogEntryType. JVM enum initialisation on first use by SL.send (SL:117), which builds LogEntry values with SessionLogEntryType.*.name(). |
| 5 | SessionLogger$SessionLogFilter.<clinit> | `()V` | REACHABLE | INFERRED | SL:64 enum SessionLogFilter. JVM enum initialisation on first use by SL.applyFilterParams (SL:169-197), which references SESSION/DHT/PEER/PORTMAP/TORRENT. |
| 6 | SessionLogger$SessionLogFilter.<init> | `(Ljava/lang/String;ILorg/proninyaroslav/libretorrent/core/logger/LogFilter;)V` | REACHABLE | INFERRED | SL:78 SessionLogFilter(LogFilter) ctor; invoked during <clinit> for each constant, each holding a NewFilter(name(), filter) (SL:64-77). |
| 7 | SessionLogger$SessionLogFilter.filter | `()Lorg/proninyaroslav/libretorrent/core/logger/Logger$NewFilter;` | REACHABLE | INFERRED | SL:175/:180/:185/:190/:195 SESSION/DHT/PEER/PORTMAP/TORRENT.filter() inside SL.applyFilterParams, reached via the row 1 Rx route. |
| 8 | SessionLogger$SessionLogFilter.lambda$static$0 | `(Lorg/proninyaroslav/libretorrent/core/logger/LogEntry;)Z` | REACHABLE | INFERRED | SL:65 SESSION lambda (entry == null || !entry.getTag().equals(SESSION_LOG.name())); invoked via LOG.applyFilters LOG:319-327 (f.apply(entry) :322). LogFilter interface dispatch unprinted. Lambda index is source order (first constant), NOT bytecode-verified. |
| 9 | SessionLogger$SessionLogFilter.lambda$static$1 | `(Lorg/proninyaroslav/libretorrent/core/logger/LogEntry;)Z` | REACHABLE | INFERRED | SL:67 DHT lambda; same LOG.applyFilters route as row 8. Index source order, NOT bytecode-verified. |
| 10 | SessionLogger$SessionLogFilter.lambda$static$2 | `(Lorg/proninyaroslav/libretorrent/core/logger/LogEntry;)Z` | REACHABLE | INFERRED | SL:69 PEER lambda; same LOG.applyFilters route as row 8. Index source order, NOT bytecode-verified. |
| 11 | SessionLogger$SessionLogFilter.lambda$static$3 | `(Lorg/proninyaroslav/libretorrent/core/logger/LogEntry;)Z` | REACHABLE | INFERRED | SL:71 PORTMAP lambda; same LOG.applyFilters route as row 8. Index source order, NOT bytecode-verified. |
| 12 | SessionLogger$SessionLogFilter.lambda$static$4 | `(Lorg/proninyaroslav/libretorrent/core/logger/LogEntry;)Z` | REACHABLE | INFERRED | SL:73 TORRENT lambda; same LOG.applyFilters route as row 8. Index source order, NOT bytecode-verified. |
| 13 | TorrentCriticalWork.<init> | `()V` | REACHABLE | SOURCE | TDI:139 field criticalWork = new TorrentCriticalWork(); TDI constructed in TSI newTask :1432, called from TSI InnerListener ADD_TORRENT case :1081. |
| 14 | TorrentCriticalWork.emitChangedEvent | `()V` | REACHABLE | SOURCE | TCW.setMoving :68-71 and TCW.setSaveResume :79-85 both call emitChangedEvent(); both setters are REACHABLE (rows 17-18). |
| 15 | TorrentCriticalWork.lambda$emitChangedEvent$0 | `()V` | REACHABLE | INFERRED | TCW.emitChangedEvent :93-97, exec.submit(lambda) :95-96; thread-pool dispatch unprinted. The lambda is the sole lambda in the method ($0 by source order), NOT bytecode-verified. |
| 16 | TorrentCriticalWork.observeStateChanging | `()Lio/reactivex/Observable;` | REACHABLE | INFERRED | TDI:550 criticalWork.observeStateChanging() inside requestStop (batch 37 row 28), reached via TSI requestStop :911-918 -> TSI:924 .map(TorrentDownload::requestStop). Rx subscribe dispatch unprinted. |
| 17 | TorrentCriticalWork.setMoving | `(Z)V` | REACHABLE | SOURCE | TDI:286 criticalWork.setMoving(false) (onStorageMoved); TDI:1217 criticalWork.setMoving(true) (setDownloadPath). |
| 18 | TorrentCriticalWork.setSaveResume | `(Z)V` | REACHABLE | SOURCE | TDI:504 criticalWork.setSaveResume(true) (saveResumeData); TDI:512 and :526 criticalWork.setSaveResume(false). |
| 19 | TorrentCriticalWork$State.<init> | `(ZZJ)V` | REACHABLE | SOURCE | TCW:61 BehaviorSubject.createDefault(new State(false, false, System.currentTimeMillis())) field initialiser; TCW emitChangedEvent :96 new State(...). |
| 20 | TorrentCriticalWork$State.isDuringChange | `()Z` | REACHABLE | INFERRED | TDI:557 state.isDuringChange() inside the requestStop subscribe lambda, via the row 16 route. Rx dispatch unprinted. |
| 21 | TorrentDownloadImpl.<clinit> | `()V` | REACHABLE | INFERRED | TDI <clinit>: JVM class initialisation on first construction via TSI newTask :1432. |
| 22 | TorrentDownloadImpl.<init> | `(Lorg/libtorrent4j/SessionManager;Lorg/proninyaroslav/libretorrent/core/storage/TorrentRepository;Lorg/proninyaroslav/libretorrent/core/system/FileSystemFacade;Ljava/util/Queue;Ljava/lang/String;Lorg/libtorrent4j/TorrentHandle;Z)V` | REACHABLE | SOURCE | TSI:1432 new TorrentDownloadImpl(...) in newTask; newTask called from TSI InnerListener ADD_TORRENT case :1081. |
| 23 | TorrentDownloadImpl.addTrackers | `(Ljava/util/Set;)V` | REACHABLE | SOURCE | TE:574 task.addTrackers(new HashSet<>(urls)). |
| 24 | TorrentDownloadImpl.advancedPeerInfo | `()Ljava/util/List;` | REACHABLE | SOURCE | TDI:917 getPeerInfoList body calls advancedPeerInfo(); TDI:1522 getPiecesAvailability body calls it; both callers REACHABLE (TE:880, TE:844). |
| 25 | TorrentDownloadImpl.applyFirstLastPiecePriority(boolean) | `(Z)V` | REACHABLE | SOURCE | TDI:171 ctor calls applyFirstLastPiecePriority(hasFirstLastPiecePriority); TDI:267 handleMetadata calls it; TDI:1094 setFirstLastPiecePriority calls it. |
| 26 | TorrentDownloadImpl.applyFirstLastPiecePriority(boolean,Priority[]) | `(Z[Lorg/proninyaroslav/libretorrent/core/model/data/Priority;)V` | REACHABLE | SOURCE | TDI:740 prioritizeFiles calls applyFirstLastPiecePriority(true, priorities); TDI:1110 the 1-arg overload calls the 2-arg overload. |
| 27 | TorrentDownloadImpl.checkError | `(Lorg/libtorrent4j/alerts/Alert;)V` | REACHABLE | INFERRED | TDI:278 checkError(alert) in InnerListener.alert default case; listener registered in TDI ctor :166 (sessionManager.addListener(listener)). Alert dispatch is library dispatch, unprinted. |
| 28 | TorrentDownloadImpl.doPause | `()V` | REACHABLE | SOURCE | TDI:599 pause() calls doPause(); TDI:628 pauseManually() calls doPause(). |
| 29 | TorrentDownloadImpl.doResume | `()V` | REACHABLE | SOURCE | TDI:612 resume() calls doResume(); TDI:644 resumeManually() calls doResume(). |
| 30 | TorrentDownloadImpl.doStop | `()V` | REACHABLE | SOURCE | TDI:579 forceStop() calls doStop(); TDI:558 and :566 requestStop subscribe lambdas call doStop(). |
| 31 | TorrentDownloadImpl.forceRecheck | `()V` | REACHABLE | SOURCE | TE:516 task.forceRecheck(); also TDI:664 doResume path calls forceRecheck(). |
| 32 | TorrentDownloadImpl.forceStop | `()V` | REACHABLE | INFERRED | TDI:461 forceStop() inside torrentRemoved (batch 38 row 6), on the alert route (TORRENT_REMOVED case); alert dispatch unprinted. |
| 33 | TorrentDownloadImpl.getActiveTime | `()J` | REACHABLE | SOURCE | TE:853 task.getActiveTime() in makeAdvancedInfoSync. |
| 34 | TorrentDownloadImpl.getAvailability | `([I)D` | REACHABLE | SOURCE | TE:855 task.getAvailability(piecesAvail) in makeAdvancedInfoSync. |
| 35 | TorrentDownloadImpl.getBencode | `()[B` | REACHABLE | SOURCE | TE:935 task.getBencode(). |
| 36 | TorrentDownloadImpl.getConnectedLeechers | `()I` | REACHABLE | SOURCE | TE:857 task.getConnectedLeechers() in makeAdvancedInfoSync. |
| 37 | TorrentDownloadImpl.getConnectedPeers | `()I` | REACHABLE | SOURCE | TE:800 task.getConnectedPeers() in makeInfo. |
| 38 | TorrentDownloadImpl.getConnectedSeeds | `()I` | REACHABLE | SOURCE | TE:850 task.getConnectedSeeds() in makeAdvancedInfoSync. |
| 39 | TorrentDownloadImpl.getDownloadSpeed | `()J` | REACHABLE | SOURCE | TE:795 task.getDownloadSpeed() in makeInfo. |
| 40 | TorrentDownloadImpl.getDownloadSpeedLimit | `()I` | REACHABLE | SOURCE | TE:902 task.getDownloadSpeedLimit(). |

## Counts

- REACHABLE proposed: 40 / 40
- UNREACHABLE proposed: 0 / 40
- OPEN: 0 / 40
- 0 rows verified for merge. Main-agent spot-check (1 in 5), py_compile, build,
  sampler, full-repo grep, and Mac build/C1 are all outstanding and not claimed passed.

## Still owed before merge

- Printed launcher-to-TorrentService step, if the merger requires strict entry routes.
- Bytecode confirmation of lambda $n indices (batch 35 rows 8-12, 15; batch 37 rows 6-16).
- TorrentStreamServer.java re-fetched fresh in the merger's pass if it requires fresh
  evidence for every row: the :206/:243 getTorrentInputStream sites above are CARRIED
  from the batch 23 fresh fetch (~/workspace/b232425-src/), not re-fetched here; the
  Engine side (TE:758-759) IS freshly fetched here.
- Main-agent spot-check, py_compile, build, Mac build/C1.

