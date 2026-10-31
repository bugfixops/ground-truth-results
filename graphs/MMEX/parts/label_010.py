# ================================================================== batch 010 (label_010): com.money.manager.ex.account.AccountTransactionListFragment (40 of its 56 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_010.md.
# Every edge below has a batch 010 method as its destination, except the ASYNC edge whose source is CalculateRunningBalanceTask2.onPostExecute (batch 012 owns that method and its route) and the GUI and ENTERS edges from the page this batch defines.
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here, except three interface forwards from AllDataListFragment that the bytecode does not record.
# Framework and library claims are INFERRED where the library source was not read (androidx Fragment, LoaderManager, EventBus, AppCompat).

# ---- screen: the account transaction list. Batch 011 reuses this key and does not redefine it.

SCREENS.update({
    'S_ACCOUNT_TRANSACTIONS': 'Account transaction list (AccountTransactionListFragment): the account header with the balances, the transaction list, the account spinner in the action bar, and the options menu (period, status, filters, add transaction, export to CSV)',
})

e('AccountTransactionListFragment.onCreateView', 'S_ACCOUNT_TRANSACTIONS', 'ENTERS',
  'the account transaction list is shown: the header is added and the transaction list fragment is placed in R.id.fragmentMain',
  evidence='SRC account/AccountTransactionListFragment.java:163, 170-174, 181; SRC account/AccountTransactionListFragment.java:850 (transaction.replace into R.id.fragmentMain)')

# ---- lifecycle of the fragment (androidx Fragment; library source not read: INFERRED)

e('AccountTransactionListFragment.<init>', 'AccountTransactionListFragment.onAttach', 'LIFECYCLE',
  'the FragmentManager attaches the fragment when the transaction that adds it commits (MainActivity.showFragment, MainActivity.java:768-773)',
  evidence='SRC account/AccountTransactionListFragment.java:102-103; SRC home/MainActivity.java:768-773; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onAttach', 'AccountTransactionListFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after onAttach',
  evidence='SRC account/AccountTransactionListFragment.java:129-136; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onCreate', 'AccountTransactionListFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC account/AccountTransactionListFragment.java:136, 155; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onCreateView', 'AccountTransactionListFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onCreateView',
  evidence='SRC account/AccountTransactionListFragment.java:155, 187; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onActivityCreated', 'AccountTransactionListFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after onActivityCreated',
  evidence='SRC account/AccountTransactionListFragment.java:187, 198; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onStart', 'AccountTransactionListFragment.onResume', 'LIFECYCLE',
  'the framework calls onResume after onStart',
  evidence='SRC account/AccountTransactionListFragment.java:198, 205; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onResume', 'AccountTransactionListFragment.onStop', 'LIFECYCLE',
  'the user leaves the screen: the framework pauses and then stops the fragment (the pause is not a method of this class)',
  evidence='SRC account/AccountTransactionListFragment.java:205, 218; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onResume', 'AccountTransactionListFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state when the activity leaves the foreground (the state is saved before the fragment stops)',
  evidence='SRC account/AccountTransactionListFragment.java:384-392; INFERRED androidx FragmentManager saves state through onSaveInstanceState (library source not read)')

e('AccountTransactionListFragment.onStop', 'AccountTransactionListFragment.onDestroy', 'LIFECYCLE',
  'the fragment is removed from its container (for example when MainActivity shows another fragment) and the framework destroys it',
  evidence='SRC account/AccountTransactionListFragment.java:218, 395; SRC home/MainActivity.java:768-773; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- EventBus: registered in onStart, the balance task posts the event from onPostExecute (library: INFERRED)

e('AccountTransactionListFragment.onStart', 'AccountTransactionListFragment.onEvent', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe method onEvent receives RunningBalanceCalculatedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at line 201, unregister at line 221, @Subscribe at line 409 (library source not read, INFERRED)',
  evidence='SRC account/AccountTransactionListFragment.java:198-202, 218-222, 407-413; INFERRED EventBus library source not read')

e('CalculateRunningBalanceTask2.onPostExecute', 'AccountTransactionListFragment.onEvent', 'ASYNC',
  'the balance task posts RunningBalanceCalculatedEvent on EventBus when it finishes; the registered fragment receives it in onEvent',
  guard='the fragment is registered: onStart has run and onStop has not (lines 201 and 221)',
  cls='non_standard', via='EventBus post at CalculateRunningBalanceTask2.java:99 to the subscriber registered in onStart (library source not read, INFERRED)',
  evidence='SRC account/CalculateRunningBalanceTask2.java:97-100 (post at 99); SRC account/AccountTransactionListFragment.java:409-413; INFERRED EventBus library source not read')

# ---- options menu: the page's menu items, the menu opening, and the framework rebuild after invalidateOptionsMenu

e('S_ACCOUNT_TRANSACTIONS', 'AccountTransactionListFragment.onOptionsItemSelected', 'GUI',
  'tap an options menu item of the account transaction list: period, transaction status, filter, add transaction or export to CSV',
  gui=['Tap an item of the options menu (period, status, filter, add transaction, export to CSV) on the account transaction list'],
  evidence='SRC account/AccountTransactionListFragment.java:237-245 (menu resources inflated), 286-320 (item dispatch); INFERRED androidx FragmentManager dispatches onOptionsItemSelected to the fragment (library source not read)')

e('S_ACCOUNT_TRANSACTIONS', 'AccountTransactionListFragment.onPrepareOptionsMenu', 'GUI',
  'open the options menu of the account transaction list: the framework prepares it before it is shown',
  gui=['Open the options menu of the account transaction list (overflow icon)'],
  evidence='SRC account/AccountTransactionListFragment.java:252-283; INFERRED androidx FragmentManager dispatches onPrepareOptionsMenu to the fragment (library source not read)')

e('AccountTransactionListFragment.refreshSettings', 'AccountTransactionListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'refreshSettings calls getActivity().invalidateOptionsMenu(), so the host activity rebuilds its options menu and the framework calls the fragment onCreateOptionsMenu',
  guard='the fragment has its options menu enabled: setHasOptionsMenu(true) at line 181',
  evidence='SRC account/AccountTransactionListFragment.java:181, 881-888 (invalidateOptionsMenu at 887); FW-SRC core/java/android/app/Activity.java:3512-3516 (platform invalidateOptionsMenu calls invalidatePanelMenu); INFERRED AppCompat delegate and androidx FragmentManager dispatch (library source not read)')

e('AccountTransactionListFragment.refreshSettings', 'AccountTransactionListFragment.onPrepareOptionsMenu', 'FRAMEWORK',
  'the same invalidateOptionsMenu call (line 887) makes the framework prepare the rebuilt options menu through onPrepareOptionsMenu',
  guard='the fragment has its options menu enabled: setHasOptionsMenu(true) at line 181',
  evidence='SRC account/AccountTransactionListFragment.java:181, 881-888; FW-SRC core/java/android/app/Activity.java:3512-3516; INFERRED AppCompat delegate and androidx FragmentManager dispatch (library source not read)')

# ---- loader callbacks. AllDataListFragment forwards its loader events to this fragment (the parent set at line 847).
# The bytecode of AllDataListFragment does not record these interface calls, so they are written here as CALL edges.

e('AllDataListFragment.onCreateLoader', 'AccountTransactionListFragment.onCreateLoader', 'CALL',
  'AllDataListFragment forwards onCreateLoader to this fragment, the parent set by setSearResultFragmentLoaderCallbacks (line 847)',
  guard='the parent callbacks are set: showTransactionsFragment runs before the list loads (lines 837-847)',
  evidence='SRC common/AllDataListFragment.java:219-221 (forward at 221); SRC account/AccountTransactionListFragment.java:847; interface call, not recorded in auto_calls.json')

e('AllDataListFragment.onLoadFinished', 'AccountTransactionListFragment.onLoadFinished', 'CALL',
  'AllDataListFragment forwards the loader result to this fragment (line 264); for the transaction list loader this restarts the summary loader and refreshes the running balance',
  guard='the parent callbacks are set (line 847)',
  evidence='SRC common/AllDataListFragment.java:262-265 (forward at 264); SRC account/AccountTransactionListFragment.java:354-379; interface call, not recorded in auto_calls.json')

e('AllDataListFragment.onLoaderReset', 'AccountTransactionListFragment.onLoaderReset', 'CALL',
  'AllDataListFragment forwards onLoaderReset to this fragment (line 255); this fragment does nothing there',
  guard='the parent callbacks are set (line 847)',
  evidence='SRC common/AllDataListFragment.java:253-255 (forward at 255); SRC account/AccountTransactionListFragment.java:349-351; interface call, not recorded in auto_calls.json')

e('AccountTransactionListFragment.onLoadFinished', 'AccountTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'getLoaderManager().restartLoader(ID_LOADER_SUMMARY, null, this) creates the summary loader through onCreateLoader (the loader manager calls the callbacks)',
  evidence='SRC account/AccountTransactionListFragment.java:370-373 (restartLoader at 373); INFERRED androidx LoaderManager.restartLoader calls LoaderCallbacks.onCreateLoader (library source not read)')

# ---- UNREACHABLE: no caller in the app (grep output: graphs/MMEX/parts/label_010.grep.txt)

UNREACHABLE['AccountTransactionListFragment.populateRunningBalanceRx'] = ('no_trigger_in_app',
  'private method with no caller in the app: the only occurrence of the name in the source root is its declaration (label_010.grep.txt). Its body only builds the query (line 653) and stops; the running balance is populated by populateRunningBalance (line 375), so nothing calls this method',
  'SRC account/AccountTransactionListFragment.java:649-656; grep label_010.grep.txt', 'SOURCE')

sup(('AccountTransactionListFragment.populateRunningBalanceRx', 'AccountTransactionListFragment.prepareQuery'))  # the bytecode call from this unreachable method cannot run
