# openlauncher 0.3.1 (#67, tingsu/openlauncher@instrument-version-0.3.1, flavor flavorDefault, debug build) trigger graph definition, schema 2.
# Written by hand from the app sources (src/main and the three vendored libs smoothviewpager, materialpreffragment, launcheranim) after the schema 1 draft
# was read line by line (see AGENT_NOTES.md: what was kept, what was replaced). Direct app->app calls come from tools/extract_calls.py (bytecode, USE_AUTO);
# what the bytecode cannot see (framework callbacks, listeners, intents, reflection, generated code) and the guards of the bytecode edges are written here.
# Anonymous classes (Home$5 ...) are numbered by javac in order of appearance in the file; the numbering was checked against the class files.
# Framework claims are FW-SRC (Android 8.1.0_r1 lines that were printed and read) or INFERRED (library or system app not read).

TITLE = 'openlauncher 0.3.1 trigger graph'
USE_AUTO = True
STRICT = False        # switched to True when the build has no open classification (see the end of the file)

ENV_KINDS_OF, STATE_KINDS_OF = {}, {}


def env_text(text, kinds):
    ENV_KINDS_OF[text] = list(kinds)
    return text


def state_text(text, kinds):
    STATE_KINDS_OF[text] = list(kinds)
    return text


# ------------------------------------------------------------------ environment gates (the outside world must act)
ENV_HOME = env_text('outside package: OpenLauncher is the default home app and the system starts or re-shows its home screen (HOME key, boot, or a restart of the home screen)', ['other_app'])
ENV_EXT = env_text('outside package: another app, the system or adb sends the broadcast / intent / content call', ['other_app'])
ENV_KUSTOM = env_text('outside package: the calling package is org.kustom.wallpaper or org.kustom.widget (FiveSecsDelayContentProvider.checkCallingPackage), any other caller gets a SecurityException', ['other_app'])
ENV_PICKER = env_text('outside package: the system widget picker or the widget configure activity of the chosen widget returns a result', ['other_app'])
ENV_PICKER_CFG = env_text('outside package: the widget chosen in the picker declares a configure activity (android:configure in its provider info) and that activity returns a result', ['other_app'])
ENV_ICONPACK = env_text('outside package: an icon-pack app (an activity with category com.anddoes.launcher.THEME) is installed', ['other_app'])
ENV_PKG = env_text('system event: a package is installed, removed or changed (PACKAGE_ADDED / PACKAGE_REMOVED / PACKAGE_CHANGED broadcast)', ['system_event'])
ENV_SHORTCUT = env_text('outside package: another app sends the broadcast com.android.launcher.action.INSTALL_SHORTCUT (a legacy "add to home screen")', ['other_app'])
ENV_TIMETICK = env_text('time passes: the system sends ACTION_TIME_TICK once a minute to registered receivers', ['time'])
ENV_CLOCK = env_text('system event: the system clock or the time zone is changed (ACTION_TIME_CHANGED / ACTION_TIMEZONE_CHANGED broadcast)', ['time'])
ENV_LOWMEM = env_text('system event: the system reports low memory to the process', ['system_event'])
ENV_ADMIN_ON = env_text('outside package: the user activated OpenLauncher as a device administrator in the system settings (DEVICE_ADMIN_ENABLED broadcast; the receiver is protected by BIND_DEVICE_ADMIN)', ['other_app'])
ENV_ADMIN_OK = env_text('outside package: OpenLauncher is an active device administrator (activated in the system settings), so lockNow() does not throw', ['other_app'])
ENV_PERM_STORAGE = env_text('permission: READ_EXTERNAL_STORAGE is granted to the app (runtime permission, targetSdk 25; granted with adb install -g, pm grant or the system dialog)', ['permission'])
ENV_PERM_ANSWER = env_text('permission: the system permission controller answers the runtime-permission request (READ_CALL_LOG is not declared in the manifest, so it is denied at once; READ_EXTERNAL_STORAGE shows the system dialog)', ['permission'])
ENV_CONFIG = env_text('hardware: the device configuration changes while Home is shown (a hardware keyboard is attached or the screen size or orientation changes; Home declares android:configChanges="orientation|keyboard|screenSize" and handles it itself)', ['hardware'])
ENV_LANDSCAPE = env_text('hardware: the configuration delivered to Home reports landscape (Home is locked to portrait by android:screenOrientation, so this needs a device that ignores the lock; INFERRED, window manager not read)', ['hardware'])
ENV_CORRUPT = env_text('other: LauncherSettings.readSettings() returns false because generalSettings.json is not valid JSON for GeneralSettings (a JsonSyntaxException is caught)', ['other'])
ENV_OLD = env_text('outside package: the app that owns the tapped icon was uninstalled after the app list was built (startActivity throws)', ['other_app'])
ENV_STARTFAIL = env_text('other: the system app-info screen cannot be opened for the dragged package (startActivity throws, for example ActivityNotFoundException)', ['other'])
ENV_WALLPAPER = env_text('other: the current wallpaper cannot be read or blurred (an exception is thrown while blurring)', ['other'])

# ------------------------------------------------------------------ in-app state gates (an earlier action of the user is needed)
NEED_NOTFIRST = state_text('The intro was finished or skipped in an earlier start (the preference quickSettings.firstStart is false)', ['settings'])
NEED_LOADED = state_text('Home was created before in this process, so the settings are loaded (a second Home creation, for example after recreate())', ['session'])
NEED_ITEM = state_text('An app, folder or shortcut icon was placed on a desktop page (drag it from the app drawer and drop it)', ['data'])
NEED_DOCKITEM = state_text('An app, folder or shortcut icon was placed in the dock (drop it on the dock)', ['data'])
NEED_SAVED = state_text('Desktop or dock items were saved by an earlier run and the data files desktopData.json / dockData.json are read at the start of the process', ['data'])
NEED_FOLDER = state_text('A folder exists on the desktop or in the dock (drop one app icon on another one)', ['data'])
NEED_SHORTCUT = state_text('A shortcut item exists on the desktop or in the dock (another app sent INSTALL_SHORTCUT before)', ['data'])
NEED_WIDGET = state_text('A widget item exists on a desktop page (added with the edit panel "Widget" button)', ['data'])
NEED_TWOPAGES = state_text('The desktop has two or more pages (hold a dragged item at a screen edge to add one)', ['data'])
NEED_SWIPE = state_text('Settings > Gestures > "Swipe up to open the app drawer" is on (default off)', ['settings'])
NEED_GESTURE = state_text('A gesture action other than "None" was chosen in Settings > Gestures (all six gestures default to None)', ['settings'])
NEED_VERTICAL = state_text('Settings > Drawer > Drawer style is Vertical and Home was recreated (the style is read by AppDrawerController.init at Home start)', ['settings'])
NEED_VSEARCH = state_text('Settings > Drawer > Drawer style is Vertical and the drawer search bar is on (default on), and Home was recreated', ['settings'])
NEED_ICONPACK = state_text('An icon pack was picked in Settings > Icons > Icon pack (iconPackName is not empty)', ['settings'])
NEED_SHRINK = state_text('An app was removed or hidden so the reloaded app list is shorter than the previous one', ['session'])
NEED_RESTART = state_text('A setting that needs a restart of the launcher was changed in Settings (prepareRestart) or the Restart button was used', ['settings'])
NEED_HIDDEN = state_text('Apps were hidden in Settings > Icons > Hide apps (hiddenList is not null)', ['settings'])
NEED_GONE_APP = state_text('A saved app item whose app was uninstalled or hidden (ItemViewFactory.getItemView returns null for it)', ['data'])
NEED_MINIBAR_USED = state_text('The minibar was opened before (its overlay layout is visible)', ['session'])
NEED_SHOWALL = state_text('Settings > Desktop > Desktop style is "Show all apps" (experimental)', ['settings'])
NEED_GRIDGROUP = state_text('A folder holds a shortcut item (a shortcut was dropped on an app icon)', ['data'])

# ------------------------------------------------------------------ framework claims (Android 8.1.0_r1 sources that were read) and library claims
FW_LAUNCH = ('FW-SRC core/java/android/app/ActivityThread.java:2644-2660, 2685-2741, 2833-2863 (performLaunchActivity instantiates the activity, attaches it and calls callActivityOnCreate, then performStart; '
             'handleLaunchActivity then calls handleResumeActivity) and core/java/android/app/Activity.java:7014-7019, 7098-7107 (performStart and performResume call onStart and onResume)')
FW_STOP = ('FW-SRC core/java/android/app/ActivityThread.java:3985-4004, 4324-4372 (performStopActivityInner pauses and stops an activity, performDestroyActivity stops it and calls callActivityOnDestroy) '
           'and core/java/android/app/Activity.java:7159-7181 (performStop calls onStop)')
FW_RELAUNCH = ('FW-SRC core/java/android/app/Activity.java:5472-5483 (recreate asks the activity manager for a relaunch), services/core/java/com/android/server/am/ActivityManagerService.java:4999-5014 and '
               'services/core/java/com/android/server/am/ActivityRecord.java:2450-2484, 2573-2604 (requestActivityRelaunch forces a new configuration, which schedules the relaunch), '
               'core/java/android/app/ActivityThread.java:4553, 4668-4699 (handleRelaunchActivity saves the state, destroys the old activity and launches a new instance)')
FW_CLICK = ('FW-SRC core/java/android/view/View.java:6289-6300, 6368-6375, 11764-11779 (performClick and performLongClick call the OnClickListener / OnLongClickListener set with setOn...Listener; '
            'dispatchTouchEvent calls the OnTouchListener first)')
FW_DRAG = ('FW-SRC core/java/android/view/View.java:22844-22847, 22899-22966 (startDrag calls startDragAndDrop, which asks the shadow builder for its metrics and draws it, prepares the drag and calls performDrag on the window session), '
           'services/core/java/com/android/server/wm/Session.java:316-375 and services/core/java/com/android/server/wm/DragState.java:249-300, 359-380, 448-482, 493-540 '
           '(the window manager sends DRAG_STARTED, DRAG_LOCATION, DROP and DRAG_ENDED to the windows) and services/core/java/com/android/server/wm/WindowManagerService.java:802-851 (touch moves and the up event of the drag channel call notifyMoveLw / notifyDropLw / endDragLw), '
           'core/java/android/view/ViewRootImpl.java:3943-3948, 5892-5960, 6044-6074 (the window handles the event, ENTERED and EXITED are made by setDragFocus), core/java/android/view/ViewGroup.java:1576-1700 and '
           'core/java/android/view/View.java:23109-23130 (ViewGroup passes the event down, View calls its OnDragListener, else onDragEvent)')
FW_POST = ('FW-SRC core/java/android/view/View.java:15777-15787, 15808-15818 (post and postDelayed hand the Runnable to the view handler) and core/java/android/os/Handler.java:97-107, 355-358, 427-430, 789-791 '
           '(post and postDelayed queue the Runnable as the callback of a message, dispatchMessage runs it on the handler looper thread); INFERRED that thread is the main thread because the views and handlers are created on it')
FW_ANIM_END = ('FW-SRC core/java/android/view/ViewPropertyAnimator.java:841-847, 889-894, 1112-1130 (withEndAction stores the Runnable, startAnimation attaches it to the animator, the animator listener runs it in onAnimationEnd)')
FW_ASYNC = ('FW-SRC core/java/android/os/AsyncTask.java:219-224, 237-262, 594-596, 632-650, 326-334, 369-374, 285, 705-713, 691-697 (execute uses the serial executor, which hands each task to THREAD_POOL_EXECUTOR '
            'and the worker calls doInBackground; postResult sends the result to a main-looper handler whose handleMessage calls finish, which calls onPostExecute)')
FW_ASYNC_PRE = 'FW-SRC core/java/android/os/AsyncTask.java:632-650 (execute and executeOnExecutor call onPreExecute on the calling thread before the worker starts)'
FW_ASYNC_CANCEL = 'FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-697 (cancel sets the cancelled flag, and finish then calls onCancelled instead of onPostExecute)'
FW_INFLATE = ('FW-SRC core/java/android/view/LayoutInflater.java:615-617, 645-648 (createView looks up the (Context, AttributeSet) constructor of the view class named in the XML and calls newInstance)')
FW_PASS = ('FW-SRC core/java/android/view/View.java:22034-22050, 22071, 19644-19659, 19192, 19308 (measure, layout and draw call the onMeasure, onLayout and onDraw of the view)')
FW_TEXT = ('FW-SRC core/java/android/widget/TextView.java:9286-9292, 9309-9316, 9359-9366, 9375-9382, 11902-11939 (the text watchers added with addTextChangedListener are called through the ChangeWatcher on every change of the Editable)')
FW_RECV_DYN = ('FW-SRC core/java/android/app/ContextImpl.java:1412-1435 (registerReceiver hands the receiver to a ReceiverDispatcher and the activity manager) and core/java/android/app/LoadedApk.java:1389-1402, 1300-1313 '
               '(a delivered broadcast is posted to the main thread, where receiver.onReceive runs); INFERRED the activity manager sends a matching broadcast to the registered receiver (ActivityManagerService not read for this)')
FW_RECV_MAN = ('FW-SRC core/java/android/app/ActivityThread.java:3141-3188 (handleReceiver loads the receiver class named in the manifest, creates it and calls onReceive); '
               'INFERRED the activity manager sends the broadcast to the manifest receiver of the explicit component (ActivityManagerService not read for this)')
FW_PROVIDER_START = ('FW-SRC core/java/android/app/ActivityThread.java:5792-5812, 6225-6239 (the process installs the providers of its manifest: installProvider loads the class, creates it and calls attachInfo) and '
                     'core/java/android/content/ContentProvider.java:1891-1918 (attachInfo calls onCreate)')
FW_PROVIDER_CALL = ('FW-SRC core/java/android/content/ContentProvider.java:209-246, 256-268, 333-345, 513-525 (the Transport that serves a remote call checks the permission, records the calling package and calls query / insert / delete of the provider) '
                    'and 743-749 (getCallingPackage returns the recorded package); INFERRED the content resolver of the caller routes the call to the exported provider by authority')
FW_PERM = ('FW-SRC core/java/android/app/Activity.java:4371-4384 (requestPermissions starts the permission-controller activity for result), 7259-7270, 7412-7419 (the result is dispatched to onRequestPermissionsResult); '
           'INFERRED ActivityCompat.requestPermissions calls Activity.requestPermissions on API 23+ and the permission controller (another app) returns the grant results (support library and PackageInstaller not read)')
FW_RESULT = ('FW-SRC core/java/android/app/Activity.java:824, 5489-5508 (an activity that finishes without setResult reports RESULT_CANCELED with no data) and core/java/android/app/ActivityThread.java:4253-4265, '
             'core/java/android/app/Activity.java:7259-7266 (the result is delivered to the starting activity through dispatchActivityResult, which calls onActivityResult)')
FW_BACK = ('FW-SRC core/java/android/app/Activity.java:2886-2894, 2975-2985 (the Back key calls onBackPressed) and 3001-3010 (the platform onBackPressed pops the fragment back stack or finishes the activity)')
FW_WIDGETHOST = ('FW-SRC core/java/android/appwidget/AppWidgetHost.java:373-393, 399-402 (createView calls onCreateView, which the app overrides, then fills the view with the widget RemoteViews)')
FW_ADAPTER = ('FW-SRC core/java/android/widget/ListView.java:575 and core/java/android/widget/AbsListView.java:2365 (setAdapter reads getCount, the list asks the adapter for getView) and '
              'core/java/android/widget/AbsListView.java:3108-3127, core/java/android/widget/AdapterView.java:314-321 (a tap calls adapter.getItemId and then the OnItemClickListener)')
FW_ADAPTER_ID = 'FW-SRC core/java/android/widget/AdapterView.java:833-847, 1245-1263 (after the adapter notifies a change the list calls getItemId of the first row)'
FW_PARCEL = ('FW-SRC core/java/android/os/Parcel.java:1785-1791 (writeParcelable calls writeToParcel) and 2841-2852, 2867-2907 (readParcelableCreator finds the static CREATOR field of the class by reflection, readParcelable then calls its createFromParcel)')
FW_CONFIG = ('FW-SRC core/java/android/app/ActivityThread.java:5106-5140, core/java/android/view/ViewRootImpl.java:3575-3604, core/java/android/view/ViewGroup.java:1512-1519, core/java/android/view/View.java:12301-12303 '
             '(an activity configuration change that the manifest handles itself reaches the view tree through dispatchConfigurationChanged, which calls onConfigurationChanged of every view)')
FW_LOWMEM = 'FW-SRC core/java/android/app/ActivityThread.java:4725-4746, 5296-5302 (handleLowMemory calls onLowMemory of the application and of every resumed or live activity)'
FW_GLOBALLAYOUT = 'FW-SRC core/java/android/view/ViewRootImpl.java:2248-2251 (performTraversals calls dispatchOnGlobalLayout of the tree observer, which calls the registered OnGlobalLayoutListener)'
FW_FLING = 'FW-SRC core/java/android/view/GestureDetector.java:640-657 (the detector calls the listener onFling when a touch ends with enough velocity)'
FW_TIMETICK = 'FW-SRC services/core/java/com/android/server/AlarmManagerService.java:1007-1012, 2781-2793 (the alarm manager sends ACTION_TIME_TICK to registered receivers at the top of every minute)'
FW_PKGBCAST = ('FW-SRC services/core/java/com/android/server/pm/PackageManagerService.java:14564-14600, 14864-14887, 19590-19612, 22134-22153 (the package manager broadcasts PACKAGE_ADDED, PACKAGE_REMOVED and PACKAGE_CHANGED)')
FW_VP = ('SRC SmoothViewPager.java:427-462, 901, 911-961, 1021, 1071, 1105, 1506 (the vendored copy of ViewPager: setAdapter requests a layout, onMeasure calls populate, populate calls the adapter getCount / instantiateItem / destroyItem, dataSetChanged asks getItemPosition)')
FW_VPSCROLL = 'SRC SmoothViewPager.java:1685-1725, 1744-1785, 1804-1817 (scrolling calls onPageScrolled of the pager, which calls the registered OnPageChangeListener)'
FW_CLINIT = 'INFERRED the class has a static initialiser that the JVM runs on first use of the class (Java language rule, not read from a source)'
INF_BK = 'INFERRED ButterKnife.bind loads the generated <Class>$$ViewBinder by name and calls its bind, which registers the click listeners and reads the views (ButterKnife source not read; the generated class is in the APK)'
INF_MD = 'INFERRED MaterialDialogs builds the dialog and calls the registered callbacks when the user acts (library source not read)'
INF_FAST = 'INFERRED FastAdapter and RecyclerView ask the item for getType, getLayoutRes, getFactory and call bindView when a row is shown (library source not read)'
INF_CIRC = 'INFERRED the animator created by the CircularReveal library calls its AnimatorListener while it runs (library source not read)'
INF_DRAWER = 'INFERRED the support DrawerLayout calls the registered DrawerListener while it moves (support library source not read)'
INF_FRAG = 'INFERRED the support FragmentManager drives the fragment lifecycle callbacks (support library source not read)'
INF_COMPAT = 'INFERRED the AppCompat activity base classes call the activity callbacks (support library source not read)'
INF_ONB = 'INFERRED the OnboarderActivity library shows the pages and calls onSkipButtonPressed / onFinishButtonPressed when the buttons are tapped (library source not read)'
INF_GSON = 'INFERRED Gson reads the file with reflection and calls the no-argument constructor of the class (Gson source not read)'
INF_POPUP = 'INFERRED the support PopupMenu calls the OnMenuItemClickListener when an item is tapped (support library source not read)'
INF_ACT_MENU = 'INFERRED the support library calls onCreateOptionsMenu / onOptionsItemSelected for the toolbar (support library source not read)'

ANDROID_SRC_NOTE = 'AndroidManifest.xml'

# ------------------------------------------------------------------ pages
DRAG_TYPES = ('APP', 'APP_DRAWER', 'GROUP', 'SHORTCUT', 'WIDGET', 'LAUNCHER')
SCREENS = {
    'S_ENTRY': 'Outside the app: another launcher, the HOME key, boot, other apps, the system or adb',
    'S_EXIT': 'The process is killed by System.exit (Restore backup) or the screen is finished',
    'S_HOME_PAUSED': 'Home is stopped: another app, a system screen or Settings is on top',
    'S_SETTINGS_PAUSED': 'SettingsActivity is stopped (another activity or Home on top)',
    'S_INTRO': 'Three-page onboarding of Init (Skip / Finish) on the first start',
    'S_HOME_LOADING': 'Home splash while LauncherSettings.readSettings runs (first creation per process)',
    'S_HOME_DESKTOP': 'Home, normal mode, after the app list is loaded: desktop page, dock with the All Apps button, clock text',
    'S_HOME_EDIT': 'Home, desktop edit mode: pages scaled down, edit panel (Remove page, Set as home, Widget, Action, Settings); page touches are blocked',
    'S_HOME_DRAWER_PAGED': 'App drawer, paged style (default): pages of app icons with a page indicator',
    'S_HOME_DRAWER_VERTICAL': 'App drawer, vertical style: scrolling grid with a drag scroll bar and a search field',
    'S_HOME_GROUP_POPUP': 'Folder popup over the desktop: the apps of a folder and its title',
    'S_HOME_MINIBAR': 'Minibar (left drawer) open: rows EditMinBar, Wallpaper, Lock, ClearRam, Device settings, Launcher settings, Volume, App drawer',
    'S_MINIBAR_POPUP': 'Minibar popup window; variant CLEARRAM shows free RAM and storage, VOLUME shows the four volume sliders; the next touch closes it',
    'S_ACTION_MENU': 'PopupMenu over the edit panel Action button (one item: AppDrawer)',
    'S_DLG_WALLPAPER': 'Dialog "Wallpaper": Set wallpaper / Blur',
    'S_DLG_RENAME_GROUP': 'Dialog to rename a folder (text input, OK / Cancel)',
    'S_DLG_SETTINGS_ERROR': 'Alert "Some settings can\'t be read" after an unreadable settings file',
    'S_HOME_DRAG': 'A long-press drag of an item is in progress (variant = what is dragged); the drag bar and edge zones appear',
    'S_EXT_WIDGET_PICKER': 'System widget picker / widget configure screen (another package)',
    'S_EXT_APP': 'Another app launched from an icon, folder item or shortcut',
    'S_EXT_SYSTEM': 'A system screen: app info, uninstall dialog, system settings, wallpaper chooser, device-admin settings, volume panel',
    'S_CRASH': 'CustomActivityOnCrash error screen in the :error_activity process',
    'S_SETTINGS_ROOT': 'SettingsActivity root: 7 category buttons and an Info menu item',
    'S_SETTINGS_DESKTOP': 'Settings > Desktop: minibar, desktop style, desktop size, search bar, fullscreen, indicator, labels',
    'S_SETTINGS_DOCK': 'Settings > Dock: dock size, dock labels',
    'S_SETTINGS_DRAWER': 'Settings > Drawer: drawer style, size, card, search bar, icon, remember page, indicator',
    'S_SETTINGS_INPUT': 'Settings > Gestures: swipe switch and six gesture buttons',
    'S_SETTINGS_COLORS': 'Settings > Colors: five color buttons',
    'S_SETTINGS_ICONS': 'Settings > Icons: icon size, icon pack, hide apps',
    'S_SETTINGS_OTHER': 'Settings > Other: Backup / Restore, Restart',
    'S_DLG_DESKTOP_STYLE': 'Single-choice dialog Normal / Show all apps',
    'S_DLG_DRAWER_STYLE': 'Single-choice dialog Paged / Vertical',
    'S_DLG_NUMPREF': 'Number seek-bar dialog (grid size / icon size)',
    'S_DLG_GESTURE': 'Single-choice dialog for one gesture action (variant = which gesture)',
    'S_DLG_COLOR': 'Color chooser dialog',
    'S_DLG_ICONPACK': 'List dialog: Default and the installed icon packs',
    'S_DLG_BACKUP': 'Dialog: Backup / Restore / Cancel',
    'S_PERMISSION': 'System runtime-permission dialog for READ_EXTERNAL_STORAGE',
    'S_ABOUT': 'About screen (version, GitHub, libraries, rate, team cards)',
    'S_HIDEAPPS_LOADING': 'Hide apps: progress while the app list loads',
    'S_HIDEAPPS_LIST': 'Hide apps: checkable list of all apps and a confirm button',
    'S_HIDEAPPS_SNACKBAR': 'Hide apps: snackbar "select at least one app" with OK',
    'S_MINIBAR_EDIT': 'Minibar editor: on/off switch and a draggable, checkable list of the rows',
}


def gui(src, dst, text, kind='GUI', **kw):
    e(src, dst, kind, text, gui=[text], **kw)


def sup(*pairs):
    for p_ in pairs:
        SUPPRESS.add(p_)


AUTO_GUARDS = {}


def ag(src, dst, guard=None, state=None, env=None):
    """Guard / STATE / ENV of a bytecode-derived edge: the bytecode scan shows the call but not the conditions around it (read in the source, see the cited lines)."""
    AUTO_GUARDS[(src, dst)] = (guard, state, env)


HOME_PAGES = ['S_HOME_DESKTOP', 'S_HOME_EDIT', 'S_HOME_DRAWER_PAGED', 'S_HOME_DRAWER_VERTICAL', 'S_HOME_GROUP_POPUP', 'S_HOME_MINIBAR']
DESKTOP_PAGES = ['S_HOME_DESKTOP', 'S_HOME_EDIT']
DRAWER_PAGES = ['S_HOME_DRAWER_PAGED', 'S_HOME_DRAWER_VERTICAL']

# ================================================================== A. entry points (manifest) and the intro
e('S_ENTRY', 'Init.<init>', 'ENTRY', 'Tap the OpenLauncher icon in another launcher (MAIN + LAUNCHER filter), or adb monkey / am start',
  gui=['Home screen of another launcher: tap the OpenLauncher icon'], evidence='SRC AndroidManifest.xml:28-36; ' + FW_LAUNCH)
e('S_ENTRY', 'Home.<init>', 'ENTRY', 'The system starts the home screen (MAIN + HOME + DEFAULT filter)', gui=['Press the HOME key'], env=ENV_HOME,
  evidence='SRC AndroidManifest.xml:38-54; ' + FW_LAUNCH, cls='non_standard', via='implicit intent: the system resolves the HOME category to the activity through its manifest intent filter')
e('Home.<init>', 'Home.<clinit>', 'LIFECYCLE', 'class initialisation before the first instance (the three static IntentFilters)', evidence='SRC activity/Home.java:148-178; ' + FW_CLINIT)
e('S_ENTRY', 'FiveSecsDelayContentProvider.<init>', 'ENTRY', 'The process installs the providers of its manifest when it starts, before any component',
  evidence='SRC AndroidManifest.xml:56-61; ' + FW_PROVIDER_START)
e('FiveSecsDelayContentProvider.<init>', 'FiveSecsDelayContentProvider.onCreate', 'LIFECYCLE', 'ContentProvider.attachInfo calls onCreate', evidence='SRC util/FiveSecsDelayContentProvider.java:19-22; ' + FW_PROVIDER_START)
for m_, ln_ in (('query', '24-32'), ('insert', '41-46'), ('update', '65-72'), ('getType', '34-39'), ('delete', '48-63')):
    e('S_ENTRY', 'FiveSecsDelayContentProvider.' + m_, 'ENTRY', 'Another app or `adb shell content` calls %s on the exported provider (authority com.benny.openlauncher.util.FiveSecsDelayContentProvider)' % m_,
      gui=['In another app or adb: content %s on the authority' % m_], env=ENV_EXT, evidence='SRC util/FiveSecsDelayContentProvider.java:%s; AndroidManifest.xml:56-61; ' % ln_ + FW_PROVIDER_CALL,
      cls='non_standard', via='content resolver: the provider is found by its authority, nothing in the app calls it')
e('FiveSecsDelayContentProvider.delete', 'AutoFinishActivity.start', 'CALL', 'the last path segment is "reset5secs": start the invisible activity',
  guard='checkCallingPackage() did not throw (the caller is org.kustom.wallpaper or org.kustom.widget) and uri.getLastPathSegment() equals "reset5secs"', env=ENV_KUSTOM,
  evidence='SRC util/FiveSecsDelayContentProvider.java:48-63, 79-87')
e('AutoFinishActivity.start', 'AutoFinishActivity.<init>', 'INTENT', 'c.startActivity(new Intent(c, AutoFinishActivity.class)) with the provider context (application context)',
  guard='startActivity(Intent) passes null options, so the NEW_TASK check of ContextImpl does not throw on API 27', evidence='SRC activity/AutoFinishActivity.java:15-17; FW-SRC core/java/android/app/ContextImpl.java:853-856, 865-877 (startActivity(Intent) calls startActivity(intent, null); the missing-NEW_TASK exception needs non-null options)')
e('AutoFinishActivity.<init>', 'AutoFinishActivity.onCreate', 'LIFECYCLE', 'the system creates the activity and calls onCreate, which calls finish()', evidence='SRC activity/AutoFinishActivity.java:9-13; ' + FW_LAUNCH)
e('S_ENTRY', 'DeviceAdminReceiver.<init>', 'ENTRY', 'The user activates OpenLauncher as device admin: the system sends DEVICE_ADMIN_ENABLED to the manifest receiver',
  gui=['System settings > Security > Device administrators > activate OpenLauncher'], env=ENV_ADMIN_ON, evidence='SRC AndroidManifest.xml:84-94; ' + FW_RECV_MAN,
  cls='non_standard', via='manifest receiver started by the system broadcast ACTION_DEVICE_ADMIN_ENABLED (resolved by action name)')
e('DeviceAdminReceiver.<init>', 'DeviceAdminReceiver.onReceive', 'LIFECYCLE', 'BroadcastReceiver.onReceive (empty body)', evidence='SRC util/DeviceAdminReceiver.java:7-12; ' + FW_RECV_MAN)
e('S_ENTRY', 'ShortcutReceiver.onReceive', 'ENTRY', 'An explicit broadcast to the exported manifest receiver (it has no intent filter)', env=ENV_EXT, needs_state=NEED_LOADED,
  guard='Home.launcher is not null: Home was created in this process (the receiver uses Home.launcher after its first lines)',
  evidence='SRC AndroidManifest.xml:95-98; util/ShortcutReceiver.java:23-25, 48; ' + FW_RECV_MAN, cls='non_standard', via='manifest receiver started by an explicit-component broadcast from another app')

# ---- Init: the intro
e('Init.<init>', 'Init.onCreate', 'LIFECYCLE', 'The system instantiates Init, then calls onCreate', evidence='SRC activity/Init.java:16-18; ' + FW_LAUNCH)
e('Init.onCreate', 'S_INTRO', 'ENTERS', 'First start: the three onboarding pages are set up', guard='getBoolean("firstStart", true) is true (the default on a fresh install)',
  evidence='SRC activity/Init.java:20-51; ' + INF_ONB)
e('Init.onCreate', 'Init.RockIt', 'CALL', 'not the first start: RockIt() runs at once and onCreate returns', guard='the preference quickSettings.firstStart is false', needs_state=NEED_NOTFIRST,
  evidence='SRC activity/Init.java:20-23')
e('S_INTRO', 'Init.onSkipButtonPressed', 'GUI', 'Tap Skip', gui=['Tap "Skip"'], evidence='SRC activity/Init.java:54-60; ' + INF_ONB,
  cls='non_standard', via='OnboarderActivity library calls the abstract button callbacks')
e('S_INTRO', 'Init.onFinishButtonPressed', 'GUI', 'Swipe to the last page and tap "Let\'s start."', gui=['Swipe to the last page and tap "Let\'s start."'], evidence='SRC activity/Init.java:72-76; ' + INF_ONB,
  cls='non_standard', via='OnboarderActivity library calls the abstract button callbacks')
e('Init.RockIt', 'Home.<init>', 'INTENT', 'startActivity(new Intent(Init.this, Home.class)) then finish()', evidence='SRC activity/Init.java:62-70; ' + FW_LAUNCH)

# ================================================================== B. Home: lifecycle, creation, settings load, app list load
e('Home.<init>', 'Home.onCreate', 'LIFECYCLE', 'The system instantiates Home, then calls onCreate', evidence='SRC activity/Home.java:180-182; ' + FW_LAUNCH)
e('Home.onCreate', 'Home.onStart', 'LIFECYCLE', 'onStart after onCreate', evidence='SRC activity/Home.java:723-728; ' + FW_LAUNCH)
e('Home.onStart', 'Home.onResume', 'LIFECYCLE', 'onResume after onStart (first resume of this instance: the splash or the desktop is built only later)', evidence='SRC activity/Home.java:743-749; ' + FW_LAUNCH)
e('Home.onCreate', 'Home$$ViewBinder.<init>', 'FRAMEWORK', 'ButterKnife.bind(this) creates the generated binder', evidence='SRC activity/Home.java:197; ' + INF_BK,
  cls='non_standard', via='ButterKnife: the generated Home$$ViewBinder is loaded by name')
e('Home.onCreate', 'Home$$ViewBinder.bind', 'FRAMEWORK', 'ButterKnife.bind(this) calls bind(finder, target, source)', evidence='SRC activity/Home.java:197; ' + INF_BK,
  cls='non_standard', via='ButterKnife: the generated Home$$ViewBinder is loaded by name')
INF_GEN = 'INFERRED generated ButterKnife class (no source file in the dataset; the class file shows this call)'
e('Home$$ViewBinder.bind', 'Home$$ViewBinder.createUnbinder', 'CALL', 'bind creates the unbinder', evidence=INF_GEN, cls='explicit')
e('Home$$ViewBinder.createUnbinder', 'Home$$ViewBinder$InnerUnbinder.<init>', 'CALL', 'createUnbinder builds the InnerUnbinder', evidence=INF_GEN, cls='explicit')
for _i in range(1, 6):
    e('Home$$ViewBinder.bind', 'Home$$ViewBinder$%d.<init>' % _i, 'CALL', 'bind creates click listener %d for the %s button' % (_i, ('Remove', 'Set as home', 'Widget', 'Action', 'Settings')[_i - 1]),
      evidence=INF_GEN + '; SRC activity/Home.java:470 (the five ids of @OnClick in this order)', cls='explicit')
sup(('Home$$ViewBinder.bind', 'Home$$ViewBinder.createUnbinder'), ('Home$$ViewBinder.createUnbinder', 'Home$$ViewBinder$InnerUnbinder.<init>'), 'Home$$ViewBinder$InnerUnbinder.unbind()')
for _i in range(1, 6):
    sup(('Home$$ViewBinder.bind', 'Home$$ViewBinder$%d.<init>' % _i))
# views that the layouts name (view_home.xml is included by activity_home.xml)
for _cls, _lay in (('Desktop', 'view_home.xml:8-17'), ('Dock', 'view_home.xml:79-91'), ('AppDrawerController', 'view_home.xml:93-100'), ('DragOptionView', 'view_home.xml:102-114'),
                   ('GroupPopupView', 'view_home.xml:116-123'), ('PagerIndicator', 'view_home.xml:70-77'), ('MiniPopupView', 'activity_home.xml:53-58'), ('SwipeListView', 'activity_home.xml:21-30')):
    e('Home.onCreate', _cls + '.<init>(Context,AttributeSet)', 'FRAMEWORK', 'setContentView inflates the layout, which names <%s>' % _cls, evidence='SRC res/layout/%s; activity/Home.java:194-195; ' % _lay + FW_INFLATE,
      cls='non_standard', via='LayoutInflater builds the view class named in the XML layout by reflection')

# ---- onCreate: the first creation in this process reads the settings on a worker thread; later creations skip it
e('Home.onCreate', 'S_HOME_LOADING', 'ENTERS', 'The loading splash is shown while the settings are read', guard='LauncherSettings.init is false (the first Home creation in this process)', evidence='SRC activity/Home.java:202-210')
e('Home.onCreate', 'Home$2.doInBackground', 'ASYNC', 'new AsyncTask().execute(): LauncherSettings.readSettings runs on a worker thread', guard='LauncherSettings.init is false', evidence='SRC activity/Home.java:205-228; ' + FW_ASYNC)
e('Home$2.doInBackground', 'Home$2.onPostExecute', 'ASYNC', 'the settings are read: onPostExecute runs on the main thread', evidence='SRC activity/Home.java:213-227; ' + FW_ASYNC)
e('Home$2.onPostExecute', 'Home$2$1.run', 'ASYNC', 'loadingSplash.animate().alpha(0).withEndAction(...): the splash is removed when the fade ends', evidence='SRC activity/Home.java:216-221; ' + FW_ANIM_END)
e('Home$2.onPostExecute', 'S_DLG_SETTINGS_ERROR', 'ENTERS', 'readSettings() returned false: the alert "Some settings can\'t be read"', guard='!result && Home.launcher != null', env=ENV_CORRUPT,
  evidence='SRC activity/Home.java:223-226; util/LauncherSettings.java:126-156')
e('Home.onCreate', 'Home.init', 'CALL', 'the settings are already loaded in this process: no splash, init() runs at once', guard='LauncherSettings.init is true', needs_state=NEED_LOADED, evidence='SRC activity/Home.java:202-204')
# ---- reading the settings and the saved items (on a fresh install there is no file: openFileInput throws IOException, which is caught)
for _s, _f, _l in (('LauncherSettings.readDockData', 'dockData.json', '61-70'), ('LauncherSettings.readDesktopData', 'desktopData.json', '92-104')):
    e(_s, 'Desktop$Item.<init>(SimpleItem)', 'CALL', 'one Item is built for each saved SimpleItem of ' + _f, guard='the file exists and its JSON has an element', needs_state=NEED_SAVED, evidence='SRC util/LauncherSettings.java:' + _l)
    e(_s, 'Desktop$SimpleItem.<init>()', 'FRAMEWORK', 'gson.fromJson(reader, SimpleItem.class) builds each saved item of ' + _f, guard='the file exists and its JSON has an element', needs_state=NEED_SAVED,
      evidence='SRC util/LauncherSettings.java:65, 99; ' + INF_GSON, cls='non_standard', via='Gson: reflection on the no-argument constructor')

# ---- Home.init: first load of the app list, listeners
e('Home$3.onAppUpdated', 'S_HOME_DESKTOP', 'ENTERS', 'the app list is loaded: the desktop items and the dock (with the All Apps button) are built and shown', evidence='SRC activity/Home.java:260-278')
e('AppManager.getAllApps', 'AppManager$AsyncGetApps.onPreExecute', 'FRAMEWORK', 'new AsyncGetApps().execute(): onPreExecute runs on the calling thread', guard='no task yet, or the previous task finished, or the previous task is cancelled first',
  evidence='SRC util/AppManager.java:101-107, 162-166; ' + FW_ASYNC_PRE)
e('AppManager.getAllApps', 'AppManager$AsyncGetApps.doInBackground', 'ASYNC', 'the worker thread lists the launcher activities, applies the hidden list and an icon pack', evidence='SRC util/AppManager.java:101-107, 174-217; ' + FW_ASYNC)
e('AppManager$AsyncGetApps.doInBackground', 'AppManager$AsyncGetApps.onPostExecute', 'ASYNC', 'the list is ready: onPostExecute runs on the main thread and tells the listeners', evidence='SRC util/AppManager.java:219-251; ' + FW_ASYNC)
NEED_RELOAD2 = state_text('A second app-list reload starts while the first one is still running (two package events, or hide-apps closing right after another reload)', ['session'])
e('AppManager.getAllApps', 'AppManager$AsyncGetApps.onCancelled', 'FRAMEWORK', 'task.cancel(false) while the previous load is still running: onCancelled replaces onPostExecute of that task',
  guard='task.getStatus() == RUNNING', needs_state=NEED_RELOAD2, evidence='SRC util/AppManager.java:101-107, 168-172; ' + FW_ASYNC_CANCEL)
e('AppManager$AsyncGetApps.doInBackground', 'AppManager$AsyncGetApps$1.compare', 'FRAMEWORK', 'Collections.sort(activitiesInfo, comparator) compares the labels of the launcher activities',
  guard='the device has two or more launcher activities (the standard emulator has many)', evidence='SRC util/AppManager.java:181-187; INFERRED java.util sorting calls compare for lists with at least two elements (libcore source not read)')

# ---- system callbacks of Home: permission result, receivers, low memory, crash screen, stop / resume / recreate, Back
e('Home.initQuickCenter', 'Home.onRequestPermissionsResult', 'SYSTEM', 'ActivityCompat.requestPermissions(READ_CALL_LOG): the permission controller answers',
  guard='checkSelfPermission(READ_CALL_LOG) is not PERMISSION_GRANTED (the permission is commented out of the manifest, so it never is)', env=ENV_PERM_ANSWER,
  evidence='SRC activity/Home.java:617-624, 627-637; AndroidManifest.xml:4-8; ' + FW_PERM)
sup(('Home.initQuickCenter', 'Home$CallLogObserver.<init>'), ('Home.initQuickCenter', 'Home$CallLogObserver.onChange(boolean)'),
    ('Home.onRequestPermissionsResult', 'Home$CallLogObserver.<init>'), ('Home.onRequestPermissionsResult', 'Home$CallLogObserver.onChange(boolean)'))
e('S_HOME_DESKTOP', 'Home$1.onReceive', 'SYSTEM', 'ACTION_TIME_TICK arrives every minute (the receiver is registered for TIME_TICK, TIMEZONE_CHANGED and TIME_CHANGED)', gui=['Wait up to a minute'], env=ENV_TIMETICK,
  evidence='SRC activity/Home.java:153-168, 639-643; ' + FW_RECV_DYN + '; ' + FW_TIMETICK)
e('S_HOME_DESKTOP', 'AppUpdateReceiver.onReceive', 'SYSTEM', 'Another app is installed, removed or changed (PACKAGE_ADDED / REMOVED / CHANGED)', gui=['Install or uninstall an app'], env=ENV_PKG,
  evidence='SRC activity/Home.java:170-174, 639-643; util/AppUpdateReceiver.java:7-12; ' + FW_RECV_DYN + '; ' + FW_PKGBCAST)
e('S_HOME_DESKTOP', 'ShortcutReceiver.onReceive', 'SYSTEM', 'An app sends the legacy INSTALL_SHORTCUT broadcast', gui=['In another app: "add to home screen" (legacy shortcut)'], env=ENV_SHORTCUT,
  evidence='SRC activity/Home.java:176-177, 639-643; util/ShortcutReceiver.java:23-65; ' + FW_RECV_DYN)
e('S_HOME_DESKTOP', 'Home.onLowMemory', 'SYSTEM', 'The system reports low memory', gui=['(the system is under memory pressure)'], env=ENV_LOWMEM, evidence='SRC activity/Home.java:699-704; ' + FW_LOWMEM)
e('S_HOME_DESKTOP', 'S_CRASH', 'SYSTEM', 'An uncaught exception ends the process and CustomActivityOnCrash shows its error screen',
  env=env_text('other: an uncaught exception is thrown in the app process (the crash handler is installed in Home.onCreate)', ['other']),
  evidence='SRC activity/Home.java:184-187; INFERRED CustomActivityOnCrash installs an uncaught-exception handler that starts the error activity (library source not read)')
for p_ in HOME_PAGES + ['S_HOME_DRAG@' + t_ for t_ in DRAG_TYPES]:
    gui(p_, 'Home.onStop', 'Press Home or Recents, or another activity covers Home (onStop writes the settings)', kind='SYSTEM', evidence='SRC activity/Home.java:730-735; ' + FW_STOP)
e('Home.onStop', 'S_HOME_PAUSED', 'ENTERS', 'Home is stopped: another app or screen is in front', evidence='SRC activity/Home.java:730-735; ' + FW_STOP)
e('S_HOME_PAUSED', 'Home.onResume@RETURN', 'SYSTEM', 'Home returns to the foreground (launcher icon, recents, Back from the app on top)', gui=['Return to OpenLauncher from the recents list'],
  evidence='SRC activity/Home.java:743-749; ' + FW_LAUNCH)
e('Home.onResume@RETURN', 'S_HOME_DESKTOP', 'ENTERS', 'handleLauncherPause() leaves edit mode, closes the drawer and goes to the home page',
  needs_state=NEED_LOADED, evidence='SRC activity/Home.java:743-765')
e('Home.onResume@RETURN', 'Home.handleLauncherPause@DESKTOP', 'CALL', 'handleLauncherPause() when Home resumes', evidence='SRC activity/Home.java:747')
e('Home.onResume', 'Home.handleLauncherPause@DESKTOP', 'CALL', 'handleLauncherPause() at the first resume: desktop is not in edit mode and the drawer is not visible', evidence='SRC activity/Home.java:747, 751-760')
sup('Home.handleLauncherPause')
e('Home.handleLauncherPause@DRAWER', 'Home.closeAppDrawer', 'CALL', 'the drawer view is visible: closeAppDrawer()', guard='!desktop.inEditMode && appDrawerController.getDrawer() != null and its visibility is VISIBLE', evidence='SRC activity/Home.java:752-755')
e('Home.handleLauncherPause@EDIT', 'Desktop$DesktopAdapter$4.onClick', 'CALL', 'desktop.pages.get(currentItem).performClick() ends edit mode', guard='desktop.inEditMode', evidence='SRC activity/Home.java:758-760; ' + FW_CLICK)
for _n in ('DESKTOP', 'DRAWER', 'EDIT', 'POPUP'):
    e('Home.handleLauncherPause@' + _n, 'GroupPopupView.dismissPopup', 'CALL', 'groupPopup.dismissPopup()', guard='groupPopup != null', evidence='SRC activity/Home.java:762-764')
# Back: DrawerLayout.closeDrawers() closes the minibar, then handleLauncherPause()
BACKV = {'DESKTOP': ('S_HOME_DESKTOP', 'S_HOME_MINIBAR'), 'EDIT': ('S_HOME_EDIT',), 'DRAWER': DRAWER_PAGES, 'POPUP': ('S_HOME_GROUP_POPUP',)}
for _v, _pages in BACKV.items():
    for p_ in _pages:
        gui(p_, 'Home.onBackPressed@' + _v, 'Press Back', kind='SYSTEM', evidence='SRC activity/Home.java:737-741; ' + FW_BACK)
    e('Home.onBackPressed@' + _v, 'Home.handleLauncherPause@' + _v, 'CALL', 'handleLauncherPause()', evidence='SRC activity/Home.java:738-741')
    e('Home.onBackPressed@' + _v, 'S_HOME_DESKTOP', 'ENTERS', 'Back closes the minibar, the drawer, the popup or edit mode and shows the desktop', evidence='SRC activity/Home.java:737-765')
sup('Home.onBackPressed')
# recreate(): the relaunch stops and destroys the old instance, then creates a new one (callers: SettingsActivity, AppManager, HideApps)
e('Home.onDestroy', 'Home.<init>', 'SYSTEM', 'recreate(): a new Home instance is created after the old one was destroyed', guard='the destroy came from a relaunch', needs_state=NEED_RESTART,
  evidence='SRC activity/Home.java:686-697; ' + FW_RELAUNCH)

# ================================================================== C. desktop pages: pager, touches, edit mode, gestures
FW_TAP = ('FW-SRC core/java/android/view/View.java:12972-12990, 13029-13044, 24767-24771 (a tap on a clickable view posts PerformClick, which calls performClick) and 23212-23225, 24725-24739 '
          '(a press held for the long-press timeout calls performLongClick); ' + FW_CLICK[len('FW-SRC '):])
FW_TOUCH = ('FW-SRC core/java/android/view/ViewGroup.java:2495-2520 (dispatchTouchEvent asks onInterceptTouchEvent on a down) and core/java/android/view/View.java:11764-11779 (dispatchTouchEvent calls the OnTouchListener, then onTouchEvent)')
FW_PRESS = 'FW-SRC core/java/android/view/View.java:9947-9958, 23132-23145 (setPressed and the drag callbacks call refreshDrawableState)'
# ---- the pager of the desktop: the layout pass populates it; scrolling reports to the page-change listeners
e('Desktop.init', 'Desktop$DesktopAdapter.getCount', 'FRAMEWORK', 'setAdapter(new DesktopAdapter) reads the page count', evidence='SRC widget/Desktop.java:76-86; ' + FW_VP)
for _cb in ('instantiateItem', 'isViewFromObject'):
    e('Desktop.init', 'Desktop$DesktopAdapter.' + _cb, 'FRAMEWORK', 'the first layout of the pager populates it: %s builds / checks the current page' % _cb, evidence='SRC widget/Desktop.java:375-390; ' + FW_VP)
e('Desktop.init', 'Desktop.onPageScrolled', 'FRAMEWORK', 'the first layout of the pager scrolls to the home page (scrollToItem -> pageScrolled -> onPageScrolled)',
  evidence='SRC widget/Desktop.java:316-322; SmoothViewPager.java:572-590, 1676-1678, 1695-1725, 1744-1785')
e('Desktop.onPageScrolled', 'PagerIndicator.onPageScrolled', 'FRAMEWORK', 'super.onPageScrolled dispatches to the registered OnPageChangeListener (the indicator)', guard='the indicator is registered (Settings > Desktop > page indicator is on, default on)',
  evidence='SRC widget/PagerIndicator.java:64-89; widget/Desktop.java:316-322; ' + FW_VPSCROLL)
gui('S_HOME_DESKTOP', 'PagerIndicator.onPageScrollStateChanged', 'Drag the desktop horizontally', evidence='SRC widget/PagerIndicator.java:95-97; SmoothViewPager.java:419, 1804-1844')
gui('S_HOME_DESKTOP', 'PagerIndicator.onPageSelected', 'Swipe to another desktop page', needs_state=NEED_TWOPAGES, evidence='SRC widget/PagerIndicator.java:91-93; SmoothViewPager.java:528-590, 1821-1836')
for _s in ('addPageRight', 'addPageLeft', 'removePage'):
    e('Desktop$DesktopAdapter.' + _s, 'Desktop$DesktopAdapter.getItemPosition', 'FRAMEWORK', 'notifyDataSetChanged(): the pager asks getItemPosition of every page (always POSITION_NONE)', evidence='SRC widget/Desktop.java:350-368; SmoothPagerAdapter.java:275-281; ' + FW_VP)
    e('Desktop$DesktopAdapter.' + _s, 'Desktop$DesktopAdapter.destroyItem', 'FRAMEWORK', 'POSITION_NONE: the pager destroys the old page views and populates again', evidence='SRC widget/Desktop.java:380-390; ' + FW_VP)
    e('Desktop$DesktopAdapter.' + _s, 'Desktop$DesktopAdapter.instantiateItem', 'FRAMEWORK', 'the pager populates again after the change', evidence='SRC widget/Desktop.java:385-390; ' + FW_VP)
# ---- touches on the desktop page
for _p in DESKTOP_PAGES:
    gui(_p, 'CellContainer.onInterceptTouchEvent', 'Touch the desktop page', evidence='SRC widget/CellContainer.java:164-168; ' + FW_TOUCH)
    gui(_p, 'Desktop$DesktopAdapter$3.onTouch', 'Touch the desktop page (the page touch listener remembers where the touch started)', evidence='SRC widget/Desktop.java:473-497; ' + FW_TOUCH)
    gui(_p, 'CellContainer.onTouchEvent', 'Touch an empty area of the desktop page', evidence='SRC widget/CellContainer.java:143-162; ' + FW_TOUCH)
    gui(_p, 'Desktop$DesktopAdapter$4.onClick', 'Tap an empty area of the desktop page (ends edit mode; runs the single-click gesture when one is set)', evidence='SRC widget/Desktop.java:498-519; ' + FW_TAP)
gui('S_HOME_DESKTOP', 'Desktop$DesktopAdapter$5.onLongClick', 'Long-press an empty area of the desktop page', evidence='SRC widget/Desktop.java:520-537; ' + FW_TAP)
e('Desktop$DesktopAdapter$5.onLongClick', 'S_HOME_EDIT', 'ENTERS', 'The pages scale down, the edit panel appears and page touches are blocked', evidence='SRC widget/Desktop.java:522-535')
e('Desktop$DesktopAdapter$4.onClick', 'S_HOME_DESKTOP', 'ENTERS', 'the pages scale back and edit mode ends', evidence='SRC widget/Desktop.java:498-519')
# CellContainer touch: the quick tap in edit mode runs the page click; the gesture library sees every touch outside edit mode
e('CellContainer.onTouchEvent', 'SimpleFingerGestures.onTouch', 'CALL', 'gestures.onTouch(this, event) outside edit mode (exceptions are ignored)', guard='blockTouch is false (not in edit mode) and gestures != null', evidence='SRC widget/CellContainer.java:155-160')
# ---- Home callbacks of the desktop edit listener
e('Desktop$DesktopAdapter$5.onLongClick', 'Home.onDesktopEdit', 'CALL', 'desktop.desktopEditListener.onDesktopEdit()', guard='desktop.desktopEditListener != null (set in Home.initViews)', evidence='SRC widget/Desktop.java:533-534; activity/Home.java:314')
e('Desktop$DesktopAdapter$4.onClick', 'Home.onFinishDesktopEdit', 'CALL', 'desktop.desktopEditListener.onFinishDesktopEdit()', guard='desktop.desktopEditListener != null; runs on every tap of the page, also outside edit mode', evidence='SRC widget/Desktop.java:515-518')
e('Home.onDesktopEdit', 'Home$7.run', 'ASYNC', 'desktopEditOptionPanel.postDelayed(..., 100): hide the dock, set the search bar', evidence='SRC activity/Home.java:425-435; ' + FW_POST)
e('Home.onFinishDesktopEdit', 'Home$8.run', 'ASYNC', 'desktopEditOptionPanel.postDelayed(..., 100): show the dock, hide the edit panel', evidence='SRC activity/Home.java:446-458; ' + FW_POST)

# ---- finger gestures on the desktop page: the vendored SimpleFingerGestures library classifies the touch and calls the listener of Desktop$DesktopAdapter
SFG = 'in/championswimmer/sfg/lib/SimpleFingerGestures.java'
GA = 'in/championswimmer/sfg/lib/GestureAnalyser.java'
GESTURES = [   # variant, listener callbacks (callback, ...), GUI text, guard (calcGesture flag)
    ('SWIPE_UP', ('onSwipeUp',), 'Swipe up on the desktop with one to four fingers', 'calcGesture returns SWIPE_n_UP (every finger moved up with |dy| > 3 * |dx|)'),
    ('SWIPE_DOWN', ('onSwipeDown',), 'Swipe down on the desktop with one to four fingers', 'calcGesture returns SWIPE_n_DOWN'),
    ('SWIPE_LEFT', ('onSwipeLeft',), 'Swipe left on the desktop with one finger (not a page change when the touch starts on the page border)', 'calcGesture returns SWIPE_n_LEFT'),
    ('SWIPE_RIGHT', ('onSwipeRight',), 'Swipe right on the desktop with one finger', 'calcGesture returns SWIPE_n_RIGHT'),
    ('PINCH', ('onPinch',), 'Pinch the desktop with two to four fingers', 'calcGesture returns PINCH_n (the fingers moved together)'),
    ('UNPINCH', ('onUnpinch',), 'Spread two to four fingers on the desktop', 'calcGesture returns UNPINCH_n (the fingers moved apart)'),
    ('DOUBLE_TAP', ('onDoubleTap',), 'Double-tap the desktop', 'calcGesture returns DOUBLE_TAP_1 (a second short touch within 500 ms of the previous one)'),
]
sup(*[('SimpleFingerGestures.doCallBack', 'Desktop$DesktopAdapter$1.' + _cb) for _cb in ('onSwipeUp', 'onSwipeDown', 'onSwipeLeft', 'onSwipeRight', 'onPinch', 'onUnpinch', 'onDoubleTap')])
for _v, _cbs, _text, _g in GESTURES:
    e('SimpleFingerGestures.onTouch', 'SimpleFingerGestures.doCallBack@' + _v, 'CALL', 'the finger is released after a tracked gesture: doCallBack(ga.getGesture(ev))', gui=[_text], guard=_g,
      evidence='SRC %s:76-83, 89-96, 107-181; %s:130-250' % (SFG, GA))
    for _cb in _cbs:
        e('SimpleFingerGestures.doCallBack@' + _v, 'Desktop$DesktopAdapter$1.' + _cb, 'CALL', 'the library calls the listener registered with setOnFingerGestureListener', guard=_g,
          evidence='SRC %s:107-181; widget/Desktop.java:392-444, 461' % SFG, cls='standard')
e('SimpleFingerGestures.doCallBack@UNPINCH', 'Desktop$DesktopAdapter$1.onDoubleTap', 'CALL', 'the case UNPINCH_4 has no break, so DOUBLE_TAP_1 runs as well', guard='calcGesture returns UNPINCH_4 (four fingers moved apart)',
  evidence='SRC %s:172-179' % SFG, cls='standard')
# the six callbacks that read a gesture setting and run a launcher action; each action number is one variant of RunAction
RA = ('EditMinBar', 'SetWallpaper', 'LockScreen', 'ClearRam', 'DeviceSettings', 'LauncherSettings', 'VolumeDialog', 'OpenAppDrawer')
RA_LABEL = dict(EditMinBar='Minibar Settings', SetWallpaper='Set Wallpaper', LockScreen='Lock Screen', ClearRam='Clear RAM', DeviceSettings='Device Settings', LauncherSettings='Launcher Settings',
                VolumeDialog='Volume Dialog', OpenAppDrawer='Open App Drawer')
GESTURE_SITES = (('Desktop$DesktopAdapter$1.onSwipeUp', 'swipeUp', '396-398'), ('Desktop$DesktopAdapter$1.onSwipeDown', 'swipeDown', '404-406'),
                 ('Desktop$DesktopAdapter$1.onPinch', 'pinch', '422-424'), ('Desktop$DesktopAdapter$1.onUnpinch', 'unPinch', '430-432'),
                 ('Desktop$DesktopAdapter$1.onDoubleTap', 'doubleClick', '438-440'), ('Desktop$DesktopAdapter$4.onClick', 'singleClick', '501-503'))
for _site, _field, _ln in GESTURE_SITES:
    for _k, _v in enumerate(RA, 1):
        e(_site, 'LauncherAction.RunAction@' + _v, 'CALL', 'the %s gesture is set to "%s"' % (_field, RA_LABEL[_v]), needs_state=NEED_GESTURE,
          guard='gestureValues[generalSettings.%s] == %d, so LauncherAction.actionItems[%d] (%s) is run%s' % (_field, _k, _k - 1, _v, ' and the desktop is not in edit mode' if _field == 'singleClick' else ''),
          evidence='SRC widget/Desktop.java:%s; res/values/arrays.xml:13-23; util/LauncherAction.java:29-39' % _ln)
sup('LauncherAction.RunAction')

# ---- the edit panel (view_desktop_edit_option.xml): five buttons with ButterKnife click listeners
EDIT_BTN = (('removepage', 'REMOVE_PAGE', 'Remove'), ('setashomepage', 'SET_HOME', 'Set as home'), ('addwidgetbtn', 'WIDGET', 'Widget'), ('addLauncherAction', 'ACTION', 'Action'), ('openSettings', 'SETTINGS', 'Settings'))
for _i, (_id, _var, _lab) in enumerate(EDIT_BTN, 1):
    e('S_HOME_EDIT', 'Home$$ViewBinder$%d.doClick' % _i, 'GUI', 'Tap "%s" in the edit panel' % _lab, gui=['Tap "%s" in the edit panel' % _lab],
      evidence='SRC activity/Home.java:470; res/layout/view_desktop_edit_option.xml:11-59; ' + INF_BK + '; ' + FW_TAP, cls='non_standard', via='ButterKnife: the generated DebouncingOnClickListener calls doClick')
    e('Home$$ViewBinder$%d.doClick' % _i, 'Home.onViewClicked@' + _var, 'CALL', 'doClick calls target.onViewClicked(view)', evidence=INF_GEN + '; SRC activity/Home.java:470-488', cls='explicit')
e('S_HOME_EDIT', 'Tool$1.onTouch', 'GUI', 'Touch an edit-panel button (the colour mask animation)', gui=['Press an edit-panel button'], evidence='SRC activity/Home.java:396-402; util/Tool.java:359-376; ' + FW_TOUCH)
sup('Home.onViewClicked')
e('Home.onViewClicked@REMOVE_PAGE', 'Desktop.removeCurrentPage', 'CALL', 'desktop.removeCurrentPage()', evidence='SRC activity/Home.java:473-475')
e('Home.onViewClicked@SET_HOME', 'LauncherSettings.getInstance', 'CALL', 'desktopHomePage = desktop.getCurrentItem()', evidence='SRC activity/Home.java:476-478')
e('Home.onViewClicked@WIDGET', 'Home.pickWidget', 'CALL', 'pickWidget(view)', evidence='SRC activity/Home.java:479-481')
e('Home.onViewClicked@ACTION', 'Home.addLauncherAction', 'CALL', 'addLauncherAction(view)', evidence='SRC activity/Home.java:482-484')
e('Home.onViewClicked@SETTINGS', 'LauncherAction.RunAction@LauncherSettings', 'CALL', 'LauncherAction.RunAction(LauncherSettings, this)', evidence='SRC activity/Home.java:485-487')
e('Home.addLauncherAction', 'S_ACTION_MENU', 'ENTERS', 'PopupMenu.show(): the menu with the single item "AppDrawer"', evidence='SRC activity/Home.java:491-501; res/menu/launcher_action.xml:3-5; ' + INF_POPUP)
gui('S_ACTION_MENU', 'Home$9.onMenuItemClick', 'Tap "AppDrawer" in the popup menu', evidence='SRC activity/Home.java:494-499; ' + INF_POPUP, cls='standard')
e('Home$9.onMenuItemClick', 'S_HOME_EDIT', 'ENTERS', 'an "All apps" button is added to a free cell of the current page and the menu closes', evidence='SRC activity/Home.java:503-512')
# the item the Action menu adds is an ACTION item: its view comes from the LAUNCHER variant of the item factory
e('Home.onOptionsItemSelected', 'ItemViewFactory.getItemView@LAUNCHER', 'CALL', 'desktop.addItemToPosition(Item.newAppDrawerBtn(), ...) builds the All Apps button view', guard='item id is R.id.appDrawer',
  evidence='SRC activity/Home.java:503-512; widget/Desktop.java:292-314')

# ================================================================== D. icons on the desktop and in the dock: the item factory, taps, long-press drags, drops, folders
IVF = 'ItemViewFactory.getItemView'
_B = 'AppItemView$Builder.'
IVF_RANGE = {'LAUNCHER': '43-55', 'APP': '56-81', 'WIDGET': '82-178', 'SHORTCUT': '179-199', 'GROUP': '200-233'}
IVF_TYPE = {'LAUNCHER': 'ACTION', 'APP': 'APP', 'WIDGET': 'WIDGET', 'SHORTCUT': 'SHORTCUT', 'GROUP': 'GROUP'}
# which branch of the switch (item.type) makes each call; the bytecode scan reports one call site per callee, so the branches are read from the source (lines 39-237)
TYPES_OF = {}
for _d in (_B + '<init>(Context)', _B + 'getView', _B + 'setTextColor', _B + 'setLabelVisibility', _B + 'withOnLongPressDrag(Item,Action,LongPressCallBack)', _B + 'vibrateWhenLongPress', _B + 'withOnTouchGetPosition'):
    TYPES_OF[_d] = ('LAUNCHER', 'APP', 'SHORTCUT', 'GROUP')
TYPES_OF.update({_B + 'setLauncherAction': ('LAUNCHER',), 'ItemViewFactory$1.<init>': ('LAUNCHER',),
                 'AppManager.getInstance': ('APP',), 'AppManager.findApp': ('APP',), _B + 'setAppItem': ('APP',), _B + 'withOnClickLaunchApp': ('APP',), 'ItemViewFactory$2.<init>': ('APP',),
                 _B + 'setShortcutItem': ('SHORTCUT',), 'ItemViewFactory$10.<init>': ('SHORTCUT',),
                 'ItemViewFactory$11.<init>': ('GROUP',), 'ItemViewFactory$12.<init>': ('GROUP',), 'ItemViewFactory.getGroupIconDrawable': ('GROUP',), 'AppItemView.setIcon': ('GROUP',), 'AppItemView.setLabel': ('GROUP',),
                 'WidgetView.setOnLongClickListener': ('WIDGET',)})
for _n in range(3, 10):
    TYPES_OF['ItemViewFactory$%d.<init>' % _n] = ('WIDGET',)
_seen = set()
for _c in AUTO['calls']:
    if _c['src'] != IVF or _c['dst'] not in TYPES_OF or _c['dst'] in _seen:
        continue
    _seen.add(_c['dst'])
    for _t in TYPES_OF[_c['dst']]:
        e(IVF + '@' + _t, _c['dst'], 'CALL', 'the %s branch of the switch on item.type builds the view' % IVF_TYPE[_t], guard='item.type == ' + IVF_TYPE[_t], evidence='SRC viewutil/ItemViewFactory.java:' + IVF_RANGE[_t])
    SUPPRESS.add((IVF, _c['dst']))
assert _seen == set(TYPES_OF), set(TYPES_OF) - _seen
# widget views: the app widget host creates the view and calls the app's onCreateView; the handles and the long press are listeners on it
e(IVF + '@WIDGET', 'WidgetHost.onCreateView', 'FRAMEWORK', 'Home.appWidgetHost.createView(context, id, info) calls the overridden onCreateView', guard='item.type == WIDGET', evidence='SRC viewutil/ItemViewFactory.java:82-85; ' + FW_WIDGETHOST)
e('WidgetHost.onCreateView', 'WidgetView.<init>(Context)', 'CALL', 'new WidgetView(context)', evidence='SRC viewutil/WidgetHost.java:16-19')
e(IVF + '@WIDGET', 'ItemViewFactory$3.run', 'ASYNC', 'widgetView.post(...): updateWidgetOption runs when the view is attached', guard='item.type == WIDGET', evidence='SRC viewutil/ItemViewFactory.java:87-92; ' + FW_POST)
e(IVF + '@WIDGET', 'ItemViewFactory$4.run', 'ASYNC', 'widgetContainer.postDelayed(action, 2000): the resize handles shrink away', guard='item.type == WIDGET', evidence='SRC viewutil/ItemViewFactory.java:111-120; ' + FW_POST)
e('ItemViewFactory$3.run', 'ItemViewFactory.updateWidgetOption', 'CALL', 'updateWidgetOption(item)', evidence='SRC viewutil/ItemViewFactory.java:87-92, 261-268')
# the resize handles (vertexpand, horiexpand, vertless, horiless) of the widget container
for _n, _lab, _ln in ((6, 'taller', '136-145'), (7, 'wider', '146-155'), (8, 'shorter', '156-165'), (9, 'narrower', '166-175')):
    e('S_HOME_DESKTOP', 'ItemViewFactory$%d.onClick' % _n, 'GUI', 'Tap the resize handle that makes the widget %s' % _lab, gui=['Tap the widget resize handle (visible for 2 s after the widget appears or is touched)'],
      needs_state=NEED_WIDGET, guard='the handle is visible (view.getScaleX() >= 1)', evidence='SRC viewutil/ItemViewFactory.java:%s; ' % _ln + FW_TAP)
    e('ItemViewFactory$%d.onClick' % _n, 'ItemViewFactory$4.run', 'ASYNC', 'widgetContainer.postDelayed(action, 2000) after the resize', guard='the handle is visible', evidence='SRC viewutil/ItemViewFactory.java:%s; ' % _ln + FW_POST)
gui('S_HOME_DESKTOP', 'WidgetView.onInterceptTouchEvent', 'Touch a widget', needs_state=NEED_WIDGET, evidence='SRC widget/WidgetView.java:33-51; ' + FW_TOUCH)
e('WidgetView.onInterceptTouchEvent', 'ItemViewFactory$5.onLongClick', 'CALL', 'longClick.onLongClick(WidgetView.this) after a touch that moved for more than 500 ms (the view keeps its own long-click listener)', guard='ACTION_MOVE and System.currentTimeMillis() - down > 500',
  needs_state=NEED_WIDGET, evidence='SRC widget/WidgetView.java:23-26, 38-47')

# ---- who builds a view of which type (the switch above is reached from these places)
e('Dock.initDockItem', IVF + '@LAUNCHER', 'CALL', 'the dock builds its saved items: the All Apps button is the item the first start adds to dockData', guard='dockData holds an ACTION item with x < dockGridX (added by Home$3.onAppUpdated on the first launch)',
  evidence='SRC widget/Dock.java:50-58; activity/Home.java:263-274')
for _t in ('APP', 'SHORTCUT', 'GROUP'):
    e('Dock.initDockItem', IVF + '@' + _t, 'CALL', 'the dock builds a saved %s item' % IVF_TYPE[_t], needs_state=NEED_SAVED, guard='dockData holds an item of this type with x < dockGridX', evidence='SRC widget/Dock.java:50-58')
for _t in ('LAUNCHER', 'APP', 'SHORTCUT', 'GROUP', 'WIDGET'):
    e('Desktop.initDesktopItem', IVF + '@' + _t, 'CALL', 'the desktop builds a saved %s item' % IVF_TYPE[_t], needs_state=NEED_SAVED, guard='desktopData holds an item of this type with x < desktopGridX and y < desktopGridY',
      evidence='SRC widget/Desktop.java:88-102')
e('ShortcutReceiver.onReceive', IVF + '@SHORTCUT', 'CALL', 'Home.launcher.desktop.addItemToPagePosition(item, page) builds the shortcut view', evidence='SRC util/ShortcutReceiver.java:46-64; widget/Desktop.java:278-289')
e('Home.createWidget', IVF + '@WIDGET', 'CALL', 'desktop.addItemToPagePosition(item, page) builds the widget view', evidence='SRC activity/Home.java:668-682; widget/Desktop.java:278-289')
# a drop on the desktop or the dock builds the view of the dropped item (Desktop.onDrag / Dock.onDrag -> addItemToPosition -> getItemView)
DROP = {'APP': ('desktop', 'dock', 'delete', 'info', 'remove', 'left', 'right'), 'APP_DRAWER': ('desktop', 'dock', 'delete', 'info', 'left', 'right'), 'GROUP': ('desktop', 'dock', 'remove', 'left', 'right'),
        'SHORTCUT': ('desktop', 'dock', 'remove', 'left', 'right'), 'WIDGET': ('desktop', 'remove', 'left', 'right'), 'LAUNCHER': ('desktop', 'dock', 'remove', 'left', 'right')}
VIEWTYPE_OF_DRAG = {'APP': 'APP', 'APP_DRAWER': 'APP', 'GROUP': 'GROUP', 'SHORTCUT': 'SHORTCUT', 'WIDGET': 'WIDGET', 'LAUNCHER': 'LAUNCHER'}
for _dt, _vt in VIEWTYPE_OF_DRAG.items():
    e('S_HOME_DRAG@' + _dt, IVF + '@' + _vt, 'GUI', 'Drop the item on a free cell of the desktop page (Desktop.onDrag, ACTION_DROP, addItemToPosition)', gui=['Drop the item on a free cell of the desktop'],
      guard='a free cell exists at the drop point', evidence='SRC widget/Desktop.java:186-225, 292-314; ' + FW_DRAG)
    if _dt != 'WIDGET':
        e('S_HOME_DRAG@' + _dt, IVF + '@' + _vt, 'GUI', 'Drop the item on a free cell of the dock (Dock.onDrag, ACTION_DROP, addItemToPosition)', gui=['Drop the item on a free cell of the dock'],
          guard='a free cell exists at the drop point', evidence='SRC widget/Dock.java:114-142, 199-220; ' + FW_DRAG)
# dropping an app or a shortcut on an occupied app / shortcut / folder icon makes (or extends) a folder
e('Desktop.handleOnDropOver@MERGE', IVF + '@GROUP', 'CALL', 'callBack.addItemToPagePosition(item, page) builds the folder view', guard='item.type becomes GROUP', evidence='SRC widget/Desktop.java:543-569')
e('S_HOME_DRAG@APP', 'Desktop.handleOnDropOver@MERGE', 'GUI', 'Drop the app on another app, shortcut or folder icon on the desktop or in the dock (makes a folder)', gui=['Drop the item on another icon'], needs_state=NEED_ITEM,
  guard='the drop cell is occupied by an APP, SHORTCUT or GROUP item whose actions.length < 12 and the dropped item is an APP or SHORTCUT', evidence='SRC widget/Desktop.java:201-224, 543-569; widget/Dock.java:118-141; ' + FW_DRAG)
for _dt in ('APP_DRAWER', 'SHORTCUT'):
    e('S_HOME_DRAG@' + _dt, 'Desktop.handleOnDropOver@MERGE', 'GUI', 'Drop the item on another app, shortcut or folder icon (makes a folder)', gui=['Drop the item on another icon'], needs_state=NEED_ITEM,
      guard='the drop cell is occupied by an APP, SHORTCUT or GROUP item whose actions.length < 12 and the dropped item is an APP or SHORTCUT', evidence='SRC widget/Desktop.java:201-224, 543-569; ' + FW_DRAG)
sup(('Desktop.onDrag', 'Desktop.handleOnDropOver'), ('Dock.onDrag', 'Desktop.handleOnDropOver'))
for _c in AUTO['calls']:
    if _c['src'] == 'Desktop.handleOnDropOver':
        e('Desktop.handleOnDropOver@MERGE', _c['dst'], 'CALL', 'the merge branch of handleOnDropOver', guard='the dropped item is an APP or SHORTCUT, the target is an APP, SHORTCUT or GROUP and has fewer than 12 actions',
          evidence='SRC widget/Desktop.java:%d (bytecode)' % _c['line'])
        SUPPRESS.add(('Desktop.handleOnDropOver', _c['dst']))

# ---- taps on the icons
gui('S_HOME_DESKTOP', 'AppItemView$Builder$1.onClick', 'Tap the round "All Apps" button (in the dock after the first start)', evidence='SRC widget/AppItemView.java:285-293; activity/Home.java:263-274; ' + FW_TAP)
e('AppItemView$Builder$1.onClick', 'Home.openAppDrawer(View)', 'CALL', 'Home.launcher.openAppDrawer(view)', guard='Home.launcher != null', evidence='SRC widget/AppItemView.java:285-293')
gui('S_HOME_DESKTOP', 'AppItemView$Builder$2.onClick', 'Tap an app icon on the desktop or in the dock', needs_state=NEED_ITEM, evidence='SRC widget/AppItemView.java:299-312; viewutil/ItemViewFactory.java:56-81; ' + FW_TAP)
for _p in DRAWER_PAGES:
    gui(_p, 'AppItemView$Builder$2.onClick', 'Tap an app in the drawer', evidence='SRC widget/AppDrawer_Paged.java:137-141; widget/AppDrawer_Vertical.java:198-203; ' + FW_TAP)
gui('S_HOME_DESKTOP', 'AppItemView$Builder$4.onClick', 'Tap a shortcut icon on the desktop or in the dock', needs_state=NEED_SHORTCUT, evidence='SRC widget/AppItemView.java:367-383; viewutil/ItemViewFactory.java:179-199; ' + FW_TAP)
e('AppItemView$Builder$2.onClick', 'AppItemView$Builder$2$1.run', 'ASYNC', 'Tool.createScaleInScaleOutAnim posts the end action about 160 ms later', evidence='SRC widget/AppItemView.java:299-312; util/Tool.java:490-502; ' + FW_POST)
e('AppItemView$Builder$4.onClick', 'AppItemView$Builder$4$1.run', 'ASYNC', 'Tool.createScaleInScaleOutAnim posts the end action about 160 ms later', evidence='SRC widget/AppItemView.java:367-383; util/Tool.java:490-502; ' + FW_POST)
e('Tool.createScaleInScaleOutAnim', 'Tool$3.run', 'ASYNC', 'new Handler().postDelayed(runnable, 80)', evidence='SRC util/Tool.java:490-502; ' + FW_POST)
e('Tool$3.run', 'Tool$3$1.run', 'ASYNC', 'the inner Handler.postDelayed(runnable, 80); its run() then calls endAction.run() (the end actions are reached by the ASYNC edges of the click handlers)', evidence='SRC util/Tool.java:492-500; ' + FW_POST)
e('AppItemView$Builder$2$1.run', 'Tool.startApp@OTHER', 'CALL', 'Tool.startApp(context, app) for another app', guard='app.packageName is not com.benny.openlauncher', evidence='SRC widget/AppItemView.java:303-308; util/Tool.java:336-349')
e('AppItemView$Builder$2$1.run', 'Tool.startApp@OLSETTINGS', 'CALL', 'Tool.startApp(context, app) for OpenLauncher itself (shown as "OLSettings")', guard='app.packageName equals com.benny.openlauncher (the Init launcher entry, label "OLSettings")',
  evidence='SRC widget/AppItemView.java:303-308; util/Tool.java:336-339; util/AppManager.java:267-269')
e('Tool.startApp@OTHER', 'S_EXT_APP', 'ENTERS', 'startActivity(ACTION_MAIN, class of the app) with FLAG_ACTIVITY_NEW_TASK', evidence='SRC util/Tool.java:340-345')
e('Tool.startApp@OTHER', 'Tool.toast(Context,int)', 'CALL', 'startActivity threw (the app is gone): toast "This app has uninstalled."', guard='catch (Exception e)', env=ENV_OLD, evidence='SRC util/Tool.java:345-347')
e('Tool.startApp@OLSETTINGS', 'LauncherAction.RunAction@LauncherSettings', 'CALL', 'LauncherAction.RunAction(LauncherSettings, c)', evidence='SRC util/Tool.java:337-339')
sup('Tool.startApp')
e('AppItemView$Builder$4$1.run', 'S_EXT_APP', 'ENTERS', 'view.getContext().startActivity(intent): the shortcut intent opens its target', evidence='SRC widget/AppItemView.java:372-377')

# ---- long-press starts a drag. AppItemView$Builder$3.onLongClick is one method for six kinds of icons; the LongPressCallBack it calls and the drag it starts depend on the icon
NEED_FOLDER_ONE = state_text('A folder shrank to one app (one of the two apps of a folder was dragged out)', ['data'])
LP = {   # variant: (page, LongPressCallBack implementor, GUI text, STATE)
    'APP': ('S_HOME_DESKTOP', 'ItemViewFactory$2', 'Long-press an app icon on the desktop or in the dock', NEED_ITEM),
    'LAUNCHER': ('S_HOME_DESKTOP', 'ItemViewFactory$1', 'Long-press the round "All Apps" button', None),
    'SHORTCUT': ('S_HOME_DESKTOP', 'ItemViewFactory$10', 'Long-press a shortcut icon', NEED_SHORTCUT),
    'GROUP': ('S_HOME_DESKTOP', 'ItemViewFactory$11', 'Long-press a folder icon', NEED_FOLDER),
    'APP_DRAWER': ('S_HOME_DRAWER_PAGED', 'AppDrawer_Paged$Adapter$1', 'Long-press an app in the paged drawer', None),
    'APP_DRAWER_V': ('S_HOME_DRAWER_VERTICAL', 'AppDrawer_Vertical$AppItem$1', 'Long-press an app in the vertical drawer', None),
    'APP_FROM_FOLDER': ('S_HOME_DESKTOP', 'GroupPopupView$8', 'Long-press the single app that is left in a folder', NEED_FOLDER_ONE),
}
DRAG_OF = {'APP': 'APP', 'LAUNCHER': 'LAUNCHER', 'SHORTCUT': 'SHORTCUT', 'GROUP': 'GROUP', 'APP_DRAWER': 'APP_DRAWER', 'APP_DRAWER_V': 'APP_DRAWER', 'APP_FROM_FOLDER': 'APP'}
LP_IMPLS = ('ItemViewFactory$1', 'ItemViewFactory$2', 'ItemViewFactory$10', 'ItemViewFactory$11', 'AppDrawer_Paged$Adapter$1', 'AppDrawer_Vertical$AppItem$1', 'GroupPopupView$8')
for _i in LP_IMPLS:
    sup(('AppItemView$Builder$3.onLongClick', _i + '.readyForDrag'), ('AppItemView$Builder$3.onLongClick', _i + '.afterDrag'))
FW_DRAGDATA_W = ('FW-SRC core/java/android/content/ClipData.java:1076-1099, core/java/android/content/Intent.java:9556-9595, core/java/android/os/Bundle.java:1229, core/java/android/os/BaseBundle.java:1507, '
                 'core/java/android/os/Parcel.java:1673-1697, 1785-1791 (writing the ClipData writes the item Intent, its extras Bundle and every Parcelable value through writeToParcel); '
                 'INFERRED the IWindowSession proxy generated from AIDL writes the ClipData argument of performDrag into the transaction (generated code not read)')
FW_DRAGDATA_R = ('FW-SRC core/java/android/content/Intent.java:7166-7168, core/java/android/os/BaseBundle.java:257-273 (getParcelableExtra reads the extras bundle, which unparcels its map with the class loader set before), '
                 'core/java/android/os/Parcel.java:2744-2745, 2841-2852, 2867-2907 (a parceled Parcelable is read through its static CREATOR field by reflection and createFromParcel)')
for _v, (_page, _impl, _text, _need) in LP.items():
    _n = 'AppItemView$Builder$3.onLongClick@' + _v
    e(_page, _n, 'GUI', _text, gui=[_text], needs_state=_need, evidence='SRC widget/AppItemView.java:319-340; ' + FW_TAP)
    e(_n, _impl + '.readyForDrag', 'CALL', 'eventAction.readyForDrag(view)', evidence='SRC widget/AppItemView.java:323-325')
    e(_n, _impl + '.afterDrag', 'CALL', 'eventAction.afterDrag(view) after the drag has started', guard='readyForDrag returned true', evidence='SRC widget/AppItemView.java:333-335')
    e(_n, 'S_HOME_DRAG@' + DRAG_OF[_v], 'ENTERS', 'view.startDrag(...): the drag of this icon starts', guard='readyForDrag returned true', evidence='SRC widget/AppItemView.java:329-332; ' + FW_DRAG)
    e(_n, 'Desktop$Item.writeToParcel', 'FRAMEWORK', 'the drag data (a ClipData whose Intent holds the item Parcelable) is written to the parcel of performDrag', guard='readyForDrag returned true',
      evidence='SRC widget/AppItemView.java:329-332; widget/Desktop.java:831-848; ' + FW_DRAGDATA_W, cls='standard')
    for _cb in ('onProvideShadowMetrics', 'onDrawShadow'):
        e(_n, 'GoodDragShadowBuilder.' + _cb, 'FRAMEWORK', 'startDrag asks the shadow builder for the drag shadow', guard='readyForDrag returned true', evidence='SRC viewutil/GoodDragShadowBuilder.java:19-28; widget/AppItemView.java:332; ' + FW_DRAG)
ag('AppItemView$Builder$3.onLongClick', 'DragAction.<init>', guard='readyForDrag returned true (the drag starts)')
ag('AppItemView$Builder$3.onLongClick', 'GoodDragShadowBuilder.<init>', guard='readyForDrag returned true (the drag starts)')
# the container that holds the dragged item (dock or desktop) remembers it so a failed drop can be reverted
_AFTER = [('ItemViewFactory$1', state_text('The All Apps button sits on a desktop page (it was dropped there or added with the Action menu)', ['data'])), ('ItemViewFactory$2', None), ('ItemViewFactory$10', None), ('ItemViewFactory$11', None), ('GroupPopupView$8', None)]
for _N, _need in _AFTER:
    for _cont, _st in (('Dock', None), ('Desktop', _need)):
        e(_N + '.afterDrag', _cont + '.setLastItem', 'CALL', 'callBack.setLastItem(item, view): the item was built by the %s, which keeps it for a revert' % _cont.lower(), needs_state=_st,
          guard='the view was built by the ' + _cont.lower(), evidence='SRC viewutil/ItemViewFactory.java:50-53, 72-75, 191-194, 208-211; widget/GroupPopupView.java:278-281')

# ---- while a drag is running: which view gets which drag event (the window manager sends the events, ViewGroup passes them down, each view answers in its OnDragListener / onDragEvent)
TARGET = {'desktop': ('Desktop.onDrag', 'Drag the item over the desktop or drop it there (DRAG_LOCATION / DROP)', 'widget/Desktop.java:160-231'),
          'dock': ('Dock.onDrag', 'Drag the item over the dock or drop it there (DROP)', 'widget/Dock.java:96-147'),
          'delete': ('DragOptionView$1.onDrag', 'Drop the app on "Uninstall" in the top bar', 'widget/DragOptionView.java:86-108'),
          'info': ('DragOptionView$2.onDrag', 'Drop the app on "Info" in the top bar', 'widget/DragOptionView.java:110-141'),
          'remove': ('DragOptionView$3.onDrag', 'Drop the item on "Remove" in the top bar', 'widget/DragOptionView.java:143-170'),
          'left': ('DragNavigationControl$3.onDrag', 'Hold the item at the left screen edge', 'viewutil/DragNavigationControl.java:37-77'),
          'right': ('DragNavigationControl$4.onDrag', 'Hold the item at the right screen edge', 'viewutil/DragNavigationControl.java:78-117')}
for _t, _targets in DROP.items():
    _p = 'S_HOME_DRAG@' + _t
    e(_p, 'DragOptionView.dispatchDragEvent', 'FRAMEWORK', 'DRAG_STARTED and DRAG_ENDED are dispatched to the top bar (the view overrides dispatchDragEvent)', evidence='SRC widget/DragOptionView.java:196-208; ' + FW_DRAG)
    for _k in _targets:
        _node, _text, _ln = TARGET[_k]
        _g = {'remove': 'the Remove icon is visible: the dragged item is not an app in the "Show all apps" desktop style' if _t == 'APP' else None,
              'delete': 'the Uninstall icon is visible (the drag is of an app)', 'info': 'the Info icon is visible (the drag is of an app)'}.get(_k)
        e(_p, _node, 'GUI', _text, gui=[_text], guard=_g, evidence='SRC %s; %s' % (_ln, FW_DRAG))
e('DragOptionView.dispatchDragEvent', 'DragOptionView.onDragEvent', 'CALL', 'onDragEvent(ev) is called for DRAG_STARTED and DRAG_ENDED when super.dispatchDragEvent answered true', guard='r && (ACTION_DRAG_STARTED || ACTION_DRAG_ENDED)',
  evidence='SRC widget/DragOptionView.java:196-208')
e('DragOptionView.onDragEvent', 'S_HOME_DESKTOP', 'ENTERS', 'DRAG_ENDED: the drag is over (dropped, or released over nothing and reverted)', guard='ev.getAction() == ACTION_DRAG_ENDED', evidence='SRC widget/DragOptionView.java:287-307')
ag('DragOptionView.onDragEvent', 'DragOptionView.animShowView', guard='ACTION_DRAG_STARTED for an app, widget, folder, shortcut, launcher or drawer-app drag')

# ================================================================== E. the app drawer: open / close animation, the paged and the vertical style, the search field
DR = 'widget/AppDrawerController.java'
e('Home.openAppDrawer(View,int,int)', 'S_HOME_DRAWER_PAGED', 'ENTERS', 'The circular reveal shows the paged drawer (the default style)', guard='drawerMode == Paged', evidence='SRC activity/Home.java:779-805; %s:63-113, 172-183' % DR)
e('Home.openAppDrawer(View,int,int)', 'S_HOME_DRAWER_VERTICAL', 'ENTERS', 'The circular reveal shows the vertical drawer', guard='drawerMode == Vertical', needs_state=NEED_VERTICAL, evidence='SRC activity/Home.java:779-805; %s:63-113, 184-189' % DR)
e('AppDrawerController.open', 'AppDrawerController$1.onAnimationStart', 'FRAMEWORK', 'appDrawerAnimator.start(): the reveal animator starts', evidence='SRC %s:63-113; ' % DR + INF_CIRC, cls='non_standard', via='CircularReveal library animator calls the AnimatorListener')
e('AppDrawerController.open', 'AppDrawerController$1.onAnimationEnd', 'FRAMEWORK', 'the reveal animator ends', evidence='SRC %s:63-113; ' % DR + INF_CIRC, cls='non_standard', via='CircularReveal library animator calls the AnimatorListener')
e('AppDrawerController.close', 'AppDrawerController$3.run', 'ASYNC', 'paged style: the page fades out, then the end action starts the reveal animator', guard='appDrawerAnimator != null and not running, and drawerMode == Paged', evidence='SRC %s:115-158; ' % DR + FW_ANIM_END)
e('AppDrawerController.close', 'AppDrawerController$4.run', 'ASYNC', 'vertical style: the list fades out, then the end action starts the reveal animator', guard='appDrawerAnimator != null and not running, and drawerMode == Vertical', needs_state=NEED_VERTICAL,
  evidence='SRC %s:115-170; ' % DR + FW_ANIM_END)
for _r in ('AppDrawerController$3.run', 'AppDrawerController$4.run'):
    for _cb in ('onAnimationStart', 'onAnimationEnd'):
        e(_r, 'AppDrawerController$2.' + _cb, 'FRAMEWORK', 'appDrawerAnimator.start(): the hide animator calls its listener', needs_state=NEED_VERTICAL if _r.endswith('$4.run') else None,
          evidence='SRC %s:122-168; ' % DR + INF_CIRC, cls='non_standard', via='CircularReveal library animator calls the AnimatorListener')
sup(('AppDrawerController.open', 'Home$6.onStart'), ('AppDrawerController$1.onAnimationEnd', 'Home$6.onEnd'), ('AppDrawerController$2.onAnimationStart', 'Home$5.onStart'), ('AppDrawerController$2.onAnimationEnd', 'Home$5.onEnd'))
e('Home$6.onStart', 'Home$6$1.run', 'ASYNC', 'appSearchBar.animate()...withEndAction(...) restores the search bar of the desktop when the fade ends', guard='appSearchBar != null (the vertical drawer has its own search card)', needs_state=NEED_VSEARCH,
  evidence='SRC activity/Home.java:352-378; ' + FW_ANIM_END)
e('S_HOME_DRAWER_PAGED', 'AppDrawer_Paged.onConfigurationChanged', 'SYSTEM', 'A configuration change reaches the view (keyboard, screen size or orientation; Home handles these itself)', gui=['Change the device configuration (attach a keyboard, resize the display)'], env=ENV_CONFIG,
  guard='apps != null (the app list was loaded)', evidence='SRC widget/AppDrawer_Paged.java:47-64; AndroidManifest.xml:38-47; ' + FW_CONFIG, cls='standard')
e('S_HOME_DRAWER_VERTICAL', 'AppDrawer_Vertical.onConfigurationChanged', 'SYSTEM', 'A configuration change reaches the view', gui=['Change the device configuration (attach a keyboard, resize the display)'], env=ENV_CONFIG,
  guard='apps != null (the app list was loaded)', evidence='SRC widget/AppDrawer_Vertical.java:82-95; AndroidManifest.xml:38-47; ' + FW_CONFIG, cls='standard')
# the paged drawer: ViewPager of CellContainer pages built by the adapter
e('AppDrawerController.init', 'AppDrawer_Paged.<init>(Context,AttributeSet)', 'FRAMEWORK', 'inflates view_pageddrawer.xml (paged style)', guard='drawerMode == Paged', evidence='SRC %s:172-183; res/layout/view_pageddrawer.xml:2-6; ' % DR + FW_INFLATE,
  cls='non_standard', via='LayoutInflater builds the view class named in the XML layout by reflection')
e('AppDrawerController.init', 'PagerIndicator.<init>(Context,AttributeSet)', 'FRAMEWORK', 'inflates view_drawerindicator.xml (paged style)', guard='drawerMode == Paged', evidence='SRC %s:172-183; res/layout/view_drawerindicator.xml:2; ' % DR + FW_INFLATE,
  cls='non_standard', via='LayoutInflater builds the view class named in the XML layout by reflection')
e('AppDrawerController.init', 'AppDrawer_Vertical.<init>(Context,AttributeSet)', 'FRAMEWORK', 'inflates view_griddrawer.xml (vertical style)', guard='drawerMode == Vertical', needs_state=NEED_VERTICAL,
  evidence='SRC %s:172-190; res/layout/view_griddrawer.xml:2-12; ' % DR + FW_INFLATE, cls='non_standard', via='LayoutInflater builds the view class named in the XML layout by reflection')
e('AppDrawerController.init', 'SearchBar.<init>(Context,AttributeSet)', 'FRAMEWORK', 'inflates view_searchbar_app.xml, which names <SearchBar>', guard='drawerSearchBar && drawerMode == Vertical', needs_state=NEED_VSEARCH,
  evidence='SRC %s:191-203; res/layout/view_searchbar_app.xml:26-33; ' % DR + FW_INFLATE, cls='non_standard', via='LayoutInflater builds the view class named in the XML layout by reflection')
for _cls in ('CellContainer',):
    e('AppDrawer_Paged$Adapter.<init>', 'CellContainer.<init>(Context,AttributeSet)', 'FRAMEWORK', 'inflates item_appdrawer_page.xml, which names <CellContainer>', evidence='SRC widget/AppDrawer_Paged.java:156-159; res/layout/item_appdrawer_page.xml:15; ' + FW_INFLATE,
      cls='non_standard', via='LayoutInflater builds the view class named in the XML layout by reflection')
    e('GroupPopupView.init', 'CellContainer.<init>(Context,AttributeSet)', 'FRAMEWORK', 'inflates view_grouppopup.xml, which names <CellContainer>', guard='not isInEditMode()', evidence='SRC widget/GroupPopupView.java:50-57; res/layout/view_grouppopup.xml:11; ' + FW_INFLATE,
      cls='non_standard', via='LayoutInflater builds the view class named in the XML layout by reflection')
e('AppDrawer_Paged$1.onAppUpdated', 'AppDrawer_Paged$Adapter.getCount', 'FRAMEWORK', 'setAdapter(new Adapter()) reads the page count', evidence='SRC widget/AppDrawer_Paged.java:102-111, 184-187; ' + FW_VP)
for _cb in ('instantiateItem', 'isViewFromObject'):
    e('AppDrawer_Paged$1.onAppUpdated', 'AppDrawer_Paged$Adapter.' + _cb, 'FRAMEWORK', 'the layout of the pager populates it: %s' % _cb, evidence='SRC widget/AppDrawer_Paged.java:189-213; ' + FW_VP)
e('AppDrawer_Paged$1.onAppUpdated', 'AppDrawer_Paged$Adapter.destroyItem', 'FRAMEWORK', 'setAdapter replaces the old adapter: the pager destroys the old pages', needs_state=NEED_LOADED, guard='the pager already had an adapter with pages',
  evidence='SRC widget/AppDrawer_Paged.java:102-111, 194-197; SmoothViewPager.java:427-440')
e('AppDrawer_Paged.resetAdapter', 'AppDrawer_Paged$Adapter.destroyItem', 'FRAMEWORK', 'setAdapter(null) destroys the pages of the old adapter', guard='the old adapter had pages', evidence='SRC widget/AppDrawer_Paged.java:121-124, 194-197; SmoothViewPager.java:427-440')
for _cb in ('onPageSelected', 'onPageScrollStateChanged'):
    gui('S_HOME_DRAWER_PAGED', 'PagerIndicator.' + _cb, 'Swipe the drawer pages left or right', guard='the drawer indicator is registered with the drawer pager; onPageSelected needs two or more drawer pages (more apps than one page holds)',
        evidence='SRC widget/PagerIndicator.java:91-97; ' + FW_VPSCROLL)
gui('S_HOME_DRAWER_PAGED', 'PagerIndicator.onPageScrolled', 'Swipe the drawer pages left or right', evidence='SRC widget/PagerIndicator.java:82-89; ' + FW_VPSCROLL)
# the vertical drawer: the first layout builds the grid; FastAdapter and RecyclerView read the items; the search field filters them
e('AppDrawer_Vertical.<init>(Context,AttributeSet)', 'AppDrawer_Vertical$1.onGlobalLayout', 'FRAMEWORK', 'the first layout pass calls the OnGlobalLayoutListener registered in preInit()', evidence='SRC widget/AppDrawer_Vertical.java:63-80; ' + FW_GLOBALLAYOUT)
for _cb in ('getType', 'getLayoutRes', 'getFactory', 'bindView'):
    e('AppDrawer_Vertical.init', 'AppDrawer_Vertical$AppItem.' + _cb, 'FRAMEWORK', 'the RecyclerView shows the rows: FastAdapter asks the item (%s)' % _cb, evidence='SRC widget/AppDrawer_Vertical.java:167-217; ' + INF_FAST,
      cls='non_standard', via='FastAdapter library calls the item methods')
e('AppDrawer_Vertical.init', 'AppItemView.<init>(Context,AttributeSet)', 'FRAMEWORK', 'the RecyclerView inflates item_app.xml, which names <AppItemView>, for each shown row', evidence='SRC widget/AppDrawer_Vertical.java:167-229; res/layout/item_app.xml:2-4; ' + FW_INFLATE + '; ' + INF_FAST,
  cls='non_standard', via='LayoutInflater builds the view class named in the XML layout by reflection')
gui('S_HOME_DRAWER_VERTICAL', 'AppDrawer_Vertical$GridAppDrawerAdapter.getCharacterForElement', 'Drag the scroll bar at the right edge', needs_state=NEED_VERTICAL, evidence='SRC widget/AppDrawer_Vertical.java:159-165; INFERRED the DragScrollBar library asks the INameableAdapter for the letter of an element (library source not read)',
  cls='non_standard', via='DragScrollBar library calls the INameableAdapter')
gui('S_HOME_DRAWER_VERTICAL', 'SearchBar.onClick', 'Tap the search field: it takes focus and the keyboard opens', needs_state=NEED_VSEARCH, evidence='SRC widget/SearchBar.java:57-64; ' + FW_TAP)
gui('S_HOME_DRAWER_VERTICAL', 'SearchBar.onKeyPreIme', 'Press Back while the keyboard is open (the field is cleared)', needs_state=NEED_VSEARCH, evidence='SRC widget/SearchBar.java:45-55; INFERRED the view root hands key events to the focused view before the input method (ViewRootImpl not read)')
gui('S_HOME_DRAWER_VERTICAL', 'SearchBar.onEditorAction', 'Press the action key of the keyboard', needs_state=NEED_VSEARCH, evidence='SRC widget/SearchBar.java:40-43; INFERRED the input method sends the editor action to the focused TextView (IME not read)')
for _t in ('APP_DRAWER',):
    e('S_HOME_DRAG@' + _t, 'SearchBar.onDragEvent', 'FRAMEWORK', 'DRAG_STARTED reaches the visible search field while the vertical drawer closes', needs_state=NEED_VSEARCH, evidence='SRC widget/SearchBar.java:35-38; ' + FW_DRAG)
for _cb in ('beforeTextChanged', 'onTextChanged', 'afterTextChanged'):
    gui('S_HOME_DRAWER_VERTICAL', 'AppDrawerController.' + _cb, 'Type in the drawer search field', needs_state=NEED_VSEARCH, evidence='SRC widget/AppDrawerController.java:199-204, 247-266; ' + FW_TEXT)
e('AppDrawerController.onTextChanged', 'AppDrawer_Vertical$GridAppDrawerAdapter$1.filter', 'FRAMEWORK', 'gridDrawerAdapter.filter(text) runs the filter predicate for every item', guard='drawerMode == Vertical and gridDrawerAdapter != null',
  needs_state=NEED_VSEARCH, evidence='SRC widget/AppDrawerController.java:252-261; widget/AppDrawer_Vertical.java:150-157; ' + INF_FAST, cls='non_standard', via='FastAdapter library calls the filter predicate')

# ================================================================== F. the folder popup (GroupPopupView)
GP = 'widget/GroupPopupView.java'
gui('S_HOME_DESKTOP', 'ItemViewFactory$12.onClick', 'Tap a folder icon', needs_state=NEED_FOLDER, evidence='SRC viewutil/ItemViewFactory.java:224-231; ' + FW_TAP)
e('GroupPopupView.showWindowV', 'S_HOME_GROUP_POPUP', 'ENTERS', 'the folder card is added with the apps of the folder and its title', guard='getVisibility() != VISIBLE (a popup is not showing yet; otherwise showWindowV returns false)', evidence='SRC %s:96-258' % GP)
gui('S_HOME_GROUP_POPUP', 'GroupPopupView$2.onClick', 'Tap outside the folder card', evidence='SRC %s:67-76; ' % GP + FW_TAP)
e('GroupPopupView$2.onClick', 'S_HOME_DESKTOP', 'ENTERS', 'the popup closes', evidence='SRC %s:67-76' % GP)
e('GroupPopupView.dismissPopup', 'GroupPopupView$7.onDismiss', 'CALL', 'dismissListener.onDismiss(): the label and the folder icon are restored', guard='dismissListener != null (set by showWindowV)', evidence='SRC %s:87-94, 204-213' % GP)
e('GroupPopupView$2.onClick', 'GroupPopupView$7.onDismiss', 'CALL', 'dismissListener.onDismiss() before dismissPopup()', guard='dismissListener != null', evidence='SRC %s:67-76, 204-213' % GP)
e('GroupPopupView.dismissPopup', 'S_HOME_DESKTOP', 'ENTERS', 'the popup is hidden', evidence='SRC %s:87-94' % GP)
e('GroupPopupView.init', 'GroupPopupView$1.run', 'ASYNC', 'postDelayed(..., 2000) sets the title and background colours', evidence='SRC %s:59-66; ' % GP + FW_POST)
gui('S_HOME_GROUP_POPUP', 'GroupPopupView$3.onLongClick', 'Long-press an app or shortcut in the folder (drags it out)', evidence='SRC %s:128-148; ' % GP + FW_TAP)
e('GroupPopupView$3.onLongClick', 'S_HOME_DRAG@APP', 'ENTERS', 'itemView.startDrag(ACTION_APP): the app leaves the folder and is dragged', guard='act.getStringExtra("shortCutIconID") == null', evidence='SRC %s:134-139; ' % GP + FW_DRAG)
e('GroupPopupView$3.onLongClick', 'S_HOME_DRAG@SHORTCUT', 'ENTERS', 'itemView.startDrag(ACTION_SHORTCUT): the shortcut leaves the folder and is dragged', guard='act.getStringExtra("shortCutIconID") != null', needs_state=NEED_GRIDGROUP,
  evidence='SRC %s:140-144; ' % GP + FW_DRAG)
e('GroupPopupView$3.onLongClick', 'Desktop$Item.writeToParcel', 'FRAMEWORK', 'the drag data is written to the parcel of performDrag', evidence='SRC %s:134-144; widget/Desktop.java:831-848; ' % GP + FW_DRAGDATA_W, cls='standard')
for _cb in ('onProvideShadowMetrics', 'onDrawShadow'):
    e('GroupPopupView$3.onLongClick', 'GoodDragShadowBuilder.' + _cb, 'FRAMEWORK', 'startDrag asks the shadow builder for the drag shadow', evidence='SRC viewutil/GoodDragShadowBuilder.java:19-28; %s:139, 143; ' % GP + FW_DRAG)
gui('S_HOME_GROUP_POPUP', 'GroupPopupView$4.onClick', 'Tap an app in the folder', evidence='SRC %s:149-167; ' % GP + FW_TAP)
gui('S_HOME_GROUP_POPUP', 'GroupPopupView$5.onClick', 'Tap a shortcut in the folder', needs_state=NEED_GRIDGROUP, evidence='SRC %s:168-182; ' % GP + FW_TAP)
e('GroupPopupView$4.onClick', 'GroupPopupView$4$1.run', 'ASYNC', 'Tool.createScaleInScaleOutAnim posts the end action about 160 ms later', evidence='SRC %s:154-166; util/Tool.java:490-502; ' % GP + FW_POST)
e('GroupPopupView$5.onClick', 'GroupPopupView$5$1.run', 'ASYNC', 'Tool.createScaleInScaleOutAnim posts the end action about 160 ms later', needs_state=NEED_GRIDGROUP, evidence='SRC %s:169-181; util/Tool.java:490-502; ' % GP + FW_POST)
e('GroupPopupView$4$1.run', 'Tool.startApp@OTHER', 'CALL', 'Tool.startApp(c, app)', guard='app.packageName is not com.benny.openlauncher', evidence='SRC %s:157-164; util/Tool.java:336-349' % GP)
e('GroupPopupView$4$1.run', 'Tool.startApp@OLSETTINGS', 'CALL', 'Tool.startApp(c, app) for OpenLauncher itself ("OLSettings")', guard='app.packageName equals com.benny.openlauncher', evidence='SRC %s:157-164; util/Tool.java:336-339' % GP)
e('GroupPopupView$5$1.run', 'S_EXT_APP', 'ENTERS', 'view.getContext().startActivity(act): the shortcut opens its target', needs_state=NEED_GRIDGROUP, evidence='SRC %s:172-180' % GP)
gui('S_HOME_GROUP_POPUP', 'GroupPopupView$6.onClick', 'Tap the folder title', evidence='SRC %s:187-202; ' % GP + FW_TAP)
e('GroupPopupView$6.onClick', 'S_DLG_RENAME_GROUP', 'ENTERS', 'Tool.DialogHelper.promptInputText(...).show(): the rename dialog', evidence='SRC %s:187-202; util/Tool.java:463-475; ' % GP + INF_MD)
gui('S_DLG_RENAME_GROUP', 'Tool$DialogHelper$1.onInput', 'Type a new name and tap "OK"', evidence='SRC util/Tool.java:466-471; ' + INF_MD, cls='non_standard', via='MaterialDialogs library calls the InputCallback')
e('Tool$DialogHelper$1.onInput', 'S_HOME_GROUP_POPUP', 'ENTERS', 'the folder is renamed; the popup stays', evidence='SRC %s:190-199' % GP)
e('GroupPopupView.showWindowV', 'GroupPopupView$GroupDef.<clinit>', 'CALL', 'class initialisation on first use (GroupDef.getCellSize, maxItem)', evidence='SRC %s:292-310; ' % GP + FW_CLINIT)

# ================================================================== G. the minibar (left drawer), its rows and popup windows
e('S_HOME_DESKTOP', 'Home.onDrawerStateChanged', 'GUI', 'Swipe in from the left screen edge: the DrawerLayout starts to move and settles open', gui=['Swipe in from the left screen edge'],
  guard='generalSettings.minBarEnable is true (the default; the drawer is locked closed otherwise)', evidence='SRC activity/Home.java:235, 544, 857-878; res/layout/activity_home.xml:5-32; ' + INF_DRAWER, cls='non_standard', via='DrawerLayout library calls the DrawerListener')
for _cb in ('onDrawerSlide', 'onDrawerOpened'):
    gui('S_HOME_DESKTOP', 'Home.' + _cb, 'Swipe in from the left screen edge', guard='minBarEnable is true', evidence='SRC activity/Home.java:235, 845-855; ' + INF_DRAWER, cls='non_standard', via='DrawerLayout library calls the DrawerListener')
e('Home.onDrawerStateChanged', 'Home$12.run', 'ASYNC', 'the overlay layout fades out first (withEndAction hides it)', guard='newState is STATE_DRAGGING or STATE_SETTLING and shortcutLayout.getAlpha() == 1', evidence='SRC activity/Home.java:859-869; ' + FW_ANIM_END)
e('Home.onDrawerStateChanged', 'S_HOME_MINIBAR', 'ENTERS', 'STATE_IDLE with the left drawer open: the overlay layout is shown and the minibar is open', guard='newState == STATE_IDLE and drawerLayout.isDrawerOpen(Gravity.LEFT)', evidence='SRC activity/Home.java:870-875')
gui('S_HOME_MINIBAR', 'Home.onDrawerClosed', 'Swipe the minibar back to the left', evidence='SRC activity/Home.java:235, 853-855; ' + INF_DRAWER, cls='non_standard', via='DrawerLayout library calls the DrawerListener')
e('Home.onDrawerClosed', 'S_HOME_DESKTOP', 'ENTERS', 'the minibar is closed', evidence='SRC activity/Home.java:853-855')
gui('S_HOME_MINIBAR', 'SwipeListView.dispatchTouchEvent', 'Touch the minibar list', evidence='SRC widget/SwipeListView.java:70-74; ' + FW_TOUCH)
for _cb in ('getCount', 'getItemId', 'getView'):
    e('Home.initMinBar', 'IconListAdapter.' + _cb, 'FRAMEWORK', 'minBar.setAdapter(...): the ListView reads the rows (%s)' % _cb, evidence='SRC activity/Home.java:583-584; viewutil/IconListAdapter.java:27-56; ' + FW_ADAPTER)
e('SwipeListView.init', 'SwipeListView$1.onFling', 'FRAMEWORK', 'the GestureDetector calls onFling when a touch ends with enough velocity', guard='Math.abs(dx) > dis && Math.abs(dy) < vDis; the touch is processed by dispatchTouchEvent',
  evidence='SRC widget/SwipeListView.java:42-74; ' + FW_FLING)
ROWV = [('EditMinBar', 'Change the layout of the minibar', 'pencil'), ('SetWallpaper', 'Set and blur the wallpaper', 'photo'), ('LockScreen', 'Lock the screen', 'padlock'),
        ('ClearRam', 'Clear RAM', 'donut chart'), ('DeviceSettings', 'Device settings', 'gear in a window'), ('LauncherSettings', 'Launcher settings', 'launcher gear'),
        ('VolumeDialog', 'Volume dialog', 'speaker'), ('OpenAppDrawer', 'Open the app drawer', 'grid of dots')]   # the rows show an icon only (IconListAdapter.getView leaves the text empty)
for _v, _lab, _icon in ROWV:
    e('S_HOME_MINIBAR', 'Home$11.onItemClick@' + _v, 'GUI', 'Tap the minibar row "%s" (%s icon)' % (_lab, _icon), gui=['Tap the %s icon in the minibar ("%s")' % (_icon, _lab)],
      guard='the row is enabled in the minibar arrangement (all eight are, by default)', evidence='SRC activity/Home.java:591-607; util/LauncherAction.java:29-39; viewutil/IconListAdapter.java:39-56; ' + FW_ADAPTER)
    e('Home$11.onItemClick@' + _v, 'LauncherAction.RunAction@' + _v, 'CALL', 'LauncherAction.RunAction(action, Home.this)', evidence='SRC activity/Home.java:594-595')
    if _v not in ('EditMinBar', 'LauncherSettings', 'DeviceSettings'):
        e('Home$11.onItemClick@' + _v, 'S_HOME_DESKTOP', 'ENTERS', 'drawerLayout.closeDrawers(): the minibar closes after this action', guard='action is not EditMinBar, LauncherSettings or DeviceSettings', evidence='SRC activity/Home.java:596-606')
sup('Home$11.onItemClick')
# fling to the right on a row shows a popup window (only ClearRam and VolumeDialog have one)
for _v, _pg in (('CLEARRAM', 'S_MINIBAR_POPUP@CLEARRAM'), ('VOLUME', 'S_MINIBAR_POPUP@VOLUME'), ('OTHER', None)):
    _n = 'Home$10.onSwipe@' + _v
    _lab = {'CLEARRAM': 'the donut icon (Clear RAM)', 'VOLUME': 'the speaker icon (Volume dialog)', 'OTHER': 'another icon (these rows have no popup window)'}[_v]
    e('SwipeListView$1.onFling', _n, 'CALL', 'onSwipeRight.onSwipe(pos, x, y) for the row: ' + _lab, gui=['Fling right on %s in the minibar' % _lab],
      guard='velocityX > 0, |dx| > 10 dp, |dy| < 30 dp, pointToPosition != -1 and onSwipeRight != null', evidence='SRC widget/SwipeListView.java:47-66')
    e(_n, 'MiniPopupView.showActionWindow@' + _v, 'CALL', 'miniPopup.showActionWindow(Action.valueOf(label), x, y)', evidence='SRC activity/Home.java:585-590')
    if _pg:
        e('MiniPopupView.showActionWindow@' + _v, _pg, 'ENTERS', 'displayWindow adds the popup window to the layer', evidence='SRC widget/MiniPopupView.java:52-122')
sup('Home$10.onSwipe', 'MiniPopupView.showActionWindow')
e('MiniPopupView.showActionWindow@CLEARRAM', 'MiniPopupView$ClearRamViewHolder.<init>', 'CALL', 'new ClearRamViewHolder(window)', guard='action == ClearRam', evidence='SRC widget/MiniPopupView.java:57-60')
e('MiniPopupView.showActionWindow@CLEARRAM', 'Tool.getFreeRAM', 'CALL', 'the free RAM text', guard='action == ClearRam', evidence='SRC widget/MiniPopupView.java:60')
e('MiniPopupView.showActionWindow@CLEARRAM', 'Tool.getFreeMemory', 'CALL', 'the free storage text', guard='action == ClearRam', evidence='SRC widget/MiniPopupView.java:61')
e('MiniPopupView.showActionWindow@VOLUME', 'MiniPopupView$VolumeDialogViewHolder.<init>', 'CALL', 'new VolumeDialogViewHolder(window)', guard='action == VolumeDialog', evidence='SRC widget/MiniPopupView.java:71-74')
e('MiniPopupView.showActionWindow@VOLUME', 'MiniPopupView$VolumeDialogViewHolder.getSoundChangeListener', 'CALL', 'the four sliders get a listener', guard='action == VolumeDialog', evidence='SRC widget/MiniPopupView.java:85-88')
for _v in ('CLEARRAM', 'VOLUME', 'OTHER'):
    e('MiniPopupView.showActionWindow@' + _v, 'MiniPopupView.displayWindow', 'CALL', 'displayWindow(window, x, y) (a null window closes all windows)', evidence='SRC widget/MiniPopupView.java:91')
e('MiniPopupView.displayWindow', 'MiniPopupView$1.onGlobalLayout', 'FRAMEWORK', 'the added window is laid out: the listener positions it', guard='window != null', evidence='SRC widget/MiniPopupView.java:98-122; ' + FW_GLOBALLAYOUT)
for _h, _ln in (('MiniPopupView$ClearRamViewHolder', '163-172'), ('MiniPopupView$VolumeDialogViewHolder', '124-136')):
    e(_h + '.<init>', _h + '$$ViewBinder.<init>', 'FRAMEWORK', 'ButterKnife.bind(this, view) creates the generated binder', evidence='SRC widget/MiniPopupView.java:%s; ' % _ln + INF_BK, cls='non_standard', via='ButterKnife: the generated binder is loaded by name')
    e(_h + '.<init>', _h + '$$ViewBinder.bind', 'FRAMEWORK', 'ButterKnife.bind(this, view) calls bind', evidence='SRC widget/MiniPopupView.java:%s; ' % _ln + INF_BK, cls='non_standard', via='ButterKnife: the generated binder is loaded by name')
    e(_h + '$$ViewBinder.bind', _h + '$$ViewBinder.createUnbinder', 'CALL', 'bind creates the unbinder', evidence=INF_GEN, cls='explicit')
    e(_h + '$$ViewBinder.createUnbinder', _h + '$$ViewBinder$InnerUnbinder.<init>', 'CALL', 'createUnbinder builds the InnerUnbinder', evidence=INF_GEN, cls='explicit')
    sup((_h + '$$ViewBinder.bind', _h + '$$ViewBinder.createUnbinder'), (_h + '$$ViewBinder.createUnbinder', _h + '$$ViewBinder$InnerUnbinder.<init>'))
for _pg in ('S_MINIBAR_POPUP@CLEARRAM', 'S_MINIBAR_POPUP@VOLUME'):
    gui(_pg, 'MiniPopupView.onTouchEvent', 'Touch anywhere: the popup closes', evidence='SRC widget/MiniPopupView.java:40-50; ' + FW_TOUCH)
    e(_pg, 'S_HOME_MINIBAR', 'ENTERS', 'the popup closes (closeAllWindow)', evidence='SRC widget/MiniPopupView.java:40-50, 94-96')
e('MiniPopupView.onTouchEvent', 'MiniPopupView.closeAllWindow', 'CALL', 'closeAllWindow() while a popup window is displayed', guard='haveWidowDisplayed', evidence='SRC widget/MiniPopupView.java:40-50')
for _cb in ('onProgressChanged', 'onStartTrackingTouch', 'onStopTrackingTouch'):
    gui('S_MINIBAR_POPUP@VOLUME', 'MiniPopupView$VolumeDialogViewHolder$1.' + _cb, 'Drag one of the four volume sliders', evidence='SRC widget/MiniPopupView.java:138-159; INFERRED the SeekBar calls its OnSeekBarChangeListener while the user drags (SeekBar source not read)')

# ================================================================== H. LauncherAction.RunAction: one variant per action (the switch on the action)
LA = 'util/LauncherAction.java'
BACK_DLG = ('FW-SRC core/java/android/app/Dialog.java:352-358, 597-604, 626-633, 650-654, 1231-1238 (the Back key is tracked on key down; on key up onBackPressed cancels the dialog while it is cancelable, '
            'and cancel() sends the cancel message and calls dismiss()); INFERRED the MaterialDialog library builds an android.app.Dialog subclass and keeps the cancelable default (library source not read)')
e('LauncherAction.RunAction@EditMinBar', 'MinibarEditActivity.<init>', 'INTENT', 'context.startActivity(new Intent(context, MinibarEditActivity.class))', evidence='SRC %s:43-46; ' % LA + FW_LAUNCH)
# set wallpaper: a list dialog with two items
e('LauncherAction.RunAction@SetWallpaper', 'LauncherAction$1.<init>', 'CALL', 'new MaterialDialog.ListCallback() for b.itemsCallback(...)', evidence='SRC %s:48-71' % LA)
e('LauncherAction.RunAction@SetWallpaper', 'S_DLG_WALLPAPER', 'ENTERS', 'b.show(): the dialog "Wallpaper" with the items "Set wallpaper" and "Blur"', evidence='SRC %s:47-72; ' % LA + INF_MD)
gui('S_DLG_WALLPAPER', 'LauncherAction$1.onSelection', 'Tap "Set wallpaper" or "Blur" in the dialog', evidence='SRC %s:53-70; ' % LA + INF_MD, cls='non_standard', via='MaterialDialogs library calls the ListCallback')
e('S_DLG_WALLPAPER', 'S_HOME_DESKTOP', 'ENTERS', 'Press Back: the dialog is dismissed', gui=['Press Back'], evidence=BACK_DLG)
e('LauncherAction$1.onSelection', 'S_EXT_SYSTEM', 'ENTERS', 'startActivity(Intent.createChooser(ACTION_SET_WALLPAPER)): the system wallpaper chooser', guard='position == 0 ("Set wallpaper")', evidence='SRC %s:57-60' % LA)
e('LauncherAction$1.onSelection', 'S_HOME_DESKTOP', 'ENTERS', 'the dialog closes after the item was handled (MaterialDialogs dismisses on item selection)', evidence='SRC %s:53-70; ' % LA + INF_MD)
e('LauncherAction$1.onSelection', 'Tool.drawableToBitmap', 'CALL', 'StackBlur.blur(Tool.drawableToBitmap(context.getWallpaper()), 10, false)', guard='position == 1 ("Blur")', evidence='SRC %s:61-63' % LA)
e('LauncherAction$1.onSelection', 'Tool.toast(Context,String)', 'CALL', 'the blur threw: toast "Unable to blur wallpaper"', guard='position == 1 and the try block threw (catch Exception)', env=ENV_WALLPAPER, evidence='SRC %s:62-66' % LA)
# lock screen: DevicePolicyManager.lockNow() throws unless OpenLauncher is an active device administrator (the default is not)
e('LauncherAction.RunAction@LockScreen', 'Tool.toast(Context,String)', 'CALL', 'lockNow() threw (OpenLauncher is not an active device administrator, the default): toast "please enable device admin"',
  guard='catch (Exception e) around lockNow()', evidence='SRC %s:73-77' % LA)
e('LauncherAction.RunAction@LockScreen', 'S_EXT_SYSTEM', 'ENTERS', 'lockNow() threw: startActivity opens com.android.settings.DeviceAdminSettings', guard='catch (Exception e) around lockNow()', evidence='SRC %s:76-81' % LA)
e('LauncherAction.RunAction@LockScreen', 'S_EXT_SYSTEM', 'ENTERS', 'lockNow() succeeded: the screen is locked and the lock screen shows', guard='no exception from lockNow()', env=ENV_ADMIN_OK, evidence='SRC %s:73-75' % LA)
# clear RAM: one AsyncTask at a time (the static flag clearingRam)
e('LauncherAction.RunAction@ClearRam', 'LauncherAction$2.<init>', 'CALL', 'new AsyncTask<Void, Void, Void>() {...}', guard='clearingRam is false', evidence='SRC %s:83-90' % LA)
e('LauncherAction.RunAction@ClearRam', 'LauncherAction$2.onPreExecute', 'FRAMEWORK', 'execute(): onPreExecute sets clearingRam', guard='clearingRam is false', evidence='SRC %s:90-95, 121; ' % LA + FW_ASYNC_PRE)
e('LauncherAction.RunAction@ClearRam', 'LauncherAction$2.doInBackground', 'ASYNC', 'execute(): the worker kills background processes and runs the garbage collector', guard='clearingRam is false', evidence='SRC %s:96-107, 121; ' % LA + FW_ASYNC)
e('LauncherAction$2.doInBackground', 'LauncherAction$2.onPostExecute', 'ASYNC', 'the worker is done: onPostExecute runs on the main thread', evidence='SRC %s:109-120; ' % LA + FW_ASYNC)
e('LauncherAction$2.onPostExecute', 'Tool.toast(Context,String)', 'CALL', 'toast with the free RAM (both branches of the if show a toast)', evidence='SRC %s:115-118' % LA)
# device settings, launcher settings, volume, app drawer
e('LauncherAction.RunAction@DeviceSettings', 'S_EXT_SYSTEM', 'ENTERS', 'startActivity(new Intent(Settings.ACTION_SETTINGS)): the system settings', evidence='SRC %s:123-125' % LA,
  cls='non_standard', via='implicit intent: Settings.ACTION_SETTINGS is resolved to the system Settings app by action name, not by an explicit component')
e('LauncherAction.RunAction@LauncherSettings', 'SettingsActivity.<init>', 'INTENT', 'context.startActivity(new Intent(context, SettingsActivity.class))', evidence='SRC %s:126-128; ' % LA + FW_LAUNCH)
e('LauncherAction.RunAction@VolumeDialog', 'S_EXT_SYSTEM', 'ENTERS', 'setStreamVolume(STREAM_RING, current, FLAG_SHOW_UI): the system shows its volume panel', evidence='SRC %s:129-132' % LA)
e('LauncherAction.RunAction@OpenAppDrawer', 'Home.openAppDrawer()', 'CALL', 'Home.launcher.openAppDrawer()', guard='Home.launcher != null', evidence='SRC %s:133-135' % LA)

# ================================================================== I. widgets: the system picker, the configure screen of the chosen widget, and the result
INF_PICK = 'INFERRED the system widget picker (another package, not read) returns RESULT_OK with EXTRA_APPWIDGET_ID when the user chooses a widget'
INF_CFG = 'INFERRED the configure activity of the widget (another package, not read) returns RESULT_OK, or RESULT_CANCELED with the widget id, when the user leaves it'
e('Home.pickWidget', 'S_EXT_WIDGET_PICKER', 'ENTERS', 'startActivityForResult(ACTION_APPWIDGET_PICK): the system widget picker opens', evidence='SRC activity/Home.java:647-652')
e('S_EXT_WIDGET_PICKER', 'Home.onActivityResult@PICKED', 'RESULT', 'the user chose a widget: the picker finishes with RESULT_OK and the widget id', gui=['Choose a widget in the system picker'], env=ENV_PICKER,
  guard='resultCode == RESULT_OK and requestCode == REQUEST_PICK_APPWIDGET', evidence='SRC activity/Home.java:706-713; ' + FW_RESULT + '; ' + INF_PICK)
e('S_EXT_WIDGET_PICKER', 'Home.onActivityResult@CONFIGURED', 'RESULT', 'the configure screen of the widget finishes with RESULT_OK', gui=['Finish the configure screen of the widget'], env=ENV_PICKER_CFG,
  guard='resultCode == RESULT_OK and requestCode == REQUEST_CREATE_APPWIDGET', evidence='SRC activity/Home.java:706-713; ' + FW_RESULT + '; ' + INF_CFG)
e('S_EXT_WIDGET_PICKER', 'Home.onActivityResult@CANCEL', 'RESULT', 'the picker or the configure screen finishes with RESULT_CANCELED and the widget id: the reserved id is released', gui=['Press Back in the configure screen of the widget'], env=ENV_PICKER_CFG,
  guard='resultCode == RESULT_CANCELED && data != null && the extra widget id != -1', evidence='SRC activity/Home.java:714-720; ' + FW_RESULT + '; ' + INF_CFG)
e('Home.onActivityResult@PICKED', 'Home.configureWidget', 'CALL', 'configureWidget(data)', guard='requestCode == REQUEST_PICK_APPWIDGET', evidence='SRC activity/Home.java:709-710')
e('Home.onActivityResult@CONFIGURED', 'Home.createWidget', 'CALL', 'createWidget(data)', guard='requestCode == REQUEST_CREATE_APPWIDGET', evidence='SRC activity/Home.java:711-712')
e('Home.onActivityResult@CANCEL', 'S_HOME_DESKTOP', 'ENTERS', 'the user is back on the desktop (the reserved widget id was deleted)', evidence='SRC activity/Home.java:714-720')
e('Home.configureWidget', 'S_EXT_WIDGET_PICKER', 'ENTERS', 'startActivityForResult(ACTION_APPWIDGET_CONFIGURE): the configure screen of the widget opens', guard='appWidgetInfo.configure != null', env=ENV_PICKER_CFG,
  evidence='SRC activity/Home.java:654-662')
e('Home.configureWidget', 'Home.createWidget', 'CALL', 'createWidget(data) at once when the widget has no configure activity', guard='appWidgetInfo.configure == null', evidence='SRC activity/Home.java:657-665')
e('Home.createWidget', 'S_HOME_DESKTOP', 'ENTERS', 'the widget item is added to the current desktop page and shown when Home resumes', evidence='SRC activity/Home.java:668-682')
# ================================================================== J. Settings: SettingsActivity, MaterialPrefFragment (vendored library, part of this build) and the dialog pickers (DialogUtils)
MPF = 'libs/materialpreffragment/src/main/java/com/bennyv5/materialpreffragment/MaterialPrefFragment.java'
BSA = 'libs/materialpreffragment/src/main/java/com/bennyv5/materialpreffragment/BaseSettingsActivity.java'
MPF_ONCLICK = ('SRC %s:360-373 (ButtonPref.onCreateView sets the click listener to the fragment itself) and %s:113-119 '
               '(onClick reads the pref id tag and calls the registered OnPrefClickedListener)' % (MPF, MPF))
MPF_ONCHANGE_TB = 'SRC %s:155-176 (TBPref.onCreateView: the Switch calls the registered OnPrefChangedListener when toggled)' % MPF
MPF_NUM = 'SRC %s:272-304 (NUMPref.onCreateView: the button shows a MaterialDialog with one SeekBar per item; OK saves every item and calls the OnPrefChangedListener)' % MPF
MPF_COLOR = ('SRC %s:318-340 (ColorPref.onCreateView: the button opens a ColorChooserDialog) and %s:17-21 '
             '(BaseSettingsActivity.onColorSelection calls the OnPrefChangedListener when a color is picked)' % (MPF, BSA))
MPF_ATTACH = 'SRC activity/SettingsActivity.java:41-51; ' + INF_FRAG

e('LauncherAction.RunAction@LauncherSettings', 'SettingsActivity.onCreate', 'LIFECYCLE', 'the system creates SettingsActivity, then calls onCreate', evidence='SRC activity/SettingsActivity.java:28-29; ' + FW_LAUNCH)
e('SettingsActivity.onCreate', 'Tool.setTheme', 'CALL', 'Tool.setTheme(this) (the body is commented out: a no-op on this build)', evidence='SRC activity/SettingsActivity.java:30; util/Tool.java:436-445')
e('SettingsActivity.onCreate', 'S_SETTINGS_ROOT', 'ENTERS', 'MaterialPrefFragment.newInstance(...) with the 7 category buttons is added to the layout (getSupportFragmentManager().add)',
  evidence='SRC activity/SettingsActivity.java:33-51; ' + MPF_ATTACH, cls='non_standard', via='MaterialPrefFragment library (vendored, compiled into this build) builds the button list from the layout XML')

SS_CATS = [  # pref id tapped on the root screen, settingsCategory index, the sub-screen, its title string
    ('desktopSettings', 0, 'S_SETTINGS_DESKTOP', 'Desktop'),
    ('dockSettings', 1, 'S_SETTINGS_DOCK', 'Dock'),
    ('drawerSettings', 2, 'S_SETTINGS_DRAWER', 'Drawer'),
    ('inputSettings', 3, 'S_SETTINGS_INPUT', 'Gestures'),
    ('colorsSettings', 4, 'S_SETTINGS_COLORS', 'Colors'),
    ('iconsSettings', 5, 'S_SETTINGS_ICONS', 'Icons'),
    ('otherSettings', 6, 'S_SETTINGS_OTHER', 'Other'),
]
for _ssid, _ssidx, _ssscr, _sslab in SS_CATS:
    e('S_SETTINGS_ROOT', 'SettingsActivity.onPrefClicked@' + _ssid, 'GUI', 'Tap "%s" on the Settings root screen' % _sslab, gui=['Tap "%s"' % _sslab],
      guard="id == '%s'" % _ssid, evidence='SRC activity/SettingsActivity.java:41-49, 302-324; ' + MPF_ONCLICK,
      cls='non_standard', via='MaterialPrefFragment library (vendored) calls the OnPrefClickedListener when a ButtonPref is tapped')
    e('SettingsActivity.onPrefClicked@' + _ssid, 'SettingsActivity.onSettingsSelected@%d' % _ssidx, 'CALL', 'onSettingsSelected(%d)' % _ssidx,
      guard="id == '%s'" % _ssid, evidence='SRC activity/SettingsActivity.java:304-324')
    e('SettingsActivity.onSettingsSelected@%d' % _ssidx, _ssscr, 'ENTERS', 'the %s sub-screen fragment replaces the root list (fragment transaction, added to the back stack)' % _sslab,
      guard='settingsCategory == %d' % _ssidx, evidence='SRC activity/SettingsActivity.java:54-138')
# Press Back on a sub-screen pops the fragment back stack to the root; on the root it finishes the activity
for _ssid, _ssidx, _ssscr, _sslab in SS_CATS:
    gui(_ssscr, 'SettingsActivity.onBackPressed@SUB', 'Press Back on the %s sub-screen' % _sslab, kind='SYSTEM', evidence='SRC activity/SettingsActivity.java:378-382; ' + FW_BACK)
gui('S_SETTINGS_ROOT', 'SettingsActivity.onBackPressed@ROOT', 'Press Back on the Settings root screen', kind='SYSTEM', evidence='SRC activity/SettingsActivity.java:378-382; ' + FW_BACK)
e('SettingsActivity.onBackPressed@SUB', 'S_SETTINGS_ROOT', 'ENTERS', 'super.onBackPressed() pops the fragment back stack to the root list', evidence='SRC activity/SettingsActivity.java:379-381')
e('SettingsActivity.onBackPressed@ROOT', 'SettingsActivity.onDestroy', 'SYSTEM', 'the root screen has no more back stack: super.onBackPressed() finishes the activity, which the system then destroys',
  evidence='SRC activity/SettingsActivity.java:379-381; ' + FW_STOP)
sup('SettingsActivity.onBackPressed')

# ---- the actions of each sub-screen (ButtonPref -> onPrefClicked@id; TBPref -> onPrefChanged@id directly, no screen change; NUMPref/ColorPref -> a dialog, no app callback until committed)
e('S_SETTINGS_DESKTOP', 'SettingsActivity.onPrefClicked@editMiniBar', 'GUI', 'Tap "Minibar" on Settings > Desktop', gui=['Tap "Minibar"'], guard="id == 'editMiniBar'",
  evidence='SRC activity/SettingsActivity.java:59-60, 331-333; ' + MPF_ONCLICK, cls='non_standard', via='MaterialPrefFragment library calls the OnPrefClickedListener')
e('SettingsActivity.onPrefClicked@editMiniBar', 'LauncherAction.RunAction@EditMinBar', 'CALL', "LauncherAction.RunAction(Action.EditMinBar, this)", guard="id == 'editMiniBar'", evidence='SRC activity/SettingsActivity.java:331-333')
e('S_SETTINGS_DESKTOP', 'SettingsActivity.onPrefClicked@desktopMode', 'GUI', 'Tap "Desktop style" on Settings > Desktop', gui=['Tap "Desktop style"'], guard="id == 'desktopMode'",
  evidence='SRC activity/SettingsActivity.java:61-62, 341-344; ' + MPF_ONCLICK, cls='non_standard', via='MaterialPrefFragment library calls the OnPrefClickedListener')
e('SettingsActivity.onPrefClicked@desktopMode', 'DialogUtils.desktopStylePicker', 'CALL', 'DialogUtils.desktopStylePicker(this)', guard="id == 'desktopMode'", evidence='SRC activity/SettingsActivity.java:341-344')
e('S_SETTINGS_DRAWER', 'SettingsActivity.onPrefClicked@drawerStyle', 'GUI', 'Tap "Drawer style" on Settings > Drawer', gui=['Tap "Drawer style"'], guard="id == 'drawerStyle'",
  evidence='SRC activity/SettingsActivity.java:85, 337-340; ' + MPF_ONCLICK, cls='non_standard', via='MaterialPrefFragment library calls the OnPrefClickedListener')
e('SettingsActivity.onPrefClicked@drawerStyle', 'DialogUtils.appDrawerStylePicker', 'CALL', 'DialogUtils.appDrawerStylePicker(this)', guard="id == 'drawerStyle'", evidence='SRC activity/SettingsActivity.java:337-340')
GEST_PICK = [('singleClick', 'DialogUtils.startSingleClickPicker', 'Single tap', 101, 345), ('doubleClick', 'DialogUtils.startDoubleClickPicker', 'Double tap', 102, 348),
             ('pinch', 'DialogUtils.startPinchPicker', 'Pinch', 103, 351), ('unPinch', 'DialogUtils.startUnpinchPicker', 'Un-pinch', 104, 354),
             ('swipeDown', 'DialogUtils.startSwipeDownPicker', 'Swipe down', 105, 357), ('swipeUp', 'DialogUtils.startSwipeUpPicker', 'Swipe up', 106, 360)]
for _gid, _gfn, _glab, _gln, _gcall in GEST_PICK:
    e('S_SETTINGS_INPUT', "SettingsActivity.onPrefClicked@" + _gid, 'GUI', 'Tap "%s" on Settings > Gestures' % _glab, gui=['Tap "%s"' % _glab], guard="id == '%s'" % _gid,
      evidence='SRC activity/SettingsActivity.java:%d, %d-%d; ' % (_gln, _gcall, _gcall + 1) + MPF_ONCLICK, cls='non_standard', via='MaterialPrefFragment library calls the OnPrefClickedListener')
    e("SettingsActivity.onPrefClicked@" + _gid, _gfn, 'CALL', '%s(this)' % _gfn, guard="id == '%s'" % _gid, evidence='SRC activity/SettingsActivity.java:%d-%d' % (_gcall, _gcall + 1))
e('S_SETTINGS_ICONS', 'SettingsActivity.onPrefClicked@iconPack', 'GUI', 'Tap "Icon pack" on Settings > Icons', gui=['Tap "Icon pack"'], guard="id == 'iconPack'",
  evidence='SRC activity/SettingsActivity.java:123, 334-336; ' + MPF_ONCLICK, cls='non_standard', via='MaterialPrefFragment library calls the OnPrefClickedListener')
e('SettingsActivity.onPrefClicked@iconPack', 'AppManager.startPickIconPackIntent', 'CALL', 'AppManager.getInstance(this).startPickIconPackIntent(this)', guard="id == 'iconPack'", evidence='SRC activity/SettingsActivity.java:334-336')
e('S_SETTINGS_ICONS', 'SettingsActivity.onPrefClicked@iconHide', 'GUI', 'Tap "Hide apps" on Settings > Icons', gui=['Tap "Hide apps"'], guard="id == 'iconHide'",
  evidence='SRC activity/SettingsActivity.java:124, 363-367; ' + MPF_ONCLICK, cls='non_standard', via='MaterialPrefFragment library calls the OnPrefClickedListener')
e('SettingsActivity.onPrefClicked@iconHide', 'HideAppsActivity.<init>', 'INTENT', 'startActivity(new Intent(SettingsActivity.this, HideAppsActivity.class))', guard="id == 'iconHide'",
  evidence='SRC activity/SettingsActivity.java:364-366; ' + FW_LAUNCH)
e('S_SETTINGS_OTHER', 'SettingsActivity.onPrefClicked@backup', 'GUI', 'Tap "Backup / Restore" on Settings > Other', gui=['Tap "Backup / Restore"'], guard="id == 'backup'",
  evidence='SRC activity/SettingsActivity.java:130, 368-374; ' + MPF_ONCLICK, cls='non_standard', via='MaterialPrefFragment library calls the OnPrefClickedListener')
e('SettingsActivity.onPrefClicked@backup', 'DialogUtils.backupDialog', 'CALL', 'checkSelfPermission(READ_EXTERNAL_STORAGE) is granted: DialogUtils.backupDialog(this)', guard="id == 'backup' and the permission is already granted",
  env=ENV_PERM_STORAGE, evidence='SRC activity/SettingsActivity.java:369-370')
e('SettingsActivity.onPrefClicked@backup', 'S_PERMISSION', 'ENTERS', 'the permission is not granted: ActivityCompat.requestPermissions(READ_EXTERNAL_STORAGE)', guard="id == 'backup' and the permission is not granted",
  evidence='SRC activity/SettingsActivity.java:371-373; ' + FW_PERM)
e('S_SETTINGS_OTHER', 'SettingsActivity.onPrefClicked@restart', 'GUI', 'Tap "Restart" on Settings > Other', gui=['Tap "Restart"'], guard="id == 'restart'",
  evidence='SRC activity/SettingsActivity.java:131, 325-330; ' + MPF_ONCLICK, cls='non_standard', via='MaterialPrefFragment library calls the OnPrefClickedListener')
e('SettingsActivity.onPrefClicked@restart', 'Home.<init>', 'SYSTEM', 'Home.launcher.recreate(): the launcher relaunches', guard="id == 'restart' and Home.launcher != null", evidence='SRC activity/SettingsActivity.java:326-328; ' + FW_RELAUNCH)
e('SettingsActivity.onPrefClicked@restart', 'SettingsActivity.onDestroy', 'SYSTEM', 'finish(): SettingsActivity is destroyed', guard="id == 'restart'", evidence='SRC activity/SettingsActivity.java:329; ' + FW_STOP)
sup('SettingsActivity.onPrefClicked')

# ---- NUMPref / ColorPref dialogs (one screen reused for several ids) and the plain toggle switches (TBPref -> onPrefChanged directly, no screen change)
NUM_SITES = [('gridSizeDesktop', 'S_SETTINGS_DESKTOP', 'Desktop size'), ('gridSizeDock', 'S_SETTINGS_DOCK', 'Dock size'), ('gridSize', 'S_SETTINGS_DRAWER', 'Drawer size'), ('iconSize', 'S_SETTINGS_ICONS', 'Icon size')]
for _nid, _nscr, _nlab in NUM_SITES:
    e(_nscr, 'S_DLG_NUMPREF', 'ENTERS', 'Tap "%s" (a NUMPref button, library-managed: no app method sits between the tap and the dialog)' % _nlab, gui=['Tap "%s"' % _nlab], guard="id == '%s'" % _nid, evidence=MPF_NUM,
      cls='non_standard', via='MaterialPrefFragment library opens the seek-bar dialog')
COLOR_SITES = [('dockBackground', 'S_SETTINGS_DESKTOP', 'Dock background'), ('drawerBackground', 'S_SETTINGS_DRAWER', 'Drawer background'), ('drawerCardBackground', 'S_SETTINGS_DRAWER', 'Drawer card background'),
               ('folderColor', 'S_SETTINGS_COLORS', 'Folder color'), ('drawerLabelColor', 'S_SETTINGS_COLORS', 'Drawer label color')]
for _cid, _cscr, _clab in COLOR_SITES:
    e(_cscr, 'S_DLG_COLOR', 'ENTERS', 'Tap "%s" (a ColorPref button, library-managed: no app method sits between the tap and the dialog)' % _clab, gui=['Tap "%s"' % _clab], guard="id == '%s'" % _cid, evidence=MPF_COLOR,
      cls='non_standard', via='MaterialPrefFragment library opens the ColorChooserDialog')
e('S_DLG_NUMPREF', 'S_SETTINGS_DESKTOP', 'ENTERS', 'OK saves the values and calls onPrefChanged; Cancel or Back dismisses with no change', evidence=MPF_NUM)
e('S_DLG_COLOR', 'S_SETTINGS_DRAWER', 'ENTERS', 'picking a color calls onColorSelection, which calls onPrefChanged; Cancel or Back dismisses with no change', evidence=MPF_COLOR)
gui('S_SETTINGS_DESKTOP', 'SettingsActivity.onPrefChanged', 'Toggle a switch (desktopSearchBar shown here), or commit a NUMPref/ColorPref dialog', guard="id == 'desktopSearchBar' (one of 23 ids the switch handles)",
    evidence='SRC activity/SettingsActivity.java:162-289; ' + MPF_ONCHANGE_TB, cls='non_standard', via='MaterialPrefFragment library calls the OnPrefChangedListener')
e('SettingsActivity.onPrefChanged', 'SettingsActivity.prepareRestart', 'CALL', 'most branches end with prepareRestart() (sets requireLauncherRestart)', evidence='SRC activity/SettingsActivity.java:178, 191, etc.')
e('SettingsActivity.onDestroy', 'Home.<init>', 'SYSTEM', 'requireLauncherRestart was set: Home.launcher.recreate()', guard='requireLauncherRestart && Home.launcher != null', needs_state=state_text(
    'A setting that needs a restart was changed in this SettingsActivity instance (requireLauncherRestart)', ['session']), evidence='SRC activity/SettingsActivity.java:296-298; ' + FW_RELAUNCH)
e('SettingsActivity.onDestroy', 'S_HOME_PAUSED', 'ENTERS', 'requireLauncherRestart is false (or Home.launcher is null): SettingsActivity simply finishes', evidence='SRC activity/SettingsActivity.java:295-299; ' + FW_STOP)

# ---- the Info menu item and AboutActivity (a 3rd-party library, materialaboutlibrary, not vendored: its own calls stay INFERRED)
INF_ABOUT = 'INFERRED MaterialAboutActivity (materialaboutlibrary, not vendored) calls getActivityTitle and getMaterialAboutList from its own onCreate, and onOptionsItemSelected overrides its handling of the Up button (library source not read)'
gui('S_SETTINGS_ROOT', 'SettingsActivity.onOptionsItemSelected@INFO', 'Tap the overflow menu, then "Info"', guard='item id == R.id.launcherInfo', evidence='SRC activity/SettingsActivity.java:141-144, 149-153; res/menu/settings_options.xml', cls='standard')
e('SettingsActivity.onOptionsItemSelected@INFO', 'SettingsActivity.onCreateOptionsMenu', 'CALL', 'the toolbar inflates settings_options.xml the first time the menu is shown', evidence='SRC activity/SettingsActivity.java:141-144; res/menu/settings_options.xml', cls='standard')
e('SettingsActivity.onOptionsItemSelected@INFO', 'AboutActivity.<init>', 'INTENT', 'startActivity(new Intent(this, AboutActivity.class))', guard='item id == R.id.launcherInfo', evidence='SRC activity/SettingsActivity.java:150-152; ' + FW_LAUNCH)
gui('S_SETTINGS_ROOT', 'SettingsActivity.onOptionsItemSelected@HOME', 'Tap the toolbar Up arrow', guard='item id == android.R.id.home', evidence='SRC activity/SettingsActivity.java:154-156', cls='standard')
e('SettingsActivity.onOptionsItemSelected@HOME', 'SettingsActivity.onBackPressed@ROOT', 'CALL', 'onBackPressed()', guard='item id == android.R.id.home', evidence='SRC activity/SettingsActivity.java:155')
sup('SettingsActivity.onOptionsItemSelected')
e('AboutActivity.<init>', 'S_ABOUT', 'ENTERS', 'MaterialAboutActivity.onCreate builds the title/team/credit cards from getMaterialAboutList', evidence='SRC activity/AboutActivity.java:18-77; ' + INF_ABOUT)
e('AboutActivity.<init>', 'AboutActivity.getActivityTitle', 'FRAMEWORK', 'MaterialAboutActivity.onCreate calls getActivityTitle for the toolbar title', evidence='SRC activity/AboutActivity.java:86-89; ' + INF_ABOUT, cls='non_standard', via='materialaboutlibrary calls the overridden methods')
e('AboutActivity.<init>', 'AboutActivity.getMaterialAboutList', 'FRAMEWORK', 'MaterialAboutActivity.onCreate calls getMaterialAboutList to build the cards', evidence='SRC activity/AboutActivity.java:18-77; ' + INF_ABOUT, cls='non_standard', via='materialaboutlibrary calls the overridden methods')
gui('S_ABOUT', 'AboutActivity.onOptionsItemSelected', 'Tap the toolbar Up arrow', guard='item id == android.R.id.home', evidence='SRC activity/AboutActivity.java:80-83', cls='standard')
e('AboutActivity.onOptionsItemSelected', 'S_SETTINGS_ROOT', 'ENTERS', 'onBackPressed() finishes AboutActivity', guard='item id == android.R.id.home', evidence='SRC activity/AboutActivity.java:81-82; ' + FW_BACK)

# ---- DialogUtils gesture / style / backup dialogs
e('DialogUtils.desktopStylePicker', 'DialogUtils$1.<init>', 'CALL', 'new MaterialDialog.ListCallbackSingleChoice() {...}', evidence='SRC util/DialogUtils.java:19-30')
e('DialogUtils.desktopStylePicker', 'S_DLG_DESKTOP_STYLE', 'ENTERS', 'b.show(): single-choice list Normal / Show all apps', evidence='SRC util/DialogUtils.java:19-30; ' + INF_MD)
gui('S_DLG_DESKTOP_STYLE', 'DialogUtils$1.onSelection', 'Tap "Normal" or "Show all apps"', evidence='SRC util/DialogUtils.java:23-28; ' + INF_MD, cls='non_standard', via='MaterialDialogs library calls the ListCallbackSingleChoice')
e('DialogUtils$1.onSelection', 'LauncherSettings.switchDesktopMode', 'CALL', 'LauncherSettings.getInstance(context).switchDesktopMode(position)', evidence='SRC util/DialogUtils.java:26')
e('LauncherSettings.switchDesktopMode', 'LauncherSettings.checkIconCacheIDs', 'CALL', 'every existing desktop/dock item is checked for a cached shortcut icon', evidence='SRC util/LauncherSettings.java:186-194')
e('LauncherSettings.switchDesktopMode', 'Tool.checkForUnusedIconAndDelete', 'CALL', 'icon files not referenced by any item are deleted from the cache', evidence='SRC util/LauncherSettings.java:202')
e('DialogUtils$1.onSelection', 'S_SETTINGS_DESKTOP', 'ENTERS', 'the dialog closes after the selection (MaterialDialogs dismisses on single-choice tap)', evidence='SRC util/DialogUtils.java:19-30; ' + INF_MD)

e('DialogUtils.appDrawerStylePicker', 'DialogUtils$2.<init>', 'CALL', 'new MaterialDialog.ListCallbackSingleChoice() {...}', evidence='SRC util/DialogUtils.java:32-50')
e('DialogUtils.appDrawerStylePicker', 'AppDrawerController$DrawerMode.<clinit>', 'CALL', 'AppDrawerController.DrawerMode.values() (class init on first use)', evidence='SRC util/DialogUtils.java:33-40; ' + FW_CLINIT)
e('DialogUtils.appDrawerStylePicker', 'S_DLG_DRAWER_STYLE', 'ENTERS', 'b.show(): single-choice list Paged / Vertical', evidence='SRC util/DialogUtils.java:32-50; ' + INF_MD)
gui('S_DLG_DRAWER_STYLE', 'DialogUtils$2.onSelection', 'Tap "Paged" or "Vertical"', evidence='SRC util/DialogUtils.java:45-49; ' + INF_MD, cls='non_standard', via='MaterialDialogs library calls the ListCallbackSingleChoice')
e('DialogUtils$2.onSelection', 'S_SETTINGS_DRAWER', 'ENTERS', 'the drawerMode field is updated; prepareRestart() was already called by onPrefClicked; the dialog closes', evidence='SRC util/DialogUtils.java:45-49; ' + INF_MD)

GEST_DLG = [('startSingleClickPicker', 3, 'singleClick', 'setSingleClickGesture', '53-64'), ('startDoubleClickPicker', 4, 'doubleClick', 'setDoubleClickGesture', '66-77'),
            ('startPinchPicker', 5, 'pinch', 'setPinchGesture', '79-90'), ('startUnpinchPicker', 6, 'unPinch', 'setUnPinchGesture', '92-103'),
            ('startSwipeDownPicker', 7, 'swipeDown', 'setSwipeDownGesture', '105-116'), ('startSwipeUpPicker', 8, 'swipeUp', 'setSwipeUpGesture', '118-129')]
for _fn, _dn, _fld, _setter, _ln in GEST_DLG:
    e('DialogUtils.' + _fn, 'DialogUtils$%d.<init>' % _dn, 'CALL', 'new MaterialDialog.ListCallbackSingleChoice() {...}', evidence='SRC util/DialogUtils.java:%s' % _ln)
    e('DialogUtils.' + _fn, 'S_DLG_GESTURE@' + _fld, 'ENTERS', 'b.show(): single-choice list of gesture actions (None, Minibar, Wallpaper, Lock, Clear RAM, Device settings, Launcher settings, Volume, App drawer)',
      evidence='SRC util/DialogUtils.java:%s; res/values/arrays.xml:13-23; ' % _ln + INF_MD)
    gui('S_DLG_GESTURE@' + _fld, 'DialogUtils$%d.onSelection' % _dn, 'Tap a gesture action', evidence='SRC util/DialogUtils.java:%s; ' % _ln + INF_MD, cls='non_standard', via='MaterialDialogs library calls the ListCallbackSingleChoice')
    e('DialogUtils$%d.onSelection' % _dn, 'LauncherSettings.' + _setter, 'CALL', 'LauncherSettings.getInstance(context).%s(position)' % _setter, evidence='SRC util/DialogUtils.java:%s' % _ln)
    e('DialogUtils$%d.onSelection' % _dn, 'S_SETTINGS_INPUT', 'ENTERS', 'the dialog closes after the selection', evidence='SRC util/DialogUtils.java:%s; ' % _ln + INF_MD)

e('DialogUtils.backupDialog', 'DialogUtils$9.<init>', 'CALL', 'new MaterialDialog.ListCallback() {...}', evidence='SRC util/DialogUtils.java:140-182')
e('DialogUtils.backupDialog', 'S_DLG_BACKUP', 'ENTERS', 'b.show(): the list "Backup" / "Restore" with a Cancel button', evidence='SRC util/DialogUtils.java:131-184; ' + INF_MD)
gui('S_DLG_BACKUP', 'DialogUtils$9.onSelection', 'Tap "Backup" or "Restore"', evidence='SRC util/DialogUtils.java:140-182; ' + INF_MD, cls='non_standard', via='MaterialDialogs library calls the ListCallback')
e('DialogUtils$9.onSelection', 'DialogUtils.copy', 'CALL', 'copy(context, src, dst) for each of the three data files',
  guard='the package info lookup (and, for the second/third call, the earlier copy calls) do not throw (catch (Exception) around each branch)', evidence='SRC util/DialogUtils.java:153-158, 169-173')
e('DialogUtils$9.onSelection', 'S_SETTINGS_OTHER', 'ENTERS', '"Backup" finishes with a toast (success or failure, the catch only shows a toast); the dialog closes. Restore never reaches this state: System.exit(1) at line 179 runs unconditionally after the Restore try/catch, whether or not the copy threw', guard='item is "Backup"', evidence='SRC util/DialogUtils.java:146-163')
e('DialogUtils$9.onSelection', 'S_EXIT', 'ENTERS', '"Restore": System.exit(1) kills the process (unconditionally, whether or not the copy threw - the catch only shows a toast and exit() is after the try/catch) so the restored files (or the pre-existing ones, if the copy failed) are read on the next cold start', guard='item is "Restore"', evidence='SRC util/DialogUtils.java:164-180')
e('DialogUtils.copy', 'Tool.print(Object)', 'CALL', 'Tool.print("deleted") / Tool.print("copied")', evidence='SRC util/DialogUtils.java:194, 209')
sup('DialogUtils.copy')

# ================================================================== K. HideAppsActivity / HideAppsFragment (Settings > Icons > Hide apps)
e('HideAppsActivity.<init>', 'HideAppsActivity.onCreate', 'LIFECYCLE', 'the system creates HideAppsActivity, then calls onCreate', evidence='SRC activity/HideAppsActivity.java:24-26; ' + FW_LAUNCH)
e('HideAppsActivity.onCreate', 'HideAppsActivity.setupViewPager', 'CALL', 'setupViewPager(viewPager)', evidence='SRC activity/HideAppsActivity.java:33-34')
e('HideAppsActivity.setupViewPager', 'HideAppsActivity$ViewPagerAdapter.<init>', 'CALL', 'new ViewPagerAdapter(getSupportFragmentManager())', evidence='SRC activity/HideAppsActivity.java:51')
e('HideAppsActivity.setupViewPager', 'HideAppsActivity$ViewPagerAdapter.addFragment', 'CALL', 'adapter.addFragment(new HideAppsFragment(), "Skip")', evidence='SRC activity/HideAppsActivity.java:52')
e('HideAppsActivity$ViewPagerAdapter.addFragment', 'HideAppsFragment.<init>', 'CALL', 'new HideAppsFragment()', evidence='SRC activity/HideAppsActivity.java:52')
e('HideAppsFragment.<init>', 'HideAppsFragment.<clinit>', 'LIFECYCLE', 'class init on first use (TAG, DEBUG)', evidence='SRC fragment/HideAppsFragment.java:45-46; ' + FW_CLINIT)
INF_VPFRAG = ('INFERRED the support FragmentPagerAdapter calls getCount, getItem and getPageTitle when the ViewPager first lays out, and the FragmentManager then drives the lifecycle '
              'of the fragment it returns (support library source not read)')
e('HideAppsActivity.setupViewPager', 'HideAppsActivity$ViewPagerAdapter.getCount', 'FRAMEWORK', 'viewPager.setAdapter(adapter): the pager reads the page count', evidence='SRC activity/HideAppsActivity.java:53; ' + INF_VPFRAG, cls='non_standard', via='support FragmentPagerAdapter')
e('HideAppsActivity.setupViewPager', 'HideAppsActivity$ViewPagerAdapter.getItem', 'FRAMEWORK', 'the first layout populates page 0: getItem(0) returns the HideAppsFragment', evidence='SRC activity/HideAppsActivity.java:53, 74-77; ' + INF_VPFRAG, cls='non_standard', via='support FragmentPagerAdapter')
e('HideAppsActivity.setupViewPager', 'HideAppsActivity$ViewPagerAdapter.getPageTitle', 'FRAMEWORK', 'the tab strip (none shown here) would read the page title', evidence='SRC activity/HideAppsActivity.java:53, 89-93; ' + INF_VPFRAG, cls='non_standard', via='support FragmentPagerAdapter')
e('HideAppsActivity$ViewPagerAdapter.getItem', 'HideAppsFragment.onCreateView', 'FRAMEWORK', 'the FragmentManager attaches the returned fragment and calls onCreateView', evidence=INF_FRAG, cls='non_standard', via='support FragmentManager drives the fragment lifecycle')
e('HideAppsFragment.onCreateView', 'HideAppsFragment$1.<init>', 'CALL', 'fab.setOnClickListener(new View.OnClickListener() {...})', evidence='SRC fragment/HideAppsFragment.java:58-64')
e('HideAppsFragment.onCreateView', 'HideAppsFragment$AsyncWorkerList.<init>', 'CALL', 'the field taskList = new AsyncWorkerList() runs when HideAppsFragment is constructed, not here; execute() is called once the view is created', evidence='SRC fragment/HideAppsFragment.java:42, 66-69', note='field initialiser runs in the constructor; the edge is drawn from onCreateView for readability')
e('HideAppsFragment.onCreateView', 'HideAppsFragment$AsyncWorkerList.onPreExecute', 'ASYNC', 'taskList.execute(): onPreExecute runs on the calling thread', guard='taskList.getStatus() == PENDING (first time)', evidence='SRC fragment/HideAppsFragment.java:66-69; ' + FW_ASYNC_PRE)
e('HideAppsFragment$AsyncWorkerList.onPreExecute', 'HideAppsFragment$AsyncWorkerList.doInBackground', 'ASYNC', 'the worker thread runs next', evidence='SRC fragment/HideAppsFragment.java:84-105; ' + FW_ASYNC)
e('HideAppsFragment$AsyncWorkerList.doInBackground', 'HideAppsFragment.prepareData', 'CALL', 'prepareData() compares the installed apps to the stored hidden list', evidence='SRC fragment/HideAppsFragment.java:96-104, 161-173')
e('HideAppsFragment.prepareData', 'AppManager.getNonFilteredApps', 'CALL', 'AppManager.getInstance(getContext()).getNonFilteredApps()', evidence='SRC fragment/HideAppsFragment.java:162')
e('HideAppsFragment$AsyncWorkerList.doInBackground', 'HideAppsFragment$AsyncWorkerList.onPostExecute', 'ASYNC', 'the worker is done: onPostExecute runs on the main thread', evidence='SRC fragment/HideAppsFragment.java:107-114; ' + FW_ASYNC)
e('HideAppsFragment$AsyncWorkerList.onPostExecute', 'HideAppsFragment.populateView', 'CALL', 'populateView() builds the ListView and its adapter', evidence='SRC fragment/HideAppsFragment.java:107-114, 176-208')
e('HideAppsFragment.populateView', 'HideAppsFragment$AppAdapter.<init>', 'CALL', 'new AppAdapter(getActivity(), list_activities_final)', evidence='SRC fragment/HideAppsFragment.java:183')
e('HideAppsFragment.populateView', 'HideAppsFragment$3.<init>', 'CALL', 'grid.setOnItemClickListener(new AdapterView.OnItemClickListener() {...})', evidence='SRC fragment/HideAppsFragment.java:186-207')
e('HideAppsFragment.onCreateView', 'S_HIDEAPPS_LOADING', 'ENTERS', 'the ViewSwitcher shows its first child (a progress view) while the AsyncTask runs', evidence='SRC fragment/HideAppsFragment.java:54-56, 66-76; res/layout/request.xml')
e('HideAppsFragment$AsyncWorkerList.onPostExecute', 'S_HIDEAPPS_LIST', 'ENTERS', 'switcherLoad.showNext(): the checkable app list is shown', evidence='SRC fragment/HideAppsFragment.java:109-113')
gui('S_HIDEAPPS_LIST', 'HideAppsFragment$AppAdapter.getView', 'The list shows a row', evidence='SRC fragment/HideAppsFragment.java:210-256; ' + FW_ADAPTER, cls='standard')
gui('S_HIDEAPPS_LIST', 'HideAppsFragment$3.onItemClick', 'Tap an app row to toggle it', evidence='SRC fragment/HideAppsFragment.java:186-207; ' + FW_ADAPTER)
gui('S_HIDEAPPS_LIST', 'HideAppsFragment$1.onClick', 'Tap the floating confirm button', evidence='SRC fragment/HideAppsFragment.java:58-64; ' + FW_TAP)
e('HideAppsFragment$1.onClick', 'HideAppsFragment.confirmSelection', 'CALL', 'confirmSelection()', evidence='SRC fragment/HideAppsFragment.java:62')
e('HideAppsFragment.confirmSelection', 'HideAppsFragment$2.<init>', 'CALL', 'new Thread() {...}.start()', evidence='SRC fragment/HideAppsFragment.java:124-154')
e('HideAppsFragment$2.<init>', 'HideAppsFragment$2.run', 'FRAMEWORK', 'Thread.start() calls run() on a new thread', evidence='SRC fragment/HideAppsFragment.java:155-158; INFERRED java.lang.Thread.start() calls run() (libcore source not read)', cls='non_standard', via='java.lang.Thread')
e('HideAppsFragment$2.run', 'HideAppsFragment$2$1.<init>', 'CALL', 'Snackbar.make(...).setAction(label, new View.OnClickListener() {...}): the app registers the action listener directly (not a library/reflection link)',
  guard='no app is selected (selected == 0)', needs_state=state_text('Every app row is left unchecked (the default: none was tapped, or all were tapped back off)', ['session']),
  evidence='SRC fragment/HideAppsFragment.java:139-148', cls='explicit')
e('HideAppsFragment$2.run', 'S_HIDEAPPS_SNACKBAR', 'ENTERS', 'no app is selected: the snackbar "select at least one app" with OK is shown', guard='selected == 0', evidence='SRC fragment/HideAppsFragment.java:139-148')
gui('S_HIDEAPPS_SNACKBAR', 'HideAppsFragment$2$1.onClick', 'Tap "OK" on the snackbar', evidence='SRC fragment/HideAppsFragment.java:142-147; ' + FW_TAP, cls='non_standard', via='Snackbar (support library) calls the action OnClickListener')
e('HideAppsFragment$2$1.onClick', 'HideAppsActivity.onDestroy', 'SYSTEM', 'getActivity().finish(): HideAppsActivity is destroyed', evidence='SRC fragment/HideAppsFragment.java:145; ' + FW_STOP)
e('HideAppsFragment$2.run', 'HideAppsActivity.onDestroy', 'SYSTEM', 'at least one app is selected: getActivity().finish() at once', guard='selected > 0', evidence='SRC fragment/HideAppsFragment.java:150-151; ' + FW_STOP)
e('HideAppsActivity.onDestroy', 'AppManager.getAllApps', 'CALL', 'AppManager.getInstance(this).init() reloads the app list with the new hidden list', evidence='SRC activity/HideAppsActivity.java:44-47')
gui('S_HIDEAPPS_LIST', 'HideAppsActivity.onOptionsItemSelected', 'Tap the toolbar Up arrow', guard='item id == android.R.id.home', evidence='SRC activity/HideAppsActivity.java:56-64', cls='standard')
e('HideAppsActivity.onOptionsItemSelected', 'HideAppsActivity.onDestroy', 'SYSTEM', 'onBackPressed() finishes the activity', guard='item id == android.R.id.home', evidence='SRC activity/HideAppsActivity.java:59-61; ' + FW_BACK)
e('HideAppsActivity.onDestroy', 'S_SETTINGS_ICONS', 'ENTERS', 'HideAppsActivity finishes; Settings > Icons resumes', evidence='SRC activity/HideAppsActivity.java:43-48; ' + FW_STOP)
e('HideAppsFragment.onSaveInstanceState', 'HideAppsFragment.onSaveInstanceState', 'LIFECYCLE', 'placeholder', evidence='SRC fragment/HideAppsFragment.java:118-121')
sup(('HideAppsFragment.onSaveInstanceState', 'HideAppsFragment.onSaveInstanceState'))
gui('S_HIDEAPPS_LIST', 'HideAppsFragment.onSaveInstanceState', 'Rotate the device or switch apps while Hide apps is open (the fragment may be asked to save its state)', env=ENV_CONFIG, evidence='SRC fragment/HideAppsFragment.java:117-121; ' + INF_FRAG)

# ================================================================== L. MinibarEditActivity (Settings > Desktop > Minibar, or the minibar row "Minibar Settings")
e('LauncherAction.RunAction@EditMinBar', 'MinibarEditActivity.onCreate', 'LIFECYCLE', 'the system creates MinibarEditActivity, then calls onCreate', evidence='SRC activity/MinibarEditActivity.java:36-37; ' + FW_LAUNCH)
e('MinibarEditActivity.onCreate', 'Tool.setTheme', 'CALL', 'Tool.setTheme(this) (the body is commented out: a no-op)', evidence='SRC activity/MinibarEditActivity.java:47; util/Tool.java:436-445')
e('MinibarEditActivity.onCreate', 'MinibarEditActivity$$ViewBinder.<init>', 'FRAMEWORK', 'ButterKnife.bind(this) creates the generated binder', evidence='SRC activity/MinibarEditActivity.java:51; ' + INF_BK, cls='non_standard', via='ButterKnife: the generated binder is loaded by name')
e('MinibarEditActivity.onCreate', 'MinibarEditActivity$$ViewBinder.bind', 'FRAMEWORK', 'ButterKnife.bind(this) calls bind', evidence='SRC activity/MinibarEditActivity.java:51; ' + INF_BK, cls='non_standard', via='ButterKnife: the generated binder is loaded by name')
e('MinibarEditActivity$$ViewBinder.bind', 'MinibarEditActivity$$ViewBinder.createUnbinder', 'CALL', 'bind creates the unbinder', evidence=INF_GEN, cls='explicit')
e('MinibarEditActivity$$ViewBinder.createUnbinder', 'MinibarEditActivity$$ViewBinder$InnerUnbinder.<init>', 'CALL', 'createUnbinder builds the InnerUnbinder', evidence=INF_GEN, cls='explicit')
sup(('MinibarEditActivity$$ViewBinder.bind', 'MinibarEditActivity$$ViewBinder.createUnbinder'), ('MinibarEditActivity$$ViewBinder.createUnbinder', 'MinibarEditActivity$$ViewBinder$InnerUnbinder.<init>'),
    'MinibarEditActivity$$ViewBinder$InnerUnbinder.unbind()')
e('MinibarEditActivity.onCreate', 'MinibarEditActivity$Item.<init>', 'CALL', 'adapter.add(new Item(i, item, enabled)) for each of the 8 rows of miniBarArrangement', evidence='SRC activity/MinibarEditActivity.java:67-73')
e('MinibarEditActivity$Item.<init>', 'MinibarEditActivity$Item.<clinit>', 'LIFECYCLE', 'class init on first Item (the static FACTORY field)', evidence='SRC activity/MinibarEditActivity.java:119-129, 141; ' + FW_CLINIT)
e('MinibarEditActivity.onCreate', 'MinibarEditActivity$1.<init>', 'CALL', 'enableSwitch.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {...})', evidence='SRC activity/MinibarEditActivity.java:78-88')
e('MinibarEditActivity.onCreate', 'S_MINIBAR_EDIT', 'ENTERS', 'the on/off switch and the draggable row list are shown', evidence='SRC activity/MinibarEditActivity.java:46-91')
gui('S_MINIBAR_EDIT', 'MinibarEditActivity$1.onCheckedChanged', 'Toggle the minibar on/off switch', evidence='SRC activity/MinibarEditActivity.java:78-88; INFERRED SwitchCompat calls its OnCheckedChangeListener (support library source not read)', cls='non_standard', via='support SwitchCompat calls the OnCheckedChangeListener')
e('MinibarEditActivity.onCreate', 'MinibarEditActivity$Item.getType', 'FRAMEWORK', 'rv.setAdapter(adapter): FastAdapter shows the 8 rows', evidence='SRC activity/MinibarEditActivity.java:57-65, 131-168; ' + INF_FAST, cls='non_standard', via='FastAdapter library calls the item methods')
for _mcb in ('getLayoutRes', 'getFactory', 'bindView'):
    e('MinibarEditActivity$Item.getType', 'MinibarEditActivity$Item.' + _mcb, 'FRAMEWORK', 'FastAdapter asks the item for %s' % _mcb, evidence='SRC activity/MinibarEditActivity.java:131-168; ' + INF_FAST, cls='non_standard', via='FastAdapter library calls the item methods')
e('MinibarEditActivity$Item.getFactory', 'MinibarEditActivity$Item$ItemFactory.<init>', 'CALL', 'the static FACTORY field holds one ItemFactory', evidence='SRC activity/MinibarEditActivity.java:141')
e('MinibarEditActivity$Item.getFactory', 'MinibarEditActivity$Item$ItemFactory.create', 'FRAMEWORK', 'FastAdapter calls factory.create(view) for a new row', evidence='SRC activity/MinibarEditActivity.java:143-147; ' + INF_FAST, cls='non_standard', via='FastAdapter library calls the ViewHolderFactory')
e('MinibarEditActivity$Item$ItemFactory.create', 'MinibarEditActivity$Item$ViewHolder.<init>', 'CALL', 'new ViewHolder(v)', evidence='SRC activity/MinibarEditActivity.java:144-146, 176-182')
e('MinibarEditActivity$Item.bindView', 'MinibarEditActivity$Item$1.<init>', 'CALL', 'holder.cb.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {...})', evidence='SRC activity/MinibarEditActivity.java:160-166')
gui('S_MINIBAR_EDIT', 'MinibarEditActivity$Item$1.onCheckedChanged', 'Toggle the checkbox of a row', evidence='SRC activity/MinibarEditActivity.java:160-166; INFERRED CheckBox calls its OnCheckedChangeListener (support library source not read)', cls='non_standard', via='CompoundButton calls the OnCheckedChangeListener')
INF_ITH = 'INFERRED ItemTouchHelper (fastadapter_extensions SimpleDragCallback, support ItemTouchHelper) calls itemTouchOnMove while a row is dragged to reorder it (library source not read)'
gui('S_MINIBAR_EDIT', 'MinibarEditActivity.itemTouchOnMove', 'Drag a row to reorder the minibar', evidence='SRC activity/MinibarEditActivity.java:59-61, 112-117; ' + INF_ITH, cls='non_standard', via='ItemTouchHelper / SimpleDragCallback call itemTouchOnMove')
gui('S_MINIBAR_EDIT', 'MinibarEditActivity.onPause', 'Press Home, Recents or Back: MinibarEditActivity is paused', kind='SYSTEM', evidence='SRC activity/MinibarEditActivity.java:93-103; ' + FW_STOP)
e('MinibarEditActivity.onPause', 'MinibarEditActivity.onStop', 'LIFECYCLE', 'onStop follows onPause', evidence='SRC activity/MinibarEditActivity.java:105-110; ' + FW_STOP)
e('MinibarEditActivity.onStop', 'Home.initMinBar', 'CALL', 'launcher.initMinBar() rebuilds the minibar rows with the edited arrangement', guard='Home.launcher != null', evidence='SRC activity/MinibarEditActivity.java:106-109')
e('MinibarEditActivity.onStop', 'S_HOME_MINIBAR', 'ENTERS', 'MinibarEditActivity is stopped; Home (minibar open) resumes underneath', evidence='SRC activity/MinibarEditActivity.java:105-110; ' + FW_STOP)

# ================================================================== M. the gesture library: remaining unused public API, and the class-init triggers (Desktop.Item, its Type, DesktopMode, DragAction.Action, CellContainer.PeekDirection, LauncherAction.Theme/Action)
e('LauncherSettings.readDockData', 'Desktop$Item.<clinit>', 'CALL', 'class init on first use of Desktop.Item (the static CREATOR field)', evidence='SRC util/LauncherSettings.java:61-70; ' + FW_CLINIT)
e('Desktop$Item.<clinit>', 'Desktop$Item$1.<init>', 'CALL', 'the static CREATOR field holds one Parcelable.Creator', evidence='SRC widget/Desktop.java:604-615')
e('Desktop$Item.<init>(SimpleItem)', 'Desktop$Item$Type.<clinit>', 'CALL', 'this.type = in.type reads the Type enum of the saved SimpleItem (class init on first use)', evidence='SRC widget/Desktop.java:691-701; ' + FW_CLINIT)
e('LauncherSettings.readSettings', 'Desktop$DesktopMode.<clinit>', 'CALL', 'new GeneralSettings() (no settings file yet, or gson parses one): the field default desktopMode = DesktopMode.Normal reads the enum (class init on first use)',
  guard='generalSettings.json does not exist or does not deserialise (GeneralSettings() runs its field initialisers)', evidence='SRC util/LauncherSettings.java:134-143, 277; ' + FW_CLINIT)
e('LauncherSettings.readSettings', 'AppDrawerController$DrawerMode.<clinit>', 'CALL', 'new GeneralSettings(): the field default drawerMode = DrawerMode.Paged reads the enum (class init on first use)',
  guard='generalSettings.json does not exist or does not deserialise', evidence='SRC util/LauncherSettings.java:134-143, 299; ' + FW_CLINIT)
e('LauncherSettings.readSettings', 'LauncherAction$Theme.<clinit>', 'CALL', 'new GeneralSettings(): the field default theme = Theme.Light reads the enum (class init on first use)',
  guard='generalSettings.json does not exist or does not deserialise', evidence='SRC util/LauncherSettings.java:134-143, 320; ' + FW_CLINIT)
e('Home.initMinBar', 'LauncherAction$Action.<clinit>', 'CALL', 'class init on first use (LauncherAction.actionItems references the enum constants)', evidence='SRC util/LauncherAction.java:29-39; ' + FW_CLINIT)
e('LauncherAction$Action.<clinit>', 'LauncherAction.<clinit>', 'CALL', 'the static actionItems array is built while the class initialises', evidence='SRC util/LauncherAction.java:29-39')
e('LauncherAction.<clinit>', 'LauncherAction$ActionItem.<init>', 'CALL', 'one ActionItem per row of actionItems', evidence='SRC util/LauncherAction.java:29-39')
e('Desktop.onDrag', 'CellContainer$PeekDirection.<clinit>', 'CALL', 'ACTION_DRAG_LOCATION calls peekItemAndSwap, which reads the PeekDirection enum (class init on first use)', evidence='SRC widget/Desktop.java:182-184; widget/CellContainer.java:91-103; ' + FW_CLINIT)
e('AppDrawer_Paged$Adapter.getItemView', 'DragAction$Action.<clinit>', 'CALL', 'withOnLongPressDrag(..., DragAction.Action.ACTION_APP_DRAWER, ...) (class init on first use)', evidence='SRC widget/AppDrawer_Paged.java:142; ' + FW_CLINIT)

# ================================================================== N. custom view plumbing: framework passes (onDraw/onLayout/onMeasure), remaining icon-pack / adapter wiring, drag-to-edge paging
INF_ARRAYLIST = 'INFERRED java.util.ArrayList.remove(Object) / .contains(Object) calls equals() on its elements until one matches (libcore source not read)'

# ---- CellContainer: layout pass, cell geometry helpers, the drag-reorder path
e('CellContainer.init', 'CellContainer.onLayout', 'FRAMEWORK', 'the first layout pass of an attached CellContainer', evidence='SRC widget/CellContainer.java:171-184, 494-538; ' + FW_PASS)
e('CellContainer.onLayout', 'CellContainer.initCellInfo', 'CALL', 'onLayout computes the cell rectangles', evidence='SRC widget/CellContainer.java:507')
e('CellContainer.onLayout', 'CellContainer.onDraw', 'FRAMEWORK', 'the layout pass invalidates the view, which the next draw pass paints', evidence='SRC widget/CellContainer.java:290-339; ' + FW_PASS)
e('Dock.addItemToPosition', 'CellContainer.positionToLayoutPrams(int,int,int,int)', 'CALL', 'positionToLayoutPrams(x, y, item.spanX, item.spanY) finds a free cell for the dropped item', evidence='SRC widget/Dock.java:199-200; widget/CellContainer.java:481-486')
e('CellContainer.positionToLayoutPrams(int,int,int,int)', 'CellContainer.touchPosToCoordinate', 'CALL', 'positionToLayoutPrams(mX, mY, xSpan, ySpan) calls touchPosToCoordinate with checkAvailability', evidence='SRC widget/CellContainer.java:482')
# note: CellContainer.cellPositionToLayoutPrams(int,int,int,int) (no 'current' LayoutParams) and .positionToLayoutPrams(Point,int,int) have no caller anywhere in the app
# (grep over every .java file: only the 4-int positionToLayoutPrams and the 5-arg cellPositionToLayoutPrams-with-current are ever called) -> UNREACHABLE in section O.

# ---- Dock: swipe-up gesture detection and touch dispatch (parallels Desktop's own CellContainer.onTouchListener)
gui('S_HOME_DESKTOP', 'Dock.dispatchTouchEvent', 'Touch the dock', evidence='SRC widget/Dock.java:60-71; ' + FW_TOUCH)
e('Dock.dispatchTouchEvent', 'Dock.detectSwipe', 'CALL', 'detectSwipe(ev) on ACTION_UP', evidence='SRC widget/Dock.java:68, 78-93')
e('Dock.dispatchTouchEvent', 'Dock.onTouchEvent', 'FRAMEWORK', 'super.dispatchTouchEvent(ev) eventually reaches onTouchEvent', evidence='SRC widget/Dock.java:69; ' + FW_TOUCH)
e('Dock.detectSwipe', 'Home.openAppDrawer(View,int,int)', 'CALL', 'a swipe up of more than 150px on the dock opens the drawer (Settings > Gestures > swipe)', guard='generalSettings.swipe is true and Home.launcher != null',
  needs_state=NEED_SWIPE, evidence='SRC widget/Dock.java:84-91')

# ---- Desktop: finger-held-at-edge paging (DragNavigationControl), the Item Parcelable, and the drop-over-folder merge
e('Home.onCreate', 'DragNavigationControl.init', 'CALL', 'DragNavigationControl.init(this, findViewById(R.id.left), findViewById(R.id.right))', evidence='SRC activity/Home.java:302')
e('DragNavigationControl.init', 'DragNavigationControl.<clinit>', 'LIFECYCLE', 'class init on first use (the static leftok/rightok flags)', evidence='SRC viewutil/DragNavigationControl.java:12; ' + FW_CLINIT)
e('DragNavigationControl.init', 'DragNavigationControl$1.<init>', 'CALL', 'leftView.setOnDragListener(new View.OnDragListener() {...})', evidence='SRC viewutil/DragNavigationControl.java:16-25')
e('DragNavigationControl.init', 'DragNavigationControl$2.<init>', 'CALL', 'the left Runnable (page left every 1000 ms while held)', evidence='SRC viewutil/DragNavigationControl.java:26-35')
e('DragNavigationControl$3.onDrag', 'DragNavigationControl$2.run', 'CALL', 'ACTION_DRAG_ENTERED: l.post(left) runs the paging Runnable once, which reposts itself every second while still entered', guard='leftok is true (not already paging)',
  evidence='SRC viewutil/DragNavigationControl.java:55-60')
e('DragNavigationControl$2.run', 'Desktop.addPageLeft', 'CALL', 'the current page is page 0: addPageLeft()', guard='home.desktop.getCurrentItem() == 0', evidence='SRC viewutil/DragNavigationControl.java:29-32')
e('DragNavigationControl$4.onDrag', 'DragNavigationControl$1.run', 'CALL', 'ACTION_DRAG_ENTERED: l.post(right) runs the paging Runnable once, which reposts itself every second while still entered', guard='rightok is true (not already paging)',
  evidence='SRC viewutil/DragNavigationControl.java:96-101')
e('DragNavigationControl$1.run', 'Desktop.addPageRight()', 'CALL', 'the current page is the last one: addPageRight()', guard='home.desktop.getCurrentItem() == home.desktop.pageCount - 1', evidence='SRC viewutil/DragNavigationControl.java:19-22')
e('Desktop.addPageRight()', 'Desktop.addPageRight(boolean)', 'CALL', 'addPageRight() calls addPageRight(false)', evidence='SRC widget/Desktop.java:104-106')
e('Desktop.addPageRight(boolean)', 'Desktop$DesktopAdapter.addPageRight', 'CALL', '((DesktopAdapter) getAdapter()).addPageRight()', evidence='SRC widget/Desktop.java:108-120')
e('Desktop.addPageLeft', 'Desktop$DesktopAdapter.addPageLeft', 'CALL', '((DesktopAdapter) getAdapter()).addPageLeft()', evidence='SRC widget/Desktop.java:122-134')

e('AppItemView$Builder$3.onLongClick@APP', 'Desktop$Item$1.createFromParcel', 'FRAMEWORK', 'the dragged item is read back from the ClipData Intent extra: getParcelableExtra finds the static CREATOR by reflection and calls createFromParcel',
  guard='readyForDrag returned true (the drag starts) and, later, the drop site calls intent.getParcelableExtra("mDragData")', evidence='SRC widget/AppItemView.java:329-332; widget/Desktop.java:188-190, 604-609; ' + FW_DRAGDATA_R, cls='non_standard', via='Parcel: readParcelableCreator finds the static CREATOR field by reflection')
e('Desktop$Item$1.createFromParcel', 'Desktop$Item.<init>(Parcel)', 'CALL', 'return new Item(in)', evidence='SRC widget/Desktop.java:606-609')
e('Desktop.removeItemFromSettings', 'Desktop$Item.equals', 'FRAMEWORK', 'desktopData.get(page).remove(item): ArrayList.remove compares with equals', evidence='SRC widget/Desktop.java:325-327; ' + INF_ARRAYLIST, cls='non_standard', via='java.util.ArrayList calls equals')
# note: Desktop$Item$1.newArray (the Creator reads a single item via getParcelableExtra, never an array) and Desktop$Item.describeContents (nothing ever calls it; the drag path only calls writeToParcel) -> UNREACHABLE in section O.

# ---- AppDrawerController: the three Animator.AnimatorListener nested classes never cancel or repeat in this build
# note: AppDrawerController$1/$2 .onAnimationCancel / .onAnimationRepeat are required by Animator.AnimatorListener but neither animator is ever
# cancelled (no .cancel() call in this file) nor set to repeat (no setRepeatCount) -> UNREACHABLE framework_never_calls in section O.

# ---- AppDrawer_Paged / AppDrawer_Vertical: the one still-missing framework callback of each adapter
e('AppDrawer_Paged.resetAdapter', 'AppDrawer_Paged$Adapter.getItemPosition', 'FRAMEWORK', 'setAdapter(null) after reloadDrawerCardTheme makes the pager ask the old adapter for getItemPosition of its existing pages before destroying them',
  evidence='SRC widget/AppDrawer_Paged.java:121-124; SmoothPagerAdapter.java:275-281; ' + FW_VP)
e('AppDrawer_Vertical$AppItem.getFactory', 'AppDrawer_Vertical$AppItem$ItemFactory.create', 'FRAMEWORK', 'FastAdapter calls factory.create(view) for a new row', evidence='SRC widget/AppDrawer_Vertical.java:184-189; ' + INF_FAST, cls='non_standard', via='FastAdapter library calls the ViewHolderFactory')
e('AppDrawer_Vertical$AppItem$ItemFactory.create', 'AppDrawer_Vertical$AppItem$ViewHolder.<init>', 'CALL', 'new ViewHolder(v)', evidence='SRC widget/AppDrawer_Vertical.java:187-188, 219-227')

# ---- AppItemView: the remaining Drawable.Callback plumbing (invalidateDrawable/refreshDrawableState) and the measure/layout/draw pass
INF_DRAWABLE_CB = 'INFERRED Drawable.invalidateSelf() calls Drawable.Callback.invalidateDrawable(this) on the callback set by setCallback (android.graphics.drawable.Drawable source not read)'
e('ItemViewFactory$12.onClick', 'AppItemView.invalidateDrawable', 'FRAMEWORK', 'popUp() calls invalidateSelf(); setIcon(groupIconDrawable) set this AppItemView as its Drawable.Callback',
  needs_state=NEED_FOLDER, evidence='SRC widget/AppItemView.java:39-45; viewutil/GroupIconDrawable.java:63-69; viewutil/ItemViewFactory.java:224-231; ' + INF_DRAWABLE_CB, cls='non_standard', via='Drawable.invalidateSelf calls the Drawable.Callback')
gui('S_HOME_DESKTOP', 'AppItemView.refreshDrawableState', 'A pressed/focused state changes on a desktop or dock icon', needs_state=NEED_ITEM, evidence='SRC widget/AppItemView.java:47-51; ' + FW_PRESS)
e('AppDrawer_Vertical$AppItem$ViewHolder.<init>', 'AppItemView.setTargetedWidth', 'CALL', 'appItemView.setTargetedWidth(itemWidth)', evidence='SRC widget/AppDrawer_Vertical.java:225')
e('AppDrawer_Vertical$AppItem$ViewHolder.<init>', 'AppItemView.setTargetedHeightPadding', 'CALL', 'appItemView.setTargetedHeightPadding(itemHeightPadding)', evidence='SRC widget/AppDrawer_Vertical.java:226')
e('ItemViewFactory.getItemView@APP', 'AppItemView.onMeasure', 'FRAMEWORK', 'the measure/layout/draw pass of every AppItemView shown on the desktop, dock or drawer', evidence='SRC widget/AppItemView.java:170-177; ' + FW_PASS)
e('AppItemView.onMeasure', 'AppItemView.onLayout', 'FRAMEWORK', 'the layout pass follows measure', evidence='SRC widget/AppItemView.java:199-202; ' + FW_PASS)
e('AppItemView.onLayout', 'AppItemView.onDraw', 'FRAMEWORK', 'the draw pass follows layout', evidence='SRC widget/AppItemView.java:204-243; ' + FW_PASS)
e('AppItemView.onDraw', 'GroupIconDrawable.draw', 'CALL', 'icon.draw(canvas): a group icon paints itself (a static image icon does not override draw)', guard='the item is a folder (icon is a GroupIconDrawable)', needs_state=NEED_FOLDER,
  evidence='SRC widget/AppItemView.java:230-241; viewutil/GroupIconDrawable.java:77-112')

# ---- the gesture library: unused public API, and PagerIndicator's unused theming setters
gui('S_HOME_DESKTOP', 'Tool$2.onTouch', 'Touch an app, shortcut, folder or widget item (withOnTouchGetPosition remembers the touch position for the drag shadow)', needs_state=NEED_ITEM,
    evidence='SRC util/Tool.java:389-400; widget/AppItemView.java:347-350; ' + FW_TOUCH)
e('GroupIconDrawable.draw', 'Tool.clampFloat', 'CALL', 'the pop animation eases the scale factor toward 0.5/1 each frame', evidence='SRC viewutil/GroupIconDrawable.java:81-85')
e('GroupIconDrawable.draw', 'Tool.clampInt', 'CALL', 'the pop animation eases the alpha toward 0/255 each frame', evidence='SRC viewutil/GroupIconDrawable.java:105-110')
e('PagerIndicator.onDraw', 'Tool.clampFloat', 'CALL', 'the selected dot eases its scale factor toward 1/1.5 each frame', evidence='SRC widget/PagerIndicator.java:120-135')
e('Desktop.init', 'PagerIndicator.onDraw', 'FRAMEWORK', 'the indicator draws itself whenever it invalidates (every onPageScrolled)', evidence='SRC widget/Desktop.java:316-322; widget/PagerIndicator.java:82-89, 108-141; ' + FW_PASS)
e('Desktop.init', 'PagerIndicator.onLayout', 'FRAMEWORK', 'the first layout of the indicator sets the dot size from its own height', evidence='SRC widget/Desktop.java:316-322; widget/PagerIndicator.java:99-105; ' + FW_PASS)

# note: IconListAdapter.getItem always returns null and nothing in this plain ListView flow (no getItemAtPosition, no AdapterContextMenu) ever calls it -> UNREACHABLE framework_never_calls in section O.
# note: PagerIndicator.setColor / setFillPaint / setOutlinePaint, and CellContainer$LayoutParams.<init>(int,int) / <init>(int,int,int,int), have no caller anywhere in the app -> UNREACHABLE no_trigger_in_app in section O.

# ---- icon pack picker (Settings > Icons > Icon pack): the list dialog and its two row kinds
e('AppManager.startPickIconPackIntent', 'S_DLG_ICONPACK', 'ENTERS', 'd.show(): the list dialog "Default" plus the installed icon packs', evidence='SRC util/AppManager.java:114-152; ' + INF_MD)
e('AppManager.startPickIconPackIntent', 'AppManager$1.<init>', 'CALL', 'fastItemAdapter.add(new IconLabelItem(..., "Default", new View.OnClickListener() {...}))', evidence='SRC util/AppManager.java:123-131')
e('AppManager.startPickIconPackIntent', 'AppManager$2.<init>', 'CALL', 'one IconLabelItem with a View.OnClickListener per installed icon pack', evidence='SRC util/AppManager.java:135-149')
e('AppManager.startPickIconPackIntent', 'IconLabelItem.<init>', 'CALL', 'new IconLabelItem(icon, label, listener) for "Default" and for every installed icon pack', evidence='SRC util/AppManager.java:123, 135')
e('IconLabelItem.<init>', 'IconLabelItem.<clinit>', 'LIFECYCLE', 'class init on first use (the static FACTORY field)', evidence='SRC viewutil/IconLabelItem.java:39, 41-45; ' + FW_CLINIT)
e('AppManager.startPickIconPackIntent', 'IconLabelItem.getType', 'FRAMEWORK', 'fastItemAdapter.add(...) then d.show(): FastAdapter shows the rows', evidence='SRC util/AppManager.java:114-152; ' + INF_FAST, cls='non_standard', via='FastAdapter library calls the item methods')
for _ilcb in ('getLayoutRes', 'getFactory', 'bindView'):
    e('IconLabelItem.getType', 'IconLabelItem.' + _ilcb, 'FRAMEWORK', 'FastAdapter asks the item for %s' % _ilcb, evidence='SRC viewutil/IconLabelItem.java:34-58; ' + INF_FAST, cls='non_standard', via='FastAdapter library calls the item methods')
e('IconLabelItem.getFactory', 'IconLabelItem$ItemFactory.<init>', 'CALL', 'the static FACTORY field holds one ItemFactory', evidence='SRC viewutil/IconLabelItem.java:39, 41')
e('IconLabelItem.getFactory', 'IconLabelItem$ItemFactory.create', 'FRAMEWORK', 'FastAdapter calls factory.create(view) for a new row', evidence='SRC viewutil/IconLabelItem.java:41-45; ' + INF_FAST, cls='non_standard', via='FastAdapter library calls the ViewHolderFactory')
e('IconLabelItem$ItemFactory.create', 'IconLabelItem$ViewHolder.<init>', 'CALL', 'new ViewHolder(v)', evidence='SRC viewutil/IconLabelItem.java:43, 60-66')
gui('S_DLG_ICONPACK', 'AppManager$1.onClick', 'Tap "Default"', evidence='SRC util/AppManager.java:123-131; ' + INF_FAST, cls='non_standard', via='the IconLabelItem click listener (bindView sets it as the item view\'s OnClickListener)')
gui('S_DLG_ICONPACK', 'AppManager$2.onClick', 'Tap an installed icon pack', evidence='SRC util/AppManager.java:135-149; ' + INF_FAST, cls='non_standard', via='the IconLabelItem click listener (bindView sets it as the item view\'s OnClickListener)')
e('AppManager$1.onClick', 'AppManager.getAllApps', 'CALL', 'getAllApps() reloads the app list with no icon pack', evidence='SRC util/AppManager.java:126-129')
e('AppManager$2.onClick', 'AppManager.getAllApps', 'CALL', 'getAllApps() reloads the app list themed with the chosen pack', guard='READ_EXTERNAL_STORAGE is granted', env=ENV_PERM_STORAGE, evidence='SRC util/AppManager.java:138-144')
e('AppManager$2.onClick', 'S_PERMISSION', 'ENTERS', 'the permission is not granted: a toast, then ActivityCompat.requestPermissions', guard='READ_EXTERNAL_STORAGE is not granted', evidence='SRC util/AppManager.java:143-146; ' + FW_PERM)
e('AppManager$1.onClick', 'S_SETTINGS_ICONS', 'ENTERS', 'd.dismiss(): the dialog closes', evidence='SRC util/AppManager.java:129-130; ' + INF_MD)
e('AppManager$2.onClick', 'S_SETTINGS_ICONS', 'ENTERS', 'd.dismiss(): the dialog closes', guard='READ_EXTERNAL_STORAGE is granted', env=ENV_PERM_STORAGE, evidence='SRC util/AppManager.java:138-144; ' + INF_MD)
e('AppManager$AsyncGetApps.onPostExecute', 'AppManager$App.equals', 'FRAMEWORK', 'tempApps.contains(...) / apps.contains(...) compares apps while looking for a deleted one', evidence='SRC util/AppManager.java:225-231; ' + INF_ARRAYLIST, cls='non_standard', via='java.util.ArrayList calls equals')
e('AppManager$AsyncGetApps.onPostExecute', 'AppManager$AppUpdatedListener.equals', 'FRAMEWORK', 'updateListeners.remove(listener): ArrayList.remove compares with equals', evidence='SRC util/AppManager.java:239-241; ' + INF_ARRAYLIST, cls='non_standard', via='java.util.ArrayList calls equals')
e('SettingsActivity.onCreate', 'Tool.wrapColorTag', 'CALL', 'every ButtonPref/TBPref/NUMPref/ColorPref with a non-null summary wraps it in a colored font tag (warpText)',
  evidence='SRC activity/SettingsActivity.java:42-48; SRC %s:390-392, 403 (warpText calls Tool.wrapColorTag)' % MPF, cls='non_standard', via='MaterialPrefFragment library (vendored) calls Tool.wrapColorTag from warpText')

# ================================================================== N2. a few framework passes and call sites missed above
e('DragOptionView.<init>(Context,AttributeSet)', 'DragOptionView.onLayout', 'FRAMEWORK', 'the first layout pass of the inflated top bar (sets its initial off-screen Y)', evidence='SRC widget/DragOptionView.java:58-65; ' + FW_PASS)
e('DragOptionView.onDragEvent', 'DragOptionView$4.run', 'ASYNC', 'ACTION_DRAG_STARTED (every drag type except none): animShowView() hides the auto-hide view, then withEndAction shows the top bar', evidence='SRC widget/DragOptionView.java:210-218; ' + FW_ANIM_END)
e('DragOptionView$4.run', 'DragOptionView.show', 'CALL', 'show(): the top bar animates up into view', evidence='SRC widget/DragOptionView.java:71-76, 210-217')
e('DragOptionView.onDragEvent', 'DragOptionView$5.run', 'ASYNC', 'ACTION_DRAG_ENDED: hide().withEndAction(...) hides the icons after the top bar animates back down', evidence='SRC widget/DragOptionView.java:287-303; ' + FW_ANIM_END)
e('GroupPopupView.init', 'GroupPopupView.onLayout', 'FRAMEWORK', 'the first layout pass of the inflated folder popup view', evidence='SRC widget/GroupPopupView.java:50-57; ' + FW_PASS)

# ================================================================== O. UNREACHABLE: every method with no route in the standard configuration, with its kind, reason and source reference
UNREACHABLE = {}


def unreach(method, kind, reason, ref, confirmed='SOURCE'):
    UNREACHABLE[method] = (kind, reason, ref, confirmed)


_DB_WHY = ("DatabaseHelper is never instantiated: the only three call sites are commented out (util/LauncherSettings.java:49, 80, 237: '// DatabaseHelper db = new DatabaseHelper(context);'); "
           "the app reads and writes desktopData.json / dockData.json / generalSettings.json with Gson instead (util/LauncherSettings.java:126-156, 231-268). No path to `new DatabaseHelper(...)` exists.")
for _m, _ref in (('<init>', 'util/DatabaseHelper.java:52-55'), ('onCreate', 'util/DatabaseHelper.java:57-64'), ('onUpgrade', 'util/DatabaseHelper.java:66-72'), ('onDowngrade', 'util/DatabaseHelper.java:74-76'),
                  ('createItem', 'util/DatabaseHelper.java:78-123'), ('deleteItem', 'util/DatabaseHelper.java:125-129'), ('addItem', 'util/DatabaseHelper.java:131-141'), ('removeItem', 'util/DatabaseHelper.java:143-146'),
                  ('getDesktop', 'util/DatabaseHelper.java:148-169'), ('getDock', 'util/DatabaseHelper.java:171-186'), ('setDesktop', 'util/DatabaseHelper.java:188-200'), ('setDock', 'util/DatabaseHelper.java:202-210'),
                  ('getSelection', 'util/DatabaseHelper.java:212-222'), ('getItem', 'util/DatabaseHelper.java:224-281'), ('getIntentAsString', 'util/DatabaseHelper.java:283-285'), ('getIntentFromString', 'util/DatabaseHelper.java:287-297')):
    unreach('DatabaseHelper.' + _m, 'no_trigger_in_app', _DB_WHY, _ref)

_QC_UNUSED_WHY = ("QuickCenterItem is marked @Deprecated ('Concept idea of adding a place that enable user to take notes, suggest apps and contacts', viewutil/QuickCenterItem.java:26-27); "
                "NoteItem / NoteContent / SearchHeader are never instantiated anywhere in the app (no `new QuickCenterItem.NoteItem(`, `.NoteContent(` or `.SearchHeader(` outside their own declarations).")
for _m, _ref in (('<init>', 'viewutil/QuickCenterItem.java:30-39'), ('bindView', 'viewutil/QuickCenterItem.java:52-67'), ('getFactory', 'viewutil/QuickCenterItem.java:77-80'), ('getLayoutRes', 'viewutil/QuickCenterItem.java:47-49'),
                  ('getType', 'viewutil/QuickCenterItem.java:42-44'), ('$1.<init>', 'viewutil/QuickCenterItem.java:56-65'), ('$1.onLongClick', 'viewutil/QuickCenterItem.java:57-64'),
                  ('$ItemFactory.<init>', 'viewutil/QuickCenterItem.java:69, 71'), ('$ItemFactory.create', 'viewutil/QuickCenterItem.java:72-74'), ('$ViewHolder.<init>', 'viewutil/QuickCenterItem.java:86-90')):
    unreach('QuickCenterItem$NoteItem' + _m if _m.startswith('$') else 'QuickCenterItem$NoteItem.' + _m, 'no_trigger_in_app', _QC_UNUSED_WHY, _ref)
unreach('QuickCenterItem$NoteContent.<init>', 'no_trigger_in_app', _QC_UNUSED_WHY, 'viewutil/QuickCenterItem.java:98-101')
unreach('QuickCenterItem$NoteContent.equals', 'no_trigger_in_app', _QC_UNUSED_WHY, 'viewutil/QuickCenterItem.java:103-106')
for _m, _ref in (('<init>', 'viewutil/QuickCenterItem.java:200-201'), ('bindView', 'viewutil/QuickCenterItem.java:213-216'), ('getFactory', 'viewutil/QuickCenterItem.java:226-229'), ('getLayoutRes', 'viewutil/QuickCenterItem.java:208-211'),
                  ('getType', 'viewutil/QuickCenterItem.java:203-206'), ('$ItemFactory.<init>', 'viewutil/QuickCenterItem.java:218, 220'), ('$ItemFactory.create', 'viewutil/QuickCenterItem.java:221-223'),
                  ('$ViewHolder.<init>', 'viewutil/QuickCenterItem.java:231-237')):
    unreach('QuickCenterItem$SearchHeader' + _m if _m.startswith('$') else 'QuickCenterItem$SearchHeader.' + _m, 'no_trigger_in_app', _QC_UNUSED_WHY, _ref)

_QC_CFG_WHY = ("QuickCenterItem.ContactItem / ContactContent are built only inside Home$CallLogObserver.logCallLog (viewutil/QuickCenterItem.java is otherwise the same dead class as NoteItem/SearchHeader above), "
               "and logCallLog never runs: see Home$CallLogObserver below (READ_CALL_LOG is commented out of the manifest).")
for _m, _ref in (('<init>', 'viewutil/QuickCenterItem.java:112-114'), ('bindView', 'viewutil/QuickCenterItem.java:126-154'), ('getFactory', 'viewutil/QuickCenterItem.java:164-167'), ('getLayoutRes', 'viewutil/QuickCenterItem.java:121-124'),
                  ('getType', 'viewutil/QuickCenterItem.java:116-119'), ('$1.<init>', 'viewutil/QuickCenterItem.java:141-153'), ('$1.onClick', 'viewutil/QuickCenterItem.java:142-152'),
                  ('$ItemFactory.<init>', 'viewutil/QuickCenterItem.java:156, 158'), ('$ItemFactory.create', 'viewutil/QuickCenterItem.java:159-161'), ('$ViewHolder.<init>', 'viewutil/QuickCenterItem.java:169-176')):
    unreach('QuickCenterItem$ContactItem' + _m if _m.startswith('$') else 'QuickCenterItem$ContactItem.' + _m, 'closed_by_configuration', _QC_CFG_WHY, _ref)
unreach('QuickCenterItem$ContactContent.<init>', 'closed_by_configuration', _QC_CFG_WHY, 'viewutil/QuickCenterItem.java:185-190')
unreach('QuickCenterItem$ContactContent.equals', 'closed_by_configuration', _QC_CFG_WHY, 'viewutil/QuickCenterItem.java:192-195')

_RD_WHY = "RoundDrawable is only used by QuickCenterItem.ContactItem.bindView (viewutil/QuickCenterItem.java:131: 'new RoundDrawable(info.icon)'), which never runs (see QuickCenterItem.ContactItem above); no other call site exists."
for _m, _ref in (('<init>', 'viewutil/RoundDrawable.java:22-24'), ('draw', 'viewutil/RoundDrawable.java:26-32'), ('getCroppedBitmap', 'viewutil/RoundDrawable.java:34-52'), ('getOpacity', 'viewutil/RoundDrawable.java:64-67'),
                  ('setAlpha', 'viewutil/RoundDrawable.java:54-57'), ('setColorFilter', 'viewutil/RoundDrawable.java:59-62')):
    unreach('RoundDrawable.' + _m, 'no_trigger_in_app', _RD_WHY, _ref)

_CLO_WHY = ("android.permission.READ_CALL_LOG is commented out of AndroidManifest.xml ('TODO activate later again', AndroidManifest.xml:4-8, together with CALL_PHONE and READ_CONTACTS); "
            "ActivityCompat.checkSelfPermission(READ_CALL_LOG) can therefore never return PERMISSION_GRANTED (the system denies a permission the manifest does not declare) and requestPermissions cannot grant it either, "
            "so Home.initQuickCenter's else branch (which builds CallLogObserver) never runs, and onRequestPermissionsResult's `callLogObserver != null` guard is also never true (the field starts null and only the two unreachable branches set it).")
for _m, _ref in (('<init>', 'activity/Home.java:887-889'), ('deliverSelfNotifications', 'activity/Home.java:891-894'), ('logCallLog', 'activity/Home.java:896-918'),
                  ('onChange(boolean)', 'activity/Home.java:920-923'), ('onChange(boolean,Uri)', 'activity/Home.java:925-928')):
    unreach('Home$CallLogObserver.' + _m, 'closed_by_configuration', _CLO_WHY, _ref)

unreach('Home.onSearch', 'no_trigger_in_app', "an XML android:onClick handler for the desktop search bar, documented 'However the search bar is removed out for now' (activity/Home.java:812-815); "
        "no layout XML in this dataset references onSearch (grep over res/layout/*.xml found none).", 'activity/Home.java:816-829')
unreach('Home.onVoiceSearch', 'no_trigger_in_app', "an XML android:onClick handler for the same removed search bar (activity/Home.java:831-834); no layout XML references onVoiceSearch.", 'activity/Home.java:835-843')

unreach('Tool.<init>', 'no_trigger_in_app', 'Tool is a static-utility class (private constructor); it is never instantiated.', 'util/Tool.java:54-55')
unreach('Tool.setHomeTheme', 'no_trigger_in_app', 'Never called anywhere in the app (grep found no call site); its body is also fully commented out, like Tool.setTheme.', 'util/Tool.java:447-456')
unreach('Tool.getContactIDFromNumber', 'no_trigger_in_app', 'Never called anywhere in the app (its only prospective caller, Tool.openPhoto, is itself never called).', 'util/Tool.java:123-134')
unreach('Tool.openPhoto', 'no_trigger_in_app', 'Never called anywhere in the app (grep found no call site).', 'util/Tool.java:175-198')
unreach('Tool.fetchThumbnail', 'closed_by_configuration', 'Only called from Home$CallLogObserver.logCallLog, which never runs (READ_CALL_LOG is not declared; see Home$CallLogObserver above).', 'util/Tool.java:152-173')
unreach('Tool.fetchThumbnailId', 'closed_by_configuration', 'Only called from Tool.fetchThumbnail, which never runs for the same reason.', 'util/Tool.java:136-150')
unreach('Tool$DialogHelper.<init>', 'no_trigger_in_app', 'DialogHelper only has static methods (promptInputText, alert); its implicit no-arg constructor is never called.', 'util/Tool.java:462')

unreach('ItemViewFactory.<init>', 'no_trigger_in_app', 'ItemViewFactory is a static-utility class; its implicit constructor is never called.', 'viewutil/ItemViewFactory.java:34')
unreach('DialogUtils.<init>', 'no_trigger_in_app', 'DialogUtils is a static-utility class; its implicit constructor is never called.', 'util/DialogUtils.java:18')
unreach('IconPackHelper.<init>', 'no_trigger_in_app', 'IconPackHelper has only the static method themePacs (called from AppManager$AsyncGetApps.doInBackground); its implicit constructor is never called.', 'util/IconPackHelper.java:24')
unreach('LauncherAction.<init>', 'no_trigger_in_app', 'LauncherAction is a static-utility class; its implicit constructor is never called.', 'util/LauncherAction.java:25')
unreach('LauncherAction$Theme.names', 'no_trigger_in_app', 'Never called anywhere in the app; only the field default LauncherAction.Theme.Light is read (util/LauncherSettings.java:320), never Theme.values() via names().', 'util/LauncherAction.java:163-172')

unreach('GestureAnalyser.getOngoingGesture', 'no_trigger_in_app',
        'Public API of the vendored gesture library; only getGesture is called by SimpleFingerGestures.onTouch (in/championswimmer/sfg/lib/SimpleFingerGestures.java:79, 92); getOngoingGesture has no caller.',
        'in/championswimmer/sfg/lib/GestureAnalyser.java:119')
unreach('SimpleFingerGestures.getConsumeTouchEvents', 'no_trigger_in_app', 'Public API never called by the app (CellContainer only constructs new SimpleFingerGestures() and calls setOnFingerGestureListener).', 'in/championswimmer/sfg/lib/SimpleFingerGestures.java:22-24')
unreach('SimpleFingerGestures.setConsumeTouchEvents', 'no_trigger_in_app', 'Public API never called by the app.', 'in/championswimmer/sfg/lib/SimpleFingerGestures.java:26-28')
unreach('SimpleFingerGestures.setDebug', 'no_trigger_in_app', 'Public API never called by the app.', 'in/championswimmer/sfg/lib/SimpleFingerGestures.java:18-20')
unreach('SimpleFingerGestures.<init>(int,int,int)', 'no_trigger_in_app', 'Only the no-arg constructor is used (widget/Desktop.java:460: `new SimpleFingerGestures()`); the 3-arg constructor has no caller.', 'in/championswimmer/sfg/lib/SimpleFingerGestures.java:47-49')

unreach('PagerIndicator.setColor', 'no_trigger_in_app', 'Public theming API never called anywhere in the app (grep over every .java file found no caller outside PagerIndicator.java itself).', 'widget/PagerIndicator.java:57-60')
unreach('PagerIndicator.setFillPaint', 'no_trigger_in_app', 'Public theming API never called anywhere in the app.', 'widget/PagerIndicator.java:52-55')
unreach('PagerIndicator.setOutlinePaint', 'no_trigger_in_app', 'Public theming API never called anywhere in the app.', 'widget/PagerIndicator.java:47-50')
unreach('CellContainer.cellPositionToLayoutPrams(int,int,int,int)', 'no_trigger_in_app', 'The only caller (viewutil/ItemViewFactory.java:245, scaleWidget) uses the 5-arg overload that also takes the current LayoutParams to clear first.', 'widget/CellContainer.java:404-430')
unreach('CellContainer.positionToLayoutPrams(Point,int,int)', 'no_trigger_in_app', 'Both callers of a positionToLayoutPrams overload (widget/Desktop.java:293, widget/Dock.java:200) use the 4-int overload, not this Point-based one.', 'widget/CellContainer.java:488-492')
unreach('CellContainer$LayoutParams.<init>(int,int)', 'no_trigger_in_app', 'Every LayoutParams built in the app uses the 6-arg constructor (w,h,x,y,xSpan,ySpan; e.g. widget/CellContainer.java:364, widget/AppDrawer_Paged.java:174); the 2-arg convenience constructor has no caller.', 'widget/CellContainer.java:595-597')
unreach('CellContainer$LayoutParams.<init>(int,int,int,int)', 'no_trigger_in_app', 'Same as the 2-arg constructor: every LayoutParams built in the app uses the 6-arg constructor; the 4-arg one has no caller.', 'widget/CellContainer.java:578-583')

unreach('IconListAdapter.getItem', 'framework_never_calls',
        "Always returns null; the minibar's OnItemClickListener reads the label list directly (activity/Home.java:594: `labels.get(i)`) instead of calling adapter.getItem, and this plain ListView has no AdapterContextMenu or accessibility path that would call it either.",
        'viewutil/IconListAdapter.java:31-33')
unreach('GroupIconDrawable.setAlpha', 'framework_never_calls', "Required Drawable override; nothing in the app calls setAlpha on a GroupIconDrawable (it is drawn directly with icon.draw(canvas) in AppItemView.onDraw, never attached through setBackground/setImageDrawable).", 'viewutil/GroupIconDrawable.java:114-116')
unreach('GroupIconDrawable.setColorFilter', 'framework_never_calls', "Required Drawable override; nothing in the app calls setColorFilter on a GroupIconDrawable.", 'viewutil/GroupIconDrawable.java:118-120')
unreach('GroupIconDrawable.getOpacity', 'framework_never_calls', "Required Drawable override; nothing in the app calls getOpacity on a GroupIconDrawable.", 'viewutil/GroupIconDrawable.java:122-125')
unreach('Desktop$Item.describeContents', 'framework_never_calls',
        "INFERRED: the only Parcelable write of an Item is through ClipData.Item/Intent extras (widget/AppItemView.java:329-332, widget/GroupPopupView.java:134-144), which call writeToParcel directly; "
        "describeContents is part of the Parcelable contract but is used by the platform only for flags this single-item drag path does not need (android.os.Parcel / android.content.Intent not read line-by-line for this specific negative claim).",
        'widget/Desktop.java:826-829')
unreach('Desktop$Item$1.newArray', 'framework_never_calls',
        "The Creator is only used to read a single dragged Item (Intent.getParcelableExtra, widget/Desktop.java:189-190, widget/Dock.java:117), never a Parcelable array of Items, so newArray (used only by readParcelableArray / createTypedArray) is never invoked.",
        'widget/Desktop.java:611-614')
unreach('Desktop$Item.fromGroupItem', 'no_trigger_in_app', 'A static factory method with no caller anywhere in the app (grep found only its own declaration).', 'widget/Desktop.java:752-759')

unreach('AppItemView.getBgColor', 'no_trigger_in_app', 'Public getter with no caller anywhere in the app (the setter setBgColor is used, but nothing reads it back).', 'widget/AppItemView.java:125-127')
unreach('AppItemView.getHeightPadding', 'no_trigger_in_app', 'Public getter with no caller anywhere in the app.', 'widget/AppItemView.java:142-144')
unreach('AppItemView.getIconPadding', 'no_trigger_in_app', 'Public getter with no caller anywhere in the app (the setter setIconPadding is used, but nothing reads it back).', 'widget/AppItemView.java:79-81')
unreach('AppItemView.getIconSizeSmall', 'no_trigger_in_app', 'Public getter with no caller anywhere in the app (the setter setIconSizeSmall is used, but nothing reads it back).', 'widget/AppItemView.java:69-71')
unreach('AppItemView.isRoundBg', 'no_trigger_in_app', 'Public getter with no caller anywhere in the app (the setter setRoundBg is used, but nothing reads it back).', 'widget/AppItemView.java:117-119')

_ANIM_WHY = 'Required Animator.AnimatorListener overrides; the reveal/hide ObjectAnimator this listener is attached to is never cancelled (no .cancel() call anywhere in AppDrawerController.java) and never set to repeat (no setRepeatCount), so these two callbacks never fire.'
unreach('AppDrawerController$1.onAnimationCancel', 'framework_never_calls', _ANIM_WHY, 'widget/AppDrawerController.java:103-105')
unreach('AppDrawerController$1.onAnimationRepeat', 'framework_never_calls', _ANIM_WHY, 'widget/AppDrawerController.java:107-109')
unreach('AppDrawerController$2.onAnimationCancel', 'framework_never_calls', _ANIM_WHY, 'widget/AppDrawerController.java:139-141')
unreach('AppDrawerController$2.onAnimationRepeat', 'framework_never_calls', _ANIM_WHY, 'widget/AppDrawerController.java:143-145')

_CTOR_WHY = 'The app only ever inflates this view from an XML layout, which always supplies an AttributeSet (LayoutInflater.createView looks up the (Context, AttributeSet) constructor); this constructor is never called.'
for _cls, _sig, _ref in (
    ('AppDrawerController', '<init>(Context)', 'widget/AppDrawerController.java:46-48'), ('AppDrawerController', '<init>(Context,AttributeSet,int)', 'widget/AppDrawerController.java:50-52'),
    ('AppDrawer_Paged', '<init>(Context)', 'widget/AppDrawer_Paged.java:42-45'),
    ('AppDrawer_Vertical', '<init>(Context)', 'widget/AppDrawer_Vertical.java:48-51'), ('AppDrawer_Vertical', '<init>(Context,AttributeSet,int)', 'widget/AppDrawer_Vertical.java:58-61'),
    ('Desktop', '<init>(Context)', 'widget/Desktop.java:72-74'),
    ('Dock', '<init>(Context)', 'widget/Dock.java:31-33'),
    ('DragOptionView', '<init>(Context)', 'widget/DragOptionView.java:44-47'),
    ('GroupPopupView', '<init>(Context)', 'widget/GroupPopupView.java:40-43'),
    ('MiniPopupView', '<init>(Context)', 'widget/MiniPopupView.java:1-200'), ('MiniPopupView', '<init>(Context,AttributeSet,int)', 'widget/MiniPopupView.java:1-200'),
    ('PagerIndicator', '<init>(Context)', 'widget/PagerIndicator.java:29-32'),
    ('SearchBar', '<init>(Context)', 'widget/SearchBar.java:16-20'),
    ('SwipeListView', '<init>(Context)', 'widget/SwipeListView.java:24-28'), ('SwipeListView', '<init>(Context,AttributeSet,int)', 'widget/SwipeListView.java:36-40'),
    ('WidgetView', '<init>(Context,int,int)', 'widget/WidgetView.java:19-21'),
):
    unreach('%s.%s' % (_cls, _sig), 'no_trigger_in_app', _CTOR_WHY, _ref)

unreach('GroupPopupView$GroupDef.<init>', 'no_trigger_in_app', 'GroupDef has only static fields/methods (maxItem, getCellSize); its implicit constructor is never called (no `new GroupDef(` anywhere).', 'widget/GroupPopupView.java:292-293')

_UNBIND_WHY = 'ButterKnife.bind(...) is called but its return value (the Unbinder) is never stored or unbound anywhere in this file; the generated unbind() is never invoked.'
unreach('Home$$ViewBinder$InnerUnbinder.unbind()', 'no_trigger_in_app', _UNBIND_WHY, 'activity/Home.java:197')
unreach('Home$$ViewBinder$InnerUnbinder.unbind(Home)', 'no_trigger_in_app', _UNBIND_WHY, 'activity/Home.java:197')
unreach('MinibarEditActivity$$ViewBinder$InnerUnbinder.unbind()', 'no_trigger_in_app', _UNBIND_WHY, 'activity/MinibarEditActivity.java:51')
unreach('MinibarEditActivity$$ViewBinder$InnerUnbinder.unbind(MinibarEditActivity)', 'no_trigger_in_app', _UNBIND_WHY, 'activity/MinibarEditActivity.java:51')
unreach('MiniPopupView$ClearRamViewHolder$$ViewBinder$InnerUnbinder.unbind()', 'no_trigger_in_app', _UNBIND_WHY, 'widget/MiniPopupView.java:163-172')
unreach('MiniPopupView$ClearRamViewHolder$$ViewBinder$InnerUnbinder.unbind(ClearRamViewHolder)', 'no_trigger_in_app', _UNBIND_WHY, 'widget/MiniPopupView.java:163-172')
unreach('MiniPopupView$VolumeDialogViewHolder$$ViewBinder$InnerUnbinder.unbind()', 'no_trigger_in_app', _UNBIND_WHY, 'widget/MiniPopupView.java:124-136')
unreach('MiniPopupView$VolumeDialogViewHolder$$ViewBinder$InnerUnbinder.unbind(VolumeDialogViewHolder)', 'no_trigger_in_app', _UNBIND_WHY, 'widget/MiniPopupView.java:124-136')

_SF_WHY = ("SettingsFragment is @Deprecated (fragment/SettingsFragment.java:14); SettingsActivity.onCreate comments out its only instantiation "
           "('//SettingsFragment settings = new SettingsFragment();', activity/SettingsActivity.java:39) and uses MaterialPrefFragment instead. No path to `new SettingsFragment()` exists.")
for _m, _ref in (('<init>', 'fragment/SettingsFragment.java:15'), ('onAttach', 'fragment/SettingsFragment.java:88-96'), ('onCreateView', 'fragment/SettingsFragment.java:18-81'), ('onOptionsItemSelected', 'fragment/SettingsFragment.java:83-86')):
    unreach('SettingsFragment.' + _m, 'no_trigger_in_app', _SF_WHY, _ref)
_SF_LN = {1: '31-36', 2: '38-43', 3: '45-50', 4: '52-57', 5: '59-64', 6: '66-71', 7: '73-78'}
for _n in range(1, 8):
    unreach('SettingsFragment$%d.<init>' % _n, 'no_trigger_in_app', _SF_WHY, 'fragment/SettingsFragment.java:' + _SF_LN[_n])
    unreach('SettingsFragment$%d.onClick' % _n, 'no_trigger_in_app', _SF_WHY, 'fragment/SettingsFragment.java:' + _SF_LN[_n])

_MBF_WHY = ("MinibarEditFragment is never referenced anywhere in the app (grep over every .java file found only its own declaration in fragment/MinibarEditFragment.java); "
            "MinibarEditActivity (a separate class, not this fragment) implements the minibar editor shown to the user. No path to `new MinibarEditFragment()` exists.")
for _m, _ref in (('<init>', 'fragment/MinibarEditFragment.java:40'), ('onAttach', 'fragment/MinibarEditFragment.java:46-54'), ('onCreate', 'fragment/MinibarEditFragment.java:56-90'), ('onCreateView', 'fragment/MinibarEditFragment.java:92-97'),
                  ('itemTouchOnMove', 'fragment/MinibarEditFragment.java:150-154'), ('onPause', 'fragment/MinibarEditFragment.java:99-108'), ('onStop', 'fragment/MinibarEditFragment.java:110-115'),
                  ('$$ViewBinder.<init>', 'fragment/MinibarEditFragment.java:60-64'), ('$$ViewBinder.bind', 'fragment/MinibarEditFragment.java:60-64'), ('$$ViewBinder.createUnbinder', 'fragment/MinibarEditFragment.java:60-64'),
                  ('$$ViewBinder$InnerUnbinder.<init>', 'fragment/MinibarEditFragment.java:60-64'), ('$$ViewBinder$InnerUnbinder.unbind()', 'fragment/MinibarEditFragment.java:60-64'),
                  ('$$ViewBinder$InnerUnbinder.unbind(MinibarEditFragment)', 'fragment/MinibarEditFragment.java:60-64'), ('$1.<init>', 'fragment/MinibarEditFragment.java:79-89'), ('$1.onCheckedChanged', 'fragment/MinibarEditFragment.java:81-88'),
                  ('$AppItem.<clinit>', 'fragment/MinibarEditFragment.java:170'), ('$AppItem.<init>', 'fragment/MinibarEditFragment.java:160-164'), ('$AppItem.bindView', 'fragment/MinibarEditFragment.java:180-190'),
                  ('$AppItem.getFactory', 'fragment/MinibarEditFragment.java:172-175'), ('$AppItem.getLayoutRes', 'fragment/MinibarEditFragment.java:168'), ('$AppItem.getType', 'fragment/MinibarEditFragment.java:166'),
                  ('$AppItem$1.<init>', 'fragment/MinibarEditFragment.java:183-189'), ('$AppItem$1.onCheckedChanged', 'fragment/MinibarEditFragment.java:184-188'),
                  ('$AppItem$ItemFactory.<init>', 'fragment/MinibarEditFragment.java:172, 174'), ('$AppItem$ItemFactory.create', 'fragment/MinibarEditFragment.java:175-177'),
                  ('$AppItem$ViewHolder.<init>', 'fragment/MinibarEditFragment.java:192-193')):
    key = 'MinibarEditFragment' + _m if _m.startswith('$') else 'MinibarEditFragment.' + _m
    unreach(key, 'no_trigger_in_app', _MBF_WHY, _ref)

unreach('QuickCenterItem.<init>', 'no_trigger_in_app', 'QuickCenterItem only holds static nested classes (NoteItem, ContactItem, SearchHeader, ...); the outer class itself is never instantiated.', 'viewutil/QuickCenterItem.java:28')
unreach('DragNavigationControl.<init>', 'no_trigger_in_app', 'DragNavigationControl is a static-utility class (only the static method init is used, from Home.onCreate); its implicit no-arg constructor is never called.', 'viewutil/DragNavigationControl.java:10')

# ---- P. a few more page edges found missing on rebuild (S_SETTINGS_PAUSED), and Home.onDestroy's incoming edge
e('S_SETTINGS_ROOT', 'S_SETTINGS_PAUSED', 'ENTERS', 'Press Home or Recents, or another activity covers Settings', gui=['Press Home or Recents while Settings is open'], evidence='SRC activity/SettingsActivity.java:1-30; ' + FW_STOP)
e('S_SETTINGS_PAUSED', 'S_SETTINGS_ROOT', 'ENTERS', 'SettingsActivity returns to the foreground', gui=['Return to Settings from the recents list'], evidence='SRC activity/SettingsActivity.java:1-30; ' + FW_LAUNCH)
e('S_HOME_PAUSED', 'Home.onDestroy', 'SYSTEM', 'the system destroys the stopped Home instance (low memory, or recreate()/finish())', evidence='SRC activity/Home.java:686-697; ' + FW_STOP)

# ---- Q. silence "UNREACHABLE but has incoming edges" warnings: every method above is dead because its whole small cluster is dead
# (internal calls between two unreachable methods still appear as bytecode edges; suppressing their outgoing auto edges keeps the
# warning list honest without inventing a route). No hand-written edge in this file uses an UNREACHABLE method as its source.
for _um in UNREACHABLE:
    sup(_um)

# ---- R. bytecode line fix (tools/check_bytecode_lines.py --emit): a multi-line constructor call whose line table points one line late
FIX_LINES = {
    ('HideAppsFragment.prepareData', 'AppInfo.<init>', 'SRC HideAppsFragment.java:169 (bytecode)'): 'SRC HideAppsFragment.java:165-169 (bytecode line was 169)',
}


def EDIT(x):
    for (src, dst, old), new in FIX_LINES.items():
        if x['src'] == src and x['dst'] == dst and old in (x['evidence'] or ''):
            x['evidence'] = x['evidence'].replace(old, new)


STRICT = True
