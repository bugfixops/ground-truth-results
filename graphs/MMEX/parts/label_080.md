STATUS: RUNNING 15:42

# batch 080 (label_080): 40 methods of home/MainActivity (methods 1-40 of 83; graphs/MMEX/scratch/batches/batch_080.txt)
# Paths in the last column are relative to final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/ unless prefixed FW (relative to fw_src/android-8.1.0_r1/core/java/ or services/core/java/), MAN (relative to final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/) or RES (relative to the same app/src/main/ folder, res/).
# Source lines are the ones printed with sed -n and grep -n for this batch. "auto" means an auto CALL record in graphs/MMEX/auto_calls.json.
# Edges and UNREACHABLE entries: graphs/MMEX/parts/label_080.py.

| method | label | kind | reason | printed file:lines |
|---|---|---|---|---|
| MainActivity.<clinit> | REACHABLE | ENTRY | Static initializer: mRestartActivity (line 155) has a non-constant initializer, so the class has one. The launcher or a VIEW intent starts the class: S_ENTRY ENTRY edge in label_080.py. The JVM order (class init before the constructor) is INFERRED | home/MainActivity.java:155; MAN AndroidManifest.xml:135-174 |
| MainActivity.<init> | REACHABLE | ENTRY | Implicit constructor (the class declares none). Already reached from S_ENTRY by the two ENTRY edges in graph_def.py (launcher and VIEW intent). Its LIFECYCLE edge to onCreate is in label_080.py | home/MainActivity.java:133-134; graph_def.py:49-57 |
| MainActivity.changeDatabase | REACHABLE | CALL | auto calls: handleIntent at 1199 (VIEW intent, reached from onCreate at 210), onActivityResult at 316, 326, 332 (the SELECT_FILE, SELECT_DOCUMENT and CREATE_DOCUMENT results), and a call at 1364 (auto) | home/MainActivity.java:536-563; calls at 316, 326, 332, 1199, 1364 |
| MainActivity.createExpandableDrawer | REACHABLE | CALL | auto call from initializeDrawer (1289-1306), which onCreate calls at 240 | home/MainActivity.java:840-987; call at 846, 853 |
| MainActivity.createSyncToolbarItem | REACHABLE | CALL | auto call from onCreateOptionsMenu at 376, under the gate mIsSynchronizing (375). State gate kept REACHABLE (D19). The only write of true (line 494) is inside the UNREACHABLE onEvent(SyncStartingEvent), so this branch is dead in practice (open point) | home/MainActivity.java:375-377, 494, 989-1025 |
| MainActivity.destroySyncToolbarItem | REACHABLE | CALL | auto call from onCreateOptionsMenu at 380 (else branch: the common path when not syncing); it calls stopSyncIconRotation at 1037 | home/MainActivity.java:378-381, 1027-1040 |
| MainActivity.getContentId | REACHABLE | CALL | auto calls from initHomeFragment at 1318 (single-panel branch) and from the fragment routing at 738, 785, 803 (batch 008 route) | home/MainActivity.java:572-576; calls at 738, 785, 803, 1318 |
| MainActivity.getDatabases | REACHABLE | CALL | auto calls from onActivityResult (320), changeDatabase (559), onDrawerMenuAndOptionMenuSelected (596), getRecentDatabasesDrawerMenuItems (1131) and migrateRecentDatabases (1514) | home/MainActivity.java:1042-1044; calls at 320, 559, 596, 1131, 1514 |
| MainActivity.getDrawerMenuItems | REACHABLE | CALL | auto call from createExpandableDrawer at 846 | home/MainActivity.java:1046-1125; call at 846 |
| MainActivity.getNavigationId | REACHABLE | CALL | auto call from initHomeFragment at 1318 (dual-panel branch) | home/MainActivity.java:578-582; call at 1318 |
| MainActivity.getRecentDatabasesDrawerMenuItems | REACHABLE | CALL | auto call from createExpandableDrawer at 853 | home/MainActivity.java:1127-1160; call at 853 |
| MainActivity.getUiHelper | REACHABLE | CALL | auto call from getRecentDatabasesDrawerMenuItems at 1154 (folder icon) | home/MainActivity.java:1162-1167; call at 1154 |
| MainActivity.handleDeviceRotation | REACHABLE | CALL | auto call from onCreate at 217 | home/MainActivity.java:1169-1182; call at 217 |
| MainActivity.handleIntent | REACHABLE | CALL | auto call from onCreate at 210. A VIEW intent with data opens that database (1189-1199) | home/MainActivity.java:1184-1208; call at 210 |
| MainActivity.initHomeFragment | REACHABLE | CALL | auto call from onCreate at 238. Its ENTERS edge to S_HOME is in label_080.py; the FRAMEWORK edges to HomeFragment are in label_077.py:12-17 | home/MainActivity.java:1308-1324; call at 238 |
| MainActivity.initializeDrawer | REACHABLE | CALL | auto call from onCreate at 240 | home/MainActivity.java:1289-1306; call at 240 |
| MainActivity.initializeDrawerVariables | REACHABLE | CALL | auto call from initializeDrawer at 1300 | home/MainActivity.java:1326-1336; call at 1300 |
| MainActivity.initializeSync | REACHABLE | CALL | auto call from onCreate at 242. The return at 1212 when the sync is not active is a settings state gate, not a dead branch | home/MainActivity.java:1210-1229; call at 242, 1212 |
| MainActivity.isDatabaseAvailable | REACHABLE | CALL | auto call from showPrerequisite at 1486 (showPrerequisite is called from onCreate at 184) | home/MainActivity.java:1338-1349; call at 1486 |
| MainActivity.isDualPanel | REACHABLE | CALL | auto calls from getContentId (573), getNavigationId (579), initHomeFragment (1318) and lines 1451, 1459 | home/MainActivity.java:568-570; calls at 573, 579, 1318, 1451, 1459 |
| MainActivity.isRestartActivitySet | REACHABLE | CALL | auto call from onResume at 279 | home/MainActivity.java:141-147; call at 279 |
| MainActivity.isTutorialNeeded | REACHABLE | CALL | auto call from showPrerequisite at 1480 | home/MainActivity.java:1351-1353; call at 1480 |
| MainActivity.migrateRecentDatabases | REACHABLE | CALL | auto call from onCreate at 190 | home/MainActivity.java:1509-1528; call at 190 |
| MainActivity.onActivityResult | REACHABLE | RESULT | No auto record: the framework calls it (Activity.dispatchActivityResult). RESULT edges in label_080.py from PasswordActivity.returnPassword (REQUEST_PASSWORD) and PasscodeActivity$1.onClick (PASSCODE). The system picker results (SELECT_FILE, SELECT_DOCUMENT, CREATE_DOCUMENT) have no app node, so no edge (open point) | home/MainActivity.java:297-361; database/PasswordActivity.java:62-73; PasscodeActivity.java:125-126; FW core/java/android/app/Activity.java:7259-7266 |
| MainActivity.onBackPressed | REACHABLE | GUI | The Back key on the home screen: the framework calls this override (no auto record). GUI edge S_HOME to onBackPressed in label_080.py. The page is an open point | home/MainActivity.java:439-450; FW core/java/android/app/Activity.java:3001-3010 |
| MainActivity.onClickCardViewIncomesVsExpenses | REACHABLE | GUI | android:onClick on the Income vs Expenses card (RES layout/home_fragment.xml:127), inflated by HomeFragment at line 173. The handler resolves on the host activity (INFERRED: View.java not read). GUI edge S_HOME to here in label_080.py | home/MainActivity.java:832-834; RES layout/home_fragment.xml:119-129; home/HomeFragment.java:173 |
| MainActivity.onConfigurationChanged | UNREACHABLE | framework_never_calls | INFERRED. The manifest declares no configChanges (MAN AndroidManifest.xml:135-137), so a change that matters relaunches the activity (ActivityRecord.java:2450; shouldRelaunchLocked at 2527). A change with no diff is not delivered (ActivityRecord.java:2416-2426; ActivityThread.java:5033-5038). Residual: the order in the app queue of the relaunch and the process-level push (ActivityManagerService.java:20451-20457) was not traced. The auto call to setRestartActivity (line 366) is cut by sup | home/MainActivity.java:363-367; FW services/core/java/com/android/server/am/ActivityRecord.java:2416-2426, 2450, 2527; FW core/java/android/app/ActivityThread.java:5025-5038 |
| MainActivity.onCreate | REACHABLE | LIFECYCLE | From <init> (edge in label_080.py). The framework calls it after the instance is created. Its auto calls carry the rest of the start-up route | home/MainActivity.java:178-245; FW core/java/android/app/ActivityThread.java:2722-2731 |
| MainActivity.onCreateOptionsMenu | REACHABLE | FRAMEWORK | From onCreate (FRAMEWORK edge in label_080.py): PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu. The body inflates the menu and calls createSyncToolbarItem or destroySyncToolbarItem (auto, 376 and 380) | home/MainActivity.java:371-384; FW core/java/com/android/internal/policy/PhoneWindow.java:631; FW core/java/android/app/Activity.java:3386-3393 |
| MainActivity.onDestroy | REACHABLE | LIFECYCLE | From onCreate (185), onActivityResult (357), onBackPressed (445) and restartActivity (715): LIFECYCLE edges in label_080.py | home/MainActivity.java:430-437; calls and finish at 185, 357, 445, 715 |
| MainActivity.onDrawerMenuAndOptionMenuSelected | REACHABLE | CALL | auto calls from the postDelayed Runnables MainActivity$3$1.run (957) and MainActivity$4$1.run (978), which the drawer listeners start (those classes belong to other batches) | home/MainActivity.java:589-697; calls at 957, 978 |
| MainActivity.onEvent(AccountsTotalLoadedEvent) | REACHABLE | ASYNC | HomeFragment.onLoadFinished posts it (HomeFragment.java:297). REGISTER edge from MmxBaseFragmentActivity.onStart in label_080.py | home/MainActivity.java:480-483 |
| MainActivity.onEvent(RequestAccountFragmentEvent) | REACHABLE | ASYNC | HomeFragment$6.onChildClick posts it (704; account branch at 701-702). REGISTER edge | home/MainActivity.java:454-457 |
| MainActivity.onEvent(RequestOpenDatabaseEvent) | UNREACHABLE | no_trigger_in_app | No poster in the source root: the only mentions are the import (86) and this handler. SOURCE. Its auto calls to FileStorageHelper are cut by sup | home/MainActivity.java:86, 469-473 |
| MainActivity.onEvent(RequestPortfolioFragmentEvent) | REACHABLE | ASYNC | HomeFragment.onContextItemSelected posts it (HomeFragment.java:474, portfolio item). REGISTER edge | home/MainActivity.java:464-467 |
| MainActivity.onEvent(RequestWatchlistFragmentEvent) | REACHABLE | ASYNC | HomeFragment$6.onChildClick posts it (704; INVESTMENT branch at 699-700). REGISTER edge | home/MainActivity.java:459-462 |
| MainActivity.onEvent(UsernameLoadedEvent) | REACHABLE | ASYNC | HomeFragment$4.onSuccess posts it (HomeFragment.java:653). REGISTER edge | home/MainActivity.java:475-478 |
| MainActivity.onEvent(DbFileDownloadedEvent) | REACHABLE | ASYNC | SyncServiceMessageHandler.handleMessage posts it on DOWNLOAD_COMPLETE (line 89). REGISTER edge | home/MainActivity.java:526-530; sync/SyncServiceMessageHandler.java:84-90 |
| MainActivity.onEvent(SyncStartingEvent) | UNREACHABLE | no_trigger_in_app | The only poster, SyncService.sendStartEvent (post at line 241), has only commented call sites (lines 95, 108, 116, 186, 198). SOURCE. Its auto call to MainActivity$1.<init> is cut by sup | home/MainActivity.java:489-502; sync/SyncService.java:238-243 |
| MainActivity.onEvent(SyncStoppingEvent) | UNREACHABLE | no_trigger_in_app | The only poster, SyncService.sendStopEvent (post at line 247), has the same commented call sites. SOURCE. Its auto call to MainActivity$2.<init> is cut by sup | home/MainActivity.java:508-521; sync/SyncService.java:245-249 |

Counts: 40 rows; 36 REACHABLE; 4 UNREACHABLE (3 SOURCE, 1 INFERRED); 0 INCOMPLETE.
Edges in label_080.py: 24 (1 ENTRY, 5 LIFECYCLE, 1 FRAMEWORK, 2 RESULT, 1 ENTERS, 6 ASYNC, 6 REGISTER, 2 GUI). sup pairs: 5. UNREACHABLE entries: 4.
Files: graphs/MMEX/parts/label_080.md and graphs/MMEX/parts/label_080.py. No label_080.grep.txt (no UNREACHABLE method is library or generated).
Naming: method_list.json has HomeFragment$4.onSuccess and HomeFragment$4.onError (the SingleSubscriber, lines 649-660) and HomeFragment$5.call (the Callable, line 640). The labels follow those names.

Open points:
1. onConfigurationChanged: UNREACHABLE INFERRED. The residual is the order of the relaunch and the process-level config push (ActivityManagerService.java:20451-20457).
2. createSyncToolbarItem: REACHABLE with the mIsSynchronizing gate. The only write of true is inside the UNREACHABLE onEvent(SyncStartingEvent), so the branch is dead in practice.
3. onBackPressed: the GUI edge uses page S_HOME only. The Back key on other screens of this activity is not modeled here.
4. System picker results (SELECT_FILE, SELECT_DOCUMENT, CREATE_DOCUMENT) have no app node, so onActivityResult has no RESULT edge for them.
5. label_081.py:57 and 61 write ASYNC edges from onEvent(SyncStartingEvent) and onEvent(SyncStoppingEvent), which are UNREACHABLE here. Those edges stay dead unless the two subscribers become reachable. Not changed by this batch.

STATUS: DONE 15:43
