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

e('MainActivity.searchMenuItem.click', 'MainFragment.onSearchPreExecute', 'CALL',
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
    'MainFragment.lambda$reloadListElements$5': ('no_trigger_in_app',
        'Synthetic lambda in method_list but AppBarLayout.OnOffsetChangedListener at line 1149-1151 is anonymous class, not separate lambda method',
        'SRC fragments/MainFragment.java:1149-1151 shows anonymous class; lambda$reloadListElements$5 not in source',
        'SOURCE'),
    
    'MainFragment.lambda$reauthenticateSmb$10': ('no_trigger_in_app',
        'Synthetic lambda in method_list but reauthenticateSmb.runOnUiThread at line 1346 is anonymous Runnable, not separate lambda method',
        'SRC fragments/MainFragment.java:1346-1352 shows anonymous Runnable; lambda$reauthenticateSmb$10 not in source',
        'SOURCE'),
}
