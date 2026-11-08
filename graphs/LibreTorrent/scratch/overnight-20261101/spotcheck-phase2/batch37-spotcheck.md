# Spot-check — Batch 37 (Stream A Phase 2)

- Work file: `~/workspace/overnight/stream-A/work/batch37-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived from already-fetched local source only (`~/workspace/b353637-src/`, `~/workspace/overnight/stream-A/corpus/java/`). No GitHub connector fetch was needed; no 429 encountered. No edit was made to the work file.
- Phase 1 label changes in this batch: none listed in any dated 2026-11-01 revision note (batch is 40/40 REACHABLE as found). Rows checked = sample rows 1, 6, 11, 16, 21, 26, 31, 36.
- Build / sampler / C1: not run (not this task).

## Per-row verdicts

| Row | Method | Table label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | TorrentDownloadImpl.isPaused(TorrentStatus) | REACHABLE / SOURCE | PASS | TorrentDownloadImpl.java:1358 `boolean isPaused = isPaused(status)` inside getStateCode — exact; TorrentEngine.java:790 `task.getStateCode()` reaches getStateCode — exact. Distinct from the no-arg isPaused() (batch 36 row 40) as the row states. |
| 6 | TorrentDownloadImpl.lambda$checkError$1 | REACHABLE / INFERRED | PASS | TorrentDownloadImpl.java:334 `notifyListeners((listener) -> listener.onTorrentError(id, new Exception(errorMsg)))` inside checkError (:302; pause() at :331 in the same body) — exact. Listener dispatch is unprinted, so INFERRED is correct. The $1 index is source-order, NOT bytecode-verified, as the row itself states. |
| 11 | TorrentDownloadImpl.lambda$onStorageMoved$0 | REACHABLE / INFERRED | PASS | TorrentDownloadImpl.java:287 `notifyListeners((listener) -> listener.onTorrentMoved(id, success))` inside onStorageMoved — exact, and it is the single lambda in that method. INFERRED (dispatch unprinted) is correct; $0 is source-order, NOT bytecode-verified, as the row states. |
| 16 | TorrentDownloadImpl.lambda$torrentRemoved$5 | REACHABLE / INFERRED | PASS | TorrentDownloadImpl.java:458 `notifyListeners((listener) -> listener.onTorrentRemoved(id))` inside torrentRemoved (:456) — exact. INFERRED is correct; index NOT bytecode-verified, as the row states. |
| 21 | TorrentDownloadImpl.pause | REACHABLE / SOURCE | PASS | TorrentEngine.java:1283, :1298, :1448 `task.pause()` — all three exact. (TorrentDownloadImpl.java:331 checkError-body pause also confirmed; :421 handleMetadata site not re-checked, not needed.) |
| 26 | TorrentDownloadImpl.remove | REACHABLE / SOURCE | PASS | TorrentSessionImpl.java:391 `task.remove(withFiles)` inside deleteTorrent — exact; TorrentEngine.java:539 `session.deleteTorrent(id, withFiles)` calls it — exact. |
| 31 | TorrentDownloadImpl.resume | REACHABLE / INFERRED | PASS | TorrentDownloadImpl.java:320 `resume()` inside checkError — exact. INFERRED is correct because checkError is reached on the alert route whose dispatch is unprinted. |
| 36 | TorrentDownloadImpl.setDownloadPath | REACHABLE / SOURCE | PASS | TorrentEngine.java:690 `task.setDownloadPath(path)` — exact; TorrentDownloadImpl.java:1217 `criticalWork.setMoving(true)` inside setDownloadPath (:1215) — exact. |

## Totals

- Rows checked: 8. **PASS: 8. FAIL: 0.**
- Proposed corrections: none.
