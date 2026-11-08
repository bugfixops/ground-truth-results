# LibreTorrent batch 36 source audit

Membership is the exact 40-row set in `scratch/batch_036_plan.txt`. I checked the helper's `TorrentDownloadImpl`, engine wrapper, session/alert dispatch, and interface excerpts in `scratch/batch_036_helper_printed.txt`. Local engine calls and registered alert listeners are present, but complete hand-authored routes from app entries are not. Alert callbacks also depend on library dispatch. No row is labeled unreachable based only on a missing call-site match.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentDownloadImpl.getETA()` | OPEN | Engine caller shown; entry chain unresolved. |
| 2 | `TorrentDownloadImpl.getErrorMsg(Alert)` | OPEN | Local alert-processing call shown; upstream alert dispatch unresolved. |
| 3 | `TorrentDownloadImpl.getFileIndicesBep53(Priority[])` | OPEN | Local caller shown; app-entry route unresolved. |
| 4 | `TorrentDownloadImpl.getFilePieces(TorrentInfo,int)` | OPEN | Internal callers shown; complete public entry route unresolved. |
| 5 | `TorrentDownloadImpl.getFilePriorities()` | OPEN | Engine caller shown; entry chain unresolved. |
| 6 | `TorrentDownloadImpl.getFilesAvailability(int[])` | OPEN | Engine caller shown; entry chain unresolved. |
| 7 | `TorrentDownloadImpl.getFilesReceivedBytes()` | OPEN | Engine caller shown; entry chain unresolved. |
| 8 | `TorrentDownloadImpl.getInfoHash()` | OPEN | Implementation printed; complete entry route not verified. |
| 9 | `TorrentDownloadImpl.getNumDownloadedPieces()` | OPEN | Engine caller shown; entry chain unresolved. |
| 10 | `TorrentDownloadImpl.getPartsFile()` | OPEN | Implementation printed; complete entry route not verified. |
| 11 | `TorrentDownloadImpl.getPeerInfoList()` | OPEN | Engine caller shown; entry chain unresolved. |
| 12 | `TorrentDownloadImpl.getPiecesAvailability()` | OPEN | Engine caller shown; entry chain unresolved. |
| 13 | `TorrentDownloadImpl.getProgress()` | OPEN | Engine caller shown; entry chain unresolved. |
| 14 | `TorrentDownloadImpl.getReceivedBytes()` | OPEN | Engine caller shown; entry chain unresolved. |
| 15 | `TorrentDownloadImpl.getSeedingTime()` | OPEN | Engine caller shown; entry chain unresolved. |
| 16 | `TorrentDownloadImpl.getShareRatio()` | OPEN | Engine caller shown; entry chain unresolved. |
| 17 | `TorrentDownloadImpl.getStateCode()` | OPEN | Engine caller shown; entry chain unresolved. |
| 18 | `TorrentDownloadImpl.getStream(int)` | OPEN | Engine wrapper shown; UI/stream entry route unresolved. |
| 19 | `TorrentDownloadImpl.getTorrentMetaInfo()` | OPEN | Engine caller shown; entry chain unresolved. |
| 20 | `TorrentDownloadImpl.getTorrentName()` | OPEN | Implementation printed; full route not verified. |
| 21 | `TorrentDownloadImpl.getTotalLeechers()` | OPEN | Engine caller shown; entry chain unresolved. |
| 22 | `TorrentDownloadImpl.getTotalPeers()` | OPEN | Engine caller shown; entry chain unresolved. |
| 23 | `TorrentDownloadImpl.getTotalSeeds()` | OPEN | Engine caller shown; entry chain unresolved. |
| 24 | `TorrentDownloadImpl.getTotalSentBytes()` | OPEN | Engine caller shown; entry chain unresolved. |
| 25 | `TorrentDownloadImpl.getTotalWanted()` | OPEN | Engine caller shown; entry chain unresolved. |
| 26 | `TorrentDownloadImpl.getTrackerInfoList()` | OPEN | Engine caller shown; entry chain unresolved. |
| 27 | `TorrentDownloadImpl.getTrackersUrl()` | OPEN | Engine caller shown; entry chain unresolved. |
| 28 | `TorrentDownloadImpl.getUploadSpeed()` | OPEN | Engine caller shown; entry chain unresolved. |
| 29 | `TorrentDownloadImpl.getUploadSpeedLimit()` | OPEN | Engine caller shown; entry chain unresolved. |
| 30 | `TorrentDownloadImpl.handleMetadata(MetadataReceivedAlert)` | OPEN | Registered listener shown; library callback delivery not independently established. |
| 31 | `TorrentDownloadImpl.handleReadPiece(ReadPieceAlert)` | OPEN | Registered listener shown; library callback delivery not independently established. |
| 32 | `TorrentDownloadImpl.handleTorrentChecked()` | OPEN | Registered listener shown; library callback delivery not independently established. |
| 33 | `TorrentDownloadImpl.handleTorrentFinished()` | OPEN | Registered listener shown; library callback delivery not independently established. |
| 34 | `TorrentDownloadImpl.hasMetadata()` | OPEN | Internal callers printed; complete route to them unresolved. |
| 35 | `TorrentDownloadImpl.hasMissingFiles()` | OPEN | Session caller shown; session entry chain unresolved. |
| 36 | `TorrentDownloadImpl.havePiece(int)` | OPEN | Stream caller shown; stream/server route unresolved. |
| 37 | `TorrentDownloadImpl.indicesToStr(int,int)` | OPEN | Called by `getFileIndicesBep53`, whose entry route is unresolved. |
| 38 | `TorrentDownloadImpl.isFinished()` | OPEN | Body/local uses printed; complete entry route unresolved. |
| 39 | `TorrentDownloadImpl.isFirstLastPiecePriority()` | OPEN | Engine caller shown; entry chain unresolved. |
| 40 | `TorrentDownloadImpl.isPaused()` | OPEN | Engine/local callers shown; entry chain unresolved. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
