"""LibreTorrent 3.5.2 schema-2 trigger graph.

This file is being rebuilt from the uploaded source.  The generated draft is
preserved separately and is not imported here.
"""

TITLE = 'LibreTorrent 3.5.2 trigger graph — source re-audit'
STRICT = True
USE_AUTO = True
PREFER_SETUP_OVER_ENV = True

# These bytecode call pairs have no route-bearing caller.  Suppress them from
# the inventory-derived auto edges after confirming their source call sites.
SUPPRESS = {
    ('NanoHTTPD.decodeParameters(Map)', 'NanoHTTPD.decodeParameters(String)'),
    ('NanoHTTPD.mimeTypes', 'NanoHTTPD.loadMimeTypes'),
    ('NanoHTTPD.makeSSLSocketFactory(String,char[])', 'NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManagerFactory)'),
    ('NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManagerFactory)', 'NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManager[])'),
    ('NanoHTTPD.getMimeTypeForFile', 'NanoHTTPD.mimeTypes'),
    ('NanoHTTPD.isAlive', 'NanoHTTPD.wasStarted'),
    ('NanoHTTPD$Cookie.<init>(String,String)', 'NanoHTTPD$Cookie.<init>(String,String,int)'),
    ('NanoHTTPD.makeSecure', 'NanoHTTPD$SecureServerSocketFactory.<init>'),
    ('TorrentEngine.addTorrentSync(AddTorrentParams,boolean)', 'TorrentSessionImpl.addTorrent'),
    ('TorrentSessionImpl.addTorrent', 'TorrentSessionImpl.download(String,AddTorrentParams,byte[])'),
}

# Remove inventory-generated component edges that the printed app source
# disproves: receivers are internal and PendingIntent cancellation is not a
# receiver invocation.
_GENERATED_EDGE_DROPS = {
    ('S_ENTRY', 'S_SYS_NotificationReceiver', 'ENTRY'),
    ('S_ENTRY', 'S_SYS_SchedulerReceiver', 'ENTRY'),
    ('Scheduler.cancelStartAppAlarm', 'S_SYS_SchedulerReceiver', 'INTENT'),
    ('Scheduler.cancelStopAppAlarm', 'S_SYS_SchedulerReceiver', 'INTENT'),
}
_append_edge = e

def _filter_generated_edge(src, dst, kind, trigger, *args, **kwargs):
    if (src, dst, kind) in _GENERATED_EDGE_DROPS:
        return
    return _append_edge(src, dst, kind, trigger, *args, **kwargs)

e = _filter_generated_edge


def _source_audit_edit(edge):
    """Do not represent generated framework guesses as remembered facts."""
    evidence = edge.get('evidence') or ''

    # Exact source predicates/texts replace generator prose gates. The kind
    # maps below classify these exact strings after this edit runs.
    if edge.get('src') == 'S_ENTRY' and edge.get('dst') == 'S_SYS_BootReceiver':
        edge['env'] = 'isBootCompleted(action)'
    elif edge.get('src') == 'S_ENTRY' and edge.get('dst') in {
        'MainActivity.onCreate', 'MainActivity.<init>',
        'SendTextToClipboard.<init>', 'SendTextToClipboard.onCreate',
        'AddFeedActivity.<init>', 'AddFeedActivity.onCreate',
        'AddTorrentActivity.<init>', 'AddTorrentActivity.onCreate',
        'SettingsActivity.<init>', 'SettingsActivity.onCreate'
    }:
        edge['env'] = 'android:exported="true"'
    elif edge.get('src') == 'TorrentNotifier.makeTorrentFinishedNotify' and edge.get('dst') == 'DetailTorrentActivity.<init>':
        edge['env'] = 'openPendingIntent'
    elif edge.get('src') == 'TorrentService.initPendingIntents' and edge.get('dst') == 'S_SYS_NotificationReceiver':
        edge['env'] = 'PendingIntent.getBroadcast('
    elif edge.get('src') == 'Scheduler.setStartStopAppAlarm' and edge.get('dst') == 'S_SYS_SchedulerReceiver':
        edge['env'] = 'calendar.getTimeInMillis()'

    if edge.get('needs_state') == 'The list / adapter shows at least one row (some user data exists: add an item first)':
        edge['needs_state'] = 'getAdapter().getItemCount()'


EDIT = _source_audit_edit
ENV_KINDS_OF = {
    'isBootCompleted(action)': ['system_event'],
    'android.app.action.SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED': ['system_event'],
    'android:exported="true"': ['other_app'],
    'openPendingIntent': ['system_event'],
    'PendingIntent.getBroadcast(': ['system_event'],
    'calendar.getTimeInMillis()': ['time'],
}
STATE_KINDS_OF = {
    'getAdapter().getItemCount()': ['data'],
    'adapter.getItemCount() > 0': ['data'],
    'pref.autostart() && pref.keepAlive()': ['settings'],
    'pref.enableSchedulingStart()': ['settings'],
    'pref.enableSchedulingShutdown()': ['settings'],
    'isRunning()': ['session'],
}

# S3 entry/lifecycle edges authored from manifest and Android 8.1 source.
# Application startup and activity creation dispatch are standard framework
# callbacks; calls within the app body are explicit app-code calls.
SCREENS['S_ENTRY'] = {'title': 'Application entry'}
e('S_ENTRY', 'MainApplication.onCreate', 'ENTRY', 'Application process startup',
  cls='standard', evidence='SRC AndroidManifest.xml:31-32; FW-SRC core/java/android/app/ActivityThread.java:5709-5742; core/java/android/app/Instrumentation.java:1118-1119')
e('S_ENTRY', 'MainApplication.<init>', 'ENTRY', 'Instantiate manifest application class',
  cls='standard', evidence='SRC AndroidManifest.xml:31-32; MainApplication.java:37; FW-SRC core/java/android/app/LoadedApk.java:959-985; core/java/android/app/Instrumentation.java:1084-1104')
e('S_ENTRY', 'MainApplication.<clinit>', 'ENTRY', 'Initialize manifest application class before construction',
  cls='standard', evidence='SRC MainApplication.java:40-43; INFERRED Java class initialization during class loading; FW-SRC core/java/android/app/Instrumentation.java:1084-1104')
e('S_ENTRY', 'MainActivity.onCreate', 'ENTRY', 'Launcher activity startup',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:43-59; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('S_ENTRY', 'MainActivity.<clinit>', 'ENTRY', 'Initialize the launcher activity class before first use',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:43-59; ui/main/MainActivity.java:99; INFERRED JVM class initialization before construction; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('MainApplication.onCreate', 'TorrentNotifier.getInstance', 'CALL', 'Initialize notification service facade',
  cls='explicit', evidence='SRC MainApplication.java:70; ui/TorrentNotifier.java:65-72')
e('MainApplication.onCreate', 'MainApplication.increaseCursorWindowSize', 'CALL', 'Increase CursorWindow capacity after ACRA initialization',
  cls='explicit', evidence='SRC MainApplication.java:66-70,73-82')
e('MainApplication.onCreate', 'TorrentNotifier.makeNotifyChans', 'CALL', 'Create notification channels during application startup',
  cls='explicit', evidence='SRC MainApplication.java:70; ui/TorrentNotifier.java:81-114')
e('MainActivity.onCreate', 'TorrentInfoProvider.getInstance(Context)', 'CALL', 'Initialize torrent info provider for main screen',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:146; core/model/TorrentInfoProvider.java:76-87')
e('TorrentInfoProvider.getInstance(Context)', 'TorrentEngine.getInstance', 'CALL', 'Obtain the app torrent engine while initializing torrent info provider',
  cls='explicit', evidence='SRC core/model/TorrentInfoProvider.java:76-87')
e('TorrentEngine.getInstance', 'TorrentEngine.<init>', 'CALL', 'Construct the singleton torrent engine on its first request',
  guard='INSTANCE == null', cls='explicit', evidence='SRC core/model/TorrentEngine.java:117-125')
e('TorrentEngine.<init>', 'TorrentSessionImpl.<init>', 'CALL', 'Construct the concrete session owned by the torrent engine',
  cls='explicit', evidence='SRC core/model/TorrentEngine.java:128-141')
e('MainActivity.onCreate', 'Utils.getAppTheme', 'CALL', 'Resolve the user-selected app theme before activity creation',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:136-138; core/utils/Utils.java:374-388')
e('MainActivity.onCreate', 'MainActivity.onStart', 'LIFECYCLE', 'Activity starts after successful creation',
  guard='getIntent().getAction() != NOTIFY_ACTION_SHUTDOWN_APP; !mFinished', cls='standard', evidence='SRC ui/main/MainActivity.java:140-144,381-389; FW-SRC core/java/android/app/ActivityThread.java:2738-2745; core/java/android/app/Activity.java:7014-7023; core/java/android/app/Instrumentation.java:1333-1335')
e('MainActivity.onStart', 'MainActivity.subscribeAlertDialog', 'CALL', 'Subscribe to alert dialog events at activity start',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:381-389')
e('MainActivity.onStart', 'MainActivity.subscribeMsgViewModel', 'CALL', 'Subscribe to message events at activity start',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:381-389')
e('MainActivity.onStart', 'MainActivity.subscribeSessionStats', 'CALL', 'Subscribe to session stats at activity start',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:381-389')
e('MainActivity.onStart', 'MainActivity.subscribeNeedStartEngine', 'CALL', 'Subscribe to engine start state at activity start',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:381-389')
e('MainActivity.onStart', 'MainActivity.subscribeTags', 'CALL', 'Subscribe to tag state at activity start',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:381-389')
e('MainActivity.onStart', 'MainActivity.onPostCreate', 'LIFECYCLE', 'Dispatch post-create callback after start and state restoration',
  cls='standard', evidence='FW-SRC core/java/android/app/ActivityThread.java:2727-2762; core/java/android/app/Instrumentation.java:1284-1286; SRC ui/main/MainActivity.java:372-378')
e('MainActivity.onStop', 'MainActivity.onDestroy', 'LIFECYCLE', 'Destroy activity during framework teardown after stop',
  cls='standard', evidence='FW-SRC core/java/android/app/ActivityThread.java:4029-4041,4368-4377; core/java/android/app/Instrumentation.java:1232-1250,1374-1376; SRC ui/main/MainActivity.java:396-404')
e('MainActivity.onStart', 'MainActivity.onStop', 'LIFECYCLE', 'Stop the activity after it leaves the started foreground state',
  cls='standard', evidence='FW-SRC core/java/android/app/Activity.java:7130-7182; core/java/android/app/Instrumentation.java:1374-1376; SRC ui/main/MainActivity.java:381-394')
e('MainActivity.onDestroy', 'MainViewModel.requestStopEngine', 'CALL', 'Request engine shutdown while destroying the main activity',
  guard='viewModel != null', cls='explicit', evidence='SRC ui/main/MainActivity.java:396-403; ui/main/MainViewModel.java:166-168')
e('S_ENTRY', 'MainActivity.<init>', 'ENTRY', 'Instantiate launcher activity',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:43-45; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('S_ENTRY', 'AddTorrentActivity.<init>', 'ENTRY', 'Instantiate exported torrent-add activity for matching SEND or VIEW intent',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:62-92; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('S_ENTRY', 'AddTorrentActivity.<clinit>', 'ENTRY', 'Initialize the exported torrent-add activity class before first use',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:62-92; ui/addtorrent/AddTorrentActivity.java:73; INFERRED JVM class initialization before construction; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('S_ENTRY', 'AddTorrentActivity.onCreate', 'ENTRY', 'Create exported torrent-add activity for matching SEND or VIEW intent',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:62-92; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('S_ENTRY', 'SendTextToClipboard.<init>', 'ENTRY', 'Instantiate exported text-share activity',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:141-152; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('S_ENTRY', 'SendTextToClipboard.onCreate', 'ENTRY', 'Create exported text-share activity',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:141-152; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('S_ENTRY', 'SettingsActivity.<init>', 'ENTRY', 'Instantiate exported settings activity',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:155-161; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('S_ENTRY', 'SettingsActivity.onCreate', 'ENTRY', 'Create exported settings activity',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:155-161; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('S_ENTRY', 'SettingsActivity.<clinit>', 'ENTRY', 'Initialize the exported settings activity class before first use',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:155-161; ui/settings/SettingsActivity.java:35; INFERRED JVM class initialization before construction; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('S_ENTRY', 'AddFeedActivity.<init>', 'ENTRY', 'Instantiate exported feed-add activity for matching SEND or VIEW intent',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:179-227; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('S_ENTRY', 'AddFeedActivity.onCreate', 'ENTRY', 'Create exported feed-add activity for matching SEND or VIEW intent',
  cls='standard', env='android:exported="true"', evidence='SRC AndroidManifest.xml:179-227; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('S_ENTRY', 'BootReceiver.<init>', 'ENTRY', 'Instantiate receiver for a boot or quickboot broadcast',
  cls='standard', env='isBootCompleted(action)', evidence='SRC AndroidManifest.xml:265-274; receiver/BootReceiver.java:54-58; FW-SRC core/java/android/app/ActivityThread.java:3141-3167')
e('S_ENTRY', 'BootReceiver.onReceive', 'ENTRY', 'Deliver boot or quickboot broadcast',
  cls='standard', env='isBootCompleted(action)', evidence='SRC AndroidManifest.xml:265-274; receiver/BootReceiver.java:39-58; FW-SRC core/java/android/app/ActivityThread.java:3176-3188')
e('S_ENTRY', 'BootReceiver.<init>', 'ENTRY', 'Instantiate receiver for exact-alarm permission state change broadcast',
  cls='standard', env='android.app.action.SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED', evidence='SRC AndroidManifest.xml:265-274; FW-SRC core/java/android/app/ActivityThread.java:3141-3167')
e('S_ENTRY', 'BootReceiver.onReceive', 'ENTRY', 'Deliver exact-alarm permission state change broadcast',
  cls='standard', env='android.app.action.SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED', evidence='SRC AndroidManifest.xml:265-274; receiver/BootReceiver.java:39-51; FW-SRC core/java/android/app/ActivityThread.java:3176-3188')
e('BootReceiver.onReceive', 'TorrentEngine.getInstance', 'CALL', 'Get engine and autostart after boot when both settings are enabled',
  guard='isBootCompleted(action) && pref.autostart() && pref.keepAlive()', needs_state='pref.autostart() && pref.keepAlive()', cls='explicit', evidence='SRC receiver/BootReceiver.java:43-48; core/model/TorrentEngine.java:117-125')
e('BootReceiver.onReceive', 'TorrentEngine.start', 'CALL', 'Start engine after boot when both settings are enabled',
  guard='isBootCompleted(action) && pref.autostart() && pref.keepAlive()', needs_state='pref.autostart() && pref.keepAlive()', cls='explicit', evidence='SRC receiver/BootReceiver.java:43-48')
e('TorrentEngine.start', 'Utils.startServiceBackground', 'CALL', 'Start TorrentService for engine startup',
  guard='!isRunning()', cls='explicit', evidence='SRC core/model/TorrentEngine.java:148-153')
e('Utils.startServiceBackground', 'Utils.lambda$startServiceBackground$0', 'REGISTER', 'Post service launch on the main thread on API 26 and later',
  guard='Build.VERSION.SDK_INT >= Build.VERSION_CODES.O', cls='standard', evidence='SRC core/utils/Utils.java:426-434')
e('Utils.lambda$startServiceBackground$0', 'TorrentService.<init>', 'INTENT', 'Instantiate explicit TorrentService target',
  cls='standard', evidence='SRC core/model/TorrentEngine.java:148-153; core/utils/Utils.java:426-434; FW-SRC core/java/android/app/ActivityThread.java:3311-3327')
e('Utils.lambda$startServiceBackground$0', 'TorrentService.onCreate', 'INTENT', 'Create explicit TorrentService target',
  cls='standard', evidence='SRC core/model/TorrentEngine.java:148-153; core/utils/Utils.java:426-434; service/TorrentService.java:105-114; FW-SRC core/java/android/app/ActivityThread.java:3311-3340')
e('Utils.lambda$startServiceBackground$0', 'TorrentService.onStartCommand', 'INTENT', 'Deliver service start intent to explicit TorrentService target',
  cls='standard', evidence='SRC core/model/TorrentEngine.java:148-153; core/utils/Utils.java:426-434; FW-SRC core/java/android/app/ActivityThread.java:3464-3475')
e('TorrentService.onCreate', 'TorrentService.initPendingIntents', 'CALL', 'Initialize notification action PendingIntents',
  cls='explicit', evidence='SRC service/TorrentService.java:105-114')
e('TorrentService.onCreate', 'TorrentService.makeForegroundNotify', 'CALL', 'Create initial foreground notification',
  cls='explicit', evidence='SRC service/TorrentService.java:105-114')
e('TorrentService.onStartCommand', 'TorrentService.handleShutdownActions', 'CALL', 'Inspect service shutdown and foreground restart actions',
  guard='action != null', cls='explicit', evidence='SRC service/TorrentService.java:178-187; service/TorrentService.java:199-211')
e('TorrentService.onStartCommand', 'TorrentService.init', 'CALL', 'Initialize service on its first start',
  guard='isAlreadyRunning.compareAndSet(false, true)', cls='explicit', evidence='SRC service/TorrentService.java:189-192')
e('TorrentService.onStartCommand', 'TorrentService.handleActions', 'CALL', 'Apply non-shutdown service action',
  guard='action != null', cls='explicit', evidence='SRC service/TorrentService.java:193-195; service/TorrentService.java:214-232')
e('TorrentService.initPendingIntents', 'NotificationReceiver.<init>', 'REGISTER', 'Create notification receiver when a notification action is activated',
  env='PendingIntent.getBroadcast(', cls='standard', evidence='SRC service/TorrentService.java:497-524; receiver/NotificationReceiver.java:33-42; FW-SRC core/java/android/app/ActivityThread.java:3164-3188')
e('TorrentService.initPendingIntents', 'NotificationReceiver.onReceive', 'REGISTER', 'Deliver activated notification action to its receiver',
  env='PendingIntent.getBroadcast(', cls='standard', evidence='SRC service/TorrentService.java:497-524; receiver/NotificationReceiver.java:41-81; FW-SRC core/java/android/app/ActivityThread.java:3164-3188')
e('NotificationReceiver.onReceive', 'TorrentService.onStartCommand', 'INTENT', 'Start service for notification shutdown, pause, or resume actions',
  guard='action is one of NOTIFY_ACTION_SHUTDOWN_APP, NOTIFY_ACTION_PAUSE_ALL, NOTIFY_ACTION_RESUME_ALL, NOTIFY_ACTION_PAUSE_RESUME_ALL', cls='standard', evidence='SRC receiver/NotificationReceiver.java:50-58,66-80; service/TorrentService.java:175-232; FW-SRC core/java/android/app/ActivityThread.java:3464-3475')
e('NotificationReceiver.onReceive', 'MainActivity.onCreate', 'INTENT', 'Open main activity for notification shutdown or add-torrent actions',
  guard='action is NOTIFY_ACTION_SHUTDOWN_APP or NOTIFY_ACTION_ADD_TORRENT', cls='standard', evidence='SRC receiver/NotificationReceiver.java:50-65; AndroidManifest.xml:43-60; FW-SRC core/java/android/app/ActivityThread.java:2644-2660,2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('BootReceiver.onReceive', 'BootReceiver.initScheduling', 'CALL', 'Initialize configured alarms after boot or exact-alarm permission change',
  guard='isBootCompleted(action) or action == ACTION_SCHEDULE_EXACT_ALARM_PERMISSION_STATE_CHANGED', cls='explicit', evidence='SRC receiver/BootReceiver.java:43-51,60-72')
e('BootReceiver.initScheduling', 'Scheduler.setStartAppAlarm', 'CALL', 'Schedule app start when enabled in settings',
  guard='pref.enableSchedulingStart()', needs_state='pref.enableSchedulingStart()', cls='explicit', evidence='SRC receiver/BootReceiver.java:60-66; service/Scheduler.java:52-58')
e('BootReceiver.initScheduling', 'Scheduler.setStopAppAlarm', 'CALL', 'Schedule app shutdown when enabled in settings',
  guard='pref.enableSchedulingShutdown()', needs_state='pref.enableSchedulingShutdown()', cls='explicit', evidence='SRC receiver/BootReceiver.java:60-72; service/Scheduler.java:52-58')
e('Scheduler.setStartAppAlarm', 'Scheduler.setStartStopAppAlarm', 'CALL', 'Create start-app alarm',
  cls='explicit', evidence='SRC service/Scheduler.java:52-55,80-105')
e('Scheduler.setStopAppAlarm', 'Scheduler.setStartStopAppAlarm', 'CALL', 'Create stop-app alarm',
  cls='explicit', evidence='SRC service/Scheduler.java:56-58,80-105')
e('Scheduler.setStartStopAppAlarm', 'SchedulerReceiver.<init>', 'REGISTER', 'Deliver scheduled alarm to app receiver',
  env='calendar.getTimeInMillis()', cls='standard', evidence='SRC service/Scheduler.java:80-105; receiver/SchedulerReceiver.java:41-45; FW-SRC core/java/android/app/ActivityThread.java:3141-3167')
e('Scheduler.setStartStopAppAlarm', 'SchedulerReceiver.onReceive', 'REGISTER', 'Deliver scheduled start or stop action',
  env='calendar.getTimeInMillis()', cls='standard', evidence='SRC service/Scheduler.java:80-105; receiver/SchedulerReceiver.java:41-63; FW-SRC core/java/android/app/ActivityThread.java:3176-3188')
e('SchedulerReceiver.onReceive', 'SchedulerReceiver.onStartApp', 'CALL', 'Handle scheduled start-app alarm',
  guard='intent.getAction() == SCHEDULER_WORK_START_APP', cls='explicit', evidence='SRC receiver/SchedulerReceiver.java:44-62,65-82')
e('SchedulerReceiver.onReceive', 'SchedulerReceiver.onStopApp', 'CALL', 'Handle scheduled stop-app alarm',
  guard='intent.getAction() == SCHEDULER_WORK_STOP_APP', cls='explicit', evidence='SRC receiver/SchedulerReceiver.java:44-62,84-103')
e('SchedulerReceiver.onStartApp', 'TorrentEngine.getInstance', 'CALL', 'Get engine for scheduled app start',
  guard='pref.enableSchedulingStart()', needs_state='pref.enableSchedulingStart()', cls='explicit', evidence='SRC receiver/SchedulerReceiver.java:65-82; core/model/TorrentEngine.java:117-125')
e('SchedulerReceiver.onStartApp', 'TorrentEngine.start', 'CALL', 'Start engine for scheduled app start',
  guard='pref.enableSchedulingStart()', needs_state='pref.enableSchedulingStart()', cls='explicit', evidence='SRC receiver/SchedulerReceiver.java:65-82; core/model/TorrentEngine.java:148-153')
e('SchedulerReceiver.onStopApp', 'TorrentEngine.getInstance', 'CALL', 'Get engine for scheduled shutdown',
  guard='pref.enableSchedulingShutdown()', needs_state='pref.enableSchedulingShutdown()', cls='explicit', evidence='SRC receiver/SchedulerReceiver.java:84-103; core/model/TorrentEngine.java:117-125')
e('SchedulerReceiver.onStopApp', 'TorrentEngine.forceStop', 'CALL', 'Stop engine for scheduled shutdown',
  guard='pref.enableSchedulingShutdown()', needs_state='pref.enableSchedulingShutdown()', cls='explicit', evidence='SRC receiver/SchedulerReceiver.java:84-103; core/model/TorrentEngine.java:282-286')
e('MainActivity.onCreate', 'MainActivity.cleanGarbageFragments', 'CALL', 'Remove stale tablet detail fragments during initialization',
  guard='getIntent().getAction() != NOTIFY_ACTION_SHUTDOWN_APP', cls='explicit', evidence='SRC ui/main/MainActivity.java:140-144,182-189; ui/main/MainActivity.java:640-650')
e('MainActivity.onCreate', 'MainActivity.initLayout', 'CALL', 'Initialize main screen and drawer layout',
  guard='getIntent().getAction() != NOTIFY_ACTION_SHUTDOWN_APP', cls='explicit', evidence='SRC ui/main/MainActivity.java:140-144,182-189; ui/main/MainActivity.java:191-228')
e('MainActivity.onCreate', 'Utils.showManageAllFilesWarningDialog', 'CALL', 'Show the managed-storage notice when platform and preference conditions allow',
  guard='getIntent().getAction() != NOTIFY_ACTION_SHUTDOWN_APP', cls='explicit', evidence='SRC ui/main/MainActivity.java:140-144,177-182; core/utils/Utils.java:699-723')
e('MainActivity.initLayout', 'MainActivity.showBlankFragment', 'CALL', 'Show empty detail pane in two-pane layout',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:191-228; ui/main/MainActivity.java:676-685')
e('MainActivity.initLayout', 'MainActivity.initDrawer', 'CALL', 'Initialize navigation drawer and tag controls',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:191-228; ui/main/MainActivity.java:230-293')
e('MainActivity.initLayout', 'MainViewModel.resetSearch', 'CALL', 'Reset search during main layout initialization',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:227; ui/main/MainViewModel.java:130-132')
e('MainActivity.initDrawer', 'DrawerExpandableAdapter.<init>', 'CALL', 'Create drawer group adapter',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:248-252')
e('MainActivity.initDrawer', 'MainActivity.onDrawerGroupsCreated', 'CALL', 'Apply initial drawer group settings',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:248-252; ui/main/MainActivity.java:582-601')
e('MainActivity.initDrawer', 'drawer.TagsAdapter.<init>', 'CALL', 'Create tag drawer adapter',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:270-273')
e('MainActivity.initDrawer', 'MainActivity.onDrawerItemSelected', 'REGISTER', 'Pass the drawer selection callback to the app-owned adapter',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:248-252; ui/main/drawer/DrawerExpandableAdapter.java:56-65')
e('MainActivity.initDrawer', 'DrawerExpandableAdapter.onBindChildViewHolder', 'FRAMEWORK', 'Bind drawer child rows through the configured RecyclerView adapter',
  cls='non_standard', via='AndroidX RecyclerView adapter binding', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/main/MainActivity.java:264-268; ui/main/drawer/DrawerExpandableAdapter.java:85-123')
e('DrawerExpandableAdapter.onBindChildViewHolder', 'DrawerExpandableAdapter.lambda$onBindChildViewHolder$0', 'REGISTER', 'Register the child-row click listener',
  cls='standard', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:108-123; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('DrawerExpandableAdapter.onBindChildViewHolder', 'DrawerExpandableAdapter.lambda$onBindChildViewHolder$0', 'FRAMEWORK', 'Dispatch a drawer child-row click to its registered listener',
  cls='standard', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:108-123; FW-SRC core/java/android/view/View.java:6289-6305')
e('DrawerExpandableAdapter.lambda$onBindChildViewHolder$0', 'MainActivity.onDrawerItemSelected', 'CALL', 'Send the selected drawer item to the activity callback',
  guard='group item is not already selected', cls='explicit', evidence='SRC ui/main/drawer/DrawerExpandableAdapter.java:118-123; ui/main/MainActivity.java:248-252,610-631')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$2', 'REGISTER', 'Register add-tag button click callback',
  cls='standard', evidence='SRC ui/main/MainActivity.java:273-275; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$2', 'FRAMEWORK', 'Dispatch a click on the add-tag button',
  cls='standard', evidence='SRC ui/main/MainActivity.java:273-275; FW-SRC core/java/android/view/View.java:6289-6305')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$3', 'REGISTER', 'Register tag section header click callback',
  cls='standard', evidence='SRC ui/main/MainActivity.java:282-292; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$3', 'FRAMEWORK', 'Dispatch clicks on the tag section header',
  cls='standard', evidence='SRC ui/main/MainActivity.java:282-292; FW-SRC core/java/android/view/View.java:6289-6305')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$0', 'REGISTER', 'Register drawer group collapse persistence callback',
  cls='non_standard', via='ExpandableItemManager group listener', evidence='INFERRED expandable adapter listener dispatch; SRC ui/main/MainActivity.java:230-241')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$0', 'FRAMEWORK', 'Persist group state after a user collapse',
  guard='fromUser == true', cls='non_standard', via='ExpandableItemManager group listener', evidence='INFERRED expandable adapter listener dispatch; SRC ui/main/MainActivity.java:233-236')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$1', 'REGISTER', 'Register drawer group expand persistence callback',
  cls='non_standard', via='ExpandableItemManager group listener', evidence='INFERRED expandable adapter listener dispatch; SRC ui/main/MainActivity.java:230-241')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$1', 'FRAMEWORK', 'Persist group state after a user expansion',
  guard='fromUser == true', cls='non_standard', via='ExpandableItemManager group listener', evidence='INFERRED expandable adapter listener dispatch; SRC ui/main/MainActivity.java:237-240')
e('MainActivity.lambda$initDrawer$0', 'MainActivity.saveGroupExpandState', 'CALL', 'Save collapse state for a user action',
  guard='fromUser == true', cls='explicit', evidence='SRC ui/main/MainActivity.java:233-236; ui/main/MainActivity.java:559-582')
e('MainActivity.lambda$initDrawer$1', 'MainActivity.saveGroupExpandState', 'CALL', 'Save expansion state for a user action',
  guard='fromUser == true', cls='explicit', evidence='SRC ui/main/MainActivity.java:237-240; ui/main/MainActivity.java:559-582')
e('MainActivity.lambda$initDrawer$2', 'AddTagActivity.<init>', 'INTENT', 'Open AddTagActivity after add-tag button click',
  cls='standard', evidence='SRC ui/main/MainActivity.java:273-275; AndroidManifest.xml:245-251; FW-SRC core/java/android/app/ActivityThread.java:2665-2671,2727-2732; core/java/android/app/Instrumentation.java:1170-1175,1212-1215')
e('MainActivity.lambda$initDrawer$2', 'AddTagActivity.onCreate', 'INTENT', 'Create AddTagActivity after add-tag button click',
  cls='standard', evidence='SRC ui/main/MainActivity.java:273-275; AndroidManifest.xml:245-251; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('MainActivity$3.onTagMenuClicked', 'MainActivity$3.lambda$onTagMenuClicked$0', 'REGISTER', 'Reset drawer selection after deleting the selected tag',
  guard='abstractItem instanceof TagItem && menuId == R.id.delete_tag_menu', cls='non_standard', via='RxJava Completable success callback', evidence='INFERRED RxJava Completable callback dispatch; SRC ui/main/MainActivity.java:316-347')
e('MainActivity$3.onTagMenuClicked', 'MainActivity$3.lambda$onTagMenuClicked$0', 'FRAMEWORK', 'Deliver successful tag deletion to the drawer update callback',
  guard='abstractItem instanceof TagItem && menuId == R.id.delete_tag_menu', cls='non_standard', via='RxJava Completable success callback', evidence='INFERRED RxJava Completable completion dispatch; SRC ui/main/MainActivity.java:325-347')
e('MainActivity$3.onTagMenuClicked', 'MainActivity$3.lambda$onTagMenuClicked$1', 'REGISTER', 'Show an error when tag deletion fails',
  guard='abstractItem instanceof TagItem && menuId == R.id.delete_tag_menu', cls='non_standard', via='RxJava Completable error callback', evidence='INFERRED RxJava Completable error dispatch; SRC ui/main/MainActivity.java:325-347')
e('MainActivity$3.onTagMenuClicked', 'MainActivity$3.lambda$onTagMenuClicked$1', 'FRAMEWORK', 'Deliver tag deletion failures to the error callback',
  guard='abstractItem instanceof TagItem && menuId == R.id.delete_tag_menu', cls='non_standard', via='RxJava Completable error callback', evidence='INFERRED RxJava Completable error dispatch; SRC ui/main/MainActivity.java:325-347')
e('MainActivity$3.onTagMenuClicked', 'AddTagActivity.<init>', 'INTENT', 'Open AddTagActivity to edit a stored tag',
  guard='abstractItem instanceof TagItem && menuId == R.id.edit_tag_menu', cls='standard', evidence='SRC ui/main/MainActivity.java:316-324; AndroidManifest.xml:245-251; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('MainActivity$3.onTagMenuClicked', 'AddTagActivity.onCreate', 'INTENT', 'Create AddTagActivity with the selected tag as initial data',
  guard='abstractItem instanceof TagItem && menuId == R.id.edit_tag_menu', cls='standard', evidence='SRC ui/main/MainActivity.java:316-324; AndroidManifest.xml:245-251; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('MainActivity$3.lambda$onTagMenuClicked$0', 'drawer.TagsAdapter.getSelectedItem', 'CALL', 'Check whether the deleted tag was selected',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:330-336')
e('MainActivity$3.lambda$onTagMenuClicked$0', 'MainActivity.saveSelectedTag', 'CALL', 'Persist the all-torrents selection after deleting the selected tag',
  guard='item.isSame(tagsAdapter.getSelectedItem())', cls='explicit', evidence='SRC ui/main/MainActivity.java:330-336')
e('MainActivity$3.lambda$onTagMenuClicked$0', 'drawer.TagsAdapter.setSelectedItem', 'CALL', 'Select the all-torrents row after deleting the selected tag',
  guard='item.isSame(tagsAdapter.getSelectedItem())', cls='explicit', evidence='SRC ui/main/MainActivity.java:330-336')
e('MainActivity$3.lambda$onTagMenuClicked$0', 'MainViewModel.setTagFilter', 'CALL', 'Reset the torrent filter after deleting the selected tag',
  guard='item.isSame(tagsAdapter.getSelectedItem())', cls='explicit', evidence='SRC ui/main/MainActivity.java:330-336')
e('MainActivity.onDrawerItemSelected', 'MainViewModel.setTagFilter', 'CALL', 'Apply selected tag filter',
  guard='item instanceof TagItem or EmptyTagItem or NoTagsItem', cls='explicit', evidence='SRC ui/main/MainActivity.java:297-309')
e('MainActivity.onDrawerItemSelected', 'MainActivity.saveSelectedTag', 'CALL', 'Persist selected drawer tag',
  guard='item instanceof TagItem or EmptyTagItem or NoTagsItem', cls='explicit', evidence='SRC ui/main/MainActivity.java:297-310; ui/main/MainActivity.java:352-369')
e('MainActivity.onDrawerItemSelected', 'MainViewModel.setStatusFilter', 'CALL', 'Apply selected status filter',
  guard='group.id == drawer_status_id', cls='explicit', evidence='SRC ui/main/MainActivity.java:610-624')
e('MainActivity.onDrawerItemSelected', 'MainViewModel.setSort', 'CALL', 'Apply selected sorting mode',
  guard='group.id == drawer_sorting_id', cls='explicit', evidence='SRC ui/main/MainActivity.java:610-624')
e('MainActivity.onDrawerItemSelected', 'MainViewModel.setDateAddedFilter', 'CALL', 'Apply selected added-date filter',
  guard='group.id == drawer_date_added_id', cls='explicit', evidence='SRC ui/main/MainActivity.java:610-624')
e('MainActivity.onDrawerItemSelected', 'MainActivity.saveSelectionState', 'CALL', 'Save selected drawer group item',
  guard='prefKey != null', cls='explicit', evidence='SRC ui/main/MainActivity.java:626-637')
e('MainActivity.onStart', 'MainActivity.onCreateOptionsMenu', 'FRAMEWORK', 'Prepare toolbar menu through the AppCompat action bar',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu callback dispatch; SRC ui/main/MainActivity.java:214-216,697-705')
e('MainActivity.onCreateOptionsMenu', 'MainActivity.initSearch', 'CALL', 'Initialize search menu item',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:698-705; ui/main/MainActivity.java:707-735')
e('MainActivity.onCreateOptionsMenu', 'MainActivity.onOptionsItemSelected', 'REGISTER', 'Register toolbar menu item selection callback',
  cls='non_standard', via='AndroidX AppCompat Toolbar', evidence='INFERRED AppCompat Toolbar menu callback dispatch; SRC ui/main/MainActivity.java:698-705,738-758')
e('MainActivity.onCreateOptionsMenu', 'MainActivity.onOptionsItemSelected', 'FRAMEWORK', 'Dispatch selected toolbar menu actions through AppCompat',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu callback dispatch; SRC ui/main/MainActivity.java:698-705,738-758')
e('MainActivity.onOptionsItemSelected', 'FeedActivity.<init>', 'INTENT', 'Open feeds screen from the toolbar menu',
  guard='itemId == R.id.feed_menu', cls='standard', evidence='SRC ui/main/MainActivity.java:738-758; AndroidManifest.xml:174-175; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('MainActivity.onOptionsItemSelected', 'FeedActivity.onCreate', 'INTENT', 'Create feeds screen from the toolbar menu',
  guard='itemId == R.id.feed_menu', cls='standard', evidence='SRC ui/main/MainActivity.java:738-758; AndroidManifest.xml:174-175; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('MainActivity.onOptionsItemSelected', 'SettingsActivity.<init>', 'INTENT', 'Open settings screen from the toolbar menu',
  guard='itemId == R.id.settings_menu', cls='standard', evidence='SRC ui/main/MainActivity.java:738-758; AndroidManifest.xml:155-162; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('MainActivity.onOptionsItemSelected', 'SettingsActivity.onCreate', 'INTENT', 'Create settings screen from the toolbar menu',
  guard='itemId == R.id.settings_menu', cls='standard', evidence='SRC ui/main/MainActivity.java:738-758; AndroidManifest.xml:155-162; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('MainActivity.onOptionsItemSelected', 'MainActivity.showAboutDialog', 'CALL', 'Show about dialog from the toolbar menu',
  guard='itemId == R.id.about_menu', cls='explicit', evidence='SRC ui/main/MainActivity.java:738-758; ui/main/MainActivity.java:761-774')
e('MainActivity.onOptionsItemSelected', 'MainViewModel.stopEngine', 'CALL', 'Stop engine from shutdown menu action',
  guard='itemId == R.id.shutdown_app_menu', cls='explicit', evidence='SRC ui/main/MainActivity.java:746-750')
e('MainActivity.onOptionsItemSelected', 'MainViewModel.pauseAll', 'CALL', 'Pause all torrents from toolbar menu',
  guard='itemId == R.id.pause_all_menu', cls='explicit', evidence='SRC ui/main/MainActivity.java:750-752')
e('MainActivity.onOptionsItemSelected', 'MainViewModel.resumeAll', 'CALL', 'Resume all torrents from toolbar menu',
  guard='itemId == R.id.resume_all_menu', cls='explicit', evidence='SRC ui/main/MainActivity.java:752-754')
e('MainActivity.onOptionsItemSelected', 'MainActivity.showLog', 'CALL', 'Open session log from toolbar menu',
  guard='itemId == R.id.log_menu', cls='explicit', evidence='SRC ui/main/MainActivity.java:754-758; ui/main/MainActivity.java:801-804')
e('MainActivity.showLog', 'LogActivity.<init>', 'INTENT', 'Open session log screen',
  cls='standard', evidence='SRC ui/main/MainActivity.java:801-804; AndroidManifest.xml:239-240; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('MainActivity.showLog', 'LogActivity.onCreate', 'INTENT', 'Create session log screen',
  cls='standard', evidence='SRC ui/main/MainActivity.java:801-804; AndroidManifest.xml:239-240; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('LogActivity.onCreate', 'LogActivity.onStart', 'LIFECYCLE', 'Start log screen after activity creation',
  cls='standard', evidence='FW-SRC core/java/android/app/ActivityThread.java:2727-2762; core/java/android/app/Instrumentation.java:1284-1286; SRC ui/log/LogActivity.java:76-80,167-173')
e('LogActivity.onStart', 'LogActivity.onStop', 'LIFECYCLE', 'Stop log screen when it leaves the foreground',
  cls='standard', evidence='FW-SRC core/java/android/app/ActivityThread.java:4029-4041; core/java/android/app/Instrumentation.java:1232-1250; SRC ui/log/LogActivity.java:158-173')
e('LogActivity.onStop', 'LogActivity.onDestroy', 'LIFECYCLE', 'Destroy log screen when the stopped activity is finishing',
  guard='activity is finishing', cls='standard', evidence='FW-SRC core/java/android/app/ActivityThread.java:4368-4377; core/java/android/app/Instrumentation.java:1374-1376; SRC ui/log/LogActivity.java:149-165')
e('LogActivity.onDestroy', 'LogActivity.resumeLog', 'CALL', 'Resume live logging as the activity is destroyed',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:149-156')
e('LogActivity.onCreate', 'LogActivity.updateToolbarSubtitle', 'CALL', 'Set the initial log-count subtitle',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:96-103,450-455')
e('LogActivity.onCreate', 'LogAdapter.<init>', 'CALL', 'Create the log list adapter',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:116-120')
e('LogActivity.onCreate', 'LogViewModel.observeLog', 'CALL', 'Observe the paged log entries',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:119-120')
e('LogActivity.onCreate', 'LogActivity.lambda$onCreate$1', 'REGISTER', 'Observe log entries and submit changed pages to the adapter',
  cls='non_standard', via='AndroidX LiveData observer', evidence='INFERRED AndroidX LiveData observer dispatch; SRC ui/log/LogActivity.java:119-120')
e('LogActivity.lambda$onCreate$1', 'LogActivity.lambda$new$7', 'REGISTER', 'Update scroll position and subtitle after the adapter applies a page',
  cls='non_standard', via='AndroidX PagedListAdapter commit callback', evidence='INFERRED AndroidX PagedListAdapter callback dispatch; SRC ui/log/LogActivity.java:119-120,438-441')
e('LogActivity.lambda$onCreate$1', 'LogActivity.lambda$new$7', 'FRAMEWORK', 'Invoke the adapter commit callback after a log page is applied',
  cls='non_standard', via='AndroidX PagedListAdapter commit callback', evidence='INFERRED AndroidX PagedListAdapter callback dispatch; SRC ui/log/LogActivity.java:119-120,438-441')
e('LogActivity.onCreate', 'LogActivity.lambda$onCreate$1', 'FRAMEWORK', 'Deliver paged log updates to the registered LiveData observer',
  cls='non_standard', via='AndroidX LiveData observer', evidence='INFERRED AndroidX LiveData observer dispatch; SRC ui/log/LogActivity.java:119-120')
e('LogActivity.lambda$new$7', 'LogActivity.scrollLogList', 'CALL', 'Restore or follow the current log list position',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:412-420,448-455')
e('LogActivity.lambda$new$7', 'LogActivity.updateToolbarSubtitle', 'CALL', 'Refresh log count after the list changes',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:412-420,448-455')
e('LogActivity.onCreate', 'LogActivity$2.onScrolled', 'REGISTER', 'Register scroll direction handling for the log list',
  cls='non_standard', via='AndroidX RecyclerView', evidence='INFERRED RecyclerView listener dispatch; SRC ui/log/LogActivity.java:122,295-312')
e('LogActivity.onCreate', 'LogActivity$2.onScrolled', 'FRAMEWORK', 'Dispatch visible log list scroll changes',
  cls='non_standard', via='AndroidX RecyclerView', evidence='INFERRED RecyclerView listener dispatch; SRC ui/log/LogActivity.java:122,338-356')
e('LogActivity.onCreate', 'LogActivity$2.onScrollStateChanged', 'REGISTER', 'Register scroll-state handling for the log list',
  cls='non_standard', via='AndroidX RecyclerView', evidence='INFERRED RecyclerView listener dispatch; SRC ui/log/LogActivity.java:122,314-365')
e('LogActivity.onCreate', 'LogActivity$2.onScrollStateChanged', 'FRAMEWORK', 'Dispatch log list scroll-state changes',
  cls='non_standard', via='AndroidX RecyclerView', evidence='INFERRED RecyclerView listener dispatch; SRC ui/log/LogActivity.java:122,358-405')
e('LogActivity.onCreate', 'LogActivity.lambda$onCreate$0', 'REGISTER', 'Register toolbar navigation click handling',
  cls='standard', via='android.view.View.OnClickListener', evidence='SRC ui/log/LogActivity.java:96-101; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('LogActivity.onCreate', 'LogActivity.lambda$onCreate$0', 'FRAMEWORK', 'Dispatch toolbar navigation clicks',
  cls='standard', via='android.view.View.OnClickListener', evidence='SRC ui/log/LogActivity.java:96-101; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('LogActivity.onCreate', 'LogActivity.lambda$onCreate$2', 'REGISTER', 'Register the jump-to-oldest-log button callback',
  cls='standard', via='android.view.View.OnClickListener', evidence='SRC ui/log/LogActivity.java:124-132; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('LogActivity.onCreate', 'LogActivity.lambda$onCreate$2', 'FRAMEWORK', 'Dispatch taps on the jump-to-oldest-log button',
  cls='standard', via='android.view.View.OnClickListener', evidence='SRC ui/log/LogActivity.java:124-132; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('LogActivity.onCreate', 'LogActivity.lambda$onCreate$3', 'REGISTER', 'Register the jump-to-newest-log button callback',
  cls='standard', via='android.view.View.OnClickListener', evidence='SRC ui/log/LogActivity.java:134-143; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('LogActivity.onCreate', 'LogActivity.lambda$onCreate$3', 'FRAMEWORK', 'Dispatch taps on the jump-to-newest-log button',
  cls='standard', via='android.view.View.OnClickListener', evidence='SRC ui/log/LogActivity.java:134-143; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('LogActivity.onCreate', 'LogAdapter.onBindViewHolder', 'FRAMEWORK', 'Bind visible log rows through RecyclerView',
  needs_state='adapter.getItemCount() > 0', cls='non_standard', via='AndroidX RecyclerView.Adapter', evidence='INFERRED AndroidX RecyclerView binding dispatch; SRC ui/log/LogActivity.java:116-120; ui/log/LogAdapter.java:59-65')
e('LogActivity.onCreate', 'LogAdapter.onCreateViewHolder', 'FRAMEWORK', 'Create a row view holder when the log list has entries',
  needs_state='adapter.getItemCount() > 0', cls='non_standard', via='AndroidX RecyclerView.Adapter', evidence='INFERRED AndroidX RecyclerView row creation dispatch; SRC ui/log/LogActivity.java:116-120; ui/log/LogAdapter.java:46-57')
e('LogAdapter.onBindViewHolder', 'LogAdapter$ViewHolder.bind', 'CALL', 'Bind log entry text and row click listener',
  guard='getItem(position) != null', cls='explicit', evidence='SRC ui/log/LogAdapter.java:59-65,100-110')
e('LogAdapter$ViewHolder.bind', 'LogAdapter$ViewHolder.lambda$bind$0', 'REGISTER', 'Register a click callback for the log row',
  cls='standard', evidence='SRC ui/log/LogAdapter.java:100-105; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('LogAdapter$ViewHolder.bind', 'LogAdapter$ViewHolder.lambda$bind$0', 'FRAMEWORK', 'Dispatch taps on a log row',
  cls='standard', evidence='SRC ui/log/LogAdapter.java:100-105; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('LogAdapter$ViewHolder.lambda$bind$0', 'LogActivity.onItemClicked', 'CALL', 'Copy the clicked log entry through the activity listener',
  guard='listener != null', cls='explicit', evidence='SRC ui/log/LogAdapter.java:39-44,100-105; ui/log/LogActivity.java:460-469')
e('LogActivity.onItemClicked', 'LogViewModel.copyLogEntryToClipboard', 'CALL', 'Copy the selected log entry to the clipboard',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:460-468')
e('LogActivity.lambda$onCreate$2', 'LogActivity.hideFabUp', 'CALL', 'Hide the jump-to-oldest button before moving to the newest entry',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:124-132,383-388')
e('LogActivity.lambda$onCreate$2', 'LogActivity.resumeLog', 'CALL', 'Resume log collection after repositioning the list',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:124-132,276-280')
e('LogActivity.lambda$onCreate$3', 'LogActivity.hideFabUp', 'CALL', 'Hide the jump-to-oldest button before moving to the newest entry',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:134-143,383-388')
e('LogActivity.lambda$onCreate$3', 'LogActivity.resumeLog', 'CALL', 'Resume log collection after repositioning the list',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:134-143,276-280')
e('LogActivity.onCreate', 'LogActivity.hideFabUp', 'CALL', 'Initialize the jump-to-oldest button as hidden',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:145-146,383-388')
e('LogActivity.onCreate', 'LogActivity.hideFabDown', 'CALL', 'Initialize the jump-to-newest button as hidden',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:145-146,390-395')
e('LogActivity.showFabUp', 'LogActivity.lambda$new$5', 'FRAMEWORK', 'Hide the jump-to-oldest button after its delayed timeout',
  cls='standard', evidence='SRC ui/log/LogActivity.java:408-413,434-436; FW-SRC core/java/android/os/Handler.java:97-107,427-429,789')
e('LogActivity.showFabDown', 'LogActivity.lambda$new$6', 'FRAMEWORK', 'Hide the jump-to-newest button after its delayed timeout',
  cls='standard', evidence='SRC ui/log/LogActivity.java:421-426,434-436; FW-SRC core/java/android/os/Handler.java:97-107,427-429,789')
e('LogActivity.onCreate', 'LogActivity.onCreateOptionsMenu', 'FRAMEWORK', 'Inflate the log toolbar menu through the AppCompat action bar',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu callback dispatch; SRC ui/log/LogActivity.java:57-58,194-200')
e('LogActivity.onCreateOptionsMenu', 'LogActivity.onPrepareOptionsMenu', 'FRAMEWORK', 'Prepare log menu visibility and action labels',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu preparation dispatch; SRC ui/log/LogActivity.java:194-228')
e('LogActivity.onCreateOptionsMenu', 'LogActivity.onOptionsItemSelected', 'REGISTER', 'Register log toolbar menu selection handling',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu callback dispatch; SRC ui/log/LogActivity.java:194-200,231-248')
e('LogActivity.onCreateOptionsMenu', 'LogActivity.onOptionsItemSelected', 'FRAMEWORK', 'Dispatch selected log toolbar actions through AppCompat',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu callback dispatch; SRC ui/log/LogActivity.java:194-200,231-248')
e('LogActivity.onOptionsItemSelected', 'LogActivity.pauseResumeLog', 'CALL', 'Pause or resume live log updates from the toolbar',
  guard='itemId == R.id.pause_resume_log_menu', cls='explicit', evidence='SRC ui/log/LogActivity.java:231-247,266-274')
e('LogActivity.onOptionsItemSelected', 'LogActivity.toggleRecord', 'CALL', 'Start or stop recording from the toolbar',
  guard='itemId == R.id.record_log_menu', cls='explicit', evidence='SRC ui/log/LogActivity.java:231-247,282-309')
e('LogActivity.onOptionsItemSelected', 'LogActivity.saveLogPathChooseDialog', 'CALL', 'Choose an output file from the toolbar',
  guard='itemId == R.id.save_log_menu', cls='explicit', evidence='SRC ui/log/LogActivity.java:231-247,311-326')
e('LogActivity.onOptionsItemSelected', 'LogActivity.showFilterDialog', 'CALL', 'Open log filters from the toolbar',
  guard='itemId == R.id.filter_log_menu', cls='explicit', evidence='SRC ui/log/LogActivity.java:231-247,250-259')
e('LogActivity.onOptionsItemSelected', 'LogActivity.showLogSettings', 'CALL', 'Open log settings from the toolbar',
  guard='itemId == R.id.log_settings_menu', cls='explicit', evidence='SRC ui/log/LogActivity.java:231-247,261-264')
e('LogActivity.pauseResumeLog', 'LogViewModel.logPausedManually', 'CALL', 'Read manual pause state before toggling log updates',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:264-273')
e('LogActivity.pauseResumeLog', 'LogViewModel.pauseLogManually', 'CALL', 'Pause log updates when currently running',
  guard='!viewModel.logPausedManually()', cls='explicit', evidence='SRC ui/log/LogActivity.java:264-273')
e('LogActivity.pauseResumeLog', 'LogViewModel.resumeLogManually', 'CALL', 'Resume log updates when manually paused',
  guard='viewModel.logPausedManually()', cls='explicit', evidence='SRC ui/log/LogActivity.java:264-273')
e('LogActivity.resumeLog', 'LogViewModel.logPausedManually', 'CALL', 'Check manual pause state before resuming collection',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:275-279')
e('LogActivity.resumeLog', 'LogViewModel.resumeLog', 'CALL', 'Resume log collection unless manually paused',
  guard='!viewModel.logPausedManually()', cls='explicit', evidence='SRC ui/log/LogActivity.java:275-279')
e('LogActivity.toggleRecord', 'LogViewModel.logRecording', 'CALL', 'Read recording state before toggling',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:281-302')
e('LogActivity.toggleRecord', 'LogViewModel.logPausedManually', 'CALL', 'Check whether starting a recording is allowed',
  guard='recording', cls='explicit', evidence='SRC ui/log/LogActivity.java:283-286')
e('LogActivity.toggleRecord', 'LogViewModel.startLogRecording', 'CALL', 'Start a log recording when recording is enabled and updates are not paused',
  guard='recording && !viewModel.logPausedManually()', cls='explicit', evidence='SRC ui/log/LogActivity.java:283-297')
e('LogActivity.toggleRecord', 'LogViewModel.pauseLog', 'CALL', 'Pause live log updates before saving a recording',
  guard='!recording', cls='explicit', evidence='SRC ui/log/LogActivity.java:298-301')
e('LogActivity.showLogSettings', 'LogSettingsActivity.<init>', 'INTENT', 'Open log settings screen',
  cls='standard', evidence='SRC ui/log/LogActivity.java:259-262; AndroidManifest.xml:241-242; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('LogActivity.showLogSettings', 'LogSettingsActivity.onCreate', 'INTENT', 'Create log settings screen',
  cls='standard', evidence='SRC ui/log/LogActivity.java:259-262; AndroidManifest.xml:241-242; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('LogActivity.saveLogPathChooseDialog', 'FileManagerDialog.<init>', 'INTENT', 'Launch the file manager to choose a log output path',
  cls='standard', evidence='SRC ui/log/LogActivity.java:304-316; AndroidManifest.xml:137; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('LogActivity.saveLogPathChooseDialog', 'FileManagerDialog.onCreate', 'INTENT', 'Create the file manager for log output selection',
  cls='standard', evidence='SRC ui/log/LogActivity.java:304-316; AndroidManifest.xml:137; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('LogActivity.saveLogPathChooseDialog', 'LogViewModel.getSaveLogFileName', 'CALL', 'Use the generated log filename as the file manager suggestion',
  cls='explicit', evidence='SRC ui/log/LogActivity.java:304-315')
e('LogActivity.<init>', 'LogActivity.lambda$new$4', 'REGISTER', 'Register the callback for the log output file picker result',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher registration; SRC ui/log/LogActivity.java:73-74,318-336')
e('LogActivity.saveLogPathChooseDialog', 'LogActivity.lambda$new$4', 'RESULT', 'Deliver the file picker result to log save handling',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher result dispatch; SRC ui/log/LogActivity.java:304-336')
e('LogActivity.lambda$new$4', 'LogViewModel.saveLog', 'CALL', 'Save the recording when the file manager returns a valid path',
  guard='result.getResultCode() == RESULT_OK && data != null && data.getData() != null', cls='explicit', evidence='SRC ui/log/LogActivity.java:320-328')
e('LogActivity.lambda$new$4', 'LogViewModel.stopLogRecording', 'CALL', 'Stop recording when file selection is canceled or invalid',
  guard='result.getResultCode() != RESULT_OK || data == null', cls='explicit', evidence='SRC ui/log/LogActivity.java:320-334')
e('LogActivity.showFilterDialog', 'SessionLogFilterDialog.newInstance', 'CALL', 'Create the log filter dialog if one is not already shown',
  guard='fm.findFragmentByTag(TAG_FILTER_DIALOG) == null', cls='explicit', evidence='SRC ui/log/LogActivity.java:250-257')
e('SessionLogFilterDialog.newInstance', 'SessionLogFilterDialog.<init>', 'CALL', 'Instantiate the log filter dialog fragment',
  cls='explicit', evidence='SRC ui/log/SessionLogFilterDialog.java:49-56')
e('SessionLogFilterDialog.newInstance', 'SessionLogFilterDialog.onAttach', 'LIFECYCLE', 'Attach the filter dialog when FragmentManager shows it',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/log/LogActivity.java:250-257; ui/log/SessionLogFilterDialog.java:49-66')
e('SessionLogFilterDialog.onAttach', 'SessionLogFilterDialog.onCreateDialog', 'LIFECYCLE', 'Create filter dialog after attachment',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/log/SessionLogFilterDialog.java:59-66,90-104')
e('SessionLogFilterDialog.onCreateDialog', 'SessionLogFilterDialog.initLayoutView', 'CALL', 'Create the filter dialog buttons and content view',
  cls='explicit', evidence='SRC ui/log/SessionLogFilterDialog.java:97-114')
e('SessionLogFilterDialog.initLayoutView', 'SessionLogFilterDialog.lambda$initLayoutView$1', 'REGISTER', 'Register the filter dialog cancel button',
  cls='non_standard', via='AndroidX AlertDialog', evidence='INFERRED AndroidX AlertDialog button dispatch; SRC ui/log/SessionLogFilterDialog.java:106-114')
e('SessionLogFilterDialog.initLayoutView', 'SessionLogFilterDialog.lambda$initLayoutView$1', 'FRAMEWORK', 'Dispatch the filter dialog cancel button',
  cls='non_standard', via='AndroidX AlertDialog', evidence='INFERRED AndroidX AlertDialog button dispatch; SRC ui/log/SessionLogFilterDialog.java:106-114')
e('SessionLogFilterDialog.lambda$initLayoutView$1', 'SessionLogFilterDialog.onBackPressed', 'CALL', 'Dismiss filter dialog when cancel is selected',
  cls='explicit', evidence='SRC ui/log/SessionLogFilterDialog.java:108-114,116-119')
e('SessionLogFilterDialog.onCreateDialog', 'SessionLogFilterDialog.onResume', 'LIFECYCLE', 'Resume dialog after creation',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/log/SessionLogFilterDialog.java:68-86,90-104')
e('SessionLogFilterDialog.onResume', 'SessionLogFilterDialog.lambda$onResume$0', 'REGISTER', 'Register dialog back-key handling',
  cls='standard', evidence='SRC ui/log/SessionLogFilterDialog.java:68-86; FW-SRC core/java/android/app/Dialog.java:1346-1348,775-778')
e('SessionLogFilterDialog.onResume', 'SessionLogFilterDialog.lambda$onResume$0', 'FRAMEWORK', 'Dispatch dialog key events to the registered key listener',
  cls='standard', evidence='SRC ui/log/SessionLogFilterDialog.java:68-86; FW-SRC core/java/android/app/Dialog.java:1346-1348,775-778')
e('SessionLogFilterDialog.lambda$onResume$0', 'SessionLogFilterDialog.onBackPressed', 'CALL', 'Dismiss filter dialog when back is pressed',
  guard='keyCode == KeyEvent.KEYCODE_BACK && event.getAction() == KeyEvent.ACTION_DOWN', cls='explicit', evidence='SRC ui/log/SessionLogFilterDialog.java:74-85,116-119; FW-SRC core/java/android/app/Dialog.java:775-778')
e('LogSettingsActivity.onCreate', 'LogSettingsFragment.<init>', 'FRAMEWORK', 'Inflate log preferences fragment from the activity layout',
  cls='non_standard', via='AndroidX FragmentContainerView', evidence='INFERRED AndroidX FragmentContainerView inflation; SRC ui/log/LogSettingsActivity.java:37-50; res/layout/activity_log_settings.xml:13-18')
e('LogSettingsActivity.onCreate', 'LogSettingsActivity.lambda$onCreate$0', 'REGISTER', 'Register the settings toolbar navigation callback',
  cls='standard', via='android.view.View.OnClickListener', evidence='SRC ui/log/LogSettingsActivity.java:44-49; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('LogSettingsActivity.onCreate', 'LogSettingsActivity.lambda$onCreate$0', 'FRAMEWORK', 'Dispatch settings toolbar navigation clicks',
  cls='standard', via='android.view.View.OnClickListener', evidence='SRC ui/log/LogSettingsActivity.java:44-49; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('LogSettingsFragment.<init>', 'LogSettingsFragment.onCreate', 'LIFECYCLE', 'Create log settings fragment after layout inflation',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/log/LogSettingsFragment.java:36-58')
e('LogSettingsFragment.onCreate', 'LogSettingsFragment.onCreatePreferences', 'FRAMEWORK', 'Load the log preferences screen',
  cls='non_standard', via='AndroidX PreferenceFragmentCompat', evidence='INFERRED AndroidX PreferenceFragmentCompat callback dispatch; SRC ui/log/LogSettingsFragment.java:51-81')
e('LogSettingsFragment.onCreate', 'LogSettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'Register max-log-size preference change handling when the preference exists',
  guard='maxLogSize != null', cls='explicit', evidence='SRC ui/log/LogSettingsFragment.java:66-75,83-86')
e('LogSettingsFragment.onCreate', 'LogSettingsFragment.lambda$onCreate$0', 'REGISTER', 'Register the max-log-size editor input filter',
  guard='maxLogSize != null', cls='non_standard', via='AndroidX EditTextPreference', evidence='INFERRED AndroidX EditTextPreference edit-text binding dispatch; SRC ui/log/LogSettingsFragment.java:66-74')
e('LogSettingsFragment.onCreate', 'LogSettingsFragment.lambda$onCreate$0', 'FRAMEWORK', 'Apply the max-log-size input filter when the preference editor opens',
  guard='maxLogSize != null', cls='non_standard', via='AndroidX EditTextPreference', evidence='INFERRED AndroidX EditTextPreference edit-text binding dispatch; SRC ui/log/LogSettingsFragment.java:66-74')
e('LogSettingsFragment.bindOnPreferenceChangeListener', 'LogSettingsFragment.onPreferenceChange', 'REGISTER', 'Handle max-log-size preference edits',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/log/LogSettingsFragment.java:83-99')
e('LogSettingsFragment.bindOnPreferenceChangeListener', 'LogSettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Dispatch changed max-log-size preferences to the listener',
  guard='preference key is pref_key_max_log_size', cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/log/LogSettingsFragment.java:83-99')
e('ErrorReportActivity.onCreate', 'ErrorReportActivity.onStart', 'LIFECYCLE', 'Start error report screen after activity creation',
  cls='standard', evidence='FW-SRC core/java/android/app/ActivityThread.java:2738-2745; core/java/android/app/Instrumentation.java:1333-1335; SRC ui/errorreport/ErrorReportActivity.java:54-58,81-87')
e('ErrorReportActivity.onStart', 'ErrorReportActivity.onStop', 'LIFECYCLE', 'Stop error report screen when it leaves the foreground',
  cls='standard', evidence='FW-SRC core/java/android/app/ActivityThread.java:4029-4041; core/java/android/app/Instrumentation.java:1374-1376; SRC ui/errorreport/ErrorReportActivity.java:73-87')
e('ErrorReportActivity.onCreate', 'ErrorReportActivity.getStackTrace', 'CALL', 'Read the stack trace from the pending crash report',
  cls='explicit', evidence='SRC ui/errorreport/ErrorReportActivity.java:63-70,127-142')
e('ErrorReportActivity.onCreate', 'ErrorReportDialog.newInstance', 'CALL', 'Create the report dialog when no restored dialog exists',
  guard='errDialog == null', cls='explicit', evidence='SRC ui/errorreport/ErrorReportActivity.java:61-70; ui/errorreport/ErrorReportDialog.java:39-52')
e('ErrorReportDialog.newInstance', 'ErrorReportDialog.<init>', 'CALL', 'Instantiate the error report dialog fragment',
  cls='explicit', evidence='SRC ui/errorreport/ErrorReportDialog.java:39-51')
e('ErrorReportDialog.newInstance', 'ErrorReportDialog.onCreateDialog', 'LIFECYCLE', 'Create error report dialog after FragmentManager shows it',
  guard='errDialog == null', cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/errorreport/ErrorReportActivity.java:63-70; ui/errorreport/ErrorReportDialog.java:39-75')
e('ErrorReportDialog.onCreateDialog', 'BaseAlertDialog.onCreateDialog', 'CALL', 'Initialize the shared alert dialog ViewModel',
  cls='explicit', evidence='SRC ui/errorreport/ErrorReportDialog.java:54-60; ui/BaseAlertDialog.java:114-119')
e('ErrorReportDialog.onCreateDialog', 'ErrorReportDialog.initLayoutView', 'CALL', 'Set up expandable crash detail text',
  cls='explicit', evidence='SRC ui/errorreport/ErrorReportDialog.java:67-75,77-83')
e('ErrorReportDialog.onCreateDialog', 'BaseAlertDialog.buildDialog', 'CALL', 'Build report and cancel actions into the alert dialog',
  cls='explicit', evidence='SRC ui/errorreport/ErrorReportDialog.java:71-75; ui/BaseAlertDialog.java:143-197')
e('BaseAlertDialog.buildDialog', 'BaseAlertDialog.lambda$buildDialog$3', 'REGISTER', 'Register alert dialog shown handling',
  cls='standard', evidence='SRC ui/BaseAlertDialog.java:167-195; FW-SRC core/java/android/app/Dialog.java:1294')
e('BaseAlertDialog.buildDialog', 'BaseAlertDialog.lambda$buildDialog$3', 'FRAMEWORK', 'Run alert dialog shown handling after the dialog is displayed',
  cls='standard', evidence='SRC ui/BaseAlertDialog.java:167-195; FW-SRC core/java/android/app/Dialog.java:1367')
e('BaseAlertDialog.lambda$buildDialog$3', 'BaseAlertDialog.lambda$buildDialog$0', 'REGISTER', 'Register the positive button event callback',
  guard='positiveButton != null', cls='standard', evidence='SRC ui/BaseAlertDialog.java:168-177; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('BaseAlertDialog.lambda$buildDialog$3', 'BaseAlertDialog.lambda$buildDialog$1', 'REGISTER', 'Register the negative button event callback',
  guard='negativeButton != null', cls='standard', evidence='SRC ui/BaseAlertDialog.java:168-184; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('BaseAlertDialog.lambda$buildDialog$3', 'BaseAlertDialog.lambda$buildDialog$0', 'FRAMEWORK', 'Dispatch report submission button taps',
  guard='positiveButton != null', cls='standard', evidence='SRC ui/BaseAlertDialog.java:168-177; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('BaseAlertDialog.lambda$buildDialog$3', 'BaseAlertDialog.lambda$buildDialog$1', 'FRAMEWORK', 'Dispatch report cancellation button taps',
  guard='negativeButton != null', cls='standard', evidence='SRC ui/BaseAlertDialog.java:168-184; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('BaseAlertDialog.lambda$buildDialog$0', 'BaseAlertDialog$SharedViewModel.sendEvent', 'CALL', 'Publish positive button event to the shared dialog ViewModel',
  cls='explicit', evidence='SRC ui/BaseAlertDialog.java:172-177,65-68')
e('BaseAlertDialog.lambda$buildDialog$1', 'BaseAlertDialog$SharedViewModel.sendEvent', 'CALL', 'Publish negative button event to the shared dialog ViewModel',
  cls='explicit', evidence='SRC ui/BaseAlertDialog.java:179-184,65-68')
e('ErrorReportActivity.onStart', 'ErrorReportActivity.subscribeAlertDialog', 'CALL', 'Subscribe to report dialog button events while started',
  cls='explicit', evidence='SRC ui/errorreport/ErrorReportActivity.java:81-93')
e('ErrorReportActivity.subscribeAlertDialog', 'BaseAlertDialog$SharedViewModel.observeEvents', 'CALL', 'Observe shared alert dialog events',
  cls='explicit', evidence='SRC ui/errorreport/ErrorReportActivity.java:89-93; ui/BaseAlertDialog.java:56-63')
e('ErrorReportActivity.subscribeAlertDialog', 'ErrorReportActivity.handleAlertDialogEvent', 'REGISTER', 'Subscribe the activity event handler to dialog events',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/errorreport/ErrorReportActivity.java:89-93')
e('ErrorReportActivity.subscribeAlertDialog', 'ErrorReportActivity.handleAlertDialogEvent', 'FRAMEWORK', 'Deliver dialog events to the subscribed activity handler',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/errorreport/ErrorReportActivity.java:89-93')
e('ErrorReportActivity.handleAlertDialogEvent', 'ErrorReportActivity.finish', 'CALL', 'Close report flow after a successful submission',
  guard='event.dialogTag == TAG_ERROR_DIALOG && errDialog != null && event.type == POSITIVE_BUTTON_CLICKED && dialog != null', cls='explicit', evidence='SRC ui/errorreport/ErrorReportActivity.java:95-109')
e('ErrorReportActivity.handleAlertDialogEvent', 'ErrorReportActivity.finish', 'CALL', 'Close report flow after cancellation',
  guard='event.dialogTag == TAG_ERROR_DIALOG && errDialog != null && event.type == NEGATIVE_BUTTON_CLICKED', cls='explicit', evidence='SRC ui/errorreport/ErrorReportActivity.java:95-115')
e('ErrorReportDialog.initLayoutView', 'ErrorReportDialog.lambda$initLayoutView$0', 'REGISTER', 'Register the crash detail expander button',
  cls='standard', evidence='SRC ui/errorreport/ErrorReportDialog.java:77-83; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('ErrorReportDialog.initLayoutView', 'ErrorReportDialog.lambda$initLayoutView$0', 'FRAMEWORK', 'Dispatch taps on the crash detail expander',
  cls='standard', evidence='SRC ui/errorreport/ErrorReportDialog.java:77-83; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('CreateTorrentActivity.onCreate', 'CreateTorrentActivity.onStart', 'LIFECYCLE', 'Start Create Torrent after activity creation',
  cls='standard', evidence='FW-SRC core/java/android/app/ActivityThread.java:2738-2745; core/java/android/app/Instrumentation.java:1333-1335; SRC ui/createtorrent/CreateTorrentActivity.java:54-58,95-100')
e('CreateTorrentActivity.onStart', 'CreateTorrentActivity.onStop', 'LIFECYCLE', 'Stop Create Torrent when it leaves the foreground',
  cls='standard', evidence='FW-SRC core/java/android/app/ActivityThread.java:4029-4041; core/java/android/app/Instrumentation.java:1374-1376; SRC ui/createtorrent/CreateTorrentActivity.java:95-107')
e('CreateTorrentActivity.onCreate', 'CreateTorrentDialog.newInstance', 'CALL', 'Create the torrent builder dialog when it has not been restored',
  guard='createTorrentDialog == null', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:83-87; ui/createtorrent/CreateTorrentDialog.java:87-93')
e('CreateTorrentActivity.onCreate', 'PermissionManager.<init>', 'CALL', 'Set up runtime permission launchers for the activity',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:63-81; ui/PermissionManager.java:50-94')
e('CreateTorrentActivity.onCreate', 'CreateTorrentActivity$1.<init>', 'CALL', 'Create the activity callback passed to the permission manager',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:63-81')
e('CreateTorrentActivity.onCreate', 'PermissionManager.checkPermissions', 'CALL', 'Check permissions before requesting them',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:89-91; ui/PermissionManager.java:146-148')
e('CreateTorrentActivity.onCreate', 'PermissionManager.requestPermissions', 'CALL', 'Request missing permissions when the denied-dialog flow is not active',
  guard='!permissionManager.checkPermissions() && permDeniedDialog == null', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:89-91; ui/PermissionManager.java:96-114')
e('MainActivity.onCreate', 'MainActivity$1.<init>', 'CALL', 'Create the main screen permission-result callback',
  guard='getIntent().getAction() != NOTIFY_ACTION_SHUTDOWN_APP', cls='explicit', evidence='SRC ui/main/MainActivity.java:140-144,152-173')
e('MainActivity.onCreate', 'PermissionManager.<init>', 'CALL', 'Register main-screen runtime permission result launchers',
  guard='getIntent().getAction() != NOTIFY_ACTION_SHUTDOWN_APP', cls='explicit', evidence='SRC ui/main/MainActivity.java:140-144,152-173; ui/PermissionManager.java:50-94')
e('MainActivity.onCreate', 'PermissionManager.checkPermissions', 'CALL', 'Check storage and notification permissions before requesting them',
  guard='getIntent().getAction() != NOTIFY_ACTION_SHUTDOWN_APP', cls='explicit', evidence='SRC ui/main/MainActivity.java:140-144,152-180; ui/PermissionManager.java:146-148')
e('MainActivity.onCreate', 'PermissionManager.requestPermissions', 'CALL', 'Request permissions when the main-screen permission check fails and no denial dialog exists',
  guard='getIntent().getAction() != NOTIFY_ACTION_SHUTDOWN_APP && !permissionManager.checkPermissions() && permDeniedDialog == null', cls='explicit', evidence='SRC ui/main/MainActivity.java:140-144,152-180; ui/PermissionManager.java:96-114')
e('PermissionManager.<init>', 'PermissionManager.lambda$new$0', 'REGISTER', 'Register manage-all-files permission result handling on supported devices',
  guard='Build.VERSION.SDK_INT >= R && hasManageExternalStoragePermission', cls='non_standard', via='AndroidX Activity Result API', evidence='SRC ui/PermissionManager.java:60-68')
e('PermissionManager.<init>', 'PermissionManager.lambda$new$1', 'REGISTER', 'Register multiple runtime permission result handling',
  cls='non_standard', via='AndroidX Activity Result API', evidence='SRC ui/PermissionManager.java:70-94')
e('PermissionManager.requestPermissions', 'PermissionManager.lambda$new$0', 'RESULT', 'Deliver manage-all-files settings result to the registered callback',
  guard='Build.VERSION.SDK_INT >= R && !checkStoragePermissions() && pref.askManageAllFilesPermission()', cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/PermissionManager.java:96-114')
e('PermissionManager.requestPermissions', 'PermissionManager.lambda$new$1', 'RESULT', 'Deliver runtime permission results to the registered callback',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/PermissionManager.java:96-114')
e('PermissionManager.lambda$new$0', 'CreateTorrentActivity$1.onStorageResult', 'RESULT', 'Return manage-all-files permission result to the activity callback',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/PermissionManager.java:60-68; ui/createtorrent/CreateTorrentActivity.java:64-75')
e('PermissionManager.lambda$new$1', 'CreateTorrentActivity$1.onStorageResult', 'RESULT', 'Return storage permission result to the activity callback',
  guard='storageResult != null', cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/PermissionManager.java:70-85; ui/createtorrent/CreateTorrentActivity.java:64-75')
e('PermissionManager.lambda$new$1', 'CreateTorrentActivity$1.onNotificationResult', 'RESULT', 'Return notification permission result to the activity callback',
  guard='notificationsResult != null', cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/PermissionManager.java:75-92; ui/createtorrent/CreateTorrentActivity.java:77-80')
e('PermissionManager.lambda$new$0', 'MainActivity$1.onStorageResult', 'RESULT', 'Deliver the manage-all-files result to the main-screen permission callback',
  cls='non_standard', via='PermissionManager.Callback dispatch', evidence='INFERRED Java callback-interface dispatch; SRC ui/PermissionManager.java:60-68; ui/main/MainActivity.java:153-164')
e('PermissionManager.lambda$new$1', 'MainActivity$1.onStorageResult', 'RESULT', 'Deliver storage permission results to the main-screen callback when present',
  guard='storageResult != null', cls='non_standard', via='PermissionManager.Callback dispatch', evidence='INFERRED Java callback-interface dispatch; SRC ui/PermissionManager.java:70-85; ui/main/MainActivity.java:153-164')
e('PermissionManager.lambda$new$1', 'MainActivity$1.onNotificationResult', 'RESULT', 'Deliver notification permission results to the main-screen callback when present',
  guard='notificationsResult != null', cls='non_standard', via='PermissionManager.Callback dispatch', evidence='INFERRED Java callback-interface dispatch; SRC ui/PermissionManager.java:75-92; ui/main/MainActivity.java:166-173')
e('MainActivity$1.onStorageResult', 'PermissionDeniedDialog.newInstance', 'CALL', 'Create permission guidance after denial when another request is allowed',
  guard='!isGranted && shouldRequestStoragePermission && fm.findFragmentByTag(TAG_PERM_DENIED_DIALOG) == null', cls='explicit', evidence='SRC ui/main/MainActivity.java:155-164; ui/PermissionDeniedDialog.java:40-46')
e('MainActivity$1.onNotificationResult', 'PermissionManager.setDoNotAskNotifications', 'CALL', 'Update whether notification permission should be requested again',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:166-172; ui/PermissionManager.java:122-125')
e('MainActivity$1.onNotificationResult', 'MainViewModel.restartForegroundNotification', 'CALL', 'Restart foreground notification after notification permission is granted',
  guard='isGranted', cls='explicit', evidence='SRC ui/main/MainActivity.java:166-172')
e('CreateTorrentActivity$1.onStorageResult', 'PermissionDeniedDialog.newInstance', 'CALL', 'Show storage permission guidance when the user can be prompted again',
  guard='!isGranted && shouldRequestStoragePermission && fm.findFragmentByTag(TAG_PERM_DENIED_DIALOG) == null', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:64-75')
e('PermissionDeniedDialog.newInstance', 'PermissionDeniedDialog.<init>', 'CALL', 'Instantiate the storage permission guidance dialog',
  cls='explicit', evidence='SRC ui/PermissionDeniedDialog.java:31-38')
e('PermissionDeniedDialog.newInstance', 'PermissionDeniedDialog.onCreateDialog', 'LIFECYCLE', 'Create permission guidance after FragmentTransaction adds the dialog',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/PermissionDeniedDialog.java:31-60; ui/createtorrent/CreateTorrentActivity.java:68-73')
e('PermissionDeniedDialog.onCreateDialog', 'BaseAlertDialog.onCreateDialog', 'CALL', 'Initialize the shared dialog ViewModel',
  cls='explicit', evidence='SRC ui/PermissionDeniedDialog.java:40-44; ui/BaseAlertDialog.java:114-119')
e('PermissionDeniedDialog.onCreateDialog', 'BaseAlertDialog.buildDialog', 'CALL', 'Build storage permission guidance actions',
  cls='explicit', evidence='SRC ui/PermissionDeniedDialog.java:42-60; ui/BaseAlertDialog.java:143-197')
e('CreateTorrentActivity$1.onNotificationResult', 'PermissionManager.setDoNotAskNotifications', 'CALL', 'Persist whether notification permission should be requested again',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:77-80; ui/PermissionManager.java:122-125')
e('CreateTorrentDialog.newInstance', 'CreateTorrentDialog.<init>', 'CALL', 'Instantiate the torrent builder dialog fragment',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:87-93')
e('CreateTorrentActivity.onCreate', 'CreateTorrentDialog.onAttach', 'LIFECYCLE', 'Attach the torrent builder dialog when shown',
  guard='createTorrentDialog == null', cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/createtorrent/CreateTorrentActivity.java:83-87; ui/createtorrent/CreateTorrentDialog.java:95-102')
e('CreateTorrentDialog.onAttach', 'CreateTorrentDialog.onCreateDialog', 'LIFECYCLE', 'Create torrent builder controls after attachment',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:95-102,170-192')
e('CreateTorrentDialog.onCreateDialog', 'CreateTorrentDialog.onStart', 'LIFECYCLE', 'Start torrent builder observers after dialog creation',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:124-138,170-192')
e('CreateTorrentDialog.onCreateDialog', 'CreateTorrentDialog.onResume', 'LIFECYCLE', 'Resume torrent builder dialog after creation',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:104-122,170-192')
e('CreateTorrentDialog.onStart', 'CreateTorrentDialog.onStop', 'LIFECYCLE', 'Stop torrent builder subscriptions when the dialog stops',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:124-130,132-138')
e('CreateTorrentDialog.onCreateDialog', 'CreateTorrentDialog.initLayoutView', 'CALL', 'Initialize torrent builder inputs and file chooser actions',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:184-191,194-278')
e('CreateTorrentDialog.onCreateDialog', 'CreateTorrentDialog.initAlertDialog', 'CALL', 'Create torrent build and cancel buttons',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:189-191,277-323')
e('CreateTorrentDialog.onStart', 'CreateTorrentDialog.subscribeAlertDialog', 'CALL', 'Observe alert dialog actions while the builder is started',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:132-138,140-168')
e('CreateTorrentDialog.subscribeAlertDialog', 'BaseAlertDialog$SharedViewModel.observeEvents', 'CALL', 'Observe builder alert dialog events',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:140-168; ui/BaseAlertDialog.java:56-63')
e('CreateTorrentDialog.subscribeAlertDialog', 'CreateTorrentDialog.lambda$subscribeAlertDialog$1', 'REGISTER', 'Subscribe torrent builder to shared alert dialog events',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:140-168')
e('CreateTorrentDialog.subscribeAlertDialog', 'CreateTorrentDialog.lambda$subscribeAlertDialog$1', 'FRAMEWORK', 'Deliver shared alert dialog events to the builder observer',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:140-168')
e('CreateTorrentDialog.onResume', 'CreateTorrentDialog.lambda$onResume$0', 'REGISTER', 'Register back-key handling for the torrent builder dialog',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:104-122; FW-SRC core/java/android/app/Dialog.java:1346-1348,775-778')
e('CreateTorrentDialog.onResume', 'CreateTorrentDialog.lambda$onResume$0', 'FRAMEWORK', 'Dispatch back-key events to the torrent builder dialog listener',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:104-122; FW-SRC core/java/android/app/Dialog.java:1346-1348,775-778')
e('CreateTorrentDialog.lambda$onResume$0', 'CreateTorrentDialog.onBackPressed', 'CALL', 'Return BACK when the user presses back in the dialog',
  guard='keyCode == KeyEvent.KEYCODE_BACK && event.getAction() == KeyEvent.ACTION_DOWN', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:110-121,550-553; FW-SRC core/java/android/app/Dialog.java:775-778')
e('CreateTorrentActivity.onStart', 'CreateTorrentActivity.subscribeAlertDialog', 'CALL', 'Observe permission dialog actions while the activity is started',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:95-100,109-127')
e('CreateTorrentActivity.subscribeAlertDialog', 'CreateTorrentActivity.lambda$subscribeAlertDialog$0', 'REGISTER', 'Subscribe permission dialog event handling',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentActivity.java:109-127')
e('CreateTorrentActivity.subscribeAlertDialog', 'CreateTorrentActivity.lambda$subscribeAlertDialog$0', 'FRAMEWORK', 'Deliver permission dialog events to the activity observer',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentActivity.java:109-127')
e('CreateTorrentActivity.subscribeAlertDialog', 'BaseAlertDialog$SharedViewModel.observeEvents', 'CALL', 'Observe permission dialog actions from the shared dialog ViewModel',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:109-127; ui/BaseAlertDialog.java:56-63')
e('CreateTorrentActivity.lambda$subscribeAlertDialog$0', 'PermissionManager.requestPermissions', 'CALL', 'Request permissions again after the permission dialog is canceled',
  guard='event.dialogTag == TAG_PERM_DENIED_DIALOG && event.type == NEGATIVE_BUTTON_CLICKED', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:109-125')
e('CreateTorrentActivity.lambda$subscribeAlertDialog$0', 'PermissionManager.setDoNotAskStorage', 'CALL', 'Stop asking for storage permission after explicit confirmation',
  guard='event.dialogTag == TAG_PERM_DENIED_DIALOG && event.type == POSITIVE_BUTTON_CLICKED', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:109-125')
e('CreateTorrentActivity.onBackPressed', 'CreateTorrentDialog.onBackPressed', 'CALL', 'Forward back press to the torrent builder dialog',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:135-139')
e('CreateTorrentActivity.onStart', 'CreateTorrentActivity.onBackPressed', 'FRAMEWORK', 'Forward system Back key presses to the torrent builder activity',
  guard='keyCode == KeyEvent.KEYCODE_BACK && event.isTracking() && !event.isCanceled()', cls='standard', via='android.app.Activity.onKeyUp', evidence='SRC ui/createtorrent/CreateTorrentActivity.java:135-139; FW-SRC core/java/android/app/Activity.java:2975-2983')
e('CreateTorrentDialog.onBackPressed', 'CreateTorrentDialog.finish', 'CALL', 'Return BACK result from the torrent builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:550-560')
e('CreateTorrentDialog.finish', 'CreateTorrentViewModel.finish', 'CALL', 'Mark the torrent builder ViewModel as finished',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:555-560')
e('CreateTorrentDialog.finish', 'CreateTorrentActivity.onFragmentFinished', 'CALL', 'Return dialog completion to the host activity',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:555-560; ui/createtorrent/CreateTorrentActivity.java:129-133')
e('CreateTorrentDialog.initLayoutView', 'CreateTorrentDialog.lambda$initLayoutView$2', 'REGISTER', 'Register file chooser button',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:257-265; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('CreateTorrentDialog.initLayoutView', 'CreateTorrentDialog.lambda$initLayoutView$2', 'FRAMEWORK', 'Dispatch file chooser button taps',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:257-265; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('CreateTorrentDialog.initLayoutView', 'CreateTorrentDialog.lambda$initLayoutView$3', 'REGISTER', 'Register folder chooser button',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:267-275; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('CreateTorrentDialog.initLayoutView', 'CreateTorrentDialog.lambda$initLayoutView$3', 'FRAMEWORK', 'Dispatch folder chooser button taps',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:267-275; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('CreateTorrentDialog.initLayoutView', 'CreateTorrentDialog$3.onItemSelected', 'REGISTER', 'Register piece-size spinner selection handling',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:227-240; FW-SRC core/java/android/widget/AdapterView.java:412-415,944-945')
e('CreateTorrentDialog.initLayoutView', 'CreateTorrentDialog$3.onItemSelected', 'FRAMEWORK', 'Dispatch piece-size spinner selection changes',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:227-240; FW-SRC core/java/android/widget/AdapterView.java:412-415,944-945')
e('CreateTorrentDialog.initLayoutView', 'CreateTorrentDialog$4.onItemSelected', 'REGISTER', 'Register torrent-version spinner selection handling',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:242-255; FW-SRC core/java/android/widget/AdapterView.java:412-415,944-945')
e('CreateTorrentDialog.initLayoutView', 'CreateTorrentDialog$4.onItemSelected', 'FRAMEWORK', 'Dispatch torrent-version spinner selection changes',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:242-255; FW-SRC core/java/android/widget/AdapterView.java:412-415,944-945')
e('CreateTorrentDialog$3.onItemSelected', 'CreateTorrentViewModel.setPiecesSizeIndex', 'CALL', 'Store selected piece size',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:227-240; ui/createtorrent/CreateTorrentViewModel.java:136-142')
e('CreateTorrentDialog$4.onItemSelected', 'CreateTorrentViewModel.setTorrentVersionIndex', 'CALL', 'Store selected torrent format version',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:242-255; ui/createtorrent/CreateTorrentViewModel.java:144-149')
e('CreateTorrentDialog.lambda$initLayoutView$2', 'FileManagerDialog.onCreate', 'RESULT', 'Launch file chooser for the seed path',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:257-265; AndroidManifest.xml:137')
e('CreateTorrentDialog.lambda$initLayoutView$3', 'FileManagerDialog.onCreate', 'RESULT', 'Launch directory chooser for the seed path',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:267-275; AndroidManifest.xml:137')
e('CreateTorrentDialog.choosePathToSaveDialog', 'FileManagerDialog.onCreate', 'RESULT', 'Launch output file chooser for the created torrent',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:325-336; AndroidManifest.xml:137')
e('CreateTorrentDialog.<init>', 'CreateTorrentDialog.lambda$new$9', 'REGISTER', 'Register the directory chooser result handler',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher registration; SRC ui/createtorrent/CreateTorrentDialog.java:500-515')
e('CreateTorrentDialog.<init>', 'CreateTorrentDialog.lambda$new$10', 'REGISTER', 'Register the file chooser result handler',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher registration; SRC ui/createtorrent/CreateTorrentDialog.java:517-532')
e('CreateTorrentDialog.<init>', 'CreateTorrentDialog.lambda$new$11', 'REGISTER', 'Register the output chooser result handler',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher registration; SRC ui/createtorrent/CreateTorrentDialog.java:534-548')
e('FileManagerDialog.returnDirectoryUri', 'CreateTorrentDialog.lambda$new$9', 'RESULT', 'Return selected directory URI to torrent builder',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/filemanager/FileManagerDialog.java:557-568; ui/createtorrent/CreateTorrentDialog.java:500-515')
e('FileManagerDialog.returnFileUri', 'CreateTorrentDialog.lambda$new$10', 'RESULT', 'Return selected seed file URI to torrent builder',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/filemanager/FileManagerDialog.java:593-604; ui/createtorrent/CreateTorrentDialog.java:517-532')
e('FileManagerDialog.createFile', 'CreateTorrentDialog.lambda$new$11', 'RESULT', 'Return created torrent file URI to torrent builder',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/filemanager/FileManagerDialog.java:570-591; ui/createtorrent/CreateTorrentDialog.java:534-548')
e('CreateTorrentDialog.initAlertDialog', 'CreateTorrentDialog.lambda$initAlertDialog$7', 'REGISTER', 'Register alert shown setup for build state and buttons',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:280-323; FW-SRC core/java/android/app/Dialog.java:1294,1367')
e('CreateTorrentDialog.initAlertDialog', 'CreateTorrentDialog.lambda$initAlertDialog$7', 'FRAMEWORK', 'Run build state and button setup when the alert is shown',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:280-323; FW-SRC core/java/android/app/Dialog.java:1294,1367')
e('CreateTorrentDialog.lambda$initAlertDialog$7', 'CreateTorrentDialog.lambda$initAlertDialog$4', 'REGISTER', 'Observe torrent build state while the alert is shown',
  cls='non_standard', via='AndroidX LiveData observer', evidence='INFERRED AndroidX LiveData observer dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:291-309')
e('CreateTorrentDialog.lambda$initAlertDialog$7', 'CreateTorrentDialog.lambda$initAlertDialog$4', 'FRAMEWORK', 'Deliver torrent build state to the registered observer',
  cls='non_standard', via='AndroidX LiveData observer', evidence='INFERRED AndroidX LiveData observer dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:291-309')
e('CreateTorrentDialog.lambda$initAlertDialog$7', 'CreateTorrentDialog.lambda$initAlertDialog$5', 'REGISTER', 'Register the torrent builder cancel button',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:291-313; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('CreateTorrentDialog.lambda$initAlertDialog$7', 'CreateTorrentDialog.lambda$initAlertDialog$6', 'REGISTER', 'Register the torrent builder add button',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:291-321; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('CreateTorrentDialog.lambda$initAlertDialog$7', 'CreateTorrentDialog.lambda$initAlertDialog$5', 'FRAMEWORK', 'Dispatch the torrent builder cancel action',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:291-313; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('CreateTorrentDialog.lambda$initAlertDialog$7', 'CreateTorrentDialog.lambda$initAlertDialog$6', 'FRAMEWORK', 'Dispatch the torrent builder add action',
  cls='standard', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:291-321; FW-SRC core/java/android/view/View.java:6143-6147,6289-6294')
e('CreateTorrentDialog.lambda$initAlertDialog$4', 'CreateTorrentDialog.handleFinish', 'CALL', 'Finish torrent build after successful completion',
  guard='state.status == FINISHED', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:295-309,380-403')
e('CreateTorrentDialog.lambda$initAlertDialog$4', 'CreateTorrentDialog.handleBuildError', 'CALL', 'Handle torrent build errors',
  guard='state.status == ERROR', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:295-309,348-378')
e('CreateTorrentDialog.handleBuildError', 'CreateTorrentDialog.fileOrFolderNotFoundDialog', 'CALL', 'Show a missing-file or folder message for an input lookup failure',
  guard='err instanceof FileNotFoundException', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:348-378,425-443')
e('CreateTorrentDialog.handleBuildError', 'CreateTorrentDialog.emptyFolderErrorDialog', 'CALL', 'Show an empty-folder message for an empty input tree',
  guard='err instanceof IOException && err.getMessage().contains("content total size can\'t be 0")', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:367-374,445-463')
e('CreateTorrentDialog.handleBuildError', 'CreateTorrentDialog.errorReportDialog', 'CALL', 'Offer an error report for other build failures',
  guard='err instanceof IOException with non-empty content or any other Throwable', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:370-377,465-478')
e('CreateTorrentDialog.errorReportDialog', 'ErrorReportDialog.newInstance', 'CALL', 'Create a crash report dialog for a torrent build failure',
  guard='fm.findFragmentByTag(TAG_ERROR_REPORT_DIALOG) == null', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:465-477; ui/errorreport/ErrorReportDialog.java:39-52')
e('ErrorReportDialog.newInstance', 'ErrorReportDialog.onCreateDialog', 'LIFECYCLE', 'Create build error report dialog after it is shown',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:469-477; ui/errorreport/ErrorReportDialog.java:54-75')
e('CreateTorrentDialog.handleFinish', 'CreateTorrentDialog.finish', 'CALL', 'Return success when the user did not request seeding',
  guard='!viewModel.mutableParams.isStartSeeding()', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:380-403,555-560')
e('CreateTorrentDialog.handleFinish', 'CreateTorrentViewModel.downloadTorrent', 'CALL', 'Add the generated torrent when seeding is requested',
  guard='viewModel.mutableParams.isStartSeeding()', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:389-399; ui/createtorrent/CreateTorrentViewModel.java:352-384')
e('CreateTorrentDialog.handleFinish', 'CreateTorrentDialog.lambda$handleFinish$8', 'REGISTER', 'Subscribe to the generated torrent download result',
  guard='viewModel.mutableParams.isStartSeeding()', cls='non_standard', via='RxJava Completable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:389-399')
e('CreateTorrentDialog.handleFinish', 'CreateTorrentDialog.lambda$handleFinish$8', 'FRAMEWORK', 'Deliver successful torrent download completion',
  guard='viewModel.mutableParams.isStartSeeding()', cls='non_standard', via='RxJava Completable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:389-399')
e('CreateTorrentDialog.lambda$handleFinish$8', 'CreateTorrentDialog.finish', 'CALL', 'Return success after generated torrent has been added',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:391-396,555-560')
e('CreateTorrentDialog.lambda$handleFinish$8', 'CreateTorrentDialog.handleBuildError', 'CALL', 'Handle failure to add the generated torrent',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:391-396,348-378')
e('CreateTorrentDialog.lambda$initAlertDialog$5', 'CreateTorrentDialog.finish', 'CALL', 'Return CANCEL result from the torrent builder dialog',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:311-313,555-560')
e('CreateTorrentDialog.lambda$initAlertDialog$6', 'CreateTorrentDialog.choosePathToSaveDialog', 'CALL', 'Choose save path after a seed path is supplied',
  guard='!TextUtils.isEmpty(viewModel.mutableParams.getSeedPathName()) && !"null".equals(viewModel.mutableParams.getSeedPathName())', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:313-321,325-336')
e('CreateTorrentDialog.lambda$new$9', 'CreateTorrentDialog.openPathErrorDialog', 'CALL', 'Show a missing-path error when the folder chooser returns no URI',
  guard='resultCode == Activity.RESULT_OK && (data == null || data.getData() == null)', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:500-515')
e('CreateTorrentDialog.lambda$new$10', 'CreateTorrentDialog.openPathErrorDialog', 'CALL', 'Show a missing-path error when the file chooser returns no URI',
  guard='resultCode == Activity.RESULT_OK && (data == null || data.getData() == null)', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:517-532')
e('CreateTorrentDialog.lambda$new$11', 'CreateTorrentDialog.createFileErrorDialog', 'CALL', 'Show a save-path error when the output chooser returns no URI',
  guard='resultCode == Activity.RESULT_OK && (data == null || data.getData() == null)', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:534-548')
e('CreateTorrentDialog.lambda$new$11', 'CreateTorrentDialog.buildTorrent', 'CALL', 'Build torrent after the output chooser returns a path',
  guard='resultCode == Activity.RESULT_OK && data != null && data.getData() != null', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:534-548')
e('CreateTorrentDialog.buildTorrent', 'CreateTorrentViewModel.buildTorrent', 'CALL', 'Start torrent generation with the current dialog inputs',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:338-346')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.makeBuilder', 'CALL', 'Validate inputs and construct the torrent builder',
  guard='builder construction succeeds', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:151-164,177-209')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.onBuildError', 'CALL', 'Publish construction errors as build errors',
  guard='makeBuilder throws Exception', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:155-163,228-240')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.resetPercentProgress', 'CALL', 'Reset progress before starting the build subscriptions',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:165-170,247-250')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.makePercentProgress', 'REGISTER', 'Observe asynchronous torrent build progress',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:165-170,242-245')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.makePercentProgress', 'FRAMEWORK', 'Deliver progress updates from the torrent builder',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:165-170,242-245')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.onBuildSuccess', 'REGISTER', 'Subscribe to torrent builder completion',
  cls='non_standard', via='RxJava Single.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:171-174,211-226')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.onBuildError', 'REGISTER', 'Subscribe to torrent builder failure',
  cls='non_standard', via='RxJava Single.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:171-174,228-240')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.onBuildSuccess', 'FRAMEWORK', 'Deliver completed torrent bytes to success handling',
  cls='non_standard', via='RxJava Single.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:171-174,211-226')
e('CreateTorrentViewModel.makeBuilder', 'CreateTorrentViewModel.getPieceSizeByIndex', 'CALL', 'Select piece size for the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:189-193,333-336')
e('CreateTorrentViewModel.makeBuilder', 'CreateTorrentViewModel.getTorrentVersionByIndex', 'CALL', 'Select torrent format version for the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:189-193,338-349')
e('CreateTorrentViewModel.makeBuilder', 'CreateTorrentViewModel.getAndValidateTrackers', 'CALL', 'Validate tracker URLs before building',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:189-195,264-279')
e('CreateTorrentViewModel.makeBuilder', 'CreateTorrentViewModel.getAndValidateWebSeeds', 'CALL', 'Validate web seed URLs before building',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:189-195,281-295')
e('CreateTorrentViewModel.makeBuilder', 'CreateTorrentViewModel.makeCreator', 'CALL', 'Set the application creator string on the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:189-197,252-262')
e('CreateTorrentViewModel.makeBuilder', 'CreateTorrentViewModel.lambda$makeBuilder$2', 'REGISTER', 'Register skip-file filtering for builder input paths',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:198-208')
e('CreateTorrentViewModel.lambda$makeBuilder$2', 'CreateTorrentViewModel.decodeSkipFilesList', 'CALL', 'Read configured filename suffixes for each file-tree entry',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:198-208,323-331')
e('CreateTorrentViewModel.getAndValidateTrackers', 'CreateTorrentViewModel.decodeUrls', 'CALL', 'Split tracker URLs into individual lines',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:264-279,297-304')
e('CreateTorrentViewModel.getAndValidateTrackers', 'CreateTorrentViewModel.normalizeAndValidateUrl', 'CALL', 'Normalize and validate each tracker URL',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:268-275,306-321')
e('CreateTorrentViewModel.getAndValidateWebSeeds', 'CreateTorrentViewModel.decodeUrls', 'CALL', 'Split web seed URLs into individual lines',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:281-295,297-304')
e('CreateTorrentViewModel.getAndValidateWebSeeds', 'CreateTorrentViewModel.normalizeAndValidateUrl', 'CALL', 'Normalize and validate each web seed URL',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:284-291,306-321')
e('CreateTorrentViewModel.onBuildSuccess', 'CreateTorrentViewModel.onBuildError', 'CALL', 'Report failure to write generated torrent bytes',
  guard='fs.write throws IOException or UnknownUriException', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:211-226,228-240')
e('MainFragment.onViewCreated', 'MainFragment$2.onSelectionChanged', 'REGISTER', 'Observe torrent list selection changes',
  cls='non_standard', via='AndroidX SelectionTracker', evidence='INFERRED AndroidX SelectionTracker observer dispatch; SRC ui/main/MainFragment.java:157-194')
e('MainFragment.onViewCreated', 'MainFragment$2.onSelectionChanged', 'FRAMEWORK', 'Notify the registered selection observer when list selection changes',
  cls='non_standard', via='AndroidX SelectionTracker', evidence='INFERRED AndroidX SelectionTracker observer dispatch; SRC ui/main/MainFragment.java:157-194')
e('MainFragment$2.onSelectionChanged', 'MainFragment$3.onCreateActionMode', 'FRAMEWORK', 'Start contextual action mode when a torrent is selected',
  guard='selectionTracker.hasSelection() && actionMode == null', cls='non_standard', via='AndroidX AppCompat ActionMode', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/main/MainFragment.java:166-184,457-472')
e('MainFragment$2.onSelectionChanged', 'MainFragment.setActionModeTitle', 'CALL', 'Update contextual action count after selection changes',
  guard='selectionTracker.hasSelection()', cls='explicit', evidence='SRC ui/main/MainFragment.java:172-183; ui/main/MainFragment.java:452-455')
e('MainFragment$2.onSelectionChanged', 'MainFragment$3.onActionItemClicked', 'REGISTER', 'Register contextual action menu item callback',
  cls='non_standard', via='AndroidX AppCompat ActionMode', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/main/MainFragment.java:457-490')
e('MainFragment$2.onSelectionChanged', 'MainFragment$3.onActionItemClicked', 'FRAMEWORK', 'Dispatch contextual menu selections to the registered action-mode callback',
  guard='selectionTracker.hasSelection() && actionMode != null', cls='non_standard', via='AndroidX AppCompat ActionMode', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/main/MainFragment.java:166-184,457-490')
e('MainFragment$3.onActionItemClicked', 'MainFragment.deleteTorrentsDialog', 'CALL', 'Confirm deleting selected torrents',
  guard='itemId == R.id.delete_torrent_menu', cls='explicit', evidence='SRC ui/main/MainFragment.java:474-490; ui/main/MainFragment.java:501-520')
e('MainFragment$3.onActionItemClicked', 'MainFragment.selectAllTorrents', 'CALL', 'Select all torrents from contextual menu',
  guard='itemId == R.id.select_all_torrent_menu', cls='explicit', evidence='SRC ui/main/MainFragment.java:474-490; ui/main/MainFragment.java:588-595')
e('MainFragment$3.onActionItemClicked', 'MainFragment.forceRecheckTorrents', 'CALL', 'Force recheck selected torrents',
  guard='itemId == R.id.force_recheck_torrent_menu', cls='explicit', evidence='SRC ui/main/MainFragment.java:474-490; ui/main/MainFragment.java:597-606')
e('MainFragment$3.onActionItemClicked', 'MainFragment.forceAnnounceTorrents', 'CALL', 'Force announce selected torrents',
  guard='itemId == R.id.force_announce_torrent_menu', cls='explicit', evidence='SRC ui/main/MainFragment.java:474-490; ui/main/MainFragment.java:608-617')
e('MainFragment.deleteTorrentsDialog', 'BaseAlertDialog.newInstance', 'CALL', 'Create confirmation dialog for selected torrent deletion',
  guard='isAdded() && no dialog is already shown', cls='explicit', evidence='SRC ui/main/MainFragment.java:501-520')
e('MainFragment.subscribeAlertDialog', 'MainFragment.lambda$subscribeAlertDialog$3', 'REGISTER', 'Subscribe to dialog confirmation events through Rx',
  cls='non_standard', via='RxJava', evidence='INFERRED RxJava subscription dispatch; SRC ui/main/MainFragment.java:302-323')
e('MainFragment.subscribeAlertDialog', 'MainFragment.lambda$subscribeAlertDialog$3', 'FRAMEWORK', 'Deliver shared alert-dialog events to the Rx observer',
  cls='non_standard', via='RxJava', evidence='INFERRED RxJava observer delivery; SRC ui/main/MainFragment.java:302-323')
e('MainFragment.lambda$subscribeAlertDialog$3', 'MainFragment.deleteTorrents', 'CALL', 'Delete selected torrents after positive confirmation',
  guard='event.type == POSITIVE_BUTTON_CLICKED && event.dialogTag == TAG_DELETE_TORRENTS_DIALOG && deleteTorrentsDialog != null', cls='explicit', evidence='SRC ui/main/MainFragment.java:309-314; ui/main/MainFragment.java:566-581')
e('MainFragment.deleteTorrents', 'MainFragment.lambda$deleteTorrents$12', 'REGISTER', 'Map selected torrent rows to IDs',
  cls='non_standard', via='RxJava Observable.map', evidence='INFERRED RxJava operator dispatch; SRC ui/main/MainFragment.java:575-581')
e('MainFragment.deleteTorrents', 'MainFragment.lambda$deleteTorrents$12', 'FRAMEWORK', 'Apply the registered ID mapping to selected torrent rows',
  cls='non_standard', via='RxJava Observable.map', evidence='INFERRED RxJava operator dispatch; SRC ui/main/MainFragment.java:575-581')
e('MainFragment.deleteTorrents', 'MainFragment.lambda$deleteTorrents$13', 'REGISTER', 'Submit deletion after selection IDs are collected',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/main/MainFragment.java:575-581')
e('MainFragment.deleteTorrents', 'MainFragment.lambda$deleteTorrents$13', 'FRAMEWORK', 'Deliver selected torrent IDs to the deletion subscriber',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/main/MainFragment.java:575-581')
e('MainFragment.lambda$deleteTorrents$13', 'MainViewModel.deleteTorrents', 'CALL', 'Delete selected torrent IDs using current checkbox setting',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:578-581')
e('MainFragment.addLinkDialog', 'AddLinkActivity.<init>', 'INTENT', 'Open Add Link screen from main fragment',
  cls='standard', evidence='SRC ui/main/MainFragment.java:523-526; AndroidManifest.xml:235-238; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('MainFragment.addLinkDialog', 'AddLinkActivity.onCreate', 'INTENT', 'Create Add Link screen from main fragment',
  cls='standard', evidence='SRC ui/main/MainFragment.java:523-526; AndroidManifest.xml:235-238; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('MainFragment.createTorrentDialog', 'CreateTorrentActivity.<init>', 'INTENT', 'Open Create Torrent screen from main fragment',
  cls='standard', evidence='SRC ui/main/MainFragment.java:561-564; AndroidManifest.xml:231-233; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('MainFragment.createTorrentDialog', 'CreateTorrentActivity.onCreate', 'INTENT', 'Create Create Torrent screen from main fragment',
  cls='standard', evidence='SRC ui/main/MainFragment.java:561-564; AndroidManifest.xml:231-233; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('MainFragment.openTorrentFileDialog', 'FileManagerDialog.<init>', 'INTENT', 'Launch file picker through AndroidX ActivityResult',
  cls='non_standard', via='AndroidX ActivityResult API', evidence='INFERRED AndroidX ActivityResult dispatch; SRC ui/main/MainFragment.java:528-539,619-636; AndroidManifest.xml:137-138')
e('MainFragment.openTorrentFileDialog', 'FileManagerDialog.onCreate', 'INTENT', 'Create file picker through AndroidX ActivityResult',
  cls='non_standard', via='AndroidX ActivityResult API', evidence='INFERRED AndroidX ActivityResult dispatch; SRC ui/main/MainFragment.java:528-539,619-636; AndroidManifest.xml:137-138')
e('MainFragment.<init>', 'MainFragment.lambda$new$18', 'REGISTER', 'Register file picker ActivityResult callback',
  cls='non_standard', via='AndroidX ActivityResult API', evidence='INFERRED AndroidX ActivityResult callback dispatch; SRC ui/main/MainFragment.java:619-636')
e('FileManagerDialog.returnFileUri', 'MainFragment.lambda$new$18', 'RESULT', 'Return a selected torrent file through the registered ActivityResult launcher',
  guard='RESULT_OK and MainFragment launched FileManagerDialog in FILE_CHOOSER_MODE', cls='non_standard', via='AndroidX ActivityResultRegistry', evidence='INFERRED AndroidX ActivityResult delivery; SRC ui/main/MainFragment.java:528-539,619-636; ui/filemanager/FileManagerDialog.java:593-604')
e('MainFragment.lambda$new$18', 'AddTorrentActivity.<init>', 'RESULT', 'Open add-torrent screen for selected file URI',
  guard='resultCode == Activity.RESULT_OK && data != null && data.getData() != null', cls='standard', evidence='SRC ui/main/MainFragment.java:619-635; AndroidManifest.xml:62-92; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('MainFragment.lambda$new$18', 'AddTorrentActivity.onCreate', 'RESULT', 'Create add-torrent screen for selected file URI',
  guard='resultCode == Activity.RESULT_OK && data != null && data.getData() != null', cls='standard', evidence='SRC ui/main/MainFragment.java:619-635; AndroidManifest.xml:62-92; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('MainFragment.lambda$new$18', 'MainFragment.openFileErrorDialog', 'CALL', 'Show error when file picker returns no URI',
  guard='resultCode == Activity.RESULT_OK && (data == null || data.getData() == null)', cls='explicit', evidence='SRC ui/main/MainFragment.java:623-630; ui/main/MainFragment.java:541-559')
e('MainFragment.openFileErrorDialog', 'BaseAlertDialog.newInstance', 'CALL', 'Create file-open error dialog',
  guard='isAdded() && no open-file error dialog exists', cls='explicit', evidence='SRC ui/main/MainFragment.java:541-559')
e('MainFragment.onItemClicked', 'TorrentListAdapter.markAsOpen', 'CALL', 'Mark selected torrent as open in two-pane layout',
  guard='Utils.isTwoPane(activity)', cls='explicit', evidence='SRC ui/main/MainFragment.java:378-384; ui/main/TorrentListAdapter.java:122-137')
e('MainFragment.onItemClicked', 'MsgMainViewModel.torrentDetailsOpened', 'CALL', 'Publish selected torrent details request',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:378-384')
e('MainFragment.onItemPauseClicked', 'MainViewModel.pauseResumeTorrent', 'CALL', 'Pause or resume clicked torrent',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:386-390')
e('MainActivity.subscribeMsgViewModel', 'MainActivity.showDetailTorrent', 'REGISTER', 'Subscribe to torrent detail navigation events',
  cls='non_standard', via='RxJava observeOn/subscribe', evidence='INFERRED RxJava callback dispatch; SRC ui/main/MainActivity.java:437-445')
e('MainActivity.subscribeMsgViewModel', 'MainActivity.showBlankFragment', 'REGISTER', 'Subscribe to detail-close message events',
  cls='non_standard', via='RxJava observeOn/subscribe', evidence='INFERRED RxJava callback dispatch; SRC ui/main/MainActivity.java:437-454')
e('MainActivity.subscribeMsgViewModel', 'MainActivity.lambda$subscribeMsgViewModel$5', 'REGISTER', 'Observe torrent detail close messages',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/main/MainActivity.java:442-445')
e('MainActivity.subscribeMsgViewModel', 'MainActivity.lambda$subscribeMsgViewModel$5', 'FRAMEWORK', 'Deliver a detail-close event to the activity',
  cls='non_standard', via='RxJava observeOn/subscribe dispatch', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/main/MainActivity.java:442-445')
e('MainActivity.lambda$subscribeMsgViewModel$5', 'MainActivity.showBlankFragment', 'CALL', 'Clear the selected detail page after a close message',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:442-445')
e('MsgMainViewModel.torrentDetailsOpened', 'MainActivity.showDetailTorrent', 'FRAMEWORK', 'Deliver the published torrent-details-open event to the subscribed activity',
  cls='non_standard', via='RxJava PublishSubject', evidence='INFERRED RxJava PublishSubject observer delivery; SRC ui/main/MsgMainViewModel.java:30-40; ui/main/MainActivity.java:437-440; ui/main/MainFragment.java:378-384')
e('MsgMainViewModel.torrentDetailsClosed', 'MainActivity.showBlankFragment', 'FRAMEWORK', 'Deliver the published torrent-details-close event to the subscribed activity',
  cls='non_standard', via='RxJava PublishSubject', evidence='INFERRED RxJava PublishSubject observer delivery; SRC ui/main/MsgMainViewModel.java:31,43-50; ui/main/MainActivity.java:442-445; ui/main/MainActivity.java:806-810')
e('MainActivity.subscribeSessionStats', 'MainActivity.updateSessionStats', 'REGISTER', 'Subscribe to session statistics updates',
  cls='non_standard', via='RxJava observeOn/subscribe', evidence='INFERRED RxJava callback dispatch; SRC ui/main/MainActivity.java:456-461')
e('MainActivity.subscribeSessionStats', 'MainActivity.updateSessionStats', 'FRAMEWORK', 'Deliver session-statistics values to the subscribed observer',
  cls='non_standard', via='RxJava observeOn/subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/main/MainActivity.java:456-461')
e('MainActivity.subscribeAlertDialog', 'MainActivity.lambda$subscribeAlertDialog$4', 'REGISTER', 'Subscribe the activity dialog-event handler through RxJava',
  cls='non_standard', via='RxJava subscribe', evidence='INFERRED RxJava observer registration; SRC ui/main/MainActivity.java:406-434')
e('MainActivity.subscribeAlertDialog', 'MainActivity.lambda$subscribeAlertDialog$4', 'FRAMEWORK', 'Deliver shared dialog events to the subscribed activity handler',
  cls='non_standard', via='RxJava observeOn/subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/main/MainActivity.java:406-434')
e('MainActivity.lambda$subscribeAlertDialog$4', 'MainActivity.openChangelogLink', 'CALL', 'Open the changelog for the About dialog negative-button event',
  guard='event.dialogTag == TAG_ABOUT_DIALOG && event.type == NEGATIVE_BUTTON_CLICKED', cls='explicit', evidence='SRC ui/main/MainActivity.java:413-417; ui/main/MainActivity.java:795-799')
e('MainActivity.lambda$subscribeAlertDialog$4', 'MainActivity.initAboutDialog', 'CALL', 'Fill About dialog details after its shown event',
  guard='event.dialogTag == TAG_ABOUT_DIALOG && event.type == DIALOG_SHOWN', cls='explicit', evidence='SRC ui/main/MainActivity.java:413-420; ui/main/MainActivity.java:776-793')
e('MainActivity.showDetailTorrent', 'DetailTorrentFragment.newInstance', 'CALL', 'Create two-pane torrent detail fragment',
  guard='Utils.isTwoPane(this)', cls='explicit', evidence='SRC ui/main/MainActivity.java:653-667')
e('MainActivity.showDetailTorrent', 'DetailTorrentActivity.<init>', 'INTENT', 'Open detail activity in single-pane layout',
  guard='!Utils.isTwoPane(this)', cls='standard', evidence='SRC ui/main/MainActivity.java:669-673; AndroidManifest.xml:139; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('MainActivity.showDetailTorrent', 'DetailTorrentActivity.<clinit>', 'INTENT', 'Initialize the internal detail activity class before ActivityThread constructs it',
  guard='!Utils.isTwoPane(this)', cls='standard', evidence='SRC ui/main/MainActivity.java:669-673; ui/detailtorrent/DetailTorrentActivity.java:43; INFERRED JVM class initialization before construction; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('MainActivity.showDetailTorrent', 'DetailTorrentActivity.onCreate', 'INTENT', 'Create detail activity in single-pane layout',
  guard='!Utils.isTwoPane(this)', cls='standard', evidence='SRC ui/main/MainActivity.java:669-673; AndroidManifest.xml:139; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('AddTorrentActivity.onCreate', 'AddTorrentActivity.fillMutableParams', 'CALL', 'Load add-torrent defaults from preferences',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:128-132; ui/addtorrent/AddTorrentActivity.java:142-167')
e('AddTorrentActivity.onCreate', 'PermissionManager.requestPermissions', 'CALL', 'Request missing add-torrent permissions',
  guard='!permissionManager.checkPermissions() && permDeniedDialog == null', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:133-135')
e('AddTorrentActivity.onCreate', 'AddTorrentActivity.initLayout', 'CALL', 'Initialize add-torrent tabs and toolbar',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:136-140; ui/addtorrent/AddTorrentActivity.java:277-303')
e('AddTorrentActivity.onCreate', 'AddTorrentActivity.observeDecodeState', 'CALL', 'Observe torrent decode state after activity setup',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:138-140; ui/addtorrent/AddTorrentActivity.java:305-327')
e('AddTorrentActivity.onCreate', 'AddTorrentActivity.onStart', 'LIFECYCLE', 'Start add-torrent activity after successful creation',
  guard='!mFinished', cls='standard', evidence='SRC ui/addtorrent/AddTorrentActivity.java:96-140,178-185; FW-SRC core/java/android/app/ActivityThread.java:2738-2745; core/java/android/app/Instrumentation.java:1333-1335')
e('AddTorrentActivity.onStart', 'AddTorrentActivity.onStop', 'LIFECYCLE', 'Stop the add-torrent activity after it leaves the started foreground state',
  cls='standard', evidence='FW-SRC core/java/android/app/Activity.java:7130-7182; core/java/android/app/Instrumentation.java:1374-1376; SRC ui/addtorrent/AddTorrentActivity.java:169-185')
e('AddTorrentActivity.onStop', 'AddTorrentActivity.unsubscribeParamsChanged', 'CALL', 'Remove the mutable-parameter observer when the activity stops',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:169-199')
e('AddTorrentActivity.onStart', 'AddTorrentActivity.subscribeAlertDialog', 'CALL', 'Subscribe to dialog events at activity start',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:178-190')
e('AddTorrentActivity.subscribeAlertDialog', 'AddTorrentActivity.handleAlertDialogEvent', 'REGISTER', 'Subscribe the activity handler to shared alert-dialog events',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer registration; SRC ui/addtorrent/AddTorrentActivity.java:187-190,237-274')
e('AddTorrentActivity.subscribeAlertDialog', 'AddTorrentActivity.handleAlertDialogEvent', 'FRAMEWORK', 'Deliver shared alert-dialog events to the activity handler',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/addtorrent/AddTorrentActivity.java:187-190,237-274')
e('AddTorrentActivity.onStart', 'AddTorrentActivity.subscribeParamsChanged', 'CALL', 'Register mutable parameter observer at activity start',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:178-195')
e('AddTorrentActivity.onStart', 'AddTorrentActivity.onBackPressed', 'FRAMEWORK', 'Handle Back while the add-torrent activity is active',
  guard='keyCode == KEYCODE_BACK && event.isTracking() && !event.isCanceled() && targetSdkVersion >= ECLAIR', cls='standard', evidence='SRC ui/addtorrent/AddTorrentActivity.java:178-185,573-576; FW-SRC core/java/android/app/Activity.java:2975-2983')
e('AddTorrentActivity.onStart', 'AddTorrentActivity.onPrepareOptionsMenu', 'FRAMEWORK', 'Prepare toolbar actions through the AppCompat action bar',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu dispatch; SRC ui/addtorrent/AddTorrentActivity.java:277-280,539-548')
e('AddTorrentActivity.onPrepareOptionsMenu', 'AddTorrentActivity.onOptionsItemSelected', 'FRAMEWORK', 'Dispatch selected add-torrent toolbar actions',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu dispatch; SRC ui/addtorrent/AddTorrentActivity.java:539-562; FW-SRC core/java/android/app/Activity.java:3431-3451')
e('AddTorrentActivity.initLayout', 'AddTorrentPagerAdapter.<init>', 'CALL', 'Create add-torrent information and files pager adapter',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:288-303')
e('AddTorrentActivity.initLayout', 'AddTorrentActivity.lambda$initLayout$0', 'REGISTER', 'Register tab labels with TabLayoutMediator',
  cls='non_standard', via='Google Material TabLayoutMediator', evidence='INFERRED TabLayoutMediator callback dispatch; SRC ui/addtorrent/AddTorrentActivity.java:288-303')
e('AddTorrentActivity.initLayout', 'AddTorrentActivity.lambda$initLayout$0', 'FRAMEWORK', 'Configure tab labels when the mediator attaches or the selected page changes',
  cls='non_standard', via='Google Material TabLayoutMediator', evidence='INFERRED TabLayoutMediator callback dispatch; SRC ui/addtorrent/AddTorrentActivity.java:288-303')
e('MainActivity.onCreate', 'MainFragment.<init>', 'FRAMEWORK', 'Inflate MainFragment from the selected activity_main layout',
  cls='non_standard', via='AndroidX FragmentContainerView', evidence='INFERRED AndroidX FragmentContainerView class inflation; SRC ui/main/MainActivity.java:182-185; res/values/layouts.xml:1-4; res/values-large-land-notouch/layouts.xml:1-4; res/layout/activity_main_drawer.xml:22-28; res/layout/activity_main_two_pane.xml:26-32; ui/main/MainFragment.java:85-87')
e('MainFragment.<init>', 'MainFragment.onAttach', 'LIFECYCLE', 'Attach inflated main fragment to its activity',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/main/MainFragment.java:85-87,223-230')
e('MainFragment.onAttach', 'MainFragment.onCreateView', 'LIFECYCLE', 'Create view for the attached main fragment',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/main/MainFragment.java:223-230,113-122')
e('MainFragment.onCreateView', 'MainFragment.onViewCreated', 'LIFECYCLE', 'Initialize main fragment after creating its view',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/main/MainFragment.java:115-127')
e('MainFragment.onViewCreated', 'TorrentListAdapter.<init>', 'CALL', 'Create torrent list adapter',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:125-156')
e('MainFragment.onViewCreated', 'MainFragment.initFabSpeedDial', 'CALL', 'Initialize main screen floating action menu',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:157-208')
e('MainFragment.onViewCreated', 'MainFragment.showAddTorrentMenu', 'CALL', 'Open shortcut add-torrent menu after view creation',
  guard='i != null && ACTION_ADD_TORRENT_SHORTCUT.equals(i.getAction())', cls='explicit', evidence='SRC ui/main/MainFragment.java:202-208; ui/main/MainFragment.java:210-221')
e('MainFragment.showAddTorrentMenu', 'MainFragment.lambda$showAddTorrentMenu$0', 'REGISTER', 'Post context-menu setup until the content view is attached',
  cls='standard', evidence='SRC ui/main/MainFragment.java:210-220; FW-SRC core/java/android/view/View.java:15765-15786')
e('MainFragment.showAddTorrentMenu', 'MainFragment.lambda$showAddTorrentMenu$0', 'FRAMEWORK', 'Run the posted context-menu setup on the UI thread',
  cls='standard', evidence='SRC ui/main/MainFragment.java:210-220; FW-SRC core/java/android/view/View.java:15765-15786')
e('MainFragment.lambda$showAddTorrentMenu$0', 'MainFragment.onCreateContextMenu', 'FRAMEWORK', 'Create the registered main-fragment context menu',
  cls='non_standard', via='AndroidX Fragment context-menu dispatch', evidence='INFERRED AndroidX Fragment context-menu dispatch; SRC ui/main/MainFragment.java:216-220,393-399; FW-SRC core/java/android/app/Activity.java:3760-3792')
e('MainFragment.onCreateContextMenu', 'MainFragment.onContextItemSelected', 'FRAMEWORK', 'Deliver the selected context-menu item to the main fragment',
  cls='non_standard', via='AndroidX FragmentActivity context-menu dispatch', evidence='INFERRED AndroidX FragmentActivity context-menu dispatch; SRC ui/main/MainFragment.java:393-411; FW-SRC core/java/android/app/Activity.java:3466-3473,3821-3825')
e('MainFragment.onViewCreated', 'MainFragment.onStart', 'LIFECYCLE', 'Start main fragment after its view is created',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/main/MainFragment.java:125-127,232-242')
e('MainFragment.onStart', 'MainFragment.subscribeAdapter', 'CALL', 'Subscribe adapter to torrent updates at fragment start',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:232-242')
e('MainFragment.onStart', 'MainFragment.subscribeAlertDialog', 'CALL', 'Subscribe to alert dialog events at fragment start',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:232-242')
e('MainFragment.onStart', 'MainFragment.subscribeForceSortAndFilter', 'CALL', 'Subscribe to sort and filter changes at fragment start',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:232-242')
e('MainFragment.subscribeForceSortAndFilter', 'MainFragment.lambda$subscribeForceSortAndFilter$4', 'REGISTER', 'Register the force-update filter predicate with RxJava',
  cls='non_standard', via='RxJava Observable.filter', evidence='INFERRED RxJava operator dispatch; SRC ui/main/MainFragment.java:325-330')
e('MainFragment.subscribeForceSortAndFilter', 'MainFragment.lambda$subscribeForceSortAndFilter$4', 'FRAMEWORK', 'Evaluate the sort/filter refresh predicate for emitted values',
  cls='non_standard', via='RxJava Observable.filter', evidence='INFERRED RxJava operator dispatch; SRC ui/main/MainFragment.java:325-330')
e('MainFragment.subscribeForceSortAndFilter', 'MainFragment.lambda$subscribeForceSortAndFilter$5', 'REGISTER', 'Register the sort/filter refresh subscriber with RxJava',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer registration; SRC ui/main/MainFragment.java:325-330')
e('MainFragment.subscribeForceSortAndFilter', 'MainFragment.lambda$subscribeForceSortAndFilter$5', 'FRAMEWORK', 'Deliver force-update values to the subscriber',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/main/MainFragment.java:325-330')
e('MainFragment.lambda$subscribeForceSortAndFilter$5', 'MainFragment.getAllTorrentsSingle', 'CALL', 'Refresh the torrent list after a forced sort or filter update',
  guard='force == true', cls='explicit', evidence='SRC ui/main/MainFragment.java:327-330,333-348')
e('MainFragment.forceRecheckTorrents', 'MainFragment.lambda$forceRecheckTorrents$14', 'REGISTER', 'Map selected rows to IDs for the recheck operation',
  cls='non_standard', via='RxJava Observable.map', evidence='INFERRED RxJava operator dispatch; SRC ui/main/MainFragment.java:597-605')
e('MainFragment.forceRecheckTorrents', 'MainFragment.lambda$forceRecheckTorrents$14', 'FRAMEWORK', 'Map selected rows to IDs for the recheck operation',
  cls='non_standard', via='RxJava Observable.map', evidence='INFERRED RxJava operator dispatch; SRC ui/main/MainFragment.java:597-605')
e('MainFragment.forceRecheckTorrents', 'MainFragment.lambda$forceRecheckTorrents$15', 'REGISTER', 'Subscribe to the selected ID list for torrent rechecking',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer registration; SRC ui/main/MainFragment.java:597-605')
e('MainFragment.forceRecheckTorrents', 'MainFragment.lambda$forceRecheckTorrents$15', 'FRAMEWORK', 'Deliver selected IDs to the recheck subscriber',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/main/MainFragment.java:597-605')
e('MainFragment.lambda$forceRecheckTorrents$15', 'MainViewModel.forceRecheckTorrents', 'CALL', 'Recheck the selected torrent IDs',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:602-605')
e('MainFragment.forceAnnounceTorrents', 'MainFragment.lambda$forceAnnounceTorrents$16', 'REGISTER', 'Map selected rows to IDs for the announce operation',
  cls='non_standard', via='RxJava Observable.map', evidence='INFERRED RxJava operator dispatch; SRC ui/main/MainFragment.java:608-616')
e('MainFragment.forceAnnounceTorrents', 'MainFragment.lambda$forceAnnounceTorrents$16', 'FRAMEWORK', 'Map selected rows to IDs for the announce operation',
  cls='non_standard', via='RxJava Observable.map', evidence='INFERRED RxJava operator dispatch; SRC ui/main/MainFragment.java:608-616')
e('MainFragment.forceAnnounceTorrents', 'MainFragment.lambda$forceAnnounceTorrents$17', 'REGISTER', 'Subscribe to the selected ID list for the announce operation',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer registration; SRC ui/main/MainFragment.java:608-616')
e('MainFragment.forceAnnounceTorrents', 'MainFragment.lambda$forceAnnounceTorrents$17', 'FRAMEWORK', 'Deliver selected IDs to the announce subscriber',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/main/MainFragment.java:608-616')
e('MainFragment.lambda$forceAnnounceTorrents$17', 'MainViewModel.forceAnnounceTorrents', 'CALL', 'Announce the selected torrent IDs',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:613-616')
e('MainFragment.onStart', 'MainFragment.subscribeTorrentsDeleted', 'CALL', 'Subscribe to torrent deletion events at fragment start',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:232-242')
e('MainFragment.onStart', 'MainFragment.subscribeMsgViewModel', 'CALL', 'Subscribe to main messages at fragment start',
  cls='explicit', evidence='SRC ui/main/MainFragment.java:232-242')
e('MainFragment.subscribeTorrentsDeleted', 'MainFragment.lambda$subscribeTorrentsDeleted$8', 'REGISTER', 'Filter deletion events to the currently opened torrent',
  cls='non_standard', via='RxJava Observable.filter', evidence='INFERRED RxJava operator dispatch; SRC ui/main/MainFragment.java:350-365')
e('MainFragment.subscribeTorrentsDeleted', 'MainFragment.lambda$subscribeTorrentsDeleted$8', 'FRAMEWORK', 'Evaluate deletion events against the currently opened torrent',
  cls='non_standard', via='RxJava Observable.filter', evidence='INFERRED RxJava operator dispatch; SRC ui/main/MainFragment.java:350-365')
e('MainFragment.subscribeTorrentsDeleted', 'MainFragment.lambda$subscribeTorrentsDeleted$9', 'REGISTER', 'Subscribe to deletion events matching the opened torrent',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer registration; SRC ui/main/MainFragment.java:350-365')
e('MainFragment.subscribeTorrentsDeleted', 'MainFragment.lambda$subscribeTorrentsDeleted$9', 'FRAMEWORK', 'Deliver matching deletion events to the fragment observer',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/main/MainFragment.java:350-365')
e('MainFragment.lambda$subscribeTorrentsDeleted$9', 'TorrentListAdapter.markAsOpen', 'CALL', 'Clear the opened row after its torrent is deleted in two-pane mode',
  guard='Utils.isTwoPane(activity)', cls='explicit', evidence='SRC ui/main/MainFragment.java:362-365; ui/main/TorrentListAdapter.java:122-137')
e('MainFragment.subscribeMsgViewModel', 'MainFragment.lambda$subscribeMsgViewModel$10', 'REGISTER', 'Subscribe to detail-close messages from the shared view model',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer registration; SRC ui/main/MainFragment.java:368-376')
e('MainFragment.subscribeMsgViewModel', 'MainFragment.lambda$subscribeMsgViewModel$10', 'FRAMEWORK', 'Deliver a detail-close message to the fragment observer',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/main/MainFragment.java:368-376')
e('MainFragment.lambda$subscribeMsgViewModel$10', 'TorrentListAdapter.markAsOpen', 'CALL', 'Clear the opened row after a detail-close message in two-pane mode',
  guard='Utils.isTwoPane(activity)', cls='explicit', evidence='SRC ui/main/MainFragment.java:370-375; ui/main/TorrentListAdapter.java:122-137')
e('MainFragment.onViewCreated', 'TorrentListAdapter.onBindViewHolder', 'FRAMEWORK', 'Bind torrent rows through the RecyclerView adapter',
  cls='non_standard', via='AndroidX RecyclerView.Adapter', evidence='INFERRED AndroidX RecyclerView invokes adapter binding; SRC ui/main/MainFragment.java:136-155; ui/main/TorrentListAdapter.java:74-104')
e('TorrentListAdapter.onBindViewHolder', 'TorrentListAdapter$ViewHolder.bind', 'CALL', 'Bind a torrent row and its click listeners',
  cls='explicit', evidence='SRC ui/main/TorrentListAdapter.java:88-104,171-202')
e('TorrentListAdapter$ViewHolder.bind', 'TorrentListAdapter$ViewHolder.lambda$bind$0', 'REGISTER', 'Register torrent row click callback',
  cls='standard', evidence='SRC ui/main/TorrentListAdapter.java:189-196; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('TorrentListAdapter$ViewHolder.bind', 'TorrentListAdapter$ViewHolder.lambda$bind$0', 'FRAMEWORK', 'Dispatch a tap on a torrent row to its listener',
  cls='standard', evidence='SRC ui/main/TorrentListAdapter.java:189-196; FW-SRC core/java/android/view/View.java:6289-6305')
e('TorrentListAdapter$ViewHolder.bind', 'TorrentListAdapter$ViewHolder.lambda$bind$1', 'REGISTER', 'Register torrent pause button callback',
  cls='standard', evidence='SRC ui/main/TorrentListAdapter.java:198-202; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('TorrentListAdapter$ViewHolder.bind', 'TorrentListAdapter$ViewHolder.lambda$bind$1', 'FRAMEWORK', 'Dispatch a tap on the torrent pause control to its listener',
  cls='standard', evidence='SRC ui/main/TorrentListAdapter.java:198-202; FW-SRC core/java/android/view/View.java:6289-6305')
e('TorrentListAdapter$ViewHolder.lambda$bind$0', 'MainFragment.onItemClicked', 'CALL', 'Handle torrent row selection',
  cls='explicit', evidence='SRC ui/main/TorrentListAdapter.java:189-196; ui/main/MainFragment.java:378-384')
e('TorrentListAdapter$ViewHolder.lambda$bind$1', 'MainFragment.onItemPauseClicked', 'CALL', 'Handle torrent pause control click',
  cls='explicit', evidence='SRC ui/main/TorrentListAdapter.java:198-202; ui/main/MainFragment.java:386-390')
e('MainFragment.onContextItemSelected', 'MainFragment.addLinkDialog', 'CALL', 'Open add-link dialog from context menu',
  guard='itemId == R.id.add_link_menu', cls='explicit', evidence='SRC ui/main/MainFragment.java:402-411; ui/main/MainFragment.java:523-526')
e('MainFragment.onContextItemSelected', 'MainFragment.openTorrentFileDialog', 'CALL', 'Open torrent file picker from context menu',
  guard='itemId == R.id.open_file_menu', cls='explicit', evidence='SRC ui/main/MainFragment.java:402-411; ui/main/MainFragment.java:528-533')
e('MainFragment.initFabSpeedDial', 'MainFragment.lambda$initFabSpeedDial$11', 'REGISTER', 'Register floating action menu item callback',
  cls='non_standard', via='com.leinardi.android.speeddial', evidence='INFERRED SpeedDial library callback dispatch; SRC ui/main/MainFragment.java:414-431')
e('MainFragment.initFabSpeedDial', 'MainFragment.lambda$initFabSpeedDial$11', 'FRAMEWORK', 'Dispatch a selected floating action menu item',
  cls='non_standard', via='com.leinardi.android.speeddial', evidence='INFERRED SpeedDial library callback dispatch; SRC ui/main/MainFragment.java:414-431')
e('MainFragment.lambda$initFabSpeedDial$11', 'MainFragment.addLinkDialog', 'CALL', 'Open add-link dialog from floating action menu',
  guard='item.getId() == R.id.main_fab_add_link', cls='explicit', evidence='SRC ui/main/MainFragment.java:416-430; ui/main/MainFragment.java:523-526')
e('MainFragment.lambda$initFabSpeedDial$11', 'MainFragment.openTorrentFileDialog', 'CALL', 'Open torrent file dialog from floating action menu',
  guard='item.getId() == R.id.main_fab_open_file', cls='explicit', evidence='SRC ui/main/MainFragment.java:416-430; ui/main/MainFragment.java:528-533')
e('MainFragment.lambda$initFabSpeedDial$11', 'MainFragment.createTorrentDialog', 'CALL', 'Open create-torrent dialog from floating action menu',
  guard='item.getId() == R.id.main_fab_create_torrent', cls='explicit', evidence='SRC ui/main/MainFragment.java:416-430; ui/main/MainFragment.java:561-567')
e('AddTorrentActivity.observeDecodeState', 'AddTorrentActivity.lambda$observeDecodeState$1', 'REGISTER', 'Observe decode-state updates through LiveData',
  cls='non_standard', via='AndroidX LiveData', evidence='INFERRED AndroidX LiveData observer dispatch; SRC ui/addtorrent/AddTorrentActivity.java:305-327')
e('AddTorrentActivity.observeDecodeState', 'AddTorrentActivity.lambda$observeDecodeState$1', 'FRAMEWORK', 'Deliver decode-state updates to the activity observer',
  cls='non_standard', via='AndroidX LiveData', evidence='INFERRED AndroidX LiveData observer dispatch; SRC ui/addtorrent/AddTorrentActivity.java:305-327')
e('AddTorrentActivity.lambda$observeDecodeState$1', 'AddTorrentActivity.getUri', 'CALL', 'Read incoming torrent URI for initial decode',
  guard='state.status == UNKNOWN', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:307-313,350-360')
e('AddTorrentActivity.lambda$observeDecodeState$1', 'AddTorrentViewModel.startDecode', 'CALL', 'Start decode when an input URI is present',
  guard='state.status == UNKNOWN && uri != null', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:307-313; ui/addtorrent/AddTorrentViewModel.java:182-216')
e('AddTorrentActivity.lambda$observeDecodeState$1', 'AddTorrentActivity.onStartDecode', 'CALL', 'Show decoding progress for active fetch/decode states',
  guard='state.status is DECODE_TORRENT_FILE, FETCHING_HTTP, or FETCHING_MAGNET', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:314-318,329-334')
e('AddTorrentActivity.lambda$observeDecodeState$1', 'AddTorrentActivity.onStopDecode', 'CALL', 'Finish progress state for completed or failed decoding',
  guard='state.status is FETCHING_HTTP_COMPLETED, DECODE_TORRENT_COMPLETED, FETCHING_MAGNET_COMPLETED, or ERROR', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:319-327,336-348')
e('AddTorrentActivity.onStopDecode', 'AddTorrentViewModel.makeFileTree', 'CALL', 'Build file tree after successful decode',
  guard='e == null', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:340-347; ui/addtorrent/AddTorrentViewModel.java:368-390')
e('AddTorrentActivity.onStopDecode', 'AddTorrentActivity.handleDecodeException', 'CALL', 'Show decode or fetch error when the state contains a failure',
  guard='e != null', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:340-348,452-525')
e('AddTorrentActivity.onOptionsItemSelected', 'AddTorrentActivity.addTorrent', 'CALL', 'Add decoded torrent from action-bar menu',
  guard='itemId == R.id.add_torrent_dialog_add_menu', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:552-562; ui/addtorrent/AddTorrentActivity.java:362-389')
e('AddTorrentActivity.addTorrent', 'AddTorrentViewModel.addTorrent', 'CALL', 'Submit torrent using the add-torrent view model',
  guard='!TextUtils.isEmpty(name)', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:362-389; ui/addtorrent/AddTorrentViewModel.java:466-520')
e('AddTorrentActivity.addTorrent', 'AddTorrentActivity.finish', 'CALL', 'Finish after successful addition or duplicate torrent',
  guard='viewModel.addTorrent() returns true or exception is TorrentAlreadyExistsException', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:373-384; ui/addtorrent/AddTorrentActivity.java:565-570')
e('AddTorrentActivity.finish', 'AddTorrentViewModel.finish', 'CALL', 'Finish add-torrent view-model state',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:565-570')
e('AddTorrentActivity.onOptionsItemSelected', 'AddTorrentActivity.finish', 'CALL', 'Finish activity from action-bar home item',
  guard='itemId == android.R.id.home', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:552-561; ui/addtorrent/AddTorrentActivity.java:565-570')
e('AddTorrentActivity.onBackPressed', 'AddTorrentActivity.finish', 'CALL', 'Finish activity on back action',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:573-576,565-570')
e('AddTorrentActivity.onPrepareOptionsMenu', 'AddTorrentActivity.onOptionsItemSelected', 'REGISTER', 'Expose add and home menu actions to user selection',
  cls='standard', evidence='SRC ui/addtorrent/AddTorrentActivity.java:539-562; FW-SRC core/java/android/app/Activity.java:3388-3409,3439-3451; user menu selection')
e('AddTorrentActivity.addTorrent', 'AddTorrentActivity.handleAddException', 'CALL', 'Handle addition exceptions other than duplicate torrents',
  guard='viewModel.addTorrent() throws e && !(e instanceof TorrentAlreadyExistsException)', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:373-387,391-417')
e('AddTorrentActivity.handleAddException', 'AddTorrentActivity.showAddErrorDialog', 'CALL', 'Display add error for file, I/O, or other failures',
  guard='e instanceof FileNotFoundException || e instanceof IOException || other exception', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:391-417,419-450')
e('AddTorrentActivity.handleDecodeException', 'BaseAlertDialog.newInstance', 'CALL', 'Create decode, fetch, invalid-link, or oversized-file dialog',
  guard='e instanceof DecodeException || FetchLinkException || IllegalArgumentException || OutOfMemoryError, and matching dialog absent', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:452-525')
e('AddTorrentActivity.handleDecodeException', 'ErrorReportDialog.newInstance', 'CALL', 'Create report dialog for decode I/O failures',
  guard='e instanceof IOException && error report dialog absent', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:503-515')
e('AddTorrentViewModel.addTorrent', 'AddTorrentViewModel.lambda$addTorrent$5', 'REGISTER', 'Run synchronous engine insertion on a worker thread',
  cls='standard', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:520-544; Thread(Runnable).start()')
e('AddTorrentViewModel.addTorrent', 'AddTorrentViewModel.lambda$addTorrent$5', 'FRAMEWORK', 'Dispatch the worker thread Runnable after Thread.start()',
  cls='non_standard', via='java.lang.Thread', evidence='INFERRED java.lang.Thread Runnable dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:527-536')
e('AddTorrentViewModel.lambda$addTorrent$5', 'TorrentEngine.addTorrentSync(AddTorrentParams,boolean)', 'CALL', 'Insert torrent from the worker thread',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:527-534')
e('TorrentEngine.addTorrentSync(AddTorrentParams,boolean)', 'TorrentSessionImpl.addTorrent', 'CALL', 'Insert torrent into the concrete session when the engine is running',
  guard='isRunning()', needs_state='isRunning()', cls='explicit', evidence='SRC core/model/TorrentEngine.java:401-413,128-141; core/model/session/TorrentSessionImpl.java:251-260')
e('TorrentSessionImpl.addTorrent', 'TorrentSessionImpl.download(String,AddTorrentParams,byte[])', 'CALL', 'Begin download setup for the newly added torrent',
  guard='!operationNotAllowed() && torrent is not already present', cls='explicit', evidence='SRC core/model/session/TorrentSessionImpl.java:251-310')
e('TorrentSessionImpl.download(String,AddTorrentParams,byte[])', 'TorrentSessionImpl.download(TorrentInfo,File,Priority[],boolean,boolean,List)', 'CALL', 'Build libtorrent parameters from a local torrent file and its selected priorities',
  guard='!params.fromMagnet && !torrent.isDownloadingMetadata() && torrent file descriptor opens', cls='explicit', evidence='SRC core/model/session/TorrentSessionImpl.java:328-371')
e('TorrentSessionImpl.download(TorrentInfo,File,Priority[],boolean,boolean,List)', 'PriorityConverter.convert(Priority)#2', 'CALL', 'Convert each non-null selected file priority to the libtorrent priority enum',
  guard='priorities != null && ti.files().numFiles() == priorities.length && priority != null', cls='explicit', evidence='SRC core/model/session/TorrentSessionImpl.java:1541-1575; core/model/session/PriorityConverter.java:94-101; dst qualified to the :94 app->lib overload (build name #2) at b003 merge: the :1574 call passes app Priority and .swig()s a lib Priority; the bare form resolves to the :103 lib->app overload, which has zero callers')
e('AddTorrentViewModel.finish', 'AddTorrentViewModel.cancelFetchMagnet', 'CALL', 'Cancel an active magnet fetch when leaving the screen',
  guard='decodeState != null && decodeState.status == FETCHING_MAGNET', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:557-570')
e('AddTorrentActivity.initLayout', 'AddTorrentPagerAdapter.createFragment', 'FRAMEWORK', 'Create the selected add-torrent page on demand',
  cls='non_standard', via='AndroidX ViewPager2 / FragmentStateAdapter', evidence='INFERRED AndroidX pager adapter dispatch; SRC ui/addtorrent/AddTorrentActivity.java:288-303; ui/addtorrent/AddTorrentPagerAdapter.java:37-53')
e('AddTorrentPagerAdapter.createFragment', 'AddTorrentInfoFragment.newInstance', 'CALL', 'Create information page for pager position zero',
  guard='position == INFO_FRAG_POS', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentPagerAdapter.java:43-47')
e('AddTorrentPagerAdapter.createFragment', 'AddTorrentFilesFragment.newInstance', 'CALL', 'Create files page for pager position one',
  guard='position == FILES_FRAG_POS', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentPagerAdapter.java:43-49')
e('AddTorrentInfoFragment.newInstance', 'AddTorrentInfoFragment.<init>', 'CALL', 'Instantiate torrent information page',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:66-73')
e('AddTorrentFilesFragment.newInstance', 'AddTorrentFilesFragment.<init>', 'CALL', 'Instantiate torrent files page',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:62-69')
e('AddTorrentInfoFragment.newInstance', 'AddTorrentInfoFragment.onAttach', 'LIFECYCLE', 'Attach information page to add-torrent activity',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:66-90')
e('AddTorrentInfoFragment.onAttach', 'AddTorrentInfoFragment.onCreateView', 'LIFECYCLE', 'Inflate information page view',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:91-97')
e('AddTorrentInfoFragment.onCreateView', 'AddTorrentInfoFragment.onViewCreated', 'LIFECYCLE', 'Bind information page handlers after view inflation',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:91-121')
e('AddTorrentInfoFragment.onViewCreated', 'AddTorrentInfoFragment.onStart', 'LIFECYCLE', 'Start information page after view setup',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:98-128')
e('AddTorrentInfoFragment.onViewCreated', 'AddTorrentInfoFragment.showChooseDirDialog', 'REGISTER', 'Register folder chooser button click',
  cls='standard', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:99-106,192-213; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('AddTorrentInfoFragment.onViewCreated', 'AddTorrentInfoFragment$1.afterTextChanged', 'REGISTER', 'Register torrent name validation text watcher',
  cls='standard', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:106-119; Android TextWatcher callback interface')
e('AddTorrentInfoFragment$1.afterTextChanged', 'AddTorrentInfoFragment.checkNameField', 'CALL', 'Validate changed torrent name',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:115-119,231-240')
e('AddTorrentInfoFragment.onStart', 'AddTorrentInfoFragment.subscribeTags', 'CALL', 'Subscribe to tag list updates while page is started',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:123-128,186-190')
e('AddTorrentInfoFragment.subscribeTags', 'AddTorrentViewModel.observeTags', 'CALL', 'Observe the current torrent tags',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:186-190; ui/addtorrent/AddTorrentViewModel.java:145-154')
e('AddTorrentInfoFragment.subscribeTags', 'TorrentTagsList.submit', 'REGISTER', 'Submit tag updates through the Rx observer',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:186-190; ui/tag/TorrentTagsList.java:44-52')
e('AddTorrentInfoFragment.onViewCreated', 'AddTorrentInfoFragment.lambda$new$1', 'REGISTER', 'Register tag-selection activity result callback',
  cls='non_standard', via='AndroidX ActivityResult API', evidence='INFERRED AndroidX ActivityResult callback dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:137-148')
e('AddTorrentInfoFragment.lambda$new$1', 'AddTorrentViewModel.addTag', 'CALL', 'Add returned tag when selection result is valid',
  guard='resultCode == Activity.RESULT_OK && data != null && returned TagInfo != null', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:139-147')
e('AddTorrentInfoFragment.showChooseDirDialog', 'FileManagerDialog.<init>', 'INTENT', 'Launch directory chooser through ActivityResult launcher',
  cls='non_standard', via='AndroidX ActivityResult API', evidence='INFERRED AndroidX ActivityResult dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:192-213; AndroidManifest.xml:137-138')
e('AddTorrentInfoFragment.showChooseDirDialog', 'AddTorrentInfoFragment.lambda$new$2', 'REGISTER', 'Register directory chooser result callback',
  cls='non_standard', via='AndroidX ActivityResult API', evidence='INFERRED AndroidX ActivityResult callback dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:150-161')
e('AddTorrentInfoFragment.lambda$new$2', 'AddTorrentInfoFragment.showOpenDirErrorDialog', 'CALL', 'Report successful chooser result without a returned URI',
  guard='resultCode == Activity.RESULT_OK && (data == null || data.getData() == null)', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:152-161,215-233')
e('AddTorrentFilesFragment.newInstance', 'AddTorrentFilesFragment.onAttach', 'LIFECYCLE', 'Attach files page to add-torrent activity',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:62-93')
e('AddTorrentFilesFragment.onAttach', 'AddTorrentFilesFragment.onCreateView', 'LIFECYCLE', 'Inflate files page view',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:127-141')
e('AddTorrentFilesFragment.onCreateView', 'AddTorrentFilesFragment.onViewCreated', 'LIFECYCLE', 'Create file list and adapter after view inflation',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:127-141')
e('AddTorrentFilesFragment.onViewCreated', 'AddTorrentFilesFragment.onStart', 'LIFECYCLE', 'Start file list observation',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:103-141')
e('AddTorrentFilesFragment.onViewCreated', 'DownloadableFilesAdapter.<init>', 'CALL', 'Create downloadable file list adapter',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:128-141')
e('AddTorrentFilesFragment.onStart', 'AddTorrentFilesFragment.subscribeAdapter', 'CALL', 'Subscribe to visible file-tree children',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:103-124')
e('AddTorrentFilesFragment.subscribeAdapter', 'AddTorrentFilesFragment.lambda$subscribeAdapter$0', 'REGISTER', 'Map file-tree children into downloadable rows',
  cls='non_standard', via='RxJava Flowable.flatMapSingle/map', evidence='INFERRED RxJava operator dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:111-124')
e('AddTorrentFilesFragment.lambda$subscribeAdapter$0', 'DownloadableFileItem.<init>(BencodeFileTree)', 'CALL', 'Wrap each file-tree entry for display',
  cls='non_standard', via='RxJava Flowable.map method reference', evidence='INFERRED RxJava map dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:115-119')
e('AddTorrentFilesFragment.subscribeAdapter', 'AddTorrentFilesFragment.lambda$subscribeAdapter$1', 'REGISTER', 'Deliver converted file rows on the main thread',
  cls='non_standard', via='RxJava subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:120-124')
e('AddTorrentFilesFragment.lambda$subscribeAdapter$1', 'AddTorrentFilesFragment.updateFileSize', 'CALL', 'Update selected and total file sizes',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:121-124,143-153')
e('AddTorrentFilesFragment.onViewCreated', 'DownloadableFilesAdapter.onBindViewHolder', 'FRAMEWORK', 'Bind file rows through RecyclerView',
  cls='non_standard', via='AndroidX RecyclerView.Adapter', evidence='INFERRED AndroidX RecyclerView binding dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:137-141; ui/addtorrent/DownloadableFilesAdapter.java:51-58')
e('DownloadableFilesAdapter.onBindViewHolder', 'DownloadableFilesAdapter$ViewHolder.bind', 'CALL', 'Bind file row click and selection listeners',
  cls='explicit', evidence='SRC ui/addtorrent/DownloadableFilesAdapter.java:51-58,91-132')
e('DownloadableFilesAdapter$ViewHolder.bind', 'DownloadableFilesAdapter$ViewHolder.lambda$bind$0', 'REGISTER', 'Register file row click callback',
  cls='standard', evidence='SRC ui/addtorrent/DownloadableFilesAdapter.java:93-102; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('DownloadableFilesAdapter$ViewHolder.bind', 'DownloadableFilesAdapter$ViewHolder.lambda$bind$1', 'REGISTER', 'Register file selection checkbox callback',
  cls='standard', evidence='SRC ui/addtorrent/DownloadableFilesAdapter.java:103-106; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('DownloadableFilesAdapter$ViewHolder.lambda$bind$0', 'AddTorrentFilesFragment.onItemClicked', 'CALL', 'Handle clicked file or directory',
  cls='explicit', evidence='SRC ui/addtorrent/DownloadableFilesAdapter.java:93-102; ui/addtorrent/AddTorrentFilesFragment.java:182-189')
e('DownloadableFilesAdapter$ViewHolder.lambda$bind$1', 'AddTorrentFilesFragment.onItemCheckedChanged', 'CALL', 'Handle changed file selection',
  cls='explicit', evidence='SRC ui/addtorrent/DownloadableFilesAdapter.java:103-106; ui/addtorrent/AddTorrentFilesFragment.java:191-196')
e('AddTorrentFilesFragment.onItemClicked', 'AddTorrentViewModel.upToParentDirectory', 'CALL', 'Navigate to parent directory row',
  guard='item.name.equals(BencodeFileTree.PARENT_DIR)', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:182-189; ui/addtorrent/AddTorrentViewModel.java:403-409')
e('AddTorrentFilesFragment.onItemClicked', 'AddTorrentViewModel.chooseDirectory', 'CALL', 'Enter clicked directory',
  guard='!item.name.equals(BencodeFileTree.PARENT_DIR) && !item.isFile', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:182-189; ui/addtorrent/AddTorrentViewModel.java:425-434')
e('AddTorrentFilesFragment.onItemCheckedChanged', 'AddTorrentViewModel.selectFile', 'CALL', 'Update selected state for clicked file row',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:191-196; ui/addtorrent/AddTorrentViewModel.java:436-443')
e('AddLinkActivity.onCreate', 'AddLinkDialog.newInstance', 'CALL', 'Create add-link dialog when activity has no saved instance',
  guard='findFragmentByTag(TAG_ADD_LINK_DIALOG) == null', cls='explicit', evidence='SRC ui/addlink/AddLinkActivity.java:21-37; ui/addlink/AddLinkDialog.java:73-81')
e('AddLinkDialog.newInstance', 'AddLinkDialog.<init>', 'CALL', 'Instantiate add-link dialog fragment',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:73-81')
e('AddLinkDialog.newInstance', 'AddLinkDialog.onAttach', 'LIFECYCLE', 'Attach add-link dialog to its activity',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/addlink/AddLinkDialog.java:73-90')
e('AddLinkDialog.onAttach', 'AddLinkDialog.onCreateDialog', 'LIFECYCLE', 'Create add-link dialog view and model',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/addlink/AddLinkDialog.java:169-192')
e('AddLinkDialog.onCreateDialog', 'AddLinkDialog.onStart', 'LIFECYCLE', 'Start add-link dialog after creation',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/addlink/AddLinkDialog.java:121-128,169-192')
e('AddLinkDialog.onCreateDialog', 'AddLinkDialog.initLayoutView', 'CALL', 'Register input, clipboard, and dialog controls',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:171-191,202-226')
e('AddLinkDialog.initLayoutView', 'AddLinkDialog.lambda$initLayoutView$3', 'REGISTER', 'Register clipboard dialog button handler',
  cls='standard', evidence='SRC ui/addlink/AddLinkDialog.java:221; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('AddLinkDialog.lambda$initLayoutView$3', 'AddLinkDialog.showClipboardDialog', 'CALL', 'Open clipboard picker when its button is tapped',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:221,248-258')
e('AddLinkDialog.initLayoutView', 'AddLinkDialog.initAlertDialog', 'CALL', 'Create add and cancel dialog buttons',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:221-226,228-246')
e('AddLinkDialog.initAlertDialog', 'AddLinkDialog.lambda$initAlertDialog$6', 'REGISTER', 'Register dialog shown callback to attach button actions',
  cls='standard', evidence='SRC ui/addlink/AddLinkDialog.java:228-246; Android DialogInterface.OnShowListener callback')
e('AddLinkDialog.lambda$initAlertDialog$6', 'AddLinkDialog.lambda$initAlertDialog$4', 'REGISTER', 'Register positive add button click',
  cls='standard', evidence='SRC ui/addlink/AddLinkDialog.java:238-241; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('AddLinkDialog.lambda$initAlertDialog$6', 'AddLinkDialog.lambda$initAlertDialog$5', 'REGISTER', 'Register cancel button click',
  cls='standard', evidence='SRC ui/addlink/AddLinkDialog.java:242-245; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('AddLinkDialog.lambda$initAlertDialog$4', 'AddLinkDialog.addLink', 'CALL', 'Validate and submit the typed torrent URL',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:238-241,260-288')
e('AddLinkDialog.lambda$initAlertDialog$5', 'AddLinkDialog.finish', 'CALL', 'Finish add-link dialog on cancel',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:242-245,299-304')
e('AddLinkDialog.addLink', 'AddLinkDialog.checkUrlField', 'CALL', 'Reject empty URL before normalization',
  guard='!TextUtils.isEmpty(viewModel.link.get())', cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:260-281,290-297')
e('AddLinkDialog.addLink', 'AddLinkViewModel.normalizeUrl', 'CALL', 'Normalize a non-empty validated link',
  guard='checkUrlField() returns true', cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:266-281; ui/addlink/AddLinkViewModel.java:61-73')
e('AddLinkDialog.addLink', 'AddTorrentActivity.<init>', 'INTENT', 'Open add-torrent activity for normalized link',
  guard='normalizeUrl succeeds', cls='standard', evidence='SRC ui/addlink/AddLinkDialog.java:272-287; AndroidManifest.xml:62-92; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('AddLinkDialog.addLink', 'AddLinkDialog.finish', 'CALL', 'Dismiss add-link dialog after successful handoff',
  guard='normalizeUrl succeeds', cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:283-288,299-304')
e('AddLinkDialog.finish', 'AddLinkActivity.onFragmentFinished', 'CALL', 'Notify host activity that add-link dialog finished',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:299-304; ui/addlink/AddLinkActivity.java:40-43')
e('AddLinkActivity.onBackPressed', 'AddLinkDialog.onBackPressed', 'CALL', 'Forward back action to add-link dialog',
  cls='explicit', evidence='SRC ui/addlink/AddLinkActivity.java:46-49; ui/addlink/AddLinkDialog.java:294-297')
e('AddLinkDialog.onStart', 'AddLinkDialog.subscribeClipboardManager', 'CALL', 'Listen for clipboard changes while dialog is started',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:121-128,148-156')
e('AddLinkDialog.onStart', 'AddLinkDialog.subscribeAlertDialog', 'CALL', 'Subscribe to clipboard dialog selection events',
  cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:121-137')
e('AddLinkDialog.subscribeAlertDialog', 'AddLinkDialog.lambda$subscribeAlertDialog$1', 'REGISTER', 'Observe clipboard item events through Rx',
  cls='non_standard', via='RxJava', evidence='INFERRED RxJava subscription dispatch; SRC ui/addlink/AddLinkDialog.java:130-137')
e('AddLinkDialog.lambda$subscribeAlertDialog$1', 'AddLinkDialog.handleUrlClipItem', 'CALL', 'Use selected clipboard text when the item belongs to this dialog',
  guard='item.dialogTag == TAG_CLIPBOARD_DIALOG', cls='explicit', evidence='SRC ui/addlink/AddLinkDialog.java:132-135,139-146')
e('AddLinkDialog.handleUrlClipItem', 'AddLinkDialog.addLink', 'REGISTER', 'Submit clipboard URL after the field update delay',
  guard='!TextUtils.isEmpty(item)', cls='standard', evidence='SRC ui/addlink/AddLinkDialog.java:139-146; View.postDelayed callback')
e('AddTagActivity.onCreate', 'AddTagDialog.newInstance', 'CALL', 'Create add or edit tag dialog when absent after recreation',
  guard='findFragmentByTag(TAG_DIALOG) == null', cls='explicit', evidence='SRC ui/addtag/AddTagActivity.java:51-69; ui/addtag/AddTagDialog.java:59-68')
e('AddTagDialog.newInstance', 'AddTagDialog.<init>', 'CALL', 'Instantiate tag editor dialog',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:59-68')
e('AddTagDialog.newInstance', 'AddTagDialog.onAttach', 'LIFECYCLE', 'Attach tag editor to host activity',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/addtag/AddTagDialog.java:59-84')
e('AddTagDialog.onAttach', 'AddTagDialog.onCreateDialog', 'LIFECYCLE', 'Create tag editor dialog and initialize tag state',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/addtag/AddTagDialog.java:112-152')
e('AddTagDialog.onCreateDialog', 'AddTagDialog.onResume', 'LIFECYCLE', 'Install dialog key handling when tag editor becomes active',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/addtag/AddTagDialog.java:86-101,112-152')
e('AddTagDialog.onResume', 'AddTagDialog.onStop', 'LIFECYCLE', 'Dispose tag editor work when its dialog stops',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/addtag/AddTagDialog.java:86-108')
e('AddTagDialog.onResume', 'AddTagDialog.lambda$onResume$0', 'REGISTER', 'Register the dialog key listener for back handling',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:87-101; FW-SRC core/java/android/app/Dialog.java:1346-1347')
e('AddTagDialog.onResume', 'AddTagDialog.lambda$onResume$0', 'FRAMEWORK', 'Dispatch key events to the dialog key listener',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:87-101; FW-SRC core/java/android/app/Dialog.java:776')
e('AddTagDialog.lambda$onResume$0', 'AddTagDialog.onBackPressed', 'CALL', 'Close the tag editor when Back is pressed',
  guard='keyCode == KEYCODE_BACK && event.action == ACTION_DOWN', cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:91-100,225-227')
e('AddTagDialog.onCreateDialog', 'AddTagViewModel.setInitValues', 'CALL', 'Load existing tag values when editing a tag',
  guard='initInfo != null', cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:123-135; ui/addtag/AddTagViewModel.java:45-49')
e('AddTagDialog.onCreateDialog', 'AddTagViewModel.setRandomColor', 'CALL', 'Choose initial random color for a new tag without a saved color',
  guard='initInfo == null && viewModel.state.getColor() == -1', cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:123-135; ui/addtag/AddTagViewModel.java:51-53')
e('AddTagDialog.onCreateDialog', 'AddTagDialog.initLayoutView', 'CALL', 'Register tag name and color controls',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:137-152')
e('AddTagDialog.onCreateDialog', 'AddTagDialog.initAlertDialog', 'CALL', 'Create tag add/edit and cancel actions',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:150-152,180-202')
e('AddTagDialog.initLayoutView', 'AddTagDialog$1.afterTextChanged', 'REGISTER', 'Clear name error after user edits tag text',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:155-171; Android TextWatcher callback')
e('AddTagDialog.initLayoutView', 'AddTagDialog.lambda$initLayoutView$1', 'REGISTER', 'Register color picker click',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:172-176; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('AddTagDialog.lambda$initLayoutView$1', 'AddTagActivity.onColorSelected', 'FRAMEWORK', 'Receive selected tag color from color picker library',
  cls='non_standard', via='ColorPickerDialog listener', evidence='INFERRED color picker listener dispatch; SRC ui/addtag/AddTagDialog.java:172-176; ui/addtag/AddTagActivity.java:79-81')
e('AddTagDialog.initLayoutView', 'AddTagDialog.lambda$initLayoutView$1', 'FRAMEWORK', 'Dispatch color picker button click',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:172-176; FW-SRC core/java/android/view/View.java:6289-6305')
e('AddTagActivity.onColorSelected', 'AddTagState.setColor', 'CALL', 'Apply chosen color to tag state',
  cls='explicit', evidence='SRC ui/addtag/AddTagActivity.java:79-81; ui/addtag/AddTagViewModel.java:36')
e('AddTagDialog.initAlertDialog', 'AddTagDialog.lambda$initAlertDialog$4', 'REGISTER', 'Register shown callback to attach tag dialog button handlers',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:180-202; Android DialogInterface.OnShowListener callback')
e('AddTagDialog.initAlertDialog', 'AddTagDialog.lambda$initAlertDialog$4', 'FRAMEWORK', 'Run the dialog shown callback after display',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:180-202; FW-SRC core/java/android/app/Dialog.java:1294-1302,1358-1367')
e('AddTagDialog.lambda$initAlertDialog$4', 'AddTagDialog.lambda$initAlertDialog$2', 'REGISTER', 'Register positive tag save button',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:190-194; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('AddTagDialog.lambda$initAlertDialog$4', 'AddTagDialog.lambda$initAlertDialog$3', 'REGISTER', 'Register cancel button',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:195-199; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('AddTagDialog.lambda$initAlertDialog$4', 'AddTagDialog.lambda$initAlertDialog$2', 'FRAMEWORK', 'Dispatch positive tag dialog button click',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:190-194; FW-SRC core/java/android/view/View.java:6289-6305')
e('AddTagDialog.lambda$initAlertDialog$4', 'AddTagDialog.lambda$initAlertDialog$3', 'FRAMEWORK', 'Dispatch cancel tag dialog button click',
  cls='standard', evidence='SRC ui/addtag/AddTagDialog.java:195-199; FW-SRC core/java/android/view/View.java:6289-6305')
e('AddTagDialog.lambda$initAlertDialog$2', 'AddTagDialog.addTag', 'CALL', 'Save tag after positive action',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:190-194,204-240')
e('AddTagDialog.lambda$initAlertDialog$3', 'AddTagDialog.finish', 'CALL', 'Close tag editor on cancel',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:195-199,253-260')
e('AddTagDialog.addTag', 'AddTagDialog.checkName', 'CALL', 'Validate tag name before saving',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:204-210,178-188')
e('AddTagDialog.addTag', 'AddTagViewModel.saveTag', 'CALL', 'Persist tag after name validation succeeds',
  guard='checkName() returns true', cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:204-215; ui/addtag/AddTagViewModel.java:55-75')
e('AddTagDialog.addTag', 'AddTagDialog.lambda$addTag$5', 'REGISTER', 'Finish dialog after save completes successfully',
  cls='non_standard', via='RxJava Completable.subscribe', evidence='INFERRED RxJava completion dispatch; SRC ui/addtag/AddTagDialog.java:211-239')
e('AddTagDialog.addTag', 'AddTagDialog.lambda$addTag$6', 'REGISTER', 'Show save error when tag persistence fails',
  cls='non_standard', via='RxJava Completable.subscribe', evidence='INFERRED RxJava error dispatch; SRC ui/addtag/AddTagDialog.java:211-239')
e('AddTagDialog.addTag', 'AddTagDialog.lambda$addTag$5', 'FRAMEWORK', 'Deliver successful tag save completion',
  cls='non_standard', via='RxJava Completable.subscribe', evidence='INFERRED RxJava Completable completion dispatch; SRC ui/addtag/AddTagDialog.java:211-239')
e('AddTagDialog.addTag', 'AddTagDialog.lambda$addTag$6', 'FRAMEWORK', 'Deliver tag persistence error',
  cls='non_standard', via='RxJava Completable.subscribe', evidence='INFERRED RxJava Completable error dispatch; SRC ui/addtag/AddTagDialog.java:211-239')
e('AddTagDialog.lambda$addTag$5', 'AddTagDialog.finish', 'CALL', 'Return success after saving tag',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:211-239,253-260')
e('AddTagDialog.finish', 'AddTagActivity.onFragmentFinished', 'CALL', 'Close tag activity after dialog completion',
  cls='explicit', evidence='SRC ui/addtag/AddTagDialog.java:253-260; ui/addtag/AddTagActivity.java:72-76')
e('AddTagActivity.onBackPressed', 'AddTagDialog.onBackPressed', 'CALL', 'Forward back press to tag editor dialog',
  cls='explicit', evidence='SRC ui/addtag/AddTagActivity.java:77-78; ui/addtag/AddTagDialog.java:249-251')
e('AddTorrentInfoFragment.onViewCreated', 'TorrentTagsList.setListener', 'CALL', 'Install tag add/remove callbacks on tag chip list',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:98-121; ui/tag/TorrentTagsList.java:40-42')
e('TorrentTagsList.buildAddTagButton', 'TorrentTagsList.lambda$buildAddTagButton$1', 'REGISTER', 'Register add-tag chip click listener',
  cls='standard', evidence='SRC ui/tag/TorrentTagsList.java:78-86; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('TorrentTagsList.lambda$buildAddTagButton$1', 'AddTorrentInfoFragment$2.onAddTagClick', 'CALL', 'Handle the add-tag chip action',
  cls='explicit', evidence='SRC ui/tag/TorrentTagsList.java:80-84; ui/addtorrent/AddTorrentInfoFragment.java:163-178')
e('TorrentTagsList.buildChip', 'TorrentTagsList.lambda$buildChip$0', 'REGISTER', 'Register tag chip removal action',
  cls='non_standard', via='Material Chip close-icon callback', evidence='INFERRED Material Chip close-icon callback dispatch; SRC ui/tag/TorrentTagsList.java:54-75')
e('TorrentTagsList.lambda$buildChip$0', 'AddTorrentInfoFragment$2.onTagRemoved', 'CALL', 'Handle removal of a torrent tag',
  cls='explicit', evidence='SRC ui/tag/TorrentTagsList.java:69-73; ui/addtorrent/AddTorrentInfoFragment.java:180-183')
e('AddTorrentInfoFragment$2.onAddTagClick', 'AddTorrentInfoFragment$2.lambda$onAddTagClick$0', 'REGISTER', 'Map current tags to IDs before selecting another tag',
  cls='non_standard', via='RxJava Observable.map', evidence='INFERRED RxJava operator dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:165-177')
e('AddTorrentInfoFragment$2.onAddTagClick', 'AddTorrentInfoFragment$2.lambda$onAddTagClick$1', 'REGISTER', 'Launch tag selection after current tag IDs are collected',
  cls='non_standard', via='RxJava Observable.toList/subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:165-177')
e('AddTorrentInfoFragment$2.lambda$onAddTagClick$1', 'SelectTagActivity.<init>', 'RESULT', 'Open tag chooser for current torrent',
  cls='non_standard', via='AndroidX ActivityResult API', evidence='INFERRED AndroidX ActivityResult launch dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:169-176; AndroidManifest.xml:137-138')
e('AddTorrentInfoFragment$2.lambda$onAddTagClick$1', 'SelectTagActivity.onCreate', 'RESULT', 'Create tag chooser for current torrent',
  cls='non_standard', via='AndroidX ActivityResult API', evidence='INFERRED AndroidX ActivityResult launch dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:169-176; AndroidManifest.xml:137-138')
e('AddTorrentInfoFragment$2.onTagRemoved', 'AddTorrentViewModel.removeTag', 'CALL', 'Remove selected tag from add-torrent state',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:180-183; ui/addtorrent/AddTorrentViewModel.java:162-165')
e('SelectTagActivity.onCreate', 'SelectTagDialog.newInstance', 'CALL', 'Create tag chooser dialog if no saved dialog exists',
  guard='findFragmentByTag(TAG_DIALOG) == null', cls='explicit', evidence='SRC ui/tag/SelectTagActivity.java:35-51; ui/tag/SelectTagDialog.java:60-70')
e('SelectTagDialog.newInstance', 'SelectTagDialog.<init>', 'CALL', 'Instantiate tag chooser dialog',
  cls='explicit', evidence='SRC ui/tag/SelectTagDialog.java:60-70')
e('SelectTagDialog.newInstance', 'SelectTagDialog.onAttach', 'LIFECYCLE', 'Attach tag chooser dialog to activity',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/tag/SelectTagDialog.java:60-88')
e('SelectTagDialog.onAttach', 'SelectTagDialog.onCreateDialog', 'LIFECYCLE', 'Create tag chooser list and dialog controls',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/tag/SelectTagDialog.java:126-154')
e('SelectTagDialog.onCreateDialog', 'SelectTagViewModel.setExcludeTagsId', 'CALL', 'Exclude tags already selected for the torrent',
  guard='getArguments() != null', cls='explicit', evidence='SRC ui/tag/SelectTagDialog.java:120-125; ui/tag/SelectTagViewModel.java:47-56')
e('SelectTagDialog.onCreateDialog', 'tag.TagsAdapter.<init>', 'CALL', 'Create selection adapter',
  cls='explicit', evidence='SRC ui/tag/SelectTagDialog.java:126-154; ui/tag/TagsAdapter.java:34-42')
e('SelectTagDialog.onCreateDialog', 'SelectTagDialog.initLayoutView', 'CALL', 'Attach tag adapter to selection list',
  cls='explicit', evidence='SRC ui/tag/SelectTagDialog.java:142-154,156-160')
e('SelectTagDialog.onCreateDialog', 'SelectTagDialog.initAlertDialog', 'CALL', 'Create new-tag and cancel controls',
  cls='explicit', evidence='SRC ui/tag/SelectTagDialog.java:152-154,163-182')
e('SelectTagDialog.initAlertDialog', 'SelectTagDialog.lambda$initAlertDialog$3', 'REGISTER', 'Register dialog shown callback',
  cls='standard', evidence='SRC ui/tag/SelectTagDialog.java:163-182; Android DialogInterface.OnShowListener callback')
e('SelectTagDialog.lambda$initAlertDialog$3', 'SelectTagDialog.lambda$initAlertDialog$1', 'REGISTER', 'Register new-tag activity action',
  cls='standard', evidence='SRC ui/tag/SelectTagDialog.java:172-176; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('SelectTagDialog.lambda$initAlertDialog$3', 'SelectTagDialog.lambda$initAlertDialog$2', 'REGISTER', 'Register cancel action',
  cls='standard', evidence='SRC ui/tag/SelectTagDialog.java:177-180; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('SelectTagDialog.lambda$initAlertDialog$1', 'AddTagActivity.<init>', 'INTENT', 'Open new-tag editor from tag chooser',
  cls='standard', evidence='SRC ui/tag/SelectTagDialog.java:172-176; AndroidManifest.xml:165-168; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('SelectTagDialog.lambda$initAlertDialog$2', 'SelectTagDialog.finish', 'CALL', 'Dismiss tag chooser on cancel',
  cls='explicit', evidence='SRC ui/tag/SelectTagDialog.java:177-180,235-242')
e('SelectTagDialog.onStart', 'SelectTagDialog.subscribeTags', 'CALL', 'Observe tags while chooser is started',
  cls='explicit', evidence='SRC ui/tag/SelectTagDialog.java:103-111,184-197')
e('SelectTagDialog.subscribeTags', 'SelectTagViewModel.observeTags', 'CALL', 'Load tags for chooser list',
  cls='explicit', evidence='SRC ui/tag/SelectTagDialog.java:165-175; ui/tag/SelectTagViewModel.java:62-64')
e('SelectTagDialog.subscribeTags', 'SelectTagDialog.lambda$subscribeTags$4', 'REGISTER', 'Filter and convert tag updates using Rx',
  cls='non_standard', via='RxJava Flowable', evidence='INFERRED RxJava operator/subscription dispatch; SRC ui/tag/SelectTagDialog.java:184-197')
e('tag.TagsAdapter.onBindViewHolder', 'tag.TagsAdapter$ViewHolder.bind', 'CALL', 'Bind click handler for each selectable tag',
  cls='explicit', evidence='SRC ui/tag/TagsAdapter.java:57-63,98-109')
e('tag.TagsAdapter$ViewHolder.bind', 'tag.TagsAdapter$ViewHolder.lambda$bind$0', 'REGISTER', 'Register tag row click listener',
  cls='standard', evidence='SRC ui/tag/TagsAdapter.java:98-109; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('tag.TagsAdapter$ViewHolder.lambda$bind$0', 'SelectTagDialog.onTagClicked', 'CALL', 'Return clicked tag to activity',
  cls='explicit', evidence='SRC ui/tag/TagsAdapter.java:104-108; ui/tag/SelectTagDialog.java:199-207')
e('SelectTagDialog.onTagClicked', 'SelectTagDialog.finish', 'CALL', 'Finish selection dialog with selected tag result',
  cls='explicit', evidence='SRC ui/tag/SelectTagDialog.java:199-207,235-242')
e('SelectTagDialog.finish', 'SelectTagActivity.onFragmentFinished', 'CALL', 'Return tag selection result to host activity',
  cls='explicit', evidence='SRC ui/tag/SelectTagDialog.java:235-242; ui/tag/SelectTagActivity.java:54-64')
e('AddTorrentInfoFragment.showChooseDirDialog', 'FileManagerDialog.onCreate', 'INTENT', 'Create directory chooser for add-torrent destination selection',
  cls='non_standard', via='AndroidX ActivityResult API', evidence='INFERRED AndroidX ActivityResult launch dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:192-213; ui/filemanager/FileManagerDialog.java:119-140; AndroidManifest.xml:137-138')
e('FileManagerDialog.onCreate', 'FileManagerDialog.onStart', 'LIFECYCLE', 'Start file manager after activity creation',
  cls='standard', evidence='SRC ui/filemanager/FileManagerDialog.java:119-241,272-279; FW-SRC core/java/android/app/ActivityThread.java:2738-2745; core/java/android/app/Instrumentation.java:1333-1335')
e('FileManagerDialog.onCreate', 'FileManagerDialog.registerMediaReceiver', 'CALL', 'Register media mount/unmount receiver',
  cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:119-241,281-287')
e('FileManagerDialog.onCreate', 'FileManagerDialog.lambda$onCreate$0', 'REGISTER', 'Register create-folder floating action button',
  cls='standard', evidence='SRC ui/filemanager/FileManagerDialog.java:168-173,243-255; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('FileManagerDialog.lambda$onCreate$0', 'FileManagerDialog.showInputNameDialog', 'CALL', 'Open new-folder name dialog',
  cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:172-173,243-255')
e('FileManagerDialog.onCreate', 'FileManagerAdapter.<init>', 'CALL', 'Create file list adapter with activity click listener',
  cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:192-199; ui/filemanager/FileManagerAdapter.java:50-61')
e('FileManagerDialog.onStart', 'FileManagerDialog.subscribeAlertDialog', 'CALL', 'Subscribe to file manager dialog events',
  cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:272-279,297-300')
e('FileManagerDialog.onStart', 'FileManagerDialog.subscribeAdapter', 'CALL', 'Subscribe to current directory children',
  cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:272-279,302-309')
e('FileManagerDialog.subscribeAdapter', 'FileManagerDialog.lambda$subscribeAdapter$1', 'REGISTER', 'Submit directory list updates to the adapter',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava callback dispatch; SRC ui/filemanager/FileManagerDialog.java:302-309')
e('FileManagerDialog.lambda$subscribeAdapter$1', 'FileManagerAdapter.submitList', 'CALL', 'Display current file manager rows',
  cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:302-309; ui/filemanager/FileManagerAdapter.java:88-94')
e('FileManagerDialog.onCreate', 'FileManagerAdapter.onBindViewHolder', 'FRAMEWORK', 'Bind file manager rows through RecyclerView',
  cls='non_standard', via='AndroidX RecyclerView.Adapter', evidence='INFERRED RecyclerView binding dispatch; SRC ui/filemanager/FileManagerDialog.java:192-199; ui/filemanager/FileManagerAdapter.java:81-85')
e('FileManagerDialog.onCreate', 'FileManagerAdapter.onCreateViewHolder', 'FRAMEWORK', 'Create file manager row views when entries exist',
  needs_state='adapter.getItemCount() > 0', cls='non_standard', via='AndroidX RecyclerView.Adapter', evidence='INFERRED RecyclerView row creation dispatch; SRC ui/filemanager/FileManagerDialog.java:192-199; ui/filemanager/FileManagerAdapter.java:73-79')
e('FileManagerAdapter.onBindViewHolder', 'FileManagerAdapter$ViewHolder.bind', 'CALL', 'Bind file row and click handler',
  cls='explicit', evidence='SRC ui/filemanager/FileManagerAdapter.java:81-85,126-134')
e('FileManagerAdapter$ViewHolder.bind', 'FileManagerAdapter$ViewHolder.lambda$bind$0', 'REGISTER', 'Register file row click',
  cls='standard', evidence='SRC ui/filemanager/FileManagerAdapter.java:126-134; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('FileManagerAdapter$ViewHolder.bind', 'FileManagerAdapter$ViewHolder.lambda$bind$0', 'FRAMEWORK', 'Dispatch taps on file manager rows',
  cls='standard', evidence='SRC ui/filemanager/FileManagerAdapter.java:126-134; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('FileManagerAdapter$ViewHolder.lambda$bind$0', 'FileManagerDialog.onItemClicked', 'CALL', 'Handle file or directory row selection',
  cls='explicit', evidence='SRC ui/filemanager/FileManagerAdapter.java:130-133; ui/filemanager/FileManagerDialog.java:430-457')
e('FileManagerDialog.onItemClicked', 'FileManagerViewModel.upToParentDirectory', 'CALL', 'Navigate to parent directory',
  guard='item.getName().equals(FileManagerNode.PARENT_DIR)', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:430-439; ui/filemanager/FileManagerViewModel.java:206-217')
e('FileManagerDialog.onItemClicked', 'FileManagerViewModel.openDirectory', 'CALL', 'Open selected directory',
  guard='item.getType() == DIR', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:441-450; ui/filemanager/FileManagerViewModel.java:173-184')
e('FileManagerDialog.onItemClicked', 'FileManagerDialog.returnFileUri', 'CALL', 'Return selected file in file chooser mode',
  guard='item.getType() == FILE && showMode == FILE_CHOOSER_MODE', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:452-456,593-604')
e('FileManagerDialog.onCreate', 'FileManagerDialog.onCreateOptionsMenu', 'FRAMEWORK', 'Create file manager toolbar menu',
  cls='standard', evidence='SRC ui/filemanager/FileManagerDialog.java:474-481; FW-SRC core/java/android/app/Activity.java:3383-3391')
e('FileManagerDialog.onCreateOptionsMenu', 'FileManagerDialog.onPrepareOptionsMenu', 'FRAMEWORK', 'Prepare toolbar actions for file manager mode',
  cls='standard', evidence='SRC ui/filemanager/FileManagerDialog.java:474-491; FW-SRC core/java/android/app/Activity.java:3399-3410')
e('FileManagerDialog.onPrepareOptionsMenu', 'FileManagerDialog.onOptionsItemSelected', 'REGISTER', 'Expose toolbar actions for user selection',
  cls='standard', evidence='SRC ui/filemanager/FileManagerDialog.java:483-515; FW-SRC core/java/android/app/Activity.java:3439-3451; user menu selection')
e('FileManagerDialog.onPrepareOptionsMenu', 'FileManagerDialog.onOptionsItemSelected', 'FRAMEWORK', 'Dispatch selected file manager toolbar actions',
  cls='standard', evidence='SRC ui/filemanager/FileManagerDialog.java:483-515; FW-SRC core/java/android/app/Activity.java:3439-3451')
e('FileManagerDialog.onOptionsItemSelected', 'FileManagerDialog.openHomeDirectory', 'CALL', 'Navigate to user home folder',
  guard='itemId == R.id.filemanager_home_menu', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:499-515,518-522')
e('FileManagerDialog.onOptionsItemSelected', 'FileManagerDialog.returnDirectoryUri', 'CALL', 'Return selected directory from chooser mode',
  guard='itemId == R.id.filemanager_ok_menu && showMode != SAVE_FILE_MODE', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:499-515,557-568')
e('FileManagerDialog.onOptionsItemSelected', 'FileManagerDialog.createFile', 'CALL', 'Create selected output file in save mode',
  guard='itemId == R.id.filemanager_ok_menu && showMode == SAVE_FILE_MODE', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:499-515,570-591')
e('FileManagerDialog.onOptionsItemSelected', 'FileManagerDialog.goToDirectoryDialog', 'CALL', 'Open direct path dialog',
  guard='itemId == R.id.filemanager_go_to_folder_menu', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:499-515,548-555')
e('FileManagerDialog.showInputNameDialog', 'BaseAlertDialog.newInstance', 'CALL', 'Create folder-name input dialog',
  guard='input dialog not already shown', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:243-255')
e('FileManagerDialog.handleAlertDialogEvent', 'FileManagerViewModel.createDirectory', 'CALL', 'Create requested folder after positive confirmation',
  guard='event is positive for TAG_INPUT_NAME_DIALOG && dialog != null', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:319-345; ui/filemanager/FileManagerViewModel.java:163-171')
e('FileManagerDialog.handleAlertDialogEvent', 'FileManagerDialog.createFile', 'CALL', 'Replace existing output after positive confirmation',
  guard='event is positive for TAG_REPLACE_FILE_DIALOG', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:323-349,570-591')
e('FileManagerDialog.createFile', 'FileManagerViewModel.fileExists', 'CALL', 'Check whether output file already exists',
  guard='!replace && checkFileNameField()', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:570-578; ui/filemanager/FileManagerViewModel.java:219-227')
e('FileManagerDialog.createFile', 'FileManagerViewModel.createFile', 'CALL', 'Create file after confirmation or when no target exists',
  guard='checkFileNameField() && (replace || !viewModel.fileExists(fileName))', cls='explicit', evidence='SRC ui/filemanager/FileManagerDialog.java:570-590; ui/filemanager/FileManagerViewModel.java:248-260')
e('DetailTorrentActivity.onCreate', 'DetailTorrentActivity.onStart', 'LIFECYCLE', 'Start detail activity after successful setup',
  guard='!Utils.isTwoPane(this)', cls='standard', evidence='SRC ui/detailtorrent/DetailTorrentActivity.java:52-77,87-93; FW-SRC core/java/android/app/ActivityThread.java:2738-2745; core/java/android/app/Instrumentation.java:1333-1335')
e('DetailTorrentActivity.onStart', 'DetailTorrentActivity.onStop', 'LIFECYCLE', 'Stop the detail activity after it leaves the started foreground state',
  cls='standard', evidence='FW-SRC core/java/android/app/Activity.java:7130-7182; core/java/android/app/Instrumentation.java:1374-1376; SRC ui/detailtorrent/DetailTorrentActivity.java:79-93')
e('DetailTorrentActivity.onCreate', 'DetailTorrentFragment.<init>', 'FRAMEWORK', 'Inflate detail fragment from activity layout',
  guard='!Utils.isTwoPane(this)', cls='non_standard', via='AndroidX Fragment layout inflation', evidence='INFERRED AndroidX Fragment inflater dispatch; SRC ui/detailtorrent/DetailTorrentActivity.java:63-71; res/layout/activity_detail_torrent.xml:7-13')
e('DetailTorrentActivity.onCreate', 'DetailTorrentFragment.setTorrentId', 'CALL', 'Pass selected torrent ID to detail fragment',
  guard='detailTorrentFragment != null', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentActivity.java:67-72')
e('DetailTorrentActivity.onCreate', 'DetailTorrentFragment.showFiles', 'CALL', 'Show file tab for a file-open notification action',
  guard='ACTION_OPEN_FILES.equals(getIntent().getAction()) && detailTorrentFragment != null', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentActivity.java:73-76')
e('DetailTorrentActivity.onStart', 'DetailTorrentActivity.subscribeTorrentDeleted', 'CALL', 'Observe torrent deletion while detail page is visible',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentActivity.java:87-105')
e('DetailTorrentActivity.subscribeTorrentDeleted', 'DetailTorrentActivity.lambda$subscribeTorrentDeleted$0', 'REGISTER', 'Observe deletion events through Rx',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava subscription dispatch; SRC ui/detailtorrent/DetailTorrentActivity.java:95-105')
e('DetailTorrentActivity.subscribeTorrentDeleted', 'DetailTorrentActivity.lambda$subscribeTorrentDeleted$0', 'FRAMEWORK', 'Deliver torrent deletion events to the activity observer',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/detailtorrent/DetailTorrentActivity.java:95-105')
e('DetailTorrentFragment.newInstance', 'DetailTorrentFragment.<init>', 'CALL', 'Instantiate detail fragment for selected torrent',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:115-122')
e('DetailTorrentFragment.newInstance', 'DetailTorrentFragment.setTorrentId', 'CALL', 'Set requested torrent ID on new fragment',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:115-122,129-132')
e('DetailTorrentFragment.<init>', 'DetailTorrentFragment.onAttach', 'LIFECYCLE', 'Attach detail fragment to selected host activity',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:138-145')
e('DetailTorrentFragment.onAttach', 'DetailTorrentFragment.onCreateView', 'LIFECYCLE', 'Inflate detail view',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:147-153')
e('DetailTorrentFragment.onCreateView', 'DetailTorrentFragment.onViewCreated', 'LIFECYCLE', 'Initialize detail toolbar and page tabs',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:155-221')
e('DetailTorrentFragment.onViewCreated', 'DetailTorrentFragment.onStart', 'LIFECYCLE', 'Start detail page subscriptions',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:223-232')
e('DetailTorrentFragment.onViewCreated', 'DetailTorrentFragment.onCreateOptionsMenu', 'FRAMEWORK', 'Create the detail menu in single-pane activity mode',
  guard='!Utils.isTwoPane(activity)', cls='non_standard', via='AndroidX FragmentManager options-menu dispatch', evidence='INFERRED AndroidX Fragment options-menu dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:176-181,413-418')
e('DetailTorrentFragment.onCreateOptionsMenu', 'DetailTorrentFragment.onPrepareOptionsMenu', 'FRAMEWORK', 'Prepare the detail menu after it is created',
  cls='non_standard', via='AndroidX FragmentManager options-menu dispatch', evidence='INFERRED AndroidX Fragment options-menu dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:413-425')
e('DetailTorrentFragment.onPrepareOptionsMenu', 'DetailTorrentFragment.prepareOptionsMenu', 'CALL', 'Set menu visibility and pause/resume presentation from current torrent state',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:421-449')
e('DetailTorrentFragment.onCreateOptionsMenu', 'DetailTorrentFragment.onOptionsItemSelected', 'FRAMEWORK', 'Dispatch selected single-pane detail menu actions to the fragment',
  cls='non_standard', via='AndroidX FragmentManager options-menu dispatch', evidence='INFERRED AndroidX Fragment options-menu dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:176-181,413-475')
e('DetailTorrentFragment.onViewCreated', 'DetailTorrentFragment.onOptionsItemSelected', 'REGISTER', 'Register the detail toolbar menu callback in two-pane mode',
  guard='Utils.isTwoPane(activity)', cls='non_standard', via='AndroidX Toolbar', evidence='INFERRED AppCompat Toolbar callback dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:170-175,452-475')
e('DetailTorrentFragment.onViewCreated', 'DetailTorrentFragment.onOptionsItemSelected', 'FRAMEWORK', 'Dispatch two-pane toolbar selections to the detail fragment',
  guard='Utils.isTwoPane(activity)', cls='non_standard', via='AndroidX Toolbar', evidence='INFERRED AppCompat Toolbar callback dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:170-175,452-475')
e('DetailTorrentFragment.onViewCreated', 'DetailTorrentFragment.onBackPressed', 'REGISTER', 'Register the detail toolbar navigation click callback',
  cls='standard', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:183,822-825; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('DetailTorrentFragment.onViewCreated', 'DetailTorrentFragment.onBackPressed', 'FRAMEWORK', 'Dispatch detail toolbar navigation clicks to the fragment',
  cls='standard', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:183,822-825; FW-SRC core/java/android/view/View.java:6289-6305')
e('DetailTorrentFragment.onBackPressed', 'DetailTorrentFragment.finish', 'CALL', 'Finish the detail fragment with a Back result',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:822-825,827-831')
e('DetailTorrentFragment.finish', 'MainActivity.onFragmentFinished', 'CALL', 'Return detail-fragment completion to the two-pane host',
  guard='activity instanceof MainActivity', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:827-831; ui/main/MainActivity.java:805-810')
e('DetailTorrentFragment.finish', 'DetailTorrentActivity.onFragmentFinished', 'CALL', 'Return detail-fragment completion to the single-pane host',
  guard='activity instanceof DetailTorrentActivity', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:827-831; ui/detailtorrent/DetailTorrentActivity.java:107-113')
e('DetailTorrentFragment.onOptionsItemSelected', 'DetailTorrentFragment.onBackPressed', 'CALL', 'Return to the prior screen from the toolbar home action',
  guard='itemId == android.R.id.home', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:452-475,822-825')
e('DetailTorrentFragment.onOptionsItemSelected', 'DetailTorrentViewModel.pauseResumeTorrent', 'CALL', 'Pause or resume the displayed torrent from the detail menu',
  guard='itemId == R.id.pause_resume_torrent_menu', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:452-459')
e('DetailTorrentFragment.onOptionsItemSelected', 'DetailTorrentViewModel.forceRecheckTorrent', 'CALL', 'Force recheck the displayed torrent from the detail menu',
  guard='itemId == R.id.force_recheck_torrent_menu', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:461-462')
e('DetailTorrentFragment.onOptionsItemSelected', 'DetailTorrentViewModel.forceAnnounceTorrent', 'CALL', 'Force announce the displayed torrent from the detail menu',
  guard='itemId == R.id.force_announce_torrent_menu', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:463-464')
e('DetailTorrentFragment.onOptionsItemSelected', 'DetailTorrentFragment.deleteTorrentDialog', 'CALL', 'Open delete confirmation from the detail menu',
  guard='itemId == R.id.delete_torrent_menu', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:459-461,478-494')
e('DetailTorrentFragment.onOptionsItemSelected', 'DetailTorrentFragment.shareMagnetDialog', 'CALL', 'Open magnet-sharing options from the detail menu',
  guard='itemId == R.id.share_magnet_menu', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:465-466,498-514')
e('DetailTorrentFragment.onOptionsItemSelected', 'DetailTorrentFragment.torrentSaveChooseDialog', 'CALL', 'Open the torrent-file destination chooser from the detail menu',
  guard='itemId == R.id.save_torrent_file_menu', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:467-468')
e('DetailTorrentFragment.onOptionsItemSelected', 'DetailTorrentFragment.addTrackersDialog', 'CALL', 'Open the add-trackers dialog from the detail menu',
  guard='itemId == R.id.add_trackers_menu', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:469-470')
e('DetailTorrentFragment.onOptionsItemSelected', 'DetailTorrentFragment.speedLimitDialog', 'CALL', 'Open the speed-limit dialog from the detail menu',
  guard='itemId == R.id.torrent_speed_limit', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:471-472,566-582')
e('DetailTorrentFragment.onViewCreated', 'DetailTorrentViewModel.setTorrentId', 'CALL', 'Load selected torrent in shared detail view model',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:162-168; ui/detailtorrent/DetailTorrentViewModel.java:126-135')
e('DetailTorrentFragment.onViewCreated', 'DetailPagerAdapter.<init>', 'CALL', 'Create six-page torrent detail adapter',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:185-212; ui/detailtorrent/DetailPagerAdapter.java:40-43')
e('DetailTorrentFragment.onViewCreated', 'DetailPagerAdapter.createFragment', 'FRAMEWORK', 'Create selected detail page on demand',
  cls='non_standard', via='AndroidX ViewPager2 / FragmentStateAdapter', evidence='INFERRED AndroidX ViewPager2 dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:185-212; ui/detailtorrent/DetailPagerAdapter.java:48-73')
e('DetailPagerAdapter.createFragment', 'DetailTorrentInfoFragment.newInstance', 'CALL', 'Create torrent info page at position zero',
  guard='position == INFO_FRAG_POS', cls='explicit', evidence='SRC ui/detailtorrent/DetailPagerAdapter.java:54-57')
e('DetailPagerAdapter.createFragment', 'DetailTorrentStateFragment.newInstance', 'CALL', 'Create torrent state page at position one',
  guard='position == STATE_FRAG_POS', cls='explicit', evidence='SRC ui/detailtorrent/DetailPagerAdapter.java:56-59')
e('DetailPagerAdapter.createFragment', 'DetailTorrentFilesFragment.newInstance', 'CALL', 'Create file list page at position two',
  guard='position == FILES_FRAG_POS', cls='explicit', evidence='SRC ui/detailtorrent/DetailPagerAdapter.java:58-61')
e('DetailPagerAdapter.createFragment', 'DetailTorrentTrackersFragment.newInstance', 'CALL', 'Create trackers page at position three',
  guard='position == TRACKERS_FRAG_POS', cls='explicit', evidence='SRC ui/detailtorrent/DetailPagerAdapter.java:60-63')
e('DetailPagerAdapter.createFragment', 'DetailTorrentPeersFragment.newInstance', 'CALL', 'Create peers page at position four',
  guard='position == PEERS_FRAG_POS', cls='explicit', evidence='SRC ui/detailtorrent/DetailPagerAdapter.java:62-65')
e('DetailPagerAdapter.createFragment', 'DetailTorrentPiecesFragment.newInstance', 'CALL', 'Create pieces page at position five',
  guard='position == PIECES_FRAG_POS', cls='explicit', evidence='SRC ui/detailtorrent/DetailPagerAdapter.java:64-67')
e('DetailTorrentFragment.onStart', 'DetailTorrentFragment.subscribeTorrentInfo', 'CALL', 'Subscribe to torrent info while detail view is started',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:223-232,251-276')
e('DetailTorrentFragment.onStart', 'DetailTorrentFragment.subscribeAlertDialog', 'CALL', 'Subscribe to detail dialog events',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:223-232,297-354')
e('DetailTorrentFragment.onStart', 'DetailTorrentFragment.subscribeMsgViewModel', 'CALL', 'Observe detail action mode state',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:223-232,278-287')
e('DetailTorrentFragment.onStart', 'DetailTorrentFragment.subscribeFreeSpaceError', 'CALL', 'Observe torrent storage errors',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:223-232,290-295')
e('DetailTorrentFragment.subscribeFreeSpaceError', 'DetailTorrentFragment.lambda$subscribeFreeSpaceError$8', 'REGISTER', 'Subscribe to free-space error notifications through RxJava',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer registration; SRC ui/detailtorrent/DetailTorrentFragment.java:290-295,404-410')
e('DetailTorrentFragment.subscribeFreeSpaceError', 'DetailTorrentFragment.lambda$subscribeFreeSpaceError$8', 'FRAMEWORK', 'Deliver free-space error notifications to the fragment observer',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/detailtorrent/DetailTorrentFragment.java:290-295,404-410')
e('DetailTorrentFragment.lambda$subscribeFreeSpaceError$8', 'DetailTorrentFragment.showFreeSpaceErrorToast', 'CALL', 'Show the storage-space error message',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:290-295,404-410')
e('DetailTorrentFragment.subscribeAlertDialog', 'DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'REGISTER', 'Subscribe to detail dialog actions through RxJava',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer registration; SRC ui/detailtorrent/DetailTorrentFragment.java:297-354')
e('DetailTorrentFragment.subscribeAlertDialog', 'DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'FRAMEWORK', 'Deliver detail dialog events to the fragment observer',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/detailtorrent/DetailTorrentFragment.java:297-354')
e('DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'DetailTorrentFragment.deleteTorrent', 'CALL', 'Delete the torrent after delete confirmation',
  guard='event.type == POSITIVE_BUTTON_CLICKED && event.dialogTag == TAG_DELETE_TORRENT_DIALOG && deleteTorrentDialog != null', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:304-308; ui/detailtorrent/DetailTorrentFragment.java:588-607')
e('DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'DetailTorrentFragment.shareMagnet', 'CALL', 'Share the magnet link after the user chooses the include-priorities option',
  guard='event.type == POSITIVE_BUTTON_CLICKED && event.dialogTag == TAG_MAGNET_INCLUDE_PRIOR_DIALOG', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:309-310; ui/detailtorrent/DetailTorrentFragment.java:686-710')
e('DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'DetailTorrentFragment.shareMagnet', 'CALL', 'Share the magnet link without priorities after the user declines that option',
  guard='event.type == NEGATIVE_BUTTON_CLICKED && event.dialogTag == TAG_MAGNET_INCLUDE_PRIOR_DIALOG', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:328-333; ui/detailtorrent/DetailTorrentFragment.java:686-710')
e('DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'DetailTorrentFragment.addTrackers', 'CALL', 'Apply tracker additions from the dialog positive action',
  guard='event.type == POSITIVE_BUTTON_CLICKED && event.dialogTag == TAG_ADD_TRACKERS_DIALOG && addTrackersDialog != null', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:321-322; ui/detailtorrent/DetailTorrentFragment.java:640-682')
e('DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'DetailTorrentFragment.addTrackers', 'CALL', 'Apply tracker additions from the dialog negative action',
  guard='event.type == NEGATIVE_BUTTON_CLICKED && event.dialogTag == TAG_ADD_TRACKERS_DIALOG && addTrackersDialog != null', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:335-336; ui/detailtorrent/DetailTorrentFragment.java:640-682')
e('DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'DetailTorrentFragment.setSpeedLimit', 'CALL', 'Apply speed limits after positive confirmation',
  guard='event.type == POSITIVE_BUTTON_CLICKED && event.dialogTag == TAG_SPEED_LIMIT_DIALOG && speedLimitDialog != null', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:323-325; ui/detailtorrent/DetailTorrentFragment.java:741-768')
e('DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'DetailTorrentFragment.initAddTrackersDialog', 'CALL', 'Initialize tracker fields when the add-trackers dialog is shown',
  guard='event.type == DIALOG_SHOWN && event.dialogTag == TAG_ADD_TRACKERS_DIALOG && addTrackersDialog != null', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:345-348; ui/detailtorrent/DetailTorrentFragment.java:640-655')
e('DetailTorrentFragment.lambda$subscribeAlertDialog$9', 'DetailTorrentFragment.initSpeedLimitDialog', 'CALL', 'Initialize speed-limit fields when the dialog is shown',
  guard='event.type == DIALOG_SHOWN && event.dialogTag == TAG_SPEED_LIMIT_DIALOG && speedLimitDialog != null', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:345-350; ui/detailtorrent/DetailTorrentFragment.java:741-755')
e('DetailTorrentFragment.subscribeTorrentInfo', 'DetailTorrentViewModel.observeTorrentMetaInfo', 'CALL', 'Observe torrent metadata',
  guard='torrentId != null', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:251-263; ui/detailtorrent/DetailTorrentViewModel.java:195-197')
e('DetailTorrentFragment.subscribeTorrentInfo', 'DetailTorrentViewModel.observeTorrentInfoPair', 'CALL', 'Observe torrent info pairs',
  guard='torrentId != null', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:265-269; ui/detailtorrent/DetailTorrentViewModel.java:191-193')
e('DetailTorrentInfoFragment.newInstance', 'DetailTorrentInfoFragment.<init>', 'CALL', 'Instantiate torrent information page',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:81-88')
e('DetailTorrentInfoFragment.newInstance', 'DetailTorrentInfoFragment.onAttach', 'LIFECYCLE', 'Attach torrent information page',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:81-97')
e('DetailTorrentInfoFragment.onAttach', 'DetailTorrentInfoFragment.onCreateView', 'LIFECYCLE', 'Create torrent information view',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:91-113')
e('DetailTorrentInfoFragment.onCreateView', 'DetailTorrentInfoFragment.onStart', 'LIFECYCLE', 'Start torrent information subscriptions',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:99-105,197-205')
e('DetailTorrentInfoFragment.onStart', 'DetailTorrentInfoFragment.subscribeAlertDialog', 'CALL', 'Observe info-page dialog events',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:197-205')
e('DetailTorrentInfoFragment.onCreateView', 'DetailTorrentInfoFragment.lambda$onCreateView$0', 'REGISTER', 'Register the folder-chooser button click callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:99-114; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('DetailTorrentInfoFragment.onCreateView', 'DetailTorrentInfoFragment.lambda$onCreateView$0', 'FRAMEWORK', 'Dispatch folder-chooser button clicks to the registered callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:99-114; FW-SRC core/java/android/view/View.java:6289-6305')
e('DetailTorrentInfoFragment.lambda$onCreateView$0', 'DetailTorrentInfoFragment.showChooseDirDialog', 'CALL', 'Open the directory picker for the torrent save location',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:110,185-194')
e('DetailTorrentInfoFragment.onCreateView', 'DetailTorrentInfoFragment.lambda$onCreateView$1', 'REGISTER', 'Register the edit-name button click callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:99-114; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('DetailTorrentInfoFragment.onCreateView', 'DetailTorrentInfoFragment.lambda$onCreateView$1', 'FRAMEWORK', 'Dispatch edit-name button clicks to the registered callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:99-114; FW-SRC core/java/android/view/View.java:6289-6305')
e('DetailTorrentInfoFragment.lambda$onCreateView$1', 'DetailTorrentInfoFragment.showEditNameDialog', 'CALL', 'Open the torrent-name editor',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:111,275-291')
e('FileManagerDialog.returnDirectoryUri', 'DetailTorrentInfoFragment.lambda$new$2', 'RESULT', 'Return a chosen save directory through the registered ActivityResult launcher',
  guard='RESULT_OK and DetailTorrentInfoFragment launched FileManagerDialog in DIR_CHOOSER_MODE', cls='non_standard', via='AndroidX ActivityResultRegistry', evidence='INFERRED AndroidX ActivityResult delivery; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:117-130,185-194; ui/filemanager/FileManagerDialog.java:557-568')
e('DetailTorrentInfoFragment.lambda$new$2', 'DetailTorrentInfoFragment.showOpenDirErrorDialog', 'CALL', 'Show the directory error dialog when a successful result has no URI',
  guard='resultCode == Activity.RESULT_OK && (data == null || data.getData() == null)', cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:119-130,240-257')
e('DetailTorrentInfoFragment.subscribeAlertDialog', 'DetailTorrentInfoFragment.lambda$subscribeAlertDialog$4', 'REGISTER', 'Subscribe the info page to edit-name dialog events through RxJava',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer registration; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:211-238')
e('DetailTorrentInfoFragment.subscribeAlertDialog', 'DetailTorrentInfoFragment.lambda$subscribeAlertDialog$4', 'FRAMEWORK', 'Deliver edit-name dialog events to the info-page observer',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava observer delivery; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:211-238')
e('DetailTorrentInfoFragment.lambda$subscribeAlertDialog$4', 'DetailTorrentInfoFragment.initEditNameDialog', 'CALL', 'Initialize the editor after the edit-name dialog is shown',
  guard='event.type == DIALOG_SHOWN && event.dialogTag == TAG_EDIT_NAME_DIALOG && editNameDialog != null', cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:214-219,294-322')
e('DetailTorrentInfoFragment.lambda$subscribeAlertDialog$4', 'DetailTorrentInfoFragment.checkNameField', 'CALL', 'Validate the edited name before applying it',
  guard='event.type == POSITIVE_BUTTON_CLICKED && event.dialogTag == TAG_EDIT_NAME_DIALOG && dialog != null', cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:220-230,259-273')
e('DetailTorrentInfoFragment.onStart', 'DetailTorrentInfoFragment.subscribeTags', 'CALL', 'Observe torrent tags in info page',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:197-205,177-183')
e('DetailTorrentStateFragment.newInstance', 'DetailTorrentStateFragment.<init>', 'CALL', 'Instantiate torrent state page',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentStateFragment.java:51-58')
e('DetailTorrentStateFragment.newInstance', 'DetailTorrentStateFragment.onAttach', 'LIFECYCLE', 'Attach torrent state page',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/DetailTorrentStateFragment.java:51-70')
e('DetailTorrentStateFragment.onAttach', 'DetailTorrentStateFragment.onCreateView', 'LIFECYCLE', 'Create torrent state view',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/DetailTorrentStateFragment.java:62-77')
e('DetailTorrentStateFragment.onCreateView', 'DetailTorrentStateFragment.onViewCreated', 'LIFECYCLE', 'Bind torrent state fields',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/DetailTorrentStateFragment.java:79-100')
e('DetailTorrentFilesFragment.newInstance', 'DetailTorrentFilesFragment.<init>', 'CALL', 'Instantiate torrent files page',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:101-108')
e('DetailTorrentFilesFragment.newInstance', 'DetailTorrentFilesFragment.onAttach', 'LIFECYCLE', 'Attach torrent files page',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:101-128')
e('DetailTorrentFilesFragment.onAttach', 'DetailTorrentFilesFragment.onCreateView', 'LIFECYCLE', 'Inflate torrent files page view',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:112-144')
e('DetailTorrentFilesFragment.onCreateView', 'DetailTorrentFilesFragment.onViewCreated', 'LIFECYCLE', 'Initialize files list and selection controls',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:193-240')
e('DetailTorrentFilesFragment.onViewCreated', 'DetailTorrentFilesFragment.onStart', 'LIFECYCLE', 'Start files page observers',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:146-151,193-240')
e('DetailTorrentFilesFragment.onStart', 'DetailTorrentFilesFragment.subscribeAdapter', 'CALL', 'Subscribe to torrent file rows',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:146-151')
e('DetailTorrentFilesFragment.onStart', 'DetailTorrentFilesFragment.subscribeAlertDialog', 'CALL', 'Subscribe to file page dialog events',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:146-151')
e('DetailTorrentFilesFragment.onViewCreated', 'TorrentContentFilesAdapter.onCreateViewHolder', 'FRAMEWORK', 'Create file rows when RecyclerView needs holders',
  cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView.Adapter dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:205-208; ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:72-82')
e('DetailTorrentFilesFragment.onViewCreated', 'TorrentContentFilesAdapter.onBindViewHolder', 'FRAMEWORK', 'Bind file rows displayed by RecyclerView',
  cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:205-208; ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:85-92')
e('TorrentContentFilesAdapter.onBindViewHolder', 'TorrentContentFilesAdapter$ViewHolder.bind', 'CALL', 'Bind file row content and click handlers',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:85-92')
e('TorrentContentFilesAdapter$ViewHolder.bind', 'TorrentContentFilesAdapter$ViewHolder.lambda$bind$0', 'REGISTER', 'Register file row click callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:166-172; FW-SRC core/java/android/view/View.java:6143-6148')
e('TorrentContentFilesAdapter$ViewHolder.bind', 'TorrentContentFilesAdapter$ViewHolder.lambda$bind$0', 'FRAMEWORK', 'Deliver row taps to the click callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:166-172; FW-SRC core/java/android/view/View.java:6289-6295')
e('TorrentContentFilesAdapter$ViewHolder.lambda$bind$0', 'DetailTorrentFilesFragment.onItemClicked', 'CALL', 'Handle a tapped torrent file or directory row',
  guard='!isSelected && listener != null', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:166-172; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:333-348')
e('TorrentContentFilesAdapter$ViewHolder.bind', 'TorrentContentFilesAdapter$ViewHolder.lambda$bind$1', 'REGISTER', 'Register file priority checkbox callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:173-177; FW-SRC core/java/android/view/View.java:6143-6148')
e('TorrentContentFilesAdapter$ViewHolder.bind', 'TorrentContentFilesAdapter$ViewHolder.lambda$bind$1', 'FRAMEWORK', 'Deliver checkbox taps to the priority callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:173-177; FW-SRC core/java/android/view/View.java:6289-6295')
e('TorrentContentFilesAdapter$ViewHolder.lambda$bind$1', 'DetailTorrentFilesFragment.onItemCheckedChanged', 'CALL', 'Apply priority for a changed file checkbox',
  guard='listener != null', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/TorrentContentFilesAdapter.java:173-177; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:351-356')
e('DetailTorrentFilesFragment.subscribeAdapter', 'DetailTorrentFilesFragment.lambda$subscribeAdapter$0', 'REGISTER', 'Convert directory children into displayed file items',
  cls='non_standard', via='RxJava flatMapSingle callback', evidence='INFERRED RxJava flatMapSingle dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:154-163')
e('DetailTorrentFilesFragment.subscribeAdapter', 'DetailTorrentFilesFragment.lambda$subscribeAdapter$0', 'FRAMEWORK', 'Invoke the directory-child conversion callback',
  cls='non_standard', via='RxJava flatMapSingle callback', evidence='INFERRED RxJava flatMapSingle dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:154-163')
e('DetailTorrentFilesFragment.lambda$subscribeAdapter$0', 'TorrentContentFileItem.<init>(TorrentContentFileTree)', 'CALL', 'Wrap each directory child as a list item',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:158-161')
e('DetailTorrentFilesFragment.subscribeAdapter', 'DetailTorrentFilesFragment.lambda$subscribeAdapter$1', 'REGISTER', 'Observe converted directory children on the main thread',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:154-168')
e('DetailTorrentFilesFragment.subscribeAdapter', 'DetailTorrentFilesFragment.lambda$subscribeAdapter$1', 'FRAMEWORK', 'Deliver converted children to the subscriber',
  cls='non_standard', via='RxJava observeOn and subscribe callback', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:162-168')
e('DetailTorrentFilesFragment.lambda$subscribeAdapter$1', 'DetailTorrentFilesFragment.updateFileSize', 'CALL', 'Refresh total and selected file sizes after list update',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:164-167')
e('DetailTorrentFilesFragment.subscribeAlertDialog', 'DetailTorrentFilesFragment.lambda$subscribeAlertDialog$2', 'REGISTER', 'Observe priority-dialog events',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:170-190')
e('DetailTorrentFilesFragment.subscribeAlertDialog', 'DetailTorrentFilesFragment.lambda$subscribeAlertDialog$2', 'FRAMEWORK', 'Deliver priority-dialog events to the observer',
  cls='non_standard', via='RxJava event delivery', evidence='INFERRED RxJava event delivery; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:170-190')
e('DetailTorrentFilesFragment.lambda$subscribeAlertDialog$2', 'DetailTorrentFilesFragment.initPriorityDialog', 'CALL', 'Initialize the priority selection after the dialog is shown',
  guard='event matches TAG_PRIORITY_DIALOG && priorityDialog != null && event.type == DIALOG_SHOWN', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:173-179')
e('DetailTorrentFilesFragment.lambda$subscribeAlertDialog$2', 'DetailTorrentFilesFragment.changePriority', 'CALL', 'Apply selected priority after positive dialog action',
  guard='event matches TAG_PRIORITY_DIALOG && priorityDialog != null && event.type == POSITIVE_BUTTON_CLICKED', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:173-184; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:477-507')
e('DetailTorrentFilesFragment.onItemClicked', 'DetailTorrentFilesFragment.lambda$onItemClicked$3', 'REGISTER', 'Receive the resolved content URI for a file row',
  guard='item.name != PARENT_DIR && item.isFile', cls='non_standard', via='RxJava success callback', evidence='INFERRED RxJava subscribe callback; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:339-346')
e('DetailTorrentFilesFragment.onItemClicked', 'DetailTorrentFilesFragment.lambda$onItemClicked$3', 'FRAMEWORK', 'Deliver the resolved content URI to the success callback',
  guard='item.name != PARENT_DIR && item.isFile', cls='non_standard', via='RxJava subscribe success callback', evidence='INFERRED RxJava subscribe success dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:339-346')
e('DetailTorrentFilesFragment.lambda$onItemClicked$3', 'DetailTorrentFilesFragment.openFile', 'CALL', 'Launch the resolved file URI',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:339-346; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:527-533')
e('DetailTorrentFilesFragment.onItemClicked', 'DetailTorrentFilesFragment.handleOpenFileError', 'REGISTER', 'Handle a failed file URI lookup',
  guard='item.name != PARENT_DIR && item.isFile', cls='non_standard', via='RxJava error consumer', evidence='INFERRED RxJava subscribe error dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:339-346; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:535-542')
e('DetailTorrentFilesFragment.onItemClicked', 'DetailTorrentFilesFragment.handleOpenFileError', 'FRAMEWORK', 'Deliver file URI lookup errors to the error consumer',
  guard='item.name != PARENT_DIR && item.isFile', cls='non_standard', via='RxJava subscribe error consumer', evidence='INFERRED RxJava subscribe error dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:339-346; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:535-542')
e('DetailTorrentFilesFragment.onViewCreated', 'DetailTorrentFilesFragment$3.onSelectionChanged', 'REGISTER', 'Register the file selection observer',
  cls='non_standard', via='AndroidX SelectionTracker observer', evidence='INFERRED AndroidX SelectionTracker observer dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:249-272')
e('DetailTorrentFilesFragment.onViewCreated', 'DetailTorrentFilesFragment$3.onSelectionChanged', 'FRAMEWORK', 'Notify the observer when file selection changes',
  cls='non_standard', via='AndroidX SelectionTracker observer', evidence='INFERRED AndroidX SelectionTracker observer dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:249-272')
e('DetailTorrentFilesFragment.onViewCreated', 'DetailTorrentFilesFragment$3.onSelectionRestored', 'REGISTER', 'Register the restored-selection callback',
  cls='non_standard', via='AndroidX SelectionTracker observer', evidence='INFERRED AndroidX SelectionTracker observer dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:274-282')
e('DetailTorrentFilesFragment.onViewCreated', 'DetailTorrentFilesFragment$3.onSelectionRestored', 'FRAMEWORK', 'Notify the observer when saved selection is restored',
  guard='savedInstanceState != null', cls='non_standard', via='AndroidX SelectionTracker restore callback', evidence='INFERRED AndroidX SelectionTracker restore dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:274-285')
e('DetailTorrentFilesFragment$3.onSelectionChanged', 'DetailTorrentFilesFragment.setActionModeTitle', 'CALL', 'Update the contextual title while selection exists',
  guard='selectionTracker.hasSelection()', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:255-270; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:358-361')
e('DetailTorrentFilesFragment$3.onSelectionChanged', 'DetailTorrentFilesFragment$4.onCreateActionMode', 'FRAMEWORK', 'Create contextual actions for the first selected file',
  guard='selectionTracker.hasSelection() && actionMode == null', cls='non_standard', via='AppCompat startSupportActionMode callback', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:255-257; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:363-391')
e('DetailTorrentFilesFragment$3.onSelectionChanged', 'DetailTorrentFilesFragment$4.onPrepareActionMode', 'FRAMEWORK', 'Refresh contextual actions after selection changes',
  guard='selectionTracker.hasSelection() && (selection size == 1 || selection size == 2)', cls='non_standard', via='AppCompat ActionMode invalidate callback', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:264-270; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:366-381')
e('DetailTorrentFilesFragment$3.onSelectionRestored', 'DetailTorrentFilesFragment$4.onCreateActionMode', 'FRAMEWORK', 'Create contextual actions for restored file selection',
  guard='savedInstanceState != null', cls='non_standard', via='AppCompat startSupportActionMode callback', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:274-280; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:363-391')
e('DetailTorrentFilesFragment$4.onCreateActionMode', 'DetailTorrentFilesFragment$4.onPrepareActionMode', 'FRAMEWORK', 'Prepare menu items after creating contextual actions',
  cls='non_standard', via='AppCompat ActionMode callback dispatch', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:383-391,366-381')
e('DetailTorrentFilesFragment$4.onActionItemClicked', 'DetailTorrentFilesFragment.showPriorityDialog', 'CALL', 'Open the selected-file priority dialog',
  guard='itemId == R.id.change_priority_menu', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:393-404; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:416-439')
e('DetailTorrentFilesFragment$4.onActionItemClicked', 'DetailTorrentFilesFragment.shareStreamUrl', 'CALL', 'Share the selected file stream URL',
  guard='itemId == R.id.share_stream_url_menu', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:393-402; ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:509-525')
e('DetailTorrentFilesFragment$4.onCreateActionMode', 'DetailTorrentFilesFragment$4.onActionItemClicked', 'FRAMEWORK', 'Dispatch a selected contextual menu action',
  cls='non_standard', via='AppCompat ActionMode menu callback', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:383-405')
e('DetailTorrentFilesFragment$4.onCreateActionMode', 'DetailTorrentFilesFragment$4.onDestroyActionMode', 'FRAMEWORK', 'Deliver contextual-mode teardown when the user exits',
  cls='non_standard', via='AppCompat ActionMode callback', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:383-413')
e('DetailTorrentFilesFragment.initPriorityDialog', 'DetailTorrentFilesFragment.lambda$initPriorityDialog$4', 'REGISTER', 'Map selected file rows to their names for priority display',
  cls='non_standard', via='RxJava map callback', evidence='INFERRED RxJava map dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:435-444')
e('DetailTorrentFilesFragment.initPriorityDialog', 'DetailTorrentFilesFragment.lambda$initPriorityDialog$4', 'FRAMEWORK', 'Invoke the file-name mapping callback',
  cls='non_standard', via='RxJava map callback', evidence='INFERRED RxJava map dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:435-444')
e('DetailTorrentFilesFragment.initPriorityDialog', 'DetailTorrentFilesFragment.lambda$initPriorityDialog$5', 'REGISTER', 'Apply current file priorities to the dialog controls',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:441-474')
e('DetailTorrentFilesFragment.initPriorityDialog', 'DetailTorrentFilesFragment.lambda$initPriorityDialog$5', 'FRAMEWORK', 'Deliver selected file names to the priority dialog observer',
  cls='non_standard', via='RxJava toList/subscribe callback', evidence='INFERRED RxJava toList/subscribe dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:441-474')
e('DetailTorrentFilesFragment.lambda$initPriorityDialog$5', 'DetailTorrentViewModel.getFilesPriority', 'CALL', 'Read the current priority for selected files',
  guard='priorityDialog.getDialog() != null', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:445-451')
e('DetailTorrentFilesFragment.changePriority', 'DetailTorrentFilesFragment.lambda$changePriority$6', 'REGISTER', 'Map selected rows to names before applying a priority',
  guard='priorityDialog.getDialog() != null && priorityType != null', cls='non_standard', via='RxJava map callback', evidence='INFERRED RxJava map dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:477-502')
e('DetailTorrentFilesFragment.changePriority', 'DetailTorrentFilesFragment.lambda$changePriority$6', 'FRAMEWORK', 'Invoke the selected-file name mapping callback',
  guard='priorityDialog.getDialog() != null && priorityType != null', cls='non_standard', via='RxJava map callback', evidence='INFERRED RxJava map dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:477-502')
e('DetailTorrentFilesFragment.changePriority', 'DetailTorrentFilesFragment.lambda$changePriority$7', 'REGISTER', 'Apply the chosen priority to selected file names',
  guard='priorityDialog.getDialog() != null && priorityType != null', cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:494-502')
e('DetailTorrentFilesFragment.changePriority', 'DetailTorrentFilesFragment.lambda$changePriority$7', 'FRAMEWORK', 'Deliver selected file names to the priority update subscriber',
  guard='priorityDialog.getDialog() != null && priorityType != null', cls='non_standard', via='RxJava toList/subscribe callback', evidence='INFERRED RxJava toList/subscribe dispatch; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:494-502')
e('DetailTorrentFilesFragment.lambda$changePriority$7', 'DetailTorrentViewModel.applyPriority', 'CALL', 'Apply the chosen priority to the selected files',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:499-502')
e('DetailTorrentPiecesFragment.onViewCreated', 'DetailTorrentPiecesFragment.onViewStateRestored', 'LIFECYCLE', 'Restore saved piece-map scroll position',
  guard='savedInstanceState != null', cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:125-133')
e('DetailTorrentPiecesFragment.onViewCreated', 'DetailTorrentPiecesFragment.onSaveInstanceState', 'LIFECYCLE', 'Save piece-map scroll position during state save',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:113-122')
e('DetailTorrentPiecesFragment.onStart', 'DetailTorrentPiecesFragment.onStop', 'LIFECYCLE', 'Clear piece observers when the page stops',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:86-93')
e('DetailTorrentPiecesFragment.subscribeAdapter', 'DetailTorrentPiecesFragment.lambda$subscribeAdapter$0', 'REGISTER', 'Observe piece updates on the main thread',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:136-143')
e('DetailTorrentPiecesFragment.subscribeAdapter', 'DetailTorrentPiecesFragment.lambda$subscribeAdapter$0', 'FRAMEWORK', 'Deliver observed pieces to the UI subscriber',
  cls='non_standard', via='RxJava observeOn/subscribe callback', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:136-143')
e('DetailTorrentPiecesFragment.lambda$subscribeAdapter$0', 'PiecesView.setPieces', 'CALL', 'Update the piece-map custom view',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:136-143')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter.onCreateViewHolder', 'FRAMEWORK', 'Create tracker rows when RecyclerView needs holders',
  cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:166-183; ui/detailtorrent/pages/trackers/TrackerListAdapter.java:67-79')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter.onBindViewHolder', 'FRAMEWORK', 'Bind tracker rows displayed by RecyclerView',
  cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:166-183; ui/detailtorrent/pages/trackers/TrackerListAdapter.java:82-92')
e('TrackerListAdapter.onBindViewHolder', 'TrackerListAdapter$ViewHolder.bind', 'CALL', 'Bind tracker URL and status details',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:82-92')
e('DetailTorrentTrackersFragment.subscribeAdapter', 'DetailTorrentTrackersFragment.lambda$subscribeAdapter$0', 'REGISTER', 'Convert observed tracker rows into adapter items',
  cls='non_standard', via='RxJava flatMapSingle callback', evidence='INFERRED RxJava flatMapSingle dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:258-268')
e('DetailTorrentTrackersFragment.subscribeAdapter', 'DetailTorrentTrackersFragment.lambda$subscribeAdapter$0', 'FRAMEWORK', 'Invoke tracker conversion callback',
  cls='non_standard', via='RxJava flatMapSingle callback', evidence='INFERRED RxJava flatMapSingle dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:258-268')
e('DetailTorrentTrackersFragment.lambda$subscribeAdapter$0', 'TrackerItem.<init>', 'CALL', 'Wrap each observed tracker for display',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:262-266')
e('DetailTorrentTrackersFragment.subscribeAdapter', 'DetailTorrentTrackersFragment.lambda$subscribeAdapter$1', 'REGISTER', 'Submit tracker updates on the main thread',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:260-268')
e('DetailTorrentTrackersFragment.subscribeAdapter', 'DetailTorrentTrackersFragment.lambda$subscribeAdapter$1', 'FRAMEWORK', 'Deliver converted trackers to the list subscriber',
  cls='non_standard', via='RxJava observeOn/subscribe callback', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:267-268')
e('DetailTorrentTrackersFragment.lambda$subscribeAdapter$1', 'TrackerListAdapter.submitList', 'CALL', 'Display the updated tracker list',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:267-268')
e('DetailTorrentTrackersFragment.subscribeAlertDialog', 'DetailTorrentTrackersFragment.lambda$subscribeAlertDialog$2', 'REGISTER', 'Observe delete-tracker confirmation events',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:271-288')
e('DetailTorrentTrackersFragment.subscribeAlertDialog', 'DetailTorrentTrackersFragment.lambda$subscribeAlertDialog$2', 'FRAMEWORK', 'Deliver delete-tracker dialog events to the observer',
  cls='non_standard', via='RxJava event delivery', evidence='INFERRED RxJava event dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:271-288')
e('DetailTorrentTrackersFragment.lambda$subscribeAlertDialog$2', 'DetailTorrentTrackersFragment.deleteTrackers', 'CALL', 'Delete selected tracker URLs after confirmation',
  guard='event matches TAG_DELETE_TRACKERS_DIALOG && deleteTrackersDialog != null && event.type == POSITIVE_BUTTON_CLICKED', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:274-285; ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:360-372')
e('DetailTorrentTrackersFragment$3.onActionItemClicked', 'DetailTorrentTrackersFragment.deleteTrackersDialog', 'CALL', 'Ask for confirmation before deleting selected tracker URLs',
  guard='itemId == R.id.delete_tracker_url', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:314-326; ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:338-358')
e('DetailTorrentTrackersFragment$3.onActionItemClicked', 'DetailTorrentTrackersFragment.shareUrl', 'CALL', 'Share selected tracker URLs',
  guard='itemId == R.id.share_url_menu', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:314-326; ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:374-395')
e('DetailTorrentTrackersFragment$3.onActionItemClicked', 'DetailTorrentTrackersFragment.selectAllTrackers', 'CALL', 'Select every tracker row',
  guard='itemId == R.id.select_all_trackers_menu', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:314-326; ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:397-405')
e('DetailTorrentTrackersFragment.onViewCreated', 'DetailTorrentTrackersFragment$2.onSelectionChanged', 'REGISTER', 'Register tracker selection observer',
  cls='non_standard', via='AndroidX SelectionTracker observer', evidence='INFERRED AndroidX SelectionTracker observer dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:187-214')
e('DetailTorrentTrackersFragment.onViewCreated', 'DetailTorrentTrackersFragment$2.onSelectionChanged', 'FRAMEWORK', 'Notify observer when tracker selection changes',
  cls='non_standard', via='AndroidX SelectionTracker observer', evidence='INFERRED AndroidX SelectionTracker observer dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:187-214')
e('DetailTorrentTrackersFragment.onViewCreated', 'DetailTorrentTrackersFragment$2.onSelectionRestored', 'REGISTER', 'Register tracker selection restore callback',
  cls='non_standard', via='AndroidX SelectionTracker observer', evidence='INFERRED AndroidX SelectionTracker observer dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:187-214')
e('DetailTorrentTrackersFragment.onViewCreated', 'DetailTorrentTrackersFragment$2.onSelectionRestored', 'FRAMEWORK', 'Notify observer when tracker selection is restored',
  guard='savedInstanceState != null', cls='non_standard', via='AndroidX SelectionTracker restore callback', evidence='INFERRED AndroidX SelectionTracker restore dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:187-224')
e('DetailTorrentTrackersFragment$2.onSelectionChanged', 'DetailTorrentTrackersFragment$3.onCreateActionMode', 'FRAMEWORK', 'Create contextual tracker actions after first selection',
  guard='selectionTracker.hasSelection() && actionMode == null', cls='non_standard', via='AppCompat startSupportActionMode callback', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:197-199; ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:295-311')
e('DetailTorrentTrackersFragment$2.onSelectionChanged', 'DetailTorrentTrackersFragment$3.onPrepareActionMode', 'FRAMEWORK', 'Refresh contextual tracker actions after selection changes',
  guard='selectionTracker.hasSelection() && (selection size == 1 || selection size == 2)', cls='non_standard', via='AppCompat ActionMode invalidate callback', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:206-211; ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:298-302')
e('DetailTorrentTrackersFragment$2.onSelectionRestored', 'DetailTorrentTrackersFragment$3.onCreateActionMode', 'FRAMEWORK', 'Create contextual tracker actions for restored selection',
  guard='savedInstanceState != null', cls='non_standard', via='AppCompat startSupportActionMode callback', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:215-218; ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:295-311')
e('DetailTorrentTrackersFragment$3.onCreateActionMode', 'DetailTorrentTrackersFragment$3.onActionItemClicked', 'FRAMEWORK', 'Dispatch a selected tracker contextual menu action',
  cls='non_standard', via='AppCompat ActionMode menu callback', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:304-326')
e('DetailTorrentTrackersFragment$3.onCreateActionMode', 'DetailTorrentTrackersFragment$3.onDestroyActionMode', 'FRAMEWORK', 'Deliver contextual tracker action-mode teardown',
  cls='non_standard', via='AppCompat ActionMode callback', evidence='INFERRED AppCompat ActionMode callback dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:304-335')
e('DetailTorrentInfoFragment.initEditNameDialog', 'DetailTorrentInfoFragment$2.<init>', 'CALL', 'Create a text watcher for the name editor',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:309-323')
e('DetailTorrentInfoFragment.initEditNameDialog', 'DetailTorrentInfoFragment$2.beforeTextChanged', 'REGISTER', 'Register the text watcher before-change callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:309-323; FW-SRC core/java/android/widget/TextView.java:9286-9288')
e('DetailTorrentInfoFragment.initEditNameDialog', 'DetailTorrentInfoFragment$2.onTextChanged', 'REGISTER', 'Register the text watcher text-change callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:309-323; FW-SRC core/java/android/widget/TextView.java:9286-9288')
e('DetailTorrentInfoFragment.initEditNameDialog', 'DetailTorrentInfoFragment$2.afterTextChanged', 'REGISTER', 'Register validation after name edits',
  cls='standard', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:309-323; FW-SRC core/java/android/widget/TextView.java:9286-9288')
e('DetailTorrentInfoFragment.initEditNameDialog', 'DetailTorrentInfoFragment$2.beforeTextChanged', 'FRAMEWORK', 'Dispatch the before-change watcher callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:309-323; FW-SRC core/java/android/widget/TextView.java:9309-9337')
e('DetailTorrentInfoFragment.initEditNameDialog', 'DetailTorrentInfoFragment$2.onTextChanged', 'FRAMEWORK', 'Dispatch the text-change watcher callback',
  cls='standard', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:309-323; FW-SRC core/java/android/widget/TextView.java:9359-9368')
e('DetailTorrentInfoFragment.initEditNameDialog', 'DetailTorrentInfoFragment$2.afterTextChanged', 'FRAMEWORK', 'Dispatch name validation after text edits',
  cls='standard', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:309-323; FW-SRC core/java/android/widget/TextView.java:9375-9388')
e('DetailTorrentInfoFragment$2.afterTextChanged', 'DetailTorrentInfoFragment.checkNameField', 'CALL', 'Validate the edited name and show field feedback',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:320-322')
e('DetailTorrentInfoFragment.onStart', 'DetailTorrentInfoFragment.onStop', 'LIFECYCLE', 'Clear info-page observers when the fragment stops',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:200-209')
e('DetailTorrentFragment.onStart', 'DetailTorrentFragment.onStop', 'LIFECYCLE', 'Clear detail-page observers when the fragment stops',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:223-240')
e('DetailTorrentFragment.onViewCreated', 'DetailTorrentFragment.onSaveInstanceState', 'LIFECYCLE', 'Save the current detail page and torrent ID',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment state-save dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:243-249')
e('DetailTorrentFragment.subscribeTorrentInfo', 'DetailTorrentFragment.handleTorrentInfo', 'REGISTER', 'Observe and handle torrent-info updates',
  guard='torrentId != null', cls='non_standard', via='RxJava subscribe method reference', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:251-276,356-375')
e('DetailTorrentFragment.subscribeTorrentInfo', 'DetailTorrentFragment.handleTorrentInfo', 'FRAMEWORK', 'Deliver each torrent-info pair to the fragment handler',
  guard='torrentId != null', cls='non_standard', via='RxJava observeOn/subscribe method reference', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:265-269,356-375')
e('DetailTorrentFragment.handleTorrentInfo', 'DetailTorrentViewModel.updateInfo(Torrent,TorrentInfo)', 'CALL', 'Update displayed torrent and runtime information',
  cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:356-375; ui/detailtorrent/DetailTorrentViewModel.java:206-216')
e('DetailTorrentFragment.handleTorrentInfo', 'DetailTorrentFragment.prepareOptionsMenu', 'CALL', 'Refresh pause/resume and save-file menu state for paused torrent info',
  guard='torrent != null && ti != null && (ti.stateCode == PAUSED || alreadyPaused) && Utils.isTwoPane(activity)', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:356-375; ui/detailtorrent/DetailTorrentFragment.java:467-490')
e('DetailTorrentFragment.subscribeMsgViewModel', 'DetailTorrentFragment.setTabLayoutColor', 'REGISTER', 'Observe action-mode color changes for the detail tabs',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:278-287,377-382')
e('DetailTorrentFragment.subscribeMsgViewModel', 'DetailTorrentFragment.setTabLayoutColor', 'FRAMEWORK', 'Deliver action-mode state to update tab color',
  cls='non_standard', via='RxJava observeOn/subscribe callback', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:278-287,377-382')
e('DetailTorrentFragment.onViewCreated', 'DetailTorrentFragment$1.onPageSelected', 'REGISTER', 'Register the detail page selection callback',
  cls='non_standard', via='AndroidX ViewPager2 page callback', evidence='INFERRED AndroidX ViewPager2 callback dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:161-180')
e('DetailTorrentFragment.onViewCreated', 'DetailTorrentFragment$1.onPageSelected', 'FRAMEWORK', 'Update the current page position after a swipe or tab change',
  cls='non_standard', via='AndroidX ViewPager2 page callback', evidence='INFERRED AndroidX ViewPager2 callback dispatch; SRC ui/detailtorrent/DetailTorrentFragment.java:161-180; ui/detailtorrent/DetailTorrentFragment.java:426-433')
e('MainActivity.subscribeMsgViewModel', 'MainActivity.lambda$subscribeMsgViewModel$6', 'REGISTER', 'Observe torrent deletion events for the currently open detail page',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/main/MainActivity.java:437-454')
e('MainActivity.subscribeMsgViewModel', 'MainActivity.lambda$subscribeMsgViewModel$6', 'FRAMEWORK', 'Deliver deleted torrent IDs to the activity observer',
  cls='non_standard', via='RxJava observeOn/subscribe callback', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/main/MainActivity.java:446-454')
e('MainActivity.lambda$subscribeMsgViewModel$6', 'MainActivity.getCurrentDetailFragment', 'CALL', 'Find the currently displayed detail page for a deletion event',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:449-453')
e('MainActivity.lambda$subscribeMsgViewModel$6', 'MainActivity.showBlankFragment', 'CALL', 'Close the detail page when its torrent was deleted',
  guard='current detail fragment != null && deletedId.equals(fragment.getTorrentId())', cls='explicit', evidence='SRC ui/main/MainActivity.java:449-453')
e('MainActivity.subscribeNeedStartEngine', 'MainActivity.lambda$subscribeNeedStartEngine$7', 'REGISTER', 'Filter engine-start events by their requested state',
  cls='non_standard', via='RxJava filter callback', evidence='INFERRED RxJava filter dispatch; SRC ui/main/MainActivity.java:463-468')
e('MainActivity.subscribeNeedStartEngine', 'MainActivity.lambda$subscribeNeedStartEngine$7', 'FRAMEWORK', 'Evaluate the engine-start condition',
  cls='non_standard', via='RxJava filter callback', evidence='INFERRED RxJava filter dispatch; SRC ui/main/MainActivity.java:463-468')
e('MainActivity.subscribeNeedStartEngine', 'MainActivity.lambda$subscribeNeedStartEngine$8', 'REGISTER', 'Start the engine for a requested startup event',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/main/MainActivity.java:463-468')
e('MainActivity.lambda$subscribeNeedStartEngine$7', 'MainActivity.lambda$subscribeNeedStartEngine$8', 'FRAMEWORK', 'Deliver the event when the filter allows engine startup',
  guard='needStart == true', cls='non_standard', via='RxJava filter/subscribe dispatch', evidence='INFERRED RxJava filter/subscribe dispatch; SRC ui/main/MainActivity.java:463-468')
e('MainActivity.lambda$subscribeNeedStartEngine$8', 'MainViewModel.startEngine', 'CALL', 'Start the engine after an app request',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:463-468')
e('MainActivity.initSearch', 'MainActivity$4.onQueryTextSubmit', 'REGISTER', 'Register search submission callback',
  cls='non_standard', via='AppCompat SearchView listener', evidence='INFERRED AppCompat SearchView callback dispatch; SRC ui/main/MainActivity.java:707-730')
e('MainActivity.initSearch', 'MainActivity$4.onQueryTextChange', 'REGISTER', 'Register search text-change callback',
  cls='non_standard', via='AppCompat SearchView listener', evidence='INFERRED AppCompat SearchView callback dispatch; SRC ui/main/MainActivity.java:707-730')
e('MainActivity.initSearch', 'MainActivity$4.onQueryTextSubmit', 'FRAMEWORK', 'Dispatch search submission to the registered listener',
  cls='non_standard', via='AppCompat SearchView listener', evidence='INFERRED AppCompat SearchView callback dispatch; SRC ui/main/MainActivity.java:714-730')
e('MainActivity.initSearch', 'MainActivity$4.onQueryTextChange', 'FRAMEWORK', 'Dispatch changed search text to the registered listener',
  cls='non_standard', via='AppCompat SearchView listener', evidence='INFERRED AppCompat SearchView callback dispatch; SRC ui/main/MainActivity.java:714-730')
e('MainActivity$4.onQueryTextSubmit', 'MainViewModel.setSearchQuery', 'CALL', 'Apply a submitted torrent search query',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:716-721')
e('MainActivity$4.onQueryTextChange', 'MainViewModel.setSearchQuery', 'CALL', 'Apply each changed torrent search query',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:724-729')
e('MainActivity.initSearch', 'MainActivity.lambda$initSearch$13', 'REGISTER', 'Register search close callback',
  cls='non_standard', via='AppCompat SearchView close listener', evidence='INFERRED AppCompat SearchView callback dispatch; SRC ui/main/MainActivity.java:707-714')
e('MainActivity.initSearch', 'MainActivity.lambda$initSearch$13', 'FRAMEWORK', 'Dispatch the SearchView close event',
  cls='non_standard', via='AppCompat SearchView close listener', evidence='INFERRED AppCompat SearchView close callback dispatch; SRC ui/main/MainActivity.java:709-714')
e('MainActivity.lambda$initSearch$13', 'MainViewModel.resetSearch', 'CALL', 'Clear the active search query',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:709-714')
e('MainActivity.subscribeTags', 'MainActivity.lambda$subscribeTags$9', 'REGISTER', 'Convert tag updates into drawer rows',
  cls='non_standard', via='RxJava flatMapSingle callback', evidence='INFERRED RxJava flatMapSingle dispatch; SRC ui/main/MainActivity.java:470-480')
e('MainActivity.subscribeTags', 'MainActivity.lambda$subscribeTags$9', 'FRAMEWORK', 'Invoke the tag-list conversion callback',
  cls='non_standard', via='RxJava flatMapSingle callback', evidence='INFERRED RxJava flatMapSingle dispatch; SRC ui/main/MainActivity.java:470-480')
e('MainActivity.lambda$subscribeTags$9', 'EmptyTagItem.<init>', 'CALL', 'Add the all-torrents drawer row',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:473-478')
e('MainActivity.lambda$subscribeTags$9', 'NoTagsItem.<init>', 'CALL', 'Add the no-tags drawer row',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:473-478')
e('MainActivity.lambda$subscribeTags$9', 'drawer.TagItem.<init>', 'CALL', 'Wrap each stored tag as a drawer row',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:473-478')
e('MainActivity.subscribeTags', 'MainActivity.lambda$subscribeTags$10', 'REGISTER', 'Submit current tags to the drawer adapter',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/main/MainActivity.java:480-487')
e('MainActivity.subscribeTags', 'MainActivity.lambda$subscribeTags$10', 'FRAMEWORK', 'Deliver converted tag rows to the activity subscriber',
  cls='non_standard', via='RxJava observeOn/subscribe callback', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/main/MainActivity.java:480-487')
e('MainActivity.lambda$subscribeTags$10', 'MainActivity.setInitSelection', 'CALL', 'Restore the initial drawer tag selection for an empty adapter',
  guard='tagsAdapter.getItemCount() == 0', cls='explicit', evidence='SRC ui/main/MainActivity.java:481-485; ui/main/MainActivity.java:490-527')
e('MainActivity.setInitSelection', 'drawer.TagsAdapter.setSelectedItem', 'CALL', 'Select the all-torrents tag when that preference is stored',
  guard='selectedTagIdStr == tag_empty_item || invalid tag ID', cls='explicit', evidence='SRC ui/main/MainActivity.java:497-511')
e('MainActivity.setInitSelection', 'drawer.TagsAdapter.setSelectedItem', 'CALL', 'Select the no-tags drawer row when that preference is stored',
  guard='selectedTagIdStr == tag_no_tags_item', cls='explicit', evidence='SRC ui/main/MainActivity.java:500-503')
e('MainActivity.setInitSelection', 'MainViewModel.setTagFilter', 'CALL', 'Apply the all-torrents filter for the stored all-torrents selection',
  guard='selectedTagIdStr == tag_empty_item || invalid tag ID', cls='explicit', evidence='SRC ui/main/MainActivity.java:497-511')
e('MainActivity.setInitSelection', 'MainViewModel.setTagFilter', 'CALL', 'Apply the no-tags filter for the stored no-tags selection',
  guard='selectedTagIdStr == tag_no_tags_item', cls='explicit', evidence='SRC ui/main/MainActivity.java:500-503')
e('MainActivity.setInitSelection', 'MainActivity.lambda$setInitSelection$11', 'REGISTER', 'Find the stored tag among drawer items',
  guard='selectedTagIdStr is a valid numeric tag ID', cls='non_standard', via='RxJava filter callback', evidence='INFERRED RxJava filter dispatch; SRC ui/main/MainActivity.java:504-525')
e('MainActivity.setInitSelection', 'MainActivity.lambda$setInitSelection$11', 'FRAMEWORK', 'Test each drawer item against the stored tag ID',
  guard='selectedTagIdStr is a valid numeric tag ID', cls='non_standard', via='RxJava filter callback', evidence='INFERRED RxJava filter dispatch; SRC ui/main/MainActivity.java:513-525')
e('MainActivity.setInitSelection', 'MainActivity.lambda$setInitSelection$12', 'REGISTER', 'Restore a matching tag selection and filter',
  guard='selectedTagIdStr is a valid numeric tag ID', cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/main/MainActivity.java:513-525')
e('MainActivity.lambda$setInitSelection$11', 'MainActivity.lambda$setInitSelection$12', 'FRAMEWORK', 'Deliver the stored tag row when it matches the saved ID',
  guard='item instanceof TagItem && item.info.id == selectedTagId', cls='non_standard', via='RxJava filter/subscribe dispatch', evidence='INFERRED RxJava filter/subscribe dispatch; SRC ui/main/MainActivity.java:513-525')
e('MainActivity.lambda$setInitSelection$12', 'drawer.TagsAdapter.setSelectedItem', 'CALL', 'Select the matching stored tag row',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:518-520')
e('MainActivity.lambda$setInitSelection$12', 'MainViewModel.setTagFilter', 'CALL', 'Apply the matching stored tag filter',
  cls='explicit', evidence='SRC ui/main/MainActivity.java:519-523')
e('MainActivity.initDrawer', 'drawer.TagsAdapter.onCreateViewHolder', 'FRAMEWORK', 'Create tag drawer rows as RecyclerView requests them',
  cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/main/MainActivity.java:248-259,270-272; ui/main/drawer/TagsAdapter.java:64-93')
e('MainActivity.initDrawer', 'drawer.TagsAdapter.onBindViewHolder', 'FRAMEWORK', 'Bind current tag drawer rows',
  cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/main/MainActivity.java:270-272; ui/main/drawer/TagsAdapter.java:95-101')
e('MainActivity.initDrawer', 'drawer.TagsAdapter.getItemViewType', 'FRAMEWORK', 'Choose the tag-row holder type before creating it',
  cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/main/MainActivity.java:270-272; ui/main/drawer/TagsAdapter.java:103-116')
e('MainActivity.initDrawer', 'MainActivity$2.canScrollVertically', 'FRAMEWORK', 'Ask the drawer list layout manager whether vertical scrolling is available',
  cls='non_standard', via='AndroidX RecyclerView LayoutManager dispatch', evidence='INFERRED AndroidX RecyclerView LayoutManager dispatch; SRC ui/main/MainActivity.java:198-204,254-259')
e('drawer.TagsAdapter.onCreateViewHolder', 'drawer.TagsAdapter$EmptyItemViewHolder.<init>', 'CALL', 'Create the all-torrents tag row holder',
  guard='viewType == TYPE_EMPTY_ITEM', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:64-93')
e('drawer.TagsAdapter.onCreateViewHolder', 'drawer.TagsAdapter$ItemViewHolder.<init>', 'CALL', 'Create a stored-tag row holder',
  guard='viewType == TYPE_TAG_ITEM', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:64-93')
e('drawer.TagsAdapter.onCreateViewHolder', 'drawer.TagsAdapter$NoTagsItemViewHolder.<init>', 'CALL', 'Create the no-tags row holder',
  guard='viewType == TYPE_NO_TAGS_ITEM', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:64-93')
e('drawer.TagsAdapter.onBindViewHolder', 'drawer.TagsAdapter$ItemViewHolder.bind(TagItem,OnClickListener)', 'CALL', 'Bind a stored tag row and its click callbacks',
  guard='item != null && item instanceof TagItem', cls='non_standard', via='RecyclerView holder subtype dispatch', evidence='INFERRED RecyclerView holder subtype dispatch; SRC ui/main/drawer/TagsAdapter.java:95-101,179-208')
e('drawer.TagsAdapter.onBindViewHolder', 'drawer.TagsAdapter$EmptyItemViewHolder.bind(EmptyTagItem,OnClickListener)', 'CALL', 'Bind the all-torrents row click callback',
  guard='item != null && item instanceof EmptyTagItem', cls='non_standard', via='RecyclerView holder subtype dispatch', evidence='INFERRED RecyclerView holder subtype dispatch; SRC ui/main/drawer/TagsAdapter.java:95-101,232-255')
e('drawer.TagsAdapter.onBindViewHolder', 'drawer.TagsAdapter$NoTagsItemViewHolder.bind(NoTagsItem,OnClickListener)', 'CALL', 'Bind the no-tags row click callback',
  guard='item != null && item instanceof NoTagsItem', cls='non_standard', via='RecyclerView holder subtype dispatch', evidence='INFERRED RecyclerView holder subtype dispatch; SRC ui/main/drawer/TagsAdapter.java:95-101,279-301')
e('drawer.TagsAdapter$ItemViewHolder.bind(TagItem,OnClickListener)', 'drawer.TagsAdapter$ItemViewHolder.lambda$bind$0', 'REGISTER', 'Register selection click for a stored tag row',
  cls='standard', evidence='SRC ui/main/drawer/TagsAdapter.java:192-197; FW-SRC core/java/android/view/View.java:6143-6158')
e('drawer.TagsAdapter$ItemViewHolder.bind(TagItem,OnClickListener)', 'drawer.TagsAdapter$ItemViewHolder.lambda$bind$0', 'FRAMEWORK', 'Dispatch a tap on a stored tag row',
  cls='standard', evidence='SRC ui/main/drawer/TagsAdapter.java:192-197; FW-SRC core/java/android/view/View.java:6289-6305')
e('drawer.TagsAdapter$ItemViewHolder.lambda$bind$0', 'drawer.TagsAdapter.setSelectedItem', 'CALL', 'Mark the tapped tag row as selected',
  cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:192-197')
e('drawer.TagsAdapter$ItemViewHolder.lambda$bind$0', 'MainActivity$3.onTagSelected', 'CALL', 'Apply the selected tag filter',
  guard='listener != null', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:192-197; ui/main/MainActivity.java:300-327')
e('drawer.TagsAdapter$ItemViewHolder.bind(TagItem,OnClickListener)', 'drawer.TagsAdapter$ItemViewHolder.lambda$bind$1', 'REGISTER', 'Register the stored-tag overflow menu click',
  cls='standard', evidence='SRC ui/main/drawer/TagsAdapter.java:198-208; FW-SRC core/java/android/view/View.java:6143-6158')
e('drawer.TagsAdapter$ItemViewHolder.bind(TagItem,OnClickListener)', 'drawer.TagsAdapter$ItemViewHolder.lambda$bind$1', 'FRAMEWORK', 'Dispatch a tap on the stored-tag overflow button',
  cls='standard', evidence='SRC ui/main/drawer/TagsAdapter.java:198-208; FW-SRC core/java/android/view/View.java:6289-6305')
e('drawer.TagsAdapter$ItemViewHolder.lambda$bind$1', 'drawer.TagsAdapter$ItemViewHolder.lambda$bind$2', 'REGISTER', 'Register popup-menu item action callback',
  cls='non_standard', via='Android PopupMenu listener', evidence='INFERRED Android PopupMenu callback dispatch; SRC ui/main/drawer/TagsAdapter.java:198-208')
e('drawer.TagsAdapter$ItemViewHolder.lambda$bind$1', 'drawer.TagsAdapter$ItemViewHolder.lambda$bind$2', 'FRAMEWORK', 'Dispatch selected popup-menu action',
  cls='non_standard', via='Android PopupMenu listener', evidence='INFERRED Android PopupMenu callback dispatch; SRC ui/main/drawer/TagsAdapter.java:198-208')
e('drawer.TagsAdapter$ItemViewHolder.lambda$bind$2', 'MainActivity$3.onTagMenuClicked', 'CALL', 'Handle edit or delete action for a stored tag',
  guard='listener != null', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:201-205; ui/main/MainActivity.java:314-358')
e('drawer.TagsAdapter$EmptyItemViewHolder.bind(EmptyTagItem,OnClickListener)', 'drawer.TagsAdapter$EmptyItemViewHolder.lambda$bind$0', 'REGISTER', 'Register selection click for all torrents',
  cls='standard', evidence='SRC ui/main/drawer/TagsAdapter.java:247-255; FW-SRC core/java/android/view/View.java:6143-6158')
e('drawer.TagsAdapter$EmptyItemViewHolder.bind(EmptyTagItem,OnClickListener)', 'drawer.TagsAdapter$EmptyItemViewHolder.lambda$bind$0', 'FRAMEWORK', 'Dispatch a tap on the all-torrents row',
  cls='standard', evidence='SRC ui/main/drawer/TagsAdapter.java:247-255; FW-SRC core/java/android/view/View.java:6289-6305')
e('drawer.TagsAdapter$EmptyItemViewHolder.lambda$bind$0', 'MainActivity$3.onTagSelected', 'CALL', 'Apply the all-torrents filter',
  guard='listener != null', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:249-254; ui/main/MainActivity.java:300-327')
e('drawer.TagsAdapter$NoTagsItemViewHolder.bind(NoTagsItem,OnClickListener)', 'drawer.TagsAdapter$NoTagsItemViewHolder.lambda$bind$0', 'REGISTER', 'Register selection click for torrents without tags',
  cls='standard', evidence='SRC ui/main/drawer/TagsAdapter.java:293-301; FW-SRC core/java/android/view/View.java:6143-6158')
e('drawer.TagsAdapter$NoTagsItemViewHolder.bind(NoTagsItem,OnClickListener)', 'drawer.TagsAdapter$NoTagsItemViewHolder.lambda$bind$0', 'FRAMEWORK', 'Dispatch a tap on the no-tags row',
  cls='standard', evidence='SRC ui/main/drawer/TagsAdapter.java:293-301; FW-SRC core/java/android/view/View.java:6289-6305')
e('drawer.TagsAdapter$NoTagsItemViewHolder.lambda$bind$0', 'MainActivity$3.onTagSelected', 'CALL', 'Apply the no-tags filter',
  guard='listener != null', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:295-300; ui/main/MainActivity.java:300-327')
e('DetailTorrentInfoFragment.onCreateView', 'TorrentTagsList.setListener', 'CALL', 'Install add/remove callbacks on the detail tag list',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:110-114; ui/tag/TorrentTagsList.java:40-42')
e('DetailTorrentInfoFragment.subscribeTags', 'DetailTorrentViewModel.observeTags', 'CALL', 'Observe the torrent tag collection',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:177-182')
e('DetailTorrentInfoFragment.subscribeTags', 'TorrentTagsList.submit', 'REGISTER', 'Submit tag updates through the Rx subscriber',
  cls='non_standard', via='RxJava Observable.subscribe method reference', evidence='INFERRED RxJava subscriber dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:177-182; ui/tag/TorrentTagsList.java:44-52')
e('DetailTorrentInfoFragment.subscribeTags', 'TorrentTagsList.submit', 'FRAMEWORK', 'Deliver observed tags to the tag-list view',
  cls='non_standard', via='RxJava observeOn/subscribe method reference', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:177-182; ui/tag/TorrentTagsList.java:44-52')
e('TorrentTagsList.submit', 'TorrentTagsList.buildChip', 'CALL', 'Build a chip for each observed tag',
  cls='explicit', evidence='SRC ui/tag/TorrentTagsList.java:44-52,54-75')
e('TorrentTagsList.buildChip', 'TorrentTagsList.lambda$buildChip$0', 'REGISTER', 'Register close-icon tag removal callback',
  cls='non_standard', via='Material Chip close-icon listener', evidence='INFERRED Material Chip callback dispatch; SRC ui/tag/TorrentTagsList.java:54-75')
e('TorrentTagsList.buildChip', 'TorrentTagsList.lambda$buildChip$0', 'FRAMEWORK', 'Deliver a tag chip close-icon tap',
  cls='non_standard', via='Material Chip close-icon listener', evidence='INFERRED Material Chip close-icon dispatch; SRC ui/tag/TorrentTagsList.java:54-75')
e('TorrentTagsList.lambda$buildChip$0', 'DetailTorrentInfoFragment$1.onTagRemoved', 'CALL', 'Remove the selected tag from torrent details',
  guard='listener != null', cls='explicit', evidence='SRC ui/tag/TorrentTagsList.java:69-73; ui/detailtorrent/pages/DetailTorrentInfoFragment.java:147-174')
e('DetailTorrentInfoFragment$1.onTagRemoved', 'DetailTorrentViewModel.removeTag', 'CALL', 'Remove the tag from detail torrent state',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:168-174')
e('DetailTorrentTrackersFragment.deleteTrackers', 'DetailTorrentTrackersFragment.lambda$deleteTrackers$3', 'REGISTER', 'Map selected tracker rows to their URLs',
  cls='non_standard', via='RxJava map callback', evidence='INFERRED RxJava map dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:360-368')
e('DetailTorrentTrackersFragment.deleteTrackers', 'DetailTorrentTrackersFragment.lambda$deleteTrackers$3', 'FRAMEWORK', 'Invoke selected-tracker URL mapping callback',
  cls='non_standard', via='RxJava map callback', evidence='INFERRED RxJava map dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:362-368')
e('DetailTorrentTrackersFragment.deleteTrackers', 'DetailTorrentTrackersFragment.lambda$deleteTrackers$4', 'REGISTER', 'Delete selected tracker URLs after collecting them',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava toList/subscribe dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:365-368')
e('DetailTorrentTrackersFragment.deleteTrackers', 'DetailTorrentTrackersFragment.lambda$deleteTrackers$4', 'FRAMEWORK', 'Deliver selected tracker URLs to the delete subscriber',
  cls='non_standard', via='RxJava toList/subscribe callback', evidence='INFERRED RxJava toList/subscribe dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:365-368')
e('DetailTorrentTrackersFragment.lambda$deleteTrackers$4', 'DetailTorrentViewModel.deleteTrackers', 'CALL', 'Delete selected tracker URLs in the view model',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:365-368')
e('DetailTorrentTrackersFragment.shareUrl', 'DetailTorrentTrackersFragment.lambda$shareUrl$5', 'REGISTER', 'Map selected tracker rows to URLs for sharing',
  cls='non_standard', via='RxJava map callback', evidence='INFERRED RxJava map dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:374-394')
e('DetailTorrentTrackersFragment.shareUrl', 'DetailTorrentTrackersFragment.lambda$shareUrl$5', 'FRAMEWORK', 'Invoke selected-tracker URL mapping for sharing',
  cls='non_standard', via='RxJava map callback', evidence='INFERRED RxJava map dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:376-394')
e('DetailTorrentTrackersFragment.shareUrl', 'DetailTorrentTrackersFragment.lambda$shareUrl$6', 'REGISTER', 'Build the share chooser from selected tracker URLs',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava toList/subscribe dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:379-394')
e('DetailTorrentTrackersFragment.shareUrl', 'DetailTorrentTrackersFragment.lambda$shareUrl$6', 'FRAMEWORK', 'Deliver selected URLs to the share chooser subscriber',
  cls='non_standard', via='RxJava toList/subscribe callback', evidence='INFERRED RxJava toList/subscribe dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:379-394')
e('DetailTorrentPeersFragment.onViewCreated', 'PeerListAdapter.onBindViewHolder', 'FRAMEWORK', 'Bind peer rows displayed by RecyclerView',
  cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:123-142; ui/detailtorrent/pages/peers/PeerListAdapter.java:71-74')
e('PeerListAdapter.onBindViewHolder', 'PeerListAdapter$ViewHolder.bind', 'CALL', 'Bind peer row details and the long-click listener',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:71-74')
e('PeerListAdapter$ViewHolder.bind', 'PeerListAdapter$ViewHolder.lambda$bind$0', 'REGISTER', 'Register peer row long-click handler',
  cls='standard', evidence='SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:134-143; FW-SRC core/java/android/view/View.java:6165-6170')
e('PeerListAdapter$ViewHolder.bind', 'PeerListAdapter$ViewHolder.lambda$bind$0', 'FRAMEWORK', 'Dispatch a long press on a peer row',
  cls='standard', evidence='SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:134-143; FW-SRC core/java/android/view/View.java:6320-6345')
e('PeerListAdapter$ViewHolder.lambda$bind$0', 'DetailTorrentPeersFragment.onItemLongClick', 'CALL', 'Share the peer address when its row is long-pressed',
  guard='listener != null', cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:138-143; ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:185-190')
e('DetailTorrentPeersFragment.onItemLongClick', 'DetailTorrentPeersFragment.sharePeerIp', 'CALL', 'Open a share chooser for the peer IP address',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:185-190')
e('DetailTorrentPeersFragment.subscribeAdapter', 'DetailTorrentPeersFragment.lambda$subscribeAdapter$0', 'REGISTER', 'Convert observed peers into list items',
  cls='non_standard', via='RxJava flatMapSingle callback', evidence='INFERRED RxJava flatMapSingle dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:172-180')
e('DetailTorrentPeersFragment.subscribeAdapter', 'DetailTorrentPeersFragment.lambda$subscribeAdapter$0', 'FRAMEWORK', 'Invoke peer-list conversion callback',
  cls='non_standard', via='RxJava flatMapSingle callback', evidence='INFERRED RxJava flatMapSingle dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:172-180')
e('DetailTorrentPeersFragment.lambda$subscribeAdapter$0', 'PeerItem.<init>', 'CALL', 'Wrap each observed peer for display',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:176-180')
e('DetailTorrentPeersFragment.subscribeAdapter', 'DetailTorrentPeersFragment.lambda$subscribeAdapter$1', 'REGISTER', 'Submit peer updates on the main thread',
  cls='non_standard', via='RxJava subscribe callback', evidence='INFERRED RxJava subscribe dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:174-182')
e('DetailTorrentPeersFragment.subscribeAdapter', 'DetailTorrentPeersFragment.lambda$subscribeAdapter$1', 'FRAMEWORK', 'Deliver converted peers to the list subscriber',
  cls='non_standard', via='RxJava observeOn/subscribe callback', evidence='INFERRED RxJava observeOn/subscribe dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:181-182')
e('DetailTorrentPeersFragment.lambda$subscribeAdapter$1', 'PeerListAdapter.submitList', 'CALL', 'Display the updated peer list',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:181-182')
e('DetailTorrentTrackersFragment.newInstance', 'DetailTorrentTrackersFragment.<init>', 'CALL', 'Instantiate tracker list page',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:93-100')
e('DetailTorrentTrackersFragment.newInstance', 'DetailTorrentTrackersFragment.onAttach', 'LIFECYCLE', 'Attach tracker list page',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:93-120')
e('DetailTorrentTrackersFragment.onAttach', 'DetailTorrentTrackersFragment.onCreateView', 'LIFECYCLE', 'Inflate tracker list page view',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:103-135')
e('DetailTorrentTrackersFragment.onCreateView', 'DetailTorrentTrackersFragment.onViewCreated', 'LIFECYCLE', 'Initialize tracker list and adapter',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:146-242')
e('DetailTorrentTrackersFragment.onViewCreated', 'DetailTorrentTrackersFragment.onStart', 'LIFECYCLE', 'Start tracker page observers',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:137-144,146-242')
e('DetailTorrentTrackersFragment.onStart', 'DetailTorrentTrackersFragment.subscribeAdapter', 'CALL', 'Subscribe to tracker rows',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:137-144')
e('DetailTorrentTrackersFragment.onStart', 'DetailTorrentTrackersFragment.subscribeAlertDialog', 'CALL', 'Subscribe to tracker dialog events',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:137-144')
e('DetailTorrentPeersFragment.newInstance', 'DetailTorrentPeersFragment.<init>', 'CALL', 'Instantiate peer list page',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:72-79')
e('DetailTorrentPeersFragment.newInstance', 'DetailTorrentPeersFragment.onAttach', 'LIFECYCLE', 'Attach peer list page',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:72-99')
e('DetailTorrentPeersFragment.onAttach', 'DetailTorrentPeersFragment.onCreateView', 'LIFECYCLE', 'Inflate peer list page view',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:82-104')
e('DetailTorrentPeersFragment.onCreateView', 'DetailTorrentPeersFragment.onViewCreated', 'LIFECYCLE', 'Initialize peer list and adapter',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:115-164')
e('DetailTorrentPeersFragment.onViewCreated', 'DetailTorrentPeersFragment.onStart', 'LIFECYCLE', 'Start peer list observer',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:107-112,115-164')
e('DetailTorrentPeersFragment.onStart', 'DetailTorrentPeersFragment.subscribeAdapter', 'CALL', 'Subscribe to peer list updates',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:107-113')
e('DetailTorrentPiecesFragment.newInstance', 'DetailTorrentPiecesFragment.<init>', 'CALL', 'Instantiate pieces visualization page',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:59-66')
e('DetailTorrentPiecesFragment.newInstance', 'DetailTorrentPiecesFragment.onAttach', 'LIFECYCLE', 'Attach pieces visualization page',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:59-86')
e('DetailTorrentPiecesFragment.onAttach', 'DetailTorrentPiecesFragment.onCreateView', 'LIFECYCLE', 'Inflate pieces visualization view',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:69-91')
e('DetailTorrentPiecesFragment.onCreateView', 'DetailTorrentPiecesFragment.onViewCreated', 'LIFECYCLE', 'Initialize pieces view',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:102-125')
e('DetailTorrentPiecesFragment.onViewCreated', 'DetailTorrentPiecesFragment.onStart', 'LIFECYCLE', 'Start pieces data subscription',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:94-99,102-125')
e('DetailTorrentPiecesFragment.onStart', 'DetailTorrentPiecesFragment.subscribeAdapter', 'CALL', 'Subscribe pieces view to torrent state',
  cls='explicit', evidence='SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:94-100')
e('AddFeedActivity.onCreate', 'AddFeedDialog.newInstance(long)', 'CALL', 'Create edit-feed dialog for an edit action',
  guard='ACTION_EDIT_FEED.equals(intent.getAction())', cls='explicit', evidence='SRC ui/addfeed/AddFeedActivity.java:45-67; ui/addfeed/AddFeedDialog.java:73-93')
e('AddFeedActivity.onCreate', 'AddFeedActivity.getUriFromIntent', 'CALL', 'Read incoming feed URI for add mode',
  guard='intent action is not ACTION_EDIT_FEED', cls='explicit', evidence='SRC ui/addfeed/AddFeedActivity.java:45-67,70-83')
e('AddFeedActivity.onCreate', 'AddFeedDialog.newInstance(Uri)', 'CALL', 'Create add-feed dialog for incoming link or URI',
  guard='intent action is not ACTION_EDIT_FEED', cls='explicit', evidence='SRC ui/addfeed/AddFeedActivity.java:54-67,70-83; ui/addfeed/AddFeedDialog.java:73-82')
e('AddFeedDialog.newInstance(long)', 'AddFeedDialog.<init>', 'CALL', 'Instantiate feed editor dialog',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:84-93')
e('AddFeedDialog.newInstance(Uri)', 'AddFeedDialog.<init>', 'CALL', 'Instantiate feed add dialog',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:73-82')
e('AddFeedDialog.newInstance(Uri)', 'AddFeedDialog.onAttach', 'LIFECYCLE', 'Attach feed dialog to host activity',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/addfeed/AddFeedDialog.java:73-82,135-145')
e('AddFeedDialog.onAttach', 'AddFeedDialog.onCreateDialog', 'LIFECYCLE', 'Initialize feed dialog and view model',
  cls='non_standard', via='AndroidX DialogFragment lifecycle', evidence='INFERRED AndroidX DialogFragment lifecycle dispatch; SRC ui/addfeed/AddFeedDialog.java:165-209')
e('AddFeedDialog.onCreateDialog', 'AddFeedDialog.initParams', 'CALL', 'Initialize add, edit, or clipboard feed values',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:165-209,135-145')
e('AddFeedDialog.initParams', 'AddFeedViewModel.initAddMode', 'CALL', 'Initialize add mode from a supplied URI',
  guard='uri != null', cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:135-145; ui/addfeed/AddFeedViewModel.java:80-85')
e('AddFeedDialog.initParams', 'AddFeedViewModel.initEditMode', 'CALL', 'Initialize edit mode from feed ID',
  guard='uri == null && feedId != -1', cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:135-145; ui/addfeed/AddFeedViewModel.java:99-104')
e('AddFeedDialog.initParams', 'AddFeedViewModel.initAddModeFromClipboard', 'CALL', 'Initialize add mode from clipboard when no URI or feed ID is supplied',
  guard='uri == null && feedId == -1', cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:135-145; ui/addfeed/AddFeedViewModel.java:87-97')
e('AddFeedDialog.onCreateDialog', 'AddFeedDialog.initLayoutView', 'CALL', 'Initialize feed fields and clipboard controls',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:165-209,211-242')
e('AddFeedDialog.onCreateDialog', 'AddFeedDialog.initAlertDialog', 'CALL', 'Build add/edit/delete feed actions',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:230-242,244-282')
e('AddFeedDialog.onStart', 'AddFeedDialog.subscribeAlertDialog', 'CALL', 'Observe delete confirmation and clipboard selection',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:157-163,285-312')
e('AddFeedDialog.onStart', 'AddFeedDialog.subscribeClipboardManager', 'CALL', 'Listen for clipboard changes while dialog is visible',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:157-163,98-107')
e('AddFeedDialog.onBackPressed', 'AddFeedDialog.finish', 'CALL', 'Dismiss feed editor on back',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:424-427')
e('AddFeedDialog.finish', 'AddFeedActivity.onFragmentFinished', 'CALL', 'Notify add-feed activity that dialog closed',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedDialog.java:429-432; ui/addfeed/AddFeedActivity.java:84-88')
e('AddFeedActivity.onBackPressed', 'AddFeedDialog.onBackPressed', 'CALL', 'Forward activity back action to feed dialog',
  cls='explicit', evidence='SRC ui/addfeed/AddFeedActivity.java:90-94; ui/addfeed/AddFeedDialog.java:424-427')
e('SettingsActivity.onCreate', 'SettingsFragment.<init>', 'FRAMEWORK', 'Inflate settings fragment from selected settings layout',
  cls='non_standard', via='AndroidX FragmentContainerView', evidence='INFERRED AndroidX FragmentContainerView inflation; SRC ui/settings/SettingsActivity.java:45-60; res/layout/activity_settings_portrait.xml:8-14; res/layout/activity_settings_two_pane.xml:19-25')
e('SettingsActivity.onCreate', 'SettingsActivity.lambda$onCreate$0', 'REGISTER', 'Observe settings detail-title changes through LiveData',
  cls='non_standard', via='AndroidX LiveData', evidence='INFERRED AndroidX LiveData observer dispatch; SRC ui/settings/SettingsActivity.java:57-61')
e('SettingsActivity.onCreate', 'SettingsActivity.lambda$onCreate$0', 'FRAMEWORK', 'Deliver a settings detail-title update to the activity observer',
  cls='non_standard', via='AndroidX LiveData', evidence='INFERRED AndroidX LiveData observer dispatch; SRC ui/settings/SettingsActivity.java:57-61')
e('SettingsActivity.onCreate', 'SettingsActivity.onOptionsItemSelected', 'FRAMEWORK', 'Dispatch the toolbar home action through the AppCompat action bar',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu dispatch; SRC ui/settings/SettingsActivity.java:49-55,64-72; FW-SRC core/java/android/app/Activity.java:3431-3451')
e('AddFeedActivity.onCreate', 'AddFeedActivity.onBackPressed', 'FRAMEWORK', 'Forward Back key handling to the feed dialog while the activity is active',
  guard='keyCode == KEYCODE_BACK && event.isTracking() && !event.isCanceled() && targetSdkVersion >= ECLAIR', cls='standard', evidence='SRC ui/addfeed/AddFeedActivity.java:90-93; FW-SRC core/java/android/app/Activity.java:2975-2983')
e('SettingsFragment.<init>', 'SettingsFragment.onAttach', 'LIFECYCLE', 'Attach settings preferences fragment',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/settings/SettingsFragment.java:71-80')
e('SettingsFragment.onAttach', 'SettingsFragment.onCreatePreferences', 'LIFECYCLE', 'Load settings preference headers',
  cls='non_standard', via='AndroidX PreferenceFragmentCompat', evidence='INFERRED AndroidX PreferenceFragmentCompat callback dispatch; SRC ui/settings/SettingsFragment.java:215-218')
e('SettingsFragment.onCreatePreferences', 'SettingsFragment.onViewCreated', 'LIFECYCLE', 'Register settings header click listeners',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/settings/SettingsFragment.java:82-131,215-218')
e('SettingsFragment.onViewCreated', 'SettingsFragment.lambda$new$0', 'REGISTER', 'Register settings preference header click listener',
  cls='non_standard', via='AndroidX Preference click listener', evidence='INFERRED AndroidX Preference dispatch; SRC ui/settings/SettingsFragment.java:82-131')
e('SettingsFragment.onViewCreated', 'SettingsFragment.lambda$new$0', 'FRAMEWORK', 'Dispatch a click on a settings preference header',
  cls='non_standard', via='AndroidX Preference click listener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/SettingsFragment.java:82-131')
e('SettingsFragment.lambda$new$0', 'SettingsFragment.openPreference', 'CALL', 'Open settings category selected by user',
  cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:129-132,134-213')
e('SettingsFragment.onViewCreated', 'AppearanceSettingsFragment.newInstance', 'CALL', 'Create the default appearance page when the two-pane detail container is empty',
  guard='Utils.isTwoPane(activity) && f == null', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:90-96; ui/settings/sections/AppearanceSettingsFragment.java:57-62')
e('SettingsFragment.onViewCreated', 'SettingsFragment.setFragment', 'CALL', 'Install the default appearance page in the two-pane detail container',
  guard='Utils.isTwoPane(activity) && f == null', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:90-96,220-230')
e('SettingsFragment.openPreference', 'AppearanceSettingsFragment.newInstance', 'CALL', 'Create appearance settings page for two-pane display',
  guard='prefName == AppearanceSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:138-146; ui/settings/sections/AppearanceSettingsFragment.java:57-62')
e('SettingsFragment.openPreference', 'SettingsFragment.setFragment', 'CALL', 'Show appearance settings in two-pane layout',
  guard='prefName == AppearanceSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:138-146,220-230')
e('SettingsFragment.openPreference', 'SettingsFragment.startActivity', 'CALL', 'Open appearance settings activity in single-pane layout',
  guard='prefName == AppearanceSettings && !Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:138-146,232-240')
e('SettingsFragment.openPreference', 'SettingsFragment.setFragment', 'CALL', 'Show behavior settings in two-pane layout',
  guard='prefName == BehaviorSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:147-155,220-230')
e('SettingsFragment.openPreference', 'BehaviorSettingsFragment.newInstance', 'CALL', 'Create behavior settings page for two-pane display',
  guard='prefName == BehaviorSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:147-155; ui/settings/sections/BehaviorSettingsFragment.java:53-58')
e('SettingsFragment.openPreference', 'SettingsFragment.startActivity', 'CALL', 'Open behavior settings activity in single-pane layout',
  guard='prefName == BehaviorSettings && !Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:147-155,232-240')
e('SettingsFragment.openPreference', 'SettingsFragment.setFragment', 'CALL', 'Show network settings in two-pane layout',
  guard='prefName == NetworkSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:156-164,220-230')
e('SettingsFragment.openPreference', 'NetworkSettingsFragment.newInstance', 'CALL', 'Create network settings page for two-pane display',
  guard='prefName == NetworkSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:156-164; ui/settings/sections/NetworkSettingsFragment.java:77-82')
e('SettingsFragment.openPreference', 'SettingsFragment.startActivity', 'CALL', 'Open network settings activity in single-pane layout',
  guard='prefName == NetworkSettings && !Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:156-164,232-240')
e('SettingsFragment.openPreference', 'SettingsFragment.setFragment', 'CALL', 'Show storage settings in two-pane layout',
  guard='prefName == StorageSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:165-173,220-230')
e('SettingsFragment.openPreference', 'StorageSettingsFragment.newInstance', 'CALL', 'Create storage settings page for two-pane display',
  guard='prefName == StorageSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:165-173; ui/settings/sections/StorageSettingsFragment.java:64-69')
e('SettingsFragment.openPreference', 'SettingsFragment.startActivity', 'CALL', 'Open storage settings activity in single-pane layout',
  guard='prefName == StorageSettings && !Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:165-173,232-240')
e('SettingsFragment.openPreference', 'SettingsFragment.setFragment', 'CALL', 'Show limitations settings in two-pane layout',
  guard='prefName == LimitationsSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:174-182,220-230')
e('SettingsFragment.openPreference', 'LimitationsSettingsFragment.newInstance', 'CALL', 'Create limitations settings page for two-pane display',
  guard='prefName == LimitationsSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:174-182; ui/settings/sections/LimitationsSettingsFragment.java:44-49')
e('SettingsFragment.openPreference', 'SettingsFragment.startActivity', 'CALL', 'Open limitations settings activity in single-pane layout',
  guard='prefName == LimitationsSettings && !Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:174-182,232-240')
e('SettingsFragment.openPreference', 'SettingsFragment.setFragment', 'CALL', 'Show scheduling settings in two-pane layout',
  guard='prefName == SchedulingSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:183-191,220-230')
e('SettingsFragment.openPreference', 'SchedulingSettingsFragment.newInstance', 'CALL', 'Create scheduling settings page for two-pane display',
  guard='prefName == SchedulingSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:183-191; ui/settings/sections/SchedulingSettingsFragment.java:53-58')
e('SettingsFragment.openPreference', 'SettingsFragment.startActivity', 'CALL', 'Open scheduling settings activity in single-pane layout',
  guard='prefName == SchedulingSettings && !Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:183-191,232-240')
e('SettingsFragment.openPreference', 'SettingsFragment.setFragment', 'CALL', 'Show feed settings in two-pane layout',
  guard='prefName == FeedSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:192-200,220-230')
e('SettingsFragment.openPreference', 'FeedSettingsFragment.newInstance', 'CALL', 'Create feed settings page for two-pane display',
  guard='prefName == FeedSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:192-200; ui/settings/sections/FeedSettingsFragment.java:42-47')
e('SettingsFragment.openPreference', 'SettingsFragment.startActivity', 'CALL', 'Open feed settings activity in single-pane layout',
  guard='prefName == FeedSettings && !Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:192-200,232-240')
e('SettingsFragment.openPreference', 'SettingsFragment.setFragment', 'CALL', 'Show streaming settings in two-pane layout',
  guard='prefName == StreamingSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:201-209,220-230')
e('SettingsFragment.openPreference', 'StreamingSettingsFragment.newInstance', 'CALL', 'Create streaming settings page for two-pane display',
  guard='prefName == StreamingSettings && Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:201-209; ui/settings/sections/StreamingSettingsFragment.java:43-48')
e('SettingsFragment.openPreference', 'SettingsFragment.startActivity', 'CALL', 'Open streaming settings activity in single-pane layout',
  guard='prefName == StreamingSettings && !Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:201-209,232-240')
e('SettingsFragment.startActivity', 'PreferenceActivity.<init>', 'INTENT', 'Start single-pane preference host activity',
  cls='standard', evidence='SRC ui/settings/SettingsFragment.java:232-240; AndroidManifest.xml:168-170; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('SettingsFragment.startActivity', 'PreferenceActivity.onCreate', 'INTENT', 'Create single-pane preference host activity',
  cls='standard', evidence='SRC ui/settings/SettingsFragment.java:232-240; AndroidManifest.xml:168-170; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('PreferenceActivity.onCreate', 'PreferenceActivity.getFragment', 'CALL', 'Resolve configured preference fragment',
  guard='intent contains PreferenceActivity.TAG_CONFIG && !Utils.isLargeScreenDevice(this)', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:45-84,101-139; ui/settings/PreferenceActivityConfig.java:51-54')
e('PreferenceActivity.onCreate', 'PreferenceActivity.setFragment', 'CALL', 'Install resolved fragment into preference host',
  guard='fragment != null && savedInstanceState == null', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:76-84,89-99')
e('PreferenceActivity.getFragment', 'AppearanceSettingsFragment.newInstance', 'CALL', 'Create appearance settings page',
  guard='fragment == AppearanceSettingsFragment.class.getSimpleName()', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:101-137')
e('PreferenceActivity.getFragment', 'BehaviorSettingsFragment.newInstance', 'CALL', 'Create behavior settings page',
  guard='fragment == BehaviorSettingsFragment.class.getSimpleName()', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:101-137')
e('PreferenceActivity.getFragment', 'StorageSettingsFragment.newInstance', 'CALL', 'Create storage settings page',
  guard='fragment == StorageSettingsFragment.class.getSimpleName()', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:101-137')
e('PreferenceActivity.getFragment', 'LimitationsSettingsFragment.newInstance', 'CALL', 'Create limitations settings page',
  guard='fragment == LimitationsSettingsFragment.class.getSimpleName()', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:101-137')
e('PreferenceActivity.getFragment', 'NetworkSettingsFragment.newInstance', 'CALL', 'Create network settings page',
  guard='fragment == NetworkSettingsFragment.class.getSimpleName()', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:101-137')
e('PreferenceActivity.getFragment', 'SchedulingSettingsFragment.newInstance', 'CALL', 'Create scheduling settings page',
  guard='fragment == SchedulingSettingsFragment.class.getSimpleName()', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:101-137')
e('PreferenceActivity.getFragment', 'FeedSettingsFragment.newInstance', 'CALL', 'Create feed settings page',
  guard='fragment == FeedSettingsFragment.class.getSimpleName()', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:101-137')
e('PreferenceActivity.getFragment', 'StreamingSettingsFragment.newInstance', 'CALL', 'Create streaming settings page',
  guard='fragment == StreamingSettingsFragment.class.getSimpleName()', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:101-137')
e('AppearanceSettingsFragment.newInstance', 'AppearanceSettingsFragment.<init>', 'CALL', 'Instantiate the appearance settings fragment',
  cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:57-63')
e('BehaviorSettingsFragment.newInstance', 'BehaviorSettingsFragment.<init>', 'CALL', 'Instantiate the behavior settings fragment',
  cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:53-59')
e('NetworkSettingsFragment.newInstance', 'NetworkSettingsFragment.<init>', 'CALL', 'Instantiate the network settings fragment',
  cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:77-83')
e('StorageSettingsFragment.newInstance', 'StorageSettingsFragment.<init>', 'CALL', 'Instantiate the storage settings fragment',
  cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:64-70')
e('LimitationsSettingsFragment.newInstance', 'LimitationsSettingsFragment.<init>', 'CALL', 'Instantiate the limitations settings fragment',
  cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:44-50')
e('SchedulingSettingsFragment.newInstance', 'SchedulingSettingsFragment.<init>', 'CALL', 'Instantiate the scheduling settings fragment',
  cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:53-59')
e('FeedSettingsFragment.newInstance', 'FeedSettingsFragment.<init>', 'CALL', 'Instantiate the feed settings fragment',
  cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:42-48')
e('StreamingSettingsFragment.newInstance', 'StreamingSettingsFragment.<init>', 'CALL', 'Instantiate the streaming settings fragment',
  cls='explicit', evidence='SRC ui/settings/sections/StreamingSettingsFragment.java:43-49')
e('AppearanceSettingsFragment.<init>', 'AppearanceSettingsFragment.onCreate', 'LIFECYCLE', 'Create appearance settings after FragmentManager installs the page',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/AppearanceSettingsFragment.java:57-75')
e('AppearanceSettingsFragment.onCreate', 'AppearanceSettingsFragment.onCreatePreferences', 'LIFECYCLE', 'Load appearance preference definitions',
  cls='non_standard', via='AndroidX PreferenceFragmentCompat', evidence='INFERRED AndroidX PreferenceFragmentCompat callback dispatch; SRC ui/settings/sections/AppearanceSettingsFragment.java:74-75,193-199')
e('AppearanceSettingsFragment.onCreate', 'RepositoryHelper.getSettingsRepository', 'CALL', 'Obtain the shared settings repository for appearance preferences',
  cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:74-79; core/RepositoryHelper.java:61-67')
e('RepositoryHelper.getSettingsRepository', 'SettingsRepositoryImpl.<init>', 'CALL', 'Create the settings repository on first access',
  guard='settingsRepo == null', cls='explicit', evidence='SRC core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:184-192')
e('AppearanceSettingsFragment.onCreate', 'AppearanceSettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'Register listeners on the appearance preferences that exist',
  guard='preference != null', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:74-188,219-221')
e('AppearanceSettingsFragment.onCreate', 'AppearanceSettingsFragment.initLegacyNotifySettings', 'CALL', 'Initialize notification preferences on Android versions below Oreo',
  guard='Build.VERSION.SDK_INT < Build.VERSION_CODES.O', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:118-120,128-190')
e('AppearanceSettingsFragment.bindOnPreferenceChangeListener', 'AppearanceSettingsFragment.onPreferenceChange', 'REGISTER', 'Register the appearance preference change listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/AppearanceSettingsFragment.java:219-221,224-263')
e('AppearanceSettingsFragment.bindOnPreferenceChangeListener', 'AppearanceSettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Dispatch appearance preference changes to the registered listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/AppearanceSettingsFragment.java:219-221,224-263')
e('AppearanceSettingsFragment.onCreatePreferences', 'AppearanceSettingsFragment.onViewCreated', 'LIFECYCLE', 'Initialize appearance page view after preference view inflation',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/settings/sections/AppearanceSettingsFragment.java:66-72,193-199')
e('AppearanceSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.theme(int)', 'CALL', 'Persist a changed theme preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_theme))', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:227-235; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:329-340')
e('AppearanceSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.torrentFinishNotify(boolean)', 'CALL', 'Persist the torrent-finished notification setting',
  guard='preference.getKey().equals(getString(R.string.pref_key_torrent_finish_notify))', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:237-239; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:277-288')
e('AppearanceSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.playSoundNotify(boolean)', 'CALL', 'Persist the legacy notification sound toggle',
  guard='preference.getKey().equals(getString(R.string.pref_key_play_sound_notify))', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:240-242; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:290-301')
e('AppearanceSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.ledIndicatorNotify(boolean)', 'CALL', 'Persist the legacy LED notification toggle',
  guard='preference.getKey().equals(getString(R.string.pref_key_led_indicator_notify))', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:243-245; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:303-314')
e('AppearanceSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.vibrationNotify(boolean)', 'CALL', 'Persist the legacy vibration notification toggle',
  guard='preference.getKey().equals(getString(R.string.pref_key_vibration_notify))', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:246-248; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:316-327')
e('AppearanceSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.ledIndicatorColorNotify(int)', 'CALL', 'Persist the legacy notification LED color',
  guard='preference.getKey().equals(getString(R.string.pref_key_led_indicator_color_notify))', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:249-251; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:342-352')
e('AppearanceSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.foregroundNotifyStatusFilter(String)', 'CALL', 'Persist the foreground notification status filter',
  guard='preference.getKey().equals(getString(R.string.pref_key_foreground_notify_status_filter))', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:252-254; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:355-370')
e('AppearanceSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.foregroundNotifySorting(String)', 'CALL', 'Persist foreground notification sorting order',
  guard='preference.getKey().equals(getString(R.string.pref_key_foreground_notify_sorting))', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:255-257; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:373-388')
e('AppearanceSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.foregroundNotifyCombinedPauseButton(boolean)', 'CALL', 'Persist the combined foreground notification pause button setting',
  guard='preference.getKey().equals(getString(R.string.pref_key_foreground_notify_combined_pause_button))', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:258-260; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:391-398')
e('AppearanceSettingsFragment.onPreferenceChange', 'AppearanceSettingsFragment.lambda$onPreferenceChange$2', 'REGISTER', 'Register the theme restart action on the snackbar',
  guard='preference.getKey() == pref_key_theme', cls='non_standard', via='Material Snackbar action callback', evidence='INFERRED Material Snackbar action dispatch; SRC ui/settings/sections/AppearanceSettingsFragment.java:227-235,265-270')
e('AppearanceSettingsFragment.onPreferenceChange', 'AppearanceSettingsFragment.lambda$onPreferenceChange$2', 'FRAMEWORK', 'Dispatch a tap on the snackbar theme restart action',
  guard='preference.getKey() == pref_key_theme', cls='non_standard', via='Material Snackbar action callback', evidence='INFERRED Material Snackbar action dispatch; SRC ui/settings/sections/AppearanceSettingsFragment.java:227-235,265-270')
e('AppearanceSettingsFragment.lambda$onPreferenceChange$2', 'AppearanceSettingsFragment.restartMainActivity', 'CALL', 'Restart the main activity after the user selects Apply',
  cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:234-235,265-270')
e('AppearanceSettingsFragment.restartMainActivity', 'MainActivity.<init>', 'INTENT', 'Recreate the main screen for the selected theme',
  cls='standard', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:265-270; AndroidManifest.xml:43-59; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('AppearanceSettingsFragment.restartMainActivity', 'MainActivity.onCreate', 'INTENT', 'Create the restarted main screen',
  cls='standard', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:265-270; AndroidManifest.xml:43-59; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('AppearanceSettingsFragment.<init>', 'AppearanceSettingsFragment.lambda$new$1', 'REGISTER', 'Register the ringtone picker result callback',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult registration; SRC ui/settings/sections/AppearanceSettingsFragment.java:198-217')
e('AppearanceSettingsFragment.lambda$initLegacyNotifySettings$0', 'AppearanceSettingsFragment.lambda$new$1', 'RESULT', 'Deliver a ringtone picker result to the appearance settings page',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult dispatch; SRC ui/settings/sections/AppearanceSettingsFragment.java:144-167,198-217')
e('AppearanceSettingsFragment.lambda$new$1', 'SettingsRepositoryImpl.notifySound(String)', 'CALL', 'Persist the selected ringtone after a successful picker result',
  guard='result.getResultCode() == Activity.RESULT_OK && data != null && ringtone != null', cls='explicit', evidence='SRC ui/settings/sections/AppearanceSettingsFragment.java:200-216; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:270-275')
e('AppearanceSettingsFragment.initLegacyNotifySettings', 'AppearanceSettingsFragment.lambda$initLegacyNotifySettings$0', 'REGISTER', 'Register the ringtone picker launch callback when its preference exists',
  guard='notifySound != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/AppearanceSettingsFragment.java:137-167')
e('AppearanceSettingsFragment.initLegacyNotifySettings', 'AppearanceSettingsFragment.lambda$initLegacyNotifySettings$0', 'FRAMEWORK', 'Dispatch taps on the legacy notification sound preference',
  guard='notifySound != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/AppearanceSettingsFragment.java:137-167')
e('BehaviorSettingsFragment.<init>', 'BehaviorSettingsFragment.onCreate', 'LIFECYCLE', 'Create behavior settings after FragmentManager installs the page',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/BehaviorSettingsFragment.java:53-64')
e('BehaviorSettingsFragment.onCreate', 'BehaviorSettingsFragment.onCreatePreferences', 'LIFECYCLE', 'Load behavior preference definitions',
  cls='non_standard', via='AndroidX PreferenceFragmentCompat', evidence='INFERRED AndroidX PreferenceFragmentCompat callback dispatch; SRC ui/settings/sections/BehaviorSettingsFragment.java:63-64,188-192')
e('BehaviorSettingsFragment.onCreate', 'BehaviorSettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'Register listeners on behavior preferences that exist',
  guard='preference != null', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:63-158,193-195')
e('BehaviorSettingsFragment.bindOnPreferenceChangeListener', 'BehaviorSettingsFragment.onPreferenceChange', 'REGISTER', 'Register the behavior preference change listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/BehaviorSettingsFragment.java:193-195,198-244')
e('BehaviorSettingsFragment.bindOnPreferenceChangeListener', 'BehaviorSettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Dispatch behavior preference changes to the registered listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/BehaviorSettingsFragment.java:193-195,198-244')
e('BehaviorSettingsFragment.onCreate', 'RepositoryHelper.getSettingsRepository', 'CALL', 'Obtain the shared repository for behavior preferences',
  cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:63-70; core/RepositoryHelper.java:61-67')
e('BehaviorSettingsFragment.onCreate', 'BehaviorSettingsFragment.lambda$onCreate$0', 'REGISTER', 'Register the custom tracker text editor callback',
  guard='defaultTrackersList != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/BehaviorSettingsFragment.java:147-155')
e('BehaviorSettingsFragment.onCreate', 'BehaviorSettingsFragment.lambda$onCreate$0', 'FRAMEWORK', 'Bind the tracker text editor to the multiline listener',
  guard='defaultTrackersList != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/BehaviorSettingsFragment.java:147-155')
e('BehaviorSettingsFragment.onPreferenceChange', 'Utils.enableBootReceiver', 'CALL', 'Enable or disable boot startup for the autostart preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_autostart))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:199-204; core/utils/Utils.java:436-448')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.autostart(boolean)', 'CALL', 'Persist the autostart preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_autostart))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:201-204; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:415-425')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.onlyCharging(boolean)', 'CALL', 'Persist the only-while-charging preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_download_and_upload_only_when_charging))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:205-210; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:467-478')
e('BehaviorSettingsFragment.onPreferenceChange', 'BehaviorSettingsFragment.disableBatteryControl', 'CALL', 'Disable battery control when charging restriction is turned off',
  guard='preference.getKey().equals(getString(R.string.pref_key_download_and_upload_only_when_charging)) && !((SwitchPreferenceCompat)preference).isChecked()', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:205-210,267-275')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.batteryControl(boolean)', 'CALL', 'Persist the battery-control preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_battery_control))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:211-216; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:480-491')
e('BehaviorSettingsFragment.onPreferenceChange', 'BehaviorSettingsFragment.disableCustomBatteryControl', 'CALL', 'Disable custom battery control when built-in battery control is enabled',
  guard='preference.getKey().equals(getString(R.string.pref_key_battery_control)) && ((SwitchPreferenceCompat)preference).isChecked()', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:211-216,277-284')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.customBatteryControl(boolean)', 'CALL', 'Persist custom battery-control preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_custom_battery_control))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:217-222; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:493-504')
e('BehaviorSettingsFragment.onPreferenceChange', 'BehaviorSettingsFragment.showCustomBatteryDialog', 'CALL', 'Show custom battery threshold guidance when that setting is turned off',
  guard='preference.getKey().equals(getString(R.string.pref_key_custom_battery_control)) && !((SwitchPreferenceCompat)preference).isChecked()', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:217-222,247-265')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.unmeteredConnectionsOnly(boolean)', 'CALL', 'Persist the unmetered-connections preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_unmetered_connections_only))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:222-224; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:519-530')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.enableRoaming(boolean)', 'CALL', 'Persist roaming behavior',
  guard='preference.getKey().equals(getString(R.string.pref_key_enable_roaming))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:225-227; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:532-543')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.keepAlive(boolean)', 'CALL', 'Persist keep-alive preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_keep_alive))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:228-230; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:428-438')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.shutdownDownloadsComplete(boolean)', 'CALL', 'Persist stop-on-completion preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_shutdown_downloads_complete))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:231-233; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:441-451')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.cpuDoNotSleep(boolean)', 'CALL', 'Persist CPU sleep behavior',
  guard='preference.getKey().equals(getString(R.string.pref_key_cpu_do_not_sleep))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:234-236; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:454-464')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.customBatteryControlValue(int)', 'CALL', 'Persist the custom battery threshold',
  guard='preference.getKey().equals(getString(R.string.pref_key_custom_battery_control_value))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:237-239; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:506-517')
e('BehaviorSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.defaultTrackersList(String)', 'CALL', 'Persist the default tracker list',
  guard='preference.getKey().equals(getString(R.string.pref_key_default_trackers_list))', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:240-242; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:961-970')
e('BehaviorSettingsFragment.showCustomBatteryDialog', 'BaseAlertDialog.newInstance', 'CALL', 'Create custom battery-control guidance when no copy of the dialog is present',
  guard='isAdded() && fm.findFragmentByTag(TAG_CUSTOM_BATTERY_DIALOG) == null', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:247-264; ui/BaseAlertDialog.java:77-89')
e('BehaviorSettingsFragment.onCreate', 'BehaviorSettingsFragment.onStart', 'LIFECYCLE', 'Start behavior settings subscriptions after creation',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/settings/sections/BehaviorSettingsFragment.java:63-64,168-185')
e('BehaviorSettingsFragment.onStart', 'BehaviorSettingsFragment.onStop', 'LIFECYCLE', 'Clear behavior settings subscriptions when stopped',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/settings/sections/BehaviorSettingsFragment.java:160-173')
e('BehaviorSettingsFragment.onStart', 'BehaviorSettingsFragment.subscribeAlertDialog', 'CALL', 'Subscribe to custom battery dialog events while the page is started',
  cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:168-185')
e('BehaviorSettingsFragment.subscribeAlertDialog', 'BehaviorSettingsFragment.lambda$subscribeAlertDialog$1', 'REGISTER', 'Subscribe the custom battery dialog event handler',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava callback dispatch; SRC ui/settings/sections/BehaviorSettingsFragment.java:175-185')
e('BehaviorSettingsFragment.subscribeAlertDialog', 'BehaviorSettingsFragment.lambda$subscribeAlertDialog$1', 'FRAMEWORK', 'Deliver shared dialog events to the custom battery handler',
  cls='non_standard', via='RxJava Observable.subscribe', evidence='INFERRED RxJava callback dispatch; SRC ui/settings/sections/BehaviorSettingsFragment.java:175-185')
e('BehaviorSettingsFragment.lambda$subscribeAlertDialog$1', 'BehaviorSettingsFragment.disableCustomBatteryControl', 'CALL', 'Disable custom battery control when its warning dialog is canceled',
  guard='event.dialogTag != null && event.dialogTag.equals(TAG_CUSTOM_BATTERY_DIALOG) && event.type == NEGATIVE_BUTTON_CLICKED', cls='explicit', evidence='SRC ui/settings/sections/BehaviorSettingsFragment.java:177-183,277-284')
e('NetworkSettingsFragment.<init>', 'NetworkSettingsFragment.onAttach', 'LIFECYCLE', 'Attach network settings after FragmentManager installs the page',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:77-92')
e('NetworkSettingsFragment.onAttach', 'NetworkSettingsFragment.onCreate', 'LIFECYCLE', 'Create network settings after attachment',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:85-109')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.onCreatePreferences', 'LIFECYCLE', 'Load network preference definitions',
  cls='non_standard', via='AndroidX PreferenceFragmentCompat', evidence='INFERRED AndroidX PreferenceFragmentCompat callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:104-105,280-282')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'Register listeners on network preferences that exist',
  guard='preference != null', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:104-278,299-300')
e('NetworkSettingsFragment.bindOnPreferenceChangeListener', 'NetworkSettingsFragment.onPreferenceChange', 'REGISTER', 'Register the network preference change listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:299-300,304-306')
e('NetworkSettingsFragment.bindOnPreferenceChangeListener', 'NetworkSettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Dispatch network preference changes to the registered listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:299-300,304-306')
e('NetworkSettingsFragment.onCreate', 'RepositoryHelper.getSettingsRepository', 'CALL', 'Obtain shared settings for network preferences',
  cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:104-109; core/RepositoryHelper.java:61-67')
e('NetworkSettingsFragment.onCreate', 'SystemFacadeHelper.getFileSystemFacade', 'CALL', 'Create or retrieve the filesystem facade for filter-file display',
  cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:104-109; core/system/SystemFacadeHelper.java:39-46')
e('SystemFacadeHelper.getFileSystemFacade', 'FileSystemFacadeImpl.<init>', 'CALL', 'Construct the concrete filesystem facade on first access',
  guard='fileSystemFacade == null', cls='explicit', evidence='SRC core/system/SystemFacadeHelper.java:39-45; core/system/FileSystemFacadeImpl.java:52-58')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.lambda$onCreate$0', 'REGISTER', 'Register the start-port editor input filter',
  guard='portStart != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:157-167')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.lambda$onCreate$0', 'FRAMEWORK', 'Bind the start-port editor to its input filter',
  guard='portStart != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:157-167')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.lambda$onCreate$1', 'REGISTER', 'Register the end-port editor input filter',
  guard='portEnd != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:169-177')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.lambda$onCreate$1', 'FRAMEWORK', 'Bind the end-port editor to its input filter',
  guard='portEnd != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:169-177')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.lambda$onCreate$2', 'REGISTER', 'Register IP-filter file selection',
  guard='ipFilterFile != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:202-218')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.lambda$onCreate$2', 'FRAMEWORK', 'Dispatch a tap on the IP-filter file preference',
  guard='ipFilterFile != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:202-218')
e('NetworkSettingsFragment.lambda$onCreate$2', 'NetworkSettingsFragment.fileChooseDialog', 'CALL', 'Open the file picker for IP-filter selection',
  cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:213-217,284-297')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.lambda$onCreate$3', 'REGISTER', 'Register the proxy settings preference click handler',
  guard='proxy != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:227-240')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.lambda$onCreate$3', 'FRAMEWORK', 'Dispatch proxy settings preference clicks',
  guard='proxy != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:227-240')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.lambda$onCreate$4', 'REGISTER', 'Register the anonymous-mode preference click handler',
  guard='anonymousMode != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:242-262')
e('NetworkSettingsFragment.onCreate', 'NetworkSettingsFragment.lambda$onCreate$4', 'FRAMEWORK', 'Dispatch anonymous-mode preference clicks',
  guard='anonymousMode != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:242-262')
e('NetworkSettingsFragment.<init>', 'NetworkSettingsFragment.lambda$new$5', 'REGISTER', 'Register the IP-filter Activity Result callback',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult registration; SRC ui/settings/sections/NetworkSettingsFragment.java:381-403')
e('NetworkSettingsFragment.<init>', 'NetworkSettingsFragment.lambda$new$6', 'REGISTER', 'Register the anonymous-mode result callback',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult registration; SRC ui/settings/sections/NetworkSettingsFragment.java:405-413')
e('NetworkSettingsFragment.fileChooseDialog', 'FileManagerDialog.<init>', 'INTENT', 'Launch the file manager for an IP-filter file',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult launch; SRC ui/settings/sections/NetworkSettingsFragment.java:284-297; AndroidManifest.xml:137-138')
e('NetworkSettingsFragment.fileChooseDialog', 'FileManagerDialog.onCreate', 'INTENT', 'Create the IP-filter file picker activity',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult launch; SRC ui/settings/sections/NetworkSettingsFragment.java:284-297; AndroidManifest.xml:137-138')
e('NetworkSettingsFragment.fileChooseDialog', 'NetworkSettingsFragment.lambda$new$5', 'RESULT', 'Deliver the IP-filter file picker result',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:284-297,381-403')
e('NetworkSettingsFragment.lambda$new$5', 'SettingsRepositoryImpl.ipFilteringFile(String)', 'CALL', 'Save the selected IP-filter file URI',
  guard='result.getResultCode() == Activity.RESULT_OK && path != null', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:383-401; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:688-699')
e('NetworkSettingsFragment.lambda$new$5', 'FileSystemFacadeImpl.getFilePath', 'CALL', 'Resolve the selected IP-filter URI for its displayed summary',
  guard='result.getResultCode() == Activity.RESULT_OK && path != null && ipFilterFile != null', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:392-399; core/system/SystemFacadeHelper.java:39-45; core/system/FileSystemFacadeImpl.java:430-434')
e('NetworkSettingsFragment.lambda$onCreate$3', 'ProxySettingsFragment.newInstance', 'CALL', 'Create the proxy settings page for two-pane display',
  guard='Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:229-236; ui/settings/sections/ProxySettingsFragment.java:56-62')
e('NetworkSettingsFragment.lambda$onCreate$3', 'NetworkSettingsFragment.setFragment', 'CALL', 'Show proxy settings in the two-pane detail container',
  guard='Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:229-236,361-369')
e('NetworkSettingsFragment.lambda$onCreate$3', 'NetworkSettingsFragment.startActivity', 'CALL', 'Open proxy settings in the single-pane host',
  guard='!Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:229-236,371-379')
e('NetworkSettingsFragment.startActivity', 'PreferenceActivity.<init>', 'INTENT', 'Launch single-pane proxy or anonymous-mode settings host',
  cls='standard', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:371-379; AndroidManifest.xml:168-170; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('NetworkSettingsFragment.startActivity', 'PreferenceActivity.onCreate', 'INTENT', 'Create single-pane proxy or anonymous-mode settings host',
  cls='standard', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:371-379; AndroidManifest.xml:168-170; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('NetworkSettingsFragment.lambda$onCreate$4', 'AnonymousModeSettingsFragment.newInstance', 'CALL', 'Create anonymous-mode settings page for two-pane display',
  guard='Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:246-258; ui/settings/sections/AnonymousModeSettingsFragment.java:40-46')
e('NetworkSettingsFragment.lambda$onCreate$4', 'NetworkSettingsFragment.setFragment', 'CALL', 'Show anonymous-mode settings in the two-pane detail container',
  guard='Utils.isLargeScreenDevice(activity)', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:246-258,361-369')
e('NetworkSettingsFragment.lambda$onCreate$4', 'PreferenceActivity.<init>', 'RESULT', 'Launch anonymous-mode settings in the single-pane preference host',
  guard='!Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult launch; SRC ui/settings/sections/NetworkSettingsFragment.java:246-258; AndroidManifest.xml:168-170')
e('NetworkSettingsFragment.lambda$onCreate$4', 'PreferenceActivity.onCreate', 'RESULT', 'Create the anonymous-mode settings host for a result',
  guard='!Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult launch; SRC ui/settings/sections/NetworkSettingsFragment.java:246-258; AndroidManifest.xml:168-170')
e('NetworkSettingsFragment.lambda$onCreate$4', 'NetworkSettingsFragment.lambda$new$6', 'RESULT', 'Deliver completion of the anonymous-mode settings activity',
  guard='!Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:246-258,405-413')
e('NetworkSettingsFragment.lambda$new$6', 'SettingsRepositoryImpl.anonymousMode()', 'CALL', 'Read the updated anonymous-mode value after returning from settings',
  guard='anonymousMode != null', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:407-412; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:929-933')
e('PreferenceActivity.getFragment', 'ProxySettingsFragment.newInstance', 'CALL', 'Create the proxy settings page from its configured class name',
  guard='fragment.equals(ProxySettingsFragment.class.getSimpleName())', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:94-119')
e('PreferenceActivity.getFragment', 'AnonymousModeSettingsFragment.newInstance', 'CALL', 'Create the anonymous-mode page from its configured class name',
  guard='fragment.equals(AnonymousModeSettingsFragment.class.getSimpleName())', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:94-119')
e('ProxySettingsFragment.newInstance', 'ProxySettingsFragment.<init>', 'CALL', 'Instantiate the proxy settings fragment',
  cls='explicit', evidence='SRC ui/settings/sections/ProxySettingsFragment.java:56-62')
e('AnonymousModeSettingsFragment.newInstance', 'AnonymousModeSettingsFragment.<init>', 'CALL', 'Instantiate the anonymous-mode settings fragment',
  cls='explicit', evidence='SRC ui/settings/sections/AnonymousModeSettingsFragment.java:40-46')
e('NetworkSettingsFragment.setFragment', 'ProxySettingsFragment.onCreate', 'LIFECYCLE', 'Install the proxy page in the two-pane detail container',
  guard='Utils.isLargeScreenDevice(getActivity().getApplicationContext())', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:361-369; ui/settings/sections/ProxySettingsFragment.java:95-101')
e('NetworkSettingsFragment.setFragment', 'AnonymousModeSettingsFragment.onCreate', 'LIFECYCLE', 'Install the anonymous-mode page in the two-pane detail container',
  guard='Utils.isLargeScreenDevice(getActivity().getApplicationContext())', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:361-369; ui/settings/sections/AnonymousModeSettingsFragment.java:50-56')
e('PreferenceActivity.setFragment', 'ProxySettingsFragment.onCreate', 'LIFECYCLE', 'Install the proxy page in the single-pane preference host',
  guard='fragment != null', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/PreferenceActivity.java:85-92; ui/settings/sections/ProxySettingsFragment.java:95-101')
e('PreferenceActivity.setFragment', 'AnonymousModeSettingsFragment.onCreate', 'LIFECYCLE', 'Install the anonymous-mode page in the single-pane preference host',
  guard='fragment != null', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/PreferenceActivity.java:85-92; ui/settings/sections/AnonymousModeSettingsFragment.java:50-56')
e('NetworkSettingsFragment.onCreatePreferences', 'NetworkSettingsFragment.onViewCreated', 'LIFECYCLE', 'Initialize network page controls after preference view inflation',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/settings/sections/NetworkSettingsFragment.java:94-102,280-282')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.portRangeFirst(int)', 'CALL', 'Persist the first port bound or its default',
  guard='preference.getKey().equals(getString(R.string.pref_key_port_range_first))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:304-311; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:545-555')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.portRangeSecond(int)', 'CALL', 'Persist the second port bound or its default',
  guard='preference.getKey().equals(getString(R.string.pref_key_port_range_second))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:312-317; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:558-568')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.enableDht(boolean)', 'CALL', 'Persist DHT enablement',
  guard='preference.getKey().equals(getString(R.string.pref_key_enable_dht))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:319-321; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:571-581')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.enableLsd(boolean)', 'CALL', 'Persist local peer discovery enablement',
  guard='preference.getKey().equals(getString(R.string.pref_key_enable_lsd))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:322-324; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:584-594')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.enableUtp(boolean)', 'CALL', 'Persist uTP enablement',
  guard='preference.getKey().equals(getString(R.string.pref_key_enable_utp))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:325-327; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:597-607')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.enableUpnp(boolean)', 'CALL', 'Persist UPnP enablement',
  guard='preference.getKey().equals(getString(R.string.pref_key_enable_upnp))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:328-330; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:610-620')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.enableNatPmp(boolean)', 'CALL', 'Persist NAT-PMP enablement',
  guard='preference.getKey().equals(getString(R.string.pref_key_enable_natpmp))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:331-333; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:623-633')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.showNatErrors(boolean)', 'CALL', 'Persist NAT error display preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_show_nat_errors))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:334-336; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:701-711')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.useRandomPort(boolean)', 'CALL', 'Persist random-port selection',
  guard='preference.getKey().equals(getString(R.string.pref_key_use_random_port))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:337-339; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:636-646')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.encryptInConnectionsMode(int)', 'CALL', 'Persist inbound connection encryption mode',
  guard='preference.getKey().equals(getString(R.string.pref_key_enc_in_connections_mode))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:340-343; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:649-659')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.encryptOutConnectionsMode(int)', 'CALL', 'Persist outbound connection encryption mode',
  guard='preference.getKey().equals(getString(R.string.pref_key_enc_out_connections_mode))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:344-347; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:662-672')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.enableIpFiltering(boolean)', 'CALL', 'Persist IP-filtering enablement',
  guard='preference.getKey().equals(getString(R.string.pref_key_enable_ip_filtering))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:348-350; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:675-685')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.seedingOutgoingConnections(boolean)', 'CALL', 'Persist outgoing seeding connection behavior',
  guard='preference.getKey().equals(getString(R.string.pref_key_seeding_outgoing_connections))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:351-353; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:948-958')
e('NetworkSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.validateHttpsTrackers(boolean)', 'CALL', 'Persist HTTPS tracker validation preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_validate_https_trackers))', cls='explicit', evidence='SRC ui/settings/sections/NetworkSettingsFragment.java:354-356; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:974-984')
e('StorageSettingsFragment.<init>', 'StorageSettingsFragment.onCreate', 'LIFECYCLE', 'Create storage settings after FragmentManager installs the page',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:64-82')
e('StorageSettingsFragment.onCreate', 'StorageSettingsFragment.onCreatePreferences', 'LIFECYCLE', 'Load storage preference definitions',
  cls='non_standard', via='AndroidX PreferenceFragmentCompat', evidence='INFERRED AndroidX PreferenceFragmentCompat callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:81-82,217-220')
e('StorageSettingsFragment.onCreate', 'StorageSettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'Register listeners on storage preferences that exist',
  guard='preference != null', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:81-205,222-224')
e('StorageSettingsFragment.onCreate', 'RepositoryHelper.getSettingsRepository', 'CALL', 'Obtain the shared settings repository for storage preferences',
  cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:81-90; core/RepositoryHelper.java:61-67')
e('StorageSettingsFragment.onCreate', 'SystemFacadeHelper.getFileSystemFacade', 'CALL', 'Obtain the filesystem facade for directory summaries',
  cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:81-90; core/system/SystemFacadeHelper.java:39-46')
e('StorageSettingsFragment.onCreate', 'StorageSettingsFragment.lambda$onCreate$0', 'REGISTER', 'Register directory selection for the save-torrents location',
  guard='saveTorrentsIn != null && path != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:92-109')
e('StorageSettingsFragment.onCreate', 'StorageSettingsFragment.lambda$onCreate$0', 'FRAMEWORK', 'Dispatch clicks on the save-torrents directory preference',
  guard='saveTorrentsIn != null && path != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:92-109')
e('StorageSettingsFragment.lambda$onCreate$0', 'StorageSettingsFragment.dirChooseDialog', 'CALL', 'Open the folder chooser for the torrents location',
  cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:103-109,227-240')
e('StorageSettingsFragment.onCreate', 'StorageSettingsFragment.lambda$onCreate$1', 'REGISTER', 'Register directory selection for the move-after-download location',
  guard='moveAfterDownloadIn != null && path != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:119-137')
e('StorageSettingsFragment.onCreate', 'StorageSettingsFragment.lambda$onCreate$1', 'FRAMEWORK', 'Dispatch clicks on the move-after-download directory preference',
  guard='moveAfterDownloadIn != null && path != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:119-137')
e('StorageSettingsFragment.lambda$onCreate$1', 'StorageSettingsFragment.dirChooseDialog', 'CALL', 'Open the folder chooser for the move-after-download location',
  cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:130-136,227-240')
e('StorageSettingsFragment.onCreate', 'StorageSettingsFragment.lambda$onCreate$2', 'REGISTER', 'Register directory selection for the torrent-files location',
  guard='saveTorrentFilesIn != null && path != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:146-164')
e('StorageSettingsFragment.onCreate', 'StorageSettingsFragment.lambda$onCreate$2', 'FRAMEWORK', 'Dispatch clicks on the torrent-files directory preference',
  guard='saveTorrentFilesIn != null && path != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:146-164')
e('StorageSettingsFragment.lambda$onCreate$2', 'StorageSettingsFragment.dirChooseDialog', 'CALL', 'Open the folder chooser for the torrent-files location',
  cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:157-163,227-240')
e('StorageSettingsFragment.onCreate', 'StorageSettingsFragment.lambda$onCreate$3', 'REGISTER', 'Register directory selection for the watch-folder location',
  guard='dirToWatch != null && path != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:173-191')
e('StorageSettingsFragment.onCreate', 'StorageSettingsFragment.lambda$onCreate$3', 'FRAMEWORK', 'Dispatch clicks on the watch-folder directory preference',
  guard='dirToWatch != null && path != null', cls='non_standard', via='AndroidX Preference.OnPreferenceClickListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:173-191')
e('StorageSettingsFragment.lambda$onCreate$3', 'StorageSettingsFragment.dirChooseDialog', 'CALL', 'Open the folder chooser for the watch folder',
  cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:184-190,227-240')
e('StorageSettingsFragment.bindOnPreferenceChangeListener', 'StorageSettingsFragment.onPreferenceChange', 'REGISTER', 'Register the storage preference change listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:222-224,279-281')
e('StorageSettingsFragment.bindOnPreferenceChangeListener', 'StorageSettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Dispatch storage preference changes to the registered listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:222-224,279-281')
e('StorageSettingsFragment.onCreatePreferences', 'StorageSettingsFragment.onViewCreated', 'LIFECYCLE', 'Initialize storage page controls after preference view inflation',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/settings/sections/StorageSettingsFragment.java:73-79,217-220')
e('StorageSettingsFragment.<init>', 'StorageSettingsFragment.lambda$new$4', 'REGISTER', 'Register folder chooser result handling',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult registration; SRC ui/settings/sections/StorageSettingsFragment.java:241-276')
e('StorageSettingsFragment.dirChooseDialog', 'FileManagerDialog.<init>', 'INTENT', 'Launch the file manager in directory chooser mode',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult launch; SRC ui/settings/sections/StorageSettingsFragment.java:227-240; AndroidManifest.xml:137-138')
e('StorageSettingsFragment.dirChooseDialog', 'FileManagerDialog.onCreate', 'INTENT', 'Create the file manager for directory selection',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult launch; SRC ui/settings/sections/StorageSettingsFragment.java:227-240; AndroidManifest.xml:137-138')
e('FileManagerDialog.returnDirectoryUri', 'StorageSettingsFragment.lambda$new$4', 'RESULT', 'Return a selected directory to the storage settings page',
  guard='resultCode == RESULT_OK && launched with FileManagerConfig.DIR_CHOOSER_MODE', cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResult dispatch; SRC ui/filemanager/FileManagerDialog.java:498-510,557-568; ui/settings/sections/StorageSettingsFragment.java:241-276')
e('StorageSettingsFragment.lambda$new$4', 'SettingsRepositoryImpl.dirToWatch(String)', 'CALL', 'Save the selected watch-folder URI',
  guard='result.getResultCode() == Activity.RESULT_OK && path != null && p != null && dirChooserBindPref.equals(getString(R.string.pref_key_dir_to_watch))', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:243-268; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:792-802')
e('StorageSettingsFragment.lambda$new$4', 'SettingsRepositoryImpl.moveAfterDownloadIn(String)', 'CALL', 'Save the selected move-after-download directory',
  guard='result.getResultCode() == Activity.RESULT_OK && path != null && p != null && dirChooserBindPref.equals(getString(R.string.pref_key_move_after_download_in))', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:243-268; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:740-750')
e('StorageSettingsFragment.lambda$new$4', 'SettingsRepositoryImpl.saveTorrentFilesIn(String)', 'CALL', 'Save the selected torrent-files directory',
  guard='result.getResultCode() == Activity.RESULT_OK && path != null && p != null && dirChooserBindPref.equals(getString(R.string.pref_key_save_torrent_files_in))', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:243-268; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:766-776')
e('StorageSettingsFragment.lambda$new$4', 'SettingsRepositoryImpl.saveTorrentsIn(String)', 'CALL', 'Save the selected torrents directory',
  guard='result.getResultCode() == Activity.RESULT_OK && path != null && p != null && dirChooserBindPref.equals(getString(R.string.pref_key_save_torrents_in))', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:243-268; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:714-724')
e('StorageSettingsFragment.lambda$new$4', 'FileSystemFacadeImpl.getDirPath', 'CALL', 'Resolve the selected directory URI for its preference summary',
  guard='result.getResultCode() == Activity.RESULT_OK && path != null && p != null', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:270-274; core/system/SystemFacadeHelper.java:39-45; core/system/FileSystemFacadeImpl.java:418-422')
e('StorageSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.watchDir(boolean)', 'CALL', 'Persist watch-folder enablement',
  guard='preference.getKey().equals(getString(R.string.pref_key_watch_dir))', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:278-282; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:779-789')
e('StorageSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.moveAfterDownload(boolean)', 'CALL', 'Persist move-after-download behavior',
  guard='preference.getKey().equals(getString(R.string.pref_key_move_after_download))', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:282-284; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:727-737')
e('StorageSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.saveTorrentFiles(boolean)', 'CALL', 'Persist save-torrent-files behavior',
  guard='preference.getKey().equals(getString(R.string.pref_key_save_torrent_files))', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:284-286; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:753-763')
e('StorageSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.watchDirDeleteFile(boolean)', 'CALL', 'Persist whether processed watch-folder files should be deleted',
  guard='preference.getKey().equals(getString(R.string.pref_key_watch_dir_delete_file))', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:286-288; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:805-815')
e('StorageSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.posixDiskIo(boolean)', 'CALL', 'Persist POSIX disk I/O selection',
  guard='preference.getKey().equals(getString(R.string.pref_key_posix_disk_io))', cls='explicit', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:288-292; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:818-828')
e('LimitationsSettingsFragment.<init>', 'LimitationsSettingsFragment.onCreate', 'LIFECYCLE', 'Create limitations settings after FragmentManager installs the page',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:44-54')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.onCreatePreferences', 'LIFECYCLE', 'Load limitations preference definitions',
  cls='non_standard', via='AndroidX PreferenceFragmentCompat', evidence='INFERRED AndroidX PreferenceFragmentCompat callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:53-54,169-172')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'Register listeners on limitations preferences that exist',
  guard='preference != null', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:53-167,174-176')
e('LimitationsSettingsFragment.onCreate', 'RepositoryHelper.getSettingsRepository', 'CALL', 'Obtain shared settings for limitations preferences',
  cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:53-57; core/RepositoryHelper.java:61-67')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$0', 'REGISTER', 'Register the download speed editor filter',
  guard='maxDownloadSpeedLimit != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:72-81')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$0', 'FRAMEWORK', 'Bind the download speed editor input filter',
  guard='maxDownloadSpeedLimit != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:72-81')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$1', 'REGISTER', 'Register the upload speed editor filter',
  guard='maxUploadSpeedLimit != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:83-92')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$1', 'FRAMEWORK', 'Bind the upload speed editor input filter',
  guard='maxUploadSpeedLimit != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:83-92')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$2', 'REGISTER', 'Register the max connections editor filter',
  guard='maxConnections != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:94-103')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$2', 'FRAMEWORK', 'Bind the max connections editor input filter',
  guard='maxConnections != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:94-103')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$3', 'REGISTER', 'Register the max active uploads editor filter',
  guard='maxActiveUploads != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:112-121')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$3', 'FRAMEWORK', 'Bind the active uploads editor input filter',
  guard='maxActiveUploads != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:112-121')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$4', 'REGISTER', 'Register the max active downloads editor filter',
  guard='maxActiveDownloads != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:123-132')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$4', 'FRAMEWORK', 'Bind the active downloads editor input filter',
  guard='maxActiveDownloads != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:123-132')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$5', 'REGISTER', 'Register the max active torrents editor filter',
  guard='maxActiveTorrents != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:134-143')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$5', 'FRAMEWORK', 'Bind the active torrents editor input filter',
  guard='maxActiveTorrents != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:134-143')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$6', 'REGISTER', 'Register the per-torrent connections editor filter',
  guard='maxConnectionsPerTorrent != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:145-154')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$6', 'FRAMEWORK', 'Bind the per-torrent connections editor input filter',
  guard='maxConnectionsPerTorrent != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:145-154')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$7', 'REGISTER', 'Register the per-torrent uploads editor filter',
  guard='maxUploadsPerTorrent != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:156-165')
e('LimitationsSettingsFragment.onCreate', 'LimitationsSettingsFragment.lambda$onCreate$7', 'FRAMEWORK', 'Bind the per-torrent uploads editor input filter',
  guard='maxUploadsPerTorrent != null', cls='non_standard', via='AndroidX EditTextPreference.OnBindEditTextListener', evidence='INFERRED AndroidX EditTextPreference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:156-165')
e('LimitationsSettingsFragment.bindOnPreferenceChangeListener', 'LimitationsSettingsFragment.onPreferenceChange', 'REGISTER', 'Register the limitations preference change listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:174-176,180-183')
e('LimitationsSettingsFragment.bindOnPreferenceChangeListener', 'LimitationsSettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Dispatch limitations preference changes to the registered listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/LimitationsSettingsFragment.java:174-176,180-183')
e('LimitationsSettingsFragment.onPreferenceChange', 'LimitationsSettingsFragment.parseMaxConnectionValue', 'CALL', 'Parse max-connection preference values',
  guard='preference.getKey().equals(getString(R.string.pref_key_max_connections)) || preference.getKey().equals(getString(R.string.pref_key_max_connections_per_torrent))', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:180-190,247-255')
e('LimitationsSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.maxConnections(int)', 'CALL', 'Persist the total connection limit',
  guard='preference.getKey().equals(getString(R.string.pref_key_max_connections))', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:182-186; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:857-867')
e('LimitationsSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.maxConnectionsPerTorrent(int)', 'CALL', 'Persist the per-torrent connection limit',
  guard='preference.getKey().equals(getString(R.string.pref_key_max_connections_per_torrent))', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:187-190; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:870-880')
e('LimitationsSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.maxUploadSpeedLimit(int)', 'CALL', 'Persist the upload speed limit in bytes per second',
  guard='preference.getKey().equals(getString(R.string.pref_key_max_upload_speed))', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:192-200; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:844-854')
e('LimitationsSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.maxDownloadSpeedLimit(int)', 'CALL', 'Persist the download speed limit in bytes per second',
  guard='preference.getKey().equals(getString(R.string.pref_key_max_download_speed))', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:202-210; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:831-841')
e('LimitationsSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.maxActiveDownloads(int)', 'CALL', 'Persist the active download limit',
  guard='preference.getKey().equals(getString(R.string.pref_key_max_active_downloads))', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:212-218; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:909-919')
e('LimitationsSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.maxActiveUploads(int)', 'CALL', 'Persist the active upload limit',
  guard='preference.getKey().equals(getString(R.string.pref_key_max_active_uploads))', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:219-225; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:896-906')
e('LimitationsSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.maxActiveTorrents(int)', 'CALL', 'Persist the active torrent limit',
  guard='preference.getKey().equals(getString(R.string.pref_key_max_active_torrents))', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:226-232; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:922-932')
e('LimitationsSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.maxUploadsPerTorrent(int)', 'CALL', 'Persist the per-torrent upload limit',
  guard='preference.getKey().equals(getString(R.string.pref_key_max_uploads_per_torrent))', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:233-239; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:883-893')
e('LimitationsSettingsFragment.onPreferenceChange', 'SettingsRepositoryImpl.autoManage(boolean)', 'CALL', 'Persist automatic transfer management preference',
  guard='preference.getKey().equals(getString(R.string.pref_key_auto_manage))', cls='explicit', evidence='SRC ui/settings/sections/LimitationsSettingsFragment.java:240-242; core/RepositoryHelper.java:61-67; core/settings/SettingsRepositoryImpl.java:987-997')
e('SchedulingSettingsFragment.<init>', 'SchedulingSettingsFragment.onCreate', 'LIFECYCLE', 'Create scheduling settings after FragmentManager installs the page',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/SchedulingSettingsFragment.java:53-63')
e('SchedulingSettingsFragment.onCreate', 'SchedulingSettingsFragment.onCreatePreferences', 'LIFECYCLE', 'Load scheduling preference definitions',
  cls='non_standard', via='AndroidX PreferenceFragmentCompat', evidence='INFERRED AndroidX PreferenceFragmentCompat callback dispatch; SRC ui/settings/sections/SchedulingSettingsFragment.java:62-63,164-167')
e('SchedulingSettingsFragment.onCreate', 'SchedulingSettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'Register listeners on scheduling preferences that exist',
  guard='preference != null', cls='explicit', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:62-112,169-171')
e('SchedulingSettingsFragment.bindOnPreferenceChangeListener', 'SchedulingSettingsFragment.onPreferenceChange', 'REGISTER', 'Register the scheduling preference change listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/SchedulingSettingsFragment.java:169-171,191-195')
e('SchedulingSettingsFragment.bindOnPreferenceChangeListener', 'SchedulingSettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Dispatch scheduling preference changes to the registered listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/SchedulingSettingsFragment.java:169-171,191-195')
e('SchedulingSettingsFragment.onCreate', 'SchedulingSettingsFragment.onStart', 'LIFECYCLE', 'Start scheduling settings subscriptions after creation',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/settings/sections/SchedulingSettingsFragment.java:62-63,122-139')
e('SchedulingSettingsFragment.onStart', 'SchedulingSettingsFragment.onStop', 'LIFECYCLE', 'Clear scheduling settings subscriptions when stopped',
  cls='non_standard', via='AndroidX Fragment lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/settings/sections/SchedulingSettingsFragment.java:114-127')
e('FeedSettingsFragment.<init>', 'FeedSettingsFragment.onCreate', 'LIFECYCLE', 'Create feed settings after FragmentManager installs the page',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/FeedSettingsFragment.java:42-52')
e('FeedSettingsFragment.onCreate', 'FeedSettingsFragment.onCreatePreferences', 'LIFECYCLE', 'Load feed preference definitions',
  cls='non_standard', via='AndroidX PreferenceFragmentCompat', evidence='INFERRED AndroidX PreferenceFragmentCompat callback dispatch; SRC ui/settings/sections/FeedSettingsFragment.java:51-52,114-117')
e('FeedSettingsFragment.onCreate', 'FeedSettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'Register listeners on feed preferences that exist',
  guard='preference != null', cls='explicit', evidence='SRC ui/settings/sections/FeedSettingsFragment.java:51-112,119-121')
e('FeedSettingsFragment.bindOnPreferenceChangeListener', 'FeedSettingsFragment.onPreferenceChange', 'REGISTER', 'Register the feed preference change listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/FeedSettingsFragment.java:119-121,125-128')
e('FeedSettingsFragment.bindOnPreferenceChangeListener', 'FeedSettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Dispatch feed preference changes to the registered listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/FeedSettingsFragment.java:119-121,125-128')
e('StreamingSettingsFragment.<init>', 'StreamingSettingsFragment.onCreate', 'LIFECYCLE', 'Create streaming settings after FragmentManager installs the page',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/StreamingSettingsFragment.java:43-53')
e('StreamingSettingsFragment.onCreate', 'StreamingSettingsFragment.onCreatePreferences', 'LIFECYCLE', 'Load streaming preference definitions',
  cls='non_standard', via='AndroidX PreferenceFragmentCompat', evidence='INFERRED AndroidX PreferenceFragmentCompat callback dispatch; SRC ui/settings/sections/StreamingSettingsFragment.java:52-53,88-91')
e('StreamingSettingsFragment.onCreate', 'StreamingSettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'Register listeners on streaming preferences that exist',
  guard='preference != null', cls='explicit', evidence='SRC ui/settings/sections/StreamingSettingsFragment.java:52-86,93-95')
e('StreamingSettingsFragment.bindOnPreferenceChangeListener', 'StreamingSettingsFragment.onPreferenceChange', 'REGISTER', 'Register the streaming preference change listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StreamingSettingsFragment.java:93-95,99-102')
e('StreamingSettingsFragment.bindOnPreferenceChangeListener', 'StreamingSettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Dispatch streaming preference changes to the registered listener',
  cls='non_standard', via='AndroidX Preference.OnPreferenceChangeListener', evidence='INFERRED AndroidX Preference callback dispatch; SRC ui/settings/sections/StreamingSettingsFragment.java:93-95,99-102')
e('SettingsFragment.setFragment', 'AppearanceSettingsFragment.onCreate', 'LIFECYCLE', 'Install the appearance page through the two-pane fragment transaction',
  guard='Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/SettingsFragment.java:220-230; ui/settings/sections/AppearanceSettingsFragment.java:74-75')
e('SettingsFragment.setFragment', 'BehaviorSettingsFragment.onCreate', 'LIFECYCLE', 'Install the behavior page through the two-pane fragment transaction',
  guard='Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/SettingsFragment.java:220-230; ui/settings/sections/BehaviorSettingsFragment.java:63-64')
e('SettingsFragment.setFragment', 'NetworkSettingsFragment.onCreate', 'LIFECYCLE', 'Install the network page through the two-pane fragment transaction',
  guard='Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/SettingsFragment.java:220-230; ui/settings/sections/NetworkSettingsFragment.java:104-109')
e('SettingsFragment.setFragment', 'StorageSettingsFragment.onCreate', 'LIFECYCLE', 'Install the storage page through the two-pane fragment transaction',
  guard='Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/SettingsFragment.java:220-230; ui/settings/sections/StorageSettingsFragment.java:81-82')
e('SettingsFragment.setFragment', 'LimitationsSettingsFragment.onCreate', 'LIFECYCLE', 'Install the limitations page through the two-pane fragment transaction',
  guard='Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/SettingsFragment.java:220-230; ui/settings/sections/LimitationsSettingsFragment.java:53-54')
e('SettingsFragment.setFragment', 'SchedulingSettingsFragment.onCreate', 'LIFECYCLE', 'Install the scheduling page through the two-pane fragment transaction',
  guard='Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/SettingsFragment.java:220-230; ui/settings/sections/SchedulingSettingsFragment.java:62-63')
e('SettingsFragment.setFragment', 'FeedSettingsFragment.onCreate', 'LIFECYCLE', 'Install the feed page through the two-pane fragment transaction',
  guard='Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/SettingsFragment.java:220-230; ui/settings/sections/FeedSettingsFragment.java:51-52')
e('SettingsFragment.setFragment', 'StreamingSettingsFragment.onCreate', 'LIFECYCLE', 'Install the streaming page through the two-pane fragment transaction',
  guard='Utils.isLargeScreenDevice(activity)', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/SettingsFragment.java:220-230; ui/settings/sections/StreamingSettingsFragment.java:52-53')
e('PreferenceActivity.setFragment', 'AppearanceSettingsFragment.onCreate', 'LIFECYCLE', 'Install the appearance page through the single-pane fragment transaction',
  guard='fragment != null', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/PreferenceActivity.java:85-92; ui/settings/sections/AppearanceSettingsFragment.java:74-75')
e('PreferenceActivity.setFragment', 'BehaviorSettingsFragment.onCreate', 'LIFECYCLE', 'Install the behavior page through the single-pane fragment transaction',
  guard='fragment != null', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/PreferenceActivity.java:85-92; ui/settings/sections/BehaviorSettingsFragment.java:63-64')
e('PreferenceActivity.setFragment', 'NetworkSettingsFragment.onCreate', 'LIFECYCLE', 'Install the network page through the single-pane fragment transaction',
  guard='fragment != null', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/PreferenceActivity.java:85-92; ui/settings/sections/NetworkSettingsFragment.java:104-109')
e('PreferenceActivity.setFragment', 'StorageSettingsFragment.onCreate', 'LIFECYCLE', 'Install the storage page through the single-pane fragment transaction',
  guard='fragment != null', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/PreferenceActivity.java:85-92; ui/settings/sections/StorageSettingsFragment.java:81-82')
e('PreferenceActivity.setFragment', 'LimitationsSettingsFragment.onCreate', 'LIFECYCLE', 'Install the limitations page through the single-pane fragment transaction',
  guard='fragment != null', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/PreferenceActivity.java:85-92; ui/settings/sections/LimitationsSettingsFragment.java:53-54')
e('PreferenceActivity.setFragment', 'SchedulingSettingsFragment.onCreate', 'LIFECYCLE', 'Install the scheduling page through the single-pane fragment transaction',
  guard='fragment != null', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/PreferenceActivity.java:85-92; ui/settings/sections/SchedulingSettingsFragment.java:62-63')
e('PreferenceActivity.setFragment', 'FeedSettingsFragment.onCreate', 'LIFECYCLE', 'Install the feed page through the single-pane fragment transaction',
  guard='fragment != null', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/PreferenceActivity.java:85-92; ui/settings/sections/FeedSettingsFragment.java:51-52')
e('PreferenceActivity.setFragment', 'StreamingSettingsFragment.onCreate', 'LIFECYCLE', 'Install the streaming page through the single-pane fragment transaction',
  guard='fragment != null', cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/PreferenceActivity.java:85-92; ui/settings/sections/StreamingSettingsFragment.java:52-53')
e('FeedActivity.onCreate', 'FeedActivity.initLayout', 'CALL', 'Initialize feed toolbar and two-pane placeholder',
  cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:75-101')
e('FeedActivity.initLayout', 'FeedFragment.<init>', 'FRAMEWORK', 'Inflate feed list fragment from activity layout',
  cls='non_standard', via='AndroidX FragmentContainerView', evidence='INFERRED AndroidX FragmentContainerView dispatch; SRC ui/feeds/FeedActivity.java:89-101; res/layout/activity_feed_portrait.xml:8-14; res/layout/activity_feed_two_pane.xml:19-25')
e('FeedActivity.onCreate', 'FeedActivity.onStart', 'LIFECYCLE', 'Start feed activity after screen setup',
  cls='standard', evidence='SRC ui/feeds/FeedActivity.java:75-101,119-132; FW-SRC core/java/android/app/ActivityThread.java:2738-2745; core/java/android/app/Instrumentation.java:1333-1335')
e('FeedActivity.onStart', 'FeedActivity.subscribeAlertDialog', 'CALL', 'Subscribe to feed activity error report events',
  cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:119-132,138-166')
e('FeedActivity.onStart', 'FeedActivity.subscribeMsgViewModel', 'CALL', 'Subscribe to feed item open/close and deletion messages',
  cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:119-132,169-189')
e('FeedActivity.subscribeMsgViewModel', 'FeedActivity.showFeedItems', 'REGISTER', 'Open feed items when a feed row selection message arrives',
  cls='non_standard', via='RxJava observeOn/subscribe method reference', evidence='INFERRED RxJava callback dispatch; SRC ui/feeds/FeedActivity.java:172-178,203-227')
e('FeedActivity.showFeedItems', 'FeedItemsFragment.newInstance', 'CALL', 'Show selected feed items in two-pane layout',
  guard='Utils.isTwoPane(this)', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:203-227')
e('FeedActivity.showFeedItems', 'FeedItemsActivity.<init>', 'INTENT', 'Open feed items in single-pane layout',
  guard='!Utils.isTwoPane(this)', cls='standard', evidence='SRC ui/feeds/FeedActivity.java:203-227; AndroidManifest.xml:185-187; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('FeedActivity.subscribeMsgViewModel', 'FeedActivity.lambda$subscribeMsgViewModel$2', 'REGISTER', 'Clear two-pane feed items when close event arrives',
  cls='non_standard', via='RxJava observeOn/subscribe', evidence='INFERRED RxJava callback dispatch; SRC ui/feeds/FeedActivity.java:179-181')
e('FeedActivity.lambda$subscribeMsgViewModel$2', 'FeedActivity.showBlankFragment', 'CALL', 'Clear feed detail after close notification',
  cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:179-181,191-201')
e('FeedFragment.<init>', 'FeedFragment.onAttach', 'LIFECYCLE', 'Attach feed list fragment to activity',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/feeds/FeedFragment.java:194-201')
e('FeedFragment.onAttach', 'FeedFragment.onCreateView', 'LIFECYCLE', 'Inflate feed list view',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/feeds/FeedFragment.java:88-102')
e('FeedFragment.onCreateView', 'FeedFragment.onViewCreated', 'LIFECYCLE', 'Initialize feed adapter, selection tracker, and buttons',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/feeds/FeedFragment.java:104-192')
e('FeedFragment.onViewCreated', 'FeedFragment.onStart', 'LIFECYCLE', 'Start feed list subscriptions',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/feeds/FeedFragment.java:104-212')
e('FeedFragment.onStart', 'FeedFragment.subscribeAdapter', 'CALL', 'Subscribe to feed list data',
  cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:203-212,250-284')
e('FeedFragment.onStart', 'FeedFragment.subscribeAlertDialog', 'CALL', 'Subscribe to feed deletion dialog events',
  cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:203-212,310-331')
e('FeedFragment.onStart', 'FeedFragment.subscribeMsgViewModel', 'CALL', 'Subscribe to feed item close/deletion messages',
  cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:203-212,286-308')
e('FeedFragment.onStart', 'FeedFragment.subscribeRefreshStatus', 'CALL', 'Subscribe to feed refresh loading state',
  cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:203-212,333-338')
e('FeedFragment.onViewCreated', 'FeedFragment.lambda$onViewCreated$1', 'REGISTER', 'Register add-feed channel button',
  cls='standard', evidence='SRC ui/feeds/FeedFragment.java:185-188; FW-SRC core/java/android/view/View.java:6143-6158,6289-6310')
e('FeedFragment.lambda$onViewCreated$1', 'AddFeedActivity.<init>', 'INTENT', 'Open exported add-feed activity from feed list',
  cls='standard', evidence='SRC ui/feeds/FeedFragment.java:187-188; AndroidManifest.xml:178-228; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('FeedFragment.onItemClicked', 'MsgFeedViewModel.feedItemsOpened', 'CALL', 'Publish selected feed channel for detail display',
  cls='explicit', evidence='SRC ui/feeds/FeedFragment.java:340-346')
e('FeedFragment.editChannel', 'AddFeedActivity.<init>', 'INTENT', 'Open add-feed activity with selected channel ID for editing',
  cls='standard', evidence='SRC ui/feeds/FeedFragment.java:494-507; AndroidManifest.xml:178-228; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('FeedActivity.showFeedItems', 'FeedItemsActivity.onCreate', 'INTENT', 'Create single-pane feed items screen',
  guard='!Utils.isTwoPane(this)', cls='standard', evidence='SRC ui/feeds/FeedActivity.java:203-227; AndroidManifest.xml:185-187; FW-SRC core/java/android/app/ActivityThread.java:2727-2732; core/java/android/app/Instrumentation.java:1212-1215')
e('FeedItemsActivity.onCreate', 'FeedItemsFragment.<init>', 'FRAMEWORK', 'Inflate feed items fragment from activity layout',
  guard='!Utils.isTwoPane(this)', cls='non_standard', via='AndroidX FragmentContainerView', evidence='INFERRED AndroidX FragmentContainerView dispatch; SRC ui/feeditems/FeedItemsActivity.java:39-63; res/layout/activity_feed_items.xml:1-10')
e('FeedItemsActivity.onCreate', 'FeedItemsFragment.setFeedId', 'CALL', 'Pass selected feed ID into loaded fragment',
  guard='feedItemsFragment != null', cls='explicit', evidence='SRC ui/feeditems/FeedItemsActivity.java:54-63; ui/feeditems/FeedItemsFragment.java:94-97')
e('FeedItemsFragment.newInstance', 'FeedItemsFragment.<init>', 'CALL', 'Instantiate feed items detail fragment in two-pane mode',
  cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:80-87')
e('FeedItemsFragment.onAttach', 'FeedItemsFragment.onCreateView', 'LIFECYCLE', 'Attach and inflate feed items fragment',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/feeditems/FeedItemsFragment.java:99-114')
e('FeedItemsFragment.onCreateView', 'FeedItemsFragment.onViewCreated', 'LIFECYCLE', 'Initialize feed items list and toolbar callbacks',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/feeditems/FeedItemsFragment.java:116-156')
e('FeedItemsFragment.onViewCreated', 'FeedItemsFragment.onStart', 'LIFECYCLE', 'Start feed items observers',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/feeditems/FeedItemsFragment.java:158-165')
e('FeedItemsFragment.onViewCreated', 'FeedItemsViewModel.setFeedId', 'CALL', 'Load items for selected feed channel',
  cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:123-128; ui/feeditems/FeedItemsViewModel.java:77-86')
e('FeedItemsFragment.onStart', 'FeedItemsFragment.subscribeAdapter', 'CALL', 'Subscribe to feed items and populate list',
  cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:158-165,202-221')
e('FeedItemsFragment.onStart', 'FeedItemsFragment.subscribeRefreshStatus', 'CALL', 'Observe feed refresh state',
  cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:158-165,238-243')
e('FeedItemsFragment.onItemClicked', 'FeedItemsFragment.openDownloadUrl', 'CALL', 'Open torrent download link from selected feed item',
  cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:245-249,280-295')
e('FeedItemsFragment.openDownloadUrl', 'AddTorrentActivity.<init>', 'INTENT', 'Open add-torrent screen for feed download URL',
  guard='!TextUtils.isEmpty(item.downloadUrl)', cls='standard', evidence='SRC ui/feeditems/FeedItemsFragment.java:280-295; AndroidManifest.xml:62-92; FW-SRC core/java/android/app/ActivityThread.java:2665-2671; core/java/android/app/Instrumentation.java:1170-1175')
e('FeedItemsFragment.onItemMenuClicked', 'FeedItemsFragment.openArticle', 'CALL', 'Open feed article from item menu',
  guard='menuId == R.id.open_article_menu', cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:251-261,263-278')

e('FeedActivity.onStart', 'FeedActivity.onCreateOptionsMenu', 'FRAMEWORK', 'Prepare feed toolbar menu through the AppCompat action bar',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu callback dispatch; SRC ui/feeds/FeedActivity.java:115,122,239-242')
e('FeedActivity.onCreateOptionsMenu', 'FeedActivity.onOptionsItemSelected', 'REGISTER', 'Register feed toolbar menu item selection callback',
  cls='non_standard', via='AndroidX AppCompat Toolbar', evidence='INFERRED AppCompat Toolbar menu callback dispatch; SRC ui/feeds/FeedActivity.java:241-242')
e('FeedActivity.onCreateOptionsMenu', 'FeedActivity.onOptionsItemSelected', 'FRAMEWORK', 'Dispatch selected feed toolbar menu actions through AppCompat',
  cls='non_standard', via='AndroidX AppCompat action bar', evidence='INFERRED AppCompat menu callback dispatch; SRC ui/feeds/FeedActivity.java:241-242,248-252')
e('FeedActivity.onOptionsItemSelected', 'FeedViewModel.refreshAllFeeds', 'CALL', 'Refresh all feed channels from the toolbar refresh item',
  guard='itemId == R.id.refresh_feed_channel_menu', cls='explicit', evidence='SRC ui/feeds/FeedActivity.java:251-252; ui/feeds/FeedViewModel.java:118-127')
e('FeedViewModel.refreshAllFeeds', 'FeedViewModel.runFetchWorker', 'CALL', 'Enqueue all-channel fetch work',
  cls='explicit', evidence='SRC ui/feeds/FeedViewModel.java:118-127,153-157')
e('FeedViewModel.runFetchWorker', 'FeedFetcherWorker.doWork', 'FRAMEWORK', 'Run enqueued feed fetch work through WorkManager',
  cls='non_standard', via='AndroidX WorkManager OneTimeWorkRequest', evidence='INFERRED WorkManager worker dispatch; SRC ui/feeds/FeedViewModel.java:157; service/FeedFetcherWorker.java:51,74')
e('FeedFetcherWorker.doWork', 'FeedFetcherWorker.fetchChannels', 'CALL', 'Fetch every saved feed channel for the all-channels action',
  guard='action == ACTION_FETCH_ALL_CHANNELS', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:92-101')
e('FeedFetcherWorker.fetchChannels', 'FeedFetcherWorker.fetchChannel', 'CALL', 'Fetch one saved feed channel',
  guard='channel != null', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:124-135')
e('FeedFetcherWorker.fetchChannel', 'FeedParser.<init>', 'CALL', 'Download and parse the saved feed URL',
  guard='channel != null', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:150-156; core/FeedParser.java:62-71')
e('FeedFetcherWorker.fetchChannel', 'FeedParser.getItems', 'CALL', 'Read parsed feed items for filtering and storage',
  cls='explicit', evidence='SRC service/FeedFetcherWorker.java:165')
e('FeedFetcherWorker.fetchChannel', 'FeedParser.getTitle', 'CALL', 'Read feed title when the saved channel has no name',
  guard='TextUtils.isEmpty(channel.name)', cls='explicit', evidence='SRC service/FeedFetcherWorker.java:175-176')
e('FeedParser.<init>', 'FeedParserFactory.newParser', 'CALL', 'Create the feed parser implementation',
  guard='response != null', cls='explicit', evidence='SRC core/FeedParser.java:67-71')
e('FeedParserFactory.newParser', 'DefaultFeedParser.<init>', 'CALL', 'Instantiate the default SAX feed parser',
  cls='explicit', evidence='SRC com/ernieyu/feedparser/FeedParserFactory.java:25')
e('FeedParser.<init>', 'DefaultFeedParser.parse', 'CALL', 'Parse downloaded feed bytes through the parser interface',
  guard='response != null', cls='non_standard', via='FeedParser interface dispatch to DefaultFeedParser', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:71; com/ernieyu/feedparser/FeedParserFactory.java:25')
e('DefaultFeedParser.parse', 'XMLInputStream.<init>', 'CALL', 'Wrap the feed stream in the XML cleaning stream',
  cls='explicit', evidence='SRC impl/DefaultFeedParser.java:37')
e('DefaultFeedParser.parse', 'FeedHandler.<init>', 'CALL', 'Create the SAX feed handler',
  cls='explicit', evidence='SRC impl/DefaultFeedParser.java:34')
e('DefaultFeedParser.parse', 'FeedHandler.startElement', 'FRAMEWORK', 'SAX parser sends start-element events to the feed handler',
  cls='non_standard', via='JDK SAX DefaultHandler callback', evidence='INFERRED SAX DefaultHandler callback dispatch; SRC impl/DefaultFeedParser.java:37; impl/FeedHandler.java:54-107')
e('DefaultFeedParser.parse', 'FeedHandler.endElement', 'FRAMEWORK', 'SAX parser sends end-element events to the feed handler',
  cls='non_standard', via='JDK SAX DefaultHandler callback', evidence='INFERRED SAX DefaultHandler callback dispatch; SRC impl/DefaultFeedParser.java:37; impl/FeedHandler.java:110-131')
e('DefaultFeedParser.parse', 'FeedHandler.getFeed', 'CALL', 'Read the feed built by the SAX handler',
  cls='explicit', evidence='SRC impl/DefaultFeedParser.java:38')
e('DefaultFeedParser.parse', 'FeedException.<init>(String)', 'CALL', 'Reject input that produced no feed',
  guard='handler.getFeed() == null', cls='explicit', evidence='SRC impl/DefaultFeedParser.java:38-40')
e('DefaultFeedParser.parse', 'FeedException.<init>(Throwable)', 'CALL', 'Wrap any SAX or stream failure',
  guard='parse throws an exception', cls='explicit', evidence='SRC impl/DefaultFeedParser.java:44-45')
e('DefaultFeedParser.parse', 'XMLInputStream.read(byte[],int,int)', 'FRAMEWORK', 'SAX parser reads feed bytes through the XML cleaning stream',
  cls='non_standard', via='JDK SAX parser input stream read', evidence='INFERRED SAX parser input stream read; SRC impl/DefaultFeedParser.java:37; XMLInputStream.java:134-144')
e('DefaultFeedParser.parse', 'XMLInputStream.read()', 'FRAMEWORK', 'SAX parser reads the first bytes one at a time for encoding detection',
  cls='non_standard', via='JDK SAX parser input stream read', evidence='INFERRED SAX parser encoding detection reads single bytes; SRC impl/DefaultFeedParser.java:37; XMLInputStream.java:127-132')
e('XMLInputStream.read()', 'XMLInputStream.read(int)', 'CALL', 'Read one cleaned character',
  cls='explicit', evidence='SRC XMLInputStream.java:129')
e('XMLInputStream.read()', 'XMLInputStream.given', 'CALL', 'Record the character handed to the parser',
  cls='explicit', evidence='SRC XMLInputStream.java:130')
e('XMLInputStream.read(byte[],int,int)', 'XMLInputStream.read(int)', 'CALL', 'Read a block of cleaned characters',
  cls='explicit', evidence='SRC XMLInputStream.java:137')
e('XMLInputStream.read(byte[],int,int)', 'XMLInputStream.given', 'CALL', 'Record the block handed to the parser',
  cls='explicit', evidence='SRC XMLInputStream.java:142')
e('XMLInputStream.read(int)', 'XMLInputStream.readIntoPushBack', 'CALL', 'Refill the pushback buffer from the wrapped stream',
  guard='pushBack is empty', cls='explicit', evidence='SRC XMLInputStream.java:49-51')
e('XMLInputStream.readIntoPushBack', 'XMLInputStream.isWhiteSpace', 'CALL', 'Drop whitespace before the first character',
  guard='pulled == 0 and ch >= 0', cls='explicit', evidence='SRC XMLInputStream.java:73-75')
e('XMLInputStream.readIntoPushBack', 'XMLInputStream.readAmpersand', 'CALL', 'Translate an ampersand reference',
  guard="ch == '&'", cls='explicit', evidence='SRC XMLInputStream.java:79-81')
e('XMLInputStream.readAmpersand', 'XMLInputStream.isAlphaNumeric', 'CALL', 'Collect the characters of an entity name',
  cls='explicit', evidence='SRC XMLInputStream.java:100')
e('XMLInputStream.readAmpersand', 'XML.hash', 'CALL', 'Look up a named character reference',
  guard="reference ends with ';'", cls='explicit', evidence='SRC XMLInputStream.java:104-106')
e('XMLInputStream.readAmpersand', 'XML.<clinit>', 'FRAMEWORK', 'Initialize the named-entity table before the first lookup',
  cls='non_standard', via='JVM class initialization before first static call', evidence='INFERRED JVM class initialization; SRC com/ernieyu/feedparser/XML.java:9,19; XMLInputStream.java:106')
e('FeedHandler.startElement', 'FeedType.<clinit>', 'FRAMEWORK', 'Initialize feed type constants before the first type assignment',
  cls='non_standard', via='JVM class initialization before first enum access', evidence='INFERRED JVM class initialization; SRC impl/FeedHandler.java:64,71,78; FeedType.java:6-8')
e('FeedHandler.startElement', 'AtomFeed.<init>', 'CALL', 'Create the Atom feed for a feed root element',
  guard='localName equals feed', cls='explicit', evidence='SRC impl/FeedHandler.java:74-78')
e('FeedHandler.startElement', 'Rss1Item.<init>', 'CALL', 'Create an RSS 1.0 item',
  guard='feed type is RSS 1.0 and localName equals item', cls='explicit', evidence='SRC impl/FeedHandler.java:81-85')
e('FeedHandler.startElement', 'Rss2Item.<init>', 'CALL', 'Create an RSS 2.0 item',
  guard='feed type is RSS 2.0 and localName equals item', cls='explicit', evidence='SRC impl/FeedHandler.java:81-88')
e('FeedHandler.startElement', 'AtomItem.<init>', 'CALL', 'Create an Atom entry',
  guard='localName equals entry', cls='explicit', evidence='SRC impl/FeedHandler.java:94-96')
e('FeedParser.getItems', 'AtomFeed.getItemList', 'CALL', 'Read entries from an Atom feed',
  guard='feed is an Atom feed', cls='non_standard', via='Feed interface dispatch to AtomFeed', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:95; impl/AtomFeed.java:94-106')
e('FeedParser.getItems', 'Rss2Feed.getItemList', 'CALL', 'Read items from an RSS 2.0 feed',
  guard='feed is an RSS 2.0 feed', cls='non_standard', via='Feed interface dispatch to Rss2Feed', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:95; impl/Rss2Feed.java:113')
e('FeedParser.getItems', 'Rss1Feed.getItemList', 'CALL', 'Read items from an RSS 1.0 feed',
  guard='feed is an RSS 1.0 feed', cls='non_standard', via='Feed interface dispatch to Rss1Feed', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:95; impl/Rss1Feed.java:103')
e('FeedParser.getTitle', 'AtomFeed.getTitle', 'CALL', 'Read the Atom feed title',
  guard='feed is an Atom feed', cls='non_standard', via='Feed interface dispatch to AtomFeed', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:86; impl/AtomFeed.java:44-46')
e('FeedParser.getTitle', 'Rss2Feed.getTitle', 'CALL', 'Read the RSS 2.0 feed title',
  guard='feed is an RSS 2.0 feed', cls='non_standard', via='Feed interface dispatch to Rss2Feed', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:86; impl/Rss2Feed.java:47')
e('FeedParser.getTitle', 'Rss1Feed.getTitle', 'CALL', 'Read the RSS 1.0 feed title',
  guard='feed is an RSS 1.0 feed', cls='non_standard', via='Feed interface dispatch to Rss1Feed', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:86; impl/Rss1Feed.java:46')
e('FeedParser.getItems', 'FeedParser.findDownloadUrl', 'CALL', 'Find the download URL when no link is a magnet or torrent',
  guard='downloadUrl == null', cls='explicit', evidence='SRC core/FeedParser.java:101-102')
e('FeedParser.findDownloadUrl', 'FeedParser.watchEnclosure', 'CALL', 'Check enclosure tags first',
  cls='explicit', evidence='SRC core/FeedParser.java:147-148')
e('FeedParser.findDownloadUrl', 'FeedParser.watchTorrentInfoHash', 'CALL', 'Check EzRSS info hash after enclosures',
  guard='watchEnclosure returned null', cls='explicit', evidence='SRC core/FeedParser.java:151-152')
e('FeedParser.watchEnclosure', 'AtomItem.getEnclosures', 'CALL', 'Read Atom enclosure links',
  cls='non_standard', via='Item interface dispatch to AtomItem', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:168-170; impl/AtomItem.java:99-119')
e('FeedParser.watchEnclosure', 'Rss2Item.getEnclosures', 'CALL', 'Read RSS 2.0 enclosure links',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:168-170; impl/Rss2Item.java:94-110')
e('FeedParser.watchEnclosure', 'Rss1Item.getEnclosures', 'CALL', 'Read RSS 1.0 enclosure links',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:168-170; impl/Rss1Item.java:88-104')
e('AtomItem.getEnclosures', 'Enclosure.<init>', 'CALL', 'Create an enclosure for each rel=enclosure link',
  guard='rel equals enclosure', cls='explicit', evidence='SRC impl/AtomItem.java:105-116')
e('FeedParser.watchEnclosure', 'Enclosure.getUrl', 'CALL', 'Read enclosure URL',
  guard='enclosure != null', cls='explicit', evidence='SRC core/FeedParser.java:172-174')
e('FeedParser.watchEnclosure', 'Enclosure.getType', 'CALL', 'Read enclosure MIME type',
  guard='enclosure != null', cls='explicit', evidence='SRC core/FeedParser.java:175')
e('FeedParser.watchTorrentInfoHash', 'AtomItem.getEzRssTorrentItem', 'CALL', 'Read EzRSS metadata from an Atom entry',
  cls='non_standard', via='Item interface dispatch to AtomItem', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:236-238; impl/AtomItem.java:136-137')
e('FeedParser.watchTorrentInfoHash', 'Rss2Item.getEzRssTorrentItem', 'CALL', 'Read EzRSS metadata from an RSS 2.0 item',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:236-238; impl/Rss2Item.java:119-120')
e('FeedParser.watchTorrentInfoHash', 'EzRssTorrentItem.getInfoHash', 'CALL', 'Read the info hash from EzRSS metadata',
  guard='torrentItem != null', cls='explicit', evidence='SRC core/FeedParser.java:238-242')
e('Rss2Item.getEzRssTorrentItem', 'EzRss01Parser.<init>', 'CALL', 'Create the EzRSS 0.1 parser for this item',
  cls='explicit', evidence='SRC impl/Rss2Item.java:120; impl/EzRss01Parser.java:22-24')
e('Rss2Item.getEzRssTorrentItem', 'EzRss01Parser.parse', 'CALL', 'Parse EzRSS 0.1 metadata',
  cls='explicit', evidence='SRC impl/Rss2Item.java:120; impl/EzRss01Parser.java:26-36')
e('EzRss01Parser.parse', 'EzRssTorrentItem.<init>', 'CALL', 'Build the EzRSS torrent metadata object',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:35-36')
e('FeedParser.getItems', 'AtomItem.getPubDate', 'CALL', 'Read Atom entry publication date',
  cls='non_standard', via='Item interface dispatch to AtomItem', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:104; impl/AtomItem.java:80-82')
e('FeedParser.getItems', 'Rss2Item.getPubDate', 'CALL', 'Read RSS 2.0 item publication date',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:104; impl/Rss2Item.java:75-77')
e('FeedParser.getItems', 'Rss1Item.getPubDate', 'CALL', 'Read RSS 1.0 item publication date',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:104; impl/Rss1Item.java:76-79')
e('AtomItem.getPubDate', 'FeedUtils.convertAtomDate', 'CALL', 'Parse Atom publication date',
  guard='pubDate != null', cls='explicit', evidence='SRC impl/AtomItem.java:80-82')
e('Rss2Item.getPubDate', 'FeedUtils.<clinit>', 'FRAMEWORK', 'Initialize date formats before the first date parse',
  cls='non_standard', via='JVM class initialization before first static call', evidence='INFERRED JVM class initialization; SRC FeedUtils.java:14-18; impl/Rss2Item.java:75-77')
e('Rss2Item.getPubDate', 'FeedUtils.convertRss2Date', 'CALL', 'Parse RSS 2.0 publication date',
  guard='pubDate != null', cls='explicit', evidence='SRC impl/Rss2Item.java:75-77')
e('Rss1Item.getPubDate', 'FeedUtils.convertRss1Date', 'CALL', 'Parse RSS 1.0 publication date',
  guard='pubDate != null', cls='explicit', evidence='SRC impl/Rss1Item.java:76-79')
e('FeedUtils.convertRss1Date', 'FeedUtils.convertAtomDate', 'CALL', 'Reuse the Atom date parser for RSS 1.0 dates',
  cls='explicit', evidence='SRC FeedUtils.java:81-84')

UNREACHABLE.update({
    'FeedUtils.equalsOrNull': ('no_trigger_in_app', 'Its only caller, BaseItem.equals, is never invoked: the feed path only iterates Item lists and never tests Item equality.', 'SRC FeedUtils.java:112-114; BaseItem.java:53-58; FeedParser.java:95', 'SOURCE'),
})

# S4 batch 1 (40 methods): bundled feed parser methods with no source trigger.
# The app consumes only the subset shown in core/FeedParser.java:84-267; these
# accessors/constructors are never called by that code or by the parser itself.
_NO_FEED_TRIGGER = 'No app or bundled feed-parser source path calls this method.'
UNREACHABLE.update({
    'Enclosure.getLength': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Enclosure.java:52', 'SOURCE'),
    'EzRssTorrentItem.getContentLength': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC EzRssTorrentItem.java:69', 'SOURCE'),
    'EzRssTorrentItem.getFileName': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC EzRssTorrentItem.java:45', 'SOURCE'),
    'EzRssTorrentItem.getMagnetUri': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC EzRssTorrentItem.java:53', 'SOURCE'),
    'EzRssTorrentItem.getPeers': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC EzRssTorrentItem.java:85', 'SOURCE'),
    'EzRssTorrentItem.getSeeds': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC EzRssTorrentItem.java:77', 'SOURCE'),
    'EzRssTorrentItem.isVerified': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC EzRssTorrentItem.java:93', 'SOURCE'),
    'FeedException.<init>()': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC FeedException.java:8', 'SOURCE'),
    'FeedException.<init>(String,Throwable)': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC FeedException.java:19', 'SOURCE'),
    'FeedParserFactory.<init>': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC FeedParserFactory.java:16', 'SOURCE'),
    'FeedUtils.<init>': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC FeedUtils.java:12', 'SOURCE'),
    'XML.<init>': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC XML.java:7', 'SOURCE'),
    'AtomFeed.getCategories': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC AtomFeed.java:81', 'SOURCE'),
    'AtomFeed.getCopyright': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC AtomFeed.java:69', 'SOURCE'),
    'AtomFeed.getDescription': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC AtomFeed.java:56', 'SOURCE'),
    'AtomFeed.getLanguage': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC AtomFeed.java:62', 'SOURCE'),
    'AtomFeed.getLink': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC AtomFeed.java:50', 'SOURCE'),
    'AtomFeed.getPubDate': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC AtomFeed.java:75', 'SOURCE'),
    'AtomFeed.getType': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC AtomFeed.java:39', 'SOURCE'),
    'AtomItem.getAuthor': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC AtomItem.java:64', 'SOURCE'),
    'AtomItem.getCategories': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC AtomItem.java:86', 'SOURCE'),
    'AtomItem.getType': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC AtomItem.java:35', 'SOURCE'),
    'BaseElement.<init>(String,String)': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC BaseElement.java:29', 'SOURCE'),
    'BaseElement.getElementKeys': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC BaseElement.java:84', 'SOURCE'),
    'BaseElement.getName': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC BaseElement.java:51', 'SOURCE'),
    'Rss1Feed.getCategories': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss1Feed.java:98', 'SOURCE'),
    'Rss1Feed.getCopyright': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss1Feed.java:82', 'SOURCE'),
    'Rss1Feed.getDescription': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss1Feed.java:67', 'SOURCE'),
    'Rss1Feed.getLanguage': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss1Feed.java:74', 'SOURCE'),
    'Rss1Feed.getLink': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss1Feed.java:53', 'SOURCE'),
    'Rss1Feed.getPubDate': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss1Feed.java:90', 'SOURCE'),
    'Rss1Feed.getType': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss1Feed.java:41', 'SOURCE'),
    'Rss1Item.getAuthor': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss1Item.java:62', 'SOURCE'),
    'Rss1Item.getCategories': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss1Item.java:83', 'SOURCE'),
    'Rss1Item.getType': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss1Item.java:34', 'SOURCE'),
    'Rss2Feed.getCategories': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss2Feed.java:100', 'SOURCE'),
    'Rss2Feed.getCopyright': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss2Feed.java:82', 'SOURCE'),
    'Rss2Feed.getDescription': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss2Feed.java:68', 'SOURCE'),
    'Rss2Feed.getLanguage': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss2Feed.java:75', 'SOURCE'),
    'Rss2Feed.getLink': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss2Feed.java:54', 'SOURCE'),
})

# S4 batch 2 (40 methods): remaining unused feed accessors, unused NanoHTTPD
# public surface, and generated constructors absent from the uploaded sources.
_NO_NANO_TRIGGER = 'LibreTorrent uses the host/port constructor and the streaming response overloads; no source path calls this NanoHTTPD API.'
_NO_GENERATED_TRIGGER = 'Generated class constructor has no trigger in the compiled app call graph; source grep found no declaration.'
UNREACHABLE.update({
    'baseAdapters.BR.<init>': ('no_trigger_in_app', _NO_GENERATED_TRIGGER, 'INFERRED scratch/generated_class_grep.txt:1-2 (grep: no declaration)', 'INFERRED'),
    'Rss2Feed.getPubDate': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss2Feed.java:89', 'SOURCE'),
    'Rss2Feed.getType': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss2Feed.java:42', 'SOURCE'),
    'Rss2Item.getAuthor': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss2Item.java:63', 'SOURCE'),
    'Rss2Item.getCategories': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss2Item.java:81', 'SOURCE'),
    'Rss2Item.getType': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC Rss2Item.java:35', 'SOURCE'),
    'MediaRss.getPeerLinks': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC MediaRss.java:38', 'SOURCE'),
    'PeerLink.getHref': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC PeerLink.java:27', 'SOURCE'),
    'PeerLink.getType': ('no_trigger_in_app', _NO_FEED_TRIGGER, 'SRC PeerLink.java:38', 'SOURCE'),
    'NanoHTTPD.<init>(int)': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1544', 'SOURCE'),
    'NanoHTTPD.closeAllConnections': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1566', 'SOURCE'),
    'NanoHTTPD.decodeParameters(String)': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1619', 'SOURCE'),
    'NanoHTTPD.decodeParameters(Map)': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1604', 'SOURCE'),
    'NanoHTTPD.getHostname': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1675', 'SOURCE'),
    'NanoHTTPD.getListeningPort': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1663', 'SOURCE'),
    'NanoHTTPD.getMimeTypeForFile': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1503', 'SOURCE'),
    'NanoHTTPD.getTempFileManagerFactory': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1678', 'SOURCE'),
    'NanoHTTPD.isAlive': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1666', 'SOURCE'),
    'NanoHTTPD.loadMimeTypes': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1429', 'SOURCE'),
    'NanoHTTPD.makeSSLSocketFactory(String,char[])': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1484', 'SOURCE'),
    'NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManagerFactory)': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1473', 'SOURCE'),
    'NanoHTTPD.makeSSLSocketFactory(KeyStore,KeyManager[])': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1455', 'SOURCE'),
    'NanoHTTPD.makeSecure': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1684', 'SOURCE'),
    'NanoHTTPD.mimeTypes': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1418', 'SOURCE'),
    'NanoHTTPD.newChunkedResponse': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1690', 'SOURCE'),
    'NanoHTTPD.newFixedLengthResponse(String)': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1719', 'SOURCE'),
    'NanoHTTPD.setServerSocketFactory': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1672', 'SOURCE'),
    'NanoHTTPD.wasStarted': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:1848', 'SOURCE'),
    'NanoHTTPD$Cookie.<init>(String,String)': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:205', 'SOURCE'),
    'NanoHTTPD$Cookie.<init>(String,String,int)': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:208', 'SOURCE'),
    'NanoHTTPD$DefaultAsyncRunner.getRunning': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:315', 'SOURCE'),
    'NanoHTTPD$DefaultTempFile.open': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:366', 'SOURCE'),
    'NanoHTTPD$HTTPSession.<init>(NanoHTTPD,TempFileManager,InputStream,OutputStream)': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:479', 'SOURCE'),
    'NanoHTTPD$HTTPSession.getCookies': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:817', 'SOURCE'),
    'NanoHTTPD$HTTPSession.getInputStream': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:825', 'SOURCE'),
    'NanoHTTPD$SecureServerSocketFactory.<init>': ('no_trigger_in_app', _NO_NANO_TRIGGER, 'SRC NanoHTTPD.java:436', 'SOURCE'),
    'libretorrent.BR.<init>': ('no_trigger_in_app', _NO_GENERATED_TRIGGER, 'INFERRED scratch/generated_class_grep.txt:1-2 (grep: no declaration)', 'INFERRED'),
    'libretorrent.DataBinderMapperImpl$InnerBrLookup.<init>': ('no_trigger_in_app', _NO_GENERATED_TRIGGER, 'INFERRED scratch/generated_class_grep.txt:1-2 (grep: no declaration)', 'INFERRED'),
    'libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.<init>': ('no_trigger_in_app', _NO_GENERATED_TRIGGER, 'INFERRED scratch/generated_class_grep.txt:1-2 (grep: no declaration)', 'INFERRED'),
    'DataBindingTriggerClass.<init>': ('no_trigger_in_app', _NO_GENERATED_TRIGGER, 'INFERRED scratch/generated_class_grep.txt:1-2 (grep: no declaration)', 'INFERRED'),
})

# S4 batch 3: source-printed no-trigger cases. Methods whose dispatch or
# construction route was not closed remain OPEN in scratch/batch_003.md.
UNREACHABLE.update({
    'RepositoryHelper.<init>': ('no_trigger_in_app', 'RepositoryHelper exposes only static repository accessors; app code does not construct it.', 'SRC core/RepositoryHelper.java:36-76', 'SOURCE'),
    'FixedRingBuffer.<init>(int)': ('no_trigger_in_app', 'The one-argument constructor delegates to the two-argument overload; Logger constructs it with two arguments.', 'SRC core/collections/FixedRingBuffer.java:45-63; core/logger/Logger.java:65-90', 'SOURCE'),
    'DecodeException.<init>()': ('no_trigger_in_app', 'The inspected app constructions pass an exception; no zero-argument construction is present.', 'SRC core/exception/DecodeException.java:28-37; core/model/data/metainfo/TorrentMetaInfo.java:69,79,92; core/model/TorrentEngine.java:387', 'SOURCE'),
    'DecodeException.<init>(String)': ('no_trigger_in_app', 'The inspected app constructions pass an exception; no string-only construction is present.', 'SRC core/exception/DecodeException.java:30-37; core/model/data/metainfo/TorrentMetaInfo.java:69,79,92; core/model/TorrentEngine.java:387', 'SOURCE'),
    'FetchLinkException.<init>()': ('no_trigger_in_app', 'App call sites use string or exception arguments, not the zero-argument constructor.', 'SRC core/exception/FetchLinkException.java:28-38; core/utils/Utils.java:467,474,493,509,522', 'SOURCE'),
    'FileAlreadyExistsException.<init>()': ('no_trigger_in_app', 'No app construction site for this exception is present in the inspected source.', 'SRC core/exception/FileAlreadyExistsException.java:22-30', 'SOURCE'),
    'FileAlreadyExistsException.<init>(String)': ('no_trigger_in_app', 'No app construction site for this exception is present in the inspected source.', 'SRC core/exception/FileAlreadyExistsException.java:22-30', 'SOURCE'),
    'FreeSpaceException.<init>(Exception)': ('no_trigger_in_app', 'Observed app constructions use the no-argument or string overload, not this exception overload.', 'SRC core/exception/FreeSpaceException.java:26-40; core/model/TorrentEngine.java:1201; core/model/session/TorrentDownloadImpl.java:417; ui/addtorrent/AddTorrentViewModel.java:493-496', 'SOURCE'),
    'IPFilterException.<init>()': ('no_trigger_in_app', 'Observed IP filter errors construct the string overload, not the zero-argument overload.', 'SRC core/exception/IPFilterException.java:22-34; core/model/session/IPFilterImpl.java:44,54,58', 'SOURCE'),
    'IPFilterException.<init>(Exception)': ('no_trigger_in_app', 'Observed IP filter errors construct the string overload; no exception-argument construction is present.', 'SRC core/exception/IPFilterException.java:22-34; core/model/session/IPFilterImpl.java:44,54,58', 'SOURCE'),
    'NoFilesSelectedException.<init>(String)': ('no_trigger_in_app', 'The inspected app construction uses the no-argument overload.', 'SRC core/exception/NoFilesSelectedException.java:22-30; ui/addtorrent/AddTorrentViewModel.java:493', 'SOURCE'),
    'NormalizeUrlException.<init>(String)': ('no_trigger_in_app', 'The inspected app construction passes both a string and an exception.', 'SRC core/urlnormalizer/NormalizeUrl.java:185; core/exception/NormalizeUrlException.java:19-31', 'SOURCE'),
    'TorrentAlreadyExistsException.<init>(String)': ('no_trigger_in_app', 'The inspected app construction uses the no-argument overload.', 'SRC core/exception/TorrentAlreadyExistsException.java:22-30; core/model/session/TorrentSessionImpl.java:282', 'SOURCE'),
    'TorrentFilterCollection.<init>': ('no_trigger_in_app', 'The class exposes static filter factories; app call sites use those static methods and do not construct instances.', 'SRC core/filter/TorrentFilterCollection.java:26-104; ui/main/MainActivity.java:300-306,335,499-521; ui/main/MainViewModel.java:53-55', 'SOURCE'),
    'LogEntry.getTimeStamp': ('no_trigger_in_app', 'No app call site invokes this accessor; timestamp formatting reads the field directly.', 'SRC core/logger/LogEntry.java:36-47,66-74', 'SOURCE'),
    'Logger.getEntry': ('no_trigger_in_app', 'No app call site invokes this accessor.', 'SRC core/logger/Logger.java:301', 'SOURCE'),
    'Logger.stopRecording(OutputStream)': ('no_trigger_in_app', 'App call sites use the no-argument or two-argument form, not this one-argument overload.', 'SRC core/logger/Logger.java:362-372; service/SaveLogWorker.java:93; core/model/session/TorrentSessionImpl.java:1021; ui/log/LogViewModel.java:183', 'SOURCE'),
    'Logger.write(OutputStream)': ('no_trigger_in_app', 'App call sites use the two-argument form, not this one-argument overload.', 'SRC core/logger/Logger.java:405-410; service/SaveLogWorker.java:95', 'SOURCE'),
    'TorrentInfoProvider.getInstance(TorrentEngine,TagRepository)': ('no_trigger_in_app', 'The overload has no app call site; the Context overload directly invokes the private constructor.', 'SRC core/model/TorrentInfoProvider.java:63-87; service/TorrentService.java:108-110', 'SOURCE'),
    'AdvancedTorrentInfo.<init>()': ('no_trigger_in_app', 'App code creates this model through the parameterized constructor; parcel restoration uses the Parcel constructor.', 'SRC core/model/data/AdvancedTorrentInfo.java:49-74,119-126; core/model/TorrentEngine.java:846-858', 'SOURCE'),
    'PeerInfo$ConnectionType.<init>': ('no_trigger_in_app', 'The nested type declares integer constants only; no app construction site is present.', 'SRC core/model/data/PeerInfo.java:49-54', 'SOURCE'),
    'TrackerInfo$Status.<init>': ('no_trigger_in_app', 'The nested type declares integer constants only; no app construction site is present.', 'SRC core/model/data/TrackerInfo.java:49-55,88-91', 'SOURCE'),
    'FeedChannel.<init>(String)': ('no_trigger_in_app', 'The app construction uses seven arguments; parcel restoration uses the Parcel constructor.', 'SRC core/model/data/entity/FeedChannel.java:52-83,104-116; ui/addfeed/AddFeedViewModel.java:173', 'SOURCE'),
    'IPFilterParser.<init>(boolean)': ('no_trigger_in_app', 'The source-root constructor search finds only the no-argument app construction; the boolean overload has no in-app caller.', 'SRC core/model/session/IPFilterParser.java:49-56; core/model/session/TorrentSessionImpl.java:731; scratch/batch_003_printed.txt search output', 'SOURCE'),
    'PriorityConverter.<init>': ('no_trigger_in_app', 'The converter exposes static methods and no app instance construction is present.', 'SRC core/model/session/PriorityConverter.java:25-54,94-110; core/model/session/TorrentDownloadImpl.java:731,1139,1646; core/model/session/TorrentSessionImpl.java:437', 'SOURCE'),
    'SessionErrors.<init>': ('no_trigger_in_app', 'The package-private utility class is used through static methods and has no app instance construction.', 'SRC core/model/session/SessionErrors.java:26-63; core/model/session/TorrentSessionImpl.java:1117-1134; core/model/session/TorrentDownloadImpl.java:352-382', 'SOURCE'),
    'TorrentCriticalWork.isMoving': ('no_trigger_in_app', 'No app source call site invokes this accessor.', 'SRC core/model/session/TorrentCriticalWork.java:57-72', 'SOURCE'),
    'TorrentCriticalWork.isSaveResume': ('no_trigger_in_app', 'No app source call site invokes this accessor.', 'SRC core/model/session/TorrentCriticalWork.java:57-86', 'SOURCE'),
    'TorrentCriticalWork$Type.<clinit>': ('no_trigger_in_app', 'The enum constants have no references elsewhere in app source.', 'SRC core/model/session/TorrentCriticalWork.java:30-36,93-97', 'SOURCE'),
    'TorrentDownloadImpl.getMaxConnections': ('no_trigger_in_app', 'No app invocation of this accessor is present in the inspected source.', 'SRC core/model/session/TorrentDownloadImpl.java:1436-1448; core/model/session/TorrentDownload.java:166', 'SOURCE'),
    'TorrentDownloadImpl.getMaxUploads': ('no_trigger_in_app', 'No app invocation of this accessor is present in the inspected source.', 'SRC core/model/session/TorrentDownloadImpl.java:1453-1465; core/model/session/TorrentDownload.java:170', 'SOURCE'),
    'TorrentDownloadImpl.getSize': ('no_trigger_in_app', 'No app invocation on TorrentDownload is present; other getSize hits are different classes.', 'SRC core/model/session/TorrentDownloadImpl.java:745-752; core/model/session/TorrentDownload.java:70; core/model/data/metainfo/BencodeFileItem.java:61; core/utils/TorrentContentFileTreeUtils.java:102', 'SOURCE'),
    'TorrentDownloadImpl.isAutoManaged': ('no_trigger_in_app', 'No app invocation of this accessor is present in the inspected source.', 'SRC core/model/session/TorrentDownloadImpl.java:690-697; core/model/session/TorrentDownload.java:59', 'SOURCE'),
    'TorrentEngine.addTorrent(AddTorrentParams,boolean)': ('no_trigger_in_app', 'The source-root call search finds no app caller of this overload; the observed CreateTorrentViewModel call uses the URI overload.', 'SRC core/model/TorrentEngine.java:329-340; ui/createtorrent/CreateTorrentViewModel.java:372-380; scratch/batch_003_addtorrent_calls.txt', 'SOURCE'),
    'TorrentEngine.lambda$addTorrent$8': ('no_trigger_in_app', 'This synthetic body is registered only inside the uncalled AddTorrentParams overload, and the source-root call search finds no app caller of that overload.', 'SRC core/model/TorrentEngine.java:329-340; scratch/batch_003_addtorrent_calls.txt', 'SOURCE'),
    'TorrentDownloadImpl.getTorrentId': ('no_trigger_in_app', 'The source-root search finds no app invocation of the TorrentDownload interface method; the same-named app invocations target DetailTorrentFragment instead.', 'SRC core/model/session/TorrentDownloadImpl.java:530-538; core/model/session/TorrentDownload.java:44-45; scratch/batch_003_gettorrentid_calls.txt', 'SOURCE'),
    'FileNode$Type.<init>': ('no_trigger_in_app', 'The nested Type class has no explicit constructor and source contains no construction of a Type instance; code reads its static DIR/FILE constants instead.', 'SRC core/model/filetree/FileNode.java:30-36; scratch/batch_003_reaudit_exact_calls.txt', 'SOURCE'),
    'FileTree.<init>(int,String,long,int)': ('no_trigger_in_app', 'The source-root construction and super-constructor searches show no invocation of this four-argument overload; the app uses subclass constructors whose super calls pass three or five arguments.', 'SRC core/model/filetree/FileTree.java:51-73; core/model/filetree/BencodeFileTree.java:35-48; core/model/filetree/TorrentContentFileTree.java:30-48; scratch/batch_003_reaudit_exact_calls.txt', 'SOURCE'),
})

# S4 batch 4: methods whose source declarations and exact source-root call
# searches were printed in scratch/batch_004_printed.txt and
# scratch/batch_004_exact_calls.txt. Filesystem delegates without a complete
# entry-to-method route were initially left OPEN; their overload/caller checks
# are in scratch/batch_004_independent_routes.txt.
_BATCH4_NO_CALLER = 'No app source call site reaches this method; see the printed declaration and exact source-root search output.'
UNREACHABLE.update({
    'TorrentDownloadImpl.isDownloading': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/model/session/TorrentDownloadImpl.java:1415-1419; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'SettingsRepositoryImpl$Default.<init>': ('no_trigger_in_app', 'The private nested class contains only static defaults; app source does not instantiate it.', 'SRC core/settings/SettingsRepositoryImpl.java:41-75; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'BaseSorting$Direction.fromValue': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/sorting/BaseSorting.java:26-39; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'DatabaseMigration.<init>': ('no_trigger_in_app', 'DatabaseMigration exposes the static migration factory; app source does not instantiate DatabaseMigration.', 'SRC core/storage/DatabaseMigration.java:39-55; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'DatabaseMigration$RoomDatabaseMigration$OldDataModel.<init>': ('no_trigger_in_app', 'OldDataModel contains only static filename constants and has no app construction site.', 'SRC core/storage/DatabaseMigration.java:120-127; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'FeedRepositoryImpl.getSerializeFileFormat': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/storage/FeedRepositoryImpl.java:65-69; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'FeedRepositoryImpl.getSerializeMimeType': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/storage/FeedRepositoryImpl.java:71-75; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'TorrentRepositoryImpl.getTorrentDataDir': ('no_trigger_in_app', 'This private helper has no app caller; the only source call in its class is from it to makeTorrentDataDir.', 'SRC core/storage/TorrentRepositoryImpl.java:140-155; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'TorrentRepositoryImpl.makeTorrentDataDir': ('no_trigger_in_app', 'The private helper is called only by getTorrentDataDir, which has no app caller.', 'SRC core/storage/TorrentRepositoryImpl.java:145-170; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'TorrentRepositoryImpl$FileDataModel.<init>': ('no_trigger_in_app', 'The private nested class contains only a static filename constant and has no app construction site.', 'SRC core/storage/TorrentRepositoryImpl.java:40-45; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'DefaultFsModule.getName': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/system/DefaultFsModule.java:40-44; core/system/FsModuleResolverImpl.java:35-49; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'DefaultFsModule.lastModified': ('no_trigger_in_app', 'Filesystem facade dispatch has no app caller; the default module method is reached only through that dispatch.', 'SRC core/system/DefaultFsModule.java:113-118; core/system/FileSystemFacadeImpl.java:160-166; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'FileSystemFacadeImpl.isStorageWritable': ('no_trigger_in_app', 'The only app caller is makeTorrentDataDir, reached only through the uncalled private getTorrentDataDir helper.', 'SRC core/system/FileSystemFacadeImpl.java:172-178; core/storage/TorrentRepositoryImpl.java:145-170; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'FileSystemFacadeImpl.isValidFatFilename': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/system/FileSystemFacadeImpl.java:331-335; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'FileSystemFacadeImpl.lastModified': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/system/FileSystemFacadeImpl.java:160-166; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem.delete(FakePath)': ('no_trigger_in_app', 'The SAF module calls delete(Uri), not this FakePath overload.', 'SRC core/system/SafFileSystem.java:314-323; core/system/SafFsModule.java:83-89; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem.exists(FakePath)': ('no_trigger_in_app', 'The SAF module calls exists(Uri), not this FakePath overload.', 'SRC core/system/SafFileSystem.java:329-366; core/system/SafFsModule.java:135-139; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem.mkdirs': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/system/SafFileSystem.java:504-530; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem.openFD(Uri,String)': ('no_trigger_in_app', 'Only the two outer openFD overloads call this overload, and neither outer overload has an app caller.', 'SRC core/system/SafFileSystem.java:382-422; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem.openFD(Uri,String,String)': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/system/SafFileSystem.java:382-390; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem.openFD(FakePath,String)': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/system/SafFileSystem.java:394-402; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem.stat(Uri,String)': ('no_trigger_in_app', 'The SAF module calls stat(Uri), not the two-argument stat overload.', 'SRC core/system/SafFileSystem.java:426-440,459-470; core/system/SafFsModule.java:45-52,141-148; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem.stat(FakePath)': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/system/SafFileSystem.java:472-485; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem$FakePath.deserialize': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/system/SafFileSystem.java:118-130; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem$FakePath.isFakePath': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/system/SafFileSystem.java:157-160; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFileSystem$FakePath.relativePath': ('no_trigger_in_app', 'The only path-node accessor used by the implementation is makeRelativePathNodes; no app source invokes relativePath.', 'SRC core/system/SafFileSystem.java:140-155; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFsModule.getName': ('no_trigger_in_app', 'No facade dispatch or app call invokes the interface implementation.', 'SRC core/system/SafFsModule.java:45-52; core/system/FsModuleResolverImpl.java:35-49; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SafFsModule.lastModified': ('no_trigger_in_app', 'Its only dispatcher is FileSystemFacadeImpl.lastModified, which has no app caller.', 'SRC core/system/SafFsModule.java:141-148; core/system/FileSystemFacadeImpl.java:160-166; scratch/batch_004_independent_routes.txt', 'SOURCE'),
    'SystemFacadeHelper.<init>': ('no_trigger_in_app', 'SystemFacadeHelper is used through static singleton getters; app source has no construction site.', 'SRC core/system/SystemFacadeHelper.java:26-47; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'NormalizeUrl.<init>': ('no_trigger_in_app', 'NormalizeUrl declares a private constructor to disallow instantiation.', 'SRC core/urlnormalizer/NormalizeUrl.java:14-15; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'NormalizeUrl.normalize(String)': ('no_trigger_in_app', 'App callers invoke the two-argument overload; this one-argument forwarding overload has no app caller.', 'SRC core/urlnormalizer/NormalizeUrl.java:165-168; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'PathResolver.<init>': ('no_trigger_in_app', 'PathResolver declares a private constructor to disallow instantiation.', 'SRC core/urlnormalizer/PathResolver.java:9-15; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'PercentEncoder.<init>': ('no_trigger_in_app', 'PercentEncoder declares a private constructor to disallow instantiation.', 'SRC core/urlnormalizer/PercentEncoder.java:12-22; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'BencodeFileTreeUtils.<init>': ('no_trigger_in_app', 'The utility class has no app construction site.', 'SRC core/utils/BencodeFileTreeUtils.java:40-58; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'BindingAdapterUtils.<init>': ('no_trigger_in_app', 'The utility class has no app construction site.', 'SRC core/utils/BindingAdapterUtils.java:36-54; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'DateUtils.<init>': ('no_trigger_in_app', 'The utility class has no app construction site.', 'SRC core/utils/DateUtils.java:31-48; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'TorrentContentFileTreeUtils.<init>': ('no_trigger_in_app', 'The utility class has no app construction site.', 'SRC core/utils/TorrentContentFileTreeUtils.java:40-58; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'Utils.<init>': ('no_trigger_in_app', 'The utility class has no app construction site.', 'SRC core/utils/Utils.java:32-60; scratch/batch_004_exact_calls.txt', 'SOURCE'),
    'Utils.normalizeURL': ('no_trigger_in_app', _BATCH4_NO_CALLER, 'SRC core/utils/Utils.java:220-227; scratch/batch_004_exact_calls.txt', 'SOURCE'),
})

# S4 batch 10: three source-verified no-trigger methods. The other 37 rows
# remain OPEN in scratch/batch_010.md pending generated/framework dispatch evidence.
UNREACHABLE.update({
    'Scheduler.<init>': ('no_trigger_in_app', 'Scheduler is a static utility with no app construction site.', 'SRC service/Scheduler.java:43-53; scratch/batch_010_independent_printed.txt', 'SOURCE'),
    'RecyclerViewDividerDecoration.<init>(Context,int)': ('no_trigger_in_app', 'App constructor calls use the Drawable overload; there is no app call to this Context,int overload.', 'SRC ui/customviews/RecyclerViewDividerDecoration.java:35-47; scratch/batch_010_independent_printed.txt', 'SOURCE'),
    'LogSettingsFragment.newInstance': ('no_trigger_in_app', 'The factory has no app source caller.', 'SRC ui/log/LogSettingsFragment.java:43-49; scratch/batch_010_independent_printed.txt', 'SOURCE'),
})

# S4 batch 11: six source-verified no-trigger entries; the three XML preference
# constructor rows remain OPEN in scratch/batch_011.md.
UNREACHABLE.update({
    'SettingsFragment.newInstance': ('no_trigger_in_app', 'No app source calls this factory.', 'SRC ui/settings/SettingsFragment.java:63-70; scratch/batch_011_independent_printed.txt', 'SOURCE'),
    'AddTagButton.<init>(Context,AttributeSet)': ('no_trigger_in_app', 'The app constructs AddTagButton using the Context-only overload and no AddTagButton XML element exists.', 'SRC ui/tag/AddTagButton.java:36-47; ui/tag/TorrentTagsList.java:78-86; scratch/batch_011_independent_printed.txt', 'SOURCE'),
    'AddTagButton.<init>(Context,AttributeSet,int)': ('no_trigger_in_app', 'No app call uses this constructor signature and no AddTagButton XML element exists.', 'SRC ui/tag/AddTagButton.java:49-57; scratch/batch_011_independent_printed.txt', 'SOURCE'),
    'tag.TagItem.hashCode': ('no_trigger_in_app', 'The app tag adapter compares items with isSame and equals; no app hash-based use or direct call is present.', 'SRC ui/tag/TagItem.java:34-51; ui/tag/TagsAdapter.java:65-81; scratch/batch_011_independent_printed.txt', 'SOURCE'),
    'tag.TagItem.toString': ('no_trigger_in_app', 'No app call or string interpolation invokes this override.', 'SRC ui/tag/TagItem.java:53-59; scratch/batch_011_independent_printed.txt', 'SOURCE'),
    'TorrentTagsList.<init>(Context)': ('no_trigger_in_app', 'The XML layout invokes the Context,AttributeSet constructor; no app source constructs the Context-only overload.', 'SRC ui/tag/TorrentTagsList.java:23-33; FW-SRC core/java/android/view/LayoutInflater.java:90-91,615,639-647; scratch/batch_011_independent_printed.txt; scratch/batch_011_framework_printed.txt', 'SOURCE'),
})

# S4 batch 12: nine methods have no source caller in the app or bundled feed
# parser. All parser methods with a source caller stay OPEN until a complete
# hand-written entry-to-method route is recorded; see scratch/batch_012.md.
_BATCH12_NO_FEED_CALLER = 'No app or bundled feed-parser source path calls this method.'
UNREACHABLE.update({
    'Enclosure.equals': ('no_trigger_in_app', _BATCH12_NO_FEED_CALLER, 'SRC com/ernieyu/feedparser/Enclosure.java:56-67; scratch/batch_012_call_audit.txt', 'SOURCE'),
    'Enclosure.hashCode': ('no_trigger_in_app', _BATCH12_NO_FEED_CALLER, 'SRC com/ernieyu/feedparser/Enclosure.java:69-75; scratch/batch_012_call_audit.txt', 'SOURCE'),
    'Enclosure.toString': ('no_trigger_in_app', _BATCH12_NO_FEED_CALLER, 'SRC com/ernieyu/feedparser/Enclosure.java:77-84; scratch/batch_012_call_audit.txt', 'SOURCE'),
    'EzRssTorrentItem.equals': ('no_trigger_in_app', _BATCH12_NO_FEED_CALLER, 'SRC com/ernieyu/feedparser/EzRssTorrentItem.java:97-113; scratch/batch_012_call_audit.txt', 'SOURCE'),
    'EzRssTorrentItem.hashCode': ('no_trigger_in_app', _BATCH12_NO_FEED_CALLER, 'SRC com/ernieyu/feedparser/EzRssTorrentItem.java:115-125; scratch/batch_012_call_audit.txt', 'SOURCE'),
    'EzRssTorrentItem.toString': ('no_trigger_in_app', _BATCH12_NO_FEED_CALLER, 'SRC com/ernieyu/feedparser/EzRssTorrentItem.java:127-139; scratch/batch_012_call_audit.txt', 'SOURCE'),
    'XMLInputStream.length': ('no_trigger_in_app', _BATCH12_NO_FEED_CALLER, 'SRC com/ernieyu/feedparser/XMLInputStream.java:31-40; scratch/batch_012_call_audit.txt', 'SOURCE'),
    'AtomFeed.toString': ('no_trigger_in_app', _BATCH12_NO_FEED_CALLER, 'SRC com/ernieyu/feedparser/impl/AtomFeed.java:109-113; scratch/batch_012_call_audit.txt', 'SOURCE'),
    'AtomItem.getDescription': ('no_trigger_in_app', _BATCH12_NO_FEED_CALLER, 'SRC com/ernieyu/feedparser/impl/AtomItem.java:56-61; scratch/batch_012_call_audit.txt', 'SOURCE'),
})

# S4 batch 15: NanoHTTPD base dispatch/API paths absent from this app's use.
_BATCH15_NO_CALLER = 'The uploaded app subclass overrides this base method or has no caller for this helper; app source has no route to it.'
UNREACHABLE.update({
    'NanoHTTPD.serve(String,Method,Map,Map,Map)': ('no_trigger_in_app', 'Only base serve(IHTTPSession) calls this overload; the app subclass overrides serve(IHTTPSession) and does not call super.serve.', 'SRC org/nanohttpd/NanoHTTPD.java:1732-1746,1750-1770; org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java:110-121; scratch/batch_015_independent_printed.txt', 'SOURCE'),
    'NanoHTTPD.serve(IHTTPSession)': ('no_trigger_in_app', 'ClientHandler makes a virtual serve(this) call, which dispatches to TorrentStreamServer.serve; the override does not call super.serve.', 'SRC org/nanohttpd/NanoHTTPD.java:720; org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java:110-121; scratch/batch_015_independent_printed.txt', 'SOURCE'),
    'NanoHTTPD$CookieHandler.delete': ('no_trigger_in_app', _BATCH15_NO_CALLER, 'SRC org/nanohttpd/NanoHTTPD.java:252-254; scratch/batch_015_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$CookieHandler.iterator': ('no_trigger_in_app', _BATCH15_NO_CALLER, 'SRC org/nanohttpd/NanoHTTPD.java:255-259; scratch/batch_015_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$CookieHandler.read': ('no_trigger_in_app', _BATCH15_NO_CALLER, 'SRC org/nanohttpd/NanoHTTPD.java:260-269; scratch/batch_015_helper_printed.txt', 'SOURCE'),
})

# S4 batch 16: unused cookie and request-body parsing helpers. The app's
# TorrentStreamServer override does not invoke NanoHTTPD's base serve body parser.
_BATCH16_BODY_PATH_CLOSED = 'The app override bypasses the only caller path, which is NanoHTTPD base request-body parsing.'
UNREACHABLE.update({
    'NanoHTTPD$CookieHandler.set(String,String,int)': ('no_trigger_in_app', 'The only in-scope caller is CookieHandler.delete, which is itself not on the app route.', 'SRC org/nanohttpd/NanoHTTPD.java:252-254,283-285; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$CookieHandler.set(Cookie)': ('no_trigger_in_app', 'No app or in-scope source calls this CookieHandler setter.', 'SRC org/nanohttpd/NanoHTTPD.java:270-272; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$DefaultTempFile.<init>': ('no_trigger_in_app', _BATCH16_BODY_PATH_CLOSED, 'SRC org/nanohttpd/NanoHTTPD.java:402-405,865-877,1732-1747; core/model/stream/TorrentStreamServer.java:110-121; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$DefaultTempFile.delete': ('no_trigger_in_app', 'A temp file can reach the manager list only from unreachable createTempFile; ordinary cleanup clears an empty list.', 'SRC org/nanohttpd/NanoHTTPD.java:391-405,865-877,1732-1747; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$DefaultTempFile.getName': ('no_trigger_in_app', _BATCH16_BODY_PATH_CLOSED, 'SRC org/nanohttpd/NanoHTTPD.java:362-364,840-844,944-956,1732-1747; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$DefaultTempFileManager.createTempFile': ('no_trigger_in_app', _BATCH16_BODY_PATH_CLOSED, 'SRC org/nanohttpd/NanoHTTPD.java:402-405,865-877,1732-1747; core/model/stream/TorrentStreamServer.java:110-121; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$HTTPSession.decodeMultipartFormData': ('no_trigger_in_app', _BATCH16_BODY_PATH_CLOSED, 'SRC org/nanohttpd/NanoHTTPD.java:544-547,907-915,1732-1747; core/model/stream/TorrentStreamServer.java:110-121; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$HTTPSession.getAttributeFromContentHeader': ('no_trigger_in_app', _BATCH16_BODY_PATH_CLOSED, 'SRC org/nanohttpd/NanoHTTPD.java:907-915,936-939,1732-1747; core/model/stream/TorrentStreamServer.java:110-121; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$HTTPSession.getBodySize': ('no_trigger_in_app', 'Only executable caller is parseBody; other source mention is a TODO comment.', 'SRC org/nanohttpd/NanoHTTPD.java:717,856-868,1732-1747; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$HTTPSession.getBoundaryPositions': ('no_trigger_in_app', 'Only called from unreachable decodeMultipartFormData.', 'SRC org/nanohttpd/NanoHTTPD.java:544-547,781-805,1732-1747; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$HTTPSession.getMethod': ('no_trigger_in_app', 'Only executable caller is base serve(IHTTPSession), which the app override bypasses.', 'SRC org/nanohttpd/NanoHTTPD.java:829-831,1732-1747; core/model/stream/TorrentStreamServer.java:110-121; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$HTTPSession.getQueryParameterString': ('no_trigger_in_app', 'Only executable call is in base serve(IHTTPSession), which the app override bypasses.', 'SRC org/nanohttpd/NanoHTTPD.java:837-839,1732-1747; core/model/stream/TorrentStreamServer.java:110-121; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$HTTPSession.getTmpBucket': ('no_trigger_in_app', _BATCH16_BODY_PATH_CLOSED, 'SRC org/nanohttpd/NanoHTTPD.java:840-847,865-877,1732-1747; core/model/stream/TorrentStreamServer.java:110-121; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$HTTPSession.parseBody': ('no_trigger_in_app', 'Base serve calls parseBody only for POST/PUT; TorrentStreamServer overrides serve and does not call super.serve(session).', 'SRC org/nanohttpd/NanoHTTPD.java:865-935,1732-1747; core/model/stream/TorrentStreamServer.java:110-121; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$HTTPSession.saveTmpFile': ('no_trigger_in_app', 'Only callers are multipart/PUT branches inside unreachable parseBody.', 'SRC org/nanohttpd/NanoHTTPD.java:606,929-930,944-960,1732-1747; scratch/batch_016_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$HTTPSession.scipOverNewLine': ('no_trigger_in_app', _BATCH16_BODY_PATH_CLOSED, 'SRC org/nanohttpd/NanoHTTPD.java:590-592,625-630,544-547; scratch/batch_016_helper_printed.txt', 'SOURCE'),
})

# S4 batch 17: unused response getters/setters and secure socket factory.
_BATCH17_NO_CALLER = 'No app or NanoHTTPD request-path caller invokes this method.'
UNREACHABLE.update({
    'NanoHTTPD$Response.getData': ('no_trigger_in_app', _BATCH17_NO_CALLER, 'SRC org/nanohttpd/NanoHTTPD.java:1147-1149; scratch/batch_017_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$Response.getRequestMethod': ('no_trigger_in_app', _BATCH17_NO_CALLER, 'SRC org/nanohttpd/NanoHTTPD.java:1161-1163; scratch/batch_017_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$Response.getStatus': ('no_trigger_in_app', 'Response.send reads the status field directly; no source call to this getter was found.', 'SRC org/nanohttpd/NanoHTTPD.java:1164-1166,1188-1192; scratch/batch_017_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$Response.setData': ('no_trigger_in_app', 'The app constructs responses with constructors and no source call to this setter was found.', 'SRC org/nanohttpd/NanoHTTPD.java:1293-1295; scratch/batch_017_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$Response.setStatus': ('no_trigger_in_app', _BATCH17_NO_CALLER, 'SRC org/nanohttpd/NanoHTTPD.java:1302-1304; scratch/batch_017_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$Response$Status.getRequestStatus': ('no_trigger_in_app', _BATCH17_NO_CALLER, 'SRC org/nanohttpd/NanoHTTPD.java:1055-1058; scratch/batch_017_helper_printed.txt', 'SOURCE'),
    'NanoHTTPD$SecureServerSocketFactory.create': ('no_trigger_in_app', 'Installed only by NanoHTTPD.makeSecure; no app call to makeSecure or setServerSocketFactory was found.', 'SRC org/nanohttpd/NanoHTTPD.java:1684-1685; scratch/batch_017_helper_printed.txt', 'SOURCE'),
})

# S4 batch 18: InputFilterRange bounds are stored and used internally; their
# public getters have no app or library-source caller.
UNREACHABLE.update({
    'InputFilterRange.getMax': ('no_trigger_in_app', 'Full app source search finds only the declaration; the filter reads the field internally.', 'SRC core/InputFilterRange.java:58-62; scratch/batch_018_independent_printed.txt', 'SOURCE'),
    'InputFilterRange.getMin': ('no_trigger_in_app', 'Full app source search finds only the declaration; the filter reads the field internally.', 'SRC core/InputFilterRange.java:52-56; scratch/batch_018_independent_printed.txt', 'SOURCE'),
})

# S4 batch 19: uncalled FixedRingBuffer public APIs/overloads; Logger uses the
# single-element add and does not use the query/removal helpers below.
_BATCH19_NO_BUFFER_CALLER = 'No app source path invokes this FixedRingBuffer method or overload.'
UNREACHABLE.update({
    'FixedRingBuffer.add(Iterable)': ('no_trigger_in_app', 'Logger calls add(entry) with one LogEntry; no source caller uses the Iterable overload.', 'SRC core/collections/FixedRingBuffer.java:80-84; core/logger/Logger.java:99-110,139-156; scratch/batch_019_independent_printed.txt', 'SOURCE'),
    'FixedRingBuffer.contains': ('no_trigger_in_app', _BATCH19_NO_BUFFER_CALLER, 'SRC core/collections/FixedRingBuffer.java:179-188; scratch/batch_019_independent_printed.txt', 'SOURCE'),
    'FixedRingBuffer.getAllocatedSize': ('no_trigger_in_app', _BATCH19_NO_BUFFER_CALLER, 'SRC core/collections/FixedRingBuffer.java:75-78; scratch/batch_019_independent_printed.txt', 'SOURCE'),
    'FixedRingBuffer.indexOf': ('no_trigger_in_app', 'Only called by the unused remove overload.', 'SRC core/collections/FixedRingBuffer.java:99-123; scratch/batch_019_helper_printed.txt', 'SOURCE'),
    'FixedRingBuffer.isFull': ('no_trigger_in_app', _BATCH19_NO_BUFFER_CALLER, 'SRC core/collections/FixedRingBuffer.java:174-177; scratch/batch_019_helper_printed.txt', 'SOURCE'),
    'FixedRingBuffer.remove': ('no_trigger_in_app', _BATCH19_NO_BUFFER_CALLER, 'SRC core/collections/FixedRingBuffer.java:99-110; scratch/batch_019_helper_printed.txt', 'SOURCE'),
    'FixedRingBuffer.removeAt': ('no_trigger_in_app', 'Only called by the unused remove overload.', 'SRC core/collections/FixedRingBuffer.java:125-148; scratch/batch_019_helper_printed.txt', 'SOURCE'),
})

# S4 batch 20: LogEntry.hashCode is unused by the source-backed log adapter.
UNREACHABLE.update({
    'LogEntry.hashCode': ('no_trigger_in_app', 'The log adapter compares IDs and calls equals; no app source uses LogEntry as a hash key or calls this override.', 'SRC core/logger/LogEntry.java:92-101; ui/log/LogAdapter.java:67-81; scratch/batch_020_independent_printed.txt', 'SOURCE'),
})

# S4 batch 21: AddTorrentParams is created and consumed in app code, not
# transported through Parcel; its hash/string overrides are also unused.
UNREACHABLE.update({
    'AddTorrentParams.<init>(Parcel)': ('no_trigger_in_app', 'Only Parcelable.Creator.createFromParcel constructs this overload; app source does not parcel or transport AddTorrentParams.', 'SRC core/model/AddTorrentParams.java:77-82,109-113; scratch/batch_021_helper_printed.txt', 'SOURCE'),
    'AddTorrentParams.describeContents': ('no_trigger_in_app', 'No app source parcels AddTorrentParams, so no framework call path reaches this Parcelable method.', 'SRC core/model/AddTorrentParams.java:91-93; scratch/batch_021_helper_printed.txt', 'SOURCE'),
    'AddTorrentParams.hashCode': ('no_trigger_in_app', 'No source collection or callsite uses AddTorrentParams.hashCode.', 'SRC core/model/AddTorrentParams.java:122-125; scratch/batch_021_helper_printed.txt', 'SOURCE'),
    'AddTorrentParams.toString': ('no_trigger_in_app', 'No explicit caller or app string formatting of AddTorrentParams was found.', 'SRC core/model/AddTorrentParams.java:127-142; scratch/batch_021_helper_printed.txt', 'SOURCE'),
})

# S4 batch 22: the app uses AddTorrentParams in memory; it is not parcelled.
UNREACHABLE.update({
    'AddTorrentParams.writeToParcel': ('no_trigger_in_app', 'No app code writes AddTorrentParams to a Parcel; it is passed directly to engine/session methods.', 'SRC core/model/AddTorrentParams.java:90-107; scratch/batch_022_independent_printed.txt', 'SOURCE'),
    'AddTorrentParams$1.createFromParcel': ('no_trigger_in_app', 'The Creator is declared, but no app Parcel transport uses it to read AddTorrentParams.', 'SRC core/model/AddTorrentParams.java:109-113; scratch/batch_022_independent_printed.txt', 'SOURCE'),
    'AddTorrentParams$1.newArray': ('no_trigger_in_app', 'No app Parcel path invokes the Creator array factory.', 'SRC core/model/AddTorrentParams.java:109,116-118; scratch/batch_022_independent_printed.txt', 'SOURCE'),
})

# S4 batch 29: MagnetInfo stays in memory; the app has no Parcel transport for it.
UNREACHABLE.update({
    'MagnetInfo.writeToParcel': ('no_trigger_in_app', 'No app source writes MagnetInfo to a Parcel, so this Parcelable hook has no app trigger.', 'SRC core/model/data/MagnetInfo.java:71-77; scratch/batch_029_helper_printed.txt', 'SOURCE'),
    'MagnetInfo$1.createFromParcel': ('no_trigger_in_app', 'No app Parcel transport reads MagnetInfo, so Android has no app request to invoke this Creator callback.', 'SRC core/model/data/MagnetInfo.java:79-87; scratch/batch_029_helper_printed.txt', 'SOURCE'),
    'MagnetInfo$1.newArray': ('no_trigger_in_app', 'No app Parcel transport reads MagnetInfo or requests an array from its Creator.', 'SRC core/model/data/MagnetInfo.java:79-93; scratch/batch_029_helper_printed.txt', 'SOURCE'),
})

# S4 batch 32: Torrent is passed by ID; app source does not parcel the entity.
UNREACHABLE.update({
    'Torrent.writeToParcel': ('no_trigger_in_app', 'App intents pass Torrent IDs and no app source writes a Torrent Parcelable.', 'SRC core/model/data/entity/Torrent.java:142-170; scratch/batch_032_helper_printed.txt', 'SOURCE'),
    'Torrent$1.createFromParcel': ('no_trigger_in_app', 'The Creator is declared, but the app has no Parcel transport that reads Torrent entities.', 'SRC core/model/data/entity/Torrent.java:157-170; scratch/batch_032_helper_printed.txt', 'SOURCE'),
    'Torrent$1.newArray': ('no_trigger_in_app', 'No app Parcel path requests a Torrent Creator array.', 'SRC core/model/data/entity/Torrent.java:157-170; scratch/batch_032_helper_printed.txt', 'SOURCE'),
})


# S4 batches 3-4: TagInfo.hashCode and UriConverter.<init> have no app caller (evidence in scratch/batch_003_004_printed.txt and scratch/batch_003_hash_callers.txt).
UNREACHABLE.update({
    'TagInfo.hashCode': ('no_trigger_in_app', 'No app code hashes a TagInfo: no hash-based collection in app source holds TagInfo, TagItem or TorrentInfo, so the hashCode overrides are not reached from app code.', 'SRC core/model/data/entity/TagInfo.java:94-99; SRC ui/tag/TagItem.java:49-51; SRC ui/main/drawer/TagItem.java:50-51; SRC core/model/data/TorrentInfo.java:191-210; scratch/batch_003_hash_callers.txt', 'SOURCE'),
    'UriConverter.<init>': ('no_trigger_in_app', 'UriConverter has only static @TypeConverter methods and app source never constructs it; AppDatabase names the class only in @TypeConverters, which Room uses through the static methods.', 'SRC core/storage/converter/UriConverter.java:27-40; SRC core/storage/AppDatabase.java:53; scratch/batch_003_004_printed.txt; scratch/batch_003_004_evidence.txt', 'INFERRED'),
})

# S4 batches 5-9 (200 methods): generated data-binding statics XBinding.inflate and XBinding.bind.
# The app creates these layouts through DataBindingUtil or a layout include, never through these statics (scratch/generated_class_grep_batch5_9.txt).
_NO_BINDING_STATIC = 'No app source calls this generated static method; the layout is created through DataBindingUtil or a layout include.'
UNREACHABLE.update({
    'ActivityAddTorrentBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityAddTorrentBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityAddTorrentBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityAddTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityAddTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityAddTorrentBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityFilemanagerDialogBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityFilemanagerDialogBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityFilemanagerDialogBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityFilemanagerDialogBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityFilemanagerDialogBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityFilemanagerDialogBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityLogBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityLogBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityLogBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityLogBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityLogBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ActivityLogBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'AddTorrentInfoBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'AddTorrentInfoBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'AddTorrentInfoBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'AddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'AddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'AddTorrentInfoBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DetailTorrentAppbarBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DetailTorrentAppbarBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DetailTorrentAppbarBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DetailTorrentAppbarBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DetailTorrentAppbarBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DetailTorrentAppbarBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddFeedChannelBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddFeedChannelBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddFeedChannelBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddFeedChannelBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddFeedChannelBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddFeedChannelBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddLinkBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddLinkBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddLinkBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddLinkBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddLinkBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddLinkBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddTagBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddTagBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddTagBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddTagBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddTagBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogAddTagBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogCreateTorrentBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogCreateTorrentBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogCreateTorrentBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogCreateTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogCreateTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogCreateTorrentBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogErrorBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogErrorBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogErrorBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogErrorBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogErrorBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogErrorBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogGoToFolderBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogGoToFolderBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogGoToFolderBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogGoToFolderBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogGoToFolderBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogGoToFolderBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogLogFilterBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogLogFilterBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogLogFilterBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogLogFilterBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogLogFilterBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogLogFilterBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogSelectTagBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogSelectTagBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogSelectTagBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogSelectTagBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogSelectTagBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DialogSelectTagBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerEmptyTagsListItemBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerEmptyTagsListItemBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerEmptyTagsListItemBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerNoTagsListItemBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerNoTagsListItemBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerNoTagsListItemBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerNoTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerNoTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerNoTagsListItemBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerTagsListItemBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerTagsListItemBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerTagsListItemBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'DrawerTagsListItemBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentFilesBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentFilesBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentFilesBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentFilesBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentInfoBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentInfoBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentInfoBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentAddTorrentInfoBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentFilesBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentFilesBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentFilesBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentInfoBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentInfoBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentInfoBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentInfoBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPeerListBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPeerListBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPiecesBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPiecesBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentStateBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentStateBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentStateBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentStateBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentStateBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentStateBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentTrackerListBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentTrackerListBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedItemsBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedItemsBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedItemsBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedItemsBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedItemsBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentFeedItemsBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentMainBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentMainBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentMainBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentMainBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentMainBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'FragmentMainBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedChannelListBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedChannelListBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedChannelListBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedChannelListBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedChannelListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedChannelListBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedItemsListBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedItemsListBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedItemsListBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedItemsListBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedItemsListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemFeedItemsListBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemLogListBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemLogListBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemLogListBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemLogListBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemLogListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemLogListBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemPeersListBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemPeersListBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemPeersListBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemPeersListBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemPeersListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemPeersListBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemTorrentContentFileBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemTorrentContentFileBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemTorrentContentFileBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemTorrentContentFileBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemTorrentContentFileBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemTorrentContentFileBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemTorrentDownloadableFileBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
    'ItemTorrentDownloadableFileBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC scratch/generated_class_grep_batch5_9.txt (grep command A: no XBinding static call)', 'INFERRED'),
})

# S4 batches 3-9: these bytecode edges leave UNREACHABLE callers (generated XBinding overloads, grep in scratch/generated_class_grep_batch5_9.txt;
# tag.TagItem.hashCode, ui/tag/TagItem.java:49-51). Removing them does not change any route.
SUPPRESS.update({
    ('ActivityAddTorrentBinding.bind(View)', 'ActivityAddTorrentBinding.bind(View,Object)'),
    ('ActivityAddTorrentBinding.inflate(LayoutInflater)', 'ActivityAddTorrentBinding.inflate(LayoutInflater,Object)'),
    ('ActivityAddTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ActivityAddTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('ActivityFilemanagerDialogBinding.bind(View)', 'ActivityFilemanagerDialogBinding.bind(View,Object)'),
    ('ActivityFilemanagerDialogBinding.inflate(LayoutInflater)', 'ActivityFilemanagerDialogBinding.inflate(LayoutInflater,Object)'),
    ('ActivityFilemanagerDialogBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ActivityFilemanagerDialogBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('ActivityLogBinding.bind(View)', 'ActivityLogBinding.bind(View,Object)'),
    ('ActivityLogBinding.inflate(LayoutInflater)', 'ActivityLogBinding.inflate(LayoutInflater,Object)'),
    ('ActivityLogBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ActivityLogBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('AddTorrentInfoBinding.bind(View)', 'AddTorrentInfoBinding.bind(View,Object)'),
    ('AddTorrentInfoBinding.inflate(LayoutInflater)', 'AddTorrentInfoBinding.inflate(LayoutInflater,Object)'),
    ('AddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'AddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DetailTorrentAppbarBinding.bind(View)', 'DetailTorrentAppbarBinding.bind(View,Object)'),
    ('DetailTorrentAppbarBinding.inflate(LayoutInflater)', 'DetailTorrentAppbarBinding.inflate(LayoutInflater,Object)'),
    ('DetailTorrentAppbarBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DetailTorrentAppbarBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DialogAddFeedChannelBinding.bind(View)', 'DialogAddFeedChannelBinding.bind(View,Object)'),
    ('DialogAddFeedChannelBinding.inflate(LayoutInflater)', 'DialogAddFeedChannelBinding.inflate(LayoutInflater,Object)'),
    ('DialogAddFeedChannelBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DialogAddFeedChannelBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DialogAddLinkBinding.bind(View)', 'DialogAddLinkBinding.bind(View,Object)'),
    ('DialogAddLinkBinding.inflate(LayoutInflater)', 'DialogAddLinkBinding.inflate(LayoutInflater,Object)'),
    ('DialogAddLinkBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DialogAddLinkBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DialogAddTagBinding.bind(View)', 'DialogAddTagBinding.bind(View,Object)'),
    ('DialogAddTagBinding.inflate(LayoutInflater)', 'DialogAddTagBinding.inflate(LayoutInflater,Object)'),
    ('DialogAddTagBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DialogAddTagBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DialogCreateTorrentBinding.bind(View)', 'DialogCreateTorrentBinding.bind(View,Object)'),
    ('DialogCreateTorrentBinding.inflate(LayoutInflater)', 'DialogCreateTorrentBinding.inflate(LayoutInflater,Object)'),
    ('DialogCreateTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DialogCreateTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DialogErrorBinding.bind(View)', 'DialogErrorBinding.bind(View,Object)'),
    ('DialogErrorBinding.inflate(LayoutInflater)', 'DialogErrorBinding.inflate(LayoutInflater,Object)'),
    ('DialogErrorBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DialogErrorBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DialogGoToFolderBinding.bind(View)', 'DialogGoToFolderBinding.bind(View,Object)'),
    ('DialogGoToFolderBinding.inflate(LayoutInflater)', 'DialogGoToFolderBinding.inflate(LayoutInflater,Object)'),
    ('DialogGoToFolderBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DialogGoToFolderBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DialogLogFilterBinding.bind(View)', 'DialogLogFilterBinding.bind(View,Object)'),
    ('DialogLogFilterBinding.inflate(LayoutInflater)', 'DialogLogFilterBinding.inflate(LayoutInflater,Object)'),
    ('DialogLogFilterBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DialogLogFilterBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DialogSelectTagBinding.bind(View)', 'DialogSelectTagBinding.bind(View,Object)'),
    ('DialogSelectTagBinding.inflate(LayoutInflater)', 'DialogSelectTagBinding.inflate(LayoutInflater,Object)'),
    ('DialogSelectTagBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DialogSelectTagBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DrawerEmptyTagsListItemBinding.bind(View)', 'DrawerEmptyTagsListItemBinding.bind(View,Object)'),
    ('DrawerEmptyTagsListItemBinding.inflate(LayoutInflater)', 'DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,Object)'),
    ('DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DrawerEmptyTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DrawerNoTagsListItemBinding.bind(View)', 'DrawerNoTagsListItemBinding.bind(View,Object)'),
    ('DrawerNoTagsListItemBinding.inflate(LayoutInflater)', 'DrawerNoTagsListItemBinding.inflate(LayoutInflater,Object)'),
    ('DrawerNoTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DrawerNoTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DrawerTagsListItemBinding.bind(View)', 'DrawerTagsListItemBinding.bind(View,Object)'),
    ('DrawerTagsListItemBinding.inflate(LayoutInflater)', 'DrawerTagsListItemBinding.inflate(LayoutInflater,Object)'),
    ('DrawerTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DrawerTagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FileSystemFacadeImpl.lastModified', 'DefaultFsModule.lastModified'),
    ('FileSystemFacadeImpl.lastModified', 'SafFsModule.lastModified'),
    ('FragmentAddTorrentFilesBinding.bind(View)', 'FragmentAddTorrentFilesBinding.bind(View,Object)'),
    ('FragmentAddTorrentFilesBinding.inflate(LayoutInflater)', 'FragmentAddTorrentFilesBinding.inflate(LayoutInflater,Object)'),
    ('FragmentAddTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentAddTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentAddTorrentInfoBinding.bind(View)', 'FragmentAddTorrentInfoBinding.bind(View,Object)'),
    ('FragmentAddTorrentInfoBinding.inflate(LayoutInflater)', 'FragmentAddTorrentInfoBinding.inflate(LayoutInflater,Object)'),
    ('FragmentAddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentAddTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentDetailTorrentBinding.bind(View)', 'FragmentDetailTorrentBinding.bind(View,Object)'),
    ('FragmentDetailTorrentBinding.inflate(LayoutInflater)', 'FragmentDetailTorrentBinding.inflate(LayoutInflater,Object)'),
    ('FragmentDetailTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentDetailTorrentBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentDetailTorrentFilesBinding.bind(View)', 'FragmentDetailTorrentFilesBinding.bind(View,Object)'),
    ('FragmentDetailTorrentFilesBinding.inflate(LayoutInflater)', 'FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,Object)'),
    ('FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentDetailTorrentFilesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentDetailTorrentInfoBinding.bind(View)', 'FragmentDetailTorrentInfoBinding.bind(View,Object)'),
    ('FragmentDetailTorrentInfoBinding.inflate(LayoutInflater)', 'FragmentDetailTorrentInfoBinding.inflate(LayoutInflater,Object)'),
    ('FragmentDetailTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentDetailTorrentInfoBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentDetailTorrentPeerListBinding.bind(View)', 'FragmentDetailTorrentPeerListBinding.bind(View,Object)'),
    ('FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater)', 'FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater,Object)'),
    ('FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentDetailTorrentPeerListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentDetailTorrentPiecesBinding.bind(View)', 'FragmentDetailTorrentPiecesBinding.bind(View,Object)'),
    ('FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater)', 'FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater,Object)'),
    ('FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentDetailTorrentPiecesBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentDetailTorrentStateBinding.bind(View)', 'FragmentDetailTorrentStateBinding.bind(View,Object)'),
    ('FragmentDetailTorrentStateBinding.inflate(LayoutInflater)', 'FragmentDetailTorrentStateBinding.inflate(LayoutInflater,Object)'),
    ('FragmentDetailTorrentStateBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentDetailTorrentStateBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentDetailTorrentTrackerListBinding.bind(View)', 'FragmentDetailTorrentTrackerListBinding.bind(View,Object)'),
    ('FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater)', 'FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater,Object)'),
    ('FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentDetailTorrentTrackerListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentFeedBinding.bind(View)', 'FragmentFeedBinding.bind(View,Object)'),
    ('FragmentFeedBinding.inflate(LayoutInflater)', 'FragmentFeedBinding.inflate(LayoutInflater,Object)'),
    ('FragmentFeedBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentFeedBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentFeedItemsBinding.bind(View)', 'FragmentFeedItemsBinding.bind(View,Object)'),
    ('FragmentFeedItemsBinding.inflate(LayoutInflater)', 'FragmentFeedItemsBinding.inflate(LayoutInflater,Object)'),
    ('FragmentFeedItemsBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentFeedItemsBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('FragmentMainBinding.bind(View)', 'FragmentMainBinding.bind(View,Object)'),
    ('FragmentMainBinding.inflate(LayoutInflater)', 'FragmentMainBinding.inflate(LayoutInflater,Object)'),
    ('FragmentMainBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'FragmentMainBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('ItemFeedChannelListBinding.bind(View)', 'ItemFeedChannelListBinding.bind(View,Object)'),
    ('ItemFeedChannelListBinding.inflate(LayoutInflater)', 'ItemFeedChannelListBinding.inflate(LayoutInflater,Object)'),
    ('ItemFeedChannelListBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemFeedChannelListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('ItemFeedItemsListBinding.bind(View)', 'ItemFeedItemsListBinding.bind(View,Object)'),
    ('ItemFeedItemsListBinding.inflate(LayoutInflater)', 'ItemFeedItemsListBinding.inflate(LayoutInflater,Object)'),
    ('ItemFeedItemsListBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemFeedItemsListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('ItemLogListBinding.bind(View)', 'ItemLogListBinding.bind(View,Object)'),
    ('ItemLogListBinding.inflate(LayoutInflater)', 'ItemLogListBinding.inflate(LayoutInflater,Object)'),
    ('ItemLogListBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemLogListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('ItemPeersListBinding.bind(View)', 'ItemPeersListBinding.bind(View,Object)'),
    ('ItemPeersListBinding.inflate(LayoutInflater)', 'ItemPeersListBinding.inflate(LayoutInflater,Object)'),
    ('ItemPeersListBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemPeersListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('ItemTorrentContentFileBinding.bind(View)', 'ItemTorrentContentFileBinding.bind(View,Object)'),
    ('ItemTorrentContentFileBinding.inflate(LayoutInflater)', 'ItemTorrentContentFileBinding.inflate(LayoutInflater,Object)'),
    ('ItemTorrentContentFileBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemTorrentContentFileBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('ItemTorrentDownloadableFileBinding.bind(View)', 'ItemTorrentDownloadableFileBinding.bind(View,Object)'),
    ('SafFileSystem.openFD(FakePath,String)', 'SafFileSystem.openFD(Uri,String)'),
    ('SafFileSystem.openFD(Uri,String,String)', 'SafFileSystem.openFD(Uri,String)'),
    ('TorrentRepositoryImpl.getTorrentDataDir', 'TorrentRepositoryImpl.makeTorrentDataDir'),
    ('TorrentRepositoryImpl.makeTorrentDataDir', 'FileSystemFacadeImpl.isStorageWritable'),
    ('tag.TagItem.hashCode', 'TagInfo.hashCode'),
})

# S4 batch 10
UNREACHABLE.update({
    'drawer.TagItem.hashCode': ('no_trigger_in_app', 'The drawer tag list is a ListAdapter that compares items with isSame and equals through DiffUtil, and the list is built with toList, so no app code hashes a drawer TagItem and this override is not reached.', 'SRC ui/main/drawer/TagItem.java:50-51; SRC ui/main/drawer/TagsAdapter.java:130-146; SRC ui/main/MainActivity.java:474-485; scratch/batch_010_drawer_tagitem_evidence.txt', 'SOURCE'),
})
# drawer.TagItem.hashCode, ui/main/drawer/TagItem.java:50-51, has the same bytecode edge into TagInfo.hashCode as tag.TagItem.hashCode.
SUPPRESS.update({
    ('drawer.TagItem.hashCode', 'TagInfo.hashCode'),
})

# S4 batches 10 and 11 (39 methods)
_NO_CONTEXT_ONLY_VIEW = 'The XML layout invokes the Context,AttributeSet constructor; no app source constructs the Context-only overload.'
_NO_CONTEXT_ONLY_PREF = 'The preference XML invokes the Context,AttributeSet constructor through androidx PreferenceInflater; no app source constructs the Context-only overload.'
_NO_SPINNER_ACCESSOR = 'No app code calls this StorageSpinnerItem accessor; the spinner adapter reads name and size as fields and uses getStoragePath only.'
_NO_SPINNER_SETTER = 'No app code calls this StorageSpinnerItem setter; the spinner adapter only reads items.'
_BINDING_BATCH10 = 'scratch/batch_010_011_evidence.txt (grep A: DataBindingUtil.inflate only; no XBinding static call)'
UNREACHABLE.update({
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/addtorrent/DownloadableFilesAdapter.java:60; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/addtorrent/DownloadableFilesAdapter.java:60; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/addtorrent/DownloadableFilesAdapter.java:60; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/addtorrent/DownloadableFilesAdapter.java:60; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTorrentListBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/main/TorrentListAdapter.java:79; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTorrentListBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/main/TorrentListAdapter.java:79; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTorrentListBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/main/TorrentListAdapter.java:79; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/main/TorrentListAdapter.java:79; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/main/TorrentListAdapter.java:79; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTorrentListBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/main/TorrentListAdapter.java:79; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTrackersListBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTrackersListBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTrackersListBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; ' + _BINDING_BATCH10, 'INFERRED'),
    'ItemTrackersListBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; ' + _BINDING_BATCH10, 'INFERRED'),
    'TagsListItemBinding.bind(View)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/tag/TagsAdapter.java:48; ' + _BINDING_BATCH10, 'INFERRED'),
    'TagsListItemBinding.bind(View,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/tag/TagsAdapter.java:48; ' + _BINDING_BATCH10, 'INFERRED'),
    'TagsListItemBinding.inflate(LayoutInflater)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/tag/TagsAdapter.java:48; ' + _BINDING_BATCH10, 'INFERRED'),
    'TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/tag/TagsAdapter.java:48; ' + _BINDING_BATCH10, 'INFERRED'),
    'TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/tag/TagsAdapter.java:48; ' + _BINDING_BATCH10, 'INFERRED'),
    'TagsListItemBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app', _NO_BINDING_STATIC, 'SRC ui/tag/TagsAdapter.java:48; ' + _BINDING_BATCH10, 'INFERRED'),
    'EmptyRecyclerView.<init>(Context)': ('no_trigger_in_app', _NO_CONTEXT_ONLY_VIEW, 'SRC ui/customviews/EmptyRecyclerView.java:54-58; res/layout/fragment_main.xml:10; FW-SRC core/java/android/view/LayoutInflater.java:90-91,615,645-647', 'SOURCE'),
    'ExpansionHeader.<init>(Context)': ('no_trigger_in_app', _NO_CONTEXT_ONLY_VIEW, 'SRC ui/customviews/ExpansionHeader.java:56-58; res/layout/drawer_group_header.xml:2; FW-SRC core/java/android/view/LayoutInflater.java:90-91,615,645-647', 'SOURCE'),
    'FixHintTextInputEditText.<init>(Context)': ('no_trigger_in_app', _NO_CONTEXT_ONLY_VIEW, 'SRC ui/customviews/FixHintTextInputEditText.java:35-37; res/layout/dialog_create_torrent.xml:143; FW-SRC core/java/android/view/LayoutInflater.java:90-91,615,645-647', 'SOURCE'),
    'SwitchBar.<init>(Context)': ('no_trigger_in_app', _NO_CONTEXT_ONLY_VIEW, 'SRC ui/customviews/SwitchBar.java:37-41; res/layout/preference_switchbar.xml:6; FW-SRC core/java/android/view/LayoutInflater.java:90-91,615,645-647', 'SOURCE'),
    'ThemedSpeedDialView.<init>(Context)': ('no_trigger_in_app', _NO_CONTEXT_ONLY_VIEW, 'SRC ui/customviews/ThemedSpeedDialView.java:35-38; res/layout/fragment_main.xml:33; FW-SRC core/java/android/view/LayoutInflater.java:90-91,615,645-647', 'SOURCE'),
    'SummaryPreference.<init>(Context)': ('no_trigger_in_app', _NO_CONTEXT_ONLY_PREF, 'SRC ui/settings/customprefs/SummaryPreference.java:39-42; res/xml/pref_anonymous_mode.xml:8; androidx.preference not in fw_src', 'INFERRED'),
    'SwitchBarPreference.<init>(Context)': ('no_trigger_in_app', _NO_CONTEXT_ONLY_PREF, 'SRC ui/settings/customprefs/SwitchBarPreference.java:40-43; res/xml/pref_anonymous_mode.xml:3; androidx.preference not in fw_src', 'INFERRED'),
    'TimePreference.<init>(Context)': ('no_trigger_in_app', _NO_CONTEXT_ONLY_PREF, 'SRC ui/settings/customprefs/TimePreference.java:32-35; res/xml/pref_scheduling.xml:11,26; androidx.preference not in fw_src', 'INFERRED'),
    'PeerItem.hashCode': ('no_trigger_in_app', 'PeerListAdapter compares items with equals through DiffUtil, and no hash-based collection holds PeerItem.', 'SRC ui/detailtorrent/pages/peers/PeerItem.java:36-39; ui/detailtorrent/pages/peers/PeerListAdapter.java:110-113; scratch/batch_010_011_evidence.txt (grep D)', 'SOURCE'),
    'FeedItemsListItem.hashCode': ('no_trigger_in_app', 'FeedItemsAdapter compares items with equals through DiffUtil, and no hash-based collection holds FeedItemsListItem.', 'SRC ui/feeditems/FeedItemsListItem.java:38-41; ui/feeditems/FeedItemsAdapter.java:115-118; scratch/batch_010_011_evidence.txt (grep D)', 'SOURCE'),
    'FileManagerSpinnerAdapter$StorageSpinnerItem.getName': ('no_trigger_in_app', _NO_SPINNER_ACCESSOR, 'SRC ui/filemanager/FileManagerSpinnerAdapter.java:64-67,148-149; scratch/batch_010_011_evidence.txt (grep E)', 'SOURCE'),
    'FileManagerSpinnerAdapter$StorageSpinnerItem.getSize': ('no_trigger_in_app', _NO_SPINNER_ACCESSOR, 'SRC ui/filemanager/FileManagerSpinnerAdapter.java:84-87,148-149; scratch/batch_010_011_evidence.txt (grep E)', 'SOURCE'),
    'FileManagerSpinnerAdapter$StorageSpinnerItem.setName': ('no_trigger_in_app', _NO_SPINNER_SETTER, 'SRC ui/filemanager/FileManagerSpinnerAdapter.java:69-72; scratch/batch_010_011_evidence.txt (grep E)', 'SOURCE'),
    'FileManagerSpinnerAdapter$StorageSpinnerItem.setSize': ('no_trigger_in_app', _NO_SPINNER_SETTER, 'SRC ui/filemanager/FileManagerSpinnerAdapter.java:89-92; scratch/batch_010_011_evidence.txt (grep E)', 'SOURCE'),
    'FileManagerSpinnerAdapter$StorageSpinnerItem.setStoragePath': ('no_trigger_in_app', _NO_SPINNER_SETTER, 'SRC ui/filemanager/FileManagerSpinnerAdapter.java:79-82; scratch/batch_010_011_evidence.txt (grep E: definition only)', 'SOURCE'),
    'drawer.TagItem.toString': ('no_trigger_in_app', 'No string conversion or formatting of a drawer TagItem appears in app source; the adapter concatenates only in the unknown-type branch.', 'SRC ui/main/drawer/TagItem.java:56-57; ui/main/drawer/TagsAdapter.java:105-114; scratch/batch_010_011_evidence.txt (grep D)', 'SOURCE'),
})

e('FeedItemsFragment.subscribeAdapter', 'FeedItemsFragment.observeFeedItems', 'CALL', 'Subscribe to the feed item list for the adapter',
  cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:205')
e('FeedItemsFragment.observeFeedItems', 'FeedItemsAdapter.submitList', 'REGISTER', 'Register the adapter update as the feed item subscriber',
  cls='explicit', evidence='SRC ui/feeditems/FeedItemsFragment.java:218')
e('FeedItemsFragment.observeFeedItems', 'FeedItemsAdapter.submitList', 'FRAMEWORK', 'Deliver each emitted feed item list to the adapter on the main thread',
  cls='non_standard', via='RxJava Consumer dispatch', evidence='SRC ui/feeditems/FeedItemsFragment.java:217-218; INFERRED RxJava subscribe dispatch')
e('FeedItemsAdapter.submitList', 'FeedItemsListItem.compareTo', 'CALL', 'Sort submitted feed items by publication date',
  guard='list != null and list.size() >= 2', cls='non_standard', via='java.util.Collections.sort Comparable callback',
  evidence='SRC ui/feeditems/FeedItemsAdapter.java:84-85; ui/feeditems/FeedItemsListItem.java:44-47; INFERRED JDK sort calls compareTo only for two or more elements')
e('FeedItemsFragment.newInstance', 'FeedItemsFragment.onAttach', 'LIFECYCLE', 'Attach feed items fragment when FragmentManager shows it',
  cls='non_standard', via='AndroidX FragmentManager lifecycle', evidence='INFERRED AndroidX Fragment lifecycle dispatch; SRC ui/feeditems/FeedItemsFragment.java:80-87,99-104')
e('FeedActivity.subscribeMsgViewModel', 'FeedActivity.showFeedItems', 'FRAMEWORK', 'Deliver feed-items-opened message to the open-feed handler',
  cls='non_standard', via='RxJava Consumer dispatch', evidence='SRC ui/feeds/FeedActivity.java:174-176; INFERRED RxJava subscribe dispatch')
# generated overload calls between two UNREACHABLE binding statics (bytecode CALL edges)
SUPPRESS.update({
    ('ItemTorrentDownloadableFileBinding.inflate(LayoutInflater)', 'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,Object)'),
    ('ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('ItemTorrentListBinding.bind(View)', 'ItemTorrentListBinding.bind(View,Object)'),
    ('ItemTorrentListBinding.inflate(LayoutInflater)', 'ItemTorrentListBinding.inflate(LayoutInflater,Object)'),
    ('ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('ItemTrackersListBinding.bind(View)', 'ItemTrackersListBinding.bind(View,Object)'),
    ('ItemTrackersListBinding.inflate(LayoutInflater)', 'ItemTrackersListBinding.inflate(LayoutInflater,Object)'),
    ('ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('TagsListItemBinding.bind(View)', 'TagsListItemBinding.bind(View,Object)'),
    ('TagsListItemBinding.inflate(LayoutInflater)', 'TagsListItemBinding.inflate(LayoutInflater,Object)'),
    ('TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
})
# generated BaseItem.equals copies calling the UNREACHABLE FeedUtils.equalsOrNull
SUPPRESS.update({
    ('BaseItem.equals', 'FeedUtils.equalsOrNull'),
    ('BaseItem.equals@AtomItem', 'FeedUtils.equalsOrNull'),
    ('BaseItem.equals@Rss1Item', 'FeedUtils.equalsOrNull'),
    ('BaseItem.equals@Rss2Item', 'FeedUtils.equalsOrNull'),
})

# ---- part: batch 14 (parts/b014.py; printed evidence scratch/b014_printed.txt)
# Batch 14 part (com.ernieyu.feedparser impl and mediarss: Rss1Feed, Rss2Feed,
# Rss1Item, Rss2Item, MediaRssParser, Content, Hash). Hand-written edges and
# UNREACHABLE entries only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b014_printed.txt.
#
# Route steps owned by other batches are written here so that the routes of
# batch-14 methods are complete: FeedParser.findDownloadUrl -> watchMediaContent
# and watchGuid, FeedParser.watchMediaContent -> watchMediaHash. If another part
# writes the same edge, the merge keeps one copy.

# FeedHandler creates the RSS feed roots (impl/FeedHandler.java:60-62, 67-69).
e('FeedHandler.startElement', 'Rss1Feed.<init>', 'CALL', 'Create an RSS 1.0 feed for the RDF root element',
  guard='localName equals RDF', cls='explicit', evidence='SRC impl/FeedHandler.java:60-62')
e('FeedHandler.startElement', 'Rss2Feed.<init>', 'CALL', 'Create an RSS 2.0 feed for the rss root element',
  guard='localName equals RSS', cls='explicit', evidence='SRC impl/FeedHandler.java:67-69')

# core/FeedParser.getItems reads item accessors (core/FeedParser.java:95-110).
e('FeedParser.getItems', 'Rss1Item.getLinks', 'CALL', 'Read RSS 1.0 item links',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:95-96; impl/Rss1Item.java:45-52')
e('FeedParser.getItems', 'Rss2Item.getLinks', 'CALL', 'Read RSS 2.0 item links',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:95-96; impl/Rss2Item.java:46-54')
e('FeedParser.getItems', 'Rss1Item.getTitle', 'CALL', 'Read RSS 1.0 item title',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:110; impl/Rss1Item.java:39-42')
e('FeedParser.getItems', 'Rss2Item.getTitle', 'CALL', 'Read RSS 2.0 item title',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:110; impl/Rss2Item.java:40-43')

# findDownloadUrl checks the remaining sources in order (core/FeedParser.java:147-160).
e('FeedParser.findDownloadUrl', 'FeedParser.watchMediaContent', 'CALL', 'Check media:content entries when no enclosure or EzRSS hash matched',
  guard='watchEnclosure and watchTorrentInfoHash returned null', cls='explicit', evidence='SRC core/FeedParser.java:155-157')
e('FeedParser.findDownloadUrl', 'FeedParser.watchGuid', 'CALL', 'Use the item guid when no earlier source matched',
  guard='watchMediaContent returned null', cls='explicit', evidence='SRC core/FeedParser.java:159-160')
e('FeedParser.watchTorrentInfoHash', 'Rss1Item.getEzRssTorrentItem', 'CALL', 'Read EzRSS metadata from an RSS 1.0 item',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:238; impl/Rss1Item.java:120-123')

# watchMediaContent and the media:hash fallback (core/FeedParser.java:188-229).
e('FeedParser.watchMediaContent', 'Rss1Item.getMediaRss', 'CALL', 'Read the media RSS block of an RSS 1.0 item',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:190; impl/Rss1Item.java:111-114')
e('FeedParser.watchMediaContent', 'Rss2Item.getMediaRss', 'CALL', 'Parse the media RSS block of an RSS 2.0 item',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:190; impl/Rss2Item.java:113-116')
e('FeedParser.watchMediaContent', 'Content.getUrl', 'CALL', 'Read the URL of a media:content entry',
  guard='content is not null', cls='explicit', evidence='SRC core/FeedParser.java:195-199; mediarss/Content.java:48-50')
e('FeedParser.watchMediaContent', 'Content.getType', 'CALL', 'Read the MIME type of a media:content entry that has a URL',
  guard='content URL is not null', cls='explicit', evidence='SRC core/FeedParser.java:200-202; mediarss/Content.java:59-61')
e('FeedParser.watchMediaContent', 'FeedParser.watchMediaHash', 'CALL', 'Check the media:hash fallback when a URL is null or no content matched',
  guard='content URL is null, or the content list ends without a match', cls='explicit', evidence='SRC core/FeedParser.java:200-201,207')
e('FeedParser.watchMediaHash', 'Hash.getAlgorithm', 'CALL', 'Read the algorithm of a media:hash value',
  guard='hash value is not null', cls='explicit', evidence='SRC core/FeedParser.java:217-224; mediarss/Hash.java:44-46')

# watchGuid reads the guid of the item (core/FeedParser.java:254-260).
e('FeedParser.watchGuid', 'Rss1Item.getGuid', 'CALL', 'Read the RSS 1.0 item identifier used as a fallback URL',
  cls='non_standard', via='Item interface dispatch to Rss1Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:256; impl/Rss1Item.java:69-72')
e('FeedParser.watchGuid', 'Rss2Item.getGuid', 'CALL', 'Read the RSS 2.0 item guid used as a fallback URL',
  cls='non_standard', via='Item interface dispatch to Rss2Item', evidence='INFERRED interface dispatch; SRC core/FeedParser.java:256; impl/Rss2Item.java:69-72')

# Rss2Item.getMediaRss runs the Media RSS parser (impl/Rss2Item.java:113-116).
e('Rss2Item.getMediaRss', 'MediaRssParser.<init>', 'CALL', 'Create the Media RSS parser bound to this item',
  cls='explicit', evidence='SRC impl/Rss2Item.java:115; impl/MediaRssParser.java:25-27')
e('Rss2Item.getMediaRss', 'MediaRssParser.parse', 'CALL', 'Parse the media:* elements of this item',
  cls='explicit', evidence='SRC impl/Rss2Item.java:115; impl/MediaRssParser.java:29-38')
e('MediaRssParser.parse', 'MediaRssParser.<init>', 'CALL', 'Create a parser bound to the item',
  cls='explicit', evidence='SRC impl/MediaRssParser.java:31; impl/MediaRssParser.java:25-27')
e('MediaRssParser.parse', 'MediaRssParser.parseContent', 'CALL', 'Parse media:content entries',
  cls='explicit', evidence='SRC impl/MediaRssParser.java:33; impl/MediaRssParser.java:40-56')
e('MediaRssParser.parse', 'MediaRssParser.parseHash', 'CALL', 'Parse the media:hash element',
  cls='explicit', evidence='SRC impl/MediaRssParser.java:34; impl/MediaRssParser.java:58-74')
e('MediaRssParser.parse', 'MediaRssParser.parsePeerLinks', 'CALL', 'Parse media:peerLink entries',
  cls='explicit', evidence='SRC impl/MediaRssParser.java:35; impl/MediaRssParser.java:76-92')
e('MediaRssParser.parseContent', 'MediaRssParser.isMediaRssElement', 'CALL', 'Accept only media-namespace media:content elements',
  guard='each media:content element', cls='explicit', evidence='SRC impl/MediaRssParser.java:45; impl/MediaRssParser.java:94-97')
e('MediaRssParser.parseContent', 'Content.<init>', 'CALL', 'Create a Content value for each accepted media:content element',
  guard='element is in the media namespace', cls='explicit', evidence='SRC impl/MediaRssParser.java:52; mediarss/Content.java:36-39')
e('MediaRssParser.parseHash', 'MediaRssParser.isMediaRssElement', 'CALL', 'Accept the media:hash element only in the media namespace',
  guard='media:hash element found', cls='explicit', evidence='SRC impl/MediaRssParser.java:60; impl/MediaRssParser.java:94-97')
e('MediaRssParser.parseHash', 'Hash.<init>', 'CALL', 'Create a Hash value from the media:hash text',
  guard='hash text is not null', cls='explicit', evidence='SRC impl/MediaRssParser.java:68; mediarss/Hash.java:21-23')
e('MediaRssParser.parsePeerLinks', 'MediaRssParser.isMediaRssElement', 'CALL', 'Accept only media-namespace media:peerLink elements',
  guard='each media:peerLink element', cls='explicit', evidence='SRC impl/MediaRssParser.java:81; impl/MediaRssParser.java:94-97')

# UNREACHABLE: no app or feed-parser path converts these values to text or compares them.
# core/FeedParser.java keeps the Feed in one field and reads only getTitle and getItemList.
_B14_FEED_TEXT = 'No app or feed-parser path converts this Feed to text: core/FeedParser.java keeps the feed in one field and reads only getTitle and getItemList.'
_B14_ITEM_DESCRIPTION = 'Its only caller is BaseItem.getUniqueId, which runs only from BaseItem.equals and hashCode; no app or feed-parser code compares or hashes Item values, and core/FeedParser.java never reads the description.'
_B14_MEDIA_VALUE = 'Content and Hash values are only read through getters in core/FeedParser.java; no app or feed-parser code compares, hashes or converts them to text, and MediaRss has no equals.'
UNREACHABLE.update({
    'Rss1Feed.toString': ('no_trigger_in_app', _B14_FEED_TEXT, 'SRC impl/Rss1Feed.java:118-122; core/FeedParser.java:60,86,92-95', 'SOURCE'),
    'Rss2Feed.toString': ('no_trigger_in_app', _B14_FEED_TEXT, 'SRC impl/Rss2Feed.java:132-136; core/FeedParser.java:60,86,92-95', 'SOURCE'),
    'Rss1Item.getDescription': ('no_trigger_in_app', _B14_ITEM_DESCRIPTION, 'SRC impl/Rss1Item.java:56-59; impl/BaseItem.java:30-44,53-69; core/FeedParser.java:95-110', 'SOURCE'),
    'Rss2Item.getDescription': ('no_trigger_in_app', _B14_ITEM_DESCRIPTION, 'SRC impl/Rss2Item.java:57-60; impl/BaseItem.java:30-44,53-69; core/FeedParser.java:95-110', 'SOURCE'),
    'Content.equals': ('no_trigger_in_app', _B14_MEDIA_VALUE, 'SRC mediarss/Content.java:63-73; core/FeedParser.java:194-199', 'SOURCE'),
    'Content.hashCode': ('no_trigger_in_app', _B14_MEDIA_VALUE, 'SRC mediarss/Content.java:75-80; core/FeedParser.java:194-199', 'SOURCE'),
    'Content.toString': ('no_trigger_in_app', _B14_MEDIA_VALUE, 'SRC mediarss/Content.java:82-89; mediarss/MediaRss.java:44-49', 'SOURCE'),
    'Hash.equals': ('no_trigger_in_app', _B14_MEDIA_VALUE, 'SRC mediarss/Hash.java:54-64; core/FeedParser.java:217-224', 'SOURCE'),
})

# Bytecode auto edges whose caller is an UNREACHABLE batch-14 method above, or
# BaseItem.getUniqueId (its only callers are BaseItem.equals and hashCode, which
# nothing invokes; that label is owned by the BaseItem batch).
SUPPRESS.update({
    ('Rss1Feed.toString', 'Rss1Feed.getTitle'),
    ('Rss2Feed.toString', 'Rss2Feed.getTitle'),
    ('Rss1Item.getDescription', 'BaseElement.getElement'),
    ('Rss1Item.getDescription', 'BaseElement.getContent'),
    ('Rss2Item.getDescription', 'BaseElement.getElement'),
    ('Rss2Item.getDescription', 'BaseElement.getContent'),
    ('BaseItem.getUniqueId', 'Rss1Item.getDescription'),
    ('BaseItem.getUniqueId', 'Rss2Item.getDescription'),
    ('BaseItem.getUniqueId@Rss1Item', 'Rss1Item.getDescription'),
    ('BaseItem.getUniqueId@Rss2Item', 'Rss2Item.getDescription'),
})

# ---- part: batch 13 (parts/b013.py; printed evidence scratch/b013_printed.txt)
# Batch 13 part (com.ernieyu.feedparser impl: FeedHandler, BaseElement, BaseItem,
# AtomItem getters, EzRss01Parser). Hand-written edges, UNREACHABLE entries and
# SUPPRESS strings only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b013_printed.txt.
#
# Routes into batch-13 methods that already exist in graph_def.py and are not
# repeated here: FeedFetcherWorker.fetchChannel -> FeedParser.getItems (2711),
# FeedParser.getItems -> findDownloadUrl (2781), findDownloadUrl -> watchTorrentInfoHash
# (2785), -> watchGuid (3597), -> watchMediaContent (3595), watchTorrentInfoHash ->
# AtomItem.getEzRssTorrentItem (2799) and -> Rss2Item.getEzRssTorrentItem (2801),
# Rss2Item.getEzRssTorrentItem -> EzRss01Parser.<init> / parse (2805, 2807),
# getItems -> AtomItem.getPubDate (2811), FeedParser.<init> -> newParser (2715),
# newParser -> DefaultFeedParser.<init> (2717), FeedParser.<init> -> DefaultFeedParser.parse
# (2719), DefaultFeedParser.parse -> FeedHandler.<init> / startElement / endElement /
# getFeed (2723-2729), FeedHandler.startElement -> AtomItem.<init> (2767),
# watchMediaContent -> Rss2Item.getMediaRss (3605), Rss2Item.getMediaRss ->
# MediaRssParser.<init> (3623).

# SAX callbacks made by the JDK parser for parser.parse(..., handler) (impl/DefaultFeedParser.java:37).
e('DefaultFeedParser.parse', 'FeedHandler.startDocument', 'FRAMEWORK', 'SAX parser sends the start-document event to the feed handler',
  cls='non_standard', via='JDK SAX DefaultHandler callback',
  evidence='INFERRED SAX DefaultHandler callback dispatch; SRC impl/DefaultFeedParser.java:37; impl/FeedHandler.java:41-45')
e('DefaultFeedParser.parse', 'FeedHandler.characters', 'FRAMEWORK', 'SAX parser sends element text to the feed handler',
  cls='non_standard', via='JDK SAX DefaultHandler callback',
  evidence='INFERRED SAX DefaultHandler callback dispatch; SRC impl/DefaultFeedParser.java:37; impl/FeedHandler.java:36-39')
e('DefaultFeedParser.parse', 'FeedHandler.endDocument', 'FRAMEWORK', 'SAX parser sends the end-document event to the feed handler',
  cls='non_standard', via='JDK SAX DefaultHandler callback',
  evidence='INFERRED SAX DefaultHandler callback dispatch; SRC impl/DefaultFeedParser.java:37; impl/FeedHandler.java:47-51')

# FeedHandler builds the element tree (impl/FeedHandler.java:94-131).
e('FeedHandler.startElement', 'BaseElement.<init>(String,String,Attributes)', 'CALL', 'Create a generic XML element for a tag that is not a feed root, item or entry',
  guard='no earlier branch matched localName', cls='explicit',
  evidence='SRC impl/FeedHandler.java:98-100; impl/BaseElement.java:39-43')
e('FeedHandler.endElement', 'BaseElement.setContent', 'CALL', 'Store the collected text in the element that is closing',
  cls='explicit', evidence='SRC impl/FeedHandler.java:115-121; impl/BaseElement.java:68-70')
e('FeedHandler.endElement', 'BaseElement.addElement', 'CALL', 'Add the closed element to its parent element',
  guard='elementStack is not empty after the pop', cls='explicit',
  evidence='SRC impl/FeedHandler.java:124-126; impl/BaseElement.java:91-99')

# Item constructor chain (impl/AtomItem.java:30-32; impl/BaseItem.java:21-23).
e('AtomItem.<init>', 'BaseItem.<init>', 'CALL', 'Pass the entry uri, name and attributes to the item base class',
  cls='explicit', evidence='SRC impl/AtomItem.java:31; impl/BaseItem.java:21-23')
e('BaseItem.<init>', 'BaseElement.<init>(String,String,Attributes)', 'CALL', 'Pass the uri, name and attributes to the element base class',
  cls='explicit', evidence='SRC impl/BaseItem.java:22; impl/BaseElement.java:39-43')

# core/FeedParser.getItems and its watchers read Atom items through the Item interface.
e('FeedParser.getItems', 'AtomItem.getLinks', 'CALL', 'Read Atom entry links',
  guard='feed is an Atom feed', cls='non_standard', via='Item interface dispatch to AtomItem',
  evidence='INFERRED interface dispatch; SRC core/FeedParser.java:95-96; impl/AtomItem.java:46-54')
e('FeedParser.getItems', 'AtomItem.getTitle', 'CALL', 'Read the Atom entry title for the feed item',
  guard='feed is an Atom feed', cls='non_standard', via='Item interface dispatch to AtomItem',
  evidence='INFERRED interface dispatch; SRC core/FeedParser.java:110; impl/AtomItem.java:40-43')
e('FeedParser.watchGuid', 'AtomItem.getGuid', 'CALL', 'Read the Atom entry id used as a fallback URL',
  guard='feed is an Atom feed', cls='non_standard', via='Item interface dispatch to AtomItem',
  evidence='INFERRED interface dispatch; SRC core/FeedParser.java:256; impl/AtomItem.java:74-77')
e('FeedParser.watchMediaContent', 'AtomItem.getMediaRss', 'CALL', 'Read the media RSS block of an Atom entry (always null)',
  guard='feed is an Atom feed', cls='non_standard', via='Item interface dispatch to AtomItem',
  evidence='INFERRED interface dispatch; SRC core/FeedParser.java:190; impl/AtomItem.java:127-129')

# Atom getters read child elements through BaseElement (impl/AtomItem.java:41-82).
e('AtomItem.getTitle', 'BaseElement.getElement', 'CALL', 'Find the title child element',
  cls='explicit', evidence='SRC impl/AtomItem.java:41; impl/BaseElement.java:72-76')
e('AtomItem.getTitle', 'BaseElement.getContent', 'CALL', 'Read the title text',
  guard='title element is not null', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/AtomItem.java:42; impl/BaseElement.java:60-63')
e('AtomItem.getLinks', 'BaseElement.getElementList', 'CALL', 'Find all link child elements',
  cls='explicit', evidence='SRC impl/AtomItem.java:48; impl/BaseElement.java:78-81')
e('AtomItem.getLinks', 'BaseElement.getAttributes', 'CALL', 'Read the attributes of each link element',
  cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/AtomItem.java:50; impl/BaseElement.java:55-58')
e('AtomItem.getGuid', 'BaseElement.getElement', 'CALL', 'Find the id child element',
  cls='explicit', evidence='SRC impl/AtomItem.java:75; impl/BaseElement.java:72-76')
e('AtomItem.getGuid', 'BaseElement.getContent', 'CALL', 'Read the id text',
  guard='id element is not null', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/AtomItem.java:76; impl/BaseElement.java:60-63')
e('AtomItem.getPubDate', 'BaseElement.getElement', 'CALL', 'Find the updated child element',
  cls='explicit', evidence='SRC impl/AtomItem.java:81; impl/BaseElement.java:72-76')
e('AtomItem.getPubDate', 'BaseElement.getContent', 'CALL', 'Read the updated text',
  guard='updated element is not null', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/AtomItem.java:82; impl/BaseElement.java:60-63')

# EzRss01Parser.parse calls each field parser (impl/EzRss01Parser.java:26-33).
e('EzRss01Parser.parse', 'EzRss01Parser.parseFileName', 'CALL', 'Read the EzRSS file name',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:27')
e('EzRss01Parser.parse', 'EzRss01Parser.parseMagnetUri', 'CALL', 'Read the EzRSS magnet URI',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:28')
e('EzRss01Parser.parse', 'EzRss01Parser.parseInfoHash', 'CALL', 'Read the EzRSS info hash',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:29')
e('EzRss01Parser.parse', 'EzRss01Parser.parseContentLength', 'CALL', 'Read the EzRSS content length',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:30')
e('EzRss01Parser.parse', 'EzRss01Parser.parseSeeds', 'CALL', 'Read the EzRSS seed count',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:31')
e('EzRss01Parser.parse', 'EzRss01Parser.parsePeers', 'CALL', 'Read the EzRSS peer count',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:32')
e('EzRss01Parser.parse', 'EzRss01Parser.parseVerified', 'CALL', 'Read the EzRSS verified flag',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:33')

# Each field parser reads its child element from the item (impl/EzRss01Parser.java:39-103).
e('EzRss01Parser.parseFileName', 'BaseElement.getElement', 'CALL', 'Find the fileName child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:40; impl/BaseElement.java:72-76')
e('EzRss01Parser.parseMagnetUri', 'BaseElement.getElement', 'CALL', 'Find the magnetURI child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:48; impl/BaseElement.java:72-76')
e('EzRss01Parser.parseInfoHash', 'BaseElement.getElement', 'CALL', 'Find the infoHash child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:56; impl/BaseElement.java:72-76')
e('EzRss01Parser.parseContentLength', 'BaseElement.getElement', 'CALL', 'Find the contentLength child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:64; impl/BaseElement.java:72-76')
e('EzRss01Parser.parseSeeds', 'BaseElement.getElement', 'CALL', 'Find the seeds child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:80; impl/BaseElement.java:72-76')
e('EzRss01Parser.parsePeers', 'BaseElement.getElement', 'CALL', 'Find the peers child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:88; impl/BaseElement.java:72-76')
e('EzRss01Parser.parseVerified', 'BaseElement.getElement', 'CALL', 'Find the verified child element',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:96; impl/BaseElement.java:72-76')

e('EzRss01Parser.parseFileName', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the fileName element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:41; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parseMagnetUri', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the magnetURI element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:49; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parseInfoHash', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the infoHash element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:57; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parseContentLength', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the contentLength element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:65; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parseSeeds', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the seeds element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:81; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parsePeers', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the peers element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:89; impl/EzRss01Parser.java:118-121')
e('EzRss01Parser.parseVerified', 'EzRss01Parser.isEzRssElement', 'CALL', 'Accept the verified element only in the EzRSS namespace',
  guard='element is not null', cls='explicit', evidence='SRC impl/EzRss01Parser.java:97; impl/EzRss01Parser.java:118-121')

e('EzRss01Parser.parseFileName', 'BaseElement.getContent', 'CALL', 'Read the fileName text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:44; impl/BaseElement.java:60-63')
e('EzRss01Parser.parseMagnetUri', 'BaseElement.getContent', 'CALL', 'Read the magnetURI text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:52; impl/BaseElement.java:60-63')
e('EzRss01Parser.parseInfoHash', 'BaseElement.getContent', 'CALL', 'Read the infoHash text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:60; impl/BaseElement.java:60-63')
e('EzRss01Parser.parseContentLength', 'BaseElement.getContent', 'CALL', 'Read the contentLength text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:70; impl/BaseElement.java:60-63')
e('EzRss01Parser.parseSeeds', 'BaseElement.getContent', 'CALL', 'Read the seeds text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:84; impl/BaseElement.java:60-63')
e('EzRss01Parser.parsePeers', 'BaseElement.getContent', 'CALL', 'Read the peers text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:92; impl/BaseElement.java:60-63')
e('EzRss01Parser.parseVerified', 'BaseElement.getContent', 'CALL', 'Read the verified text',
  guard='element is an EzRSS element', cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:100; impl/BaseElement.java:60-63')

e('EzRss01Parser.parseSeeds', 'EzRss01Parser.parseInt', 'CALL', 'Convert the seeds text to an integer',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:84; impl/EzRss01Parser.java:105-116')
e('EzRss01Parser.parsePeers', 'EzRss01Parser.parseInt', 'CALL', 'Convert the peers text to an integer',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:92; impl/EzRss01Parser.java:105-116')
e('EzRss01Parser.parseVerified', 'EzRss01Parser.parseInt', 'CALL', 'Convert the verified text to an integer',
  cls='explicit', evidence='SRC impl/EzRss01Parser.java:100; impl/EzRss01Parser.java:105-116')

# isEzRssElement reads the namespace uri of the element (impl/EzRss01Parser.java:118-121).
e('EzRss01Parser.isEzRssElement', 'BaseElement.getUri', 'CALL', 'Read the namespace uri of the element',
  cls='non_standard', via='Element interface dispatch to BaseElement',
  evidence='INFERRED interface dispatch; SRC impl/EzRss01Parser.java:119-120; impl/BaseElement.java:45-48')

# Items with no trigger in the app: nothing compares, hashes or converts an Item to text
# (core/FeedParser.java iterates the feed and reads accessors; the feed-parser package and
# service/FeedFetcherWorker.java have no equals, hashCode or toString use on an Item).
UNREACHABLE.update({
    'BaseItem.equals': ('no_trigger_in_app',
        'No app or feed-parser code calls equals on an Item. core/FeedParser.java only iterates getItemList() and reads accessors; its equals calls (lines 176, 203) compare Strings; FeedFetcherWorker removeIf calls (lines 193, 203) compare app FeedItem records.',
        'SRC impl/BaseItem.java:53-62; core/FeedParser.java:89-111,176,203; service/FeedFetcherWorker.java:193,203',
        'SOURCE'),
    'BaseItem.getUniqueId': ('no_trigger_in_app',
        'Private. Its only callers are BaseItem.equals and BaseItem.hashCode, and neither is invoked.',
        'SRC impl/BaseItem.java:30-44 (callers at 56-57 and 67)',
        'SOURCE'),
    'BaseItem.hashCode': ('no_trigger_in_app',
        'No app or feed-parser code hashes an Item. The only hashed collection in the package is BaseElement.elementMap with String keys, and core/FeedParser.java keeps items in a List.',
        'SRC impl/BaseItem.java:64-69; impl/BaseElement.java:23; core/FeedParser.java:95',
        'SOURCE'),
    'BaseItem.toString': ('no_trigger_in_app',
        'No app or feed-parser code converts an Item to text. No string concatenation or log call in core/FeedParser.java or the feed-parser package takes an Item value; the one concatenating log call in FeedFetcherWorker (line 255) does not use an item.',
        'SRC impl/BaseItem.java:48-50; service/FeedFetcherWorker.java:255',
        'SOURCE'),
})

# Suppress bytecode auto edges into and out of the four UNREACHABLE methods and their
# generated copies (tools/build_graph.py add_auto_edges checks src and dst against SUPPRESS).
SUPPRESS.update({
    'BaseItem.equals', 'BaseItem.equals@AtomItem', 'BaseItem.equals@Rss1Item', 'BaseItem.equals@Rss2Item',
    'BaseItem.hashCode', 'BaseItem.hashCode@AtomItem', 'BaseItem.hashCode@Rss1Item', 'BaseItem.hashCode@Rss2Item',
    'BaseItem.toString', 'BaseItem.toString@AtomItem', 'BaseItem.toString@Rss1Item', 'BaseItem.toString@Rss2Item',
    'BaseItem.getUniqueId', 'BaseItem.getUniqueId@AtomItem', 'BaseItem.getUniqueId@Rss1Item', 'BaseItem.getUniqueId@Rss2Item',
})

# ---- merged batch parts (loader added 2026-11-01; see handoff/MUSE_FINISH_ALL.md)
# Each merged batch part is its own file, parts/b<NNN>.py, run here in this namespace in the order of MERGED_PARTS.
# Batches 13 and 14 are already pasted inline above; never list them here. Append one name at a time, in plan order,
# and build after each append (C1). Keeping the parts in their own files keeps every file below the connector's 1 MB limit.
MERGED_PARTS = ['b000_trunks.py', 'b001.py', 'b002.py', 'b003.py', 'b004.py', 'b005.py', 'b006.py', 'b007.py', 'b008.py', 'b009.py', 'b010.py', 'b011.py', 'b012.py']
import os as _mp_os
for _mp_name in MERGED_PARTS:
    _mp_path = _mp_os.path.join(GDIR, 'parts', _mp_name)
    exec(compile(open(_mp_path, encoding='utf-8').read(), _mp_path, 'exec'))
del _mp_os
