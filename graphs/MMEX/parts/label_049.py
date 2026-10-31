# batch 049 (label_049): com.money.manager.ex.currency.list.CurrencyListActivity (4 methods), CurrencyListAdapter (3),
# CurrencyListFragment (26, including its implicit <init>), CurrencyListFragment$1 (4) and
# com.money.manager.ex.currency.recycler.CurrencyContentObserver (3). 40 methods in all.
# Rows and printed lines: graphs/MMEX/parts/label_049.md.
# CALL edges between the batch methods and to other classes come from auto_calls.json, including the receiver-variant
# records BaseListFragment.onActivityCreated@CurrencyListFragment, BaseListFragment.onPreQueryTextChange@CurrencyListFragment
# and BaseListFragment.setResultAndFinish@CurrencyListFragment, so none are written here except the sup cut below.
# androidx Fragment, LoaderManager, CursorAdapter, SearchView and the options-menu dispatch are not in fw_src: those claims are INFERRED.
# The class initialiser and the INTENT edges into it follow the batch 028 pattern.

SCREENS.update({
    'S_CURRENCY_LIST': 'Currency list (CurrencyListActivity with CurrencyListFragment): the list of currencies, opened from the main menu, from the account editor, or by another app (ACTION_PICK or ACTION_EDIT)',
})

# ---- entry from another app (exported=true, PICK and EDIT filters) and the in-app intents

e('S_ENTRY', 'CurrencyListActivity.<init>', 'ENTRY',
  'another app sends an ACTION_PICK or ACTION_EDIT intent to the exported CurrencyListActivity',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to CurrencyListActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:205-215 (exported=true; PICK and EDIT filters at 210-214); FW-SRC core/java/android/app/ActivityThread.java:2665-2672 (mInstrumentation.newActivity); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance())')

e('S_ENTRY', 'CurrencyListActivity.<clinit>', 'ENTRY',
  'the first CurrencyListActivity instance (the exported-intent start above) initialises the class',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to CurrencyListActivity (exported=true)', ('other_app',)),
  evidence='SRC currency/list/CurrencyListActivity.java:39 (FRAGMENTTAG = CurrencyListActivity.class.getSimpleName() + "_Fragment" is a method call, so the class has a static initialiser); SRC AndroidManifest.xml:205-215; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'CurrencyListActivity.<init>', 'INTENT',
  'the Currencies item of the main menu starts CurrencyListActivity with ACTION_EDIT',
  gui=['Tap Currencies in the main menu (drawer or options menu)'],
  evidence='SRC home/MainActivity.java:641-646 (case R.id.menu_currency at 641; new Intent 643; ACTION_EDIT 645; startActivity 646); FW-SRC core/java/android/app/Instrumentation.java:1170-1174')

e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'CurrencyListActivity.<clinit>', 'INTENT',
  'the first CurrencyListActivity instance (the start above) initialises the class',
  gui=['Tap Currencies in the main menu (drawer or options menu)'],
  evidence='SRC home/MainActivity.java:641-646; SRC currency/list/CurrencyListActivity.java:39; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

e('AccountEditActivity$4.onClick', 'CurrencyListActivity.<init>', 'INTENT',
  'tap the currency field in the account editor: startActivityForResult(ACTION_PICK) starts CurrencyListActivity',
  gui=['Tap the currency field in the account editor'],
  evidence='SRC account/AccountEditActivity.java:390-395 (setOnClickListener 390; new Intent 393; ACTION_PICK 394; startActivityForResult 395); FW-SRC core/java/android/app/Instrumentation.java:1170-1174')

e('AccountEditActivity$4.onClick', 'CurrencyListActivity.<clinit>', 'INTENT',
  'the first CurrencyListActivity instance (the start above) initialises the class',
  gui=['Tap the currency field in the account editor'],
  evidence='SRC account/AccountEditActivity.java:390-395; SRC currency/list/CurrencyListActivity.java:39; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

# ---- lifecycle: activity and fragment (framework; androidx Fragment is INFERRED)

e('CurrencyListActivity.<init>', 'CurrencyListActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999)')

e('CurrencyListFragment.<init>', 'CurrencyListFragment.onCreate', 'LIFECYCLE',
  'the fragment manager calls onCreate after the constructor, for the fragment that CurrencyListActivity.onCreate adds (commit at 63-66)',
  evidence='SRC currency/list/CurrencyListActivity.java:50, 63-66; SRC currency/list/CurrencyListFragment.java:86-101 (onCreate); INFERRED androidx FragmentManager calls onCreate after the constructor (library not read)')

e('CurrencyListFragment.onCreate', 'CurrencyListFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC currency/list/CurrencyListFragment.java:86-108 (onCreate 86-101; onCreateView 103-108); INFERRED androidx Fragment lifecycle (library not read)')

e('AbsListFragment.onCreateView', 'CurrencyListFragment.onViewCreated', 'LIFECYCLE',
  'the framework calls onViewCreated after the view is created by the inherited onCreateView (AbsListFragment inflates abs_list_fragment.xml). CurrencyListFragment overrides onViewCreated without calling super (154-156), so the BaseListFragment body that label_026 writes does not run for this receiver',
  evidence='SRC core/AbsListFragment.java:74-80 (onCreateView); SRC currency/list/CurrencyListFragment.java:153-156 (onViewCreated, no super); SRC common/BaseListFragment.java:62-67; INFERRED androidx Fragment lifecycle (library not read)')

e('CurrencyListFragment.onViewCreated', 'CurrencyListFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onViewCreated',
  evidence='SRC currency/list/CurrencyListFragment.java:153-156 (onViewCreated), 124-151 (onActivityCreated); INFERRED androidx Fragment lifecycle (library not read)')

e('CurrencyListActivity.onCreate', 'CurrencyListFragment.onActivityCreated', 'LIFECYCLE',
  'the fragment that CurrencyListActivity.onCreate adds (commit at 63-66) gets its onActivityCreated call after the activity has created it, the same pattern as batch 029',
  evidence='SRC currency/list/CurrencyListActivity.java:50, 63-66; SRC currency/list/CurrencyListFragment.java:124-151; INFERRED androidx FragmentManager (library not read)')

e('CurrencyListFragment.onActivityCreated', 'CurrencyListFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after onActivityCreated; onStart registers the fragment on EventBus (line 114)',
  evidence='SRC currency/list/CurrencyListFragment.java:110-115 (onStart), 124-151; INFERRED androidx Fragment lifecycle (library not read)')

e('CurrencyListFragment.onStart', 'CurrencyListFragment.onStop', 'LIFECYCLE',
  'the framework stops the fragment after onStart when the activity leaves the foreground; onStop unregisters EventBus (line 121)',
  evidence='SRC currency/list/CurrencyListFragment.java:117-122 (onStop); INFERRED androidx Fragment lifecycle (library not read)')

# ---- the screen (ENTERS): the activity and the fragment both show the currency list

e('CurrencyListActivity.onCreate', 'S_CURRENCY_LIST', 'ENTERS',
  'the activity creates the currency list fragment and commits it to the content view (add and commit at 63-66)',
  evidence='SRC currency/list/CurrencyListActivity.java:41-67 (fragment at 50; add and commit at 63-66)')

e('CurrencyListFragment.onActivityCreated', 'S_CURRENCY_LIST', 'ENTERS',
  'the fragment is attached and its list is set up (adapter 139, loader 145) once the activity has created it',
  evidence='SRC currency/list/CurrencyListFragment.java:124-151 (adapter 139; loadData 145)')

# ---- framework dispatch (FRAMEWORK): options menu, context menu, loader and adapter callbacks

e('CurrencyListFragment.onActivityCreated', 'CurrencyListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'onActivityCreated calls setHasOptionsMenu(true) (line 136), so the framework builds the options menu through onCreateOptionsMenu, which calls super (162) and adds its items',
  evidence='SRC currency/list/CurrencyListFragment.java:136, 160-173 (super 161-162); SRC common/BaseListFragment.java:113-149 (the inherited body reached by the super call); INFERRED androidx FragmentManager dispatches onCreateOptionsMenu to fragments with an options menu (library not read)')

e('CurrencyListFragment.onListItemClick', 'CurrencyListFragment.onCreateContextMenu', 'FRAMEWORK',
  'the row tap calls openContextMenu (line 336); the framework then calls onCreateContextMenu for the list (registered for the context menu at line 155)',
  evidence='SRC currency/list/CurrencyListFragment.java:155 (registerForContextMenu), 215-229 (onCreateContextMenu), 329-341 (openContextMenu 336); INFERRED View.openContextMenu dispatch (android.view.View not read in this batch)')

e('CurrencyListFragment.loadData', 'CurrencyListFragment$1.onCreateLoader', 'FRAMEWORK',
  'initLoader (line 499) starts the currency loader and the LoaderManager calls onCreateLoader',
  evidence='SRC currency/list/CurrencyListFragment.java:498-500 (initLoader at 499, this.loaderCallbacks); INFERRED androidx LoaderManager.initLoader calls LoaderCallbacks.onCreateLoader (library not read)')

e('CurrencyListFragment.reloadData', 'CurrencyListFragment$1.onCreateLoader', 'FRAMEWORK',
  'restartLoader (reloadData, 502-504) calls onCreateLoader again for the restarted loader',
  evidence='SRC currency/list/CurrencyListFragment.java:502-504 (restartLoader); INFERRED androidx LoaderManager.restartLoader calls onCreateLoader (library not read); same pattern as label_008 (AccountListFragment)')

e('CurrencyListFragment$1.onCreateLoader', 'CurrencyListFragment$1.onLoadFinished', 'FRAMEWORK',
  'the loader (MmxCursorLoader, line 459) delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC currency/list/CurrencyListFragment.java:459 (new MmxCursorLoader); INFERRED androidx LoaderManager delivers the result to onLoadFinished (library not read); same pattern as label_016 and label_008')

e('CurrencyListFragment$1.onLoadFinished', 'CurrencyListFragment$1.onLoaderReset', 'FRAMEWORK',
  'a loader that has delivered data is reset (fragment destroyed or loader restarted) and the LoaderManager calls onLoaderReset',
  evidence='SRC currency/list/CurrencyListFragment.java:465-472 (onLoaderReset), 474-489 (onLoadFinished); INFERRED androidx LoaderManager calls onLoaderReset (library not read); same pattern as label_008')

e('CurrencyListFragment$1.onLoadFinished', 'CurrencyListAdapter.newView', 'FRAMEWORK',
  'adapter.changeCursor(data) (line 479) swaps in the new cursor and notifies the list; on the relayout the framework calls getView, which calls newView for a row with no scrap view',
  evidence='SRC currency/list/CurrencyListFragment.java:477, 479; SRC currency/list/CurrencyListAdapter.java:29, 35 (extends androidx CursorAdapter); same chain as label_014.py:11-12 (the FW-SRC CursorAdapter and ListView lines cited there); androidx CursorAdapter is not in the dataset, INFERRED')

e('CurrencyListFragment$1.onLoadFinished', 'CurrencyListAdapter.bindView', 'FRAMEWORK',
  'the same relayout (changeCursor at 479) makes the framework call getView, which calls bindView for every visible row',
  evidence='SRC currency/list/CurrencyListFragment.java:479; SRC currency/list/CurrencyListAdapter.java:29, 35; same chain as label_014.py:14-16; androidx CursorAdapter INFERRED as in label_014')

# ---- EventBus (greenrobot): REGISTER edges are skipped by reachability; the ASYNC edges below carry the route to each handler

e('CurrencyListFragment.onStart', 'CurrencyListFragment.onEvent(PriceDownloadedEvent)', 'REGISTER',
  'onStart registers the fragment on EventBus; EventBus calls the @Subscribe method for PriceDownloadedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at CurrencyListFragment.java:114; @Subscribe at 354 (onEvent(PriceDownloadedEvent)); library dispatch INFERRED',
  evidence='SRC currency/list/CurrencyListFragment.java:110-122 (register at 114, unregister at 121), 354-358; INFERRED EventBus library source not read')

e('CurrencyListFragment.onStart', 'CurrencyListFragment.onEvent(ExchangeRateUpdateConfirmedEvent)', 'REGISTER',
  'onStart registers the fragment on EventBus; EventBus calls the @Subscribe method for ExchangeRateUpdateConfirmedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at CurrencyListFragment.java:114; @Subscribe at 360 (onEvent(ExchangeRateUpdateConfirmedEvent)); library dispatch INFERRED',
  evidence='SRC currency/list/CurrencyListFragment.java:110-122 (register at 114, unregister at 121), 360-369; INFERRED EventBus library source not read')

e('CurrencyListFragment.onStart', 'CurrencyListFragment.onEvent(CurrencyDeletionConfirmedEvent)', 'REGISTER',
  'onStart registers the fragment on EventBus; EventBus calls the @Subscribe method for CurrencyDeletionConfirmedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at CurrencyListFragment.java:114; @Subscribe at 371 (onEvent(CurrencyDeletionConfirmedEvent)); library dispatch INFERRED',
  evidence='SRC currency/list/CurrencyListFragment.java:110-122 (register at 114, unregister at 121), 371-380; INFERRED EventBus library source not read')

# ---- EventBus posters (ASYNC): each post dispatches to the @Subscribe method

e('CurrencyUIFeatures$3.onClick', 'CurrencyListFragment.onEvent(CurrencyDeletionConfirmedEvent)', 'ASYNC',
  'the user confirms the currency deletion dialog: the listener posts CurrencyDeletionConfirmedEvent and EventBus calls the subscriber',
  gui=['Confirm the currency deletion dialog'],
  cls='non_standard', via='EventBus (greenrobot): post(new CurrencyDeletionConfirmedEvent(...)) at CurrencyUIFeatures.java:123 to the @Subscribe method (library dispatch INFERRED)',
  evidence='SRC currency/CurrencyUIFeatures.java:113-134 (showDialogDeleteCurrency; the listener is $3.onClick), 123 (post); SRC currency/list/CurrencyListFragment.java:371-372 (@Subscribe, decl); INFERRED EventBus library source not read')

e('CurrencyUIFeatures$7.onClick', 'CurrencyListFragment.onEvent(ExchangeRateUpdateConfirmedEvent)', 'ASYNC',
  'the user confirms the exchange rate update: the listener posts ExchangeRateUpdateConfirmedEvent(true) and EventBus calls the subscriber',
  gui=['Confirm the exchange rate update dialog'],
  cls='non_standard', via='EventBus (greenrobot): post(new ExchangeRateUpdateConfirmedEvent(true)) at CurrencyUIFeatures.java:169 to the @Subscribe method (library dispatch INFERRED)',
  evidence='SRC currency/CurrencyUIFeatures.java:159-180 (showDialogUpdateExchangeRates; the listener is $7.onClick), 169 (post); SRC currency/list/CurrencyListFragment.java:360-361 (@Subscribe, decl); INFERRED EventBus library source not read')

e('FixerService.onContentDownloaded', 'CurrencyListFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'a Fixer price download finishes: the service posts PriceDownloadedEvent and EventBus calls the subscriber while the currency list is started',
  env=env_text('a Fixer price download finishes while the currency list is started (registered on EventBus between onStart and onStop)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(new PriceDownloadedEvent(...)) at FixerService.java:120 to the @Subscribe method (library dispatch INFERRED)',
  evidence='SRC investment/prices/FixerService.java:100 (onContentDownloaded), 120 (post); SRC currency/list/CurrencyListFragment.java:354-355 (@Subscribe, decl); INFERRED EventBus library source not read')

e('YqlSecurityPriceUpdaterRetrofit.onContentDownloaded', 'CurrencyListFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'a YQL price download finishes: the updater posts PriceDownloadedEvent and EventBus calls the subscriber while the currency list is started',
  env=env_text('a YQL price download finishes while the currency list is started (registered on EventBus between onStart and onStop)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(new PriceDownloadedEvent(...)) at YqlSecurityPriceUpdaterRetrofit.java:130 to the @Subscribe method (library dispatch INFERRED)',
  evidence='SRC investment/yql/YqlSecurityPriceUpdaterRetrofit.java:113 (onContentDownloaded), 130 (post); SRC currency/list/CurrencyListFragment.java:354-355 (@Subscribe, decl); INFERRED EventBus library source not read')

e('YahooCsvQuoteDownloaderRetrofit.onContentDownloaded', 'CurrencyListFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'a Yahoo CSV price download finishes and parses: the downloader posts PriceDownloadedEvent and EventBus calls the subscriber while the currency list is started',
  env=env_text('a Yahoo CSV price download finishes while the currency list is started (registered on EventBus between onStart and onStop)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(event) at YahooCsvQuoteDownloaderRetrofit.java:124 to the @Subscribe method (library dispatch INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:103 (onContentDownloaded), 116 (parse), 123-125 (post at 124); SRC currency/list/CurrencyListFragment.java:354-355 (@Subscribe, decl); INFERRED EventBus library source not read')

# ---- user actions on the currency list (GUI from S_CURRENCY_LIST)

gui('S_CURRENCY_LIST', 'CurrencyListActivity.onKeyUp', 'press Back while the currency list is in front',
  evidence='SRC currency/list/CurrencyListActivity.java:69-80 (onKeyUp 70; KEYCODE_BACK 75; setResultAndFinish 76); FW-SRC core/java/android/app/Activity.java:3255-3272 (dispatchKeyEvent passes the key to event.dispatch); FW-SRC core/java/android/view/KeyEvent.java:2709-2715 (ACTION_UP calls receiver.onKeyUp)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onListItemClick', 'tap a currency row in the list',
  evidence='SRC core/AbsListFragment.java:40-47 (onItemClick calls onListItemClick at 44); SRC currency/list/CurrencyListFragment.java:329-341 (openContextMenu 336; setResultAndFinish 339)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onCreateContextMenu', 'long-press a currency row (the list is registered for the context menu at line 155)',
  evidence='SRC currency/list/CurrencyListFragment.java:155 (registerForContextMenu), 215-229 (onCreateContextMenu); INFERRED View long-press dispatch (android.view.View not read in this batch)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onContextItemSelected', 'tap an item of the row context menu (chart, edit, update rate or delete)',
  evidence='SRC currency/list/CurrencyListFragment.java:231-283 (edit 245; getService and update rate 266; delete dialog 278); label_046.py:14 (the chart item, case 1 at 257-262)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onOptionsItemSelected', 'tap an options menu item (import all currencies, update exchange rates, reload)',
  evidence='SRC currency/list/CurrencyListFragment.java:183-211 (showDialogImportAllCurrencies 189; showDialogUpdateExchangeRates 193; reloadData 206); INFERRED androidx options-menu dispatch (library not read)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onPrepareOptionsMenu', 'open the options menu (the framework prepares it before it is shown)',
  evidence='SRC currency/list/CurrencyListFragment.java:175-181; INFERRED androidx calls onPrepareOptionsMenu before it shows the menu (library not read)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onQueryTextChange', 'type in the search box of the currency list',
  evidence='SRC common/BaseListFragment.java:224-227 (onPreQueryTextChange returns onQueryTextChange at 226); SRC currency/list/CurrencyListFragment.java:287-295 (reloadData 293); INFERRED androidx SearchView calls the listener (not in fw_src)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onFloatingActionButtonClicked', 'tap the + button on the currency list',
  evidence='SRC currency/list/CurrencyListFragment.java:323-327 (startCurrencyEditActivity 326); SRC common/BaseListFragment.java:238-248 (FAB listener at 241-246, call at 244); the listener edge to this override is cut in label_026.py:54, so this GUI edge is the route')

# ---- UNREACHABLE: batch 049 methods with no trigger in the app

UNREACHABLE['CurrencyListFragment.initializeSwipeToRefresh'] = (
  'no_trigger_in_app',
  'method with an empty body (lines 494-496). Its only call, at line 105 in onCreateView, is commented out, so no caller exists and no auto CALL record has it as destination',
  'SRC currency/list/CurrencyListFragment.java:103-108 (105 commented out), 494-496 (empty body)',
  'SOURCE')

UNREACHABLE['CurrencyContentObserver.<init>'] = (
  'no_trigger_in_app',
  'the only creator is CurrencyRecyclerListFragment.onCreate (line 93), which is UNREACHABLE (batch 050). The CALL from that method to this constructor is cut in label_050.py:44. auto_calls.json has one CALL record with this constructor as destination, and its source is that UNREACHABLE method, so the constructor never runs',
  'SRC currency/recycler/CurrencyContentObserver.java:35-37; SRC currency/recycler/CurrencyRecyclerListFragment.java:93; label_050.py:44; auto_calls.json (one CALL record with dst CurrencyContentObserver.<init>)',
  'SOURCE')

UNREACHABLE['CurrencyContentObserver.onChange(boolean)'] = (
  'no_trigger_in_app',
  'reached only by the framework ContentObserver dispatch, and that needs a registered instance. The instance is never built (see CurrencyContentObserver.<init> above). Registration sits in CurrencyRecyclerListFragment.onPause (line 137), which is UNREACHABLE. No auto CALL record has this method as destination',
  'SRC currency/recycler/CurrencyContentObserver.java:39-42 (41 is the call to onChange(boolean,Uri)); SRC currency/recycler/CurrencyRecyclerListFragment.java:137; auto_calls.json (no record with dst CurrencyContentObserver.onChange(boolean))',
  'SOURCE')

UNREACHABLE['CurrencyContentObserver.onChange(boolean,Uri)'] = (
  'no_trigger_in_app',
  'the only in-app caller is onChange(boolean) at line 41 (auto CALL record), which is UNREACHABLE. This method never runs. The CALL edge from onChange(boolean) is cut by the sup below',
  'SRC currency/recycler/CurrencyContentObserver.java:41 (the call), 44-50 (the method body; logs only at 49); auto_calls.json CALL record CurrencyContentObserver.onChange(boolean) to onChange(boolean,Uri), line 41',
  'SOURCE')

# sup cut owned by this batch: the caller onChange(boolean) is UNREACHABLE, so its CALL to onChange(boolean,Uri) is cut
sup(('CurrencyContentObserver.onChange(boolean)', 'CurrencyContentObserver.onChange(boolean,Uri)'))  # line 41
