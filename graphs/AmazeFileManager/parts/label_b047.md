STATUS: RUNNING 21:55

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| MainFragment.<init> | REACHABLE | | Framework instantiates MainFragment from TabFragment.addTab | SRC fragments/TabFragment.java:351 "Fragment main = new MainFragment()" |
| MainFragment.onCreate | REACHABLE | | Framework lifecycle method called after construction | SRC fragments/MainFragment.java:202-220 (method definition) |
| MainFragment.onCreateView | REACHABLE | | Framework lifecycle method called after onCreate | SRC fragments/MainFragment.java:237-269 (method definition) |
| MainFragment.onActivityCreated | REACHABLE | | Framework lifecycle method called after onCreateView | SRC fragments/MainFragment.java:271-340 (method definition) |
| MainFragment.onResume | REACHABLE | | Framework lifecycle method called when fragment becomes visible | SRC fragments/MainFragment.java:1419-1428 (method definition) |
| MainFragment.onPause | REACHABLE | | Framework lifecycle method called when fragment loses focus | SRC fragments/MainFragment.java:1433-1443 (method definition) |
| MainFragment.onStop | REACHABLE | | Framework lifecycle method called after onPause | SRC fragments/MainFragment.java:1446-1458 (method definition) |
| MainFragment.onDestroy | REACHABLE | | Framework lifecycle method called before fragment destruction | SRC fragments/MainFragment.java:1544-1548 (method definition) |
| MainFragment.onDetach | REACHABLE | | Framework lifecycle method called after onDestroy | SRC fragments/MainFragment.java:1698-1700 (method definition) |
| MainFragment.onSaveInstanceState | REACHABLE | | Framework lifecycle method called to save state before destruction | SRC fragments/MainFragment.java:397-430 (method definition) |
| MainFragment.onSavedInstanceState | REACHABLE | | Called from onActivityCreated to restore saved state | SRC fragments/MainFragment.java:432-459 and SRC fragments/MainFragment.java:320,337 (call sites) |
| MainFragment.getMainActivity | REACHABLE | | Called from onCreate, onCreateView, onActivityCreated, and throughout class | SRC fragments/MainFragment.java:1702-1704 and SRC fragments/MainFragment.java:207,242,281,1423 (call sites) |
| MainFragment.loadlist | REACHABLE | | Called from onActivityCreated, swipe refresh, navigation; loads file list | SRC fragments/MainFragment.java:1016-1031 and SRC fragments/MainFragment.java:334,260,894 (call sites) |
| MainFragment.lambda$onCreateView$0 | REACHABLE | | Lambda for listView.setOnTouchListener; calls stopAnimation | SRC fragments/MainFragment.java:244-248 (lambda body) |
| MainFragment.lambda$onCreateView$1 | REACHABLE | | Lambda for mToolbarContainer.setOnTouchListener; calls stopAnimation | SRC fragments/MainFragment.java:250-256 (lambda body) |
| MainFragment.lambda$onCreateView$2 | REACHABLE | | Lambda for mSwipeRefreshLayout.setOnRefreshListener; calls loadlist | SRC fragments/MainFragment.java:260 (lambda body) |
| MainFragment.stopAnimation | REACHABLE | | Called from touch listeners to stop list animations | SRC fragments/MainFragment.java:226-235 and SRC fragments/MainFragment.java:246,253 (call sites) |
| MainFragment.initNoFileLayout | REACHABLE | | Called from onActivityCreated to setup empty view | SRC fragments/MainFragment.java:1033-1055 and SRC fragments/MainFragment.java:276 (call site) |
| MainFragment.lambda$initNoFileLayout$4 | REACHABLE | | Lambda for nofilesview.setOnRefreshListener; calls loadlist | SRC fragments/MainFragment.java:1039-1042 (lambda body) |
| MainFragment.getSortModes | REACHABLE | | Called from onActivityCreated to initialize sort settings | SRC fragments/MainFragment.java:1405-1416 and SRC fragments/MainFragment.java:277 (call site) |
| MainFragment.setGridLayoutSpanSizeLookup | REACHABLE | | Called from onActivityCreated and switchToGrid for grid layout setup | SRC fragments/MainFragment.java:344-354 and SRC fragments/MainFragment.java:297,367 (call sites) |
| MainFragment.startFileObserver | REACHABLE | | Called from onResume and reloadListElements to watch file changes | SRC fragments/MainFragment.java:1177-1205 and SRC fragments/MainFragment.java:1428,1156 (call sites) |
| MainFragment.getBoolean | REACHABLE | | Called throughout class to get preference booleans | SRC fragments/MainFragment.java:1725-1727 and SRC fragments/MainFragment.java:302,1024,1089 (call sites) |
| MainFragment.lambda$loadlist$3 | REACHABLE | | Lambda callback for LoadFilesListTask; calls setListElements | SRC fragments/MainFragment.java:1023-1029 (lambda body) |
| MainFragment.setListElements | REACHABLE | | Called from LoadFilesListTask lambda to set file list data | SRC fragments/MainFragment.java:1065-1076 and SRC fragments/MainFragment.java:1026 (call site) |
| MainFragment.reloadListElements | REACHABLE | | Called from setListElements and switchView to render list/grid | SRC fragments/MainFragment.java:1079-1162 and SRC fragments/MainFragment.java:1071,393 (call sites) |
| MainFragment.getBackElement | REACHABLE | | Called from reloadListElements to create back button element | SRC fragments/MainFragment.java:1169-1174 and SRC fragments/MainFragment.java:1093 (call site) |
| MainFragment.switchToGrid | REACHABLE | | Called from reloadListElements to switch to grid view | SRC fragments/MainFragment.java:356-370 and SRC fragments/MainFragment.java:1101 (call site) |
| MainFragment.switchToList | REACHABLE | | Called from reloadListElements to switch to list view | SRC fragments/MainFragment.java:372-385 and SRC fragments/MainFragment.java:1102 (call site) |
| MainFragment.switchView | REACHABLE | | Called from MainActivity menu to toggle list/grid view | SRC fragments/MainFragment.java:391-394 |
| MainFragment.lambda$reloadListElements$6 | REACHABLE | | Lambda for FastScroller touch listener; calls stopAnimation | SRC fragments/MainFragment.java:1152-1157 (lambda body) |
| MainFragment.onListItemClicked | REACHABLE | | Called from RecyclerAdapter when list item clicked | SRC fragments/MainFragment.java:851-946 |
| MainFragment.goBackItemClick | REACHABLE | | Called from onListItemClicked and BottomBar back button | SRC fragments/MainFragment.java:1359-1390 and SRC fragments/MainFragment.java:884 (call site) |
| MainFragment.computeScroll | REACHABLE | | Called from onListItemClicked, updateList to save scroll position | SRC fragments/MainFragment.java:1252-1262 and SRC fragments/MainFragment.java:893,1394 (call sites) |
| MainFragment.returnIntentResults | REACHABLE | | Called from onListItemClicked when mReturnIntent is true (file picker) | SRC fragments/MainFragment.java:976-1013 and SRC fragments/MainFragment.java:908 (call site) |
| MainFragment.launchSMB | REACHABLE | | Static method called from onListItemClicked for SMB files | SRC fragments/MainFragment.java:1656-1695 and SRC fragments/MainFragment.java:912 (call site) |
| MainFragment.goBack | REACHABLE | | Called from MainActivity.onBackPressed for back navigation | SRC fragments/MainFragment.java:1265-1340 |
| MainFragment.reauthenticateSmb | REACHABLE | | Called from MainActivity on SMB authentication failure | SRC fragments/MainFragment.java:1344-1357 |
| MainFragment.updateList | REACHABLE | | Called from receiver2 broadcast and MainActivity to refresh list | SRC fragments/MainFragment.java:1393-1395 and SRC fragments/MainFragment.java:824 (call site) |
| MainFragment.receiver2 | REACHABLE | | BroadcastReceiver registered in onResume for KEY_INTENT_LOAD_LIST | SRC fragments/MainFragment.java:776-826 and SRC fragments/MainFragment.java:1422 (registration) |
| MainFragment.decryptReceiver | REACHABLE | | BroadcastReceiver registered in onResume for DECRYPT_BROADCAST | SRC fragments/MainFragment.java:828-837 and SRC fragments/MainFragment.java:1425-1426 (registration) |
| MainFragment.updateTabWithDb | REACHABLE | | Called from MainActivity.onCreate to restore tab from database | SRC fragments/MainFragment.java:967-971 and SRC activities/MainActivity.java:462,465 (call sites) |
| MainFragment.rename | REACHABLE | | Called from RecyclerAdapter for rename action | SRC fragments/MainFragment.java:1209-1247 |
| MainFragment.lambda$rename$7 | REACHABLE | | Lambda for rename dialog positive button | SRC fragments/MainFragment.java:1217-1226 (lambda body) |
| MainFragment.lambda$rename$8 | REACHABLE | | Lambda for rename text validation | SRC fragments/MainFragment.java:1227-1236 (lambda body) |
| MainFragment.lambda$rename$9 | REACHABLE | | Lambda for rename EditText cursor positioning | SRC fragments/MainFragment.java:1241-1245 (lambda body) |
| MainFragment.hide | REACHABLE | | Called from MainActivity to hide file/folder | SRC fragments/MainFragment.java:1551-1566 |
| MainFragment.addToSmb | REACHABLE | | Called from LoadFilesListTask for SMB file list | SRC fragments/MainFragment.java:1461-1496 |
| MainFragment.addTo | REACHABLE | | Private method called from addSearchResult to create layout element | SRC fragments/MainFragment.java:1499-1541 and SRC fragments/MainFragment.java:1621 (call site) |
| MainFragment.onSearchPreExecute | REACHABLE | | Called from SearchWorkerFragment before search starts | SRC fragments/MainFragment.java:1603-1606 |
| MainFragment.addSearchResult | REACHABLE | | Called from SearchWorkerFragment for each search result | SRC fragments/MainFragment.java:1611-1633 |
| MainFragment.onSearchCompleted | REACHABLE | | Called from SearchWorkerFragment when search finishes | SRC fragments/MainFragment.java:1635-1652 |
| MainFragment.addShortcut | REACHABLE | | Called from action mode menu for add shortcut action | SRC fragments/MainFragment.java:1573-1600 |
| MainFragment.home | REACHABLE | | Called from MainActivity to navigate to home directory | SRC fragments/MainFragment.java:839-841 |
| MainFragment.changePath | REACHABLE | | BottomBarButtonPath interface method called from BottomBar | SRC fragments/MainFragment.java:1711-1713 |
| MainFragment.getPath | REACHABLE | | BottomBarButtonPath interface method called from onResume | SRC fragments/MainFragment.java:1716-1718 and SRC fragments/MainFragment.java:1423 (call site) |
| MainFragment.getCurrentPath | REACHABLE | | Called from getPath and MainActivity | SRC fragments/MainFragment.java:1569-1571 and SRC fragments/MainFragment.java:1717 (call site) |
| MainFragment.getElementsList | REACHABLE | | Called from MainActivity to get current file list | SRC fragments/MainFragment.java:1706-1708 |
| MainFragment.getRootDrawable | REACHABLE | | BottomBarButtonPath interface method called from BottomBar | SRC fragments/MainFragment.java:1721-1723 |
| MainFragment.findEncryptedEntry | REACHABLE | | Static method called from EncryptDecryptUtils | SRC fragments/MainFragment.java:950-964 |
| MainFragment.lambda$reloadListElements$5 | UNREACHABLE | no_trigger_in_app | Synthetic lambda in method_list but AppBarLayout.OnOffsetChangedListener at line 1149-1151 is anonymous class, not separate lambda method | SRC fragments/MainFragment.java:1149-1151 shows anonymous class; lambda$reloadListElements$5 not in source |
| MainFragment.lambda$reauthenticateSmb$10 | UNREACHABLE | no_trigger_in_app | Synthetic lambda in method_list but reauthenticateSmb.runOnUiThread at line 1346 is anonymous Runnable, not separate lambda method | SRC fragments/MainFragment.java:1346-1352 shows anonymous Runnable; lambda$reauthenticateSmb$10 not in source |

STATUS: DONE 21:55
