STATUS: RUNNING 21:45

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| MainActivity.<clinit> | REACHABLE | | Static initializer called by framework when class loads | SRC MainActivity.java:161 static final Pattern DIR_SEPARATOR = Pattern.compile("/") |
| MainActivity.<init> | REACHABLE | | Constructor called by framework for LAUNCHER and other intent-filters | SRC AndroidManifest.xml:62-113 nine intent-filters for MainActivity |
| MainActivity.onCreate | REACHABLE | | Lifecycle method called by framework after constructor | SRC MainActivity.java:277-434 onCreate implementation |
| MainActivity.initialisePreferences | REACHABLE | | Called from onCreate | SRC MainActivity.java:280 initialisePreferences() |
| MainActivity.initializeInteractiveShell | REACHABLE | | Called from onCreate | SRC MainActivity.java:281 initializeInteractiveShell() |
| MainActivity.initialiseViews | REACHABLE | | Called from onCreate | SRC MainActivity.java:293 initialiseViews() |
| MainActivity.initialiseFab | REACHABLE | | Called from onCreate | SRC MainActivity.java:298 initialiseFab() |
| MainActivity.checkForExternalIntent | REACHABLE | | Called from onCreate and onNewIntent | SRC MainActivity.java:313,1602 checkForExternalIntent(intent) |
| MainActivity.checkForExternalPermission | REACHABLE | | Called from onCreate | SRC MainActivity.java:359 checkForExternalPermission() |
| MainActivity.initFabToSave | REACHABLE | | Called from checkForExternalIntent for SEND intents | SRC MainActivity.java:531,537 initFabToSave(uris) or initFabToSave(arrayList) |
| MainActivity.goToMain | REACHABLE | | Called from onCreate async, onBackPressed, onNewIntent | SRC MainActivity.java:411,415,418,739,743,745,1580 goToMain calls |
| MainActivity.openCompressed | REACHABLE | | Called from goToMain when openzip flag is set | SRC MainActivity.java:799-801 if(openzip && zippath != null) openCompressed(zippath) |
| MainActivity.onPostCreate | REACHABLE | | Lifecycle method called by framework after onCreate | SRC MainActivity.java:1060 onPostCreate override |
| MainActivity.onResume | REACHABLE | | Lifecycle method called by framework when activity visible | SRC MainActivity.java:1105 onResume override |
| MainActivity.updateUsbInformation | REACHABLE | | Called from onResume on API 19+ | SRC MainActivity.java:1121-1123 if SDK_INT >= KITKAT updateUsbInformation() |
| MainActivity.onPause | REACHABLE | | Lifecycle method called by framework on focus loss | SRC MainActivity.java:1093 onPause override |
| MainActivity.killToast | REACHABLE | | Called from onPause | SRC MainActivity.java:1101 killToast() |
| MainActivity.onSaveInstanceState | REACHABLE | | Lifecycle method called by framework before stop | SRC MainActivity.java:1074 onSaveInstanceState override |
| MainActivity.onConfigurationChanged | REACHABLE | | Lifecycle method called by framework on config change | SRC MainActivity.java:1067 onConfigurationChanged override |
| MainActivity.onDestroy | REACHABLE | | Lifecycle method called by framework on destroy | SRC MainActivity.java:1204 onDestroy override |
| MainActivity.closeInteractiveShell | REACHABLE | | Called from onDestroy | SRC MainActivity.java:1208 closeInteractiveShell() |
| MainActivity.onCreateOptionsMenu | REACHABLE | | Menu lifecycle called by framework | SRC MainActivity.java:804 onCreateOptionsMenu override |
| MainActivity.onPrepareOptionsMenu | REACHABLE | | Menu lifecycle called by framework before menu shown | SRC MainActivity.java:834 onPrepareOptionsMenu override |
| MainActivity.invalidatePasteButton | REACHABLE | | Called from onPrepareOptionsMenu | SRC MainActivity.java:863,915 invalidatePasteButton(paste) |
| MainActivity.onOptionsItemSelected | REACHABLE | | Menu lifecycle called by framework on item click | SRC MainActivity.java:928 onOptionsItemSelected override |
| MainActivity.exit | REACHABLE | | Called from onOptionsItemSelected for exit menu | SRC MainActivity.java:973 case R.id.exit finish() |
| MainActivity.updatePaths | REACHABLE | | Called from onOptionsItemSelected for sethome action | SRC MainActivity.java:961 updatePaths(main.no) |
| MainActivity.showToast | REACHABLE | | Called from exit and other UI methods | SRC MainActivity.java:774 showToast(getString(R.string.press_again)) |
| MainActivity.onActivityResult | REACHABLE | | Lifecycle method called by framework after startActivityForResult | SRC MainActivity.java:1306 onActivityResult override |
| MainActivity.onBackPressed | REACHABLE | | Lifecycle method called by framework on back button | SRC MainActivity.java:703 onBackPressed override |
| MainActivity.onNewIntent | REACHABLE | | Lifecycle called by framework for singleInstance launchMode | SRC AndroidManifest.xml:60 singleInstance; MainActivity.java:1568 onNewIntent override |
| MainActivity.onKeyDown | REACHABLE | | Lifecycle called by framework for key events | SRC MainActivity.java:1188 onKeyDown override |
| MainActivity.onCreateLoader | REACHABLE | | LoaderCallbacks method called by framework | SRC MainActivity.java:299 initLoader triggers; MainActivity.java:1832 onCreateLoader |
| MainActivity.onLoadFinished | REACHABLE | | LoaderCallbacks method called by framework | SRC MainActivity.java:1902 onLoadFinished |
| MainActivity.onLoaderReset | REACHABLE | | LoaderCallbacks method called by framework | SRC MainActivity.java:1927 onLoaderReset |
| MainActivity.getCurrentMainFragment | REACHABLE | | Called from multiple methods | SRC MainActivity.java:717,853,936,1367,1388,1392,1575,1698 getCurrentMainFragment calls |
| MainActivity.getTabFragment | REACHABLE | | Called from getCurrentMainFragment and setPagingEnabled | SRC MainActivity.java:1253,1272 getTabFragment calls |
| MainActivity.getFragmentAtFrame | REACHABLE | | Called from getTabFragment, onBackPressed, onPrepareOptionsMenu, onOptionsItemSelected | SRC MainActivity.java:710,720,724,843,974,1030,1261 getFragmentAtFrame calls |
| MainActivity.getFAB | REACHABLE | | Getter for FAB component | SRC MainActivity.java:1294 getFAB return floatingActionButton |
| MainActivity.getAppbar | REACHABLE | | Getter for appbar component | SRC MainActivity.java:287-291,710,1039,1298,1425 getAppbar calls |
| MainActivity.getDrawer | REACHABLE | | Getter for drawer component | SRC MainActivity.java:318,704-706,1302,1693,1727 drawer/getDrawer calls |
| MainActivity.getStorageDirectories | REACHABLE | | Returns storage paths | SRC MainActivity.java:624 getStorageDirectories implementation |
| MainActivity.getUsbDrive | REACHABLE | | Called from getStorageDirectories | SRC MainActivity.java:697 File usb = getUsbDrive() |
| MainActivity.setPagingEnabled | REACHABLE | | Controls ViewPager paging | SRC MainActivity.java:1271 setPagingEnabled |
| MainActivity.copyToClipboard | REACHABLE | | Utility for clipboard operations | SRC MainActivity.java:1537 copyToClipboard implementation |
| MainActivity.renameBookmark | REACHABLE | | BookmarkCallback interface method | SRC MainActivity.java:157 implements BookmarkCallback; MainActivity.java:1550 renameBookmark |
| MainActivity.delete | REACHABLE | | BookmarkCallback interface method | SRC MainActivity.java:157 implements BookmarkCallback; MainActivity.java:1757 delete |
| MainActivity.modify | REACHABLE | | BookmarkCallback interface method | SRC MainActivity.java:157 implements BookmarkCallback; MainActivity.java:1765 modify |
| MainActivity.getPaste | REACHABLE | | Getter for paste helper | SRC MainActivity.java:1558 return pasteHelper |
| MainActivity.setPaste | REACHABLE | | Setter for paste helper | SRC MainActivity.java:1562 pasteHelper = p |
| MainActivity.showSMBDialog | REACHABLE | | SmbConnectionListener interface method | SRC MainActivity.java:157 implements SmbConnectionListener; MainActivity.java:1622 showSMBDialog |
| MainActivity.showSftpDialog | REACHABLE | | Shows SFTP connection dialog | SRC MainActivity.java:1637 showSftpDialog |
| MainActivity.showSmokeScreen | REACHABLE | | Shows overlay screen | SRC MainActivity.java:1670 fabBgView.show() |
| MainActivity.hideSmokeScreen | REACHABLE | | Hides overlay screen | SRC MainActivity.java:1674 fabBgView.hide() |
| MainActivity.addConnection | REACHABLE | | SmbConnectionListener interface method for SMB/SFTP connections (6 params) | SRC MainActivity.java:157 implements SmbConnectionListener; MainActivity.java:1679-1710 addConnection with edit, name, path, encryptedPath, oldname, oldPath |
| MainActivity.addConnection | REACHABLE | | CloudConnectionCallbacks interface method for cloud connections (OpenMode param) | SRC MainActivity.java:157 implements CloudConnectionCallbacks; MainActivity.java:1794-1821 addConnection(OpenMode service) |
| MainActivity.deleteConnection | REACHABLE | | SmbConnectionListener interface method for SMB/SFTP (name, path) | SRC MainActivity.java:157 implements SmbConnectionListener; MainActivity.java:1714-1728 deleteConnection(String name, String path) |
| MainActivity.deleteConnection | REACHABLE | | CloudConnectionCallbacks interface method for cloud (OpenMode) | SRC MainActivity.java:157 implements CloudConnectionCallbacks; MainActivity.java:1823-1827 deleteConnection(OpenMode service) |
| MainActivity.onHiddenFileAdded | REACHABLE | | DataChangeListener callback | SRC MainActivity.java:283 registerOnDataChangedListener; MainActivity.java:1731 onHiddenFileAdded |
| MainActivity.onHiddenFileRemoved | REACHABLE | | DataChangeListener callback | SRC MainActivity.java:283 registerOnDataChangedListener; MainActivity.java:1736 onHiddenFileRemoved |
| MainActivity.onHistoryAdded | REACHABLE | | DataChangeListener callback | SRC MainActivity.java:283 registerOnDataChangedListener; MainActivity.java:1741 onHistoryAdded |
| MainActivity.onBookAdded | REACHABLE | | DataChangeListener callback | SRC MainActivity.java:283 registerOnDataChangedListener; MainActivity.java:1746 onBookAdded |
| MainActivity.onHistoryCleared | REACHABLE | | DataChangeListener callback | SRC MainActivity.java:283 registerOnDataChangedListener; MainActivity.java:1752 onHistoryCleared |
| MainActivity.onPreExecute | REACHABLE | | SearchWorkerFragment.HelperCallbacks interface | SRC MainActivity.java:157 implements HelperCallbacks; MainActivity.java:1771 onPreExecute |
| MainActivity.onPostExecute | REACHABLE | | SearchWorkerFragment.HelperCallbacks interface | SRC MainActivity.java:157 implements HelperCallbacks; MainActivity.java:1777 onPostExecute |
| MainActivity.onProgressUpdate | REACHABLE | | SearchWorkerFragment.HelperCallbacks interface | SRC MainActivity.java:157 implements HelperCallbacks; MainActivity.java:1783 onProgressUpdate |
| MainActivity.onCancelled | REACHABLE | | SearchWorkerFragment.HelperCallbacks interface | SRC MainActivity.java:157 implements HelperCallbacks; MainActivity.java:1788 onCancelled |
| MainActivity.initFabTitle | REACHABLE | | Called from initialiseFab | SRC MainActivity.java:1502-1504 three initFabTitle calls |
| MainActivity.updateViews | REACHABLE | | Updates UI component colors | SRC MainActivity.java:1473 updateViews implementation |
| MainActivity.lambda$onCreate$0 | REACHABLE | | Lambda from onCreate AppConfig.runInParallel | SRC MainActivity.java:367-383 doInBackground and onPostExecute in anonymous class |
| MainActivity.lambda$checkForExternalPermission$1 | REACHABLE | | Lambda from checkForExternalPermission requestStoragePermission | SRC MainActivity.java:440-472 requestStoragePermission callback |
| MainActivity.lambda$initFabToSave$2 | REACHABLE | | Lambda from initFabToSave FAB click listener | SRC MainActivity.java:560-576 setOnClickListener lambda |
| MainActivity.lambda$exit$3 | REACHABLE | | Lambda from exit Handler.postDelayed | SRC MainActivity.java:775-777 postDelayed lambda |
| MainActivity.lambda$onOptionsItemSelected$4 | REACHABLE | | Lambda from onOptionsItemSelected dialog positive button | SRC MainActivity.java:960-963 dialog positive button lambda |
| MainActivity.lambda$onOptionsItemSelected$5 | REACHABLE | | Lambda from onOptionsItemSelected directory sort dialog | SRC MainActivity.java:996-1001 items callback lambda |
| MainActivity.lambda$onOptionsItemSelected$6 | REACHABLE | | Lambda from onOptionsItemSelected view toggle background task | SRC MainActivity.java:1012-1015 runInBackground lambda |
| MainActivity.lambda$onOptionsItemSelected$7 | REACHABLE | | Lambda from onOptionsItemSelected view toggle background task | SRC MainActivity.java:1021-1024 runInBackground lambda |
| MainActivity.lambda$initialiseViews$8 | REACHABLE | | Lambda from initialiseViews fabBgView click listener | SRC MainActivity.java:1442-1444 setOnClickListener lambda |
| MainActivity.lambda$addConnection$9 | REACHABLE | | Lambda from addConnection background task | SRC MainActivity.java:1707-1709 runInBackground lambda |
| MainActivity.lambda$deleteConnection$10 | REACHABLE | | Lambda from deleteConnection background task | SRC MainActivity.java:1721-1724 runInBackground lambda |

STATUS: DONE 21:49
