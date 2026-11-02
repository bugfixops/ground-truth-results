# Citation-form rework 2026-11-01: evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, edges, endpoints, SUPPRESS entries and line ranges unchanged; full relative paths remain in the .md and printed files.
# C02 conversion of helper/a3-fix-buildnames batch-20 part (2026-11-01).
# Base part verified against clone batch20-merge-ready.md: labels/kinds
# match exactly; counts R39 U1 O0; edges 39; SUPPRESS 1.
# STRONGER-EVIDENCE upgrade (tree graph_def.py holds SOURCE, part held
# INFERRED; kind/reason/ref unchanged; never downgraded):
#   LogEntry.hashCode (1 key: INFERRED -> SOURCE).
# HARNESS NOTE: check_part.py compares the part grade to the merge-ready
# grade (INFERRED), so the upgrade above produces exactly 1
# grade-mismatch FAIL line and no other FAILs. Do NOT revert this grade
# to INFERRED at merge; the merger must either waive that FAIL line or
# patch the harness to accept SOURCE where the tree holds SOURCE.
# Greps: parts-staging/grep/20/ (1 file, one per UNREACHABLE row).
# Printed evidence: parts/b020_printed.txt (verbatim base printed file,
# 32,515 B, under 900 KB; copy pending only on the sandbox exec-write
# block - see REPORT-b020.md).

# Batch 20 part (exception constructors, TorrentFilterCollection factories and lambdas,
# LogEntry). Hand-written edges, UNREACHABLE entries and SUPPRESS strings only.
# Each evidence string cites lines printed in graphs/LibreTorrent/scratch/b020_printed.txt.
# Source paths are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
#
# No batch-20 method has an incoming edge in graph_def.py, so no route is listed
# as a Dependency here; every REACHABLE row below has a new edge in this file.

# Exception constructors: thrown from the printed sites below.
e('Utils.fetchHttpUrl', 'FetchLinkException.<init>(String)', 'CALL', 'Throw for a missing network connection or a failed fetch',
  cls='explicit', evidence='SRC Utils.java:467,493,509,522; FetchLinkException.java:30')
e('TorrentEngine.addTorrentSync(Uri,TorrentMetaInfo,Uri)', 'FreeSpaceException.<init>()', 'CALL', 'Throw when the free-space check fails while adding a torrent',
  cls='explicit', evidence='SRC TorrentEngine.java:1201; FreeSpaceException.java:28')
e('TorrentDownloadImpl.handleMetadata', 'FreeSpaceException.<init>(String)', 'CALL', 'Throw for insufficient free space when metadata arrives',
  cls='explicit', evidence='SRC TorrentDownloadImpl.java:417; FreeSpaceException.java:30')
e('IPFilterImpl.addRange', 'IPFilterException.<init>(String)', 'CALL', 'Throw when an IP filter range is malformed',
  cls='explicit', evidence='SRC IPFilterImpl.java:44,54,58; IPFilterException.java:26')
e('AddTorrentViewModel.addTorrent', 'NoFilesSelectedException.<init>()', 'CALL', 'Throw when the add-torrent check finds no selected files',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:493; NoFilesSelectedException.java:24')
e('NormalizeUrl.normalize(String,Options)', 'NormalizeUrlException.<init>(String,Exception)', 'CALL', 'Throw when URL normalisation fails',
  cls='explicit', evidence='SRC NormalizeUrl.java:185; NormalizeUrlException.java:21')
e('TorrentSessionImpl.addTorrent', 'TorrentAlreadyExistsException.<init>()', 'CALL', 'Throw when the repository already contains the torrent id',
  cls='explicit', evidence='SRC TorrentSessionImpl.java:282; TorrentAlreadyExistsException.java:24')
e('FsModuleResolverImpl.resolveFsByUri', 'UnknownUriException.<init>', 'CALL', 'Throw when no file system resolves the URI',
  cls='explicit', evidence='SRC FsModuleResolverImpl.java:48; UnknownUriException.java:23')

# TorrentFilterCollection factories: called from the drawer filter builders and the
# main screen; MainViewModel field initialisers run in its constructor.
e('MainViewModel.<init>', 'TorrentFilterCollection.all', 'CALL', 'Initialise the default status, date-added and tag filters to all',
  cls='explicit', evidence='SRC ui/main/MainViewModel.java:53-55; TorrentFilterCollection.java:27-29')
e('Utils.getDrawerGroupDateAddedFilter', 'TorrentFilterCollection.dateAddedMonth', 'CALL', 'Build the date-added-month filter for the drawer selection',
  cls='explicit', evidence='SRC Utils.java:866; TorrentFilterCollection.java:77-85')
e('Utils.getDrawerGroupDateAddedFilter', 'TorrentFilterCollection.dateAddedToday', 'CALL', 'Build the date-added-today filter for the drawer selection',
  cls='explicit', evidence='SRC Utils.java:860; TorrentFilterCollection.java:47-55')
e('Utils.getDrawerGroupDateAddedFilter', 'TorrentFilterCollection.dateAddedWeek', 'CALL', 'Build the date-added-week filter for the drawer selection',
  cls='explicit', evidence='SRC Utils.java:864; TorrentFilterCollection.java:67-75')
e('Utils.getDrawerGroupDateAddedFilter', 'TorrentFilterCollection.dateAddedYear', 'CALL', 'Build the date-added-year filter for the drawer selection',
  cls='explicit', evidence='SRC Utils.java:868; TorrentFilterCollection.java:87-95')
e('Utils.getDrawerGroupDateAddedFilter', 'TorrentFilterCollection.dateAddedYesterday', 'CALL', 'Build the date-added-yesterday filter for the drawer selection',
  cls='explicit', evidence='SRC Utils.java:862; TorrentFilterCollection.java:57-65')
e('Utils.getDrawerGroupStatusFilter', 'TorrentFilterCollection.statusDownloaded', 'CALL', 'Build the downloaded-status filter for the drawer selection',
  cls='explicit', evidence='SRC Utils.java:845; TorrentFilterCollection.java:35-37')
e('Utils.getDrawerGroupStatusFilter', 'TorrentFilterCollection.statusDownloading', 'CALL', 'Build the downloading-status filter for the drawer selection',
  cls='explicit', evidence='SRC Utils.java:843; TorrentFilterCollection.java:31-33')
e('Utils.getDrawerGroupStatusFilter', 'TorrentFilterCollection.statusDownloadingMetadata', 'CALL', 'Build the downloading-metadata-status filter for the drawer selection',
  cls='explicit', evidence='SRC Utils.java:847; TorrentFilterCollection.java:39-41')
e('Utils.getDrawerGroupStatusFilter', 'TorrentFilterCollection.statusError', 'CALL', 'Build the error-status filter for the drawer selection',
  cls='explicit', evidence='SRC Utils.java:849; TorrentFilterCollection.java:43-45')
e('MainActivity$3.onTagSelected', 'TorrentFilterCollection.noTags', 'CALL', 'Build the no-tags filter when a tag is selected',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:306; TorrentFilterCollection.java:101-103')
e('MainActivity$3.onTagSelected', 'TorrentFilterCollection.tag', 'CALL', 'Build the filter for the selected tag',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:300; TorrentFilterCollection.java:97-99')

# Filter lambdas: created by their factory method and invoked through TorrentFilter.test.
e('TorrentFilterCollection.all', 'TorrentFilterCollection.lambda$all$0', 'CALL', 'Test a torrent state against the always-true filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:28')
e('TorrentFilterCollection.dateAddedMonth', 'TorrentFilterCollection.lambda$dateAddedMonth$8', 'CALL', 'Test a torrent state against the date-added-month filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:78-84')
e('TorrentFilterCollection.dateAddedToday', 'TorrentFilterCollection.lambda$dateAddedToday$5', 'CALL', 'Test a torrent state against the date-added-today filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:48-54')
e('TorrentFilterCollection.dateAddedWeek', 'TorrentFilterCollection.lambda$dateAddedWeek$7', 'CALL', 'Test a torrent state against the date-added-week filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:69-74')
e('TorrentFilterCollection.dateAddedYear', 'TorrentFilterCollection.lambda$dateAddedYear$9', 'CALL', 'Test a torrent state against the date-added-year filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:88-94')
e('TorrentFilterCollection.dateAddedYesterday', 'TorrentFilterCollection.lambda$dateAddedYesterday$6', 'CALL', 'Test a torrent state against the date-added-yesterday filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:58-64')
e('TorrentFilterCollection.noTags', 'TorrentFilterCollection.lambda$noTags$11', 'CALL', 'Test a torrent state against the no-tags filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:102')
e('TorrentFilterCollection.statusDownloaded', 'TorrentFilterCollection.lambda$statusDownloaded$2', 'CALL', 'Test a torrent state against the downloaded filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:36')
e('TorrentFilterCollection.statusDownloading', 'TorrentFilterCollection.lambda$statusDownloading$1', 'CALL', 'Test a torrent state against the downloading filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:32')
e('TorrentFilterCollection.statusDownloadingMetadata', 'TorrentFilterCollection.lambda$statusDownloadingMetadata$3', 'CALL', 'Test a torrent state against the downloading-metadata filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:40')
e('TorrentFilterCollection.statusError', 'TorrentFilterCollection.lambda$statusError$4', 'CALL', 'Test a torrent state against the error filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:44')
e('TorrentFilterCollection.tag', 'TorrentFilterCollection.lambda$tag$10', 'CALL', 'Test a torrent state against the tag filter',
  cls='non_standard', via='TorrentFilter Predicate.test dispatch',
  evidence='INFERRED Predicate.test dispatch; SRC TorrentFilterCollection.java:98')

# LogEntry: constructed by SessionLogger.send and read by the log adapter and Logger.
e('SessionLogger.send', 'LogEntry.<init>', 'CALL', 'Construct a log entry for a session alert',
  cls='explicit', evidence='SRC SessionLogger.java:124,132,144,152,158; LogEntry.java:39-47')
e('LogAdapter$1.areContentsTheSame', 'LogEntry.equals', 'CALL', 'Compare log entries in the DiffUtil contents check',
  cls='explicit', evidence='SRC ui/log/LogAdapter.java:73; LogEntry.java:77-90')
e('LogAdapter$1.areItemsTheSame', 'LogEntry.getId', 'CALL', 'Compare log entry ids in the DiffUtil identity check',
  cls='explicit', evidence='SRC ui/log/LogAdapter.java:80; LogEntry.java:49-52')
e('LogAdapter$ViewHolder.bind', 'LogEntry.getMsg', 'CALL', 'Bind the log message text in the view holder',
  cls='explicit', evidence='SRC ui/log/LogAdapter.java:108; LogEntry.java:60-64')
e('LogAdapter$ViewHolder.bind', 'LogEntry.getTag', 'CALL', 'Bind the log tag text in the view holder',
  cls='explicit', evidence='SRC ui/log/LogAdapter.java:107; LogEntry.java:55-58')
e('LogAdapter$ViewHolder.bind', 'LogEntry.getTimeStampAsString', 'CALL', 'Bind the formatted timestamp in the view holder',
  cls='explicit', evidence='SRC ui/log/LogAdapter.java:109; LogEntry.java:71-74')
e('Logger.write(FixedRingBuffer,OutputStream,int,int,boolean)', 'LogEntry.toString', 'CALL', 'Write a log entry as text when writing the log file',
  cls='explicit', evidence='SRC Logger.java:437; LogEntry.java:110-113')

# hashCode with no caller: the printed equals call does not by itself print a hashCode
# call, and a saved full-tree grep confirms zero hash use of LogEntry.
UNREACHABLE.update({
    'LogEntry.hashCode': ('no_trigger_in_app',
        'No app code hashes a LogEntry. The only hashCode calls in the fresh corpus are the String hashCode calls inside this definition itself; the printed equals call (LogAdapter) does not print a hashCode call, and a saved 252-file tree grep confirms zero hash use.',
        'SRC LogEntry.java:93-101',
        'SOURCE'),
})

# Suppress bytecode auto edges into LogEntry.hashCode. LogEntry is not subclassed
# in the app, so there are no @Variant generated copies to add.
SUPPRESS.update({
    'LogEntry.hashCode',
})
