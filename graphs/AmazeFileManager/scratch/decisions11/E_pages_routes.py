e('MainActivity.onCreate', 'S_MAIN', 'LIFECYCLE', 'onCreate builds the main shell (views, FAB, preferences); the main screen is shown from here', evidence='SRC activities/MainActivity.java:277 public void onCreate; lines 243-245 call initialiseViews and initialiseFab')

e('MainFragment.onCreateView', 'S_MAIN_TAB', 'LIFECYCLE', 'onCreateView inflates the tab that shows the file list', evidence='SRC fragments/MainFragment.java:237 public View onCreateView(LayoutInflater, ViewGroup, Bundle)')

e('PermissionsActivity.<init>', 'S_PERM', 'LIFECYCLE', 'PermissionsActivity (superclass of MainActivity) is the activity that requests storage permission', evidence='SRC activities/superclasses/PermissionsActivity.java class declaration; MainActivity.<init> extends it (existing LIFECYCLE edge)')

e('TextEditorActivity.onCreate', 'S_TEXT_EDITOR', 'LIFECYCLE', 'onCreate shows the text viewer/editor screen', evidence='SRC activities/TextEditorActivity.java:126 public void onCreate(Bundle)')

e('DatabaseViewerActivity.onCreate', 'S_DB_VIEWER', 'LIFECYCLE', 'onCreate shows the SQLite database viewer screen', evidence='SRC activities/DatabaseViewerActivity.java:79 public void onCreate(Bundle)')

e('AboutActivity.onCreate', 'S_ABOUT', 'LIFECYCLE', 'onCreate shows the about screen', evidence='SRC activities/AboutActivity.java (src/fdroid and src/play flavors) onCreate; reached through the existing BasicActivity.<init> -> AboutActivity.onCreate LIFECYCLE edge')

e('ExtractService.onStartCommand', 'S_SERVICE', 'LIFECYCLE', 'onStartCommand starts the background extraction work, so a service is running', evidence='SRC asynchronous/services/ExtractService.java:97 public int onStartCommand(Intent, int, int)')

e('Drawer.open', 'S_DRAWER', 'CALL', 'open() opens the navigation drawer', evidence='SRC ui/views/drawer/Drawer.java:522 public void open() calls mDrawerLayout.openDrawer')

e('MainActivity.onDestroy', 'S_EXIT', 'LIFECYCLE', 'onDestroy ends the activity; the process is leaving the main screen', evidence='SRC activities/MainActivity.java:1204 protected void onDestroy()')

SCREENS.pop('S_DIALOG', None)
