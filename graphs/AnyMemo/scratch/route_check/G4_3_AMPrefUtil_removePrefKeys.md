# G4-3: AMPrefUtil.removePrefKeys

- Method: AMPrefUtil.removePrefKeys (utils/AMPrefUtil.java:74-83). Loops over settings.getAll(), editor.remove(key) when key.contains(keyContains), then editor.commit(). No early return.
- Label: REACHABLE (cold start AnyMemo -> Recent tab (auto-selected) -> tap Open tab -> FileBrowserFragment menu Create DB -> dialog OK with an existing file name -> AMFileUtil.deleteFileWithBackup -> deleteDbSafe -> removePrefKeys)
- Steps: 16 (show_route.py --dedupe). Checked: 16.
- Verdict: WRONG (4 wrong steps: 9, 14, 15, 16)

## Wrong steps

Step 9: S_MAIN_OPEN -> FileBrowserFragment.onCreateOptionsMenu (LIFECYCLE), graph_def.py:541 (FB_PAGES loop).
- Wrong: the framework calls onCreateOptionsMenu only when mHasMenu is set. Fragment.java:2626-2629 (`if (!mHidden) { if (mHasMenu && mMenuVisible) { ... onCreateOptionsMenu(menu, inflater);`). mHasMenu is set only by setHasOptionsMenu (Fragment.java:940-946). FileBrowserFragment sets it in onCreate (FileBrowserFragment.java:173). The route skips onCreate, so the menu flag is never set and no menu exists for step 10.
- Fix: remove 'onCreateOptionsMenu' from the tuple at graph_def.py:541. Do it for every FB_PAGES host, since the same direct edge exists for each. Add hand edges S_MAIN_OPEN -> OpenTabFragment.onAttach (graph_def.py:586, already there) -> FileBrowserFragment.onCreate (LIFECYCLE) -> FileBrowserFragment.onCreateOptionsMenu (FRAMEWORK, guard='setHasOptionsMenu(true) ran in onCreate (FileBrowserFragment.java:173)').

Step 14: DatabaseOperationDialogUtil$1$3.onClick -> AMFileUtil.deleteFileWithBackup (CALL), DatabaseOperationDialogUtil.java:58. Guard at :57 is correct; the STATE is missing.
- Wrong (state): this call needs a DB file with the typed name to exist already. The graph has the guard text but no needs_state, and the route's state is '-'. Nothing on this route creates that file, so the state must come from an earlier Create DB or from a fixture.
- Fix: in the dict at graph_def.py:2772, add needs_state with kind 'file' and text 'a database file with the typed name already exists in the current folder (made by an earlier Create DB or a fixture)'. Keep the guard.

Step 15: AMFileUtil.deleteFileWithBackup -> AMFileUtil.deleteDbSafe (CALL), AMFileUtil.java:80.
- Wrong (guard): the method returns at once when the file is missing (AMFileUtil.java:72-73, `if (!new File(filepath).exists()) { return; }`). Everything after it, including the call at :80, runs only when the file exists. On this route step 14 makes that true, but the graph shows no guard.
- Fix: guard='the file exists (AMFileUtil.java:72-73 early return)' on this edge.

Step 16: AMFileUtil.deleteDbSafe -> AMPrefUtil.removePrefKeys (CALL), AMFileUtil.java:66.
- Wrong (guard): deleteDbSafe returns at once when the file is missing (AMFileUtil.java:59-60). The call at :66 is after that early return. The graph shows no guard.
- Fix: guard='the file exists (AMFileUtil.java:59-60 early return)' on this edge.

## Steps checked and OK

1. ENTRY: AndroidManifest.xml:23-46 (MAIN/LAUNCHER on ui.AnyMemo) OK.
2. AnyMemo.<init> -> AnyMemo.onCreate (LIFECYCLE): AnyMemo.java:116 OK. The framework part is cited in the graph without line numbers. The printed lines are FW-SRC core/java/android/app/Activity.java:6989-6999 (performCreate calls onCreate(icicle) at :6997/:6999). Fix the citation to these lines (not counted as wrong).
3. onCreate -> loadUiComponents: guard (API <= 29, WRITE_EXTERNAL_STORAGE granted, !isUiLoaded) matches AnyMemo.java:124-134 OK.
4. loadUiComponents -> initDrawer: AnyMemo.java:187 OK.
5. initDrawer -> AnyMemo$2.onNavigationItemSelected@INIT: setSelectedItemId at :263, after the listener is set at :234. Library dispatch INFERRED (Material BottomNavigationView not read).
6. Guard itemId == recent_tab_menu (AnyMemo.java:240-241) OK.
7. Tap on the bottom nav (S_MAIN_RECENT -> listener, AnyMemo.java:234-236): dispatch INFERRED. OK.
8. Guard itemId == open_tab_menu (AnyMemo.java:242-246); commit at :253-257 under `if (fragment != null)`. OK.
10. onCreateOptionsMenu -> onOptionsItemSelected on tap: onOptionsItemSelected at FileBrowserFragment.java:289-291; the item file_browser_createdb is in res/menu/file_browser_menu.xml:4. Dispatch INFERRED. The menu itself exists only after the step 9 fix. OK.
11. onOptionsItemSelected -> DatabaseOperationDialogUtil.showCreateDbDialog: guard itemId == file_browser_createdb (FileBrowserFragment.java:291); call at :292 (bytecode line matches). OK.
12. showCreateDbDialog -> DatabaseOperationDialogUtil$1.subscribe (FRAMEWORK, Rx): Maybe.create(new MaybeOnSubscribe) at :41. Subscription called by Rx at :292-294. RxJava source not read, INFERRED. OK.
13. $1.subscribe -> $1$3.onClick: the compiled class $1$3 holds onClick, onSuccess, deleteFileWithBackup and createDbFileWithDefaultSettings (constant pool). That makes it the positive listener set at DatabaseOperationDialogUtil.java:48. The class names are not in source order ($1$1 is the cancel listener), so the name comes from the class file, not from position. Dialog dispatch INFERRED (AlertDialog not read). OK. The edge text should name the OK tap.

## Not checked

- androidx DialogFragment/AlertDialog dispatch, RxJava subscribe ordering, AppCompat options-menu dispatch: no source in the tree, INFERRED stays.
- Step 14 needs a DB file with the typed name in the Open folder: confirm on the API 27 emulator (DEVICE) with a fixture.
