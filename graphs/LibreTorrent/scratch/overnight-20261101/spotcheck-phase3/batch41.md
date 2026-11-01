# Spot-check — batch 41 (LibreTorrent Phase 3b, batches 1–60)

Scope: changed rows from verdicts_applied_table.json + coordinator_verdicts.json (none in this batch), plus 1-in-5 sample rows (1, 6, 11, 16, 21, 26, 31, 36). No work file edited.

## Changed rows (0)

None.

## Sample rows (8)

- 41/1 TorrentSessionImpl$InnerListener.lambda$alert$1 — REACHABLE INFERRED — PASS. Second notifyListeners lambda in InnerListener.alert ADD_TORRENT branch (TorrentSessionImpl.java:1073-1090, listener.onTorrentLoaded(hash)); notify loop printed (:1445-1455); alert dispatch INFERRED.
- 41/6 TorrentSessionImpl$LoadTorrentTask.run — REACHABLE INFERRED — PASS. TorrentSessionImpl.java:1470 loadTorrentsExec.execute(task) in runNextLoadTorrentTask; executor Thread → run() dispatch INFERRED; body is SOURCE (isTorrentAlreadyRunning check, download() or restoreDownload(), catch → notify onRestoreSessionError).
- 41/11 TorrentInputStream.finalize — REACHABLE INFERRED — PASS. The cell's final substantive statement is the applied decision: "[APPLIED 2026-11-01 D3b: OPEN → REACHABLE INFERRED per DECISIONS.md]". The earlier "stays OPEN" conditional-table text (convention (vi) option (b)) is dated history superseded by that applied decision; the row also correctly rejects UNREACHABLE no_trigger_in_app (the enclosing object IS created on a printed route, and an app-tree grep cannot rule out GC dispatch). Saved full-tree grep §H finds finalize only at :122 (definition) and :132 (super call).
- 41/16 TorrentInputStream.read(byte[],int,int) — REACHABLE SOURCE — PASS. NanoHTTPD.java:1267 this.data.read(buff, 0, (int) bytesToRead) in sendBody, reached via Response.send → sendBodyWithCorrectTransferAndEncoding → sendBodyWithCorrectEncoding → sendBody (NanoHTTPD.java:1223,1233,1236,1243,1246,1261); definition TorrentInputStream.java:257-354.
- 41/21 TorrentInputStream.waitForPiece — REACHABLE SOURCE — PASS. TorrentInputStream.java:196-256 read() and :257-354 read(byte[],int,int) call waitForPiece(task, p); definition :135-149.
- 41/26 TorrentInputStream$Piece.\<init\> — REACHABLE SOURCE — PASS. TorrentInputStream.java:232 new Piece(p) in read(); loop new Piece(p) in read(byte[],int,int) :257-354; definition :85-89 area.
- 41/31 TorrentStream.\<init\>(Parcel) — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition TorrentStream.java:55-66; only reached via CREATOR.createFromParcel (row 40); saved full-tree grep §D: no putParcelable/getParcelable/Bundle/Intent site passing a TorrentStream anywhere in the 252 app Java files.
- 41/36 TorrentStream.hashCode — UNREACHABLE no_trigger_in_app INFERRED — PASS. Definition TorrentStream.java:109-113 (id.hashCode()); no printed hash caller in saved full-tree grep §§D/G; no hash-collection use of a TorrentStream anywhere; res grep §I zero.

Totals: checked 8 (0 changed + 8 sample-only) — PASS 8, FAIL-prose 0, FAIL-label 0.
