# ================================================================== part 146 (label_146): dispatch edges for four frontier methods
# Written by the orchestrator, not by a helper (2026-10-31). No methods are owned here: no UNREACHABLE entries, no sups.
# REGISTER edges are skipped by reachability (tools/build_graph.py bfs and cheapest), so each subscriber or callback that
# was reached only through a REGISTER edge needs a dispatch edge from the method that runs the call.

# ---- PasscodeActivity.onEvent(ErrorRaisedEvent): the Timber trees post the event (DebugTree.java:46, ScreenTree.java:27)

e('DebugTree.log', 'PasscodeActivity.onEvent', 'ASYNC',
  'a debug build logs an error through Timber while the passcode activity is registered: DebugTree posts ErrorRaisedEvent and EventBus calls onEvent',
  env=env_text('an error is logged through Timber while the passcode activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/DebugTree.java:45-46 (posts only when a subscriber exists); SRC MmexApplication.java:134-135 (DebugTree in the debug branch); SRC PasscodeActivity.java:202-215 (onStart registers; @Subscribe onEvent(ErrorRaisedEvent) at 214-215); INFERRED EventBus library source not read')

e('ScreenTree.log', 'PasscodeActivity.onEvent', 'ASYNC',
  'a release build logs an error through Timber while the passcode activity is registered: ScreenTree posts ErrorRaisedEvent and EventBus calls onEvent (the debug build plants DebugTree instead)',
  env=env_text('an error is logged through Timber while the passcode activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/ScreenTree.java:26-27; SRC MmexApplication.java:134-140 (ScreenTree in the release branch); SRC PasscodeActivity.java:202-215; INFERRED EventBus library source not read')

# ---- BudgetsActivity.onEvent(BudgetSelectedEvent): a budget row tap posts the event (BudgetListFragment.java:215)

e('BudgetListFragment.onListItemClick', 'BudgetsActivity.onEvent', 'ASYNC',
  'tapping a budget row posts BudgetSelectedEvent, and EventBus calls the @Subscribe method onEvent while the activity is registered',
  cls='non_standard', via='EventBus (greenrobot): post(BudgetSelectedEvent) at BudgetListFragment.java:215 to the @Subscribe method BudgetsActivity.onEvent (library dispatch, INFERRED)',
  evidence='SRC budget/BudgetListFragment.java:208-215 (onListItemClick posts at 215); SRC budget/BudgetsActivity.java:82-83 (@Subscribe onEvent(BudgetSelectedEvent)); INFERRED EventBus library source not read')

# ---- MmexApplication.lambda$onCreate$0: the Amplitude configuration block, called while the client is built

e('MmexApplication.onCreate', 'MmexApplication.lambda$onCreate$0', 'CALL',
  'onCreate calls the Amplitude factory with the configuration block, and the library calls the block while it builds the client',
  cls='non_standard', via='AmplitudeKt.Amplitude (com.amplitude.android) calls the Kotlin configuration block (library source not in the dataset, INFERRED)',
  evidence='SRC MmexApplication.java:147-154 (AmplitudeKt.Amplitude with the lambda); library com.amplitude.android is not in the dataset: its call of the block is INFERRED, source not read')

# ---- BehaviourSettingsFragment.lambda$showTimePicker$0: the TimePickerDialog OnTimeSetListener, called when the user sets the time

e('BehaviourSettingsFragment.showTimePicker', 'BehaviourSettingsFragment.lambda$showTimePicker$0', 'FRAMEWORK',
  'the framework TimePickerDialog calls the listener lambda when the user sets the time in the dialog that showTimePicker shows (line 114)',
  cls='non_standard', via='android.app.TimePickerDialog calls its OnTimeSetListener (framework source not in fw_src, INFERRED)',
  evidence='SRC settings/BehaviourSettingsFragment.java:101-106 (lambda and TimePickerDialog construction), 114 (show); the TimePickerDialog source is not in fw_src: INFERRED')
