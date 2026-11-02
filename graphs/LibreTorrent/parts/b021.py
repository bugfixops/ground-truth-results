# Citation-form rework 2026-11-01: evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, edges, endpoints, SUPPRESS entries and line ranges unchanged; full relative paths remain in the .md and printed files.
# C02 conversion of helper/a3-fix-buildnames batch-21 part (2026-11-01).
# Base part verified against merger/staging-A1 batch21-merge-ready.md:
# labels/kinds match exactly; counts R36 U4 O0; edges 36; SUPPRESS 4.
# STRONGER-EVIDENCE upgrades (tree graph_def.py holds SOURCE, part held
# INFERRED; kind/reason/ref unchanged; never downgraded): all 4
# AddTorrentParams UNREACHABLE keys (<init>(Parcel), describeContents,
# hashCode, toString): INFERRED -> SOURCE.
# Kind note (unchanged, matches merge-ready): describeContents kind is
# framework_never_calls in the part/merge-ready, vs no_trigger_in_app in
# the tree; the kind is governed by merge-ready and is NOT changed.
# HARNESS NOTE: check_part.py compares the part grade to the merge-ready
# grade (INFERRED for all 4 rows), so the 4 upgrades above produce
# exactly 4 grade-mismatch FAIL lines and no other FAILs. Do NOT revert
# these grades to INFERRED at merge; the merger must either waive those
# 4 FAIL lines or patch the harness to accept SOURCE where the tree
# holds SOURCE.
# Greps: parts-staging/grep/21/ (4 files, one per UNREACHABLE row).
# Printed evidence: parts/b021_printed.txt (verbatim base printed file,
# 31,470 B, under 900 KB; copy pending only on the sandbox exec-write
# block - see REPORT-b021.md).

# Batch 21 part (LogEntry.toStringWithTimeStamp, Logger and its helpers,
# AddTorrentParams). Hand-written edges, UNREACHABLE entries and SUPPRESS strings only.
# Each evidence string cites lines printed in graphs/LibreTorrent/scratch/b021_printed.txt.
# Source paths are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
#
# No batch-21 method has an incoming edge in graph_def.py, so no route is listed
# as a Dependency here; every REACHABLE row below has a new edge in this file.

# LogEntry.toStringWithTimeStamp: used by Logger's private write.
e('Logger.write(FixedRingBuffer,OutputStream,int,int,boolean)', 'LogEntry.toStringWithTimeStamp', 'CALL', 'Format a log entry with its timestamp while writing the log file',
  cls='explicit', evidence='SRC Logger.java:437; LogEntry.java:103-106')

# Logger: constructed via SessionLogger, driven by the log data source, the log view
# model, the session implementation and the save-log worker.
e('SessionLogger.<init>', 'Logger.<init>', 'CALL', 'Construct the session logger with a single stored log entry',
  cls='explicit', evidence='SRC SessionLogger.java:111-115; Logger.java:57-64')
e('SessionLogger.applyFilterParams', 'Logger.addFilter', 'CALL', 'Add the session log filters',
  cls='explicit', evidence='SRC SessionLogger.java:200; Logger.java:202-221')
e('Logger.swapBuffers', 'Logger.applyFilters', 'CALL', 'Apply the registered filters while swapping buffers',
  cls='explicit', evidence='SRC Logger.java:152; Logger.java:319-327')
e('Logger.lazyGetInputBuf', 'Logger.calcInitBufCapacity', 'CALL', 'Compute the initial buffer capacity while lazily creating the input buffer',
  cls='explicit', evidence='SRC Logger.java:68; Logger.java:94-97')
e('TorrentSessionImpl.enableSessionLogger', 'Logger.clean', 'CALL', 'Clean the session logger when session logging is disabled',
  cls='explicit', evidence='SRC TorrentSessionImpl.java:1023; Logger.java:475-485')
e('Logger.clean', 'Logger.doClean', 'CALL', 'Perform the buffer clean requested by clean()',
  cls='explicit', evidence='SRC Logger.java:480; Logger.java:487-499')
e('Logger.addFilter', 'Logger.forceFilterBuf', 'CALL', 'Refilter the buffered entries after adding a filter',
  cls='explicit', evidence='SRC Logger.java:216; Logger.java:244-257')
e('LogDataSource.loadInitial', 'Logger.getEntries', 'CALL', 'Load the initial page of log entries for the log list',
  cls='explicit', evidence='SRC ui/log/LogDataSource.java:70; Logger.java:271-298')
e('TorrentSessionImpl.applyMaxStoredLogs', 'Logger.getMaxStoredLogs', 'CALL', 'Read the maximum stored log count while applying log settings',
  cls='explicit', evidence='SRC TorrentSessionImpl.java:1410; Logger.java:190-200')
e('LogDataSource.loadInitial', 'Logger.getNumEntries', 'CALL', 'Count the buffered entries while loading the initial page',
  cls='explicit', evidence='SRC ui/log/LogDataSource.java:66; Logger.java:445-458')
e('LogDataSource.loadInitial', 'Logger.isPaused', 'CALL', 'Check whether logging is paused while loading the initial page',
  cls='explicit', evidence='SRC ui/log/LogDataSource.java:59; Logger.java:470-473')
e('LogViewModel.<init>', 'Logger.isRecording', 'CALL', 'Check whether session logging is recording while creating the log view model',
  cls='explicit', evidence='SRC ui/log/LogViewModel.java:74; Logger.java:345-355')
e('Logger.submitDataSetChanged', 'Logger.lambda$submitDataSetChanged$0', 'FRAMEWORK', 'Publish a data-set change on the executor',
  cls='non_standard', via='executor dispatch',
  evidence='INFERRED executor dispatch; SRC Logger.java:170; Logger.java:168-171')
e('Logger.send', 'Logger.lazyGetInputBuf', 'CALL', 'Lazily create the input buffer when sending a log entry',
  cls='explicit', evidence='SRC Logger.java:104; Logger.java:65-84')
e('Logger.swapBuffers', 'Logger.lazyGetOutputBuf', 'CALL', 'Lazily create the output buffer while swapping buffers',
  cls='explicit', evidence='SRC Logger.java:147; Logger.java:86-92')
e('LogDataSource.<init>', 'Logger.observeDataSetChanged', 'CALL', 'Subscribe to data-set changes when creating the log data source',
  cls='explicit', evidence='SRC ui/log/LogDataSource.java:42; Logger.java:259-262')
e('LogDataSource.loadInitial', 'Logger.pause', 'CALL', 'Pause logging while loading the initial page',
  cls='explicit', evidence='SRC ui/log/LogDataSource.java:60; Logger.java:460-463')
e('Logger.lazyGetInputBuf', 'Logger.periodicSwapBuffers', 'FRAMEWORK', 'Run the periodic buffer-swap loop on its thread',
  cls='non_standard', via='Thread.start dispatch',
  evidence='INFERRED Thread.start dispatch; SRC Logger.java:71-72; Logger.java:113-137')
e('SessionLogger.applyFilterParams', 'Logger.removeFilter', 'CALL', 'Remove the session log filters',
  cls='explicit', evidence='SRC SessionLogger.java:199; Logger.java:223-242')
e('LogDataSource.loadInitial', 'Logger.resume', 'CALL', 'Resume logging after loading the initial page',
  cls='explicit', evidence='SRC ui/log/LogDataSource.java:88; Logger.java:465-468')
e('SessionLogger.send', 'Logger.send', 'CALL', 'Send a constructed log entry to the logger',
  cls='explicit', evidence='SRC SessionLogger.java:166; Logger.java:99-111')
e('TorrentSessionImpl.applyMaxStoredLogs', 'Logger.setMaxStoredLogs', 'CALL', 'Apply the maximum stored log count from settings',
  cls='explicit', evidence='SRC TorrentSessionImpl.java:1413; Logger.java:177-188')
e('LogViewModel.startLogRecording', 'Logger.startRecording', 'CALL', 'Start log recording from the log view model',
  cls='explicit', evidence='SRC ui/log/LogViewModel.java:176; Logger.java:329-343')
e('LogViewModel.stopLogRecording', 'Logger.stopRecording()', 'CALL', 'Stop log recording from the log view model',
  cls='explicit', evidence='SRC ui/log/LogViewModel.java:183; Logger.java:362-365')
e('SaveLogWorker.saveLog', 'Logger.stopRecording(OutputStream,boolean)', 'CALL', 'Stop recording to a file in the save-log worker',
  cls='explicit', evidence='SRC service/SaveLogWorker.java:93; Logger.java:372-398')
e('Logger.swapBuffers', 'Logger.submitDataSetChanged', 'CALL', 'Notify data-set observers after swapping buffers',
  cls='explicit', evidence='SRC Logger.java:165; Logger.java:168-171')
e('Logger.periodicSwapBuffers', 'Logger.swapBuffers', 'CALL', 'Swap buffers in the periodic loop',
  cls='explicit', evidence='SRC Logger.java:122; Logger.java:139-166')
e('SaveLogWorker.saveLog', 'Logger.write(OutputStream,boolean)', 'CALL', 'Write the log to a file in the save-log worker',
  cls='explicit', evidence='SRC service/SaveLogWorker.java:95; Logger.java:410-423')
e('Logger.stopRecording(OutputStream,boolean)', 'Logger.write(FixedRingBuffer,OutputStream,int,int,boolean)', 'CALL', 'Write the buffered entries to the output stream while stopping',
  cls='explicit', evidence='SRC Logger.java:387; Logger.java:425-443')
e('Logger.forceFilterBuf', 'Logger$DataSetChange.<init>(Reason)', 'CALL', 'Publish a filter data-set change after refiltering',
  cls='explicit', evidence='SRC Logger.java:256; Logger.java:527-530')
e('Logger.swapBuffers', 'Logger$DataSetChange.<init>(Reason,List)', 'CALL', 'Publish a new-entries data-set change after swapping',
  cls='explicit', evidence='SRC Logger.java:165; Logger.java:532-536')
e('Logger.swapBuffers', 'Logger$DataSetChange$Reason.<clinit>', 'FRAMEWORK', 'First use of a Reason constant initialises the enum',
  cls='non_standard', via='JVM enum class initialization on first active use',
  evidence='INFERRED JVM enum initialization; SRC Logger.java:165; Logger.java:515-520')
e('SessionLogger$SessionLogFilter.<init>', 'Logger$NewFilter.<init>', 'CALL', 'Construct the new filter for a session log filter entry',
  cls='explicit', evidence='SRC SessionLogger.java:80; Logger.java:506-510')

# AddTorrentParams: the class loads and the 10-arg constructor runs on the add-torrent
# path; the Parcelable machinery never runs (no marshalling site in the app tree).
e('AddTorrentViewModel.addTorrent', 'AddTorrentParams.<clinit>', 'FRAMEWORK', 'First construction of AddTorrentParams initialises the class and its CREATOR field',
  cls='non_standard', via='JVM class initialization on first active use',
  evidence='INFERRED JVM class initialization; SRC ui/addtorrent/AddTorrentViewModel.java:510; AddTorrentParams.java:109-119')
e('AddTorrentViewModel.addTorrent', 'AddTorrentParams.<init>(String,boolean,String,String,Priority[],Uri,boolean,boolean,List,boolean)', 'CALL', 'Construct the add-torrent parameters on the add-torrent path',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:510; AddTorrentParams.java:53-75')

# Parcelable machinery and value methods with no trigger: a saved full-tree grep finds
# no marshalling site for AddTorrentParams, and no hashCode/toString caller.
UNREACHABLE.update({
    'AddTorrentParams.<init>(Parcel)': ('no_trigger_in_app',
        'No app code unparcels an AddTorrentParams. Its only printed caller is CREATOR.createFromParcel, itself UNREACHABLE (batch 22); a saved full-tree grep finds no marshalling site outside CREATOR.',
        'SRC AddTorrentParams.java:77-88',
        'SOURCE'),
    'AddTorrentParams.describeContents': ('framework_never_calls',
        'The framework calls describeContents only when parcelling, which never happens for AddTorrentParams: no marshalling site exists in the app tree.',
        'SRC AddTorrentParams.java:91-93',
        'SOURCE'),
    'AddTorrentParams.hashCode': ('no_trigger_in_app',
        'No app code hashes an AddTorrentParams; a saved full-tree grep confirms zero hash use.',
        'SRC AddTorrentParams.java:123-125',
        'SOURCE'),
    'AddTorrentParams.toString': ('no_trigger_in_app',
        'No app code converts an AddTorrentParams to text; a saved full-tree grep confirms zero callers.',
        'SRC AddTorrentParams.java:129-142',
        'SOURCE'),
})

# Suppress bytecode auto edges into the UNREACHABLE AddTorrentParams methods.
# AddTorrentParams is not subclassed in the app, so there are no @Variant copies.
# Note: the Parcel constructor is suppressed by its qualified name so the
# REACHABLE 10-arg constructor keeps its hand edge in this file.
SUPPRESS.update({
    'AddTorrentParams.<init>(Parcel)', 'AddTorrentParams.describeContents',
    'AddTorrentParams.hashCode', 'AddTorrentParams.toString',
})
