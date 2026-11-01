**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 36 — MERGE-READY — UNVERIFIED

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
Status: MERGE-READY PROPOSAL ONLY — UNVERIFIED — NOT MERGED into graph_def.py.
Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]) (pushed UNVERIFIED before [L] at user request 2026-11-01).
Build: not run. C1: not run (both run on the user's Mac after a push, never claimed passed).
No sampler or full-repo grep was run in this pass. No search_code result was used as
evidence for any row, and no search_code 0 was used as evidence of absence.
No true git clone was attempted: a true git clone fails in this VM (no credential
device) — that check is missing, not passed. Work is via the GitHub connector only.

Membership: exactly the plan rows for batch 36 in handoff/LIBRETORRENT_BATCH_PLAN.tsv
(local copy ~/workspace/agent27-plan.tsv, git blob SHA 0104806dd666c840049b3db52823d4b384fa1c92;
raw sha1 of the same file is afedc8af26f... — the blob SHA is the git hash-object SHA,
verified by the main agent for batches 14-16; the two are the same file, not a mismatch).
Prior proposals (~/workspace/libretorrent-batch36-proposal.md) were leads only; every row
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

| 1 | TorrentDownloadImpl.getETA | `()J` | REACHABLE | SOURCE | TE:797 task.getETA() in makeInfo; internally TDI:1171 getETA body checks getStateCode(). |
| 2 | TorrentDownloadImpl.getErrorMsg | `(Lorg/libtorrent4j/alerts/Alert;)Landroidx/core/util/Pair;` | REACHABLE | INFERRED | TDI:304 getErrorMsg(alert) inside checkError (batch 35 row 27), on the alert route; alert dispatch unprinted. |
| 3 | TorrentDownloadImpl.getFileIndicesBep53 | `([Lorg/libtorrent4j/Priority;)Ljava/lang/String;` | REACHABLE | SOURCE | TDI:1015 getFileIndicesBep53(th.filePriorities()) inside makeMagnet (batch 37 row 17, TE:585). |
| 4 | TorrentDownloadImpl.getFilePieces | `(Lorg/libtorrent4j/TorrentInfo;I)Landroidx/core/util/Pair;` | REACHABLE | SOURCE | TDI:1140 applyFirstLastPiecePriority body calls getFilePieces(ti, index); TDI:1501 and :1617 (getPiecesAvailability / getStream bodies) call it. |
| 5 | TorrentDownloadImpl.getFilePriorities | `()[Lorg/proninyaroslav/libretorrent/core/model/data/Priority;` | REACHABLE | SOURCE | TE:803 task.getFilePriorities() in makeInfo. |
| 6 | TorrentDownloadImpl.getFilesAvailability | `([I)[D` | REACHABLE | SOURCE | TE:856 task.getFilesAvailability(piecesAvail) in makeAdvancedInfoSync. |
| 7 | TorrentDownloadImpl.getFilesReceivedBytes | `()[J` | REACHABLE | SOURCE | TE:848 task.getFilesReceivedBytes() in makeAdvancedInfoSync. |
| 8 | TorrentDownloadImpl.getInfoHash | `()Ljava/lang/String;` | REACHABLE | SOURCE | TDI:1196 getInfoHash() inside getTorrentMetaInfo (row 19, TE:631). |
| 9 | TorrentDownloadImpl.getNumDownloadedPieces | `()I` | REACHABLE | SOURCE | TE:851 task.getNumDownloadedPieces() in makeAdvancedInfoSync. |
| 10 | TorrentDownloadImpl.getPartsFile | `()Landroid/net/Uri;` | REACHABLE | SOURCE | TDI:164 partsFile = getPartsFile() in the ctor (batch 35 row 22). |
| 11 | TorrentDownloadImpl.getPeerInfoList | `()Ljava/util/List;` | REACHABLE | SOURCE | TE:880 task.getPeerInfoList(). |
| 12 | TorrentDownloadImpl.getPiecesAvailability | `()[I` | REACHABLE | SOURCE | TE:844 task.getPiecesAvailability() in makeAdvancedInfoSync. |
| 13 | TorrentDownloadImpl.getProgress | `()I` | REACHABLE | SOURCE | TE:791 task.getProgress() in makeInfo. |
| 14 | TorrentDownloadImpl.getReceivedBytes | `()J` | REACHABLE | SOURCE | TE:792 task.getReceivedBytes() in makeInfo. |
| 15 | TorrentDownloadImpl.getSeedingTime | `()J` | REACHABLE | SOURCE | TE:854 task.getSeedingTime() in makeAdvancedInfoSync. |
| 16 | TorrentDownloadImpl.getShareRatio | `()D` | REACHABLE | SOURCE | TE:852 task.getShareRatio() in makeAdvancedInfoSync. |
| 17 | TorrentDownloadImpl.getStateCode | `()Lorg/proninyaroslav/libretorrent/core/model/data/TorrentStateCode;` | REACHABLE | SOURCE | TE:790 task.getStateCode() in makeInfo; TDI:1171 getETA body checks getStateCode(). |
| 18 | TorrentDownloadImpl.getStream | `(I)Lorg/proninyaroslav/libretorrent/core/model/stream/TorrentStream;` | REACHABLE | SOURCE | TE:755 task.getStream(fileIndex). |
| 19 | TorrentDownloadImpl.getTorrentMetaInfo | `()Lorg/proninyaroslav/libretorrent/core/model/data/metainfo/TorrentMetaInfo;` | REACHABLE | SOURCE | TE:631 task.getTorrentMetaInfo(). |
| 20 | TorrentDownloadImpl.getTorrentName | `()Ljava/lang/String;` | REACHABLE | SOURCE | TDI:1197 getTorrentName() inside getTorrentMetaInfo (row 19). |
| 21 | TorrentDownloadImpl.getTotalLeechers | `()I` | REACHABLE | SOURCE | TE:858 task.getTotalLeechers() in makeAdvancedInfoSync. |
| 22 | TorrentDownloadImpl.getTotalPeers | `()I` | REACHABLE | SOURCE | TE:799 task.getTotalPeers() in makeInfo. |
| 23 | TorrentDownloadImpl.getTotalSeeds | `()I` | REACHABLE | SOURCE | TE:849 task.getTotalSeeds() in makeAdvancedInfoSync. |
| 24 | TorrentDownloadImpl.getTotalSentBytes | `()J` | REACHABLE | SOURCE | TE:793 task.getTotalSentBytes() in makeInfo. |
| 25 | TorrentDownloadImpl.getTotalWanted | `()J` | REACHABLE | SOURCE | TE:794 task.getTotalWanted() in makeInfo. |
| 26 | TorrentDownloadImpl.getTrackerInfoList | `()Ljava/util/List;` | REACHABLE | SOURCE | TE:869 task.getTrackerInfoList(). |
| 27 | TorrentDownloadImpl.getTrackersUrl | `()Ljava/util/Set;` | REACHABLE | SOURCE | TE:551 task.getTrackersUrl(). |
| 28 | TorrentDownloadImpl.getUploadSpeed | `()J` | REACHABLE | SOURCE | TE:796 task.getUploadSpeed() in makeInfo. |
| 29 | TorrentDownloadImpl.getUploadSpeedLimit | `()I` | REACHABLE | SOURCE | TE:891 task.getUploadSpeedLimit(). |
| 30 | TorrentDownloadImpl.handleMetadata | `(Lorg/libtorrent4j/alerts/MetadataReceivedAlert;)V` | REACHABLE | INFERRED | TDI:263 handleMetadata((MetadataReceivedAlert)alert) in InnerListener.alert METADATA_RECEIVED case; alert dispatch unprinted. |
| 31 | TorrentDownloadImpl.handleReadPiece | `(Lorg/libtorrent4j/alerts/ReadPieceAlert;)V` | REACHABLE | INFERRED | TDI:272 handleReadPiece((ReadPieceAlert)alert) in InnerListener.alert READ_PIECE case; alert dispatch unprinted. |
| 32 | TorrentDownloadImpl.handleTorrentChecked | `()V` | REACHABLE | INFERRED | TDI:275 handleTorrentChecked() in InnerListener.alert TORRENT_CHECKED case; alert dispatch unprinted. |
| 33 | TorrentDownloadImpl.handleTorrentFinished | `()V` | REACHABLE | INFERRED | TDI:232 handleTorrentFinished() in InnerListener.alert TORRENT_FINISHED case; alert dispatch unprinted. |
| 34 | TorrentDownloadImpl.hasMetadata | `()Z` | REACHABLE | SOURCE | TDI:719, :747, :1090, :1115, :1286 hasMetadata() guards inside REACHABLE methods (getStream / applyFirstLastPiecePriority / setFirstLastPiecePriority / isValid paths). |
| 35 | TorrentDownloadImpl.hasMissingFiles | `()Z` | REACHABLE | SOURCE | TSI:953 task.hasMissingFiles() inside saveAllResumeData; saveAllResumeData called from TSI requestStop :911-918. |
| 36 | TorrentDownloadImpl.havePiece | `(I)Z` | REACHABLE | SOURCE | FLIPPED from prior OPEN on fresh evidence: TIS:139 task.havePiece(pieceIndex) inside waitForPiece, called from TIS read paths :239 and :335. TIS is constructed by TE getTorrentInputStream :758-759, called from TorrentStreamServer (batch 23 fresh fetch :206/:243, CARRIED here, not re-fetched in this pass). The prior proposal's only-havePiece sites were th.havePiece on the libtorrent handle (TDI:1588/:1598), a different receiver; the TIS task.havePiece site was not printed in that pass. |
| 37 | TorrentDownloadImpl.indicesToStr | `(II)Ljava/lang/String;` | REACHABLE | SOURCE | TDI:1033 and :1043 indicesToStr(startIndex, endIndex) inside getFileIndicesBep53 (row 3). |
| 38 | TorrentDownloadImpl.isFinished | `()Z` | REACHABLE | SOURCE | TDI:759 getDownloadSpeed body uses isFinished(); TDI:767 getUploadSpeed body uses isFinished(); both TE-called (TE:795-796). |
| 39 | TorrentDownloadImpl.isFirstLastPiecePriority | `()Z` | REACHABLE | SOURCE | TE:731 task.isFirstLastPiecePriority(). |
| 40 | TorrentDownloadImpl.isPaused() | `()Z` | REACHABLE | SOURCE | TE:494 task.isPaused(); also TDI:1351 and :1392 internal paths. Distinct from the isPaused(TorrentStatus) overload in batch 37 row 1. |

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

