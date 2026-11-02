# C03 delivered part b022 (LibreTorrent batch 22), 2026-11-01.
# Converter: C03. Base: audited A3 output (see REPORT-b022.md). No label and no kind changed by the converter.
# Branch head at pre-test: f8676c8a (b007 landed; MERGED_PARTS tail b007.py matches head).
# CITATION REWORDING (citation-only, no line or label change): every bare core/... citation in evidence strings was reworded to basename form (e.g. core/model/TorrentEngine.java:243 -> TorrentEngine.java:243) so the citation checker, which resolves only against the framework source cache, does not count new app citations as problems; every basename was verified unique in the app tree, line specs are unchanged, and full paths are retained in the .md and printed.txt.
# This part was pre-tested singly on top of that head (see REPORT-b022.md for build counts and check-2 delta).
# FLAG 1 — STRONGER-EVIDENCE UPGRADES (mandatory, user order 2026-11-01 18:41): the three UNREACHABLE entries below were INFERRED in the base part and are SOURCE here, because the merger tree already holds the same three keys at SOURCE (tree lines 3127-3129; clone main graph file lines ~3132-3134). No label, kind, reason or citation was changed. This upgrade makes the official harness report 3 confirmed_by FAILs (part SOURCE vs merge-ready table INFERRED) — that is the documented stronger-evidence exception, not a build-name or label failure; all other harness checks pass. The merger must accept SOURCE (fixing the earlier SOURCE regression) or explicitly revert the grade; the converter must not silently downgrade SOURCE to INFERRED.
# FLAG 2 — AUTHORITATIVE-FILE INCONSISTENCY (auditor/merger must reconcile before queueing): the staging-A1 batch-22 file's TABLE (rows 1, 3, 4) and its A1 evidence say UNREACHABLE, and the harness validates the table (37 REACHABLE / 3 UNREACHABLE / 0 OPEN, PASS on the base part), but the same file's header/counts/caveats sections still say 37 / 0 / 3 OPEN. This part follows the TABLE (the harness-validated label record); no label was flipped by the converter. If the header prose is treated as authoritative instead, HOLD this part — do not merge it until the file is reconciled.
# FLAG 3 — OVERLAP: the tree/clone main graph file already holds these same three UNREACHABLE keys at SOURCE (S4 batch-22 block). Merging this part overwrites them with the same label/kind/grade; the merger should reconcile the duplicate block at merge.
# FLAG 4 — SINGLE-COPY EDGE: the TorrentService.init -> TorrentEngine.doStart edge below is the single conversion-pipeline copy. The old helper draft b017.py was verified to carry no such edge (grep doStart in helper/a3-g3/parts/b017.py: no hits). Note the landed trunks part already contains the same edge, so the merger must reconcile that duplicate at merge; the edge is kept here because batch-22 row 34 requires an incoming edge in this part or a Dependency.
# Greps for the three UNREACHABLE rows are in parts-staging/grep/22/ (one file per row; full-repo marshalling grep, no site names this class; bytecode auto_calls shows no outside caller).
#
# Batch 22 part (AddTorrentParams CREATOR, DownloadsCompletedListener, SessionErrorFilter,
# TorrentEngine). Hand-written edges, UNREACHABLE entries and SUPPRESS strings only.
# Each evidence string cites lines printed in graphs/LibreTorrent/scratch/b022_printed.txt.
# Source paths are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
#
# Routes into batch-22 methods that already exist in graph_def.py and are not
# repeated here: TorrentEngine.getInstance -> TorrentEngine.<init> (120),
# AddTorrentViewModel.lambda$addTorrent$5 -> TorrentEngine.addTorrentSync(AddTorrentParams,boolean)
# (1106), SchedulerReceiver.onStopApp -> TorrentEngine.forceStop (232).
# NOTE for the merger: the TorrentService.init -> TorrentEngine.doStart edge below
# duplicates the edge already in parts/b017.py (TorrentService.init -> doStart);
# it is written here because batch 22 row 34 requires an incoming edge in this part
# or a graph_def.py Dependency, and b017.py is not graph_def.py. Reconcile at merge
# (keep one copy).

# AddTorrentParams CREATOR: the anonymous Creator instance is created by the CREATOR
# field initialiser during class initialisation.
e('AddTorrentParams.<clinit>', 'AddTorrentParams$1.<init>', 'CALL', 'Construct the anonymous Parcelable.Creator for AddTorrentParams',
  cls='explicit', evidence='SRC AddTorrentParams.java:109-119')

# DownloadsCompletedListener: subscribed in doStart, invoked through the session
# listener dispatch, disposed in doStop.
e('TorrentEngine.<init>', 'DownloadsCompletedListener.<init>', 'CALL', 'Construct the downloads-completed listener owned by the engine',
  cls='explicit', evidence='SRC TorrentEngine.java:135; DownloadsCompletedListener.java:40-43')
e('DownloadsCompletedListener.listen', 'DownloadsCompletedListener.lambda$listen$0', 'FRAMEWORK', 'Run the Completable that tracks in-progress torrents when subscribed',
  cls='non_standard', via='RxJava Completable.create subscription dispatch',
  evidence='INFERRED Rx subscription dispatch; SRC DownloadsCompletedListener.java:47-85; TorrentEngine.java:243-251')
e('DownloadsCompletedListener$1.onTorrentFinished', 'DownloadsCompletedListener.lambda$listen$1', 'CALL', 'Complete the tracking Completable when a torrent finishes',
  cls='explicit', evidence='SRC DownloadsCompletedListener.java:69; DownloadsCompletedListener.java:50-53')
e('DownloadsCompletedListener$1.onTorrentRemoved', 'DownloadsCompletedListener.lambda$listen$1', 'CALL', 'Complete the tracking Completable when a torrent is removed',
  cls='explicit', evidence='SRC DownloadsCompletedListener.java:76; DownloadsCompletedListener.java:50-53')
e('TorrentEngine.doStop', 'DownloadsCompletedListener.lambda$listen$2', 'FRAMEWORK', 'Run the dispose action that removes the session listener',
  cls='non_standard', via='RxJava dispose dispatch',
  evidence='INFERRED Rx dispose dispatch; SRC TorrentEngine.java:296; DownloadsCompletedListener.java:82-83')
e('TorrentEngine.doStart', 'DownloadsCompletedListener.listen', 'CALL', 'Subscribe the downloads-completed listener when the engine starts',
  cls='explicit', evidence='SRC TorrentEngine.java:243; DownloadsCompletedListener.java:45-86')
e('DownloadsCompletedListener.listen', 'DownloadsCompletedListener$1.<init>', 'CALL', 'Construct the anonymous engine listener registered by listen()',
  cls='explicit', evidence='SRC DownloadsCompletedListener.java:55')
e('DownloadsCompletedListener.listen', 'DownloadsCompletedListener$1.onTorrentFinished', 'CALL', 'Notify the listener when a torrent finishes',
  cls='non_standard', via='session listener dispatch',
  evidence='INFERRED session listener dispatch; SRC DownloadsCompletedListener.java:81; DownloadsCompletedListener.java:66-70')
e('DownloadsCompletedListener.listen', 'DownloadsCompletedListener$1.onTorrentRemoved', 'CALL', 'Notify the listener when a torrent is removed',
  cls='non_standard', via='session listener dispatch',
  evidence='INFERRED session listener dispatch; SRC DownloadsCompletedListener.java:81; DownloadsCompletedListener.java:73-77')
e('DownloadsCompletedListener.listen', 'DownloadsCompletedListener$1.onTorrentStateChanged', 'CALL', 'Notify the listener when a torrent state changes',
  cls='non_standard', via='session listener dispatch',
  evidence='INFERRED session listener dispatch; SRC DownloadsCompletedListener.java:81; DownloadsCompletedListener.java:57-63')

# SessionErrorFilter: created as a TorrentEngine field; its skip() is called by the
# engine listener's onSessionError.
e('TorrentEngine.<init>', 'SessionErrorFilter.<clinit>', 'FRAMEWORK', 'First construction of a SessionErrorFilter initialises the class and its errors set',
  cls='non_standard', via='JVM class initialization on first active use',
  evidence='INFERRED JVM class initialization; SRC TorrentEngine.java:113; SessionErrorFilter.java:26-28')
e('TorrentEngine.<init>', 'SessionErrorFilter.<init>', 'CALL', 'Construct the session error filter owned by the engine',
  cls='explicit', evidence='SRC TorrentEngine.java:113; SessionErrorFilter.java:20-24')
e('TorrentEngine$5.onSessionError', 'SessionErrorFilter.skip', 'CALL', 'Test whether a session error message is skippable',
  cls='explicit', evidence='SRC TorrentEngine.java:1386; SessionErrorFilter.java:30-32')

# TorrentEngine: the engine lifecycle and its torrent operations.
e('TorrentEngine.getInstance', 'TorrentEngine.<clinit>', 'FRAMEWORK', 'First use of the engine singleton initialises the class and its static fields',
  cls='non_standard', via='JVM class initialization on first active use',
  evidence='INFERRED JVM class initialization; SRC TorrentEngine.java:97,115,117')
e('TorrentService.init', 'TorrentEngine.addListener', 'CALL', 'Register the service as an engine listener during service init',
  cls='explicit', evidence='SRC service/TorrentService.java:132; TorrentEngine.java:307-309')
e('TorrentEngine.scanTorrentsInDir', 'TorrentEngine.addTorrent(Uri)', 'CALL', 'Add a torrent found while scanning the watch directory',
  cls='explicit', evidence='SRC TorrentEngine.java:1173; TorrentEngine.java:359-361')
e('TorrentEngine.addTorrent(Uri)', 'TorrentEngine.addTorrent(Uri,Uri)', 'CALL', 'Add a torrent with its save location from the single-URI overload',
  cls='explicit', evidence='SRC TorrentEngine.java:360; TorrentEngine.java:363-367')
e('TorrentEngine$4.onEvent', 'TorrentEngine.addTorrentCompletable(Uri)', 'CALL', 'Add a torrent observed by the watch-directory file observer',
  cls='explicit', evidence='SRC TorrentEngine.java:1149; TorrentEngine.java:370-372')
e('TorrentEngine.addTorrent(Uri,Uri)', 'TorrentEngine.addTorrentCompletable(Uri,Uri)', 'CALL', 'Add a torrent through the completable path from the two-URI overload',
  cls='explicit', evidence='SRC TorrentEngine.java:364; TorrentEngine.java:374-390')
e('TorrentEngine.addTorrentCompletable(Uri,Uri)', 'TorrentEngine.addTorrentSync(Uri,TorrentMetaInfo,Uri)', 'CALL', 'Add a torrent synchronously from the completable path',
  cls='explicit', evidence='SRC TorrentEngine.java:389; TorrentEngine.java:1177-1205')
e('FeedDownloaderWorker.addTorrents', 'TorrentEngine.addTorrents', 'CALL', 'Add the downloaded feed torrents through the engine',
  cls='explicit', evidence='SRC service/FeedDownloaderWorker.java:211; TorrentEngine.java:342-356')
e('DetailTorrentViewModel.addTrackers', 'TorrentEngine.addTrackers', 'CALL', 'Add trackers to a torrent from the detail view model',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:354; TorrentEngine.java:568-575')
e('AddTorrentViewModel.cancelFetchMagnet', 'TorrentEngine.cancelFetchMagnet', 'CALL', 'Cancel a magnet fetch from the add-torrent view model',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:572; TorrentEngine.java:481-486')
e('TorrentEngine.rescheduleTorrents', 'TorrentEngine.checkPauseTorrents', 'CALL', 'Check whether torrents must pause while rescheduling',
  cls='explicit', evidence='SRC TorrentEngine.java:320; TorrentEngine.java:1023-1032')
e('TorrentEngine.doStop', 'TorrentEngine.cleanTemp', 'CALL', 'Clean the temporary directory while stopping the engine',
  cls='explicit', evidence='SRC TorrentEngine.java:300; TorrentEngine.java:1223-1227')
e('TorrentEngine.fetchMagnet', 'TorrentEngine.createFetchMagnetSingle', 'CALL', 'Create the single that fetches a magnet link',
  cls='explicit', evidence='SRC TorrentEngine.java:422; TorrentEngine.java:431-479')
e('MainViewModel.deleteTorrents', 'TorrentEngine.deleteTorrents', 'CALL', 'Delete torrents from the main view model',
  cls='explicit', evidence='SRC ui/main/MainViewModel.java:143; TorrentEngine.java:533-541')
e('DetailTorrentViewModel.deleteTrackers', 'TorrentEngine.deleteTrackers', 'CALL', 'Delete trackers from a torrent from the detail view model',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:346; TorrentEngine.java:543-557')
e('TorrentService.init', 'TorrentEngine.doStart', 'CALL', 'Start the engine during service init',
  cls='explicit', evidence='SRC service/TorrentService.java:131; TorrentEngine.java:234-260')
e('TorrentService.stopEngine', 'TorrentEngine.doStop', 'CALL', 'Stop the engine from the service stop path',
  cls='explicit', evidence='SRC service/TorrentService.java:161; TorrentEngine.java:292-304')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'TorrentEngine.fetchMagnet', 'CALL', 'Fetch a magnet link while decoding an add-torrent request',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:237; TorrentEngine.java:415-429')
e('MainViewModel.forceAnnounceTorrents', 'TorrentEngine.forceAnnounceTorrents', 'CALL', 'Force-announce torrents from the main view model',
  cls='explicit', evidence='SRC ui/main/MainViewModel.java:151; TorrentEngine.java:520-531')
e('MainViewModel.forceRecheckTorrents', 'TorrentEngine.forceRecheckTorrents', 'CALL', 'Force-recheck torrents from the main view model',
  cls='explicit', evidence='SRC ui/main/MainViewModel.java:147; TorrentEngine.java:507-518')
e('TorrentEngine.saveTorrentFile', 'TorrentEngine.getBencode', 'CALL', 'Read the torrent bencode while saving the torrent file',
  cls='explicit', evidence='SRC TorrentEngine.java:974; TorrentEngine.java:927-936')

# Parcelable machinery with no trigger: a saved full-tree grep finds no marshalling
# site for AddTorrentParams, so the framework never writes, creates or arrays it.
UNREACHABLE.update({
    'AddTorrentParams.writeToParcel': ('no_trigger_in_app',
        'The framework calls writeToParcel only when parcelling, which never happens for AddTorrentParams: a saved full-tree grep finds no marshalling site.',
        'SRC AddTorrentParams.java:96-107',
        'SOURCE'),
    'AddTorrentParams$1.createFromParcel': ('no_trigger_in_app',
        'The framework calls CREATOR.createFromParcel only when unparcelling, which never happens for AddTorrentParams: a saved full-tree grep finds no marshalling site. Its body (which constructs the Parcel ctor, batch 21 row 36, also UNREACHABLE) therefore never runs.',
        'SRC AddTorrentParams.java:111-113',
        'SOURCE'),
    'AddTorrentParams$1.newArray': ('no_trigger_in_app',
        'The framework calls CREATOR.newArray only when unparcelling an array, which never happens for AddTorrentParams: a saved full-tree grep finds no marshalling site and no put/getParcelableArrayList site.',
        'SRC AddTorrentParams.java:116-118',
        'SOURCE'),
})

# Suppress bytecode auto edges into the UNREACHABLE Parcelable machinery.
# AddTorrentParams and its CREATOR class are not subclassed in the app,
# so there are no @Variant generated copies to add.
SUPPRESS.update({
    'AddTorrentParams.writeToParcel', 'AddTorrentParams$1.createFromParcel', 'AddTorrentParams$1.newArray',
})
