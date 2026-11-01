**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

**REVISION 2026-11-01 (round 2, G6): row 11 re-examined, NOT flipped. Saved full-tree grep §§H-I in ~/workspace/b414748-openclose2-src/full_tree_grep_414748.txt (252 app Java files): finalize appears only at TorrentInputStream.java:122 (definition) and :132 (super.finalize()); TorrentInputStream holders remain TorrentEngine.getTorrentInputStream :758-759 and TorrentStreamServer :206/:243, as in the prior pass. Row 11 now carries a CONDITIONAL table under convention (vi) only (see row). Counts unchanged 27/12/1. Build: not run. C1: not run. No GitHub connector fetch was needed in this pass (all target files already present locally); no fresh 429. Original file backed up at ~/workspace/libretorrent-merge-backup-pre-openclose2/batch41-merge-ready.md before this edit. TorrentStream fresh line numbers in revised rows still run ~2-4 lower than prior carried citations; unrevised rows still carry prior numbers and should be re-checked at merge.**

**REVISION 2026-11-01 — OPEN-closing pass (this task, batches 39-42).** 12 of 13 OPEN rows closed to UNREACHABLE; only row 11 (finalize) stays OPEN. Fresh source in `~/workspace/b394142-openclose-src/` (TorrentInputStream.java 471 lines SHA `7f447b88…`, TorrentStream.java 137 lines SHA `4009bda6…`, TorrentStreamServer.java 284 lines SHA `d69e997f…`, TorrentEngine.java 1659 lines SHA `17d06efe…`, TorrentDownloadImpl.java 1711 lines SHA `30024b5d…`, NanoHTTPD.java 1851 lines SHA `bdb2ab67…`, all branch `work-2026-10-31`, connector only, no fresh 429). Saved grep: `b394142-openclose-src/full_tree_grep_394142.txt` — §§C-D, F-G over all 252 app Java files + §H (test/androidTest zero; debug/play/release have no .java) + §I (87 res layout/xml files, zero hits). Fresh TorrentStream.java line numbers in the revised rows supersede the prior file's carried-forward TorrentStream citations (which ran ~2-4 lines higher); unrevised rows still carry prior numbers and should be re-checked at merge. `confirmed_by` for the twelve flips is INFERRED (no printed call site exists to be SOURCE; verdicts rest on the saved grep + printed definitions and the single-consumer proofs in each row) — recorded, not decided. Each flipped row flips back to REACHABLE on one printed caller (parcel rows 31/34/38/40 flip together with batch 42 row 1 on one printed parceling site). Build: not run. C1: not run.

# LibreTorrent batch 41 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 41 only, no other batch, no other app, no device replay, no Aegis.
- Membership: exactly the 40 rows for batch 41 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`,
  taken from the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
  `0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
  All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan, in plan order, method names and
  JVM descriptors matched row for row against the plan in this pass.
- Prior work used as INPUT only: `~/workspace/libretorrent-batch41-proposal.md`
  (27 REACHABLE proposed / 0 UNREACHABLE / 13 OPEN). No verdict below is copied as a result:
  every row was checked against printed source, and the OPEN rows were re-examined in this
  pass against the freshly fetched files in `~/workspace/b4143-src/` (settings fragments,
  PermissionManager, DetailTorrentViewModel — none of which contains a caller for any
  batch-41 OPEN row) plus the prior proposal's printed corpus, flagged below as
  carried-forward where not freshly re-printed here.
- Printed source in this pass, fresh connector fetches from branch `work-2026-10-31`,
  one file at a time with 20 s pauses, no fresh HTTP 429 hit, saved in
  `~/workspace/b4143-src/`: BehaviorSettingsFragment.java (286 lines),
  FeedSettingsFragment.java (164), LimitationsSettingsFragment.java (258),
  NetworkSettingsFragment.java (415), SchedulingSettingsFragment.java (243),
  StorageSettingsFragment.java (297), StreamingSettingsFragment.java (119),
  PermissionManager.java (156), DetailTorrentViewModel.java (611),
  AnonymousModeSettingsFragment.java (84).
- Carried-forward printed source (prior proposal session, printed in full then, NOT
  freshly re-printed in this pass — merger should re-verify line numbers against a fresh
  fetch if it requires it): TorrentSessionImpl.java (full, sections),
  TorrentInputStream.java (470 lines, connector SHA `7f447b88600d949ec9233f59c46108041bb2272b`),
  TorrentStream.java (137 lines), TorrentStreamServer.java (284 lines),
  NanoHTTPD.java sendBody/send sections (:1185-1280, :1261-1275),
  TorrentEngine.java getStream/getTorrentInputStream sections (:747-759),
  TorrentDownloadImpl.java getStream section (:1607-1625).
- `confirmed_by` convention in this file: SOURCE = a direct app-to-app call site naming
  the method is printed in app source (including a printed listener body that calls it);
  INFERRED = the method is reached only through unprinted framework/library dispatch
  (listener/Rx/executor/JVM class initialisation) where the registration or first use is
  printed. This is the per-row convention, not the whole-route convention used in some
  earlier batches; labels are unaffected, only `confirmed_by` would change at merge if the
  merger adopts the whole-route convention.
- No connector `search_code` result was used as evidence of absence anywhere in this file.

## Shared trunk (carried-forward, prior proposal)

Batch 39/40 trunk: TorrentService -> TorrentEngine.doStart -> TorrentSessionImpl.start ->
onAfterStart -> handleOnSessionStarted -> startStreamingServer ->
TorrentStreamServer.serve/handleTorrent, then:
TorrentStreamServer.handleTorrent (TorrentStreamServer.java:127-260) ->
engine.getStream(torrentId, fileIndex) (TorrentEngine.java:747-755) ->
task.getStream(fileIndex) (TorrentDownloadImpl.java:1607-1625, new TorrentStream :1621) ->
engine.getTorrentInputStream(stream) (TorrentEngine.java:758-759, new TorrentInputStream :759) ->
NanoHTTPD Response.sendBody (NanoHTTPD.java:1261-1275, this.data.read(buff, 0, bytesToRead) :1267)
and Response.send safeClose(this.data). Streaming gate: pref.enableStreaming()
(TorrentEngine.java:1056-1059). Strict-entry caveat as in batches 39-40:
launcher -> TorrentService step was NOT printed in the prior proposal or in this pass, so
under a strict launcher-entry rule all REACHABLE rows in this batch revert to OPEN.
The merger must pick one strict-entry convention for all batches; it is recorded here,
not decided.

## Table (plan order)

| # | Method | JVM descriptor | Label proposed | confirmed_by | Printed citation / note |
|---|---|---|---|---|---|
| 1 | TorrentSessionImpl$InnerListener.lambda$alert$1 | (Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V | REACHABLE | INFERRED | Second notifyListeners lambda in InnerListener.alert ADD_TORRENT branch (TorrentSessionImpl.java:1073-1090, listener.onTorrentLoaded(hash)). Notify loop printed (:1445-1455); alert dispatch INFERRED. Per-inner-class lambda numbering; distinct from outer-class $1. Carried-forward. |
| 2 | TorrentSessionImpl$InnerListener.types | ()[I | REACHABLE | INFERRED | TorrentSessionImpl.java:1063-1068 types() returns INNER_LISTENER_TYPES. AlertListener registration requires types(); registered at :987 addListener(innerListener); library call to types() INFERRED, not printed. Carried-forward. |
| 3 | TorrentSessionImpl$LoadTorrentTask.<init> | (Lorg/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl;Ljava/lang/String;)V | REACHABLE | SOURCE | TorrentSessionImpl.java:420 LoadTorrentTask loadTask = new LoadTorrentTask(torrent.id) in restoreTorrents. Carried-forward. |
| 4 | TorrentSessionImpl$LoadTorrentTask.lambda$run$0 | (Lorg/proninyaroslav/libretorrent/core/model/TorrentEngineListener;)V | REACHABLE | INFERRED | NotifyListeners lambda in LoadTorrentTask.run catch block (TorrentSessionImpl.java:1517-1530, listener.onRestoreSessionError(torrentId)). Notify loop printed; executor dispatch for run INFERRED (row 6). Carried-forward. |
| 5 | TorrentSessionImpl$LoadTorrentTask.putMagnet | (Ljava/lang/String;Ljava/io/File;ZZ)V | REACHABLE | SOURCE | TorrentSessionImpl.java:421-427 loadTask.putMagnet(torrent.getMagnet(), new File(path), torrent.manuallyPaused, torrent.sequentialDownload) in restoreTorrents, gate torrent.isDownloadingMetadata(). Carried-forward. |
| 6 | TorrentSessionImpl$LoadTorrentTask.run | ()V | REACHABLE | INFERRED | TorrentSessionImpl.java:1470 loadTorrentsExec.execute(task) in runNextLoadTorrentTask; executor Thread -> run() dispatch INFERRED, as in batch 16. Body is SOURCE (isTorrentAlreadyRunning check, download() or restoreDownload(), catch -> notify onRestoreSessionError). Carried-forward. |
| 7 | TorrentInputStream.<clinit> | ()V | REACHABLE | INFERRED | Static field `lock = new ReentrantLock()` (TorrentInputStream.java:60-70 area). JVM class initialisation on first use via TorrentEngine.getTorrentInputStream :758-759; init ordering is JVM semantics, not a printed line. Carried-forward. |
| 8 | TorrentInputStream.<init> | (Lorg/proninyaroslav/libretorrent/core/model/session/TorrentSession;Lorg/proninyaroslav/libretorrent/core/model/stream/TorrentStream;)V | REACHABLE | SOURCE | TorrentEngine.java:758-759 return new TorrentInputStream(session, stream) in getTorrentInputStream. Def TorrentInputStream.java:97-120 (session.getTask, session.addListener(listener), task.setInterestedPieces). Carried-forward. |
| 9 | TorrentInputStream.close | ()V | REACHABLE | INFERRED | InputStream passed to newFixedLengthResponse in TorrentStreamServer.handleTorrent :206,:243; NanoHTTPD Response.send closes the data stream via safeClose(this.data) (NanoHTTPD.java send :1185-1229 area, safeClose body not printed in the prior session, so INFERRED, not SOURCE). Def TorrentInputStream.java:361-371. Carried-forward. |
| 10 | TorrentInputStream.filePosToPiecePos | (IJ)I | REACHABLE | SOURCE | TorrentInputStream.java:196-256 read() and :257-354 read(byte[],int,int) both call filePosToPiecePos(p, filePos). Def :169-179. Carried-forward. |
| 11 | TorrentInputStream.finalize | ()V | OPEN | — | GC finalizer (TorrentInputStream.java:122-133, stopped=true, session.removeListener, super.finalize() :132). No printed app caller and no printed GC/finalizer dispatch in any file printed for this batch; saved full-tree grep §H (252 app Java files, ~/workspace/b414748-openclose2-src/full_tree_grep_414748.txt) finds finalize only at :122 (definition) and :132 (super call) — the tree's only finalize method. CONDITIONAL TABLE, convention (vi) ONLY, never flipped here: (a) IF the project rules that JVM/GC finalization counts as a trigger-graph route, this row flips to REACHABLE INFERRED — the object is created on a printed route (row 8, TorrentEngine.getTorrentInputStream :758-759, served via TorrentStreamServer/NanoHTTPD), so a stream that becomes unreachable after serving could be finalized, with the printed body side-effects (stopped=true, removeListener); (b) IF the project rules that GC dispatch does not count as a route, or leaves (vi) undecided, this row stays OPEN. (c) NOT adopted: UNREACHABLE no_trigger_in_app — rejected in the prior pass and here, because the enclosing object IS created on a printed route, so creation-plus-GC is not 'no trigger', and an app-tree grep cannot rule out GC dispatch. A printed GC/finalizer dispatch or a project (vi) decision is what resolves this row. |
| 12 | TorrentInputStream.markSupported | ()Z | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Returns false (TorrentInputStream.java:405-408). Saved full-tree grep §C: the only TorrentInputStream holders in the tree are TorrentEngine.getTorrentInputStream (:758-759, creation) and TorrentStreamServer (:206, :243, use); the sole stream consumer, NanoHTTPD Response, never calls mark/markSupported on its data — fresh NanoHTTPD.java sendBody (:1261-1275) reads with the 3-arg overload only (:1267), and its only `.mark(` call (:667) is on HTTPSession's own request input stream, not on the response data. Res grep §I zero; test/androidTest §H zero. Flips to REACHABLE on any printed markSupported caller. |
| 13 | TorrentInputStream.pieceFinished | ()V | REACHABLE | INFERRED | TorrentInputStream.java:422-429 listener.onPieceFinished -> pieceFinished() (:431-435, notifyAll). Listener callback dispatch via notifyListeners INFERRED; internal call printed. Carried-forward. |
| 14 | TorrentInputStream.read() | ()I | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Single-byte read (TorrentInputStream.java:196-256). Saved full-tree grep §C: no other TorrentInputStream consumer exists besides TorrentStreamServer → NanoHTTPD, and fresh NanoHTTPD sendBody calls the 3-arg overload only (NanoHTTPD.java:1267 `this.data.read(buff, 0, bytesToRead)`), NOT read(). No wrapping (no BufferedInputStream/transferTo/available on a stream in the tree). Res grep §I zero. Flips to REACHABLE on any printed read() caller. |
| 15 | TorrentInputStream.read(byte[]) | ([B)I | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Delegates to the 3-arg read (TorrentInputStream.java:355-359), but fresh NanoHTTPD sendBody calls the 3-arg overload directly (:1267), so this overload has no caller; saved full-tree grep §C shows no other stream consumer. Res grep §I zero. Flips to REACHABLE on any printed read(byte[]) caller. |
| 16 | TorrentInputStream.read(byte[],int,int) | ([BII)I | REACHABLE | SOURCE | NanoHTTPD.java:1267 this.data.read(buff, 0, (int) bytesToRead) in sendBody, reached via Response.send -> sendBodyWithCorrectTransferAndEncoding -> sendBodyWithCorrectEncoding -> sendBody (NanoHTTPD.java:1223,1233,1236,1243,1246,1261). Def TorrentInputStream.java:257-354. Carried-forward. |
| 17 | TorrentInputStream.readFromCache | (Lorg/proninyaroslav/libretorrent/core/model/stream/TorrentInputStream$Piece;[B)V | REACHABLE | SOURCE | TorrentInputStream.java:196-256 read() and :257-354 read(byte[],int,int) call readFromCache(piece, ...); also readPiece :436-470. Def :180-188. Carried-forward. |
| 18 | TorrentInputStream.readPiece | (Lorg/proninyaroslav/libretorrent/core/model/data/ReadPieceInfo;)V | REACHABLE | INFERRED | TorrentInputStream.java:413-420 listener.onReadPiece -> readPiece(info) (:436-470). Listener dispatch INFERRED; internal call printed. Carried-forward. |
| 19 | TorrentInputStream.skip | (J)J | REACHABLE | SOURCE | TorrentStreamServer.java:207 is.skip(startFrom) in handleTorrent (range branch). Def TorrentInputStream.java:375-404. Carried-forward. |
| 20 | TorrentInputStream.toUnsignedByte | (B)I | REACHABLE | SOURCE | TorrentInputStream.java:196-256 read() returns toUnsignedByte(readSession.buf[0]). Def :190-194. Carried-forward. |
| 21 | TorrentInputStream.waitForPiece | (Lorg/proninyaroslav/libretorrent/core/model/session/TorrentDownload;I)Z | REACHABLE | SOURCE | TorrentInputStream.java:196-256 read() and :257-354 read(byte[],int,int) call waitForPiece(task, p). Def :135-149. Carried-forward. |
| 22 | TorrentInputStream.waitForReadPieces | ()Z | REACHABLE | SOURCE | Same callers as row 21 (read() and read(byte[],int,int)). Def :150-167. Carried-forward. |
| 23 | TorrentInputStream$1.<init> | (Lorg/proninyaroslav/libretorrent/core/model/stream/TorrentInputStream;)V | REACHABLE | INFERRED | Anonymous TorrentEngineListener `listener`, field initialiser at TorrentInputStream.java:410. Runs when a TorrentInputStream is constructed (row 8); anonymous-class numbering inferred from source order — merger must confirm against bytecode. Carried-forward. |
| 24 | TorrentInputStream$1.onPieceFinished | (Ljava/lang/String;I)V | REACHABLE | INFERRED | TorrentInputStream.java:422-429 onPieceFinished (guard stream.torrentId.equals(id), then pieceFinished()). Listener dispatch INFERRED. Carried-forward. |
| 25 | TorrentInputStream$1.onReadPiece | (Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/data/ReadPieceInfo;)V | REACHABLE | INFERRED | TorrentInputStream.java:413-420 onReadPiece (guard, then readPiece(info)). Listener dispatch INFERRED. Carried-forward. |
| 26 | TorrentInputStream$Piece.<init> | (I)V | REACHABLE | SOURCE | TorrentInputStream.java:232 new Piece(p) in read(); loop new Piece(p) in read(byte[],int,int) :257-354. Def :85-89 area (Piece(int index) ctor). Carried-forward. |
| 27 | TorrentInputStream$Piece.equals | (Ljava/lang/Object;)Z | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Def TorrentInputStream.java:91-95. readPiece (:436-470) compares `p.index == info.piece`, NOT Piece.equals; no HashMap/HashSet/contains of Piece in the file. Saved full-tree grep §F: ZERO `Piece` hits outside TorrentInputStream.java — and Piece is a private static nested class, so no code outside this file can name it at all. Flips to REACHABLE on any printed equals caller. |
| 28 | TorrentInputStream$Piece.hashCode | ()I | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Def TorrentInputStream.java:85-89 (return index). Same as row 27: no printed hash caller in the file, and saved full-tree grep §F shows no Piece use outside TorrentInputStream.java (private nested class). Flips to REACHABLE on any printed hashCode caller. |
| 29 | TorrentInputStream$ReadSession.<init> | (Lorg/proninyaroslav/libretorrent/core/model/stream/TorrentInputStream;)V | REACHABLE | SOURCE | Implicit default ctor. TorrentInputStream.java:225 new ReadSession() in read(); :~295 new ReadSession() in read(byte[],int,int). Carried-forward. |
| 30 | TorrentStream.<clinit> | ()V | REACHABLE | INFERRED | Static CREATOR field (TorrentStream.java:101-115). JVM class initialisation on first use via TorrentDownloadImpl.getStream :1607-1625; init ordering JVM semantics, not a printed line. Carried-forward. |
| 31 | TorrentStream.<init>(Parcel) | (Landroid/os/Parcel;)V | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Def TorrentStream.java:55-66 (fresh numbering). Only reached via CREATOR.createFromParcel (row 40). Saved full-tree grep §D: no putParcelable/getParcelable/Bundle/Intent site passing a TorrentStream anywhere in the 252 app Java files; the only TorrentStream creation is TorrentDownloadImpl.getStream (:1621), and all other uses read fields directly. Framework Parcelable dispatch requires an app parceling site, and none exists; res grep §I zero. Flips together with rows 34, 38, 40 and batch 42 row 1 on one printed parceling site. |
| 32 | TorrentStream.<init>(String,int,int,int,int,long,long,int) | (Ljava/lang/String;IIIIJJI)V | REACHABLE | SOURCE | TorrentDownloadImpl.java:1621 new TorrentStream(id, fileIndex, filePieces.first, filePieces.second, ti.pieceLength(), fs.fileOffset(fileIndex), fs.fileSize(fileIndex), ti.pieceSize(filePieces.second)) in getStream. Def TorrentStream.java:35-50. Carried-forward. |
| 33 | TorrentStream.bytesToPieceIndex | (J)I | REACHABLE | SOURCE | TorrentInputStream.java:196-256 read() (bytesToPieceIndex(filePos + 1)); :257-354 read(byte[],int,int); :375-404 skip() (bytesToPieceIndex(filePos + 1)). Def TorrentStream.java:60-63. Carried-forward. |
| 34 | TorrentStream.describeContents | ()I | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Parcelable, returns 0 (TorrentStream.java:73-77, fresh numbering). Same parcel argument as row 31: no printed parceling site in the saved full-tree grep §D; framework calls describeContents only when the object is parceled. Flips together with rows 31, 38, 40 and batch 42 row 1. |
| 35 | TorrentStream.equals | (Ljava/lang/Object;)Z | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Def TorrentStream.java:115-119 (fresh numbering; id comparison). Saved full-tree grep §G: no `stream.equals` / TorrentStream equals call anywhere (the only `id.equals` hit is inside this method's own body); no collection holding a TorrentStream, no log/concat use (supplementary grep clean); TorrentStreamServer/TorrentInputStream read `stream.id` directly. Res grep §I zero. Flips to REACHABLE on any printed equals caller. |
| 36 | TorrentStream.hashCode | ()I | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Def TorrentStream.java:109-113 (fresh numbering; `id.hashCode()`). Same as row 35: no printed hash caller in saved full-tree grep §§D/G; no hash-collection use of a TorrentStream anywhere. Res grep §I zero. Flips to REACHABLE on any printed hashCode caller. |
| 37 | TorrentStream.toString | ()Ljava/lang/String; | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Def TorrentStream.java:121-136 (fresh numbering). Supplementary full-tree grep for Log/concat uses of a stream variable: zero hits (TorrentStreamServer concatenates `stream.id`/`stream.fileSize`, never the stream itself); no `stream.toString()` call in grep §G; res grep §I zero. Flips to REACHABLE on any printed log/concat/toString caller. |
| 38 | TorrentStream.writeToParcel | (Landroid/os/Parcel;I)V | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Def TorrentStream.java:79-91 (fresh numbering). No printed putParcelable site in saved full-tree grep §D; framework calls writeToParcel only when the object is parceled. Flips together with rows 31, 34, 40 and batch 42 row 1 on one printed parceling site. |
| 39 | TorrentStream$1.<init> | ()V | REACHABLE | INFERRED | Anonymous Parcelable.Creator, static CREATOR field initialiser (TorrentStream.java:101-115). Runs on TorrentStream class load (row 30); numbering inferred from source order — merger must confirm against bytecode. Carried-forward. |
| 40 | TorrentStream$1.createFromParcel | (Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/stream/TorrentStream; | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. TorrentStream.java:96-100 (fresh numbering; `return new TorrentStream(source)`). Framework Parcelable dispatch only; no printed unparcel site in saved full-tree grep §D. Flips together with rows 31, 34, 38 and batch 42 row 1 on one printed parceling site. |

## Counts (mechanically verified in this pass: 40 rows, sequence 1-40 intact)

- REACHABLE proposed: 27 (SOURCE 14, INFERRED 13)
- UNREACHABLE proposed: 12 (all INFERRED; 2026-11-01 revision, was 0)
- OPEN: 1 (row 11 only; 2026-11-01 revision, was 13)
- Total: 40. **0 rows verified for merge** — main-agent spot-check 1 in 5, py_compile,
  build, and Mac build/C1 are all still outstanding and are marked not run, never passed.

## OPEN items and what resolves them

- Row 11 (finalize): CONDITIONAL under convention (vi) — REACHABLE INFERRED if GC dispatch counts as a route (object created on the printed row-8 route), OPEN if it does not / while (vi) is undecided; never UNREACHABLE on this evidence. Resolved by a printed GC/finalizer dispatch or a project (vi) decision, not by an app-tree grep.
- Row 12 (markSupported): a printed caller, or a saved full-repo grep for `.markSupported()`.
- Rows 14, 15 (read overloads not used by NanoHTTPD sendBody): a second stream consumer.
- Rows 27, 28 (Piece equals/hashCode): a collection/equals caller.
- Rows 31, 34, 38, 40 (TorrentStream Parcelable quartet, plus batch 42 row 1 newArray):
  one printed putParcelable/getParcelable site passing a TorrentStream.
- Rows 35, 36, 37 (TorrentStream equals/hashCode/toString): one printed caller each.
- No row in this batch is labelled UNREACHABLE: none meets the bar of exactly one kind
  + reason + source reference on printed evidence.
