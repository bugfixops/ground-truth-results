# Spot-check — batch 37 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 37/1 TorrentDownloadImpl.isPaused(TorrentStatus) — REACHABLE SOURCE — PASS. TDI:1358 boolean isPaused = isPaused(status) inside getStateCode (TE:790). Distinct from the no-arg isPaused() in batch 36 row 40 (stated in row).
- 37/6 TorrentDownloadImpl.lambda$checkError$1 — REACHABLE INFERRED — PASS. TDI:334 notifyListeners lambda inside checkError (batch 35 row 27); listener dispatch unprinted. $1 by source order, NOT bytecode-verified (stated in row).
- 37/11 TorrentDownloadImpl.lambda$onStorageMoved$0 — REACHABLE INFERRED — PASS. TDI:287 notifyListeners lambda inside onStorageMoved; listener dispatch unprinted. $0 matches the single lambda in that method, NOT bytecode-verified (stated in row).
- 37/16 TorrentDownloadImpl.lambda$torrentRemoved$5 — REACHABLE INFERRED — PASS. TDI:458 notifyListeners lambda inside torrentRemoved (batch 38 row 6); listener dispatch unprinted. Index NOT bytecode-verified (stated in row).
- 37/21 TorrentDownloadImpl.pause — REACHABLE SOURCE — PASS. TE:1283, :1298, :1448 task.pause(); also TDI:331 checkError body and :421 handleMetadata body call pause().
- 37/26 TorrentDownloadImpl.remove — REACHABLE SOURCE — PASS. TSI:391 task.remove(withFiles) inside deleteTorrent; TSI deleteTorrent called from TE:539 session.deleteTorrent(id, withFiles).
- 37/31 TorrentDownloadImpl.resume — REACHABLE INFERRED — PASS. TDI:320 resume() inside checkError (batch 35 row 27), on the alert route; alert dispatch unprinted.
- 37/36 TorrentDownloadImpl.setDownloadPath — REACHABLE SOURCE — PASS. TE:690 task.setDownloadPath(path); internally TDI:1217 criticalWork.setMoving(true).

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
