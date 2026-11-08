# Batch 21 source audit

Membership is the exact 40 rows in `batch_021_plan.txt`; printed source and call-site evidence are in `batch_021_helper_printed.txt`, with independent AddTorrentParams method evidence in `batch_021_independent_printed.txt`.

The helper supports 33 local source routes, but those still need full hand-authored entry routes. Three rows depend on Rx, Thread, or libtorrent callbacks whose execution dispatch was not sourced. I added four source-supported `no_trigger_in_app` labels for AddTorrentParams' unused parcel constructor/Parcelable method and unused hash/string overrides.

| Method | Label | Evidence / reason |
|---|---|---|
| `LogEntry.toStringWithTimeStamp` | OPEN | SaveLogWorker export path exists; full worker route not handwritten. `Logger.java:425-440`; `SaveLogWorker.java:84-96`. |
| `Logger.<init>(int)` | OPEN | Constructed by SessionLogger; full session entry route not handwritten. `TorrentSessionImpl.java:162-176`; `SessionLogger.java:111-115`. |
| `Logger.addFilter(NewFilter[])` | OPEN | Called by SessionLogger settings path; full route not handwritten. `SessionLogger.java:169-201`; `TorrentSessionImpl.java:1416-1427`. |
| `Logger.applyFilters(LogEntry)` | OPEN | Internal buffer operations call it; complete logger route not handwritten. `Logger.java:139-165,244-256`. |
| `Logger.calcInitBufCapacity(int)` | OPEN | Called by lazy buffer constructors; full entry route not handwritten. `Logger.java:65-91,94-97`. |
| `Logger.clean` | OPEN | Torrent session calls it during stop; full session route not handwritten. `TorrentSessionImpl.java:1015-1037`. |
| `Logger.doClean` | OPEN | Internal callers exist; logger entry route not handwritten. `Logger.java:177-187,475-499`. |
| `Logger.forceFilterBuf` | OPEN | Called by filter mutation; full UI/session route not handwritten. `Logger.java:202-257`; `SessionLogger.java:169-201`. |
| `Logger.getEntries(int,int)` | OPEN | LogDataSource calls it; complete UI route not handwritten. `LogDataSource.java:60-110`. |
| `Logger.getMaxStoredLogs` | OPEN | Session settings reads it; full route not handwritten. `TorrentSessionImpl.java:1408-1414`. |
| `Logger.getNumEntries` | OPEN | LogViewModel calls it; full UI route not handwritten. `LogViewModel.java:162-165`. |
| `Logger.isPaused` | OPEN | LogViewModel reads it; full UI route not handwritten. `LogViewModel.java:65-78`. |
| `Logger.isRecording` | OPEN | ViewModel/worker read it; complete routes not handwritten. `LogViewModel.java:72-75,186-189`; `SaveLogWorker.java:86-95`. |
| `Logger.lambda$submitDataSetChanged$0(DataSetChange)` | OPEN | Passed to Rx sender; execution dispatch external. `Logger.java:168-171`. |
| `Logger.lazyGetInputBuf` | OPEN | Internal calls exist; complete logger entry route not handwritten. `Logger.java:65-83,99-110,139-147`. |
| `Logger.lazyGetOutputBuf` | OPEN | Internal calls exist; complete logger entry route not handwritten. `Logger.java:86-91,139-165,244-256,281-312,337-338,385-418,445-453`. |
| `Logger.observeDataSetChanged` | OPEN | TorrentEngine subscribes; complete engine route not handwritten. `TorrentEngine.java:245-260`; `Logger.java:259-262`. |
| `Logger.pause` | OPEN | ViewModel and worker call it; complete routes not handwritten. `LogViewModel.java:140-149`; `SaveLogWorker.java:84-96`. |
| `Logger.periodicSwapBuffers` | OPEN | Registered as Thread method reference; callback dispatch not source-verified. `Logger.java:65-83`. |
| `Logger.removeFilter(String[])` | OPEN | SessionLogger calls it; full session route not handwritten. `SessionLogger.java:169-201`; `TorrentSessionImpl.java:1416-1427`. |
| `Logger.resume` | OPEN | ViewModel and worker call it; complete routes not handwritten. `LogViewModel.java:151-159`; `SaveLogWorker.java:104-107`. |
| `Logger.send(LogEntry)` | OPEN | Reached through session logger alert dispatch in libtorrent; external callback not source-verified. `SessionLogger.java:117-167`; `TorrentSessionImpl.java:1061-1104`. |
| `Logger.setMaxStoredLogs(int)` | OPEN | Session settings call exists; full session route not handwritten. `TorrentSessionImpl.java:1408-1414`. |
| `Logger.startRecording` | OPEN | LogViewModel calls it; full UI entry route not handwritten. `LogViewModel.java:172-177`. |
| `Logger.stopRecording` | OPEN | ViewModel/session shutdown callers exist; complete routes not handwritten. `LogViewModel.java:179-184`; `TorrentSessionImpl.java:1021-1024`. |
| `Logger.stopRecording(OutputStream,boolean)` | OPEN | SaveLogWorker calls it; worker entry route not handwritten. `SaveLogWorker.java:84-96`; `Logger.java:362-374`. |
| `Logger.submitDataSetChanged(DataSetChange)` | OPEN | Internal callers exist; complete logger route not handwritten. `Logger.java:139-168,244-257,475-499`. |
| `Logger.swapBuffers` | OPEN | Internal callers exist; complete logger route not handwritten. `Logger.java:139-168,271-317,329-338,372-418,445-453`. |
| `Logger.write(OutputStream,boolean)` | OPEN | SaveLogWorker calls it; worker entry route not handwritten. `SaveLogWorker.java:84-96`. |
| `Logger.write(FixedRingBuffer,OutputStream,int,int,boolean)` | OPEN | Called by public write/stop overloads; complete route not handwritten. `Logger.java:372-388,405-420`. |
| `Logger$DataSetChange.<init>(Reason)` | OPEN | Logger.doClean constructs it; full entry route not handwritten. `Logger.java:487-499,527-535`. |
| `Logger$DataSetChange.<init>(Reason,List)` | OPEN | Logger.swapBuffers constructs it; full entry route not handwritten. `Logger.java:139-168`. |
| `Logger$DataSetChange$Reason.<clinit>` | OPEN | Referenced from logger methods; complete logger route not handwritten. `Logger.java:165,256,498`. |
| `Logger$NewFilter.<init>(String,LogFilter)` | OPEN | SessionLogger constructs it; complete route not handwritten. `SessionLogger.java:30-90,169-201`. |
| `AddTorrentParams.<clinit>` | OPEN | Direct app constructors exist; complete caller routes not handwritten. `AddTorrentViewModel.java:510`; `TorrentEngine.java:1187`; `FeedDownloaderWorker.java:178`. |
| `AddTorrentParams.<init>(Parcel)` | UNREACHABLE | no_trigger_in_app; only CREATOR path and no app Parcel transport. `AddTorrentParams.java:77-82,109-113`. |
| `AddTorrentParams.<init>(String,boolean,String,String,Priority[],Uri,boolean,boolean,List,boolean)` | OPEN | App constructors exist; complete caller routes not handwritten. `AddTorrentViewModel.java:510`; `TorrentEngine.java:1187`; `FeedDownloaderWorker.java:178`. |
| `AddTorrentParams.describeContents` | UNREACHABLE | no_trigger_in_app; no app Parcel transport. `AddTorrentParams.java:91-93`. |
| `AddTorrentParams.hashCode` | UNREACHABLE | no_trigger_in_app; no hash-key or hashCode caller. `AddTorrentParams.java:122-125`. |
| `AddTorrentParams.toString` | UNREACHABLE | no_trigger_in_app; no formatting or explicit call. `AddTorrentParams.java:127-142`. |

Count: 40 plan rows; 0 REACHABLE; 4 `UNREACHABLE/no_trigger_in_app`; 36 OPEN. No coverage evidence was used.
