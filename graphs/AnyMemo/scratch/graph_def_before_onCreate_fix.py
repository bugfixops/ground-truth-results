# AnyMemo 10.12.2 (helloworld1/AnyMemo@10.12.2, commit 8887e8211de337f0c947ca4ce6bfeddbba6d66a5, package
# org.liberty.android.fantastischmemo.fantastischmemopro, single flavor, instrumented debug build) trigger graph
# definition, schema 2. Written by hand from the app sources under
# final_java_only/AnyMemo/app/AnyMemo-#10.12.2/app/src/main/ after the schema-1 draft (a gen_edges.py-generated
# stub, never hand-reviewed) was found to be "not real work" per the conversion brief. The schema-1 draft is kept
# as generated_draft_graph_def.py.txt (inventory only; nothing is taken over from it).
# Direct app->app calls come from tools/extract_calls.py (bytecode, USE_AUTO); what the bytecode cannot see
# (framework callbacks: lifecycle, listeners registered through the framework, Loader/AsyncTask, Handler.post,
# menus, dialogs, BroadcastReceiver dispatch, ContentProvider CRUD, AppWidget/RemoteViews, Dagger injection root)
# and the guards of the bytecode edges are written here.
# Anonymous inner classes (Foo$1, Foo$2, ...) are numbered by javac in the order they are *declared* in the
# source file (confirmed against AnyMemo$1..$5 and AnyMemo$FileAsyncTaskLoader/$HandleOpenIntentLoaderCallbacks
# in method_list.json, which match top-to-bottom declaration order in AnyMemo.java).
# Framework claims are FW-SRC (Android 8.1.0_r1 lines printed and read) or INFERRED (androidx, Material
# Components, Dagger generated code, ORMLite, RxJava, LocalBroadcastManager, greenrobot-style libraries not
# available locally: see the brief's "stays INFERRED" list).
#
# Section index (search for "# =====")
#  A  helpers, FW-SRC / INFERRED citation constants, ENV / STATE gate texts
#  B  entry points (manifest), process start, Dagger injection root, Base*/QACardActivity lifecycle plumbing
#  C  AnyMemo launcher shell: permission gate, drawer + bottom nav, first-run dialog, ACTION_VIEW open-intent
#  D  tabs: RecentListFragment, OpenTabFragment + OpenActionsFragment, DownloadTabFragment, MiscTabFragment
#  E  study/quiz: QACardActivity base continued, StudyActivity, QuizActivity, CardFragment family,
#     GradeButtonsFragment, QuizLauncherDialogFragment, GestureSelectionDialogFragment
#  F  card management: CardEditor, CardListActivity, PreviewEditActivity, DetailScreen, CategoryEditorFragment,
#     AudioRecorderFragment, FileBrowserActivity, EditTabFragment
#  G  settings / stats: SettingsScreen, OptionScreen, AlgorithmCustomizationScreen, StatisticsScreen
#  H  db import/export: DatabaseMerger, ExportAnyMemoDbFragment, ConverterFragment, converters
#  I  downloader: AnyMemoDownloader*, AbstractDownloaderFragment, Dropbox*, Oauth2AccountActivity,
#     OauthAccountActivity / OauthAccessCodeRetrievalFragment (dead oauth1 code)
#  J  widget / receivers / services: AnyMemoWidgetProvider, UpdateWidgetService, WidgetRemoteViewsFactory,
#     AlarmReceiver, SetAlarmReceiver, CardPlayerService + state machine, ConvertIntentService,
#     CardPlayerActivity / CardPlayerFragment / CardPlayerSettingDialogFragment
#  K  TTS, content providers, Jacoco instrumentation, ShareScreen
#  L  UNREACHABLE table, ENV_KINDS_OF / STATE_KINDS_OF, CLASSIFY, EDIT, STRICT

TITLE = 'AnyMemo 10.12.2 trigger graph'
USE_AUTO = True
STRICT = False        # switched to True once sections A-L classify everything (see the end of the file)

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


# ================================================================== A. helpers, FW citations, gates

# ---- framework citations (filled in with real AOSP line numbers during step 5/6; INFERRED for
#      libraries not available locally, per the brief: androidx, Material Components, Dagger generated
#      code, ORMLite, RxJava, LocalBroadcastManager, the JVM class-initialiser rule)
FW_ACTIVITY = 'FW-SRC core/java/android/app/Activity.java (Activity lifecycle callback dispatched by ActivityThread)'
FW_APP = 'FW-SRC core/java/android/app/Application.java (Application.onCreate called once at process start)'
FW_VIEW = ('INFERRED a tapped/long-pressed View dispatches to the listener registered with setOnClickListener / '
           'setOnLongClickListener / setOnItemClickListener / setOnItemLongClickListener / setOnTouchListener / '
           'setOnCheckedChangeListener / addTextChangedListener / setOnFocusChangeListener / setOnSeekBarChangeListener '
           '(androidx widgets wrap the platform View/AdapterView dispatch; androidx source not read)')
FW_FRAG = 'INFERRED androidx.fragment.app.FragmentManager drives the fragment lifecycle callbacks (androidx source not read)'
FW_DIALOGFRAG = 'INFERRED androidx.fragment.app.DialogFragment shows an android.app.Dialog and forwards its button/cancel/dismiss callbacks (androidx source not read)'
FW_MENU = 'INFERRED the platform options-menu machinery calls onCreateOptionsMenu / onPrepareOptionsMenu / onOptionsItemSelected (AppCompat source not read)'
FW_LOADER = 'INFERRED androidx.loader.app.LoaderManager drives onCreateLoader / onLoadFinished / onLoaderReset and runs AsyncTaskLoader.loadInBackground on a worker thread (androidx source not read)'
FW_ASYNC = 'INFERRED android.os.AsyncTask.execute/executeOnExecutor runs doInBackground on a worker thread and onPreExecute/onPostExecute on the main thread (platform source not read for this exact flow; see FW-SRC citation added in step 6 for the base class)'
FW_HANDLER = 'INFERRED Handler.post/postDelayed queues the Runnable on the thread the Handler was created on (platform source not read for this exact flow; see FW-SRC citation added in step 6)'
FW_MATERIAL = 'INFERRED com.google.android.material (BottomNavigationView / NavigationView / FloatingActionButton / Snackbar) dispatches the listener registered on it, the same way a platform View dispatches a click (Material Components source not read)'
FW_DAGGER = 'INFERRED Dagger-generated code (DaggerAppComponents and its Impl/Builder classes) wires the object graph; most of the chain is explicit calls visible to the bytecode extractor, this citation covers only the parts that are not (field injection assigning an @Inject field is not a call)'
FW_RECEIVER = 'FW-SRC core/java/android/app/ActivityThread.java (a registered BroadcastReceiver is dispatched on its process by ActivityThread/LoadedApk.ReceiverDispatcher when a matching broadcast arrives)'
FW_LOCALBROADCAST = 'INFERRED androidx.localbroadcastmanager.content.LocalBroadcastManager.sendBroadcast delivers synchronously, in-process, to every receiver registered for the action (androidx source not read)'
FW_SERVICE = 'FW-SRC core/java/android/app/ActivityThread.java (a bound/started Service is created and its lifecycle callbacks dispatched by ActivityThread)'
FW_SERVICECONN = 'INFERRED bindService connects asynchronously and calls ServiceConnection.onServiceConnected once the service is created and bound (platform source not read for this exact callback path)'
FW_PROVIDER = 'FW-SRC core/java/android/app/ActivityThread.java (a ContentProvider is instantiated and onCreate() called by ActivityThread as part of attaching the application, before Application.onCreate)'
FW_PROVIDER_CRUD = 'INFERRED another app\'s ContentResolver call (query/insert/update/delete/getType) is dispatched by the system process to this provider (ContentProvider/ActivityThread source not read for the cross-process call path)'
FW_WIDGET = 'INFERRED AppWidgetHost/AppWidgetService delivers APPWIDGET_UPDATE to the exported AppWidgetProvider receiver, and RemoteViewsService.onGetViewFactory / RemoteViewsFactory callbacks are driven by the widget host process (platform source not read for this exact flow)'
FW_ALARM = 'INFERRED AlarmManagerService delivers the PendingIntent broadcast at (or after) the scheduled time to the BroadcastReceiver named in the Intent (platform source not read for this exact flow)'
FW_BOOT = 'INFERRED the system sends ACTION_BOOT_COMPLETED to every registered receiver after the device finishes booting (platform source not read for this exact flow)'
FW_TTS = 'INFERRED android.speech.tts.TextToSpeech calls OnInitListener.onInit once the engine is ready and OnUtteranceCompletedListener.onUtteranceCompleted when an utterance finishes, on its own binder thread (platform TTS client source not read)'
FW_MEDIAPLAYER = 'INFERRED android.media.MediaPlayer calls the registered OnCompletionListener when playback finishes (platform source not read for this exact flow)'
FW_WEBVIEW = 'INFERRED android.webkit.WebView calls the registered WebViewClient.onPageFinished once a page load completes (WebView/Chromium source not read)'
FW_ACTIONMODE = 'INFERRED androidx.appcompat.view.ActionMode (started by startSupportActionMode) calls the registered ActionMode.Callback (onCreateActionMode, onPrepareActionMode, onActionItemClicked, onDestroyActionMode) (AppCompat source not read)'
FW_PREFERENCE = 'INFERRED android.preference.PreferenceActivity / Preference calls the registered OnPreferenceClickListener when the preference row is tapped (platform preference framework source not read for this exact flow)'
FW_RESULT = 'FW-SRC core/java/android/app/Activity.java, core/java/android/app/ActivityThread.java (an activity started with startActivityForResult delivers its result to the caller\'s onActivityResult through ActivityThread.deliverResults)'
RES_CANCEL = 'INFERRED an activity (or dialog) that finishes without calling setResult reports RESULT_CANCELED to the caller\'s onActivityResult by platform default (Activity.setResult/finish default not read line-by-line for this app; see FW-SRC citation added in step 6)'
FW_RX = 'INFERRED RxJava 2 (io.reactivex) Observable/Single/Completable/Maybe delivers onNext/onSuccess/onComplete/onError/accept to the subscriber on the thread named by observeOn (library source not read)'
FW_CUSTOMTABS = 'INFERRED androidx.browser.customtabs.CustomTabsIntent.launchUrl starts an external browser/Custom Tabs activity in another app; the OAuth site later redirects back into this app\'s exported activity by its intent-filter (androidx + external browser source not read)'
FW_GESTURE = 'INFERRED android.gesture.GestureOverlayView calls the registered OnGesturePerformedListener once a gesture stroke is recognised against the loaded GestureLibrary (platform source not read for this exact flow)'
FW_ORMLITE = 'INFERRED com.j256.ormlite (OrmLiteSqliteOpenHelper, BaseDaoImpl, DaoManager) builds and caches the DAO implementations and the SQLite schema; this edge is not read from the ORMLite source (not available locally)'

# ---- ENV gate texts (outside the app / the device)
ENV_VIEW = env_text(
    'outside package: another app (or adb) opens a .db file with AnyMemo (an ACTION_VIEW content intent on a '
    '*.db path; AnyMemo.loadUiComponents calls handleOpenIntent only when getIntent().getAction() is '
    'Intent.ACTION_VIEW, AnyMemo.java:193)', ('other_app',))
ENV_PICKER = env_text(
    'outside package: the system document picker (ACTION_OPEN_DOCUMENT / ACTION_OPEN_DOCUMENT_TREE / '
    'ACTION_CREATE_DOCUMENT) must return a file or folder (the baseline runs started with `-p <app>` refuse to '
    'start other packages, so onActivityResult only gets RESULT_CANCELED without a real device)', ('other_app',))
ENV_NET = env_text('outside package: the AnyMemo download server (anymemo.org) must be reachable (network)', ('network',))
ENV_DROPBOX = env_text('outside package: a Dropbox account and network access (OAuth2 login in an external browser / Custom Tab, api.dropboxapi.com reachable)', ('network', 'other_app'))
ENV_WIDGET = env_text('outside package: the user adds the AnyMemo widget to the launcher home screen, or its update alarm/broadcast fires', ('other_app', 'system_event'))
ENV_ALARM = env_text('outside package: the device delivers the scheduled AlarmManager broadcast (daily notification check)', ('time',))
ENV_BOOT = env_text('outside package: the device reboots (ACTION_BOOT_COMPLETED)', ('system_event',))
ENV_OTHERAPP_SEND = env_text('outside package: another app sends text to AnyMemo with Intent.ACTION_SEND (for example a dictionary app\'s "add to AnyMemo")', ('other_app',))
ENV_PROVIDER = env_text('outside package: another app queries the exported CardProvider / DatabasesProvider content provider', ('other_app',))
ENV_JACOCO = env_text('outside package: the test harness sends the edu.gatech.m3.emma.COLLECT_COVERAGE broadcast (adb) to dump JaCoCo coverage', ('other_app',))
ENV_TTS = env_text('the device has a working text-to-speech engine that finishes speaking an utterance (a TTS engine is required; emulator default engine)', ('hardware',))
ENV_MIC = env_text('the microphone records audio (audio hardware; a virtual microphone on the emulator) and the RECORD_AUDIO permission is granted', ('hardware', 'permission'))
ENV_STORAGE_PERM = env_text('the WRITE_EXTERNAL_STORAGE runtime permission is granted (requested once on API <= 29; always granted on API 27 if accepted)', ('permission',))
ENV_EXT_DICT = env_text('outside package: an external dictionary app (ColorDict / Fora / BlueDict) is installed to receive the lookup intent', ('other_app',))
ENV_EXT_BROWSER = env_text('outside package: a browser app handles the ACTION_VIEW/CATEGORY_BROWSABLE link', ('other_app',))
ENV_COLORDICT_SHARE = env_text('outside package: another app (for example ColorDict) starts ShareScreen with an ACTION_SEND text intent', ('other_app',))
ENV_OAUTH_CALLBACK = env_text('outside package: the Dropbox OAuth2 web page redirects back into this app\'s exported anymemo-dropbox:// activity (a browser / Custom Tab and network access)', ('network', 'other_app'))
ENV_NOTIF = env_text('outside package: the user opens the notification shade and taps the notification', ('system_event',))

# ---- STATE gate texts (earlier in-app action needed)
NEED_DECK = state_text('A deck (.db file) was opened at least once, so one is in the recent list / the Download folder has a .db file', ('data',))
NEED_RECENT = state_text('At least one entry exists in the recent-deck list (Recent tab is not empty)', ('data',))
NEED_CARD = state_text('The open deck has at least one card', ('data',))
NEED_CATEGORY = state_text('The open deck has at least one category other than Uncategorized', ('data',))
NEED_ATTACH_IMG = state_text('The current question/answer text names an image file that exists under the AnyMemo images folder', ('file',))
NEED_FILE_MNEMOSYNE = state_text('A Mnemosyne (.xml) export file exists in the Download folder (the baseline Download fixtures have none)', ('file',))
NEED_FILE_SUPERMEMO = state_text('A SuperMemo (.xml) export file exists in the Download folder (the baseline Download fixtures have none)', ('file',))
NEED_FILE_QA = state_text('A QA text file exists in the Download folder (the baseline Download fixtures have none)', ('file',))
NEED_FILE_ZIP = state_text('A zip export file exists in the Download folder', ('file',))
NEED_SAVED_TOKEN = state_text('A Dropbox access token was saved before (returning user; the fixtures have none)', ('account',))
NEED_AUDIO_RECORDED = state_text('An audio clip was recorded or picked for the focused field before Play/Save is tapped', ('data',))
NEED_PASSWORD_AUDIO = state_text('A previous audio tag already exists in the focused field (<audio src=... />)', ('data',))
NEED_UPGRADE = state_text('This is the very first run after installing (or after upgrading from a version older than 239): savedVersionCode != the build\'s versionCode', ('settings',))
NEED_FIRST_RUN = state_text('This is the very first run (no saved preferences yet, or savedVersionCode < 154 which forces a preference reset)', ('settings',))

SCREENS = {
    'S_ENTRY': 'Outside the app: launcher, a .db file opened from another app/adb, a widget tap, an alarm, boot, the share-from-another-app flow, or the test harness',
    'S_PERM_STORAGE': 'AnyMemo activity showing (or having just shown) the WRITE_EXTERNAL_STORAGE runtime permission dialog (API <= 29)',
    'S_MAIN_RECENT': 'AnyMemo shell: Recent tab (bottom navigation) selected; recent deck list, drawer, FAB to import',
    'S_MAIN_OPEN': 'AnyMemo shell: Open tab selected; file browser rooted at the AnyMemo folder, create-db FAB',
    'S_MAIN_DOWNLOAD': 'AnyMemo shell: Download tab selected; AnyMemo-server / Dropbox source buttons',
    'S_MAIN_MISC': 'AnyMemo shell: Misc tab selected; options, import/export, merge, reset, donate, help, about',
    'S_DRAWER': 'Navigation drawer open over the AnyMemo shell',
    'S_DLG_OPEN_ACTIONS': 'OpenActionsFragment: Study / Edit / List / Quiz / Settings / Statistics / Share / Card player / Delete for the tapped deck',
    'S_DLG_FIRST_RUN': "The first-time-run / what's-new dialog (shown once per install / upgrade)",
    'S_DLG_SDCARD_WARNING': 'The "sdcard not available" warning dialog (exit only)',
    'S_FILEBROWSER': 'FileBrowserActivity: a standalone file browser used by CardEditor (image/audio pick), DatabaseMerger, ShareScreen, SettingsScreen (custom typeface)',
    'S_DLG_CREATE_DB': 'Create-new-database name dialog (file browser FAB / menu)',
    'S_DLG_CREATE_FOLDER': 'Create-folder name dialog (file browser menu)',
    'S_DLG_OVERWRITE_DB': 'Confirm overwrite of an existing .db on import',
    'S_DLG_FB_EDIT': 'Long-press popup on a file-browser row: Delete / Clone / Rename',
    'S_STUDY': 'StudyActivity: classic study screen for the open deck',
    'S_QUIZ': 'QuizActivity: quiz-mode study screen (no grading persisted except via the normal grade buttons)',
    'S_CARD_PLAYER': 'CardPlayerActivity: hands-free audio playback of question/answer with play/prev/next/shuffle/repeat',
    'S_DLG_QUIZ_LAUNCHER': 'QuizLauncherDialogFragment: choose quiz by group / category / range, shuffle',
    'S_DLG_CATEGORY': 'CategoryEditorFragment: pick/create/rename/delete a category (used from Study, Preview/Edit, Quiz launcher)',
    'S_DLG_GESTURE': 'GestureSelectionDialogFragment: enable gestures and show which gesture does what',
    'S_DLG_NO_ITEM': 'The "no card to study" dialog (an empty deck or filter)',
    'S_DLG_UNDO_FAIL': 'The "nothing to undo" dialog',
    'S_DLG_DELETE_CARD': 'Confirm card delete (Study menu / Preview-edit menu)',
    'S_DLG_MARK_LEARNED': 'Confirm "mark as learned forever"',
    'S_CARD_EDITOR': 'CardEditor: add/edit one card (question/answer/note/category, inline image/audio)',
    'S_DLG_EDIT_DISCARD': 'Confirm discarding unsaved edits in CardEditor (Back with changes)',
    'S_DLG_AUDIO_RECORDER': 'AudioRecorderFragment: record / play / save an audio clip for a field',
    'S_DLG_AUDIO_OVERRIDE': 'Confirm overriding an existing audio tag in CardEditor',
    'S_CARD_LIST': 'CardListActivity: scrollable list of all cards with search, sort, per-row popup menus',
    'S_DLG_CARD_SORT': 'Sort-by dialog (CardListActivity menu)',
    'S_CARD_LIST_ROW_MENU': 'Single-tap popup on a card-list row: mark as learned/forgotten/new/learned-forever',
    'S_CARD_LIST_ROW_LONGMENU': 'Long-press popup on a card-list row: Edit / Detail / Preview-edit',
    'S_PREVIEW_EDIT': 'PreviewEditActivity: browse cards one at a time with New/Edit/Prev/Next and a long context menu',
    'S_DETAIL': 'DetailScreen: raw field editor (id, question, answer, note, category text, learning-data numbers)',
    'S_DLG_DETAIL_SAVE': 'Confirm saving the raw DetailScreen fields',
    'S_SETTINGS': 'SettingsScreen: per-deck display settings (fonts, colors, locale/audio, HTML fields)',
    'S_DLG_SETTINGS_DISCARD': 'Confirm discarding unsaved SettingsScreen changes (Back with changes)',
    'S_DLG_LOAD_DEFAULT': 'Confirm "load default settings"',
    'S_DLG_COLOR_PICKER': 'Color-picker dialog (SettingsScreen color row)',
    'S_DLG_FIELD_CHOOSER': 'Multi-choice field-selection dialog (HTML display / field1 / field2)',
    'S_OPTION_SCREEN': 'OptionScreen: app-wide preferences (PreferenceActivity)',
    'S_ALGORITHM_SCREEN': 'AlgorithmCustomizationScreen: scheduling-algorithm parameters (PreferenceActivity)',
    'S_DLG_ALGORITHM_WARN': 'Confirm opening/resetting the scheduling-algorithm customization screen',
    'S_STATISTICS': 'StatisticsScreen: drawer of 4 charts (cards scheduled / accumulative / new learned / grade pie)',
    'S_DB_MERGER': 'DatabaseMerger: pick target + source .db and merge',
    'S_DLG_EXPORT_ANYMEMO': 'ExportAnyMemoDbFragment: pick a .db to export (file browser dialog, then the system Save dialog)',
    'S_DLG_CONVERTER': 'ConverterFragment: pick a .db to export to a foreign format (file browser dialog, then the system Save dialog for text formats)',
    'S_DLG_CONVERT_MERGE': 'Confirm merge-or-replace when the converted output file already exists',
    'S_DLG_RESET_PREF': 'Confirm "reset all preferences" (Misc tab)',
    'S_DLG_DONATE': 'The donate dialog (Misc tab, non-pro flavor)',
    'S_DOWNLOAD_AM': 'AnyMemoDownloaderActivity + AnyMemoDownloaderFragment: browse anymemo.org categories/databases',
    'S_DLG_DOWNLOAD_CONFIRM': 'Confirm downloading one shared database',
    'S_DLG_DOWNLOAD_FAIL': 'Download/connection-error dialog',
    'S_DLG_DOWNLOAD_OK': 'Download-succeeded dialog',
    'S_DROPBOX_LOGIN': 'Oauth2AccountActivity (Dropbox): an external browser/Custom Tab shows the Dropbox login page',
    'S_DROPBOX_LIST': 'DropboxListActivity + DropboxListFragment: browse the AnyMemo folder on Dropbox',
    'S_DROPBOX_UPLOAD': 'UploadDropboxActivity: pick a local .db to upload to Dropbox',
    'S_DLG_DROPBOX_UPLOAD_CONFIRM': 'Confirm uploading the picked file to Dropbox',
    'S_EXT_PICKER': 'The system document picker / Save dialog (another package)',
    'S_EXT_BROWSER': 'An external browser / Custom Tab (another package)',
    'S_EXT_DICT': 'An external dictionary app (another package)',
    'S_HOME_WIDGET': 'Launcher home screen with an AnyMemo widget showing the recent decks',
    'S_NOTIF_REVIEW': 'Notification shade with the "cards to review" reminder notification',
    'S_SHARE_SCREEN': 'ShareScreen: add a card received from another app\'s share/ACTION_SEND',
    'S_EXIT': 'The process ended (finish() back out of the task, or System.exit on a forced version reset)',
}


# ================================================================== B. entry points, process start, Dagger root,
#                                                                       Base*/QACardActivity lifecycle plumbing

# ---- process start: Application and the two exported ContentProviders are created by ActivityThread before
#      Application.onCreate; neither needs a manifest component to be targeted by an Intent.
e('S_ENTRY', 'AMApplication.<init>', 'ENTRY', 'The process starts (any component of the app is about to run)',
  gui=['Tap the AnyMemo icon on the home screen'], evidence='SRC AndroidManifest.xml:20; ' + FW_APP)
e('AMApplication.<init>', 'AMApplication.<clinit>', 'LIFECYCLE', 'class initialisation',
  evidence='SRC AMApplication.java:44 (static field initialiser); INFERRED the class has a static initialiser the JVM runs on first use (Java language rule, not read from a source)')
e('AMApplication.<init>', 'AMApplication.attachBaseContext', 'LIFECYCLE', 'the system calls Application.attachBaseContext before onCreate', evidence=FW_APP + '; SRC AMApplication.java:56-60')
e('AMApplication.<init>', 'AMApplication.onCreate', 'LIFECYCLE', 'the system calls Application.onCreate once, after every ContentProvider in the manifest is created', evidence=FW_APP + '; SRC AMApplication.java:62-73')
# Dagger root: the rest of the object graph (appComponents().inject(this) and every other @Inject site reached
# from it) is wired by explicit calls visible to the bytecode extractor (AUTO); see FW_DAGGER.
sup(('AMApplication.onCreate', 'AMApplication.appComponents'))  # the local var `appComponents` is set, not read, in onCreate
e('S_ENTRY', 'CardProvider.<init>', 'ENTRY', 'The process starts (exported provider; created before Application.onCreate)',
  evidence='SRC AndroidManifest.xml:183-187; ' + FW_PROVIDER)
e('CardProvider.<init>', 'CardProvider.<clinit>', 'LIFECYCLE', 'class initialisation (UriMatcher table)', evidence='SRC provider/CardProvider.java:62-80; INFERRED the class has a static initialiser the JVM runs on first use (Java language rule, not read from a source)')
e('CardProvider.<init>', 'CardProvider.onCreate', 'LIFECYCLE', 'the system calls ContentProvider.onCreate', evidence=FW_PROVIDER + '; SRC provider/CardProvider.java:111-115')
for m in ('query', 'insert', 'update', 'delete', 'getType'):
    e('CardProvider.onCreate', 'CardProvider.' + m, 'FRAMEWORK', 'another app\'s ContentResolver.%s() call on content://<pkg>.cardprovider/...' % m,
      env=ENV_PROVIDER, evidence=FW_PROVIDER_CRUD + '; SRC provider/CardProvider.java:42,83-197; AndroidManifest.xml:183-187')
e('S_ENTRY', 'DatabasesProvider.<init>', 'ENTRY', 'The process starts (exported provider; created before Application.onCreate)',
  evidence='SRC AndroidManifest.xml:188-192; ' + FW_PROVIDER)
e('DatabasesProvider.<init>', 'DatabasesProvider.onCreate', 'LIFECYCLE', 'the system calls ContentProvider.onCreate', evidence=FW_PROVIDER + '; SRC provider/DatabasesProvider.java:58-61')
for m in ('query', 'insert', 'update', 'delete', 'getType'):
    e('DatabasesProvider.onCreate', 'DatabasesProvider.' + m, 'FRAMEWORK', 'another app\'s ContentResolver.%s() call on content://<pkg>.databasesprovider/...' % m,
      env=ENV_PROVIDER, evidence=FW_PROVIDER_CRUD + '; SRC provider/DatabasesProvider.java:41,43-80; AndroidManifest.xml:188-192')

# ---- the AMApplication.<clinit>/DaggerAppComponents class-initialiser rule (androidx.core.content.FileProvider
# is declared in the manifest but is a pure androidx library class with no app bytecode: no node for it).

# ---- AnyMemo (MAIN/LAUNCHER, and VIEW for a .db file opened elsewhere)
e('S_ENTRY', 'AnyMemo.<init>', 'ENTRY', 'MAIN / LAUNCHER intent starts AnyMemo',
  gui=['Home screen of the launcher: tap the AnyMemo icon'], evidence='SRC AndroidManifest.xml:23-46')
e('S_ENTRY', 'AnyMemo.<init>', 'ENTRY', 'another app (or adb) opens a *.db file with ACTION_VIEW',
  env=ENV_VIEW, gui=['Another app: "open with AnyMemo" on a .db file'], evidence='SRC AndroidManifest.xml:34-45')
for cb in ('onCreate', 'onResume', 'onRequestPermissionsResult', 'onActivityResult', 'onOptionsItemSelected', 'onDestroy'):
    e('AnyMemo.<init>', 'AnyMemo.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/AnyMemo.java:115-434')
sup(('AnyMemo.onCreate', 'AnyMemo.loadUiComponents'), ('AnyMemo.onResume', 'AnyMemo.loadUiComponents'),
    ('AnyMemo.onRequestPermissionsResult', 'AnyMemo.loadUiComponents'))
e('AnyMemo.onCreate', 'AnyMemo.loadUiComponents', 'CALL',
  'onCreate: API <= 29 and the WRITE_EXTERNAL_STORAGE permission is already granted (SDK_INT <= Q is always true on the API 27 standard configuration)',
  env=ENV_STORAGE_PERM, evidence='SRC ui/AnyMemo.java:124-141')
e('AnyMemo.onCreate', 'AnyMemo.onRequestPermissionsResult', 'FRAMEWORK',
  'onCreate: the permission is not yet granted, so requestPermissions() is called; the system later calls onRequestPermissionsResult once the user answers the dialog',
  evidence='INFERRED core/java/android/app/Activity.java requestPermissions forwards to the PackageManager and the result returns through onRequestPermissionsResult (platform source not read for this exact callback path); SRC ui/AnyMemo.java:124-141,165-182')
e('AnyMemo.onRequestPermissionsResult', 'AnyMemo.loadUiComponents', 'CALL', 'the user granted the permission in the dialog', env=ENV_STORAGE_PERM, evidence='SRC ui/AnyMemo.java:165-182')
e('AnyMemo.onResume', 'AnyMemo.loadUiComponents', 'CALL',
  'onResume: API <= 29 (always true on API 27) and isUiLoaded is still false and the permission is already granted (the same first-run gap onCreate could not fill because the permission dialog was still pending)',
  env=ENV_STORAGE_PERM, needs_state=state_text('onCreate already requested the WRITE_EXTERNAL_STORAGE permission and the process is still the same (isUiLoaded is false)', ('session',)),
  evidence='SRC ui/AnyMemo.java:145-162')
sup(('AnyMemo.loadUiComponents', 'AnyMemo.handleOpenIntent'))
e('AnyMemo.loadUiComponents', 'AnyMemo.initDrawer', 'CALL', 'initDrawer()', evidence='SRC ui/AnyMemo.java:187')
e('AnyMemo.loadUiComponents', 'AnyMemo.prepareStoreage', 'CALL', 'prepareStoreage()', evidence='SRC ui/AnyMemo.java:189')
e('AnyMemo.loadUiComponents', 'AnyMemo.prepareFirstTimeRun', 'CALL', 'prepareFirstTimeRun()', evidence='SRC ui/AnyMemo.java:190')
e('AnyMemo.loadUiComponents', 'AnyMemo.prepareNotification', 'CALL', 'prepareNotification()', evidence='SRC ui/AnyMemo.java:191')
e('AnyMemo.loadUiComponents', 'AnyMemo.handleOpenIntent', 'CALL', 'getIntent().getAction() is Intent.ACTION_VIEW', env=ENV_VIEW, evidence='SRC ui/AnyMemo.java:193-199')
e('AnyMemo.prepareStoreage', 'S_DLG_SDCARD_WARNING', 'ENTERS', 'the AnyMemo folder on external storage cannot be read (first run, storage unavailable)',
  guard='!sdPath.canRead()', evidence='SRC ui/AnyMemo.java:269-285')
e('AnyMemo$3.onClick', 'S_EXIT', 'ENTERS', 'the only button (Exit) finishes the activity', gui=['Tap Exit'], evidence='SRC ui/AnyMemo.java:273-277')
gui('S_DLG_SDCARD_WARNING', 'AnyMemo$3.onClick', 'Tap Exit', evidence=FW_DIALOGFRAG + '; SRC ui/AnyMemo.java:278-283')
e('AnyMemo.prepareFirstTimeRun', 'S_DLG_FIRST_RUN', 'ENTERS', "a version upgrade or the very first run shows the what's-new dialog",
  needs_state=NEED_UPGRADE, evidence='SRC ui/AnyMemo.java:332-382')
gui('S_DLG_FIRST_RUN', 'AnyMemo$4.onClick', 'Tap the "import_folder" link in the message', needs_state=NEED_UPGRADE, evidence='SRC ui/AnyMemo.java:355-361')
e('AnyMemo$4.onClick', 'AnyMemo.onActivityResult', 'RESULT', 'ACTION_OPEN_DOCUMENT_TREE returns (another app/adb picks a folder)', env=ENV_PICKER,
  evidence=FW_RESULT + '; SRC ui/AnyMemo.java:356-361,424-434')
gui('S_DLG_FIRST_RUN', 'AnyMemo$5.onClick', 'Tap "About this version" (negative button)', needs_state=NEED_UPGRADE, evidence='SRC ui/AnyMemo.java:371-380')
e('AnyMemo$5.onClick', 'S_EXT_BROWSER', 'ENTERS', 'an ACTION_VIEW/CATEGORY_BROWSABLE intent to the versions-view website', env=ENV_EXT_BROWSER, evidence='SRC ui/AnyMemo.java:374-379')
# (AnyMemo.onActivityResult -> FolderImportExportUtil.importFolder and AnyMemo.onDestroy -> AnyMemoWidgetProvider.updateWidget /
#  NotificationUtil.cancelNotification are explicit calls already visible to the bytecode extractor: AUTO covers them.
# The ENV_PICKER gate on reaching FolderImportExportUtil.importFolder/exportFolder bodies is added via CFG['EDGES']-style
# per-pair env in the EDIT hook at the end of this file (frontier gate on the auto edge), not here.

# initDrawer: the navigation drawer header + the bottom navigation
for p in ('S_MAIN_RECENT', 'S_MAIN_OPEN', 'S_MAIN_DOWNLOAD', 'S_MAIN_MISC'):
    gui(p, 'AnyMemo$1.onNavigationItemSelected', 'Swipe in the drawer, tap a drawer entry (Recent / Open / Download / Misc / Options / About)', evidence=FW_MATERIAL + '; SRC ui/AnyMemo.java:209-232')
e('AnyMemo$1.onNavigationItemSelected', 'OptionScreen.<init>', 'INTENT', 'startActivity(OptionScreen) for the Options drawer item', evidence='SRC ui/AnyMemo.java:222-223')
e('AnyMemo$1.onNavigationItemSelected', 'AboutUtil.createAboutDialog', 'CALL', 'the About drawer item calls aboutUtil.createAboutDialog()', evidence='SRC ui/AnyMemo.java:224-225')
e('AnyMemo$1.onNavigationItemSelected', 'AnyMemo$2.onNavigationItemSelected', 'CALL', 'binding.bottomNavigation.setSelectedItemId(...) re-dispatches to the bottom-nav listener for Recent/Open/Download/Misc', evidence='SRC ui/AnyMemo.java:213-221')
for p in ('S_MAIN_RECENT', 'S_MAIN_OPEN', 'S_MAIN_DOWNLOAD', 'S_MAIN_MISC'):
    gui(p, 'AnyMemo$2.onNavigationItemSelected', 'Tap a bottom-navigation item (Recent / Open / Download / Misc)', evidence=FW_MATERIAL + '; SRC ui/AnyMemo.java:234-261')
e('AnyMemo.initDrawer', 'S_MAIN_RECENT', 'ENTERS', 'bottomNavigation.setSelectedItemId(recent_tab_menu): the Recent tab is selected by default on a cold start', evidence='SRC ui/AnyMemo.java:241,253-257,263')
# AnyMemo$2.onNavigationItemSelected: a single method, no context variants (it switches tab the same way no matter
# which tab was selected before); the 4 outgoing ENTERS edges are its 4 itemId branches (explicit `new XxxFragment()`
# + the fragment-transaction commit are already explicit calls the bytecode extractor covers; USE_AUTO).
e('AnyMemo$2.onNavigationItemSelected', 'S_MAIN_RECENT', 'ENTERS', 'itemId == recent_tab_menu', evidence='SRC ui/AnyMemo.java:240-241,253-257')
e('AnyMemo$2.onNavigationItemSelected', 'S_MAIN_OPEN', 'ENTERS', 'itemId == open_tab_menu', evidence='SRC ui/AnyMemo.java:242-246,253-257')
e('AnyMemo$2.onNavigationItemSelected', 'S_MAIN_DOWNLOAD', 'ENTERS', 'itemId == download_tab_menu', evidence='SRC ui/AnyMemo.java:247-248,253-257')
e('AnyMemo$2.onNavigationItemSelected', 'S_MAIN_MISC', 'ENTERS', 'itemId == misc_tab_menu', evidence='SRC ui/AnyMemo.java:249-250,253-257')

e('S_MAIN_RECENT', 'AnyMemo.onOptionsItemSelected', 'FRAMEWORK', 'tap the Up/home icon (drawer burger)', gui=['Tap the menu/burger icon'], evidence=FW_MENU + '; SRC ui/AnyMemo.java:413-421')
e('AnyMemo.onOptionsItemSelected', 'S_DRAWER', 'ENTERS', 'binding.drawerLayout.openDrawer(START)', evidence='SRC ui/AnyMemo.java:414-418')
# BaseActivity.onPause/onStop/onConfigurationChanged are shared, un-overridden lifecycle callbacks (one node for
# every BaseActivity subclass): modelled as plain SYSTEM sinks reached from every live page, not as a shared
# "paused" page (a page needs an unambiguous ENTERS target; BaseActivity.onPause does not identify which concrete
# activity paused, so routing it into one page would be wrong for every activity except the one written here).
for src in ('S_MAIN_RECENT', 'S_MAIN_OPEN', 'S_MAIN_DOWNLOAD', 'S_MAIN_MISC'):
    e(src, 'BaseActivity.onPause', 'SYSTEM', 'Press Home or open another app', gui=['Press Home'], evidence=FW_ACTIVITY + '; SRC common/BaseActivity.java:55-59')
    e(src, 'AnyMemo.onResume', 'SYSTEM', 'return to the app from the recent-apps list (the task resumes without being re-created)', gui=['Press Home, then return to the app from the recent-apps list'], evidence=FW_ACTIVITY)
e('AnyMemo.onResume', 'S_MAIN_RECENT', 'ENTERS', 'isUiLoaded is already true (resumed, not a cold start): the last-selected tab is shown again',
  needs_state=state_text('AnyMemo already finished loadUiComponents() once in this process', ('session',)), evidence='SRC ui/AnyMemo.java:145-162')

# ---- BaseActivity / QACardActivity lifecycle plumbing shared by every other activity (declared once; each
# activity's own <init> below chains into these the same way AnyMemo's does)
e('BaseActivity.<init>', 'BaseActivity.onConfigurationChanged', 'SYSTEM', 'rotate the device or change the system locale', gui=['Rotate the device'], evidence=FW_ACTIVITY + '; SRC common/BaseActivity.java:68-71')
e('QACardActivity.<init>', 'QACardActivity.onCreate', 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:136-141')
e('QACardActivity.<init>', 'QACardActivity.onDestroy', 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:488-503')
e('QACardActivity.<init>', 'QACardActivity.onKeyDown', 'SYSTEM', 'a hardware/volume key is pressed', gui=['Press a volume key'], evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:595-608')
e('QACardActivity.<init>', 'QACardActivity.onKeyUp', 'SYSTEM', 'a hardware/volume key is released', gui=['Press a volume key'], evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:611-623')
e('QACardActivity.<init>', 'QACardActivity.<clinit>', 'LIFECYCLE', 'class initialisation', evidence='SRC ui/QACardActivity.java:90 (static field initialiser); INFERRED the class has a static initialiser the JVM runs on first use (Java language rule, not read from a source)')
e('QACardActivity.onCreate', 'QACardActivity.getContentView', 'CALL', 'setContentView(getContentView())', evidence='SRC ui/QACardActivity.java:137-140')
e('QACardActivity.startInit', 'QACardActivity.loadGestures', 'CALL', 'loadGestures()', evidence='SRC ui/QACardActivity.java:160')
e('QACardActivity.loadGestures', 'QACardActivity$8.onGesturePerformed', 'FRAMEWORK', 'a gesture is drawn on the gesture overlay', gui=['Draw a gesture on the card'], evidence=FW_GESTURE + '; SRC ui/QACardActivity.java:531-542,757-770')
e('QACardActivity$8.onGesturePerformed', 'QACardActivity.onGestureDetected', 'CALL', 'the recognised gesture (score > 3.0) is reported', evidence='SRC ui/QACardActivity.java:761-767')
# SettingLoader / CardTTSUtilLoader only override DBLoader.dbLoadInBackground (an explicit call AUTO already
# makes from DBLoader.loadInBackground); the framework drives the shared DBLoader.loadInBackground template method.
e('QACardActivity.startInit', 'QACardActivity$SettingLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'multipleLoaderManager registers the Setting loader', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:162-163,448-465')
e('QACardActivity$SettingLoaderCallbacks.onCreateLoader', 'DBLoader.loadInBackground', 'ASYNC', 'loader.forceLoad() runs loadInBackground on a worker thread', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:449-452; ui/loader/DBLoader.java:41-50')
e('DBLoader.loadInBackground', 'QACardActivity$SettingLoaderCallbacks.onLoadFinished', 'ASYNC', 'the loaded Setting is delivered on the main thread', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:455-459')
e('QACardActivity.startInit', 'QACardActivity$CardTTSUtilLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'multipleLoaderManager registers the CardTTSUtil loader', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:164-165,467-485')
e('QACardActivity$CardTTSUtilLoaderCallbacks.onCreateLoader', 'DBLoader.loadInBackground', 'ASYNC', 'loader.forceLoad() runs loadInBackground on a worker thread', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:470-473; ui/loader/DBLoader.java:41-50')
e('DBLoader.loadInBackground', 'QACardActivity$CardTTSUtilLoaderCallbacks.onLoadFinished', 'ASYNC', 'the loaded CardTTSUtil is delivered on the main thread', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:476-480')
# MultipleLoaderManager.checkAllLoadersCompleted() is called explicitly from every *LoaderCallbacks.onLoadFinished
# (AUTO already covers that specific call); it then does `handler.post(onAllLoaderCompletedRunnable)` where the
# field is typed java.lang.Runnable -- too generic for the bytecode extractor's CHA to resolve (confirmed: no auto
# edge exists for this call), so every caller's stored Runnable is hand-wired below, once, as the single shared
# fan-out point every onLoadFinished reaches through the explicit (AUTO) call to checkAllLoadersCompleted.
e('MultipleLoaderManager.checkAllLoadersCompleted', 'QACardActivity$2.run', 'FRAMEWORK', 'handler.post(onAllLoaderCompletedRunnable): QACardActivity-family callers (Study/Quiz/CardPlayer/PreviewEdit)',
  needs_state=state_text('every loader registered on this MultipleLoaderManager has reported (runningLoaderCount <= 0)', ('session',)), evidence=FW_HANDLER + '; SRC ui/loader/MultipleLoaderManager.java:104-114')
e('QACardActivity$2.run', 'QACardActivity.onPostInit', 'CALL', 'onPostInitRunnable.run() calls onPostInit() (a virtual call CHA-resolved to whichever QACardActivity subclass is running)', evidence='SRC ui/QACardActivity.java:658-662 (bytecode)')
e('QACardActivity.generateImageOnLongClickListener', 'QACardActivity$3.onLongClick', 'REGISTER', 'the returned listener is attached to the question/answer CardFragment.Builder as its long-click listener', evidence='SRC ui/QACardActivity.java:314-317,691-724')
e('QACardActivity$3.onLongClick', 'S_EXT_PICKER', 'ENTERS', 'ACTION_VIEW on the matched image file (through the FileProvider) opens an external image viewer',
  needs_state=NEED_ATTACH_IMG, evidence='SRC ui/QACardActivity.java:691-723')
for n, m in ((4, 'onClickQuestionText'), (5, 'onClickAnswerText'), (6, 'onClickQuestionView'), (7, 'onClickAnswerView')):
    e('QACardActivity$%d.onClick' % n, 'QACardActivity.' + m, 'CALL', 'the click listener field calls %s()' % m, evidence='SRC ui/QACardActivity.java:726-755')


# ================================================================== D. tabs: RecentListFragment,
#                                                                       OpenTabFragment + OpenActionsFragment,
#                                                                       DownloadTabFragment, MiscTabFragment
for cb in ('onCreate', 'onAttach', 'onDetach', 'onDestroy', 'onCreateView', 'onResume', 'onCreateOptionsMenu'):
    e('RecentListFragment.<init>', 'RecentListFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/RecentListFragment.java:127-226')
e('RecentListFragment.onAttach', 'RecentListFragment$1.onReceive', 'FRAMEWORK', 'LocalBroadcastManager delivers ACTION_REMOVE_SELECTED (sent by RecentListActionModeUtil.ActionModeCallback.onActionItemClicked)',
  evidence=FW_LOCALBROADCAST + '; SRC ui/RecentListFragment.java:111-116,138-141; utils/RecentListActionModeUtil.java:124-128')
e('RecentListFragment.onAttach', 'RecentListFragment$2.onReceive', 'FRAMEWORK', 'LocalBroadcastManager delivers ACTION_DESELECT_ALL (sent by RecentListActionModeUtil on stop / onDestroyActionMode)',
  evidence=FW_LOCALBROADCAST + '; SRC ui/RecentListFragment.java:118-123,139-140; utils/RecentListActionModeUtil.java:62-66,136-139')
e('RecentListFragment.onResume', 'RecentListFragment$RecentListLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'getLoaderManager().restartLoader(1, ...)', evidence=FW_LOADER + '; SRC ui/RecentListFragment.java:218,250-265')
e('RecentListFragment$RecentListLoaderCallbacks.onCreateLoader', 'RecentListFragment$RecentListLoaderCallbacks$1.loadInBackground', 'ASYNC', 'loader.forceLoad() runs loadInBackground on a worker thread', evidence=FW_LOADER + '; SRC ui/RecentListFragment.java:256-263')
e('RecentListFragment$RecentListLoaderCallbacks$1.loadInBackground', 'RecentListFragment$RecentListLoaderCallbacks.onLoadFinished', 'ASYNC', 'the recent-list names are delivered on the main thread', evidence=FW_LOADER + '; SRC ui/RecentListFragment.java:267-272')
e('RecentListFragment.onResume', 'RecentListFragment$RecentListDetailLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'getLoaderManager().restartLoader(2, ...)', evidence=FW_LOADER + '; SRC ui/RecentListFragment.java:219,280-295')
e('RecentListFragment$RecentListDetailLoaderCallbacks.onCreateLoader', 'RecentListFragment$RecentListDetailLoaderCallbacks$1.loadInBackground', 'ASYNC', 'loader.forceLoad() runs loadInBackground on a worker thread', evidence=FW_LOADER + '; SRC ui/RecentListFragment.java:285-292')
e('RecentListFragment$RecentListDetailLoaderCallbacks$1.loadInBackground', 'RecentListFragment$RecentListDetailLoaderCallbacks.onLoadFinished', 'ASYNC', 'the recent-list details (per-deck stats, opens each db) are delivered on the main thread',
  evidence=FW_LOADER + '; SRC ui/RecentListFragment.java:297-304')
e('RecentListFragment.onCreateView', 'RecentListFragment$3.onClick', 'FRAMEWORK', 'tap the import FAB (R.id.import_fab, only present in some layouts)', gui=['Tap the import FAB on the Recent tab'], evidence=FW_VIEW + '; SRC ui/RecentListFragment.java:184-195')
e('RecentListFragment$3.onClick', 'RecentListFragment.onActivityResult', 'RESULT', 'ACTION_OPEN_DOCUMENT returns', env=ENV_PICKER, evidence=FW_RESULT + '; SRC ui/RecentListFragment.java:188-193,201-213')
e('RecentListFragment.onActivityResult', 'DatabaseImportUtil.handleImportDbResult', 'CALL', 'REQUEST_CODE_IMPORT_DB, RESULT_OK: import the picked .db', env=ENV_PICKER, evidence='SRC ui/RecentListFragment.java:202-209')
e('DatabaseImportUtil.handleImportDbResult', 'RecentListFragment$4.run', 'CALL', 'the onSuccess Runnable passed by RecentListFragment.onActivityResult is run after a successful import', evidence=FW_RX + '; SRC utils/DatabaseImportUtil.java:37-62; ui/RecentListFragment.java:204-209')
e('RecentListFragment$4.run', 'RecentListFragment.onResume', 'CALL', 'the Runnable calls onResume() directly to reload the list', evidence='SRC ui/RecentListFragment.java:206-208')
e('RecentListFragment.onCreateView', 'RecentListFragment$RecentListAdapter$1.onClick', 'FRAMEWORK', 'tap a recent-deck row (no row selected)', gui=['Tap a deck in the Recent list'], needs_state=NEED_RECENT, evidence=FW_VIEW + '; SRC ui/RecentListFragment.java:413-428')
e('RecentListFragment$RecentListAdapter$1.onClick', 'S_STUDY', 'ENTERS', 'getSelectedItemCount() == 0: startActivity(StudyActivity) for the tapped deck', evidence='SRC ui/RecentListFragment.java:416-422')
e('RecentListFragment.onCreateView', 'RecentListFragment$RecentListAdapter$2.onLongClick', 'FRAMEWORK', 'long-press a recent-deck row', gui=['Long-press a deck in the Recent list'], needs_state=NEED_RECENT, evidence=FW_VIEW + '; SRC ui/RecentListFragment.java:430-440')
e('RecentListFragment$RecentListAdapter$2.onLongClick', 'RecentListActionModeUtil.startActionMode', 'CALL', 'the first long-press (getSelectedItemCount() == 0) starts the action mode', evidence='SRC ui/RecentListFragment.java:433-435')
e('RecentListActionModeUtil.startActionMode', 'RecentListActionModeUtil$1.onReceive', 'FRAMEWORK', 'LocalBroadcastManager delivers ACTION_START_ACTION_MODE (sent to itself)', evidence=FW_LOCALBROADCAST + '; SRC utils/RecentListActionModeUtil.java:35-40,91-94')
e('RecentListActionModeUtil$1.onReceive', 'RecentListActionModeUtil$ActionModeCallback.onCreateActionMode', 'FRAMEWORK', 'startSupportActionMode(callback) creates the CAB and calls onCreateActionMode', evidence=FW_ACTIONMODE + '; SRC utils/RecentListActionModeUtil.java:38,107-114')
e('RecentListActionModeUtil.updateActionMode', 'RecentListActionModeUtil$2.onReceive', 'FRAMEWORK', 'LocalBroadcastManager delivers ACTION_UPDATE_ACTION_MODE', evidence=FW_LOCALBROADCAST + '; SRC utils/RecentListActionModeUtil.java:42-55,96-100')
e('RecentListActionModeUtil$ActionModeCallback.onActionItemClicked', 'RecentListFragment$1.onReceive', 'FRAMEWORK', 'tap "Remove" in the CAB: LocalBroadcastManager delivers ACTION_REMOVE_SELECTED', gui=['Tap Remove in the selection toolbar'], env=None,
  needs_state=NEED_RECENT, evidence=FW_LOCALBROADCAST + '; SRC utils/RecentListActionModeUtil.java:122-129')
e('RecentListActionModeUtil$ActionModeCallback.onDestroyActionMode', 'RecentListActionModeUtil$3.onReceive', 'FRAMEWORK', 'the CAB is dismissed: LocalBroadcastManager delivers ACTION_DESELECT_ALL via mode.finish()/system Back', evidence=FW_LOCALBROADCAST + '; SRC utils/RecentListActionModeUtil.java:57-67,135-139')
e('RecentListFragment.onCreateView', 'RecentListFragment$RecentListAdapter$3.onClick', 'FRAMEWORK', 'tap the "more" button on a recent-deck row', gui=['Tap the "..." button on a deck row'], needs_state=NEED_RECENT, evidence=FW_VIEW + '; SRC ui/RecentListFragment.java:442-452')
e('RecentListFragment$RecentListAdapter$3.onClick', 'OpenActionsFragment.<init>', 'CALL', 'a new OpenActionsFragment is shown for the tapped deck', evidence='SRC ui/RecentListFragment.java:446-451')
e('RecentListFragment$RecentListAdapter$3.onClick', 'S_DLG_OPEN_ACTIONS', 'ENTERS', 'df.show(...)', evidence='SRC ui/RecentListFragment.java:450')
e('RecentListFragment.onOptionsItemSelected', 'RecentListUtil.clearRecentList', 'CALL', 'openmenu_clear menu item', evidence='SRC ui/RecentListFragment.java:228-234')


def clone_auto(src, variant, exclude=(), only=None, need=None, env=None, guard=None):
    """Copy the bytecode call edges of `src` onto `variant` (a context node of the same method), minus `exclude`."""
    seen = set()
    for c in AUTO['calls']:
        if c['src'] != src or c['dst'] in exclude or c['dst'] in seen:
            continue
        if only is not None and c['dst'] not in only:
            continue
        seen.add(c['dst'])
        e(variant, c['dst'], 'CALL', 'call made by %s' % src.split('.', 1)[1], needs_state=need, env=env, guard=guard,
          evidence='SRC %s:%d (bytecode)' % (c['file'], c['line']))


# ---- FileBrowserFragment is instantiated directly (not through a subclass) by FileBrowserActivity, SettingsScreen
# (twice: question/answer custom typeface) and UploadDropboxActivity, and subclassed by OpenTabFragment,
# EditTabFragment (dead: never instantiated anywhere in the app, see section L), ExportAnyMemoDbFragment and
# ConverterFragment. Every one of those 6 live call sites sets its own OnFileClickListener (or, for
# UploadDropboxActivity, implements the interface on the Activity itself and relies on the
# `getActivity() instanceof OnFileClickListener` fallback in notifyFileClick). The single compiled
# FileBrowserFragment.openFile()/notifyFileClick() therefore has ONE bytecode call site that CHA-resolves to los
# 7 different onFileBrowserFileClick implementations (verified in auto_calls.json): the auto edges are suppressed
# and replaced by one context variant per real caller (recipe: "split a method by how it is reached").
sup(('FileBrowserFragment.openFile', 'OpenTabFragment$1.onFileBrowserFileClick'),
    ('FileBrowserFragment.openFile', 'EditTabFragment$1.onFileBrowserFileClick'),
    ('FileBrowserFragment.openFile', 'ExportAnyMemoDbFragment$1.onFileBrowserFileClick'),
    ('FileBrowserFragment.openFile', 'ConverterFragment$1.onFileBrowserFileClick'),
    ('FileBrowserFragment.openFile', 'FileBrowserActivity$1.onFileBrowserFileClick'),
    ('FileBrowserFragment.openFile', 'SettingsScreen$11.onFileBrowserFileClick'),
    ('FileBrowserFragment.openFile', 'SettingsScreen$12.onFileBrowserFileClick'),
    ('FileBrowserFragment.openFile', 'UploadDropboxActivity.onFileBrowserFileClick'),
    ('FileBrowserFragment.notifyFileClick', 'OpenTabFragment$1.onFileBrowserFileClick'),
    ('FileBrowserFragment.notifyFileClick', 'EditTabFragment$1.onFileBrowserFileClick'),
    ('FileBrowserFragment.notifyFileClick', 'ExportAnyMemoDbFragment$1.onFileBrowserFileClick'),
    ('FileBrowserFragment.notifyFileClick', 'ConverterFragment$1.onFileBrowserFileClick'),
    ('FileBrowserFragment.notifyFileClick', 'FileBrowserActivity$1.onFileBrowserFileClick'),
    ('FileBrowserFragment.notifyFileClick', 'SettingsScreen$11.onFileBrowserFileClick'),
    ('FileBrowserFragment.notifyFileClick', 'SettingsScreen$12.onFileBrowserFileClick'))
# every live caller sets the listener directly except UploadDropboxActivity, so the (notifyFileClick,
# UploadDropboxActivity.onFileBrowserFileClick) auto edge is correct on its own and is kept (not suppressed).
FB_CALLERS = ('OPEN', 'EXPORT', 'CONVERTER', 'FBACTIVITY', 'SETTINGS_Q', 'SETTINGS_A', 'UPLOADDROPBOX')
FB_TARGET = {
    'OPEN': 'OpenTabFragment$1.onFileBrowserFileClick',
    'EXPORT': 'ExportAnyMemoDbFragment$1.onFileBrowserFileClick',
    'CONVERTER': 'ConverterFragment$1.onFileBrowserFileClick',
    'FBACTIVITY': 'FileBrowserActivity$1.onFileBrowserFileClick',
    'SETTINGS_Q': 'SettingsScreen$11.onFileBrowserFileClick',
    'SETTINGS_A': 'SettingsScreen$12.onFileBrowserFileClick',
}
for v in FB_CALLERS:
    clone_auto('FileBrowserFragment.openFile', 'FileBrowserFragment.openFile@' + v,
               exclude=set(FB_TARGET.values()) | {'UploadDropboxActivity.onFileBrowserFileClick'})
    if v == 'UPLOADDROPBOX':
        e('FileBrowserFragment.openFile@UPLOADDROPBOX', 'FileBrowserFragment.notifyFileClick', 'CALL',
          'onFileClickListener is null (UploadDropboxActivity never calls setOnFileClickListener)', evidence='SRC ui/FileBrowserFragment.java:412,415')
    else:
        e('FileBrowserFragment.openFile@' + v, FB_TARGET[v], 'CALL', 'onFileClickListener.onFileBrowserFileClick(clickedFile)', evidence='SRC ui/FileBrowserFragment.java:412-414 (bytecode)')
e('FileBrowserFragment.notifyFileClick', 'UploadDropboxActivity.onFileBrowserFileClick', 'CALL', 'getActivity() instanceof OnFileClickListener (UploadDropboxActivity implements it directly)', evidence='SRC ui/FileBrowserFragment.java:434-440 (bytecode)')

# ---- the lifecycle/menu/adapter part of FileBrowserFragment is shared unchanged by every caller (only the final
# openFile@X branch above differs): one set of edges, reached from every page that hosts a FileBrowserFragment.
FB_PAGES = {'S_MAIN_OPEN': 'OPEN', 'S_FILEBROWSER': 'FBACTIVITY', 'S_DLG_EXPORT_ANYMEMO': 'EXPORT',
            'S_DLG_CONVERTER': 'CONVERTER', 'S_DROPBOX_UPLOAD': 'UPLOADDROPBOX'}
for page, v in FB_PAGES.items():
    for cb in ('onCreate', 'onCreateView', 'onResume', 'onCreateOptionsMenu', 'onDestroy'):
        e(page, 'FileBrowserFragment.' + cb, 'LIFECYCLE', 'DialogFragment/Fragment lifecycle callback (OPEN/FBACTIVITY/UPLOADDROPBOX call it directly; EXPORT/CONVERTER reach it through their own onCreate -> super.onCreate(), an explicit call AUTO already covers)',
          evidence=FW_FRAG + '; SRC ui/FileBrowserFragment.java:122-322')
e('FileBrowserFragment.onResume', 'FileBrowserFragment.browseTo', 'CALL', 'onResume() browses to the current/default directory', evidence='SRC ui/FileBrowserFragment.java:208-212')
e('FileBrowserFragment.onCreateView', 'FileBrowserFragment$FileBrowserAdapter$1.onClick', 'FRAMEWORK', 'tap a row in the file list', gui=['Tap a file or folder'], evidence=FW_VIEW + '; SRC ui/FileBrowserFragment.java:463-519')
for v in FB_CALLERS:
    e('FileBrowserFragment$FileBrowserAdapter$1.onClick', 'FileBrowserFragment.openFile@' + v, 'CALL', 'fragment.openFile(selectedFileName)', evidence='SRC ui/FileBrowserFragment.java:514-519')
e('FileBrowserFragment.onCreateView', 'FileBrowserFragment$FileBrowserAdapter$2.onLongClick', 'FRAMEWORK', 'long-press a file row', gui=['Long-press a file'], evidence=FW_VIEW + '; SRC ui/FileBrowserFragment.java:521-586')
e('FileBrowserFragment$FileBrowserAdapter$2.onLongClick', 'S_DLG_FB_EDIT', 'ENTERS', 'the row is a file (not "." or ".."): AlertDialog.setItems(fb_dialog_list)', evidence='SRC ui/FileBrowserFragment.java:540-547')
gui('S_DLG_FB_EDIT', 'FileBrowserFragment$FileBrowserAdapter$2$1.onClick', 'Tap Delete / Clone / Rename', evidence=FW_DIALOGFRAG + '; SRC ui/FileBrowserFragment.java:546-577')
e('FileBrowserFragment$FileBrowserAdapter$2$1.onClick', 'DatabaseOperationDialogUtil.showDeleteDbDialog', 'CALL', 'which == 0', evidence='SRC ui/FileBrowserFragment.java:549-557')
e('FileBrowserFragment$FileBrowserAdapter$2$1.onClick', 'DatabaseOperationDialogUtil.showCloneDbDialog', 'CALL', 'which == 1', evidence='SRC ui/FileBrowserFragment.java:558-566')
e('FileBrowserFragment$FileBrowserAdapter$2$1.onClick', 'DatabaseOperationDialogUtil.showRenameDbDialog', 'CALL', 'which == 2', evidence='SRC ui/FileBrowserFragment.java:567-575')
e('DatabaseOperationDialogUtil.showDeleteDbDialog', 'FileBrowserFragment$FileBrowserAdapter$2$1$1.accept', 'FRAMEWORK', 'the Maybe emits onSuccess(file) once the delete-confirm dialog\'s OK is tapped', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:550-557; utils/DatabaseOperationDialogUtil.java:86-117')
e('DatabaseOperationDialogUtil.showCloneDbDialog', 'FileBrowserFragment$FileBrowserAdapter$2$1$2.accept', 'FRAMEWORK', 'the Maybe emits onSuccess(file) once the clone finishes', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:559-566; utils/DatabaseOperationDialogUtil.java:119-139')
e('DatabaseOperationDialogUtil.showRenameDbDialog', 'FileBrowserFragment$FileBrowserAdapter$2$1$3.accept', 'FRAMEWORK', 'the Maybe emits onSuccess(file) once the rename-confirm dialog\'s OK is tapped', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:568-575; utils/DatabaseOperationDialogUtil.java:141-181')
e('FileBrowserFragment$FileBrowserAdapter$2$1$1.accept', 'FileBrowserFragment.browseTo', 'CALL', 'browseTo(file.getParentFile())', evidence='SRC ui/FileBrowserFragment.java:554-556')
e('FileBrowserFragment$FileBrowserAdapter$2$1$2.accept', 'FileBrowserFragment.browseTo', 'CALL', 'browseTo(file.getParentFile())', evidence='SRC ui/FileBrowserFragment.java:563-565')
e('FileBrowserFragment$FileBrowserAdapter$2$1$3.accept', 'FileBrowserFragment.browseTo', 'CALL', 'browseTo(file.getParentFile())', evidence='SRC ui/FileBrowserFragment.java:572-574')
e('FileBrowserFragment.onCreateOptionsMenu', 'FileBrowserFragment.onOptionsItemSelected', 'FRAMEWORK', 'tap a file-browser menu item', gui=['Tap a menu item in the file browser'], evidence=FW_MENU + '; SRC ui/FileBrowserFragment.java:283-322')
e('FileBrowserFragment.onOptionsItemSelected', 'S_DLG_CREATE_DB', 'ENTERS', 'file_browser_createdb', evidence='SRC ui/FileBrowserFragment.java:291-300')
gui('S_DLG_CREATE_DB', 'FileBrowserFragment$1.accept', 'Type a name and tap OK', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:292-299; utils/DatabaseOperationDialogUtil.java:39-84')
e('FileBrowserFragment$1.accept', 'FileBrowserFragment.browseTo', 'CALL', 'browseTo(file.getParentFile())', evidence='SRC ui/FileBrowserFragment.java:296-298')
e('FileBrowserFragment.onOptionsItemSelected', 'S_DLG_CREATE_FOLDER', 'ENTERS', 'file_browser_createdirectory', evidence='SRC ui/FileBrowserFragment.java:301-310')
gui('S_DLG_CREATE_FOLDER', 'FileBrowserFragment$2.accept', 'Type a name and tap OK', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:302-309; utils/DatabaseOperationDialogUtil.java:183-219')
e('FileBrowserFragment$2.accept', 'FileBrowserFragment.browseTo', 'CALL', 'browseTo(file)', evidence='SRC ui/FileBrowserFragment.java:306-307')
e('FileBrowserFragment.onOptionsItemSelected', 'FileBrowserFragment.onActivityResult', 'RESULT', 'file_browser_importdb: ACTION_OPEN_DOCUMENT returns', env=ENV_PICKER, evidence=FW_RESULT + '; SRC ui/FileBrowserFragment.java:311-316,325-356')
e('FileBrowserFragment.onActivityResult', 'S_DLG_OVERWRITE_DB', 'ENTERS', 'RESULT_OK and a file of the same name already exists', env=ENV_PICKER, evidence='SRC ui/FileBrowserFragment.java:338-349')
gui('S_DLG_OVERWRITE_DB', 'FileBrowserFragment$3.onClick', 'Tap Yes (overwrite)', evidence=FW_DIALOGFRAG + '; SRC ui/FileBrowserFragment.java:342-347')
e('FileBrowserFragment$3.onClick', 'FileBrowserFragment.importDb', 'CALL', 'importDb(uri, newFile)', evidence='SRC ui/FileBrowserFragment.java:345-346')
e('FileBrowserFragment.onActivityResult', 'FileBrowserFragment.importDb', 'CALL', 'RESULT_OK and no file of the same name exists', env=ENV_PICKER, evidence='SRC ui/FileBrowserFragment.java:350-352')
e('FileBrowserFragment.importDb', 'FileBrowserFragment$4.accept', 'FRAMEWORK', 'the Observable emits onNext(file) once the copy finishes (observeOn mainThread)', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:369-377')
e('FileBrowserFragment.importDb', 'FileBrowserFragment$5.accept', 'FRAMEWORK', 'the Observable emits onError(throwable)', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:378-383')
e('FileBrowserFragment$4.accept', 'FileBrowserFragment.refreshFileList', 'CALL', 'refreshFileList(currentDirectory)', evidence='SRC ui/FileBrowserFragment.java:372-375')
e('FileBrowserFragment.onCreateView', 'FileBrowserFragment$7.onClick', 'FRAMEWORK', 'tap the create-db FAB (only shown with EXTRA_SHOW_CREATE_DB_BUTTON, i.e. the Open tab)',
  gui=['Tap the create-database FAB on the Open tab'], evidence=FW_VIEW + '; SRC ui/FileBrowserFragment.java:196-200,447-461')
e('FileBrowserFragment$7.onClick', 'S_DLG_CREATE_DB', 'ENTERS', 'showCreateDbDialog(AMEnv.DEFAULT_ROOT_PATH)', evidence='SRC ui/FileBrowserFragment.java:451-460')
gui('S_DLG_CREATE_DB', 'FileBrowserFragment$7$1.accept', 'Type a name and tap OK (FAB variant)', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:453-458')
e('FileBrowserFragment$7$1.accept', 'FileBrowserFragment.refreshFileList', 'CALL', 'refreshFileList(file.getAbsoluteFile().getParentFile())', evidence='SRC ui/FileBrowserFragment.java:456-457')

# ---- OpenTabFragment (the Open tab = a FileBrowserFragment rooted at the AnyMemo folder) + OpenActionsFragment
e('S_MAIN_OPEN', 'OpenTabFragment.onAttach', 'LIFECYCLE', 'Fragment lifecycle callback (onAttach sets the file-click listener)', evidence=FW_FRAG + '; SRC ui/OpenTabFragment.java:34-39')
e('OpenTabFragment.onAttach', 'FileBrowserFragment.setOnFileClickListener', 'CALL', 'setOnFileClickListener(fileClickListener)', evidence='SRC ui/OpenTabFragment.java:38')
e('OpenTabFragment$1.onFileBrowserFileClick', 'OpenActionsFragment.<init>', 'CALL', 'a new OpenActionsFragment is created for the tapped .db', evidence='SRC ui/OpenTabFragment.java:43-47')
e('OpenTabFragment$1.onFileBrowserFileClick', 'S_DLG_OPEN_ACTIONS', 'ENTERS', 'df.show(...)', needs_state=NEED_DECK, evidence='SRC ui/OpenTabFragment.java:48')


# ================================================================== E. study/quiz
e('OpenActionsFragment$1.onClick', 'StudyActivity.<init>', 'INTENT', 'v == studyItem: startActivity(StudyActivity)', evidence='SRC ui/OpenActionsFragment.java:121-127')
e('RecentListFragment$RecentListAdapter$1.onClick', 'StudyActivity.<init>', 'INTENT', 'tap a recent-deck row (getSelectedItemCount() == 0)', evidence='SRC ui/RecentListFragment.java:417-422')
e('AnyMemoWidgetProvider.onUpdate', 'StudyActivity.<init>', 'INTENT', 'tap a widget row (RemoteViews PendingIntentTemplate + the row\'s fill-in intent)', env=ENV_WIDGET, evidence='SRC widget/AnyMemoWidgetProvider.java:66-77; widget/WidgetRemoteViewsFactory.java:89-91')
for cb in ('onCreate', 'onSaveInstanceState', 'onCreateOptionsMenu', 'onOptionsItemSelected', 'onCreateContextMenu', 'onActivityResult', 'onDestroy', 'onResume'):
    e('StudyActivity.<init>', 'StudyActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/StudyActivity.java:103-257')
e('StudyActivity.onCreate', 'StudyActivity$LearnQueueManagerLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'getMultipleLoaderManager().registerLoaderCallbacks(...); startInit() starts loading', evidence=FW_LOADER + '; SRC ui/StudyActivity.java:119-121,428-437')
e('StudyActivity$LearnQueueManagerLoaderCallbacks.onCreateLoader', 'StudyActivity$LearnQueueManagerLoader.dbLoadInBackground', 'ASYNC', 'loader.forceLoad()', evidence=FW_LOADER + '; SRC ui/StudyActivity.java:429-436; ui/loader/DBLoader.java:41-50')
e('StudyActivity$LearnQueueManagerLoader.dbLoadInBackground', 'StudyActivity$LearnQueueManagerLoaderCallbacks.onLoadFinished', 'ASYNC', 'the built LearnQueueManager is delivered on the main thread', evidence=FW_LOADER + '; SRC ui/StudyActivity.java:440-443')
e('StudyActivity$LearnQueueManagerLoaderCallbacks.onLoadFinished', 'QACardActivity.onPostInit', 'CALL', 'both this loader and the Setting/CardTTSUtil loaders have reported', evidence='SRC ui/StudyActivity.java:441-442')
e('StudyActivity.onPostInit', 'StudyActivity.showNoItemDialog', 'CALL', 'the deck has no card to study', guard='queueManager.dequeue() == null', evidence='SRC ui/StudyActivity.java:280-295')
gui('S_DLG_NO_ITEM', 'StudyActivity$2.onClick', 'Tap Back (study, no card)', evidence=FW_DIALOGFRAG + '; SRC ui/StudyActivity.java:404-423')
e('StudyActivity$2.onClick', 'S_EXIT', 'ENTERS', 'onBackPressed() (BaseActivity has no override: the platform pops the task)', evidence=FW_ACTIVITY + '; SRC ui/StudyActivity.java:408-414')
e('StudyActivity$1.onCancel', 'S_EXIT', 'ENTERS', 'the dialog is cancelled (Back/outside tap): onBackPressed()', evidence='SRC ui/StudyActivity.java:416-420')
e('StudyActivity.onPostInit', 'StudyActivity.setupGradeButtons', 'CALL', 'the deck has at least one card', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:296-300')
e('StudyActivity.setupGradeButtons', 'GradeButtonsFragment.<init>', 'CALL', 'a new GradeButtonsFragment is added to buttons_root', evidence='SRC ui/StudyActivity.java:533-543')
e('StudyActivity.onPostInit', 'S_STUDY', 'ENTERS', 'displayCard(false) shows the first card', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:296-300')
e('S_STUDY', 'StudyActivity.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is inflated (study_activity_menu)', evidence=FW_MENU + '; SRC ui/StudyActivity.java:138-142')
e('S_STUDY', 'StudyActivity.onOptionsItemSelected', 'FRAMEWORK', 'tap a Study toolbar/overflow menu item', gui=['Tap a menu item in Study'], evidence=FW_MENU + '; SRC ui/StudyActivity.java:144-194')
e('StudyActivity.onOptionsItemSelected', 'S_EXT_BROWSER', 'ENTERS', 'menu_memo_help', env=ENV_EXT_BROWSER, evidence='SRC ui/StudyActivity.java:147-149,725-731')
e('StudyActivity.onOptionsItemSelected', 'S_SETTINGS', 'ENTERS', 'menusettings: startActivityForResult(SettingsScreen)', evidence='SRC ui/StudyActivity.java:154-156,719-723')
e('StudyActivity.onOptionsItemSelected', 'S_DETAIL', 'ENTERS', 'menudetail: startActivityForResult(DetailScreen)', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:157-159,712-717')
e('StudyActivity.onOptionsItemSelected', 'StudyActivity.undoCard', 'CALL', 'menuundo', evidence='SRC ui/StudyActivity.java:160-162,549-573')
e('StudyActivity.undoCard', 'S_DLG_UNDO_FAIL', 'ENTERS', 'no previous card to undo: the nothing-to-undo dialog (undo_fail_text) is shown', guard='prevCard == null', evidence='SRC ui/StudyActivity.java:565-573')
e('StudyActivity.undoCard', 'S_STUDY', 'ENTERS', 'restartActivity() re-displays the restored previous card', needs_state=state_text('a grade was given to at least one card before in this process (prevCard != null)', ('session',)), evidence='SRC ui/StudyActivity.java:549-564')
e('StudyActivity.onOptionsItemSelected', 'S_DLG_CATEGORY', 'ENTERS', 'menu_memo_category: showCategoriesDialog()', evidence='SRC ui/StudyActivity.java:163-165,515-530')
e('StudyActivity.onOptionsItemSelected', 'S_CARD_EDITOR', 'ENTERS', 'menu_context_edit: startActivityForResult(CardEditor)', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:166-168,662-668')
e('StudyActivity.onOptionsItemSelected', 'S_DLG_DELETE_CARD', 'ENTERS', 'menu_context_delete', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:169-171,670-686')
gui('S_DLG_DELETE_CARD', 'StudyActivity$5.onClick', 'Tap OK (confirm delete)', evidence=FW_DIALOGFRAG + '; SRC ui/StudyActivity.java:674-683')
e('StudyActivity$5.onClick', 'S_STUDY', 'ENTERS', 'the card is deleted and restartActivity() dequeues the next one', evidence='SRC ui/StudyActivity.java:676-681')
e('StudyActivity.onOptionsItemSelected', 'S_DLG_MARK_LEARNED', 'ENTERS', 'menu_mark_as_learned_forever', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:172-174,688-699')
gui('S_DLG_MARK_LEARNED', 'StudyActivity$6.onClick', 'Tap OK (confirm)', evidence=FW_DIALOGFRAG + '; SRC ui/StudyActivity.java:692-697')
e('StudyActivity$6.onClick', 'StudyActivity.markCurrentCardAsLearnedForever', 'CALL', 'markCurrentCardAsLearnedForever()', evidence='SRC ui/StudyActivity.java:693')
e('StudyActivity.markCurrentCardAsLearnedForever', 'S_STUDY', 'ENTERS', 'restartActivity()', evidence='SRC ui/StudyActivity.java:634-643')
e('StudyActivity.onOptionsItemSelected', 'S_PREVIEW_EDIT', 'ENTERS', 'menu_context_gotoprev: gotoPreviewEdit()', evidence='SRC ui/StudyActivity.java:175-177,701-710')
e('StudyActivity.onOptionsItemSelected', 'DictionaryUtil.showLookupListDialog', 'CALL', 'menu_context_lookup', guard='getCurrentCard() != null', evidence='SRC ui/StudyActivity.java:178-184,658-660')
e('DictionaryUtil.showLookupListDialog', 'S_EXT_DICT', 'ENTERS', 'tap a word: the lookup intent is sent to the configured dictionary app', gui=['Tap a word in the lookup list'], env=ENV_EXT_DICT, evidence='SRC utils/DictionaryUtil.java:102-113,115-159')
e('StudyActivity.onOptionsItemSelected', 'StudyActivity.showGesturesDialog', 'CALL', 'menu_gestures', evidence='SRC ui/StudyActivity.java:185-187,645-656')
e('StudyActivity.showGesturesDialog', 'S_DLG_GESTURE', 'ENTERS', 'df.show(...)', evidence='SRC ui/StudyActivity.java:651-655')
e('StudyActivity.onOptionsItemSelected', 'ShareUtil.shareCard', 'CALL', 'menu_share', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:188-191')
e('ShareUtil.shareCard', 'S_EXT_PICKER', 'ENTERS', 'Intent.createChooser(ACTION_SEND text/plain) shows the system share sheet', env=ENV_PICKER, evidence='SRC utils/ShareUtil.java:38-44')
e('S_STUDY', 'StudyActivity.onCreateContextMenu', 'FRAMEWORK', 'long-press the card area', gui=['Long-press the card'], evidence=FW_MENU + '; SRC ui/StudyActivity.java:196-202')
e('StudyActivity.onActivityResult', 'S_STUDY', 'ENTERS', 'restartActivity() for every request code except RESULT_CANCELED', evidence='SRC ui/StudyActivity.java:204-244,259-271')
e('StudyActivity.showCategoriesDialog', 'S_DLG_CATEGORY', 'ENTERS', 'df.show(...)', evidence='SRC ui/StudyActivity.java:515-529')
e('S_DLG_CATEGORY', 'StudyActivity$3.onReceiveCategory', 'CALL', 'a category is picked (CategoryEditorFragment ok button)', evidence='SRC ui/StudyActivity.java:576-586; ui/CategoryEditorFragment.java:94-109')
e('StudyActivity$3.onReceiveCategory', 'S_STUDY', 'ENTERS', 'restartActivity() for the new filter category', evidence='SRC ui/StudyActivity.java:576-586')
e('GradeButtonsFragment$5.onGradeButtonClick', 'GradeButtonsFragment$GradeTask.doInBackground', 'ASYNC', 'new GradeTask().execute(grade)', evidence=FW_ASYNC + '; SRC ui/GradeButtonsFragment.java:211-217')
e('GradeButtonsFragment$GradeTask.doInBackground', 'GradeButtonsFragment$GradeTask.onPostExecute', 'ASYNC', 'the graded card is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/GradeButtonsFragment.java:293-304')
e('GradeButtonsFragment$GradeTask.onPostExecute', 'StudyActivity$4.onCardChanged', 'CALL', 'onCardChangedListener.onCardChanged(prevCard, updatedCard)', evidence='SRC ui/GradeButtonsFragment.java:302')
e('StudyActivity$4.onCardChanged', 'StudyActivity.showNoItemDialog', 'CALL', 'the queue is empty after this grade', guard='nextCard == null', evidence='SRC ui/StudyActivity.java:613-614')
e('StudyActivity$4.onCardChanged', 'S_STUDY', 'ENTERS', 'the next card is dequeued and displayed', needs_state=state_text('a card was already displayed and graded once in this process (prevCard tracking)', ('session',)), evidence='SRC ui/StudyActivity.java:588-619')

# GradeButtonsFragment: buttons_root click/touch pass-through, per-grade buttons, long-press help text
e('S_STUDY', 'GradeButtonsFragment.onAttach', 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/GradeButtonsFragment.java:98-119')
e('GradeButtonsFragment.onAttach', 'GradeButtonsFragment.onCreateView', 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/GradeButtonsFragment.java:127-179')
gui('S_STUDY', 'GradeButtonsFragment$1.onClick', 'Tap the blank area of the grade-buttons bar', needs_state=state_text('the answer is shown (the grade buttons are visible)', ('session',)), evidence=FW_VIEW + '; SRC ui/GradeButtonsFragment.java:150-154')
e('GradeButtonsFragment$1.onClick', 'QACardActivity.onClickAnswerView', 'CALL', 'activity.onClickAnswerView()', evidence='SRC ui/GradeButtonsFragment.java:151-153')
gui('S_STUDY', 'GradeButtonsFragment$3.onClick', 'Tap a grade button (0-5)', needs_state=state_text('the answer is shown (the grade buttons are visible)', ('session',)), evidence=FW_VIEW + '; SRC ui/GradeButtonsFragment.java:171-173,185-191')
e('GradeButtonsFragment$3.onClick', 'GradeButtonsFragment$5.onGradeButtonClick', 'CALL', 'onGradeButtonClickListener.onGradeButtonClick(grade)', evidence='SRC ui/GradeButtonsFragment.java:187-189')
gui('S_STUDY', 'GradeButtonsFragment$4.onLongClick', 'Long-press a grade button (0-5)', needs_state=state_text('the answer is shown (the grade buttons are visible)', ('session',)), evidence=FW_VIEW + '; SRC ui/GradeButtonsFragment.java:171-173,193-209')
e('GradeButtonsFragment.setVisibility', 'GradeButtonsFragment$6.run', 'FRAMEWORK', 'handler.post(...) runs once the fragment view is attached', evidence=FW_HANDLER + '; SRC ui/GradeButtonsFragment.java:245-251')

# ---- QuizActivity (reached via the quiz launcher dialog, see below)
for cb in ('onCreate', 'onSaveInstanceState', 'onCreateOptionsMenu', 'onOptionsItemSelected'):
    e('QuizActivity.<init>', 'QuizActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/QuizActivity.java:86-164')
e('QuizActivity.onCreate', 'QuizActivity$QuizQueueManagerLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'getMultipleLoaderManager().registerLoaderCallbacks(...); startInit() starts loading', evidence=FW_LOADER + '; SRC ui/QuizActivity.java:131,133')
e('QuizActivity$QuizQueueManagerLoaderCallbacks.onCreateLoader', 'QuizActivity$QuizQueueManagerLoader.dbLoadInBackground', 'ASYNC', 'loader.forceLoad()', evidence=FW_LOADER + '; SRC ui/QuizActivity.java:290-294; ui/loader/DBLoader.java:41-50')
e('QuizActivity$QuizQueueManagerLoader.dbLoadInBackground', 'QuizActivity$QuizQueueManagerLoaderCallbacks.onLoadFinished', 'ASYNC', 'the built QuizQueueManager is delivered on the main thread', evidence=FW_LOADER + '; SRC ui/QuizActivity.java:297-300')
e('QuizActivity$QuizQueueManagerLoaderCallbacks.onLoadFinished', 'QACardActivity.onPostInit', 'CALL', 'both this loader and the Setting/CardTTSUtil loaders have reported', evidence='SRC ui/QuizActivity.java:298-299')
e('QuizActivity.onPostInit', 'QuizActivity.showNoItemDialog', 'CALL', 'the deck has no card to quiz', guard='queueManager.dequeue() == null', evidence='SRC ui/QuizActivity.java:108-111')
gui('S_DLG_NO_ITEM', 'QuizActivity$4.onClick', 'Tap Back (quiz, no card)', evidence=FW_DIALOGFRAG + '; SRC ui/QuizActivity.java:453-471')
e('QuizActivity$4.onClick', 'S_EXIT', 'ENTERS', 'finish()', evidence='SRC ui/QuizActivity.java:457-463')
e('QuizActivity$3.onCancel', 'S_EXIT', 'ENTERS', 'finish()', evidence='SRC ui/QuizActivity.java:465-469')
e('QuizActivity.onPostInit', 'QuizActivity.setupGradeButtons', 'CALL', 'the deck has at least one card', needs_state=NEED_CARD, evidence='SRC ui/QuizActivity.java:112-116')
e('QuizActivity.setupGradeButtons', 'GradeButtonsFragment.<init>', 'CALL', 'a new GradeButtonsFragment is added to buttons_root', evidence='SRC ui/QuizActivity.java:328-340')
e('QuizActivity.onPostInit', 'S_QUIZ', 'ENTERS', 'displayCard(false) shows the first card', needs_state=NEED_CARD, evidence='SRC ui/QuizActivity.java:112-116')
e('S_QUIZ', 'QuizActivity.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is inflated (quiz_activity_menu)', evidence=FW_MENU + '; SRC ui/QuizActivity.java:147-151')
e('S_QUIZ', 'QuizActivity.onOptionsItemSelected', 'FRAMEWORK', 'tap a Quiz toolbar/overflow menu item', gui=['Tap a menu item in Quiz'], evidence=FW_MENU + '; SRC ui/QuizActivity.java:153-164')
e('QuizActivity.onOptionsItemSelected', 'DictionaryUtil.showLookupListDialog', 'CALL', 'menu_lookup', evidence='SRC ui/QuizActivity.java:156-157')
e('GradeButtonsFragment$5.onGradeButtonClick', 'QuizActivity$ChangeCardTask.doInBackground', 'ASYNC', 'onGradeButtonClickListener (shared across Study/Quiz): onCardChangedListener.onCardChanged -> QuizActivity\'s listener creates and executes a ChangeCardTask', evidence=FW_ASYNC + '; SRC ui/GradeButtonsFragment.java:211-217; ui/QuizActivity.java:392-401,407-431')
e('QuizActivity$ChangeCardTask.doInBackground', 'QuizActivity$ChangeCardTask.onPostExecute', 'ASYNC', 'the next card (or null) is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/QuizActivity.java:433-450')
e('QuizActivity$ChangeCardTask.onPostExecute', 'QuizActivity.showCompleteAllDialog', 'CALL', 'the review and new queues are both empty', guard='result == null', evidence='SRC ui/QuizActivity.java:436-439')
e('QuizActivity.showCompleteAllDialog', 'S_DLG_NO_ITEM', 'ENTERS', 'the quiz-completed dialog is shown (reuses the no-item page)', evidence='SRC ui/QuizActivity.java:354-361')
gui('S_DLG_NO_ITEM', 'QuizActivity$1.onClick', 'Tap Back (quiz completed)', evidence=FW_DIALOGFRAG + '; SRC ui/QuizActivity.java:358-360,383-390')
e('QuizActivity$1.onClick', 'S_EXIT', 'ENTERS', 'dialog.dismiss(); finish()', evidence='SRC ui/QuizActivity.java:386-389')
e('QuizActivity$ChangeCardTask.onPostExecute', 'QuizActivity.showCompleteNewDialog', 'CALL', 'the new-card queue just became empty for the first time', guard='newQueueSizeBeforeDequeue <= 0 && !isNewCardsCompleted', evidence='SRC ui/QuizActivity.java:441-444')
e('QuizActivity.showCompleteNewDialog', 'S_DLG_NO_ITEM', 'ENTERS', 'the new-cards-completed dialog is shown (Review continues the quiz; reuses the no-item page for Cancel)', evidence='SRC ui/QuizActivity.java:364-379')
gui('S_DLG_NO_ITEM', 'QuizActivity$2.onCardChanged', 'Tap Review (dismiss, continue the quiz)', evidence=FW_DIALOGFRAG + '; SRC ui/QuizActivity.java:375-376')
e('QuizActivity$ChangeCardTask.onPostExecute', 'S_QUIZ', 'ENTERS', 'the next card is displayed', needs_state=state_text('a card was already graded once in this process (totalQuizSize tracking)', ('session',)), evidence='SRC ui/QuizActivity.java:446-449')

# ---- QuizLauncherDialogFragment
e('OpenActionsFragment$1.onClick', 'QuizLauncherDialogFragment.<init>', 'CALL', 'v == quizItem: a new QuizLauncherDialogFragment is created', evidence='SRC ui/OpenActionsFragment.java:147-153')
for cb in ('onCreate', 'onAttach', 'onCreateDialog', 'onStart', 'onDestroy'):
    e('QuizLauncherDialogFragment.<init>', 'QuizLauncherDialogFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/QuizLauncherDialogFragment.java:120-213')
e('QuizLauncherDialogFragment.onStart', 'QuizLauncherDialogFragment$InitTask.doInBackground', 'ASYNC', 'new InitTask().execute()', evidence=FW_ASYNC + '; SRC ui/QuizLauncherDialogFragment.java:210-212')
e('QuizLauncherDialogFragment$InitTask.doInBackground', 'QuizLauncherDialogFragment$InitTask.onPostExecute', 'ASYNC', 'the card count is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/QuizLauncherDialogFragment.java:293-310')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$1.onCheckedChanged', 'Tap a quiz-mode radio button (Group / Category / Range)', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:152-154,215-228')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$2.onClick', 'Tap "Start quiz"', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:148-150,231-268')
e('QuizLauncherDialogFragment$2.onClick', 'QuizActivity.<init>', 'ENTRY', 'startActivity(QuizActivity) for the chosen group/category/range', evidence='SRC ui/QuizLauncherDialogFragment.java:233-266')
e('QuizLauncherDialogFragment$2.onClick', 'S_QUIZ', 'ENTERS', 'startActivity(QuizActivity)', evidence='SRC ui/QuizLauncherDialogFragment.java:233-266')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$3.onClick', 'Tap the category button (Category mode)', needs_state=state_text('quizByCategoryRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:190-191,270-275')
e('QuizLauncherDialogFragment$3.onClick', 'QuizLauncherDialogFragment.showCategoriesDialog', 'CALL', 'showCategoriesDialog()', evidence='SRC ui/QuizLauncherDialogFragment.java:272-274')
e('QuizLauncherDialogFragment.showCategoriesDialog', 'S_DLG_CATEGORY', 'ENTERS', 'df.show(...)', needs_state=NEED_CATEGORY, evidence='SRC ui/QuizLauncherDialogFragment.java:508-516')
e('S_DLG_CATEGORY', 'QuizLauncherDialogFragment$10.onReceiveCategory', 'CALL', 'a category is picked', needs_state=NEED_CATEGORY, evidence='SRC ui/QuizLauncherDialogFragment.java:520-531; ui/CategoryEditorFragment.java:94-109')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$4.afterTextChanged', 'Type a group size', needs_state=state_text('quizByGroupRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:169,342-373')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$5.afterTextChanged', 'Type a group number', needs_state=state_text('quizByGroupRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:175,376-405')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$6.afterTextChanged', 'Type a range start ordinal', needs_state=state_text('quizByRangeRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:183,407-441')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$7.afterTextChanged', 'Type a range end ordinal', needs_state=state_text('quizByRangeRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:187,444-482')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$8.onFocusChange', 'Leave the group-size/number field (focus lost)', needs_state=state_text('quizByGroupRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:170,176,496-506')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$9.onFocusChange', 'Leave the range-start/end field (focus lost)', needs_state=state_text('quizByRangeRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:184,188,484-494')

# ---- GestureSelectionDialogFragment (shown from Study and Preview/Edit)
for cb in ('onAttach', 'onCreate', 'onCreateView'):
    e('GestureSelectionDialogFragment.<init>', 'GestureSelectionDialogFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/GestureSelectionDialogFragment.java:76-133')
e('StudyActivity.showGesturesDialog', 'GestureSelectionDialogFragment.<init>', 'CALL', 'a new GestureSelectionDialogFragment is created', evidence='SRC ui/StudyActivity.java:645-655')
e('PreviewEditActivity.showGesturesDialog', 'GestureSelectionDialogFragment.<init>', 'CALL', 'a new GestureSelectionDialogFragment is created', evidence='SRC ui/PreviewEditActivity.java:571-583')
gui('S_DLG_GESTURE', 'GestureSelectionDialogFragment$1.onCheckedChanged', 'Toggle "Enable gestures"', evidence=FW_VIEW + '; SRC ui/GestureSelectionDialogFragment.java:100-101,193-200')
# onDismiss calls the shared BaseActivity-typed `mActivity.restartActivity()` (one compiled call site, virtual
# dispatch to whichever concrete caller opened the dialog): modelled as reaching either caller's page, same
# simplification as BaseActivity.onPause above (documented in readme_notes.md Limits).
e('GestureSelectionDialogFragment.onDismiss', 'S_STUDY', 'ENTERS', 'dismiss (Back / outside tap) after the checkbox was toggled: mActivity.restartActivity() (Study caller)', needs_state=state_text('the gesture-enabled checkbox was toggled while this dialog was open', ('settings',)), evidence='SRC ui/GestureSelectionDialogFragment.java:181-186')
e('GestureSelectionDialogFragment.onDismiss', 'S_PREVIEW_EDIT', 'ENTERS', 'dismiss (Back / outside tap) after the checkbox was toggled: mActivity.restartActivity() (Preview/Edit caller)', needs_state=state_text('the gesture-enabled checkbox was toggled while this dialog was open', ('settings',)), evidence='SRC ui/GestureSelectionDialogFragment.java:181-186')


# ================================================================== F. card management: CardEditor,
#                                                                       CardListActivity, PreviewEditActivity,
#                                                                       DetailScreen, CategoryEditorFragment,
#                                                                       AudioRecorderFragment, FileBrowserActivity
# ---- CardEditor
e('OpenActionsFragment$1.onClick', 'CardEditor.<init>', 'ENTRY', 'v == editItem: startActivity(CardEditor)', evidence='SRC ui/OpenActionsFragment.java:129-137')
e('StudyActivity.showEditDialog', 'CardEditor.<init>', 'ENTRY', 'startActivityForResult(CardEditor)', evidence='SRC ui/StudyActivity.java:662-668')
for cb in ('onCreate', 'onDestroy', 'onBackPressed', 'onCreateOptionsMenu', 'onOptionsItemSelected', 'onRequestPermissionsResult', 'onActivityResult', 'onConfigurationChanged'):
    e('CardEditor.<init>', 'CardEditor.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/CardEditor.java:101-419')
e('CardEditor.onCreate', 'CardEditor$InitTask.doInBackground', 'ASYNC', 'new InitTask().execute()', evidence=FW_ASYNC + '; SRC ui/CardEditor.java:105-106')
e('CardEditor$InitTask.doInBackground', 'CardEditor$InitTask.onPostExecute', 'ASYNC', 'the card/category/learning-data are delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CardEditor.java:512-560')
e('CardEditor$InitTask.onPostExecute', 'S_CARD_EDITOR', 'ENTERS', 'the editor fields are populated and shown', evidence='SRC ui/CardEditor.java:544-559')
e('S_CARD_EDITOR', 'CardEditor.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is inflated (card_editor_menu)', evidence=FW_MENU + '; SRC ui/CardEditor.java:162-166')
e('S_CARD_EDITOR', 'CardEditor.onOptionsItemSelected', 'FRAMEWORK', 'tap a CardEditor toolbar/overflow menu item', gui=['Tap a menu item in the card editor'], evidence=FW_MENU + '; SRC ui/CardEditor.java:168-204')
e('CardEditor.onOptionsItemSelected', 'CardEditor$InitTask.onPostExecute', 'RESULT', 'save: startActivityForResult(FileBrowserActivity) for an image returns', env=ENV_PICKER,
  guard='the focused field is question/answer/note', evidence=FW_RESULT + '; SRC ui/CardEditor.java:180-186,361-388')
e('CardEditor.onOptionsItemSelected', 'S_FILEBROWSER', 'ENTERS', 'editor_menu_image: startActivityForResult(FileBrowserActivity, image extensions)', env=ENV_PICKER,
  guard='the focused field is question/answer/note', evidence='SRC ui/CardEditor.java:180-186')
e('CardEditor.onOptionsItemSelected', 'CardEditor.addExistingAudio', 'CALL', 'add_existing_audio', guard='the focused field is question/answer', evidence='SRC ui/CardEditor.java:187-191')
e('CardEditor.onOptionsItemSelected', 'CardEditor.addNewAudio', 'CALL', 'add_new_audio', guard='the focused field is question/answer', evidence='SRC ui/CardEditor.java:192-196')
e('CardEditor.onOptionsItemSelected', 'CardEditor.removeAudio', 'CALL', 'remove_audio', guard='the focused field is question/answer', evidence='SRC ui/CardEditor.java:197-201')
e('CardEditor.addExistingAudio', 'S_DLG_AUDIO_OVERRIDE', 'ENTERS', 'the focused field already has an <audio src=...> tag', needs_state=NEED_PASSWORD_AUDIO, evidence='SRC ui/CardEditor.java:249-261')
gui('S_DLG_AUDIO_OVERRIDE', 'CardEditor$3.onClick', 'Tap Yes (existing audio -> browse)', needs_state=NEED_PASSWORD_AUDIO, evidence=FW_DIALOGFRAG + '; SRC ui/CardEditor.java:252-257')
e('CardEditor$3.onClick', 'CardEditor.startAudioBrowser', 'CALL', 'startAudioBrowser()', evidence='SRC ui/CardEditor.java:254')
e('CardEditor.addExistingAudio', 'CardEditor.startAudioBrowser', 'CALL', 'the focused field has no audio tag yet', evidence='SRC ui/CardEditor.java:258-260')
e('CardEditor.startAudioBrowser', 'S_FILEBROWSER', 'ENTERS', 'startActivityForResult(FileBrowserActivity, audio extensions)', env=ENV_PICKER, evidence='SRC ui/CardEditor.java:290-295')
e('CardEditor.addNewAudio', 'S_DLG_AUDIO_OVERRIDE', 'ENTERS', 'the focused field already has an <audio src=...> tag', needs_state=NEED_PASSWORD_AUDIO, evidence='SRC ui/CardEditor.java:263-275')
gui('S_DLG_AUDIO_OVERRIDE', 'CardEditor$4.onClick', 'Tap Yes (existing audio -> record new)', needs_state=NEED_PASSWORD_AUDIO, evidence=FW_DIALOGFRAG + '; SRC ui/CardEditor.java:266-271')
e('CardEditor$4.onClick', 'CardEditor.startAudioRecorderWithPermissionCheck', 'CALL', 'startAudioRecorderWithPermissionCheck()', evidence='SRC ui/CardEditor.java:268')
e('CardEditor.addNewAudio', 'CardEditor.startAudioRecorderWithPermissionCheck', 'CALL', 'the focused field has no audio tag yet', evidence='SRC ui/CardEditor.java:272-274')
e('CardEditor.startAudioRecorderWithPermissionCheck', 'CardEditor.startAudioRecorder', 'CALL', 'RECORD_AUDIO is already granted', env=ENV_MIC, evidence='SRC ui/CardEditor.java:299-306')
e('CardEditor.startAudioRecorderWithPermissionCheck', 'CardEditor.onRequestPermissionsResult', 'FRAMEWORK', 'RECORD_AUDIO is requested; the system calls onRequestPermissionsResult once the user answers',
  evidence='INFERRED core/java/android/app/Activity.java requestPermissions forwards to the PackageManager and the result returns through onRequestPermissionsResult (platform source not read for this exact callback path); SRC ui/CardEditor.java:299-306,207-222')
e('CardEditor.onRequestPermissionsResult', 'CardEditor.startAudioRecorder', 'CALL', 'the user granted RECORD_AUDIO', env=ENV_MIC, evidence='SRC ui/CardEditor.java:207-222')
e('CardEditor.startAudioRecorder', 'AudioRecorderFragment.<init>', 'CALL', 'a new AudioRecorderFragment is added (commitAllowingStateLoss)', evidence='SRC ui/CardEditor.java:313-338')
e('CardEditor.startAudioRecorder', 'S_DLG_AUDIO_RECORDER', 'ENTERS', 'the recorder dialog is added', evidence='SRC ui/CardEditor.java:336-338')
e('AudioRecorderFragment.setAudioRecorderResultListener', 'CardEditor$5.onReceiveAudio', 'REGISTER', 'the listener passed by CardEditor.startAudioRecorder is stored', evidence='SRC ui/CardEditor.java:325-334')
e('CardEditor.onOptionsItemSelected', 'CardEditor.setInitRadioButton', 'CALL', 'save: SaveCardTask.execute()', evidence='SRC ui/CardEditor.java:171-174')
for cb in ('onAttach', 'onCreate', 'onCreateDialog'):
    e('S_DLG_AUDIO_RECORDER', 'AudioRecorderFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/AudioRecorderFragment.java:83-118')
e('S_DLG_AUDIO_RECORDER', 'AudioRecorderFragment$1.onClick', 'FRAMEWORK', 'tap Record / Play / Save', gui=['Tap Record, Play or Save'], evidence=FW_VIEW + '; SRC ui/AudioRecorderFragment.java:44-81,99-108')
e('AudioRecorderFragment$1.onClick', 'AudioRecorderFragment.onRecord', 'CALL', 'v == mRecordButton', env=ENV_MIC, evidence='SRC ui/AudioRecorderFragment.java:46-60')
e('AudioRecorderFragment.onRecord', 'AudioRecorderFragment.startRecording', 'CALL', 'mStartRecording toggled on', env=ENV_MIC, evidence='SRC ui/AudioRecorderFragment.java:125-131,168-182')
e('AudioRecorderFragment$1.onClick', 'AudioRecorderFragment.onPlay', 'CALL', 'v == mPlayButton', needs_state=NEED_AUDIO_RECORDED, evidence='SRC ui/AudioRecorderFragment.java:61-73')
e('AudioRecorderFragment.onPlay', 'AudioRecorderFragment.startPlaying', 'CALL', 'mStartPlaying toggled on', needs_state=NEED_AUDIO_RECORDED, evidence='SRC ui/AudioRecorderFragment.java:133-139,141-161')
e('AudioRecorderFragment.startPlaying', 'AudioRecorderFragment$2.onCompletion', 'FRAMEWORK', 'the recorded clip finishes playing', evidence=FW_MEDIAPLAYER + '; SRC ui/AudioRecorderFragment.java:143-153')
e('AudioRecorderFragment$1.onClick', 'CardEditor$5.onReceiveAudio', 'CALL', 'v == mSaveButton: audioRecorderResultListener.onReceiveAudio()', needs_state=NEED_AUDIO_RECORDED, evidence='SRC ui/AudioRecorderFragment.java:75-77')
e('CardEditor$5.onReceiveAudio', 'CardEditor.addTextToView', 'CALL', 'the <audio src=...> tag is inserted at the cursor', evidence='SRC ui/CardEditor.java:326-333')
e('CardEditor.setInitRadioButton', 'CardEditor$6.onCheckedChanged', 'FRAMEWORK', 'toggle Add back / Add here (new-card radio group, only shown for a new card)', gui=['Toggle the Add-back / Add-here radio'],
  needs_state=state_text('isEditNew is true (adding a new card, not editing an existing one)', ('data',)), evidence=FW_VIEW + '; SRC ui/CardEditor.java:421-458')
e('CardEditor$InitTask.onPostExecute', 'CardEditor$7.onClick', 'FRAMEWORK', 'tap the category button', gui=['Tap the category button'], evidence=FW_VIEW + '; SRC ui/CardEditor.java:553,563-574')
e('CardEditor$7.onClick', 'CategoryEditorFragment.<init>', 'CALL', 'a new CategoryEditorFragment is shown', evidence='SRC ui/CardEditor.java:566-572')
e('CardEditor$7.onClick', 'S_DLG_CATEGORY', 'ENTERS', 'df.show(...)', evidence='SRC ui/CardEditor.java:572')
e('S_DLG_CATEGORY', 'CardEditor$8.onReceiveCategory', 'CALL', 'a category is picked', evidence='SRC ui/CardEditor.java:634-639; ui/CategoryEditorFragment.java:94-109')
e('CardEditor$8.onReceiveCategory', 'CardEditor.updateCategoryView', 'CALL', 'updateCategoryView()', evidence='SRC ui/CardEditor.java:637')
e('CardEditor.onBackPressed', 'S_DLG_EDIT_DISCARD', 'ENTERS', 'the fields changed and this is not a new card', guard='!isEditNew && fields changed', evidence='SRC ui/CardEditor.java:127-159')
gui('S_DLG_EDIT_DISCARD', 'CardEditor$2.onClick', 'Tap Yes (save before leaving)', guard='!isEditNew && fields changed', evidence=FW_DIALOGFRAG + '; SRC ui/CardEditor.java:135-140')
gui('S_DLG_EDIT_DISCARD', 'CardEditor$1.onClick', 'Tap No (discard)', evidence=FW_DIALOGFRAG + '; SRC ui/CardEditor.java:141-147')
e('CardEditor$1.onClick', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_CANCELED); finish() (reuses the caller\'s page: Study or Preview/Edit)', evidence='SRC ui/CardEditor.java:143-146')
e('CardEditor.onBackPressed', 'S_PREVIEW_EDIT', 'ENTERS', 'isEditNew, or nothing changed: setResult(RESULT_CANCELED); finish()', evidence='SRC ui/CardEditor.java:153-158')
e('CardEditor$SaveCardTask.doInBackground', 'CardEditor$SaveCardTask.onPostExecute', 'ASYNC', 'the saved card is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CardEditor.java:623-630')
e('CardEditor$SaveCardTask.onPostExecute', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_OK); finish() (reuses the caller\'s page: Study or Preview/Edit)', evidence='SRC ui/CardEditor.java:624-629')
e('CardEditor$2.onClick', 'CardEditor$SaveCardTask.doInBackground', 'ASYNC', 'new SaveCardTask().execute()', evidence=FW_ASYNC + '; SRC ui/CardEditor.java:137-139')

# ---- CategoryEditorFragment (shown from Study / Quiz launcher / Preview-Edit / CardEditor)
for cb in ('onAttach', 'onCreate', 'onCreateView', 'onDestroy'):
    e('CategoryEditorFragment.<init>', 'CategoryEditorFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/CategoryEditorFragment.java:50-92')
e('CategoryEditorFragment.onCreateView', 'CategoryEditorFragment$InitTask.doInBackground', 'ASYNC', 'new InitTask().execute()', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:77-78')
e('CategoryEditorFragment$InitTask.doInBackground', 'CategoryEditorFragment$InitTask.onPostExecute', 'ASYNC', 'the category list is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:152-172')
e('CategoryEditorFragment$InitTask.onPostExecute', 'CategoryEditorFragment.enableListeners', 'CALL', 'enableListeners()', evidence='SRC ui/CategoryEditorFragment.java:170')
e('CategoryEditorFragment.enableListeners', 'CategoryEditorFragment$1.onClick', 'FRAMEWORK', 'tap OK / New / Edit / Delete', gui=['Tap OK, New, Edit or Delete in the category dialog'], evidence=FW_VIEW + '; SRC ui/CategoryEditorFragment.java:94-126,412-417')
e('CategoryEditorFragment.onCreateView', 'CategoryEditorFragment$2.onItemClick', 'FRAMEWORK', 'tap a category row', gui=['Tap a category in the list'], evidence=FW_VIEW + '; SRC ui/CategoryEditorFragment.java:76,404-410')
e('CategoryEditorFragment$1.onClick', 'StudyActivity$3.onReceiveCategory', 'CALL', 'v == okButton: resultListener.onReceiveCategory(selectedCategory) (Study caller)', evidence='SRC ui/CategoryEditorFragment.java:96-109')
e('CategoryEditorFragment$1.onClick', 'CardEditor$8.onReceiveCategory', 'CALL', 'v == okButton: resultListener.onReceiveCategory(selectedCategory) (CardEditor caller)', evidence='SRC ui/CategoryEditorFragment.java:96-109')
e('CategoryEditorFragment$1.onClick', 'PreviewEditActivity$11.onReceiveCategory', 'CALL', 'v == okButton: resultListener.onReceiveCategory(selectedCategory) (Preview/Edit caller)', evidence='SRC ui/CategoryEditorFragment.java:96-109')
e('CategoryEditorFragment$1.onClick', 'QuizLauncherDialogFragment$10.onReceiveCategory', 'CALL', 'v == okButton: resultListener.onReceiveCategory(selectedCategory) (Quiz-launcher caller)', evidence='SRC ui/CategoryEditorFragment.java:96-109')
e('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$NewCategoryTask.doInBackground', 'ASYNC', 'v == newButton', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:111-114')
e('CategoryEditorFragment$NewCategoryTask.doInBackground', 'CategoryEditorFragment$NewCategoryTask.onPostExecute', 'ASYNC', 'the created/found category is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:258-278')
e('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$EditCategoryTask.doInBackground', 'ASYNC', 'v == editButton', needs_state=NEED_CATEGORY, evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:116-119')
e('CategoryEditorFragment$EditCategoryTask.doInBackground', 'CategoryEditorFragment$EditCategoryTask.onPostExecute', 'ASYNC', 'the edited category is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:207-234')
e('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$DeleteCategoryTask.doInBackground', 'ASYNC', 'v == deleteButton', needs_state=NEED_CATEGORY, evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:121-124')
e('CategoryEditorFragment$DeleteCategoryTask.doInBackground', 'CategoryEditorFragment$DeleteCategoryTask.onPostExecute', 'ASYNC', 'the deletion is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:296-325')

# ---- CardListActivity
e('OpenActionsFragment$1.onClick', 'CardListActivity.<init>', 'ENTRY', 'v == listItem: startActivity(CardListActivity)', evidence='SRC ui/OpenActionsFragment.java:139-145')
e('PreviewEditActivity.onOptionsItemSelected', 'CardListActivity.<init>', 'ENTRY', 'editmenu_list_id: startActivityForResult(CardListActivity)', evidence='SRC ui/PreviewEditActivity.java:285-294')
for cb in ('onCreate', 'onDestroy', 'onActivityResult', 'onCreateOptionsMenu', 'onOptionsItemSelected'):
    e('CardListActivity.<init>', 'CardListActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/CardListActivity.java:112-421')
e('CardListActivity.onCreate', 'CardListActivity$CardWrapperLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'multipleLoaderManager registers the CardWrapperList loader', evidence=FW_LOADER + '; SRC ui/CardListActivity.java:144-146,617-624')
e('CardListActivity$CardWrapperLoaderCallbacks.onCreateLoader', 'DBLoader.loadInBackground', 'ASYNC', 'loader.forceLoad()', evidence=FW_LOADER + '; SRC ui/CardListActivity.java:618-624; ui/loader/DBLoader.java:41-50')
e('DBLoader.loadInBackground', 'CardListActivity$CardWrapperLoaderCallbacks.onLoadFinished', 'ASYNC', 'the card-wrapper list is delivered on the main thread', evidence=FW_LOADER + '; SRC ui/CardListActivity.java:627-633')
e('MultipleLoaderManager.checkAllLoadersCompleted', 'CardListActivity$11.run', 'FRAMEWORK', 'handler.post(onAllLoaderCompletedRunnable): CardListActivity caller', evidence=FW_HANDLER + '; SRC ui/loader/MultipleLoaderManager.java:104-114; ui/CardListActivity.java:145,632')
e('CardListActivity$11.run', 'S_CARD_LIST', 'ENTERS', 'the adapter is attached and the list is shown', needs_state=NEED_CARD, evidence='SRC ui/CardListActivity.java:640-655')
e('S_CARD_LIST', 'CardListActivity.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu (with SearchView) is inflated', evidence=FW_MENU + '; SRC ui/CardListActivity.java:176-186')
e('CardListActivity.onCreateOptionsMenu', 'CardListActivity$8.onQueryTextChange', 'FRAMEWORK', 'type in the search box (also used to clear a previous search)', gui=['Type in the card-list search box'], evidence=FW_VIEW + '; SRC ui/CardListActivity.java:183,389-407')
e('S_CARD_LIST', 'CardListActivity.onOptionsItemSelected', 'FRAMEWORK', 'tap a CardList toolbar/overflow menu item', gui=['Tap a menu item in the card list'], evidence=FW_MENU + '; SRC ui/CardListActivity.java:409-421')
e('CardListActivity.onOptionsItemSelected', 'CardListActivity.showSortListDialog', 'CALL', 'sort', evidence='SRC ui/CardListActivity.java:412-414,319-340')
e('CardListActivity.showSortListDialog', 'S_DLG_CARD_SORT', 'ENTERS', 'builder.show()', evidence='SRC ui/CardListActivity.java:319-339')
gui('S_DLG_CARD_SORT', 'CardListActivity$3.onClick', 'Tap a sort method', evidence=FW_DIALOGFRAG + '; SRC ui/CardListActivity.java:328-338')
e('CardListActivity$3.onClick', 'CardListActivity.sortList', 'CALL', 'sortList(SortMethod.valueOf(items[which]))', evidence='SRC ui/CardListActivity.java:333')
e('CardListActivity.onOptionsItemSelected', 'CardListActivity.showHideAnswers', 'CALL', 'show_hide_answers', evidence='SRC ui/CardListActivity.java:415-417,303-317')
e('S_CARD_LIST', 'CardListActivity$9.onItemClick', 'FRAMEWORK', 'tap a card row', gui=['Tap a card in the list'], needs_state=NEED_CARD, evidence=FW_VIEW + '; SRC ui/CardListActivity.java:423-435,648')
e('CardListActivity$9.onItemClick', 'CardListActivity.showListItemPopup', 'CALL', 'the answer was already visible: show the popup menu', needs_state=state_text('the row\'s answer is already visible (a second tap)', ('session',)), evidence='SRC ui/CardListActivity.java:431-433')
e('CardListActivity.showListItemPopup', 'CardListActivity$1.onMenuItemClick', 'FRAMEWORK', 'tap a popup item (mark as learned/forgotten/new/learned-forever)', gui=['Tap a row\'s popup menu item'], evidence=FW_MATERIAL + '; SRC ui/CardListActivity.java:188-209')
e('S_CARD_LIST', 'CardListActivity$10.onItemLongClick', 'FRAMEWORK', 'long-press a card row', gui=['Long-press a card in the list'], needs_state=NEED_CARD, evidence=FW_VIEW + '; SRC ui/CardListActivity.java:437-446,649')
e('CardListActivity$10.onItemLongClick', 'CardListActivity.showListItemLongClickPopup', 'CALL', 'showListItemLongClickPopup(view, card)', evidence='SRC ui/CardListActivity.java:442-443')
e('CardListActivity.showListItemLongClickPopup', 'CardListActivity$2.onMenuItemClick', 'FRAMEWORK', 'tap a popup item (Edit / Detail / Preview-edit)', gui=['Tap a row\'s long-press popup item'], evidence=FW_MATERIAL + '; SRC ui/CardListActivity.java:212-233')
e('CardListActivity$2.onMenuItemClick', 'CardEditor.<init>', 'ENTRY', 'itemId == edit: startActivity(CardEditor)', evidence='SRC ui/CardListActivity.java:223-224,236-241')
e('CardListActivity$2.onMenuItemClick', 'DetailScreen.<init>', 'ENTRY', 'itemId == detail: startActivity(DetailScreen)', evidence='SRC ui/CardListActivity.java:225-226,243-248')
e('CardListActivity$2.onMenuItemClick', 'PreviewEditActivity.<init>', 'ENTRY', 'itemId == preview_edit: startActivity(PreviewEditActivity)', evidence='SRC ui/CardListActivity.java:227-228,250-255')
e('CardListActivity.onActivityResult', 'CardListActivity.restartActivity', 'CALL', 'RESULT_OK: refresh the list', evidence='SRC ui/CardListActivity.java:167-173')
e('CardListActivity.restartActivity', 'S_CARD_LIST', 'ENTERS', 'finish(); startActivity(CardListActivity)', evidence='SRC ui/CardListActivity.java:158-164')

# ---- DetailScreen
e('CardListActivity$2.onMenuItemClick', 'DetailScreen.<init>', 'ENTRY', 'itemId == detail: startActivity(DetailScreen) (duplicate text for clarity; see above)', evidence='SRC ui/CardListActivity.java:225-226,243-248')
for cb in ('onCreate', 'onDestroy', 'onCreateOptionsMenu', 'onOptionsItemSelected'):
    e('DetailScreen.<init>', 'DetailScreen.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/DetailScreen.java:82-151')
e('DetailScreen.onCreate', 'DetailScreen$InitTask.doInBackground', 'ASYNC', 'new InitTask().execute()', evidence=FW_ASYNC + '; SRC ui/DetailScreen.java:103-104')
e('DetailScreen$InitTask.doInBackground', 'DetailScreen$InitTask.onPostExecute', 'ASYNC', 'the card is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/DetailScreen.java:262-283')
e('DetailScreen$InitTask.onPostExecute', 'S_DETAIL', 'ENTERS', 'the raw fields are populated and shown', evidence='SRC ui/DetailScreen.java:276-282')
e('S_DETAIL', 'DetailScreen.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is inflated (detail_screen_menu)', evidence=FW_MENU + '; SRC ui/DetailScreen.java:108-111')
e('S_DETAIL', 'DetailScreen.onOptionsItemSelected', 'FRAMEWORK', 'tap a Detail toolbar/overflow menu item', gui=['Tap a menu item in Detail'], evidence=FW_MENU + '; SRC ui/DetailScreen.java:114-151')
e('DetailScreen.onOptionsItemSelected', 'S_DLG_DETAIL_SAVE', 'ENTERS', 'save', evidence='SRC ui/DetailScreen.java:117-131')
gui('S_DLG_DETAIL_SAVE', 'DetailScreen$1.onClick', 'Tap OK (confirm save)', evidence=FW_DIALOGFRAG + '; SRC ui/DetailScreen.java:121-128')
e('DetailScreen$1.onClick', 'DetailScreen$SaveCardTask.doInBackground', 'ASYNC', 'new SaveCardTask().execute()', evidence=FW_ASYNC + '; SRC ui/DetailScreen.java:124-125')
e('DetailScreen$SaveCardTask.doInBackground', 'DetailScreen$SaveCardTask.onPostExecute', 'ASYNC', 'the save result (or exception) is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/DetailScreen.java:213-235')
e('DetailScreen$SaveCardTask.onPostExecute', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_OK); finish() (the caller, Preview/Edit, restarts)', guard='no parse exception', evidence='SRC ui/DetailScreen.java:224-234')
e('DetailScreen.onOptionsItemSelected', 'S_DETAIL', 'ENTERS', 'reset: the fields are reset to defaults in place (no navigation)', evidence='SRC ui/DetailScreen.java:133-148')

# ---- FileBrowserActivity (standalone file browser: CardEditor image/audio, DatabaseMerger, ShareScreen, Settings typeface)
for cb in ('onCreate',):
    e('S_FILEBROWSER', 'FileBrowserActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/FileBrowserActivity.java:37-57')
e('FileBrowserActivity$1.onFileBrowserFileClick', 'FileBrowserActivity.fileClickAction', 'CALL', 'fileClickAction(file)', evidence='SRC ui/FileBrowserActivity.java:68-71')
e('FileBrowserActivity.fileClickAction', 'S_CARD_EDITOR', 'ENTERS', 'setResult(RESULT_OK); finish() (the CardEditor caller restarts with the picked path)', evidence='SRC ui/FileBrowserActivity.java:59-65')
e('FileBrowserActivity.fileClickAction', 'S_DB_MERGER', 'ENTERS', 'setResult(RESULT_OK); finish() (the DatabaseMerger caller restarts with the picked path)', evidence='SRC ui/FileBrowserActivity.java:59-65')
e('FileBrowserActivity.fileClickAction', 'S_SHARE_SCREEN', 'ENTERS', 'setResult(RESULT_OK); finish() (the ShareScreen caller restarts with the picked path)', evidence='SRC ui/FileBrowserActivity.java:59-65')
e('FileBrowserActivity.fileClickAction', 'S_SETTINGS', 'ENTERS', 'setResult(RESULT_OK); finish() (the SettingsScreen typeface caller restarts with the picked path)', evidence='SRC ui/FileBrowserActivity.java:59-65')

# ---- PreviewEditActivity
e('OpenActionsFragment$1.onClick', 'PreviewEditActivity.<init>', 'ENTRY', 'v == editItem: startActivity(PreviewEditActivity)', evidence='SRC ui/OpenActionsFragment.java:129-137')
e('EditTabFragment$1.onFileBrowserFileClick', 'PreviewEditActivity.<init>', 'ENTRY', 'Edit tab (dead code: EditTabFragment is never instantiated, see section L)', evidence='SRC ui/EditTabFragment.java:51-57')
for cb in ('onCreate', 'onDestroy', 'onPause', 'onSaveInstanceState', 'onCreateOptionsMenu', 'onOptionsItemSelected', 'onActivityResult'):
    e('PreviewEditActivity.<init>', 'PreviewEditActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/PreviewEditActivity.java:95-423')
e('PreviewEditActivity.onPostInit', 'PreviewEditActivity.composeViews', 'CALL', 'composeViews()', evidence='SRC ui/PreviewEditActivity.java:161')
e('PreviewEditActivity.onPostInit', 'PreviewEditActivity.setViewListeners', 'CALL', 'setViewListeners()', evidence='SRC ui/PreviewEditActivity.java:163')
e('PreviewEditActivity.onPostInit', 'S_PREVIEW_EDIT', 'ENTERS', 'updateCardFrontSide(); updateTitle()', evidence='SRC ui/PreviewEditActivity.java:164-168')
e('S_PREVIEW_EDIT', 'PreviewEditActivity.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu (with SearchView) is inflated', evidence=FW_MENU + '; SRC ui/PreviewEditActivity.java:245-254')
e('PreviewEditActivity.onCreateOptionsMenu', 'PreviewEditActivity$12.onQueryTextSubmit', 'FRAMEWORK', 'submit a search (#id or text)', gui=['Search for a card by id or text'], evidence=FW_VIEW + '; SRC ui/PreviewEditActivity.java:250,750-763')
e('PreviewEditActivity$12.onQueryTextSubmit', 'PreviewEditActivity.searchCard', 'CALL', 'searchCard(text)', evidence='SRC ui/PreviewEditActivity.java:759')
e('PreviewEditActivity.searchCard', 'PreviewEditActivity$SearchCardTask.doInBackground', 'ASYNC', 'new SearchCardTask().execute(text)', evidence=FW_ASYNC + '; SRC ui/PreviewEditActivity.java:588-589')
e('PreviewEditActivity$SearchCardTask.doInBackground', 'PreviewEditActivity$SearchCardTask.onPostExecute', 'ASYNC', 'the found card (or null) is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/PreviewEditActivity.java:738-747')
e('PreviewEditActivity$SearchCardTask.onPostExecute', 'S_PREVIEW_EDIT', 'ENTERS', 'the found card is displayed', guard='result != null', evidence='SRC ui/PreviewEditActivity.java:739-746')
e('S_PREVIEW_EDIT', 'PreviewEditActivity.onOptionsItemSelected', 'FRAMEWORK', 'tap a Preview/Edit toolbar/overflow menu item', gui=['Tap a menu item in Preview/Edit'], evidence=FW_MENU + '; SRC ui/PreviewEditActivity.java:257-423')
e('PreviewEditActivity.onOptionsItemSelected', 'QACardActivity.speakQuestion', 'CALL', 'menuspeakquestion', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:259-263')
e('PreviewEditActivity.onOptionsItemSelected', 'QACardActivity.speakAnswer', 'CALL', 'menuspeakanswer', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:264-268')
e('PreviewEditActivity.onOptionsItemSelected', 'S_SETTINGS', 'ENTERS', 'editmenu_settings_id: startActivityForResult(SettingsScreen)', evidence='SRC ui/PreviewEditActivity.java:269-273')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.deleteCard', 'CALL', 'editmenu_delete_id', evidence='SRC ui/PreviewEditActivity.java:274-276,510-525')
e('PreviewEditActivity.deleteCard', 'S_DLG_DELETE_CARD', 'ENTERS', 'the confirm dialog is shown', evidence='SRC ui/PreviewEditActivity.java:510-525')
gui('S_DLG_DELETE_CARD', 'PreviewEditActivity$6.onClick', 'Tap Yes (confirm delete)', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:515-521')
e('PreviewEditActivity$6.onClick', 'PreviewEditActivity$DeleteCardTask.doInBackground', 'ASYNC', 'new DeleteCardTask(...).execute()', evidence=FW_ASYNC + '; SRC ui/PreviewEditActivity.java:518-519')
e('PreviewEditActivity$DeleteCardTask.doInBackground', 'PreviewEditActivity$DeleteCardTask.onPostExecute', 'ASYNC', 'the delete result is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/PreviewEditActivity.java:663-684')
e('PreviewEditActivity$DeleteCardTask.onPostExecute', 'S_PREVIEW_EDIT', 'ENTERS', 'activity.restartActivity()', evidence='SRC ui/PreviewEditActivity.java:677-683')
e('PreviewEditActivity.onOptionsItemSelected', 'S_DETAIL', 'ENTERS', 'editmenu_detail_id', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:277-284')
e('PreviewEditActivity.onOptionsItemSelected', 'S_CARD_LIST', 'ENTERS', 'editmenu_list_id (duplicate text for clarity; see CardListActivity entry above)', evidence='SRC ui/PreviewEditActivity.java:285-294')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.showCategoriesDialog', 'CALL', 'menu_edit_categories', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:295-299,554-568')
e('PreviewEditActivity.showCategoriesDialog', 'S_DLG_CATEGORY', 'ENTERS', 'df.show(...)', evidence='SRC ui/PreviewEditActivity.java:554-568')
e('PreviewEditActivity.onOptionsItemSelected', 'S_EXT_BROWSER', 'ENTERS', 'editmenu_help', env=ENV_EXT_BROWSER, evidence='SRC ui/PreviewEditActivity.java:300-306')
e('PreviewEditActivity.onOptionsItemSelected', 'S_CARD_PLAYER', 'ENTERS', 'menu_card_player', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:307-316')
e('PreviewEditActivity.onOptionsItemSelected', 'S_PREVIEW_EDIT', 'ENTERS', 'menu_context_paste (restartActivity) / menu_context_swap_current (restartActivity): no further page', guard='menu_context_paste or menu_context_swap_current', evidence='SRC ui/PreviewEditActivity.java:323-337')
e('PreviewEditActivity.onOptionsItemSelected', 'S_DLG_RESET_PREF', 'ENTERS', 'menu_context_wipe: AMGUIUtility.doConfirmProgressTask shows a confirm dialog (reuses the Misc-tab reset-confirm page)', evidence='SRC ui/PreviewEditActivity.java:342-350; utils/AMGUIUtility.java:121-138')
gui('S_DLG_RESET_PREF', 'PreviewEditActivity$1.doHeavyTask', 'Tap OK (confirm wipe all learning data)', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:343-348; utils/AMGUIUtility.java:130-132')
e('PreviewEditActivity$1.doHeavyTask', 'PreviewEditActivity$1.doUITask', 'FRAMEWORK', 'doProgressTask runs doHeavyTask() on a background Thread, then posts doUITask() to the main thread', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:80-112')
e('PreviewEditActivity$1.doUITask', 'S_PREVIEW_EDIT', 'ENTERS', 'the progress dialog is dismissed (no further navigation)', evidence='SRC ui/PreviewEditActivity.java:347-348')
gui('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity$3.onClick', 'Choose the swap menu item, then tap Yes (swap question and answer of every card)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:352-367')
gui('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity$2.onClick', 'Choose the swap menu item, then tap the neutral button (swap, keep duplicates)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:368-379')
e('PreviewEditActivity$3.onClick', 'PreviewEditActivity$3$1.doHeavyTask', 'CALL', 'AMGUIUtility.doProgressTask(swapAllQA)', evidence='SRC ui/PreviewEditActivity.java:358-365')
e('PreviewEditActivity$3$1.doUITask', 'S_PREVIEW_EDIT', 'ENTERS', 'restartActivity()', evidence='SRC ui/PreviewEditActivity.java:362-364')
e('PreviewEditActivity$2.onClick', 'PreviewEditActivity$2$1.doHeavyTask', 'CALL', 'AMGUIUtility.doProgressTask(swapAllQADup)', evidence='SRC ui/PreviewEditActivity.java:369-377')
e('PreviewEditActivity$2$1.doUITask', 'S_PREVIEW_EDIT', 'ENTERS', 'restartActivity()', evidence='SRC ui/PreviewEditActivity.java:373-376')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.showGesturesDialog', 'CALL', 'menu_gestures', evidence='SRC ui/PreviewEditActivity.java:385-387,571-583')
e('PreviewEditActivity$3$1.doHeavyTask', 'PreviewEditActivity$3$1.doUITask', 'FRAMEWORK', 'doProgressTask runs doHeavyTask() on a background Thread, then posts doUITask() to the main thread', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:80-112')
e('PreviewEditActivity$2$1.doHeavyTask', 'PreviewEditActivity$2$1.doUITask', 'FRAMEWORK', 'doProgressTask runs doHeavyTask() on a background Thread, then posts doUITask() to the main thread', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:80-112')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity$4.doHeavyTask', 'CALL', 'menu_context_remove_dup: AMGUIUtility.doConfirmProgressTask(removeDuplicates)', evidence='SRC ui/PreviewEditActivity.java:388-399')
e('PreviewEditActivity$4.doUITask', 'S_PREVIEW_EDIT', 'ENTERS', 'restartActivity()', evidence='SRC ui/PreviewEditActivity.java:395-397')
e('PreviewEditActivity.onOptionsItemSelected', 'DatabaseMerger.<init>', 'ENTRY', 'menu_context_merge_db: startActivityForResult(DatabaseMerger)', evidence='SRC ui/PreviewEditActivity.java:400-404')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity$5.doHeavyTask', 'CALL', 'menu_context_shuffle: AMGUIUtility.doConfirmProgressTask(shuffleOrdinals)', evidence='SRC ui/PreviewEditActivity.java:405-416')
e('PreviewEditActivity$5.doUITask', 'S_PREVIEW_EDIT', 'ENTERS', 'restartActivity()', evidence='SRC ui/PreviewEditActivity.java:412-414')
e('PreviewEditActivity.onOptionsItemSelected', 'ShareUtil.shareCard', 'CALL', 'menu_share', evidence='SRC ui/PreviewEditActivity.java:417-419')
e('PreviewEditActivity.composeViews', 'PreviewEditActivity.setViewListeners', 'CALL', 'order of calls within onPostInit (both are explicit; kept for readability)', evidence='SRC ui/PreviewEditActivity.java:161-163')
e('PreviewEditActivity.setViewListeners', 'PreviewEditActivity$7.onClick', 'FRAMEWORK', 'tap Prev', gui=['Tap Prev in Preview/Edit'], evidence=FW_VIEW + '; SRC ui/PreviewEditActivity.java:475,592-597')
e('PreviewEditActivity$7.onClick', 'PreviewEditActivity.gotoPrev', 'CALL', 'gotoPrev()', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:594-595')
e('PreviewEditActivity.setViewListeners', 'PreviewEditActivity$8.onClick', 'FRAMEWORK', 'tap Next', gui=['Tap Next in Preview/Edit'], evidence=FW_VIEW + '; SRC ui/PreviewEditActivity.java:476,599-604')
e('PreviewEditActivity$8.onClick', 'PreviewEditActivity.gotoNext', 'CALL', 'gotoNext()', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:601-602')
e('PreviewEditActivity.setViewListeners', 'PreviewEditActivity$9.onClick', 'FRAMEWORK', 'tap New', gui=['Tap New in Preview/Edit'], evidence=FW_VIEW + '; SRC ui/PreviewEditActivity.java:477,606-616')
e('PreviewEditActivity$9.onClick', 'CardEditor.<init>', 'ENTRY', 'startActivityForResult(CardEditor, isEditNew=true)', evidence='SRC ui/PreviewEditActivity.java:607-615')
e('PreviewEditActivity.setViewListeners', 'PreviewEditActivity$10.onClick', 'FRAMEWORK', 'tap Edit', gui=['Tap Edit in Preview/Edit'], needs_state=NEED_CARD, evidence=FW_VIEW + '; SRC ui/PreviewEditActivity.java:478,618-628')
e('PreviewEditActivity$10.onClick', 'CardEditor.<init>', 'ENTRY', 'startActivityForResult(CardEditor, isEditNew=false)', needs_state=NEED_CARD, evidence='SRC ui/PreviewEditActivity.java:620-627')
e('PreviewEditActivity.onActivityResult', 'S_PREVIEW_EDIT', 'ENTERS', 'restartActivity() for every request code except RESULT_CANCELED', evidence='SRC ui/PreviewEditActivity.java:194-242,454-464')
e('S_DLG_CATEGORY', 'PreviewEditActivity$11.onReceiveCategory', 'CALL', 'a category is picked', evidence='SRC ui/PreviewEditActivity.java:630-637; ui/CategoryEditorFragment.java:94-109')
e('PreviewEditActivity$11.onReceiveCategory', 'S_PREVIEW_EDIT', 'ENTERS', 'restartActivity() for the new filter category', evidence='SRC ui/PreviewEditActivity.java:630-637')


# ================================================================== G. settings / stats
e('OpenActionsFragment$1.onClick', 'SettingsScreen.<init>', 'ENTRY', 'v == settingsItem: startActivity(SettingsScreen)', evidence='SRC ui/OpenActionsFragment.java:156-161')
for cb in ('onDestroy', 'onCreateOptionsMenu', 'onConfigurationChanged', 'onOptionsItemSelected', 'onBackPressed'):
    e('SettingsScreen.<init>', 'SettingsScreen.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/SettingsScreen.java:124-222')
e('SettingsScreen.<init>', 'SettingsScreen$SettingLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'multipleLoaderManager registers the Setting loader in onCreate', evidence=FW_LOADER + '; SRC ui/SettingsScreen.java:137-139,394-414')
e('SettingsScreen$SettingLoaderCallbacks.onCreateLoader', 'DBLoader.loadInBackground', 'ASYNC', 'loader.forceLoad()', evidence=FW_LOADER + '; SRC ui/SettingsScreen.java:398-401; ui/loader/DBLoader.java:41-50')
e('DBLoader.loadInBackground', 'SettingsScreen$SettingLoaderCallbacks.onLoadFinished', 'ASYNC', 'the Setting is delivered on the main thread', evidence=FW_LOADER + '; SRC ui/SettingsScreen.java:404-408')
e('MultipleLoaderManager.checkAllLoadersCompleted', 'SettingsScreen$6.run', 'FRAMEWORK', 'handler.post(onAllLoaderCompletedRunnable): SettingsScreen caller', evidence=FW_HANDLER + '; SRC ui/loader/MultipleLoaderManager.java:104-114; ui/SettingsScreen.java:138,268')
e('SettingsScreen$6.run', 'SettingsScreen.updateViews', 'CALL', 'onPostInitRunnable.run() calls the body (settingDao = ...; setContentView; updateViews())', evidence='SRC ui/SettingsScreen.java:268-353')
e('SettingsScreen.updateViews', 'S_SETTINGS', 'ENTERS', 'setContentView(settings_screen); the widgets are populated', evidence='SRC ui/SettingsScreen.java:270-275,416-487')
e('SettingsScreen.updateViews', 'SettingsScreen.setSpinnerListeners', 'CALL', 'setSpinnerListeners()', evidence='SRC ui/SettingsScreen.java:350-352')
e('S_SETTINGS', 'SettingsScreen.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is inflated (settings_menu)', evidence=FW_MENU + '; SRC ui/SettingsScreen.java:149-153')
e('S_SETTINGS', 'SettingsScreen.onOptionsItemSelected', 'FRAMEWORK', 'tap a Settings toolbar/overflow menu item', gui=['Tap a menu item in Settings'], evidence=FW_MENU + '; SRC ui/SettingsScreen.java:161-192')
e('SettingsScreen.onOptionsItemSelected', 'SettingsScreen$SaveButtonTask.doInBackground', 'ASYNC', 'save', evidence=FW_ASYNC + '; SRC ui/SettingsScreen.java:163-166')
e('SettingsScreen$SaveButtonTask.doInBackground', 'SettingsScreen$SaveButtonTask.onPostExecute', 'ASYNC', 'the save completes on the main thread', evidence=FW_ASYNC + '; SRC ui/SettingsScreen.java:562-575')
e('SettingsScreen$SaveButtonTask.onPostExecute', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_OK); finish() (the caller, Study/Preview-Edit/Misc, restarts)', evidence='SRC ui/SettingsScreen.java:569-574')
e('SettingsScreen.onOptionsItemSelected', 'S_DLG_LOAD_DEFAULT', 'ENTERS', 'load_default', evidence='SRC ui/SettingsScreen.java:167-182')
gui('S_DLG_LOAD_DEFAULT', 'SettingsScreen$1.onClick', 'Tap OK (confirm load default settings)', evidence=FW_DIALOGFRAG + '; SRC ui/SettingsScreen.java:171-179')
e('SettingsScreen$1.onClick', 'SettingsScreen$LoadDefaultTask.doInBackground', 'ASYNC', 'new LoadDefaultTask().execute()', evidence=FW_ASYNC + '; SRC ui/SettingsScreen.java:173-174')
e('SettingsScreen$LoadDefaultTask.doInBackground', 'SettingsScreen$LoadDefaultTask.onPostExecute', 'ASYNC', 'the default Setting is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/SettingsScreen.java:598-604')
e('SettingsScreen$LoadDefaultTask.onPostExecute', 'SettingsScreen$SettingLoaderCallbacks.onCreateLoader', 'CALL', 'multipleLoaderManager.startLoading(true) forces the Setting loader to reload', evidence='SRC ui/SettingsScreen.java:602-603')
e('SettingsScreen.onOptionsItemSelected', 'S_EXT_BROWSER', 'ENTERS', 'settingsmenu_help', env=ENV_EXT_BROWSER, evidence='SRC ui/SettingsScreen.java:183-189')
e('SettingsScreen.onBackPressed', 'S_DLG_SETTINGS_DISCARD', 'ENTERS', 'settingsChanged is true', evidence='SRC ui/SettingsScreen.java:196-215')
gui('S_DLG_SETTINGS_DISCARD', 'SettingsScreen$3.onClick', 'Tap Yes (save before leaving)', evidence=FW_DIALOGFRAG + '; SRC ui/SettingsScreen.java:200-205')
e('SettingsScreen$3.onClick', 'SettingsScreen$SaveButtonTask.doInBackground', 'ASYNC', 'new SaveButtonTask().execute()', evidence=FW_ASYNC + '; SRC ui/SettingsScreen.java:202-203')
gui('S_DLG_SETTINGS_DISCARD', 'SettingsScreen$2.onClick', 'Tap No (discard)', evidence=FW_DIALOGFRAG + '; SRC ui/SettingsScreen.java:206-211')
e('SettingsScreen$2.onClick', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_CANCELED); finish()', evidence='SRC ui/SettingsScreen.java:208-210')
e('SettingsScreen.onBackPressed', 'S_PREVIEW_EDIT', 'ENTERS', 'settingsChanged is false: setResult(RESULT_CANCELED); finish()', evidence='SRC ui/SettingsScreen.java:216-221')
e('SettingsScreen.setSpinnerListeners', 'SettingsScreen$7.onTouch', 'FRAMEWORK', 'touch any settings spinner (only sets settingsChanged = true; no further navigation)', gui=['Open a spinner in Settings'], evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:358-367,369-377')
e('SettingsScreen.setSpinnerListeners', 'SettingsScreen$8.onItemSelected', 'FRAMEWORK', 'pick a color-item in the color spinner', gui=['Pick a color item in the color spinner'], needs_state=state_text('"Customize color" is checked', ('settings',)), evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:379-391')
e('SettingsScreen.updateViews', 'SettingsScreen$10.onClick', 'FRAMEWORK', 'tap a checkbox / color button / typeface field', gui=['Tap a checkbox or the color/typeface row in Settings'], evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:309,314,323,325,328,331,334,338,341,345,640-734')
e('SettingsScreen$10.onClick', 'SettingsScreen.showColorPickerDialog', 'CALL', 'v == colorButton', needs_state=state_text('"Customize color" is checked', ('settings',)), evidence='SRC ui/SettingsScreen.java:654-656,607-638')
e('SettingsScreen.showColorPickerDialog', 'S_DLG_COLOR_PICKER', 'ENTERS', 'the ColorPickerView dialog is shown', needs_state=state_text('"Customize color" is checked', ('settings',)), evidence='SRC ui/SettingsScreen.java:626-637')
gui('S_DLG_COLOR_PICKER', 'SettingsScreen$9.onClick', 'Pick a color and tap OK', evidence=FW_DIALOGFRAG + '; SRC ui/SettingsScreen.java:629-635')
e('SettingsScreen$10.onClick', 'SettingsScreen.showCardFieldMultipleChoiceAlertDialog', 'CALL', 'v == displayInHTMLCheckbox (now checked) / field1Checkbox / field2Checkbox', evidence='SRC ui/SettingsScreen.java:676-711')
e('SettingsScreen.showCardFieldMultipleChoiceAlertDialog', 'S_DLG_FIELD_CHOOSER', 'ENTERS', 'builder.show()', evidence='SRC ui/SettingsScreen.java:245-262')
gui('S_DLG_FIELD_CHOOSER', 'SettingsScreen$4.onClick', 'Toggle a field checkbox', evidence=FW_DIALOGFRAG + '; SRC ui/SettingsScreen.java:247-256')
gui('S_DLG_FIELD_CHOOSER', 'SettingsScreen$5.onClick', 'Tap OK', evidence=FW_DIALOGFRAG + '; SRC ui/SettingsScreen.java:257-261')
e('SettingsScreen$10.onClick', 'S_FILEBROWSER', 'ENTERS', 'v == qTypefaceEdit / aTypefaceEdit: df.show(getSupportFragmentManager(), ...)', evidence='SRC ui/SettingsScreen.java:712-732')

# ---- OptionScreen, AlgorithmCustomizationScreen (preference screens)
e('AnyMemo$1.onNavigationItemSelected', 'OptionScreen.onCreate', 'LIFECYCLE', 'startActivity(OptionScreen) is a plain ENTRY above; its only lifecycle callback is onCreate (a PreferenceActivity)', evidence=FW_ACTIVITY + '; SRC ui/OptionScreen.java:44-58')
e('MiscTabFragment.onClick', 'OptionScreen.onCreate', 'LIFECYCLE', 'v == optionButton: startActivity(OptionScreen)', evidence='SRC ui/MiscTabFragment.java:226-228; ui/OptionScreen.java:44-58')
e('OptionScreen.onCreate', 'S_OPTION_SCREEN', 'ENTERS', 'addPreferencesFromResource(option_screen)', evidence='SRC ui/OptionScreen.java:46')
e('S_OPTION_SCREEN', 'OptionScreen.onConfigurationChanged', 'SYSTEM', 'rotate the device', gui=['Rotate the device'], evidence=FW_ACTIVITY + '; SRC ui/OptionScreen.java:60-63')
e('S_ALGORITHM_SCREEN', 'AlgorithmCustomizationScreen.onConfigurationChanged', 'SYSTEM', 'rotate the device', gui=['Rotate the device'], evidence=FW_ACTIVITY + '; SRC ui/AlgorithmCustomizationScreen.java:57-60')
e('S_OPTION_SCREEN', 'OptionScreen$1.onPreferenceClick', 'FRAMEWORK', 'tap "Customize scheduling algorithm"', gui=['Tap "Customize scheduling algorithm"'], evidence=FW_PREFERENCE + '; SRC ui/OptionScreen.java:50-51,65-82')
e('OptionScreen$1.onPreferenceClick', 'S_DLG_ALGORITHM_WARN', 'ENTERS', 'the warning dialog is shown', evidence='SRC ui/OptionScreen.java:68-78')
gui('S_DLG_ALGORITHM_WARN', 'OptionScreen$1$1.onClick', 'Tap OK (open the algorithm screen)', evidence=FW_DIALOGFRAG + '; SRC ui/OptionScreen.java:71-76')
e('OptionScreen$1$1.onClick', 'AlgorithmCustomizationScreen.onCreate', 'ENTRY', 'startActivity(AlgorithmCustomizationScreen)', evidence='SRC ui/OptionScreen.java:73-74')
e('AlgorithmCustomizationScreen.onCreate', 'S_ALGORITHM_SCREEN', 'ENTERS', 'addPreferencesFromResource(algorithm_customization_screen)', evidence='SRC ui/AlgorithmCustomizationScreen.java:43')
e('S_ALGORITHM_SCREEN', 'AlgorithmCustomizationScreen$1.onPreferenceClick', 'FRAMEWORK', 'tap "Reset customized algorithm"', gui=['Tap "Reset customized algorithm"'], evidence=FW_PREFERENCE + '; SRC ui/AlgorithmCustomizationScreen.java:48-49,62-78')
e('AlgorithmCustomizationScreen$1.onPreferenceClick', 'S_DLG_ALGORITHM_WARN', 'ENTERS', 'the warning dialog is shown (reused page)', evidence='SRC ui/AlgorithmCustomizationScreen.java:65-76')
gui('S_DLG_ALGORITHM_WARN', 'AlgorithmCustomizationScreen$1$1.onClick', 'Tap OK (reset)', evidence=FW_DIALOGFRAG + '; SRC ui/AlgorithmCustomizationScreen.java:68-73')
e('AlgorithmCustomizationScreen$1$1.onClick', 'S_EXIT', 'ENTERS', 'finish(); parameters.reset()', evidence='SRC ui/AlgorithmCustomizationScreen.java:70-72')

# ---- StatisticsScreen
e('OpenActionsFragment$1.onClick', 'StatisticsScreen.onCreate', 'ENTRY', 'v == statisticsItem: startActivity(StatisticsScreen)', evidence='SRC ui/OpenActionsFragment.java:163-168')
e('StatisticsScreen.onCreate', 'StatisticsScreen.onDestroy', 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/StatisticsScreen.java:78-155')
e('StatisticsScreen.onCreate', 'StatisticsScreen.initDrawer', 'CALL', 'initDrawer()', evidence='SRC ui/StatisticsScreen.java:98')
e('StatisticsScreen.onCreate', 'StatisticsScreen$CardToReviewTask.doInBackground', 'ASYNC', 'new CardToReviewTask().execute() (the default chart on open)', evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:104-105')
e('StatisticsScreen$CardToReviewTask.doInBackground', 'StatisticsScreen$ChartTask.onPostExecute', 'ASYNC', 'the chart data is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:172-179')
e('StatisticsScreen$ChartTask.onPostExecute', 'S_STATISTICS', 'ENTERS', 'generateChart(result): the chart view replaces the frame', evidence='SRC ui/StatisticsScreen.java:173-178')
e('S_STATISTICS', 'StatisticsScreen.onOptionsItemSelected', 'FRAMEWORK', 'tap the Up/home icon (drawer burger)', gui=['Tap the menu/burger icon'], evidence=FW_MENU + '; SRC ui/StatisticsScreen.java:108-116')
e('StatisticsScreen.onOptionsItemSelected', 'S_DRAWER', 'ENTERS', 'drawerLayout.openDrawer(START) (reuses the shell drawer page)', evidence='SRC ui/StatisticsScreen.java:110-112')
e('StatisticsScreen.initDrawer', 'StatisticsScreen$1.onNavigationItemSelected', 'FRAMEWORK', 'tap a chart entry in the drawer', gui=['Tap a chart entry in the Statistics drawer'], evidence=FW_MATERIAL + '; SRC ui/StatisticsScreen.java:120-146')
e('StatisticsScreen$1.onNavigationItemSelected', 'StatisticsScreen$CardToReviewTask.doInBackground', 'ASYNC', 'cards_scheduled_in_a_month_menu', evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:124-127')
e('StatisticsScreen$1.onNavigationItemSelected', 'StatisticsScreen$AccumulativeCardsToReviewTask.doInBackground', 'ASYNC', 'accumulative_cards_scheduled_menu', evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:128-131')
e('StatisticsScreen$AccumulativeCardsToReviewTask.doInBackground', 'StatisticsScreen$ChartTask.onPostExecute', 'ASYNC', 'the chart data is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:272-279')
e('StatisticsScreen$1.onNavigationItemSelected', 'StatisticsScreen$NewCardTask.doInBackground', 'ASYNC', 'new_cards_learned_in_the_past_month_menu', evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:132-134')
e('StatisticsScreen$NewCardTask.doInBackground', 'StatisticsScreen$ChartTask.onPostExecute', 'ASYNC', 'the chart data is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:182-209')
e('StatisticsScreen$1.onNavigationItemSelected', 'StatisticsScreen$GradeStatisticsTask.doInBackground', 'ASYNC', 'grade_statistics_menu', evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:135-138')
e('StatisticsScreen$GradeStatisticsTask.doInBackground', 'StatisticsScreen$ChartTask.onPostExecute', 'ASYNC', 'the chart data is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:314-345')


# ================================================================== H. db import/export: DatabaseMerger,
#                                                                       ExportAnyMemoDbFragment, ConverterFragment,
#                                                                       converters, ConvertIntentService
# ---- DatabaseMerger
e('MiscTabFragment.onClick', 'DatabaseMerger.<init>', 'ENTRY', 'v == mergeButton (duplicate text for clarity; see Misc tab section)', evidence='SRC ui/MiscTabFragment.java:346-349')
for cb in ('onCreate', 'onActivityResult'):
    e('DatabaseMerger.<init>', 'DatabaseMerger.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/DatabaseMerger.java:52-97')
e('DatabaseMerger.onCreate', 'S_DB_MERGER', 'ENTERS', 'setContentView(merge_layout)', evidence='SRC ui/DatabaseMerger.java:56')
e('S_DB_MERGER', 'DatabaseMerger.onClick', 'FRAMEWORK', 'tap the target/source field or the Merge/Cancel button', gui=['Tap a field or button in Database Merger'], evidence=FW_VIEW + '; SRC ui/DatabaseMerger.java:66-69,99-137')
e('DatabaseMerger.onClick', 'S_FILEBROWSER', 'ENTERS', 'v == targetEdit or v == sourceEdit: startActivityForResult(FileBrowserActivity, .db)', env=ENV_PICKER, evidence='SRC ui/DatabaseMerger.java:101-113')
e('DatabaseMerger.onActivityResult', 'S_DB_MERGER', 'ENTERS', 'the picked path is written into the target/source field', env=ENV_PICKER, evidence='SRC ui/DatabaseMerger.java:83-96')
e('DatabaseMerger.onClick', 'DatabaseMerger$1.doHeavyTask', 'CALL', 'v == mergeButton: AMGUIUtility.doProgressTask', evidence=FW_ASYNC + '; SRC ui/DatabaseMerger.java:115-131')
e('DatabaseMerger$1.doHeavyTask', 'DatabaseMerger$1.doUITask', 'FRAMEWORK', 'doProgressTask runs doHeavyTask() on a background Thread, then posts doUITask() to the main thread', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:80-112')
e('DatabaseMerger$1.doUITask', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_OK); finish() (the Preview/Edit caller restarts)', evidence='SRC ui/DatabaseMerger.java:123-129')
e('DatabaseMerger.onClick', 'S_EXIT', 'ENTERS', 'v == cancelButton: finish()', evidence='SRC ui/DatabaseMerger.java:133-135')

# ---- ExportAnyMemoDbFragment (FileBrowserFragment@EXPORT variant; picks a .db, then the system Save dialog)
e('MiscTabFragment.onClick', 'ExportAnyMemoDbFragment.onCreate', 'LIFECYCLE', 'v == exportAnyMemoButton: df.show(...) triggers the DialogFragment lifecycle', evidence=FW_DIALOGFRAG + '; SRC ui/MiscTabFragment.java:253-256; ui/ExportAnyMemoDbFragment.java:32-43')
for cb in ('onDestroy',):
    e('ExportAnyMemoDbFragment.onCreate', 'ExportAnyMemoDbFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/ExportAnyMemoDbFragment.java:54-60')
e('FileBrowserFragment.openFile@EXPORT', 'ExportAnyMemoDbFragment$1.onFileBrowserFileClick', 'CALL', 'onFileClickListener.onFileBrowserFileClick(clickedFile)', evidence='SRC ui/FileBrowserFragment.java:412-414 (bytecode); ui/ExportAnyMemoDbFragment.java:37-42')
e('ExportAnyMemoDbFragment$1.onFileBrowserFileClick', 'ExportAnyMemoDbFragment.exportDatabase', 'CALL', 'exportDatabase(file)', evidence='SRC ui/ExportAnyMemoDbFragment.java:39-41')
e('ExportAnyMemoDbFragment.exportDatabase', 'S_EXT_PICKER', 'ENTERS', 'ACTION_CREATE_DOCUMENT is started', env=ENV_PICKER, evidence='SRC ui/ExportAnyMemoDbFragment.java:45-52')
e('ExportAnyMemoDbFragment.onActivityResult', 'ExportAnyMemoDbFragment$4.call', 'FRAMEWORK', 'RESULT_OK: Observable.fromCallable runs call() on the io scheduler', env=ENV_PICKER, evidence=FW_RX + '; SRC ui/ExportAnyMemoDbFragment.java:64-75')
e('ExportAnyMemoDbFragment$4.call', 'ExportAnyMemoDbFragment$2.accept', 'FRAMEWORK', 'the Observable emits onNext(true/false) on the main thread', evidence=FW_RX + '; SRC ui/ExportAnyMemoDbFragment.java:77-87')
e('ExportAnyMemoDbFragment$4.call', 'ExportAnyMemoDbFragment$3.accept', 'FRAMEWORK', 'the Observable emits onError(throwable)', evidence=FW_RX + '; SRC ui/ExportAnyMemoDbFragment.java:88-94')
e('ExportAnyMemoDbFragment$2.accept', 'S_MAIN_MISC', 'ENTERS', 'dismiss() returns to the Misc tab underneath', evidence='SRC ui/ExportAnyMemoDbFragment.java:79-86')

# ---- ConverterFragment (FileBrowserFragment@CONVERTER variant)
e('MiscTabFragment.onClick', 'ConverterFragment.onCreate', 'LIFECYCLE', 'df.show(...) triggers the DialogFragment lifecycle (duplicate text for clarity; see Misc tab section)', evidence=FW_DIALOGFRAG + '; SRC ui/ConverterFragment.java:59-70')
e('FileBrowserFragment.openFile@CONVERTER', 'ConverterFragment$1.onFileBrowserFileClick', 'CALL', 'onFileClickListener.onFileBrowserFileClick(clickedFile)', evidence='SRC ui/FileBrowserFragment.java:412-414 (bytecode); ui/ConverterFragment.java:72-77')
e('ConverterFragment$1.onFileBrowserFileClick', 'ConverterFragment.startConversion', 'CALL', 'startConversion(file)', evidence='SRC ui/ConverterFragment.java:74-76')
e('ConverterFragment.startConversion', 'S_DLG_CONVERT_MERGE', 'ENTERS', 'destExtension is db and the output file already exists (chained import converters only; export converters never target .db)', guard='converter.getDestExtension().equals("db")', evidence='SRC ui/ConverterFragment.java:93-123')
gui('S_DLG_CONVERT_MERGE', 'ConverterFragment$3.onClick', 'Tap Yes (overwrite)', evidence=FW_DIALOGFRAG + '; SRC ui/ConverterFragment.java:99-105')
gui('S_DLG_CONVERT_MERGE', 'ConverterFragment$2.onClick', 'Tap No (back up and replace)', evidence=FW_DIALOGFRAG + '; SRC ui/ConverterFragment.java:106-120')
e('ConverterFragment$3.onClick', 'ConverterFragment.invokeConverterService', 'CALL', 'invokeConverterService(inputPath, outputPath, null)', evidence='SRC ui/ConverterFragment.java:102-103')
e('ConverterFragment$2.onClick', 'ConverterFragment.invokeConverterService', 'CALL', 'deleteFileWithBackup then invokeConverterService(inputPath, outputPath, null)', evidence='SRC ui/ConverterFragment.java:110-112')
e('ConverterFragment.startConversion', 'S_EXT_PICKER', 'ENTERS', 'the destination is not .db (a text/xml export format): ACTION_CREATE_DOCUMENT is started', env=ENV_PICKER, evidence='SRC ui/ConverterFragment.java:127-135')
e('ConverterFragment.onActivityResult', 'ConverterFragment.invokeConverterService', 'CALL', 'REQUEST_CODE_EXPORT, RESULT_OK: invokeConverterService(pendingInputPath, pendingOutputPath, uri)', env=ENV_PICKER, evidence='SRC ui/ConverterFragment.java:140-142')
e('ConverterFragment.invokeConverterService', 'S_MAIN_MISC', 'ENTERS', 'ConvertIntentService is started in the background, a Toast is shown and dismiss() returns to the Misc tab', evidence='SRC ui/ConverterFragment.java:151-167')
e('ConverterFragment.startConversion', 'S_MAIN_MISC', 'ENTERS', 'destExtension is db and the output file does not yet exist: invokeConverterService runs immediately', evidence='SRC ui/ConverterFragment.java:123-126')

# ---- ConvertIntentService (IntentService; started by MiscTabFragment.invokeImportConversion and ConverterFragment.invokeConverterService)
e('MiscTabFragment.invokeImportConversion', 'ConvertIntentService.onCreate', 'ENTRY', 'startService(ConvertIntentService)', evidence='SRC ui/MiscTabFragment.java:469-477')
e('ConverterFragment.invokeConverterService', 'ConvertIntentService.onCreate', 'ENTRY', 'getActivity().startService(intent)', evidence='SRC ui/ConverterFragment.java:162')
e('ConvertIntentService.onCreate', 'ConvertIntentService.onHandleIntent', 'LIFECYCLE', 'IntentService queues and runs onHandleIntent on its single worker thread', evidence=FW_SERVICE + '; SRC common/BaseIntentService.java:7-14; service/ConvertIntentService.java:75-144')
e('ConvertIntentService.onHandleIntent', 'ConvertIntentService.showSuccessNotification', 'CALL', 'the conversion succeeds', evidence='SRC service/ConvertIntentService.java:124-134')
e('ConvertIntentService.onHandleIntent', 'ConvertIntentService.showFailureNotification', 'CALL', 'the conversion throws', evidence='SRC service/ConvertIntentService.java:136-138')
e('ConvertIntentService.showSuccessNotification', 'PreviewEditActivity.<init>', 'INTENT', 'the output is a .db: tapping the success notification opens PreviewEditActivity', env=ENV_NOTIF, evidence='SRC service/ConvertIntentService.java:185-191,197-212')
e('ConvertIntentService.showSuccessNotification', 'AnyMemo.<init>', 'INTENT', 'the output is not a .db: tapping the success notification opens AnyMemo', env=ENV_NOTIF, evidence='SRC service/ConvertIntentService.java:192-212')


# ================================================================== I. downloader: AnyMemoDownloader*,
#                                                                       AbstractDownloaderFragment, Dropbox*,
#                                                                       Oauth2AccountActivity, dead oauth1 code
# ---- shared AbstractDownloaderFragment (AnyMemoDownloaderFragment@AM / DropboxListFragment@DROPBOX variants
# are unnecessary: each subclass fully overrides all 6 abstract hooks itself, and the non-abstract framework
# methods below are identical bytecode regardless of which subclass is mounted, exactly like FileBrowserFragment's
# onCreateView/onResume -- the only per-subclass part is the abstract-method dispatch, already resolved correctly
# by AUTO's CHA (each subclass only implements its own abstract methods, no shared ambiguous target).
for page in ('S_DOWNLOAD_AM', 'S_DROPBOX_LIST'):
    for cb in ('onAttach', 'onCreate', 'onCreateView', 'onViewCreated'):
        e(page, 'AbstractDownloaderFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC downloader/common/AbstractDownloaderFragment.java:127-174')
e('AbstractDownloaderFragment.onViewCreated', 'AbstractDownloaderFragment.refreshList', 'CALL', 'refreshList()', evidence='SRC downloader/common/AbstractDownloaderFragment.java:173')
e('AbstractDownloaderFragment.refreshList', 'AbstractDownloaderFragment$1.call', 'ASYNC', 'new RetrieveTask().execute(Callable: initialRetrieve)', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:181-187')
e('AbstractDownloaderFragment$1.call', 'AbstractDownloaderFragment$RetrieveTask.onPostExecute', 'ASYNC', 'the retrieved list (or the exception) is delivered on the main thread', env=ENV_NET, evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:220-234')
e('AbstractDownloaderFragment$RetrieveTask.onPostExecute', 'S_DOWNLOAD_AM', 'ENTERS', 'the category/database list is shown (AnyMemo source)', env=ENV_NET, evidence='SRC downloader/common/AbstractDownloaderFragment.java:229-234')
e('AbstractDownloaderFragment$RetrieveTask.onPostExecute', 'S_DROPBOX_LIST', 'ENTERS', 'the Dropbox folder listing is shown (Dropbox source)', env=ENV_DROPBOX, evidence='SRC downloader/common/AbstractDownloaderFragment.java:229-234')
e('AbstractDownloaderFragment$RetrieveTask.onPostExecute', 'S_DLG_DOWNLOAD_FAIL', 'ENTERS', 'initialRetrieve() threw (no network / Dropbox error)', env=ENV_NET, evidence='SRC downloader/common/AbstractDownloaderFragment.java:224-227')
e('AbstractDownloaderFragment.onCreateView', 'AbstractDownloaderFragment$DownloadListAdapter$1.onClick', 'FRAMEWORK', 'tap a row (category, back, or a database)', gui=['Tap a row in the download list'], evidence=FW_VIEW + '; SRC downloader/common/AbstractDownloaderFragment.java:409-437')
e('AbstractDownloaderFragment$DownloadListAdapter$1.onClick', 'AbstractDownloaderFragment$DownloadListAdapter$1$1.call', 'ASYNC', 'the row is a category: new RetrieveTask().execute(Callable: openCategory)', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:417-424')
e('AbstractDownloaderFragment$DownloadListAdapter$1$1.call', 'AbstractDownloaderFragment$RetrieveTask.onPostExecute', 'ASYNC', 'the category\'s databases are delivered on the main thread', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:417-424')
e('AbstractDownloaderFragment$DownloadListAdapter$1.onClick', 'AbstractDownloaderFragment$DownloadListAdapter$1$2.call', 'ASYNC', 'the row is "..": new RetrieveTask().execute(Callable: goBack)', needs_state=state_text('a category was opened before in this session', ('session',)), evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:425-432')
e('AbstractDownloaderFragment$DownloadListAdapter$1$2.call', 'AbstractDownloaderFragment$RetrieveTask.onPostExecute', 'ASYNC', 'the top-level category list is delivered on the main thread', needs_state=state_text('a category was opened before in this session', ('session',)), evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:425-432')
e('AbstractDownloaderFragment$DownloadListAdapter$1.onClick', 'AbstractDownloaderFragment.showFetchDatabaseDialog', 'CALL', 'the row is a database (or a Dropbox file)', evidence='SRC downloader/common/AbstractDownloaderFragment.java:433-435')
e('AbstractDownloaderFragment.showFetchDatabaseDialog', 'S_DLG_DOWNLOAD_CONFIRM', 'ENTERS', 'the confirm-download dialog is shown', evidence='SRC downloader/common/AbstractDownloaderFragment.java:276-291')
gui('S_DLG_DOWNLOAD_CONFIRM', 'AbstractDownloaderFragment$2.onClick', 'Tap Yes (download this database)', evidence=FW_DIALOGFRAG + '; SRC downloader/common/AbstractDownloaderFragment.java:284-289')
e('AbstractDownloaderFragment$2.onClick', 'AbstractDownloaderFragment.startFetchDatabaseTask', 'CALL', 'startFetchDatabaseTask(item)', evidence='SRC downloader/common/AbstractDownloaderFragment.java:286-287')
e('AbstractDownloaderFragment.startFetchDatabaseTask', 'AbstractDownloaderFragment$FetchDatabaseTask.doInBackground', 'ASYNC', 'new FetchDatabaseTask().execute(item)', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:294-297')
e('AbstractDownloaderFragment$FetchDatabaseTask.doInBackground', 'AbstractDownloaderFragment$FetchDatabaseTask.onPostExecute', 'ASYNC', 'the fetched path (or the exception) is delivered on the main thread', env=ENV_NET, evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:316-343')
e('AbstractDownloaderFragment$FetchDatabaseTask.onPostExecute', 'S_DLG_DOWNLOAD_OK', 'ENTERS', 'the download succeeds (fetchDatabase: AnyMemo source needs the network, Dropbox source needs Dropbox+network)', env=ENV_NET, evidence='SRC downloader/common/AbstractDownloaderFragment.java:334-341')
e('AbstractDownloaderFragment$FetchDatabaseTask.onPostExecute', 'S_DLG_DOWNLOAD_FAIL', 'ENTERS', 'fetchDatabase() threw', env=ENV_NET, evidence='SRC downloader/common/AbstractDownloaderFragment.java:330-333')
e('AbstractDownloaderFragment.onCreateView', 'AbstractDownloaderFragment$3.onClick', 'FRAMEWORK', 'tap "Load more" (only shown when hasMore() is true; AnyMemo source never sets more, so this is closed_by_configuration for the AnyMemo source and open for a hypothetical Dropbox paging that the source never uses either)',
  gui=['Tap "Load more" at the bottom of the download list'], evidence=FW_VIEW + '; SRC downloader/common/AbstractDownloaderFragment.java:153,346-354')
e('AbstractDownloaderFragment$3.onClick', 'AbstractDownloaderFragment$LoadMoreTask.doInBackground', 'ASYNC', 'new LoadMoreTask().execute()', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:349-350')
e('AbstractDownloaderFragment$LoadMoreTask.doInBackground', 'AbstractDownloaderFragment$LoadMoreTask.onPostExecute', 'ASYNC', 'loadMore() always returns null for both sources: the result is delivered on the main thread', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:258-274')

# ---- AnyMemoDownloaderActivity / Fragment (no login needed; needs the AnyMemo server)
e('AnyMemoDownloaderActivity.<init>', 'AnyMemoDownloaderActivity.onCreate', 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC downloader/anymemo/AnyMemoDownloaderActivity.java:9-13')
e('AnyMemoDownloaderActivity.onCreate', 'AnyMemoDownloaderFragment.onCreate', 'LIFECYCLE', 'the layout statically includes the fragment (<fragment> tag)', evidence=FW_FRAG + '; SRC downloader/anymemo/AnyMemoDownloaderActivity.java:10-13; res/layout/anymemo_downloader.xml')
e('AnyMemoDownloaderFragment.onCreate', 'S_DOWNLOAD_AM', 'ENTERS', 'the fragment (and its AbstractDownloaderFragment base) is created', evidence='SRC downloader/anymemo/AnyMemoDownloaderFragment.java:35-39')

# ---- DropboxOauth2AccountActivity / Oauth2AccountActivity (OAuth2 + Custom Tabs) / DropboxListActivity+Fragment / UploadDropboxActivity
for cb in ('onCreate', 'onDestroy', 'onNewIntent'):
    e('DropboxOauth2AccountActivity.onCreate', 'Oauth2AccountActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback (DropboxOauth2AccountActivity does not override these)', evidence=FW_ACTIVITY + '; SRC downloader/oauth/Oauth2AccountActivity.java:37-63')
e('Oauth2AccountActivity.onCreate', 'Oauth2AccountActivity.requestAuth', 'CALL', 'no token saved yet (first use / fixtures have none)', evidence='SRC downloader/oauth/Oauth2AccountActivity.java:44-49')
e('Oauth2AccountActivity.requestAuth', 'S_DROPBOX_LOGIN', 'ENTERS', 'CustomTabsIntent.launchUrl shows the Dropbox login page', env=ENV_DROPBOX, evidence=FW_CUSTOMTABS + '; SRC downloader/oauth/Oauth2AccountActivity.java:127-131')
e('Oauth2AccountActivity.onCreate', 'Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'CALL', 'a token was saved before', needs_state=NEED_SAVED_TOKEN, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:44-46')
e('Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onSuccess', 'FRAMEWORK', 'verifyAccessToken(token) (a Completable) completes on the main thread', needs_state=NEED_SAVED_TOKEN, env=ENV_NET, evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:105-123')
e('Oauth2AccountActivity$1.onSuccess', 'DropboxOauth2AccountActivity.onAuthenticated', 'CALL', 'onAuthenticated(token)', needs_state=NEED_SAVED_TOKEN, env=ENV_NET, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:93; downloader/dropbox/DropboxOauth2AccountActivity.java:25-30')
e('Oauth2AccountActivity$1.onError', 'Oauth2AccountActivity.requestAuth', 'CALL', 'the saved token is no longer valid', needs_state=NEED_SAVED_TOKEN, env=ENV_NET, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:97-101')
e('Oauth2AccountActivity.onNewIntent', 'Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'CALL', 'the browser redirects back with the access-token fragment', env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:59-62')
e('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$2.onComplete', 'FRAMEWORK', 'fetchAuthTokenFromCallback(uri) (a Single) succeeds on the main thread', env=ENV_OAUTH_CALLBACK, evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:85-103')
e('Oauth2AccountActivity$2.onComplete', 'DropboxOauth2AccountActivity.onAuthenticated', 'CALL', 'onAuthenticated(token)', env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:93')
e('DropboxOauth2AccountActivity.onAuthenticated', 'DropboxListActivity.<init>', 'ENTRY', 'startActivity(DropboxListActivity); finish()', env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/dropbox/DropboxOauth2AccountActivity.java:25-30')
for cb in ('onActivityResult', 'onCreateOptionsMenu', 'onOptionsItemSelected'):
    e('DropboxListActivity.onCreate', 'DropboxListActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/DropboxListActivity.java:36-91')
e('DropboxListActivity.onCreate', 'DropboxListFragment.onCreate', 'CALL', 'the fragment transaction commits a new DropboxListFragment', evidence='SRC downloader/dropbox/DropboxListActivity.java:49-56')
e('DropboxListActivity.onCreate', 'S_DROPBOX_LIST', 'ENTERS', 'the fragment transaction commits', evidence='SRC downloader/dropbox/DropboxListActivity.java:49-56')
e('S_DROPBOX_LIST', 'DropboxListActivity$1.onClick', 'FRAMEWORK', 'tap the upload FAB', gui=['Tap the upload FAB'], evidence=FW_VIEW + '; SRC downloader/dropbox/DropboxListActivity.java:58-63')
e('DropboxListActivity$1.onClick', 'DropboxListActivity.openUploadDropbox', 'CALL', 'openUploadDropbox()', evidence='SRC downloader/dropbox/DropboxListActivity.java:61')
e('DropboxListActivity.openUploadDropbox', 'UploadDropboxActivity.<init>', 'ENTRY', 'startActivityForResult(UploadDropboxActivity)', evidence='SRC downloader/dropbox/DropboxListActivity.java:95-99')
e('DropboxListActivity.onOptionsItemSelected', 'S_EXIT', 'ENTERS', 'logout: invalidateSavedToken(); finish()', evidence='SRC downloader/dropbox/DropboxListActivity.java:78-85')
e('DropboxListActivity.onActivityResult', 'DropboxListActivity.refreshList', 'CALL', 'the upload activity returns RESULT_OK', evidence='SRC downloader/dropbox/DropboxListActivity.java:70-74')
e('DropboxListActivity.refreshList', 'AbstractDownloaderFragment.refreshList', 'CALL', 'fragment.refreshList()', evidence='SRC downloader/dropbox/DropboxListActivity.java:88-90')
e('DropboxListFragment.initialRetrieve', 'DropboxListFragment$1.accept', 'FRAMEWORK', 'dropboxApiHelper.listFiles(...).blockingForEach(...) calls accept() synchronously on the calling (background) thread for each page', env=ENV_DROPBOX, evidence=FW_RX + '; SRC downloader/dropbox/DropboxListFragment.java:58-67')
for cb in ('onCreate',):
    e('S_DROPBOX_UPLOAD', 'UploadDropboxActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/UploadDropboxActivity.java:42-59')
for cb in ('onStart', 'onStop', 'onDestroy'):
    e('UploadDropboxActivity.onCreate', 'UploadDropboxActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/UploadDropboxActivity.java:61-75')
e('FileBrowserFragment.notifyFileClick', 'UploadDropboxActivity.onFileBrowserFileClick', 'CALL', 'getActivity() instanceof OnFileClickListener (duplicate text for clarity; see the FileBrowserFragment section)', evidence='SRC ui/FileBrowserFragment.java:434-440 (bytecode)')
e('UploadDropboxActivity.onFileBrowserFileClick', 'UploadDropboxActivity.showUploadDialog', 'CALL', 'showUploadDialog(file)', evidence='SRC downloader/dropbox/UploadDropboxActivity.java:123-124')
e('UploadDropboxActivity.showUploadDialog', 'S_DLG_DROPBOX_UPLOAD_CONFIRM', 'ENTERS', 'the confirm-upload dialog is shown', evidence='SRC downloader/dropbox/UploadDropboxActivity.java:77-87')
gui('S_DLG_DROPBOX_UPLOAD_CONFIRM', 'UploadDropboxActivity$1.onClick', 'Tap OK (upload)', evidence=FW_DIALOGFRAG + '; SRC downloader/dropbox/UploadDropboxActivity.java:81-86')
e('UploadDropboxActivity$1.onClick', 'UploadDropboxActivity.uploadToDropbox', 'CALL', 'uploadToDropbox(file)', evidence='SRC downloader/dropbox/UploadDropboxActivity.java:84')
e('UploadDropboxActivity.uploadToDropbox', 'UploadDropboxActivity$2.run', 'FRAMEWORK', 'dropboxApiHelper.uploadDropbox(...) (a Completable) runs on the main thread', env=ENV_DROPBOX, evidence=FW_RX + '; SRC downloader/dropbox/UploadDropboxActivity.java:99-112')
e('UploadDropboxActivity.uploadToDropbox', 'UploadDropboxActivity$3.accept', 'FRAMEWORK', 'the Completable errors', env=ENV_DROPBOX, evidence=FW_RX + '; SRC downloader/dropbox/UploadDropboxActivity.java:113-119')
e('UploadDropboxActivity$2.run', 'S_DROPBOX_UPLOAD', 'ENTERS', 'the success dialog is shown over the same page (setResult(RESULT_OK) happens only in showUploadDialog\'s positive button, already recorded)', evidence='SRC downloader/dropbox/UploadDropboxActivity.java:105-111')

# ---- dead oauth1 code: OauthAccountActivity / OauthAccessCodeRetrievalFragment have no concrete subclass anywhere
# in this app module (grepped: 0 matches for "extends OauthAccountActivity" / "extends OauthAccessCodeRetrievalFragment").
# Nothing can ever construct one, so every one of their methods (and every DialogFragment/AsyncTask nested inside
# them) is classified UNREACHABLE no_trigger_in_app in section L; no edges are written for them here.


# ================================================================== J. widget / receivers / services:
#                                                                       AnyMemoWidgetProvider, UpdateWidgetService,
#                                                                       WidgetRemoteViewsFactory, AlarmReceiver,
#                                                                       SetAlarmReceiver, CardPlayerService +
#                                                                       state machine, CardPlayerActivity/Fragment
# ---- AnyMemoWidgetProvider / UpdateWidgetService / WidgetRemoteViewsFactory (exported, APPWIDGET_UPDATE)
e('S_ENTRY', 'AnyMemoWidgetProvider.<init>', 'ENTRY', 'the user adds the AnyMemo widget to the home screen, or its periodic APPWIDGET_UPDATE fires',
  env=ENV_WIDGET, gui=['Long-press the home screen, add the AnyMemo widget'], evidence='SRC AndroidManifest.xml:153-163; ' + FW_WIDGET)
e('AnyMemoWidgetProvider.<init>', 'AnyMemoWidgetProvider.onEnabled', 'LIFECYCLE', 'the first widget instance is placed', env=ENV_WIDGET, evidence=FW_WIDGET + '; SRC widget/AnyMemoWidgetProvider.java:50-53')
e('AnyMemoWidgetProvider.<init>', 'AnyMemoWidgetProvider.onDisabled', 'LIFECYCLE', 'the last widget instance is removed', env=ENV_WIDGET, evidence=FW_WIDGET + '; SRC widget/AnyMemoWidgetProvider.java:55-58')
e('AnyMemoWidgetProvider.<init>', 'AnyMemoWidgetProvider.onUpdate', 'LIFECYCLE', 'a widget instance needs an update (placed, or the periodic updatePeriodMillis fires)', env=ENV_WIDGET, evidence=FW_WIDGET + '; SRC widget/AnyMemoWidgetProvider.java:60-79')
e('AnyMemoWidgetProvider.onUpdate', 'UpdateWidgetService.onGetViewFactory', 'ENTRY', 'rv.setRemoteAdapter(...) binds the RemoteViewsService', env=ENV_WIDGET, evidence=FW_WIDGET + '; SRC widget/AnyMemoWidgetProvider.java:66,74; widget/UpdateWidgetService.java:9-13')
e('UpdateWidgetService.onGetViewFactory', 'WidgetRemoteViewsFactory.onCreate', 'LIFECYCLE', 'the factory is constructed and onCreate() called', evidence=FW_WIDGET + '; SRC widget/UpdateWidgetService.java:11-13; widget/WidgetRemoteViewsFactory.java:33-41')
e('WidgetRemoteViewsFactory.onCreate', 'WidgetRemoteViewsFactory.onDataSetChanged', 'LIFECYCLE', 'the widget host loads the data before the first getViewAt', env=ENV_WIDGET, evidence=FW_WIDGET + '; SRC widget/WidgetRemoteViewsFactory.java:40,46-48')
e('WidgetRemoteViewsFactory.onDataSetChanged', 'WidgetRemoteViewsFactory.getViewAt', 'CALL', 'the widget host asks for each visible row', env=ENV_WIDGET, evidence=FW_WIDGET + '; SRC widget/WidgetRemoteViewsFactory.java:74-94')
e('WidgetRemoteViewsFactory.getViewAt', 'S_HOME_WIDGET', 'ENTERS', 'the row is rendered with its fill-in intent', needs_state=NEED_RECENT, env=ENV_WIDGET, evidence='SRC widget/WidgetRemoteViewsFactory.java:74-94')
e('WidgetRemoteViewsFactory.onDestroy', 'S_EXIT', 'ENTERS', 'the widget host releases the factory (not a real page transition; kept so onDestroy has a route)', env=ENV_WIDGET, evidence=FW_WIDGET + '; SRC widget/WidgetRemoteViewsFactory.java:43-44')
sup(('UpdateWidgetService.onGetViewFactory', 'WidgetRemoteViewsFactory.onDestroy'))
e('UpdateWidgetService.onGetViewFactory', 'WidgetRemoteViewsFactory.onDestroy', 'LIFECYCLE', 'the widget host releases the factory', env=ENV_WIDGET, evidence=FW_WIDGET + '; SRC widget/WidgetRemoteViewsFactory.java:43-44')

# ---- AlarmReceiver / SetAlarmReceiver
e('AnyMemo.prepareNotification', 'SetAlarmReceiver.cancelNotificationAlarm', 'CALL', 'cancelNotificationAlarm(this)', evidence='SRC ui/AnyMemo.java:386')
e('AnyMemo.prepareNotification', 'SetAlarmReceiver.setNotificationAlarm', 'CALL', 'setNotificationAlarm(this)', evidence='SRC ui/AnyMemo.java:387')
e('S_ENTRY', 'SetAlarmReceiver.<init>', 'ENTRY', 'the device finishes booting (ACTION_BOOT_COMPLETED)', env=ENV_BOOT, evidence='SRC AndroidManifest.xml:145-152; ' + FW_BOOT)
e('SetAlarmReceiver.<init>', 'SetAlarmReceiver.onReceive', 'FRAMEWORK', 'the system delivers the matched broadcast', env=ENV_BOOT, evidence=FW_RECEIVER + '; SRC receiver/SetAlarmReceiver.java:40-43')
e('SetAlarmReceiver.onReceive', 'SetAlarmReceiver.setNotificationAlarm', 'CALL', 'setNotificationAlarm(context)', env=ENV_BOOT, evidence='SRC receiver/SetAlarmReceiver.java:42')
# SetAlarmReceiver.setNotificationAlarm/cancelNotificationAlarm only schedule/cancel an AlarmManager PendingIntent
# (no page of their own); AlarmReceiver.<init> below is reached independently, through the scheduled alarm firing.
e('S_ENTRY', 'AlarmReceiver.<init>', 'ENTRY', 'AlarmManager delivers the scheduled daily-notification-check PendingIntent (a separate :remote process)', env=ENV_ALARM, evidence='SRC AndroidManifest.xml:142-144; ' + FW_ALARM + '; receiver/SetAlarmReceiver.java:68-88')
e('AlarmReceiver.<init>', 'AlarmReceiver.onReceive', 'FRAMEWORK', 'the system delivers the matched broadcast', env=ENV_ALARM, evidence=FW_RECEIVER + '; SRC receiver/AlarmReceiver.java:43-49')
e('AlarmReceiver.onReceive', 'NotificationUtil.showNotification', 'CALL', 'request_code has ALARM_SHOW_NOTIFICATION set (the only request_code AnyMemo ever schedules)', env=ENV_ALARM, evidence='SRC receiver/AlarmReceiver.java:55-59')
e('NotificationUtil.showNotification', 'S_NOTIF_REVIEW', 'ENTERS', 'the review-reminder notification is posted (needs >= 10 scheduled cards)', env=ENV_ALARM, needs_state=state_text('at least one recent deck has 10 or more cards scheduled for review', ('data',)), evidence='SRC utils/NotificationUtil.java:41-69')
e('S_NOTIF_REVIEW', 'AnyMemo.<init>', 'INTENT', 'tap the review-reminder notification', env=ENV_NOTIF, gui=['Tap the review-reminder notification'], evidence='SRC utils/NotificationUtil.java:47-51')

# ---- CardPlayerService (bound by CardPlayerActivity) + its state machine
e('CardPlayerActivity.onPostInit', 'CardPlayerService.onCreate', 'ENTRY', 'bindCardPlayerService(): bindService(Context.BIND_AUTO_CREATE)', evidence='SRC ui/CardPlayerActivity.java:111,210-215')
e('CardPlayerService.onCreate', 'CardPlayerService.onBind', 'LIFECYCLE', 'the system binds the freshly created service', evidence=FW_SERVICE + '; SRC service/CardPlayerService.java:79-83,87-109')
e('CardPlayerService.onBind', 'CardPlayerActivity$3.onServiceConnected', 'FRAMEWORK', 'the binder is delivered to the ServiceConnection', evidence=FW_SERVICECONN + '; SRC service/CardPlayerService.java:88,108; ui/CardPlayerActivity.java:221-227')
for cb in ('onCreate', 'onDestroy'):
    e('CardPlayerActivity.<init>', 'CardPlayerActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/CardPlayerActivity.java:61-92')
e('OpenActionsFragment$1.onClick', 'CardPlayerActivity.<init>', 'ENTRY', 'v == cardPlayerItem: startActivity(CardPlayerActivity) (duplicate text for clarity; see Open-actions section)', evidence='SRC ui/OpenActionsFragment.java:192-197')
e('PreviewEditActivity.onOptionsItemSelected', 'CardPlayerActivity.<init>', 'ENTRY', 'menu_card_player: startActivityForResult(CardPlayerActivity) (duplicate text for clarity)', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:307-316')
e('CardPlayerActivity.onPostInit', 'CardPlayerActivity.showNoItemDialog', 'CALL', 'the deck has no card', guard='getCurrentCard() == null', evidence='SRC ui/CardPlayerActivity.java:112-115')
e('CardPlayerActivity.showNoItemDialog', 'S_DLG_NO_ITEM', 'ENTERS', 'the no-item dialog is shown (reused page)', evidence='SRC ui/CardPlayerActivity.java:150-169')
e('CardPlayerActivity.onPostInit', 'CardPlayerActivity.setupControlButtons', 'CALL', 'the deck has at least one card', needs_state=NEED_CARD, evidence='SRC ui/CardPlayerActivity.java:116')
e('CardPlayerActivity.setupControlButtons', 'CardPlayerFragment.<init>', 'CALL', 'a new CardPlayerFragment replaces buttons_root', evidence='SRC ui/CardPlayerActivity.java:122-128')
e('CardPlayerActivity.onPostInit', 'S_CARD_PLAYER', 'ENTERS', 'updateCardFrontSide() displays the first card', needs_state=NEED_CARD, evidence='SRC ui/CardPlayerActivity.java:117')
e('S_CARD_PLAYER', 'CardPlayerFragment.onCreate', 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/CardPlayerFragment.java:68-72')
for cb in ('onResume', 'onPause', 'onCreateView', 'onDestroyView', 'onCreateOptionsMenu', 'onOptionsItemSelected'):
    e('CardPlayerFragment.onCreate', 'CardPlayerFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle / framework callback', evidence=FW_FRAG + '; SRC ui/CardPlayerFragment.java:78-146')
e('CardPlayerFragment.onCreateView', 'CardPlayerFragment$1.onClick', 'FRAMEWORK', 'tap Play/Pause, Previous, Next, Repeat or Shuffle', gui=['Tap a Card Player control'], evidence=FW_VIEW + '; SRC ui/CardPlayerFragment.java:99,105,109,113,118,148-193')
e('CardPlayerFragment$1.onClick', 'CardPlayerService.startPlaying', 'CALL', 'v == playButton, not already playing', evidence='SRC ui/CardPlayerFragment.java:157,163,195-199')
e('CardPlayerService.startPlaying', 'CardPlayerState$1.transition', 'CALL', 'cardPlayerContext.getState().transition(context, START_PLAYING): state is STOPPED after reset() (bytecode: virtual call through the CardPlayerStateTransition interface, CHA-resolved to the STOPPED enum body)', evidence='SRC service/CardPlayerService.java:138-147 (bytecode); service/cardplayer/CardPlayerState.java:36-67')
e('CardPlayerFragment$1.onClick', 'CardPlayerService.stopPlaying', 'CALL', 'v == playButton, already playing', evidence='SRC ui/CardPlayerFragment.java:157-160,201-207')
e('CardPlayerFragment$1.onClick', 'CardPlayerService.skipToNext', 'CALL', 'v == nextButton', evidence='SRC ui/CardPlayerFragment.java:167-168')
e('CardPlayerFragment$1.onClick', 'CardPlayerService.skipToPrev', 'CALL', 'v == previousButton', evidence='SRC ui/CardPlayerFragment.java:165-166')
e('CardPlayerFragment$1.onClick', 'CardPlayerService.reset', 'CALL', 'v == repeatButton or v == shuffleButton', evidence='SRC ui/CardPlayerFragment.java:169-191')
# CardPlayerState$1/$2/$3.transition (STOPPED/PLAYING_QUESTION/PLAYING_ANSWER) call each other, CardPlayerState.playQuestion/
# playAnswer/findNextCard/findPrevCard/stopPlaying, and context.getEventHandler().onPlayCard/onStopPlaying (CHA-resolved to
# CardPlayerService$cardPlayerEventHandler) through explicit calls/virtual dispatch the bytecode extractor already covers (AUTO).
e('CardPlayerService$1.onPlayCard', 'CardPlayerFragment$2.onReceive', 'FRAMEWORK', 'sendBroadcast(ACTION_GO_TO_CARD) (same-package, not exported)', evidence=FW_RECEIVER + '; SRC service/CardPlayerService.java:229-235; ui/CardPlayerFragment.java:220-241')
e('CardPlayerService$1.onStopPlaying', 'CardPlayerFragment$2.onReceive', 'FRAMEWORK', 'sendBroadcast(ACTION_PLAYING_STOPPED) (same-package, not exported)', evidence=FW_RECEIVER + '; SRC service/CardPlayerService.java:238-243; ui/CardPlayerFragment.java:220-241,243-245')
e('CardPlayerFragment$2.onReceive', 'CardPlayerActivity.gotoCardId', 'CALL', 'the activity is foreground and the card id changed', guard='activity.isActivityForeground()', evidence='SRC ui/CardPlayerFragment.java:238-239')
e('CardPlayerActivity.gotoCardId', 'S_CARD_PLAYER', 'ENTERS', 'gotoCard(card) displays it', evidence='SRC ui/CardPlayerActivity.java:188-191,171-177')
e('CardTTSUtil.speakCardQuestion(Card,OnTextToSpeechCompletedListener)', 'CardPlayerState$4.onTextToSpeechCompleted', 'FRAMEWORK', 'the TTS finishes speaking the question (playQuestion\'s listener)', env=ENV_TTS, evidence=FW_TTS + '; SRC service/cardplayer/CardPlayerState.java:172-190')
e('CardPlayerState$4.onTextToSpeechCompleted', 'CardPlayerState$4$1.run', 'FRAMEWORK', 'handler.postDelayed(...)', env=ENV_TTS, evidence=FW_HANDLER + '; SRC service/cardplayer/CardPlayerState.java:176-187')
e('CardPlayerState$4$1.run', 'CardPlayerState$2.transition', 'CALL', 'context.getState().transition(context, PLAYING_QUESTION_COMPLETED): state is PLAYING_QUESTION (bytecode: virtual call CHA-resolved to the PLAYING_QUESTION enum body)', env=ENV_TTS, evidence='SRC service/cardplayer/CardPlayerState.java:182-186 (bytecode); service/cardplayer/CardPlayerState.java:69-115')
e('CardTTSUtil.speakCardAnswer(Card,OnTextToSpeechCompletedListener)', 'CardPlayerState$5.onTextToSpeechCompleted', 'FRAMEWORK', 'the TTS finishes speaking the answer (playAnswer\'s listener)', env=ENV_TTS, evidence=FW_TTS + '; SRC service/cardplayer/CardPlayerState.java:196-210')
e('CardPlayerState$5.onTextToSpeechCompleted', 'CardPlayerState$5$1.run', 'FRAMEWORK', 'handler.postDelayed(...)', env=ENV_TTS, evidence=FW_HANDLER + '; SRC service/cardplayer/CardPlayerState.java:199-209')
e('CardPlayerState$5$1.run', 'CardPlayerState$3.transition', 'CALL', 'context.getState().transition(context, PLAYING_ANSWER_COMPLETED): state is PLAYING_ANSWER (bytecode: virtual call CHA-resolved to the PLAYING_ANSWER enum body)', env=ENV_TTS, evidence='SRC service/cardplayer/CardPlayerState.java:201-205 (bytecode); service/cardplayer/CardPlayerState.java:117-163')
e('CardPlayerFragment$1.onClick', 'CardPlayerFragment.displaySettingsDialog', 'CALL', 'card_player_settings menu item', evidence='SRC ui/CardPlayerFragment.java:140-145,209-213')
e('CardPlayerFragment.displaySettingsDialog', 'CardPlayerSettingDialogFragment.onAttach', 'LIFECYCLE', 'a new CardPlayerSettingDialogFragment is shown', evidence=FW_DIALOGFRAG + '; SRC ui/CardPlayerFragment.java:211-212')
e('CardPlayerSettingDialogFragment.onAttach', 'CardPlayerSettingDialogFragment.onCreateView', 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/CardPlayerSettingDialogFragment.java:64-120')
e('CardPlayerSettingDialogFragment.onCreateView', 'S_CARD_PLAYER', 'ENTERS', 'the settings dialog is shown over Card Player (no distinct page modelled: only two seek bars)', evidence='SRC ui/CardPlayerSettingDialogFragment.java:68-119')
e('S_CARD_PLAYER', 'CardPlayerSettingDialogFragment$1.onProgressChanged', 'FRAMEWORK', 'drag the QA-interval seek bar', gui=['Drag the Q->A interval seek bar'], evidence=FW_VIEW + '; SRC ui/CardPlayerSettingDialogFragment.java:76,86-90')
e('S_CARD_PLAYER', 'CardPlayerSettingDialogFragment$2.onProgressChanged', 'FRAMEWORK', 'drag the card-interval seek bar', gui=['Drag the card-interval seek bar'], evidence=FW_VIEW + '; SRC ui/CardPlayerSettingDialogFragment.java:100,110-114')
e('CardPlayerSettingDialogFragment.onCreateView', 'CardPlayerSettingDialogFragment.onDismiss', 'LIFECYCLE', 'the dialog is dismissed (Back / outside tap)', evidence=FW_DIALOGFRAG + '; SRC ui/CardPlayerSettingDialogFragment.java:122-131')
e('CardPlayerSettingDialogFragment.onDismiss', 'S_CARD_PLAYER', 'ENTERS', 'the seek-bar values are saved to preferences', evidence='SRC ui/CardPlayerSettingDialogFragment.java:124-129')
e('CardPlayerFragment.onDestroyView', 'CardPlayerService.stopPlaying', 'CALL', 'stopPlaying() (make sure playback stops if the fragment is killed)', evidence='SRC ui/CardPlayerFragment.java:125-130,201-207')
e('CardPlayerActivity.onDestroy', 'CardPlayerActivity$3.onServiceDisconnected', 'FRAMEWORK', 'unbindCardPlayerService()', evidence=FW_SERVICECONN + '; SRC ui/CardPlayerActivity.java:90-91,217-219,229-232')
e('CardPlayerActivity.onBackPressed', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_OK) with the current card id; finish() (the Preview/Edit caller restarts)', evidence='SRC ui/CardPlayerActivity.java:180-185')
e('S_CARD_PLAYER', 'CardPlayerActivity.onBackPressed', 'SYSTEM', 'press Back', gui=['Press Back in Card Player'], evidence=FW_ACTIVITY + '; SRC ui/CardPlayerActivity.java:179-185')

# ---- ShareScreen (another app's share sheet, e.g. ColorDict, sends ACTION_SEND text/*)
e('S_ENTRY', 'ShareScreen.<init>', 'ENTRY', 'another app sends ACTION_SEND text/* to AnyMemo (the share sheet)', env=ENV_COLORDICT_SHARE,
  gui=['Share text from another app, choose AnyMemo'], evidence='SRC AndroidManifest.xml:164-172; ' + FW_ACTIVITY)
e('ShareScreen.<init>', 'ShareScreen.onCreate', 'LIFECYCLE', 'Activity lifecycle callback', env=ENV_COLORDICT_SHARE, evidence=FW_ACTIVITY + '; SRC ui/ShareScreen.java:63-95')
e('ShareScreen.onCreate', 'ShareScreen.onClick', 'FRAMEWORK', 'tap the db-name field, Save, Save+Preview or Cancel', gui=['Tap a field or button in the share screen'], env=ENV_COLORDICT_SHARE, evidence=FW_VIEW + '; SRC ui/ShareScreen.java:77-80,96-139')
e('ShareScreen.onClick', 'S_FILEBROWSER', 'ENTERS', 'v == dbnameView: startActivityForResult(FileBrowserActivity, .db)', env=ENV_PICKER, evidence='SRC ui/ShareScreen.java:129-133')
e('ShareScreen.onActivityResult', 'S_SHARE_SCREEN', 'ENTERS', 'the picked path is written into dbnameView', env=ENV_PICKER, evidence='SRC ui/ShareScreen.java:142-157')
e('ShareScreen.onClick', 'S_EXIT', 'ENTERS', 'v == saveButton / savePrevButton / cancelButton: finish()', env=ENV_COLORDICT_SHARE, evidence='SRC ui/ShareScreen.java:102-125')
e('ShareScreen.onClick', 'PreviewEditActivity.<init>', 'ENTRY', 'v == savePrevButton: startActivity(PreviewEditActivity)', env=ENV_COLORDICT_SHARE, evidence='SRC ui/ShareScreen.java:114-119')


# ================================================================== K. TTS (content providers and ShareScreen
#                                                                       are in sections B and J)
# CardTTSUtil.initTTS/speakCardQuestion/speakCardAnswer/stopSpeak/release call AnyMemoTTSImpl/NullAnyMemoTTS
# through the AnyMemoTTS interface with explicit calls the bytecode extractor already covers (AUTO); only the two
# framework-driven callbacks (TextToSpeech init/utterance-completed, MediaPlayer completion for a stored audio tag)
# are written here.
e('AnyMemoTTSImpl.<init>', 'AnyMemoTTSImpl.onInit', 'FRAMEWORK', 'new TextToSpeech(context, this): the engine calls onInit once it is ready', env=ENV_TTS, evidence=FW_TTS + '; SRC tts/AnyMemoTTSImpl.java:92-106')
e('AnyMemoTTSImpl.sayText', 'AnyMemoTTSImpl$2.onUtteranceCompleted', 'FRAMEWORK', 'no stored audio tag matched: myTTS.speak(...) finishes the synthesized utterance', env=ENV_TTS, evidence=FW_TTS + '; SRC tts/AnyMemoTTSImpl.java:136,170-177,183')
e('AnyMemoTTSImpl.sayText', 'SpeakWord.speakWord', 'CALL', 'speakWord.speakWord(s) is tried first (a stored audio tag in the text)', evidence='SRC tts/AnyMemoTTSImpl.java:138')
e('SpeakWord.speakWord', 'SpeakWord$2.onCompletion', 'FRAMEWORK', 'the matched audio clip finishes playing', needs_state=NEED_ATTACH_IMG, evidence=FW_MEDIAPLAYER + '; SRC tts/SpeakWord.java:130,141-147')
e('SpeakWord$2.onCompletion', 'SpeakWord$1.onCompleted', 'CALL', 'mOnCompletedListener.onCompleted() (the SpeakWord-constructor default listener; only before any sayText call on this instance replaces it)', needs_state=NEED_ATTACH_IMG, evidence='SRC tts/SpeakWord.java:37-42,144-146')
e('SpeakWord$2.onCompletion', 'AnyMemoTTSImpl$1.onCompleted', 'CALL', 'mOnCompletedListener.onCompleted() (replaced by AnyMemoTTSImpl.sayText right after this same speakWord() call returned true)', needs_state=NEED_ATTACH_IMG, evidence='SRC tts/SpeakWord.java:144-146; tts/AnyMemoTTSImpl.java:140-148')
e('AnyMemoTTSImpl.sayText', 'AnyMemoTTSImpl$1.onCompleted', 'REGISTER', 'speakWord.setOnCompletedListener(new OnCompletedListener(){AnyMemoTTSImpl$1}) replaces the default listener for this call', needs_state=NEED_ATTACH_IMG, evidence='SRC tts/AnyMemoTTSImpl.java:140-148')
# ---- Dagger converter-map multibinding: DaggerAppComponents$AppComponentsImpl.mapOfClassOfAndConverter() builds the
# injected `Map<Class<?>, Converter> converterMap` field (ConvertIntentService, ConverterFragment). TOOL BUG /
# LIMITATION: tools/extract_calls.py finds zero outgoing calls from this one compiler-generated method (verified:
# `grep` of auto_calls.json for this src is empty), unlike every other Dagger Impl method in this app, which do show
# their calls normally (confirmed working for e.g. injectConvertIntentService -> mapOfClassOfAndConverter itself).
# Likely cause: this method's bytecode is large (14 synthesized Converter instances inlined in one method body,
# no separate per-binding Factory class for most of them) and the extractor's method-body walk stops short or
# mis-parses it; every other provides*/injectXxx method in this build was captured correctly, so this looks like a
# parser edge case specific to one unusually large synthetic method rather than a general CHA/library gap. Reported
# as a tool bug in the final message; worked around here with explicit hand edges (AppModules.providesXxx ->
# Converter.<init> is separately auto-covered and confirmed correct).
for _name in ('CSVExporter', 'CSVImporter', 'Mnemosyne2CardsExporter', 'Mnemosyne2CardsImporter', 'MnemosyneXMLExporter',
              'MnemosyneXMLImporter', 'QATxtExporter', 'QATxtImporter', 'Supermemo2008XMLImporter', 'SupermemoXMLImporter',
              'TabTxtExporter', 'TabTxtImporter', 'ZipExporter', 'ZipImporter'):
    e('DaggerAppComponents$AppComponentsImpl.mapOfClassOfAndConverter', 'AppModules.provides' + _name, 'CALL',
      'builds the Class -> Converter multibinding map (one @Provides @IntoMap entry per converter)', evidence=FW_DAGGER + '; SRC modules/AppModules.java:49-177 (bytecode call not captured by extract_calls.py for this method; see AGENT_NOTES.md)')
# the SAX-parser importers (MnemosyneXMLImporter, SupermemoXMLImporter, Supermemo2008XMLImporter) extend
# org.xml.sax.helpers.DefaultHandler: convert() hands the file to a SAXParser, which then calls back
# startDocument/startElement/characters/endElement/endDocument/setDocumentLocator on the handler (library not
# available locally: org.xml.sax, INFERRED).
FW_SAX = 'INFERRED org.xml.sax (a SAXParser driven by convert()) calls back startDocument/setDocumentLocator/startElement/characters/endElement/endDocument on the registered DefaultHandler while parsing (SAX implementation source not read)'
for _cls in ('MnemosyneXMLImporter', 'SupermemoXMLImporter', 'Supermemo2008XMLImporter'):
    for _cb in ('startDocument', 'setDocumentLocator', 'startElement', 'characters', 'endElement', 'endDocument'):
        e(_cls + '.convert', _cls + '.' + _cb, 'FRAMEWORK', 'the SAX parser calls back the handler while parsing the XML file', evidence=FW_SAX)

# AnyMemoTTSImpl$1.onCompleted calls onTextToSpeechCompletedListener.onTextToSpeechCompleted(s), an explicit virtual
# call on the AnyMemoTTS.OnTextToSpeechCompletedListener field captured in its constructor: AUTO resolves this to
# every implementer (CardPlayerState$4/$5 in the card-player flow; QACardActivity's plain speakQuestion/speakAnswer
# pass null, so nothing fires there).
for cb in ('onCreate', 'onAttach', 'onCreateView'):
    e('OpenActionsFragment.<init>', 'OpenActionsFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/OpenActionsFragment.java:70-117')
for item, dst, env, need in (
        ('studyItem', 'S_STUDY', None, None),
        ('editItem', 'S_PREVIEW_EDIT', None, None),
        ('listItem', 'S_CARD_LIST', None, None),
        ('quizItem', 'S_DLG_QUIZ_LAUNCHER', None, None),
        ('settingsItem', 'S_SETTINGS', None, None),
        ('statisticsItem', 'S_STATISTICS', None, None),
        ('cardPlayerItem', 'S_CARD_PLAYER', None, None)):
    gui('S_DLG_OPEN_ACTIONS', 'OpenActionsFragment$1.onClick', 'Tap "%s" in the action sheet' % item.replace('Item', ''), evidence=FW_VIEW + '; SRC ui/OpenActionsFragment.java:119-201')
e('OpenActionsFragment$1.onClick', 'S_STUDY', 'ENTERS', 'v == studyItem', evidence='SRC ui/OpenActionsFragment.java:121-127')
e('OpenActionsFragment$1.onClick', 'S_PREVIEW_EDIT', 'ENTERS', 'v == editItem', evidence='SRC ui/OpenActionsFragment.java:129-137')
e('OpenActionsFragment$1.onClick', 'S_CARD_LIST', 'ENTERS', 'v == listItem', evidence='SRC ui/OpenActionsFragment.java:139-145')
e('OpenActionsFragment$1.onClick', 'S_DLG_QUIZ_LAUNCHER', 'ENTERS', 'v == quizItem', evidence='SRC ui/OpenActionsFragment.java:147-154')
e('OpenActionsFragment$1.onClick', 'S_SETTINGS', 'ENTERS', 'v == settingsItem', evidence='SRC ui/OpenActionsFragment.java:156-161')
e('OpenActionsFragment$1.onClick', 'S_STATISTICS', 'ENTERS', 'v == statisticsItem', evidence='SRC ui/OpenActionsFragment.java:163-168')
e('OpenActionsFragment$1.onClick', 'ShareUtil.shareDb', 'CALL', 'v == shareItem', evidence='SRC ui/OpenActionsFragment.java:170-172')
e('ShareUtil.shareDb', 'S_EXT_PICKER', 'ENTERS', 'Intent.createChooser(ACTION_SEND) shows the system share sheet', env=ENV_PICKER, evidence='SRC utils/ShareUtil.java:25-36')
e('OpenActionsFragment$1.onClick', 'S_DLG_DELETE_CARD', 'ENTERS', 'v == deleteItem (reuses the delete-confirm page: confirm deleting the whole deck file)', evidence='SRC ui/OpenActionsFragment.java:174-190')
e('OpenActionsFragment$1$1.onClick', 'BaseActivity.restartActivity', 'CALL', 'confirm delete: amFileUtil.deleteDbSafe + restartActivity()', evidence='SRC ui/OpenActionsFragment.java:178-185')
gui('S_DLG_DELETE_CARD', 'OpenActionsFragment$1$1.onClick', 'Tap Delete (confirm)', evidence=FW_DIALOGFRAG + '; SRC ui/OpenActionsFragment.java:177-186')
e('OpenActionsFragment$1.onClick', 'S_CARD_PLAYER', 'ENTERS', 'v == cardPlayerItem', evidence='SRC ui/OpenActionsFragment.java:192-197')

# ---- DownloadTabFragment
e('S_MAIN_DOWNLOAD', 'DownloadTabFragment.onAttach', 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/DownloadTabFragment.java:46-50')
e('DownloadTabFragment.onAttach', 'DownloadTabFragment.onCreateView', 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/DownloadTabFragment.java:52-61')
e('DownloadTabFragment.onCreateView', 'DownloadTabFragment.onClick', 'FRAMEWORK', 'tap a download-source button', gui=['Tap AnyMemo / Dropbox on the Download tab'], evidence=FW_VIEW + '; SRC ui/DownloadTabFragment.java:56-70')
e('DownloadTabFragment.onClick', 'AnyMemoDownloaderActivity.<init>', 'ENTRY', 'v == amButton: startActivity(AnyMemoDownloaderActivity)', evidence='SRC ui/DownloadTabFragment.java:64-66')
e('DownloadTabFragment.onClick', 'DropboxOauth2AccountActivity.<init>', 'ENTRY', 'v == dropboxButton: startActivity(DropboxOauth2AccountActivity)', evidence='SRC ui/DownloadTabFragment.java:67-69')

# ---- MiscTabFragment
for cb in ('onAttach', 'onCreate', 'onCreateView', 'onDestroy', 'onSaveInstanceState'):
    e('S_MAIN_MISC', 'MiscTabFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/MiscTabFragment.java:128-222,400-406')
e('MiscTabFragment.onCreateView', 'MiscTabFragment.onClick', 'FRAMEWORK', 'tap any Misc-tab button (every button shares one OnClickListener, dispatched by v == field)', gui=['Tap a button on the Misc tab'], evidence=FW_VIEW + '; SRC ui/MiscTabFragment.java:156-221,224-398')
e('MiscTabFragment.onClick', 'S_OPTION_SCREEN', 'ENTERS', 'v == optionButton', evidence='SRC ui/MiscTabFragment.java:226-228')
e('MiscTabFragment.onClick', 'S_DLG_EXPORT_ANYMEMO', 'ENTERS', 'v == exportAnyMemoButton', needs_state=NEED_DECK, evidence='SRC ui/MiscTabFragment.java:253-256')
e('MiscTabFragment.onClick', 'S_FILEBROWSER', 'ENTERS', 'v == importAnyMemoButton: ACTION_OPEN_DOCUMENT', env=ENV_PICKER, evidence='SRC ui/MiscTabFragment.java:247-252')
for btn, converter in (('importMnemosyneButton', 'MnemosyneXMLImporter'), ('importSupermemoButton', 'SupermemoXMLImporter'),
                       ('importCSVButton', 'CSVImporter'), ('importZipButton', 'ZipImporter'), ('importTabButton', 'TabTxtImporter'),
                       ('importQAButton', 'QATxtImporter'), ('importSupermemo2008Button', 'Supermemo2008XMLImporter'),
                       ('importMnemosyne2CardsButton', 'Mnemosyne2CardsImporter')):
    e('MiscTabFragment.onClick', 'MiscTabFragment.launchImportConvert', 'CALL', 'v == %s' % btn, evidence='SRC ui/MiscTabFragment.java:266-289,408-414')
e('MiscTabFragment.launchImportConvert', 'S_EXT_PICKER', 'ENTERS', 'ACTION_OPEN_DOCUMENT is started for the chosen importer format', env=ENV_PICKER, evidence='SRC ui/MiscTabFragment.java:410-413')
for btn, converter in (('exportMnemosyneButton', 'MnemosyneXMLExporter'), ('exportCSVButton', 'CSVExporter'), ('exportTabButton', 'TabTxtExporter'),
                       ('exportQAButton', 'QATxtExporter'), ('exportZipButton', 'ZipExporter'), ('exportMnemosyne2CardsButton', 'Mnemosyne2CardsExporter')):
    e('MiscTabFragment.onClick', 'ConverterFragment.<init>', 'CALL', 'v == %s' % btn, needs_state=NEED_DECK, evidence='SRC ui/MiscTabFragment.java:290-337')
e('MiscTabFragment.onClick', 'S_DLG_CONVERTER', 'ENTERS', 'df.show(...)', needs_state=NEED_DECK, evidence='SRC ui/MiscTabFragment.java:296,304,312,320,328,336')
e('MiscTabFragment.onClick', 'SettingsScreen.<init>', 'ENTRY', 'v == defaultSettingsButton: startActivity(SettingsScreen) for the empty/default db', evidence='SRC ui/MiscTabFragment.java:339-344')
e('MiscTabFragment.onClick', 'DatabaseMerger.<init>', 'ENTRY', 'v == mergeButton', evidence='SRC ui/MiscTabFragment.java:346-349')
e('MiscTabFragment.onClick', 'S_DLG_RESET_PREF', 'ENTERS', 'v == resetButton', evidence='SRC ui/MiscTabFragment.java:350-366')
gui('S_DLG_RESET_PREF', 'MiscTabFragment$1.onClick', 'Tap OK (confirm reset)', evidence=FW_DIALOGFRAG + '; SRC ui/MiscTabFragment.java:354-363')
e('MiscTabFragment$1.onClick', 'S_EXIT', 'ENTERS', 'clear all preferences then mActivity.finish()', evidence='SRC ui/MiscTabFragment.java:357-362')
e('MiscTabFragment.onClick', 'S_DLG_DONATE', 'ENTERS', 'v == donateButton (non-pro flavor only)', evidence='SRC ui/MiscTabFragment.java:367-387')
gui('S_DLG_DONATE', 'MiscTabFragment$2.onClick', 'Tap "Buy the pro version"', evidence=FW_DIALOGFRAG + '; SRC ui/MiscTabFragment.java:375-380')
e('MiscTabFragment$2.onClick', 'S_EXT_BROWSER', 'ENTERS', 'ACTION_VIEW/CATEGORY_BROWSABLE to the pro-version link', env=ENV_EXT_BROWSER, evidence='SRC ui/MiscTabFragment.java:376-379')
e('MiscTabFragment.onClick', 'S_EXT_BROWSER', 'ENTERS', 'v == helpButton: ACTION_VIEW/CATEGORY_BROWSABLE to the versions-view website', env=ENV_EXT_BROWSER, evidence='SRC ui/MiscTabFragment.java:388-394')
e('MiscTabFragment.onClick', 'AboutUtil.createAboutDialog', 'CALL', 'v == aboutButton', evidence='SRC ui/MiscTabFragment.java:395-397')
e('MiscTabFragment.onActivityResult', 'DatabaseImportUtil.handleImportDbResult', 'CALL', 'REQUEST_CODE_IMPORT_DB, RESULT_OK', env=ENV_PICKER, evidence='SRC ui/MiscTabFragment.java:418-420')
e('MiscTabFragment.onActivityResult', 'FolderImportExportUtil.importFolder', 'CALL', 'REQUEST_CODE_IMPORT_FOLDER, RESULT_OK', env=ENV_PICKER, evidence='SRC ui/MiscTabFragment.java:421-422')
e('MiscTabFragment.onActivityResult', 'FolderImportExportUtil.exportFolder', 'CALL', 'REQUEST_CODE_EXPORT_FOLDER, RESULT_OK', env=ENV_PICKER, evidence='SRC ui/MiscTabFragment.java:423-424')
e('MiscTabFragment.onActivityResult', 'MiscTabFragment.invokeImportConversion', 'CALL', 'REQUEST_CODE_IMPORT_CONVERT, RESULT_OK, the converted output file does not already exist', env=ENV_PICKER, evidence='SRC ui/MiscTabFragment.java:425-461')
e('MiscTabFragment.onActivityResult', 'S_DLG_CONVERT_MERGE', 'ENTERS', 'REQUEST_CODE_IMPORT_CONVERT, RESULT_OK, the converted output file already exists', env=ENV_PICKER, evidence='SRC ui/MiscTabFragment.java:435-459')
gui('S_DLG_CONVERT_MERGE', 'MiscTabFragment$4.onClick', 'Tap Yes (overwrite the existing converted file)', evidence=FW_DIALOGFRAG + '; SRC ui/MiscTabFragment.java:439-444')
e('MiscTabFragment$4.onClick', 'MiscTabFragment.invokeImportConversion', 'CALL', 'invokeImportConversion(uri, outputPath)', evidence='SRC ui/MiscTabFragment.java:441-442')
gui('S_DLG_CONVERT_MERGE', 'MiscTabFragment$3.onClick', 'Tap No (back up and replace)', evidence=FW_DIALOGFRAG + '; SRC ui/MiscTabFragment.java:445-457')
e('MiscTabFragment$3.onClick', 'MiscTabFragment.invokeImportConversion', 'CALL', 'deleteFileWithBackup then invokeImportConversion(uri, outputPath)', evidence='SRC ui/MiscTabFragment.java:448-450')
e('MiscTabFragment.invokeImportConversion', 'S_MAIN_MISC', 'ENTERS', 'ConvertIntentService is started in the background and a Toast is shown; the Misc tab stays on screen', evidence='SRC ui/MiscTabFragment.java:468-478')


# ================================================================== M. anonymous-class callbacks (generated from the listener table)
# Each anonymous class (Foo$N) that the bytecode extractor cannot link is entered from the method that creates it
# (its `new` site, named in scratch/listeners.txt) through the framework callback of its interface. The citation is
# the interface's framework constant plus the class body lines of the app source. Generated by scratch/gen_anon.py,
# then checked by hand against the source of each listed class (see scratch/anon_flags.txt).
FW_SORT = ('INFERRED java.util.Collections.sort / List.sort calls Comparator.compare for every pair of elements '
           '(JDK source not read)')
FW_TAG = ('INFERRED android.text.Html.fromHtml calls the registered Html.TagHandler.handleTag for each unknown tag '
          '(platform source not read)')

gui('AMGUIUtility.displayException', 'AMGUIUtility$3.onClick', 'Tap a dialog button (listener at utils/AMGUIUtility.java:69)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC utils/AMGUIUtility.java:69-73')
e('AMGUIUtility.doProgressTask(Activity,String,String,ProgressTask)', 'AMGUIUtility$4.run', 'FRAMEWORK', 'the framework calls run (Thread) at utils/AMGUIUtility.java:80', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:80-112')
e('AMGUIUtility$4.run', 'AMGUIUtility$4$1.run', 'FRAMEWORK', 'the framework calls run (Runnable) at utils/AMGUIUtility.java:84', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:84-89')
e('AMGUIUtility$4.run', 'AMGUIUtility$4$2.run', 'FRAMEWORK', 'the framework calls run (Runnable) at utils/AMGUIUtility.java:92', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:92-100')
e('AMGUIUtility$4.run', 'AMGUIUtility$4$3.run', 'FRAMEWORK', 'the framework calls run (Runnable) at utils/AMGUIUtility.java:103', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:103-109')
gui('AMGUIUtility.doConfirmProgressTask', 'AMGUIUtility$5.onClick', 'Tap a dialog button (listener at utils/AMGUIUtility.java:130)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC utils/AMGUIUtility.java:130-134')
gui('AMGUIUtility.getDialogFinishListener', 'AMGUIUtility$6.onClick', 'Tap a dialog button (listener at utils/AMGUIUtility.java:146)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC utils/AMGUIUtility.java:146-150')
gui('AboutUtil.createAboutDialog', 'AboutUtil$1.onClick', 'Tap a dialog button (listener at utils/AboutUtil.java:49)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC utils/AboutUtil.java:49-58')
e('AnyMemoDBOpenHelperManager.<clinit>', 'AnyMemoDBOpenHelperManager$1.compare', 'FRAMEWORK', 'the framework calls compare (Comparator<String>) at common/AnyMemoDBOpenHelperManager.java:24', evidence=FW_SORT + '; SRC common/AnyMemoDBOpenHelperManager.java:24-33')
e('AnyMemoDownloaderFragment.retrieveAllDatabases', 'AnyMemoDownloaderFragment$1.compare', 'FRAMEWORK', 'the framework calls compare (Comparator<DownloadItem>) at downloader/anymemo/AnyMemoDownloaderFragment.java:124', evidence=FW_SORT + '; SRC downloader/anymemo/AnyMemoDownloaderFragment.java:124-129')
e('AnyMemoDownloaderFragment.getCategories', 'AnyMemoDownloaderFragment$2.compare', 'FRAMEWORK', 'the framework calls compare (Comparator<DownloadItem>) at downloader/anymemo/AnyMemoDownloaderFragment.java:142', evidence=FW_SORT + '; SRC downloader/anymemo/AnyMemoDownloaderFragment.java:142-147')
gui('BaseActivity.enableImmersiveMode', 'BaseActivity$1.onSystemUiVisibilityChange', 'Tap or use the control whose View.OnSystemUiVisibilityChangeListener listener is set at common/BaseActivity.java:159', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC common/BaseActivity.java:159-179')
e('BaseActivity$1.onSystemUiVisibilityChange', 'BaseActivity$1$1.run', 'FRAMEWORK', 'the framework calls run (Runnable) at common/BaseActivity.java:165', evidence=FW_HANDLER + '; SRC common/BaseActivity.java:165-176')
e('CSVExporter.convert', 'CSVExporter$1.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at converter/CSVExporter.java:69', evidence=FW_RX + '; SRC converter/CSVExporter.java:69-76')
e('CardDaoImpl.queryFirstOrdinal(Category)', 'CardDaoImpl$1.call', 'FRAMEWORK', 'the framework calls call (Callable<Card>) at dao/CardDaoImpl.java:49', evidence=FW_RX + '; SRC dao/CardDaoImpl.java:49-69')
e('CardDaoImpl.createCards', 'CardDaoImpl$2.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at dao/CardDaoImpl.java:491', evidence=FW_RX + '; SRC dao/CardDaoImpl.java:491-496')
e('CardDaoImpl.createCard', 'CardDaoImpl$3.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at dao/CardDaoImpl.java:513', evidence=FW_RX + '; SRC dao/CardDaoImpl.java:513-540')
e('CardDaoImpl.swapAllQA', 'CardDaoImpl$4.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at dao/CardDaoImpl.java:601', evidence=FW_RX + '; SRC dao/CardDaoImpl.java:601-608')
e('CardDaoImpl.swapAllQADup', 'CardDaoImpl$5.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at dao/CardDaoImpl.java:616', evidence=FW_RX + '; SRC dao/CardDaoImpl.java:616-634')
e('CardDaoImpl.shuffleOrdinals', 'CardDaoImpl$6.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at dao/CardDaoImpl.java:644', evidence=FW_RX + '; SRC dao/CardDaoImpl.java:644-654')
e('CardDaoImpl.getById', 'CardDaoImpl$7.call', 'FRAMEWORK', 'the framework calls call (Callable<Card>) at dao/CardDaoImpl.java:719', evidence=FW_RX + '; SRC dao/CardDaoImpl.java:719-731')
e('CardDaoImpl.getAllCards', 'CardDaoImpl$8.call', 'FRAMEWORK', 'the framework calls call (Callable<List<Card>>) at dao/CardDaoImpl.java:737', evidence=FW_RX + '; SRC dao/CardDaoImpl.java:737-757')
e('CardDaoImpl.getByOrdinal', 'CardDaoImpl$9.call', 'FRAMEWORK', 'the framework calls call (Callable<Card>) at dao/CardDaoImpl.java:765', evidence=FW_RX + '; SRC dao/CardDaoImpl.java:765-782')
gui('CardFragment.onCreateView', 'CardFragment$1.onClick', 'Tap or use the control whose View.OnClickListener listener is set at ui/CardFragment.java:136', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/CardFragment.java:136-143')
e('CardListActivity.sortList', 'CardListActivity$4.compare', 'FRAMEWORK', 'the framework calls compare (Comparator<CardWrapper>) at ui/CardListActivity.java:346', evidence=FW_SORT + '; SRC ui/CardListActivity.java:346-352')
e('CardListActivity.sortList', 'CardListActivity$5.compare', 'FRAMEWORK', 'the framework calls compare (Comparator<CardWrapper>) at ui/CardListActivity.java:355', evidence=FW_SORT + '; SRC ui/CardListActivity.java:355-361')
e('CardListActivity.sortList', 'CardListActivity$6.compare', 'FRAMEWORK', 'the framework calls compare (Comparator<CardWrapper>) at ui/CardListActivity.java:364', evidence=FW_SORT + '; SRC ui/CardListActivity.java:364-370')
e('CardListActivity.sortList', 'CardListActivity$7.compare', 'FRAMEWORK', 'the framework calls compare (Comparator<CardWrapper>) at ui/CardListActivity.java:373', evidence=FW_SORT + '; SRC ui/CardListActivity.java:373-380')
gui('CardListActivity.<init>', 'CardListActivity$8.onQueryTextSubmit', 'Tap or use the control whose SearchView.OnQueryTextListener listener is set at ui/CardListActivity.java:389', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/CardListActivity.java:389-407')
e('CardListActivity$CardListAdapter.getFilter', 'CardListActivity$CardListAdapter$1.performFiltering', 'FRAMEWORK', 'the framework calls performFiltering (Filter) at ui/CardListActivity.java:529', evidence=FW_FRAG + '; SRC ui/CardListActivity.java:529-579')
e('CardListActivity$CardListAdapter.getFilter', 'CardListActivity$CardListAdapter$1.publishResults', 'FRAMEWORK', 'the framework calls publishResults (Filter) at ui/CardListActivity.java:529', evidence=FW_FRAG + '; SRC ui/CardListActivity.java:529-579')
gui('CardPlayerSettingDialogFragment.onCreateView', 'CardPlayerSettingDialogFragment$1.onStartTrackingTouch', 'Tap or use the control whose OnSeekBarChangeListener listener is set at ui/CardPlayerSettingDialogFragment.java:76', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/CardPlayerSettingDialogFragment.java:76-91')
gui('CardPlayerSettingDialogFragment.onCreateView', 'CardPlayerSettingDialogFragment$1.onStopTrackingTouch', 'Tap or use the control whose OnSeekBarChangeListener listener is set at ui/CardPlayerSettingDialogFragment.java:76', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/CardPlayerSettingDialogFragment.java:76-91')
gui('CardPlayerSettingDialogFragment.onCreateView', 'CardPlayerSettingDialogFragment$2.onStartTrackingTouch', 'Tap or use the control whose OnSeekBarChangeListener listener is set at ui/CardPlayerSettingDialogFragment.java:100', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/CardPlayerSettingDialogFragment.java:100-115')
gui('CardPlayerSettingDialogFragment.onCreateView', 'CardPlayerSettingDialogFragment$2.onStopTrackingTouch', 'Tap or use the control whose OnSeekBarChangeListener listener is set at ui/CardPlayerSettingDialogFragment.java:100', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/CardPlayerSettingDialogFragment.java:100-115')
e('CardTextUtil.<init>', 'CardTextUtil$1.handleTag', 'FRAMEWORK', 'the framework calls handleTag (TagHandler) at utils/CardTextUtil.java:67', evidence=FW_TAG + '; SRC utils/CardTextUtil.java:67-73')
e('CategoryDaoImpl.populateCategory', 'CategoryDaoImpl$1.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at dao/CategoryDaoImpl.java:60', evidence=FW_RX + '; SRC dao/CategoryDaoImpl.java:60-67')
e('CategoryEditorFragment$CategoryAdapter.<init>', 'CategoryEditorFragment$CategoryAdapter$1.compare', 'FRAMEWORK', 'the framework calls compare (Comparator<Category>) at ui/CategoryEditorFragment.java:388', evidence=FW_SORT + '; SRC ui/CategoryEditorFragment.java:388-401')
gui('DatabaseImportUtil.handleImportDbResult', 'DatabaseImportUtil$1.onClick', 'Tap a dialog button (listener at utils/DatabaseImportUtil.java:51)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseImportUtil.java:51-56')
e('DatabaseImportUtil.importDb', 'DatabaseImportUtil$2.accept', 'FRAMEWORK', 'the framework calls accept (Callable<File>) at utils/DatabaseImportUtil.java:65', evidence=FW_RX + '; SRC utils/DatabaseImportUtil.java:65-72')
e('DatabaseImportUtil.importDb', 'DatabaseImportUtil$3.accept', 'FRAMEWORK', 'the framework calls accept (Consumer<File>) at utils/DatabaseImportUtil.java:75', evidence=FW_RX + '; SRC utils/DatabaseImportUtil.java:75-84')
e('DatabaseOperationDialogUtil.showCreateDbDialog', 'DatabaseOperationDialogUtil$1.subscribe', 'FRAMEWORK', 'the framework calls subscribe (MaybeOnSubscribe<File>) at utils/DatabaseOperationDialogUtil.java:41', evidence=FW_RX + '; SRC utils/DatabaseOperationDialogUtil.java:41-83')
gui('DatabaseOperationDialogUtil$1.subscribe', 'DatabaseOperationDialogUtil$1$2.onClick', 'Tap a dialog button (listener at utils/DatabaseOperationDialogUtil.java:68)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:68-73')
e('DatabaseOperationDialogUtil.showDeleteDbDialog', 'DatabaseOperationDialogUtil$2.subscribe', 'FRAMEWORK', 'the framework calls subscribe (MaybeOnSubscribe<File>) at utils/DatabaseOperationDialogUtil.java:87', evidence=FW_RX + '; SRC utils/DatabaseOperationDialogUtil.java:87-116')
gui('DatabaseOperationDialogUtil$2.subscribe', 'DatabaseOperationDialogUtil$2$2.onClick', 'Tap a dialog button (listener at utils/DatabaseOperationDialogUtil.java:100)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:100-106')
e('DatabaseOperationDialogUtil.showCloneDbDialog', 'DatabaseOperationDialogUtil$3.subscribe', 'FRAMEWORK', 'the framework calls subscribe (MaybeOnSubscribe<File>) at utils/DatabaseOperationDialogUtil.java:120', evidence=FW_RX + '; SRC utils/DatabaseOperationDialogUtil.java:120-138')
e('DatabaseOperationDialogUtil.showRenameDbDialog', 'DatabaseOperationDialogUtil$4.subscribe', 'FRAMEWORK', 'the framework calls subscribe (MaybeOnSubscribe<File>) at utils/DatabaseOperationDialogUtil.java:142', evidence=FW_RX + '; SRC utils/DatabaseOperationDialogUtil.java:142-180')
e('DatabaseOperationDialogUtil.showCreateFolderDialog', 'DatabaseOperationDialogUtil$5.subscribe', 'FRAMEWORK', 'the framework calls subscribe (MaybeOnSubscribe<File>) at utils/DatabaseOperationDialogUtil.java:184', evidence=FW_RX + '; SRC utils/DatabaseOperationDialogUtil.java:184-218')
gui('DatabaseOperationDialogUtil$5.subscribe', 'DatabaseOperationDialogUtil$5$2.onClick', 'Tap a dialog button (listener at utils/DatabaseOperationDialogUtil.java:201)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:201-206')
e('DatabaseUtil.mergeDatabases', 'DatabaseUtil$1.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at utils/DatabaseUtil.java:60', evidence=FW_RX + '; SRC utils/DatabaseUtil.java:60-70')
e('DatabasesProvider.query', 'DatabasesProvider$1.accept', 'FRAMEWORK', 'the framework calls accept (FilenameFilter) at provider/DatabasesProvider.java:67', evidence=FW_FRAG + '; SRC provider/DatabasesProvider.java:67-72')
gui('DictionaryUtil.showLookupListDialog', 'DictionaryUtil$1.onItemClick', 'Tap or use the control whose AdapterView.OnItemClickListener listener is set at utils/DictionaryUtil.java:102', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC utils/DictionaryUtil.java:102-110')
gui('DoubleClickButton.<init>(Context,AttributeSet,int)', 'DoubleClickButton$1.onClick', 'Tap or use the control whose View.OnClickListener listener is set at ui/widgets/DoubleClickButton.java:87', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/widgets/DoubleClickButton.java:87-104')
e('DropboxApiHelper.getUserInfo', 'DropboxApiHelper$1.subscribe', 'FRAMEWORK', 'the framework calls subscribe (SingleOnSubscribe<UserInfo>) at downloader/dropbox/DropboxApiHelper.java:78', evidence=FW_RX + '; SRC downloader/dropbox/DropboxApiHelper.java:78-113')
e('DropboxApiHelper.createFolder', 'DropboxApiHelper$2.subscribe', 'FRAMEWORK', 'the framework calls subscribe (CompletableOnSubscribe) at downloader/dropbox/DropboxApiHelper.java:117', evidence=FW_RX + '; SRC downloader/dropbox/DropboxApiHelper.java:117-139')
e('DropboxApiHelper.listFiles', 'DropboxApiHelper$3.subscribe', 'FRAMEWORK', 'the framework calls subscribe (ObservableOnSubscribe<List<DownloadItem>>) at downloader/dropbox/DropboxApiHelper.java:143', evidence=FW_RX + '; SRC downloader/dropbox/DropboxApiHelper.java:143-190')
e('DropboxApiHelper.downloadFile', 'DropboxApiHelper$4.call', 'FRAMEWORK', 'the framework calls call (Callable<String>) at downloader/dropbox/DropboxApiHelper.java:194', evidence=FW_RX + '; SRC downloader/dropbox/DropboxApiHelper.java:194-229')
e('DropboxApiHelper.uploadDropbox', 'DropboxApiHelper$5.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at downloader/dropbox/DropboxApiHelper.java:233', evidence=FW_RX + '; SRC downloader/dropbox/DropboxApiHelper.java:233-255')
gui('ErrorUtil.showNonFatalError', 'ErrorUtil$3.onClick', 'Tap a dialog button (listener at utils/ErrorUtil.java:58)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC utils/ErrorUtil.java:58-62')
e('ExportAnyMemoDbFragment.onActivityResult', 'ExportAnyMemoDbFragment$2.accept', 'FRAMEWORK', 'the framework calls accept (Callable<Boolean>) at ui/ExportAnyMemoDbFragment.java:66', evidence=FW_RX + '; SRC ui/ExportAnyMemoDbFragment.java:66-75')
e('ExportAnyMemoDbFragment.onActivityResult', 'ExportAnyMemoDbFragment$3.accept', 'FRAMEWORK', 'the framework calls accept (Consumer<Boolean>) at ui/ExportAnyMemoDbFragment.java:78', evidence=FW_RX + '; SRC ui/ExportAnyMemoDbFragment.java:78-88')
e('FileBrowserFragment.importDb', 'FileBrowserFragment$6.call', 'FRAMEWORK', 'the framework calls call (io.reactivex.functions.Consumer<Throwable>) at ui/FileBrowserFragment.java:378', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:378-384')
e('FileBrowserFragment$FileBrowserAdapter.setItems', 'FileBrowserFragment$FileBrowserAdapter$3.compare', 'FRAMEWORK', 'the framework calls compare (Comparator<String>) at ui/FileBrowserFragment.java:598', evidence=FW_SORT + '; SRC ui/FileBrowserFragment.java:598-613')
e('FlipableCardFragment.onCreateView', 'FlipableCardFragment$1.getCount', 'FRAMEWORK', 'the framework calls getCount (FragmentStatePagerAdapter) at ui/FlipableCardFragment.java:78', evidence=FW_FRAG + '; SRC ui/FlipableCardFragment.java:79-90')
e('FlipableCardFragment.onCreateView', 'FlipableCardFragment$1.getItem', 'FRAMEWORK', 'the framework calls getItem (FragmentStatePagerAdapter) at ui/FlipableCardFragment.java:78', evidence=FW_FRAG + '; SRC ui/FlipableCardFragment.java:79-90')
e('FolderImportExportUtil.importFolder', 'FolderImportExportUtil$1.accept', 'FRAMEWORK', 'the framework calls accept (Callable<Pair<Integer, List<String>>>) at utils/FolderImportExportUtil.java:40', evidence=FW_RX + '; SRC utils/FolderImportExportUtil.java:40-63')
e('FolderImportExportUtil.importFolder', 'FolderImportExportUtil$2.accept', 'FRAMEWORK', 'the framework calls accept (Consumer<Pair<Integer, List<String>>>) at utils/FolderImportExportUtil.java:66', evidence=FW_RX + '; SRC utils/FolderImportExportUtil.java:66-74')
e('FolderImportExportUtil.exportFolder', 'FolderImportExportUtil$4.accept', 'FRAMEWORK', 'the framework calls accept (Callable<Integer>) at utils/FolderImportExportUtil.java:83', evidence=FW_RX + '; SRC utils/FolderImportExportUtil.java:83-113')
e('FolderImportExportUtil.exportFolder', 'FolderImportExportUtil$5.accept', 'FRAMEWORK', 'the framework calls accept (Consumer<Integer>) at utils/FolderImportExportUtil.java:116', evidence=FW_RX + '; SRC utils/FolderImportExportUtil.java:116-121')
gui('GradeButtonsFragment.onCreateView', 'GradeButtonsFragment$2.onTouch', 'Tap or use the control whose View.OnTouchListener listener is set at ui/GradeButtonsFragment.java:155', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/GradeButtonsFragment.java:155-162')
e('LearnQueueManager.flushDirtyCache', 'LearnQueueManager$1.run', 'FRAMEWORK', 'the framework calls run (Runnable) at queue/LearnQueueManager.java:246', evidence=FW_HANDLER + '; SRC queue/LearnQueueManager.java:246-278')
e('LearnQueueManager$1.run', 'LearnQueueManager$1$1.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at queue/LearnQueueManager.java:255', evidence=FW_RX + '; SRC queue/LearnQueueManager.java:255-273')
e('LearningDataDaoImpl.resetAllLearningData', 'LearningDataDaoImpl$1.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at dao/LearningDataDaoImpl.java:43', evidence=FW_RX + '; SRC dao/LearningDataDaoImpl.java:43-50')
e('MnemosyneXMLExporter.convert', 'MnemosyneXMLExporter$1.call', 'FRAMEWORK', 'the framework calls call (Callable<List<Card>>) at converter/MnemosyneXMLExporter.java:52', evidence=FW_RX + '; SRC converter/MnemosyneXMLExporter.java:52-61')
e('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onError', 'FRAMEWORK', 'the framework calls onError (DisposableSingleObserver<String>) at downloader/oauth/Oauth2AccountActivity.java:89', evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:89-102')
e('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onSuccess', 'FRAMEWORK', 'the framework calls onSuccess (DisposableSingleObserver<String>) at downloader/oauth/Oauth2AccountActivity.java:89', evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:89-102')
e('Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'Oauth2AccountActivity$2.onComplete', 'FRAMEWORK', 'the framework calls onComplete (DisposableCompletableObserver) at downloader/oauth/Oauth2AccountActivity.java:110', evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:110-123')
e('Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'Oauth2AccountActivity$2.onError', 'FRAMEWORK', 'the framework calls onError (DisposableCompletableObserver) at downloader/oauth/Oauth2AccountActivity.java:110', evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:110-123')
gui('OauthAccessCodeRetrievalFragment$RequestTokenTask.onPostExecute', 'OauthAccessCodeRetrievalFragment$RequestTokenTask$1.onTouch', 'Tap or use the control whose View.OnTouchListener listener is set at downloader/oauth/OauthAccessCodeRetrievalFragment.java:151', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:151-163')
e('OauthAccessCodeRetrievalFragment$RequestTokenTask.onPostExecute', 'OauthAccessCodeRetrievalFragment$RequestTokenTask$2.onPageFinished', 'FRAMEWORK', 'the framework calls onPageFinished (WebViewClient) at downloader/oauth/OauthAccessCodeRetrievalFragment.java:166', evidence=FW_WEBVIEW + '; SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:166-186')
gui('OauthAccountActivity.showAuthErrorDialog', 'OauthAccountActivity$2.onClick', 'Tap a dialog button (listener at downloader/oauth/OauthAccountActivity.java:216)', kind='FRAMEWORK', evidence=FW_DIALOGFRAG + '; SRC downloader/oauth/OauthAccountActivity.java:216-221')
gui('PreviewEditActivity.<init>', 'PreviewEditActivity$12.onQueryTextChange', 'Tap or use the control whose SearchView.OnQueryTextListener listener is set at ui/PreviewEditActivity.java:750', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/PreviewEditActivity.java:750-763')
gui('QACardActivity.displayCard', 'QACardActivity$1.onClick', 'Tap or use the control whose View.OnClickListener listener is set at ui/QACardActivity.java:236', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:236-240')
e('QACardActivity.generateImageOnLongClickListener', 'QACardActivity$3.onLongClick', 'FRAMEWORK', 'the framework calls onLongClick (CardFragment.OnLongClickListener) at ui/QACardActivity.java:692', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:692-723')
gui('QACardActivity.<init>', 'QACardActivity$4.onClick', 'Tap or use the control whose CardFragment.OnClickListener listener is set at ui/QACardActivity.java:726', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:726-732')
gui('QACardActivity.<init>', 'QACardActivity$5.onClick', 'Tap or use the control whose CardFragment.OnClickListener listener is set at ui/QACardActivity.java:734', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:734-740')
gui('QACardActivity.<init>', 'QACardActivity$6.onClick', 'Tap or use the control whose CardFragment.OnClickListener listener is set at ui/QACardActivity.java:742', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:742-748')
gui('QACardActivity.<init>', 'QACardActivity$7.onClick', 'Tap or use the control whose CardFragment.OnClickListener listener is set at ui/QACardActivity.java:749', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:749-755')
gui('QuizLauncherDialogFragment.<init>', 'QuizLauncherDialogFragment$4.beforeTextChanged', 'Tap or use the control whose TextWatcher listener is set at ui/QuizLauncherDialogFragment.java:342', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:342-374')
gui('QuizLauncherDialogFragment.<init>', 'QuizLauncherDialogFragment$4.onTextChanged', 'Tap or use the control whose TextWatcher listener is set at ui/QuizLauncherDialogFragment.java:342', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:342-374')
gui('QuizLauncherDialogFragment.<init>', 'QuizLauncherDialogFragment$5.beforeTextChanged', 'Tap or use the control whose TextWatcher listener is set at ui/QuizLauncherDialogFragment.java:376', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:376-405')
gui('QuizLauncherDialogFragment.<init>', 'QuizLauncherDialogFragment$5.onTextChanged', 'Tap or use the control whose TextWatcher listener is set at ui/QuizLauncherDialogFragment.java:376', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:376-405')
gui('QuizLauncherDialogFragment.<init>', 'QuizLauncherDialogFragment$6.beforeTextChanged', 'Tap or use the control whose TextWatcher listener is set at ui/QuizLauncherDialogFragment.java:407', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:407-442')
gui('QuizLauncherDialogFragment.<init>', 'QuizLauncherDialogFragment$6.onTextChanged', 'Tap or use the control whose TextWatcher listener is set at ui/QuizLauncherDialogFragment.java:407', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:407-442')
gui('QuizLauncherDialogFragment.<init>', 'QuizLauncherDialogFragment$7.beforeTextChanged', 'Tap or use the control whose TextWatcher listener is set at ui/QuizLauncherDialogFragment.java:444', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:444-482')
gui('QuizLauncherDialogFragment.<init>', 'QuizLauncherDialogFragment$7.onTextChanged', 'Tap or use the control whose TextWatcher listener is set at ui/QuizLauncherDialogFragment.java:444', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:444-482')
e('RecentListActionModeUtil.<init>', 'RecentListActionModeUtil$3.onReceive', 'FRAMEWORK', 'the framework calls onReceive (BroadcastReceiver) at utils/RecentListActionModeUtil.java:57', evidence=FW_RECEIVER + '; SRC utils/RecentListActionModeUtil.java:57-67')
e('SettingsScreen.setSpinnerListeners', 'SettingsScreen$8.onNothingSelected', 'FRAMEWORK', 'the framework calls onNothingSelected (AdapterView.OnItemSelectedListener) at ui/SettingsScreen.java:379', evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:379-391')
e('SpeakWord.speakWord', 'SpeakWord$3.run', 'FRAMEWORK', 'the framework calls run (Thread) at tts/SpeakWord.java:152', evidence=FW_HANDLER + '; SRC tts/SpeakWord.java:152-173')
e('TwoFieldsCardFragment.onCreateView', 'TwoFieldsCardFragment$1.getCount', 'FRAMEWORK', 'the framework calls getCount (FragmentStatePagerAdapter) at ui/TwoFieldsCardFragment.java:131', evidence=FW_FRAG + '; SRC ui/TwoFieldsCardFragment.java:132-143')
e('TwoFieldsCardFragment.onCreateView', 'TwoFieldsCardFragment$1.getItem', 'FRAMEWORK', 'the framework calls getItem (FragmentStatePagerAdapter) at ui/TwoFieldsCardFragment.java:131', evidence=FW_FRAG + '; SRC ui/TwoFieldsCardFragment.java:132-143')
e('TwoFieldsCardFragment.onCreateView', 'TwoFieldsCardFragment$2.getCount', 'FRAMEWORK', 'the framework calls getCount (FragmentStatePagerAdapter) at ui/TwoFieldsCardFragment.java:145', evidence=FW_FRAG + '; SRC ui/TwoFieldsCardFragment.java:146-157')
e('TwoFieldsCardFragment.onCreateView', 'TwoFieldsCardFragment$2.getItem', 'FRAMEWORK', 'the framework calls getItem (FragmentStatePagerAdapter) at ui/TwoFieldsCardFragment.java:145', evidence=FW_FRAG + '; SRC ui/TwoFieldsCardFragment.java:146-157')


# =====================================================================
# N  roots and framework dispatch from the second pass (2026-10-26)
#    - lifecycle of the three activities started by an intent (the <init> node is the start of the activity)
#    - ENTERS edges for the three pages that had none (permission dialog, card-row popups)
#    - AsyncTask edges generated from the bytecode execute() / cancel() sites (scratch/gen_async.py);
#      the framework lines are AOSP 8.1.0_r1 lines printed and read (work/fw_src/android-8.1.0_r1)
# ---------------------------------------------------------------------
e('DropboxOauth2AccountActivity.<init>', 'DropboxOauth2AccountActivity.onCreate', 'LIFECYCLE', 'Activity lifecycle callback: the system creates the activity (started from DownloadTabFragment), then calls onCreate, which calls super.onCreate', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/DropboxOauth2AccountActivity.java:19-21')
e('DropboxListActivity.<init>', 'DropboxListActivity.onCreate', 'LIFECYCLE', 'Activity lifecycle callback (the activity is started by DropboxOauth2AccountActivity.onAuthenticated)', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/DropboxListActivity.java:36')
e('UploadDropboxActivity.<init>', 'UploadDropboxActivity.onCreate', 'LIFECYCLE', 'Activity lifecycle callback (the activity is started by DropboxListActivity.openUploadDropbox)', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/UploadDropboxActivity.java:43-45')
e('AnyMemo.onCreate', 'S_PERM_STORAGE', 'ENTERS', 'API <= 29 (SDK_INT <= Q) and WRITE_EXTERNAL_STORAGE not granted: requestPermissions shows the system permission dialog', guard='SDK_INT <= Q and WRITE_EXTERNAL_STORAGE not granted', evidence='SRC ui/AnyMemo.java:124-131')
e('CardListActivity.showListItemPopup', 'S_CARD_LIST_ROW_MENU', 'ENTERS', 'PopupMenu with R.menu.card_list_popup_menu is shown on the tapped row', evidence='SRC ui/CardListActivity.java:189-199,209')
e('CardListActivity.showListItemLongClickPopup', 'S_CARD_LIST_ROW_LONGMENU', 'ENTERS', 'PopupMenu with R.menu.card_list_long_click_popup_menu is shown on the long-pressed row', evidence='SRC ui/CardListActivity.java:212-225')
# ---- AsyncTask edges (generated; see scratch/gen_async.py)
e('AbstractDownloaderFragment$3.onClick', 'AbstractDownloaderFragment$LoadMoreTask.onPreExecute', 'ASYNC', 'new LoadMoreTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC downloader/common/AbstractDownloaderFragment.java:182; SRC downloader/common/AbstractDownloaderFragment.java:241')
e('AbstractDownloaderFragment$DownloadListAdapter$1.onClick', 'AbstractDownloaderFragment$RetrieveTask.onPreExecute', 'ASYNC', 'new RetrieveTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC downloader/common/AbstractDownloaderFragment.java:182; SRC downloader/common/AbstractDownloaderFragment.java:195')
e('AbstractDownloaderFragment$DownloadListAdapter$1.onClick', 'AbstractDownloaderFragment$RetrieveTask.doInBackground', 'ASYNC', 'the worker thread runs doInBackground of RetrieveTask', evidence='FW-SRC core/java/android/os/AsyncTask.java:333; SRC downloader/common/AbstractDownloaderFragment.java:182; SRC downloader/common/AbstractDownloaderFragment.java:208')
e('AbstractDownloaderFragment$RetrieveTask.doInBackground', 'AbstractDownloaderFragment$RetrieveTask.onPostExecute', 'ASYNC', 'the result is delivered to onPostExecute on the main thread', evidence='FW-SRC core/java/android/os/AsyncTask.java:691-696; SRC downloader/common/AbstractDownloaderFragment.java:221')
e('AbstractDownloaderFragment.refreshList', 'AbstractDownloaderFragment$RetrieveTask.onPreExecute', 'ASYNC', 'new RetrieveTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC downloader/common/AbstractDownloaderFragment.java:182; SRC downloader/common/AbstractDownloaderFragment.java:195')
e('AbstractDownloaderFragment.refreshList', 'AbstractDownloaderFragment$RetrieveTask.doInBackground', 'ASYNC', 'the worker thread runs doInBackground of RetrieveTask', evidence='FW-SRC core/java/android/os/AsyncTask.java:333; SRC downloader/common/AbstractDownloaderFragment.java:182; SRC downloader/common/AbstractDownloaderFragment.java:208')
e('AbstractDownloaderFragment$RetrieveTask.doInBackground', 'AbstractDownloaderFragment$RetrieveTask.onPostExecute', 'ASYNC', 'the result is delivered to onPostExecute on the main thread', evidence='FW-SRC core/java/android/os/AsyncTask.java:691-696; SRC downloader/common/AbstractDownloaderFragment.java:221')
e('AbstractDownloaderFragment.startFetchDatabaseTask', 'AbstractDownloaderFragment$FetchDatabaseTask.onPreExecute', 'ASYNC', 'new FetchDatabaseTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC downloader/common/AbstractDownloaderFragment.java:182; SRC downloader/common/AbstractDownloaderFragment.java:305')
e('CardEditor$2.onClick', 'CardEditor$SaveCardTask.onPreExecute', 'ASYNC', 'new SaveCardTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/CardEditor.java:106; SRC ui/CardEditor.java:581')
e('CardEditor.onCreate', 'CardEditor$InitTask.onPreExecute', 'ASYNC', 'new InitTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/CardEditor.java:106; SRC ui/CardEditor.java:493')
e('CardEditor.onOptionsItemSelected', 'CardEditor$SaveCardTask.onPreExecute', 'ASYNC', 'new SaveCardTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/CardEditor.java:106; SRC ui/CardEditor.java:581')
e('CardEditor.onOptionsItemSelected', 'CardEditor$SaveCardTask.doInBackground', 'ASYNC', 'the worker thread runs doInBackground of SaveCardTask', evidence='FW-SRC core/java/android/os/AsyncTask.java:333; SRC ui/CardEditor.java:106; SRC ui/CardEditor.java:600')
e('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$DeleteCategoryTask.onPreExecute', 'ASYNC', 'new DeleteCategoryTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/CategoryEditorFragment.java:78; SRC ui/CategoryEditorFragment.java:286')
e('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$EditCategoryTask.onPreExecute', 'ASYNC', 'new EditCategoryTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/CategoryEditorFragment.java:78; SRC ui/CategoryEditorFragment.java:183')
e('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$NewCategoryTask.onPreExecute', 'ASYNC', 'new NewCategoryTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/CategoryEditorFragment.java:78; SRC ui/CategoryEditorFragment.java:241')
e('CategoryEditorFragment.onCreateView', 'CategoryEditorFragment$InitTask.onPreExecute', 'ASYNC', 'new InitTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/CategoryEditorFragment.java:78; SRC ui/CategoryEditorFragment.java:135')
e('DetailScreen$1.onClick', 'DetailScreen$SaveCardTask.onPreExecute', 'ASYNC', 'new SaveCardTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/DetailScreen.java:104; SRC ui/DetailScreen.java:205')
e('DetailScreen.onCreate', 'DetailScreen$InitTask.onPreExecute', 'ASYNC', 'new InitTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/DetailScreen.java:104; SRC ui/DetailScreen.java:242')
e('GradeButtonsFragment$5.onGradeButtonClick', 'GradeButtonsFragment$GradeTask.onPreExecute', 'ASYNC', 'new GradeTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/GradeButtonsFragment.java:215; SRC ui/GradeButtonsFragment.java:264')
e('OauthAccessCodeRetrievalFragment.onCreateView', 'OauthAccessCodeRetrievalFragment$RequestTokenTask.onPreExecute', 'ASYNC', 'new RequestTokenTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:108; SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:124')
e('OauthAccessCodeRetrievalFragment.onCreateView', 'OauthAccessCodeRetrievalFragment$RequestTokenTask.doInBackground', 'ASYNC', 'the worker thread runs doInBackground of RequestTokenTask', evidence='FW-SRC core/java/android/os/AsyncTask.java:333; SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:108; SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:131')
e('OauthAccessCodeRetrievalFragment$RequestTokenTask.doInBackground', 'OauthAccessCodeRetrievalFragment$RequestTokenTask.onPostExecute', 'ASYNC', 'the result is delivered to onPostExecute on the main thread', evidence='FW-SRC core/java/android/os/AsyncTask.java:691-696; SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:141')
e('OauthAccountActivity$1.onAuthCodeReceived', 'OauthAccountActivity$GetAccessTokenTask.onPreExecute', 'ASYNC', 'new GetAccessTokenTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC downloader/oauth/OauthAccountActivity.java:87; SRC downloader/oauth/OauthAccountActivity.java:167')
e('OauthAccountActivity$1.onAuthCodeReceived', 'OauthAccountActivity$GetAccessTokenTask.doInBackground', 'ASYNC', 'the worker thread runs doInBackground of GetAccessTokenTask', evidence='FW-SRC core/java/android/os/AsyncTask.java:333; SRC downloader/oauth/OauthAccountActivity.java:87; SRC downloader/oauth/OauthAccountActivity.java:178')
e('OauthAccountActivity$GetAccessTokenTask.doInBackground', 'OauthAccountActivity$GetAccessTokenTask.onPostExecute', 'ASYNC', 'the result is delivered to onPostExecute on the main thread', evidence='FW-SRC core/java/android/os/AsyncTask.java:691-696; SRC downloader/oauth/OauthAccountActivity.java:188')
e('OauthAccountActivity.onCreate', 'OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.onPreExecute', 'ASYNC', 'new ValidateAccessTokenAndRunCallbackTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC downloader/oauth/OauthAccountActivity.java:87; SRC downloader/oauth/OauthAccountActivity.java:119')
e('OauthAccountActivity.onCreate', 'OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.doInBackground', 'ASYNC', 'the worker thread runs doInBackground of ValidateAccessTokenAndRunCallbackTask', evidence='FW-SRC core/java/android/os/AsyncTask.java:333; SRC downloader/oauth/OauthAccountActivity.java:87; SRC downloader/oauth/OauthAccountActivity.java:130')
e('OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.doInBackground', 'OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.onPostExecute', 'ASYNC', 'the result is delivered to onPostExecute on the main thread', evidence='FW-SRC core/java/android/os/AsyncTask.java:691-696; SRC downloader/oauth/OauthAccountActivity.java:143')
e('PreviewEditActivity$6.onClick', 'PreviewEditActivity$DeleteCardTask.onPreExecute', 'ASYNC', 'new DeleteCardTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/PreviewEditActivity.java:519; SRC ui/PreviewEditActivity.java:650')
e('PreviewEditActivity.searchCard', 'PreviewEditActivity$SearchCardTask.onPreExecute', 'ASYNC', 'new SearchCardTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/PreviewEditActivity.java:519; SRC ui/PreviewEditActivity.java:695')
e('QuizActivity$2.onCardChanged', 'QuizActivity$ChangeCardTask.doInBackground', 'ASYNC', 'the worker thread runs doInBackground of ChangeCardTask', evidence='FW-SRC core/java/android/os/AsyncTask.java:333; SRC ui/QuizActivity.java:400; SRC ui/QuizActivity.java:420')
e('QuizLauncherDialogFragment.onStart', 'QuizLauncherDialogFragment$InitTask.onPreExecute', 'ASYNC', 'new InitTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/QuizLauncherDialogFragment.java:212; SRC ui/QuizLauncherDialogFragment.java:283')
e('SettingsScreen$1.onClick', 'SettingsScreen$LoadDefaultTask.onPreExecute', 'ASYNC', 'new LoadDefaultTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/SettingsScreen.java:165; SRC ui/SettingsScreen.java:581')
e('SettingsScreen$3.onClick', 'SettingsScreen$SaveButtonTask.onPreExecute', 'ASYNC', 'new SaveButtonTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/SettingsScreen.java:165; SRC ui/SettingsScreen.java:496')
e('SettingsScreen.onOptionsItemSelected', 'SettingsScreen$SaveButtonTask.onPreExecute', 'ASYNC', 'new SaveButtonTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/SettingsScreen.java:165; SRC ui/SettingsScreen.java:496')
e('CategoryEditorFragment$DeleteCategoryTask.onPreExecute', 'CategoryEditorFragment$DeleteCategoryTask.onCancelled', 'ASYNC', 'cancel() was called on DeleteCategoryTask; onCancelled runs on the main thread after the worker finishes', evidence='FW-SRC core/java/android/os/AsyncTask.java:525-526,691-696; SRC ui/CategoryEditorFragment.java:None; SRC ui/CategoryEditorFragment.java:307')
e('CategoryEditorFragment$EditCategoryTask.onPreExecute', 'CategoryEditorFragment$EditCategoryTask.onCancelled', 'ASYNC', 'cancel() was called on EditCategoryTask; onCancelled runs on the main thread after the worker finishes', evidence='FW-SRC core/java/android/os/AsyncTask.java:525-526,691-696; SRC ui/CategoryEditorFragment.java:None; SRC ui/CategoryEditorFragment.java:217')

# ---- section L part 1 (UNREACHABLE, declaration-only groups; refs printed from source) ----
UNREACHABLE = {}
UNREACHABLE['CSVExporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/CSVExporter.java:95', 'SOURCE')
UNREACHABLE['CSVImporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/CSVImporter.java:121', 'SOURCE')
UNREACHABLE['Mnemosyne2CardsExporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/Mnemosyne2CardsExporter.java:229', 'SOURCE')
UNREACHABLE['Mnemosyne2CardsImporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/Mnemosyne2CardsImporter.java:285', 'SOURCE')
UNREACHABLE['MnemosyneXMLExporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/MnemosyneXMLExporter.java:166', 'SOURCE')
UNREACHABLE['MnemosyneXMLImporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/MnemosyneXMLImporter.java:219', 'SOURCE')
UNREACHABLE['QATxtExporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/QATxtExporter.java:62', 'SOURCE')
UNREACHABLE['QATxtImporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/QATxtImporter.java:134', 'SOURCE')
UNREACHABLE['Supermemo2008XMLImporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/Supermemo2008XMLImporter.java:114', 'SOURCE')
UNREACHABLE['SupermemoXMLImporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/SupermemoXMLImporter.java:196', 'SOURCE')
UNREACHABLE['TabTxtImporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/TabTxtImporter.java:38', 'SOURCE')
UNREACHABLE['ZipExporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/ZipExporter.java:41', 'SOURCE')
UNREACHABLE['ZipImporter.getSrcExtension'] = ('no_trigger_in_app', 'getSrcExtension() is implemented by every converter and declared on the Converter interface; no call of it exists in the app (grep: declarations only; bytecode: no invoke site)', 'SRC converter/ZipImporter.java:19', 'SOURCE')
UNREACHABLE['ErrorUtil.showFatalError'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC utils/ErrorUtil.java:32', 'SOURCE')
UNREACHABLE['ErrorUtil.showNonFatalError'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC utils/ErrorUtil.java:52', 'SOURCE')
UNREACHABLE['AMStringUtils.isInteger'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC utils/AMStringUtils.java:45', 'SOURCE')
UNREACHABLE['AMUiUtil.convertPxToDp'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC utils/AMUiUtil.java:45', 'SOURCE')
UNREACHABLE['AMGUIUtility.getDialogFinishListener'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC utils/AMGUIUtility.java:145', 'SOURCE')
UNREACHABLE['RecentListUtil.getRecentDBPath'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC utils/RecentListUtil.java:52', 'SOURCE')
UNREACHABLE['DownloaderUtils.validateDBName'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC downloader/common/DownloaderUtils.java:104', 'SOURCE')
UNREACHABLE['DownloaderUtils.validateEmail'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC downloader/common/DownloaderUtils.java:97', 'SOURCE')
UNREACHABLE['AnyMemoExecutor.waitTask'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC utils/AnyMemoExecutor.java:43', 'SOURCE')
UNREACHABLE['NotificationUtil$DatabaseInfo.getNewCount'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC utils/NotificationUtil.java:107', 'SOURCE')
UNREACHABLE['SetAlarmReceiver.setWidgetUpdateAlarm'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC receiver/SetAlarmReceiver.java:104', 'SOURCE')
UNREACHABLE['SetAlarmReceiver.cancelWidgetUpdateAlarm'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC receiver/SetAlarmReceiver.java:113', 'SOURCE')
UNREACHABLE['CardDaoImpl.getRandomReviewedCards'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC dao/CardDaoImpl.java:546', 'SOURCE')
UNREACHABLE['CardDaoImpl.searchPrevCard'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC dao/CardDaoImpl.java:678', 'SOURCE')
UNREACHABLE['CategoryDaoImpl.populateCategory'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC dao/CategoryDaoImpl.java:57', 'SOURCE')
UNREACHABLE['FilterDaoImpl.getActiveFilter'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC dao/FilterDaoImpl.java:24', 'SOURCE')
UNREACHABLE['AbstractDownloaderFragment.getDownloadItemCount'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC downloader/common/AbstractDownloaderFragment.java:123', 'SOURCE')
UNREACHABLE['CardImageGetter.scaleBitmap'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC ui/CardImageGetter.java:132', 'SOURCE')
UNREACHABLE['GradeButtonsFragment.setButtonText'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC ui/GradeButtonsFragment.java:220', 'SOURCE')
UNREACHABLE['FlipableCardFragment.flipTo'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC ui/FlipableCardFragment.java:96', 'SOURCE')
UNREACHABLE['EditTabFragment.setRecentListUtil'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC ui/EditTabFragment.java:38', 'SOURCE')
UNREACHABLE['CardPlayerService$LocalBinder.getCurrentPlayingCard'] = ('no_trigger_in_app', 'no call of this method in the app (grep: declaration only; bytecode: no invoke site)', 'SRC service/CardPlayerService.java:256', 'SOURCE')







# ---- section L part 2, pass 1 (generated by scratch/gen_L2.py; do not edit by hand) ----
e('AMGUIUtility.displayError', 'AMGUIUtility$1.onCancel', 'FRAMEWORK', 'framework calls onCancel on the object created at utils/AMGUIUtility.java:50', evidence=FW_DIALOGFRAG + '; SRC utils/AMGUIUtility.java:50')
e('AMGUIUtility.displayError', 'AMGUIUtility$2.onClick', 'FRAMEWORK', 'framework calls onClick on the object created at utils/AMGUIUtility.java:50', evidence=FW_DIALOGFRAG + '; SRC utils/AMGUIUtility.java:50')
e('AbstractDownloaderFragment.onCreateView', 'AbstractDownloaderFragment$DownloadListAdapter.getView', 'FRAMEWORK', 'framework calls getView on the object created at downloader/common/AbstractDownloaderFragment.java:158', evidence=FW_VIEW + '; SRC downloader/common/AbstractDownloaderFragment.java:158')
e('AnyMemo.handleOpenIntent', 'AnyMemo$HandleOpenIntentLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'framework calls onCreateLoader on the object created at ui/AnyMemo.java:394', evidence=FW_LOADER + '; SRC ui/AnyMemo.java:394')
e('AnyMemo.handleOpenIntent', 'AnyMemo$HandleOpenIntentLoaderCallbacks.onLoadFinished', 'FRAMEWORK', 'framework calls onLoadFinished on the object created at ui/AnyMemo.java:394', evidence=FW_LOADER + '; SRC ui/AnyMemo.java:394')
e('AnyMemo.handleOpenIntent', 'AnyMemo$HandleOpenIntentLoaderCallbacks.onLoaderReset', 'FRAMEWORK', 'framework calls onLoaderReset on the object created at ui/AnyMemo.java:394', evidence=FW_LOADER + '; SRC ui/AnyMemo.java:394')
e('CardListActivity.onCreate', 'CardListActivity$CardWrapperLoaderCallbacks.onLoaderReset', 'FRAMEWORK', 'framework calls onLoaderReset on the object created at ui/CardListActivity.java:144', evidence=FW_LOADER + '; SRC ui/CardListActivity.java:144')
e('CardPlayerActivity.showNoItemDialog', 'CardPlayerActivity$1.onCancel', 'FRAMEWORK', 'framework calls onCancel on the object created at ui/CardPlayerActivity.java:154', evidence=FW_DIALOGFRAG + '; SRC ui/CardPlayerActivity.java:154')
e('CardPlayerActivity.showNoItemDialog', 'CardPlayerActivity$2.onClick', 'FRAMEWORK', 'framework calls onClick on the object created at ui/CardPlayerActivity.java:154', evidence=FW_DIALOGFRAG + '; SRC ui/CardPlayerActivity.java:154')
e('DatabaseImportUtil.importDb', 'DatabaseImportUtil$4.call', 'FRAMEWORK', 'framework calls call on the object created at utils/DatabaseImportUtil.java:65', evidence=FW_RX + '; SRC utils/DatabaseImportUtil.java:65')
e('DatabaseOperationDialogUtil$1.subscribe', 'DatabaseOperationDialogUtil$1$1.onCancel', 'FRAMEWORK', 'framework calls onCancel on the object created at utils/DatabaseOperationDialogUtil.java:68', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:68')
e('DatabaseOperationDialogUtil$1.subscribe', 'DatabaseOperationDialogUtil$1$3.onClick', 'FRAMEWORK', 'framework calls onClick on the object created at utils/DatabaseOperationDialogUtil.java:48', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:48')
e('DatabaseOperationDialogUtil$2.subscribe', 'DatabaseOperationDialogUtil$2$1.onCancel', 'FRAMEWORK', 'framework calls onCancel on the object created at utils/DatabaseOperationDialogUtil.java:100', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:100')
e('DatabaseOperationDialogUtil$2.subscribe', 'DatabaseOperationDialogUtil$2$3.onClick', 'FRAMEWORK', 'framework calls onClick on the object created at utils/DatabaseOperationDialogUtil.java:93', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:93')
e('DatabaseOperationDialogUtil$4.subscribe', 'DatabaseOperationDialogUtil$4$1.onCancel', 'FRAMEWORK', 'framework calls onCancel on the object created at utils/DatabaseOperationDialogUtil.java:151', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:151')
e('DatabaseOperationDialogUtil$4.subscribe', 'DatabaseOperationDialogUtil$4$2.onClick', 'FRAMEWORK', 'framework calls onClick on the object created at utils/DatabaseOperationDialogUtil.java:151', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:151')
e('DatabaseOperationDialogUtil$5.subscribe', 'DatabaseOperationDialogUtil$5$1.onCancel', 'FRAMEWORK', 'framework calls onCancel on the object created at utils/DatabaseOperationDialogUtil.java:201', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:201')
e('DatabaseOperationDialogUtil$5.subscribe', 'DatabaseOperationDialogUtil$5$3.onClick', 'FRAMEWORK', 'framework calls onClick on the object created at utils/DatabaseOperationDialogUtil.java:192', evidence=FW_DIALOGFRAG + '; SRC utils/DatabaseOperationDialogUtil.java:192')
e('FolderImportExportUtil.importFolder', 'FolderImportExportUtil$3.call', 'FRAMEWORK', 'framework calls call on the object created at utils/FolderImportExportUtil.java:40', evidence=FW_RX + '; SRC utils/FolderImportExportUtil.java:40')
e('GestureSelectionDialogFragment.onCreateView', 'GestureSelectionDialogFragment$GesturesAdapter.getView', 'FRAMEWORK', 'framework calls getView on the object created at ui/GestureSelectionDialogFragment.java:103', evidence=FW_VIEW + '; SRC ui/GestureSelectionDialogFragment.java:103')
e('QACardActivity.startInit', 'QACardActivity$CardTTSUtilLoaderCallbacks.onLoaderReset', 'FRAMEWORK', 'framework calls onLoaderReset on the object created at ui/QACardActivity.java:164', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:164')
e('QACardActivity.startInit', 'QACardActivity$SettingLoaderCallbacks.onLoaderReset', 'FRAMEWORK', 'framework calls onLoaderReset on the object created at ui/QACardActivity.java:162', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:162')
e('QuizActivity.showNoItemDialog', 'QuizActivity$3.onCancel', 'FRAMEWORK', 'framework calls onCancel on the object created at ui/QuizActivity.java:457', evidence=FW_DIALOGFRAG + '; SRC ui/QuizActivity.java:457')
e('QuizActivity.onCreate', 'QuizActivity$QuizQueueManagerLoaderCallbacks.onLoaderReset', 'FRAMEWORK', 'framework calls onLoaderReset on the object created at ui/QuizActivity.java:131', evidence=FW_LOADER + '; SRC ui/QuizActivity.java:131')
e('RecentListFragment.onResume', 'RecentListFragment$RecentListDetailLoaderCallbacks.onLoaderReset', 'FRAMEWORK', 'framework calls onLoaderReset on the object created at ui/RecentListFragment.java:219', evidence=FW_LOADER + '; SRC ui/RecentListFragment.java:219')
e('RecentListFragment.onResume', 'RecentListFragment$RecentListLoaderCallbacks.onLoaderReset', 'FRAMEWORK', 'framework calls onLoaderReset on the object created at ui/RecentListFragment.java:218', evidence=FW_LOADER + '; SRC ui/RecentListFragment.java:218')
e('StudyActivity.showNoItemDialog', 'StudyActivity$1.onCancel', 'FRAMEWORK', 'framework calls onCancel on the object created at ui/StudyActivity.java:408', evidence=FW_DIALOGFRAG + '; SRC ui/StudyActivity.java:408')
e('StudyActivity.onCreate', 'StudyActivity$LearnQueueManagerLoaderCallbacks.onLoaderReset', 'FRAMEWORK', 'framework calls onLoaderReset on the object created at ui/StudyActivity.java:119', evidence=FW_LOADER + '; SRC ui/StudyActivity.java:119')
UNREACHABLE['Card.getCardType'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Card.java:128', 'SOURCE')
UNREACHABLE['Card.getCreationDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Card.java:112', 'SOURCE')
UNREACHABLE['Card.getUpdateDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Card.java:120', 'SOURCE')
UNREACHABLE['Card.setCardType'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Card.java:132', 'SOURCE')
UNREACHABLE['Category.getCreationDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Category.java:56', 'SOURCE')
UNREACHABLE['Category.getUpdateDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Category.java:45', 'SOURCE')
UNREACHABLE['Category.setId'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Category.java:33', 'SOURCE')
UNREACHABLE['Deck.getCreationDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Deck.java:54', 'SOURCE')
UNREACHABLE['Deck.getDescription'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Deck.java:46', 'SOURCE')
UNREACHABLE['Deck.getId'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Deck.java:30', 'SOURCE')
UNREACHABLE['Deck.getName'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Deck.java:38', 'SOURCE')
UNREACHABLE['Deck.getUpdateDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Deck.java:62', 'SOURCE')
UNREACHABLE['Deck.setCreationDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Deck.java:58', 'SOURCE')
UNREACHABLE['Deck.setDescription'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Deck.java:50', 'SOURCE')
UNREACHABLE['Deck.setId'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Deck.java:34', 'SOURCE')
UNREACHABLE['Deck.setName'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Deck.java:42', 'SOURCE')
UNREACHABLE['Deck.setUpdateDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Deck.java:66', 'SOURCE')
UNREACHABLE['DownloadItem.getExtras'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC downloader/common/DownloadItem.java:87', 'SOURCE')
UNREACHABLE['DownloadItem.setExtras'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC downloader/common/DownloadItem.java:67', 'SOURCE')
UNREACHABLE['DropboxApiHelper.createFolder'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC downloader/dropbox/DropboxApiHelper.java:116', 'SOURCE')
UNREACHABLE['Filter.getExpression'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Filter.java:45', 'SOURCE')
UNREACHABLE['Filter.getId'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Filter.java:29', 'SOURCE')
UNREACHABLE['Filter.getIsActive'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Filter.java:53', 'SOURCE')
UNREACHABLE['Filter.getName'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Filter.java:37', 'SOURCE')
UNREACHABLE['Filter.getUpdateDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Filter.java:61', 'SOURCE')
UNREACHABLE['Filter.setExpression'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Filter.java:49', 'SOURCE')
UNREACHABLE['Filter.setId'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Filter.java:33', 'SOURCE')
UNREACHABLE['Filter.setIsActive'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Filter.java:57', 'SOURCE')
UNREACHABLE['Filter.setName'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Filter.java:41', 'SOURCE')
UNREACHABLE['Filter.setUpdateDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Filter.java:65', 'SOURCE')
UNREACHABLE['LearningData.getUpdateDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/LearningData.java:132', 'SOURCE')
UNREACHABLE['LearningData.setUpdateDate'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/LearningData.java:136', 'SOURCE')
UNREACHABLE['Option$CopyToClipboard.parse'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Option.java:135', 'SOURCE')
UNREACHABLE['Option.getEnableArabicEngine'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Option.java:25', 'SOURCE')
UNREACHABLE['Option.setButtonStyle'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Option.java:38', 'SOURCE')
UNREACHABLE['Option.setCopyClipboard'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Option.java:56', 'SOURCE')
UNREACHABLE['Option.setEnableArabicEngine'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Option.java:29', 'SOURCE')
UNREACHABLE['Option.setVolumeKeyShortcut'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode: no invoke site; declaration only)', 'SRC entity/Option.java:47', 'SOURCE')
# ---- end pass 1 ----
