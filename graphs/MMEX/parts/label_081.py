# ================================================================== batch 081 (label_081): MainActivity, 40 methods (graphs/MMEX/scratch/batches/batch_081.txt)
# Rows, printed lines and counts: graphs/MMEX/parts/label_081.md. No grep file: every row is REACHABLE, so no library or generated class is UNREACHABLE.
# Edges written here: the activity lifecycle into MainActivity (onStart, onResume, onSaveInstanceState, onPostCreate), the Menu key, the Up button and the drawer taps on the home screen S_HOME (gui), the drawer Runnable (FRAMEWORK, postDelayed), and the Icepick reflection helper (cls=non_standard). The two sync Callables are UNREACHABLE (their subscribers have no poster, batch 080).
# CALL edges come from auto_calls.json and are not written here (D7). No SCREENS key is added: S_HOME is already in SCREENS (graph_def.py:6401).
# UNREACHABLE: none. sup(): none (no auto CALL caller of a method in this batch is UNREACHABLE).

# ---- activity lifecycle: MainActivity.onCreate is batch 080; the edges below have their destination in this batch
e('MainActivity.onCreate', 'MainActivity.onStart', 'LIFECYCLE',
  'the framework starts the activity right after onCreate (performLaunchActivity runs performStart)',
  evidence='SRC home/MainActivity.java:179-181, 248-249; FW-SRC core/java/android/app/ActivityThread.java:2740-2760 (performStart at 2741)')

e('MainActivity.onStart', 'MainActivity.onResume', 'LIFECYCLE',
  'after onStart the framework resumes the activity (performResume)',
  evidence='SRC home/MainActivity.java:248-249, 271-273; FW-SRC core/java/android/app/ActivityThread.java:2950; FW-SRC core/java/android/app/Activity.java:7098-7104')

e('MainActivity.onResume', 'MainActivity.onSaveInstanceState', 'LIFECYCLE',
  'the user leaves the home screen (Home button, another activity starts): the framework stops the activity and saves its state',
  evidence='SRC home/MainActivity.java:271-283, 423-429; FW-SRC core/java/android/app/ActivityThread.java:4713-4722 (callCallActivityOnSaveInstanceState); pattern label_027.py:65-73')

e('MainActivity.onCreate', 'MainActivity.onPostCreate', 'FRAMEWORK',
  'the framework calls onPostCreate right after onCreate and the state restore (callActivityOnPostCreate)',
  evidence='SRC home/MainActivity.java:179-181, 285-296; FW-SRC core/java/android/app/ActivityThread.java:2740-2760 (callActivityOnPostCreate at 2757, 2760)')

# ---- Icepick: the library loads the generated helper MainActivity$$Icepick by reflection (not in the dataset).
# Restore from MmxBaseFragmentActivity.onCreate (line 74, unguarded); save from MmxBaseFragmentActivity.onSaveInstanceState (line 155).
e('MmxBaseFragmentActivity.onCreate', 'MainActivity$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State fields: the library loads the generated helper by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at common/MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:72-75; SRC home/MainActivity.java:159-162; the icepick library is not in the dataset: INFERRED, source not read; pattern label_077.py:71-73')

e('MmxBaseFragmentActivity.onCreate', 'MainActivity$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection for the restore',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at common/MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:72-75; SRC home/MainActivity.java:159-162; INFERRED icepick library (not read); pattern label_077.py:77-79')

e('MmxBaseFragmentActivity.onCreate', 'MainActivity$$Icepick.restore', 'FRAMEWORK',
  'Icepick calls the generated restore for the @State fields (dbUpdateCheckDone, mIsSynchronizing, isAuthenticated, deviceOrientation)',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at common/MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:72-75; SRC home/MainActivity.java:159-162; INFERRED icepick library (not read); pattern label_077.py:83-85')

e('MmxBaseFragmentActivity.onSaveInstanceState', 'MainActivity$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick saves the @State fields: the library loads the generated helper by reflection, which runs its static initialiser first if onCreate did not',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at common/MmxBaseFragmentActivity.java:155)',
  evidence='SRC common/MmxBaseFragmentActivity.java:150-156; SRC home/MainActivity.java:159-162; INFERRED icepick library (not read); pattern label_077.py:89-91')

e('MmxBaseFragmentActivity.onSaveInstanceState', 'MainActivity$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection for the save',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at common/MmxBaseFragmentActivity.java:155)',
  evidence='SRC common/MmxBaseFragmentActivity.java:150-156; INFERRED icepick library (not read); pattern label_077.py:94-96')

e('MmxBaseFragmentActivity.onSaveInstanceState', 'MainActivity$$Icepick.save', 'FRAMEWORK',
  'Icepick calls the generated save for the @State fields',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at common/MmxBaseFragmentActivity.java:155)',
  evidence='SRC common/MmxBaseFragmentActivity.java:150-156; SRC home/MainActivity.java:159-162, 423-429; INFERRED icepick library (not read); pattern label_077.py:99-101')

# ---- the sync Callables are dead: their constructors are cut by the batch 080 sup pairs, and no code posts the two events
UNREACHABLE['MainActivity$1.<init>'] = ('no_trigger_in_app',
  'auto CALL from MainActivity.onEvent(SyncStartingEvent), which is UNREACHABLE (batch 080): no code posts SyncStartingEvent, because its only poster SyncService.sendStartEvent is called only from a commented line',
  'SRC home/MainActivity.java:490-502 (create at 491); SRC sync/SyncService.java:95 (commented call), 238-241 (sendStartEvent, post at 241)',
  'SOURCE')

UNREACHABLE['MainActivity$1.call'] = ('no_trigger_in_app',
  'RxJava Callable created only in MainActivity.onEvent(SyncStartingEvent) (UNREACHABLE, batch 080): the subscribe at line 501 is never reached, so call() (which sets mIsSynchronizing at 494) never runs',
  'SRC home/MainActivity.java:490-502 (Callable 491-497, subscribeOn 499, subscribe 501); SRC sync/SyncService.java:95, 238-241',
  'SOURCE')

UNREACHABLE['MainActivity$2.<init>'] = ('no_trigger_in_app',
  'auto CALL from MainActivity.onEvent(SyncStoppingEvent), which is UNREACHABLE (batch 080): no code posts SyncStoppingEvent, because its only poster SyncService.sendStopEvent is called only from commented lines',
  'SRC home/MainActivity.java:509-521 (create at 510); SRC sync/SyncService.java:108, 116, 186, 198 (commented calls), 245-247 (sendStopEvent, post at 247)',
  'SOURCE')

UNREACHABLE['MainActivity$2.call'] = ('no_trigger_in_app',
  'RxJava Callable created only in MainActivity.onEvent(SyncStoppingEvent) (UNREACHABLE, batch 080): the subscribe at line 520 is never reached, so call() (which clears mIsSynchronizing at 513-514) never runs',
  'SRC home/MainActivity.java:509-521 (Callable 510-516, subscribeOn 518, subscribe 520); SRC sync/SyncService.java:108, 116, 186, 198, 245-247',
  'SOURCE')

# ---- FRAMEWORK: the drawer item runs 200 ms after the tap (Handler.postDelayed, same pattern as batches 041 and 082)
e('MainActivity$3.onGroupClick', 'MainActivity$3$1.run', 'FRAMEWORK',
  'the tap posts the drawer item Runnable with a 200 ms delay; the framework runs run() when the delay ends, and run() calls onDrawerMenuAndOptionMenuSelected (auto CALL at line 957)',
  evidence='SRC home/MainActivity.java:948-962 (postDelayed 953, run 955, call 957); FW-SRC core/java/android/os/Handler.java:427-429 (postDelayed calls sendMessageDelayed), 596, 97-99 (dispatchMessage calls handleCallback), 789-790 (handleCallback runs message.callback.run())')

# ---- GUI edges from the home screen S_HOME (MainActivity shows HomeFragment; its ENTERS edge is written by batch 080)
gui('S_HOME', 'MainActivity.onKeyDown',
    'Press the hardware Menu key while the home screen is shown: the drawer opens, or closes when it is already open',
    evidence='SRC home/MainActivity.java:407-421; FW-SRC core/java/android/app/Activity.java:3255-3274; FW-SRC core/java/android/view/KeyEvent.java:2684-2692 (onKeyDown called at about 2690); pattern label_001.py:19-26')

gui('S_HOME', 'MainActivity.onOptionsItemSelected',
    'Tap the Up (drawer) button at the left of the toolbar: the framework passes android.R.id.home to onOptionsItemSelected, which toggles the drawer',
    evidence='SRC home/MainActivity.java:387-405 (home branch and toggle), 1289-1307 (setDisplayHomeAsUpEnabled(true)); FW-SRC core/java/android/app/Activity.java:3439-3452; INFERRED AppCompat toolbar click sends android.R.id.home to the callback (androidx not in fw_src); pattern label_019.py:31-36')

gui('S_HOME', 'MainActivity$3.onGroupClick',
    'Open the drawer (Up button or Menu key), then tap a top-level drawer item that has no sub-items (for example Payees or Recurring transactions)',
    evidence='SRC home/MainActivity.java:928-962 (childItems.add(null) for groups without children at 928; onGroupClick at 938 returns false when children is not null); INFERRED ExpandableListView group click dispatch (library not read)')
