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
