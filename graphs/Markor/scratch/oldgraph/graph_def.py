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

ENV_KINDS_OF, STATE_KINDS_OF = {}, {}
ENV_KINDS_OF.update({ENV_LAUNCHER: ['other_app'], ENV_OTHER_APP: ['other_app'], ENV_ADB: ['other_app'], ENV_PICKER: ['other_app'],
                     ENV_PERM_MISSING: ['permission'], ENV_PERM_DIALOG: ['permission'], ENV_EXC: ['other']})
STATE_KINDS_OF.update({NEED_STARTUP_TAB: ['settings'], NEED_NOTE: ['file'], NEED_DOC_OPEN: ['session'], NEED_PREVIEW: ['session'],
                       NEED_SHORTCUT: ['settings'], NEED_APP_OPEN: ['session']})

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
    'S_TODO': 'MainActivity, todo tab: DocumentEditAndViewFragment for the todo.txt file',
    'S_QUICKNOTE': 'MainActivity, quick note tab: DocumentEditAndViewFragment for the quick note file',
    'S_MORE': 'MainActivity, more tab: MoreFragment with the info and links of the app',
    'S_NEWFILE': 'NewFileDialog (opened by the FAB): name, type, template',
    'S_DOCUMENT': 'DocumentActivity with DocumentEditAndViewFragment (the editor or the viewer of one file); variants per open mode',
    'S_SHARE_INTO': 'DocumentActivity with DocumentShareIntoFragment (text or file shared into Markor, choose the target file)',
    'S_SETTINGS': 'SettingsActivity root: settings list with sub-screens',
    'S_ACTION_BUTTONS': 'ActionButtonSettingsActivity: order of the editor action buttons',
    'S_INTRO': 'IntroActivity: the AppIntro slides shown on the first start',
    'S_PERMISSION': 'StoragePermissionActivity: the storage permission request dialog (the app cannot run without it)',
    'S_EXT_APP': 'Another app or system screen without a result (share chooser, browser, viewer)',
    'S_WIDGET_CONFIG': 'WrWidgetConfigure: configuration screen of a notebook widget',
    'S_HOME_WIDGET': 'Launcher home screen with a Markor widget (notebook widget or todo widget)',
}


def gui(src, dst, text, kind='GUI', **kw):
    e(src, dst, kind, text, gui=[text], **kw)


def sup(*pairs):
    for p in pairs:
        SUPPRESS.add(p)


# edge wrapper: records the hand-written (src, dst, kind) triples so the listener loop at the end does not add duplicates
_e_builtin = e
_HAND = set()


def e(src, dst, kind, trigger, **kw):
    _HAND.add((src, dst, kind))
    _e_builtin(src, dst, kind, trigger, **kw)


# ================================================================== A. process start, launcher, lifecycle, first visible tab
e('S_ENTRY', 'ApplicationObject.<init>', 'ENTRY', 'The process starts when the launcher icon is tapped (before any activity)',
  gui=['Tap the Markor launcher icon'], evidence='SRC AndroidManifest.xml:39-40')
e('ApplicationObject.<init>', 'ApplicationObject.onCreate', 'LIFECYCLE', 'The system calls Application.onCreate',
  evidence='SRC ApplicationObject.java:16, 39')
e('S_ENTRY', 'MainActivity.<init>', 'ENTRY', 'The MAIN / LAUNCHER intent starts MainActivity',
  gui=['Tap the Markor launcher icon'], evidence='SRC AndroidManifest.xml:61-71')
e('MainActivity.<init>', 'MainActivity.<clinit>', 'LIFECYCLE', 'class initialisation before the first instance',
  evidence='INFERRED the JVM runs the static initialiser of a class before its first instance (Java language rule, not read from a source)')
e('MainActivity.<init>', 'MainActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC MainActivity.java:76; ' + FW_ACT)
e('MainActivity.<init>', 'MainActivity.onResume', 'LIFECYCLE', 'The system calls Activity.onResume after onCreate',
  evidence='SRC MainActivity.java:279; ' + FW_ACT)
e('MainActivity.<init>', 'MainActivity.onPostResume', 'LIFECYCLE', 'The system calls Activity.onPostResume after onResume',
  evidence='SRC MainActivity.java:317; ' + FW_ACT)

# the first page: ViewPager2 shows position 0 (notebook) once the adapter is set in onCreate (tabIdToPos: notebook -> 0)
e('MainActivity.onCreate', 'S_NOTEBOOK', 'ENTERS', 'The notebook tab is the first page the pager shows (position 0)',
  evidence='SRC MainActivity.java:105-106; ' + FW_VIEWPAGER)

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
  'Handler posts onActivityFirstTimeVisible on the main looper (only on a cold start: no saved instance state)',
  evidence=FW_POST + '; SRC GsActivityBase.java:101-108; SRC MainActivity.java:317-319')
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

# ================================================================== B. other entries: other-app intents, storage permission activity, home-screen widgets and their list services, configuration, shortcuts
# B1 another app sends or opens a file with Markor (manifest 187-225). DocumentActivity has the standard launch mode (manifest 190).
e('S_ENTRY', 'DocumentActivity.<init>', 'ENTRY', 'Another app sends a text or a file to Markor (share sheet, Open with, Edit with)',
  gui=['Share or open a file from another app and choose Markor'], env=ENV_OTHER_APP, evidence='SRC AndroidManifest.xml:187-225')
e('DocumentActivity.launch(Activity,File,Boolean,Integer,boolean)', 'DocumentActivity.<init>', 'INTENT',
  'The app starts DocumentActivity with an explicit intent (startActivity)', evidence='SRC DocumentActivity.java:116')
e('DocumentActivity.<init>', 'DocumentActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC DocumentActivity.java:135; ' + FW_ACT)
e('DocumentActivity.<init>', 'DocumentActivity.onResume', 'LIFECYCLE', 'The system calls Activity.onResume',
  evidence='SRC DocumentActivity.java:310; ' + FW_ACT)
e('DocumentActivity.<init>', 'GsActivityBase.onPostResume', 'LIFECYCLE', 'The system calls Activity.onPostResume (not overridden by DocumentActivity)',
  evidence='SRC GsActivityBase.java:101-108; ' + FW_ACT)
e('DocumentActivity.<init>', 'GsActivityBase.onActivityFirstTimeVisible', 'FRAMEWORK',
  'The first-visible post calls onActivityFirstTimeVisible; DocumentActivity does not override it, so the empty base method runs',
  evidence=FW_POST + '; SRC GsActivityBase.java:101-114')

# B2 storage permission: DocumentActivity.onCreate asks for it; StoragePermissionActivity opens only when the permission is missing
e('StoragePermissionActivity.requestPermissions', 'StoragePermissionActivity.<init>', 'INTENT',
  'The storage permission is missing: the caller starts StoragePermissionActivity and finishes', env=ENV_PERM_MISSING,
  evidence='SRC StoragePermissionActivity.java:18-22')
e('StoragePermissionActivity.<init>', 'MarkorBaseActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate (the class has no own onCreate)',
  evidence='SRC StoragePermissionActivity.java:14; ' + FW_ACT)
e('StoragePermissionActivity.<init>', 'StoragePermissionActivity.onActivityFirstTimeVisible', 'FRAMEWORK',
  'The first-visible post calls the override on a cold start', evidence=FW_POST + '; SRC GsActivityBase.java:101-108; SRC StoragePermissionActivity.java:27-30')
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
e('S_ENTRY', 'WrMarkorWidgetProvider.<init>', 'ENTRY', 'The launcher adds the Markor notebook widget to the home screen',
  gui=['Add the Markor notebook widget to the home screen'], env=ENV_LAUNCHER, evidence='SRC AndroidManifest.xml:99-108')
e('WrMarkorWidgetProvider.<init>', 'WrMarkorWidgetProvider.onUpdate', 'FRAMEWORK',
  'AppWidgetProvider.onReceive gets ACTION_APPWIDGET_UPDATE and calls onUpdate',
  evidence='SRC WrMarkorWidgetProvider.java:40; FW-SRC core/java/android/appwidget/AppWidgetProvider.java:61-66')
e('WrMarkorWidgetProvider.updateLauncherWidgets', 'WrMarkorWidgetProvider.onUpdate', 'SYSTEM',
  'The app sends ACTION_APPWIDGET_UPDATE to its own provider to refresh the views',
  evidence='SRC WrMarkorWidgetProvider.java:118-134; FW-SRC core/java/android/appwidget/AppWidgetProvider.java:61-66')
e('WrMarkorWidgetProvider.onUpdate', 'S_HOME_WIDGET', 'ENTERS', 'The launcher shows the notebook widget with its buttons',
  evidence='SRC WrMarkorWidgetProvider.java:40-114')
gui('S_HOME_WIDGET', 'OpenFromShortcutOrWidgetActivity.<init>', 'Tap a button of the notebook widget (new note, quick note, todo, note list)',
    env=ENV_LAUNCHER, evidence='SRC WrMarkorWidgetProvider.java:60-107')
gui('S_HOME_WIDGET', 'MainActivity.<init>', 'Tap the folder header or the home button of the notebook widget (the notebook opens)',
    env=ENV_LAUNCHER, evidence='SRC WrMarkorWidgetProvider.java:67-93')
gui('S_HOME_WIDGET', 'MainActivity.onNewIntent', 'Tap the folder header or the home button while Markor is open (singleTop)',
    needs_state=NEED_APP_OPEN, env=ENV_LAUNCHER, evidence='SRC AndroidManifest.xml:65 (singleTop); SRC WrMarkorWidgetProvider.java:67-93; SRC MainActivity.java:223')
e('S_ENTRY', 'TodoWidgetProvider.<init>', 'ENTRY', 'The launcher adds the Markor todo widget to the home screen',
  gui=['Add the Markor todo widget to the home screen'], env=ENV_LAUNCHER, evidence='SRC AndroidManifest.xml:114-123')
e('TodoWidgetProvider.<init>', 'TodoWidgetProvider.onUpdate', 'FRAMEWORK',
  'AppWidgetProvider.onReceive gets ACTION_APPWIDGET_UPDATE and calls onUpdate',
  evidence='SRC TodoWidgetProvider.java:21; FW-SRC core/java/android/appwidget/AppWidgetProvider.java:61-66')
e('TodoWidgetProvider.updateTodoWidgets', 'TodoWidgetProvider.onUpdate', 'SYSTEM',
  'The app sends ACTION_APPWIDGET_UPDATE to its own provider to refresh the views',
  evidence='SRC TodoWidgetProvider.java:52-68; FW-SRC core/java/android/appwidget/AppWidgetProvider.java:61-66')
e('TodoWidgetProvider.onUpdate', 'S_HOME_WIDGET', 'ENTERS', 'The launcher shows the todo widget list and its buttons',
  evidence='SRC TodoWidgetProvider.java:21-42')
gui('S_HOME_WIDGET', 'OpenFromShortcutOrWidgetActivity.<init>', 'Tap a todo in the todo widget list or its header',
    env=ENV_LAUNCHER, evidence='SRC TodoWidgetProvider.java:38-42')

# B4 list services of the widgets: the launcher binds them (setRemoteAdapter); RemoteViewsService.onBind calls onGetViewFactory and factory.onCreate
e('TodoWidgetProvider.onUpdate', 'TodoWidgetService.<init>', 'SYSTEM', 'The launcher binds the todo list service named by setRemoteAdapter',
  env=ENV_LAUNCHER, evidence='SRC TodoWidgetProvider.java:33-34; SRC AndroidManifest.xml:125-127; FW-SRC core/java/android/widget/RemoteViewsService.java:235-241')
e('TodoWidgetService.<init>', 'TodoWidgetService.onGetViewFactory', 'FRAMEWORK', 'RemoteViewsService.onBind calls onGetViewFactory',
  evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:235-241; SRC TodoWidgetService.java:8-10')
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
e('WrFilesWidgetService.<init>', 'WrFilesWidgetService.onGetViewFactory', 'FRAMEWORK', 'RemoteViewsService.onBind calls onGetViewFactory',
  evidence='FW-SRC core/java/android/widget/RemoteViewsService.java:235-241; SRC WrFilesWidgetService.java:17-19')
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
e('S_ENTRY', 'WrWidgetConfigure.<init>', 'ENTRY', 'The launcher opens the notebook widget setup when the widget is added',
  gui=['Add the notebook widget: the setup screen opens and asks for a folder'], env=ENV_LAUNCHER, evidence='SRC AndroidManifest.xml:91-97')
e('WrWidgetConfigure.<init>', 'WrWidgetConfigure.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC WrWidgetConfigure.java:35; ' + FW_ACT)
e('WrWidgetConfigure.showWidgetSelectFolderDialog', 'S_WIDGET_CONFIG', 'ENTERS', 'The folder browser for the widget folder is shown',
  evidence='SRC WrWidgetConfigure.java:44, 56-58')
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
e('S_ENTRY', 'OpenFromShortcutOrWidgetActivity.<init>', 'ENTRY', 'The launcher opens a dynamic shortcut for a recent file (long-press the app icon)',
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
e('MainActivity$SectionsPagerAdapter.createFragment', 'GsFileBrowserFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'The notebook fragment adds its menu to the toolbar',
  evidence='SRC GsFileBrowserFragment.java:357; ' + FW_MENU)
e('MainActivity.onSaveInstanceState', 'GsFileBrowserFragment.onSaveInstanceState', 'FRAMEWORK',
  'The activity state includes the notebook fragment state',
  evidence='SRC MainActivity.java:154; SRC GsFileBrowserFragment.java:329; ' + FW_SAVE)

# todo and quick note pages: DocumentEditAndViewFragment created by the pager
e('MainActivity$SectionsPagerAdapter.createFragment', 'DocumentEditAndViewFragment.onCreate', 'FRAMEWORK',
  'The pager creates the todo or quick note page (DocumentEditAndViewFragment); the FragmentManager runs its onCreate',
  evidence='SRC MainActivity.java:509-526; SRC DocumentEditAndViewFragment.java:122; ' + FW_FRAG)
e('DocumentEditAndViewFragment.onCreate', 'DocumentEditAndViewFragment.onViewCreated', 'FRAMEWORK',
  'The FragmentManager creates the page view', evidence='SRC DocumentEditAndViewFragment.java:138; ' + FW_FRAG)
e('DocumentEditAndViewFragment.onViewCreated', 'DocumentEditAndViewFragment.onResume', 'FRAMEWORK',
  'The FragmentManager resumes the visible page', evidence='SRC DocumentEditAndViewFragment.java:265; ' + FW_FRAG)
e('DocumentEditAndViewFragment.onViewCreated', 'DocumentEditAndViewFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'The page adds its editor menu to the toolbar', evidence='SRC DocumentEditAndViewFragment.java:299; ' + FW_MENU)
e('GsFragmentBase.checkRunFirstTimeVisible', 'DocumentEditAndViewFragment.onFragmentFirstTimeVisible', 'CALL',
  'The base page class calls the first-visible hook, which the editor page overrides to load its document',
  evidence='SRC GsFragmentBase.java:135-140; SRC DocumentEditAndViewFragment.java:241')
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

# More page: MoreFragment shows the child preference fragment MoreInfoFragment (MoreFragment.java:48-54)
e('MainActivity$SectionsPagerAdapter.createFragment', 'MoreFragment.onViewCreated', 'FRAMEWORK',
  'The pager creates the more page; the FragmentManager creates its view',
  evidence='SRC MainActivity.java:509-526; SRC MoreFragment.java:46; ' + FW_FRAG)
for m in ('doUpdatePreferences', 'getPreferenceResourceForInflation', 'isDividerVisible'):
    e('MoreFragment.onViewCreated', 'MoreInfoFragment.%s' % m, 'FRAMEWORK',
      'The child preference fragment (MoreInfoFragment) is shown and asks for its preferences (%s)' % m,
      evidence='SRC MoreFragment.java:48-54; INFERRED the preference base class calls %s (GsPreferenceFragmentBase source not read)' % m)
gui('S_MORE', 'MoreInfoFragment.onPreferenceClicked', 'Tap a row of the More list (website, Settings, rate app)',
    evidence='SRC MoreInfoFragment.java:58-67')
e('MoreInfoFragment.onPreferenceClicked', 'SettingsActivity.<init>', 'INTENT',
  'The Settings row starts SettingsActivity with startActivityForResult (request code 124)',
  cls='explicit', evidence='SRC MoreInfoFragment.java:66-67; SRC GsContextUtils.java:1116-1117, 1128-1138; ' + FW_RESULT)

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
e('MainActivity.onResume', 'MainActivity.onPause', 'LIFECYCLE',
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
  cls='explicit', needs_state=NEED_FIRST_START, evidence='SRC IntroActivity.java:25-31, 33-35; ' + FW_RESULT)
e('IntroActivity.<init>', 'IntroActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC IntroActivity.java:39; ' + FW_ACT)
e('IntroActivity.onCreate', 'S_INTRO', 'ENTERS', 'The intro slides are shown (five slides are added in onCreate)',
  evidence='SRC IntroActivity.java:39-49')
gui('S_INTRO', 'IntroActivity.onSkipPressed', 'Tap Skip', evidence='SRC IntroActivity.java:59-61; ' + FW_APPINTRO)
gui('S_INTRO', 'IntroActivity.onNextPressed', 'Tap Next', evidence='SRC IntroActivity.java:65-66; ' + FW_APPINTRO)
gui('S_INTRO', 'IntroActivity.onDonePressed', 'Tap Done on the last slide', evidence='SRC IntroActivity.java:70-73; ' + FW_APPINTRO)
gui('S_INTRO', 'IntroActivity.onSlideChanged', 'Swipe to another slide', evidence='SRC IntroActivity.java:77-78; ' + FW_APPINTRO)

# C4 settings: opened from the More tab (the toolbar item is hidden: AppSettings.isShowSettingsOptionInMainToolbar is false)
e('SettingsActivity.<init>', 'SettingsActivity.onCreate', 'LIFECYCLE', 'The system calls Activity.onCreate',
  evidence='SRC SettingsActivity.java:65-81; ' + FW_ACT)
e('SettingsActivity.onCreate', 'S_SETTINGS', 'ENTERS', 'The settings list is shown (SettingsFragmentMaster)',
  evidence='SRC SettingsActivity.java:80; SRC SettingsActivity.java:83-102')
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
e('ActionButtonSettingsActivity.onCreate', 'S_ACTION_BUTTONS', 'ENTERS', 'The action order list is shown',
  evidence='SRC ActionButtonSettingsActivity.java:56')
e('ActionButtonSettingsActivity.onCreate', 'ActionButtonSettingsActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'AppCompat builds the toolbar menu', evidence='SRC ActionButtonSettingsActivity.java:82; ' + FW_MENU)
gui('S_ACTION_BUTTONS', 'ActionButtonSettingsActivity.onOptionsItemSelected', 'Tap the back arrow in the toolbar',
    evidence='SRC ActionButtonSettingsActivity.java:91-94')
e('ActionButtonSettingsActivity.onOptionsItemSelected', 'ActionButtonSettingsActivity.onPause', 'FRAMEWORK',
  'finish() ends the screen; the system calls onPause, which saves the new order',
  evidence='SRC ActionButtonSettingsActivity.java:93-94, 112-114; FW-SRC core/java/android/app/Activity.java:1673 (onPause), 5526 (finish)')
gui('S_ACTION_BUTTONS', 'ActionButtonSettingsActivity.onPause', 'Press Back (the screen closes and the new order is saved)',
    evidence='SRC ActionButtonSettingsActivity.java:112-114; ' + FW_PAUSE)

# C5 editor (DocumentActivity): fragment lifecycle, share-into screen, back and keys, Back target, re-open of a running editor
e('DocumentActivity.handleLaunchingIntent', 'S_DOCUMENT', 'ENTERS',
  'The editor or viewer of the file is shown (DocumentEditAndViewFragment)',
  evidence='SRC DocumentActivity.java:229; ' + FW_FRAG)
e('DocumentActivity.showFragment', 'DocumentEditAndViewFragment.onCreate', 'FRAMEWORK',
  'The FragmentManager runs the editor fragment lifecycle (create, view, resume)',
  evidence='SRC DocumentActivity.java:342; ' + FW_FRAG)
e('DocumentActivity.showFragment', 'DocumentEditAndViewFragment.onViewCreated', 'FRAMEWORK',
  'The FragmentManager creates the editor view', evidence='SRC DocumentActivity.java:342; ' + FW_FRAG)
e('DocumentActivity.showFragment', 'DocumentEditAndViewFragment.onResume', 'FRAMEWORK',
  'The FragmentManager resumes the editor', evidence='SRC DocumentActivity.java:342; ' + FW_FRAG)
e('DocumentActivity.showShareInto', 'S_SHARE_INTO', 'ENTERS',
  'The share-into screen is shown (text or file shared into Markor)',
  evidence='SRC DocumentActivity.java:304-307; ' + FW_FRAG)
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
e('DocumentEditAndViewFragment.onOptionsItemSelected', 'DocumentEditAndViewFragment.lambda$onOptionsItemSelected$9', 'FRAMEWORK',
  'View.postDelayed runs the Runnable that opens the file browser after the menu closes',
  evidence='SRC DocumentEditAndViewFragment.java:630; ' + FW_POST)

# C6 listener and callback bodies: each lambda or method reference that the bytecode registers (REGISTER edge, which the
# search skips) gets one FRAMEWORK edge from the method that registers it, so the body is reachable once that method is.
# The listener type is not read per lambda, so the label is INFERRED (see Limits in readme_notes.md).
for _l in AUTO['lambdas']:
    if (_l['src'], _l['dst'], 'FRAMEWORK') in _HAND:
        continue
    e(_l['src'], _l['dst'], 'FRAMEWORK',
      'Listener or callback registered by this method runs when its event fires (view event, dialog button, handler or fragment callback)',
      evidence='INFERRED listener registered at %s:%s (bytecode line); the listener type is not read per lambda' % (_l['file'], _l['line']))

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
visit render parse create extend getNodeRenderingHandlers setAttributes finalizeBlock finalizeDocument getAfterDependents
getBeforeDependents getCharacters affectsGlobalScope getSegments getOpeningMarker getClosingMarker setOpeningMarker
setClosingMarker getAstExtra setIn parserOptions rendererOptions setText
updateDrawState updateMeasureState draw getSize chooseHeight drawBackground
append charAt clear delete getChars getFilters getSpans insert removeSpan setFilters setSpan subSequence getSpanEnd
getSpanFlags getSpanStart nextSpanTransition clearSpans length getSummary callChangeListener
'''.split())
_MENU_CLASSES = {'net/gsantner/opoc/wrapper/GsMenuItemDummy', 'net/gsantner/opoc/wrapper/GsMenuItemDummy$Menu'}


def _ancestors(c, seen=None):
    seen = set() if seen is None else seen
    h = _HIER.get(c)
    if h:
        for p in ([h['super']] if h['super'] else []) + h['ifaces']:
            if p and p not in seen:
                seen.add(p)
                _ancestors(p, seen)
    return seen


_INC = set()
for _c in AUTO['calls']:
    _INC.add(_c['dst'])
    _INC.add(_c['dst'].split('(')[0])
for _l in AUTO['lambdas']:
    _INC.add(_l['dst'])
    _INC.add(_l['dst'].split('(')[0])
for _h in _HAND:
    _INC.add(_h[1])
    _INC.add(_h[1].split('(')[0])
_CREATORS = {}
for _c in AUTO['calls']:
    _d = _c['dst'].split('(')[0]
    if _d.endswith('.<init>'):
        _CREATORS.setdefault(_d[:-len('.<init>')], set()).add(_c['src'])
_D1 = []
for _simple, _names in AUTO['impl'].items():
    _internals = _SIMPLE_CLS.get(_simple.split('.')[-1], set())
    if len(_internals) != 1:
        continue
    _cls = next(iter(_internals))
    for _name, _descs in _names.items():
        if _name in ('<init>', '<clinit>') or _name.startswith('lambda$'):
            continue
        for _desc, _node in _descs.items():
            _fl = _FLAGS.get((_cls, _name, _desc))
            if _fl is None or 'static' in _fl or 'private' in _fl:
                continue
            if _node in _INC or _node.split('(')[0] in _INC:
                continue
            _is_menu = _cls in _MENU_CLASSES
            if not _is_menu:
                if _name not in _CB_NAMES:
                    continue
                _anc = _ancestors(_cls)
                _ext = any(a not in _HIER and a != 'java/lang/Object' for a in _anc)
                _ovr = any(a in _HIER and (a, _name, _desc) in _FLAGS for a in _anc)
                if not (_ext or _ovr):
                    continue
            _D1.append((_node, _simple, _name, _is_menu))
for _node, _simple, _name, _is_menu in _D1:
    _creators = sorted(_CREATORS.get(_simple.split('(')[0], ()))
    for _x in _creators:
        if _x == _node or (_x, _node, 'FRAMEWORK') in _HAND:
            continue
        e(_x, _node, 'FRAMEWORK',
          'Framework or library calls this method on the object created here (listener, adapter, view, dialog, task or fragment hook)'
          if not _is_menu else
          'App code calls this Menu or MenuItem method through the interface on the placeholder created here',
          evidence='INFERRED method has no bytecode caller; %s; object of %s created at %s (bytecode)'
                   % ('Menu placeholder (interface dispatch)' if _is_menu else 'callback name %s' % _name,
                      _simple, _x))
