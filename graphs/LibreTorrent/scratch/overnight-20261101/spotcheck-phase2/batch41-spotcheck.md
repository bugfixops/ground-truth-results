# LibreTorrent batch 41 — Phase 2 spot-check — UNVERIFIED spot-check only

- Source file checked: `~/workspace/overnight/stream-A/work/batch41-merge-ready.md` (UNVERIFIED proposal, not a result).
- Method: re-derived each row below from already-fetched local source only — the 281-file
  complete-tree corpus in `~/workspace/overnight/stream-A/corpus/java/` and the saved
  recheck grep `~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt`.
  No connector fetch was needed; no merge-ready file was edited; no label was flipped.
- Rows checked (18): sample 1, 6, 11, 16, 21, 26, 31, 36 PLUS Phase 1 changed/re-checked rows
  11 (Phase 1c D3b flip), 12, 14, 15, 27, 28, 34, 35, 37, 38, 40, plus must-include rows 36, 37.
- Build / sampler / C1: not run (not this task).

## Verdicts

| Row | Method | Filed label | Verdict | Printed evidence |
|---|---|---|---|---|
| 1 | TorrentSessionImpl$InnerListener.lambda$alert$1 | REACHABLE INFERRED | PASS | TorrentSessionImpl.java:1085-1086, second notify lambda `listener.onTorrentLoaded(hash)` (first lambda is onTorrentAdded); notify loop :1445-1450. Lambda numbering by source order, consistent with filed claim. |
| 6 | TorrentSessionImpl$LoadTorrentTask.run | REACHABLE INFERRED | PASS | TorrentSessionImpl.java:1472 `loadTorrentsExec.execute(task)`; run() body :1509+ (isTorrentAlreadyRunning / download / restoreDownload, catch -> notify onRestoreSessionError). Executor dispatch INFERRED, as filed. |
| 11 | TorrentInputStream.finalize | REACHABLE INFERRED (Phase 1c D3b flip) | PASS | Def TorrentInputStream.java:122-132 (stopped=true, removeListener, super.finalize() :132). Object created on printed route TorrentEngine.java:758-759 `new TorrentInputStream(session, stream)`. Under adopted D3b (GC dispatch counts as a route) the filed REACHABLE INFERRED stands. Corpus-wide grep: finalize appears only at :122 (def) and :132 (super call). |
| 12 | TorrentInputStream.markSupported | UNREACHABLE INFERRED | PASS | Def TorrentInputStream.java:405-408 (returns false). Corpus grep: no `markSupported` caller anywhere; NanoHTTPD's only `.mark(` is :667 on the HTTPSession request stream, not response data. Only TorrentInputStream holders: TorrentEngine.java:758-759, TorrentStreamServer.java:206,:243. |
| 14 | TorrentInputStream.read() | UNREACHABLE INFERRED | PASS | Def :196. Corpus grep: no external caller of the 0-arg read; sole stream consumer NanoHTTPD Response reads response data only via the 3-arg overload (NanoHTTPD.java:1267). |
| 15 | TorrentInputStream.read(byte[]) | UNREACHABLE INFERRED | PASS | Def :355-359 (delegates to 3-arg read). Same consumer evidence as row 14: NanoHTTPD.java:1267 calls the 3-arg overload directly, so this overload has no caller. |
| 16 | TorrentInputStream.read(byte[],int,int) | REACHABLE SOURCE | PASS | NanoHTTPD.java:1267 `this.data.read(buff, 0, (int) bytesToRead)` in sendBody. Def TorrentInputStream.java:257. |
| 21 | TorrentInputStream.waitForPiece | REACHABLE SOURCE | PASS | Called from read() :239 and read(byte[],int,int) :335. Def :135. |
| 26 | TorrentInputStream$Piece.<init> | REACHABLE SOURCE | PASS | `new Piece(p)` at TorrentInputStream.java:224 (read()) and :303 (3-arg read). Def :79. |
| 27 | TorrentInputStream$Piece.equals | UNREACHABLE INFERRED | PASS | Def :91-95. `Piece` is a private static nested class (TorrentInputStream.java:71); corpus grep shows no Piece use outside TorrentInputStream.java and no equals caller; readPiece compares `p.index` directly. |
| 28 | TorrentInputStream$Piece.hashCode | UNREACHABLE INFERRED | PASS | Def :85-89 (return index). Same private-nested-class / no-caller evidence as row 27. |
| 31 | TorrentStream.<init>(Parcel) | UNREACHABLE INFERRED | PASS | Def TorrentStream.java:55. Only reached via CREATOR.createFromParcel (row 40); corpus grep shows no putParcelable/getParcelable site passing a TorrentStream (parcel sites pass Uri, TagInfo, list state, etc. only). |
| 34 | TorrentStream.describeContents | UNREACHABLE INFERRED | PASS | Def TorrentStream.java:74. Same no-parceling-site evidence as row 31; framework calls it only when parceled. |
| 35 | TorrentStream.equals | UNREACHABLE INFERRED | PASS | Def TorrentStream.java:116-118. Corpus grep: no `stream.equals` / TorrentStream-equals caller; server/stream code reads `stream.id`, `stream.fileSize` fields directly. |
| 36 | TorrentStream.hashCode | UNREACHABLE INFERRED — MUST-INCLUDE D6/D7 flag | PASS, DO NOT FLIP | Def TorrentStream.java:110-112 (`id.hashCode()`). Corpus grep: no TorrentStream hashCode caller and no hash-collection use of a TorrentStream. Stays UNREACHABLE as filed, per task instruction; re-derived, not flipped. |
| 37 | TorrentStream.toString | UNREACHABLE INFERRED — MUST-INCLUDE D6/D7 flag | PASS, DO NOT FLIP | Def TorrentStream.java:123. Corpus grep: no `stream.toString()` / log / concat caller of a TorrentStream (TorrentStreamServer concatenates `stream.id`/`stream.fileSize` only, e.g. :212,:214; its :104 `.toString()` is on a URI, not a stream). Stays UNREACHABLE as filed; re-derived, not flipped. |
| 38 | TorrentStream.writeToParcel | UNREACHABLE INFERRED | PASS | Def TorrentStream.java:80. Same no-parceling-site evidence as row 31. |
| 40 | TorrentStream$1.createFromParcel | UNREACHABLE INFERRED | PASS | Def TorrentStream.java:97-99 (`return new TorrentStream(source)`). Same no-unparcel-site evidence as row 31. |

## Totals

- Checked: 18. PASS: 18. FAIL: 0.
- Proposed corrections: none. No row in this batch is proposed for a label change.
- Citation note (not a label failure): filed TorrentSessionImpl line numbers run a few lines
  higher than the local corpus copy (e.g. filed :1073-1090 vs corpus :1061-1087; filed notify
  loop :1445-1455 vs corpus :1445-1450); the cited code is present at the corpus lines above.
  The merger should use fresh-print numbers at merge if it requires them.
