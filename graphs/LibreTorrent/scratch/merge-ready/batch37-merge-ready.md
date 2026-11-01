**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 37 — MERGE-READY — UNVERIFIED

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
Status: MERGE-READY PROPOSAL ONLY — UNVERIFIED — NOT MERGED into graph_def.py.
Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]) (pushed UNVERIFIED before [L] at user request 2026-11-01).
Build: not run. C1: not run (both run on the user's Mac after a push, never claimed passed).
No sampler or full-repo grep was run in this pass. No search_code result was used as
evidence for any row, and no search_code 0 was used as evidence of absence.
No true git clone was attempted: a true git clone fails in this VM (no credential
device) — that check is missing, not passed. Work is via the GitHub connector only.

Membership: exactly the plan rows for batch 37 in handoff/LIBRETORRENT_BATCH_PLAN.tsv
(local copy ~/workspace/agent27-plan.tsv, git blob SHA 0104806dd666c840049b3db52823d4b384fa1c92;
raw sha1 of the same file is afedc8af26f... — the blob SHA is the git hash-object SHA,
verified by the main agent for batches 14-16; the two are the same file, not a mismatch).
Prior proposals (~/workspace/libretorrent-batch37-proposal.md) were leads only; every row
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

| 1 | TorrentDownloadImpl.isPaused(TorrentStatus) | `(Lorg/libtorrent4j/TorrentStatus;)Z` | REACHABLE | SOURCE | TDI:1358 boolean isPaused = isPaused(status) inside getStateCode (TE:790). Distinct from the no-arg isPaused() in batch 36 row 40. |
| 2 | TorrentDownloadImpl.isSeeding | `()Z` | REACHABLE | SOURCE | TDI:759 getDownloadSpeed body uses isSeeding(); TDI:767 getUploadSpeed body uses isSeeding(); both TE-called (TE:795-796). |
| 3 | TorrentDownloadImpl.isSequentialDownload | `()Z` | REACHABLE | SOURCE | TE:802 task.isSequentialDownload() in makeInfo; TE:946 isSequentialDownload(). |
| 4 | TorrentDownloadImpl.isStopped | `()Z` | REACHABLE | SOURCE | TE:778 makeInfo guard: if (task == null || !task.isValid() || task.isStopped()). |
| 5 | TorrentDownloadImpl.isValid | `()Z` | REACHABLE | SOURCE | TE:778 makeInfo guard: if (task == null || !task.isValid() || task.isStopped()). |
| 6 | TorrentDownloadImpl.lambda$checkError$1 | `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | TDI:334 notifyListeners lambda inside checkError (batch 35 row 27); listener dispatch unprinted. $1 by source order, NOT bytecode-verified. |
| 7 | TorrentDownloadImpl.lambda$handleMetadata$2 | `(Ljava/lang/Exception;Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | TDI:422 notifyListeners lambda (error path) inside handleMetadata (batch 36 row 30); listener dispatch unprinted. $2/$3 pair with row 8, indices NOT bytecode-verified. |
| 8 | TorrentDownloadImpl.lambda$handleMetadata$3 | `([Ljava/lang/Exception;Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | TDI:438 notifyListeners lambda (metadata-loaded path) inside handleMetadata; listener dispatch unprinted. Indices NOT bytecode-verified. |
| 9 | TorrentDownloadImpl.lambda$handleReadPiece$4 | `(Lorg/proninyaroslav/libretorrent/core/model/data/ReadPieceInfo;Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | TDI:452 notifyListeners lambda inside handleReadPiece (batch 36 row 31); listener dispatch unprinted. Index NOT bytecode-verified. |
| 10 | TorrentDownloadImpl.lambda$handleTorrentFinished$6 | `(Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | TDI:482 notifyListeners lambda inside handleTorrentFinished (batch 36 row 33); listener dispatch unprinted. Index NOT bytecode-verified. |
| 11 | TorrentDownloadImpl.lambda$onStorageMoved$0 | `(ZLorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | TDI:287 notifyListeners((listener) -> listener.onTorrentMoved(id, success)) inside onStorageMoved; listener dispatch unprinted. $0 matches the single lambda in that method, NOT bytecode-verified. |
| 12 | TorrentDownloadImpl.lambda$requestStop$7 | `(Ljava/util/concurrent/atomic/AtomicLong;Lio/reactivex/CompletableEmitter;Lorg/proninyaroslav/libretorrent/core/model/session/TorrentCriticalWork$State;)V` | REACHABLE | INFERRED | TDI:545 Completable.create lambda inside requestStop; Rx dispatch unprinted. Index NOT bytecode-verified. |
| 13 | TorrentDownloadImpl.lambda$requestStop$8 | `(Lio/reactivex/CompletableEmitter;Ljava/lang/Throwable;)V` | REACHABLE | INFERRED | TDI:552-563 subscribe onNext lambda inside requestStop (state.isDuringChange() -> doStop()); Rx dispatch unprinted. Index NOT bytecode-verified. |
| 14 | TorrentDownloadImpl.lambda$requestStop$9 | `(Lio/reactivex/CompletableEmitter;)V` | REACHABLE | INFERRED | TDI:565-571 subscribe onError lambda inside requestStop (doStop() on error); Rx dispatch unprinted. Index NOT bytecode-verified. |
| 15 | TorrentDownloadImpl.lambda$setDownloadPath$10 | `(Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | TDI:1226 notifyListeners((listener) -> listener.onTorrentMoving(id)) inside setDownloadPath; listener dispatch unprinted. Index NOT bytecode-verified. |
| 16 | TorrentDownloadImpl.lambda$torrentRemoved$5 | `(Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V` | REACHABLE | INFERRED | TDI:458 notifyListeners lambda inside torrentRemoved (batch 38 row 6); listener dispatch unprinted. Index NOT bytecode-verified. |
| 17 | TorrentDownloadImpl.makeMagnet | `(Z)Ljava/lang/String;` | REACHABLE | SOURCE | TE:585 task.makeMagnet(includePriorities); internally TDI:1015 getFileIndicesBep53. |
| 18 | TorrentDownloadImpl.notifyListeners | `(Lorg/proninyaroslav/libretorrent/core/model/session/TorrentDownloadImpl$CallListener;)V` | REACHABLE | SOURCE | TDI notifyListeners called from many REACHABLE methods: TDI:226/:238/:244/:259 (InnerListener.alert), :287, :334, :422, :438, :452, :458, :482, :1226. |
| 19 | TorrentDownloadImpl.onStorageMoved | `(Z)V` | REACHABLE | INFERRED | TDI:251 onStorageMoved(true) and :254 onStorageMoved(false) in InnerListener.alert STORAGE_MOVED cases; alert dispatch unprinted. |
| 20 | TorrentDownloadImpl.operationNotAllowed | `()Z` | REACHABLE | SOURCE | TDI:1555 havePiece body, :1560-1561 readPiece body, :1588/:1598 setInterestedPieces bodies all call operationNotAllowed(); those three methods are REACHABLE (batch 36 row 36; rows 25 and 39 below). |
| 21 | TorrentDownloadImpl.pause | `()V` | REACHABLE | SOURCE | TE:1283, :1298, :1448 task.pause(); also TDI:331 checkError body and :421 handleMetadata body call pause(). |
| 22 | TorrentDownloadImpl.pauseManually | `()V` | REACHABLE | SOURCE | TE:497 task.pauseManually(). |
| 23 | TorrentDownloadImpl.pieces | `()[Z` | REACHABLE | SOURCE | TE:649 task.pieces(). |
| 24 | TorrentDownloadImpl.prioritizeFiles | `([Lorg/proninyaroslav/libretorrent/core/model/data/Priority;)V` | REACHABLE | SOURCE | TE:741 task.prioritizeFiles(priorities); internally TDI:740 applyFirstLastPiecePriority(true, priorities). |
| 25 | TorrentDownloadImpl.readPiece | `(I)V` | REACHABLE | SOURCE | FLIPPED from prior OPEN on fresh evidence: TIS:242 task.readPiece(p) (read(int) path) and TIS:338 task.readPiece(p) (read(byte[]) path), each after waitForPiece. TIS is constructed by TE getTorrentInputStream :758-759, called from TorrentStreamServer (batch 23 fresh fetch :206/:243, CARRIED here, not re-fetched in this pass). Prior proposal printed only the definition (TDI:1559-1567) and no caller. |
| 26 | TorrentDownloadImpl.remove | `(Z)V` | REACHABLE | SOURCE | TSI:391 task.remove(withFiles) inside deleteTorrent; TSI deleteTorrent called from TE:539 session.deleteTorrent(id, withFiles). |
| 27 | TorrentDownloadImpl.replaceTrackers | `(Ljava/util/Set;)V` | REACHABLE | SOURCE | TE:554 and :565 task.replaceTrackers(...). |
| 28 | TorrentDownloadImpl.requestStop | `()Lio/reactivex/Completable;` | REACHABLE | INFERRED | TSI:924 .map(TorrentDownload::requestStop) inside stopTasks; TSI requestStop :911-918 called from TE:299 session.requestStop(). Rx map dispatch unprinted. |
| 29 | TorrentDownloadImpl.requestTrackerAnnounce | `()V` | REACHABLE | SOURCE | TE:529 task.requestTrackerAnnounce(). |
| 30 | TorrentDownloadImpl.resetTorrentError | `()V` | REACHABLE | INFERRED | TDI:242 resetTorrentError() in InnerListener.alert TORRENT_RESUMED case; alert dispatch unprinted. |
| 31 | TorrentDownloadImpl.resume | `()V` | REACHABLE | INFERRED | TDI:320 resume() inside checkError (batch 35 row 27), on the alert route; alert dispatch unprinted. |
| 32 | TorrentDownloadImpl.resumeManually | `()V` | REACHABLE | SOURCE | TE:495 task.resumeManually(). |
| 33 | TorrentDownloadImpl.saveResumeData | `(Z)V` | REACHABLE | SOURCE | TSI:955 task.saveResumeData(false) inside saveAllResumeData; saveAllResumeData called from TSI requestStop :911-918 (TSI:916). |
| 34 | TorrentDownloadImpl.serializeResumeData | `(Lorg/libtorrent4j/alerts/SaveResumeDataAlert;)V` | REACHABLE | INFERRED | TDI:248 serializeResumeData((SaveResumeDataAlert)alert) in InnerListener.alert SAVE_RESUME_DATA case; alert dispatch unprinted. |
| 35 | TorrentDownloadImpl.setAutoManaged | `(Z)V` | REACHABLE | SOURCE | FLIPPED from prior OPEN on fresh evidence: TSI:843 task.setAutoManaged(autoManaged) inside the session-level setAutoManaged (TSI:836-844), called from TE:1579 (pref_key_auto_manage branch: session.setAutoManaged(pref.autoManage())). The prior proposal's claim that the Engine/Session sites are 'different receivers, not this TorrentDownload method' was wrong: the session method delegates to this task method over all torrentTasks. The session-level method itself is a different plan row (not in batches 35-37) and is not judged here. |
| 36 | TorrentDownloadImpl.setDownloadPath | `(Landroid/net/Uri;)V` | REACHABLE | SOURCE | TE:690 task.setDownloadPath(path); internally TDI:1217 criticalWork.setMoving(true). |
| 37 | TorrentDownloadImpl.setDownloadSpeedLimit | `(I)V` | REACHABLE | SOURCE | TE:913 task.setDownloadSpeedLimit(limit). |
| 38 | TorrentDownloadImpl.setFirstLastPiecePriority | `(Z)V` | REACHABLE | SOURCE | TE:716 task.setFirstLastPiecePriority(enabled); internally TDI:1094 applyFirstLastPiecePriority(enabled). |
| 39 | TorrentDownloadImpl.setInterestedPieces | `(Lorg/proninyaroslav/libretorrent/core/model/stream/TorrentStream;II)V` | REACHABLE | SOURCE | FLIPPED from prior OPEN on fresh evidence: TIS:118 task.setInterestedPieces(stream, stream.firstFilePiece, 1) in the TorrentInputStream ctor; also TIS read paths :217, :288, :394. TIS is constructed by TE getTorrentInputStream :758-759, called from TorrentStreamServer (batch 23 fresh fetch :206/:243, CARRIED here, not re-fetched in this pass). Prior proposal printed only the definition (TDI:1574-1605) and no caller. |
| 40 | TorrentDownloadImpl.setMaxConnections | `(I)V` | REACHABLE | SOURCE | TSI:817 task.setMaxConnections(connections) inside setMaxConnectionsPerTorrent (TSI:808-818); TSI:1434 newTask also sets task.setMaxConnections; the session method is called from TE:1490. |

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

