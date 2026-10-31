# LibreTorrent batch 19 helper audit

Membership is restricted to batch 19 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`. Its plan query printed 40 methods. Source output and focused caller searches are in `scratch/batch_019_helper_printed.txt`.

OPEN means the full route depends on an external callback/library edge or another source path not established in this audit. No graph, notes, output, or coverage files were changed.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `TorrentBuilder.lambda$build$0` | OPEN | Source lambda is in `build()` (`TorrentBuilder.java:173-178`), subscribed by `CreateTorrentViewModel.buildTorrent` (`CreateTorrentViewModel.java:171-174`); execution of Rx `Single.fromCallable` depends on external Rx behavior. |
| 2 | `TorrentBuilder.observeProgress` | REACHABLE | `CreateTorrentViewModel.buildTorrent` calls `builder.observeProgress()` (`CreateTorrentViewModel.java:151-170`); builder method returns its subject (`TorrentBuilder.java:168-171`). |
| 3 | `TorrentBuilder.setAsPrivate(boolean)` | REACHABLE | App `makeBuilder()` calls it (`CreateTorrentViewModel.java:189-199`); implementation is in `TorrentBuilder.java:134-139`. |
| 4 | `TorrentBuilder.setComment(String)` | REACHABLE | App `makeBuilder()` calls it (`CreateTorrentViewModel.java:189-199`); implementation is in `TorrentBuilder.java:148-153`. |
| 5 | `TorrentBuilder.setCreator(String)` | REACHABLE | App `makeBuilder()` calls it (`CreateTorrentViewModel.java:189-199`); implementation is in `TorrentBuilder.java:141-146`. |
| 6 | `TorrentBuilder.setFileNameFilter(Predicate)` | REACHABLE | App `makeBuilder()` calls it with a predicate (`CreateTorrentViewModel.java:189-208`); implementation is in `TorrentBuilder.java:155-160`. |
| 7 | `TorrentBuilder.setPieceSize(int)` | REACHABLE | App `makeBuilder()` calls it (`CreateTorrentViewModel.java:189-199`); implementation is in `TorrentBuilder.java:109-114`. |
| 8 | `TorrentBuilder.setSeedPath(Uri)` | REACHABLE | App `makeBuilder()` calls it (`CreateTorrentViewModel.java:177-199`); implementation is in `TorrentBuilder.java:94-101`. |
| 9 | `TorrentBuilder.setTorrentVersion(TorrentVersion)` | REACHABLE | App `makeBuilder()` calls it (`CreateTorrentViewModel.java:189-199`); implementation is in `TorrentBuilder.java:162-166`. |
| 10 | `TorrentBuilder.subscribeProgress()` | REACHABLE | `TorrentBuilder.build()` calls it (`TorrentBuilder.java:173-178`); `CreateTorrentViewModel.buildTorrent` calls `builder.build()` and subscribes (`CreateTorrentViewModel.java:171-174`). |
| 11 | `TorrentBuilder$1.<init>` | REACHABLE | `subscribeProgress()` directly constructs the anonymous `org.libtorrent4j.TorrentBuilder.Listener` (`TorrentBuilder.java:180-183`). |
| 12 | `TorrentBuilder$1.accept(String)` | OPEN | Registered listener method body is printed (`TorrentBuilder.java:182-192`), but libtorrent4j callback invocation is outside the uploaded source. |
| 13 | `TorrentBuilder$1.progress(int,int)` | OPEN | Registered listener method body is printed (`TorrentBuilder.java:194-198`), but libtorrent4j callback invocation is outside the uploaded source. |
| 14 | `TorrentBuilder$Progress.<init>(int,int)` | OPEN | Constructed from listener callback `progress()` (`TorrentBuilder.java:194-198`); callback invocation remains OPEN. |
| 15 | `TorrentBuilder$TorrentVersion.<clinit>` | REACHABLE | `CreateTorrentViewModel.makeBuilder()` passes a version (`CreateTorrentViewModel.java:189-199`); `getTorrentVersionByIndex()` selects enum values (`CreateTorrentViewModel.java:338-350`), initializing the enum class. |
| 16 | `TorrentBuilder$TorrentVersion.<init>(String,int,create_flags_t)` | REACHABLE | Enum constants call this constructor (`TorrentBuilder.java:72-85`); version values are selected by the app (`CreateTorrentViewModel.java:338-350`). |
| 17 | `TorrentBuilder$TorrentVersion.flag()` | REACHABLE | `setTorrentVersion()` calls `version.flag()` (`TorrentBuilder.java:162-165`); `makeBuilder()` calls `setTorrentVersion` (`CreateTorrentViewModel.java:189-199`). |
| 18 | `TorrentBuilder$Tracker.<init>(String,int)` | REACHABLE | `CreateTorrentViewModel.getAndValidateTrackers()` constructs trackers in its URL loop (`CreateTorrentViewModel.java:264-278`), called by `makeBuilder()` (`:189-199`). |
| 19 | `TorrentFileObserver.<init>(String)` | REACHABLE | `TorrentEngine.startWatchDir()` calls `makeTorrentFileObserver(dir)` (`TorrentEngine.java:1116-1125`), which directly constructs it (`:1136-1138`); watch-directory setting paths call `startWatchDir` (`TorrentEngine.java:1053-1054,1581-1590`). |
| 20 | `FixedRingBuffer.<init>(int,int)` | REACHABLE | `Logger.lazyGetInputBuf()` and `lazyGetOutputBuf()` instantiate it (`Logger.java:65-91`); the session logger is used by engine logging/UI routes. |
| 21 | `FixedRingBuffer.add(Iterable)` | UNREACHABLE `no_trigger_in_app` | Body delegates to `add(E)` (`FixedRingBuffer.java:80-84`); source caller search found no call to this overload. `Logger` calls `add(entry)` with a single `LogEntry` (`Logger.java:99-110,139-156`). |
| 22 | `FixedRingBuffer.add(Object)` | REACHABLE | `Logger.send` calls `lazyGetInputBuf().add(entry)` and `swapBuffers` calls `outputBuf.add(entry)` (`Logger.java:99-110,139-156`). |
| 23 | `FixedRingBuffer.clear()` | REACHABLE | `Logger.forceFilterBuf()` calls `outputBuf.clear()` (`Logger.java:244-256`); filter updates can invoke that helper (`Logger.java:202-240`). |
| 24 | `FixedRingBuffer.contains(Object)` | UNREACHABLE `no_trigger_in_app` | Method body printed (`FixedRingBuffer.java:179-188`); focused caller search found no use of this buffer method. |
| 25 | `FixedRingBuffer.get(int)` | REACHABLE | `Logger` reads entries in swaps, getters, and writes (`Logger.java:139-156,281-312,425-442`). |
| 26 | `FixedRingBuffer.getAllocatedSize()` | UNREACHABLE `no_trigger_in_app` | Method body printed (`FixedRingBuffer.java:75-78`); focused caller search found no use of this buffer method. |
| 27 | `FixedRingBuffer.indexOf(Object)` | UNREACHABLE `no_trigger_in_app` | Only called by `FixedRingBuffer.remove(E)` (`FixedRingBuffer.java:99-123`); no source caller of this buffer's `remove` overload was found. |
| 28 | `FixedRingBuffer.isEmpty()` | REACHABLE | `Logger.swapBuffers()` checks `inputBuf.isEmpty()` (`Logger.java:139-147`); `FixedRingBuffer.clear()` also uses it (`FixedRingBuffer.java:159-166`). |
| 29 | `FixedRingBuffer.isFull()` | UNREACHABLE `no_trigger_in_app` | Method body printed (`FixedRingBuffer.java:174-177`); focused caller search found no use of this buffer method. |
| 30 | `FixedRingBuffer.iterator()` | REACHABLE | `Logger.forceFilterBuf()` iterates over `inputBuf` (`Logger.java:244-256`); iterator creates the nested iterator (`FixedRingBuffer.java:207-212`). |
| 31 | `FixedRingBuffer.remove(Object)` | UNREACHABLE `no_trigger_in_app` | Method body printed (`FixedRingBuffer.java:99-110`); no caller of this buffer method found in the only source user, `Logger`. |
| 32 | `FixedRingBuffer.removeAt(int)` | UNREACHABLE `no_trigger_in_app` | Only called from `remove(E)` (`FixedRingBuffer.java:99-110,125-148`); no `remove` caller found in `Logger` or other source. |
| 33 | `FixedRingBuffer.resetHead()` | REACHABLE | Called by reachable `clear()` (`FixedRingBuffer.java:159-167,190-194`). |
| 34 | `FixedRingBuffer.size()` | REACHABLE | Called internally by buffer operations and from `Logger` (`FixedRingBuffer.java:65-73`; `Logger.java:139-152,281-312,337-338,385-418,445-453`). |
| 35 | `FixedRingBuffer.tryGrow()` | REACHABLE | Called by `add(E)` (`FixedRingBuffer.java:86-97`), which `Logger` invokes (`Logger.java:99-110,139-156`). |
| 36 | `FixedRingBuffer$FixedRingBufferIterator.<init>` | REACHABLE | Constructed by `iterator()` (`FixedRingBuffer.java:207-215`), used by Logger's enhanced for loop (`Logger.java:244-256`). |
| 37 | `FixedRingBuffer$FixedRingBufferIterator.hasNext()` | REACHABLE | Iterator callback used by Logger's enhanced for loop (`Logger.java:244-256`); method body at `FixedRingBuffer.java:218-222`. |
| 38 | `FixedRingBuffer$FixedRingBufferIterator.next()` | REACHABLE | Iterator callback used by Logger's enhanced for loop (`Logger.java:244-256`); method body at `FixedRingBuffer.java:224-228`. |
| 39 | `DecodeException.<init>(Exception)` | REACHABLE | App parser methods throw it when bencode decoding fails (`TorrentMetaInfo.java:60-93`); engine also wraps decode exceptions (`TorrentEngine.java:378-391`). |
| 40 | `FetchLinkException.<init>(Exception)` | REACHABLE | `Utils.fetchHttpUrl()` throws it from its connection-construction catch (`Utils.java:462-475`); app feed parsing calls `fetchHttpUrl` (`core/FeedParser.java:62-71`). |

Table totals: 40 rows = 29 REACHABLE, 7 UNREACHABLE (`no_trigger_in_app`), 4 OPEN. The two listener callback methods and the progress constructor remain OPEN pending libtorrent4j callback evidence; the synthetic Rx lambda remains OPEN pending the `Single.fromCallable` execution route.
