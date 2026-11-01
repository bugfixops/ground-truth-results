# Trunk part b000 (LibreTorrent 3.5.2 trigger graph, finish run).
# Hand-written trunk edges ONLY: the five entry chains that make the
# batch parts reachable from S_ENTRY. No label is changed here: this file
# adds e() edges only, and no SUPPRESS entries (see REPORT.md: no b000
# destination carries an UNREACHABLE entry in graph_def.py, so no
# "UNREACHABLE but has incoming edges" warning arises from these edges).
#
# Conventions (as in parts/b013.py):
# - Every evidence string cites lines printed in scratch/b000_printed.txt.
# - Paths in evidence are relative to
#   final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java,
#   except AndroidManifest.xml (at src/main) and org/nanohttpd/ files.
# - Edges already in graph_def.py are NOT repeated here; the route table in
#   parts/b000_trunks.md names them as graph_def dependencies.
# - Edges that a batch part also carries are included here because the
#   trunk needs them for entry reachability in a graph_def + b000 build;
#   each such overlap is listed in REPORT.md so the merger keeps exactly
#   one copy at merge.
# - Method names are build names (tools/build_graph.py method_names):
#   non-overloaded methods take BARE names; overloaded methods take
#   (params) with JVM-derived simple params. All endpoints below were
#   verified against method_names (see REPORT.md).

# ---- Chain 1: feed refresh -------------------------------------------------
# Entry (already in graph_def.py): S_ENTRY -> SettingsActivity.onCreate ->
# SettingsFragment -> openPreference -> FeedSettingsFragment.newInstance
# (two-pane) or startActivity -> PreferenceActivity -> getFragment ->
# FeedSettingsFragment.newInstance (single-pane) -> onCreate ->
# bindOnPreferenceChangeListener -> onPreferenceChange (REGISTER + FRAMEWORK).
# The task's cited lines: SettingsFragment.java:122 (feed header click
# listener) and 195-198 (FeedSettings case: setFragment on large screens,
# startActivity otherwise); PreferenceActivity.java:113-114 (FeedSettings
# branch of getFragment); FeedSettingsFragment.java:121 (bind), 134 and 142
# (the two runPeriodicalRefreshFeeds calls).

e('FeedSettingsFragment.onPreferenceChange', 'Scheduler.runPeriodicalRefreshFeeds', 'CALL', 'Re-schedule periodic feed refresh when auto-refresh is switched on',
  guard='preference key is pref_key_feed_auto_refresh and newValue is true', cls='explicit',
  evidence='SRC ui/settings/sections/FeedSettingsFragment.java:129-134')
e('FeedSettingsFragment.onPreferenceChange', 'Scheduler.runPeriodicalRefreshFeeds', 'CALL', 'Re-schedule periodic feed refresh when the refresh interval changes',
  guard='preference key is pref_key_feed_refresh_interval', cls='explicit',
  evidence='SRC ui/settings/sections/FeedSettingsFragment.java:139-142')
e('FeedSettingsFragment.onPreferenceChange', 'Scheduler.cancelPeriodicalRefreshFeeds', 'CALL', 'Cancel periodic feed refresh when auto-refresh is switched off',
  guard='preference key is pref_key_feed_auto_refresh and newValue is false', cls='explicit',
  evidence='SRC ui/settings/sections/FeedSettingsFragment.java:129-136')
e('Scheduler.runPeriodicalRefreshFeeds', 'Scheduler.getRefreshFeedsConstraints', 'CALL', 'Build the network constraints for the periodic refresh work',
  cls='explicit', evidence='SRC service/Scheduler.java:120; service/Scheduler.java:128-140')
e('Scheduler.runPeriodicalRefreshFeeds', 'FeedFetcherWorker.doWork', 'FRAMEWORK', 'WorkManager runs the enqueued periodic feed-fetch work',
  cls='non_standard', via='AndroidX WorkManager PeriodicWorkRequest',
  evidence='INFERRED WorkManager periodic-work dispatch; SRC service/Scheduler.java:112-125; service/FeedFetcherWorker.java:51,74')
# Downstream (already in graph_def.py): FeedFetcherWorker.doWork ->
# fetchChannels -> fetchChannel -> FeedParser.<init> / getItems.

# ---- Chain 2: torrent service and engine -----------------------------------
# Entry (already in graph_def.py): TorrentEngine.start ->
# Utils.startServiceBackground -> Utils.lambda$startServiceBackground$0 ->
# TorrentService.onCreate / onStartCommand; onStartCommand -> init.
# TorrentEngine.<init> -> TorrentSessionImpl.<init> is also in graph_def.py.

e('TorrentService.init', 'TorrentEngine.doStart', 'CALL', 'Start the engine during service init',
  cls='explicit', evidence='SRC service/TorrentService.java:131; core/model/TorrentEngine.java:234-260')
e('TorrentService.init', 'TorrentEngine.addListener', 'CALL', 'Register the service as an engine listener during service init',
  cls='explicit', evidence='SRC service/TorrentService.java:132; core/model/TorrentEngine.java:307-309')
e('TorrentEngine.<init>', 'TorrentSessionImpl.addListener', 'CALL', 'Register the engine listener on the concrete session at construction',
  cls='non_standard', via='TorrentSession interface dispatch to TorrentSessionImpl',
  evidence='INFERRED interface dispatch; SRC core/model/TorrentEngine.java:136-140; core/model/TorrentEngine.java:1265-1269; core/model/session/TorrentSessionImpl.java:184-188')
e('TorrentEngine.addListener', 'TorrentSessionImpl.addListener', 'CALL', 'Forward an engine listener registration to the concrete session',
  cls='non_standard', via='TorrentSession interface dispatch to TorrentSessionImpl',
  evidence='INFERRED interface dispatch; SRC core/model/TorrentEngine.java:307-309; core/model/session/TorrentSessionImpl.java:184-188')
e('TorrentEngine.doStart', 'TorrentSessionImpl.start', 'CALL', 'Start the libtorrent session',
  cls='non_standard', via='TorrentSession interface field (TorrentEngine.java:100); TorrentSessionImpl implements it',
  evidence='INFERRED interface dispatch; SRC core/model/TorrentEngine.java:234-235,259; core/model/session/TorrentSessionImpl.java:862-863')
e('TorrentSessionImpl.start', 'TorrentSessionImpl.onAfterStart', 'FRAMEWORK', 'libtorrent session start calls the onAfterStart hook',
  cls='non_standard', via='libtorrent4j SessionManager.start(SessionParams) calls the protected onAfterStart hook (library, not in upload)',
  evidence='INFERRED libtorrent4j SessionManager.start calls onAfterStart; SRC core/model/session/TorrentSessionImpl.java:907,990-991')
e('TorrentSessionImpl.onAfterStart', 'TorrentSessionImpl.lambda$onAfterStart$4', 'FRAMEWORK', 'Completable runs the notify lambda on the io scheduler',
  cls='non_standard', via='RxJava Completable.fromRunnable runs the Runnable on Schedulers.io() (library, not in upload)',
  evidence='INFERRED RxJava Completable.fromRunnable runs the lambda on subscribe; SRC core/model/session/TorrentSessionImpl.java:1009-1012')
e('TorrentSessionImpl.lambda$onAfterStart$4', 'TorrentSessionImpl.notifyListeners', 'CALL', 'Notify the registered engine listeners that the session started',
  cls='explicit', evidence='SRC core/model/session/TorrentSessionImpl.java:1009-1010')
e('TorrentSessionImpl.notifyListeners', 'TorrentEngine$5.onSessionStarted', 'CALL', 'Deliver onSessionStarted to the listener TorrentEngine registered',
  cls='standard', evidence='SRC core/model/session/TorrentSessionImpl.java:1447-1449; core/model/TorrentEngine.java:140,1265-1269')
e('TorrentEngine$5.onSessionStarted', 'TorrentEngine.handleOnSessionStarted', 'CALL', 'Handle session start in the engine',
  cls='explicit', evidence='SRC core/model/TorrentEngine.java:1267-1268')
# Note on the service listener: TorrentService.engineListener (the anonymous
# TorrentService$1) is registered by the init -> addListener edge above, but
# it overrides only onSessionStopped (TorrentService.java:255-262), not
# onSessionStarted, so no onSessionStarted edge to it is claimed on this
# start path. Its stop path is chain 5 below.

# ---- Chain 3: add torrent ---------------------------------------------------
# Entry (already in graph_def.py): S_ENTRY -> AddTorrentActivity.onCreate
# (exported SEND/VIEW activity, AndroidManifest.xml:62-64); onCreate ->
# observeDecodeState -> lambda$observeDecodeState$1 -> getUri / startDecode;
# onOptionsItemSelected -> addTorrent -> AddTorrentViewModel.addTorrent ->
# lambda$addTorrent$5 -> TorrentEngine.addTorrentSync(AddTorrentParams,boolean)
# -> TorrentSessionImpl.addTorrent (graph_def.py SUPPRESS pair aside).

e('AddTorrentActivity.onCreate', 'AddTorrentViewModel.<init>', 'FRAMEWORK', 'ViewModelProvider constructs the add-torrent view model on first request',
  cls='non_standard', via='AndroidX ViewModelProvider',
  evidence='INFERRED AndroidX ViewModelProvider construction; SRC ui/addtorrent/AddTorrentActivity.java:103-104; ui/addtorrent/AddTorrentViewModel.java:128-133')
e('AddTorrentViewModel.<init>', 'TorrentEngine.getInstance', 'CALL', 'Obtain the torrent engine while constructing the add-torrent view model',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:133')
e('AddTorrentViewModel.<init>', 'TorrentEngine.observeNeedStartEngine', 'CALL', 'Subscribe to engine-start need while constructing the add-torrent view model',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:135-138')
e('AddTorrentViewModel.<init>', 'TorrentEngine.start', 'CALL', 'Start the engine from the add-torrent view model when it is needed',
  guard='needStart is true', cls='non_standard', via='RxJava subscribe/filter dispatch in <init>',
  evidence='INFERRED RxJava subscribe/filter dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:135-138; core/model/TorrentEngine.java:148-153')
e('AddTorrentViewModel.startDecode', 'AddTorrentViewModel.startDecodeTask', 'CALL', 'Start the decode task once the engine is running',
  guard='isRunning is true', cls='non_standard', via='RxJava subscribe dispatch in startDecode',
  evidence='INFERRED RxJava subscribe dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:182-194; ui/addtorrent/AddTorrentViewModel.java:197-199')
e('AddTorrentViewModel.startDecodeTask', 'AddTorrentViewModel$TorrentDecodeTask.<init>', 'CALL', 'Construct the torrent decode task for the incoming URI',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:197-199; ui/addtorrent/AddTorrentViewModel.java:202-209')
e('AddTorrentViewModel.startDecodeTask', 'AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'FRAMEWORK', 'AsyncTask runs the decode task on the thread-pool executor',
  cls='non_standard', via='Android AsyncTask THREAD_POOL_EXECUTOR dispatch',
  evidence='INFERRED Android AsyncTask dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:197-199; ui/addtorrent/AddTorrentViewModel.java:217-220')
# Downstream (batch b022, not repeated): TorrentDecodeTask.doInBackground ->
# TorrentEngine.fetchMagnet (magnet URIs) and the decode-state posts that
# drive AddTorrentActivity.onStopDecode -> makeFileTree (graph_def.py).

# ---- Chain 4: streaming server ----------------------------------------------
# Primary entry: the chain-2 spine above, continuing from
# TorrentEngine$5.onSessionStarted -> handleOnSessionStarted. A second entry
# is the settings-change restart (doStart subscribes handleSettingsChanged;
# a streaming key change restarts the server). A third, user-facing entry
# is sharing a stream URL from the detail files screen.

e('TorrentEngine.handleOnSessionStarted', 'TorrentEngine.startStreamingServer', 'CALL', 'Start the streaming server when streaming is enabled',
  guard='pref.enableStreaming()', cls='explicit', evidence='SRC core/model/TorrentEngine.java:1056-1058; core/model/TorrentEngine.java:1063-1077')
e('TorrentEngine.doStart', 'TorrentEngine.handleSettingsChanged', 'CALL', 'Engine start subscribes the settings-change handler',
  cls='non_standard', via='RxJava subscription method reference in doStart',
  evidence='INFERRED Rx dispatch; SRC core/model/TorrentEngine.java:240-242; core/model/TorrentEngine.java:1456-1458')
e('TorrentEngine.handleSettingsChanged', 'TorrentEngine.startStreamingServer', 'CALL', 'Restart the streaming server when streaming is switched on',
  guard='key is pref_key_streaming_enable and pref.enableStreaming()', cls='explicit', evidence='SRC core/model/TorrentEngine.java:1592-1594')
e('TorrentEngine.handleSettingsChanged', 'TorrentEngine.startStreamingServer', 'CALL', 'Restart the streaming server when its hostname or port changes',
  guard='key is pref_key_streaming_port or pref_key_streaming_hostname', cls='explicit', evidence='SRC core/model/TorrentEngine.java:1598-1600')
e('TorrentEngine.startStreamingServer', 'TorrentStreamServer.<init>', 'CALL', 'Construct the streaming HTTP server with the configured host and port',
  cls='explicit', evidence='SRC core/model/TorrentEngine.java:1069; core/model/stream/TorrentStreamServer.java:67-70')
e('TorrentEngine.startStreamingServer', 'TorrentStreamServer.start', 'CALL', 'Start the streaming HTTP server',
  cls='explicit', evidence='SRC core/model/TorrentEngine.java:1071; core/model/stream/TorrentStreamServer.java:72-78')
e('TorrentStreamServer.start', 'TorrentEngine.getInstance', 'CALL', 'Obtain the torrent engine while starting the streaming server',
  cls='explicit', evidence='SRC core/model/stream/TorrentStreamServer.java:72-78')
e('TorrentStreamServer.start', 'NanoHTTPD.start()', 'CALL', 'Start the NanoHTTPD base server',
  cls='explicit', evidence='SRC core/model/stream/TorrentStreamServer.java:78; org/nanohttpd/NanoHTTPD.java:1794-1795')
# Downstream (batch b017, not repeated): NanoHTTPD.start() -> start(int) ->
# start(int,boolean) -> createServerRunnable -> ServerRunnable.run ->
# createClientHandler / DefaultAsyncRunner.exec -> ClientHandler.run ->
# HTTPSession.execute -> TorrentStreamServer.serve -> handleTorrent.
e('DetailTorrentFilesFragment.shareStreamUrl', 'DetailTorrentViewModel.getStreamUrl', 'CALL', 'Build the stream URL for the selected file to share it',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:509-524; ui/detailtorrent/DetailTorrentViewModel.java:338-343')
e('DetailTorrentViewModel.getStreamUrl', 'TorrentStreamServer.makeStreamUrl', 'CALL', 'Format the /stream URL for a torrent file',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:338-343; core/model/stream/TorrentStreamServer.java:93-108')

# ---- Chain 5: notification actions ------------------------------------------
# The foreground notification's buttons are PendingIntents built in
# TorrentService.initPendingIntents (graph_def.py, REGISTER edges to
# NotificationReceiver.<init> / onReceive). Tapping a button is a system
# delivery of the app's own PendingIntent, modelled here as an S_ENTRY
# ENTRY edge exactly as S_ENTRY -> BootReceiver.onReceive models system
# delivery of a boot broadcast in graph_def.py. Note the receiver is
# exported=false (AndroidManifest.xml:256-263): it cannot be triggered by
# other apps, only by these PendingIntents.
# Entry points and where they lead (all printed in NotificationReceiver
# and TorrentService):
#   SHUTDOWN_APP  -> MainActivity.onCreate (graph_def.py) + TorrentService.onStartCommand (graph_def.py) -> handleShutdownActions -> shutdown
#   ADD_TORRENT   -> MainActivity.onCreate (graph_def.py)
#   PAUSE_ALL / RESUME_ALL / PAUSE_RESUME_ALL -> TorrentService.onStartCommand (graph_def.py) -> handleActions -> pauseAll / resumeAll

e('S_ENTRY', 'NotificationReceiver.<init>', 'ENTRY', 'Instantiate the notification-action receiver for a tapped notification action',
  cls='standard', env='PendingIntent.getBroadcast(', env_kinds=('system_event',),
  evidence='SRC AndroidManifest.xml:256-263; service/TorrentService.java:497-524; receiver/NotificationReceiver.java:33-42')
e('S_ENTRY', 'NotificationReceiver.onReceive', 'ENTRY', 'Deliver a tapped notification action to the notification-action receiver',
  cls='standard', env='PendingIntent.getBroadcast(', env_kinds=('system_event',),
  evidence='SRC AndroidManifest.xml:256-263; service/TorrentService.java:497-524; receiver/NotificationReceiver.java:41-81')
e('TorrentService.handleShutdownActions', 'TorrentService.shutdown', 'CALL', 'Shut the service down for a shutdown action',
  guard='action is NOTIFY_ACTION_SHUTDOWN_APP or ACTION_SHUTDOWN', cls='explicit', evidence='SRC service/TorrentService.java:199-205')
e('TorrentService.handleShutdownActions', 'TorrentService.makeForegroundNotify', 'CALL', 'Rebuild the foreground notification for a restart-foreground action',
  guard='action is ACTION_RESTART_FOREGROUND_NOTIFICATION', cls='explicit', evidence='SRC service/TorrentService.java:206-208')
e('TorrentService.shutdown', 'TorrentService.stopEngine', 'CALL', 'Stop the engine on the shutdown path',
  cls='non_standard', via='RxJava Completable.fromRunnable dispatch in shutdown',
  evidence='INFERRED RxJava Completable.fromRunnable dispatch; SRC service/TorrentService.java:150-155')
e('TorrentService.stopEngine', 'TorrentEngine.doStop', 'CALL', 'Stop the engine from the service stop path',
  cls='explicit', evidence='SRC service/TorrentService.java:157-162; core/model/TorrentEngine.java:292-304')
e('TorrentService.handleActions', 'TorrentEngine.pauseAll', 'CALL', 'Pause all torrents for a notification pause action',
  guard='action is NOTIFY_ACTION_PAUSE_ALL or (PAUSE_RESUME_ALL and not paused)', cls='explicit', evidence='SRC service/TorrentService.java:217-218,224-229')
e('TorrentService.handleActions', 'TorrentEngine.resumeAll', 'CALL', 'Resume all torrents for a notification resume action',
  guard='action is NOTIFY_ACTION_RESUME_ALL or (PAUSE_RESUME_ALL and paused)', cls='explicit', evidence='SRC service/TorrentService.java:220-221,224-230')
e('TorrentService.makeForegroundNotify', 'TorrentService.setForegroundNotifyActions', 'CALL', 'Attach the pause/resume/shutdown action buttons to the foreground notification',
  cls='explicit', evidence='SRC service/TorrentService.java:361; service/TorrentService.java:455-490')
# Tapping the notification body opens the main activity (content intent
# built in makeForegroundNotify); tapping a finished-torrent notification
# opens the detail activity (openPendingIntent built in
# TorrentNotifier.makeTorrentFinishedNotify). Both are INTENT deliveries of
# the app's own PendingIntents.
e('TorrentService.makeForegroundNotify', 'MainActivity.<init>', 'INTENT', 'Open the main activity when the foreground notification body is tapped',
  cls='standard', env='PendingIntent.getActivity(', env_kinds=('system_event',),
  evidence='SRC service/TorrentService.java:342-351')
e('TorrentService.makeForegroundNotify', 'MainActivity.onCreate', 'INTENT', 'Create the main activity when the foreground notification body is tapped',
  cls='standard', env='PendingIntent.getActivity(', env_kinds=('system_event',),
  evidence='SRC service/TorrentService.java:342-351')
e('TorrentNotifier.makeTorrentFinishedNotify', 'DetailTorrentActivity.<init>', 'INTENT', 'Open the detail activity when a finished-torrent notification is tapped',
  cls='standard', env='openPendingIntent',
  evidence='SRC ui/TorrentNotifier.java:230-239; ui/detailtorrent/DetailTorrentActivity.java:40-56')
e('TorrentNotifier.makeTorrentFinishedNotify', 'DetailTorrentActivity.onCreate', 'INTENT', 'Create the detail activity when a finished-torrent notification is tapped',
  cls='standard', env='openPendingIntent',
  evidence='SRC ui/TorrentNotifier.java:230-239; ui/detailtorrent/DetailTorrentActivity.java:40-56')
# Engine-stop loop back to the service: onAfterStop notifies listeners;
# the service listener (TorrentService$1, registered by chain 2's
# init -> addListener edge) stops the service. This is distinct from batch
# b026's edge to the base TorrentEngineListener.onSessionStopped.
e('TorrentSessionImpl.notifyListeners', 'TorrentService$1.onSessionStopped', 'CALL', 'Deliver onSessionStopped to the listener TorrentService registered',
  cls='non_standard', via='session listener dispatch to the service listener',
  evidence='INFERRED session listener dispatch; SRC core/model/session/TorrentSessionImpl.java:1041-1044; core/model/session/TorrentSessionImpl.java:1445-1450; service/TorrentService.java:255-262')
e('TorrentService$1.onSessionStopped', 'TorrentService.stopService', 'CALL', 'Stop the service when the session reports it stopped',
  cls='explicit', evidence='SRC service/TorrentService.java:257-261')
