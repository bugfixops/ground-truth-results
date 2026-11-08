# Spot-check — Batch 36 (Stream A Phase 2)

- Work file: `~/workspace/overnight/stream-A/work/batch36-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived from already-fetched local source only (`~/workspace/b353637-src/`). No GitHub connector fetch was needed; no 429 encountered. No edit was made to the work file.
- Phase 1 label changes in this batch: none listed in any dated 2026-11-01 revision note (batch is 40/40 REACHABLE as found). Rows checked = sample rows 1, 6, 11, 16, 21, 26, 31, 36.
- Build / sampler / C1: not run (not this task).

## Per-row verdicts

| Row | Method | Table label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | TorrentDownloadImpl.getETA | REACHABLE / SOURCE | PASS | TorrentEngine.java:797 `task.getETA()` inside makeInfo — exact. |
| 6 | TorrentDownloadImpl.getFilesAvailability | REACHABLE / SOURCE | PASS | TorrentEngine.java:856 `task.getFilesAvailability(piecesAvail)` inside makeAdvancedInfoSync — exact. |
| 11 | TorrentDownloadImpl.getPeerInfoList | REACHABLE / SOURCE | PASS | TorrentEngine.java:880 `return task.getPeerInfoList();` — exact. |
| 16 | TorrentDownloadImpl.getShareRatio | REACHABLE / SOURCE | PASS | TorrentEngine.java:852 `task.getShareRatio()` inside makeAdvancedInfoSync — exact. |
| 21 | TorrentDownloadImpl.getTotalLeechers | REACHABLE / SOURCE | PASS | TorrentEngine.java:858 `task.getTotalLeechers()` inside makeAdvancedInfoSync — exact. |
| 26 | TorrentDownloadImpl.getTrackerInfoList | REACHABLE / SOURCE | PASS | TorrentEngine.java:869 `return task.getTrackerInfoList();` inside makeTrackerInfoList — exact. |
| 31 | TorrentDownloadImpl.handleReadPiece | REACHABLE / INFERRED | PASS | TorrentDownloadImpl.java:272 `handleReadPiece((ReadPieceAlert)alert)` inside InnerListener.alert's READ_PIECE case (:271) — exact. INFERRED is correct because the library alert dispatch is unprinted. |
| 36 | TorrentDownloadImpl.havePiece | REACHABLE / SOURCE | PASS | TorrentInputStream.java:139 `task.havePiece(pieceIndex)` inside waitForPiece (:135) — exact; waitForPiece is called from the read paths at :239 and :335 — both exact. TorrentInputStream is constructed by TorrentEngine.getTorrentInputStream at :758–759 (`return new TorrentInputStream(session, stream)`) — exact. The row's distinction from the libtorrent-handle `th.havePiece` sites (TorrentDownloadImpl:1588/:1598, different receiver) is correct and was not re-conflated here. |

## Totals

- Rows checked: 8. **PASS: 8. FAIL: 0.**
- Proposed corrections: none.
