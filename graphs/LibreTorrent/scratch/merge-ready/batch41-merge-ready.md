# LibreTorrent batch 41 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
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
| 11 | TorrentInputStream.finalize | ()V | OPEN | — | GC finalizer (TorrentInputStream.java:122-133, stopped=true, session.removeListener). No printed app caller and no printed GC/finalizer dispatch in any file printed for this batch, including the fresh files in this pass. NOT UNREACHABLE on this evidence: a stream that becomes unreachable after serving could be finalized, but that is not a printed route. Needs a framework/GC citation or a project decision on whether finalizers count as routes — the same undecided convention as the Room Callable finalize() rows in batches 51-52; recorded, not decided. Do not label on absence alone. |
| 12 | TorrentInputStream.markSupported | ()Z | OPEN | — | Returns false (TorrentInputStream.java:405-408). No printed caller in the prior fetched corpus (NanoHTTPD sendBody does not call mark/markSupported) and none in the fresh files in this pass. Needs a printed caller or a saved full-repo grep for `.markSupported()`. NOT UNREACHABLE on absence alone. |
| 13 | TorrentInputStream.pieceFinished | ()V | REACHABLE | INFERRED | TorrentInputStream.java:422-429 listener.onPieceFinished -> pieceFinished() (:431-435, notifyAll). Listener callback dispatch via notifyListeners INFERRED; internal call printed. Carried-forward. |
| 14 | TorrentInputStream.read() | ()I | OPEN | — | Single-byte read (TorrentInputStream.java:196-256). NanoHTTPD sendBody calls the 3-arg overload only (NanoHTTPD.java:1267 this.data.read(buff, 0, bytesToRead)), NOT read(). No other printed caller in the prior corpus or the fresh files in this pass. Needs a printed caller (e.g. another stream consumer) or a saved full-repo grep. NOT UNREACHABLE on absence alone. |
| 15 | TorrentInputStream.read(byte[]) | ([B)I | OPEN | — | Same as row 14: delegates to 3-arg read (TorrentInputStream.java:355-359), but NanoHTTPD sendBody calls 3-arg directly, so this overload has no printed caller. Needs a printed caller or a saved full-repo grep. |
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
| 27 | TorrentInputStream$Piece.equals | (Ljava/lang/Object;)Z | OPEN | — | Def TorrentInputStream.java:91-95. readPiece (:436-470) compares p.index == info.piece, NOT Piece.equals; no HashMap/HashSet of Piece printed in the prior corpus or the fresh files in this pass. Needs a printed equals caller or a saved full-repo grep. NOT UNREACHABLE on absence alone. |
| 28 | TorrentInputStream$Piece.hashCode | ()I | OPEN | — | Def TorrentInputStream.java:85-89 (return index). Same as row 27: no printed hash caller. Needs a printed caller or a saved full-repo grep. |
| 29 | TorrentInputStream$ReadSession.<init> | (Lorg/proninyaroslav/libretorrent/core/model/stream/TorrentInputStream;)V | REACHABLE | SOURCE | Implicit default ctor. TorrentInputStream.java:225 new ReadSession() in read(); :~295 new ReadSession() in read(byte[],int,int). Carried-forward. |
| 30 | TorrentStream.<clinit> | ()V | REACHABLE | INFERRED | Static CREATOR field (TorrentStream.java:101-115). JVM class initialisation on first use via TorrentDownloadImpl.getStream :1607-1625; init ordering JVM semantics, not a printed line. Carried-forward. |
| 31 | TorrentStream.<init>(Parcel) | (Landroid/os/Parcel;)V | OPEN | — | Only via CREATOR.createFromParcel (row 40), which itself has no printed unparcel site. No printed Intent-extra/Bundle putParcelable/getParcelable site passing a TorrentStream in the prior corpus or the fresh files in this pass. Needs such a site or a saved full-repo grep for TorrentStream parceling. NOT UNREACHABLE on absence alone (framework could unparcel it). Flips together with rows 34, 38, 40 and batch 42 row 1 on one printed parceling site. |
| 32 | TorrentStream.<init>(String,int,int,int,int,long,long,int) | (Ljava/lang/String;IIIIJJI)V | REACHABLE | SOURCE | TorrentDownloadImpl.java:1621 new TorrentStream(id, fileIndex, filePieces.first, filePieces.second, ti.pieceLength(), fs.fileOffset(fileIndex), fs.fileSize(fileIndex), ti.pieceSize(filePieces.second)) in getStream. Def TorrentStream.java:35-50. Carried-forward. |
| 33 | TorrentStream.bytesToPieceIndex | (J)I | REACHABLE | SOURCE | TorrentInputStream.java:196-256 read() (bytesToPieceIndex(filePos + 1)); :257-354 read(byte[],int,int); :375-404 skip() (bytesToPieceIndex(filePos + 1)). Def TorrentStream.java:60-63. Carried-forward. |
| 34 | TorrentStream.describeContents | ()I | OPEN | — | Parcelable, returns 0 (TorrentStream.java:71-75). No printed caller. Framework Parcelable method; needs a printed parceling site or a saved full-repo grep. NOT UNREACHABLE on absence alone. See row 31. |
| 35 | TorrentStream.equals | (Ljava/lang/Object;)Z | OPEN | — | Def TorrentStream.java:117-121 (id comparison). No printed caller in the prior corpus or the fresh files in this pass; stream.id is read directly elsewhere (e.g. TorrentStreamServer handleTorrent etag = stream.id), not via equals. Needs a printed caller or a saved full-repo grep. |
| 36 | TorrentStream.hashCode | ()I | OPEN | — | Def TorrentStream.java:113-116 (id.hashCode()). Same as row 35: no printed caller. |
| 37 | TorrentStream.toString | ()Ljava/lang/String; | OPEN | — | Def TorrentStream.java:123-137. No printed log/concat caller in the prior corpus or the fresh files in this pass. Needs a printed caller or a saved full-repo grep. |
| 38 | TorrentStream.writeToParcel | (Landroid/os/Parcel;I)V | OPEN | — | Def TorrentStream.java:78-90. No printed putParcelable site. Needs a printed parceling site or a saved full-repo grep. See row 31. |
| 39 | TorrentStream$1.<init> | ()V | REACHABLE | INFERRED | Anonymous Parcelable.Creator, static CREATOR field initialiser (TorrentStream.java:101-115). Runs on TorrentStream class load (row 30); numbering inferred from source order — merger must confirm against bytecode. Carried-forward. |
| 40 | TorrentStream$1.createFromParcel | (Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/stream/TorrentStream; | OPEN | — | TorrentStream.java:106-110 return new TorrentStream(source). Framework Parcelable dispatch only; no printed unparcel site in the prior corpus or the fresh files in this pass. Needs a printed read site or a saved full-repo grep. NOT UNREACHABLE on absence alone. See row 31. |

## Counts (mechanically verified in this pass: 40 rows, sequence 1-40 intact)

- REACHABLE proposed: 27 (SOURCE 14, INFERRED 13)
- UNREACHABLE proposed: 0
- OPEN: 13 (rows 11, 12, 14, 15, 27, 28, 31, 34, 35, 36, 37, 38, 40)
- Total: 40. **0 rows verified for merge** — main-agent spot-check 1 in 5, py_compile,
  build, and Mac build/C1 are all still outstanding and are marked not run, never passed.

## OPEN items and what resolves them

- Row 11 (finalize): a framework/GC citation, or the undecided finalizer convention.
- Row 12 (markSupported): a printed caller, or a saved full-repo grep for `.markSupported()`.
- Rows 14, 15 (read overloads not used by NanoHTTPD sendBody): a second stream consumer.
- Rows 27, 28 (Piece equals/hashCode): a collection/equals caller.
- Rows 31, 34, 38, 40 (TorrentStream Parcelable quartet, plus batch 42 row 1 newArray):
  one printed putParcelable/getParcelable site passing a TorrentStream.
- Rows 35, 36, 37 (TorrentStream equals/hashCode/toString): one printed caller each.
- No row in this batch is labelled UNREACHABLE: none meets the bar of exactly one kind
  + reason + source reference on printed evidence.
