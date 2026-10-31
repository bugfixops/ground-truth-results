# Markor 2.16.1 (#v2.16.1, provenance gsantner/markor@v2.16.1, flavor atest, debug build, package net.gsantner.markor_test)
# trigger graph definition, schema 2.
# Hand-written part: entry points (launcher, intents, widgets, broadcast), lifecycle, pages (SCREENS), GUI handlers and
# framework callbacks (menus, listeners, Handler, AsyncTask, AppIntro, ViewPager2 callbacks), context variants of the big switch
# methods, ENV / STATE gates and UNREACHABLE reasons. Direct app-to-app calls and lambda creation come from the bytecode
# extractor (USE_AUTO); this file adds only what the framework or the manifest starts.
# Standard configuration: flavorAtest debug build (BuildConfig.IS_TEST_BUILD = true, IS_GPLAY_BUILD = false), fresh install,
# API 27 emulator, runtime permissions granted only where a route needs them (ENV permission gate).

TITLE = 'Markor 2.16.1 (flavorAtest debug build, net.gsantner.markor_test) trigger graph'
USE_AUTO = True
STRICT = True

# ------------------------------------------------------------------ gate texts (ENV: outside the app; STATE: earlier in-app action)
ENV_LAUNCHER = 'outside package: the launcher home screen (app icon, widget, pinned shortcut) must be operated'
ENV_OTHER_APP = 'outside package: another app sends the intent (a file manager or share sheet opens a file with Markor)'
ENV_ADB = 'outside package: adb sends the broadcast (am broadcast -a edu.gatech.m3.emma.COLLECT_COVERAGE)'
ENV_PICKER = 'outside package: an external activity (share chooser, browser, document picker or camera) must be driven and returns a result'
ENV_PERM_MISSING = 'the runtime storage permission is not granted yet (the standard configuration grants it only where a route needs it)'
ENV_PERM_DIALOG = 'the system permission dialog is answered (Allow or Deny)'
ENV_EXC = 'a runtime exception (I/O, illegal state, missing handler app) is thrown'

NEED_NOTE = 'A file exists in the notebook (create one with the + button)'
NEED_STARTUP_TAB = 'The startup tab was changed in Settings from the default (Notebook)'
NEED_DOC_OPEN = 'A document is open in the editor or viewer'
NEED_PREVIEW = 'The editor is in preview mode (the view mode was chosen from the menu or the swipe gesture)'
NEED_SHORTCUT = 'A file was opened in the app earlier (addRecentFile then refreshes the launcher shortcuts)'
NEED_APP_OPEN = 'Markor is already open with MainActivity on the screen (singleTop: the new intent goes to that instance)'
NEED_SELECTED = 'One or more files or folders are selected in the notebook list (a long-press on a row selects it; the selection stays until it is cleared)'
# (round 8) addRecentFile calls setRecentDocuments only for a file that is neither the todo nor the quick-note file (AppSettings.java:396).
# The todo and quick-note pages are the only pages the notebook tab route reaches, so this call needs a notebook file opened in the editor.
NEED_OTHER_DOC = ('A notebook file other than the todo and quick-note pages is open in the editor (opened from the notebook list; '
                  'the todo and quick-note pages do not count)')
# document format states: the editor menu and the key handler are chosen by the document format (FormatRegistry), so every
# format-specific edge names the format it needs (the file name decides the format)
NEED_FMT = {
    'WIKITEXT': 'The open document uses the wikitext format (chosen by the file name or the format menu)',
    'MARKDOWN': 'The open document uses the markdown format (chosen by the file name or the format menu)',
    'TODOTXT': 'The open document uses the todo.txt format (chosen by the file name or the format menu)',
    'PLAINTEXT': 'The open document uses the plain text format (chosen by the file name or the format menu)',
    'ORGMODE': 'The open document uses the org-mode format (chosen by the file name or the format menu)',
    'ASCIIDOC': 'The open document uses the asciidoc format (chosen by the file name or the format menu)',
    'CSV': 'The open document uses the CSV format (chosen by the file name or the format menu)',
    'EMBED': 'The open document uses the embed-binary format (chosen by the file name or the format menu)',
    'KEYVALUE': 'The open document uses the key-value format (chosen by the file name or the format menu)',
}
# the Tab key indents the selected lines only when the editor setting "tab to indent" is on (off by default; ActionButtonBase.java:1038)
NEED_TAB_INDENT = 'The editor setting "tab to indent" is on (Settings, off by default); the Tab key then indents the lines'

ENV_KINDS_OF, STATE_KINDS_OF = {}, {}
ENV_KINDS_OF.update({ENV_LAUNCHER: ['other_app'], ENV_OTHER_APP: ['other_app'], ENV_ADB: ['other_app'], ENV_PICKER: ['other_app'],
                     ENV_PERM_MISSING: ['permission'], ENV_PERM_DIALOG: ['permission'], ENV_EXC: ['other']})
STATE_KINDS_OF.update({NEED_STARTUP_TAB: ['settings'], NEED_NOTE: ['file'], NEED_DOC_OPEN: ['session'], NEED_PREVIEW: ['session'],
                       NEED_SHORTCUT: ['settings'], NEED_APP_OPEN: ['session']})
STATE_KINDS_OF.update({v: ['file'] for v in NEED_FMT.values()})
STATE_KINDS_OF[NEED_TAB_INDENT] = ['settings']
STATE_KINDS_OF[NEED_SELECTED] = ['session']   # an earlier long-press in this session (the selection is in memory, not saved)
STATE_KINDS_OF[NEED_OTHER_DOC] = ['file']     # a file the user chose in the notebook (the same kind as NEED_NOTE)

# framework evidence (AOSP 8.1.0_r1 under work/fw_src; every line below was printed and checked)
FW_POST = ('FW-SRC core/java/android/os/Handler.java:355-358 (post), 427-430 (postDelayed), 97-107 (dispatchMessage runs the message callback), '
           '789-791 (handleCallback calls message.callback.run()): the Runnable runs on the handler thread')
FW_VIEW = ('FW-SRC core/java/android/view/View.java:6289-6296 (performClick calls the OnClickListener), 6331-6376 (performLongClick calls the '
           'OnLongClickListener), 11768-11774 (the touch listener), 6143-6170 (setOnClickListener / setOnLongClickListener register them); '
           'core/java/android/widget/AdapterView.java:314-321 (performItemClick calls the OnItemClickListener)')
FW_ACT = ('FW-SRC core/java/android/app/Activity.java:989 (onCreate), 1311 (onResume), 1331 (onPostResume), 3001-3010 (onBackPressed), '
          '5679 (onActivityResult), 824 (mResultCode defaults to RESULT_CANCELED)')
FW_RESULT = ('FW-SRC core/java/android/app/ActivityThread.java:4253-4265 (deliverResults hands the result to the activity), '
             'core/java/android/app/Activity.java:7259 (dispatchActivityResult ends in onActivityResult)')
FW_ASYNC = ('FW-SRC core/java/android/os/AsyncTask.java:594-596 (execute), 326-334 (the worker calls doInBackground), '
            '369-374 (postResult), 691-697 (finish calls onPostExecute)')
FW_BIND = 'INFERRED ButterKnife.bind(...) reflectively calls the generated X_ViewBinding(target, source) constructor (ButterKnife source not read)'
FW_FRAG = 'INFERRED androidx.fragment.app.FragmentManager drives the fragment lifecycle callbacks (androidx source not read)'
FW_APPINTRO = 'INFERRED com.github.appintro.AppIntro calls the onDonePressed / onNextPressed / onSkipPressed / onSlideChanged overrides of the activity (AppIntro library source not read)'
FW_VIEWPAGER = 'INFERRED androidx ViewPager2 calls the registered OnPageChangeCallback after the page changes (androidx source not read)'

# ------------------------------------------------------------------ pages (screens)
SCREENS = {
    'S_ENTRY': 'Outside the app: launcher icon, widget, pinned shortcut, another app or file manager, adb broadcast',
    'S_EXIT': 'The process ends (Back out of the last activity, or the system kills the process)',
    'S_NOTEBOOK': 'MainActivity, notebook tab: the file browser of the notebook folder (GsFileBrowserFragment) with the FAB and the bottom navigation',
    'S_NOTEBOOK_SEL': 'MainActivity, notebook tab with a selection: one or more rows are selected (after a long-press on a row); the info item of the toolbar menu acts on the selection',
    'S_TODO': 'MainActivity, todo tab: DocumentEditAndViewFragment for the todo.txt file',
    'S_QUICKNOTE': 'MainActivity, quick note tab: DocumentEditAndViewFragment for the quick note file',
    'S_MORE': 'MainActivity, more tab: MoreFragment with the info and links of the app',
    'S_NEWFILE': 'NewFileDialog (opened by the FAB): name, type, template',
    'S_DOCUMENT': 'DocumentActivity with DocumentEditAndViewFragment (the editor or the viewer of one file); variants per open mode',
    'S_SHARE_INTO': 'DocumentActivity with DocumentShareIntoFragment (text or file shared into Markor, choose the target file)',
    'S_SHARE_PICKER': 'DocumentShareIntoFragment: the folder browser opened by the share import (OK chooses the folder for the shared file)',
    'S_SETTINGS': 'SettingsActivity root: settings list with sub-screens',
    'S_ACTION_BUTTONS': 'ActionButtonSettingsActivity: order of the editor action buttons',
    'S_INTRO': 'IntroActivity: the AppIntro slides shown on the first start',
    'S_PERMISSION': 'StoragePermissionActivity: the storage permission request dialog (the app cannot run without it)',
    'S_EXT_APP': 'Another app or system screen without a result (share chooser, browser, viewer)',
    'S_WIDGET_CONFIG': 'WrWidgetConfigure: configuration screen of a notebook widget',
    'S_HOME_WIDGET_NOTEBOOK': 'Launcher home screen with the Markor notebook widget (WrMarkorWidgetProvider: buttons and the file list)',
    'S_HOME_WIDGET_TODO': 'Launcher home screen with the Markor todo widget (TodoWidgetProvider: the todo list and its header)',
}


def gui(src, dst, text, kind='GUI', **kw):
    e(src, dst, kind, text, gui=[text], **kw)


def sup(*pairs):
    for p in pairs:
        SUPPRESS.add(p)


# edge wrapper: records the hand-written (src, dst, kind) triples so the listener loop at the end does not add duplicates
_e_builtin = e
_HAND = set()
_EDGE_LOG = []     # every hand-written edge as (src, dst, kind), for the reachability search in section E


def e(src, dst, kind, trigger, **kw):
    _HAND.add((src, dst, kind))
    _EDGE_LOG.append((src, dst, kind))
    _e_builtin(src, dst, kind, trigger, **kw)


# ================================================================== A. process start, launcher, lifecycle, first visible tab
# cold start: the process starts before any component, so Application.onCreate runs first. Every component that the launcher or
# another app starts from a cold process hangs off ApplicationObject.onCreate (this node), not off S_ENTRY (cold-start fix, this pass).
e('S_ENTRY', 'ApplicationObject.<init>', 'ENTRY', 'The process starts when the launcher icon is tapped (before any activity)',
  gui=['Tap the Markor launcher icon'], evidence='SRC AndroidManifest.xml:39-40')
e('ApplicationObject.<init>', 'ApplicationObject.onCreate', 'LIFECYCLE', 'The system calls Application.onCreate',
  evidence='SRC ApplicationObject.java:16,39')
e('ApplicationObject.onCreate', 'MainActivity.<init>', 'ENTRY', 'The MAIN / LAUNCHER intent starts MainActivity (after Application.onCreate on a cold start)',
  gui=['Tap the Markor launcher icon'], evidence='SRC AndroidManifest.xml:61-71; FW-SRC core/java/android/app/ActivityThread.java:5740 (callApplicationOnCreate runs before the first activity)')
e('MainActivity.<init>', 'MainActivity.<clinit>', 'LIFECYCLE', 'class initialisation before the first instance',
  evidence='INFERRED the JVM runs the static initialiser of a class before its first instance (Java language rule, not read from a source)')
e('MainActivity.<init>', 'MainActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC MainActivity.java:76; ' + FW_ACT)
# cold-start order: the direct MainActivity.<init> -> onResume and -> onPostResume edges skipped onCreate and are removed.
# Method used for the cold start: MainActivity.<init> -> MainActivity.onCreate -> MainActivity.onResume -> MainActivity.onPostResume -> MainActivity.onPause.
# Every route that resumes or pauses MainActivity goes through onCreate first, so no direct <init> -> onResume edge is kept.
# An activity instance is never resumed before its own onCreate, so the STATE option ('resumed before in this process') does not apply.
e('MainActivity.onCreate', 'MainActivity.onResume', 'LIFECYCLE', 'The system calls Activity.onStart and then Activity.onResume after onCreate returns (cold start)',
  evidence='SRC MainActivity.java:76,279; FW-SRC core/java/android/app/ActivityThread.java:2729 (callActivityOnCreate), 2741 (performStart), 2950 (performResume)')
e('MainActivity.onResume', 'MainActivity.onPostResume', 'LIFECYCLE', 'Activity.performResume calls onPostResume after onResume',
  evidence='SRC MainActivity.java:317; FW-SRC core/java/android/app/Activity.java:7098-7131 (onPostResume at 7131)')

# the first page: ViewPager2 shows position 0 (notebook) once the adapter is set in onCreate (tabIdToPos: notebook -> 0).
# Cold-start state: the notebook is the default startup tab (AppSettings.java:781 default R.id.nav_notebook), and
# MainActivity.onActivityFirstTimeVisible (MainActivity.java:142-144) switches tabs only when the setting is not the notebook.
# So on a fresh install the notebook is the visible, resumed page after a cold start.
# The notebook page is entered from onPostResume, the resumed step: the pager page is shown only after onResume (Activity.java:7107)
# and onPostResume (Activity.java:7131), so an edge from onCreate would skip the resume. Route: <init> -> onCreate -> onResume -> onPostResume -> S_NOTEBOOK.
e('MainActivity.onPostResume', 'S_NOTEBOOK', 'ENTERS', 'The notebook tab is the first page the pager shows (position 0); it is the default startup tab, so it is the visible page after a cold start',
  evidence='SRC MainActivity.java:105-106; SRC AppSettings.java:781; SRC MainActivity.java:142-144; FW-SRC core/java/android/app/Activity.java:7098-7131; ' + FW_VIEWPAGER)
# the listener and the plus button are wired in onCreate, but the user taps them on a shown page. The registration edges
# from onCreate are dropped (_REG_SKIP, section D), so the routes go <init> -> onCreate -> onResume -> onPostResume -> S_NOTEBOOK -> tap -> listener / onClickFab.

# the bottom navigation: the taps are GUI edges from each shown tab page to the listener lambda (the extractor records the
# lambda creation as REGISTER, which the reachability search does not follow, so the taps are written here)
for pg in ('S_NOTEBOOK', 'S_TODO', 'S_QUICKNOTE', 'S_MORE'):
    gui(pg, 'MainActivity.lambda$onCreate$0', 'Tap a bottom navigation tab',
        evidence='SRC MainActivity.java:109-114; INFERRED the BottomNavigationView calls the listener on a tap (material library source not read)')
e('MainActivity.lambda$onCreate$0', 'S_TODO', 'ENTERS', 'Tab Todo is shown (the listener selects its position)',
  evidence='SRC MainActivity.java:109-114; ' + FW_VIEWPAGER)
e('MainActivity.lambda$onCreate$0', 'S_QUICKNOTE', 'ENTERS', 'Tab Quick note is shown (the listener selects its position)',
  evidence='SRC MainActivity.java:109-114; ' + FW_VIEWPAGER)
e('MainActivity.lambda$onCreate$0', 'S_MORE', 'ENTERS', 'Tab More is shown (the listener selects its position)',
  evidence='SRC MainActivity.java:109-114; ' + FW_VIEWPAGER)
e('MainActivity.lambda$onCreate$0', 'S_NOTEBOOK', 'ENTERS', 'Tab Notebook is shown (the listener selects its position)',
  evidence='SRC MainActivity.java:109-114; ' + FW_VIEWPAGER)
# the page-change callback is called by the pager after the listener or the startup code changes the page
e('MainActivity.lambda$onCreate$0', 'MainActivity$1.onPageSelected', 'FRAMEWORK', 'The pager calls the registered page-change callback after setCurrentItem',
  evidence='SRC MainActivity.java:93-99, 111-112; ' + FW_VIEWPAGER)

# first visible: GsActivityBase posts onActivityFirstTimeVisible on the first resume without saved state
# per-class edge (not from the shared GsActivityBase.onPostResume, which would give false routes into other activities)
e('MainActivity.onPostResume', 'MainActivity.onActivityFirstTimeVisible', 'FRAMEWORK',
  'MainActivity.onPostResume calls super, and the base class posts onActivityFirstTimeVisible on the main looper '
  '(only on a cold start: no saved instance state); this edge shortens the super step to save a shared base node',
  evidence=FW_POST + '; SRC GsActivityBase.java:101-108; SRC MainActivity.java:317-319 (super.onPostResume at 318)')
# startup tab: the Runnable posted with a 100 ms delay selects the tab from the settings (not used when an intent names a file)
e('MainActivity.onActivityFirstTimeVisible', 'MainActivity.lambda$onActivityFirstTimeVisible$1', 'FRAMEWORK',
  'View.postDelayed runs the startup-tab Runnable after 100 ms (only when the startup tab is not Notebook and the intent names no file)',
  needs_state=NEED_STARTUP_TAB, guard='startup tab preference is not Notebook, and no file is requested by the intent',
  evidence='SRC MainActivity.java:139-146; INFERRED View.postDelayed runs the Runnable on the view handler (View.java postDelayed not read)')
for tab_state, pg in (('Todo', 'S_TODO'), ('Quick note', 'S_QUICKNOTE'), ('More', 'S_MORE')):
    e('MainActivity.lambda$onActivityFirstTimeVisible$1', pg, 'ENTERS', 'The startup tab %s is shown' % tab_state,
      needs_state=NEED_STARTUP_TAB, guard='startup tab preference is %s' % tab_state,
      evidence='SRC MainActivity.java:143-146; ' + FW_VIEWPAGER)
e('MainActivity.lambda$onActivityFirstTimeVisible$1', 'MainActivity$1.onPageSelected', 'FRAMEWORK', 'The pager calls the page-change callback after setCurrentItem',
  evidence='SRC MainActivity.java:93-99, 144; ' + FW_VIEWPAGER)
# (More fix) the startup tab More realizes the More page through its own variant (the generic page-change callback no longer does)
e('MainActivity.lambda$onActivityFirstTimeVisible$1', 'MainActivity.onViewPagerPageSelected@MORE', 'FRAMEWORK',
  'The startup tab More is selected: the pager realizes the More page', needs_state=NEED_STARTUP_TAB,
  guard='startup tab preference is More', evidence='SRC MainActivity.java:143-146; ' + FW_VIEWPAGER)

# ================================================================== B. other entries: other-app intents, storage permission activity, home-screen widgets and their list services, configuration, shortcuts
# B1 another app sends or opens a file with Markor (manifest 187-225). DocumentActivity has the standard launch mode (manifest 190).
# (S4 fix, sample routes 1 and 5) the other-app entry runs its own context chain (@SEND). The in-app launch (DocumentActivity.launch)
# reaches the plain DocumentActivity.<init>, onCreate and handleLaunchingIntent nodes, so the share-into branch must not sit there.
e('ApplicationObject.onCreate', 'DocumentActivity.<init>@SEND', 'ENTRY', 'Another app sends a text or a file to Markor (share sheet, Open with, Edit with); on a cold start Application.onCreate runs first',
  gui=['Share or open a file from another app and choose Markor'], env=ENV_OTHER_APP, evidence='SRC AndroidManifest.xml:187-225')
e('DocumentActivity.<init>@SEND', 'DocumentActivity.onCreate@SEND', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC DocumentActivity.java:135; ' + FW_ACT)
# cold-start order for the other-app chain: onResume follows onCreate (not <init>), and the pages that handleLaunchingIntent commits in
# onCreate (the editor and the share-into screen) are shown from this resumed step, so they are entered from onResume@SEND, not from onCreate.
# The variant keeps the in-app chain (plain onResume) apart from this chain.
e('DocumentActivity.onCreate@SEND', 'DocumentActivity.onResume@SEND', 'LIFECYCLE', 'The system calls Activity.onResume after onCreate (cold start, other-app intent)',
  evidence='SRC DocumentActivity.java:310-313; FW-SRC core/java/android/app/Activity.java:7098-7131 (performResume: execPendingActions 7101, onResume 7107, dispatchResume and execPendingActions 7128-7129)')
for _rs in ('DocumentActivity.onResume', 'DocumentActivity.onResume@SEND', 'DocumentActivity.onResume@EDIT', 'DocumentActivity.onResume@SHARE'):
    e(_rs, 'GsActivityBase.onPostResume', 'LIFECYCLE', 'Activity.performResume calls onPostResume after onResume (not overridden by DocumentActivity)',
      evidence='SRC GsActivityBase.java:101-108; FW-SRC core/java/android/app/Activity.java:7098-7131 (onPostResume at 7131)')
e('DocumentActivity.onCreate', 'DocumentActivity.handleLaunchingIntent', 'CALL',
  'onCreate hands the launching intent to handleLaunchingIntent (the in-app launch; the bytecode call is replaced by this edge)',
  evidence='SRC DocumentActivity.java:149 (bytecode)')
e('DocumentActivity.onCreate@SEND', 'DocumentActivity.handleLaunchingIntent@SEND', 'CALL',
  'onCreate hands the other-app intent to handleLaunchingIntent (the @SEND chain)',
  evidence='SRC DocumentActivity.java:149 (bytecode)')
e('DocumentActivity.launch(Activity,File,Boolean,Integer,boolean)', 'DocumentActivity.<init>', 'INTENT',
  'The app starts DocumentActivity with an explicit intent (startActivity)',
  guard=['not (activity == null || file == null) (early return at DocumentActivity.java:71-73)',
         'not (GsFileUtils.getFilenameExtension(file).equals(".apk")) (early return at DocumentActivity.java:75-78)',
         'not (!forceOpenInThisApp && file.isFile() && !FormatRegistry.isFileSupported(file)) (early return at DocumentActivity.java:80-83)'],
  evidence='SRC DocumentActivity.java:116')
e('DocumentActivity.<init>', 'DocumentActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC DocumentActivity.java:135; ' + FW_ACT)
e('DocumentActivity.onCreate', 'DocumentActivity.onResume', 'LIFECYCLE', 'The system calls Activity.onResume after onCreate (cold start)',
  evidence='SRC DocumentActivity.java:310; ' + FW_ACT)

# B2 storage permission: DocumentActivity.onCreate asks for it; StoragePermissionActivity opens only when the permission is missing
e('StoragePermissionActivity.requestPermissions', 'StoragePermissionActivity.<init>', 'INTENT',
  'The storage permission is missing: the caller starts StoragePermissionActivity and finishes', env=ENV_PERM_MISSING,
  evidence='SRC StoragePermissionActivity.java:18-22')
# cold-start chain for this instance: the class has no own onCreate, onResume or onPostResume, so the chain uses per-instance context
# variants (@PERM) of the inherited nodes. The shared nodes would let other activities' resumes reach this class's first-visible hook.
e('StoragePermissionActivity.<init>', 'MarkorBaseActivity.onCreate@PERM', 'LIFECYCLE', 'The system calls Activity.onCreate (the class has no own onCreate)',
  evidence='SRC StoragePermissionActivity.java:14; ' + FW_ACT)
e('MarkorBaseActivity.onCreate@PERM', 'GsActivityBase.onResume@PERM', 'LIFECYCLE', 'The system calls Activity.onStart and then onResume after onCreate (the class has no own onResume)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729, 2741, 2950; SRC MarkorBaseActivity.java:21')
e('GsActivityBase.onResume@PERM', 'GsActivityBase.onPostResume@PERM', 'LIFECYCLE', 'Activity.performResume calls onPostResume after onResume',
  evidence='FW-SRC core/java/android/app/Activity.java:7098-7131; SRC GsActivityBase.java:101-108')
e('GsActivityBase.onPostResume@PERM', 'StoragePermissionActivity.onActivityFirstTimeVisible', 'FRAMEWORK',
  'The base onPostResume posts onActivityFirstTimeVisible; the override in this class runs on a cold start',
  evidence=FW_POST + '; SRC GsActivityBase.java:101-108; SRC StoragePermissionActivity.java:27-30')
e('StoragePermissionActivity.askForPermissions', 'S_PERMISSION', 'ENTERS', 'The storage permission dialog is shown',
  evidence='SRC StoragePermissionActivity.java:32-41')
gui('S_PERMISSION', 'StoragePermissionActivity.lambda$askForPermissions$0', 'Tap Exit in the dialog (the activity finishes)',
    evidence='SRC StoragePermissionActivity.java:35')
gui('S_PERMISSION', 'StoragePermissionActivity.lambda$askForPermissions$1', 'Tap Yes in the dialog (the storage permission is requested)',
    evidence='SRC StoragePermissionActivity.java:36-39')
e('StoragePermissionActivity.lambda$askForPermissions$1', 'StoragePermissionActivity.onRequestPermissionsResult', 'FRAMEWORK',
  'The system permission dialog answers; the framework calls onRequestPermissionsResult', env=ENV_PERM_DIALOG,
  evidence='SRC GsContextUtils.java:2400 (ActivityCompat.requestPermissions, API 27 branch); SRC StoragePermissionActivity.java:64; '
           'INFERRED ActivityCompat calls the activity callback (androidx source not read)')
e('StoragePermissionActivity.processPermissionState', 'MainActivity.<init>', 'INTENT',
  'The permission is granted: the activity opens MainActivity through animateToActivity and finishes', guard='the storage permission check passes',
  evidence='SRC StoragePermissionActivity.java:51-52; SRC GsContextUtils.java:1116-1117 (animateToActivity to the class), 1128-1138 (startActivity, then finish)')

# B3 home screen widgets: the launcher places them; the provider's onUpdate sets their views and their buttons
e('ApplicationObject.onCreate', 'WrMarkorWidgetProvider.<init>', 'ENTRY', 'The launcher adds the Markor notebook widget to the home screen (cold start: Application.onCreate first)',
  gui=['Add the Markor notebook widget to the home screen'], env=ENV_LAUNCHER, evidence='SRC AndroidManifest.xml:99-108')
e('WrMarkorWidgetProvider.<init>', 'WrMarkorWidgetProvider.onUpdate', 'FRAMEWORK',
  'AppWidgetProvider.onReceive gets ACTION_APPWIDGET_UPDATE and calls onUpdate',
  evidence='SRC WrMarkorWidgetProvider.java:40; FW-SRC core/java/android/appwidget/AppWidgetProvider.java:61-66')
e('WrMarkorWidgetProvider.updateLauncherWidgets', 'WrMarkorWidgetProvider.onUpdate', 'SYSTEM',
  'The app sends ACTION_APPWIDGET_UPDATE to its own provider to refresh the views',
  evidence='SRC WrMarkorWidgetProvider.java:118-134; FW-SRC core/java/android/appwidget/AppWidgetProvider.java:61-66')
e('WrMarkorWidgetProvider.onUpdate', 'S_HOME_WIDGET_NOTEBOOK', 'ENTERS', 'The launcher shows the notebook widget with its buttons',
  evidence='SRC WrMarkorWidgetProvider.java:40-114')
gui('S_HOME_WIDGET_NOTEBOOK', 'OpenFromShortcutOrWidgetActivity.<init>', 'Tap a button of the notebook widget (new note, quick note, todo, note list)',
    env=ENV_LAUNCHER, evidence='SRC WrMarkorWidgetProvider.java:60-107')
gui('S_HOME_WIDGET_NOTEBOOK', 'MainActivity.<init>', 'Tap the folder header or the home button of the notebook widget (the notebook opens)',
    env=ENV_LAUNCHER, evidence='SRC WrMarkorWidgetProvider.java:67-93')
gui('S_HOME_WIDGET_NOTEBOOK', 'MainActivity.onNewIntent', 'Tap the folder header or the home button while Markor is open (singleTop)',
    needs_state=NEED_APP_OPEN, env=ENV_LAUNCHER, evidence='SRC AndroidManifest.xml:65 (singleTop); SRC WrMarkorWidgetProvider.java:67-93; SRC MainActivity.java:223')
e('ApplicationObject.onCreate', 'TodoWidgetProvider.<init>', 'ENTRY', 'The launcher adds the Markor todo widget to the home screen (cold start: Application.onCreate first)',
  gui=['Add the Markor todo widget to the home screen'], env=ENV_LAUNCHER, evidence='SRC AndroidManifest.xml:114-123')
e('TodoWidgetProvider.<init>', 'TodoWidgetProvider.onUpdate', 'FRAMEWORK',
  'AppWidgetProvider.onReceive gets ACTION_APPWIDGET_UPDATE and calls onUpdate',
  evidence='SRC TodoWidgetProvider.java:21; FW-SRC core/java/android/appwidget/AppWidgetProvider.java:61-66')
e('TodoWidgetProvider.updateTodoWidgets', 'TodoWidgetProvider.onUpdate', 'SYSTEM',
  'The app sends ACTION_APPWIDGET_UPDATE to its own provider to refresh the views',
  evidence='SRC TodoWidgetProvider.java:52-68; FW-SRC core/java/android/appwidget/AppWidgetProvider.java:61-66')
e('TodoWidgetProvider.onUpdate', 'S_HOME_WIDGET_TODO', 'ENTERS', 'The launcher shows the todo widget list and its buttons',
  evidence='SRC TodoWidgetProvider.java:21-42')
gui('S_HOME_WIDGET_TODO', 'OpenFromShortcutOrWidgetActivity.<init>', 'Tap a todo in the todo widget list or its header',
    env=ENV_LAUNCHER, evidence='SRC TodoWidgetProvider.java:38-42')

# B4 list services of the widgets: the launcher binds them (setRemoteAdapter); RemoteViewsService.onBind calls onGetViewFactory and factory.onCreate
e('TodoWidgetProvider.onUpdate', 'TodoWidgetService.<init>', 'SYSTEM', 'The launcher binds the todo list service named by setRemoteAdapter',
  env=ENV_LAUNCHER, evidence='SRC TodoWidgetProvider.java:33-34; SRC AndroidManifest.xml:125-127; FW-SRC core/java/android/widget/RemoteViewsService.java:235-241')
# Service lifecycle (round 7): Service.onCreate and RemoteViewsService.onBind are framework nodes (FRAMEWORK_NODES, below). The app
# declares neither, so the chain is <init> -> onCreate -> onBind -> onGetViewFactory, each step a LIFECYCLE edge.
e('TodoWidgetService.<init>', 'TodoWidgetService.onCreate', 'LIFECYCLE',
  'The framework creates the service (ActivityThread.handleCreateService) and calls Service.onCreate (not overridden in the app)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3311 (handleCreateService), 3339 (service.onCreate()); FW-SRC core/java/android/app/Service.java:343 (public void onCreate); SRC TodoWidgetService.java:8-10')
e('TodoWidgetService.onCreate', 'TodoWidgetService.onBind', 'LIFECYCLE',
  'handleBindService calls the service onBind (RemoteViewsService.onBind, not overridden in the app)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3356 (handleBindService), 3366 (s.onBind); FW-SRC core/java/android/widget/RemoteViewsService.java:235-244 (onBind), 257 (abstract)')
e('TodoWidgetService.onBind', 'TodoWidgetService.onGetViewFactory', 'LIFECYCLE',
  'RemoteViewsService.onBind calls onGetViewFactory, which the app overrides',
  evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:235-244 (onBind calls onGetViewFactory), 257 (abstract); SRC TodoWidgetService.java:8-10')
e('TodoWidgetService.onGetViewFactory', 'TodoWidgetRemoteViewsFactory.onCreate', 'FRAMEWORK', 'onBind calls factory.onCreate on the new factory',
  evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; SRC TodoWidgetService.java:8-10')
e('TodoWidgetRemoteViewsFactory.onCreate', 'TodoWidgetRemoteViewsFactory.onDataSetChanged', 'FRAMEWORK',
  'The launcher asks for the list data; the adapter calls factory.onDataSetChanged',
  evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:140-142; SRC TodoWidgetRemoteViewsFactory.java:31-36')
e('TodoWidgetRemoteViewsFactory.onCreate', 'TodoWidgetRemoteViewsFactory.onDestroy', 'FRAMEWORK',
  'The launcher drops the list; the adapter calls factory.onDestroy',
  evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:214-222; SRC TodoWidgetRemoteViewsFactory.java:47')
for m, fw_ln, src_ln in (('getCount', 154, 52), ('getViewAt', 164, 57), ('getLoadingView', 177, 70),
                         ('getViewTypeCount', 187, 75), ('getItemId', 197, 80), ('hasStableIds', 207, 85)):
    e('TodoWidgetRemoteViewsFactory.onDataSetChanged', 'TodoWidgetRemoteViewsFactory.%s' % m, 'FRAMEWORK',
      'The launcher asks the adapter for the list (%s); the adapter calls factory.%s' % (m, m),
      evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:%d; SRC TodoWidgetRemoteViewsFactory.java:%d' % (fw_ln, src_ln))

e('WrMarkorWidgetProvider.onUpdate', 'WrFilesWidgetService.<init>', 'SYSTEM', 'The launcher binds the notebook list service named by setRemoteAdapter',
  env=ENV_LAUNCHER, evidence='SRC WrMarkorWidgetProvider.java:98-104; SRC AndroidManifest.xml:110-112; FW-SRC core/java/android/widget/RemoteViewsService.java:235-241')
# Service lifecycle (round 7): the same chain as the todo service, with its own nodes.
e('WrFilesWidgetService.<init>', 'WrFilesWidgetService.onCreate', 'LIFECYCLE',
  'The framework creates the service (ActivityThread.handleCreateService) and calls Service.onCreate (not overridden in the app)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3311 (handleCreateService), 3339 (service.onCreate()); FW-SRC core/java/android/app/Service.java:343 (public void onCreate); SRC WrFilesWidgetService.java:17-19')
e('WrFilesWidgetService.onCreate', 'WrFilesWidgetService.onBind', 'LIFECYCLE',
  'handleBindService calls the service onBind (RemoteViewsService.onBind, not overridden in the app)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3356 (handleBindService), 3366 (s.onBind); FW-SRC core/java/android/widget/RemoteViewsService.java:235-244 (onBind), 257 (abstract)')
e('WrFilesWidgetService.onBind', 'WrFilesWidgetService.onGetViewFactory', 'LIFECYCLE',
  'RemoteViewsService.onBind calls onGetViewFactory, which the app overrides',
  evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:235-244 (onBind calls onGetViewFactory), 257 (abstract); SRC WrFilesWidgetService.java:17-19')
e('WrFilesWidgetService.onGetViewFactory', 'WrFilesWidgetFactory.onCreate', 'FRAMEWORK', 'onBind calls factory.onCreate on the new factory',
  evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; SRC WrFilesWidgetService.java:17-19')
e('WrFilesWidgetFactory.onCreate', 'WrFilesWidgetFactory.onDataSetChanged', 'FRAMEWORK',
  'The launcher asks for the list data; the adapter calls factory.onDataSetChanged',
  evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:140-142; SRC WrFilesWidgetFactory.java:43-48')
e('WrFilesWidgetFactory.onDataSetChanged', 'WrFilesWidgetFactory.lambda$onDataSetChanged$0', 'FRAMEWORK',
  'File.listFiles calls the filter lambda for each file of the notebook folder',
  evidence='SRC WrFilesWidgetFactory.java:62; INFERRED File.listFiles calls the FileFilter (JDK source not read)')
e('WrFilesWidgetFactory.onCreate', 'WrFilesWidgetFactory.onDestroy', 'FRAMEWORK', 'The launcher drops the list; the adapter calls factory.onDestroy',
  evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:214-222; SRC WrFilesWidgetFactory.java:70')
for m, fw_ln, src_ln in (('getCount', 154, 75), ('getViewAt', 164, 80), ('getLoadingView', 177, 95),
                         ('getViewTypeCount', 187, 100), ('getItemId', 197, 105), ('hasStableIds', 207, 110)):
    e('WrFilesWidgetFactory.onDataSetChanged', 'WrFilesWidgetFactory.%s' % m, 'FRAMEWORK',
      'The launcher asks the adapter for the list (%s); the adapter calls factory.%s' % (m, m),
      evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:%d; SRC WrFilesWidgetFactory.java:%d' % (fw_ln, src_ln))

# B5 widget configuration screen (manifest 91-97): the launcher opens it when the widget is added; the folder browser picks the notebook folder
e('ApplicationObject.onCreate', 'WrWidgetConfigure.<init>', 'ENTRY', 'The launcher opens the notebook widget setup when the widget is added (cold start: Application.onCreate first)',
  gui=['Add the notebook widget: the setup screen opens and asks for a folder'], env=ENV_LAUNCHER, evidence='SRC AndroidManifest.xml:91-97')
e('WrWidgetConfigure.<init>', 'WrWidgetConfigure.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC WrWidgetConfigure.java:35; ' + FW_ACT)
# the folder browser is created in onCreate (WrWidgetConfigure.java:44) but shown from the resumed step, so it is entered from that step
# (the same rule as DocumentActivity and SettingsActivity). MarkorBaseActivity has no onResume of its own (MarkorBaseActivity.java has none).
e('WrWidgetConfigure.onCreate', 'GsActivityBase.onResume@WRCONFIG', 'LIFECYCLE',
  'The system calls Activity.onResume after onCreate (WrWidgetConfigure and MarkorBaseActivity have no own onResume; the inherited GsActivityBase.onResume runs)',
  evidence='SRC WrWidgetConfigure.java:28 (extends MarkorBaseActivity), 35; SRC MarkorBaseActivity.java:18; ' + FW_ACT + '; SRC GsActivityBase.java:86-99')
e('GsActivityBase.onResume@WRCONFIG', 'S_WIDGET_CONFIG', 'ENTERS', 'The folder browser for the widget folder is shown',
  evidence='SRC WrWidgetConfigure.java:44, 56-58; SRC GsActivityBase.java:86-99; FW-SRC core/java/android/app/Activity.java:7098-7131')
gui('S_WIDGET_CONFIG', 'WrWidgetConfigure$1.onFsViewerSelected', 'Pick a folder in the browser and tap Select',
    evidence='SRC WrWidgetConfigure.java:60-64')
gui('S_WIDGET_CONFIG', 'WrWidgetConfigure$1.onFsViewerCancel', 'Cancel the folder browser',
    evidence='SRC WrWidgetConfigure.java:73-75')
e('WrWidgetConfigure$1.onFsViewerSelected', 'WrWidgetConfigure.onStop', 'FRAMEWORK',
  'finish() ends the screen and the system calls onStop, which refreshes the widgets',
  evidence='SRC WrWidgetConfigure.java:61-63, 49-52; FW-SRC core/java/android/app/Activity.java:5526 (finish), 1858 (onStop)')
e('WrWidgetConfigure$1.onFsViewerCancel', 'WrWidgetConfigure.onStop', 'FRAMEWORK',
  'finish() ends the screen and the system calls onStop',
  evidence='SRC WrWidgetConfigure.java:73-75; FW-SRC core/java/android/app/Activity.java:5526 (finish), 1858 (onStop)')

# B6 shortcuts and the open-from-widget activity (manifest 182-185, standard launch mode)
e('OpenFromShortcutOrWidgetActivity.<init>', 'OpenFromShortcutOrWidgetActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC OpenFromShortcutOrWidgetActivity.java:16-19; ' + FW_ACT)
e('ApplicationObject.onCreate', 'OpenFromShortcutOrWidgetActivity.<init>', 'ENTRY', 'The launcher opens a dynamic shortcut for a recent file (long-press the app icon; cold start: Application.onCreate first)',
  gui=['Long-press the Markor icon and tap a recent file'], env=ENV_LAUNCHER, needs_state=NEED_SHORTCUT,
  evidence='SRC AppSettings.java:382-398 (addRecentFile calls ShortcutUtils.setShortcuts); SRC ShortcutUtils.java:65, 79, 98')

# ------------------------------------------------------------------ edge classes: components started by the launcher or another app through a manifest entry
def CLASSIFY(x):
    ev = (x['evidence'] or '') + ' ' + (x['trigger'] or '')
    dst = x['dst'].split('@')[0]
    if x['kind'] in ('ENTRY', 'SYSTEM', 'INTENT') and 'AndroidManifest' in ev and dst.endswith('.<init>') and not dst.startswith('ApplicationObject.'):
        return ('non_standard', 'manifest component started by the launcher or another app through an intent action (resolved by the manifest, not by the app)')
    return None


# ================================================================== C. MainActivity callbacks and results, tab fragments, intro, settings, editor callbacks
NEED_FIRST_START = 'Markor has not shown the intro before (first start, or the app data was cleared): the intro flag is not set'
NEED_RECREATE_MAIN = 'A setting that needs the main screen to restart was changed in Settings (AppSettings.setRecreateMainRequired)'
NEED_SAF_TREE = 'The notebook folder is on storage that needs the storage access framework (removable SD card), and no tree is granted yet'
NEED_SAVED_STATE = 'The activity is recreated from saved state (a configuration change, or the system killed the app in the background)'
STATE_KINDS_OF.update({NEED_FIRST_START: ['settings'], NEED_RECREATE_MAIN: ['settings'], NEED_SAF_TREE: ['settings'],
                       NEED_SAVED_STATE: ['session']})
FW_PAUSE = 'FW-SRC core/java/android/app/Activity.java:1673 (onPause), 5526 (finish), 1858 (onStop)'
FW_DIALOG = 'INFERRED androidx DialogFragment.show makes the framework call onCreateDialog (androidx source not read)'
FW_MENU = 'INFERRED AppCompat calls onCreateOptionsMenu when the toolbar menu is built (androidx source not read)'
FW_SAVE = 'INFERRED the framework saves the activity and fragment state when the activity leaves the foreground (AOSP order not read)'

# C1 MainActivity pager: the first tab fragment is created after setAdapter; the FragmentManager runs the fragment lifecycle
e('MainActivity.onCreate', 'MainActivity$SectionsPagerAdapter.createFragment', 'FRAMEWORK',
  'After setAdapter the pager asks the adapter for the first page fragment (the notebook tab)',
  evidence='SRC MainActivity.java:105-106, 509-526; ' + FW_VIEWPAGER)
e('MainActivity$SectionsPagerAdapter.createFragment', 'GsFileBrowserFragment.onViewCreated', 'FRAMEWORK',
  'The FragmentManager attaches the notebook fragment and creates its view',
  evidence='SRC MainActivity.java:509-526; SRC GsFileBrowserFragment.java:107; ' + FW_FRAG)
e('GsFileBrowserFragment.onViewCreated', 'GsFileBrowserFragment.onViewStateRestored', 'FRAMEWORK',
  'The FragmentManager restores the saved view state after the view is created',
  evidence='SRC GsFileBrowserFragment.java:335; ' + FW_FRAG)
e('MainActivity$SectionsPagerAdapter.createFragment', 'GsFileBrowserFragment.onResume', 'FRAMEWORK',
  'The FragmentManager resumes the visible notebook fragment',
  evidence='SRC GsFileBrowserFragment.java:345; ' + FW_FRAG)
# menu order (fix 6): the fragment menu comes from FragmentManager.dispatchCreateOptionsMenu (needs CREATED or later, FragmentManager.java:3108-3109),
# called by Activity.onCreatePanelMenu (Activity.java:3386-3389). AOSP does not pin the first panel build before the resume step, so the
# edge is drawn after GsFileBrowserFragment.onResume (the resume dispatch is Activity.java:7128-7129). The route is createFragment -> onResume -> onCreateOptionsMenu.
e('GsFileBrowserFragment.onResume', 'GsFileBrowserFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'The notebook fragment adds its menu to the toolbar once it is resumed (modelled order, see readme_notes.md Limits)',
  evidence='FW-SRC core/java/android/app/FragmentManager.java:3108-3109; FW-SRC core/java/android/app/Activity.java:3386-3389, 7128-7129; SRC GsFileBrowserFragment.java:357; ' + FW_MENU)
e('MainActivity.onSaveInstanceState', 'GsFileBrowserFragment.onSaveInstanceState', 'FRAMEWORK',
  'The activity state includes the notebook fragment state',
  evidence='SRC MainActivity.java:154; SRC GsFileBrowserFragment.java:329; ' + FW_SAVE)

# todo, quick note and more pages: a tab page is created only after its tab is realized (MainActivity.java:446 ensureRealized, run by
# onViewPagerPageSelected). createFragment also runs once at the cold start (the notebook is the only real page then), so the branch
# calls of the other tabs are suppressed from createFragment (sup below) and drawn from onViewPagerPageSelected instead (E1 fix).
_REALIZED_BRANCH = ('Realized tab: the pager asks createFragment for the page after ensureRealized, and the branch of this tab makes '
                    'the call (INFERRED pager path; androidx FragmentStateAdapter source not read)')
sup(('MainActivity$SectionsPagerAdapter.createFragment', 'DocumentEditAndViewFragment.newInstance'),
    ('MainActivity$SectionsPagerAdapter.createFragment', 'MoreFragment.newInstance'),
    ('MainActivity$SectionsPagerAdapter.createFragment', 'Document.<init>'),
    ('MainActivity$SectionsPagerAdapter.createFragment', 'AppSettings.getTodoFile'),
    ('MainActivity$SectionsPagerAdapter.createFragment', 'AppSettings.getQuickNoteFile'),
    ('MainActivity$SectionsPagerAdapter.createFragment', 'DocumentEditAndViewFragment.<clinit>'))
for _dst in ('DocumentEditAndViewFragment.newInstance', 'Document.<init>', 'AppSettings.getTodoFile',
             'AppSettings.getQuickNoteFile', 'DocumentEditAndViewFragment.<clinit>'):
    e('MainActivity.onViewPagerPageSelected', _dst, 'CALL', _REALIZED_BRANCH,
      evidence='SRC MainActivity.java:446 (ensureRealized), 515-518 (createFragment todo and quick note branches, bytecode call)')
# (More fix, sample route 4) onViewPagerPageSelected runs on every page change, so the More page is realized only through its own
# variant @MORE, which the tap on the More tab reaches (see the More page block below).
e('MainActivity.onViewPagerPageSelected@MORE', 'MoreFragment.newInstance', 'CALL', _REALIZED_BRANCH,
  evidence='SRC MainActivity.java:446 (ensureRealized), 519-520 (createFragment more branch, bytecode call)')
e('MainActivity.onViewPagerPageSelected', 'DocumentEditAndViewFragment.onCreate', 'FRAMEWORK',
  'The realized todo or quick note page is created by the pager; the FragmentManager runs its onCreate',
  guard=['_sectionsAdapter != null (the if at MainActivity.java:445 encloses ensureRealized at line 446)',
         'the realized tab is the quick note or the todo tab (the branches at MainActivity.java:515-518)'],
  evidence='SRC MainActivity.java:446, 515-518; SRC DocumentEditAndViewFragment.java:122; ' + FW_FRAG)
e('DocumentEditAndViewFragment.onCreate', 'DocumentEditAndViewFragment.onViewCreated', 'FRAMEWORK',
  'The FragmentManager creates the page view', evidence='SRC DocumentEditAndViewFragment.java:138; ' + FW_FRAG)
e('DocumentEditAndViewFragment.onViewCreated', 'DocumentEditAndViewFragment.onResume', 'FRAMEWORK',
  'The FragmentManager resumes the visible page', evidence='SRC DocumentEditAndViewFragment.java:265; ' + FW_FRAG)
# same menu order as the notebook (fix 6 rule): the page menu is drawn after the page resume step
e('DocumentEditAndViewFragment.onResume', 'DocumentEditAndViewFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'The page adds its editor menu to the toolbar once it is resumed (modelled order, see readme_notes.md Limits)',
  evidence='SRC DocumentEditAndViewFragment.java:299; FW-SRC core/java/android/app/FragmentManager.java:3108-3109; FW-SRC core/java/android/app/Activity.java:3386-3389; ' + FW_MENU)
# (first-visible fix, sample route 8) GsFragmentBase.checkRunFirstTimeVisible calls the first-visible hook of whatever page is visible, so
# from the notebook it reached the editor's hook. The base edge is suppressed; the editor runs its own first-visible check from its onResume.
sup(('GsFragmentBase.checkRunFirstTimeVisible', 'DocumentEditAndViewFragment.onFragmentFirstTimeVisible'))
e('DocumentEditAndViewFragment.onResume', 'DocumentEditAndViewFragment.onFragmentFirstTimeVisible', 'FRAMEWORK',
  'The editor page resumes and posts its first-visible check, which runs the editor own hook (the page loads its document)',
  evidence='SRC GsFragmentBase.java:152-156, 135-140; SRC DocumentEditAndViewFragment.java:241, 277; ' + FW_FRAG)
e('DocumentEditAndViewFragment.onResume', 'DocumentEditAndViewFragment.onPause', 'FRAMEWORK',
  'The page is left (another tab, another app, or the screen turns off)',
  evidence='SRC DocumentEditAndViewFragment.java:277; ' + FW_FRAG)
e('DocumentEditAndViewFragment.onPause', 'DocumentEditAndViewFragment.onSaveInstanceState', 'FRAMEWORK',
  'The page state is saved when the page is left', evidence='SRC DocumentEditAndViewFragment.java:293; ' + FW_SAVE)
e('DocumentEditAndViewFragment.onPause', 'DocumentEditAndViewFragment.onDestroy', 'FRAMEWORK',
  'The page is destroyed when its activity is finished', evidence='SRC DocumentEditAndViewFragment.java:1106; ' + FW_FRAG)
for pg in ('S_TODO', 'S_QUICKNOTE'):
    gui(pg, 'DocumentEditAndViewFragment.onOptionsItemSelected', 'Tap an item of the editor menu (todo or quick note)',
        evidence='SRC DocumentEditAndViewFragment.java:421; ' + FW_MENU)
# (toolbar fix, sample route 2) GsActivityBase.onToolbarClick hands the tap to the first visible page for every page, so the base
# edge is suppressed for the editor. The editor's title-click handler is reached only from the todo page's own toolbar tap.
sup(('GsActivityBase.onToolbarClick', 'DocumentEditAndViewFragment.onToolbarClicked'))
gui('S_TODO', 'DocumentEditAndViewFragment.onToolbarClicked', 'Tap the toolbar title of the todo page (the filter or the title action)',
    evidence='SRC GsActivityBase.java:110-120; SRC DocumentEditAndViewFragment.java:1090')
# (fix 3) GsActivityBase.onResume only registers the toolbar listener (GsActivityBase.java:94-98, when the toolbar exists). The tap is a user
# action on the notebook page, so the auto call edge GsActivityBase.onResume -> onToolbarClick is suppressed and the notebook tap is a GUI edge.
sup(('GsActivityBase.onResume', 'GsActivityBase.onToolbarClick'))
gui('S_NOTEBOOK', 'GsActivityBase.onToolbarClick', 'Tap the toolbar title of the notebook (the listener is set in GsActivityBase.onResume when the toolbar exists)',
    evidence='SRC GsActivityBase.java:94-98 (listener, toolbar != null), 116-124 (onToolbarClick hands the tap to the visible resumed page)')
# (notebook row tap) the row click is the adapter's onClick (SRC GsFileBrowserListAdapter.java:271). The auto FRAMEWORK edges from the
# object creation sites (GsFileBrowserFragment.onViewCreated line 123, and the adapter constructor) reach onClick without the notebook being
# resumed or visible, so both are suppressed and the tap is a GUI edge from the notebook page. The dialog's row tap has no page node here;
# its picker listeners are GUI edges of their own (S_SHARE_PICKER, S_WIDGET_CONFIG) or FRAMEWORK edges from their dialog creation.
sup(('GsFileBrowserFragment.onViewCreated', 'GsFileBrowserListAdapter.onClick'),
    ('GsFileBrowserListAdapter.<init>', 'GsFileBrowserListAdapter.onClick'))
gui('S_NOTEBOOK', 'GsFileBrowserListAdapter.onClick', 'Tap a file or folder in the notebook list (a folder opens; a file goes to the notebook listener)',
    evidence='SRC GsFileBrowserListAdapter.java:271 (row click listener), 404-416 (folder load, file to the listener); SRC GsFileBrowserFragment.java:123-124; ' + FW_VIEW)
# (notebook menu) the menu items of the visible page are dispatched by the activity to the fragment (Activity.java:3450-3453,
# FragmentManager.java:3157), so the menu callback is a GUI edge from the notebook page. The auto creation edges are suppressed.
sup(('GsFileBrowserFragment.<init>', 'GsFileBrowserFragment.onOptionsItemSelected'),
    ('GsFileBrowserFragment.newInstance', 'GsFileBrowserFragment.onOptionsItemSelected'))
gui('S_NOTEBOOK', 'GsFileBrowserFragment.onOptionsItemSelected', 'Tap an item of the notebook toolbar menu (sort, search, import, create shortcut, and the rest)',
    evidence='SRC GsFileBrowserFragment.java:380; FW-SRC core/java/android/app/Activity.java:3450-3453; FW-SRC core/java/android/app/FragmentManager.java:3157; ' + FW_MENU)

# (notebook selection, round 7) a long-press on a row selects it: the adapter's long-press listener (SRC GsFileBrowserListAdapter.java:272)
# calls onLongClick, which toggles the selection (562-567). The two auto creation edges (fragment onViewCreated, adapter constructor)
# reach onLongClick without a tap, so both are suppressed; the long-press is a GUI edge from the notebook page. The selection is a screen
# (S_NOTEBOOK_SEL) that the info action needs.
sup(('GsFileBrowserFragment.onViewCreated', 'GsFileBrowserListAdapter.onLongClick'),
    ('GsFileBrowserListAdapter.<init>', 'GsFileBrowserListAdapter.onLongClick'))
gui('S_NOTEBOOK', 'GsFileBrowserListAdapter.onLongClick', 'Long-press a file or folder in the notebook list (the row becomes selected)',
    evidence='SRC GsFileBrowserListAdapter.java:272 (long-press listener), 562-567 (onLongClick: toggleSelection, then the listener); ' + FW_VIEW)
e('GsFileBrowserListAdapter.onLongClick', 'S_NOTEBOOK_SEL', 'ENTERS',
  'The long-press selected a row: the notebook page now holds a selection',
  guard='view.getId() == R.id.opoc_filesystem_item__root (the row root view is the one that selects, GsFileBrowserListAdapter.java:563)',
  evidence='SRC GsFileBrowserListAdapter.java:562-567')

# (notebook info, round 7) the info item acts only when items are selected (GsFileBrowserFragment.java:457-460). The auto call from the
# menu dispatch to FileInfoDialog.show is suppressed, so the info tap is only reachable from the selection screen: the route selects first.
# The dispatch itself (GsFileBrowserFragment.onOptionsItemSelected, case R.id.action_info_selected_item) is named in the trigger text.
sup(('GsFileBrowserFragment.onOptionsItemSelected', 'FileInfoDialog.show'))
gui('S_NOTEBOOK_SEL', 'FileInfoDialog.show',
    'Tap the info item of the notebook toolbar menu (GsFileBrowserFragment.onOptionsItemSelected dispatches it, case R.id.action_info_selected_item)',
    guard='_filesystemViewerAdapter.areItemsSelected() (the if at GsFileBrowserFragment.java:458 encloses the call at line 460)',
    needs_state=NEED_SELECTED,
    evidence='SRC GsFileBrowserFragment.java:457-460; ' + FW_MENU)

# (round 8) the auto call addRecentFile -> setRecentDocuments (AppSettings.java:396) is written here with its file guard and the
# NEED_OTHER_DOC state. Without the state, the route search picked the todo page's close (DocumentEditAndViewFragment.onPause) as the
# cheapest way to AppSettings.getPopularDocumentsSorted, and that route breaks the guard (the todo file is not a recent-list file).
sup(('AppSettings.addRecentFile', 'AppSettings.setRecentDocuments'))
e('AppSettings.addRecentFile', 'AppSettings.setRecentDocuments', 'CALL',
  'Direct call: a notebook file (not the todo or quick-note file) that is closed or left goes to the recent list (the call is under the file guard)',
  guard='!file.equals(getTodoFile()) && !file.equals(getQuickNoteFile()); listFileInRecents(file)',
  needs_state=NEED_OTHER_DOC,
  evidence='SRC AppSettings.java:396 (the guard, read from the bytecode line of the call; the auto edge is replaced here to carry the state)')

# (search, round 7) the search listener is set in view mode only: setupSearchView returns early unless the preview is visible and the
# web view exists (DocumentEditAndViewFragment.java:697-698). search() returns at once when the web view is null (707-708), before the
# debounced task (lambda$search$0, line 711) that calls findAllAsync. The auto creation edges of the listener are suppressed, and the
# listener edges are written here with the guards and the view-mode state.
sup(('DocumentEditAndViewFragment$2.<init>', 'DocumentEditAndViewFragment$2.onQueryTextChange'),
    ('DocumentEditAndViewFragment.setupSearchView', 'DocumentEditAndViewFragment$2.onQueryTextChange'),
    ('DocumentEditAndViewFragment$2.search', 'DocumentEditAndViewFragment$2.lambda$search$0'))
e('DocumentEditAndViewFragment.setupSearchView', 'DocumentEditAndViewFragment$2.onQueryTextChange', 'FRAMEWORK',
  'The search view calls its query listener when the text changes (the listener is set only in view mode, DocumentEditAndViewFragment.java:697-702)',
  guard='not (!_isPreviewVisible || _webView == null) (early return at DocumentEditAndViewFragment.java:697-698)',
  needs_state=NEED_PREVIEW,
  evidence='SRC DocumentEditAndViewFragment.java:697-702 (setOnQueryTextListener); INFERRED the SearchView calls onQueryTextChange on each text change (the listener type is not read per lambda)')
e('DocumentEditAndViewFragment$2.search', 'DocumentEditAndViewFragment$2.lambda$search$0', 'FRAMEWORK',
  'The debounced task (500 ms) runs the web-view search (findAllAsync)',
  guard='not (_webView == null) (early return at DocumentEditAndViewFragment.java:707-708)',
  evidence='SRC DocumentEditAndViewFragment.java:707-711 (search, and the debounced lambda at 711); INFERRED TextViewUtils.makeDebounced runs the Runnable after its delay')

# More page: MoreFragment shows the child preference fragment MoreInfoFragment (MoreFragment.java:48-54)
e('MainActivity.onViewPagerPageSelected@MORE', 'MoreFragment.onViewCreated', 'FRAMEWORK',
  'The realized more page is created by the pager; the FragmentManager creates its view',
  guard=['_sectionsAdapter != null (the if at MainActivity.java:445 encloses ensureRealized at line 446)',
         'the realized tab is More (the branch at MainActivity.java:519-520)'],
  evidence='SRC MainActivity.java:446, 519-520; SRC MoreFragment.java:46; ' + FW_FRAG)
for pg in ('S_NOTEBOOK', 'S_TODO', 'S_QUICKNOTE'):
    gui(pg, 'MainActivity.onViewPagerPageSelected@MORE', 'Tap the More tab in the bottom bar (the pager realizes the More page)',
        guard=['_sectionsAdapter != null (the if at MainActivity.java:445 encloses ensureRealized at line 446)',
               'the realized tab is More (the branch at MainActivity.java:519-520)'],
        evidence='SRC MainActivity.java:446, 519-520; ' + FW_FRAG)
for m in ('doUpdatePreferences', 'getPreferenceResourceForInflation', 'isDividerVisible'):
    e('MoreFragment.onViewCreated', 'MoreInfoFragment.%s' % m, 'FRAMEWORK',
      'The child preference fragment (MoreInfoFragment) is shown and asks for its preferences (%s)' % m,
      evidence='SRC MoreFragment.java:48-54; INFERRED the preference base class calls %s (GsPreferenceFragmentBase source not read)' % m)
gui('S_MORE', 'MoreInfoFragment.onPreferenceClicked', 'Tap a row of the More list (website, Settings, rate app)',
    evidence='SRC MoreInfoFragment.java:58-67')
e('MoreInfoFragment.onPreferenceClicked', 'SettingsActivity.<init>', 'INTENT',
  'The Settings row starts SettingsActivity with startActivityForResult (request code 124)',
  cls='explicit', guard=['isAdded() && preference.hasKey() (the if at MoreInfoFragment.java:60)',
                         'keyResId == R.string.pref_key__more_info__settings (the case label at MoreInfoFragment.java:66)'],
  evidence='SRC MoreInfoFragment.java:66-67; SRC GsContextUtils.java:1116-1117, 1128-1138; ' + FW_RESULT)

# C2 MainActivity: options menu (one item, hidden), the + button, the new file dialog, Back and key presses, lifecycle, restart, launch
e('MainActivity.onCreate', 'MainActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'AppCompat builds the toolbar menu (its one item is hidden by the settings flag)',
  evidence='SRC MainActivity.java:269-276; ' + FW_MENU)
gui('S_NOTEBOOK', 'MainActivity.onClickFab', 'Tap the plus button (new file)',
    evidence='SRC MainActivity.java:91, 343-362; ' + FW_VIEW)
gui('S_NOTEBOOK', 'MainActivity.onLongClickFab', 'Long-press the plus button (cycles the recent, favourite and folder views)',
    evidence='SRC MainActivity.java:92, 322-341; ' + FW_VIEW)
e('MainActivity.onClickFab', 'NewFileDialog.onCreateDialog', 'FRAMEWORK', 'The fragment manager shows the new file dialog',
  evidence='SRC MainActivity.java:359-360; SRC NewFileDialog.java:94; ' + FW_DIALOG)
e('MainActivity.onClickFab', 'S_NEWFILE', 'ENTERS', 'The new file dialog is shown',
  evidence='SRC MainActivity.java:359-360; ' + FW_DIALOG)
e('NewFileDialog.callback', 'MainActivity.newItemCallback', 'CALL',
  'The dialog callback is the method reference this::newItemCallback: the new file is opened or shown',
  evidence='SRC NewFileDialog.java:382-384; SRC MainActivity.java:359-360, 364-371')
for pg in ('S_NOTEBOOK', 'S_TODO', 'S_QUICKNOTE', 'S_MORE'):
    gui(pg, 'MainActivity.onBackPressed', 'Press Back on a main tab',
        evidence='SRC MainActivity.java:374-380; FW-SRC core/java/android/app/Activity.java:3001-3010')
    gui(pg, 'MainActivity.onKeyDown', 'Press a hardware key on a main tab',
        evidence='SRC MainActivity.java:591-593')
e('MainActivity.onBackPressed', 'S_EXIT', 'ENTERS',
  'No page handles Back, so the activity finishes; the process ends when no activity is left',
  guard='the visible page does not handle Back (GsFragmentBase.onBackPressed returns false)',
  evidence='SRC MainActivity.java:374-380; FW-SRC core/java/android/app/Activity.java:3001-3010')
# cold-start order fix: the framework runs onPostResume right after onResume (Activity.java:7098-7131), so onPause
# follows onPostResume. The old direct onResume -> onPause edge skipped onPostResume on the widget routes.
e('MainActivity.onPostResume', 'MainActivity.onPause', 'LIFECYCLE',
  'The activity leaves the foreground (another activity, or the home screen)',
  evidence='SRC MainActivity.java:569-576; ' + FW_PAUSE)
e('MainActivity.onPause', 'MainActivity.onSaveInstanceState', 'LIFECYCLE',
  'The system saves the activity state when it leaves the foreground',
  evidence='SRC MainActivity.java:154; ' + FW_SAVE)
e('MainActivity.onPause', 'MainActivity.onStop', 'LIFECYCLE', 'The system calls Activity.onStop',
  evidence='SRC MainActivity.java:579-582; ' + FW_PAUSE)
e('MainActivity.onCreate', 'MainActivity.onRestoreInstanceState', 'LIFECYCLE',
  'The activity is recreated from saved state', needs_state=NEED_SAVED_STATE,
  evidence='SRC MainActivity.java:171; ' + FW_ACT)
e('MainActivity.onResume', 'MainActivity.<init>', 'INTENT',
  'The app restarts itself: a setting needs the main screen rebuilt (finish, then startActivity with the same intent)',
  cls='explicit', needs_state=NEED_RECREATE_MAIN, evidence='SRC MainActivity.java:285-293; ' + FW_ACT)
e('MainActivity.launch', 'MainActivity.<init>', 'INTENT',
  'The app starts MainActivity with a file extra (animateToActivity with the intent)',
  cls='explicit', evidence='SRC MainActivity.java:238-245; SRC GsContextUtils.java:1128-1138')
e('MainActivity.launch', 'MainActivity.onNewIntent', 'INTENT',
  'Markor is already open (singleTop): the new intent goes to the running MainActivity',
  cls='explicit', needs_state=NEED_APP_OPEN, evidence='SRC MainActivity.java:238-245; SRC AndroidManifest.xml:65; SRC MainActivity.java:223')

# results returned to MainActivity.onActivityResult (request codes: intro, settings 124, SD card picker 50003)
e('IntroActivity.onSkipPressed', 'MainActivity.onActivityResult', 'RESULT',
  'The intro is skipped and finishes; the result returns to MainActivity (request code REQ_CODE_APPINTRO)',
  evidence='SRC IntroActivity.java:25-28, 59-61; ' + FW_RESULT)
e('IntroActivity.onDonePressed', 'MainActivity.onActivityResult', 'RESULT',
  'The intro is finished with Done; the result returns to MainActivity',
  evidence='SRC IntroActivity.java:70-73; ' + FW_RESULT)
e('SettingsActivity.onStop', 'MainActivity.onActivityResult', 'RESULT',
  'Settings sets its result (changed or not) in onStop; the result returns to MainActivity (request code 124)',
  evidence='SRC SettingsActivity.java:105-108; SRC MoreInfoFragment.java:67; ' + FW_RESULT)
e('GsContextUtils.requestStorageAccessFramework', 'MainActivity.onActivityResult', 'RESULT',
  'The SD card folder picker returns the chosen tree (request code 50003)',
  env=ENV_PICKER, needs_state=NEED_SAF_TREE,
  evidence='SRC MainActivity.java:585-588; SRC GsContextUtils.java:2085-2093; ' + FW_RESULT)
e('GsContextUtils.showMountSdDialog', 'GsContextUtils.requestStorageAccessFramework', 'FRAMEWORK',
  'The Yes button of the mount SD card dialog (a lambda, so no call edge is drawn) opens the folder picker',
  evidence='SRC GsContextUtils.java:2260-2271; INFERRED the dialog button calls its listener (dialog framework source not read)')

# C3 intro (first start only): AppIntro calls the page hooks (library source not read)
e('IntroActivity.optStart', 'IntroActivity.<init>', 'INTENT',
  'First start: MainActivity starts the intro with startActivityForResult',
  cls='explicit', needs_state=NEED_FIRST_START, evidence='SRC IntroActivity.java:25-31,33-35; ' + FW_RESULT)
e('IntroActivity.<init>', 'IntroActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC IntroActivity.java:39; ' + FW_ACT)
# The framework resume step: IntroActivity does not override onResume, so the call is the inherited Activity.onResume.
# The node is added after exec of this file (build_graph FRAMEWORK_NODES); the class is taken from IntroActivity.onCreate in method_list.json.
# Round 7: the widget services declare only <init> and onGetViewFactory, so Service.onCreate and RemoteViewsService.onBind are
# framework nodes (the names are not in method_list.json; the classes are the app's service classes, as the inherited methods are called on them).
FRAMEWORK_NODES = {
    'IntroActivity.onResume': {'class': 'net/gsantner/markor/activity/IntroActivity', 'short': 'IntroActivity.onResume',
                               'name': 'onResume', 'desc': '()V', 'flags': []},
    'WrFilesWidgetService.onCreate': {'class': 'other/writeily/widget/WrFilesWidgetService', 'short': 'WrFilesWidgetService.onCreate',
                                      'name': 'onCreate', 'desc': '()V', 'flags': []},
    'WrFilesWidgetService.onBind': {'class': 'other/writeily/widget/WrFilesWidgetService', 'short': 'WrFilesWidgetService.onBind',
                                    'name': 'onBind', 'desc': '(Landroid/content/Intent;)Landroid/os/IBinder;', 'flags': []},
    'TodoWidgetService.onCreate': {'class': 'net/gsantner/markor/widget/TodoWidgetService', 'short': 'TodoWidgetService.onCreate',
                                   'name': 'onCreate', 'desc': '()V', 'flags': []},
    'TodoWidgetService.onBind': {'class': 'net/gsantner/markor/widget/TodoWidgetService', 'short': 'TodoWidgetService.onBind',
                                 'name': 'onBind', 'desc': '(Landroid/content/Intent;)Landroid/os/IBinder;', 'flags': []},
}
e('IntroActivity.onCreate', 'IntroActivity.onResume', 'LIFECYCLE',
  'The framework calls Activity.onCreate (the five intro slides are added in onCreate, IntroActivity.java:39-49), then Activity.performResume calls onResume. IntroActivity does not override onResume: the call is the framework\'s (inherited Activity.onResume)',
  evidence='FW-SRC core/java/android/app/Activity.java:7098-7131 (performResume calls onResume at 7107); FW-SRC core/java/android/app/Activity.java:6989-6999 (performCreate calls onCreate); FW-SRC core/java/android/app/ActivityThread.java:2729 (callActivityOnCreate), 2950 (performResume); SRC IntroActivity.java:39-49')
e('IntroActivity.onResume', 'S_INTRO', 'ENTERS',
  'The intro is shown on the first resumed step of the intro activity: the framework calls the inherited onResume (IntroActivity does not override it), and the five slides already added in onCreate are visible',
  evidence='SRC IntroActivity.java:39-49; FW-SRC core/java/android/app/Activity.java:7098-7131')
gui('S_INTRO', 'IntroActivity.onSkipPressed', 'Tap Skip', evidence='SRC IntroActivity.java:59-61; ' + FW_APPINTRO)
gui('S_INTRO', 'IntroActivity.onNextPressed', 'Tap Next', evidence='SRC IntroActivity.java:65-66; ' + FW_APPINTRO)
gui('S_INTRO', 'IntroActivity.onDonePressed', 'Tap Done on the last slide', evidence='SRC IntroActivity.java:70-73; ' + FW_APPINTRO)
gui('S_INTRO', 'IntroActivity.onSlideChanged', 'Swipe to another slide', evidence='SRC IntroActivity.java:77-78; ' + FW_APPINTRO)

# C4 settings: opened from the More tab (the toolbar item is hidden: AppSettings.isShowSettingsOptionInMainToolbar is false)
e('SettingsActivity.<init>', 'SettingsActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC SettingsActivity.java:65-81; ' + FW_ACT)
# the settings list is set in onCreate and shown at the resumed step: SettingsActivity has no onResume of its own, so the inherited
# GsActivityBase.onResume runs after onCreate (the variant @SETTINGS keeps this resume apart from the other activities)
e('SettingsActivity.onCreate', 'GsActivityBase.onResume@SETTINGS', 'LIFECYCLE',
  'The system calls Activity.onResume after onCreate (SettingsActivity has no own onResume; the inherited GsActivityBase.onResume runs)',
  evidence='SRC SettingsActivity.java:50 (extends MarkorBaseActivity), 65-81; ' + FW_ACT + '; SRC GsActivityBase.java:86-99')
e('GsActivityBase.onResume@SETTINGS', 'S_SETTINGS', 'ENTERS', 'The settings list is shown (SettingsFragmentMaster)',
  evidence='SRC SettingsActivity.java:80, 83-102; SRC GsActivityBase.java:86-99; FW-SRC core/java/android/app/Activity.java:7098-7131')
gui('S_SETTINGS', 'SettingsActivity.lambda$onCreate$0', 'Tap the back arrow in the toolbar', evidence='SRC SettingsActivity.java:79')
gui('S_SETTINGS', 'SettingsActivity.onBackPressed', 'Press Back', evidence='SRC SettingsActivity.java:133-141; ' + FW_ACT)
e('SettingsActivity.onBackPressed', 'SettingsActivity.onStop', 'FRAMEWORK',
  'With no sub-screen to go back to, the activity finishes and the system calls onStop',
  evidence='SRC SettingsActivity.java:133-141; FW-SRC core/java/android/app/Activity.java:5526 (finish), 1858 (onStop)')
gui('S_SETTINGS', 'SettingsActivity$MarkorSettingsFragment.onPreferenceChanged', 'Change a setting',
    evidence='SRC SettingsActivity.java:117-119; INFERRED GsPreferenceFragmentBase calls onPreferenceChanged after a change (base source not read)')
gui('S_SETTINGS', 'SettingsActivity$MarkorSettingsFragment.onPreferenceScreenChanged', 'Open a sub-screen of the settings',
    evidence='SRC SettingsActivity.java:122-130; INFERRED GsPreferenceFragmentBase calls onPreferenceScreenChanged (base source not read)')
gui('S_SETTINGS', 'SettingsActivity$SettingsFragmentMaster.onPreferenceClicked', 'Tap a row of the settings list',
    evidence='SRC SettingsActivity.java:250')
e('SettingsActivity$SettingsFragmentMaster.onPreferenceClicked', 'ActionButtonSettingsActivity.<init>', 'INTENT',
  'The action button row starts ActionButtonSettingsActivity', cls='explicit',
  evidence='SRC SettingsActivity.java:371')
e('ActionButtonSettingsActivity.<init>', 'ActionButtonSettingsActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC ActionButtonSettingsActivity.java:56; ' + FW_ACT)
# same as the settings screen: no own onResume (the methods are onCreate, onPause and the menu), so the inherited GsActivityBase.onResume
# is the resumed step (variant @ACTIONBTN)
e('ActionButtonSettingsActivity.onCreate', 'GsActivityBase.onResume@ACTIONBTN', 'LIFECYCLE',
  'The system calls Activity.onResume after onCreate (ActionButtonSettingsActivity has no own onResume; the inherited GsActivityBase.onResume runs)',
  evidence='SRC ActionButtonSettingsActivity.java:45 (extends MarkorBaseActivity), 56; ' + FW_ACT + '; SRC GsActivityBase.java:86-99')
e('GsActivityBase.onResume@ACTIONBTN', 'S_ACTION_BUTTONS', 'ENTERS', 'The action order list is shown',
  evidence='SRC ActionButtonSettingsActivity.java:56; SRC GsActivityBase.java:86-99; FW-SRC core/java/android/app/Activity.java:7098-7131')
# same menu order: the activity menu is built after the (inherited) onResume step (Activity.onCreatePanelMenu, Activity.java:3386-3389)
e('GsActivityBase.onResume@ACTIONBTN', 'ActionButtonSettingsActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'The toolbar menu is built after the activity is resumed (modelled order, see readme_notes.md Limits)',
  evidence='SRC ActionButtonSettingsActivity.java:82; FW-SRC core/java/android/app/Activity.java:3386-3389; ' + FW_MENU)
gui('S_ACTION_BUTTONS', 'ActionButtonSettingsActivity.onOptionsItemSelected', 'Tap the back arrow in the toolbar',
    evidence='SRC ActionButtonSettingsActivity.java:91-94')
e('ActionButtonSettingsActivity.onOptionsItemSelected', 'ActionButtonSettingsActivity.onPause', 'FRAMEWORK',
  'finish() ends the screen; the system calls onPause, which saves the new order',
  evidence='SRC ActionButtonSettingsActivity.java:93-94, 112-114; FW-SRC core/java/android/app/Activity.java:1673 (onPause), 5526 (finish)')
gui('S_ACTION_BUTTONS', 'ActionButtonSettingsActivity.onPause', 'Press Back (the screen closes and the new order is saved)',
    evidence='SRC ActionButtonSettingsActivity.java:112-114; ' + FW_PAUSE)

# C5 editor (DocumentActivity): fragment lifecycle, share-into screen, back and keys, Back target, re-open of a running editor
# (fix 2) the editor is committed by handleLaunchingIntent (showFragment, DocumentActivity.java:229; called from onCreate at 149 or from
# onNewIntent at 155) and is shown when the activity resumes. The commit and the resume are an ordered pair of edges, so a route
# reaches the editor only through the commit step (a shortcut from onCreate to the editor would skip the commit).
# onNewIntent is followed by resume (AOSP: deliverNewIntents, then performResume or performResumeActivity).
e('DocumentActivity.onNewIntent', 'DocumentActivity.onResume', 'LIFECYCLE',
  'Android delivers the new intent (onNewIntent) and then resumes the activity (onResume)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2949 (deliverNewIntents calls onNewIntent), 2950-2951 (performResume when resumed), '
           '2955-2958 (performResumeActivity when paused); SRC DocumentActivity.java:153-155')
EDIT_GUARDS = ['not (intent == null) (early return at DocumentActivity.java:159)',
               'not (intentIsSend) (early return at DocumentActivity.java:172-174)',
               'not (Intent.ACTION_PROCESS_TEXT.equals(intentAction) && intent.hasExtra(Intent.EXTRA_PROCESS_TEXT)) (early return at DocumentActivity.java:175-178)',
               'not (file == null || !_cu.canWriteFile(this, file, false, true)) (the else of the if at DocumentActivity.java:183)',
               'not (frag != null) (no visible fragment: the else of the if at DocumentActivity.java:211)']
e('DocumentActivity.handleLaunchingIntent', 'DocumentActivity.onResume@EDIT', 'LIFECYCLE',
  'The editor of the file is committed (no visible fragment); the activity then resumes and shows it',
  guard=EDIT_GUARDS,
  evidence='SRC DocumentActivity.java:229 (showFragment), 149 and 155 (callers); FW-SRC core/java/android/app/Activity.java:7098-7131; ' + FW_FRAG)
e('DocumentActivity.handleLaunchingIntent@SEND', 'DocumentActivity.onResume@EDIT', 'LIFECYCLE',
  'The editor of the file sent by another app is committed (no visible fragment); the activity then resumes and shows it',
  env=ENV_OTHER_APP, guard=EDIT_GUARDS,
  evidence='SRC DocumentActivity.java:229 (showFragment), 149 (onCreate@SEND caller); FW-SRC core/java/android/app/Activity.java:7098-7131; ' + FW_FRAG)
e('DocumentActivity.onResume@EDIT', 'S_DOCUMENT', 'ENTERS',
  'The editor or viewer of the file is shown once the activity resumes',
  evidence='SRC DocumentActivity.java:229, 310-313; FW-SRC core/java/android/app/Activity.java:7128-7129; ' + FW_FRAG)
e('DocumentActivity.showFragment', 'DocumentEditAndViewFragment.onCreate', 'FRAMEWORK',
  'The FragmentManager runs the editor fragment lifecycle (create, view, resume)',
  evidence='SRC DocumentActivity.java:342; ' + FW_FRAG)
e('DocumentActivity.showFragment', 'DocumentEditAndViewFragment.onViewCreated', 'FRAMEWORK',
  'The FragmentManager creates the editor view', evidence='SRC DocumentActivity.java:342; ' + FW_FRAG)
e('DocumentActivity.showFragment', 'DocumentEditAndViewFragment.onResume', 'FRAMEWORK',
  'The FragmentManager resumes the editor', evidence='SRC DocumentActivity.java:342; ' + FW_FRAG)
# (S4 fix, sample route 3) handleLaunchingIntent reaches showShareInto only for an intent with ACTION_SEND, ACTION_SEND_MULTIPLE or
# ACTION_PROCESS_TEXT (DocumentActivity.java:168-178). The app's own file launch (DocumentActivity.launch) builds an intent with no
# action, so the AUTO call (line 177) is dropped and replaced by the gated edge: the send comes from another app (ENV_OTHER_APP).
sup(('DocumentActivity.handleLaunchingIntent', 'DocumentActivity.showShareInto'))
e('DocumentActivity.handleLaunchingIntent@SEND', 'DocumentActivity.showShareInto', 'CALL',
  'The intent action is ACTION_SEND, ACTION_SEND_MULTIPLE or PROCESS_TEXT: another app sent the text or file (the app\'s own file launch has no action)',
  env=ENV_OTHER_APP, evidence='SRC DocumentActivity.java:168-178 (action branch), 177 (bytecode)')
# (fix 2) the share-into fragment is committed by showShareInto (showFragment, DocumentActivity.java:306; called from
# handleLaunchingIntent@SEND in onCreate, 172-178) and shown when the activity resumes: an ordered pair of edges, as for the editor.
e('DocumentActivity.showShareInto', 'DocumentActivity.onResume@SHARE', 'LIFECYCLE',
  'The share-into fragment is committed by showShareInto; the activity then resumes and shows it',
  evidence='SRC DocumentActivity.java:304-307 (showShareInto, showFragment at 306), 310-313 (onResume); FW-SRC core/java/android/app/Activity.java:7128-7129; ' + FW_FRAG)
e('DocumentActivity.onResume@SHARE', 'S_SHARE_INTO', 'ENTERS',
  'The share-into screen is shown once the activity resumes (text or file shared into Markor)',
  evidence='SRC DocumentActivity.java:304-307, 310-313; FW-SRC core/java/android/app/Activity.java:7098-7131; ' + FW_FRAG)
e('DocumentActivity.showShareInto', 'DocumentShareIntoFragment.onViewCreated', 'FRAMEWORK',
  'The FragmentManager creates the share-into view',
  evidence='SRC DocumentActivity.java:304-307; SRC DocumentShareIntoFragment.java:90; ' + FW_FRAG)
e('DocumentActivity.launch(Activity,File,Boolean,Integer,boolean)', 'DocumentActivity.onNewIntent', 'INTENT',
  'Markor shows another file in the running editor (launch sets the SINGLE_TOP flag)',
  cls='explicit', needs_state=NEED_DOC_OPEN, evidence='SRC DocumentActivity.java:100-102, 153-156; ' + FW_ACT)
gui('S_DOCUMENT', 'DocumentActivity.onBackPressed', 'Press Back in the editor or viewer',
    evidence='SRC DocumentActivity.java:317-336; ' + FW_ACT)
gui('S_DOCUMENT', 'DocumentActivity.onKeyDown', 'Press a hardware key in the editor or viewer',
    evidence='SRC DocumentActivity.java:338-340')
gui('S_DOCUMENT', 'DocumentActivity.dispatchTouchEvent', 'Touch the screen', evidence='SRC DocumentActivity.java:258; ' + FW_VIEW)
e('DocumentActivity.onBackPressed', 'S_EXIT', 'ENTERS',
  'Back closes the editor (the activity finishes or the task is removed) and no activity is left',
  guard='the editor was opened by another app (no Markor screen under it)',
  evidence='SRC DocumentActivity.java:317-336; ' + FW_ACT)
e('DocumentActivity.onBackPressed', 'S_NOTEBOOK', 'ENTERS',
  'Back closes the editor and the main Markor screen (notebook tab) is shown again',
  guard='the editor was opened from Markor (MainActivity under it)',
  evidence='SRC DocumentActivity.java:317-336; SRC MainActivity.java:364-367 (launch with finish false keeps MainActivity under the editor); ' + FW_ACT)
e('GsContextUtils.viewFileInOtherApp', 'S_EXT_APP', 'ENTERS',
  'Markor sends the file to another app (no result returns)',
  evidence='SRC GsContextUtils.java:1337')
gui('S_DOCUMENT', 'DocumentEditAndViewFragment.onOptionsItemSelected', 'Tap an item of the editor menu (for example the file browser or the other app)',
    evidence='SRC DocumentEditAndViewFragment.java:421; ' + FW_MENU)
# share as HTML (route of wikitextPagePathToRelativeFilePath): the menu code picks the converter by format (line 485) and its
# CALLs (line 487) reach every format's convertMarkup. The base method keeps none of them. Each conversion is a page edge from the
# editor (S_DOCUMENT, any document) that names its format, so the todo page cannot reach a wikitext conversion.
for _fmt, _conv in (('WIKITEXT', 'WikitextTextConverter'), ('MARKDOWN', 'MarkdownTextConverter'), ('TODOTXT', 'TodoTxtTextConverter'),
                    ('PLAINTEXT', 'PlaintextTextConverter'), ('ORGMODE', 'OrgmodeTextConverter'), ('ASCIIDOC', 'AsciidocTextConverter'),
                    ('CSV', 'CsvTextConverter'), ('EMBED', 'EmbedBinaryTextConverter')):
    sup(('DocumentEditAndViewFragment.onOptionsItemSelected', _conv + '.convertMarkup'))
    gui('S_DOCUMENT', _conv + '.convertMarkup', 'Tap Share as HTML in the editor menu (the document uses this format)',
        needs_state=NEED_FMT[_fmt], evidence='SRC DocumentEditAndViewFragment.java:482-487 (bytecode); SRC DocumentEditAndViewFragment.java:485 (converter by format)')
# key press (route of TextViewUtils): MarkorBaseActivity.onReceiveKeyPress passes the key to whichever fragment it is given, so the
# notebook page reached the editor. The base edge to the editor is removed; the todo and quick note pages and a document reach
# the editor directly. The editor hands the key to its format's actions (line 342): only the wikitext actions reach TextViewUtils.
sup(('MarkorBaseActivity.onReceiveKeyPress', 'DocumentEditAndViewFragment.onReceiveKeyPress'),
    ('DocumentEditAndViewFragment.onReceiveKeyPress', 'WikitextActionButtons.onReceiveKeyPress'),
    ('DocumentEditAndViewFragment.onReceiveKeyPress', 'ActionButtonBase.onReceiveKeyPress'))
for pg in ('S_TODO', 'S_QUICKNOTE'):
    gui(pg, 'DocumentEditAndViewFragment.onReceiveKeyPress', 'Press a hardware key on the page (the editor takes the key first)',
        evidence='SRC MarkorBaseActivity.java:35-36; SRC DocumentEditAndViewFragment.java:341-342')
gui('S_DOCUMENT', 'DocumentEditAndViewFragment.onReceiveKeyPress@DOC', 'Press a hardware key in the editor of a document (the editor takes the key first)',
    evidence='SRC DocumentActivity.java:338-340; SRC MarkorBaseActivity.java:35-36')
e('DocumentEditAndViewFragment.onReceiveKeyPress@DOC', 'WikitextActionButtons.onReceiveKeyPress', 'CALL',
  'The wikitext actions take the key of a wikitext document (line 342)',
  needs_state=NEED_FMT['WIKITEXT'], evidence='SRC DocumentEditAndViewFragment.java:341-342 (bytecode)')
# the base key handler (the Tab key indents the lines when the setting is on): every format's actions except wikitext inherit it
# (TodoTxt, Markdown, Orgmode, Asciidoc, Plaintext, CSV). Wikitext reaches it through super (WikitextActionButtons.java:287).
for _src in ('DocumentEditAndViewFragment.onReceiveKeyPress', 'DocumentEditAndViewFragment.onReceiveKeyPress@DOC'):
    e(_src, 'ActionButtonBase.onReceiveKeyPress', 'CALL',
      'The editor gives the key to its format actions; the base handler indents the lines on Tab when the setting is on',
      needs_state=NEED_TAB_INDENT, evidence='SRC DocumentEditAndViewFragment.java:341-342 (bytecode); SRC ActionButtonBase.java:1037-1038')
e('DocumentEditAndViewFragment.onOptionsItemSelected', 'DocumentEditAndViewFragment.lambda$onOptionsItemSelected$9', 'FRAMEWORK',
  'View.postDelayed runs the Runnable that starts MainActivity with this file (MainActivity.launch) after the menu closes; '
  'the notebook tab opens because the start tab is skipped when a file is in the intent (MainActivity.java:143)',
  evidence='SRC DocumentEditAndViewFragment.java:630; SRC MainActivity.java:143; ' + FW_POST)
# preview or view mode (sample route 9): TextConverterBase.convertMarkupShowInWebView runs with the page's converter as receiver
# (updateViewModeText takes it from FormatRegistry.getConverter, DocumentEditAndViewFragment.java:995). Its lifts to every converter
# are skipped (_LIFT_SKIP); each converter is reached from the base body with its format state.
_CONV = (('WIKITEXT', 'WikitextTextConverter'), ('MARKDOWN', 'MarkdownTextConverter'), ('TODOTXT', 'TodoTxtTextConverter'),
         ('PLAINTEXT', 'PlaintextTextConverter'), ('ORGMODE', 'OrgmodeTextConverter'), ('ASCIIDOC', 'AsciidocTextConverter'),
         ('CSV', 'CsvTextConverter'), ('EMBED', 'EmbedBinaryTextConverter'))
for _fmt, _conv in _CONV:
    e('TextConverterBase.convertMarkupShowInWebView', _conv + '.convertMarkup', 'CALL',
      'The view mode converts the document with the converter of its format (the base body runs with that converter)',
      needs_state=NEED_FMT[_fmt],
      guard=['not (_webView == null) (early return at DocumentEditAndViewFragment.java:988-990, updateViewModeText)'],
      evidence='SRC TextConverterBase.java:110 (bytecode); SRC DocumentEditAndViewFragment.java:995')

# toolbar action buttons of the editor (sample route 9): the button's listener (ActionButtonBase.java:343-354 onActionClick, 366
# onActionLongClick) runs the action class of the page's own format, which is built by the format list (ActionButtonBase.java:305).
# The editor and the quick note take the format state; the todo page always holds the todo.txt format. The lift of the listener
# to every format's class is skipped (_LIFT_SKIP).
_ACT_CLICK = (('ASCIIDOC', 'AsciidocActionButtons'), ('MARKDOWN', 'MarkdownActionButtons'), ('ORGMODE', 'OrgmodeActionButtons'),
              ('WIKITEXT', 'WikitextActionButtons'), ('TODOTXT', 'TodoTxtActionButtons'))
_ACT_LONG = (('MARKDOWN', 'MarkdownActionButtons'), ('WIKITEXT', 'WikitextActionButtons'), ('TODOTXT', 'TodoTxtActionButtons'))
# the button exists only when its action is in the bar being built: the if at ActionButtonBase.java:305 gates the append of each action.
_ABM = ('the action is in this bar: !disabledKeys.contains(key) && (action.displayMode == displayMode || '
        'action.displayMode == ActionItem.DisplayMode.ANY) (ActionButtonBase.java:305, the if around appendActionButtonToBar)')
for _fmt, _cls in _ACT_CLICK:
    for pg in ('S_DOCUMENT', 'S_QUICKNOTE'):
        gui(pg, _cls + '.onActionClick', 'Tap an action button in the toolbar of the editor (the document uses this format)',
            needs_state=NEED_FMT[_fmt], guard=[_ABM], evidence='SRC ActionButtonBase.java:343-354 (bytecode); SRC ActionButtonBase.java:305')
for _fmt, _cls in _ACT_LONG:
    for pg in ('S_DOCUMENT', 'S_QUICKNOTE'):
        gui(pg, _cls + '.onActionLongClick', 'Long-press an action button in the toolbar of the editor (the document uses this format)',
            needs_state=NEED_FMT[_fmt], guard=[_ABM], evidence='SRC ActionButtonBase.java:366 (bytecode); SRC ActionButtonBase.java:305')
gui('S_TODO', 'TodoTxtActionButtons.onActionClick', 'Tap an action button in the toolbar of the todo page (the todo.txt format)',
    guard=[_ABM], evidence='SRC ActionButtonBase.java:343-354 (bytecode); SRC ActionButtonBase.java:305')
gui('S_TODO', 'TodoTxtActionButtons.onActionLongClick', 'Long-press an action button in the toolbar of the todo page (the todo.txt format)',
    guard=[_ABM], evidence='SRC ActionButtonBase.java:366 (bytecode); SRC ActionButtonBase.java:305')

# the import options of the share-into page: the row click is the page's own action (its receiver is the import options fragment).
# This replaces the base-method lift that the E2 fix removed for this override.
gui('S_SHARE_INTO', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.onPreferenceClicked',
    'Tap a row of the import options of the shared file (target file, folder, file name)',
    evidence='SRC DocumentShareIntoFragment.java:516; SRC DocumentShareIntoFragment.java:94-101 (the import options fragment is shown in the page)')
# the attach dialog's camera or gallery picture (fetchAndInsertItem, AttachLinkOrFileDialog.java:355-375, 414-420): the picture comes
# back from the external camera or gallery app, so the result callback runs only after that app returns a result.
e('AttachLinkOrFileDialog.fetchAndInsertItem', 'AttachLinkOrFileDialog.lambda$fetchAndInsertItem$9', 'FRAMEWORK',
  'The camera or gallery app returns the picture, and the callback inserts it (the link is written to the document)',
  env=ENV_PICKER, evidence='SRC AttachLinkOrFileDialog.java:414-420 (cu.requestCameraPicture / requestGalleryPicture pass the callback); SRC AttachLinkOrFileDialog.java:355-375')
# the folder browser of the share import (selectOrCreateDestination, line 450): its OK calls the listener onFsViewerSelected (line 466).
# The notebook browser's click (GsFileBrowserListAdapter.onClick, line 440) also reached that listener through a CALL with no
# picker check, so that CALL is removed and the picker is its own page.
sup(('GsFileBrowserListAdapter.onClick', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerSelected'),
    # the same listener is also reached through the dialog's own OK (GsFileBrowserDialog.java:271, a CALL to all picker listeners)
    ('GsFileBrowserDialog.onFsViewerSelected', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerSelected'),
    # the notebook browser's fragment passes the click to its own listener field (GsFileBrowserFragment.java:202), which is a CALL to
    # every picker listener; the notebook browser never opens the share import, so this CALL is removed (sample route 7)
    ('GsFileBrowserFragment.onFsViewerSelected', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerSelected'))
e('DocumentShareIntoFragment$ShareIntoImportOptionsFragment.selectOrCreateDestination', 'S_SHARE_PICKER', 'ENTERS',
  'The share import opens the folder browser (the destination folder is chosen there)',
  evidence='SRC DocumentShareIntoFragment.java:450-456')
gui('S_SHARE_PICKER', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerSelected',
    'Tap OK in the folder browser of the share import (the chosen folder receives the shared file)',
    evidence='SRC DocumentShareIntoFragment.java:466-476; SRC GsFileBrowserListAdapter.java:436-440',
    guard=['case R.id.ui__filesystem_dialog__button_ok (the OK button is pressed; GsFileBrowserListAdapter.java:436)',
           'not (_dopt.doSelectMultiple && areItemsSelected()) (single-select path; GsFileBrowserListAdapter.java:437-440)'])
# the share picker's neutral button (attach or copy here) is the picker's own listener (DocumentShareIntoFragment.java:487-489). The
# dialog and fragment dispatchers call every picker listener, so the notebook's folder dialog (move or copy) would reach this listener
# on its neutral button; those two CALL edges are removed, and the neutral button is a GUI edge from the share picker only.
sup(('GsFileBrowserDialog.onFsViewerNeutralButtonPressed', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerNeutralButtonPressed'),
    ('GsFileBrowserFragment.onFsViewerNeutralButtonPressed', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerNeutralButtonPressed'))
gui('S_SHARE_PICKER', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerNeutralButtonPressed',
    'Tap the neutral button of the share folder browser (attach or copy the shared file into the folder shown)',
    evidence='SRC DocumentShareIntoFragment.java:487-489; SRC GsFileBrowserDialog.java:236, 198 (neutral button; _callback is the dialog listener)')

# the attach dialog's browse button (lambda$showInsertImageOrLinkDialog$3, AttachLinkOrFileDialog.java:155) starts fetchAndInsertItem
# with a browse action. Its browse case (lines 446-456) makes the file-browser listener (AttachLinkOrFileDialog$1) that passes the
# picked file to setFields (lambda$fetchAndInsertItem$10, line 380). The registration of lambda$10 is skipped (_REG_SKIP), so this
# is the only route to it. The browse listener is reached from the browse button only, not from the notebook browser or the dialog
# (the same fan-outs are removed here as for the share picker).
sup(('GsFileBrowserListAdapter.onClick', 'AttachLinkOrFileDialog$1.onFsViewerSelected'),
    ('GsFileBrowserFragment.onFsViewerSelected', 'AttachLinkOrFileDialog$1.onFsViewerSelected'),
    ('GsFileBrowserDialog.onFsViewerSelected', 'AttachLinkOrFileDialog$1.onFsViewerSelected'))
e('AttachLinkOrFileDialog.lambda$showInsertImageOrLinkDialog$3', 'AttachLinkOrFileDialog$1.onFsViewerSelected', 'FRAMEWORK',
  'Tap Browse in the attach dialog: a file browser opens, and the file tapped there is passed to the attach dialog',
  evidence='SRC AttachLinkOrFileDialog.java:155 (browse button starts the browse action); SRC AttachLinkOrFileDialog.java:446-456 (browse case registers the listener, 450-456)',
  guard=['the attach dialog action is LINK_BROWSE, IMAGE_BROWSE or AUDIO_BROWSE (case labels AttachLinkOrFileDialog.java:446-448)',
         'activity instanceof AppCompatActivity && nameEdit != null && pathEdit != null (AttachLinkOrFileDialog.java:449)'])
e('AttachLinkOrFileDialog$1.onFsViewerSelected', 'AttachLinkOrFileDialog.lambda$fetchAndInsertItem$10', 'CALL',
  'The picked file is put into the name and path fields of the attach dialog (setFields)',
  evidence='SRC AttachLinkOrFileDialog.java:455 (setFields.callback(file)); SRC AttachLinkOrFileDialog.java:380 (bytecode, lambda$10)')

# the wikitext branch of the attach dialog's setFields (lambda$fetchAndInsertItem$10, AttachLinkOrFileDialog.java:380-398) and of
# setupFileAttachment (lines 278-281) turns the picked or shared file into a notebook-relative link path with resolveSystemFilePath,
# which reaches findNotebookRootDir. Both calls only happen when the open document is wikitext, so the edges need the wikitext state.
sup(('AttachLinkOrFileDialog.lambda$fetchAndInsertItem$10', 'WikitextLinkResolver.resolveSystemFilePath'),
    ('AttachLinkOrFileDialog.setupFileAttachment', 'WikitextLinkResolver.resolveSystemFilePath'))
e('AttachLinkOrFileDialog.lambda$fetchAndInsertItem$10', 'WikitextLinkResolver.resolveSystemFilePath', 'CALL',
  'In a wikitext document, the browsed file becomes a notebook-relative link path (the path field is filled in)',
  needs_state=NEED_FMT['WIKITEXT'],
  guard=['the wikitext branch of setFields is taken: textFormatId == FormatRegistry.FORMAT_WIKITEXT (AttachLinkOrFileDialog.java:381)'],
  evidence='SRC AttachLinkOrFileDialog.java:380-398 (setFields: wikitext branch calls resolveSystemFilePath at line 397)')
e('AttachLinkOrFileDialog.setupFileAttachment', 'WikitextLinkResolver.resolveSystemFilePath', 'CALL',
  'In a wikitext document, the shared file becomes a notebook-relative link path',
  needs_state=NEED_FMT['WIKITEXT'],
  evidence='SRC AttachLinkOrFileDialog.java:276-281 (setupFileAttachment: wikitext branch calls resolveSystemFilePath)')

# the clearFixup route (sample route 8). The fixup that clearFixup clears is recorded by the text watcher on every edit
# (HighlightingEditor.java:94-101, _hl.fixup), and the debounced re-highlight applies it (applyDynamic -> applyFixup -> clearFixup).
# Two ways to reach the clear: applyFixup clears a pending shift (the NEED_FIX state on the applyFixup edge, below), and setComputed
# clears unconditionally on every full recompute (SyntaxHighlighterBase.java:418-425; recompute() calls it). So a format change from
# the editor menu reaches clearFixup with no state: applyTextFormat -> setHighlighter -> recomputeHighlighting -> recompute -> setComputed.
gui('S_TODO', 'HighlightingEditor$1.onTextChanged',
    'Type or delete text in the todo document (the highlighter records the change as a pending shift of its spans; a second edit away from the first one, before the debounce, applies it)',
    # the typing is on a todo document: the todo.txt state, so no other format's highlighter can follow this edit (a todo page is not a key-value file)
    needs_state=NEED_FMT['TODOTXT'],
    evidence='SRC HighlightingEditor.java:94-103 (TextWatcher.onTextChanged calls _hl.fixup); SRC SyntaxHighlighterBase.java:296-306 (fixup applies a pending shift when a later edit does not overlap it)')
# the highlighter of a document is its format's class, so the base compute (SyntaxHighlighterBase.java:443, a virtual generateSpans call)
# may reach a format's generateSpans only with that format's state. The typing edge below is from any document page; the format is the
# state on the spans edge (sample route 6: tab spans are drawn by the key-value format only for a key-value document).
_HL_FMT = (('KEYVALUE', 'KeyValueSyntaxHighlighter'), ('MARKDOWN', 'MarkdownSyntaxHighlighter'), ('ORGMODE', 'OrgmodeSyntaxHighlighter'),
           ('ASCIIDOC', 'AsciidocSyntaxHighlighter'), ('WIKITEXT', 'WikitextSyntaxHighlighter'), ('PLAINTEXT', 'PlaintextSyntaxHighlighter'),
           ('CSV', 'CsvSyntaxHighlighter'), ('TODOTXT', 'TodoTxtSyntaxHighlighter'))
# compute returns before generateSpans when the spannable is empty (SyntaxHighlighterBase.java:437-439); the key-value format's
# case label is FormatRegistry.java:167 (the highlighter is built at line 169)
_SPANS_EMPTY = 'not (TextUtils.isEmpty(_spannable)) (early return at SyntaxHighlighterBase.java:437-439, compute)'


def _spans_guard(_fmt):
    return [_SPANS_EMPTY] + (['case FORMAT_KEYVALUE (the key-value highlighter is built in this case, FormatRegistry.java:167-169)']
                             if _fmt == 'KEYVALUE' else [])


for _fmt, _hl in _HL_FMT:
    sup(('SyntaxHighlighterBase.compute', _hl + '.generateSpans'),
        ('SyntaxHighlighterBase.compute@' + _hl, _hl + '.generateSpans'))
    e('SyntaxHighlighterBase.compute', _hl + '.generateSpans', 'CALL',
      'The open document is highlighted with its own format (the base computes the spans, the format class makes them)',
      needs_state=NEED_FMT[_fmt], guard=_spans_guard(_fmt),
      evidence='SRC SyntaxHighlighterBase.java:443 (compute calls generateSpans virtually); SRC FormatRegistry.java:169 (the key-value format uses KeyValueSyntaxHighlighter)')
    # the receiver variant compute@X (the same compute run with an X object as receiver) makes the same call on its own receiver:
    # that call is gated by the same format state, so the variant cannot skip the format check
    e('SyntaxHighlighterBase.compute@' + _hl, _hl + '.generateSpans', 'CALL',
      'The open document is highlighted with its own format (the receiver variant runs the format class as its own receiver)',
      needs_state=NEED_FMT[_fmt], guard=_spans_guard(_fmt),
      evidence='SRC SyntaxHighlighterBase.java:443 (bytecode: the receiver variant calls generateSpans on its own receiver)')
# TodoTxtBasicSyntaxHighlighter is not created by FormatRegistry (only TodoTxtSyntaxHighlighter is, FormatRegistry.java:162). Its
# generateSpans runs only as the super call of TodoTxtSyntaxHighlighter.generateSpans, so the impossible receiver variant is suppressed.
sup(('SyntaxHighlighterBase.compute', 'TodoTxtBasicSyntaxHighlighter.generateSpans'),
    ('SyntaxHighlighterBase.compute@TodoTxtBasicSyntaxHighlighter', 'TodoTxtBasicSyntaxHighlighter.generateSpans'))
# CsvSyntaxHighlighter extends MarkdownSyntaxHighlighter (CsvSyntaxHighlighter.java:24) and calls super.generateSpans() (line 49),
# so a CSV document gets the markdown spans, including the tab spans, only through its own CSV state.
sup(('CsvSyntaxHighlighter.generateSpans', 'MarkdownSyntaxHighlighter.generateSpans'))
e('CsvSyntaxHighlighter.generateSpans', 'MarkdownSyntaxHighlighter.generateSpans', 'CALL',
  'A CSV document: its spans include the markdown spans (the CSV format builds on them)',
  needs_state=NEED_FMT['CSV'],
  evidence='SRC CsvSyntaxHighlighter.java:24 (extends MarkdownSyntaxHighlighter); SRC CsvSyntaxHighlighter.java:49 (super.generateSpans())')
gui('S_DOCUMENT', 'HighlightingEditor$1.onTextChanged',
    'Type or delete text in a document (the highlighter re-highlights the open document in its own format)',
    evidence='SRC HighlightingEditor.java:94-103 (TextWatcher.onTextChanged calls _hl.fixup)')
# (clearFixup gate) fixup() records a shift only when none is pending (SyntaxHighlighterBase.java:296-306); the shift is applied and
# cleared by applyFixup only when a shift is pending (java:315-330, clearFixup is inside the if). So the clear needs the pending state.
NEED_FIX = 'A text shift is pending in the highlighter (an earlier edit it has not applied yet)'
STATE_KINDS_OF[NEED_FIX] = ['session']  # an earlier in-app edit of this session (the same kind as NEED_DOC_OPEN and NEED_PREVIEW)
e('SyntaxHighlighterBase.applyFixup', 'SyntaxHighlighterBase.clearFixup', 'CALL',
  'Apply the pending text shift and forget it (only a pending shift is cleared)',
  needs_state=NEED_FIX,
  evidence='SRC SyntaxHighlighterBase.java:296-306 (fixup records a shift only when none is pending); SRC SyntaxHighlighterBase.java:315-330 (applyFixup calls clearFixup only when _fixupAfter >= 0 and _fixupDelta != 0)')
e('HighlightingEditor$1.onTextChanged', 'HighlightingEditor$1.afterTextChanged', 'CALL',
  'The same edit then reaches afterTextChanged, which starts the debounced re-highlight',
  evidence='SRC HighlightingEditor.java:94-108 (the watcher gets onTextChanged, then afterTextChanged, for one edit)')
e('HighlightingEditor$1.afterTextChanged', 'HighlightingEditor.recomputeHighlightingAsync', 'FRAMEWORK',
  'The debounce timer runs the async re-highlight: the worker computes the spans and the screen thread applies them',
  evidence='SRC HighlightingEditor.java:105-108 (afterTextChanged runs _hlDebounced); SRC HighlightingEditor.java:238 (the debounced runnable is recomputeHighlightingAsync)')

# C6 listener and callback bodies: each lambda or method reference that the bytecode registers (REGISTER edge, which the
# search skips) gets one FRAMEWORK edge from the method that registers it, so the body is reachable once that method is.
# The listener type is not read per lambda, so the label is INFERRED (see Limits in readme_notes.md).
# guards of the listener registrations that cite the bytecode line (the registration line, read in the source with its enclosing
# if and the early returns above it). Keyed by (registrar, listener). Only these registrations carry a guard.
_LISTENER_GUARDS = {
    ('DocumentShareIntoFragment$ShareIntoImportOptionsFragment.getFormatted', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.lambda$getFormatted$2'):
        ['asLink is true (the if at DocumentShareIntoFragment.java:385 encloses the line walk that registers the listener)'],
    ('MarkorDialogFactory.showSetPasswordDialog', 'MarkorDialogFactory.lambda$showSetPasswordDialog$63'):
        ['Build.VERSION.SDK_INT >= Build.VERSION_CODES.M (the if at MarkorDialogFactory.java:1024 encloses the dialog setup)'],
    ('MainActivity.onClickFab', 'MainActivity.newItemCallback'): [
        'not (_notebook == null || _notebook.getAdapter() == null) (early return at MainActivity.java:344-346)',
        '_notebook.getAdapter().isCurrentFolderWriteable() is true (early return at MainActivity.java:348-351 when false)',
        'view.getId() == R.id.fab_add_new_item (the if at MainActivity.java:353)',
        'not (_cu.isUnderStorageAccessFolder(this, _notebook.getCurrentFolder(), true) && _cu.getStorageAccessFrameworkTreeUri(this) == null) (early return at MainActivity.java:354-357)'],
    ('HighlightingEditor.setHighlighter', 'HighlightingEditor.recomputeHighlightingAsync'):
        ['_hl != null (the if at HighlightingEditor.java:236 encloses the debounced listener)'],
    ('HighlightingEditor.recomputeHighlightingAsync', 'HighlightingEditor._recomputeHighlightingWorker'):
        ['_hlEnabled && runHighlight(true) (the if at HighlightingEditor.java:204 encloses the executor call)'],
    ('DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.onFsViewerSelected',
     'DocumentShareIntoFragment$ShareIntoImportOptionsFragment$1.lambda$onFsViewerSelected$0'):
        ['sel is not null and sel.isDirectory() (the else-if at DocumentShareIntoFragment.java:469 encloses the registration)'],
    ('GsFileBrowserListAdapter.loadFolder', 'GsFileBrowserListAdapter.lambda$loadFolder$5'): [
        'not (folder == null || _recyclerView == null) (early return at GsFileBrowserListAdapter.java:645-647)',
        '_currentFolder != null (the if at GsFileBrowserListAdapter.java:675 encloses the executor call)'],
    ('GsFileBrowserListAdapter.postScrollToAndFlash', 'GsFileBrowserListAdapter.lambda$postScrollToAndFlash$2'):
        ['_recyclerView != null && file != null (the if at GsFileBrowserListAdapter.java:616 encloses the post)'],
    ('GsFileBrowserListAdapter.scrollToAndFlash', 'GsFileBrowserListAdapter.lambda$scrollToAndFlash$4'):
        ['pos >= 0 && _layoutManager != null (the if at GsFileBrowserListAdapter.java:628 encloses the post at line 630)'],
    ('GsFileBrowserListAdapter.lambda$scrollToAndFlash$4', 'GsFileBrowserListAdapter.lambda$scrollToAndFlash$3'):
        ['pos >= 0 && _layoutManager != null (the if at GsFileBrowserListAdapter.java:628 encloses the lambda that registers this one)'],
    ('MarkorDialogFactory.showSearchFilesDialog', 'MarkorDialogFactory.lambda$showSearchFilesDialog$2'): [
        'not (activity == null || searchDir == null || !searchDir.canRead()) (early return at MarkorDialogFactory.java:149-151)',
        '!FileSearchEngine.isSearchExecuting.get() (the if at MarkorDialogFactory.java:153 encloses the dialog call)'],
    ('MarkorDialogFactory.lambda$showSearchFilesDialog$2', 'MarkorDialogFactory.lambda$showSearchFilesDialog$1'): [
        'not (activity == null || searchDir == null || !searchDir.canRead()) (early return at MarkorDialogFactory.java:149-151)',
        '!FileSearchEngine.isSearchExecuting.get() (the if at MarkorDialogFactory.java:153; the file search dialog calls this callback only inside it)'],
    ('TextSearchFragment.onViewCreated', 'TextSearchFragment.lambda$onViewCreated$9'):
        ['initialized is true (early return at TextSearchFragment.java:91-94 when false, after close())'],
}


def _wire_listeners(rf):
    # called inside the section E fixpoint with the current reach set rf: a registration gets its edge only when the
    # method that registers it is reached (a dead registrar must not make its listener look reachable). Returns the count added.
    n = 0
    for _l in AUTO['lambdas']:
        if _l['src'] not in rf or (_l['src'], _l['dst'], 'FRAMEWORK') in _HAND or (_l['src'], _l['dst']) in _REG_SKIP:
            continue
        e(_l['src'], _l['dst'], 'FRAMEWORK',
          'Listener or callback registered by this method runs when its event fires (view event, dialog button, handler or fragment callback)',
          guard=list(_LISTENER_GUARDS.get((_l['src'], _l['dst']), [])) or None,
          evidence='INFERRED listener registered at %s:%s (bytecode line); the listener type is not read per lambda' % (_l['file'], _l['line']))
        n += 1
    return n

# D1 framework and library callbacks. A method with no bytecode caller (no call, lambda or hand edge reaches it) that is an
# instance method of a class with a supertype outside the app source (or an override of an app method), and whose name is a
# callback name of a framework or library interface, runs when the framework or library calls it on an object the app creates.
# Each constructor caller of that class (bytecode `C.<init>` call) gets one FRAMEWORK edge to the method. The label is INFERRED:
# the callback name is matched, not read per interface. Menu placeholder classes (GsMenuItemDummy, its Menu) are wired for all
# instance methods: app code calls them through android.view.Menu / MenuItem, which the bytecode table does not link.
import json as _json
import os as _os
_ML = _json.load(open(_os.path.join(GDIR, 'method_list.json')))
_HIER = _json.load(open(_os.path.join(GDIR, 'scratch', 'hier.json')))
_FLAGS = {(m['class'], m['name'], m['desc']): m.get('flags', []) for m in _ML}
_SIMPLE_CLS = {}
for _m in _ML:
    _SIMPLE_CLS.setdefault(_m['class'].split('/')[-1], set()).add(_m['class'])
_CB_NAMES = set('''
afterTextChanged beforeTextChanged onTextChanged onClick onLongClick onItemClick onItemSelected onNothingSelected run
onScrollChanged onGlobalLayout onLayoutChange onAnimationEnd onAnimationStart onAnimationCancel onReceive
onQueryTextChange onQueryTextSubmit onActionItemClicked onCreateActionMode onDestroyActionMode onPrepareActionMode
onDismissed onTouchEvent onInterceptTouchEvent onDraw onMeasure onLayout onAttachedToWindow onDetachedFromWindow
onVisibilityChanged onSelectionChanged onTextContextMenuItem getAutofillType sendAccessibilityEventUnchecked onPreDraw
onOverScrolled onSaveInstanceState onRestoreInstanceState onViewAttachedToWindow onViewDetachedFromWindow
onHideCustomView onShowCustomView onPageFinished shouldOverrideUrlLoading onProgressChanged
getItemCount getItemId getItem getCount getView getItemViewType onCreateViewHolder onBindViewHolder onAttachedToRecyclerView
getDropDownView isEmpty getChildView getGroupView getChildrenCount getGroupCount getChildId getGroupId getCombinedChildId
getCombinedGroupId hasStableIds isChildSelectable areAllItemsEnabled onGroupCollapsed onGroupExpanded registerDataSetObserver
unregisterDataSetObserver performFiltering publishResults onMove onSwiped onSelectedChanged clearView accept
doInBackground onPreExecute onPostExecute onProgressUpdate onCancelled compare compareTo equals hashCode toString
onCreate onCreateDialog onCreateView onViewCreated onResume onPause onStop onStart onDismiss onAttach onDestroy onDestroyView
onActivityResult onOptionsItemSelected onCreateOptionsMenu onBackPressed onKeyDown onPreferenceTreeClick onCreatePreferences
onPreferenceStartScreen onSharedPreferenceChanged onDisplayPreferenceDialog onPreferenceChanged onPreferenceScreenChanged
onPreferenceClicked onPostResume onNewIntent getItemOffsets
containsItem setSelection filter isSuggestionsEnabled getOriginal getReplacement getCallbackFragment
visit render parse create extend getNodeRenderingHandlers setAttributes finalizeBlock finalizeDocument getAfterDependents
getBeforeDependents getCharacters affectsGlobalScope getSegments getOpeningMarker getClosingMarker setOpeningMarker
setClosingMarker getAstExtra setIn parserOptions rendererOptions setText
updateDrawState updateMeasureState draw getSize chooseHeight drawBackground
append charAt clear delete getChars getFilters getSpans insert removeSpan setFilters setSpan subSequence getSpanEnd
getSpanFlags getSpanStart nextSpanTransition clearSpans length getSummary callChangeListener
'''.split())
_MENU_CLASSES = {'net/gsantner/opoc/wrapper/GsMenuItemDummy', 'net/gsantner/opoc/wrapper/GsMenuItemDummy$Menu'}


# ================================================================== G. views and preferences inflated from XML layouts
# The layout inflater and the preference inflater create each XML tag with its (Context, AttributeSet) constructor.
# The creating method is the one that inflates the layout (SRC line numbers below); the framework lifecycle step is INFERRED.
_XML_LIFE = 'The fragment system creates the view of this fragment: AndroidX calls onCreateView (library source not read)'
e('DocumentEditAndViewFragment.<init>', 'GsFragmentBase.onCreateView', 'FRAMEWORK', _XML_LIFE,
  evidence='INFERRED AndroidX Fragment calls onCreateView (library source not read); SRC GsFragmentBase.java:71-75 inflates getLayoutResId; SRC DocumentEditAndViewFragment.java:133-135 returns document__fragment__edit')
e('DocumentShareIntoFragment.<init>', 'GsFragmentBase.onCreateView', 'FRAMEWORK', _XML_LIFE,
  evidence='INFERRED AndroidX Fragment calls onCreateView (library source not read); SRC GsFragmentBase.java:71-75; SRC DocumentShareIntoFragment.java:85-87 returns document__fragment__share_into')
for _ctor, _ln in (('DraggableScrollbarScrollView.<init>(Context,AttributeSet)', 31), ('LineNumbersView.<init>(Context,AttributeSet)', 44),
                   ('HighlightingEditor.<init>', 49), ('GsHorizontalScrollView.<init>(Context,AttributeSet)', 74)):
    e('DocumentEditAndViewFragment.<init>', _ctor, 'FRAMEWORK',
      'The layout inflater creates this view from its XML tag in the edit layout',
      evidence='INFERRED layout inflater creates this tag (XML constructor); SRC res/layout/document__fragment__edit.xml:%d; the layout is inflated by GsFragmentBase.onCreateView for DocumentEditAndViewFragment' % _ln)
e('DocumentEditAndViewFragment.setupWebViewIfNeeded', 'DraggableScrollbarWebView.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'The web view stub inflates the view-mode layout (ViewStub.inflate) and creates this web view',
  evidence='SRC DocumentEditAndViewFragment.java:1006 (_webViewStub.inflate); SRC res/layout/document__fragment__edit.xml:98 (ViewStub layout document__fragment_view); SRC res/layout/document__fragment_view.xml:2')
for _ctor, _ln in (('GsLinearSplitLayout.<init>(Context,AttributeSet)', 11), ('HighlightingEditor.<init>', 28)):
    e('DocumentShareIntoFragment.<init>', _ctor, 'FRAMEWORK', 'The layout inflater creates this view from its XML tag in the share-into layout',
      evidence='INFERRED layout inflater creates this tag (XML constructor); SRC res/layout/document__fragment__share_into.xml:%d; inflated by GsFragmentBase.onCreateView for DocumentShareIntoFragment' % _ln)
e('NewFileDialog.makeDialog', 'NewFileDialog$ReselectSpinner.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'The new-file dialog inflates its layout, which has two spinners of this class',
  evidence='SRC NewFileDialog.java:106 (inflate R.layout.new_file_dialog); SRC res/layout/new_file_dialog.xml:139, 156')
e('SettingsActivity$SettingsFragmentMaster.<init>', 'GsPreferenceFragmentBase.onCreatePreferences', 'FRAMEWORK',
  'The preference fragment creates its screen: PreferenceFragmentCompat calls onCreatePreferences (library source not read)',
  evidence='INFERRED PreferenceFragmentCompat calls onCreatePreferences (library source not read); SRC GsPreferenceFragmentBase.java:153-160; SRC SettingsActivity.java:147-148')
# (getLinkTitle route, step 11) the share-into import options fragment creates its own screen: the framework calls onCreatePreferences
# on this receiver, so the call to afterOnCreate is made on the variant node (the base lift to the share-into override is in _LIFT_SKIP).
e('DocumentShareIntoFragment$ShareIntoImportOptionsFragment.<init>', 'GsPreferenceFragmentBase.onCreatePreferences@DocumentShareIntoFragment$ShareIntoImportOptionsFragment', 'FRAMEWORK',
  'The import options fragment creates its screen: PreferenceFragmentCompat calls onCreatePreferences on this receiver (library source not read)',
  guard=['_savedInstanceState == null (the if at DocumentShareIntoFragment.java:95 encloses the creation at line 97)'],
  evidence='INFERRED PreferenceFragmentCompat calls onCreatePreferences on the fragment (library source not read); SRC GsPreferenceFragmentBase.java:153-160; SRC DocumentShareIntoFragment.java:97')
for _ctor, _ln in (('GsFontPreferenceCompat.<init>(Context,AttributeSet)', 210), ('GsLanguagePreferenceCompat.<init>(Context,AttributeSet)', 652)):
    e('GsPreferenceFragmentBase.onCreatePreferences', _ctor, 'FRAMEWORK', 'addPreferencesFromResource creates this preference from its XML tag in preferences_master',
      evidence='INFERRED preference inflater creates this tag (XML constructor); SRC res/xml/preferences_master.xml:%d; SRC GsPreferenceFragmentBase.java:160' % _ln)

def _ancestors(c, seen=None):
    seen = set() if seen is None else seen
    h = _HIER.get(c)
    if h:
        for p in ([h['super']] if h['super'] else []) + h['ifaces']:
            if p and p not in seen:
                seen.add(p)
                _ancestors(p, seen)
    return seen


import collections as _collections
_TEXT = _json.load(open(_os.path.join(GDIR, 'scratch', 'textcount.json')))   # identifier -> count in app .java/.kt/.xml (scratch/textcount.py)
_DECL_N = _collections.Counter(_m['name'] for _m in _ML)
_DOT = _json.load(open(_os.path.join(GDIR, 'scratch', 'dotcount.json')))   # identifier used as 'x.name(' in app .java/.kt
_UNIV = {_m['class'] for _m in _ML}
_CB_TRIG = 'Framework or library calls this method on the object created here (listener, adapter, view, dialog, task or fragment hook)'
_MENU_TRIG = 'App code calls this Menu or MenuItem method through the interface on the placeholder created here'


def _has_text_ref(name):
    return _TEXT.get(name, 0) - _DECL_N.get(name, 0) > 0


def _base(n):
    return n.split('@')[0]


def _auto_edges_now():
    # the same filter the builder applies (tools/build_graph.py add_auto_edges): a bytecode call is dropped when a hand
    # edge already links the same base pair (or the same receiver node), and is copied onto the hand-written context
    # variants of its source. Without this filter the search below would follow calls the builder never makes.
    recv = set(AUTO.get('receiver_variants', ()))
    manual = {(_base(s_), _base(d_)) for s_, d_, k_ in _EDGE_LOG if k_ != 'REGISTER'}
    manual_nodes = {(s_, _base(d_)) for s_, d_, k_ in _EDGE_LOG if k_ != 'REGISTER'}
    variants = _collections.defaultdict(set)
    for s_, d_, k_ in _EDGE_LOG:
        for n_ in (s_, d_):
            if '@' in n_ and not n_.startswith('S_') and n_ not in recv:
                variants[_base(n_)].add(n_)
    out = []
    for c_ in AUTO['calls']:
        if c_['src'] in recv:
            if (c_['src'], _base(c_['dst'])) in manual_nodes:
                continue
        elif (_base(c_['src']), _base(c_['dst'])) in manual:
            continue
        for s_ in [c_['src']] + sorted(variants.get(c_['src'], ())):
            out.append((s_, c_['dst']))
    return out


def _reach_full():
    # the same search the builder runs, on full node names (receiver variants 'X.m@Y' are separate nodes):
    # from S_ENTRY over every edge except REGISTER (hand edges and the bytecode calls the builder keeps)
    adj = _collections.defaultdict(set)
    for s_, d_, k_ in _EDGE_LOG:
        if k_ != 'REGISTER':
            adj[s_].add(d_)
    for s_, d_ in _auto_edges_now():
        adj[s_].add(d_)
    seen, st = {'S_ENTRY'}, ['S_ENTRY']
    while st:
        x = st.pop()
        for y in adj.get(x, ()):
            if y not in seen:
                seen.add(y)
                st.append(y)
    return seen


def _labels(rf):
    # the build labels a method REACHABLE when its own node or one of its receiver variants is reached
    return {n for n in rf if '@' not in n} | {_base(n) for n in rf if '@' in n}


_VAR_TRIG = 'A receiver variant runs the body of the same method (INFERRED link; the variant is the same method for another receiver class)'


_LIFT_TRIG = 'The base method runs with the receiver of a live subclass, so the call on that receiver is made (INFERRED lift of a receiver-variant call)'


def _class_live(simple_cls, rf):
    # an object of this simple class is created on a reached path (a bytecode constructor call or its own <init> node)
    if any(x in rf for x in _CREATORS.get(simple_cls, ())):
        return True
    return any(n in rf for n in AUTO['impl'].get(simple_cls, {}).get('<init>', {}).values())


# (E2 fix) base-method lifts that would send a preference fragment's receiver to another class's override. The base body
# GsPreferenceFragmentBase.onPreferenceTreeClick is reached from every preference fragment's creator; the lift to each live
# subclass's onPreferenceClicked made the More page's receiver run the Settings override (wrong route). Each of these overrides is
# reached from its own page (S_MORE, S_SETTINGS, S_SHARE_INTO), and its receiver-specific call stays on the variant node.
_LIFT_SKIP = {
    ('GsPreferenceFragmentBase.onPreferenceTreeClick', 'MoreInfoFragment.onPreferenceClicked'),
    ('GsPreferenceFragmentBase.onPreferenceTreeClick', 'SettingsActivity$SettingsFragmentMaster.onPreferenceClicked'),
    ('GsPreferenceFragmentBase.onPreferenceTreeClick', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.onPreferenceClicked'),
    # (getLinkTitle route, step 11) the base onCreatePreferences was reached with the Settings fragment as receiver and lifted to the
    # share-into override afterOnCreate, which that receiver never calls. The share-into receiver makes this call on its own variant
    # node (GsPreferenceFragmentBase.java:169), which is reached from the share-into fragment's creation (hand edge below).
    ('GsPreferenceFragmentBase.onCreatePreferences', 'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.afterOnCreate'),
    # (S2, sample route 21, partial) SyntaxHighlighterBase.compute was lifted to AsciidocSyntaxHighlighter on the todo page; the
    # Asciidoc receiver is not the todo page's highlighter. The base body still lifts to KeyValueSyntaxHighlighter (not fixed).
    ('SyntaxHighlighterBase.compute', 'AsciidocSyntaxHighlighter.generateSpans'),
    # (draw route) the base compute reaches TodoTxtBasicSyntaxHighlighter.generateSpans only as TodoTxtSyntaxHighlighter's super call
    ('SyntaxHighlighterBase.compute', 'TodoTxtBasicSyntaxHighlighter.generateSpans'),
    # (first-visible fix, sample route 8) checkRunFirstTimeVisible runs with the visible page as receiver. The lift from the editor's
    # receiver variant would send the notebook page's first-visible check to the editor hook. The editor's own check is its onResume edge.
    ('GsFragmentBase.checkRunFirstTimeVisible', 'DocumentEditAndViewFragment.onFragmentFirstTimeVisible'),
    # (sample route 9, wikitextPagePathToRelativeFilePath) the toolbar button listener (ActionButtonBase.java:354, 366) runs the
    # onActionClick / onActionLongClick of the page's own format. The lift to every format's class sent a todo page's button to the
    # wikitext actions. Each class is now reached from its own page with its format state (the action-button edges below).
    ('ActionButtonBase.lambda$appendActionButtonToBar$3', 'AsciidocActionButtons.onActionClick'),
    ('ActionButtonBase.lambda$appendActionButtonToBar$3', 'MarkdownActionButtons.onActionClick'),
    ('ActionButtonBase.lambda$appendActionButtonToBar$3', 'OrgmodeActionButtons.onActionClick'),
    ('ActionButtonBase.lambda$appendActionButtonToBar$3', 'TodoTxtActionButtons.onActionClick'),
    ('ActionButtonBase.lambda$appendActionButtonToBar$3', 'WikitextActionButtons.onActionClick'),
    ('ActionButtonBase.lambda$appendActionButtonToBar$4', 'MarkdownActionButtons.onActionLongClick'),
    ('ActionButtonBase.lambda$appendActionButtonToBar$4', 'TodoTxtActionButtons.onActionLongClick'),
    ('ActionButtonBase.lambda$appendActionButtonToBar$4', 'WikitextActionButtons.onActionLongClick'),
    # (sample route 9, wikitextPagePathToRelativeFilePath) TextConverterBase.convertMarkupShowInWebView runs with the page's converter
    # as receiver. Its lifts to every converter's convertMarkup (TextConverterBase.java:110) are skipped; each converter is reached
    # from the base body with its format state (the converter edges below).
    ('TextConverterBase.convertMarkupShowInWebView', 'AsciidocTextConverter.convertMarkup'),
    ('TextConverterBase.convertMarkupShowInWebView', 'CsvTextConverter.convertMarkup'),
    ('TextConverterBase.convertMarkupShowInWebView', 'EmbedBinaryTextConverter.convertMarkup'),
    ('TextConverterBase.convertMarkupShowInWebView', 'MarkdownTextConverter.convertMarkup'),
    ('TextConverterBase.convertMarkupShowInWebView', 'OrgmodeTextConverter.convertMarkup'),
    ('TextConverterBase.convertMarkupShowInWebView', 'PlaintextTextConverter.convertMarkup'),
    ('TextConverterBase.convertMarkupShowInWebView', 'TodoTxtTextConverter.convertMarkup'),
    ('TextConverterBase.convertMarkupShowInWebView', 'WikitextTextConverter.convertMarkup'),
}

# (sample route 7, findNotebookRootDir) fetchAndInsertItem registers its callbacks for every insert action. The lambda that sets
# a picked file (lambda$10, the in-app browse action only) is not run by the camera path, so its registration is skipped here.
# The camera and gallery result callback (lambda$9, insertFileLink) runs only after an external app returns a picture: it gets
# the picker environment edge below.
# _REG_SKIP: listener registrations that get no FRAMEWORK edge from the registrar (the route must reach the listener by the user's tap)
_REG_SKIP = {('AttachLinkOrFileDialog.fetchAndInsertItem', 'AttachLinkOrFileDialog.lambda$fetchAndInsertItem$10'),
             # the bottom-nav listener and the plus / long-press buttons are tapped on a shown page (S_NOTEBOOK etc.), not
             # right after onCreate: the taps are the GUI edges written above, so the route keeps the tap step
             ('MainActivity.onCreate', 'MainActivity.lambda$onCreate$0'),
             ('MainActivity.onCreate', 'MainActivity.onClickFab'),
             ('MainActivity.onCreate', 'MainActivity.onLongClickFab'),
             # the toolbar listener is registered in GsActivityBase.onResume (GsActivityBase.java:94-98), but the tap is a user action on
             # the shown notebook page: the registration gets no FRAMEWORK edge, and the tap is the GUI edge from S_NOTEBOOK (above)
             ('GsActivityBase.onResume', 'GsActivityBase.onToolbarClick')}


def _link_variants(rf):
    # (1) a receiver variant 'M@C' reached without its base M: link it to M, so the body's own calls are followed by the search.
    # (2) a call made from a receiver variant 'M@C' is also made from the base M when C is a live class: the base body
    #     runs with C as the receiver (lambda bodies and other base methods reached without a receiver context need this).
    # The builder labels M REACHABLE through a variant, and the calls must follow the same way.
    n = 0
    for _v in sorted(rf):
        if '@' in _v and _base(_v) not in rf and (_v, _base(_v), 'CALL') not in _HAND:
            e(_v, _base(_v), 'CALL', _VAR_TRIG,
              evidence='INFERRED receiver variant %s runs the body of %s (same method, another receiver class)' % (_v, _base(_v)))
            n += 1
    for c_ in AUTO['calls']:
        sv_ = c_['src']
        if '@' not in sv_:
            continue
        bx_, rc_ = sv_.split('@', 1)
        if bx_ not in rf or c_['dst'] == bx_ or (bx_, c_['dst'], 'CALL') in _HAND:
            continue
        if not _class_live(rc_, rf):
            continue
        if (bx_, c_['dst']) in _LIFT_SKIP:
            continue
        e(bx_, c_['dst'], 'CALL', _LIFT_TRIG,
          evidence='INFERRED %s is reached and %s is a live class: the body of %s runs with %s as receiver (call in %s, file %s line %s)'
          % (bx_, rc_, bx_, rc_, sv_, c_.get('file'), c_.get('line')))
        n += 1
    return n


_CREATORS = {}     # simple class name -> nodes that call its constructor (bytecode `X.<init>` calls)
for _c in AUTO['calls']:
    _d = _c['dst'].split('(')[0]
    if _d.endswith('.<init>'):
        _CREATORS.setdefault(_d[:-len('.<init>')], set()).add(_c['src'])
_SUBS = _collections.defaultdict(set)
for _k in _HIER:
    for _a in _ancestors(_k):
        _SUBS[_a].add(_k)


def _creators_of(cls, name, desc):
    # creators of the class and of its subclasses that do not override this method: bytecode X.<init> calls, and the
    # constructor itself (a component that the manifest or the framework creates is live once its <init> is reached)
    out = set()
    for k in [cls] + sorted(_SUBS.get(cls, ())):
        if k != cls:
            blocked = any(p != cls and cls in _ancestors(p) and (p, name, desc) in _FLAGS for p in {k} | _ancestors(k))
            if blocked:
                continue
        out |= _CREATORS.get(k.split('/')[-1], set())
        for _init in AUTO['impl'].get(k.split('/')[-1], {}).get('<init>', {}).values():
            out.add(_init)
    return out


_NAME_N = _collections.Counter((_m['class'], _m['name']) for _m in _ML)   # overload count per (class, method name)
_CAND = []
for _m in _ML:
    _name, _cls, _fl = _m['name'], _m['class'], _m.get('flags', [])
    if _name in ('<init>', '<clinit>') or _name.startswith('lambda$') or 'static' in _fl or 'private' in _fl:
        continue
    _menu = _cls in _MENU_CLASSES
    if _menu:
        if _DOT.get(_name, 0) <= 0:    # the app calls this name on some object (menu.add, item.getItemId, ...)
            continue
    else:
        if _name not in _CB_NAMES:
            continue
        _anc = _ancestors(_cls)
        _ext = any(a not in _HIER and a != 'java/lang/Object' for a in _anc)
        _ovr = any(a in _UNIV and (a, _name, _m['desc']) in _FLAGS for a in _anc)
        if not (_ext or _ovr or _name in ('equals', 'hashCode', 'toString')):   # Object overrides are called by library collections and string code
            continue
    _crs = _creators_of(_cls, _name, _m['desc'])
    _node = AUTO['impl'].get(_cls.split('/')[-1], {}).get(_name, {}).get(_m['desc'])   # builder node name (with parameters if overloaded)
    if _node is None and _NAME_N[(_cls, _name)] == 1:   # class missing from AUTO impl (abstract base with no `new`): plain Class.method when not overloaded
        _node = _cls.split('/')[-1] + '.' + _name
    if _crs and _node:
        _CAND.append((_node, sorted(_crs), _menu, _name))

# (S3 fix, sample route 17) StoragePermissionActivity.onActivityResult is an Activity result hook. It runs only after
# startActivityForResult from this activity, and GsContextUtils.requestExternalStoragePermission calls that only on API 30+
# (GsContextUtils.java:2386-2402; the API 27 path is ActivityCompat.requestPermissions, which returns to onRequestPermissionsResult).
# The generic wiring from the constructor is skipped; the method is recorded UNREACHABLE (closed_by_api_level) in section H.
_CB_SKIP = {
    ('StoragePermissionActivity.<init>', 'StoragePermissionActivity.onActivityResult'),
    # (S5, route check) createFragment creates a Document only in its quick-note and todo branches, but the generic Object-override
    # wiring is per method, so the equals edge appeared on every createFragment route (cold-start notebook included).
    ('MainActivity$SectionsPagerAdapter.createFragment', 'Document.equals'),
}

# fixpoint: wire each candidate from every creator that the search already reaches; repeat until nothing new is wired
for _pass in range(60):
    _RF = _reach_full()
    _added = _link_variants(_RF) + _wire_listeners(_RF)
    _RF = _reach_full()
    _R = _labels(_RF)
    for _node, _crs, _menu, _name in _CAND:
        if _node in _R:
            continue
        for _x in _crs:
            if _x not in _RF or _x == _node or (_x, _node, 'FRAMEWORK') in _HAND or (_x, _node) in _CB_SKIP:
                continue
            e(_x, _node, 'FRAMEWORK', _MENU_TRIG if _menu else _CB_TRIG,
              evidence=('INFERRED method has no bytecode caller; object of this class created at %s (bytecode); '
                        'app text uses the name %s (Menu placeholder)' % (_x, _name)) if _menu else
                       ('INFERRED method has no bytecode caller; object of this class created at %s (bytecode); '
                        'callback name %s' % (_x, _name)))
            _added += 1
    if not _added:
        break

# ------------------------------------------------------------------ section F: an app override of a library method is reached through the app's library call
# The bytecode call table lists app-to-app calls only (dispatch 'exact' or 'cha'). Calls to library methods are listed in
# AUTO['framework_calls'] as 'Lib.m' per caller. If the app calls Lib.m and an app class overriding m has Lib among its
# ancestors, the library call can run that override (class-hierarchy target). Library sources are not on disk, so this is
# INFERRED.
_TRIG_CHA = 'The app calls the library method on an object whose app class overrides it here (class-hierarchy target)'
_FWC_IDX = _collections.defaultdict(set)     # (library simple name, method name) -> app nodes that make that call
for _src, _lst in (AUTO.get('framework_calls') or {}).items():
    for _s in _lst:
        if '.' in _s:
            _lc, _mn = _s.split('(')[0].rsplit('.', 1)
            _FWC_IDX[(_lc, _mn)].add(_src)
_CHA = []     # (app node that overrides, sorted caller nodes)
for _m in _ML:
    _name, _cls, _fl = _m['name'], _m['class'], _m.get('flags', [])
    if _name in ('<init>', '<clinit>') or _name.startswith('lambda$') or 'static' in _fl or 'private' in _fl:
        continue
    _libs = set()
    for _a in _ancestors(_cls):
        if _a not in _HIER and _a != 'java/lang/Object':
            _p = _a.split('/')[-1]
            _libs.add(_p)
            _libs.add(_p.split('$')[-1])
    _srcs = set()
    for _ln in _libs:
        _srcs |= _FWC_IDX.get((_ln, _name), set())
    _node = AUTO['impl'].get(_cls.split('/')[-1], {}).get(_name, {}).get(_m['desc'])
    if _srcs and _node:
        _CHA.append((_node, sorted(_srcs), sorted(_creators_of(_cls, _name, _m['desc']))))
for _pass in range(60):
    _RF = _reach_full()
    _added = _link_variants(_RF)
    _RF = _reach_full()
    _R = _labels(_RF)
    for _node, _srcs, _crs in _CHA:
        if _node in _R or not any(_c in _RF for _c in _crs):   # the object must be created on a reached path first
            continue
        for _x in _srcs:
            if _x not in _RF or _x == _node or (_x, _node, 'FRAMEWORK') in _HAND:
                continue
            e(_x, _node, 'FRAMEWORK', _TRIG_CHA,
              evidence='INFERRED library call made from %s dispatches to this app override (class hierarchy; library source not read)' % _x)
            _added += 1
    if not _added:
        break


# ================================================================== BYTECODE CITATIONS (tools/check_bytecode_lines.py, 2026-10-27)
# The bytecode line table gives the start of the statement (for example `return Arrays.asList(` or `runRegexReplaceAction(`).
# For these edges the constructor call sits on a later line of the same statement, and the callee name is not on the cited
# line. Each entry moves the citation to the line that holds the matching `new X(` call (parameter types read from the source).
# The bytecode line stays in the edge note. Applied to every edge before ids are made (EDIT hook of tools/build_graph.py).
_BC_LINE_FIX = {
    ('SearchAndReplaceTextDialog.saveRecentReplace', 'SearchAndReplaceTextDialog$ReplaceGroup.<init>', 326): 325,
    ('PlaintextActionButtons.getFormatActionList', 'ActionButtonBase$ActionItem.<init>', 32): 33,
    ('MarkdownActionButtons.getFormatActionList', 'ActionButtonBase$ActionItem.<init>', 66): 67,
    ('MarkdownActionButtons.runLineSurroundAction', 'ActionButtonBase$ReplacePattern.<init>(Pattern,String)', 174): 175,
    ('OrgmodeActionButtons.getFormatActionList', 'ActionButtonBase$ActionItem.<init>', 24): 25,
    ('TodoTxtActionButtons.getFormatActionList', 'ActionButtonBase$ActionItem.<init>', 54): 55,
    ('TodoTxtActionButtons.onActionClick', 'ActionButtonBase$ReplacePattern.<init>(String,String)', 85): 87,
    ('TodoTxtActionButtons.insertUniqueItem', 'ActionButtonBase$ReplacePattern.<init>(String,String)', 311): 316,
    ('TodoTxtActionButtons.insertUniqueItem', 'ActionButtonBase$ReplacePattern.<init>(Pattern,String)', 311): 314,
    ('TodoTxtActionButtons.lambda$setDueDate$5', 'ActionButtonBase$ReplacePattern.<init>(String,String)', 407): 411,
    ('TodoTxtActionButtons.lambda$setDueDate$5', 'ActionButtonBase$ReplacePattern.<init>(Pattern,String)', 407): 409,
    ('AsciidocActionButtons.getFormatActionList', 'ActionButtonBase$ActionItem.<init>', 32): 33,
    ('AsciidocSyntaxHighlighter.generateSpans', 'WrMarkdownHeaderSpanCreator.<init>', 243): 242,
    ('AsciidocSyntaxHighlighter.generateSpans', 'WrAsciidocHeaderSpanCreator.<init>', 241): 240,
    ('WikitextReplacePatternGenerator.toggleCheckboxToNextState', 'ActionButtonBase$ReplacePattern.<init>(Pattern,String)', 118): 119,
    ('WikitextActionButtons.getFormatActionList', 'ActionButtonBase$ActionItem.<init>', 47): 48,
}
# An implicit call (try-with-resources closes Csv2MdTable at the end of the try block): no line of the source names close().
# The citation stays on line 88 and is labelled as implicit, so the bytecode check does not report it as a missing callee.
_BC_TEXT_FIX = {
    ('CsvTextConverter$Csv2MdTable.toMdTable(Reader)', 'CsvTextConverter$Csv2MdTable.close', 88):
        'try-with-resources, implicit close at the end of the try block',
}


def _bc_citation_fix(x):
    ev = x.get('evidence') or ''
    if not (ev.startswith('SRC ') and ev.endswith(' (bytecode)')):
        return
    fname, _, n = ev[4:-len(' (bytecode)')].rpartition(':')
    if not n.isdigit():
        return
    key = (x['src'], x['dst'], int(n))
    if key in _BC_LINE_FIX:
        new = _BC_LINE_FIX[key]
        x['evidence'] = 'SRC %s:%d (bytecode)' % (fname, new)
        note = 'bytecode line table gives line %s (start of the statement); the constructor call is on line %d' % (n, new)
        x['note'] = ((x.get('note') or '') + ' ' + note).strip()
    elif key in _BC_TEXT_FIX:
        x['evidence'] = 'SRC %s:%s (%s)' % (fname, n, _BC_TEXT_FIX[key])
        note = 'bytecode line table gives line %s; the name close is not written on that line (implicit call)' % n
        x['note'] = ((x.get('note') or '') + ' ' + note).strip()


# Guards on bytecode-cited calls of the sampled routes. The data file holds, for each call site (src|dst|source line),
# the enclosing conditions from the source (Cases.guard_of) plus the negated early returns above the call in the same
# scope (scratch/gen_guards2.py, run in this pass). The build copies the text onto the edge, so the route note states it.
_ROUTE_GUARD = _json.load(open(_os.path.join(GDIR, 'scratch', 'route_guards.json'), encoding='utf-8'))


def _route_guard_add(x):
    ev = x.get('evidence') or ''
    if not (ev.startswith('SRC ') and ev.endswith(' (bytecode)')):
        return
    # the bytecode line is the last number before ' (bytecode)': 'SRC F.java:L (bytecode)' or 'SRC F.java:A-B (text), L (bytecode)'
    n = ev[4:-len(' (bytecode)')].rsplit(',', 1)[-1].rpartition(':')[2].strip()
    key = '%s|%s|%s' % (x['src'], x['dst'], n)
    if key in _ROUTE_GUARD:
        x['guard'] = _ROUTE_GUARD[key]


def _row_tap_cite(x):
    # (round 8, Limits item 4) the adapter calls the dialog listener from two lines: the single-file row tap (GsFileBrowserListAdapter.java:426)
    # and the OK button (440). The bytecode scan keeps one line per edge (440 was the first it met), so the file-tap edges cite both lines.
    if (x.get('kind') == 'CALL' and x['src'] == 'GsFileBrowserListAdapter.onClick' and x['dst'].rpartition('.')[2] == 'onFsViewerSelected'
            and x.get('evidence') == 'SRC GsFileBrowserListAdapter.java:440 (bytecode)'):
        x['evidence'] = ('SRC GsFileBrowserListAdapter.java:426 (the single-file row tap calls the same listener on this line); '
                         'SRC GsFileBrowserListAdapter.java:440 (bytecode)')
        x['note'] = ((x.get('note') or '') + ' The OK button (line 440) and the file tap (line 426) both call this listener; the bytecode '
                     'citation is the OK-button line, the file tap is cited in the text.').strip()


def _edit(x):
    _bc_citation_fix(x)
    _route_guard_add(x)
    _row_tap_cite(x)


EDIT = _edit


# ================================================================== H. UNREACHABLE entries (generated by scratch/emit_unreach.py)
# Each entry: method -> (kind, reason, source_ref, confirmed_by). Source of truth: scratch/dead_plan.json plus the manual decisions in emit_unreach.py.
UNREACHABLE = {
    'ActionButtonBase$ReplacePattern.<init>(String,String,boolean)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/markor/format/ActionButtonBase.java:436', 'SOURCE'),
    'ActionButtonBase.getDocument': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getDocument', 'src/main/java/net/gsantner/markor/format/ActionButtonBase.java:600', 'SOURCE'),
    'ActionButtonBase.runRegularPrefixAction(String)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name runRegularPrefixAction', 'src/main/java/net/gsantner/markor/format/ActionButtonBase.java:378', 'SOURCE'),
    'ActionButtonBase.runRegularPrefixAction(String,String)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name runRegularPrefixAction', 'src/main/java/net/gsantner/markor/format/ActionButtonBase.java:386', 'SOURCE'),
    'AppSettings.getAsFileList': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getAsFileList', 'src/main/java/net/gsantner/markor/model/AppSettings.java:652', 'SOURCE'),
    'AppSettings.getFileBrowserLastBrowsedFolder': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getFileBrowserLastBrowsedFolder', 'src/main/java/net/gsantner/markor/model/AppSettings.java:994', 'SOURCE'),
    'AppSettings.getLastEditScrollY': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getLastEditScrollY', 'src/main/java/net/gsantner/markor/model/AppSettings.java:473', 'SOURCE'),
    'AppSettings.getLastViewPositionX': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getLastViewPositionX', 'src/main/java/net/gsantner/markor/model/AppSettings.java:610', 'SOURCE'),
    'AppSettings.getLastViewPositionY': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getLastViewPositionY', 'src/main/java/net/gsantner/markor/model/AppSettings.java:617', 'SOURCE'),
    'AppSettings.getNavigationBarColor': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getNavigationBarColor', 'src/main/java/net/gsantner/markor/model/AppSettings.java:805', 'SOURCE'),
    'AppSettings.getRating': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getRating', 'src/main/java/net/gsantner/markor/model/AppSettings.java:888', 'SOURCE'),
    'AppSettings.isDynamicHighlightingEnabled': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isDynamicHighlightingEnabled', 'src/main/java/net/gsantner/markor/model/AppSettings.java:182', 'SOURCE'),
    'AppSettings.isEditorStartOnBotttom': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isEditorStartOnBotttom', 'src/main/java/net/gsantner/markor/model/AppSettings.java:366', 'SOURCE'),
    'AppSettings.isFileBrowserSortFolderFirst': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isFileBrowserSortFolderFirst', 'src/main/java/net/gsantner/markor/model/AppSettings.java:801', 'SOURCE'),
    'AppSettings.isHighlightingHexColorEnabled': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isHighlightingHexColorEnabled', 'src/main/java/net/gsantner/markor/model/AppSettings.java:338', 'SOURCE'),
    'AppSettings.isLineNumbersEnabled': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isLineNumbersEnabled', 'src/main/java/net/gsantner/markor/model/AppSettings.java:174', 'SOURCE'),
    'AppSettings.isLoadLastDirectoryAtStartup': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isLoadLastDirectoryAtStartup', 'src/main/java/net/gsantner/markor/model/AppSettings.java:85', 'SOURCE'),
    'AppSettings.setFileBrowserSortFolderFirst': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setFileBrowserSortFolderFirst', 'src/main/java/net/gsantner/markor/model/AppSettings.java:795', 'SOURCE'),
    'AppSettings.setLastViewPosition': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setLastViewPosition', 'src/main/java/net/gsantner/markor/model/AppSettings.java:481', 'SOURCE'),
    'AppSettings.setLineNumbersEnabled': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setLineNumbersEnabled', 'src/main/java/net/gsantner/markor/model/AppSettings.java:178', 'SOURCE'),
    'AppSettings.setRating': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setRating', 'src/main/java/net/gsantner/markor/model/AppSettings.java:892', 'SOURCE'),
    'AsciidocReplacePatternGenerator.<init>': ('no_trigger_in_app', 'class AsciidocReplacePatternGenerator is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/format/asciidoc/AsciidocReplacePatternGenerator.java:19', 'SOURCE'),
    'AttachLinkOrFileDialog.<init>': ('no_trigger_in_app', 'class AttachLinkOrFileDialog is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/frontend/AttachLinkOrFileDialog.java:45', 'SOURCE'),
    'AutoTextFormatter$ListLine.isSiblingLevelOf': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isSiblingLevelOf', 'src/main/java/net/gsantner/markor/frontend/textview/AutoTextFormatter.java:116', 'SOURCE'),
    'BackupUtils.<init>': ('no_trigger_in_app', 'class BackupUtils is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/util/BackupUtils.java', 'SOURCE'),
    'CodeTheme$ThemeValue.<init>': ('no_trigger_in_app', 'class CodeTheme$ThemeValue is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/format/plaintext/highlight/CodeTheme.java:12', 'SOURCE'),
    'CodeTheme.<init>': ('no_trigger_in_app', 'class CodeTheme is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/format/plaintext/highlight/CodeTheme.java:8', 'SOURCE'),
    'DatetimeFormatDialog.<init>': ('no_trigger_in_app', 'class DatetimeFormatDialog is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/frontend/DatetimeFormatDialog.java:49', 'SOURCE'),
    'Document.filenameFromContent': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name filenameFromContent', 'src/main/java/net/gsantner/markor/model/Document.java:374', 'SOURCE'),
    'Document.getFileExtension': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getFileExtension; the class extends library Serializable, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/model/Document.java:152', 'INFERRED'),
    'DocumentActivity.getExistingFragment': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getExistingFragment; the class extends library AppCompatActivity, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/activity/DocumentActivity.java:353', 'INFERRED'),
    'DocumentActivity.isDocumentAlreadyOpen': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isDocumentAlreadyOpen', 'src/main/java/net/gsantner/markor/activity/DocumentActivity.java:234', 'SOURCE'),
    'DocumentEditAndViewFragment.webViewJavascriptCallback': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name webViewJavascriptCallback; the class extends library Fragment, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/activity/DocumentEditAndViewFragment.java:1081', 'INFERRED'),
    'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.addDocumentToPrefgroup': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name addDocumentToPrefgroup', 'src/main/java/net/gsantner/markor/activity/DocumentShareIntoFragment.java:592', 'SOURCE'),
    'DocumentShareIntoFragment$ShareIntoImportOptionsFragment.getFragmentTag': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getFragmentTag; the class extends library PreferenceFragmentCompat, PreferenceFragmentCompat$OnPreferenceStartScreenCallback, SharedPreferences$OnSharedPreferenceChangeListener, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/activity/DocumentShareIntoFragment.java:180', 'INFERRED'),
    'DocumentShareIntoFragment.removeCheckbox': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name removeCheckbox', 'src/main/java/net/gsantner/markor/activity/DocumentShareIntoFragment.java:162', 'SOURCE'),
    'DraggableScrollbarScrollView.<init>(Context)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/markor/frontend/DraggableScrollbarScrollView.java:21', 'SOURCE'),
    'DraggableScrollbarScrollView.isFastScrollEnabled': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isFastScrollEnabled; the class extends library ScrollView, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/frontend/DraggableScrollbarScrollView.java:97', 'INFERRED'),
    'DraggableScrollbarScrollView.setFastScrollEnabled': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setFastScrollEnabled; the class extends library ScrollView, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/frontend/DraggableScrollbarScrollView.java:93', 'INFERRED'),
    'DraggableScrollbarScrollView.slowScrollShift': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name slowScrollShift; the class extends library ScrollView, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/frontend/DraggableScrollbarScrollView.java:29', 'INFERRED'),
    'DraggableScrollbarWebView.<init>(Context)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/markor/web/DraggableScrollbarWebView.java:21', 'SOURCE'),
    'DraggableScrollbarWebView.<init>(Context,AttributeSet,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/markor/web/DraggableScrollbarWebView.java:29', 'SOURCE'),
    'DraggableScrollbarWebView.isFastScrollEnabled': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isFastScrollEnabled; the class extends library WebView, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/web/DraggableScrollbarWebView.java:92', 'INFERRED'),
    'DraggableScrollbarWebView.lambda$scrollAnimatedToXY$0': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (DraggableScrollbarWebView.scrollAnimatedToXY)', 'src/main/java/net/gsantner/markor/web/DraggableScrollbarWebView.java:98', 'INFERRED'),
    'DraggableScrollbarWebView.scrollAnimatedToXY': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name scrollAnimatedToXY; the class extends library WebView, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/web/DraggableScrollbarWebView.java:98', 'INFERRED'),
    'DraggableScrollbarWebView.setFastScrollEnabled': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setFastScrollEnabled; the class extends library WebView, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/web/DraggableScrollbarWebView.java:88', 'INFERRED'),
    'FileSearchDialog.<init>': ('no_trigger_in_app', 'class FileSearchDialog is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/frontend/filesearch/FileSearchDialog.java:26', 'SOURCE'),
    'FileSearchEngine.<init>': ('no_trigger_in_app', 'class FileSearchEngine is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/frontend/filesearch/FileSearchEngine.java:46', 'SOURCE'),
    'FileSearchResultSelectorDialog.<init>': ('no_trigger_in_app', 'class FileSearchResultSelectorDialog is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/frontend/filesearch/FileSearchResultSelectorDialog.java:34', 'SOURCE'),
    'FlexmarkKatexExtension$FlexmarkKatexExtensionInternal.<init>': ('no_trigger_in_app', 'class FlexmarkKatexExtension$FlexmarkKatexExtensionInternal is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java:258', 'SOURCE'),
    'FlexmarkKatexExtension$KatexDisplayMath.<init>()': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java:132', 'SOURCE'),
    'FlexmarkKatexExtension$KatexDisplayMath.<init>(BasedSequence)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java:135', 'SOURCE'),
    'FlexmarkKatexExtension$KatexInlineMath.<init>()': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java:187', 'SOURCE'),
    'FlexmarkKatexExtension$KatexInlineMath.<init>(BasedSequence)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java:190', 'SOURCE'),
    'FlexmarkKatexExtension$KatexVisitorExt$1.<init>': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (FlexmarkKatexExtension$KatexVisitorExt.VISIT_HANDLERS)', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java', 'INFERRED'),
    'FlexmarkKatexExtension$KatexVisitorExt$1.visit': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of FlexmarkKatexExtension$KatexVisitorExt$1 or of a subclass', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java:122', 'SOURCE'),
    'FlexmarkKatexExtension$KatexVisitorExt$2.<init>': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (FlexmarkKatexExtension$KatexVisitorExt.VISIT_HANDLERS)', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java', 'INFERRED'),
    'FlexmarkKatexExtension$KatexVisitorExt$2.visit': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of FlexmarkKatexExtension$KatexVisitorExt$2 or of a subclass', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java:122', 'SOURCE'),
    'FlexmarkKatexExtension$KatexVisitorExt.<init>': ('no_trigger_in_app', 'class FlexmarkKatexExtension$KatexVisitorExt is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java:237', 'SOURCE'),
    'FlexmarkKatexExtension$KatexVisitorExt.VISIT_HANDLERS': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name VISIT_HANDLERS', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java:238', 'SOURCE'),
    'FlexmarkKatexExtension.<init>': ('no_trigger_in_app', 'class FlexmarkKatexExtension is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'thirdparty/java/other/com/vladsch/flexmark/ext/katex/FlexmarkKatexExtension.java:73', 'SOURCE'),
    'GsBackupUtils.<init>': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (BackupUtils.<init>)', 'src/main/java/net/gsantner/opoc/util/GsBackupUtils.java:40', 'INFERRED'),
    'GsCallback.<init>': ('no_trigger_in_app', 'class GsCallback is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/wrapper/GsCallback.java:13', 'SOURCE'),
    'GsCollectionUtils.<init>': ('no_trigger_in_app', 'class GsCollectionUtils is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/util/GsCollectionUtils.java:29', 'SOURCE'),
    'GsCollectionUtils.addAll(Collection,Collection)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name addAll', 'src/main/java/net/gsantner/opoc/util/GsCollectionUtils.java:40', 'SOURCE'),
    'GsCollectionUtils.all': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name all', 'src/main/java/net/gsantner/opoc/util/GsCollectionUtils.java:178', 'SOURCE'),
    'GsCollectionUtils.asList': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name asList', 'src/main/java/net/gsantner/opoc/util/GsCollectionUtils.java:35', 'SOURCE'),
    'GsCollectionUtils.intersection': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name intersection', 'src/main/java/net/gsantner/opoc/util/GsCollectionUtils.java:147', 'SOURCE'),
    'GsCollectionUtils.listComp': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name listComp', 'src/main/java/net/gsantner/opoc/util/GsCollectionUtils.java:77', 'SOURCE'),
    'GsCollectionUtils.replaceAll': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name replaceAll', 'src/main/java/net/gsantner/opoc/util/GsCollectionUtils.java:51', 'SOURCE'),
    'GsCollectionUtils.reverse': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name reverse', 'src/main/java/net/gsantner/opoc/util/GsCollectionUtils.java:257', 'SOURCE'),
    'GsCollectionUtils.select': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name select', 'src/main/java/net/gsantner/opoc/util/GsCollectionUtils.java:208', 'SOURCE'),
    'GsContextUtils$1.<init>': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsContextUtils.receiveResultFromLocalBroadcast)', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java', 'INFERRED'),
    'GsContextUtils$1.onReceive': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsContextUtils$1 or of a subclass', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:1939', 'SOURCE'),
    'GsContextUtils.areResourcesAvailable': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name areResourcesAvailable', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:283', 'SOURCE'),
    'GsContextUtils.bcbool': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsContextUtils.isFossBuild, GsContextUtils.isGooglePlayBuild)', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:395', 'INFERRED'),
    'GsContextUtils.calculateInSampleSize': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsContextUtils.loadImageFromFilesystem)', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:805', 'INFERRED'),
    'GsContextUtils.callTelephoneNumber': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name callTelephoneNumber', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2337', 'SOURCE'),
    'GsContextUtils.convertPxToDp': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name convertPxToDp', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:638', 'SOURCE'),
    'GsContextUtils.createLauncherDesktopShortcutLegacy': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name createLauncherDesktopShortcutLegacy', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:1212', 'SOURCE'),
    'GsContextUtils.createPdf': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name createPdf', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:1477', 'SOURCE'),
    'GsContextUtils.drawTextOnDrawable': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name drawTextOnDrawable', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:858', 'SOURCE'),
    'GsContextUtils.drawableToBitmap(Context,int)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsContextUtils.drawTextOnDrawable)', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:776', 'INFERRED'),
    'GsContextUtils.drawableToBitmap(Drawable)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsContextUtils.drawableToBitmap(Context,int))', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:753', 'INFERRED'),
    'GsContextUtils.getApplicationObject': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getApplicationObject', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:337', 'SOURCE'),
    'GsContextUtils.getClipboard': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getClipboard', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:1536', 'SOURCE'),
    'GsContextUtils.getCurrentAccentColor': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getCurrentAccentColor', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2678', 'SOURCE'),
    'GsContextUtils.getCurrentPrimaryColor': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getCurrentPrimaryColor', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2664', 'SOURCE'),
    'GsContextUtils.getCurrentPrimaryDarkColor': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getCurrentPrimaryDarkColor', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2671', 'SOURCE'),
    'GsContextUtils.getEstimatedScreenSizeInches': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getEstimatedScreenSizeInches', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:537', 'SOURCE'),
    'GsContextUtils.getLocalizedDateTimeFormat': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getLocalizedDateTimeFormat', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:947', 'SOURCE'),
    'GsContextUtils.getMediaUri': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getMediaUri', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:1989', 'SOURCE'),
    'GsContextUtils.isAppInstalled': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isAppInstalled', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:476', 'SOURCE'),
    'GsContextUtils.isConnectedToInternet': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isConnectedToInternet', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:463', 'SOURCE'),
    'GsContextUtils.isDeviceOrientationPortrait': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isDeviceOrientationPortrait', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:1084', 'SOURCE'),
    'GsContextUtils.isFossBuild': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isFossBuild', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:435', 'SOURCE'),
    'GsContextUtils.isGooglePlayBuild': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isGooglePlayBuild', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:428', 'SOURCE'),
    'GsContextUtils.isInPortraitMode': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isInPortraitMode', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:550', 'SOURCE'),
    'GsContextUtils.isInSplitScreenMode': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isInSplitScreenMode', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2743', 'SOURCE'),
    'GsContextUtils.isLauncherEnabled': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isLauncherEnabled', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2654', 'SOURCE'),
    'GsContextUtils.isWifiConnected': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isWifiConnected', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:1075', 'SOURCE'),
    'GsContextUtils.lambda$requestExternalStoragePermission$5': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsContextUtils.requestExternalStoragePermission(Activity,String))', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2386', 'INFERRED'),
    'GsContextUtils.loadImageFromFilesystem': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name loadImageFromFilesystem', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:789', 'SOURCE'),
    'GsContextUtils.loadMarkdownForTextViewFromRaw': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name loadMarkdownForTextViewFromRaw', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:513', 'SOURCE'),
    'GsContextUtils.mediaScannerScanFile': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name mediaScannerScanFile', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:728', 'SOURCE'),
    'GsContextUtils.receiveResultFromLocalBroadcast': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name receiveResultFromLocalBroadcast', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:1932', 'SOURCE'),
    'GsContextUtils.removeActivityFromHistory': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name removeActivityFromHistory', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2804', 'SOURCE'),
    'GsContextUtils.requestExternalStoragePermission(Activity,String)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsContextUtils.requestExternalStoragePermission(Activity,int), GsPermissionChecker.doIfExtStoragePermissionGranted(String))', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2408', 'INFERRED'),
    'GsContextUtils.requestExternalStoragePermission(Activity,int)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name requestExternalStoragePermission', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2404', 'SOURCE'),
    'GsContextUtils.restartApp': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name restartApp', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:489', 'SOURCE'),
    'GsContextUtils.scaleBitmap': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name scaleBitmap', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:821', 'SOURCE'),
    'GsContextUtils.sendLocalBroadcastWithStringExtra': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name sendLocalBroadcastWithStringExtra', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:1918', 'SOURCE'),
    'GsContextUtils.setDrawableWithColorToImageView': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setDrawableWithColorToImageView', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:745', 'SOURCE'),
    'GsContextUtils.setHtmlToTextView': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setHtmlToTextView', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:529', 'SOURCE'),
    'GsContextUtils.setStatusbarColor': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setStatusbarColor', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2643', 'SOURCE'),
    'GsContextUtils.showSnackBar(Activity,int,boolean)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name showSnackBar', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2539', 'SOURCE'),
    'GsContextUtils.showSnackBar(Activity,int,boolean,int,OnClickListener)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name showSnackBar', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2545', 'SOURCE'),
    'GsContextUtils.startCalendarApp': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name startCalendarApp', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2731', 'SOURCE'),
    'GsContextUtils.stopBlinking': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name stopBlinking', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2929', 'SOURCE'),
    'GsContextUtils.toggleStatusbarVisibility': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name toggleStatusbarVisibility', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2616', 'SOURCE'),
    'GsContextUtils.vibrate': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name vibrate', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:1057', 'SOURCE'),
    'GsContextUtils.windowAspectRatio': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name windowAspectRatio', 'src/main/java/net/gsantner/opoc/util/GsContextUtils.java:2778', 'SOURCE'),
    'GsCoolExperimentalStuff.<init>': ('no_trigger_in_app', 'class GsCoolExperimentalStuff is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/util/GsCoolExperimentalStuff.java:35', 'SOURCE'),
    'GsFileBrowserFragment.getOptions': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getOptions; the class extends library Fragment, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/filebrowser/GsFileBrowserFragment.java:606', 'INFERRED'),
    'GsFileBrowserFragment.onClicked': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name onClicked; the class extends library Fragment, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/filebrowser/GsFileBrowserFragment.java:159', 'INFERRED'),
    'GsFileBrowserListAdapter$1.<init>': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsFileBrowserListAdapter.doAfterChange)', 'src/main/java/net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java', 'INFERRED'),
    'GsFileBrowserListAdapter$1.onLayoutChange': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsFileBrowserListAdapter$1 or of a subclass', 'src/main/java/net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java:608', 'SOURCE'),
    'GsFileBrowserListAdapter.doAfterChange': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name doAfterChange', 'src/main/java/net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java:605', 'SOURCE'),
    'GsFileBrowserListAdapter.getFsOptions': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getFsOptions; the class extends library Filterable, RecyclerView$Adapter, View$OnClickListener, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java:808', 'INFERRED'),
    'GsFileBrowserListAdapter.getPathLevel': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getPathLevel', 'src/main/java/net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java:391', 'SOURCE'),
    'GsFileBrowserListAdapter.isCurrentFolderHome': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isCurrentFolderHome; the class extends library Filterable, RecyclerView$Adapter, View$OnClickListener, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java:812', 'INFERRED'),
    'GsFileBrowserListAdapter.toggleSelectionAll': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name toggleSelectionAll; the class extends library Filterable, RecyclerView$Adapter, View$OnClickListener, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/filebrowser/GsFileBrowserListAdapter.java:447', 'INFERRED'),
    'GsFileBrowserOptions.<init>': ('no_trigger_in_app', 'class GsFileBrowserOptions is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/frontend/filebrowser/GsFileBrowserOptions.java:31', 'SOURCE'),
    'GsFileUtils$1.<init>': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsFileUtils.searchFiles)', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java', 'INFERRED'),
    'GsFileUtils$1.visitFile': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsFileUtils$1 or of a subclass', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:1006', 'SOURCE'),
    'GsFileUtils.<init>': ('no_trigger_in_app', 'class GsFileUtils is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:72', 'SOURCE'),
    'GsFileUtils.copyFile(File,OutputStream)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name copyFile', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:307', 'SOURCE'),
    'GsFileUtils.crc32(byte[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name crc32', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:703', 'SOURCE'),
    'GsFileUtils.deleteRecursive': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsFileUtils.deleteRecursive)', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:357', 'INFERRED'),
    'GsFileUtils.fileContains': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name fileContains', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:335', 'SOURCE'),
    'GsFileUtils.getPrefix': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getPrefix', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:778', 'SOURCE'),
    'GsFileUtils.hasExtension': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name hasExtension', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:370', 'SOURCE'),
    'GsFileUtils.hash': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name hash', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:654', 'SOURCE'),
    'GsFileUtils.isUriOrFilePath': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isUriOrFilePath', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:933', 'SOURCE'),
    'GsFileUtils.join(File[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name join', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:642', 'SOURCE'),
    'GsFileUtils.readBinaryFile': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name readBinaryFile', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:195', 'SOURCE'),
    'GsFileUtils.readCloseBinaryStream(InputStream,int)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsFileUtils.readBinaryFile)', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:205', 'INFERRED'),
    'GsFileUtils.readCloseTextStream(InputStream)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsFileUtils.readTextFile, GsNetworkUtils.performCall(URL,String,String,HttpURLConnection))', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:157', 'INFERRED'),
    'GsFileUtils.readCloseTextStream(InputStream,boolean)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsFileUtils.readCloseTextStream(InputStream))', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:161', 'INFERRED'),
    'GsFileUtils.readTextFile': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name readTextFile', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:147', 'SOURCE'),
    'GsFileUtils.searchFiles': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (MarkorDialogFactory.lambda$showGlobFilesDialog$39)', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:997', 'INFERRED'),
    'GsFileUtils.writeFile(File,String,FileInfo)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name writeFile', 'src/main/java/net/gsantner/opoc/util/GsFileUtils.java:271', 'SOURCE'),
    'GsFontPreferenceCompat.<init>(Context)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/settings/GsFontPreferenceCompat.java:69', 'SOURCE'),
    'GsFontPreferenceCompat.<init>(Context,AttributeSet,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/settings/GsFontPreferenceCompat.java:80', 'SOURCE'),
    'GsFontPreferenceCompat.<init>(Context,AttributeSet,int,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/settings/GsFontPreferenceCompat.java:86', 'SOURCE'),
    'GsFontPreferenceCompat.getFontNames': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getFontNames; the class extends library ListPreference, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsFontPreferenceCompat.java:164', 'INFERRED'),
    'GsFontPreferenceCompat.getFontValues': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getFontValues; the class extends library ListPreference, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsFontPreferenceCompat.java:172', 'INFERRED'),
    'GsFontPreferenceCompat.loadFonts(Context)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name loadFonts', 'src/main/java/net/gsantner/opoc/frontend/settings/GsFontPreferenceCompat.java:91', 'SOURCE'),
    'GsFontPreferenceCompat.setFontNames': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setFontNames; the class extends library ListPreference, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsFontPreferenceCompat.java:168', 'INFERRED'),
    'GsFontPreferenceCompat.setFontValues': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setFontValues; the class extends library ListPreference, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsFontPreferenceCompat.java:176', 'INFERRED'),
    'GsFragmentBase.post': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name post; the class extends library Fragment, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/base/GsFragmentBase.java:142', 'INFERRED'),
    'GsHashMap.getOrDefault(Object)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getOrDefault', 'src/main/java/net/gsantner/opoc/wrapper/GsHashMap.java:41', 'SOURCE'),
    'GsHashMap.getOrDefault(Object,Object)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getOrDefault', 'src/main/java/net/gsantner/opoc/wrapper/GsHashMap.java:45', 'SOURCE'),
    'GsHashMap.keySet': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name keySet', 'src/main/java/net/gsantner/opoc/wrapper/GsHashMap.java:59', 'SOURCE'),
    'GsHashMap.limitSizeByRemovingOldest': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name limitSizeByRemovingOldest', 'src/main/java/net/gsantner/opoc/wrapper/GsHashMap.java:63', 'SOURCE'),
    'GsHashMap.withDefault': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsHashMap.getOrDefault(Object,Object))', 'src/main/java/net/gsantner/opoc/wrapper/GsHashMap.java:54', 'INFERRED'),
    'GsHorizontalScrollView.<init>(Context)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/GsHorizontalScrollView.java:14', 'SOURCE'),
    'GsHorizontalScrollView.<init>(Context,AttributeSet,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/GsHorizontalScrollView.java:22', 'SOURCE'),
    'GsHorizontalScrollView.<init>(Context,AttributeSet,int,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/GsHorizontalScrollView.java:27', 'SOURCE'),
    'GsLanguagePreferenceCompat.<init>(Context)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/settings/GsLanguagePreferenceCompat.java:76', 'SOURCE'),
    'GsLanguagePreferenceCompat.<init>(Context,AttributeSet,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/settings/GsLanguagePreferenceCompat.java:87', 'SOURCE'),
    'GsLanguagePreferenceCompat.<init>(Context,AttributeSet,int,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/settings/GsLanguagePreferenceCompat.java:93', 'SOURCE'),
    'GsLanguagePreferenceCompat.getDefaultLanguageCode': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getDefaultLanguageCode; the class extends library ListPreference, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsLanguagePreferenceCompat.java:192', 'INFERRED'),
    'GsLanguagePreferenceCompat.getSystemLanguageName': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getSystemLanguageName; the class extends library ListPreference, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsLanguagePreferenceCompat.java:183', 'INFERRED'),
    'GsLanguagePreferenceCompat.loadLangs(Context)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsLanguagePreferenceCompat.setDefaultLanguageCode, GsLanguagePreferenceCompat.setSystemLanguageName)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsLanguagePreferenceCompat.java:108', 'INFERRED'),
    'GsLanguagePreferenceCompat.setDefaultLanguageCode': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setDefaultLanguageCode; the class extends library ListPreference, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsLanguagePreferenceCompat.java:196', 'INFERRED'),
    'GsLanguagePreferenceCompat.setSystemLanguageName': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setSystemLanguageName; the class extends library ListPreference, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsLanguagePreferenceCompat.java:187', 'INFERRED'),
    'GsLinearSplitLayout.<init>(Context)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/GsLinearSplitLayout.java:46', 'SOURCE'),
    'GsLinearSplitLayout.<init>(Context,AttributeSet,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/GsLinearSplitLayout.java:54', 'SOURCE'),
    'GsLinearSplitLayout.<init>(Context,AttributeSet,int,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/GsLinearSplitLayout.java:59', 'SOURCE'),
    'GsMapPropertyBackend.<init>': ('no_trigger_in_app', 'class GsMapPropertyBackend is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:28', 'SOURCE'),
    'GsMapPropertyBackend.getBool': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:48', 'SOURCE'),
    'GsMapPropertyBackend.getDouble': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:58', 'SOURCE'),
    'GsMapPropertyBackend.getFloat': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:53', 'SOURCE'),
    'GsMapPropertyBackend.getInt': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:38', 'SOURCE'),
    'GsMapPropertyBackend.getIntList': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:63', 'SOURCE'),
    'GsMapPropertyBackend.getLong': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:43', 'SOURCE'),
    'GsMapPropertyBackend.getString': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:33', 'SOURCE'),
    'GsMapPropertyBackend.getStringList': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:68', 'SOURCE'),
    'GsMapPropertyBackend.setBool': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:91', 'SOURCE'),
    'GsMapPropertyBackend.setDouble': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:103', 'SOURCE'),
    'GsMapPropertyBackend.setFloat': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:97', 'SOURCE'),
    'GsMapPropertyBackend.setInt': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:79', 'SOURCE'),
    'GsMapPropertyBackend.setIntList': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:109', 'SOURCE'),
    'GsMapPropertyBackend.setLong': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:85', 'SOURCE'),
    'GsMapPropertyBackend.setString': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:73', 'SOURCE'),
    'GsMapPropertyBackend.setStringList': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsMapPropertyBackend or of a subclass', 'src/main/java/net/gsantner/opoc/model/GsMapPropertyBackend.java:115', 'SOURCE'),
    'GsMenuItemDummy$Menu.addIntentOptions': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name addIntentOptions, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:276', 'INFERRED'),
    'GsMenuItemDummy$Menu.addSubMenu(CharSequence)': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name addSubMenu, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:256', 'INFERRED'),
    'GsMenuItemDummy$Menu.addSubMenu(int)': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name addSubMenu, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:256', 'INFERRED'),
    'GsMenuItemDummy$Menu.addSubMenu(int,int,int,CharSequence)': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name addSubMenu, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:266', 'INFERRED'),
    'GsMenuItemDummy$Menu.addSubMenu(int,int,int,int)': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name addSubMenu, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:271', 'INFERRED'),
    'GsMenuItemDummy$Menu.hasVisibleItems': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name hasVisibleItems, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:305', 'INFERRED'),
    'GsMenuItemDummy$Menu.isShortcutKey': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name isShortcutKey, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:334', 'INFERRED'),
    'GsMenuItemDummy$Menu.performShortcut': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name performShortcut, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:329', 'INFERRED'),
    'GsMenuItemDummy$Menu.removeGroup': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name removeGroup, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:285', 'INFERRED'),
    'GsMenuItemDummy$Menu.removeItem': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name removeItem, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:281', 'INFERRED'),
    'GsMenuItemDummy$Menu.setGroupCheckable': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name setGroupCheckable, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:293', 'INFERRED'),
    'GsMenuItemDummy$Menu.setGroupEnabled': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name setGroupEnabled, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:301', 'INFERRED'),
    'GsMenuItemDummy$Menu.setGroupVisible': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name setGroupVisible, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:297', 'INFERRED'),
    'GsMenuItemDummy$Menu.setQwertyMode': ('no_trigger_in_app', 'placeholder for library Menu; the app text never uses the name setQwertyMode, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:344', 'INFERRED'),
    'GsMenuItemDummy.collapseActionView': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name collapseActionView, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:219', 'INFERRED'),
    'GsMenuItemDummy.expandActionView': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name expandActionView, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:214', 'INFERRED'),
    'GsMenuItemDummy.getActionProvider': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name getActionProvider, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:209', 'INFERRED'),
    'GsMenuItemDummy.getAlphabeticShortcut': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name getAlphabeticShortcut, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:115', 'INFERRED'),
    'GsMenuItemDummy.getGroupId': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name getGroupId, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:35', 'INFERRED'),
    'GsMenuItemDummy.getMenuInfo': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name getMenuInfo, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:175', 'INFERRED'),
    'GsMenuItemDummy.getNumericShortcut': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name getNumericShortcut, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:105', 'INFERRED'),
    'GsMenuItemDummy.getOrder': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name getOrder, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:40', 'INFERRED'),
    'GsMenuItemDummy.getTitleCondensed': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name getTitleCondensed, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:65', 'INFERRED'),
    'GsMenuItemDummy.isActionViewExpanded': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name isActionViewExpanded, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:224', 'INFERRED'),
    'GsMenuItemDummy.isCheckable': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name isCheckable, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:125', 'INFERRED'),
    'GsMenuItemDummy.setActionProvider': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setActionProvider, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:204', 'INFERRED'),
    'GsMenuItemDummy.setActionView(View)': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setActionView, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:189', 'INFERRED'),
    'GsMenuItemDummy.setActionView(int)': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setActionView, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:194', 'INFERRED'),
    'GsMenuItemDummy.setAlphabeticShortcut': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setAlphabeticShortcut, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:110', 'INFERRED'),
    'GsMenuItemDummy.setCheckable': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setCheckable, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:120', 'INFERRED'),
    'GsMenuItemDummy.setNumericShortcut': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setNumericShortcut, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:100', 'INFERRED'),
    'GsMenuItemDummy.setOnActionExpandListener': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setOnActionExpandListener, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:229', 'INFERRED'),
    'GsMenuItemDummy.setOnMenuItemClickListener': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setOnMenuItemClickListener, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:170', 'INFERRED'),
    'GsMenuItemDummy.setShortcut': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setShortcut, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:95', 'INFERRED'),
    'GsMenuItemDummy.setShowAsAction': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setShowAsAction, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:180', 'INFERRED'),
    'GsMenuItemDummy.setShowAsActionFlags': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setShowAsActionFlags, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:184', 'INFERRED'),
    'GsMenuItemDummy.setTitleCondensed': ('no_trigger_in_app', 'placeholder for library MenuItem; the app text never uses the name setTitleCondensed, so no app code calls it through the placeholder (library source not read)', 'src/main/java/net/gsantner/opoc/wrapper/GsMenuItemDummy.java:60', 'INFERRED'),
    'GsNanoProfiler.<clinit>': ('no_trigger_in_app', 'the class GsNanoProfiler is named only in its own file (no other app .java/.kt/.xml file uses it), so no code runs its static initializer', 'src/main/java/net/gsantner/opoc/util/GsNanoProfiler.java', 'SOURCE'),
    'GsNanoProfiler.<init>': ('no_trigger_in_app', 'class GsNanoProfiler is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/util/GsNanoProfiler.java:19', 'SOURCE'),
    'GsNanoProfiler.end': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNanoProfiler.restart)', 'src/main/java/net/gsantner/opoc/util/GsNanoProfiler.java:64', 'INFERRED'),
    'GsNanoProfiler.printProfilingGroup': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsNanoProfiler or of a subclass', 'src/main/java/net/gsantner/opoc/util/GsNanoProfiler.java:55', 'SOURCE'),
    'GsNanoProfiler.resetDebugText': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsNanoProfiler or of a subclass', 'src/main/java/net/gsantner/opoc/util/GsNanoProfiler.java:33', 'SOURCE'),
    'GsNanoProfiler.restart': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsNanoProfiler or of a subclass', 'src/main/java/net/gsantner/opoc/util/GsNanoProfiler.java:50', 'SOURCE'),
    'GsNanoProfiler.setEnabled': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsNanoProfiler or of a subclass', 'src/main/java/net/gsantner/opoc/util/GsNanoProfiler.java:28', 'SOURCE'),
    'GsNanoProfiler.start': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNanoProfiler.restart)', 'src/main/java/net/gsantner/opoc/util/GsNanoProfiler.java:39', 'INFERRED'),
    'GsNetworkUtils.<init>': ('no_trigger_in_app', 'class GsNetworkUtils is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:33', 'SOURCE'),
    'GsNetworkUtils.downloadFile(String,File)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name downloadFile', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:43', 'SOURCE'),
    'GsNetworkUtils.downloadFile(String,File,a1)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNetworkUtils.downloadFile(String,File))', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:47', 'INFERRED'),
    'GsNetworkUtils.downloadFile(URL,File,HttpURLConnection,a1)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNetworkUtils.downloadFile(URL,File,a1))', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:61', 'INFERRED'),
    'GsNetworkUtils.downloadFile(URL,File,a1)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNetworkUtils.downloadFile(String,File,a1))', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:57', 'INFERRED'),
    'GsNetworkUtils.encodeQuery': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNetworkUtils.performCall(String,String,HashMap))', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:181', 'INFERRED'),
    'GsNetworkUtils.getDataMap': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getDataMap', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:196', 'SOURCE'),
    'GsNetworkUtils.httpGetAsync': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name httpGetAsync', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:227', 'SOURCE'),
    'GsNetworkUtils.lambda$httpGetAsync$0': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNetworkUtils.httpGetAsync)', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:227', 'INFERRED'),
    'GsNetworkUtils.performCall(String,JSONObject)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name performCall', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:138', 'SOURCE'),
    'GsNetworkUtils.performCall(String,String)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNetworkUtils.lambda$httpGetAsync$0)', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:109', 'INFERRED'),
    'GsNetworkUtils.performCall(String,String,HashMap)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name performCall', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:128', 'SOURCE'),
    'GsNetworkUtils.performCall(String,String,JSONObject)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNetworkUtils.performCall(String,JSONObject))', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:142', 'INFERRED'),
    'GsNetworkUtils.performCall(String,String,String)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name performCall', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:118', 'SOURCE'),
    'GsNetworkUtils.performCall(URL,String,String)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNetworkUtils.performCall(String,String), GsNetworkUtils.performCall(String,String,HashMap), GsNetworkUtils.performCall(String,String,JSONObject))', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:151', 'INFERRED'),
    'GsNetworkUtils.performCall(URL,String,String,HttpURLConnection)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsNetworkUtils.performCall(URL,String,String))', 'src/main/java/net/gsantner/opoc/web/GsNetworkUtils.java:156', 'INFERRED'),
    'GsPermissionChecker.<init>': ('no_trigger_in_app', 'class GsPermissionChecker is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsPermissionChecker.java:20', 'SOURCE'),
    'GsPermissionChecker.checkPermissionResult': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsPermissionChecker or of a subclass', 'src/main/java/net/gsantner/opoc/frontend/settings/GsPermissionChecker.java:41', 'SOURCE'),
    'GsPermissionChecker.doIfExtStoragePermissionGranted()': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsPermissionChecker.mkdirIfStoragePermissionGranted)', 'src/main/java/net/gsantner/opoc/frontend/settings/GsPermissionChecker.java:29', 'INFERRED'),
    'GsPermissionChecker.doIfExtStoragePermissionGranted(String)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsPermissionChecker.doIfExtStoragePermissionGranted())', 'src/main/java/net/gsantner/opoc/frontend/settings/GsPermissionChecker.java:33', 'INFERRED'),
    'GsPermissionChecker.mkdirIfStoragePermissionGranted': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsPermissionChecker or of a subclass', 'src/main/java/net/gsantner/opoc/frontend/settings/GsPermissionChecker.java:54', 'SOURCE'),
    'GsPreferenceFragmentBase$DividerDecoration.<init>(Context,b1)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/opoc/frontend/base/GsPreferenceFragmentBase.java:599', 'SOURCE'),
    'GsPreferenceFragmentBase.eq(Preference,int[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name eq; the class extends library PreferenceFragmentCompat, PreferenceFragmentCompat$OnPreferenceStartScreenCallback, SharedPreferences$OnSharedPreferenceChangeListener, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/base/GsPreferenceFragmentBase.java:478', 'INFERRED'),
    'GsPreferenceFragmentBase.getPreferenceParent': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsPreferenceFragmentBase.getPreferenceParent, GsPreferenceFragmentBase.removePreference)', 'src/main/java/net/gsantner/opoc/frontend/base/GsPreferenceFragmentBase.java:447', 'INFERRED'),
    'GsPreferenceFragmentBase.keyToStringResId(String)': ('no_trigger_in_app', "no caller of this String overload: the app's only call to keyToStringResId (GsPreferenceFragmentBase.java:320) passes a Preference and binds to keyToStringResId(Preference) at line 215; no method reference and no XML handler uses this overload (the library ancestors do not declare a method of this name)", 'src/main/java/net/gsantner/opoc/frontend/base/GsPreferenceFragmentBase.java:226', 'SOURCE'),
    'GsPreferenceFragmentBase.removePreference': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name removePreference; the class extends library PreferenceFragmentCompat, PreferenceFragmentCompat$OnPreferenceStartScreenCallback, SharedPreferences$OnSharedPreferenceChangeListener, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/base/GsPreferenceFragmentBase.java:422', 'INFERRED'),
    'GsPreferenceFragmentBase.restartActivity': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name restartActivity; the class extends library PreferenceFragmentCompat, PreferenceFragmentCompat$OnPreferenceStartScreenCallback, SharedPreferences$OnSharedPreferenceChangeListener, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/base/GsPreferenceFragmentBase.java:508', 'INFERRED'),
    'GsPreferenceFragmentBase.setDialogMessage': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setDialogMessage; the class extends library PreferenceFragmentCompat, PreferenceFragmentCompat$OnPreferenceStartScreenCallback, SharedPreferences$OnSharedPreferenceChangeListener, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/opoc/frontend/base/GsPreferenceFragmentBase.java:362', 'INFERRED'),
    'GsSearchOrCustomTextDialog.<init>': ('no_trigger_in_app', 'class GsSearchOrCustomTextDialog is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/frontend/GsSearchOrCustomTextDialog.java:80', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.afterDaysTrue': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name afterDaysTrue', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:590', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.contains': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.afterDaysTrue)', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:559', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.didDaysPassedSince': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.afterDaysTrue)', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:583', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getColor(String,int,SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.getColor(int,int,SharedPreferences[]))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:456', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getColor(int,int,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getColor', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:456', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getDateOfDaysAgo': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.afterDaysTrue, GsSharedPreferencesPropertyBackend.didDaysPassedSince)', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:574', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getDefaultPreferences': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getDefaultPreferences', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:122', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getDefaultPreferencesEditor': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getDefaultPreferencesEditor', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:126', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getDefaultPreferencesName': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getDefaultPreferencesName', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:130', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getDouble(String,double)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getDouble', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:410', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getDouble(String,double,SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.getDouble(String,double), GsSharedPreferencesPropertyBackend.getDouble(int,double,SharedPreferences[]))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:410', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getDouble(int,double,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getDouble', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:410', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getFloat(String,float)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.getFloat(int,float,SharedPreferences[]))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:387', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getFloat(String,float,SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.getFloat(String,float))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:387', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getFloat(int,float,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getFloat', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:387', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getIntArray(String,SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.getIntArray(int,SharedPreferences[]))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:326', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getIntArray(int,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getIntArray', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:326', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getIntList(String)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getIntList', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:344', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getIntList(String,SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.getIntList(String))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:344', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getIntList(int,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getIntList', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:344', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getIntListOne': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.getIntArray(String,SharedPreferences[]), GsSharedPreferencesPropertyBackend.getIntList(String,SharedPreferences[]), GsSharedPreferencesPropertyBackend.getIntList(int,SharedPreferences[]))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:306', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getLong(String,long)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.afterDaysTrue)', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:364', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getLong(String,long,SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.getDouble(String,double,SharedPreferences[]), GsSharedPreferencesPropertyBackend.getLong(String,long), GsSharedPreferencesPropertyBackend.getLong(int,long,SharedPreferences[]))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:364', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getLong(int,long,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getLong', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:364', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getString(int,String,int,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getString', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:206', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getString(int,int,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getString', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:190', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.getStringArray(String,SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.getStringArray(int,SharedPreferences[]))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:246', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.getStringArray(int,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getStringArray', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:246', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.isKeyEqual': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isKeyEqual', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:85', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.isPrefSet(SharedPreferences,int)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.isPrefSet(int))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:102', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.isPrefSet(int)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isPrefSet', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:98', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.registerPreferenceChangedListener(OnSharedPreferenceChangeListener)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name registerPreferenceChangedListener', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:106', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.remove(int,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name remove', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:563', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.resetSettings()': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name resetSettings', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:89', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.resetSettings(SharedPreferences)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.resetSettings())', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:94', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.rstrs': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name rstrs', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:166', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setDouble(String,double)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setDouble', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:402', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setDouble(String,double,SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.setDouble(String,double))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:402', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.setDouble(int,double,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setDouble', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:402', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setFloat(String,float)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setFloat', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:379', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setFloat(String,float,SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.setFloat(String,float))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:379', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.setFloat(int,float,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setFloat', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:379', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setIntArray(String,Integer[],SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.setIntArray(int,Integer[],SharedPreferences[]))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:318', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.setIntArray(int,Integer[],SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setIntArray', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:318', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setIntList(String,List)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setIntList', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:336', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setIntList(String,List,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setIntList', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:336', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setIntList(int,List,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setIntList', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:336', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setIntListOne': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.setIntArray(String,Integer[],SharedPreferences[]), GsSharedPreferencesPropertyBackend.setIntList(String,List), GsSharedPreferencesPropertyBackend.setIntList(String,List,SharedPreferences[]))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:297', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.setLong(String,long)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.afterDaysTrue, GsSharedPreferencesPropertyBackend.setDouble(String,double,SharedPreferences[]), GsSharedPreferencesPropertyBackend.setDouble(int,double,SharedPreferences[]))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:356', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.setLong(String,long,SharedPreferences[])': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSharedPreferencesPropertyBackend.setLong(String,long))', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:356', 'INFERRED'),
    'GsSharedPreferencesPropertyBackend.setLong(int,long,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setLong', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:356', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setString(int,int,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setString', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:178', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setStringArray(int,String[],SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setStringArray', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:229', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.setStringList(String,List,SharedPreferences[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setStringList', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:237', 'SOURCE'),
    'GsSharedPreferencesPropertyBackend.unregisterPreferenceChangedListener(OnSharedPreferenceChangeListener)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name unregisterPreferenceChangedListener', 'src/main/java/net/gsantner/opoc/model/GsSharedPreferencesPropertyBackend.java:114', 'SOURCE'),
    'GsSimpleMarkdownParser.parse(String,SmpFilter[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name parse', 'src/main/java/net/gsantner/opoc/format/GsSimpleMarkdownParser.java:178', 'SOURCE'),
    'GsSimpleMarkdownParser.removeMultiNewlines': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsContextUtils.loadMarkdownForTextViewFromRaw)', 'src/main/java/net/gsantner/opoc/format/GsSimpleMarkdownParser.java:229', 'INFERRED'),
    'GsSimpleMarkdownParser.replaceBulletCharacter': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsContextUtils.loadMarkdownForTextViewFromRaw)', 'src/main/java/net/gsantner/opoc/format/GsSimpleMarkdownParser.java:234', 'INFERRED'),
    'GsSimpleMarkdownParser.replaceColor': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsContextUtils.loadMarkdownForTextViewFromRaw)', 'src/main/java/net/gsantner/opoc/format/GsSimpleMarkdownParser.java:239', 'INFERRED'),
    'GsSimpleMarkdownParser.setHtml': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setHtml', 'src/main/java/net/gsantner/opoc/format/GsSimpleMarkdownParser.java:224', 'SOURCE'),
    'GsSimplePlaylistParser.parse(File)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name parse', 'src/main/java/net/gsantner/opoc/format/GsSimplePlaylistParser.java:48', 'SOURCE'),
    'GsSimplePlaylistParser.parse(InputStream)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsSimplePlaylistParser.parse(File))', 'src/main/java/net/gsantner/opoc/format/GsSimplePlaylistParser.java:57', 'INFERRED'),
    'GsTextUtils.<init>': ('no_trigger_in_app', 'class GsTextUtils is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/opoc/format/GsTextUtils.java:36', 'SOURCE'),
    'GsTextUtils.countChar(CharSequence,char)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name countChar', 'src/main/java/net/gsantner/opoc/format/GsTextUtils.java:427', 'SOURCE'),
    'GsTextUtils.countChars(CharSequence,char[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name countChars', 'src/main/java/net/gsantner/opoc/format/GsTextUtils.java:394', 'SOURCE'),
    'GsTextUtils.countSubstrings': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name countSubstrings', 'src/main/java/net/gsantner/opoc/format/GsTextUtils.java:324', 'SOURCE'),
    'GsTextUtils.fromBase64': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (GsTextUtils.fromBase64ToString)', 'src/main/java/net/gsantner/opoc/format/GsTextUtils.java:216', 'INFERRED'),
    'GsTextUtils.fromBase64ToString': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name fromBase64ToString', 'src/main/java/net/gsantner/opoc/format/GsTextUtils.java:220', 'SOURCE'),
    'GsTextUtils.newHuuid': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name newHuuid', 'src/main/java/net/gsantner/opoc/format/GsTextUtils.java:164', 'SOURCE'),
    'GsTextUtils.padLeft': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name padLeft', 'src/main/java/net/gsantner/opoc/format/GsTextUtils.java:342', 'SOURCE'),
    'GsTextUtils.removeLinesOfTextAround': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name removeLinesOfTextAround', 'src/main/java/net/gsantner/opoc/format/GsTextUtils.java:142', 'SOURCE'),
    'GsTextUtils.toArrayList': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name toArrayList', 'src/main/java/net/gsantner/opoc/format/GsTextUtils.java:236', 'SOURCE'),
    'GsTextWatcherAdapter$1.<init>': ('no_trigger_in_app', 'created only inside GsTextWatcherAdapter.before, which has no caller', 'src/main/java/net/gsantner/opoc/wrapper/GsTextWatcherAdapter.java:29', 'SOURCE'),
    'GsTextWatcherAdapter$1.beforeTextChanged': ('no_trigger_in_app', 'no bytecode caller; no reached code creates an object of GsTextWatcherAdapter$1 or of a subclass', 'src/main/java/net/gsantner/opoc/wrapper/GsTextWatcherAdapter.java:18', 'SOURCE'),
    'GsTextWatcherAdapter.before': ('no_trigger_in_app', 'no caller in the app or thirdparty source: grep for GsTextWatcherAdapter.before( and GsTextWatcherAdapter::before finds none; the other two factories (on, after) are used', 'src/main/java/net/gsantner/opoc/wrapper/GsTextWatcherAdapter.java:29', 'SOURCE'),
    'HighlightingEditor.getHighlighter': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getHighlighter; the class extends library AppCompatEditText, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/frontend/textview/HighlightingEditor.java:253', 'INFERRED'),
    'HighlightingEditor.setTextSize': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setTextSize; the class extends library AppCompatEditText, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/frontend/textview/HighlightingEditor.java:374', 'INFERRED'),
    'LineNumbersView.<init>(Context)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/markor/frontend/textview/LineNumbersView.java:22', 'SOURCE'),
    'LineNumbersView.<init>(Context,AttributeSet,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/markor/frontend/textview/LineNumbersView.java:30', 'SOURCE'),
    'MainActivity.getPosTitle': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getPosTitle; the class extends library AppCompatActivity, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/activity/MainActivity.java:407', 'INFERRED'),
    'MarkdownReplacePatternGenerator.<init>': ('no_trigger_in_app', 'class MarkdownReplacePatternGenerator is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/format/markdown/MarkdownReplacePatternGenerator.java:19', 'SOURCE'),
    'MarkorDialogFactory.<init>': ('no_trigger_in_app', 'class MarkorDialogFactory is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:83', 'SOURCE'),
    'MarkorDialogFactory.lambda$showColorSelectionModeDialog$28': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (MarkorDialogFactory.showColorSelectionModeDialog)', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:484', 'INFERRED'),
    'MarkorDialogFactory.lambda$showGlobFilesDialog$37': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (MarkorDialogFactory.lambda$showGlobFilesDialog$39)', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:698', 'INFERRED'),
    'MarkorDialogFactory.lambda$showGlobFilesDialog$38': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (MarkorDialogFactory.lambda$showGlobFilesDialog$39)', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:698', 'INFERRED'),
    'MarkorDialogFactory.lambda$showGlobFilesDialog$39': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (MarkorDialogFactory.showGlobFilesDialog)', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:698', 'INFERRED'),
    'MarkorDialogFactory.lambda$showInsertItemsDialog$32': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (MarkorDialogFactory.showInsertItemsDialog)', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:584', 'INFERRED'),
    'MarkorDialogFactory.lambda$showInsertItemsDialog$33': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (MarkorDialogFactory.showInsertItemsDialog)', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:584', 'INFERRED'),
    'MarkorDialogFactory.lambda$showInsertItemsDialog$34': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (MarkorDialogFactory.showInsertItemsDialog)', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:584', 'INFERRED'),
    'MarkorDialogFactory.showColorSelectionModeDialog': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name showColorSelectionModeDialog', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:484', 'SOURCE'),
    'MarkorDialogFactory.showGlobFilesDialog': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (MarkorDialogFactory.lambda$showGlobFilesDialog$38)', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:698', 'INFERRED'),
    'MarkorDialogFactory.showInsertItemsDialog': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name showInsertItemsDialog', 'src/main/java/net/gsantner/markor/frontend/MarkorDialogFactory.java:584', 'SOURCE'),
    'MarkorFileBrowserFactory.<init>': ('no_trigger_in_app', 'class MarkorFileBrowserFactory is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/frontend/filebrowser/MarkorFileBrowserFactory.java:26', 'SOURCE'),
    'MoreInfoFragment.getFragmentTag': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getFragmentTag; the class extends library PreferenceFragmentCompat, PreferenceFragmentCompat$OnPreferenceStartScreenCallback, SharedPreferences$OnSharedPreferenceChangeListener, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/activity/MoreInfoFragment.java:42', 'INFERRED'),
    'NewFileDialog$ReselectSpinner.<init>(Context)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/markor/frontend/NewFileDialog.java:407', 'SOURCE'),
    'NewFileDialog$ReselectSpinner.<init>(Context,AttributeSet,int)': ('no_trigger_in_app', 'no bytecode call creates an object with this constructor (no caller in the call table); the layout and preference inflaters use the (Context, AttributeSet) constructor only', 'src/main/java/net/gsantner/markor/frontend/NewFileDialog.java:415', 'SOURCE'),
    'OpenEditorActivity.<init>': ('closed_by_configuration', 'in the openeditor launcher group: the manifest entry is android:enabled=false (AndroidManifest.xml 140-180) and only MarkorContextUtils.java:45-51 enables it, when isSpecialFileLaunchersEnabled() is true; it is false in this test build (AppSettings.java:254-258, BuildConfig.IS_TEST_BUILD)', 'src/main/java/net/gsantner/markor/activity/openeditor/OpenEditorActivity.java', 'SOURCE'),
    'OpenEditorActivity.onCreate': ('closed_by_configuration', 'in the openeditor launcher group: the manifest entry is android:enabled=false (AndroidManifest.xml 140-180) and only MarkorContextUtils.java:45-51 enables it, when isSpecialFileLaunchersEnabled() is true; it is false in this test build (AppSettings.java:254-258, BuildConfig.IS_TEST_BUILD)', 'src/main/java/net/gsantner/markor/activity/openeditor/OpenEditorActivity.java:24', 'SOURCE'),
    'OpenEditorActivity.openEditorForFile': ('closed_by_configuration', 'in the openeditor launcher group: the manifest entry is android:enabled=false (AndroidManifest.xml 140-180) and only MarkorContextUtils.java:45-51 enables it, when isSpecialFileLaunchersEnabled() is true; it is false in this test build (AppSettings.java:254-258, BuildConfig.IS_TEST_BUILD)', 'src/main/java/net/gsantner/markor/activity/openeditor/OpenEditorActivity.java:29', 'SOURCE'),
    'OpenEditorQuickNoteActivity.<init>': ('closed_by_configuration', 'in the openeditor launcher group: the manifest entry is android:enabled=false (AndroidManifest.xml 140-180) and only MarkorContextUtils.java:45-51 enables it, when isSpecialFileLaunchersEnabled() is true; it is false in this test build (AppSettings.java:254-258, BuildConfig.IS_TEST_BUILD)', 'src/main/java/net/gsantner/markor/activity/openeditor/OpenEditorQuickNoteActivity.java', 'SOURCE'),
    'OpenEditorQuickNoteActivity.onCreate': ('closed_by_configuration', 'in the openeditor launcher group: the manifest entry is android:enabled=false (AndroidManifest.xml 140-180) and only MarkorContextUtils.java:45-51 enables it, when isSpecialFileLaunchersEnabled() is true; it is false in this test build (AppSettings.java:254-258, BuildConfig.IS_TEST_BUILD)', 'src/main/java/net/gsantner/markor/activity/openeditor/OpenEditorQuickNoteActivity.java:17', 'SOURCE'),
    'OpenEditorTodoActivity.<init>': ('closed_by_configuration', 'in the openeditor launcher group: the manifest entry is android:enabled=false (AndroidManifest.xml 140-180) and only MarkorContextUtils.java:45-51 enables it, when isSpecialFileLaunchersEnabled() is true; it is false in this test build (AppSettings.java:254-258, BuildConfig.IS_TEST_BUILD)', 'src/main/java/net/gsantner/markor/activity/openeditor/OpenEditorTodoActivity.java', 'SOURCE'),
    'OpenEditorTodoActivity.onCreate': ('closed_by_configuration', 'in the openeditor launcher group: the manifest entry is android:enabled=false (AndroidManifest.xml 140-180) and only MarkorContextUtils.java:45-51 enables it, when isSpecialFileLaunchersEnabled() is true; it is false in this test build (AppSettings.java:254-258, BuildConfig.IS_TEST_BUILD)', 'src/main/java/net/gsantner/markor/activity/openeditor/OpenEditorTodoActivity.java:17', 'SOURCE'),
    'OpenShareIntoActivity.<init>': ('closed_by_configuration', 'in the openeditor launcher group: the manifest entry is android:enabled=false (AndroidManifest.xml 140-180) and only MarkorContextUtils.java:45-51 enables it, when isSpecialFileLaunchersEnabled() is true; it is false in this test build (AppSettings.java:254-258, BuildConfig.IS_TEST_BUILD)', 'src/main/java/net/gsantner/markor/activity/openeditor/OpenShareIntoActivity.java', 'SOURCE'),
    'OpenShareIntoActivity.onCreate': ('closed_by_configuration', 'in the openeditor launcher group: the manifest entry is android:enabled=false (AndroidManifest.xml 140-180) and only MarkorContextUtils.java:45-51 enables it, when isSpecialFileLaunchersEnabled() is true; it is false in this test build (AppSettings.java:254-258, BuildConfig.IS_TEST_BUILD)', 'src/main/java/net/gsantner/markor/activity/openeditor/OpenShareIntoActivity.java:18', 'SOURCE'),
    'OrgmodeReplacePatternGenerator.<init>': ('no_trigger_in_app', 'class OrgmodeReplacePatternGenerator is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/format/orgmode/OrgmodeReplacePatternGenerator.java:18', 'SOURCE'),
    'ReplacePatternGeneratorHelper.<init>': ('no_trigger_in_app', 'class ReplacePatternGeneratorHelper is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/frontend/textview/ReplacePatternGeneratorHelper.java:16', 'SOURCE'),
    'SearchAndReplaceTextDialog.showSearchReplaceDialog(Activity,Editable,int[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name showSearchReplaceDialog', 'src/main/java/net/gsantner/markor/frontend/SearchAndReplaceTextDialog.java:82', 'SOURCE'),
    'Selection.getLength': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getLength', 'src/main/java/net/gsantner/markor/frontend/textsearch/Selection.java:33', 'SOURCE'),
    'SettingsActivity$RESULT.<init>': ('no_trigger_in_app', 'class SettingsActivity$RESULT is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/activity/SettingsActivity.java:53', 'SOURCE'),
    'SettingsActivity$SettingsFragmentMaster.getFragmentTag': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getFragmentTag; the class extends library PreferenceFragmentCompat, PreferenceFragmentCompat$OnPreferenceStartScreenCallback, SharedPreferences$OnSharedPreferenceChangeListener, which could call a method of this name (library source not read)', 'src/main/java/net/gsantner/markor/activity/SettingsActivity.java:152', 'INFERRED'),
    'ShortcutUtils.<init>': ('no_trigger_in_app', 'class ShortcutUtils is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/util/ShortcutUtils.java:33', 'SOURCE'),
    'StoragePermissionActivity.onActivityResult': ('closed_by_api_level', 'Activity result hook: it runs only after startActivityForResult from this activity; on API 27 GsContextUtils.requestExternalStoragePermission only calls ActivityCompat.requestPermissions (the startActivityForResult calls are in the API 30+ branch)', 'src/main/java/net/gsantner/markor/activity/StoragePermissionActivity.java:70-73', 'SOURCE'),
    'Syntax$Rule.<init>': ('no_trigger_in_app', 'class Syntax$Rule is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/format/plaintext/highlight/Syntax.java:11', 'SOURCE'),
    'Syntax.<init>': ('no_trigger_in_app', 'class Syntax is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/format/plaintext/highlight/Syntax.java:7', 'SOURCE'),
    'SyntaxHighlighterBase.getDefaultHighlighter': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getDefaultHighlighter', 'src/main/java/net/gsantner/markor/frontend/textview/SyntaxHighlighterBase.java:104', 'SOURCE'),
    'SyntaxHighlighterBase.getSpannable': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getSpannable', 'src/main/java/net/gsantner/markor/frontend/textview/SyntaxHighlighterBase.java:273', 'SOURCE'),
    'TextCasingUtils.<init>': ('no_trigger_in_app', 'class TextCasingUtils is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/util/TextCasingUtils.java:3', 'SOURCE'),
    'TextViewUndoRedo$EditHistory.setMaxHistorySize': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (TextViewUndoRedo.setMaxHistorySize)', 'src/main/java/net/gsantner/opoc/frontend/textview/TextViewUndoRedo.java:127', 'INFERRED'),
    'TextViewUndoRedo.doRestorePersistentState': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (TextViewUndoRedo.restorePersistentState)', 'src/main/java/net/gsantner/opoc/frontend/textview/TextViewUndoRedo.java:257', 'INFERRED'),
    'TextViewUndoRedo.restorePersistentState': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name restorePersistentState', 'src/main/java/net/gsantner/opoc/frontend/textview/TextViewUndoRedo.java:246', 'SOURCE'),
    'TextViewUndoRedo.setMaxHistorySize': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setMaxHistorySize', 'src/main/java/net/gsantner/opoc/frontend/textview/TextViewUndoRedo.java:127', 'SOURCE'),
    'TextViewUndoRedo.storePersistentState': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name storePersistentState', 'src/main/java/net/gsantner/opoc/frontend/textview/TextViewUndoRedo.java:218', 'SOURCE'),
    'TextViewUndoRedo.undoRedoPrefKeyForFile': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name undoRedoPrefKeyForFile', 'src/main/java/net/gsantner/opoc/frontend/textview/TextViewUndoRedo.java:100', 'SOURCE'),
    'TextViewUtils.<init>': ('no_trigger_in_app', 'class TextViewUtils is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/frontend/textview/TextViewUtils.java:48', 'SOURCE'),
    'TextViewUtils.isViewVisible': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isViewVisible', 'src/main/java/net/gsantner/markor/frontend/textview/TextViewUtils.java:777', 'SOURCE'),
    'TodoTxtFilter.<init>': ('no_trigger_in_app', 'class TodoTxtFilter is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/format/todotxt/TodoTxtFilter.java:28', 'SOURCE'),
    'TodoTxtTask$SttTaskSimpleComparator.compare(String[],String[])': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name compare', 'src/main/java/net/gsantner/markor/format/todotxt/TodoTxtTask.java:366', 'SOURCE'),
    'TodoTxtTask$SttTaskSimpleComparator.compareDone': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name compareDone', 'src/main/java/net/gsantner/markor/format/todotxt/TodoTxtTask.java:358', 'SOURCE'),
    'TodoTxtTask.getCompletionDate()': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getCompletionDate', 'src/main/java/net/gsantner/markor/format/todotxt/TodoTxtTask.java:234', 'SOURCE'),
    'TodoTxtTask.getCompletionDate(String)': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (TodoTxtTask.getCompletionDate())', 'src/main/java/net/gsantner/markor/format/todotxt/TodoTxtTask.java:238', 'INFERRED'),
    'TodoTxtTask.getDueStates': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getDueStates', 'src/main/java/net/gsantner/markor/format/todotxt/TodoTxtTask.java:113', 'SOURCE'),
    'TodoTxtTask.getPriorities': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getPriorities', 'src/main/java/net/gsantner/markor/format/todotxt/TodoTxtTask.java:105', 'SOURCE'),
    'WikitextActionButtons.createWikitextHeaderAndTitleContents': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name createWikitextHeaderAndTitleContents', 'src/main/java/net/gsantner/markor/format/wikitext/WikitextActionButtons.java:228', 'SOURCE'),
    'WikitextLinkResolver.getNotebookRootDir': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getNotebookRootDir', 'src/main/java/net/gsantner/markor/format/wikitext/WikitextLinkResolver.java:181', 'SOURCE'),
    'WikitextReplacePatternGenerator.<init>': ('no_trigger_in_app', 'class WikitextReplacePatternGenerator is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/format/wikitext/WikitextReplacePatternGenerator.java:21', 'SOURCE'),
    'WikitextSyntaxHighlighter$Colors.<init>': ('no_trigger_in_app', 'class WikitextSyntaxHighlighter$Colors is never created on a reachable path (no reached constructor call, no XML or manifest name)', 'src/main/java/net/gsantner/markor/format/wikitext/WikitextSyntaxHighlighter.java:55', 'SOURCE'),
    'WrMarkorSingleton.addMarkdownFilesFromDirectory': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name addMarkdownFilesFromDirectory', 'thirdparty/java/other/writeily/model/WrMarkorSingleton.java:185', 'SOURCE'),
    'WrMarkorSingleton.getNotesLastDirectory': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name getNotesLastDirectory', 'thirdparty/java/other/writeily/model/WrMarkorSingleton.java:42', 'SOURCE'),
    'WrMarkorSingleton.isDirectoryEmpty': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name isDirectoryEmpty', 'thirdparty/java/other/writeily/model/WrMarkorSingleton.java:176', 'SOURCE'),
    'WrMarkorSingleton.lambda$addMarkdownFilesFromDirectory$1': ('no_trigger_in_app', 'no route from the entry points: every caller is unreachable (WrMarkorSingleton.addMarkdownFilesFromDirectory)', 'thirdparty/java/other/writeily/model/WrMarkorSingleton.java:185', 'INFERRED'),
    'WrMarkorSingleton.setNotesLastDirectory': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name setNotesLastDirectory', 'thirdparty/java/other/writeily/model/WrMarkorSingleton.java:46', 'SOURCE'),
    'WrRenameDialog.newInstance(File)': ('no_trigger_in_app', 'no bytecode caller in the app call table, no method reference and no XML handler uses the name newInstance', 'thirdparty/java/other/writeily/ui/WrRenameDialog.java:40', 'SOURCE'),
}

# SUPPRESS: AUTO calls dropped from the graph (src, dst) because they start in unreachable code or call a closed component.
sup(*[('BackupUtils.<init>', 'GsBackupUtils.<init>'), ('FlexmarkKatexExtension$KatexVisitorExt.VISIT_HANDLERS', 'FlexmarkKatexExtension$KatexVisitorExt$1.<init>'), ('FlexmarkKatexExtension$KatexVisitorExt.VISIT_HANDLERS', 'FlexmarkKatexExtension$KatexVisitorExt$2.<init>'), ('GsContextUtils.drawTextOnDrawable', 'GsContextUtils.drawableToBitmap(Context,int)'), ('GsContextUtils.drawableToBitmap(Context,int)', 'GsContextUtils.drawableToBitmap(Drawable)'), ('GsContextUtils.isFossBuild', 'GsContextUtils.bcbool'), ('GsContextUtils.isGooglePlayBuild', 'GsContextUtils.bcbool'), ('GsContextUtils.loadImageFromFilesystem', 'GsContextUtils.calculateInSampleSize'), ('GsContextUtils.loadMarkdownForTextViewFromRaw', 'GsSimpleMarkdownParser.removeMultiNewlines'), ('GsContextUtils.loadMarkdownForTextViewFromRaw', 'GsSimpleMarkdownParser.replaceBulletCharacter'), ('GsContextUtils.loadMarkdownForTextViewFromRaw', 'GsSimpleMarkdownParser.replaceColor'), ('GsContextUtils.receiveResultFromLocalBroadcast', 'GsContextUtils$1.<init>'), ('GsContextUtils.requestExternalStoragePermission(Activity,int)', 'GsContextUtils.requestExternalStoragePermission(Activity,String)'), ('GsFileBrowserListAdapter.doAfterChange', 'GsFileBrowserListAdapter$1.<init>'), ('GsFileUtils.deleteRecursive', 'GsFileUtils.deleteRecursive'), ('GsFileUtils.readBinaryFile', 'GsFileUtils.readCloseBinaryStream(InputStream,int)'), ('GsFileUtils.readCloseTextStream(InputStream)', 'GsFileUtils.readCloseTextStream(InputStream,boolean)'), ('GsFileUtils.readTextFile', 'GsFileUtils.readCloseTextStream(InputStream)'), ('GsFileUtils.searchFiles', 'GsFileUtils$1.<init>'), ('GsHashMap.getOrDefault(Object,Object)', 'GsHashMap.withDefault'), ('GsLanguagePreferenceCompat.setDefaultLanguageCode', 'GsLanguagePreferenceCompat.loadLangs(Context)'), ('GsLanguagePreferenceCompat.setSystemLanguageName', 'GsLanguagePreferenceCompat.loadLangs(Context)'), ('GsNanoProfiler.restart', 'GsNanoProfiler.end'), ('GsNanoProfiler.restart', 'GsNanoProfiler.start'), ('GsNetworkUtils.downloadFile(String,File)', 'GsNetworkUtils.downloadFile(String,File,a1)'), ('GsNetworkUtils.downloadFile(String,File,a1)', 'GsNetworkUtils.downloadFile(URL,File,a1)'), ('GsNetworkUtils.downloadFile(URL,File,a1)', 'GsNetworkUtils.downloadFile(URL,File,HttpURLConnection,a1)'), ('GsNetworkUtils.lambda$httpGetAsync$0', 'GsNetworkUtils.performCall(String,String)'), ('GsNetworkUtils.performCall(String,JSONObject)', 'GsNetworkUtils.performCall(String,String,JSONObject)'), ('GsNetworkUtils.performCall(String,String)', 'GsNetworkUtils.performCall(URL,String,String)'), ('GsNetworkUtils.performCall(String,String,HashMap)', 'GsNetworkUtils.encodeQuery'), ('GsNetworkUtils.performCall(String,String,HashMap)', 'GsNetworkUtils.performCall(URL,String,String)'), ('GsNetworkUtils.performCall(String,String,JSONObject)', 'GsNetworkUtils.performCall(URL,String,String)'), ('GsNetworkUtils.performCall(String,String,String)', 'GsNetworkUtils.performCall(URL,String,String)'), ('GsNetworkUtils.performCall(URL,String,String)', 'GsNetworkUtils.performCall(URL,String,String,HttpURLConnection)'), ('GsNetworkUtils.performCall(URL,String,String,HttpURLConnection)', 'GsFileUtils.readCloseTextStream(InputStream)'), ('GsPermissionChecker.doIfExtStoragePermissionGranted()', 'GsPermissionChecker.doIfExtStoragePermissionGranted(String)'), ('GsPermissionChecker.doIfExtStoragePermissionGranted(String)', 'GsContextUtils.requestExternalStoragePermission(Activity,String)'), ('GsPermissionChecker.mkdirIfStoragePermissionGranted', 'GsPermissionChecker.doIfExtStoragePermissionGranted()'), ('GsPreferenceFragmentBase.getPreferenceParent', 'GsPreferenceFragmentBase.getPreferenceParent'), ('GsPreferenceFragmentBase.removePreference', 'GsPreferenceFragmentBase.getPreferenceParent'), ('GsSharedPreferencesPropertyBackend.afterDaysTrue', 'GsSharedPreferencesPropertyBackend.contains'), ('GsSharedPreferencesPropertyBackend.afterDaysTrue', 'GsSharedPreferencesPropertyBackend.didDaysPassedSince'), ('GsSharedPreferencesPropertyBackend.afterDaysTrue', 'GsSharedPreferencesPropertyBackend.getDateOfDaysAgo'), ('GsSharedPreferencesPropertyBackend.afterDaysTrue', 'GsSharedPreferencesPropertyBackend.getLong(String,long)'), ('GsSharedPreferencesPropertyBackend.afterDaysTrue', 'GsSharedPreferencesPropertyBackend.setLong(String,long)'), ('GsSharedPreferencesPropertyBackend.didDaysPassedSince', 'GsSharedPreferencesPropertyBackend.getDateOfDaysAgo'), ('GsSharedPreferencesPropertyBackend.getColor(int,int,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getColor(String,int,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.getDouble(String,double)', 'GsSharedPreferencesPropertyBackend.getDouble(String,double,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.getDouble(String,double,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getLong(String,long,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.getDouble(int,double,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getDouble(String,double,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.getFloat(String,float)', 'GsSharedPreferencesPropertyBackend.getFloat(String,float,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.getFloat(int,float,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getFloat(String,float)'), ('GsSharedPreferencesPropertyBackend.getIntArray(String,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getIntListOne'), ('GsSharedPreferencesPropertyBackend.getIntArray(int,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getIntArray(String,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.getIntList(String)', 'GsSharedPreferencesPropertyBackend.getIntList(String,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.getIntList(String,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getIntListOne'), ('GsSharedPreferencesPropertyBackend.getIntList(int,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getIntListOne'), ('GsSharedPreferencesPropertyBackend.getLong(String,long)', 'GsSharedPreferencesPropertyBackend.getLong(String,long,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.getLong(int,long,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getLong(String,long,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.getStringArray(int,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.getStringArray(String,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.isPrefSet(int)', 'GsSharedPreferencesPropertyBackend.isPrefSet(SharedPreferences,int)'), ('GsSharedPreferencesPropertyBackend.resetSettings()', 'GsSharedPreferencesPropertyBackend.resetSettings(SharedPreferences)'), ('GsSharedPreferencesPropertyBackend.setDouble(String,double)', 'GsSharedPreferencesPropertyBackend.setDouble(String,double,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.setDouble(String,double,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.setLong(String,long)'), ('GsSharedPreferencesPropertyBackend.setDouble(int,double,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.setLong(String,long)'), ('GsSharedPreferencesPropertyBackend.setFloat(String,float)', 'GsSharedPreferencesPropertyBackend.setFloat(String,float,SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.setIntArray(String,Integer[],SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.setIntListOne'), ('GsSharedPreferencesPropertyBackend.setIntArray(int,Integer[],SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.setIntArray(String,Integer[],SharedPreferences[])'), ('GsSharedPreferencesPropertyBackend.setIntList(String,List)', 'GsSharedPreferencesPropertyBackend.setIntListOne'), ('GsSharedPreferencesPropertyBackend.setIntList(String,List,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.setIntListOne'), ('GsSharedPreferencesPropertyBackend.setIntList(int,List,SharedPreferences[])', 'GsSharedPreferencesPropertyBackend.setIntListOne'), ('GsSharedPreferencesPropertyBackend.setLong(String,long)', 'GsSharedPreferencesPropertyBackend.setLong(String,long,SharedPreferences[])'), ('GsSimplePlaylistParser.parse(File)', 'GsSimplePlaylistParser.parse(InputStream)'), ('GsTextUtils.fromBase64ToString', 'GsTextUtils.fromBase64'), ('GsTextWatcherAdapter.before', 'GsTextWatcherAdapter$1.<init>'), ('MarkorDialogFactory.lambda$showGlobFilesDialog$38', 'MarkorDialogFactory.showGlobFilesDialog'), ('MarkorDialogFactory.lambda$showGlobFilesDialog$39', 'GsFileUtils.searchFiles'), ('OpenEditorQuickNoteActivity.<init>', 'OpenEditorActivity.<init>'), ('OpenEditorQuickNoteActivity.onCreate', 'OpenEditorActivity.onCreate@OpenEditorQuickNoteActivity'), ('OpenEditorQuickNoteActivity.onCreate', 'OpenEditorActivity.openEditorForFile'), ('OpenEditorTodoActivity.<init>', 'OpenEditorActivity.<init>'), ('OpenEditorTodoActivity.onCreate', 'OpenEditorActivity.onCreate@OpenEditorTodoActivity'), ('OpenEditorTodoActivity.onCreate', 'OpenEditorActivity.openEditorForFile'), ('OpenShareIntoActivity.<init>', 'OpenEditorActivity.<init>'), ('OpenShareIntoActivity.onCreate', 'OpenEditorActivity.onCreate@OpenShareIntoActivity'), ('TextViewUndoRedo.restorePersistentState', 'TextViewUndoRedo.doRestorePersistentState'), ('TextViewUndoRedo.setMaxHistorySize', 'TextViewUndoRedo$EditHistory.setMaxHistorySize'), ('TodoTxtTask.getCompletionDate()', 'TodoTxtTask.getCompletionDate(String)')])

