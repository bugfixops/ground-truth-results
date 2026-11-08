# LibreTorrent batch 41 source audit

Membership is the exact 40-row set in `scratch/batch_041_plan.txt`. I reviewed source definitions, stream/server callers, listeners and focused use searches in `scratch/batch_041_helper_printed.txt`. Local stream/server callers exist, but the complete HTTP/stream entry chain and listener/library dispatch were not closed. Parcel and finalizer paths are also unresolved. All rows remain OPEN.

| # | Method | Label | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentSessionImpl$InnerListener.lambda$alert$1` | OPEN | ADD_TORRENT listener callback; alert entry path unresolved. |
| 2 | `TorrentSessionImpl$InnerListener.types` | OPEN | Registered alert listener; library invocation unresolved. |
| 3 | `TorrentSessionImpl$LoadTorrentTask.<init>` | OPEN | Session load scheduling caller; app-entry route unresolved. |
| 4 | `TorrentSessionImpl$LoadTorrentTask.lambda$run$0` | OPEN | Task callback; entry route unresolved. |
| 5 | `TorrentSessionImpl$LoadTorrentTask.putMagnet` | OPEN | Load-task magnet preparation; full route unresolved. |
| 6 | `TorrentSessionImpl$LoadTorrentTask.run` | OPEN | Queued Runnable; complete entry route unresolved. |
| 7 | `TorrentInputStream.<clinit>` | OPEN | Static init when used; app entry route not recorded. |
| 8 | `TorrentInputStream.<init>` | OPEN | Engine/server stream factory callers; HTTP entry chain unresolved. |
| 9 | `TorrentInputStream.close` | OPEN | InputStream close; client/framework route unresolved. |
| 10 | `TorrentInputStream.filePosToPiecePos` | OPEN | Internal read helper; stream-read route unresolved. |
| 11 | `TorrentInputStream.finalize` | OPEN | Runtime finalizer dispatch not established. |
| 12 | `TorrentInputStream.markSupported` | OPEN | InputStream method; caller route unresolved. |
| 13 | `TorrentInputStream.pieceFinished` | OPEN | Registered listener callback; delivery unresolved. |
| 14 | `TorrentInputStream.read()` | OPEN | Server uses stream; HTTP request-to-read route unresolved. |
| 15 | `TorrentInputStream.read(byte[])` | OPEN | Delegates to ranged read; caller route unresolved. |
| 16 | `TorrentInputStream.read(byte[],int,int)` | OPEN | Server uses stream; client request route unresolved. |
| 17 | `TorrentInputStream.readFromCache` | OPEN | Internal read helper; outer entry route unresolved. |
| 18 | `TorrentInputStream.readPiece` | OPEN | Registered TorrentEngineListener caller; event path incomplete. |
| 19 | `TorrentInputStream.skip(long)` | OPEN | Server HTTP range caller; request route unresolved. |
| 20 | `TorrentInputStream.toUnsignedByte(int)` | OPEN | Internal read conversion; entry route unresolved. |
| 21 | `TorrentInputStream.waitForPiece(int)` | OPEN | Internal read helper; entry route unresolved. |
| 22 | `TorrentInputStream.waitForReadPieces(int,int)` | OPEN | Internal read helper; entry route unresolved. |
| 23 | `TorrentInputStream$1.<init>` | OPEN | Listener field initialized with stream; stream entry route incomplete. |
| 24 | `TorrentInputStream$1.onPieceFinished(String,int)` | OPEN | Registered listener callback; torrent alert route unresolved. |
| 25 | `TorrentInputStream$1.onReadPiece(String,ReadPieceInfo)` | OPEN | Registered listener callback; torrent alert route unresolved. |
| 26 | `TorrentInputStream$Piece.<init>(int,int)` | OPEN | Piece records created in read methods; stream entry route unresolved. |
| 27 | `TorrentInputStream$Piece.equals(Object)` | OPEN | No proven equality call route in focused source search. |
| 28 | `TorrentInputStream$Piece.hashCode()` | OPEN | No proven hash call route in focused source search. |
| 29 | `TorrentInputStream$ReadSession.<init>` | OPEN | Allocated during read; full entry route unresolved. |
| 30 | `TorrentStream.<clinit>` | OPEN | Static init on use; complete stream entry route absent. |
| 31 | `TorrentStream.<init>(Parcel)` | OPEN | Parcel constructor; app Parcelable dispatch not established. |
| 32 | `TorrentStream.<init>(String,int,int,int,int,long,long,int)` | OPEN | Definition printed; complete caller route absent. |
| 33 | `TorrentStream.bytesToPieceIndex(long)` | OPEN | TorrentInputStream read/skip callers; stream entry route unresolved. |
| 34 | `TorrentStream.describeContents()` | OPEN | Parcelable callback; app dispatch unresolved. |
| 35 | `TorrentStream.equals(Object)` | OPEN | No hand-authored equality route established. |
| 36 | `TorrentStream.hashCode()` | OPEN | No hand-authored hash route established. |
| 37 | `TorrentStream.toString()` | OPEN | No hand-authored string route established. |
| 38 | `TorrentStream.writeToParcel(Parcel,int)` | OPEN | Parcelable override; framework dispatch unresolved. |
| 39 | `TorrentStream$1.<init>` | OPEN | Creator is initialized in static field; entry route incomplete. |
| 40 | `TorrentStream$1.createFromParcel(Parcel)` | OPEN | No app Parcel dispatch route established. |

Totals: 40 rows = 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. No graph labels changed, so no graph build was run for this batch.
