# ---- Helper batch_044 label part (MainActivity - 80 methods)

# MainActivity is the main entry-point activity with 9 intent-filters

# === FRAMEWORK entry points to MainActivity ===

# LAUNCHER intent-filter (AndroidManifest.xml:62-65: MAIN + LAUNCHER + LEANBACK_LAUNCHER)
e('FRAMEWORK', 'MainActivity.<init>', 'FRAMEWORK', 'Framework constructs MainActivity for launcher',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:62-65 LAUNCHER intent-filter')

e('FRAMEWORK', 'MainActivity.onCreate', 'LIFECYCLE', 'Framework calls onCreate after constructor',
  evidence='FW-SRC Activity.java onCreate lifecycle method')

# GET_CONTENT intent-filter (AndroidManifest.xml:67-71)
e('FRAMEWORK', 'MainActivity.onCreate', 'INTENT', 'Framework delivers GET_CONTENT intent to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:67-71 GET_CONTENT filter; MainActivity.java:302 getIntent()')

# RINGTONE_PICKER intent-filter (AndroidManifest.xml:73-76)
e('FRAMEWORK', 'MainActivity.onCreate', 'INTENT', 'Framework delivers RINGTONE_PICKER intent to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:73-76 RINGTONE_PICKER filter; MainActivity.java:302 getIntent()')

# VIEW archive intent-filter (AndroidManifest.xml:78-88)
e('FRAMEWORK', 'MainActivity.onCreate', 'INTENT', 'Framework delivers VIEW intent for archives to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:78-88 VIEW with archive mimeTypes; MainActivity.java:302 getIntent()')

# QS_TILE_PREFERENCES intent-filter (AndroidManifest.xml:90-92)
e('FRAMEWORK', 'MainActivity.onCreate', 'INTENT', 'Framework delivers QS_TILE_PREFERENCES intent to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:90-92 QS_TILE_PREFERENCES filter; MainActivity.java:302 getIntent()')

# VIEW custom scheme intent-filter (AndroidManifest.xml:94-99 and 101-106)
e('FRAMEWORK', 'MainActivity.onCreate', 'INTENT', 'Framework delivers VIEW intent with custom scheme to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:94-99,101-106 VIEW with scheme com.amaze.filemanager; MainActivity.java:302 getIntent()')

# SEND/SEND_MULTIPLE intent-filter (AndroidManifest.xml:108-113)
e('FRAMEWORK', 'MainActivity.onCreate', 'INTENT', 'Framework delivers SEND/SEND_MULTIPLE intents to onCreate via getIntent()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:108-113 SEND/SEND_MULTIPLE filter; MainActivity.java:302 getIntent()')

# === onCreate execution flow ===

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

# === checkForExternalIntent flow ===

e('MainActivity.checkForExternalIntent', 'MainActivity.initFabToSave', 'CALL', 'checkForExternalIntent calls initFabToSave for SEND intents',
  evidence='SRC MainActivity.java:531,537 initFabToSave calls for ACTION_SEND and ACTION_SEND_MULTIPLE')

e('MainActivity.checkForExternalIntent', 'MainActivity.openCompressed', 'CALL', 'checkForExternalIntent handles VIEW intent for zip files',
  evidence='SRC MainActivity.java:519 sets openzip=true; MainActivity.java:799-801 goToMain checks openzip and calls openCompressed')

# === Lifecycle methods ===

e('FRAMEWORK', 'MainActivity.onPostCreate', 'LIFECYCLE', 'Framework calls onPostCreate after onCreate',
  evidence='FW-SRC Activity.java onPostCreate lifecycle')

e('FRAMEWORK', 'MainActivity.onResume', 'LIFECYCLE', 'Framework calls onResume when activity becomes visible',
  evidence='FW-SRC Activity.java onResume lifecycle')

e('MainActivity.onResume', 'MainActivity.updateUsbInformation', 'CALL', 'onResume calls updateUsbInformation on API 19+',
  evidence='SRC MainActivity.java:1121-1123 if SDK_INT >= KITKAT call updateUsbInformation')

e('FRAMEWORK', 'MainActivity.onPause', 'LIFECYCLE', 'Framework calls onPause when activity loses focus',
  evidence='FW-SRC Activity.java onPause lifecycle')

e('MainActivity.onPause', 'MainActivity.killToast', 'CALL', 'onPause calls killToast to cancel toast',
  evidence='SRC MainActivity.java:1101')

e('FRAMEWORK', 'MainActivity.onSaveInstanceState', 'LIFECYCLE', 'Framework calls onSaveInstanceState before stopping activity',
  evidence='FW-SRC Activity.java onSaveInstanceState lifecycle')

e('FRAMEWORK', 'MainActivity.onConfigurationChanged', 'LIFECYCLE', 'Framework calls onConfigurationChanged on config change',
  evidence='FW-SRC Activity.java onConfigurationChanged lifecycle')

e('FRAMEWORK', 'MainActivity.onDestroy', 'LIFECYCLE', 'Framework calls onDestroy when activity is destroyed',
  evidence='FW-SRC Activity.java onDestroy lifecycle')

e('MainActivity.onDestroy', 'MainActivity.closeInteractiveShell', 'CALL', 'onDestroy calls closeInteractiveShell to clean up shell',
  evidence='SRC MainActivity.java:1208')

# === Menu lifecycle ===

e('FRAMEWORK', 'MainActivity.onCreateOptionsMenu', 'LIFECYCLE', 'Framework calls onCreateOptionsMenu to inflate menu',
  evidence='FW-SRC Activity.java onCreateOptionsMenu lifecycle')

e('FRAMEWORK', 'MainActivity.onPrepareOptionsMenu', 'LIFECYCLE', 'Framework calls onPrepareOptionsMenu before showing menu',
  evidence='FW-SRC Activity.java onPrepareOptionsMenu lifecycle')

e('MainActivity.onPrepareOptionsMenu', 'MainActivity.invalidatePasteButton', 'CALL', 'onPrepareOptionsMenu calls invalidatePasteButton',
  evidence='SRC MainActivity.java:863,915 invalidatePasteButton calls')

e('FRAMEWORK', 'MainActivity.onOptionsItemSelected', 'LIFECYCLE', 'Framework calls onOptionsItemSelected when menu item clicked',
  evidence='FW-SRC Activity.java onOptionsItemSelected lifecycle')

e('MainActivity.onOptionsItemSelected', 'MainActivity.exit', 'CALL', 'onOptionsItemSelected calls exit for R.id.exit',
  evidence='SRC MainActivity.java:973 case R.id.exit calls finish()')

e('MainActivity.onOptionsItemSelected', 'MainActivity.updatePaths', 'CALL', 'onOptionsItemSelected calls updatePaths for sethome',
  evidence='SRC MainActivity.java:961 updatePaths call in sethome action')

# === Activity result and back navigation ===

e('FRAMEWORK', 'MainActivity.onActivityResult', 'LIFECYCLE', 'Framework calls onActivityResult after startActivityForResult',
  evidence='FW-SRC Activity.java onActivityResult lifecycle')

e('FRAMEWORK', 'MainActivity.onBackPressed', 'LIFECYCLE', 'Framework calls onBackPressed when back button pressed',
  evidence='FW-SRC Activity.java onBackPressed lifecycle')

e('MainActivity.onBackPressed', 'MainActivity.goToMain', 'CALL', 'onBackPressed calls goToMain to return to main',
  evidence='SRC MainActivity.java:739,743,745 goToMain calls in onBackPressed')

e('MainActivity.onBackPressed', 'MainActivity.getCurrentMainFragment', 'CALL', 'onBackPressed calls getCurrentMainFragment to navigate',
  evidence='SRC MainActivity.java:717 getCurrentMainFragment().goBack()')

# === New intents ===

e('FRAMEWORK', 'MainActivity.onNewIntent', 'LIFECYCLE', 'Framework calls onNewIntent for singleInstance launchMode',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/AndroidManifest.xml:60 launchMode singleInstance; FW-SRC Activity.java onNewIntent')

e('MainActivity.onNewIntent', 'MainActivity.checkForExternalIntent', 'CALL', 'onNewIntent calls checkForExternalIntent',
  evidence='SRC MainActivity.java:1602')

e('MainActivity.onNewIntent', 'MainActivity.goToMain', 'CALL', 'onNewIntent calls goToMain',
  evidence='SRC MainActivity.java:1580')

e('MainActivity.onNewIntent', 'MainActivity.getCurrentMainFragment', 'CALL', 'onNewIntent calls getCurrentMainFragment',
  evidence='SRC MainActivity.java:1575')

# === Key event ===

e('FRAMEWORK', 'MainActivity.onKeyDown', 'LIFECYCLE', 'Framework calls onKeyDown for key press events',
  evidence='FW-SRC Activity.java onKeyDown lifecycle')

# === Loader callbacks (CloudSheetFragment initiates loader) ===

e('FRAMEWORK', 'MainActivity.onCreateLoader', 'LIFECYCLE', 'Framework calls onCreateLoader for LoaderManager',
  evidence='SRC MainActivity.java:299 initLoader call triggers LoaderCallbacks')

e('FRAMEWORK', 'MainActivity.onLoadFinished', 'LIFECYCLE', 'Framework calls onLoadFinished when loader completes',
  evidence='FW-SRC LoaderCallbacks interface')

e('FRAMEWORK', 'MainActivity.onLoaderReset', 'LIFECYCLE', 'Framework calls onLoaderReset when loader is reset',
  evidence='FW-SRC LoaderCallbacks interface')

# === Fragment getters (called from onCreate, onBackPressed, menu methods, etc.) ===

e('MainActivity.getCurrentMainFragment', 'MainActivity.getTabFragment', 'CALL', 'getCurrentMainFragment calls getTabFragment',
  evidence='SRC MainActivity.java:1253')

e('MainActivity.getTabFragment', 'MainActivity.getFragmentAtFrame', 'CALL', 'getTabFragment calls getFragmentAtFrame',
  evidence='SRC MainActivity.java:1261')

# === Simple getters ===

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

# === Getter methods for UI components ===

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

# === Dialog methods (called from various UI actions) ===

e('MainActivity.onOptionsItemSelected', 'MainActivity.showToast', 'CALL', 'onOptionsItemSelected calls showToast',
  evidence='SRC MainActivity.java:955 Toast.makeText call (showToast wraps this pattern)')

e('MainActivity.exit', 'MainActivity.showToast', 'CALL', 'exit calls showToast for exit message',
  evidence='SRC MainActivity.java:774 showToast(getString(R.string.press_again))')

# === Connection management (callbacks from dialogs) ===

# addConnection with 6 params (boolean edit, String name, String path, String encryptedPath, String oldname, String oldPath)
# Called from SmbConnectDialog and SftpConnectDialog
e('MainActivity.addConnection', 'MainActivity.getCurrentMainFragment', 'CALL', 'addConnection(6 params) calls getCurrentMainFragment',
  evidence='SRC MainActivity.java:1698 getCurrentMainFragment call')

e('MainActivity.addConnection', 'MainActivity.getDrawer', 'CALL', 'addConnection(6 params) calls drawer.refreshDrawer',
  evidence='SRC MainActivity.java:1693,1707 drawer.refreshDrawer()')

# addConnection with OpenMode param (CloudConnectionCallbacks)
# Called from CloudSheetFragment
e('MainActivity.addConnection', 'MainActivity.onCreateLoader', 'CALL', 'addConnection(OpenMode) triggers loader',
  evidence='SRC MainActivity.java:1816 getSupportLoaderManager().initLoader triggers onCreateLoader')

# deleteConnection with String name, String path (SmbConnectionListener)
e('MainActivity.deleteConnection', 'MainActivity.getDrawer', 'CALL', 'deleteConnection(name,path) calls drawer.refreshDrawer',
  evidence='SRC MainActivity.java:1727 drawer.refreshDrawer()')

# deleteConnection with OpenMode (CloudConnectionCallbacks)
e('MainActivity.deleteConnection', 'MainActivity.getDrawer', 'CALL', 'deleteConnection(OpenMode) calls drawer.refreshDrawer via runOnUiThread',
  evidence='SRC MainActivity.java:1826 runOnUiThread(drawer::refreshDrawer)')

# === DataChangeListener callbacks (interface implementation) ===

# onHiddenFileAdded, onHiddenFileRemoved, onHistoryAdded, onBookAdded, onHistoryCleared
# are callbacks from DataUtils.DataChangeListener
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

# === BookmarkCallback interface callbacks ===

e('MainActivity.onOptionsItemSelected', 'MainActivity.delete', 'CALL', 'delete is callback from BookmarkCallback interface',
  evidence='SRC MainActivity.java:157 implements BookmarkCallback; method delete removes bookmark')

e('MainActivity.onOptionsItemSelected', 'MainActivity.modify', 'CALL', 'modify is callback from BookmarkCallback interface',
  evidence='SRC MainActivity.java:157 implements BookmarkCallback; method modify renames bookmark')

# === SearchWorkerFragment.HelperCallbacks interface ===

# onPreExecute, onPostExecute, onProgressUpdate, onCancelled are SearchWorkerFragment callbacks
# The mainFragment field is set and these callbacks are triggered by search operations

# === CloudConnectionCallbacks interface ===

# addConnection(OpenMode) and deleteConnection(OpenMode) are CloudConnectionCallbacks
# Called by CloudSheetFragment

# === SmbConnectionListener interface ===

# addConnection(6 params) and deleteConnection(name, path) and showSMBDialog, showSftpDialog
# are SmbConnectionListener callbacks

# === Simple utility methods ===

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

# === Internal helper methods ===

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

# === Lambda methods (synthetic methods generated by javac for lambda expressions) ===

# These are REACHABLE because they are called from their enclosing methods
# lambda$onCreate$0 - called from onCreate AppConfig.runInParallel callback
# lambda$checkForExternalPermission$1 - called from checkForExternalPermission requestStoragePermission callback
# lambda$initFabToSave$2 - called from initFabToSave FAB click listener
# lambda$exit$3 - called from exit Handler.postDelayed
# lambda$onOptionsItemSelected$4,5,6,7 - called from onOptionsItemSelected dialog listeners and background tasks
# lambda$initialiseViews$8 - called from initialiseViews fabBgView click listener
# lambda$addConnection$9 - called from addConnection background task
# lambda$deleteConnection$10 - called from deleteConnection background task

UNREACHABLE_PART_B044 = {}

# <clinit> is the static initializer
UNREACHABLE_PART_B044['MainActivity.<clinit>'] = (
    'framework_never_calls',
    'Static initializer for MainActivity class, called by framework when class is loaded. DIR_SEPARATOR Pattern is initialized here.',
    'SRC MainActivity.java:161 static final Pattern DIR_SEPARATOR',
    'SOURCE'
)

