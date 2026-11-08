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
STRICT = True         # sections A-L classify everything (CLASSIFY, ENV/STATE tables, EDIT at the end of the file)

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


# Lifecycle order for the edges that start at a constructor (X.<init>) and for the callbacks after it.
# The system creates the object and then calls its first callback: onAttach for a fragment (when the class has
# one), otherwise onCreate. A ranked callback is reached from the nearest earlier-ranked callback that the class
# list has, following the framework order (FW-SRC core/java/android/app/Fragment.java: onAttach, onCreate,
# onCreateView, onResume; Activity.java:6989-6999 onCreate). onStart/onStop are not in the lists, so an edge may
# skip them (a modelling simplification, not a route error). Unranked callbacks (menu, onSaveInstanceState,
# onCreateContextMenu) are reached from onCreate: the menu machinery and the framework trigger them.
# onDestroy, onDetach and onConfigurationChanged have NO automatic edge (round 1): each needs a real exit or
# rotation trigger, added by hand (AnyMemo below is the first; see scratch/fix_round1.md for the rest).
# onOptionsItemSelected is not chained: a menu item tap is a FRAMEWORK edge from the screen page (S_... entry).
LC_RANK = {'onAttach': 0, 'onCreate': 1, 'onCreateDialog': 2, 'onCreateView': 2, 'onStart': 3, 'onResume': 4,
           'onPause': 5, 'onStop': 6, 'onDestroyView': 7}
LC_NO_TRIGGER = ('onDestroy', 'onDetach', 'onConfigurationChanged', 'onOptionsItemSelected')
def lc_chain(cls, cbs):
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
# group 11: FileBrowserActivity is an activity of this app (not the system picker): it needs external storage only.
ENV_FB_STORAGE = env_text(
    'the device has external storage mounted and readable (FileBrowserActivity is part of this app and lists the '
    'AnyMemo folder on external storage; no other package runs)', ('hardware',))
ENV_NET =env_text('outside package: the AnyMemo download server (anymemo.org) must be reachable (network)', ('network',))
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
ENV_PERM_ANSWER_STORAGE = env_text('the user answers the system permission dialog for WRITE_EXTERNAL_STORAGE (Allow or Deny; the result is delivered once answered)', ('permission',))
ENV_PERM_DENY_STORAGE = env_text('the user taps Deny in the system permission dialog for WRITE_EXTERNAL_STORAGE', ('permission',))
ENV_CARD_SVC_DIES = env_text('the CardPlayerService process is killed or crashes while the card player is open (a system event; unbindService does not report a disconnect)', ('system_event',))
ENV_HW_KEY = env_text('a hardware or volume key is pressed or released while this screen is in front (key event)', ('hardware',))
ENV_EXT_DICT = env_text('outside package: an external dictionary app (ColorDict / Fora / BlueDict) is installed to receive the lookup intent', ('other_app',))
ENV_EXT_BROWSER = env_text('outside package: a browser app handles the ACTION_VIEW/CATEGORY_BROWSABLE link', ('other_app',))
ENV_COLORDICT_SHARE = env_text('outside package: another app (for example ColorDict) starts ShareScreen with an ACTION_SEND text intent', ('other_app',))
ENV_OAUTH_CALLBACK = env_text('outside package: the Dropbox OAuth2 web page redirects back into this app\'s exported anymemo-dropbox:// activity (a browser / Custom Tab and network access)', ('network', 'other_app'))
ENV_NOTIF = env_text('outside package: the user opens the notification shade and taps the notification', ('system_event',))

# ---- STATE gate texts (earlier in-app action needed)
NEED_DECK = state_text('A deck (.db file) was opened at least once, so one is in the recent list / the Download folder has a .db file', ('data',))
# round 1 (G3-5 s11): the export and converter buttons are rows of export_items, which is GONE until the Export header is tapped (misc_tab.xml:256-257; MiscTabFragment.java:240-241)
NEED_EXPORT_SECTION = state_text('The Export section of the Misc tab is expanded: its header was tapped (MiscTabFragment.java:240-241; export_items is GONE in misc_tab.xml:256-257)', ('session',))
NEED_RECENT = state_text('At least one entry exists in the recent-deck list (Recent tab is not empty)', ('data',))
NEED_CARD = state_text('The open deck has at least one card', ('data',))
NEED_CATEGORY = state_text('The open deck has at least one category other than Uncategorized', ('data',))
NEED_ATTACH_IMG = state_text('The current question/answer text names an image file that exists under the AnyMemo images folder', ('file',))
NEED_FILE_MNEMOSYNE = state_text('A Mnemosyne (.xml) export file exists in the Download folder (the baseline Download fixtures have none)', ('file',))
NEED_FILE_SUPERMEMO = state_text('A SuperMemo (.xml) export file exists in the Download folder (the baseline Download fixtures have none)', ('file',))
NEED_FILE_QA = state_text('A QA text file exists in the Download folder (the baseline Download fixtures have none)', ('file',))
NEED_FILE_ZIP = state_text('A zip export file exists in the Download folder', ('file',))
NEED_DB_NAME_TAKEN = state_text("A .db file with the picked file's name already exists in the folder being browsed (FileBrowserFragment.java:336-338)", ('file',))
NEED_SAVED_TOKEN = state_text('A Dropbox access token was saved before (returning user; the fixtures have none)', ('account',))
NEED_AUDIO_RECORDED = state_text('Record was tapped and then tapped again to Stop in this recorder dialog (Play and Save are enabled only after that Stop; AudioRecorderFragment.java:50-58, 103)', ('session',))
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
    'S_FILEBROWSER': 'FileBrowserActivity: a standalone file browser used by CardEditor (image/audio pick), DatabaseMerger, ShareScreen',
    'S_DLG_TYPEFACE_Q': 'FileBrowserFragment dialog (.ttf) opened from the Settings question-typeface field (SettingsScreen.java:712-721)',
    'S_DLG_TYPEFACE_A': 'FileBrowserFragment dialog (.ttf) opened from the Settings answer-typeface field (SettingsScreen.java:723-732)',
    'S_DLG_CREATE_DB': 'Create-new-database name dialog (file browser FAB / menu)',
    'S_DLG_CREATE_FOLDER': 'Create-folder name dialog (file browser menu)',
    'S_DLG_OVERWRITE_DB': 'Confirm overwrite of an existing .db on import',
    'S_DLG_FB_EDIT': 'Long-press popup on a file-browser row: Delete / Clone / Rename',
    'S_STUDY': 'StudyActivity: classic study screen for the open deck',
    'S_QUIZ': 'QuizActivity: quiz-mode study screen (no grading persisted except via the normal grade buttons)',
    'S_CARD_PLAYER': 'CardPlayerActivity: hands-free audio playback of question/answer with play/prev/next/shuffle/repeat',
    'S_DLG_QUIZ_LAUNCHER': 'QuizLauncherDialogFragment: choose quiz by group / category / range, shuffle',
    'S_DLG_CATEGORY_STUDY': 'CategoryEditorFragment shown from Study (menu_memo_category): pick a category; the result goes to Study only',
    'S_DLG_CATEGORY_PREVIEW': 'CategoryEditorFragment shown from Preview/Edit (menu_edit_categories): pick a category; the result goes to Preview/Edit only',
    'S_DLG_CATEGORY_QUIZ': 'CategoryEditorFragment shown from the Quiz launcher: pick a category; the result goes to the launcher only',
    'S_DLG_CATEGORY_CARD': 'CategoryEditorFragment shown from CardEditor (category button): pick a category; the result goes to the editor only',
    'S_DLG_GESTURE': 'GestureSelectionDialogFragment: enable gestures and show which gesture does what',
    'S_DLG_NO_ITEM': 'The "no card to study" dialog (an empty deck or filter)',
    'S_DLG_UNDO_FAIL': 'The "nothing to undo" dialog',
    'S_DLG_DELETE_CARD': 'Confirm card delete (Study menu)',
    'S_DLG_DELETE_CARD_PREVIEW': 'Confirm card delete (Preview-edit menu)',
    'S_DLG_DELETE_DECK': 'Confirm delete of a whole deck file (Open tab deck menu)',
    'S_DLG_WIPE_LEARNING': 'Confirm wipe all learning data (Preview-edit menu)',
    'S_DLG_REMOVE_DUP': 'Confirm remove duplicate cards (Preview-edit menu)',
    'S_DLG_SHUFFLE': 'Confirm shuffle card order (Preview-edit menu)',
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
    'S_DLG_DOWNLOAD_CONFIRM_AM': 'Confirm downloading one AnyMemo database (AnyMemo source)',
    'S_DLG_DOWNLOAD_CONFIRM_DBX': 'Confirm downloading one Dropbox database (Dropbox source)',
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
e('AMApplication.attachBaseContext', 'AMApplication.onCreate', 'LIFECYCLE', 'the system calls Application.onCreate once, after every ContentProvider in the manifest is created', evidence=FW_APP + '; SRC AMApplication.java:62-73')
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
for cb, lsrc in lc_chain('AnyMemo', ('onCreate', 'onResume', 'onOptionsItemSelected', 'onDestroy')):
    e(lsrc, 'AnyMemo.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/AnyMemo.java:115-434')
# AnyMemo exits (round 1): onDestroy has no automatic edge any more. The real exits are the Back key on a main tab
# (no onBackPressed in AnyMemo or BaseActivity: the platform default finishes the activity), a denied
# WRITE_EXTERNAL_STORAGE (AnyMemo.java:175-178) and the Exit button of the unreadable-storage dialog (AnyMemo$3).
for page in ('S_MAIN_RECENT', 'S_MAIN_OPEN', 'S_MAIN_DOWNLOAD', 'S_MAIN_MISC'):
    e(page, 'AnyMemo.onDestroy', 'SYSTEM', 'press Back on a main tab: the default back press finishes the activity, then onDestroy',
      gui=['Press Back on a main tab'], env=ENV_HW_KEY,
      evidence='FW-SRC core/java/android/app/Activity.java:3001-3010 (onBackPressed -> finishAfterTransition), :5580-5584 (-> finish), :7203-7208 (performDestroy -> onDestroy); SRC ui/AnyMemo.java:399-411; no onBackPressed in AnyMemo.java or common/BaseActivity.java')
e('AnyMemo.onRequestPermissionsResult', 'AnyMemo.onDestroy', 'LIFECYCLE', 'WRITE_EXTERNAL_STORAGE denied: Toast, then finish() (the activity is destroyed)',
  guard='grantResults[0] != PERMISSION_GRANTED (AnyMemo.java:169-178; finish() at 178)', env=ENV_PERM_DENY_STORAGE,
  evidence='SRC ui/AnyMemo.java:165-182; FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')
e('AnyMemo$3.onClick', 'AnyMemo.onDestroy', 'LIFECYCLE', 'the Exit button of the unreadable-storage dialog calls finish(); the activity is destroyed',
  evidence='SRC ui/AnyMemo.java:273-277; FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')
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
e('AnyMemo$1.onNavigationItemSelected', 'OptionScreen.<init>', 'INTENT', 'startActivity(OptionScreen) for the Options drawer item', guard='itemId == option_tab_menu (AnyMemo.java:222-223)', evidence='SRC ui/AnyMemo.java:222-223')
e('AnyMemo$1.onNavigationItemSelected', 'AboutUtil.createAboutDialog', 'CALL', 'the About drawer item calls aboutUtil.createAboutDialog()', guard='itemId == about_tab_menu (AnyMemo.java:224-225)', evidence='SRC ui/AnyMemo.java:224-225')
e('AnyMemo$1.onNavigationItemSelected', 'AnyMemo$2.onNavigationItemSelected', 'CALL', 'binding.bottomNavigation.setSelectedItemId(...) re-dispatches to the bottom-nav listener for Recent/Open/Download/Misc', guard='itemId is recent, open, download or misc (AnyMemo.java:213-220)', cls='non_standard', via='material library: BottomNavigationView.setSelectedItemId calls the bottom-nav listener (library source not read)', evidence='SRC ui/AnyMemo.java:213-221; INFERRED com.google.android.material BottomNavigationView.setSelectedItemId dispatches the listener (not read)')
for p in ('S_MAIN_RECENT', 'S_MAIN_OPEN', 'S_MAIN_DOWNLOAD', 'S_MAIN_MISC'):
    gui(p, 'AnyMemo$2.onNavigationItemSelected', 'Tap a bottom-navigation item (Recent / Open / Download / Misc)', evidence=FW_MATERIAL + '; SRC ui/AnyMemo.java:234-261')
e('AnyMemo.initDrawer', 'AnyMemo$2.onNavigationItemSelected@INIT', 'CALL', 'bottomNavigation.setSelectedItemId(recent_tab_menu): the library calls the bottom-nav listener for the Recent item, so the Recent tab is selected by default on a cold start', cls='non_standard', via='material library: BottomNavigationView.setSelectedItemId calls the bottom-nav listener (library source not read)', evidence='SRC ui/AnyMemo.java:263; INFERRED com.google.android.material BottomNavigationView.setSelectedItemId dispatches the listener (not read)')
# AnyMemo$2.onNavigationItemSelected: a single method, no context variants (it switches tab the same way no matter
# which tab was selected before). Group 2 (round 1): the bottom-nav branches no longer enter the tab pages directly.
# Each tab fragment is constructed by the CALL edges below (AnyMemo.java:242-250), and its tab page is entered from the
# fragment's onCreateView (the Open tab from its onResume, in the FileBrowserFragment host block), so the construction and
# lifecycle run first (checker G3-5 steps 6 and 8).
e('RecentListFragment.onCreateView', 'S_MAIN_RECENT', 'ENTERS', 'the Recent tab is shown once its view exists (cold start selects it, AnyMemo.java:263; or the Recent item is tapped)', evidence='SRC ui/RecentListFragment.java:169-182; ui/AnyMemo.java:240-241,253-257')
e('DownloadTabFragment.onCreateView', 'S_MAIN_DOWNLOAD', 'ENTERS', 'the Download tab is shown once its view exists', evidence='SRC ui/DownloadTabFragment.java:52-61; ui/AnyMemo.java:247-248,253-257')
e('MiscTabFragment.onCreateView', 'S_MAIN_MISC', 'ENTERS', 'the Misc tab is shown once its view exists', evidence='SRC ui/MiscTabFragment.java:156-222; ui/AnyMemo.java:249-250,253-257')
# Tab fragments, one branch each (AnyMemo.java:242-250). The bytecode copies of these `new` calls were unguarded and also
# copied to the cold-start @INIT variant. A hand edge on the base pair suppresses the bytecode copy on every variant, so
# the cold start (which takes only the Recent branch) gets none of these three.
e('AnyMemo$2.onNavigationItemSelected', 'OpenTabFragment.<init>', 'CALL', 'itemId == open_tab_menu: new OpenTabFragment()', guard='itemId == open_tab_menu (AnyMemo.java:242-246)', evidence='SRC ui/AnyMemo.java:242-246')
e('AnyMemo$2.onNavigationItemSelected', 'DownloadTabFragment.<init>', 'CALL', 'itemId == download_tab_menu: new DownloadTabFragment()', guard='itemId == download_tab_menu (AnyMemo.java:247-248)', evidence='SRC ui/AnyMemo.java:247-248')
e('AnyMemo$2.onNavigationItemSelected', 'MiscTabFragment.<init>', 'CALL', 'itemId == misc_tab_menu: new MiscTabFragment()', guard='itemId == misc_tab_menu (AnyMemo.java:249-250)', evidence='SRC ui/AnyMemo.java:249-250')
# AnyMemo.java:245 reads FileBrowserFragment.EXTRA_SHOW_CREATE_DB_BUTTON, a constant variable (FileBrowserFragment.java:77: public final static String with a literal). javac inlines it, so the read does not start the class (JLS 12.4.1; INFERRED, the JVM rule was not read). The bytecode copy of that edge is removed.
sup(('AnyMemo$2.onNavigationItemSelected', 'FileBrowserFragment.<clinit>'))
# CardFragment.OnClickListener is implemented by several classes, and a bytecode call on its onClick fans out to all of them.
# QACardActivity.java:236-240 calls the field onQuestionViewClickListener, which is QACardActivity$6 (QACardActivity.java:742-748).
# The other implementors (QACardActivity$4/$5/$7, FileBrowserFragment$7 at FileBrowserFragment.java:448 on a FAB, and
# DropboxListActivity$1 at DropboxListActivity.java:56 on the upload FAB) are suppressed for that call.
# CardFragment.java:136-140 calls textOnClickListener, which QACardActivity sets only to the text listeners
# (QACardActivity.java:258, 270, 281 = $4 and $5), so $6, $7, FileBrowserFragment$7 and DropboxListActivity$1 are suppressed.
sup(('QACardActivity$1.onClick', 'QACardActivity$4.onClick'), ('QACardActivity$1.onClick', 'QACardActivity$5.onClick'),
    ('QACardActivity$1.onClick', 'QACardActivity$7.onClick'), ('QACardActivity$1.onClick', 'FileBrowserFragment$7.onClick'),
    ('QACardActivity$1.onClick', 'DropboxListActivity$1.onClick'),
    ('CardFragment$1.onClick', 'QACardActivity$6.onClick'), ('CardFragment$1.onClick', 'QACardActivity$7.onClick'),
    ('CardFragment$1.onClick', 'FileBrowserFragment$7.onClick'), ('CardFragment$1.onClick', 'DropboxListActivity$1.onClick'))

e('S_MAIN_RECENT', 'AnyMemo.onOptionsItemSelected', 'FRAMEWORK', 'tap the Up/home icon (drawer burger)', gui=['Tap the menu/burger icon'], evidence=FW_MENU + '; SRC ui/AnyMemo.java:413-421')
e('AnyMemo.onOptionsItemSelected', 'S_DRAWER', 'ENTERS', 'binding.drawerLayout.openDrawer(START)', evidence='SRC ui/AnyMemo.java:414-418')
# BaseActivity.onPause/onStop/onConfigurationChanged are shared, un-overridden lifecycle callbacks (one node for
# every BaseActivity subclass): modelled as plain SYSTEM sinks reached from every live page, not as a shared
# "paused" page (a page needs an unambiguous ENTERS target; BaseActivity.onPause does not identify which concrete
# activity paused, so routing it into one page would be wrong for every activity except the one written here).
for src in ('S_MAIN_RECENT', 'S_MAIN_OPEN', 'S_MAIN_DOWNLOAD', 'S_MAIN_MISC'):
    e(src, 'BaseActivity.onPause', 'SYSTEM', 'Press Home or open another app', gui=['Press Home'], evidence=FW_ACTIVITY + '; SRC common/BaseActivity.java:55-59')
    e(src, 'AnyMemo.onResume', 'SYSTEM', 'return to the app from the recent-apps list (the task resumes without being re-created)', gui=['Press Home, then return to the app from the recent-apps list'], evidence=FW_ACTIVITY)
# No edge from AnyMemo.onResume to S_MAIN_RECENT. A return from the recent-apps list shows the page that was in front
# before the pause (the SYSTEM edges above); the Recent tab is selected only in initDrawer (AnyMemo.java:263), which
# loadUiComponents runs, so the cold start reaches S_MAIN_RECENT through onCreate or onResume with the storage permission.

# ---- BaseActivity / QACardActivity lifecycle plumbing shared by every other activity (declared once; each
# activity's own <init> below chains into these the same way AnyMemo's does)
e('BaseActivity.<init>', 'BaseActivity.onConfigurationChanged', 'SYSTEM', 'rotate the device or change the system locale', gui=['Rotate the device'], evidence=FW_ACTIVITY + '; SRC common/BaseActivity.java:68-71')
e('QACardActivity.<init>', 'QACardActivity.onCreate', 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:136-141')
e('QACardActivity.onCreate', 'QACardActivity.onDestroy', 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:488-503')
e('QACardActivity.<init>', 'QACardActivity.onKeyDown', 'SYSTEM', 'a hardware/volume key is pressed', gui=['Press a volume key'], evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:595-608')
e('QACardActivity.<init>', 'QACardActivity.onKeyUp', 'SYSTEM', 'a hardware/volume key is released', gui=['Press a volume key'], evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:611-623')
e('S_QUIZ', 'QACardActivity.onKeyUp@QuizActivity', 'SYSTEM', 'a hardware/volume key is released on the Quiz screen (QuizActivity is the receiver of the inherited onKeyUp)', gui=['Press a volume key'], evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:611-623')
e('S_STUDY', 'QACardActivity.onKeyUp@StudyActivity', 'SYSTEM', 'a hardware/volume key is released on the Study screen (StudyActivity is the receiver of the inherited onKeyUp)', gui=['Press a volume key'], evidence=FW_ACTIVITY + '; SRC ui/QACardActivity.java:611-623')
e('QACardActivity.onKeyUp@QuizActivity', 'QuizActivity.onVolumeUpKeyPressed', 'CALL', 'the volume-up key is handled by the Quiz override', evidence='SRC ui/QACardActivity.java:615 (bytecode receiver variant; QuizActivity override at ui/QuizActivity.java:207)')
e('QACardActivity.onKeyUp@QuizActivity', 'QuizActivity.onVolumeDownKeyPressed', 'CALL', 'the volume-down key is handled by the Quiz override', evidence='SRC ui/QACardActivity.java:619 (bytecode receiver variant; QuizActivity override at ui/QuizActivity.java:219)')
e('QACardActivity.onKeyUp@StudyActivity', 'StudyActivity.onVolumeUpKeyPressed', 'CALL', 'the volume-up key is handled by the Study override', evidence='SRC ui/QACardActivity.java:615 (bytecode receiver variant; StudyActivity override at ui/StudyActivity.java:382)')
e('QACardActivity.onKeyUp@StudyActivity', 'StudyActivity.onVolumeDownKeyPressed', 'CALL', 'the volume-down key is handled by the Study override', evidence='SRC ui/QACardActivity.java:619 (bytecode receiver variant; StudyActivity override at ui/StudyActivity.java:394)')
e('QACardActivity.<init>', 'QACardActivity.<clinit>', 'LIFECYCLE', 'class initialisation', evidence='SRC ui/QACardActivity.java:90 (static field initialiser); INFERRED the class has a static initialiser the JVM runs on first use (Java language rule, not read from a source)')
e('QACardActivity.onCreate', 'QACardActivity.getContentView', 'CALL', 'setContentView(getContentView())', evidence='SRC ui/QACardActivity.java:137-140')
e('QACardActivity.startInit', 'QACardActivity.loadGestures', 'CALL', 'loadGestures()', evidence='SRC ui/QACardActivity.java:160')
e('QACardActivity.loadGestures', 'QACardActivity$8.onGesturePerformed', 'FRAMEWORK', 'a gesture is drawn on the gesture overlay', gui=['Draw a gesture on the card'], evidence=FW_GESTURE + '; SRC ui/QACardActivity.java:531-542,757-770')
e('QACardActivity$8.onGesturePerformed', 'QACardActivity.onGestureDetected', 'CALL', 'the recognised gesture (score > 3.0) is reported', evidence='SRC ui/QACardActivity.java:761-767')
# SettingLoader / CardTTSUtilLoader only override DBLoader.dbLoadInBackground (an explicit call AUTO already
# makes from DBLoader.loadInBackground); the framework drives the shared DBLoader.loadInBackground template method.
e('QACardActivity.startInit', 'QACardActivity$SettingLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'multipleLoaderManager registers the Setting loader', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:162-163,448-465')
e('QACardActivity$SettingLoaderCallbacks.onCreateLoader', 'DBLoader.loadInBackground', 'ASYNC', 'loader.forceLoad() runs loadInBackground on a worker thread', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:449-452; ui/loader/DBLoader.java:41-50')
e('QACardActivity$SettingLoaderCallbacks.onCreateLoader', 'QACardActivity$SettingLoaderCallbacks.onLoadFinished', 'ASYNC', 'the Setting loader that this onCreateLoader made delivers the Setting to this callbacks object on the main thread (DBLoader.loadInBackground runs on a worker thread)', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:449-459; ui/loader/DBLoader.java:41-50')
e('QACardActivity.startInit', 'QACardActivity$CardTTSUtilLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'multipleLoaderManager registers the CardTTSUtil loader', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:164-165,467-485')
e('QACardActivity$CardTTSUtilLoaderCallbacks.onCreateLoader', 'DBLoader.loadInBackground', 'ASYNC', 'loader.forceLoad() runs loadInBackground on a worker thread', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:470-473; ui/loader/DBLoader.java:41-50')
e('QACardActivity$CardTTSUtilLoaderCallbacks.onCreateLoader', 'QACardActivity$CardTTSUtilLoaderCallbacks.onLoadFinished', 'ASYNC', 'the CardTTSUtil loader that this onCreateLoader made delivers the result to this callbacks object on the main thread', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:470-480; ui/loader/DBLoader.java:41-50')
# DBLoader.loadInBackground is one method shared by every loader, and the bytecode links it to every subclass's
# dbLoadInBackground. Suppressed here, so one host's loader cannot reach another host's loader. Each host's
# onCreateLoader reaches its own loader's dbLoadInBackground (Study and Quiz have their own edges above).
sup(('DBLoader.loadInBackground', 'SettingLoader.dbLoadInBackground'),
    ('DBLoader.loadInBackground', 'CardTTSUtilLoader.dbLoadInBackground'),
    ('DBLoader.loadInBackground', 'CardWrapperListLoader.dbLoadInBackground'),
    ('DBLoader.loadInBackground', 'StudyActivity$LearnQueueManagerLoader.dbLoadInBackground'),
    ('DBLoader.loadInBackground', 'QuizActivity$QuizQueueManagerLoader.dbLoadInBackground'))
e('SettingsScreen$SettingLoaderCallbacks.onCreateLoader', 'SettingLoader.dbLoadInBackground', 'ASYNC', 'loader.forceLoad() runs the Setting load on a worker thread (DBLoader.loadInBackground calls this dbLoadInBackground)', evidence=FW_LOADER + '; SRC ui/SettingsScreen.java:398-401; ui/loader/DBLoader.java:41-50')
e('QACardActivity$SettingLoaderCallbacks.onCreateLoader', 'SettingLoader.dbLoadInBackground', 'ASYNC', 'loader.forceLoad() runs the Setting load on a worker thread (DBLoader.loadInBackground calls this dbLoadInBackground)', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:449-452; ui/loader/DBLoader.java:41-50')
e('QACardActivity$CardTTSUtilLoaderCallbacks.onCreateLoader', 'CardTTSUtilLoader.dbLoadInBackground', 'ASYNC', 'loader.forceLoad() runs the CardTTSUtil load on a worker thread (DBLoader.loadInBackground calls this dbLoadInBackground)', evidence=FW_LOADER + '; SRC ui/QACardActivity.java:470-473; ui/loader/DBLoader.java:41-50')
e('CardListActivity$CardWrapperLoaderCallbacks.onCreateLoader', 'CardWrapperListLoader.dbLoadInBackground', 'ASYNC', 'loader.forceLoad() runs the card-wrapper load on a worker thread (DBLoader.loadInBackground calls this dbLoadInBackground)', evidence=FW_LOADER + '; SRC ui/CardListActivity.java:618-624; ui/loader/DBLoader.java:41-50')
# MultipleLoaderManager.checkAllLoadersCompleted() is called explicitly from every *LoaderCallbacks.onLoadFinished
# (AUTO covers that call). It then does handler.post(stored runnable), and the field is typed java.lang.Runnable, so the
# bytecode extractor cannot resolve it (no auto edge). Each activity has its own MultipleLoaderManager (@Inject,
# ui/loader/MultipleLoaderManager.java:61-64), so the stored runnable is wired from that host's own onLoadFinished.
# checkAllLoadersCompleted itself has no outgoing edge: one shared node would let one host's loader reach another's runnable.
LOADERS_DONE = state_text('every loader registered on this MultipleLoaderManager has reported (runningLoaderCount <= 0)', ('session',))
e('QACardActivity$SettingLoaderCallbacks.onLoadFinished', 'QACardActivity$2.run', 'FRAMEWORK', 'handler.post(stored runnable) after the Setting loader reports: QACardActivity family (Study/Quiz/CardPlayer/PreviewEdit)',
  needs_state=LOADERS_DONE, evidence=FW_HANDLER + '; SRC ui/loader/MultipleLoaderManager.java:104-114; ui/QACardActivity.java:167,458')
e('QACardActivity$CardTTSUtilLoaderCallbacks.onLoadFinished', 'QACardActivity$2.run', 'FRAMEWORK', 'handler.post(stored runnable) after the CardTTSUtil loader reports: QACardActivity family',
  needs_state=LOADERS_DONE, evidence=FW_HANDLER + '; SRC ui/loader/MultipleLoaderManager.java:104-114; ui/QACardActivity.java:167,479')
# Study's and Quiz's own callbacks run onPostInit of their own class: the shared runnable (QACardActivity$2.run) would
# dispatch to every QACardActivity subclass, which is a cross-host route.
e('StudyActivity$LearnQueueManagerLoaderCallbacks.onLoadFinished', 'StudyActivity.onPostInit', 'CALL', 'the stored runnable runs onPostInit() on this StudyActivity after every loader has reported',
  needs_state=LOADERS_DONE, evidence='SRC ui/StudyActivity.java:441-442; ui/QACardActivity.java:658-662; ui/loader/MultipleLoaderManager.java:104-114')
e('QuizActivity$QuizQueueManagerLoaderCallbacks.onLoadFinished', 'QuizActivity.onPostInit', 'CALL', 'the stored runnable runs onPostInit() on this QuizActivity after every loader has reported',
  needs_state=LOADERS_DONE, evidence='SRC ui/QuizActivity.java:298-300; ui/QACardActivity.java:658-662; ui/loader/MultipleLoaderManager.java:104-114')
e('QACardActivity$2.run', 'QACardActivity.onPostInit', 'CALL', 'onPostInitRunnable.run() calls onPostInit() (a virtual call CHA-resolved to whichever QACardActivity subclass is running)', evidence='SRC ui/QACardActivity.java:658-662 (bytecode)')
e('QACardActivity.generateImageOnLongClickListener', 'QACardActivity$3.onLongClick', 'REGISTER', 'the returned listener is attached to the question/answer CardFragment.Builder as its long-click listener', evidence='SRC ui/QACardActivity.java:314-317,691-724')
e('QACardActivity$3.onLongClick', 'S_EXT_PICKER', 'ENTERS', 'ACTION_VIEW on the matched image file (through the FileProvider) opens an external image viewer',
  needs_state=NEED_ATTACH_IMG, evidence='SRC ui/QACardActivity.java:691-723')
for n, m in ((4, 'onClickQuestionText'), (5, 'onClickAnswerText'), (6, 'onClickQuestionView'), (7, 'onClickAnswerView')):
    e('QACardActivity$%d.onClick' % n, 'QACardActivity.' + m, 'CALL', 'the click listener field calls %s()' % m, evidence='SRC ui/QACardActivity.java:726-755')


# ================================================================== D. tabs: RecentListFragment,
#                                                                       OpenTabFragment + OpenActionsFragment,
#                                                                       DownloadTabFragment, MiscTabFragment
for cb, lsrc in lc_chain('RecentListFragment', ('onCreate', 'onAttach', 'onDetach', 'onDestroy', 'onCreateView', 'onResume', 'onCreateOptionsMenu')):
    e(lsrc, 'RecentListFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/RecentListFragment.java:127-226')
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
e('RecentListFragment$RecentListAdapter.onBindViewHolder', 'RecentListFragment$RecentListAdapter$1.onClick', 'FRAMEWORK', 'tap a recent-deck row (no row selected)', gui=['Tap a deck in the Recent list'], needs_state=NEED_RECENT, evidence=FW_VIEW + '; SRC ui/RecentListFragment.java:413-428')
# S3b (round 1): no ENTERS from the row tap straight to S_STUDY. The tap starts StudyActivity by INTENT (below), and
# StudyActivity.onPostInit reaches S_STUDY (ui/StudyActivity.java:296-300, the edge at graph_def.py ~632).
e('RecentListFragment$RecentListAdapter.onBindViewHolder', 'RecentListFragment$RecentListAdapter$2.onLongClick', 'FRAMEWORK', 'long-press a recent-deck row', gui=['Long-press a deck in the Recent list'], needs_state=NEED_RECENT, evidence=FW_VIEW + '; SRC ui/RecentListFragment.java:430-440')
e('RecentListFragment$RecentListAdapter$2.onLongClick', 'RecentListActionModeUtil.startActionMode', 'CALL', 'the first long-press (getSelectedItemCount() == 0) starts the action mode', evidence='SRC ui/RecentListFragment.java:433-435')
e('RecentListActionModeUtil.startActionMode', 'RecentListActionModeUtil$1.onReceive', 'FRAMEWORK', 'LocalBroadcastManager delivers ACTION_START_ACTION_MODE (sent to itself)', evidence=FW_LOCALBROADCAST + '; SRC utils/RecentListActionModeUtil.java:35-40,91-94')
e('RecentListActionModeUtil$1.onReceive', 'RecentListActionModeUtil$ActionModeCallback.onCreateActionMode', 'FRAMEWORK', 'startSupportActionMode(callback) creates the CAB and calls onCreateActionMode', evidence=FW_ACTIONMODE + '; SRC utils/RecentListActionModeUtil.java:38,107-114')
e('RecentListActionModeUtil.updateActionMode', 'RecentListActionModeUtil$2.onReceive', 'FRAMEWORK', 'LocalBroadcastManager delivers ACTION_UPDATE_ACTION_MODE', evidence=FW_LOCALBROADCAST + '; SRC utils/RecentListActionModeUtil.java:42-55,96-100')
e('RecentListActionModeUtil$ActionModeCallback.onActionItemClicked', 'RecentListFragment$1.onReceive', 'FRAMEWORK', 'tap "Remove" in the CAB: LocalBroadcastManager delivers ACTION_REMOVE_SELECTED', gui=['Tap Remove in the selection toolbar'], env=None,
  needs_state=NEED_RECENT, evidence=FW_LOCALBROADCAST + '; SRC utils/RecentListActionModeUtil.java:122-129')
e('RecentListActionModeUtil$ActionModeCallback.onDestroyActionMode', 'RecentListActionModeUtil$3.onReceive', 'FRAMEWORK', 'the CAB is dismissed: LocalBroadcastManager delivers ACTION_DESELECT_ALL via mode.finish()/system Back', evidence=FW_LOCALBROADCAST + '; SRC utils/RecentListActionModeUtil.java:57-67,135-139')
e('RecentListFragment$RecentListAdapter.onBindViewHolder', 'RecentListFragment$RecentListAdapter$3.onClick', 'FRAMEWORK', 'tap the "more" button on a recent-deck row', gui=['Tap the "..." button on a deck row'], needs_state=NEED_RECENT, evidence=FW_VIEW + '; SRC ui/RecentListFragment.java:442-452')
e('RecentListFragment$RecentListAdapter$3.onClick', 'OpenActionsFragment.<init>', 'CALL', 'a new OpenActionsFragment is shown for the tapped deck', evidence='SRC ui/RecentListFragment.java:446-451')
# Round 1b B1: the action sheet is entered from its own onCreateView (its view is built there); df.show(...) is at RecentListFragment.java:450
e('OpenActionsFragment.onCreateView', 'S_DLG_OPEN_ACTIONS', 'ENTERS', 'the action sheet is shown (df.show(...) runs in RecentListFragment.java:450; its view is built here)', evidence='SRC ui/OpenActionsFragment.java:85-117; ui/RecentListFragment.java:450')
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


NEED_FB_ROW = state_text('The current folder has at least one file or sub-folder to list, so a row is bound and can be tapped', ('data',))
FB_MENU_GUARD = 'setHasOptionsMenu(true) ran in onCreate (FileBrowserFragment.java:173)'
FB_ROW_IS_FILE = 'the tapped row is a file: clickedFile.isFile() (FileBrowserFragment.java:407); a folder row browses instead, and onFileClickListener != null (:412)'
FW_RECYCLER = ('INFERRED androidx.recyclerview.widget.RecyclerView calls Adapter.getItemCount, onCreateViewHolder '
               'and onBindViewHolder, and ItemDecoration.getItemOffsets and onDraw, while it lays out and draws the rows '
               '(androidx source not read)')

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
# round 1 leak fix: the base openFile auto edge to notifyFileClick would reach UploadDropboxActivity.onFileBrowserFileClick from every host.
# Only the UPLOADDROPBOX variant calls notifyFileClick (explicit edge below).
sup(('FileBrowserFragment.openFile', 'FileBrowserFragment.notifyFileClick'),
    ('ExportAnyMemoDbFragment.onCreate', 'FileBrowserFragment.onCreate'),
    ('ConverterFragment.onCreate', 'FileBrowserFragment.onCreate'),
    # round 1 (G3-5 s18-19): the export and converter result else-branches forward their own request codes (1002, 1003), so the base
    # onActivityResult import branch (needs REQUEST_CODE_IMPORT_DB 1001, FileBrowserFragment.java:106, 326) cannot run. No edge is kept.
    ('ExportAnyMemoDbFragment.onActivityResult', 'FileBrowserFragment.onActivityResult'),
    ('ConverterFragment.onActivityResult', 'FileBrowserFragment.onActivityResult'))
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
               exclude=set(FB_TARGET.values()) | {'UploadDropboxActivity.onFileBrowserFileClick', 'EditTabFragment$1.onFileBrowserFileClick',
                                                 'FileBrowserFragment.notifyFileClick', 'FileBrowserFragment.browseTo', 'FileBrowserFragment.upOneLevel'})
    # a folder row, the "." row, or an exception in the row click (catch at FileBrowserFragment.java:425-428) browses this host's folder
    e('FileBrowserFragment.openFile@' + v, 'FileBrowserFragment.browseTo@' + v, 'CALL', 'browse this host\'s folder for a folder row, the "." row, or a click that throws',
      guard='a folder row or "." (FileBrowserFragment.java:388-389, 404-405), or the click threw (:425-428)', evidence='SRC ui/FileBrowserFragment.java:388-389, 404-406, 425-428')
    e('FileBrowserFragment.openFile@' + v, 'FileBrowserFragment.upOneLevel@' + v, 'CALL', 'the ".." row: upOneLevel()', guard='the row is ".." (FileBrowserFragment.java:390-391)', evidence='SRC ui/FileBrowserFragment.java:390-391')
    e('FileBrowserFragment.upOneLevel@' + v, 'FileBrowserFragment.browseTo@' + v, 'CALL', 'upOneLevel browses to the parent folder (this host)', evidence='SRC ui/FileBrowserFragment.java:278 (bytecode)')
    if v == 'UPLOADDROPBOX':
        e('FileBrowserFragment.openFile@UPLOADDROPBOX', 'FileBrowserFragment.notifyFileClick', 'CALL', 'onFileClickListener is null (UploadDropboxActivity never calls setOnFileClickListener)', evidence='SRC ui/FileBrowserFragment.java:412,415')
    else:
        e('FileBrowserFragment.openFile@' + v, FB_TARGET[v], 'CALL', 'onFileClickListener.onFileBrowserFileClick(clickedFile)', guard=FB_ROW_IS_FILE, evidence='SRC ui/FileBrowserFragment.java:407-414 (bytecode)')
e('FileBrowserFragment.notifyFileClick', 'UploadDropboxActivity.onFileBrowserFileClick', 'CALL', 'getActivity() instanceof OnFileClickListener (UploadDropboxActivity implements it directly)',
  guard='getParentFragment() is not an OnFileClickListener (FileBrowserFragment.java:435; null on this activity host), and getActivity() is one (:437)', evidence='SRC ui/FileBrowserFragment.java:434-440 (bytecode)')

# ---- FileBrowserFragment lifecycle and file list (group 2, round 1). Two layers:
#  (a) BASE chain: host-neutral nodes. The base constructor is called by FileBrowserActivity.onCreate, SettingsScreen$10.onClick
#      and UploadDropboxActivity.onCreate (auto CALL). No base node reaches a host listener (the openFile listener edges are suppressed above).
#  (b) VARIANT chain per host (@X): the host entry, then onCreate@X, onCreateView@X, onResume@X, browseTo@X, fill@X, setItems@X,
#      onBindViewHolder@X, onClick@X and openFile@X. A route cannot pass from one host into another host's row click or listener.
# Rows exist only after setItems (FileBrowserFragment.java:594), so the row click is on onBindViewHolder, not on onCreateView.
FB_PAGES = {'S_MAIN_OPEN': 'OPEN', 'S_FILEBROWSER': 'FBACTIVITY', 'S_DLG_EXPORT_ANYMEMO': 'EXPORT',
            'S_DLG_CONVERTER': 'CONVERTER', 'S_DROPBOX_UPLOAD': 'UPLOADDROPBOX',
            'S_DLG_TYPEFACE_Q': 'SETTINGS_Q', 'S_DLG_TYPEFACE_A': 'SETTINGS_A'}
# (a) base chain
e('FileBrowserFragment.<init>', 'FileBrowserFragment.onAttach', 'LIFECYCLE', 'constructor then onAttach (Fragment lifecycle)', evidence=FW_FRAG + '; SRC ui/FileBrowserFragment.java:122-128')
e('FileBrowserFragment.onAttach', 'FileBrowserFragment.onCreate', 'LIFECYCLE', 'onAttach then onCreate', evidence=FW_FRAG + '; SRC ui/FileBrowserFragment.java:131-174')
e('FileBrowserFragment.onCreate', 'FileBrowserFragment.onCreateView', 'LIFECYCLE', 'onCreate then onCreateView', evidence=FW_FRAG + '; SRC ui/FileBrowserFragment.java:183-206')
e('FileBrowserFragment.onCreate', 'FileBrowserFragment.onCreateOptionsMenu', 'FRAMEWORK', 'the options menu is built after onCreate, which called setHasOptionsMenu(true)', guard=FB_MENU_GUARD, evidence=FW_FRAG + '; FW-SRC Fragment.java:940-946, 2626-2629; SRC ui/FileBrowserFragment.java:173')
e('FileBrowserFragment.onCreateView', 'FileBrowserFragment.onResume', 'LIFECYCLE', 'onCreateView then onResume', evidence=FW_FRAG + '; SRC ui/FileBrowserFragment.java:183-212')
e('FileBrowserFragment.onResume', 'FileBrowserFragment.browseTo', 'CALL', 'onResume() browses to the current/default directory', evidence='SRC ui/FileBrowserFragment.java:208-212')
e('FileBrowserFragment$FileBrowserAdapter.setItems', 'FileBrowserFragment$FileBrowserAdapter.onCreateViewHolder', 'FRAMEWORK', 'setItems calls notifyDataSetChanged: the recycler view creates the row holders', cls='non_standard', via='RecyclerView calls the adapter callbacks (androidx library, INFERRED)', evidence=FW_RECYCLER + '; SRC ui/FileBrowserFragment.java:594, 473')
e('FileBrowserFragment$FileBrowserAdapter.setItems', 'FileBrowserFragment$FileBrowserAdapter.onBindViewHolder', 'FRAMEWORK', 'setItems calls notifyDataSetChanged: the recycler view binds the rows', cls='non_standard', via='RecyclerView calls the adapter callbacks (androidx library, INFERRED)', evidence=FW_RECYCLER + '; SRC ui/FileBrowserFragment.java:594, 480')
e('FileBrowserFragment$FileBrowserAdapter.onBindViewHolder', 'FileBrowserFragment$FileBrowserAdapter$2.onLongClick', 'FRAMEWORK', 'long-press a file row (base copy)', gui=['Long-press a file'], needs_state=NEED_FB_ROW, evidence=FW_VIEW + '; SRC ui/FileBrowserFragment.java:521-586')
e('FileBrowserFragment$FileBrowserAdapter.onBindViewHolder', 'FileBrowserFragment$FileBrowserAdapter$1.onClick', 'FRAMEWORK', 'tap a file or folder row (base copy)', gui=['Tap a file or folder'], needs_state=NEED_FB_ROW, evidence=FW_VIEW + '; SRC ui/FileBrowserFragment.java:514-519')
# Base bytecode CALLs that add_auto_edges (tools/build_graph.py:223) drops. That rule skips an auto edge when ANY hand edge has the same
# base-name pair, so the host copies (browseTo@X -> fill@X, fill@X -> setItems@X, onCreate@X -> AMEnv.<clinit>, ...) silently removed the
# base edges. Without browseTo -> fill and fill -> setItems the base chain never reaches the sort comparator (build 7: UNRESOLVED).
# Restored by hand with the line numbers from auto_calls.json (round 1, group 2 fix). Base openFile reaches no host listener (sup above).
e('FileBrowserFragment.onCreate', 'AMEnv.<clinit>', 'CALL', 'static initializer of AMEnv (base copy)', evidence='SRC ui/FileBrowserFragment.java:164 (bytecode)')
e('FileBrowserFragment.onCreate', 'DaggerAppComponents$FragmentComponentsImpl.inject(FileBrowserFragment)', 'CALL', 'Direct call into the generated component injector (base copy)', evidence='SRC ui/FileBrowserFragment.java:133 (bytecode)')
e('FileBrowserFragment.onCreate', 'BaseDialogFragment.fragmentComponents', 'CALL', 'the base dialog fragment provides its components (base copy)', evidence='SRC ui/FileBrowserFragment.java:133 (bytecode)')
e('FileBrowserFragment.browseTo', 'FileBrowserFragment.fill', 'CALL', 'browseTo lists the folder (base copy)', evidence='SRC ui/FileBrowserFragment.java:228 (bytecode)')
e('FileBrowserFragment.fill', 'FileBrowserFragment$DISPLAYMODE.<clinit>', 'CALL', 'fill reads the display-mode enum (static initializer, base copy)', evidence='SRC ui/FileBrowserFragment.java:243 (bytecode)')
e('FileBrowserFragment.fill', 'FileBrowserFragment$FileBrowserAdapter.setItems', 'CALL', 'fill passes the file list to the adapter (base copy)', evidence='SRC ui/FileBrowserFragment.java:272 (bytecode)')
e('FileBrowserFragment.upOneLevel', 'FileBrowserFragment.browseTo', 'CALL', 'upOneLevel browses to the parent folder (base copy)', evidence='SRC ui/FileBrowserFragment.java:278 (bytecode)')
e('FileBrowserFragment.openFile', 'FileBrowserFragment$DISPLAYMODE.<clinit>', 'CALL', 'openFile reads the display-mode enum (static initializer, base copy)', evidence='SRC ui/FileBrowserFragment.java:394 (bytecode)')
e('FileBrowserFragment.openFile', 'FileBrowserFragment.upOneLevel', 'CALL', 'the ".." row: upOneLevel() (base copy)', evidence='SRC ui/FileBrowserFragment.java:391 (bytecode)')
e('FileBrowserFragment.openFile', 'FileBrowserFragment.browseTo', 'CALL', 'browse the folder for a folder row or "." (base copy)', evidence='SRC ui/FileBrowserFragment.java:428 (bytecode)')
e('FileBrowserFragment$FileBrowserAdapter$1.onClick', 'FileBrowserFragment.openFile', 'CALL', 'fragment.openFile(selectedFileName) (base copy)', evidence='SRC ui/FileBrowserFragment.java:517 (bytecode)')
# (b) one variant chain per host
for v in FB_PAGES.values():
    clone_auto('FileBrowserFragment.onCreate', 'FileBrowserFragment.onCreate@' + v)
    clone_auto('FileBrowserFragment.fill', 'FileBrowserFragment.fill@' + v, exclude={'FileBrowserFragment$FileBrowserAdapter.setItems'})
    e('FileBrowserFragment.onCreate@' + v, 'FileBrowserFragment.onCreateView@' + v, 'LIFECYCLE', 'onCreate then onCreateView (this host)', evidence=FW_FRAG + '; SRC ui/FileBrowserFragment.java:183-206')
    e('FileBrowserFragment.onCreate@' + v, 'FileBrowserFragment.onCreateOptionsMenu', 'FRAMEWORK', 'the options menu, reached from this host after its onCreate', guard=FB_MENU_GUARD, evidence=FW_FRAG + '; FW-SRC Fragment.java:940-946, 2626-2629; SRC ui/FileBrowserFragment.java:173')
    e('FileBrowserFragment.onCreateView@' + v, 'FileBrowserFragment$FileBrowserAdapter.getItemCount', 'FRAMEWORK', 'the recycler view asks for the row count on every layout pass (this host)', cls='non_standard', via='RecyclerView calls the adapter callbacks (androidx library, INFERRED)', evidence=FW_RECYCLER + '; SRC ui/FileBrowserFragment.java:590')
    e('FileBrowserFragment.onCreateView@' + v, 'FileBrowserFragment.onResume@' + v, 'LIFECYCLE', 'onCreateView then onResume (this host)', evidence=FW_FRAG + '; SRC ui/FileBrowserFragment.java:183-212')
    e('FileBrowserFragment.onResume@' + v, 'FileBrowserFragment.browseTo@' + v, 'CALL', 'onResume() browses to the current/default directory (this host)', evidence='SRC ui/FileBrowserFragment.java:208-212')
    e('FileBrowserFragment.browseTo@' + v, 'FileBrowserFragment.fill@' + v, 'CALL', 'browseTo lists the folder (this host)', evidence='SRC ui/FileBrowserFragment.java:222-233 (bytecode :228)')
    e('FileBrowserFragment.fill@' + v, 'FileBrowserFragment$FileBrowserAdapter.setItems@' + v, 'CALL', 'fill passes the file list to the adapter of this host', evidence='SRC ui/FileBrowserFragment.java:272 (bytecode)')
    e('FileBrowserFragment$FileBrowserAdapter.setItems@' + v, 'FileBrowserFragment$FileBrowserAdapter.onBindViewHolder@' + v, 'FRAMEWORK', 'the recycler view binds the rows (this host)', cls='non_standard', via='RecyclerView calls the adapter callbacks (androidx library, INFERRED)', evidence=FW_RECYCLER + '; SRC ui/FileBrowserFragment.java:594, 480')
    e('FileBrowserFragment$FileBrowserAdapter.setItems@' + v, 'FileBrowserFragment$FileBrowserAdapter.onCreateViewHolder', 'FRAMEWORK', 'the recycler view creates the row holders (shared copy)', cls='non_standard', via='RecyclerView calls the adapter callbacks (androidx library, INFERRED)', evidence=FW_RECYCLER + '; SRC ui/FileBrowserFragment.java:594, 473')
    e('FileBrowserFragment$FileBrowserAdapter.onBindViewHolder@' + v, 'FileBrowserFragment$FileBrowserAdapter$1.onClick@' + v, 'FRAMEWORK', 'tap a file or folder row (this host)', gui=['Tap a file or folder'], needs_state=NEED_FB_ROW, evidence=FW_VIEW + '; SRC ui/FileBrowserFragment.java:514-519')
    e('FileBrowserFragment$FileBrowserAdapter.onBindViewHolder@' + v, 'FileBrowserFragment$FileBrowserAdapter$2.onLongClick', 'FRAMEWORK', 'long-press a file row (this host reaches the shared long-press dialog)', gui=['Long-press a file'], needs_state=NEED_FB_ROW, evidence=FW_VIEW + '; SRC ui/FileBrowserFragment.java:521-586')
    e('FileBrowserFragment$FileBrowserAdapter$1.onClick@' + v, 'FileBrowserFragment.openFile@' + v, 'CALL', 'fragment.openFile(selectedFileName) (this host)', evidence='SRC ui/FileBrowserFragment.java:514-519')
# host entries. The page is entered from the host's onResume, after the file list is filled.
e('OpenTabFragment.onAttach', 'FileBrowserFragment.onCreate@OPEN', 'LIFECYCLE', 'onAttach (sets the listener) then onCreate of the Open-tab file browser', evidence=FW_FRAG + '; SRC ui/OpenTabFragment.java:34-39')
e('FileBrowserActivity.onCreate', 'FileBrowserFragment.onCreate@FBACTIVITY', 'LIFECYCLE', 'the activity commits the file browser fragment in onCreate (listener at :52)', evidence='SRC ui/FileBrowserActivity.java:46-52')
e('ExportAnyMemoDbFragment.onCreate', 'FileBrowserFragment.onCreate@EXPORT', 'CALL', 'super.onCreate() of the export picker', evidence='SRC ui/ExportAnyMemoDbFragment.java:34')
e('ConverterFragment.onCreate', 'FileBrowserFragment.onCreate@CONVERTER', 'CALL', 'super.onCreate() of the converter picker', evidence='SRC ui/ConverterFragment.java:61-62')
e('UploadDropboxActivity.onCreate', 'FileBrowserFragment.onCreate@UPLOADDROPBOX', 'LIFECYCLE', 'the activity commits the file browser fragment in onCreate (new FileBrowserFragment at :55)', evidence='SRC downloader/dropbox/UploadDropboxActivity.java:55-59')
e('SettingsScreen$10.onClick', 'FileBrowserFragment.onCreate@SETTINGS_Q', 'LIFECYCLE', 'v == qTypefaceEdit: df.show() of the question-typeface picker runs its lifecycle', guard='v == qTypefaceEdit (SettingsScreen.java:712-721)', evidence='SRC ui/SettingsScreen.java:712-721')
e('SettingsScreen$10.onClick', 'FileBrowserFragment.onCreate@SETTINGS_A', 'LIFECYCLE', 'v == aTypefaceEdit: df.show() of the answer-typeface picker runs its lifecycle', guard='v == aTypefaceEdit (SettingsScreen.java:723-732)', evidence='SRC ui/SettingsScreen.java:723-732')
e('FileBrowserFragment.onResume@OPEN', 'S_MAIN_OPEN', 'ENTERS', 'the Open tab is shown with its file list (onResume browses to the folder)', evidence='SRC ui/AnyMemo.java:242-246,253-257; ui/FileBrowserFragment.java:208-212')
e('FileBrowserFragment.onResume@EXPORT', 'S_DLG_EXPORT_ANYMEMO', 'ENTERS', 'the export picker is shown (df.show) with its file list', needs_state=NEED_EXPORT_SECTION, evidence='SRC ui/MiscTabFragment.java:253-256; ui/ExportAnyMemoDbFragment.java:33-41')
e('FileBrowserFragment.onResume@CONVERTER', 'S_DLG_CONVERTER', 'ENTERS', 'the converter picker is shown (df.show) with its file list', needs_state=NEED_EXPORT_SECTION, evidence='SRC ui/MiscTabFragment.java:290-337; ui/ConverterFragment.java:59-70')
for page in FB_PAGES:
    e(page, 'FileBrowserFragment.onDestroy', 'LIFECYCLE', 'Fragment onDestroy when the page is left (page-sourced; the only lifecycle edge kept from the page)', evidence=FW_FRAG + '; SRC ui/FileBrowserFragment.java:122-322')
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
e('FileBrowserFragment.onCreateView@OPEN', 'FileBrowserFragment$7.onClick', 'FRAMEWORK', 'tap the create-db FAB (only shown with EXTRA_SHOW_CREATE_DB_BUTTON, i.e. the Open tab)',
  gui=['Tap the create-database FAB on the Open tab'], evidence=FW_VIEW + '; SRC ui/FileBrowserFragment.java:196-200,447-461')
e('FileBrowserFragment$7.onClick', 'S_DLG_CREATE_DB', 'ENTERS', 'showCreateDbDialog(AMEnv.DEFAULT_ROOT_PATH)', evidence='SRC ui/FileBrowserFragment.java:451-460')
gui('S_DLG_CREATE_DB', 'FileBrowserFragment$7$1.accept', 'Type a name and tap OK (FAB variant)', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:453-458')
e('FileBrowserFragment$7$1.accept', 'FileBrowserFragment.refreshFileList', 'CALL', 'refreshFileList(file.getAbsoluteFile().getParentFile())', evidence='SRC ui/FileBrowserFragment.java:456-457')

# ---- OpenTabFragment (the Open tab = a FileBrowserFragment rooted at the AnyMemo folder) + OpenActionsFragment
e('OpenTabFragment.<init>', 'OpenTabFragment.onAttach', 'LIFECYCLE', 'constructor then onAttach (sets the file-click listener); the Open tab is constructed by AnyMemo.java:242-246', evidence=FW_FRAG + '; SRC ui/OpenTabFragment.java:34-39')
e('OpenTabFragment.onAttach', 'FileBrowserFragment.setOnFileClickListener', 'CALL', 'setOnFileClickListener(fileClickListener)', evidence='SRC ui/OpenTabFragment.java:38')
e('OpenTabFragment$1.onFileBrowserFileClick', 'OpenActionsFragment.<init>', 'CALL', 'a new OpenActionsFragment is created for the tapped .db', evidence='SRC ui/OpenTabFragment.java:43-47')


# ================================================================== E. study/quiz
e('OpenActionsFragment$1.onClick', 'StudyActivity.<init>', 'INTENT', 'v == studyItem: startActivity(StudyActivity)', evidence='SRC ui/OpenActionsFragment.java:121-127')
e('RecentListFragment$RecentListAdapter$1.onClick', 'StudyActivity.<init>', 'INTENT', 'tap a recent-deck row: startActivity(StudyActivity) for the tapped deck',
  guard='getSelectedItemCount() == 0 (RecentListFragment.java:416); with a selection the tap toggles it instead (:423-424)', evidence='SRC ui/RecentListFragment.java:416-422')
e('AnyMemoWidgetProvider.onUpdate', 'StudyActivity.<init>', 'INTENT', 'tap a widget row (RemoteViews PendingIntentTemplate + the row\'s fill-in intent)', env=ENV_WIDGET, evidence='SRC widget/AnyMemoWidgetProvider.java:66-77; widget/WidgetRemoteViewsFactory.java:89-91')
for cb, lsrc in lc_chain('StudyActivity', ('onCreate', 'onSaveInstanceState', 'onCreateOptionsMenu', 'onOptionsItemSelected', 'onCreateContextMenu', 'onDestroy', 'onResume')):
    e(lsrc, 'StudyActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/StudyActivity.java:103-257')
e('StudyActivity.onCreate', 'StudyActivity$LearnQueueManagerLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'getMultipleLoaderManager().registerLoaderCallbacks(...); startInit() starts loading', evidence=FW_LOADER + '; SRC ui/StudyActivity.java:119-121,428-437')
e('StudyActivity$LearnQueueManagerLoaderCallbacks.onCreateLoader', 'StudyActivity$LearnQueueManagerLoader.dbLoadInBackground', 'ASYNC', 'loader.forceLoad()', evidence=FW_LOADER + '; SRC ui/StudyActivity.java:429-436; ui/loader/DBLoader.java:41-50')
e('StudyActivity$LearnQueueManagerLoader.dbLoadInBackground', 'StudyActivity$LearnQueueManagerLoaderCallbacks.onLoadFinished', 'ASYNC', 'the built LearnQueueManager is delivered on the main thread', evidence=FW_LOADER + '; SRC ui/StudyActivity.java:440-443')
# Study's onLoadFinished calls checkAllLoadersCompleted (StudyActivity.java:442); onPostInit runs from the stored runnable (QACardActivity$2.run).
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
e('StudyActivity.onOptionsItemSelected', 'DetailScreen.<init>', 'ENTRY', 'menudetail: startActivityForResult(DetailScreen)', guard='itemId == menudetail (StudyActivity.java:157-159)', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:157-159,712-717')
e('StudyActivity.onOptionsItemSelected', 'StudyActivity.undoCard', 'CALL', 'menuundo', evidence='SRC ui/StudyActivity.java:160-162,549-573')
e('StudyActivity.undoCard', 'S_DLG_UNDO_FAIL', 'ENTERS', 'no previous card to undo: the nothing-to-undo dialog (undo_fail_text) is shown', guard='prevCard == null', evidence='SRC ui/StudyActivity.java:565-573')
e('StudyActivity.undoCard', 'S_STUDY', 'ENTERS', 'restartActivity() re-displays the restored previous card', needs_state=state_text('a grade was given to at least one card before in this process (prevCard != null)', ('session',)), evidence='SRC ui/StudyActivity.java:549-564')
e('StudyActivity.onOptionsItemSelected', 'S_DLG_CATEGORY_STUDY', 'ENTERS', 'menu_memo_category: showCategoriesDialog()', evidence='SRC ui/StudyActivity.java:163-165,515-530')
e('StudyActivity.onOptionsItemSelected', 'S_CARD_EDITOR', 'ENTERS', 'menu_context_edit: startActivityForResult(CardEditor)', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:166-168,662-668')
e('StudyActivity.onOptionsItemSelected', 'S_DLG_DELETE_CARD', 'ENTERS', 'menu_context_delete', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:169-171,670-686')
gui('S_DLG_DELETE_CARD', 'StudyActivity$5.onClick', 'Tap OK (confirm delete)', evidence=FW_DIALOGFRAG + '; SRC ui/StudyActivity.java:674-683')
e('StudyActivity$5.onClick', 'S_STUDY', 'ENTERS', 'the card is deleted and restartActivity() dequeues the next one', evidence='SRC ui/StudyActivity.java:676-681')
e('StudyActivity.onOptionsItemSelected', 'S_DLG_MARK_LEARNED', 'ENTERS', 'menu_mark_as_learned_forever', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:172-174,688-699')
gui('S_DLG_MARK_LEARNED', 'StudyActivity$6.onClick', 'Tap OK (confirm)', evidence=FW_DIALOGFRAG + '; SRC ui/StudyActivity.java:692-697')
e('StudyActivity$6.onClick', 'StudyActivity.markCurrentCardAsLearnedForever', 'CALL', 'markCurrentCardAsLearnedForever()', evidence='SRC ui/StudyActivity.java:693')
e('StudyActivity.markCurrentCardAsLearnedForever', 'S_STUDY', 'ENTERS', 'restartActivity()', evidence='SRC ui/StudyActivity.java:634-643')
# Round 1b B8: menu_context_gotoprev starts PreviewEditActivity (gotoPreviewEdit, StudyActivity.java:701-710)
e('StudyActivity.onOptionsItemSelected', 'PreviewEditActivity.<init>', 'ENTRY', 'menu_context_gotoprev: startActivity(PreviewEditActivity) via gotoPreviewEdit()', guard='itemId == menu_context_gotoprev (StudyActivity.java:175-177)', evidence='SRC ui/StudyActivity.java:175-177,701-710')
e('StudyActivity.onOptionsItemSelected', 'DictionaryUtil.showLookupListDialog', 'CALL', 'menu_context_lookup', guard='getCurrentCard() != null', evidence='SRC ui/StudyActivity.java:178-184,658-660')
e('DictionaryUtil.showLookupListDialog', 'S_EXT_DICT', 'ENTERS', 'tap a word: the lookup intent is sent to the configured dictionary app', gui=['Tap a word in the lookup list'], env=ENV_EXT_DICT, evidence='SRC utils/DictionaryUtil.java:102-113,115-159')
e('StudyActivity.onOptionsItemSelected', 'StudyActivity.showGesturesDialog', 'CALL', 'menu_gestures', evidence='SRC ui/StudyActivity.java:185-187,645-656')
e('StudyActivity.showGesturesDialog', 'S_DLG_GESTURE', 'ENTERS', 'df.show(...)', evidence='SRC ui/StudyActivity.java:651-655')
e('StudyActivity.onOptionsItemSelected', 'ShareUtil.shareCard', 'CALL', 'menu_share', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:188-191')
e('ShareUtil.shareCard', 'S_EXT_PICKER', 'ENTERS', 'Intent.createChooser(ACTION_SEND text/plain) shows the system share sheet', env=ENV_PICKER, evidence='SRC utils/ShareUtil.java:38-44')
e('S_STUDY', 'StudyActivity.onCreateContextMenu', 'FRAMEWORK', 'long-press the card area', gui=['Long-press the card'], evidence=FW_MENU + '; SRC ui/StudyActivity.java:196-202')
e('StudyActivity.onActivityResult', 'S_STUDY', 'ENTERS', 'restartActivity() for every request code except RESULT_CANCELED', evidence='SRC ui/StudyActivity.java:204-244,259-271')
e('StudyActivity.showCategoriesDialog', 'S_DLG_CATEGORY_STUDY', 'ENTERS', 'df.show(...)', evidence='SRC ui/StudyActivity.java:515-529')
e('S_DLG_CATEGORY_STUDY', 'StudyActivity$3.onReceiveCategory', 'CALL', 'a category is picked (CategoryEditorFragment ok button)', evidence='SRC ui/StudyActivity.java:576-586; ui/CategoryEditorFragment.java:94-109')
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
# Round 1b C11: onPostDisplayCard sets the grade buttons three ways (StudyActivity.java:306-313); the automatic edge is replaced by these three
e('StudyActivity.onPostDisplayCard', 'GradeButtonsFragment.setVisibility', 'CALL', 'setVisibility(VISIBLE): the answer is shown', guard='isAnswerShown() is true (StudyActivity.java:306-307)', evidence='SRC ui/StudyActivity.java:306-313')
e('StudyActivity.onPostDisplayCard', 'GradeButtonsFragment.setVisibility', 'CALL', 'setVisibility(GONE): the answer is hidden on a double sided card', guard='answer not shown and DOUBLE_SIDED (StudyActivity.java:310-311)', evidence='SRC ui/StudyActivity.java:306-313')
e('StudyActivity.onPostDisplayCard', 'GradeButtonsFragment.setVisibility', 'CALL', 'setVisibility(INVISIBLE): the answer is hidden on a single sided card', guard='answer not shown and not DOUBLE_SIDED (StudyActivity.java:312-313)', evidence='SRC ui/StudyActivity.java:306-313')

# ---- QuizActivity (reached via the quiz launcher dialog, see below)
for cb, lsrc in lc_chain('QuizActivity', ('onCreate', 'onSaveInstanceState', 'onCreateOptionsMenu', 'onOptionsItemSelected')):
    e(lsrc, 'QuizActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/QuizActivity.java:86-164')
e('QuizActivity.onCreate', 'QuizActivity$QuizQueueManagerLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'getMultipleLoaderManager().registerLoaderCallbacks(...); startInit() starts loading', evidence=FW_LOADER + '; SRC ui/QuizActivity.java:131,133')
e('QuizActivity$QuizQueueManagerLoaderCallbacks.onCreateLoader', 'QuizActivity$QuizQueueManagerLoader.dbLoadInBackground', 'ASYNC', 'loader.forceLoad()', evidence=FW_LOADER + '; SRC ui/QuizActivity.java:290-294; ui/loader/DBLoader.java:41-50')
e('QuizActivity$QuizQueueManagerLoader.dbLoadInBackground', 'QuizActivity$QuizQueueManagerLoaderCallbacks.onLoadFinished', 'ASYNC', 'the built QuizQueueManager is delivered on the main thread', evidence=FW_LOADER + '; SRC ui/QuizActivity.java:297-300')
# Quiz's onLoadFinished calls checkAllLoadersCompleted (QuizActivity.java:300); onPostInit runs from the stored runnable (QACardActivity$2.run).
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
for cb, lsrc in lc_chain('QuizLauncherDialogFragment', ('onCreate', 'onAttach', 'onCreateDialog', 'onStart', 'onDestroy')):
    e(lsrc, 'QuizLauncherDialogFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/QuizLauncherDialogFragment.java:120-213')
e('QuizLauncherDialogFragment.onStart', 'QuizLauncherDialogFragment$InitTask.doInBackground', 'ASYNC', 'new InitTask().execute()', evidence=FW_ASYNC + '; SRC ui/QuizLauncherDialogFragment.java:210-212')
e('QuizLauncherDialogFragment$InitTask.doInBackground', 'QuizLauncherDialogFragment$InitTask.onPostExecute', 'ASYNC', 'the card count is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/QuizLauncherDialogFragment.java:293-310')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$1.onCheckedChanged', 'Tap a quiz-mode radio button (Group / Category / Range)', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:152-154,215-228')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$2.onClick', 'Tap "Start quiz"', evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:148-150,231-268')
# Start button: three branches (QuizLauncherDialogFragment.java:234-266), one edge per branch. The category branch
# uses categoryId, which is 0 until a category is picked (set at line 524). The range branch needs quizByRangeRadio.
QZ_CAT_STATE = state_text('a category was picked in this launcher (categoryId is set at QuizLauncherDialogFragment.java:524)', ('session',))
QZ_RANGE_STATE = state_text('quizByRangeRadio is checked', ('session',))
e('QuizLauncherDialogFragment$2.onClick', 'QuizActivity.<init>', 'ENTRY', 'startActivity(QuizActivity) with the category id (category mode)', guard='quizByCategoryRadio is checked', needs_state=QZ_CAT_STATE, evidence='SRC ui/QuizLauncherDialogFragment.java:234-239')
e('QuizLauncherDialogFragment$2.onClick', 'QuizActivity.<init>', 'ENTRY', 'startActivity(QuizActivity) with the start and end ordinals (range mode; both fields must hold numbers, parseInt at 242-243)', guard='quizByCategoryRadio is not checked and quizByRangeRadio is checked', needs_state=QZ_RANGE_STATE, evidence='SRC ui/QuizLauncherDialogFragment.java:240-254')
e('QuizLauncherDialogFragment$2.onClick', 'QuizActivity.<init>', 'ENTRY', 'startActivity(QuizActivity) for group mode (the else branch)', guard='quizByCategoryRadio and quizByRangeRadio are both not checked', evidence='SRC ui/QuizLauncherDialogFragment.java:255-265')
e('QuizLauncherDialogFragment$2.onClick', 'S_QUIZ', 'ENTERS', 'startActivity(QuizActivity) with the category id (category mode)', guard='quizByCategoryRadio is checked', needs_state=QZ_CAT_STATE, evidence='SRC ui/QuizLauncherDialogFragment.java:234-239')
e('QuizLauncherDialogFragment$2.onClick', 'S_QUIZ', 'ENTERS', 'startActivity(QuizActivity) with the start and end ordinals (range mode)', guard='quizByCategoryRadio is not checked and quizByRangeRadio is checked', needs_state=QZ_RANGE_STATE, evidence='SRC ui/QuizLauncherDialogFragment.java:240-254')
e('QuizLauncherDialogFragment$2.onClick', 'S_QUIZ', 'ENTERS', 'startActivity(QuizActivity) for group mode (the else branch)', guard='quizByCategoryRadio and quizByRangeRadio are both not checked', evidence='SRC ui/QuizLauncherDialogFragment.java:255-265')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$3.onClick', 'Tap the category button (Category mode)', needs_state=state_text('quizByCategoryRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:190-191,270-275')
e('QuizLauncherDialogFragment$3.onClick', 'QuizLauncherDialogFragment.showCategoriesDialog', 'CALL', 'showCategoriesDialog()', evidence='SRC ui/QuizLauncherDialogFragment.java:272-274')
# Round 1b B4: the picker is entered from CategoryEditorFragment.onCreateView (the construction CALL and the onAttach/onCreate chain already exist as automatic edges)
e('CategoryEditorFragment.onCreateView', 'S_DLG_CATEGORY_QUIZ', 'ENTERS', 'df.show(...) in showCategoriesDialog: the category picker is shown with the view built in onCreateView', needs_state=NEED_CATEGORY, evidence='SRC ui/CategoryEditorFragment.java:72-86; ui/QuizLauncherDialogFragment.java:508-516')
# Round 1b B4: the category result is sent by the OK button handler (CategoryEditorFragment.java:96-107), not by the screen node
e('CategoryEditorFragment$1.onClick', 'QuizLauncherDialogFragment$10.onReceiveCategory', 'CALL', 'a category is picked: OK tapped, resultListener.onReceiveCategory(selectedCategory)', guard='v == okButton (CategoryEditorFragment.java:96)', needs_state=NEED_CATEGORY, evidence='SRC ui/QuizLauncherDialogFragment.java:520-531; ui/CategoryEditorFragment.java:94-109')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$4.afterTextChanged', 'Type a group size', needs_state=state_text('quizByGroupRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:169,342-373')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$5.afterTextChanged', 'Type a group number', needs_state=state_text('quizByGroupRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:175,376-405')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$6.afterTextChanged', 'Type a range start ordinal', needs_state=state_text('quizByRangeRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:183,407-441')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$7.afterTextChanged', 'Type a range end ordinal', needs_state=state_text('quizByRangeRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:187,444-482')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$8.onFocusChange', 'Leave the group-size/number field (focus lost)', needs_state=state_text('quizByGroupRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:170,176,496-506')
gui('S_DLG_QUIZ_LAUNCHER', 'QuizLauncherDialogFragment$9.onFocusChange', 'Leave the range-start/end field (focus lost)', needs_state=state_text('quizByRangeRadio is checked', ('session',)), evidence=FW_VIEW + '; SRC ui/QuizLauncherDialogFragment.java:184,188,484-494')

# ---- GestureSelectionDialogFragment (shown from Study and Preview/Edit)
for cb, lsrc in lc_chain('GestureSelectionDialogFragment', ('onAttach', 'onCreate', 'onCreateView')):
    e(lsrc, 'GestureSelectionDialogFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/GestureSelectionDialogFragment.java:76-133')
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
e('StudyActivity.showEditDialog', 'CardEditor.<init>', 'ENTRY', 'startActivityForResult(CardEditor): getCurrentCard().getId() needs an open card', needs_state=NEED_CARD, evidence='SRC ui/StudyActivity.java:662-668')
for cb, lsrc in lc_chain('CardEditor', ('onCreate', 'onDestroy', 'onCreateOptionsMenu', 'onOptionsItemSelected', 'onConfigurationChanged')):
    e(lsrc, 'CardEditor.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/CardEditor.java:101-419')
e('CardEditor.onCreate', 'CardEditor$InitTask.doInBackground', 'ASYNC', 'new InitTask().execute()', evidence=FW_ASYNC + '; SRC ui/CardEditor.java:105-106')
e('CardEditor$InitTask.doInBackground', 'CardEditor$InitTask.onPostExecute', 'ASYNC', 'the card/category/learning-data are delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CardEditor.java:512-560')
e('CardEditor$InitTask.onPostExecute', 'S_CARD_EDITOR', 'ENTERS', 'the editor fields are populated and shown', evidence='SRC ui/CardEditor.java:544-559')
e('S_CARD_EDITOR', 'CardEditor.onCreateOptionsMenu', 'FRAMEWORK', 'the toolbar menu is inflated (card_editor_menu)', evidence=FW_MENU + '; SRC ui/CardEditor.java:162-166')
e('S_CARD_EDITOR', 'CardEditor.onOptionsItemSelected', 'FRAMEWORK', 'tap a CardEditor toolbar/overflow menu item', gui=['Tap a menu item in the card editor'], evidence=FW_MENU + '; SRC ui/CardEditor.java:168-204')
# group 6: the image-picker RESULT edge is in block E2 (it returns to CardEditor.onActivityResult).
e('CardEditor.onOptionsItemSelected', 'S_FILEBROWSER', 'ENTERS', 'editor_menu_image: startActivityForResult(FileBrowserActivity, image extensions)', env=ENV_FB_STORAGE,
  guard='the focused field is question/answer/note', evidence='SRC ui/CardEditor.java:180-186')
e('CardEditor.onOptionsItemSelected', 'CardEditor.addExistingAudio', 'CALL', 'add_existing_audio', guard='the focused field is question/answer', evidence='SRC ui/CardEditor.java:187-191')
e('CardEditor.onOptionsItemSelected', 'CardEditor.addNewAudio', 'CALL', 'add_new_audio', guard='the focused field is the question or answer edit (CardEditor.java:192-194, 224-231)', evidence='SRC ui/CardEditor.java:192-196')
e('CardEditor.onOptionsItemSelected', 'CardEditor.removeAudio', 'CALL', 'remove_audio', guard='the focused field is question/answer', evidence='SRC ui/CardEditor.java:197-201')
e('CardEditor.addExistingAudio', 'S_DLG_AUDIO_OVERRIDE', 'ENTERS', 'the focused field already has an <audio src=...> tag', guard='the focused field already contains src= (CardEditor.java:250)', needs_state=NEED_PASSWORD_AUDIO, evidence='SRC ui/CardEditor.java:249-261')
gui('S_DLG_AUDIO_OVERRIDE', 'CardEditor$3.onClick', 'Tap Yes (existing audio -> browse)', needs_state=NEED_PASSWORD_AUDIO, evidence=FW_DIALOGFRAG + '; SRC ui/CardEditor.java:252-257')
e('CardEditor$3.onClick', 'CardEditor.startAudioBrowser', 'CALL', 'startAudioBrowser()', evidence='SRC ui/CardEditor.java:254')
e('CardEditor.addExistingAudio', 'CardEditor.startAudioBrowser', 'CALL', 'the focused field has no audio tag yet', guard='the focused field does not contain src= (CardEditor.java:250, 258-260)', evidence='SRC ui/CardEditor.java:258-260')
e('CardEditor.startAudioBrowser', 'S_FILEBROWSER', 'ENTERS', 'startActivityForResult(FileBrowserActivity, audio extensions)', env=ENV_FB_STORAGE, evidence='SRC ui/CardEditor.java:290-295')
e('CardEditor.addNewAudio', 'S_DLG_AUDIO_OVERRIDE', 'ENTERS', 'the focused field already has an <audio src=...> tag', guard='the focused field already contains src= (CardEditor.java:264)', needs_state=NEED_PASSWORD_AUDIO, evidence='SRC ui/CardEditor.java:263-275')
gui('S_DLG_AUDIO_OVERRIDE', 'CardEditor$4.onClick', 'Tap Yes (existing audio -> record new)', needs_state=NEED_PASSWORD_AUDIO, evidence=FW_DIALOGFRAG + '; SRC ui/CardEditor.java:266-271')
e('CardEditor$4.onClick', 'CardEditor.startAudioRecorderWithPermissionCheck', 'CALL', 'startAudioRecorderWithPermissionCheck()', evidence='SRC ui/CardEditor.java:268')
e('CardEditor.addNewAudio', 'CardEditor.startAudioRecorderWithPermissionCheck', 'CALL', 'the focused field has no audio tag yet', guard='the focused field does not contain src= (audioPreviouslyExists() is false, CardEditor.java:243-247, 264, 272-273)', evidence='SRC ui/CardEditor.java:243-247,264,272-274')
e('CardEditor.startAudioRecorderWithPermissionCheck', 'CardEditor.startAudioRecorder', 'CALL', 'RECORD_AUDIO is already granted', env=ENV_MIC, evidence='SRC ui/CardEditor.java:299-306')
e('CardEditor.startAudioRecorderWithPermissionCheck', 'CardEditor.onRequestPermissionsResult', 'FRAMEWORK', 'RECORD_AUDIO is requested; the system calls onRequestPermissionsResult once the user answers',
  evidence='INFERRED core/java/android/app/Activity.java requestPermissions forwards to the PackageManager and the result returns through onRequestPermissionsResult (platform source not read for this exact callback path); SRC ui/CardEditor.java:299-306,207-222')
e('CardEditor.onRequestPermissionsResult', 'CardEditor.startAudioRecorder', 'CALL', 'the user granted RECORD_AUDIO', env=ENV_MIC, evidence='SRC ui/CardEditor.java:207-222')
e('CardEditor.startAudioRecorder', 'AudioRecorderFragment.<init>', 'CALL', 'a new AudioRecorderFragment is added (commitAllowingStateLoss)', evidence='SRC ui/CardEditor.java:313-338')
e('CardEditor.startAudioRecorder', 'S_DLG_AUDIO_RECORDER', 'ENTERS', 'the recorder dialog is added', guard='the focused field is question or answer (CardEditor.java:315-321)', evidence='SRC ui/CardEditor.java:336-338')
e('AudioRecorderFragment.setAudioRecorderResultListener', 'CardEditor$5.onReceiveAudio', 'REGISTER', 'the listener passed by CardEditor.startAudioRecorder is stored', evidence='SRC ui/CardEditor.java:325-334')
e('CardEditor.onOptionsItemSelected', 'CardEditor.setInitRadioButton', 'CALL', 'save: SaveCardTask.execute()', evidence='SRC ui/CardEditor.java:171-174')
for cb in ('onAttach', 'onCreate', 'onCreateDialog'):
    e('S_DLG_AUDIO_RECORDER', 'AudioRecorderFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/AudioRecorderFragment.java:83-118')
e('S_DLG_AUDIO_RECORDER', 'AudioRecorderFragment$1.onClick', 'FRAMEWORK', 'tap Record / Play / Save', gui=['Tap Record, Play or Save'], evidence=FW_VIEW + '; SRC ui/AudioRecorderFragment.java:44-81,99-108')
e('AudioRecorderFragment$1.onClick', 'AudioRecorderFragment.onRecord', 'CALL', 'v == mRecordButton', env=ENV_MIC, evidence='SRC ui/AudioRecorderFragment.java:46-60')
e('AudioRecorderFragment.onRecord', 'AudioRecorderFragment.startRecording', 'CALL', 'mStartRecording toggled on', guard='start is true (Record was tapped to start; AudioRecorderFragment.java:125-127)', env=ENV_MIC, evidence='SRC ui/AudioRecorderFragment.java:125-131,168-182')
e('AudioRecorderFragment$1.onClick', 'AudioRecorderFragment.onPlay', 'CALL', 'v == mPlayButton', needs_state=NEED_AUDIO_RECORDED, evidence='SRC ui/AudioRecorderFragment.java:61-73')
e('AudioRecorderFragment.onPlay', 'AudioRecorderFragment.startPlaying', 'CALL', 'mStartPlaying toggled on', guard='start is true (Play was tapped to start; AudioRecorderFragment.java:134-135)', needs_state=NEED_AUDIO_RECORDED, evidence='SRC ui/AudioRecorderFragment.java:133-139,141-161')
e('AudioRecorderFragment.startPlaying', 'AudioRecorderFragment$2.onCompletion', 'FRAMEWORK', 'the recorded clip finishes playing', guard='the file prepares and starts without an IOException (AudioRecorderFragment.java:154-157)', evidence=FW_MEDIAPLAYER + '; SRC ui/AudioRecorderFragment.java:143-153')
e('AudioRecorderFragment$1.onClick', 'CardEditor$5.onReceiveAudio', 'CALL', 'v == mSaveButton: audioRecorderResultListener.onReceiveAudio()', needs_state=NEED_AUDIO_RECORDED, evidence='SRC ui/AudioRecorderFragment.java:75-77')
e('CardEditor$5.onReceiveAudio', 'CardEditor.addTextToView', 'CALL', 'the <audio src=...> tag is inserted at the cursor', evidence='SRC ui/CardEditor.java:326-333')
e('CardEditor.setInitRadioButton', 'CardEditor$6.onCheckedChanged', 'FRAMEWORK', 'toggle Add back / Add here (new-card radio group, only shown for a new card)', gui=['Toggle the Add-back / Add-here radio'],
  needs_state=state_text('isEditNew is true (adding a new card, not editing an existing one)', ('data',)), evidence=FW_VIEW + '; SRC ui/CardEditor.java:421-458')
e('CardEditor$InitTask.onPostExecute', 'CardEditor$7.onClick', 'FRAMEWORK', 'tap the category button', gui=['Tap the category button'], evidence=FW_VIEW + '; SRC ui/CardEditor.java:553,563-574')
e('CardEditor$7.onClick', 'CategoryEditorFragment.<init>', 'CALL', 'a new CategoryEditorFragment is shown', evidence='SRC ui/CardEditor.java:566-572')
e('CardEditor$7.onClick', 'S_DLG_CATEGORY_CARD', 'ENTERS', 'df.show(...)', evidence='SRC ui/CardEditor.java:572')
e('S_DLG_CATEGORY_CARD', 'CardEditor$8.onReceiveCategory', 'CALL', 'a category is picked', guard='the OK button is tapped (CategoryEditorFragment.java:96); resultListener != null, set by CardEditor$7.onClick (CardEditor.java:567) before show (:572); the category is null when no row is checked (CategoryEditorFragment.java:100-101)', evidence='SRC ui/CardEditor.java:634-639; ui/CategoryEditorFragment.java:94-109')
e('CardEditor$8.onReceiveCategory', 'CardEditor.updateCategoryView', 'CALL', 'updateCategoryView()', evidence='SRC ui/CardEditor.java:637')
e('CardEditor.onBackPressed', 'S_DLG_EDIT_DISCARD', 'ENTERS', 'the fields changed and this is not a new card', guard='!isEditNew && fields changed (CardEditor.java:131)', evidence='SRC ui/CardEditor.java:127-159')
gui('S_DLG_EDIT_DISCARD', 'CardEditor$2.onClick', 'Tap Yes (save before leaving)', guard='!isEditNew && fields changed', evidence=FW_DIALOGFRAG + '; SRC ui/CardEditor.java:135-140')
gui('S_DLG_EDIT_DISCARD', 'CardEditor$1.onClick', 'Tap No (discard)', evidence=FW_DIALOGFRAG + '; SRC ui/CardEditor.java:141-147')
e('CardEditor$1.onClick', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_CANCELED); finish() (reuses the caller\'s page: Study or Preview/Edit)', evidence='SRC ui/CardEditor.java:143-146')
e('S_CARD_EDITOR', 'CardEditor.onBackPressed', 'SYSTEM', 'press Back in the card editor', gui=['Press Back in the card editor'], env=ENV_HW_KEY, evidence=FW_ACTIVITY + '; SRC ui/CardEditor.java:127-131')
e('CardEditor.onBackPressed', 'S_PREVIEW_EDIT', 'ENTERS', 'isEditNew, or nothing changed: setResult(RESULT_CANCELED); finish()', guard='isEditNew, or the fields did not change (CardEditor.java:131)',
  needs_state=state_text('CardEditor was started from Preview/Edit (PreviewEditActivity newButtonListener or editButtonListener onClick, PreviewEditActivity.java:608-625) in this process', ('session',)), evidence='SRC ui/CardEditor.java:153-158')
e('CardEditor.onBackPressed', 'S_STUDY', 'ENTERS', 'isEditNew, or nothing changed: setResult(RESULT_CANCELED); finish() (the Study caller restarts in StudyActivity.onActivityResult)', guard='isEditNew, or the fields did not change (CardEditor.java:131)',
  needs_state=state_text('CardEditor was started from Study (StudyActivity.showEditDialog, StudyActivity.java:662-667) in this process', ('session',)), evidence='SRC ui/CardEditor.java:153-158')
e('CardEditor.onBackPressed', 'S_CARD_LIST', 'ENTERS', 'isEditNew, or nothing changed: setResult(RESULT_CANCELED); finish() (back to the card list)', guard='isEditNew, or the fields did not change (CardEditor.java:131)',
  needs_state=state_text('CardEditor was started from the card list row popup (CardListActivity.gotoCardEditorActivity, startActivity, CardListActivity.java:236-241) in this process', ('session',)), evidence='SRC ui/CardEditor.java:153-158; SRC ui/CardListActivity.java:236-241')
e('CardEditor$SaveCardTask.doInBackground', 'CardEditor$SaveCardTask.onPostExecute', 'ASYNC', 'the saved card is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CardEditor.java:623-630')
e('CardEditor$SaveCardTask.onPostExecute', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_OK); finish() (reuses the caller\'s page: Study or Preview/Edit)', evidence='SRC ui/CardEditor.java:624-629')
e('CardEditor$2.onClick', 'CardEditor$SaveCardTask.doInBackground', 'ASYNC', 'new SaveCardTask().execute()', evidence=FW_ASYNC + '; SRC ui/CardEditor.java:137-139')

# ---- CategoryEditorFragment (shown from Study / Quiz launcher / Preview-Edit / CardEditor)
for cb, lsrc in lc_chain('CategoryEditorFragment', ('onAttach', 'onCreate', 'onCreateView', 'onDestroy')):
    e(lsrc, 'CategoryEditorFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/CategoryEditorFragment.java:50-92')
e('CategoryEditorFragment.onCreateView', 'CategoryEditorFragment$InitTask.doInBackground', 'ASYNC', 'new InitTask().execute()', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:77-78')
e('CategoryEditorFragment$InitTask.doInBackground', 'CategoryEditorFragment$InitTask.onPostExecute', 'ASYNC', 'the category list is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:152-172')
e('CategoryEditorFragment$InitTask.onPostExecute', 'CategoryEditorFragment.enableListeners', 'CALL', 'enableListeners()', evidence='SRC ui/CategoryEditorFragment.java:170')
e('CategoryEditorFragment.enableListeners', 'CategoryEditorFragment$1.onClick', 'FRAMEWORK', 'tap OK / New / Edit (Delete goes through DoubleClickButton, see chunk 2)', gui=['Tap OK, New or Edit in the category dialog'], evidence=FW_VIEW + '; SRC ui/CategoryEditorFragment.java:94-126,412-417')
e('CategoryEditorFragment.onCreateView', 'CategoryEditorFragment$2.onItemClick', 'FRAMEWORK', 'tap a category row', gui=['Tap a category in the list'], evidence=FW_VIEW + '; SRC ui/CategoryEditorFragment.java:76,404-410')
# The OK click (CategoryEditorFragment.java:94-109) calls resultListener.onReceiveCategory, and the bytecode links that
# call to all four hosts. Each host has its own page (S_DLG_CATEGORY_STUDY / _PREVIEW / _QUIZ / _CARD) with one callback
# edge, so a dialog opened from one host reaches only that host's listener. The four bytecode fan-out edges are suppressed.
sup(('CategoryEditorFragment$1.onClick', 'StudyActivity$3.onReceiveCategory'),
    ('CategoryEditorFragment$1.onClick', 'QuizLauncherDialogFragment$10.onReceiveCategory'),
    ('CategoryEditorFragment$1.onClick', 'PreviewEditActivity$11.onReceiveCategory'),
    ('CategoryEditorFragment$1.onClick', 'CardEditor$8.onReceiveCategory'))
e('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$NewCategoryTask.doInBackground', 'ASYNC', 'v == newButton', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:111-114')
e('CategoryEditorFragment$NewCategoryTask.doInBackground', 'CategoryEditorFragment$NewCategoryTask.onPostExecute', 'ASYNC', 'the created/found category is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:258-278')
e('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$EditCategoryTask.doInBackground', 'ASYNC', 'v == editButton', needs_state=NEED_CATEGORY, evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:116-119')
e('CategoryEditorFragment$EditCategoryTask.doInBackground', 'CategoryEditorFragment$EditCategoryTask.onPostExecute', 'ASYNC', 'the edited category is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:207-234')
e('CategoryEditorFragment$1.onClick', 'CategoryEditorFragment$DeleteCategoryTask.doInBackground', 'ASYNC', 'v == deleteButton', needs_state=NEED_CATEGORY, evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:121-124')
e('CategoryEditorFragment$DeleteCategoryTask.doInBackground', 'CategoryEditorFragment$DeleteCategoryTask.onPostExecute', 'ASYNC', 'the deletion is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/CategoryEditorFragment.java:296-325')

# ---- CardListActivity
e('OpenActionsFragment$1.onClick', 'CardListActivity.<init>', 'ENTRY', 'v == listItem: startActivity(CardListActivity)', evidence='SRC ui/OpenActionsFragment.java:139-145')
e('PreviewEditActivity.onOptionsItemSelected', 'CardListActivity.<init>', 'ENTRY', 'editmenu_list_id: startActivityForResult(CardListActivity)', evidence='SRC ui/PreviewEditActivity.java:285-294')
for cb, lsrc in lc_chain('CardListActivity', ('onCreate', 'onDestroy', 'onCreateOptionsMenu', 'onOptionsItemSelected')):
    e(lsrc, 'CardListActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/CardListActivity.java:112-421')
e('CardListActivity.onCreate', 'CardListActivity$CardWrapperLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'multipleLoaderManager registers the CardWrapperList loader', evidence=FW_LOADER + '; SRC ui/CardListActivity.java:144-146,617-624')
e('CardListActivity$CardWrapperLoaderCallbacks.onCreateLoader', 'DBLoader.loadInBackground', 'ASYNC', 'loader.forceLoad()', evidence=FW_LOADER + '; SRC ui/CardListActivity.java:618-624; ui/loader/DBLoader.java:41-50')
e('CardListActivity$CardWrapperLoaderCallbacks.onCreateLoader', 'CardListActivity$CardWrapperLoaderCallbacks.onLoadFinished', 'ASYNC', 'the card-wrapper list is delivered to this callbacks object on the main thread (DBLoader.loadInBackground runs on a worker thread)', evidence=FW_LOADER + '; SRC ui/CardListActivity.java:618-633; ui/loader/DBLoader.java:41-50')
e('CardListActivity$CardWrapperLoaderCallbacks.onLoadFinished', 'CardListActivity$11.run', 'FRAMEWORK', 'handler.post(stored runnable) after the card list reports (CardListActivity manager only)', needs_state=LOADERS_DONE, evidence=FW_HANDLER + '; SRC ui/loader/MultipleLoaderManager.java:104-114; ui/CardListActivity.java:145,632')
# Round 1b B2: the list setup (adapter, selection, listeners, sort) needs no card; the card need stays on the long-press edge (CardListActivity.java:437-446)
e('CardListActivity$11.run', 'S_CARD_LIST', 'ENTERS', 'the adapter is attached and the list is shown', evidence='SRC ui/CardListActivity.java:640-655')
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
# group 6: CardListActivity.onActivityResult and CardListActivity.restartActivity are UNREACHABLE (see UNREACHABLE).

# ---- DetailScreen
e('CardListActivity$2.onMenuItemClick', 'DetailScreen.<init>', 'ENTRY', 'itemId == detail: startActivity(DetailScreen) (duplicate text for clarity; see above)', evidence='SRC ui/CardListActivity.java:225-226,243-248')
for cb, lsrc in lc_chain('DetailScreen', ('onCreate', 'onDestroy', 'onCreateOptionsMenu', 'onOptionsItemSelected')):
    e(lsrc, 'DetailScreen.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/DetailScreen.java:82-151')
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
e('S_FILEBROWSER', 'FileBrowserActivity.<init>', 'LIFECYCLE', 'the platform creates the activity before onCreate', evidence=FW_ACTIVITY + '; SRC ui/FileBrowserActivity.java:32')
e('FileBrowserActivity.<init>', 'FileBrowserActivity.<clinit>', 'LIFECYCLE', 'the JVM initialises the class before its first constructor call', evidence='INFERRED JVM class initialiser runs before the first constructor (Java language rule, not read from a source); SRC ui/FileBrowserActivity.java:32')
e('FileBrowserActivity$1.onFileBrowserFileClick', 'FileBrowserActivity.fileClickAction', 'CALL', 'fileClickAction(file)', evidence='SRC ui/FileBrowserActivity.java:68-71')
# group 11: fileClickAction (setResult(RESULT_OK); finish(), FileBrowserActivity.java:59-65) has NO edge to a host page.
# It is shared by every starter, so an edge here would let any route return to the wrong host. The result goes to the
# starter's own onActivityResult through that starter's RESULT edge (CardEditor.onOptionsItemSelected and
# CardEditor.startAudioBrowser, DatabaseMerger.onClick, ShareScreen.onClick: see section E and E2 below).

# ---- PreviewEditActivity
e('OpenActionsFragment$1.onClick', 'PreviewEditActivity.<init>', 'ENTRY', 'v == editItem: startActivity(PreviewEditActivity)', evidence='SRC ui/OpenActionsFragment.java:129-137')
e('EditTabFragment$1.onFileBrowserFileClick', 'PreviewEditActivity.<init>', 'ENTRY', 'Edit tab (dead code: EditTabFragment is never instantiated, see section L)', evidence='SRC ui/EditTabFragment.java:51-57')
for cb, lsrc in lc_chain('PreviewEditActivity', ('onCreate', 'onDestroy', 'onPause', 'onSaveInstanceState', 'onCreateOptionsMenu', 'onOptionsItemSelected')):
    e(lsrc, 'PreviewEditActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/PreviewEditActivity.java:95-423')
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
e('PreviewEditActivity.deleteCard', 'S_DLG_DELETE_CARD_PREVIEW', 'ENTERS', 'the confirm dialog is shown', evidence='SRC ui/PreviewEditActivity.java:510-525')
gui('S_DLG_DELETE_CARD_PREVIEW', 'PreviewEditActivity$6.onClick', 'Tap Yes (confirm delete)', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:515-521')
e('PreviewEditActivity$6.onClick', 'PreviewEditActivity$DeleteCardTask.doInBackground', 'ASYNC', 'new DeleteCardTask(...).execute()', evidence=FW_ASYNC + '; SRC ui/PreviewEditActivity.java:518-519')
e('PreviewEditActivity$DeleteCardTask.doInBackground', 'PreviewEditActivity$DeleteCardTask.onPostExecute', 'ASYNC', 'the delete result is delivered on the main thread', evidence=FW_ASYNC + '; SRC ui/PreviewEditActivity.java:663-684')
e('PreviewEditActivity$DeleteCardTask.onPostExecute', 'S_PREVIEW_EDIT', 'ENTERS', 'activity.restartActivity()', evidence='SRC ui/PreviewEditActivity.java:677-683')
# Round 1b B9: editmenu_detail_id starts DetailScreen (startActivityForResult, PreviewEditActivity.java:277-283)
e('PreviewEditActivity.onOptionsItemSelected', 'DetailScreen.<init>', 'ENTRY', 'editmenu_detail_id: startActivityForResult(DetailScreen)', guard='getCurrentCard() != null (PreviewEditActivity.java:278)', evidence='SRC ui/PreviewEditActivity.java:277-283')
e('PreviewEditActivity.onOptionsItemSelected', 'S_CARD_LIST', 'ENTERS', 'editmenu_list_id (duplicate text for clarity; see CardListActivity entry above)', evidence='SRC ui/PreviewEditActivity.java:285-294')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.showCategoriesDialog', 'CALL', 'menu_edit_categories', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:295-299,554-568')
e('PreviewEditActivity.showCategoriesDialog', 'S_DLG_CATEGORY_PREVIEW', 'ENTERS', 'df.show(...)', evidence='SRC ui/PreviewEditActivity.java:554-568')
e('S_DLG_CATEGORY_PREVIEW', 'PreviewEditActivity$11.onReceiveCategory', 'CALL', 'a category is picked (CategoryEditorFragment ok button); the Preview/Edit listener restarts the activity', evidence='SRC ui/PreviewEditActivity.java:631-637; ui/CategoryEditorFragment.java:94-109')
e('PreviewEditActivity.onOptionsItemSelected', 'S_EXT_BROWSER', 'ENTERS', 'editmenu_help', env=ENV_EXT_BROWSER, evidence='SRC ui/PreviewEditActivity.java:300-306')
e('PreviewEditActivity.onOptionsItemSelected', 'S_CARD_PLAYER', 'ENTERS', 'menu_card_player', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:307-316')
e('PreviewEditActivity.onOptionsItemSelected', 'S_PREVIEW_EDIT', 'ENTERS', 'menu_context_paste (restartActivity) / menu_context_swap_current (restartActivity): no further page', guard='menu_context_paste or menu_context_swap_current', evidence='SRC ui/PreviewEditActivity.java:323-337')
e('PreviewEditActivity.onOptionsItemSelected', 'S_DLG_WIPE_LEARNING', 'ENTERS', 'menu_context_wipe: AMGUIUtility.doConfirmProgressTask shows the confirm dialog', guard='itemId == menu_context_wipe (PreviewEditActivity.java:341)', evidence='SRC ui/PreviewEditActivity.java:341-342; utils/AMGUIUtility.java:121-138')
gui('S_DLG_WIPE_LEARNING', 'PreviewEditActivity$1.doHeavyTask', 'Tap OK (confirm wipe all learning data)', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:341-350; utils/AMGUIUtility.java:121-138')
# AMGUIUtility$4.run calls task.doHeavyTask() through the ProgressTask interface, so its bytecode edges reach every
# ProgressTask in the app (6 tasks). Those edges are suppressed; each task gets its own edge from its caller or dialog.
sup(('AMGUIUtility$4.run', 'DatabaseMerger$1.doHeavyTask'), ('AMGUIUtility$4.run', 'PreviewEditActivity$2$1.doHeavyTask'),
    ('AMGUIUtility$4.run', 'PreviewEditActivity$4.doHeavyTask'), ('AMGUIUtility$4.run', 'PreviewEditActivity$5.doHeavyTask'),
    ('AMGUIUtility$4.run', 'PreviewEditActivity$3$1.doHeavyTask'), ('AMGUIUtility$4.run', 'PreviewEditActivity$1.doHeavyTask'),
    ('AMGUIUtility$4$1.run', 'DatabaseMerger$1.doUITask'), ('AMGUIUtility$4$1.run', 'PreviewEditActivity$2$1.doUITask'),
    ('AMGUIUtility$4$1.run', 'PreviewEditActivity$4.doUITask'), ('AMGUIUtility$4$1.run', 'PreviewEditActivity$5.doUITask'),
    ('AMGUIUtility$4$1.run', 'PreviewEditActivity$3$1.doUITask'), ('AMGUIUtility$4$1.run', 'PreviewEditActivity$1.doUITask'))
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
e('PreviewEditActivity.onOptionsItemSelected', 'S_DLG_REMOVE_DUP', 'ENTERS', 'menu_context_remove_dup: AMGUIUtility.doConfirmProgressTask shows the confirm dialog', guard='itemId == menu_context_remove_dup (PreviewEditActivity.java:388)', evidence='SRC ui/PreviewEditActivity.java:388-389; utils/AMGUIUtility.java:121-138')
gui('S_DLG_REMOVE_DUP', 'PreviewEditActivity$4.doHeavyTask', 'Tap OK (confirm remove duplicate cards)', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:388-399; utils/AMGUIUtility.java:121-138')
e('PreviewEditActivity$4.doHeavyTask', 'PreviewEditActivity$4.doUITask', 'FRAMEWORK', 'doProgressTask runs doHeavyTask() on a background Thread, then posts doUITask() to the main thread', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:80-112')
e('PreviewEditActivity$4.doUITask', 'S_PREVIEW_EDIT', 'ENTERS', 'restartActivity()', evidence='SRC ui/PreviewEditActivity.java:395-397')
e('PreviewEditActivity.onOptionsItemSelected', 'DatabaseMerger.<init>', 'ENTRY', 'menu_context_merge_db: startActivityForResult(DatabaseMerger)', evidence='SRC ui/PreviewEditActivity.java:400-404')
e('PreviewEditActivity.onOptionsItemSelected', 'S_DLG_SHUFFLE', 'ENTERS', 'menu_context_shuffle: AMGUIUtility.doConfirmProgressTask shows the confirm dialog', guard='itemId == menu_context_shuffle (PreviewEditActivity.java:405)', evidence='SRC ui/PreviewEditActivity.java:405-406; utils/AMGUIUtility.java:121-138')
gui('S_DLG_SHUFFLE', 'PreviewEditActivity$5.doHeavyTask', 'Tap OK (confirm shuffle card order)', evidence=FW_DIALOGFRAG + '; SRC ui/PreviewEditActivity.java:405-416; utils/AMGUIUtility.java:121-138')
e('PreviewEditActivity$5.doHeavyTask', 'PreviewEditActivity$5.doUITask', 'FRAMEWORK', 'doProgressTask runs doHeavyTask() on a background Thread, then posts doUITask() to the main thread', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:80-112')
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
e('PreviewEditActivity$11.onReceiveCategory', 'S_PREVIEW_EDIT', 'ENTERS', 'restartActivity() for the new filter category', evidence='SRC ui/PreviewEditActivity.java:630-637')


# ================================================================== G. settings / stats
e('OpenActionsFragment$1.onClick', 'SettingsScreen.<init>', 'ENTRY', 'v == settingsItem: startActivity(SettingsScreen)', evidence='SRC ui/OpenActionsFragment.java:156-161')
for cb, lsrc in lc_chain('SettingsScreen', ('onCreate', 'onDestroy', 'onCreateOptionsMenu', 'onConfigurationChanged', 'onOptionsItemSelected')):
    e(lsrc, 'SettingsScreen.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC ui/SettingsScreen.java:124-222')
e('SettingsScreen.onCreate', 'SettingsScreen$SettingLoaderCallbacks.onCreateLoader', 'FRAMEWORK', 'multipleLoaderManager registers the Setting loader in onCreate', evidence=FW_LOADER + '; SRC ui/SettingsScreen.java:137-139,394-414')
e('SettingsScreen$SettingLoaderCallbacks.onCreateLoader', 'DBLoader.loadInBackground', 'ASYNC', 'loader.forceLoad()', evidence=FW_LOADER + '; SRC ui/SettingsScreen.java:398-401; ui/loader/DBLoader.java:41-50')
e('SettingsScreen$SettingLoaderCallbacks.onCreateLoader', 'SettingsScreen$SettingLoaderCallbacks.onLoadFinished', 'ASYNC', 'the Setting loader that this onCreateLoader made delivers the Setting to this callbacks object on the main thread (DBLoader.loadInBackground runs on a worker thread)', evidence=FW_LOADER + '; SRC ui/SettingsScreen.java:398-408; ui/loader/DBLoader.java:41-50')
e('SettingsScreen$SettingLoaderCallbacks.onLoadFinished', 'SettingsScreen$6.run', 'FRAMEWORK', 'handler.post(stored runnable) after the Setting loader reports (SettingsScreen manager only)', needs_state=LOADERS_DONE, evidence=FW_HANDLER + '; SRC ui/loader/MultipleLoaderManager.java:104-114; ui/SettingsScreen.java:138,407')
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
e('SettingsScreen.onBackPressed', 'S_DLG_SETTINGS_DISCARD', 'ENTERS', 'settingsChanged is true', guard='settingsChanged is true (SettingsScreen.java:196)', evidence='SRC ui/SettingsScreen.java:196-215')
e('S_SETTINGS', 'SettingsScreen.onBackPressed', 'SYSTEM', 'press Back in Settings', gui=['Press Back in Settings'], env=ENV_HW_KEY, evidence=FW_ACTIVITY + '; SRC ui/SettingsScreen.java:195-196')
gui('S_DLG_SETTINGS_DISCARD', 'SettingsScreen$3.onClick', 'Tap Yes (save before leaving)', evidence=FW_DIALOGFRAG + '; SRC ui/SettingsScreen.java:200-205')
e('SettingsScreen$3.onClick', 'SettingsScreen$SaveButtonTask.doInBackground', 'ASYNC', 'new SaveButtonTask().execute()', evidence=FW_ASYNC + '; SRC ui/SettingsScreen.java:202-203')
gui('S_DLG_SETTINGS_DISCARD', 'SettingsScreen$2.onClick', 'Tap No (discard)', evidence=FW_DIALOGFRAG + '; SRC ui/SettingsScreen.java:206-211')
e('SettingsScreen$2.onClick', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_CANCELED); finish()', evidence='SRC ui/SettingsScreen.java:208-210')
e('SettingsScreen.onBackPressed', 'S_PREVIEW_EDIT', 'ENTERS', 'settingsChanged is false: setResult(RESULT_CANCELED); finish()', guard='settingsChanged is false (SettingsScreen.java:196, 216-221)',
  needs_state=state_text('SettingsScreen was started from Preview/Edit (PreviewEditActivity.onOptionsItemSelected, editmenu_settings_id, PreviewEditActivity.java:269-272) in this process', ('session',)), evidence='SRC ui/SettingsScreen.java:216-221')
e('SettingsScreen.onBackPressed', 'S_STUDY', 'ENTERS', 'settingsChanged is false: setResult(RESULT_CANCELED); finish() (the Study caller restarts)', guard='settingsChanged is false (SettingsScreen.java:196, 216-221)',
  needs_state=state_text('SettingsScreen was started from Study (StudyActivity.onOptionsItemSelected, menusettings, gotoSettings at StudyActivity.java:155 and 719-723) in this process', ('session',)), evidence='SRC ui/SettingsScreen.java:216-221')
e('SettingsScreen.onBackPressed', 'S_MAIN_OPEN', 'ENTERS', 'settingsChanged is false: setResult(RESULT_CANCELED); finish() (back to the Open tab)', guard='settingsChanged is false (SettingsScreen.java:196, 216-221)',
  needs_state=state_text('SettingsScreen was started from the Open tab actions (OpenActionsFragment buttonClickListener onClick, settingsItem, OpenActionsFragment.java:156-161) in this process', ('session',)), evidence='SRC ui/SettingsScreen.java:216-221')
e('SettingsScreen.onBackPressed', 'S_MAIN_MISC', 'ENTERS', 'settingsChanged is false: setResult(RESULT_CANCELED); finish() (back to the Misc tab)', guard='settingsChanged is false (SettingsScreen.java:196, 216-221)',
  needs_state=state_text('SettingsScreen was started from the Misc tab (MiscTabFragment.onClick, defaultSettingsButton, MiscTabFragment.java:339-345) in this process', ('session',)), evidence='SRC ui/SettingsScreen.java:216-221')
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
# Round 1b B10: the .ttf picker is entered after its fragment lifecycle (onCreate, onCreateView, onResume browses the folder)
e('FileBrowserFragment.onResume@SETTINGS_Q', 'S_DLG_TYPEFACE_Q', 'ENTERS', 'the question-typeface .ttf picker is on screen (df.show at SettingsScreen.java:720; onResume lists the folder)', evidence='SRC ui/SettingsScreen.java:712-721; ui/FileBrowserFragment.java:209-212')
e('FileBrowserFragment.onResume@SETTINGS_A', 'S_DLG_TYPEFACE_A', 'ENTERS', 'the answer-typeface .ttf picker is on screen (df.show at SettingsScreen.java:731; onResume lists the folder)', evidence='SRC ui/SettingsScreen.java:723-732; ui/FileBrowserFragment.java:209-212')
NEED_TYPEFACE_Q_VISIBLE = state_text('the question typeface field is VISIBLE: its checkbox is ticked (a question font is saved, SettingsScreen.java:467-472, or the box was ticked, :659-660)', ('settings',))
NEED_TYPEFACE_A_VISIBLE = state_text('the answer typeface field is VISIBLE: its checkbox is ticked (an answer font is saved, SettingsScreen.java:475-480, or the box was ticked, :669-670)', ('settings',))
gui('S_SETTINGS', 'SettingsScreen$10.onClick', 'Tap the question-font checkbox', evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:658-661')
gui('S_SETTINGS', 'SettingsScreen$10.onClick', 'Tap the question-font field (opens the .ttf picker when visible)', needs_state=NEED_TYPEFACE_Q_VISIBLE, evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:712-721')
gui('S_SETTINGS', 'SettingsScreen$10.onClick', 'Tap the answer-font checkbox', evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:667-674')
gui('S_SETTINGS', 'SettingsScreen$10.onClick', 'Tap the answer-font field (opens the .ttf picker when visible)', needs_state=NEED_TYPEFACE_A_VISIBLE, evidence=FW_VIEW + '; SRC ui/SettingsScreen.java:723-732')

# ---- OptionScreen, AlgorithmCustomizationScreen (preference screens)
# (chunk 2: removed. The drawer Options item reaches OptionScreen.<init> through the INTENT edge above, then LIFECYCLE to onCreate.)
e('MiscTabFragment.onClick', 'OptionScreen.<init>', 'ENTRY', 'v == optionButton: startActivity(OptionScreen)', evidence='SRC ui/MiscTabFragment.java:226-228; ui/OptionScreen.java:44-58')
e('OptionScreen.onCreate', 'S_OPTION_SCREEN', 'ENTERS', 'addPreferencesFromResource(option_screen)', evidence='SRC ui/OptionScreen.java:46')
e('S_OPTION_SCREEN', 'OptionScreen.onConfigurationChanged', 'SYSTEM', 'rotate the device', gui=['Rotate the device'], evidence=FW_ACTIVITY + '; SRC ui/OptionScreen.java:60-63')
e('S_ALGORITHM_SCREEN', 'AlgorithmCustomizationScreen.onConfigurationChanged', 'SYSTEM', 'rotate the device', gui=['Rotate the device'], evidence=FW_ACTIVITY + '; SRC ui/AlgorithmCustomizationScreen.java:57-60')
e('S_OPTION_SCREEN', 'OptionScreen$1.onPreferenceClick', 'FRAMEWORK', 'tap "Customize scheduling algorithm"', gui=['Tap "Customize scheduling algorithm"'], evidence=FW_PREFERENCE + '; SRC ui/OptionScreen.java:50-51,65-82')
e('OptionScreen$1.onPreferenceClick', 'S_DLG_ALGORITHM_WARN', 'ENTERS', 'the warning dialog is shown', evidence='SRC ui/OptionScreen.java:68-78')
gui('S_DLG_ALGORITHM_WARN', 'OptionScreen$1$1.onClick', 'Tap OK (open the algorithm screen)', evidence=FW_DIALOGFRAG + '; SRC ui/OptionScreen.java:71-76')
e('OptionScreen$1$1.onClick', 'AlgorithmCustomizationScreen.<init>', 'ENTRY', 'startActivity(AlgorithmCustomizationScreen)', evidence='SRC ui/OptionScreen.java:73-74')
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
for cb, lsrc in lc_chain('DatabaseMerger', ('onCreate',)):
    e(lsrc, 'DatabaseMerger.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/DatabaseMerger.java:52-97')
e('DatabaseMerger.onCreate', 'S_DB_MERGER', 'ENTERS', 'setContentView(merge_layout)', evidence='SRC ui/DatabaseMerger.java:56')
e('S_DB_MERGER', 'DatabaseMerger.onClick', 'FRAMEWORK', 'tap the target/source field or the Merge/Cancel button', gui=['Tap a field or button in Database Merger'], evidence=FW_VIEW + '; SRC ui/DatabaseMerger.java:66-69,99-137')
e('DatabaseMerger.onClick', 'S_FILEBROWSER', 'ENTERS', 'v == targetEdit or v == sourceEdit: startActivityForResult(FileBrowserActivity, .db)', env=ENV_FB_STORAGE, evidence='SRC ui/DatabaseMerger.java:101-113')
e('DatabaseMerger.onActivityResult', 'S_DB_MERGER', 'ENTERS', 'the picked path is written into the target/source field', evidence='SRC ui/DatabaseMerger.java:83-96')
e('DatabaseMerger.onClick', 'DatabaseMerger$1.doHeavyTask', 'CALL', 'v == mergeButton: AMGUIUtility.doProgressTask (this edge skips doProgressTask; its task.doHeavyTask() call is utils/AMGUIUtility.java:83)', evidence='SRC ui/DatabaseMerger.java:115-120; utils/AMGUIUtility.java:83')
e('DatabaseMerger$1.doHeavyTask', 'DatabaseMerger$1.doUITask', 'FRAMEWORK', 'doProgressTask runs doHeavyTask() on a background Thread, then posts doUITask() to the main thread', evidence=FW_HANDLER + '; SRC utils/AMGUIUtility.java:80-112')
# DatabaseMerger has two starters. The Misc tab uses startActivity (no result: the Misc page stays on screen, so no edge).
# The Preview/Edit menu uses startActivityForResult (PreviewEditActivity.java:401-404), so the result goes to its
# onActivityResult only; that edge needs the session state that the merge was started from Preview/Edit.
e('DatabaseMerger$1.doUITask', 'PreviewEditActivity.onActivityResult', 'RESULT', 'setResult(RESULT_OK); finish(): the Preview/Edit starter gets its result (menu_context_merge_db)',
  needs_state=state_text('DatabaseMerger was started from Preview/Edit (menu_context_merge_db, startActivityForResult), not from the Misc tab', ('session',)),
  evidence=FW_RESULT + '; SRC ui/DatabaseMerger.java:123-129; ui/PreviewEditActivity.java:400-404')
e('DatabaseMerger.onClick', 'S_EXIT', 'ENTERS', 'v == cancelButton: finish()', evidence='SRC ui/DatabaseMerger.java:133-135')

# ---- ExportAnyMemoDbFragment (FileBrowserFragment@EXPORT variant; picks a .db, then the system Save dialog)
e('MiscTabFragment.onClick', 'ExportAnyMemoDbFragment.<init>', 'CALL', 'v == exportAnyMemoButton: new ExportAnyMemoDbFragment() before df.show', needs_state=NEED_EXPORT_SECTION, guard='v == exportAnyMemoButton (MiscTabFragment.java:253-256)', evidence='SRC ui/MiscTabFragment.java:253-256')
e('ExportAnyMemoDbFragment.<init>', 'ExportAnyMemoDbFragment.onCreate', 'LIFECYCLE', 'df.show(...) then the DialogFragment lifecycle runs onCreate', evidence=FW_DIALOGFRAG + '; SRC ui/ExportAnyMemoDbFragment.java:32-43')
for cb in ('onDestroy',):
    e('ExportAnyMemoDbFragment.onCreate', 'ExportAnyMemoDbFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/ExportAnyMemoDbFragment.java:54-60')
# group 2 (round 1): removed here. The guarded edge openFile@EXPORT -> ExportAnyMemoDbFragment$1.onFileBrowserFileClick is created in the FileBrowserFragment host loop.
e('ExportAnyMemoDbFragment$1.onFileBrowserFileClick', 'ExportAnyMemoDbFragment.exportDatabase', 'CALL', 'exportDatabase(file)', evidence='SRC ui/ExportAnyMemoDbFragment.java:39-41')
e('ExportAnyMemoDbFragment.exportDatabase', 'S_EXT_PICKER', 'ENTERS', 'ACTION_CREATE_DOCUMENT is started', env=ENV_PICKER, evidence='SRC ui/ExportAnyMemoDbFragment.java:45-52')
e('ExportAnyMemoDbFragment.onActivityResult', 'ExportAnyMemoDbFragment$4.call', 'FRAMEWORK', 'RESULT_OK: Observable.fromCallable runs call() on the io scheduler', env=ENV_PICKER, evidence=FW_RX + '; SRC ui/ExportAnyMemoDbFragment.java:64-75')
# round 1 (G3-5 s18, s19): the else branch (not the export save, ExportAnyMemoDbFragment.java:64, 96-97) forwards the export request code.
# The base FileBrowserFragment.onActivityResult import branch needs REQUEST_CODE_IMPORT_DB (FileBrowserFragment.java:326), so the forwarded
# call reaches no app code. No edge is kept: a '@EXPORT' variant would inherit the base auto CALLs (build_graph.py:228 copies them onto every variant).
e('ExportAnyMemoDbFragment$4.call', 'ExportAnyMemoDbFragment$2.accept', 'FRAMEWORK', 'the Observable emits onNext(true/false) on the main thread', evidence=FW_RX + '; SRC ui/ExportAnyMemoDbFragment.java:77-87')
e('ExportAnyMemoDbFragment$4.call', 'ExportAnyMemoDbFragment$3.accept', 'FRAMEWORK', 'the Observable emits onError(throwable)', evidence=FW_RX + '; SRC ui/ExportAnyMemoDbFragment.java:88-94')
e('ExportAnyMemoDbFragment$2.accept', 'S_MAIN_MISC', 'ENTERS', 'dismiss() returns to the Misc tab underneath', evidence='SRC ui/ExportAnyMemoDbFragment.java:79-86')

# ---- ConverterFragment (FileBrowserFragment@CONVERTER variant)
e('ConverterFragment.<init>', 'ConverterFragment.onCreate', 'LIFECYCLE', 'constructor then onCreate (the converter dialog is created by MiscTabFragment.onClick, MiscTabFragment.java:290-337, and shown with df.show)', evidence=FW_DIALOGFRAG + '; SRC ui/ConverterFragment.java:59-70')
# group 2 (round 1): removed here. The guarded edge openFile@CONVERTER -> ConverterFragment$1.onFileBrowserFileClick is created in the FileBrowserFragment host loop.
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
# ---- AbstractDownloaderFragment, split by host (group 12). The base class calls its abstract hooks
# (initialRetrieve, openCategory, goBack, hasMore, fetchDatabase) on `this`. From a node that both hosts reach, CHA
# resolves BOTH overrides, so a route that started on one host could run the other host's override (shared-node
# fan-out). Fix: every node on a path from a host page to a hook exists once per host, with suffix @AM
# (S_DOWNLOAD_AM, AnyMemoDownloaderFragment) or @DBX (S_DROPBOX_LIST, DropboxListFragment). The builder skips the
# bytecode CALL edges from the base method to both overrides, because a hand edge with the same base pair exists
# (tools/build_graph.py, add_auto_edges). Still shared, since none of them reaches a host-specific callee or page:
# onAttach, onCreate, RetrieveTask.onPreExecute, FetchDatabaseTask.onPreExecute and onPostExecute, the leaf dialogs
# S_DLG_DOWNLOAD_OK / S_DLG_DOWNLOAD_FAIL, and DownloadListAdapter.getView.
# A row click starts its Callable directly (ASYNC edge to the Callable node). A shared RetrieveTask.doInBackground
# would carry one CALL to the refresh Callable, so the click paths would appear to run initialRetrieve(); doInBackground@X
# therefore appears only on the refresh path. The row listener is registered in the shared getView; the row-click edge is drawn
# from RetrieveTask.onPostExecute@X (the host's rows are added there, AbstractDownloaderFragment.java:229-230), not from onCreateView@X.
DL_HOSTS = (
    ('AM', 'S_DOWNLOAD_AM', 'AnyMemoDownloaderFragment', ENV_NET, 'S_DLG_DOWNLOAD_CONFIRM_AM', 'AnyMemo source'),
    ('DBX', 'S_DROPBOX_LIST', 'DropboxListFragment', ENV_DROPBOX, 'S_DLG_DOWNLOAD_CONFIRM_DBX', 'Dropbox source'),
)
DL_AB = 'AbstractDownloaderFragment'
DL_RT = DL_AB + '$RetrieveTask'
DL_FT = DL_AB + '$FetchDatabaseTask'
DL_LN = DL_AB + '$DownloadListAdapter$1'
DL_CAT = DL_LN + '$1'
DL_BACK = DL_LN + '$2'
DL_NEEDS_BACK = state_text('a category was opened before in this session', ('session',))
for h_key, h_page, h_cls, h_env, h_confirm, h_desc in DL_HOSTS:
    hv = '@' + h_key
    if h_key == 'DBX':
        # Round 1b D12: DropboxListFragment.onCreate reads authToken from the arguments (DropboxListFragment.java:49-55)
        e(h_page, 'DropboxListFragment.onCreate', 'LIFECYCLE', 'fragment onCreate reads authToken from args', needs_state=state_text('the Dropbox token arrived in the activity extras (DropboxListActivity.java:42-43)', ('session',)), evidence='SRC downloader/dropbox/DropboxListFragment.java:49-55')
    for cb in ('onAttach', 'onCreate'):
        e(h_page, DL_AB + '.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback (no host-specific callee)', evidence=FW_FRAG + '; SRC downloader/common/AbstractDownloaderFragment.java:127-137')
    e(h_page, DL_AB + '.onCreateView' + hv, 'LIFECYCLE', 'Fragment onCreateView of this host (builds the row list and its row click)', evidence=FW_FRAG + '; SRC downloader/common/AbstractDownloaderFragment.java:139-167')
    e(h_page, DL_AB + '.onViewCreated' + hv, 'LIFECYCLE', 'Fragment onViewCreated of this host', evidence=FW_FRAG + '; SRC downloader/common/AbstractDownloaderFragment.java:169-174')
    # ---- list rows (tap a row)
    # Round 1b D6: the getView edge is no longer drawn from onCreateView@X; it is drawn once, from addList (below the loop)
    e(DL_RT + '.onPostExecute' + hv, DL_LN + '.onClick' + hv, 'FRAMEWORK', 'tap a row (category, back, or a database) once the list is shown; the row listener is set in getView', env=h_env, gui=['Tap a row in the download list'], evidence=FW_VIEW + '; SRC downloader/common/AbstractDownloaderFragment.java:229-230, 386-411, 409-438')
    e(DL_LN + '.onClick' + hv, DL_RT + '.onPreExecute', 'ASYNC', 'new RetrieveTask().execute(): onPreExecute runs on the calling (main) thread first', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:417-432')
    e(DL_LN + '.onClick' + hv, DL_CAT + '.call' + hv, 'ASYNC', 'the row is a category: new RetrieveTask().execute(Callable: openCategory)', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:417-424')
    e(DL_CAT + '.call' + hv, h_cls + '.openCategory', 'CALL', 'openCategory(di)', evidence='SRC downloader/common/AbstractDownloaderFragment.java:421-423')
    e(DL_CAT + '.call' + hv, DL_RT + '.onPostExecute' + hv, 'ASYNC', "the category's databases are delivered on the main thread", evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:417-424')
    e(DL_LN + '.onClick' + hv, DL_BACK + '.call' + hv, 'ASYNC', 'the row is ".." (back): new RetrieveTask().execute(Callable: goBack)', needs_state=DL_NEEDS_BACK, evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:425-432')
    e(DL_BACK + '.call' + hv, h_cls + '.goBack', 'CALL', 'goBack()', needs_state=DL_NEEDS_BACK, evidence='SRC downloader/common/AbstractDownloaderFragment.java:429-431')
    e(DL_BACK + '.call' + hv, DL_RT + '.onPostExecute' + hv, 'ASYNC', 'the top-level category list is delivered on the main thread', needs_state=DL_NEEDS_BACK, evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:425-432')
    e(DL_LN + '.onClick' + hv, DL_AB + '.showFetchDatabaseDialog' + hv, 'CALL', 'the row is a database (or a Dropbox file)', guard='row is neither Category nor Back (AbstractDownloaderFragment.java:417, 425)', evidence='SRC downloader/common/AbstractDownloaderFragment.java:433-435')
    # ---- download one database
    e(DL_AB + '.showFetchDatabaseDialog' + hv, h_confirm, 'ENTERS', 'the confirm-download dialog is shown', evidence='SRC downloader/common/AbstractDownloaderFragment.java:276-291')
    gui(h_confirm, DL_AB + '$2.onClick' + hv, 'Tap Yes (download this database)', evidence=FW_DIALOGFRAG + '; SRC downloader/common/AbstractDownloaderFragment.java:284-289')
    e(DL_AB + '$2.onClick' + hv, DL_AB + '.startFetchDatabaseTask' + hv, 'CALL', 'startFetchDatabaseTask(item)', evidence='SRC downloader/common/AbstractDownloaderFragment.java:286-287')
    e(DL_AB + '.startFetchDatabaseTask' + hv, DL_FT + '.onPreExecute' + hv, 'ASYNC', 'new FetchDatabaseTask().execute(item): onPreExecute runs on the calling (main) thread first', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:294-297')
    e(DL_FT + '.onPreExecute' + hv, DL_FT + '.doInBackground' + hv, 'ASYNC', 'the worker thread runs doInBackground after onPreExecute', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:305-316')
    # Round 1b D7: the direct startFetchDatabaseTask -> doInBackground edge is removed (doInBackground follows onPreExecute, see above)
    e(DL_FT + '.doInBackground' + hv, h_cls + '.fetchDatabase', 'CALL', 'fetchDatabase(item)', evidence='SRC downloader/common/AbstractDownloaderFragment.java:318-319')
    e(DL_FT + '.doInBackground' + hv, DL_FT + '.onPostExecute', 'ASYNC', 'the fetched path (or the exception) is delivered on the main thread', env=ENV_NET, evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:316-325')
    # ---- list the host's content on open (onViewCreated -> refreshList -> initialRetrieve)
    e(DL_AB + '.onViewCreated' + hv, DL_AB + '.refreshList' + hv, 'CALL', 'refreshList()', evidence='SRC downloader/common/AbstractDownloaderFragment.java:173')
    e(DL_AB + '.refreshList' + hv, DL_RT + '.onPreExecute' + hv, 'ASYNC', 'new RetrieveTask().execute(): onPreExecute runs on the calling (main) thread first', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:181-187')
    e(DL_RT + '.onPreExecute' + hv, DL_RT + '.doInBackground' + hv, 'ASYNC', 'the worker thread runs doInBackground of RetrieveTask (its Callable is initialRetrieve)', evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:181-187')
    # Round 1b D7 (RetrieveTask): the direct refreshList -> doInBackground edge is removed (doInBackground follows the host's onPreExecute)
    e(DL_RT + '.doInBackground' + hv, DL_AB + '$1.call' + hv, 'CALL', 'task.call(): runs the Callable, which returns initialRetrieve()', guard='refresh path: the one Callable from refreshList (AbstractDownloaderFragment.java:208-212; for-loop at :210)', evidence='SRC downloader/common/AbstractDownloaderFragment.java:208-212')
    e(DL_AB + '$1.call' + hv, h_cls + '.initialRetrieve', 'CALL', 'return initialRetrieve()', evidence='SRC downloader/common/AbstractDownloaderFragment.java:184-186')
    e(DL_AB + '$1.call' + hv, DL_RT + '.onPostExecute' + hv, 'ASYNC', 'the retrieved list (or the exception) is delivered on the main thread', env=ENV_NET, evidence=FW_ASYNC + '; SRC downloader/common/AbstractDownloaderFragment.java:220-234')
    e(DL_RT + '.onPostExecute' + hv, h_page, 'ENTERS', 'the list is shown (' + h_desc + ')', env=h_env, evidence='SRC downloader/common/AbstractDownloaderFragment.java:229-234')
    e(DL_RT + '.onPostExecute' + hv, 'S_DLG_DOWNLOAD_FAIL', 'ENTERS', 'initialRetrieve() threw (no network / Dropbox error)', env=ENV_NET, evidence='SRC downloader/common/AbstractDownloaderFragment.java:224-227')
    e(DL_RT + '.onPostExecute' + hv, h_cls + '.hasMore', 'CALL', 'hasMore() decides whether the Load-more footer is shown', evidence='SRC downloader/common/AbstractDownloaderFragment.java:231')
    e(DL_RT + '.onPostExecute' + hv, DL_AB + '$DownloadListAdapter.addList', 'CALL', 'dlAdapter.addList(downloadItems): the rows of the retrieved list are added', evidence='SRC downloader/common/AbstractDownloaderFragment.java:229-230')
# Round 1b D6: rows are laid out by the framework after addList (one shared node; the row listener is set in getView)
e(DL_AB + '$DownloadListAdapter.addList', DL_AB + '$DownloadListAdapter.getView', 'FRAMEWORK', 'the ListView lays out the new rows and calls getView (layout timing INFERRED)', evidence=FW_VIEW + '; fw_src android-8.1.0_r1 widget/ArrayAdapter.java:345 (notifyDataSetChanged), BaseAdapter.java:51, AbsListView.java:6406 (onChanged), 1989 (requestLayout), 2348 (obtainView calls getView)')
# ---- shared leaves: no host-specific callee; each dialog only shows a message
e(DL_FT + '.onPostExecute', 'S_DLG_DOWNLOAD_OK', 'ENTERS', 'the download succeeds: success dialog, then the path is added to the recent list', env=ENV_NET, evidence='SRC downloader/common/AbstractDownloaderFragment.java:334-341')
e(DL_FT + '.onPostExecute', 'S_DLG_DOWNLOAD_FAIL', 'ENTERS', 'fetchDatabase() threw', env=ENV_NET, evidence='SRC downloader/common/AbstractDownloaderFragment.java:330-333')
# Load more (AbstractDownloaderFragment$3 and LoadMoreTask) is dead in the standard configuration: the footer is
# removed again in onCreateView (AbstractDownloaderFragment.java:162-164) and is re-added only when hasMore() is
# true (AbstractDownloaderFragment.java:231-232, 270-271); both subclasses return false (AnyMemoDownloaderFragment.java:54-56,
# DropboxListFragment.java:91-93). No hand edge leads into the chain; it is UNREACHABLE (step-5 block at the end).

# ---- AnyMemoDownloaderActivity / Fragment (no login needed; needs the AnyMemo server)
e('AnyMemoDownloaderActivity.<init>', 'AnyMemoDownloaderActivity.onCreate', 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC downloader/anymemo/AnyMemoDownloaderActivity.java:9-13')
e('AnyMemoDownloaderActivity.onCreate', 'AnyMemoDownloaderFragment.onCreate', 'LIFECYCLE', 'the layout statically includes the fragment (<fragment> tag)', evidence=FW_FRAG + '; SRC downloader/anymemo/AnyMemoDownloaderActivity.java:10-13; res/layout/anymemo_downloader.xml')
# Round 1b D9: the two download branches of fetchDatabase (AnyMemoDownloaderFragment.java:79-85), one hand CALL each
e('AnyMemoDownloaderFragment.fetchDatabase', 'DownloaderUtils.downloadFile', 'CALL', 'fileName ends with .db: downloadFile(address, filePath), filePath = AMEnv.DEFAULT_ROOT_PATH + fileName', guard='fileName ends with .db (AnyMemoDownloaderFragment.java:79-81)', evidence='SRC downloader/anymemo/AnyMemoDownloaderFragment.java:81')
e('AnyMemoDownloaderFragment.fetchDatabase', 'DownloaderUtils.downloadFile', 'CALL', 'fileName ends with .zip: downloadFile(address, zipFilePath), zipFilePath = AMEnv.DEFAULT_TMP_PATH + fileName', guard='fileName ends with .zip (AnyMemoDownloaderFragment.java:83-85)', evidence='SRC downloader/anymemo/AnyMemoDownloaderFragment.java:85')
e('AnyMemoDownloaderFragment.onCreate', 'S_DOWNLOAD_AM', 'ENTERS', 'the fragment (and its AbstractDownloaderFragment base) is created', evidence='SRC downloader/anymemo/AnyMemoDownloaderFragment.java:35-39')

# ---- DropboxOauth2AccountActivity / Oauth2AccountActivity (OAuth2 + Custom Tabs) / DropboxListActivity+Fragment / UploadDropboxActivity
# Round 1b D2: the old loop (onCreate, onDestroy, onNewIntent as lifecycle steps) is replaced. super.onCreate is a CALL (DropboxOauth2AccountActivity.java:21).
# onNewIntent is entered by the browser redirect into the running activity (AndroidManifest.xml:79,86), so its entry comes from the login screen.
e('DropboxOauth2AccountActivity.onCreate', 'Oauth2AccountActivity.onCreate', 'CALL', 'super.onCreate(savedInstanceState)', evidence='SRC downloader/dropbox/DropboxOauth2AccountActivity.java:21')
e('S_DROPBOX_LOGIN', 'Oauth2AccountActivity.onNewIntent', 'ENTRY', 'browser redirect reaches the running singleTask activity (framework redirect delivery INFERRED)', needs_state=state_text('the Dropbox login page was opened by requestAuth() and this activity is still alive', ('session',)), env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:59-62; AndroidManifest.xml:79,86')
e('Oauth2AccountActivity.onCreate', 'Oauth2AccountActivity.requestAuth', 'CALL', 'no token saved yet (first use / fixtures have none)', evidence='SRC downloader/oauth/Oauth2AccountActivity.java:44-49')
e('Oauth2AccountActivity.requestAuth', 'S_DROPBOX_LOGIN', 'ENTERS', 'CustomTabsIntent.launchUrl shows the Dropbox login page', env=ENV_DROPBOX, evidence=FW_CUSTOMTABS + '; SRC downloader/oauth/Oauth2AccountActivity.java:127-131')
e('Oauth2AccountActivity.onCreate', 'Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'CALL', 'a token was saved before', needs_state=NEED_SAVED_TOKEN, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:44-46')
e('Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'Oauth2AccountActivity$2.onComplete', 'FRAMEWORK', 'verifyAccessToken(token) (a Completable) completes on the main thread', needs_state=NEED_SAVED_TOKEN, env=ENV_DROPBOX, evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:105-123')
e('Oauth2AccountActivity$1.onSuccess', 'DropboxOauth2AccountActivity.onAuthenticated', 'CALL', 'onAuthenticated(token)', env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:93; downloader/dropbox/DropboxOauth2AccountActivity.java:25-30')
e('Oauth2AccountActivity$2.onError', 'Oauth2AccountActivity.requestAuth', 'CALL', 'the saved token is no longer valid (verify error path)', needs_state=NEED_SAVED_TOKEN, env=ENV_DROPBOX, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:118-121')
e('Oauth2AccountActivity.onNewIntent', 'Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'CALL', 'the browser redirects back with the access-token fragment', env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:59-62')
# Round 1b D3: removed. The fetch path (fetchTokenAndOnAuthenticate, Oauth2AccountActivity.java:85-103) goes to $1.onSuccess and $1.onError only.
e('Oauth2AccountActivity$2.onComplete', 'DropboxOauth2AccountActivity.onAuthenticated', 'CALL', 'onAuthenticated(token): the saved token passed the verify call, then the list opens', needs_state=NEED_SAVED_TOKEN, env=ENV_DROPBOX, evidence='SRC downloader/oauth/Oauth2AccountActivity.java:114')
e('DropboxOauth2AccountActivity.onAuthenticated', 'DropboxListActivity.<init>', 'ENTRY', 'startActivity(DropboxListActivity); finish()', env=ENV_OAUTH_CALLBACK, evidence='SRC downloader/dropbox/DropboxOauth2AccountActivity.java:25-30')
for cb in ('onCreateOptionsMenu', 'onOptionsItemSelected'):
    e('DropboxListActivity.onCreate', 'DropboxListActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle / framework callback', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/DropboxListActivity.java:65-82')
e('DropboxListActivity.onCreate', 'DropboxListFragment.onCreate', 'CALL', 'the fragment transaction commits a new DropboxListFragment', evidence='SRC downloader/dropbox/DropboxListActivity.java:49-56')
e('DropboxListActivity.onCreate', 'S_DROPBOX_LIST', 'ENTERS', 'the fragment transaction commits', evidence='SRC downloader/dropbox/DropboxListActivity.java:49-56')
e('S_DROPBOX_LIST', 'DropboxListActivity$1.onClick', 'FRAMEWORK', 'tap the upload FAB', gui=['Tap the upload FAB'], evidence=FW_VIEW + '; SRC downloader/dropbox/DropboxListActivity.java:56-61')
e('DropboxListActivity$1.onClick', 'DropboxListActivity.openUploadDropbox', 'CALL', 'openUploadDropbox()', evidence='SRC downloader/dropbox/DropboxListActivity.java:59')
e('DropboxListActivity.openUploadDropbox', 'UploadDropboxActivity.<init>', 'ENTRY', 'startActivityForResult(UploadDropboxActivity)', evidence='SRC downloader/dropbox/DropboxListActivity.java:100-104')
e('DropboxListActivity.onOptionsItemSelected', 'S_EXIT', 'ENTERS', 'logout: invalidateSavedToken(); finish()', evidence='SRC downloader/dropbox/DropboxListActivity.java:75-78')
e('DropboxListActivity.onActivityResult', 'DropboxListActivity.refreshList', 'CALL', 'the upload activity returns RESULT_OK', guard='requestCode == OPEN_UPLOAD_DROPBOX_REQUEST_CODE and resultCode == RESULT_OK', evidence='SRC downloader/dropbox/DropboxListActivity.java:85-90')
e('DropboxListActivity.refreshList', 'AbstractDownloaderFragment.refreshList@DBX', 'CALL', 'fragment.refreshList() (Dropbox list fragment)', evidence='SRC downloader/dropbox/DropboxListActivity.java:95')
e('DropboxListFragment.initialRetrieve', 'DropboxListFragment$1.accept', 'FRAMEWORK', 'dropboxApiHelper.listFiles(...).blockingForEach(...) calls accept() synchronously on the calling (background) thread for each page', env=ENV_DROPBOX, evidence=FW_RX + '; SRC downloader/dropbox/DropboxListFragment.java:58-67')
for cb in ('onCreate',):
    e('S_DROPBOX_UPLOAD', 'UploadDropboxActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/UploadDropboxActivity.java:42-59')
for cb in ('onStart', 'onStop', 'onDestroy'):
    e('UploadDropboxActivity.onCreate', 'UploadDropboxActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC downloader/dropbox/UploadDropboxActivity.java:61-75')
# round 1 (G2-1 s13): duplicate of the guarded edge in the FileBrowserFragment section (notifyFileClick -> UploadDropboxActivity.onFileBrowserFileClick); removed here
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
e('CardPlayerActivity.onPostInit', 'CardPlayerService.onCreate', 'ENTRY', 'bindCardPlayerService(): bindService(Context.BIND_AUTO_CREATE)', needs_state=NEED_CARD, evidence='SRC ui/CardPlayerActivity.java:111,210-215')
# Round 1b C7: updateCardFrontSide has one CALL per branch (CardPlayerActivity.java:199-205); the automatic edge is replaced by these two
e('CardPlayerActivity.updateCardFrontSide', 'QACardActivity.displayCard@CardPlayerActivity', 'CALL', 'DOUBLE_SIDED: displayCard(false) shows the front side', guard='current card not null and DOUBLE_SIDED (CardPlayerActivity.java:199-202)', evidence='SRC ui/CardPlayerActivity.java:198-208')
e('CardPlayerActivity.updateCardFrontSide', 'QACardActivity.displayCard@CardPlayerActivity', 'CALL', 'displayCard(true) otherwise: single sided, question and answer shown', guard='current card not null and not DOUBLE_SIDED (CardPlayerActivity.java:199-205)', evidence='SRC ui/CardPlayerActivity.java:198-208')
e('CardPlayerService.onCreate', 'CardPlayerService.onBind', 'LIFECYCLE', 'the system binds the freshly created service', evidence=FW_SERVICE + '; SRC service/CardPlayerService.java:79-83,87-109')
e('CardPlayerService.onBind', 'CardPlayerActivity$3.onServiceConnected', 'FRAMEWORK', 'the binder is delivered to the ServiceConnection', evidence=FW_SERVICECONN + '; SRC service/CardPlayerService.java:88,108; ui/CardPlayerActivity.java:221-227')
for cb, lsrc in lc_chain('CardPlayerActivity', ('onCreate', 'onDestroy')):
    e(lsrc, 'CardPlayerActivity.' + cb, 'LIFECYCLE', 'Activity lifecycle callback', evidence=FW_ACTIVITY + '; SRC ui/CardPlayerActivity.java:61-92')
e('OpenActionsFragment$1.onClick', 'CardPlayerActivity.<init>', 'ENTRY', 'v == cardPlayerItem: startActivity(CardPlayerActivity) (duplicate text for clarity; see Open-actions section)', guard='v == cardPlayerItem (OpenActionsFragment.java:192-197)', evidence='SRC ui/OpenActionsFragment.java:192-197')
e('PreviewEditActivity.onOptionsItemSelected', 'CardPlayerActivity.<init>', 'ENTRY', 'menu_card_player: startActivityForResult(CardPlayerActivity) (duplicate text for clarity)', guard='getCurrentCard() != null', evidence='SRC ui/PreviewEditActivity.java:307-316')
e('CardPlayerActivity.onPostInit', 'CardPlayerActivity.showNoItemDialog', 'CALL', 'the deck has no card', guard='getCurrentCard() == null', evidence='SRC ui/CardPlayerActivity.java:112-115')
e('CardPlayerActivity.showNoItemDialog', 'S_DLG_NO_ITEM', 'ENTERS', 'the no-item dialog is shown (reused page)', evidence='SRC ui/CardPlayerActivity.java:150-169')
e('CardPlayerActivity.onPostInit', 'CardPlayerActivity.setupControlButtons', 'CALL', 'the deck has at least one card', needs_state=NEED_CARD, evidence='SRC ui/CardPlayerActivity.java:116')
e('CardPlayerActivity.setupControlButtons', 'CardPlayerFragment.<init>', 'CALL', 'a new CardPlayerFragment replaces buttons_root', evidence='SRC ui/CardPlayerActivity.java:122-128')
e('CardPlayerActivity.onPostInit', 'S_CARD_PLAYER', 'ENTERS', 'updateCardFrontSide() displays the first card', needs_state=NEED_CARD, evidence='SRC ui/CardPlayerActivity.java:117')
e('S_CARD_PLAYER', 'CardPlayerFragment.onCreate', 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/CardPlayerFragment.java:68-72')
# Round 1b B7: the fragment lifecycle is a chain (CardPlayerFragment.java:68-130), not a star from onCreate.
# onOptionsItemSelected is a menu callback (FRAMEWORK edge below), not a lifecycle step.
for cb_from, cb_to in (('onCreate', 'onCreateView'), ('onCreateView', 'onResume'), ('onResume', 'onPause'), ('onPause', 'onDestroyView')):
    e('CardPlayerFragment.' + cb_from, 'CardPlayerFragment.' + cb_to, 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/CardPlayerFragment.java:68-130')
e('CardPlayerFragment.onCreate', 'CardPlayerFragment.onCreateOptionsMenu', 'LIFECYCLE', 'Fragment lifecycle / framework callback', evidence=FW_FRAG + '; SRC ui/CardPlayerFragment.java:68-72,132-135')
e('S_CARD_PLAYER', 'CardPlayerFragment.onOptionsItemSelected', 'FRAMEWORK', 'tap the Card Player menu item (card_player_settings)', evidence=FW_MENU + '; SRC ui/CardPlayerFragment.java:137-146')
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
e('CardPlayerFragment$2.onReceive', 'CardPlayerActivity.gotoCardId', 'CALL', 'the activity is foreground and the card id changed', guard='activity is not null, activity.isActivityForeground(), and currentCardId != activity.getCurrentCard().getId() (CardPlayerFragment.java:234-238)', evidence='SRC ui/CardPlayerFragment.java:234-239')
e('CardPlayerActivity.gotoCardId', 'S_CARD_PLAYER', 'ENTERS', 'gotoCard(card) displays it', evidence='SRC ui/CardPlayerActivity.java:188-191,171-177')
e('CardTTSUtil.speakCardQuestion(Card,OnTextToSpeechCompletedListener)', 'CardPlayerState$4.onTextToSpeechCompleted', 'FRAMEWORK', 'the TTS finishes speaking the question (playQuestion\'s listener)', env=ENV_TTS, evidence=FW_TTS + '; SRC service/cardplayer/CardPlayerState.java:172-190')
e('CardPlayerState$4.onTextToSpeechCompleted', 'CardPlayerState$4$1.run', 'FRAMEWORK', 'handler.postDelayed(...)', env=ENV_TTS, evidence=FW_HANDLER + '; SRC service/cardplayer/CardPlayerState.java:176-187')
e('CardPlayerState$4$1.run', 'CardPlayerState$2.transition', 'CALL', 'context.getState().transition(context, PLAYING_QUESTION_COMPLETED): state is PLAYING_QUESTION (bytecode: virtual call CHA-resolved to the PLAYING_QUESTION enum body)', env=ENV_TTS, evidence='SRC service/cardplayer/CardPlayerState.java:182-186 (bytecode); service/cardplayer/CardPlayerState.java:69-115')
e('CardTTSUtil.speakCardAnswer(Card,OnTextToSpeechCompletedListener)', 'CardPlayerState$5.onTextToSpeechCompleted', 'FRAMEWORK', 'the TTS finishes speaking the answer (playAnswer\'s listener)', env=ENV_TTS, evidence=FW_TTS + '; SRC service/cardplayer/CardPlayerState.java:196-210')
e('CardPlayerState$5.onTextToSpeechCompleted', 'CardPlayerState$5$1.run', 'FRAMEWORK', 'handler.postDelayed(...)', env=ENV_TTS, evidence=FW_HANDLER + '; SRC service/cardplayer/CardPlayerState.java:199-209')
e('CardPlayerState$5$1.run', 'CardPlayerState$3.transition', 'CALL', 'context.getState().transition(context, PLAYING_ANSWER_COMPLETED): state is PLAYING_ANSWER (bytecode: virtual call CHA-resolved to the PLAYING_ANSWER enum body)', env=ENV_TTS, evidence='SRC service/cardplayer/CardPlayerState.java:201-205 (bytecode); service/cardplayer/CardPlayerState.java:117-163')
# Round 1b B7: the settings item is handled in onOptionsItemSelected (CardPlayerFragment.java:140-141), not in the button listener
e('CardPlayerFragment.onOptionsItemSelected', 'CardPlayerFragment.displaySettingsDialog', 'CALL', 'itemId == card_player_settings: displaySettingsDialog()', evidence='SRC ui/CardPlayerFragment.java:140-145,209-213')
e('CardPlayerFragment.displaySettingsDialog', 'CardPlayerSettingDialogFragment.onAttach', 'LIFECYCLE', 'a new CardPlayerSettingDialogFragment is shown', evidence=FW_DIALOGFRAG + '; SRC ui/CardPlayerFragment.java:211-212')
e('CardPlayerSettingDialogFragment.onAttach', 'CardPlayerSettingDialogFragment.onCreateView', 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/CardPlayerSettingDialogFragment.java:64-120')
e('CardPlayerSettingDialogFragment.onCreateView', 'S_CARD_PLAYER', 'ENTERS', 'the settings dialog is shown over Card Player (no distinct page modelled: only two seek bars)', evidence='SRC ui/CardPlayerSettingDialogFragment.java:68-119')
e('S_CARD_PLAYER', 'CardPlayerSettingDialogFragment$1.onProgressChanged', 'FRAMEWORK', 'drag the QA-interval seek bar', gui=['Drag the Q->A interval seek bar'], evidence=FW_VIEW + '; SRC ui/CardPlayerSettingDialogFragment.java:76,86-90')
e('S_CARD_PLAYER', 'CardPlayerSettingDialogFragment$2.onProgressChanged', 'FRAMEWORK', 'drag the card-interval seek bar', gui=['Drag the card-interval seek bar'], evidence=FW_VIEW + '; SRC ui/CardPlayerSettingDialogFragment.java:100,110-114')
e('CardPlayerSettingDialogFragment.onCreateView', 'CardPlayerSettingDialogFragment.onDismiss', 'LIFECYCLE', 'the dialog is dismissed (Back / outside tap)', evidence=FW_DIALOGFRAG + '; SRC ui/CardPlayerSettingDialogFragment.java:122-131')
e('CardPlayerSettingDialogFragment.onDismiss', 'S_CARD_PLAYER', 'ENTERS', 'the seek-bar values are saved to preferences', evidence='SRC ui/CardPlayerSettingDialogFragment.java:124-129')
e('CardPlayerFragment.onDestroyView', 'CardPlayerService.stopPlaying', 'CALL', 'stopPlaying() (make sure playback stops if the fragment is killed)', guard='activity and bound CardPlayerService are non-null (CardPlayerFragment.java:204-205)', evidence='SRC ui/CardPlayerFragment.java:125-130,201-207')
# round 1: onServiceDisconnected is NOT called by unbindService. LoadedApk.java:1644-1646 and :1668 show it is called only when an
# old connection is replaced (doConnected) or the service binder dies (doDeath). So it is a process-death event from the page.
e('S_CARD_PLAYER', 'CardPlayerActivity$3.onServiceDisconnected', 'FRAMEWORK', 'the CardPlayerService process dies (or the connection is replaced) while the card player is open; the system reports the disconnect',
  env=ENV_CARD_SVC_DIES, evidence='FW-SRC core/java/android/app/LoadedApk.java:1644-1646, 1668; SRC ui/CardPlayerActivity.java:229-232')
e('CardPlayerActivity.onBackPressed', 'S_PREVIEW_EDIT', 'ENTERS', 'setResult(RESULT_OK) with the current card id; finish() (the Preview/Edit caller restarts)',
  needs_state=state_text('CardPlayerActivity was started from Preview/Edit (PreviewEditActivity.onOptionsItemSelected, menu_card_player, PreviewEditActivity.java:307-314) in this process', ('session',)), evidence='SRC ui/CardPlayerActivity.java:180-185')
e('CardPlayerActivity.onBackPressed', 'S_MAIN_OPEN', 'ENTERS', 'setResult(RESULT_OK) with the current card id; finish() (back to the Open tab)',
  needs_state=state_text('CardPlayerActivity was started from the Open tab actions (OpenActionsFragment buttonClickListener onClick, cardPlayerItem, OpenActionsFragment.java:192-196) in this process', ('session',)), evidence='SRC ui/CardPlayerActivity.java:180-185')
e('S_CARD_PLAYER', 'CardPlayerActivity.onBackPressed', 'SYSTEM', 'press Back', gui=['Press Back in Card Player'], env=ENV_HW_KEY, evidence=FW_ACTIVITY + '; SRC ui/CardPlayerActivity.java:179-185')

# ---- ShareScreen (another app's share sheet, e.g. ColorDict, sends ACTION_SEND text/*)
e('S_ENTRY', 'ShareScreen.<init>', 'ENTRY', 'another app sends ACTION_SEND text/* to AnyMemo (the share sheet)', env=ENV_COLORDICT_SHARE,
  gui=['Share text from another app, choose AnyMemo'], evidence='SRC AndroidManifest.xml:164-172; ' + FW_ACTIVITY)
e('ShareScreen.<init>', 'ShareScreen.onCreate', 'LIFECYCLE', 'Activity lifecycle callback', env=ENV_COLORDICT_SHARE, evidence=FW_ACTIVITY + '; SRC ui/ShareScreen.java:63-95')
e('ShareScreen.onCreate', 'ShareScreen.onClick', 'FRAMEWORK', 'tap the db-name field, Save, Save+Preview or Cancel', gui=['Tap a field or button in the share screen'], env=ENV_COLORDICT_SHARE, evidence=FW_VIEW + '; SRC ui/ShareScreen.java:77-80,96-139')
e('ShareScreen.onClick', 'S_FILEBROWSER', 'ENTERS', 'v == dbnameView: startActivityForResult(FileBrowserActivity, .db)', env=ENV_FB_STORAGE, evidence='SRC ui/ShareScreen.java:129-133')
e('ShareScreen.onActivityResult', 'S_SHARE_SCREEN', 'ENTERS', 'the picked path is written into dbnameView', evidence='SRC ui/ShareScreen.java:142-157')
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
for cb, lsrc in lc_chain('OpenActionsFragment', ('onCreate', 'onAttach', 'onCreateView')):
    e(lsrc, 'OpenActionsFragment.' + cb, 'LIFECYCLE', 'DialogFragment lifecycle callback', evidence=FW_DIALOGFRAG + '; SRC ui/OpenActionsFragment.java:70-117')
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
# Round 1b B3: the quiz launcher is entered from its own onCreateDialog; df.show(...) is at OpenActionsFragment.java:152
e('QuizLauncherDialogFragment.onCreateDialog', 'S_DLG_QUIZ_LAUNCHER', 'ENTERS', 'the launcher is shown (df.show(...) runs in OpenActionsFragment.java:152; the dialog is built in onCreateDialog)', evidence='SRC ui/QuizLauncherDialogFragment.java:145-205; ui/OpenActionsFragment.java:152')
e('OpenActionsFragment$1.onClick', 'S_SETTINGS', 'ENTERS', 'v == settingsItem', evidence='SRC ui/OpenActionsFragment.java:156-161')
e('OpenActionsFragment$1.onClick', 'S_STATISTICS', 'ENTERS', 'v == statisticsItem', evidence='SRC ui/OpenActionsFragment.java:163-168')
e('OpenActionsFragment$1.onClick', 'ShareUtil.shareDb', 'CALL', 'v == shareItem', evidence='SRC ui/OpenActionsFragment.java:170-172')
e('ShareUtil.shareDb', 'S_EXT_PICKER', 'ENTERS', 'Intent.createChooser(ACTION_SEND) shows the system share sheet', env=ENV_PICKER, evidence='SRC utils/ShareUtil.java:25-36')
e('OpenActionsFragment$1.onClick', 'S_DLG_DELETE_DECK', 'ENTERS', 'v == deleteItem: confirm deleting the whole deck file', evidence='SRC ui/OpenActionsFragment.java:174-190')
e('OpenActionsFragment$1$1.onClick', 'BaseActivity.restartActivity', 'CALL', 'confirm delete: amFileUtil.deleteDbSafe + restartActivity()', evidence='SRC ui/OpenActionsFragment.java:178-185')
gui('S_DLG_DELETE_DECK', 'OpenActionsFragment$1$1.onClick', 'Tap Delete (confirm)', evidence=FW_DIALOGFRAG + '; SRC ui/OpenActionsFragment.java:177-186')

# ---- DownloadTabFragment
e('DownloadTabFragment.<init>', 'DownloadTabFragment.onAttach', 'LIFECYCLE', 'constructor then onAttach (the tab is constructed by AnyMemo$2, AnyMemo.java:247-248)', evidence=FW_FRAG + '; SRC ui/DownloadTabFragment.java:46-50')
e('DownloadTabFragment.onAttach', 'DownloadTabFragment.onCreateView', 'LIFECYCLE', 'Fragment lifecycle callback; the inherited Fragment.onCreate (not overridden in DownloadTabFragment) runs in between', evidence=FW_FRAG + '; SRC ui/DownloadTabFragment.java:52-61')
e('DownloadTabFragment.onCreateView', 'DownloadTabFragment.onClick', 'FRAMEWORK', 'tap a download-source button', gui=['Tap AnyMemo / Dropbox on the Download tab'], evidence=FW_VIEW + '; SRC ui/DownloadTabFragment.java:56-70')
e('DownloadTabFragment.onClick', 'AnyMemoDownloaderActivity.<init>', 'ENTRY', 'v == amButton: startActivity(AnyMemoDownloaderActivity)', guard='v == amButton (DownloadTabFragment.java:64)', evidence='SRC ui/DownloadTabFragment.java:64-66')
e('DownloadTabFragment.onClick', 'DropboxOauth2AccountActivity.<init>', 'ENTRY', 'v == dropboxButton: startActivity(DropboxOauth2AccountActivity)', guard='v == dropboxButton (DownloadTabFragment.java:67-69)', evidence='SRC ui/DownloadTabFragment.java:67-69')

# ---- MiscTabFragment
for cb in ('onDestroy', 'onSaveInstanceState'):
    e('S_MAIN_MISC', 'MiscTabFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback (the Misc page is left or its state is saved)', evidence=FW_FRAG + '; SRC ui/MiscTabFragment.java:128-222,400-406')
# group 2 (round 1): the Misc tab is constructed by AnyMemo$2 (AnyMemo.java:249-250), then runs onAttach, onCreate and onCreateView.
e('MiscTabFragment.<init>', 'MiscTabFragment.onAttach', 'LIFECYCLE', 'constructor then onAttach', evidence=FW_FRAG + '; SRC ui/MiscTabFragment.java:128-131')
e('MiscTabFragment.onAttach', 'MiscTabFragment.onCreate', 'LIFECYCLE', 'onAttach then onCreate', evidence=FW_FRAG + '; SRC ui/MiscTabFragment.java:143-146')
e('MiscTabFragment.onCreate', 'MiscTabFragment.onCreateView', 'LIFECYCLE', 'onCreate then onCreateView', evidence=FW_FRAG + '; SRC ui/MiscTabFragment.java:156-222')
e('MiscTabFragment.onCreateView', 'MiscTabFragment.onClick', 'FRAMEWORK', 'tap any Misc-tab button (every button shares one OnClickListener, dispatched by v == field)', gui=['Tap a button on the Misc tab'], evidence=FW_VIEW + '; SRC ui/MiscTabFragment.java:156-221,224-398')
e('MiscTabFragment.onClick', 'S_OPTION_SCREEN', 'ENTERS', 'v == optionButton', evidence='SRC ui/MiscTabFragment.java:226-228')
# group 2 (round 1): removed. The export picker is entered from FileBrowserFragment.onResume@EXPORT (host block).
e('MiscTabFragment.onClick', 'S_EXT_PICKER', 'ENTERS', 'v == importAnyMemoButton: ACTION_OPEN_DOCUMENT (the system document picker, not AnyMemo)', env=ENV_PICKER, evidence='SRC ui/MiscTabFragment.java:247-252')
for btn, converter in (('importMnemosyneButton', 'MnemosyneXMLImporter'), ('importSupermemoButton', 'SupermemoXMLImporter'),
                       ('importCSVButton', 'CSVImporter'), ('importZipButton', 'ZipImporter'), ('importTabButton', 'TabTxtImporter'),
                       ('importQAButton', 'QATxtImporter'), ('importSupermemo2008Button', 'Supermemo2008XMLImporter'),
                       ('importMnemosyne2CardsButton', 'Mnemosyne2CardsImporter')):
    e('MiscTabFragment.onClick', 'MiscTabFragment.launchImportConvert', 'CALL', 'v == %s' % btn, evidence='SRC ui/MiscTabFragment.java:266-289,408-414')
e('MiscTabFragment.launchImportConvert', 'S_EXT_PICKER', 'ENTERS', 'ACTION_OPEN_DOCUMENT is started for the chosen importer format', env=ENV_PICKER, evidence='SRC ui/MiscTabFragment.java:410-413')
for btn, converter in (('exportMnemosyneButton', 'MnemosyneXMLExporter'), ('exportCSVButton', 'CSVExporter'), ('exportTabButton', 'TabTxtExporter'),
                       ('exportQAButton', 'QATxtExporter'), ('exportZipButton', 'ZipExporter'), ('exportMnemosyne2CardsButton', 'Mnemosyne2CardsExporter')):
    e('MiscTabFragment.onClick', 'ConverterFragment.<init>', 'CALL', 'v == %s' % btn, needs_state=NEED_EXPORT_SECTION, evidence='SRC ui/MiscTabFragment.java:290-337')
# group 2 (round 1): removed. The converter picker is entered from FileBrowserFragment.onResume@CONVERTER (host block).
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
# (chunk 2: this pass-1 edge was moved by hand. Its source was the 3-arg DoubleClickButton constructor, which the framework never calls; the tap edge is now DoubleClickButton.setOnClickListener -> DoubleClickButton$1.onClick.)
e('DropboxApiHelper.getUserInfo', 'DropboxApiHelper$1.subscribe', 'FRAMEWORK', 'the framework calls subscribe (SingleOnSubscribe<UserInfo>) at downloader/dropbox/DropboxApiHelper.java:78', evidence=FW_RX + '; SRC downloader/dropbox/DropboxApiHelper.java:78-113')
# Round 1b D10: the four helper calls of DropboxApiHelper$3.subscribe (DropboxApiHelper.java:155-186); one hand CALL per site
e('DropboxApiHelper$3.subscribe', 'DropboxApiHelper.parseListFolderResponse', 'CALL', 'first list_folder page is parsed', guard='first list_folder response successful (DropboxApiHelper.java:155-158)', evidence='SRC downloader/dropbox/DropboxApiHelper.java:164')
e('DropboxApiHelper$3.subscribe', 'DropboxApiHelper.parseListFolderResponse', 'CALL', 'a continuation page is parsed (the has_more loop)', guard='hasMore is true and the continuation response is successful (DropboxApiHelper.java:167, 177-180)', evidence='SRC downloader/dropbox/DropboxApiHelper.java:186')
e('DropboxApiHelper$3.subscribe', 'DropboxApiHelper.getResponseErrorString', 'CALL', 'the first list_folder response failed: the error text is built', guard='first response failed (DropboxApiHelper.java:155-158)', evidence='SRC downloader/dropbox/DropboxApiHelper.java:156')
e('DropboxApiHelper$3.subscribe', 'DropboxApiHelper.getResponseErrorString', 'CALL', 'a continuation response failed: the error text is built', guard='continuation failed (DropboxApiHelper.java:177-180)', evidence='SRC downloader/dropbox/DropboxApiHelper.java:178')
e('DropboxApiHelper.listFiles', 'DropboxApiHelper$3.subscribe', 'FRAMEWORK', 'the framework calls subscribe (ObservableOnSubscribe<List<DownloadItem>>) at downloader/dropbox/DropboxApiHelper.java:143', evidence=FW_RX + '; SRC downloader/dropbox/DropboxApiHelper.java:143-190')
e('DropboxApiHelper.downloadFile', 'DropboxApiHelper$4.call', 'FRAMEWORK', 'the framework calls call (Callable<String>) at downloader/dropbox/DropboxApiHelper.java:194', evidence=FW_RX + '; SRC downloader/dropbox/DropboxApiHelper.java:194-229')
e('DropboxApiHelper.uploadDropbox', 'DropboxApiHelper$5.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at downloader/dropbox/DropboxApiHelper.java:233', evidence=FW_RX + '; SRC downloader/dropbox/DropboxApiHelper.java:233-255')
e('ExportAnyMemoDbFragment.onActivityResult', 'ExportAnyMemoDbFragment$2.accept', 'FRAMEWORK', 'the framework calls accept (Callable<Boolean>) at ui/ExportAnyMemoDbFragment.java:66', evidence=FW_RX + '; SRC ui/ExportAnyMemoDbFragment.java:66-75')
e('ExportAnyMemoDbFragment.onActivityResult', 'ExportAnyMemoDbFragment$3.accept', 'FRAMEWORK', 'the framework calls accept (Consumer<Boolean>) at ui/ExportAnyMemoDbFragment.java:78', evidence=FW_RX + '; SRC ui/ExportAnyMemoDbFragment.java:78-88')
e('FileBrowserFragment.importDb', 'FileBrowserFragment$6.call', 'FRAMEWORK', 'the framework calls call (io.reactivex.functions.Consumer<Throwable>) at ui/FileBrowserFragment.java:378', evidence=FW_RX + '; SRC ui/FileBrowserFragment.java:378-384')
e('FileBrowserFragment$FileBrowserAdapter.setItems', 'FileBrowserFragment$FileBrowserAdapter$3.compare', 'FRAMEWORK', 'the framework calls compare (Comparator<String>) at ui/FileBrowserFragment.java:598', evidence=FW_SORT + '; SRC ui/FileBrowserFragment.java:598-613')
e('FlipableCardFragment.onCreateView', 'FlipableCardFragment$1.getCount', 'FRAMEWORK', 'the framework calls getCount (FragmentStatePagerAdapter) at ui/FlipableCardFragment.java:78', evidence=FW_FRAG + '; SRC ui/FlipableCardFragment.java:79-90')
e('FlipableCardFragment.onCreateView', 'FlipableCardFragment$1.getItem', 'FRAMEWORK', 'the framework calls getItem (FragmentStatePagerAdapter) at ui/FlipableCardFragment.java:78', evidence=FW_FRAG + '; SRC ui/FlipableCardFragment.java:79-90')
e('FolderImportExportUtil.importFolder', 'FolderImportExportUtil$1.accept', 'FRAMEWORK', 'the framework calls accept (Consumer<Pair<Integer, List<String>>>) at utils/FolderImportExportUtil.java:66', evidence=FW_RX + '; SRC utils/FolderImportExportUtil.java:66-73')
e('FolderImportExportUtil.importFolder', 'FolderImportExportUtil$2.accept', 'FRAMEWORK', 'the framework calls accept (Consumer<Throwable>) at utils/FolderImportExportUtil.java:74', evidence=FW_RX + '; SRC utils/FolderImportExportUtil.java:74-78')
e('FolderImportExportUtil.exportFolder', 'FolderImportExportUtil$4.accept', 'FRAMEWORK', 'the framework calls accept (Consumer<Integer>) at utils/FolderImportExportUtil.java:116', evidence=FW_RX + '; SRC utils/FolderImportExportUtil.java:116-120')
e('FolderImportExportUtil.exportFolder', 'FolderImportExportUtil$6.call', 'FRAMEWORK', 'the framework calls call (Callable<Integer>) at utils/FolderImportExportUtil.java:83', evidence=FW_RX + '; SRC utils/FolderImportExportUtil.java:83-113')
e('FolderImportExportUtil.exportFolder', 'FolderImportExportUtil$5.accept', 'FRAMEWORK', 'the framework calls accept (Consumer<Throwable>) at utils/FolderImportExportUtil.java:121', evidence=FW_RX + '; SRC utils/FolderImportExportUtil.java:121-125')
gui('GradeButtonsFragment.onCreateView', 'GradeButtonsFragment$2.onTouch', 'Tap or use the control whose View.OnTouchListener listener is set at ui/GradeButtonsFragment.java:155', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/GradeButtonsFragment.java:155-162')
e('LearnQueueManager.flushDirtyCache', 'LearnQueueManager$1.run', 'FRAMEWORK', 'the framework calls run (Runnable) at queue/LearnQueueManager.java:246', evidence=FW_HANDLER + '; SRC queue/LearnQueueManager.java:246-278')
e('LearnQueueManager$1.run', 'LearnQueueManager$1$1.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at queue/LearnQueueManager.java:255', evidence=FW_RX + '; SRC queue/LearnQueueManager.java:255-273')
e('LearningDataDaoImpl.resetAllLearningData', 'LearningDataDaoImpl$1.call', 'FRAMEWORK', 'the framework calls call (Callable<Void>) at dao/LearningDataDaoImpl.java:43', evidence=FW_RX + '; SRC dao/LearningDataDaoImpl.java:43-50')
e('MnemosyneXMLExporter.convert', 'MnemosyneXMLExporter$1.call', 'FRAMEWORK', 'the framework calls call (Callable<List<Card>>) at converter/MnemosyneXMLExporter.java:52', evidence=FW_RX + '; SRC converter/MnemosyneXMLExporter.java:52-61')
e('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onError', 'FRAMEWORK', 'the framework calls onError (DisposableSingleObserver<String>) at downloader/oauth/Oauth2AccountActivity.java:89', evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:89-102')
e('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onSuccess', 'FRAMEWORK', 'the framework calls onSuccess (DisposableSingleObserver<String>) at downloader/oauth/Oauth2AccountActivity.java:89', evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:89-102')
# Round 1b D4(c): duplicate verify -> $2.onComplete removed (the verify edge above now targets it)
e('Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'Oauth2AccountActivity$2.onError', 'FRAMEWORK', 'the framework calls onError (DisposableCompletableObserver) at downloader/oauth/Oauth2AccountActivity.java:110', evidence=FW_RX + '; SRC downloader/oauth/Oauth2AccountActivity.java:110-123')
gui('PreviewEditActivity.<init>', 'PreviewEditActivity$12.onQueryTextChange', 'Tap or use the control whose SearchView.OnQueryTextListener listener is set at ui/PreviewEditActivity.java:750', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/PreviewEditActivity.java:750-763')
gui('QACardActivity.displayCard', 'QACardActivity$1.onClick', 'Tap or use the control whose View.OnClickListener listener is set at ui/QACardActivity.java:236', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:236-240')
e('QACardActivity.generateImageOnLongClickListener', 'QACardActivity$3.onLongClick', 'FRAMEWORK', 'the framework calls onLongClick (CardFragment.OnLongClickListener) at ui/QACardActivity.java:692', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:692-723')
gui('CardFragment.onCreateView', 'QACardActivity$4.onClick', 'Tap or use the control whose CardFragment.OnClickListener listener is set at ui/QACardActivity.java:726', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:726-732; ui/CardFragment.java:135-140')
gui('CardFragment.onCreateView', 'QACardActivity$5.onClick', 'Tap or use the control whose CardFragment.OnClickListener listener is set at ui/QACardActivity.java:734', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:734-740; ui/CardFragment.java:135-140')
gui('CardFragment.onCreateView', 'QACardActivity$6.onClick', 'Tap or use the control whose CardFragment.OnClickListener listener is set at ui/QACardActivity.java:742', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:742-748; ui/CardFragment.java:127-128')
gui('CardFragment.onCreateView', 'QACardActivity$7.onClick', 'Tap or use the control whose CardFragment.OnClickListener listener is set at ui/QACardActivity.java:749', kind='FRAMEWORK', evidence=FW_VIEW + '; SRC ui/QACardActivity.java:749-755; ui/CardFragment.java:127-128')
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
e('PreviewEditActivity$6.onClick', 'PreviewEditActivity$DeleteCardTask.onPreExecute', 'ASYNC', 'new DeleteCardTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/PreviewEditActivity.java:519; SRC ui/PreviewEditActivity.java:650')
e('PreviewEditActivity.searchCard', 'PreviewEditActivity$SearchCardTask.onPreExecute', 'ASYNC', 'new SearchCardTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/PreviewEditActivity.java:519; SRC ui/PreviewEditActivity.java:695')
e('QuizActivity$2.onCardChanged', 'QuizActivity$ChangeCardTask.doInBackground', 'ASYNC', 'the worker thread runs doInBackground of ChangeCardTask', evidence='FW-SRC core/java/android/os/AsyncTask.java:333; SRC ui/QuizActivity.java:400; SRC ui/QuizActivity.java:420')
e('QuizLauncherDialogFragment.onStart', 'QuizLauncherDialogFragment$InitTask.onPreExecute', 'ASYNC', 'new InitTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/QuizLauncherDialogFragment.java:212; SRC ui/QuizLauncherDialogFragment.java:283')
e('SettingsScreen$1.onClick', 'SettingsScreen$LoadDefaultTask.onPreExecute', 'ASYNC', 'new LoadDefaultTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/SettingsScreen.java:165; SRC ui/SettingsScreen.java:581')
e('SettingsScreen$3.onClick', 'SettingsScreen$SaveButtonTask.onPreExecute', 'ASYNC', 'new SaveButtonTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/SettingsScreen.java:165; SRC ui/SettingsScreen.java:496')
e('SettingsScreen.onOptionsItemSelected', 'SettingsScreen$SaveButtonTask.onPreExecute', 'ASYNC', 'new SaveButtonTask().execute(): onPreExecute runs on the calling (main) thread first', evidence='FW-SRC core/java/android/os/AsyncTask.java:645-650; SRC ui/SettingsScreen.java:165; SRC ui/SettingsScreen.java:496')
# cancel(true) runs in onPreExecute, which AsyncTask calls before it submits the FutureTask (AsyncTask.java:648-651).
# The FutureTask is then cancelled before it runs, so doInBackground does not run (JDK FutureTask skips it; INFERRED).
# done() posts the null result (AsyncTask.java:345-358, 362-371) and finish() calls onCancelled on the main thread (691-696, 710).
e('CategoryEditorFragment$DeleteCategoryTask.onPreExecute', 'CategoryEditorFragment$DeleteCategoryTask.onCancelled', 'ASYNC', 'cancel(true) in onPreExecute when no category is checked: doInBackground does not run; onCancelled runs on the main thread', guard='no category is checked in the list', evidence='FW-SRC core/java/android/os/AsyncTask.java:345-358,362-371,525-526,632-651,691-696,710; SRC ui/CategoryEditorFragment.java:287-289,307')
e('CategoryEditorFragment$EditCategoryTask.onPreExecute', 'CategoryEditorFragment$EditCategoryTask.onCancelled', 'ASYNC', 'cancel(true) in onPreExecute when no category is checked, the name is empty, or a category with the typed name exists: doInBackground does not run; onCancelled runs on the main thread', guard='no category is checked, or the name field is empty, or a category with the typed name already exists', evidence='FW-SRC core/java/android/os/AsyncTask.java:345-358,362-371,525-526,632-651,691-696,710; SRC ui/CategoryEditorFragment.java:187-189,196-201,217')

# ---- section L part 1 (UNREACHABLE, declaration-only groups; refs printed from source) ----
UNREACHABLE = {}
# ---- round 1: real exits for the lifecycle destroy (systemic S1). lc_chain no longer chains onDestroy / onDetach /
# onConfigurationChanged from onCreate (no trigger). Each exit below is a finish() or host destroy. Anonymous-class
# names were checked against the compiled LineNumberTable (javap is not installed; read with a small parser):
# CardEditor$1 = Neutral (Cancel) listener, SettingsScreen$2 = Neutral listener, StudyActivity$1 = OnCancelListener.
e('CardEditor$1.onClick', 'CardEditor.onDestroy', 'LIFECYCLE', 'setResult(RESULT_CANCELED); finish(): the activity is destroyed',
  evidence='SRC ui/CardEditor.java:143-146 (finish, the Cancel path); FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')
e('CardEditor.onBackPressed', 'CardEditor.onDestroy', 'LIFECYCLE', 'finish() on the Back path (isEditNew, or nothing changed): the activity is destroyed',
  guard='isEditNew, or the fields did not change (CardEditor.java:131; the else at 153-158)', evidence='SRC ui/CardEditor.java:127-131, 153-158; FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')
e('CardEditor$SaveCardTask.onPostExecute', 'CardEditor.onDestroy', 'LIFECYCLE', 'setResult(RESULT_OK); finish(): the activity is destroyed',
  evidence='SRC ui/CardEditor.java:624-629; FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')
e('DetailScreen$SaveCardTask.onPostExecute', 'DetailScreen.onDestroy', 'LIFECYCLE', 'setResult(RESULT_OK); finish(): the activity is destroyed',
  guard='exception is absent (DetailScreen.java:228; the else at 230-233)', evidence='SRC ui/DetailScreen.java:228-233; FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')
e('SettingsScreen$SaveButtonTask.onPostExecute', 'SettingsScreen.onDestroy', 'LIFECYCLE', 'setResult(RESULT_OK); finish(): the activity is destroyed',
  evidence='SRC ui/SettingsScreen.java:569-574; FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')
e('SettingsScreen$2.onClick', 'SettingsScreen.onDestroy', 'LIFECYCLE', 'setResult(RESULT_CANCELED); finish(): the activity is destroyed',
  evidence='SRC ui/SettingsScreen.java:208-210; FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')
e('SettingsScreen.onBackPressed', 'SettingsScreen.onDestroy', 'LIFECYCLE', 'settingsChanged is false: setResult(RESULT_CANCELED); finish(): the activity is destroyed',
  guard='settingsChanged is false (SettingsScreen.java:196, 216-221)', evidence='SRC ui/SettingsScreen.java:195-196; FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')
e('StudyActivity$1.onCancel', 'StudyActivity.onDestroy', 'LIFECYCLE', 'the dialog is cancelled (Back/outside tap): onBackPressed() finishes the activity, then onDestroy',
  evidence='SRC ui/StudyActivity.java:416-420 (class table 418-419); FW-SRC core/java/android/app/Activity.java:3001-3010, :7203-7208; INFERRED androidx AppCompatActivity/FragmentActivity.onBackPressed defers to super (androidx source not read; StudyActivity, QACardActivity and BaseActivity do not override it)')
e('CardPlayerActivity.onBackPressed', 'CardPlayerActivity.onDestroy', 'LIFECYCLE', 'setResult(RESULT_OK) with the current card id; finish(): the activity is destroyed',
  evidence='SRC ui/CardPlayerActivity.java:179-185 (finish at 184); FW-SRC core/java/android/app/Activity.java:5526-5528, :7203-7208')
# RecentListFragment is an androidx fragment hosted by the Recent tab (S_MAIN_RECENT). Back on that tab finishes the activity and
# the host destroys its fragments with it. The androidx destroy order is INFERRED (androidx source not read); the activity side is FW-SRC.
e('S_MAIN_RECENT', 'RecentListFragment.onDestroy', 'FRAMEWORK', 'Back on the Recent tab: the activity finishes and its fragments are destroyed with it',
  gui=['Press Back on the Recent tab'], env=ENV_HW_KEY, evidence='INFERRED androidx FragmentActivity destroys its fragments with the activity (androidx source not read); SRC ui/AnyMemo.java:399-411; FW-SRC core/java/android/app/Activity.java:7203-7208')
e('RecentListFragment.onDestroy', 'RecentListFragment.onDetach', 'LIFECYCLE', 'Fragment onDetach follows onDestroy', evidence=FW_FRAG + '; SRC ui/RecentListFragment.java:144-157')

# ---- round 1 PENDING: no exit modelled yet (the destroy is a placeholder, not a final verdict; see scratch/fix_round1.md)
for _n, _what in (
        ('CardListActivity.onDestroy', 'destroyed after finish() (Back or the activity exit); the finish sites are not modelled yet.'),
        ('PreviewEditActivity.onDestroy', 'destroyed after finish() (Back or the activity exit); the finish sites are not modelled yet.'),
        ('CategoryEditorFragment.onDestroy', 'a fragment is destroyed with its host or when its dialog is dismissed; the host is not modelled yet.'),
        ('QuizLauncherDialogFragment.onDestroy', 'a DialogFragment is destroyed when its dialog is dismissed or its host is destroyed; not modelled yet.'),
        ('CardEditor.onConfigurationChanged', 'runs on a rotation or other configuration change (system event); not modelled yet.'),
        ('SettingsScreen.onConfigurationChanged', 'runs on a rotation or other configuration change (system event); not modelled yet.'),
):
    UNREACHABLE[_n] = ('no_trigger_in_app', 'PENDING (round 1), not a final verdict: ' + _what + ' See scratch/fix_round1.md.',
                       'SRC lifecycle callback; exit not modelled in round 1', 'SOURCE')
UNREACHABLE['CardListActivity.onActivityResult'] = ('no_trigger_in_app', 'CardListActivity starts no child with startActivityForResult (every start in ui/CardListActivity.java is startActivity: lines 163, 240, 247, 254; no setResult either), so the framework never delivers a result to it; the list is started for a result by PreviewEditActivity (ui/PreviewEditActivity.java:285-294), and that result goes to PreviewEditActivity.onActivityResult', 'SRC ui/CardListActivity.java:167-173', 'SOURCE')
UNREACHABLE['CardListActivity.restartActivity'] = ('no_trigger_in_app', 'its only call in the app is in CardListActivity.onActivityResult (ui/CardListActivity.java:172), which is UNREACHABLE; the BaseActivity-typed mActivity.restartActivity() calls in GestureSelectionDialogFragment.onDismiss and OpenActionsFragment$1$1.onClick reach it only by class-hierarchy analysis: the gesture dialog is shown only by PreviewEditActivity (ui/PreviewEditActivity.java:578) and StudyActivity (ui/StudyActivity.java:651), and OpenActionsFragment only from AnyMemo (ui/AnyMemo.java:241, 243, via RecentListFragment and OpenTabFragment), so the runtime receiver is never a CardListActivity', 'SRC ui/CardListActivity.java:158-164', 'SOURCE')
UNREACHABLE['CardEditor.restartActivity'] = ('no_trigger_in_app', 'no call of CardEditor.restartActivity in the app (grep of restartActivity() in ui: only the declaration at ui/CardEditor.java:116); the mActivity.restartActivity() calls in GestureSelectionDialogFragment and OpenActionsFragment reach it only by class-hierarchy analysis, and their hosts are never a CardEditor', 'SRC ui/CardEditor.java:116', 'SOURCE')
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

# ---- section L part 2, pass 2 (hand-written 2026-10-26; NOT generated: do not run gen_L2.py on this file) ----
# Chunk 1: lifecycle of the REACHABLE card fragments, GradeButtonsFragment, CardPlayerActivity.onSaveInstanceState,
# and the bound-only CardPlayerService (created by bindService, never started with startService).
FW_CREATE_SVC = 'FW-SRC core/java/android/app/ActivityThread.java:3311-3321 (handleCreateService loads the class and calls newInstance) + FW-SRC core/java/android/app/Service.java:141-143 (bindService creates the service and calls onCreate)'
FW_TEARDOWN = 'INFERRED the system stops a bound-only Service after onUnbind returned false (ActiveServices.java in services/core not read); onUnbind dispatch is FW-SRC core/java/android/app/ActivityThread.java:3388-3400'

# card fragments (created in QACardActivity.displayCard: FlipableCardFragment at 372, TwoFieldsCardFragment at 322)
for cb, lsrc in lc_chain('FlipableCardFragment', ('onCreate', 'onCreateView')):
    e(lsrc, 'FlipableCardFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/FlipableCardFragment.java:59,73')
for cb, lsrc in lc_chain('TwoFieldsCardFragment', ('onCreate', 'onCreateView')):
    e(lsrc, 'TwoFieldsCardFragment.' + cb, 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/TwoFieldsCardFragment.java:96,126')

# GradeButtonsFragment: onCreate injects the fragment components, onDetach releases the helper
e('GradeButtonsFragment.<init>', 'GradeButtonsFragment.onCreate', 'LIFECYCLE', 'Fragment lifecycle callback', evidence=FW_FRAG + '; SRC ui/GradeButtonsFragment.java:99-101')
e('GradeButtonsFragment.onCreate', 'GradeButtonsFragment.onDetach', 'LIFECYCLE', 'the fragment is detached (replaced in buttons_root or its activity finishes)', evidence=FW_FRAG + '; SRC ui/GradeButtonsFragment.java:122-124')

# CardPlayerActivity: the list of lifecycle callbacks at section CardPlayerService lacked onSaveInstanceState
e('CardPlayerActivity.onCreate', 'CardPlayerActivity.onSaveInstanceState', 'LIFECYCLE', 'Activity saves its state (rotation or the activity is stopped)', evidence=FW_ACTIVITY + '; SRC ui/CardPlayerActivity.java:75-81')

# CardPlayerService: created by bindService (ui/CardPlayerActivity.java:214), never started
e('CardPlayerActivity.bindCardPlayerService', 'CardPlayerService.<init>', 'FRAMEWORK', 'bindService(BIND_AUTO_CREATE) creates the service object (the system instantiates the class)', evidence=FW_CREATE_SVC + '; SRC ui/CardPlayerActivity.java:210-215')
# round 1: enabled. unbindService -> ActivityThread.handleUnbindService calls s.onUnbind (ActivityThread.java:3388-3394, checked).
# The unbind is reached from CardPlayerActivity.onDestroy (auto CALL edge, unbindCardPlayerService), which now has a real exit.
e('CardPlayerActivity.unbindCardPlayerService', 'CardPlayerService.onUnbind', 'FRAMEWORK', 'unbindService() from unbindCardPlayerService: the system calls onUnbind', evidence=FW_SERVICE + '; SRC ui/CardPlayerActivity.java:217-219; FW-SRC core/java/android/app/ActivityThread.java:3388-3400')
# round 1: enabled. onUnbind returns false (CardPlayerService.java:130), so the bound-only service is stopped; the stop itself is INFERRED (see FW_TEARDOWN).
e('CardPlayerService.onUnbind', 'CardPlayerService.onDestroy', 'LIFECYCLE', 'the system stops the bound-only service after onUnbind returned false', evidence=FW_TEARDOWN + '; SRC service/CardPlayerService.java:124-134')

UNREACHABLE['CardPlayerService.onRebind'] = ('framework_never_calls', 'onUnbind returns false (service/CardPlayerService.java:124-130), so the system never calls onRebind: ActivityThread calls onRebind only when the rebind flag was set by a true onUnbind (FW-SRC core/java/android/app/ActivityThread.java:3356-3370, 3388-3392; Service.java:571-572)', 'SRC service/CardPlayerService.java:112', 'SOURCE')
UNREACHABLE['CardPlayerService.onStartCommand'] = ('framework_never_calls', 'no startService() of CardPlayerService in the app: the two startService calls start ConvertIntentService (ui/MiscTabFragment.java:477, ui/ConverterFragment.java:162); the card player service is only bound (ui/CardPlayerActivity.java:214, BIND_AUTO_CREATE), and a bind does not call onStartCommand (FW-SRC core/java/android/app/Service.java:141-143)', 'SRC service/CardPlayerService.java:117', 'SOURCE')

# ---- end pass 2 chunk 1 ----

# ---- section L part 2, pass 2, chunk 2 (hand-written 2026-10-26; NOT generated) ----
# Widgets and preferences created from XML, the list adapter that ListView calls, and the preference
# screens (the framework creates each activity with <init> before onCreate).
NEED_PREF_SAVED = state_text('A value was saved for this preference before (its key exists in SharedPreferences; not on a fresh install)', ('settings',))
NEED_FULLSCREEN = state_text('The Fullscreen mode box in Settings was ticked and saved before (SharedPreferences fullscreen_mode = true; option_screen.xml:66-69), so the flag is on when this activity is created', ('settings',))
FW_INFLATE_VIEW = ('FW-SRC core/java/android/view/LayoutInflater.java:90-91 (mConstructorSignature is (Context, AttributeSet)) '
                   'and :592-647 (createView constructs the view class reflectively with that signature)')
FW_INFLATE_PREF = ('FW-SRC core/java/android/preference/PreferenceManager.java:318-325 (inflateFromResource runs the PreferenceInflater, then onAttachedToHierarchy); '
                   'FW-SRC core/java/android/preference/GenericInflater.java:56-57 (mConstructorSignature is (Context, AttributeSet)), :368-385 (createItem), '
                   ':422-433 (a tag with a dot goes to createItem); FW-SRC core/java/android/preference/PreferenceInflater.java:45-48')
FW_PREF_INIT = ('FW-SRC core/java/android/preference/Preference.java:1323-1328 (onAttachedToHierarchy calls dispatchSetInitialValue), '
                '1547-1560 (dispatchSetInitialValue calls onSetInitialValue for a stored key or for an android:defaultValue); '
                'FW-SRC core/java/android/preference/EditTextPreference.java:159-160 (onSetInitialValue calls setText with getPersistedString or the default)')
FW_PREF_TAP = ('FW-SRC core/java/android/preference/DialogPreference.java:274-277 (onClick shows the dialog); '
               'FW-SRC core/java/android/preference/EditTextPreference.java:142-148 (OK calls setText), :88-94 (setText calls persistString)')
FW_CLICK = ('FW-SRC core/java/android/view/View.java:6143 (setOnClickListener stores the listener) and :6289-6294 '
            '(performClick calls li.mOnClickListener.onClick(this))')

# AMSpinner: settings_screen.xml has nine AMSpinner tags, all created by setContentView in SettingsScreen$6.run
e('SettingsScreen$6.run', 'AMSpinner.<init>', 'FRAMEWORK', 'setContentView(settings_screen) creates the spinners from the layout',
  evidence=FW_INFLATE_VIEW + '; SRC ui/SettingsScreen.java:275; res/layout/settings_screen.xml:24-219')
e('AMSpinner.<init>', 'AMSpinner.<clinit>', 'LIFECYCLE', 'class initialisation: the class has assert statements, so javac sets a static flag in <clinit>',
  evidence='SRC ui/widgets/AMSpinner.java:56-57; INFERRED the JVM runs the class initialiser before the first constructor call (JVM class-initialiser rule, not read)')
UNREACHABLE['AMSpinner.getItemValueForPosition'] = ('no_trigger_in_app', 'no call of this method in the app (grep: only its declaration); the spinner values are read through getSelectedItemValue and selectItemFromValue, which do not call it', 'SRC ui/widgets/AMSpinner.java:79', 'SOURCE')

# DoubleClickButton (the Delete button of category_dialog.xml): created by inflate in CategoryEditorFragment.onCreateView
e('CategoryEditorFragment.onCreateView', 'DoubleClickButton.<init>(Context,AttributeSet)', 'FRAMEWORK', 'inflate(category_dialog) creates the Delete button',
  evidence=FW_INFLATE_VIEW + '; SRC ui/CategoryEditorFragment.java:73; res/layout/category_dialog.xml:67-75')
# deleteButton is typed Button (line 42) and assigned at line 82; the bytecode call goes to Button, the JVM runs the DoubleClickButton override
e('CategoryEditorFragment.enableListeners', 'DoubleClickButton.setOnClickListener', 'CALL', 'deleteButton.setOnClickListener(buttonOnClickListener): the JVM dispatches to the DoubleClickButton override',
  evidence='SRC ui/CategoryEditorFragment.java:414,42,82; ui/widgets/DoubleClickButton.java:80-84')
e('DoubleClickButton.setOnClickListener', 'DoubleClickButton$1.onClick', 'FRAMEWORK', 'tap Delete in the category dialog (the first tap only shows a toast)',
  gui=['Tap Delete in the category dialog'], evidence=FW_CLICK + '; SRC ui/widgets/DoubleClickButton.java:80-84,89-104')
e('DoubleClickButton$1.onClick', 'CategoryEditorFragment$1.onClick', 'CALL', 'second tap within effective_duration_millis: onClickListener.onClick(v) runs the delete listener',
  guard='the second tap comes within effective_duration_millis (5000, res/layout/category_dialog.xml:75) of the first; the first tap only shows a toast (DoubleClickButton.java:89-104)',
  gui=['Tap Delete again within 5 seconds'], evidence='SRC ui/widgets/DoubleClickButton.java:89-104; res/layout/category_dialog.xml:75; ui/CategoryEditorFragment.java:94-102,414')
UNREACHABLE['DoubleClickButton.<init>(Context)'] = ('framework_never_calls', 'the layout inflater constructs a view only with (Context, AttributeSet) (LayoutInflater.java:90-91, 592-647); no app code calls this constructor (grep: no new DoubleClickButton)', 'SRC ui/widgets/DoubleClickButton.java:67', 'SOURCE')
UNREACHABLE['DoubleClickButton.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'the same: the inflater uses only the (Context, AttributeSet) constructor (LayoutInflater.java:90-91); no app code calls this one (grep: no new DoubleClickButton)', 'SRC ui/widgets/DoubleClickButton.java:55', 'SOURCE')

# CategoryAdapter.getView: the ListView calls the adapter when it lays out the rows (setAdapter in InitTask.onPreExecute)
e('CategoryEditorFragment$InitTask.onPreExecute', 'CategoryEditorFragment$CategoryAdapter.getView', 'FRAMEWORK', 'the list is laid out after setAdapter: the ListView asks the adapter for each row view',
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2335-2365 (obtainView calls mAdapter.getView); INFERRED setAdapter (AbsListView.java:908, read) leads to the layout pass that calls obtainView (layout code not read); SRC ui/CategoryEditorFragment.java:137-140')

# Preference screens: the framework creates the activity with <init>, then calls onCreate (the old shortcuts into onCreate are removed above)
e('OptionScreen.<init>', 'OptionScreen.onCreate', 'LIFECYCLE', 'the system creates the activity and calls onCreate (PreferenceActivity)',
  evidence=FW_ACTIVITY + '; SRC ui/OptionScreen.java:44-46')
e('AlgorithmCustomizationScreen.<init>', 'AlgorithmCustomizationScreen.onCreate', 'LIFECYCLE', 'the system creates the activity and calls onCreate (PreferenceActivity)',
  evidence=FW_ACTIVITY + '; SRC ui/AlgorithmCustomizationScreen.java:42-44')

# Preferences from XML: addPreferencesFromResource creates each preference (framework), attaches it, and calls getPersistedString or persistString
e('AlgorithmCustomizationScreen.onCreate', 'FloatEditTextPreference.<init>(Context,AttributeSet)', 'FRAMEWORK', 'addPreferencesFromResource(algorithm_customization_screen) creates each float preference',
  evidence=FW_INFLATE_PREF + '; SRC ui/AlgorithmCustomizationScreen.java:44; res/xml/algorithm_customization_screen.xml:25-151')
e('OptionScreen.onCreate', 'IntegerEditTextPreference.<init>(Context,AttributeSet)', 'FRAMEWORK', 'addPreferencesFromResource(option_screen) creates the integer preference',
  evidence=FW_INFLATE_PREF + '; SRC ui/OptionScreen.java:46; res/xml/option_screen.xml:87')
UNREACHABLE['FloatEditTextPreference.<init>(Context)'] = ('framework_never_calls', 'the preference inflater constructs a preference only with (Context, AttributeSet) (GenericInflater.java:56-57, 368-385); no app code calls this constructor (grep: no new FloatEditTextPreference)', 'SRC ui/widgets/FloatEditTextPreference.java:34', 'SOURCE')
UNREACHABLE['FloatEditTextPreference.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'the same: the inflater uses only the (Context, AttributeSet) constructor (GenericInflater.java:56-57); no app code calls this one (grep: no new FloatEditTextPreference)', 'SRC ui/widgets/FloatEditTextPreference.java:42', 'SOURCE')
UNREACHABLE['IntegerEditTextPreference.<init>(Context)'] = ('framework_never_calls', 'the preference inflater constructs a preference only with (Context, AttributeSet) (GenericInflater.java:56-57, 368-385); no app code calls this constructor (grep: no new IntegerEditTextPreference)', 'SRC ui/widgets/IntegerEditTextPreference.java:39', 'SOURCE')
UNREACHABLE['IntegerEditTextPreference.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'the same: the inflater uses only the (Context, AttributeSet) constructor (GenericInflater.java:56-57); no app code calls this one (grep: no new IntegerEditTextPreference)', 'SRC ui/widgets/IntegerEditTextPreference.java:64', 'SOURCE')

e('AlgorithmCustomizationScreen.onCreate', 'FloatEditTextPreference.getPersistedString', 'FRAMEWORK', 'a float value was saved before: the preference reads it when the screen is set up',
  needs_state=NEED_PREF_SAVED, evidence=FW_PREF_INIT + '; SRC ui/widgets/FloatEditTextPreference.java:47-49')
e('AlgorithmCustomizationScreen.onCreate', 'FloatEditTextPreference.persistString', 'FRAMEWORK', 'the screen is set up and the preference has an android:defaultValue or a stored value: setText stores it',
  guard='the preference has android:defaultValue (or a stored key), so dispatchSetInitialValue calls onSetInitialValue (Preference.java:1547-1560)',
  evidence=FW_PREF_INIT + '; SRC ui/widgets/FloatEditTextPreference.java:52-53; res/xml/algorithm_customization_screen.xml')
e('S_ALGORITHM_SCREEN', 'FloatEditTextPreference.persistString', 'FRAMEWORK', 'tap a float setting, type a value, tap OK in its dialog',
  gui=['Tap a float setting', 'Type a value', 'Tap OK'], evidence=FW_PREF_TAP + '; SRC ui/widgets/FloatEditTextPreference.java:52-53')

e('OptionScreen.onCreate', 'IntegerEditTextPreference.getPersistedString', 'FRAMEWORK', 'an integer value was saved before: the preference reads it when the screen is set up',
  needs_state=NEED_PREF_SAVED, evidence=FW_PREF_INIT + '; SRC ui/widgets/IntegerEditTextPreference.java:69-71')
e('OptionScreen.onCreate', 'IntegerEditTextPreference.persistString', 'FRAMEWORK', 'the screen is set up and the preference has an android:defaultValue or a stored value: setText stores it',
  guard='the preference has android:defaultValue (or a stored key), so dispatchSetInitialValue calls onSetInitialValue (Preference.java:1547-1560)',
  evidence=FW_PREF_INIT + '; SRC ui/widgets/IntegerEditTextPreference.java:74-80; res/xml/option_screen.xml:87-90')
e('S_OPTION_SCREEN', 'IntegerEditTextPreference.persistString', 'FRAMEWORK', 'tap the integer setting, type a number, tap OK in its dialog',
  gui=['Tap the integer setting', 'Type a number', 'Tap OK'], evidence=FW_PREF_TAP + '; SRC ui/widgets/IntegerEditTextPreference.java:74-80')

# ---- end pass 2 chunk 2 ----
# ---- section L part 2, pass 2, chunk 3 (2026-10-26) ----
# ORMLite DAO links, Dagger providers and injected-field edges, the data-binding path, no-caller roots,
# the Oauth1 island. Hand part from scratch/gen_hand4.py; Dagger field edges from scratch/gen_dagger.py.
C3_ORM = ('INFERRED ORMLite (DaoManager, called by OrmLiteSqliteOpenHelper.getDao) creates the DAO class named by '
          '@DatabaseTable(daoClass=...) through one of its constructors; the overload is not known, so both are kept, '
          'and the ORMLite source is not read')
C3_CLINIT = ('INFERRED the JVM initialises a class before its first constructor call (class-initialiser rule; '
             'the JVM specification is not read in this build)')
C3_DATABIND = ('INFERRED the androidx DataBindingUtil and its DataBinderMapper (library source not read) bind the '
               'layout through the generated mapper, which selects the Binding class by layout id')
C3_PROVIDER = ('INFERRED javax.inject.Provider.get() is an interface call made by Dagger-generated code, which is not '
               'in the build output; the bytecode extractor does not follow it, so the target is the object the provider builds')
C3_LIB_PENDING = ('INFERRED the androidx ViewDataBinding pending-bindings pass (library source not read) runs '
                  'executeBindings and hasPendingBindings after the generated invalidateAll marks the binding dirty')

e('AnyMemoDBOpenHelper.getCardDao', 'CardDaoImpl.<init>(ConnectionSource,DatabaseTableConfig)', 'FRAMEWORK', 'the first getCardDao() call asks ORMLite for the Card DAO, which creates it',
  evidence=C3_ORM + '; SRC common/AnyMemoDBOpenHelper.java:174 (getDao(Card.class))', cls='non_standard', via='ORMLite DaoManager (reflection)')
e('AnyMemoDBOpenHelper.getCardDao', 'CardDaoImpl.<init>(ConnectionSource,Class)', 'FRAMEWORK', 'the first getCardDao() call asks ORMLite for the Card DAO, which creates it',
  evidence=C3_ORM + '; SRC common/AnyMemoDBOpenHelper.java:174 (getDao(Card.class))', cls='non_standard', via='ORMLite DaoManager (reflection)')
e('CardDaoImpl.<init>(ConnectionSource,DatabaseTableConfig)', 'CardDaoImpl.<clinit>', 'LIFECYCLE', 'the JVM initialises CardDaoImpl before its constructor runs',
  evidence=C3_CLINIT + '; SRC dao/CardDaoImpl.java')
e('CardDaoImpl.<init>(ConnectionSource,Class)', 'CardDaoImpl.<clinit>', 'LIFECYCLE', 'the JVM initialises CardDaoImpl before its constructor runs',
  evidence=C3_CLINIT + '; SRC dao/CardDaoImpl.java')
e('AnyMemoDBOpenHelper.getCategoryDao', 'CategoryDaoImpl.<init>(ConnectionSource,DatabaseTableConfig)', 'FRAMEWORK', 'the first getCategoryDao() call asks ORMLite for the Category DAO, which creates it',
  evidence=C3_ORM + '; SRC common/AnyMemoDBOpenHelper.java:219 (getDao(Category.class))', cls='non_standard', via='ORMLite DaoManager (reflection)')
e('AnyMemoDBOpenHelper.getCategoryDao', 'CategoryDaoImpl.<init>(ConnectionSource,Class)', 'FRAMEWORK', 'the first getCategoryDao() call asks ORMLite for the Category DAO, which creates it',
  evidence=C3_ORM + '; SRC common/AnyMemoDBOpenHelper.java:219 (getDao(Category.class))', cls='non_standard', via='ORMLite DaoManager (reflection)')
e('CategoryDaoImpl.<init>(ConnectionSource,DatabaseTableConfig)', 'CategoryDaoImpl.<clinit>', 'LIFECYCLE', 'the JVM initialises CategoryDaoImpl before its constructor runs',
  evidence=C3_CLINIT + '; SRC dao/CategoryDaoImpl.java')
e('CategoryDaoImpl.<init>(ConnectionSource,Class)', 'CategoryDaoImpl.<clinit>', 'LIFECYCLE', 'the JVM initialises CategoryDaoImpl before its constructor runs',
  evidence=C3_CLINIT + '; SRC dao/CategoryDaoImpl.java')
e('AnyMemoDBOpenHelper.getSettingDao', 'SettingDaoImpl.<init>(ConnectionSource,DatabaseTableConfig)', 'FRAMEWORK', 'the first getSettingDao() call asks ORMLite for the Setting DAO, which creates it',
  evidence=C3_ORM + '; SRC common/AnyMemoDBOpenHelper.java:197 (getDao(Setting.class))', cls='non_standard', via='ORMLite DaoManager (reflection)')
e('AnyMemoDBOpenHelper.getSettingDao', 'SettingDaoImpl.<init>(ConnectionSource,Class)', 'FRAMEWORK', 'the first getSettingDao() call asks ORMLite for the Setting DAO, which creates it',
  evidence=C3_ORM + '; SRC common/AnyMemoDBOpenHelper.java:197 (getDao(Setting.class))', cls='non_standard', via='ORMLite DaoManager (reflection)')
e('AnyMemoDBOpenHelper.getLearningDataDao', 'LearningDataDaoImpl.<init>(ConnectionSource,DatabaseTableConfig)', 'FRAMEWORK', 'the first getLearningDataDao() call asks ORMLite for the LearningData DAO, which creates it',
  evidence=C3_ORM + '; SRC common/AnyMemoDBOpenHelper.java:230 (getDao(LearningData.class))', cls='non_standard', via='ORMLite DaoManager (reflection)')
e('AnyMemoDBOpenHelper.getLearningDataDao', 'LearningDataDaoImpl.<init>(ConnectionSource,Class)', 'FRAMEWORK', 'the first getLearningDataDao() call asks ORMLite for the LearningData DAO, which creates it',
  evidence=C3_ORM + '; SRC common/AnyMemoDBOpenHelper.java:230 (getDao(LearningData.class))', cls='non_standard', via='ORMLite DaoManager (reflection)')
e('AbstractHelperDaoImpl.<init>(ConnectionSource,DatabaseTableConfig)', 'AbstractHelperDaoImpl.<clinit>', 'LIFECYCLE', 'the JVM initialises the superclass before a DAO constructor runs the superclass constructor',
  evidence=C3_CLINIT + '; SRC dao/AbstractHelperDaoImpl.java')
e('AbstractHelperDaoImpl.<init>(ConnectionSource,Class)', 'AbstractHelperDaoImpl.<clinit>', 'LIFECYCLE', 'the JVM initialises the superclass before a DAO constructor runs the superclass constructor',
  evidence=C3_CLINIT + '; SRC dao/AbstractHelperDaoImpl.java')
UNREACHABLE['AnyMemoDBOpenHelper.getDeckDao'] = ('no_trigger_in_app', 'no code calls getDeckDao() (the declaration at common/AnyMemoDBOpenHelper.java:183 is the only mention), so no code asks ORMLite for the Deck DAO',
    'SRC common/AnyMemoDBOpenHelper.java:183', 'SOURCE')
UNREACHABLE['AnyMemoDBOpenHelper.getFilterDao'] = ('no_trigger_in_app', 'no code calls getFilterDao() (the declaration at common/AnyMemoDBOpenHelper.java:205 is the only mention), so no code asks ORMLite for the Filter DAO',
    'SRC common/AnyMemoDBOpenHelper.java:205', 'SOURCE')
for dao_key_ in ('DeckDaoImpl.<init>(ConnectionSource,Class)', 'DeckDaoImpl.<init>(ConnectionSource,DatabaseTableConfig)'):
    e('AnyMemoDBOpenHelper.onCreate', dao_key_, 'FRAMEWORK', 'onCreate builds the Deck table: TableUtils.createTable makes the Deck DAO through ORMLite DaoManager',
      evidence=C3_ORM + '; SRC common/AnyMemoDBOpenHelper.java:55', cls='non_standard', via='ORMLite DaoManager (reflection)')
for dao_key_ in ('FilterDaoImpl.<init>(ConnectionSource,Class)', 'FilterDaoImpl.<init>(ConnectionSource,DatabaseTableConfig)'):
    e('AnyMemoDBOpenHelper.onCreate', dao_key_, 'FRAMEWORK', 'onCreate builds the Filter table: TableUtils.createTable makes the Filter DAO through ORMLite DaoManager',
      evidence=C3_ORM + '; SRC common/AnyMemoDBOpenHelper.java:57', cls='non_standard', via='ORMLite DaoManager (reflection)')
UNREACHABLE['StatDaoImpl.<init>(ConnectionSource,Class)'] = ('no_trigger_in_app', 'no getStatDao() exists and no code calls getDao(Stat.class) or TableUtils for Stat (grep); ORMLite would create the DAO only when asked for it',
    'SRC dao/StatDaoImpl.java:12', 'SOURCE')
UNREACHABLE['StatDaoImpl.<init>(ConnectionSource,DatabaseTableConfig)'] = ('no_trigger_in_app', 'no getStatDao() exists and no code calls getDao(Stat.class) or TableUtils for Stat (grep); ORMLite would create the DAO only when asked for it',
    'SRC dao/StatDaoImpl.java:12', 'SOURCE')
UNREACHABLE['DaggerAppComponents.<init>'] = ('no_trigger_in_app', 'the generated Dagger root class is used only through its static builder; its constructor is never invoked (bytecode: no invoke site; the generated source is not in the build output)',
    'SRC modules/AppComponents.java:15', 'INFERRED')
UNREACHABLE['ActivityModules.<init>'] = ('no_trigger_in_app', 'every @Provides method of ActivityModules is static (first one at ActivityModules.java:25), so Dagger creates no module instance (bytecode: no invoke site)',
    'SRC modules/ActivityModules.java:25', 'INFERRED')
UNREACHABLE['AppModules.<init>'] = ('no_trigger_in_app', 'every @Provides method of AppModules is static (from AppModules.java:51) and the @Binds methods are abstract, so Dagger creates no module instance (bytecode: no invoke site)',
    'SRC modules/AppModules.java:51', 'INFERRED')
UNREACHABLE['AppModules.provideExecutorService'] = ('no_trigger_in_app', 'no @Inject field or call asks for an ExecutorService in the app (grep); AnyMemoExecutor creates its own executor (utils/AnyMemoExecutor.java:34)',
    'SRC modules/AppModules.java:51', 'SOURCE')
UNREACHABLE['AppModules_ProvideExecutorServiceFactory$InstanceHolder.<clinit>'] = ('no_trigger_in_app', 'the holder of provideExecutorService is initialised only when provideExecutorService is called, and no code path calls it (see AppModules.provideExecutorService)',
    'SRC modules/AppModules.java:51', 'INFERRED')
UNREACHABLE['AppModules_ProvideExecutorServiceFactory$InstanceHolder.<init>'] = ('no_trigger_in_app', 'javac default constructor of the Dagger holder of provideExecutorService (a class with one static INSTANCE field); nothing creates the holder (bytecode: no invoke site)',
    'SRC modules/AppModules.java:51', 'INFERRED')
UNREACHABLE['AppModules_ProvidesCSVExporterFactory$InstanceHolder.<init>'] = ('no_trigger_in_app', 'javac default constructor of the Dagger holder of providesCSVExporter (a class with one static INSTANCE field); nothing creates the holder (bytecode: no invoke site)',
    'SRC modules/AppModules.java:71', 'INFERRED')
UNREACHABLE['AppModules_ProvidesMnemosyneXMLExporterFactory$InstanceHolder.<init>'] = ('no_trigger_in_app', 'javac default constructor of the Dagger holder of providesMnemosyneXMLExporter (a class with one static INSTANCE field); nothing creates the holder (bytecode: no invoke site)',
    'SRC modules/AppModules.java:103', 'INFERRED')
UNREACHABLE['AppModules_ProvidesOkHttpClientFactory$InstanceHolder.<init>'] = ('no_trigger_in_app', 'javac default constructor of the Dagger holder of providesOkHttpClient (a class with one static INSTANCE field); nothing creates the holder (bytecode: no invoke site)',
    'SRC modules/AppModules.java:63', 'INFERRED')
UNREACHABLE['AppModules_ProvidesQATxtExporterFactory$InstanceHolder.<init>'] = ('no_trigger_in_app', 'javac default constructor of the Dagger holder of providesQATxtExporter (a class with one static INSTANCE field); nothing creates the holder (bytecode: no invoke site)',
    'SRC modules/AppModules.java:119', 'INFERRED')
UNREACHABLE['AppModules_ProvidesSupermemo2008XMLImporterFactory$InstanceHolder.<init>'] = ('no_trigger_in_app', 'javac default constructor of the Dagger holder of providesSupermemo2008XMLImporter (a class with one static INSTANCE field); nothing creates the holder (bytecode: no invoke site)',
    'SRC modules/AppModules.java:135', 'INFERRED')
UNREACHABLE['AppModules_ProvidesTabTxtExporterFactory$InstanceHolder.<init>'] = ('no_trigger_in_app', 'javac default constructor of the Dagger holder of providesTabTxtExporter (a class with one static INSTANCE field); nothing creates the holder (bytecode: no invoke site)',
    'SRC modules/AppModules.java:151', 'INFERRED')
UNREACHABLE['AppModules_ProvidesZipExporterFactory$InstanceHolder.<init>'] = ('no_trigger_in_app', 'javac default constructor of the Dagger holder of providesZipExporter (a class with one static INSTANCE field); nothing creates the holder (bytecode: no invoke site)',
    'SRC modules/AppModules.java:167', 'INFERRED')
UNREACHABLE['AppModules_ProvidesZipImporterFactory$InstanceHolder.<init>'] = ('no_trigger_in_app', 'javac default constructor of the Dagger holder of providesZipImporter (a class with one static INSTANCE field); nothing creates the holder (bytecode: no invoke site)',
    'SRC modules/AppModules.java:175', 'INFERRED')
e('AMApplication.activityComponents', 'DaggerAppComponents$AppComponentsImpl$1.get', 'FRAMEWORK', 'the ActivityComponents builder is obtained from the Dagger provider when a builder is needed',
  evidence=C3_PROVIDER + '; SRC common/AMApplication.java:81 (activityComponentsBuilder.get())', cls='non_standard', via='Dagger provider (javax.inject.Provider.get)')
e('DaggerAppComponents$ActivityComponentsImpl.fragmentsComponentsBuilder', 'DaggerAppComponents$ActivityComponentsImpl$1.get', 'FRAMEWORK', 'the component returns its fragment builder through the Dagger provider',
  evidence=C3_PROVIDER + '; generated class, no source line in the build output', cls='non_standard', via='Dagger provider (javax.inject.Provider.get)')
UNREACHABLE['DaggerAppComponents$ActivityComponentsImpl.inject(CardEditor)'] = ('no_trigger_in_app', 'CardEditor.onCreate never calls the component injector (no inject call in ui/CardEditor.java), so the member injector for CardEditor has no caller',
    'SRC ui/CardEditor.java:102', 'SOURCE')
e('CardEditor.<init>', 'CardEditor.<clinit>', 'LIFECYCLE', 'the JVM initialises CardEditor before its first constructor runs',
  evidence=C3_CLINIT + '; SRC ui/CardEditor.java:65 (class declaration)')
UNREACHABLE['DaggerAppComponents$AppComponentsImpl.inject(LearnQueueManagerLoader)'] = ('no_trigger_in_app', 'no code calls this component injector (no call site of inject with this loader; grep). The loader is created by the LoaderManager; the component declares the injector at modules/AppComponents.java:20',
    'SRC ui/StudyActivity.java:450', 'SOURCE')
UNREACHABLE['DaggerAppComponents$AppComponentsImpl.inject(QuizQueueManagerLoader)'] = ('no_trigger_in_app', 'no code calls this component injector (no call site of inject with this loader; grep). The loader is created by the LoaderManager; the component declares the injector at modules/AppComponents.java:22',
    'SRC ui/QuizActivity.java:229', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment$RequestTokenTask$1.<init>'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment$RequestTokenTask$1.onTouch'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment$RequestTokenTask$2.<init>'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment$RequestTokenTask$2.onPageFinished'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment$RequestTokenTask.<init>'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment$RequestTokenTask.doInBackground'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment$RequestTokenTask.onPostExecute'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment$RequestTokenTask.onPreExecute'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment.<init>'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment.getAuthCodeReceiveListener'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment.onAttach'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment.onCancel'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment.onCreate'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment.onCreateView'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccessCodeRetrievalFragment.setAuthCodeReceiveListener'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccessCodeRetrievalFragment has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccessCodeRetrievalFragment.java:43', 'SOURCE')
UNREACHABLE['OauthAccountActivity$1.<init>'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$1.onAuthCodeError'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$1.onAuthCodeReceived'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$1.onCancelled'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$2.<init>'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$2.onClick'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$GetAccessTokenTask.<init>'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$GetAccessTokenTask.doInBackground'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$GetAccessTokenTask.onPostExecute'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$GetAccessTokenTask.onPreExecute'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.<init>'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.doInBackground'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.onPostExecute'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.onPreExecute'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity.<init>'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity.invalidateSavedToken'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity.onCreate'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity.showAuthErrorDialog'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['OauthAccountActivity.showGetTokenDialog'] = ('no_trigger_in_app', 'Oauth1 island: OauthAccountActivity has no entry in AndroidManifest.xml and no other code starts it (OauthAccessCodeRetrievalFragment is referenced only from OauthAccountActivity, which nothing starts)',
    'SRC downloader/oauth/OauthAccountActivity.java:41', 'SOURCE')
UNREACHABLE['AnyMemoDBOpenHelperManager.<init>'] = ('no_trigger_in_app', 'every use of AnyMemoDBOpenHelperManager is a static call; the app never creates an instance (grep: no "new AnyMemoDBOpenHelperManager")',
    'SRC common/AnyMemoDBOpenHelperManager.java:20', 'SOURCE')
e('AnyMemo.onCreate', 'databinding.DataBinderMapperImpl.<init>', 'FRAMEWORK', 'setContentView with the data-binding layout main_tabs asks the library for the generated mapper',
  evidence=C3_DATABIND + '; SRC ui/AnyMemo.java:121 (R.layout.main_tabs); SRC res/layout/main_tabs.xml:3 (layout root)', cls='non_standard', via='androidx DataBindingUtil loads the generated mapper by name')
e('AnyMemo.onCreate', 'fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FRAMEWORK', 'the library asks the generated mapper for the Binding class of R.layout.main_tabs',
  evidence=C3_DATABIND + '; SRC ui/AnyMemo.java:121 (R.layout.main_tabs); SRC res/layout/main_tabs.xml:3 (layout root)', cls='non_standard', via='androidx DataBindingUtil -> generated getDataBinder')
e('AnyMemo.onCreate', 'MainTabsBindingImpl.<init>(DataBindingComponent,View)', 'FRAMEWORK', 'the layout main_tabs is bound to its generated Binding class (the switch in getDataBinder selects this class for this layout id)',
  evidence=C3_DATABIND + '; SRC ui/AnyMemo.java:121 (R.layout.main_tabs); SRC res/layout/main_tabs.xml:3 (layout root)', cls='non_standard', via='androidx DataBindingUtil -> generated getDataBinder')
sup(('fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'MainTabsBindingImpl.<init>(DataBindingComponent,View)'))
sup(('fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'MainTabsBindingImpl.<clinit>'))
e('MainTabsBindingImpl.<init>(DataBindingComponent,View)', 'MainTabsBindingImpl.<clinit>', 'LIFECYCLE', 'the JVM initialises MainTabsBindingImpl when its first instance is created',
  evidence=C3_CLINIT + '; SRC res/layout/main_tabs.xml:3 (generated Binding class of the layout)')
e('MainTabsBindingImpl.invalidateAll', 'MainTabsBindingImpl.executeBindings', 'FRAMEWORK', 'invalidateAll marks the binding dirty; the library runs executeBindings in its pending pass',
  evidence=C3_LIB_PENDING + '; the generated constructor calls invalidateAll (bytecode edge of MainTabsBindingImpl.<init>)', cls='non_standard', via='androidx ViewDataBinding pending-bindings pass')
e('MainTabsBindingImpl.invalidateAll', 'MainTabsBindingImpl.hasPendingBindings', 'FRAMEWORK', 'the library checks hasPendingBindings in the same pending pass',
  evidence=C3_LIB_PENDING + '; the generated constructor calls invalidateAll (bytecode edge of MainTabsBindingImpl.<init>)', cls='non_standard', via='androidx ViewDataBinding pending-bindings pass')
UNREACHABLE['MainTabsBindingImpl.setVariable'] = ('no_trigger_in_app', 'the app never calls setVariable on this binding (grep: no call); res/layout/main_tabs.xml declares no <variable>',
    'SRC res/layout/main_tabs.xml:3', 'SOURCE')
UNREACHABLE['MainTabsBindingImpl.onFieldChange'] = ('framework_never_calls', 'the library calls onFieldChange only when an observable field or a <variable> changes; res/layout/main_tabs.xml declares no <variable> (library source not read)',
    'SRC res/layout/main_tabs.xml:3', 'INFERRED')
e('DropboxListActivity.onCreate', 'databinding.DataBinderMapperImpl.<init>', 'FRAMEWORK', 'setContentView with the data-binding layout dropbox_list_activity asks the library for the generated mapper',
  evidence=C3_DATABIND + '; SRC downloader/dropbox/DropboxListActivity.java:38 (R.layout.dropbox_list_activity); SRC res/layout/dropbox_list_activity.xml:3 (layout root)', cls='non_standard', via='androidx DataBindingUtil loads the generated mapper by name')
e('DropboxListActivity.onCreate', 'fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FRAMEWORK', 'the library asks the generated mapper for the Binding class of R.layout.dropbox_list_activity',
  evidence=C3_DATABIND + '; SRC downloader/dropbox/DropboxListActivity.java:38 (R.layout.dropbox_list_activity); SRC res/layout/dropbox_list_activity.xml:3 (layout root)', cls='non_standard', via='androidx DataBindingUtil -> generated getDataBinder')
e('DropboxListActivity.onCreate', 'DropboxListActivityBindingImpl.<init>(DataBindingComponent,View)', 'FRAMEWORK', 'the layout dropbox_list_activity is bound to its generated Binding class (the switch in getDataBinder selects this class for this layout id)',
  evidence=C3_DATABIND + '; SRC downloader/dropbox/DropboxListActivity.java:38 (R.layout.dropbox_list_activity); SRC res/layout/dropbox_list_activity.xml:3 (layout root)', cls='non_standard', via='androidx DataBindingUtil -> generated getDataBinder')
sup(('fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DropboxListActivityBindingImpl.<init>(DataBindingComponent,View)'))
sup(('fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DropboxListActivityBindingImpl.<clinit>'))
e('DropboxListActivityBindingImpl.<init>(DataBindingComponent,View)', 'DropboxListActivityBindingImpl.<clinit>', 'LIFECYCLE', 'the JVM initialises DropboxListActivityBindingImpl when its first instance is created',
  evidence=C3_CLINIT + '; SRC res/layout/dropbox_list_activity.xml:3 (generated Binding class of the layout)')
e('DropboxListActivityBindingImpl.invalidateAll', 'DropboxListActivityBindingImpl.executeBindings', 'FRAMEWORK', 'invalidateAll marks the binding dirty; the library runs executeBindings in its pending pass',
  evidence=C3_LIB_PENDING + '; the generated constructor calls invalidateAll (bytecode edge of DropboxListActivityBindingImpl.<init>)', cls='non_standard', via='androidx ViewDataBinding pending-bindings pass')
e('DropboxListActivityBindingImpl.invalidateAll', 'DropboxListActivityBindingImpl.hasPendingBindings', 'FRAMEWORK', 'the library checks hasPendingBindings in the same pending pass',
  evidence=C3_LIB_PENDING + '; the generated constructor calls invalidateAll (bytecode edge of DropboxListActivityBindingImpl.<init>)', cls='non_standard', via='androidx ViewDataBinding pending-bindings pass')
UNREACHABLE['DropboxListActivityBindingImpl.setVariable'] = ('no_trigger_in_app', 'the app never calls setVariable on this binding (grep: no call); res/layout/dropbox_list_activity.xml declares no <variable>',
    'SRC res/layout/dropbox_list_activity.xml:3', 'SOURCE')
UNREACHABLE['DropboxListActivityBindingImpl.onFieldChange'] = ('framework_never_calls', 'the library calls onFieldChange only when an observable field or a <variable> changes; res/layout/dropbox_list_activity.xml declares no <variable> (library source not read)',
    'SRC res/layout/dropbox_list_activity.xml:3', 'INFERRED')
e('UploadDropboxActivity.onCreate', 'databinding.DataBinderMapperImpl.<init>', 'FRAMEWORK', 'setContentView with the data-binding layout upload_dropbox_screen asks the library for the generated mapper',
  evidence=C3_DATABIND + '; SRC downloader/dropbox/UploadDropboxActivity.java:47 (R.layout.upload_dropbox_screen); SRC res/layout/upload_dropbox_screen.xml:3 (layout root)', cls='non_standard', via='androidx DataBindingUtil loads the generated mapper by name')
e('UploadDropboxActivity.onCreate', 'fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FRAMEWORK', 'the library asks the generated mapper for the Binding class of R.layout.upload_dropbox_screen',
  evidence=C3_DATABIND + '; SRC downloader/dropbox/UploadDropboxActivity.java:47 (R.layout.upload_dropbox_screen); SRC res/layout/upload_dropbox_screen.xml:3 (layout root)', cls='non_standard', via='androidx DataBindingUtil -> generated getDataBinder')
e('UploadDropboxActivity.onCreate', 'UploadDropboxScreenBindingImpl.<init>(DataBindingComponent,View)', 'FRAMEWORK', 'the layout upload_dropbox_screen is bound to its generated Binding class (the switch in getDataBinder selects this class for this layout id)',
  evidence=C3_DATABIND + '; SRC downloader/dropbox/UploadDropboxActivity.java:47 (R.layout.upload_dropbox_screen); SRC res/layout/upload_dropbox_screen.xml:3 (layout root)', cls='non_standard', via='androidx DataBindingUtil -> generated getDataBinder')
sup(('fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'UploadDropboxScreenBindingImpl.<init>(DataBindingComponent,View)'))
sup(('fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'UploadDropboxScreenBindingImpl.<clinit>'))
e('UploadDropboxScreenBindingImpl.<init>(DataBindingComponent,View)', 'UploadDropboxScreenBindingImpl.<clinit>', 'LIFECYCLE', 'the JVM initialises UploadDropboxScreenBindingImpl when its first instance is created',
  evidence=C3_CLINIT + '; SRC res/layout/upload_dropbox_screen.xml:3 (generated Binding class of the layout)')
e('UploadDropboxScreenBindingImpl.invalidateAll', 'UploadDropboxScreenBindingImpl.executeBindings', 'FRAMEWORK', 'invalidateAll marks the binding dirty; the library runs executeBindings in its pending pass',
  evidence=C3_LIB_PENDING + '; the generated constructor calls invalidateAll (bytecode edge of UploadDropboxScreenBindingImpl.<init>)', cls='non_standard', via='androidx ViewDataBinding pending-bindings pass')
e('UploadDropboxScreenBindingImpl.invalidateAll', 'UploadDropboxScreenBindingImpl.hasPendingBindings', 'FRAMEWORK', 'the library checks hasPendingBindings in the same pending pass',
  evidence=C3_LIB_PENDING + '; the generated constructor calls invalidateAll (bytecode edge of UploadDropboxScreenBindingImpl.<init>)', cls='non_standard', via='androidx ViewDataBinding pending-bindings pass')
UNREACHABLE['UploadDropboxScreenBindingImpl.setVariable'] = ('no_trigger_in_app', 'the app never calls setVariable on this binding (grep: no call); res/layout/upload_dropbox_screen.xml declares no <variable>',
    'SRC res/layout/upload_dropbox_screen.xml:3', 'SOURCE')
UNREACHABLE['UploadDropboxScreenBindingImpl.onFieldChange'] = ('framework_never_calls', 'the library calls onFieldChange only when an observable field or a <variable> changes; res/layout/upload_dropbox_screen.xml declares no <variable> (library source not read)',
    'SRC res/layout/upload_dropbox_screen.xml:3', 'INFERRED')
UNREACHABLE['fantastischmemo.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View[],int)'] = ('framework_never_calls', 'the library calls the View[] variant only to bind the children of a <merge> root; the three layouts have a single <layout> root and no <merge> or <include> (res/layout/*.xml, grep)',
    'SRC res/layout/main_tabs.xml:3', 'INFERRED')
e('databinding.DataBinderMapperImpl.<init>', 'fantastischmemo.DataBinderMapperImpl.collectDependencies', 'FRAMEWORK', 'the data-binding library calls collectDependencies on the app mapper to load the mappers of other modules (AnyMemo has none)',
  evidence=C3_DATABIND + '; SRC res/layout/main_tabs.xml:3')
UNREACHABLE['fantastischmemo.DataBinderMapperImpl.convertBrIdToString'] = ('framework_never_calls', 'the library calls convertBrIdToString only to name a <variable> in an error message; the layouts declare no <variable> (library source not read)',
    'SRC res/layout/main_tabs.xml:3', 'INFERRED')
UNREACHABLE['fantastischmemo.DataBinderMapperImpl.getLayoutId'] = ('framework_never_calls', 'the library calls getLayoutId only while it binds the children of an <include> or <merge> layout (library source not read); the three layouts have neither (res/layout/*.xml)',
    'SRC res/layout/main_tabs.xml:3', 'INFERRED')
UNREACHABLE['fantastischmemo.DataBinderMapperImpl$InnerBrLookup.<clinit>'] = ('framework_never_calls', 'the static lookup table of BrLookup is initialised only by convertBrIdToString or getLayoutId, which no caller reaches (library source not read)',
    'SRC res/layout/main_tabs.xml:3', 'INFERRED')
UNREACHABLE['fantastischmemo.DataBinderMapperImpl$InnerBrLookup.<init>'] = ('no_trigger_in_app', 'javac default constructor of a static lookup holder; nothing creates it (bytecode: no invoke site)',
    'SRC res/layout/main_tabs.xml:3', 'INFERRED')
UNREACHABLE['fantastischmemo.DataBinderMapperImpl$InnerLayoutIdLookup.<clinit>'] = ('framework_never_calls', 'the static lookup table of LayoutIdLookup is initialised only by convertBrIdToString or getLayoutId, which no caller reaches (library source not read)',
    'SRC res/layout/main_tabs.xml:3', 'INFERRED')
UNREACHABLE['fantastischmemo.DataBinderMapperImpl$InnerLayoutIdLookup.<init>'] = ('no_trigger_in_app', 'javac default constructor of a static lookup holder; nothing creates it (bytecode: no invoke site)',
    'SRC res/layout/main_tabs.xml:3', 'INFERRED')
UNREACHABLE['baseAdapters.BR.<init>'] = ('no_trigger_in_app', 'the BR constants class is generated from the layout variables; nothing creates it (bytecode: no invoke site) and the three layouts declare no <variable>',
    'SRC res/layout/main_tabs.xml:3', 'INFERRED')
UNREACHABLE['fantastischmemo.BR.<init>'] = ('no_trigger_in_app', 'the BR constants class is generated from the layout variables; nothing creates it (bytecode: no invoke site) and the three layouts declare no <variable>',
    'SRC res/layout/main_tabs.xml:3', 'INFERRED')
e('DaggerAppComponents$AppComponentsImpl.injectAMApplication', 'NotificationChannelUtil.<init>', 'CALL', 'Dagger creates the @Inject field notificationChannelUtil of AMApplication',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC common/AMApplication.java:40 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectAbstractDownloaderFragment', 'RecentListUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListUtil of AbstractDownloaderFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/common/AbstractDownloaderFragment.java:70 (@Inject field)')
e('RecentListUtil.<init>', 'Option.<init>', 'CALL', 'Dagger passes the Option dependency of the @Inject constructor of RecentListUtil',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC utils/RecentListUtil.java:44 (@Inject constructor)')
e('DaggerAppComponents$AppComponentsImpl.injectAlarmReceiver', 'NotificationUtil.<init>', 'CALL', 'Dagger creates the @Inject field notificationUtil of AlarmReceiver',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC receiver/AlarmReceiver.java:41 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectAnyMemo', 'AMFileUtil.<init>', 'CALL', 'Dagger creates the @Inject field amFileUtil of AnyMemo',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/AnyMemo.java:92 (@Inject field)')
e('AMFileUtil.<init>', 'AMPrefUtil.<init>', 'CALL', 'Dagger passes the AMPrefUtil dependency of the @Inject constructor of AMFileUtil',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC utils/AMFileUtil.java:52 (@Inject constructor)')
e('DaggerAppComponents$ActivityComponentsImpl.injectAnyMemo', 'RecentListUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListUtil of AnyMemo',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/AnyMemo.java:94 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectAnyMemo', 'DatabaseUtil.<init>', 'CALL', 'Dagger creates the @Inject field databaseUtil of AnyMemo',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/AnyMemo.java:96 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectAnyMemo', 'ActivityModules.providesMultipleLoaderManager', 'CALL', 'Dagger creates the @Inject field multipleLoaderManager of AnyMemo',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/AnyMemo.java:98 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectAnyMemo', 'AboutUtil.<init>', 'CALL', 'Dagger creates the @Inject field aboutUtil of AnyMemo',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/AnyMemo.java:100 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectAnyMemo', 'RecentListActionModeUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListActionModeUtil of AnyMemo',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/AnyMemo.java:102 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectAnyMemo', 'DatabaseOperationDialogUtil.<init>', 'CALL', 'Dagger creates the @Inject field databaseOperationDialogUtil of AnyMemo',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/AnyMemo.java:104 (@Inject field)')
e('DatabaseOperationDialogUtil.<init>', 'AMFileUtil.<init>', 'CALL', 'Dagger passes the AMFileUtil dependency of the @Inject constructor of DatabaseOperationDialogUtil',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC utils/DatabaseOperationDialogUtil.java:30 (@Inject constructor)')
e('DatabaseOperationDialogUtil.<init>', 'RecentListUtil.<init>', 'CALL', 'Dagger passes the RecentListUtil dependency of the @Inject constructor of DatabaseOperationDialogUtil',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC utils/DatabaseOperationDialogUtil.java:30 (@Inject constructor)')
e('DaggerAppComponents$ActivityComponentsImpl.injectAnyMemo', 'NotificationUtil.<init>', 'CALL', 'Dagger creates the @Inject field notificationUtil of AnyMemo',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/AnyMemo.java:106 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectAnyMemo', 'FolderImportExportUtil.<init>', 'CALL', 'Dagger creates the @Inject field folderImportExportUtil of AnyMemo',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/AnyMemo.java:108 (@Inject field)')
e('FolderImportExportUtil.<init>', 'RecentListUtil.<init>', 'CALL', 'Dagger passes the RecentListUtil dependency of the @Inject constructor of FolderImportExportUtil',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC utils/FolderImportExportUtil.java:34 (@Inject constructor)')
e('DaggerAppComponents$FragmentComponentsImpl.injectAnyMemoDownloaderFragment', 'DownloaderUtils.<init>', 'CALL', 'Dagger creates the @Inject field downloaderUtils of AnyMemoDownloaderFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/anymemo/AnyMemoDownloaderFragment.java:33 (@Inject field)')
e('DownloaderUtils.<init>', 'AppModules.providesOkHttpClient', 'CALL', 'Dagger passes the OkHttpClient dependency of the @Inject constructor of DownloaderUtils',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/common/DownloaderUtils.java:52 (@Inject constructor)')
e('DownloaderUtils.<init>', 'AMFileUtil.<init>', 'CALL', 'Dagger passes the AMFileUtil dependency of the @Inject constructor of DownloaderUtils',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/common/DownloaderUtils.java:52 (@Inject constructor)')
e('DaggerAppComponents$FragmentComponentsImpl.injectCardFragment', 'AMFileUtil.<init>', 'CALL', 'Dagger creates the @Inject field amFileUtil of CardFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/CardFragment.java:53 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectCardListActivity', 'ActivityModules.providesMultipleLoaderManager', 'CALL', 'Dagger creates the @Inject field multipleLoaderManager of CardListActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/CardListActivity.java:102 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectCardListActivity', 'DefaultScheduler.<init>', 'CALL', 'Dagger creates the @Inject field scheduler of CardListActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/CardListActivity.java:104 (@Inject field)')
e('DefaultScheduler.<init>', 'SchedulingAlgorithmParameters.<init>', 'CALL', 'Dagger passes the SchedulingAlgorithmParameters dependency of the @Inject constructor of DefaultScheduler',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC scheduler/DefaultScheduler.java:45 (@Inject constructor)')
e('DaggerAppComponents$ActivityComponentsImpl.injectCardListActivity', 'AMPrefUtil.<init>', 'CALL', 'Dagger creates the @Inject field amPrefUtil of CardListActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/CardListActivity.java:106 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectCardListActivity', 'SchedulingAlgorithmParameters.<init>', 'CALL', 'Dagger creates the @Inject field schedulingAlgorithmParameters of CardListActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/CardListActivity.java:108 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectCardListActivity', 'AMFileUtil.<init>', 'CALL', 'Dagger creates the @Inject field amFileUtil of CardListActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/CardListActivity.java:110 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectCardPlayerFragment', 'Option.<init>', 'CALL', 'Dagger creates the @Inject field option of CardPlayerFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/CardPlayerFragment.java:62 (@Inject field)')
e('DaggerAppComponents$AppComponentsImpl.injectCardPlayerService', 'Option.<init>', 'CALL', 'Dagger creates the @Inject field option of CardPlayerService',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC service/CardPlayerService.java:74 (@Inject field)')
e('DaggerAppComponents$AppComponentsImpl.injectConvertIntentService', 'RecentListUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListUtil of ConvertIntentService',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC service/ConvertIntentService.java:67 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectConverterFragment', 'AMFileUtil.<init>', 'CALL', 'Dagger creates the @Inject field amFileUtil of ConverterFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/ConverterFragment.java:55 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectDatabaseMerger', 'DatabaseUtil.<init>', 'CALL', 'Dagger creates the @Inject field databaseUtil of DatabaseMerger',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/DatabaseMerger.java:50 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectDropboxListFragment', 'DropboxApiHelper.<init>', 'CALL', 'Dagger creates the @Inject field dropboxApiHelper of DropboxListFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/dropbox/DropboxListFragment.java:41 (@Inject field)')
e('DropboxApiHelper.<init>', 'AMFileUtil.<init>', 'CALL', 'Dagger passes the AMFileUtil dependency of the @Inject constructor of DropboxApiHelper',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/dropbox/DropboxApiHelper.java:66 (@Inject constructor)')
e('DropboxApiHelper.<init>', 'AppModules.providesOkHttpClient', 'CALL', 'Dagger passes the OkHttpClient dependency of the @Inject constructor of DropboxApiHelper',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/dropbox/DropboxApiHelper.java:66 (@Inject constructor)')
e('DropboxApiHelper.<init>', 'RecentListUtil.<init>', 'CALL', 'Dagger passes the RecentListUtil dependency of the @Inject constructor of DropboxApiHelper',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/dropbox/DropboxApiHelper.java:66 (@Inject constructor)')
e('DaggerAppComponents$ActivityComponentsImpl.injectDropboxOauth2AccountActivity', 'DropboxApiHelper.<init>', 'CALL', 'Dagger creates the @Inject field dropboxApiHelper of DropboxOauth2AccountActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/dropbox/DropboxOauth2AccountActivity.java:16 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectFileBrowserFragment', 'AMFileUtil.<init>', 'CALL', 'Dagger creates the @Inject field amFileUtil of FileBrowserFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/FileBrowserFragment.java:114 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectFileBrowserFragment', 'RecentListUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListUtil of FileBrowserFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/FileBrowserFragment.java:116 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectFileBrowserFragment', 'DatabaseOperationDialogUtil.<init>', 'CALL', 'Dagger creates the @Inject field databaseOperationDialogUtil of FileBrowserFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/FileBrowserFragment.java:118 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectGestureSelectionDialogFragment', 'AMUiUtil.<init>', 'CALL', 'Dagger creates the @Inject field amUiUtil of GestureSelectionDialogFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/GestureSelectionDialogFragment.java:72 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectGestureSelectionDialogFragment', 'Option.<init>', 'CALL', 'Dagger creates the @Inject field option of GestureSelectionDialogFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/GestureSelectionDialogFragment.java:74 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectGradeButtonsFragment', 'DefaultScheduler.<init>', 'CALL', 'Dagger creates the @Inject field scheduler of GradeButtonsFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/GradeButtonsFragment.java:81 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectGradeButtonsFragment', 'AMDateUtil.<init>', 'CALL', 'Dagger creates the @Inject field amDateUtil of GradeButtonsFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/GradeButtonsFragment.java:83 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectGradeButtonsFragment', 'Option.<init>', 'CALL', 'Dagger creates the @Inject field option of GradeButtonsFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/GradeButtonsFragment.java:85 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectMiscTabFragment', 'RecentListUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListUtil of MiscTabFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/MiscTabFragment.java:98 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectMiscTabFragment', 'AMFileUtil.<init>', 'CALL', 'Dagger creates the @Inject field amFileUtil of MiscTabFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/MiscTabFragment.java:99 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectMiscTabFragment', 'DatabaseImportUtil.<init>', 'CALL', 'Dagger creates the @Inject field databaseImportUtil of MiscTabFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/MiscTabFragment.java:100 (@Inject field)')
e('DatabaseImportUtil.<init>', 'AMFileUtil.<init>', 'CALL', 'Dagger passes the AMFileUtil dependency of the @Inject constructor of DatabaseImportUtil',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC utils/DatabaseImportUtil.java:31 (@Inject constructor)')
e('DatabaseImportUtil.<init>', 'RecentListUtil.<init>', 'CALL', 'Dagger passes the RecentListUtil dependency of the @Inject constructor of DatabaseImportUtil',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC utils/DatabaseImportUtil.java:31 (@Inject constructor)')
e('DaggerAppComponents$FragmentComponentsImpl.injectMiscTabFragment', 'FolderImportExportUtil.<init>', 'CALL', 'Dagger creates the @Inject field folderImportExportUtil of MiscTabFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/MiscTabFragment.java:101 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectMiscTabFragment', 'AboutUtil.<init>', 'CALL', 'Dagger creates the @Inject field aboutUtil of MiscTabFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/MiscTabFragment.java:124 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectOauth2AccountActivity', 'Oauth2TokenUtil.<init>', 'CALL', 'Dagger creates the @Inject field oauth2TokenUtil of Oauth2AccountActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/oauth/Oauth2AccountActivity.java:27 (@Inject field)')
e('Oauth2TokenUtil.<init>', 'AppModules.providesSharedPreferences', 'CALL', 'Dagger passes the SharedPreferences dependency of the @Inject constructor of Oauth2TokenUtil',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/oauth/Oauth2TokenUtil.java:22 (@Inject constructor)')
e('DaggerAppComponents$FragmentComponentsImpl.injectOpenActionsFragment', 'AMFileUtil.<init>', 'CALL', 'Dagger creates the @Inject field amFileUtil of OpenActionsFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/OpenActionsFragment.java:59 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectOpenActionsFragment', 'RecentListUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListUtil of OpenActionsFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/OpenActionsFragment.java:61 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectOpenActionsFragment', 'ActivityModules.providesShareUtil', 'CALL', 'Dagger creates the @Inject field shareUtil of OpenActionsFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/OpenActionsFragment.java:63 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectOpenActionsFragment', 'AMPrefUtil.<init>', 'CALL', 'Dagger creates the @Inject field amPrefUtil of OpenActionsFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/OpenActionsFragment.java:65 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectPreviewEditActivity', 'ActivityModules.providesShareUtil', 'CALL', 'Dagger creates the @Inject field shareUtil of PreviewEditActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/PreviewEditActivity.java:88 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectPreviewEditActivity', 'AMPrefUtil.<init>', 'CALL', 'Dagger creates the @Inject field amPrefUtil of PreviewEditActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/PreviewEditActivity.java:90 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectQACardActivity', 'ActivityModules.providesMultipleLoaderManager', 'CALL', 'Dagger creates the @Inject field multipleLoaderManager of QACardActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/QACardActivity.java:113 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectQACardActivity', 'AMFileUtil.<init>', 'CALL', 'Dagger creates the @Inject field amFileUtil of QACardActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/QACardActivity.java:115 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectQACardActivity', 'Option.<init>', 'CALL', 'Dagger creates the @Inject field option of QACardActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/QACardActivity.java:117 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectQACardActivity', 'NotificationUtil.<init>', 'CALL', 'Dagger creates the @Inject field notificationUtil of QACardActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/QACardActivity.java:119 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectQuizActivity', 'ActivityModules.providesDictionaryUtil', 'CALL', 'Dagger creates the @Inject field dictionaryUtil of QuizActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/QuizActivity.java:69 (@Inject field)')
e('ActivityModules.providesDictionaryUtil', 'Option.<init>', 'CALL', 'Dagger passes the Option parameter of ActivityModules.providesDictionaryUtil',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC modules/ActivityModules.java:35 (@Provides parameter)')
e('DaggerAppComponents$ActivityComponentsImpl.injectQuizActivity', 'DefaultScheduler.<init>', 'CALL', 'Dagger creates the @Inject field scheduler of QuizActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/QuizActivity.java:71 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectQuizLauncherDialogFragment', 'AMPrefUtil.<init>', 'CALL', 'Dagger creates the @Inject field amPrefUtil of QuizLauncherDialogFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/QuizLauncherDialogFragment.java:116 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectRecentListFragment', 'RecentListUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListUtil of RecentListFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/RecentListFragment.java:99 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectRecentListFragment', 'DatabaseUtil.<init>', 'CALL', 'Dagger creates the @Inject field databaseUtil of RecentListFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/RecentListFragment.java:101 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectRecentListFragment', 'RecentListActionModeUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListActionModeUtil of RecentListFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/RecentListFragment.java:103 (@Inject field)')
e('DaggerAppComponents$FragmentComponentsImpl.injectRecentListFragment', 'DatabaseImportUtil.<init>', 'CALL', 'Dagger creates the @Inject field databaseImportUtil of RecentListFragment',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/RecentListFragment.java:105 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectSettingsScreen', 'DatabaseUtil.<init>', 'CALL', 'Dagger creates the @Inject field databaseUtil of SettingsScreen',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/SettingsScreen.java:120 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectSettingsScreen', 'ActivityModules.providesMultipleLoaderManager', 'CALL', 'Dagger creates the @Inject field multipleLoaderManager of SettingsScreen',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/SettingsScreen.java:122 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectShareScreen', 'RecentListUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListUtil of ShareScreen',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/ShareScreen.java:61 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectStudyActivity', 'DefaultScheduler.<init>', 'CALL', 'Dagger creates the @Inject field scheduler of StudyActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/StudyActivity.java:93 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectStudyActivity', 'ActivityModules.providesDictionaryUtil', 'CALL', 'Dagger creates the @Inject field dictionaryUtil of StudyActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/StudyActivity.java:95 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectStudyActivity', 'ActivityModules.providesShareUtil', 'CALL', 'Dagger creates the @Inject field shareUtil of StudyActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/StudyActivity.java:97 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectStudyActivity', 'SchedulingAlgorithmParameters.<init>', 'CALL', 'Dagger creates the @Inject field schedulingAlgorithmParameters of StudyActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC ui/StudyActivity.java:99 (@Inject field)')
e('DaggerAppComponents$ActivityComponentsImpl.injectUploadDropboxActivity', 'DropboxApiHelper.<init>', 'CALL', 'Dagger creates the @Inject field dropboxApiHelper of UploadDropboxActivity',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC downloader/dropbox/UploadDropboxActivity.java:32 (@Inject field)')
e('DaggerAppComponents$AppComponentsImpl.injectWidgetRemoteViewsFactory', 'RecentListUtil.<init>', 'CALL', 'Dagger creates the @Inject field recentListUtil of WidgetRemoteViewsFactory',
  cls='non_standard', via='Dagger (DI; generated injector and provider code)', evidence=FW_DAGGER + 'SRC widget/WidgetRemoteViewsFactory.java:31 (@Inject field)')
# ---- end pass 2 chunk 3 ----
# ---- section L part 2, pass 2, chunk 4 (2026-10-26) ----
# Chunk 4 (step 1, pass 2). Every entry was checked in the app source under
# org/liberty/android/fantastischmemo/ or in the AOSP 8.1.0_r1 copy in work/fw_src/.
# Auto edges from the bytecode extractor already cover: Dagger inject(CardFragment) and
# injectCardFragment (from CardFragment.onCreate), CardListAdapter.getView -> DefaultScheduler.isCardForReview,
# CardFragment.onCreateView and CardListAdapter.getView -> CardTextUtil.getSpannableText, and
# getSpannableText -> AMStringUtils.isHTML. Those are not repeated here.

C4_FINAL = ('INFERRED the JVM calls finalize() on an object after the garbage collector finds it unreachable '
            '(finalizer rule; the JVM specification is not read in this build)')
C4_CLINIT_VIA = 'JVM class initialiser (class-initialiser rule, INFERRED)'
DB_NEW_OR_CHANGED = state_text('the database file is new or its schema version changed (fresh install, upgrade or downgrade)', ('data',))

# ---- A. database open: the first DAO request opens the database through SQLiteOpenHelper ----
e('AnyMemoDBOpenHelper.getCardDao', 'AnyMemoDBOpenHelper.onCreate', 'FRAMEWORK',
  'the first DAO request opens the database; when the file is new, SQLiteOpenHelper calls onCreate',
  needs_state=DB_NEW_OR_CHANGED, cls='non_standard', via='ORMLite opens the database through SQLiteOpenHelper',
  evidence=FW_ORMLITE + '; FW-SRC core/java/android/database/sqlite/SQLiteOpenHelper.java:333 (onCreate called)')
e('AnyMemoDBOpenHelper.getCardDao', 'AnyMemoDBOpenHelper.onDowngrade', 'FRAMEWORK',
  'the first DAO request opens the database; when the stored schema version is newer, SQLiteOpenHelper calls onDowngrade',
  needs_state=DB_NEW_OR_CHANGED, cls='non_standard', via='ORMLite opens the database through SQLiteOpenHelper',
  evidence=FW_ORMLITE + '; FW-SRC core/java/android/database/sqlite/SQLiteOpenHelper.java:336 (onDowngrade called)')
e('AnyMemoDBOpenHelper.getCardDao', 'AnyMemoDBOpenHelper.onUpgrade', 'FRAMEWORK',
  'the first DAO request opens the database; when the stored schema version is older, SQLiteOpenHelper calls onUpgrade',
  needs_state=DB_NEW_OR_CHANGED, cls='non_standard', via='ORMLite opens the database through SQLiteOpenHelper',
  evidence=FW_ORMLITE + '; FW-SRC core/java/android/database/sqlite/SQLiteOpenHelper.java:338 (onUpgrade called)')
e('AnyMemoDBOpenHelper.onCreate', 'Setting.<init>', 'CALL',
  'onCreate saves the default settings row',
  evidence='SRC common/AnyMemoDBOpenHelper.java:61 (getSettingDao().create(new Setting()))')
e('AnyMemoDBOpenHelper.onCreate', 'AnyMemoDBOpenHelper.convertOldDatabase', 'CALL',
  'onCreate converts an old database file when its version is 0',
  evidence='SRC common/AnyMemoDBOpenHelper.java:65 (if database.getVersion() == 0)')
e('AnyMemoDBOpenHelper.getCardDao', 'AbstractHelperDaoImpl.setHelper', 'CALL',
  'getCardDao gives the new Card DAO the helper it uses to reach the database',
  evidence='SRC common/AnyMemoDBOpenHelper.java:175 (cardDao.setHelper(this))', cls='non_standard',
  via='CardDao interface; setHelper is inherited from AbstractHelperDaoImpl (interface dispatch not followed)')
e('AnyMemoDBOpenHelper.<init>', 'AnyMemoDBOpenHelper.finalize', 'LIFECYCLE',
  'the garbage collector finalizes the helper after the app stops using it',
  cls='non_standard', via='JVM finalizer rule', evidence=C4_FINAL + '; SRC common/AnyMemoDBOpenHelper.java:242')
e('CardTTSUtil.<init>', 'CardTTSUtil.finalize', 'LIFECYCLE',
  'the garbage collector finalizes the TTS helper after the app stops using it',
  cls='non_standard', via='JVM finalizer rule', evidence=C4_FINAL + '; SRC utils/CardTTSUtil.java:134')

# ---- B. DAO call sites: the bytecode extractor does not follow DAO interface calls ----
C4_DAO_SITES = [
    ('DetailScreen$InitTask.doInBackground', 'refresh', 'ui/DetailScreen.java:270-271'),
    ('CardEditor$InitTask.doInBackground', 'refresh', 'ui/CardEditor.java:539'),
    ('Mnemosyne2CardsExporter.createXMLFile', 'countOf', 'converter/Mnemosyne2CardsExporter.java:129'),
    ('Mnemosyne2CardsExporter.createXMLFile', 'refresh', 'converter/Mnemosyne2CardsExporter.java:169-170'),
    ('MnemosyneXMLExporter$1.call', 'queryForAll', 'converter/MnemosyneXMLExporter.java:54'),
    ('MnemosyneXMLExporter$1.call', 'refresh', 'converter/MnemosyneXMLExporter.java:56-57'),
    ('CSVExporter$1.call', 'queryForAll', 'converter/CSVExporter.java:66'),
    ('CSVExporter$1.call', 'refresh', 'converter/CSVExporter.java:72'),
    ('DatabaseUtil$1.call', 'queryForAll', 'utils/DatabaseUtil.java:57'),
    ('DatabaseUtil$1.call', 'refresh', 'utils/DatabaseUtil.java:65-66'),
    ('LearnQueueManager.position', 'refresh', 'queue/LearnQueueManager.java:237'),
    ('CardPlayerState.findNextCard', 'refresh', 'service/cardplayer/CardPlayerState.java:229-230'),
    ('CardPlayerState.findPrevCard', 'refresh', 'service/cardplayer/CardPlayerState.java:251-252'),
    ('GradeButtonsFragment$GradeTask.doInBackground', 'refresh', 'ui/GradeButtonsFragment.java:283'),
    ('PreviewEditActivity.onPostInit', 'countOf', 'ui/PreviewEditActivity.java:158'),
    ('CardPlayerActivity.onPostInit', 'countOf', 'ui/CardPlayerActivity.java:109'),
    ('CardWrapperListLoader.dbLoadInBackground', 'countOf', 'ui/loader/CardWrapperListLoader.java:43'),
    ('CategoryEditorFragment$InitTask.doInBackground', 'queryForAll', 'ui/CategoryEditorFragment.java:147'),
]
for _src, _meth, _ref in C4_DAO_SITES:
    e(_src, 'AbstractHelperDaoImpl.' + _meth, 'CALL',
      'the code calls ' + _meth + ' on a DAO; the DAO runs the inherited AbstractHelperDaoImpl method',
      evidence='SRC ' + _ref, cls='non_standard',
      via='DAO interface dispatch to the inherited AbstractHelperDaoImpl method (not followed by the bytecode extractor)')

# ---- C. class initialisers: the JVM runs <clinit> before the first constructor call ----
C4_CLINIT_SITES = [
    ('AlarmReceiver', 'receiver/AlarmReceiver.java:35'),
    ('CardPlayerService', 'service/CardPlayerService.java:49'),
    ('ConvertIntentService', 'service/ConvertIntentService.java:48'),
    ('CardListActivity', 'ui/CardListActivity.java:77'),
    ('DatabaseMerger', 'ui/DatabaseMerger.java:39'),
    ('DownloaderUtils', 'downloader/common/DownloaderUtils.java:45'),
    ('NotificationUtil', 'utils/NotificationUtil.java:28'),
    ('PreviewEditActivity', 'ui/PreviewEditActivity.java:61'),
    ('SettingsScreen', 'ui/SettingsScreen.java:69'),
]
for _c, _ref in C4_CLINIT_SITES:
    e(_c + '.<init>', _c + '.<clinit>', 'LIFECYCLE',
      'the JVM runs the static initialiser of ' + _c + ' before its first constructor call',
      cls='non_standard', via=C4_CLINIT_VIA, evidence=C3_CLINIT + '; SRC ' + _ref)

# ---- D. fragments, views and menus (framework callbacks) ----
C4_CARD_CB = [
    ('onAttach', 'ui/CardFragment.java:109'),
    ('onCreate', 'ui/CardFragment.java:100'),
    ('onCreateView', 'ui/CardFragment.java:114'),
    ('onCreateAnimation', 'ui/CardFragment.java:202'),
]
for _name, _ref in C4_CARD_CB:
    e('CardFragment.<init>', 'CardFragment.' + _name, 'FRAMEWORK',
      'the fragment manager calls ' + _name + ' on the new fragment',
      cls='non_standard', via='androidx FragmentManager lifecycle (library)', evidence=FW_FRAG + '; SRC ' + _ref)

e('CardTextUtil.getSpannableText', 'CardImageGetter.getDrawable', 'FRAMEWORK',
  'Html.fromHtml asks the image getter for the drawable of each image tag in the card text',
  cls='non_standard', via='android.text.Html calls the ImageGetter it is given (platform source not read)',
  evidence='INFERRED android.text.Html.fromHtml calls ImageGetter.getDrawable (platform Html source not read); SRC utils/CardTextUtil.java:58, 60')

e('CardListActivity$11.run', 'CardListActivity$CardListAdapter.getView', 'FRAMEWORK',
  'the list view asks the adapter for the view of each visible row',
  cls='non_standard', via='AbsListView.obtainView calls the adapter getView',
  evidence='FW-SRC core/java/android/widget/AbsListView.java:2335 (obtainView) and :2365 (mAdapter.getView); SRC ui/CardListActivity.java:645 (listView.setAdapter)')
C4_SECTION_CB = [
    ('getSections', 'FW-SRC core/java/android/widget/FastScroller.java:969, 974 (getSections)'),
    ('getPositionForSection', 'FW-SRC core/java/android/widget/FastScroller.java:1000, 1016 (getPositionForSection)'),
    ('getSectionForPosition', 'FW-SRC core/java/android/widget/FastScroller.java:1288 (getSectionForPosition)'),
]
for _name, _ref in C4_SECTION_CB:
    e('CardListActivity$11.run', 'CardListActivity$CardListAdapter.' + _name, 'FRAMEWORK',
      'the fast scroller asks the adapter for its section index',
      cls='non_standard', via='FastScroller calls the SectionIndexer methods of the adapter',
      evidence=_ref + '; SRC ui/CardListActivity.java:647 (setFastScrollEnabled(true))')

# S3 (round 1): onCreateView sets an EMPTY adapter (RecentListFragment.java:179-182) and loads no rows. The recycler view
# still asks the adapter for its item count, and the decoration for offsets and draws, during layout, so those stay here.
# onCreateViewHolder and onBindViewHolder are NOT called from onCreateView: rows exist only after setItems (see below).
for _name, _ref in [
        ('RecentListFragment$RecentListAdapter.getItemCount', 'SRC ui/RecentListFragment.java:182 (setAdapter)'),
        ('RecentListFragment$DividerItemDecoration.onDraw', 'SRC ui/RecentListFragment.java:174 (addItemDecoration)'),
        ('RecentListFragment$DividerItemDecoration.getItemOffsets', 'SRC ui/RecentListFragment.java:174 (addItemDecoration)')]:
    e('RecentListFragment.onCreateView', _name, 'FRAMEWORK',
      'the recycler view calls the adapter or decoration callbacks while it lays out and draws the rows',
      cls='non_standard', via='RecyclerView calls the adapter and decoration callbacks (androidx library)',
      evidence=FW_RECYCLER + '; ' + _ref)

# S3 (round 1): rows arrive only through setItems (RecentListFragment.java:464-468), which the two loader callbacks call
# (their guards are on the auto CALL edges, in GATE). setItems calls notifyDataSetChanged; the recycler view then creates
# and binds the row views (INFERRED androidx).
for _name in ('onCreateViewHolder', 'onBindViewHolder'):
    e('RecentListFragment$RecentListAdapter.setItems', 'RecentListFragment$RecentListAdapter.' + _name, 'FRAMEWORK',
      'notifyDataSetChanged: the recycler view creates and binds the row views (' + _name + ')',
      needs_state=NEED_RECENT, cls='non_standard', via='RecyclerView lays out the rows after notifyDataSetChanged (androidx library)',
      evidence=FW_RECYCLER + '; SRC ui/RecentListFragment.java:464-468')

e('RecentListFragment.onCreateOptionsMenu', 'RecentListFragment.onOptionsItemSelected', 'FRAMEWORK',
  'the options menu passes the tapped item to the fragment',
  cls='non_standard', via='options menu machinery (AppCompat, library)',
  evidence=FW_MENU + '; SRC ui/RecentListFragment.java:223 (inflate R.menu.open_screen_menu), :228')

for _name, _ln in [('onPrepareActionMode', 117), ('onActionItemClicked', 122), ('onDestroyActionMode', 136)]:
    e('RecentListActionModeUtil$ActionModeCallback.onCreateActionMode',
      'RecentListActionModeUtil$ActionModeCallback.' + _name, 'FRAMEWORK',
      'the action bar calls ' + _name + ' on the action mode callback',
      cls='non_standard', via='ActionMode (AppCompat, library)',
      evidence=FW_ACTIONMODE + '; SRC utils/RecentListActionModeUtil.java:' + str(_ln))

# ---- E. results of startActivityForResult ----
C4_RESULTS = [
    ('MiscTabFragment.onClick', 'MiscTabFragment.onActivityResult',
     'ui/MiscTabFragment.java:251, 259, 263 (startActivityForResult) and :417 (onActivityResult)'),
    ('MiscTabFragment.launchImportConvert', 'MiscTabFragment.onActivityResult',
     'ui/MiscTabFragment.java:413 (startActivityForResult) and :417 (onActivityResult)'),
    ('ConverterFragment.startConversion', 'ConverterFragment.onActivityResult',
     'ui/ConverterFragment.java:134 (startActivityForResult) and :139 (onActivityResult)'),
    ('ShareScreen.onClick', 'ShareScreen.onActivityResult',
     'ui/ShareScreen.java:132 (startActivityForResult) and :142 (onActivityResult)'),
    ('ExportAnyMemoDbFragment.exportDatabase', 'ExportAnyMemoDbFragment.onActivityResult',
     'ui/ExportAnyMemoDbFragment.java:51 (startActivityForResult) and :63 (onActivityResult)'),
]
for _s, _d, _ref in C4_RESULTS:
    e(_s, _d, 'RESULT', 'the started activity or picker finishes and returns its result to the caller',
      evidence=FW_RESULT + '; SRC ' + _ref)

# ---- E2. group 6 (2026-10-26): RESULT edges for the starters that section E does not list.
# FW_RESULT: the framework delivers a result to the activity that made the start, so each RESULT edge goes to the
# onActivityResult of the STARTER's own class (the cold-start LIFECYCLE shortcut to onActivityResult was removed).
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'editmenu_settings_id: startActivityForResult(SettingsScreen) returns',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:269-273')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'editmenu_detail_id: startActivityForResult(DetailScreen) returns', guard='getCurrentCard() != null',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:277-284')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'editmenu_list_id: startActivityForResult(CardListActivity) returns',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:285-294')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'menu_card_player: startActivityForResult(CardPlayerActivity) returns', guard='getCurrentCard() != null',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:307-316')
e('PreviewEditActivity.onOptionsItemSelected', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'menu_context_merge_db: startActivityForResult(DatabaseMerger) returns',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:400-404')
e('PreviewEditActivity$9.onClick', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'newButtonListener: startActivityForResult(CardEditor, isEditNew=true) returns',
  evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:606-616')
e('PreviewEditActivity$10.onClick', 'PreviewEditActivity.onActivityResult', 'RESULT',
  'editButtonListener: startActivityForResult(CardEditor, isEditNew=false) returns', guard='getCurrentCard() != null',
  needs_state=NEED_CARD, evidence=FW_RESULT + '; SRC ui/PreviewEditActivity.java:618-628')
e('StudyActivity.gotoSettings', 'StudyActivity.onActivityResult', 'RESULT',
  'menusettings: startActivityForResult(SettingsScreen) returns',
  evidence=FW_RESULT + '; SRC ui/StudyActivity.java:719-723')
e('StudyActivity.gotoDetail', 'StudyActivity.onActivityResult', 'RESULT',
  'menudetail: startActivityForResult(DetailScreen) returns', needs_state=NEED_CARD,
  evidence=FW_RESULT + '; SRC ui/StudyActivity.java:712-717')
e('StudyActivity.showEditDialog', 'StudyActivity.onActivityResult', 'RESULT',
  'menu_context_edit: startActivityForResult(CardEditor, isEditNew=false) returns', needs_state=NEED_CARD,
  evidence=FW_RESULT + '; SRC ui/StudyActivity.java:662-668')
e('CardEditor.onOptionsItemSelected', 'CardEditor.onActivityResult', 'RESULT',
  'editor_menu_image: startActivityForResult(FileBrowserActivity, image extensions) returns the picked image',
  env=ENV_FB_STORAGE, guard='the focused field is question/answer/note',
  evidence=FW_RESULT + '; SRC ui/CardEditor.java:180-186,361-388')
e('CardEditor.startAudioBrowser', 'CardEditor.onActivityResult', 'RESULT',
  'add_existing_audio: startActivityForResult(FileBrowserActivity, audio extensions) returns the picked audio',
  env=ENV_FB_STORAGE, guard='isViewEligibleToEditAudio() is true (add_existing_audio branch)',
  evidence=FW_RESULT + '; SRC ui/CardEditor.java:187-191,290-295,389')
e('DatabaseMerger.onClick', 'DatabaseMerger.onActivityResult', 'RESULT',
  'v == targetEdit: startActivityForResult(FileBrowserActivity, .db) returns the picked path', env=ENV_FB_STORAGE,
  guard='v == targetEdit', evidence=FW_RESULT + '; SRC ui/DatabaseMerger.java:100-106,74-97')
e('DatabaseMerger.onClick', 'DatabaseMerger.onActivityResult', 'RESULT',
  'v == sourceEdit: startActivityForResult(FileBrowserActivity, .db) returns the picked path', env=ENV_FB_STORAGE,
  guard='v == sourceEdit', evidence=FW_RESULT + '; SRC ui/DatabaseMerger.java:108-113,74-97')
e('DropboxListActivity.openUploadDropbox', 'DropboxListActivity.onActivityResult', 'RESULT',
  'startActivityForResult(UploadDropboxActivity) returns', evidence=FW_RESULT + '; SRC downloader/dropbox/DropboxListActivity.java:100-104,85-90')

# ---- E3. group 6: CHA over-approximations of the BaseActivity-typed mActivity.restartActivity() calls.
# The gesture dialog's host is PreviewEditActivity or StudyActivity (both override restartActivity), so the CHA edges to
# CardEditor, CardListActivity and BaseActivity never run; OpenActionsFragment's host is AnyMemo (no override), so only
# BaseActivity.restartActivity runs there (kept).
sup(('GestureSelectionDialogFragment.onDismiss', 'CardEditor.restartActivity'),
    ('GestureSelectionDialogFragment.onDismiss', 'CardListActivity.restartActivity'),
    ('GestureSelectionDialogFragment.onDismiss', 'BaseActivity.restartActivity'),
    ('OpenActionsFragment$1$1.onClick', 'PreviewEditActivity.restartActivity'),
    ('OpenActionsFragment$1$1.onClick', 'CardEditor.restartActivity'),
    ('OpenActionsFragment$1$1.onClick', 'StudyActivity.restartActivity'),
    ('OpenActionsFragment$1$1.onClick', 'CardListActivity.restartActivity'),
    ('CardListActivity.onActivityResult', 'CardListActivity.restartActivity'))

# ---- F. layout <fragment> tag, loader, service and widget creation by the framework ----
e('AnyMemoDownloaderActivity.onCreate', 'AnyMemoDownloaderFragment.<init>', 'FRAMEWORK',
  'the layout names the fragment, so the activity creates it while it inflates the layout',
  cls='non_standard', via='layout fragment tag; the framework creates the fragment by name (Fragment.instantiate)',
  evidence='FW-SRC core/java/android/app/Activity.java:6205 (fragment tag); FW-SRC core/java/android/app/Fragment.java:490 (instantiate); SRC downloader/anymemo/AnyMemoDownloaderActivity.java:12 (setContentView) and res/layout/anymemo_downloader.xml:6')

e('AnyMemo$HandleOpenIntentLoaderCallbacks.onCreateLoader', 'AnyMemo$FileAsyncTaskLoader.loadInBackground', 'FRAMEWORK',
  'forceLoad starts the loader, which runs loadInBackground on a worker thread',
  cls='non_standard', via='AsyncTaskLoader (androidx library)',
  evidence=FW_LOADER + '; SRC ui/AnyMemo.java:450 (loader.forceLoad())')

e('ConverterFragment.invokeConverterService', 'ConvertIntentService.<init>', 'FRAMEWORK',
  'startService makes the system create ConvertIntentService',
  cls='non_standard', via='Context.startService (the system creates the service)',
  evidence=FW_CREATE_SVC + '; SRC ui/ConverterFragment.java:162 (getActivity().startService(intent))')

e('AnyMemoWidgetProvider.onUpdate', 'UpdateWidgetService.<init>', 'FRAMEWORK',
  'the widget host creates the RemoteViews service named in the intent given to setRemoteAdapter',
  cls='non_standard', via='RemoteViews adapter; the widget host creates the service',
  evidence=FW_WIDGET + '; SRC widget/AnyMemoWidgetProvider.java:66 (new Intent), :74 (setRemoteAdapter)')

for _name in ['getCount', 'getItemId', 'getLoadingView', 'getViewTypeCount', 'hasStableIds']:
    e('UpdateWidgetService.onGetViewFactory', 'WidgetRemoteViewsFactory.' + _name, 'FRAMEWORK',
      'the widget host asks the factory for ' + _name + ' while it shows the widget list',
      cls='non_standard', via='RemoteViewsService factory callbacks',
      evidence=FW_WIDGET + '; SRC widget/UpdateWidgetService.java:11-12 (onGetViewFactory returns the factory)')

# ---- G. dead chains: no trigger in the app, or only dead callers ----
_NOCALL_UTIL = 'no new of this class and no call of this constructor anywhere in the app source (static utility class)'
UNREACHABLE['AMEnv.<init>'] = ('no_trigger_in_app', _NOCALL_UTIL, 'SRC common/AMEnv.java:34', 'SOURCE')
UNREACHABLE['AMPrefKeys.<init>'] = ('no_trigger_in_app', _NOCALL_UTIL, 'SRC common/AMPrefKeys.java:26', 'SOURCE')
UNREACHABLE['AMSecrets.<init>'] = ('no_trigger_in_app', _NOCALL_UTIL, 'SRC common/AMSecrets.java:25', 'SOURCE')
UNREACHABLE['AMZipUtils.<init>'] = ('no_trigger_in_app', _NOCALL_UTIL, 'SRC utils/AMZipUtils.java:23', 'SOURCE')
UNREACHABLE['AnyMemoExecutor.<init>'] = ('no_trigger_in_app', _NOCALL_UTIL, 'SRC utils/AnyMemoExecutor.java:32', 'SOURCE')
UNREACHABLE['AMStringUtils.<init>'] = ('no_trigger_in_app', _NOCALL_UTIL, 'SRC utils/AMStringUtils.java:30', 'SOURCE')
UNREACHABLE['AMGUIUtility.<init>'] = ('no_trigger_in_app',
    'the constructor is private and no code in the app source calls it (no new AMGUIUtility anywhere)',
    'SRC utils/AMGUIUtility.java:40', 'SOURCE')

for _key, _ref in [
        ('Setting.getDisplayInHTML', 'SRC entity/Setting.java:265'),
        ('Setting.setDisplayInHTML', 'SRC entity/Setting.java:269'),
        ('Setting.getQuestionField', 'SRC entity/Setting.java:289'),
        ('Setting.setQuestionField', 'SRC entity/Setting.java:293'),
        ('Setting.getAnswerField', 'SRC entity/Setting.java:305'),
        ('Setting.setAnswerField', 'SRC entity/Setting.java:309'),
        ('Setting.setAnswerFieldEnum', 'SRC entity/Setting.java:313'),
        ('Setting.getCreationDate', 'SRC entity/Setting.java:342'),
        ('Setting.getUpdateDate', 'SRC entity/Setting.java:350')]:
    UNREACHABLE[_key] = ('no_trigger_in_app', 'no call of this accessor anywhere in the app source (Java or res)', _ref, 'SOURCE')

UNREACHABLE['CardFragment$Builder.setCardOnLongClickListener'] = (
    'no_trigger_in_app', 'no caller of this builder method anywhere in the app source',
    'SRC ui/CardFragment.java:262', 'SOURCE')
UNREACHABLE['CardPlayerSettingDialogFragment.newInstance'] = (
    'no_trigger_in_app', 'no caller of newInstance anywhere in the app source',
    'SRC ui/CardPlayerSettingDialogFragment.java:56', 'SOURCE')
UNREACHABLE['CategoryEditorFragment$NewCategoryTask.onCancelled'] = (
    'framework_never_calls', 'AsyncTask calls onCancelled only after cancel() (FW-SRC core/java/android/os/AsyncTask.java:462); this task is never cancelled',
    'SRC ui/CategoryEditorFragment.java:254', 'SOURCE')

for _key, _ref in [
        ('EditTabFragment.<init>', 'SRC ui/EditTabFragment.java:29'),
        ('EditTabFragment.onAttach', 'SRC ui/EditTabFragment.java:43'),
        ('EditTabFragment$1.<init>', 'SRC ui/EditTabFragment.java:51')]:
    UNREACHABLE[_key] = ('no_trigger_in_app',
        'no reference to EditTabFragment in the manifest, res or any other Java file of the app', _ref, 'SOURCE')
# The bytecode still shows two callers (tools/scan_unreachable.py --callers): FileBrowserFragment.openFile (line 413) and
# notifyFileClick (line 438) call the listener on the field onFileClickListener. That field holds this object only if
# EditTabFragment is constructed (field initializer EditTabFragment.java:49-50, set in onAttach at line 46). No code
# constructs EditTabFragment, so those two calls never reach this method (the auto edges are suppressed, see the sup block above).
UNREACHABLE['EditTabFragment$1.onFileBrowserFileClick'] = ('no_trigger_in_app',
    'no reference to EditTabFragment in the manifest, res or any other Java file of the app; the bytecode callers FileBrowserFragment.openFile (FileBrowserFragment.java:413) and notifyFileClick (FileBrowserFragment.java:438) reach it only through the listener field, which holds this object only when EditTabFragment is constructed (EditTabFragment.java:46, 49-50)',
    'SRC ui/EditTabFragment.java:51', 'SOURCE')

for _key in ['CategoryDaoImpl$1.<init>', 'CategoryDaoImpl$1.call']:
    UNREACHABLE[_key] = ('no_trigger_in_app',
        'the anonymous Callable is created only inside populateCategory, which has no caller',
        'SRC dao/CategoryDaoImpl.java:60', 'SOURCE')

UNREACHABLE['ErrorUtil.getErrorString'] = ('no_trigger_in_app',
    'only called from ErrorUtil.showFatalError and showNonFatalError, which are already unreachable (no caller)',
    'SRC utils/ErrorUtil.java:66', 'SOURCE')
for _key in ['ErrorUtil$1.<init>', 'ErrorUtil$1.onCancel', 'ErrorUtil$2.<init>', 'ErrorUtil$2.onClick',
             'ErrorUtil$3.<init>', 'ErrorUtil$3.onClick']:
    UNREACHABLE[_key] = ('no_trigger_in_app',
        'listener created only inside ErrorUtil.showFatalError or showNonFatalError, which are already unreachable',
        'SRC utils/ErrorUtil.java:32-66', 'SOURCE')

for _key in ['DropboxApiHelper$2.<init>', 'DropboxApiHelper$2.subscribe',
             'DropboxApiHelper$2$1.<init>', 'DropboxApiHelper$2$1.onFailure', 'DropboxApiHelper$2$1.onResponse']:
    UNREACHABLE[_key] = ('no_trigger_in_app',
        'the Completable is built only inside createFolder, which has no caller',
        'SRC downloader/dropbox/DropboxApiHelper.java:116', 'SOURCE')

UNREACHABLE['RecentListFragment.setUserVisibleHint'] = ('framework_never_calls',
    'setUserVisibleHint is called by a ViewPager or pager adapter; this fragment is added with FragmentTransaction.replace (ui/AnyMemo.java:255) and no pager exists',
    'SRC ui/RecentListFragment.java:160', 'INFERRED')
UNREACHABLE['RecentListFragment$RecentListAdapter.stopActionMode'] = ('no_trigger_in_app',
    'its only caller is RecentListFragment.setUserVisibleHint (line 164), which is never called',
    'SRC ui/RecentListFragment.java:470', 'INFERRED')
UNREACHABLE['RecentListActionModeUtil.stopActionMode'] = ('no_trigger_in_app',
    'its only caller is RecentListFragment$RecentListAdapter.stopActionMode (line 471), which is never called',
    'SRC utils/RecentListActionModeUtil.java:102', 'INFERRED')

UNREACHABLE['RecentListFragment$RecentListAdapter.getList'] = ('no_trigger_in_app',
    'no call of getList() anywhere in the app source; the only occurrence is its declaration',
    'SRC ui/RecentListFragment.java:460', 'SOURCE')
UNREACHABLE['AbstractDownloaderFragment$DownloadListAdapter.getList'] = ('no_trigger_in_app',
    'no call of getList() anywhere in the app source; the only occurrence is its declaration',
    'SRC downloader/common/AbstractDownloaderFragment.java:375', 'SOURCE')

C4_BIND_SIGS = ['bind(View)', 'bind(View,Object)', 'inflate(LayoutInflater)',
                'inflate(LayoutInflater,ViewGroup,boolean)', 'inflate(LayoutInflater,ViewGroup,boolean,Object)',
                'inflate(LayoutInflater,Object)']
for _cls, _ref in [
        ('DropboxListActivityBinding', 'SRC downloader/dropbox/DropboxListActivity.java:39'),
        ('MainTabsBinding', 'SRC ui/AnyMemo.java:121'),
        ('UploadDropboxScreenBinding', 'SRC downloader/dropbox/UploadDropboxActivity.java:47')]:
    for _sig in C4_BIND_SIGS:
        UNREACHABLE[_cls + '.' + _sig] = ('no_trigger_in_app',
            'no call of this static method in the app source; the activity builds its binding through DataBindingUtil.setContentView, which uses the generated mapper and its *BindingImpl constructor',
            _ref, 'INFERRED')
# ---- end pass 2 chunk 4 ----
# ---- pass 2 chunk 5 (2026-10-26): the 41 build errors; every reason and reference was read in the source ----
FW_OKHTTP = ('INFERRED okhttp3.Call.enqueue runs the Callback on an OkHttp worker thread: onFailure when the request '
             'fails, onResponse when a response arrives (okhttp source not read; the enqueue call is at '
             'downloader/dropbox/DropboxApiHelper.java:87)')
FW_JDK = ('INFERRED the java.util collection calls equals() or hashCode() on the argument or on the elements while it '
          'removes, searches or inserts (AbstractCollection.remove(Object), AbstractList.indexOf, HashSet.add; the JDK '
          'source is not in work/fw_src)')
FW_TOSTRING = ('INFERRED string concatenation converts a non-String operand with String.valueOf, which calls toString() '
               '(JLS 5.1.11); javac emits StringBuilder.append(Object), so the call is not visible in the app bytecode')
FW_CHART = ('INFERRED the MPAndroidChart library (com.github.mikephil.charting, imported at ui/StatisticsScreen.java:34-38) '
            'draws the chart and calls ValueFormatter.getFormattedValue(float) for each label (library source not read)')

# Dropbox: the OkHttp Callback created in DropboxApiHelper$1.subscribe (enqueue at 87; onFailure 89-91; onResponse 94-110)
for _cb, _lines in [('onFailure', '87-91'), ('onResponse', '87-110')]:
    e('DropboxApiHelper$1.subscribe', 'DropboxApiHelper$1$1.' + _cb, 'FRAMEWORK',
      'OkHttp calls the enqueued Callback on a worker thread when the request ' +
      ('fails' if _cb == 'onFailure' else 'gets a response'),
      env=ENV_DROPBOX, cls='non_standard', via='OkHttp Call.enqueue calls the Callback (okhttp3 library)',
      evidence=FW_OKHTTP + '; SRC downloader/dropbox/DropboxApiHelper.java:' + _lines)

# JDK collection dispatch from REACHABLE callers (equals / hashCode / toString are not visible as app invoke sites)
e('LearnQueueManager.remove', 'Card.equals', 'FRAMEWORK',
  'learnQueue.remove(card): the LinkedList compares card with each element by equals',
  cls='non_standard', via='JDK List.remove(Object) calls equals', evidence=FW_JDK + '; SRC queue/LearnQueueManager.java:119-121')
e('LearnQueueManager.position', 'Card.equals', 'FRAMEWORK',
  'learnQueue.indexOf(c): the LinkedList compares c with each element by equals',
  cls='non_standard', via='JDK List.indexOf(Object) calls equals', evidence=FW_JDK + '; SRC queue/LearnQueueManager.java:210')
e('QuizQueueManager.remove', 'Card.equals', 'FRAMEWORK',
  'reviewCache.remove(card) and newCache.remove(card): the LinkedList compares card with each element by equals',
  cls='non_standard', via='JDK List.remove(Object) calls equals', evidence=FW_JDK + '; SRC queue/QuizQueueManager.java:82-83 (LinkedList, lines 58-59)')
e('QuizQueueManager.update', 'Card.hashCode', 'FRAMEWORK',
  'dirtyCache.add(card): the HashSet hashes the card',
  cls='non_standard', via='JDK HashSet.add calls hashCode', evidence=FW_JDK + '; SRC queue/QuizQueueManager.java:140 (HashSet, line 60)')
e('LearnQueueManager$1$1.call', 'LearningData.toString', 'FRAMEWORK',
  'string concatenation of card.getLearningData() in the Log and RuntimeException messages of the flush',
  cls='non_standard', via='JLS 5.1.11 string conversion calls toString', evidence=FW_TOSTRING + '; SRC queue/LearnQueueManager.java:260-263,266')
e('LearnQueueManager$1$1.call', 'Card.toString', 'FRAMEWORK',
  'string concatenation of card in the RuntimeException message of the flush',
  cls='non_standard', via='JLS 5.1.11 string conversion calls toString', evidence=FW_TOSTRING + '; SRC queue/LearnQueueManager.java:267')
e('CategoryEditorFragment$DeleteCategoryTask.onPostExecute', 'Category.equals', 'FRAMEWORK',
  'categoryAdapter.remove(selectedCategory): ArrayAdapter.remove(T) calls List.remove(Object), which compares the category with each element by equals',
  cls='non_standard', via='ArrayAdapter.remove(T) -> List.remove(Object) -> Category.equals (AOSP 8.1.0_r1)',
  evidence=FW_JDK + '; FW-SRC core/java/android/widget/ArrayAdapter.java:300-306; SRC ui/CategoryEditorFragment.java:314')

# FileBrowser file list: the RecyclerView calls the adapter after setAdapter (line 203) in onCreateView (183)
for _name, _ref in [('getItemCount', '590')]:
    e('FileBrowserFragment.onCreateView', 'FileBrowserFragment$FileBrowserAdapter.' + _name, 'FRAMEWORK',
      'the recycler view calls the adapter ' + _name + ' while it lays out the file rows',
      cls='non_standard', via='RecyclerView calls the adapter callbacks (androidx library)',
      evidence=FW_RECYCLER + '; SRC ui/FileBrowserFragment.java:203 (setAdapter), :' + _ref + ' (' + _name + ')')

# GestureSelectionDialogFragment (created in StudyActivity.showGesturesDialog / PreviewEditActivity.showGesturesDialog)
e('GestureSelectionDialogFragment.<init>', 'GestureSelectionDialogFragment.onDismiss', 'FRAMEWORK',
  'the dialog is dismissed (Back, outside tap or a button): DialogFragment calls onDismiss',
  evidence=FW_DIALOGFRAG + '; SRC ui/GestureSelectionDialogFragment.java:182')

# SettingsScreen loader: onLoaderReset is registered with the same loader as onCreateLoader (line 137-139)
e('SettingsScreen.onCreate', 'SettingsScreen$SettingLoaderCallbacks.onLoaderReset', 'FRAMEWORK',
  'the loader is reset when the activity is destroyed or the loader is restarted: LoaderManager calls onLoaderReset',
  evidence=FW_LOADER + '; SRC ui/SettingsScreen.java:411')

# StatisticsScreen: created by OpenActionsFragment$1.onClick (same pattern as SettingsScreen.<init>)
e('OpenActionsFragment$1.onClick', 'StatisticsScreen.<init>', 'ENTRY',
  'v == statisticsItem: startActivity(StatisticsScreen) creates the activity object',
  evidence='SRC ui/OpenActionsFragment.java:163-168')
e('StatisticsScreen.<init>', 'StatisticsScreen.onCreate', 'LIFECYCLE', 'Activity lifecycle: the framework calls onCreate after the constructor',
  evidence=FW_ACTIVITY + '; SRC ui/StatisticsScreen.java:78-80')
e('StatisticsScreen.onCreate', 'StatisticsScreen$ChartTask.onPreExecute', 'ASYNC',
  'new CardToReviewTask().execute(): AsyncTask calls onPreExecute on the main thread before doInBackground',
  evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:104-105,161')
e('StatisticsScreen$1.onNavigationItemSelected', 'StatisticsScreen$ChartTask.onPreExecute', 'ASYNC',
  'a chart menu item executes one ChartTask: AsyncTask calls onPreExecute first',
  evidence=FW_ASYNC + '; SRC ui/StatisticsScreen.java:124-138,161')
for _fmt, _ln in [('StatisticsScreen$ChartValueFormatter.getFormattedValue', '361'),
                  ('StatisticsScreen$ChartYAxisValueFormatter.getFormattedValue', '369')]:
    e('StatisticsScreen$ChartTask.onPostExecute', _fmt, 'FRAMEWORK',
      'the chart is added to the frame and drawn: the chart library calls the value formatter for each label',
      cls='non_standard', via='MPAndroidChart calls ValueFormatter.getFormattedValue while it draws (library)',
      evidence=FW_CHART + '; SRC ui/StatisticsScreen.java:173-177, 205 (valueFormatter on the data), 219-220 (yAxisValueFormatter on the axes), ' + _ln + ' (getFormattedValue)')

# dead chains (no caller in the app)
UNREACHABLE['AMGUIUtility$6.<init>'] = ('no_trigger_in_app', 'created only in AMGUIUtility.getDialogFinishListener, which has no caller (its own UNREACHABLE entry; grep and bytecode: declaration only)',
    'SRC utils/AMGUIUtility.java:146', 'SOURCE')
UNREACHABLE['AMGUIUtility$6.onClick'] = ('no_trigger_in_app', 'the OnClickListener is created only in AMGUIUtility.getDialogFinishListener (dead, no caller); it is never set on a dialog',
    'SRC utils/AMGUIUtility.java:146-150', 'SOURCE')
UNREACHABLE['ErrorUtil.<init>'] = ('no_trigger_in_app', 'the @Inject constructor runs only when Dagger needs an ErrorUtil; no injection point or @Provides requests it (grep: ActivityModules.java only imports the class; no @Inject field of this type)',
    'SRC utils/ErrorUtil.java:25', 'SOURCE')
UNREACHABLE['BaseActivity.appComponents'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode and grep): activities use activityComponents() (BaseActivity.java:77); the appComponents() callers are in the Service classes only',
    'SRC common/BaseActivity.java:73', 'SOURCE')
UNREACHABLE['BaseActivity.isActivityCreated'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode and grep: declaration only)',
    'SRC common/BaseActivity.java:98', 'SOURCE')
UNREACHABLE['BaseDialogFragment.appComponents'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode and grep: declaration only)',
    'SRC common/BaseDialogFragment.java:12', 'SOURCE')
UNREACHABLE['BaseFragment.appComponents'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode and grep: declaration only)',
    'SRC common/BaseFragment.java:12', 'SOURCE')
UNREACHABLE['DownloadItem.clone'] = ('no_trigger_in_app', 'no call of this method in the app (bytecode and grep: declaration only; the clone() at DownloadItem.java:47 is HashMap.clone)',
    'SRC downloader/common/DownloadItem.java:44', 'SOURCE')
UNREACHABLE['Deck.<init>'] = ('no_trigger_in_app', 'no new Deck in the app (bytecode and grep); getDeckDao() (common/AnyMemoDBOpenHelper.java:183) has no caller, so no ORMLite query builds Deck objects',
    'SRC entity/Deck.java:28', 'SOURCE')
UNREACHABLE['Filter.<init>'] = ('no_trigger_in_app', 'no new entity Filter in the app (bytecode and grep; CardListActivity.java:529 creates android.widget.Filter); getFilterDao() (common/AnyMemoDBOpenHelper.java:205) has no caller',
    'SRC entity/Filter.java:27', 'SOURCE')
UNREACHABLE['Stat.<init>'] = ('no_trigger_in_app', 'no new Stat in the app (bytecode and grep); there is no getStatDao(), and StatDaoImpl.<init> is itself UNREACHABLE',
    'SRC entity/Stat.java:31', 'SOURCE')
for _acc, _ln in [('getId', 129), ('setId', 133), ('getName', 137), ('setName', 141), ('getDescription', 145), ('setDescription', 149)]:
    UNREACHABLE['Setting.' + _acc] = ('no_trigger_in_app', 'no invoke site of this accessor in the app bytecode (auto_calls.json has no caller)',
        'SRC entity/Setting.java:%d' % _ln, 'SOURCE')
UNREACHABLE['DataBindingTriggerClass.<init>'] = ('no_trigger_in_app', 'generated data-binding trigger class (no source file); no invoke site of its constructor in the app bytecode (auto_calls.json records only the framework Object.<init> link); coverage_baseline monkey and ape both false',
    'auto_calls.json framework_calls: DataBindingTriggerClass.<init> <- Object.<init>', 'INFERRED')
# ---- end pass 2 chunk 5 ----

# ---- pass 2 warning fix (2026-10-26): auto CALL edges whose caller is UNREACHABLE (dead-to-dead) ----
sup(
    ('fantastischmemo.DataBinderMapperImpl.getLayoutId', 'fantastischmemo.DataBinderMapperImpl$InnerLayoutIdLookup.<clinit>'),
    ('fantastischmemo.DataBinderMapperImpl.convertBrIdToString', 'fantastischmemo.DataBinderMapperImpl$InnerBrLookup.<clinit>'),
    ('RecentListFragment$RecentListAdapter.stopActionMode', 'RecentListActionModeUtil.stopActionMode'),
    ('RecentListFragment.setUserVisibleHint', 'RecentListFragment$RecentListAdapter.stopActionMode'),
    ('EditTabFragment.<init>', 'EditTabFragment$1.<init>'),
    ('CategoryDaoImpl.populateCategory', 'CategoryDaoImpl$1.<init>'),
    ('OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.onPostExecute', 'OauthAccountActivity.showGetTokenDialog'),
    ('OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.onPostExecute', 'OauthAccountActivity.invalidateSavedToken'),
    ('OauthAccountActivity$1.onAuthCodeReceived', 'OauthAccountActivity$GetAccessTokenTask.<init>'),
    ('OauthAccountActivity$1.onAuthCodeError', 'OauthAccountActivity.showAuthErrorDialog'),
    ('OauthAccountActivity$GetAccessTokenTask.onPostExecute', 'OauthAccountActivity.showAuthErrorDialog'),
    ('OauthAccessCodeRetrievalFragment$RequestTokenTask.onPostExecute', 'OauthAccessCodeRetrievalFragment$RequestTokenTask$2.<init>'),
    ('OauthAccessCodeRetrievalFragment$RequestTokenTask.onPostExecute', 'OauthAccessCodeRetrievalFragment$RequestTokenTask$1.<init>'),
    ('OauthAccountActivity.<init>', 'OauthAccountActivity$1.<init>'),
    ('OauthAccountActivity.onCreate', 'OauthAccountActivity$ValidateAccessTokenAndRunCallbackTask.<init>'),
    ('OauthAccountActivity.onCreate', 'OauthAccountActivity.showGetTokenDialog'),
    ('OauthAccountActivity.showAuthErrorDialog', 'OauthAccountActivity$2.<init>'),
    ('OauthAccountActivity.showGetTokenDialog', 'OauthAccessCodeRetrievalFragment.setAuthCodeReceiveListener'),
    ('OauthAccessCodeRetrievalFragment.onCancel', 'OauthAccountActivity$1.onCancelled'),
    ('OauthAccessCodeRetrievalFragment.onCreateView', 'OauthAccessCodeRetrievalFragment$RequestTokenTask.<init>'),
    ('DropboxApiHelper.createFolder', 'DropboxApiHelper$2.<init>'),
    ('DropboxApiHelper$2.subscribe', 'DropboxApiHelper$2$1.<init>'),
    ('ErrorUtil.showFatalError', 'ErrorUtil$1.<init>'),
    ('ErrorUtil.showFatalError', 'ErrorUtil$2.<init>'),
    ('ErrorUtil.showFatalError', 'ErrorUtil.getErrorString'),
    ('ErrorUtil.showNonFatalError', 'ErrorUtil$3.<init>'),
    ('ErrorUtil.showNonFatalError', 'ErrorUtil.getErrorString'),
    ('AMGUIUtility.getDialogFinishListener', 'AMGUIUtility$6.<init>'),
    ('UploadDropboxScreenBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'UploadDropboxScreenBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('UploadDropboxScreenBinding.inflate(LayoutInflater)', 'UploadDropboxScreenBinding.inflate(LayoutInflater,Object)'),
    ('UploadDropboxScreenBinding.bind(View)', 'UploadDropboxScreenBinding.bind(View,Object)'),
    ('DropboxListActivityBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'DropboxListActivityBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('DropboxListActivityBinding.inflate(LayoutInflater)', 'DropboxListActivityBinding.inflate(LayoutInflater,Object)'),
    ('DropboxListActivityBinding.bind(View)', 'DropboxListActivityBinding.bind(View,Object)'),
    ('MainTabsBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'MainTabsBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)'),
    ('MainTabsBinding.inflate(LayoutInflater)', 'MainTabsBinding.inflate(LayoutInflater,Object)'),
    ('MainTabsBinding.bind(View)', 'MainTabsBinding.bind(View,Object)'),
)
# ---- end pass 2 warning fix ----

# ---- pass 2 CLASSIFY (2026-10-26): library / reflection links (REVIEW list, 140 default-class edges). None keeps the default. ----
DI_VIA = 'Dagger (DI; generated injector and provider code)'


def CLASSIFY(x):
    src, dst, ev = x['src'], x['dst'], str(x.get('evidence') or '')
    # RxJava 2: the Rx operator calls the subscriber callback (Consumer, Action, Callable, CompletableOnSubscribe)
    if 'RxJava 2 (io.reactivex)' in ev:
        return ('non_standard', 'RxJava 2 (io.reactivex) calls the Rx callback (subscribe / onNext / call)')
    # Dagger: the generated component (DaggerAppComponents) and the generated provider factories make these calls
    if src.startswith('DaggerAppComponents') or src.startswith('AppModules_'):
        return ('non_standard', DI_VIA)
    if dst == 'DaggerAppComponents$Builder.<init>':
        return ('non_standard', DI_VIA)
    # app code names the generated builder methods (builder().application(this), activityComponents().activity(...))
    if src.startswith('AMApplication.') and dst.startswith('DaggerAppComponents$'):
        return 'explicit'
    # data binding: the generated <Layout>BindingImpl classes are created by DataBindingUtil through DataBinderMapperImpl
    if 'BindingImpl' in src:
        return ('non_standard', 'data binding (androidx DataBindingUtil creates the generated <Layout>BindingImpl through DataBinderMapperImpl)')
    # data binding: androidx DataBindingUtil creates the generated mapper and calls it
    if src.startswith('databinding.'):
        return ('non_standard', 'data binding (androidx DataBindingUtil creates the generated DataBinderMapperImpl and calls it)')
    # reflection: LayoutInflater.createView constructs the view class named in the layout XML
    if 'reflectively' in ev:
        return ('non_standard', 'reflection (LayoutInflater.createView constructs the view class named in the layout XML)')
    return None
# ---- end pass 2 CLASSIFY ----

# ---- pass 2 EDIT (2026-10-26): bytecode-line fixes (check_bytecode_lines --all --emit) and generated-class citations ----
# FIX_LINES: each corrected line was read in the source (CardPlayerService.java:176-188, QACardActivity.java:158-168)
FIX_LINES = {
    ('CardPlayerService.reset', 'CardPlayerContext.<init>', 'SRC CardPlayerService.java:186 (bytecode)'): 'SRC CardPlayerService.java:178-186 (bytecode line was 186)',
    ('QACardActivity.startInit', 'QACardActivity$CardTTSUtilLoaderCallbacks.<init>', 'SRC QACardActivity.java:164 (bytecode)'): 'SRC QACardActivity.java:165 (bytecode line was 164)',
    ('QACardActivity.startInit', 'QACardActivity$SettingLoaderCallbacks.<init>', 'SRC QACardActivity.java:162 (bytecode)'): 'SRC QACardActivity.java:163 (bytecode line was 162)',
}
# these files are written by the annotation processors / data binding at build time: no source file in the tree
GENERATED_CITES = ('SRC DaggerAppComponents.java:', 'SRC DropboxListActivityBindingImpl.java:',
                   'SRC MainTabsBindingImpl.java:', 'SRC UploadDropboxScreenBindingImpl.java:')


def EDIT(x):
    # step-5 gates (GATE, defined at the end of this file): a text sets its kinds from the registry, so clear the authored kinds
    gate = GATE.get((x['src'], x['dst']))
    if gate:
        for k, v in gate.items():
            if k == 'env':
                x['env'], x['env_kinds'] = v, []
            elif k == 'needs_state':
                x['needs_state'], x['state_kinds'] = v, []
            else:
                x[k] = v
    ev = x.get('evidence') or ''
    fix = FIX_LINES.get((x['src'], x['dst'], ev))
    if fix:
        x['evidence'] = fix
        return
    for cite in GENERATED_CITES:
        if ev.startswith(cite):
            line = ev[len(cite):].split(' ')[0]
            gen = cite[len('SRC '):-1]
            x['evidence'] = ('INFERRED generated class %s (written by the annotation processor or data binding at build time; '
                             'no source file in the tree; bytecode line %s)' % (gen, line))
            return
    if x['src'] == 'CardListActivity.showHideAnswers' and x['dst'] == 'CardListActivity$CardListAdapter.iterator' and ev == 'SRC CardListActivity.java:310 (bytecode)':
        x['evidence'] = ('INFERRED the enhanced for at CardListActivity.java:310 calls CardListAdapter.iterator() '
                         '(JLS 14.14.2; javac writes this call, not the source text)')
# ---- end pass 2 EDIT ----

# ---- step 5 (2026-10-26): gates, states and ENV kinds; the dead Load-more chain ----
# Each text is registered by env_text / state_text (its kinds come from the exact text). Each GATE entry was read in the
# source at the lines it names. EDIT applies GATE to the edge with the same (src, dst) pair.
ENV_PERM_DIALOG_STORAGE = env_text('the user taps Allow in the system permission dialog for WRITE_EXTERNAL_STORAGE (requestPermissions on API <= 29)', ('permission',))
ENV_PERM_DIALOG_MIC = env_text('the user taps Allow in the system permission dialog for RECORD_AUDIO (requestPermissions from the audio recorder)', ('permission',))
ENV_EXT_IMAGE_VIEWER = env_text('outside package: an image viewer app handles the ACTION_VIEW intent for the matched image file (sent through the FileProvider)', ('other_app',))
ENV_STORAGE_HW = env_text('the device has external storage mounted and readable (the AnyMemo folder is on external storage)', ('hardware',))
ENV_HOME_PAUSE = env_text('the user presses Home or opens another app, so this activity is paused (onPause)', ('other_app',))
ENV_ROTATE = env_text('the user rotates the device or changes the system locale, so the configuration changes (onConfigurationChanged)', ('system_event',))
ENV_AUDIO_OUT = env_text('the device plays audio through its audio output (MediaPlayer plays the audio file; the emulator has a default output)', ('hardware',))
NEED_AUDIO_FILE = state_text('A stored audio tag names an audio file that exists under the AnyMemo audio folder (speakWord returns false when none is found)', ('file',))
NEED_PLAYING = state_text('The Card Player service is bound: a bind happened earlier, when the Card Player screen was opened (onUnbind runs only after a bind)', ('session',))
NEED_UPLOAD = state_text('An upload was started from the confirm-upload dialog (OK) on this screen, and the Dropbox upload has finished', ('session',))
NEED_IMPORT_PICKED = state_text('A .db file was picked with the system document picker and the import has started (the picker returned RESULT_OK)', ('session',))

GATE = {
    # Group D route check (2026-10-26): three bytecode edges had no guard; each guard was read in source.
    ('FileBrowserFragment.onOptionsItemSelected', 'DatabaseOperationDialogUtil.showCreateDbDialog'): {'guard': 'the Create DB menu item is tapped (itemId == R.id.file_browser_createdb, FileBrowserFragment.java:291)'},
    ('DatabaseOperationDialogUtil$1$3.onClick', 'AMFileUtil.deleteFileWithBackup'): {'guard': 'the file name typed in the Create DB dialog already exists (DatabaseOperationDialogUtil.java:57-58)'},
    ('BaseActivity.onCreate', 'BaseActivity.enableImmersiveMode'): {'guard': 'the fullscreen mode preference is on (common/BaseActivity.java:36-37)', 'needs_state': NEED_FULLSCREEN},
    # Recent tab (AnyMemo.java:240-241): the bytecode copies of `new RecentListFragment()` are kept and guarded. The @INIT copy is
    # the cold-start selection, which always takes this branch (AnyMemo.java:263).
    ('AnyMemo$2.onNavigationItemSelected', 'RecentListFragment.<init>'): {'guard': 'itemId == recent_tab_menu (AnyMemo.java:240-241)'},
    ('AnyMemo$2.onNavigationItemSelected', 'RecentListFragment.<clinit>'): {'guard': 'itemId == recent_tab_menu (AnyMemo.java:240-241); the class starts at its first new (JLS 12.4.1, INFERRED)'},
    ('AnyMemo$2.onNavigationItemSelected@INIT', 'RecentListFragment.<init>'): {'guard': 'itemId == recent_tab_menu: the cold-start selection always takes this branch (AnyMemo.java:240-241, 263)'},
    ('AnyMemo$2.onNavigationItemSelected@INIT', 'RecentListFragment.<clinit>'): {'guard': 'itemId == recent_tab_menu: the cold-start selection always takes this branch (AnyMemo.java:240-241, 263); the class starts at its first new (JLS 12.4.1, INFERRED)'},
    ('MiscTabFragment.onClick', 'S_DLG_RESET_PREF'): {'guard': 'v == resetButton (MiscTabFragment.java:350)'},
    ('CardEditor.onRequestPermissionsResult', 'CardEditor.startAudioRecorder'): {'guard': 'RECORD_AUDIO is granted in the permission result: grantResults[0] == PERMISSION_GRANTED (CardEditor.java:212-214); a denial only shows a toast'},
    ('StudyActivity.onOptionsItemSelected', 'StudyActivity.showEditDialog'): {'guard': 'itemId == menu_context_edit (StudyActivity.java:166-168)'},
    ('StudyActivity$5.onClick', 'S_STUDY'): {'guard': 'getCurrentCard() != null (StudyActivity.java:676); a null card does nothing'},
    ('PreviewEditActivity.onOptionsItemSelected', 'AMGUIUtility.doConfirmProgressTask'): {'guard': 'one of the three confirm items: menu_context_wipe (PreviewEditActivity.java:341), menu_context_remove_dup (388), menu_context_shuffle (405)'},
    ('FileBrowserFragment.onActivityResult', 'S_DLG_OVERWRITE_DB'): {'guard': 'RESULT_OK from the document picker (FileBrowserFragment.java:326), and a file with the picked name already exists in the AnyMemo folder (newFile.exists(), FileBrowserFragment.java:338-351)'},
    ('FileBrowserFragment.onCreateView@OPEN', 'FileBrowserFragment$7.onClick'): {'guard': 'the page was opened with EXTRA_SHOW_CREATE_DB_BUTTON set (showCreateDbButton; AnyMemo.java:245 sets it; FileBrowserFragment.java:196-199)'},
    ('FileBrowserFragment.openFile@UPLOADDROPBOX', 'FileBrowserFragment.notifyFileClick'): {'guard': 'onFileClickListener is null: this page never sets one, so the click goes to notifyFileClick (FileBrowserFragment.java:412-415)'},
    ('StudyActivity.onActivityResult', 'S_STUDY'): {'guard': 'the result code is not RESULT_CANCELED (StudyActivity.java:208-209 return early for it)'},
    ('PreviewEditActivity.onActivityResult', 'S_PREVIEW_EDIT'): {'guard': 'the result code is not RESULT_CANCELED (PreviewEditActivity.java:190-191 return early for it)'},
    ('ConverterFragment$3.onClick', 'ConverterFragment.invokeConverterService'): {'guard': 'the merge dialog is answered Yes (ConverterFragment.java:102-103)'},
    ('ConverterFragment$2.onClick', 'ConverterFragment.invokeConverterService'): {'guard': 'the merge dialog is answered No: the existing output is first deleted with a backup (deleteFileWithBackup, ConverterFragment.java:110-112)'},
    ('ConverterFragment.startConversion', 'S_DLG_CONVERT_MERGE'): {'guard': 'the destination extension is db and the output file already exists (ConverterFragment.java:93-94)'},
    ('MiscTabFragment.onClick', 'SettingsScreen.<init>'): {'guard': 'v == defaultSettingsButton (MiscTabFragment.java:339)'},
    ('MiscTabFragment.onClick', 'S_DLG_DONATE'): {'guard': 'v == donateButton, and the build is not the pro flavor (MiscTabFragment.java:213-214, 367)'},
    ('MiscTabFragment.onActivityResult', 'MiscTabFragment.invokeImportConversion'): {'guard': 'REQUEST_CODE_IMPORT_CONVERT with RESULT_OK, and the converted output file does not exist yet (MiscTabFragment.java:425-427, 435, 459-460)'},
    ('MiscTabFragment.onActivityResult', 'S_DLG_CONVERT_MERGE'): {'guard': 'REQUEST_CODE_IMPORT_CONVERT with RESULT_OK, and the converted output file already exists (MiscTabFragment.java:425-427, 435)'},
    ('AlarmReceiver.onReceive', 'NotificationUtil.showNotification'): {'guard': 'the request code has the ALARM_SHOW_NOTIFICATION bit set (AlarmReceiver.java:55)'},
    ('AnyMemoDBOpenHelper.onCreate', 'AnyMemoDBOpenHelper.convertOldDatabase'): {'guard': 'the database version is 0 (database.getVersion() == 0, AnyMemoDBOpenHelper.java:64-65)'},
    ('RecentListFragment.onCreateView', 'RecentListFragment$3.onClick'): {'guard': 'the layout has the import_fab view (the listener is set only when it is not null, RecentListFragment.java:184-195)'},
    ('DoubleClickButton.setOnClickListener', 'DoubleClickButton$1.onClick'): {'guard': 'the second tap comes within the time window after the first (the first tap only shows a toast, DoubleClickButton.java:89-96)'},
    ('CardPlayerFragment$1.onClick', 'CardPlayerService.startPlaying'): {'guard': 'v == playButton and the button is not selected (not already playing; CardPlayerFragment.java:157-158, 163)'},
    ('CardPlayerFragment$1.onClick', 'CardPlayerService.stopPlaying'): {'guard': 'v == playButton and the button is selected (already playing; CardPlayerFragment.java:157-160)'},
    ('CardEditor.setInitRadioButton', 'CardEditor$6.onCheckedChanged'): {'guard': 'the card is a new card (isEditNew is true; CardEditor.java:421-458)', 'needs_state': None},
    ('CardPlayerService.onUnbind', 'CardPlayerService.onDestroy'): {'guard': 'onUnbind returned false (CardPlayerService.java:130), so the bound-only service is stopped (CardPlayerService.java:124-134)', 'needs_state': NEED_PLAYING},
    ('UploadDropboxActivity$2.run', 'S_DROPBOX_UPLOAD'): {'env': ENV_DROPBOX, 'needs_state': NEED_UPLOAD},
    ('SpeakWord$2.onCompletion', 'SpeakWord$1.onCompleted'): {'needs_state': NEED_AUDIO_FILE},
    ('DatabaseImportUtil.handleImportDbResult', 'RecentListFragment$4.run'): {'needs_state': NEED_IMPORT_PICKED},
    # S3 (round 1): the loader callbacks call setItems only when their version check passes (RecentListFragment.java:269-270, 301-302)
    ('RecentListFragment$RecentListLoaderCallbacks.onLoadFinished', 'RecentListFragment$RecentListAdapter.setItems'): {'guard': 'recentListVersion.get() == loadedVersion: this load is still the latest one (RecentListFragment.java:269)'},
    ('RecentListFragment$RecentListDetailLoaderCallbacks.onLoadFinished', 'RecentListFragment$RecentListAdapter.setItems'): {'guard': 'recentListVersion.compareAndSet(loadedVersion, loadedVersion + 1) succeeds: this load is still the latest one (RecentListFragment.java:301)'},
    ('DatabaseOperationDialogUtil.showDeleteDbDialog', 'FileBrowserFragment$FileBrowserAdapter$2$1$1.accept'): {'needs_state': NEED_DECK},
    ('DatabaseOperationDialogUtil.showCloneDbDialog', 'FileBrowserFragment$FileBrowserAdapter$2$1$2.accept'): {'needs_state': NEED_DECK},
    ('DatabaseOperationDialogUtil.showRenameDbDialog', 'FileBrowserFragment$FileBrowserAdapter$2$1$3.accept'): {'needs_state': NEED_DECK},
    ('Oauth2AccountActivity.onCreate', 'Oauth2AccountActivity.requestAuth'): {'guard': 'no Dropbox token was saved (savedToken is null, Oauth2AccountActivity.java:44-48)'},
    ('AnyMemo.prepareStoreage', 'S_DLG_SDCARD_WARNING'): {'env': ENV_STORAGE_HW},
    ('AnyMemo.onCreate', 'S_PERM_STORAGE'): {'env': ENV_PERM_DIALOG_STORAGE},
    ('AnyMemo.onCreate', 'AnyMemo.onRequestPermissionsResult'): {'env': ENV_PERM_ANSWER_STORAGE, 'guard': 'WRITE_EXTERNAL_STORAGE is not granted yet, so requestPermissions runs (AnyMemo.java:124-131)'},
    ('AnyMemo.onCreate', 'AnyMemo.loadUiComponents'): {'guard': 'API <= 29 and WRITE_EXTERNAL_STORAGE is already granted (AnyMemo.java:124-134)'},
    ('CardEditor.startAudioRecorderWithPermissionCheck', 'CardEditor.startAudioRecorder'): {'guard': 'RECORD_AUDIO is already granted, so no request is made (CardEditor.java:299-306)'},
    ('CardEditor.startAudioRecorderWithPermissionCheck', 'CardEditor.onRequestPermissionsResult'): {'env': ENV_PERM_DIALOG_MIC, 'guard': 'RECORD_AUDIO is not granted yet, so it is requested (CardEditor.java:299-303)'},
    ('QACardActivity$3.onLongClick', 'S_EXT_PICKER'): {'env': ENV_EXT_IMAGE_VIEWER, 'guard': 'the card text names an image file that exists (filesFound is not empty, QACardActivity.java:696-699)'},
    ('QACardActivity.<init>', 'QACardActivity.onKeyDown'): {'env': ENV_HW_KEY},
    ('QACardActivity.<init>', 'QACardActivity.onKeyUp'): {'env': ENV_HW_KEY},
    ('S_QUIZ', 'QACardActivity.onKeyUp@QuizActivity'): {'env': ENV_HW_KEY},
    ('S_STUDY', 'QACardActivity.onKeyUp@StudyActivity'): {'env': ENV_HW_KEY},
    ('S_MAIN_RECENT', 'BaseActivity.onPause'): {'env': ENV_HOME_PAUSE},
    ('S_MAIN_OPEN', 'BaseActivity.onPause'): {'env': ENV_HOME_PAUSE},
    ('S_MAIN_DOWNLOAD', 'BaseActivity.onPause'): {'env': ENV_HOME_PAUSE},
    ('S_MAIN_MISC', 'BaseActivity.onPause'): {'env': ENV_HOME_PAUSE},
    ('BaseActivity.<init>', 'BaseActivity.onConfigurationChanged'): {'env': ENV_ROTATE},
    ('S_ENTRY', 'CardProvider.<init>'): {'env': ENV_PROVIDER},
    ('S_ENTRY', 'DatabasesProvider.<init>'): {'env': ENV_PROVIDER},
    ('DropboxApiHelper.getUserInfo', 'DropboxApiHelper$1.subscribe'): {'env': ENV_DROPBOX},
    ('DropboxApiHelper.listFiles', 'DropboxApiHelper$3.subscribe'): {'env': ENV_DROPBOX},
    ('DropboxApiHelper.downloadFile', 'DropboxApiHelper$4.call'): {'env': ENV_DROPBOX},
    ('DropboxApiHelper.uploadDropbox', 'DropboxApiHelper$5.call'): {'env': ENV_DROPBOX},
    ('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onError'): {'env': ENV_OAUTH_CALLBACK},
    ('Oauth2AccountActivity.fetchTokenAndOnAuthenticate', 'Oauth2AccountActivity$1.onSuccess'): {'env': ENV_OAUTH_CALLBACK},
    ('Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'Oauth2AccountActivity$2.onComplete'): {'env': ENV_DROPBOX},
    ('Oauth2AccountActivity.verifyTokenAndOnAuthenticate', 'Oauth2AccountActivity$2.onError'): {'env': ENV_DROPBOX},
    ('SpeakWord.speakWord', 'SpeakWord$3.run'): {'env': ENV_AUDIO_OUT},
    ('AnyMemoTTSImpl.sayText', 'AnyMemoTTSImpl$2.onUtteranceCompleted'): {'guard': 'no stored audio tag matched, so speakWord returned false and the TTS engine speaks the text (AnyMemoTTSImpl.java:136-138)'},    ('AnyMemo.prepareFirstTimeRun', 'S_DLG_FIRST_RUN'): {'guard': 'the saved version code differs from this build (savedVersionCode != thisVersionCode, AnyMemo.java:333); the upgrade alert is then shown'},
    ('AnyMemoDBOpenHelper.getCardDao', 'AnyMemoDBOpenHelper.onCreate'): {'guard': 'the stored database version is 0, so the helper creates the schema (SQLiteOpenHelper.java:332-333)'},
    ('AnyMemoDBOpenHelper.getCardDao', 'AnyMemoDBOpenHelper.onDowngrade'): {'guard': 'the stored database version is higher than the new version (SQLiteOpenHelper.java:335-336)'},
    ('AnyMemoDBOpenHelper.getCardDao', 'AnyMemoDBOpenHelper.onUpgrade'): {'guard': 'the stored database version is not 0 and not higher than the new version (SQLiteOpenHelper.java:337-338)'},
    ('DropboxApiHelper$1.subscribe', 'DropboxApiHelper$1$1.onFailure'): {'guard': 'the request fails, so OkHttp calls onFailure (DropboxApiHelper.java:89-91)'},
    ('DropboxApiHelper$1.subscribe', 'DropboxApiHelper$1$1.onResponse'): {'guard': 'a response arrives, so OkHttp calls onResponse (DropboxApiHelper.java:94)'},
    ('SettingsScreen.onCreate', 'SettingsScreen$SettingLoaderCallbacks.onLoaderReset'): {'guard': 'the loader is reset: the activity is destroyed or the loader is restarted (SettingsScreen.java:411)'},
    ('QuizActivity$ChangeCardTask.doInBackground', 'QuizActivity$ChangeCardTask.onPostExecute'): {'guard': 'the task was not cancelled: AsyncTask.finish calls onPostExecute only when isCancelled() is false (AOSP os/AsyncTask.java:691-696)'},
    ('PreviewEditActivity$SearchCardTask.doInBackground', 'PreviewEditActivity$SearchCardTask.onPostExecute'): {'guard': 'the task was not cancelled: AsyncTask.finish calls onPostExecute only when isCancelled() is false (AOSP os/AsyncTask.java:691-696)'},
    ('CardEditor$SaveCardTask.doInBackground', 'CardEditor$SaveCardTask.onPostExecute'): {'guard': 'the task was not cancelled: AsyncTask.finish calls onPostExecute only when isCancelled() is false (AOSP os/AsyncTask.java:691-696)'},
    ('FileBrowserFragment.importDb', 'FileBrowserFragment$4.accept'): {'guard': 'the import completes and RxJava delivers the file to the success consumer (FileBrowserFragment.java:369-377); the error consumer (378-383) runs instead when the copy fails'},
    ('AudioRecorderFragment.setAudioRecorderResultListener', 'CardEditor$5.onReceiveAudio'): {'guard': 'the Save button is tapped (AudioRecorderFragment.java:75-76); Save is enabled only after a recording is stopped (AudioRecorderFragment.java:53, 58)', 'needs_state': NEED_AUDIO_RECORDED},
    # Group 2 (round 1): result branches (checker G3-5 steps 18 and 19)
    ('FileBrowserFragment.onActivityResult', 'FileBrowserFragment$3.<init>'): {'guard': 'the import branch: requestCode == REQUEST_CODE_IMPORT_DB, RESULT_OK and data.getData() != null (FileBrowserFragment.java:326), and newFile.exists() (:338)', 'needs_state': NEED_DB_NAME_TAKEN},
    # Group 2 (round 1): G2-1 step 20. The auto CALL has no graph_def line, so the guard goes in GATE (it applies to every edge with this pair).
    ('DropboxApiHelper$5.call', 'DropboxApiHelper.getResponseErrorString'): {'guard': 'the server answered with an error status: !response.isSuccessful() (DropboxApiHelper.java:249-250), after the file exists (:236-238 throw otherwise)'},
    # Round 1b F1: the three auto CALLs leave createNotificationChannels inside the API 26 block (NotificationChannelUtil.java:36-49)
    ('NotificationChannelUtil.createNotificationChannels', 'NotificationChannelUtil.createConversationNotificationChannel'): {'guard': 'Build.VERSION.SDK_INT >= Build.VERSION_CODES.O (API 26+; always true on API 27) (NotificationChannelUtil.java:36)'},
    ('NotificationChannelUtil.createNotificationChannels', 'NotificationChannelUtil.createCardPlayerNotificationChannel'): {'guard': 'Build.VERSION.SDK_INT >= Build.VERSION_CODES.O (API 26+; always true on API 27) (NotificationChannelUtil.java:36)'},
    ('NotificationChannelUtil.createNotificationChannels', 'NotificationChannelUtil.createReviewReminderNotificationChannel'): {'guard': 'Build.VERSION.SDK_INT >= Build.VERSION_CODES.O (API 26+; always true on API 27) (NotificationChannelUtil.java:36)'},
    # Round 1b F4: the cached field is read first (BaseActivity.java:78)
    ('BaseActivity.activityComponents', 'AMApplication.activityComponents'): {'guard': 'the cached field activityComponents is still null, i.e. the first call in this activity (BaseActivity.java:78)'},
    # Round 1b F5: the null check before destroy (AnyMemo.java:408)
    ('AnyMemo.onDestroy', 'MultipleLoaderManager.destroy'): {'guard': 'multipleLoaderManager != null (AnyMemo.java:408)'},
    # Round 1b C2: the DOUBLE_SIDED check in onClickQuestionView (QACardActivity.java:548-549), one key per variant
    ('QACardActivity.onClickQuestionView', 'QACardActivity.displayCard'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:548-549)'},
    ('QACardActivity.onClickQuestionView@CardPlayerActivity', 'QACardActivity.displayCard@CardPlayerActivity'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:548-549)'},
    ('QACardActivity.onClickQuestionView@PreviewEditActivity', 'QACardActivity.displayCard@PreviewEditActivity'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:548-549)'},
    ('QACardActivity.onClickQuestionView@QuizActivity', 'QACardActivity.displayCard@QuizActivity'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:548-549)'},
    ('QACardActivity.onClickQuestionView@StudyActivity', 'QACardActivity.displayCard@StudyActivity'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:548-549)'},
    # Round 1b C3: the card style picks the card fragment (QACardActivity.java:321-322 single sided, 371-372 double sided)
    ('QACardActivity.displayCard', 'FlipableCardFragment.<init>'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:371-372)'},
    ('QACardActivity.displayCard', 'TwoFieldsCardFragment.<init>'): {'guard': 'card style is SINGLE_SIDED (QACardActivity.java:321-322)'},
    ('QACardActivity.displayCard@CardPlayerActivity', 'FlipableCardFragment.<init>'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:371-372)'},
    ('QACardActivity.displayCard@CardPlayerActivity', 'TwoFieldsCardFragment.<init>'): {'guard': 'card style is SINGLE_SIDED (QACardActivity.java:321-322)'},
    ('QACardActivity.displayCard@PreviewEditActivity', 'FlipableCardFragment.<init>'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:371-372)'},
    ('QACardActivity.displayCard@PreviewEditActivity', 'TwoFieldsCardFragment.<init>'): {'guard': 'card style is SINGLE_SIDED (QACardActivity.java:321-322)'},
    ('QACardActivity.displayCard@QuizActivity', 'FlipableCardFragment.<init>'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:371-372)'},
    ('QACardActivity.displayCard@QuizActivity', 'TwoFieldsCardFragment.<init>'): {'guard': 'card style is SINGLE_SIDED (QACardActivity.java:321-322)'},
    ('QACardActivity.displayCard@StudyActivity', 'FlipableCardFragment.<init>'): {'guard': 'card style is DOUBLE_SIDED (QACardActivity.java:371-372)'},
    ('QACardActivity.displayCard@StudyActivity', 'TwoFieldsCardFragment.<init>'): {'guard': 'card style is SINGLE_SIDED (QACardActivity.java:321-322)'},
    # Round 1b C5: the STOPPED state moves to the next or previous card and calls the event handler (CardPlayerState.java:43-61)
    ('CardPlayerState$1.transition', 'CardPlayerService$1.onPlayCard'): {'guard': 'state is STOPPED, message is GO_TO_NEXT or GO_TO_PREV, and a next/previous card is found (CardPlayerState.java:43-61)'},
    # Round 1b C8: the registered onPostInit runnable runs on the host activity (QACardActivity.java:167)
    ('QACardActivity$2.run', 'CardPlayerActivity.onPostInit'): {'guard': 'the registering activity is CardPlayerActivity (QACardActivity.java:167)'},
    ('QACardActivity$2.run', 'StudyActivity.onPostInit'): {'guard': 'the registering activity is StudyActivity (QACardActivity.java:167)'},
    ('QACardActivity$2.run', 'QuizActivity.onPostInit'): {'guard': 'the registering activity is QuizActivity (QACardActivity.java:167)'},
    ('QACardActivity$2.run', 'PreviewEditActivity.onPostInit'): {'guard': 'the registering activity is PreviewEditActivity (QACardActivity.java:167)'},
    # Round 1b C10: the question view tap only displays the answer when it is not shown yet (StudyActivity.java:365)
    ('StudyActivity.onClickQuestionView', 'QACardActivity.displayCard@StudyActivity'): {'guard': 'answer not yet shown (StudyActivity.java:365)', 'needs_state': NEED_CARD},
    # Round 1b C12: the noise is added only when the schedule asks for it (DefaultScheduler.java:128)
    ('DefaultScheduler.schedule', 'DefaultScheduler.calculateIntervalNoise'): {'guard': 'includeNoise is true and noise is enabled (DefaultScheduler.java:128)'},
    # Round 1b C13: the minimal-interval branch sets noise to 0 and never calls randomNumber (DefaultScheduler.java:199-200)
    ('DefaultScheduler.calculateIntervalNoise', 'DefaultScheduler.randomNumber'): {'guard': 'interval is above the minimal interval so noise is not forced to 0 (DefaultScheduler.java:199-200)'},
    # Round 1b B5: refill(Category) runs only when a category filter is set (QuizQueueManager.java:199-202); the category must exist (QuizActivity.java:264-268)
    ('QuizQueueManager$Builder.build', 'QuizQueueManager.refill(Category)'): {'guard': 'filterCategory != null (QuizQueueManager.java:199-202)', 'needs_state': state_text('the category id from EXTRA_CATEGORY_ID exists in the category table (QuizActivity.java:264-268)', ('data',))},
    # Round 1b B11: the Open tab row tap needs a .db file in the folder (FileBrowserFragment.java:516-517; the sheet is entered from OpenActionsFragment.onCreateView, B1)
    ('FileBrowserFragment$FileBrowserAdapter$1.onClick@OPEN', 'FileBrowserFragment.openFile@OPEN'): {'needs_state': state_text('the Open tab folder holds at least one .db file', ('data',))},
}

# ---- dead Load-more chain (AbstractDownloaderFragment$3 and LoadMoreTask): UNREACHABLE, no hand edge leads in ----
UNREACHABLE['AbstractDownloaderFragment$3.onClick'] = ('branch_never_taken',
    'the Load more listener is set on the footer (AbstractDownloaderFragment.java:153); the footer is removed in onCreateView (164) and is re-added only when hasMore() is true (231-232, 270-271); both subclasses return false (AnyMemoDownloaderFragment.java:54-56, DropboxListFragment.java:91-93), so the tap cannot happen',
    'SRC downloader/common/AbstractDownloaderFragment.java:346-350', 'SOURCE')
UNREACHABLE['AbstractDownloaderFragment$LoadMoreTask.<init>'] = ('branch_never_taken',
    'created only by the Load more listener (AbstractDownloaderFragment.java:349), which cannot run (see AbstractDownloaderFragment$3.onClick)',
    'SRC downloader/common/AbstractDownloaderFragment.java:349', 'SOURCE')
UNREACHABLE['AbstractDownloaderFragment$LoadMoreTask.onPreExecute'] = ('branch_never_taken',
    'AsyncTask calls it only after LoadMoreTask.execute(), which only the Load more listener calls (never reached)',
    'SRC downloader/common/AbstractDownloaderFragment.java:240-245', 'SOURCE')
UNREACHABLE['AbstractDownloaderFragment$LoadMoreTask.doInBackground'] = ('branch_never_taken',
    'AsyncTask runs it only after LoadMoreTask.execute(), which only the Load more listener calls (never reached); it calls loadMore() at line 250',
    'SRC downloader/common/AbstractDownloaderFragment.java:247-255', 'SOURCE')
UNREACHABLE['AbstractDownloaderFragment$LoadMoreTask.onPostExecute'] = ('branch_never_taken',
    'AsyncTask calls it only after doInBackground, which never runs (see AbstractDownloaderFragment$3.onClick)',
    'SRC downloader/common/AbstractDownloaderFragment.java:258-273', 'SOURCE')
UNREACHABLE['AnyMemoDownloaderFragment.loadMore'] = ('branch_never_taken',
    'called only from LoadMoreTask.doInBackground (AbstractDownloaderFragment.java:250), which never runs; hasMore() is false in this subclass (AnyMemoDownloaderFragment.java:54-56)',
    'SRC downloader/anymemo/AnyMemoDownloaderFragment.java:49', 'SOURCE')
UNREACHABLE['DropboxListFragment.loadMore'] = ('branch_never_taken',
    'called only from LoadMoreTask.doInBackground (AbstractDownloaderFragment.java:250), which never runs; hasMore() is false in this subclass (DropboxListFragment.java:91-93)',
    'SRC downloader/dropbox/DropboxListFragment.java:86', 'SOURCE')
# auto CALL edges from the dead Load-more chain into the dead Load-more methods (reported by the build as UNREACHABLE with incoming edges)
sup(
    ('AbstractDownloaderFragment$LoadMoreTask.doInBackground', 'AnyMemoDownloaderFragment.loadMore'),
    ('AbstractDownloaderFragment$LoadMoreTask.doInBackground', 'DropboxListFragment.loadMore'),
    ('AbstractDownloaderFragment$3.onClick', 'AbstractDownloaderFragment$LoadMoreTask.<init>'),
)
# ---- end step 5 ----
