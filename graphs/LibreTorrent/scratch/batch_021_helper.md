# LibreTorrent batch 21 helper audit

Membership comes only from batch 21 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`; its query printed exactly 40 rows. Printed source and caller evidence are in `scratch/batch_021_helper_printed.txt`.

OPEN means the route depends on a framework or library callback whose execution source was not printed. No graph, notes, output, or coverage files were changed.

| # | Method | Finding | Evidence / route note |
|---:|---|---|---|
| 1 | `LogEntry.toStringWithTimeStamp` | REACHABLE | `Logger.write` selects it when `timeStamp` is true (`Logger.java:425-440`); `SaveLogWorker` calls `logger.write(fout,true)` and `stopRecording(fout,true)` (`SaveLogWorker.java:84-96`). |
| 2 | `Logger.<init>(int)` | REACHABLE | `TorrentSessionImpl` constructs `SessionLogger` (`TorrentSessionImpl.java:162-176`); its constructor calls `super(1)` (`SessionLogger.java:111-115`). |
| 3 | `Logger.addFilter(NewFilter[])` | REACHABLE | `SessionLogger.applyFilterParams` calls it (`SessionLogger.java:169-201`); session settings application calls that method (`TorrentSessionImpl.java:1416-1427`). |
| 4 | `Logger.applyFilters(LogEntry)` | REACHABLE | Called while swapping and rebuilding filtered log buffers (`Logger.java:139-165,244-256`). |
| 5 | `Logger.calcInitBufCapacity(int)` | REACHABLE | Called by both lazy buffer constructors (`Logger.java:65-91,94-97`). |
| 6 | `Logger.clean()` | REACHABLE | `TorrentSessionImpl.enableSessionLogger(false)` calls `sessionLogger.clean()` (`TorrentSessionImpl.java:1015-1024`); invoked during session stop (`:1027-1037`). |
| 7 | `Logger.doClean()` | REACHABLE | Called by `clean()` and `setMaxStoredLogs()` (`Logger.java:177-187,475-499`). |
| 8 | `Logger.forceFilterBuf()` | REACHABLE | Called by `addFilter` and `removeFilter` after changes (`Logger.java:202-240,244-257`); SessionLogger applies its filter settings (`SessionLogger.java:169-201`). |
| 9 | `Logger.getEntries(int,int)` | REACHABLE | `LogDataSource` calls it to load log pages (`LogDataSource.java:60-110`). |
| 10 | `Logger.getMaxStoredLogs()` | REACHABLE | Session settings application compares the current max (`TorrentSessionImpl.java:1408-1414`). |
| 11 | `Logger.getNumEntries()` | REACHABLE | `LogViewModel.getLogEntriesCount` calls it (`LogViewModel.java:162-165`). |
| 12 | `Logger.isPaused()` | REACHABLE | `LogViewModel` reads it during initialization (`LogViewModel.java:65-78`). |
| 13 | `Logger.isRecording()` | REACHABLE | `LogViewModel` reads it during initialization and state checks; `SaveLogWorker` also branches on it (`LogViewModel.java:72-75,186-189`; `SaveLogWorker.java:86-95`). |
| 14 | `Logger.lambda$submitDataSetChanged$0(DataSetChange)` | OPEN | Lambda expression is passed to `sender.submit` (`Logger.java:168-171`); RxJava execution is external to the uploaded source. |
| 15 | `Logger.lazyGetInputBuf()` | REACHABLE | Called by `Logger.send` and buffer processing (`Logger.java:65-83,99-110,139-147`). |
| 16 | `Logger.lazyGetOutputBuf()` | REACHABLE | Called by swaps, filters, reads, and writes (`Logger.java:86-91,139-165,244-256,281-312,337-338,385-418,445-453`). |
| 17 | `Logger.observeDataSetChanged()` | REACHABLE | `TorrentEngine` subscribes to the session logger's observable (`TorrentEngine.java:245-260`); method returns the subject (`Logger.java:259-262`). |
| 18 | `Logger.pause()` | REACHABLE | Called by `LogViewModel` and `SaveLogWorker` (`LogViewModel.java:140-149`; `SaveLogWorker.java:84-96`). |
| 19 | `Logger.periodicSwapBuffers()` | OPEN | Registered as a `Thread` method reference (`Logger.java:65-83`); `Thread` callback dispatch source was not printed. |
| 20 | `Logger.removeFilter(String[])` | REACHABLE | Called by `SessionLogger.applyFilterParams` (`SessionLogger.java:169-201`), itself reached from session settings application (`TorrentSessionImpl.java:1416-1427`). |
| 21 | `Logger.resume()` | REACHABLE | Called by `LogViewModel` and `SaveLogWorker` (`LogViewModel.java:151-159`; `SaveLogWorker.java:104-107`). |
| 22 | `Logger.send(LogEntry)` | OPEN | Called by `SessionLogger.send(Alert)` (`SessionLogger.java:117-167`), which is called from `TorrentSessionImpl.InnerListener.alert` (`TorrentSessionImpl.java:1061-1104`); libtorrent alert dispatch is external to uploaded source. |
| 23 | `Logger.setMaxStoredLogs(int)` | REACHABLE | Called from `TorrentSessionImpl.applyMaxStoredLogs` (`TorrentSessionImpl.java:1408-1414`). |
| 24 | `Logger.startRecording()` | REACHABLE | `LogViewModel.startLogRecording` calls it (`LogViewModel.java:172-177`). |
| 25 | `Logger.stopRecording()` | REACHABLE | Called from `LogViewModel` and session logger shutdown (`LogViewModel.java:179-184`; `TorrentSessionImpl.java:1021-1024`). |
| 26 | `Logger.stopRecording(OutputStream,boolean)` | REACHABLE | Called by `SaveLogWorker` with timestamp flag true (`SaveLogWorker.java:84-96`); no-arg overload also delegates to it (`Logger.java:362-374`). |
| 27 | `Logger.submitDataSetChanged(DataSetChange)` | REACHABLE | Called from `swapBuffers`, `forceFilterBuf`, and `doClean` (`Logger.java:139-168,244-257,475-499`). |
| 28 | `Logger.swapBuffers()` | REACHABLE | Called from log reads, writes, recording, and buffer maintenance (`Logger.java:139-168,271-317,329-338,372-418,445-453`). |
| 29 | `Logger.write(OutputStream,boolean)` | REACHABLE | `SaveLogWorker` calls it with timestamp flag true (`SaveLogWorker.java:84-96`). |
| 30 | `Logger.write(FixedRingBuffer,OutputStream,int,int,boolean)` | REACHABLE | Called from public `write` and `stopRecording` overloads (`Logger.java:372-388,405-420`). |
| 31 | `Logger$DataSetChange.<init>(Reason)` | REACHABLE | Constructed by `Logger.doClean()` (`Logger.java:487-499`); also delegates from the list constructor (`Logger.java:527-535`). |
| 32 | `Logger$DataSetChange.<init>(Reason,List)` | REACHABLE | Constructed by `Logger.swapBuffers()` (`Logger.java:139-168`). |
| 33 | `Logger$DataSetChange$Reason.<clinit>` | REACHABLE | Enum constants are referenced at `Logger.java:165,256,498` and initialized as part of those source routes. |
| 34 | `Logger$NewFilter.<init>(String,LogFilter)` | REACHABLE | `SessionLogger.applyFilterParams` obtains filter objects and constructs the array (`SessionLogger.java:169-201`); its filter factory creates `NewFilter` values (`SessionLogger.java:30-90`). |
| 35 | `AddTorrentParams.<clinit>` | REACHABLE | App code constructs `AddTorrentParams` in ViewModel, engine, and feed worker (`AddTorrentViewModel.java:510`; `TorrentEngine.java:1187`; `FeedDownloaderWorker.java:178`), initializing its static Creator field. |
| 36 | `AddTorrentParams.<init>(Parcel)` | UNREACHABLE `no_trigger_in_app` | Only reached from its `CREATOR.createFromParcel` (`AddTorrentParams.java:109-113`); no app parcel write/read or `AddTorrentParams` parcel transport was found. |
| 37 | `AddTorrentParams.<init>(String,boolean,String,String,Priority[],Uri,boolean,boolean,List,boolean)` | REACHABLE | Direct app constructors are present in `AddTorrentViewModel`, `TorrentEngine`, and `FeedDownloaderWorker` (call sites above). |
| 38 | `AddTorrentParams.describeContents()` | UNREACHABLE `no_trigger_in_app` | Body returns 0 (`AddTorrentParams.java:90-93`); no app code parcels this class, so no Parcel framework call route was found. |
| 39 | `AddTorrentParams.hashCode()` | UNREACHABLE `no_trigger_in_app` | Body printed (`AddTorrentParams.java:122-125`); no `AddTorrentParams` hash collection or hashCode caller found in app source. |
| 40 | `AddTorrentParams.toString()` | UNREACHABLE `no_trigger_in_app` | Body printed (`AddTorrentParams.java:127-142`); no explicit caller or string formatting of this type found in app source. |

Table totals: 40 rows = 33 REACHABLE, 4 UNREACHABLE (`no_trigger_in_app`), and 3 OPEN. The OPEN rows are the Rx callback lambda, the periodic Thread callback, and `Logger.send` through libtorrent alert dispatch.
