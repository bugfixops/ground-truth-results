# LibreTorrent batch 36 source audit

Membership is exactly the 40 batch 36 rows printed at the top of `batch_036_helper_printed.txt` from `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. The report preserves uncertainty as OPEN: the evidence includes `TorrentDownloadImpl` bodies, local call sites, the engine wrappers, session construction/alert dispatch, and the `TorrentDownload` interface, but does not establish complete hand-authored entry-to-method routes for these rows. In particular, alert callbacks depend on library dispatch and public getters are reached through engine/session paths whose complete entry chain has not been verified here. No method is labeled UNREACHABLE based only on a missing call-site match.

| # | Method | Finding | Printed source / route gap |
|---:|---|---|---|
| 1 | `TorrentDownloadImpl.getETA()J` | OPEN | `TorrentDownloadImpl.java:1167`; engine caller shown, full entry chain unresolved. |
| 2 | `TorrentDownloadImpl.getErrorMsg(Alert)Pair` | OPEN | `TorrentDownloadImpl.java:304-388`; local alert-processing call shown, upstream alert dispatch unresolved. |
| 3 | `TorrentDownloadImpl.getFileIndicesBep53(Priority[])String` | OPEN | `TorrentDownloadImpl.java:1015-1051`; local caller shown, full entry chain unresolved. |
| 4 | `TorrentDownloadImpl.getFilePieces(TorrentInfo,int)Pair` | OPEN | `TorrentDownloadImpl.java:1537+`; internal callers shown, complete public entry route unresolved. |
| 5 | `TorrentDownloadImpl.getFilePriorities()Priority[]` | OPEN | `TorrentDownloadImpl.java:1641+`; engine caller shown, full entry chain unresolved. |
| 6 | `TorrentDownloadImpl.getFilesAvailability(int[])double[]` | OPEN | `TorrentDownloadImpl.java:1481+`; engine caller shown, full entry chain unresolved. |
| 7 | `TorrentDownloadImpl.getFilesReceivedBytes()long[]` | OPEN | `TorrentDownloadImpl.java:1238+`; engine caller shown, full entry chain unresolved. |
| 8 | `TorrentDownloadImpl.getInfoHash()String` | OPEN | `TorrentDownloadImpl.java:1340+`; implementation printed, no complete entry route verified. |
| 9 | `TorrentDownloadImpl.getNumDownloadedPieces()int` | OPEN | `TorrentDownloadImpl.java:1256+`; engine caller shown, full entry chain unresolved. |
| 10 | `TorrentDownloadImpl.getPartsFile()Uri` | OPEN | `TorrentDownloadImpl.java:1284+`; implementation printed, no complete entry route verified. |
| 11 | `TorrentDownloadImpl.getPeerInfoList()List` | OPEN | `TorrentDownloadImpl.java:911+`; engine caller shown, full entry chain unresolved. |
| 12 | `TorrentDownloadImpl.getPiecesAvailability()int[]` | OPEN | `TorrentDownloadImpl.java:1516+`; engine caller shown, full entry chain unresolved. |
| 13 | `TorrentDownloadImpl.getProgress()int` | OPEN | `TorrentDownloadImpl.java:696`; engine caller shown, full entry chain unresolved. |
| 14 | `TorrentDownloadImpl.getReceivedBytes()long` | OPEN | `TorrentDownloadImpl.java:801`; engine caller shown, full entry chain unresolved. |
| 15 | `TorrentDownloadImpl.getSeedingTime()long` | OPEN | `TorrentDownloadImpl.java:795`; engine caller shown, full entry chain unresolved. |
| 16 | `TorrentDownloadImpl.getShareRatio()double` | OPEN | `TorrentDownloadImpl.java:1262`; implementation printed, full entry chain unresolved. |
| 17 | `TorrentDownloadImpl.getStateCode()TorrentStateCode` | OPEN | `TorrentDownloadImpl.java:1346+`; engine caller shown, full entry chain unresolved. |
| 18 | `TorrentDownloadImpl.getStream(int)TorrentStream` | OPEN | `TorrentDownloadImpl.java:1607+`; engine wrapper shown, complete UI/stream entry route unresolved. |
| 19 | `TorrentDownloadImpl.getTorrentMetaInfo()TorrentMetaInfo` | OPEN | `TorrentDownloadImpl.java:1186+`; engine caller shown, full entry chain unresolved. |
| 20 | `TorrentDownloadImpl.getTorrentName()String` | OPEN | `TorrentDownloadImpl.java:1207+`; implementation printed, no complete entry route verified. |
| 21 | `TorrentDownloadImpl.getTotalLeechers()int` | OPEN | `TorrentDownloadImpl.java:860`; engine caller shown, full entry chain unresolved. |
| 22 | `TorrentDownloadImpl.getTotalPeers()int` | OPEN | `TorrentDownloadImpl.java:836`; engine caller shown, full entry chain unresolved. |
| 23 | `TorrentDownloadImpl.getTotalSeeds()int` | OPEN | `TorrentDownloadImpl.java:848`; engine caller shown, full entry chain unresolved. |
| 24 | `TorrentDownloadImpl.getTotalSentBytes()long` | OPEN | `TorrentDownloadImpl.java:807`; engine caller shown, full entry chain unresolved. |
| 25 | `TorrentDownloadImpl.getTotalWanted()long` | OPEN | `TorrentDownloadImpl.java:955`; engine caller shown, full entry chain unresolved. |
| 26 | `TorrentDownloadImpl.getTrackerInfoList()List` | OPEN | `TorrentDownloadImpl.java:896`; engine caller shown, full entry chain unresolved. |
| 27 | `TorrentDownloadImpl.getTrackersUrl()Set` | OPEN | `TorrentDownloadImpl.java:881`; engine caller shown, full entry chain unresolved. |
| 28 | `TorrentDownloadImpl.getUploadSpeed()long` | OPEN | `TorrentDownloadImpl.java:765`; engine caller shown, full entry chain unresolved. |
| 29 | `TorrentDownloadImpl.getUploadSpeedLimit()int` | OPEN | `TorrentDownloadImpl.java:1334+`; engine caller shown, full entry chain unresolved. |
| 30 | `TorrentDownloadImpl.handleMetadata(MetadataReceivedAlert)V` | OPEN | `TorrentDownloadImpl.java:263,391+`; inner alert dispatch shown, registration and library delivery not independently established. |
| 31 | `TorrentDownloadImpl.handleReadPiece(ReadPieceAlert)V` | OPEN | `TorrentDownloadImpl.java:272,442+`; inner alert dispatch shown, registration and library delivery not independently established. |
| 32 | `TorrentDownloadImpl.handleTorrentChecked()V` | OPEN | `TorrentDownloadImpl.java:275,472+`; inner alert dispatch shown, registration and library delivery not independently established. |
| 33 | `TorrentDownloadImpl.handleTorrentFinished()V` | OPEN | `TorrentDownloadImpl.java:232,478+`; inner alert dispatch shown, registration and library delivery not independently established. |
| 34 | `TorrentDownloadImpl.hasMetadata()Z` | OPEN | `TorrentDownloadImpl.java:200-203`; internal callers printed; complete route to callers unresolved. |
| 35 | `TorrentDownloadImpl.hasMissingFiles()Z` | OPEN | `TorrentDownloadImpl.java:1707+`; session caller shown, complete session entry route unresolved. |
| 36 | `TorrentDownloadImpl.havePiece(int)Z` | OPEN | `TorrentDownloadImpl.java:1553+`; stream caller shown, complete stream/server entry route unresolved. |
| 37 | `TorrentDownloadImpl.indicesToStr(int,int)String` | OPEN | `TorrentDownloadImpl.java:1033-1057`; called by `getFileIndicesBep53`, whose route is unresolved. |
| 38 | `TorrentDownloadImpl.isFinished()Z` | OPEN | `TorrentDownloadImpl.java:1410+`; body and local uses printed, complete entry route unresolved. |
| 39 | `TorrentDownloadImpl.isFirstLastPiecePriority()Z` | OPEN | `TorrentDownloadImpl.java:1105+`; engine caller shown, full entry chain unresolved. |
| 40 | `TorrentDownloadImpl.isPaused()Z` | OPEN | `TorrentDownloadImpl.java:1392+`; engine/local callers shown, full entry chain unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
