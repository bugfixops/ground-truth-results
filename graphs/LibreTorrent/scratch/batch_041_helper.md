# Batch 41 helper report

Membership is exactly the 40 rows with `batch==41` in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; the plan TSV is the sole membership source. Definitions and focused callback/caller excerpts are recorded in `scratch/batch_041_helper_printed.txt`. This review did not complete app-entry routes for these targets; uncertain rows remain OPEN.

| Method | Label | Kind | Reason | Printed evidence |
|---|---|---|---|---|
| `TorrentSessionImpl$InnerListener.lambda$alert$1` | OPEN | — | Captured listener callback in ADD_TORRENT dispatch; alert entry path not established. | `TorrentSessionImpl.java:1073-1090` |
| `TorrentSessionImpl$InnerListener.types` | OPEN | — | Registered alert listener method; framework/library invocation route not verified. | `TorrentSessionImpl.java:1061-1070` |
| `TorrentSessionImpl$LoadTorrentTask.<init>` | OPEN | — | Task is created by session load scheduling, but complete app-entry route not recorded. | `TorrentSessionImpl.java:1480-1492`; call-site search |
| `TorrentSessionImpl$LoadTorrentTask.lambda$run$0` | OPEN | — | Lambda callback in task run flow; route not established from app entry. | `TorrentSessionImpl.java:1507-1529` |
| `TorrentSessionImpl$LoadTorrentTask.putMagnet` | OPEN | — | Called when a load task is prepared for a magnet; full entry route not established. | `TorrentSessionImpl.java:1494-1505`; `TorrentSessionImpl.java:414` |
| `TorrentSessionImpl$LoadTorrentTask.run` | OPEN | — | Runnable is queued by session scheduling; complete entry route not traced. | `TorrentSessionImpl.java:1507-1530`; `TorrentSessionImpl.java:1468-1472` |
| `TorrentInputStream.<clinit>` | OPEN | — | Static initialization occurs upon use; app entry path not recorded. | `TorrentInputStream.java:51-62`; stream server construction sites |
| `TorrentInputStream.<init>` | OPEN | — | Created by engine stream factory and TorrentStreamServer; complete HTTP/stream entry chain not established. | `TorrentInputStream.java:97-119`; `TorrentStreamServer.java:206-209,243-248` |
| `TorrentInputStream.close` | OPEN | — | InputStream close implementation read; client/framework call route not established. | `TorrentInputStream.java:360-372` |
| `TorrentInputStream.filePosToPiecePos` | OPEN | — | Internal read helper; entry depends on untraced stream read call. | `TorrentInputStream.java:169-178,219-227` |
| `TorrentInputStream.finalize` | OPEN | — | Runtime finalization callback route not established. | `TorrentInputStream.java:121-130` |
| `TorrentInputStream.markSupported` | OPEN | — | InputStream API method; no app/framework caller route established. | `TorrentInputStream.java:404-408` |
| `TorrentInputStream.pieceFinished` | OPEN | — | Called by registered listener; callback dispatch route not established. | `TorrentInputStream.java:421-434` |
| `TorrentInputStream.read()` | OPEN | — | Stream-server response uses this stream, but complete HTTP request-to-read route not traced. | `TorrentInputStream.java:195-254`; `TorrentStreamServer.java:206-209,243-248` |
| `TorrentInputStream.read(byte[])` | OPEN | — | Delegates to ranged read; caller route not established. | `TorrentInputStream.java:354-358` |
| `TorrentInputStream.read(byte[],int,int)` | OPEN | — | Stream-server response uses this stream; complete client request route not established. | `TorrentInputStream.java:256-352`; `TorrentStreamServer.java:206-209,243-248` |
| `TorrentInputStream.readFromCache` | OPEN | — | Private helper called by read methods; full app entry route not established. | `TorrentInputStream.java:180-184,229-235` |
| `TorrentInputStream.readPiece` | OPEN | — | Called by registered TorrentEngineListener; event path not fully established. | `TorrentInputStream.java:410-419,436-455` |
| `TorrentInputStream.skip` | OPEN | — | Called by server for HTTP range response; full request route not traced. | `TorrentInputStream.java:374-402`; `TorrentStreamServer.java:206-209` |
| `TorrentInputStream.toUnsignedByte` | OPEN | — | Internal read conversion helper; full app entry route not established. | `TorrentInputStream.java:190-193,234-248` |
| `TorrentInputStream.waitForPiece` | OPEN | — | Internal read helper; full app entry route not established. | `TorrentInputStream.java:135-148,239-242` |
| `TorrentInputStream.waitForReadPieces` | OPEN | — | Internal read helper; full app entry route not established. | `TorrentInputStream.java:150-163,244-248` |
| `TorrentInputStream$1.<init>` | OPEN | — | Listener instance is initialized as a field; outer stream construction route not fully traced. | `TorrentInputStream.java:97-119,410-429` |
| `TorrentInputStream$1.onPieceFinished` | OPEN | — | Registered listener callback; complete torrent alert route not established. | `TorrentInputStream.java:421-429`; `TorrentDownloadImpl.java:256-261` |
| `TorrentInputStream$1.onReadPiece` | OPEN | — | Registered listener callback; complete torrent alert route not established. | `TorrentInputStream.java:412-419`; `TorrentDownloadImpl.java:442-454` |
| `TorrentInputStream$Piece.<init>` | OPEN | — | Piece records are constructed in read methods; complete stream entry route not established. | `TorrentInputStream.java:71-82,219-227` |
| `TorrentInputStream$Piece.equals` | OPEN | — | No proven map/set call route for equality in this review. | `TorrentInputStream.java:90-94`; focused source search |
| `TorrentInputStream$Piece.hashCode` | OPEN | — | No proven map/set call route for hashCode in this review. | `TorrentInputStream.java:84-88`; focused source search |
| `TorrentInputStream$ReadSession.<init>` | OPEN | — | Implicit constructor; ReadSession is allocated from read; full entry route not established. | `TorrentInputStream.java:64-69,219-223` |
| `TorrentStream.<clinit>` | OPEN | — | Static initialization upon class use; complete entry route not recorded. | `TorrentStream.java:29-53,93-107`; stream server caller search |
| `TorrentStream.<init>(Parcel)` | OPEN | — | Parcel constructor is present; no app Parcelable dispatch route established. | `TorrentStream.java:55-66,93-107`; printed Parcelable search |
| `TorrentStream.<init>(String,int,int,int,int,long,long,int)` | OPEN | — | Definition read; complete app caller route not established. | `TorrentStream.java:40-53`; focused call-site search |
| `TorrentStream.bytesToPieceIndex` | OPEN | — | Used by TorrentInputStream read/skip paths; full entry route not established. | `TorrentStream.java:68-71`; `TorrentInputStream.java:215-217,392-394` |
| `TorrentStream.describeContents` | OPEN | — | Parcelable callback; app parcel dispatch route not established. | `TorrentStream.java:73-77`; printed Parcelable search |
| `TorrentStream.equals` | OPEN | — | No hand-written equality route established. | `TorrentStream.java:117-130`; focused call-site search |
| `TorrentStream.hashCode` | OPEN | — | No hand-written hash route established. | `TorrentStream.java:109-113`; focused call-site search |
| `TorrentStream.toString` | OPEN | — | No hand-written string conversion route established. | `TorrentStream.java:132-145`; focused call-site search |
| `TorrentStream.writeToParcel` | OPEN | — | Parcelable override, but framework dispatch route is not established. | `TorrentStream.java:79-107`; printed Parcelable search |
| `TorrentStream$1.<init>` | OPEN | — | CREATOR construction is in the static field initializer; complete class-init entry route not recorded. | `TorrentStream.java:93-107` |
| `TorrentStream$1.createFromParcel` | OPEN | — | No app parcel dispatch route established. | `TorrentStream.java:93-107`; printed Parcelable search |

Count: 40 plan rows; 0 REACHABLE; 0 UNREACHABLE; 40 OPEN. No coverage evidence was used. These helper labels are source research only, not graph edits.
