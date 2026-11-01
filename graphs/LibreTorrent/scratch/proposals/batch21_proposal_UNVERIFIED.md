# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# LibreTorrent batch 21 — proposal, UNVERIFIED, NOT merged

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
Membership: exactly 40 rows in handoff/LIBRETORRENT_BATCH_PLAN.tsv (SHA 0104806dd666c840049b3db52823d4b384fa1c92), all TODO_CANDIDATE_REACHABLE — candidates, not evidence.
Status: UNVERIFIED proposal. No build, sampler, full-repo grep, or C1 check was run for this batch, and no such count is claimed. No graph_def.py / out/ edit was made, nothing was pushed by the helper in this stage.
Rules: confirmed_by SOURCE only where lines were printed, otherwise INFERRED, never DYN / FW-MEMORY / UNVERIFIED. Tool coverage, old generated graphs, and build REACHABLE counts are never evidence. Connector search_code 0/incomplete is NOT evidence of absence and was not used.

## Counts (proposal, not verified)
- Judged: 40 / 40. REACHABLE proposed: 33. UNREACHABLE proposed: 0. OPEN: 7.
- OPEN: Logger.clean, Logger.doClean, Logger.getMaxStoredLogs, Logger.setMaxStoredLogs, AddTorrentParams.describeContents, AddTorrentParams.hashCode, AddTorrentParams.toString.
- Groups: LogEntry.toStringWithTimeStamp 1/1 REACHABLE; Logger 28/30 REACHABLE (clean/doClean OPEN, plus getMax/setMax OPEN — see below, total Logger rows 30? count in table: Logger rows are #2-30 = 29 rows, of which 25 REACHABLE / 4 OPEN; plus DataSetChange/NewFilter 4/4 REACHABLE; AddTorrentParams 3/6 REACHABLE, 3 OPEN. 1+25+4+3 = 33 REACHABLE, 4+3 = 7 OPEN. Yes.)

## Shared route
SessionLogger (core/model/session/SessionLogger.java) extends Logger and is constructed with super(1) (:111-115); TorrentSessionImpl creates it (:170 in batch 19) and calls sessionLogger.send(alert) (:1102-1103). Log UI: LogActivity -> LogViewModel (engine.getSessionLogger()) -> LogDataSource (Paging PositionalDataSource; framework dispatch for loadInitial/loadRange INFERRED) -> Logger methods. Save path: LogActivity save_log_menu -> LogViewModel.saveLog -> WorkManager SaveLogWorker (standard registration, WorkManager dispatch INFERRED) -> logger.stopRecording/write.

## Table

| # | Method | Label | confirmed_by | Printed citations |
|---|---|---|---|---|
| 1 | LogEntry.toStringWithTimeStamp() | REACHABLE | SOURCE | Logger.java:437 write(...) `entry.toStringWithTimeStamp() : entry.toString()`; definition LogEntry.java calls getTimeStampAsString() + toString(). |
| 2 | Logger.<init>(int) | REACHABLE | SOURCE | SessionLogger.java:111-115 `SessionLogger() { super(1); }`; definition Logger.java:57-64. |
| 3 | Logger.addFilter(NewFilter...) | REACHABLE | SOURCE | SessionLogger.java:199 `addFilter(addFilters)` in applyFilterParams; definition Logger.java:202-221. |
| 4 | Logger.applyFilters(LogEntry) | REACHABLE | SOURCE (internal) | Logger.java:152 swapBuffers and :252 forceFilterBuf call applyFilters; definition :319-327. |
| 5 | Logger.calcInitBufCapacity(int) | REACHABLE | SOURCE (internal) | Logger.java:68 lazyGetInputBuf and :89 lazyGetOutputBuf; definition :94-97. |
| 6 | Logger.clean() | OPEN | — | No clean() caller printed in LogViewModel/LogActivity/Logger files read. doClean is only called by clean() and setMaxStoredLogs() (both OPEN), so clean's reachability is not established by internal calls. Pending full-repo grep; not UNREACHABLE. |
| 7 | Logger.doClean() | OPEN | — | Logger.java:182 (called by setMaxStoredLogs) and :480 (called by clean); both callers are OPEN rows, so doClean inherits OPEN. Pending full-repo grep. |
| 8 | Logger.forceFilterBuf() | REACHABLE | SOURCE (internal) | Logger.java:217 (addFilter) and :237 (removeFilter) call forceFilterBuf; definition :244-258. Both callers are REACHABLE. |
| 9 | Logger.getEntries(int,int) | REACHABLE | SOURCE | LogDataSource.java loadInitial and loadRange call logger.getEntries(...); definition Logger.java:271-300. |
| 10 | Logger.getMaxStoredLogs() | OPEN | — | No caller printed; the log-settings preference pref.maxLogSize() (LogSettingsFragment, TorrentEngine:1644) is a different method and does not call Logger.getMaxStoredLogs(). Pending full-repo grep. |
| 11 | Logger.getNumEntries() | REACHABLE | SOURCE | LogDataSource.java loadInitial/loadRange call logger.getNumEntries(); LogViewModel.java:164; definition Logger.java:445-458. |
| 12 | Logger.isPaused() | REACHABLE | SOURCE | LogDataSource.java loadInitial/loadRange check logger.isPaused(); LogViewModel.java:73; definition :470-473. |
| 13 | Logger.isRecording() | REACHABLE | SOURCE | LogViewModel.java:74 and :188 call sessionLogger.isRecording(); definition :345-354. |
| 14 | Logger.lambda$submitDataSetChanged$0 | REACHABLE | SOURCE body / INFERRED Rx dispatch | Logger.java:168-170 submitDataSetChanged: `sender.submit(() -> dataSetChangedPublish.onNext(change))`; executor dispatch INFERRED. |
| 15 | Logger.lazyGetInputBuf() | REACHABLE | SOURCE (internal) | Logger.java:102 send, :144 swapBuffers, :246 forceFilterBuf; definition :65-83. Also creates FixedRingBuffer (batch 19 route) and starts pendingThread. |
| 16 | Logger.lazyGetOutputBuf() | REACHABLE | SOURCE (internal) | Logger.java:147, :281, :306, :337, :385, :416, :450; definition :86-92. |
| 17 | Logger.observeDataSetChanged() | REACHABLE | SOURCE | LogDataSource.java ctor `logger.observeDataSetChanged().subscribe(...)`; definition Logger.java:259-262. |
| 18 | Logger.pause() | REACHABLE | SOURCE | LogDataSource.java loadInitial/loadRange call logger.pause(); LogViewModel.java:142 pauseLog; definition :460-463. |
| 19 | Logger.periodicSwapBuffers() | REACHABLE | SOURCE body / INFERRED thread dispatch | Logger.java:71 lazyGetInputBuf `new Thread(this::periodicSwapBuffers)` + start(); definition :113-... loop. Thread.start()->run() dispatch INFERRED, same caveat as batch 16 ServerRunnable. |
| 20 | Logger.removeFilter(String...) | REACHABLE | SOURCE | SessionLogger.java:198 `removeFilter(removeFilters)` in applyFilterParams; definition Logger.java:223-242. |
| 21 | Logger.resume() | REACHABLE | SOURCE | LogDataSource.java finally blocks call logger.resume(); LogViewModel.java:153; definition :465-468. |
| 22 | Logger.send(LogEntry) | REACHABLE | SOURCE | SessionLogger.java:166 `send(entry)` in send(Alert); definition Logger.java:99-110 (lazyGetInputBuf().add(entry)). |
| 23 | Logger.setMaxStoredLogs(int) | OPEN | — | No caller printed; see getMaxStoredLogs note — pref.maxLogSize() is not this method. Pending full-repo grep. |
| 24 | Logger.startRecording() | REACHABLE | SOURCE | LogViewModel.java:176 sessionLogger.startRecording(); definition :329-343. |
| 25 | Logger.stopRecording() | REACHABLE | SOURCE | LogViewModel.java:183 sessionLogger.stopRecording(); definition :362-364 delegates to stopRecording(null, false). |
| 26 | Logger.stopRecording(OutputStream,boolean) | REACHABLE | SOURCE | SaveLogWorker.java:93 `logger.stopRecording(fout, true)`; definition :372-399. WorkManager dispatch for SaveLogWorker INFERRED, standard registration as in batch 14. |
| 27 | Logger.submitDataSetChanged(DataSetChange) | REACHABLE | SOURCE (internal) | Logger.java:165 swapBuffers, :257 forceFilterBuf, :496 doClean; definition :168-170. Callers swapBuffers/forceFilterBuf are REACHABLE, so submit is REACHABLE even though doClean is OPEN. |
| 28 | Logger.swapBuffers() | REACHABLE | SOURCE (internal) | Logger.java:282 getEntries, :307 getEntry, :335 startRecording, :380 stopRecording, :413 write; definition :139-165. |
| 29 | Logger.write(OutputStream,boolean) | REACHABLE | SOURCE | SaveLogWorker.java:95 `logger.write(fout, true)`; definition :410-423 delegates to private write(...). |
| 30 | Logger.write(FixedRingBuffer,OutputStream,int,int,boolean) | REACHABLE | SOURCE (internal) | Logger.java:390 stopRecording(...,boolean) and :419 write(...,boolean); definition :425-443, calls entry.toStringWithTimeStamp()/toString() :437 and FixedRingBuffer.get :436. This also confirms FixedRingBuffer.get usage (batch 19). |
| 31 | Logger$DataSetChange.<init>(Reason) | REACHABLE | SOURCE (internal) | Logger.java:496 doClean and DataSetChange ctor delegation :529-531 `this(reason, null)`; also swapBuffers/forceFilterBuf submit with a Reason+entries or Reason-only change. Definition :529-531. |
| 32 | Logger$DataSetChange.<init>(Reason,List) | REACHABLE | SOURCE (internal) | Logger.java:165 swapBuffers `new DataSetChange(Reason.NEW_ENTRIES, newEntries)`; definition :532-536. |
| 33 | Logger$DataSetChange$Reason.<clinit> | REACHABLE | INFERRED JVM | Enum constants NEW_ENTRIES, CLEAN, FILTER (Logger.java:515-520) used in swapBuffers/forceFilterBuf/doClean; JVM enum initialisation INFERRED. |
| 34 | Logger$NewFilter.<init>(String,LogFilter) | REACHABLE | SOURCE | SessionLogger.java:82 SessionLogFilter ctor `this.filter = new NewFilter(name(), filter)`; definition Logger.java:506-510. Enum initialisation INFERRED. |
| 35 | AddTorrentParams.<clinit> | REACHABLE | INFERRED JVM | Static CREATOR field (AddTorrentParams.java:125-133) initialised on class load; class is loaded via AddTorrentViewModel:510 ctor call. JVM initialisation INFERRED. |
| 36 | AddTorrentParams.<init>(Parcel) | REACHABLE | SOURCE (internal) / INFERRED framework | AddTorrentParams.java CREATOR.createFromParcel (batch 22 row) calls `new AddTorrentParams(source)`; definition :80-92. Parcelable framework dispatch to createFromParcel INFERRED. |
| 37 | AddTorrentParams.<init>(String,boolean,String,String,Priority[],Uri,boolean,boolean,List,boolean) | REACHABLE | SOURCE | AddTorrentViewModel.java:510 `new AddTorrentParams(...)` in the add-torrent path; definition :52-76. |
| 38 | AddTorrentParams.describeContents() | OPEN | — | No parceling site printed for AddTorrentParams in files read; framework calls describeContents only when the object is actually parcelled, which was not printed. Pending full-repo grep / Intent-extra evidence. Not UNREACHABLE. |
| 39 | AddTorrentParams.hashCode() | OPEN | — | No hashCode caller printed (definition :136-139 returns sha1hash.hashCode()). Pending full-repo grep; not UNREACHABLE. |
| 40 | AddTorrentParams.toString() | OPEN | — | No toString/log/concat caller printed in files read. Pending full-repo grep; not UNREACHABLE. |

## Cross-batch notes (not verdict changes in this stage)
- FixedRingBuffer: batch 19 OPEN methods add(Iterable), contains, indexOf, remove, removeAt, isFull, getAllocatedSize remain OPEN — Logger.java in this stage uses add(Object), get, size, clear, iterator (for-loop), but does not use those 7 methods. FixedRingBuffer.get is confirmed again at Logger.java:436 (write) and :152/:285 (getEntries path).
- Batch 18 OPEN InputFilterRange: LogSettingsFragment.java (printed this stage) uses `new InputFilterRange.Builder().setMin(1).setMax(Integer.MAX_VALUE).build()` for the max-log-size preference. That is new printed evidence for Builder methods, but InputFilterRange.java itself was not re-printed in this stage, so no batch 18 verdict is changed here — follow-up should re-print InputFilterRange.java against this attach site.
- Logger.getEntry(int) (not in batch 21) and Logger.write(OutputStream) 1-arg and stopRecording(OutputStream) 1-arg are also not in batch 21; do not conflate them with the 2-arg rows judged above.
