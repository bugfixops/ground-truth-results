# Batch 19 source audit

Membership is the 40 rows in `batch_019_plan.txt`. Printed source findings are in `batch_019_helper_printed.txt`; independent FixedRingBuffer and Logger prints are in `batch_019_independent_printed.txt`.

Seven FixedRingBuffer methods/overloads have no app-source caller and are labeled UNREACHABLE `no_trigger_in_app`. The helper identified 29 additional source-local paths, but I have not added their complete graph entry routes; those remain OPEN. The four helper OPEN rows remain OPEN for Rx/libtorrent callback dispatch. No coverage evidence was used.

| Method | Label | Evidence / reason |
|---|---|---|
| `TorrentBuilder.lambda$build$0` | OPEN | Rx `Single.fromCallable` execution outside printed app source; `TorrentBuilder.java:173-178`; `CreateTorrentViewModel.java:171-174`. |
| `TorrentBuilder.observeProgress` | OPEN | Called from ViewModel; complete screen entry path not handwritten; `CreateTorrentViewModel.java:151-170`; `TorrentBuilder.java:168-171`. |
| `TorrentBuilder.setAsPrivate(boolean)` | OPEN | App calls in makeBuilder; complete screen entry path not handwritten; `CreateTorrentViewModel.java:189-199`. |
| `TorrentBuilder.setComment(String)` | OPEN | App calls in makeBuilder; complete screen entry path not handwritten; `CreateTorrentViewModel.java:189-199`. |
| `TorrentBuilder.setCreator(String)` | OPEN | App calls in makeBuilder; complete screen entry path not handwritten; `CreateTorrentViewModel.java:189-199`. |
| `TorrentBuilder.setFileNameFilter(Predicate)` | OPEN | App calls in makeBuilder; complete screen entry path not handwritten; `CreateTorrentViewModel.java:189-208`. |
| `TorrentBuilder.setPieceSize(int)` | OPEN | App calls in makeBuilder; complete screen entry path not handwritten; `CreateTorrentViewModel.java:189-199`. |
| `TorrentBuilder.setSeedPath(Uri)` | OPEN | App calls in makeBuilder; complete screen entry path not handwritten; `CreateTorrentViewModel.java:177-199`. |
| `TorrentBuilder.setTorrentVersion(TorrentVersion)` | OPEN | App calls in makeBuilder; complete screen entry path not handwritten; `CreateTorrentViewModel.java:189-199`. |
| `TorrentBuilder.subscribeProgress` | OPEN | Called by build(); full screen entry path not handwritten; `TorrentBuilder.java:173-183`. |
| `TorrentBuilder$1.<init>` | OPEN | Constructed by subscribeProgress; full screen route not handwritten; `TorrentBuilder.java:180-183`. |
| `TorrentBuilder$1.accept(String)` | OPEN | Registered libtorrent4j listener; callback dispatch outside uploaded source; `TorrentBuilder.java:182-192`. |
| `TorrentBuilder$1.progress(int,int)` | OPEN | Registered libtorrent4j listener; callback dispatch outside uploaded source; `TorrentBuilder.java:194-198`. |
| `TorrentBuilder$Progress.<init>(int,int)` | OPEN | Constructed in listener callback; libtorrent4j callback dispatch OPEN; `TorrentBuilder.java:194-198`. |
| `TorrentBuilder$TorrentVersion.<clinit>` | OPEN | Enum used in makeBuilder; complete screen route not handwritten; `CreateTorrentViewModel.java:189-199,338-350`. |
| `TorrentBuilder$TorrentVersion.<init>(String,int,create_flags_t)` | OPEN | Enum initialization; screen route not handwritten; `TorrentBuilder.java:72-85`; `CreateTorrentViewModel.java:338-350`. |
| `TorrentBuilder$TorrentVersion.flag` | OPEN | Called by setTorrentVersion; screen route not handwritten; `TorrentBuilder.java:162-165`. |
| `TorrentBuilder$Tracker.<init>(String,int)` | OPEN | Constructed by makeBuilder helper; screen route not handwritten; `CreateTorrentViewModel.java:264-278`. |
| `TorrentFileObserver.<init>(String)` | OPEN | TorrentEngine directory watch path exists; complete engine entry route not handwritten; `TorrentEngine.java:1116-1125,1136-1138`. |
| `FixedRingBuffer.<init>(int,int)` | OPEN | Logger constructs it; complete logging entry route not handwritten; `Logger.java:65-91`. |
| `FixedRingBuffer.add(Iterable)` | UNREACHABLE | no_trigger_in_app; Logger uses single LogEntry overload only. `FixedRingBuffer.java:80-84`; `Logger.java:99-110,139-156`. |
| `FixedRingBuffer.add(Object)` | OPEN | Logger invokes single-item add; complete logging entry route not handwritten; `Logger.java:99-110,139-156`. |
| `FixedRingBuffer.clear` | OPEN | Logger filter path calls it; complete route not handwritten; `Logger.java:244-256`. |
| `FixedRingBuffer.contains` | UNREACHABLE | no_trigger_in_app; no app caller. `FixedRingBuffer.java:179-188`; helper call search. |
| `FixedRingBuffer.get(int)` | OPEN | Logger reads entries; complete logging entry route not handwritten; `Logger.java:139-156,281-312,425-442`. |
| `FixedRingBuffer.getAllocatedSize` | UNREACHABLE | no_trigger_in_app; full source search shows no caller. `FixedRingBuffer.java:75-78`; independent print. |
| `FixedRingBuffer.indexOf` | UNREACHABLE | no_trigger_in_app; only called by unused remove. `FixedRingBuffer.java:99-123`. |
| `FixedRingBuffer.isEmpty` | OPEN | Logger calls it; complete logging entry route not handwritten; `Logger.java:139-147`. |
| `FixedRingBuffer.isFull` | UNREACHABLE | no_trigger_in_app; no app caller. `FixedRingBuffer.java:174-177`; helper call search. |
| `FixedRingBuffer.iterator` | OPEN | Logger enhanced-for uses it; complete route not handwritten; `Logger.java:244-256`. |
| `FixedRingBuffer.remove(Object)` | UNREACHABLE | no_trigger_in_app; no source caller. `FixedRingBuffer.java:99-110`; helper call search. |
| `FixedRingBuffer.removeAt(int)` | UNREACHABLE | no_trigger_in_app; only called by unused remove overload. `FixedRingBuffer.java:99-110,125-148`. |
| `FixedRingBuffer.resetHead` | OPEN | Called by clear; complete logging entry route not handwritten; `FixedRingBuffer.java:159-167,190-194`. |
| `FixedRingBuffer.size` | OPEN | Used by buffer and Logger; complete logging entry route not handwritten; `Logger.java:139-152,281-312,337-338,385-418,445-453`. |
| `FixedRingBuffer.tryGrow` | OPEN | Called by reachable candidate add(Object); complete route not handwritten; `FixedRingBuffer.java:86-97`. |
| `FixedRingBuffer$FixedRingBufferIterator.<init>` | OPEN | Constructed by iterator; complete Logger route not handwritten; `FixedRingBuffer.java:207-215`; `Logger.java:244-256`. |
| `FixedRingBuffer$FixedRingBufferIterator.hasNext` | OPEN | Enhanced-for callback; full logging route not handwritten; `FixedRingBuffer.java:218-222`. |
| `FixedRingBuffer$FixedRingBufferIterator.next` | OPEN | Enhanced-for callback; full logging route not handwritten; `FixedRingBuffer.java:224-228`. |
| `DecodeException.<init>(Exception)` | OPEN | Thrown by metainfo parser paths; full app caller route not handwritten; `TorrentMetaInfo.java:60-93`; `TorrentEngine.java:378-391`. |
| `FetchLinkException.<init>(Exception)` | OPEN | Thrown by HTTP fetch path; complete app entry route not handwritten; `Utils.java:462-475`; `core/FeedParser.java:62-71`. |

Count: 40 plan rows; 0 REACHABLE; 7 `UNREACHABLE/no_trigger_in_app`; 33 OPEN. No coverage evidence was used.
