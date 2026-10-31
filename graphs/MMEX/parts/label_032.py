# batch 032 (label_032): com.money.manager.ex.common.MmxBaseFragmentActivity (26 methods, including the anonymous listeners $1 and $2 and the two lambdas), MmxCursorLoader (3) and MoneyParcelConverter (3). Rows and printed lines: graphs/MMEX/parts/label_032.md. grep evidence: graphs/MMEX/parts/label_032.grep.txt.
# Scratch (not evidence): graphs/MMEX/scratch/batch032_auto_hits.txt lists the auto_calls.json records for this batch.
# CALL edges come from auto_calls.json (the super calls of the subclasses, the calls inside this class, the anonymous listeners, the Money$$Parcelable calls), so none are written here.
# Written here: the edges that auto data cannot give (EventBus, the activity lifecycle, the loader thread), and the currency edit page S_CURRENCY_EDIT with its GUI edges to the two listeners (no screen key existed for that form, grep of graph_def.py and parts found none).

# ---- EventBus subscriber in the base activity (greenrobot EventBus: library source not read, INFERRED)

e('MmxBaseFragmentActivity.onStart', 'MmxBaseFragmentActivity.onEvent', 'REGISTER',
  'the activity registers itself on EventBus in onStart; EventBus calls the @Subscribe method onEvent for ErrorRaisedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141, @Subscribe onEvent(ErrorRaisedEvent) at 167-168 (library source not read, INFERRED)',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141, unregister at 146), 167-171 (@Subscribe at 167); SRC log/DebugTree.java:45-46; SRC log/ScreenTree.java:26-27; INFERRED EventBus library source not read')

# REGISTER edges are skipped by reachability, so the two ASYNC edges below carry the route from the Timber trees to onEvent.
e('DebugTree.log', 'MmxBaseFragmentActivity.onEvent', 'ASYNC',
  'a debug build logs an error through Timber while the activity is registered: DebugTree posts ErrorRaisedEvent and EventBus calls onEvent',
  env=env_text('an error is logged through Timber while the activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/DebugTree.java:45-46 (posts only when a subscriber exists); SRC MmexApplication.java:134-135 (DebugTree is planted in the debug branch); SRC common/MmxBaseFragmentActivity.java:167-168; INFERRED EventBus library source not read')

e('ScreenTree.log', 'MmxBaseFragmentActivity.onEvent', 'ASYNC',
  'a release build logs an error through Timber while the activity is registered: ScreenTree posts ErrorRaisedEvent and EventBus calls onEvent (the debug build plants DebugTree instead)',
  env=env_text('an error is logged through Timber while the activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/ScreenTree.java:26-27; SRC MmexApplication.java:134-140 (ScreenTree is planted in the else branch, release only); SRC common/MmxBaseFragmentActivity.java:167-168; INFERRED EventBus library source not read')

# ---- activity lifecycle (framework, source read in fw_src)

e('MmxBaseFragmentActivity.onStart', 'MmxBaseFragmentActivity.onStop', 'LIFECYCLE',
  'the framework stops the activity after onStart when it leaves the foreground (the Home key, or another activity opens on top); no subclass overrides onStop, so this inherited body runs',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-149; grep label_032.grep.txt section G (no subclass of MmxBaseFragmentActivity declares onStop); FW-SRC core/java/android/app/Activity.java:7159 (performStop), 7181 (callActivityOnStop); FW-SRC core/java/android/app/Instrumentation.java:1374-1375')

# ---- loader thread (androidx CursorLoader: library not read, INFERRED)

e('MmxCursorLoader.<init>(Context,Uri,Select)', 'MmxCursorLoader.loadInBackground', 'ASYNC',
  'the LoaderManager starts the loader that the three-argument constructor creates, and the loader calls loadInBackground to query the data off the UI thread',
  cls='non_standard', via='androidx CursorLoader (AsyncTaskLoader): startLoading runs loadInBackground on a worker thread (library not read, INFERRED)',
  evidence='SRC common/MmxCursorLoader.java:32-33, 39-43, 46-53; SRC home/HomeFragment.java:266 (creates the loader in onCreateLoader); INFERRED androidx CursorLoader source not read')

# ---- currency edit form: the cancel and done buttons (page S_CURRENCY_EDIT; its ENTERS edge is written by the batch that owns CurrencyEditActivity.onCreate)

SCREENS.update({
    'S_CURRENCY_EDIT': 'Currency edit form (CurrencyEditActivity): its fields, and the cancel and done buttons from action_buttons.xml (currency_edit_activity.xml:208; that layout has no toolbar)',
})

e('S_CURRENCY_EDIT', 'MmxBaseFragmentActivity$1.onClick', 'GUI',
  'the user taps the cancel button on the currency edit form: the listener calls onActionCancelClick, which CurrencyEditActivity overrides and which finishes the activity',
  evidence='SRC currency/CurrencyEditActivity.java:63-66, 83; SRC common/MmxBaseFragmentActivity.java:102, 176-179, 185-191, 209-219; SRC res/layout/currency_edit_activity.xml:208; SRC res/layout/action_buttons.xml:22, 28; SRC res/layout/actionbar_button_cancel_done.xml:30')

e('S_CURRENCY_EDIT', 'MmxBaseFragmentActivity$2.onClick', 'GUI',
  'the user taps the done button on the currency edit form: the listener calls onActionDoneClick, which CurrencyEditActivity overrides; it saves and finishes when save() succeeds',
  evidence='SRC currency/CurrencyEditActivity.java:69-76; SRC common/MmxBaseFragmentActivity.java:176-179, 185-191, 222-226; SRC res/layout/actionbar_button_cancel_done.xml:46')

# ---- auto edges that cannot run: cut the exact edge only; the cha edges to the overrides stay (label_025.py convention)
# $1 and $2 are created only where the view has action_cancel or action_done (showStandardToolbarActions(View,int,int), lines 211-227). The toolbar of BudgetsActivity (toolbar.xml) has neither, so at runtime only CurrencyEditActivity creates them, and it overrides both callbacks (CurrencyEditActivity.java:63 and 69).

sup(('MmxBaseFragmentActivity$1.onClick', 'MmxBaseFragmentActivity.onActionCancelClick'))  # line 217
sup(('MmxBaseFragmentActivity$2.onClick', 'MmxBaseFragmentActivity.onActionDoneClick'))  # line 225

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_032.grep.txt)

UNREACHABLE['MmxBaseFragmentActivity.onPermissionGranted'] = (
  'no_trigger_in_app',
  'public method that launches openDocumentLauncher (line 271). Nothing in src/main calls it: grep finds only the declaration (Java, res and manifest), and it is not an XML onClick target. With no caller the launcher is never started, so its callback lambda$onCreate$0 never runs',
  'SRC common/MmxBaseFragmentActivity.java:265-272; grep label_032.grep.txt section A',
  'SOURCE')

UNREACHABLE['MmxBaseFragmentActivity.openDirectoryPicker'] = (
  'no_trigger_in_app',
  'public method that launches directoryPickerLauncher (line 277). Nothing in src/main calls it: grep finds only the declaration (Java, res and manifest). With no caller the launcher is never started, so its callback lambda$onCreate$1 never runs',
  'SRC common/MmxBaseFragmentActivity.java:274-278; grep label_032.grep.txt section B',
  'SOURCE')

UNREACHABLE['MmxBaseFragmentActivity.lambda$onCreate$0'] = (
  'no_trigger_in_app',
  'result callback of openDocumentLauncher (registered at line 78). The callback runs only after openDocumentLauncher.launch(), which is called only from onPermissionGranted (line 271), and that method has no caller (grep section A). The REGISTER edge from onCreate (auto lambdas record, line 78) does not make it reachable. The androidx ActivityResult dispatch is INFERRED (library not read)',
  'SRC common/MmxBaseFragmentActivity.java:78-85, 271; grep label_032.grep.txt sections A, C, I',
  'INFERRED')

UNREACHABLE['MmxBaseFragmentActivity.lambda$onCreate$1'] = (
  'no_trigger_in_app',
  'result callback of directoryPickerLauncher (registered at line 87). The callback runs only after directoryPickerLauncher.launch() at line 277, which is called only from openDirectoryPicker, and that method has no caller (grep section B). The REGISTER edge from onCreate (auto lambdas record, line 87) does not make it reachable. The androidx ActivityResult dispatch is INFERRED (library not read)',
  'SRC common/MmxBaseFragmentActivity.java:87-95, 277; grep label_032.grep.txt sections B, C, I',
  'INFERRED')

UNREACHABLE['MmxBaseFragmentActivity.onActionCancelClick'] = (
  'no_trigger_in_app',
  'base body returns true (lines 234-236). Its only call in the base class is the exact call at line 217 in the cancel listener $1.onClick. $1 is created only where the view has action_cancel: CurrencyEditActivity through action_buttons.xml (grep F). The BudgetsActivity toolbar (toolbar.xml) has no such view. CurrencyEditActivity overrides onActionCancelClick (line 63), so the override runs on that receiver. No super.onActionCancelClick call exists (grep section D). The exact edge $1.onClick to this body is cut by sup; the cha edges to the overrides stay',
  'SRC common/MmxBaseFragmentActivity.java:209-236; SRC currency/CurrencyEditActivity.java:63; SRC budget/BudgetsActivity.java:48; grep label_032.grep.txt sections D, F',
  'SOURCE')

UNREACHABLE['MmxCursorLoader.<init>(Context)'] = (
  'no_trigger_in_app',
  'one-argument constructor (lines 35-37). Every new MmxCursorLoader in src/main passes three arguments (context, uri and query), and no class extends MmxCursorLoader (grep section E). With no caller the constructor never runs',
  'SRC common/MmxCursorLoader.java:35-37; grep label_032.grep.txt section E',
  'SOURCE')
