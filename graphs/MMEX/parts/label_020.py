# ================================================================== batch 020 (label_020): com.money.manager.ex.common.AllDataListFragment (methods 1-40 of 63)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_020.md.
# Grep evidence for the two UNREACHABLE methods and the menu and library claims: graphs/MMEX/parts/label_020.grep.txt.
# Page S_ACCOUNT_TRANSACTIONS is defined in label_010.py and only reused here. The search results screen (SearchActivity, batch 107) hosts the same fragment too; no page key is defined for it here, so its entry edges start from SearchActivity methods.
# CALL edges come from auto_calls.json and are not written here. Framework and library claims (androidx Fragment, FragmentManager, LoaderManager, FragmentActivity options dispatch) are INFERRED: the androidx source is not read. FW-SRC is cited where the platform source applies.

# ---- lifecycle of the list fragment. On the account screen it is a child of AccountTransactionListFragment (child FragmentManager, line 835);
# on the search screen SearchActivity adds it to the activity FragmentManager (SearchActivity.java:205, commit at 212).

e('AccountTransactionListFragment.showTransactionsFragment', 'AllDataListFragment.onCreate', 'FRAMEWORK',
  'the child FragmentManager runs the replace when the transaction commits (line 851): the framework attaches the new fragment and calls its onCreate',
  evidence='SRC account/AccountTransactionListFragment.java:835-851 (getChildFragmentManager 835; newInstance 837; setAutoStarLoader 846; replace 850; commit 851); INFERRED androidx FragmentManager (library source not read)')

e('SearchActivity.showSearchResultsFragment', 'AllDataListFragment.onCreate', 'FRAMEWORK',
  'the search results fragment is added to R.id.fragmentDetail and the transaction commits (SearchActivity.java:205, 212); the framework calls onCreate of the new fragment',
  evidence='SRC search/SearchActivity.java:183 (newInstance), 205 (add), 212 (commit); INFERRED androidx FragmentManager (library source not read)')

e('AllDataListFragment.onCreate', 'AllDataListFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC common/AllDataListFragment.java:204-214; INFERRED androidx Fragment lifecycle (library source not read)')

e('AllDataListFragment.onCreateView', 'AllDataListFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onCreateView (the view exists; the list and the adapter are set up in it)',
  evidence='SRC common/AllDataListFragment.java:128-130, 211-214; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onStop', 'AllDataListFragment.onStop', 'FRAMEWORK',
  'the child list fragment stops when its parent stops (parent onStop at line 218)',
  guard='the account screen is shown: the list is a child of AccountTransactionListFragment',
  evidence='SRC account/AccountTransactionListFragment.java:218 (parent onStop); SRC common/AllDataListFragment.java:341-358; INFERRED androidx FragmentManager dispatches the stop to child fragments (library source not read)')

e('AllDataListFragment.onStop', 'AllDataListFragment.onDestroy', 'LIFECYCLE',
  'the framework destroys the fragment after it stops (its container is removed or the parent is destroyed)',
  evidence='SRC common/AllDataListFragment.java:328-333, 341-343; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onResume', 'AllDataListFragment.onResume', 'FRAMEWORK',
  'the child list fragment resumes when its parent resumes (parent onResume at line 205)',
  guard='the account screen is resumed (the parent is visible)',
  evidence='SRC account/AccountTransactionListFragment.java:205 (parent onResume); SRC common/AllDataListFragment.java:335-339; INFERRED androidx FragmentManager dispatches the resume to child fragments (library source not read)')

e('SearchActivity.onResume', 'AllDataListFragment.onResume', 'FRAMEWORK',
  'the search screen resumes: super.onResume (SearchActivity.java:74) makes the framework dispatch onResume to the fragments of the activity',
  guard='the search results fragment is in the activity FragmentManager (added at SearchActivity.java:205)',
  evidence='SRC search/SearchActivity.java:72-80 (super.onResume at 74; loadData at 79); SRC common/AllDataListFragment.java:335-339; INFERRED androidx FragmentActivity dispatches onResume to its fragments (library source not read)')

# ---- options menu. The fragment has an options menu (setHasOptionsMenu at line 208). On the account screen the parent calls onCreateOptionsMenu (auto edge at AccountTransactionListFragment.java:248).

e('SearchActivity.onCreateOptionsMenu', 'AllDataListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options panel: onCreatePanelMenu calls the activity onCreateOptionsMenu (SearchActivity.java:91-104), then the fragments with an options menu add their items; on the search screen this adds menu_alldata_operations (line 323)',
  guard='the fragment has its options menu enabled: setHasOptionsMenu(true) at AllDataListFragment.java:208',
  evidence='SRC search/SearchActivity.java:91-104 (inflate at 97); SRC common/AllDataListFragment.java:204-209, 300-326 (search-only inflation at 318-323); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreatePanelMenu calls onCreateOptionsMenu at 3388); INFERRED androidx FragmentActivity dispatch to fragments (library source not read)')

e('SearchActivity.onOptionsItemSelected', 'AllDataListFragment.onOptionsItemSelected', 'FRAMEWORK',
  'an item that is not the Up arrow or the search item: the default branch returns super (SearchActivity.java:118), and the framework then dispatches the item to the fragments; the QIF item of the search screen reaches this fragment',
  guard='the item is menu_qif_export (added by onCreateOptionsMenu on the search screen); the home and search cases return before this',
  evidence='SRC search/SearchActivity.java:107-120 (default super at 118); SRC common/AllDataListFragment.java:360-374; FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450), 3597-3599 (the Activity body returns mParent.onOptionsItemSelected); INFERRED androidx FragmentActivity dispatch to fragments (library source not read)')

# ---- loader. loadData(Bundle) restarts the loader; the LoaderManager then calls the callbacks (LoaderManager is androidx: INFERRED).

e('AllDataListFragment.loadData(Bundle)', 'AllDataListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader (line 532) starts the loader for ID_LOADER_ALL_DATA_DETAIL and the LoaderManager calls onCreateLoader with the arguments',
  evidence='SRC common/AllDataListFragment.java:521-533 (restartLoader at 532); INFERRED androidx LoaderManager calls the callbacks (library source not read)')

e('AllDataListFragment.loadData(Bundle)', 'AllDataListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader finishes its query and the LoaderManager delivers the cursor to onLoadFinished on the main thread',
  guard='the query started by restartLoader (line 532) completes',
  evidence='SRC common/AllDataListFragment.java:521-533 (restartLoader at 532); INFERRED androidx LoaderManager delivers results to the callbacks (library source not read)')

e('AllDataListFragment.loadData(Bundle)', 'AllDataListFragment.onLoaderReset', 'FRAMEWORK',
  'restartLoader destroys the loader that already exists for the same id, and the LoaderManager calls onLoaderReset for it',
  guard='a loader for ID_LOADER_ALL_DATA_DETAIL already delivered its data (the second and later loadData calls)',
  evidence='SRC common/AllDataListFragment.java:521-533 (restartLoader at 532); INFERRED androidx LoaderManager resets an old loader on restart (library source not read)')

# ---- user actions on the account screen: the + button (the list shows it when the fragment is built with the floating button flag)

gui('S_ACCOUNT_TRANSACTIONS', 'AllDataListFragment.onFloatingActionButtonClicked', 'Tap the + button on the account transaction list',
    evidence='SRC common/AllDataListFragment.java:191-196 (the button is shown when ARG_SHOW_FLOATING_BUTTON is true, set by newInstance(int) at 92), 381-384; SRC account/AccountTransactionListFragment.java:837; SRC common/BaseListFragment.java:238-248 (listener 241-246, call at 244); auto_calls.json record BaseListFragment$2.onClick -> AllDataListFragment.onFloatingActionButtonClicked (BaseListFragment.java:244, cha)')

# ---- auto edges that cannot run: the export case of the menu of this fragment, and the export case of the parent (cross-batch sources)

# line 365: the export case in onOptionsItemSelected is never taken (menu_export_to_csv is in no shown menu; grep sections B-E)
sup(('AllDataListFragment.onOptionsItemSelected', 'AllDataListFragment.exportDataToCSVFile()'))

# line 465: the zero-argument overload calls the prefix overload, but the zero-argument overload itself cannot run
sup(('AllDataListFragment.exportDataToCSVFile()', 'AllDataListFragment.exportDataToCSVFile(String)'))

# line 305 (AccountTransactionListFragment.java:303-306): the parent's export case is never taken either; batch 010 owns the source, this batch owns the destination
sup(('AccountTransactionListFragment.onOptionsItemSelected', 'AllDataListFragment.exportDataToCSVFile(String)'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_020.grep.txt)

UNREACHABLE['AllDataListFragment.exportDataToCSVFile()'] = (
  'branch_never_taken',
  'Its only caller is the export case of AllDataListFragment.onOptionsItemSelected (line 364-365). That case needs R.id.menu_export_to_csv to be the id of an item in a menu the fragment is shown with. The id is declared only in res/menu/menu_main.xml:60, res/menu-v14/menu_main.xml:65 and res/menu/menu_search_transaction.xml:30, and no Java in the source root inflates menu_main or menu_search_transaction (grep sections B-D). The menus that are actually shown here do not declare it: the account screen inflates menu_period_picker_transactions, menu_transaction_status_selector and menu_transaction_filters (AccountTransactionListFragment.java:237-244); the search screen inflates menu_search (SearchActivity.java:97, no export id; section F) and menu_alldata_operations (only menu_qif_export, section G); the action mode inflates menu_all_data_adapter (line 393). The export case never runs.',
  'common/AllDataListFragment.java:360-374 (case 364-367), 461-466; account/AccountTransactionListFragment.java:237-244; search/SearchActivity.java:97; common/AllDataListFragment.java:318-323, 393; res/menu/menu_alldata_operations.xml:23; graphs/MMEX/parts/label_020.grep.txt sections A-G, O',
  'SOURCE')

UNREACHABLE['AllDataListFragment.exportDataToCSVFile(String)'] = (
  'branch_never_taken',
  'Its callers are exportDataToCSVFile() (line 465), which cannot run (see the entry above), and the case R.id.menu_export_to_csv of AccountTransactionListFragment.onOptionsItemSelected (AccountTransactionListFragment.java:303-305). That case cannot run either: the parent fragment inflates only menu_period_picker_transactions, menu_transaction_status_selector and menu_transaction_filters (lines 237-244), and none of them declares the id (grep sections A-B). No other caller exists in the source root (section A).',
  'common/AllDataListFragment.java:461-477; account/AccountTransactionListFragment.java:237-248, 303-306; graphs/MMEX/parts/label_020.grep.txt sections A, B, E',
  'SOURCE')
