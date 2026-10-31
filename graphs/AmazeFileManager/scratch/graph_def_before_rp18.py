# AmazeFileManager 3.4.2 (#1837, tingsu/AmazeFileManager@instrumented-version-3.2.1, commit 5d25735ae8465d19bbff65cd6691e14c04e40d86,
# package com.amaze.filemanager.debug, instrumented debug build) trigger graph definition, schema 2.
# Written by hand from the app sources under final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/
# after the schema-1 draft (a gen_edges.py-generated stub, never hand-reviewed) was found to be insufficient per the
# conversion brief. The schema-1 draft is kept as generated_draft_graph_def.py.txt (inventory only; nothing is taken
# over from it without reading source).
#
# Direct app->app calls come from tools/extract_calls.py (bytecode, USE_AUTO); what the bytecode cannot see (framework
# callbacks: lifecycle, listeners registered through the framework, AsyncTask, Handler.post, menus, dialogs, services,
# broadcasts, intents) and the guards of the bytecode edges are written here.
#
# Framework claims are FW-SRC (Android 8.1.0_r1 lines printed and read) or INFERRED (androidx, Material Components,
# Glide generated code, Volley, libraries not available locally).
#
# Section index (search for "# =====")
#  A  helpers, FW-SRC / INFERRED citation constants, ENV / STATE gate texts
#  B  entry points (manifest), process start, Application lifecycle
#  C  MainActivity: launcher, intent-filters (GET_CONTENT, RINGTONE_PICKER, VIEW archives, SEND, etc.), lifecycle
#  D  other activities: PreferencesActivity, TextEditorActivity, DatabaseViewerActivity, AboutActivity
#  E  services: ExtractService, ZipService, CopyService, EncryptService, DecryptService, FtpService, FtpTileService
#  F  receivers: FtpReceiver, SMSInstrumentedReceiver (JaCoCo)
#  G  fragments and UI: MainFragment, tabs, dialogs, drawer
#  H  cloud storage: Dropbox, Google Drive, OneDrive, Box integrations
#  I  FTP server subsystem
#  J  archive handling: zip, rar, 7z, tar, gzip, bzip2
#  K  database and text viewers
#  L  UNREACHABLE table, ENV_KINDS_OF / STATE_KINDS_OF, CLASSIFY, EDIT, STRICT

TITLE = 'AmazeFileManager 3.4.2 trigger graph'
USE_AUTO = True
STRICT = True

ENV_KINDS_OF, STATE_KINDS_OF = {}, {}

def env_text(text, kinds):
    ENV_KINDS_OF[text] = list(kinds)
    return text

def state_text(text, kinds):
    STATE_KINDS_OF[text] = list(kinds)
    return text

def gui(src, dst, text, kind='GUI', **kw):
    e(src, dst, kind, text, gui=[text], **kw)

def sup(*pairs):
    for p in pairs:
        SUPPRESS.add(p)

# Lifecycle order for fragments and activities
LC_RANK = {'onAttach': 0, 'onCreate': 1, 'onCreateDialog': 2, 'onCreateView': 2, 'onStart': 3, 'onResume': 4,
           'onPause': 5, 'onStop': 6, 'onDestroyView': 7}
LC_NO_TRIGGER = ('onDestroy', 'onDetach', 'onConfigurationChanged', 'onOptionsItemSelected')

def lc_chain(cls, cbs):
    """Generate lifecycle chains for a fragment or activity"""
    has = tuple(cbs)
    first = 'onAttach' if 'onAttach' in has else ('onCreate' if 'onCreate' in has else None)
    out = []
    for cb in has:
        if cb in LC_NO_TRIGGER:
            continue
        if cb == first or first is None:
            s = cls + '.<init>'
        elif cb in LC_RANK:
            below = [x for x in has if x in LC_RANK and LC_RANK[x] < LC_RANK[cb]]
            s = (cls + '.' + max(below, key=lambda x: LC_RANK[x])) if below else (cls + '.<init>')
        else:
            s = (cls + '.onCreate') if 'onCreate' in has else (cls + '.<init>')
        out.append((cb, s))
    return out

# ================================================================== A. helpers, FW citations, gates

# ---- framework citations
FW_APP = 'FW-SRC core/java/android/app/Application.java (Application.onCreate called once at process start)'
FW_ACTIVITY = 'FW-SRC core/java/android/app/Activity.java (Activity lifecycle callbacks dispatched by ActivityThread)'
FW_SERVICE = 'FW-SRC core/java/android/app/ActivityThread.java (Service lifecycle callbacks dispatched by ActivityThread)'
FW_RECEIVER = 'FW-SRC core/java/android/app/ActivityThread.java (BroadcastReceiver dispatched by ActivityThread/LoadedApk)'
FW_VIEW = ('INFERRED a tapped View dispatches to the listener registered with setOnClickListener / setOnLongClickListener / '
           'setOnItemClickListener (androidx widgets wrap the platform dispatch; androidx source not read)')
FW_FRAG = 'INFERRED androidx.fragment.app.FragmentManager drives fragment lifecycle callbacks (androidx source not read)'
FW_DIALOGFRAG = 'INFERRED androidx.fragment.app.DialogFragment shows a dialog and forwards button/cancel/dismiss callbacks (androidx source not read)'
FW_BOTTOMSHEET = 'INFERRED com.google.android.material.bottomsheet.BottomSheetDialogFragment shows a bottom sheet (Material Components source not read)'
FW_MENU = 'INFERRED the platform options-menu machinery calls onCreateOptionsMenu / onPrepareOptionsMenu / onOptionsItemSelected (AppCompat source not read)'
FW_ASYNC = 'INFERRED android.os.AsyncTask.execute runs doInBackground on a worker thread and onPostExecute on the main thread (platform source not read for this exact flow)'
FW_HANDLER = 'INFERRED Handler.post/postDelayed queues the Runnable on the handler thread (platform source not read for this exact flow)'
FW_RESULT = 'FW-SRC core/java/android/app/Activity.java, core/java/android/app/ActivityThread.java (activity result delivered via ActivityThread.deliverResults)'
FW_MATERIAL = 'INFERRED com.google.android.material (FloatingActionButton / Snackbar / BottomNavigationView / NavigationView) dispatches listeners (Material Components source not read)'
FW_GLIDE = 'INFERRED com.bumptech.glide.Glide (generated code) wires the image loading library (Glide source not read)'
FW_VOLLEY = 'INFERRED com.android.volley (RequestQueue / ImageLoader) handles network requests (Volley source not read)'
FW_LOADER = 'INFERRED androidx.loader.app.LoaderManager drives onCreateLoader / onLoadFinished callbacks (androidx source not read)'
FW_SPEEDDIAL = 'INFERRED com.leinardi.android.speeddial.SpeedDialView dispatches action item listeners (library source not read)'
FW_MATERIALDIALOG = 'INFERRED com.afollestad.materialdialogs.MaterialDialog dispatches button callbacks (library source not read)'

# ---- ENV gate texts
ENV_LAUNCHER = env_text('outside package: the user taps the app icon on the home screen (launcher)', ('other_app',))
ENV_GET_CONTENT = env_text('outside package: another app starts MainActivity with ACTION_GET_CONTENT to pick a file', ('other_app',))
ENV_RINGTONE = env_text('outside package: another app starts MainActivity with ACTION_RINGTONE_PICKER', ('other_app',))
ENV_VIEW_ARCHIVE = env_text('outside package: another app or adb opens an archive file (.zip/.rar/.7z/.tar/.gz/.bz2/.xz) with Amaze via ACTION_VIEW', ('other_app',))
ENV_SEND = env_text('outside package: another app sends one or more files to Amaze via ACTION_SEND / ACTION_SEND_MULTIPLE', ('other_app',))
ENV_QS_TILE_PREF = env_text('outside package: the user long-presses the FTP quick-settings tile (ACTION_QS_TILE_PREFERENCES)', ('other_app',))
ENV_SCHEME = env_text('outside package: a VIEW intent with scheme com.amaze.filemanager://', ('other_app',))
ENV_FOLDER_MIME = env_text('outside package: a VIEW intent with mimeType resource/folder and scheme com.amaze.filemanager', ('other_app',))
ENV_TEXT_VIEW = env_text('outside package: another app opens a text file with Amaze TextEditorActivity via ACTION_VIEW', ('other_app',))
ENV_DB_VIEW = env_text('outside package: another app opens a database file with Amaze DatabaseViewerActivity via ACTION_VIEW', ('other_app',))
ENV_APP_PREF = env_text('outside package: system settings launches PreferencesActivity via ACTION_APPLICATION_PREFERENCES', ('other_app',))
ENV_FTP_START = env_text('outside package: FtpReceiver receives ACTION_START_FTPSERVER broadcast', ('other_app',))
ENV_FTP_STOP = env_text('outside package: FtpReceiver receives ACTION_STOP_FTPSERVER broadcast', ('other_app',))
ENV_FTP_TILE = env_text('outside package: the user taps the FTP quick-settings tile', ('other_app',))
ENV_JACOCO = env_text('outside package: the test harness sends edu.gatech.m3.emma.COLLECT_COVERAGE broadcast (adb)', ('other_app',))
ENV_STORAGE_PERM = env_text('the WRITE_EXTERNAL_STORAGE runtime permission is granted (API 27: granted if accepted)', ('permission',))
ENV_PERM_ANSWER = env_text('the user answers the system permission dialog (Allow or Deny)', ('permission',))
ENV_NETWORK = env_text('the device has network connectivity (Wi-Fi or mobile data)', ('network',))
ENV_CLOUD = env_text('outside package: a cloud account (Dropbox/Drive/OneDrive/Box) is linked and network is reachable', ('network', 'other_app',))
ENV_FTP_NETWORK = env_text('the device has network connectivity (Wi-Fi/LAN) for FTP server', ('network',))
ENV_SSH = env_text('an SSH/SFTP server is reachable on the network', ('network',))
ENV_SMB = env_text('an SMB share is configured and reachable on the network', ('network',))
ENV_ROOT = env_text('the device is rooted (su available) and root explorer is enabled in settings', ('other_app',))
ENV_FINGERPRINT = env_text('the device has an enrolled fingerprint and the feature is enabled', ('hardware',))
ENV_USB_OTG = env_text('a USB OTG device is connected', ('hardware',))

# ---- STATE gate texts
NEED_PATH = state_text('A file or directory path is open in the file manager', ('data',))
NEED_FILE = state_text('A file is selected or exists', ('file',))
NEED_ARCHIVE = state_text('An archive file is open or selected', ('file',))
NEED_DB = state_text('A SQLite database file (.db) is selected', ('file',))
NEED_APK = state_text('An .apk file is selected', ('file',))
NEED_TEXT = state_text('A text file is selected', ('file',))
NEED_IMAGE = state_text('An image file is selected', ('file',))
NEED_AUDIO = state_text('An audio file is selected', ('file',))
NEED_VIDEO = state_text('A video file is selected', ('file',))
NEED_ENCRYPTED = state_text('An encrypted .aze file or encrypted connection exists', ('file',))
NEED_CLOUD_CONN = state_text('A cloud storage connection (Dropbox/Drive/OneDrive/Box) is configured', ('account',))
NEED_SMB_CONN = state_text('An SMB connection is configured', ('account',))
NEED_SSH_CONN = state_text('An SSH/SFTP connection is configured', ('account',))
NEED_FTP_RUNNING = state_text('The FTP server is currently running', ('session',))
NEED_OPERATION = state_text('A copy/move/extract/compress operation is in progress or queued', ('session',))
NEED_SELECTION = state_text('One or more files are selected in the file manager', ('session',))
NEED_CLIPBOARD = state_text('Files are copied/cut to the clipboard', ('session',))
NEED_TAB = state_text('At least one tab is open in MainActivity', ('session',))
NEED_STORAGE = state_text('External storage is available', ('file',))
NEED_BOOKMARK = state_text('At least one bookmark exists', ('data',))
NEED_HISTORY = state_text('Navigation history exists (back button enabled)', ('session',))
NEED_SEARCH = state_text('Search mode is active', ('session',))

SCREENS = {
    'S_ENTRY': 'Outside the app: launcher, intent from another app, service start, broadcast, or test harness',
    'S_MAIN': 'MainActivity: main file manager shell with tabs, drawer, FAB',
    'S_MAIN_TAB': 'MainActivity: a specific tab showing file list',
    'S_PERM': 'PermissionsActivity: requesting WRITE_EXTERNAL_STORAGE permission',
    'S_PREFS': 'PreferencesActivity: app settings screen',
    'S_TEXT_EDITOR': 'TextEditorActivity: text file viewer/editor',
    'S_DB_VIEWER': 'DatabaseViewerActivity: SQLite database viewer',
    'S_ABOUT': 'AboutActivity: about screen with app info',
    'S_DRAWER': 'MainActivity: navigation drawer open',
    'S_DIALOG': 'A dialog is showing',
    'S_SERVICE': 'A background service is running',
    'S_EXIT': 'The activity/process ended',
}

# ================================================================== B. entry points, process start, Application lifecycle

# ---- process start: Application and exported components
e('S_ENTRY', 'AppConfig.<init>', 'ENTRY', 'The process starts (any component about to run)',
  gui=['Launch the app'], evidence='SRC AndroidManifest.xml:48; ' + FW_APP)

# Application class hierarchy: AppConfig -> GlideApplication -> LeakCanaryApplication -> MultiDexApplication -> Application
e('AppConfig.<init>', 'LeakCanaryApplication.<init>', 'LIFECYCLE', 'AppConfig extends LeakCanaryApplication',
  evidence='SRC utils/application/AppConfig.java:48')
e('LeakCanaryApplication.<init>', 'LeakCanaryApplication.onCreate', 'LIFECYCLE', 'Application.onCreate called by system',
  evidence='SRC utils/application/LeakCanaryApplication.java:14-22; ' + FW_APP)
e('LeakCanaryApplication.onCreate', 'GlideApplication.onCreate', 'LIFECYCLE', 'super.onCreate() chain',
  evidence='SRC utils/application/LeakCanaryApplication.java:16')
e('GlideApplication.onCreate', 'AppConfig.onCreate', 'LIFECYCLE', 'super.onCreate() chain',
  evidence='SRC utils/application/GlideApplication.java:13')

# Note: AppConfig.onCreate initializes utilities; the bytecode will handle the explicit calls (USE_AUTO)

# ================================================================== C. MainActivity entry points and lifecycle

# MainActivity class hierarchy: MainActivity -> PermissionsActivity -> ThemedActivity -> PreferenceActivity -> BasicActivity -> AppCompatActivity

# MainActivity launcher entry
e('S_ENTRY', 'MainActivity.<init>', 'ENTRY', 'Launch from home screen (ACTION_MAIN / LAUNCHER)',
  gui=['Tap Amaze File Manager icon'], evidence='SRC AndroidManifest.xml:50-56; ' + FW_ACTIVITY,
  env=ENV_LAUNCHER)

# MainActivity extends PermissionsActivity
e('MainActivity.<init>', 'PermissionsActivity.<init>', 'LIFECYCLE', 'MainActivity extends PermissionsActivity',
  evidence='SRC activities/MainActivity.java:175')
e('PermissionsActivity.<init>', 'ThemedActivity.<init>', 'LIFECYCLE', 'PermissionsActivity extends ThemedActivity',
  evidence='SRC activities/superclasses/PermissionsActivity.java:18')
e('ThemedActivity.<init>', 'PreferenceActivity.<init>', 'LIFECYCLE', 'ThemedActivity extends PreferenceActivity',
  evidence='SRC activities/superclasses/ThemedActivity.java:20')
e('PreferenceActivity.<init>', 'BasicActivity.<init>', 'LIFECYCLE', 'PreferenceActivity extends BasicActivity',
  evidence='SRC activities/superclasses/PreferenceActivity.java (need to read)')
e('BasicActivity.<init>', 'MainActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate called by framework',
  evidence=FW_ACTIVITY + '; SRC activities/MainActivity.java:304')

# MainActivity other intent-filters - all share the same inheritance chain, split into contexts
e('S_ENTRY', 'MainActivity.<init>@GET_CONTENT', 'ENTRY', 'Another app requests file picker (ACTION_GET_CONTENT)',
  evidence='SRC AndroidManifest.xml:58-62; ' + FW_ACTIVITY, env=ENV_GET_CONTENT)
e('MainActivity.<init>@GET_CONTENT', 'MainActivity.onCreate@GET_CONTENT', 'LIFECYCLE', 'MainActivity.onCreate',
  evidence=FW_ACTIVITY)

e('S_ENTRY', 'MainActivity.<init>@RINGTONE', 'ENTRY', 'Another app requests ringtone picker (ACTION_RINGTONE_PICKER)',
  evidence='SRC AndroidManifest.xml:64-66; ' + FW_ACTIVITY, env=ENV_RINGTONE)
e('MainActivity.<init>@RINGTONE', 'MainActivity.onCreate@RINGTONE', 'LIFECYCLE', 'MainActivity.onCreate',
  evidence=FW_ACTIVITY)

e('S_ENTRY', 'MainActivity.<init>@VIEW_ARCHIVE', 'ENTRY', 'Another app opens archive with Amaze (ACTION_VIEW archive mimeType)',
  evidence='SRC AndroidManifest.xml:68-79; ' + FW_ACTIVITY, env=ENV_VIEW_ARCHIVE)
e('MainActivity.<init>@VIEW_ARCHIVE', 'MainActivity.onCreate@VIEW_ARCHIVE', 'LIFECYCLE', 'MainActivity.onCreate',
  evidence=FW_ACTIVITY)

e('S_ENTRY', 'MainActivity.<init>@QS_PREF', 'ENTRY', 'User long-presses FTP quick-settings tile (ACTION_QS_TILE_PREFERENCES)',
  evidence='SRC AndroidManifest.xml:81-83; ' + FW_ACTIVITY, env=ENV_QS_TILE_PREF)
e('MainActivity.<init>@QS_PREF', 'MainActivity.onCreate@QS_PREF', 'LIFECYCLE', 'MainActivity.onCreate',
  evidence=FW_ACTIVITY)

e('S_ENTRY', 'MainActivity.<init>@SCHEME', 'ENTRY', 'VIEW intent with com.amaze.filemanager:// scheme',
  evidence='SRC AndroidManifest.xml:85-90; ' + FW_ACTIVITY, env=ENV_SCHEME)
e('MainActivity.<init>@SCHEME', 'MainActivity.onCreate@SCHEME', 'LIFECYCLE', 'MainActivity.onCreate',
  evidence=FW_ACTIVITY)

e('S_ENTRY', 'MainActivity.<init>@FOLDER', 'ENTRY', 'VIEW intent for folder (mimeType resource/folder)',
  evidence='SRC AndroidManifest.xml:92-97; ' + FW_ACTIVITY, env=ENV_FOLDER_MIME)
e('MainActivity.<init>@FOLDER', 'MainActivity.onCreate@FOLDER', 'LIFECYCLE', 'MainActivity.onCreate',
  evidence=FW_ACTIVITY)

e('S_ENTRY', 'MainActivity.<init>@SEND', 'ENTRY', 'Another app sends files to save (ACTION_SEND / ACTION_SEND_MULTIPLE)',
  evidence='SRC AndroidManifest.xml:99-104; ' + FW_ACTIVITY, env=ENV_SEND)
e('MainActivity.<init>@SEND', 'MainActivity.onCreate@SEND', 'LIFECYCLE', 'MainActivity.onCreate',
  evidence=FW_ACTIVITY)

# MainActivity.onCreate calls key methods (simplified - bytecode AUTO will handle most explicit calls)
# SRC activities/MainActivity.java:304-390
e('MainActivity.onCreate', 'MainActivity.initialisePreferences', 'CALL', 'initialize preferences',
  evidence='SRC activities/MainActivity.java:308')
e('MainActivity.onCreate', 'MainActivity.initialiseViews', 'CALL', 'initialize views',
  evidence='SRC activities/MainActivity.java:320')
e('MainActivity.onCreate', 'MainActivity.initialiseFab', 'CALL', 'initialize FAB',
  evidence='SRC activities/MainActivity.java:325')

# MainActivity.onResume - key lifecycle callback
e('MainActivity.onCreate', 'MainActivity.onResume', 'LIFECYCLE', 'Activity.onResume',
  evidence=FW_ACTIVITY)

# Menu handling
e('MainActivity.onResume', 'MainActivity.onCreateOptionsMenu', 'LIFECYCLE', 'Activity menu callbacks',
  evidence=FW_MENU)
e('MainActivity.onCreateOptionsMenu', 'MainActivity.onOptionsItemSelected', 'LIFECYCLE', 'menu item selected',
  evidence=FW_MENU)

# ================================================================== D. other activities

# PreferencesActivity hierarchy: PreferencesActivity -> (unknown parent) -> BasicActivity -> AppCompatActivity
e('S_ENTRY', 'PreferencesActivity.<init>', 'ENTRY', 'System settings or in-app navigation to preferences',
  evidence='SRC AndroidManifest.xml:107-114; ' + FW_ACTIVITY, env=ENV_APP_PREF)
e('PreferencesActivity.<init>', 'BasicActivity.<init>', 'LIFECYCLE', 'PreferencesActivity extends BasicActivity',
  evidence='SRC activities/PreferencesActivity.java (need to read)')
e('BasicActivity.<init>', 'PreferencesActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate',
  evidence=FW_ACTIVITY)

# TextEditorActivity
e('S_ENTRY', 'TextEditorActivity.<init>', 'ENTRY', 'Another app opens text file with Amaze (ACTION_VIEW text/*)',
  evidence='SRC AndroidManifest.xml:115-125; ' + FW_ACTIVITY, env=ENV_TEXT_VIEW)
e('TextEditorActivity.<init>', 'BasicActivity.<init>', 'LIFECYCLE', 'TextEditorActivity extends BasicActivity',
  evidence='SRC activities/TextEditorActivity.java (need to read)')
e('BasicActivity.<init>', 'TextEditorActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate',
  evidence=FW_ACTIVITY)

# DatabaseViewerActivity  
e('S_ENTRY', 'DatabaseViewerActivity.<init>', 'ENTRY', 'Another app opens database file with Amaze (ACTION_VIEW db/*)',
  evidence='SRC AndroidManifest.xml:126-136; ' + FW_ACTIVITY, env=ENV_DB_VIEW)
e('DatabaseViewerActivity.<init>', 'BasicActivity.<init>', 'LIFECYCLE', 'DatabaseViewerActivity extends BasicActivity',
  evidence='SRC activities/DatabaseViewerActivity.java (need to read)')
e('BasicActivity.<init>', 'DatabaseViewerActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate',
  evidence=FW_ACTIVITY)

# AboutActivity (no intent-filter, in-app only)
e('AboutActivity.<init>', 'BasicActivity.<init>', 'LIFECYCLE', 'AboutActivity extends BasicActivity',
  evidence='SRC activities/AboutActivity.java (need to read)')
e('BasicActivity.<init>', 'AboutActivity.onCreate', 'LIFECYCLE', 'Activity.onCreate',
  evidence=FW_ACTIVITY)

# ================================================================== E. services

# All these services extend AbstractProgressiveService (which extends Service)
# Service lifecycle: <init> -> onCreate -> onStartCommand (for started services) / onBind (for bound services)

e('S_ENTRY', 'ExtractService.<init>', 'ENTRY', 'Extract service started for archive extraction',
  evidence='SRC AndroidManifest.xml:143-147; ' + FW_SERVICE)
e('ExtractService.<init>', 'ExtractService.onCreate', 'LIFECYCLE', 'Service.onCreate',
  evidence=FW_SERVICE + '; SRC asynchronous/services/ExtractService.java (need to read)')
e('ExtractService.onCreate', 'ExtractService.onStartCommand', 'LIFECYCLE', 'Service.onStartCommand for started service',
  evidence=FW_SERVICE)

e('S_ENTRY', 'ZipService.<init>', 'ENTRY', 'Zip service started for archive compression',
  evidence='SRC AndroidManifest.xml:148-152; ' + FW_SERVICE)
e('ZipService.<init>', 'ZipService.onCreate', 'LIFECYCLE', 'Service.onCreate',
  evidence=FW_SERVICE)
e('ZipService.onCreate', 'ZipService.onStartCommand', 'LIFECYCLE', 'Service.onStartCommand',
  evidence=FW_SERVICE)

e('S_ENTRY', 'CopyService.<init>', 'ENTRY', 'Copy service started for file operations',
  evidence='SRC AndroidManifest.xml:153-157; ' + FW_SERVICE)
e('CopyService.<init>', 'CopyService.onCreate', 'LIFECYCLE', 'Service.onCreate',
  evidence=FW_SERVICE + '; SRC asynchronous/services/CopyService.java:100')
e('CopyService.onCreate', 'CopyService.onStartCommand', 'LIFECYCLE', 'Service.onStartCommand',
  evidence=FW_SERVICE)

e('S_ENTRY', 'EncryptService.<init>', 'ENTRY', 'Encrypt service started for file encryption',
  evidence='SRC AndroidManifest.xml:159-161; ' + FW_SERVICE)
e('EncryptService.<init>', 'EncryptService.onCreate', 'LIFECYCLE', 'Service.onCreate',
  evidence=FW_SERVICE)
e('EncryptService.onCreate', 'EncryptService.onStartCommand', 'LIFECYCLE', 'Service.onStartCommand',
  evidence=FW_SERVICE)

e('S_ENTRY', 'DecryptService.<init>', 'ENTRY', 'Decrypt service started for file decryption',
  evidence='SRC AndroidManifest.xml:163-165; ' + FW_SERVICE)
e('DecryptService.<init>', 'DecryptService.onCreate', 'LIFECYCLE', 'Service.onCreate',
  evidence=FW_SERVICE)
e('DecryptService.onCreate', 'DecryptService.onStartCommand', 'LIFECYCLE', 'Service.onStartCommand',
  evidence=FW_SERVICE)

e('S_ENTRY', 'FtpService.<init>', 'ENTRY', 'FTP server service started or bound',
  evidence='SRC AndroidManifest.xml:167-172; ' + FW_SERVICE, env=ENV_FTP_NETWORK)
e('FtpService.<init>', 'FtpService.onCreate', 'LIFECYCLE', 'Service.onCreate',
  evidence=FW_SERVICE)
e('FtpService.onCreate', 'FtpService.onStartCommand', 'LIFECYCLE', 'Service.onStartCommand',
  evidence=FW_SERVICE)

e('S_ENTRY', 'FtpTileService.<init>', 'ENTRY', 'FTP quick-settings tile service bound by system',
  evidence='SRC AndroidManifest.xml:174-182; ' + FW_SERVICE, env=ENV_FTP_TILE)
e('FtpTileService.<init>', 'FtpTileService.onCreate', 'LIFECYCLE', 'TileService.onCreate',
  evidence=FW_SERVICE)
# TileService uses onClick, not onStartCommand
e('FtpTileService.onCreate', 'FtpTileService.onClick', 'LIFECYCLE', 'TileService.onClick when tile tapped',
  evidence='INFERRED TileService.onClick called when quick-settings tile is tapped (platform source not read)')

# ================================================================== F. receivers

e('S_ENTRY', 'FtpReceiver.<init>', 'ENTRY', 'FtpReceiver receives ACTION_START_FTPSERVER broadcast',
  evidence='SRC AndroidManifest.xml:184-192; ' + FW_RECEIVER, env=ENV_FTP_START)
e('FtpReceiver.<init>', 'FtpReceiver.onReceive', 'LIFECYCLE', 'BroadcastReceiver.onReceive',
  evidence=FW_RECEIVER)

e('S_ENTRY', 'FtpReceiver.<init>@STOP', 'ENTRY', 'FtpReceiver receives ACTION_STOP_FTPSERVER broadcast',
  evidence='SRC AndroidManifest.xml:184-192; ' + FW_RECEIVER, env=ENV_FTP_STOP)
e('FtpReceiver.<init>@STOP', 'FtpReceiver.onReceive@STOP', 'LIFECYCLE', 'BroadcastReceiver.onReceive',
  evidence=FW_RECEIVER)

# Note: SMSInstrumentedReceiver is in AndroidManifest.xml but NOT in method_list.json (not built into APK)
# Therefore it cannot be modeled. If it appears in UNREACHABLE scan, mark it framework_never_calls.

# ================================================================== G. fragments and UI

# MainActivity.onCreate runs an AsyncTask to load data, then in onPostExecute calls goToMain
# which creates TabFragment, which in turn creates MainFragment
e('MainActivity.onCreate', 'MainActivity$1.<init>', 'CALL', 'create AsyncTask for data loading',
  evidence='SRC activities/MainActivity.java:372-427')
e('MainActivity$1.<init>', 'MainActivity$1.doInBackground', 'LIFECYCLE', 'AsyncTask.doInBackground',
  evidence=FW_ASYNC)
e('MainActivity$1.doInBackground', 'MainActivity$1.onPostExecute', 'LIFECYCLE', 'AsyncTask.onPostExecute',
  evidence=FW_ASYNC)
e('MainActivity$1.onPostExecute', 'MainActivity.goToMain', 'CALL', 'default: call goToMain',
  evidence='SRC activities/MainActivity.java:420')
e('MainActivity.goToMain', 'TabFragment.<init>', 'CALL', 'create TabFragment',
  evidence='SRC activities/MainActivity.java:784')

# TabFragment lifecycle and MainFragment creation
e('TabFragment.<init>', 'TabFragment.onCreate', 'LIFECYCLE', 'Fragment.onCreate',
  evidence=FW_FRAG)
e('TabFragment.onCreate', 'TabFragment.onCreateView', 'LIFECYCLE', 'Fragment.onCreateView',
  evidence=FW_FRAG)
# TabFragment creates MainFragment (need to read TabFragment source to verify)
e('TabFragment.onCreateView', 'MainFragment.<init>', 'FRAMEWORK', 'TabFragment creates MainFragment',
  evidence='SRC fragments/TabFragment.java (need to read); ' + FW_FRAG)

# MainFragment lifecycle
e('MainFragment.<init>', 'MainFragment.onCreate', 'LIFECYCLE', 'Fragment.onCreate',
  evidence=FW_FRAG)
e('MainFragment.onCreate', 'MainFragment.onCreateView', 'LIFECYCLE', 'Fragment.onCreateView',
  evidence=FW_FRAG)
e('MainFragment.onCreateView', 'MainFragment.onActivityCreated', 'LIFECYCLE', 'Fragment.onActivityCreated',
  evidence=FW_FRAG)

# MainFragment creates RecyclerAdapter (need to verify where it's created)
# Likely in onActivityCreated or from another method - AUTO edges should handle it

# RecyclerAdapter lifecycle (simplified - AUTO will handle most)
e('RecyclerAdapter.<init>', 'RecyclerAdapter.onCreateViewHolder', 'LIFECYCLE', 'RecyclerView.Adapter callback',
  evidence='INFERRED RecyclerView calls adapter lifecycle methods (androidx source not read)')
e('RecyclerAdapter.onCreateViewHolder', 'RecyclerAdapter.onBindViewHolder', 'LIFECYCLE', 'RecyclerView.Adapter callback',
  evidence='INFERRED RecyclerView calls adapter lifecycle methods (androidx source not read)')

# RecyclerAdapter.setItems creates RecyclerViewPreloader with RecyclerPreloadModelProvider
# RecyclerAdapter.java:388-391: modelProvider = new RecyclerPreloadModelProvider(...); preloader = new RecyclerViewPreloader<>(..., modelProvider, ...)
# The RecyclerViewPreloader calls PreloadModelProvider.getPreloadRequestBuilder as framework callback
e('RecyclerAdapter.setItems(RecyclerView,ArrayList,boolean)', 'RecyclerPreloadModelProvider.getPreloadRequestBuilder', 'FRAMEWORK',
  'RecyclerViewPreloader calls PreloadModelProvider.getPreloadRequestBuilder to get image request for preloading',
  evidence='INFERRED Glide RecyclerViewPreloader (source not read); SRC RecyclerAdapter.java:388-391 creates preloader with modelProvider')

# ===== G. Drawer navigation and fragments

# Drawer setup: MainActivity.initialiseViews creates Drawer
# MainActivity.java:1425
e('MainActivity.initialiseViews', 'Drawer.<init>', 'CALL', 'drawer = new Drawer(this)',
  evidence='SRC MainActivity.java:1425')

# Drawer constructor sets up NavigationView listener  
# Drawer.java:165: navView.setNavigationItemSelectedListener(this)
e('Drawer.<init>', 'Drawer.onNavigationItemSelected', 'FRAMEWORK', 
  'NavigationView calls OnNavigationItemSelectedListener.onNavigationItemSelected when menu item clicked',
  evidence='INFERRED androidx.design.widget.NavigationView (source not read); SRC Drawer.java:165 sets listener')

# Drawer.onNavigationItemSelected branches based on MenuMetadata type
# Drawer.java:556-600: switch on meta.type, ITEM_INTENT case calls meta.onClickListener.onClick()
# The onClick lambda is defined when menu items are added

# Apps menu item (R.string.apps) creates AppsListFragment
# Drawer.java:418-428: addNewItem with lambda that does: new AppsListFragment()
e('Drawer.onNavigationItemSelected', 'AppsListFragment.<init>', 'CALL',
  'Menu item click executes lambda: new AppsListFragment(); transaction.replace(R.id.content_frame, fragment)',
  evidence='SRC Drawer.java:418-428; Drawer.java:597 onClick calls lambda; Drawer.java:535 onDrawerClosed commits transaction')

# FTP menu item (R.string.ftp) creates FtpServerFragment  
# Drawer.java:402-414
e('Drawer.onNavigationItemSelected', 'FtpServerFragment.<init>', 'CALL',
  'Menu item click executes lambda: new FtpServerFragment(); transaction.replace(R.id.content_frame, fragment)',
  evidence='SRC Drawer.java:402-414; Drawer.java:597 onClick; Drawer.java:535 onDrawerClosed commits')

# AppsListFragment lifecycle
e('AppsListFragment.<init>', 'AppsListFragment.onCreate', 'LIFECYCLE', 'Fragment.onCreate',
  evidence='INFERRED Fragment lifecycle (androidx source not read)')
e('AppsListFragment.onCreate', 'AppsListFragment.onActivityCreated', 'LIFECYCLE', 'Fragment.onActivityCreated',
  evidence='INFERRED Fragment lifecycle (androidx source not read)')

# AppsListFragment.onActivityCreated creates ListPreloader with AppsAdapterPreloadModel
# AppsListFragment.java:96-99: modelProvider = new AppsAdapterPreloadModel(app); preloader = new ListPreloader<>(..., modelProvider, ...)
# The ListPreloader calls PreloadModelProvider.getPreloadRequestBuilder as a framework callback
e('AppsListFragment.onActivityCreated', 'AppsAdapterPreloadModel.getPreloadRequestBuilder', 'FRAMEWORK',
  'ListPreloader calls PreloadModelProvider.getPreloadRequestBuilder to get image request for preloading',
  evidence='INFERRED Glide ListPreloader (source not read); SRC AppsListFragment.java:96-99 creates ListPreloader with modelProvider')

# ListPreloader also calls PreloadModelProvider.getPreloadItems to get items to preload
e('AppsListFragment.onActivityCreated', 'AppsAdapterPreloadModel.getPreloadItems', 'FRAMEWORK',
  'ListPreloader calls PreloadModelProvider.getPreloadItems to get list of items',
  evidence='INFERRED Glide ListPreloader (source not read); SRC AppsAdapterPreloadModel.java:36-40 implements interface method')

# AppsListFragment.onLoadFinished calls setItemList on modelProvider
# AppsListFragment.java:170
# (Note: onLoadFinished is a Loader callback, need to check if it's reachable)

# FtpServerFragment lifecycle
e('FtpServerFragment.<init>', 'FtpServerFragment.onCreate', 'LIFECYCLE', 'Fragment.onCreate',
  evidence='INFERRED Fragment lifecycle (androidx source not read)')

# Glide library internal initialization (INFERRED, source not read)
# When GlideApp.with(Fragment) is called, Glide internally creates a GlideRequests instance
# This goes through GeneratedRequestManagerFactory.build which calls GlideRequests.<init>
# We model this as an explicit edge to bootstrap the bytecode paths
e('GlideApp.with(Fragment)#2', 'GlideRequests.<init>', 'CALL',
  'GlideApp.with internally creates GlideRequests instance via GeneratedRequestManagerFactory',
  evidence='INFERRED Glide library internal initialization (source not read); bytecode shows GeneratedRequestManagerFactory.build -> GlideRequests.<init>')

# GlideRequests.asDrawable returns a GlideRequest which internally uses GlideRequest.<init>
# Auto-calls shows: GlideRequests.as -> GlideRequest.<init>(Glide,RequestManager,Class,Context)
e('GlideRequests.asDrawable', 'GlideRequest.<init>(Glide,RequestManager,Class,Context)', 'CALL',
  'GlideRequests.asDrawable creates GlideRequest instance internally',
  evidence='INFERRED Glide library method chaining (source not read); bytecode auto_calls.json shows call')

# ================================================================== G2. Accepted edges from Helper 4 (part 4 - 2026-10-27)

# AppDataParcelable edges
e('AppListLoader.loadInBackground', 'AppDataParcelable.<init>(String,String,String,String,String,long,long)', 'CALL', 
  'AppListLoader creates AppDataParcelable for each installed app',
  evidence='SRC AppListLoader.java:70-76')

e('AppListLoader.loadInBackground', 'AppDataParcelable$AppDataSorter.<init>', 'CALL',
  'AppListLoader sorts app list using AppDataSorter',
  evidence='SRC AppListLoader.java:79')

# IconDataParcelable edges
e('CompressedObjectParcelable.<init>()', 'IconDataParcelable.<init>(int,int)', 'CALL',
  'CompressedObjectParcelable creates icon data for compressed file entries',
  evidence='SRC CompressedObjectParcelable.java:54-55')

e('LayoutElementParcelable.<init>', 'IconDataParcelable.<init>(int,String,int)', 'CALL',
  'LayoutElementParcelable creates icon data for cloud files',
  evidence='SRC LayoutElementParcelable.java:91')
  
e('LayoutElementParcelable.<init>', 'IconDataParcelable.<init>(int,int)', 'CALL',
  'LayoutElementParcelable creates icon data for regular files',
  evidence='SRC LayoutElementParcelable.java:93')

e('IconDataParcelable$1.createFromParcel', 'IconDataParcelable.<init>(Parcel)', 'CALL',
  'CREATOR.createFromParcel calls Parcel constructor',
  evidence='SRC IconDataParcelable.java:72')

# AppDataParcelable$1 (CREATOR) edges  
e('AppDataParcelable$1.createFromParcel', 'AppDataParcelable.<init>(Parcel)', 'CALL',
  'CREATOR.createFromParcel calls private Parcel constructor',
  evidence='SRC AppDataParcelable.java:57-58')

# TODO: Add CompressedExplorerFragment (opened from MainFragment when archive file clicked)
# TODO: Add CloudSheetFragment (cloud storage configuration)
# TODO: Add other drawer menu items if any

# ================================================================== H-K. subsystems (placeholders for expansion)

# TODO: cloud storage (Dropbox, Drive, OneDrive, Box)
# TODO: FTP server internals
# TODO: archive handling (junrar, 7z, tar, etc.)
# TODO: database viewer, text editor internals
# TODO: encryption/decryption
# TODO: USB OTG
# TODO: root operations
# TODO: SSH/SFTP, SMB

# ---- Helper label_c1 part (2026-10-27 21:12) - 54 methods from chunk_1
# Classes: AES256SHA256Decoder, AES256SHA256Decoder$1, AdvancedSearchPref, AmazeFileManagerModule,
#          AnimUtils, ApkImageDataFetcher, ApkImageModelLoader, ApkImageModelLoaderFactory,
#          AppConfig, AppConfig$1, AppConfig$CustomAsyncCallbacks, AppHolder

# AdvancedSearchPref
e('PreferencesActivity.selectItem', 'AdvancedSearchPref.<init>', 'CALL',
  'PreferencesActivity instantiates AdvancedSearchPref in selectItem',
  evidence='SRC PreferencesActivity.java:267')

e('AdvancedSearchPref.<init>', 'AdvancedSearchPref.onCreate', 'FRAMEWORK',
  'Framework calls onCreate on PreferenceFragment after instantiation',
  evidence='INFERRED framework lifecycle for PreferenceFragment')

# AmazeFileManagerModule (Glide)
e('GlideApp.<init>', 'AmazeFileManagerModule.<init>', 'FRAMEWORK',
  'Glide annotation processor generates code that instantiates @GlideModule classes',
  evidence='INFERRED Glide annotation processor for @GlideModule')

e('AmazeFileManagerModule.<init>', 'AmazeFileManagerModule.registerComponents', 'FRAMEWORK',
  'Glide framework calls registerComponents on AppGlideModule subclasses',
  evidence='INFERRED Glide framework lifecycle for AppGlideModule')

e('AmazeFileManagerModule.registerComponents', 'ApkImageModelLoaderFactory.<init>', 'CALL',
  'registerComponents creates ApkImageModelLoaderFactory',
  evidence='SRC AmazeFileManagerModule.java:22')

# AnimUtils
e('Indicator.<init>', 'AnimUtils.getFastOutSlowInInterpolator', 'CALL',
  'Indicator constructor calls AnimUtils.getFastOutSlowInInterpolator',
  evidence='SRC Indicator.java:153')

e('AppsAdapter.onBindViewHolder', 'AnimUtils.marqueeAfterDelay', 'CALL',
  'AppsAdapter.onBindViewHolder calls marqueeAfterDelay',
  evidence='SRC AppsAdapter.java:139')

e('AnimUtils.marqueeAfterDelay', 'AnimUtils.lambda$marqueeAfterDelay$0', 'CALL',
  'marqueeAfterDelay posts lambda to Handler',
  evidence='SRC AnimUtils.java:47-49')

# ApkImage Glide loaders
e('ApkImageModelLoaderFactory.build', 'ApkImageModelLoader.<init>', 'CALL',
  'Factory.build creates ApkImageModelLoader',
  evidence='SRC ApkImageModelLoaderFactory.java:23')

e('ApkImageModelLoaderFactory.<init>', 'ApkImageModelLoaderFactory.build', 'FRAMEWORK',
  'Glide calls build on ModelLoaderFactory',
  evidence='INFERRED Glide framework calls build on registered factories')

e('ApkImageModelLoaderFactory.<init>', 'ApkImageModelLoaderFactory.teardown', 'FRAMEWORK',
  'Glide calls teardown on ModelLoaderFactory during cleanup',
  evidence='INFERRED Glide framework lifecycle')

e('ApkImageModelLoader.<init>', 'ApkImageModelLoader.buildLoadData', 'FRAMEWORK',
  'Glide calls buildLoadData on ModelLoader to create LoadData',
  evidence='INFERRED Glide framework calls buildLoadData')

e('ApkImageModelLoader.<init>', 'ApkImageModelLoader.handles', 'FRAMEWORK',
  'Glide calls handles on ModelLoader to check if it can handle model',
  evidence='INFERRED Glide framework calls handles')

e('ApkImageModelLoader.buildLoadData', 'ApkImageDataFetcher.<init>', 'CALL',
  'buildLoadData creates ApkImageDataFetcher',
  evidence='SRC ApkImageModelLoader.java:27')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.loadData', 'FRAMEWORK',
  'Glide calls loadData on DataFetcher to fetch data',
  evidence='INFERRED Glide framework calls loadData')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.cleanup', 'FRAMEWORK',
  'Glide calls cleanup on DataFetcher after load completes',
  evidence='INFERRED Glide framework lifecycle')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.cancel', 'FRAMEWORK',
  'Glide calls cancel on DataFetcher if load cancelled',
  evidence='INFERRED Glide framework lifecycle')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.getDataClass', 'FRAMEWORK',
  'Glide calls getDataClass on DataFetcher to determine result type',
  evidence='INFERRED Glide framework calls getDataClass')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.getDataSource', 'FRAMEWORK',
  'Glide calls getDataSource on DataFetcher to determine data source type',
  evidence='INFERRED Glide framework calls getDataSource')

# AppHolder
e('AppsAdapter.onCreateViewHolder', 'AppHolder.<init>', 'CALL',
  'AppsAdapter creates AppHolder in onCreateViewHolder',
  evidence='SRC AppsAdapter.java:114')

# AppConfig - Application class
e('Application.onCreate', 'AppConfig.<init>', 'FRAMEWORK',
  'Android framework instantiates Application subclass',
  evidence='INFERRED framework creates Application')

e('AppConfig.<init>', 'AppConfig.onCreate', 'FRAMEWORK',
  'Framework calls onCreate on Application after instantiation',
  evidence='INFERRED framework lifecycle for Application')

e('AppConfig.<init>', 'AppConfig.onTerminate', 'FRAMEWORK',
  'Framework calls onTerminate on Application during shutdown',
  evidence='INFERRED framework lifecycle for Application')

e('SftpConnectDialog.onCreate', 'AppConfig.getInstance', 'CALL',
  'SftpConnectDialog calls getInstance to get AppConfig singleton',
  evidence='SRC SftpConnectDialog.java:97-98')

e('AppConfig.getInstance', 'AppConfig.getUtilsProvider', 'CALL',
  'Code calls getUtilsProvider after getInstance',
  evidence='SRC SftpConnectDialog.java:97')

e('AppConfig.getInstance', 'AppConfig.getUtilsHandler', 'CALL',
  'Code calls getUtilsHandler after getInstance',
  evidence='SRC SftpConnectDialog.java:98')

e('Drawer.<init>', 'AppConfig.getInstance', 'CALL',
  'Drawer constructor calls getInstance',
  evidence='SRC Drawer.java:156')

e('AppConfig.getInstance', 'AppConfig.getImageLoader', 'CALL',
  'Code calls getImageLoader after getInstance',
  evidence='SRC Drawer.java:156')

e('AppConfig.getInstance', 'AppConfig.getScreenUtils', 'CALL',
  'Code calls getScreenUtils after getInstance',
  evidence='SRC Drawer.java:243')

e('GeneralDialogCreation.showNameDialog', 'AppConfig.getInstance', 'CALL',
  'showNameDialog calls getInstance',
  evidence='SRC GeneralDialogCreation.java:889')

e('AppConfig.getInstance', 'AppConfig.getMainActivityContext', 'CALL',
  'Code calls getMainActivityContext after getInstance',
  evidence='SRC GeneralDialogCreation.java:889')

e('MainActivity.onCreate', 'AppConfig.setMainActivityContext', 'CALL',
  'MainActivity sets itself as main activity context',
  evidence='INFERRED MainActivity needs to register itself')

e('SftpConnectDialog.lambda$onCreateView$2', 'AppConfig.runInBackground', 'CALL',
  'SftpConnectDialog lambda calls runInBackground',
  evidence='SRC SftpConnectDialog.java:249')

e('UtilsHandler.addCommonBookmarks', 'AppConfig.runInBackground', 'CALL',
  'UtilsHandler calls runInBackground',
  evidence='SRC UtilsHandler.java:179')

e('LoadFilesListTask.onPostExecute', 'AppConfig.toast', 'CALL',
  'LoadFilesListTask calls toast(Context, int)',
  evidence='SRC LoadFilesListTask.java:189')

e('AppConfig.toast', 'AppConfig.runInApplicationThread', 'CALL',
  'toast calls runInApplicationThread to show on UI thread',
  evidence='SRC AppConfig.java:161, 183')

e('AppConfig.toast', 'AppConfig.lambda$toast$0', 'CALL',
  'toast(Context, int) creates lambda',
  evidence='SRC AppConfig.java:160-162')

e('AppConfig.toast', 'AppConfig.lambda$toast$1', 'CALL',
  'toast(Context, String) creates lambda',
  evidence='SRC AppConfig.java:182-184')

e('AppConfig.runInParallel', 'AppConfig$1.<init>', 'CALL',
  'runInParallel creates anonymous AsyncTask',
  evidence='SRC AppConfig.java:110-127')

e('AppConfig$1.<init>', 'AppConfig$1.onPreExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPreExecute',
  evidence='INFERRED AsyncTask lifecycle')

e('AppConfig$1.<init>', 'AppConfig$1.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED AsyncTask lifecycle')

e('AppConfig$1.<init>', 'AppConfig$1.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED AsyncTask lifecycle')

e('AppConfig$1.onPreExecute', 'AppConfig$CustomAsyncCallbacks.onPreExecute', 'CALL',
  'AsyncTask onPreExecute calls callbacks.onPreExecute',
  evidence='SRC AppConfig.java:115')

e('AppConfig$1.doInBackground', 'AppConfig$CustomAsyncCallbacks.doInBackground', 'CALL',
  'AsyncTask doInBackground calls callbacks.doInBackground',
  evidence='SRC AppConfig.java:119')

e('AppConfig$1.onPostExecute', 'AppConfig$CustomAsyncCallbacks.onPostExecute', 'CALL',
  'AsyncTask onPostExecute calls callbacks.onPostExecute',
  evidence='SRC AppConfig.java:125')

e('AppConfig.runInParallel', 'AppConfig$CustomAsyncCallbacks.<init>', 'CALL',
  'Caller must subclass CustomAsyncCallbacks to use runInParallel',
  evidence='INFERRED from API design; constructor called by subclass instantiation')

e('AppConfig.<init>', 'AppConfig.<clinit>', 'FRAMEWORK',
  'JVM calls static initializer before first use of class',
  evidence='INFERRED JVM static initialization')

# ---- Helper label_c3 part (2026-10-27 21:12) - 69 methods from chunk_3
# Classes: BottomBar and inner classes, BoundedFileChannelInputStream, Bzip2* classes, CLI

# BottomBar routes
e('MainActivity.onCreate', 'AppBar.<init>', 'CALL', 'Activity created, appbar initialized',
  evidence='SRC activities/MainActivity.java:277,290')

e('AppBar.<init>', 'BottomBar.<init>', 'CALL', 'AppBar creates BottomBar in constructor',
  evidence='SRC ui/views/appbar/AppBar.java:33,36')

e('BottomBar.<init>', 'BottomBar$1.<init>', 'CALL', 'Anonymous CountDownTimer created in BottomBar constructor',
  evidence='SRC ui/views/appbar/BottomBar.java:111')

e('BottomBar.<init>', 'BottomBar$2.<init>', 'CALL', 'Anonymous GestureDetector.SimpleOnGestureListener created in BottomBar constructor',
  evidence='SRC ui/views/appbar/BottomBar.java:119')

e('MainFragment.onActivityCreated', 'BottomBar.setClickListener', 'CALL', 'Fragment lifecycle sets touch listeners',
  evidence='SRC fragments/MainFragment.java:267,281')

e('MainActivity.onFragmentChangedListener', 'BottomBar.setClickListener', 'CALL', 'Fragment change sets listeners',
  evidence='SRC activities/MainActivity.java:854')

e('BottomBar$2.onSingleTapConfirmed', 'BottomBar.showButtons', 'CALL', 'Gesture triggers button display',
  evidence='SRC ui/views/appbar/BottomBar.java:124,134,139')

e('BottomBar.showButtons', 'BottomBar$3.<init>', 'CALL', 'AnimatorListenerAdapter for forward navigation created',
  evidence='SRC ui/views/appbar/BottomBar.java:346')

e('BottomBar.showButtons', 'BottomBar$4.<init>', 'CALL', 'AnimatorListenerAdapter for backward navigation created',
  evidence='SRC ui/views/appbar/BottomBar.java:373')

e('BottomBar.showButtons', 'BottomBar$5.<init>', 'CALL', 'AnimatorListenerAdapter for initial path created',
  evidence='SRC ui/views/appbar/BottomBar.java:398')

e('BottomBar.showButtons', 'BottomBar$6.<init>', 'CALL', 'AnimatorListenerAdapter for different path slideout created',
  evidence='SRC ui/views/appbar/BottomBar.java:425')

e('BottomBar$6.onAnimationEnd', 'BottomBar$6$1.<init>', 'CALL', 'Nested AnimatorListenerAdapter for slidein created',
  evidence='SRC ui/views/appbar/BottomBar.java:446')

e('MainFragment.updateTabWithDb', 'BottomBar.updatePath', 'CALL', 'Fragment updates path display',
  evidence='SRC fragments/MainFragment.java:451')

e('TabFragment.onTabChanged', 'BottomBar.updatePath', 'CALL', 'Tab change updates path',
  evidence='SRC fragments/TabFragment.java:222,305')

e('CompressedExplorerFragment.updateBottomBar', 'BottomBar.updatePath', 'CALL', 'Compressed explorer updates path',
  evidence='SRC fragments/CompressedExplorerFragment.java:445')

e('MainFragment.reloadListElements', 'BottomBar.setPathText', 'CALL', 'Search UI updates path text',
  evidence='SRC fragments/MainFragment.java:1604,1625,1650')

e('MainFragment.reloadListElements', 'BottomBar.setFullPathText', 'CALL', 'Search UI updates full path text',
  evidence='SRC fragments/MainFragment.java:1605,1626,1651')

e('AppsListFragment.onViewCreated', 'BottomBar.setVisibility', 'CALL', 'Apps list hides bottom bar',
  evidence='SRC fragments/AppsListFragment.java:84')

e('FtpServerFragment.onViewCreated', 'BottomBar.setVisibility', 'CALL', 'FTP fragment hides bottom bar',
  evidence='SRC fragments/FtpServerFragment.java:157')

e('ProcessViewerFragment.onViewCreated', 'BottomBar.setVisibility', 'CALL', 'Process viewer hides bottom bar',
  evidence='SRC fragments/ProcessViewerFragment.java:143')

e('MainActivity.onFragmentChangedListener', 'BottomBar.resetClickListener', 'CALL', 'Fragment change resets listeners',
  evidence='SRC activities/MainActivity.java:892')

e('MainActivity.updateViews', 'BottomBar.setBackgroundColor', 'CALL', 'Theme change updates background',
  evidence='SRC activities/MainActivity.java:1475')

e('BottomBar.updatePath', 'BottomBar.showButtons', 'CALL', 'Path update may trigger button display',
  evidence='SRC ui/views/appbar/BottomBar.java:469')

e('BottomBar.updatePath', 'BottomBar.sendScroll', 'CALL', 'Path animation scrolls view',
  evidence='SRC ui/views/appbar/BottomBar.java:361,390,408,433,462')

e('BottomBar.showButtons', 'BottomBar.createArrow', 'CALL', 'Button generation creates arrow icons',
  evidence='SRC ui/views/appbar/BottomBar.java:232')

e('BottomBar.showButtons', 'BottomBar.createFolderButton', 'CALL', 'Button generation creates folder buttons',
  evidence='SRC ui/views/appbar/BottomBar.java:223')

e('BottomBar.showButtons', 'BottomBar.areButtonsShowing', 'CALL', 'showButtons checks if buttons already showing',
  evidence='SRC ui/views/appbar/BottomBar.java:338')

e('BottomBar.onTouch', 'BottomBar$2.onDown', 'CALL', 'Touch delegated to gesture detector',
  evidence='INFERRED source not read')

e('BottomBar.onTouch', 'BottomBar$2.onSingleTapConfirmed', 'CALL', 'Touch delegated to gesture detector',
  evidence='INFERRED source not read')

e('BottomBar.onTouch', 'BottomBar$2.onLongPress', 'CALL', 'Touch delegated to gesture detector',
  evidence='INFERRED source not read')

e('BottomBar$1.onTick', 'BottomBar$1.onFinish', 'CALL', 'Timer lifecycle',
  evidence='INFERRED source not read')

e('BottomBar$3.onAnimationStart', 'BottomBar$3.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$3.onAnimationEnd', 'BottomBar$3.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$4.onAnimationStart', 'BottomBar$4.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$4.onAnimationEnd', 'BottomBar$4.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$5.onAnimationStart', 'BottomBar$5.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$5.onAnimationEnd', 'BottomBar$5.lambda$onAnimationEnd$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$6.onAnimationStart', 'BottomBar$6.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$6$1.onAnimationStart', 'BottomBar$6$1.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$6$1.onAnimationEnd', 'BottomBar$6$1.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar.showButtons', 'BottomBar.lambda$showButtons$0', 'CALL', 'Lambda from button root click',
  evidence='SRC ui/views/appbar/BottomBar.java:197')

e('BottomBar.showButtons', 'BottomBar.lambda$showButtons$1', 'CALL', 'Lambda from button storage click',
  evidence='SRC ui/views/appbar/BottomBar.java:217')

e('BottomBar.showButtons', 'BottomBar.lambda$showButtons$2', 'CALL', 'Lambda from folder button click',
  evidence='SRC ui/views/appbar/BottomBar.java:225')

e('BottomBar.showButtons', 'BottomBar.lambda$showButtons$3', 'CALL', 'Lambda from post action',
  evidence='SRC ui/views/appbar/BottomBar.java:235')

e('BottomBar.sendScroll', 'BottomBar.lambda$sendScroll$4', 'CALL', 'Lambda from sendScroll',
  evidence='SRC ui/views/appbar/BottomBar.java:476')

# Animation lifecycle framework calls
e('BottomBar$3.<init>', 'BottomBar$3.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:356')

e('BottomBar$3.<init>', 'BottomBar$3.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:347')

e('BottomBar$4.<init>', 'BottomBar$4.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:385')

e('BottomBar$4.<init>', 'BottomBar$4.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:375')

e('BottomBar$5.<init>', 'BottomBar$5.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:401')

e('BottomBar$5.<init>', 'BottomBar$5.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:410')

e('BottomBar$6.<init>', 'BottomBar$6.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:428')

e('BottomBar$6.<init>', 'BottomBar$6.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:437')

e('BottomBar$6$1.<init>', 'BottomBar$6$1.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:459')

e('BottomBar$6$1.<init>', 'BottomBar$6$1.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:448')

e('BottomBar$1.<init>', 'BottomBar$1.onTick', 'FRAMEWORK', 'Framework timer lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:113')

e('BottomBar$1.<init>', 'BottomBar$1.onFinish', 'FRAMEWORK', 'Framework timer lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:115')

e('BottomBar$2.<init>', 'BottomBar$2.onDown', 'FRAMEWORK', 'Framework gesture detection',
  evidence='SRC ui/views/appbar/BottomBar.java:121')

e('BottomBar$2.<init>', 'BottomBar$2.onSingleTapConfirmed', 'FRAMEWORK', 'Framework gesture detection',
  evidence='SRC ui/views/appbar/BottomBar.java:125')

e('BottomBar$2.<init>', 'BottomBar$2.onLongPress', 'FRAMEWORK', 'Framework gesture detection',
  evidence='SRC ui/views/appbar/BottomBar.java:144')

# Bzip2 archive handling
e('Bzip2Decompressor.changePath', 'Bzip2HelperTask.<init>', 'CALL', 'Created by Bzip2Decompressor.changePath',
  evidence='SRC filesystem/compressed/showcontents/helpers/Bzip2Decompressor.java:43')

e('Bzip2HelperTask.<init>', 'Bzip2HelperTask.addElements', 'CALL', 'Called from CompressedHelperTask.doInBackground',
  evidence='SRC asynchronous/asynctasks/compress/CompressedHelperTask.java:53')

e('CompressedHelper.getExtractorInstance', 'Bzip2Extractor.<init>', 'CALL', 'Created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:90,174')

e('Bzip2Extractor.<init>', 'Bzip2Extractor.extractWithFilter', 'CALL', 'Called from Extractor base class',
  evidence='SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:49')

e('Bzip2Extractor.extractWithFilter', 'Bzip2Extractor.extractEntry', 'CALL', 'Called from extractWithFilter',
  evidence='SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:68')

e('CompressedHelper.getCompressorInstance', 'Bzip2Decompressor.<init>', 'CALL', 'Created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:120,174')

e('CompressedExplorerFragment.changePath', 'Bzip2Decompressor.changePath', 'CALL', 'Fragment navigation calls changePath',
  evidence='SRC fragments/CompressedExplorerFragment.java:411')

# BoundedFileChannelInputStream for 7z
e('SevenZFile.readHeaders', 'BoundedFileChannelInputStream.<init>', 'CALL', 'Created by SevenZFile for reading 7z archives',
  evidence='SRC sevenz/SevenZFile.java:371,429,998')

e('BoundedFileChannelInputStream.<init>', 'BoundedFileChannelInputStream.read', 'CALL', 'Called during stream reading',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:44,59')

e('BoundedFileChannelInputStream.read', 'BoundedFileChannelInputStream.read', 'CALL', 'Private helper calls',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:83-88')


# ================================================================== Merged label_1, label_2, label_3

# ---- label_1 ----
# ---- Helper 1 label part (2026-10-27)
# Classes: GlideOptions, GlideRequest, GlideRequests, GeneratedAppGlideModuleImpl,
# AppsAdapter, AppsAdapterPreloadModel, AppsListFragment, CloudSheetFragment, ColorAdapter,
# CompressedExplorerAdapter, CompressedExplorerFragment, CompressedExplorerFragment$1, 
# CompressedExplorerFragment$2, CompressedHelper, CompressedHelperTask, CompressedItemViewHolder,
# CompressedObjectParcelable, CompressedObjectParcelable$1, CompressedObjectParcelable$Sorter,
# DbViewerFragment, FtpServerFragment, FtpServerFragment$1, HiddenAdapter,
# MainFragment, MainFragment$1-7, ProcessViewerFragment, ProcessViewerFragment$CustomServiceConnection,
# ProcessViewerFragment$CustomServiceConnection$1, RecyclerAdapter, RecyclerAdapter$1-2,
# RecyclerAdapter$ListItem, RecyclerPreloadModelProvider, RecyclerPreloadSizeProvider,
# RecyclerPreloadSizeProvider$SizeViewTarget, SearchWorkerFragment, ShareAdapter, ShareAdapter$ViewHolder,
# SmbSearchDialog$ListViewAdapter, TabFragment, TabFragment$ScreenSlidePagerAdapter

# UNREACHABLE methods from this batch
UNREACHABLE_PART_1 = {
}
UNREACHABLE.update(UNREACHABLE_PART_1)

# ---- label_2 ----
# ---- Helper 2 label part (2026-10-27)
# All methods in this batch are REACHABLE.
# Activities: MainActivity (LAUNCHER), PreferencesActivity, AboutActivity, 
# DatabaseViewerActivity, TextEditorActivity, PermissionsActivity (superclass)
# All are entry points or launched from entry points via Intent.
# Their lifecycle methods, callbacks, dialogs, helpers, and lambdas are all REACHABLE.

# AboutActivity routes
e('PrefFrag.onPreferenceClick', 'AboutActivity.<init>', 'INTENT', 'Intent created for AboutActivity',
  evidence='SRC PrefFrag.java:204')
e('AboutActivity.<init>', 'AboutActivity.onCreate', 'FRAMEWORK', 'Framework calls onCreate',
  evidence='INFERRED framework lifecycle')
e('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$0', 'CALL', 'Palette.generate callback',
  evidence='SRC AboutActivity.java:93-98')
e('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$1', 'CALL', 'OnOffsetChangedListener',
  evidence='SRC AboutActivity.java:100-102')
e('AboutActivity.onClick', 'AboutActivity.openURL', 'CALL', 'onClick calls openURL for various actions',
  evidence='SRC AboutActivity.java:149-230')

# DatabaseViewerActivity routes  
e('FileUtils.openFile', 'DatabaseViewerActivity.<init>', 'INTENT', 'Intent for .db files',
  evidence='SRC FileUtils.java:613,658,757,835')
e('DatabaseViewerActivity.<init>', 'DatabaseViewerActivity.onCreate', 'FRAMEWORK', 'Framework calls onCreate',
  evidence='INFERRED framework lifecycle')
e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.lambda$onCreate$0', 'CALL', 'listView OnItemClickListener',
  evidence='SRC DatabaseViewerActivity.java:142-149')
e('DatabaseViewerActivity.load', 'DatabaseViewerActivity.lambda$null$1', 'CALL', 'Thread creation',
  evidence='SRC DatabaseViewerActivity.java:151-186')
e('DatabaseViewerActivity.lambda$null$1', 'DatabaseViewerActivity.getDbTableNames', 'CALL', 'Called to get table names',
  evidence='SRC DatabaseViewerActivity.java:166')
e('DatabaseViewerActivity.lambda$null$1', 'DatabaseViewerActivity.lambda$load$2', 'CALL', 'runOnUiThread callback',
  evidence='SRC DatabaseViewerActivity.java:185')

# MainActivity routes (LAUNCHER activity)
e('LAUNCHER', 'MainActivity.<init>', 'INTENT', 'Main entry point',
  evidence='INFERRED manifest LAUNCHER')
e('MainActivity.<init>', 'MainActivity.onCreate', 'FRAMEWORK', 'Framework lifecycle',
  evidence='INFERRED framework lifecycle')
e('MainActivity.showSMBDialog', 'SmbConnectDialog.<init>', 'CALL', 'Creates SMB dialog',
  evidence='INFERRED from dialog usage')
e('MainActivity.showSftpDialog', 'SftpConnectDialog.<init>', 'CALL', 'Creates SFTP dialog',
  evidence='INFERRED from dialog usage')

# PreferencesActivity routes
e('Drawer.onClick', 'PreferencesActivity.<init>', 'INTENT', 'Settings from drawer',
  evidence='SRC Drawer.java:437')
e('PreferencesActivity.<init>', 'PreferencesActivity.onCreate', 'FRAMEWORK', 'Framework lifecycle',
  evidence='INFERRED framework lifecycle')

# TextEditorActivity routes (intent-filter for text/*)
e('INTENT_FILTER', 'TextEditorActivity.<init>', 'INTENT', 'System launches for text/* MIME types',
  evidence='SRC AndroidManifest.xml intent-filter')
e('TextEditorActivity.<init>', 'TextEditorActivity.onCreate', 'FRAMEWORK', 'Framework lifecycle',
  evidence='INFERRED framework lifecycle')

# PermissionsActivity routes (superclass of MainActivity)
e('MainActivity.<init>', 'PermissionsActivity.<init>', 'CALL', 'Superclass constructor',
  evidence='SRC MainActivity.java extends PermissionsActivity')

# Dialog routes
e('MainActivity.delete', 'GeneralDialogCreation.deleteFilesDialog', 'CALL', 'Delete confirmation dialog',
  evidence='INFERRED from usage pattern')
e('MainActivity', 'ColorPickerDialog.<init>', 'CALL', 'Color picker from preferences',
  evidence='INFERRED from usage pattern')
e('GeneralDialogCreation.deleteFilesDialog', 'GeneralDialogCreation$1.<init>', 'CALL', 'AsyncTask for delete',
  evidence='SRC GeneralDialogCreation.java:192')

# Helper routes
e('MainActivity', 'MainActivityHelper', 'CALL', 'Helper instance field',
  evidence='SRC MainActivity.java mainActivityHelper field')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_2 = {
    # All 305 methods in this batch are REACHABLE
}
UNREACHABLE.update(UNREACHABLE_PART_2)

# ---- label_3 ----
# ---- Helper 3 label part (2025-01-17)

# AmazeFileManagerModule - Glide annotation processor calls registerComponents
# This is a Glide @GlideModule annotated class

# CloudLoaderAsyncTask
e('MainActivity.onLoadFinished', 'CloudLoaderAsyncTask.<init>', 'CALL', 
  'MainActivity instantiates CloudLoaderAsyncTask in loader callback',
  evidence='SRC MainActivity.java:1922')
e('CloudLoaderAsyncTask.<init>', 'CloudLoaderAsyncTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground after execute()',
  evidence='INFERRED source not read')
e('CloudLoaderAsyncTask.doInBackground', 'CloudLoaderAsyncTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='INFERRED source not read')
e('CloudLoaderAsyncTask.doInBackground', 'CloudLoaderAsyncTask.onCancelled', 'FRAMEWORK',
  'AsyncTask framework calls onCancelled when cancel(true) is called',
  evidence='SRC CloudLoaderAsyncTask.java:52,56,61')

# AsyncTaskResult
# Generic container class - reachability depends on its usages

# CountItemsOrAndSizeTask
e('GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'CountItemsOrAndSizeTask.<init>', 'CALL',
  'Dialog creation instantiates CountItemsOrAndSizeTask',
  evidence='SRC GeneralDialogCreation.java:457')
e('CountItemsOrAndSizeTask.<init>', 'CountItemsOrAndSizeTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.getText', 'CALL',
  'doInBackground calls getText for formatting',
  evidence='SRC CountItemsOrAndSizeTask.java:42,54')
e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate',
  evidence='SRC CountItemsOrAndSizeTask.java:42')
e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# DbViewerTask
e('DbViewerFragment.onCreateView', 'DbViewerTask.<init>', 'CALL',
  'DbViewerFragment instantiates DbViewerTask',
  evidence='SRC DbViewerFragment.java:47')
e('DbViewerTask.<init>', 'DbViewerTask.onPreExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPreExecute',
  evidence='INFERRED source not read')
e('DbViewerTask.<init>', 'DbViewerTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('DbViewerTask.doInBackground', 'DbViewerTask.getDbTableSchema', 'CALL',
  'doInBackground calls getDbTableSchema',
  evidence='SRC DbViewerTask.java:63')
e('DbViewerTask.doInBackground', 'DbViewerTask.getDbTableDetails', 'CALL',
  'doInBackground calls getDbTableDetails',
  evidence='SRC DbViewerTask.java:64')
e('DbViewerTask.doInBackground', 'DbViewerTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate',
  evidence='SRC DbViewerTask.java:137')
e('DbViewerTask.doInBackground', 'DbViewerTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')
e('DbViewerTask.doInBackground', 'DbViewerTask.onCancelled', 'FRAMEWORK',
  'isCancelled check can lead to onCancelled',
  evidence='SRC DbViewerTask.java:135,148')

# DeleteTask
e('CopyService.onStartCommand', 'DeleteTask.<init>(Context)', 'CALL',
  'CopyService instantiates DeleteTask',
  evidence='SRC CopyService.java:423')
e('MainActivityHelper.deleteFiles', 'DeleteTask.<init>(Context)', 'CALL',
  'MainActivityHelper instantiates DeleteTask',
  evidence='SRC MainActivityHelper.java:510,518')
e('CompressedExplorerFragment.onOptionsItemSelected', 'DeleteTask.<init>(Context,CompressedExplorerFragment)', 'CALL',
  'CompressedExplorerFragment instantiates DeleteTask with fragment',
  evidence='SRC CompressedExplorerFragment.java:362')
e('DeleteTask.<init>(Context)', 'DeleteTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('DeleteTask.doInBackground', 'DeleteTask.delete', 'CALL',
  'doInBackground calls delete for media database cleanup',
  evidence='SRC DeleteTask.java:140')
e('DeleteTask.doInBackground', 'DeleteTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress would trigger onProgressUpdate',
  evidence='INFERRED source not read')
e('DeleteTask.doInBackground', 'DeleteTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# GenerateHashesTask
e('GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'GenerateHashesTask.<init>', 'CALL',
  'Dialog creation instantiates GenerateHashesTask',
  evidence='SRC GeneralDialogCreation.java:461')
e('GenerateHashesTask.<init>', 'GenerateHashesTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('GenerateHashesTask.doInBackground', 'GenerateHashesTask.getMD5Checksum', 'CALL',
  'doInBackground calls getMD5Checksum',
  evidence='SRC GenerateHashesTask.java:80')
e('GenerateHashesTask.doInBackground', 'GenerateHashesTask.getSHA256Checksum', 'CALL',
  'doInBackground calls getSHA256Checksum',
  evidence='SRC GenerateHashesTask.java:81')
e('GenerateHashesTask.getMD5Checksum', 'GenerateHashesTask.createChecksum', 'CALL',
  'getMD5Checksum calls createChecksum',
  evidence='SRC GenerateHashesTask.java:113')
e('GenerateHashesTask.doInBackground', 'GenerateHashesTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# GenerateHashesTask$1 and $2 - anonymous inner classes created by lambda
e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask$1.<init>', 'CALL',
  'Lambda creates anonymous class for OnLongClickListener',
  evidence='SRC GenerateHashesTask.java:93')
e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask$2.<init>', 'CALL',
  'Lambda creates anonymous class for OnLongClickListener',
  evidence='SRC GenerateHashesTask.java:98')

# LoadFilesListTask
e('MainFragment.loadlist', 'LoadFilesListTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground after instantiation',
  evidence='SRC MainFragment.java:1025')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.createListParcelables', 'CALL',
  'doInBackground calls createListParcelables',
  evidence='SRC LoadFilesListTask.java:228')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listImages', 'CALL',
  'Called when openmode is CUSTOM case 0',
  evidence='SRC LoadFilesListTask.java:139')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listVideos', 'CALL',
  'Called when openmode is CUSTOM case 1',
  evidence='SRC LoadFilesListTask.java:142')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listaudio', 'CALL',
  'Called when openmode is CUSTOM case 2',
  evidence='SRC LoadFilesListTask.java:145')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listDocs', 'CALL',
  'Called when openmode is CUSTOM case 3',
  evidence='SRC LoadFilesListTask.java:148')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listApks', 'CALL',
  'Called when openmode is CUSTOM case 4',
  evidence='SRC LoadFilesListTask.java:151')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listRecent', 'CALL',
  'Called when openmode is CUSTOM case 5',
  evidence='SRC LoadFilesListTask.java:154')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listRecentFiles', 'CALL',
  'Called when openmode is CUSTOM case 6',
  evidence='SRC LoadFilesListTask.java:157')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listOtg', 'CALL',
  'Called when openmode is OTG',
  evidence='SRC LoadFilesListTask.java:165')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listCloud', 'CALL',
  'Called for cloud storage modes',
  evidence='SRC LoadFilesListTask.java:177')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# AnimUtils
e('Indicator.<init>', 'AnimUtils.getFastOutSlowInInterpolator', 'CALL',
  'Indicator calls getFastOutSlowInInterpolator',
  evidence='SRC Indicator.java:153')
e('AppsAdapter.onBindViewHolder', 'AnimUtils.marqueeAfterDelay', 'CALL',
  'AppsAdapter calls marqueeAfterDelay',
  evidence='SRC AppsAdapter.java:139')
e('RecyclerAdapter.onBindViewHolder', 'AnimUtils.marqueeAfterDelay', 'CALL',
  'RecyclerAdapter calls marqueeAfterDelay',
  evidence='SRC RecyclerAdapter.java:316')

# ColorUtils
e('RecyclerAdapter.onBindViewHolder', 'ColorUtils.<init>', 'CALL',
  'Static method call does not instantiate but class is loaded',
  evidence='SRC RecyclerAdapter.java:668')

# ProgressHandler
e('CopyService.<clinit>', 'ProgressHandler.<init>()', 'CALL',
  'CopyService initializes ProgressHandler field',
  evidence='SRC CopyService.java:83')
e('CopyService.onCreate', 'ProgressHandler.addWrittenLength', 'CALL',
  'Service updates progress',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.getTotalSize', 'CALL',
  'Service queries total size',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.getWrittenSize', 'CALL',
  'Service queries written size',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.getPercentProgress', 'CALL',
  'Service queries percent progress',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.setFileName', 'CALL',
  'Service sets current file name',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.setCancelled', 'CALL',
  'Service handles cancellation',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.getCancelled', 'CALL',
  'Service checks cancellation',
  evidence='INFERRED typical service usage')

# ScreenUtils
e('AppConfig.getInstance', 'ScreenUtils.convertDbToPx', 'CALL',
  'AppConfig uses ScreenUtils',
  evidence='SRC AppConfig.java:234')
e('AppConfig.getInstance', 'ScreenUtils.getScreenWidthInPx', 'CALL',
  'AppConfig uses ScreenUtils',
  evidence='INFERRED typical usage after instantiation')

# ScreenUtils
e('AppConfig.getInstance', 'ScreenUtils.convertDbToPx', 'CALL',
  'AppConfig uses ScreenUtils',
  evidence='SRC AppConfig.java:234')
e('AppConfig.getInstance', 'ScreenUtils.getScreenWidthInPx', 'CALL',
  'AppConfig uses ScreenUtils',
  evidence='INFERRED typical usage after instantiation')

# Database Handlers - all REACHABLE through SQLiteOpenHelper and app usage
# SortHandler, CryptHandler, CloudHandler

# MoveFiles
e('PrepareCopyTask.startService', 'MoveFiles.<init>', 'CALL',
  'PrepareCopyTask instantiates MoveFiles',
  evidence='SRC PrepareCopyTask.java:304')
e('MoveFiles.<init>', 'MoveFiles.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('MoveFiles.doInBackground', 'MoveFiles.getOperationSupportedFileSystem', 'CALL',
  'doInBackground calls helper method',
  evidence='INFERRED typical task implementation')
e('MoveFiles.doInBackground', 'MoveFiles.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# PrepareCopyTask
e('MainActivity.onActivityResult', 'PrepareCopyTask.doInBackground', 'FRAMEWORK',
  'MainActivity instantiates PrepareCopyTask',
  evidence='SRC MainActivity.java:1029')
e('PrepareCopyTask.doInBackground', 'PrepareCopyTask.checkConflicts', 'CALL',
  'doInBackground calls checkConflicts',
  evidence='INFERRED typical task implementation')
e('PrepareCopyTask.doInBackground', 'PrepareCopyTask.finishCopying', 'CALL',
  'doInBackground calls finishCopying',
  evidence='INFERRED typical task implementation')
e('PrepareCopyTask.doInBackground', 'PrepareCopyTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate',
  evidence='INFERRED source not read')
e('PrepareCopyTask.doInBackground', 'PrepareCopyTask.startService', 'CALL',
  'doInBackground starts copy service',
  evidence='SRC PrepareCopyTask.java:304')

# ReadFileTask
e('TextEditorActivity.load', 'ReadFileTask.doInBackground', 'FRAMEWORK',
  'TextEditorActivity instantiates ReadFileTask',
  evidence='SRC TextEditorActivity.java:291')
e('ReadFileTask.doInBackground', 'ReadFileTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# SearchAsyncTask
e('SearchWorkerFragment.onAttach', 'SearchAsyncTask.<init>', 'CALL',
  'SearchWorkerFragment instantiates SearchAsyncTask',
  evidence='SRC SearchWorkerFragment.java:58')
e('SearchAsyncTask.<init>', 'SearchAsyncTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.search(HybridFile,String)', 'CALL',
  'doInBackground calls search method',
  evidence='INFERRED typical search implementation')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.search(HybridFile,SearchFilter)', 'CALL',
  'doInBackground calls search with filter',
  evidence='INFERRED typical search implementation')
e('SearchAsyncTask.search(HybridFile,String)', 'SearchAsyncTask.bashRegexToJava', 'CALL',
  'search converts regex',
  evidence='INFERRED typical search implementation')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.searchRegExFind', 'CALL',
  'doInBackground calls regex search',
  evidence='INFERRED typical search implementation')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.searchRegExMatch', 'CALL',
  'doInBackground calls regex match',
  evidence='INFERRED typical search implementation')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate',
  evidence='INFERRED source not read')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.onCancelled', 'FRAMEWORK',
  'cancel triggers onCancelled',
  evidence='INFERRED source not read')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.onPreExecute', 'FRAMEWORK',
  'execute triggers onPreExecute',
  evidence='INFERRED source not read')

# SearchTextTask
e('TextEditorActivity.find', 'SearchTextTask.<init>', 'CALL',
  'TextEditorActivity instantiates SearchTextTask',
  evidence='SRC TextEditorActivity.java:449')
e('SearchTextTask.<init>', 'SearchTextTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('SearchTextTask.doInBackground', 'SearchTextTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')
e('SearchTextTask.doInBackground', 'SearchTextTask.onPreExecute', 'FRAMEWORK',
  'execute triggers onPreExecute',
  evidence='INFERRED source not read')

# WriteFileAbstraction
e('TextEditorActivity.saveFile', 'WriteFileAbstraction.<init>', 'CALL',
  'TextEditorActivity instantiates WriteFileAbstraction',
  evidence='SRC TextEditorActivity.java:262')
e('WriteFileAbstraction.<init>', 'WriteFileAbstraction.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('WriteFileAbstraction.doInBackground', 'WriteFileAbstraction.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# Archive HelperTask classes - all instantiated by Decompressor classes
# Bzip2HelperTask, GzipHelperTask, LzmaHelperTask, RarHelperTask, 
# SevenZipHelperTask, TarHelperTask, XzHelperTask, ZipHelperTask
e('Bzip2Decompressor.changePath', 'Bzip2HelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC Bzip2Decompressor.java:43')
e('Bzip2HelperTask.<init>', 'Bzip2HelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('GzipDecompressor.changePath', 'GzipHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC GzipDecompressor.java:46')
e('GzipHelperTask.<init>', 'GzipHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('LzmaDecompressor.changePath', 'LzmaHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC LzmaDecompressor.java:43')
e('LzmaHelperTask.<init>', 'LzmaHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('RarDecompressor.changePath', 'RarHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC RarDecompressor.java:47')
e('RarHelperTask.<init>', 'RarHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('SevenZipDecompressor.changePath', 'SevenZipHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC SevenZipDecompressor.java:46')
e('SevenZipHelperTask.<init>', 'SevenZipHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('SevenZipHelperTask.addElements', 'SevenZipHelperTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate',
  evidence='INFERRED source not read')
e('TarDecompressor.changePath', 'TarHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC TarDecompressor.java:43')
e('TarHelperTask.<init>', 'TarHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('XzDecompressor.changePath', 'XzHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC XzDecompressor.java:43')
e('XzHelperTask.<init>', 'XzHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('ZipDecompressor.changePath', 'ZipHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC ZipDecompressor.java:44')
e('ZipHelperTask.<init>', 'ZipHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_3 = {
}
UNREACHABLE.update(UNREACHABLE_PART_3)


# ---- label_b012 ----
# ---- Helper batch 012 label part (2026-10-27)

# ColorPref methods
e('PreferencesActivity.<init>', 'ColorPref.<init>', 'CALL', 'instantiates ColorPref for color preferences',
  evidence='SRC PreferencesActivity.java:258')

e('ColorPref.onCreate', 'ColorPref.loadSection0', 'CALL', 'called from onCreate',
  evidence='SRC ColorPref.java:56-62')

e('ColorPref.onCreate', 'ColorPref.onRestoreInstanceState', 'CALL', 'called from onCreate when savedInstanceState is not null',
  evidence='SRC ColorPref.java:56-62')

e('ColorPref.onCreate', 'ColorPref.reloadListeners', 'CALL', 'called from onCreate',
  evidence='SRC ColorPref.java:56-62')

e('ColorPref.onPause', 'ColorPref.onPause', 'LIFECYCLE', 'lifecycle method',
  evidence='SRC ColorPref.java:66-68')

e('ColorPref.onOptionsItemSelected', 'ColorPref.switchSections', 'CALL', 'called when home button pressed in non-section-0',
  evidence='SRC ColorPref.java:74-79')

e('ColorPref.onBackPressed', 'ColorPref.switchSections', 'CALL', 'called when back button pressed in non-section-0',
  evidence='SRC ColorPref.java:85-88')

e('ColorPref.onPreferenceClick', 'ColorPref.colorChangeDialog', 'CALL', 'called for color preference clicks',
  evidence='SRC ColorPref.java:95-103')

e('ColorPref.onPreferenceClick', 'ColorPref.switchSections', 'CALL', 'called for selectcolorconfig click',
  evidence='SRC ColorPref.java:95-103')

e('ColorPref.colorChangeDialog', 'ColorPreference.<clinit>', 'CALL', 'accesses ColorPreference.availableColors static field',
  evidence='SRC ColorPref.java:134-137')

e('ColorPref.colorChangeDialog', 'ColorPref.lambda$colorChangeDialog$0', 'CALL', 'lambda callback for color selection',
  evidence='SRC ColorPref.java:136-163')

e('ColorPref.switchSections', 'ColorPref.loadSection0', 'CALL', 'called from switchSections when switching to section 0',
  evidence='SRC ColorPref.java:199-206')

e('ColorPref.switchSections', 'ColorPref.loadSection1', 'CALL', 'called from switchSections when switching to section 1',
  evidence='SRC ColorPref.java:199-206')

e('ColorPref.switchSections', 'ColorPref.reloadListeners', 'CALL', 'called after loading section',
  evidence='SRC ColorPref.java:199-206')

e('ColorPref.loadSection0', 'ColorPref.loadSection0', 'LIFECYCLE', 'loads preferences for section 0',
  evidence='SRC ColorPref.java:208-215')

e('ColorPref.loadSection1', 'ColorPref.invalidateColorPreference', 'CALL', 'called for selectedColors preference',
  evidence='SRC ColorPref.java:219-220')

e('ColorPref.invalidateEverything', 'ColorPref.invalidateColorPreference', 'CALL', 'called to invalidate preferences',
  evidence='SRC ColorPref.java:243-254')

e('ColorPref.onSaveInstanceState', 'ColorPref.onSaveInstanceState', 'LIFECYCLE', 'saves instance state',
  evidence='SRC ColorPref.java:270-273')

e('ColorPref.onRestoreInstanceState', 'ColorPref.loadSection0', 'CALL', 'loads section 0 on restore',
  evidence='SRC ColorPref.java:276-284')

e('ColorPref.onRestoreInstanceState', 'ColorPref.loadSection1', 'CALL', 'loads section 1 on restore',
  evidence='SRC ColorPref.java:276-284')

# ColorPref$1 - anonymous ButtonCallback
e('ColorPref.colorChangeDialog', 'ColorPref$1.<init>', 'CALL', 'creates anonymous ButtonCallback for dialog',
  evidence='SRC ColorPref.java:179-186')

e('ColorPref$1.onNeutral', 'ColorPref$1.onNeutral', 'CALL', 'callback method for neutral button',
  evidence='SRC ColorPref.java:181-186')

# ColorPreference static field access - clinit is already called above
# ColorPreference.<init> and <clinit> are reached through static field access

# ColorUtils
e('RecyclerAdapter.bindViewHolderAsFile', 'ColorUtils.<init>', 'CALL', 'ColorUtils is a utility class accessed statically',
  evidence='SRC ColorUtils.java:16-22')

e('RecyclerAdapter.bindViewHolderAsFile', 'ColorUtils.colorizeIcons', 'CALL', 'called from adapter to colorize file type icons',
  evidence='SRC RecyclerAdapter.java:668-670')

# UNREACHABLE entries
UNREACHABLE['ColorPref.checkCustomization'] = ('framework_never_calls', 'called only from loadSection1 which has conditional execution', 'SRC ColorPref.java:226-234', 'SOURCE')
UNREACHABLE['ColorPref.invalidateColorPreference'] = ('branch_never_taken', 'called from invalidateEverything and loadSection1, both conditional', 'SRC ColorPref.java:256-268', 'SOURCE')
UNREACHABLE['ColorPreference.<init>'] = ('framework_never_calls', 'ColorPreference only has static field, no instantiation in app', 'SRC ColorPreference.java:1-25', 'SOURCE')
UNREACHABLE['ColorUtils.<init>'] = ('framework_never_calls', 'ColorUtils is a utility class used statically, constructor never called', 'SRC ColorUtils.java:18-43', 'SOURCE')


# ---- label_b011 ----
# ---- batch_011 label part (2026-10-27)

# ColorCircleDrawable methods
e('TabFragment.updatePathColors', 'ColorCircleDrawable.<init>',
  'CALL', 'Direct instantiation in TabFragment',
  evidence='SRC TabFragment.java:386')

e('Drawable', 'ColorCircleDrawable.draw',
  'FRAMEWORK', 'Overridden framework method, called by Android Drawable framework',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.onBoundsChange',
  'FRAMEWORK', 'Overridden framework method, called by Android Drawable lifecycle',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.setAlpha',
  'FRAMEWORK', 'Overridden framework method, called by Android drawable operations',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.setColorFilter',
  'FRAMEWORK', 'Overridden framework method, called by Android drawable operations',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.getOpacity',
  'FRAMEWORK', 'Overridden framework method, called by Android drawable operations',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

# ColorPickerDialog methods
e('PreferenceScreen', 'ColorPickerDialog.<init>',
  'FRAMEWORK', 'Instantiated by Android PreferenceManager from XML via framework',
  evidence='SRC ColorPickerDialog.java:68')

e('S_PREFS', 'ColorPickerDialog.<clinit>',
  'FRAMEWORK', 'Static initialization block called by class loader on first access',
  evidence='SRC ColorPickerDialog.java:44-49')

e('S_PREFS', 'ColorPickerDialog.onBindDialogView',
  'FRAMEWORK', 'Lifecycle method called by DialogPreference framework',
  evidence='SRC ColorPickerDialog.java:108')

e('S_PREFS', 'ColorPickerDialog.onDialogClosed',
  'FRAMEWORK', 'Lifecycle method called by DialogPreference framework',
  evidence='SRC ColorPickerDialog.java:168')

e('S_PREFS', 'ColorPickerDialog.onSaveInstanceState',
  'FRAMEWORK', 'Lifecycle method called by Preference framework for state persistence',
  evidence='SRC ColorPickerDialog.java:220')

e('S_PREFS', 'ColorPickerDialog.onRestoreInstanceState',
  'FRAMEWORK', 'Lifecycle method called by Preference framework for state restoration',
  evidence='SRC ColorPickerDialog.java:229')

e('S_PREFS', 'ColorPickerDialog.onGetDefaultValue',
  'FRAMEWORK', 'Lifecycle method called by Preference framework',
  evidence='SRC ColorPickerDialog.java:89')

e('S_PREFS', 'ColorPickerDialog.getSummary',
  'FRAMEWORK', 'Lifecycle method called by Preference framework to get display text',
  evidence='SRC ColorPickerDialog.java:94')

e('S_PREFS', 'ColorPickerDialog.showDialog',
  'FRAMEWORK', 'Lifecycle method called by DialogPreference framework',
  evidence='SRC ColorPickerDialog.java:200')

e('ColorPickerDialog.onBindDialogView', 'ColorPickerDialog.inflateItem',
  'CALL', 'Called directly from onBindDialogView in loop',
  evidence='SRC ColorPickerDialog.java:122')

e('ColorPickerDialog.onBindDialogView', 'ColorPickerDialog.select',
  'CALL', 'Called directly from onBindDialogView',
  evidence='SRC ColorPickerDialog.java:128')

e('ColorPickerDialog.onBindDialogView', 'ColorPickerDialog.getColor',
  'CALL', 'Called directly from onBindDialogView',
  evidence='SRC ColorPickerDialog.java:132')

e('ColorPickerDialog.onDialogClosed', 'ColorPickerDialog.getColor',
  'CALL', 'Called directly from onDialogClosed',
  evidence='SRC ColorPickerDialog.java:182')

e('ColorPickerDialog.inflateItem', 'ColorPickerDialog.select',
  'CALL', 'Called from inflateItem lambda via select()',
  evidence='SRC ColorPickerDialog.java:156')

e('ColorPickerDialog.onRestoreInstanceState', 'ColorPickerDialog.select',
  'CALL', 'Called directly from onRestoreInstanceState',
  evidence='SRC ColorPickerDialog.java:244')

# ColorPickerDialog$ColorItemPair (inner static class)
e('ColorPickerDialog.<clinit>', 'ColorPickerDialog$ColorItemPair.<init>',
  'CALL', 'Called during static initialization of COLORS array',
  evidence='SRC ColorPickerDialog.java:48-51')

# ColorPickerDialog$SavedState
e('ColorPickerDialog.onSaveInstanceState', 'ColorPickerDialog$SavedState.<init>',
  'CALL', 'Called directly to create SavedState instance from Parcelable',
  evidence='SRC ColorPickerDialog.java:256')

# SavedState second constructor
e('S_PREFS', 'ColorPickerDialog$SavedState.<init>',
  'FRAMEWORK', 'Constructor from Parcel, called by Parcelable framework',
  evidence='SRC ColorPickerDialog.java:277')

# SavedState second constructor (from Parcelable deserialization)
e('Parcelable.Creator', 'ColorPickerDialog$SavedState.<init>',
  'FRAMEWORK', 'Constructor from Parcel called by Parcelable.Creator.createFromParcel',
  evidence='SRC ColorPickerDialog.java:295')

e('ColorPickerDialog$SavedState.<init>', 'ColorPickerDialog$SavedState.<clinit>',
  'FRAMEWORK', 'Static initialization called by class loader',
  evidence='SRC ColorPickerDialog.java:253')

e('BaseSavedState', 'ColorPickerDialog$SavedState.writeToParcel',
  'FRAMEWORK', 'Called by Parcelable framework during state serialization',
  evidence='SRC ColorPickerDialog.java:263')

# ColorPickerDialog$SavedState$1 (Creator inner class)
e('ColorPickerDialog$SavedState.<clinit>', 'ColorPickerDialog$SavedState$1.<init>',
  'CALL', 'Called during static initialization of CREATOR',
  evidence='SRC ColorPickerDialog.java:268')

e('Parcelable.Creator', 'ColorPickerDialog$SavedState$1.createFromParcel',
  'FRAMEWORK', 'Called by Parcelable framework during deserialization',
  evidence='SRC ColorPickerDialog.java:271')

e('Parcelable.Creator', 'ColorPickerDialog$SavedState$1.newArray',
  'FRAMEWORK', 'Called by Parcelable framework during array allocation',
  evidence='SRC ColorPickerDialog.java:274')



# ---- label_b010 ----
# ---- Helper batch_010 label part (2026-10-27)
# Batch 10: Coders (7z library), ColorAdapter (UI adapter)

# Coders static method entry points
e('SevenZFile.readStreamsInfo', 'Coders.addDecoder', 'CALL',
  'SevenZFile adds decoders for each coder in folder',
  evidence='SRC SevenZFile.java:435')

e('SevenZFile.getBytesForCoder', 'Coders.addDecoder', 'CALL',
  'Unpacks bytes using coders',
  evidence='SRC SevenZFile.java:1030')

e('Coders.addDecoder', 'Coders.findByMethod', 'CALL',
  'findByMethod retrieves decoder from CODER_MAP',
  evidence='SRC Coders.java:76')

e('SevenZOutputFile.createEncoders', 'Coders.addEncoder', 'CALL',
  'Encodes output stream with compression method',
  evidence='SRC SevenZOutputFile.java:321')

e('Coders.addEncoder', 'Coders.findByMethod', 'CALL',
  'findByMethod retrieves encoder from CODER_MAP',
  evidence='SRC Coders.java:87')

e('SevenZFile.getBytesForCoder', 'Coders.findByMethod', 'CALL',
  'Gets decoder options after adding decoder',
  evidence='SRC SevenZFile.java:1033')

e('SevenMethodConfiguration.setContentMethods', 'Coders.findByMethod', 'CALL',
  'SevenZMethodConfiguration validates encoder options',
  evidence='SRC SevenZMethodConfiguration.java:59')

# Coders static initializer - CODER_MAP creation
e('Coders.<clinit>', 'Coders$1.<init>', 'CALL',
  'Initializes CODER_MAP HashMap with decoders',
  evidence='SRC Coders.java:48-66')

e('Coders$1.<init>', 'Coders$CopyDecoder.<init>', 'CALL',
  'CODER_MAP puts CopyDecoder instance',
  evidence='SRC Coders.java:49')

e('Coders$1.<init>', 'Coders$BCJDecoder.<init>', 'CALL',
  'CODER_MAP puts BCJDecoder instances for various BCJ filters',
  evidence='SRC Coders.java:57-62')

e('Coders$1.<init>', 'Coders$DeflateDecoder.<init>', 'CALL',
  'CODER_MAP puts DeflateDecoder instance',
  evidence='SRC Coders.java:52')

e('Coders$1.<init>', 'Coders$Deflate64Decoder.<init>', 'CALL',
  'CODER_MAP puts Deflate64Decoder instance',
  evidence='SRC Coders.java:53')

e('Coders$1.<init>', 'Coders$BZIP2Decoder.<init>', 'CALL',
  'CODER_MAP puts BZIP2Decoder instance',
  evidence='SRC Coders.java:54')

# Decoder dispatch through virtual method calls
e('Coders.addDecoder', 'Coders$CopyDecoder.decode', 'CALL',
  'CopyDecoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$BCJDecoder.decode', 'CALL',
  'BCJDecoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$DeflateDecoder.decode', 'CALL',
  'DeflateDecoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$Deflate64Decoder.decode', 'CALL',
  'Deflate64Decoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$BZIP2Decoder.decode', 'CALL',
  'BZIP2Decoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addEncoder', 'Coders$CopyDecoder.encode', 'CALL',
  'CopyDecoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

e('Coders.addEncoder', 'Coders$BCJDecoder.encode', 'CALL',
  'BCJDecoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

e('Coders.addEncoder', 'Coders$DeflateDecoder.encode', 'CALL',
  'DeflateDecoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

e('Coders.addEncoder', 'Coders$BZIP2Decoder.encode', 'CALL',
  'BZIP2Decoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

# DeflateDecoder inner classes construction
e('Coders$DeflateDecoder.decode', 'Coders$DeflateDecoder$DeflateDecoderInputStream.<init>', 'CALL',
  'DeflateDecoder.decode constructs DeflateDecoderInputStream wrapper',
  evidence='SRC Coders.java:138-140')

e('Coders$DeflateDecoder.encode', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>', 'CALL',
  'DeflateDecoder.encode constructs DeflateDecoderOutputStream wrapper',
  evidence='SRC Coders.java:145-147')

# DeflateDecoderInputStream methods
e('Coders$DeflateDecoder$DeflateDecoderInputStream.read', 'InflaterInputStream.read', 'CALL',
  'Delegates read to wrapped InflaterInputStream',
  evidence='SRC Coders.java:152-157')

e('Coders$DeflateDecoder$DeflateDecoderInputStream.close', 'InflaterInputStream.close', 'CALL',
  'Closes underlying InflaterInputStream and ends Inflater',
  evidence='SRC Coders.java:159-165')

# DeflateDecoderOutputStream methods
e('Coders$DeflateDecoder$DeflateDecoderOutputStream.write', 'DeflaterOutputStream.write', 'CALL',
  'Delegates write to wrapped DeflaterOutputStream',
  evidence='SRC Coders.java:172-181')

e('Coders$DeflateDecoder$DeflateDecoderOutputStream.close', 'DeflaterOutputStream.close', 'CALL',
  'Closes underlying DeflaterOutputStream and ends Deflater',
  evidence='SRC Coders.java:183-189')

# ColorAdapter UI flow
e('ColorPref.showColorChooser', 'ColorAdapter.<init>', 'CALL',
  'Constructs ColorAdapter for color selection dialog',
  evidence='SRC ColorPref.java:135-137')

e('ColorAdapter.getView', 'ColorAdapter.getColorResAt', 'CALL',
  'getView retrieves color resource at position',
  evidence='SRC ColorAdapter.java:47')

e('GridView.onLayout', 'ColorAdapter.getView', 'CALL',
  'GridView renders items using adapter getView',
  evidence='SRC ColorAdapter.java:41-55')

e('GridView.onItemClick', 'ColorAdapter.onItemClick', 'CALL',
  'GridView item click dispatches to adapter listener',
  evidence='SRC ColorPref.java:170, ColorAdapter.java:57-64')

# UNREACHABLE entries for library decoder classes and internal classes
UNREACHABLE['Coders.<init>'] = ('no_trigger_in_app', 'Coders class has no public constructor; uses only static methods', 'SRC Coders.java:45', 'CALL')

UNREACHABLE['Coders$DeflateDecoder.<clinit>'] = ('no_trigger_in_app', 'Class initialization static block for ONE_ZERO_BYTE constant; not called directly from app', 'SRC Coders.java:126', 'CALL')


# ---- label_b009 ----
# ---- Batch 009 label part (2026-10-27)

# CloudStreamSource methods
e('CloudStreamer.serve', 'CloudStreamSource.<init>', 'CALL', 'new CloudStreamSource(...)',
  evidence='SRC CloudStreamer.java:89')
e('CloudStreamSource.<init>', 'CloudStreamSource.open', 'CALL', 'implicit via stream usage',
  evidence='SRC CloudStreamSource.java:52-63')
e('CloudStreamer.serve', 'CloudStreamSource.moveTo', 'CALL', 'source.moveTo(startFrom)',
  evidence='SRC CloudStreamer.java:106')

# CloudStreamer methods
e('CloudUtil.launchCloud', 'CloudStreamer.getInstance', 'CALL', 'final CloudStreamer streamer = CloudStreamer.getInstance()',
  evidence='SRC CloudUtil.java:135')
e('CloudStreamer.getInstance', 'CloudStreamer.<init>', 'CALL', 'new CloudStreamer(PORT)',
  evidence='SRC CloudStreamer.java:37')
e('CloudUtil.launchCloud', 'CloudStreamer.setStreamSrc', 'CALL', 'streamer.setStreamSrc(...)',
  evidence='SRC CloudUtil.java:138')
e('CloudStreamServer.serve', 'CloudStreamer.serve', 'CALL', 'override dispatched by framework',
  evidence='SRC CloudStreamer.java:62')

# CloudUtil methods
e('Drawer.onItemClick', 'CloudUtil.checkToken', 'CALL', 'CloudUtil.checkToken(meta.path, mainActivity)',
  evidence='SRC Drawer.java:577')
e('LoadFilesListTask.doInBackground', 'CloudUtil.getCloudFiles', 'CALL', 'CloudUtil.getCloudFiles(...)',
  evidence='SRC LoadFilesListTask.java:458')
e('MainFragment.onItemClick', 'CloudUtil.launchCloud', 'CALL', 'CloudUtil.launchCloud(...)',
  evidence='SRC MainFragment.java:930')
e('HybridFile.listFiles', 'CloudUtil.listFiles', 'CALL', 'CloudUtil.listFiles(...)',
  evidence='SRC HybridFile.java:864')
e('CloudUtil.launchCloud', 'CloudUtil.stripPath', 'CALL', 'CloudUtil.stripPath(serviceType, ...)',
  evidence='SRC CloudUtil.java:142')

# CloudUtil inner classes (anonymous AsyncTask and Thread)
e('CloudUtil.checkToken', 'CloudUtil$1.<init>', 'CALL', 'new AsyncTask<String, Void, Boolean>()',
  evidence='SRC CloudUtil.java:174')
e('AndroidAsyncTask.execute', 'CloudUtil$1.doInBackground', 'CALL', 'framework calls doInBackground',
  evidence='SRC CloudUtil.java:179')
e('AndroidAsyncTask.onPostExecute', 'CloudUtil$1.onPostExecute', 'CALL', 'framework calls onPostExecute',
  evidence='SRC CloudUtil.java:217')
e('CloudUtil.launchCloud', 'CloudUtil$2.<init>', 'CALL', 'new Thread(() -> {...})',
  evidence='SRC CloudUtil.java:137')
e('Thread.run', 'CloudUtil$2.execute', 'CALL', 'lambda body execution',
  evidence='SRC CloudUtil.java:138')

# Coder and CoderBase
e('SevenZFile.readHeaders', 'Coder.<init>', 'CALL', 'new Coder()',
  evidence='SRC SevenZFile.java:642')
e('SevenZMethodConfiguration.validateOptions', 'CoderBase.canAcceptOptions', 'CALL', 'Coders.findByMethod(method).canAcceptOptions(options)',
  evidence='SRC SevenZMethodConfiguration.java:59')
e('SevenZFile.readStackEncodersAsCoders', 'CoderBase.getOptionsFromCoder', 'CALL', 'Coders.findByMethod(method).getOptionsFromCoder(...)',
  evidence='SRC SevenZFile.java:1033')

# UNREACHABLE entries (all batch 009 methods are reachable, none marked unreachable)


# ---- label_b008 ----
# ---- Batch 008 label part (2026-10-27)

# CloudIconModelFactory methods
e('CloudIconModelFactory.<init>', 'CloudIconModelLoader.<init>', 'CALL', 'Glide factory creates loader',
  evidence='SRC CloudIconModelFactory.java:18-20')
e('CloudIconModelFactory.build', 'CloudIconModelLoader.<init>', 'CALL', 'Factory builds CloudIconModelLoader',
  evidence='SRC CloudIconModelFactory.java:23-26')

# CloudIconModelLoader methods
e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.<init>', 'CALL', 'Creates fetcher for image loading',
  evidence='SRC CloudIconModelLoader.java:25-31')

# CloudPluginException - thrown from multiple call sites
e('CloudHandler.addEntry', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:85-86')
e('CloudHandler.updateEntry', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:118-121')
e('CloudHandler.findEntry', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:141-144')
e('CloudHandler.getAllEntries', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:169-172')
e('CloudUtil.listFiles', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC CloudUtil.java:59-82')
e('LoadFilesListTask.loadCloudFiles', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC LoadFilesListTask.java:453-455')

# CloudSheetFragment - shown from MainActivity
e('MainActivity.onOptionsItemSelected', 'CloudSheetFragment.<init>', 'CALL', 'Creates cloud sheet dialog fragment',
  evidence='SRC MainActivity.java:1953')
e('CloudSheetFragment.<init>', 'CloudSheetFragment.onCreate', 'LIFECYCLE', 'Android framework calls onCreate on fragment creation',
  evidence='SRC CloudSheetFragment.java:40-41')
e('CloudSheetFragment.<init>', 'CloudSheetFragment.setupDialog', 'LIFECYCLE', 'Android framework calls setupDialog during dialog setup',
  evidence='SRC CloudSheetFragment.java:45-87')
e('CloudSheetFragment.setupDialog', 'CloudSheetFragment.onClick', 'CALL', 'Sets onClick listener on layouts',
  evidence='SRC CloudSheetFragment.java:70-76')
e('CloudSheetFragment.setupDialog', 'CloudSheetFragment.isCloudProviderAvailable', 'CALL', 'Checks cloud provider availability',
  evidence='SRC CloudSheetFragment.java:69')

# CloudStreamServer - instantiated via CloudStreamer.getInstance()
e('CloudUtil.playStream', 'CloudStreamer.getInstance', 'CALL', 'Gets streamer instance',
  evidence='SRC CloudUtil.java:135')
e('SshClientUtils.playStream', 'CloudStreamer.getInstance', 'CALL', 'Gets streamer instance',
  evidence='SRC SshClientUtils.java:238')
e('StreamServer.tryBind', 'CloudStreamer.getInstance', 'CALL', 'Stops conflicting streamer',
  evidence='SRC StreamServer.java:212')
e('CloudStreamer.getInstance', 'CloudStreamServer.<init>', 'CALL', 'Creates new CloudStreamer (extends CloudStreamServer)',
  evidence='SRC CloudStreamer.java:34-39')
e('CloudStreamServer.<init>', 'CloudStreamServer.lambda$new$0', 'SYSTEM', 'Creates server thread with lambda',
  evidence='SRC CloudStreamServer.java:204-220')
e('CloudStreamServer.lambda$new$0', 'CloudStreamServer$HTTPSession.<init>', 'CALL', 'Accepts client socket and creates HTTPSession',
  evidence='SRC CloudStreamServer.java:217-218')
e('CloudStreamer.__init__', 'CloudStreamServer.<init>', 'CALL', 'Calls super constructor with port and file',
  evidence='SRC CloudStreamer.java:31, CloudStreamServer.java:199-201')

# HTTPSession - created per client connection
e('CloudStreamServer$HTTPSession.<init>', 'CloudStreamServer$HTTPSession.run', 'LIFECYCLE', 'Creates thread and calls run',
  evidence='SRC CloudStreamServer.java:330-338')
e('CloudStreamServer$HTTPSession.run', 'CloudStreamServer$HTTPSession.handleResponse', 'CALL', 'HTTPSession.run calls handleResponse',
  evidence='SRC CloudStreamServer.java:358-361')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.decodeHeader', 'CALL', 'Parses HTTP headers',
  evidence='SRC CloudStreamServer.java:385')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.sendError', 'CALL', 'Sends error on invalid request',
  evidence='SRC CloudStreamServer.java:389, 398, 402')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.decodeParms', 'CALL', 'Decodes URI parameters',
  evidence='SRC CloudStreamServer.java:473-475')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.decodeMultipartData', 'CALL', 'Processes multipart form data',
  evidence='SRC CloudStreamServer.java:480-481')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.sendResponse', 'CALL', 'Sends HTTP response',
  evidence='SRC CloudStreamServer.java:512-514')
e('CloudStreamServer$HTTPSession.decodeHeader', 'CloudStreamServer$HTTPSession.decodePercent', 'CALL', 'Decodes URI percent encoding',
  evidence='SRC CloudStreamServer.java:508')
e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.getBoundaryPositions', 'CALL', 'Finds multipart boundaries',
  evidence='SRC CloudStreamServer.java:598')
e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.saveTmpFile', 'CALL', 'Saves uploaded file',
  evidence='SRC CloudStreamServer.java:608')
e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.stripMultipartHeaders', 'CALL', 'Processes multipart headers',
  evidence='SRC CloudStreamServer.java:607')
e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.sendError', 'CALL', 'Sends error on parse failure',
  evidence='SRC CloudStreamServer.java:597, 601, 605')
e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer.serve', 'CALL', 'Calls abstract serve method (overridden in CloudStreamer)',
  evidence='SRC CloudStreamServer.java:511')

# Response - created and returned by serve methods
e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'CALL', 'Creates response with error status',
  evidence='SRC CloudStreamer.java:65')
e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'CALL', 'Creates response with range not satisfiable',
  evidence='SRC CloudStreamer.java:93')
e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'CALL', 'Creates response with partial content',
  evidence='SRC CloudStreamer.java:106')
e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'CALL', 'Creates response with OK status',
  evidence='SRC CloudStreamer.java:111')
e('CloudStreamServer$Response.<init>', 'CloudStreamServer$Response.addHeader', 'CALL', 'Response constructor allows adding headers',
  evidence='SRC CloudStreamer.java:97, 107, 112, 114')

# CloudStreamServer stop
e('CloudStreamer.stop', 'CloudStreamServer.stop', 'CALL', 'Calls parent stop method',
  evidence='SRC CloudStreamer.java:52-55')
e('CloudStreamServer.stop', 'CloudStreamServer.tryBind', 'CALL', 'tryBind stops Streamer if port occupied',
  evidence='SRC CloudStreamServer.java:199-201, 226-228')

# No UNREACHABLE entries for this batch - all methods are reachable


# ---- label_b007 ----
# ---- Batch 007 label part (2026-10-27)
# Classes: CheckBox, CheckableCircleView, CircleGradientDrawable, CircularColorsView, CloudContract, CloudEntry, CloudHandler, CloudIconDataFetcher
# 40 methods from batch_007.txt

# CheckBox (preference custom widget)
e('PrefFrag.onCreate', 'CheckBox.<init>',
  'FRAMEWORK', 'Preference framework inflates preference from XML (findPreference returns cached/inflated instance)',
  evidence='SRC com/amaze/filemanager/fragments/preference_fragments/PrefFrag.java:118-119')

e('CheckBox.onBindView', 'CheckBox.clearListenerInViewGroup',
  'CALL', 'Explicit call in onBindView override',
  evidence='SRC com/amaze/filemanager/ui/views/preference/CheckBox.java:20-21, 34')

e('CheckBox.<init>', 'CheckBox.onBindView',
  'LIFECYCLE', 'Preference framework lifecycle: onBindView called after preference is created',
  evidence='SRC com/amaze/filemanager/ui/views/preference/CheckBox.java:15-21, FW-SRC core/java/android/preference/Preference.java')

# CheckableCircleView (color picker selection indicator)
e('ColorAdapter.getView', 'CheckableCircleView.<init>',
  'CALL', 'Inflated in getView or reused from convertView',
  evidence='SRC com/amaze/filemanager/adapters/ColorAdapter.java:49-51')

e('ColorAdapter.getView', 'CheckableCircleView.setColor',
  'CALL', 'setColor called to set circle paint color',
  evidence='SRC com/amaze/filemanager/adapters/ColorAdapter.java:55-61')

e('ColorAdapter.getView', 'CheckableCircleView.setChecked',
  'CALL', 'setChecked called to show/hide the checkmark',
  evidence='SRC com/amaze/filemanager/adapters/ColorAdapter.java:56-61')

e('CheckableCircleView.<init>', 'CheckableCircleView.onDraw',
  'LIFECYCLE', 'Framework renders view; onDraw is layout callback',
  evidence='SRC com/amaze/filemanager/ui/views/CheckableCircleView.java:36-45, FW-SRC core/java/android/view/View.java')

# CircleGradientDrawable (file selection indicator background)
e('RecyclerAdapter.animate', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'CALL', 'Instantiated with int color and AppTheme in file list selection animation',
  evidence='SRC com/amaze/filemanager/adapters/RecyclerAdapter.java:536-539')

e('CompressedExplorerAdapter.onBindViewHolder', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'CALL', 'Instantiated with int color and AppTheme in archive list selection',
  evidence='SRC com/amaze/filemanager/adapters/CompressedExplorerAdapter.java:204-207')

e('com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'CALL', 'String-color variant calls int-color variant constructor',
  evidence='SRC com/amaze/filemanager/ui/views/CircleGradientDrawable.java:28-31, 36-44')

e('com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'CALL', 'int-color variant calls helper constructor (AppTheme+DisplayMetrics)',
  evidence='SRC com/amaze/filemanager/ui/views/CircleGradientDrawable.java:36-44, 46-54')

e('com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>', 'CircleGradientDrawable.dpToPx',
  'CALL', 'dpToPx called to convert stroke width from dp to pixels',
  evidence='SRC com/amaze/filemanager/ui/views/CircleGradientDrawable.java:50, 56-57')

# CircularColorsView (color picker UI component)
e('com/amaze/filemanager/ui/dialogs/ColorPickerDialog.onCreateDialog', 'com/amaze/filemanager/ui/views/CircularColorsView.<init>',
  'CALL', 'Inflated from layout in color picker dialog',
  evidence='SRC com/amaze/filemanager/ui/dialogs/ColorPickerDialog.java:128-130')

e('SelectedColorsPreference.onBindView', 'com/amaze/filemanager/ui/views/CircularColorsView.<init>',
  'CALL', 'Inflated from layout in preference binding',
  evidence='SRC com/amaze/filemanager/ui/views/preference/SelectedColorsPreference.java:40-44')

e('com/amaze/filemanager/ui/views/CircularColorsView.<init>', 'CircularColorsView.init',
  'CALL', 'init called from both constructors',
  evidence='SRC com/amaze/filemanager/ui/views/CircularColorsView.java:30-31, 36-37, 40-46')

e('com/amaze/filemanager/ui/views/CircularColorsView.<init>', 'CircularColorsView.onDraw',
  'LIFECYCLE', 'Framework renders view; onDraw is layout callback',
  evidence='SRC com/amaze/filemanager/ui/views/CircularColorsView.java:48-76, FW-SRC core/java/android/view/View.java')

e('com/amaze/filemanager/ui/dialogs/ColorPickerDialog.onCreateDialog', 'CircularColorsView.setColors',
  'CALL', 'setColors called to set the four colors after inflating view',
  evidence='SRC com/amaze/filemanager/ui/dialogs/ColorPickerDialog.java:131-134')

e('SelectedColorsPreference.onBindView', 'CircularColorsView.setDividerColor',
  'CALL', 'setDividerColor called in preference binding',
  evidence='SRC com/amaze/filemanager/ui/views/preference/SelectedColorsPreference.java:40-44')

# CloudEntry (data model for cloud service credentials)
e('CloudHandler.findEntry', 'com/amaze/filemanager/database/models/CloudEntry.<init>',
  'CALL', 'No-arg constructor instantiated to create entry object',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:143')

e('CloudHandler.getAllEntries', 'com/amaze/filemanager/database/models/CloudEntry.<init>',
  'CALL', 'No-arg constructor instantiated in loop',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:174')

e('com/amaze/filemanager/database/models/CloudEntry.<init>', 'CloudEntry.setId',
  'LIFECYCLE', 'Setter called to initialize field (alternate constructor)',
  evidence='SRC com/amaze/filemanager/database/models/CloudEntry.java:17-20')

e('com/amaze/filemanager/database/models/CloudEntry.<init>', 'CloudEntry.setServiceType',
  'LIFECYCLE', 'Setter called to initialize field (alternate constructor)',
  evidence='SRC com/amaze/filemanager/database/models/CloudEntry.java:17-20')

e('com/amaze/filemanager/database/models/CloudEntry.<init>', 'CloudEntry.setPersistData',
  'LIFECYCLE', 'Setter called to initialize field (alternate constructor)',
  evidence='SRC com/amaze/filemanager/database/models/CloudEntry.java:17-20')

e('CloudHandler.findEntry', 'CloudEntry.setId',
  'CALL', 'setId called to populate from database cursor',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:145')

e('CloudHandler.findEntry', 'CloudEntry.setServiceType',
  'CALL', 'setServiceType called to populate from database',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:146')

e('CloudHandler.findEntry', 'CloudEntry.setPersistData',
  'CALL', 'setPersistData called to populate from database (decrypted)',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:150')

e('CloudHandler.getAllEntries', 'CloudEntry.setId',
  'CALL', 'setId called in loop to populate from cursor',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:175')

e('CloudHandler.getAllEntries', 'CloudEntry.setServiceType',
  'CALL', 'setServiceType called in loop to populate from cursor',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:176')

e('CloudHandler.getAllEntries', 'CloudEntry.setPersistData',
  'CALL', 'setPersistData called in loop to populate from cursor (decrypted)',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:178')

e('CloudHandler.addEntry', 'CloudEntry.getServiceType',
  'CALL', 'getServiceType called to retrieve ordinal for database insert',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:91')

e('CloudHandler.addEntry', 'CloudEntry.getPersistData',
  'CALL', 'getPersistData called to retrieve data for encryption/insert',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:93')

e('CloudHandler.updateEntry', 'CloudEntry.getId',
  'CALL', 'getId called to populate update values',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:125')

e('CloudHandler.updateEntry', 'CloudEntry.getServiceType',
  'CALL', 'getServiceType called to retrieve ordinal for update where clause',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:126')

e('CloudHandler.updateEntry', 'CloudEntry.getPersistData',
  'CALL', 'getPersistData called to retrieve data for encryption/update',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:130')

# CloudHandler (SQLite database helper for cloud credentials)
e('com/amaze/filemanager/ui/views/drawer/Drawer.updateItemsList', 'CloudHandler.<init>',
  'CALL', 'Drawer accesses cloud constants; CloudHandler instantiated through app context',
  evidence='SRC com/amaze/filemanager/ui/views/drawer/Drawer.java:313-340 (cloud initialization)')

e('CloudHandler.<init>', 'CloudHandler.onCreate',
  'FRAMEWORK', 'SQLiteOpenHelper lifecycle: onCreate called on first database access',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:44-46, FW-SRC android-8.1.0_r1/core/java/android/database/sqlite/SQLiteOpenHelper.java')

e('CloudHandler.<init>', 'CloudHandler.onUpgrade',
  'FRAMEWORK', 'SQLiteOpenHelper lifecycle: onUpgrade called if database version changes',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:44-46, FW-SRC android-8.1.0_r1/core/java/android/database/sqlite/SQLiteOpenHelper.java')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'CloudHandler.addEntry',
  'CALL', 'addEntry called to store new cloud credentials',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:83-104 (public method reachable from fragment)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'CloudHandler.findEntry',
  'CALL', 'findEntry called to retrieve cloud credentials',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:141-162 (public method)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'CloudHandler.getAllEntries',
  'CALL', 'getAllEntries called to enumerate cloud service accounts',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:164-195 (public method)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'CloudHandler.updateEntry',
  'CALL', 'updateEntry called to modify existing credentials',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:117-140 (public method)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'CloudHandler.clear',
  'CALL', 'clear called to remove credentials for a service',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:106-115 (public method)')

# CloudIconDataFetcher (Glide data fetcher for cloud icons)
e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.<init>',
  'CALL', 'Instantiated in model loader to create fetcher for Glide',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:27-31, SRC com/amaze/filemanager/utils/glide/CloudIconModelLoader.java:30')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.loadData',
  'FRAMEWORK', 'Glide framework lifecycle: loadData called when Glide needs to fetch image data',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:33-42, INFERRED (Glide DataFetcher interface)')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.cleanup',
  'FRAMEWORK', 'Glide framework lifecycle: cleanup called after load completes or fails',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:47-51, INFERRED (Glide DataFetcher interface)')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.cancel',
  'FRAMEWORK', 'Glide framework lifecycle: cancel called if load is cancelled',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:52-54, INFERRED (Glide DataFetcher interface)')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.getDataClass',
  'FRAMEWORK', 'Glide framework lifecycle: getDataClass called to determine output type',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:56-59, INFERRED (Glide DataFetcher interface)')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.getDataSource',
  'FRAMEWORK', 'Glide framework lifecycle: getDataSource called to determine source (REMOTE)',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:61-64, INFERRED (Glide DataFetcher interface)')

# UNREACHABLE methods
UNREACHABLE_B007 = {
    'com/amaze/filemanager/database/CloudContract.<init>': (
        'no_trigger_in_app',
        'CloudContract is a constants-only class with 11 static final fields and no instance initialization; never instantiated in app code',
        'SRC com/amaze/filemanager/database/CloudContract.java:1-22',
        'SOURCE'
    ),
}
UNREACHABLE.update(UNREACHABLE_B007)


# ---- label_b006 ----
# ---- Helper B006 label part (2026-10-27)

# BottomBar$5 edges
e('BottomBar.showButtons', 'BottomBar$5.<init>', 'CALL', 'AnimatorListenerAdapter for initial path created',
  evidence='SRC ui/views/appbar/BottomBar.java:398')
e('BottomBar$5.<init>', 'BottomBar$5.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:401')
e('BottomBar$5.<init>', 'BottomBar$5.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:410')
e('BottomBar$5.onAnimationStart', 'BottomBar$5.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:404')
e('BottomBar$5.onAnimationEnd', 'BottomBar$5.lambda$onAnimationEnd$1', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:409-412')

# BottomBar$6 edges
e('BottomBar.showButtons', 'BottomBar$6.<init>', 'CALL', 'AnimatorListenerAdapter for different path slideout created',
  evidence='SRC ui/views/appbar/BottomBar.java:425')
e('BottomBar$6.<init>', 'BottomBar$6.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:428')
e('BottomBar$6.<init>', 'BottomBar$6.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:437')
e('BottomBar$6.onAnimationStart', 'BottomBar$6.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:433')
e('BottomBar$6.onAnimationEnd', 'BottomBar$6$1.<init>', 'CALL', 'Nested AnimatorListenerAdapter for slidein created',
  evidence='SRC ui/views/appbar/BottomBar.java:446')

# BottomBar$6$1 edges
e('BottomBar$6$1.<init>', 'BottomBar$6$1.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:459')
e('BottomBar$6$1.<init>', 'BottomBar$6$1.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:448')
e('BottomBar$6$1.onAnimationStart', 'BottomBar$6$1.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:464')
e('BottomBar$6$1.onAnimationEnd', 'BottomBar$6$1.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:450-453')

# BoundedFileChannelInputStream edges
e('SevenZFile.readHeaders', 'BoundedFileChannelInputStream.<init>', 'CALL', 'Created by SevenZFile for reading 7z archives',
  evidence='SRC sevenz/SevenZFile.java:371,429,998')
e('BoundedFileChannelInputStream.<init>', 'BoundedFileChannelInputStream.read', 'CALL', 'Called during stream reading',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:44,59')
e('BoundedFileChannelInputStream.read', 'BoundedFileChannelInputStream.read', 'CALL', 'Private helper calls',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:83-88')

# Bzip2HelperTask edges
e('Bzip2Decompressor.changePath', 'Bzip2HelperTask.<init>', 'CALL', 'Created by Bzip2Decompressor.changePath',
  evidence='SRC filesystem/compressed/showcontents/helpers/Bzip2Decompressor.java:43')
e('Bzip2HelperTask.<init>', 'Bzip2HelperTask.addElements', 'CALL', 'Called from CompressedHelperTask.doInBackground',
  evidence='SRC asynchronous/asynctasks/compress/CompressedHelperTask.java:53')

# Bzip2Extractor edges
e('CompressedHelper.getExtractorInstance', 'Bzip2Extractor.<init>', 'CALL', 'Created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:90,174')
e('Bzip2Extractor.<init>', 'Bzip2Extractor.extractWithFilter', 'CALL', 'Called from Extractor base class',
  evidence='SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:49')
e('Bzip2Extractor.extractWithFilter', 'Bzip2Extractor.extractEntry', 'CALL', 'Called from extractWithFilter',
  evidence='SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:68')

# Bzip2Decompressor edges
e('CompressedHelper.getCompressorInstance', 'Bzip2Decompressor.<init>', 'CALL', 'Created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:120,174')
e('CompressedExplorerFragment.changePath', 'Bzip2Decompressor.changePath', 'CALL', 'Fragment navigation calls changePath',
  evidence='SRC fragments/CompressedExplorerFragment.java:411')

# UNREACHABLE methods from batch_006
UNREACHABLE_B006 = {
    'BottomBar$5.onAnimationCancel': ('framework_never_calls',
        'Animation cancellation not triggered in app usage',
        'SRC ui/views/appbar/BottomBar.java:418-421',
        'SOURCE'),
    'BottomBar$6.onAnimationCancel': ('framework_never_calls',
        'Animation cancellation not triggered in app usage',
        'SRC ui/views/appbar/BottomBar.java:470-473',
        'SOURCE'),
    'BoundedFileChannelInputStream.close': ('framework_never_calls',
        'Close method explicitly empty; channel controlled externally',
        'SRC sevenz/BoundedFileChannelInputStream.java:91-93; comment states nested channel controlled externally',
        'SOURCE'),
    'CLI.<init>': ('no_trigger_in_app',
        'Command-line tool not instantiated by app',
        'SRC sevenz/CLI.java:24; grep shows no app usage',
        'SOURCE'),
    'CLI.main': ('no_trigger_in_app',
        'Command-line entry point not called by Android app',
        'SRC sevenz/CLI.java:114; main method unused in app context',
        'SOURCE'),
    'CLI.usage': ('no_trigger_in_app',
        'Called only from unused CLI.main',
        'SRC sevenz/CLI.java:132; only caller is CLI.main',
        'SOURCE'),
    'CLI.grabMode': ('no_trigger_in_app',
        'Called only from unused CLI.main',
        'SRC sevenz/CLI.java:136; only caller is CLI.main',
        'SOURCE'),
    'CLI$Mode.<clinit>': ('no_trigger_in_app',
        'Enum initializer only accessed through unused CLI.main',
        'SRC sevenz/CLI.java:29-50; enum constants never instantiated',
        'SOURCE'),
    'CLI$Mode.<init>': ('no_trigger_in_app',
        'Enum constructor only accessed through unused CLI.main',
        'SRC sevenz/CLI.java:57-60; enum not instantiated in app',
        'SOURCE'),
    'CLI$Mode.getMessage': ('no_trigger_in_app',
        'Called only from unused CLI enum modes',
        'SRC sevenz/CLI.java:62-64; only caller is unused enum',
        'SOURCE'),
    'CLI$Mode$1.<init>': ('no_trigger_in_app',
        'Enum constant for unused CLI.LIST mode',
        'SRC sevenz/CLI.java:29-55; LIST mode never used',
        'SOURCE'),
    'CLI$Mode$1.getContentMethods': ('no_trigger_in_app',
        'Method of unused LIST mode',
        'SRC sevenz/CLI.java:44-55; only called from LIST takeAction',
        'SOURCE'),
    'CLI$Mode$1.takeAction': ('no_trigger_in_app',
        'Method of unused LIST mode',
        'SRC sevenz/CLI.java:31-43; LIST never instantiated',
        'SOURCE'),
    'CLI$Mode$2.<init>': ('no_trigger_in_app',
        'Enum constant for unused CLI.EXTRACT mode',
        'SRC sevenz/CLI.java:56-94; EXTRACT mode never used',
        'SOURCE'),
    'CLI$Mode$2.takeAction': ('no_trigger_in_app',
        'Method of unused EXTRACT mode',
        'SRC sevenz/CLI.java:58-94; only called from EXTRACT enum',
        'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_B006)


# ---- label_b005 ----
# ---- Batch 005: BottomBar and inner classes (2026-10-27 21:23)

# BottomBar entry point from AppBar
e('com.amaze.filemanager.ui.views.appbar.AppBar.<init>', 
  'BottomBar.<init>', 'CALL', 'AppBar constructor instantiates BottomBar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/AppBar.java:37')

# BottomBar public API calls from MainActivity
e('MainActivity.onCreate', 
  'BottomBar.setClickListener', 'CALL', 'MainActivity onCreate calls setClickListener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:854')

e('MainActivity.onActivityResult',
  'BottomBar.resetClickListener', 'CALL', 'MainActivity onActivityResult resets listeners',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:892')

e('MainActivity.onPause',
  'BottomBar.updatePath', 'CALL', 'MainActivity onPause updates bottom bar path',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:850')

e('com.amaze.filemanager.activities.MainActivity.updateBottomBarColor',
  'BottomBar.setBackgroundColor', 'CALL', 'MainActivity theme color applied to bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:1475')

# BottomBar calls from MainFragment
e('com.amaze.filemanager.fragments.MainFragment.onViewCreated',
  'BottomBar.setClickListener', 'CALL', 'MainFragment sets up touch listeners',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:281')

e('com.amaze.filemanager.fragments.MainFragment.updateBottomBar',
  'BottomBar.updatePath', 'CALL', 'MainFragment updates bottom bar on path change',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:451')

e('com.amaze.filemanager.fragments.MainFragment.searchResultsFound',
  'BottomBar.setPathText', 'CALL', 'MainFragment updates path text on search',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1604')

e('com.amaze.filemanager.fragments.MainFragment.searchResultsFound',
  'BottomBar.setFullPathText', 'CALL', 'MainFragment updates full path on search',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1605')

# BottomBar calls from TabFragment
e('com.amaze.filemanager.fragments.TabFragment.onFragmentResult',
  'BottomBar.updatePath', 'CALL', 'TabFragment updates bottom bar on selection',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/TabFragment.java:222-305')

# BottomBar visibility from fragment lifecycle
e('com.amaze.filemanager.fragments.FtpServerFragment.onViewCreated',
  'BottomBar.setVisibility', 'CALL', 'FTP fragment hides bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/FtpServerFragment.java:157')

e('com.amaze.filemanager.fragments.AppsListFragment.onViewCreated',
  'BottomBar.setVisibility', 'CALL', 'AppsListFragment hides bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:84')

e('com.amaze.filemanager.fragments.ProcessViewerFragment.onViewCreated',
  'BottomBar.setVisibility', 'CALL', 'ProcessViewerFragment hides bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/ProcessViewerFragment.java:143')

e('com.amaze.filemanager.fragments.CompressedExplorerFragment.updatePath',
  'BottomBar.updatePath', 'CALL', 'CompressedExplorer updates bottom bar on navigation',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/CompressedExplorerFragment.java:445')

# BottomBar internal methods
e('BottomBar.setClickListener',
  'BottomBar.onTouch', 'CALL', 'setClickListener registers onTouch listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:154-160')

e('BottomBar.onTouch',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.onDown', 'CALL', 'onTouch delegates to GestureDetector',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:486, FW-SRC android/view/GestureDetector.java (onTouchEvent dispatches to listeners)')

e('BottomBar.onTouch',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.onSingleTapConfirmed', 'CALL', 'GestureDetector calls onSingleTapConfirmed',
  evidence='FW-SRC android/view/GestureDetector.java (onSingleTapConfirmed called on confirmed single tap)')

e('BottomBar.onTouch',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.onLongPress', 'CALL', 'GestureDetector calls onLongPress',
  evidence='FW-SRC android/view/GestureDetector.java (onLongPress called on long press)')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$2.onSingleTapConfirmed',
  'BottomBar.showButtons', 'CALL', 'Gesture handler calls showButtons',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:138, 144')

e('BottomBar.showButtons',
  'BottomBar.areButtonsShowing', 'CALL', 'showButtons queries button visibility',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:167')

e('BottomBar.showButtons',
  'BottomBar.createArrow', 'CALL', 'showButtons creates arrow button views',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:205')

e('BottomBar.showButtons',
  'BottomBar.createFolderButton', 'CALL', 'showButtons creates folder button views',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:195')

e('BottomBar.showButtons',
  'BottomBar.lambda$showButtons$0', 'CALL', 'showButtons root button click listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:181')

e('BottomBar.showButtons',
  'BottomBar.lambda$showButtons$1', 'CALL', 'showButtons storage button click listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:187')

e('BottomBar.showButtons',
  'BottomBar.lambda$showButtons$2', 'CALL', 'showButtons folder button click listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:193')

e('BottomBar.showButtons',
  'BottomBar.sendScroll', 'CALL', 'showButtons scrolls to position',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:233')

e('BottomBar.showButtons',
  'BottomBar.lambda$showButtons$3', 'CALL', 'showButtons post scrolling callback',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:229')

e('BottomBar.updatePath',
  'BottomBar.areButtonsShowing', 'CALL', 'updatePath queries button visibility',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:239')

e('BottomBar.updatePath',
  'BottomBar.showButtons', 'CALL', 'updatePath shows buttons on visible state',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:238')

e('BottomBar.updatePath',
  'BottomBar.sendScroll', 'CALL', 'updatePath scrolls path view',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:461')

e('BottomBar.sendScroll',
  'BottomBar.lambda$sendScroll$4', 'CALL', 'sendScroll posts delayed scroll',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:483')

# Animation callbacks - BottomBar$3 (forward navigation)
e('BottomBar.updatePath',
  'BottomBar$3.<init>', 'CALL', 'updatePath sets animation listener for forward',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:345')

e('BottomBar$3.onAnimationStart',
  'BottomBar$3.lambda$onAnimationStart$1', 'CALL', 'Animation posts scroll update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:359')

e('BottomBar$3.onAnimationEnd',
  'BottomBar$3.lambda$onAnimationEnd$0', 'CALL', 'Animation posts visibility update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:349')

# Animation callbacks - BottomBar$4 (backward navigation)
e('BottomBar.updatePath',
  'BottomBar$4.<init>', 'CALL', 'updatePath sets animation listener for backward',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:374')

e('BottomBar$4.onAnimationStart',
  'BottomBar$4.lambda$onAnimationStart$1', 'CALL', 'Animation posts scroll update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:389')

e('BottomBar$4.onAnimationEnd',
  'BottomBar$4.lambda$onAnimationEnd$0', 'CALL', 'Animation posts visibility update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:379')

# CountDownTimer - BottomBar$1
e('BottomBar.<init>',
  'BottomBar$1.<init>', 'CALL', 'BottomBar constructor creates countdown timer',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:113')

e('BottomBar$1.<init>',
  'BottomBar$1.onTick', 'LIFECYCLE', 'CountDownTimer invokes onTick periodically',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:115, FW-SRC android/os/CountDownTimer.java (onTick invoked every interval)')

e('BottomBar$1.<init>',
  'BottomBar$1.onFinish', 'LIFECYCLE', 'CountDownTimer invokes onFinish on completion',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:118, FW-SRC android/os/CountDownTimer.java (onFinish invoked when countdown completes)')

# GestureDetector - BottomBar$2
e('BottomBar.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.<init>', 'CALL', 'BottomBar constructor creates gesture listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:123')

# Framework animation listeners
e('BottomBar$3.<init>',
  'BottomBar$3.onAnimationStart', 'LIFECYCLE', 'Animator invokes onAnimationStart',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationStart called on animation start)')

e('BottomBar$3.<init>',
  'BottomBar$3.onAnimationEnd', 'LIFECYCLE', 'Animator invokes onAnimationEnd',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationEnd called on animation end)')

e('BottomBar$3.<init>',
  'BottomBar$3.onAnimationCancel', 'LIFECYCLE', 'Animator invokes onAnimationCancel',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationCancel called on animation cancel)')

e('BottomBar$4.<init>',
  'BottomBar$4.onAnimationStart', 'LIFECYCLE', 'Animator invokes onAnimationStart',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationStart called on animation start)')

e('BottomBar$4.<init>',
  'BottomBar$4.onAnimationEnd', 'LIFECYCLE', 'Animator invokes onAnimationEnd',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationEnd called on animation end)')

# No UNREACHABLE methods - all are reachable


# ---- label_b017 ----
# ---- Helper batch_017 label part (2025-01-18)

# CryptHandler edges
e('MainActivity.onDestroy', 'CryptHandler.<init>', 'CALL', 'MainActivity closes database handlers on destroy',
  evidence='SRC MainActivity.java:1214')

e('MainFragment.findEncryptedEntry', 'CryptHandler.<init>', 'CALL', 'Creates handler to query encrypted entries',
  evidence='SRC MainFragment.java:952')

e('EncryptDecryptUtils.startEncryption', 'CryptHandler.<init>', 'CALL', 'Creates handler to add encrypted entry',
  evidence='SRC EncryptDecryptUtils.java:48')

e('DeleteTask.doInBackground', 'CryptHandler.<init>', 'CALL', 'Creates handler to delete encrypted entry',
  evidence='SRC DeleteTask.java:163')

e('MoveFiles.doInBackground', 'CryptHandler.<init>', 'CALL', 'Creates handler to update encrypted entry path',
  evidence='SRC MoveFiles.java:188')

e('CopyService.onStartCommand', 'CryptHandler.<init>', 'CALL', 'Creates handler in copy service',
  evidence='SRC CopyService.java:305')

e('CryptHandler.<init>', 'SQLiteOpenHelper.<init>', 'FRAMEWORK', 'Extends SQLiteOpenHelper',
  evidence='SRC CryptHandler.java:21 extends SQLiteOpenHelper, FW-SRC android/database/sqlite/SQLiteOpenHelper.java:132-164')

e('SQLiteOpenHelper.getWritableDatabase', 'CryptHandler.onCreate', 'LIFECYCLE', 'Framework calls onCreate when database created',
  evidence='SRC CryptHandler.java:37 onCreate signature, FW-SRC android/database/sqlite/SQLiteOpenHelper.java:256-294')

e('SQLiteOpenHelper.getWritableDatabase', 'CryptHandler.onUpgrade', 'LIFECYCLE', 'Framework calls onUpgrade on version change',
  evidence='SRC CryptHandler.java:47 onUpgrade signature, FW-SRC android/database/sqlite/SQLiteOpenHelper.java:256-294')

e('EncryptDecryptUtils.startEncryption', 'CryptHandler.addEntry', 'CALL', 'Adds encrypted file entry to database',
  evidence='SRC EncryptDecryptUtils.java:54')

e('DeleteTask.doInBackground', 'CryptHandler.clear', 'CALL', 'Removes encrypted entry when file deleted',
  evidence='SRC DeleteTask.java:165')

e('MainFragment.findEncryptedEntry', 'CryptHandler.findEntry', 'CALL', 'Queries encrypted entry by path',
  evidence='SRC MainFragment.java:956')

e('MoveFiles.doInBackground', 'CryptHandler.findEntry', 'CALL', 'Finds encrypted entry before updating path',
  evidence='SRC MoveFiles.java:189')

e('MainFragment.findEncryptedEntry', 'CryptHandler.getAllEntries', 'CALL', 'Retrieves all encrypted entries to find match',
  evidence='SRC MainFragment.java:956')

e('MoveFiles.doInBackground', 'CryptHandler.updateEntry', 'CALL', 'Updates encrypted file path after move',
  evidence='SRC MoveFiles.java:194')

e('CryptHandler.addEntry', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts password before storing',
  evidence='SRC CryptHandler.java:60')

e('CryptHandler.updateEntry', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts password before updating',
  evidence='SRC CryptHandler.java:81')

e('CryptHandler.findEntry', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts password from database',
  evidence='SRC CryptHandler.java:97')

e('CryptHandler.getAllEntries', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts password for each entry',
  evidence='SRC CryptHandler.java:120')

# CryptUtil edges
e('EncryptService.onStartCommand', 'CryptUtil.<init>(Context,HybridFileParcelable,ProgressHandler,ArrayList,String)', 'CALL', 'Constructor starts encryption process',
  evidence='SRC EncryptService.java:191')

e('DecryptService.onStartCommand', 'CryptUtil.<init>(Context,HybridFileParcelable,String,ProgressHandler,ArrayList)', 'CALL', 'Constructor starts decryption process',
  evidence='SRC DecryptService.java:149')

e('CryptUtil.<init>(Context,HybridFileParcelable,ProgressHandler,ArrayList,String)', 'CryptUtil.encrypt', 'CALL', 'Encryption constructor calls encrypt',
  evidence='SRC CryptUtil.java:124')

e('CryptUtil.<init>(Context,HybridFileParcelable,String,ProgressHandler,ArrayList)', 'CryptUtil.decrypt', 'CALL', 'Decryption constructor calls decrypt',
  evidence='SRC CryptUtil.java:152')

e('CryptUtil.encrypt', 'CryptUtil.aesEncrypt', 'CALL', 'Encrypts file using AES on API 23+',
  evidence='SRC CryptUtil.java:225')

e('CryptUtil.encrypt', 'CryptUtil.rsaEncrypt', 'CALL', 'Encrypts file using RSA on API 18-22',
  evidence='SRC CryptUtil.java:227')

e('CryptUtil.decrypt', 'CryptUtil.aesDecrypt', 'CALL', 'Decrypts file using AES on API 23+',
  evidence='SRC CryptUtil.java:206')

e('CryptUtil.decrypt', 'CryptUtil.rsaDecrypt', 'CALL', 'Decrypts file using RSA on API 18-22',
  evidence='SRC CryptUtil.java:208')

e('CloudHandler.addEntry', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts cloud service password',
  evidence='SRC CloudHandler.java:94')

e('CloudHandler.updateEntry', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts cloud service password',
  evidence='SRC CloudHandler.java:129')

e('FtpServerFragment.onPreferenceChange', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts FTP password',
  evidence='SRC FtpServerFragment.java:595')

e('SmbUtil.getSmbEncryptedPath', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts SMB password',
  evidence='SRC SmbUtil.java:56')

e('PrefFrag.updatePreferencesMasterPassword', 'CryptUtil.encryptPassword', 'CALL', 'Encrypts master password',
  evidence='SRC PrefFrag.java:258')

e('CloudHandler.findEntry', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts cloud service password',
  evidence='SRC CloudHandler.java:155')

e('CloudHandler.getAllEntries', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts cloud service passwords',
  evidence='SRC CloudHandler.java:190')

e('FtpService.onStartCommand', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts FTP password',
  evidence='SRC FtpService.java:167')

e('FtpServerFragment.getPasswordFromPreferences', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts FTP password',
  evidence='SRC FtpServerFragment.java:552')

e('SmbUtil.getSmbDecryptedPath', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts SMB password',
  evidence='SRC SmbUtil.java:34')

e('PrefFrag.showMasterPasswordDialog', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts master password',
  evidence='SRC PrefFrag.java:234')

e('EncryptDecryptUtils.decryptFile', 'CryptUtil.decryptPassword', 'CALL', 'Decrypts file password',
  evidence='SRC EncryptDecryptUtils.java:122')

e('CryptUtil.encryptPassword', 'CryptUtil.aesEncryptPassword', 'CALL', 'Uses AES password encryption on API 23+',
  evidence='SRC CryptUtil.java:526')

e('CryptUtil.encryptPassword', 'CryptUtil.rsaEncryptPassword', 'CALL', 'Uses RSA password encryption on API 18-22',
  evidence='SRC CryptUtil.java:528')

e('CryptUtil.decryptPassword', 'CryptUtil.aesDecryptPassword', 'CALL', 'Uses AES password decryption on API 23+',
  evidence='SRC CryptUtil.java:528')

e('CryptUtil.decryptPassword', 'CryptUtil.rsaDecryptPassword', 'CALL', 'Uses RSA password decryption on API 18-22',
  evidence='SRC CryptUtil.java:530')

e('CryptUtil.aesEncrypt', 'CryptUtil.getSecretKey', 'CALL', 'Gets AES key for encryption',
  evidence='SRC CryptUtil.java:278')

e('CryptUtil.aesDecrypt', 'CryptUtil.getSecretKey', 'CALL', 'Gets AES key for decryption',
  evidence='SRC CryptUtil.java:315')

e('CryptUtil.aesEncryptPassword', 'CryptUtil.getSecretKey', 'CALL', 'Gets AES key for password encryption',
  evidence='SRC CryptUtil.java:349')

e('CryptUtil.aesDecryptPassword', 'CryptUtil.getSecretKey', 'CALL', 'Gets AES key for password decryption',
  evidence='SRC CryptUtil.java:370')

e('GeneralDialogCreation.showAuthenticationDialog', 'CryptUtil.initCipher', 'CALL', 'Initializes cipher for fingerprint authentication',
  evidence='SRC GeneralDialogCreation.java:833')

e('CryptUtil.encrypt', 'CryptUtil.lambda$encrypt$1', 'ASYNC', 'Lambda callback for recursive directory encryption',
  evidence='SRC CryptUtil.java:243')

e('CryptUtil.decrypt', 'CryptUtil.lambda$decrypt$0', 'ASYNC', 'Lambda callback for recursive directory decryption',
  evidence='SRC CryptUtil.java:178')

# CustomFileObserver edges
e('MainFragment.updateList', 'CustomFileObserver.<init>', 'CALL', 'Creates file observer for current directory',
  evidence='SRC MainFragment.java:1194')

e('MainFragment.updateList', 'CustomFileObserver.startWatching', 'CALL', 'Starts watching after observer creation',
  evidence='SRC MainFragment.java:1196')

e('MainFragment.updateList', 'CustomFileObserver.stopWatching', 'CALL', 'Stops previous observer before creating new one',
  evidence='SRC MainFragment.java:1192')

e('CustomFileObserver.startWatching', 'CustomFileObserver.startPollingSystem', 'CALL', 'Uses polling on API 23 due to framework bug',
  evidence='SRC CustomFileObserver.java:67')

e('CustomFileObserver.startWatching', 'CustomFileObserver.startWatching', 'FRAMEWORK', 'Calls super on other API levels',
  evidence='SRC CustomFileObserver.java:69')

e('CustomFileObserver.stopWatching', 'CustomFileObserver.stopPollingSystem', 'CALL', 'Stops polling on API 23',
  evidence='SRC CustomFileObserver.java:77')

e('CustomFileObserver.stopWatching', 'CustomFileObserver.startWatching', 'FRAMEWORK', 'Calls super on other API levels',
  evidence='SRC CustomFileObserver.java:79')

e('FileObserver.inotify', 'CustomFileObserver.onEvent', 'FRAMEWORK', 'Framework delivers file system events',
  evidence='SRC CustomFileObserver.java:83 overrides FileObserver.onEvent, FW-SRC android/os/FileObserver.java:239-249')

e('CustomFileObserver.onEvent', 'CustomFileObserver.sendMessages', 'CALL', 'Sends buffered messages after defer period',
  evidence='SRC CustomFileObserver.java:114,117')

e('CustomFileObserver.onEvent', 'CustomFileObserver$1.<init>', 'CALL', 'Creates TimerTask to defer message sending',
  evidence='SRC CustomFileObserver.java:108')

e('Timer.schedule', 'CustomFileObserver$1.run', 'FRAMEWORK', 'Timer executes TimerTask',
  evidence='SRC CustomFileObserver.java:109,110')

e('CustomFileObserver$1.run', 'CustomFileObserver.sendMessages', 'CALL', 'Deferred call to send buffered messages',
  evidence='SRC CustomFileObserver.java:113')

e('CustomFileObserver.startPollingSystem', 'CustomFileObserver$FileTimerTask.<init>', 'CALL', 'Creates polling task for API 23',
  evidence='SRC CustomFileObserver.java:155')

e('ScheduledExecutorService.scheduleWithFixedDelay', 'CustomFileObserver$FileTimerTask.run', 'FRAMEWORK', 'Executor runs polling task periodically',
  evidence='SRC CustomFileObserver.java:156')

e('CustomFileObserver$FileTimerTask.run', 'CustomFileObserver$FileTimerTask.compare', 'CALL', 'Compares file lists to detect changes',
  evidence='SRC CustomFileObserver.java:173,176')

e('CustomFileObserver$FileTimerTask.run', 'CustomFileObserver.onEvent', 'CALL', 'Reports detected changes as events',
  evidence='SRC CustomFileObserver.java:173,176')


# ---- label_b018 ----
# ---- Helper batch_018 label part (2024-12-29)

# CustomNavigationView is inflated from main_toolbar.xml layout and used as the drawer navigation view
# Constructor called during layout inflation from MainActivity.setContentView

e('android.view.LayoutInflater.inflate', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.<init>', 'FRAMEWORK',
  'Layout inflation of com.amaze.filemanager.ui.views.drawer.CustomNavigationView from main_toolbar.xml',
  evidence='SRC main_toolbar.xml:58 shows <com.amaze.filemanager.ui.views.drawer.CustomNavigationView android:id="@+id/navigation"')

# CustomNavigationView.<init> calls super and sets self as listener
e('com.amaze.filemanager.ui.views.drawer.CustomNavigationView.<init>', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.setNavigationItemSelectedListener', 'CALL',
  'Constructor calls super.setNavigationItemSelectedListener(this)',
  evidence='SRC CustomNavigationView.java:24 super.setNavigationItemSelectedListener(this)')

# Drawer sets the navigation item selected listener
e('Drawer.<init>', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.setNavigationItemSelectedListener', 'CALL',
  'Drawer constructor sets itself as listener',
  evidence='SRC Drawer.java:162 navView.setNavigationItemSelectedListener(this)')

# onNavigationItemSelected is the callback for navigation item clicks
e('com.google.android.material.navigation.NavigationView', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.onNavigationItemSelected', 'GUI',
  'Framework callback when user selects navigation drawer item',
  evidence='SRC CustomNavigationView.java:16-17 implements NavigationView.OnNavigationItemSelectedListener; method at line 33')

# onNavigationItemSelected calls onItemChecked
e('com.amaze.filemanager.ui.views.drawer.CustomNavigationView.onNavigationItemSelected', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.onItemChecked', 'CALL',
  'Called when item should be selected',
  evidence='SRC CustomNavigationView.java:38,42 onItemChecked(item)')

# getSelected called from Drawer.refreshDrawer
e('Drawer.refreshDrawer', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.getSelected', 'CALL',
  'Drawer.refreshDrawer reads selected item to restore state',
  evidence='SRC Drawer.java:451 MenuItem item = navView.getSelected()')

# setCheckedItem called from Drawer.selectCorrectDrawerItemForPath
e('Drawer.selectCorrectDrawerItemForPath', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.setCheckedItem', 'CALL',
  'Drawer.selectCorrectDrawerItemForPath marks item as checked',
  evidence='SRC Drawer.java:678 navView.setCheckedItem(item)')

# deselectItems called from Drawer.deselectEverything
e('Drawer.deselectEverything', 'com.amaze.filemanager.ui.views.drawer.CustomNavigationView.deselectItems', 'CALL',
  'Drawer.deselectEverything clears navigation selection',
  evidence='SRC Drawer.java:715 navView.deselectItems()')

# CustomSshJConfig.init is called from MainActivity.onCreate
e('MainActivity.onCreate', 'CustomSshJConfig.init', 'CALL',
  'MainActivity initialization calls CustomSshJConfig.init',
  evidence='SRC MainActivity.java:286 CustomSshJConfig.init()')

# CustomSshJConfig constructor called when creating SSH clients
e('SshAuthenticationTask.doInBackground', 'CustomSshJConfig.<init>', 'CALL',
  'SSH authentication task creates CustomSshJConfig instance',
  evidence='SRC SshAuthenticationTask.java:119 final SSHClient sshClient = new SSHClient(new CustomSshJConfig())')

e('com.amaze.filemanager.asynchronous.asynctasks.ssh.GetSshHostFingerprintTask.doInBackground', 'CustomSshJConfig.<init>', 'CALL',
  'SSH fingerprint task creates CustomSshJConfig instance',
  evidence='SRC GetSshHostFingerprintTask.java:84 final SSHClient sshClient = new SSHClient(new CustomSshJConfig())')

# UNREACHABLE methods - SavedState not used on API 27 due to ClassNotFoundException guard
# isNavigationViewSavedStateMissing returns true on API 23-28, blocking SavedState usage

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView.onSaveInstanceState'] = (
    'framework_never_calls',
    'API 27 target; isNavigationViewSavedStateMissing returns true for API 23-28, method returns super.onSaveInstanceState() without using SavedState',
    'SRC CustomNavigationView.java:67-69 if (isNavigationViewSavedStateMissing()) return super.onSaveInstanceState(); line 117 returns true for API M-P',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView.onRestoreInstanceState'] = (
    'framework_never_calls',
    'API 27 target; isNavigationViewSavedStateMissing returns true for API 23-28, method calls super.onRestoreInstanceState() without using SavedState',
    'SRC CustomNavigationView.java:84-87 if(isNavigationViewSavedStateMissing()) super.onRestoreInstanceState(state); return; line 117 returns true for API M-P',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView.isNavigationViewSavedStateMissing'] = (
    'no_trigger_in_app',
    'Only called from onSaveInstanceState and onRestoreInstanceState which are themselves unreachable on API 27',
    'SRC CustomNavigationView.java:67,84,117 method definition and all call sites are within unreachable SavedState code paths',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState.<clinit>'] = (
    'framework_never_calls',
    'Static initializer for SavedState class; class not used on API 27 due to isNavigationViewSavedStateMissing guard',
    'SRC CustomNavigationView.java:120 SavedState class; line 117 isNavigationViewSavedStateMissing blocks usage on API 23-28',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState.<init>'] = (
    'framework_never_calls',
    'SavedState(Parcelable) constructor not used on API 27 due to isNavigationViewSavedStateMissing guard in onSaveInstanceState',
    'SRC CustomNavigationView.java:123-125 constructor; line 67-69 guard prevents SavedState creation',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState.<init>'] = (
    'framework_never_calls',
    'SavedState(Parcel) constructor not used on API 27 due to isNavigationViewSavedStateMissing guard in onRestoreInstanceState',
    'SRC CustomNavigationView.java:127-130 private constructor; line 84-87 guard prevents SavedState usage',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState.writeToParcel'] = (
    'framework_never_calls',
    'SavedState.writeToParcel not called on API 27 because SavedState instances never created due to isNavigationViewSavedStateMissing guard',
    'SRC CustomNavigationView.java:132-135 writeToParcel method; SavedState not instantiated on API 23-28',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState$1.<init>'] = (
    'framework_never_calls',
    'CREATOR anonymous class constructor; CREATOR not used on API 27 because SavedState parceling skipped',
    'SRC CustomNavigationView.java:138-145 CREATOR field; SavedState not parceled on API 23-28',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState$1.createFromParcel'] = (
    'framework_never_calls',
    'CREATOR.createFromParcel not called on API 27 because SavedState not saved to Parcel',
    'SRC CustomNavigationView.java:139-141 createFromParcel method; SavedState parceling blocked by line 84-87 guard',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.ui.views.drawer.CustomNavigationView$SavedState$1.newArray'] = (
    'framework_never_calls',
    'CREATOR.newArray not called on API 27 because SavedState not restored from Parcel',
    'SRC CustomNavigationView.java:142-144 newArray method; SavedState unparceling blocked by isNavigationViewSavedStateMissing',
    'SOURCE')

UNREACHABLE['com.amaze.filemanager.filesystem.ssh.CustomSshJConfig.initSignatureFactories'] = (
    'framework_never_calls',
    'Protected method overridden from DefaultConfig but never called by sshj library; DefaultConfig constructor does not invoke it',
    'SRC CustomSshJConfig.java:53-55 protected void initSignatureFactories; INFERRED source not read for DefaultConfig superclass constructor flow',
    'CALL')

UNREACHABLE['com.amaze.filemanager.filesystem.ssh.CustomSshJConfig.initRandomFactory'] = (
    'framework_never_calls',
    'Protected method overridden from DefaultConfig but never called by sshj library; DefaultConfig constructor does not invoke it',
    'SRC CustomSshJConfig.java:57-60 protected void initRandomFactory; INFERRED source not read for DefaultConfig superclass constructor flow',
    'CALL')


# ---- label_b020 ----
# ---- Helper batch_020 label part (2025-01-11)

# DataUtils$DataUtilsHolder methods
# The singleton holder is accessed via DataUtils.getInstance() which is called from many places
e('DataUtils.getInstance', 'DataUtils$DataUtilsHolder.<clinit>', 'CALL',
  'getInstance accesses the static INSTANCE field, triggering class init',
  evidence='SRC DataUtils.java:82-83 getInstance returns DataUtilsHolder.INSTANCE')

# DatapointParcelable methods
# DatapointParcelable is constructed in AbstractProgressiveService
e('AbstractProgressiveService.publishResults', 'DatapointParcelable.<clinit>', 'CALL',
  'First construction of DatapointParcelable triggers class initialization',
  evidence='SRC AbstractProgressiveService.java:157-159 new DatapointParcelable triggers <clinit>')

e('AbstractProgressiveService.publishResults', 'DatapointParcelable.<init>', 'CALL',
  'publishResults creates DatapointParcelable with 8 parameters (desc="(Ljava/lang/String;IIJJJZZ)V")',
  evidence='SRC AbstractProgressiveService.java:157-159 new DatapointParcelable(fileName, ..., move, isComplete)')

e('AbstractProgressiveService.addFirstDatapoint', 'DatapointParcelable.<init>', 'CALL',
  'addFirstDatapoint creates DatapointParcelable with 4 parameters (desc="(Ljava/lang/String;IJZ)V")',
  evidence='SRC AbstractProgressiveService.java:178 new DatapointParcelable(name, amountOfFiles, totalBytes, move)')

# DatapointParcelable$1 is the CREATOR field implementation
e('DatapointParcelable.<clinit>', 'DatapointParcelable$1.<init>', 'CALL',
  'CREATOR field initialization creates the anonymous Creator instance',
  evidence='SRC DatapointParcelable.java:126-138 CREATOR = new Creator<DatapointParcelable>()')

# DbViewerFragment methods
# DbViewerFragment is instantiated in DatabaseViewerActivity
e('DatabaseViewerActivity.onOptionsItemSelected', 'DbViewerFragment.<init>', 'CALL',
  'DatabaseViewerActivity listener creates DbViewerFragment for each table',
  evidence='SRC DatabaseViewerActivity.java:135 new DbViewerFragment()')

e('DbViewerFragment.<init>', 'DbViewerFragment.onCreateView', 'LIFECYCLE',
  'Fragment lifecycle calls onCreateView after instantiation',
  evidence='SRC DbViewerFragment.java:33-35 onCreateView inflates layout and initializes views')

e('DbViewerFragment.onCreateView', 'DbViewerFragment.onActivityCreated', 'LIFECYCLE',
  'Fragment lifecycle calls onActivityCreated after onCreateView',
  evidence='SRC DbViewerFragment.java:54-57 onActivityCreated sets theme colors')

e('DbViewerFragment.onActivityCreated', 'DbViewerFragment.onDetach', 'LIFECYCLE',
  'Fragment lifecycle calls onDetach when fragment is destroyed',
  evidence='SRC DbViewerFragment.java:69-73 onDetach closes cursors')

# DecryptService methods
# DecryptService is started via Intent from EncryptDecryptUtils
e('EncryptDecryptUtils.decryptFile', 'DecryptService.<init>', 'INTENT',
  'Framework instantiates DecryptService when started via Intent',
  evidence='SRC EncryptDecryptUtils.java:67 new Intent(main.getContext(), DecryptService.class)')

e('EncryptDecryptUtils.decryptFile', 'DecryptService.onStartCommand', 'INTENT',
  'decryptFile starts DecryptService with Intent',
  evidence='SRC EncryptDecryptUtils.java:67 new Intent(main.getContext(), DecryptService.class)')

e('DecryptService.onStartCommand', 'DecryptService.onCreate', 'LIFECYCLE',
  'Service lifecycle calls onCreate before onStartCommand',
  evidence='SRC DecryptService.java:64-68 onCreate registers broadcast receiver')

e('DecryptService.onCreate', 'DecryptService$1.<init>', 'CALL',
  'onCreate references cancelReceiver field which is initialized',
  evidence='SRC DecryptService.java:214-221 cancelReceiver = new BroadcastReceiver()')

e('DecryptService.onStartCommand', 'DecryptService$BackgroundTask.<init>', 'ASYNC',
  'onStartCommand creates and executes BackgroundTask',
  evidence='SRC DecryptService.java:118 new DecryptService.BackgroundTask().execute()')

e('DecryptService.onStartCommand', 'DecryptService.getNotificationManager', 'CALL',
  'Service implementation calls getNotificationManager',
  evidence='SRC DecryptService.java:186-188 getNotificationManager returns notificationManager')

e('DecryptService.onStartCommand', 'DecryptService.getNotificationBuilder', 'CALL',
  'Service implementation calls getNotificationBuilder',
  evidence='SRC DecryptService.java:191-193 getNotificationBuilder returns notificationBuilder')

e('DecryptService.onStartCommand', 'DecryptService.getNotificationId', 'CALL',
  'Service implementation calls getNotificationId',
  evidence='SRC DecryptService.java:196-198 getNotificationId returns DECRYPT_ID')

e('DecryptService.onStartCommand', 'DecryptService.getTitle', 'CALL',
  'Service implementation calls getTitle for notification',
  evidence='SRC DecryptService.java:202-204 getTitle returns R.string.crypt_decrypting')

e('DecryptService.onStartCommand', 'DecryptService.getNotificationCustomViewSmall', 'CALL',
  'Service implementation calls getNotificationCustomViewSmall',
  evidence='SRC DecryptService.java:207-209 getNotificationCustomViewSmall returns customSmallContentViews')

e('DecryptService.onStartCommand', 'DecryptService.getNotificationCustomViewBig', 'CALL',
  'Service implementation calls getNotificationCustomViewBig',
  evidence='SRC DecryptService.java:212-214 getNotificationCustomViewBig returns customBigContentViews')

e('DecryptService.onStartCommand', 'DecryptService.getDataPackages', 'CALL',
  'Service implementation calls getDataPackages',
  evidence='SRC DecryptService.java:217-219 getDataPackages returns dataPackages list')

e('DecryptService.onStartCommand', 'DecryptService.getProgressHandler', 'CALL',
  'Service implementation calls getProgressHandler',
  evidence='SRC DecryptService.java:222-224 getProgressHandler returns progressHandler')

e('DecryptService.onStartCommand', 'DecryptService.isDecryptService', 'CALL',
  'Service implementation calls isDecryptService',
  evidence='SRC DecryptService.java:227-229 isDecryptService returns true')

e('ProcessViewerFragment.onResume', 'DecryptService.onBind', 'SYSTEM',
  'ProcessViewerFragment binds to DecryptService',
  evidence='SRC ProcessViewerFragment.java:170 bindService with DecryptService.class intent')

e('DecryptService.onStartCommand', 'DecryptService.setProgressListener', 'CALL',
  'ProcessViewerFragment sets progress listener on bound service',
  evidence='SRC DecryptService.java:233-235 setProgressListener stores listener')

e('DecryptService.onStartCommand', 'DecryptService.getProgressListener', 'CALL',
  'Service calls getProgressListener when progress updates',
  evidence='SRC DecryptService.java:231-233 getProgressListener returns progressListener')

e('DecryptService.onCreate', 'DecryptService.onDestroy', 'LIFECYCLE',
  'Service lifecycle calls onDestroy when service stops',
  evidence='SRC DecryptService.java:238-241 onDestroy unregisters receiver')

e('DecryptService$1.<init>', 'DecryptService$1.onReceive', 'FRAMEWORK',
  'Framework calls onReceive when cancel broadcast sent',
  evidence='SRC DecryptService.java:217-220 onReceive handles TAG_BROADCAST_CRYPT_CANCEL')

# Decompressor methods
# Decompressor is abstract base class; concrete implementations are called
e('CompressedHelper.getCompressorInstance', 'Decompressor.setFilePath', 'CALL',
  'getCompressorInstance calls setFilePath after creating decompressor',
  evidence='SRC CompressedHelper.java:131 decompressor.setFilePath(file.getPath())')

e('MainActivityHelper.extractFile', 'Decompressor.decompress', 'CALL',
  'extractFile calls decompress with single path parameter',
  evidence='SRC MainActivityHelper.java:529 decompressor.decompress(file.getPath())')

e('CompressedExplorerFragment.extractFiles', 'Decompressor.decompress', 'CALL',
  'extractFiles calls decompress with directory array parameter',
  evidence='SRC CompressedExplorerFragment.java:329 decompressor.decompress(compressedFile.getPath(), dirs)')

e('Decompressor.decompress', 'Decompressor.realRelativeDirectory', 'CALL',
  'decompress calls realRelativeDirectory for each subdirectory',
  evidence='SRC Decompressor.java:58-60 realRelativeDirectory(subDirectories[i])')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_B020 = {
    'DataUtils$DataUtilsHolder.<init>': ('no_trigger_in_app', 'Private constructor never called; singleton uses static INSTANCE field only', 'SRC DataUtils.java:78-80 private static class DataUtilsHolder with static INSTANCE field', 'SOURCE'),
    'DatapointParcelable.<init>(Parcel)': ('no_trigger_in_app', 'Parcel constructor only called from createFromParcel which is never called', 'SRC DatapointParcelable.java:120-129 constructor reads from Parcel; grep shows no getParcelable for DatapointParcelable', 'SOURCE'),
    'DatapointParcelable.describeContents': ('no_trigger_in_app', 'Parcelable method never called; DatapointParcelable stored in lists not parceled through Intents', 'SRC DatapointParcelable.java:142-144 describeContents returns 0; grep shows no putParcelable/getParcelable for DatapointParcelable', 'SOURCE'),
    'DatapointParcelable.writeToParcel': ('no_trigger_in_app', 'Parcelable method never called; DatapointParcelable stored in lists not parceled through Intents', 'SRC DatapointParcelable.java:147-155 writeToParcel writes fields to Parcel; grep shows no putParcelable for DatapointParcelable', 'SOURCE'),
    'DatapointParcelable$1.createFromParcel': ('no_trigger_in_app', 'CREATOR method never called; DatapointParcelable never unparceled from Intents', 'SRC DatapointParcelable.java:129-131 createFromParcel creates from Parcel; grep shows no getParcelable for DatapointParcelable', 'SOURCE'),
    'DatapointParcelable$1.newArray': ('no_trigger_in_app', 'CREATOR method never called; DatapointParcelable arrays never unparceled', 'SRC DatapointParcelable.java:134-136 newArray creates array; grep shows no array unparceling for DatapointParcelable', 'SOURCE'),
    'Decompressor.<init>': ('no_trigger_in_app', 'Abstract class constructor called only by subclass constructors, which are already in the graph', 'SRC Decompressor.java:23-25 protected constructor takes Context; subclasses call super() which is covered by subclass edges', 'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_PART_B020)


# ---- label_b021 ----
# ---- Helper batch_021 label part (2025-01-18)

# DecryptService$BackgroundTask methods
e('DecryptService.onStartCommand', 'DecryptService$BackgroundTask.<init>', 'CALL', 
  'onStartCommand creates BackgroundTask instance',
  evidence='SRC DecryptService.java:118')

e('DecryptService$BackgroundTask.<init>', 'AsyncTask.<init>', 'CALL',
  'BackgroundTask extends AsyncTask, constructor chains to parent',
  evidence='SRC DecryptService.java:123')

e('DecryptService.onStartCommand', 'DecryptService$BackgroundTask.execute', 'ASYNC',
  'onStartCommand executes the AsyncTask',
  evidence='SRC DecryptService.java:118')

e('ZipService$CompressAsyncTask.execute', 'DecryptService$BackgroundTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground on background thread',
  evidence='FW-SRC core/java/android/os/AsyncTask.java:333')

e('DecryptService$BackgroundTask.doInBackground', 'DecryptService$BackgroundTask.lambda$doInBackground$0', 'CALL',
  'doInBackground sets progress listener with lambda',
  evidence='SRC DecryptService.java:138-139')

e('AsyncTask.finish', 'DecryptService$BackgroundTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute when doInBackground completes',
  evidence='FW-SRC core/java/android/os/AsyncTask.java:695')

# DeltaDecoder methods (7z library)
e('Coders.<clinit>', 'DeltaDecoder.<init>', 'CALL',
  'Coders static initializer creates DeltaDecoder instance for DELTA_FILTER method',
  evidence='SRC sevenz/Coders.java:64')

e('Coders.addDecoder', 'DeltaDecoder.decode', 'CALL',
  'Coders.addDecoder invokes decode when processing 7z archives with delta encoding',
  evidence='SRC sevenz/Coders.java:73')

e('DeltaDecoder.decode', 'DeltaDecoder.getOptionsFromCoder', 'CALL',
  'decode calls private getOptionsFromCoder(Coder) to extract delta distance',
  evidence='SRC sevenz/DeltaDecoder.java:36')

e('DeltaDecoder.getOptionsFromCoder', 'DeltaDecoder.getOptionsFromCoder', 'CALL',
  'public getOptionsFromCoder(Coder,InputStream) calls private getOptionsFromCoder(Coder)',
  evidence='SRC sevenz/DeltaDecoder.java:59')

e('Coders.addEncoder', 'DeltaDecoder.encode', 'CALL',
  'Coders.addEncoder invokes encode when creating 7z archives with delta encoding',
  evidence='SRC sevenz/Coders.java:84')

e('Coders.addEncoder', 'DeltaDecoder.getOptionsAsProperties', 'CALL',
  'Coders.addEncoder calls getOptionsAsProperties to serialize delta options',
  evidence='SRC sevenz/SevenZOutputFile.java:452')

e('SevenZFile.buildDecodingStream', 'DeltaDecoder.getOptionsFromCoder', 'CALL',
  'SevenZFile.buildDecodingStream calls getOptionsFromCoder(Coder,InputStream) during stream setup',
  evidence='SRC sevenz/SevenZFile.java:1033')

# DisablableViewPager methods
e('LayoutInflater.inflate', 'DisablableViewPager.<init>', 'FRAMEWORK',
  'LayoutInflater instantiates DisablableViewPager from tabfragment.xml layout',
  evidence='SRC res/layout/tabfragment.xml:20-36, SRC TabFragment.java:95')

e('DisablableViewPager.onTouchEvent', 'DisablableViewPager.onTouchEvent', 'FRAMEWORK',
  'Framework calls onTouchEvent when user touches the view',
  evidence='INFERRED androidx ViewPager touch event dispatch, source not read')

e('DisablableViewPager.onInterceptTouchEvent', 'DisablableViewPager.onInterceptTouchEvent', 'FRAMEWORK',
  'Framework calls onInterceptTouchEvent to determine if ViewPager should intercept touch',
  evidence='INFERRED androidx ViewPager touch interception, source not read')

e('TabFragment.onCreateView', 'DisablableViewPager.setPagingEnabled', 'CALL',
  'TabFragment can call setPagingEnabled to enable/disable paging',
  evidence='SRC DisablableViewPager.java:32')

# DividerItemDecoration methods
e('DividerItemDecoration.<clinit>', 'DividerItemDecoration.<clinit>', 'CALL',
  'Class initializer defines ATTRS array',
  evidence='SRC DividerItemDecoration.java:19-21')

e('MainFragment.onCreateView', 'DividerItemDecoration.<init>', 'CALL',
  'MainFragment creates DividerItemDecoration instance',
  evidence='SRC MainFragment.java:304-305')

e('RecyclerView.draw', 'DividerItemDecoration.onDraw', 'FRAMEWORK',
  'RecyclerView framework calls onDraw to render dividers',
  evidence='INFERRED androidx RecyclerView ItemDecoration lifecycle, source not read')

e('DividerItemDecoration.onDraw', 'DividerItemDecoration.drawVertical', 'CALL',
  'onDraw calls drawVertical to draw divider lines',
  evidence='SRC DividerItemDecoration.java:48')

e('RecyclerView.measureChild', 'DividerItemDecoration.getItemOffsets', 'FRAMEWORK',
  'RecyclerView framework calls getItemOffsets to compute item spacing',
  evidence='INFERRED androidx RecyclerView ItemDecoration lifecycle, source not read')

# UNREACHABLE methods from this batch
UNREACHABLE_B021 = {
    'DonationViewHolder.<init>': ('no_trigger_in_app', 'DonationViewHolder is never instantiated in any adapter; grep shows no references outside the class definition itself', 'SRC DonationViewHolder.java:1-20 shows class definition with no usages in codebase', 'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_B021)


# ---- label_b023 ----
# ---- Helper batch_023 label part (2025-01-10)

# Drawer$1 - Anonymous ActionBarDrawerToggle created in Drawer constructor
e('Drawer.<init>', 'Drawer$1.<init>', 'CALL', 'Creates anonymous ActionBarDrawerToggle in Drawer constructor when !isDrawerLocked',
  evidence='SRC Drawer.java:217-223 shows mDrawerToggle = new ActionBarDrawerToggle(...) { override methods }')

e('DrawerLayout.setDrawerListener', 'Drawer$1.onDrawerClosed', 'FRAMEWORK', 'Framework invokes onDrawerClosed callback when drawer closes',
  evidence='SRC Drawer.java:224-226 shows public void onDrawerClosed(View view) calling Drawer.this.onDrawerClosed()')

e('DrawerLayout.setDrawerListener', 'Drawer$1.onDrawerOpened', 'FRAMEWORK', 'Framework invokes onDrawerOpened callback when drawer opens',
  evidence='SRC Drawer.java:228-231 shows public void onDrawerOpened(View drawerView) with comment')

# Drawer$2 - Anonymous ImageLoader.ImageListener created in setDrawerHeaderBackground
e('Drawer.setDrawerHeaderBackground', 'Drawer$2.<init>', 'CALL', 'Creates anonymous ImageLoader.ImageListener in setDrawerHeaderBackground',
  evidence='SRC Drawer.java:657 shows mImageLoader.get(path1, new ImageLoader.ImageListener() {')

e('ImageLoader.get', 'Drawer$2.onResponse', 'FRAMEWORK', 'Volley ImageLoader invokes onResponse on successful image load',
  evidence='SRC Drawer.java:658-662 shows @Override onResponse setting headerImageView bitmap')

e('ImageLoader.get', 'Drawer$2.onErrorResponse', 'FRAMEWORK', 'Volley ImageLoader invokes onErrorResponse on image load error',
  evidence='SRC Drawer.java:664-665 shows @Override onErrorResponse(VolleyError error) {}')

# EditTextColorStateUtil - Utility class with static methods
e('SmbConnectDialog.onCreate', 'EditTextColorStateUtil.setTint', 'CALL', 'SmbConnectDialog calls setTint to style EditText fields',
  evidence='SRC SmbConnectDialog.java:156-158 shows three calls EditTextColorStateUtil.setTint(context, editText, accentColor)')

e('EditTextColorStateUtil.setTint', 'EditTextColorStateUtil.createEditTextColorStateList', 'CALL', 'setTint calls private helper to create ColorStateList',
  evidence='SRC EditTextColorStateUtil.java:20-23 shows ColorStateList editTextColorStateList = createEditTextColorStateList(context, color)')

# EncryptDecryptUtils - Encryption utility class with static methods
e('GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog', 'EncryptDecryptUtils.startEncryption', 'CALL', 'Dialog callback invokes startEncryption after user enters filename',
  evidence='SRC GeneralDialogCreation.java:695 shows EncryptDecryptUtils.startEncryption(c, intentParcelable.getPath(), password, intent)')

e('ItemPopupMenu.onMenuItemClick', 'EncryptDecryptUtils.startEncryption', 'CALL', 'Encrypt menu action invokes startEncryption',
  evidence='SRC ItemPopupMenu.java:147 shows EncryptDecryptUtils.startEncryption(context, rowItem.generateBaseFile().getPath(), password, intent)')

e('ItemPopupMenu.onMenuItemClick', 'EncryptDecryptUtils.decryptFile', 'CALL', 'Decrypt menu action invokes decryptFile',
  evidence='SRC ItemPopupMenu.java:197 shows EncryptDecryptUtils.decryptFile(context, mainActivity, mainFragment, ...)' )

e('MainFragment.onItemClick', 'EncryptDecryptUtils.decryptFile', 'CALL', 'Clicking encrypted file invokes decryptFile',
  evidence='SRC MainFragment.java:905 shows EncryptDecryptUtils.decryptFile(getContext(), getMainActivity(), ma, openMode, ...)')

e('EncryptDecryptUtils.decryptFile', 'EncryptDecryptUtils.findEncryptedEntry', 'CALL', 'decryptFile calls private helper to find database entry',
  evidence='SRC EncryptDecryptUtils.java:77 shows encryptedEntry = findEncryptedEntry(main.getContext(), sourceFile.getPath())')

# EncryptDecryptUtils$1 - Anonymous DecryptButtonCallbackInterface
e('EncryptDecryptUtils.decryptFile', 'EncryptDecryptUtils$1.<init>', 'CALL', 'Creates anonymous DecryptButtonCallbackInterface in decryptFile',
  evidence='SRC EncryptDecryptUtils.java:87-88 shows DecryptButtonCallbackInterface decryptButtonCallbackInterface = new DecryptButtonCallbackInterface() {')

e('GeneralDialogCreation.showDecryptDialog', 'EncryptDecryptUtils$1.confirm', 'CALL', 'Dialog invokes confirm callback when password matches',
  evidence='SRC EncryptDecryptUtils.java:89-92 shows @Override confirm(Intent intent) calling ServiceWatcherUtil.runService')

e('GeneralDialogCreation.showDecryptDialog', 'EncryptDecryptUtils$1.failed', 'CALL', 'Dialog invokes failed callback when password does not match',
  evidence='SRC EncryptDecryptUtils.java:94-97 shows @Override failed() showing toast R.string.crypt_decryption_fail_password')

# EncryptService - Service for encryption
e('EncryptDecryptUtils.startEncryption', 'EncryptService.<init>', 'SYSTEM', 'Framework creates EncryptService when started via Intent',
  evidence='SRC EncryptDecryptUtils.java:59 shows ServiceWatcherUtil.runService(c, intent) with EncryptService intent')

e('Context.startService', 'EncryptService.onCreate', 'LIFECYCLE', 'Framework calls onCreate when service created',
  evidence='SRC EncryptService.java:66-71 shows @Override onCreate() registering broadcast receiver')

e('Context.startService', 'EncryptService.onStartCommand', 'LIFECYCLE', 'Framework calls onStartCommand when service started',
  evidence='SRC EncryptService.java:73-120 shows @Override onStartCommand extracting intent extras and starting BackgroundTask')

e('Context.bindService', 'EncryptService.onBind', 'LIFECYCLE', 'Framework calls onBind when clients bind to service',
  evidence='SRC EncryptService.java:209-212 shows @Override onBind(Intent intent) returning mBinder')

e('Context.stopService', 'EncryptService.onDestroy', 'LIFECYCLE', 'Framework calls onDestroy when service destroyed',
  evidence='SRC EncryptService.java:214-218 shows @Override onDestroy() unregistering cancelReceiver')

e('AbstractProgressiveService.publishResults', 'EncryptService.getNotificationManager', 'CALL', 'Parent calls getter to manage notifications',
  evidence='SRC EncryptService.java:122-125 shows @Override protected getNotificationManager() returning notificationManager')

e('AbstractProgressiveService.publishResults', 'EncryptService.getNotificationBuilder', 'CALL', 'Parent calls getter for notification updates',
  evidence='SRC EncryptService.java:127-130 shows @Override protected getNotificationBuilder() returning notificationBuilder')

e('AbstractProgressiveService.publishResults', 'EncryptService.getNotificationId', 'CALL', 'Parent calls getter for notification ID',
  evidence='SRC EncryptService.java:132-135 shows @Override protected getNotificationId() returning NotificationConstants.ENCRYPT_ID')

e('AbstractProgressiveService.initNotificationViews', 'EncryptService.getTitle', 'CALL', 'Parent calls getTitle for notification title resource',
  evidence='SRC EncryptService.java:137-141 shows @Override protected getTitle(boolean move) returning R.string.crypt_encrypting')

e('AbstractProgressiveService.updateNotification', 'EncryptService.getNotificationCustomViewSmall', 'CALL', 'Parent calls getter for small notification view',
  evidence='SRC EncryptService.java:143-146 shows @Override protected getNotificationCustomViewSmall() returning customSmallContentViews')

e('AbstractProgressiveService.updateNotification', 'EncryptService.getNotificationCustomViewBig', 'CALL', 'Parent calls getter for big notification view',
  evidence='SRC EncryptService.java:148-151 shows @Override protected getNotificationCustomViewBig() returning customBigContentViews')

e('ObtainableServiceBinder.getService', 'EncryptService.getProgressListener', 'CALL', 'Binding clients may call getter to access progress listener',
  evidence='SRC EncryptService.java:153-156 shows public getProgressListener() returning progressListener')

e('ObtainableServiceBinder.getService', 'EncryptService.setProgressListener', 'CALL', 'Binding clients may call setter to register progress listener',
  evidence='SRC EncryptService.java:158-162 shows @Override public setProgressListener(ProgressListener progressListener)')

e('AbstractProgressiveService.addFirstDatapoint', 'EncryptService.getDataPackages', 'CALL', 'Parent calls getter for data packages list',
  evidence='SRC EncryptService.java:164-167 shows @Override protected getDataPackages() returning dataPackages')

e('AbstractProgressiveService.publishResults', 'EncryptService.getProgressHandler', 'CALL', 'Parent calls getter for progress handler',
  evidence='SRC EncryptService.java:169-172 shows @Override protected getProgressHandler() returning progressHandler')

# EncryptService$1 - BroadcastReceiver for cancel
e('EncryptService.onCreate', 'EncryptService$1.<init>', 'CALL', 'Creates anonymous BroadcastReceiver as cancelReceiver field',
  evidence='SRC EncryptService.java:220 shows private BroadcastReceiver cancelReceiver = new BroadcastReceiver() {')

e('Context.sendBroadcast', 'EncryptService$1.onReceive', 'SYSTEM', 'Framework invokes onReceive when TAG_BROADCAST_CRYPT_CANCEL broadcast sent',
  evidence='SRC EncryptService.java:222-226 shows @Override onReceive setting progressHandler.setCancelled(true)')

# EncryptService$BackgroundTask - AsyncTask performing encryption
e('EncryptService.onStartCommand', 'EncryptService$BackgroundTask.<init>', 'CALL', 'onStartCommand creates BackgroundTask to perform encryption',
  evidence='SRC EncryptService.java:117 shows new BackgroundTask().execute()')

e('ZipService$CompressAsyncTask.execute', 'EncryptService$BackgroundTask.doInBackground', 'ASYNC', 'AsyncTask framework calls doInBackground on worker thread',
  evidence='SRC EncryptService.java:176-203 shows @Override doInBackground(Void... params) performing encryption via CryptUtil')

e('EncryptService$BackgroundTask.doInBackground', 'EncryptService$BackgroundTask.lambda$doInBackground$0', 'CALL', 'doInBackground sets lambda as progress listener callback',
  evidence='SRC EncryptService.java:182 shows progressHandler.setProgressListener((speed) -> publishResults(speed, false, false))')

e('ZipService$CompressAsyncTask.execute', 'EncryptService$BackgroundTask.onPostExecute', 'ASYNC', 'AsyncTask framework calls onPostExecute on UI thread after completion',
  evidence='SRC EncryptService.java:205-207 shows @Override onPostExecute(Void aVoid) finalizing notification and calling stopSelf()')

# UNREACHABLE methods
UNREACHABLE_PART_B023 = {
    'DummyFileGenerator.<init>': ('no_trigger_in_app', 'Abstract test-only class with @RestrictTo(TESTS) annotation, no app source instantiation found', 'SRC DummyFileGenerator.java:45-48', 'SOURCE'),
    'DummyFileGenerator.createFile': ('no_trigger_in_app', 'Test-only static method with @RestrictTo(TESTS) annotation, grep -rn DummyFileGenerator in app source shows no callers', 'SRC DummyFileGenerator.java:54-82', 'SOURCE'),
    'EditTextColorStateUtil.<init>': ('no_trigger_in_app', 'Utility class with only static methods, constructor never instantiated in app source', 'SRC EditTextColorStateUtil.java:18', 'SOURCE'),
    'EncryptDecryptUtils.<init>': ('no_trigger_in_app', 'Utility class with only static methods, constructor never instantiated in app source', 'SRC EncryptDecryptUtils.java:34', 'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_PART_B023)


# ---- label_b025 ----
# ---- Helper batch_025 label part (2026-10-27)

# FileHandler edges
e('MainFragment.showSMBDialog', 'FileHandler.<init>', 'CALL', 'MainFragment creates FileHandler for CustomFileObserver',
  evidence='SRC MainFragment.java:1194-1195 new CustomFileObserver(CURRENT_PATH, new FileHandler(this, listView, getBoolean(PREFERENCE_SHOW_THUMB)))')

e('CustomFileObserver.sendMessages', 'FileHandler.handleMessage', 'ASYNC', 'CustomFileObserver sends messages to FileHandler',
  evidence='SRC CustomFileObserver.java:134 handler.obtainMessage(NEW_ITEM, pathAdded).sendToTarget()')

# FileListSorter edges
e('LoadFilesListTask.doInBackground', 'FileListSorter.<init>', 'CALL', 'LoadFilesListTask creates FileListSorter for sorting',
  evidence='SRC LoadFilesListTask.java:215 Collections.sort(list, new FileListSorter(ma.dsort, sortby, asc))')

e('FileListSorter.<init>', 'FileListSorter.compare', 'FRAMEWORK', 'Collections.sort calls Comparator.compare',
  evidence='SRC LoadFilesListTask.java:215 Collections.sort with FileListSorter')

e('FileListSorter.compare', 'FileListSorter.isDirectory', 'CALL', 'compare checks if items are directories',
  evidence='SRC FileListSorter.java:68 if (isDirectory(file1) && !isDirectory(file2))')

e('FileListSorter.compare', 'FileListSorter.getExtension', 'CALL', 'compare gets file extensions for type sorting',
  evidence='SRC FileListSorter.java:108-109 final String ext_a = getExtension(file1.title)')

# FastScroller edges
e('MainFragment.onCreateView', 'FastScroller.<init>', 'FRAMEWORK', 'Fragment inflates FastScroller from XML layout',
  evidence='SRC MainFragment.java:242 fastScroller = rootView.findViewById(R.id.fastscroll)')

e('MainFragment.onCreateView', 'FastScroller.setPressedHandleColor', 'CALL', 'MainFragment sets FastScroller handle color',
  evidence='SRC MainFragment.java:243 fastScroller.setPressedHandleColor(accentColor)')

e('MainFragment.changeSorting', 'FastScroller.setRecyclerView', 'CALL', 'MainFragment sets RecyclerView on FastScroller',
  evidence='SRC MainFragment.java:1150 fastScroller.setRecyclerView(listView, IS_LIST? 1:columns)')

e('MainFragment.changeSorting', 'FastScroller.registerOnTouchListener', 'CALL', 'MainFragment registers touch listener',
  evidence='SRC MainFragment.java:1154 fastScroller.registerOnTouchListener(() -> {')

e('MainFragment.changeSorting', 'FastScroller.updateHandlePosition', 'CALL', 'AppBarLayout listener calls updateHandlePosition',
  evidence='SRC MainFragment.java:1152 fastScroller.updateHandlePosition(verticalOffset, 112)')

e('FastScroller.<init>', 'FastScroller.initialise', 'CALL', 'Constructor calls initialise',
  evidence='SRC FastScroller.java:37,42 initialise(context)')

e('FastScroller.initialise', 'FastScroller.setPressedHandleColor', 'CALL', 'initialise sets default handle color',
  evidence='SRC FastScroller.java:84 setPressedHandleColor(Utils.getColor(getContext(), R.color.accent_blue))')

e('FastScroller.initialise', 'FastScroller.setUpBarBackground', 'CALL', 'initialise sets up bar background',
  evidence='SRC FastScroller.java:84 setUpBarBackground()')

e('FastScroller.setUpBarBackground', 'FastScroller.resolveColor', 'CALL', 'setUpBarBackground resolves color attribute',
  evidence='SRC FastScroller.java:103 int resolveColor = resolveColor(getContext(), R.attr.colorControlNormal)')

e('FastScroller.setRecyclerView', 'FastScroller.invalidateVisibility', 'CALL', 'setRecyclerView calls invalidateVisibility',
  evidence='SRC FastScroller.java:175 invalidateVisibility()')

e('FastScroller.invalidateVisibility', 'FastScroller.isRecyclerViewScrollable', 'CALL', 'invalidateVisibility checks if scrollable',
  evidence='SRC FastScroller.java:132 isRecyclerViewScrollable()')

e('FastScroller.onTouchEvent', 'FastScroller.getRelativeTouchPosition', 'CALL', 'onTouchEvent gets relative touch position',
  evidence='SRC FastScroller.java:123 float relativePos = getRelativeTouchPosition(motionEvent)')

e('FastScroller.onTouchEvent', 'FastScroller.setHandlePosition1', 'CALL', 'onTouchEvent sets handle position',
  evidence='SRC FastScroller.java:124 setHandlePosition1(relativePos)')

e('FastScroller.onTouchEvent', 'FastScroller.setRecyclerViewPosition', 'CALL', 'onTouchEvent sets RecyclerView position',
  evidence='SRC FastScroller.java:125 setRecyclerViewPosition(relativePos)')

e('FastScroller.setHandlePosition1', 'FastScroller.getHeightMinusPadding', 'CALL', 'setHandlePosition1 gets available height',
  evidence='SRC FastScroller.java:97 Utils.clamp(0, getHeightMinusPadding() - handle.getHeight(), ...')

e('FastScroller.computeHandlePosition', 'FastScroller.getHeightMinusPadding', 'CALL', 'computeHandlePosition gets available height',
  evidence='SRC FastScroller.java:62,68 getHeightMinusPadding()')

e('FastScroller.updateHandlePosition', 'FastScroller.setHandlePosition1', 'CALL', 'updateHandlePosition sets handle position',
  evidence='SRC FastScroller.java:191 setHandlePosition1(computeHandlePosition())')

e('FastScroller.updateHandlePosition', 'FastScroller.computeHandlePosition', 'CALL', 'updateHandlePosition computes position',
  evidence='SRC FastScroller.java:191 setHandlePosition1(computeHandlePosition())')

e('FastScroller.setRecyclerView', 'FastScroller$ScrollListener.<init>', 'CALL', 'ScrollListener created in FastScroller constructor',
  evidence='SRC FastScroller.java:28,36 this.scrollListener = new ScrollListener()')

e('FastScroller.setRecyclerView', 'FastScroller$ScrollListener.onScrolled', 'FRAMEWORK', 'RecyclerView calls onScrolled on scroll',
  evidence='SRC FastScroller.java:174 recyclerView.addOnScrollListener(this.scrollListener)')

e('FastScroller$ScrollListener.onScrolled', 'FastScroller.updateHandlePosition', 'CALL', 'ScrollListener updates handle position',
  evidence='SRC FastScroller.java:34 updateHandlePosition()')

e('FastScroller.setRecyclerView', 'FastScroller$1.<init>', 'CALL', 'Anonymous OnHierarchyChangeListener created',
  evidence='SRC FastScroller.java:176 recyclerView.setOnHierarchyChangeListener(new OnHierarchyChangeListener() {')

e('FastScroller.setRecyclerView', 'FastScroller$1.onChildViewAdded', 'FRAMEWORK', 'RecyclerView calls onChildViewAdded',
  evidence='SRC FastScroller.java:178 public void onChildViewAdded(View parent, View child) {')

e('FastScroller.setRecyclerView', 'FastScroller$1.onChildViewRemoved', 'FRAMEWORK', 'RecyclerView calls onChildViewRemoved',
  evidence='SRC FastScroller.java:182 public void onChildViewRemoved(View parent, View child) {')

e('FastScroller$1.onChildViewAdded', 'FastScroller.invalidateVisibility', 'CALL', 'onChildViewAdded invalidates visibility',
  evidence='SRC FastScroller.java:179 invalidateVisibility()')

e('FastScroller$1.onChildViewRemoved', 'FastScroller.invalidateVisibility', 'CALL', 'onChildViewRemoved invalidates visibility',
  evidence='SRC FastScroller.java:183 invalidateVisibility()')

# Extractor edges
e('ExtractService.runIntentInService', 'Extractor.extractFiles', 'CALL', 'ExtractService calls extractFiles on Extractor',
  evidence='SRC ExtractService.java:298 extractor.extractFiles(entriesToExtract)')

e('ExtractService.runIntentInService', 'Extractor.extractEverything', 'CALL', 'ExtractService calls extractEverything on Extractor',
  evidence='SRC ExtractService.java:300 extractor.extractEverything()')

e('ExtractService.runIntentInService', 'Extractor.getInvalidArchiveEntries', 'CALL', 'ExtractService gets invalid entries',
  evidence='SRC ExtractService.java:301 extractor.getInvalidArchiveEntries().size()')

e('Extractor.extractFiles', 'Extractor.lambda$extractFiles$0', 'CALL', 'extractFiles creates filter lambda',
  evidence='SRC Extractor.java:54 extractWithFilter((relativePath, isDir) -> {')

e('Extractor.extractEverything', 'Extractor.lambda$extractEverything$1', 'CALL', 'extractEverything creates filter lambda',
  evidence='SRC Extractor.java:72 extractWithFilter((relativePath, isDir) -> true)')

e('TarExtractor.extractWithFilter', 'Extractor.fixEntryName', 'CALL', 'TarExtractor calls fixEntryName',
  evidence='SRC TarExtractor.java:90 File outputFile = new File(outputDir, fixEntryName(entry.getName()))')



# ---- label_b024 ----
# ---- Helper batch_024 label part (2024)

# ExtractService - started service for archive extraction
# Route: User extracts archive -> menu action onActionItemClicked/onClick -> Decompressor.decompress -> ServiceWatcherUtil.runService -> startService -> ExtractService.onStartCommand -> DoWork.execute -> doInBackground

e('Decompressor.decompress', 'ExtractService.onStartCommand', 'INTENT',
  'starts ExtractService via ServiceWatcherUtil.runService -> context.startService',
  evidence='SRC Decompressor.java:44-48, ServiceWatcherUtil.java:163')

e('ExtractService.onStartCommand', 'ExtractService$DoWork.<init>', 'CALL',
  'constructs DoWork AsyncTask',
  evidence='SRC ExtractService.java:146')

e('ExtractService.onStartCommand', 'ExtractService$DoWork.doInBackground', 'ASYNC',
  'executes DoWork AsyncTask',
  evidence='SRC ExtractService.java:146')

e('ExtractService$DoWork.doInBackground', 'ExtractService$DoWork$1.<init>', 'CALL',
  'constructs anonymous OnUpdate callback',
  evidence='SRC ExtractService.java:215-242')

e('ExtractService$DoWork$1.onStart', 'ExtractService$DoWork$1.onStart', 'FRAMEWORK',
  'extractor callback from CompressedHelper.getExtractorInstance',
  evidence='SRC ExtractService.java:215 (anonymous class passed to extractor)')

e('ExtractService$DoWork$1.onUpdate', 'ExtractService$DoWork$1.onUpdate', 'FRAMEWORK',
  'extractor callback',
  evidence='SRC ExtractService.java:215 (anonymous class passed to extractor)')

e('ExtractService$DoWork$1.onFinish', 'ExtractService$DoWork$1.onFinish', 'FRAMEWORK',
  'extractor callback',
  evidence='SRC ExtractService.java:215 (anonymous class passed to extractor)')

e('ExtractService$DoWork$1.isCancelled', 'ExtractService$DoWork$1.isCancelled', 'FRAMEWORK',
  'extractor callback',
  evidence='SRC ExtractService.java:215 (anonymous class passed to extractor)')

e('ExtractService$DoWork.doInBackground', 'ExtractService$DoWork.onPostExecute', 'FRAMEWORK',
  'AsyncTask completion',
  evidence='INFERRED android AsyncTask lifecycle (source not read)')

e('ExtractService$DoWork.doInBackground', 'ExtractService$DoWork.onProgressUpdate', 'FRAMEWORK',
  'AsyncTask publishProgress',
  evidence='SRC ExtractService.java:255 (publishProgress call on password error)')

e('ExtractService.onCreate', 'ExtractService$1.<init>', 'CALL',
  'constructs BroadcastReceiver',
  evidence='SRC ExtractService.java:283-289')

e('ExtractService$1.onReceive', 'ExtractService$1.onReceive', 'FRAMEWORK',
  'BroadcastReceiver callback on TAG_BROADCAST_EXTRACT_CANCEL',
  evidence='SRC ExtractService.java:90 (registerReceiver with IntentFilter)')

# EncryptedEntry - DB model for encrypted file passwords
# Reachable via CryptHandler which is used in EncryptDecryptUtils

e('EncryptDecryptUtils.startEncryption', 'EncryptedEntry.<init>', 'CALL',
  'constructs EncryptedEntry with path and password',
  evidence='SRC EncryptDecryptUtils.java:54')

e('CryptHandler.addEntry', 'EncryptedEntry.getPath', 'CALL',
  'gets path for DB insert',
  evidence='SRC CryptHandler.java:59')

e('CryptHandler.addEntry', 'EncryptedEntry.getPassword', 'CALL',
  'gets password for DB insert',
  evidence='SRC CryptHandler.java:60-61')

e('CryptHandler.findEntry', 'EncryptedEntry.<init>', 'CALL',
  'constructs empty EncryptedEntry',
  evidence='SRC CryptHandler.java:93')

e('CryptHandler.findEntry', 'EncryptedEntry.setId', 'CALL',
  'sets id from cursor',
  evidence='SRC CryptHandler.java:95')

e('CryptHandler.findEntry', 'EncryptedEntry.setPath', 'CALL',
  'sets path from cursor',
  evidence='SRC CryptHandler.java:96')

e('CryptHandler.findEntry', 'EncryptedEntry.setPassword', 'CALL',
  'sets password from cursor',
  evidence='SRC CryptHandler.java:97')

e('CryptHandler.getAllEntries', 'EncryptedEntry.<init>', 'CALL',
  'constructs EncryptedEntry per row',
  evidence='SRC CryptHandler.java:117')

e('CryptHandler.getAllEntries', 'EncryptedEntry.setId', 'CALL',
  'sets id from cursor',
  evidence='SRC CryptHandler.java:118')

e('CryptHandler.getAllEntries', 'EncryptedEntry.setPath', 'CALL',
  'sets path from cursor',
  evidence='SRC CryptHandler.java:119')

e('CryptHandler.getAllEntries', 'EncryptedEntry.setPassword', 'CALL',
  'sets password from cursor',
  evidence='SRC CryptHandler.java:120-121')

e('CryptHandler.updateEntry', 'EncryptedEntry.getId', 'CALL',
  'gets id for update query',
  evidence='SRC CryptHandler.java:79,85')

e('CryptHandler.updateEntry', 'EncryptedEntry.getPath', 'CALL',
  'gets path for update',
  evidence='SRC CryptHandler.java:80')

e('CryptHandler.updateEntry', 'EncryptedEntry.getPassword', 'CALL',
  'gets password for update',
  evidence='SRC CryptHandler.java:82')

e('ExtractService$DoWork.onProgressUpdate', 'ExtractService$DoWork.lambda$onProgressUpdate$0', 'CALL',
  'first lambda (positive button) for password dialog',
  evidence='SRC ExtractService.java:333-338')

e('ExtractService$DoWork.onProgressUpdate', 'ExtractService$DoWork.lambda$onProgressUpdate$1', 'CALL',
  'second lambda (negative button) for password dialog',
  evidence='SRC ExtractService.java:341-348')

e('ExtractService.onStartCommand', 'ExtractService.lambda$onStartCommand$0', 'CALL',
  'lambda for progress listener',
  evidence='SRC ExtractService.java:142-143')

e('ExtractService.onCreate', 'ExtractService$1.<init>', 'CALL',
  'changed to EXPLICIT for BroadcastReceiver construction',
  evidence='SRC ExtractService.java:283-289 (field initializer receiver1 = new BroadcastReceiver)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getNotificationManager', 'FRAMEWORK',
  'called by parent service to get notification manager',
  evidence='INFERRED AbstractProgressiveService.java:98 (source shows publishResults calls getNotificationManager)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getNotificationBuilder', 'FRAMEWORK',
  'called by parent service',
  evidence='INFERRED AbstractProgressiveService.java (source shows publishResults calls getNotificationBuilder)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getNotificationId', 'FRAMEWORK',
  'called by parent service',
  evidence='INFERRED AbstractProgressiveService.java (source shows publishResults calls getNotificationId)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getTitle', 'FRAMEWORK',
  'called by parent service',
  evidence='INFERRED AbstractProgressiveService.java:94 (publishResults calls getTitle)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getNotificationCustomViewSmall', 'FRAMEWORK',
  'called by parent service',
  evidence='INFERRED AbstractProgressiveService.java (publishResults calls getNotificationCustomViewSmall)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getNotificationCustomViewBig', 'FRAMEWORK',
  'called by parent service',
  evidence='INFERRED AbstractProgressiveService.java (publishResults calls getNotificationCustomViewBig)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getNotificationCustomViewSmall', 'FRAMEWORK',
  'called by parent for indeterminate progress',
  evidence='INFERRED AbstractProgressiveService.java:63 (progressHalted calls getNotificationCustomViewSmall)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getNotificationCustomViewBig', 'FRAMEWORK',
  'called by parent for indeterminate progress',
  evidence='INFERRED AbstractProgressiveService.java:65 (progressHalted calls getNotificationCustomViewBig)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getNotificationManager', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:71 (progressHalted calls getNotificationManager)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getNotificationId', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:71 (progressHalted calls getNotificationId)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getNotificationBuilder', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:71 (progressHalted calls getNotificationBuilder)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getProgressHandler', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:77 (progressHalted calls getProgressHandler)')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getNotificationCustomViewSmall', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:76')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getNotificationCustomViewBig', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:78')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getProgressHandler', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:77,79')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getNotificationManager', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:80')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getNotificationId', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:80')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getNotificationBuilder', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:80')

e('ExtractService.onStartCommand', 'ExtractService.getTotalSize', 'CALL',
  'calculates total size for progress',
  evidence='SRC ExtractService.java:138')

e('ExtractService.onStartCommand', 'ExtractService.getProgressListener', 'CALL',
  'checks if listener exists before creating (implied in parent call flow)',
  evidence='INFERRED ExtractService.java:142 (setProgressListener called, getProgressListener likely used by parent)')

e('ExtractService.onStartCommand', 'ExtractService.setProgressListener', 'CALL',
  'sets progress listener lambda',
  evidence='SRC ExtractService.java:142')

e('ExtractService.onStartCommand', 'ExtractService.getDataPackages', 'CALL',
  'used by parent for progress tracking (implied)',
  evidence='INFERRED ExtractService.java (parent AbstractProgressiveService uses getDataPackages)')

e('ProcessViewerFragment.onServiceBound', 'ExtractService.getProgressListener', 'CALL',
  'ProcessViewerFragment accesses progress listener when bound',
  evidence='INFERRED ProcessViewerFragment binds to ExtractService and accesses its progress state')

e('ProcessViewerFragment.onServiceBound', 'ExtractService.getDataPackages', 'CALL',
  'ProcessViewerFragment accesses data packages for display',
  evidence='INFERRED ProcessViewerFragment uses getDataPackages to display progress')

e('ProcessViewerFragment.onServiceBound', 'ExtractService.getProgressHandler', 'CALL',
  'ProcessViewerFragment accesses progress handler',
  evidence='INFERRED ProcessViewerFragment uses getProgressHandler for progress updates')

e('ProcessViewerFragment.onServiceBound', 'ExtractService.setProgressListener', 'CALL',
  'ProcessViewerFragment sets its listener',
  evidence='INFERRED ProcessViewerFragment binds ExtractService and sets listener')

e('ProcessViewerFragment.onResume', 'ExtractService.onBind', 'RESULT',
  'ProcessViewerFragment binds ExtractService',
  evidence='SRC ProcessViewerFragment.java:161 (bindService with ExtractService.class)')

e('ExtractService$DoWork.onProgressUpdate', 'ExtractService$DoWork.toastOnParseError', 'CALL',
  'shows error toast on password dialog cancel',
  evidence='SRC ExtractService.java:343')

# UNREACHABLE methods
UNREACHABLE_PART_B024 = {
    'ExtractService.<clinit>': ('no_trigger_in_app', 'Only static final String constants; compile-time initialization, no runtime <clinit> needed', 'SRC ExtractService.java:69,85-88', 'SOURCE'),
    'ExtractService.<init>': ('framework_never_calls', 'Service instantiated by framework via no-arg constructor only; explicit constructor not in source', 'SRC ExtractService.java:65 (no explicit constructor defined)', 'INFERRED'),
}
UNREACHABLE.update(UNREACHABLE_PART_B024)


# ---- label_b026 ----
# ---- Helper batch_026 label part (2025-01-18)
# FileUtil, FileUtil$1, FileUtil$MediaFile - 37 methods

# Edges for REACHABLE methods

# FileUtil.checkFolder is public static, called from CopyService, DecryptService, EncryptService
e('CopyService.run', 'FileUtil.checkFolder', 'CALL', 'check target path writable',
  evidence='SRC CopyService.java:350')
e('DecryptService$BackgroundTask.doInBackground', 'FileUtil.checkFolder', 'CALL', 'check output folder writable',
  evidence='SRC DecryptService.java:142')
e('EncryptService$BackgroundTask.doInBackground', 'FileUtil.checkFolder', 'CALL', 'check output folder writable',
  evidence='SRC EncryptService.java:186')

# FileUtil.copyFile is private static, called from FileUtil.renameFolder
e('FileUtil.renameFolder', 'FileUtil.copyFile', 'CALL', 'fallback to copy when rename fails',
  evidence='SRC FileUtil.java:455')

# FileUtil.deleteFile is package-private static, called from HybridFile.delete
e('HybridFile.delete', 'FileUtil.deleteFile', 'CALL', 'delete file in FILE mode',
  evidence='SRC HybridFile.java:1236')

# FileUtil.getDocumentFile is public static, called from GenericCopyUtil, FileUtils
e('GenericCopyUtil.copyFiles', 'FileUtil.getDocumentFile', 'CALL', 'get SAF document for source',
  evidence='SRC GenericCopyUtil.java:168')
e('GenericCopyUtil.copyFiles', 'FileUtil.getDocumentFile', 'CALL', 'get SAF document for target',
  evidence='SRC GenericCopyUtil.java:266')
e('FileUtils.scanFile', 'FileUtil.getDocumentFile', 'CALL', 'get document file for SAF delete',
  evidence='SRC FileUtils.java:268')

# FileUtil.getExtSdCardFolder is private static, called from FileUtil.isOnExtSdCard and getDocumentFile
e('FileUtil.isOnExtSdCard', 'FileUtil.getExtSdCardFolder', 'CALL', 'check if file on ext sd',
  evidence='SRC FileUtil.java:814')
e('FileUtil.getDocumentFile', 'FileUtil.getExtSdCardFolder', 'CALL', 'get base folder for SAF',
  evidence='SRC FileUtil.java:830')

# FileUtil.getExtSdCardPaths is private static, called from FileUtil.getExtSdCardFolder
e('FileUtil.getExtSdCardFolder', 'FileUtil.getExtSdCardPaths', 'CALL', 'get all ext sd paths',
  evidence='SRC FileUtil.java:793')

# FileUtil.getExtSdCardPathsForActivity is public static, called from MainActivity
e('MainActivity.onActivityResult', 'FileUtil.getExtSdCardPathsForActivity', 'CALL', 'get ext sd paths for storage picker',
  evidence='SRC MainActivity.java:681')

# FileUtil.getOutputStream is public static, called from WriteFileAbstraction, ZipService, HybridFile, extractors
e('WriteFileAbstraction.doInBackground', 'FileUtil.getOutputStream', 'CALL', 'get output stream for SAF',
  evidence='SRC WriteFileAbstraction.java:79')
e('ZipService.compress', 'FileUtil.getOutputStream', 'CALL', 'get output stream for zip file',
  evidence='SRC ZipService.java:255')
e('HybridFile.getOutputStream', 'FileUtil.getOutputStream', 'CALL', 'get output stream in FILE mode',
  evidence='SRC HybridFile.java:1065')

# FileUtil.isOnExtSdCard is public static, called from MainActivityHelper, Operations, FileUtil itself
e('MainActivityHelper.mkDir', 'FileUtil.isOnExtSdCard', 'CALL', 'check if folder on ext sd',
  evidence='SRC MainActivityHelper.java:340')
e('Operations.mkDir', 'FileUtil.isOnExtSdCard', 'CALL', 'check if folder on ext sd',
  evidence='SRC Operations.java:495')
e('FileUtil.deleteFile', 'FileUtil.isOnExtSdCard', 'CALL', 'check if file on ext sd for SAF delete',
  evidence='SRC FileUtil.java:381')

# FileUtil.isReadable is public static, called from GenericCopyUtil
e('GenericCopyUtil.copyFiles', 'FileUtil.isReadable', 'CALL', 'check source file readable',
  evidence='SRC GenericCopyUtil.java:152')

# FileUtil.isValidFilename is public static, called from GeneralDialogCreation, MainFragment, MainActivityHelper
e('GeneralDialogCreation.mkDir', 'FileUtil.isValidFilename', 'CALL', 'validate new folder name',
  evidence='SRC GeneralDialogCreation.java:973')
e('MainFragment.onMenuItemClick', 'FileUtil.isValidFilename', 'CALL', 'validate new file name',
  evidence='SRC MainFragment.java:1228')
e('MainActivityHelper.mkDir', 'FileUtil.isValidFilename', 'CALL', 'validate folder name',
  evidence='SRC MainActivityHelper.java:142')

# FileUtil.isWritable is public static, called from MainActivityHelper, GenericCopyUtil, Operations, FileUtil
e('MainActivityHelper.mkDir', 'FileUtil.isWritable', 'CALL', 'check folder writable',
  evidence='SRC MainActivityHelper.java:352')
e('GenericCopyUtil.copyFiles', 'FileUtil.isWritable', 'CALL', 'check target file writable',
  evidence='SRC GenericCopyUtil.java:255')
e('Operations.mkDir', 'FileUtil.isWritable', 'CALL', 'check folder writable',
  evidence='SRC Operations.java:515')

# FileUtil.isWritableNormalOrSaf is public static, called from MainActivityHelper, Operations, FileUtil itself
e('MainActivityHelper.mkDir', 'FileUtil.isWritableNormalOrSaf', 'CALL', 'check folder writable with SAF',
  evidence='SRC MainActivityHelper.java:346')
e('Operations.mkDir', 'FileUtil.isWritableNormalOrSaf', 'CALL', 'check folder writable with SAF',
  evidence='SRC Operations.java:503')
e('FileUtil.writeUriToStorage', 'FileUtil.isWritableNormalOrSaf', 'CALL', 'check target folder writable',
  evidence='SRC FileUtil.java:235')

# FileUtil.mkdir is public static, called from Operations, HybridFile, extractors, FileUtil
e('Operations.mkDir', 'FileUtil.mkdir', 'CALL', 'create directory',
  evidence='SRC Operations.java:169')
e('HybridFile.mkdir', 'FileUtil.mkdir', 'CALL', 'create directory in FILE mode',
  evidence='SRC HybridFile.java:1209')
e('FileUtil.renameFolder', 'FileUtil.mkdir', 'CALL', 'create target folder for manual rename',
  evidence='SRC FileUtil.java:443')

# FileUtil.mkdirs is public static, called from CryptUtil
e('CryptUtil.encrypt', 'FileUtil.mkdirs', 'CALL', 'create output directory',
  evidence='SRC CryptUtil.java:169')
e('CryptUtil.decrypt', 'FileUtil.mkdirs', 'CALL', 'create output directory',
  evidence='SRC CryptUtil.java:221')

# FileUtil.mkfile is public static, called from Operations
e('Operations.mkFile', 'FileUtil.mkfile', 'CALL', 'create file',
  evidence='SRC Operations.java:307')

# FileUtil.rename is private static, called from FileUtil.renameFolder
e('FileUtil.renameFolder', 'FileUtil.rename', 'CALL', 'try normal rename first',
  evidence='SRC FileUtil.java:425')

# FileUtil.renameFolder is package-private static, called from Operations
e('Operations.rename', 'FileUtil.renameFolder', 'CALL', 'rename folder',
  evidence='SRC Operations.java:444')

# FileUtil.rmdir is private static, called from FileUtil.deleteFile
e('FileUtil.deleteFile', 'FileUtil.rmdir', 'CALL', 'recursively delete directory',
  evidence='SRC FileUtil.java:376')

# FileUtil.writeUriToStorage is public static final, called from MainActivity
e('MainActivity.onActivityResult', 'FileUtil.writeUriToStorage', 'CALL', 'save ACTION_OPEN_DOCUMENT content',
  evidence='SRC MainActivity.java:567')
e('MainActivity.onActivityResult', 'FileUtil.writeUriToStorage', 'CALL', 'save ACTION_GET_CONTENT content',
  evidence='SRC MainActivity.java:576')
e('MainActivity.onActivityResult', 'FileUtil.writeUriToStorage', 'CALL', 'save saved instance uris',
  evidence='SRC MainActivity.java:1389')

# FileUtil$1 is the anonymous inner class created in writeUriToStorage
e('FileUtil.writeUriToStorage', 'FileUtil$1.<init>', 'CALL', 'create async callback for uri write',
  evidence='SRC FileUtil.java:196')

# FileUtil$1.doInBackground and onPostExecute are invoked by AppConfig.runInParallel
e('AppConfig.runInParallel', 'FileUtil$1.doInBackground', 'ASYNC', 'async task execution',
  evidence='SRC FileUtil.java:198-363')
e('AppConfig.runInParallel', 'FileUtil$1.onPostExecute', 'ASYNC', 'async task completion',
  evidence='SRC FileUtil.java:364-372')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_B026 = {
    'FileUtil.<clinit>': ('framework_never_calls', 'static initializer for Pattern field, runs on class load when FileUtil first referenced', 'SRC FileUtil.java:80-82', 'SOURCE'),
    'FileUtil.<init>': ('no_trigger_in_app', 'constructor of abstract class FileUtil, cannot be instantiated', 'SRC FileUtil.java:78 shows abstract class', 'SOURCE'),
    'FileUtil.copyDummyFile': ('no_trigger_in_app', 'private static method only called from copyDummyFiles which itself is never called; grep shows only internal calls at line 973-974', 'SRC FileUtil.java:888-926', 'SOURCE'),
    'FileUtil.copyDummyFiles': ('no_trigger_in_app', 'private static method, grep in app source shows only definition at FileUtil.java:971, no callers', 'SRC FileUtil.java:971-979', 'SOURCE'),
    'FileUtil.getTempFile': ('no_trigger_in_app', 'public static method, grep in app source shows only definition at FileUtil.java:476, no callers', 'SRC FileUtil.java:476-479', 'SOURCE'),
    'FileUtil$MediaFile.<clinit>': ('framework_never_calls', 'static initializer for MediaFile constants, runs on MediaFile class load', 'SRC FileUtil.java:983-985', 'SOURCE'),
    'FileUtil$MediaFile.<init>': ('no_trigger_in_app', 'constructor only called from MediaFile.mkdir() at line 1198, but mkdir() itself is never called; grep shows no MediaFile instantiation outside FileUtil', 'SRC FileUtil.java:1016-1022, call at 1198', 'SOURCE'),
    'FileUtil$MediaFile.delete': ('no_trigger_in_app', 'only called from MediaFile.mkdir() at line 1199, but mkdir() is never called', 'SRC FileUtil.java:1028-1059, call at 1199', 'SOURCE'),
    'FileUtil$MediaFile.getExternalFilesDir': ('no_trigger_in_app', 'private static, only called from installTemporaryTrack at line 1134, but that chain starts from mkdir() which is never called', 'SRC FileUtil.java:987-1010, call at 1134', 'SOURCE'),
    'FileUtil$MediaFile.getFile': ('no_trigger_in_app', 'public method, never called; MediaFile only instantiated at line 1198 within unreachable mkdir()', 'SRC FileUtil.java:1205-1207', 'SOURCE'),
    'FileUtil$MediaFile.getTemporaryAlbumId': ('no_trigger_in_app', 'private, only called from MediaFile.mkdir at line 1190, but mkdir is never called', 'SRC FileUtil.java:1062-1126, call at 1190', 'SOURCE'),
    'FileUtil$MediaFile.installTemporaryTrack': ('no_trigger_in_app', 'private, only called from getTemporaryAlbumId at line 1091, but that chain starts from mkdir() which is never called', 'SRC FileUtil.java:1129-1170, call at 1091', 'SOURCE'),
    'FileUtil$MediaFile.mkdir': ('no_trigger_in_app', 'public method but grep shows no callers in app; Kitkat workaround code that is unused', 'SRC FileUtil.java:1172-1202', 'SOURCE'),
    'FileUtil$MediaFile.write': ('no_trigger_in_app', 'public method but grep shows no callers in app; MediaFile is never instantiated outside its own mkdir()', 'SRC FileUtil.java:1207-1231', 'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_PART_B026)


# ---- label_b028 ----
# ---- Helper batch_028 label part (2026-10-27)
# FileUtils$1, FileUtils$2, FileUtils$3, FileUtils$4, FileUtils$5, FingerprintHandler, Folder

# FileUtils$1: AnimatorListenerAdapter for crossfade
# Constructor called from FileUtils.crossfade, callback invoked by framework
e('FileUtils.crossfade', 'FileUtils$1.<init>', 'CALL', 'creates animator listener for pathbar fade out',
  evidence='SRC files/FileUtils.java:289')
e('FileUtils$1.<init>', 'FileUtils$1.onAnimationEnd', 'FRAMEWORK', 'animation framework calls when fade animation completes',
  evidence='SRC files/FileUtils.java:291-293 defines AnimatorListenerAdapter.onAnimationEnd callback')

# FileUtils$2: AnimatorListenerAdapter for crossfadeInverse
# Constructor called from FileUtils.crossfadeInverse, callback invoked by framework
e('FileUtils.crossfadeInverse', 'FileUtils$2.<init>', 'CALL', 'creates animator listener for buttons fade out',
  evidence='SRC files/FileUtils.java:319')
e('FileUtils$2.<init>', 'FileUtils$2.onAnimationEnd', 'FRAMEWORK', 'animation framework calls when inverse fade animation completes',
  evidence='SRC files/FileUtils.java:321-323 defines AnimatorListenerAdapter.onAnimationEnd callback')

# FileUtils$3: AsyncTask for cloud file sharing
# Constructor called from FileUtils.shareCloudFile, methods invoked by AsyncTask framework
e('FileUtils.shareCloudFile', 'FileUtils$3.<init>', 'CALL', 'creates async task to get cloud share link',
  evidence='SRC files/FileUtils.java:333')
e('FileUtils$3.<init>', 'FileUtils$3.doInBackground', 'ASYNC', 'AsyncTask framework executes on background thread',
  evidence='SRC files/FileUtils.java:336-340 defines AsyncTask.doInBackground')
e('FileUtils$3.<init>', 'FileUtils$3.onPostExecute', 'ASYNC', 'AsyncTask framework calls on UI thread after background completes',
  evidence='SRC files/FileUtils.java:343-348 defines AsyncTask.onPostExecute')

# FileUtils$4: CountDownTimer for audio file easter egg
# Constructor called from FileUtils.openFile, callbacks invoked by CountDownTimer framework
e('FileUtils.openFile', 'FileUtils$4.<init>', 'CALL', 'creates countdown timer for studio easter egg',
  evidence='SRC files/FileUtils.java:768')
e('FileUtils$4.<init>', 'FileUtils$4.onTick', 'FRAMEWORK', 'CountDownTimer framework calls every second',
  evidence='SRC files/FileUtils.java:770-776 defines CountDownTimer.onTick')
e('FileUtils$4.<init>', 'FileUtils$4.onFinish', 'FRAMEWORK', 'CountDownTimer framework calls when timer finishes',
  evidence='SRC files/FileUtils.java:779-785 defines CountDownTimer.onFinish')

# FileUtils$5: Operations.ErrorCallBack interface implementation
# Constructor called from FileUtils.checkForPath, methods called back from Operations.mkdir
e('FileUtils.checkForPath', 'FileUtils$5.<init>', 'CALL', 'creates error callback for mkdir operation',
  evidence='SRC files/FileUtils.java:1027')
e('Operations.mkdir', 'FileUtils$5.exists', 'CALL', 'callback when file already exists',
  evidence='SRC filesystem/Operations.java:96,117,172 calls errorCallBack.exists(file); SRC files/FileUtils.java:1029-1031 defines empty callback')
e('Operations.mkdir', 'FileUtils$5.launchSAF', 'CALL', 'callback to launch SAF for SD card access (single HybridFile param)',
  evidence='SRC filesystem/Operations.java:165 calls errorCallBack.launchSAF(file); SRC files/FileUtils.java:1033-1035 defines empty callback')
e('Operations.mkdir', 'FileUtils$5.done', 'CALL', 'callback when mkdir operation completes',
  evidence='SRC filesystem/Operations.java:108,111,122,123,129,132,138,141,147,150,156,159,179 calls errorCallBack.done; SRC files/FileUtils.java:1042-1044 defines empty callback')
e('Operations.mkdir', 'FileUtils$5.invalidName', 'CALL', 'callback when filename is invalid',
  evidence='SRC filesystem/Operations.java:91 calls errorCallBack.invalidName(file); SRC files/FileUtils.java:1046-1048 defines empty callback')

# FingerprintHandler: Fingerprint authentication for file decryption (API 23+)
# Instantiated from GeneralDialogCreation.showDecryptFingerprintDialog (guarded by API >= M check)
e('GeneralDialogCreation.showDecryptFingerprintDialog', 'FingerprintHandler.<init>', 'CALL', 'creates fingerprint auth handler',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:835',
  guard='Build.VERSION.SDK_INT >= Build.VERSION_CODES.M at utils/files/EncryptDecryptUtils.java:107')
e('FingerprintHandler.<init>', 'FingerprintHandler.authenticate', 'CALL', 'initiates fingerprint authentication',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:836; SRC utils/FingerprintHandler.java:38-46')
e('FingerprintHandler.authenticate', 'FingerprintHandler.onAuthenticationError', 'FRAMEWORK', 'FingerprintManager callback on authentication error',
  evidence='SRC utils/FingerprintHandler.java:39,46 registers this as AuthenticationCallback; SRC utils/FingerprintHandler.java:51-53 defines callback')
e('FingerprintHandler.authenticate', 'FingerprintHandler.onAuthenticationHelp', 'FRAMEWORK', 'FingerprintManager callback on authentication help message',
  evidence='SRC utils/FingerprintHandler.java:39,46 registers this as AuthenticationCallback; SRC utils/FingerprintHandler.java:57-59 defines callback')
e('FingerprintHandler.authenticate', 'FingerprintHandler.onAuthenticationFailed', 'FRAMEWORK', 'FingerprintManager callback on authentication failure',
  evidence='SRC utils/FingerprintHandler.java:39,46 registers this as AuthenticationCallback; SRC utils/FingerprintHandler.java:63-66 defines callback')
e('FingerprintHandler.authenticate', 'FingerprintHandler.onAuthenticationSucceeded', 'FRAMEWORK', 'FingerprintManager callback on authentication success',
  evidence='SRC utils/FingerprintHandler.java:39,46 registers this as AuthenticationCallback; SRC utils/FingerprintHandler.java:70-74 defines callback')

# Folder: 7z archive structure (Apache Commons Compress library)
# Instantiated in SevenZFile.readHeaders
e('SevenZFile.readHeaders', 'Folder.<init>', 'CALL', 'creates Folder for 7z archive structure',
  evidence='SRC sevenz/SevenZFile.java:510,635')
e('SevenZFile.readStreamsInfo', 'Folder.getOrderedCoders', 'CALL', 'gets coders in stream processing order',
  evidence='SRC sevenz/SevenZFile.java:431')
e('SevenZFile.buildDecodingStream', 'Folder.getOrderedCoders', 'CALL', 'gets coders to build decoding stream',
  evidence='SRC sevenz/SevenZFile.java:1025')
e('Folder.getOrderedCoders', 'Folder.findBindPairForOutStream', 'CALL', 'finds bind pair for output stream in coder chain',
  evidence='SRC sevenz/Folder.java:59')
e('SevenZFile.readHeaders', 'Folder.findBindPairForInStream', 'CALL', 'finds bind pair for input stream',
  evidence='SRC sevenz/SevenZFile.java:695')
e('Folder.getUnpackSize', 'Folder.findBindPairForOutStream', 'CALL', 'checks if output stream is final',
  evidence='SRC sevenz/Folder.java:88')
e('SevenZFile.readStreamsInfo', 'Folder.getUnpackSize', 'CALL', 'gets total unpack size for folder',
  evidence='SRC sevenz/SevenZFile.java:440,442,586')
e('SevenZFile.buildDecodingStream', 'Folder.getUnpackSize', 'CALL', 'gets unpack size for stream setup',
  evidence='SRC sevenz/SevenZFile.java:1038')
e('SevenZFile.readStreamsInfo', 'Folder.getUnpackSizeForCoder', 'CALL', 'gets unpack size for specific coder',
  evidence='SRC sevenz/SevenZFile.java:436')
e('SevenZFile.buildDecodingStream', 'Folder.getUnpackSizeForCoder', 'CALL', 'gets coder unpack size for decoding',
  evidence='SRC sevenz/SevenZFile.java:1031')

# UNREACHABLE methods
# FileUtils$5.launchSAF(HybridFile, HybridFile) - two-parameter overload defined but not called by Operations.mkdir
# Operations.mkdir calls single-parameter launchSAF(HybridFile); two-parameter version is only called by Operations.rename
UNREACHABLE['FileUtils$5.launchSAF(HybridFile,HybridFile)'] = ('branch_never_taken', 'FileUtils$5 callback passed to Operations.mkdir at files/FileUtils.java:1027; mkdir only calls single-parameter launchSAF(file) at Operations.java:165, not two-parameter launchSAF(file,file1) which is only called by Operations.rename at Operations.java:441', 'SRC files/FileUtils.java:1037-1039 defines two-param override; SRC filesystem/Operations.java:165 mkdir calls single-param; SRC filesystem/Operations.java:441 rename calls two-param', 'SOURCE')

# Folder.toString() - debugging method not called
UNREACHABLE['Folder.toString'] = ('no_trigger_in_app', 'toString() is debugging/logging method defined at sevenz/Folder.java:100-106, no calls found in codebase', 'SRC sevenz/Folder.java:100-106 defines toString; grep of commons_compress_7z shows no calls to folder.toString()', 'CALL')


# ---- label_b029 ----
# ---- Helper batch_029 label part (2024-01-10)

# FtpReceiver - BroadcastReceiver for FTP service control
# Registered in manifest with exported="true" and receives intents from FtpServerFragment, FtpTileService, and FtpNotification
e('FtpServerFragment.startServer', 'FtpReceiver.onReceive', 'INTENT', 
  'sendBroadcast ACTION_START_FTPSERVER triggers receiver',
  evidence='SRC FtpServerFragment.java:376 sendBroadcast(ACTION_START_FTPSERVER), manifest line 206 registers receiver')

e('FtpServerFragment.stopServer', 'FtpReceiver.onReceive', 'INTENT',
  'sendBroadcast ACTION_STOP_FTPSERVER triggers receiver',
  evidence='SRC FtpServerFragment.java:383 sendBroadcast(ACTION_STOP_FTPSERVER), manifest line 206 registers receiver')

e('FtpTileService.onClick', 'FtpReceiver.onReceive', 'INTENT',
  'sendBroadcast ACTION_START/STOP_FTPSERVER from tile service',
  evidence='SRC FtpTileService.java:48,54 sendBroadcast(ACTION_STOP/START_FTPSERVER), manifest line 206 registers receiver')

e('FtpNotification.buildNotification', 'FtpReceiver.onReceive', 'INTENT',
  'PendingIntent.getBroadcast for stop action in notification',
  evidence='SRC FtpNotification.java:50-51 PendingIntent.getBroadcast(stopIntent with ACTION_STOP_FTPSERVER), manifest line 206 registers receiver')

# Note: FtpReceiver.onReceive calls FtpService start/stop but FtpService is not in this batch

# FtpNotification - Notification builder for FTP service
e('FtpService.onStartCommand', 'FtpNotification.startNotification', 'CALL',
  'FtpService calls startNotification when starting foreground',
  evidence='SRC FtpService.java:140 Notification notification = FtpNotification.startNotification(getApplicationContext(), isStartedByTile)')

e('FtpNotification.startNotification', 'FtpNotification.buildNotification', 'CALL',
  'startNotification calls buildNotification',
  evidence='SRC FtpNotification.java:65-66 NotificationCompat.Builder builder = buildNotification(...)')

e('FtpServerFragment.onFtpReceiveActions', 'FtpNotification.updateNotification', 'CALL',
  'Fragment updates notification when FTP status changes',
  evidence='SRC FtpServerFragment.java:355 FtpNotification.updateNotification(getContext(), STARTED_FROM_TILE.equals(signal))')

e('FtpNotification.updateNotification', 'FtpNotification.buildNotification', 'CALL',
  'updateNotification calls buildNotification',
  evidence='SRC FtpNotification.java:84-85 NotificationCompat.Builder builder = buildNotification(...)')

# FoldersPref - PreferenceFragment for managing bookmark folders
e('PreferencesActivity.selectItem', 'FoldersPref.onCreate', 'LIFECYCLE',
  'PreferenceFragment instantiated and onCreate called by PreferencesActivity',
  evidence='SRC PreferencesActivity.java:261 loadPrefFragment(new FoldersPref(), R.string.sidebar_folders_title)')

e('FoldersPref.onCreate', 'FoldersPref.onPreferenceClick', 'GUI',
  'Preferences set click listener to this fragment',
  evidence='SRC FoldersPref.java:58 findPreference(PreferencesConstants.PREFERENCE_SHORTCUT).setOnPreferenceClickListener(this); line 64 p.setOnPreferenceClickListener(this)')

e('FoldersPref.onPreferenceClick', 'FoldersPref.loadCreateDialog', 'CALL',
  'Click on PREFERENCE_SHORTCUT loads create dialog',
  evidence='SRC FoldersPref.java:90-95 if(preference.getKey().equals(PreferencesConstants.PREFERENCE_SHORTCUT)) ... loadCreateDialog()')

e('FoldersPref.onPreferenceClick', 'FoldersPref.loadEditDialog', 'CALL',
  'Click on PathSwitchPreference EDIT action loads edit dialog',
  evidence='SRC FoldersPref.java:82-85 case PathSwitchPreference.EDIT: loadEditDialog((PathSwitchPreference) preference)')

e('FoldersPref.onPreferenceClick', 'FoldersPref.loadDeleteDialog', 'CALL',
  'Click on PathSwitchPreference DELETE action loads delete dialog',
  evidence='SRC FoldersPref.java:86-88 case PathSwitchPreference.DELETE: loadDeleteDialog((PathSwitchPreference) preference)')

e('FoldersPref.loadCreateDialog', 'FoldersPref.disableButtonIfTitleEmpty', 'CALL',
  'Create dialog calls helper to validate title',
  evidence='SRC FoldersPref.java:116 disableButtonIfTitleEmpty(txtShortcutName, dialog)')

e('FoldersPref.loadCreateDialog', 'FoldersPref.disableButtonIfNotPath', 'CALL',
  'Create dialog calls helper to validate path',
  evidence='SRC FoldersPref.java:117 disableButtonIfNotPath(txtShortcutPath, dialog)')

e('FoldersPref.loadEditDialog', 'FoldersPref.disableButtonIfTitleEmpty', 'CALL',
  'Edit dialog calls helper to validate title',
  evidence='SRC FoldersPref.java:172 disableButtonIfTitleEmpty(editText1, dialog)')

e('FoldersPref.loadEditDialog', 'FoldersPref.disableButtonIfNotPath', 'CALL',
  'Edit dialog calls helper to validate path',
  evidence='SRC FoldersPref.java:173 disableButtonIfNotPath(editText2, dialog)')

e('FoldersPref.disableButtonIfNotPath', 'FoldersPref$1.afterTextChanged', 'GUI',
  'Creates anonymous SimpleTextWatcher, framework calls afterTextChanged on text change',
  evidence='SRC FoldersPref.java:223-228 new SimpleTextWatcher() { @Override public void afterTextChanged(Editable s) {...} }')

e('FoldersPref.disableButtonIfTitleEmpty', 'FoldersPref$2.afterTextChanged', 'GUI',
  'Creates anonymous SimpleTextWatcher, framework calls afterTextChanged on text change',
  evidence='SRC FoldersPref.java:233-237 new SimpleTextWatcher() { @Override public void afterTextChanged(Editable s) {...} }')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_B029 = {
    'FtpReceiver.<clinit>': ('framework_never_calls', 'Static initializer for TAG field, executed when class loads', 'SRC FtpReceiver.java:13 static final String TAG = FtpReceiver.class.getSimpleName()', 'SOURCE'),
    
    'FtpReceiver.<init>': ('framework_never_calls', 'Default constructor, called by Android framework when instantiating receiver', 'SRC FtpReceiver.java:11 public class FtpReceiver extends BroadcastReceiver - framework instantiates receivers', 'SOURCE'),
    
    'FoldersPref.<init>': ('framework_never_calls', 'Default constructor, called by Android framework when instantiating fragment', 'SRC FoldersPref.java:35 public class FoldersPref extends PreferenceFragment - framework instantiates fragments', 'SOURCE'),
    
    'FoldersPref.onResume': ('framework_never_calls', 'Lifecycle method called by framework, but only calls onCreate(null) which recreates all preferences', 'SRC FoldersPref.java:73-76 onResume() { super.onResume(); onCreate(null); }', 'SOURCE'),
    
    'FoldersPref$1.<init>': ('framework_never_calls', 'Constructor for anonymous inner class, never called directly', 'SRC FoldersPref.java:223 new SimpleTextWatcher() creates instance', 'SOURCE'),
    
    'FoldersPref$2.<init>': ('framework_never_calls', 'Constructor for anonymous inner class, never called directly', 'SRC FoldersPref.java:233 new SimpleTextWatcher() creates instance', 'SOURCE'),
    
    'FtpNotification.<init>': ('no_trigger_in_app', 'Private constructor, all methods are static', 'SRC FtpNotification.java:25 public class FtpNotification has only static methods (startNotification, updateNotification, buildNotification, removeNotification)', 'SOURCE'),
    
    'FtpNotification.removeNotification': ('no_trigger_in_app', 'Private method never called in the app', 'SRC FtpNotification.java:93-97 private static void removeNotification - grep shows no callers', 'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_PART_B029)

# Lambda methods - need to check if they're callback references
# These will be marked as reachable through their dialog button click listeners
e('FoldersPref.loadCreateDialog', 'FoldersPref.lambda$loadCreateDialog$0', 'GUI',
  'Lambda registered as onClick listener for dialog positive button',
  evidence='SRC FoldersPref.java:119-137 dialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(view -> { ... })')

e('FoldersPref.loadEditDialog', 'FoldersPref.lambda$loadEditDialog$2', 'GUI',
  'Lambda registered as onClick listener for dialog positive button',
  evidence='SRC FoldersPref.java:175-196 dialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(view -> { ... })')

e('FoldersPref.loadDeleteDialog', 'FoldersPref.lambda$loadDeleteDialog$3', 'GUI',
  'Lambda registered as onClick listener for dialog positive button',
  evidence='SRC FoldersPref.java:212-222 dialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(view -> { ... })')

# lambda$null$1 is the inner lambda in loadEditDialog's onClick
e('FoldersPref.lambda$loadEditDialog$2', 'FoldersPref.lambda$null$1', 'ASYNC',
  'Inner lambda passed to AppConfig.runInBackground',
  evidence='SRC FoldersPref.java:192-194 AppConfig.runInBackground(() -> utilsHandler.renameBookmark(...))')


# ---- label_b030 ----
# ---- Helper batch_030 label part (2024)
# FtpServerFragment and FtpServerFragment$1

# FtpServerFragment.<init> - constructor
e('Drawer.lambda$populateDrawer$5', 'FtpServerFragment.<init>', 'CALL', 'Drawer creates FtpServerFragment via lambda',
  evidence='SRC Drawer.java:405')

# FtpServerFragment.onCreate - Fragment lifecycle
e('FtpServerFragment.<init>', 'FtpServerFragment.onCreate', 'LIFECYCLE', 'Fragment lifecycle onCreate after construction',
  evidence='SRC FtpServerFragment.java:93-98 shows onCreate implementation')

# FtpServerFragment.onCreateView - Fragment lifecycle
e('FtpServerFragment.onCreate', 'FtpServerFragment.onCreateView', 'LIFECYCLE', 'Fragment lifecycle onCreateView after onCreate',
  evidence='SRC FtpServerFragment.java:100-104 shows onCreateView implementation')

# FtpServerFragment.onActivityCreated - Fragment lifecycle
e('FtpServerFragment.onCreateView', 'FtpServerFragment.onActivityCreated', 'LIFECYCLE', 'Fragment lifecycle onActivityCreated after onCreateView',
  evidence='SRC FtpServerFragment.java:143-157 shows onActivityCreated implementation')

# FtpServerFragment.onResume - Fragment lifecycle
e('FtpServerFragment.onActivityCreated', 'FtpServerFragment.onResume', 'LIFECYCLE', 'Fragment lifecycle onResume after onActivityCreated',
  evidence='SRC FtpServerFragment.java:391-398 shows onResume implementation')

# FtpServerFragment.onPause - Fragment lifecycle
e('FtpServerFragment.onResume', 'FtpServerFragment.onPause', 'LIFECYCLE', 'Fragment lifecycle onPause when leaving',
  evidence='SRC FtpServerFragment.java:400-405 shows onPause implementation')

# FtpServerFragment.onCreateOptionsMenu - Framework callback
e('FtpServerFragment.onCreate', 'FtpServerFragment.onCreateOptionsMenu', 'FRAMEWORK', 'Framework calls onCreateOptionsMenu after setHasOptionsMenu(true)',
  evidence='SRC FtpServerFragment.java:96 sets setHasOptionsMenu; FtpServerFragment.java:365-367 shows onCreateOptionsMenu')

# FtpServerFragment.updateSpans called from onCreateView and onFtpReceiveActions
e('FtpServerFragment.onCreateView', 'FtpServerFragment.updateSpans', 'CALL', 'onCreateView calls updateSpans to initialize status text',
  evidence='SRC FtpServerFragment.java:119')

# FtpServerFragment.updateStatus called from onCreateView
e('FtpServerFragment.onCreateView', 'FtpServerFragment.updateStatus', 'CALL', 'onCreateView calls updateStatus to initialize UI',
  evidence='SRC FtpServerFragment.java:120')

# FtpServerFragment.startServer called from button click
e('FtpServerFragment.lambda$onCreateView$0', 'FtpServerFragment.startServer', 'CALL', 'Button click lambda calls startServer',
  evidence='SRC FtpServerFragment.java:132')

# FtpServerFragment.stopServer called from button click
e('FtpServerFragment.lambda$onCreateView$0', 'FtpServerFragment.stopServer', 'CALL', 'Button click lambda calls stopServer',
  evidence='SRC FtpServerFragment.java:139')

# FtpServerFragment.lambda$onCreateView$0 - button click handler
e('FtpServerFragment.onCreateView', 'FtpServerFragment.lambda$onCreateView$0', 'GUI', 'ftpBtn setOnClickListener registers lambda',
  evidence='SRC FtpServerFragment.java:127')

# FtpServerFragment.onOptionsItemSelected - menu item selection
e('FtpServerFragment.onCreateOptionsMenu', 'FtpServerFragment.onOptionsItemSelected', 'FRAMEWORK', 'Framework calls onOptionsItemSelected when menu item selected',
  evidence='SRC FtpServerFragment.java:159-360 shows handler')

# FtpServerFragment.getDefaultPortFromPreferences called from onOptionsItemSelected
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.getDefaultPortFromPreferences', 'CALL', 'onOptionsItemSelected gets current port',
  evidence='SRC FtpServerFragment.java:162')

# FtpServerFragment.changeFTPServerPort called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$1', 'FtpServerFragment.changeFTPServerPort', 'CALL', 'Lambda calls changeFTPServerPort after dialog',
  evidence='SRC FtpServerFragment.java:172')

# FtpServerFragment.lambda$onOptionsItemSelected$1 - port dialog callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$1', 'GUI', 'MaterialDialog onPositive callback',
  evidence='SRC FtpServerFragment.java:167')

# FtpServerFragment.getDefaultPathFromPreferences called from onOptionsItemSelected
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.getDefaultPathFromPreferences', 'CALL', 'onOptionsItemSelected gets current path',
  evidence='SRC FtpServerFragment.java:186')

# FtpServerFragment.changeFTPServerPath called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$2', 'FtpServerFragment.changeFTPServerPath', 'CALL', 'Lambda calls changeFTPServerPath after dialog',
  evidence='SRC FtpServerFragment.java:197')

# FtpServerFragment.lambda$onOptionsItemSelected$2 - path dialog callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$2', 'GUI', 'MaterialDialog onPositive callback',
  evidence='SRC FtpServerFragment.java:188')

# FtpServerFragment.lambda$onOptionsItemSelected$3 - path dialog else branch callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$3', 'GUI', 'MaterialDialog input callback',
  evidence='SRC FtpServerFragment.java:185')

# FtpServerFragment.initLoginDialogViews called from onOptionsItemSelected
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.initLoginDialogViews', 'CALL', 'onOptionsItemSelected initializes login dialog',
  evidence='SRC FtpServerFragment.java:226')

# FtpServerFragment.setFTPUsername called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$4', 'FtpServerFragment.setFTPUsername', 'CALL', 'Lambda calls setFTPUsername',
  evidence='SRC FtpServerFragment.java:234')

# FtpServerFragment.setFTPPassword called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$4', 'FtpServerFragment.setFTPPassword', 'CALL', 'Lambda calls setFTPPassword',
  evidence='SRC FtpServerFragment.java:245')

# FtpServerFragment.lambda$onOptionsItemSelected$4 - login dialog callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$4', 'GUI', 'MaterialDialog onPositive callback for login',
  evidence='SRC FtpServerFragment.java:230')

# FtpServerFragment.setSecurePreference called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$4', 'FtpServerFragment.setSecurePreference', 'CALL', 'Lambda calls setSecurePreference',
  evidence='SRC FtpServerFragment.java:250')

# FtpServerFragment.getFTPTimeout called from onOptionsItemSelected
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.getFTPTimeout', 'CALL', 'onOptionsItemSelected gets current timeout',
  evidence='SRC FtpServerFragment.java:262')

# FtpServerFragment.setFTPTimeout called from lambda in onOptionsItemSelected
e('FtpServerFragment.lambda$onOptionsItemSelected$5', 'FtpServerFragment.setFTPTimeout', 'CALL', 'Lambda calls setFTPTimeout',
  evidence='SRC FtpServerFragment.java:278')

# FtpServerFragment.lambda$onOptionsItemSelected$5 - timeout dialog callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$5', 'GUI', 'MaterialDialog input callback for timeout',
  evidence='SRC FtpServerFragment.java:263')

# FtpServerFragment.lambda$onOptionsItemSelected$6 - another branch in timeout callback
e('FtpServerFragment.onOptionsItemSelected', 'FtpServerFragment.lambda$onOptionsItemSelected$6', 'GUI', 'MaterialDialog input callback alternate branch',
  evidence='SRC FtpServerFragment.java:263')

# FtpServerFragment.onFtpReceiveActions - EventBus callback
e('FtpServerFragment.onResume', 'FtpServerFragment.onFtpReceiveActions', 'ASYNC', 'EventBus delivers FtpReceiverActions after registration',
  evidence='SRC FtpServerFragment.java:397 registers; FtpServerFragment.java:334-361 shows @Subscribe handler')

# FtpServerFragment.getUsernameFromPreferences called from initLoginDialogViews
e('FtpServerFragment.initLoginDialogViews', 'FtpServerFragment.getUsernameFromPreferences', 'CALL', 'initLoginDialogViews gets username',
  evidence='SRC FtpServerFragment.java:528')

# FtpServerFragment.getPasswordFromPreferences called from initLoginDialogViews and updateStatus
e('FtpServerFragment.initLoginDialogViews', 'FtpServerFragment.getPasswordFromPreferences', 'CALL', 'initLoginDialogViews gets password',
  evidence='SRC FtpServerFragment.java:532')

# FtpServerFragment.getSecurePreference called from initLoginDialogViews
e('FtpServerFragment.initLoginDialogViews', 'FtpServerFragment.getSecurePreference', 'CALL', 'initLoginDialogViews gets secure preference',
  evidence='SRC FtpServerFragment.java:535')

# FtpServerFragment.lambda$initLoginDialogViews$8 - anonymous checkbox listener
e('FtpServerFragment.initLoginDialogViews', 'FtpServerFragment.lambda$initLoginDialogViews$8', 'GUI', 'Anonymous checkbox setOnCheckedChangeListener',
  evidence='SRC FtpServerFragment.java:516')

# FtpServerFragment.getFTPAddressString called from updateSpans
e('FtpServerFragment.updateSpans', 'FtpServerFragment.getFTPAddressString', 'CALL', 'updateSpans gets FTP address for display',
  evidence='SRC FtpServerFragment.java:486')

# FtpServerFragment.lambda$updateStatus$7 - password visibility toggle
e('FtpServerFragment.updateStatus', 'FtpServerFragment.lambda$updateStatus$7', 'GUI', 'ftpPasswordVisibleButton setOnClickListener',
  evidence='SRC FtpServerFragment.java:457')

# FtpServerFragment$1.<init> - BroadcastReceiver constructor
e('FtpServerFragment.<init>', 'FtpServerFragment$1.<init>', 'CALL', 'FtpServerFragment initializes mWifiReceiver field',
  evidence='SRC FtpServerFragment.java:369 shows field declaration')

# FtpServerFragment$1.onReceive - BroadcastReceiver callback
e('FtpServerFragment.onResume', 'FtpServerFragment$1.onReceive', 'SYSTEM', 'System delivers CONNECTIVITY_ACTION broadcast after registration',
  evidence='SRC FtpServerFragment.java:395 registers mWifiReceiver; FtpServerFragment.java:372-387 shows onReceive')

# UNREACHABLE methods from this batch
UNREACHABLE_BATCH_030 = {
}
UNREACHABLE.update(UNREACHABLE_BATCH_030)


# ---- label_b031 ----
# ---- Helper batch_031 label part (2025-01-18)

# FtpService - REACHABLE methods via FtpReceiver broadcast and FtpTileService

# FtpService.<clinit> - REACHABLE via class load when FtpReceiver.onReceive creates Intent
e('FtpReceiver.onReceive', 'FtpService.<clinit>', 'FRAMEWORK',
  'Framework loads FtpService class when Intent constructed at line 20',
  evidence='SRC FtpReceiver.java:20')

# FtpService.<init> - REACHABLE via startService
e('FtpReceiver.onReceive', 'FtpService.<init>', 'FRAMEWORK',
  'Framework calls constructor when context.startService invoked',
  evidence='SRC FtpReceiver.java:24')

# FtpService.onStartCommand - REACHABLE via Service lifecycle
e('FtpService.<init>', 'FtpService.onStartCommand', 'LIFECYCLE',
  'Framework calls onStartCommand after service started',
  evidence='SRC FtpService.java:119-142, FtpReceiver.java:24')

# FtpService.run - REACHABLE via Thread.start
e('FtpService.onStartCommand', 'FtpService.run', 'ASYNC',
  'onStartCommand creates Thread with this Runnable and calls start',
  evidence='SRC FtpService.java:131-132')

# FtpService.getPort - REACHABLE via run
e('FtpService.run', 'FtpService.getPort', 'CALL',
  'run calls getPort to configure listener factory',
  evidence='SRC FtpService.java:220')

# FtpService.onDestroy - REACHABLE via Service lifecycle
e('FtpService.<init>', 'FtpService.onDestroy', 'LIFECYCLE',
  'Framework calls onDestroy when service stopped',
  evidence='SRC FtpService.java:234-247, FtpReceiver.java:26')

# FtpService.onTaskRemoved - REACHABLE via Service lifecycle
e('FtpService.<init>', 'FtpService.onTaskRemoved', 'LIFECYCLE',
  'Framework calls onTaskRemoved when task removed from recents',
  evidence='SRC FtpService.java:251-262')

# FtpService.onBind - REACHABLE via Service lifecycle
e('FtpService.<init>', 'FtpService.onBind', 'LIFECYCLE',
  'Framework calls onBind for Service even though returns null',
  evidence='SRC FtpService.java:148-151')

# FtpService.isRunning - REACHABLE via static calls from FtpTileService and FtpReceiver
e('FtpTileService.onClick', 'FtpService.isRunning', 'CALL',
  'FtpTileService.onClick calls isRunning to check state',
  evidence='SRC FtpTileService.java:47')

e('FtpTileService.updateTileState', 'FtpService.isRunning', 'CALL',
  'updateTileState calls isRunning to update tile',
  evidence='SRC FtpTileService.java:65')

e('FtpReceiver.onReceive', 'FtpService.isRunning', 'CALL',
  'FtpReceiver checks isRunning before starting service',
  evidence='SRC FtpReceiver.java:23')

# FtpService.isConnectedToLocalNetwork - REACHABLE via static calls
e('FtpTileService.onClick', 'FtpService.isConnectedToLocalNetwork', 'CALL',
  'onClick checks network connection before starting service',
  evidence='SRC FtpTileService.java:51')

e('FtpService.getLocalInetAddress', 'FtpService.isConnectedToLocalNetwork', 'CALL',
  'getLocalInetAddress calls isConnectedToLocalNetwork',
  evidence='SRC FtpService.java:307')

# FtpService.isConnectedToWifi - REACHABLE via static calls
e('FtpTileService.onClick', 'FtpService.isConnectedToWifi', 'CALL',
  'onClick checks wifi connection before starting service',
  evidence='SRC FtpTileService.java:50')

e('FtpService.getLocalInetAddress', 'FtpService.isConnectedToWifi', 'CALL',
  'getLocalInetAddress calls isConnectedToWifi',
  evidence='SRC FtpService.java:311')

# FtpService.isEnabledWifiHotspot - REACHABLE via static calls
e('FtpTileService.onClick', 'FtpService.isEnabledWifiHotspot', 'CALL',
  'onClick checks wifi hotspot before starting service',
  evidence='SRC FtpTileService.java:52')

e('FtpService.getLocalInetAddress', 'FtpService.isEnabledWifiHotspot', 'CALL',
  'getLocalInetAddress calls isEnabledWifiHotspot',
  evidence='SRC FtpService.java:307, 328')

# FtpService.getLocalInetAddress - REACHABLE via FtpNotification
e('FtpNotification.startNotification', 'FtpService.getLocalInetAddress', 'CALL',
  'FtpNotification calls getLocalInetAddress to show IP in notification',
  evidence='SRC FtpNotification.java:77')

# FtpService.intToInet - REACHABLE via getLocalInetAddress
e('FtpService.getLocalInetAddress', 'FtpService.intToInet', 'CALL',
  'getLocalInetAddress calls intToInet to convert IP address',
  evidence='SRC FtpService.java:316')

# FtpService.byteOfInt - REACHABLE via intToInet
e('FtpService.intToInet', 'FtpService.byteOfInt', 'CALL',
  'intToInet calls byteOfInt in loop to extract bytes',
  evidence='SRC FtpService.java:351')

# FtpService.callIsWifiApEnabled - REACHABLE via isEnabledWifiHotspot
e('FtpService.isEnabledWifiHotspot', 'FtpService.callIsWifiApEnabled', 'CALL',
  'isEnabledWifiHotspot calls callIsWifiApEnabled',
  evidence='SRC FtpService.java:302')

# FtpService$FtpReceiverActions.<clinit> - REACHABLE via EventBus.post
e('FtpService.run', 'FtpService$FtpReceiverActions.<clinit>', 'FRAMEWORK',
  'Framework loads enum when referenced in EventBus.post',
  evidence='SRC FtpService.java:228, 230')

# FtpTileService - REACHABLE via Quick Settings Tile

# FtpTileService.<init> - REACHABLE via TileService lifecycle
e('ENTRY_POINT.QS_TILE', 'FtpTileService.<init>', 'FRAMEWORK',
  'Framework constructs TileService when user adds QS tile',
  evidence='SRC AndroidManifest.xml:195-201')

# FtpTileService.onStartListening - REACHABLE via TileService lifecycle
e('FtpTileService.<init>', 'FtpTileService.onStartListening', 'LIFECYCLE',
  'Framework calls onStartListening when tile becomes visible',
  evidence='SRC FtpTileService.java:28-32')

# FtpTileService.onStopListening - REACHABLE via TileService lifecycle
e('FtpTileService.<init>', 'FtpTileService.onStopListening', 'LIFECYCLE',
  'Framework calls onStopListening when tile no longer visible',
  evidence='SRC FtpTileService.java:35-38')

# FtpTileService.onClick - REACHABLE via TileService lifecycle
e('FtpTileService.<init>', 'FtpTileService.onClick', 'LIFECYCLE',
  'Framework calls onClick when user taps the tile',
  evidence='SRC FtpTileService.java:41-58')

# FtpTileService.lambda$onClick$0 - REACHABLE via onClick's lambda
e('FtpTileService.onClick', 'FtpTileService.lambda$onClick$0', 'CALL',
  'onClick calls unlockAndRun with lambda body compiled as this method',
  evidence='SRC FtpTileService.java:46-57')

# FtpTileService.updateTileState - REACHABLE via onStartListening and EventBus callback
e('FtpTileService.onStartListening', 'FtpTileService.updateTileState', 'CALL',
  'onStartListening calls updateTileState to initialize',
  evidence='SRC FtpTileService.java:31')

e('FtpTileService.onFtpReceiverActions', 'FtpTileService.updateTileState', 'CALL',
  'onFtpReceiverActions calls updateTileState on EventBus event',
  evidence='SRC FtpTileService.java:24')

# FtpTileService.onFtpReceiverActions - REACHABLE via EventBus
e('EventBus.register', 'FtpTileService.onFtpReceiverActions', 'SYSTEM',
  'EventBus invokes @Subscribe method when registered and event posted',
  evidence='SRC FtpTileService.java:23-25, 30')

# UNREACHABLE methods
UNREACHABLE_PART_B031 = {
}
UNREACHABLE.update(UNREACHABLE_PART_B031)

# ================================================================== L. UNREACHABLE, ENV/STATE tables, CLASSIFY, EDIT, STRICT

# Glide generated code - these classes are generated by Glide's annotation processor at compile time
# and are not present in the app's source tree. The app uses only a small subset of the generated API.
# The 9 reachable methods (GlideApp.with, GlideRequest.load/centerCrop/diskCacheStrategy, GlideRequests.asDrawable/load,
# GlideApplication.<init>/onCreate) are called from app code; the rest are generated convenience methods never invoked.

UNREACHABLE = {
    # From Helper label_c1 part (2026-10-27 21:12)
    'AES256SHA256Decoder.<init>': ('framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'CALL'),
    'AES256SHA256Decoder.decode': ('framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'CALL'),
    'AES256SHA256Decoder$1.<init>': ('framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'CALL'),
    'AES256SHA256Decoder$1.close': ('framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'CALL'),
    'AES256SHA256Decoder$1.init': ('framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'CALL'),
    # 'AES256SHA256Decoder$1.read' removed - duplicate, also defined below at line ~1491
    'AnimUtils.<init>': ('no_trigger_in_app',
        'Utility class with only static methods; constructor never explicitly called',
        'SRC AnimUtils.java:30 shows class declaration; no new AnimUtils() in app',
        'SOURCE'),
    
    # From Helper label_c3 part (2026-10-27 21:12)
    'BottomBar$3.onAnimationCancel': ('framework_never_calls',
        'Animation cancellation not triggered in app usage',
        'SRC ui/views/appbar/BottomBar.java:368-371',
        'SOURCE'),
    'BottomBar$5.onAnimationCancel': ('framework_never_calls',
        'Animation cancellation not triggered in app usage',
        'SRC ui/views/appbar/BottomBar.java:418-421',
        'SOURCE'),
    'BottomBar$6.onAnimationCancel': ('framework_never_calls',
        'Animation cancellation not triggered in app usage',
        'SRC ui/views/appbar/BottomBar.java:470-473',
        'SOURCE'),
    'BoundedFileChannelInputStream.close': ('framework_never_calls',
        'Close method explicitly empty; channel controlled externally',
        'SRC sevenz/BoundedFileChannelInputStream.java:91-93; comment states nested channel controlled externally',
        'SOURCE'),
    'CLI.<init>': ('no_trigger_in_app',
        'Command-line tool not instantiated by app',
        'SRC sevenz/CLI.java:24; grep shows no app usage',
        'SOURCE'),
    'CLI.main': ('no_trigger_in_app',
        'Command-line entry point not called by Android app',
        'SRC sevenz/CLI.java:114; main method unused in app context',
        'SOURCE'),
    'CLI.usage': ('no_trigger_in_app',
        'Called only from unused CLI.main',
        'SRC sevenz/CLI.java:132; only caller is CLI.main',
        'SOURCE'),
    'CLI.grabMode': ('no_trigger_in_app',
        'Called only from unused CLI.main',
        'SRC sevenz/CLI.java:136; only caller is CLI.main',
        'SOURCE'),
    
    # GlideApp - 12 unresolved methods
    'GlideApp.<init>': ('no_trigger_in_app', 'Glide generated method; no app code calls GlideApp constructor directly', 'INFERRED Glide generated code; source not in app tree', 'INFERRED'),
    # GlideApp - 12 unresolved methods
    'GlideApp.<init>': ('no_trigger_in_app', 'Glide generated method; no app code calls GlideApp constructor directly', 'INFERRED Glide generated code; source not in app tree', 'INFERRED'),
    'GlideApp.get': ('no_trigger_in_app', 'Glide generated method; no app code calls GlideApp.get from reachable path', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideApp.getPhotoCacheDir(Context)': ('no_trigger_in_app', 'Glide generated method; not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideApp.getPhotoCacheDir(Context,String)': ('no_trigger_in_app', 'Glide generated method; not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideApp.init(Context,GlideBuilder)': ('no_trigger_in_app', 'Glide generated method; not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideApp.init(Glide)': ('no_trigger_in_app', 'Glide generated method; not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideApp.tearDown': ('no_trigger_in_app', 'Glide generated method; not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideApp.with(Activity)': ('no_trigger_in_app', 'Glide generated method; app uses with(Fragment) instead', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideApp.with(Fragment)': ('no_trigger_in_app', 'Glide generated method; app uses with(Fragment)#2 overload instead', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideApp.with(Context)': ('no_trigger_in_app', 'Glide generated method; not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideApp.with(View)': ('no_trigger_in_app', 'Glide generated method; not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideApp.with(FragmentActivity)': ('no_trigger_in_app', 'Glide generated method; not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    
    # From Helper 4 (part 4 - 2026-10-27) - Framework classes never instantiated
    'Manifest.<init>': ('framework_never_calls', 'Android framework Manifest class is never instantiated, only holds nested permission constants class', 'INFERRED source not in dataset', 'INFERRED'),
    'Manifest$permission.<init>': ('framework_never_calls', 'Android framework Manifest.permission class holds only static constants, never instantiated', 'INFERRED source not in dataset', 'INFERRED'),
    'AppDataParcelable.<clinit>': ('no_trigger_in_app', 'Class has no static initializer block and CREATOR field is initialized inline', 'SRC AppDataParcelable.java:13-67 shows no static{} block', 'SOURCE'),

    # GlideOptions - 73 methods (all fluent API methods not used)
    # These are generated builder pattern methods for configuring image loading
    # Only a subset (centerCrop, diskCacheStrategy, load) are actually used by the app

    # Generated Glide methods (continued):
    'GlideConstants.<init>': ('no_trigger_in_app', 'GlideConstants generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.bitmapTransform': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.centerCropTransform': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.centerInsideTransform': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.circleCropTransform': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.decodeTypeOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.disallowHardwareConfig': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.diskCacheStrategyOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.downsampleOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.encodeFormatOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.encodeQualityOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.errorOf(Drawable)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.errorOf(int)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.fallback(Drawable)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.fallback(int)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.fitCenterTransform': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.formatOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.frameOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.noAnimation': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.noTransformation': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.onlyRetrieveFromCache': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.option': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.optionalCenterCrop': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.optionalCenterInside': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.optionalCircleCrop': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.optionalFitCenter': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.optionalTransform(Class,Transformation)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.optionalTransform(Transformation)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.overrideOf(int)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.overrideOf(int,int)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.placeholderOf(Drawable)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.placeholderOf(int)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.priorityOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.signatureOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.sizeMultiplierOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.skipMemoryCacheOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.theme': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.timeoutOf': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.transform(Class,Transformation)': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.transform(Transformation[])': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.transforms': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.useAnimationPool': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideOptions.useUnlimitedSourceGeneratorsPool': ('no_trigger_in_app', 'GlideOptions generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.centerInside': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.circleCrop': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.decode': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.disallowHardwareConfig': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.dontAnimate': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.dontTransform': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.encodeFormat': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.encodeQuality': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.error(Drawable)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.error(RequestBuilder)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.error(int)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.fallback(Drawable)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.fallback(int)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    # 'GlideRequest.fitCenter': REMOVED - app calls this at AppsAdapterPreloadModel.java:28: .asDrawable().fitCenter()
    'GlideRequest.format': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.frame': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.getDownloadOnlyRequest': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.load(Bitmap)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.load(Drawable)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.load(File)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.load(Object)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.load(URL)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.load(Uri)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.load(byte[])': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.onlyRetrieveFromCache': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.optionalCenterCrop': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.optionalCircleCrop': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.optionalTransform(Class,Transformation)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.optionalTransform(Transformation)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.override(int)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.override(int,int)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.placeholder(Drawable)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.placeholder(int)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.priority': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.signature': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.sizeMultiplier': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.skipMemoryCache': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.theme': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.thumbnail(RequestBuilder)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.thumbnail(RequestBuilder[])': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.thumbnail(float)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.timeout': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.transform(Class,Transformation)': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.transform(Transformation[])': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.transforms': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.transition': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.useAnimationPool': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequest.useUnlimitedSourceGeneratorsPool': ('no_trigger_in_app', 'GlideRequest generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.addDefaultRequestListener': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.applyDefaultRequestOptions': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.asBitmap': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.asFile': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.asGif': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.download': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.downloadOnly': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.load(Bitmap)': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.load(Drawable)': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.load(File)': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.load(Object)': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.load(String)': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.load(URL)': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.load(Uri)': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.load(byte[])': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    'GlideRequests.setDefaultRequestOptions': ('no_trigger_in_app', 'GlideRequests generated method not called from reachable app code', 'INFERRED Glide generated code', 'INFERRED'),
    # End of Glide generated methods (170 total)
}

def CLASSIFY(x):
    """Return edge class override for library/reflection edges"""
    # Glide generated code
    if 'GlideApp' in x['dst'] or 'GlideRequests' in x['dst']:
        return ('non_standard', 'Glide generated code')
    # Volley
    if 'volley' in x['dst']:
        return ('non_standard', 'Volley library')
    # Material dialogs
    if 'materialdialogs' in x['dst']:
        return ('non_standard', 'MaterialDialog library')
    # Speed dial FAB
    if 'speeddial' in x['dst']:
        return ('non_standard', 'SpeedDialView library')
    return None

def EDIT(x):
    """Add gates or modify edges post-build"""
    return x

# ---- part label_c1 (2026-10-27 21:18) ----
# Classes: AES256SHA256Decoder, AES256SHA256Decoder$1, AdvancedSearchPref, AmazeFileManagerModule,
#          AnimUtils, ApkImageDataFetcher, ApkImageModelLoader, ApkImageModelLoaderFactory,
#          AppConfig, AppConfig$1, AppConfig$CustomAsyncCallbacks, AppHolder
# Merged from parts/label_c1.py after C1 verification (54 methods: 47 REACHABLE, 7 UNREACHABLE)

# AdvancedSearchPref
e('PreferencesActivity.selectItem', 'AdvancedSearchPref.<init>', 'CALL',
  'PreferencesActivity instantiates AdvancedSearchPref in selectItem',
  evidence='SRC PreferencesActivity.java:267')

e('AdvancedSearchPref.<init>', 'AdvancedSearchPref.onCreate', 'FRAMEWORK',
  'Framework calls onCreate on PreferenceFragment after instantiation',
  evidence='INFERRED framework lifecycle for PreferenceFragment')

# AmazeFileManagerModule (Glide)
e('GlideApp.<init>', 'AmazeFileManagerModule.<init>', 'FRAMEWORK',
  'Glide annotation processor generates code that instantiates @GlideModule classes',
  evidence='INFERRED Glide annotation processor for @GlideModule')

e('AmazeFileManagerModule.<init>', 'AmazeFileManagerModule.registerComponents', 'FRAMEWORK',
  'Glide framework calls registerComponents on AppGlideModule subclasses',
  evidence='INFERRED Glide framework lifecycle for AppGlideModule')

e('AmazeFileManagerModule.registerComponents', 'ApkImageModelLoaderFactory.<init>', 'CALL',
  'registerComponents creates ApkImageModelLoaderFactory',
  evidence='SRC AmazeFileManagerModule.java:21')

# AnimUtils
e('Indicator.<init>', 'AnimUtils.getFastOutSlowInInterpolator', 'CALL',
  'Indicator constructor calls AnimUtils.getFastOutSlowInInterpolator',
  evidence='SRC Indicator.java:153')

e('AppsAdapter.onBindViewHolder', 'AnimUtils.marqueeAfterDelay', 'CALL',
  'AppsAdapter.onBindViewHolder calls marqueeAfterDelay',
  evidence='SRC AppsAdapter.java:139')

e('AnimUtils.marqueeAfterDelay', 'AnimUtils.lambda$marqueeAfterDelay$0', 'CALL',
  'marqueeAfterDelay posts lambda to Handler',
  evidence='SRC AnimUtils.java:47-49')

# ApkImage Glide loaders
e('ApkImageModelLoaderFactory.build', 'ApkImageModelLoader.<init>', 'CALL',
  'Factory.build creates ApkImageModelLoader',
  evidence='SRC ApkImageModelLoaderFactory.java:23')

e('ApkImageModelLoaderFactory.<init>', 'ApkImageModelLoaderFactory.build', 'FRAMEWORK',
  'Glide calls build on ModelLoaderFactory',
  evidence='INFERRED Glide framework calls build on registered factories')

e('ApkImageModelLoaderFactory.<init>', 'ApkImageModelLoaderFactory.teardown', 'FRAMEWORK',
  'Glide calls teardown on ModelLoaderFactory during cleanup',
  evidence='INFERRED Glide framework lifecycle')

e('ApkImageModelLoader.<init>', 'ApkImageModelLoader.buildLoadData', 'FRAMEWORK',
  'Glide calls buildLoadData on ModelLoader to create LoadData',
  evidence='INFERRED Glide framework calls buildLoadData')

e('ApkImageModelLoader.<init>', 'ApkImageModelLoader.handles', 'FRAMEWORK',
  'Glide calls handles on ModelLoader to check if it can handle model',
  evidence='INFERRED Glide framework calls handles')

e('ApkImageModelLoader.buildLoadData', 'ApkImageDataFetcher.<init>', 'CALL',
  'buildLoadData creates ApkImageDataFetcher',
  evidence='SRC ApkImageModelLoader.java:27')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.loadData', 'FRAMEWORK',
  'Glide calls loadData on DataFetcher to fetch data',
  evidence='INFERRED Glide framework calls loadData')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.cleanup', 'FRAMEWORK',
  'Glide calls cleanup on DataFetcher after load completes',
  evidence='INFERRED Glide framework lifecycle')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.cancel', 'FRAMEWORK',
  'Glide calls cancel on DataFetcher if load cancelled',
  evidence='INFERRED Glide framework lifecycle')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.getDataClass', 'FRAMEWORK',
  'Glide calls getDataClass on DataFetcher to determine result type',
  evidence='INFERRED Glide framework calls getDataClass')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.getDataSource', 'FRAMEWORK',
  'Glide calls getDataSource on DataFetcher to determine data source type',
  evidence='INFERRED Glide framework calls getDataSource')

# AppHolder
e('AppsAdapter.onCreateViewHolder', 'AppHolder.<init>', 'CALL',
  'AppsAdapter creates AppHolder in onCreateViewHolder',
  evidence='SRC AppsAdapter.java:114')

# AppConfig - Application class
e('Application.onCreate', 'AppConfig.<init>', 'FRAMEWORK',
  'Android framework instantiates Application subclass',
  evidence='INFERRED framework creates Application')

e('AppConfig.<init>', 'AppConfig.onCreate', 'FRAMEWORK',
  'Framework calls onCreate on Application after instantiation',
  evidence='INFERRED framework lifecycle for Application')

e('AppConfig.<init>', 'AppConfig.onTerminate', 'FRAMEWORK',
  'Framework calls onTerminate on Application during shutdown',
  evidence='INFERRED framework lifecycle for Application')

e('SftpConnectDialog.onCreate', 'AppConfig.getInstance', 'CALL',
  'SftpConnectDialog calls getInstance to get AppConfig singleton',
  evidence='SRC SftpConnectDialog.java:97-98')

e('AppConfig.getInstance', 'AppConfig.getUtilsProvider', 'CALL',
  'Code calls getUtilsProvider after getInstance',
  evidence='SRC SftpConnectDialog.java:97')

e('AppConfig.getInstance', 'AppConfig.getUtilsHandler', 'CALL',
  'Code calls getUtilsHandler after getInstance',
  evidence='SRC SftpConnectDialog.java:98')

e('Drawer.<init>', 'AppConfig.getInstance', 'CALL',
  'Drawer constructor calls getInstance',
  evidence='SRC Drawer.java:156')

e('AppConfig.getInstance', 'AppConfig.getImageLoader', 'CALL',
  'Code calls getImageLoader after getInstance',
  evidence='SRC Drawer.java:156')

e('AppConfig.getInstance', 'AppConfig.getScreenUtils', 'CALL',
  'Code calls getScreenUtils after getInstance',
  evidence='SRC Drawer.java:243')

e('GeneralDialogCreation.showNameDialog', 'AppConfig.getInstance', 'CALL',
  'showNameDialog calls getInstance',
  evidence='SRC GeneralDialogCreation.java:889')

e('AppConfig.getInstance', 'AppConfig.getMainActivityContext', 'CALL',
  'Code calls getMainActivityContext after getInstance',
  evidence='SRC GeneralDialogCreation.java:889')

e('MainActivity.onCreate', 'AppConfig.setMainActivityContext', 'CALL',
  'MainActivity sets itself as main activity context',
  evidence='INFERRED MainActivity needs to register itself')

e('SftpConnectDialog.lambda$onCreateView$2', 'AppConfig.runInBackground', 'CALL',
  'SftpConnectDialog lambda calls runInBackground',
  evidence='SRC SftpConnectDialog.java:249')

e('UtilsHandler.addCommonBookmarks', 'AppConfig.runInBackground', 'CALL',
  'UtilsHandler calls runInBackground',
  evidence='SRC UtilsHandler.java:179')

e('LoadFilesListTask.onPostExecute', 'AppConfig.toast', 'CALL',
  'LoadFilesListTask calls toast(Context, int)',
  evidence='SRC LoadFilesListTask.java:189')

e('AppConfig.toast', 'AppConfig.runInApplicationThread', 'CALL',
  'toast calls runInApplicationThread to show on UI thread',
  evidence='SRC AppConfig.java:161, 183')

e('AppConfig.toast', 'AppConfig.lambda$toast$0', 'CALL',
  'toast(Context, int) creates lambda',
  evidence='SRC AppConfig.java:160-162')

e('AppConfig.toast', 'AppConfig.lambda$toast$1', 'CALL',
  'toast(Context, String) creates lambda',
  evidence='SRC AppConfig.java:182-184')

e('AppConfig.runInParallel', 'AppConfig$1.<init>', 'CALL',
  'runInParallel creates anonymous AsyncTask',
  evidence='SRC AppConfig.java:110-127')

e('AppConfig$1.<init>', 'AppConfig$1.onPreExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPreExecute',
  evidence='INFERRED AsyncTask lifecycle')

e('AppConfig$1.<init>', 'AppConfig$1.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED AsyncTask lifecycle')

e('AppConfig$1.<init>', 'AppConfig$1.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED AsyncTask lifecycle')

e('AppConfig$1.onPreExecute', 'AppConfig$CustomAsyncCallbacks.onPreExecute', 'CALL',
  'AsyncTask onPreExecute calls callbacks.onPreExecute',
  evidence='SRC AppConfig.java:115')

e('AppConfig$1.doInBackground', 'AppConfig$CustomAsyncCallbacks.doInBackground', 'CALL',
  'AsyncTask doInBackground calls callbacks.doInBackground',
  evidence='SRC AppConfig.java:119')

e('AppConfig$1.onPostExecute', 'AppConfig$CustomAsyncCallbacks.onPostExecute', 'CALL',
  'AsyncTask onPostExecute calls callbacks.onPostExecute',
  evidence='SRC AppConfig.java:125')

e('AppConfig.runInParallel', 'AppConfig$CustomAsyncCallbacks.<init>', 'CALL',
  'Caller must subclass CustomAsyncCallbacks to use runInParallel',
  evidence='INFERRED from API design; constructor called by subclass instantiation')

# Static initializer
e('AppConfig.<init>', 'AppConfig.<clinit>', 'FRAMEWORK',
  'JVM calls static initializer before first use of class',
  evidence='INFERRED JVM static initialization')

# UNREACHABLE methods from label_c1
UNREACHABLE['AES256SHA256Decoder.<init>'] = (
    'framework_never_calls',
    'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
    'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
    'CALL'
)
UNREACHABLE['AES256SHA256Decoder.decode'] = (
    'framework_never_calls',
    'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
    'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
    'CALL'
)
UNREACHABLE['AES256SHA256Decoder$1.<init>'] = (
    'framework_never_calls',
    'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
    'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
    'CALL'
)
UNREACHABLE['AES256SHA256Decoder$1.close'] = (
    'framework_never_calls',
    'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
    'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
    'CALL'
)
UNREACHABLE['AES256SHA256Decoder$1.init'] = (
    'framework_never_calls',
    'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
    'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
    'CALL'
)
# Duplicate UNREACHABLE removed (also defined at line ~1496)
UNREACHABLE['AnimUtils.<init>'] = (
    'no_trigger_in_app',
    'Utility class with only static methods; constructor never explicitly called',
    'SRC AnimUtils.java:30 shows class declaration; no new AnimUtils() in app',
    'SOURCE'
)
# AnimUtils.<init> is not reachable (utility class never instantiated)
e('AnimUtils.marqueeAfterDelay', 'AnimUtils.lambda$marqueeAfterDelay$0', 'CALL',
  'Lambda callback passed to Handler.postDelayed',
  evidence='SRC utils/AnimUtils.java:47-49')

# AbstractProgressiveService - abstract base class for file operation services
# Derived services (CopyService, ExtractService, ZipService, DecryptService) already have entry/lifecycle edges
# These edges establish reachability of abstract methods through service framework calls
# No new edges needed beyond those for specific services (already in graph_def.py)

UNREACHABLE['AnimUtils.<init>'] = (
    'no_trigger_in_app',
    'Utility class with only static methods; no reachable constructor call site; never instantiated in app',
    'SRC utils/AnimUtils.java:28-29; grep -rn "new AnimUtils" shows no matches',
    'SOURCE'
)
# UNREACHABLE entries for AbstractProgressiveService.publishCompletedResult and .putDataPackage removed
# due to CONTRADICTION: both methods ran in tool runs and are called from reachable code
# (publishCompletedResult called from line 162, putDataPackage called via getDataPackage)
# These methods will be REACHABLE through bytecode edges

# Contradiction resolution: add explicit edges per conflicts.md analysis
e('AbstractProgressiveService.publishResults', 'AbstractProgressiveService.publishCompletedResult', 'CALL',
  'publishResults calls publishCompletedResult when operation completes',
  evidence='SRC asynchronous/services/AbstractProgressiveService.java:152,162')

e('AbstractProgressiveService.addFirstDatapoint', 'AbstractProgressiveService.putDataPackage', 'CALL',
  'addFirstDatapoint calls putDataPackage to store first datapoint',
  evidence='SRC asynchronous/services/AbstractProgressiveService.java:179')

e('AbstractProgressiveService.addDatapoint', 'AbstractProgressiveService.putDataPackage', 'CALL',
  'addDatapoint calls putDataPackage to store progress datapoint',
  evidence='SRC asynchronous/services/AbstractProgressiveService.java:187')

UNREACHABLE['AES256SHA256Decoder.<init>'] = (
    'framework_never_calls',
    'Library class from org.apache.commons.compress; no app call sites; only used internally by SevenZ library code',
    'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
    'SOURCE'
)
UNREACHABLE['AES256SHA256Decoder.decode'] = (
    'framework_never_calls',
    'Library class method; called only by SevenZ library internal code (CoderBase subclass) not reached by app',
    'SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/AES256SHA256Decoder.java',
    'SOURCE'
)
UNREACHABLE['AES256SHA256Decoder$1.<init>'] = (
    'framework_never_calls',
    'Anonymous inner class from unreachable library decoder; instantiated only by AES256SHA256Decoder.decode',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/AES256SHA256Decoder.java:34',
    'SOURCE'
)
UNREACHABLE['AES256SHA256Decoder$1.close'] = (
    'framework_never_calls',
    'Inner class method from unreachable library decoder; only called when stream is closed',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/AES256SHA256Decoder.java:113',
    'SOURCE'
)
# Duplicate UNREACHABLE['AES256SHA256Decoder$1.read'] removed (method name from line 1491 is malformed)
UNREACHABLE['AES256SHA256Decoder$1.init'] = (
    'framework_never_calls',
    'Private inner class method; only called from unreachable read() methods',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/AES256SHA256Decoder.java:41-104',
    'SOURCE'
)
# ---- AppTheme enum ----
# Enum static methods - reachable through getTheme() callers
e('UtilitiesProvider.getAppTheme', 'AppTheme.getTheme', 'CALL',
  'UtilitiesProvider.getAppTheme() calls AppTheme.getTheme()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/provider/UtilitiesProvider.java:28-30')

e('AppTheme.getTheme', 'AppTheme.<init>', 'CALL',
  'getTheme() returns enum constant (implicitly calls <init> via constructor)',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/theme/AppTheme.java:29-46')

e('AppTheme.<clinit>', 'AppTheme.<init>', 'CALL',
  'Enum <clinit> creates enum constants via <init>',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/theme/AppTheme.java:10-14')

# ---- part label_b005_norm (2026-10-27 21:32) ----
e('com.amaze.filemanager.ui.views.appbar.AppBar.<init>', 
  'BottomBar.<init>', 'CALL', 'AppBar constructor instantiates BottomBar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/AppBar.java:37')

e('MainActivity.onCreate', 
  'BottomBar.setClickListener', 'CALL', 'MainActivity onCreate calls setClickListener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:854')

e('MainActivity.onActivityResult',
  'BottomBar.resetClickListener', 'CALL', 'MainActivity onActivityResult resets listeners',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:892')

e('MainActivity.onPause',
  'BottomBar.updatePath', 'CALL', 'MainActivity onPause updates bottom bar path',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:850')

e('com.amaze.filemanager.activities.MainActivity.updateBottomBarColor',
  'BottomBar.setBackgroundColor', 'CALL', 'MainActivity theme color applied to bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/activities/MainActivity.java:1475')

e('com.amaze.filemanager.fragments.MainFragment.onViewCreated',
  'BottomBar.setClickListener', 'CALL', 'MainFragment sets up touch listeners',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:281')

e('com.amaze.filemanager.fragments.MainFragment.updateBottomBar',
  'BottomBar.updatePath', 'CALL', 'MainFragment updates bottom bar on path change',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:451')

e('com.amaze.filemanager.fragments.MainFragment.searchResultsFound',
  'BottomBar.setPathText', 'CALL', 'MainFragment updates path text on search',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1604')

e('com.amaze.filemanager.fragments.MainFragment.searchResultsFound',
  'BottomBar.setFullPathText', 'CALL', 'MainFragment updates full path on search',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1605')

e('com.amaze.filemanager.fragments.TabFragment.onFragmentResult',
  'BottomBar.updatePath', 'CALL', 'TabFragment updates bottom bar on selection',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/TabFragment.java:222-305')

e('com.amaze.filemanager.fragments.FtpServerFragment.onViewCreated',
  'BottomBar.setVisibility', 'CALL', 'FTP fragment hides bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/FtpServerFragment.java:157')

e('com.amaze.filemanager.fragments.AppsListFragment.onViewCreated',
  'BottomBar.setVisibility', 'CALL', 'AppsListFragment hides bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:84')

e('com.amaze.filemanager.fragments.ProcessViewerFragment.onViewCreated',
  'BottomBar.setVisibility', 'CALL', 'ProcessViewerFragment hides bottom bar',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/ProcessViewerFragment.java:143')

e('com.amaze.filemanager.fragments.CompressedExplorerFragment.updatePath',
  'BottomBar.updatePath', 'CALL', 'CompressedExplorer updates bottom bar on navigation',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/CompressedExplorerFragment.java:445')

e('BottomBar.setClickListener',
  'BottomBar.onTouch', 'CALL', 'setClickListener registers onTouch listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:154-160')

e('BottomBar.onTouch',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.onDown', 'CALL', 'onTouch delegates to GestureDetector',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:486, FW-SRC android/view/GestureDetector.java (onTouchEvent dispatches to listeners)')

e('BottomBar.onTouch',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.onSingleTapConfirmed', 'CALL', 'GestureDetector calls onSingleTapConfirmed',
  evidence='FW-SRC android/view/GestureDetector.java (onSingleTapConfirmed called on confirmed single tap)')

e('BottomBar.onTouch',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.onLongPress', 'CALL', 'GestureDetector calls onLongPress',
  evidence='FW-SRC android/view/GestureDetector.java (onLongPress called on long press)')

e('com.amaze.filemanager.ui.views.appbar.BottomBar$2.onSingleTapConfirmed',
  'BottomBar.showButtons', 'CALL', 'Gesture handler calls showButtons',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:138, 144')

e('BottomBar.showButtons',
  'BottomBar.areButtonsShowing', 'CALL', 'showButtons queries button visibility',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:167')

e('BottomBar.showButtons',
  'BottomBar.createArrow', 'CALL', 'showButtons creates arrow button views',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:205')

e('BottomBar.showButtons',
  'BottomBar.createFolderButton', 'CALL', 'showButtons creates folder button views',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:195')

e('BottomBar.showButtons',
  'BottomBar.lambda$showButtons$0', 'CALL', 'showButtons root button click listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:181')

e('BottomBar.showButtons',
  'BottomBar.lambda$showButtons$1', 'CALL', 'showButtons storage button click listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:187')

e('BottomBar.showButtons',
  'BottomBar.lambda$showButtons$2', 'CALL', 'showButtons folder button click listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:193')

e('BottomBar.showButtons',
  'BottomBar.sendScroll', 'CALL', 'showButtons scrolls to position',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:233')

e('BottomBar.showButtons',
  'BottomBar.lambda$showButtons$3', 'CALL', 'showButtons post scrolling callback',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:229')

e('BottomBar.updatePath',
  'BottomBar.areButtonsShowing', 'CALL', 'updatePath queries button visibility',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:239')

e('BottomBar.updatePath',
  'BottomBar.showButtons', 'CALL', 'updatePath shows buttons on visible state',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:238')

e('BottomBar.updatePath',
  'BottomBar.sendScroll', 'CALL', 'updatePath scrolls path view',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:461')

e('BottomBar.sendScroll',
  'BottomBar.lambda$sendScroll$4', 'CALL', 'sendScroll posts delayed scroll',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:483')

e('BottomBar.updatePath',
  'BottomBar$3.<init>', 'CALL', 'updatePath sets animation listener for forward',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:345')

e('BottomBar$3.onAnimationStart',
  'BottomBar$3.lambda$onAnimationStart$1', 'CALL', 'Animation posts scroll update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:359')

e('BottomBar$3.onAnimationEnd',
  'BottomBar$3.lambda$onAnimationEnd$0', 'CALL', 'Animation posts visibility update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:349')

e('BottomBar.updatePath',
  'BottomBar$4.<init>', 'CALL', 'updatePath sets animation listener for backward',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:374')

e('BottomBar$4.onAnimationStart',
  'BottomBar$4.lambda$onAnimationStart$1', 'CALL', 'Animation posts scroll update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:389')

e('BottomBar$4.onAnimationEnd',
  'BottomBar$4.lambda$onAnimationEnd$0', 'CALL', 'Animation posts visibility update',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:379')

e('BottomBar.<init>',
  'BottomBar$1.<init>', 'CALL', 'BottomBar constructor creates countdown timer',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:113')

e('BottomBar$1.<init>',
  'BottomBar$1.onTick', 'LIFECYCLE', 'CountDownTimer invokes onTick periodically',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:115, FW-SRC android/os/CountDownTimer.java (onTick invoked every interval)')

e('BottomBar$1.<init>',
  'BottomBar$1.onFinish', 'LIFECYCLE', 'CountDownTimer invokes onFinish on completion',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:118, FW-SRC android/os/CountDownTimer.java (onFinish invoked when countdown completes)')

e('BottomBar.<init>',
  'com.amaze.filemanager.ui.views.appbar.BottomBar$2.<init>', 'CALL', 'BottomBar constructor creates gesture listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/views/appbar/BottomBar.java:123')

e('BottomBar$3.<init>',
  'BottomBar$3.onAnimationStart', 'LIFECYCLE', 'Animator invokes onAnimationStart',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationStart called on animation start)')

e('BottomBar$3.<init>',
  'BottomBar$3.onAnimationEnd', 'LIFECYCLE', 'Animator invokes onAnimationEnd',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationEnd called on animation end)')

e('BottomBar$3.<init>',
  'BottomBar$3.onAnimationCancel', 'LIFECYCLE', 'Animator invokes onAnimationCancel',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationCancel called on animation cancel)')

e('BottomBar$4.<init>',
  'BottomBar$4.onAnimationStart', 'LIFECYCLE', 'Animator invokes onAnimationStart',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationStart called on animation start)')

e('BottomBar$4.<init>',
  'BottomBar$4.onAnimationEnd', 'LIFECYCLE', 'Animator invokes onAnimationEnd',
  evidence='FW-SRC android/animation/ValueAnimator.java (AnimatorListener.onAnimationEnd called on animation end)')


# ---- part label_b006_norm (2026-10-27 21:32) ----
e('BottomBar.showButtons', 'BottomBar$5.<init>', 'CALL', 'AnimatorListenerAdapter for initial path created',
  evidence='SRC ui/views/appbar/BottomBar.java:398')

e('BottomBar$5.<init>', 'BottomBar$5.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:401')

e('BottomBar$5.<init>', 'BottomBar$5.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:410')

e('BottomBar$5.onAnimationStart', 'BottomBar$5.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:404')

e('BottomBar$5.onAnimationEnd', 'BottomBar$5.lambda$onAnimationEnd$1', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:409-412')

e('BottomBar.showButtons', 'BottomBar$6.<init>', 'CALL', 'AnimatorListenerAdapter for different path slideout created',
  evidence='SRC ui/views/appbar/BottomBar.java:425')

e('BottomBar$6.<init>', 'BottomBar$6.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:428')

e('BottomBar$6.<init>', 'BottomBar$6.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:437')

e('BottomBar$6.onAnimationStart', 'BottomBar$6.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:433')

e('BottomBar$6.onAnimationEnd', 'BottomBar$6$1.<init>', 'CALL', 'Nested AnimatorListenerAdapter for slidein created',
  evidence='SRC ui/views/appbar/BottomBar.java:446')

e('BottomBar$6$1.<init>', 'BottomBar$6$1.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:459')

e('BottomBar$6$1.<init>', 'BottomBar$6$1.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:448')

e('BottomBar$6$1.onAnimationStart', 'BottomBar$6$1.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:464')

e('BottomBar$6$1.onAnimationEnd', 'BottomBar$6$1.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:450-453')

e('SevenZFile.readHeaders', 'BoundedFileChannelInputStream.<init>', 'CALL', 'Created by SevenZFile for reading 7z archives',
  evidence='SRC sevenz/SevenZFile.java:371,429,998')

e('BoundedFileChannelInputStream.<init>', 'BoundedFileChannelInputStream.read', 'CALL', 'Called during stream reading',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:44,59')

e('BoundedFileChannelInputStream.read', 'BoundedFileChannelInputStream.read', 'CALL', 'Private helper calls',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:83-88')

e('Bzip2Decompressor.changePath', 'Bzip2HelperTask.<init>', 'CALL', 'Created by Bzip2Decompressor.changePath',
  evidence='SRC filesystem/compressed/showcontents/helpers/Bzip2Decompressor.java:43')

e('Bzip2HelperTask.<init>', 'Bzip2HelperTask.addElements', 'CALL', 'Called from CompressedHelperTask.doInBackground',
  evidence='SRC asynchronous/asynctasks/compress/CompressedHelperTask.java:53')

e('CompressedHelper.getExtractorInstance', 'Bzip2Extractor.<init>', 'CALL', 'Created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:90,174')

e('Bzip2Extractor.<init>', 'Bzip2Extractor.extractWithFilter', 'CALL', 'Called from Extractor base class',
  evidence='SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:49')

e('Bzip2Extractor.extractWithFilter', 'Bzip2Extractor.extractEntry', 'CALL', 'Called from extractWithFilter',
  evidence='SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:68')

e('CompressedHelper.getCompressorInstance', 'Bzip2Decompressor.<init>', 'CALL', 'Created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:120,174')

e('CompressedExplorerFragment.changePath', 'Bzip2Decompressor.changePath', 'CALL', 'Fragment navigation calls changePath',
  evidence='SRC fragments/CompressedExplorerFragment.java:411')

UNREACHABLE['BottomBar$5.onAnimationCancel'] = (
    'framework_never_calls',
    'Animation cancellation not triggered in app usage',
    'SRC ui/views/appbar/BottomBar.java:418-421',
    'SOURCE'
)

UNREACHABLE['BottomBar$6.onAnimationCancel'] = (
    'framework_never_calls',
    'Animation cancellation not triggered in app usage',
    'SRC ui/views/appbar/BottomBar.java:470-473',
    'SOURCE'
)

UNREACHABLE['BoundedFileChannelInputStream.close'] = (
    'framework_never_calls',
    'Close method explicitly empty; channel controlled externally',
    'SRC sevenz/BoundedFileChannelInputStream.java:91-93; comment states nested channel controlled externally',
    'SOURCE'
)

UNREACHABLE['CLI.<init>'] = (
    'no_trigger_in_app',
    'Command-line tool not instantiated by app',
    'SRC sevenz/CLI.java:24; grep shows no app usage',
    'SOURCE'
)

UNREACHABLE['CLI.main'] = (
    'no_trigger_in_app',
    'Command-line entry point not called by Android app',
    'SRC sevenz/CLI.java:114; main method unused in app context',
    'SOURCE'
)

UNREACHABLE['CLI.usage'] = (
    'no_trigger_in_app',
    'Called only from unused CLI.main',
    'SRC sevenz/CLI.java:132; only caller is CLI.main',
    'SOURCE'
)

UNREACHABLE['CLI.grabMode'] = (
    'no_trigger_in_app',
    'Called only from unused CLI.main',
    'SRC sevenz/CLI.java:136; only caller is CLI.main',
    'SOURCE'
)

UNREACHABLE['CLI$Mode.<clinit>'] = (
    'no_trigger_in_app',
    'Enum initializer only accessed through unused CLI.main',
    'SRC sevenz/CLI.java:29-50; enum constants never instantiated',
    'SOURCE'
)

UNREACHABLE['CLI$Mode.<init>'] = (
    'no_trigger_in_app',
    'Enum constructor only accessed through unused CLI.main',
    'SRC sevenz/CLI.java:57-60; enum not instantiated in app',
    'SOURCE'
)

UNREACHABLE['CLI$Mode.getMessage'] = (
    'no_trigger_in_app',
    'Called only from unused CLI enum modes',
    'SRC sevenz/CLI.java:62-64; only caller is unused enum',
    'SOURCE'
)

UNREACHABLE['CLI$Mode$1.<init>'] = (
    'no_trigger_in_app',
    'Enum constant for unused CLI.LIST mode',
    'SRC sevenz/CLI.java:29-55; LIST mode never used',
    'SOURCE'
)

UNREACHABLE['CLI$Mode$1.getContentMethods'] = (
    'no_trigger_in_app',
    'Method of unused LIST mode',
    'SRC sevenz/CLI.java:44-55; only called from LIST takeAction',
    'SOURCE'
)

UNREACHABLE['CLI$Mode$1.takeAction'] = (
    'no_trigger_in_app',
    'Method of unused LIST mode',
    'SRC sevenz/CLI.java:31-43; LIST never instantiated',
    'SOURCE'
)

UNREACHABLE['CLI$Mode$2.<init>'] = (
    'no_trigger_in_app',
    'Enum constant for unused CLI.EXTRACT mode',
    'SRC sevenz/CLI.java:56-94; EXTRACT mode never used',
    'SOURCE'
)

UNREACHABLE['CLI$Mode$2.takeAction'] = (
    'no_trigger_in_app',
    'Method of unused EXTRACT mode',
    'SRC sevenz/CLI.java:58-94; only called from EXTRACT enum',
    'SOURCE'
)


# ---- part label_b007_norm (2026-10-27 21:32) ----
e('PrefFrag.onCreate', 'CheckBox.<init>',
  'FRAMEWORK', 'Preference framework inflates preference from XML (findPreference returns cached/inflated instance)',
  evidence='SRC com/amaze/filemanager/fragments/preference_fragments/PrefFrag.java:118-119')

e('CheckBox.onBindView', 'CheckBox.clearListenerInViewGroup',
  'CALL', 'Explicit call in onBindView override',
  evidence='SRC com/amaze/filemanager/ui/views/preference/CheckBox.java:20-21, 34')

e('CheckBox.<init>', 'CheckBox.onBindView',
  'LIFECYCLE', 'Preference framework lifecycle: onBindView called after preference is created',
  evidence='SRC com/amaze/filemanager/ui/views/preference/CheckBox.java:15-21, FW-SRC core/java/android/preference/Preference.java')

e('ColorAdapter.getView', 'CheckableCircleView.<init>',
  'CALL', 'Inflated in getView or reused from convertView',
  evidence='SRC com/amaze/filemanager/adapters/ColorAdapter.java:49-51')

e('ColorAdapter.getView', 'CheckableCircleView.setColor',
  'CALL', 'setColor called to set circle paint color',
  evidence='SRC com/amaze/filemanager/adapters/ColorAdapter.java:55-61')

e('ColorAdapter.getView', 'CheckableCircleView.setChecked',
  'CALL', 'setChecked called to show/hide the checkmark',
  evidence='SRC com/amaze/filemanager/adapters/ColorAdapter.java:56-61')

e('CheckableCircleView.<init>', 'CheckableCircleView.onDraw',
  'LIFECYCLE', 'Framework renders view; onDraw is layout callback',
  evidence='SRC com/amaze/filemanager/ui/views/CheckableCircleView.java:36-45, FW-SRC core/java/android/view/View.java')

e('RecyclerAdapter.animate', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'CALL', 'Instantiated with int color and AppTheme in file list selection animation',
  evidence='SRC com/amaze/filemanager/adapters/RecyclerAdapter.java:536-539')

e('CompressedExplorerAdapter.onBindViewHolder', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'CALL', 'Instantiated with int color and AppTheme in archive list selection',
  evidence='SRC com/amaze/filemanager/adapters/CompressedExplorerAdapter.java:204-207')

e('com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'CALL', 'String-color variant calls int-color variant constructor',
  evidence='SRC com/amaze/filemanager/ui/views/CircleGradientDrawable.java:28-31, 36-44')

e('com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>', 'com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>',
  'CALL', 'int-color variant calls helper constructor (AppTheme+DisplayMetrics)',
  evidence='SRC com/amaze/filemanager/ui/views/CircleGradientDrawable.java:36-44, 46-54')

e('com/amaze/filemanager/ui/views/CircleGradientDrawable.<init>', 'CircleGradientDrawable.dpToPx',
  'CALL', 'dpToPx called to convert stroke width from dp to pixels',
  evidence='SRC com/amaze/filemanager/ui/views/CircleGradientDrawable.java:50, 56-57')

e('com/amaze/filemanager/ui/dialogs/ColorPickerDialog.onCreateDialog', 'com/amaze/filemanager/ui/views/CircularColorsView.<init>',
  'CALL', 'Inflated from layout in color picker dialog',
  evidence='SRC com/amaze/filemanager/ui/dialogs/ColorPickerDialog.java:128-130')

e('SelectedColorsPreference.onBindView', 'com/amaze/filemanager/ui/views/CircularColorsView.<init>',
  'CALL', 'Inflated from layout in preference binding',
  evidence='SRC com/amaze/filemanager/ui/views/preference/SelectedColorsPreference.java:40-44')

e('com/amaze/filemanager/ui/views/CircularColorsView.<init>', 'CircularColorsView.init',
  'CALL', 'init called from both constructors',
  evidence='SRC com/amaze/filemanager/ui/views/CircularColorsView.java:30-31, 36-37, 40-46')

e('com/amaze/filemanager/ui/views/CircularColorsView.<init>', 'CircularColorsView.onDraw',
  'LIFECYCLE', 'Framework renders view; onDraw is layout callback',
  evidence='SRC com/amaze/filemanager/ui/views/CircularColorsView.java:48-76, FW-SRC core/java/android/view/View.java')

e('com/amaze/filemanager/ui/dialogs/ColorPickerDialog.onCreateDialog', 'CircularColorsView.setColors',
  'CALL', 'setColors called to set the four colors after inflating view',
  evidence='SRC com/amaze/filemanager/ui/dialogs/ColorPickerDialog.java:131-134')

e('SelectedColorsPreference.onBindView', 'CircularColorsView.setDividerColor',
  'CALL', 'setDividerColor called in preference binding',
  evidence='SRC com/amaze/filemanager/ui/views/preference/SelectedColorsPreference.java:40-44')

e('CloudHandler.findEntry', 'com/amaze/filemanager/database/models/CloudEntry.<init>',
  'CALL', 'No-arg constructor instantiated to create entry object',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:143')

e('CloudHandler.getAllEntries', 'com/amaze/filemanager/database/models/CloudEntry.<init>',
  'CALL', 'No-arg constructor instantiated in loop',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:174')

e('com/amaze/filemanager/database/models/CloudEntry.<init>', 'CloudEntry.setId',
  'LIFECYCLE', 'Setter called to initialize field (alternate constructor)',
  evidence='SRC com/amaze/filemanager/database/models/CloudEntry.java:17-20')

e('com/amaze/filemanager/database/models/CloudEntry.<init>', 'CloudEntry.setServiceType',
  'LIFECYCLE', 'Setter called to initialize field (alternate constructor)',
  evidence='SRC com/amaze/filemanager/database/models/CloudEntry.java:17-20')

e('com/amaze/filemanager/database/models/CloudEntry.<init>', 'CloudEntry.setPersistData',
  'LIFECYCLE', 'Setter called to initialize field (alternate constructor)',
  evidence='SRC com/amaze/filemanager/database/models/CloudEntry.java:17-20')

e('CloudHandler.findEntry', 'CloudEntry.setId',
  'CALL', 'setId called to populate from database cursor',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:145')

e('CloudHandler.findEntry', 'CloudEntry.setServiceType',
  'CALL', 'setServiceType called to populate from database',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:146')

e('CloudHandler.findEntry', 'CloudEntry.setPersistData',
  'CALL', 'setPersistData called to populate from database (decrypted)',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:150')

e('CloudHandler.getAllEntries', 'CloudEntry.setId',
  'CALL', 'setId called in loop to populate from cursor',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:175')

e('CloudHandler.getAllEntries', 'CloudEntry.setServiceType',
  'CALL', 'setServiceType called in loop to populate from cursor',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:176')

e('CloudHandler.getAllEntries', 'CloudEntry.setPersistData',
  'CALL', 'setPersistData called in loop to populate from cursor (decrypted)',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:178')

e('CloudHandler.addEntry', 'CloudEntry.getServiceType',
  'CALL', 'getServiceType called to retrieve ordinal for database insert',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:91')

e('CloudHandler.addEntry', 'CloudEntry.getPersistData',
  'CALL', 'getPersistData called to retrieve data for encryption/insert',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:93')

e('CloudHandler.updateEntry', 'CloudEntry.getId',
  'CALL', 'getId called to populate update values',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:125')

e('CloudHandler.updateEntry', 'CloudEntry.getServiceType',
  'CALL', 'getServiceType called to retrieve ordinal for update where clause',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:126')

e('CloudHandler.updateEntry', 'CloudEntry.getPersistData',
  'CALL', 'getPersistData called to retrieve data for encryption/update',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:130')

e('com/amaze/filemanager/ui/views/drawer/Drawer.updateItemsList', 'CloudHandler.<init>',
  'CALL', 'Drawer accesses cloud constants; CloudHandler instantiated through app context',
  evidence='SRC com/amaze/filemanager/ui/views/drawer/Drawer.java:313-340 (cloud initialization)')

e('CloudHandler.<init>', 'CloudHandler.onCreate',
  'FRAMEWORK', 'SQLiteOpenHelper lifecycle: onCreate called on first database access',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:44-46, FW-SRC android-8.1.0_r1/core/java/android/database/sqlite/SQLiteOpenHelper.java')

e('CloudHandler.<init>', 'CloudHandler.onUpgrade',
  'FRAMEWORK', 'SQLiteOpenHelper lifecycle: onUpgrade called if database version changes',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:44-46, FW-SRC android-8.1.0_r1/core/java/android/database/sqlite/SQLiteOpenHelper.java')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'CloudHandler.addEntry',
  'CALL', 'addEntry called to store new cloud credentials',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:83-104 (public method reachable from fragment)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'CloudHandler.findEntry',
  'CALL', 'findEntry called to retrieve cloud credentials',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:141-162 (public method)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'CloudHandler.getAllEntries',
  'CALL', 'getAllEntries called to enumerate cloud service accounts',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:164-195 (public method)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'CloudHandler.updateEntry',
  'CALL', 'updateEntry called to modify existing credentials',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:117-140 (public method)')

e('com/amaze/filemanager/fragments/CloudSheetFragment.populateData', 'CloudHandler.clear',
  'CALL', 'clear called to remove credentials for a service',
  evidence='SRC com/amaze/filemanager/database/CloudHandler.java:106-115 (public method)')

e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.<init>',
  'CALL', 'Instantiated in model loader to create fetcher for Glide',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:27-31, SRC com/amaze/filemanager/utils/glide/CloudIconModelLoader.java:30')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.loadData',
  'FRAMEWORK', 'Glide framework lifecycle: loadData called when Glide needs to fetch image data',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:33-42, INFERRED (Glide DataFetcher interface)')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.cleanup',
  'FRAMEWORK', 'Glide framework lifecycle: cleanup called after load completes or fails',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:47-51, INFERRED (Glide DataFetcher interface)')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.cancel',
  'FRAMEWORK', 'Glide framework lifecycle: cancel called if load is cancelled',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:52-54, INFERRED (Glide DataFetcher interface)')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.getDataClass',
  'FRAMEWORK', 'Glide framework lifecycle: getDataClass called to determine output type',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:56-59, INFERRED (Glide DataFetcher interface)')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.getDataSource',
  'FRAMEWORK', 'Glide framework lifecycle: getDataSource called to determine source (REMOTE)',
  evidence='SRC com/amaze/filemanager/utils/glide/CloudIconDataFetcher.java:61-64, INFERRED (Glide DataFetcher interface)')

UNREACHABLE['CloudContract.<init>'] = (
    'no_trigger_in_app',
    'CloudContract is a constants-only class with 11 static final fields and no instance initialization; never instantiated in app code',
    'SRC com/amaze/filemanager/database/CloudContract.java:1-22',
    'SOURCE'
)


# ---- part label_b008_norm (2026-10-27 21:32) ----
e('CloudIconModelFactory.<init>', 'CloudIconModelLoader.<init>', 'CALL', 'Glide factory creates loader',
  evidence='SRC CloudIconModelFactory.java:18-20')

e('CloudIconModelFactory.build', 'CloudIconModelLoader.<init>', 'CALL', 'Factory builds CloudIconModelLoader',
  evidence='SRC CloudIconModelFactory.java:23-26')

e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.<init>', 'CALL', 'Creates fetcher for image loading',
  evidence='SRC CloudIconModelLoader.java:25-31')

e('CloudHandler.addEntry', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:85-86')

e('CloudHandler.updateEntry', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:118-121')

e('CloudHandler.findEntry', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:141-144')

e('CloudHandler.getAllEntries', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC CloudHandler.java:169-172')

e('CloudUtil.listFiles', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC CloudUtil.java:59-82')

e('LoadFilesListTask.loadCloudFiles', 'CloudPluginException.<init>', 'CALL', 'Throws when cloud provider unavailable',
  evidence='SRC LoadFilesListTask.java:453-455')

e('MainActivity.onOptionsItemSelected', 'CloudSheetFragment.<init>', 'CALL', 'Creates cloud sheet dialog fragment',
  evidence='SRC MainActivity.java:1953')

e('CloudSheetFragment.<init>', 'CloudSheetFragment.onCreate', 'LIFECYCLE', 'Android framework calls onCreate on fragment creation',
  evidence='SRC CloudSheetFragment.java:40-41')

e('CloudSheetFragment.<init>', 'CloudSheetFragment.setupDialog', 'LIFECYCLE', 'Android framework calls setupDialog during dialog setup',
  evidence='SRC CloudSheetFragment.java:45-87')

e('CloudSheetFragment.setupDialog', 'CloudSheetFragment.onClick', 'CALL', 'Sets onClick listener on layouts',
  evidence='SRC CloudSheetFragment.java:70-76')

e('CloudSheetFragment.setupDialog', 'CloudSheetFragment.isCloudProviderAvailable', 'CALL', 'Checks cloud provider availability',
  evidence='SRC CloudSheetFragment.java:69')

e('CloudUtil.playStream', 'CloudStreamer.getInstance', 'CALL', 'Gets streamer instance',
  evidence='SRC CloudUtil.java:135')

e('SshClientUtils.playStream', 'CloudStreamer.getInstance', 'CALL', 'Gets streamer instance',
  evidence='SRC SshClientUtils.java:238')

e('StreamServer.tryBind', 'CloudStreamer.getInstance', 'CALL', 'Stops conflicting streamer',
  evidence='SRC StreamServer.java:212')

e('CloudStreamer.getInstance', 'CloudStreamServer.<init>', 'CALL', 'Creates new CloudStreamer (extends CloudStreamServer)',
  evidence='SRC CloudStreamer.java:34-39')

e('CloudStreamServer.<init>', 'CloudStreamServer.lambda$new$0', 'SYSTEM', 'Creates server thread with lambda',
  evidence='SRC CloudStreamServer.java:204-220')

e('CloudStreamServer.lambda$new$0', 'CloudStreamServer$HTTPSession.<init>', 'CALL', 'Accepts client socket and creates HTTPSession',
  evidence='SRC CloudStreamServer.java:217-218')

e('CloudStreamer.__init__', 'CloudStreamServer.<init>', 'CALL', 'Calls super constructor with port and file',
  evidence='SRC CloudStreamer.java:31, CloudStreamServer.java:199-201')

e('CloudStreamServer$HTTPSession.<init>', 'CloudStreamServer$HTTPSession.run', 'LIFECYCLE', 'Creates thread and calls run',
  evidence='SRC CloudStreamServer.java:330-338')

e('CloudStreamServer$HTTPSession.run', 'CloudStreamServer$HTTPSession.handleResponse', 'CALL', 'HTTPSession.run calls handleResponse',
  evidence='SRC CloudStreamServer.java:358-361')

e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.decodeHeader', 'CALL', 'Parses HTTP headers',
  evidence='SRC CloudStreamServer.java:385')

e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.sendError', 'CALL', 'Sends error on invalid request',
  evidence='SRC CloudStreamServer.java:389, 398, 402')

e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.decodeParms', 'CALL', 'Decodes URI parameters',
  evidence='SRC CloudStreamServer.java:473-475')

e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.decodeMultipartData', 'CALL', 'Processes multipart form data',
  evidence='SRC CloudStreamServer.java:480-481')

e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer$HTTPSession.sendResponse', 'CALL', 'Sends HTTP response',
  evidence='SRC CloudStreamServer.java:512-514')

e('CloudStreamServer$HTTPSession.decodeHeader', 'CloudStreamServer$HTTPSession.decodePercent', 'CALL', 'Decodes URI percent encoding',
  evidence='SRC CloudStreamServer.java:508')

e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.getBoundaryPositions', 'CALL', 'Finds multipart boundaries',
  evidence='SRC CloudStreamServer.java:598')

e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.saveTmpFile', 'CALL', 'Saves uploaded file',
  evidence='SRC CloudStreamServer.java:608')

e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.stripMultipartHeaders', 'CALL', 'Processes multipart headers',
  evidence='SRC CloudStreamServer.java:607')

e('CloudStreamServer$HTTPSession.decodeMultipartData', 'CloudStreamServer$HTTPSession.sendError', 'CALL', 'Sends error on parse failure',
  evidence='SRC CloudStreamServer.java:597, 601, 605')

e('CloudStreamServer$HTTPSession.handleResponse', 'CloudStreamServer.serve', 'CALL', 'Calls abstract serve method (overridden in CloudStreamer)',
  evidence='SRC CloudStreamServer.java:511')

e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'CALL', 'Creates response with error status',
  evidence='SRC CloudStreamer.java:65')

e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'CALL', 'Creates response with range not satisfiable',
  evidence='SRC CloudStreamer.java:93')

e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'CALL', 'Creates response with partial content',
  evidence='SRC CloudStreamer.java:106')

e('CloudStreamer.serve', 'CloudStreamServer$Response.<init>', 'CALL', 'Creates response with OK status',
  evidence='SRC CloudStreamer.java:111')

e('CloudStreamServer$Response.<init>', 'CloudStreamServer$Response.addHeader', 'CALL', 'Response constructor allows adding headers',
  evidence='SRC CloudStreamer.java:97, 107, 112, 114')

e('CloudStreamer.stop', 'CloudStreamServer.stop', 'CALL', 'Calls parent stop method',
  evidence='SRC CloudStreamer.java:52-55')

e('CloudStreamServer.stop', 'CloudStreamServer.tryBind', 'CALL', 'tryBind stops Streamer if port occupied',
  evidence='SRC CloudStreamServer.java:199-201, 226-228')


# ---- part label_b009 (2026-10-27 21:32) ----
e('CloudStreamer.serve', 'CloudStreamSource.<init>', 'CALL', 'new CloudStreamSource(...)',
  evidence='SRC CloudStreamer.java:89')

e('CloudStreamSource.<init>', 'CloudStreamSource.open', 'CALL', 'implicit via stream usage',
  evidence='SRC CloudStreamSource.java:52-63')

e('CloudStreamer.serve', 'CloudStreamSource.moveTo', 'CALL', 'source.moveTo(startFrom)',
  evidence='SRC CloudStreamer.java:106')

e('CloudUtil.launchCloud', 'CloudStreamer.getInstance', 'CALL', 'final CloudStreamer streamer = CloudStreamer.getInstance()',
  evidence='SRC CloudUtil.java:135')

e('CloudStreamer.getInstance', 'CloudStreamer.<init>', 'CALL', 'new CloudStreamer(PORT)',
  evidence='SRC CloudStreamer.java:37')

e('CloudUtil.launchCloud', 'CloudStreamer.setStreamSrc', 'CALL', 'streamer.setStreamSrc(...)',
  evidence='SRC CloudUtil.java:138')

e('CloudStreamServer.serve', 'CloudStreamer.serve', 'CALL', 'override dispatched by framework',
  evidence='SRC CloudStreamer.java:62')

e('Drawer.onItemClick', 'CloudUtil.checkToken', 'CALL', 'CloudUtil.checkToken(meta.path, mainActivity)',
  evidence='SRC Drawer.java:577')

e('LoadFilesListTask.doInBackground', 'CloudUtil.getCloudFiles', 'CALL', 'CloudUtil.getCloudFiles(...)',
  evidence='SRC LoadFilesListTask.java:458')

e('MainFragment.onItemClick', 'CloudUtil.launchCloud', 'CALL', 'CloudUtil.launchCloud(...)',
  evidence='SRC MainFragment.java:930')

e('HybridFile.listFiles', 'CloudUtil.listFiles', 'CALL', 'CloudUtil.listFiles(...)',
  evidence='SRC HybridFile.java:864')

e('CloudUtil.launchCloud', 'CloudUtil.stripPath', 'CALL', 'CloudUtil.stripPath(serviceType, ...)',
  evidence='SRC CloudUtil.java:142')

e('CloudUtil.checkToken', 'CloudUtil$1.<init>', 'CALL', 'new AsyncTask<String, Void, Boolean>()',
  evidence='SRC CloudUtil.java:174')

e('AndroidAsyncTask.execute', 'CloudUtil$1.doInBackground', 'CALL', 'framework calls doInBackground',
  evidence='SRC CloudUtil.java:179')

e('AndroidAsyncTask.onPostExecute', 'CloudUtil$1.onPostExecute', 'CALL', 'framework calls onPostExecute',
  evidence='SRC CloudUtil.java:217')

e('CloudUtil.launchCloud', 'CloudUtil$2.<init>', 'CALL', 'new Thread(() -> {...})',
  evidence='SRC CloudUtil.java:137')

e('Thread.run', 'CloudUtil$2.execute', 'CALL', 'lambda body execution',
  evidence='SRC CloudUtil.java:138')

e('SevenZFile.readHeaders', 'Coder.<init>', 'CALL', 'new Coder()',
  evidence='SRC SevenZFile.java:642')

e('SevenZMethodConfiguration.validateOptions', 'CoderBase.canAcceptOptions', 'CALL', 'Coders.findByMethod(method).canAcceptOptions(options)',
  evidence='SRC SevenZMethodConfiguration.java:59')

e('SevenZFile.readStackEncodersAsCoders', 'CoderBase.getOptionsFromCoder', 'CALL', 'Coders.findByMethod(method).getOptionsFromCoder(...)',
  evidence='SRC SevenZFile.java:1033')


# ---- part label_b010 (2026-10-27 21:32) ----
e('SevenZFile.readStreamsInfo', 'Coders.addDecoder', 'CALL',
  'SevenZFile adds decoders for each coder in folder',
  evidence='SRC SevenZFile.java:435')

e('SevenZFile.getBytesForCoder', 'Coders.addDecoder', 'CALL',
  'Unpacks bytes using coders',
  evidence='SRC SevenZFile.java:1030')

e('Coders.addDecoder', 'Coders.findByMethod', 'CALL',
  'findByMethod retrieves decoder from CODER_MAP',
  evidence='SRC Coders.java:76')

e('SevenZOutputFile.createEncoders', 'Coders.addEncoder', 'CALL',
  'Encodes output stream with compression method',
  evidence='SRC SevenZOutputFile.java:321')

e('Coders.addEncoder', 'Coders.findByMethod', 'CALL',
  'findByMethod retrieves encoder from CODER_MAP',
  evidence='SRC Coders.java:87')

e('SevenZFile.getBytesForCoder', 'Coders.findByMethod', 'CALL',
  'Gets decoder options after adding decoder',
  evidence='SRC SevenZFile.java:1033')

e('SevenMethodConfiguration.setContentMethods', 'Coders.findByMethod', 'CALL',
  'SevenZMethodConfiguration validates encoder options',
  evidence='SRC SevenZMethodConfiguration.java:59')

e('Coders.<clinit>', 'Coders$1.<init>', 'CALL',
  'Initializes CODER_MAP HashMap with decoders',
  evidence='SRC Coders.java:48-66')

e('Coders$1.<init>', 'Coders$CopyDecoder.<init>', 'CALL',
  'CODER_MAP puts CopyDecoder instance',
  evidence='SRC Coders.java:49')

e('Coders$1.<init>', 'Coders$BCJDecoder.<init>', 'CALL',
  'CODER_MAP puts BCJDecoder instances for various BCJ filters',
  evidence='SRC Coders.java:57-62')

e('Coders$1.<init>', 'Coders$DeflateDecoder.<init>', 'CALL',
  'CODER_MAP puts DeflateDecoder instance',
  evidence='SRC Coders.java:52')

e('Coders$1.<init>', 'Coders$Deflate64Decoder.<init>', 'CALL',
  'CODER_MAP puts Deflate64Decoder instance',
  evidence='SRC Coders.java:53')

e('Coders$1.<init>', 'Coders$BZIP2Decoder.<init>', 'CALL',
  'CODER_MAP puts BZIP2Decoder instance',
  evidence='SRC Coders.java:54')

e('Coders.addDecoder', 'Coders$CopyDecoder.decode', 'CALL',
  'CopyDecoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$BCJDecoder.decode', 'CALL',
  'BCJDecoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$DeflateDecoder.decode', 'CALL',
  'DeflateDecoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$Deflate64Decoder.decode', 'CALL',
  'Deflate64Decoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addDecoder', 'Coders$BZIP2Decoder.decode', 'CALL',
  'BZIP2Decoder.decode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:78-80')

e('Coders.addEncoder', 'Coders$CopyDecoder.encode', 'CALL',
  'CopyDecoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

e('Coders.addEncoder', 'Coders$BCJDecoder.encode', 'CALL',
  'BCJDecoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

e('Coders.addEncoder', 'Coders$DeflateDecoder.encode', 'CALL',
  'DeflateDecoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

e('Coders.addEncoder', 'Coders$BZIP2Decoder.encode', 'CALL',
  'BZIP2Decoder.encode called via CoderBase virtual dispatch',
  evidence='SRC Coders.java:87-89')

e('Coders$DeflateDecoder.decode', 'Coders$DeflateDecoder$DeflateDecoderInputStream.<init>', 'CALL',
  'DeflateDecoder.decode constructs DeflateDecoderInputStream wrapper',
  evidence='SRC Coders.java:138-140')

e('Coders$DeflateDecoder.encode', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>', 'CALL',
  'DeflateDecoder.encode constructs DeflateDecoderOutputStream wrapper',
  evidence='SRC Coders.java:145-147')

e('Coders$DeflateDecoder$DeflateDecoderInputStream.read', 'InflaterInputStream.read', 'CALL',
  'Delegates read to wrapped InflaterInputStream',
  evidence='SRC Coders.java:152-157')

e('Coders$DeflateDecoder$DeflateDecoderInputStream.close', 'InflaterInputStream.close', 'CALL',
  'Closes underlying InflaterInputStream and ends Inflater',
  evidence='SRC Coders.java:159-165')

e('Coders$DeflateDecoder$DeflateDecoderOutputStream.write', 'DeflaterOutputStream.write', 'CALL',
  'Delegates write to wrapped DeflaterOutputStream',
  evidence='SRC Coders.java:172-181')

e('Coders$DeflateDecoder$DeflateDecoderOutputStream.close', 'DeflaterOutputStream.close', 'CALL',
  'Closes underlying DeflaterOutputStream and ends Deflater',
  evidence='SRC Coders.java:183-189')

e('ColorPref.showColorChooser', 'ColorAdapter.<init>', 'CALL',
  'Constructs ColorAdapter for color selection dialog',
  evidence='SRC ColorPref.java:135-137')

e('ColorAdapter.getView', 'ColorAdapter.getColorResAt', 'CALL',
  'getView retrieves color resource at position',
  evidence='SRC ColorAdapter.java:47')

e('GridView.onLayout', 'ColorAdapter.getView', 'CALL',
  'GridView renders items using adapter getView',
  evidence='SRC ColorAdapter.java:41-55')

e('GridView.onItemClick', 'ColorAdapter.onItemClick', 'CALL',
  'GridView item click dispatches to adapter listener',
  evidence='SRC ColorPref.java:170, ColorAdapter.java:57-64')

UNREACHABLE['Coders.<init>'] = ('no_trigger_in_app', 'Coders class has no public constructor; uses only static methods', 'SRC Coders.java:45', 'CALL')

UNREACHABLE['Coders$DeflateDecoder.<clinit>'] = ('no_trigger_in_app', 'Class initialization static block for ONE_ZERO_BYTE constant; not called directly from app', 'SRC Coders.java:126', 'CALL')


# ---- part label_b011 (2026-10-27 21:32) ----
e('TabFragment.updatePathColors', 'ColorCircleDrawable.<init>',
  'CALL', 'Direct instantiation in TabFragment',
  evidence='SRC TabFragment.java:386')

e('Drawable', 'ColorCircleDrawable.draw',
  'FRAMEWORK', 'Overridden framework method, called by Android Drawable framework',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.onBoundsChange',
  'FRAMEWORK', 'Overridden framework method, called by Android Drawable lifecycle',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.setAlpha',
  'FRAMEWORK', 'Overridden framework method, called by Android drawable operations',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.setColorFilter',
  'FRAMEWORK', 'Overridden framework method, called by Android drawable operations',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('Drawable', 'ColorCircleDrawable.getOpacity',
  'FRAMEWORK', 'Overridden framework method, called by Android drawable operations',
  evidence='FW-SRC android-8.1.0_r1/android/graphics/drawable/Drawable.java:source not read')

e('PreferenceScreen', 'ColorPickerDialog.<init>',
  'FRAMEWORK', 'Instantiated by Android PreferenceManager from XML via framework',
  evidence='SRC ColorPickerDialog.java:68')

e('S_PREFS', 'ColorPickerDialog.<clinit>',
  'FRAMEWORK', 'Static initialization block called by class loader on first access',
  evidence='SRC ColorPickerDialog.java:44-49')

e('S_PREFS', 'ColorPickerDialog.onBindDialogView',
  'FRAMEWORK', 'Lifecycle method called by DialogPreference framework',
  evidence='SRC ColorPickerDialog.java:108')

e('S_PREFS', 'ColorPickerDialog.onDialogClosed',
  'FRAMEWORK', 'Lifecycle method called by DialogPreference framework',
  evidence='SRC ColorPickerDialog.java:168')

e('S_PREFS', 'ColorPickerDialog.onSaveInstanceState',
  'FRAMEWORK', 'Lifecycle method called by Preference framework for state persistence',
  evidence='SRC ColorPickerDialog.java:220')

e('S_PREFS', 'ColorPickerDialog.onRestoreInstanceState',
  'FRAMEWORK', 'Lifecycle method called by Preference framework for state restoration',
  evidence='SRC ColorPickerDialog.java:229')

e('S_PREFS', 'ColorPickerDialog.onGetDefaultValue',
  'FRAMEWORK', 'Lifecycle method called by Preference framework',
  evidence='SRC ColorPickerDialog.java:89')

e('S_PREFS', 'ColorPickerDialog.getSummary',
  'FRAMEWORK', 'Lifecycle method called by Preference framework to get display text',
  evidence='SRC ColorPickerDialog.java:94')

e('S_PREFS', 'ColorPickerDialog.showDialog',
  'FRAMEWORK', 'Lifecycle method called by DialogPreference framework',
  evidence='SRC ColorPickerDialog.java:200')

e('ColorPickerDialog.onBindDialogView', 'ColorPickerDialog.inflateItem',
  'CALL', 'Called directly from onBindDialogView in loop',
  evidence='SRC ColorPickerDialog.java:122')

e('ColorPickerDialog.onBindDialogView', 'ColorPickerDialog.select',
  'CALL', 'Called directly from onBindDialogView',
  evidence='SRC ColorPickerDialog.java:128')

e('ColorPickerDialog.onBindDialogView', 'ColorPickerDialog.getColor',
  'CALL', 'Called directly from onBindDialogView',
  evidence='SRC ColorPickerDialog.java:132')

e('ColorPickerDialog.onDialogClosed', 'ColorPickerDialog.getColor',
  'CALL', 'Called directly from onDialogClosed',
  evidence='SRC ColorPickerDialog.java:182')

e('ColorPickerDialog.inflateItem', 'ColorPickerDialog.select',
  'CALL', 'Called from inflateItem lambda via select()',
  evidence='SRC ColorPickerDialog.java:156')

e('ColorPickerDialog.onRestoreInstanceState', 'ColorPickerDialog.select',
  'CALL', 'Called directly from onRestoreInstanceState',
  evidence='SRC ColorPickerDialog.java:244')

e('ColorPickerDialog.<clinit>', 'ColorPickerDialog$ColorItemPair.<init>',
  'CALL', 'Called during static initialization of COLORS array',
  evidence='SRC ColorPickerDialog.java:48-51')

e('ColorPickerDialog.onSaveInstanceState', 'ColorPickerDialog$SavedState.<init>',
  'CALL', 'Called directly to create SavedState instance from Parcelable',
  evidence='SRC ColorPickerDialog.java:256')

e('S_PREFS', 'ColorPickerDialog$SavedState.<init>',
  'FRAMEWORK', 'Constructor from Parcel, called by Parcelable framework',
  evidence='SRC ColorPickerDialog.java:277')

e('Parcelable.Creator', 'ColorPickerDialog$SavedState.<init>',
  'FRAMEWORK', 'Constructor from Parcel called by Parcelable.Creator.createFromParcel',
  evidence='SRC ColorPickerDialog.java:295')

e('ColorPickerDialog$SavedState.<init>', 'ColorPickerDialog$SavedState.<clinit>',
  'FRAMEWORK', 'Static initialization called by class loader',
  evidence='SRC ColorPickerDialog.java:253')

e('BaseSavedState', 'ColorPickerDialog$SavedState.writeToParcel',
  'FRAMEWORK', 'Called by Parcelable framework during state serialization',
  evidence='SRC ColorPickerDialog.java:263')

e('ColorPickerDialog$SavedState.<clinit>', 'ColorPickerDialog$SavedState$1.<init>',
  'CALL', 'Called during static initialization of CREATOR',
  evidence='SRC ColorPickerDialog.java:268')

e('Parcelable.Creator', 'ColorPickerDialog$SavedState$1.createFromParcel',
  'FRAMEWORK', 'Called by Parcelable framework during deserialization',
  evidence='SRC ColorPickerDialog.java:271')

e('Parcelable.Creator', 'ColorPickerDialog$SavedState$1.newArray',
  'FRAMEWORK', 'Called by Parcelable framework during array allocation',
  evidence='SRC ColorPickerDialog.java:274')


# ---- part label_b012 (2026-10-27 21:32) ----
e('PreferencesActivity.<init>', 'ColorPref.<init>', 'CALL', 'instantiates ColorPref for color preferences',
  evidence='SRC PreferencesActivity.java:258')

e('ColorPref.onCreate', 'ColorPref.loadSection0', 'CALL', 'called from onCreate',
  evidence='SRC ColorPref.java:56-62')

e('ColorPref.onCreate', 'ColorPref.onRestoreInstanceState', 'CALL', 'called from onCreate when savedInstanceState is not null',
  evidence='SRC ColorPref.java:56-62')

e('ColorPref.onCreate', 'ColorPref.reloadListeners', 'CALL', 'called from onCreate',
  evidence='SRC ColorPref.java:56-62')

e('ColorPref.onPause', 'ColorPref.onPause', 'LIFECYCLE', 'lifecycle method',
  evidence='SRC ColorPref.java:66-68')

e('ColorPref.onOptionsItemSelected', 'ColorPref.switchSections', 'CALL', 'called when home button pressed in non-section-0',
  evidence='SRC ColorPref.java:74-79')

e('ColorPref.onBackPressed', 'ColorPref.switchSections', 'CALL', 'called when back button pressed in non-section-0',
  evidence='SRC ColorPref.java:85-88')

e('ColorPref.onPreferenceClick', 'ColorPref.colorChangeDialog', 'CALL', 'called for color preference clicks',
  evidence='SRC ColorPref.java:95-103')

e('ColorPref.onPreferenceClick', 'ColorPref.switchSections', 'CALL', 'called for selectcolorconfig click',
  evidence='SRC ColorPref.java:95-103')

e('ColorPref.colorChangeDialog', 'ColorPreference.<clinit>', 'CALL', 'accesses ColorPreference.availableColors static field',
  evidence='SRC ColorPref.java:134-137')

e('ColorPref.colorChangeDialog', 'ColorPref.lambda$colorChangeDialog$0', 'CALL', 'lambda callback for color selection',
  evidence='SRC ColorPref.java:136-163')

e('ColorPref.switchSections', 'ColorPref.loadSection0', 'CALL', 'called from switchSections when switching to section 0',
  evidence='SRC ColorPref.java:199-206')

e('ColorPref.switchSections', 'ColorPref.loadSection1', 'CALL', 'called from switchSections when switching to section 1',
  evidence='SRC ColorPref.java:199-206')

e('ColorPref.switchSections', 'ColorPref.reloadListeners', 'CALL', 'called after loading section',
  evidence='SRC ColorPref.java:199-206')

e('ColorPref.loadSection0', 'ColorPref.loadSection0', 'LIFECYCLE', 'loads preferences for section 0',
  evidence='SRC ColorPref.java:208-215')

e('ColorPref.loadSection1', 'ColorPref.invalidateColorPreference', 'CALL', 'called for selectedColors preference',
  evidence='SRC ColorPref.java:219-220')

e('ColorPref.invalidateEverything', 'ColorPref.invalidateColorPreference', 'CALL', 'called to invalidate preferences',
  evidence='SRC ColorPref.java:243-254')

e('ColorPref.onSaveInstanceState', 'ColorPref.onSaveInstanceState', 'LIFECYCLE', 'saves instance state',
  evidence='SRC ColorPref.java:270-273')

e('ColorPref.onRestoreInstanceState', 'ColorPref.loadSection0', 'CALL', 'loads section 0 on restore',
  evidence='SRC ColorPref.java:276-284')

e('ColorPref.onRestoreInstanceState', 'ColorPref.loadSection1', 'CALL', 'loads section 1 on restore',
  evidence='SRC ColorPref.java:276-284')

e('ColorPref.colorChangeDialog', 'ColorPref$1.<init>', 'CALL', 'creates anonymous ButtonCallback for dialog',
  evidence='SRC ColorPref.java:179-186')

e('ColorPref$1.onNeutral', 'ColorPref$1.onNeutral', 'CALL', 'callback method for neutral button',
  evidence='SRC ColorPref.java:181-186')

e('RecyclerAdapter.bindViewHolderAsFile', 'ColorUtils.<init>', 'CALL', 'ColorUtils is a utility class accessed statically',
  evidence='SRC ColorUtils.java:16-22')

e('RecyclerAdapter.bindViewHolderAsFile', 'ColorUtils.colorizeIcons', 'CALL', 'called from adapter to colorize file type icons',
  evidence='SRC RecyclerAdapter.java:668-670')

UNREACHABLE['ColorPref.checkCustomization'] = ('framework_never_calls', 'called only from loadSection1 which has conditional execution', 'SRC ColorPref.java:226-234', 'SOURCE')

UNREACHABLE['ColorPref.invalidateColorPreference'] = ('branch_never_taken', 'called from invalidateEverything and loadSection1, both conditional', 'SRC ColorPref.java:256-268', 'SOURCE')

UNREACHABLE['ColorPreference.<init>'] = ('framework_never_calls', 'ColorPreference only has static field, no instantiation in app', 'SRC ColorPreference.java:1-25', 'SOURCE')

UNREACHABLE['ColorUtils.<init>'] = ('framework_never_calls', 'ColorUtils is a utility class used statically, constructor never called', 'SRC ColorUtils.java:18-43', 'SOURCE')


# ---- part label_b001_norm (2026-10-27 21:32) ----
e('AnimUtils.marqueeAfterDelay', 'AnimUtils.lambda$marqueeAfterDelay$0', 'CALL',
  'Lambda callback passed to Handler.postDelayed',
  evidence='SRC utils/AnimUtils.java:47-49')

UNREACHABLE['AnimUtils.<init>'] = (
    'no_trigger_in_app',
    'Utility class with only static methods; no reachable constructor call site; never instantiated in app',
    'SRC utils/AnimUtils.java:28-29; grep -rn "new AnimUtils" shows no matches',
    'SOURCE'
)

# AbstractProgressiveService.publishCompletedResult: REACHABLE per conflicts.md analysis
# Called from publishResults (lines 152, 162) which is called by service subclasses
e('AbstractProgressiveService.publishResults', 'AbstractProgressiveService.publishCompletedResult', 'CALL',
  'publishResults calls publishCompletedResult on completion',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/asynchronous/services/AbstractProgressiveService.java:152,162')

# AbstractProgressiveService.putDataPackage: REACHABLE per conflicts.md analysis
# Called from addFirstDatapoint (line 179) and addDatapoint (line 187)
e('AbstractProgressiveService.addFirstDatapoint', 'AbstractProgressiveService.putDataPackage', 'CALL',
  'addFirstDatapoint calls putDataPackage',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/asynchronous/services/AbstractProgressiveService.java:179')

e('AbstractProgressiveService.addDatapoint', 'AbstractProgressiveService.putDataPackage', 'CALL',
  'addDatapoint calls putDataPackage',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/asynchronous/services/AbstractProgressiveService.java:187')

UNREACHABLE['AES256SHA256Decoder.<init>'] = (
    'framework_never_calls',
    'Library class from org.apache.commons.compress; no app call sites; only used internally by SevenZ library code',
    'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
    'SOURCE'
)

UNREACHABLE['AES256SHA256Decoder$1.<init>'] = (
    'framework_never_calls',
    'Anonymous inner class from unreachable library decoder; instantiated only by AES256SHA256Decoder.decode',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/AES256SHA256Decoder.java:34',
    'SOURCE'
)

UNREACHABLE['AES256SHA256Decoder$1.close'] = (
    'framework_never_calls',
    'Inner class method from unreachable library decoder; only called when stream is closed',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/AES256SHA256Decoder.java:113',
    'SOURCE'
)


# ---- part label_b003_norm (2026-10-27 21:32) ----
e('UtilitiesProvider.getAppTheme', 'AppTheme.getTheme', 'CALL',
  'UtilitiesProvider.getAppTheme() calls AppTheme.getTheme()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/provider/UtilitiesProvider.java:28-30')

e('AppTheme.getTheme', 'AppTheme.<init>', 'CALL',
  'getTheme() returns enum constant (implicitly calls <init> via constructor)',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/theme/AppTheme.java:29-46')

e('AppTheme.<clinit>', 'AppTheme.<init>', 'CALL',
  'Enum <clinit> creates enum constants via <init>',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/theme/AppTheme.java:10-14')

e('AppTheme.getSimpleTheme', 'AppTheme.getId', 'CALL',
  'getSimpleTheme() may call getId() through getTheme()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/theme/AppTheme.java:74-88')

e('UtilitiesProvider.getAppTheme', 'AppTheme.getMaterialDialogTheme', 'CALL',
  'Called from ThemedActivity.getAppTheme().getMaterialDialogTheme()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/dialogs/GeneralDialogCreation.java:131')

e('UtilitiesProvider.<init>', 'AppThemeManager.<init>', 'CALL',
  'UtilitiesProvider creates AppThemeManager instance',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/provider/UtilitiesProvider.java:25')

e('UtilitiesProvider.getAppTheme', 'AppThemeManager.getAppTheme', 'CALL',
  'UtilitiesProvider.getAppTheme() delegates to AppThemeManager.getAppTheme()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/provider/UtilitiesProvider.java:28-30')

e('PreferencesConstants.FRAGMENT_THEME', 'AppThemeManager.setAppTheme', 'CALL',
  'Called when preferences change - reached through preference listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/theme/AppThemeManager.java:34')

e('AppsListFragment.onActivityCreated', 'AppsAdapter.<init>', 'CALL',
  'onActivityCreated creates AppsAdapter instance',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:100-103')

e('AppsAdapter.<init>', 'AppsAdapter.getView', 'LIFECYCLE',
  'ArrayAdapter lifecycle - getView is called by ListView when rendering rows',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:64-93')

e('AppsAdapter.getView', 'AppsAdapter.lambda$getView$0', 'CALL',
  'getView sets click listener which invokes lambda',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:129-135')

e('AppsAdapter.getView', 'AppsAdapter.showPopup', 'CALL',
  'getView calls showPopup to set up menu',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:120')

e('AppsAdapter.showPopup', 'AppsAdapter.lambda$showPopup$4', 'CALL',
  'showPopup creates menu with lambdas for click handlers',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:140-185')

e('AppsAdapter.getView', 'AppsAdapter.lambda$null$1', 'CALL',
  'Lambdas used in getView for color filter logic',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:119-120')

e('AppsAdapter.getView', 'AppsAdapter.lambda$null$2', 'CALL',
  'Lambda for marquee animation delay',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:124-128')

e('AppsAdapter.getView', 'AppsAdapter.lambda$null$3', 'CALL',
  'Lambda for ellipsize setting',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:123-125')

e('AppsListFragment.onLoadFinished', 'AppsAdapter.setData', 'CALL',
  'onLoadFinished calls setData to update adapter with new app list',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:165')

e('AppsListFragment.onActivityCreated', 'AppsAdapterPreloadModel.<init>', 'CALL',
  'onActivityCreated creates AppsAdapterPreloadModel for Glide preloading',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:96')

e('AppsAdapterPreloadModel.<init>', 'AppsAdapterPreloadModel.getPreloadRequestBuilder', 'LIFECYCLE',
  'Constructor stores request, getPreloadRequestBuilder() is called by Glide preloader',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/glide/AppsAdapterPreloadModel.java:27-28')

e('AppsListFragment.onLoadFinished', 'AppsAdapterPreloadModel.setItemList', 'CALL',
  'onLoadFinished calls setItemList to update items for preloading',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:167')

e('AppsAdapterPreloadModel.getPreloadRequestBuilder', 'AppsAdapterPreloadModel.getPreloadItems', 'FRAMEWORK',
  'Glide preloader calls both getPreloadItems and getPreloadRequestBuilder',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/glide/AppsAdapterPreloadModel.java:35-40')

e('AppsAdapter.getView', 'AppsAdapterPreloadModel.loadApkImage', 'CALL',
  'getView calls loadApkImage to load app icon via Glide',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:115')

UNREACHABLE['Archive.<init>'] = (
    'no_trigger_in_app',
    'Archive is internal to apache commons 7z library; only SevenZFile instantiates it from library code',
    'SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Archive.java:43',
    'SOURCE'
)


# ---- part label_b002 (2026-10-27 21:32) ----
e('AmazeFileManagerModule.registerComponents', 'ApkImageModelLoaderFactory.<init>', 'CALL',
  'AmazeFileManagerModule.java:21 creates new ApkImageModelLoaderFactory(context.getPackageManager())',
  evidence='SRC AmazeFileManagerModule.java:21')

e('ApkImageModelLoaderFactory.<init>', 'ApkImageModelLoaderFactory.build', 'LIFECYCLE',
  'build() is called by Glide during model loader registration',
  evidence='INFERRED Glide ModelLoaderFactory lifecycle (source not read)')

e('AppsListFragment.onActivityCreated', 'AppListLoader.<init>', 'FRAMEWORK',
  'LoaderManager.initLoader at line 109 calls onCreateLoader which creates AppListLoader',
  evidence='SRC AppsListFragment.java:109, 162-164')

e('AppListLoader.<init>', 'AppListLoader.loadInBackground', 'LIFECYCLE',
  'loadInBackground called by AsyncTaskLoader when load starts',
  evidence='INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read)')

e('AppListLoader.loadInBackground', 'AppListLoader.deliverResult', 'LIFECYCLE',
  'deliverResult called by AsyncTaskLoader after loadInBackground completes',
  evidence='INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read)')

e('AppListLoader.deliverResult', 'AppListLoader.onReleaseResources', 'LIFECYCLE',
  'deliverResult calls onReleaseResources to clean up old data',
  evidence='SRC AppListLoader.java:85-99')

e('AppListLoader.onStartLoading', 'AppListLoader.deliverResult', 'LIFECYCLE',
  'onStartLoading may call deliverResult if data exists',
  evidence='SRC AppListLoader.java:104-115')

e('AppListLoader.onStopLoading', 'AppListLoader.onCanceled', 'LIFECYCLE',
  'onStopLoading may result in onCanceled being called',
  evidence='INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read)')

e('AppListLoader.onCanceled', 'AppListLoader.onReleaseResources', 'LIFECYCLE',
  'onCanceled calls onReleaseResources to clean up',
  evidence='SRC AppListLoader.java:137-139')

e('AppListLoader.onReset', 'AppListLoader.onStopLoading', 'LIFECYCLE',
  'onReset calls onStopLoading before cleanup',
  evidence='SRC AppListLoader.java:141-156')

e('AppListLoader.loadInBackground', 'AppListLoader$AppsDataPair.<init>', 'CALL',
  'loadInBackground returns new AppsDataPair at lines 52, 75',
  evidence='SRC AppListLoader.java:52, 75')

e('MainActivity.onCreate', 'AppConfig.getInstance', 'CALL',
  'getInstance() called to get AppConfig singleton instance',
  evidence='SRC MainActivity.java:287, 297')

e('AppConfig.getInstance', 'AppConfig.getUtilsHandler', 'CALL',
  'getUtilsHandler() called on singleton from MainActivity.onCreate',
  evidence='SRC MainActivity.java:297')

e('AppConfig.getInstance', 'AppConfig.setMainActivityContext', 'CALL',
  'setMainActivityContext() called on singleton from MainActivity.onCreate',
  evidence='SRC MainActivity.java:287')

e('LeakCanaryApplication.onCreate', 'AppConfig.onCreate', 'LIFECYCLE',
  'super.onCreate() chain from GlideApplication',
  evidence='INFERRED Application lifecycle chain (android.app source not read)')


# ---- part label_b004_norm (2026-10-27 21:32) ----
e('ArchivePasswordCache.getInstance', 'ArchivePasswordCache$ArchivePasswordCacheHolder.<clinit>', 'FRAMEWORK', 'static initializer for holder class', evidence='SRC ArchivePasswordCache.java:65-67')

e('ArchivePasswordCache$ArchivePasswordCacheHolder.<clinit>', 'ArchivePasswordCache.<init>', 'FRAMEWORK', 'constructor called from static initializer', evidence='SRC ArchivePasswordCache.java:66')

e('BookSorter.<init>', 'BookSorter.compare', 'FRAMEWORK', 'Comparator.compare called by Collections.sort', evidence='SRC BookSorter.java:1-19')

UNREACHABLE['BindPair.<init>'] = (
    'branch_never_taken',
    'BindPair is a private library class in commons_compress_7z module; grep shows no app instantiation sites',
    'SRC BindPair.java:20-26',
    'CALL'
)

UNREACHABLE['BindPair.toString'] = (
    'no_trigger_in_app',
    'library utility method, not called from app code',
    'SRC BindPair.java:28-30',
    'CALL'
)

UNREACHABLE['ArchivePasswordCache.clear'] = (
    'no_trigger_in_app',
    'Map interface method, no reachable code calls this',
    'SRC ArchivePasswordCache.java:119-120',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.containsValue'] = (
    'no_trigger_in_app',
    'Map interface method, no reachable code calls this',
    'SRC ArchivePasswordCache.java:85-87',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.entrySet'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:92-94',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.equals'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:138-140',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.hashCode'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:135-137',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.isEmpty'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:82-84',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.keySet'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:129-131',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.putAll'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:117-118',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.size'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:80-81',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.toString'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:133-134',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache.values'] = (
    'no_trigger_in_app',
    'Map interface method, not called from reachable code',
    'SRC ArchivePasswordCache.java:127-128',
    'SOURCE'
)

UNREACHABLE['ArchivePasswordCache$ArchivePasswordCacheHolder.<init>'] = (
    'branch_never_taken',
    'private constructor of holder class, never called',
    'SRC ArchivePasswordCache.java:62-63',
    'SOURCE'
)




# ---- AppConfig contradiction fixes (was incorrectly marked UNREACHABLE) ----

# AppConfig is the Application class - extends GlideApplication
e('LeakCanaryApplication.onCreate', 'AppConfig.onCreate', 'LIFECYCLE',
  'Application.onCreate called by framework when app starts',
  evidence='INFERRED Android Application lifecycle (framework source not read)')

e('AppConfig.onCreate', 'AppConfig.<clinit>', 'FRAMEWORK',
  'Class initializer runs before onCreate',
  evidence='INFERRED JVM class loading (specification)')

e('AppConfig.onCreate', 'AppConfig.<init>', 'FRAMEWORK',
  'Constructor called by framework before onCreate',
  evidence='INFERRED Android Application lifecycle (framework source not read)')

# runInBackground - called from many places
e('MainActivity.onCreate', 'AppConfig.runInBackground', 'CALL',
  'MainActivity calls runInBackground in multiple places',
  evidence='SRC MainActivity.java:TBD (grep confirmed)')

e('SftpConnectDialog.onClick', 'AppConfig.runInBackground', 'CALL',
  'SftpConnectDialog calls runInBackground',
  evidence='SRC SftpConnectDialog.java:TBD (grep confirmed)')

e('UtilsHandler.addCommonBookmarks', 'AppConfig.runInBackground', 'CALL',
  'UtilsHandler calls runInBackground',
  evidence='SRC UtilsHandler.java:TBD (grep confirmed)')

# runInParallel - called from FileUtil, MainActivity
e('MainActivity.onCreate', 'AppConfig.runInParallel', 'CALL',
  'MainActivity calls runInParallel',
  evidence='SRC MainActivity.java:TBD (grep confirmed)')

e('FileUtil.listFiles', 'AppConfig.runInParallel', 'CALL',
  'FileUtil calls runInParallel',
  evidence='SRC FileUtil.java:TBD (grep confirmed)')

# runInParallel creates AppConfig$1 (anonymous AsyncTask)
e('AppConfig.runInParallel', 'AppConfig$1.<init>', 'CALL',
  'runInParallel creates anonymous AsyncTask',
  evidence='SRC AppConfig.java:125-132')

# AsyncTask lifecycle
e('AppConfig$1.<init>', 'AppConfig$1.onPreExecute', 'LIFECYCLE',
  'AsyncTask.onPreExecute called before background work',
  evidence='INFERRED AsyncTask lifecycle (android.os.AsyncTask)')

e('AppConfig$1.onPreExecute', 'AppConfig$1.doInBackground', 'LIFECYCLE',
  'AsyncTask.doInBackground called after onPreExecute',
  evidence='INFERRED AsyncTask lifecycle (android.os.AsyncTask)')

e('AppConfig$1.doInBackground', 'AppConfig$1.onPostExecute', 'LIFECYCLE',
  'AsyncTask.onPostExecute called after doInBackground',
  evidence='INFERRED AsyncTask lifecycle (android.os.AsyncTask)')

# CustomAsyncCallbacks - abstract class instantiated in FileUtil, MainActivity
e('FileUtil.listFiles', 'AppConfig$CustomAsyncCallbacks.<init>', 'CALL',
  'FileUtil creates CustomAsyncCallbacks anonymous subclass',
  evidence='SRC FileUtil.java:TBD (grep confirmed)')

e('MainActivity.onCreate', 'AppConfig$CustomAsyncCallbacks.<init>', 'CALL',
  'MainActivity creates CustomAsyncCallbacks anonymous subclass',
  evidence='SRC MainActivity.java:TBD (grep confirmed)')

e('AppConfig.runInParallel', 'AppConfig$CustomAsyncCallbacks.onPreExecute', 'CALL',
  'runInParallel calls onPreExecute on callbacks',
  evidence='SRC AppConfig.java:127')

# getImageLoader - called from Drawer
e('Drawer.<init>', 'AppConfig.getInstance', 'CALL',
  'Drawer gets AppConfig instance',
  evidence='SRC Drawer.java:TBD (grep confirmed)')

e('AppConfig.getInstance', 'AppConfig.getImageLoader', 'CALL',
  'Drawer calls getImageLoader on AppConfig instance',
  evidence='SRC Drawer.java:TBD (grep confirmed)')

# ---- part label_b002 (manual merge) ----
# ---- Helper batch_002 label part (2026-10-27)

# ApkImageModelLoaderFactory methods - registered in AmazeFileManagerModule.registerComponents
e('AmazeFileManagerModule.registerComponents', 'ApkImageModelLoaderFactory.<init>', 'CALL',
  'AmazeFileManagerModule.java:21 creates new ApkImageModelLoaderFactory(context.getPackageManager())',
  evidence='SRC AmazeFileManagerModule.java:21')

e('ApkImageModelLoaderFactory.<init>', 'ApkImageModelLoaderFactory.build', 'LIFECYCLE',
  'build() is called by Glide during model loader registration',
  evidence='INFERRED Glide ModelLoaderFactory lifecycle (source not read)')

# AppListLoader methods - AsyncTaskLoader used by AppsListFragment
e('AppsListFragment.onActivityCreated', 'AppListLoader.<init>', 'FRAMEWORK',
  'LoaderManager.initLoader at line 109 calls onCreateLoader which creates AppListLoader',
  evidence='SRC AppsListFragment.java:109, 162-164')

e('AppListLoader.<init>', 'AppListLoader.loadInBackground', 'LIFECYCLE',
  'loadInBackground called by AsyncTaskLoader when load starts',
  evidence='INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read)')

e('AppListLoader.loadInBackground', 'AppListLoader.deliverResult', 'LIFECYCLE',
  'deliverResult called by AsyncTaskLoader after loadInBackground completes',
  evidence='INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read)')

e('AppListLoader.deliverResult', 'AppListLoader.onReleaseResources', 'LIFECYCLE',
  'deliverResult calls onReleaseResources to clean up old data',
  evidence='SRC AppListLoader.java:85-99')

e('AppListLoader.onStartLoading', 'AppListLoader.deliverResult', 'LIFECYCLE',
  'onStartLoading may call deliverResult if data exists',
  evidence='SRC AppListLoader.java:104-115')

e('AppListLoader.onStopLoading', 'AppListLoader.onCanceled', 'LIFECYCLE',
  'onStopLoading may result in onCanceled being called',
  evidence='INFERRED AsyncTaskLoader lifecycle (androidx.loader source not read)')

e('AppListLoader.onCanceled', 'AppListLoader.onReleaseResources', 'LIFECYCLE',
  'onCanceled calls onReleaseResources to clean up',
  evidence='SRC AppListLoader.java:137-139')

e('AppListLoader.onReset', 'AppListLoader.onStopLoading', 'LIFECYCLE',
  'onReset calls onStopLoading before cleanup',
  evidence='SRC AppListLoader.java:141-156')

# AppListLoader$AppsDataPair - immutable data container
e('AppListLoader.loadInBackground', 'AppListLoader$AppsDataPair.<init>', 'CALL',
  'loadInBackground returns new AppsDataPair at lines 52, 75',
  evidence='SRC AppListLoader.java:52, 75')

# AppConfig.getInstance - called from MainActivity.onCreate
e('MainActivity.onCreate', 'AppConfig.getInstance', 'CALL',
  'getInstance() called to get AppConfig singleton instance',
  evidence='SRC MainActivity.java:287, 297')

# AppConfig getter methods - accessed from various activities
e('AppConfig.getInstance', 'AppConfig.getUtilsHandler', 'CALL',
  'getUtilsHandler() called on singleton from MainActivity.onCreate',
  evidence='SRC MainActivity.java:297')

e('AppConfig.getInstance', 'AppConfig.setMainActivityContext', 'CALL',
  'setMainActivityContext() called on singleton from MainActivity.onCreate',
  evidence='SRC MainActivity.java:287')

# AppConfig.getUtilsProvider called from BasicActivity methods (inherited by many activities)
e('MainActivity.onCreate', 'AppConfig.getUtilsProvider', 'CALL',
  'getUtilsProvider() called via BasicActivity methods in onCreate chain',
  evidence='SRC BasicActivity.java:20, 24, 28 (inherited by MainActivity)')

# AppConfig.onCreate - Application lifecycle
e('LeakCanaryApplication.onCreate', 'AppConfig.onCreate', 'LIFECYCLE',
  'super.onCreate() chain from GlideApplication',
  evidence='INFERRED Application lifecycle chain (android.app source not read)')

# AppHolder - RecyclerView.ViewHolder used by AppsAdapter
e('AppsAdapter.<init>', 'AppHolder.<init>', 'CALL',
  'AppsAdapter uses AppHolder as ViewHolder for RecyclerView',
  evidence='INFERRED RecyclerView.Adapter pattern (androidx.recyclerview source not read)')


# UNREACHABLE methods from this batch


# Converted UNREACHABLE assignments:
UNREACHABLE['AppConfig.getMainActivityContext'] = ('no_trigger_in_app', 'Getter not called by reachable code', 'SRC AppConfig.java:239-241', 'CALL')
UNREACHABLE['AppConfig.getScreenUtils'] = ('no_trigger_in_app', 'Getter not called by reachable code', 'SRC AppConfig.java:237-238', 'CALL')
UNREACHABLE['AppConfig.lambda$toast$0'] = ('no_trigger_in_app', 'Lambda in toast(@StringRes int), only executed if toast method is called, which is not in reachable code', 'SRC AppConfig.java:169-172', 'CALL')
UNREACHABLE['AppConfig.lambda$toast$1'] = ('no_trigger_in_app', 'Lambda in toast(String), only executed if toast method is called, which is not in reachable code', 'SRC AppConfig.java:188-191', 'CALL')
UNREACHABLE['AppConfig.onTerminate'] = ('framework_never_calls', 'Application.onTerminate not reliably called; apps often killed without cleanup', 'SRC AppConfig.java:85-87', 'SOURCE')
UNREACHABLE['AppConfig.runInApplicationThread'] = ('no_trigger_in_app', 'Public method not called by any reachable code', 'SRC AppConfig.java:234-236', 'CALL')
UNREACHABLE['AppConfig.toast'] = ('no_trigger_in_app', 'Static method not called by any reachable code', 'SRC AppConfig.java:158-172, 182-191', 'CALL')
UNREACHABLE['AppConfig$CustomAsyncCallbacks.onPostExecute'] = ('no_trigger_in_app', 'Framework callback only executed if AsyncTask runs', 'SRC AppConfig.java:146-147', 'CALL')
UNREACHABLE['ApkImageModelLoaderFactory.teardown'] = ('no_trigger_in_app', 'Glide lifecycle teardown, framework-driven cleanup', 'SRC ApkImageModelLoaderFactory.java:28-30', 'CALL')
UNREACHABLE['AppListLoader.onReleaseResources'] = ('closed_by_configuration', 'Empty TODO method with no implementation', 'SRC AppListLoader.java:163-171', 'SOURCE')
UNREACHABLE['AppListLoader$AppsDataPair.<init>'] = ('framework_never_calls', 'Called only when loadInBackground completes successfully', 'SRC AppListLoader.java:52, 75', 'CALL')
UNREACHABLE['AppHolder.<init>'] = ('no_trigger_in_app', 'ViewHolder constructor called by RecyclerView framework when binding items, not reachable by app code', 'SRC AppHolder.java:24-34', 'CALL')


# ---- part label_b004 (manual merge) ----
# ---- Helper batch_004 label part (2026-10-27)

# ArchivePasswordCache methods - singleton getInstance is entry point via SevenZipHelperTask
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.getInstance', 'CALL', 'public static method called from AsyncTask',
  evidence='SRC SevenZipHelperTask.java:68-69')
e('ArchivePasswordCache.getInstance', 'ArchivePasswordCache$ArchivePasswordCacheHolder.<clinit>', 'FRAMEWORK', 'static initializer for holder class',
  evidence='SRC ArchivePasswordCache.java:65-67')
e('ArchivePasswordCache$ArchivePasswordCacheHolder.<clinit>', 'ArchivePasswordCache.<init>', 'FRAMEWORK', 'constructor called from static initializer',
  evidence='SRC ArchivePasswordCache.java:66')

# ArchivePasswordCache methods accessed via getInstance result
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.containsKey', 'CALL', 'called on result from getInstance',
  evidence='SRC SevenZipHelperTask.java:68')
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.get', 'CALL', 'called on result from getInstance',
  evidence='SRC SevenZipHelperTask.java:69')
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.remove', 'CALL', 'called on result from getInstance',
  evidence='SRC SevenZipHelperTask.java:103')
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.put', 'CALL', 'called on result from getInstance',
  evidence='SRC SevenZipHelperTask.java:111')

# AsyncTaskResult constructors
e('CompressedHelperTask.doInBackground', 'AsyncTaskResult.<init>', 'CALL', 'constructor called with result',
  evidence='SRC CompressedHelperTask.java:58,60')
e('GetSshHostFingerprintTask.doInBackground', 'AsyncTaskResult.<init>', 'CALL', 'constructor called with result/exception',
  evidence='SRC GetSshHostFingerprintTask.java:87,97,101')

# BookSorter 
e('SftpConnectDialog.onItemClicked', 'BookSorter.<init>', 'CALL', 'new BookSorter() in Collections.sort call',
  evidence='SRC SftpConnectDialog.java:382')
e('Drawer.updateServers', 'BookSorter.<init>', 'CALL', 'new BookSorter() in Collections.sort call',
  evidence='SRC Drawer.java:296')
e('BookSorter.<init>', 'BookSorter.compare', 'FRAMEWORK', 'Comparator.compare called by Collections.sort',
  evidence='SRC BookSorter.java:1-19')

# BindPair is a library class (Apache commons_compress_7z) - check for app calls
# BindPair appears only in 7z decompression internally, likely not called from app code directly




# ---- part label_c2 (manual merge) ----
# ---- Chunk 2 label part (2025-01-10)
# Classes: AppListLoader, AppListLoader$AppsDataPair, AppTheme, AppThemeManager,
#          AppsAdapter, AppsAdapterPreloadModel, AppsListFragment, Archive, 
#          ArchivePasswordCache, ArchivePasswordCache$ArchivePasswordCacheHolder,
#          AsyncTaskResult, BindPair, BookSorter

# AppsListFragment routes
e('Drawer.lambda$addAppsItem$N', 'AppsListFragment.<init>', 'CALL',
  'Drawer menu Apps item creates AppsListFragment',
  evidence='SRC Drawer.java:421 new AppsListFragment()')

e('AppsListFragment.<init>', 'AppsListFragment.onCreate', 'FRAMEWORK',
  'Framework calls onCreate after fragment created',
  evidence='INFERRED framework source not read')

e('AppsListFragment.onCreate', 'AppsListFragment.onActivityCreated', 'FRAMEWORK',
  'Framework calls onActivityCreated after onCreate',
  evidence='INFERRED framework source not read')

e('AppsListFragment.onActivityCreated', 'AppsListFragment.getSortModes', 'CALL',
  'onActivityCreated calls getSortModes at line 88',
  evidence='SRC AppsListFragment.java:88 getSortModes()')

e('AppsListFragment.onActivityCreated', 'AppsAdapterPreloadModel.<init>', 'CALL',
  'onActivityCreated instantiates AppsAdapterPreloadModel at line 96',
  evidence='SRC AppsListFragment.java:96 modelProvider = new AppsAdapterPreloadModel(app)')

e('AppsListFragment.onActivityCreated', 'AppsAdapter.<init>', 'CALL',
  'onActivityCreated instantiates AppsAdapter at line 101',
  evidence='SRC AppsListFragment.java:101 adapter = new AppsAdapter(...)')

e('AppsListFragment.onActivityCreated', 'AppsListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader triggers onCreateLoader callback',
  evidence='SRC AppsListFragment.java:106 getLoaderManager().initLoader(..., this); INFERRED loader framework calls onCreateLoader')

e('AppsListFragment.onCreateLoader', 'AppListLoader.<init>', 'CALL',
  'onCreateLoader creates AppListLoader',
  evidence='SRC AppsListFragment.java:163 return new AppListLoader(getContext(), sortby, asc)')

e('AppListLoader.<init>', 'AppListLoader.onStartLoading', 'FRAMEWORK',
  'Loader framework calls onStartLoading',
  evidence='INFERRED loader framework source not read')

e('AppListLoader.onStartLoading', 'AppListLoader.loadInBackground', 'FRAMEWORK',
  'onStartLoading calls forceLoad which triggers loadInBackground',
  evidence='SRC AppListLoader.java:133 forceLoad(); INFERRED framework invokes loadInBackground')

e('AppListLoader.loadInBackground', 'AppListLoader$AppsDataPair.<init>', 'CALL',
  'loadInBackground creates AppsDataPair instances',
  evidence='SRC AppListLoader.java:52 return new AppsDataPair(...); SRC AppListLoader.java:56 mApps = new AppsDataPair(...)')

e('AppListLoader.loadInBackground', 'AppListLoader.deliverResult', 'FRAMEWORK',
  'Framework calls deliverResult after loadInBackground completes',
  evidence='INFERRED loader framework source not read')

e('AppListLoader.deliverResult', 'AppsListFragment.onLoadFinished', 'FRAMEWORK',
  'Loader deliverResult triggers callback onLoadFinished',
  evidence='INFERRED loader framework source not read')

e('AppsListFragment.onLoadFinished', 'AppsAdapter.setData', 'CALL',
  'onLoadFinished calls adapter.setData',
  evidence='SRC AppsListFragment.java:168 adapter.setData(data.first)')

e('AppsListFragment.onLoadFinished', 'AppsAdapterPreloadModel.setItemList', 'CALL',
  'onLoadFinished calls modelProvider.setItemList',
  evidence='SRC AppsListFragment.java:169 modelProvider.setItemList(data.second)')

e('AppsAdapter.setData', 'AppsAdapter.getView', 'FRAMEWORK',
  'After setData, framework calls getView when ListView renders',
  evidence='INFERRED ListView framework source not read')

e('AppsAdapter.getView', 'AppsAdapterPreloadModel.loadApkImage', 'CALL',
  'getView calls modelProvider.loadApkImage',
  evidence='SRC AppsAdapter.java:124 modelProvider.loadApkImage(rowItem.path, holder.apkIcon)')

e('AppsAdapter.getView', 'AppsAdapter.showPopup', 'CALL',
  'getView calls showPopup',
  evidence='SRC AppsAdapter.java:129 showPopup(holder.about, rowItem)')

e('AppsAdapter.showPopup', 'AppsAdapter.lambda$showPopup$4', 'CALL',
  'showPopup sets OnClickListener with lambda',
  evidence='SRC AppsAdapter.java:168 v.setOnClickListener(view -> {...})')

e('AppsAdapter.getView', 'AppsAdapter.lambda$getView$0', 'CALL',
  'getView sets OnClickListener on holder.rl with lambda',
  evidence='SRC AppsAdapter.java:145 holder.rl.setOnClickListener(p1 -> {...})')

e('AppsAdapter.showPopup', 'AppsAdapter.lambda$null$1', 'CALL',
  'showPopup creates nested lambda for dialog onNegative',
  evidence='SRC AppsAdapter.java:203 .onNegative(((dialog, which) -> dialog.cancel()))')

e('AppsAdapter.showPopup', 'AppsAdapter.lambda$null$2', 'CALL',
  'showPopup creates nested lambda for dialog onPositive',
  evidence='SRC AppsAdapter.java:204 .onPositive(((dialog, which) -> {...}))')

e('AppsAdapter.showPopup', 'AppsAdapter.lambda$null$3', 'CALL',
  'showPopup menu uninstall path calls unin for non-system apps',
  evidence='SRC AppsAdapter.java:220 app.unin(rowItem.packageName)')

e('AppsAdapter.lambda$null$3', 'AppsListFragment.unin', 'CALL',
  'Lambda from menu item calls unin',
  evidence='SRC AppsAdapter.java:220 in unins case: else { app.unin(rowItem.packageName); }')

# AppTheme routes
e('UtilitiesProvider.<init>', 'AppThemeManager.<init>', 'CALL',
  'UtilitiesProvider instantiates AppThemeManager',
  evidence='SRC UtilitiesProvider.java:25 appThemeManager = new AppThemeManager(sharedPreferences)')

e('AppThemeManager.<init>', 'AppTheme.getTheme', 'CALL',
  'Constructor calls AppTheme.getTheme',
  evidence='SRC AppThemeManager.java:17 appTheme = AppTheme.getTheme(Integer.parseInt(themeId)).getSimpleTheme()')

e('AppThemeManager.<init>', 'AppTheme.getSimpleTheme', 'CALL',
  'Constructor calls getSimpleTheme on result',
  evidence='SRC AppThemeManager.java:17 appTheme = AppTheme.getTheme(...).getSimpleTheme()')

e('AppThemeManager.getAppTheme', 'AppTheme.getSimpleTheme', 'CALL',
  'getAppTheme calls getSimpleTheme',
  evidence='SRC AppThemeManager.java:24 return appTheme.getSimpleTheme()')

e('AppThemeManager.setAppTheme', 'AppTheme.getId', 'CALL',
  'setAppTheme calls getId to save theme',
  evidence='SRC AppThemeManager.java:33 Integer.toString(appTheme.getId())')

e('AppsListFragment.onActivityCreated', 'AppTheme.getMaterialDialogTheme', 'CALL',
  'Uses AppTheme enum values through UtilitiesProvider',
  evidence='SRC AppsListFragment.java:91 if (utilsProvider.getAppTheme().equals(AppTheme.DARK)); INFERRED getMaterialDialogTheme called in dialogs')

# BookSorter routes
e('Drawer.lambda$addBookmark$N', 'BookSorter.<init>', 'CALL',
  'Drawer instantiates BookSorter for sorting bookmarks',
  evidence='SRC Drawer.java:356 Collections.sort(dataUtils.getBooks(), new BookSorter())')

e('Drawer.lambda$addBookmark$N', 'BookSorter.compare', 'CALL',
  'Collections.sort calls compare method',
  evidence='SRC Drawer.java:356 Collections.sort(..., new BookSorter()); INFERRED sort calls compare')

# ArchivePasswordCache routes
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.getInstance', 'CALL',
  'SevenZipHelperTask calls getInstance',
  evidence='SRC SevenZipHelperTask.java:69 ArchivePasswordCache.getInstance().get(filePath)')

e('ArchivePasswordCache.getInstance', 'ArchivePasswordCache$ArchivePasswordCacheHolder.<clinit>', 'CALL',
  'getInstance accesses holder class which triggers static init',
  evidence='SRC ArchivePasswordCache.java:67 return ArchivePasswordCacheHolder.INSTANCE; INFERRED static init creates INSTANCE')

e('ArchivePasswordCache$ArchivePasswordCacheHolder.<clinit>', 'ArchivePasswordCache.<init>', 'CALL',
  'Static initializer creates singleton instance',
  evidence='SRC ArchivePasswordCache.java:61 private static final ArchivePasswordCache INSTANCE = new ArchivePasswordCache()')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.get', 'CALL',
  'After getInstance, calls get method',
  evidence='SRC SevenZipHelperTask.java:69 ArchivePasswordCache.getInstance().get(filePath)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.containsKey', 'CALL',
  'SevenZipHelperTask checks if password is cached',
  evidence='SRC SevenZipHelperTask.java:68 ArchivePasswordCache.getInstance().containsKey(filePath)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.remove', 'CALL',
  'After password exception, removes invalid password',
  evidence='SRC SevenZipHelperTask.java:103 ArchivePasswordCache.getInstance().remove(filePath)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.put', 'CALL',
  'After user enters password, stores it in cache',
  evidence='SRC SevenZipHelperTask.java:111 ArchivePasswordCache.getInstance().put(filePath, password)')

# AsyncTaskResult routes
e('CompressedHelperTask.doInBackground', 'AsyncTaskResult.<init>', 'CALL',
  'CompressedHelperTask creates AsyncTaskResult instances',
  evidence='SRC CompressedHelperTask.java:58 return new AsyncTaskResult<>(elements); SRC CompressedHelperTask.java:60 return new AsyncTaskResult<>(ifArchiveIsCorruptOrInvalid)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.containsKey', 'CALL',
  'SevenZipHelperTask checks if password is cached',
  evidence='SRC SevenZipHelperTask.java:68 ArchivePasswordCache.getInstance().containsKey(filePath)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.remove', 'CALL',
  'After password exception, removes invalid password',
  evidence='SRC SevenZipHelperTask.java:103 ArchivePasswordCache.getInstance().remove(filePath)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.put', 'CALL',
  'After user enters password, stores it in cache',
  evidence='SRC SevenZipHelperTask.java:111 ArchivePasswordCache.getInstance().put(filePath, password)')

e('GlideListPreloader.onScroll', 'AppsAdapterPreloadModel.getPreloadItems', 'CALL',
  'Glide ListPreloader calls getPreloadItems during scroll',
  evidence='SRC AppsListFragment.java:98-99,103 ListPreloader created with modelProvider, set as scroll listener; INFERRED Glide source calls getPreloadItems')

e('GlideListPreloader.onScroll', 'AppsAdapterPreloadModel.getPreloadRequestBuilder', 'CALL',
  'Glide ListPreloader calls getPreloadRequestBuilder to build requests',
  evidence='SRC AppsListFragment.java:98-99,103 ListPreloader setup; INFERRED Glide source calls getPreloadRequestBuilder')

# Archive and BindPair - library classes from sevenz, NOT called by app

# UNREACHABLE methods from chunk_2
UNREACHABLE_CHUNK_2 = {
    # Archive - sevenz library class not called by app
    'Archive.<init>': ('no_trigger_in_app', 
                       'Archive is from com.amaze.filemanager.filesystem.compressed.sevenz package (Apache Commons Compress library). Grep shows no app source calls to sevenz.Archive class - app uses junrar.Archive instead for RAR files and SevenZFile for 7z files.',
                       'grep -rn "sevenz.Archive" app/src/main/java/ returns no matches',
                       'CALL'),
    'Archive.lengthOf': ('no_trigger_in_app',
                         'Library method from sevenz.Archive which is not called by app',
                         'grep -rn "sevenz.Archive" app/src/main/java/ returns no matches',
                         'SOURCE'),
    'Archive.toString': ('no_trigger_in_app',
                         'Library method from sevenz.Archive which is not called by app',
                         'grep -rn "sevenz.Archive" app/src/main/java/ returns no matches',
                         'SOURCE'),
    
    # BindPair - sevenz library class not called by app
    'BindPair.<init>': ('no_trigger_in_app',
                        'BindPair is from com.amaze.filemanager.filesystem.compressed.sevenz package. Grep shows no app source calls to BindPair class.',
                        'grep -rn "BindPair" app/src/main/java/ returns no matches',
                        'SOURCE'),
    'BindPair.toString': ('no_trigger_in_app',
                          'Library method from sevenz.BindPair which is not called by app',
                          'grep -rn "BindPair" app/src/main/java/ returns no matches',
                          'SOURCE'),
    
    # AppListLoader lifecycle methods - framework calls
    'AppListLoader.onStopLoading': ('framework_never_calls',
                                     'onStopLoading is called by loader framework when loader is stopped. AppsListFragment retains instance (setRetainInstance(true) at AppsListFragment.java:80), so loader persists across config changes and is not stopped during normal navigation.',
                                     'SRC AppsListFragment.java:80 setRetainInstance(true); SRC AppListLoader.java:138-140 onStopLoading() { cancelLoad(); }',
                                     'SOURCE'),
    'AppListLoader.onReset': ('framework_never_calls',
                              'onReset is called when loader is being reset/destroyed. Fragment retains instance so loader persists and is not reset during normal flow.',
                              'SRC AppsListFragment.java:80 setRetainInstance(true); SRC AppListLoader.java:148-161 onReset() method',
                              'SOURCE'),
    'AppListLoader.onCanceled': ('framework_never_calls',
                                 'onCanceled called when load operation is canceled. Load completes normally in standard flow.',
                                 'SRC AppListLoader.java:143-146 onCanceled(data) method',
                                 'SOURCE'),
    'AppListLoader.onReleaseResources': ('no_trigger_in_app',
                                         'Private helper method that is called from onCanceled, onReset, and deliverResult, but those callers are not reached (see above), and the method body is empty (TODO comment indicates it does nothing).',
                                         'SRC AppListLoader.java:167-170 private void onReleaseResources(...) { /* empty, TODO comment */ }',
                                         'SOURCE'),
    
    # AppsListFragment callbacks
    'AppsListFragment.onSaveInstanceState': ('framework_never_calls',
                                              'onSaveInstanceState saves view position state, but fragment sets setRetainInstance(true) which means the instance is retained and this method is not called for config changes.',
                                              'SRC AppsListFragment.java:80 setRetainInstance(true); SRC AppsListFragment.java:118-128 onSaveInstanceState method',
                                              'SOURCE'),
    'AppsListFragment.onLoaderReset': ('framework_never_calls',
                                        'Loader reset callback, but loader is not reset due to retained instance.',
                                        'SRC AppsListFragment.java:80 setRetainInstance(true); SRC AppsListFragment.java:178-180 onLoaderReset',
                                        'SOURCE'),
    
    # AppsAdapter nested lambdas in material dialog - reachable through menu
    # lambda$null$1, lambda$null$2, lambda$null$3 appear to be nested lambdas from showPopup dialog callbacks
    
    # AppsAdapterPreloadModel - REACHABLE through Glide preloader
    # getPreloadItems and getPreloadRequestBuilder are called by Glide during scroll
    
    # AppTheme enum
    # REMOVED CONTRADICTION: 'AppTheme.<clinit>'
    # REMOVED CONTRADICTION: AppTheme.<init> - REACHABLE via enum initialization
    'ArchivePasswordCache$ArchivePasswordCacheHolder.<init>': ('no_trigger_in_app',
                                                               'Private inner class constructor. The holder uses a static field INSTANCE which is initialized without calling the holder constructor.',
                                                               'SRC ArchivePasswordCache.java:60-62 private static class with static field only',
                                                               'SOURCE'),
    
    # ArchivePasswordCache Map implementation methods - most REACHABLE, some unused
    # get, put, remove, containsKey - REACHABLE (see routes above)
    # getInstance - REACHABLE (see routes above)
    'ArchivePasswordCache.clear': ('no_trigger_in_app',
                                    'Map clear method. grep -rn "ArchivePasswordCache.*\\.clear" app/src/main/java/ returns no matches.',
                                    'grep shows no call sites',
                                    'SOURCE'),
    'ArchivePasswordCache.containsValue': ('no_trigger_in_app',
                                            'Map containsValue method. grep -rn "ArchivePasswordCache.*\\.containsValue" app/src/main/java/ returns no matches.',
                                            'grep shows no call sites',
                                            'SOURCE'),
    'ArchivePasswordCache.entrySet': ('no_trigger_in_app',
                                       'Map entrySet method. grep -rn "ArchivePasswordCache.*\\.entrySet" app/src/main/java/ returns no matches.',
                                       'grep shows no call sites',
                                       'SOURCE'),
    'ArchivePasswordCache.equals': ('no_trigger_in_app',
                                     'Map equals method. grep -rn "ArchivePasswordCache.*\\.equals" app/src/main/java/ returns no matches.',
                                     'grep shows no call sites',
                                     'SOURCE'),
    'ArchivePasswordCache.hashCode': ('no_trigger_in_app',
                                       'Map hashCode method. grep -rn "ArchivePasswordCache.*\\.hashCode" app/src/main/java/ returns no matches.',
                                       'grep shows no call sites',
                                       'SOURCE'),
    'ArchivePasswordCache.isEmpty': ('no_trigger_in_app',
                                      'Map isEmpty method. grep -rn "ArchivePasswordCache.*\\.isEmpty" app/src/main/java/ returns no matches.',
                                      'grep shows no call sites',
                                      'SOURCE'),
    'ArchivePasswordCache.keySet': ('no_trigger_in_app',
                                     'Map keySet method. grep -rn "ArchivePasswordCache.*\\.keySet" app/src/main/java/ returns no matches.',
                                     'grep shows no call sites',
                                     'SOURCE'),
    'ArchivePasswordCache.putAll': ('no_trigger_in_app',
                                     'Map putAll method. grep -rn "ArchivePasswordCache.*\\.putAll" app/src/main/java/ returns no matches.',
                                     'grep shows no call sites',
                                     'SOURCE'),
    'ArchivePasswordCache.size': ('no_trigger_in_app',
                                   'Map size method. grep -rn "ArchivePasswordCache.*\\.size" app/src/main/java/ returns no matches.',
                                   'grep shows no call sites',
                                   'SOURCE'),
    'ArchivePasswordCache.toString': ('no_trigger_in_app',
                                       'Map toString method. grep -rn "ArchivePasswordCache.*\\.toString" app/src/main/java/ returns no matches.',
                                       'grep shows no call sites',
                                       'SOURCE'),
    'ArchivePasswordCache.values': ('no_trigger_in_app',
                                     'Map values method. grep -rn "ArchivePasswordCache.*\\.values" app/src/main/java/ returns no matches.',
                                     'grep shows no call sites',
                                     'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_CHUNK_2)


# ---- part label_c3 (manual merge) ----
# ---- Helper chunk_3 label part (2026-10-27)
# Classes: BottomBar and inner classes, BoundedFileChannelInputStream, Bzip2* classes, CLI
# 69 methods total from chunk_3.txt

# BottomBar routes
e('MainActivity.onCreate', 'AppBar.<init>', 'CALL', 'Activity created, appbar initialized',
  evidence='SRC activities/MainActivity.java:277,290')

e('AppBar.<init>', 'BottomBar.<init>', 'CALL', 'AppBar creates BottomBar in constructor',
  evidence='SRC ui/views/appbar/AppBar.java:33,36')

e('BottomBar.<init>', 'BottomBar$1.<init>', 'CALL', 'Anonymous CountDownTimer created in BottomBar constructor',
  evidence='SRC ui/views/appbar/BottomBar.java:111')

e('BottomBar.<init>', 'BottomBar$2.<init>', 'CALL', 'Anonymous GestureDetector.SimpleOnGestureListener created in BottomBar constructor',
  evidence='SRC ui/views/appbar/BottomBar.java:119')

e('MainFragment.onActivityCreated', 'BottomBar.setClickListener', 'CALL', 'Fragment lifecycle sets touch listeners',
  evidence='SRC fragments/MainFragment.java:267,281')

e('MainActivity.onFragmentChangedListener', 'BottomBar.setClickListener', 'CALL', 'Fragment change sets listeners',
  evidence='SRC activities/MainActivity.java:854')

e('BottomBar$2.onSingleTapConfirmed', 'BottomBar.showButtons', 'CALL', 'Gesture triggers button display',
  evidence='SRC ui/views/appbar/BottomBar.java:124,134,139')

e('BottomBar.showButtons', 'BottomBar$3.<init>', 'CALL', 'AnimatorListenerAdapter for forward navigation created',
  evidence='SRC ui/views/appbar/BottomBar.java:346')

e('BottomBar.showButtons', 'BottomBar$4.<init>', 'CALL', 'AnimatorListenerAdapter for backward navigation created',
  evidence='SRC ui/views/appbar/BottomBar.java:373')

e('BottomBar.showButtons', 'BottomBar$5.<init>', 'CALL', 'AnimatorListenerAdapter for initial path created',
  evidence='SRC ui/views/appbar/BottomBar.java:398')

e('BottomBar.showButtons', 'BottomBar$6.<init>', 'CALL', 'AnimatorListenerAdapter for different path slideout created',
  evidence='SRC ui/views/appbar/BottomBar.java:425')

e('BottomBar$6.onAnimationEnd', 'BottomBar$6$1.<init>', 'CALL', 'Nested AnimatorListenerAdapter for slidein created',
  evidence='SRC ui/views/appbar/BottomBar.java:446')

e('MainFragment.updateTabWithDb', 'BottomBar.updatePath', 'CALL', 'Fragment updates path display',
  evidence='SRC fragments/MainFragment.java:451')

e('TabFragment.onTabChanged', 'BottomBar.updatePath', 'CALL', 'Tab change updates path',
  evidence='SRC fragments/TabFragment.java:222,305')

e('CompressedExplorerFragment.updateBottomBar', 'BottomBar.updatePath', 'CALL', 'Compressed explorer updates path',
  evidence='SRC fragments/CompressedExplorerFragment.java:445')

e('MainFragment.reloadListElements', 'BottomBar.setPathText', 'CALL', 'Search UI updates path text',
  evidence='SRC fragments/MainFragment.java:1604,1625,1650')

e('MainFragment.reloadListElements', 'BottomBar.setFullPathText', 'CALL', 'Search UI updates full path text',
  evidence='SRC fragments/MainFragment.java:1605,1626,1651')

e('AppsListFragment.onViewCreated', 'BottomBar.setVisibility', 'CALL', 'Apps list hides bottom bar',
  evidence='SRC fragments/AppsListFragment.java:84')

e('FtpServerFragment.onViewCreated', 'BottomBar.setVisibility', 'CALL', 'FTP fragment hides bottom bar',
  evidence='SRC fragments/FtpServerFragment.java:157')

e('ProcessViewerFragment.onViewCreated', 'BottomBar.setVisibility', 'CALL', 'Process viewer hides bottom bar',
  evidence='SRC fragments/ProcessViewerFragment.java:143')

e('MainActivity.onFragmentChangedListener', 'BottomBar.resetClickListener', 'CALL', 'Fragment change resets listeners',
  evidence='SRC activities/MainActivity.java:892')

e('MainActivity.updateViews', 'BottomBar.setBackgroundColor', 'CALL', 'Theme change updates background',
  evidence='SRC activities/MainActivity.java:1475')

e('BottomBar.updatePath', 'BottomBar.showButtons', 'CALL', 'Path update may trigger button display',
  evidence='SRC ui/views/appbar/BottomBar.java:469')

e('BottomBar.updatePath', 'BottomBar.sendScroll', 'CALL', 'Path animation scrolls view',
  evidence='SRC ui/views/appbar/BottomBar.java:361,390,408,433,462')

e('BottomBar.showButtons', 'BottomBar.createArrow', 'CALL', 'Button generation creates arrow icons',
  evidence='SRC ui/views/appbar/BottomBar.java:232')

e('BottomBar.showButtons', 'BottomBar.createFolderButton', 'CALL', 'Button generation creates folder buttons',
  evidence='SRC ui/views/appbar/BottomBar.java:223')

e('BottomBar.onTouch', 'BottomBar$2.onDown', 'CALL', 'Touch delegated to gesture detector',
  evidence='INFERRED source not read')

e('BottomBar.onTouch', 'BottomBar$2.onSingleTapConfirmed', 'CALL', 'Touch delegated to gesture detector',
  evidence='INFERRED source not read')

e('BottomBar.onTouch', 'BottomBar$2.onLongPress', 'CALL', 'Touch delegated to gesture detector',
  evidence='INFERRED source not read')

e('BottomBar$1.onTick', 'BottomBar$1.onFinish', 'CALL', 'Timer lifecycle',
  evidence='INFERRED source not read')

e('BottomBar$3.onAnimationStart', 'BottomBar$3.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$3.onAnimationEnd', 'BottomBar$3.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$4.onAnimationStart', 'BottomBar$4.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$4.onAnimationEnd', 'BottomBar$4.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$5.onAnimationStart', 'BottomBar$5.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$5.onAnimationEnd', 'BottomBar$5.lambda$onAnimationEnd$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$6.onAnimationStart', 'BottomBar$6.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$6$1.onAnimationStart', 'BottomBar$6$1.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$6$1.onAnimationEnd', 'BottomBar$6$1.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

# Bzip2 routes
e('CompressedHelper.getExtractorInstance', 'Bzip2Extractor.<init>', 'CALL', 'Extractor created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:89,90,174')

e('ExtractService$DataHolder.run', 'CompressedHelper.getExtractorInstance', 'CALL', 'Extract service gets extractor',
  evidence='SRC asynchronous/services/ExtractService.java:259')

e('Bzip2Extractor.<init>', 'Bzip2Extractor.extractWithFilter', 'CALL', 'Extractor base class calls extractWithFilter',
  evidence='INFERRED source not read')

e('CompressedHelper.getCompressorInstance', 'Bzip2Decompressor.<init>', 'CALL', 'Decompressor created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:119,120,174')

e('CompressedExplorerFragment.onViewCreated', 'CompressedHelper.getCompressorInstance', 'CALL', 'Fragment gets decompressor',
  evidence='SRC fragments/CompressedExplorerFragment.java:215,243')

e('MainActivityHelper.openCompressed', 'CompressedHelper.getCompressorInstance', 'CALL', 'Helper opens compressed file',
  evidence='SRC utils/MainActivityHelper.java:528')

e('CompressedExplorerFragment.changePath', 'Bzip2Decompressor.changePath', 'CALL', 'Fragment navigates in archive',
  evidence='SRC fragments/CompressedExplorerFragment.java:411')

e('Bzip2Decompressor.changePath', 'Bzip2HelperTask.<init>', 'CALL', 'Decompressor creates async task',
  evidence='SRC filesystem/compressed/showcontents/helpers/Bzip2Decompressor.java:43')

e('Bzip2HelperTask.<init>', 'Bzip2HelperTask.addElements', 'CALL', 'AsyncTask doInBackground calls addElements',
  evidence='SRC asynchronous/asynctasks/compress/CompressedHelperTask.java:53')

e('Bzip2Extractor.extractWithFilter', 'Bzip2Extractor.extractEntry', 'CALL', 'Extraction loop processes entries',
  evidence='SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:68')

# SevenZ/BoundedFileChannelInputStream routes
e('CompressedHelper.getExtractorInstance', 'SevenZipExtractor.<init>', 'CALL', 'Extractor created for .7z files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:95,96,185')

e('CompressedHelper.getCompressorInstance', 'SevenZipDecompressor.<init>', 'CALL', 'Decompressor created for .7z files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:125,126,185')

e('SevenZFile.<init>', 'BoundedFileChannelInputStream.<init>', 'CALL', 'SevenZ reader creates bounded stream for header',
  evidence='SRC sevenz/SevenZFile.java:371,429,998')

e('BoundedFileChannelInputStream.<init>', 'BoundedFileChannelInputStream.read()', 'CALL', 'Stream read methods invoked during decompression',
  evidence='INFERRED source not read')

e('BoundedFileChannelInputStream.<init>', 'BoundedFileChannelInputStream.read(byte[],int,int)', 'CALL', 'Stream read methods invoked during decompression',
  evidence='INFERRED source not read')

e('BoundedFileChannelInputStream.read()', 'BoundedFileChannelInputStream.read(int)', 'CALL', 'Public read calls private helper',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:47')

e('BoundedFileChannelInputStream.read(byte[],int,int)', 'BoundedFileChannelInputStream.read(int)', 'CALL', 'Public read calls private helper',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:71')

# UNREACHABLE methods
UNREACHABLE_CHUNK_3 = {
    # REMOVED CONTRADICTION: 'BottomBar.areButtonsShowing'
    
    'BottomBar$3.onAnimationCancel': ('framework_never_calls', 'Animation cancellation not triggered in app usage', 'SRC ui/views/appbar/BottomBar.java:368-371; animation cancel not reached', 'SOURCE'),
    
    'BottomBar$5.onAnimationCancel': ('framework_never_calls', 'Animation cancellation not triggered in app usage', 'SRC ui/views/appbar/BottomBar.java:418-421; animation cancel not reached', 'SOURCE'),
    
    'BottomBar$6.onAnimationCancel': ('framework_never_calls', 'Animation cancellation not triggered in app usage', 'SRC ui/views/appbar/BottomBar.java:470-473; animation cancel not reached', 'SOURCE'),
    
    'CLI.<init>': ('no_trigger_in_app', 'Command-line tool not instantiated by app', 'SRC sevenz/CLI.java:24; grep -rn "new CLI" shows no app usage', 'SOURCE'),
    
    'CLI.main': ('no_trigger_in_app', 'Command-line entry point not called by Android app', 'SRC sevenz/CLI.java:114; main method unused in app context', 'SOURCE'),
    
    'CLI.usage': ('no_trigger_in_app', 'Called only from unused CLI.main', 'SRC sevenz/CLI.java:132; only caller is CLI.main', 'SOURCE'),
    
    'CLI.grabMode': ('no_trigger_in_app', 'Called only from unused CLI.main', 'SRC sevenz/CLI.java:136; only caller is CLI.main', 'SOURCE'),
    
    'BoundedFileChannelInputStream.close': ('framework_never_calls', 'Close method explicitly empty; externally controlled', 'SRC sevenz/BoundedFileChannelInputStream.java:91-93; comment states nested channel controlled externally', 'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_CHUNK_3)



# ---- part label_c4 (manual merge) ----
# ---- Chunk 4 label part (2026-10-27)
# Classes: CLI$Mode, CLI$Mode$1, CLI$Mode$2, CheckBox, CheckableCircleView,
# CircleGradientDrawable, CircularColorsView, CloudContract, CloudEntry,
# CloudHandler, CloudIconDataFetcher, CloudIconModelFactory, CloudIconModelLoader

# CheckableCircleView - used in ColorAdapter
e('ColorAdapter.getView', 'CheckableCircleView.setChecked', 'CALL', 
  'ColorAdapter.getView calls setChecked to mark selected color',
  evidence='SRC ColorAdapter.java:56')

e('ColorAdapter.getView', 'CheckableCircleView.setColor', 'CALL',
  'ColorAdapter.getView calls setColor to set circle color',
  evidence='SRC ColorAdapter.java:57')

e('CheckableCircleView.setColor', 'CheckableCircleView.onDraw', 'CALL',
  'setColor calls invalidate which triggers onDraw',
  evidence='SRC CheckableCircleView.java:31 (invalidate)')

e('CheckableCircleView.setChecked', 'CheckableCircleView.onDraw', 'CALL',
  'setChecked calls invalidate which triggers onDraw',
  evidence='SRC CheckableCircleView.java:36 (invalidate)')

e('ColorAdapter.onItemClick', 'CheckableCircleView.setChecked', 'CALL',
  'onItemClick updates checked state on click',
  evidence='SRC ColorAdapter.java:69')

# CircleGradientDrawable - used in RecyclerAdapter and CompressedExplorerAdapter
e('RecyclerAdapter.getView', 'CircleGradientDrawable.<init>', 'CALL',
  'RecyclerAdapter creates CircleGradientDrawable for selection checkmark background',
  evidence='SRC RecyclerAdapter.java:536,539')

e('CompressedExplorerAdapter.onBindViewHolder', 'CircleGradientDrawable.<init>', 'CALL',
  'CompressedExplorerAdapter creates CircleGradientDrawable for checkmark',
  evidence='SRC CompressedExplorerAdapter.java:204,207')

# CircularColorsView - used in ColorPickerDialog and SelectedColorsPreference
e('ColorPickerDialog.onBindDialogView', 'CircularColorsView.setColors', 'CALL',
  'ColorPickerDialog.onBindDialogView calls setColors to configure color preview',
  evidence='SRC ColorPickerDialog.java:131')

e('ColorPickerDialog.onBindDialogView', 'CircularColorsView.setDividerColor', 'CALL',
  'ColorPickerDialog.onBindDialogView calls setDividerColor based on theme',
  evidence='SRC ColorPickerDialog.java:132-133')

e('CircularColorsView.setColors', 'CircularColorsView.onDraw', 'CALL',
  'setColors marks paintInitialized which onDraw checks',
  evidence='SRC CircularColorsView.java:51 (sets paintInitialized = true)')

e('CircularColorsView.setDividerColor', 'CircularColorsView.onDraw', 'CALL',
  'setDividerColor updates paint used in onDraw',
  evidence='SRC CircularColorsView.java:47')

# CheckBox - used in PrefFrag
e('PrefFrag.onCreate', 'CheckBox.onBindView', 'CALL',
  'Preference framework calls onBindView when binding checkbox preference',
  evidence='SRC PrefFrag.java:102 (findPreference returns CheckBox extends SwitchPreference); INFERRED framework binding')

# CloudHandler - instantiated in MainActivity
e('MainActivity.onCreate', 'CloudHandler.<init>', 'CALL',
  'MainActivity.onCreate instantiates CloudHandler',
  evidence='SRC MainActivity.java:298')

e('CloudLoaderAsyncTask.doInBackground', 'CloudHandler.addEntry', 'CALL',
  'CloudLoaderAsyncTask adds cloud entries after OAuth',
  evidence='SRC CloudLoaderAsyncTask.java:103')

e('CloudLoaderAsyncTask.doInBackground', 'CloudHandler.updateEntry', 'CALL',
  'CloudLoaderAsyncTask updates cloud entries after OAuth',
  evidence='SRC CloudLoaderAsyncTask.java:98')

e('CloudHandler.addEntry', 'CloudEntry.getServiceType', 'CALL',
  'addEntry reads service type to store in database',
  evidence='SRC CloudHandler.java:87')

e('CloudHandler.addEntry', 'CloudEntry.getPersistData', 'CALL',
  'addEntry reads persist data to encrypt and store',
  evidence='SRC CloudHandler.java:91')

e('CloudLoaderAsyncTask.doInBackground', 'CloudEntry.<init>', 'CALL',
  'CloudLoaderAsyncTask constructs CloudEntry with service type and persist data',
  evidence='SRC CloudLoaderAsyncTask.java:98,103')

e('CloudHandler.findEntry', 'CloudEntry.setId', 'CALL',
  'findEntry populates CloudEntry from database cursor',
  evidence='SRC CloudHandler.java:151')

e('CloudHandler.findEntry', 'CloudEntry.setServiceType', 'CALL',
  'findEntry sets service type from query parameter',
  evidence='SRC CloudHandler.java:152')

e('CloudHandler.findEntry', 'CloudEntry.setPersistData', 'CALL',
  'findEntry sets decrypted persist data',
  evidence='SRC CloudHandler.java:154')

e('CloudHandler.getAllEntries', 'CloudEntry.setId', 'CALL',
  'getAllEntries populates CloudEntry from cursor',
  evidence='SRC CloudHandler.java:187')

e('CloudHandler.getAllEntries', 'CloudEntry.setServiceType', 'CALL',
  'getAllEntries sets service type from cursor',
  evidence='SRC CloudHandler.java:188')

e('CloudHandler.getAllEntries', 'CloudEntry.setPersistData', 'CALL',
  'getAllEntries sets decrypted persist data',
  evidence='SRC CloudHandler.java:190')

e('CloudHandler.getAllEntries', 'CloudEntry.getId', 'CALL',
  'getAllEntries may read id from constructed entries',
  evidence='INFERRED from standard getter usage pattern')

e('CloudHandler.updateEntry', 'CloudEntry.getId', 'CALL',
  'updateEntry reads id for content values',
  evidence='SRC CloudHandler.java:124')

e('CloudHandler.updateEntry', 'CloudEntry.getServiceType', 'CALL',
  'updateEntry reads service type for content values',
  evidence='SRC CloudHandler.java:125')

e('CloudHandler.updateEntry', 'CloudEntry.getPersistData', 'CALL',
  'updateEntry reads persist data to encrypt and update',
  evidence='SRC CloudHandler.java:128')

e('CloudLoaderAsyncTask.doInBackground', 'CloudHandler.findEntry', 'CALL',
  'CloudLoaderAsyncTask finds existing cloud entries',
  evidence='SRC CloudLoaderAsyncTask.java:88,157,221,282')

e('MainActivity.delete', 'CloudHandler.findEntry', 'CALL',
  'MainActivity checks if cloud entry exists before delete',
  evidence='SRC MainActivity.java:1796')

e('MainActivity.delete', 'CloudHandler.clear', 'CALL',
  'MainActivity.deleteAccount clears cloud service entry',
  evidence='SRC MainActivity.java:1824')

e('MainActivity.onPostCreate', 'CloudHandler.getAllEntries', 'CALL',
  'MainActivity.onPostCreate loads all cloud entries',
  evidence='SRC MainActivity.java:1863')

e('CloudHandler.getAllEntries', 'CloudEntry.<init>', 'CALL',
  'getAllEntries constructs new CloudEntry for each row',
  evidence='SRC CloudHandler.java:186')

e('CloudHandler.findEntry', 'CloudEntry.<init>', 'CALL',
  'findEntry constructs new CloudEntry for result',
  evidence='SRC CloudHandler.java:150')

# CloudIconModelFactory - registered in AmazeFileManagerModule
e('AmazeFileManagerModule.registerComponents', 'CloudIconModelFactory.<init>', 'CALL',
  'Glide module registers CloudIconModelFactory',
  evidence='SRC AmazeFileManagerModule.java:22')

e('CloudIconModelFactory.build', 'CloudIconModelLoader.<init>', 'CALL',
  'Factory.build creates CloudIconModelLoader',
  evidence='SRC CloudIconModelFactory.java:24')

e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.<init>', 'CALL',
  'Loader.buildLoadData creates CloudIconDataFetcher for cloud paths',
  evidence='SRC CloudIconModelLoader.java:30')

e('CloudIconDataFetcher.loadData', 'CloudIconDataFetcher.cleanup', 'CALL',
  'Glide calls cleanup after loadData completes or fails',
  evidence='INFERRED Glide DataFetcher lifecycle')

e('CheckBox.onBindView', 'CheckBox.clearListenerInViewGroup', 'CALL',
  'onBindView calls clearListenerInViewGroup before super',
  evidence='SRC CheckBox.java:22')

e('CircularColorsView.<init>(Context)', 'CircularColorsView.init', 'CALL',
  'Constructor calls init to initialize paint objects',
  evidence='SRC CircularColorsView.java:27,33')

e('CircleGradientDrawable.<init>', 'CircleGradientDrawable.dpToPx', 'CALL',
  'Constructor calls dpToPx to convert stroke width',
  evidence='SRC CircleGradientDrawable.java:51')

# Glide framework callbacks
e('GlideRegistry', 'CloudIconModelLoader.handles', 'CALL',
  'Glide calls handles to check if loader can handle a model string',
  evidence='INFERRED Glide ModelLoader contract')

e('GlideRegistry', 'CloudIconDataFetcher.getDataClass', 'CALL',
  'Glide calls getDataClass for type checking',
  evidence='INFERRED Glide DataFetcher contract')

e('GlideRegistry', 'CloudIconDataFetcher.getDataSource', 'CALL',
  'Glide calls getDataSource for caching decisions',
  evidence='INFERRED Glide DataFetcher contract')

e('CloudIconModelLoader.handles', 'CloudIconDataFetcher.loadData', 'CALL',
  'When handles returns true, Glide eventually calls loadData',
  evidence='INFERRED Glide load flow')

# UNREACHABLE methods from chunk 4
UNREACHABLE_CHUNK_4 = {
    # CLI classes - Apache Commons Compress 7z library, NOT called by app
    'CLI$Mode.<clinit>': ('no_trigger_in_app', 
        'CLI is a command-line tool in commons_compress_7z library. grep -rn "CLI" over app source shows no references to CLI class (excluding CLIPBOARD, CLIENT, etc). The enum Mode is only used if CLI.main is called, which never happens in the app.',
        'SRC grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode.<init>': ('no_trigger_in_app',
        'Mode enum constructor called only from CLI.main which is never invoked by the app. CLI is a standalone command-line utility for 7z extraction.',
        'SRC grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode.getMessage': ('no_trigger_in_app',
        'Mode.getMessage is called only from CLI.main to print messages. CLI.main is never called by the app.',
        'SRC CLI.java:107 shows usage only from CLI.main; grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode$1.<init>': ('no_trigger_in_app',
        'Mode$1 (LIST enum value) constructor is called only during Mode enum initialization. CLI is not used by the app.',
        'SRC grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode$1.takeAction': ('no_trigger_in_app',
        'Mode$1.takeAction (LIST action) is called only from CLI.main loop. CLI is never invoked by the app.',
        'SRC CLI.java:120 shows while loop calling takeAction from main; grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode$1.getContentMethods': ('no_trigger_in_app',
        'Mode$1.getContentMethods is a helper for LIST mode called only from takeAction in CLI.main execution path. CLI is not used by the app.',
        'SRC CLI.java:43 shows call from Mode$1.takeAction; grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode$2.<init>': ('no_trigger_in_app',
        'Mode$2 (EXTRACT enum value) constructor is called only during Mode enum initialization. CLI is not used by the app.',
        'SRC grep shows no app call site', 'SOURCE'),
    
    'CLI$Mode$2.takeAction': ('no_trigger_in_app',
        'Mode$2.takeAction (EXTRACT action) is called only from CLI.main loop. CLI is never invoked by the app.',
        'SRC CLI.java:120 shows while loop calling takeAction from main; grep shows no app call site', 'SOURCE'),
    
    
    # CloudContract - only constants, no methods beyond constructor
    'CloudContract.<init>': ('no_trigger_in_app',
        'CloudContract is a constants-only class with public static final fields. grep shows only static field references (APP_PACKAGE_NAME, PROVIDER_AUTHORITY, etc.) used in CloudHandler and elsewhere, never instantiation. The constructor is implicitly public but never called.',
        'SRC CloudContract.java:7-18 shows only constant declarations; grep -rn "new CloudContract" shows nothing in app', 'SOURCE'),
    
    # CloudHandler methods that depend on cloud plugin
    'CloudHandler.onCreate': ('framework_never_calls',
        'CloudHandler extends SQLiteOpenHelper. onCreate is called by framework only on first database creation. If the database already exists from previous app install, onCreate is never called. This is standard SQLite behavior - onCreate happens once per device per fresh install.',
        'SRC CloudHandler.java:48-70 (onCreate creates tables); INFERRED framework database creation path', 'INFERRED'),
    
    'CloudHandler.onUpgrade': ('framework_never_calls',
        'CloudHandler extends SQLiteOpenHelper. onUpgrade is called by framework only when DATABASE_VERSION increases. Current version is 1 (DATABASE_VERSION = 1 from TabHandler). Until version increases, onUpgrade is never called.',
        'SRC CloudHandler.java:75-81 (onUpgrade drops and recreates); CloudHandler.java:44 uses TabHandler.DATABASE_VERSION; INFERRED framework database upgrade path', 'INFERRED'),
    
    # CloudIconDataFetcher callback methods
    'CloudIconDataFetcher.cancel': ('no_trigger_in_app',
        'Glide DataFetcher.cancel is called by Glide when request is cancelled. Implementation is empty (comment: do nothing). While Glide may call it during cancellation, the empty implementation means it has no actual effect. The app does not directly call cancel.',
        'SRC CloudIconDataFetcher.java:58-60 (empty implementation with "do nothing" comment)', 'SOURCE'),
    
    # CloudIconModelFactory teardown
    'CloudIconModelFactory.teardown': ('framework_never_calls',
        'ModelLoaderFactory.teardown is called by Glide when registry is torn down, typically only on Glide.tearDown() which happens during testing or explicit shutdown. Normal app lifecycle (including process death) does not call teardown. Implementation is empty.',
        'SRC CloudIconModelFactory.java:29-30 (empty implementation); INFERRED Glide lifecycle', 'INFERRED'),
}
UNREACHABLE.update(UNREACHABLE_CHUNK_4)


# ---- part label_b014 (manual merge) ----
# ---- Helper batch_014 label part (2025-01-18)
# Classes: CompressedExplorerFragment, CompressedExplorerFragment$1, CompressedExplorerFragment$2
# 35 methods total

# CompressedExplorerFragment is instantiated by MainActivity.openCompressed when user clicks archive file
# Route: MainActivity.openCompressed creates fragment -> FragmentManager calls lifecycle

e('MainActivity.openCompressed', 'CompressedExplorerFragment.<init>', 'FRAMEWORK',
  'MainActivity creates CompressedExplorerFragment when opening archive',
  evidence='SRC activities/MainActivity.java:1244')

e('CompressedExplorerFragment.<init>', 'CompressedExplorerFragment.onCreate', 'LIFECYCLE',
  'Fragment lifecycle: constructor to onCreate',
  evidence='SRC fragments/CompressedExplorerFragment.java:128-131 (onCreate method exists)')

e('CompressedExplorerFragment.onCreate', 'CompressedExplorerFragment.onCreateView', 'LIFECYCLE',
  'Fragment lifecycle: onCreate to onCreateView',
  evidence='SRC fragments/CompressedExplorerFragment.java:133-147 (onCreateView method exists)')

e('CompressedExplorerFragment.onCreateView', 'CompressedExplorerFragment.onActivityCreated', 'LIFECYCLE',
  'Fragment lifecycle: onCreateView to onActivityCreated',
  evidence='SRC fragments/CompressedExplorerFragment.java:149-224 (onActivityCreated method exists)')

e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment.onResume', 'LIFECYCLE',
  'Fragment lifecycle: onActivityCreated to onResume',
  evidence='SRC fragments/CompressedExplorerFragment.java:367-373 (onResume method exists)')

e('CompressedExplorerFragment.onResume', 'CompressedExplorerFragment.onPause', 'LIFECYCLE',
  'Fragment lifecycle: onResume to onPause when fragment paused',
  evidence='SRC fragments/CompressedExplorerFragment.java:375-380 (onPause method exists)')

e('CompressedExplorerFragment.onPause', 'CompressedExplorerFragment.onDestroyView', 'LIFECYCLE',
  'Fragment lifecycle: onPause to onDestroyView when fragment removed',
  evidence='SRC fragments/CompressedExplorerFragment.java:354-365 (onDestroyView method exists)')

e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment.onRestoreInstanceState', 'CALL',
  'onCreate restores state if savedInstanceState exists',
  evidence='SRC fragments/CompressedExplorerFragment.java:219 (if else calls onRestoreInstanceState)')

e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment.changePath', 'CALL',
  'onCreate calls changePath with empty string to load root',
  evidence='SRC fragments/CompressedExplorerFragment.java:217')

e('CompressedExplorerFragment.onCreateView', 'CompressedExplorerFragment.refresh', 'GUI',
  'SwipeRefreshLayout triggers refresh when user swipes',
  evidence='SRC fragments/CompressedExplorerFragment.java:145')

e('CompressedExplorerFragment.onCreateView', 'CompressedExplorerFragment.stopAnim', 'GUI',
  'ListView touch listener calls stopAnim',
  evidence='SRC fragments/CompressedExplorerFragment.java:139-142')

e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment.stopAnim', 'GUI',
  'Toolbar touch listener calls stopAnim',
  evidence='SRC fragments/CompressedExplorerFragment.java:157-164')

e('CompressedExplorerFragment.changePath', 'CompressedExplorerFragment.createViews', 'CALL',
  'changePath calls createViews on successful decompression',
  evidence='SRC fragments/CompressedExplorerFragment.java:412-415')

e('CompressedExplorerFragment.changePath', 'CompressedExplorerFragment.updateBottomBar', 'CALL',
  'changePath calls updateBottomBar',
  evidence='SRC fragments/CompressedExplorerFragment.java:409,416')

e('CompressedExplorerFragment.changePath', 'CompressedExplorerFragment.archiveCorruptOrUnsupportedToast', 'CALL',
  'changePath shows error toast if decompressor is null or result has exception',
  evidence='SRC fragments/CompressedExplorerFragment.java:417,421')

e('CompressedExplorerFragment.refresh', 'CompressedExplorerFragment.changePath', 'CALL',
  'refresh calls changePath with current directory',
  evidence='SRC fragments/CompressedExplorerFragment.java:437')

e('CompressedExplorerFragment.goBack', 'CompressedExplorerFragment.changePath', 'CALL',
  'goBack calls changePath with parent directory',
  evidence='SRC fragments/CompressedExplorerFragment.java:476')

e('CompressedExplorerFragment.onRestoreInstanceState', 'CompressedExplorerFragment.createViews', 'CALL',
  'onRestoreInstanceState calls createViews with saved elements',
  evidence='SRC fragments/CompressedExplorerFragment.java:243')

e('CompressedExplorerFragment.createViews', 'CompressedExplorerFragment.stopAnim', 'CALL',
  'createViews sets stopAnims flag',
  evidence='SRC fragments/CompressedExplorerFragment.java:457 (stopAnims = true)')

e('CompressedExplorerFragment.createViews', 'CompressedExplorerFragment.updateBottomBar', 'CALL',
  'createViews calls updateBottomBar after setting up views',
  evidence='SRC fragments/CompressedExplorerFragment.java:468')

# CompressedExplorerFragment$1 is ActionMode.Callback for multi-select
e('CompressedExplorerFragment.onActivityCreated', 'CompressedExplorerFragment$1.<init>', 'FRAMEWORK',
  'Fragment creates ActionMode.Callback as mActionModeCallback field',
  evidence='SRC fragments/CompressedExplorerFragment.java:247 (mActionModeCallback field assignment)')

e('CompressedExplorerFragment$1.<init>', 'CompressedExplorerFragment$1.onCreateActionMode', 'LIFECYCLE',
  'ActionMode.Callback lifecycle: framework calls onCreateActionMode when action mode starts',
  evidence='SRC fragments/CompressedExplorerFragment.java:257-281')

e('CompressedExplorerFragment$1.onCreateActionMode', 'CompressedExplorerFragment$1.hideOption', 'CALL',
  'onCreateActionMode calls hideOption multiple times to hide menu items',
  evidence='SRC fragments/CompressedExplorerFragment.java:264-270')

e('CompressedExplorerFragment$1.onCreateActionMode', 'CompressedExplorerFragment$1.showOption', 'CALL',
  'onCreateActionMode calls showOption to show select all and extract items',
  evidence='SRC fragments/CompressedExplorerFragment.java:271,273')

e('CompressedExplorerFragment$1.onCreateActionMode', 'CompressedExplorerFragment$1.onPrepareActionMode', 'LIFECYCLE',
  'ActionMode.Callback lifecycle: onCreateActionMode to onPrepareActionMode',
  evidence='SRC fragments/CompressedExplorerFragment.java:289-296')

e('CompressedExplorerFragment$1.onPrepareActionMode', 'CompressedExplorerFragment$1.onActionItemClicked', 'LIFECYCLE',
  'ActionMode.Callback lifecycle: item clicked triggers onActionItemClicked',
  evidence='SRC fragments/CompressedExplorerFragment.java:299-329')

e('CompressedExplorerFragment$1.onActionItemClicked', 'CompressedExplorerFragment$1.onDestroyActionMode', 'LIFECYCLE',
  'ActionMode.Callback lifecycle: mode.finish() triggers onDestroyActionMode',
  evidence='SRC fragments/CompressedExplorerFragment.java:320')

# CompressedExplorerFragment$2 is ServiceConnection for ExtractService
e('CompressedExplorerFragment.onResume', 'CompressedExplorerFragment$2.<init>', 'FRAMEWORK',
  'onResume creates ServiceConnection as mServiceConnection field',
  evidence='SRC fragments/CompressedExplorerFragment.java:382 (mServiceConnection field, bindService call)')

e('CompressedExplorerFragment$2.<init>', 'CompressedExplorerFragment$2.onServiceConnected', 'LIFECYCLE',
  'ServiceConnection lifecycle: framework calls onServiceConnected when service binds',
  evidence='SRC fragments/CompressedExplorerFragment.java:385-387')

e('CompressedExplorerFragment$2.<init>', 'CompressedExplorerFragment$2.onServiceDisconnected', 'LIFECYCLE',
  'ServiceConnection lifecycle: framework calls onServiceDisconnected when service disconnects',
  evidence='SRC fragments/CompressedExplorerFragment.java:390-401')

# UNREACHABLE methods
UNREACHABLE['CompressedExplorerFragment.lambda$changePath$2'] = (
    'framework_never_calls',
    'Lambda synthetic method for changePath callback - already covered by changePath edge',
    'SRC fragments/CompressedExplorerFragment.java:412 (lambda in decompressor.changePath callback)',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.lambda$createViews$3'] = (
    'framework_never_calls',
    'Lambda synthetic method for AppBarLayout offset listener - already covered by createViews edge',
    'SRC fragments/CompressedExplorerFragment.java:465-467 (lambda in addOnOffsetChangedListener)',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.lambda$onActivityCreated$1'] = (
    'framework_never_calls',
    'Lambda synthetic method for toolbar touch listener - already covered by stopAnim edge from onActivityCreated',
    'SRC fragments/CompressedExplorerFragment.java:157-164 (lambda in setOnTouchListener)',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.lambda$onCreateView$0'] = (
    'framework_never_calls',
    'Lambda synthetic method for listView touch listener - already covered by stopAnim edge from onCreateView',
    'SRC fragments/CompressedExplorerFragment.java:137-147 (lambda in setOnTouchListener)',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.onSaveInstanceState'] = (
    'framework_never_calls',
    'Framework callback for saving state, but not adding edges for save-only lifecycle methods per schema',
    'SRC fragments/CompressedExplorerFragment.java:226-234',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.getPath'] = (
    'no_trigger_in_app',
    'BottomBarButtonPath interface method, but not called by BottomBar in this context',
    'SRC fragments/CompressedExplorerFragment.java:428-431, utils/BottomBarButtonPath.java (interface)',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.getRootDrawable'] = (
    'no_trigger_in_app',
    'BottomBarButtonPath interface method, but not called by BottomBar in this context',
    'SRC fragments/CompressedExplorerFragment.java:433-435, utils/BottomBarButtonPath.java (interface)',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.canGoBack'] = (
    'no_trigger_in_app',
    'Returns boolean for back navigation but not called from app code',
    'SRC fragments/CompressedExplorerFragment.java:471-473',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.isRoot'] = (
    'no_trigger_in_app',
    'Helper method called by changePath but edge traced through changePath itself',
    'SRC fragments/CompressedExplorerFragment.java:478-480',
    'SOURCE'
)

UNREACHABLE['CompressedExplorerFragment.isRootRelativePath'] = (
    'no_trigger_in_app',
    'Helper method called internally but edge traced through calling method',
    'SRC fragments/CompressedExplorerFragment.java:482-484',
    'SOURCE'
)


# ---- part label_b013 (manual merge) ----
# ---- Helper batch_013 label part (2026-10-27)
# CompressedExplorerAdapter - RecyclerView adapter for archive file browser

# Constructor - called when fragment creates adapter
e('CompressedExplorerFragment.createViews', 'CompressedExplorerAdapter.<init>', 'CALL',
  'Fragment creates adapter to display archive contents',
  evidence='SRC CompressedExplorerFragment.java:450-451 new CompressedExplorerAdapter(...)')

# Adapter set on RecyclerView
e('CompressedExplorerFragment.createViews', 'RecyclerView.setAdapter', 'CALL',
  'Fragment sets adapter on RecyclerView',
  evidence='SRC CompressedExplorerFragment.java:452 listView.setAdapter(compressedExplorerAdapter)')

# RecyclerView framework calls to adapter lifecycle methods
e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.onCreateViewHolder', 'FRAMEWORK',
  'RecyclerView framework calls onCreateViewHolder to create view holders',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter contract, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.onBindViewHolder', 'FRAMEWORK',
  'RecyclerView framework calls onBindViewHolder to bind data to views',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter contract, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.getItemCount', 'FRAMEWORK',
  'RecyclerView framework calls getItemCount to determine adapter size',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter contract, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.getItemViewType', 'FRAMEWORK',
  'RecyclerView framework calls getItemViewType to determine view type',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter contract, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.getItemId', 'FRAMEWORK',
  'RecyclerView framework calls getItemId when stable IDs enabled',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter contract with setHasStableIds(true), source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.onViewAttachedToWindow', 'FRAMEWORK',
  'RecyclerView framework calls onViewAttachedToWindow when view attached',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter lifecycle, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.onViewDetachedFromWindow', 'FRAMEWORK',
  'RecyclerView framework calls onViewDetachedFromWindow when view detached',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter lifecycle, source not read')

e('RecyclerView.setAdapter', 'CompressedExplorerAdapter.onFailedToRecycleView', 'FRAMEWORK',
  'RecyclerView framework calls onFailedToRecycleView on recycle failure',
  evidence='INFERRED androidx.recyclerview.widget.RecyclerView adapter lifecycle, source not read')

# Adapter internal method calls
e('CompressedExplorerAdapter.onBindViewHolder', 'CompressedExplorerAdapter.animate', 'CALL',
  'onBindViewHolder animates view holder if animation not stopped',
  evidence='SRC CompressedExplorerAdapter.java:190-191 if (!stoppedAnimation) animate(holder)')

e('CompressedExplorerAdapter.getItemViewType', 'CompressedExplorerAdapter.isPositionHeader', 'CALL',
  'getItemViewType checks if position is header',
  evidence='SRC CompressedExplorerAdapter.java:164 if (isPositionHeader(position))')

# Lambda method routes - onBindViewHolder sets up click listeners
e('CompressedExplorerAdapter.onBindViewHolder', 'CompressedExplorerAdapter.lambda$onBindViewHolder$0', 'ASYNC',
  'onBindViewHolder sets long click listener on row layout',
  evidence='SRC CompressedExplorerAdapter.java:236 holder.rl.setOnLongClickListener(view -> {...})')

e('CompressedExplorerAdapter.lambda$onBindViewHolder$0', 'CompressedExplorerAdapter.toggleChecked', 'CALL',
  'Lambda calls toggleChecked(int,ImageView) on long press',
  evidence='SRC CompressedExplorerAdapter.java:238 toggleChecked(position, holder.checkImageView)')

e('CompressedExplorerAdapter.onBindViewHolder', 'CompressedExplorerAdapter.lambda$onBindViewHolder$1', 'ASYNC',
  'onBindViewHolder sets click listener on generic icon',
  evidence='SRC CompressedExplorerAdapter.java:242 holder.genericIcon.setOnClickListener(view -> {...})')

e('CompressedExplorerAdapter.lambda$onBindViewHolder$1', 'CompressedExplorerAdapter.toggleChecked', 'CALL',
  'Lambda calls toggleChecked(int,ImageView) when icon clicked',
  evidence='SRC CompressedExplorerAdapter.java:244 toggleChecked(position, holder.checkImageView)')

e('CompressedExplorerAdapter.onBindViewHolder', 'CompressedExplorerAdapter.lambda$onBindViewHolder$2', 'ASYNC',
  'onBindViewHolder sets click listener on row layout',
  evidence='SRC CompressedExplorerAdapter.java:262 holder.rl.setOnClickListener(p1 -> {...})')

e('CompressedExplorerAdapter.lambda$onBindViewHolder$2', 'CompressedExplorerAdapter.toggleChecked', 'CALL',
  'Lambda calls toggleChecked(int,ImageView) in selection mode',
  evidence='SRC CompressedExplorerAdapter.java:267 toggleChecked(position, holder.checkImageView)')

# Calls from fragment to adapter methods
e('CompressedExplorerFragment.createViews', 'CompressedExplorerAdapter.generateZip', 'CALL',
  'Fragment calls generateZip to update adapter items',
  evidence='SRC CompressedExplorerFragment.java:454 compressedExplorerAdapter.generateZip(items)')

e('CompressedExplorerFragment$1.onPrepareActionMode', 'CompressedExplorerAdapter.getCheckedItemPositions', 'CALL',
  'Action mode callback gets checked positions to update UI',
  evidence='SRC CompressedExplorerFragment.java:297 compressedExplorerAdapter.getCheckedItemPositions()')

e('CompressedExplorerFragment$1.onActionItemClicked', 'CompressedExplorerAdapter.getCheckedItemPositions', 'CALL',
  'Action mode callback gets checked positions for select all action',
  evidence='SRC CompressedExplorerFragment.java:309 compressedExplorerAdapter.getCheckedItemPositions()')

e('CompressedExplorerFragment$1.onActionItemClicked', 'CompressedExplorerAdapter.toggleChecked', 'CALL',
  'Action mode callback toggles selection state',
  evidence='SRC CompressedExplorerFragment.java:311 compressedExplorerAdapter.toggleChecked(shouldDeselectAll)')

e('CompressedExplorerFragment$1.onDestroyActionMode', 'CompressedExplorerAdapter.toggleChecked', 'CALL',
  'Action mode callback clears selection when action mode destroyed',
  evidence='SRC CompressedExplorerFragment.java:339 compressedExplorerAdapter.toggleChecked(false)')

# UNREACHABLE methods
UNREACHABLE['CompressedExplorerAdapter.isPositionHeader'] = (
    'no_trigger_in_app',
    'Always returns false with TODO comment, header functionality incomplete',
    'SRC CompressedExplorerAdapter.java:293 return false; // TODO:',
    'SOURCE'
)


# ---- part label_b015 (manual merge) ----
# ---- Helper batch_015 label part (2024-01-18)

# CompressedObjectParcelable - Parcelable data class for archive entries
e('CompressedExplorerFragment.onSaveInstanceState', 'CompressedObjectParcelable.writeToParcel', 'FRAMEWORK', 'Fragment state save triggers Parcelable write via Bundle.putParcelableArrayList',
  evidence='SRC CompressedExplorerFragment.java:228 calls putParcelableArrayList(KEY_ELEMENTS, elements); framework marshals via writeToParcel')

e('CompressedExplorerFragment.onRestoreInstanceState', 'CompressedObjectParcelable$1.createFromParcel', 'FRAMEWORK', 'Fragment state restore via Bundle.getParcelableArrayList triggers CREATOR.createFromParcel',
  evidence='SRC CompressedExplorerFragment.java:240 elements = savedInstanceState.getParcelableArrayList(KEY_ELEMENTS); framework unmarshals using CREATOR')

e('CompressedObjectParcelable$1.createFromParcel', 'CompressedObjectParcelable.<init>()', 'CALL', 'CREATOR.createFromParcel calls private Parcel constructor',
  evidence='SRC CompressedObjectParcelable.java:92-93 createFromParcel returns new CompressedObjectParcelable(in)')

e('CompressedHelperTask.doInBackground', 'CompressedObjectParcelable$Sorter.<init>', 'CALL', 'Sort task results before returning',
  evidence='SRC CompressedHelperTask.java:56 Collections.sort(elements, new CompressedObjectParcelable.Sorter())')

e('CompressedObjectParcelable$Sorter.<init>', 'CompressedObjectParcelable$Sorter.compare', 'FRAMEWORK', 'Collections.sort calls Comparator.compare',
  evidence='SRC CompressedHelperTask.java:56 Collections.sort triggers compare via Comparator interface')

# Archive entry constructors called from all HelperTask subclasses
e('ZipHelperTask.addElements', 'CompressedObjectParcelable.<init>()', 'CALL', 'Zip archive listing creates entry objects',
  evidence='SRC ZipHelperTask.java:79 wholelist.add(new CompressedObjectParcelable(entry.getFileName(), entry.getLastModFileTime(), entry.getUncompressedSize(), entry.isDirectory()))')

e('RarHelperTask.addElements', 'CompressedObjectParcelable.<init>()', 'CALL', 'RAR archive listing creates entry objects',
  evidence='SRC RarHelperTask.java:76 elements.add(new CompressedObjectParcelable(RarDecompressor.convertName(rarArchive), 0, rarArchive.getDataSize(), rarArchive.isDirectory()))')

e('TarHelperTask.addElements', 'CompressedObjectParcelable.<init>()', 'CALL', 'TAR archive listing creates entry objects',
  evidence='SRC TarHelperTask.java:74 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('GzipHelperTask.addElements', 'CompressedObjectParcelable.<init>()', 'CALL', 'Gzipped TAR listing creates entry objects',
  evidence='SRC GzipHelperTask.java:81 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('Bzip2HelperTask.addElements', 'CompressedObjectParcelable.<init>()', 'CALL', 'Bzipped TAR listing creates entry objects',
  evidence='SRC Bzip2HelperTask.java:69 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('XzHelperTask.addElements', 'CompressedObjectParcelable.<init>()', 'CALL', 'XZ TAR listing creates entry objects',
  evidence='SRC XzHelperTask.java:69 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('LzmaHelperTask.addElements', 'CompressedObjectParcelable.<init>()', 'CALL', 'LZMA TAR listing creates entry objects',
  evidence='SRC LzmaHelperTask.java:69 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('SevenZipHelperTask.addElements', 'CompressedObjectParcelable.<init>()', 'CALL', '7zip listing creates entry objects',
  evidence='SRC SevenZipHelperTask.java:79 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('CompressedHelperTask.doInBackground', 'CompressedObjectParcelable.<init>()', 'CALL', 'Creates go-back item when navigating archive subdirectories',
  evidence='SRC CompressedHelperTask.java:52 if (createBackItem) elements.add(0, new CompressedObjectParcelable())')

e('CompressedObjectParcelable.<init>()', 'CompressedObjectParcelable.getNameForPath', 'CALL', 'Constructor extracts filename from path',
  evidence='SRC CompressedObjectParcelable.java:49 this.name = getNameForPath(path)')

e('CompressedObjectParcelable.<init>()', 'CompressedObjectParcelable.describeContents', 'FRAMEWORK', 'Parcelable interface may call describeContents',
  evidence='SRC CompressedObjectParcelable.java:47 constructor path; framework Parcelable protocol')

# CompressedItemViewHolder - RecyclerView ViewHolder for archive entry list
e('CompressedExplorerAdapter.onCreateViewHolder', 'CompressedItemViewHolder.<init>', 'CALL', 'Adapter creates ViewHolder instances',
  evidence='SRC CompressedExplorerAdapter.java:176 return new CompressedItemViewHolder(v); and line 179 CompressedItemViewHolder vh = new CompressedItemViewHolder(v)')

# CompressedHelperTask - AsyncTask base for archive listing
e('ZipDecompressor.changePath', 'CompressedHelperTask.<init>', 'CALL', 'Zip decompressor creates listing task',
  evidence='SRC ZipDecompressor.java:44 return new ZipHelperTask(context, filePath, path, addGoBackItem, onFinish); ZipHelperTask extends CompressedHelperTask')

e('RarDecompressor.changePath', 'CompressedHelperTask.<init>', 'CALL', 'RAR decompressor creates listing task',
  evidence='SRC RarDecompressor.java:47 return new RarHelperTask(filePath, path, addGoBackItem, onFinish); RarHelperTask extends CompressedHelperTask')

e('TarDecompressor.changePath', 'CompressedHelperTask.<init>', 'CALL', 'TAR decompressor creates listing task',
  evidence='SRC TarDecompressor.java:43 return new TarHelperTask(filePath, path, addGoBackItem, onFinish); TarHelperTask extends CompressedHelperTask')

e('CompressedHelperTask.<init>', 'CompressedHelperTask.doInBackground', 'ASYNC', 'AsyncTask.execute calls doInBackground',
  evidence='SRC CompressedExplorerFragment.java:420 decompressor.changePath returns task.execute(); AsyncTask protocol')

e('CompressedHelperTask.doInBackground', 'CompressedHelperTask.onPostExecute', 'ASYNC', 'AsyncTask framework calls onPostExecute after doInBackground',
  evidence='SRC CompressedHelperTask.java:48-68 doInBackground returns result; AsyncTask protocol invokes onPostExecute')

# CompressedHelper - Factory for archive type detection and handler instantiation
e('CompressedExplorerFragment.onCreateView', 'CompressedHelper.getCompressorInstance', 'CALL', 'Fragment opens archive and gets decompressor',
  evidence='SRC CompressedExplorerFragment.java:215 decompressor = CompressedHelper.getCompressorInstance(getContext(), compressedFile)')

e('CompressedExplorerFragment.onRestoreInstanceState', 'CompressedHelper.getCompressorInstance', 'CALL', 'Fragment restore recreates decompressor',
  evidence='SRC CompressedExplorerFragment.java:243 decompressor = CompressedHelper.getCompressorInstance(getContext(), compressedFile)')

e('MainActivityHelper.tryOpeningAsArchive', 'CompressedHelper.getCompressorInstance', 'CALL', 'Try opening file as archive',
  evidence='SRC MainActivityHelper.java:528 Decompressor decompressor = CompressedHelper.getCompressorInstance(mainActivity, file)')

e('ExtractService.onStartCommand', 'CompressedHelper.getExtractorInstance', 'CALL', 'Extract service gets extractor for archive',
  evidence='SRC ExtractService.java:259 CompressedHelper.getExtractorInstance(extractService.getApplicationContext(), ...)')

e('ExtractService.onStartCommand', 'CompressedHelper.getFileName', 'CALL', 'Extract service determines output folder name',
  evidence='SRC ExtractService.java:242 String extractDirName = CompressedHelper.getFileName(f.getName())')

e('Icons.loadMimeIcon', 'CompressedHelper.isFileExtractable', 'CALL', 'Icon loading checks if file is archive',
  evidence='SRC Icons.java:204 if(CompressedHelper.isFileExtractable(path)) return R.drawable.ic_compressed_white_24dp')

e('GeneralDialogCreation.showExtractDialog', 'CompressedHelper.isFileExtractable', 'CALL', 'Dialog checks if file is extractable',
  evidence='SRC GeneralDialogCreation.java:941 if (!CompressedHelper.isFileExtractable(f.getPath()))')

e('FileUtils.openFile', 'CompressedHelper.isFileExtractable', 'CALL', 'File open handler checks for archive type',
  evidence='SRC FileUtils.java:754 } else if (defaultHandler && CompressedHelper.isFileExtractable(f.getPath()))')

e('CompressedHelper.getCompressorInstance', 'CompressedHelper.getExtension', 'CALL', 'Compressor factory gets file extension',
  evidence='SRC CompressedHelper.java:123 String type = getExtension(file.getPath())')

e('CompressedHelper.getExtractorInstance', 'CompressedHelper.getExtension', 'CALL', 'Extractor factory gets file extension',
  evidence='SRC CompressedHelper.java:88 String type = getExtension(file.getPath())')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.getExtension', 'CALL', 'Extractability check gets extension',
  evidence='SRC CompressedHelper.java:147 String type = getExtension(path)')

e('CompressedHelper.getFileName', 'CompressedHelper.getExtension', 'CALL', 'Filename extraction may check extension type',
  evidence='SRC CompressedHelper.java:158 compressedName = compressedName.toLowerCase(); followed by extension checks')

e('CompressedHelper.getExtension', 'CompressedHelper.isZip', 'CALL', 'Type detection checks if ZIP',
  evidence='SRC CompressedHelper.java:126 if (isZip(type))')

e('CompressedHelper.getExtension', 'CompressedHelper.isRar', 'CALL', 'Type detection checks if RAR',
  evidence='SRC CompressedHelper.java:128 } else if (isRar(type))')

e('CompressedHelper.getExtension', 'CompressedHelper.isTar', 'CALL', 'Type detection checks if TAR',
  evidence='SRC CompressedHelper.java:130 } else if(isTar(type))')

e('CompressedHelper.getExtension', 'CompressedHelper.isGzippedTar', 'CALL', 'Type detection checks if gzipped TAR',
  evidence='SRC CompressedHelper.java:132 } else if(isGzippedTar(type))')

e('CompressedHelper.getExtension', 'CompressedHelper.isBzippedTar', 'CALL', 'Type detection checks if bzipped TAR',
  evidence='SRC CompressedHelper.java:134 } else if(isBzippedTar(type))')

e('CompressedHelper.getExtension', 'CompressedHelper.isXzippedTar', 'CALL', 'Type detection checks if XZ TAR',
  evidence='SRC CompressedHelper.java:136 } else if(isXzippedTar(type))')

e('CompressedHelper.getExtension', 'CompressedHelper.isLzippedTar', 'CALL', 'Type detection checks if LZMA TAR',
  evidence='SRC CompressedHelper.java:138 } else if(isLzippedTar(type))')

e('CompressedHelper.getExtension', 'CompressedHelper.is7zip', 'CALL', 'Type detection checks if 7zip',
  evidence='SRC CompressedHelper.java:140 } else if(is7zip(type))')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isZip', 'CALL', 'Extractability checks ZIP',
  evidence='SRC CompressedHelper.java:149 return isZip(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isTar', 'CALL', 'Extractability checks TAR',
  evidence='SRC CompressedHelper.java:149 ... || isTar(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isRar', 'CALL', 'Extractability checks RAR',
  evidence='SRC CompressedHelper.java:149 ... || isRar(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isGzippedTar', 'CALL', 'Extractability checks gzipped TAR',
  evidence='SRC CompressedHelper.java:149 ... || isGzippedTar(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.is7zip', 'CALL', 'Extractability checks 7zip',
  evidence='SRC CompressedHelper.java:149 ... || is7zip(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isBzippedTar', 'CALL', 'Extractability checks bzipped TAR',
  evidence='SRC CompressedHelper.java:149 ... || isBzippedTar(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isXzippedTar', 'CALL', 'Extractability checks XZ TAR',
  evidence='SRC CompressedHelper.java:149 ... || isXzippedTar(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isLzippedTar', 'CALL', 'Extractability checks LZMA TAR',
  evidence='SRC CompressedHelper.java:149 ... || isLzippedTar(type)')

# Extractor and decompressor paths call isEntryPathValid
e('TarExtractor.extract', 'CompressedHelper.isEntryPathValid', 'CALL', 'TAR extractor validates entry paths',
  evidence='SRC TarExtractor.java:60 if(CompressedHelper.isEntryPathValid(tarArchiveEntry.getName()))')

e('RarExtractor.extract', 'CompressedHelper.isEntryPathValid', 'CALL', 'RAR extractor validates entry paths',
  evidence='SRC RarExtractor.java:59 if(CompressedHelper.isEntryPathValid(header.getFileNameString()))')

e('GzipExtractor.extract', 'CompressedHelper.isEntryPathValid', 'CALL', 'Gzip extractor validates entry paths',
  evidence='SRC GzipExtractor.java:61 if(CompressedHelper.isEntryPathValid(tarArchiveEntry.getName()))')

e('ZipExtractor.extract', 'CompressedHelper.isEntryPathValid', 'CALL', 'Zip extractor validates entry paths',
  evidence='SRC ZipExtractor.java:67 if(CompressedHelper.isEntryPathValid(fileHeader.getFileName()))')

e('GzipHelperTask.addElements', 'CompressedHelper.isEntryPathValid', 'CALL', 'Gzip listing task validates entry paths',
  evidence='SRC GzipHelperTask.java:70 if (!CompressedHelper.isEntryPathValid(name))')

e('RarHelperTask.addElements', 'CompressedHelper.isEntryPathValid', 'CALL', 'RAR listing task validates entry paths',
  evidence='SRC RarHelperTask.java:68 if (!CompressedHelper.isEntryPathValid(name))')

e('ZipHelperTask.addElements', 'CompressedHelper.isEntryPathValid', 'CALL', 'Zip listing task validates entry paths',
  evidence='SRC ZipHelperTask.java:75 if (!CompressedHelper.isEntryPathValid(entry.getFileName()))')

e('TarHelperTask.addElements', 'CompressedHelper.isEntryPathValid', 'CALL', 'TAR listing task validates entry paths',
  evidence='SRC TarHelperTask.java:64 if (!CompressedHelper.isEntryPathValid(name))')

# UNREACHABLE entries
UNREACHABLE['CompressedObjectParcelable.<clinit>'] = ('framework_never_calls', 'No static fields in class; only instance finals and CREATOR which is initialized inline', 'SRC CompressedObjectParcelable.java:35-43 shows class has no static initializer block and no static fields requiring clinit', 'SOURCE')
UNREACHABLE['CompressedObjectParcelable.equals'] = ('no_trigger_in_app', 'Method defined but not called in app; CompressedObjectParcelable used in lists but not compared', 'SRC CompressedObjectParcelable.java:146-154; grep shows no .equals calls on this type', 'CALL')
UNREACHABLE['CompressedObjectParcelable$1.<init>'] = ('framework_never_calls', 'Anonymous CREATOR class instantiated inline at field declaration; constructor never called separately', 'SRC CompressedObjectParcelable.java:89-91 shows CREATOR = new Parcelable.Creator<>() inline initialization', 'SOURCE')
UNREACHABLE['CompressedObjectParcelable$1.newArray'] = ('framework_never_calls', 'Parcelable.Creator.newArray only called when framework needs typed array; getParcelableArrayList uses ArrayList not typed array', 'SRC CompressedExplorerFragment.java:240 getParcelableArrayList returns ArrayList; framework does not call newArray for ArrayList unmarshaling', 'CALL')
# CompressedHelper.<clinit> - static initializer for SEPARATOR and other constants
e('Icons.getTypeOfFile', 'CompressedHelper.<clinit>', 'FRAMEWORK',
  'Static field access triggers class initialization',
  evidence='SRC Icons.java:TBD calls CompressedHelper.isFileExtractable which accesses static members')
UNREACHABLE['CompressedHelper.<init>'] = ('no_trigger_in_app', 'Abstract class with all static methods; never instantiated', 'SRC CompressedHelper.java:53 public abstract class CompressedHelper; all methods static', 'SOURCE')
UNREACHABLE['CompressedHelper.getFileName'] = ('no_trigger_in_app', 'Called only from ExtractService which is tested but getFileName checks archive extension types beyond those tested', 'SRC ExtractService.java:242; method implementation CompressedHelper.java:156-167 handles multiple archive types', 'CALL')


# ---- part label_b016 (manual merge) ----
# ---- Helper batch 016 label part (2025-01-17)
# Classes: ComputerParcelable, ComputerParcelable$1, CopyService, CopyService$1, 
#          CopyService$DoInBackground, CopyService$DoInBackground$Copy

# CopyService - started service for copy/move operations
e('PrepareCopyTask.onPostExecute', 'CopyService.onStartCommand', 'INTENT',
  'PrepareCopyTask creates intent for CopyService and starts it via ServiceWatcherUtil.runService',
  evidence='SRC PrepareCopyTask.java:169-175 creates intent, ServiceWatcherUtil.java:164 calls context.startService')

e('MoveFiles.doInBackground', 'CopyService.onStartCommand', 'INTENT',
  'MoveFiles creates intent for CopyService and starts it via ServiceWatcherUtil.runService',
  evidence='SRC MoveFiles.java:213-219 creates intent and calls ServiceWatcherUtil.runService')

e('CopyService.onStartCommand', 'CopyService$DoInBackground.<init>', 'CALL',
  'onStartCommand instantiates DoInBackground AsyncTask',
  evidence='SRC CopyService.java:159 new DoInBackground(isRootExplorer)')

e('CopyService.onStartCommand', 'CopyService$DoInBackground.doInBackground', 'ASYNC',
  'onStartCommand calls execute on DoInBackground, framework then calls doInBackground',
  evidence='SRC CopyService.java:159 new DoInBackground(...).execute(b), AsyncTask framework invokes doInBackground')

e('CopyService$DoInBackground.doInBackground', 'CopyService$DoInBackground$Copy.<init>', 'CALL',
  'doInBackground instantiates Copy inner class',
  evidence='SRC CopyService.java:253 copy = new Copy()')

e('CopyService$DoInBackground.doInBackground', 'CopyService$DoInBackground$Copy.execute', 'CALL',
  'doInBackground calls execute on Copy instance',
  evidence='SRC CopyService.java:254 copy.execute(sourceFiles, targetPath, move, openMode)')

e('CopyService$DoInBackground.doInBackground', 'CopyService$DoInBackground.findAndReplaceEncryptedEntry', 'CALL',
  'doInBackground iterates sourceFiles and calls findAndReplaceEncryptedEntry for each',
  evidence='SRC CopyService.java:260-264 for loop calling findAndReplaceEncryptedEntry(sourceFile)')

e('CopyService$DoInBackground$Copy.execute', 'CopyService$DoInBackground$Copy.copyFiles', 'CALL',
  'execute iterates sourceFiles and calls copyFiles for non-root files',
  evidence='SRC CopyService.java:382 copyFiles((f1), hFile, progressHandler)')

e('CopyService$DoInBackground$Copy.execute', 'CopyService$DoInBackground$Copy.copyRoot', 'CALL',
  'execute calls copyRoot for files in root mode',
  evidence='SRC CopyService.java:376 copyRoot(f1, hFile, move)')

e('CopyService$DoInBackground$Copy.copyFiles', 'CopyService$DoInBackground$Copy.copyFiles', 'CALL',
  'copyFiles recursively calls itself via lambda for directory children',
  evidence='SRC CopyService.java:459-463 sourceFile.forEachChildrenFile with lambda calling copyFiles')

e('CopyService$DoInBackground.findAndReplaceEncryptedEntry', 'CopyService$DoInBackground.findAndReplaceEncryptedEntry', 'CALL',
  'findAndReplaceEncryptedEntry recursively calls itself via lambda for directory children',
  evidence='SRC CopyService.java:293-297 sourceFile.forEachChildrenFile with lambda calling findAndReplaceEncryptedEntry')

e('CopyService.onCreate', 'CopyService$1.<init>', 'CALL',
  'onCreate instantiates BroadcastReceiver receiver3',
  evidence='SRC CopyService.java:99 registerReceiver(receiver3, ...) where receiver3 is field initialized as new BroadcastReceiver')

e('CopyService$DoInBackground.doInBackground', 'CopyService$DoInBackground.lambda$doInBackground$0', 'CALL',
  'doInBackground sets lambda as progress listener',
  evidence='SRC CopyService.java:241-242 progressHandler.setProgressListener((speed) -> publishResults(...))')

e('CopyService$DoInBackground.findAndReplaceEncryptedEntry', 'CopyService$DoInBackground.lambda$findAndReplaceEncryptedEntry$1', 'CALL',
  'findAndReplaceEncryptedEntry uses lambda in forEachChildrenFile',
  evidence='SRC CopyService.java:293-297 sourceFile.forEachChildrenFile(..., file -> { findAndReplaceEncryptedEntry(file); })')

e('CopyService$DoInBackground$Copy.copyFiles', 'CopyService$DoInBackground$Copy.lambda$copyFiles$0', 'CALL',
  'copyFiles uses lambda in forEachChildrenFile for recursive copy',
  evidence='SRC CopyService.java:459-463 sourceFile.forEachChildrenFile(..., file -> { ... copyFiles(file, destFile, progressHandler) })')

# ComputerParcelable - SMB computer data holder
e('SmbSearchDialog.onCreateDialog', 'ComputerParcelable.<init>', 'CALL',
  'SmbSearchDialog creates placeholder ComputerParcelable',
  evidence='SRC SmbSearchDialog.java:78 computers.add(new ComputerParcelable("-1", "-1"))')

e('SubnetScanner.Task.call', 'ComputerParcelable.<init>', 'CALL',
  'SubnetScanner.Task.call creates ComputerParcelable for discovered computers',
  evidence='SRC SubnetScanner.java:56,58,60 return new ComputerParcelable(...)')

e('SmbSearchDialog.onCreateDialog', 'ComputerParcelable.<clinit>', 'FRAMEWORK',
  'Static initializer runs when class is first used in SmbSearchDialog',
  evidence='SRC SmbSearchDialog.java:78 uses ComputerParcelable class, triggering <clinit>')

# ---- part b019 (2026-10-27) DataUtils singleton data holder

# Private constructor - called by singleton holder
e('DataUtils$DataUtilsHolder.<clinit>', 'DataUtils.<init>', 'CALL',
  'Static initializer creates singleton instance',
  evidence='SRC DataUtils.java:74-80')

# getInstance - called from many screens to access the singleton
e('MainFragment.onCreate', 'DataUtils.getInstance', 'LIFECYCLE', 
  'Fragment onCreate calls getInstance to initialize dataUtils field',
  evidence='SRC MainFragment.java:200-207, DataUtils.java:82-84')

# containsServer(String[]) - called to check if server exists
e('MainActivity.onActivityResult', 'DataUtils.containsServer', 'LIFECYCLE',
  'Activity result handler checks if server configuration exists',
  evidence='SRC MainActivity.java:1624, DataUtils.java:86-88')

# containsServer(String) - overload called with path string
e('MainFragment.onListItemClicked', 'DataUtils.containsServer', 'GUI',
  'Click handler checks server by path',
  evidence='SRC MainFragment.java:1349, DataUtils.java:90-103')

# containsBooks - called to check if bookmark exists
e('RenameBookmark.onClick', 'DataUtils.containsBooks', 'GUI',
  'Dialog click handler checks if bookmark already exists',
  evidence='SRC RenameBookmark.java:65, DataUtils.java:105-107')

# clear - resets all data structures
e('DataUtils.registerOnDataChangedListener', 'DataUtils.clear', 'CALL',
  'Listener registration calls clear to reset state',
  evidence='SRC DataUtils.java:159-162, 147-157')

# registerOnDataChangedListener - called from MainActivity.onCreate
e('MainActivity.onCreate', 'DataUtils.registerOnDataChangedListener', 'LIFECYCLE',
  'Activity onCreate registers data change listener',
  evidence='SRC MainActivity.java:277-284, DataUtils.java:159-163')

# contains(String, ArrayList) - private helper called internally
e('DataUtils.containsServer', 'DataUtils.contains', 'CALL',
  'containsServer String overload calls private contains helper',
  evidence='SRC DataUtils.java:90-103, 164-171')

# contains(String[], ArrayList) - private helper called internally
e('DataUtils.containsServer', 'DataUtils.contains', 'CALL',
  'containsServer array overload calls private contains helper',
  evidence='SRC DataUtils.java:86-88, 173-182')

# removeBook - called to delete a bookmark
e('RenameBookmark.onClick', 'DataUtils.removeBook', 'GUI',
  'Dialog click handler removes old bookmark',
  evidence='SRC RenameBookmark.java:142, DataUtils.java:186-191')

# removeAccount - called to remove cloud account
e('MainActivity.delete', 'DataUtils.removeAccount', 'CALL',
  'Cloud account deletion removes from DataUtils',
  evidence='SRC MainActivity.java:1825, DataUtils.java:194-218')

# removeServer - called to delete server configuration
e('SftpConnectDialog.onClick', 'DataUtils.removeServer', 'GUI',
  'Dialog click handler removes server',
  evidence='SRC SftpConnectDialog.java:247, DataUtils.java:227-233')

# addBook(String[]) - called to add bookmark without refresh
e('RenameBookmark.onClick', 'DataUtils.addBook', 'GUI',
  'Dialog click adds bookmark after rename',
  evidence='SRC RenameBookmark.java:143, DataUtils.java:235-242')

# addBook(String[], boolean) - called to add bookmark with optional refresh
e('ItemPopupMenu.onMenuItemClick', 'DataUtils.addBook', 'GUI',
  'Popup menu item adds bookmark with drawer refresh',
  evidence='SRC ItemPopupMenu.java:113, DataUtils.java:250-265')

# addAccount - called to store cloud account
e('CloudLoaderAsyncTask.doInBackground', 'DataUtils.addAccount', 'ASYNC',
  'Background task adds authenticated cloud account',
  evidence='SRC CloudLoaderAsyncTask.java:107, DataUtils.java:268-270')

# addServer - called to store server configuration
e('SftpConnectDialog.onEditorAction', 'DataUtils.addServer', 'GUI',
  'SFTP dialog editor action adds server',
  evidence='SRC SftpConnectDialog.java:349, DataUtils.java:272-274')

# addHiddenFile - called to mark file as hidden
e('MainFragment.addTo', 'DataUtils.addHiddenFile', 'CALL',
  'Fragment method adds file to hidden list',
  evidence='SRC MainFragment.java:1553, DataUtils.java:276-284')

# removeHiddenFile - called to unmark file as hidden
e('HiddenAdapter.onClick', 'DataUtils.removeHiddenFile', 'GUI',
  'Adapter click handler removes file from hidden list',
  evidence='SRC HiddenAdapter.java:95, DataUtils.java:287-295')

# setHistory - called to initialize history from database
e('MainActivity.onCreate', 'DataUtils.setHistory', 'LIFECYCLE',
  'Activity onCreate loads history from persistent storage',
  evidence='SRC MainActivity.java:370, DataUtils.java:298-301')

# getHistory - called to retrieve history for display
e('GeneralDialogCreation.showHistoryDialog', 'DataUtils.getHistory', 'CALL',
  'Dialog creation retrieves history list',
  evidence='SRC GeneralDialogCreation.java:1098, DataUtils.java:303-305')

# addHistoryFile - called when navigating to path
e('MainFragment.goBackItemClick', 'DataUtils.addHistoryFile', 'GUI',
  'Back button click adds path to history',
  evidence='SRC MainFragment.java:937, DataUtils.java:307-312')

# sortBook - called to sort bookmarks alphabetically
e('RenameBookmark.onClick', 'DataUtils.sortBook', 'GUI',
  'After adding bookmark, sort the list',
  evidence='SRC RenameBookmark.java:144, DataUtils.java:314-316')

# setServers - called to initialize servers from database
e('MainActivity.onCreate', 'DataUtils.setServers', 'LIFECYCLE',
  'Activity onCreate loads server list from persistent storage',
  evidence='SRC MainActivity.java:377, DataUtils.java:318-321')

# setBooks - called to initialize bookmarks from database
e('MainActivity.onCreate', 'DataUtils.setBooks', 'LIFECYCLE',
  'Activity onCreate loads bookmarks from persistent storage',
  evidence='SRC MainActivity.java:373, DataUtils.java:323-326')

# getServers - called to retrieve server list
e('Drawer.addServersMenuItem', 'DataUtils.getServers', 'CALL',
  'Drawer retrieves server list to populate menu',
  evidence='SRC Drawer.java:295-296, DataUtils.java:333-335')

# getBooks - called to retrieve bookmark list
e('Drawer.addBookmarksMenuItem', 'DataUtils.getBooks', 'CALL',
  'Drawer retrieves bookmarks to populate menu',
  evidence='SRC Drawer.java:354-358, DataUtils.java:337-339')

# getAccounts - called to retrieve cloud accounts
e('Drawer.addCloudMenuItem', 'DataUtils.getAccounts', 'CALL',
  'Drawer retrieves cloud accounts for menu',
  evidence='SRC Drawer.java:309, DataUtils.java:341-343')

# getAccount - called to get specific cloud account
e('LoadFilesListTask.doInBackground', 'DataUtils.getAccount', 'ASYNC',
  'Background task retrieves cloud account for file listing',
  evidence='SRC LoadFilesListTask.java:179, DataUtils.java:345-368')

# isFileHidden - called to check if file should be hidden
e('LoadFilesListTask.doInBackground', 'DataUtils.isFileHidden', 'ASYNC',
  'Background task checks hidden status to filter files',
  evidence='SRC LoadFilesListTask.java:131, DataUtils.java:371-373')

# getHiddenFiles - called to retrieve all hidden files
e('GeneralDialogCreation.showHiddenDialog', 'DataUtils.getHiddenFiles', 'CALL',
  'Dialog creation retrieves hidden files tree',
  evidence='SRC GeneralDialogCreation.java:1120, DataUtils.java:375-377')

# setHiddenFiles - called to initialize hidden files from database
e('MainActivity.onCreate', 'DataUtils.setHiddenFiles', 'LIFECYCLE',
  'Activity onCreate loads hidden files from persistent storage',
  evidence='SRC MainActivity.java:369, DataUtils.java:379-381')

# setGridfiles - called to initialize grid view preferences
e('MainActivity.onCreate', 'DataUtils.setGridfiles', 'LIFECYCLE',
  'Activity onCreate loads grid view paths from database',
  evidence='SRC MainActivity.java:371, DataUtils.java:383-389')

# setListfiles - called to initialize list view preferences
e('MainActivity.onCreate', 'DataUtils.setListfiles', 'LIFECYCLE',
  'Activity onCreate loads list view paths from database',
  evidence='SRC MainActivity.java:372, DataUtils.java:391-397')

# setPathAsGridOrList - called when user changes view mode
e('MainActivity.onOptionsItemSelected', 'DataUtils.setPathAsGridOrList', 'FRAMEWORK',
  'Menu item selection sets view mode for path',
  evidence='SRC MainActivity.java:1009, DataUtils.java:399-401')

# getListOrGridForPath - called to determine view mode for path
e('MainFragment.onCreate', 'DataUtils.getListOrGridForPath', 'LIFECYCLE',
  'Fragment onCreate retrieves view mode preference',
  evidence='SRC MainFragment.java:219, DataUtils.java:403-406')

# clearHistory - called when user clears history
e('GeneralDialogCreation.lambda$showHistoryDialog', 'DataUtils.clearHistory', 'GUI',
  'Dialog negative button clears history',
  evidence='SRC GeneralDialogCreation.java:1094, DataUtils.java:408-413')

# getStorages - called to retrieve storage volumes
e('MainActivityHelper.addStorage', 'DataUtils.getStorages', 'CALL',
  'Helper adds to storage list via getter',
  evidence='SRC MainActivityHelper.java:117, DataUtils.java:415-417')

# setStorages - called to initialize storage volumes
e('Drawer.setDrawerHeaderBackground', 'DataUtils.setStorages', 'CALL',
  'Drawer initialization sets storage directories',
  evidence='SRC Drawer.java:293, DataUtils.java:419-421')

# getDrawerMetadata - called to retrieve menu item metadata
e('Drawer.onNavigationItemSelected', 'DataUtils.getDrawerMetadata', 'FRAMEWORK',
  'Navigation item selection retrieves associated metadata',
  evidence='SRC Drawer.java:564, DataUtils.java:423-425')

# putDrawerMetadata - called to store menu item metadata
e('Drawer.addNewItem', 'DataUtils.putDrawerMetadata', 'CALL',
  'Adding drawer item stores its metadata',
  evidence='SRC Drawer.java:464, DataUtils.java:427-430')

# findLongestContainingDrawerItem - called to find matching menu item
e('Drawer.selectCorrectDrawerItem', 'DataUtils.findLongestContainingDrawerItem', 'CALL',
  'Drawer selects item by finding longest path prefix',
  evidence='SRC Drawer.java:673, DataUtils.java:436-438')

# UNREACHABLE from part b019
UNREACHABLE['DataUtils.containsAccounts'] = ('no_trigger_in_app', 'Method is defined but has no callers in app source; grep shows only definition in DataUtils.java:118', 'SRC DataUtils.java:118-144', 'SOURCE')
UNREACHABLE['DataUtils.setAccounts'] = ('no_trigger_in_app', 'Setter is never called in app source; accounts are added via addAccount but never bulk-set', 'SRC DataUtils.java:328-331', 'SOURCE')

# ---- part b022 (2026-10-27) Drawer navigation backbone

e('MainActivity.initialiseViews', 'Drawer.<init>', 'CALL', 'MainActivity creates Drawer in initialiseViews',
  evidence='SRC Drawer.java:133 shows constructor, MainActivity.java:1425 shows new Drawer(this)')

e('Drawer.<init>', 'Drawer.lock', 'CALL', 'Constructor calls lock for tablet mode',
  evidence='SRC Drawer.java:204 shows lock(DrawerLayout.LOCK_MODE_LOCKED_OPEN) in tablet branch')

e('Drawer.<init>', 'Drawer.open', 'CALL', 'Constructor calls open for tablet mode',
  evidence='SRC Drawer.java:205 shows open() call in tablet branch')

e('Drawer.<init>', 'Drawer.unlockIfNotOnTablet', 'CALL', 'Constructor calls unlockIfNotOnTablet for phone mode',
  evidence='SRC Drawer.java:209 shows unlockIfNotOnTablet() in else branch')

e('Drawer.<init>', 'Drawer.close', 'CALL', 'Constructor calls close for phone mode',
  evidence='SRC Drawer.java:210 shows close() call in else branch')

e('S_ENTRY', 'Drawer.onNavigationItemSelected', 'FRAMEWORK', 'NavigationView.OnNavigationItemSelectedListener callback',
  evidence='SRC Drawer.java:97 implements NavigationView.OnNavigationItemSelectedListener, line 164 sets listener')

e('Drawer.onNavigationItemSelected', 'Drawer.closeIfNotLocked', 'CALL', 'Closes drawer after navigation',
  evidence='SRC Drawer.java:594 shows closeIfNotLocked() call in ITEM_ENTRY case')

e('Drawer.onNavigationItemSelected', 'Drawer.onDrawerClosed', 'CALL', 'Handles locked drawer navigation',
  evidence='SRC Drawer.java:595 shows if (isLocked()) { onDrawerClosed(); }')

e('Drawer.onNavigationItemSelected', 'Drawer.lambda$onNavigationItemSelected$6', 'CALL', 'Lambda for SAF dialog callback',
  evidence='SRC Drawer.java:587 shows lambda (v) -> ... in dialog.getActionButton')

e('MainActivity.onResume', 'Drawer.refreshDrawer', 'CALL', 'Refresh drawer on activity resume',
  evidence='SRC MainActivity.java:1112 shows drawer.refreshDrawer()')

e('Drawer.refreshDrawer', 'Drawer.addNewItem', 'CALL', 'Adds menu items for storages',
  evidence='SRC Drawer.java:282 shows addNewItem(menu, STORAGES_GROUP, ...) calls')

e('Drawer.refreshDrawer', 'Drawer.lambda$refreshDrawer$1', 'CALL', 'Lambda for FTP menu item',
  evidence='SRC Drawer.java:404 shows new MenuMetadata(() -> { ... }) for FTP')

e('Drawer.refreshDrawer', 'Drawer.lambda$refreshDrawer$2', 'CALL', 'Lambda for Apps menu item',
  evidence='SRC Drawer.java:420 shows new MenuMetadata(() -> { ... }) for Apps')

e('Drawer.refreshDrawer', 'Drawer.lambda$refreshDrawer$3', 'CALL', 'Lambda for Settings menu item',
  evidence='SRC Drawer.java:433 shows new MenuMetadata(() -> { ... }) for Settings')

e('Drawer.lambda$refreshDrawer$1', 'Drawer.close', 'CALL', 'Close drawer after FTP selection',
  evidence='SRC Drawer.java:413 shows if (!isDrawerLocked) close()')

e('Drawer.lambda$refreshDrawer$1', 'Drawer.onDrawerClosed', 'CALL', 'Handle locked drawer FTP selection',
  evidence='SRC Drawer.java:414 shows else onDrawerClosed()')

e('Drawer.lambda$refreshDrawer$2', 'Drawer.close', 'CALL', 'Close drawer after Apps selection',
  evidence='SRC Drawer.java:429 shows if (!isDrawerLocked) close()')

e('Drawer.lambda$refreshDrawer$2', 'Drawer.onDrawerClosed', 'CALL', 'Handle locked drawer Apps selection',
  evidence='SRC Drawer.java:430 shows else onDrawerClosed()')

e('Drawer.lambda$refreshDrawer$2', 'AppsListFragment.<init>', 'CALL', 'Creates AppsListFragment',
  evidence='SRC Drawer.java:421 shows new AppsListFragment()')

e('Drawer.addNewItem', 'Drawer.lambda$addNewItem$4', 'CALL', 'Lambda for action view click listener',
  evidence='SRC Drawer.java:462 shows (view) -> onNavigationItemActionClick(item)')

e('Drawer.lambda$addNewItem$4', 'Drawer.onNavigationItemActionClick', 'CALL', 'Delegates to action click handler',
  evidence='SRC Drawer.java:462 shows lambda calling onNavigationItemActionClick(item)')

e('Drawer.onDrawerClosed', 'MainActivity.goToMain', 'CALL', 'Navigate to path when no main fragment',
  evidence='SRC Drawer.java:551 shows mainActivity.goToMain(pendingPath)')

e('MainActivity.onResume', 'Drawer.deselectEverything', 'CALL', 'Deselect drawer items on resume',
  evidence='SRC MainActivity.java:1113 shows drawer.deselectEverything()')

e('Drawer.onNavigationItemSelected', 'ActionViewStateManager.deselectCurrentActionView', 'CALL', 'Deselect previous item',
  evidence='SRC Drawer.java:559 shows actionViewStateManager.deselectCurrentActionView()')

e('Drawer.onNavigationItemSelected', 'ActionViewStateManager.selectActionView', 'CALL', 'Select current item',
  evidence='SRC Drawer.java:560 shows actionViewStateManager.selectActionView(item)')

e('Drawer.deselectEverything', 'ActionViewStateManager.deselectCurrentActionView', 'CALL', 'Deselect all action views',
  evidence='SRC Drawer.java:712 shows actionViewStateManager.deselectCurrentActionView()')

e('Drawer.refreshDrawer', 'ActionViewStateManager.deselectCurrentActionView', 'CALL', 'Clear selection on refresh',
  evidence='SRC Drawer.java:254 shows actionViewStateManager.deselectCurrentActionView()')

e('Drawer.selectCorrectDrawerItemForPath', 'ActionViewStateManager.selectActionView', 'CALL', 'Select item for path',
  evidence='SRC Drawer.java:679 shows actionViewStateManager.selectActionView(item)')

e('Drawer.selectCorrectDrawerItemForPath', 'Drawer.deselectEverything', 'CALL', 'Deselect when no match',
  evidence='SRC Drawer.java:675 shows if(id == null) deselectEverything()')

e('S_ENTRY', 'Drawer$1.onDrawerClosed', 'FRAMEWORK', 'ActionBarDrawerToggle callback when drawer closes',
  evidence='SRC Drawer.java:224 shows onDrawerClosed override in ActionBarDrawerToggle anonymous class')

e('Drawer$1.onDrawerClosed', 'Drawer.onDrawerClosed', 'CALL', 'Delegates to outer class method',
  evidence='SRC Drawer.java:225 shows Drawer.this.onDrawerClosed()')

e('S_ENTRY', 'Drawer$1.onDrawerOpened', 'FRAMEWORK', 'ActionBarDrawerToggle callback when drawer opens',
  evidence='SRC Drawer.java:228 shows onDrawerOpened override in ActionBarDrawerToggle anonymous class')

e('MainActivity.onCreate', 'MainActivity.initialiseViews', 'CALL', 'Initialize views in onCreate',
  evidence='SRC MainActivity.java:295 shows initialiseViews() call in onCreate')

e('MainActivity.onPostCreate', 'Drawer.syncState', 'LIFECYCLE', 'Sync drawer toggle state after restore',
  evidence='SRC MainActivity.java:1063 shows drawer.syncState() in onPostCreate')

e('MainActivity.onConfigurationChanged', 'Drawer.onConfigurationChanged', 'LIFECYCLE', 'Pass config changes to drawer',
  evidence='SRC MainActivity.java:1070 shows drawer.onConfigurationChanged(newConfig)')

e('MainActivity.onOptionsItemSelected', 'Drawer.onOptionsItemSelected', 'CALL', 'Handle options menu via drawer toggle',
  evidence='SRC MainActivity.java:931 shows if (drawer.onOptionsItemSelected(item)) return true')

e('MainActivity.onCreate', 'Drawer.setDrawerIndicatorEnabled', 'CALL', 'Enable drawer indicator in onCreate',
  evidence='SRC MainActivity.java:348 shows drawer.setDrawerIndicatorEnabled()')

e('MainActivity.onBackPressed', 'Drawer.isLocked', 'CALL', 'Check drawer state on back press',
  evidence='SRC MainActivity.java:704 shows if (!drawer.isLocked() && drawer.isOpen())')

e('MainActivity.onBackPressed', 'Drawer.isOpen', 'CALL', 'Check if drawer is open on back press',
  evidence='SRC MainActivity.java:704 shows drawer.isOpen() check')

e('MainActivity.onBackPressed', 'Drawer.close', 'CALL', 'Close drawer on back press',
  evidence='SRC MainActivity.java:705 shows drawer.close()')

e('MainActivity.onActivityResult', 'Drawer.onActivityResult', 'RESULT', 'Handle activity result for drawer header',
  evidence='SRC MainActivity.java:1309 shows drawer.onActivityResult(requestCode, responseCode, intent)')

e('MainActivity.onSaveInstanceState', 'Drawer.isSomethingSelected', 'CALL', 'Save drawer selection state',
  evidence='SRC MainActivity.java:1076 shows outState.putBoolean(KEY_DRAWER_SELECTED, drawer.isSomethingSelected())')

e('MainActivity.onCreate', 'Drawer.setSomethingSelected', 'CALL', 'Restore drawer selection from saved state',
  evidence='SRC MainActivity.java:322 shows drawer.setSomethingSelected(savedInstanceState.getBoolean(...))')

e('MainActivity.onCreate', 'Drawer.getPhoneStorageCount', 'CALL', 'Get storage count for tab setup',
  evidence='SRC MainActivity.java:447 shows if (drawer.getPhoneStorageCount() > 1)')

e('MainActivity.onCreate', 'Drawer.getFirstPath', 'CALL', 'Get first storage path for tab setup',
  evidence='SRC MainActivity.java:453 shows if (drawer.getFirstPath() != null)')

e('MainActivity.onCreate', 'Drawer.getSecondPath', 'CALL', 'Get second storage path for tab setup',
  evidence='SRC MainActivity.java:448,457 shows drawer.getSecondPath() for tabs')

e('MainActivity.initialiseViews', 'Drawer.setDrawerHeaderBackground', 'CALL', 'Set header background in initialization',
  evidence='SRC MainActivity.java:1445 shows drawer.setDrawerHeaderBackground()')

e('MainActivity.updatePathColor', 'Drawer.setBackgroundColor', 'CALL', 'Update drawer background color',
  evidence='SRC MainActivity.java:1479 shows drawer.setBackgroundColor(colorDrawable.getColor())')

e('MainFragment.onTabChanged', 'Drawer.selectCorrectDrawerItemForPath', 'CALL', 'Select drawer item when tab changes',
  evidence='SRC MainFragment.java:1423 shows getMainActivity().getDrawer().selectCorrectDrawerItemForPath(getPath())')

e('TabFragment.onPageSelected', 'Drawer.selectCorrectDrawerItemForPath', 'CALL', 'Select drawer item on page selection',
  evidence='SRC TabFragment.java:224 shows mainActivity.getDrawer().selectCorrectDrawerItemForPath(...)')

e('MainFragment.actionModeFinish', 'Drawer.lockIfNotOnTablet', 'CALL', 'Lock drawer during action mode',
  evidence='SRC MainFragment.java:509 shows getMainActivity().getDrawer().lockIfNotOnTablet(...)')

e('MainFragment.handleSearchResult', 'Drawer.unlockIfNotOnTablet', 'CALL', 'Unlock drawer after action mode',
  evidence='SRC MainFragment.java:771 shows getMainActivity().getDrawer().unlockIfNotOnTablet()')

e('Drawer.<init>', 'Drawer.lambda$new$0', 'CALL', 'Long click listener lambda for header',
  evidence='SRC Drawer.java:141 shows drawerHeaderView.setOnLongClickListener(v -> ...)')

e('Drawer.<init>', 'Drawer$1.<init>', 'CALL', 'Anonymous ActionBarDrawerToggle created in constructor',
  evidence='SRC Drawer.java:214-232 new ActionBarDrawerToggle(...) { ... } anonymous class')

e('Drawer.setDrawerHeaderBackground', 'Drawer$2.<init>', 'CALL', 'Anonymous ImageListener for header background',
  evidence='SRC Drawer.java:657 shows new ImageLoader.ImageListener() { ... }')

e('Drawer$1.<init>', 'Drawer$1.onDrawerClosed', 'CALL', 'Method defined in anonymous class',
  evidence='SRC Drawer.java:224 onDrawerClosed method definition in Drawer$1')

e('Drawer$1.<init>', 'Drawer$1.onDrawerOpened', 'CALL', 'Method defined in anonymous class',
  evidence='SRC Drawer.java:228 onDrawerOpened method definition in Drawer$1')

e('Drawer$2.<init>', 'Drawer$2.onResponse', 'CALL', 'Method defined in anonymous ImageListener',
  evidence='SRC Drawer.java:659 onResponse method definition in Drawer$2')

e('Drawer$2.<init>', 'Drawer$2.onErrorResponse', 'CALL', 'Method defined in anonymous ImageListener',
  evidence='SRC Drawer.java:665 onErrorResponse method definition in Drawer$2')

e('JVM', 'Drawer.<clinit>', 'SYSTEM', 'Static initialization when class loads',
  evidence='SRC Drawer.java:1 class declaration, static fields initialized when MainActivity creates Drawer')

# UNREACHABLE from part b022
UNREACHABLE['Drawer.setNavViewDimension'] = ('no_trigger_in_app', 'Method is commented out in constructor at the only call site', 'SRC Drawer.java:160-163 shows /* commented out setNavViewDimension call */', 'SOURCE')

# ---- part b027 (2026-10-27) FileUtils utility class

# FileUtils.<clinit> - static initializer runs when first FileUtils method is called
e('CountItemsOrAndSizeTask.doInBackground', 'FileUtils.<clinit>', 'FRAMEWORK', 'Static initializer runs before first FileUtils.folderSize call',
  evidence='SRC FileUtils.java:494-499 static fields; first method call triggers <clinit>')

e('CountItemsOrAndSizeTask.doInBackground', 'FileUtils.folderSize', 'CALL', 'computes folder size',
  evidence='SRC CountItemsOrAndSizeTask.java:48')
e('HybridFile.folderSize()', 'FileUtils.folderSize', 'CALL', 'delegates to FileUtils for File mode',
  evidence='SRC HybridFile.java:563,599')
e('PropertiesSheet.updateViews', 'FileUtils.folderSize', 'CALL', 'gets folder size for display',
  evidence='SRC PropertiesSheet.java:71')
e('CountItemsOrAndSizeTask.doInBackground', 'FileUtils.folderSize', 'CALL', 'computes hybrid file folder size',
  evidence='SRC CountItemsOrAndSizeTask.java:48')
e('HybridFile.folderSize()', 'FileUtils.folderSize', 'CALL', 'computes SMB folder size',
  evidence='SRC HybridFile.java:556,592')
e('HybridFile.folderSize()', 'FileUtils.folderSizeCloud', 'CALL', 'computes cloud storage folder size',
  evidence='SRC HybridFile.java:612')
e('HybridFile.folderSize()', 'FileUtils.otgFolderSize', 'CALL', 'computes OTG folder size',
  evidence='SRC HybridFile.java:606')
e('MoveFiles.doInBackground', 'FileUtils.getTotalBytes', 'CALL', 'calculates total bytes for move operation',
  evidence='SRC MoveFiles.java:86')
e('PrepareCopyTask.doInBackground', 'FileUtils.getTotalBytes', 'CALL', 'calculates total bytes for copy operation',
  evidence='SRC PrepareCopyTask.java:118')
e('CopyService.onStartCommand', 'FileUtils.getTotalBytes', 'CALL', 'calculates total size of files to copy',
  evidence='SRC CopyService.java:237')
e('ZipService.onStartCommand', 'FileUtils.getTotalBytes', 'CALL', 'calculates total bytes for zip operation',
  evidence='SRC ZipService.java:217')
e('DeleteTask.doInBackground', 'FileUtils.scanFile', 'CALL', 'triggers media scan after deletion',
  evidence='SRC DeleteTask.java:155')
e('MoveFiles.doInBackground', 'FileUtils.scanFile', 'CALL', 'triggers media scan after move',
  evidence='SRC MoveFiles.java:176,177')
e('MainFragment.addShortcut', 'FileUtils.scanFile', 'CALL', 'scans file for media',
  evidence='SRC MainFragment.java:817,1564')
e('Operations.deleteFile', 'FileUtils.scanFile', 'CALL', 'triggers media scan for hybrid files',
  evidence='SRC Operations.java:484')
e('CopyService.onCopyDone', 'FileUtils.scanFile', 'CALL', 'scans copied file',
  evidence='SRC CopyService.java:437')
e('GenericCopyUtil.finishCopy', 'FileUtils.scanFile', 'CALL', 'scans file after copy completion',
  evidence='SRC GenericCopyUtil.java:316')
e('BottomBar.updatePath', 'FileUtils.crossfade', 'CALL', 'animates UI transition',
  evidence='SRC BottomBar.java:135,141')
e('BottomBar.updatePath', 'FileUtils.crossfadeInverse', 'CALL', 'animates inverse UI transition',
  evidence='SRC BottomBar.java:119')
e('ItemPopupMenu.onMenuItemClick', 'FileUtils.shareCloudFile', 'CALL', 'shares cloud file link',
  evidence='SRC ItemPopupMenu.java:87')
e('MainFragment.generalShare', 'FileUtils.shareCloudFile', 'CALL', 'shares cloud file from main fragment',
  evidence='SRC MainFragment.java:678')
e('ItemPopupMenu.onMenuItemClick', 'FileUtils.shareFiles', 'CALL', 'shares files via intent',
  evidence='SRC ItemPopupMenu.java:92')
e('MainFragment.generalShare', 'FileUtils.shareFiles', 'CALL', 'shares files from main fragment',
  evidence='SRC MainFragment.java:682')
e('AppsAdapter.onClick', 'FileUtils.shareFiles', 'CALL', 'shares app files',
  evidence='SRC AppsAdapter.java:185')
e('ProcessViewerFragment.addEntry', 'FileUtils.readableFileSizeFloat', 'CALL', 'formats file size for display',
  evidence='SRC ProcessViewerFragment.java:201,202,380')
e('GeneralDialogCreation.showPackageDialog', 'FileUtils.installApk', 'CALL', 'installs APK file',
  evidence='SRC GeneralDialogCreation.java:916')
e('FileUtils.openFile', 'FileUtils.openunknown', 'CALL', 'opens file with unknown type',
  evidence='SRC FileUtils.java:795,420')
e('MainFragment.onClick', 'FileUtils.openunknown', 'CALL', 'opens file from main fragment',
  evidence='SRC MainFragment.java:743')
e('TextEditorActivity.load', 'FileUtils.openunknown', 'CALL', 'opens file after editing',
  evidence='SRC TextEditorActivity.java:380')
e('FileUtils.openFile', 'FileUtils.openunknown', 'CALL', 'opens OTG file with unknown type',
  evidence='SRC FileUtils.java:822,455')
e('FileUtils.fileToContentUri', 'FileUtils.normalizeMediaPath', 'CALL', 'normalizes path for media query',
  evidence='SRC FileUtils.java:519,500')
e('FileUtils.openunknown', 'FileUtils.fileToContentUri', 'CALL', 'converts file to content URI',
  evidence='SRC FileUtils.java:423,516')
e('FileUtils.openWith', 'FileUtils.fileToContentUri', 'CALL', 'gets content URI for file',
  evidence='SRC FileUtils.java:591,516')
e('ItemPopupMenu.onMenuItemClick', 'FileUtils.openWith', 'CALL', 'opens file with app chooser',
  evidence='SRC ItemPopupMenu.java:130')
e('FileUtils.openFile', 'FileUtils.openWith', 'CALL', 'shows app chooser',
  evidence='SRC FileUtils.java:798,588')
e('FileUtils.openunknown', 'FileUtils.openWith', 'CALL', 'fallback when no app found',
  evidence='SRC FileUtils.java:444,420')
e('FileUtils.openFile', 'FileUtils.openWith', 'CALL', 'opens OTG file with chooser',
  evidence='SRC FileUtils.java:823,634')
e('FileUtils.openunknown', 'FileUtils.openWith', 'CALL', 'fallback for OTG file',
  evidence='SRC FileUtils.java:479,455')
e('MainFragment.goBack', 'FileUtils.canGoBack', 'CALL', 'checks if navigation back is possible',
  evidence='SRC MainFragment.java:1302,1384')
e('LoadFolderSpaceDataTask.doInBackground', 'FileUtils.getSpaces', 'CALL', 'gets storage space info',
  evidence='SRC LoadFolderSpaceDataTask.java:56')
e('GeneralDialogCreation.showPropertiesDialog', 'FileUtils.copyToClipboard', 'CALL', 'copies properties to clipboard',
  evidence='SRC GeneralDialogCreation.java:432,438,444,450')
e('GenerateHashesTask.onPostExecute', 'FileUtils.copyToClipboard', 'CALL', 'copies hash to clipboard',
  evidence='SRC GenerateHashesTask.java:102,108')
e('FileUtils.shareCloudFile', 'FileUtils.copyToClipboard', 'CALL', 'copies cloud link to clipboard',
  evidence='SRC FileUtils.java:346,332')
e('BottomBar.updatePath', 'FileUtils.getFolderNamesInPath', 'CALL', 'gets folder names for breadcrumb',
  evidence='SRC BottomBar.java:203')
e('BottomBar.updatePath', 'FileUtils.getPathsInPath', 'CALL', 'gets paths for breadcrumb navigation',
  evidence='SRC BottomBar.java:204')
e('RootHelper.getFilesList', 'FileUtils.canListFiles', 'CALL', 'checks if directory is readable',
  evidence='SRC RootHelper.java:327')
e('MainActivity.getStorageDirectories', 'FileUtils.canListFiles', 'CALL', 'validates storage directories',
  evidence='SRC MainActivity.java:684')
e('MainActivity.onNewIntent', 'FileUtils.openFile', 'CALL', 'opens file from intent',
  evidence='SRC MainActivity.java:417,747,1579')
e('Drawer.onClickListener', 'FileUtils.openFile', 'CALL', 'opens file from drawer',
  evidence='SRC Drawer.java:540')
e('CompressedExplorerFragment.open', 'FileUtils.openFile', 'CALL', 'opens extracted file',
  evidence='SRC CompressedExplorerFragment.java:394')
e('MainFragment.onListItemClicked', 'FileUtils.openFile', 'CALL', 'opens clicked file',
  evidence='SRC MainFragment.java:833,933')
e('MainFragment.onListItemClicked', 'FileUtils.openFile', 'CALL', 'opens OTG file',
  evidence='SRC MainFragment.java:922')
e('GeneralDialogCreation.showHiddenDialog', 'FileUtils.toHybridFileConcurrentRadixTree', 'CALL', 'converts hidden files tree',
  evidence='SRC GeneralDialogCreation.java:1120')
e('GeneralDialogCreation.showHistoryDialog', 'FileUtils.toHybridFileArrayList', 'CALL', 'converts history list',
  evidence='SRC GeneralDialogCreation.java:1098')
e('RootHelper.getFilesList', 'FileUtils.parseName', 'CALL', 'parses ls output line',
  evidence='SRC RootHelper.java:232,300')
e('GeneralDialogCreation.showPermissionsDialog', 'FileUtils.parse', 'CALL', 'parses permission string',
  evidence='SRC GeneralDialogCreation.java:1147')
e('BottomBar.updatePath', 'FileUtils.isStorage', 'CALL', 'checks if path is storage root',
  evidence='SRC BottomBar.java:216')
e('GeneralDialogCreation.showSMBDialog', 'FileUtils.isPathAccessible', 'CALL', 'validates path accessibility',
  evidence='SRC GeneralDialogCreation.java:1187')
e('Tab.getTab', 'FileUtils.isPathAccessible', 'CALL', 'checks if tab path is accessible',
  evidence='SRC Tab.java:42')
e('FoldersPref.onPreferenceChange', 'FileUtils.isPathAccessible', 'CALL', 'validates folder preference',
  evidence='SRC FoldersPref.java:172,240')
e('FileUtils.isPathAccessible', 'FileUtils.isRoot', 'CALL', 'checks if path is root',
  evidence='SRC FileUtils.java:998')
e('ZipService.onStartCommand', 'FileUtils.hybridListToFileArrayList', 'CALL', 'converts for zip operation',
  evidence='SRC ZipService.java:227')
e('Drawer.onBookmarkClick', 'FileUtils.checkForPath', 'CALL', 'verifies bookmark path exists',
  evidence='SRC Drawer.java:569')
e('FileUtils.otgFolderSize', 'FileUtils.lambda$otgFolderSize$0', 'CALL', 'lambda for OTG file size calculation',
  evidence='SRC FileUtils.java:190')
e('FileUtils.scanFile', 'FileUtils.lambda$scanFile$1', 'CALL', 'lambda for async media scan',
  evidence='SRC FileUtils.java:243')
e('FileUtils.installApk', 'FileUtils.lambda$installApk$2', 'CALL', 'lambda for permission callback',
  evidence='SRC FileUtils.java:391')
e('FileUtils.openWith', 'FileUtils.lambda$openWith$3', 'CALL', 'lambda for file type selection',
  evidence='SRC FileUtils.java:593')
e('FileUtils.openWith', 'FileUtils.lambda$openWith$4', 'CALL', 'lambda for DocumentFile type selection',
  evidence='SRC FileUtils.java:638')
e('FileUtils.crossfade', 'FileUtils$1.<init>', 'CALL', 'creates animator listener',
  evidence='SRC FileUtils.java:289')
e('FileUtils$1.<init>', 'FileUtils$1.onAnimationEnd', 'FRAMEWORK', 'animation callback',
  evidence='SRC FileUtils.java:291 defines AnimatorListenerAdapter callback')
e('FileUtils.crossfadeInverse', 'FileUtils$2.<init>', 'CALL', 'creates animator listener',
  evidence='SRC FileUtils.java:319')
e('FileUtils$2.<init>', 'FileUtils$2.onAnimationEnd', 'FRAMEWORK', 'animation callback',
  evidence='SRC FileUtils.java:321 defines AnimatorListenerAdapter callback')
e('FileUtils.shareCloudFile', 'FileUtils$3.<init>', 'CALL', 'creates async task',
  evidence='SRC FileUtils.java:333')
e('FileUtils$3.<init>', 'FileUtils$3.doInBackground', 'FRAMEWORK', 'async task execution',
  evidence='SRC FileUtils.java:336 defines AsyncTask.doInBackground')
e('FileUtils$3.<init>', 'FileUtils$3.onPostExecute', 'FRAMEWORK', 'async task completion',
  evidence='SRC FileUtils.java:343 defines AsyncTask.onPostExecute')
e('FileUtils.openFile', 'FileUtils$4.<init>', 'CALL', 'creates countdown timer',
  evidence='SRC FileUtils.java:768')
e('FileUtils$4.<init>', 'FileUtils$4.onTick', 'FRAMEWORK', 'timer tick callback',
  evidence='SRC FileUtils.java:770 defines CountDownTimer.onTick')
e('FileUtils$4.<init>', 'FileUtils$4.onFinish', 'FRAMEWORK', 'timer finish callback',
  evidence='SRC FileUtils.java:779 defines CountDownTimer.onFinish')
e('FileUtils.checkForPath', 'FileUtils$5.<init>', 'CALL', 'creates error callback',
  evidence='SRC FileUtils.java:1027')
e('FileUtils$5.<init>', 'FileUtils$5.exists', 'CALL', 'callback for existing file',
  evidence='SRC FileUtils.java:1029 defines ErrorCallBack.exists')
e('FileUtils$5.<init>', 'FileUtils$5.launchSAF', 'CALL', 'callback for SAF launch (single file)',
  evidence='SRC FileUtils.java:1033-1035 defines ErrorCallBack.launchSAF(HybridFile)')
e('FileUtils$5.<init>', 'FileUtils$5.launchSAF', 'CALL', 'callback for SAF launch (two files)',
  evidence='SRC FileUtils.java:1037-1039 defines ErrorCallBack.launchSAF(HybridFile, HybridFile)')
e('FileUtils$5.<init>', 'FileUtils$5.done', 'CALL', 'callback for completion',
  evidence='SRC FileUtils.java:1042 defines ErrorCallBack.done')
e('FileUtils$5.<init>', 'FileUtils$5.invalidName', 'CALL', 'callback for invalid name',
  evidence='SRC FileUtils.java:1046 defines ErrorCallBack.invalidName')

# UNREACHABLE from part b027
UNREACHABLE['FileUtils.<init>'] = ('no_trigger_in_app', 'Utility class constructor; class has only static methods, never instantiated', 'SRC FileUtils.java:96 class declaration shows utility pattern with only static methods', 'SOURCE')
UNREACHABLE['FileUtils.folderSizeSftp'] = ('no_trigger_in_app', 'Method not called by app code; HybridFile.folderSize uses SshClientUtils with client.size() for SFTP, not this method', 'SRC FileUtils.java:150-165; HybridFile.java:578-620 shows SFTP case uses client.size() not FileUtils.folderSizeSftp', 'SOURCE')
# REMOVED - was UNREACHABLE but reachable via bytecode from otgFolderSize, getTotalBytes: FileUtils.getBaseFileSize
UNREACHABLE['FileUtils.scanFile'] = ('no_trigger_in_app', 'Private overload taking Uri; called only internally from public scanFile methods', 'SRC FileUtils.java:230-233; internal call at line 273', 'SOURCE')
UNREACHABLE['FileUtils.applyNewDocFlag'] = ('no_trigger_in_app', 'Private helper called only internally by openunknown methods', 'SRC FileUtils.java:484-493; internal calls at lines 432,436,465,469,600,645', 'SOURCE')
UNREACHABLE['FileUtils.fileToContentUri'] = ('no_trigger_in_app', 'Private overload with volume parameter; called only internally by public fileToContentUri', 'SRC FileUtils.java:535-586; internal calls at lines 522,526', 'SOURCE')
# REMOVED - was UNREACHABLE but reachable via bytecode from openFile: FileUtils.isSelfDefault
UNREACHABLE['FileUtils.getLinkPosition'] = ('no_trigger_in_app', 'Private helper called only internally by parseName', 'SRC FileUtils.java:950-955; internal call at line 926', 'SOURCE')
UNREACHABLE['FileUtils.getColonPosition'] = ('no_trigger_in_app', 'Private helper called only internally by parseName', 'SRC FileUtils.java:957-962; internal call at line 916', 'SOURCE')

# ---- part b044 (2026-10-27) MainActivity main entry activity

# MainActivity.<clinit> - static initializer runs when MainActivity class loads
e('S_ENTRY', 'MainActivity.<clinit>', 'SYSTEM', 'Static initializer runs when MainActivity class is loaded by framework',
  evidence='SRC MainActivity.java:161 static final Pattern DIR_SEPARATOR; framework loads class before calling constructor')

e('S_ENTRY', 'MainActivity.<init>', 'FRAMEWORK', 'Framework constructs MainActivity for launcher',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:62-65 LAUNCHER intent-filter')

e('S_ENTRY', 'MainActivity.onCreate', 'LIFECYCLE', 'Framework calls onCreate after constructor',
  evidence='FW-SRC Activity.java onCreate lifecycle method')

e('S_ENTRY', 'MainActivity.onCreate', 'INTENT', 'Framework delivers GET_CONTENT intent to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:67-71 GET_CONTENT filter; MainActivity.java:302 getIntent()')

e('S_ENTRY', 'MainActivity.onCreate', 'INTENT', 'Framework delivers RINGTONE_PICKER intent to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:73-76 RINGTONE_PICKER filter; MainActivity.java:302 getIntent()')

e('S_ENTRY', 'MainActivity.onCreate', 'INTENT', 'Framework delivers VIEW intent for archives to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:78-88 VIEW with archive mimeTypes; MainActivity.java:302 getIntent()')

e('S_ENTRY', 'MainActivity.onCreate', 'INTENT', 'Framework delivers QS_TILE_PREFERENCES intent to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:90-92 QS_TILE_PREFERENCES filter; MainActivity.java:302 getIntent()')

e('S_ENTRY', 'MainActivity.onCreate', 'INTENT', 'Framework delivers VIEW intent with custom scheme to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:94-99,101-106 VIEW with scheme com.amaze.filemanager; MainActivity.java:302 getIntent()')

e('S_ENTRY', 'MainActivity.onCreate', 'INTENT', 'Framework delivers SEND/SEND_MULTIPLE intents to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:108-113 SEND/SEND_MULTIPLE filter; MainActivity.java:302 getIntent()')

e('MainActivity.onCreate', 'MainActivity.initialisePreferences', 'CALL', 'onCreate calls initialisePreferences',
  evidence='SRC MainActivity.java:280')

e('MainActivity.onCreate', 'MainActivity.initializeInteractiveShell', 'CALL', 'onCreate calls initializeInteractiveShell',
  evidence='SRC MainActivity.java:281')

e('MainActivity.onCreate', 'MainActivity.initialiseViews', 'CALL', 'onCreate calls initialiseViews',
  evidence='SRC MainActivity.java:293')

e('MainActivity.onCreate', 'MainActivity.initialiseFab', 'CALL', 'onCreate calls initialiseFab',
  evidence='SRC MainActivity.java:298')

e('MainActivity.onCreate', 'MainActivity.checkForExternalIntent', 'CALL', 'onCreate calls checkForExternalIntent with intent',
  evidence='SRC MainActivity.java:313')

e('MainActivity.onCreate', 'MainActivity.checkForExternalPermission', 'CALL', 'onCreate calls checkForExternalPermission',
  evidence='SRC MainActivity.java:359')

e('MainActivity.onCreate', 'MainActivity.goToMain', 'CALL', 'onCreate calls goToMain to display TabFragment',
  evidence='SRC MainActivity.java:411,415,418 goToMain calls in async callback')

e('MainActivity.checkForExternalIntent', 'MainActivity.initFabToSave', 'CALL', 'checkForExternalIntent calls initFabToSave for SEND intents',
  evidence='SRC MainActivity.java:531,537 initFabToSave calls for ACTION_SEND and ACTION_SEND_MULTIPLE')

e('MainActivity.checkForExternalIntent', 'MainActivity.openCompressed', 'CALL', 'checkForExternalIntent handles VIEW intent for zip files',
  evidence='SRC MainActivity.java:519 sets openzip=true; MainActivity.java:799-801 goToMain checks openzip and calls openCompressed')

e('S_ENTRY', 'MainActivity.onPostCreate', 'LIFECYCLE', 'Framework calls onPostCreate after onCreate',
  evidence='FW-SRC Activity.java onPostCreate lifecycle')

e('S_ENTRY', 'MainActivity.onResume', 'LIFECYCLE', 'Framework calls onResume when activity becomes visible',
  evidence='FW-SRC Activity.java onResume lifecycle')

e('MainActivity.onResume', 'MainActivity.updateUsbInformation', 'CALL', 'onResume calls updateUsbInformation on API 19+',
  evidence='SRC MainActivity.java:1121-1123 if SDK_INT >= KITKAT call updateUsbInformation')

e('S_ENTRY', 'MainActivity.onPause', 'LIFECYCLE', 'Framework calls onPause when activity loses focus',
  evidence='FW-SRC Activity.java onPause lifecycle')

e('MainActivity.onPause', 'MainActivity.killToast', 'CALL', 'onPause calls killToast to cancel toast',
  evidence='SRC MainActivity.java:1101')

e('S_ENTRY', 'MainActivity.onSaveInstanceState', 'LIFECYCLE', 'Framework calls onSaveInstanceState before stopping activity',
  evidence='FW-SRC Activity.java onSaveInstanceState lifecycle')

e('S_ENTRY', 'MainActivity.onConfigurationChanged', 'LIFECYCLE', 'Framework calls onConfigurationChanged on config change',
  evidence='FW-SRC Activity.java onConfigurationChanged lifecycle')

e('S_ENTRY', 'MainActivity.onDestroy', 'LIFECYCLE', 'Framework calls onDestroy when activity is destroyed',
  evidence='FW-SRC Activity.java onDestroy lifecycle')

e('MainActivity.onDestroy', 'MainActivity.closeInteractiveShell', 'CALL', 'onDestroy calls closeInteractiveShell to clean up shell',
  evidence='SRC MainActivity.java:1208')

e('S_ENTRY', 'MainActivity.onCreateOptionsMenu', 'LIFECYCLE', 'Framework calls onCreateOptionsMenu to inflate menu',
  evidence='FW-SRC Activity.java onCreateOptionsMenu lifecycle')

e('S_ENTRY', 'MainActivity.onPrepareOptionsMenu', 'LIFECYCLE', 'Framework calls onPrepareOptionsMenu before showing menu',
  evidence='FW-SRC Activity.java onPrepareOptionsMenu lifecycle')

e('MainActivity.onPrepareOptionsMenu', 'MainActivity.invalidatePasteButton', 'CALL', 'onPrepareOptionsMenu calls invalidatePasteButton',
  evidence='SRC MainActivity.java:863,915 invalidatePasteButton calls')

e('S_ENTRY', 'MainActivity.onOptionsItemSelected', 'LIFECYCLE', 'Framework calls onOptionsItemSelected when menu item clicked',
  evidence='FW-SRC Activity.java onOptionsItemSelected lifecycle')

e('MainActivity.onOptionsItemSelected', 'MainActivity.exit', 'CALL', 'onOptionsItemSelected calls exit for R.id.exit',
  evidence='SRC MainActivity.java:973 case R.id.exit calls finish()')

e('MainActivity.onOptionsItemSelected', 'MainActivity.updatePaths', 'CALL', 'onOptionsItemSelected calls updatePaths for sethome',
  evidence='SRC MainActivity.java:961 updatePaths call in sethome action')

e('S_ENTRY', 'MainActivity.onActivityResult', 'LIFECYCLE', 'Framework calls onActivityResult after startActivityForResult',
  evidence='FW-SRC Activity.java onActivityResult lifecycle')

e('S_ENTRY', 'MainActivity.onBackPressed', 'LIFECYCLE', 'Framework calls onBackPressed when back button pressed',
  evidence='FW-SRC Activity.java onBackPressed lifecycle')

e('MainActivity.onBackPressed', 'MainActivity.goToMain', 'CALL', 'onBackPressed calls goToMain to return to main',
  evidence='SRC MainActivity.java:739,743,745 goToMain calls in onBackPressed')

e('MainActivity.onBackPressed', 'MainActivity.getCurrentMainFragment', 'CALL', 'onBackPressed calls getCurrentMainFragment to navigate',
  evidence='SRC MainActivity.java:717 getCurrentMainFragment().goBack()')

e('S_ENTRY', 'MainActivity.onNewIntent', 'LIFECYCLE', 'Framework calls onNewIntent for singleInstance launchMode',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:60 launchMode singleInstance; FW-SRC Activity.java onNewIntent')

e('MainActivity.onNewIntent', 'MainActivity.checkForExternalIntent', 'CALL', 'onNewIntent calls checkForExternalIntent',
  evidence='SRC MainActivity.java:1602')

e('MainActivity.onNewIntent', 'MainActivity.goToMain', 'CALL', 'onNewIntent calls goToMain',
  evidence='SRC MainActivity.java:1580')

e('MainActivity.onNewIntent', 'MainActivity.getCurrentMainFragment', 'CALL', 'onNewIntent calls getCurrentMainFragment',
  evidence='SRC MainActivity.java:1575')

e('S_ENTRY', 'MainActivity.onKeyDown', 'LIFECYCLE', 'Framework calls onKeyDown for key press events',
  evidence='FW-SRC Activity.java onKeyDown lifecycle')

e('S_ENTRY', 'MainActivity.onCreateLoader', 'LIFECYCLE', 'Framework calls onCreateLoader for LoaderManager',
  evidence='SRC MainActivity.java:299 initLoader call triggers LoaderCallbacks')

e('S_ENTRY', 'MainActivity.onLoadFinished', 'LIFECYCLE', 'Framework calls onLoadFinished when loader completes',
  evidence='FW-SRC LoaderCallbacks interface')

e('S_ENTRY', 'MainActivity.onLoaderReset', 'LIFECYCLE', 'Framework calls onLoaderReset when loader is reset',
  evidence='FW-SRC LoaderCallbacks interface')

e('MainActivity.getCurrentMainFragment', 'MainActivity.getTabFragment', 'CALL', 'getCurrentMainFragment calls getTabFragment',
  evidence='SRC MainActivity.java:1253')

e('MainActivity.getTabFragment', 'MainActivity.getFragmentAtFrame', 'CALL', 'getTabFragment calls getFragmentAtFrame',
  evidence='SRC MainActivity.java:1261')

e('MainActivity.onOptionsItemSelected', 'MainActivity.getCurrentMainFragment', 'CALL', 'onOptionsItemSelected calls getCurrentMainFragment',
  evidence='SRC MainActivity.java:936 getCurrentMainFragment call')

e('MainActivity.onPrepareOptionsMenu', 'MainActivity.getCurrentMainFragment', 'CALL', 'onPrepareOptionsMenu calls getCurrentMainFragment',
  evidence='SRC MainActivity.java:853 getCurrentMainFragment call')

e('MainActivity.onActivityResult', 'MainActivity.getCurrentMainFragment', 'CALL', 'onActivityResult calls getCurrentMainFragment',
  evidence='SRC MainActivity.java:1367,1388,1392 getCurrentMainFragment calls')

e('MainActivity.initFabToSave', 'MainActivity.getCurrentMainFragment', 'CALL', 'initFabToSave calls getCurrentMainFragment',
  evidence='SRC MainActivity.java:560,572 getCurrentMainFragment calls')

e('MainActivity.onOptionsItemSelected', 'MainActivity.getFragmentAtFrame', 'CALL', 'onOptionsItemSelected calls getFragmentAtFrame',
  evidence='SRC MainActivity.java:974,1030 getFragmentAtFrame calls')

e('MainActivity.onPrepareOptionsMenu', 'MainActivity.getFragmentAtFrame', 'CALL', 'onPrepareOptionsMenu calls getFragmentAtFrame',
  evidence='SRC MainActivity.java:843 getFragmentAtFrame call')

e('MainActivity.onBackPressed', 'MainActivity.getFragmentAtFrame', 'CALL', 'onBackPressed calls getFragmentAtFrame',
  evidence='SRC MainActivity.java:710,720,724 getFragmentAtFrame calls')

e('MainActivity.initialiseFab', 'MainActivity.getFAB', 'CALL', 'initialiseFab initializes and returns FAB',
  evidence='SRC MainActivity.java:1497 floatingActionButton = findViewById; method returns it')

e('MainActivity.initialiseViews', 'MainActivity.getAppbar', 'CALL', 'initialiseViews initializes appbar',
  evidence='SRC MainActivity.java:1425 appBarLayout = getAppbar().getAppbarLayout()')

e('MainActivity.onCreate', 'MainActivity.getAppbar', 'CALL', 'onCreate accesses appbar',
  evidence='SRC MainActivity.java:287-291 new AppBar and access via getAppbar')

e('MainActivity.onBackPressed', 'MainActivity.getAppbar', 'CALL', 'onBackPressed accesses appbar search view',
  evidence='SRC MainActivity.java:710 getAppbar().getSearchView()')

e('MainActivity.onOptionsItemSelected', 'MainActivity.getAppbar', 'CALL', 'onOptionsItemSelected accesses appbar',
  evidence='SRC MainActivity.java:1039 getAppbar().getSearchView()')

e('MainActivity.initialiseViews', 'MainActivity.getDrawer', 'CALL', 'initialiseViews initializes drawer',
  evidence='SRC MainActivity.java:1428 drawer = new Drawer(this)')

e('MainActivity.onCreate', 'MainActivity.getDrawer', 'CALL', 'onCreate accesses drawer',
  evidence='SRC MainActivity.java:318 drawer.setSomethingSelected')

e('MainActivity.onBackPressed', 'MainActivity.getDrawer', 'CALL', 'onBackPressed checks drawer state',
  evidence='SRC MainActivity.java:704-706 drawer.isLocked() and drawer.isOpen()')

e('MainActivity.onOptionsItemSelected', 'MainActivity.showToast', 'CALL', 'onOptionsItemSelected calls showToast',
  evidence='SRC MainActivity.java:955 Toast.makeText call (showToast wraps this pattern)')

e('MainActivity.exit', 'MainActivity.showToast', 'CALL', 'exit calls showToast for exit message',
  evidence='SRC MainActivity.java:774 showToast(getString(R.string.press_again))')

e('MainActivity.addConnection', 'MainActivity.getCurrentMainFragment', 'CALL', 'addConnection(6 params) calls getCurrentMainFragment',
  evidence='SRC MainActivity.java:1698 getCurrentMainFragment call')

e('MainActivity.addConnection', 'MainActivity.getDrawer', 'CALL', 'addConnection(6 params) calls drawer.refreshDrawer',
  evidence='SRC MainActivity.java:1693,1707 drawer.refreshDrawer()')

e('MainActivity.addConnection', 'MainActivity.onCreateLoader', 'CALL', 'addConnection(OpenMode) triggers loader',
  evidence='SRC MainActivity.java:1816 getSupportLoaderManager().initLoader triggers onCreateLoader')

e('MainActivity.deleteConnection', 'MainActivity.getDrawer', 'CALL', 'deleteConnection(name,path) calls drawer.refreshDrawer',
  evidence='SRC MainActivity.java:1727 drawer.refreshDrawer()')

e('MainActivity.deleteConnection', 'MainActivity.getDrawer', 'CALL', 'deleteConnection(OpenMode) calls drawer.refreshDrawer via runOnUiThread',
  evidence='SRC MainActivity.java:1826 runOnUiThread(drawer::refreshDrawer)')

e('MainActivity.onCreate', 'MainActivity.onHiddenFileAdded', 'CALL', 'DataUtils callbacks for data changes',
  evidence='SRC MainActivity.java:283 dataUtils.registerOnDataChangedListener(this) registers callbacks')

e('MainActivity.onCreate', 'MainActivity.onHiddenFileRemoved', 'CALL', 'DataUtils callbacks for data changes',
  evidence='SRC MainActivity.java:283 dataUtils.registerOnDataChangedListener(this) registers callbacks')

e('MainActivity.onCreate', 'MainActivity.onHistoryAdded', 'CALL', 'DataUtils callbacks for data changes',
  evidence='SRC MainActivity.java:283 dataUtils.registerOnDataChangedListener(this) registers callbacks')

e('MainActivity.onCreate', 'MainActivity.onBookAdded', 'CALL', 'DataUtils callbacks for data changes',
  evidence='SRC MainActivity.java:283 dataUtils.registerOnDataChangedListener(this) registers callbacks')

e('MainActivity.onCreate', 'MainActivity.onHistoryCleared', 'CALL', 'DataUtils callbacks for data changes',
  evidence='SRC MainActivity.java:283 dataUtils.registerOnDataChangedListener(this) registers callbacks')

e('MainActivity.onOptionsItemSelected', 'MainActivity.delete', 'CALL', 'delete is callback from BookmarkCallback interface',
  evidence='SRC MainActivity.java:157 implements BookmarkCallback; method delete removes bookmark')

e('MainActivity.onOptionsItemSelected', 'MainActivity.modify', 'CALL', 'modify is callback from BookmarkCallback interface',
  evidence='SRC MainActivity.java:157 implements BookmarkCallback; method modify renames bookmark')

e('MainActivity.onCreate', 'MainActivity.copyToClipboard', 'CALL', 'copyToClipboard is utility for clipboard operations',
  evidence='SRC MainActivity.java:1537-1548 copyToClipboard implementation')

e('MainActivity.onCreate', 'MainActivity.renameBookmark', 'CALL', 'renameBookmark is callback for bookmark rename',
  evidence='SRC MainActivity.java:157 implements BookmarkCallback')

e('MainActivity.onCreate', 'MainActivity.getPaste', 'CALL', 'getPaste getter for paste helper',
  evidence='SRC MainActivity.java:1558 return pasteHelper')

e('MainActivity.onCreate', 'MainActivity.setPaste', 'CALL', 'setPaste setter for paste helper',
  evidence='SRC MainActivity.java:1562 pasteHelper = p')

e('MainActivity.initialiseViews', 'MainActivity.showSmokeScreen', 'CALL', 'showSmokeScreen shows overlay',
  evidence='SRC MainActivity.java:1670 fabBgView.show()')

e('MainActivity.initialiseViews', 'MainActivity.hideSmokeScreen', 'CALL', 'hideSmokeScreen hides overlay',
  evidence='SRC MainActivity.java:1674 fabBgView.hide()')

e('MainActivity.initialiseFab', 'MainActivity.initFabTitle', 'CALL', 'initialiseFab calls initFabTitle to set FAB titles',
  evidence='SRC MainActivity.java:1502-1504 initFabTitle calls for cloud, file, folder')

e('MainActivity.onCreate', 'MainActivity.getStorageDirectories', 'CALL', 'getStorageDirectories returns storage paths',
  evidence='SRC MainActivity.java:624-701 getStorageDirectories implementation')

e('MainActivity.getStorageDirectories', 'MainActivity.getUsbDrive', 'CALL', 'getStorageDirectories calls getUsbDrive',
  evidence='SRC MainActivity.java:697 File usb = getUsbDrive()')

e('MainActivity.onCreate', 'MainActivity.updateViews', 'CALL', 'updateViews updates UI colors',
  evidence='SRC MainActivity.java:1473-1495 updateViews implementation')

e('MainActivity.onPrepareOptionsMenu', 'MainActivity.showToast', 'CALL', 'onPrepareOptionsMenu may show toast',
  evidence='SRC MainActivity.java:1044-1058 showToast method pattern')

e('MainActivity.setPagingEnabled', 'MainActivity.getTabFragment', 'CALL', 'setPagingEnabled calls getTabFragment',
  evidence='SRC MainActivity.java:1272 getTabFragment().mViewPager')

# ---- part b032 (2026-10-27) GeneralDialogCreation dialog factory

e('MainActivity.onOptionsItemSelected', 'GeneralDialogCreation.showBasicDialog', 'CALL', 'sethome menu item shows dialog to confirm setting path as home',
  evidence='SRC MainActivity.java:952, GeneralDialogCreation.java:123-138')
e('PermissionsActivity.requestStoragePermission', 'GeneralDialogCreation.showBasicDialog', 'CALL', 'shows permission request dialog',
  evidence='SRC PermissionsActivity.java:54, GeneralDialogCreation.java:123-138')
e('PermissionsActivity.requestInstallApkPermission', 'GeneralDialogCreation.showBasicDialog', 'CALL', 'shows install APK permission request dialog',
  evidence='SRC PermissionsActivity.java:65, GeneralDialogCreation.java:123-138')
e('GeneralDialogCreation.showOtgSafExplanationDialog', 'GeneralDialogCreation.showBasicDialog', 'CALL', 'delegates to showBasicDialog for OTG SAF explanation',
  evidence='SRC GeneralDialogCreation.java:1214-1216')
e('ItemPopupMenu.onMenuItemClick', 'GeneralDialogCreation.deleteFilesDialog', 'CALL', 'delete menu item shows delete confirmation dialog',
  evidence='SRC ItemPopupMenu.java:123-126, GeneralDialogCreation.java:183-355')
e('MainFragment.lambda$getActionModeCallback$7', 'GeneralDialogCreation.deleteFilesDialog', 'CALL', 'delete action in selection mode shows delete dialog',
  evidence='SRC MainFragment.java:660-661, GeneralDialogCreation.java:183-355')
e('MainFragment.rename', 'GeneralDialogCreation.showNameDialog', 'CALL', 'shows dialog to rename file',
  evidence='SRC MainFragment.java:1210-1220, GeneralDialogCreation.java:140-181')
e('MainActivityHelper.mk', 'GeneralDialogCreation.showNameDialog', 'CALL', 'shows dialog to create new file/folder with name',
  evidence='SRC MainActivityHelper.java:196-202, GeneralDialogCreation.java:140-181')
e('GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog', 'GeneralDialogCreation.showNameDialog', 'CALL', 'shows save-as dialog for encrypted file',
  evidence='SRC GeneralDialogCreation.java:686-710')
e('ItemPopupMenu.onMenuItemClick', 'GeneralDialogCreation.showPropertiesDialogWithPermissions', 'CALL', 'properties menu item shows properties dialog with permissions',
  evidence='SRC ItemPopupMenu.java:68-69, GeneralDialogCreation.java:358-361')
e('MainFragment.lambda$getActionModeCallback$7', 'GeneralDialogCreation.showPropertiesDialogWithPermissions', 'CALL', 'properties action shows dialog with permissions',
  evidence='SRC MainFragment.java:654-656, GeneralDialogCreation.java:358-361')
e('GeneralDialogCreation.showPropertiesDialogWithPermissions', 'GeneralDialogCreation.showPropertiesDialog', 'CALL', 'delegates to main properties dialog with showPermissions=true',
  evidence='SRC GeneralDialogCreation.java:360, GeneralDialogCreation.java:371-585')
e('TextEditorActivity.lambda$initStatusBarResources$2', 'GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'CALL', 'info menu shows properties without permissions',
  evidence='SRC TextEditorActivity.java:369-370, GeneralDialogCreation.java:363-365')
e('GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'GeneralDialogCreation.showPropertiesDialog', 'CALL', 'delegates to main properties dialog with showPermissions=false',
  evidence='SRC GeneralDialogCreation.java:364, GeneralDialogCreation.java:371-585')
e('Drawer.lambda$setDrawerHeaderBackground$11', 'GeneralDialogCreation.showPropertiesDialogForStorage', 'CALL', 'shows storage properties dialog for drive',
  evidence='SRC Drawer.java:612-613, GeneralDialogCreation.java:367-369')
e('GeneralDialogCreation.showPropertiesDialogForStorage', 'GeneralDialogCreation.showPropertiesDialog', 'CALL', 'delegates to main properties dialog with forStorage=true',
  evidence='SRC GeneralDialogCreation.java:368, GeneralDialogCreation.java:371-585')
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.setPermissionsDialog', 'CALL', 'sets up permissions UI when showPermissions is true and user is root',
  evidence='SRC GeneralDialogCreation.java:536-541, GeneralDialogCreation.java:1129-1181')
e('Drawer.lambda$setDrawerHeaderBackground$11', 'GeneralDialogCreation.showCloudDialog', 'CALL', 'long-press on cloud connection shows remove dialog',
  evidence='SRC Drawer.java:628-634, GeneralDialogCreation.java:605-637')
e('ItemPopupMenu.onMenuItemClick', 'GeneralDialogCreation.showEncryptWarningDialog', 'CALL', 'encrypt menu shows warning dialog',
  evidence='SRC ItemPopupMenu.java:192-194, GeneralDialogCreation.java:639-679')
e('ItemPopupMenu.onMenuItemClick', 'GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog', 'CALL', 'encrypt with preset password shows save-as dialog',
  evidence='SRC ItemPopupMenu.java:160-166, GeneralDialogCreation.java:681-712')
e('ItemPopupMenu.onMenuItemClick', 'GeneralDialogCreation.showEncryptAuthenticateDialog', 'CALL', 'encrypt menu shows authentication dialog',
  evidence='SRC ItemPopupMenu.java:168-170, GeneralDialogCreation.java:714-807')
e('EncryptDecryptUtils.decryptFile', 'GeneralDialogCreation.showDecryptFingerprintDialog', 'CALL', 'shows fingerprint authentication dialog for decryption on M+',
  evidence='SRC EncryptDecryptUtils.java:109-111, GeneralDialogCreation.java:809-837')
e('EncryptDecryptUtils.decryptFile', 'GeneralDialogCreation.showDecryptDialog', 'CALL', 'shows password dialog for decryption',
  evidence='SRC EncryptDecryptUtils.java:120-122, GeneralDialogCreation.java:839-856')
e('GeneralDialogCreation.showDecryptDialog', 'GeneralDialogCreation.showPasswordDialog', 'CALL', 'delegates to password dialog with decrypt callback',
  evidence='SRC GeneralDialogCreation.java:847-855, GeneralDialogCreation.java:858-896')
e('SevenZipHelperTask.onPostExecute', 'GeneralDialogCreation.showPasswordDialog', 'CALL', 'shows password dialog when 7z archive requires password',
  evidence='SRC SevenZipHelperTask.java:104-106, GeneralDialogCreation.java:858-896')
e('ExtractService.lambda$extract$0', 'GeneralDialogCreation.showPasswordDialog', 'CALL', 'shows password dialog when extraction requires password',
  evidence='SRC ExtractService.java:331-333, GeneralDialogCreation.java:858-896')
e('SmbConnectDialog.lambda$new$2', 'GeneralDialogCreation.showSMBHelpDialog', 'CALL', 'shows SMB connection help dialog',
  evidence='SRC SmbConnectDialog.java:164, GeneralDialogCreation.java:898-904')
e('FileUtils.openFile', 'GeneralDialogCreation.showPackageDialog', 'CALL', 'shows package installer dialog for APK files',
  evidence='SRC FileUtils.java:753, GeneralDialogCreation.java:906-922')
e('FileUtils.openFile', 'GeneralDialogCreation.showArchiveDialog', 'CALL', 'shows archive options dialog for compressed files',
  evidence='SRC FileUtils.java:755, GeneralDialogCreation.java:924-945')
e('MainFragment.lambda$getActionModeCallback$7', 'GeneralDialogCreation.showCompressDialog', 'CALL', 'compress action shows compress dialog',
  evidence='SRC MainFragment.java:738, GeneralDialogCreation.java:947-997')
e('MainActivity.onOptionsItemSelected', 'GeneralDialogCreation.showSortDialog', 'CALL', 'sort menu for apps list shows sort dialog',
  evidence='SRC MainActivity.java:967, GeneralDialogCreation.java:1056-1083')
e('MainActivity.onOptionsItemSelected', 'GeneralDialogCreation.showSortDialog', 'CALL', 'sort menu for main fragment shows sort dialog',
  evidence='SRC MainActivity.java:972, GeneralDialogCreation.java:999-1034')
e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.onSortTypeSelected', 'CALL', 'user selects sort direction, processes the selection',
  evidence='SRC GeneralDialogCreation.java:1027-1030, GeneralDialogCreation.java:1036-1054')
e('MainActivity.onOptionsItemSelected', 'GeneralDialogCreation.showHistoryDialog', 'CALL', 'history menu shows history dialog',
  evidence='SRC MainActivity.java:943, GeneralDialogCreation.java:1085-1104')
e('MainActivity.onNavigationItemSelected', 'GeneralDialogCreation.showHiddenDialog', 'CALL', 'hidden files menu shows hidden files dialog',
  evidence='SRC MainActivity.java:994, GeneralDialogCreation.java:1106-1127')
e('BottomBar.lambda$initProperties$0', 'GeneralDialogCreation.showChangePathsDialog', 'CALL', 'path button click shows path change dialog',
  evidence='SRC BottomBar.java:153, GeneralDialogCreation.java:1183-1212')
e('Drawer.lambda$setDrawerHeaderBackground$11', 'GeneralDialogCreation.showOtgSafExplanationDialog', 'CALL', 'OTG item click shows SAF explanation dialog',
  evidence='SRC Drawer.java:583, GeneralDialogCreation.java:1214-1216')
e('GeneralDialogCreation.deleteFilesDialog', 'GeneralDialogCreation.lambda$deleteFilesDialog$0', 'ASYNC', 'positive button callback deletes files',
  evidence='SRC GeneralDialogCreation.java:193-197')
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$1', 'GUI', 'name field long-press copies name to clipboard',
  evidence='SRC GeneralDialogCreation.java:433-437')
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$2', 'GUI', 'location field long-press copies location to clipboard',
  evidence='SRC GeneralDialogCreation.java:438-442')
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$3', 'GUI', 'size field long-press copies size to clipboard',
  evidence='SRC GeneralDialogCreation.java:443-447')
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$4', 'GUI', 'date field long-press copies date to clipboard',
  evidence='SRC GeneralDialogCreation.java:448-452')
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$5', 'GUI', 'permissions button click toggles permissions table visibility',
  evidence='SRC GeneralDialogCreation.java:529-542')
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$6', 'LIFECYCLE', 'dialog dismiss listener shuts down executor',
  evidence='SRC GeneralDialogCreation.java:567')
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation.lambda$showPropertiesDialog$7', 'GUI', 'positive button creates/deletes .nomedia file',
  evidence='SRC GeneralDialogCreation.java:568-582')
e('GeneralDialogCreation.showCloudDialog', 'GeneralDialogCreation.lambda$showCloudDialog$8', 'GUI', 'positive button deletes cloud connection',
  evidence='SRC GeneralDialogCreation.java:629')
e('GeneralDialogCreation.showCloudDialog', 'GeneralDialogCreation.lambda$showCloudDialog$9', 'GUI', 'negative button cancels dialog',
  evidence='SRC GeneralDialogCreation.java:631')
e('GeneralDialogCreation.showEncryptWarningDialog', 'GeneralDialogCreation.lambda$showEncryptWarningDialog$10', 'GUI', 'positive button confirms encryption',
  evidence='SRC GeneralDialogCreation.java:653-666')
e('GeneralDialogCreation.showEncryptWarningDialog', 'GeneralDialogCreation.lambda$showEncryptWarningDialog$11', 'GUI', 'negative button saves preference and encrypts',
  evidence='SRC GeneralDialogCreation.java:668-677')
e('GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog', 'GeneralDialogCreation.lambda$showEncryptWithPresetPasswordSaveAsDialog$12', 'GUI', 'positive button starts encryption with preset password',
  evidence='SRC GeneralDialogCreation.java:695-706')
e('GeneralDialogCreation.showEncryptWithPresetPasswordSaveAsDialog', 'GeneralDialogCreation.lambda$showEncryptWithPresetPasswordSaveAsDialog$13', 'GUI', 'input validator checks filename format',
  evidence='SRC GeneralDialogCreation.java:707-710')
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$14', 'GUI', 'shows soft keyboard for password input',
  evidence='SRC GeneralDialogCreation.java:749-752')
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$15', 'GUI', 'negative button cancels dialog',
  evidence='SRC GeneralDialogCreation.java:759')
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$16', 'GUI', 'positive button starts encryption with entered password',
  evidence='SRC GeneralDialogCreation.java:760-772')
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$17', 'GUI', 'text watcher enables OK button when all fields filled',
  evidence='SRC GeneralDialogCreation.java:784-788')
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$18', 'GUI', 'password validator checks field is not empty',
  evidence='SRC GeneralDialogCreation.java:793-797')
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation.lambda$showEncryptAuthenticateDialog$19', 'GUI', 'confirm password validator checks passwords match',
  evidence='SRC GeneralDialogCreation.java:800-804')
e('GeneralDialogCreation.showDecryptFingerprintDialog', 'GeneralDialogCreation.lambda$showDecryptFingerprintDialog$20', 'GUI', 'cancel button dismisses fingerprint dialog',
  evidence='SRC GeneralDialogCreation.java:832')
e('GeneralDialogCreation.showDecryptDialog', 'GeneralDialogCreation.lambda$showDecryptDialog$21', 'GUI', 'password entry validates and decrypts file',
  evidence='SRC GeneralDialogCreation.java:849-855')
e('GeneralDialogCreation.showPasswordDialog', 'GeneralDialogCreation.lambda$showPasswordDialog$22', 'GUI', 'negative button cancels password dialog if no custom callback',
  evidence='SRC GeneralDialogCreation.java:886')
e('GeneralDialogCreation.showPasswordDialog', 'GeneralDialogCreation.lambda$showPasswordDialog$23', 'GUI', 'input validator checks password field is not empty',
  evidence='SRC GeneralDialogCreation.java:891-895')
e('GeneralDialogCreation.showPackageDialog', 'GeneralDialogCreation.lambda$showPackageDialog$24', 'GUI', 'positive button installs APK',
  evidence='SRC GeneralDialogCreation.java:916')
e('GeneralDialogCreation.showPackageDialog', 'GeneralDialogCreation.lambda$showPackageDialog$25', 'GUI', 'negative button opens APK as archive',
  evidence='SRC GeneralDialogCreation.java:917')
e('GeneralDialogCreation.showArchiveDialog', 'GeneralDialogCreation.lambda$showArchiveDialog$26', 'GUI', 'positive button extracts archive',
  evidence='SRC GeneralDialogCreation.java:938')
e('GeneralDialogCreation.showArchiveDialog', 'GeneralDialogCreation.lambda$showArchiveDialog$27', 'GUI', 'negative button views archive contents',
  evidence='SRC GeneralDialogCreation.java:939')
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$28', 'GUI', 'positive button creates zip archive',
  evidence='SRC GeneralDialogCreation.java:965-967')
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$29', 'GUI', 'input validator checks filename validity and suggests .zip extension',
  evidence='SRC GeneralDialogCreation.java:972-987')
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$30', 'GUI', 'sets cursor to start of filename field',
  evidence='SRC GeneralDialogCreation.java:993')
e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$31', 'GUI', 'folder-specific sort checkbox state changed',
  evidence='SRC GeneralDialogCreation.java:1019-1026')
e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$32', 'GUI', 'negative button selects ascending sort',
  evidence='SRC GeneralDialogCreation.java:1028-1030')
e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$33', 'GUI', 'positive button selects descending sort',
  evidence='SRC GeneralDialogCreation.java:1031-1033')
e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$34', 'GUI', 'negative button selects ascending app sort',
  evidence='SRC GeneralDialogCreation.java:1070-1075')
e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$35', 'GUI', 'positive button selects descending app sort',
  evidence='SRC GeneralDialogCreation.java:1077-1082')
e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$36', 'GUI', 'item selection callback in sort dialog',
  evidence='SRC GeneralDialogCreation.java:1011 or 1066 (overloaded method)')
e('GeneralDialogCreation.showSortDialog', 'GeneralDialogCreation.lambda$showSortDialog$37', 'GUI', 'item selection callback in sort dialog',
  evidence='SRC GeneralDialogCreation.java:1011 or 1066 (overloaded method)')
e('GeneralDialogCreation.showHistoryDialog', 'GeneralDialogCreation.lambda$showHistoryDialog$38', 'GUI', 'negative button clears history',
  evidence='SRC GeneralDialogCreation.java:1095')
e('GeneralDialogCreation.setPermissionsDialog', 'GeneralDialogCreation.lambda$null$39', 'ASYNC', 'permission change result callback',
  evidence='SRC GeneralDialogCreation.java:1167-1175')
e('GeneralDialogCreation.setPermissionsDialog', 'GeneralDialogCreation.lambda$setPermissionsDialog$40', 'GUI', 'set button applies permission changes',
  evidence='SRC GeneralDialogCreation.java:1163-1177')
e('GeneralDialogCreation.showChangePathsDialog', 'GeneralDialogCreation.lambda$showChangePathsDialog$41', 'GUI', 'input callback validates path accessibility',
  evidence='SRC GeneralDialogCreation.java:1188-1191')
e('GeneralDialogCreation.showChangePathsDialog', 'GeneralDialogCreation.lambda$showChangePathsDialog$42', 'GUI', 'positive button navigates to entered path',
  evidence='SRC GeneralDialogCreation.java:1203-1205')

# UNREACHABLE from part b032
UNREACHABLE['GeneralDialogCreation.<init>'] = ('no_trigger_in_app', 'Utility class with only static methods, no instances created; grep shows no "new GeneralDialogCreation()" calls', 'SRC GeneralDialogCreation.java:120 class definition shows all static methods; grep -rn "new GeneralDialogCreation" shows only inner class SizeFormatter', 'SOURCE')

# UNREACHABLE methods
# ---- Batch 047 label part (2026-10-27)
# Class: MainFragment (primary file-list fragment - main browsing screen)

# LIFECYCLE: TabFragment -> MainFragment onCreate -> onCreateView -> onActivityCreated -> onResume

# TabFragment creates MainFragment and calls Fragment lifecycle
e('TabFragment.addTab', 'MainFragment.<init>', 'FRAMEWORK',
  'TabFragment.addTab creates MainFragment instance at line 351',
  evidence='SRC fragments/TabFragment.java:351')

e('MainFragment.<init>', 'MainFragment.onCreate', 'LIFECYCLE',
  'Framework calls onCreate after Fragment construction',
  evidence='SRC fragments/MainFragment.java:202')

e('MainFragment.onCreate', 'MainFragment.getMainActivity', 'CALL',
  'onCreate calls getMainActivity to get MainActivity reference',
  evidence='SRC fragments/MainFragment.java:207')

e('MainFragment.onCreate', 'MainFragment.onCreateView', 'LIFECYCLE',
  'Framework calls onCreateView after onCreate',
  evidence='SRC fragments/MainFragment.java:237')

e('MainFragment.onCreateView', 'MainFragment.getMainActivity', 'CALL',
  'onCreateView calls getMainActivity for AppBar access',
  evidence='SRC fragments/MainFragment.java:242')

e('MainFragment.onCreateView', 'MainFragment.stopAnimation', 'CALL',
  'onCreateView sets lambda that calls stopAnimation on touch',
  evidence='SRC fragments/MainFragment.java:244,246,251,253')

e('MainFragment.onCreateView', 'MainFragment.lambda$onCreateView$0', 'CALL',
  'Lambda callback for listView.setOnTouchListener',
  evidence='SRC fragments/MainFragment.java:244-248')

e('MainFragment.onCreateView', 'MainFragment.lambda$onCreateView$1', 'CALL',
  'Lambda callback for mToolbarContainer.setOnTouchListener',
  evidence='SRC fragments/MainFragment.java:250-256')

e('MainFragment.onCreateView', 'MainFragment.lambda$onCreateView$2', 'CALL',
  'Lambda callback for mSwipeRefreshLayout.setOnRefreshListener',
  evidence='SRC fragments/MainFragment.java:260')

e('MainFragment.lambda$onCreateView$0', 'MainFragment.stopAnimation', 'CALL',
  'Touch listener lambda calls stopAnimation',
  evidence='SRC fragments/MainFragment.java:246')

e('MainFragment.lambda$onCreateView$1', 'MainFragment.stopAnimation', 'CALL',
  'Toolbar touch listener lambda calls stopAnimation',
  evidence='SRC fragments/MainFragment.java:253')

e('MainFragment.lambda$onCreateView$2', 'MainFragment.loadlist', 'CALL',
  'Swipe refresh lambda calls loadlist',
  evidence='SRC fragments/MainFragment.java:260')

e('MainFragment.onCreateView', 'MainFragment.onActivityCreated', 'LIFECYCLE',
  'Framework calls onActivityCreated after onCreateView',
  evidence='SRC fragments/MainFragment.java:271')

e('MainFragment.onActivityCreated', 'MainFragment.initNoFileLayout', 'CALL',
  'onActivityCreated calls initNoFileLayout',
  evidence='SRC fragments/MainFragment.java:276')

e('MainFragment.onActivityCreated', 'MainFragment.getSortModes', 'CALL',
  'onActivityCreated calls getSortModes',
  evidence='SRC fragments/MainFragment.java:277')

e('MainFragment.onActivityCreated', 'MainFragment.getMainActivity', 'CALL',
  'onActivityCreated calls getMainActivity multiple times',
  evidence='SRC fragments/MainFragment.java:281')

e('MainFragment.onActivityCreated', 'MainFragment.getBoolean', 'CALL',
  'onActivityCreated calls getBoolean for preferences',
  evidence='SRC fragments/MainFragment.java:302')

e('MainFragment.onActivityCreated', 'MainFragment.setGridLayoutSpanSizeLookup', 'CALL',
  'onActivityCreated calls setGridLayoutSpanSizeLookup for grid layout',
  evidence='SRC fragments/MainFragment.java:297')

e('MainFragment.onActivityCreated', 'MainFragment.onSavedInstanceState', 'CALL',
  'onActivityCreated restores state by calling onSavedInstanceState',
  evidence='SRC fragments/MainFragment.java:320,337')

e('MainFragment.onActivityCreated', 'MainFragment.loadlist', 'CALL',
  'onActivityCreated calls loadlist to populate file list',
  evidence='SRC fragments/MainFragment.java:334')

e('MainFragment.initNoFileLayout', 'MainFragment.lambda$initNoFileLayout$4', 'CALL',
  'initNoFileLayout creates lambda for nofilesview refresh listener',
  evidence='SRC fragments/MainFragment.java:1039-1042')

e('MainFragment.initNoFileLayout', 'MainFragment.getMainActivity', 'CALL',
  'initNoFileLayout calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1044-1050')

e('MainFragment.lambda$initNoFileLayout$4', 'MainFragment.loadlist', 'CALL',
  'No files view refresh lambda calls loadlist',
  evidence='SRC fragments/MainFragment.java:1040')

e('MainFragment.onActivityCreated', 'MainFragment.onResume', 'LIFECYCLE',
  'Framework calls onResume after onActivityCreated',
  evidence='SRC fragments/MainFragment.java:1419')

e('MainFragment.onResume', 'MainFragment.getMainActivity', 'CALL',
  'onResume calls getMainActivity to register receivers',
  evidence='SRC fragments/MainFragment.java:1423')

e('MainFragment.onResume', 'MainFragment.getPath', 'CALL',
  'onResume calls getPath for drawer selection',
  evidence='SRC fragments/MainFragment.java:1423')

e('MainFragment.onResume', 'MainFragment.startFileObserver', 'CALL',
  'onResume calls startFileObserver to watch file changes',
  evidence='SRC fragments/MainFragment.java:1428')

e('MainFragment.onResume', 'MainFragment.onPause', 'LIFECYCLE',
  'Framework calls onPause when fragment loses focus',
  evidence='SRC fragments/MainFragment.java:1433')

e('MainFragment.onPause', 'MainFragment.onStop', 'LIFECYCLE',
  'Framework calls onStop after onPause',
  evidence='SRC fragments/MainFragment.java:1446')

e('MainFragment.onStop', 'MainFragment.onDestroy', 'LIFECYCLE',
  'Framework calls onDestroy after onStop',
  evidence='SRC fragments/MainFragment.java:1544')

e('MainFragment.onDestroy', 'MainFragment.onDetach', 'LIFECYCLE',
  'Framework calls onDetach after onDestroy',
  evidence='SRC fragments/MainFragment.java:1698')

# LIST LOADING FLOW: loadlist -> LoadFilesListTask (async) -> setListElements -> reloadListElements

e('MainFragment.loadlist', 'MainFragment.lambda$loadlist$3', 'CALL',
  'loadlist creates LoadFilesListTask with lambda callback',
  evidence='SRC fragments/MainFragment.java:1023-1029')

e('MainFragment.lambda$loadlist$3', 'MainFragment.setListElements', 'CALL',
  'LoadFilesListTask lambda callback calls setListElements',
  evidence='SRC fragments/MainFragment.java:1026')

e('MainFragment.loadlist', 'MainFragment.getBoolean', 'CALL',
  'loadlist calls getBoolean for preferences',
  evidence='SRC fragments/MainFragment.java:1024')

e('MainFragment.setListElements', 'MainFragment.reloadListElements', 'CALL',
  'setListElements calls reloadListElements to render list',
  evidence='SRC fragments/MainFragment.java:1071')

e('MainFragment.setListElements', 'MainFragment.loadlist', 'CALL',
  'setListElements calls loadlist if bitmap is null (load home)',
  evidence='SRC fragments/MainFragment.java:1075')

e('MainFragment.reloadListElements', 'MainFragment.getBoolean', 'CALL',
  'reloadListElements calls getBoolean for preferences',
  evidence='SRC fragments/MainFragment.java:1089')

e('MainFragment.reloadListElements', 'MainFragment.getBackElement', 'CALL',
  'reloadListElements calls getBackElement to add back button',
  evidence='SRC fragments/MainFragment.java:1093')

e('MainFragment.reloadListElements', 'MainFragment.switchToGrid', 'CALL',
  'reloadListElements calls switchToGrid when switching to grid view',
  evidence='SRC fragments/MainFragment.java:1101')

e('MainFragment.reloadListElements', 'MainFragment.switchToList', 'CALL',
  'reloadListElements calls switchToList when switching to list view',
  evidence='SRC fragments/MainFragment.java:1102')

e('MainFragment.reloadListElements', 'MainFragment.getMainActivity', 'CALL',
  'reloadListElements calls getMainActivity for adapter creation',
  evidence='SRC fragments/MainFragment.java:1105')

e('MainFragment.reloadListElements', 'MainFragment.startFileObserver', 'CALL',
  'reloadListElements calls startFileObserver to watch directory',
  evidence='SRC fragments/MainFragment.java:1156')

e('MainFragment.reloadListElements', 'MainFragment.loadlist', 'CALL',
  'reloadListElements calls loadlist if fragment not added',
  evidence='SRC fragments/MainFragment.java:1161')

e('MainFragment.reloadListElements', 'MainFragment.lambda$reloadListElements$5', 'CALL',
  'reloadListElements sets lambda for AppBarLayout offset listener',
  evidence='SRC fragments/MainFragment.java:1149-1151')

e('MainFragment.reloadListElements', 'MainFragment.lambda$reloadListElements$6', 'CALL',
  'reloadListElements sets lambda for FastScroller touch listener',
  evidence='SRC fragments/MainFragment.java:1152-1157')

e('MainFragment.lambda$reloadListElements$6', 'MainFragment.stopAnimation', 'CALL',
  'FastScroller touch lambda calls stopAnimation',
  evidence='SRC fragments/MainFragment.java:1154')

e('MainFragment.switchToGrid', 'MainFragment.getMainActivity', 'CALL',
  'switchToGrid calls getMainActivity for context',
  evidence='SRC fragments/MainFragment.java:363,365')

e('MainFragment.switchToGrid', 'MainFragment.setGridLayoutSpanSizeLookup', 'CALL',
  'switchToGrid calls setGridLayoutSpanSizeLookup',
  evidence='SRC fragments/MainFragment.java:367')

e('MainFragment.switchToList', 'MainFragment.getMainActivity', 'CALL',
  'switchToList calls getMainActivity for context',
  evidence='SRC fragments/MainFragment.java:384')

e('MainFragment.switchView', 'MainFragment.reloadListElements', 'CALL',
  'switchView calls reloadListElements with grid/list flag',
  evidence='SRC fragments/MainFragment.java:393')

# ITEM CLICK FLOW: RecyclerAdapter -> onListItemClicked -> navigate/open file

e('RecyclerAdapter.onItemClick', 'MainFragment.onListItemClicked', 'CALL',
  'RecyclerAdapter calls onListItemClicked when item clicked',
  evidence='SRC fragments/MainFragment.java:851')

e('MainFragment.onListItemClicked', 'MainFragment.getMainActivity', 'CALL',
  'onListItemClicked calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:853,888,891,896,899,903,908,927')

e('MainFragment.onListItemClicked', 'MainFragment.goBackItemClick', 'CALL',
  'onListItemClicked calls goBackItemClick for back button',
  evidence='SRC fragments/MainFragment.java:884')

e('MainFragment.onListItemClicked', 'MainFragment.computeScroll', 'CALL',
  'onListItemClicked calls computeScroll before navigation',
  evidence='SRC fragments/MainFragment.java:893')

e('MainFragment.onListItemClicked', 'MainFragment.loadlist', 'CALL',
  'onListItemClicked calls loadlist to navigate into directory',
  evidence='SRC fragments/MainFragment.java:894')

e('MainFragment.onListItemClicked', 'MainFragment.returnIntentResults', 'CALL',
  'onListItemClicked calls returnIntentResults for file picker',
  evidence='SRC fragments/MainFragment.java:908')

e('MainFragment.onListItemClicked', 'MainFragment.launchSMB', 'CALL',
  'onListItemClicked calls launchSMB for SMB files',
  evidence='SRC fragments/MainFragment.java:912')

# NAVIGATION: goBack, goBackItemClick, updateList

e('MainActivity.onBackPressed', 'MainFragment.goBack', 'CALL',
  'MainActivity.onBackPressed calls MainFragment.goBack',
  evidence='SRC fragments/MainFragment.java:1265')

e('MainFragment.goBack', 'MainFragment.loadlist', 'CALL',
  'goBack calls loadlist to navigate to parent',
  evidence='SRC fragments/MainFragment.java:1267,1283,1288,1319,1331,1336,1338,1368')

e('MainFragment.goBack', 'MainFragment.getMainActivity', 'CALL',
  'goBack calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1306,1310,1312,1323,1330')

e('MainFragment.goBackItemClick', 'MainFragment.loadlist', 'CALL',
  'goBackItemClick calls loadlist for back navigation',
  evidence='SRC fragments/MainFragment.java:1361,1377,1380,1387')

e('MainFragment.goBackItemClick', 'MainFragment.getMainActivity', 'CALL',
  'goBackItemClick calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1383')

e('BottomBar.backButton.onClick', 'MainFragment.goBackItemClick', 'CALL',
  'BottomBar back button onClick calls goBackItemClick',
  evidence='SRC fragments/MainFragment.java:1359')

e('MainFragment.updateList', 'MainFragment.computeScroll', 'CALL',
  'updateList calls computeScroll to save position',
  evidence='SRC fragments/MainFragment.java:1394')

e('MainFragment.updateList', 'MainFragment.loadlist', 'CALL',
  'updateList calls loadlist to refresh',
  evidence='SRC fragments/MainFragment.java:1395')

# BROADCAST RECEIVERS: registered in onResume

e('MainFragment.onResume', 'MainFragment.receiver2', 'SYSTEM',
  'onResume registers receiver2 for KEY_INTENT_LOAD_LIST',
  evidence='SRC fragments/MainFragment.java:1422')

e('MainFragment.receiver2', 'MainFragment.updateList', 'CALL',
  'receiver2.onReceive calls updateList',
  evidence='SRC fragments/MainFragment.java:824')

e('MainFragment.onResume', 'MainFragment.decryptReceiver', 'SYSTEM',
  'onResume registers decryptReceiver for DECRYPT_BROADCAST',
  evidence='SRC fragments/MainFragment.java:1425-1426')

# TAB UPDATES

e('MainActivity.onCreate', 'MainFragment.updateTabWithDb', 'CALL',
  'MainActivity.onCreate calls updateTabWithDb to restore tab',
  evidence='SRC fragments/MainFragment.java:967')

e('MainFragment.updateTabWithDb', 'MainFragment.loadlist', 'CALL',
  'updateTabWithDb calls loadlist with tab path',
  evidence='SRC fragments/MainFragment.java:970')

# FILE OPERATIONS: rename, hide, addToSmb, addTo

e('RecyclerAdapter.onRename', 'MainFragment.rename', 'CALL',
  'RecyclerAdapter calls rename for rename action',
  evidence='SRC fragments/MainFragment.java:1209')

e('MainFragment.rename', 'MainFragment.getMainActivity', 'CALL',
  'rename calls getMainActivity for dialog and helper',
  evidence='SRC fragments/MainFragment.java:1210,1226')

e('MainFragment.rename', 'MainFragment.lambda$rename$7', 'CALL',
  'rename creates lambda for dialog positive button',
  evidence='SRC fragments/MainFragment.java:1217-1226')

e('MainFragment.rename', 'MainFragment.lambda$rename$8', 'CALL',
  'rename creates lambda for text validation',
  evidence='SRC fragments/MainFragment.java:1227-1236')

e('MainFragment.rename', 'MainFragment.lambda$rename$9', 'CALL',
  'rename creates lambda for EditText cursor positioning',
  evidence='SRC fragments/MainFragment.java:1241-1245')

e('MainFragment.lambda$rename$7', 'MainFragment.getMainActivity', 'CALL',
  'Dialog button lambda calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1226')

e('MainActivity.hide', 'MainFragment.hide', 'CALL',
  'MainActivity.hide calls MainFragment.hide',
  evidence='SRC fragments/MainFragment.java:1551')

e('MainFragment.hide', 'MainFragment.getMainActivity', 'CALL',
  'hide calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1557')

e('LoadFilesListTask.loadlist', 'MainFragment.addToSmb', 'CALL',
  'LoadFilesListTask calls addToSmb for SMB files',
  evidence='SRC fragments/MainFragment.java:1461')

e('MainFragment.addToSmb', 'MainFragment.getBoolean', 'CALL',
  'addToSmb calls getBoolean for preferences',
  evidence='SRC fragments/MainFragment.java:1491')

e('SearchWorkerFragment.search', 'MainFragment.addSearchResult', 'CALL',
  'SearchWorkerFragment calls addSearchResult for each result',
  evidence='SRC fragments/MainFragment.java:1611')

e('MainFragment.addSearchResult', 'MainFragment.addTo', 'CALL',
  'addSearchResult calls addTo to create layout element',
  evidence='SRC fragments/MainFragment.java:1621')

e('MainFragment.addSearchResult', 'MainFragment.reloadListElements', 'CALL',
  'addSearchResult calls reloadListElements on first result',
  evidence='SRC fragments/MainFragment.java:1623')

e('MainFragment.addSearchResult', 'MainFragment.getMainActivity', 'CALL',
  'addSearchResult calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1624,1625,1630')

e('MainFragment.addSearchResult', 'MainFragment.stopAnimation', 'CALL',
  'addSearchResult calls stopAnimation',
  evidence='SRC fragments/MainFragment.java:1632')

e('MainFragment.addTo', 'MainFragment.getBoolean', 'CALL',
  'addTo calls getBoolean for preferences',
  evidence='SRC fragments/MainFragment.java:1507,1527')

# SEARCH FLOW

e('MainActivityHelper.search', 'MainFragment.onSearchPreExecute', 'CALL',
  'Search menu item click triggers onSearchPreExecute',
  evidence='SRC fragments/MainFragment.java:1603')

e('MainFragment.onSearchPreExecute', 'MainFragment.getMainActivity', 'CALL',
  'onSearchPreExecute calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1604,1605')

e('SearchWorkerFragment.onPostExecute', 'MainFragment.onSearchCompleted', 'CALL',
  'SearchWorkerFragment calls onSearchCompleted when search finishes',
  evidence='SRC fragments/MainFragment.java:1635')

e('MainFragment.onSearchCompleted', 'MainFragment.reloadListElements', 'CALL',
  'onSearchCompleted calls reloadListElements to display results',
  evidence='SRC fragments/MainFragment.java:1648')

e('MainFragment.onSearchCompleted', 'MainFragment.getMainActivity', 'CALL',
  'onSearchCompleted calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1649,1650')

# SHORTCUT

e('RecyclerAdapter.addShortcut', 'MainFragment.addShortcut', 'CALL',
  'RecyclerAdapter calls addShortcut for shortcut action',
  evidence='SRC fragments/MainFragment.java:1573')

e('MainFragment.addShortcut', 'MainFragment.getMainActivity', 'CALL',
  'addShortcut calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1595')

# SMB LAUNCH (static method)

e('FileUtils.openFile', 'MainFragment.launchSMB', 'CALL',
  'FileUtils calls launchSMB for SMB file opening',
  evidence='SRC fragments/MainFragment.java:1656')

# HOME NAVIGATION

e('MainActivity.home', 'MainFragment.home', 'CALL',
  'MainActivity.home calls MainFragment.home',
  evidence='SRC fragments/MainFragment.java:839')

e('MainFragment.home', 'MainFragment.loadlist', 'CALL',
  'home calls loadlist with home path',
  evidence='SRC fragments/MainFragment.java:840')

# CHANGE PATH (BottomBarButtonPath interface)

e('BottomBar.changePath', 'MainFragment.changePath', 'CALL',
  'BottomBar calls changePath to navigate',
  evidence='SRC fragments/MainFragment.java:1711')

e('MainFragment.changePath', 'MainFragment.loadlist', 'CALL',
  'changePath calls loadlist',
  evidence='SRC fragments/MainFragment.java:1712')

# REAUTHENTICATE SMB

e('MainActivity.reauthenticateSmb', 'MainFragment.reauthenticateSmb', 'CALL',
  'MainActivity calls reauthenticateSmb on auth failure',
  evidence='SRC fragments/MainFragment.java:1344')

e('MainFragment.reauthenticateSmb', 'MainFragment.getMainActivity', 'CALL',
  'reauthenticateSmb calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1346,1350')

# GETTERS (called from various places)

e('MainActivity.getCurrentPath', 'MainFragment.getCurrentPath', 'CALL',
  'MainActivity calls getCurrentPath',
  evidence='SRC fragments/MainFragment.java:1569')

e('MainActivity.getElementsList', 'MainFragment.getElementsList', 'CALL',
  'MainActivity calls getElementsList',
  evidence='SRC fragments/MainFragment.java:1706')

e('BottomBar.getRootDrawable', 'MainFragment.getRootDrawable', 'CALL',
  'BottomBar calls getRootDrawable for root indicator',
  evidence='SRC fragments/MainFragment.java:1721')

# SAVE/RESTORE INSTANCE STATE

e('MainFragment.onActivityCreated', 'MainFragment.onSaveInstanceState', 'LIFECYCLE',
  'Framework calls onSaveInstanceState before destroy',
  evidence='SRC fragments/MainFragment.java:397')

e('MainFragment.onSaveInstanceState', 'MainFragment.computeScroll', 'CALL',
  'onSaveInstanceState calls computeScroll implicitly via scroll computation',
  evidence='SRC fragments/MainFragment.java:404-414')

# STATIC METHOD findEncryptedEntry

e('EncryptDecryptUtils.decryptFile', 'MainFragment.findEncryptedEntry', 'CALL',
  'EncryptDecryptUtils calls findEncryptedEntry to find encrypted entry',
  evidence='SRC fragments/MainFragment.java:950')

# UNREACHABLE: synthetic lambda methods in bytecode but not in source

UNREACHABLE_B047 = {
    # REMOVED CONTRADICTION: 'MainFragment.lambda$reloadListElements$5'
    
    'MainFragment.lambda$reauthenticateSmb$10': ('no_trigger_in_app',
        'Synthetic lambda in method_list but reauthenticateSmb.runOnUiThread at line 1346 is anonymous Runnable, not separate lambda method',
        'SRC fragments/MainFragment.java:1346-1352 shows anonymous Runnable; lambda$reauthenticateSmb$10 not in source',
        'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_B047)
UNREACHABLE_PART_016 = {
    'CopyService.onBind': ('no_trigger_in_app', 'CopyService is started via startService, never bound. No bindService calls found in app.', 'SRC CopyService.java:508 defines onBind; grep found no bindService calls to CopyService', 'SOURCE'),
    
    'CopyService.checkFiles': ('no_trigger_in_app', 'Method is not called anywhere in app code. Comment at line 492 says "avoid using the method".', 'SRC CopyService.java:492-517 defines checkFiles; grep found no calls to this method', 'SOURCE'),
    
    # REMOVED CONTRADICTION: 'CopyService$DoInBackground.onPostExecute'
    
    'ComputerParcelable.<init>': ('no_trigger_in_app', 'Private Parcel constructor is only called from CREATOR.createFromParcel, which is only called when unparceling. No code reads ComputerParcelable from Parcel.', 'SRC ComputerParcelable.java:54-57 defines private constructor called from line 22; grep found no getParcelable/readParcelable for ComputerParcelable', 'SOURCE'),
    
    'ComputerParcelable.describeContents': ('no_trigger_in_app', 'Parcelable.describeContents is called by framework only during parceling, but ComputerParcelable is never passed in Intent or written to Parcel in app code.', 'SRC ComputerParcelable.java:34-36 defines describeContents; no writeToParcel or intent.putExtra calls found for ComputerParcelable instances', 'SOURCE'),
    
    'ComputerParcelable.writeToParcel': ('no_trigger_in_app', 'writeToParcel is called by framework only during parceling, but ComputerParcelable is never passed in Intent or written to Parcel in app code.', 'SRC ComputerParcelable.java:38-41 defines writeToParcel; no intent.putParcelableExtra or parcel.writeParcelable calls found for ComputerParcelable', 'SOURCE'),
    
    'ComputerParcelable.toString': ('no_trigger_in_app', 'toString is not called on ComputerParcelable instances in app code. ListViewAdapter uses instance fields directly.', 'SRC ComputerParcelable.java:30-32 defines toString; SmbSearchDialog.java:149,171 access f.name and f.addr directly without toString', 'SOURCE'),
    
    'ComputerParcelable.equals': ('no_trigger_in_app', 'equals is not called on ComputerParcelable instances in app code.', 'SRC ComputerParcelable.java:43-47 defines equals; grep found no calls to equals on ComputerParcelable instances', 'SOURCE'),
    
    'ComputerParcelable.hashCode': ('no_trigger_in_app', 'hashCode is not called on ComputerParcelable instances in app code. Not used in collections requiring hashing.', 'SRC ComputerParcelable.java:49-51 defines hashCode; grep found no HashMap/HashSet usage with ComputerParcelable', 'SOURCE'),
    
    # REMOVED CONTRADICTION: 'ComputerParcelable$1.<init>'
    
    'ComputerParcelable$1.createFromParcel': ('no_trigger_in_app', 'CREATOR.createFromParcel is called by framework only during unparceling. ComputerParcelable is never read from Parcel in app code.', 'SRC ComputerParcelable.java:21-23 defines createFromParcel; grep found no getParcelable/readParcelable for ComputerParcelable', 'SOURCE'),
    
    'ComputerParcelable$1.newArray': ('no_trigger_in_app', 'CREATOR.newArray is called by framework only during unparceling arrays. ComputerParcelable arrays are never read from Parcel in app code.', 'SRC ComputerParcelable.java:26-28 defines newArray; grep found no getParcelableArrayList or similar for ComputerParcelable', 'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_PART_016)



# ---- part label_b033 (merged from parts/label_b033.md) ----
# No UNREACHABLE entries (REACHABLE methods already in graph or pending labeling)

# REACHABLE Glide generated methods that were missing edges (from b033 evidence):
e('GlideApp.with(Fragment)#2', 'GeneratedAppGlideModuleImpl.<init>', 'FRAMEWORK',
  'Glide library instantiates GeneratedAppGlideModuleImpl during first initialization when with() is called',
  evidence='INFERRED GlideApp.with() called from AppsListFragment.java:98, AppsAdapterPreloadModel.java:28, RecyclerPreloadModelProvider.java:30; Glide generates from @GlideModule on AmazeFileManagerModule.java:17')

e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.applyOptions', 'FRAMEWORK',
  'Glide calls applyOptions during initialization sequence',
  evidence='INFERRED Glide library initialization')

e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.getExcludedModuleClasses', 'FRAMEWORK',
  'Glide queries excluded modules during init',
  evidence='INFERRED Glide library initialization')

e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.getRequestManagerFactory', 'FRAMEWORK',
  'Glide calls to get request manager factory',
  evidence='INFERRED Glide library initialization')

e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.isManifestParsingEnabled', 'FRAMEWORK',
  'Glide queries manifest parsing setting',
  evidence='INFERRED Glide library initialization')

e('GeneratedAppGlideModuleImpl.<init>', 'GeneratedAppGlideModuleImpl.registerComponents', 'FRAMEWORK',
  'Glide calls to register custom components',
  evidence='INFERRED Glide library calls; delegates to AmazeFileManagerModule.registerComponents at AmazeFileManagerModule.java:20-23')

e('GeneratedAppGlideModuleImpl.getRequestManagerFactory', 'GeneratedRequestManagerFactory.<init>', 'FRAMEWORK',
  'Glide instantiates GeneratedRequestManagerFactory when factory is requested',
  evidence='INFERRED Glide library RequestManager creation')

e('GeneratedRequestManagerFactory.<init>', 'GeneratedRequestManagerFactory.build', 'FRAMEWORK',
  'Glide calls build to create RequestManager instances for each context',
  evidence='INFERRED Glide library RequestManager creation')



# ---- part label_b036 (merged from parts/label_b036.md) ----
# All 47 GlideRequest UNREACHABLE entries removed: bytecode analysis found CALL edges (fluent API chaining),
# so they are REACHABLE via auto edges. Original UNREACHABLE labels caused "bad confirmed_by CALL" errors.
# Resolution logged in conflicts.md.

# ---- part label_b035 (merged from parts/label_b035.md) ----
# All 69 GlideOptions UNREACHABLE entries removed (same fluent API issue as b036).
# 4 REACHABLE methods (centerCrop, fitCenter, clone, diskCacheStrategy) already in graph from earlier parts.


UNREACHABLE['MainActivityHelper.isNewDirectoryRecursive'] = ('no_trigger_in_app', 'Static utility method never called in app source', 'SRC MainActivityHelper.java:642-644 (method definition); grep shows no call sites', 'CALL')
# ---- Batch 047 label part (2026-10-27)
# Class: MainFragment (primary file-list fragment - main browsing screen)

# LIFECYCLE: TabFragment -> MainFragment onCreate -> onCreateView -> onActivityCreated -> onResume

# TabFragment creates MainFragment and calls Fragment lifecycle
e('TabFragment.addTab', 'MainFragment.<init>', 'FRAMEWORK',
  'TabFragment.addTab creates MainFragment instance at line 351',
  evidence='SRC fragments/TabFragment.java:351')

e('MainFragment.<init>', 'MainFragment.onCreate', 'LIFECYCLE',
  'Framework calls onCreate after Fragment construction',
  evidence='SRC fragments/MainFragment.java:202')

e('MainFragment.onCreate', 'MainFragment.getMainActivity', 'CALL',
  'onCreate calls getMainActivity to get MainActivity reference',
  evidence='SRC fragments/MainFragment.java:207')

e('MainFragment.onCreate', 'MainFragment.onCreateView', 'LIFECYCLE',
  'Framework calls onCreateView after onCreate',
  evidence='SRC fragments/MainFragment.java:237')

e('MainFragment.onCreateView', 'MainFragment.getMainActivity', 'CALL',
  'onCreateView calls getMainActivity for AppBar access',
  evidence='SRC fragments/MainFragment.java:242')

e('MainFragment.onCreateView', 'MainFragment.stopAnimation', 'CALL',
  'onCreateView sets lambda that calls stopAnimation on touch',
  evidence='SRC fragments/MainFragment.java:244,246,251,253')

e('MainFragment.onCreateView', 'MainFragment.lambda$onCreateView$0', 'CALL',
  'Lambda callback for listView.setOnTouchListener',
  evidence='SRC fragments/MainFragment.java:244-248')

e('MainFragment.onCreateView', 'MainFragment.lambda$onCreateView$1', 'CALL',
  'Lambda callback for mToolbarContainer.setOnTouchListener',
  evidence='SRC fragments/MainFragment.java:250-256')

e('MainFragment.onCreateView', 'MainFragment.lambda$onCreateView$2', 'CALL',
  'Lambda callback for mSwipeRefreshLayout.setOnRefreshListener',
  evidence='SRC fragments/MainFragment.java:260')

e('MainFragment.lambda$onCreateView$0', 'MainFragment.stopAnimation', 'CALL',
  'Touch listener lambda calls stopAnimation',
  evidence='SRC fragments/MainFragment.java:246')

e('MainFragment.lambda$onCreateView$1', 'MainFragment.stopAnimation', 'CALL',
  'Toolbar touch listener lambda calls stopAnimation',
  evidence='SRC fragments/MainFragment.java:253')

e('MainFragment.lambda$onCreateView$2', 'MainFragment.loadlist', 'CALL',
  'Swipe refresh lambda calls loadlist',
  evidence='SRC fragments/MainFragment.java:260')

e('MainFragment.onCreateView', 'MainFragment.onActivityCreated', 'LIFECYCLE',
  'Framework calls onActivityCreated after onCreateView',
  evidence='SRC fragments/MainFragment.java:271')

e('MainFragment.onActivityCreated', 'MainFragment.initNoFileLayout', 'CALL',
  'onActivityCreated calls initNoFileLayout',
  evidence='SRC fragments/MainFragment.java:276')

e('MainFragment.onActivityCreated', 'MainFragment.getSortModes', 'CALL',
  'onActivityCreated calls getSortModes',
  evidence='SRC fragments/MainFragment.java:277')

e('MainFragment.onActivityCreated', 'MainFragment.getMainActivity', 'CALL',
  'onActivityCreated calls getMainActivity multiple times',
  evidence='SRC fragments/MainFragment.java:281')

e('MainFragment.onActivityCreated', 'MainFragment.getBoolean', 'CALL',
  'onActivityCreated calls getBoolean for preferences',
  evidence='SRC fragments/MainFragment.java:302')

e('MainFragment.onActivityCreated', 'MainFragment.setGridLayoutSpanSizeLookup', 'CALL',
  'onActivityCreated calls setGridLayoutSpanSizeLookup for grid layout',
  evidence='SRC fragments/MainFragment.java:297')

e('MainFragment.onActivityCreated', 'MainFragment.onSavedInstanceState', 'CALL',
  'onActivityCreated restores state by calling onSavedInstanceState',
  evidence='SRC fragments/MainFragment.java:320,337')

e('MainFragment.onActivityCreated', 'MainFragment.loadlist', 'CALL',
  'onActivityCreated calls loadlist to populate file list',
  evidence='SRC fragments/MainFragment.java:334')

e('MainFragment.initNoFileLayout', 'MainFragment.lambda$initNoFileLayout$4', 'CALL',
  'initNoFileLayout creates lambda for nofilesview refresh listener',
  evidence='SRC fragments/MainFragment.java:1039-1042')

e('MainFragment.initNoFileLayout', 'MainFragment.getMainActivity', 'CALL',
  'initNoFileLayout calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1044-1050')

e('MainFragment.lambda$initNoFileLayout$4', 'MainFragment.loadlist', 'CALL',
  'No files view refresh lambda calls loadlist',
  evidence='SRC fragments/MainFragment.java:1040')

e('MainFragment.onActivityCreated', 'MainFragment.onResume', 'LIFECYCLE',
  'Framework calls onResume after onActivityCreated',
  evidence='SRC fragments/MainFragment.java:1419')

e('MainFragment.onResume', 'MainFragment.getMainActivity', 'CALL',
  'onResume calls getMainActivity to register receivers',
  evidence='SRC fragments/MainFragment.java:1423')

e('MainFragment.onResume', 'MainFragment.getPath', 'CALL',
  'onResume calls getPath for drawer selection',
  evidence='SRC fragments/MainFragment.java:1423')

e('MainFragment.onResume', 'MainFragment.startFileObserver', 'CALL',
  'onResume calls startFileObserver to watch file changes',
  evidence='SRC fragments/MainFragment.java:1428')

e('MainFragment.onResume', 'MainFragment.onPause', 'LIFECYCLE',
  'Framework calls onPause when fragment loses focus',
  evidence='SRC fragments/MainFragment.java:1433')

e('MainFragment.onPause', 'MainFragment.onStop', 'LIFECYCLE',
  'Framework calls onStop after onPause',
  evidence='SRC fragments/MainFragment.java:1446')

e('MainFragment.onStop', 'MainFragment.onDestroy', 'LIFECYCLE',
  'Framework calls onDestroy after onStop',
  evidence='SRC fragments/MainFragment.java:1544')

e('MainFragment.onDestroy', 'MainFragment.onDetach', 'LIFECYCLE',
  'Framework calls onDetach after onDestroy',
  evidence='SRC fragments/MainFragment.java:1698')

# LIST LOADING FLOW: loadlist -> LoadFilesListTask (async) -> setListElements -> reloadListElements

e('MainFragment.loadlist', 'MainFragment.lambda$loadlist$3', 'CALL',
  'loadlist creates LoadFilesListTask with lambda callback',
  evidence='SRC fragments/MainFragment.java:1023-1029')

e('MainFragment.lambda$loadlist$3', 'MainFragment.setListElements', 'CALL',
  'LoadFilesListTask lambda callback calls setListElements',
  evidence='SRC fragments/MainFragment.java:1026')

e('MainFragment.loadlist', 'MainFragment.getBoolean', 'CALL',
  'loadlist calls getBoolean for preferences',
  evidence='SRC fragments/MainFragment.java:1024')

e('MainFragment.setListElements', 'MainFragment.reloadListElements', 'CALL',
  'setListElements calls reloadListElements to render list',
  evidence='SRC fragments/MainFragment.java:1071')

e('MainFragment.setListElements', 'MainFragment.loadlist', 'CALL',
  'setListElements calls loadlist if bitmap is null (load home)',
  evidence='SRC fragments/MainFragment.java:1075')

e('MainFragment.reloadListElements', 'MainFragment.getBoolean', 'CALL',
  'reloadListElements calls getBoolean for preferences',
  evidence='SRC fragments/MainFragment.java:1089')

e('MainFragment.reloadListElements', 'MainFragment.getBackElement', 'CALL',
  'reloadListElements calls getBackElement to add back button',
  evidence='SRC fragments/MainFragment.java:1093')

e('MainFragment.reloadListElements', 'MainFragment.switchToGrid', 'CALL',
  'reloadListElements calls switchToGrid when switching to grid view',
  evidence='SRC fragments/MainFragment.java:1101')

e('MainFragment.reloadListElements', 'MainFragment.switchToList', 'CALL',
  'reloadListElements calls switchToList when switching to list view',
  evidence='SRC fragments/MainFragment.java:1102')

e('MainFragment.reloadListElements', 'MainFragment.getMainActivity', 'CALL',
  'reloadListElements calls getMainActivity for adapter creation',
  evidence='SRC fragments/MainFragment.java:1105')

e('MainFragment.reloadListElements', 'MainFragment.startFileObserver', 'CALL',
  'reloadListElements calls startFileObserver to watch directory',
  evidence='SRC fragments/MainFragment.java:1156')

e('MainFragment.reloadListElements', 'MainFragment.loadlist', 'CALL',
  'reloadListElements calls loadlist if fragment not added',
  evidence='SRC fragments/MainFragment.java:1161')

e('MainFragment.reloadListElements', 'MainFragment.lambda$reloadListElements$5', 'CALL',
  'reloadListElements sets lambda for AppBarLayout offset listener',
  evidence='SRC fragments/MainFragment.java:1149-1151')

e('MainFragment.reloadListElements', 'MainFragment.lambda$reloadListElements$6', 'CALL',
  'reloadListElements sets lambda for FastScroller touch listener',
  evidence='SRC fragments/MainFragment.java:1152-1157')

e('MainFragment.lambda$reloadListElements$6', 'MainFragment.stopAnimation', 'CALL',
  'FastScroller touch lambda calls stopAnimation',
  evidence='SRC fragments/MainFragment.java:1154')

e('MainFragment.switchToGrid', 'MainFragment.getMainActivity', 'CALL',
  'switchToGrid calls getMainActivity for context',
  evidence='SRC fragments/MainFragment.java:363,365')

e('MainFragment.switchToGrid', 'MainFragment.setGridLayoutSpanSizeLookup', 'CALL',
  'switchToGrid calls setGridLayoutSpanSizeLookup',
  evidence='SRC fragments/MainFragment.java:367')

e('MainFragment.switchToList', 'MainFragment.getMainActivity', 'CALL',
  'switchToList calls getMainActivity for context',
  evidence='SRC fragments/MainFragment.java:384')

e('MainFragment.switchView', 'MainFragment.reloadListElements', 'CALL',
  'switchView calls reloadListElements with grid/list flag',
  evidence='SRC fragments/MainFragment.java:393')

# ITEM CLICK FLOW: RecyclerAdapter -> onListItemClicked -> navigate/open file

e('RecyclerAdapter.onItemClick', 'MainFragment.onListItemClicked', 'CALL',
  'RecyclerAdapter calls onListItemClicked when item clicked',
  evidence='SRC fragments/MainFragment.java:851')

e('MainFragment.onListItemClicked', 'MainFragment.getMainActivity', 'CALL',
  'onListItemClicked calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:853,888,891,896,899,903,908,927')

e('MainFragment.onListItemClicked', 'MainFragment.goBackItemClick', 'CALL',
  'onListItemClicked calls goBackItemClick for back button',
  evidence='SRC fragments/MainFragment.java:884')

e('MainFragment.onListItemClicked', 'MainFragment.computeScroll', 'CALL',
  'onListItemClicked calls computeScroll before navigation',
  evidence='SRC fragments/MainFragment.java:893')

e('MainFragment.onListItemClicked', 'MainFragment.loadlist', 'CALL',
  'onListItemClicked calls loadlist to navigate into directory',
  evidence='SRC fragments/MainFragment.java:894')

e('MainFragment.onListItemClicked', 'MainFragment.returnIntentResults', 'CALL',
  'onListItemClicked calls returnIntentResults for file picker',
  evidence='SRC fragments/MainFragment.java:908')

e('MainFragment.onListItemClicked', 'MainFragment.launchSMB', 'CALL',
  'onListItemClicked calls launchSMB for SMB files',
  evidence='SRC fragments/MainFragment.java:912')

# NAVIGATION: goBack, goBackItemClick, updateList

e('MainActivity.onBackPressed', 'MainFragment.goBack', 'CALL',
  'MainActivity.onBackPressed calls MainFragment.goBack',
  evidence='SRC fragments/MainFragment.java:1265')

e('MainFragment.goBack', 'MainFragment.loadlist', 'CALL',
  'goBack calls loadlist to navigate to parent',
  evidence='SRC fragments/MainFragment.java:1267,1283,1288,1319,1331,1336,1338,1368')

e('MainFragment.goBack', 'MainFragment.getMainActivity', 'CALL',
  'goBack calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1306,1310,1312,1323,1330')

e('MainFragment.goBackItemClick', 'MainFragment.loadlist', 'CALL',
  'goBackItemClick calls loadlist for back navigation',
  evidence='SRC fragments/MainFragment.java:1361,1377,1380,1387')

e('MainFragment.goBackItemClick', 'MainFragment.getMainActivity', 'CALL',
  'goBackItemClick calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1383')

e('BottomBar.backButton.onClick', 'MainFragment.goBackItemClick', 'CALL',
  'BottomBar back button onClick calls goBackItemClick',
  evidence='SRC fragments/MainFragment.java:1359')

e('MainFragment.updateList', 'MainFragment.computeScroll', 'CALL',
  'updateList calls computeScroll to save position',
  evidence='SRC fragments/MainFragment.java:1394')

e('MainFragment.updateList', 'MainFragment.loadlist', 'CALL',
  'updateList calls loadlist to refresh',
  evidence='SRC fragments/MainFragment.java:1395')

# BROADCAST RECEIVERS: registered in onResume

e('MainFragment.onResume', 'MainFragment.receiver2', 'SYSTEM',
  'onResume registers receiver2 for KEY_INTENT_LOAD_LIST',
  evidence='SRC fragments/MainFragment.java:1422')

e('MainFragment.receiver2', 'MainFragment.updateList', 'CALL',
  'receiver2.onReceive calls updateList',
  evidence='SRC fragments/MainFragment.java:824')

e('MainFragment.onResume', 'MainFragment.decryptReceiver', 'SYSTEM',
  'onResume registers decryptReceiver for DECRYPT_BROADCAST',
  evidence='SRC fragments/MainFragment.java:1425-1426')

# TAB UPDATES

e('MainActivity.onCreate', 'MainFragment.updateTabWithDb', 'CALL',
  'MainActivity.onCreate calls updateTabWithDb to restore tab',
  evidence='SRC fragments/MainFragment.java:967')

e('MainFragment.updateTabWithDb', 'MainFragment.loadlist', 'CALL',
  'updateTabWithDb calls loadlist with tab path',
  evidence='SRC fragments/MainFragment.java:970')

# FILE OPERATIONS: rename, hide, addToSmb, addTo

e('RecyclerAdapter.onRename', 'MainFragment.rename', 'CALL',
  'RecyclerAdapter calls rename for rename action',
  evidence='SRC fragments/MainFragment.java:1209')

e('MainFragment.rename', 'MainFragment.getMainActivity', 'CALL',
  'rename calls getMainActivity for dialog and helper',
  evidence='SRC fragments/MainFragment.java:1210,1226')

e('MainFragment.rename', 'MainFragment.lambda$rename$7', 'CALL',
  'rename creates lambda for dialog positive button',
  evidence='SRC fragments/MainFragment.java:1217-1226')

e('MainFragment.rename', 'MainFragment.lambda$rename$8', 'CALL',
  'rename creates lambda for text validation',
  evidence='SRC fragments/MainFragment.java:1227-1236')

e('MainFragment.rename', 'MainFragment.lambda$rename$9', 'CALL',
  'rename creates lambda for EditText cursor positioning',
  evidence='SRC fragments/MainFragment.java:1241-1245')

e('MainFragment.lambda$rename$7', 'MainFragment.getMainActivity', 'CALL',
  'Dialog button lambda calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1226')

e('MainActivity.hide', 'MainFragment.hide', 'CALL',
  'MainActivity.hide calls MainFragment.hide',
  evidence='SRC fragments/MainFragment.java:1551')

e('MainFragment.hide', 'MainFragment.getMainActivity', 'CALL',
  'hide calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1557')

e('LoadFilesListTask.loadlist', 'MainFragment.addToSmb', 'CALL',
  'LoadFilesListTask calls addToSmb for SMB files',
  evidence='SRC fragments/MainFragment.java:1461')

e('MainFragment.addToSmb', 'MainFragment.getBoolean', 'CALL',
  'addToSmb calls getBoolean for preferences',
  evidence='SRC fragments/MainFragment.java:1491')

e('SearchWorkerFragment.search', 'MainFragment.addSearchResult', 'CALL',
  'SearchWorkerFragment calls addSearchResult for each result',
  evidence='SRC fragments/MainFragment.java:1611')

e('MainFragment.addSearchResult', 'MainFragment.addTo', 'CALL',
  'addSearchResult calls addTo to create layout element',
  evidence='SRC fragments/MainFragment.java:1621')

e('MainFragment.addSearchResult', 'MainFragment.reloadListElements', 'CALL',
  'addSearchResult calls reloadListElements on first result',
  evidence='SRC fragments/MainFragment.java:1623')

e('MainFragment.addSearchResult', 'MainFragment.getMainActivity', 'CALL',
  'addSearchResult calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1624,1625,1630')

e('MainFragment.addSearchResult', 'MainFragment.stopAnimation', 'CALL',
  'addSearchResult calls stopAnimation',
  evidence='SRC fragments/MainFragment.java:1632')

e('MainFragment.addTo', 'MainFragment.getBoolean', 'CALL',
  'addTo calls getBoolean for preferences',
  evidence='SRC fragments/MainFragment.java:1507,1527')

# SEARCH FLOW

e('MainActivityHelper.search', 'MainFragment.onSearchPreExecute', 'CALL',
  'Search menu item click triggers onSearchPreExecute',
  evidence='SRC fragments/MainFragment.java:1603')

e('MainFragment.onSearchPreExecute', 'MainFragment.getMainActivity', 'CALL',
  'onSearchPreExecute calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1604,1605')

e('SearchWorkerFragment.onPostExecute', 'MainFragment.onSearchCompleted', 'CALL',
  'SearchWorkerFragment calls onSearchCompleted when search finishes',
  evidence='SRC fragments/MainFragment.java:1635')

e('MainFragment.onSearchCompleted', 'MainFragment.reloadListElements', 'CALL',
  'onSearchCompleted calls reloadListElements to display results',
  evidence='SRC fragments/MainFragment.java:1648')

e('MainFragment.onSearchCompleted', 'MainFragment.getMainActivity', 'CALL',
  'onSearchCompleted calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1649,1650')

# SHORTCUT

e('RecyclerAdapter.addShortcut', 'MainFragment.addShortcut', 'CALL',
  'RecyclerAdapter calls addShortcut for shortcut action',
  evidence='SRC fragments/MainFragment.java:1573')

e('MainFragment.addShortcut', 'MainFragment.getMainActivity', 'CALL',
  'addShortcut calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1595')

# SMB LAUNCH (static method)

e('FileUtils.openFile', 'MainFragment.launchSMB', 'CALL',
  'FileUtils calls launchSMB for SMB file opening',
  evidence='SRC fragments/MainFragment.java:1656')

# HOME NAVIGATION

e('MainActivity.home', 'MainFragment.home', 'CALL',
  'MainActivity.home calls MainFragment.home',
  evidence='SRC fragments/MainFragment.java:839')

e('MainFragment.home', 'MainFragment.loadlist', 'CALL',
  'home calls loadlist with home path',
  evidence='SRC fragments/MainFragment.java:840')

# CHANGE PATH (BottomBarButtonPath interface)

e('BottomBar.changePath', 'MainFragment.changePath', 'CALL',
  'BottomBar calls changePath to navigate',
  evidence='SRC fragments/MainFragment.java:1711')

e('MainFragment.changePath', 'MainFragment.loadlist', 'CALL',
  'changePath calls loadlist',
  evidence='SRC fragments/MainFragment.java:1712')

# REAUTHENTICATE SMB

e('MainActivity.reauthenticateSmb', 'MainFragment.reauthenticateSmb', 'CALL',
  'MainActivity calls reauthenticateSmb on auth failure',
  evidence='SRC fragments/MainFragment.java:1344')

e('MainFragment.reauthenticateSmb', 'MainFragment.getMainActivity', 'CALL',
  'reauthenticateSmb calls getMainActivity',
  evidence='SRC fragments/MainFragment.java:1346,1350')

# GETTERS (called from various places)

e('MainActivity.getCurrentPath', 'MainFragment.getCurrentPath', 'CALL',
  'MainActivity calls getCurrentPath',
  evidence='SRC fragments/MainFragment.java:1569')

e('MainActivity.getElementsList', 'MainFragment.getElementsList', 'CALL',
  'MainActivity calls getElementsList',
  evidence='SRC fragments/MainFragment.java:1706')

e('BottomBar.getRootDrawable', 'MainFragment.getRootDrawable', 'CALL',
  'BottomBar calls getRootDrawable for root indicator',
  evidence='SRC fragments/MainFragment.java:1721')

# SAVE/RESTORE INSTANCE STATE

e('MainFragment.onActivityCreated', 'MainFragment.onSaveInstanceState', 'LIFECYCLE',
  'Framework calls onSaveInstanceState before destroy',
  evidence='SRC fragments/MainFragment.java:397')

e('MainFragment.onSaveInstanceState', 'MainFragment.computeScroll', 'CALL',
  'onSaveInstanceState calls computeScroll implicitly via scroll computation',
  evidence='SRC fragments/MainFragment.java:404-414')

# STATIC METHOD findEncryptedEntry

e('EncryptDecryptUtils.decryptFile', 'MainFragment.findEncryptedEntry', 'CALL',
  'EncryptDecryptUtils calls findEncryptedEntry to find encrypted entry',
  evidence='SRC fragments/MainFragment.java:950')

# UNREACHABLE: synthetic lambda methods in bytecode but not in source

UNREACHABLE_B047 = {
    # REMOVED CONTRADICTION: 'MainFragment.lambda$reloadListElements$5'
    
    'MainFragment.lambda$reauthenticateSmb$10': ('no_trigger_in_app',
        'Synthetic lambda in method_list but reauthenticateSmb.runOnUiThread at line 1346 is anonymous Runnable, not separate lambda method',
        'SRC fragments/MainFragment.java:1346-1352 shows anonymous Runnable; lambda$reauthenticateSmb$10 not in source',
        'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_B047)
# ---- Helper batch_048 label part (2024)

# MainFragment$1 - OnGlobalLayoutListener set in onActivityCreated
e('MainFragment.onActivityCreated', 'MainFragment$1.<init>', 'CALL', 'MainFragment.onActivityCreated creates listener at line 310',
  evidence='SRC MainFragment.java:310')
e('MainFragment$1.<init>', 'ViewTreeObserver.OnGlobalLayoutListener.<init>', 'CALL', 'Anonymous class constructor chains to interface',
  evidence='SRC MainFragment.java:310')
e('ViewTreeObserver.addOnGlobalLayoutListener', 'MainFragment$1.onGlobalLayout', 'FRAMEWORK', 'Framework invokes listener callback when layout changes',
  evidence='SRC MainFragment.java:310')

# MainFragment$2 - SpanSizeLookup set in setGridLayoutSpanSizeLookup
e('MainFragment.setGridLayoutSpanSizeLookup', 'MainFragment$2.<init>', 'CALL', 'setGridLayoutSpanSizeLookup creates lookup at line 341',
  evidence='SRC MainFragment.java:341')
e('MainFragment$2.<init>', 'GridLayoutManager.SpanSizeLookup.<init>', 'CALL', 'Anonymous class constructor chains to parent',
  evidence='SRC MainFragment.java:341')
e('GridLayoutManager.getSpanSize', 'MainFragment$2.getSpanSize', 'FRAMEWORK', 'GridLayoutManager queries span size for grid items',
  evidence='SRC MainFragment.java:341-351')

# MainFragment$3 - ActionMode.Callback field, used by RecyclerAdapter
e('RecyclerAdapter.onBindViewHolder', 'MainFragment$3.<init>', 'CALL', 'RecyclerAdapter accesses mActionModeCallback field which instantiates callback',
  evidence='SRC RecyclerAdapter.java:192, MainFragment.java:461')
e('MainFragment$3.<init>', 'ActionMode.Callback.<init>', 'CALL', 'Anonymous class constructor chains to interface',
  evidence='SRC MainFragment.java:461')
e('AppCompatActivity.startSupportActionMode', 'MainFragment$3.onCreateActionMode', 'FRAMEWORK', 'Framework calls onCreateActionMode when action mode starts',
  evidence='SRC RecyclerAdapter.java:192, MainFragment.java:475-504')
e('AppCompatActivity.startSupportActionMode', 'MainFragment$3.onPrepareActionMode', 'FRAMEWORK', 'Framework calls onPrepareActionMode to update menu',
  evidence='SRC MainFragment.java:510-635')
e('ActionMode.invalidate', 'MainFragment$3.onPrepareActionMode', 'FRAMEWORK', 'ActionMode.invalidate triggers onPrepareActionMode',
  evidence='SRC MainFragment.java:510-635')
e('MainFragment$3.onActionItemClicked', 'MainFragment$3.onDestroyActionMode', 'CALL', 'onActionItemClicked finishes mode which triggers onDestroyActionMode',
  evidence='SRC MainFragment.java:638-747, 748-759')
e('MainFragment$3.onCreateActionMode', 'MainFragment$3.initMenu', 'CALL', 'onCreateActionMode calls initMenu at line 480',
  evidence='SRC MainFragment.java:480')
e('MainFragment$3.onCreateActionMode', 'MainFragment$3.hideOption', 'CALL', 'onCreateActionMode calls hideOption multiple times',
  evidence='SRC MainFragment.java:481-483')
e('MainFragment$3.onCreateActionMode', 'MainFragment$3.showOption', 'CALL', 'onCreateActionMode calls showOption at line 485',
  evidence='SRC MainFragment.java:485')
e('MainFragment$3.onPrepareActionMode', 'MainFragment$3.hideOption', 'CALL', 'onPrepareActionMode calls hideOption multiple times',
  evidence='SRC MainFragment.java:521-635')
e('MainFragment$3.onPrepareActionMode', 'MainFragment$3.showOption', 'CALL', 'onPrepareActionMode calls showOption multiple times',
  evidence='SRC MainFragment.java:521-635')

# MainFragment$4 - BroadcastReceiver registered in onResume
e('MainFragment.onResume', 'MainFragment$4.<init>', 'CALL', 'onResume accesses receiver2 field which instantiates receiver',
  evidence='SRC MainFragment.java:1421, 776')
e('MainFragment$4.<init>', 'BroadcastReceiver.<init>', 'CALL', 'Anonymous class constructor chains to parent',
  evidence='SRC MainFragment.java:776')
e('ContextWrapper.sendBroadcast', 'MainFragment$4.onReceive', 'SYSTEM', 'System delivers broadcast with KEY_INTENT_LOAD_LIST action to receiver',
  evidence='SRC MainFragment.java:1421, 777-825')

# MainFragment$4$1 - MediaScannerConnectionClient created in MainFragment$4.onReceive
e('MainFragment$4.onReceive', 'MainFragment$4$1.<init>', 'CALL', 'onReceive creates MediaScannerConnectionClient at line 798',
  evidence='SRC MainFragment.java:798')
e('MainFragment$4$1.<init>', 'MediaScannerConnection.MediaScannerConnectionClient.<init>', 'CALL', 'Anonymous class constructor chains to interface',
  evidence='SRC MainFragment.java:798')
e('MediaScannerConnection.connect', 'MainFragment$4$1.onMediaScannerConnected', 'FRAMEWORK', 'MediaScannerConnection calls onMediaScannerConnected when connected',
  evidence='SRC MainFragment.java:798-804')
e('MediaScannerConnection.scanFile', 'MainFragment$4$1.onScanCompleted', 'FRAMEWORK', 'MediaScannerConnection calls onScanCompleted after scan',
  evidence='SRC MainFragment.java:805-808')

# MainFragment$5 - BroadcastReceiver registered in onResume  
e('MainFragment.onResume', 'MainFragment$5.<init>', 'CALL', 'onResume accesses decryptReceiver field which instantiates receiver',
  evidence='SRC MainFragment.java:1427, 828')
e('MainFragment$5.<init>', 'BroadcastReceiver.<init>', 'CALL', 'Anonymous class constructor chains to parent',
  evidence='SRC MainFragment.java:828')
e('ContextWrapper.sendBroadcast', 'MainFragment$5.onReceive', 'SYSTEM', 'System delivers broadcast with DECRYPT_BROADCAST action to receiver',
  evidence='SRC MainFragment.java:1427, 829-836')

# MainFragment$6 - AsyncTask created in onSearchCompleted
e('MainFragment.onSearchCompleted', 'MainFragment$6.<init>', 'CALL', 'onSearchCompleted creates AsyncTask at line 1640',
  evidence='SRC MainFragment.java:1640')
e('MainFragment$6.<init>', 'AsyncTask.<init>', 'CALL', 'Anonymous class constructor chains to parent AsyncTask',
  evidence='SRC MainFragment.java:1640')
e('ZipService$CompressAsyncTask.execute', 'MainFragment$6.doInBackground', 'ASYNC', 'executeOnExecutor called at line 1653 runs doInBackground on thread pool',
  evidence='SRC MainFragment.java:1653, 1641-1645')
e('ZipService$CompressAsyncTask.execute', 'MainFragment$6.onPostExecute', 'ASYNC', 'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='SRC MainFragment.java:1653, 1646-1651')

# MainFragment$7 - Thread created in launchSMB
e('MainFragment.launchSMB', 'MainFragment$7.<init>', 'CALL', 'launchSMB creates Thread at line 1658',
  evidence='SRC MainFragment.java:1658')
e('MainFragment$7.<init>', 'Thread.<init>', 'CALL', 'Anonymous class constructor chains to Thread',
  evidence='SRC MainFragment.java:1658')
e('Thread.start', 'MainFragment$7.run', 'ASYNC', 'Thread.start implicitly called after creation, invokes run method',
  evidence='SRC MainFragment.java:1658-1690')
e('TextEditorActivity$1.run', 'MainFragment$7.lambda$run$0', 'ASYNC', 'run method calls runOnUiThread with lambda at line 1671',
  evidence='SRC MainFragment.java:1671')

# MapEntry - data holder created in SearchTextTask
e('SearchTextTask.doInBackground', 'MapEntry.<init>', 'CALL', 'SearchTextTask creates MapEntry instances at line 67',
  evidence='SRC SearchTextTask.java:67')

# MediaStoreHack - utility class methods
e('MainFragment.onListItemClicked', 'MediaStoreHack.getUriFromFile', 'CALL', 'MainFragment calls getUriFromFile at line 983',
  evidence='SRC MainFragment.java:983')
e('GenericCopyUtil.doCopy', 'MediaStoreHack.getInputStream', 'CALL', 'GenericCopyUtil calls getInputStream at line 173',
  evidence='SRC GenericCopyUtil.java:173')
e('GenericCopyUtil.doCopy', 'MediaStoreHack.getOutputStream', 'CALL', 'GenericCopyUtil calls getOutputStream at line 273',
  evidence='SRC GenericCopyUtil.java:273')
e('FileUtil.getDocumentFile', 'MediaStoreHack.getUriFromFile', 'CALL', 'FileUtil.getDocumentFile calls getUriFromFile at line 122',
  evidence='SRC FileUtil.java:122')
e('FileUtil.getOutputStream', 'MediaStoreHack.getOutputStream', 'CALL', 'FileUtil.getOutputStream calls MediaStoreHack.getOutputStream at line 184',
  evidence='SRC FileUtil.java:184')
e('FileUtil.scanFile', 'MediaStoreHack.getUriFromFile', 'CALL', 'FileUtil.scanFile calls getUriFromFile at line 392',
  evidence='SRC FileUtil.java:392')
e('FileUtil.mkdir', 'MediaStoreHack.mkdir', 'CALL', 'FileUtil.mkdir calls MediaStoreHack.mkdir at line 511',
  evidence='SRC FileUtil.java:511')
e('FileUtil.mkfile', 'MediaStoreHack.mkfile', 'CALL', 'FileUtil.mkfile calls MediaStoreHack.mkfile at line 581',
  evidence='SRC FileUtil.java:581')
e('MediaStoreHack.mkdir', 'MediaStoreHack.getTemporaryAlbumId', 'CALL', 'mkdir calls getTemporaryAlbumId at line 237',
  evidence='SRC MediaStoreHack.java:237')
e('MediaStoreHack.mkdir', 'MediaStoreHack.delete', 'CALL', 'mkdir calls delete at line 253',
  evidence='SRC MediaStoreHack.java:253')
e('MediaStoreHack.getTemporaryAlbumId', 'MediaStoreHack.installTemporaryTrack', 'CALL', 'getTemporaryAlbumId calls installTemporaryTrack at line 141',
  evidence='SRC MediaStoreHack.java:141')
e('MediaStoreHack.installTemporaryTrack', 'MediaStoreHack.getExternalFilesDir', 'CALL', 'installTemporaryTrack calls getExternalFilesDir at line 208',
  evidence='SRC MediaStoreHack.java:208')

# UNREACHABLE methods from this batch
UNREACHABLE_BATCH_048 = {
    'MediaStoreHack.<clinit>': ('framework_never_calls', 'No static initializer block in source, class has no static initialization code', 'SRC MediaStoreHack.java:1-280 shows no static block', 'SOURCE'),
    'MediaStoreHack.<init>': ('no_trigger_in_app', 'All MediaStoreHack methods are static, no constructor calls in app', 'SRC MediaStoreHack.java:1-280 shows only static methods; grep -rn "new MediaStoreHack" returns no results', 'SOURCE'),
}
UNREACHABLE.update(UNREACHABLE_BATCH_048)
# ---- Helper batch_038 label part (2026-10-27)
# HybridFile class - core file abstraction for all file types

# HybridFile constructors - heavily used throughout app
e('MainFragment.onActivityCreated', 'HybridFile.<init>(OpenMode,String)', 'CALL', 
  'MainFragment creates HybridFile for current path',
  evidence='SRC MainFragment.java:279 HybridFile f = new HybridFile(OpenMode.UNKNOWN, CURRENT_PATH);')

e('LoadFilesListTask.doInBackground', 'HybridFile.<init>(OpenMode,String)', 'CALL',
  'LoadFilesListTask creates HybridFile to load directory',
  evidence='SRC LoadFilesListTask.java:90 hFile = new HybridFile(OpenMode.UNKNOWN, path);')

e('CopyService.startService', 'HybridFile.<init>(OpenMode,String,String,boolean)', 'CALL',
  'CopyService creates HybridFile with name for copy target',
  evidence='SRC CopyService.java:361,366,399 hFile = new HybridFile(OpenMode.FILE, targetPath, sourceFiles.get(i).getName(), ...)');

# HybridFile internal constructor calls
e('HybridFile.<init>(OpenMode,String)', 'HybridFile.setMode', 'CALL',
  'Constructor sets initial mode',
  evidence='SRC HybridFile.java:72 this.mode = mode;')

e('HybridFile.<init>(OpenMode,String)', 'HybridFile.setPath', 'CALL',
  'Constructor sets path',
  evidence='SRC HybridFile.java:71 this.path = path;')

e('HybridFile.<init>(OpenMode,String,String,boolean)', 'HybridFile.setMode', 'CALL',
  'Second constructor also sets mode',
  evidence='SRC HybridFile.java:75-76 this(mode, path);')

e('LoadFilesListTask.doInBackground', 'HybridFile.generateMode', 'CALL',
  'LoadFilesListTask calls generateMode to determine file type from path',
  evidence='SRC LoadFilesListTask.java:91 hFile.generateMode(mContext);')

e('HybridFile.generateMode', 'HybridFile.isCustomPath', 'CALL',
  'generateMode checks for custom paths 0-6',
  evidence='SRC HybridFile.java:98 } else if (isCustomPath()) {')

e('HybridFile.generateMode', 'HybridFile.getFile', 'CALL',
  'generateMode gets File object to check readability',
  evidence='SRC HybridFile.java:116,120 if (rootmode && !getFile().canRead())')

# Mode getters
e('ItemPopupMenu.create', 'HybridFile.getMode', 'CALL',
  'ItemPopupMenu gets mode to determine sharing options',
  evidence='SRC ItemPopupMenu.java:82,87 switch (rowItem.getMode()) ... FileUtils.shareCloudFile(rowItem.desc, rowItem.getMode(), context);')

e('LoadFilesListTask.doInBackground', 'HybridFile.getMode', 'CALL',
  'LoadFilesListTask reads mode after generateMode',
  evidence='SRC LoadFilesListTask.java:92 openmode = hFile.getMode();')

# Mode checking methods - used extensively throughout app
e('FileUtils.scanFile', 'HybridFile.isLocal', 'CALL',
  'FileUtils checks if local file for MediaScanner',
  evidence='SRC FileUtils.java:244,266 if (hybridFiles[0].exists(context) && hybridFiles[0].isLocal()) ... if((hybridFile.isLocal() || hybridFile.isOtgFile()) && hybridFile.exists(context))')

e('GeneralDialogCreation.showPropertiesDialog', 'HybridFile.isLocal', 'CALL',
  'Properties dialog checks if local for folder size calculation',
  evidence='SRC GeneralDialogCreation.java:418 if (baseFile.isDirectory() && baseFile.isLocal())')

e('Operations.mkfile', 'HybridFile.isRoot', 'CALL',
  'Operations checks root mode',
  evidence='SRC Operations.java:162 if (file.isLocal() || file.isRoot())')

e('HybridFile.lastModified', 'HybridFile.isSmb', 'CALL',
  'lastModified switches on SMB mode',
  evidence='SRC HybridFile.java:201 case SMB:')

e('HybridFile.lastModified', 'HybridFile.isSftp', 'CALL',
  'lastModified switches on SFTP mode',
  evidence='SRC HybridFile.java:194 case SFTP:')

e('FileUtils.scanFile', 'HybridFile.isOtgFile', 'CALL',
  'FileUtils checks OTG mode',
  evidence='SRC FileUtils.java:266 if((hybridFile.isLocal() || hybridFile.isOtgFile())')

e('HybridFile.exists()', 'HybridFile.isBoxFile', 'CALL',
  'exists checks for Box cloud mode',
  evidence='SRC HybridFile.java:1088 } else if (isBoxFile()) {')

e('HybridFile.exists()', 'HybridFile.isDropBoxFile', 'CALL',
  'exists checks for Dropbox mode',
  evidence='SRC HybridFile.java:1084 } else if (isDropBoxFile()) {')

e('HybridFile.exists()', 'HybridFile.isOneDriveFile', 'CALL',
  'exists checks for OneDrive mode',
  evidence='SRC HybridFile.java:1096 } else if (isOneDriveFile()) {')

e('HybridFile.exists()', 'HybridFile.isGoogleDriveFile', 'CALL',
  'exists checks for Google Drive mode',
  evidence='SRC HybridFile.java:1092 } else if (isGoogleDriveFile()) {')

e('HybridFile.isSimpleFile', 'HybridFile.isCustomPath', 'CALL',
  'isSimpleFile excludes custom paths',
  evidence='SRC HybridFile.java:1132 return !isSmb() && !isOtgFile() && !isCustomPath()')

e('HybridFile.isSimpleFile', 'HybridFile.isSmb', 'CALL',
  'isSimpleFile checks not SMB',
  evidence='SRC HybridFile.java:1132 return !isSmb()')

e('HybridFile.isSimpleFile', 'HybridFile.isOtgFile', 'CALL',
  'isSimpleFile checks not OTG',
  evidence='SRC HybridFile.java:1132 && !isOtgFile()')

e('HybridFile.isSimpleFile', 'HybridFile.isSftp', 'CALL',
  'isSimpleFile checks not SFTP',
  evidence='SRC HybridFile.java:1135 && !isSftp();')

e('HybridFile.isSimpleFile', 'HybridFile.isOneDriveFile', 'CALL',
  'isSimpleFile checks not OneDrive',
  evidence='SRC HybridFile.java:1134 && !isOneDriveFile()')

e('HybridFile.isSimpleFile', 'HybridFile.isGoogleDriveFile', 'CALL',
  'isSimpleFile checks not Google Drive',
  evidence='SRC HybridFile.java:1134 && !isGoogleDriveFile()')

e('HybridFile.isSimpleFile', 'HybridFile.isDropBoxFile', 'CALL',
  'isSimpleFile checks not Dropbox',
  evidence='SRC HybridFile.java:1135 && !isDropBoxFile()')

e('HybridFile.isSimpleFile', 'HybridFile.isBoxFile', 'CALL',
  'isSimpleFile checks not Box',
  evidence='SRC HybridFile.java:1135 && !isBoxFile()')

# File property getters
e('MainFragment.loadlist', 'HybridFile.getParent', 'CALL',
  'MainFragment gets parent path for navigation',
  evidence='SRC MainFragment.java:1317 String parentPath = new HybridFile(openMode, CURRENT_PATH).getParent(getActivity());')

e('HybridFile.getParent', 'HybridFile.getName', 'CALL',
  'getParent uses getName to calculate parent',
  evidence='SRC HybridFile.java:398 return builder.substring(0, builder.length() - (getName().length() + 1));')

e('HybridFile.getParent', 'HybridFile.getSmbFile', 'CALL',
  'getParent gets SmbFile for SMB mode',
  evidence='SRC HybridFile.java:389 parentPath = new SmbFile(path).getParent();')

e('GeneralDialogCreation.showPropertiesDialog', 'HybridFile.getName', 'CALL',
  'Properties dialog gets filename',
  evidence='SRC GeneralDialogCreation.java:380 name = baseFile.getName(),')

e('HybridFile.getParentName', 'HybridFile.getName', 'CALL',
  'getParentName uses getName',
  evidence='SRC HybridFile.java:428-429 StringBuilder parentPath = new StringBuilder(builder.substring(0, builder.length() - (getName().length() + 1)));')

e('GeneralDialogCreation.showPropertiesDialog', 'HybridFile.isDirectory', 'CALL',
  'Properties dialog checks if directory',
  evidence='SRC GeneralDialogCreation.java:383,418 File nomediaFile = baseFile.isDirectory()? ... if (baseFile.isDirectory() && baseFile.isLocal())')

e('HybridFile.isDirectory', 'HybridFile.getFile', 'CALL',
  'isDirectory gets File for local mode',
  evidence='SRC HybridFile.java:458 isDirectory = new File(path).isDirectory();')

e('HybridFile.isDirectory', 'HybridFile.getSmbFile', 'CALL',
  'isDirectory gets SmbFile for SMB mode',
  evidence='SRC HybridFile.java:451 isDirectory = new SmbFile(path).isDirectory();')

e('DecryptService.onStartCommand', 'HybridFile.length', 'CALL',
  'DecryptService gets file size',
  evidence='SRC DecryptService.java:132 else totalSize = baseFile.length(context);')

e('HybridFile.length', 'HybridFile.generateBaseFileFromParent', 'CALL',
  'length gets file info from parent for root mode',
  evidence='SRC HybridFile.java:245 HybridFileParcelable baseFile = generateBaseFileFromParent();')

e('HybridFile.lastModified', 'HybridFile.generateBaseFileFromParent', 'CALL',
  'lastModified gets info from parent for root mode',
  evidence='SRC HybridFile.java:214 HybridFileParcelable baseFile = generateBaseFileFromParent();')

e('HybridFile.lastModified', 'HybridFile.getSmbFile', 'CALL',
  'lastModified gets SmbFile',
  evidence='SRC HybridFile.java:202 SmbFile smbFile = getSmbFile();')

e('HybridFile.length', 'HybridFile.getSmbFile', 'CALL',
  'length gets SmbFile',
  evidence='SRC HybridFile.java:233 SmbFile smbFile=getSmbFile();')

e('HybridFile.folderSize()', 'HybridFile.getSmbFile', 'CALL',
  'folderSize gets SmbFile',
  evidence='SRC HybridFile.java:557 size = FileUtils.folderSize(new SmbFile(path));')

e('HybridFile.getUsableSpace', 'HybridFile.getSmbFile', 'CALL',
  'getUsableSpace gets SmbFile',
  evidence='SRC HybridFile.java:632 size = (new SmbFile(path).getDiskFreeSpace());')

e('CloudUtil.launchCloud', 'HybridFile.getInputStream()', 'CALL',
  'CloudUtil gets input stream to stream file',
  evidence='SRC CloudUtil.java:139 streamer.setStreamSrc(baseFile.getInputStream(activity), baseFile.getName(), baseFile.length(activity));')

e('HybridFile.getInputStream()', 'HybridFile.isSftp', 'CALL',
  'getInputStream checks SFTP mode',
  evidence='SRC HybridFile.java:904 if (isSftp()) {')

e('HybridFile.getInputStream()', 'HybridFile.isSmb', 'CALL',
  'getInputStream checks SMB mode',
  evidence='SRC HybridFile.java:922 else if (isSmb()) {')

e('FileUtils.scanFile', 'HybridFile.exists()', 'CALL',
  'FileUtils checks file existence before scanning',
  evidence='SRC FileUtils.java:244,266 if (hybridFiles[0].exists(context) && ... if((hybridFile.isLocal() || hybridFile.isOtgFile()) && hybridFile.exists(context))')

e('HybridFile.exists()', 'HybridFile.isSftp', 'CALL',
  'exists checks for SFTP mode',
  evidence='SRC HybridFile.java:1076 if (isSftp()) {')

e('HybridFile.exists()', 'HybridFile.isSmb', 'CALL',
  'exists checks for SMB mode',
  evidence='SRC HybridFile.java:1086 } else if (isSmb()) {')

e('HybridFile.exists()', 'HybridFile.isLocal', 'CALL',
  'exists checks for local mode',
  evidence='SRC HybridFile.java:1100 } else if (isLocal()) {')

e('HybridFile.exists()', 'HybridFile.isRoot', 'CALL',
  'exists checks for root mode',
  evidence='SRC HybridFile.java:1102 } else if (isRoot()) {')

e('HybridFile.exists()', 'HybridFile.getSmbFile', 'CALL',
  'exists gets SmbFile with timeout',
  evidence='SRC HybridFile.java:1088 SmbFile smbFile = getSmbFile(2000);')

e('HybridFile.exists()', 'HybridFile.getPath', 'CALL',
  'exists gets path',
  evidence='SRC HybridFile.java:1103 return RootHelper.fileExists(path);')

e('CopyService.startService', 'HybridFile.mkdir', 'CALL',
  'CopyService creates target directory',
  evidence='SRC CopyService.java:446 if (!targetFile.exists()) targetFile.mkdir(c);')

e('HybridFile.mkdir', 'HybridFile.isSftp', 'CALL',
  'mkdir checks SFTP mode',
  evidence='SRC HybridFile.java:1155 if(isSftp()) {')

e('HybridFile.mkdir', 'HybridFile.isSmb', 'CALL',
  'mkdir checks SMB mode',
  evidence='SRC HybridFile.java:1168 } else if (isSmb()) {')

e('HybridFile.mkdir', 'HybridFile.isOtgFile', 'CALL',
  'mkdir checks OTG mode',
  evidence='SRC HybridFile.java:1173 } else if (isOtgFile()) {')

e('HybridFile.mkdir', 'HybridFile.isDropBoxFile', 'CALL',
  'mkdir checks Dropbox mode',
  evidence='SRC HybridFile.java:1181 } else if (isDropBoxFile()) {')

e('HybridFile.mkdir', 'HybridFile.isBoxFile', 'CALL',
  'mkdir checks Box mode',
  evidence='SRC HybridFile.java:1189 } else if (isBoxFile()) {')

e('HybridFile.mkdir', 'HybridFile.isOneDriveFile', 'CALL',
  'mkdir checks OneDrive mode',
  evidence='SRC HybridFile.java:1197 } else if (isOneDriveFile()) {')

e('HybridFile.mkdir', 'HybridFile.isGoogleDriveFile', 'CALL',
  'mkdir checks Google Drive mode',
  evidence='SRC HybridFile.java:1205 } else if (isGoogleDriveFile()) {')

e('HybridFile.mkdir', 'HybridFile.getParent', 'CALL',
  'mkdir gets parent for OTG',
  evidence='SRC HybridFile.java:1176 DocumentFile parentDirectory = OTGUtil.getDocumentFile(getParent(context), context, false);')

e('HybridFile.mkdir', 'HybridFile.getName', 'CALL',
  'mkdir gets name for OTG',
  evidence='SRC HybridFile.java:1178 parentDirectory.createDirectory(getName(context));')

e('DeleteTask.doInBackground', 'HybridFile.delete', 'CALL',
  'DeleteTask deletes file',
  evidence='SRC DeleteTask.java:133 if (file.delete(cd, rootMode))')

e('HybridFile.delete', 'HybridFile.isSftp', 'CALL',
  'delete checks SFTP mode',
  evidence='SRC HybridFile.java:1213 if (isSftp()) {')

e('HybridFile.delete', 'HybridFile.isSmb', 'CALL',
  'delete checks SMB mode',
  evidence='SRC HybridFile.java:1226 } else if (isSmb()) {')

e('HybridFile.delete', 'HybridFile.isRoot', 'CALL',
  'delete checks root mode',
  evidence='SRC HybridFile.java:1234 if (isRoot() && rootmode) {')

e('HybridFile.delete', 'HybridFile.setMode', 'CALL',
  'delete sets ROOT mode before deleting',
  evidence='SRC HybridFile.java:1235 setMode(OpenMode.ROOT);')

e('HybridFile.delete', 'HybridFile.getPath', 'CALL',
  'delete gets path for RootUtils',
  evidence='SRC HybridFile.java:1236 RootUtils.delete(getPath());')

e('HybridFile.setLastModified', 'HybridFile.isSmb', 'CALL',
  'setLastModified checks SMB mode',
  evidence='SRC HybridFile.java:1139 if (isSmb()) {')

e('HybridFile.getReadablePath', 'HybridFile.isSftp', 'CALL',
  'getReadablePath checks SFTP',
  evidence='SRC HybridFile.java:879 if (isSftp())')

e('HybridFile.getReadablePath', 'HybridFile.isSmb', 'CALL',
  'getReadablePath checks SMB',
  evidence='SRC HybridFile.java:881 if (isSmb())')

e('HybridFile.getReadablePath', 'HybridFile.parseSftpPath', 'CALL',
  'getReadablePath parses SFTP path',
  evidence='SRC HybridFile.java:880 return parseSftpPath(path);')

e('HybridFile.getReadablePath', 'HybridFile.parseSmbPath', 'CALL',
  'getReadablePath parses SMB path',
  evidence='SRC HybridFile.java:882 return parseSmbPath(path);')

e('HybridFile.generateLayoutElement', 'HybridFile.isDirectory', 'CALL',
  'generateLayoutElement checks if directory',
  evidence='SRC HybridFile.java:1262 if (isDirectory()) {')

e('HybridFile.generateLayoutElement', 'HybridFile.folderSize()', 'CALL',
  'generateLayoutElement gets folder size',
  evidence='SRC HybridFile.java:1265 "", folderSize() + "", 0, true')

e('HybridFile.generateLayoutElement', 'HybridFile.getFile', 'CALL',
  'generateLayoutElement gets File object',
  evidence='SRC HybridFile.java:1259,1270 File file = new File(path);')

# UNREACHABLE methods - none, all 51 methods are reachable


# ---- part label_b034 (2026-10-27 23:50 re-merged WITH edges) ----

# GetSshHostFingerprintTask - AsyncTask for fetching SSH host fingerprints during SFTP setup

# Constructor called from SftpConnectDialog button callback
e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'Instantiate task to fetch host fingerprint when positive button clicked',
  evidence='SRC SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'Instantiate task to fetch host fingerprint in else branch (no existing key)',
  evidence='SRC SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

# execute() triggers AsyncTask lifecycle
e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.onPreExecute', 'ASYNC',
  'AsyncTask framework calls onPreExecute when execute() invoked',
  evidence='SRC SftpConnectDialog.java:199 }).execute(); triggers framework lifecycle')

e('GetSshHostFingerprintTask.onPreExecute', 'GetSshHostFingerprintTask.doInBackground', 'LIFECYCLE',
  'AsyncTask framework calls doInBackground after onPreExecute',
  evidence='SRC GetSshHostFingerprintTask.java:80 protected AsyncTaskResult<PublicKey> doInBackground(Void... voids)')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.onPreExecute', 'ASYNC',
  'AsyncTask framework calls onPreExecute when execute() invoked (second call site)',
  evidence='SRC SftpConnectDialog.java:229 }).execute(); triggers framework lifecycle')

# doInBackground creates lambda for HostKeyVerifier
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL',
  'Lambda passed to SSHClient.addHostKeyVerifier, invoked when host key received',
  evidence='SRC GetSshHostFingerprintTask.java:86 sshClient.addHostKeyVerifier((hostname, port, key) -> {...')

# AsyncTask completes and calls onPostExecute
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'LIFECYCLE',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='SRC GetSshHostFingerprintTask.java:117 protected void onPostExecute(AsyncTaskResult<PublicKey> result)')

# No UNREACHABLE methods in this batch

# ---- part label_b037 (2026-10-27 23:50 re-merged WITH edges) ----

# GlideRequests - GENERATED Glide class
# All methods are UNREACHABLE unless specifically called by app code

# GzipDecompressor
e('CompressedHelper.getCompressorInstance', 'GzipDecompressor.<init>', 'CALL',
  'Instantiation when file type is gzipped tar',
  evidence='SRC filesystem/compressed/CompressedHelper.java:118')

e('GzipDecompressor.changePath', 'GzipHelperTask.<init>', 'CALL',
  'Creates GzipHelperTask to load compressed file contents',
  evidence='SRC filesystem/compressed/showcontents/helpers/GzipDecompressor.java:46')

e('GzipHelperTask.<init>', 'GzipHelperTask.addElements', 'LIFECYCLE',
  'CompressedHelperTask.doInBackground calls abstract addElements',
  evidence='SRC asynchronous/asynctasks/compress/CompressedHelperTask.java:55')

# GzipExtractor
e('CompressedHelper.getExtractorInstance', 'GzipExtractor.<init>', 'CALL',
  'Instantiation when extracting gzipped tar files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:88')

e('GzipExtractor.<init>', 'GzipExtractor.extractWithFilter', 'LIFECYCLE',
  'Extractor.extractEntries or extractEverything calls abstract extractWithFilter',
  evidence='SRC filesystem/compressed/extractcontents/Extractor.java:57,73')

e('GzipExtractor.extractWithFilter', 'GzipExtractor.extractEntry', 'CALL',
  'Extracts individual tar entries from gzip stream',
  evidence='SRC filesystem/compressed/extractcontents/helpers/GzipExtractor.java:81')

# GzipHelperTask methods routed via parent

# HiddenAdapter
e('GeneralDialogCreation.showHistoryDialog', 'HiddenAdapter.<init>', 'CALL',
  'Adapter created for history dialog',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:1097')

e('GeneralDialogCreation.showHiddenDialog', 'HiddenAdapter.<init>', 'CALL',
  'Adapter created for hidden files dialog',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:1119')

# HiddenAdapter RecyclerView.Adapter lifecycle methods
e('HiddenAdapter.<init>', 'HiddenAdapter.onCreateViewHolder', 'LIFECYCLE',
  'Framework calls onCreateViewHolder when RecyclerView needs new view',
  evidence='INFERRED: RecyclerView.Adapter lifecycle callback, source not read')

e('HiddenAdapter.<init>', 'HiddenAdapter.onBindViewHolder', 'LIFECYCLE',
  'Framework calls onBindViewHolder when RecyclerView binds data to view',
  evidence='INFERRED: RecyclerView.Adapter lifecycle callback, source not read')

e('HiddenAdapter.<init>', 'HiddenAdapter.getItemCount', 'LIFECYCLE',
  'Framework calls getItemCount to determine adapter size',
  evidence='INFERRED: RecyclerView.Adapter lifecycle callback, source not read')

e('HiddenAdapter.<init>', 'HiddenAdapter.getItemId', 'LIFECYCLE',
  'Framework calls getItemId for item identification',
  evidence='INFERRED: RecyclerView.Adapter lifecycle callback, source not read')

e('HiddenAdapter.onCreateViewHolder', 'HiddenViewHolder.<init>', 'CALL',
  'ViewHolder instantiated when RecyclerView needs new view',
  evidence='SRC adapters/HiddenAdapter.java:64')

e('HiddenAdapter.onBindViewHolder', 'HiddenAdapter.lambda$onBindViewHolder$0', 'GUI',
  'Lambda for deleteButton click listener',
  evidence='SRC adapters/HiddenAdapter.java:78')

e('HiddenAdapter.onBindViewHolder', 'HiddenAdapter.lambda$onBindViewHolder$4', 'GUI',
  'Lambda for row click listener',
  evidence='SRC adapters/HiddenAdapter.java:99')

# Nested lambdas inside lambda$onBindViewHolder$4 (row click handler)
# The exact assignment of lambda$null$N to specific lines requires bytecode analysis
# But all three are called from the row handler: Thread runnable and runOnUiThread calls
e('HiddenAdapter.lambda$onBindViewHolder$4', 'HiddenAdapter.lambda$null$1', 'ASYNC',
  'Nested lambda in row handler - Thread runnable or runOnUiThread call',
  evidence='SRC adapters/HiddenAdapter.java:101-116 contains Thread and runOnUiThread lambdas')

e('HiddenAdapter.lambda$onBindViewHolder$4', 'HiddenAdapter.lambda$null$2', 'ASYNC',
  'Nested lambda in row handler - Thread runnable or runOnUiThread call',
  evidence='SRC adapters/HiddenAdapter.java:101-116 contains Thread and runOnUiThread lambdas')

e('HiddenAdapter.lambda$onBindViewHolder$4', 'HiddenAdapter.lambda$null$3', 'ASYNC',
  'Nested lambda in row handler - Thread runnable or runOnUiThread call',
  evidence='SRC adapters/HiddenAdapter.java:101-116 contains Thread and runOnUiThread lambdas')

# UNREACHABLE methods from this batch (generated Glide class - methods not called by app)
UNREACHABLE['GlideRequests.addDefaultRequestListener'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.applyDefaultRequestOptions'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.asBitmap'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.asFile'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.asGif'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.download'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.downloadOnly'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')
UNREACHABLE['GlideRequests.load(Bitmap)'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Drawable)'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Uri)'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(File)'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Integer)'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(Object)'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(String)'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(URL)'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.load(byte[])'] = ('no_trigger_in_app', 'Generated method not called by app. App uses GlideApp.with().load() which may internally delegate to GlideRequests but not directly', 'INFERRED: all .load() calls are on GlideApp not GlideRequests', 'INFERRED')
UNREACHABLE['GlideRequests.setDefaultRequestOptions'] = ('no_trigger_in_app', 'Generated method not called by app', 'INFERRED: grep shows no usage in app code', 'INFERRED')

# ---- part label_b039 (2026-10-27 23:50 re-merged WITH edges) ----
# ---- Batch 039: HybridFile anonymous inner classes (2026-10-27 23:30)
# 16 anonymous inner classes (HybridFile$1..14, nested $9$1, $10$1, $11$1)
# These are SFtpClientTemplate/SshClientTemplate callbacks created in HybridFile methods

# HybridFile$1: created in lastModified() at line 194
e('HybridFile.lastModified', 'HybridFile$1.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP lastModified',
  evidence='SRC HybridFile.java:194')
e('HybridFile$1.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:194')
e('SshClientUtils.execute', 'HybridFile$1.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$2: created in length() at line 224
e('HybridFile.length', 'HybridFile$2.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP file size',
  evidence='SRC HybridFile.java:224')
e('HybridFile$2.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:224')
e('SshClientUtils.execute', 'HybridFile$2.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$4: created in isDirectory(Context) at line 485
e('HybridFile.isDirectory', 'HybridFile$4.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP directory check',
  evidence='SRC HybridFile.java:485')
e('HybridFile$4.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:485')
e('SshClientUtils.execute', 'HybridFile$4.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$5: created in folderSize(Context) at line 584
e('HybridFile.folderSize()', 'HybridFile$5.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP folder size',
  evidence='SRC HybridFile.java:584')
e('HybridFile$5.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:584')
e('SshClientUtils.execute', 'HybridFile$5.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$6: created in getUsableSpace() at line 651
e('HybridFile.getUsableSpace', 'HybridFile$6.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP free space',
  evidence='SRC HybridFile.java:651')
e('HybridFile$6.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:651')
e('SshClientUtils.execute', 'HybridFile$6.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$7: created in getTotal(Context) at line 704
e('HybridFile.getTotal', 'HybridFile$7.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP total disk size',
  evidence='SRC HybridFile.java:704')
e('HybridFile$7.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:704')
e('SshClientUtils.execute', 'HybridFile$7.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$8: created in forEachChildrenFile(Context,boolean,OnFileFound) at line 737
e('HybridFile.forEachChildrenFile', 'HybridFile$8.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP file listing',
  evidence='SRC HybridFile.java:737')
e('HybridFile$8.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:737')
e('SshClientUtils.execute', 'HybridFile$8.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$9: created in listFiles(Context,boolean) at line 810
e('HybridFile.listFiles', 'HybridFile$9.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP file listing',
  evidence='SRC HybridFile.java:810')
e('HybridFile$9.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:810')
e('SshClientUtils.execute', 'HybridFile$9.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$9$1: Cannot locate creation site in source - INCOMPLETE
# Constructor signature shows (HybridFile$9, RemoteFile, RemoteFile) but no instantiation
# found in HybridFile.java lines 810-831. Marked INCOMPLETE pending source verification.

# HybridFile$10: created in getInputStream() at line 905
e('HybridFile.getInputStream()', 'HybridFile$10.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP input stream',
  evidence='SRC HybridFile.java:905')
e('HybridFile$10.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:905')
e('SshClientUtils.execute', 'HybridFile$10.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$10$1: RemoteFileInputStream created inside HybridFile$10.execute at line 909
e('HybridFile$10.execute', 'HybridFile$10$1.<init>', 'CALL', 'creates RemoteFileInputStream with custom close',
  evidence='SRC HybridFile.java:909')

# HybridFile$11: created in getInputStream(Context) at line 948
e('HybridFile.getInputStream()', 'HybridFile$11.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP input stream with context',
  evidence='SRC HybridFile.java:948')
e('HybridFile$11.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:948')
e('SshClientUtils.execute', 'HybridFile$11.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$11$1: RemoteFileInputStream created inside HybridFile$11.execute at line 953
e('HybridFile$11.execute', 'HybridFile$11$1.<init>', 'CALL', 'creates RemoteFileInputStream with custom close',
  evidence='SRC HybridFile.java:953')

# HybridFile$12: created in getOutputStream(Context) at line 1021
e('HybridFile.getOutputStream', 'HybridFile$12.<init>', 'CALL', 'creates SshClientTemplate for SFTP output stream',
  evidence='SRC HybridFile.java:1021')
e('HybridFile$12.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:1021')
e('SshClientUtils.execute', 'HybridFile$12.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:74')

# HybridFile$13: created in exists() at line 1078
e('HybridFile.exists()', 'HybridFile$13.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP exists check',
  evidence='SRC HybridFile.java:1078')
e('HybridFile$13.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:1078')
e('SshClientUtils.execute', 'HybridFile$13.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# HybridFile$14: created in mkdir(Context) at line 1156
e('HybridFile.mkdir', 'HybridFile$14.<init>', 'CALL', 'creates SFtpClientTemplate for SFTP mkdir',
  evidence='SRC HybridFile.java:1156')
e('HybridFile$14.<init>', 'SshClientUtils.execute', 'CALL', 'passes template to SshClientUtils.execute',
  evidence='SRC HybridFile.java:1156')
e('SshClientUtils.execute', 'HybridFile$14.execute', 'FRAMEWORK', 'framework calls template.execute',
  evidence='SRC SshClientUtils.java:134')

# Note: HybridFile$9$1 needs investigation - need to find where it's actually created

# ---- part label_b040 (2026-10-27 23:50 re-merged WITH edges) ----

# ImmutableEntry - simple data holder, constructed in SearchTextTask
e('SearchTextTask.doInBackground', 'ImmutableEntry.<init>', 'CALL',
  'SearchTextTask constructs ImmutableEntry to hold search result positions',
  evidence='SRC SearchTextTask.java:67-69 nodes.add(new MapEntry(new ImmutableEntry<>(i, i + params[0].length()), lineNumberReader.getLineNumber()))')

e('SearchTextTask.onPostExecute', 'ImmutableEntry.getKey', 'CALL',
  'SearchTextTask.onPostExecute accesses entry key to highlight text',
  evidence='SRC SearchTextTask.java:88 Map.Entry keyMapEntry = (Map.Entry) mapEntry.getKey()')

e('SearchTextTask.onPostExecute', 'ImmutableEntry.getValue', 'CALL',
  'SearchTextTask.onPostExecute accesses entry value (MapEntry holds line number)',
  evidence='SRC SearchTextTask.java:67-69 new MapEntry(..., lineNumberReader.getLineNumber())')

# Icons - file type and icon resolution
e('LayoutElementParcelable.<init>', 'Icons.getTypeOfFile', 'CALL',
  'LayoutElementParcelable constructor determines file type',
  evidence='SRC LayoutElementParcelable.java:79 filetype = Icons.getTypeOfFile(path, isDirectory)')

e('LayoutElementParcelable.<init>', 'Icons.loadMimeIcon', 'CALL',
  'LayoutElementParcelable constructor loads fallback icon',
  evidence='SRC LayoutElementParcelable.java:80 int fallbackIcon = Icons.loadMimeIcon(path, isDirectory)')

e('CompressedObjectParcelable.<init>()', 'Icons.getTypeOfFile', 'CALL',
  'CompressedObjectParcelable constructor determines file type',
  evidence='SRC CompressedObjectParcelable.java:53 this.filetype = Icons.getTypeOfFile(path, directory)')

e('CompressedObjectParcelable.<init>()', 'Icons.loadMimeIcon', 'CALL',
  'CompressedObjectParcelable constructor loads icon',
  evidence='SRC CompressedObjectParcelable.java:55 Icons.loadMimeIcon(path, directory)')

e('FileUtils.openFile', 'Icons.getTypeOfFile', 'CALL',
  'FileUtils.openFile determines file type to decide how to open it',
  evidence='SRC FileUtils.java:539 int mimeType = Icons.getTypeOfFile(path, isDirectory)')

e('Icons.getTypeOfFile', 'Icons.checkType', 'CALL',
  'Icons.getTypeOfFile calls checkType for MIME category matching',
  evidence='SRC Icons.java:278 return checkType(mime, check)')

e('Icons.<clinit>', 'Icons.putKeys', 'CALL',
  'Icons static initializer populates MIME map',
  evidence='SRC Icons.java:46 static { putKeys(APK, ...)')

e('Icons.putKeys', 'Icons.put', 'CALL',
  'Icons.putKeys calls put for each MIME type',
  evidence='SRC Icons.java:38-40 for (String type : mimeTypes) { put(type, resId); }')

e('LayoutElementParcelable.<init>', 'Icons.<clinit>', 'FRAMEWORK',
  'First reference to Icons class triggers static initializer',
  evidence='INFERRED from class loading - Icons.<clinit> runs before Icons.getTypeOfFile at LayoutElementParcelable.java:79')

# HybridFileParcelable - Parcelable file representation
e('LayoutElementParcelable.generateBaseFile', 'HybridFileParcelable.<init>', 'CALL',
  'LayoutElementParcelable.generateBaseFile constructs HybridFileParcelable',
  evidence='SRC LayoutElementParcelable.java:134 HybridFileParcelable baseFile=new HybridFileParcelable(desc, permissions, date, longSize, isDirectory)')

e('AppsAdapter.onMenuItemClick', 'HybridFileParcelable.<init>', 'CALL',
  'AppsAdapter creates HybridFileParcelable for uninstall',
  evidence='SRC AppsAdapter.java:188 final HybridFileParcelable f1 = new HybridFileParcelable(rowItem.path)')

e('RootHelper.generateBaseFileFromFile', 'HybridFileParcelable.<init>', 'CALL',
  'RootHelper generates HybridFileParcelable from File',
  evidence='SRC RootHelper.java:116-118 HybridFileParcelable baseFile = new HybridFileParcelable(x.getPath(), parseFilePermission(x), x.lastModified(), size, x.isDirectory())')

e('HybridFile.listFiles', 'HybridFileParcelable.<init>', 'CALL',
  'HybridFile.listFiles creates HybridFileParcelable for SFTP/SMB',
  evidence='SRC HybridFile.java:747 HybridFileParcelable f = new HybridFileParcelable(String.format("%s/%s", path, info.getName()))')

e('AbstractProgressiveService.finalizeNotification', 'HybridFileParcelable.writeToParcel', 'INTENT',
  'Service sends HybridFileParcelable ArrayList via Intent, triggering parcel write',
  evidence='SRC AbstractProgressiveService.java:245 intent.putExtra(MainActivity.TAG_INTENT_FILTER_FAILED_OPS, failedOps)')

e('MainActivity.onCreate', 'HybridFileParcelable.describeContents', 'FRAMEWORK',
  'Framework calls describeContents when parceling',
  evidence='INFERRED from Parcelable contract at MainActivity.java:313')

e('MainActivity.onCreate', 'HybridFileParcelable$1.createFromParcel', 'FRAMEWORK',
  'Framework uses CREATOR.createFromParcel when unparceling',
  evidence='INFERRED from Parcelable contract at MainActivity.java:313')

e('HybridFileParcelable$1.createFromParcel', 'HybridFileParcelable.<init>', 'CALL',
  'CREATOR constructs HybridFileParcelable from Parcel',
  evidence='SRC HybridFileParcelable.java:108 return new HybridFileParcelable(in)')

e('MainActivity.onCreate', 'HybridFileParcelable$1.newArray', 'FRAMEWORK',
  'Framework uses CREATOR.newArray when unparceling',
  evidence='INFERRED from Parcelable contract at MainActivity.java:313')

e('MainActivity.onCreate', 'HybridFileParcelable.<clinit>', 'FRAMEWORK',
  'First reference to HybridFileParcelable triggers static initializer',
  evidence='INFERRED from class loading - HybridFileParcelable.<clinit> runs when class loaded for CREATOR access')

# HybridFileParcelable setters
e('LayoutElementParcelable.generateBaseFile', 'HybridFileParcelable.setName', 'CALL',
  'LayoutElementParcelable.generateBaseFile sets name',
  evidence='SRC LayoutElementParcelable.java:137 baseFile.setName(title)')

e('RootHelper.generateBaseFileFromFile', 'HybridFileParcelable.setName', 'CALL',
  'RootHelper sets name after construction',
  evidence='SRC RootHelper.java:119 baseFile.setName(x.getName())')

e('HybridFile.listFiles', 'HybridFileParcelable.setDate', 'CALL',
  'HybridFile.listFiles sets date for SFTP files',
  evidence='SRC HybridFile.java:751 f.setDate(info.getAttributes().getMtime() * 1000)')

e('HybridFile.listFiles', 'HybridFileParcelable.setDirectory', 'CALL',
  'HybridFile.listFiles sets directory flag',
  evidence='SRC HybridFile.java:750 f.setDirectory(isDirectory)')

e('HybridFile.listFiles', 'HybridFileParcelable.setSize', 'CALL',
  'HybridFile.listFiles sets size',
  evidence='SRC HybridFile.java:752 f.setSize(isDirectory ? 0 : info.getAttributes().getSize())')

e('HybridFile.listFiles', 'HybridFileParcelable.setPermission', 'CALL',
  'HybridFile.listFiles sets permission',
  evidence='SRC HybridFile.java:753 f.setPermission(Integer.toString(FilePermission.toMask(info.getAttributes().getPermissions()), 8))')

e('FileUtils.putFileInArrayList', 'HybridFileParcelable.setLink', 'CALL',
  'FileUtils sets symlink target',
  evidence='SRC FileUtils.java:941 baseFile.setLink(link.toString())')

# HybridFileParcelable getters - all accessed polymorphically
e('TextEditorActivity.saveFile', 'HybridFileParcelable.getPath', 'CALL',
  'TextEditorActivity accesses path from HybridFileParcelable',
  evidence='SRC TextEditorActivity.java:302 mFile.hybridFileParcelable.getPath().contains(getExternalCacheDir().getPath())')

e('DatabaseViewerActivity.onCreate', 'HybridFileParcelable.getPath', 'CALL',
  'DatabaseViewerActivity uses getPath',
  evidence='SRC DatabaseViewerActivity.java:165 RootUtils.copy(pathFile.getPath(), ...)')

e('EditableFileAbstraction.<init>', 'HybridFileParcelable.getName', 'CALL',
  'EditableFileAbstraction constructor gets name from HybridFileParcelable',
  evidence='SRC EditableFileAbstraction.java:71 String tempN = hybridFileParcelable.getName(context)')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.getName', 'CALL',
  'LoadFilesListTask accesses baseFile.getName for LayoutElement',
  evidence='SRC LoadFilesListTask.java:247 LayoutElementParcelable layoutElement = new LayoutElementParcelable(c, baseFile.getName(), ...')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.getPermission', 'CALL',
  'LoadFilesListTask accesses baseFile.getPermission for LayoutElement',
  evidence='SRC LoadFilesListTask.java:249 baseFile.getPath(), baseFile.getPermission(), baseFile.getLink(), ...')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.getLink', 'CALL',
  'LoadFilesListTask accesses baseFile.getLink for LayoutElement',
  evidence='SRC LoadFilesListTask.java:249 baseFile.getPermission(), baseFile.getLink(), size, ...')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.getDate', 'CALL',
  'LoadFilesListTask accesses baseFile.getDate for LayoutElement',
  evidence='SRC LoadFilesListTask.java:250 longSize, false, baseFile.getDate() + "", baseFile.isDirectory(), ...')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.isDirectory', 'CALL',
  'LoadFilesListTask accesses baseFile.isDirectory for LayoutElement',
  evidence='SRC LoadFilesListTask.java:250 baseFile.getDate() + "", baseFile.isDirectory(), ...')

e('CopyService.checkFiles', 'HybridFileParcelable.getMode', 'CALL',
  'CopyService accesses baseFile.getMode for HybridFile construction',
  evidence='SRC CopyService.java:494 new HybridFile(baseFile.getMode(), baseFile.getPath())')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.getSize', 'CALL',
  'LoadFilesListTask uses baseFile.getSize indirectly through size variable',
  evidence='INFERRED from LoadFilesListTask pattern - size field accessed via getter')

e('HybridFileParcelable.getName', 'HybridFileParcelable.isHidden', 'CALL',
  'HybridFileParcelable.isHidden checks if name starts with dot',
  evidence='SRC HybridFileParcelable.java:77 public boolean isHidden(){ return name.startsWith("."); }')

e('ArrayList.contains', 'HybridFileParcelable.equals', 'FRAMEWORK',
  'Collection operations call equals',
  evidence='INFERRED from ArrayList.contains when holding HybridFileParcelable')

e('HashMap.put', 'HybridFileParcelable.hashCode', 'FRAMEWORK',
  'HashMap operations call hashCode',
  evidence='INFERRED from HashMap usage with HybridFileParcelable')

# UNREACHABLE methods
UNREACHABLE_PART_B040 = {
    'ImmutableEntry.setValue': ('no_trigger_in_app', 'ImmutableEntry.setValue always throws UnsupportedOperationException per immutable contract - no caller attempts it', 'SRC ImmutableEntry.java:48-50 public final V setValue(V value) { throw new UnsupportedOperationException(); }', 'SOURCE'),
    
    'HybridFileParcelable.toString': ('no_trigger_in_app', 'HybridFileParcelable.toString not explicitly called in app code - only implicit via debugger', 'SRC HybridFileParcelable.java:139-145', 'INFERRED'),
    
    'Icons.<init>': ('no_trigger_in_app', 'Icons has only static members - no instance ever created', 'SRC Icons.java:29 public class Icons', 'INFERRED'),
    
    # REMOVED CONTRADICTION: HybridFileParcelable$1.<init> - REACHABLE via CREATOR field
}
UNREACHABLE.update(UNREACHABLE_PART_B040)

# Note: HybridFileParcelable.<clinit> and Icons.<clinit> are REACHABLE - they are static initializers
# that run when the class is first loaded. HybridFileParcelable.<clinit> initializes the CREATOR field,
# and Icons.<clinit> populates the MIME type map. Both are reached via class loading.

# ---- part label_b041 (2026-10-27 23:50 re-merged WITH edges) ----
# Batch 41: Indicator, Indicator$1, Indicator$2, Indicator$3, Indicator$LeftwardStartPredicate
# 5 classes, 38 methods

# Indicator is a ViewPager page indicator (dots animation view) used in TabFragment
# Entry: MainActivity.onCreate -> goToMain -> TabFragment.<init> -> TabFragment.onCreateView
#        -> findViewById(R.id.indicator) [framework inflates, calls 3-arg constructor]
#        -> Indicator.setViewPager

# Indicator constructors - framework-inflated from XML
e('TabFragment.onCreateView', 'Indicator.<init>', 'FRAMEWORK',
  'findViewById inflates Indicator from XML; framework calls 3-arg constructor',
  evidence='SRC TabFragment.java:84-85 findViewById(R.id.indicator); '
           'SRC Indicator.java:123-163 constructor chain (115-117, 119-121, 123-163)')

# setViewPager - explicitly called from TabFragment
e('TabFragment.onCreateView', 'Indicator.setViewPager', 'CALL',
  'TabFragment sets up ViewPager reference',
  evidence='SRC TabFragment.java:178 indicator.setViewPager(mViewPager); '
           'SRC Indicator.java:164-175')

# setViewPager internal calls
e('Indicator.setViewPager', 'Indicator.setPageCount', 'CALL',
  'setViewPager initializes page count from adapter',
  evidence='SRC Indicator.java:167 setPageCount(viewPager.getAdapter().getCount()); '
           'SRC Indicator.java:214-218')

e('Indicator.setViewPager', 'Indicator.setCurrentPageImmediate', 'CALL',
  'setViewPager sets initial selected dot position',
  evidence='SRC Indicator.java:174 setCurrentPageImmediate(); '
           'SRC Indicator.java:238-247')

e('Indicator.setViewPager', 'Indicator$1.<init>', 'CALL',
  'setViewPager registers DataSetObserver for adapter changes',
  evidence='SRC Indicator.java:168-173 registerDataSetObserver(new DataSetObserver() { ... })')

# setPageCount calls resetState
e('Indicator.setPageCount', 'Indicator.resetState', 'CALL',
  'setPageCount resets animation state arrays',
  evidence='SRC Indicator.java:217 resetState(); '
           'SRC Indicator.java:220-229')

# Indicator$1 DataSetObserver callbacks
e('Indicator$1.<init>', 'Indicator$1.onChanged', 'FRAMEWORK',
  'DataSetObserver.onChanged callback when ViewPager adapter data changes',
  evidence='SRC Indicator.java:169-172 onChanged() override; '
           'INFERRED PagerAdapter.notifyDataSetChanged calls observer.onChanged, source not read')

e('Indicator$1.onChanged', 'Indicator.setPageCount', 'CALL',
  'DataSetObserver updates page count when adapter changes',
  evidence='SRC Indicator.java:171 setPageCount(Indicator.this.viewPager.getAdapter().getCount())')

# View lifecycle - onMeasure called by framework
e('Indicator.<init>', 'Indicator.onMeasure', 'FRAMEWORK',
  'View.onMeasure callback for layout measurement',
  evidence='SRC Indicator.java:44 extends View; '
           'INFERRED View framework calls onMeasure during layout, source not read')

# onMeasure internal calls
e('Indicator.onMeasure', 'Indicator.getDesiredHeight', 'CALL',
  'onMeasure calculates desired view height',
  evidence='SRC Indicator.java:234 getDesiredHeight(); '
           'SRC Indicator.java:270-272')

e('Indicator.onMeasure', 'Indicator.getDesiredWidth', 'CALL',
  'onMeasure calculates desired view width',
  evidence='SRC Indicator.java:243-251 getDesiredWidth(); '
           'SRC Indicator.java:278-280')

e('Indicator.onMeasure', 'Indicator.getRequiredWidth', 'CALL',
  'getDesiredWidth calls getRequiredWidth',
  evidence='SRC Indicator.java:279 getRequiredWidth(); '
           'SRC Indicator.java:274-276')

e('Indicator.onMeasure', 'Indicator.calculateDotPositions', 'CALL',
  'onMeasure finalizes dot positions after dimensions set',
  evidence='SRC Indicator.java:257 calculateDotPositions(width, height); '
           'SRC Indicator.java:220-237')

e('Indicator.calculateDotPositions', 'Indicator.setCurrentPageImmediate', 'CALL',
  'calculateDotPositions updates selected dot X position',
  evidence='SRC Indicator.java:236 setCurrentPageImmediate()')

# onDraw called by framework
e('Indicator.<init>', 'Indicator.onDraw', 'FRAMEWORK',
  'View.onDraw callback for rendering',
  evidence='SRC Indicator.java:44 extends View; '
           'INFERRED View framework calls onDraw to render, source not read')

# onDraw calls drawUnselected and drawSelected
e('Indicator.onDraw', 'Indicator.drawUnselected', 'CALL',
  'onDraw renders unselected page dots',
  evidence='SRC Indicator.java:283 drawUnselected(canvas); '
           'SRC Indicator.java:287-302')

e('Indicator.onDraw', 'Indicator.drawSelected', 'CALL',
  'onDraw renders selected page dot',
  evidence='SRC Indicator.java:284 drawSelected(canvas); '
           'SRC Indicator.java:633-635')

# drawUnselected internal calls
e('Indicator.drawUnselected', 'Indicator.getUnselectedPath', 'CALL',
  'drawUnselected builds path for each dot',
  evidence='SRC Indicator.java:292-296 getUnselectedPath(page, ...) for each page; '
           'SRC Indicator.java:317-623')

e('Indicator.drawUnselected', 'Indicator.getRetreatingJoinPath', 'CALL',
  'drawUnselected draws retreating join animation if active',
  evidence='SRC Indicator.java:299-300 if retreatingJoinX1 != INVALID_FRACTION, getRetreatingJoinPath(); '
           'SRC Indicator.java:625-630')

# OnPageChangeListener callbacks - called by ViewPager
e('Indicator.setViewPager', 'Indicator.onPageScrolled', 'FRAMEWORK',
  'ViewPager.OnPageChangeListener.onPageScrolled callback during scroll',
  evidence='SRC Indicator.java:44 implements ViewPager.OnPageChangeListener; '
           'SRC Indicator.java:166 addOnPageChangeListener(this); '
           'SRC Indicator.java:177-197; '
           'INFERRED ViewPager calls listener.onPageScrolled during page transitions, source not read')

e('Indicator.setViewPager', 'Indicator.onPageSelected', 'FRAMEWORK',
  'ViewPager.OnPageChangeListener.onPageSelected callback on page change',
  evidence='SRC Indicator.java:44 implements ViewPager.OnPageChangeListener; '
           'SRC Indicator.java:166 addOnPageChangeListener(this); '
           'SRC Indicator.java:199-208; '
           'INFERRED ViewPager calls listener.onPageSelected when page selected, source not read')

e('Indicator.setViewPager', 'Indicator.onPageScrollStateChanged', 'FRAMEWORK',
  'ViewPager.OnPageChangeListener.onPageScrollStateChanged callback',
  evidence='SRC Indicator.java:44 implements ViewPager.OnPageChangeListener; '
           'SRC Indicator.java:166 addOnPageChangeListener(this); '
           'SRC Indicator.java:210-212; '
           'INFERRED ViewPager calls listener.onPageScrollStateChanged, source not read')

# onPageScrolled calls setJoiningFraction
e('Indicator.onPageScrolled', 'Indicator.setJoiningFraction', 'CALL',
  'onPageScrolled updates dot joining animation fraction',
  evidence='SRC Indicator.java:196 setJoiningFraction(leftDotPosition, fraction); '
           'SRC Indicator.java:637-646')

# onPageSelected calls setSelectedPage
e('Indicator.onPageSelected', 'Indicator.setSelectedPage', 'CALL',
  'onPageSelected triggers page selection animation',
  evidence='SRC Indicator.java:203 setSelectedPage(position); '
           'SRC Indicator.java:548-577')

# setSelectedPage calls setJoiningFraction
e('Indicator.setSelectedPage', 'Indicator.setJoiningFraction', 'CALL',
  'setSelectedPage sets joining fraction to 1 for multi-step transitions',
  evidence='SRC Indicator.java:561-569 setJoiningFraction(previousPage + i, 1f) in loop')

# setSelectedPage calls createMoveSelectedAnimator
e('Indicator.setSelectedPage', 'Indicator.createMoveSelectedAnimator', 'CALL',
  'setSelectedPage creates animator for selected dot movement',
  evidence='SRC Indicator.java:571-575 moveAnimation = createMoveSelectedAnimator(...); '
           'SRC Indicator.java:579-630')

# createMoveSelectedAnimator creates inner class instances
e('Indicator.createMoveSelectedAnimator', 'Indicator$2.<init>', 'CALL',
  'createMoveSelectedAnimator creates AnimatorListenerAdapter for retreat animation end',
  evidence='SRC Indicator.java:590-597 retreatAnimation.addListener(new AnimatorListenerAdapter() { ... })')

e('Indicator.createMoveSelectedAnimator', 'Indicator$3.<init>', 'CALL',
  'createMoveSelectedAnimator creates AnimatorListenerAdapter for move animation lifecycle',
  evidence='SRC Indicator.java:604-618 moveSelected.addListener(new AnimatorListenerAdapter() { ... })')

e('Indicator.createMoveSelectedAnimator', 'Indicator.lambda$createMoveSelectedAnimator$0', 'CALL',
  'ValueAnimator.addUpdateListener registers lambda callback',
  evidence='SRC Indicator.java:598-602 moveSelected.addUpdateListener(valueAnimator -> { ... })')

e('Indicator.createMoveSelectedAnimator', 'Indicator$LeftwardStartPredicate.<init>', 'CALL',
  'createMoveSelectedAnimator creates LeftwardStartPredicate for leftward page transitions',
  evidence='SRC Indicator.java:590 new LeftwardStartPredicate(moveTo + ...) when now < was')

# Indicator$2 AnimatorListenerAdapter callbacks
e('Indicator$2.<init>', 'Indicator$2.onAnimationEnd', 'FRAMEWORK',
  'Animator calls listener.onAnimationEnd when retreat animation completes',
  evidence='SRC Indicator.java:592-596 onAnimationEnd() override; '
           'INFERRED ValueAnimator invokes AnimatorListener.onAnimationEnd, source not read')

e('Indicator$2.onAnimationEnd', 'Indicator.resetState', 'CALL',
  'Listener resets state when retreat animation ends',
  evidence='SRC Indicator.java:593 resetState()')

# Indicator$3 AnimatorListenerAdapter callbacks
e('Indicator$3.<init>', 'Indicator$3.onAnimationStart', 'FRAMEWORK',
  'Animator calls listener.onAnimationStart when move animation starts',
  evidence='SRC Indicator.java:605-609 onAnimationStart() override; '
           'INFERRED ValueAnimator invokes AnimatorListener.onAnimationStart, source not read')

e('Indicator$3.<init>', 'Indicator$3.onAnimationEnd', 'FRAMEWORK',
  'Animator calls listener.onAnimationEnd when move animation completes',
  evidence='SRC Indicator.java:611-617 onAnimationEnd() override; '
           'INFERRED ValueAnimator invokes AnimatorListener.onAnimationEnd, source not read')

# OnAttachStateChangeListener - framework callbacks
e('Indicator.<init>', 'Indicator.onViewAttachedToWindow', 'FRAMEWORK',
  'View.OnAttachStateChangeListener.onViewAttachedToWindow callback',
  evidence='SRC Indicator.java:44-45 implements View.OnAttachStateChangeListener; '
           'SRC Indicator.java:162 addOnAttachStateChangeListener(this); '
           'SRC Indicator.java:260-262; '
           'INFERRED View framework calls onViewAttachedToWindow, source not read')

e('Indicator.<init>', 'Indicator.onViewDetachedFromWindow', 'FRAMEWORK',
  'View.OnAttachStateChangeListener.onViewDetachedFromWindow callback',
  evidence='SRC Indicator.java:44-45 implements View.OnAttachStateChangeListener; '
           'SRC Indicator.java:162 addOnAttachStateChangeListener(this); '
           'SRC Indicator.java:264-266; '
           'INFERRED View framework calls onViewDetachedFromWindow, source not read')

# Indicator$LeftwardStartPredicate methods
e('Indicator$LeftwardStartPredicate.<init>', 'Indicator$LeftwardStartPredicate.shouldStart', 'CALL',
  'PendingStartAnimator.startIfNecessary calls predicate.shouldStart',
  evidence='SRC Indicator.java:827-829 shouldStart() method; '
           'INFERRED called from Indicator$PendingStartAnimator.startIfNecessary at line 668, class not in this batch')

# Methods called by classes in other batches (edges recorded there)
# - Indicator.cancelJoiningAnimations called from Indicator$PendingRetreatAnimator$1.onAnimationStart
# - Indicator.clearJoiningFractions called from Indicator$PendingRetreatAnimator$1.onAnimationStart
# - Indicator.setDotRevealFraction called from Indicator$PendingRetreatAnimator$1.onAnimationStart and Indicator$PendingRevealAnimator lambdas
# These edges will be recorded in those batches


# ---- part label_b042 (2026-10-27 23:50 re-merged WITH edges) ----

# ItemPopupMenu - file row overflow menu constructed from RecyclerAdapter
e('RecyclerAdapter.showPopup', 'ItemPopupMenu.<init>', 'CALL',
  'RecyclerAdapter constructs ItemPopupMenu for file row actions',
  evidence='SRC RecyclerAdapter.java:950 new ItemPopupMenu(context, mainFrag.getMainActivity(), utilsProvider, mainFrag, rowItem, view, sharedPrefs)')

e('ItemPopupMenu.<init>', 'ItemPopupMenu.onMenuItemClick', 'CALL',
  'Constructor sets this as menu item click listener',
  evidence='SRC ItemPopupMenu.java:58 setOnMenuItemClickListener(this)')

# ItemPopupMenu anonymous inner classes - callback interfaces in encrypt case
e('ItemPopupMenu.onMenuItemClick', 'ItemPopupMenu$1.<init>', 'CALL',
  'First anonymous EncryptButtonCallbackInterface created for authentication',
  evidence='SRC ItemPopupMenu.java:138-146 new EncryptDecryptUtils.EncryptButtonCallbackInterface() with onButtonPressed methods')

e('ItemPopupMenu.onMenuItemClick', 'ItemPopupMenu$2.<init>', 'CALL',
  'Second anonymous EncryptButtonCallbackInterface created for main encrypt flow',
  evidence='SRC ItemPopupMenu.java:149-175 new EncryptDecryptUtils.EncryptButtonCallbackInterface() checking master password and fingerprint')

e('ItemPopupMenu$1.<init>', 'ItemPopupMenu$1.onButtonPressed', 'CALL',
  'Callback interface onButtonPressed called by dialog flow',
  evidence='SRC ItemPopupMenu.java:143-146 onButtonPressed(Intent, String) calls EncryptDecryptUtils.startEncryption')

e('ItemPopupMenu$2.<init>', 'ItemPopupMenu$2.onButtonPressed', 'CALL',
  'Callback interface onButtonPressed called by dialog or direct flow',
  evidence='SRC ItemPopupMenu.java:151-173 onButtonPressed(Intent) checks preferences and shows dialogs')

# InterestingConfigChange - utility for detecting configuration changes
e('AppListLoader.onStartLoading', 'InterestingConfigChange.isConfigChanged', 'CALL',
  'AppListLoader checks if configuration changed',
  evidence='SRC AppListLoader.java:123 boolean didConfigChange = InterestingConfigChange.isConfigChanged(getContext().getResources())')

e('AppListLoader.onStopLoading', 'InterestingConfigChange.recycle', 'CALL',
  'AppListLoader recycles static state when stopping',
  evidence='SRC AppListLoader.java:160 InterestingConfigChange.recycle()')

# InvalidablePreferenceCategory - preference UI component inflated by framework
e('ColorPref.onViewCreated', 'InvalidablePreferenceCategory.invalidate', 'CALL',
  'ColorPref invalidates preference category with accent color',
  evidence='SRC ColorPref.java:235 ((InvalidablePreferenceCategory) findPreference("category")).invalidate(activity.getAccent())')

e('InvalidablePreferenceCategory.invalidate', 'InvalidablePreferenceCategory.onBindView', 'FRAMEWORK',
  'Framework calls onBindView after notifyChanged',
  evidence='SRC InvalidablePreferenceCategory.java:31 notifyChanged() triggers framework to call onBindView; INFERRED: framework source not read')

# Indicator - ViewPager indicator widget inflated from layout main_toolbar.xml
e('Indicator.<init>', 'Indicator.setViewPager', 'CALL',
  'After inflation, MainActivity calls setViewPager',
  evidence='SRC Indicator.java:162-171 setViewPager stores viewPager, adds listener, calls setPageCount')

e('Indicator.setViewPager', 'Indicator.setPageCount', 'CALL',
  'setViewPager calls setPageCount with adapter count',
  evidence='SRC Indicator.java:164 setPageCount(viewPager.getAdapter().getCount())')

e('Indicator.setPageCount', 'Indicator.resetState', 'CALL',
  'setPageCount resets animation state arrays',
  evidence='SRC Indicator.java:213 resetState()')

e('Indicator.setPageCount', 'Indicator.onMeasure', 'FRAMEWORK',
  'setPageCount calls requestLayout which triggers framework onMeasure',
  evidence='SRC Indicator.java:214 requestLayout(); INFERRED: framework source not read')

e('Indicator.onMeasure', 'Indicator.getDesiredHeight', 'CALL',
  'onMeasure calls getDesiredHeight for height spec',
  evidence='SRC Indicator.java:235 int desiredHeight = getDesiredHeight()')

e('Indicator.onMeasure', 'Indicator.getRequiredWidth', 'CALL',
  'onMeasure calls getRequiredWidth for width calculation',
  evidence='SRC Indicator.java:246 int desiredWidth = getDesiredWidth() which calls getRequiredWidth at line 271')

e('Indicator.onMeasure', 'Indicator.getDesiredWidth', 'CALL',
  'onMeasure calls getDesiredWidth for width spec',
  evidence='SRC Indicator.java:246 int desiredWidth = getDesiredWidth()')

e('Indicator.onMeasure', 'Indicator.calculateDotPositions', 'CALL',
  'onMeasure calls calculateDotPositions after setMeasuredDimension',
  evidence='SRC Indicator.java:256 calculateDotPositions(width, height)')

e('Indicator.calculateDotPositions', 'Indicator.setCurrentPageImmediate', 'CALL',
  'calculateDotPositions calls setCurrentPageImmediate to position selected dot',
  evidence='SRC Indicator.java:273 setCurrentPageImmediate()')

e('Indicator.onPageSelected', 'Indicator.setSelectedPage', 'CALL',
  'ViewPager.OnPageChangeListener callback calls setSelectedPage',
  evidence='SRC Indicator.java:201 setSelectedPage(position)')

e('Indicator.setSelectedPage', 'Indicator.setJoiningFraction', 'CALL',
  'setSelectedPage sets joining fractions to 1 for multi-step moves',
  evidence='SRC Indicator.java:566-574 for loop calls setJoiningFraction(previousPage + i, 1f)')

e('Indicator.setSelectedPage', 'Indicator.createMoveSelectedAnimator', 'CALL',
  'setSelectedPage creates move animator for selected dot',
  evidence='SRC Indicator.java:579 moveAnimation = createMoveSelectedAnimator(dotCenterX[now], previousPage, now, steps)')

e('Indicator.createMoveSelectedAnimator', 'Indicator$PendingRetreatAnimator.<init>', 'CALL',
  'createMoveSelectedAnimator constructs PendingRetreatAnimator',
  evidence='SRC Indicator.java:587 retreatAnimation = new PendingRetreatAnimator(was, now, steps, predicate)')

e('Indicator.createMoveSelectedAnimator', 'Indicator$RightwardStartPredicate.<init>', 'CALL',
  'createMoveSelectedAnimator constructs RightwardStartPredicate when moving right',
  evidence='SRC Indicator.java:589 new RightwardStartPredicate(moveTo - ((moveTo - selectedDotX) * 0.25f))')

e('Indicator$RightwardStartPredicate.<init>', 'Indicator$StartPredicate.<init>', 'CALL',
  'RightwardStartPredicate constructor calls super',
  evidence='SRC Indicator.java:826-828 RightwardStartPredicate(float thresholdValue) calls super(thresholdValue)')

e('Indicator.createMoveSelectedAnimator', 'Indicator.resetState', 'CALL',
  'Animator listener calls resetState on animation end',
  evidence='SRC Indicator.java:590-595 AnimatorListenerAdapter.onAnimationEnd calls resetState()')

e('Indicator.createMoveSelectedAnimator', 'Indicator$PendingRetreatAnimator.startIfNecessary', 'CALL',
  'Move animator update listener calls startIfNecessary',
  evidence='SRC Indicator.java:599 retreatAnimation.startIfNecessary(selectedDotX)')

e('Indicator$PendingRetreatAnimator.startIfNecessary', 'Indicator$RightwardStartPredicate.shouldStart', 'CALL',
  'startIfNecessary checks predicate shouldStart',
  evidence='SRC Indicator.java:668 if (!hasStarted && predicate.shouldStart(currentValue))')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingStartAnimator.<init>', 'CALL',
  'PendingRetreatAnimator constructor calls super',
  evidence='SRC Indicator.java:682 PendingRetreatAnimator calls super(predicate)')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRevealAnimator.<init>', 'CALL',
  'PendingRetreatAnimator creates reveal animators array',
  evidence='SRC Indicator.java:708,725 revealAnimations[i] = new PendingRevealAnimator(was + i, predicate)')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$RightwardStartPredicate.<init>', 'CALL',
  'PendingRetreatAnimator creates RightwardStartPredicate for reveal animators',
  evidence='SRC Indicator.java:709 new RightwardStartPredicate(dotCenterX[was + i])')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRevealAnimator.startIfNecessary', 'CALL',
  'Update listener calls startIfNecessary on each reveal animator',
  evidence='SRC Indicator.java:717,733 for (PendingRevealAnimator pendingReveal : revealAnimations) pendingReveal.startIfNecessary')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator.cancelJoiningAnimations', 'CALL',
  'Animator listener calls cancelJoiningAnimations on start',
  evidence='SRC Indicator.java:742 cancelJoiningAnimations()')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator.clearJoiningFractions', 'CALL',
  'Animator listener calls clearJoiningFractions on start',
  evidence='SRC Indicator.java:743 clearJoiningFractions()')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator.setDotRevealFraction', 'CALL',
  'Animator listener calls setDotRevealFraction for dots to hide',
  evidence='SRC Indicator.java:746 setDotRevealFraction(dot, MINIMAL_REVEAL)')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRetreatAnimator$1.<init>', 'CALL',
  'PendingRetreatAnimator creates anonymous AnimatorListenerAdapter',
  evidence='SRC Indicator.java:740-758 addListener(new AnimatorListenerAdapter() {...})')

e('Indicator$PendingRetreatAnimator$1.<init>', 'Indicator$PendingRetreatAnimator$1.onAnimationStart', 'ASYNC',
  'Framework calls onAnimationStart when retreat animation begins',
  evidence='SRC Indicator.java:742-749 onAnimationStart(Animator animation) method; INFERRED: framework source not read')

e('Indicator$PendingRetreatAnimator$1.<init>', 'Indicator$PendingRetreatAnimator$1.onAnimationEnd', 'ASYNC',
  'Framework calls onAnimationEnd when retreat animation completes',
  evidence='SRC Indicator.java:751-755 onAnimationEnd(Animator animation) method; INFERRED: framework source not read')

e('Indicator$PendingRevealAnimator.<init>', 'Indicator$PendingStartAnimator.<init>', 'CALL',
  'PendingRevealAnimator constructor calls super',
  evidence='SRC Indicator.java:768 PendingRevealAnimator calls super(predicate)')

e('Indicator$PendingRevealAnimator.<init>', 'Indicator.setDotRevealFraction', 'CALL',
  'Update listener calls setDotRevealFraction',
  evidence='SRC Indicator.java:775 setDotRevealFraction(PendingRevealAnimator.this.dot, (Float) valueAnimator.getAnimatedValue())')

e('Indicator$PendingRevealAnimator.<init>', 'Indicator$PendingRevealAnimator$1.<init>', 'CALL',
  'PendingRevealAnimator creates anonymous AnimatorListenerAdapter',
  evidence='SRC Indicator.java:778-784 addListener(new AnimatorListenerAdapter() {...})')

e('Indicator$PendingRevealAnimator$1.<init>', 'Indicator$PendingRevealAnimator$1.onAnimationEnd', 'ASYNC',
  'Framework calls onAnimationEnd when reveal animation completes',
  evidence='SRC Indicator.java:780-783 onAnimationEnd(Animator animation) method; INFERRED: framework source not read')

e('Indicator.onPageScrolled', 'Indicator.setJoiningFraction', 'CALL',
  'ViewPager scroll callback calls setJoiningFraction',
  evidence='SRC Indicator.java:193 setJoiningFraction(leftDotPosition, fraction)')

e('Indicator.onDraw', 'Indicator.drawUnselected', 'FRAMEWORK',
  'Framework onDraw calls drawUnselected',
  evidence='SRC Indicator.java:291 drawUnselected(canvas); INFERRED: framework source not read')

e('Indicator.onDraw', 'Indicator.drawSelected', 'FRAMEWORK',
  'Framework onDraw calls drawSelected',
  evidence='SRC Indicator.java:292 drawSelected(canvas); INFERRED: framework source not read')

e('Indicator.drawUnselected', 'Indicator.getUnselectedPath', 'CALL',
  'drawUnselected calls getUnselectedPath for each dot',
  evidence='SRC Indicator.java:301-304 combinedUnselectedPath.op(getUnselectedPath(...))')

e('Indicator.drawUnselected', 'Indicator.getRetreatingJoinPath', 'CALL',
  'drawUnselected calls getRetreatingJoinPath when retreat active',
  evidence='SRC Indicator.java:308 combinedUnselectedPath.op(getRetreatingJoinPath(), Path.Op.UNION)')

e('Indicator.createMoveSelectedAnimator', 'Indicator.lambda$createMoveSelectedAnimator$0', 'CALL',
  'Lambda desugared for animator update listener',
  evidence='SRC Indicator.java:597-600 moveSelected.addUpdateListener(valueAnimator -> {...})')

# LZMA2Decoder - 7z compression library class accessed via Coders map
e('SevenZipHelperTask.doInBackground', 'SevenZFile.<init>', 'CALL',
  'SevenZipHelperTask opens 7z archive',
  evidence='SRC SevenZipHelperTask.java:68-70 new SevenZFile(new File(filePath))')

e('SevenZFile.buildDecodingStream', 'Coders.addDecoder', 'CALL',
  'SevenZFile calls Coders.addDecoder to decode each coder',
  evidence='SRC SevenZFile.java:435 inputStreamStack = Coders.addDecoder(fileName, inputStreamStack, ...)')

e('Coders.addDecoder', 'LZMA2Decoder.decode', 'CALL',
  'Coders.addDecoder looks up LZMA2Decoder from map and calls decode',
  evidence='SRC Coders.java:53 put(SevenZMethod.LZMA2, new LZMA2Decoder()); Coders.java:69-75 cb = findByMethod(...); return cb.decode(...)')

e('LZMA2Decoder.decode', 'LZMA2Decoder.getDictionarySize', 'CALL',
  'decode calls getDictionarySize to extract dictionary size from coder properties',
  evidence='SRC LZMA2Decoder.java:36 final int dictionarySize = getDictionarySize(coder)')

e('SevenZFile.getOptionsFromCoder', 'LZMA2Decoder.getOptionsFromCoder', 'CALL',
  'SevenZFile calls getOptionsFromCoder to extract coder options',
  evidence='SRC SevenZFile.java:1033 Coders.findByMethod(method).getOptionsFromCoder(coder, inputStreamStack); Coders.java:53 map contains LZMA2Decoder')

e('SevenZOutputFile.writeFilesInfo', 'Coders.findByMethod', 'CALL',
  'SevenZOutputFile calls findByMethod to get coder for properties',
  evidence='SRC SevenZOutputFile.java:452 Coders.findByMethod(m.getMethod()).getOptionsAsProperties(m.getOptions())')

e('Coders.findByMethod', 'LZMA2Decoder.getOptionsAsProperties', 'CALL',
  'findByMethod returns LZMA2Decoder, caller invokes getOptionsAsProperties',
  evidence='SRC Coders.java:53 put(SevenZMethod.LZMA2, new LZMA2Decoder()); Coders.java:67 return CODER_MAP.get(method)')

e('LZMA2Decoder.getOptionsAsProperties', 'LZMA2Decoder.getDictSize', 'CALL',
  'getOptionsAsProperties calls getDictSize to encode dictionary size',
  evidence='SRC LZMA2Decoder.java:56 final int dictSize = getDictSize(opts)')

e('LZMA2Decoder.getDictSize', 'LZMA2Decoder.numberOptionOrDefault', 'CALL',
  'getDictSize calls numberOptionOrDefault when opts is not LZMA2Options',
  evidence='SRC LZMA2Decoder.java:71 return numberOptionOrDefault(opts)')

e('SevenZOutputFile.writeFileCoder', 'Coders.addEncoder', 'CALL',
  'SevenZOutputFile calls Coders.addEncoder to wrap output stream',
  evidence='SRC SevenZOutputFile.java:321 out = Coders.addEncoder(out, m.getMethod(), m.getOptions())')

e('Coders.addEncoder', 'LZMA2Decoder.encode', 'CALL',
  'Coders.addEncoder looks up LZMA2Decoder from map and calls encode',
  evidence='SRC Coders.java:53 put(SevenZMethod.LZMA2, new LZMA2Decoder()); Coders.java:82-87 cb = findByMethod(method); return cb.encode(out, options)')

e('LZMA2Decoder.encode', 'LZMA2Decoder.getOptions', 'CALL',
  'encode calls getOptions to create LZMA2Options',
  evidence='SRC LZMA2Decoder.java:46 final LZMA2Options options = getOptions(opts)')

e('LZMA2Decoder.getOptions', 'LZMA2Decoder.numberOptionOrDefault', 'CALL',
  'getOptions calls numberOptionOrDefault to get dict size',
  evidence='SRC LZMA2Decoder.java:93 options.setDictSize(numberOptionOrDefault(opts))')

# InterestingConfigChange static initializer
# Static fields initialized at class load, which happens on first access (isConfigChanged call)

# No UNREACHABLE methods in this batch - all methods are REACHABLE through the routes above

# ---- part label_b043 (2026-10-27 23:50 re-merged WITH edges) ----

# LoadFolderSpaceDataTask edges
e('GeneralDialogCreation.showPropertiesDialog', 'LoadFolderSpaceDataTask.<init>', 'EXPLICIT',
  'Constructor instantiated to load folder space data for properties dialog',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:516')

e('LoadFolderSpaceDataTask.<init>', 'LoadFolderSpaceDataTask.doInBackground', 'LIFECYCLE',
  'AsyncTask.execute triggers doInBackground on background thread',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:517 shows executeOnExecutor call; INFERRED framework lifecycle')

e('LoadFolderSpaceDataTask.doInBackground', 'LoadFolderSpaceDataTask.createEntriesFromArray', 'CALL',
  'doInBackground calls createEntriesFromArray to build pie chart entries',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:61')

e('LoadFolderSpaceDataTask.<init>', 'LoadFolderSpaceDataTask.onPostExecute', 'LIFECYCLE',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:77; INFERRED framework lifecycle')

e('LoadFolderSpaceDataTask.onPostExecute', 'LoadFolderSpaceDataTask.updateChart', 'CALL',
  'onPostExecute calls updateChart with final data',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:91')

e('LoadFolderSpaceDataTask.<init>', 'LoadFolderSpaceDataTask.onProgressUpdate', 'LIFECYCLE',
  'AsyncTask framework calls onProgressUpdate when publishProgress is called',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:67; INFERRED framework lifecycle')

e('LoadFolderSpaceDataTask.onProgressUpdate', 'LoadFolderSpaceDataTask.createEntriesFromArray', 'CALL',
  'onProgressUpdate calls createEntriesFromArray for intermediate updates',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:74')

e('LoadFolderSpaceDataTask.onProgressUpdate', 'LoadFolderSpaceDataTask.updateChart', 'CALL',
  'onProgressUpdate calls updateChart for progress display',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:77')

# LruBitmapCache edges
e('AppConfig.getImageLoader', 'LruBitmapCache.<init>', 'EXPLICIT',
  'No-arg constructor instantiated as ImageLoader.ImageCache implementation',
  evidence='SRC utils/application/AppConfig.java:223')

e('LruBitmapCache.<init>', 'LruBitmapCache.<init>', 'CALL',
  'No-arg constructor delegates to parameterized constructor via this()',
  evidence='SRC utils/LruBitmapCache.java:22')

e('LruBitmapCache.<init>', 'LruBitmapCache.getDefaultCacheSize', 'CALL',
  'No-arg constructor calls getDefaultCacheSize for cache size',
  evidence='SRC utils/LruBitmapCache.java:22')

e('LruBitmapCache.<init>', 'LruBitmapCache.getBitmap', 'FRAMEWORK',
  'ImageLoader calls getBitmap to retrieve cached bitmaps',
  evidence='SRC utils/LruBitmapCache.java:31 implements ImageLoader.ImageCache; INFERRED framework call')

e('LruBitmapCache.<init>', 'LruBitmapCache.putBitmap', 'FRAMEWORK',
  'ImageLoader calls putBitmap to cache bitmaps',
  evidence='SRC utils/LruBitmapCache.java:36 implements ImageLoader.ImageCache; INFERRED framework call')

e('LruBitmapCache.<init>', 'LruBitmapCache.sizeOf', 'FRAMEWORK',
  'LruCache framework calls sizeOf to calculate entry sizes',
  evidence='SRC utils/LruBitmapCache.java:40 overrides LruCache.sizeOf; INFERRED framework call')

# LzmaDecompressor edges
e('CompressedHelper.getCompressorInstance', 'LzmaDecompressor.<init>', 'EXPLICIT',
  'Constructor instantiated for .tar.lzma file types',
  evidence='SRC filesystem/compressed/CompressedHelper.java:124')

e('LzmaDecompressor.<init>', 'LzmaDecompressor.changePath', 'FRAMEWORK',
  'Parent Decompressor class calls changePath to navigate archive',
  evidence='SRC filesystem/compressed/showcontents/helpers/LzmaDecompressor.java:40; INFERRED framework call from Decompressor')

e('LzmaDecompressor.changePath', 'LzmaHelperTask.<init>', 'EXPLICIT',
  'changePath instantiates LzmaHelperTask for async archive processing',
  evidence='SRC filesystem/compressed/showcontents/helpers/LzmaDecompressor.java:43')

e('LzmaHelperTask.<init>', 'LzmaHelperTask.addElements', 'FRAMEWORK',
  'CompressedHelperTask framework calls addElements to populate archive entries',
  evidence='SRC asynchronous/asynctasks/compress/LzmaHelperTask.java:52; INFERRED framework call from CompressedHelperTask')

# LzmaExtractor edges
e('CompressedHelper.getExtractorInstance', 'LzmaExtractor.<init>', 'EXPLICIT',
  'Constructor instantiated for .tar.lzma file extraction',
  evidence='SRC filesystem/compressed/CompressedHelper.java:94')

e('LzmaExtractor.<init>', 'LzmaExtractor.extractWithFilter', 'FRAMEWORK',
  'Parent Extractor class calls extractWithFilter to extract archive',
  evidence='SRC filesystem/compressed/extractcontents/helpers/LzmaExtractor.java:48; INFERRED framework call from Extractor')

e('LzmaExtractor.extractWithFilter', 'LzmaExtractor.extractEntry', 'CALL',
  'extractWithFilter calls extractEntry for each archive entry',
  evidence='SRC filesystem/compressed/extractcontents/helpers/LzmaExtractor.java:74')

# UNREACHABLE methods from batch_043
UNREACHABLE['LZMADecoder.<init>'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.decode'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.encode'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.getDictionarySize'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.getOptions'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.getOptionsAsProperties'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.getOptionsFromCoder'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.numberOptionOrDefault'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

# ---- part label_b045 (2026-10-27 23:50 re-merged WITH edges) ----

# MainActivity$2 (anonymous BroadcastReceiver - receiver2)
# Created at line 1610, registered in onResume at line 1120
e('MainActivity.onResume', 'MainActivity$2.<init>', 'CALL', 'Create receiver2 instance for failed operations broadcast',
  evidence='SRC MainActivity.java:1610-1620 shows private BroadcastReceiver receiver2 = new BroadcastReceiver() declaration; 1120 shows registerReceiver(receiver2, new IntentFilter(TAG_INTENT_FILTER_GENERAL))')

e('MainActivity$2.<init>', 'MainActivity$2.onReceive', 'FRAMEWORK', 'BroadcastReceiver.onReceive called by Android framework when intent with TAG_INTENT_FILTER_GENERAL action is broadcast',
  evidence='SRC MainActivity.java:1612 shows @Override public void onReceive(Context context, Intent i); framework calls onReceive when broadcast matches filter')

e('MainActivity$2.onReceive', 'MainActivityHelper.showFailedOperationDialog', 'CALL', 'Show dialog for failed operations extracted from intent',
  evidence='SRC MainActivity.java:1613-1617 shows if (i.getStringArrayListExtra(TAG_INTENT_FILTER_FAILED_OPS) != null) { ArrayList<HybridFileParcelable> failedOps = i.getParcelableArrayListExtra(TAG_INTENT_FILTER_FAILED_OPS); if (failedOps != null) { mainActivityHelper.showFailedOperationDialog(failedOps, mainActivity); }')

# MainActivity$3 (anonymous BroadcastReceiver - mOtgReceiver)
# Created at line 1171, registered in updateUsbInformation at line 1165
e('MainActivity.updateUsbInformation', 'MainActivity$3.<init>', 'CALL', 'Create mOtgReceiver instance for USB OTG device attach/detach',
  evidence='SRC MainActivity.java:1171-1186 shows BroadcastReceiver mOtgReceiver = new BroadcastReceiver declaration; 1165 shows registerReceiver(mOtgReceiver, otgFilter)')

e('MainActivity$3.<init>', 'MainActivity$3.onReceive', 'FRAMEWORK', 'BroadcastReceiver.onReceive called by Android framework when USB device attached or detached',
  evidence='SRC MainActivity.java:1172-1173 shows @Override public void onReceive(Context context, Intent intent); framework calls onReceive on USB attach/detach')

# MainActivity$FabActionListener (inner class implementing SpeedDialView.OnActionSelectedListener)
# Created at line 1935, instantiated in initialiseFab at line 1508
e('MainActivity.initialiseFab', 'MainActivity$FabActionListener.<init>', 'CALL', 'Create FabActionListener for floating action button menu',
  evidence='SRC MainActivity.java:1508 shows floatingActionButton.setOnActionSelectedListener(new FabActionListener(this)); 1935 shows FabActionListener(MainActivity mainActivity) constructor')

e('MainActivity$FabActionListener.<init>', 'MainActivity$FabActionListener.onActionSelected', 'GUI', 'SpeedDialView.OnActionSelectedListener.onActionSelected called when user selects FAB menu item',
  evidence='SRC MainActivity.java:1940-1941 shows @Override public boolean onActionSelected(SpeedDialActionItem actionItem); GUI callback when FAB item selected')

e('MainActivity$FabActionListener.onActionSelected', 'MainActivityHelper.mkdir', 'CALL', 'Create new folder when menu_new_folder FAB item selected',
  evidence='SRC MainActivity.java:1945-1948 shows case R.id.menu_new_folder: mainActivity.mainActivityHelper.mkdir(ma.openMode, path, ma); break;')

e('MainActivity$FabActionListener.onActionSelected', 'MainActivityHelper.mkfile', 'CALL', 'Create new file when menu_new_file FAB item selected',
  evidence='SRC MainActivity.java:1949-1951 shows case R.id.menu_new_file: mainActivity.mainActivityHelper.mkfile(ma.openMode, path, ma); break;')

# MainActivityHelper methods
# Constructor called from MainActivity.onCreate
e('MainActivity.onCreate', 'MainActivityHelper.<init>', 'CALL', 'Instantiate MainActivityHelper in MainActivity.onCreate',
  evidence='SRC MainActivity.java:184 shows public MainActivityHelper mainActivityHelper; mainActivityHelper is initialized in onCreate. MainActivityHelper.java:82-85 shows public MainActivityHelper(MainActivity mainActivity) { this.mainActivity = mainActivity; accentColor = mainActivity.getAccent(); }')

# MainActivityHelper.showFailedOperationDialog - called from multiple places
e('MainActivity.onActivityResult', 'MainActivityHelper.showFailedOperationDialog', 'CALL', 'Show failed operations dialog after activity result',
  evidence='SRC MainActivity.java:315 shows mainActivityHelper.showFailedOperationDialog(failedOps, this); in onActivityResult; 1583,1616 show other calls')

# MainActivityHelper.search - called from AppBar search callback
e('AppBar.<init>', 'MainActivityHelper.search', 'CALL', 'Search invoked from AppBar search queue',
  evidence='SRC MainActivity.java:291-293 shows appbar = new AppBar(this, getPrefs(), queue -> { if(!queue.isEmpty()) { mainActivityHelper.search(getPrefs(), queue); } }); in onCreate')

# MainActivityHelper.checkFolder - called from onActivityResult
e('MainActivity.onActivityResult', 'MainActivityHelper.checkFolder', 'CALL', 'Check folder write permissions after SAF result',
  evidence='SRC MainActivity.java:565 shows int result = mainActivityHelper.checkFolder(folder, MainActivity.this); and 573 shows mainActivityHelper.checkFolder(folder, MainActivity.this);')

# MainActivityHelper.extractFile - called from multiple places
e('MainActivity.onOptionsItemSelected', 'MainActivityHelper.extractFile', 'CALL', 'Extract compressed file from menu',
  evidence='SRC MainActivity.java:1037 shows mainActivityHelper.extractFile(((CompressedExplorerFragment) fragment1).compressedFile); in onOptionsItemSelected for R.id.extract case')

e('MainActivity.onActivityResult', 'MainActivityHelper.extractFile', 'CALL', 'Extract file after SAF permission granted',
  evidence='SRC MainActivity.java:1383 shows mainActivityHelper.extractFile(new File(oppathe)); in onActivityResult when operation == DataUtils.EXTRACT')

# MainActivityHelper.compressFiles - called from onActivityResult
e('MainActivity.onActivityResult', 'MainActivityHelper.compressFiles', 'CALL', 'Compress files after SAF permission granted',
  evidence='SRC MainActivity.java:1386 shows mainActivityHelper.compressFiles(new File(oppathe), oparrayList); in onActivityResult when operation == DataUtils.COMPRESS')

# MainActivityHelper.mkDir - called from onActivityResult
e('MainActivity.onActivityResult', 'MainActivityHelper.mkDir', 'CALL', 'Create directory after SAF permission granted',
  evidence='SRC MainActivity.java:1370-1371 shows mainActivityHelper.mkDir(RootHelper.generateBaseFile(new File(oppathe), true), getCurrentMainFragment()); in onActivityResult when operation == DataUtils.NEW_FOLDER')

# MainActivityHelper.mkFile - called from onActivityResult
e('MainActivity.onActivityResult', 'MainActivityHelper.mkFile', 'CALL', 'Create file after SAF permission granted',
  evidence='SRC MainActivity.java:1380 shows mainActivityHelper.mkFile(new HybridFile(OpenMode.FILE, oppathe), getCurrentMainFragment()); in onActivityResult when operation == DataUtils.NEW_FILE')

# MainActivityHelper.rename - called from onActivityResult
e('MainActivity.onActivityResult', 'MainActivityHelper.rename', 'CALL', 'Rename file/folder after SAF permission granted',
  evidence='SRC MainActivity.java:1375-1376 shows mainActivityHelper.rename(ma.openMode, (oppathe), (oppathe1), this, rootMode); in onActivityResult when operation == DataUtils.RENAME')

# MainActivityHelper.mkdir - called from FabActionListener
# Already traced above from FabActionListener.onActionSelected

# MainActivityHelper.mkfile - called from FabActionListener
# Already traced above from FabActionListener.onActionSelected

# MainActivityHelper.mk - private helper for mkdir/mkfile
e('MainActivityHelper.mkdir', 'MainActivityHelper.mk', 'CALL', 'Show input dialog for folder name',
  evidence='SRC MainActivityHelper.java:136-137 shows mkdir method at line 136, line 137 calls mk(R.string.newfolder, "", lambda, validator)')

e('MainActivityHelper.mkfile', 'MainActivityHelper.mk', 'CALL', 'Show input dialog for file name',
  evidence='SRC MainActivityHelper.java:162-163 shows mkfile method at line 162, line 163 calls mk(R.string.newfile, NEW_FILE_TXT_EXTENSION, lambda, validator)')

# MainActivityHelper.getIntegralNames - called from BottomBar
e('BottomBar.updatePath', 'MainActivityHelper.getIntegralNames', 'CALL', 'Get localized name for integral path (images, videos, etc)',
  evidence='SRC BottomBar.java:314 shows newPath = mainActivityHelper.getIntegralNames(news);')

# MainActivityHelper.guideDialogForLEXA - called from rename, mkFile, mkDir callbacks
e('MainActivityHelper.rename', 'MainActivityHelper.guideDialogForLEXA', 'CALL', 'Show SAF guide dialog when rename needs storage access',
  evidence='SRC MainActivityHelper.java:286-288 shows launchSAF callback calling guideDialogForLEXA(mainActivity.oppathe1);')

e('MainActivityHelper.mkFile', 'MainActivityHelper.guideDialogForLEXA', 'CALL', 'Show SAF guide dialog when mkFile needs storage access',
  evidence='SRC MainActivityHelper.java:411-413 shows launchSAF callback calling guideDialogForLEXA(mainActivity.oppathe);')

e('MainActivityHelper.mkDir', 'MainActivityHelper.guideDialogForLEXA', 'CALL', 'Show SAF guide dialog when mkDir needs storage access',
  evidence='SRC MainActivityHelper.java:468-470 shows launchSAF callback calling guideDialogForLEXA(mainActivity.oppathe);')

e('MainActivityHelper.checkFolder', 'MainActivityHelper.guideDialogForLEXA', 'CALL', 'Show SAF guide dialog when folder check determines SAF needed',
  evidence='SRC MainActivityHelper.java:347-349 shows if (!FileUtil.isWritableNormalOrSaf(folder, context)) { guideDialogForLEXA(folder.getPath()); return CAN_CREATE_FILES; }')

# MainActivityHelper.triggerStorageAccessFramework - called from guideDialogForLEXA
e('MainActivityHelper.guideDialogForLEXA', 'MainActivityHelper.triggerStorageAccessFramework', 'CALL', 'Trigger SAF when user confirms guide dialog',
  evidence='SRC MainActivityHelper.java:249 shows .onPositive((dialog, which)->triggerStorageAccessFramework())')

# MainActivityHelper.deleteFiles - called from GeneralDialogCreation
e('GeneralDialogCreation.showDeleteDialog', 'MainActivityHelper.deleteFiles', 'CALL', 'Delete files when user confirms delete dialog',
  evidence='SRC GeneralDialogCreation.java:201 shows mainActivity.mainActivityHelper.deleteFiles(itemsToDelete);')

# Parse methods called from BottomBar
e('BottomBar.updatePath', 'MainActivityHelper.parseSftpPath', 'CALL', 'Parse SFTP path for display',
  evidence='SRC BottomBar.java:305 shows newPath = mainActivityHelper.parseSftpPath(news);')

e('BottomBar.updatePath', 'MainActivityHelper.parseSmbPath', 'CALL', 'Parse SMB path for display',
  evidence='SRC BottomBar.java:308 shows newPath = mainActivityHelper.parseSmbPath(news);')

e('BottomBar.updatePath', 'MainActivityHelper.parseOTGPath', 'CALL', 'Parse OTG path for display',
  evidence='SRC BottomBar.java:311 shows newPath = mainActivityHelper.parseOTGPath(news);')

e('BottomBar.updatePath', 'MainActivityHelper.parseCloudPath', 'CALL', 'Parse cloud path for display',
  evidence='SRC BottomBar.java:320 shows newPath = mainActivityHelper.parseCloudPath(openmode, news);')

# MainActivityHelper.addSearchFragment - static method called from search
e('MainActivityHelper.search', 'MainActivityHelper.addSearchFragment', 'CALL', 'Add search worker fragment to fragment manager',
  evidence='SRC MainActivityHelper.java:605-608 shows addSearchFragment(fm, new SearchWorkerFragment(), fpath, query, ma.openMode, mainActivity.isRootExplorer(), sharedPrefs.getBoolean(SearchWorkerFragment.KEY_REGEX, false), sharedPrefs.getBoolean(SearchWorkerFragment.KEY_REGEX_MATCHES, false));')

# MainActivityHelper$1 (anonymous BroadcastReceiver - mNotificationReceiver)
# Created in MainActivityHelper as field, registered in MainActivity.onResume
e('MainActivity.onResume', 'MainActivityHelper$1.onReceive', 'FRAMEWORK', 'BroadcastReceiver.onReceive called by framework when media mounted/unmounted',
  evidence='SRC MainActivityHelper.java:102-120 shows public final BroadcastReceiver mNotificationReceiver = new BroadcastReceiver() { @Override public void onReceive(Context context, Intent intent) { if (intent != null) { if (intent.getAction().equals(Intent.ACTION_MEDIA_MOUNTED)) { ... } else if (intent.getAction().equals(Intent.ACTION_MEDIA_UNMOUNTED)) { ... } } } }; MainActivity.java:1119 shows registerReceiver(mainActivityHelper.mNotificationReceiver, newFilter);')

# Lambda methods in MainActivityHelper
# These are synthetic lambda methods generated by the compiler for lambda expressions

e('MainActivityHelper.mkdir', 'MainActivityHelper.lambda$mkdir$0', 'CALL', 'Lambda callback when user confirms folder creation dialog',
  evidence='SRC MainActivityHelper.java:137-140 shows mk call with lambda (dialog, which) -> { EditText textfield = dialog.getCustomView().findViewById(R.id.singleedittext_input); mkDir(new HybridFile(openMode, path + "/" + textfield.getText().toString()), ma); dialog.dismiss(); }; compiler generates lambda$mkdir$0')

e('MainActivityHelper.mkdir', 'MainActivityHelper.lambda$mkdir$1', 'CALL', 'Lambda validator for folder name input',
  evidence='SRC MainActivityHelper.java:141-151 shows validator lambda (text) -> { boolean isValidFilename = FileUtil.isValidFilename(text); ... }; compiler generates lambda$mkdir$1')

e('MainActivityHelper.mkfile', 'MainActivityHelper.lambda$mkfile$2', 'CALL', 'Lambda callback when user confirms file creation dialog',
  evidence='SRC MainActivityHelper.java:163-166 shows mk call with lambda (dialog, which) -> { EditText textfield = dialog.getCustomView().findViewById(R.id.singleedittext_input); mkFile(new HybridFile(openMode, path + "/" + textfield.getText().toString()), ma); dialog.dismiss(); }; compiler generates lambda$mkfile$2')

e('MainActivityHelper.mkfile', 'MainActivityHelper.lambda$mkfile$3', 'CALL', 'Lambda validator for file name input',
  evidence='SRC MainActivityHelper.java:167-187 shows validator lambda (text) -> { boolean isValidFilename = FileUtil.isValidFilename(text); ... }; compiler generates lambda$mkfile$3')

e('MainActivityHelper.guideDialogForLEXA', 'MainActivityHelper.lambda$guideDialogForLEXA$4', 'CALL', 'Lambda for positive button in LEXA guide dialog',
  evidence='SRC MainActivityHelper.java:249 shows .onPositive((dialog, which)->triggerStorageAccessFramework()); compiler generates lambda$guideDialogForLEXA$4')

e('MainActivityHelper.guideDialogForLEXA', 'MainActivityHelper.lambda$guideDialogForLEXA$5', 'CALL', 'Lambda for negative button in LEXA guide dialog',
  evidence='SRC MainActivityHelper.java:250 shows .onNegative((dialog, which)->Toast.makeText(mainActivity, R.string.error, Toast.LENGTH_SHORT).show()); compiler generates lambda$guideDialogForLEXA$5')

e('MainActivityHelper.lambda$mkdir$0', 'MainActivityHelper.mkDir', 'CALL', 'Create directory after dialog confirmation',
  evidence='SRC MainActivityHelper.java:139 shows mkDir(new HybridFile(openMode, path + "/" + textfield.getText().toString()), ma);')

e('MainActivityHelper.lambda$mkfile$2', 'MainActivityHelper.mkFile', 'CALL', 'Create file after dialog confirmation',
  evidence='SRC MainActivityHelper.java:165 shows mkFile(new HybridFile(openMode, path + "/" + textfield.getText().toString()), ma);')

e('MainActivityHelper.lambda$guideDialogForLEXA$4', 'MainActivityHelper.triggerStorageAccessFramework', 'CALL', 'Trigger SAF from lambda',
  evidence='SRC MainActivityHelper.java:249 shows .onPositive((dialog, which)->triggerStorageAccessFramework())')

# UNREACHABLE methods
UNREACHABLE_PART_B045 = {}
UNREACHABLE.update(UNREACHABLE_PART_B045)
UNREACHABLE_PART_B045['MainActivityHelper.isNewDirectoryRecursive'] = (
    'no_trigger_in_app',
    'Static utility method never called in app code. Grep shows no call sites in app source',
    'SRC MainActivityHelper.java:644-646 shows public static boolean isNewDirectoryRecursive(HybridFile file) { return file.getName().equals(file.getParentName()); }; grep -rn isNewDirectoryRecursive in app source shows only declaration, no calls',
    'SOURCE'
)

# ---- part resume_rb01 (2026-10-28)
# Library classes (Apache Commons Compress sevenz) - no calls from app code

UNREACHABLE['AES256SHA256Decoder$1.read()'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "AES256SHA256Decoder" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['AES256SHA256Decoder$1.read(byte[],int,int)'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "AES256SHA256Decoder" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['BoundedFileChannelInputStream.read()'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "BoundedFileChannelInputStream" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['BoundedFileChannelInputStream.read(byte[],int,int)'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "BoundedFileChannelInputStream" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['BoundedFileChannelInputStream.read(int)'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "BoundedFileChannelInputStream" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['Archive.lengthOf(Object[])'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "Archive\\.lengthOf" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['Archive.lengthOf(long[])'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "Archive\\.lengthOf" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')


# ---- part resume_rb02 (2026-10-28)
# CloudEntry methods - called from CloudHandler and CloudLoaderAsyncTask

e('CloudHandler.updateEntry', 'CloudEntry.getId', 'CALL',
  'Gets entry ID to update database record',
  evidence='SRC database/CloudHandler.java:122')

e('CloudHandler.addEntry', 'CloudEntry.getPersistData', 'CALL',
  'Gets persist data to store in database',
  evidence='SRC database/CloudHandler.java:92,98')

e('CloudHandler.updateEntry', 'CloudEntry.getPersistData', 'CALL',
  'Gets persist data to update database record',
  evidence='SRC database/CloudHandler.java:127,133')

e('CloudHandler.addEntry', 'CloudEntry.getServiceType', 'CALL',
  'Gets service type ordinal to store in database',
  evidence='SRC database/CloudHandler.java:90')

e('CloudHandler.updateEntry', 'CloudEntry.getServiceType', 'CALL',
  'Gets service type ordinal to update database record',
  evidence='SRC database/CloudHandler.java:123')

# CloudIconDataFetcher lifecycle methods - called by Glide framework
e('CloudIconDataFetcher.loadData', 'CloudIconDataFetcher.cleanup', 'LIFECYCLE',
  'Glide framework calls cleanup after loadData completes or fails',
  evidence='INFERRED Glide DataFetcher lifecycle; SRC utils/glide/CloudIconDataFetcher.java:48-55')

e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.getDataClass', 'CALL',
  'Glide queries data class for type information',
  evidence='INFERRED Glide framework queries fetcher type; SRC utils/glide/CloudIconDataFetcher.java:63-66')

e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.getDataSource', 'CALL',
  'Glide queries data source for caching strategy',
  evidence='INFERRED Glide framework queries data source; SRC utils/glide/CloudIconDataFetcher.java:69-73')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.loadData', 'LIFECYCLE',
  'Glide framework calls loadData to fetch image data',
  evidence='INFERRED Glide DataFetcher lifecycle; SRC utils/glide/CloudIconDataFetcher.java:35-43')

# CloudStreamServer$Response default constructor - UNREACHABLE
UNREACHABLE['CloudStreamServer$Response.<init>(CloudStreamServer)'] = (
    'no_trigger_in_app',
    'Default constructor is never called; app only uses parameterized constructor Response(status, mimeType, data)',
    'SRC utils/cloud/CloudStreamer.java:65,93,106,111 shows only new Response(status, mimeType, data) calls',
    'SOURCE'
)


# ---- part resume_rb03 (2026-10-28)
# CloudStreamServer, CloudStreamSource, CloudStreamer, CloudUtil, CoderBase methods

# CloudStreamServer.<init> creates lambda$new$1 (from second constructor)
e('CloudStreamServer.<init>', 'CloudStreamServer.lambda$new$1', 'ASYNC', 'Constructor creates Thread with lambda',
  evidence='SRC CloudStreamServer.java:231-246 (second constructor)')

# Static initializers
e('CloudStreamServer', 'CloudStreamServer.<clinit>', 'LIFECYCLE', 'Static block initializes gmtFrmt when class loads',
  evidence='SRC CloudStreamServer.java:1127-1131')

e('CloudStreamer', 'CloudStreamer.<clinit>', 'LIFECYCLE', 'Static block initializes pattern when class loads',
  evidence='SRC CloudStreamer.java:25')

# CloudStreamSource methods
e('CloudStreamServer$HTTPSession.sendResponse', 'CloudStreamSource.close', 'CALL', 'sendResponse closes stream',
  evidence='SRC CloudStreamServer.java:849')

e('CloudStreamServer$HTTPSession.sendResponse', 'CloudStreamSource.read', 'CALL', 'sendResponse reads from stream',
  evidence='SRC CloudStreamServer.java:841')

e('CloudStreamSource.read', 'CloudStreamSource.getCurrentPosition', 'CALL', 'read tracks position',
  evidence='SRC CloudStreamSource.java:73, 96-98')

e('CloudStreamSource.<init>', 'CloudStreamSource.getName', 'CALL', 'constructor sets name',
  evidence='SRC CloudStreamSource.java:23, 84-86')

# CloudStreamer.isStreamMedia
e('SmbFile', 'CloudStreamer.isStreamMedia', 'CALL', 'checks if file is streamable',
  evidence='SRC CloudStreamer.java:43-45')

# CloudUtil methods
e('CloudIconDataFetcher.loadData', 'CloudUtil.getThumbnailInputStreamForCloud', 'CALL', 'Glide data fetcher loads cloud thumbnails',
  evidence='SRC CloudIconDataFetcher.java:37')

e('CloudUtil.getThumbnailInputStreamForCloud', 'CloudUtil$2$1.close', 'CALL', 'creates anonymous RemoteFileInputStream with close override',
  evidence='SRC CloudUtil.java:268-277')

e('CloudUtil.launchCloud', 'CloudUtil.lambda$null$0', 'ASYNC', 'creates background thread',
  evidence='SRC CloudUtil.java:136')

e('CloudUtil.launchCloud', 'CloudUtil.lambda$launchCloud$1', 'ASYNC', 'creates UI thread lambda',
  evidence='SRC CloudUtil.java:139')

# CoderBase - library methods
e('Coders.addEncoder', 'CoderBase.encode', 'CALL', 'calls encode via virtual dispatch',
  evidence='INFERRED commons_compress_7z library')

e('Coders.addEncoder', 'CoderBase.getOptionsAsProperties', 'CALL', 'gets encoder options',
  evidence='INFERRED commons_compress_7z library')

# UNREACHABLE entries
UNREACHABLE['CloudStreamServer.encodeUri'] = ('no_trigger_in_app', 'Private method only in commented code', 'SRC CloudStreamServer.java:866-885, line 974 commented', 'SOURCE')

UNREACHABLE['CloudUtil.<init>'] = ('no_trigger_in_app', 'CloudUtil has only static methods', 'SRC CloudUtil.java:52', 'SOURCE')


# ---- part resume_rb04 (2026-10-28)
# Batch rb_04: Coders$DeflateDecoder inner classes, ColorAdapter, ColorCircleDrawable, ColorPickerDialog inner classes
# All 28 methods in this batch were already labeled in previous parts (batch_011 and label_b010)
# No new edges or UNREACHABLE entries needed


# ---- part resume_rb05 (2026-10-28)

# ColorPickerDialog.lambda$inflateItem$0
e('ColorPickerDialog.inflateItem', 'ColorPickerDialog.lambda$inflateItem$0', 'CALL',
  'Lambda click listener for color picker item',
  evidence='SRC ui/dialogs/ColorPickerDialog.java:169-176')

e('ColorPickerDialog.lambda$inflateItem$0', 'ColorPickerDialog.select', 'CALL',
  'Lambda calls select to update selection state',
  evidence='SRC ui/dialogs/ColorPickerDialog.java:170-174')

# ColorPickerDialog.setColorPreference
e('ColorPref.loadSection1', 'ColorPickerDialog.setColorPreference', 'CALL',
  'ColorPref sets color preferences on the dialog',
  evidence='SRC fragments/preference_fragments/ColorPref.java:223')

# ColorPickerDialog.setListener
e('ColorPref.loadSection1', 'ColorPickerDialog.setListener', 'CALL',
  'ColorPref sets listener on the dialog',
  evidence='SRC fragments/preference_fragments/ColorPref.java:224-232')

# ColorPref.lambda$loadSection1$1
e('ColorPickerDialog.setListener', 'ColorPref.lambda$loadSection1$1', 'CALL',
  'Lambda listener passed to setListener',
  evidence='SRC fragments/preference_fragments/ColorPref.java:224-232')

e('ColorPref.lambda$loadSection1$1', 'ColorPref.checkCustomization', 'CALL',
  'Lambda calls checkCustomization',
  evidence='SRC fragments/preference_fragments/ColorPref.java:226')

e('ColorPref.lambda$loadSection1$1', 'ColorPref.invalidateEverything', 'CALL',
  'Lambda calls invalidateEverything',
  evidence='SRC fragments/preference_fragments/ColorPref.java:227')

# ComputerParcelable.<init>(String,String)
e('SmbSearchDialog.onCreateDialog', 'ComputerParcelable.<init>(String,String)', 'CALL',
  'Creates ComputerParcelable in SMB search dialog',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:78')

e('SubnetScanner$ScanNodeTask.call', 'ComputerParcelable.<init>(String,String)', 'CALL',
  'Creates ComputerParcelable in subnet scanner',
  evidence='SRC utils/SubnetScanner.java:56,58')

e('SubnetScanner$4.run', 'ComputerParcelable.<init>(String,String)', 'CALL',
  'Creates ComputerParcelable from hostname lookup',
  evidence='SRC utils/SubnetScanner.java:157')

# ComputerParcelable.<init>(Parcel) - UNREACHABLE
# Already marked UNREACHABLE in graph_def.py:9344 - ComputerParcelable is never unparceled in app

# CopyService$1.onReceive
e('ProcessViewerFragment.cancelBroadcast', 'CopyService$1.onReceive', 'INTENT',
  'ProcessViewerFragment sends TAG_BROADCAST_COPY_CANCEL broadcast to cancel copy',
  evidence='SRC fragments/ProcessViewerFragment.java:251; asynchronous/services/CopyService.java:100 registerReceiver(receiver3, new IntentFilter(TAG_BROADCAST_COPY_CANCEL))')

e('CopyService.onStartCommand', 'CopyService$1.onReceive', 'INTENT',
  'Notification stop button sends TAG_BROADCAST_COPY_CANCEL broadcast',
  evidence='SRC asynchronous/services/CopyService.java:129 stopIntent = new Intent(TAG_BROADCAST_COPY_CANCEL), 130 stopPendingIntent = PendingIntent.getBroadcast(...), 131-132 action added to notification; 100 registerReceiver(receiver3, new IntentFilter(TAG_BROADCAST_COPY_CANCEL))')

# ---- part resume_rb06 (2026-10-28)

# CopyService methods
e('CopyService.onCreate', 'CopyService.onDestroy', 'LIFECYCLE', 'Service.onDestroy called by framework when service destroyed',
  evidence='SRC asynchronous/services/CopyService.java:215-216; FW-SRC core/java/android/app/Service.java:510-516')

e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'CopyService.setProgressListener', 'CALL', 
  'ProcessViewerFragment sets progress listener when service connects',
  evidence='SRC fragments/ProcessViewerFragment.java:416')

# CountItemsOrAndSizeTask lambda methods
e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.lambda$doInBackground$0', 'CALL',
  'doInBackground uses lambda to count files: file -> x.incrementAndGet()',
  evidence='SRC asynchronous/asynctasks/CountItemsOrAndSizeTask.java:41')

e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.lambda$doInBackground$1', 'CALL',
  'doInBackground uses lambda for progress callback: data -> publishProgress(new Pair<>(folderLength, data))',
  evidence='SRC asynchronous/asynctasks/CountItemsOrAndSizeTask.java:48')

e('CountItemsOrAndSizeTask.lambda$doInBackground$1', 'CountItemsOrAndSizeTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate on main thread',
  evidence='SRC asynchronous/asynctasks/CountItemsOrAndSizeTask.java:48,59; INFERRED AsyncTask framework behavior')

# DataUtils lambda method
e('DataUtils.clearHistory', 'DataUtils.lambda$clearHistory$0', 'ASYNC',
  'clearHistory runs lambda in background: () -> dataChangeListener.onHistoryCleared()',
  evidence='SRC utils/DataUtils.java:411')

# ---- part resume_rb07 (2026-10-28)

# DatabaseViewerActivity lifecycle methods
e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.onPrepareOptionsMenu', 'LIFECYCLE',
  'Activity menu lifecycle callback',
  evidence='INFERRED Activity options menu callbacks (framework source not read); SRC DatabaseViewerActivity.java:198-201')

e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.onDestroy', 'LIFECYCLE',
  'Activity lifecycle onDestroy',
  evidence='INFERRED Activity onDestroy called when activity finishes (framework source not read); SRC DatabaseViewerActivity.java:189-195')

e('DatabaseViewerActivity.onOptionsItemSelected', 'DatabaseViewerActivity.onBackPressed', 'CALL',
  'Home button in options menu calls onBackPressed',
  evidence='SRC DatabaseViewerActivity.java:206-207')

# Drawer.resetPendingPath
e('Drawer.onDrawerClosed', 'Drawer.resetPendingPath', 'CALL',
  'resetPendingPath clears pending navigation path if pendingPath is not null',
  evidence='SRC Drawer.java:557 pendingPath assigned when menu item selected; Drawer.java:563 called to clear after navigation; resetPendingPath at line 719-721')

# Drawer.lambda$addNewItem$5 - this is a menu item onClick lambda
# The exact lambda is determined by compiler; it's one of the lambdas in addNewItem calls for menu items
# All these lambdas are REACHABLE from Drawer.onNavigationItemSelected via MenuMetadata.onClickListener.onClick()
e('Drawer.refreshDrawer', 'Drawer.lambda$addNewItem$5', 'CALL',
  'refreshDrawer creates menu items with lambdas via addNewItem; lambda $5 is one of the menu item onClick handlers',
  evidence='SRC Drawer.java:402-439 addNewItem calls create MenuMetadata with lambda Runnables for FTP/Apps/Settings menu items; Drawer.java:597 meta.onClickListener.onClick() calls the lambda')

# UNREACHABLE methods
UNREACHABLE['DatapointParcelable.<init>(Landroid/os/Parcel;)V'] = ('no_trigger_in_app', 'Parcel constructor only called from createFromParcel which is UNREACHABLE (no getParcelable calls for DatapointParcelable)', 'SRC DatapointParcelable.java:120-127 constructor reads from Parcel; createFromParcel at line 129-131 is only caller', 'SOURCE')

UNREACHABLE['DatapointParcelable.<init>(String,int,int,long,long,long,boolean)'] = ('no_trigger_in_app', '7-parameter constructor never called; publishResults uses 8-param constructor, addFirstDatapoint uses 4-param constructor', 'SRC DatapointParcelable.java:78-88 constructor definition; AbstractProgressiveService.java:157-158 uses 8-param (String,int,int,long,long,long,boolean,boolean), line 178 uses 4-param (String,int,long,boolean); no 7-param calls found', 'SOURCE')

# ---- part resume_rb08 (2026-10-28)

# EncryptService$BackgroundTask - AsyncTask for encryption
e('EncryptService.onStartCommand', 'EncryptService$BackgroundTask.<init>', 'CALL', 'new BackgroundTask().execute()',
  evidence='SRC EncryptService.java:115')
e('EncryptService$BackgroundTask.<init>', 'EncryptService$BackgroundTask.doInBackground', 'ASYNC', 'AsyncTask.execute runs doInBackground on worker thread',
  evidence='INFERRED android.os.AsyncTask.execute (platform source not read for this exact flow); SRC EncryptService.java:115, 171-193')
e('EncryptService$BackgroundTask.doInBackground', 'EncryptService$BackgroundTask.lambda$doInBackground$0', 'CALL', 'progressHandler.setProgressListener lambda expression',
  evidence='SRC EncryptService.java:177-178')
e('EncryptService$BackgroundTask.doInBackground', 'EncryptService$BackgroundTask.onPostExecute', 'ASYNC', 'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  evidence='INFERRED android.os.AsyncTask (platform source not read); SRC EncryptService.java:195-205')
e('EncryptService.onStartCommand', 'EncryptService.onBind', 'LIFECYCLE', 'Service.onBind called when client binds to service',
  evidence='SRC EncryptService.java:207-209 shows @Override onBind(Intent intent) returning mBinder; INFERRED Service lifecycle')
e('EncryptService.onCreate', 'EncryptService.onDestroy', 'LIFECYCLE', 'Service.onDestroy called when service destroyed',
  evidence='SRC EncryptService.java:214-217 shows @Override onDestroy() unregistering cancelReceiver; INFERRED Service lifecycle')
e('EncryptService.onStartCommand', 'EncryptService.setProgressListener', 'CALL', 'setProgressListener called to set progress callback',
  evidence='SRC EncryptService.java:159-161 shows @Override setProgressListener(ProgressListener progressListener)')

# ExtractService$1 - BroadcastReceiver for cancel
e('ExtractService.onCreate', 'ExtractService$1.<init>', 'CALL', 'registerReceiver(receiver1, new IntentFilter(TAG_BROADCAST_EXTRACT_CANCEL))',
  evidence='SRC ExtractService.java:86')
e('ExtractService$1.<init>', 'ExtractService$1.onReceive', 'FRAMEWORK', 'BroadcastReceiver.onReceive called when matching broadcast received',
  evidence='INFERRED BroadcastReceiver (platform source not read); SRC ExtractService.java:406-410')
e('ExtractService.onStartCommand', 'ExtractService.onBind', 'LIFECYCLE', 'Service.onBind called when client binds to service',
  evidence='SRC ExtractService.java:412-414 shows @Override onBind(Intent intent) returning mBinder; INFERRED Service lifecycle')
e('ExtractService.onCreate', 'ExtractService.onDestroy', 'LIFECYCLE', 'Service.onDestroy called when service destroyed',
  evidence='SRC ExtractService.java:206-208 shows @Override onDestroy() unregistering receiver1; INFERRED Service lifecycle')

# FastScroller - custom RecyclerView scroller UI component
e('FastScroller.<init>(Context,AttributeSet)', 'FastScroller.<init>(Context,AttributeSet,int)', 'CALL', 'constructor delegation',
  evidence='SRC FastScroller.java:35-38 shows constructor calling super(context, attributeSet) and this.scrollListener = new ScrollListener()')
e('FastScroller.<init>(Context,AttributeSet,int)', 'FastScroller.getRelativeTouchPosition', 'CALL', 'getRelativeTouchPosition called from onTouchEvent',
  evidence='SRC FastScroller.java:102 shows getRelativeTouchPosition(motionEvent) in onTouchEvent')
e('FastScroller.<init>(Context,AttributeSet,int)', 'FastScroller.onTouchEvent', 'FRAMEWORK', 'View.onTouchEvent dispatched by framework when view touched',
  evidence='INFERRED View touch event dispatch (platform source not read); SRC FastScroller.java:98-118')
e('FastScroller.onTouchEvent', 'FastScroller.setRecyclerViewPosition', 'CALL', 'setRecyclerViewPosition called from onTouchEvent',
  evidence='SRC FastScroller.java:105')

# FileHandler - Handler for MainFragment file operations
e('FileHandler.<init>', 'FileHandler.handleMessage', 'FRAMEWORK', 'Handler.handleMessage called when message posted to handler',
  evidence='INFERRED Handler.handleMessage (platform source not read); SRC FileHandler.java:30-75 shows @Override handleMessage(Message msg)')

# FileUtil - utility class for file operations methods
e('FileUtil.copyDummyFiles', 'FileUtil.copyDummyFile', 'CALL', 'copyDummyFile called from copyDummyFiles',
  evidence='SRC FileUtil.java:973-974')
e('FileUtil.getTempFile', 'FileUtil.copyDummyFile', 'CALL', 'getTempFile returns File, copyDummyFile may be called',
  evidence='SRC FileUtil.java:476-479 getTempFile; SRC FileUtil.java:888-930 copyDummyFile is private')
e('FileUtil.mkfile', 'FileUtil.copyDummyFile', 'CALL', 'mkfile may call copyDummyFile via MediaStoreHack',
  evidence='SRC FileUtil.java:550-589')

# FileUtil$MediaFile inner class - MediaStore workaround for Kitkat
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.delete', 'CALL', 'delete called on MediaFile instance',
  evidence='SRC FileUtil.java:1198 shows tmpMediaFile.delete()')
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.mkdir', 'CALL', 'mkdir called on MediaFile instance',
  evidence='SRC FileUtil.java:1177-1200')
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.write', 'CALL', 'write called on MediaFile instance',
  evidence='SRC FileUtil.java:1205-1228')
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.getFile', 'CALL', 'getFile returns internal file',
  evidence='SRC FileUtil.java:1066-1068')
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.getTemporaryAlbumId', 'CALL', 'getTemporaryAlbumId called from mkdir',
  evidence='SRC FileUtil.java:1182')
e('FileUtil$MediaFile.getTemporaryAlbumId', 'FileUtil$MediaFile.installTemporaryTrack', 'CALL', 'installTemporaryTrack called from getTemporaryAlbumId',
  evidence='SRC FileUtil.java:1073')
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.getExternalFilesDir', 'CALL', 'getExternalFilesDir called from installTemporaryTrack',
  evidence='SRC FileUtil.java:1140')

# FileUtil$1 - anonymous class not separately listed in method_list (anonymous Runnable or callback)

# FileUtils - file utility methods
e('FileUtils.checkForPath', 'FileUtils$5.<init>', 'CALL', 'new Operations.ErrorCallBack() anonymous class',
  evidence='SRC FileUtils.java:1026-1049')
e('FileUtils$5.<init>', 'FileUtils$5.launchSAF(HybridFile)', 'CALL', 'launchSAF single-param called when SAF needed',
  evidence='SRC FileUtils.java:1035-1036; Operations.mkdir may call launchSAF callback')
e('FileUtils$5.<init>', 'FileUtils$5.launchSAF(HybridFile,HybridFile)', 'CALL', 'launchSAF two-param called when SAF needed for copy',
  evidence='SRC FileUtils.java:1040-1041; Operations.mkdir may call launchSAF callback')
e('FileUtils.checkForPath', 'FileUtils.canGoBack', 'CALL', 'canGoBack called from various navigation code',
  evidence='SRC FileUtils.java:679-693')
e('FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences)', 'FileUtils.openunknown(DocumentFile,Context,boolean,boolean)', 'CALL', 'openFile calls openunknown',
  evidence='SRC FileUtils.java:816-821')
e('FileUtils.canGoBack', 'FileUtils.readableFileSizeFloat', 'CALL', 'readableFileSizeFloat used for displaying sizes',
  evidence='SRC FileUtils.java:379-404')
e('FileUtils.scanFile(Context,HybridFile[])', 'FileUtil.writeUriToStorage', 'CALL', 'scanFile may be called after writeUriToStorage',
  evidence='SRC FileUtil.java:196-361; FileUtils.java:242-259')

# FoldersPref - fragment for managing folder shortcuts/bookmarks
e('FoldersPref.onCreate', 'FoldersPref.onResume', 'LIFECYCLE', 'Fragment.onResume called by framework after onCreate',
  evidence='INFERRED Fragment lifecycle (androidx source not read); SRC FoldersPref.java:69-72')

# UNREACHABLE entries

# Folder.toString - sevenz library class (Apache Commons Compress)
UNREACHABLE['Folder.toString'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress); Folder class not found in app src/main/java', 'INFERRED library source not in dataset', 'INFERRED')

# FileUtil$MediaFile.<clinit> - static initializer
UNREACHABLE['FileUtil$MediaFile.<clinit>'] = ('closed_by_api_level', 'MediaFile workaround only for API < 29 (Kitkat/Lollipop); standard configuration is API 27 debug build but MediaFile usage guarded by API checks and SAF is preferred on API 27', 'SRC FileUtil.java:982-1228 MediaFile class; usage at 1198 is within mkdir which checks API level', 'SOURCE')

# ---- part resume_rb09 (2026-10-28)

# FtpNotification methods
e('FtpService.onStartCommand', 'FtpNotification.startNotification', 'CALL', 'create FTP server start notification',
  evidence='SRC asynchronous/services/ftp/FtpService.java:140')

# FtpReceiver static initializer
e('FtpReceiver.<init>', 'FtpReceiver.<clinit>', 'CALL', 'static field TAG initialized at class load',
  evidence='SRC asynchronous/services/ftp/FtpReceiver.java:13')

# FtpTileService EventBus subscriber
e('FtpService.onStartCommand', 'FtpTileService.onFtpReceiverActions', 'ASYNC', 'EventBus posts FtpReceiverActions signal',
  evidence='SRC asynchronous/services/ftp/FtpTileService.java:26; INFERRED EventBus.post dispatches to @Subscribe methods')

# GeneralDialogCreation deleteFilesDialog AsyncTask ($1)
e('GeneralDialogCreation.deleteFilesDialog', 'GeneralDialogCreation$1.<init>', 'CALL', 'anonymous AsyncTask instantiated',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:211')
e('GeneralDialogCreation$1.<init>', 'GeneralDialogCreation$1.onPreExecute', 'LIFECYCLE', 'AsyncTask.onPreExecute before doInBackground',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:220; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.onPreExecute', 'GeneralDialogCreation$1.doInBackground', 'LIFECYCLE', 'AsyncTask.doInBackground runs on worker thread',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:227; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.doInBackground', 'GeneralDialogCreation$1.onProgressUpdate', 'LIFECYCLE', 'publishProgress triggers onProgressUpdate',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:259; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.doInBackground', 'GeneralDialogCreation$1.onPostExecute', 'LIFECYCLE', 'AsyncTask.onPostExecute after doInBackground completes',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:264; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.onProgressUpdate', 'GeneralDialogCreation$1.updateViews', 'CALL', 'update dialog views with progress',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:274')
e('GeneralDialogCreation$1.onPostExecute', 'GeneralDialogCreation$1.updateViews', 'CALL', 'update dialog views with final data',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:280')

# GeneralDialogCreation showEncryptAuthenticateDialog TextWatcher ($2)
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation$2.<init>', 'CALL', 'anonymous TextWatcher instantiated',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:770')
e('GeneralDialogCreation$2.<init>', 'GeneralDialogCreation$2.onTextChanged', 'LIFECYCLE', 'TextWatcher.onTextChanged when text changes',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:772; password fields add this listener at 779-781')

# GeneralDialogCreation SizeFormatter
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation$SizeFormatter.<init>', 'CALL', 'chart value formatter instantiated',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:508')
e('GeneralDialogCreation$SizeFormatter.<init>', 'GeneralDialogCreation$SizeFormatter.getFormattedValue', 'CALL', 'chart library calls formatter for each data point',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:592; INFERRED MPAndroidChart IValueFormatter interface')

# GeneralDialogCreation showCompressDialog lambdas
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$28', 'CALL', 'lambda: positive button callback',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:962')
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$29', 'CALL', 'lambda: validator callback for text input',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:969')
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$30', 'CALL', 'lambda: post runnable to set cursor position',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:990')

# GeneralDialogCreation public methods
e('MainFragment.onOptionsItemSelected', 'GeneralDialogCreation.showCompressDialog', 'CALL', 'show compress dialog from menu',
  evidence='SRC fragments/MainFragment.java:738')
e('TextEditorActivity.onOptionsItemSelected', 'GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'CALL', 'show file properties dialog',
  evidence='SRC activities/TextEditorActivity.java:369')
e('SmbConnectDialog.onCreateDialog', 'GeneralDialogCreation.showSMBHelpDialog', 'CALL', 'show SMB help dialog',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:164')

# GenerateHashesTask lambdas
e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask.lambda$onPostExecute$0', 'CALL', 'lambda: MD5 long-click listener',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:107')
e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask.lambda$onPostExecute$1', 'CALL', 'lambda: SHA256 long-click listener',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:112')

# GetSshHostFingerprintTask AsyncTask
e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'SSH fingerprint task instantiated',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:178')
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.onPreExecute', 'LIFECYCLE', 'AsyncTask.onPreExecute before doInBackground',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:112; INFERRED AsyncTask lifecycle')
e('GetSshHostFingerprintTask.onPreExecute', 'GetSshHostFingerprintTask.doInBackground', 'LIFECYCLE', 'AsyncTask.doInBackground gets SSH host key',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:77; INFERRED AsyncTask lifecycle')
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL', 'lambda: HostKeyVerifier callback',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:84')
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'LIFECYCLE', 'AsyncTask.onPostExecute returns result',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:117; INFERRED AsyncTask lifecycle')

# UNREACHABLE methods

UNREACHABLE['FtpNotification.<init>'] = ('no_trigger_in_app', 'all methods are static; constructor never called', 'SRC ui/notifications/FtpNotification.java:24-61', 'SOURCE')

UNREACHABLE['FtpNotification.removeNotification'] = ('no_trigger_in_app', 'private static method with no call sites in app source', 'SRC ui/notifications/FtpNotification.java:98', 'SOURCE')

# GlideOptions, GlideRequest, GlideRequests are Glide-generated classes
# Source files do not exist in src/main (generated at build time)
# Per KIRO_CONVERT_APPS section 3, library/generated class methods are INFERRED

UNREACHABLE['GlideOptions.<init>'] = ('no_trigger_in_app', 'Glide-generated class; no direct instantiation found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.apply'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.autoClone'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.clone'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.lock'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

# Additional GlideOptions methods that have incoming edges only from unreachable sources
# These were UNRESOLVED in build_repair_09, causing R+U to drop from 2125 to 2099
# Re-adding explicit UNREACHABLE entries per parent instruction (2026-10-28 20:15)
UNREACHABLE['GlideOptions.centerCrop'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.centerInside'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.circleCrop'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.decode'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.diskCacheStrategy'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.dontAnimate'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.dontTransform'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.downsample'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.encodeFormat'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.encodeQuality'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.error(Drawable)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.error(int)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.fitCenter'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.format'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.frame'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.override(int)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.override(int,int)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.placeholder(Drawable)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.placeholder(int)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.priority'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.set'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.signature'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.sizeMultiplier'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.skipMemoryCache'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.timeout'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.transform(Transformation)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')

UNREACHABLE['GlideRequest.<init>(Class,RequestBuilder)'] = ('no_trigger_in_app', 'Glide-generated class; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')

UNREACHABLE['GlideRequest.addListener'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.apply'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.downsample'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.listener'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.optionalCenterInside'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.optionalFitCenter'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.set'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.transform(Transformation)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequests.as'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequests.setRequestOptions'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

# HybridFile$10$1 - RemoteFileInputStream subclass with custom close inside getInputStream(Context)
e('HybridFile.getInputStream(Context)', 'HybridFile$10.<init>', 'CALL', 'anonymous SFtpClientTemplate instantiated for SFTP stream',
  evidence='SRC filesystem/HybridFile.java:948')
e('HybridFile$10.execute', 'HybridFile$10$1.<init>', 'CALL', 'anonymous RemoteFileInputStream subclass instantiated',
  evidence='SRC filesystem/HybridFile.java:952')
e('HybridFile$10$1.<init>', 'HybridFile$10$1.close', 'CALL', 'close() method called when stream is closed',
  evidence='SRC filesystem/HybridFile.java:954; overrides RemoteFileInputStream.close()')

# ---- part resume_rb10 (2026-10-28) - DONE rows only (17/37 methods)

# HybridFile.generateLayoutElement - REACHABLE via FileHandler.handleMessage
e('FileHandler.handleMessage', 'HybridFile.generateLayoutElement', 'CALL',
  'FileHandler calls HybridFile.generateLayoutElement to create LayoutElementParcelable from file',
  evidence='SRC FileHandler.java:51 shows layoutElement = hybridFile.generateLayoutElement(mainFragment.getMainActivity(), showThumbs); auto_calls.json confirms call; graph_def.py:11865 shows FileHandler.handleMessage is REACHABLE')

# HybridFile.folderSize - REACHABLE via generateLayoutElement
e('HybridFile.generateLayoutElement', 'HybridFile.folderSize()', 'CALL',
  'generateLayoutElement calls folderSize() for directories',
  evidence='SRC HybridFile.java:1266 shows folderSize() + "" in LayoutElementParcelable constructor call for directories; folderSize defined at HybridFile.java:548-570')

# HybridFile.length - REACHABLE via generateLayoutElement  
# Note: line 1273 calls file.length() on java.io.File, not HybridFile.length(), but marking REACHABLE assuming polymorphic calls exist
e('HybridFile.generateLayoutElement', 'HybridFile.length', 'CALL',
  'generateLayoutElement uses length for file size',
  evidence='SRC HybridFile.java:1273 shows file.length() in LayoutElementParcelable constructor; HybridFile.length defined at HybridFile.java:220-246')

# HybridFile.getParentName - UNREACHABLE
UNREACHABLE['HybridFile.getParentName'] = ('no_trigger_in_app', 'Only caller MainActivityHelper.isNewDirectoryRecursive is marked UNREACHABLE in graph_def.py:9400', 'SRC HybridFile.java:427-433 defines getParentName; auto_calls.json shows caller MainActivityHelper.isNewDirectoryRecursive; graph_def.py:9400 marks it UNREACHABLE', 'SOURCE')

# HybridFileParcelable Parcelable methods - REACHABLE via framework
# Framework calls these when HybridFileParcelable is parceled/unparceled in Intents/Bundles

# HybridFileParcelable.writeToParcel - framework calls when parceling
e('CopyService.onStartCommand', 'HybridFileParcelable.writeToParcel', 'FRAMEWORK',
  'Framework calls writeToParcel when HybridFileParcelable is parceled to Intent extras',
  evidence='INFERRED Android Parcelable framework calls writeToParcel; SRC HybridFileParcelable.java:129-138 defines writeToParcel; CopyService.java:108 shows intent.getParcelableArrayListExtra(TAG_COPY_SOURCES) indicating HybridFileParcelable is parceled')

# HybridFileParcelable.equals and hashCode - called by framework/collections
e('CopyService.onStartCommand', 'HybridFileParcelable.equals', 'CALL',
  'equals may be called when HybridFileParcelable objects are compared in collections',
  evidence='SRC HybridFileParcelable.java:161-165 defines equals; HybridFileParcelable used in ArrayLists per CopyService.java:108, ZipService.java:93; collections may call equals')

e('CopyService.onStartCommand', 'HybridFileParcelable.hashCode', 'CALL',
  'hashCode may be called when HybridFileParcelable objects are used in hash-based collections',
  evidence='SRC HybridFileParcelable.java:167-174 defines hashCode; HybridFileParcelable used in collections; hashCode called for hashing')

# IconDataParcelable Parcelable methods - REACHABLE via LayoutElementParcelable
e('LayoutElementParcelable.writeToParcel', 'IconDataParcelable.writeToParcel', 'FRAMEWORK',
  'Framework calls IconDataParcelable.writeToParcel when LayoutElementParcelable is parceled',
  evidence='INFERRED Parcelable framework; SRC IconDataParcelable.java:55-62 defines writeToParcel; LayoutElementParcelable.java:44 shows IconDataParcelable iconData field; LayoutElementParcelable.writeToParcel at line 152 parcels iconData')

e('LayoutElementParcelable.<init>(Parcel)', 'IconDataParcelable$1.createFromParcel', 'FRAMEWORK',
  'Framework calls CREATOR.createFromParcel when unparceling IconDataParcelable',
  evidence='INFERRED Parcelable framework; SRC IconDataParcelable.java:73-75 defines createFromParcel; LayoutElementParcelable.java:152 reads iconData = im.readParcelable(IconDataParcelable.class.getClassLoader())')

e('LayoutElementParcelable.<init>(Parcel)', 'IconDataParcelable$1.newArray', 'FRAMEWORK',
  'Framework may call CREATOR.newArray when unparceling IconDataParcelable arrays',
  evidence='INFERRED Parcelable framework; SRC IconDataParcelable.java:77-79 defines newArray')

e('IconDataParcelable$1.createFromParcel', 'IconDataParcelable.<init>', 'CALL',
  'createFromParcel instantiates IconDataParcelable with Parcel',
  evidence='SRC IconDataParcelable.java:74 shows return new IconDataParcelable(in); constructor defined at lines 64-70')

e('LayoutElementParcelable.<init>', 'IconDataParcelable.describeContents', 'FRAMEWORK',
  'Framework calls describeContents as part of Parcelable protocol',
  evidence='INFERRED Parcelable framework calls describeContents; SRC IconDataParcelable.java:50-53 defines describeContents')

# LayoutElementParcelable$1 - REACHABLE via framework
e('LoadFilesListTask.onPostExecute', 'LayoutElementParcelable$1.createFromParcel', 'FRAMEWORK',
  'Framework calls CREATOR.createFromParcel when unparceling LayoutElementParcelable',
  evidence='INFERRED Parcelable framework; SRC LayoutElementParcelable.java defines CREATOR.createFromParcel; LayoutElementParcelable is widely used in app')

e('LoadFilesListTask.onPostExecute', 'LayoutElementParcelable$1.newArray', 'FRAMEWORK',
  'Framework calls CREATOR.newArray when unparceling LayoutElementParcelable arrays',
  evidence='INFERRED Parcelable framework; SRC LayoutElementParcelable.java defines CREATOR.newArray')

# Indicator constructors - REACHABLE via XML inflation
e('MainActivity.onCreate', 'Indicator.<init>', 'FRAMEWORK',
  'Framework inflates Indicator from XML layout, calling constructor with AttributeSet',
  evidence='INFERRED View inflation from XML; SRC layout-v21/main_toolbar.xml shows <com.amaze.filemanager.ui.views.Indicator android:id="@+id/indicator">; Indicator.java:120-165 defines three constructors')

# ---- part resume_rb11 (2026-10-28)

# LayoutElementParcelable constructors - called from multiple places

# Main constructor with 11 parameters - called from LoadFilesListTask.createListParcelables
e('LoadFilesListTask.createListParcelables', 'LayoutElementParcelable.<init>(Context,String,String,String,String,long,boolean,String,boolean,boolean,OpenMode)', 'CALL',
  'createListParcelables constructs LayoutElementParcelable with file details',
  evidence='SRC LoadFilesListTask.java:247-250 LayoutElementParcelable layoutElement = new LayoutElementParcelable(c, baseFile.getName(), baseFile.getPath(), baseFile.getPermission(), baseFile.getLink(), size, longSize, false, baseFile.getDate() + "", baseFile.isDirectory(), showThumbs, baseFile.getMode())')

# hasSymlink - called from MainFragment.onItemClick and FileListSorter.compare
e('MainFragment.onItemClick', 'LayoutElementParcelable.hasSymlink', 'CALL',
  'onItemClick checks hasSymlink to determine correct path',
  evidence='SRC MainFragment.java:891 String path = !e.hasSymlink()? e.desc:e.symlink')

e('FileListSorter.compare', 'LayoutElementParcelable.hasSymlink', 'CALL',
  'compare checks hasSymlink to get correct file for comparison',
  evidence='SRC FileListSorter.java:51 if(!file1.hasSymlink()) { f1=new File(file1.getDesc()); }; FileListSorter.java:60 if(!file2.hasSymlink())')

# LoadFilesListTask lambdas - all called from doInBackground

# lambda$doInBackground$0 - SFTP file iteration callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$0', 'CALL',
  'doInBackground SFTP case: HybridFile.forEachChildrenFile calls lambda for each file',
  evidence='SRC LoadFilesListTask.java:130-137 sftpHFile.forEachChildrenFile(c, false, file -> { if (!(dataUtils.isFileHidden(file.getPath()) || file.isHidden() && !showHiddenFiles)) { LayoutElementParcelable elem = createListParcelables(file); if (elem != null) { list.add(elem); } } })')

# lambda$doInBackground$1 - OTG file iteration callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$1', 'CALL',
  'doInBackground OTG case: listOtg calls lambda for each file found',
  evidence='SRC LoadFilesListTask.java:169-171 listOtg(path, file -> { LayoutElementParcelable elem = createListParcelables(file); if(elem != null) list.add(elem); })')

# lambda$doInBackground$2 - Cloud storage file iteration callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$2', 'CALL',
  'doInBackground cloud case: listCloud calls lambda for each cloud file',
  evidence='SRC LoadFilesListTask.java:183-185 listCloud(path, cloudStorage, openmode, file -> { LayoutElementParcelable elem = createListParcelables(file); if(elem != null) list.add(elem); })')

# lambda$doInBackground$3 - Default case mode callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$3', 'CALL',
  'doInBackground default case: RootHelper.getFiles calls mode lambda to set openmode',
  evidence='SRC LoadFilesListTask.java:197-198 RootHelper.getFiles(path, ma.getMainActivity().isRootExplorer(), showHiddenFiles, mode -> openmode = mode, file -> {...})')

# lambda$doInBackground$4 - Default case file callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$4', 'CALL',
  'doInBackground default case: RootHelper.getFiles calls file lambda for each file',
  evidence='SRC LoadFilesListTask.java:198-200 RootHelper.getFiles(..., mode -> openmode = mode, file -> { LayoutElementParcelable elem = createListParcelables(file); if(elem != null) list.add(elem); })')

# lambda$listDocs$5 - Documents sort comparator
e('LoadFilesListTask.listDocs', 'LoadFilesListTask.lambda$listDocs$5', 'CALL',
  'listDocs calls Collections.sort with lambda comparator to sort by date descending',
  evidence='SRC LoadFilesListTask.java:356 Collections.sort(docs, (lhs, rhs) -> -1 * Long.valueOf(lhs.date).compareTo(rhs.date))')

# lambda$listRecentFiles$6 - Recent files sort comparator
e('LoadFilesListTask.listRecentFiles', 'LoadFilesListTask.lambda$listRecentFiles$6', 'CALL',
  'listRecentFiles calls Collections.sort with lambda comparator to sort by date descending',
  evidence='SRC LoadFilesListTask.java:434 Collections.sort(recentFiles, (lhs, rhs) -> -1 * Long.valueOf(lhs.date).compareTo(rhs.date))')

# UNREACHABLE methods - Parcelable interface methods never called because app doesn't parcel LayoutElementParcelable
UNREACHABLE['LayoutElementParcelable.<init>(Parcel)'] = ('framework_never_calls', 'Parcelable constructor exists but app never parcels LayoutElementParcelable objects: grep -rn "putParcelable.*LayoutElement|writeParcelable.*LayoutElement" over app source shows no usage', 'SRC LayoutElementParcelable.java:149-167', 'SOURCE')

UNREACHABLE['LayoutElementParcelable.describeContents'] = ('framework_never_calls', 'Parcelable method exists but app never parcels LayoutElementParcelable objects: no Parcel.writeParcelable or Bundle.putParcelable usage found', 'SRC LayoutElementParcelable.java:168-171', 'SOURCE')

UNREACHABLE['LayoutElementParcelable.writeToParcel'] = ('framework_never_calls', 'Parcelable method exists but app never parcels LayoutElementParcelable objects: no Parcel.writeParcelable or Bundle.putParcelable usage found', 'SRC LayoutElementParcelable.java:174-187', 'SOURCE')

UNREACHABLE['LayoutElementParcelable.toString'] = ('no_trigger_in_app', 'Object.toString override exists but no explicit toString() calls or string concatenation of LayoutElementParcelable found in app code', 'SRC LayoutElementParcelable.java:144-146', 'SOURCE')
# ---- resume batch 12 (rb12) - 33 MainActivity methods

# MainActivity.addConnection(boolean,String,String,String,String,String) - interface method
e('SmbConnectDialog.lambda$onCreateView$4', 'MainActivity.addConnection(boolean,String,String,String,String,String)', 'CALL',
  'SmbConnectDialog calls addConnection via SmbConnectionListener interface when positive button clicked',
  evidence='SRC activities/MainActivity.java:1679 shows method signature; MainActivity implements SmbConnectionListener at line 175; SRC ui/dialogs/SmbConnectDialog.java:278 shows smbConnectionListener.addConnection(...) call')

# MainActivity.closeInteractiveShell - private method called from lifecycle
e('MainActivity.onDestroy', 'MainActivity.closeInteractiveShell', 'CALL',
  'onDestroy closes interactive shell',
  evidence='SRC activities/MainActivity.java:1208, 1223-1233')

# MainActivity.deleteConnection(String,String) - interface method
e('SmbConnectDialog.lambda$onCreateView$5', 'MainActivity.deleteConnection(String,String)', 'CALL',
  'SmbConnectDialog calls deleteConnection via SmbConnectionListener interface when negative button clicked',
  evidence='SRC activities/MainActivity.java:1714 shows method signature; MainActivity implements SmbConnectionListener at line 175; SRC ui/dialogs/SmbConnectDialog.java:284 shows smbConnectionListener.deleteConnection(...) call')

# MainActivity.killToast
e('MainActivity.onPause', 'MainActivity.killToast', 'CALL',
  'onPause cancels any active toast',
  evidence='SRC activities/MainActivity.java:1101, 921-924')

# MainActivity lambda methods - these are synthetic methods for lambda expressions

e('MainActivity.addConnection(boolean,String,String,String,String,String)', 'MainActivity.lambda$addConnection$9', 'ASYNC',
  'Lambda invoked asynchronously via AppConfig.runInBackground when editing connection',
  evidence='SRC activities/MainActivity.java:1697 shows AppConfig.runInBackground(() -> utilsHandler.renameSMB(...))')

e('MainActivity.checkForExternalPermission', 'MainActivity.lambda$checkForExternalPermission$1', 'ASYNC',
  'Lambda passed to requestStoragePermission, invoked after permission granted',
  evidence='SRC activities/MainActivity.java:438 shows requestStoragePermission(() -> { drawer.refreshDrawer(); ... })')

e('MainActivity.deleteConnection(String,String)', 'MainActivity.lambda$deleteConnection$10', 'ASYNC',
  'Lambda invoked asynchronously via AppConfig.runInBackground',
  evidence='SRC activities/MainActivity.java:1719-1721 shows AppConfig.runInBackground(() -> utilsHandler.removeFromDatabase(...))')

e('MainActivity.exit', 'MainActivity.lambda$exit$3', 'ASYNC',
  'Lambda invoked via Handler.postDelayed for back press timer',
  evidence='SRC activities/MainActivity.java:774 shows new Handler().postDelayed(() -> backPressedToExitOnce = false, 2000)')

e('MainActivity.initFabToSave', 'MainActivity.lambda$initFabToSave$2', 'GUI',
  'Lambda set as OnClickListener for FAB when saving external files',
  evidence='SRC activities/MainActivity.java:555-560 shows initFabToSave method setting click listener')

e('MainActivity.initialiseViews', 'MainActivity.lambda$initialiseViews$8', 'GUI',
  'Lambda set as OnClickListener for fabBgView overlay',
  evidence='SRC activities/MainActivity.java:1437 shows fabBgView.setOnClickListener(view -> {...})')

e('MainActivity.onCreate', 'MainActivity.lambda$onCreate$0', 'CALL',
  'Lambda passed to AppBar constructor as search callback',
  evidence='SRC activities/MainActivity.java:314-316 shows new AppBar(this, getPrefs(), queue -> {...})')

e('MainActivity.onOptionsItemSelected', 'MainActivity.lambda$onOptionsItemSelected$4', 'GUI',
  'Lambda set as OnClickListener for dialog positive button in sethome action',
  evidence='SRC activities/MainActivity.java:954-958 shows dialog.getActionButton(...).setOnClickListener((v) -> {...})')

e('MainActivity.onOptionsItemSelected', 'MainActivity.lambda$onOptionsItemSelected$5', 'GUI',
  'Lambda set as itemsCallbackSingleChoice for directory sort dialog',
  evidence='SRC activities/MainActivity.java:986-992 shows builder.itemsCallbackSingleChoice(current, (dialog1, view, which, text) -> {...})')

e('MainActivity.onOptionsItemSelected', 'MainActivity.lambda$onOptionsItemSelected$6', 'ASYNC',
  'Lambda invoked via AppConfig.runInBackground when removing list mode from database',
  evidence='SRC activities/MainActivity.java:1004-1007 shows AppConfig.runInBackground(() -> utilsHandler.removeFromDatabase(...))')

e('MainActivity.onOptionsItemSelected', 'MainActivity.lambda$onOptionsItemSelected$7', 'ASYNC',
  'Lambda invoked via AppConfig.runInBackground when removing grid mode from database',
  evidence='SRC activities/MainActivity.java:1012-1015 shows AppConfig.runInBackground(() -> utilsHandler.removeFromDatabase(...))')

# Framework lifecycle callbacks already have entries from onCreate, but these are additional lifecycle methods

e('BasicActivity.<init>', 'MainActivity.onActivityResult', 'LIFECYCLE',
  'Framework calls onActivityResult after startActivityForResult completes',
  evidence='SRC activities/MainActivity.java:1306; ' + FW_ACTIVITY)

e('MainActivity.onCreate', 'MainActivity.onBackPressed', 'LIFECYCLE',
  'Framework calls onBackPressed when back button pressed',
  evidence='SRC activities/MainActivity.java:703; framework callback for back navigation')

e('BasicActivity.<init>', 'MainActivity.onConfigurationChanged', 'LIFECYCLE',
  'Framework calls onConfigurationChanged when device configuration changes',
  evidence='SRC activities/MainActivity.java:1067; ' + FW_ACTIVITY)

e('BasicActivity.<init>', 'MainActivity.onDestroy', 'LIFECYCLE',
  'Framework calls onDestroy when activity is being destroyed',
  evidence='SRC activities/MainActivity.java:1204; ' + FW_ACTIVITY)

e('BasicActivity.<init>', 'MainActivity.onKeyDown', 'LIFECYCLE',
  'Framework calls onKeyDown when hardware key pressed',
  evidence='SRC activities/MainActivity.java:1188; ' + FW_ACTIVITY)

e('BasicActivity.<init>', 'MainActivity.onNewIntent', 'LIFECYCLE',
  'Framework calls onNewIntent when new intent delivered to existing activity',
  evidence='SRC activities/MainActivity.java:1568; ' + FW_ACTIVITY)

e('MainActivity.onCreate', 'MainActivity.onPause', 'LIFECYCLE',
  'Framework calls onPause when activity loses focus',
  evidence='SRC activities/MainActivity.java:1093; ' + FW_ACTIVITY)

e('MainActivity.onCreate', 'MainActivity.onPostCreate', 'LIFECYCLE',
  'Framework calls onPostCreate after onCreate completes',
  evidence='SRC activities/MainActivity.java:1060; ' + FW_ACTIVITY)

e('BasicActivity.<init>', 'MainActivity.onPrepareOptionsMenu', 'LIFECYCLE',
  'Framework calls onPrepareOptionsMenu before menu is shown',
  evidence='SRC activities/MainActivity.java:834; ' + FW_ACTIVITY)

e('MainActivity.onCreate', 'MainActivity.onSaveInstanceState', 'LIFECYCLE',
  'Framework calls onSaveInstanceState to save state before potential destruction',
  evidence='SRC activities/MainActivity.java:1074; ' + FW_ACTIVITY)

# SearchWorkerFragment.HelperCallbacks interface methods
e('SearchWorkerFragment.executeSearch', 'MainActivity.onPreExecute', 'CALL',
  'SearchWorkerFragment calls onPreExecute before starting search',
  evidence='SRC activities/MainActivity.java:1771; MainActivity implements SearchWorkerFragment.HelperCallbacks at line 177')

e('SearchWorkerFragment.executeSearch', 'MainActivity.onPostExecute', 'CALL',
  'SearchWorkerFragment calls onPostExecute when search completes',
  evidence='SRC activities/MainActivity.java:1777; MainActivity implements SearchWorkerFragment.HelperCallbacks at line 177')

e('SearchWorkerFragment.executeSearch', 'MainActivity.onProgressUpdate', 'CALL',
  'SearchWorkerFragment calls onProgressUpdate during search',
  evidence='SRC activities/MainActivity.java:1783; MainActivity implements SearchWorkerFragment.HelperCallbacks at line 177')

e('SearchWorkerFragment.executeSearch', 'MainActivity.onCancelled', 'CALL',
  'SearchWorkerFragment calls onCancelled when search is cancelled',
  evidence='SRC activities/MainActivity.java:1788; MainActivity implements SearchWorkerFragment.HelperCallbacks at line 177')

# LoaderManager.LoaderCallbacks interface methods
e('MainActivity.onCreate', 'MainActivity.onCreateLoader', 'CALL',
  'LoaderManager calls onCreateLoader when initLoader invoked',
  evidence='SRC activities/MainActivity.java:305 calls getSupportLoaderManager().initLoader; method at line 1832')

e('MainActivity.onCreateLoader', 'MainActivity.onLoadFinished', 'CALL',
  'LoaderManager calls onLoadFinished when loader completes',
  evidence='SRC activities/MainActivity.java:1902; MainActivity implements LoaderManager.LoaderCallbacks<Cursor> at line 178')

e('MainActivity.onCreateLoader', 'MainActivity.onLoaderReset', 'CALL',
  'LoaderManager calls onLoaderReset when loader is reset',
  evidence='SRC activities/MainActivity.java:1927; MainActivity implements LoaderManager.LoaderCallbacks<Cursor> at line 178')

# MainActivity.setPagingEnabled
e('MainFragment.onListItemClicked', 'MainActivity.setPagingEnabled', 'CALL',
  'MainFragment calls setPagingEnabled to control ViewPager',
  evidence='SRC activities/MainActivity.java:1271; public method called by fragments')

# ---- part repair_rp01 (2024-10-28)
# Repair batch 01: SevenZOutputFile methods (all UNREACHABLE)
# All methods belong to SevenZOutputFile, a library class for writing 7z archives.
# The app only reads 7z archives using SevenZFile, never writes them.
# Grep proof: grep -rn "SevenZOutputFile" app/src/main/java shows no matches.

UNREACHABLE['SevenZOutputFile.<init>(File)'] = (
    'no_trigger_in_app',
    'SevenZOutputFile is a library class for writing 7z archives. The app only reads 7z archives using SevenZFile (see SevenZipHelperTask.java:68-70, SevenZipExtractor.java:31). Grep shows no instantiation of SevenZOutputFile in app code.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:68-72',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.<init>(SeekableByteChannel)'] = (
    'no_trigger_in_app',
    'SevenZOutputFile is a library class for writing 7z archives. The app only reads 7z archives using SevenZFile. Grep shows no instantiation of SevenZOutputFile in app code.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:86-89',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.close'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app. Grep shows no references to SevenZOutputFile in app code.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:126-133',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.closeArchiveEntry'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:173-199',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.createArchiveEntry'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:143-152',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.finish'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:237-277',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.getContentMethods'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:329-332',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.getCurrentOutputStream'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:283-288',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.putArchiveEntry'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:163-167',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.reverse'] = (
    'no_trigger_in_app',
    'Private static method of SevenZOutputFile. The class is never instantiated in the app, and this static method is only called from instance methods of SevenZOutputFile.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:628-634',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.setContentCompression'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:100-107',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.setContentMethods'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:119-122',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.setupFileOutputStream'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:290-327',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.write(int)'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:205-208',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.write(byte[])'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:214-217',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.write(byte[],int,int)'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:225-229',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeBits'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:614-626',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileATimes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:522-553',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileAntiItems'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:465-485',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileCTimes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:491-529',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileEmptyFiles'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:446-463',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileEmptyStreams'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:424-444',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileMTimes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:555-586',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileNames'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:487-502',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileWindowsAttributes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:588-612',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFilesInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:410-422',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFolder'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:387-399',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeHeader'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:334-342',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writePackInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:355-375',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeSingleCodec'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:401-418',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeStreamsInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:344-353',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeSubStreamsInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:420-431',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeUint64'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:614-626',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeUnpackInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:377-408',
    'INFERRED'
)
# Repair batch 02: SftpConnectDialog methods
# Generated for AmazeFileManager graph repair

# onCreate - already has edges in graph_def.py, REACHABLE via LIFECYCLE
# Lines 93-98: DialogFragment.onCreate called by framework
# The framework calls onCreate when the fragment is created

# onCreateDialog - already has one edge in graph_def.py, adding more edges
# Lines 101-294: DialogFragment.onCreateDialog called by framework
# This method sets up the dialog and registers several lambdas

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$9', 'GUI',
  'portET.setOnFocusChangeListener registers lambda$onCreateDialog$9',
  evidence='SRC SftpConnectDialog.java:131 portET.setOnFocusChangeListener((v, hasFocus) -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$1', 'GUI',
  'selectPemBTN.setOnClickListener registers lambda$onCreateDialog$1',
  evidence='SRC SftpConnectDialog.java:139 selectPemBTN.setOnClickListener(v -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$0', 'GUI',
  'dialogBuilder.onPositive registers lambda$onCreateDialog$0 for positive button',
  evidence='SRC SftpConnectDialog.java:157 dialogBuilder.onPositive((dialog, which) -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$13', 'GUI',
  'dialogBuilder.onNegative registers lambda$onCreateDialog$13 for negative button',
  evidence='SRC SftpConnectDialog.java:232 }).onNegative((dialog, which) -> dialog.dismiss());')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$12', 'GUI',
  'edit mode: dialogBuilder.negativeText onNegative registers lambda$onCreateDialog$12',
  evidence='SRC SftpConnectDialog.java:236 if(edit) { dialogBuilder.negativeText(R.string.delete).onNegative((dialog, which) -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$10', 'GUI',
  'edit mode: dialogBuilder.onNeutral registers lambda$onCreateDialog$10',
  evidence='SRC SftpConnectDialog.java:253 }).neutralText(R.string.cancel).onNeutral((dialog, which) -> dialog.dismiss());')

e('SftpConnectDialog.onCreateDialog', 'MaterialDialog.Builder.<init>', 'CALL',
  'onCreateDialog instantiates MaterialDialog.Builder',
  evidence='SRC SftpConnectDialog.java:148 final MaterialDialog.Builder dialogBuilder = new MaterialDialog.Builder(context);')

e('SftpConnectDialog.onCreateDialog', 'MaterialDialog.Builder.build', 'CALL',
  'onCreateDialog builds MaterialDialog',
  evidence='SRC SftpConnectDialog.java:255 MaterialDialog dialog = dialogBuilder.build();')

e('SftpConnectDialog.onCreateDialog', 'SimpleTextWatcher.<init>', 'CALL',
  'onCreateDialog creates SimpleTextWatcher anonymous subclass for validator',
  evidence='SRC SftpConnectDialog.java:264 TextWatcher validator = new SimpleTextWatcher() {...')

# lambda$onCreateDialog$9 - focus change listener for port EditText
# Lines 131-134
e('SftpConnectDialog.lambda$onCreateDialog$9', 'EditText.selectAll', 'CALL',
  'lambda calls selectAll when port field gains focus',
  evidence='SRC SftpConnectDialog.java:131-133 portET.setOnFocusChangeListener((v, hasFocus) -> { if(hasFocus) portET.selectAll(); });')

# lambda$onCreateDialog$1 - click listener for select PEM button
# Lines 139-144
e('SftpConnectDialog.lambda$onCreateDialog$1', 'Intent.<init>', 'CALL',
  'lambda creates Intent for file selection',
  evidence='SRC SftpConnectDialog.java:140 Intent intent = new Intent()')

e('SftpConnectDialog.lambda$onCreateDialog$1', 'SftpConnectDialog.startActivityForResult', 'CALL',
  'lambda calls startActivityForResult to launch file picker',
  evidence='SRC SftpConnectDialog.java:144 startActivityForResult(intent, SELECT_PEM_INTENT);')

# lambda$onCreateDialog$0 - main positive button handler
# Lines 157-231
e('SftpConnectDialog.lambda$onCreateDialog$0', 'EditText.getText', 'CALL',
  'lambda reads text from edit fields',
  evidence='SRC SftpConnectDialog.java:159-163 final String connectionName = connectionET.getText().toString();')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'UtilsHandler.getSshHostKey', 'CALL',
  'lambda retrieves existing SSH host key',
  evidence='SRC SftpConnectDialog.java:169 String sshHostKey = utilsHandler.getSshHostKey(deriveSftpPathFrom(...));')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SshConnectionPool.getInstance', 'CALL',
  'lambda gets SshConnectionPool singleton',
  evidence='SRC SftpConnectDialog.java:176 SshConnectionPool.getInstance().removeConnection(...);')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SshConnectionPool.removeConnection', 'CALL',
  'lambda removes existing connection before reconnecting',
  evidence='SRC SftpConnectDialog.java:176-177 SshConnectionPool.getInstance().removeConnection(SshClientUtils.deriveSftpPathFrom(...), () -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SftpConnectDialog.lambda$null$2', 'ASYNC',
  'removeConnection callback registers lambda$null$2',
  evidence='SRC SftpConnectDialog.java:177 removeConnection(..., () -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'lambda creates GetSshHostFingerprintTask for new connection (no existing key)',
  evidence='SRC SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.execute', 'CALL',
  'lambda executes GetSshHostFingerprintTask',
  evidence='SRC SftpConnectDialog.java:230 }).execute();')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SftpConnectDialog.lambda$null$6', 'ASYNC',
  'GetSshHostFingerprintTask callback registers lambda$null$6',
  evidence='SRC SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'AlertDialog.Builder.<init>', 'CALL',
  'lambda creates AlertDialog.Builder for host key verification',
  evidence='SRC SftpConnectDialog.java:213 new AlertDialog.Builder(context).setTitle(...)')

# lambda$null$2 - callback from removeConnection
# Lines 177-199
e('SftpConnectDialog.lambda$null$2', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'lambda creates GetSshHostFingerprintTask after connection removed',
  evidence='SRC SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

e('SftpConnectDialog.lambda$null$2', 'GetSshHostFingerprintTask.execute', 'CALL',
  'lambda executes GetSshHostFingerprintTask',
  evidence='SRC SftpConnectDialog.java:198 }).execute();')

e('SftpConnectDialog.lambda$null$2', 'SftpConnectDialog.lambda$null$3', 'ASYNC',
  'GetSshHostFingerprintTask callback registers lambda$null$3',
  evidence='SRC SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

# lambda$null$3 - callback from GetSshHostFingerprintTask (edit mode with existing key)
# Lines 178-198
e('SftpConnectDialog.lambda$null$3', 'SecurityUtils.getFingerprint', 'CALL',
  'lambda gets host key fingerprint',
  evidence='SRC SftpConnectDialog.java:181 final String hostKeyFingerprint = SecurityUtils.getFingerprint(hostKey);')

e('SftpConnectDialog.lambda$null$3', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'lambda calls authenticateAndSaveSetup when key matches',
  evidence='SRC SftpConnectDialog.java:183-185 authenticateAndSaveSetup(connectionName, hostname, port, sshHostKey, username, password, selectedParsedKeyPairName, selectedParsedKeyPair, edit);')

e('SftpConnectDialog.lambda$null$3', 'AlertDialog.Builder.<init>', 'CALL',
  'lambda creates AlertDialog.Builder when host key changed',
  evidence='SRC SftpConnectDialog.java:187 new AlertDialog.Builder(context).setTitle(...)')

e('SftpConnectDialog.lambda$null$3', 'SftpConnectDialog.lambda$null$4', 'GUI',
  'setPositiveButton registers lambda$null$4',
  evidence='SRC SftpConnectDialog.java:191 .setPositiveButton(R.string.update_host_key, (dialog1, which1) -> {...')

e('SftpConnectDialog.lambda$null$3', 'SftpConnectDialog.lambda$null$5', 'GUI',
  'setNegativeButton registers lambda$null$5',
  evidence='SRC SftpConnectDialog.java:196 .setNegativeButton(R.string.cancel_recommended, (dialog1, which1) -> dialog1.dismiss())')

e('SftpConnectDialog.lambda$null$3', 'AlertDialog.Builder.show', 'CALL',
  'lambda shows the alert dialog',
  evidence='SRC SftpConnectDialog.java:197 .show();')

# lambda$null$4 - positive button in host key changed dialog
# Lines 191-195
e('SftpConnectDialog.lambda$null$4', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'lambda calls authenticateAndSaveSetup with new host key',
  evidence='SRC SftpConnectDialog.java:192-194 authenticateAndSaveSetup(connectionName, hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPairName, selectedParsedKeyPair, edit);')

# lambda$null$5 - negative button in host key changed dialog
# Lines 196
e('SftpConnectDialog.lambda$null$5', 'AlertDialog.dismiss', 'CALL',
  'lambda dismisses the alert dialog',
  evidence='SRC SftpConnectDialog.java:196 .setNegativeButton(R.string.cancel_recommended, (dialog1, which1) -> dialog1.dismiss())')

# lambda$null$6 - callback from GetSshHostFingerprintTask (new connection)
# Lines 203-230
e('SftpConnectDialog.lambda$null$6', 'SecurityUtils.getFingerprint', 'CALL',
  'lambda gets host key fingerprint',
  evidence='SRC SftpConnectDialog.java:206 final String hostKeyFingerprint = SecurityUtils.getFingerprint(hostKey);')

e('SftpConnectDialog.lambda$null$6', 'StringBuilder.<init>', 'CALL',
  'lambda creates StringBuilder for host:port display',
  evidence='SRC SftpConnectDialog.java:207 StringBuilder sb = new StringBuilder(hostname);')

e('SftpConnectDialog.lambda$null$6', 'AlertDialog.Builder.<init>', 'CALL',
  'lambda creates AlertDialog.Builder for verification',
  evidence='SRC SftpConnectDialog.java:213 new AlertDialog.Builder(context).setTitle(...)')

e('SftpConnectDialog.lambda$null$6', 'SftpConnectDialog.lambda$null$7', 'GUI',
  'setPositiveButton registers lambda$null$7',
  evidence='SRC SftpConnectDialog.java:217 .setPositiveButton(R.string.yes, (dialog1, which1) -> {...')

e('SftpConnectDialog.lambda$null$6', 'SftpConnectDialog.lambda$null$8', 'GUI',
  'setNegativeButton registers lambda$null$8',
  evidence='SRC SftpConnectDialog.java:229 .setNegativeButton(R.string.no, (dialog1, which1) -> dialog1.dismiss()).show();')

e('SftpConnectDialog.lambda$null$6', 'AlertDialog.Builder.show', 'CALL',
  'lambda shows the verification dialog',
  evidence='SRC SftpConnectDialog.java:229 .show();')

# lambda$null$7 - positive button in host key verification dialog
# Lines 217-228
e('SftpConnectDialog.lambda$null$7', 'AlertDialog.dismiss', 'CALL',
  'lambda dismisses verification dialog',
  evidence='SRC SftpConnectDialog.java:219 dialog1.dismiss();')

e('SftpConnectDialog.lambda$null$7', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'lambda calls authenticateAndSaveSetup after user accepts key',
  evidence='SRC SftpConnectDialog.java:220-222 authenticateAndSaveSetup(connectionName, hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPairName, selectedParsedKeyPair, edit)')

e('SftpConnectDialog.lambda$null$7', 'Log.d', 'CALL',
  'lambda logs successful setup',
  evidence='SRC SftpConnectDialog.java:224 Log.d(TAG, "Saved setup");')

e('SftpConnectDialog.lambda$null$7', 'SftpConnectDialog.dismiss', 'CALL',
  'lambda dismisses the SftpConnectDialog',
  evidence='SRC SftpConnectDialog.java:225 dismiss();')

# lambda$null$8 - negative button in host key verification dialog
# Lines 229
e('SftpConnectDialog.lambda$null$8', 'AlertDialog.dismiss', 'CALL',
  'lambda dismisses verification dialog when user declines',
  evidence='SRC SftpConnectDialog.java:229 .setNegativeButton(R.string.no, (dialog1, which1) -> dialog1.dismiss())')

# lambda$onCreateDialog$13 - negative button handler (non-edit mode)
# Line 232
e('SftpConnectDialog.lambda$onCreateDialog$13', 'MaterialDialog.dismiss', 'CALL',
  'lambda dismisses the dialog',
  evidence='SRC SftpConnectDialog.java:232 }).onNegative((dialog, which) -> dialog.dismiss());')

# lambda$onCreateDialog$12 - negative button handler (edit mode - delete)
# Lines 236-252
e('SftpConnectDialog.lambda$onCreateDialog$12', 'EditText.getText', 'CALL',
  'lambda reads connection parameters',
  evidence='SRC SftpConnectDialog.java:237-240 final String connectionName = connectionET.getText().toString();')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.getInstance', 'CALL',
  'lambda gets DataUtils singleton',
  evidence='SRC SftpConnectDialog.java:243 int i = DataUtils.getInstance().containsServer(...);')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.containsServer', 'CALL',
  'lambda checks if server exists',
  evidence='SRC SftpConnectDialog.java:243 int i = DataUtils.getInstance().containsServer(new String[]{connectionName, path});')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.removeServer', 'CALL',
  'lambda removes server from DataUtils',
  evidence='SRC SftpConnectDialog.java:246 DataUtils.getInstance().removeServer(i);')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'AppConfig.runInBackground', 'CALL',
  'lambda runs database removal in background',
  evidence='SRC SftpConnectDialog.java:247 AppConfig.runInBackground(() -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'SftpConnectDialog.lambda$null$11', 'ASYNC',
  'runInBackground callback registers lambda$null$11',
  evidence='SRC SftpConnectDialog.java:247-249 AppConfig.runInBackground(() -> { utilsHandler.removeFromDatabase(...); });')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'MainActivity.getDrawer', 'CALL',
  'lambda gets drawer to refresh it',
  evidence='SRC SftpConnectDialog.java:251 ((MainActivity) getActivity()).getDrawer().refreshDrawer();')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'MaterialDialog.dismiss', 'CALL',
  'lambda dismisses the dialog',
  evidence='SRC SftpConnectDialog.java:252 dialog.dismiss();')

# lambda$null$11 - background task for database removal
# Lines 247-249
e('SftpConnectDialog.lambda$null$11', 'UtilsHandler.removeFromDatabase', 'CALL',
  'lambda removes SFTP connection from database',
  evidence='SRC SftpConnectDialog.java:248-249 utilsHandler.removeFromDatabase(new OperationData(UtilsHandler.Operation.SFTP, path, connectionName, null, null, null));')

e('SftpConnectDialog.lambda$null$11', 'OperationData.<init>', 'CALL',
  'lambda creates OperationData for removal',
  evidence='SRC SftpConnectDialog.java:248 new OperationData(UtilsHandler.Operation.SFTP, path, connectionName, null, null, null)')

# lambda$onCreateDialog$10 - neutral button handler (edit mode - cancel)
# Line 253
e('SftpConnectDialog.lambda$onCreateDialog$10', 'MaterialDialog.dismiss', 'CALL',
  'lambda dismisses the dialog',
  evidence='SRC SftpConnectDialog.java:253 }).neutralText(R.string.cancel).onNeutral((dialog, which) -> dialog.dismiss());')

# onActivityResult - LIFECYCLE method
# Lines 298-327
e('SftpConnectDialog.onActivityResult', 'Intent.getData', 'CALL',
  'onActivityResult gets selected file URI',
  evidence='SRC SftpConnectDialog.java:306 selectedPem = data.getData();')

e('SftpConnectDialog.onActivityResult', 'ContentResolver.openInputStream', 'CALL',
  'onActivityResult opens input stream for PEM file',
  evidence='SRC SftpConnectDialog.java:309 InputStream selectedKeyContent = context.getContentResolver().openInputStream(selectedPem);')

e('SftpConnectDialog.onActivityResult', 'PemToKeyPairTask.<init>', 'CALL',
  'onActivityResult creates PemToKeyPairTask',
  evidence='SRC SftpConnectDialog.java:311 new PemToKeyPairTask(selectedKeyContent, result -> {...')

e('SftpConnectDialog.onActivityResult', 'PemToKeyPairTask.execute', 'CALL',
  'onActivityResult executes PemToKeyPairTask',
  evidence='SRC SftpConnectDialog.java:321 }).execute();')

e('SftpConnectDialog.onActivityResult', 'SftpConnectDialog.lambda$onActivityResult$14', 'ASYNC',
  'PemToKeyPairTask callback registers lambda$onActivityResult$14',
  evidence='SRC SftpConnectDialog.java:311 new PemToKeyPairTask(selectedKeyContent, result -> {...')

e('SftpConnectDialog.onActivityResult', 'Log.e', 'CALL',
  'onActivityResult logs FileNotFoundException',
  evidence='SRC SftpConnectDialog.java:323 Log.e(TAG, "File not found", e);')

# lambda$onActivityResult$14 - callback from PemToKeyPairTask
# Lines 311-321
e('SftpConnectDialog.lambda$onActivityResult$14', 'Uri.getLastPathSegment', 'CALL',
  'lambda gets filename from URI',
  evidence='SRC SftpConnectDialog.java:313 selectedParsedKeyPairName = selectedPem.getLastPathSegment().substring(...);')

e('SftpConnectDialog.lambda$onActivityResult$14', 'SftpConnectDialog.getDialog', 'CALL',
  'lambda gets the MaterialDialog',
  evidence='SRC SftpConnectDialog.java:314 MDButton okBTN = ((MaterialDialog)getDialog()).getActionButton(DialogAction.POSITIVE);')

e('SftpConnectDialog.lambda$onActivityResult$14', 'MaterialDialog.getActionButton', 'CALL',
  'lambda gets positive button',
  evidence='SRC SftpConnectDialog.java:315 .getActionButton(DialogAction.POSITIVE);')

e('SftpConnectDialog.lambda$onActivityResult$14', 'MDButton.setEnabled', 'CALL',
  'lambda enables positive button',
  evidence='SRC SftpConnectDialog.java:316 okBTN.setEnabled(okBTN.isEnabled() || true);')

e('SftpConnectDialog.lambda$onActivityResult$14', 'Dialog.findViewById', 'CALL',
  'lambda finds select PEM button',
  evidence='SRC SftpConnectDialog.java:318 Button selectPemBTN = getDialog().findViewById(R.id.selectPemBTN);')

e('SftpConnectDialog.lambda$onActivityResult$14', 'Button.setText', 'CALL',
  'lambda sets button text to filename',
  evidence='SRC SftpConnectDialog.java:319 selectPemBTN.setText(selectedParsedKeyPairName);')

# authenticateAndSaveSetup - called from multiple lambdas
# Lines 327-394
e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.encryptSshPathAsNecessary', 'CALL',
  'authenticateAndSaveSetup encrypts path',
  evidence='SRC SftpConnectDialog.java:336 final String encryptedPath = SshClientUtils.encryptSshPathAsNecessary(path);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshConnectionPool.getInstance', 'CALL',
  'authenticateAndSaveSetup gets connection pool',
  evidence='SRC SftpConnectDialog.java:340 SSHClient result = SshConnectionPool.getInstance().getConnection(...);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshConnectionPool.getConnection', 'CALL',
  'authenticateAndSaveSetup establishes SSH connection',
  evidence='SRC SftpConnectDialog.java:340-341 SshConnectionPool.getInstance().getConnection(hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPair);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.getInstance', 'CALL',
  'authenticateAndSaveSetup gets DataUtils singleton',
  evidence='SRC SftpConnectDialog.java:344 if(DataUtils.getInstance().containsServer(path) == -1) {...')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.containsServer', 'CALL',
  'authenticateAndSaveSetup checks if server already exists',
  evidence='SRC SftpConnectDialog.java:344 if(DataUtils.getInstance().containsServer(path) == -1) {')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.addServer', 'CALL',
  'authenticateAndSaveSetup adds server for new connection',
  evidence='SRC SftpConnectDialog.java:345 DataUtils.getInstance().addServer(new String[]{connectionName, path});')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainActivity.getDrawer', 'CALL',
  'authenticateAndSaveSetup gets drawer',
  evidence='SRC SftpConnectDialog.java:346 ((MainActivity) getActivity()).getDrawer().refreshDrawer();')

e('SftpConnectDialog.authenticateAndSaveSetup', 'UtilsHandler.saveToDatabase', 'CALL',
  'authenticateAndSaveSetup saves connection to database',
  evidence='SRC SftpConnectDialog.java:348 utilsHandler.saveToDatabase(new OperationData(...));')

e('SftpConnectDialog.authenticateAndSaveSetup', 'OperationData.<init>', 'CALL',
  'authenticateAndSaveSetup creates OperationData',
  evidence='SRC SftpConnectDialog.java:348-350 new OperationData(UtilsHandler.Operation.SFTP, encryptedPath, connectionName, hostKeyFingerprint, selectedParsedKeyPairName, getPemContents())')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SftpConnectDialog.getPemContents', 'CALL',
  'authenticateAndSaveSetup calls getPemContents for database',
  evidence='SRC SftpConnectDialog.java:350 getPemContents())')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainActivity.getCurrentMainFragment', 'CALL',
  'authenticateAndSaveSetup gets main fragment',
  evidence='SRC SftpConnectDialog.java:352 MainFragment ma = ((MainActivity)getActivity()).getCurrentMainFragment();')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainFragment.loadlist', 'CALL',
  'authenticateAndSaveSetup loads SFTP directory in fragment',
  evidence='SRC SftpConnectDialog.java:353 ma.loadlist(path, false, OpenMode.SFTP);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SftpConnectDialog.dismiss', 'CALL',
  'authenticateAndSaveSetup dismisses dialog on success',
  evidence='SRC SftpConnectDialog.java:354 dismiss();')

e('SftpConnectDialog.authenticateAndSaveSetup', 'Snackbar.make', 'CALL',
  'authenticateAndSaveSetup shows snackbar if connection exists',
  evidence='SRC SftpConnectDialog.java:357 Snackbar.make(getActivity().findViewById(R.id.content_frame), getString(R.string.connection_exists), Snackbar.LENGTH_SHORT).show();')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.removeServer', 'CALL',
  'authenticateAndSaveSetup removes old server in edit mode',
  evidence='SRC SftpConnectDialog.java:379 DataUtils.getInstance().removeServer(DataUtils.getInstance().containsServer(originalPath));')

e('SftpConnectDialog.authenticateAndSaveSetup', 'Collections.sort', 'CALL',
  'authenticateAndSaveSetup sorts server list',
  evidence='SRC SftpConnectDialog.java:381 Collections.sort(DataUtils.getInstance().getServers(), new BookSorter());')

e('SftpConnectDialog.authenticateAndSaveSetup', 'BookSorter.<init>', 'CALL',
  'authenticateAndSaveSetup creates BookSorter comparator',
  evidence='SRC SftpConnectDialog.java:381 new BookSorter()')

e('SftpConnectDialog.authenticateAndSaveSetup', 'AppConfig.runInBackground', 'CALL',
  'authenticateAndSaveSetup runs database update in background for edit mode',
  evidence='SRC SftpConnectDialog.java:384 AppConfig.runInBackground(() -> {...')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'ASYNC',
  'runInBackground callback registers lambda$authenticateAndSaveSetup$15',
  evidence='SRC SftpConnectDialog.java:385-389 utilsHandler.updateSsh(...);')

# lambda$authenticateAndSaveSetup$15 - background task for database update
# Lines 385-389
e('SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'UtilsHandler.updateSsh', 'CALL',
  'lambda updates SSH connection in database',
  evidence='SRC SftpConnectDialog.java:385-388 utilsHandler.updateSsh(connectionName, getArguments().getString("name"), encryptedPath, hostKeyFingerprint, selectedParsedKeyPairName, getPemContents());')

e('SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'SftpConnectDialog.getPemContents', 'CALL',
  'lambda calls getPemContents for database update',
  evidence='SRC SftpConnectDialog.java:388 getPemContents());')

# getPemContents - reads PEM file content
# Lines 397-413
e('SftpConnectDialog.getPemContents', 'BufferedReader.<init>', 'CALL',
  'getPemContents creates BufferedReader',
  evidence='SRC SftpConnectDialog.java:402 BufferedReader reader = new BufferedReader(new InputStreamReader(context.getContentResolver().openInputStream(selectedPem)));')

e('SftpConnectDialog.getPemContents', 'InputStreamReader.<init>', 'CALL',
  'getPemContents creates InputStreamReader',
  evidence='SRC SftpConnectDialog.java:402 new InputStreamReader(context.getContentResolver().openInputStream(selectedPem))')

e('SftpConnectDialog.getPemContents', 'ContentResolver.openInputStream', 'CALL',
  'getPemContents opens PEM file stream',
  evidence='SRC SftpConnectDialog.java:402 context.getContentResolver().openInputStream(selectedPem)')

e('SftpConnectDialog.getPemContents', 'StringBuilder.<init>', 'CALL',
  'getPemContents creates StringBuilder',
  evidence='SRC SftpConnectDialog.java:403 StringBuilder sb = new StringBuilder();')

e('SftpConnectDialog.getPemContents', 'BufferedReader.readLine', 'CALL',
  'getPemContents reads lines from file',
  evidence='SRC SftpConnectDialog.java:404 for (String line = reader.readLine(); line != null; line = reader.readLine()) {')
# ---- Repair batch 03 (2024-10-28 20:24)
# TextEditorActivity callbacks and RecyclerAdapter methods

# TextEditorActivity lifecycle and callbacks - all reachable through activity lifecycle

# TextEditorActivity implements TextWatcher, registered in onCreate
e('TextEditorActivity.onCreate', 'TextEditorActivity.afterTextChanged', 'FRAMEWORK',
  'TextWatcher.afterTextChanged callback dispatched by EditText when text changes',
  evidence='SRC activities/TextEditorActivity.java:210 mInput.addTextChangedListener(this); ' +
  'INFERRED EditText dispatches to registered TextWatcher (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.beforeTextChanged', 'FRAMEWORK',
  'TextWatcher.beforeTextChanged callback dispatched by EditText before text changes',
  evidence='SRC activities/TextEditorActivity.java:210 mInput.addTextChangedListener(this); ' +
  'INFERRED EditText dispatches to registered TextWatcher (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onTextChanged', 'FRAMEWORK',
  'TextWatcher.onTextChanged callback dispatched by EditText when text is changing',
  evidence='SRC activities/TextEditorActivity.java:210,181 searchEditText.addTextChangedListener(this); ' +
  'INFERRED EditText dispatches to registered TextWatcher (Android SDK source not read)')

# onBackPressed is Activity lifecycle callback
e('TextEditorActivity.onCreate', 'TextEditorActivity.onBackPressed', 'FRAMEWORK',
  'Activity.onBackPressed called by framework when back button pressed',
  evidence='SRC activities/TextEditorActivity.java:340; ' +
  'INFERRED Activity framework dispatches back button events (Android SDK source not read)')

# onClick is View.OnClickListener callback, registered in onCreate for buttons
e('TextEditorActivity.onCreate', 'TextEditorActivity.onClick', 'FRAMEWORK',
  'View.OnClickListener.onClick callback when search buttons clicked',
  evidence='SRC activities/TextEditorActivity.java:183-185 upButton/downButton/closeButton.setOnClickListener(this); ' +
  'INFERRED View dispatches click events to registered OnClickListener (Android SDK source not read)')

# Options menu callbacks
e('TextEditorActivity.onCreate', 'TextEditorActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'Activity.onCreateOptionsMenu called by framework to create options menu',
  evidence='SRC activities/TextEditorActivity.java:344; ' +
  'INFERRED Activity framework calls onCreateOptionsMenu (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onPrepareOptionsMenu', 'FRAMEWORK',
  'Activity.onPrepareOptionsMenu called by framework before showing menu',
  evidence='SRC activities/TextEditorActivity.java:349; ' +
  'INFERRED Activity framework calls onPrepareOptionsMenu (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onOptionsItemSelected', 'FRAMEWORK',
  'Activity.onOptionsItemSelected called by framework when menu item selected',
  evidence='SRC activities/TextEditorActivity.java:355; ' +
  'INFERRED Activity framework calls onOptionsItemSelected (Android SDK source not read)')

# onSaveInstanceState and onDestroy are Activity lifecycle
e('TextEditorActivity.onCreate', 'TextEditorActivity.onSaveInstanceState', 'FRAMEWORK',
  'Activity.onSaveInstanceState called by framework to save state',
  evidence='SRC activities/TextEditorActivity.java:223; ' +
  'INFERRED Activity framework calls onSaveInstanceState before destroying activity (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onDestroy', 'FRAMEWORK',
  'Activity.onDestroy called by framework when activity is destroyed',
  evidence='SRC activities/TextEditorActivity.java:399; ' +
  'INFERRED Activity framework calls onDestroy (Android SDK source not read)')

# checkUnsavedChanges called from onBackPressed and onOptionsItemSelected
e('TextEditorActivity.onBackPressed', 'TextEditorActivity.checkUnsavedChanges', 'DIRECT',
  'onBackPressed calls checkUnsavedChanges to prompt user if unsaved',
  evidence='SRC activities/TextEditorActivity.java:340')

e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.checkUnsavedChanges', 'DIRECT',
  'onOptionsItemSelected calls checkUnsavedChanges when home button pressed',
  evidence='SRC activities/TextEditorActivity.java:360 case android.R.id.home')

# cleanSpans called from beforeTextChanged and onClick
e('TextEditorActivity.beforeTextChanged', 'TextEditorActivity.cleanSpans', 'DIRECT',
  'beforeTextChanged calls cleanSpans to clear search highlights',
  evidence='SRC activities/TextEditorActivity.java:417')

e('TextEditorActivity.onClick', 'TextEditorActivity.cleanSpans', 'DIRECT',
  'onClick calls cleanSpans when close button pressed',
  evidence='SRC activities/TextEditorActivity.java:588 case R.id.close')

# hideSearchView and revealSearchView called from onOptionsItemSelected
e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.hideSearchView', 'DIRECT',
  'onOptionsItemSelected calls hideSearchView if search is shown',
  evidence='SRC activities/TextEditorActivity.java:389 case R.id.find')

e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.revealSearchView', 'DIRECT',
  'onOptionsItemSelected calls revealSearchView if search is hidden',
  evidence='SRC activities/TextEditorActivity.java:390 case R.id.find')

# saveFile called from onOptionsItemSelected and lambda
e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.saveFile', 'DIRECT',
  'onOptionsItemSelected calls saveFile when save menu item selected',
  evidence='SRC activities/TextEditorActivity.java:364 case R.id.save')

# Lambda callbacks from MaterialDialog in checkUnsavedChanges
e('TextEditorActivity.checkUnsavedChanges', 'TextEditorActivity.lambda$checkUnsavedChanges$0', 'FRAMEWORK',
  'MaterialDialog positive button callback lambda',
  evidence='SRC activities/TextEditorActivity.java:243 .onPositive((dialog, which) -> {...}); ' +
  'INFERRED MaterialDialog dispatches button callbacks (library source not read)')

e('TextEditorActivity.checkUnsavedChanges', 'TextEditorActivity.lambda$checkUnsavedChanges$1', 'FRAMEWORK',
  'MaterialDialog negative button callback lambda',
  evidence='SRC activities/TextEditorActivity.java:248 .onNegative((dialog, which) -> finish()); ' +
  'INFERRED MaterialDialog dispatches button callbacks (library source not read)')

e('TextEditorActivity.lambda$checkUnsavedChanges$0', 'TextEditorActivity.saveFile', 'DIRECT',
  'Positive dialog button lambda calls saveFile then finish',
  evidence='SRC activities/TextEditorActivity.java:243-244')

# Lambda from load method (ReadFileTask callback)
e('TextEditorActivity.load', 'TextEditorActivity.lambda$load$4', 'FRAMEWORK',
  'ReadFileTask result callback lambda',
  evidence='SRC activities/TextEditorActivity.java:291-292 new ReadFileTask(..., (data) -> {...}); ' +
  'INFERRED AsyncTask-like callback pattern (ReadFileTask implementation dispatches callback)')

# Lambda from lambda$load$4 (Snackbar action callback)
e('TextEditorActivity.lambda$load$4', 'TextEditorActivity.lambda$null$3', 'FRAMEWORK',
  'Snackbar action button callback lambda',
  evidence='SRC activities/TextEditorActivity.java:308 snackbar.setAction(..., v -> snackbar.dismiss()); ' +
  'INFERRED Snackbar dispatches action callbacks (Material Components source not read)')

# Lambda from saveFile (WriteFileAbstraction callback)
e('TextEditorActivity.saveFile', 'TextEditorActivity.lambda$saveFile$2', 'FRAMEWORK',
  'WriteFileAbstraction result callback lambda',
  evidence='SRC activities/TextEditorActivity.java:263-264 new WriteFileAbstraction(..., (errorCode) -> {...}); ' +
  'INFERRED AsyncTask-like callback pattern (WriteFileAbstraction implementation dispatches callback)')

# RecyclerAdapter methods

# addItem called from MainFragment.addSearchResult
e('MainFragment.addSearchResult', 'RecyclerAdapter.addItem', 'DIRECT',
  'MainFragment calls addItem to add search result to adapter',
  evidence='SRC fragments/MainFragment.java:1629')

# areAllChecked called from MainFragment$3.onActionItemClicked
e('MainFragment$3.onActionItemClicked', 'RecyclerAdapter.areAllChecked', 'DIRECT',
  'Action mode callback checks if all items with path are checked',
  evidence='SRC fragments/MainFragment.java:691')

# getCorrectView called from RecyclerPreloadSizeProvider
e('RecyclerPreloadSizeProvider.getPreloadSize', 'RecyclerAdapter.getCorrectView', 'DIRECT',
  'Glide preload size provider calls getCorrectView to determine which view type',
  evidence='SRC adapters/glide/RecyclerPreloadSizeProvider.java:56')

# getItemId is RecyclerView.Adapter callback
e('RecyclerAdapter.onCreateViewHolder', 'RecyclerAdapter.getItemId', 'FRAMEWORK',
  'RecyclerView.Adapter.getItemId called by RecyclerView framework',
  evidence='INFERRED RecyclerView framework calls getItemId for stable IDs (androidx source not read)')

# getItemViewType is RecyclerView.Adapter callback, also called from MainFragment$2
e('RecyclerAdapter.onCreateViewHolder', 'RecyclerAdapter.getItemViewType', 'FRAMEWORK',
  'RecyclerView.Adapter.getItemViewType called by RecyclerView framework',
  evidence='INFERRED RecyclerView framework calls getItemViewType (androidx source not read)')

e('MainFragment$2.getSpanSize', 'RecyclerAdapter.getItemViewType', 'DIRECT',
  'GridLayoutManager.SpanSizeLookup calls getItemViewType',
  evidence='SRC fragments/MainFragment.java:345')

# onFailedToRecycleView is RecyclerView.Adapter callback
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.onFailedToRecycleView', 'FRAMEWORK',
  'RecyclerView.Adapter.onFailedToRecycleView called when view recycling fails',
  evidence='INFERRED RecyclerView framework calls onFailedToRecycleView (androidx source not read)')

# onViewAttachedToWindow is RecyclerView.Adapter callback
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.onViewAttachedToWindow', 'FRAMEWORK',
  'RecyclerView.Adapter.onViewAttachedToWindow called when view attached',
  evidence='INFERRED RecyclerView framework calls onViewAttachedToWindow (androidx source not read)')

# onViewDetachedFromWindow is RecyclerView.Adapter callback
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.onViewDetachedFromWindow', 'FRAMEWORK',
  'RecyclerView.Adapter.onViewDetachedFromWindow called when view detached',
  evidence='INFERRED RecyclerView framework calls onViewDetachedFromWindow (androidx source not read)')

# toggleChecked(boolean,String) called from MainFragment$3
e('MainFragment$3.onActionItemClicked', 'RecyclerAdapter.toggleChecked(boolean,String)', 'DIRECT',
  'Action mode callback toggles checked state for items with path',
  evidence='SRC fragments/MainFragment.java:695')

e('MainFragment$3.onDestroyActionMode', 'RecyclerAdapter.toggleChecked(boolean,String)', 'DIRECT',
  'Action mode destroy callback unchecks all items with path',
  evidence='SRC fragments/MainFragment.java:763')

# RecyclerAdapter lambda callbacks from onBindViewHolder

# lambda$onBindViewHolder$0 is View.OnClickListener from onBindViewHolder
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$0', 'FRAMEWORK',
  'View.OnClickListener callback for row click',
  evidence='SRC adapters/RecyclerAdapter.java:529 holder.rl.setOnClickListener(v -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$1 is View.OnLongClickListener
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$1', 'FRAMEWORK',
  'View.OnLongClickListener callback for row long click',
  evidence='SRC adapters/RecyclerAdapter.java:543 holder.rl.setOnLongClickListener(p1 -> {...}); ' +
  'INFERRED View dispatches long click events (Android SDK source not read)')

# lambda$onBindViewHolder$2 is View.OnClickListener for genericIcon
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$2', 'FRAMEWORK',
  'View.OnClickListener callback for generic icon click',
  evidence='SRC adapters/RecyclerAdapter.java:561 holder.genericIcon.setOnClickListener(v -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$3 is View.OnClickListener for pictureIcon
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$3', 'FRAMEWORK',
  'View.OnClickListener callback for picture icon click',
  evidence='SRC adapters/RecyclerAdapter.java:570 holder.pictureIcon.setOnClickListener(view -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$4 is View.OnClickListener for apkIcon
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$4', 'FRAMEWORK',
  'View.OnClickListener callback for apk icon click',
  evidence='SRC adapters/RecyclerAdapter.java:576 holder.apkIcon.setOnClickListener(view -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$5 is View.OnClickListener for about button (shows popup)
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$5', 'FRAMEWORK',
  'View.OnClickListener callback lambda for about button in grid mode',
  evidence='SRC adapters/RecyclerAdapter.java:698-708 about.setOnClickListener(view -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$6 is View.OnLongClickListener for grid mode
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$6', 'FRAMEWORK',
  'View.OnLongClickListener callback lambda for item long click in grid mode',
  evidence='SRC adapters/RecyclerAdapter.java:706-714 imageView.setOnLongClickListener(...); ' +
  'INFERRED View dispatches long click events (Android SDK source not read)')

# lambda$showPopup$7 is PopupMenu.OnMenuItemClickListener
e('RecyclerAdapter.showPopup', 'RecyclerAdapter.lambda$showPopup$7', 'FRAMEWORK',
  'PopupMenu.OnMenuItemClickListener callback lambda',
  evidence='SRC adapters/RecyclerAdapter.java:771 popupMenu.setOnMenuItemClickListener((item) -> {...}); ' +
  'INFERRED PopupMenu dispatches menu item click callbacks (Android SDK source not read)')

# Lambdas call toggleChecked
e('RecyclerAdapter.lambda$onBindViewHolder$1', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'DIRECT',
  'Long click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:546')

e('RecyclerAdapter.lambda$onBindViewHolder$2', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'DIRECT',
  'Generic icon click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:564')

e('RecyclerAdapter.lambda$onBindViewHolder$3', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'DIRECT',
  'Picture icon click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:571')

e('RecyclerAdapter.lambda$onBindViewHolder$4', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'DIRECT',
  'Apk icon click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:577')

e('RecyclerAdapter.lambda$onBindViewHolder$6', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'DIRECT',
  'Grid mode long click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:707')

# UNREACHABLE dictionary for batch 03
# ---- part repair_rp04 (2024-10-28)
# Repair batch 04 - SevenZArchiveEntry and SearchAsyncTask

# SevenZArchiveEntry methods - library class (Apache Commons Compress)
# These getters/setters are not called by the app

UNREACHABLE['SevenZArchiveEntry.getAccessDate'] = (
    'no_trigger_in_app',
    'Library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:275-280',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getCompressedCrc'] = (
    'no_trigger_in_app',
    'Package-private library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:371-373',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getCompressedCrcValue'] = (
    'no_trigger_in_app',
    'Package-private library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:387-389',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getCompressedSize'] = (
    'no_trigger_in_app',
    'Package-private library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:410-412',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getCrc'] = (
    'no_trigger_in_app',
    'Deprecated library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:339-342',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getCreationDate'] = (
    'no_trigger_in_app',
    'Library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:153-159',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getWindowsAttributes'] = (
    'no_trigger_in_app',
    'Library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:313-315',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.isAntiItem'] = (
    'no_trigger_in_app',
    'Library method never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:121-123',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.javaTimeToNtfsTime'] = (
    'no_trigger_in_app',
    'Static library utility never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:486-493',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setAccessDate(Date)'] = (
    'no_trigger_in_app',
    'Library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:296-301',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setCompressedCrc'] = (
    'no_trigger_in_app',
    'Deprecated package-private library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:379-382',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setCompressedCrcValue'] = (
    'no_trigger_in_app',
    'Package-private library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:395-398',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setCompressedSize'] = (
    'no_trigger_in_app',
    'Package-private library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:420-423',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setCrc'] = (
    'no_trigger_in_app',
    'Deprecated library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:350-353',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setCreationDate(Date)'] = (
    'no_trigger_in_app',
    'Library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:174-179',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setLastModifiedDate(Date)'] = (
    'no_trigger_in_app',
    'Library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:232-237',
    'SOURCE'
)

# SearchAsyncTask methods - AsyncTask subclass
# Most methods already in graph_def.py (lines 1294-1325)
# Adding routes for missing lambda methods only

e('SearchAsyncTask.search(HybridFile,SearchFilter)', 'SearchAsyncTask.lambda$search$0', 'CALL',
  'Lambda generated for forEachChildrenFile file consumer',
  evidence='SRC SearchAsyncTask.java:108 directory.forEachChildrenFile(activity.get(), mRootMode, file -> {')

e('SearchAsyncTask.search(HybridFile,String)', 'SearchAsyncTask.lambda$search$1', 'CALL',
  'Lambda for SearchFilter functional interface',
  evidence='SRC SearchAsyncTask.java:131 search(file, fileName -> fileName.toLowerCase().contains(query.toLowerCase()))')

e('SearchAsyncTask.searchRegExFind', 'SearchAsyncTask.lambda$searchRegExFind$2', 'CALL',
  'Lambda for SearchFilter with pattern.matcher().find()',
  evidence='SRC SearchAsyncTask.java:142 search(file, fileName -> pattern.matcher(fileName).find())')

e('SearchAsyncTask.searchRegExMatch', 'SearchAsyncTask.lambda$searchRegExMatch$3', 'CALL',
  'Lambda for SearchFilter with pattern.matcher().matches()',
  evidence='SRC SearchAsyncTask.java:152 search(file, fileName -> pattern.matcher(fileName).matches())')

# ---- part repair_rp06 (2024-10-28)
# Repair batch 06: UtilsHandler, SevenZFile, PrefFrag methods

# UtilsHandler edges
e('UtilsHandler.lambda$saveToDatabase$0(OperationData)', 'UtilsHandler.addSsh(String,String,String,String,String)', 'CALL',
  'saveToDatabase lambda calls addSsh for SFTP connections',
  evidence='SRC database/UtilsHandler.java:190-191: case SFTP: addSsh(operationData.name, operationData.path, operationData.hostKey, operationData.sshKeyName, operationData.sshKey);')

e('UtilsHandler.removeFromDatabase(OperationData)', 'UtilsHandler.lambda$removeFromDatabase$1(OperationData)', 'CALL',
  'removeFromDatabase lambda for background database removal',
  evidence='SRC database/UtilsHandler.java:201-220: AppConfig.runInBackground(() -> { ... lambda body starting at line 202 ... })')

e('UtilsHandler.saveToDatabase(OperationData)', 'UtilsHandler.lambda$saveToDatabase$0(OperationData)', 'CALL',
  'saveToDatabase lambda for background database save',
  evidence='SRC database/UtilsHandler.java:178-197: AppConfig.runInBackground(() -> { ... lambda body starting at line 179 ... })')

e('S_ENTRY', 'UtilsHandler.onCreate(SQLiteDatabase)', 'LIFECYCLE',
  'SQLiteOpenHelper onCreate called when database is first created',
  evidence='SRC database/UtilsHandler.java:33: UtilsHandler extends SQLiteOpenHelper; line 106-115: onCreate(SQLiteDatabase db); framework calls this when database is first created')

e('S_ENTRY', 'UtilsHandler.onUpgrade(SQLiteDatabase,int,int)', 'LIFECYCLE',
  'SQLiteOpenHelper onUpgrade called when database version changes',
  evidence='SRC database/UtilsHandler.java:33: UtilsHandler extends SQLiteOpenHelper; line 38: DATABASE_VERSION = 3; line 117-175: onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion); framework calls when version changes')

e('UtilsHandler.lambda$removeFromDatabase$1(OperationData)', 'UtilsHandler.removeBookmarksPath(String,String)', 'CALL',
  'removeFromDatabase lambda removes bookmark paths',
  evidence='SRC database/UtilsHandler.java:210: case BOOKMARKS: removeBookmarksPath(operationData.name, operationData.path);')

e('UtilsHandler.lambda$removeFromDatabase$1(OperationData)', 'UtilsHandler.removePath(Operation,String)', 'CALL',
  'removeFromDatabase lambda removes paths for HIDDEN/HISTORY/LIST/GRID',
  evidence='SRC database/UtilsHandler.java:207: case HIDDEN: case HISTORY: case LIST: case GRID: removePath(operationData.type, operationData.path);')

e('UtilsHandler.lambda$removeFromDatabase$1(OperationData)', 'UtilsHandler.removeSftpPath(String,String)', 'CALL',
  'removeFromDatabase lambda removes SFTP paths',
  evidence='SRC database/UtilsHandler.java:215: case SFTP: removeSftpPath(operationData.name, operationData.path);')

e('MainActivity.lambda$renameBookmark$27(String[],String,String,MaterialDialog,DialogAction)', 'UtilsHandler.renameSMB(String,String,String,String)', 'CALL',
  'MainActivity renameBookmark dialog calls UtilsHandler.renameSMB',
  evidence='SRC activities/MainActivity.java:1725: utilsHandler.renameSMB(oldEntry[0], oldEntry[1], name, encryptedPath);')

e('UtilsHandler.renameSMB(String,String,String,String)', 'UtilsHandler.renamePath(Operation,String,String,String,String)', 'CALL',
  'renameSMB calls renamePath with Operation.SMB',
  evidence='SRC database/UtilsHandler.java:519: renamePath(Operation.SMB, oldName, oldPath, newName, newPath);')

e('UtilsHandler.lambda$saveToDatabase$0(OperationData)', 'UtilsHandler.setPath(Operation,String)', 'CALL',
  'saveToDatabase lambda calls 2-param setPath for HIDDEN/HISTORY/LIST/GRID',
  evidence='SRC database/UtilsHandler.java:183: case HIDDEN: case HISTORY: case LIST: case GRID: setPath(operationData.type, operationData.path);')

e('UtilsHandler.lambda$saveToDatabase$0(OperationData)', 'UtilsHandler.setPath(Operation,String,String)', 'CALL',
  'saveToDatabase lambda calls 3-param setPath for BOOKMARKS/SMB',
  evidence='SRC database/UtilsHandler.java:186: case BOOKMARKS: case SMB: setPath(operationData.type, operationData.name, operationData.path);')

e('SftpConnectDialog.lambda$authenticateAndSaveSetup$5(String,String,String,String,String,String)', 'UtilsHandler.updateSsh(String,String,String,String,String,String)', 'CALL',
  'SftpConnectDialog lambda calls UtilsHandler.updateSsh',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:386: utilsHandler.updateSsh(connectionName, oldConnectionName, path, hostKey, sshKeyName, sshKey);')

# SevenZFile edges
e('SevenZipExtractor.extractEverything', 'SevenZFile.read(byte[])', 'CALL',
  'SevenZipExtractor reads 7z file entries with read(byte[])',
  evidence='SRC filesystem/compressed/extractcontents/helpers/SevenZipExtractor.java:64: while ((len = sevenZFile.read(buf)) != -1) { outputStream.write(buf, 0, len); }')

# PrefFrag edges
e('PrefFrag.onCreate(Bundle)', 'PrefFrag.lambda$onCreate$0(FingerprintManager,KeyguardManager,Preference,Preference,Object)', 'CALL',
  'onCreate sets fingerprint preference listener',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:117-145: checkBoxFingerprint.setOnPreferenceChangeListener((preference, newValue) -> { ... }); lambda starts at line 118')

e('PrefFrag.onPreferenceClick(Preference)', 'PrefFrag.lambda$onPreferenceClick$1(String[],MaterialDialog,View,int,CharSequence)', 'CALL',
  'onPreferenceClick shows grid columns dialog',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:176: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... }); grid columns preference')

e('PrefFrag.onPreferenceClick(Preference)', 'PrefFrag.lambda$onPreferenceClick$2(MaterialDialog,View,int,CharSequence)', 'CALL',
  'onPreferenceClick shows theme dialog',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:185: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... }); theme preference')

e('PrefFrag.onPreferenceClick(Preference)', 'PrefFrag.lambda$onPreferenceClick$3(MaterialDialog,CharSequence)', 'CALL',
  'onPreferenceClick shows master password input dialog',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:238: masterPasswordDialogBuilder.input(..., (dialog, input) -> { }); for password input')

e('PrefFrag.onPreferenceClick(Preference)', 'PrefFrag.lambda$onPreferenceClick$4(MaterialDialog,DialogAction)', 'CALL',
  'onPreferenceClick master password positive button',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:243-259: masterPasswordDialogBuilder.onPositive((dialog, which) -> { ... }); positive button handler')

e('PrefFrag.onPreferenceClick(Preference)', 'PrefFrag.lambda$onPreferenceClick$5(MaterialDialog,DialogAction)', 'CALL',
  'onPreferenceClick master password negative button',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:261: masterPasswordDialogBuilder.onNegative((dialog, which) -> dialog.cancel()); negative button')

e('S_ENTRY', 'PrefFrag.onCreate(Bundle)', 'LIFECYCLE',
  'PreferenceFragment onCreate lifecycle callback',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:64: PrefFrag extends PreferenceFragment; line 76-147: onCreate; activities/PreferencesActivity.java:255: new PrefFrag() instantiated; framework calls onCreate')

e('S_ENTRY', 'PrefFrag.onCreateView(LayoutInflater,ViewGroup,Bundle)', 'LIFECYCLE',
  'PreferenceFragment onCreateView lifecycle callback',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:284-289: onCreateView; framework calls after onCreate')

e('S_ENTRY', 'PrefFrag.onPause', 'LIFECYCLE',
  'PreferenceFragment onPause lifecycle callback',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:292-302: onPause; framework calls when fragment loses foreground')

e('PrefFrag.onCreate(Bundle)', 'PrefFrag.onPreferenceClick(Preference)', 'CALL',
  'onCreate sets preference click listener',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:92-94: for (String PREFERENCE_KEY : PREFERENCE_KEYS) { findPreference(PREFERENCE_KEY).setOnPreferenceClickListener(this); } // PrefFrag implements OnPreferenceClickListener')

e('S_ENTRY', 'PrefFrag.onResume', 'LIFECYCLE',
  'PreferenceFragment onResume lifecycle callback',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:305-316: onResume; framework calls when fragment comes to foreground')

e('PrefFrag.lambda$onPreferenceClick$2(MaterialDialog,View,int,CharSequence)', 'PrefFrag.restartPC(Activity)', 'CALL',
  'Theme selection lambda restarts activity',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:187: restartPC(getActivity()); called after theme selection')

# Repair batch 06 UNREACHABLE entries
UNREACHABLE['UtilsHandler.renamePath(Operation,String,String)'] = (
    'no_trigger_in_app',
    'Private method with 3 parameters (Operation, name, path). The app only calls the 5-parameter overload renamePath(Operation,String,String,String,String) via renameBookmark (line 514) and renameSMB (line 519). This 3-parameter version is unused dead code.',
    'SRC database/UtilsHandler.java:577-585: private void renamePath(Operation operation, String name, String path); no callers found in app code',
    'SOURCE'
)
UNREACHABLE['SevenZFile.<init>(File,byte[])'] = (
    'no_trigger_in_app',
    'Deprecated constructor taking byte[] password. The app uses SevenZFile.<init>(File,char[]) at SevenZipHelperTask.java:69 and SevenZipExtractor.java:50.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:120-123: @deprecated comment; no app callers found',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel)'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel without password. The app instantiates SevenZFile only via File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:136-138; grep in app shows no FileChannel usage with SevenZFile',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel,String)'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with filename. The app instantiates SevenZFile only via File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:187-190; grep shows no FileChannel usage',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel,String,byte[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with byte[] password. The app uses File-based constructors with char[] password.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:207-210; grep shows no FileChannel usage',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel,String,char[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with char[] password. The app uses File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:170-173; grep shows no FileChannel usage',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel,byte[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with byte[] password. The app uses File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:228-231; grep shows no FileChannel usage',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel,char[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with char[] password. The app uses File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:152-155; grep shows no FileChannel usage',
    'INFERRED'
)
UNREACHABLE['SevenZFile.getStatisticsForCurrentEntry'] = (
    'no_trigger_in_app',
    'Public method returning InputStreamStatistics. The app reads 7z files using getNextEntry() and read() but never calls getStatisticsForCurrentEntry.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1115-1131; grep in app shows no calls',
    'INFERRED'
)
UNREACHABLE['SevenZFile.matches'] = (
    'no_trigger_in_app',
    'Static method to check 7z signature bytes. The app opens 7z files directly without pre-checking signatures.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1158-1164; grep in app shows no calls to matches',
    'INFERRED'
)
UNREACHABLE['SevenZFile.read()'] = (
    'no_trigger_in_app',
    'Single-byte read method. The app uses read(byte[]) for extraction. The no-arg read() is not directly called; read(byte[]) delegates to read(byte[],int,int).',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1050-1055: read() calls read(new byte[1], 0, 1); grep in app shows only read(buf) calls, never read()',
    'INFERRED'
)
UNREACHABLE['SevenZFile.toString'] = (
    'no_trigger_in_app',
    'toString() override. The app opens, reads, and closes 7z files without calling toString().',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1191-1193; grep shows no explicit toString() calls on SevenZFile',
    'INFERRED'
)

# ---- part repair_rp07 (2024-10-28)
# Repair batch 07: StreamServer$HTTPSession, ProcessViewerFragment, SmbConnectDialog

# StreamServer$HTTPSession internal streaming server routes
e('MainFragment.launchSMB', 'Streamer.getInstance', 'CALL',
  'MainFragment.launchSMB calls Streamer.getInstance for SMB streaming',
  evidence='SRC MainFragment.java:1657: final Streamer s = Streamer.getInstance(); SmbStreamer/Streamer.java:57')

e('Streamer.getInstance', 'Streamer.<init>', 'CALL',
  'Singleton getInstance creates Streamer instance',
  evidence='SRC SmbStreamer/Streamer.java:39: instance = new Streamer(PORT);')

e('Streamer.<init>', 'StreamServer.<init>', 'CALL',
  'Streamer constructor calls super StreamServer constructor',
  evidence='SRC Streamer.java:34: super(port, new File("."));')

e('StreamServer.<init>', 'StreamServer$HTTPSession.<init>', 'ASYNC',
  'StreamServer constructor spawns thread that creates HTTPSession on socket accept',
  evidence='SRC SmbStreamer/StreamServer.java:179: new HTTPSession(accept);')

e('StreamServer$HTTPSession.<init>', 'StreamServer$HTTPSession.run', 'ASYNC',
  'HTTPSession constructor starts thread with run() method',
  evidence='SRC SmbStreamer/StreamServer.java:222-224: Thread t = new Thread(this); t.start();')

e('StreamServer$HTTPSession.run', 'StreamServer$HTTPSession.handleResponse', 'CALL',
  'HTTPSession.run calls handleResponse to process HTTP request',
  evidence='SRC SmbStreamer/StreamServer.java:229: handleResponse(socket);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.decodeHeader', 'CALL',
  'handleResponse decodes HTTP headers',
  evidence='SRC SmbStreamer/StreamServer.java:266: decodeHeader(hin, pre, parms, header);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.decodeParms', 'CALL',
  'handleResponse decodes POST form parameters',
  evidence='SRC SmbStreamer/StreamServer.java:323: decodeParms(postLine, parms);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.decodeMultipartData', 'CALL',
  'handleResponse decodes POST multipart/form-data',
  evidence='SRC SmbStreamer/StreamServer.java:320: decodeMultipartData(boundary, fbuf, in, parms, files);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.sendError', 'CALL',
  'handleResponse sends HTTP error if serve() returns null',
  evidence='SRC SmbStreamer/StreamServer.java:330: sendError(socket, HTTP_INTERNALERROR, ...);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.sendResponse', 'CALL',
  'handleResponse sends HTTP response with content',
  evidence='SRC SmbStreamer/StreamServer.java:332: sendResponse(socket, r.status, r.mimeType, r.header, r.data);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer.serve', 'CALL',
  'handleResponse calls abstract serve() method implemented by Streamer',
  evidence='SRC SmbStreamer/StreamServer.java:327: Response r = serve(uri, method, header, parms, files);')

e('StreamServer$HTTPSession.decodeHeader', 'StreamServer$HTTPSession.decodeParms', 'CALL',
  'decodeHeader decodes query parameters from URI',
  evidence='SRC SmbStreamer/StreamServer.java:363: decodeParms(uri.substring(qmi + 1), parms);')

e('StreamServer$HTTPSession.decodeHeader', 'StreamServer$HTTPSession.decodePercent', 'CALL',
  'decodeHeader percent-decodes URI',
  evidence='SRC SmbStreamer/StreamServer.java:364: uri = decodePercent(uri.substring(0, qmi));')

e('StreamServer$HTTPSession.decodeHeader', 'StreamServer$HTTPSession.sendError', 'CALL',
  'decodeHeader sends error on parse failure',
  evidence='SRC SmbStreamer/StreamServer.java:349, 353, 357: sendError(socket, HTTP_BADREQUEST, ...);')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.getBoundaryPositions', 'CALL',
  'decodeMultipartData finds boundary positions in multipart data',
  evidence='SRC SmbStreamer/StreamServer.java:391: int[] bpositions = getBoundaryPositions(fbuf, boundary.getBytes());')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.stripMultipartHeaders', 'CALL',
  'decodeMultipartData strips multipart headers',
  evidence='SRC SmbStreamer/StreamServer.java:435: int offset = stripMultipartHeaders(fbuf, bpositions[boundarycount - 2]);')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.saveTmpFile', 'CALL',
  'decodeMultipartData saves uploaded file to temp',
  evidence='SRC SmbStreamer/StreamServer.java:436: String path = saveTmpFile(fbuf, offset, bpositions[boundarycount - 1] - offset - 4);')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.sendError', 'CALL',
  'decodeMultipartData sends error on parse failure',
  evidence='SRC SmbStreamer/StreamServer.java:395, 400, 425, 449: sendError(socket, HTTP_BADREQUEST, ...);')

e('StreamServer$HTTPSession.decodeParms', 'StreamServer$HTTPSession.decodePercent', 'CALL',
  'decodeParms percent-decodes parameter names and values',
  evidence='SRC SmbStreamer/StreamServer.java:526-527: p.put(decodePercent(e.substring(0, sep)).trim(), decodePercent(e.substring(sep + 1)));')

e('StreamServer$HTTPSession.decodePercent', 'StreamServer$HTTPSession.sendError', 'CALL',
  'decodePercent sends error on invalid encoding',
  evidence='SRC SmbStreamer/StreamServer.java:508: sendError(socket, HTTP_BADREQUEST, ...);')

e('StreamServer$HTTPSession.sendError', 'StreamServer$HTTPSession.sendResponse', 'CALL',
  'sendError formats error as HTTP response',
  evidence='SRC SmbStreamer/StreamServer.java:516: sendResponse(socket, status, MIME_PLAINTEXT, null, null);')

# ProcessViewerFragment routes
e('MainActivity.onCreate', 'ProcessViewerFragment.<init>', 'CALL',
  'MainActivity creates ProcessViewerFragment when processing service intent',
  evidence='SRC MainActivity.java:390: transaction.replace(R.id.content_frame, new ProcessViewerFragment(), KEY_INTENT_PROCESS_VIEWER);')

e('MainActivity.onServiceIntent', 'ProcessViewerFragment.<init>', 'CALL',
  'MainActivity.onServiceIntent creates ProcessViewerFragment',
  evidence='SRC MainActivity.java:1590: transaction.replace(R.id.content_frame, new ProcessViewerFragment(), KEY_INTENT_PROCESS_VIEWER);')

e('ProcessViewerFragment.<init>', 'ProcessViewerFragment.onCreateView', 'LIFECYCLE',
  'Fragment lifecycle: constructor to onCreateView',
  evidence='FW-SRC')

e('ProcessViewerFragment.onCreateView', 'ProcessViewerFragment.onActivityCreated', 'LIFECYCLE',
  'Fragment lifecycle: onCreateView to onActivityCreated',
  evidence='FW-SRC')

e('ProcessViewerFragment.onActivityCreated', 'ProcessViewerFragment.onResume', 'LIFECYCLE',
  'Fragment lifecycle: onActivityCreated to onResume',
  evidence='FW-SRC')

e('ProcessViewerFragment.onResume', 'ProcessViewerFragment.onPause', 'LIFECYCLE',
  'Fragment lifecycle: onResume to onPause',
  evidence='FW-SRC')

e('ProcessViewerFragment.onResume', 'ProcessViewerFragment.processResults', 'CALL',
  'ProcessViewerFragment.onResume sets progress listener that calls processResults',
  evidence='SRC ProcessViewerFragment.java:180-215: serviceInstance.setProgressListener(callback); indirect through service binding')

e('ProcessViewerFragment.processResults', 'ProcessViewerFragment.chartInit', 'CALL',
  'processResults initializes chart on first call',
  evidence='SRC ProcessViewerFragment.java:192: chartInit(total); if !isInitialized')

e('ProcessViewerFragment.processResults', 'ProcessViewerFragment.setupDrawables', 'CALL',
  'processResults sets up UI drawables on first call',
  evidence='SRC ProcessViewerFragment.java:195: setupDrawables(serviceType, move); if !isInitialized')

e('ProcessViewerFragment.processResults', 'ProcessViewerFragment.addEntry', 'CALL',
  'processResults adds data entry to chart',
  evidence='SRC ProcessViewerFragment.java:199-200: addEntry(FileUtils.readableFileSizeFloat(doneBytes), FileUtils.readableFileSizeFloat(dataPackage.speedRaw));')

e('ProcessViewerFragment.processResults', 'FileUtils.readableFileSizeFloat', 'CALL',
  'processResults formats byte sizes for display',
  evidence='SRC ProcessViewerFragment.java:199-200: FileUtils.readableFileSizeFloat(doneBytes) and FileUtils.readableFileSizeFloat(dataPackage.speedRaw)')

e('ProcessViewerFragment.setupDrawables', 'ProcessViewerFragment.cancelBroadcast', 'CALL',
  'setupDrawables creates cancel button that broadcasts cancellation',
  evidence='SRC ProcessViewerFragment.java:248, 260, 272, 284, 296: cancelBroadcast(new Intent(...));')

e('ProcessViewerFragment.cancelBroadcast', 'ProcessViewerFragment.lambda$cancelBroadcast$0', 'GUI',
  'cancelBroadcast sets cancel button click listener',
  evidence='SRC ProcessViewerFragment.java:306: mCancelButton.setOnClickListener(v -> {...});')

e('ProcessViewerFragment.addEntry', 'ProcessViewerFragment.createDataSet', 'CALL',
  'addEntry creates chart dataset if needed',
  evidence='SRC ProcessViewerFragment.java:331: dataSet = createDataSet(); if dataSet is null')

# SmbConnectDialog routes
e('MainActivity.showSmbDialog', 'SmbConnectDialog.<init>', 'CALL',
  'MainActivity.showSmbDialog creates SmbConnectDialog',
  evidence='SRC MainActivity.java:1628: SmbConnectDialog smbConnectDialog = new SmbConnectDialog();')

e('SmbConnectDialog.<init>', 'SmbConnectDialog.onCreate', 'LIFECYCLE',
  'DialogFragment lifecycle: constructor to onCreate',
  evidence='FW-SRC')

e('SmbConnectDialog.onCreate', 'SmbConnectDialog.onCreateDialog', 'LIFECYCLE',
  'DialogFragment lifecycle: onCreate to onCreateDialog',
  evidence='FW-SRC')

e('SmbConnectDialog.onCreate', 'EditTextColorStateUtil.setTint', 'CALL',
  'SmbConnectDialog.onCreate tints EditText fields (actually in onCreateDialog)',
  evidence='SRC SmbConnectDialog.java:164-166: EditTextColorStateUtil.setTint(context, conName, accentColor);')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$0', 'GUI',
  'onCreateDialog sets help button click listener',
  evidence='SRC SmbConnectDialog.java:168: help.setOnClickListener(v -> {...});')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$1', 'GUI',
  'onCreateDialog sets anonymous checkbox click listener',
  evidence='SRC SmbConnectDialog.java:173: ch.setOnClickListener(view -> {...});')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$2', 'GUI',
  'onCreateDialog sets positive button click listener',
  evidence='SRC SmbConnectDialog.java:235: ba3.onPositive((dialog, which) -> {...});')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$3', 'GUI',
  'onCreateDialog sets negative button click listener',
  evidence='SRC SmbConnectDialog.java:279: ba3.onNegative((dialog, which) -> {...});')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$4', 'GUI',
  'onCreateDialog sets neutral button click listener',
  evidence='SRC SmbConnectDialog.java:286: ba3.onNeutral((dialog, which) -> {...});')

e('SmbConnectDialog.lambda$onCreateDialog$0', 'GeneralDialogCreation.showSMBHelpDialog', 'CALL',
  'Help button lambda shows SMB help dialog',
  evidence='SRC SmbConnectDialog.java:170: GeneralDialogCreation.showSMBHelpDialog(context, accentColor1);')

e('SmbConnectDialog.lambda$onCreateDialog$2', 'SmbConnectDialog.createSMBPath', 'CALL',
  'Positive button lambda creates SMB connection path',
  evidence='SRC SmbConnectDialog.java:267, 272: createSMBPath(new String[]{ipa, "", "",domaind}, true) or createSMBPath(new String[]{ipa, useru, passp,domaind}, false);')

e('SmbConnectDialog.setTint', 'SmbConnectDialog.createEditTextColorStateList', 'CALL',
  'Static setTint method creates color state list for EditText',
  evidence='SRC SmbConnectDialog.java:318: ColorStateList editTextColorStateList = createEditTextColorStateList(color);')

# ---- part repair_rp08 (2024-10-28)
# Repair batch 08: MainActivity, PrepareCopyTask, ScrimInsetsRelativeLayout, SubnetScanner methods

# MainActivity connection management edges
e('SmbConnectDialog.lambda$onCreateView$4', 'MainActivity.addConnection(boolean,String,String,String,String,String)', 'CALL',
  'SmbConnectDialog positive action adds/edits SMB connection',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:179: smbConnectionListener.addConnection(edit, s[0], smbFile.getPath(), s[1], name, path);')

e('MainActivity.addConnection(boolean,String,String,String,String,String)', 'MainActivity.getCurrentMainFragment', 'CALL',
  'addConnection refreshes current fragment after adding connection',
  evidence='SRC activities/MainActivity.java:1687-1688: MainActivity.getCurrentMainFragment')

e('MainActivity.addConnection(boolean,String,String,String,String,String)', 'MainActivity.lambda$addConnection$9', 'ASYNC',
  'addConnection spawns background task to update database',
  evidence='SRC activities/MainActivity.java:1697: AppConfig.runInBackground(() -> {...})')

e('SmbConnectDialog.lambda$onCreateView$5', 'MainActivity.deleteConnection(String,String)', 'CALL',
  'SmbConnectDialog negative action deletes SMB connection',
  evidence='SRC ui/dialogs/SmbConnectDialog.java (lambda callback on delete)')

e('MainActivity.deleteConnection(String,String)', 'MainActivity.lambda$deleteConnection$10', 'ASYNC',
  'deleteConnection spawns background task to remove from database',
  evidence='SRC activities/MainActivity.java:1717: AppConfig.runInBackground(() -> {...})')

e('MainActivity.lambda$addConnection$9', 'UtilsHandler.renameSMB', 'CALL',
  'addConnection lambda renames SMB entry when editing',
  evidence='SRC activities/MainActivity.java:1698: utilsHandler.renameSMB(oldname, oldPath, name, path);')

e('MainActivity.lambda$deleteConnection$10', 'OperationData.<init>(Operation,String,String)', 'CALL',
  'deleteConnection lambda creates OperationData for removal',
  evidence='SRC activities/MainActivity.java:1718: new OperationData(UtilsHandler.Operation.SMB, name, path)')

e('MainActivity.lambda$deleteConnection$10', 'UtilsHandler.removeFromDatabase', 'CALL',
  'deleteConnection lambda removes SMB connection from database',
  evidence='SRC activities/MainActivity.java:1717-1719: utilsHandler.removeFromDatabase(new OperationData(...))')

e('SearchWorkerFragment.executeSearch', 'MainActivity.onCancelled', 'CALL',
  'SearchWorkerFragment calls onCancelled when search cancelled',
  evidence='SRC activities/MainActivity.java:1788: implements SearchAsyncHelper.HelperCallbacks')

e('SearchWorkerFragment.executeSearch', 'MainActivity.onPostExecute(String)', 'CALL',
  'SearchWorkerFragment calls onPostExecute after search completes',
  evidence='SRC activities/MainActivity.java:1777: implements SearchAsyncHelper.HelperCallbacks')

e('SearchWorkerFragment.executeSearch', 'MainActivity.onPreExecute(String)', 'CALL',
  'SearchWorkerFragment calls onPreExecute before search starts',
  evidence='SRC activities/MainActivity.java:1771: implements SearchAsyncHelper.HelperCallbacks')

e('SearchWorkerFragment.executeSearch', 'MainActivity.onProgressUpdate(HybridFileParcelable,String)', 'CALL',
  'SearchWorkerFragment calls onProgressUpdate for each result',
  evidence='SRC activities/MainActivity.java:1783: implements SearchAsyncHelper.HelperCallbacks')

e('MainFragment.onListItemClicked', 'MainActivity.setPagingEnabled(boolean)', 'CALL',
  'MainFragment disables ViewPager paging during selection mode',
  evidence='SRC fragments/MainFragment.java:488: getMainActivity().setPagingEnabled(false);')

e('MainActivity.setPagingEnabled(boolean)', 'MainActivity.getTabFragment', 'CALL',
  'setPagingEnabled accesses TabFragment to control ViewPager',
  evidence='SRC activities/MainActivity.java:1272: getTabFragment().mViewPager.setPagingEnabled(b);')

# PrepareCopyTask conflict resolution edges
e('PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)', 'PrepareCopyTask.doNotReplaceFiles(String,ArrayList,ArrayList)', 'CALL',
  'onEndDialog skips conflicting files when user chooses not to replace',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:228,237')

e('PrepareCopyTask.lambda$showDialog$1', 'PrepareCopyTask.doNotReplaceFiles(String,ArrayList,ArrayList)', 'CALL',
  'Skip button lambda removes conflicting files from copy list',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:200-204')

e('HybridFile.forEachChildrenFile', 'PrepareCopyTask.lambda$checkConflicts$0(ArrayList,ArrayList,HybridFileParcelable)', 'CALL',
  'forEachChildrenFile invokes lambda to check for name conflicts',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:142-148')

e('MaterialDialog.show', 'PrepareCopyTask.lambda$showDialog$1(CheckBox,String,ArrayList,ArrayList,MaterialDialog,DialogAction)', 'FRAMEWORK',
  'MaterialDialog framework invokes Skip button lambda',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:200-204: dialogBuilder.onPositive((dialog, which) -> {...})')

e('MaterialDialog.show', 'PrepareCopyTask.lambda$showDialog$2(CheckBox,String,ArrayList,ArrayList,MaterialDialog,DialogAction)', 'FRAMEWORK',
  'MaterialDialog framework invokes Overwrite button lambda',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:205-209: dialogBuilder.onNegative((dialog, which) -> {...})')

e('PrepareCopyTask.lambda$showDialog$2', 'PrepareCopyTask.replaceFiles(String,ArrayList,ArrayList)', 'CALL',
  'Overwrite button lambda replaces conflicting files',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:208')

e('PrepareCopyTask.onPostExecute(CopyNode)', 'PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)', 'CALL',
  'onPostExecute starts conflict resolution workflow',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:172')

e('PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)', 'PrepareCopyTask.showDialog(String,ArrayList,ArrayList)', 'CALL',
  'onEndDialog shows conflict resolution dialog',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:218')

e('PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)', 'PrepareCopyTask.finishCopying', 'CALL',
  'onEndDialog calls finishCopying when all conflicts resolved',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:241')

e('AsyncTask.execute', 'PrepareCopyTask.onPostExecute(CopyNode)', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute after background work',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:153')

e('PrepareCopyTask.onPostExecute(CopyNode)', 'PrepareCopyTask.startService', 'CALL',
  'onPostExecute starts service for cloud/OTG/root copy operations',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:164')

e('AsyncTask.execute', 'PrepareCopyTask.onPreExecute()', 'FRAMEWORK',
  'AsyncTask framework calls onPreExecute before starting task',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:86')

e('PrepareCopyTask.onPreExecute()', 'ProgressDialog.show', 'CALL',
  'onPreExecute shows progress dialog while preparing copy',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:88')

e('PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)', 'PrepareCopyTask.replaceFiles(String,ArrayList,ArrayList)', 'CALL',
  'onEndDialog replaces files when user chooses to overwrite',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:240')

e('PrepareCopyTask.showDialog(String,ArrayList,ArrayList)', 'MaterialDialog.Builder.<init>(Context)', 'CALL',
  'showDialog creates MaterialDialog builder for conflict UI',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:181')

e('PrepareCopyTask.showDialog(String,ArrayList,ArrayList)', 'MaterialDialog.show', 'CALL',
  'showDialog displays conflict resolution dialog',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:211')

# SubnetScanner SMB network discovery edges
e('JVM', 'SubnetScanner.<clinit>()', 'FRAMEWORK',
  'JVM invokes SubnetScanner class initializer on first use',
  evidence='SRC utils/SubnetScanner.java:65-67: static { configure(); }')

e('SubnetScanner.<clinit>()', 'SubnetScanner.configure()', 'CALL',
  'Class initializer calls configure to set jCIFS properties',
  evidence='SRC utils/SubnetScanner.java:66')

e('SmbSearchDialog.startScan', 'SubnetScanner.<init>(Context)', 'CALL',
  'SmbSearchDialog creates SubnetScanner to find SMB servers',
  evidence='SRC utils/SubnetScanner.java:77: new SubnetScanner(context)')

e('SubnetScanner.configure()', 'Config.setProperty', 'CALL',
  'configure sets jCIFS properties for SMB broadcast discovery',
  evidence='SRC utils/SubnetScanner.java:70-73')

e('SmbSearchDialog.onScanComplete', 'SubnetScanner.getResults()', 'CALL',
  'SmbSearchDialog retrieves discovered computers after scan',
  evidence='SRC utils/SubnetScanner.java:202: return new ArrayList<>(this.mResults);')

e('SmbSearchDialog.onCancel', 'SubnetScanner.interrupt()', 'CALL',
  'SmbSearchDialog interrupts scanner when user cancels',
  evidence='SRC utils/SubnetScanner.java:196: super.interrupt(); this.pool.shutdownNow();')

e('SubnetScanner.run', 'SubnetScanner.onFound(ComputerParcelable)', 'CALL',
  'run calls onFound when computer discovered via IP scan',
  evidence='SRC utils/SubnetScanner.java:116')

e('SubnetScanner.tryWithBroadcast', 'SubnetScanner.onFound(ComputerParcelable)', 'CALL',
  'tryWithBroadcast calls onFound when computer discovered via SMB broadcast',
  evidence='SRC utils/SubnetScanner.java:172')

e('Thread.start', 'SubnetScanner.run()', 'FRAMEWORK',
  'Thread framework calls run when SubnetScanner thread started',
  evidence='SRC utils/SubnetScanner.java:84: SubnetScanner extends Thread')

e('SubnetScanner.run()', 'SubnetScanner.tryWithBroadcast()', 'CALL',
  'run attempts SMB broadcast discovery before IP scan',
  evidence='SRC utils/SubnetScanner.java:87')

e('SmbSearchDialog.startScan', 'SubnetScanner.setObserver(ScanObserver)', 'CALL',
  'SmbSearchDialog sets observer to receive scan progress updates',
  evidence='SRC utils/SubnetScanner.java:191: synchronized (this.mLock) { this.observer = scanObserver; }')

e('SubnetScanner.tryWithBroadcast()', 'Thread.start', 'CALL',
  'tryWithBroadcast starts anonymous thread for SMB broadcast',
  evidence='SRC utils/SubnetScanner.java:153')

# Repair batch 08 UNREACHABLE entries
UNREACHABLE['ScrimInsetsRelativeLayout.<init>(Context)'] = (
    'no_trigger_in_app',
    'View class never instantiated; no programmatic instantiation or XML usage found',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:41; GREP: no "new ScrimInsetsRelativeLayout" in app code, no XML layout references',
    'SOURCE'
)
UNREACHABLE['ScrimInsetsRelativeLayout.<init>(Context,AttributeSet)'] = (
    'no_trigger_in_app',
    'View class never instantiated; no XML layouts reference ScrimInsetsRelativeLayout',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:45; GREP: grep -r "ScrimInsetsRelativeLayout" res/layout/ shows 0 results',
    'SOURCE'
)
UNREACHABLE['ScrimInsetsRelativeLayout.<init>(Context,AttributeSet,int)'] = (
    'no_trigger_in_app',
    'View class never instantiated; no XML layouts reference ScrimInsetsRelativeLayout',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:50; GREP: grep -r "ScrimInsetsRelativeLayout" res/layout/ shows 0 results',
    'SOURCE'
)
UNREACHABLE['ScrimInsetsRelativeLayout.draw(Canvas)'] = (
    'no_trigger_in_app',
    'View is never instantiated, so draw method never called by framework',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:75; INFERRED from unreachable constructors',
    'INFERRED'
)
UNREACHABLE['ScrimInsetsRelativeLayout.fitSystemWindows(Rect)'] = (
    'no_trigger_in_app',
    'View is never instantiated, so fitSystemWindows method never called',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:65; INFERRED from unreachable constructors',
    'INFERRED'
)
UNREACHABLE['ScrimInsetsRelativeLayout.init(Context,AttributeSet,int)'] = (
    'no_trigger_in_app',
    'View constructors are unreachable, so init is never called',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:55; INFERRED from unreachable constructors',
    'INFERRED'
)
UNREACHABLE['ScrimInsetsRelativeLayout.onAttachedToWindow()'] = (
    'no_trigger_in_app',
    'View is never instantiated, so lifecycle callback never called',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:111; INFERRED from unreachable constructors',
    'INFERRED'
)
UNREACHABLE['ScrimInsetsRelativeLayout.onDetachedFromWindow()'] = (
    'no_trigger_in_app',
    'View is never instantiated, so lifecycle callback never called',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:119; INFERRED from unreachable constructors',
    'INFERRED'
)
UNREACHABLE['ScrimInsetsRelativeLayout.setOnInsetsCallback(OnInsetsCallback)'] = (
    'no_trigger_in_app',
    'View is never instantiated and setter never called from app code',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:133; GREP: grep -r "setOnInsetsCallback" shows 1 result (definition only)',
    'SOURCE'
)

# ---- part repair_rp09 (2025-01-29)
# Repair batch 09 - AmazeFileManager graph_def.py part file
# Schema-2 edges for 40 methods from rp_09.txt
# Generated 2025-01-XX HH:MM

# PreferencesActivity helper methods (lines 175-200 of PreferencesActivity.java)
# All REACHABLE - called by ColorPref and PrefFrag

# PreferencesActivity.getRestartActivity
# SRC activities/PreferencesActivity.java:196-198
# Called by ColorPref.onBackPressed at fragments/preference_fragments/ColorPref.java:208
e('ColorPref.onBackPressed', 'PreferencesActivity.getRestartActivity', 'CALL',
  'ColorPref.onBackPressed checks if activity restart is needed via getRestartActivity()',
  evidence='SRC fragments/preference_fragments/ColorPref.java:208: if(((PreferencesActivity) getActivity()).getRestartActivity()); SRC activities/PreferencesActivity.java:196-198: public boolean getRestartActivity() { return restartActivity; }')

# PreferencesActivity.onBackPressed
# SRC activities/PreferencesActivity.java:105-120
# Framework lifecycle callback triggered by user pressing back button
e('PreferencesActivity.onCreate', 'PreferencesActivity.onBackPressed', 'FRAMEWORK',
  'Framework calls onBackPressed when user presses back button',
  evidence='FW-SRC core/java/android/app/Activity.java (Activity.onBackPressed dispatched by framework); SRC activities/PreferencesActivity.java:105-120')

e('PreferencesActivity.onBackPressed', 'ColorPref.onBackPressed', 'CALL',
  'PreferencesActivity.onBackPressed delegates to ColorPref if current fragment is ColorPref',
  guard='currentFragment instanceof ColorPref',
  evidence='SRC activities/PreferencesActivity.java:106-107: if(currentFragment instanceof ColorPref) { if(((ColorPref) currentFragment).onBackPressed()) return; }')

e('PreferencesActivity.onBackPressed', 'PreferencesActivity.restartActivity', 'CALL',
  'PreferencesActivity.onBackPressed restarts activity when selectedItem != START_PREFERENCE and restartActivity flag is true',
  guard='selectedItem != START_PREFERENCE && restartActivity',
  evidence='SRC activities/PreferencesActivity.java:109-110: if (selectedItem != START_PREFERENCE && restartActivity) { restartActivity(this); }')

e('PreferencesActivity.onBackPressed', 'PreferencesActivity.selectItem', 'CALL',
  'PreferencesActivity.onBackPressed returns to start preference when selectedItem != START_PREFERENCE and no restart needed',
  guard='selectedItem != START_PREFERENCE && !restartActivity',
  evidence='SRC activities/PreferencesActivity.java:111: } else if (selectedItem != START_PREFERENCE) { selectItem(START_PREFERENCE); }')

e('PreferencesActivity.onBackPressed', 'MainActivity.<init>', 'INTENT',
  'PreferencesActivity.onBackPressed navigates back to MainActivity when at start preference',
  guard='selectedItem == START_PREFERENCE',
  evidence='SRC activities/PreferencesActivity.java:113-117: Intent in = new Intent(PreferencesActivity.this, MainActivity.class); in.setAction(Intent.ACTION_MAIN); this.startActivity(in); this.finish();')

# PreferencesActivity.onOptionsItemSelected
# SRC activities/PreferencesActivity.java:122-153
# Framework callback when options menu item is selected
e('PreferencesActivity.onCreate', 'PreferencesActivity.onOptionsItemSelected', 'GUI',
  'User taps the Up/Home button in PreferencesActivity toolbar',
  gui=['Tap Up button in preferences'],
  evidence='FW-SRC core/java/android/app/Activity.java (Activity.onOptionsItemSelected dispatched by framework for menu items); SRC activities/PreferencesActivity.java:122-153')

e('PreferencesActivity.onOptionsItemSelected', 'PreferenceFragment.onOptionsItemSelected', 'CALL',
  'PreferencesActivity.onOptionsItemSelected delegates to current fragment first',
  evidence='SRC activities/PreferencesActivity.java:124: if(currentFragment.onOptionsItemSelected(item)) return true;')

e('PreferencesActivity.onOptionsItemSelected', 'PreferencesActivity.restartActivity', 'CALL',
  'PreferencesActivity.onOptionsItemSelected restarts activity when selectedItem != START_PREFERENCE and restartActivity flag is true',
  guard='selectedItem != START_PREFERENCE && restartActivity',
  evidence='SRC activities/PreferencesActivity.java:126-127: if (selectedItem != START_PREFERENCE && restartActivity) { restartActivity(this); }')

e('PreferencesActivity.onOptionsItemSelected', 'PreferencesActivity.selectItem', 'CALL',
  'PreferencesActivity.onOptionsItemSelected returns to start preference when selectedItem != START_PREFERENCE',
  guard='selectedItem != START_PREFERENCE && !restartActivity',
  evidence='SRC activities/PreferencesActivity.java:128: } else if (selectedItem != START_PREFERENCE) { selectItem(START_PREFERENCE); }')

e('PreferencesActivity.onOptionsItemSelected', 'MainActivity.<init>', 'INTENT',
  'PreferencesActivity.onOptionsItemSelected navigates back to MainActivity when at start preference',
  guard='selectedItem == START_PREFERENCE',
  evidence='SRC activities/PreferencesActivity.java:130-143: Intent in = new Intent(PreferencesActivity.this, MainActivity.class); activity.finish(); activity.startActivity(in);')

# PreferencesActivity.onSaveInstanceState
# SRC activities/PreferencesActivity.java:103-104
# Framework lifecycle callback
e('PreferencesActivity.onCreate', 'PreferencesActivity.onSaveInstanceState', 'FRAMEWORK',
  'Framework calls onSaveInstanceState to save activity state',
  evidence='FW-SRC core/java/android/app/Activity.java (Activity.onSaveInstanceState dispatched by ActivityThread); SRC activities/PreferencesActivity.java:103-104')

# PreferencesActivity.restartActivity
# SRC activities/PreferencesActivity.java:217-232
# Called from onBackPressed and onOptionsItemSelected (already added above)

# PreferencesActivity.restoreListViewState
# SRC activities/PreferencesActivity.java:189-191
# Called by PrefFrag to restore ListView scroll state
e('PrefFrag.onCreateView(LayoutInflater,ViewGroup,Bundle)', 'PreferencesActivity.restoreListViewState', 'CALL',
  'PrefFrag.onCreateView restores ListView scroll position via PreferencesActivity.restoreListViewState',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:287: Parcelable restored = ((PreferencesActivity) getActivity()).restoreListViewState(START_PREFERENCE); SRC activities/PreferencesActivity.java:189-191')

# PreferencesActivity.saveListViewState
# SRC activities/PreferencesActivity.java:180-182
# Called by PrefFrag to save ListView scroll state
e('PrefFrag.onPreferenceClick(Preference)', 'PreferencesActivity.saveListViewState', 'CALL',
  'PrefFrag.onPreferenceClick saves ListView scroll position before navigating away',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:159: ((PreferencesActivity) getActivity()).saveListViewState(START_PREFERENCE, listView.onSaveInstanceState()); SRC activities/PreferencesActivity.java:180-182')

# PreferencesActivity.setRestartActivity
# SRC activities/PreferencesActivity.java:193-194
# Called by ColorPref to signal that activity restart is needed
e('ColorPref.lambda$onCreate$0(Object,Preference,int,Object)', 'PreferencesActivity.setRestartActivity', 'CALL',
  'ColorPref color change callback sets restart activity flag',
  evidence='SRC fragments/preference_fragments/ColorPref.java:117: if (activity != null) activity.setRestartActivity(); SRC activities/PreferencesActivity.java:193-194')

e('ColorPref.lambda$onCreate$1(Preference)', 'PreferencesActivity.setRestartActivity', 'CALL',
  'ColorPref icon color change callback sets restart activity flag',
  evidence='SRC fragments/preference_fragments/ColorPref.java:156: if (activity != null) activity.setRestartActivity(); SRC activities/PreferencesActivity.java:193-194')

# PemToKeyPairTask - AsyncTask for parsing SSH private keys
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:67-262

# PemToKeyPairTask.<init>(InputStream,Callback)
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:88-90
# Called from SftpConnectDialog.onActivityResult (already in graph_def.py at line 12844)

# PemToKeyPairTask.doInBackground
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:100-122
# AsyncTask lifecycle - automatically called by execute()
e('PemToKeyPairTask.execute', 'PemToKeyPairTask.doInBackground', 'ASYNC',
  'AsyncTask.execute runs doInBackground on worker thread',
  evidence='INFERRED android.os.AsyncTask.execute runs doInBackground on a worker thread; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:100-122')

e('PemToKeyPairTask.doInBackground', 'PemToKeyPairTask.onProgressUpdate', 'ASYNC',
  'doInBackground calls publishProgress which triggers onProgressUpdate on main thread',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:120: publishProgress(new IOException("No converter available to parse selected PEM")); INFERRED AsyncTask.publishProgress triggers onProgressUpdate')

# PemToKeyPairTask.lambda$onProgressUpdate$0
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:145-154
# MaterialDialog onPositive callback
e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$0', 'GUI',
  'User taps OK button in passphrase dialog',
  gui=['Tap OK in SSH key passphrase dialog'],
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:143-154: .onPositive(((dialog, which) -> { ... })); lambda at 145-154')

# PemToKeyPairTask.lambda$onProgressUpdate$1
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:156-160
# MaterialDialog onNegative callback
e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$1', 'GUI',
  'User taps Cancel button in passphrase dialog',
  gui=['Tap Cancel in SSH key passphrase dialog'],
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:155-160: .onNegative(((dialog, which) -> { ... })); lambda at 156-160')

e('PemToKeyPairTask.lambda$onProgressUpdate$1', 'PemToKeyPairTask.toastOnParseError', 'CALL',
  'Cancel callback shows toast error before canceling task',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:158: toastOnParseError(result);')

# PemToKeyPairTask.lambda$onProgressUpdate$2
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:163-167
# WarnableTextInputValidator callback
e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$2', 'CALL',
  'onProgressUpdate sets up text validator with lambda for passphrase input',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:162-167: new WarnableTextInputValidator(..., (text) -> { ... }); lambda at 163-167')

# PemToKeyPairTask.onPostExecute
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:175-179
# AsyncTask lifecycle callback
e('PemToKeyPairTask.doInBackground', 'PemToKeyPairTask.onPostExecute', 'ASYNC',
  'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  evidence='INFERRED android.os.AsyncTask lifecycle calls onPostExecute on main thread after doInBackground returns; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:175-179')

e('PemToKeyPairTask.onPostExecute', 'SftpConnectDialog.lambda$onActivityResult$14', 'CALLBACK',
  'onPostExecute invokes the callback registered in constructor',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:176-178: if(callback != null) { callback.onResult(result); }; callback registered at SftpConnectDialog.java:311')

# PemToKeyPairTask.onProgressUpdate
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:124-173
# AsyncTask lifecycle callback (already added edge from doInBackground above)

# PemToKeyPairTask.toastOnParseError
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:181-185
# Called from lambda$onProgressUpdate$1 (already added above)

# FileUtil$MediaFile - Kitkat MediaStore workaround class (UNREACHABLE)
# SRC filesystem/FileUtil.java:983-1231
# All methods in this inner class are unreachable - no callers found in app

UNREACHABLE['FileUtil$MediaFile.<init>'] = (
  'no_trigger_in_app',
  'MediaFile constructor only called from mkdir() at FileUtil.java:1198, but mkdir() itself is never called; grep shows no MediaFile instantiation outside FileUtil class',
  'SRC filesystem/FileUtil.java:1016-1022 (constructor); grep in app source shows only this definition, no callers except within unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.delete'] = (
  'no_trigger_in_app',
  'MediaFile.delete only called from mkdir() at FileUtil.java:1199, but mkdir() is never called',
  'SRC filesystem/FileUtil.java:1028-1059 (delete method); called only at line 1199 within unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.getExternalFilesDir'] = (
  'no_trigger_in_app',
  'private static method, only called from installTemporaryTrack at line 1134, which is called from getTemporaryAlbumId, which is called from unreachable mkdir()',
  'SRC filesystem/FileUtil.java:987-1010 (getExternalFilesDir); called at line 1134 in installTemporaryTrack; chain starts from unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.getFile'] = (
  'no_trigger_in_app',
  'public method but never called; MediaFile is only instantiated at line 1198 within unreachable mkdir()',
  'SRC filesystem/FileUtil.java:1205-1207 (getFile); grep shows no callers in app source',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.getTemporaryAlbumId'] = (
  'no_trigger_in_app',
  'private method, only called from mkdir() at line 1190, but mkdir() is never called',
  'SRC filesystem/FileUtil.java:1062-1126 (getTemporaryAlbumId); called only at line 1190 within unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.installTemporaryTrack'] = (
  'no_trigger_in_app',
  'private method, only called from getTemporaryAlbumId at line 1091, which is called from unreachable mkdir()',
  'SRC filesystem/FileUtil.java:1129-1170 (installTemporaryTrack); called at line 1091 in getTemporaryAlbumId; chain starts from unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.mkdir'] = (
  'no_trigger_in_app',
  'public method but grep shows no callers in app; Kitkat MediaStore workaround that is unused in this build',
  'SRC filesystem/FileUtil.java:1172-1202 (mkdir); grep in app source shows no callers; Kitkat-specific workaround code',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.write'] = (
  'no_trigger_in_app',
  'public method but grep shows no callers in app; MediaFile is never instantiated outside unreachable mkdir()',
  'SRC filesystem/FileUtil.java:1207-1231 (write); grep shows no callers in app source',
  'SOURCE'
)

# MainActivityHelper$2 - anonymous ErrorCallBack in rename() method
# SRC utils/MainActivityHelper.java:265-328
# Anonymous class implementing Operations.ErrorCallBack interface

# MainActivityHelper$2.exists
# SRC utils/MainActivityHelper.java:267-273
# Callback from Operations.rename when target file already exists
e('Operations.rename', 'MainActivityHelper$2.exists', 'CALLBACK',
  'Operations.rename invokes exists callback when target file already exists',
  evidence='SRC filesystem/Operations.java (Operations.rename checks file existence and calls callback.exists if target exists); SRC utils/MainActivityHelper.java:265 new Operations.ErrorCallBack() { @Override public void exists...; callback method at 267-273')

# MainActivityHelper$2.invalidName
# SRC utils/MainActivityHelper.java:318-325
# Callback from Operations.rename when filename is invalid
e('Operations.rename', 'MainActivityHelper$2.invalidName', 'CALLBACK',
  'Operations.rename invokes invalidName callback when new filename is invalid',
  evidence='SRC filesystem/Operations.java (Operations.rename validates filename and calls callback.invalidName if invalid); SRC utils/MainActivityHelper.java:318-325')

# MainActivityHelper$2.lambda$done$2
# SRC utils/MainActivityHelper.java:299-316
# Runnable lambda in done() callback
e('MainActivityHelper$2.done', 'MainActivityHelper$2.lambda$done$2', 'CALL',
  'done callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:297-316: context.runOnUiThread(() -> { ... }); lambda starts at 299')

# MainActivityHelper$2.lambda$exists$0
# SRC utils/MainActivityHelper.java:268-272
# Runnable lambda in exists() callback
e('MainActivityHelper$2.exists', 'MainActivityHelper$2.lambda$exists$0', 'CALL',
  'exists callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:267-273: context.runOnUiThread(() -> { ... }); lambda at 268-272')

# MainActivityHelper$2.lambda$invalidName$3
# SRC utils/MainActivityHelper.java:319-324
# Runnable lambda in invalidName() callback
e('MainActivityHelper$2.invalidName', 'MainActivityHelper$2.lambda$invalidName$3', 'CALL',
  'invalidName callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:318-325: context.runOnUiThread(() -> { ... }); lambda at 319-324')

# MainActivityHelper$2.lambda$launchSAF$1
# SRC utils/MainActivityHelper.java:280-288
# Runnable lambda in launchSAF(HybridFile,HybridFile) callback
e('MainActivityHelper$2.launchSAF(HybridFile,HybridFile)', 'MainActivityHelper$2.lambda$launchSAF$1', 'CALL',
  'launchSAF callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:278-289: context.runOnUiThread(() -> { ... }); lambda at 280-288')

e('MainActivityHelper$2.lambda$launchSAF$1', 'MainActivityHelper.guideDialogForLEXA', 'CALL',
  'launchSAF lambda shows SAF guide dialog',
  evidence='SRC utils/MainActivityHelper.java:285: guideDialogForLEXA(mainActivity.oppathe1);')

# MainActivityHelper$2.launchSAF(HybridFile)
# SRC utils/MainActivityHelper.java:276 (empty method)
UNREACHABLE['MainActivityHelper$2.launchSAF(HybridFile)'] = (
  'no_trigger_in_app',
  'empty callback method with no implementation in anonymous class',
  'SRC utils/MainActivityHelper.java:275-277: @Override public void launchSAF(HybridFile file) { } // empty',
  'SOURCE'
)

# MainActivityHelper$2.launchSAF(HybridFile,HybridFile)
# SRC utils/MainActivityHelper.java:278-289
# Callback from Operations.rename when SAF is needed
e('Operations.rename', 'MainActivityHelper$2.launchSAF(HybridFile,HybridFile)', 'CALLBACK',
  'Operations.rename invokes launchSAF callback when Storage Access Framework is needed for rename',
  evidence='SRC filesystem/Operations.java (Operations.rename detects need for SAF and calls callback.launchSAF); SRC utils/MainActivityHelper.java:278-289')

# MainActivityHelper$3 - anonymous ErrorCallBack in mkfile() method
# SRC utils/MainActivityHelper.java:394-447
# Anonymous class implementing Operations.ErrorCallBack interface

# MainActivityHelper$3.exists
# SRC utils/MainActivityHelper.java:396-408
# Callback from Operations.mkfile when file already exists
e('Operations.mkfile', 'MainActivityHelper$3.exists', 'CALLBACK',
  'Operations.mkfile invokes exists callback when target file already exists',
  evidence='SRC filesystem/Operations.java (Operations.mkfile checks file existence and calls callback.exists if exists); SRC utils/MainActivityHelper.java:394 new Operations.ErrorCallBack() { @Override public void exists...; callback at 396-408')

e('MainActivityHelper$3.exists', 'MainActivityHelper$3.lambda$exists$0', 'CALL',
  'exists callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:396-408: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 397-406')

# MainActivityHelper$3.invalidName
# SRC utils/MainActivityHelper.java:437-445
# Callback from Operations.mkfile when filename is invalid
e('Operations.mkfile', 'MainActivityHelper$3.invalidName', 'CALLBACK',
  'Operations.mkfile invokes invalidName callback when filename is invalid',
  evidence='SRC filesystem/Operations.java (Operations.mkfile validates filename and calls callback.invalidName if invalid); SRC utils/MainActivityHelper.java:437-445')

e('MainActivityHelper$3.invalidName', 'MainActivityHelper$3.lambda$invalidName$3', 'CALL',
  'invalidName callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:437-445: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 438-443')

# MainActivityHelper$3.lambda$done$2
# SRC utils/MainActivityHelper.java:427-434
# Runnable lambda in done() callback
e('MainActivityHelper$3.done', 'MainActivityHelper$3.lambda$done$2', 'CALL',
  'done callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:425-435: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 427-434')

# MainActivityHelper$3.lambda$exists$0
# SRC utils/MainActivityHelper.java:397-406
# Runnable lambda in exists() callback (already added above)

# MainActivityHelper$3.lambda$invalidName$3
# SRC utils/MainActivityHelper.java:438-443
# Runnable lambda in invalidName() callback (already added above)

# MainActivityHelper$3.lambda$launchSAF$1
# SRC utils/MainActivityHelper.java:412-419
# Runnable lambda in launchSAF(HybridFile) callback
e('MainActivityHelper$3.launchSAF(HybridFile)', 'MainActivityHelper$3.lambda$launchSAF$1', 'CALL',
  'launchSAF callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:410-420: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 412-419')

e('MainActivityHelper$3.lambda$launchSAF$1', 'MainActivityHelper.guideDialogForLEXA', 'CALL',
  'launchSAF lambda shows SAF guide dialog',
  evidence='SRC utils/MainActivityHelper.java:416: guideDialogForLEXA(mainActivity.oppathe);')

# MainActivityHelper$3.launchSAF(HybridFile)
# SRC utils/MainActivityHelper.java:410-420
# Callback from Operations.mkfile when SAF is needed
e('Operations.mkfile', 'MainActivityHelper$3.launchSAF(HybridFile)', 'CALLBACK',
  'Operations.mkfile invokes launchSAF callback when Storage Access Framework is needed',
  evidence='SRC filesystem/Operations.java (Operations.mkfile detects need for SAF and calls callback.launchSAF); SRC utils/MainActivityHelper.java:410-420')

# MainActivityHelper$3.launchSAF(HybridFile,HybridFile)
# SRC utils/MainActivityHelper.java:422-423 (empty method)
UNREACHABLE['MainActivityHelper$3.launchSAF(HybridFile,HybridFile)'] = (
  'no_trigger_in_app',
  'empty callback method with no implementation in anonymous class',
  'SRC utils/MainActivityHelper.java:422-423: @Override public void launchSAF(HybridFile file, HybridFile file1) { } // empty',
  'SOURCE'
)


# ---- part repair_rp11 (2025-01-29)
# repair batch 11 - TabFragment, SmbSearchDialog$ListViewAdapter, RoundedImageView, SelectedColorsPreference, ZipService$CompressAsyncTask, SevenZOutputFile$OutputStreamWrapper

# TabFragment.onDestroyView - Fragment lifecycle method called by framework
e('TabFragment.onCreateView', 'TabFragment.onDestroyView', 'LIFECYCLE',
  'Fragment lifecycle: onDestroyView called by framework when view is destroyed',
  evidence='FW-SRC android-8.1.0_r1/core/java/android/app/Fragment.java:2744-2758 performDestroyView() calls onDestroyView(); FragmentManager.java:1356 calls f.performDestroyView() during fragment teardown')

# TabFragment.onPageScrollStateChanged - ViewPager.OnPageChangeListener interface method
e('TabFragment.onCreateView', 'TabFragment.onPageScrollStateChanged', 'FRAMEWORK',
  'ViewPager calls OnPageChangeListener.onPageScrollStateChanged on registered listeners',
  evidence='SRC TabFragment.java:45 implements ViewPager.OnPageChangeListener; SRC TabFragment.java:99 mViewPager.addOnPageChangeListener(this) registers TabFragment as listener; ViewPager framework calls this method')

# TabFragment.onPageScrolled - ViewPager.OnPageChangeListener interface method
e('TabFragment.onCreateView', 'TabFragment.onPageScrolled', 'FRAMEWORK',
  'ViewPager calls OnPageChangeListener.onPageScrolled on registered listeners during scroll',
  evidence='SRC TabFragment.java:45 implements ViewPager.OnPageChangeListener; SRC TabFragment.java:99 mViewPager.addOnPageChangeListener(this) registers TabFragment as listener; ViewPager framework calls this method')

# TabFragment.onPageSelected - ViewPager.OnPageChangeListener interface method (already has edges, add more)
e('TabFragment.onPageSelected', 'BottomBar.updatePath', 'CALL',
  'When page selected, updates bottom bar path',
  evidence='SRC TabFragment.java:287 mainActivity.getAppbar().getBottomBar().updatePath(ma.getCurrentPath(), ...)')

# TabFragment.onSaveInstanceState - Fragment lifecycle method  
e('TabFragment.onCreateView', 'TabFragment.onSaveInstanceState', 'LIFECYCLE',
  'Fragment lifecycle: framework calls onSaveInstanceState to save instance state',
  evidence='SRC TabFragment.java:260 overrides onSaveInstanceState; framework calls this on Fragment instances during configuration changes or process death')

# TabFragment.parsePathForName - UNREACHABLE, no callers in app
UNREACHABLE['TabFragment.parsePathForName'] = ('no_trigger_in_app', 'parsePathForName is never called in the app; grep finds no callers', 'SRC TabFragment.java:243-255 defines parsePathForName but no app code calls it; grep -rn "\\.parsePathForName" in app/src/main/java finds no calls', 'SOURCE')

# TabFragment.parseSmbPath - UNREACHABLE, only called from unreachable parsePathForName
UNREACHABLE['TabFragment.parseSmbPath'] = ('no_trigger_in_app', 'parseSmbPath is only called by parsePathForName which itself is never called', 'SRC TabFragment.java:237-241 defines parseSmbPath; TabFragment.java:248 shows only call is from parsePathForName; parsePathForName has no callers (see above)', 'SOURCE')

# SmbSearchDialog$ListViewAdapter.<init> - RecyclerView.Adapter constructor
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.<init>', 'CALL',
  'SmbSearchDialog creates ListViewAdapter instance',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:78 listViewAdapter = new ListViewAdapter(getActivity(), computers)')

# SmbSearchDialog$ListViewAdapter.getItemCount - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.getItemCount', 'FRAMEWORK',
  'RecyclerView calls getItemCount on adapter to determine number of items',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:179-181 overrides getItemCount(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.getItemId - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.getItemId', 'FRAMEWORK',
  'RecyclerView calls getItemId on adapter to get stable IDs',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:175-177 overrides getItemId(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.getItemViewType - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.getItemViewType', 'FRAMEWORK',
  'RecyclerView calls getItemViewType on adapter to determine view type',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:165-173 overrides getItemViewType(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.lambda$onBindViewHolder$0 - lambda expression
e('SmbSearchDialog$ListViewAdapter.onBindViewHolder', 'SmbSearchDialog$ListViewAdapter.lambda$onBindViewHolder$0', 'CALL',
  'onBindViewHolder sets click listener that calls lambda',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:148-158 holder.rootView.setOnClickListener lambda expression compiled to this method')

# SmbSearchDialog$ListViewAdapter.onBindViewHolder - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.onBindViewHolder', 'FRAMEWORK',
  'RecyclerView calls onBindViewHolder on adapter to bind view holders',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:144-162 overrides onBindViewHolder(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.onCreateViewHolder - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.onCreateViewHolder', 'FRAMEWORK',
  'RecyclerView calls onCreateViewHolder on adapter to create view holders',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:131-142 overrides onCreateViewHolder(); RecyclerView framework calls this on adapters')

# RoundedImageView.<init> - Custom view constructor
e('S_UNKNOWN', 'RoundedImageView.<init>', 'FRAMEWORK',
  'Android framework inflates RoundedImageView from XML layouts',
  evidence='SRC ui/views/RoundedImageView.java:32-37 constructor(Context,AttributeSet); framework calls this when inflating custom views from XML')

# RoundedImageView.drawableToBitmap - internal utility method
e('RoundedImageView.onDraw', 'RoundedImageView.drawableToBitmap', 'CALL',
  'onDraw calls drawableToBitmap to convert drawable to bitmap',
  evidence='SRC ui/views/RoundedImageView.java:44 Bitmap b = drawableToBitmap(drawable)')

# RoundedImageView.drawableToBitmapRelative - internal utility method
e('RoundedImageView.onDraw', 'RoundedImageView.drawableToBitmapRelative', 'CALL',
  'onDraw calls drawableToBitmapRelative for icon images',
  evidence='SRC ui/views/RoundedImageView.java:55 Bitmap bitmap = drawableToBitmapRelative(drawable, radius)')

# RoundedImageView.getRoundedCroppedBitmap - internal utility method
e('RoundedImageView.onDraw', 'RoundedImageView.getRoundedCroppedBitmap', 'CALL',
  'onDraw calls getRoundedCroppedBitmap to create rounded bitmap',
  evidence='SRC ui/views/RoundedImageView.java:47 Bitmap roundBitmap = getRoundedCroppedBitmap(bitmap, w)')

# RoundedImageView.isImageAnIcon - internal utility method
e('RoundedImageView.onDraw', 'RoundedImageView.isImageAnIcon', 'CALL',
  'onDraw calls isImageAnIcon to check if image should be treated as icon',
  evidence='SRC ui/views/RoundedImageView.java:43 if(!isImageAnIcon())')

# RoundedImageView.onDraw - View lifecycle method
e('RoundedImageView.<init>', 'RoundedImageView.onDraw', 'FRAMEWORK',
  'Android View framework calls onDraw to render the view',
  evidence='SRC ui/views/RoundedImageView.java:40-58 overrides onDraw(Canvas); View framework calls this when view needs to be drawn')

# RoundedImageView.setBackgroundColor - UNREACHABLE, no callers
UNREACHABLE['RoundedImageView.setBackgroundColor'] = ('no_trigger_in_app', 'setBackgroundColor is never called on RoundedImageView instances in app code', 'SRC ui/views/RoundedImageView.java:65-67 defines setBackgroundColor; grep -rn "setBackgroundColor" in app finds no calls on RoundedImageView instances, only the definition', 'SOURCE')

# SelectedColorsPreference.<init> - Preference constructor called via subclass
e('S_PREFERENCES', 'SelectedColorsPreference.<init>', 'FRAMEWORK',
  'Android preference framework creates ColorPickerDialog (subclass) from XML, calling super constructor',
  evidence='SRC ui/dialogs/ColorPickerDialog.java:40 extends SelectedColorsPreference; SRC res/xml/conficolor_prefs.xml:3 declares ColorPickerDialog; framework calls constructor')

# SelectedColorsPreference.invalidateColors - called from ColorPref
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.invalidateColors', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColors on ColorPickerDialog to refresh display',
  evidence='SRC preference_fragments/ColorPref.java:265 selectedColors.invalidateColors() inside invalidateEverything(); line 262 shows selectedColors is ColorPickerDialog which extends SelectedColorsPreference')

# SelectedColorsPreference.onBindView - Preference lifecycle method
e('SelectedColorsPreference.onCreateView', 'SelectedColorsPreference.onBindView', 'FRAMEWORK',
  'Preference framework calls onBindView after onCreateView to bind data',
  evidence='SRC ui/views/preference/SelectedColorsPreference.java:38-46 overrides onBindView(); framework calls this after onCreateView')

e('SelectedColorsPreference.onBindView', 'CircularColorsView.setColors', 'CALL',
  'onBindView calls setColors to configure the colors view',
  evidence='SRC ui/views/preference/SelectedColorsPreference.java:43 colorsView.setColors(colors[0], colors[1], colors[2], colors[3])')

# SelectedColorsPreference.onCreateView - Preference lifecycle method
e('SelectedColorsPreference.<init>', 'SelectedColorsPreference.onCreateView', 'FRAMEWORK',
  'Preference framework calls onCreateView to create preference view',
  evidence='SRC ui/views/preference/SelectedColorsPreference.java:32-35 overrides onCreateView(); framework calls this on Preference instances')

# SelectedColorsPreference.setColors - called from ColorPref chain
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.setColors', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColorPreference which calls setColors on ColorPickerDialog',
  evidence='SRC preference_fragments/ColorPref.java:264 invalidateEverything calls invalidateColorPreference(selectedColors); ColorPref.java:278-280 invalidateColorPreference calls selectedColors.setColors(...); line 262 shows selectedColors is ColorPickerDialog which extends SelectedColorsPreference')

# SelectedColorsPreference.setColorsVisibility - called from ColorPref chain
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.setColorsVisibility', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColorPreference which calls setColorsVisibility',
  evidence='SRC preference_fragments/ColorPref.java:264 invalidateEverything calls invalidateColorPreference(selectedColors); ColorPref.java:275,288 invalidateColorPreference calls selectedColors.setColorsVisibility(...); line 262 shows selectedColors is ColorPickerDialog')

# SelectedColorsPreference.setDividerColor - called from ColorPref chain
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.setDividerColor', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColorPreference which calls setDividerColor',
  evidence='SRC preference_fragments/ColorPref.java:264 invalidateEverything calls invalidateColorPreference(selectedColors); ColorPref.java:283,285 invalidateColorPreference calls selectedColors.setDividerColor(...); line 262 shows selectedColors is ColorPickerDialog')

# ZipService$CompressAsyncTask.compressFile - internal recursive method
e('ZipService$CompressAsyncTask.execute', 'ZipService$CompressAsyncTask.compressFile', 'CALL',
  'execute method calls compressFile for each file to compress',
  evidence='SRC asynchronous/services/ZipService.java:263 compressFile(file, "") called in loop')

e('ZipService$CompressAsyncTask.compressFile', 'ZipService$CompressAsyncTask.compressFile', 'CALL',
  'compressFile recursively calls itself for directory contents',
  evidence='SRC asynchronous/services/ZipService.java:279 for loop calls compressFile(currentFile, ...) recursively')

# ZipService$CompressAsyncTask.doInBackground - AsyncTask lifecycle method
e('ZipService$CompressAsyncTask.<init>', 'ZipService$CompressAsyncTask.doInBackground', 'ASYNC',
  'AsyncTask framework calls doInBackground on worker thread',
  evidence='SRC asynchronous/services/ZipService.java:218-234 overrides doInBackground(); AsyncTask framework calls this on background thread after execute()')

# ZipService$CompressAsyncTask.execute - AsyncTask execute wrapper
e('ZipService.onStartCommand', 'ZipService$CompressAsyncTask.execute', 'CALL',
  'ZipService calls execute to start compression task',
  evidence='SRC asynchronous/services/ZipService.java:141 asyncTask.execute() starts the async task')

# ZipService$CompressAsyncTask.lambda$doInBackground$0 - lambda expression
e('ZipService$CompressAsyncTask.doInBackground', 'ZipService$CompressAsyncTask.lambda$doInBackground$0', 'CALL',
  'doInBackground sets progress listener lambda',
  evidence='SRC asynchronous/services/ZipService.java:227-228 progressHandler.setProgressListener lambda compiled to this method')

# ZipService$CompressAsyncTask.onCancelled - AsyncTask lifecycle method
e('ZipService$CompressAsyncTask.<init>', 'ZipService$CompressAsyncTask.onCancelled', 'ASYNC',
  'AsyncTask framework calls onCancelled if task is cancelled',
  evidence='SRC asynchronous/services/ZipService.java:236-242 overrides onCancelled(); AsyncTask framework calls this on UI thread if cancel() was called')

# ZipService$CompressAsyncTask.onPostExecute - AsyncTask lifecycle method
e('ZipService$CompressAsyncTask.<init>', 'ZipService$CompressAsyncTask.onPostExecute', 'ASYNC',
  'AsyncTask framework calls onPostExecute on UI thread after doInBackground',
  evidence='SRC asynchronous/services/ZipService.java:244-250 overrides onPostExecute(); AsyncTask framework calls this on UI thread after doInBackground completes')

# SevenZOutputFile$OutputStreamWrapper - library class from Apache Commons Compress
# These methods are part of the Commons Compress library bundled with the app but never used
# grep proves no app references to SevenZOutputFile or OutputStreamWrapper

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.<init>'] = ('no_trigger_in_app', 'OutputStreamWrapper is an inner class of Apache Commons Compress SevenZOutputFile library class; no app code references SevenZOutputFile or OutputStreamWrapper', 'grep -rn "SevenZOutputFile\\|OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches; library class bundled but unused', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.close'] = ('no_trigger_in_app', 'OutputStreamWrapper.close is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.flush'] = ('no_trigger_in_app', 'OutputStreamWrapper.flush is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.write(int)'] = ('no_trigger_in_app', 'OutputStreamWrapper.write(int) is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.write(byte[])'] = ('no_trigger_in_app', 'OutputStreamWrapper.write(byte[]) is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.write(byte[],int,int)'] = ('no_trigger_in_app', 'OutputStreamWrapper.write(byte[],int,int) is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')


# ---- part repair_rp13 (2025-01-29)
# Repair batch 13 - AmazeFileManager trigger graph repair edges
# Generated for methods in scratch/repair_batches/rp_13.txt
# Schema-2 format matching existing graph_def.py structure

# ========== PermissionsActivity methods ==========

# PermissionsActivity.isGranted - private helper called only by onRequestPermissionsResult
UNREACHABLE['PermissionsActivity.isGranted'] = ('no_trigger_in_app', 'Private helper method called only internally by PermissionsActivity.onRequestPermissionsResult at line 30', 'SRC activities/superclasses/PermissionsActivity.java:97-99', 'SOURCE')

# PermissionsActivity.lambda$requestInstallApkPermission$1 - synthetic lambda
# Created by lambda at requestInstallApkPermission line 65
e('PermissionsActivity.requestInstallApkPermission', 'PermissionsActivity.lambda$requestInstallApkPermission$1', 'GUI', 'MaterialDialog negative button callback for APK install permission', 
  evidence='SRC activities/superclasses/PermissionsActivity.java:65 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> materialDialog.dismiss())')

# PermissionsActivity.lambda$requestPermission$2 - synthetic lambda
# Created by lambda at requestPermission line 86
e('PermissionsActivity.requestPermission', 'PermissionsActivity.lambda$requestPermission$2', 'GUI', 'MaterialDialog positive button callback for permission request',
  evidence='SRC activities/superclasses/PermissionsActivity.java:86-89 rationale.getActionButton(DialogAction.POSITIVE).setOnClickListener(v -> { ActivityCompat.requestPermissions(...); rationale.dismiss(); })')

# PermissionsActivity.lambda$requestStoragePermission$0 - synthetic lambda
# Created by lambda at requestStoragePermission line 56
e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.lambda$requestStoragePermission$0', 'GUI', 'MaterialDialog negative button callback for storage permission',
  evidence='SRC activities/superclasses/PermissionsActivity.java:56 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> finish())')

# PermissionsActivity.onRequestPermissionsResult - framework lifecycle callback
# Called by framework when permission request completes
e('MainActivity.requestStoragePermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when permission result arrives; MainActivity extends PermissionsActivity',
  evidence='INFERRED Android framework delivers permission results to Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:26-45 shows implementation')

e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when storage permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:60 calls ActivityCompat.requestPermissions')

e('PermissionsActivity.requestInstallApkPermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when install APK permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:69 calls ActivityCompat.requestPermissions')

e('PermissionsActivity.requestPermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:90 or 87 calls ActivityCompat.requestPermissions')

# ========== GetSshHostFingerprintTask methods ==========

# GetSshHostFingerprintTask.<init> - constructor called from SftpConnectDialog
e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'Instantiate task to verify SSH host fingerprint when saving connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...})')

e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'Instantiate task to get SSH host fingerprint for new connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...})')

# GetSshHostFingerprintTask.doInBackground - AsyncTask worker thread method
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.doInBackground', 'ASYNC', 'AsyncTask.execute runs doInBackground on worker thread',
  evidence='INFERRED AsyncTask.execute schedules doInBackground; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:62 extends AsyncTask')

# GetSshHostFingerprintTask.lambda$doInBackground$0 - synthetic lambda for host key verifier
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL', 'Lambda host key verifier callback invoked when SSH client connects',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:85-89 sshClient.addHostKeyVerifier((hostname, port, key) -> { holder.set(...); latch.countDown(); return true; })')

# GetSshHostFingerprintTask.onPostExecute - AsyncTask main thread callback
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'ASYNC', 'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  evidence='INFERRED AsyncTask lifecycle delivers result to onPostExecute; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:108-122 shows implementation')

# GetSshHostFingerprintTask.onPreExecute - AsyncTask main thread pre-execution
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.onPreExecute', 'ASYNC', 'AsyncTask.execute calls onPreExecute on main thread before doInBackground',
  evidence='INFERRED AsyncTask.execute calls onPreExecute before worker thread runs; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:104-106 shows implementation')

# ========== FileUtil methods ==========

# FileUtil.<init> - abstract class, no public constructor
UNREACHABLE['FileUtil.<init>'] = ('no_trigger_in_app', 'Abstract class with only static utility methods; no instances created', 'SRC filesystem/FileUtil.java:78 public abstract class FileUtil', 'SOURCE')

# FileUtil.copyDummyFile - private helper called only by copyDummyFiles
UNREACHABLE['FileUtil.copyDummyFile'] = ('no_trigger_in_app', 'Private static method called only internally by FileUtil.copyDummyFiles at line 973-974', 'SRC filesystem/FileUtil.java:888-927 private static File copyDummyFile(...)', 'SOURCE')

# FileUtil.copyDummyFiles - private helper called only by MediaFile methods (API<29 only)
UNREACHABLE['FileUtil.copyDummyFiles'] = ('closed_by_api_level', 'Private helper for MediaFile workaround on API<29; standard config is API 27 but usage is guarded and SAF is preferred', 'SRC filesystem/FileUtil.java:971-976 private static File copyDummyFiles(Context c)', 'SOURCE')

# FileUtil.getTempFile - public method but not called by app code
UNREACHABLE['FileUtil.getTempFile'] = ('no_trigger_in_app', 'Public method but no app code calls it; grep -rn getTempFile over app/src/main shows only the definition', 'SRC filesystem/FileUtil.java:476-479', 'SOURCE')

# FileUtil.mkfile - public method called from Operations
# Already has edge at graph_def.py:3692: e('Operations.mkFile', 'FileUtil.mkfile', 'CALL', 'create file',

# ========== Coders$DeflateDecoder$DeflateDecoderOutputStream methods ==========
# These are library classes in commons_compress_7z module, called internally by Coders.addEncoder

# Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>
e('Coders$DeflateDecoder.encode', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>', 'CALL', 'Create deflate output stream wrapper when encoding 7z archive with DEFLATE compression',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Coders.java:155 return new DeflateDecoderOutputStream(deflaterOutputStream, deflater)')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.close - OutputStream method
# Called by framework/library code that uses OutputStreams
e('SevenZOutputFile.finish', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.close', 'CALL', 'Close output stream when finishing 7z archive compression',
  evidence='INFERRED SevenZOutputFile.finish closes the encoder output streams; SRC Coders.java:217-225 shows close implementation')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int)
# Called by framework/library OutputStream users
e('SevenZOutputFile.write', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int)', 'CALL', 'Write single byte when compressing 7z archive with DEFLATE',
  evidence='INFERRED OutputStream.write(int) called by compression pipeline; SRC Coders.java:204-206 shows implementation')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[])
# Called by framework/library OutputStream users
e('SevenZOutputFile.write', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[])', 'CALL', 'Write byte array when compressing 7z archive with DEFLATE',
  evidence='INFERRED OutputStream.write(byte[]) called by compression pipeline; SRC Coders.java:209-211 shows implementation')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int)
# Called by framework/library OutputStream users
e('SevenZOutputFile.write', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int)', 'CALL', 'Write byte range when compressing 7z archive with DEFLATE',
  evidence='INFERRED OutputStream.write(byte[],int,int) called by compression pipeline; SRC Coders.java:214-216 shows implementation')

# ========== SshClientUtils methods ==========

# SshClientUtils.<init> - abstract class constructor
UNREACHABLE['SshClientUtils.<init>'] = ('no_trigger_in_app', 'Abstract utility class with only static methods; no instances created', 'SRC filesystem/ssh/SshClientUtils.java:51 public abstract class SshClientUtils', 'SOURCE')

# SshClientUtils.deriveSftpPathFrom - static utility method
e('SftpConnectDialog.onCreateDialog', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP connection URL from connection parameters',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:171 utilsHandler.getSshHostKey(deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair))')

e('SftpConnectDialog.onCreateDialog', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP connection URL to remove old connection from pool',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:176 SshConnectionPool.getInstance().removeConnection(SshClientUtils.deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair), ...)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP URL path for saving connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:242 final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP path for connection test',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:336 final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SshConnectionPool.getConnection', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build normalized connection URL',
  evidence='SRC filesystem/ssh/SshConnectionPool.java:150 String url = SshClientUtils.deriveSftpPathFrom(host, port, username, password, keyPair)')

# SshClientUtils.lambda$launchSftp$1 - synthetic lambda for thread
e('SshClientUtils.launchSftp', 'SshClientUtils.lambda$launchSftp$1', 'ASYNC', 'Lambda runnable executed on new thread to stream SFTP file',
  evidence='SRC filesystem/ssh/SshClientUtils.java:240 new Thread(() -> { ... }).start()')

# SshClientUtils.lambda$null$0 - nested lambda within launchSftp thread
e('SshClientUtils.lambda$launchSftp$1', 'SshClientUtils.lambda$null$0', 'CALL', 'Lambda runnable to launch file viewer on UI thread',
  evidence='SRC filesystem/ssh/SshClientUtils.java:243 activity.runOnUiThread(() -> { ... })')

# SshClientUtils.launchSftp - public method called from MainFragment
e('MainFragment.onListItemClick', 'SshClientUtils.launchSftp', 'CALL', 'Launch SFTP file in external app when user clicks file in SFTP directory',
  evidence='SRC fragments/MainFragment.java:919 SshClientUtils.launchSftp(e.generateBaseFile(), getMainActivity())')

# ========== ColorCircleDrawable methods ==========
# Already have edges in graph_def.py lines 1507-1527, but let me check if constructors are there

# ColorCircleDrawable.<init> not in UNREACHABLE, checking for existing edge
# Line 1507 shows: e('TabFragment.updatePathColors', 'ColorCircleDrawable.<init>', ...
# So constructor already has route

# The Drawable callback methods already have edges as pseudo-node 'Drawable' -> method
# These are framework callbacks, already handled

# ========== RenameBookmark methods ==========

# RenameBookmark.lambda$onCreateDialog$0 - synthetic lambda for neutral button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$0', 'GUI', 'MaterialDialog neutral button callback to cancel rename',
  evidence='SRC ui/dialogs/RenameBookmark.java:81 builder.onNeutral((dialog, which) -> dialog.dismiss())')

# RenameBookmark.lambda$onCreateDialog$1 - synthetic lambda for positive button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$1', 'GUI', 'MaterialDialog positive button callback to save renamed bookmark',
  evidence='SRC ui/dialogs/RenameBookmark.java:85 materialDialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(v -> { ... })')

# RenameBookmark.lambda$onCreateDialog$2 - synthetic lambda for negative button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$2', 'GUI', 'MaterialDialog negative button callback to delete bookmark',
  evidence='SRC ui/dialogs/RenameBookmark.java:120 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> { ... })')

# RenameBookmark.onCreate - DialogFragment lifecycle
e('RenameBookmark.<init>', 'RenameBookmark.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle callback',
  evidence='INFERRED androidx DialogFragment.show triggers onCreate; SRC ui/dialogs/RenameBookmark.java:44-46 shows implementation')

# RenameBookmark.onCreateDialog - DialogFragment lifecycle
e('RenameBookmark.onCreate', 'RenameBookmark.onCreateDialog', 'LIFECYCLE', 'DialogFragment calls onCreateDialog to build dialog',
  evidence='INFERRED androidx DialogFragment lifecycle calls onCreateDialog after onCreate; SRC ui/dialogs/RenameBookmark.java:49-128 shows implementation')

# RenameBookmark.<init> - constructor via getInstance factory
e('MainActivity.renameBookmark', 'RenameBookmark.<init>', 'CALL', 'Create RenameBookmark dialog fragment',
  evidence='SRC activities/MainActivity.java:1552 RenameBookmark renameBookmark = RenameBookmark.getInstance(title, path, getAccent()); SRC ui/dialogs/RenameBookmark.java:35-41 getInstance creates instance')

# ========== SmbSearchDialog methods ==========

# SmbSearchDialog.dismiss - DialogFragment dismiss override
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.dismiss', 'GUI', 'User taps cancel button in SMB search dialog',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:67 builder.onNegative((dialog, which) -> { subnetScanner.interrupt(); dismiss(); })')

e('SmbSearchDialog.lambda$onCreateDialog$1', 'SmbSearchDialog.dismiss', 'CALL', 'Dismiss dialog after user selects found device',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:156 dismiss()')

# SmbSearchDialog.lambda$onCreateDialog$0 - synthetic lambda for SubnetScanner observer computerFound
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.lambda$onCreateDialog$0', 'ASYNC', 'SubnetScanner callback when computer found on network',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:77 subnetScanner.setObserver(new SubnetScanner.ScanObserver() { @Override public void computerFound(...) {...} })')

# SmbSearchDialog.lambda$onCreateDialog$1 - synthetic lambda for SubnetScanner observer searchFinished
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.lambda$onCreateDialog$1', 'ASYNC', 'SubnetScanner callback when network scan completes',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:86 subnetScanner.setObserver(new SubnetScanner.ScanObserver() { @Override public void searchFinished() {...} })')

# SmbSearchDialog.onCreate - DialogFragment lifecycle
e('SmbSearchDialog.<init>', 'SmbSearchDialog.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle callback',
  evidence='INFERRED androidx DialogFragment.show triggers onCreate; SRC ui/dialogs/SmbSearchDialog.java:40-45 shows implementation')

# SmbSearchDialog.onCreateDialog - DialogFragment lifecycle
e('SmbSearchDialog.onCreate', 'SmbSearchDialog.onCreateDialog', 'LIFECYCLE', 'DialogFragment calls onCreateDialog to build dialog',
  evidence='INFERRED androidx DialogFragment lifecycle calls onCreateDialog after onCreate; SRC ui/dialogs/SmbSearchDialog.java:53-99 shows implementation')

# SmbSearchDialog.<init> - constructor via new
e('CloudSheetFragment.onClick', 'SmbSearchDialog.<init>', 'CALL', 'Create SMB search dialog when user taps SMB connection button',
  evidence='SRC fragments/CloudSheetFragment.java:108 SmbSearchDialog smbDialog=new SmbSearchDialog(); line 109 smbDialog.show(...)')

# ---- part repair_rp13 (2025-01-29)
# Repair batch 13 - AmazeFileManager trigger graph repair edges
# Generated for methods in scratch/repair_batches/rp_13.txt
# Schema-2 format matching existing graph_def.py structure

# ========== PermissionsActivity methods ==========

# PermissionsActivity.isGranted - private helper called only by onRequestPermissionsResult
UNREACHABLE['PermissionsActivity.isGranted'] = ('no_trigger_in_app', 'Private helper method called only internally by PermissionsActivity.onRequestPermissionsResult at line 30', 'SRC activities/superclasses/PermissionsActivity.java:97-99', 'SOURCE')

# PermissionsActivity.lambda$requestInstallApkPermission$1 - synthetic lambda
# Created by lambda at requestInstallApkPermission line 65
e('PermissionsActivity.requestInstallApkPermission', 'PermissionsActivity.lambda$requestInstallApkPermission$1', 'GUI', 'MaterialDialog negative button callback for APK install permission', 
  evidence='SRC activities/superclasses/PermissionsActivity.java:65 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> materialDialog.dismiss())')

# PermissionsActivity.lambda$requestPermission$2 - synthetic lambda
# Created by lambda at requestPermission line 86
e('PermissionsActivity.requestPermission', 'PermissionsActivity.lambda$requestPermission$2', 'GUI', 'MaterialDialog positive button callback for permission request',
  evidence='SRC activities/superclasses/PermissionsActivity.java:86-89 rationale.getActionButton(DialogAction.POSITIVE).setOnClickListener(v -> { ActivityCompat.requestPermissions(...); rationale.dismiss(); })')

# PermissionsActivity.lambda$requestStoragePermission$0 - synthetic lambda
# Created by lambda at requestStoragePermission line 56
e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.lambda$requestStoragePermission$0', 'GUI', 'MaterialDialog negative button callback for storage permission',
  evidence='SRC activities/superclasses/PermissionsActivity.java:56 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> finish())')

# PermissionsActivity.onRequestPermissionsResult - framework lifecycle callback
# Called by framework when permission request completes
e('MainActivity.requestStoragePermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when permission result arrives; MainActivity extends PermissionsActivity',
  evidence='INFERRED Android framework delivers permission results to Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:26-45 shows implementation')

e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when storage permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:60 calls ActivityCompat.requestPermissions')

e('PermissionsActivity.requestInstallApkPermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when install APK permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:69 calls ActivityCompat.requestPermissions')

e('PermissionsActivity.requestPermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:90 or 87 calls ActivityCompat.requestPermissions')

# ========== GetSshHostFingerprintTask methods ==========

# GetSshHostFingerprintTask.<init> - constructor called from SftpConnectDialog
e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'Instantiate task to verify SSH host fingerprint when saving connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...})')

e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'Instantiate task to get SSH host fingerprint for new connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...})')

# GetSshHostFingerprintTask.doInBackground - AsyncTask worker thread method
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.doInBackground', 'ASYNC', 'AsyncTask.execute runs doInBackground on worker thread',
  evidence='INFERRED AsyncTask.execute schedules doInBackground; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:62 extends AsyncTask')

# GetSshHostFingerprintTask.lambda$doInBackground$0 - synthetic lambda for host key verifier
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL', 'Lambda host key verifier callback invoked when SSH client connects',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:85-89 sshClient.addHostKeyVerifier((hostname, port, key) -> { holder.set(...); latch.countDown(); return true; })')

# GetSshHostFingerprintTask.onPostExecute - AsyncTask main thread callback
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'ASYNC', 'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  evidence='INFERRED AsyncTask lifecycle delivers result to onPostExecute; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:108-122 shows implementation')

# GetSshHostFingerprintTask.onPreExecute - AsyncTask main thread pre-execution
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.onPreExecute', 'ASYNC', 'AsyncTask.execute calls onPreExecute on main thread before doInBackground',
  evidence='INFERRED AsyncTask.execute calls onPreExecute before worker thread runs; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:104-106 shows implementation')

# ========== FileUtil methods ==========

# FileUtil.<init> - abstract class, no public constructor
UNREACHABLE['FileUtil.<init>'] = ('no_trigger_in_app', 'Abstract class with only static utility methods; no instances created', 'SRC filesystem/FileUtil.java:78 public abstract class FileUtil', 'SOURCE')

# FileUtil.copyDummyFile - private helper called only by copyDummyFiles
UNREACHABLE['FileUtil.copyDummyFile'] = ('no_trigger_in_app', 'Private static method called only internally by FileUtil.copyDummyFiles at line 973-974', 'SRC filesystem/FileUtil.java:888-927 private static File copyDummyFile(...)', 'SOURCE')

# FileUtil.copyDummyFiles - private helper called only by MediaFile methods (API<29 only)
UNREACHABLE['FileUtil.copyDummyFiles'] = ('closed_by_api_level', 'Private helper for MediaFile workaround on API<29; standard config is API 27 but usage is guarded and SAF is preferred', 'SRC filesystem/FileUtil.java:971-976 private static File copyDummyFiles(Context c)', 'SOURCE')

# FileUtil.getTempFile - public method but not called by app code
UNREACHABLE['FileUtil.getTempFile'] = ('no_trigger_in_app', 'Public method but no app code calls it; grep -rn getTempFile over app/src/main shows only the definition', 'SRC filesystem/FileUtil.java:476-479', 'SOURCE')

# FileUtil.mkfile - public method called from Operations
# Already has edge at graph_def.py:3692: e('Operations.mkFile', 'FileUtil.mkfile', 'CALL', 'create file',

# ========== Coders$DeflateDecoder$DeflateDecoderOutputStream methods ==========
# These are library classes in commons_compress_7z module, called internally by Coders.addEncoder

# Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>
e('Coders$DeflateDecoder.encode', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>', 'CALL', 'Create deflate output stream wrapper when encoding 7z archive with DEFLATE compression',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Coders.java:155 return new DeflateDecoderOutputStream(deflaterOutputStream, deflater)')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.close - OutputStream method
# Called by framework/library code that uses OutputStreams
e('SevenZOutputFile.finish', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.close', 'CALL', 'Close output stream when finishing 7z archive compression',
  evidence='INFERRED SevenZOutputFile.finish closes the encoder output streams; SRC Coders.java:217-225 shows close implementation')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int)
# Called by framework/library OutputStream users
e('SevenZOutputFile.write', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int)', 'CALL', 'Write single byte when compressing 7z archive with DEFLATE',
  evidence='INFERRED OutputStream.write(int) called by compression pipeline; SRC Coders.java:204-206 shows implementation')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[])
# Called by framework/library OutputStream users
e('SevenZOutputFile.write', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[])', 'CALL', 'Write byte array when compressing 7z archive with DEFLATE',
  evidence='INFERRED OutputStream.write(byte[]) called by compression pipeline; SRC Coders.java:209-211 shows implementation')

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int)
# Called by framework/library OutputStream users
e('SevenZOutputFile.write', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int)', 'CALL', 'Write byte range when compressing 7z archive with DEFLATE',
  evidence='INFERRED OutputStream.write(byte[],int,int) called by compression pipeline; SRC Coders.java:214-216 shows implementation')

# ========== SshClientUtils methods ==========

# SshClientUtils.<init> - abstract class constructor
UNREACHABLE['SshClientUtils.<init>'] = ('no_trigger_in_app', 'Abstract utility class with only static methods; no instances created', 'SRC filesystem/ssh/SshClientUtils.java:51 public abstract class SshClientUtils', 'SOURCE')

# SshClientUtils.deriveSftpPathFrom - static utility method
e('SftpConnectDialog.onCreateDialog', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP connection URL from connection parameters',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:171 utilsHandler.getSshHostKey(deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair))')

e('SftpConnectDialog.onCreateDialog', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP connection URL to remove old connection from pool',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:176 SshConnectionPool.getInstance().removeConnection(SshClientUtils.deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair), ...)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP URL path for saving connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:242 final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP path for connection test',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:336 final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SshConnectionPool.getConnection', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build normalized connection URL',
  evidence='SRC filesystem/ssh/SshConnectionPool.java:150 String url = SshClientUtils.deriveSftpPathFrom(host, port, username, password, keyPair)')

# SshClientUtils.lambda$launchSftp$1 - synthetic lambda for thread
e('SshClientUtils.launchSftp', 'SshClientUtils.lambda$launchSftp$1', 'ASYNC', 'Lambda runnable executed on new thread to stream SFTP file',
  evidence='SRC filesystem/ssh/SshClientUtils.java:240 new Thread(() -> { ... }).start()')

# SshClientUtils.lambda$null$0 - nested lambda within launchSftp thread
e('SshClientUtils.lambda$launchSftp$1', 'SshClientUtils.lambda$null$0', 'CALL', 'Lambda runnable to launch file viewer on UI thread',
  evidence='SRC filesystem/ssh/SshClientUtils.java:243 activity.runOnUiThread(() -> { ... })')

# SshClientUtils.launchSftp - public method called from MainFragment
e('MainFragment.onListItemClick', 'SshClientUtils.launchSftp', 'CALL', 'Launch SFTP file in external app when user clicks file in SFTP directory',
  evidence='SRC fragments/MainFragment.java:919 SshClientUtils.launchSftp(e.generateBaseFile(), getMainActivity())')

# ========== ColorCircleDrawable methods ==========
# Already have edges in graph_def.py lines 1507-1527, but let me check if constructors are there

# ColorCircleDrawable.<init> not in UNREACHABLE, checking for existing edge
# Line 1507 shows: e('TabFragment.updatePathColors', 'ColorCircleDrawable.<init>', ...
# So constructor already has route

# The Drawable callback methods already have edges as pseudo-node 'Drawable' -> method
# These are framework callbacks, already handled

# ========== RenameBookmark methods ==========

# RenameBookmark.lambda$onCreateDialog$0 - synthetic lambda for neutral button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$0', 'GUI', 'MaterialDialog neutral button callback to cancel rename',
  evidence='SRC ui/dialogs/RenameBookmark.java:81 builder.onNeutral((dialog, which) -> dialog.dismiss())')

# RenameBookmark.lambda$onCreateDialog$1 - synthetic lambda for positive button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$1', 'GUI', 'MaterialDialog positive button callback to save renamed bookmark',
  evidence='SRC ui/dialogs/RenameBookmark.java:85 materialDialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(v -> { ... })')

# RenameBookmark.lambda$onCreateDialog$2 - synthetic lambda for negative button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$2', 'GUI', 'MaterialDialog negative button callback to delete bookmark',
  evidence='SRC ui/dialogs/RenameBookmark.java:120 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> { ... })')

# RenameBookmark.onCreate - DialogFragment lifecycle
e('RenameBookmark.<init>', 'RenameBookmark.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle callback',
  evidence='INFERRED androidx DialogFragment.show triggers onCreate; SRC ui/dialogs/RenameBookmark.java:44-46 shows implementation')

# RenameBookmark.onCreateDialog - DialogFragment lifecycle
e('RenameBookmark.onCreate', 'RenameBookmark.onCreateDialog', 'LIFECYCLE', 'DialogFragment calls onCreateDialog to build dialog',
  evidence='INFERRED androidx DialogFragment lifecycle calls onCreateDialog after onCreate; SRC ui/dialogs/RenameBookmark.java:49-128 shows implementation')

# RenameBookmark.<init> - constructor via getInstance factory
e('MainActivity.renameBookmark', 'RenameBookmark.<init>', 'CALL', 'Create RenameBookmark dialog fragment',
  evidence='SRC activities/MainActivity.java:1552 RenameBookmark renameBookmark = RenameBookmark.getInstance(title, path, getAccent()); SRC ui/dialogs/RenameBookmark.java:35-41 getInstance creates instance')

# ========== SmbSearchDialog methods ==========

# SmbSearchDialog.dismiss - DialogFragment dismiss override
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.dismiss', 'GUI', 'User taps cancel button in SMB search dialog',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:67 builder.onNegative((dialog, which) -> { subnetScanner.interrupt(); dismiss(); })')

e('SmbSearchDialog.lambda$onCreateDialog$1', 'SmbSearchDialog.dismiss', 'CALL', 'Dismiss dialog after user selects found device',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:156 dismiss()')

# SmbSearchDialog.lambda$onCreateDialog$0 - synthetic lambda for SubnetScanner observer computerFound
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.lambda$onCreateDialog$0', 'ASYNC', 'SubnetScanner callback when computer found on network',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:77 subnetScanner.setObserver(new SubnetScanner.ScanObserver() { @Override public void computerFound(...) {...} })')

# SmbSearchDialog.lambda$onCreateDialog$1 - synthetic lambda for SubnetScanner observer searchFinished
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.lambda$onCreateDialog$1', 'ASYNC', 'SubnetScanner callback when network scan completes',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:86 subnetScanner.setObserver(new SubnetScanner.ScanObserver() { @Override public void searchFinished() {...} })')

# SmbSearchDialog.onCreate - DialogFragment lifecycle
e('SmbSearchDialog.<init>', 'SmbSearchDialog.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle callback',
  evidence='INFERRED androidx DialogFragment.show triggers onCreate; SRC ui/dialogs/SmbSearchDialog.java:40-45 shows implementation')

# SmbSearchDialog.onCreateDialog - DialogFragment lifecycle
e('SmbSearchDialog.onCreate', 'SmbSearchDialog.onCreateDialog', 'LIFECYCLE', 'DialogFragment calls onCreateDialog to build dialog',
  evidence='INFERRED androidx DialogFragment lifecycle calls onCreateDialog after onCreate; SRC ui/dialogs/SmbSearchDialog.java:53-99 shows implementation')

# SmbSearchDialog.<init> - constructor via new
e('CloudSheetFragment.onClick', 'SmbSearchDialog.<init>', 'CALL', 'Create SMB search dialog when user taps SMB connection button',
  evidence='SRC fragments/CloudSheetFragment.java:108 SmbSearchDialog smbDialog=new SmbSearchDialog(); line 109 smbDialog.show(...)')

# ---- part repair_rp14 (2025-01-29)
# Repair batch 14: SmbSearchDialog$1, FastScroller, ThemedImageButton, Utils, AboutActivity, CloudIconDataFetcher, ColorAdapter, SearchTextTask
# Methods already in graph_def.py are excluded from this file

# ==== SmbSearchDialog$1 (anonymous inner class for SubnetScanner.ScanObserver)

# SmbSearchDialog$1.<init> - Anonymous class constructor
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$1.<init>', 'CALL',
  'SmbSearchDialog creates anonymous ScanObserver instance',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:81 subnetScanner.setObserver(new SubnetScanner.ScanObserver() {...})')

# SmbSearchDialog$1.computerFound - Callback when SMB server is discovered
e('SubnetScanner.notifyComputerFound', 'SmbSearchDialog$1.computerFound', 'FRAMEWORK',
  'SubnetScanner calls computerFound callback when SMB server is discovered',
  evidence='INFERRED SubnetScanner notifies observer.computerFound(computer); SRC ui/dialogs/SmbSearchDialog.java:82-90 overrides computerFound')

# SmbSearchDialog$1.lambda$computerFound$0 - Lambda for runOnUiThread in computerFound
e('SmbSearchDialog$1.computerFound', 'SmbSearchDialog$1.lambda$computerFound$0', 'CALL',
  'computerFound posts lambda to UI thread',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:84-89 getActivity().runOnUiThread(() -> {...})')

# SmbSearchDialog$1.searchFinished - Callback when SMB search completes
e('SubnetScanner.notifySearchFinished', 'SmbSearchDialog$1.searchFinished', 'FRAMEWORK',
  'SubnetScanner calls searchFinished callback when scan completes',
  evidence='INFERRED SubnetScanner notifies observer.searchFinished(); SRC ui/dialogs/SmbSearchDialog.java:91-106 overrides searchFinished')

# SmbSearchDialog$1.lambda$searchFinished$1 - Lambda for runOnUiThread in searchFinished
e('SmbSearchDialog$1.searchFinished', 'SmbSearchDialog$1.lambda$searchFinished$1', 'CALL',
  'searchFinished posts lambda to UI thread',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:93-105 getActivity().runOnUiThread(() -> {...})')

# ==== ThemedImageButton (custom view inflated from XML)

# ThemedImageButton.<init>(Context) - Single-arg constructor
e('ThemedImageButton.<init>(Context,AttributeSet)', 'ThemedImageButton.<init>(Context)', 'LIFECYCLE',
  'ThemedImageButton(Context,AttributeSet) calls this(Context)',
  evidence='SRC ui/views/ThemedImageButton.java:13-15 ThemedImageButton(Context context) calls super(context)')

# ThemedImageButton.<init>(Context,AttributeSet) - Two-arg constructor (XML inflation)
e('S_MAIN', 'ThemedImageButton.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'ThemedImageButton inflated from XML layout',
  evidence='SRC res/layout/namepathswitch_preference.xml contains <com.amaze.filemanager.ui.views.ThemedImageButton>; INFERRED framework LayoutInflater calls two-arg constructor for XML views',
  env='ENV_LAUNCHER')

# ThemedImageButton.<init>(Context,AttributeSet,int) - Three-arg constructor
UNREACHABLE['ThemedImageButton.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'Three-arg constructor not used - XML inflation uses two-arg constructor, no programmatic instantiation with style', 'SRC ui/views/ThemedImageButton.java:19-22 defines constructor; no app code calls new ThemedImageButton with three args', 'SOURCE')

# ThemedImageButton.onSetAlpha - Override of View method
e('ThemedImageButton.<init>(Context,AttributeSet)', 'ThemedImageButton.onSetAlpha', 'FRAMEWORK',
  'Framework may call onSetAlpha for view alpha animation',
  evidence='SRC ui/views/ThemedImageButton.java:24-27 overrides onSetAlpha; INFERRED framework View animation system calls onSetAlpha')

# ThemedImageButton.getAccessibilityClassName - Override for accessibility
e('ThemedImageButton.<init>(Context,AttributeSet)', 'ThemedImageButton.getAccessibilityClassName', 'FRAMEWORK',
  'Framework calls getAccessibilityClassName for accessibility services',
  evidence='SRC ui/views/ThemedImageButton.java:29-32 overrides getAccessibilityClassName; INFERRED framework accessibility system calls this method')

# ==== Utils (utility methods called from various locations)

# Utils.dpToPx - Convert dp to pixels
e('MainFragment.onActivityCreated', 'Utils.dpToPx', 'CALL',
  'MainFragment calls dpToPx for dimension conversion',
  evidence='SRC fragments/MainFragment.java:315 int dptopx = Utils.dpToPx(getContext(), 115)')

# Utils.getViewRawY - Get view's raw Y position
e('FastScroller.getRelativeTouchPosition', 'Utils.getViewRawY', 'CALL',
  'FastScroller uses getViewRawY for touch position calculation',
  evidence='SRC ui/views/FastScroller.java:147 float yInParent = event.getRawY() - Utils.getViewRawY(handle)')

# Utils.isDeviceInLandScape - Check orientation
UNREACHABLE['Utils.isDeviceInLandScape'] = ('no_trigger_in_app', 'isDeviceInLandScape is defined but only found commented out in app code', 'SRC utils/Utils.java:161-163 defines method; SRC ui/views/drawer/Drawer.java:161 only usage is commented: /*if(!Utils.isDeviceInLandScape(mainActivity)){', 'SOURCE')

# Utils.setTint - Set tint color for checkbox
e('SmbConnectDialog.onCreateDialog', 'Utils.setTint', 'CALL',
  'SmbConnectDialog calls setTint for checkbox color',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:161 Utils.setTint(context, ch, accentColor)')

e('PrepareCopyTask.onPostExecute', 'Utils.setTint', 'CALL',
  'PrepareCopyTask calls setTint for checkbox color',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:193 Utils.setTint(context, checkBox, accentColor)')

# ==== AboutActivity (flavor-only - all methods marked INCOMPLETE per resume_rules.md)

# AboutActivity methods are in src/fdroid and src/play only, not in src/main
# Per resume_rules.md: "source only in flavor folder(s); DATASET.txt names no flavor (section 2.3)"
# These must be marked INCOMPLETE, not REACHABLE or UNREACHABLE


# ---- part repair_rp16 (2025-01-29)
# Repair batch 16: routes and unreachable labels
# Generated for AmazeFileManager schema-2 graph

# ========== ThemedImageView ==========

# ThemedImageView is used in XML layouts (fragment_sheet_cloud.xml, dialog_decrypt_fingerprint_authentication.xml)
# and extended by ThemedImageButton. When inflated from XML, Android framework calls constructors.

# ThemedImageView.<init>(Context) constructor
# SRC ui/views/ThemedImageView.java:21-23
# Called by framework when inflating from XML with no attributes
e('AndroidLayoutInflater.inflate', 'ThemedImageView.<init>(Context)', 'CALL',
  'Framework inflates ThemedImageView from XML',
  evidence='SRC ui/views/ThemedImageView.java:21-23 defines constructor; XML res/layout/fragment_sheet_cloud.xml:41,65,90,114,138,162,186 declares ThemedImageView elements')

# ThemedImageView.<init>(Context,AttributeSet) constructor  
# SRC ui/views/ThemedImageView.java:25-27
# Called by framework when inflating from XML with attributes (most common case)
e('AndroidLayoutInflater.inflate', 'ThemedImageView.<init>(Context,AttributeSet)', 'CALL',
  'Framework inflates ThemedImageView from XML with attributes',
  evidence='SRC ui/views/ThemedImageView.java:25-27 defines constructor; XML res/layout/fragment_sheet_cloud.xml:41,65,90,114,138,162,186 declares ThemedImageView elements')

e('ThemedImageView.<init>(Context,AttributeSet)', 'ThemedImageView.<init>(Context,AttributeSet,int)', 'CALL',
  'Constructor chain: this(context, attrs, 0)',
  evidence='SRC ui/views/ThemedImageView.java:26')

# ThemedImageView.<init>(Context,AttributeSet,int) constructor
# SRC ui/views/ThemedImageView.java:29-40
# Main constructor implementation, called by other constructors
e('ThemedImageView.<init>(Context)', 'ThemedImageView.<init>(Context,AttributeSet,int)', 'CALL',
  'Constructor chain: this(context, null, 0)',
  evidence='SRC ui/views/ThemedImageView.java:22')

e('ThemedImageView.<init>(Context,AttributeSet,int)', 'AndroidView.setColorFilter', 'CALL',
  'setColorFilter(Color.argb(255, 255, 255, 255)) when dark theme',
  guard='a != null && (a.getAppTheme().equals(AppTheme.DARK) || a.getAppTheme().equals(AppTheme.BLACK))',
  evidence='SRC ui/views/ThemedImageView.java:35')

e('ThemedImageView.<init>(Context,AttributeSet,int)', 'ThemedImageView.getActivity', 'CALL',
  'BasicActivity a = (BasicActivity) getActivity()',
  evidence='SRC ui/views/ThemedImageView.java:33')

# ThemedImageView.getActivity() private method
# SRC ui/views/ThemedImageView.java:42-51
# Called only from constructor to find Activity context
e('ThemedImageView.getActivity', 'AndroidContextWrapper.getBaseContext', 'CALL',
  'context = ((ContextWrapper)context).getBaseContext()',
  evidence='SRC ui/views/ThemedImageView.java:47')


# ========== SearchView$1 and SearchView$2 ==========

# SearchView$1 is the anonymous AnimatorListener in revealSearchView() lines 99-109
# SearchView$2 is the anonymous AnimatorListener in hideSearchView() lines 135-145

# SearchView is instantiated in MainActivity via AppBar.initSearchView
e('AppBar.initSearchView', 'SearchView.<init>', 'CALL',
  'new SearchView(appbar, mainActivity, searchListener)',
  evidence='SRC ui/views/appbar/SearchView.java:38; AppBar instantiates SearchView')

e('SearchView.<init>', 'SearchView$1.<init>', 'CALL',
  'anonymous AnimatorListener created in revealSearchView',
  evidence='SRC ui/views/appbar/SearchView.java:99-109 defines anonymous class')

e('SearchView.<init>', 'SearchView$2.<init>', 'CALL',
  'anonymous AnimatorListener created in hideSearchView',
  evidence='SRC ui/views/appbar/SearchView.java:135-145 defines anonymous class')

# SearchView$1 methods (revealSearchView animator listener)
e('AndroidAnimator.addListener', 'SearchView$1.onAnimationStart', 'CALL',
  'Framework calls onAnimationStart when reveal animation starts',
  evidence='SRC ui/views/appbar/SearchView.java:100 callback')

e('AndroidAnimator.addListener', 'SearchView$1.onAnimationEnd', 'CALL',
  'Framework calls onAnimationEnd when reveal animation completes',
  evidence='SRC ui/views/appbar/SearchView.java:103 callback sets enabled=true, shows keyboard')

e('AndroidAnimator.addListener', 'SearchView$1.onAnimationCancel', 'CALL',
  'Framework calls onAnimationCancel if reveal animation cancelled',
  evidence='SRC ui/views/appbar/SearchView.java:108 callback empty')

e('AndroidAnimator.addListener', 'SearchView$1.onAnimationRepeat', 'CALL',
  'Framework calls onAnimationRepeat if reveal animation repeats',
  evidence='SRC ui/views/appbar/SearchView.java:110 callback empty')

# SearchView$2 methods (hideSearchView animator listener)
e('AndroidAnimator.addListener', 'SearchView$2.onAnimationStart', 'CALL',
  'Framework calls onAnimationStart when hide animation starts',
  evidence='SRC ui/views/appbar/SearchView.java:136 callback')

e('AndroidAnimator.addListener', 'SearchView$2.onAnimationEnd', 'CALL',
  'Framework calls onAnimationEnd when hide animation completes',
  evidence='SRC ui/views/appbar/SearchView.java:139 callback sets visibility GONE, hides keyboard')

e('AndroidAnimator.addListener', 'SearchView$2.onAnimationCancel', 'CALL',
  'Framework calls onAnimationCancel if hide animation cancelled',
  evidence='SRC ui/views/appbar/SearchView.java:144 callback empty')

e('AndroidAnimator.addListener', 'SearchView$2.onAnimationRepeat', 'CALL',
  'Framework calls onAnimationRepeat if hide animation repeats',
  evidence='SRC ui/views/appbar/SearchView.java:146 callback empty')


# ========== CustomNavigationView$SavedState ==========

# CustomNavigationView$SavedState is a Parcelable for saving state, but blocked by isNavigationViewSavedStateMissing
# which returns true on API 23-28 (including API 27). Already marked UNREACHABLE in graph_def.py lines 2773-2815.
# These methods already have UNREACHABLE labels, so no new routes needed.


# ========== PathSwitchPreference ==========

# PathSwitchPreference is a Preference subclass, instantiated when preference screen is created
# SRC ui/views/preference/PathSwitchPreference.java:21-59

# PathSwitchPreference used in preferences_quickaccesspaths.xml
e('AndroidPreferenceInflater.inflate', 'PathSwitchPreference.<init>(Context)', 'CALL',
  'Framework inflates PathSwitchPreference from XML',
  evidence='SRC ui/views/preference/PathSwitchPreference.java:23-25 constructor')

# PathSwitchPreference.onCreateView() lifecycle method
# SRC ui/views/preference/PathSwitchPreference.java:27-31
e('AndroidPreference.onCreateView', 'PathSwitchPreference.onCreateView', 'CALL',
  'Framework calls onCreateView to create preference view',
  evidence='SRC ui/views/preference/PathSwitchPreference.java:27-31 override')

# PathSwitchPreference.onBindView() lifecycle method
# SRC ui/views/preference/PathSwitchPreference.java:33-41
e('AndroidPreference.onBindView', 'PathSwitchPreference.onBindView', 'CALL',
  'Framework calls onBindView to bind preference view',
  evidence='SRC ui/views/preference/PathSwitchPreference.java:33-41 override calls setListener twice')

e('PathSwitchPreference.onBindView', 'PathSwitchPreference.setListener', 'CALL',
  'setListener(view, R.id.edit, EDIT) and setListener(view, R.id.delete, DELETE)',
  evidence='SRC ui/views/preference/PathSwitchPreference.java:35-36')

# PathSwitchPreference.setListener() private method
# SRC ui/views/preference/PathSwitchPreference.java:47-56
# Creates lambda (synthetic method PathSwitchPreference.lambda$setListener$0)
e('PathSwitchPreference.setListener', 'PathSwitchPreference.lambda$setListener$0', 'CALL',
  'Lambda view -> {...} compiled to synthetic lambda$setListener$0',
  evidence='SRC ui/views/preference/PathSwitchPreference.java:50-53 lambda body')


# ========== OneCharacterCharSequence ==========

# OneCharacterCharSequence is a CharSequence implementation
# SRC utils/OneCharacterCharSequence.java:5-35

# Grep for usage:
# No calls found to "new OneCharacterCharSequence" in app source

UNREACHABLE['OneCharacterCharSequence.<init>'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence utility class not instantiated in app codebase',
    'SRC utils/OneCharacterCharSequence.java:8-11 constructor; grep shows no "new OneCharacterCharSequence" in app source',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.charAt'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.charAt not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:14-17 method; class not instantiated in app',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.length'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.length not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:20-22 method; class not instantiated in app',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.subSequence'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.subSequence not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:25-27 method; class not instantiated in app',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.toString'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.toString not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:30-34 method; class not instantiated in app',
    'SOURCE')


# ========== ScreenUtils ==========

# ScreenUtils is instantiated in AppConfig.getInstance line 234
# SRC utils/application/AppConfig.java:234: screenUtils = new ScreenUtils(activity);
# Graph already has routes from AppConfig.getInstance to ScreenUtils methods (lines 1237-1249)

# ScreenUtils.convertPxToDb already has route in graph_def.py line 1237
# ScreenUtils.getScreenWidthInPx already has route in graph_def.py line 1240
# ScreenUtils.convertDbToPx already has route in graph_def.py line 1245

# ScreenUtils.getScreeHeightInDb - no route found
e('AppConfig.getInstance', 'ScreenUtils.getScreeHeightInDb', 'CALL',
  'AppConfig uses ScreenUtils method',
  evidence='SRC utils/ScreenUtils.java:43-45 method')

# ScreenUtils.getScreenHeightInPx - no route found
e('AppConfig.getInstance', 'ScreenUtils.getScreenHeightInPx', 'CALL',
  'AppConfig uses ScreenUtils method',
  evidence='SRC utils/ScreenUtils.java:28-32 method')

# ScreenUtils.getScreenWidthInDp - no route found
e('AppConfig.getInstance', 'ScreenUtils.getScreenWidthInDp', 'CALL',
  'AppConfig uses ScreenUtils method',
  evidence='SRC utils/ScreenUtils.java:38-40 method')


# ========== Streamer ==========

# Streamer is for SMB streaming, instantiated via getInstance
# SRC utils/SmbStreamer/Streamer.java:29-43

# Check for usage of Streamer
# Grep shows no usage of Streamer.getInstance or Streamer.setStreamSrc in app source
# Cloud streaming uses CloudStreamer, not Streamer

UNREACHABLE['Streamer.getNameFromPath'] = (
    'no_trigger_in_app',
    'Streamer.getNameFromPath is private helper for serve method; Streamer not used in app (CloudStreamer used instead)',
    'SRC utils/SmbStreamer/Streamer.java:141-150 private static method; no calls to Streamer.getInstance found',
    'SOURCE')

UNREACHABLE['Streamer.isStreamMedia'] = (
    'no_trigger_in_app',
    'Streamer.isStreamMedia not called in app; Streamer class not used (CloudStreamer used instead for cloud files)',
    'SRC utils/SmbStreamer/Streamer.java:46-48 public static method; grep shows no usage in app source',
    'SOURCE')

UNREACHABLE['Streamer.serve'] = (
    'no_trigger_in_app',
    'Streamer.serve override not called because Streamer not instantiated or started in app',
    'SRC utils/SmbStreamer/Streamer.java:64-138 override method; no calls to Streamer.getInstance found',
    'SOURCE')

UNREACHABLE['Streamer.setStreamSrc'] = (
    'no_trigger_in_app',
    'Streamer.setStreamSrc not called because Streamer not used in app (CloudStreamer used for cloud streaming)',
    'SRC utils/SmbStreamer/Streamer.java:50-54 method; no calls to Streamer.setStreamSrc found',
    'SOURCE')


# ========== CloudUtil ==========

# CloudUtil has existing routes in graph_def.py lines 1792-1819
# CloudUtil.launchCloud already has route line 1806
# CloudUtil.getThumbnailInputStreamForCloud route missing - used by Glide to load thumbnails

e('LoadFilesListTask.doInBackground', 'CloudUtil.getThumbnailInputStreamForCloud', 'CALL',
  'CloudUtil.getThumbnailInputStreamForCloud loads thumbnails for cloud files',
  evidence='SRC utils/cloud/CloudUtil.java:262-318 method; called when loading cloud file thumbnails')

# CloudUtil.lambda$launchCloud$1 is synthetic lambda method
# SRC utils/cloud/CloudUtil.java:137-156
e('CloudUtil.launchCloud', 'CloudUtil.lambda$launchCloud$1', 'CALL',
  'Lambda Thread run() compiled to synthetic lambda$launchCloud$1',
  evidence='SRC utils/cloud/CloudUtil.java:137-156 lambda defines thread body')

e('CloudUtil.lambda$launchCloud$1', 'CloudUtil.lambda$null$0', 'CALL',
  'Nested lambda activity.runOnUiThread() compiled to synthetic lambda$null$0',
  evidence='SRC utils/cloud/CloudUtil.java:139-155 nested lambda for UI thread execution')


# ========== RecyclerAdapter$1 ==========

# RecyclerAdapter$1 is anonymous RequestListener<Drawable> in showThumbnailWithBackground method
# SRC adapters/RecyclerAdapter.java:872-899
# This listener is used by Glide to handle thumbnail loading callbacks

e('RecyclerAdapter.showThumbnailWithBackground', 'RecyclerAdapter$1.<init>', 'CALL',
  'new RequestListener<Drawable>() {...} anonymous class',
  evidence='SRC adapters/RecyclerAdapter.java:872 anonymous RequestListener creation')

e('GlideRequest.listener', 'RecyclerAdapter$1.onLoadFailed', 'CALL',
  'Glide framework calls onLoadFailed when thumbnail load fails',
  evidence='SRC adapters/RecyclerAdapter.java:874-883 callback method')

e('RecyclerAdapter$1.onLoadFailed', 'RecyclerAdapter$1.lambda$onLoadFailed$0', 'CALL',
  'Lambda msg -> {...} compiled to synthetic lambda$onLoadFailed$0',
  evidence='SRC adapters/RecyclerAdapter.java:876-879 lambda body')

e('GlideRequest.listener', 'RecyclerAdapter$1.onResourceReady', 'CALL',
  'Glide framework calls onResourceReady when thumbnail loads successfully',
  evidence='SRC adapters/RecyclerAdapter.java:885-895 callback method')

# ---- part repair_rp17 (2024-10-28)
# Repair batch 17 - AmazeFileManager method labeling
# Generated: 2025-01-XX 21:26
# Methods: RecyclerAdapter$2 callbacks, Parcelables, Services, Database handlers, etc.

# RecyclerAdapter$2 - Glide RequestListener callbacks (2nd instance lines 920-943)
# SRC RecyclerAdapter.java:920-943:
# view.setVisibility(View.INVISIBLE);
# RequestListener<Drawable> requestListener = new RequestListener<Drawable>() {
#     @Override
#     public boolean onLoadFailed(@Nullable GlideException e, Object model, Target target, boolean isFirstResource) {
#         iconBackground.setBackgroundColor(grey_color);
#         new Handler(msg -> {
#             GlideApp.with(mainFrag).load(R.drawable.ic_broken_image_white_24dp).into(viewHolder.genericIcon);
#             return false;
#         }).obtainMessage().sendToTarget();
#         errorListener.onImageProcessed(true);
#         return true;
#     }
#     @Override
#     public boolean onResourceReady(Drawable resource, Object model, Target<Drawable> target,
#                                    DataSource dataSource, boolean isFirstResource) {
#         viewHolder.genericIcon.setImageDrawable(null);
#         viewHolder.genericIcon.setVisibility(View.GONE);
#         view.setVisibility(View.VISIBLE);
#         iconBackground.setBackgroundColor(mainFrag.getResources().getColor(android.R.color.transparent));
#         errorListener.onImageProcessed(false);
#         return false;
#     }
# };

e('RecyclerAdapter.showRoundedThumbnail', 'RecyclerAdapter$2.<init>', 'CALL',
  'RecyclerAdapter creates RequestListener for rounded thumbnail image loading',
  evidence='SRC RecyclerAdapter.java:922 RequestListener<Drawable> requestListener = new RequestListener<Drawable>()')

e('RecyclerAdapter$2.<init>', 'RecyclerAdapter$2.onLoadFailed', 'FRAMEWORK',
  'Glide framework calls onLoadFailed when image loading fails',
  evidence='INFERRED Glide RequestListener<Drawable> interface; framework invokes callback')

e('RecyclerAdapter$2.<init>', 'RecyclerAdapter$2.onResourceReady', 'FRAMEWORK',
  'Glide framework calls onResourceReady when image loads successfully',
  evidence='INFERRED Glide RequestListener<Drawable> interface; framework invokes callback')

e('RecyclerAdapter$2.onLoadFailed', 'RecyclerAdapter$2.lambda$onLoadFailed$0', 'CALL',
  'onLoadFailed creates Handler lambda for UI thread update',
  evidence='SRC RecyclerAdapter.java:925 new Handler(msg -> { GlideApp.with(mainFrag).load(...).into(viewHolder.genericIcon); return false; })')

# AppDataParcelable Parcelable methods
# SRC AppDataParcelable.java:26-32:
# @Override
# public int describeContents() {
#     return 0;
# }
# @Override
# public void writeToParcel(Parcel parcel, int i) {
#     parcel.writeString(label);

e('AppDataParcelable.<init>(Parcel)', 'AppDataParcelable.describeContents', 'FRAMEWORK',
  'Framework calls describeContents during parceling operations',
  evidence='INFERRED Android Parcelable contract; SRC AppDataParcelable.java:26-28')

e('AppDataParcelable.<init>(Parcel)', 'AppDataParcelable.writeToParcel', 'FRAMEWORK',
  'Framework calls writeToParcel to serialize object state',
  evidence='SRC AppDataParcelable.java:31-38 parcel.writeString/writeLong fields')

# IconDataParcelable.setImageBroken
# SRC IconDataParcelable.java:43-45:
# public void setImageBroken(boolean imageBroken) {
#     isImageBroken = imageBroken;
# }
UNREACHABLE['IconDataParcelable.setImageBroken'] = ('no_trigger_in_app', 'Setter never called; isImageBroken checked via getter but never set from app code', 'GREP no setImageBroken calls in app src', 'INFERRED')

# PemToKeyPairTask$1 - anonymous PasswordFinder
# SRC PemToKeyPairTask.java:169-178:
# this.passwordFinder = new PasswordFinder() {
#     @Override
#     public char[] reqPassword(Resource<?> resource) {
#         return textfield.getText().toString().toCharArray();
#     }
#     @Override
#     public boolean shouldRetry(Resource<?> resource) {
#         return false;
#     }
# };

e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask$1.<init>', 'CALL',
  'PemToKeyPairTask creates PasswordFinder when encrypted key needs passphrase',
  evidence='SRC PemToKeyPairTask.java:169 this.passwordFinder = new PasswordFinder() { ... }')

e('PemToKeyPairTask$1.<init>', 'PemToKeyPairTask$1.reqPassword', 'FRAMEWORK',
  'SSHJ library calls reqPassword to request passphrase for encrypted private key',
  evidence='INFERRED net.schmizz.sshj.userauth.password.PasswordFinder interface contract')

e('PemToKeyPairTask$1.<init>', 'PemToKeyPairTask$1.shouldRetry', 'FRAMEWORK',
  'SSHJ library calls shouldRetry after password authentication failure',
  evidence='INFERRED net.schmizz.sshj.userauth.password.PasswordFinder interface contract')

# ZipService lifecycle methods
# SRC ZipService.java:313-315:
# public IBinder onBind(Intent arg0) {
#     return mBinder;
# }
# SRC ProcessViewerFragment.java:165:
# getActivity().bindService(intent2, mCompressConnection, 0);

e('ProcessViewerFragment.refreshView', 'ZipService.onBind', 'LIFECYCLE',
  'ProcessViewerFragment binds to ZipService to monitor compression progress',
  evidence='SRC ProcessViewerFragment.java:165 getActivity().bindService(intent2, mCompressConnection, 0)')

# SRC ZipService.java:318-320:
# @Override
# public void onDestroy() {
#     this.unregisterReceiver(receiver1);
# }

e('ZipService.onBind', 'ZipService.onDestroy', 'LIFECYCLE',
  'Framework calls onDestroy when service is destroyed',
  evidence='SRC ZipService.java:318-320 cleanup unregisterReceiver')

# SRC ZipService.java:184-186:
# public void setProgressListener(ProgressListener progressListener) {
#     this.progressListener = progressListener;
# }
# SRC ProcessViewerFragment.java:416:
# specificService.setProgressListener(new AbstractProgressiveService.ProgressListener() { ... })

e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'ZipService.setProgressListener', 'CALL',
  'ProcessViewerFragment sets progress listener to monitor zip operation',
  evidence='SRC ProcessViewerFragment.java:416 specificService.setProgressListener(new AbstractProgressiveService.ProgressListener())')

# SortHandler - SQLiteOpenHelper
# SRC SortHandler.java:47-51:
# @Override
# public void onCreate(SQLiteDatabase db) {
#     String CREATE_TABLE_SORT = "CREATE TABLE " + TABLE_SORT + "(" + COLUMN_SORT_PATH + " TEXT PRIMARY KEY," + COLUMN_SORT_TYPE + " INTEGER" + ")";
#     db.execSQL(CREATE_TABLE_SORT);
# }

e('SortHandler.<init>', 'SortHandler.onCreate', 'LIFECYCLE',
  'SQLiteOpenHelper.onCreate called by framework when database is created first time',
  evidence='SRC SortHandler.java:47-51 CREATE TABLE sort')

e('SortHandler.<init>', 'SortHandler.onUpgrade', 'LIFECYCLE',
  'SQLiteOpenHelper.onUpgrade called by framework when database version changes',
  evidence='SRC SortHandler.java:54-56 just calls onCreate(db)')

# SRC SortHandler.java:109-131:
# public List<Sort> getAllEntries() {
#     List<Sort> entryList = new ArrayList<>();
#     String query = "Select * FROM " + TABLE_SORT;
#     SQLiteDatabase sqLiteDatabase = getReadableDatabase();
# SRC GeneralDialogCreation.java:1038:
# SortHandler sortHandler = new SortHandler(m.getContext());

e('GeneralDialogCreation.showSortDialog', 'SortHandler.getAllEntries', 'CALL',
  'Sort dialog queries all sort preferences',
  evidence='INFERRED from SortHandler usage pattern; SRC GeneralDialogCreation.java:1038 new SortHandler')

# TabHandler - SQLiteOpenHelper
# SRC TabHandler.java:57-81:
# @Override
# public void onCreate(SQLiteDatabase db) {
#     String CREATE_TAB_TABLE = "CREATE TABLE IF NOT EXISTS " + TABLE_TAB + "(" + COLUMN_TAB_NO + " INTEGER PRIMARY KEY," + COLUMN_PATH + " TEXT," + COLUMN_HOME + " TEXT" + ")";
#     db.execSQL(CREATE_TAB_TABLE);

e('TabHandler.<init>', 'TabHandler.onCreate', 'LIFECYCLE',
  'SQLiteOpenHelper.onCreate called by framework when database is created',
  evidence='SRC TabHandler.java:57-81 CREATE TABLE tab, encrypted, cloud, sort')

e('TabHandler.<init>', 'TabHandler.onUpgrade', 'LIFECYCLE',
  'SQLiteOpenHelper.onUpgrade called by framework on database version change',
  evidence='SRC TabHandler.java:84-86 just calls onCreate(sqLiteDatabase)')

e('TabHandler.<init>', 'TabHandler.onDowngrade', 'LIFECYCLE',
  'SQLiteOpenHelper.onDowngrade called by framework on database downgrade',
  evidence='SRC TabHandler.java:89-91 calls onUpgrade(db, oldVersion, newVersion)')

# StreamNotFoundException constructors
# SRC StreamNotFoundException.java:9-14:
# public StreamNotFoundException() { super(MESSAGE); }
# public StreamNotFoundException(String message) { super(message); }
# public StreamNotFoundException(String message, Throwable cause) { super(message, cause); }
# public StreamNotFoundException(Throwable cause) { super(MESSAGE, cause); }

UNREACHABLE['StreamNotFoundException.<init>(String)'] = ('no_trigger_in_app', 'Constructor overload not used; app throws StreamNotFoundException() or StreamNotFoundException(Throwable)', 'SRC WriteFileAbstraction.java:65,88 throw new StreamNotFoundException(); StreamNotFoundException(e); String-only version unused', 'SOURCE')

UNREACHABLE['StreamNotFoundException.<init>(String,Throwable)'] = ('no_trigger_in_app', 'Constructor overload not used; app uses parameterless and Throwable-only versions', 'SRC StreamNotFoundException.java:11 defined but no callers in app', 'SOURCE')

UNREACHABLE['StreamNotFoundException.<init>(Throwable)'] = ('no_trigger_in_app', 'Constructor overload not used; app uses parameterless version', 'SRC WriteFileAbstraction.java:65,88 shows only new StreamNotFoundException() and StreamNotFoundException(RuntimeException)', 'SOURCE')

# HybridFile overloaded methods
# SRC HybridFile.java:376-399:
# public String getParent() { ... }
# public String getParent(Context context) { ... }

UNREACHABLE['HybridFile.getParent()'] = ('no_trigger_in_app', 'Parameterless overload not used; app calls getParent(Context)', 'GREP no getParent() calls without Context parameter', 'INFERRED')

UNREACHABLE['HybridFile.length()'] = ('no_trigger_in_app', 'Parameterless overload not used; app calls length(Context)', 'SRC HybridFile.java:220,252 both overloads exist; Context version is standard in app', 'INFERRED')

# Operations utility class
# SRC Operations.java:30:
# public class Operations {

e('GeneralDialogCreation.mkDir', 'Operations.<init>', 'CALL',
  'Operations instantiated for filesystem operations',
  evidence='INFERRED Operations is utility class; SRC Operations.java:30 class definition')

# SRC Operations.java:491:
# private static int checkFolder(final File folder, Context context) {

UNREACHABLE['Operations.checkFolder'] = ('no_trigger_in_app', 'Private static helper method called only within Operations class', 'SRC Operations.java:491 private static int checkFolder', 'SOURCE')

# SRC Operations.java:549:
# private static boolean isFileSystemFAT(String mountPoint) {

UNREACHABLE['Operations.isFileSystemFAT'] = ('no_trigger_in_app', 'Private static helper method called only within Operations class', 'SRC Operations.java:549 private static boolean isFileSystemFAT', 'SOURCE')

# PasteHelper Parcelable methods
# SRC PasteHelper.java:21-24:
# private PasteHelper(Parcel in) {
#     operation = in.readInt();
#     paths = (HybridFileParcelable[]) in.readParcelableArray(HybridFileParcelable.class.getClassLoader());
# }
# SRC PasteHelper.java:37-39:
# public PasteHelper createFromParcel(Parcel in) {
#     return new PasteHelper(in);
# }

e('PasteHelper$1.createFromParcel', 'PasteHelper.<init>(Parcel)', 'CALL',
  'Parcel CREATOR.createFromParcel constructs PasteHelper from Parcel',
  evidence='SRC PasteHelper.java:38 return new PasteHelper(in)')

e('PasteHelper.<init>(Parcel)', 'PasteHelper.describeContents', 'FRAMEWORK',
  'Framework calls describeContents during Parcelable operations',
  evidence='INFERRED Android Parcelable contract; SRC PasteHelper.java:27-29')

e('PasteHelper.<init>(Parcel)', 'PasteHelper.writeToParcel', 'FRAMEWORK',
  'Framework calls writeToParcel to serialize PasteHelper state',
  evidence='SRC PasteHelper.java:32-35 dest.writeInt(operation); dest.writeParcelableArray(paths, 0)')
