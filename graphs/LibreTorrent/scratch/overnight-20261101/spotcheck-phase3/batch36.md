# Spot-check — batch 36 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 36/1 TorrentDownloadImpl.getETA — REACHABLE SOURCE — PASS. TE:797 task.getETA() in makeInfo; internally TDI:1171 getETA body checks getStateCode().
- 36/6 TorrentDownloadImpl.getFilesAvailability — REACHABLE SOURCE — PASS. TE:856 task.getFilesAvailability(piecesAvail) in makeAdvancedInfoSync.
- 36/11 TorrentDownloadImpl.getPeerInfoList — REACHABLE SOURCE — PASS. TE:880 task.getPeerInfoList().
- 36/16 TorrentDownloadImpl.getShareRatio — REACHABLE SOURCE — PASS. TE:852 task.getShareRatio() in makeAdvancedInfoSync.
- 36/21 TorrentDownloadImpl.getTotalLeechers — REACHABLE SOURCE — PASS. TE:858 task.getTotalLeechers() in makeAdvancedInfoSync.
- 36/26 TorrentDownloadImpl.getTrackerInfoList — REACHABLE SOURCE — PASS. TE:869 task.getTrackerInfoList().
- 36/31 TorrentDownloadImpl.handleReadPiece — REACHABLE INFERRED — PASS. TDI:272 handleReadPiece((ReadPieceAlert)alert) in InnerListener.alert READ_PIECE case; alert dispatch unprinted.
- 36/36 TorrentDownloadImpl.havePiece — REACHABLE SOURCE — PASS. Flipped from prior OPEN on fresh evidence: TIS:139 task.havePiece(pieceIndex) inside waitForPiece, called from TIS read paths :239 and :335; TIS constructed by TE getTorrentInputStream :758-759, called from TorrentStreamServer (batch 23 fresh fetch :206/:243, carried here, not re-fetched in this pass — stated in row).

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
