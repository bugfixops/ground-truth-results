# ================================================================== batch 080 (label_080)
# Rows, printed lines and counts: graphs/MMEX/parts/label_080.md (36 REACHABLE, 4 UNREACHABLE, 0 INCOMPLETE).
# This file writes:
#   - 24 edges: 1 ENTRY, 5 LIFECYCLE, 1 FRAMEWORK, 2 RESULT, 1 ENTERS, 6 ASYNC, 6 REGISTER (e()), 2 GUI (gui());
#   - 5 sup pairs (D14a: auto CALL records whose caller is UNREACHABLE in this batch, and the framework setRestartActivity pair);
#   - 4 UNREACHABLE entries: 3 SOURCE (the EventBus subscribers with no live poster), onConfigurationChanged INFERRED.
# No CALL edges (D7: every app-internal route of this class is an auto CALL record in auto_calls.json).
# No edge goes into an UNREACHABLE method (D17).
# No label_080.grep.txt: no UNREACHABLE method is library or generated.
# env_text and state_text: not needed here. The passcode gate is on the INTENT edge in label_003.py, and the sync gate is in the auto records.

# ---- entry and lifecycle
e('S_ENTRY', 'MainActivity.<clinit>', 'ENTRY',
  'The launcher or a VIEW intent starts MainActivity: the framework creates the activity class by name, which initializes the class (mRestartActivity has a non-constant initializer, so the class has a static initializer)',
  evidence='SRC home/MainActivity.java:155; SRC AndroidManifest.xml:135-174; JVM class initialization is not in fw_src: INFERRED, source not read')

e('MainActivity.<init>', 'MainActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1216; FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate); same route as graph_def.py AccountEditActivity.<init> -> onCreate')

e('MainActivity.onCreate', 'MainActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:615-640 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu at 3388); same route as label_019.py:23 (BudgetsActivity)')

e('MainActivity.onCreate', 'MainActivity.onDestroy', 'LIFECYCLE',
  'onCreate calls finish() when the prerequisite check fails (tutorial needed, or no database available), and the framework then destroys the activity',
  guard='showPrerequisite() returns true (MainActivity.java:184-187)',
  evidence='SRC home/MainActivity.java:184-187, 1478-1500; INFERRED finish leads to onDestroy (ActivityThread.handleDestroyActivity at ActivityThread.java:4399, body not read)')

e('MainActivity.onActivityResult', 'MainActivity.onDestroy', 'LIFECYCLE',
  'the passcode is not accepted: onActivityResult calls finish(), and the framework destroys the activity',
  guard='the PASSCODE branch ends with isAuthenticated still false (MainActivity.java:356-358)',
  evidence='SRC home/MainActivity.java:335-359, 356-358; INFERRED finish leads to onDestroy (ActivityThread.handleDestroyActivity at ActivityThread.java:4399, body not read)')

e('MainActivity.onBackPressed', 'MainActivity.onDestroy', 'LIFECYCLE',
  'Back with the drawer closed: super.onBackPressed (inside a try block) finishes the activity when there is no back stack entry to pop, and the framework destroys it',
  guard='the fragment manager has nothing to pop, or its state is saved (Activity.java:3006-3009)',
  evidence='SRC home/MainActivity.java:439-450 (super call at 445); FW-SRC core/java/android/app/Activity.java:3001-3010 (finishAfterTransition at 3009); INFERRED finishAfterTransition leads to onDestroy (finish path not read)')

e('MainActivity.restartActivity', 'MainActivity.onDestroy', 'LIFECYCLE',
  'restartActivity starts a new MainActivity and then calls finish() on this one, and the framework destroys it',
  guard='mRestartActivity is set (MainActivity.java:703)',
  evidence='SRC home/MainActivity.java:702-716 (finish at 715); INFERRED finish leads to onDestroy (finish path not read)')

# ---- results returned to onActivityResult (the framework calls it through dispatchActivityResult)
e('PasswordActivity.returnPassword', 'MainActivity.onActivityResult', 'RESULT',
  'the password screen returns the password and finishes: setResult(RESULT_OK), and the framework calls onActivityResult (REQUEST_PASSWORD)',
  guard='requestCode is RequestCodes.REQUEST_PASSWORD (MainActivity.java:318) and resultCode is RESULT_OK (MainActivity.java:303)',
  evidence='SRC database/PasswordActivity.java:56, 62-73 (setResult at 71, finish at 72); SRC home/MainActivity.java:318-322, 601; FW-SRC core/java/android/app/ActivityThread.java:4253-4264 (deliverResults calls dispatchActivityResult at 4264); FW-SRC core/java/android/app/Activity.java:7259-7266 (onActivityResult at 7266)')

e('PasscodeActivity$1.onClick', 'MainActivity.onActivityResult', 'RESULT',
  'the passcode screen returns the five digits after the last digit is entered: setResult(RESULT_OK, result) and finish(), and the framework calls onActivityResult (PASSCODE)',
  guard='the focused field is editTextPasscode5 (PasscodeActivity.java:116)',
  evidence='SRC PasscodeActivity.java:99-131 (click listener, setResult at 125, finish at 126); SRC home/MainActivity.java:260 (startActivityForResult with RequestCodes.PASSCODE), 335-359; FW-SRC core/java/android/app/ActivityThread.java:4253-4264; FW-SRC core/java/android/app/Activity.java:7259-7266')

# ---- the home screen
e('MainActivity.initHomeFragment', 'S_HOME', 'ENTERS',
  'the home screen is shown: initHomeFragment commits HomeFragment into the content container, or the navigation container in dual-panel mode',
  guard='no HomeFragment is in the manager yet (MainActivity.java:1312-1313)',
  evidence='SRC home/MainActivity.java:1308-1324; SRC home/HomeFragment.java:167-173 (onCreateView inflates home_fragment); the ENTERS edge is assigned to batch 080 by label_077.py:6')

# ---- EventBus posts into the activity subscribers (ASYNC)
e('HomeFragment.onLoadFinished', 'MainActivity.onEvent(AccountsTotalLoadedEvent)', 'ASYNC',
  'the accounts loader finishes: HomeFragment posts AccountsTotalLoadedEvent on the EventBus, and the subscriber on the activity runs',
  cls='non_standard', via='EventBus (greenrobot) post at HomeFragment.java:297; subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC home/HomeFragment.java:287-297 (post at 297); SRC home/MainActivity.java:480-483; INFERRED EventBus delivery (library not read)')

e('HomeFragment$4.onSuccess', 'MainActivity.onEvent(UsernameLoadedEvent)', 'ASYNC',
  'the username is read on the IO thread and delivered on the main thread: HomeFragment sets it in the application and posts UsernameLoadedEvent',
  cls='non_standard', via='EventBus (greenrobot) post at HomeFragment.java:653; subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC home/HomeFragment.java:638-653 (loadUsername; SingleSubscriber at 649, onSuccess at 651-653, post at 653); method_list.json names HomeFragment$4.onSuccess and HomeFragment$4.onError (javac numbering: $5.call is the Callable); SRC home/MainActivity.java:475-478; INFERRED EventBus delivery (library not read)')

e('HomeFragment.onContextItemSelected', 'MainActivity.onEvent(RequestPortfolioFragmentEvent)', 'ASYNC',
  'the account context menu: the portfolio item posts RequestPortfolioFragmentEvent on the EventBus',
  guard='the menu title equals the portfolio string (HomeFragment.java:473)',
  cls='non_standard', via='EventBus (greenrobot) post at HomeFragment.java:474; subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC home/HomeFragment.java:450-474 (post at 474); SRC home/MainActivity.java:464-467; INFERRED EventBus delivery (library not read)')

e('HomeFragment$6.onChildClick', 'MainActivity.onEvent(RequestWatchlistFragmentEvent)', 'ASYNC',
  'tap a row of an investment account: HomeFragment posts RequestWatchlistFragmentEvent on the EventBus',
  guard='the account type is INVESTMENT (HomeFragment.java:699-700)',
  cls='non_standard', via='EventBus (greenrobot) post at HomeFragment.java:704; subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC home/HomeFragment.java:686-706 (onChildClick; event chosen at 699-703; post at 704); SRC home/MainActivity.java:459-462; INFERRED EventBus delivery (library not read)')

e('HomeFragment$6.onChildClick', 'MainActivity.onEvent(RequestAccountFragmentEvent)', 'ASYNC',
  'tap a row of any other account: HomeFragment posts RequestAccountFragmentEvent on the EventBus',
  guard='the account type is not INVESTMENT (HomeFragment.java:699, 701-702)',
  cls='non_standard', via='EventBus (greenrobot) post at HomeFragment.java:704; subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC home/HomeFragment.java:686-706 (onChildClick; event chosen at 701-703; post at 704); SRC home/MainActivity.java:454-457; INFERRED EventBus delivery (library not read)')

e('SyncServiceMessageHandler.handleMessage', 'MainActivity.onEvent(DbFileDownloadedEvent)', 'ASYNC',
  'the sync service reports DOWNLOAD_COMPLETE: the handler posts DbFileDownloadedEvent, and MainActivity uses the downloaded database file',
  cls='non_standard', via='EventBus (greenrobot) post at SyncServiceMessageHandler.java:89; subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC sync/SyncServiceMessageHandler.java:84-90 (post at 89); SRC sync/SyncService.java:125-129 (download route); SRC home/MainActivity.java:526-530 (529 useDownloadedDatabase); INFERRED EventBus delivery (library not read)')

# ---- EventBus registration: MmxBaseFragmentActivity.onStart registers the activity (inherited by MainActivity)
e('MmxBaseFragmentActivity.onStart', 'MainActivity.onEvent(RequestAccountFragmentEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited by MainActivity); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at MainActivity.java:454',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC home/MainActivity.java:454-457; INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'MainActivity.onEvent(RequestWatchlistFragmentEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited by MainActivity); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at MainActivity.java:459',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC home/MainActivity.java:459-462; INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'MainActivity.onEvent(RequestPortfolioFragmentEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited by MainActivity); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at MainActivity.java:464',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC home/MainActivity.java:464-467; INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'MainActivity.onEvent(UsernameLoadedEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited by MainActivity); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at MainActivity.java:475',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC home/MainActivity.java:475-478; INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'MainActivity.onEvent(AccountsTotalLoadedEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited by MainActivity); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at MainActivity.java:480',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC home/MainActivity.java:480-483; INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'MainActivity.onEvent(DbFileDownloadedEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited by MainActivity); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at MainActivity.java:526',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC home/MainActivity.java:526-530; INFERRED EventBus library not read')

# ---- GUI edges from the home screen S_HOME (page -> method)
gui('S_HOME', 'MainActivity.onBackPressed', 'Press the Back key on the home screen with the drawer closed',
  evidence='SRC home/MainActivity.java:439-450; FW-SRC core/java/android/app/Activity.java:3001-3010 (the framework calls the override on Back)')

gui('S_HOME', 'MainActivity.onClickCardViewIncomesVsExpenses', 'Tap the Income vs Expenses card on the home screen',
  evidence='SRC res/layout/home_fragment.xml:119-129 (CardView with android:onClick at 127, app/src/main), inflated at SRC home/HomeFragment.java:173; SRC home/MainActivity.java:832-834; INFERRED android:onClick resolves on the host activity (View.java DeclaredOnClickListener not read)')

# ---- suppressed auto CALL routes whose caller is UNREACHABLE in this batch (D14a)
sup(
    ('MainActivity.onEvent(RequestOpenDatabaseEvent)', 'FileStorageHelper.showStorageFilePicker'),
    ('MainActivity.onEvent(RequestOpenDatabaseEvent)', 'FileStorageHelper.<init>'),
    ('MainActivity.onEvent(SyncStartingEvent)', 'MainActivity$1.<init>'),
    ('MainActivity.onEvent(SyncStoppingEvent)', 'MainActivity$2.<init>'),
    ('MainActivity.onConfigurationChanged', 'MainActivity.setRestartActivity'),
)

# ---- UNREACHABLE methods
UNREACHABLE['MainActivity.onEvent(RequestOpenDatabaseEvent)'] = (
    'no_trigger_in_app',
    'no code posts RequestOpenDatabaseEvent: in the source root the only mentions are the import (MainActivity.java:86) and this handler (469-473)',
    'SRC home/MainActivity.java:86, 469-473; grep of the source root for RequestOpenDatabaseEvent finds no post',
    'SOURCE')

UNREACHABLE['MainActivity.onEvent(SyncStartingEvent)'] = (
    'no_trigger_in_app',
    'the only poster is SyncService.sendStartEvent (post at SyncService.java:241); its call sites at 95, 108, 116, 186 and 198 are commented out, so no SyncStartingEvent is posted',
    'SRC sync/SyncService.java:95, 108, 116, 186, 198 (commented call sites); SRC sync/SyncService.java:238-243 (sendStartEvent, post at 241)',
    'SOURCE')

UNREACHABLE['MainActivity.onEvent(SyncStoppingEvent)'] = (
    'no_trigger_in_app',
    'the only poster is SyncService.sendStopEvent (post at SyncService.java:247); the same call sites are commented out, so no SyncStoppingEvent is posted',
    'SRC sync/SyncService.java:95, 108, 116, 186, 198 (commented call sites); SRC sync/SyncService.java:245-249 (sendStopEvent, post at 247)',
    'SOURCE')

UNREACHABLE['MainActivity.onConfigurationChanged'] = (
    'framework_never_calls',
    'the manifest declares no configChanges, so a configuration change that touches this activity relaunches it (ActivityRecord.java:2450, shouldRelaunchLocked at 2527); a change with no diff is not delivered (ActivityRecord.java:2416-2426; the Activity branch of handleConfigurationChanged at ActivityThread.java:5033-5038 skips an unchanged config). Residual: the process-level push (ActivityManagerService.java:20451-20457) is sent after the relaunch request; the order in the app message queue was not traced',
    'FW-SRC services/core/java/com/android/server/am/ActivityRecord.java:2416-2426, 2450, 2527; FW-SRC core/java/android/app/ActivityThread.java:5025-5038; FW-SRC services/core/java/com/android/server/am/ActivityManagerService.java:20451-20457; SRC AndroidManifest.xml:135-137 (no configChanges)',
    'INFERRED')
