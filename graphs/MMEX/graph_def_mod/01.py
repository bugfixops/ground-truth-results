
e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getChildView', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then draws the child rows of each group the user expands (a tap on the group row)',
  needs_state=state_text('a child row exists: the account type group holds at least one account (mAccountsByType, HomeAccountsExpandableAdapter.java:77)', ('data',)),
  evidence='SRC home/HomeFragment.java:811-814; SRC home/HomeAccountsExpandableAdapter.java:196-216; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.hasStableIds', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter whether its ids are stable',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.isChildSelectable', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter whether a child row is selectable',
  needs_state=state_text('a child row exists: the account type group holds at least one account (mAccountsByType, HomeAccountsExpandableAdapter.java:77)', ('data',)),
  evidence='SRC home/HomeFragment.java:811-814; SRC home/HomeAccountsExpandableAdapter.java:236-239; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

# ---- UNREACHABLE (6). Tuple: (kind, reason, evidence, confirmed_by)
UNREACHABLE['DrawerMenuItem.withDivider'] = ('no_trigger_in_app',
  'no call site in the app source: the two withDivider calls in MainActivity (1105, 1116) are comments, so mDivider stays false and hasDivider is always false',
  'SRC home/DrawerMenuItem.java:81-84; SRC home/MainActivity.java:1105, 1116; label_076.grep.txt section 2',
  'SOURCE')

UNREACHABLE['DrawerMenuItemRecyclerAdapter.<init>'] = ('no_trigger_in_app',
  'no caller: no code creates a DrawerMenuItemRecyclerAdapter (the name appears only in its own file)',
  'SRC home/DrawerMenuItemRecyclerAdapter.java:34-36; label_076.grep.txt section 1',
  'SOURCE')

UNREACHABLE['DrawerMenuItemRecyclerAdapter.add'] = ('no_trigger_in_app',
  'no caller: add runs only on an adapter instance, and no instance is created',
  'SRC home/DrawerMenuItemRecyclerAdapter.java:57-59; label_076.grep.txt section 1',
  'SOURCE')

UNREACHABLE['DrawerMenuItemRecyclerAdapter.getItemCount'] = ('no_trigger_in_app',
  'RecyclerView.Adapter override: RecyclerView calls it only for an adapter attached to a RecyclerView, and no instance is created',
  'SRC home/DrawerMenuItemRecyclerAdapter.java:52-55; label_076.grep.txt section 1; INFERRED RecyclerView dispatch (androidx library not read)',
  'INFERRED')

UNREACHABLE['DrawerMenuItemRecyclerAdapter.onBindViewHolder'] = ('no_trigger_in_app',
  'RecyclerView.Adapter override (empty body): RecyclerView calls it only for an adapter attached to a RecyclerView, and no instance is created',
  'SRC home/DrawerMenuItemRecyclerAdapter.java:47-50; label_076.grep.txt section 1; INFERRED RecyclerView dispatch (androidx library not read)',
  'INFERRED')

UNREACHABLE['DrawerMenuItemRecyclerAdapter.onCreateViewHolder'] = ('no_trigger_in_app',
  'RecyclerView.Adapter override (returns null): RecyclerView calls it only for an adapter attached to a RecyclerView, and no instance is created',
  'SRC home/DrawerMenuItemRecyclerAdapter.java:40-45; label_076.grep.txt section 1; INFERRED RecyclerView dispatch (androidx library not read)',
  'INFERRED')

# ---- part 075 (2026-10-29)
# ================================================================== batch 075 (label_075): DashboardFragment (16 methods),
# DatabaseMetadata (4), DatabaseMetadataFactory (5) and DrawerMenuGroupAdapter (13): 38 in total (graphs/MMEX/scratch/batches/batch_075.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_075.md.
# Edges written here: 10 FRAMEWORK edges from MainActivity.createExpandableDrawer (source owned by another batch; D1: ownership by destination,
# so the edges sit in this part) to the DrawerMenuGroupAdapter callbacks that no auto_calls.json record reaches. Every other REACHABLE route is an auto CALL record, so no e() is written (D7).
# sup: 44 pairs, one for each auto CALL record whose caller is a DashboardFragment method (UNREACHABLE in this batch, D14a).
# UNREACHABLE: the 16 DashboardFragment methods, all SOURCE: the class is never constructed.
# No grep file: no library or generated class is involved.
# The navigation drawer has no SCREENS key (graph_def.py has no S_HOME), so no gui() edge is written for the group taps.

# ---- framework-dispatched drawer callbacks. MainActivity.createExpandableDrawer sets the adapter on the drawer list (line 933);
# the list view and its connector then call these callbacks (ExpandableListView is not in fw_src: INFERRED, same pattern as label_015.py:21-36).
e('MainActivity.createExpandableDrawer', 'DrawerMenuGroupAdapter.getChildView', 'FRAMEWORK',
  'the drawer list takes this adapter (drawerList.setAdapter, line 933); the framework then asks the adapter for the view of each visible child row',
  guard='the drawer exists: createExpandableDrawer runs only after initializeDrawer found mDrawer (MainActivity.java:1294, 1301)',
  evidence='SRC home/MainActivity.java:931-933, 1289-1301; SRC home/DrawerMenuGroupAdapter.java:63-96; INFERRED ExpandableListView and its connector call the adapter (framework source not in fw_src, not read)')

e('MainActivity.createExpandableDrawer', 'DrawerMenuGroupAdapter.getGroupView', 'FRAMEWORK',
  'the drawer list takes this adapter (line 933); the framework then asks the adapter for the view of each visible group row',
  guard='the drawer exists: createExpandableDrawer runs only after initializeDrawer found mDrawer (MainActivity.java:1294, 1301)',
  evidence='SRC home/MainActivity.java:931-933; SRC home/DrawerMenuGroupAdapter.java:134-178; INFERRED ExpandableListView and its connector call the adapter (framework source not in fw_src, not read)')

e('MainActivity.createExpandableDrawer', 'DrawerMenuGroupAdapter.getChildId', 'FRAMEWORK',
  'the framework asks the adapter for the id of each child row (returns 0, line 59); the list takes this adapter at line 933',
  guard='the drawer exists: createExpandableDrawer runs only after initializeDrawer found mDrawer (MainActivity.java:1294, 1301)',
  evidence='SRC home/MainActivity.java:931-933; SRC home/DrawerMenuGroupAdapter.java:58-60; INFERRED ExpandableListView and its connector call the adapter (framework source not in fw_src, not read)')

e('MainActivity.createExpandableDrawer', 'DrawerMenuGroupAdapter.getGroupId', 'FRAMEWORK',
  'the framework asks the adapter for the id of each group row (returns 0, line 130); the list takes this adapter at line 933',
  guard='the drawer exists: createExpandableDrawer runs only after initializeDrawer found mDrawer (MainActivity.java:1294, 1301)',
  evidence='SRC home/MainActivity.java:931-933; SRC home/DrawerMenuGroupAdapter.java:129-131; INFERRED ExpandableListView and its connector call the adapter (framework source not in fw_src, not read)')

e('MainActivity.createExpandableDrawer', 'DrawerMenuGroupAdapter.getGroup', 'FRAMEWORK',
  'the framework asks the adapter for the group item at a position (line 110); the list takes this adapter at line 933',
  guard='the drawer exists: createExpandableDrawer runs only after initializeDrawer found mDrawer (MainActivity.java:1294, 1301)',
  evidence='SRC home/MainActivity.java:931-933; SRC home/DrawerMenuGroupAdapter.java:109-111; INFERRED ExpandableListView and its connector call the adapter (framework source not in fw_src, not read)')

e('MainActivity.createExpandableDrawer', 'DrawerMenuGroupAdapter.getGroupCount', 'FRAMEWORK',
  'the framework asks the adapter for the number of groups (line 115) when the list is set; the list takes this adapter at line 933',
  guard='the drawer exists: createExpandableDrawer runs only after initializeDrawer found mDrawer (MainActivity.java:1294, 1301)',
  evidence='SRC home/MainActivity.java:931-933; SRC home/DrawerMenuGroupAdapter.java:114-116; INFERRED ExpandableListView and its connector call the adapter (framework source not in fw_src, not read)')

e('MainActivity.createExpandableDrawer', 'DrawerMenuGroupAdapter.hasStableIds', 'FRAMEWORK',
  'the framework asks the adapter whether ids are stable when the adapter is set (returns false, line 182); the list takes this adapter at line 933',
  guard='the drawer exists: createExpandableDrawer runs only after initializeDrawer found mDrawer (MainActivity.java:1294, 1301)',
  evidence='SRC home/MainActivity.java:931-933; SRC home/DrawerMenuGroupAdapter.java:181-183; INFERRED ExpandableListView and its connector call the adapter (framework source not in fw_src, not read)')

e('MainActivity.createExpandableDrawer', 'DrawerMenuGroupAdapter.isChildSelectable', 'FRAMEWORK',
  'the framework asks the adapter whether a child row is clickable (returns true, line 189); the list takes this adapter at line 933',
  guard='the drawer exists: createExpandableDrawer runs only after initializeDrawer found mDrawer (MainActivity.java:1294, 1301)',
  evidence='SRC home/MainActivity.java:931-933; SRC home/DrawerMenuGroupAdapter.java:186-189; INFERRED ExpandableListView and its connector call the adapter (framework source not in fw_src, not read)')

e('MainActivity.createExpandableDrawer', 'DrawerMenuGroupAdapter.onGroupCollapsed', 'FRAMEWORK',
  'the framework calls the adapter when the user collapses a group in the drawer (body calls super only, line 120); the list takes this adapter at line 933',
  guard='the drawer exists: createExpandableDrawer runs only after initializeDrawer found mDrawer (MainActivity.java:1294, 1301)',
  evidence='SRC home/MainActivity.java:931-933; SRC home/DrawerMenuGroupAdapter.java:119-121; INFERRED ExpandableListView and its connector call the adapter (framework source not in fw_src, not read)')

e('MainActivity.createExpandableDrawer', 'DrawerMenuGroupAdapter.onGroupExpanded', 'FRAMEWORK',
  'the framework calls the adapter when the user expands a group in the drawer (body calls super only, line 125); the list takes this adapter at line 933',
  guard='the drawer exists: createExpandableDrawer runs only after initializeDrawer found mDrawer (MainActivity.java:1294, 1301)',
  evidence='SRC home/MainActivity.java:931-933; SRC home/DrawerMenuGroupAdapter.java:124-126; INFERRED ExpandableListView and its connector call the adapter (framework source not in fw_src, not read)')

# ---- sup (D14a): every auto CALL record whose caller is a DashboardFragment method. Those callers are UNREACHABLE (below), so the
# edges from them to other classes (QueryBillDeposits, IncomeVsExpensesChartFragment, UIHelper, CurrencyService, Select, and others) are cut.
sup(
    ('DashboardFragment.onResume', 'DashboardFragment.loadData'),  # DashboardFragment.java:117
    ('DashboardFragment.onCreateLoader', 'QueryBillDeposits.<clinit>'),  # 181
    ('DashboardFragment.onCreateLoader', 'MmxCursorLoader.<init>(Context,Uri,Select)'),  # 186
    ('DashboardFragment.onCreateLoader', 'Dataset.getUri'),  # 186
    ('DashboardFragment.onCreateLoader', 'Select.orderBy'),  # 184
    ('DashboardFragment.onCreateLoader', 'Select.where(String)'),  # 183
    ('DashboardFragment.onCreateLoader', 'Select.<init>(String[])'),  # 182
    ('DashboardFragment.onCreateLoader', 'QueryBillDeposits.getAllColumns'),  # 182
    ('DashboardFragment.onCreateLoader', 'QueryBillDeposits.<init>'),  # 181
    ('DashboardFragment.onCreateLoader', 'SQLDataSet.<init>'),  # 178
    ('DashboardFragment.onCreateLoader', 'DashboardFragment.prepareQueryTopPayees'),  # 177
    ('DashboardFragment.onCreateLoader', 'Select.<init>()'),  # 177
    ('DashboardFragment.onCreateLoader', 'DashboardFragment.prepareQueryTopWithdrawals'),  # 173
    ('DashboardFragment.onCreateLoader', 'QueryReportIncomeVsExpenses.getAllColumns'),  # 165
    ('DashboardFragment.onCreateLoader', 'QueryReportIncomeVsExpenses.<init>'),  # 164
    ('DashboardFragment.onLoadFinished', 'DashboardFragment.showTableLayoutUpComingTransactions'),  # 207
    ('DashboardFragment.onLoadFinished', 'DashboardFragment.showTableLayoutTopPayees'),  # 204
    ('DashboardFragment.onLoadFinished', 'DashboardFragment.showTableLayoutTopWithdrawals'),  # 201
    ('DashboardFragment.onLoadFinished', 'DashboardFragment.showChartIncomeVsExpensesCurrentMonth'),  # 198
    ('DashboardFragment.prepareQueryTopWithdrawals', 'Dataset.getSource'),  # 235
    ('DashboardFragment.prepareQueryTopWithdrawals', 'ViewMobileData.<init>'),  # 222
    ('DashboardFragment.prepareQueryTopPayees', 'Dataset.getSource'),  # 262
    ('DashboardFragment.prepareQueryTopPayees', 'ViewMobileData.<init>'),  # 247
    ('DashboardFragment.showChartIncomeVsExpensesCurrentMonth', 'IncomeVsExpensesChartFragment.onResume'),  # 315
    ('DashboardFragment.showChartIncomeVsExpensesCurrentMonth', 'IncomeVsExpensesChartFragment.setChartArguments'),  # 312
    ('DashboardFragment.showChartIncomeVsExpensesCurrentMonth', 'IncomeVsExpensesChartFragment.<init>'),  # 311
    ('DashboardFragment.showChartIncomeVsExpensesCurrentMonth', 'MmxDate.toString'),  # 296
    ('DashboardFragment.showChartIncomeVsExpensesCurrentMonth', 'MmxDate.<init>(int,int,int)'),  # 293
    ('DashboardFragment.showTableLayoutTopWithdrawals', 'DashboardFragment.createTableRow'),  # 348
    ('DashboardFragment.showTableLayoutTopWithdrawals', 'CurrencyService.getCurrencyFormatted'),  # 350
    ('DashboardFragment.showTableLayoutTopWithdrawals', 'CurrencyService.getBaseCurrencyId'),  # 351
    ('DashboardFragment.showTableLayoutTopWithdrawals', 'CurrencyService.<init>'),  # 327
    ('DashboardFragment.showTableLayoutTopPayees', 'DashboardFragment.createTableRow'),  # 380
    ('DashboardFragment.showTableLayoutTopPayees', 'CurrencyService.getCurrencyFormatted'),  # 382
    ('DashboardFragment.showTableLayoutTopPayees', 'CurrencyService.getBaseCurrencyId'),  # 383
    ('DashboardFragment.showTableLayoutTopPayees', 'CurrencyService.<init>'),  # 362
    ('DashboardFragment.showTableLayoutUpComingTransactions', 'QueryBillDeposits.<clinit>'),  # 407
    ('DashboardFragment.showTableLayoutUpComingTransactions', 'UIHelper.resolveAttribute'),  # 421
    ('DashboardFragment.showTableLayoutUpComingTransactions', 'UIHelper.<init>'),  # 418
    ('DashboardFragment.showTableLayoutUpComingTransactions', 'DashboardFragment.createTableRow'),  # 413
    ('DashboardFragment.showTableLayoutUpComingTransactions', 'CurrencyService.getCurrencyFormatted'),  # 414
    ('DashboardFragment.showTableLayoutUpComingTransactions', 'Core.<init>'),  # 397
    ('DashboardFragment.showTableLayoutUpComingTransactions', 'CurrencyService.<init>'),  # 396
    ('DashboardFragment.createTableRow', 'RobotoTextView.<init>(Context,AttributeSet)'),  # 435
)

# ---- UNREACHABLE: DashboardFragment. The class is never constructed in app src/main: no new DashboardFragment, no
# DashboardFragment.class and no class-name string. The only mentions are the declaration (DashboardFragment.java:69) and a
# comment in res/values/arrays.xml:241. The class comment says it is not used (DashboardFragment.java:66-68).
UNREACHABLE['DashboardFragment.<init>'] = ('no_trigger_in_app',
  'implicit default constructor (no explicit constructor in the file). Nothing constructs DashboardFragment in app src/main, so no instance exists',
  'SRC home/DashboardFragment.java:66-69; source grep for DashboardFragment in final_java_only app src/main: declaration (69) and a comment in res/values/arrays.xml:241 only',
  'SOURCE')

UNREACHABLE['DashboardFragment.createTableRow'] = ('no_trigger_in_app',
  'private helper, called only from showTableLayoutTopWithdrawals (348), showTableLayoutTopPayees (380) and showTableLayoutUpComingTransactions (413), which run only from onLoadFinished. No DashboardFragment instance exists',
  'SRC home/DashboardFragment.java:430-457, 348, 380, 413, 201-207; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.loadData'] = ('no_trigger_in_app',
  'public method called only from onResume (117) of this class. The fragment is never constructed, so onResume never runs',
  'SRC home/DashboardFragment.java:129-142, 117; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.onCreate'] = ('no_trigger_in_app',
  'fragment lifecycle override. The framework calls it only on a fragment instance, and none is ever constructed',
  'SRC home/DashboardFragment.java:86-91; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.onCreateLoader'] = ('no_trigger_in_app',
  'LoaderCallbacks override. It runs only for a loader that this fragment starts (loadData, which runs only from onResume), and no fragment exists',
  'SRC home/DashboardFragment.java:144-189, 117; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.onCreateView'] = ('no_trigger_in_app',
  'fragment view creation, called only for a fragment instance. None is ever constructed',
  'SRC home/DashboardFragment.java:93-112; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.onLoadFinished'] = ('no_trigger_in_app',
  'LoaderCallbacks override. It runs only for a loader started by onCreateLoader, which needs a fragment instance',
  'SRC home/DashboardFragment.java:191-210; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.onLoaderReset'] = ('no_trigger_in_app',
  'LoaderCallbacks override. No loader is started for a fragment, because no fragment is ever constructed',
  'SRC home/DashboardFragment.java:212-215; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.onPrepareOptionsMenu'] = ('no_trigger_in_app',
  'options-menu callback of the fragment (menu_dashboard). No fragment instance exists',
  'SRC home/DashboardFragment.java:120-127; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.onResume'] = ('no_trigger_in_app',
  'fragment lifecycle override, called only for an existing fragment. Its call to loadData (117) is an auto CALL record whose caller is UNREACHABLE here, so it is cut with sup (D14a)',
  'SRC home/DashboardFragment.java:114-118, 117; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.prepareQueryTopPayees'] = ('no_trigger_in_app',
  'private query builder, called only from onCreateLoader (177), which is unreachable',
  'SRC home/DashboardFragment.java:245-269, 177; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.prepareQueryTopWithdrawals'] = ('no_trigger_in_app',
  'private query builder, called only from onCreateLoader (173), which is unreachable',
  'SRC home/DashboardFragment.java:220-242, 173; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.showChartIncomeVsExpensesCurrentMonth'] = ('no_trigger_in_app',
  'private, called only from onLoadFinished (198), which is unreachable',
  'SRC home/DashboardFragment.java:274-322, 198; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.showTableLayoutTopPayees'] = ('no_trigger_in_app',
  'private, called only from onLoadFinished (204), which is unreachable',
  'SRC home/DashboardFragment.java:359-391, 204; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.showTableLayoutTopWithdrawals'] = ('no_trigger_in_app',
  'private, called only from onLoadFinished (201), which is unreachable',
  'SRC home/DashboardFragment.java:324-357, 201; source grep (DashboardFragment is never constructed)',
  'SOURCE')

UNREACHABLE['DashboardFragment.showTableLayoutUpComingTransactions'] = ('no_trigger_in_app',
  'private, called only from onLoadFinished (207), which is unreachable',
  'SRC home/DashboardFragment.java:393-428, 207; source grep (DashboardFragment is never constructed)',
  'SOURCE')

# ---- part 077 (2026-10-29)
# ================================================================== batch 077 (label_077): HomeFragment, 40 methods (graphs/MMEX/scratch/batches/batch_077.txt)
# Rows, printed lines and counts: graphs/MMEX/parts/label_077.md. No grep file: every row is REACHABLE, so no library or generated class is UNREACHABLE.
# Edges written here: the framework routes into HomeFragment (commit in MainActivity.initHomeFragment, activity lifecycle super calls, loaders,
# options menu, EventBus register and post, the Icepick reflection helper) and the user taps on the home screen (one new page, S_HOME).
# CALL edges come from auto_calls.json and are not written here (D7).
# The page S_HOME is new: no key for the home screen exists in SCREENS (grep of graph_def.py and parts). Its ENTERS edge belongs to batch 080 (MainActivity).
# UNREACHABLE: none. sup(): none (no auto CALL caller of a method in this batch is UNREACHABLE).

SCREENS.update({'S_HOME': 'The home screen: MainActivity shows HomeFragment with the account list, the + button, the search action, the account row menu and, when no account exists, the welcome view with Settings and Add account'})

# ---- commit in MainActivity.initHomeFragment: the framework runs the fragment lifecycle (MainActivity.java:1312-1322)
e('MainActivity.initHomeFragment', 'HomeFragment.onCreate', 'FRAMEWORK',
  'the fragment transaction commits (MainActivity.java:1320-1322) and the framework runs the fragment lifecycle, starting with onCreate',
  guard='no fragment with the HomeFragment tag is in the manager yet (MainActivity.java:1312-1313)',
  evidence='SRC home/MainActivity.java:1308-1322; SRC home/HomeFragment.java:148-165; INFERRED androidx FragmentManager runs onCreate after the commit (library not read)')

e('MainActivity.initHomeFragment', 'HomeFragment.onCreateView', 'FRAMEWORK',
  'after onCreate the framework inflates the fragment view through onCreateView (commit at MainActivity.java:1320-1322)',
  guard='no fragment with the HomeFragment tag is in the manager yet (MainActivity.java:1312-1313)',
  evidence='SRC home/MainActivity.java:1308-1322; SRC home/HomeFragment.java:167-170; INFERRED androidx FragmentManager (library not read)')

e('HomeFragment.onCreateView', 'HomeFragment.onViewCreated', 'FRAMEWORK',
  'the framework calls onViewCreated once onCreateView has returned the view',
  evidence='SRC home/HomeFragment.java:167-196, 198-203; INFERRED androidx Fragment lifecycle (library not read)')

e('HomeFragment.onCreate', 'HomeFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'setHasOptionsMenu(true) (HomeFragment.java:158) makes the framework call onCreateOptionsMenu when the activity builds its options menu',
  evidence='SRC home/HomeFragment.java:158, 354-358; INFERRED androidx options menu dispatch (library not read); pattern label_073.py (PayeeListFragment.onActivityCreated to onCreateOptionsMenu)')

# ---- activity lifecycle: the super calls in MainActivity dispatch to the fragments
e('MainActivity.onStart', 'HomeFragment.onStart', 'FRAMEWORK',
  'MainActivity.onStart calls super.onStart (MainActivity.java:249) and the framework dispatches onStart to the fragments in the manager',
  evidence='SRC home/MainActivity.java:247-249; SRC home/HomeFragment.java:205-210; INFERRED androidx FragmentActivity dispatch (library not read); pattern graph_def.py:2071 (SearchActivity.onResume to AllDataListFragment.onResume)')

e('MainActivity.onResume', 'HomeFragment.onResume', 'FRAMEWORK',
  'super.onResume (MainActivity.java:273, inside try 272-276) dispatches onResume to the fragments',
  evidence='SRC home/MainActivity.java:271-276; SRC home/HomeFragment.java:378-401; INFERRED androidx FragmentActivity dispatch (library not read); pattern graph_def.py:2071')

e('MainActivity.onSaveInstanceState', 'HomeFragment.onSaveInstanceState', 'FRAMEWORK',
  'super.onSaveInstanceState (MainActivity.java:427) makes the framework save the fragment state through onSaveInstanceState',
  evidence='SRC home/MainActivity.java:423-428; SRC home/HomeFragment.java:482-486; INFERRED androidx FragmentManager saves fragment state (library not read)')

e('HomeFragment.onResume', 'HomeFragment.onStop', 'LIFECYCLE',
  'the user leaves the screen: the framework stops the fragment after it has resumed (same pattern as label_010.py:43)',
  evidence='SRC home/HomeFragment.java:212-217, 378-401; INFERRED androidx Fragment lifecycle (library not read)')

# ---- EventBus: register in onStart, delivery from the balance dialog
e('HomeFragment.onStart', 'HomeFragment.onEvent', 'REGISTER',
  'EventBus.register(this) in onStart (line 209) subscribes the @Subscribe onEvent(AmountEnteredEvent) method until onStop unregisters it',
  evidence='SRC home/HomeFragment.java:205-217, 490-491; pattern label_010.py:57 (AccountTransactionListFragment.onStart to onEvent, REGISTER)')

e('AmountInputDialog$7.onClick', 'HomeFragment.onEvent', 'ASYNC',
  'the OK button of the balance dialog posts AmountEnteredEvent (AmountInputDialog.java:260); EventBus delivers it to HomeFragment only while the fragment is registered (onStart to onStop)',
  guard='evalExpression() returns true (AmountInputDialog.java:258)',
  evidence='SRC common/AmountInputDialog.java:255-263; SRC home/HomeFragment.java:490-491, 205-217; pattern graph_def.py:4623 (CurrencyUIFeatures$3.onClick to onEvent, ASYNC)')

# ---- loaders: startLoaders restarts the two loaders; the framework calls the callbacks
e('HomeFragment.startLoaders', 'HomeFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader(LOADER_ACCOUNT_BILLS) and restartLoader(LOADER_INCOME_EXPENSES) (HomeFragment.java:535-536) make the LoaderManager call onCreateLoader',
  evidence='SRC home/HomeFragment.java:531-537; INFERRED androidx LoaderManager (library not read); pattern label_073.py:32-34')

e('HomeFragment.startLoaders', 'HomeFragment.onLoaderReset', 'FRAMEWORK',
  'the restart destroys the previous loader, which calls onLoaderReset on the callbacks (HomeFragment.java:535-536)',
  evidence='SRC home/HomeFragment.java:535-536; INFERRED androidx LoaderManager (library not read); pattern label_073.py:36-38')

e('HomeFragment.onCreateLoader', 'HomeFragment.onLoadFinished', 'FRAMEWORK',
  'the loader delivers its cursor to onLoadFinished when the load completes',
  evidence='SRC home/HomeFragment.java:222-273, 287-288; INFERRED androidx Loader delivery (library not read); pattern label_073.py:27-29')

# ---- Icepick: the library loads the generated helper HomeFragment$$Icepick by reflection (not in the dataset)
e('HomeFragment.onCreate', 'HomeFragment$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State field: the library loads the generated helper by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at HomeFragment.java:163)',
  guard='savedInstanceState is not null (HomeFragment.java:161)',
  evidence='SRC home/HomeFragment.java:144, 161-164; the icepick library and the generated class are not in the dataset: INFERRED, source not read; pattern label_006.py:114-116')

e('HomeFragment.onCreate', 'HomeFragment$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at HomeFragment.java:163)',
  guard='savedInstanceState is not null (HomeFragment.java:161)',
  evidence='SRC home/HomeFragment.java:144, 161-164; the icepick library is not in the dataset: INFERRED, source not read; pattern label_006.py:118-120')

e('HomeFragment.onCreate', 'HomeFragment$$Icepick.restore', 'FRAMEWORK',
  'Icepick calls the generated restore for the @State field accountBalancedId',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at HomeFragment.java:163)',
  guard='savedInstanceState is not null (HomeFragment.java:161)',
  evidence='SRC home/HomeFragment.java:144, 161-164; the icepick library is not in the dataset: INFERRED, source not read; pattern label_006.py:122-124')

e('HomeFragment.onSaveInstanceState', 'HomeFragment$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick saves the @State field: the library loads the generated helper by reflection, which runs its static initialiser first if onCreate did not',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at HomeFragment.java:485)',
  evidence='SRC home/HomeFragment.java:144, 482-486; the icepick library is not in the dataset: INFERRED, source not read')

e('HomeFragment.onSaveInstanceState', 'HomeFragment$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection for the save',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at HomeFragment.java:485)',
  evidence='SRC home/HomeFragment.java:144, 482-486; the icepick library is not in the dataset: INFERRED, source not read')

e('HomeFragment.onSaveInstanceState', 'HomeFragment$$Icepick.save', 'FRAMEWORK',
  'Icepick calls the generated save for the @State field accountBalancedId',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at HomeFragment.java:485)',
  evidence='SRC home/HomeFragment.java:144, 482-486; the icepick library is not in the dataset: INFERRED, source not read; pattern label_006.py:126-134')

# ---- GUI edges from the one home screen S_HOME (MainActivity shows HomeFragment; its ENTERS edge is written by batch 080)
gui('S_HOME', 'HomeFragment.onOptionsItemSelected',
    'Tap the search action (menu_search) in the options menu of the home screen',
    evidence='SRC res/menu/home_menu.xml:18-28; SRC home/HomeFragment.java:360-365 (menu_search check at 364, startActivity SearchActivity at 365)')

gui('S_HOME', 'HomeFragment.onCreateContextMenu',
    'Long-press an account row in the account list (the list is registered for the context menu at line 735)',
    evidence='SRC home/HomeFragment.java:409-412, 735; INFERRED long-press on a registered view opens its context menu (Android source not read); pattern label_073.py:67-69')

gui('S_HOME', 'HomeFragment.onContextItemSelected',
    'Tap Edit, Balance account or Portfolio in the menu of an account row',
    evidence='SRC home/HomeFragment.java:450-478 (Edit 462, balance 470, portfolio 473); INFERRED the framework dispatches the chosen item to the fragment (library not read); pattern label_073.py:71-73')

gui('S_HOME', 'HomeFragment$1.onClick',
    'Tap the + floating action button at the bottom of the home screen',
    evidence='SRC res/layout/home_fragment.xml:153-165 (live fab; 167-178 commented out); SRC home/HomeFragment.java:184-193')

gui('S_HOME', 'HomeFragment$2.onClick',
    'Tap Settings in the welcome view, which is shown only when the account list is empty',
    needs_state=state_text('the account list is empty, so the welcome view with the Settings button is shown (HomeFragment.java:793-794)', ('account',)),
    evidence='SRC res/layout/welcome_layout.xml:101 (buttonSettings); SRC res/layout/home_fragment.xml:181-184; SRC home/HomeFragment.java:590-602, 792-794')

# ---- part 079 (2026-10-29)
# ================================================================== batch 079 (label_079): com.money.manager.ex.home HomeFragment_MembersInjector
# (Dagger-generated, 4 methods: graphs/MMEX/scratch/batches/batch_079.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_079.md (1 REACHABLE, 3 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_079.grep.txt (sections 1-8).
# This file writes:
#   - 2 sup pairs (D14a): the auto CALL records of the UNREACHABLE create (to its constructor, HomeFragment_MembersInjector.java:23)
#     and of the UNREACHABLE injectMembers (to injectInfoRepositorySqlLazy, HomeFragment_MembersInjector.java:28);
#   - 3 UNREACHABLE entries: <init>, create, injectMembers (no_trigger_in_app, INFERRED from the generated class file).
# Not written: no e() or gui() edges (no destination owned by this batch needs one). The REACHABLE row for
#   injectInfoRepositorySqlLazy rests on the auto CALL record DaggerMmxComponent.injectHomeFragment -> injectInfoRepositorySqlLazy
#   (DaggerMmxComponent.java:458, D7). No CALL edges.

sup(('HomeFragment_MembersInjector.create', 'HomeFragment_MembersInjector.<init>'),
    ('HomeFragment_MembersInjector.injectMembers', 'HomeFragment_MembersInjector.injectInfoRepositorySqlLazy'))

# ================================================================== UNREACHABLE (batch 079). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['HomeFragment_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (the generated class is in build/intermediates, label_079.grep.txt section 5). Its only caller record is create, and create has no caller: no class file names create, and the component refers only to injectInfoRepositorySqlLazy. The app source has no reference to the class (section 1).',
  'python-printed auto_calls record HomeFragment_MembersInjector.java:23 (label_079.grep.txt section 6); class-file parse of HomeFragment_MembersInjector.class and DaggerMmxComponent.class (sections 3, 5); label_079.grep.txt section 1',
  'INFERRED')

UNREACHABLE['HomeFragment_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory. No caller: no class file references create (sections 3, 5). The component calls the static injectX method directly (DaggerMmxComponent.injectHomeFragment, DaggerMmxComponent.java:458), not create. No app source reference (section 1).',
  'class-file parse (label_079.grep.txt sections 3, 5); python-printed auto_calls query, no record with create as dst (section 6); label_079.grep.txt section 1',
  'INFERRED')

UNREACHABLE['HomeFragment_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (HomeFragment-typed). No caller: the component refers only to injectInfoRepositorySqlLazy (section 5), and no other class file names the injector (section 3). Its only outgoing record is injectMembers -> injectInfoRepositorySqlLazy, cut by the sup pair above.',
  'python-printed auto_calls record HomeFragment_MembersInjector.java:28 (section 6); class-file parse (sections 3, 5); label_044.grep.txt line 670 (the component calls the static injectInfoRepositorySqlLazy, not injectMembers)',
  'INFERRED')

# ---- part 078 (2026-10-29)
# ================================================================== batch 078 (label_078): HomeFragment$3 to HomeFragment$8,
# 13 methods (graphs/MMEX/scratch/batches/batch_078.txt): $3 (onClick), $4 (onSuccess, onError), $5 (call), $6 (onChildClick),
# $7 (onGroupCollapse), $8 (onGroupExpand), and the six <init> methods.
# Rows, printed lines and counts: graphs/MMEX/parts/label_078.md. Result: 13 REACHABLE, 0 UNREACHABLE.
# This file writes:
#   - 4 gui() edges from the home page S_HOME (defined by batch 077, label_077.py line 9; not redefined here):
#     the add account button, an account row tap, and the group header taps (collapse and expand),
#   - 3 e() edges from HomeFragment.loadUsername (batch 077) into the RxJava 1 callbacks: Callable.call, onSuccess, onError
#     (cls='non_standard', the library dispatches them).
# The six <init> methods are auto CALL records (auto_calls.json), so no edge is written for them (D7).
# The INTENT edge from HomeFragment$3.onClick to AccountEditActivity.<init> is written by batch 006 (label_006.py), not here.
# No sup pairs (no UNREACHABLE caller). No UNREACHABLE entries. No grep file (no library or generated class is UNREACHABLE).
# No new named constants: the gate texts are inline state_text(...) calls (D2).

# ---- GUI edges from the home page S_HOME (MainActivity shows HomeFragment; its ENTERS edge is written by batch 080)

gui('S_HOME', 'HomeFragment$3.onClick',
    'Tap Add account (buttonAddAccount) on the welcome view; the welcome view is shown only when the account list is empty',
    needs_state=state_text('the account list is empty, so the welcome view with the Add account button is shown (HomeFragment.java:793-794)', ('account',)),
    evidence='SRC home/HomeFragment.java:612-622 (button 612, listener 614, onClick 617-621); SRC res/layout/welcome_layout.xml:65-66; SRC res/layout/home_fragment.xml:181-184; SRC home/HomeFragment.java:792-794 (visibility)')

gui('S_HOME', 'HomeFragment$6.onChildClick',
    'Tap an account row (a child row) in the account list, which is shown only when at least one account exists',
    needs_state=state_text('at least one account exists, so the account list shows rows (HomeFragment.java:793), and the row group is expanded (group expansion is saved in settings, HomeFragment.java:719 and 731)', ('account', 'settings')),
    evidence='SRC home/HomeFragment.java:686-706 (onChildClick, event post 704), 792-794, 877-878 (listViewAccountBills); INFERRED the expandable list calls the child-click listener on a row tap (Android library not read)')

gui('S_HOME', 'HomeFragment$7.onGroupCollapse',
    'Tap an expanded account-type group header (the group title row) to collapse it',
    needs_state=state_text('at least one account exists, so the group headers are shown (HomeFragment.java:793), and the group is expanded (its saved setting is true, HomeFragment.java:754)', ('account', 'settings')),
    evidence='SRC home/HomeFragment.java:710-719 (listener 710, body 716-719), 747-760 (saved flag read at 754), 792-794; INFERRED the expandable list calls the collapse listener on a header tap (Android library not read)')

gui('S_HOME', 'HomeFragment$8.onGroupExpand',
    'Tap a collapsed account-type group header (the group title row) to expand it',
    needs_state=state_text('at least one account exists, so the group headers are shown (HomeFragment.java:793), and the group is collapsed (its saved setting is false, HomeFragment.java:719)', ('account', 'settings')),
    evidence='SRC home/HomeFragment.java:722-731 (listener 722, body 726-731), 747-760, 792-794; INFERRED the expandable list calls the expand listener on a header tap (Android library not read)')

# ---- RxJava 1 callbacks of the username load: loadUsername subscribes the Single (line 649); the library runs the callables

e('HomeFragment.loadUsername', 'HomeFragment$5.call', 'CALL',
  'RxJava 1 runs the Callable on the io thread once loadUsername subscribes the Single (subscribeOn at line 647); the body opens InfoService and reads the user name (lines 643-644)',
  cls='non_standard',
  via='RxJava 1 (library, INFERRED, not read): Single.fromCallable(Callable) runs Callable.call when subscribed on Schedulers.io() (subscribeOn at HomeFragment.java:647)',
  evidence='SRC home/HomeFragment.java:638-662 (fromCallable 640, call 642-645, subscribeOn 647, subscribe 649); auto_calls records HomeFragment$5.call -> InfoService.<init> (line 643), InfoService.getInfoValue (line 644); the RxJava library is not in the dataset (INFERRED)')

e('HomeFragment.loadUsername', 'HomeFragment$4.onSuccess', 'CALL',
  'RxJava 1 delivers the value returned by call to SingleSubscriber.onSuccess on the main thread (observeOn at line 648); the body sets the user name and posts UsernameLoadedEvent (lines 652-653)',
  guard='call() returns normally: it does unless the InfoService constructor throws (InfoService.java:45-48, outside the try at line 112); getInfoValue returns null or a value when a database read fails, because its catch (line 123) does not rethrow',
  cls='non_standard',
  via='RxJava 1 (library, INFERRED, not read): SingleSubscriber.onSuccess is delivered after observeOn(AndroidSchedulers.mainThread()) (HomeFragment.java:648-649)',
  evidence='SRC home/HomeFragment.java:638-662 (observeOn 648, subscribe 649, onSuccess 651-653); SRC servicelayer/InfoService.java:112-123 (getInfoValue catches Exception and returns ret); auto_calls record HomeFragment$4.onSuccess -> UsernameLoadedEvent.<init> (line 653)')

e('HomeFragment.loadUsername', 'HomeFragment$4.onError', 'CALL',
  'RxJava 1 delivers an exception thrown by Callable.call to SingleSubscriber.onError on the main thread; the body logs it with Timber (line 658)',
  guard='call() throws: only when the InfoService constructor throws (new InfoService at line 643; the constructor at InfoService.java:45-48 has no try). getInfoValue catches its own exceptions (InfoService.java:123), so a database failure reaches onSuccess instead',
  cls='non_standard',
  via='RxJava 1 (library, INFERRED, not read): SingleSubscriber.onError delivers the exception thrown by Callable.call (HomeFragment.java:640-645, 657-658)',
  evidence='SRC home/HomeFragment.java:638-662 (onError 657-659, Timber.e 658); SRC servicelayer/InfoService.java:45-48, 112-123; auto_calls record HomeFragment$4.onError -> Timber.e')

# ---- part 082 (2026-10-29)
# ================================================================== batch 082 (label_082): MainActivity$4.onChildClick, MainActivity$4$1.<init>, MainActivity$4$1.run (graphs/MMEX/scratch/batches/batch_082.txt)
# Rows, printed lines and counts: graphs/MMEX/parts/label_082.md. No grep file: every row is REACHABLE, so no library or generated class is UNREACHABLE.
# Edges written here: the tap on a child row of the navigation drawer (GUI, from the home screen S_HOME, defined in label_077.py and reused here: no new SCREENS key) and the Handler.postDelayed runnable (FRAMEWORK).
# CALL edges come from auto_calls.json and are not written here (D7): MainActivity$4.onChildClick -> MainActivity$4$1.<init> (MainActivity.java:975) and MainActivity$4$1.run -> MainActivity.onDrawerMenuAndOptionMenuSelected (MainActivity.java:978).
# The listener is installed by createExpandableDrawer (batch 080, MainActivity.java:965), and that runs only after initializeDrawer finds the drawer (batch 080, MainActivity.java:1291-1301). Those edges are batch 080's and are not written here.
# UNREACHABLE: none. sup(): none (no auto CALL caller of a method in this batch is UNREACHABLE).

# ---- user action: a tap on a child row of the navigation drawer, opened from the home screen (MainActivity shows HomeFragment first, MainActivity.java:238, then initializeDrawer at 240)

gui('S_HOME', 'MainActivity$4.onChildClick',
    'Open the navigation drawer, expand a group with child rows (for example Accounts in the Entities group) and tap a child row',
    guard='the drawer exists: initializeDrawer finds drawerLayout (MainActivity.java:1291-1294) and createExpandableDrawer installs this listener (line 965); onChildClick returns false when mDrawer is null (line 968)',
    evidence='SRC home/MainActivity.java:965-968, 1289-1301, 238-240, 862-868; SRC res/layout/main_activity.xml:18-21, 46; SRC res/layout/merge_drawer.xml:72-76; INFERRED ExpandableListView calls OnChildClickListener on a child-row tap (ExpandableListView not in fw_src, not read); INFERRED DrawerLayout opens the drawer (androidx not read)')

# ---- the runnable that onChildClick posts with a 200 ms delay; the framework runs run() when the delay ends (the same pattern as label_041.py)

e('MainActivity$4.onChildClick', 'MainActivity$4$1.run', 'FRAMEWORK',
  'onChildClick posts the Runnable to a new Handler with a 200 ms delay (postDelayed); the framework runs run() when the delay ends, and run() calls onDrawerMenuAndOptionMenuSelected (auto CALL, line 978)',
  guard='selectedItem is not null (MainActivity.java:974)',
  evidence='SRC home/MainActivity.java:973-980; FW-SRC core/java/android/os/Handler.java:427-429 (postDelayed calls sendMessageDelayed), 596 (sendMessageDelayed), 97-99 (dispatchMessage calls handleCallback), 789-790 (handleCallback runs message.callback.run())')

# ---- part 081 (2026-10-29)
# ================================================================== batch 081 (label_081): MainActivity, 40 methods (graphs/MMEX/scratch/batches/batch_081.txt)
# Rows, printed lines and counts: graphs/MMEX/parts/label_081.md. No grep file: every row is REACHABLE, so no library or generated class is UNREACHABLE.
# Edges written here: the activity lifecycle into MainActivity (onStart, onResume, onSaveInstanceState, onPostCreate), the Menu key, the Up button and the drawer taps on the home screen S_HOME (gui), the two RxJava sync Callables (CALL, cls=non_standard) and the drawer Runnable (FRAMEWORK, postDelayed), and the Icepick reflection helper (cls=non_standard).
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

# ---- part 084 (2026-10-29)
# ================================================================== batch 084 (label_084): SelectDatabaseActivity_MembersInjector (4 methods), SelectDatabaseActivity_ViewBinding (7 methods: its two constructors, unbind, and the listener classes $1 and $2 with their constructors and doClick), and the 7 home event classes (one constructor each). 18 methods in all (graphs/MMEX/scratch/batches/batch_084.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_084.md (12 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_084.grep.txt (sections 1-6).
# This file writes:
#   - 1 SCREENS key: S_SELECT_DATABASE (new; see Open points in label_084.md);
#   - 1 CALL edge (cls non_standard): SelectDatabaseActivity.onCreate to the ButterKnife binding constructor (ButterKnife.bind(this), SelectDatabaseActivity.java:60; not in auto_calls.json);
#   - 2 GUI edges (cls non_standard): S_SELECT_DATABASE to $1.doClick (Create database button) and $2.doClick (Open database button);
#   - 2 sup pairs (D14a): the auto CALL records of the UNREACHABLE create (to its constructor) and of the UNREACHABLE injectMembers (to injectMDatabasesLazy);
#   - 6 UNREACHABLE entries: MembersInjector.<init>, create, injectMembers (generated, INFERRED); ViewBinding.unbind (generated, INFERRED); MessageEvent.<init> and RequestOpenDatabaseEvent.<init> (app source, SOURCE).
# Not written: the ENTERS edge into S_SELECT_DATABASE (batch 083 owns SelectDatabaseActivity.onCreate). No CALL edges from auto_calls.json (D7). Routes through batches 080, 081 and 083 stay REACHABLE with the owner named (D8).

SCREENS.update({'S_SELECT_DATABASE': 'The database chooser (SelectDatabaseActivity), shown when no valid database is open: the Create database button (createDatabaseButton) and the Open database button (openDatabaseButton)'})

# ---- ButterKnife binding of SelectDatabaseActivity: the generated binding is built by reflection in ButterKnife.bind(this) (generated class not in the source root: INFERRED)

e('SelectDatabaseActivity.onCreate', 'SelectDatabaseActivity_ViewBinding.<init>(SelectDatabaseActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for the activity, which binds the @OnClick handlers and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated SelectDatabaseActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC home/SelectDatabaseActivity.java:53-60 (ButterKnife.bind(this) at 60; the return value is not kept); INFERRED ButterKnife generated binding (label_084.grep.txt sections 2, 5: the generated class is in build/intermediates, not in the source root)')

# ---- GUI edges from the database chooser page S_SELECT_DATABASE (the two buttons; ButterKnife @OnClick listeners: INFERRED)

e('S_SELECT_DATABASE', 'SelectDatabaseActivity_ViewBinding$1.doClick', 'GUI',
  'tap the Create database button: the @OnClick listener of the generated binding calls onCreateDatabaseClick, which starts PasswordActivity and then the create-file picker',
  gui=['Tap the Create database button (createDatabaseButton)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC home/SelectDatabaseActivity.java:99-103 (@OnClick(R.id.createDatabaseButton) at 99; onCreateDatabaseClick 100-103, startActivity at 101, showCreateFilePicker at 103); SRC res/layout/activity_select_database.xml:62-65 (createDatabaseButton at 62); auto_calls.json record (file SelectDatabaseActivity_ViewBinding.java:38) SelectDatabaseActivity_ViewBinding$1.doClick -> SelectDatabaseActivity.onCreateDatabaseClick; INFERRED ButterKnife listener')

e('S_SELECT_DATABASE', 'SelectDatabaseActivity_ViewBinding$2.doClick', 'GUI',
  'tap the Open database button: the @OnClick listener of the generated binding calls onOpenDatabaseClick, which starts PasswordActivity (the open path)',
  gui=['Tap the Open database button (openDatabaseButton)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC home/SelectDatabaseActivity.java:106-108 (@OnClick(R.id.openDatabaseButton) at 106; onOpenDatabaseClick 107-108, startActivity at 108); SRC res/layout/activity_select_database.xml:80-83 (openDatabaseButton at 80); auto_calls.json record (file SelectDatabaseActivity_ViewBinding.java:46) SelectDatabaseActivity_ViewBinding$2.doClick -> SelectDatabaseActivity.onOpenDatabaseClick; INFERRED ButterKnife listener')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE

sup(('SelectDatabaseActivity_MembersInjector.create', 'SelectDatabaseActivity_MembersInjector.<init>'),
    ('SelectDatabaseActivity_MembersInjector.injectMembers', 'SelectDatabaseActivity_MembersInjector.injectMDatabasesLazy'))

# ================================================================== UNREACHABLE (batch 084). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['SelectDatabaseActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (the generated class is in build/intermediates, label_084.grep.txt section 4). Its only caller record is create, and create has no caller: no class file names create, and the component refers only to injectMDatabasesLazy. The app source has no reference to the class (section 1).',
  'python-printed auto_calls record SelectDatabaseActivity_MembersInjector.java:24 (label_084.grep.txt section 5); class-file parse of SelectDatabaseActivity_MembersInjector.class and DaggerMmxComponent.class (sections 3, 4); label_084.grep.txt section 1',
  'INFERRED')

UNREACHABLE['SelectDatabaseActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory. No caller: no class file references create (sections 3, 4). The component calls the static injectMDatabasesLazy directly (DaggerMmxComponent.injectSelectDatabaseActivity, DaggerMmxComponent.java:426), not create. No app source reference (section 1).',
  'class-file parse (label_084.grep.txt sections 3, 4); python-printed auto_calls record DaggerMmxComponent.java:426 (section 5); label_084.grep.txt section 1',
  'INFERRED')

UNREACHABLE['SelectDatabaseActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (SelectDatabaseActivity-typed). No caller: the component refers only to injectMDatabasesLazy (section 4), and no other class file names the injector (section 3). Its only outgoing record, injectMembers -> injectMDatabasesLazy, is cut by the sup pair above. The synthetic bridge injectMembers(Object) is not in this batch (open point in label_084.md).',
  'python-printed auto_calls record SelectDatabaseActivity_MembersInjector.java:29 (section 5); class-file parse (sections 3, 4); label_084.grep.txt section 1',
  'INFERRED')

UNREACHABLE['SelectDatabaseActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root). ButterKnife.bind(this) at SelectDatabaseActivity.java:60 discards the returned Unbinder, SelectDatabaseActivity has no onDestroy (section 2), and no class file references unbind (0 references, section 4). No Unbinder reference exists in the app source (section 1).',
  'SRC home/SelectDatabaseActivity.java:60; label_084.grep.txt sections 1, 2, 4; python-printed auto_calls check (no record with unbind as dst, section 5)',
  'INFERRED')

UNREACHABLE['MessageEvent.<init>'] = ('no_trigger_in_app',
  'Event class with only the implicit default constructor and no body (MessageEvent.java:22-23). No app source constructs it (section 1: the class name appears only in its own file), and no class file calls MessageEvent.<init> (section 4). With no construction site, no EventBus post can deliver it.',
  'SRC home/events/MessageEvent.java:22-23; label_084.grep.txt sections 1, 4, 5',
  'SOURCE')

UNREACHABLE['RequestOpenDatabaseEvent.<init>'] = ('no_trigger_in_app',
  'Event class with only the implicit default constructor and no body (RequestOpenDatabaseEvent.java:22-23). No app source constructs it (section 1: the class name appears in its own file, the import at MainActivity.java:86, and the subscriber at MainActivity.java:470), and no class file calls RequestOpenDatabaseEvent.<init> (sections 3, 4). The subscriber MainActivity.onEvent(RequestOpenDatabaseEvent) therefore has no post site in the app (open point in label_084.md).',
  'SRC home/events/RequestOpenDatabaseEvent.java:22-23; SRC home/MainActivity.java:86, 469-472; label_084.grep.txt sections 1, 3, 4',
  'SOURCE')

# ---- part 080 (2026-10-29)
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

# ---- part 083 (2026-10-29)
# ================================================================== batch 083 (label_083): 6 classes, 38 methods
# (graphs/MMEX/scratch/batches/batch_083.txt): MainActivity_MembersInjector (4, Dagger-generated),
# MyActionBarDrawerToggle (4), RecentDatabaseEntryComparator (2), RecentDatabasesProvider (18, including $1.<init>),
# RecentDatabasesProvider_Factory (3, Dagger-generated), SelectDatabaseActivity (7).
# Rows, printed lines and counts: graphs/MMEX/parts/label_083.md (32 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_083.grep.txt (sections 1-4).
# This file writes:
#   - 1 SCREENS key: S_SELECT_DATABASE (new; no S_SELECT* key exists in graph_def.py or other parts; see Open points in label_083.md);
#   - 8 e() edges: 1 INTENT, 1 LIFECYCLE, 1 ENTERS, 3 FRAMEWORK (two picker results, one permission request),
#     and 2 non_standard CALL edges for the Dagger Lazy<RecentDatabasesProvider>.get hop into
#     RecentDatabasesProvider_Factory.get (from MainActivity.getDatabases and MainActivity.changeDatabase);
#   - 4 gui() edges: S_SELECT_DATABASE to the two @OnClick handlers, S_HOME to the two drawer-toggle callbacks;
#   - 3 sup() pairs (D14a): auto CALL records whose caller is UNREACHABLE (create -> <init>, injectMembers -> injectMDatabases,
#     compare -> DatabaseMetadata.isSynchronised);
#   - 6 UNREACHABLE entries (no_trigger_in_app).
# No other CALL edges: the other REACHABLE rows rest on auto_calls.json records (D7).
# Edges whose destination is owned by another batch (PasswordActivity INTENT edges, MainActivity.onCreate and similar) are not written here (D1).

SCREENS.update({'S_SELECT_DATABASE': 'The database chooser (SelectDatabaseActivity): the create-database button (createDatabaseButton) and the open-database button (openDatabaseButton); shown when no valid database is set (MainActivity.showPrerequisite) or when a database change fails (MainActivity.changeDatabase)'})

# ---- INTENT / LIFECYCLE / ENTERS: the chooser page
e('MainActivity.showSelectDatabaseActivity', 'SelectDatabaseActivity.<init>', 'INTENT',
  'new Intent(this, SelectDatabaseActivity.class) with FLAG_ACTIVITY_CLEAR_TOP, then startActivity (MainActivity.java:1503-1506)',
  evidence='SRC MainActivity.java:1486-1487 (showPrerequisite, branch taken when isDatabaseAvailable is false), 1503-1506; auto CALL changeDatabase -> showSelectDatabaseActivity at MainActivity.java:554; AndroidManifest.xml:368 (no intent-filter, explicit intent only); label_083.grep.txt sections 1, 4')

e('SelectDatabaseActivity.<init>', 'SelectDatabaseActivity.onCreate', 'LIFECYCLE',
  'Framework creates the activity (implicit constructor) and calls onCreate (SelectDatabaseActivity.java:54)',
  evidence='SRC SelectDatabaseActivity.java:46-54 (onCreate at 54); INFERRED LIFECYCLE from the implicit constructor to onCreate (framework activity lifecycle; the framework source is not read)')

e('SelectDatabaseActivity.onCreate', 'S_SELECT_DATABASE', 'ENTERS',
  'setContentView(R.layout.activity_select_database) shows the chooser (SelectDatabaseActivity.java:56)',
  evidence='SRC SelectDatabaseActivity.java:56; res/layout/activity_select_database.xml:62 and 80 (the two buttons)')

# ---- FRAMEWORK: picker results and permission result
e('SelectDatabaseActivity.onOpenDatabaseClick', 'SelectDatabaseActivity.onActivityResult', 'FRAMEWORK',
  'FileStorageHelper.showStorageFilePicker starts the document picker with startActivityForResult (request code RequestCodes.SELECT_DOCUMENT); the framework returns the result to onActivityResult',
  evidence='SRC SelectDatabaseActivity.java:106-111 (showStorageFilePicker at 110); core/docstorage/FileStorageHelper.java:56-65 (startActivityForResult at 65, SELECT_DOCUMENT at 58) under final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/')

e('SelectDatabaseActivity.onCreateDatabaseClick', 'SelectDatabaseActivity.onActivityResult', 'FRAMEWORK',
  'FileStorageHelper.showCreateFilePicker starts the create-document picker with startActivityForResult (request code RequestCodes.CREATE_DOCUMENT); the framework returns the result to onActivityResult',
  evidence='SRC SelectDatabaseActivity.java:99-104 (showCreateFilePicker at 103); core/docstorage/FileStorageHelper.java:74-83 (startActivityForResult at 83, CREATE_DOCUMENT at 76)')

e('SelectDatabaseActivity.onCreate', 'SelectDatabaseActivity.onRequestPermissionsResult', 'FRAMEWORK',
  'requestExternalStoragePermissions(this) (SelectDatabaseActivity.java:64) asks for the storage permissions when not yet granted; the framework returns the answer to onRequestPermissionsResult',
  evidence='SRC SelectDatabaseActivity.java:63-64; utils/MmxFileUtils.java:140-154 (requestExternalStoragePermissions), 156-165 (ActivityCompat.requestPermissions at 162, only when the permission is not granted, line 160)')

# ---- non_standard CALL: Dagger Lazy<RecentDatabasesProvider>.get runs RecentDatabasesProvider_Factory.get (label_036 pattern)
e('MainActivity.getDatabases', 'RecentDatabasesProvider_Factory.get', 'CALL',
  'mDatabases.get() (Dagger Lazy<RecentDatabasesProvider> injected into the field at MainActivity.java:157) runs the factory provider RecentDatabasesProvider_Factory.get on first use',
  cls='non_standard',
  via='dagger.Lazy.get: DoubleCheck calls the Provider (javax.inject.Provider.get bridge get()Object, flags 0x1041, then get()RecentDatabasesProvider). Library behaviour, INFERRED; library code not read',
  evidence='INFERRED MainActivity.java:157 (field), 1043 (mDatabases.get()); label_083.grep.txt section 3 (Factory class parse: appProvider field and get methods); label_036 pattern')

e('MainActivity.changeDatabase', 'RecentDatabasesProvider_Factory.get', 'CALL',
  'mDatabases.get().get(database.localPath) (MainActivity.java:538) calls the same Lazy, which runs RecentDatabasesProvider_Factory.get on first use',
  cls='non_standard',
  via='dagger.Lazy.get as in the getDatabases edge above (library behaviour, INFERRED)',
  evidence='INFERRED MainActivity.java:157, 538; label_083.grep.txt section 3')

# ---- GUI: page to method (S_SELECT_DATABASE and S_HOME are the pages)
gui('S_SELECT_DATABASE', 'SelectDatabaseActivity.onCreateDatabaseClick',
    'Tap the create-database button (createDatabaseButton, activity_select_database.xml:62); ButterKnife binds it through SelectDatabaseActivity_ViewBinding$1.doClick (generated, auto_calls record SelectDatabaseActivity_ViewBinding.java:38)',
    evidence='SRC SelectDatabaseActivity.java:99-100 (@OnClick(R.id.createDatabaseButton)); res/layout/activity_select_database.xml:62; label_083.grep.txt section 4')

gui('S_SELECT_DATABASE', 'SelectDatabaseActivity.onOpenDatabaseClick',
    'Tap the open-database button (openDatabaseButton, activity_select_database.xml:80); bound through SelectDatabaseActivity_ViewBinding$2.doClick (generated, auto_calls record SelectDatabaseActivity_ViewBinding.java:46)',
    evidence='SRC SelectDatabaseActivity.java:106-107 (@OnClick(R.id.openDatabaseButton)); res/layout/activity_select_database.xml:80; label_083.grep.txt section 4')

gui('S_HOME', 'MyActionBarDrawerToggle.onDrawerOpened',
    'The navigation drawer opens: the home icon (MainActivity.onOptionsItemSelected, openDrawer at MainActivity.java:395, batch 081) or MainActivity.onKeyDown (openDrawer at MainActivity.java:413, batch 081). The DrawerLayout calls the listener, which initializeDrawer adds at MainActivity.java:1297 (batch 080)',
    evidence='SRC MyActionBarDrawerToggle.java:42-45; MainActivity.java:395, 413 (batch 081); MainActivity.java:1296-1297 (batch 080); S_HOME is the page the drawer is shown on (graph_def.py SCREENS)')

gui('S_HOME', 'MyActionBarDrawerToggle.onDrawerClosed',
    'The navigation drawer closes: back press (MainActivity.onBackPressed, closeDrawer at MainActivity.java:442, batch 080), a drawer item tap (closeDrawer at MainActivity.java:948 and 970, batch 080), or MainActivity.onKeyDown (closeDrawer at MainActivity.java:411, batch 081)',
    evidence='SRC MyActionBarDrawerToggle.java:47-50; MainActivity.java:442, 948, 970 (batch 080); MainActivity.java:411 (batch 081); listener added at MainActivity.java:1297')

# ---- sup(): auto CALL records whose caller is UNREACHABLE (D14a)
sup(('MainActivity_MembersInjector.create', 'MainActivity_MembersInjector.<init>'))
sup(('MainActivity_MembersInjector.injectMembers', 'MainActivity_MembersInjector.injectMDatabases'))
sup(('RecentDatabaseEntryComparator.compare', 'DatabaseMetadata.isSynchronised'))

# ================================================================== UNREACHABLE (batch 083). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['MainActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (javax.inject.Provider argument, class-file flags 0x0001). Its only caller record is create (auto_calls.json, MainActivity_MembersInjector.java:22), and create has no caller: no app source names the injector, and DaggerMmxComponent.class references only injectMDatabases of the injector (label_083.grep.txt sections 1, 3)',
  'python-printed auto_calls record MainActivity_MembersInjector.java:22 (label_083.grep.txt section 4); class-file parse of MainActivity_MembersInjector.class and DaggerMmxComponent.class (section 3)',
  'INFERRED')

UNREACHABLE['MainActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (class-file flags 0x0009). No caller: DaggerMmxComponent.class references injectMDatabases (DaggerMmxComponent.java:403 in the auto_calls record), not create; no app source reference (label_083.grep.txt sections 1, 3)',
  'class-file parse (label_083.grep.txt section 3); section 2 (only MainActivity_MembersInjector.class and DaggerMmxComponent.class name the injector); no auto_calls record with create as dst',
  'INFERRED')

UNREACHABLE['MainActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance injector, typed to MainActivity (class-file flags 0x0001). No caller: no class file calls injectMembers(MainActivity); the component refers only to injectMDatabases. Its only outgoing record is injectMembers -> injectMDatabases (MainActivity_MembersInjector.java:27), cut by sup()',
  'python-printed auto_calls record MainActivity_MembersInjector.java:27 (section 4); class-file parse (section 3); the synthetic bridge injectMembers(Object)V (flags 0x1041) is an open point, not a row',
  'INFERRED')

UNREACHABLE['MyActionBarDrawerToggle.<init>(AppCompatActivity,DrawerLayout,Toolbar,int,int)'] = ('no_trigger_in_app',
  'Second constructor (with Toolbar). The only app construction is the 4-argument form at MainActivity.java:1296; no other "new MyActionBarDrawerToggle" in app source (grep section 1); no auto_calls record names this constructor (section 4)',
  'MyActionBarDrawerToggle.java:37-40 (declaration); MainActivity.java:1296 (the only app construction, 4-argument form); label_083.grep.txt sections 1, 3, 4',
  'SOURCE')

UNREACHABLE['RecentDatabaseEntryComparator.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor (class-file <init>()V, flags 0x0001). The class is never instantiated: source grep finds only its declaration (RecentDatabaseEntryComparator.java:24), and no class file except its own names it (grep section 2)',
  'RecentDatabaseEntryComparator.java:24-25 (declaration); label_083.grep.txt sections 1, 2, 3',
  'SOURCE')

UNREACHABLE['RecentDatabaseEntryComparator.compare'] = ('no_trigger_in_app',
  'Comparator body (RecentDatabaseEntryComparator.java:48-58). Runs only as a Comparator of DatabaseMetadata, and the comparator is never instantiated (row above). Its auto_calls record compare -> DatabaseMetadata.isSynchronised (line 49) is cut by sup()',
  'RecentDatabaseEntryComparator.java:47-59; python-printed auto_calls record line 49 (section 4); class-file parse (section 3); the synthetic bridge compare(Object,Object)I (flags 0x1041) is an open point',
  'SOURCE')

# ---- part 085 (2026-10-29)
# ================================================================== batch 085 (label_085): EditPriceDialog (11 methods), EditPriceDialog$$Icepick (4), EditPriceDialog$1 to $7 (15 methods: constructors and callbacks), EditPriceDialog_MembersInjector (4), EditPriceViewHolder (3) and EditPriceViewHolder_ViewBinding (2). 39 methods in all (graphs/MMEX/scratch/batches/batch_085.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_085.md (3 REACHABLE, 36 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_085.grep.txt (sections 1-10).
# This file writes:
#   - 1 CALL edge (cls non_standard): EditPriceViewHolder.bind(AppCompatActivity) to EditPriceViewHolder_ViewBinding.<init> (ButterKnife.bind(this, activity) at EditPriceViewHolder.java:53; no auto_calls.json record, so no D7 duplicate);
#   - 66 sup pairs (D14a): 65 auto CALL records whose caller is UNREACHABLE in this batch, and the cross-batch cut DaggerMmxComponent.injectEditPriceDialog -> EditPriceDialog_MembersInjector.injectDateTimeUtilsLazy (AGENT_NOTES.md line 307: batch 085 owns it; the batch 044 caller is UNREACHABLE);
#   - 36 UNREACHABLE entries.
# Not written here: the records of PriceEditActivity.onCreate (lines 80-81) stay, because they make the holder REACHABLE (route through batch 088, interim per D8); the cuts of injectEditPriceDialog -> MmxDateTimeUtils_Factory.<clinit> and .create belong to batch 140; the cut of DaggerMmxComponent.inject(EditPriceDialog) -> injectEditPriceDialog is in label_043.py.

# ---- REACHABLE: the holder's constructor and bind(AppCompatActivity), by auto CALL records from PriceEditActivity.onCreate (batch 088, not merged)
# ---- and the ButterKnife binding constructor, which has no auto record (generated class, built by reflection)

e('EditPriceViewHolder.bind(AppCompatActivity)', 'EditPriceViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, activity) builds the generated binding for the holder, which binds the @BindView fields of the activity',
  cls='non_standard', via='ButterKnife.bind(this, activity) (library): the generated EditPriceViewHolder_ViewBinding is built by reflection (INFERRED, library not read)',
  evidence='SRC investment/EditPriceViewHolder.java:52-54 (ButterKnife.bind at 53); SRC investment/EditPriceViewHolder.java:28-29 (butterknife imports); label_085.grep.txt section 6 (ButterKnife.bind call sites), section 10 (the generated class is in build/intermediates; no class file names it except itself)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE

sup(
    # EditPriceDialog$$Icepick.<clinit>: cut here (AGENT_NOTES.md line 315; label_041 PriceDownloadedEventBundler.<init> stays UNREACHABLE)
    ('EditPriceDialog$$Icepick.<clinit>', 'PriceDownloadedEventBundler.<init>'),
    # EditPriceDialog$5.onClick, $6.onClick, $4.onClick, $4.lambda$onClick$0 (date and day buttons, date picker)
    ('EditPriceDialog$5.onClick', 'EditPriceDialog.showDate'),
    ('EditPriceDialog$5.onClick', 'MmxDate.toDate'),
    ('EditPriceDialog$5.onClick', 'MmxDate.minusDays'),
    ('EditPriceDialog$5.onClick', 'MmxDate.<init>(Date)'),
    ('EditPriceDialog$6.onClick', 'EditPriceDialog.showDate'),
    ('EditPriceDialog$6.onClick', 'MmxDate.toDate'),
    ('EditPriceDialog$6.onClick', 'MmxDate.plusDays'),
    ('EditPriceDialog$6.onClick', 'MmxDate.<init>(Date)'),
    ('EditPriceDialog$4.onClick', 'MmxDate.getDayOfMonth'),
    ('EditPriceDialog$4.onClick', 'MmxDate.getMonthOfYear'),
    ('EditPriceDialog$4.onClick', 'MmxDate.getYear'),
    ('EditPriceDialog$4.onClick', 'MmxDate.<init>(Date)'),
    ('EditPriceDialog$4.lambda$onClick$0', 'EditPriceDialog.showDate'),
    ('EditPriceDialog$4.lambda$onClick$0', 'MmxDate.toDate'),
    ('EditPriceDialog$4.lambda$onClick$0', 'MmxDate.<init>(int,int,int)'),
    # EditPriceDialog$7.onClick (amount listener; the 4-argument AmountInputDialog.getInstance stays reached through other overloads, see label_023)
    ('EditPriceDialog$7.onClick', 'AmountInputDialog.getInstance(String,Money,Integer,boolean)'),
    # EditPriceDialog$1.get (formatUtilitiesLazy)
    ('EditPriceDialog$1.get', 'FormatUtilities.<init>(Context)'),
    # EditPriceDialog.<init>: cut the cha-dispatch record to the Dagger member injector (AGENT_NOTES.md line 307)
    ('EditPriceDialog.<init>', 'MmexApplication.<clinit>'),
    ('EditPriceDialog.<init>', 'EditPriceDialog$1.<init>'),
    ('EditPriceDialog.<init>', 'DaggerMmxComponent.inject(EditPriceDialog)'),
    ('EditPriceDialog.<init>', 'MmexApplication.getApp'),
    # EditPriceDialog.onCreateDialog
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.create'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog.showCurrentPrice'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog.showDate'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.setNegativeButton'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog$3.<init>'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.setPositiveButton'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog$2.<init>'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog.initializeControls'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceViewHolder.bind(View)'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceViewHolder.<init>'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.setView'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.setIcon'),
    ('EditPriceDialog.onCreateDialog', 'UIHelper.getIcon'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.setTitle(CharSequence)'),
    ('EditPriceDialog.onCreateDialog', 'AlertDialogWrapper.<init>'),
    ('EditPriceDialog.onCreateDialog', 'UIHelper.<init>'),
    ('EditPriceDialog.onCreateDialog', 'EditPriceDialog.createNewEntity'),
    # EditPriceDialog.onEvent, createNewEntity, getUserDateFormat, initializeControls, showCurrentPrice, showDate
    ('EditPriceDialog.onEvent', 'EditPriceDialog.showCurrentPrice'),
    ('EditPriceDialog.createNewEntity', 'PriceDownloadedEvent.<init>'),
    ('EditPriceDialog.createNewEntity', 'MmxDate.toDate'),
    ('EditPriceDialog.createNewEntity', 'MmxDate.<init>(String)'),
    ('EditPriceDialog.getUserDateFormat', 'MmxDateTimeUtils.getUserDatePattern'),
    ('EditPriceDialog.initializeControls', 'EditPriceDialog$7.<init>'),
    ('EditPriceDialog.initializeControls', 'Account.getCurrencyId'),
    ('EditPriceDialog.initializeControls', 'AccountRepository.load'),
    ('EditPriceDialog.initializeControls', 'AccountRepository.<init>'),
    ('EditPriceDialog.initializeControls', 'EditPriceDialog$6.<init>'),
    ('EditPriceDialog.initializeControls', 'EditPriceDialog$5.<init>'),
    ('EditPriceDialog.initializeControls', 'EditPriceDialog.showDate'),
    ('EditPriceDialog.initializeControls', 'EditPriceDialog$4.<init>'),
    ('EditPriceDialog.showCurrentPrice', 'FormatUtilities.format(Money,String)'),
    ('EditPriceDialog.showDate', 'MmxDateTimeUtils.format'),
    ('EditPriceDialog.showDate', 'EditPriceDialog.getUserDateFormat'),
    ('EditPriceDialog.showDate', 'MmxDateTimeUtils.<init>()'),
    # EditPriceDialog_MembersInjector.create and injectMembers (their callee records are internal to the UNREACHABLE injector)
    ('EditPriceDialog_MembersInjector.create', 'EditPriceDialog_MembersInjector.<init>'),
    ('EditPriceDialog_MembersInjector.injectMembers', 'EditPriceDialog_MembersInjector.injectDateTimeUtilsLazy'),
    # EditPriceDialog$2.onClick (positive button): addStockHistoryRecord(PriceDownloadedEvent) cut per D14c (AGENT_NOTES.md line 328)
    ('EditPriceDialog$2.onClick', 'SyncManager.<clinit>'),
    ('EditPriceDialog$2.onClick', 'SyncManager.dataChanged'),
    ('EditPriceDialog$2.onClick', 'SyncManager.<init>'),
    ('EditPriceDialog$2.onClick', 'StockHistoryRepository.addStockHistoryRecord(PriceDownloadedEvent)'),
    ('EditPriceDialog$2.onClick', 'StockHistoryRepository.<init>'),
    ('EditPriceDialog$2.onClick', 'StockRepository.updateCurrentPrice'),
    ('EditPriceDialog$2.onClick', 'StockRepository.<init>'),
    # cross-batch cut owned by batch 085 (AGENT_NOTES.md line 307); the caller row is label_044
    ('DaggerMmxComponent.injectEditPriceDialog', 'EditPriceDialog_MembersInjector.injectDateTimeUtilsLazy'),
)

# ================================================================== UNREACHABLE (batch 085). Tuple: (kind, reason, evidence, confirmed_by)
# Shared basis for the dialog family: the app source never constructs EditPriceDialog (see the entry for its constructor).

UNREACHABLE['EditPriceDialog.<init>'] = ('no_trigger_in_app',
  'Constructor of the DialogFragment. The app source never constructs EditPriceDialog: the only construction (WatchlistItemsFragment.java:255) is commented out, its show call (WatchlistItemsFragment.java:263) is commented out too, and MmxComponent.java:90 declares only the members injection inject(EditPriceDialog), which needs an instance. PriceEditActivity uses only the ARG_ constants (PriceEditActivity.java:198-204).',
  'SRC investment/EditPriceDialog.java:89-99; SRC investment/watchlist/WatchlistItemsFragment.java:255-263; SRC core/ioc/MmxComponent.java:90; label_085.grep.txt sections 1, 2',
  'SOURCE')

UNREACHABLE['EditPriceDialog.onCreateDialog'] = ('no_trigger_in_app',
  'DialogFragment callback. The framework calls it only on a live instance, and none is created (see the constructor). Its callees, including EditPriceViewHolder.bind(View), are unreached from here. EditPriceViewHolder.<init> stays REACHABLE through PriceEditActivity.',
  'SRC investment/EditPriceDialog.java:103-154; auto_calls record EditPriceDialog.java:122 (bind(View)); label_085.grep.txt sections 1, 9',
  'SOURCE')

UNREACHABLE['EditPriceDialog.onStart'] = ('no_trigger_in_app',
  'Fragment lifecycle callback. It needs a live instance, so the EventBus registration at EditPriceDialog.java:160 never runs.',
  'SRC investment/EditPriceDialog.java:157-161; label_085.grep.txt section 1',
  'SOURCE')

UNREACHABLE['EditPriceDialog.onStop'] = ('no_trigger_in_app',
  'Fragment lifecycle callback. It needs a live instance, so the EventBus unregistration at EditPriceDialog.java:167 never runs.',
  'SRC investment/EditPriceDialog.java:164-168; label_085.grep.txt section 1',
  'SOURCE')

UNREACHABLE['EditPriceDialog.onSaveInstanceState'] = ('no_trigger_in_app',
  'Fragment callback. It needs a live instance, so Icepick.saveInstanceState(this, ...) at EditPriceDialog.java:174 never runs.',
  'SRC investment/EditPriceDialog.java:170-175; label_085.grep.txt sections 1, 5',
  'SOURCE')

UNREACHABLE['EditPriceDialog.onEvent'] = ('no_trigger_in_app',
  '@Subscribe handler for AmountEnteredEvent. EventBus delivers only to registered subscribers, and this instance registers only in onStart (EditPriceDialog.java:160), which needs an instance. The handler is therefore never called, even though the event type is reachable elsewhere.',
  'SRC investment/EditPriceDialog.java:157-161, 177-181; auto_calls record EditPriceDialog.java:180 (showCurrentPrice); label_085.grep.txt section 1',
  'SOURCE')

UNREACHABLE['EditPriceDialog.createNewEntity'] = ('no_trigger_in_app',
  'Private helper, called only from onCreateDialog (EditPriceDialog.java:107), which is unreached because no instance exists.',
  'SRC investment/EditPriceDialog.java:107, 187-194; auto_calls record EditPriceDialog.java:107',
  'SOURCE')

UNREACHABLE['EditPriceDialog.getUserDateFormat'] = ('no_trigger_in_app',
  'Private helper, called only from showDate (EditPriceDialog.java:274), which is unreached because no instance exists.',
  'SRC investment/EditPriceDialog.java:196-201, 274; auto_calls record EditPriceDialog.java:274',
  'SOURCE')

UNREACHABLE['EditPriceDialog.initializeControls'] = ('no_trigger_in_app',
  'Private helper, called only from onCreateDialog (EditPriceDialog.java:123), which is unreached because no instance exists.',
  'SRC investment/EditPriceDialog.java:123, 203-266; auto_calls record EditPriceDialog.java:123',
  'SOURCE')

UNREACHABLE['EditPriceDialog.showCurrentPrice'] = ('no_trigger_in_app',
  'Private helper, called only from onCreateDialog (EditPriceDialog.java:151) and onEvent (EditPriceDialog.java:180), both unreached.',
  'SRC investment/EditPriceDialog.java:151, 180, 268-271; auto_calls records EditPriceDialog.java:151, 180',
  'SOURCE')

UNREACHABLE['EditPriceDialog.showDate'] = ('no_trigger_in_app',
  'Private helper, called only from onCreateDialog (EditPriceDialog.java:150), initializeControls (EditPriceDialog.java:230) and the listeners at EditPriceDialog.java:213, 237 and 244, all unreached.',
  'SRC investment/EditPriceDialog.java:150, 213, 230, 237, 244, 273-275; auto_calls records EditPriceDialog.java:150, 230, 237, 244',
  'SOURCE')

# ---- Icepick helper (generated; not in the source root; reached only through Icepick reflection on the dialog instance)

UNREACHABLE['EditPriceDialog$$Icepick.<clinit>'] = ('no_trigger_in_app',
  'Generated Icepick helper static initializer. Icepick uses the helper only from Icepick.restoreInstanceState and saveInstanceState (EditPriceDialog.java:105, 174), which run on an instance that is never created. Its only record is <clinit> -> PriceDownloadedEventBundler.<init> (EditPriceDialog$$Icepick.java:16), which is cut here.',
  'auto_calls record EditPriceDialog$$Icepick.java:16; SRC investment/EditPriceDialog.java:105, 174; label_085.grep.txt sections 3, 5, 9, 10',
  'INFERRED')

UNREACHABLE['EditPriceDialog$$Icepick.<init>'] = ('no_trigger_in_app',
  'Generated helper constructor. No caller: no source file names the helper, no auto_calls record targets it, and no other class file names it (section 10).',
  'label_085.grep.txt sections 4, 9, 10; class file build/intermediates EditPriceDialog$$Icepick.class (section 3)',
  'INFERRED')

UNREACHABLE['EditPriceDialog$$Icepick.restore'] = ('no_trigger_in_app',
  'Generated helper method. Icepick calls it from Icepick.restoreInstanceState(this, bundle) (EditPriceDialog.java:105) in onCreateDialog, which runs only on an instance that is never created. No record names restore.',
  'SRC investment/EditPriceDialog.java:103-106; label_085.grep.txt sections 5, 9, 10',
  'INFERRED')

UNREACHABLE['EditPriceDialog$$Icepick.save'] = ('no_trigger_in_app',
  'Generated helper method. Icepick calls it from Icepick.saveInstanceState(this, bundle) (EditPriceDialog.java:174) in onSaveInstanceState, which runs only on an instance that is never created. No record names save.',
  'SRC investment/EditPriceDialog.java:170-175; label_085.grep.txt sections 5, 9, 10',
  'INFERRED')

# ---- anonymous classes and lambda of the dialog (SOURCE: created only inside the unreached dialog methods)

UNREACHABLE['EditPriceDialog$1.<init>'] = ('no_trigger_in_app',
  'Anonymous Lazy for formatUtilitiesLazy, created in the dialog constructor (EditPriceDialog.java:93), which is unreached.',
  'SRC investment/EditPriceDialog.java:87, 89-99; auto_calls record EditPriceDialog.java:93',
  'SOURCE')

UNREACHABLE['EditPriceDialog$1.get'] = ('no_trigger_in_app',
  'Lazy.get of formatUtilitiesLazy, called only from showCurrentPrice (EditPriceDialog.java:269), which is unreached.',
  'SRC investment/EditPriceDialog.java:93-98, 268-271; auto_calls record EditPriceDialog.java:96',
  'SOURCE')

UNREACHABLE['EditPriceDialog$2.<init>'] = ('no_trigger_in_app',
  'Anonymous listener for the positive button, created in onCreateDialog (EditPriceDialog.java:126), which is unreached.',
  'SRC investment/EditPriceDialog.java:126-142; auto_calls record EditPriceDialog.java:126',
  'SOURCE')

UNREACHABLE['EditPriceDialog$2.onClick'] = ('no_trigger_in_app',
  'Positive-button listener (EditPriceDialog.java:127-141). Its only entry is onCreateDialog, which is unreached, so the price update and history record (addStockHistoryRecord at line 134) are dead here. Its records are cut in this file (D14a); the cut of the addStockHistoryRecord(PriceDownloadedEvent) record is D14c (AGENT_NOTES.md line 328).',
  'SRC investment/EditPriceDialog.java:126-142; auto_calls records EditPriceDialog.java:130-140; label_057.py (addStockHistoryRecord(PriceDownloadedEvent) is UNREACHABLE there)',
  'SOURCE')

UNREACHABLE['EditPriceDialog$3.<init>'] = ('no_trigger_in_app',
  'Anonymous listener for the negative button, created in onCreateDialog (EditPriceDialog.java:143), which is unreached.',
  'SRC investment/EditPriceDialog.java:143-148; auto_calls record EditPriceDialog.java:143',
  'SOURCE')

UNREACHABLE['EditPriceDialog$3.onClick'] = ('no_trigger_in_app',
  'Negative-button listener (EditPriceDialog.java:145-147). The dialog is never built, so it never runs.',
  'SRC investment/EditPriceDialog.java:143-148',
  'SOURCE')

UNREACHABLE['EditPriceDialog$4.<init>'] = ('no_trigger_in_app',
  'Anonymous date-field listener, created in initializeControls (EditPriceDialog.java:206), which is unreached.',
  'SRC investment/EditPriceDialog.java:203-206; auto_calls record EditPriceDialog.java:206',
  'SOURCE')

UNREACHABLE['EditPriceDialog$4.onClick'] = ('no_trigger_in_app',
  'Date-field click listener (EditPriceDialog.java:207-226). Its only entry is initializeControls, which is unreached.',
  'SRC investment/EditPriceDialog.java:206-227; auto_calls records EditPriceDialog.java:209, 219-221',
  'SOURCE')

UNREACHABLE['EditPriceDialog$4.lambda$onClick$0'] = ('no_trigger_in_app',
  'Synthetic lambda for the DatePickerDialog listener (EditPriceDialog.java:211-214). It is created only inside EditPriceDialog$4.onClick, which is unreached.',
  'SRC investment/EditPriceDialog.java:211-214; auto_calls records EditPriceDialog.java:212-213',
  'SOURCE')

UNREACHABLE['EditPriceDialog$5.<init>'] = ('no_trigger_in_app',
  'Anonymous previous-day listener, created in initializeControls (EditPriceDialog.java:233), which is unreached.',
  'SRC investment/EditPriceDialog.java:233-239; auto_calls record EditPriceDialog.java:233',
  'SOURCE')

UNREACHABLE['EditPriceDialog$5.onClick'] = ('no_trigger_in_app',
  'Previous-day listener (EditPriceDialog.java:235-238). Its only entry is initializeControls, which is unreached.',
  'SRC investment/EditPriceDialog.java:233-239; auto_calls records EditPriceDialog.java:236-237',
  'SOURCE')

UNREACHABLE['EditPriceDialog$6.<init>'] = ('no_trigger_in_app',
  'Anonymous next-day listener, created in initializeControls (EditPriceDialog.java:240), which is unreached.',
  'SRC investment/EditPriceDialog.java:240-246; auto_calls record EditPriceDialog.java:240',
  'SOURCE')

UNREACHABLE['EditPriceDialog$6.onClick'] = ('no_trigger_in_app',
  'Next-day listener (EditPriceDialog.java:242-245). Its only entry is initializeControls, which is unreached.',
  'SRC investment/EditPriceDialog.java:240-246; auto_calls records EditPriceDialog.java:243-244',
  'SOURCE')

UNREACHABLE['EditPriceDialog$7.<init>'] = ('no_trigger_in_app',
  'Anonymous amount-field listener, created in initializeControls (EditPriceDialog.java:256), which is unreached.',
  'SRC investment/EditPriceDialog.java:256-265; auto_calls record EditPriceDialog.java:256',
  'SOURCE')

UNREACHABLE['EditPriceDialog$7.onClick'] = ('no_trigger_in_app',
  'Amount-field listener (EditPriceDialog.java:258-263). Its only entry is initializeControls, which is unreached, so this route to AmountInputDialog.getInstance (line 259) is dead. The 4-argument getInstance stays reached through other overloads (AmountInputDialog.java:64-83; see label_085.grep.txt section 9 and the report to the orchestrator).',
  'SRC investment/EditPriceDialog.java:256-265; auto_calls record EditPriceDialog.java:259; label_085.grep.txt section 9',
  'SOURCE')

# ---- Dagger member injector of EditPriceDialog (generated; INFERRED: class file in build/intermediates, no source)

UNREACHABLE['EditPriceDialog_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller record is create (EditPriceDialog_MembersInjector.java:23), and create has no caller (see create below).',
  'auto_calls record EditPriceDialog_MembersInjector.java:23; label_085.grep.txt sections 3, 9, 10',
  'INFERRED')

UNREACHABLE['EditPriceDialog_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory. No auto_calls record targets create, and the component calls injectDateTimeUtilsLazy directly (DaggerMmxComponent.java:488), not create. Its callee record (EditPriceDialog_MembersInjector.java:23) is cut here.',
  'auto_calls records EditPriceDialog_MembersInjector.java:23, DaggerMmxComponent.java:488; label_085.grep.txt sections 9, 10',
  'INFERRED')

UNREACHABLE['EditPriceDialog_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance member injector. No auto_calls record targets injectMembers, and the component calls only injectDateTimeUtilsLazy (DaggerMmxComponent.java:488). Its callee record (EditPriceDialog_MembersInjector.java:28) is cut here.',
  'auto_calls records EditPriceDialog_MembersInjector.java:28, DaggerMmxComponent.java:488; label_085.grep.txt sections 9, 10',
  'INFERRED')

UNREACHABLE['EditPriceDialog_MembersInjector.injectDateTimeUtilsLazy'] = ('no_trigger_in_app',
  'Dagger-generated static member injector for dateTimeUtilsLazy. Its callers are DaggerMmxComponent.injectEditPriceDialog (DaggerMmxComponent.java:488; UNREACHABLE in label_044) and injectMembers (no caller). The record from injectEditPriceDialog is cut here (sup). injectEditPriceDialog is unreached because inject(EditPriceDialog) has no reached caller (label_043 and label_044).',
  'auto_calls records DaggerMmxComponent.java:488, EditPriceDialog_MembersInjector.java:28; label_043.py; label_044.py',
  'INFERRED')

# ---- EditPriceViewHolder: bind(View) is unreached; the constructor and bind(AppCompatActivity) are REACHABLE (above)

UNREACHABLE['EditPriceViewHolder.bind(View)'] = ('no_trigger_in_app',
  'Called only from EditPriceDialog.onCreateDialog (auto_calls record EditPriceDialog.java:122), which is unreached. No other record names bind(View) with another caller, and the ButterKnife call for this overload is only at EditPriceViewHolder.java:49.',
  'SRC investment/EditPriceViewHolder.java:48-50; auto_calls record EditPriceDialog.java:122; label_085.grep.txt sections 6, 7, 9',
  'SOURCE')

# ---- EditPriceViewHolder_ViewBinding.unbind (generated; nothing calls it)

UNREACHABLE['EditPriceViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'Generated unbind. Nothing calls it: ButterKnife.bind(this, activity) at EditPriceViewHolder.java:53 does not keep the Unbinder, and no auto_calls record targets unbind for this class.',
  'SRC investment/EditPriceViewHolder.java:52-54; label_085.grep.txt sections 6, 9, 10',
  'INFERRED')

# ---- part 086 (2026-10-29)
# ================================================================== batch 086 (label_086): 40 methods of com.money.manager.ex.investment: ExchangeRateProviders (3: <clinit>, indexOf, names), InvestmentTransactionEditActivity (27), and its listeners $1-$4 (10: constructors, onItemSelected, onNothingSelected, onClick, lambda$onClick$0).
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_086.md (38 REACHABLE, 2 UNREACHABLE, 0 INCOMPLETE).
# This file writes 13 e() edges and 2 UNREACHABLE entries. It defines no SCREENS key: S_INVESTMENT_TRANSACTION_EDIT is defined by label_087.py:13 and reused here.
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here. The ButterKnife GUI edges into InvestmentTransactionEditActivity_ViewBinding$1-$4.doClick are owned by batch 087 (label_087.py:75-97).
# Framework claims cite FW-SRC lines printed for this batch; other claims are INFERRED where the source was not read.

# ---- entry edges into the activity: the intents from the two list screens, then the framework's lifecycle calls

e('PortfolioFragment.openEditInvestmentActivity', 'InvestmentTransactionEditActivity.<init>', 'INTENT',
  'the portfolio list opens the editor: a stock row tap passes the stock id, the add button passes none (openEditInvestmentActivity)',
  evidence='SRC investment/PortfolioFragment.java:198-204 (Intent at 199; setAction at 202; startActivity at 203); SRC investment/PortfolioFragment.java:124-127 (add button calls openEditInvestmentActivity(null) at 126); SRC investment/PortfolioFragment.java:147-150 (stock row calls it at 149)')

e('WatchlistItemsFragment.openEditInvestmentActivity', 'InvestmentTransactionEditActivity.<init>', 'INTENT',
  'the watchlist add button opens the editor for a new stock (openEditInvestmentActivity, started at 469); no other part names this method',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:465-470 (Intent at 466; setAction at 468; startActivity at 469); SRC investment/watchlist/WatchlistItemsFragment.java:343-346 (onFloatingActionButtonClicked calls it at 345)')

e('InvestmentTransactionEditActivity.<init>', 'InvestmentTransactionEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1216; FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('InvestmentTransactionEditActivity.onCreate', 'S_INVESTMENT_TRANSACTION_EDIT', 'ENTERS',
  'the investment transaction edit screen is shown',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:88 (setContentView R.layout.activity_investment_transaction_edit)')

e('InvestmentTransactionEditActivity.onCreate', 'InvestmentTransactionEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:628-632 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu at 3388); INFERRED: the AppCompat delegate between the window and the activity is not read')

# ---- toolbar save and the back key: GUI edges from the page

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity.onOptionsItemSelected', 'GUI',
  'the save icon is tapped: onOptionsItemSelected runs onActionDoneClick (save branch)',
  gui=['Tap the save icon in the toolbar'],
  guard='item id is MenuHelper.save (InvestmentTransactionEditActivity.java:175)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:169-180 (save branch at 175-176; onActionDoneClick at 176; other items to super at 179); SRC core/MenuHelper.java:37 (save = 2), 87-89 (addSaveToolbarIcon adds the item at 88); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450); INFERRED: the toolbar tap reaching onMenuItemSelected through AppCompat is not read')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity.onBackPressed', 'GUI',
  'the back key is pressed: Activity.onKeyUp calls onBackPressed, which runs onActionCancelClick',
  gui=['Press the back key'],
  guard='targetSdkVersion >= ECLAIR (FW-SRC core/java/android/app/Activity.java:2977)',
  evidence='FW-SRC core/java/android/app/Activity.java:2975-2985 (onKeyUp calls onBackPressed at 2980); FW-SRC core/java/android/app/Activity.java:3001-3003 (onBackPressed); SRC investment/InvestmentTransactionEditActivity.java:182-185 (onBackPressed calls onActionCancelClick at 184); INFERRED: the AppCompat key dispatch to onKeyUp is not read')

# ---- account spinner, date text and the two day arrows (listeners set up in initAccountSelectors and initDateControl)

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity$1.onItemSelected', 'GUI',
  'an account is picked in the account spinner: the stock is held at that account and the form is marked dirty',
  gui=['Choose an account in the account spinner'],
  evidence='SRC investment/InvestmentTransactionEditActivity.java:322-339 (listener 322; onItemSelected 324-333: Account.from 327, setDirty 330, setHeldAt 331; setOnItemSelectedListener 339); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onItemSelected for a valid position at 944); FW-SRC core/java/android/widget/Spinner.java:1184-1186 (drop-down click calls setSelection); INFERRED: the AdapterView and AbsSpinner setSelection path is not read')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity$2.onClick', 'GUI',
  'the date text is tapped: the date picker dialog opens',
  gui=['Tap the date text (textViewDate)'],
  evidence='SRC investment/InvestmentTransactionEditActivity.java:345-369 (listener 345; onClick 347-368; DatePickerDialog built at 358-364; show at 367); SRC investment/InvestmentTransactionViewHolder.java:34 (dateView is textViewDate)')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity$3.onClick', 'GUI',
  'the previous-day arrow is tapped: setDate runs with the purchase date minus one day',
  gui=['Tap the previous-day arrow (previousDayButton)'],
  evidence='SRC investment/InvestmentTransactionEditActivity.java:376-382 (listener 376; minusDays(1) at 379; setDate at 380); SRC investment/InvestmentTransactionViewHolder.java:39 (previousDayButton); SRC res/layout/activity_investment_transaction_edit.xml:72 (previousDayButton)')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity$4.onClick', 'GUI',
  'the next-day arrow is tapped: setDate runs with the purchase date plus one day',
  gui=['Tap the next-day arrow (nextDayButton)'],
  evidence='SRC investment/InvestmentTransactionEditActivity.java:383-389 (listener 383; plusDays(1) at 386; setDate at 387); SRC investment/InvestmentTransactionViewHolder.java:40 (nextDayButton); SRC res/layout/activity_investment_transaction_edit.xml:92 (nextDayButton)')

e('InvestmentTransactionEditActivity$2.onClick', 'InvestmentTransactionEditActivity$2.lambda$onClick$0', 'FRAMEWORK',
  'the user taps OK in the date picker: DatePickerDialog calls the OnDateSetListener, which is this lambda, and the lambda runs setDirty',
  gui=['Tap the date text, then tap OK in the date picker'],
  evidence='SRC investment/InvestmentTransactionEditActivity.java:351-356 (lambda listener; setDirty at 352); SRC investment/InvestmentTransactionEditActivity.java:358-364 (DatePickerDialog built with the listener); FW-SRC core/java/android/app/DatePickerDialog.java:120-123 (BUTTON_POSITIVE set at 122), 164-174 (mDateSetListener.onDateSet at 171); INFERRED: the dialog button dispatch to DatePickerDialog.onClick is not read (AlertController not read)')

# ---- the calculator result returned to the editor

e('CalculatorActivity.returnResult', 'InvestmentTransactionEditActivity.onActivityResult', 'RESULT',
  'a calculator result is returned: returnResult sets RESULT_OK and finishes, and the framework delivers the result to the editor, whose onActivityResult stores the amount in the field that was tapped',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult; setResult(RESULT_OK) at 443; finish at 444; called at 149 and 249); SRC investment/InvestmentTransactionEditActivity.java:119-158 (onActivityResult; Calculator.getAmountFromResult at 125; switch on the four request codes); FW-SRC core/java/android/app/ActivityThread.java:4253-4264 (deliverResults); FW-SRC core/java/android/app/Activity.java:7259-7266 (dispatchActivityResult)')

# ---- UNREACHABLE entries (each has a reason, evidence and basis; a method with no caller in the app)

UNREACHABLE['ExchangeRateProviders.indexOf'] = (
  'no_trigger_in_app',
  'indexOf has no caller in the app: its only occurrence in the source root is its own declaration, and no auto_calls.json record targets it. No other part of graph_def.py or parts/*.py mentions it.',
  'SRC investment/ExchangeRateProviders.java:43-51 (declaration); grep of the source root finds ExchangeRateProviders in four files and indexOf only at ExchangeRateProviders.java:43; no auto_calls.json record with dst ExchangeRateProviders.indexOf',
  'SOURCE')

UNREACHABLE['InvestmentTransactionEditActivity$1.onNothingSelected'] = (
  'branch_never_taken',
  'The framework calls onNothingSelected only for a negative selected position (fireOnSelected, AdapterView.java:946-947), and only when selectionChanged is reached from checkSelectionChanged (1103-1108). The editor never sets a negative selection: its only setSelection (InvestmentTransactionEditActivity.java:275) is guarded by accountIndex >= 0 (line 274). The account adapter is loaded once (line 314) before the listener is attached (line 339), and initAccountSelectors has one caller (line 294). AccountService.loadInvestmentAccountsToSpinner is not read, so whether it can empty a selected spinner is unverified.',
  'SRC investment/InvestmentTransactionEditActivity.java:273-275 (guarded setSelection), 308-316 (loader at 314), 322-339 (listener; onNothingSelected 336-337; attached at 339); FW-SRC core/java/android/widget/AdapterView.java:944-947, 1103-1108',
  'INFERRED')

# ---- part 087 (2026-10-29)
# ================================================================== batch 087 (label_087): 40 methods (graphs/MMEX/scratch/batches/batch_087.txt): InvestmentTransactionEditActivity_MembersInjector (4), InvestmentTransactionEditActivity_ViewBinding (11: its three methods and the listeners $1-$4 with their constructors and doClick), InvestmentTransactionViewHolder.<init>, PortfolioActivity (3), PortfolioCursorAdapter (3), PortfolioFragment (17: its 11 methods and the listeners $1 and $2), PortfolioItemDataViewHolder.<init>.
# Rows, printed lines and counts: graphs/MMEX/parts/label_087.md (33 REACHABLE, 7 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_087.grep.txt (sections 1-6).
# This file writes:
#   - 2 SCREENS keys (new; grep of graph_def.py and parts/*.py found no key for either screen): S_PORTFOLIO (the portfolio list; graph_def.py:3738 notes that the portfolio list has no key) and S_INVESTMENT_TRANSACTION_EDIT (the investment transaction edit screen). batch 086 owns the ENTERS edge into S_INVESTMENT_TRANSACTION_EDIT and must reuse this key (open point in label_087.md);
#   - 17 e() edges: 4 LIFECYCLE and 5 FRAMEWORK inside PortfolioFragment and its loader listener; 1 ENTERS from PortfolioFragment.onCreateView to S_PORTFOLIO; 2 GUI from S_PORTFOLIO (the row tap and the add button); 4 GUI from S_INVESTMENT_TRANSACTION_EDIT to the four ButterKnife listeners; 1 CALL (cls non_standard) from InvestmentTransactionEditActivity.onCreate to the ButterKnife binding constructor (ITEA.java:91, not in auto_calls.json);
#   - 7 sup pairs (D14a): the auto CALL records whose caller is UNREACHABLE in this batch (MembersInjector.create and injectMembers, and the five PortfolioActivity records);
#   - 7 UNREACHABLE entries: MembersInjector.<init>, create, injectMembers, ViewBinding.unbind (generated, INFERRED); PortfolioActivity.<clinit>, <init>, onCreate (app source, SOURCE).
# Not written: the INTENT edges into InvestmentTransactionEditActivity from PortfolioFragment.openEditInvestmentActivity (dst owned by batch 086, D1); the ENTERS edge from InvestmentTransactionEditActivity.onCreate (batch 086); the auto CALL records (D7); the FAB listener BaseListFragment$2 (batch 026).

SCREENS.update({'S_PORTFOLIO': 'The investment portfolio list (PortfolioFragment, shown in MainActivity by showPortfolioFragment in place of the home content): the stock rows of one investment account, the header row, and the add (floating action) button'})

SCREENS.update({'S_INVESTMENT_TRANSACTION_EDIT': 'The investment transaction edit screen (InvestmentTransactionEditActivity): the account, date, stock name, symbol and notes fields, and the number of shares, purchase price, commission and current price fields that open the calculator'})

# ---- PortfolioFragment lifecycle (androidx Fragment; library source not read: INFERRED)

e('PortfolioFragment.<init>', 'PortfolioFragment.onCreate', 'LIFECYCLE',
  'the fragment is created by newInstance (MainActivity.showPortfolioFragment, MainActivity.java:795) and the framework then calls onCreate (the inherited onAttach step is not in this batch)',
  evidence='SRC investment/PortfolioFragment.java:64, 76-86 (onCreate reads mAccountId from the arguments); SRC home/MainActivity.java:795-797; INFERRED androidx Fragment lifecycle (library source not read)')

e('PortfolioFragment.onCreate', 'PortfolioFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC investment/PortfolioFragment.java:89-95 (onCreateView inflates fragment_portfolio at 92); INFERRED androidx Fragment lifecycle (library source not read)')

e('PortfolioFragment.onCreateView', 'PortfolioFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after the view exists; onActivityCreated builds the adapter, the list and the loader',
  evidence='SRC investment/PortfolioFragment.java:98-122; INFERRED androidx Fragment lifecycle (library source not read)')

e('PortfolioFragment.onActivityCreated', 'PortfolioFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state (mAccountId) when it saves the instance state; the save is triggered by the framework (for example before the fragment stops), not by a fixed step after onActivityCreated, and the edge records the method as the next lifecycle method of this class in batch order (INFERRED)',
  evidence='SRC investment/PortfolioFragment.java:130-134; INFERRED androidx FragmentManager saves state through onSaveInstanceState (library source not read)')

# ---- PortfolioFragment loader callbacks (androidx LoaderManager; library not read: INFERRED). Same pattern as label_008 (AccountListFragment)

e('PortfolioFragment.initializeLoader', 'PortfolioFragment$2.onCreateLoader', 'FRAMEWORK',
  'initLoader starts the stock loader and the LoaderManager calls onCreateLoader (the loader query is built there, filtered on HELDAT = the account id)',
  evidence='SRC investment/PortfolioFragment.java:156-170 (initLoader at 158, onCreateLoader at 160); INFERRED androidx LoaderManager.initLoader calls the LoaderCallbacks (library not read)')

e('PortfolioFragment$2.onCreateLoader', 'PortfolioFragment$2.onLoadFinished', 'FRAMEWORK',
  'the loader (MmxCursorLoader) delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC investment/PortfolioFragment.java:160-172, 174; INFERRED androidx Loader delivers its result to the callbacks (library not read)')

e('PortfolioFragment$2.onLoadFinished', 'PortfolioFragment$2.onLoaderReset', 'FRAMEWORK',
  'a loader that has delivered data is reset and the LoaderManager calls onLoaderReset (the cursor is set to null)',
  evidence='SRC investment/PortfolioFragment.java:192-194; INFERRED androidx LoaderManager calls onLoaderReset when a loader with data is destroyed (library not read)')

# ---- the cursor adapter rows: changeCursor relays out the list and the framework calls getView, which calls newView (no scrap view) and bindView

e('PortfolioFragment$2.onLoadFinished', 'PortfolioCursorAdapter.newView', 'FRAMEWORK',
  'adapter.changeCursor(data) swaps in the cursor and notifies the list; on the relayout the framework calls getView, which calls newView for a row that has no scrap view (the first layout of the data)',
  evidence='SRC investment/PortfolioFragment.java:174-176 (changeCursor at 176); FW-SRC fw_src/android-8.1.0_r1/core/java/android/widget/CursorAdapter.java:348-353 (changeCursor calls swapCursor), 365-381 (swapCursor calls notifyDataSetChanged at 381), 276-289 (getView calls newView at 285 when convertView is null); androidx CursorAdapter not in the dataset: INFERRED to match this framework source (label_014.py evidence)')

e('PortfolioFragment$2.onLoadFinished', 'PortfolioCursorAdapter.bindView', 'FRAMEWORK',
  'the same relayout: the framework calls getView, which calls bindView for every visible row (the cursor columns are copied into the row views)',
  evidence='SRC investment/PortfolioFragment.java:174-176; SRC investment/PortfolioCursorAdapter.java:70 (bindView); FW-SRC fw_src/android-8.1.0_r1/core/java/android/widget/CursorAdapter.java:289 (getView calls bindView); INFERRED androidx CursorAdapter (library not read)')

# ---- the portfolio list page (new key S_PORTFOLIO, D9: a user-visible screen with its own list and button)

e('PortfolioFragment.onCreateView', 'S_PORTFOLIO', 'ENTERS',
  'the portfolio list is shown: onCreateView inflates the list (fragment_portfolio.xml, list at 52) and the add button (fab at 76); MainActivity.showPortfolioFragment puts the fragment in place of the home content',
  evidence='SRC investment/PortfolioFragment.java:89-95; SRC res/layout/fragment_portfolio.xml:52, 75-76; SRC home/MainActivity.java:791-797 (showPortfolioFragment calls showFragment at 797)')

e('S_PORTFOLIO', 'PortfolioFragment$1.onItemClick', 'GUI',
  'tap a stock row in the portfolio list: the header row is ignored; the stock row opens the edit screen for that stock (openEditInvestmentActivity)',
  gui=['Tap a stock row in the portfolio list (the header row is ignored)'],
  evidence='SRC investment/PortfolioFragment.java:140-149 (setOnItemClickListener at 140, onItemClick at 142, header skip at 144, openEditInvestmentActivity at 149); SRC res/layout/fragment_portfolio.xml:52 (android:id/list); auto_calls record PortfolioFragment$1.onItemClick -> PortfolioFragment.openEditInvestmentActivity (PortfolioFragment.java:149, via PortfolioFragment.access$000)')

e('S_PORTFOLIO', 'PortfolioFragment.onFloatingActionButtonClicked', 'GUI',
  'tap the add (floating action) button on the portfolio list: the edit screen opens with no stock (ACTION_INSERT, stock id null)',
  gui=['Tap the add (floating action) button (fab) on the portfolio list'],
  evidence='SRC investment/PortfolioFragment.java:125-126 (onFloatingActionButtonClicked calls openEditInvestmentActivity(null) at 126); SRC common/BaseListFragment.java:238-244 (the fab click listener calls onFloatingActionButtonClicked at 244); SRC res/layout/fragment_portfolio.xml:75-76 (fab)')

# ---- the investment transaction edit page (new key S_INVESTMENT_TRANSACTION_EDIT). Its ENTERS edge is owned by batch 086 (ITEA.onCreate)

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity_ViewBinding$1.doClick', 'GUI',
  'tap the number of shares field: the @OnClick listener of the generated binding calls onNumSharesClick, which opens the calculator for the shares',
  gui=['Tap the number of shares field (numSharesView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:211-212 (@OnClick at 211, method at 212); SRC res/layout/activity_investment_transaction_edit.xml:168 (numSharesView); auto_calls record InvestmentTransactionEditActivity_ViewBinding$1.doClick -> InvestmentTransactionEditActivity.onNumSharesClick (generated InvestmentTransactionEditActivity_ViewBinding.java:41); INFERRED ButterKnife listener')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity_ViewBinding$2.doClick', 'GUI',
  'tap the purchase price field: the @OnClick listener of the generated binding calls onPurchasePriceClick (returns early when no account is loaded), which opens the calculator for the purchase price',
  gui=['Tap the purchase price field (purchasePriceView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:221-223 (@OnClick at 221, method at 222, guard at 223); SRC res/layout/activity_investment_transaction_edit.xml:183 (purchasePriceView); auto_calls record InvestmentTransactionEditActivity_ViewBinding$2.doClick -> InvestmentTransactionEditActivity.onPurchasePriceClick (generated InvestmentTransactionEditActivity_ViewBinding.java:49); INFERRED ButterKnife listener')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity_ViewBinding$3.doClick', 'GUI',
  'tap the commission field: the @OnClick listener of the generated binding calls onCommissionClick, which opens the calculator for the commission',
  gui=['Tap the commission field (commissionView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:232-233 (@OnClick at 232, method at 233); SRC res/layout/activity_investment_transaction_edit.xml:217 (commissionView); auto_calls record InvestmentTransactionEditActivity_ViewBinding$3.doClick -> InvestmentTransactionEditActivity.onCommissionClick (generated InvestmentTransactionEditActivity_ViewBinding.java:57); INFERRED ButterKnife listener')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity_ViewBinding$4.doClick', 'GUI',
  'tap the current price field: the @OnClick listener of the generated binding calls onCurrentPriceClick, which opens the calculator for the current price',
  gui=['Tap the current price field (currentPriceView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:240-241 (@OnClick at 240, method at 241); SRC res/layout/activity_investment_transaction_edit.xml:234 (currentPriceView); auto_calls record InvestmentTransactionEditActivity_ViewBinding$4.doClick -> InvestmentTransactionEditActivity.onCurrentPriceClick (generated InvestmentTransactionEditActivity_ViewBinding.java:65); INFERRED ButterKnife listener')

# ---- ButterKnife binding of the edit activity (CALL not in auto_calls.json: the call is made by reflection; INFERRED)

e('InvestmentTransactionEditActivity.onCreate', 'InvestmentTransactionEditActivity_ViewBinding.<init>(InvestmentTransactionEditActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for the activity, which binds the @OnClick handlers and the views (the two-argument constructor is an auto CALL record)',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated InvestmentTransactionEditActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:86-91 (onCreate; ButterKnife.bind(this) at 91; the return value is not kept); INFERRED ButterKnife generated binding (label_087.grep.txt sections 2, 3)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('InvestmentTransactionEditActivity_MembersInjector.create', 'InvestmentTransactionEditActivity_MembersInjector.<init>'),
    ('InvestmentTransactionEditActivity_MembersInjector.injectMembers', 'InvestmentTransactionEditActivity_MembersInjector.injectDateTimeUtilsLazy'),
    ('PortfolioActivity.<init>', 'MmxBaseFragmentActivity.<init>'),
    ('PortfolioActivity.onCreate', 'MmxBaseFragmentActivity.onCreate'),
    ('PortfolioActivity.onCreate', 'MmxBaseFragmentActivity.setContentView'),
    ('PortfolioActivity.onCreate', 'MmxBaseFragmentActivity.setDisplayHomeAsUpEnabled'),
    ('PortfolioActivity.onCreate', 'PortfolioFragment.newInstance'))

# ================================================================== UNREACHABLE (batch 087). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['InvestmentTransactionEditActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller record is create (auto_calls record InvestmentTransactionEditActivity_MembersInjector.java:25), and create has no caller: no class file refers to create or to this constructor (grep section 5), and DaggerMmxComponent refers only to the static injectDateTimeUtilsLazy. The app source has no reference to the class (section 1).',
  'python-printed auto_calls record InvestmentTransactionEditActivity_MembersInjector.java:25 (section 6); class-file parse (section 5); label_087.grep.txt section 1',
  'INFERRED')

UNREACHABLE['InvestmentTransactionEditActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated factory method (takes the Provider and returns a MembersInjector). No class file refers to create (section 5). The component calls the static injectDateTimeUtilsLazy directly (DaggerMmxComponent.java:396, section 6), not create. No app source reference (section 1).',
  'class-file parse (label_087.grep.txt section 5); python-printed auto_calls record DaggerMmxComponent.java:396 (section 6); label_087.grep.txt section 1',
  'INFERRED')

UNREACHABLE['InvestmentTransactionEditActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (takes the InvestmentTransactionEditActivity). No caller: no class file refers to it (section 5), and the component refers only to the static injectDateTimeUtilsLazy. Its only outgoing record, injectMembers -> injectDateTimeUtilsLazy (InvestmentTransactionEditActivity_MembersInjector.java:30), is cut by the sup pair above. The synthetic bridge injectMembers(Object) is not in this batch (open point in label_087.md).',
  'python-printed auto_calls record InvestmentTransactionEditActivity_MembersInjector.java:30 (section 6); class-file parse (section 5); label_087.grep.txt section 1',
  'INFERRED')

UNREACHABLE['InvestmentTransactionEditActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method. ButterKnife.bind(this) at InvestmentTransactionEditActivity.java:91 discards the returned Unbinder, the activity has no onDestroy and no unbind or Unbinder reference (section 2), and no class file refers to unbind (section 5). No auto_calls record has unbind as its destination (section 6).',
  'SRC investment/InvestmentTransactionEditActivity.java:86-91; label_087.grep.txt sections 1, 2, 5, 6',
  'INFERRED')

UNREACHABLE['PortfolioActivity.<clinit>'] = ('no_trigger_in_app',
  'Static initializer (FRAGMENT_TAG = PortfolioFragment.class.getSimpleName()). The class is never initialized: it has no start site. The manifest entry has no intent-filter (AndroidManifest.xml:352-354), no source file names PortfolioActivity except its own file, and no class file refers to it except its own (sections 1, 3, 4).',
  'SRC investment/PortfolioActivity.java:27-32 (class and FRAGMENT_TAG); AndroidManifest.xml:352-354; label_087.grep.txt sections 1, 3, 4',
  'SOURCE')

UNREACHABLE['PortfolioActivity.<init>'] = ('no_trigger_in_app',
  'Default constructor of an activity that has no start site (see PortfolioActivity.<clinit>). Its only outgoing record, the super call to MmxBaseFragmentActivity.<init> (PortfolioActivity.java:27), is cut by the sup pair above.',
  'SRC investment/PortfolioActivity.java:27; AndroidManifest.xml:352-354; label_087.grep.txt sections 1, 3, 4',
  'SOURCE')

UNREACHABLE['PortfolioActivity.onCreate'] = ('no_trigger_in_app',
  'Activity entry method of PortfolioActivity, which has no start site (see PortfolioActivity.<clinit>). Its outgoing records (PortfolioActivity.java:33, 35, 38, 49: the super call, setContentView, setDisplayHomeAsUpEnabled and PortfolioFragment.newInstance) are cut by the sup pairs above. The list reaches PortfolioFragment through MainActivity.showPortfolioFragment instead (MainActivity.java:795, outside this batch).',
  'SRC investment/PortfolioActivity.java:33-51; AndroidManifest.xml:352-354; label_087.grep.txt sections 1, 3, 4, 6',
  'SOURCE')

# ---- part 088 (2026-10-29)
# ================================================================== batch 088 (label_088): PriceCsvExport (5 methods), PriceCsvParser (3), PriceEditActivity (15), PriceEditActivity_MembersInjector (4), PriceEditActivity_ViewBinding (11: its two constructors, unbind, and the listener classes $1 to $4 with constructor and doClick), PriceEditModel (2). 40 methods in all (graphs/MMEX/scratch/batches/batch_088.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_088.md (35 REACHABLE, 5 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_088.grep.txt (sections 1-6).
# This file writes:
#   - 1 SCREENS key: S_PRICE_EDIT (new; no S_PRICE* or S_WATCH* key exists in graph_def.py or the parts);
#   - 13 e() edges: 1 INTENT into PriceEditActivity.<init> (from WatchlistItemsFragment.onContextItemSelected, no auto record: the Intent is built from a class literal); 1 LIFECYCLE <init> -> onCreate; 1 ENTERS onCreate -> S_PRICE_EDIT; 1 CALL (cls non_standard) onCreate -> ViewBinding.<init>(PriceEditActivity) (ButterKnife.bind(this), PriceEditActivity.java:70; not in auto_calls.json); 1 FRAMEWORK onCreate -> onCreateOptionsMenu; 1 LIFECYCLE onCreate -> onSaveInstanceState; 6 GUI edges from S_PRICE_EDIT (the four ButterKnife listeners $1 to $4, cls non_standard; the save icon -> onOptionsItemSelected; the date dialog listener lambda, cls non_standard); 1 RESULT CalculatorActivity.returnResult -> PriceEditActivity.onActivityResult;
#   - 2 sup pairs (D14a): the auto CALL records of the UNREACHABLE create (to its constructor) and of the UNREACHABLE injectMembers (to injectDateTimeUtilsLazy);
#   - 5 UNREACHABLE entries: MembersInjector.<init>, create, injectMembers and ViewBinding.unbind (generated, INFERRED, grep.txt sections 3-4); PriceCsvParser.getContext (app source, SOURCE).
# Not written: no CALL edge that is already in auto_calls.json (D7). The route into the watchlist (batches 092 and 094, not merged) stays interim (D8).

SCREENS.update({'S_PRICE_EDIT': 'The security price editor (PriceEditActivity), opened from the watchlist item context menu (Edit price): the amount field (amountTextView) opens the calculator, the date field (dateTextView) opens a date dialog, the previous and next day buttons change the date, and the save icon in the toolbar (MenuHelper.save) saves the price'})

# ---- PriceEditActivity: entry, lifecycle and the generated ButterKnife binding

e('WatchlistItemsFragment.onContextItemSelected', 'PriceEditActivity.<init>', 'INTENT',
  'the Edit price context-menu item builds an Intent for PriceEditActivity (IntentFactory.getPriceEditIntent) and starts it with startActivityForResult; the framework then creates the activity by reflection',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:240-253 (EditPrice case; getPriceEditIntent at 245; startActivityForResult at 253); SRC core/IntentFactory.java:80-83 (new Intent(context, PriceEditActivity.class)); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (newActivity: cl.loadClass(className).newInstance()); the watchlist route is interim (batches 092 and 094, not merged, D8)')

e('PriceEditActivity.<init>', 'PriceEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity (Instrumentation.callActivityOnCreate, then Activity.performCreate)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2669 (newActivity), 2729-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6997 and 6999)')

e('PriceEditActivity.onCreate', 'S_PRICE_EDIT', 'ENTERS',
  'setContentView(R.layout.activity_price_edit) shows the price editor (PriceEditActivity.java:66)',
  evidence='SRC investment/PriceEditActivity.java:66 (setContentView); res/layout/activity_price_edit.xml:27 (appbar), 77 (priceEditorScrollView); auto_calls.json record PriceEditActivity.onCreate -> MmxBaseFragmentActivity.setContentView (PriceEditActivity.java:66, exact)')

e('PriceEditActivity.onCreate', 'PriceEditActivity_ViewBinding.<init>(PriceEditActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for the activity, which binds the @OnClick handlers and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated PriceEditActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC investment/PriceEditActivity.java:70 (ButterKnife.bind(this); the return value is not kept); label_088.grep.txt section 4 (no class file has a Methodref to the one-argument constructor; PriceEditActivity.class holds only the ButterKnife.bind call)')

e('PriceEditActivity.onCreate', 'PriceEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu (the save icon is added there)',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:615-640 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu at 3388); the AppCompat toolbar path is a library (not read, INFERRED)')

e('PriceEditActivity.onCreate', 'PriceEditActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity when it is paused with saveState set (same shape as AccountEditActivity.onCreate -> onSaveInstanceState, graph_def.py:622): ActivityThread.performPauseActivity calls callCallActivityOnSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3855-3876 (performPauseActivity; callCallActivityOnSaveInstanceState at 3875 when saveState is set and the activity is not finished); FW-SRC core/java/android/app/ActivityThread.java:4713-4722 (callCallActivityOnSaveInstanceState calls Instrumentation); FW-SRC core/java/android/app/Instrumentation.java:1385-1386')

# ---- GUI edges from the price editor page S_PRICE_EDIT (ButterKnife @OnClick listeners: INFERRED; the handlers are auto CALL records)

e('S_PRICE_EDIT', 'PriceEditActivity_ViewBinding$1.doClick', 'GUI',
  'tap the amount field: the @OnClick listener of the generated binding calls onPriceClick, which opens the calculator for the price',
  gui=['Tap the amount field (amountTextView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/PriceEditActivity.java:135-141 (@OnClick(R.id.amountTextView) at 135; onPriceClick 136-141); SRC res/layout/activity_price_edit.xml:219 (amountTextView); auto_calls.json record PriceEditActivity_ViewBinding.java:40 ($1.doClick -> onPriceClick, exact); INFERRED ButterKnife listener')

e('S_PRICE_EDIT', 'PriceEditActivity_ViewBinding$2.doClick', 'GUI',
  'tap the date field: the @OnClick listener of the generated binding calls onDateClick, which opens the date dialog',
  gui=['Tap the date field (dateTextView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/PriceEditActivity.java:143-162 (@OnClick(R.id.dateTextView) at 143; onDateClick 144-162); SRC res/layout/activity_price_edit.xml:176 (dateTextView); auto_calls.json record PriceEditActivity_ViewBinding.java:48 ($2.doClick -> onDateClick, exact); INFERRED ButterKnife listener')

e('S_PRICE_EDIT', 'PriceEditActivity_ViewBinding$3.doClick', 'GUI',
  'tap the previous day button: the @OnClick listener of the generated binding calls onPreviousDayClick, which moves the date back one day and redisplays the page',
  gui=['Tap the previous day button (previousDayButton)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/PriceEditActivity.java:164-169 (@OnClick(R.id.previousDayButton) at 164; onPreviousDayClick 165-169); SRC res/layout/activity_price_edit.xml:152 (previousDayButton); auto_calls.json record PriceEditActivity_ViewBinding.java:56 ($3.doClick -> onPreviousDayClick, exact); INFERRED ButterKnife listener')

e('S_PRICE_EDIT', 'PriceEditActivity_ViewBinding$4.doClick', 'GUI',
  'tap the next day button: the @OnClick listener of the generated binding calls onNextDayClick, which moves the date forward one day and redisplays the page',
  gui=['Tap the next day button (nextDayButton)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/PriceEditActivity.java:171-176 (@OnClick(R.id.nextDayButton) at 171; onNextDayClick 172-176); SRC res/layout/activity_price_edit.xml:187 (nextDayButton); auto_calls.json record PriceEditActivity_ViewBinding.java:64 ($4.doClick -> onNextDayClick, exact); INFERRED ButterKnife listener')

e('S_PRICE_EDIT', 'PriceEditActivity.onOptionsItemSelected', 'GUI',
  'tap the save icon in the toolbar (MenuHelper.save): save() writes the price and its history, then setResult(RESULT_OK) and finish()',
  gui=['Tap the save icon in the toolbar (MenuHelper.save)'],
  evidence='SRC investment/PriceEditActivity.java:101-109 (onCreateOptionsMenu; addSaveToolbarIcon at 106); SRC investment/PriceEditActivity.java:111-126 (onOptionsItemSelected; case MenuHelper.save at 118; save() at 120; setResult at 121; finish at 122); FW-SRC core/java/android/app/Activity.java:3439-3455 (onMenuItemSelected calls onOptionsItemSelected at 3450)')

e('S_PRICE_EDIT', 'PriceEditActivity.lambda$onDateClick$0', 'GUI',
  'tap the date field, then pick a date and tap OK in the date dialog: the dialog calls the OnDateSetListener lambda, which stores the new date and redisplays the page',
  gui=['Tap the date field (dateTextView), then pick a date and tap OK in the date dialog'],
  cls='non_standard', via='DatePickerDialog (framework): its positive button calls the OnDateSetListener (FW-SRC core/java/android/app/DatePickerDialog.java:122 and 164-171); the dialog is shown inside this page (D9)',
  evidence='SRC investment/PriceEditActivity.java:143-150 (onDateClick; DatePickerDialog listener lambda at 147-150); SRC investment/PriceEditActivity.java:21 import android.app.DatePickerDialog; FW-SRC core/java/android/app/DatePickerDialog.java:122 (positive button set to this), 164-171 (onClick; positive case 166; mDateSetListener.onDateSet at 171); auto_calls.json lambdas record PriceEditActivity.java:147 (onDateClick -> lambda$onDateClick$0; a different source, kept)')

# ---- RESULT: the calculator returns the amount to this activity

e('CalculatorActivity.returnResult', 'PriceEditActivity.onActivityResult', 'RESULT',
  'CalculatorActivity.returnResult (called at CalculatorActivity.java:149 and 249) sets the result and finishes; the framework delivers the result to the caller, which calls onActivityResult (framework delivery not read, INFERRED)',
  guard='resultCode is not RESULT_CANCELED and data is not null (PriceEditActivity.java:90, otherwise return); requestCode must be RequestCodes.AMOUNT (line 94); the AMOUNT branch reads the amount (95) and redisplays the page (97)',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult; setResult(AppCompatActivity.RESULT_OK, result) at 443; finish at 444); SRC common/Calculator.java:77-81 (show(requestCode) calls activity.startActivityForResult at 79); SRC investment/PriceEditActivity.java:87-99 (onActivityResult); framework delivery of the result not read (INFERRED)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE

sup(('PriceEditActivity_MembersInjector.create', 'PriceEditActivity_MembersInjector.<init>'),
    ('PriceEditActivity_MembersInjector.injectMembers', 'PriceEditActivity_MembersInjector.injectDateTimeUtilsLazy'))

# ================================================================== UNREACHABLE (batch 088). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['PriceEditActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (flags 0x1, takes the Provider). Its only caller record is create (auto_calls.json, PriceEditActivity_MembersInjector.java:23), and create has no caller: no class file has a Methodref to create, and the component (the only other class that names the injector) refers only to the static injectDateTimeUtilsLazy. The app source has no reference to the class.',
  'python-printed class-file parse of PriceEditActivity_MembersInjector.class (label_088.grep.txt section 4: METHODS list, Methodref hits); grep of the app source root (section 1); auto_calls.json record PriceEditActivity_MembersInjector.java:23 (section 5)',
  'INFERRED')

UNREACHABLE['PriceEditActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (flags 0x9). No caller: no class file has a Methodref to create (label_088.grep.txt section 4). The component calls the static injectDateTimeUtilsLazy directly (DaggerMmxComponent.injectPriceEditActivity, DaggerMmxComponent.java:410), not create. No app source reference (section 1).',
  'class-file parse (label_088.grep.txt section 4); auto_calls.json record DaggerMmxComponent.java:410 (section 5); grep of the app source root (section 1)',
  'INFERRED')

UNREACHABLE['PriceEditActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (flags 0x1, takes the PriceEditActivity). No caller: no class file has a Methodref to it (section 4), and the component refers only to the static injectDateTimeUtilsLazy. Its only outgoing record, injectMembers -> injectDateTimeUtilsLazy (PriceEditActivity_MembersInjector.java:28), is cut by the sup pair above. The synthetic bridge injectMembers(Object) (flags 0x1041) is not in this batch (open point in label_088.md).',
  'class-file parse (label_088.grep.txt section 4: METHODS list and Methodref hits); auto_calls.json record PriceEditActivity_MembersInjector.java:28 (section 5)',
  'INFERRED')

UNREACHABLE['PriceEditActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (flags 0x1, generated class only). ButterKnife.bind(this) at PriceEditActivity.java:70 discards the returned Unbinder, PriceEditActivity has no onDestroy, and no class file has a Methodref to unbind (section 4). No Unbinder reference exists in the app source (section 1), and no auto_calls.json record has unbind as dst (section 5).',
  'SRC investment/PriceEditActivity.java:70; label_088.grep.txt sections 1, 4, 5',
  'INFERRED')

UNREACHABLE['PriceCsvParser.getContext'] = ('no_trigger_in_app',
  'Public getter (PriceCsvParser.java:48-50) with no caller. The only use of the parser in app source is YahooCsvQuoteDownloaderRetrofit.java:113-116 (new PriceCsvParser(getContext()), then parser.parse(content)), and nothing asks the parser for its context. No Methodref to PriceCsvParser.getContext exists in any build class file (section 4), and auto_calls.json has no record with it as dst (section 5).',
  'SRC investment/PriceCsvParser.java:48-50; SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:113-116; label_088.grep.txt sections 2, 4, 5',
  'SOURCE')

# ---- part 089 (2026-10-29)
# ================================================================== batch 089 (label_089): 32 methods (graphs/MMEX/scratch/batches/batch_089.txt): PriceEditModel_MembersInjector (4), QuoteProviders (3), SecurityPriceModel.<init>, SecurityPriceUpdaterFactory (2), StocksCursorAdapter (3), StocksDataViewHolder.<init>, DummyContent (3 and DummyContent$DummyItem 2), AllPricesDownloadedEvent.<init>, PriceDownloadedEvent.<init>, PriceDownloadedEvent$$Parcelable (7 and its $1 with 3), PriceUpdateRequestEvent.<init>.
# Rows, printed lines and counts: graphs/MMEX/parts/label_089.md (13 REACHABLE, 19 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_089.grep.txt (sections A-E).
# This file writes:
#   - 0 SCREENS keys (no new screen: every batch method is a helper, a generated class or a Parcelable hook, D9);
#   - 2 e() edges, both FRAMEWORK (D7: no CALL edge already exists in auto_calls.json, and the two framework routes are not in auto_calls): WatchlistItemsFragment.onLoadFinished -> StocksCursorAdapter.newView and -> StocksCursorAdapter.bindView (both dst are owned by this batch, D1);
#   - 14 sup pairs (D14a): the auto CALL records whose caller is UNREACHABLE in this batch (PriceEditModel_MembersInjector.create and injectMembers, DummyContent.<clinit>, PriceDownloadedEvent$$Parcelable.writeToParcel, write, read, <clinit> and $1.createFromParcel);
#   - 19 UNREACHABLE entries: PriceEditModel_MembersInjector.<init>, create, injectMembers (generated, INFERRED); SecurityPriceUpdaterFactory.<init> (source, SOURCE); DummyContent.<clinit>, <init>, addItem, DummyContent$DummyItem.<init>, toString (source, SOURCE); PriceDownloadedEvent$$Parcelable.<clinit>, <init>, describeContents, getParcel, read, write, writeToParcel and PriceDownloadedEvent$$Parcelable$1.<init>, createFromParcel, newArray (generated, INFERRED).
# No new constants (D2).

# ---- framework edges: WatchlistItemsFragment.onLoadFinished hands the cursor to the adapter (changeCursor) and the framework then calls getView, which calls newView (no scrap view) and bindView (each visible row)

e('WatchlistItemsFragment.onLoadFinished', 'StocksCursorAdapter.newView', 'FRAMEWORK',
  'the loader result is handed to the adapter (adapter.changeCursor(data) swaps in the cursor and notifies the list); on the relayout the framework calls getView, which calls newView for a row that has no scrap view (the first layout of the data)',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:324-327 (onLoadFinished, changeCursor at 327); FW-SRC fw_src/android-8.1.0_r1/core/java/android/widget/CursorAdapter.java:348-353 (changeCursor calls swapCursor), 276-289 (getView calls newView at 285 when convertView is null); auto_calls framework_calls WatchlistItemsFragment.onLoadFinished lists StocksCursorAdapter.changeCursor but no newView or bindView record; INFERRED that StocksCursorAdapter uses the framework CursorAdapter behaviour (same pattern as label_087 PortfolioCursorAdapter)')

e('WatchlistItemsFragment.onLoadFinished', 'StocksCursorAdapter.bindView', 'FRAMEWORK',
  'the same relayout: the framework calls getView, which calls bindView for every visible row (the cursor columns are copied into the row views)',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:324-327; SRC investment/StocksCursorAdapter.java:71 (bindView); FW-SRC fw_src/android-8.1.0_r1/core/java/android/widget/CursorAdapter.java:289 (getView calls bindView); auto_calls framework_calls WatchlistItemsFragment.onLoadFinished lists no bindView record; INFERRED that StocksCursorAdapter uses the framework CursorAdapter behaviour (library not read)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('PriceEditModel_MembersInjector.create', 'PriceEditModel_MembersInjector.<init>'),
    ('PriceEditModel_MembersInjector.injectMembers', 'PriceEditModel_MembersInjector.injectDateTimeUtilsLazy'),
    ('DummyContent.<clinit>', 'DummyContent.addItem'),
    ('DummyContent.<clinit>', 'DummyContent$DummyItem.<init>'),
    ('PriceDownloadedEvent$$Parcelable.writeToParcel', 'PriceDownloadedEvent$$Parcelable.write'),
    ('PriceDownloadedEvent$$Parcelable.write', 'Money$$Parcelable.<clinit>'),
    ('PriceDownloadedEvent$$Parcelable.write', 'Money$$Parcelable.write'),
    ('PriceDownloadedEvent$$Parcelable.read', 'Money$$Parcelable.<clinit>'),
    ('PriceDownloadedEvent$$Parcelable.read', 'PriceDownloadedEvent.<init>'),
    ('PriceDownloadedEvent$$Parcelable.read', 'Money$$Parcelable.read'),
    ('PriceDownloadedEvent$$Parcelable.<clinit>', 'PriceDownloadedEvent$$Parcelable$1.<init>'),
    ('PriceDownloadedEvent$$Parcelable$1.createFromParcel', 'PriceDownloadedEvent$$Parcelable.<clinit>'),
    ('PriceDownloadedEvent$$Parcelable$1.createFromParcel', 'PriceDownloadedEvent$$Parcelable.<init>'),
    ('PriceDownloadedEvent$$Parcelable$1.createFromParcel', 'PriceDownloadedEvent$$Parcelable.read'))

# ================================================================== UNREACHABLE (batch 089). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['PriceEditModel_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only class-file referrer is create (grep section B1), and create has no referrer. The only auto record into <init> is create -> <init> (generated PriceEditModel_MembersInjector.java:23).',
  'class-file parse (label_089.grep.txt B1, C); auto_calls PriceEditModel_MembersInjector.java:23 (generated)',
  'INFERRED')

UNREACHABLE['PriceEditModel_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated factory method (takes the Provider and returns a MembersInjector). No class file refers to create. DaggerMmxComponent refers only to the static injectDateTimeUtilsLazy (auto_calls DaggerMmxComponent.java:495).',
  'class-file parse (label_089.grep.txt B1, C); auto_calls DaggerMmxComponent.java:495 (generated)',
  'INFERRED')

UNREACHABLE['PriceEditModel_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (takes the PriceEditModel). Its only class-file referrer is the bridge injectMembers(Object), and that bridge has no referrer. Its outgoing record injectMembers -> injectDateTimeUtilsLazy (generated PriceEditModel_MembersInjector.java:28) is cut by the sup pair above.',
  'class-file parse (label_089.grep.txt B1, C); auto_calls PriceEditModel_MembersInjector.java:28 (generated)',
  'INFERRED')

UNREACHABLE['SecurityPriceUpdaterFactory.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor of a class whose only use is the static getUpdaterInstance. The source has no constructor and no new SecurityPriceUpdaterFactory, and no class file refers to <init>.',
  'SRC investment/SecurityPriceUpdaterFactory.java:32 (no constructor); label_089.grep.txt A5, B1',
  'SOURCE')

UNREACHABLE['DummyContent.<clinit>'] = ('no_trigger_in_app',
  'Static initializer of the Android template class DummyContent. Only DummyContent.java names the class in src, and no class file refers to it. Its static block (addItem at lines 45-47) therefore never runs.',
  'SRC investment/dummy/DummyContent.java:31, 43-47; label_089.grep.txt A4, B1',
  'SOURCE')

UNREACHABLE['DummyContent.<init>'] = ('no_trigger_in_app',
  'Default constructor of the template class DummyContent. No class file refers to it, and src has no new DummyContent.',
  'SRC investment/dummy/DummyContent.java:31; label_089.grep.txt A4, B1',
  'SOURCE')

UNREACHABLE['DummyContent.addItem'] = ('no_trigger_in_app',
  'Private static helper called only from the DummyContent static block (lines 45-47; auto_calls DummyContent.java:47). That block is unreachable (see DummyContent.<clinit>).',
  'SRC investment/dummy/DummyContent.java:43-50; auto_calls DummyContent.java:47',
  'SOURCE')

UNREACHABLE['DummyContent$DummyItem.<init>'] = ('no_trigger_in_app',
  'Constructed only by the DummyContent static block (lines 45-47; auto_calls DummyContent.java:47), which is unreachable.',
  'SRC investment/dummy/DummyContent.java:45-47, 58, 62; auto_calls DummyContent.java:47',
  'SOURCE')

UNREACHABLE['DummyContent$DummyItem.toString'] = ('no_trigger_in_app',
  'No DummyItem instance is ever created, and no class file refers to toString.',
  'SRC investment/dummy/DummyContent.java:58, 68; label_089.grep.txt B1',
  'SOURCE')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.<clinit>'] = ('no_trigger_in_app',
  'Static initializer of the parceler-generated wrapper. Its only class-file referrer is PriceDownloadedEvent$$Parcelable$1.createFromParcel (CREATOR construction). The wrapper exists only through Parcels.wrap in PriceDownloadedEventBundler.put (line 37), which is reached only from EditPriceDialog Icepick state, and EditPriceDialog is never constructed (label_089.grep.txt A1).',
  'SRC core/bundlers/PriceDownloadedEventBundler.java:37; SRC investment/EditPriceDialog.java:83, 89-91; class-file parse (label_089.grep.txt B1, C); auto_calls PriceDownloadedEvent$$Parcelable.java:22 (generated)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.<init>'] = ('framework_never_calls',
  'Constructed only in PriceDownloadedEvent$$Parcelable$1.createFromParcel (auto_calls generated line 27). createFromParcel is the Parcelable.Creator the framework calls when it reads a Parcel that holds this type, and such a Parcel is produced only by the dead Parcels.wrap path.',
  'class-file parse (label_089.grep.txt B1, C); auto_calls PriceDownloadedEvent$$Parcelable.java:27 (generated); SRC core/bundlers/PriceDownloadedEventBundler.java:37',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.describeContents'] = ('framework_never_calls',
  'Parcelable method. The framework calls it from Bundle.hasFileDescriptors (Bundle.java:329-330) only for a Parcelable value stored in a Bundle. The only putParcelable of this type is PriceDownloadedEventBundler.java:37, which is dead. No class file refers to describeContents.',
  'FW-SRC fw_src/android-8.1.0_r1/core/java/android/os/Bundle.java:316-332 (call at 329-330); SRC core/bundlers/PriceDownloadedEventBundler.java:37; class-file parse (label_089.grep.txt C)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.getParcel'] = ('no_trigger_in_app',
  'Accessor called by the parceler library through the bridge getParcel()Object. The library calls it only from Parcels.wrap and Parcels.unwrap, whose call sites in src are PriceDownloadedEventBundler.java:37 and 43, both dead. The bridge has no referrer (class-file parse). The library call is INFERRED (library jar not in repo).',
  'SRC core/bundlers/PriceDownloadedEventBundler.java:37, 43; class-file parse (label_089.grep.txt C)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.read'] = ('framework_never_calls',
  'Called only by PriceDownloadedEvent$$Parcelable$1.createFromParcel (auto_calls generated line 27). It is reached only through the framework Creator path.',
  'class-file parse (label_089.grep.txt B1, C); auto_calls PriceDownloadedEvent$$Parcelable.java:27, 80, 83 (generated)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.write'] = ('framework_never_calls',
  'Called only by PriceDownloadedEvent$$Parcelable.writeToParcel (auto_calls generated line 44). writeToParcel is reached only through the framework Parcelable path.',
  'class-file parse (label_089.grep.txt C); auto_calls PriceDownloadedEvent$$Parcelable.java:44 (generated)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable.writeToParcel'] = ('framework_never_calls',
  'Parcelable.writeToParcel. Parcel.writeParcelable calls it (Parcel.java:1791) when a Parcel carries this object. The only object is made by the dead Parcels.wrap path. No class file refers to writeToParcel.',
  'FW-SRC fw_src/android-8.1.0_r1/core/java/android/os/Parcel.java:1785-1791 (call at 1791); SRC core/bundlers/PriceDownloadedEventBundler.java:37; class-file parse (label_089.grep.txt C)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable$1.<init>'] = ('no_trigger_in_app',
  'Constructed by the CREATOR field initializer in PriceDownloadedEvent$$Parcelable.<clinit> (auto_calls generated line 22). That class initialisation is unreachable (see PriceDownloadedEvent$$Parcelable.<clinit>).',
  'class-file parse (label_089.grep.txt B1, C); auto_calls PriceDownloadedEvent$$Parcelable.java:22 (generated)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable$1.createFromParcel'] = ('framework_never_calls',
  'Parcelable.Creator method. The framework calls it through Parcel.readParcelable (Parcel.java:2842; readParcelableCreator at 2867) only when a Parcel holds this type. The only such Parcel comes from the dead Parcels.wrap path.',
  'FW-SRC fw_src/android-8.1.0_r1/core/java/android/os/Parcel.java:2841-2842, 2867; class-file parse (label_089.grep.txt C)',
  'INFERRED')

UNREACHABLE['PriceDownloadedEvent$$Parcelable$1.newArray'] = ('framework_never_calls',
  'Parcelable.Creator.newArray. The framework calls it from Parcel.createTypedArray (Parcel.java:2645) only when a typed array of this type is read. That needs the dead path.',
  'FW-SRC fw_src/android-8.1.0_r1/core/java/android/os/Parcel.java:2640-2645 (newArray at 2645); class-file parse (label_089.grep.txt C)',
  'INFERRED')

# ---- part 090 (2026-10-29)
# ================================================================== batch 090 (label_090): MorningstarPriceUpdater (7 methods), MorningstarPriceUpdater$1 (4), MorningstarPriceUpdater$2 (2), MorningstarPriceUpdater_Factory (4), MorningstarPriceUpdater_MembersInjector (5), SymbolConverter (4), ExchangeRateUpdaterBase (1), FixerService (6), FixerService$1 (3). 36 methods in all (graphs/MMEX/scratch/batches/batch_090.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_090.md (28 REACHABLE, 8 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_090.grep.txt (sections 1-6).
# This file writes:
#   - 6 e() edges (FRAMEWORK): processInParallel -> MorningstarPriceUpdater$1.onNext, onCompleted, onError; processInParallel -> MorningstarPriceUpdater$2.call (RxJava callbacks, library dispatch INFERRED); FixerService.downloadPrices -> FixerService$1.onResponse, onFailure (Retrofit callbacks, library dispatch INFERRED);
#   - 9 sup pairs (D14a): the auto CALL records whose caller is UNREACHABLE (Factory.create, Factory.get, Factory.newMorningstarPriceUpdater, MembersInjector.create, MembersInjector.injectMembers, ExchangeRateUpdaterBase.<init>);
#   - 8 UNREACHABLE entries: Factory.<init>, Factory.create, Factory.get, Factory.newMorningstarPriceUpdater, MembersInjector.<init>, create, injectMembers (generated, INFERRED, grep.txt sections 4-5); ExchangeRateUpdaterBase.<init> (app source, SOURCE).
# No SCREENS key (no new screen). No new constants (D2). Not written: no CALL edge that is already in auto_calls.json (D7). The watchlist and currency entry points stay interim (batches 092, 094 and the currency batches, not merged; D8).

e('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$1.onNext', 'FRAMEWORK',
  'RxJava calls the Subscriber onNext for each emitted value; the method updates progress (line 213)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:193-213 (Subscriber created at 193; onNext at 211-213); INFERRED RxJava Subscriber dispatch (library not read); auto_calls.json record MorningstarPriceUpdater$1.onNext -> PriceUpdaterBase.setProgress (line 213)',
  via='RxJava Subscriber callback (library not read, INFERRED)')

e('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$1.onCompleted', 'FRAMEWORK',
  'RxJava calls the Subscriber onCompleted when the observable completes; the method calls finishIfAllDone (line 197)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:193-213 (Subscriber created at 193; onCompleted at 196-197); INFERRED RxJava Subscriber dispatch (library not read); auto_calls.json record MorningstarPriceUpdater$1.onCompleted -> MorningstarPriceUpdater.finishIfAllDone (line 197)',
  via='RxJava Subscriber callback (library not read, INFERRED)')

e('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$1.onError', 'FRAMEWORK',
  'RxJava calls the Subscriber onError when a request fails; the method sets progress and calls finishIfAllDone (line 207)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:193-213 (Subscriber created at 193; onError at 201-207); INFERRED RxJava Subscriber dispatch (library not read); auto_calls.json record MorningstarPriceUpdater$1.onError -> MorningstarPriceUpdater.finishIfAllDone (line 207)',
  via='RxJava Subscriber callback (library not read, INFERRED)')

e('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$2.call', 'FRAMEWORK',
  'RxJava calls the Action1 (doOnNext) for each emitted value; the body calls parse (line 189) and savePrice (line 190)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:185-191 (doOnNext Action1 created at 186; call at 188-191); INFERRED RxJava Action1 dispatch (library not read); auto_calls.json records MorningstarPriceUpdater$2.call -> MorningstarPriceUpdater.parse (line 189) and -> savePrice (line 190)',
  via='RxJava Action1 callback (library not read, INFERRED)')

e('FixerService.downloadPrices', 'FixerService$1.onResponse', 'FRAMEWORK',
  'Retrofit calls the Callback onResponse with the response; the method calls onContentDownloaded (line 79)',
  evidence='SRC investment/prices/FixerService.java:76-80 (anonymous Callback created at 76; onResponse at 78-79); SRC investment/prices/FixerService.java:93 (enqueue(callback)); INFERRED Retrofit enqueue callback dispatch (library not read); auto_calls.json record FixerService$1.onResponse -> FixerService.onContentDownloaded (line 79)',
  via='Retrofit enqueue callback (library not read, INFERRED)')

e('FixerService.downloadPrices', 'FixerService$1.onFailure', 'FRAMEWORK',
  'Retrofit calls the Callback onFailure when the request fails; the method closes the progress dialog (line 84)',
  evidence='SRC investment/prices/FixerService.java:83-84 (onFailure; closeProgressDialog at 84); SRC investment/prices/FixerService.java:93 (enqueue(callback)); INFERRED Retrofit enqueue callback dispatch (library not read); auto_calls.json record FixerService$1.onFailure -> PriceUpdaterBase.closeProgressDialog (line 84)',
  via='Retrofit enqueue callback (library not read, INFERRED)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE

sup(('MorningstarPriceUpdater_Factory.create', 'MorningstarPriceUpdater_Factory.<init>'),
    ('MorningstarPriceUpdater_Factory.get', 'MorningstarPriceUpdater_MembersInjector.injectStockHistoryRepository'),
    ('MorningstarPriceUpdater_Factory.get', 'MorningstarPriceUpdater_MembersInjector.injectStockRepository'),
    ('MorningstarPriceUpdater_Factory.get', 'MorningstarPriceUpdater.<init>'),
    ('MorningstarPriceUpdater_Factory.newMorningstarPriceUpdater', 'MorningstarPriceUpdater.<init>'),
    ('MorningstarPriceUpdater_MembersInjector.create', 'MorningstarPriceUpdater_MembersInjector.<init>'),
    ('MorningstarPriceUpdater_MembersInjector.injectMembers', 'MorningstarPriceUpdater_MembersInjector.injectStockHistoryRepository'),
    ('MorningstarPriceUpdater_MembersInjector.injectMembers', 'MorningstarPriceUpdater_MembersInjector.injectStockRepository'),
    ('ExchangeRateUpdaterBase.<init>', 'PriceUpdaterBase.<init>'))

# ================================================================== UNREACHABLE (batch 090). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['MorningstarPriceUpdater_Factory.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (flags 0x1, takes three Providers). Its only caller record is create (auto_calls.json, MorningstarPriceUpdater_Factory.java:45), and create has no caller: no class file has a Methodref to create or to the Factory, and the component refers only to the MembersInjector. The app source has no reference to the class.',
  'label_090.grep.txt section 4 (METHODS list; line 214: no class refers to the Factory) and section 1; auto_calls.json record MorningstarPriceUpdater_Factory.java:45 (section 5, line 286)',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_Factory.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory method (flags 0x9). No caller: no class file has a Methodref to create (label_090.grep.txt section 4), and DaggerMmxComponent refers only to the MembersInjector inject methods (lines 141-142), not to the Factory. No app source reference (section 1).',
  'class-file parse (label_090.grep.txt section 4, lines 141-142 and 214); grep of the app source root (section 1)',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_Factory.get'] = ('no_trigger_in_app',
  'Dagger-generated provider method (flags 0x1). Its only entry is create, which has no caller. Its outgoing records (to MorningstarPriceUpdater.<init> and to the two MembersInjector inject methods) are cut by the sup pairs above.',
  'auto_calls.json records MorningstarPriceUpdater_Factory.java:33, 34, 36 (label_090.grep.txt section 5, lines 283-285); section 4 line 214',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_Factory.newMorningstarPriceUpdater'] = ('no_trigger_in_app',
  'Dagger-generated static method (flags 0x9). No class file has a Methodref to it (label_090.grep.txt section 4). Its only outgoing record, to MorningstarPriceUpdater.<init>, is cut by the sup pair above.',
  'auto_calls.json record MorningstarPriceUpdater_Factory.java:50 (label_090.grep.txt section 5, line 287); section 4',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (flags 0x1, takes the two Providers). Its only caller record is create (auto_calls.json, MorningstarPriceUpdater_MembersInjector.java:31), and create has no caller (see create below).',
  'auto_calls.json record MorningstarPriceUpdater_MembersInjector.java:31 (label_090.grep.txt section 5, line 277); section 4 line 215',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory method (flags 0x9). No class file has a Methodref to create (label_090.grep.txt section 4). DaggerMmxComponent calls the static inject methods directly (DaggerMmxComponent.java:502 and 504), not create. No app source reference (section 1).',
  'class-file parse (label_090.grep.txt section 4, lines 141-142 and 215); auto_calls.json record MorningstarPriceUpdater_MembersInjector.java:31 (section 5, line 277); grep of the app source root (section 1)',
  'INFERRED')

UNREACHABLE['MorningstarPriceUpdater_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (flags 0x1, takes the updater). No class file has a Methodref to it (label_090.grep.txt section 4), and the component refers only to the static inject methods. Its outgoing records (to injectStockRepository at line 37 and injectStockHistoryRepository at line 38) are cut by the sup pairs above. The synthetic bridge injectMembers(Object) (flags 0x1041) is not in this batch (open point in label_090.md).',
  'class-file parse (label_090.grep.txt section 4, line 107); auto_calls.json records MorningstarPriceUpdater_MembersInjector.java:37-38 (section 5, lines 278-279)',
  'INFERRED')

UNREACHABLE['ExchangeRateUpdaterBase.<init>'] = ('no_trigger_in_app',
  'Constructor of a base class (ExchangeRateUpdaterBase.java:26-30) with no subclass and no referencing class: the app source has no reference to the class other than its own declaration, and no build class file refers to it (label_090.grep.txt section 4, line 210). Its only outgoing record, to PriceUpdaterBase.<init> (ExchangeRateUpdaterBase.java:29), is cut by the sup pair above.',
  'SRC investment/prices/ExchangeRateUpdaterBase.java:26-30; label_090.grep.txt sections 1, 4 (line 210), 5 (line 248)',
  'SOURCE')

# ---- part 091 (2026-10-29)
# batch 091: PriceUpdaterBase (5 methods), SecurityPriceUpdaterBase (2) and WatchlistDataset (3).
# No e() edges: each REACHABLE method here already has its incoming CALL record in auto_calls.json, so the edge is kept from the auto set (D7).
# UNREACHABLE entries and sup pairs only. Rows and printed lines: graphs/MMEX/parts/label_091.md. Grep evidence: graphs/MMEX/parts/label_091.grep.txt.
# Each sup pair here has its destination in this batch, so this batch's owner writes it (D17(b)). The two WatchlistFragment sups cut a CHA record from a REACHABLE caller, the same pattern as batch 006 (D14).

UNREACHABLE['SecurityPriceUpdaterBase.<init>'] = (
  'no_trigger_in_app',
  'Constructor of SecurityPriceUpdaterBase, a concrete class (SecurityPriceUpdaterBase.java:28-33). No source line creates it, and no class extends it: YahooCsv, Morningstar, Yql, FixerService and ExchangeRateUpdaterBase extend PriceUpdaterBase directly. No class file other than its own references it, and no auto_calls.json record targets it.',
  'label_091.grep.txt:6-8, 10-34, 36-46; auto_calls.json:13114',
  'SOURCE')

UNREACHABLE['SecurityPriceUpdaterBase.downloadPrices'] = (
  'no_trigger_in_app',
  'Empty override of ISecurityPriceUpdater.downloadPrices (SecurityPriceUpdaterBase.java:35-38). The interface calls in WatchlistFragment (lines 363 and 474) list it as a CHA target, but the receiver is always a YahooCsv, Morningstar or Yql instance (SecurityPriceUpdaterFactory.java:42, 45, 48, 52), and no SecurityPriceUpdaterBase instance can exist. The three real overrides keep their own CHA records from the same callers, so the cut does not orphan them.',
  'SecurityPriceUpdaterFactory.java:40-52; WatchlistFragment.java:362-363, 472-474; auto_calls.json:14230-14231, 15234-15235; label_091.grep.txt:6-8, 36-46',
  'SOURCE')

UNREACHABLE['WatchlistDataset.<init>'] = (
  'no_trigger_in_app',
  'Constructor of WatchlistDataset, which extends Dataset (WatchlistDataset.java:32-40). No source line creates it (its only source lines are the declaration and this constructor), and no class file other than its own references it. No auto_calls.json record targets it. Its outgoing records (auto_calls.json:15292-15316) call methods owned by other batches, which have other callers, so they stay with those owners.',
  'WatchlistDataset.java:32-40; label_091.grep.txt:36-50; auto_calls.json:15292-15316',
  'SOURCE')

UNREACHABLE['WatchlistDataset.getAllColumns'] = (
  'no_trigger_in_app',
  'Override of the abstract Dataset.getAllColumns (Dataset.java:52). It runs only on a WatchlistDataset instance, and none is created (WatchlistDataset.<init>). The receivers of the getAllColumns calls in the source are concrete classes, none typed Dataset or RepositoryBase, so no CHA route reaches it. No incoming auto_calls.json record.',
  'WatchlistDataset.java:44-55; Dataset.java:52; label_091.grep.txt:56-70',
  'SOURCE')

UNREACHABLE['WatchlistDataset.getWatchlistSqlQuery'] = (
  'no_trigger_in_app',
  'Public method (WatchlistDataset.java:57-60). The only source line naming it is its declaration, so no source code calls it, and it runs only on a WatchlistDataset instance, which is never created. No incoming auto_calls.json record. Its outgoing records (auto_calls.json:15324, 15332) stay with the owners of MmxFileUtils.',
  'WatchlistDataset.java:57-60; label_091.grep.txt:53-54; auto_calls.json:15324-15332',
  'SOURCE')

# The dead constructor's bytecode call into PriceUpdaterBase.<init> cannot run; PriceUpdaterBase.<init> stays REACHABLE through the YahooCsv, Morningstar and Yql constructors (auto_calls.json:13342, 13502, 15406).
sup(('SecurityPriceUpdaterBase.<init>', 'PriceUpdaterBase.<init>'))

# The CHA records from the two REACHABLE WatchlistFragment callers to the unreachable base method are cut. The three real overrides keep their own CHA records from the same callers (auto_calls.json:14206-14222, 15210-15226).
sup(('WatchlistFragment.onPriceUpdateRequested', 'SecurityPriceUpdaterBase.downloadPrices'))
sup(('WatchlistFragment$4.onClick', 'SecurityPriceUpdaterBase.downloadPrices'))

# ---- part 092 (2026-10-29)
# ---- batch 092: WatchlistFragment (methods 1-40 of 55; WatchlistFragment$1 and $2 included).
# Edges are written for the destinations that this batch owns (D1). CALL edges already in auto_calls.json are not repeated (D7).
# UNREACHABLE entries: none. All 40 methods are REACHABLE (label_092.md, label_092.grep.txt).
# sup pairs: none (no UNREACHABLE caller in this batch).

SCREENS.update({
    'S_WATCHLIST': 'Watchlist screen (WatchlistFragment, shown inside MainActivity for one investment account): the account header with the favourite star, the account spinner in the action bar, the list of watched securities, and the options menu (update prices, export prices, purge history, change provider)',
})

# ---- fragment lifecycle and screen entry

e('WatchlistFragment.<init>', 'WatchlistFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor',
  evidence='SRC investment/watchlist/WatchlistFragment.java:93-125; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onCreate', 'WatchlistFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC WatchlistFragment.java:115-125, 142; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onCreateView', 'S_WATCHLIST', 'ENTERS',
  'the watchlist screen is shown: onCreateView inflates the layout and replaces the list fragment in fragmentMain',
  evidence='SRC WatchlistFragment.java:148 (layout inflate), 159-172 (child fragment replace at 171-172)')

e('WatchlistFragment.onCreateView', 'WatchlistFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onCreateView',
  evidence='SRC WatchlistFragment.java:142-183, 186-194; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onActivityCreated', 'WatchlistFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after onActivityCreated',
  evidence='SRC WatchlistFragment.java:128-132, 186-194; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onStart', 'WatchlistFragment.onResume', 'LIFECYCLE',
  'the framework calls onResume after onStart',
  evidence='SRC WatchlistFragment.java:128-132, 197-205; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onResume', 'WatchlistFragment.onStop', 'LIFECYCLE',
  'the framework calls onStop when the watchlist screen is left (after onPause, which is not in this batch)',
  evidence='SRC WatchlistFragment.java:135-139; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistFragment.onResume', 'WatchlistFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state while the watchlist screen is shown or left',
  evidence='SRC WatchlistFragment.java:277-281; same pattern as AccountTransactionListFragment (graph_def.py:823); INFERRED androidx Fragment lifecycle (library source not read)')

# ---- options menu

e('WatchlistFragment.onCreateView', 'WatchlistFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'the fragment has its options menu enabled, so the host activity calls onCreateOptionsMenu when it builds its options menu',
  guard='setHasOptionsMenu(true) at line 178 has run (in onCreateView)',
  evidence='SRC WatchlistFragment.java:178, 213-245; INFERRED androidx FragmentManager dispatch (library source not read)')

gui('S_WATCHLIST', 'WatchlistFragment.onOptionsItemSelected',
    'Tap an item of the options menu of the watchlist screen: update prices, export prices, purge history or change provider',
    evidence='SRC res/menu/menu_watchlist.xml (menu_update_prices, menu_export_prices, menu_purge_history, menu_change_provider); SRC WatchlistFragment.java:254-274; INFERRED androidx FragmentManager dispatch (library source not read)')

# ---- the provider dialog opened by Change provider (the list click is dispatched by the platform AlertController)

gui('S_WATCHLIST', 'WatchlistFragment$1.onClick',
    'Tap a provider name in the quote provider dialog that the Change provider menu item opens',
    cls='non_standard',
    via='platform AlertDialog single-choice list: AlertController.java:1138-1142 calls mOnClickListener.onClick on an item click (FW-SRC read)',
    evidence='SRC WatchlistFragment.java:384-398 (setSingleChoiceItems at 386, onClick at 388-396); FW-SRC core/java/android/app/AlertDialog.java:936-941; FW-SRC core/java/com/android/internal/app/AlertController.java:1112, 1138-1142')

# ---- the update runnable is run on the UI thread by the platform

e('WatchlistFragment.completePriceUpdate', 'WatchlistFragment$2.run', 'FRAMEWORK',
  'getActivity().runOnUiThread runs the Runnable directly when the caller is already on the UI thread, otherwise it posts the Runnable to the handler',
  evidence='SRC WatchlistFragment.java:402-413 (runOnUiThread at 404, run at 406); FW-SRC core/java/android/app/Activity.java:6170-6176')

# ---- EventBus: registered in onStart (line 131), unregistered in onStop (line 138); the subscribers are the four @Subscribe methods

e('WatchlistFragment.onStart', 'WatchlistFragment.onEvent(AllPricesDownloadedEvent)', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe method receives AllPricesDownloadedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at line 131, unregister at line 138, @Subscribe at line 285 (library source not read, INFERRED)',
  evidence='SRC WatchlistFragment.java:128-139, 285-288; INFERRED EventBus library source not read')

e('WatchlistFragment.onStart', 'WatchlistFragment.onEvent(PriceDownloadedEvent)', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe method receives PriceDownloadedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at line 131, unregister at line 138, @Subscribe at line 290 (library source not read, INFERRED)',
  evidence='SRC WatchlistFragment.java:128-139, 290-293; INFERRED EventBus library source not read')

e('WatchlistFragment.onStart', 'WatchlistFragment.onEvent(PriceUpdateRequestEvent)', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe method receives PriceUpdateRequestEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at line 131, unregister at line 138, @Subscribe at line 295 (library source not read, INFERRED)',
  evidence='SRC WatchlistFragment.java:128-139, 295-298; INFERRED EventBus library source not read')

e('WatchlistFragment.onStart', 'WatchlistFragment.onEvent(ErrorRaisedEvent)', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe method receives ErrorRaisedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at line 131, unregister at line 138, @Subscribe at line 300 (library source not read, INFERRED)',
  evidence='SRC WatchlistFragment.java:128-139, 300-303; INFERRED EventBus library source not read')

# ---- state gates for the price providers (InvestmentSettings.getQuoteProvider; the default is YahooYql at line 75)

STATE_YAHOO_CSV = state_text('the quote provider setting is YahooCsv (set in the Change provider dialog)', ('settings',))
STATE_MORNINGSTAR = state_text('the quote provider setting is Morningstar (set in the Change provider dialog)', ('settings',))
STATE_YAHOO_YQL = state_text('the quote provider setting is YahooYql (the default when the setting is unset)', ('settings',))

ENV_ERROR_LOGGED = env_text(
    'an error is logged through Timber while the watchlist fragment is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)',
    ('other',))

# ---- ASYNC: EventBus posts from the price downloaders, the watchlist items and the Timber trees into the subscribers

e('YahooCsvQuoteDownloaderRetrofit.finishIfAllDone', 'WatchlistFragment.onEvent(AllPricesDownloadedEvent)', 'ASYNC',
  'the CSV downloader posts AllPricesDownloadedEvent when every symbol is done; the registered watchlist fragment reloads its data',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  needs_state=STATE_YAHOO_CSV,
  cls='non_standard', via='EventBus post at YahooCsvQuoteDownloaderRetrofit.java:100 to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:91-100 (post at 100); SRC WatchlistFragment.java:131, 285-288; SRC settings/InvestmentSettings.java:74-86')

e('MorningstarPriceUpdater.finishIfAllDone', 'WatchlistFragment.onEvent(AllPricesDownloadedEvent)', 'ASYNC',
  'the Morningstar updater posts AllPricesDownloadedEvent when every symbol is done; the registered watchlist fragment reloads its data',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  needs_state=STATE_MORNINGSTAR,
  cls='non_standard', via='EventBus post at MorningstarPriceUpdater.java:274 to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:263-275 (post at 274); SRC WatchlistFragment.java:131, 285-288; SRC investment/SecurityPriceUpdaterFactory.java:41-42')

e('YahooCsvQuoteDownloaderRetrofit.onContentDownloaded', 'WatchlistFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'the CSV downloader posts the parsed PriceDownloadedEvent for a downloaded quote (only when the parse succeeded)',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  needs_state=STATE_YAHOO_CSV,
  cls='non_standard', via='EventBus post at YahooCsvQuoteDownloaderRetrofit.java:124 (post(event)) to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:103-125 (post at 124); SRC WatchlistFragment.java:290-293')

e('YqlSecurityPriceUpdaterRetrofit.onContentDownloaded', 'WatchlistFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'the YQL downloader (the default provider) posts a PriceDownloadedEvent for each downloaded symbol; the registered watchlist fragment updates the price',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  needs_state=STATE_YAHOO_YQL,
  cls='non_standard', via='EventBus post at YqlSecurityPriceUpdaterRetrofit.java:130 to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/yql/YqlSecurityPriceUpdaterRetrofit.java:113-131 (post at 130); SRC investment/SecurityPriceUpdaterFactory.java:44-45, 50-52; SRC settings/InvestmentSettings.java:75; SRC WatchlistFragment.java:290-293')

e('FixerService.onContentDownloaded', 'WatchlistFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'FixerService posts a PriceDownloadedEvent for each currency rate it downloads; EventBus also delivers it to the registered watchlist fragment, which then runs onPriceDownloaded with the currency code',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  cls='non_standard', via='EventBus post at FixerService.java:120 to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/prices/FixerService.java:100-121 (post at 120); SRC WatchlistFragment.java:290-293, 330-337; INFERRED EventBus library dispatch (library source not read)')

e('WatchlistItemsFragment.onContextItemSelected', 'WatchlistFragment.onEvent(PriceUpdateRequestEvent)', 'ASYNC',
  'the user chooses Download price in the context menu of a watchlist row; EventBus delivers PriceUpdateRequestEvent to the registered watchlist fragment',
  guard='the fragment is registered: onStart has run and onStop has not (lines 131 and 138)',
  cls='non_standard', via='EventBus post at WatchlistItemsFragment.java:236 to the subscriber registered in onStart (library dispatch, INFERRED)',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:215-238 (post at 236); SRC WatchlistFragment.java:131, 295-298')

e('DebugTree.log', 'WatchlistFragment.onEvent(ErrorRaisedEvent)', 'ASYNC',
  'a debug build logs an error through Timber while the watchlist fragment is registered: DebugTree posts ErrorRaisedEvent and EventBus calls onEvent, which shows a toast',
  env=ENV_ERROR_LOGGED,
  guard='the fragment is registered (lines 131 and 138), and DebugTree posts only when a subscriber exists (DebugTree.java:45)',
  cls='non_standard', via='EventBus post at DebugTree.java:46 to the @Subscribe method onEvent(ErrorRaisedEvent) (library dispatch, INFERRED)',
  evidence='SRC log/DebugTree.java:34-47 (minLevel INFO, post at 46); SRC MmexApplication.java:134-135 (DebugTree planted in the debug branch); SRC WatchlistFragment.java:300-303')

e('ScreenTree.log', 'WatchlistFragment.onEvent(ErrorRaisedEvent)', 'ASYNC',
  'a release build logs an error through Timber while the watchlist fragment is registered: ScreenTree posts ErrorRaisedEvent and EventBus calls onEvent, which shows a toast',
  env=ENV_ERROR_LOGGED,
  guard='the fragment is registered (lines 131 and 138), and ScreenTree posts only when a subscriber exists (ScreenTree.java:26)',
  cls='non_standard', via='EventBus post at ScreenTree.java:27 to the @Subscribe method onEvent(ErrorRaisedEvent) (library dispatch, INFERRED)',
  evidence='SRC log/ScreenTree.java:15-28 (minLevel INFO, post at 27); SRC MmexApplication.java:136-139 (ScreenTree planted in the release branch); SRC WatchlistFragment.java:300-303')

# ---- part 093 (2026-10-29)
# ---- batch 093: WatchlistFragment anonymous listeners $3 to $9 (15 methods; rows in label_093.md, evidence in label_093.grep.txt)
# Edges are written only for destinations owned by this batch (D1). The <init> methods have auto CALL records in auto_calls.json, so no edge is written for them (D7).
# SCREENS: none written here. S_WATCHLIST is defined by batch 092 (label_092.py:7) and reused for the page of these listeners.
# UNREACHABLE entries: none (all 15 methods are REACHABLE). sup pairs: none. The sup for WatchlistFragment$4.onClick -> SecurityPriceUpdaterBase.downloadPrices is in label_091.py:41.
# Mapping of the anonymous class numbers to the listeners rests on the class-file refs (grep.txt section 1), not on the auto_calls line numbers, which differ by one or more lines from the new expressions (grep.txt sections 2 and 3).

# ---- the two confirmation dialogs opened from the options menu (D9: shown on the watchlist page)

gui('S_WATCHLIST', 'WatchlistFragment$3.onClick',
    'Tap Update prices in the options menu, then Cancel in the confirmation dialog',
    cls='non_standard',
    via='platform AlertDialog negative button: AlertController ButtonHandler sends the click to the OnClickListener (FW-SRC AlertController.java:125-145, 160-166; setButton 344-360)',
    evidence='SRC investment/watchlist/WatchlistFragment.java:478-483 (setNegativeButton at 478; onClick 480-482; dismiss 481); SRC res/menu/menu_watchlist.xml:22-26 (menu_update_prices); SRC WatchlistFragment.java:258 (confirmPriceUpdate); class file WatchlistFragment$3 refs DialogInterface.dismiss only (grep.txt section 1)')

gui('S_WATCHLIST', 'WatchlistFragment$4.onClick',
    'Tap Update prices in the options menu, then OK in the confirmation dialog (downloads the prices of the shown securities)',
    cls='non_standard',
    via='platform AlertDialog positive button: same dispatch as the Cancel button (AlertController.java:160-166)',
    evidence='SRC WatchlistFragment.java:463-477 (setPositiveButton at 463; onClick 465-476; getAllShownSymbols 467; getUpdaterInstance 473; downloadPrices 474); SRC res/menu/menu_watchlist.xml:22-26; auto_calls.json records WatchlistFragment$4.onClick -> getAllShownSymbols (467), getUpdaterInstance (473), downloadPrices (474, cha); class file WatchlistFragment$4 refs downloadPrices (grep.txt sections 1-2)')

# ---- the account spinner in the action bar (a standard AdapterView selection, as in AccountTransactionListFragment$3.onItemSelected, graph_def.py:1155)

gui('S_WATCHLIST', 'WatchlistFragment$5.onItemSelected',
    'Pick an investment account in the account spinner of the action bar',
    evidence='SRC investment/watchlist/WatchlistFragment.java:514-538 (action bar 514; spinner 522; setOnItemSelectedListener 530; onItemSelected 532-539, switchAccount at 538); FW-SRC core/java/android/widget/AdapterView.java:903-930 (selectionChanged), 937-949 (fireOnSelected calls onItemSelected at 944)')

e('WatchlistFragment.selectCurrentAccount', 'WatchlistFragment$5.onItemSelected', 'FRAMEWORK',
  'selectCurrentAccount selects the row of the current account (spinner.setSelection at line 671); when the selected row changes, the framework calls onItemSelected for the new row, which calls switchAccount (switchAccount returns early at line 675 when the account is unchanged)',
  guard='the current account is a row of the spinner (loop at 659-669), and its position differs from the previous selection (AdapterView.java:1104-1106)',
  evidence='SRC investment/watchlist/WatchlistFragment.java:650-672 (position loop 659-669; setSelection 671), 674-675 (switchAccount early return); FW-SRC core/java/android/widget/AdapterView.java:1103-1115 (checkSelectionChanged; selectionChanged at 1105), 937-949 (fireOnSelected; onItemSelected at 944); AbsSpinner.java is not in fw_src (the path from setSelection to checkSelectionChanged is INFERRED)')

e('WatchlistFragment.selectCurrentAccount', 'WatchlistFragment$5.onNothingSelected', 'FRAMEWORK',
  'selectCurrentAccount finds no row for the current account, so position stays Constants.NOT_SET (-1) and spinner.setSelection(-1) clears the selected row; the framework then calls onNothingSelected (empty body)',
  needs_state=state_text('the spinner had a valid selected row before this call (the framework fires onNothingSelected only when the selection changes to none), and the current account is not one of its rows (WatchlistFragment.java:659-669)', ('account',)),
  evidence='SRC investment/watchlist/WatchlistFragment.java:541-544 (empty onNothingSelected), 659 (position = NOT_SET), 661-669 (row loop), 671 (setSelection); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onNothingSelected for a negative position, at 947), 1103-1115 (checkSelectionChanged fires only on a change, 1104-1106), 1086-1093 (nothing-selected branch in handleDataChanged, checkSelectionChanged at 1093); Constants.java:22 (NOT_SET = -1); AbsSpinner.java is not in fw_src, so the setSelection(-1) to checkSelectionChanged path is INFERRED')

# ---- the account header (favourite star and goto icon); the header row is hidden for all accounts (switchAccount, lines 694-700)

gui('S_WATCHLIST', 'WatchlistFragment$6.onClick',
    'Tap the favourite star (R.id.imageViewAccountFav) in the account header of the watchlist',
    needs_state=state_text('an investment account is selected: switchAccount hides the header row (headerRow GONE) for all accounts (NOT_SET) and shows it otherwise (WatchlistFragment.java:694-700)', ('account',)),
    evidence='SRC investment/watchlist/WatchlistFragment.java:554-569 (favourite listener; setFavorite 556, save 559, setImageViewFavorite 566), 694-700 (headerRow GONE at 694, VISIBLE at 700); SRC res/layout/fragment_watchlist_header.xml:27 (headerRow, no android:visibility), 78 (imageViewAccountFav); auto_calls.json records WatchlistFragment$6.onClick -> Account.setFavorite (556), AccountRepository.save (559), setImageViewFavorite (566, access$600)')

gui('S_WATCHLIST', 'WatchlistFragment$7.onClick',
    'Tap the goto-account icon (R.id.imageViewGotoAccount) in the watchlist header',
    needs_state=state_text('an investment account is selected: switchAccount hides the header row (headerRow GONE) for all accounts (NOT_SET) and shows it otherwise (WatchlistFragment.java:694-700)', ('account',)),
    evidence='SRC investment/watchlist/WatchlistFragment.java:573-581 (goto listener; intent 576, putExtra 577, setAction 578, startActivity 579), 694-700; SRC res/layout/fragment_watchlist_header.xml:69 (imageViewGotoAccount); auto_calls.json record WatchlistFragment$7.onClick -> getAccountId (577, access$700); the INTENT edge from this method to AccountEditActivity.<init> is written by batch 006 (label_006.py:30-33), not here')

# ---- the purge-history dialog (menu_purge_history, WatchlistFragment.java:264)

gui('S_WATCHLIST', 'WatchlistFragment$8.onClick',
    'Tap Purge price history in the options menu, then Cancel in the confirmation dialog',
    cls='non_standard',
    via='platform AlertDialog negative button: same dispatch as WatchlistFragment$3.onClick (AlertController.java:160-166)',
    evidence='SRC investment/watchlist/WatchlistFragment.java:638-643 (setNegativeButton at 638; onClick 640-642; dismiss 641); SRC res/menu/menu_watchlist.xml:32-36 (menu_purge_history); SRC WatchlistFragment.java:264 (purgePriceHistory); class file WatchlistFragment$8 refs DialogInterface.dismiss only (grep.txt section 1)')

gui('S_WATCHLIST', 'WatchlistFragment$9.onClick',
    'Tap Purge price history in the options menu, then OK in the confirmation dialog',
    cls='non_standard',
    via='platform AlertDialog positive button: same dispatch as WatchlistFragment$4.onClick (AlertController.java:160-166)',
    evidence='SRC investment/watchlist/WatchlistFragment.java:618-636 (setPositiveButton at 618; onClick 620-636; deleteAllPriceHistory 622; SyncManager.dataChanged 625; dismiss 635); SRC res/menu/menu_watchlist.xml:32-36; auto_calls.json records WatchlistFragment$9.onClick -> StockHistoryRepository.deleteAllPriceHistory (622), SyncManager.dataChanged (625); class file WatchlistFragment$9 refs deleteAllPriceHistory and dataChanged (grep.txt sections 1-2)')

# ---- part 094 (2026-10-29)
# ---- batch 094: WatchlistItemsFragment (27 methods), its listeners WatchlistItemsFragment$1, $2 and $3 (6 methods), and WatchlistViewHolder.<init> (1 method): 34 methods.
# Rows and printed lines: graphs/MMEX/parts/label_094.md. Grep and sed evidence: graphs/MMEX/parts/label_094.grep.txt (sections A-G).
# Edges are written only for destinations that this batch owns (D1). CALL edges already in auto_calls.json are not repeated (D7).
# Page key: S_WATCHLIST is defined in label_092.py:7 (SCREENS.update) and reused here (D9). No new key is defined in this part.
# UNREACHABLE entries: none. All 34 methods are REACHABLE.
# sup pairs: none written (no UNREACHABLE caller in this batch, D14). The merged sup pair at graph_def.py:3786 (BaseListFragment$2.onClick -> WatchlistItemsFragment.onFloatingActionButtonClicked) stays as it is; it cuts the plain CALL, so the GUI edge below is the route to onFloatingActionButtonClicked.
# Not repeated (already merged): graph_def.py:7386 (WatchlistItemsFragment.openEditInvestmentActivity -> InvestmentTransactionEditActivity.<init>, INTENT, batch 086) and graph_def.py:7631 (WatchlistItemsFragment.onContextItemSelected -> PriceEditActivity.<init>, INTENT, batch 088).
# Edges written: 16 (LIFECYCLE 6, FRAMEWORK 4, GUI 5 from S_WATCHLIST, RESULT 1).

# ---- fragment lifecycle (androidx Fragment; library source not read: INFERRED)

e('WatchlistItemsFragment.<init>', 'WatchlistItemsFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the implicit default constructor (reached from newInstance)',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:77-79 (no constructor declared), 88-91 (newInstance); INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistItemsFragment.onCreate', 'WatchlistItemsFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate (onCreate reads accountId from the saved state or the arguments, lines 109-113)',
  evidence='SRC WatchlistItemsFragment.java:103-115, 117-123; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistItemsFragment.onCreateView', 'WatchlistItemsFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onCreateView (the layout is inflated at line 120)',
  evidence='SRC WatchlistItemsFragment.java:117-127; INFERRED androidx Fragment lifecycle (library source not read)')

e('WatchlistItemsFragment.onActivityCreated', 'WatchlistItemsFragment.onSaveInstanceState', 'LIFECYCLE',
  'approximation: the host activity saves the fragment state before it stops (ActivityThread), and no app method calls this; the edge stands in for the live fragment state after onActivityCreated (same pattern as batch 087)',
  evidence='SRC WatchlistItemsFragment.java:126-174, 348-353; FW-SRC core/java/android/app/ActivityThread.java:4022-4025 (callCallActivityOnSaveInstanceState before the stop); INFERRED androidx state save (library source not read)')

e('WatchlistItemsFragment.onSaveInstanceState', 'WatchlistItemsFragment.onStop', 'LIFECYCLE',
  'the activity stops after its state is saved (ActivityThread saves the state before performStop), so the fragment gets onStop',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:4022-4032 (state save at 4025, performStop at 4032); SRC WatchlistItemsFragment.java:355-372; INFERRED androidx dispatchStop (library source not read)')

e('WatchlistItemsFragment.onStop', 'WatchlistItemsFragment.onDestroy', 'LIFECYCLE',
  'the framework calls onDestroy after onStop when the fragment is removed or the host activity finishes',
  evidence='SRC WatchlistItemsFragment.java:274-277, 355-357; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- loader callbacks (LoaderManager, androidx; library source not read: INFERRED)

e('WatchlistItemsFragment.reloadData', 'WatchlistItemsFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader creates the loader for ID_LOADER and calls the LoaderCallbacks (this fragment) through onCreateLoader',
  evidence='SRC WatchlistItemsFragment.java:386-393 (restartLoader with this as the callbacks, line 392); INFERRED androidx LoaderManager.restartLoader (library source not read)')

e('WatchlistItemsFragment.onCreateLoader', 'WatchlistItemsFragment.onLoadFinished', 'FRAMEWORK',
  'the loader runs its query and delivers the cursor to onLoadFinished',
  evidence='SRC WatchlistItemsFragment.java:282-314 (MmxCursorLoader at 309), 323-341; INFERRED androidx loader delivery (library source not read)')

e('WatchlistItemsFragment.onLoadFinished', 'WatchlistItemsFragment.onLoaderReset', 'FRAMEWORK',
  'the loader manager resets a loader that has delivered data (for example when restartLoader replaces it)',
  guard='onLoaderReset is called only for a loader whose data was delivered by onLoadFinished (INFERRED androidx LoaderInfo)',
  evidence='SRC WatchlistItemsFragment.java:316-321 (body), 323-341; INFERRED androidx LoaderManager reset (library source not read)')

e('WatchlistItemsFragment$1.onItemClick', 'WatchlistItemsFragment.onCreateContextMenu', 'FRAMEWORK',
  'a row tap calls getActivity().openContextMenu(view); the framework builds the menu by calling the fragment, which registered itself as the context menu listener (line 165)',
  evidence='SRC WatchlistItemsFragment.java:140-150 (openContextMenu at 147), 165 (registerForContextMenu); FW-SRC core/java/android/app/Activity.java:3791-3793 (openContextMenu -> view.showContextMenu()); core/java/android/view/View.java:6448-6449 (showContextMenu), 12578-12588 (createContextMenu calls the listener at 12588); core/java/android/view/ViewGroup.java:860-866; INFERRED root step (ViewRootImpl not read) and registerForContextMenu (androidx, not read)')

# ---- the result of the price editor (PriceEditActivity, batch 088)

e('PriceEditActivity.onOptionsItemSelected', 'WatchlistItemsFragment.onActivityResult', 'RESULT',
  'the price editor saves and finishes with RESULT_OK; the platform delivers the result to the fragment that started it (request code RequestCodes.PRICE)',
  guard='requestCode == RequestCodes.PRICE (line 180) and resultCode == RESULT_OK (line 181); the editor was started at line 253 with RequestCodes.PRICE',
  evidence='SRC investment/PriceEditActivity.java:111-126 (save 120, setResult 121, finish 122); SRC investment/watchlist/WatchlistItemsFragment.java:176-185, 253; FW-SRC core/java/android/app/Activity.java:7259-7284 (dispatchActivityResult to the fragment); INFERRED fragment routing by request prefix (androidx, not read)')

# ---- page-to-method GUI edges from S_WATCHLIST (the watchlist screen; key from label_092.py:7, reused, D9)

gui('S_WATCHLIST', 'WatchlistItemsFragment$1.onItemClick',
    'Tap a security row of the watchlist (not the header row): the row opens its context menu',
    evidence='SRC investment/watchlist/WatchlistItemsFragment.java:140-150 (header guard at 144; openContextMenu at 147); FW-SRC core/java/android/widget/AdapterView.java:316-318 (performItemClick calls mOnItemClickListener.onItemClick)')

gui('S_WATCHLIST', 'WatchlistItemsFragment.onContextItemSelected',
    'Tap an item of the context menu of a security row: Download price, Edit price or Delete',
    cls='non_standard',
    via='the activity forwards the context item to the fragment: FW-SRC core/java/android/app/Activity.java:3470 (onMenuItemSelected context case), then INFERRED androidx forwarding (not read)',
    evidence='SRC investment/watchlist/WatchlistItemsFragment.java:214-272 (switch 233; DownloadPrice 234-238; EditPrice 240-264; DELETE 266-268); SRC investment/watchlist/WatchlistItemsFragment.java:189-207 (the menu built by onCreateContextMenu)')

gui('S_WATCHLIST', 'WatchlistItemsFragment.onFloatingActionButtonClicked',
    'Tap the + button on the watchlist: opens the new investment transaction editor',
    cls='non_standard',
    via='BaseListFragment$2.onClick (batch 026, common/BaseListFragment.java:241-246) calls onFloatingActionButtonClicked() at line 244; the plain CALL is cut by the merged sup pair at graph_def.py:3786, so this GUI edge is the route',
    evidence='SRC investment/watchlist/WatchlistItemsFragment.java:172-173 (FAB shown and attached), 343-346 (override); SRC common/BaseListFragment.java:238-248 (listener 241-246, call 244); label_026.md row BaseListFragment$2.onClick (REACHABLE, GUI from S_PAYEE); INFERRED FAB library dispatch (com.melnykov FAB is not in fw_src)')

gui('S_WATCHLIST', 'WatchlistItemsFragment$2.onClick',
    'Tap Cancel in the delete confirmation dialog (opened by the Delete item of a row context menu): the dialog closes and nothing is deleted',
    cls='non_standard',
    via='platform AlertDialog button: FW-SRC core/java/com/android/internal/app/AlertController.java:125-140 (mButtonHandler posts the button message at 140), 149-166 (ButtonHandler calls the listener at 166)',
    evidence='SRC investment/watchlist/WatchlistItemsFragment.java:266-268 (DELETE), 472-498 (dialog; Cancel listener body 493-496, dialog.cancel() at 495); auto_calls.json has no record with src WatchlistItemsFragment$2.onClick (grep file, section D)')

gui('S_WATCHLIST', 'WatchlistItemsFragment$3.onClick',
    'Tap OK in the delete confirmation dialog: deletes the security (StockRepository.delete) and restarts the loader',
    cls='non_standard',
    via='platform AlertDialog button: FW-SRC core/java/com/android/internal/app/AlertController.java:125-140, 149-166 (as for $2.onClick)',
    evidence='SRC investment/watchlist/WatchlistItemsFragment.java:479-490 (OK listener; body 482-488: delete at 483, toast at 484, reloadData at 488); auto_calls.json records with src WatchlistItemsFragment$3.onClick at lines 482-488 (grep file, section D)')

# ---- part 095 (2026-10-29)
# batch 095 (label_095): 26 methods (graphs/MMEX/scratch/batches/batch_095.txt): YahooCsvQuoteDownloaderRetrofit (8: <init>, downloadPrices, finishIfAllDone, getYahooCsvService, onContentDownloaded, $1.<init>, $1.onFailure, $1.onResponse), YqlQueryGenerator (3), YqlSecurityPriceUpdaterRetrofit (10: <init>, downloadPrices, getPricesFromJson, getSecurityPriceFor, getYqlService, onContentDownloaded, readPrice, $1.<init>, $1.onFailure, $1.onResponse), CrashReportingTree (2), DebugTree (2), ErrorRaisedEvent (1).
# Rows, printed lines and counts: graphs/MMEX/parts/label_095.md (24 REACHABLE, 2 UNREACHABLE, 0 INCOMPLETE).
# Grep evidence: graphs/MMEX/parts/label_095.grep.txt (sections 1-6).
# This file writes:
#   - 0 SCREENS keys and 0 page edges (no GUI method in this batch);
#   - 6 e() edges, all with a destination in this batch (D1): 4 FRAMEWORK (Retrofit enqueue callbacks: downloadPrices -> $1.onResponse and $1.onFailure, for the CSV and the YQL downloaders) and 2 CALL (cls non_standard: the Timber.e calls in YahooCsv$1.onFailure and YqlSecurityPriceUpdaterRetrofit$1.onFailure dispatch to DebugTree.log);
#   - 2 UNREACHABLE entries (app source, SOURCE): CrashReportingTree.<init> and CrashReportingTree.log;
#   - 1 sup pair (D14): the auto CALL record CrashReportingTree.log -> ErrorRaisedEvent.<init> (its caller is UNREACHABLE in this batch).
# Not written (D7): every other auto CALL and CHA record into this batch (for example the factory's constructor calls, WatchlistFragment -> downloadPrices, DebugTree.<init> from MmexApplication.onCreate, DebugTree.log -> ErrorRaisedEvent.<init>); they come from graphs/MMEX/auto_calls.json and carry no needs_state. Their state gates (the quote provider setting) are kept in the batch rows only, and the callback edges below carry the gate.
# Known gap: the settings gate is on the callback edges, not on the auto CALL edges into the constructors and downloadPrices (D7), so those routes show no state gate in the graph.

# ---- gate texts (inline, D2). The CSV and YQL texts are the same strings as the state gates of batch 092 (parts/label_092.py)

# ================================================================== Yahoo CSV downloader: Retrofit callbacks (FRAMEWORK, library dispatch INFERRED)

e('YahooCsvQuoteDownloaderRetrofit.downloadPrices', 'YahooCsvQuoteDownloaderRetrofit$1.onResponse', 'FRAMEWORK',
  'Retrofit calls the Callback onResponse when the CSV request for a symbol gets a response; the method calls onContentDownloaded (line 71)',
  guard='symbols is not null and not empty (lines 60 and 62); the callback is queued for each symbol in the loop (line 84)',
  needs_state=state_text('the quote provider setting is YahooCsv (set in the Change provider dialog)', ('settings',)),
  via='Retrofit enqueue callback (library not read, INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:59-62, 68-72, 82-84 (anonymous Callback at 68, onResponse at 70-72, enqueue at 84); SRC investment/SecurityPriceUpdaterFactory.java:47-48 (the YahooCsv case that creates this object); INFERRED Retrofit enqueue callback dispatch (library not read); auto_calls.json record YahooCsvQuoteDownloaderRetrofit$1.onResponse -> YahooCsvQuoteDownloaderRetrofit.onContentDownloaded (line 71)')

e('YahooCsvQuoteDownloaderRetrofit.downloadPrices', 'YahooCsvQuoteDownloaderRetrofit$1.onFailure', 'FRAMEWORK',
  'Retrofit calls the Callback onFailure when the CSV request fails before a response; the method closes the progress dialog (line 76) and logs through Timber (line 78)',
  guard='symbols is not null and not empty (lines 60 and 62); the callback is queued for each symbol in the loop (line 84)',
  env=env_text('the price request fails before a response (no connection, timeout or server error)', ('network',)),
  needs_state=state_text('the quote provider setting is YahooCsv (set in the Change provider dialog)', ('settings',)),
  via='Retrofit enqueue callback (library not read, INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:59-62, 68, 74-79, 84 (onFailure at 75, closeProgressDialog at 76, Timber.e at 78, enqueue at 84); SRC investment/SecurityPriceUpdaterFactory.java:47-48; INFERRED Retrofit enqueue callback dispatch (library not read); auto_calls.json record YahooCsvQuoteDownloaderRetrofit$1.onFailure -> PriceUpdaterBase.closeProgressDialog (line 76)')

# ================================================================== Yahoo CSV failure path into the debug tree (CALL through Timber, library dispatch INFERRED)

e('YahooCsvQuoteDownloaderRetrofit$1.onFailure', 'DebugTree.log', 'CALL',
  'the Timber.e call at line 78 hands the failure to the planted trees; in the debug build the planted DebugTree.log runs and posts ErrorRaisedEvent when a subscriber exists',
  guard='DebugTree is planted only in the debug branch (MmexApplication.java:134-135); the posted event needs a subscriber (DebugTree.java:45)',
  env=env_text('the price request fails before a response (no connection, timeout or server error)', ('network',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 78) calls each planted Tree.log (library source not read, INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:74-79 (Timber.e at 78); SRC MmexApplication.java:134-135 (Timber.plant(new DebugTree()) in the debug branch); SRC log/DebugTree.java:34-46, 50; INFERRED Timber dispatch to planted trees (library not read)')

# ================================================================== Yql downloader: Retrofit callbacks (FRAMEWORK, library dispatch INFERRED). The YQL provider is the default

e('YqlSecurityPriceUpdaterRetrofit.downloadPrices', 'YqlSecurityPriceUpdaterRetrofit$1.onResponse', 'FRAMEWORK',
  'Retrofit calls the Callback onResponse with the YQL response; the method calls onContentDownloaded (line 90)',
  guard='symbols is not null and not empty (lines 75 and 77); the request is enqueued inside try (line 103)',
  needs_state=state_text('the quote provider setting is YahooYql (the default when the setting is unset)', ('settings',)),
  via='Retrofit enqueue callback (library not read, INFERRED)',
  evidence='SRC investment/yql/YqlSecurityPriceUpdaterRetrofit.java:74-77, 87-91, 100-103 (anonymous Callback at 87, onResponse at 89-91, enqueue at 103); SRC investment/SecurityPriceUpdaterFactory.java:44-45, 50-52 (the YahooYql and default cases); SRC settings/InvestmentSettings.java:75; INFERRED Retrofit enqueue callback dispatch (library not read)')

e('YqlSecurityPriceUpdaterRetrofit.downloadPrices', 'YqlSecurityPriceUpdaterRetrofit$1.onFailure', 'FRAMEWORK',
  'Retrofit calls the Callback onFailure when the YQL request fails before a response; the method logs through Timber (line 95) and closes the progress dialog (line 96)',
  guard='symbols is not null and not empty (lines 75 and 77); the request is enqueued inside try (line 103)',
  env=env_text('the price request fails before a response (no connection, timeout or server error)', ('network',)),
  needs_state=state_text('the quote provider setting is YahooYql (the default when the setting is unset)', ('settings',)),
  via='Retrofit enqueue callback (library not read, INFERRED)',
  evidence='SRC investment/yql/YqlSecurityPriceUpdaterRetrofit.java:74-77, 87, 93-97, 100-103 (onFailure at 94, Timber.e at 95, closeProgressDialog at 96, enqueue at 103); SRC investment/SecurityPriceUpdaterFactory.java:44-45, 50-52; SRC settings/InvestmentSettings.java:75; INFERRED Retrofit enqueue callback dispatch (library not read)')

e('YqlSecurityPriceUpdaterRetrofit$1.onFailure', 'DebugTree.log', 'CALL',
  'the Timber.e call at line 95 hands the failure to the planted trees; in the debug build the planted DebugTree.log runs and posts ErrorRaisedEvent when a subscriber exists',
  guard='DebugTree is planted only in the debug branch (MmexApplication.java:134-135); the posted event needs a subscriber (DebugTree.java:45)',
  env=env_text('the price request fails before a response (no connection, timeout or server error)', ('network',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 95) calls each planted Tree.log (library source not read, INFERRED)',
  evidence='SRC investment/yql/YqlSecurityPriceUpdaterRetrofit.java:93-97 (Timber.e at 95); SRC MmexApplication.java:134-135 (Timber.plant(new DebugTree()) in the debug branch); SRC log/DebugTree.java:34-46, 50; INFERRED Timber dispatch to planted trees (library not read)')

# ================================================================== UNREACHABLE (batch 095). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['CrashReportingTree.<init>'] = ('no_trigger_in_app',
  'The class is never instantiated in the app: the only Timber.plant of a CrashReportingTree is commented out (MmexApplication.java:137), and no other source line creates one (label_095.grep.txt sections 1, 2, 5). The implicit default constructor therefore has no caller. The class is annotated @Deprecated (CrashReportingTree.java:32).',
  'SRC log/CrashReportingTree.java:32-33; SRC MmexApplication.java:133-140; label_095.grep.txt sections 1, 2, 5',
  'SOURCE')

UNREACHABLE['CrashReportingTree.log'] = ('no_trigger_in_app',
  'Timber calls a tree log() only for trees that were planted with Timber.plant. CrashReportingTree is never planted: MmexApplication.java:137 is commented out, and the debug branch plants DebugTree (line 135) while the release branch plants ScreenTree and SysLogTree (lines 138-139). No instance exists, so log() has no caller. Its auto_calls record CrashReportingTree.log -> ErrorRaisedEvent.<init> is cut by the sup pair below.',
  'SRC log/CrashReportingTree.java:34-56 (log, post at 56); SRC MmexApplication.java:133-140; label_095.grep.txt sections 1, 2, 3, 6',
  'SOURCE')

# ================================================================== sup pairs (D14): auto CALL record whose caller is UNREACHABLE in this batch

sup(('CrashReportingTree.log', 'ErrorRaisedEvent.<init>'))

# ---- part 096 (2026-10-29)
# ================================================================== batch 096 (label_096): 33 methods (graphs/MMEX/AGENT_NOTES.md batch table, row 096): ExceptionHandler (15: constructors, e, getters, showMessage, uncaughtException, sendEmail, anonymous Runnable $1), FileLoggingTree (2), ScreenTree (2), SysLogTree (2), RecurringTransactionIntentService (4), RecurringTransactionReceiver (2), RecurringTransactionNotifications (6).
# Rows, printed lines and counts: graphs/MMEX/parts/label_096.md (22 REACHABLE, 11 UNREACHABLE, 0 INCOMPLETE).
# Grep and sed evidence: graphs/MMEX/parts/label_096.grep.txt (sections 1-16).
# This file writes:
#   - 0 SCREENS keys (no GUI method in this batch; the toast is a Handler post, not a page);
#   - 9 e() edges, each with a destination in this batch (D1): 1 FRAMEWORK from batch 038 RecurringTransactionBootReceiver.setAlarm into RecurringTransactionReceiver.<init> (the alarm broadcast); 1 LIFECYCLE from that <init> to onReceive; 2 FRAMEWORK from RecurringTransactionIntentService.enqueueWork (JobIntentService) to its <init> and onHandleWork; 1 FRAMEWORK (Handler.post) from ExceptionHandler.showMessage(String,int) to $1.run; 4 CALL (cls non_standard, release-only Timber trees) from the two Timber.e call sites in RecurringTransactionNotifications (lines 56 and 127) to ScreenTree.log and SysLogTree.log;
#   - 11 UNREACHABLE entries: 9 for ExceptionHandler (app source, SOURCE) and 2 for FileLoggingTree (never planted, SOURCE);
#   - 12 sup pairs (D14): the auto CALL records whose caller is UNREACHABLE in this batch (e(Exception,String), e(Throwable,String), uncaughtException, getAppVersionInformation, getAppVersion, getAppBuildNumber).
# Not written (D7): every other auto CALL record into or inside this batch (for example MmexApplication.onCreate -> ScreenTree.<init> and SysLogTree.<init>; FormatUtilities and RecurringTransactionListFragment -> ExceptionHandler.<init>(Context,Object) and showMessage; MainActivity -> RecurringTransactionNotifications; Receiver.onReceive -> IntentService.enqueueWork and <clinit>; ExceptionHandler$1.<init>; $1.run -> getLogcat). They come from graphs/MMEX/auto_calls.json and carry no needs_state.
# Known gaps: (a) the auto record ExceptionHandler$1.run -> getLogcat sits in the catch block (lines 118-119, the exception path only) and is shown as a normal route; (b) the Timber.e call at RecurringTransactionBootReceiver.java:45 (batch 038 call site, merged) is not written here: it would also dispatch to ScreenTree and SysLogTree, and the batch 096 routes do not depend on it; (c) the settings gate sits on the two receiver edges only, not on the auto records.

# ================================================================== alarm route from the boot receiver (batch 038 setAlarm) into the notification receiver

e('RecurringTransactionBootReceiver.setAlarm', 'RecurringTransactionReceiver.<init>', 'FRAMEWORK',
  'setAlarm schedules a daily repeating AlarmManager alarm whose PendingIntent is a broadcast to RecurringTransactionReceiver; when the alarm fires the system creates the receiver instance to deliver the broadcast',
  needs_state=state_text('the repeating transaction notifications setting is on (default on, BehaviourSettings.java:42)', ('settings',)),
  env=env_text('the daily alarm fires at the notification time (the hour set in the settings)', ('time',)),
  via='AlarmManager repeat with a broadcast PendingIntent (AlarmManager delivery and the framework are not read: INFERRED)',
  evidence='SRC core/RecurringTransactionBootReceiver.java:49-53 (notify gate), 56-57 (intent and PendingIntent.getBroadcast), 59-78 (hour and calendar), 79-84 (cancel at 81, setRepeating at 83-84); SRC notifications/RecurringTransactionReceiver.java:31-39; SRC settings/BehaviourSettings.java:41-43; INFERRED AlarmManager delivery (not read)')

e('RecurringTransactionReceiver.<init>', 'RecurringTransactionReceiver.onReceive', 'LIFECYCLE',
  'the system calls onReceive on the new receiver instance; onReceive reads the notification setting and returns when it is off, otherwise it enqueues the job service (lines 37-38)',
  guard='the setting is on (lines 33-35; the default is true)',
  needs_state=state_text('the repeating transaction notifications setting is on (default on, BehaviourSettings.java:42)', ('settings',)),
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3185-3188 (receiver.onReceive at 3187); SRC notifications/RecurringTransactionReceiver.java:31-39')

# ================================================================== the job service (JobIntentService, androidx library not read: INFERRED)

e('RecurringTransactionIntentService.enqueueWork', 'RecurringTransactionIntentService.<init>', 'FRAMEWORK',
  'JobIntentService.enqueueWork queues the work for this service; the system creates the job service instance to run it',
  via='androidx JobIntentService (library not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionIntentService.java:33, 46-48 (the static enqueueWork calls JobIntentService.enqueueWork with JOB_ID); SRC AndroidManifest.xml:398-400 (service with BIND_JOB_SERVICE); INFERRED androidx JobIntentService (library not read)')

e('RecurringTransactionIntentService.enqueueWork', 'RecurringTransactionIntentService.onHandleWork', 'FRAMEWORK',
  'the JobIntentService worker delivers the queued intent to onHandleWork, which builds the notifications object and calls notifyRepeatingTransaction (lines 42-43; these two CALL records are in auto_calls.json)',
  via='JobIntentService worker thread (library not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionIntentService.java:39-48; INFERRED androidx JobIntentService dispatch (library not read)')

# ================================================================== the toast Runnable (Handler.post on the main looper; framework source read)

e('ExceptionHandler.showMessage(String,int)', 'ExceptionHandler$1.run', 'FRAMEWORK',
  'the handler posts the anonymous Runnable to the main looper; the main thread runs it and shows the toast (line 117)',
  guard='mContext is not null (line 111; showMessage returns before the post otherwise)',
  via='Handler.post queues a message with the Runnable as its callback; dispatchMessage runs handleCallback, which calls callback.run() (FW-SRC Handler.java:355-357, 97-99, 789-790)',
  evidence='SRC log/ExceptionHandler.java:110-117 (Handler on the main looper at 113, post at 114, run body at 115-117); FW-SRC core/java/android/os/Handler.java:355-357, 97-99, 789-790')

# ================================================================== Timber calls in batch 096 dispatch to the release-only trees (library dispatch INFERRED)

e('RecurringTransactionNotifications.notifyRepeatingTransaction', 'ScreenTree.log', 'CALL',
  'the Timber.e call in the catch block (line 56) hands the exception to the planted trees; in the release build the planted ScreenTree.log runs and posts ErrorRaisedEvent when a subscriber exists',
  guard='release build only: ScreenTree is planted in the else branch (MmexApplication.java:136-139); the debug build plants DebugTree instead (line 135)',
  env=env_text('an exception is thrown while the recurring transaction notification is built or shown (the catch at line 55)', ('other',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 56) calls each planted Tree.log (library source not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionNotifications.java:52-58 (Timber.e at 56); SRC MmexApplication.java:134-140; SRC log/ScreenTree.java:15-32 (post at 26-27); INFERRED Timber dispatch (library not read)')

e('RecurringTransactionNotifications.notifyRepeatingTransaction', 'SysLogTree.log', 'CALL',
  'the same Timber.e call (line 56) hands the exception to the planted trees; in the release build the planted SysLogTree.log writes the message to the system log',
  guard='release build only: SysLogTree is planted in the else branch (MmexApplication.java:136-139); the debug build plants DebugTree instead (line 135)',
  env=env_text('an exception is thrown while the recurring transaction notification is built or shown (the catch at line 55)', ('other',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 56) calls each planted Tree.log (library source not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionNotifications.java:52-58 (Timber.e at 56); SRC MmexApplication.java:134-140; SRC log/SysLogTree.java:13-15 (Log.println at 14); INFERRED Timber dispatch (library not read)')

e('RecurringTransactionNotifications.showNotification', 'ScreenTree.log', 'CALL',
  'the Timber.e call in the catch block (line 127) hands the exception to the planted trees; in the release build the planted ScreenTree.log runs and posts ErrorRaisedEvent when a subscriber exists',
  guard='release build only: ScreenTree is planted in the else branch (MmexApplication.java:136-139); the debug build plants DebugTree instead (line 135)',
  env=env_text('an exception is thrown while the notification is created or posted (the catch at line 126)', ('other',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 127) calls each planted Tree.log (library source not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionNotifications.java:82-129 (catch at 126, Timber.e at 127); SRC MmexApplication.java:134-140; SRC log/ScreenTree.java:15-32 (post at 26-27); INFERRED Timber dispatch (library not read)')

e('RecurringTransactionNotifications.showNotification', 'SysLogTree.log', 'CALL',
  'the same Timber.e call (line 127) hands the exception to the planted trees; in the release build the planted SysLogTree.log writes the message to the system log',
  guard='release build only: SysLogTree is planted in the else branch (MmexApplication.java:136-139); the debug build plants DebugTree instead (line 135)',
  env=env_text('an exception is thrown while the notification is created or posted (the catch at line 126)', ('other',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 127) calls each planted Tree.log (library source not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionNotifications.java:82-129 (catch at 126, Timber.e at 127); SRC MmexApplication.java:134-140; SRC log/SysLogTree.java:13-15 (Log.println at 14); INFERRED Timber dispatch (library not read)')

# ================================================================== UNREACHABLE entries (app source, SOURCE: grep evidence in label_096.grep.txt)

UNREACHABLE['ExceptionHandler.<init>(Context)'] = ('no_trigger_in_app',
  'no caller: the app constructs ExceptionHandler only with two arguments (FormatUtilities.java:110, RecurringTransactionListFragment.java:185)',
  'SRC log/ExceptionHandler.java:47-50; label_096.grep.txt sections 1-2', 'SOURCE')

UNREACHABLE['ExceptionHandler.e(Exception,String)'] = ('no_trigger_in_app',
  'no caller: the two call sites use showMessage only (FormatUtilities.java:111, RecurringTransactionListFragment.java:186), and no other class calls e(...)',
  'SRC log/ExceptionHandler.java:72-74; label_096.grep.txt sections 2-3', 'SOURCE')

UNREACHABLE['ExceptionHandler.e(Throwable,String)'] = ('no_trigger_in_app',
  'its only caller is e(Exception,String) (line 73), which has no caller; the auto records from this method (lines 79-82) are cut by the sup pairs below',
  'SRC log/ExceptionHandler.java:72-86; label_096.grep.txt section 16', 'SOURCE')

UNREACHABLE['ExceptionHandler.getAppBuildNumber'] = ('no_trigger_in_app',
  'callers are e(Throwable,String) (line 79) and getAppVersionInformation (line 217), and both are UNREACHABLE',
  'SRC log/ExceptionHandler.java:235-243, 79, 217; label_096.grep.txt sections 5-6', 'SOURCE')

UNREACHABLE['ExceptionHandler.getAppVersion'] = ('no_trigger_in_app',
  'callers are e(Throwable,String) (line 79) and getAppVersionInformation (line 213), and both are UNREACHABLE',
  'SRC log/ExceptionHandler.java:225-233, 79, 213; label_096.grep.txt sections 5-6', 'SOURCE')

UNREACHABLE['ExceptionHandler.getAppVersionInformation'] = ('no_trigger_in_app',
  'its only caller is uncaughtException (line 138), which is UNREACHABLE',
  'SRC log/ExceptionHandler.java:208-223, 138; label_096.grep.txt sections 5-6', 'SOURCE')

UNREACHABLE['ExceptionHandler.getContext'] = ('no_trigger_in_app',
  'callers are getAppVersionInformation (line 209), getAppVersion (line 228) and getAppBuildNumber (line 237), all UNREACHABLE; no class outside the file calls it (grep section 3)',
  'SRC log/ExceptionHandler.java:68-70, 209, 228, 237; label_096.grep.txt sections 3 and 6', 'SOURCE')

UNREACHABLE['ExceptionHandler.sendEmail'] = ('no_trigger_in_app',
  'its only caller is uncaughtException (line 182), which is UNREACHABLE',
  'SRC log/ExceptionHandler.java:193-206, 182; label_096.grep.txt sections 5-6', 'SOURCE')

UNREACHABLE['ExceptionHandler.uncaughtException'] = ('framework_never_calls',
  'nothing registers the handler as the default or a thread uncaught handler (grep section 4); the only mention is the commented line 61; the framework would call it only after such a registration (INFERRED)',
  'SRC log/ExceptionHandler.java:40, 61, 125-126; label_096.grep.txt section 4', 'SOURCE')

UNREACHABLE['FileLoggingTree.<init>'] = ('no_trigger_in_app',
  'never constructed: the app plants DebugTree (debug) or ScreenTree and SysLogTree (release) only (MmexApplication.java:134-140); no other reference to FileLoggingTree in src/main (grep section 7)',
  'SRC log/FileLoggingTree.java:31-32; SRC MmexApplication.java:134-140; label_096.grep.txt section 7', 'SOURCE')

UNREACHABLE['FileLoggingTree.log'] = ('no_trigger_in_app',
  'never planted, so Timber never dispatches to it (grep section 7)',
  'SRC log/FileLoggingTree.java:35-47; label_096.grep.txt section 7', 'SOURCE')

# ================================================================== sup pairs (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('ExceptionHandler.e(Exception,String)', 'ExceptionHandler.e(Throwable,String)'),
    ('ExceptionHandler.e(Throwable,String)', 'ExceptionHandler.showMessage(String)'),
    ('ExceptionHandler.e(Throwable,String)', 'ExceptionHandler.getLogcat'),
    ('ExceptionHandler.e(Throwable,String)', 'ExceptionHandler.getAppBuildNumber'),
    ('ExceptionHandler.e(Throwable,String)', 'ExceptionHandler.getAppVersion'),
    ('ExceptionHandler.uncaughtException', 'ExceptionHandler.sendEmail'),
    ('ExceptionHandler.uncaughtException', 'ExceptionHandler.getAppVersionInformation'),
    ('ExceptionHandler.getAppVersionInformation', 'ExceptionHandler.getAppBuildNumber'),
    ('ExceptionHandler.getAppVersionInformation', 'ExceptionHandler.getAppVersion'),
    ('ExceptionHandler.getAppVersionInformation', 'ExceptionHandler.getContext'),
    ('ExceptionHandler.getAppVersion', 'ExceptionHandler.getContext'),
    ('ExceptionHandler.getAppBuildNumber', 'ExceptionHandler.getContext'))

# ---- part 097 (2026-10-29)
# ================================================================== batch 097 (label_097): SmsReceiverTransactions (18 methods), SmsReceiverTransactions_MembersInjector (4), SyncNotificationModel (1), Encryptor (10), FingerprintHandler (6): 39 methods, 25 REACHABLE, 14 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_097.md; grep output: graphs/MMEX/parts/label_097.grep.txt.
# Edges here: S_ENTRY to SmsReceiverTransactions.<clinit> and <init> (manifest SMS_RECEIVED receiver, exported=true), LIFECYCLE from <init> to onReceive (state gate: the bank SMS setting), and FRAMEWORK edges from FingerprintHandler.startAuth to its four callbacks (INFERRED, FingerprintManager source not in fw_src).
# Every other REACHABLE row rests on an auto_calls.json CALL record (D7: no edge written for those). The SyncNotificationModel.<init> and FingerprintHandler.<init>/startAuth rows rest on auto records as well.

ENV_SMS_BROADCAST = env_text(
    'outside package: the system delivers an SMS (SMS_RECEIVED) to the receiver, or another app sends an explicit broadcast to this exported receiver',
    ('system_event', 'other_app'))

STATE_BANK_SMS = state_text(
    'the bank SMS setting is on (Behaviour settings, default off): the body of onReceive runs only then',
    ('settings',))

ENV_FINGERPRINT_RESULT = env_text(
    'outside package: the user places a finger on the fingerprint sensor, and the framework reports the result (success, failure, help or error)',
    ('hardware',))

# ================================================================== batch 097: ENTRY and LIFECYCLE edges (SMS receiver)

e('S_ENTRY', 'SmsReceiverTransactions.<clinit>', 'ENTRY',
  'The framework loads the SMS receiver class by name before it creates the receiver; the class static fields are initialized then',
  env=ENV_SMS_BROADCAST,
  evidence='SRC AndroidManifest.xml:126-131; SRC notifications/SmsReceiverTransactions.java:87-94 (static fields); FW-SRC core/java/android/app/ActivityThread.java:3141-3166 (handleReceiver loads and creates the receiver); JVM class initialization is not in fw_src: INFERRED, source not read')

e('S_ENTRY', 'SmsReceiverTransactions.<init>', 'ENTRY',
  'The framework creates the receiver by class name when a broadcast is delivered to it (the manifest receiver for SMS_RECEIVED, exported=true, no android:permission attribute)',
  env=ENV_SMS_BROADCAST,
  evidence='SRC AndroidManifest.xml:126-131; FW-SRC core/java/android/app/ActivityThread.java:3141-3166 (handleReceiver creates the receiver with loadClass(component).newInstance())')

e('SmsReceiverTransactions.<init>', 'SmsReceiverTransactions.onReceive', 'LIFECYCLE',
  'The framework calls onReceive on the receiver it has just created; the body runs only when the bank SMS setting is on (line 117)',
  needs_state=STATE_BANK_SMS,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3187 (receiver.onReceive); SRC notifications/SmsReceiverTransactions.java:97, 117; SRC settings/BehaviourSettings.java:67-68 (getBankSmsTrans, default false)')

# ================================================================== batch 097: FRAMEWORK edges (fingerprint callbacks)

e('FingerprintHandler.startAuth', 'FingerprintHandler.onAuthenticationSucceeded', 'FRAMEWORK',
  'FingerprintManager.authenticate (called at startAuth line 32) delivers the result to the callback object it was given (this handler); the framework calls onAuthenticationSucceeded when the sensor matches a finger',
  env=ENV_FINGERPRINT_RESULT,
  evidence='SRC passcode/FingerprintHandler.java:18, 27-33, 51-61; SRC PasscodeActivity.java:193-195; FingerprintManager is not in fw_src: the callback dispatch is INFERRED, source not read')

e('FingerprintHandler.startAuth', 'FingerprintHandler.onAuthenticationFailed', 'FRAMEWORK',
  'FingerprintManager.authenticate delivers a failed match to the callback (this handler), which calls onAuthenticationFailed',
  env=ENV_FINGERPRINT_RESULT,
  evidence='SRC passcode/FingerprintHandler.java:18, 27-33, 41-43; SRC PasscodeActivity.java:195; FingerprintManager is not in fw_src: INFERRED, source not read')

e('FingerprintHandler.startAuth', 'FingerprintHandler.onAuthenticationHelp', 'FRAMEWORK',
  'FingerprintManager.authenticate delivers a help message to the callback (this handler), which calls onAuthenticationHelp',
  env=ENV_FINGERPRINT_RESULT,
  evidence='SRC passcode/FingerprintHandler.java:18, 27-33, 46-48; SRC PasscodeActivity.java:195; FingerprintManager is not in fw_src: INFERRED, source not read')

e('FingerprintHandler.startAuth', 'FingerprintHandler.onAuthenticationError', 'FRAMEWORK',
  'FingerprintManager.authenticate delivers an error to the callback (this handler), which calls onAuthenticationError',
  env=ENV_FINGERPRINT_RESULT,
  evidence='SRC passcode/FingerprintHandler.java:18, 27-33, 36-38; SRC PasscodeActivity.java:195; FingerprintManager is not in fw_src: INFERRED, source not read')

# ================================================================== UNREACHABLE (batch 097): Encryptor (SOURCE: no call site in app source)

UNREACHABLE['Encryptor.<init>'] = ('no_trigger_in_app',
    'implicit default constructor (Encryptor.java declares no constructor); no new Encryptor in the app source, and the build classes name Encryptor only in its own class file',
    'passcode/Encryptor.java:41; label_097.grep.txt sections 1, 5',
    'SOURCE')

UNREACHABLE['Encryptor.encrypt'] = ('no_trigger_in_app',
    'public method that returns "not implemented"; no call site in app source (the only reference is a todo comment at core/Passcode.java:126)',
    'passcode/Encryptor.java:45-47; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.deriveKeyInsecurely'] = ('no_trigger_in_app',
    'public static method; no live call site in app source (its only call sites in Encryptor.java, lines 130 and 137, are commented out in getKeyFor); no live auto caller',
    'passcode/Encryptor.java:56-66, 130; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.deriveKeySecurely'] = ('no_trigger_in_app',
    'private method; its only call sites (Encryptor.java:132, 137) are commented out in getKeyFor, and getKeyFor has no call site',
    'passcode/Encryptor.java:71-83, 132, 137; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.getKeyFor'] = ('no_trigger_in_app',
    'private method; no call site anywhere in app source (the definition at line 90 is the only occurrence of the name outside its commented-out callers)',
    'passcode/Encryptor.java:90-121; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.encryptOrDecrypt'] = ('no_trigger_in_app',
    'private static helper; its only callers are encryptData (line 157) and decryptData (line 160), and neither has a call site',
    'passcode/Encryptor.java:145-155, 157, 160; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.encryptData'] = ('no_trigger_in_app',
    'private static method; no call site (the name occurs only at its definition, line 156)',
    'passcode/Encryptor.java:156-158; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.decryptData'] = ('no_trigger_in_app',
    'private static method; no call site (the name occurs only at its definition, line 159)',
    'passcode/Encryptor.java:159-161; label_097.grep.txt sections 1, 2',
    'SOURCE')

UNREACHABLE['Encryptor.retrieveSalt'] = ('no_trigger_in_app',
    'private method; its only caller is deriveKeySecurely (line 73), which has no call site',
    'passcode/Encryptor.java:73, 163-169; label_097.grep.txt sections 1, 2, 3',
    'SOURCE')

UNREACHABLE['Encryptor.readFromFileOrCreateRandom'] = ('no_trigger_in_app',
    'private method; its only caller is retrieveSalt (line 167), which is itself unreachable',
    'passcode/Encryptor.java:167, 176-185; label_097.grep.txt sections 1, 2, 3',
    'SOURCE')

# ================================================================== UNREACHABLE (batch 097): SmsReceiverTransactions_MembersInjector (INFERRED: Dagger-generated, source not in the repo)

UNREACHABLE['SmsReceiverTransactions_MembersInjector.<init>'] = ('no_trigger_in_app',
    'Dagger-generated constructor (not in the source root; class file in build/intermediates). Its only caller record is create (auto record SmsReceiverTransactions_MembersInjector.java:22), and create has no caller. The app source does not name the class (label_097.grep.txt section 4)',
    'SmsReceiverTransactions_MembersInjector.java:22 (auto record); label_097.grep.txt sections 4, 5',
    'INFERRED')

UNREACHABLE['SmsReceiverTransactions_MembersInjector.create'] = ('no_trigger_in_app',
    'Dagger-generated static factory; no caller record in auto_calls.json; no app-source reference to the class (section 4); no build class except its own names the class (section 5)',
    'label_097.grep.txt sections 4, 5 (auto query: 0 callers)',
    'INFERRED')

UNREACHABLE['SmsReceiverTransactions_MembersInjector.injectDatabase'] = ('no_trigger_in_app',
    'Dagger-generated member injector for the receiver field; its only caller record is injectMembers (SmsReceiverTransactions_MembersInjector.java:27), and injectMembers has no caller',
    'SmsReceiverTransactions_MembersInjector.java:27 (auto record); label_097.grep.txt sections 4, 5',
    'INFERRED')

UNREACHABLE['SmsReceiverTransactions_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'Dagger-generated instance method; no caller record in auto_calls.json (section 5); no app-source reference (section 4)',
    'label_097.grep.txt sections 4, 5 (auto query: 0 callers)',
    'INFERRED')

# ================================================================== sup (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('Encryptor.deriveKeyInsecurely', 'InsecureSHA1PRNGKeyDerivator.<clinit>'),
    ('Encryptor.deriveKeyInsecurely', 'InsecureSHA1PRNGKeyDerivator.deriveInsecureKey'),
    ('Encryptor.deriveKeySecurely', 'Encryptor.retrieveSalt'),
    ('Encryptor.encryptData', 'Encryptor.encryptOrDecrypt'),
    ('Encryptor.decryptData', 'Encryptor.encryptOrDecrypt'),
    ('Encryptor.retrieveSalt', 'Encryptor.readFromFileOrCreateRandom'),
    ('SmsReceiverTransactions_MembersInjector.create', 'SmsReceiverTransactions_MembersInjector.<init>'),
    ('SmsReceiverTransactions_MembersInjector.injectMembers', 'SmsReceiverTransactions_MembersInjector.injectDatabase'))

# ---- part 098 (2026-10-29)
# ---- batch 098: InsecureSHA1PRNGKeyDerivator (8 methods), SimpleCrypto (11), Recurrence (4). Rows: graphs/MMEX/parts/label_098.md; evidence: graphs/MMEX/parts/label_098.grep.txt.
# No e() edges are written. The four Recurrence methods are REACHABLE only through auto CALL records (auto_calls.json: RecurringTransaction.java:70, 259, 260, 272, 276; RecurringTransactionService.java:79, 191, 198, 418, 433; RecurringTransactionEditActivity.java:246, 257; Recurrence.java:42, 61). The UNREACHABLE methods have no REACHABLE caller, so they need no edge.
# sup pairs cut the auto records whose caller is UNREACHABLE (D14). Groups: (1) inside InsecureSHA1PRNGKeyDerivator, 7 pairs; (2) Encryptor.deriveKeyInsecurely (batch 097) into this batch, 2 pairs, cross-batch; (3) inside SimpleCrypto, 9 pairs; (4) Passcode.decrypt and Passcode.encrypt (batch 038, REACHABLE, but their calls sit under if (Build.VERSION.SDK_INT <= 23), which is false on API 27) into SimpleCrypto.decrypt and SimpleCrypto.encrypt, 2 pairs, cross-batch.
# Total: 20 sup pairs. The same callers are not checked for receiver variants: auto_calls.json has no receiver_variants entry naming these classes.

# ---- sup pairs (1): InsecureSHA1PRNGKeyDerivator internal records; every caller is UNREACHABLE
sup(('InsecureSHA1PRNGKeyDerivator.deriveInsecureKey', 'InsecureSHA1PRNGKeyDerivator.<init>'),  # line 35
    ('InsecureSHA1PRNGKeyDerivator.deriveInsecureKey', 'InsecureSHA1PRNGKeyDerivator.setSeed'),  # line 36
    ('InsecureSHA1PRNGKeyDerivator.deriveInsecureKey', 'InsecureSHA1PRNGKeyDerivator.nextBytes'),  # line 38
    ('InsecureSHA1PRNGKeyDerivator.setSeed', 'InsecureSHA1PRNGKeyDerivator.updateSeed'),  # line 206
    ('InsecureSHA1PRNGKeyDerivator.updateSeed', 'InsecureSHA1PRNGKeyDerivator.updateHash'),  # line 181
    ('InsecureSHA1PRNGKeyDerivator.nextBytes', 'InsecureSHA1PRNGKeyDerivator.computeHash'),  # line 309
    ('InsecureSHA1PRNGKeyDerivator.updateHash', 'InsecureSHA1PRNGKeyDerivator.computeHash'))  # line 478

# ---- sup pairs (2): cross-batch, the caller Encryptor.deriveKeyInsecurely is batch 097's and is UNREACHABLE (no caller; Encryptor.java:130 is commented out)
sup(('Encryptor.deriveKeyInsecurely', 'InsecureSHA1PRNGKeyDerivator.<clinit>'),  # Encryptor.java:65
    ('Encryptor.deriveKeyInsecurely', 'InsecureSHA1PRNGKeyDerivator.deriveInsecureKey'))  # Encryptor.java:65

# ---- sup pairs (3): SimpleCrypto internal records; the callers are the closed String methods or the no-caller methods
sup(('SimpleCrypto.encrypt(String,String)', 'SimpleCrypto.getRawKey'),  # line 36
    ('SimpleCrypto.encrypt(String,String)', 'SimpleCrypto.encrypt(byte[],byte[])'),  # line 38
    ('SimpleCrypto.encrypt(String,String)', 'SimpleCrypto.toHex(byte[])'),  # line 39
    ('SimpleCrypto.decrypt(String,String)', 'SimpleCrypto.getRawKey'),  # line 43
    ('SimpleCrypto.decrypt(String,String)', 'SimpleCrypto.toByte'),  # line 44
    ('SimpleCrypto.decrypt(String,String)', 'SimpleCrypto.decrypt(byte[],byte[])'),  # line 45
    ('SimpleCrypto.toHex(String)', 'SimpleCrypto.toHex(byte[])'),  # line 82
    ('SimpleCrypto.fromHex', 'SimpleCrypto.toByte'),  # line 85
    ('SimpleCrypto.toHex(byte[])', 'SimpleCrypto.appendHex'))  # line 101

# ---- sup pairs (4): cross-batch, the callers are batch 038's (Passcode.java). Their calls sit under if (Build.VERSION.SDK_INT <= 23), false on API 27 (see the UNREACHABLE reasons below).
sup(('Passcode.decrypt', 'SimpleCrypto.decrypt(String,String)'),  # Passcode.java:105
    ('Passcode.encrypt', 'SimpleCrypto.encrypt(String,String)'))  # Passcode.java:124

# ---- UNREACHABLE: InsecureSHA1PRNGKeyDerivator (8). Detail and grep evidence: label_098.md rows, label_098.grep.txt sections A, B, E2, E3.

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.<clinit>'] = (
  'no_trigger_in_app',
  'static initializer of the constant tables. The only active use of the class is Encryptor.deriveKeyInsecurely (Encryptor.java:65), which has no caller (its only other mention, line 130, is commented out). No class file other than Encryptor.class refers to this class.',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:25, 48-138; SRC passcode/Encryptor.java:56-67, 130; grep label_098.grep.txt sections A, E2, E3',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.<init>'] = (
  'no_trigger_in_app',
  'private default constructor. Its only caller is deriveInsecureKey (line 35), which has no reachable caller.',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:35, 156; grep label_098.grep.txt section A',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.computeHash'] = (
  'no_trigger_in_app',
  'private static SHA-1 helper. Its callers are nextBytes (line 309) and updateHash (line 478), both reached only from deriveInsecureKey.',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:309, 353, 478; grep label_098.grep.txt sections A, E2',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.deriveInsecureKey'] = (
  'no_trigger_in_app',
  'public static entry point. Its only caller is Encryptor.deriveKeyInsecurely (Encryptor.java:65, batch 097), which has no caller. No class file calls it.',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:34-40; SRC passcode/Encryptor.java:56-67, 130; grep label_098.grep.txt sections A, E2, E3',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.nextBytes'] = (
  'no_trigger_in_app',
  'protected synchronized method. Its only caller is deriveInsecureKey (line 38).',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:38, 225, 309; grep label_098.grep.txt section A',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.setSeed'] = (
  'no_trigger_in_app',
  'private method. Its only caller is deriveInsecureKey (line 36).',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:36, 196, 206; grep label_098.grep.txt section A',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.updateHash'] = (
  'no_trigger_in_app',
  'private static method. Its only caller is updateSeed (line 181), which is reached only from setSeed (line 206).',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:181, 436, 478; grep label_098.grep.txt section A',
  'SOURCE')

UNREACHABLE['InsecureSHA1PRNGKeyDerivator.updateSeed'] = (
  'no_trigger_in_app',
  'private method. Its only caller is setSeed (line 206).',
  'SRC passcode/InsecureSHA1PRNGKeyDerivator.java:177-183, 206; grep label_098.grep.txt section A',
  'SOURCE')

# ---- UNREACHABLE: SimpleCrypto (11). The API-level claims rest on the standard configuration API 27 (handoff/SCHEMA_V2.md:38, 41), so they are INFERRED.

UNREACHABLE['SimpleCrypto.<init>'] = (
  'no_trigger_in_app',
  'implicit default constructor (the class declares none). No source or class file creates an instance; every use is a static call.',
  'SRC passcode/SimpleCrypto.java:33; SRC core/Passcode.java:105, 124; grep label_098.grep.txt sections A, E1',
  'SOURCE')

UNREACHABLE['SimpleCrypto.appendHex'] = (
  'closed_by_api_level',
  'private static helper. Its only caller is toHex(byte[]) (line 101), which is reached from encrypt(String,String) (line 39, closed) and from toHex(String) (line 82, no caller).',
  'SRC passcode/SimpleCrypto.java:96-108; SRC core/Passcode.java:120-133; grep label_098.grep.txt sections B, C',
  'INFERRED')

UNREACHABLE['SimpleCrypto.decrypt(String,String)'] = (
  'closed_by_api_level',
  'public static method. Its only caller is Passcode.decrypt (Passcode.java:105), under if (Build.VERSION.SDK_INT <= 23) (line 104). That is false on the standard configuration API 27 (handoff/SCHEMA_V2.md:38, 41), so the call never runs.',
  'SRC passcode/SimpleCrypto.java:42-47; SRC core/Passcode.java:101-113 (guard 104, call 105); handoff/SCHEMA_V2.md:38, 41; grep label_098.grep.txt section C',
  'INFERRED')

UNREACHABLE['SimpleCrypto.decrypt(byte[],byte[])'] = (
  'closed_by_api_level',
  'private static method. Its only caller is decrypt(String,String) (line 45), which is closed.',
  'SRC passcode/SimpleCrypto.java:45, 73-79',
  'INFERRED')

UNREACHABLE['SimpleCrypto.encrypt(String,String)'] = (
  'closed_by_api_level',
  'public static method. Its only caller is Passcode.encrypt (Passcode.java:124), under if (Build.VERSION.SDK_INT <= 23) (line 123). That is false on the standard configuration API 27 (handoff/SCHEMA_V2.md:38, 41), so the call never runs.',
  'SRC passcode/SimpleCrypto.java:35-40; SRC core/Passcode.java:120-133 (guard 123, call 124); handoff/SCHEMA_V2.md:38, 41; grep label_098.grep.txt section C',
  'INFERRED')

UNREACHABLE['SimpleCrypto.encrypt(byte[],byte[])'] = (
  'closed_by_api_level',
  'private static method. Its only caller is encrypt(String,String) (line 38), which is closed.',
  'SRC passcode/SimpleCrypto.java:38, 65-71',
  'INFERRED')

UNREACHABLE['SimpleCrypto.fromHex'] = (
  'no_trigger_in_app',
  'public static method. No caller in the source root; the text fromHex occurs only at its declaration. The class file mentions fromHex only inside SimpleCrypto.class.',
  'SRC passcode/SimpleCrypto.java:84-86; grep label_098.grep.txt sections B, E4, E5',
  'SOURCE')

UNREACHABLE['SimpleCrypto.getRawKey'] = (
  'closed_by_api_level',
  'private static method. Its callers are encrypt(String,String) (line 36) and decrypt(String,String) (line 43), both closed.',
  'SRC passcode/SimpleCrypto.java:36, 43, 49-63',
  'INFERRED')

UNREACHABLE['SimpleCrypto.toByte'] = (
  'closed_by_api_level',
  'public static method. Its callers are decrypt(String,String) (line 44, closed) and fromHex (line 85, no caller).',
  'SRC passcode/SimpleCrypto.java:44, 85, 88-94',
  'INFERRED')

UNREACHABLE['SimpleCrypto.toHex(String)'] = (
  'no_trigger_in_app',
  'public static method. Nothing calls it: the calls at line 39 pass a byte array to toHex(byte[]), and the text match at line 82 is inside toHex(String) itself, which has no caller.',
  'SRC passcode/SimpleCrypto.java:39, 81-83; grep label_098.grep.txt sections B, E4, E6',
  'SOURCE')

UNREACHABLE['SimpleCrypto.toHex(byte[])'] = (
  'closed_by_api_level',
  'public static method. Its callers are encrypt(String,String) (line 39, closed) and toHex(String) (line 82, no caller).',
  'SRC passcode/SimpleCrypto.java:39, 82, 96-103',
  'INFERRED')

# ---- REACHABLE: Recurrence (4) have no edge written here; their routes are auto CALL records (see the header). No UNREACHABLE entries.

# ---- part 099 (2026-10-29)
# ================================================================== batch 099 (label_099): com.money.manager.ex.recurring.transactions.RecurringTransactionEditActivity (methods 1-40 of 41 in this class group; the 41st, RecurringTransactionEditActivity$4.onClick, is in another batch and its GUI edge is written there)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_099.md (40 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE).
# Grep and sed evidence: graphs/MMEX/parts/label_099.grep.txt.
# This file writes 20 e() edges and 5 gui() edges (25 edges), one SCREENS key, 0 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). The INTENT edge from RecurringTransactionListFragment is interim: that class belongs to batch 102, which is not merged.
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here (D7).
# REGISTER edges are skipped by reachability (label_032.py:13), so the onEvent methods are reached through their ASYNC posts.
# Framework claims cite FW-SRC lines printed for this batch; other claims are INFERRED where the source was not read.

SCREENS.update({
    'S_RECURRING_TRANSACTION_EDIT': 'Recurring transaction edit form (RecurringTransactionEditActivity): payment date with the day arrows, the frequency spinner, payments left, the shared transaction controls, save and cancel',
})

# ---- the intent into the activity, then the lifecycle calls

e('RecurringTransactionListFragment.startRecurringTransactionEditActivity', 'RecurringTransactionEditActivity.<init>', 'INTENT',
  'the recurring transaction list starts the editor: ACTION_EDIT with KEY_BILL_DEPOSITS_ID when an id is passed, otherwise ACTION_INSERT',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:447-458 (ACTION_EDIT with KEY_BILL_DEPOSITS_ID when the id is not null, else ACTION_INSERT; startActivityForResult); callers at 128 (FAB) and 204 (menu_edit); that class belongs to batch 102, which is not merged, so this INTENT edge is interim')

e('RecurringTransactionEditActivity.<init>', 'RecurringTransactionEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('RecurringTransactionEditActivity.onCreate', 'RecurringTransactionEditActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity: ActivityThread calls callCallActivityOnSaveInstanceState, which calls onSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3873-3876 (callCallActivityOnSaveInstanceState at 3875); FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState at 1496)')

# ---- the screen, and the options menu built by the window

e('RecurringTransactionEditActivity.onCreate', 'S_RECURRING_TRANSACTION_EDIT', 'ENTERS',
  'the recurring transaction edit form is shown',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:98 (setContentView R.layout.activity_edit_recurring_transaction)')

e('RecurringTransactionEditActivity.onCreate', 'RecurringTransactionEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:631 (cb.onCreatePanelMenu); FW-SRC core/java/android/app/Activity.java:3386-3388 (onCreatePanelMenu calls onCreateOptionsMenu at 3388); INFERRED: the AppCompat delegate between the window and the activity is not read')

# ---- Icepick: the generated helper and the icepick library are not in the dataset (INFERRED)

e('MmxBaseFragmentActivity.onCreate', 'RecurringTransactionEditActivity$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State fields: the library loads the generated helper RecurringTransactionEditActivity$$Icepick by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState, before super.onCreate at 76); SRC recurring/transactions/RecurringTransactionEditActivity.java:63 (import icepick.State), 90 (@State String mIntentAction); INFERRED: the icepick library and its reflection are not in the dataset, source not read')

e('MmxBaseFragmentActivity.onCreate', 'RecurringTransactionEditActivity$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState); SRC recurring/transactions/RecurringTransactionEditActivity.java:90 (@State field); INFERRED: the icepick library is not in the dataset, source not read')

e('MmxBaseFragmentActivity.onCreate', 'RecurringTransactionEditActivity$$Icepick.restore', 'FRAMEWORK',
  'Icepick calls the generated restore for the @State field mIntentAction',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState); SRC recurring/transactions/RecurringTransactionEditActivity.java:90 (@State field); INFERRED: the icepick library is not in the dataset, source not read')

e('MmxBaseFragmentActivity.onSaveInstanceState', 'RecurringTransactionEditActivity$$Icepick.save', 'FRAMEWORK',
  'Icepick calls the generated save for the @State field mIntentAction',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at MmxBaseFragmentActivity.java:155)',
  evidence='SRC common/MmxBaseFragmentActivity.java:155 (Icepick.saveInstanceState); SRC recurring/transactions/RecurringTransactionEditActivity.java:90 (@State field); INFERRED: the icepick library is not in the dataset, source not read')

# ---- frequency spinner: the framework clears its selection while the listener is attached

e('RecurringTransactionEditActivity.initializeControls', 'RecurringTransactionEditActivity$1.onNothingSelected', 'FRAMEWORK',
  'the framework calls onNothingSelected when the frequency spinner loses its selected row after the listener is attached; the initial setSelection (line 328) runs before the listener is set (line 329), so it does not reach this method',
  needs_state=state_text('the frequency spinner had a selected row and its data changes so that no row is selected (the spinner adapter is static, so this is doubtful)', ('data',)),
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:328-329 (setSelection, then setOnItemSelectedListener); 339-342 (onNothingSelected: setRecurrence NOT_SET at 340, showPaymentsLeft at 341); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onNothingSelected at 947 for a negative position); AbsSpinner.java is not in fw_src, so the path from the data change to fireOnSelected is INFERRED')

# ---- payment date picker: the OK button runs the lambda listener

e('RecurringTransactionEditActivity$2.onClick', 'RecurringTransactionEditActivity$2.lambda$onClick$0', 'FRAMEWORK',
  'the user taps OK in the date picker: DatePickerDialog calls the OnDateSetListener, which is this lambda, and the lambda calls setPaymentDate',
  gui=['Tap the payment date text, then tap OK in the date picker'],
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:360-363 (lambda listener; setPaymentDate at 362); 365-374 (DatePickerDialog built with the listener; show at 374); FW-SRC core/java/android/app/DatePickerDialog.java:164-171 (onDateSet at 171); INFERRED: the dialog button dispatch to DatePickerDialog.onClick is not read (AlertController not read)')

# ---- EventBus: the activity registers in onStart; the posts are ASYNC edges

e('MmxBaseFragmentActivity.onStart', 'RecurringTransactionEditActivity.onEvent(AmountEnteredEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at RecurringTransactionEditActivity.java:219',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC recurring/transactions/RecurringTransactionEditActivity.java:219-224; INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'RecurringTransactionEditActivity.onEvent(DialogNegativeClickedEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at RecurringTransactionEditActivity.java:231',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC recurring/transactions/RecurringTransactionEditActivity.java:231-234; INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'RecurringTransactionEditActivity.onEvent(DialogPositiveClickedEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at RecurringTransactionEditActivity.java:226',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC recurring/transactions/RecurringTransactionEditActivity.java:226-229; INFERRED EventBus library not read')

e('AmountInputDialog$7.onClick', 'RecurringTransactionEditActivity.onEvent(AmountEnteredEvent)', 'ASYNC',
  'the amount dialog OK button posts AmountEnteredEvent on the EventBus, and the subscriber on the activity runs',
  cls='non_standard', via='EventBus (greenrobot) post at AmountInputDialog.java:260 (auto record AmountInputDialog$7.onClick -> AmountEnteredEvent.<init>, line 260); subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC common/AmountInputDialog.java:258-262 (post at 260); SRC recurring/transactions/RecurringTransactionEditActivity.java:219-224; INFERRED EventBus delivery (library not read)')

e('YesNoDialog$2.onClick', 'RecurringTransactionEditActivity.onEvent(DialogPositiveClickedEvent)', 'ASYNC',
  'the Yes button of the transfer warning posts DialogPositiveClickedEvent on the EventBus, and the subscriber on the activity runs',
  cls='non_standard', via='EventBus (greenrobot) post at YesNoDialog.java:73 (auto record YesNoDialog$2.onClick -> DialogPositiveClickedEvent.<init>, line 73); subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC transactions/YesNoDialog.java:65-83 (post at 73 in the positive listener, $2); SRC recurring/transactions/RecurringTransactionEditActivity.java:226-229; INFERRED EventBus delivery (library not read)')

e('YesNoDialog$1.onClick', 'RecurringTransactionEditActivity.onEvent(DialogNegativeClickedEvent)', 'ASYNC',
  'the No button of the transfer warning posts DialogNegativeClickedEvent on the EventBus, and the subscriber on the activity runs',
  cls='non_standard', via='EventBus (greenrobot) post at YesNoDialog.java:81 (auto record YesNoDialog$1.onClick -> DialogNegativeClickedEvent.<init>, line 81); subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC transactions/YesNoDialog.java:65-83 (post at 81 in the negative listener, $1); SRC recurring/transactions/RecurringTransactionEditActivity.java:231-234; INFERRED EventBus delivery (library not read)')

# ---- results returned to onActivityResult (the framework calls it through dispatchActivityResult)

e('PayeeListFragment.sendResultToActivity', 'RecurringTransactionEditActivity.onActivityResult', 'RESULT',
  'the payee list returns the picked payee and finishes: setResult(RESULT_OK, result), and the framework calls onActivityResult',
  guard='the payee activity is started with ACTION_PICK (EditTransactionCommonFunctions.java:573-576), and the ACTION_PICK path calls sendResultToActivity (PayeeListFragment.java:309)',
  evidence='SRC fragment/PayeeListFragment.java:309 (setResult calls sendResultToActivity on the pick path), 324-331 (sendResultToActivity; setResult(RESULT_OK, result) at 329); SRC transactions/EditTransactionCommonFunctions.java:573-576 (PayeeActivity start); FW-SRC core/java/android/app/ActivityThread.java:4253-4266 (deliverResults calls dispatchActivityResult); INFERRED: the dispatchActivityResult to onActivityResult step (Activity.java near 7259-7266) is not printed for this batch')

e('CategoryListFragment.setResult', 'RecurringTransactionEditActivity.onActivityResult', 'RESULT',
  'the category list returns the picked category and finishes: setResult(RESULT_OK, result), and the framework calls onActivityResult',
  guard='the category activity is started with ACTION_PICK (EditTransactionCommonFunctions.java:461-466)',
  evidence='SRC common/CategoryListFragment.java:313 (setResult), 354 (RESULT_OK in the same method, per grep.txt section 6); SRC transactions/EditTransactionCommonFunctions.java:461-466 (CategoryListActivity start with ACTION_PICK); INFERRED: the framework dispatch step is as for PayeeListFragment (ActivityThread.java:4253-4266)')

e('SplitCategoriesActivity.onActionDoneClick', 'RecurringTransactionEditActivity.onActivityResult', 'RESULT',
  'the split categories editor returns the splits and finishes: setResult(RESULT_OK, result) in onActionDoneClick, and the framework calls onActivityResult',
  guard='the editor is started with RequestCodes.SPLIT_TX (EditTransactionCommonFunctions.java:1528, in showSplitCategoriesForm at 1511)',
  evidence='SRC transactions/SplitCategoriesActivity.java:149 (onActionDoneClick), 174 (setResult RESULT_OK); SRC transactions/EditTransactionCommonFunctions.java:1511-1528 (startActivityForResult with RequestCodes.SPLIT_TX at 1528); INFERRED: the framework dispatch step is as for PayeeListFragment (ActivityThread.java:4253-4266)')

# ---- GUI edges from the form S_RECURRING_TRANSACTION_EDIT (page -> method)

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity.onOptionsItemSelected',
    'Tap the up arrow or the save icon in the toolbar',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:166-175 (home 168-169; save 170-171); SRC core/MenuHelper.java:37 (save = 2), 87-89 (addSaveToolbarIcon); FW-SRC core/java/android/app/Activity.java:3450 (onOptionsItemSelected dispatch); INFERRED: the toolbar tap reaching onMenuItemSelected through AppCompat is not read')

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity.onBackPressed',
    'Press the Back key',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:201-204 (onBackPressed calls onActionCancelClick at 203); FW-SRC core/java/android/app/Activity.java:3001 (onBackPressed); INFERRED: the AppCompat key dispatch to onBackPressed is not read')

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity$1.onItemSelected',
    'Pick a frequency in the frequency spinner (spinnerFrequencies)',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:329-336 (listener; onItemSelected 331-336); SRC res/layout/activity_edit_recurring_transaction.xml:276 (spinnerFrequencies); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onItemSelected at 944); INFERRED: the drop-down click path to setSelection is not read')

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity$2.onClick',
    'Tap the payment date text (paymentDateTextView)',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:355-376 (listener 355; onClick 357-375; DatePickerDialog show at 374); SRC res/layout/activity_edit_recurring_transaction.xml:117 (paymentDateTextView)')

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity$3.onClick',
    'Tap the previous-day button (paymentPreviousDayButton)',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:382-388 (listener 382; onClick 384-387; setPaymentDate at 386); SRC res/layout/activity_edit_recurring_transaction.xml:108 (paymentPreviousDayButton)')

# RecurringTransactionEditActivity$4.onClick (the next-day button, layout line 127) is in another batch: its GUI edge is written there.

# ---- part 100 (2026-10-29)
# ---- batch 100: RecurringTransactionEditActivity$4.onClick (1 method; rows in label_100.md, evidence in label_100.grep.txt)
# Edges are written only for destinations owned by this batch (D1). The auto CALL records out of $4.onClick (plusDays, toDate, getPaymentDate, setPaymentDate, the MmxDate constructor) and the record that creates $4 (initializePaymentDateSelector -> $4.<init>, line 390) are in auto_calls.json, so none is written here (D7).
# UNREACHABLE entries: none (the method is REACHABLE). sup pairs: none (no UNREACHABLE caller in this batch).
# SCREENS key S_RECURRING_TRANSACTION_EDIT is defined once, in label_099.py (merged first); this batch reuses it.

# ---- the next-day chevron on the payment date row (listener set at RecurringTransactionEditActivity.java:390)

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity$4.onClick',
    'Tap the next-day chevron on the payment date row of the recurring transaction form',
    via='View.OnClickListener registered by setOnClickListener (line 390); the framework calls onClick from performClick on a tap (FW-SRC View.java:6294)',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:390-396 (listener at 390; onClick 392-395; plusDays 393; setPaymentDate 394); SRC recurring/transactions/RecurringTransactionEditActivity.java:346-347 (early return only when paymentDateTextView is null), 419 (view set), 282 (initializePaymentDateSelector call), 280 (initializeControls), 136 (initializeControls call from onCreate); SRC res/layout/activity_edit_recurring_transaction.xml:127 (paymentNextDayButton), 100-145 (no visibility attribute); FW-SRC core/java/android/view/View.java:6143-6147 (setOnClickListener), 6289-6295 (performClick calls onClick at 6294), 12999 and 13029-13045 (a tap calls performClick); INFERRED com.shamanland.fonticon.FontIconView source not read')

# ---- part 101 (2026-10-29)
# batch 101 (label_101): RecurringTransactionEditActivity_MembersInjector (5 methods: <init>, create, injectDatabase, injectDateUtils, injectMembers)
# and RecurringTransactionListActivity (4 methods: <clinit>, <init>, onActivityResult, onCreate). 9 methods in all.
# Rows and printed source lines: graphs/MMEX/parts/label_101.md. Grep and record output: graphs/MMEX/parts/label_101.grep.txt.
# CALL edges between batch methods and to other classes come from auto_calls.json. The injectDatabase and injectDateUtils
# records from DaggerMmxComponent (DaggerMmxComponent.java:418-419) are already there, so no edges are written for them (D7).
# The Dagger-generated MembersInjector class is not in the app source and its methods are INFERRED.
# PendingIntent.java is not in fw_src (grep section 7), so the notification tap route is INFERRED.

SCREENS.update({
    'S_RECURRING_LIST': 'Recurring transactions list (RecurringTransactionListActivity with RecurringTransactionListFragment): the scheduled bills and deposits; the only in-app start site is the due-bill notification (grep section 5)',
})

# ---- route from the due-bill notification (posted by RecurringTransactionNotifications.showNotification)
e('RecurringTransactionNotifications.showNotification', 'RecurringTransactionListActivity.<clinit>', 'INTENT',
  'the user taps the due-bill notification: the PendingIntent built in showNotification starts RecurringTransactionListActivity, and the class is initialised',
  env=env_text('the user taps the recurring transaction notification (the activity is started with INTENT_EXTRA_LAUNCH_NOTIFICATION)', ('system_event',)),
  needs_state=state_text('a due bill exists: the query at RecurringTransactionNotifications.java:68-78 returns a row, and the notification setting is on (MainActivity.java:1236-1237 gates the poster)', ('data', 'settings')),
  evidence='SRC RecurringTransactionNotifications.java:75-78 and 90-94; SRC RecurringTransactionListActivity.java:38 (static FRAGMENTTAG initialiser); FW-SRC core/java/android/app/Instrumentation.java:1143-1148 (clazz.newInstance); INFERRED PendingIntent.getActivity delivers the Intent (PendingIntent.java not in fw_src)')

e('RecurringTransactionNotifications.showNotification', 'RecurringTransactionListActivity.<init>', 'INTENT',
  'the framework creates the RecurringTransactionListActivity instance from the notification PendingIntent (no intent-filter, not exported)',
  env=env_text('the user taps the recurring transaction notification (the activity is started with INTENT_EXTRA_LAUNCH_NOTIFICATION)', ('system_event',)),
  needs_state=state_text('a due bill exists: the query at RecurringTransactionNotifications.java:68-78 returns a row, and the notification setting is on (MainActivity.java:1236-1237 gates the poster)', ('data', 'settings')),
  evidence='SRC RecurringTransactionNotifications.java:90-94; SRC AndroidManifest.xml:235 (no intent-filter); SRC RecurringTransactionListActivity.java:33; FW-SRC core/java/android/app/Instrumentation.java:1143-1148 (clazz.newInstance); INFERRED PendingIntent.getActivity delivers the Intent (PendingIntent.java not in fw_src)')

# ---- framework lifecycle and the list screen
e('RecurringTransactionListActivity.<init>', 'RecurringTransactionListActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (callActivityOnCreate, then performCreate)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2728-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1215 (performCreate); FW-SRC core/java/android/app/Activity.java:989-990 (onCreate); SRC RecurringTransactionListActivity.java:43')

e('RecurringTransactionListActivity.onCreate', 'S_RECURRING_LIST', 'ENTERS',
  'the recurring transactions list is shown: onCreate sets the base toolbar layout and the list fragment',
  evidence='SRC RecurringTransactionListActivity.java:43-69 (setContentView at 45; RecurringTransactionListFragment at 64)')

# ---- passcode gate: onCreate starts PasscodeActivity for a result, and the result comes back to onActivityResult
e('RecurringTransactionListActivity.onCreate', 'RecurringTransactionListActivity.onActivityResult', 'FRAMEWORK',
  'the passcode screen started at line 56 returns its result: the framework calls onActivityResult',
  needs_state=state_text('a passcode is set (settings): onCreate starts PasscodeActivity only when hasPasscode is true (RecurringTransactionListActivity.java:50-56)', ('settings',)),
  evidence='SRC RecurringTransactionListActivity.java:48-58 and 72; FW-SRC core/java/android/app/ActivityThread.java:4253-4265 (deliverResults) and 4312 (its call site); FW-SRC core/java/android/app/Activity.java:7259-7266 (dispatchActivityResult calls onActivityResult)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('RecurringTransactionEditActivity_MembersInjector.create', 'RecurringTransactionEditActivity_MembersInjector.<init>'),
    ('RecurringTransactionEditActivity_MembersInjector.injectMembers', 'RecurringTransactionEditActivity_MembersInjector.injectDateUtils'),
    ('RecurringTransactionEditActivity_MembersInjector.injectMembers', 'RecurringTransactionEditActivity_MembersInjector.injectDatabase'))

# ================================================================== UNREACHABLE (batch 101). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['RecurringTransactionEditActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller record is create (auto_calls record at RecurringTransactionEditActivity_MembersInjector.java:27), and create has no caller: the app source has no reference to the generated class, and no auto_calls record has create as destination.',
  'SRC app source grep for the injector name: no output (label_101.grep.txt section 1); INFERRED class-file grep (section 2); auto_calls record RecurringTransactionEditActivity_MembersInjector.java:27 (section 3)',
  'INFERRED')

UNREACHABLE['RecurringTransactionEditActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (takes the Provider and returns a MembersInjector). The component does not call it: DaggerMmxComponent.injectRecurringTransactionEditActivity calls the static injectDatabase and injectDateUtils directly (DaggerMmxComponent.java:418-419). No app source reference.',
  'SRC app source grep: no output (label_101.grep.txt section 1); INFERRED class-file grep (section 2); auto_calls records DaggerMmxComponent.java:418-419 (section 3)',
  'INFERRED')

UNREACHABLE['RecurringTransactionEditActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method of the MembersInjector interface. No caller: DaggerMmxComponent.class has no injectMembers string (count 0), and the app source has no reference. Its two outgoing CALL records (lines 33-34) are cut by sup. Its callees stay REACHABLE through the component.',
  'SRC app source grep: no output (label_101.grep.txt section 1); INFERRED class-file grep count 0 (section 2); auto_calls records RecurringTransactionEditActivity_MembersInjector.java:33-34 (section 3)',
  'INFERRED')

# ---- part 102 (2026-10-29)
# ================================================================== batch 102 (label_102): RecurringTransactionListFragment (22 methods), its anonymous listeners $1 to $5 (13 methods), RecurringTransactionListFragment_MembersInjector (4) and RecurringTransactionViewHolder.<init> (1). 40 methods (graphs/MMEX/scratch/batches/batch_102.txt).
# Rows: graphs/MMEX/parts/label_102.md (36 REACHABLE, 4 UNREACHABLE, 0 INCOMPLETE). Grep and class-file evidence: graphs/MMEX/parts/label_102.grep.txt (sections 1-5).
# SCREENS: none written here. S_RECURRING_LIST is already defined by batch 101 (label_101.py, merged into graph_def.py:8999) and is reused.
# Edges with a batch 102 method as destination (D1) are written here. ENTERS edges start from this batch's onActivityCreated, which owns the source.
# Not written (D7): every auto_calls.json CALL record, for example RecurringTransactionListActivity.onCreate -> RecurringTransactionListFragment.<init> (line 64), BaseListFragment$2.onClick -> onFloatingActionButtonClicked (cut by label_026 sup), and the Dagger chain DaggerMmxComponent.inject -> injectRecurringTransactionListFragment -> injectDateTimeUtilsLazy.
# Not written: the INTENT edge startRecurringTransactionEditActivity -> RecurringTransactionEditActivity.<init> (batch 099 writes it, label_099.py:16).

# ---- activity and drawer routes into the fragment

e('RecurringTransactionListActivity.onCreate', 'RecurringTransactionListFragment.onActivityCreated', 'FRAMEWORK',
  'the activity adds the fragment in a transaction (lines 66-67) and the framework calls onActivityCreated after the activity onCreate',
  evidence='SRC recurring/transactions/RecurringTransactionListActivity.java:64-67; INFERRED androidx FragmentManager commits the transaction and calls onActivityCreated (library not read); precedent label_008.py:48-50 (FRAMEWORK commit -> onActivityCreated)')

e('MainActivity.showFragment_Internal', 'RecurringTransactionListFragment.onActivityCreated', 'FRAMEWORK',
  'the drawer item (MainActivity.java:651-652) reaches showFragment_Internal, which replaces fragmentMain and commits; the framework then calls onActivityCreated',
  evidence='SRC home/MainActivity.java:1446-1466 (replace at 1462, addToBackStack at 1464, commit at 1466); INFERRED androidx FragmentManager calls onActivityCreated after the commit (library not read); precedent label_008.py:48-50 (AccountListFragment)')

e('MainActivity.showFragment(Class)', 'RecurringTransactionListFragment.<init>', 'CALL',
  'the drawer item menu_recurring_transaction calls showFragment(RecurringTransactionListFragment.class), which creates the fragment with classFragment.newInstance()',
  cls='non_standard', via='Class.newInstance reflection in MainActivity.showFragment(Class) (MainActivity.java:743)',
  evidence='SRC home/MainActivity.java:651-652 (case R.id.menu_recurring_transaction); SRC home/MainActivity.java:741-745 (newInstance at 743); precedent label_008.py:42-46 (AccountListFragment.<init>)')

e('RecurringTransactionListFragment.<init>', 'RecurringTransactionListFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the fragment is created; onCreate injects the Dagger component (line 120) and sets the options menu (line 122)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:117-123; INFERRED androidx Fragment lifecycle (library not read); same pattern as label_087.py (LIFECYCLE <init> -> onCreate)')

# ---- onActivityCreated: options menu, loader chain, page entry

e('RecurringTransactionListFragment.onActivityCreated', 'RecurringTransactionListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'setHasOptionsMenu(true) at line 101 makes the framework build the options menu with this fragment; onCreateOptionsMenu inflates menu_item_calendar (line 138) and calls super (line 135)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:101, 134-144; INFERRED androidx FragmentManager builds the options menu (library not read)')

e('RecurringTransactionListFragment.onActivityCreated', 'RecurringTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader(ID_LOADER_REPEATING, null, this) at line 109 starts the loader and the LoaderManager calls onCreateLoader',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:109, 218-232 (onCreateLoader builds the MmxCursorLoader at 228); INFERRED androidx LoaderManager.initLoader calls the LoaderCallbacks (library not read); precedent graph_def.py:950-962 (AccountListFragment loader chain)')

e('RecurringTransactionListFragment.onCreateLoader', 'RecurringTransactionListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:218-232, 246-262; INFERRED androidx Loader delivers its result to the callbacks (library not read)')

e('RecurringTransactionListFragment.onLoadFinished', 'RecurringTransactionListFragment.onLoaderReset', 'FRAMEWORK',
  'the LoaderManager resets the loader when it is restarted (restartLoader at lines 272, 290, 316 and 343) and calls onLoaderReset',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:235-243, 272, 290, 316-317, 343-344; INFERRED androidx LoaderManager resets and calls onLoaderReset (library not read); precedent graph_def.py:950-962 (AccountListFragment.onLoadFinished -> onLoaderReset)')

# ---- restarts that call onCreateLoader again (FRAMEWORK, destination is this batch's onCreateLoader)

e('RecurringTransactionListFragment.onQueryTextChange', 'RecurringTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader at line 272 reloads the list with the search text and the LoaderManager calls onCreateLoader again',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:267-274; grep.txt section 4 (restartLoader at 272); INFERRED androidx LoaderManager.restartLoader calls the callbacks (library not read)')

e('RecurringTransactionListFragment.onActivityResult', 'RecurringTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader at line 290 reloads the list after RESULT_OK and the LoaderManager calls onCreateLoader again',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:277-292; INFERRED androidx LoaderManager.restartLoader calls the callbacks (library not read)')

e('RecurringTransactionListFragment$2.onClick', 'RecurringTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader at lines 316-317 reloads the list after the delete and the LoaderManager calls onCreateLoader again',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:309-319; grep.txt section 2b ($2 refers to LoaderManager.restartLoader); INFERRED androidx LoaderManager.restartLoader calls the callbacks (library not read)')

e('RecurringTransactionListFragment$4.onClick', 'RecurringTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader at lines 343-344 reloads the list after moveNextOccurrence and the LoaderManager calls onCreateLoader again',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:338-346; grep.txt section 2b ($4 refers to LoaderManager.restartLoader); INFERRED androidx LoaderManager.restartLoader calls the callbacks (library not read)')

# ---- page entry: the list page S_RECURRING_LIST (key defined by batch 101)

e('RecurringTransactionListFragment.onActivityCreated', 'S_RECURRING_LIST', 'ENTERS',
  'the list page is shown when onActivityCreated builds the list; both the activity route and the drawer route reach this method',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:94-114; SRC recurring/transactions/RecurringTransactionListActivity.java:64-67; SRC home/MainActivity.java:651-652, 1462')

# ---- calendar: the Caldroid library callback after the view is created (library not in the repo)

e('RecurringTransactionListFragment.showCaldroidFragment', 'RecurringTransactionListFragment$5.onCaldroidViewCreated', 'FRAMEWORK',
  'the Caldroid library calls onCaldroidViewCreated after it creates the calendar view for the fragment; the listener is set at line 380 and the fragment is shown at line 384',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:357-387 (getCalendarListener at 380; replace(R.id.fragmentMain) at 384); SRC same file 406-408 (empty body); INFERRED Caldroid library callback (library not in the repo; grep.txt section 1)')

# ---- result of the edit forms: RESULT edges into this batch's onActivityResult

e('RecurringTransactionEditActivity.onActionDoneClick', 'RecurringTransactionListFragment.onActivityResult', 'RESULT',
  'the edit form saves, calls setResult(RESULT_OK) and finishes; the result returns to the activity that started it, and the fragment (started at line 458) receives it in onActivityResult',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:207-211 (setResult at 210); SRC recurring/transactions/RecurringTransactionListFragment.java:447-459 (startActivityForResult at 458); INFERRED androidx FragmentActivity dispatches the result to the fragment (library not read); precedent graph_def.py:1656 (BudgetListFragment RESULT edge)')

e('CheckingTransactionEditActivity.onActionDoneClick', 'RecurringTransactionListFragment.onActivityResult', 'RESULT',
  'the checking transaction editor opened for a new transaction saves, calls setResult(RESULT_OK) and finishes; the fragment started it at line 437 and receives the result in onActivityResult',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:194-197 (setResult at 196); SRC recurring/transactions/RecurringTransactionListFragment.java:427-438 (startActivityForResult at 437); INFERRED androidx FragmentActivity dispatches the result to the fragment (library not read)')

# ---- GUI edges from the list page S_RECURRING_LIST (D6, D9: dialogs and calendar belong to the list page)

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onFloatingActionButtonClicked', 'Tap the add (floating action) button',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:126-129 (startRecurringTransactionEditActivity at 128); the FAB click listener BaseListFragment$2.onClick (BaseListFragment.java:244) is cut by label_026.py sup, and its comment says the owning batch writes this GUI edge')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onListItemClick', 'Tap a bill or deposit row (the row opens its context menu)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:156-161 (openContextMenu(v) at 160); auto_calls record AbsListFragment$1.onItemClick -> onListItemClick (AbsListFragment.java:44) is not repeated (D7)')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onCreateContextMenu', 'Long-press a row (registerForContextMenu is called at line 102)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:102, 164-176 (contextmenu_repeating_transactions inflated at 174); res/menu/contextmenu_repeating_transactions.xml:20, 24, 28, 32')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onContextItemSelected', 'Tap an item of the row context menu',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:179-213 (branches at 196, 200, 204, 208); res/menu/contextmenu_repeating_transactions.xml:20, 24, 28, 32')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onOptionsItemSelected', 'Tap the calendar icon in the action bar (menuCalendar)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:147-153 (menuCalendar check at 149; showCaldroidFragment at 150); res/menu/menu_item_calendar.xml:22')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onQueryTextChange', 'Type in the search box of the list',
  evidence='SRC common/BaseListFragment.java:128 (BaseListFragment$1.onQueryTextChange, auto_calls 4602); SRC recurring/transactions/RecurringTransactionListFragment.java:267-274; auto_calls record BaseListFragment.onPreQueryTextChange@RecurringTransactionListFragment -> onQueryTextChange (line 226) is not repeated (D7)')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$1.onClick', 'Tap Cancel in the delete confirmation dialog (the dialog is shown on the list page, D9)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:320-325 (negative button; dialog.cancel() at 323); grep.txt section 2b ($1 refers only to DialogInterface.cancel)')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$2.onClick', 'Tap OK in the delete confirmation dialog (deletes the bill or deposit and reloads the list)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:309-319 (RecurringTransactionService delete at 313; restartLoader at 316-317); grep.txt section 2b')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$3.onClick', 'Tap Cancel in the skip next occurrence dialog',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:347-352 (dialog.cancel() at 350); grep.txt section 2b ($3 refers only to DialogInterface.cancel)')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$4.onClick', 'Tap OK in the skip next occurrence dialog (moves to the next occurrence and reloads the list)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:338-346 (moveNextOccurrence at 342; restartLoader at 343-344); grep.txt section 2b')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$5.onSelectDate', 'Tap a date in the calendar (the calendar replaces the list in fragmentMain, D9)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:393-396 (comment only, empty body); SRC same file 384 (replace in fragmentMain); INFERRED Caldroid library calls onSelectDate on a tap (library not in the repo)')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$5.onLongClickDate', 'Long-press a date in the calendar',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:402-404 (empty body); INFERRED Caldroid library calls onLongClickDate on a long press (library not in the repo)')

# ================================================================== sup pairs (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('RecurringTransactionListFragment_MembersInjector.create', 'RecurringTransactionListFragment_MembersInjector.<init>'),
    ('RecurringTransactionListFragment_MembersInjector.injectMembers', 'RecurringTransactionListFragment_MembersInjector.injectDateTimeUtilsLazy'))

# ================================================================== UNREACHABLE (batch 102). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['RecurringTransactionListFragment_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller is create (auto_calls record RecurringTransactionListFragment_MembersInjector.java:25), and create has no caller: no class file refers to create (grep.txt section 2c).',
  'grep.txt sections 2c and 3; python-printed auto_calls record RecurringTransactionListFragment_MembersInjector.java:25',
  'INFERRED')

UNREACHABLE['RecurringTransactionListFragment_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated factory method. No class file refers to create (grep.txt section 2c: none), and no app source names the injector (grep.txt section 1: no hits). DaggerMmxComponent calls the static injectDateTimeUtilsLazy directly (DaggerMmxComponent.java:466), not create.',
  'grep.txt sections 1, 2c and 3; DaggerMmxComponent.java:466 (auto_calls record)',
  'INFERRED')

UNREACHABLE['RecurringTransactionListFragment_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated typed instance method (the synthetic bridge injectMembers(Object) is not in this batch, same convention as batch 087). No class file refers to it (grep.txt section 2c), so its only outgoing record injectMembers -> injectDateTimeUtilsLazy (MembersInjector.java:30) is cut by the sup pair.',
  'grep.txt sections 2c and 3; python-printed auto_calls record RecurringTransactionListFragment_MembersInjector.java:30',
  'INFERRED')

UNREACHABLE['RecurringTransactionListFragment$5.onChangeMonth'] = ('no_trigger_in_app',
  'Caldroid month-change callback with an empty body (lines 398-400). The calendar is set with SHOW_NAVIGATION_ARROWS and ENABLE_SWIPE both false (lines 372-373), and no app code calls moveToDate, prevMonth or nextMonth (grep.txt section 1), so no user or app action changes the month. The library behaviour itself is INFERRED because the library is not in the repo.',
  'SRC recurring/transactions/RecurringTransactionListFragment.java:372-373, 398-400; grep.txt section 1 (no hits for moveToDate, prevMonth, nextMonth)',
  'INFERRED')

# ---- part 103 (2026-10-29)
# ================================================================== batch 103 (label_103): BaseReportFragment (+ $1, _MembersInjector), CategoriesReportActivity, CategoriesReportAdapter, CategoriesReportFragment (+ $1)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_103.md. Class-file and grep evidence: graphs/MMEX/parts/label_103.grep.txt.
# Edges below have a batch 103 method (or S_CATEGORIES_REPORT) as destination. The INTENT source MainActivity.onDrawerMenuAndOptionMenuSelected belongs to another batch (D1).
# CALL edges already in auto_calls.json are not written here (D7).

SCREENS.update({
    'S_CATEGORIES_REPORT': 'Categories report (CategoriesReportActivity hosts CategoriesReportFragment): totals per category and subcategory for the selected period; the options menu chooses the period, custom dates or the pie chart; a tap on a row opens the search results for that category',
})

# ---- activity, page entry and fragment lifecycle

e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'CategoriesReportActivity.<init>', 'INTENT',
  'the Categories report, Where the money goes or Where the money comes from item of the main menu starts CategoriesReportActivity with an explicit intent (the two money items also pass REPORT_FILTERS Withdrawal or Deposit and a REPORT_TITLE)',
  gui=['Tap Categories report, Where the money goes or Where the money comes from in the main menu (drawer or options menu)'],
  evidence='SRC home/MainActivity.java:589 (method), 661-663, 670-675, 676-681 (case labels, new Intent and startActivity); SRC AndroidManifest.xml:292-294 (no intent-filter, so only explicit intents reach it); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (newActivity constructs the class)')

e('CategoriesReportActivity.<init>', 'CategoriesReportActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the activity is constructed',
  evidence='SRC CategoriesReportActivity.java:28-29, 37; INFERRED Android Activity lifecycle order (framework Activity.java not printed)')

e('CategoriesReportActivity.onCreate', 'S_CATEGORIES_REPORT', 'ENTERS',
  'the categories report page is shown: onCreate sets the layout and adds CategoriesReportFragment to fragmentMain when no fragment is there yet',
  evidence='SRC CategoriesReportActivity.java:36-68 (setContentView 49; mIsDualPanel 57; fragment 60; add 63-67)')

e('CategoriesReportFragment.<init>', 'BaseReportFragment.onCreate', 'LIFECYCLE',
  'CategoriesReportActivity.onCreate commits the transaction that adds the fragment (add at 63-66) and the FragmentManager then calls onCreate',
  evidence='SRC CategoriesReportActivity.java:60-67; SRC BaseReportFragment.java:67-72; INFERRED androidx Fragment lifecycle (library not read)')

e('BaseReportFragment.onCreate', 'CategoriesReportFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onCreate; CategoriesReportFragment overrides it and its super call (line 99) runs BaseReportFragment.onActivityCreated',
  evidence='SRC BaseReportFragment.java:67-72; SRC CategoriesReportFragment.java:66-100; INFERRED androidx Fragment lifecycle (library not read)')

e('CategoriesReportFragment.onActivityCreated', 'BaseReportFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework calls onSaveInstanceState on the fragment after its view is created (the inherited body runs, because CategoriesReportFragment does not override it); same chain as label_087',
  evidence='SRC CategoriesReportFragment.java:66-100 (no onSaveInstanceState in the class); SRC BaseReportFragment.java:227-238; INFERRED androidx Fragment saves state (library not read); precedent label_087')

# ---- framework dispatch from the fragment base class

e('BaseReportFragment.onActivityCreated', 'CategoriesReportFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'setHasOptionsMenu(true) (line 79) makes the framework build the options menu: it calls onCreateOptionsMenu on the fragment (the override calls super at 104)',
  evidence='SRC BaseReportFragment.java:74-79; SRC CategoriesReportFragment.java:102-113; precedent label_026 (setHasOptionsMenu); INFERRED androidx FragmentManager dispatches onCreateOptionsMenu (library not read)')

e('BaseReportFragment.startLoader', 'BaseReportFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader (line 262) creates the loader through the LoaderCallbacks of this fragment, which calls onCreateLoader',
  evidence='SRC BaseReportFragment.java:115-116, 261-263; INFERRED androidx LoaderManager.restartLoader calls LoaderCallbacks.onCreateLoader (library not read)')

e('BaseReportFragment.onCreateLoader', 'CategoriesReportFragment.onLoadFinished', 'FRAMEWORK',
  'the loader delivers its cursor and the LoaderManager calls onLoadFinished on this fragment (the override in CategoriesReportFragment, which calls super at 119)',
  evidence='SRC BaseReportFragment.java:115-132, 142-151; SRC CategoriesReportFragment.java:117-119; INFERRED androidx LoaderManager delivers the result to LoaderCallbacks (library not read); precedent label_087')

e('BaseReportFragment.startLoader', 'BaseReportFragment.onLoaderReset', 'FRAMEWORK',
  'restartLoader retires the previous loader and the LoaderManager calls onLoaderReset (INFERRED: the reset of a restarted loader is androidx behaviour, not read)',
  evidence='SRC BaseReportFragment.java:134-139, 261-263; INFERRED androidx LoaderManager calls onLoaderReset on reset (library not read)')

e('BaseReportFragment.onLoadFinished', 'CategoriesReportAdapter.newView', 'FRAMEWORK',
  'changeCursor (line 144) makes the list draw its rows; CursorAdapter.getView calls newView for a row that has no convertView',
  evidence='SRC BaseReportFragment.java:141-151; SRC CategoriesReportAdapter.java:86-89; FW-SRC core/java/android/widget/CursorAdapter.java:276-290 (analogue at 285; the androidx class is not in fw_src); INFERRED androidx CursorAdapter.changeCursor and getView (library not read)')

e('BaseReportFragment.onLoadFinished', 'CategoriesReportAdapter.bindView', 'FRAMEWORK',
  'as for newView: CursorAdapter.getView calls bindView for every row it draws',
  evidence='SRC BaseReportFragment.java:141-151; SRC CategoriesReportAdapter.java:55-84; FW-SRC core/java/android/widget/CursorAdapter.java:276-290 (analogue at 289; the androidx class is not in fw_src); INFERRED androidx CursorAdapter.getView (library not read)')

e('CategoriesReportFragment.onLoadFinished', 'CategoriesReportFragment$1.run', 'FRAMEWORK',
  'in dual-panel mode the fragment posts the Runnable with Handler.postDelayed (1000 ms) and the Handler runs it through handleCallback',
  guard='dual-panel layouts only: mIsDualPanel is true when the layout has fragmentChart (layout-sw600dp-land and layout-sw720dp-port; CategoriesReportActivity.java:57)',
  evidence='SRC CategoriesReportFragment.java:147-157; FW-SRC core/java/android/os/Handler.java:789-790; SRC CategoriesReportActivity.java:57; SRC res/layout-sw600dp-land/report_chart_fragments_activity.xml:38; SRC res/layout-sw720dp-port/report_chart_fragments_activity.xml:40')

# ---- user actions on the categories report page (GUI; page -> method, D6)

gui('S_CATEGORIES_REPORT', 'CategoriesReportFragment.onListItemClick',
    'Tap a category row in the report list (the search results for that category open)',
    evidence='SRC CategoriesReportFragment.java:272-294; SRC core/AbsListFragment.java:42-46 (OnItemClickListener calls onListItemClick); INFERRED the list view dispatches the item click to the listener (AdapterView not printed)')

gui('S_CATEGORIES_REPORT', 'CategoriesReportFragment.onOptionsItemSelected',
    'Options menu: tap Show chart (single-pane only), one of the period items (current month, last month, last 30 days, current year, last year, all time)',
    evidence='SRC CategoriesReportFragment.java:161-182 (menu_chart at 163); SRC BaseReportFragment.java:153-225 (period items); SRC res/menu/menu_report.xml:22-25; SRC res/menu/menu_period_picker.xml:22-47; INFERRED androidx dispatches the menu item to the fragment (library not read)')

gui('S_CATEGORIES_REPORT', 'CategoriesReportFragment.onQueryTextChange',
    'Type in the search box of the categories report',
    evidence='SRC common/BaseListFragment.java:112-131 (SearchView listener, onPreQueryTextChange at 128), 219-231; SRC CategoriesReportFragment.java:184-213; INFERRED androidx SearchView calls the listener on each text change (not in fw_src); precedent label_026')

gui('S_CATEGORIES_REPORT', 'BaseReportFragment$1.onClick',
    'Tap menu_custom_dates in the options menu, set the two dates in the dialog and tap OK',
    cls='non_standard',
    via='platform AlertDialog positive button: AlertController ButtonHandler sends the click to the OnClickListener (FW-SRC AlertController.java:125-146, 158-166)',
    evidence='SRC BaseReportFragment.java:195-201, 269-296 (dialog and positive listener); SRC res/menu/menu_period_picker.xml:29; SRC res/layout/dialog_choose_date_report.xml:32 and 48 (datePickerFromDate, datePickerToDate); FW-SRC core/java/com/android/internal/app/AlertController.java:125-146, 158-166; precedent label_093')

# ---- Dagger members injector: the static injector is the only reached method (auto CALL, not written here)
# The two sup pairs cut the auto records whose callers are UNREACHABLE (D14).

sup(('BaseReportFragment_MembersInjector.create', 'BaseReportFragment_MembersInjector.<init>'),
    ('BaseReportFragment_MembersInjector.injectMembers', 'BaseReportFragment_MembersInjector.injectDateTimeUtilsLazy'))

# ---- UNREACHABLE (no_trigger_in_app). Tuple: (kind, reason, evidence, confirmed_by). Evidence: graphs/MMEX/parts/label_103.grep.txt.

UNREACHABLE['BaseReportFragment_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller is create, and create has no caller: no class file refers to create (constant pool, grep section 2), and DaggerMmxComponent refers only to the static injectDateTimeUtilsLazy (section 2). The only auto record with this destination is create -> <init> (section 3), which the sup pair cuts.',
  'label_103.grep.txt sections 1, 2 and 3; auto_calls record BaseReportFragment_MembersInjector.java:24',
  'INFERRED')

UNREACHABLE['BaseReportFragment_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory method. No class file refers to it: the byte search finds the class name only in DaggerMmxComponent.class and in the injector class itself (section 1), and neither refers to create (section 2). No auto record has create as its destination (section 3). DaggerMmxComponent calls the static injectDateTimeUtilsLazy directly.',
  'label_103.grep.txt sections 1, 2 and 3',
  'INFERRED')

UNREACHABLE['BaseReportFragment_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance injector (takes a BaseReportFragment). No class file refers to it (section 2), and no auto record has it as destination (section 3). Its outgoing record injectMembers -> injectDateTimeUtilsLazy (line 29) is cut by the sup pair. The synthetic bridge injectMembers(Object) in the same class is not referred to by any class file (section 2).',
  'label_103.grep.txt sections 1, 2 and 3; auto_calls record BaseReportFragment_MembersInjector.java:29',
  'INFERRED')

# ---- part 104 (2026-10-29)
# batch 104: IncomeVsExpensesActivity (2), IncomeVsExpensesAdapter (3), IncomeVsExpensesChartFragment (13).
# Edges and UNREACHABLE entries only. Rows and printed lines: graphs/MMEX/parts/label_104.md.
# Every edge below has a batch 104 method as its destination (D1) or is a page edge (ENTERS, GUI).
# No CALL edge: every direct call between these methods is already an auto_calls.json record (D7).
# No method is UNREACHABLE, so there are no UNREACHABLE entries and no sup pairs.

SCREENS.update({
    'S_INCOME_VS_EXPENSES': 'Income vs. expenses report (IncomeVsExpensesActivity): a list of income, expenses and difference per month with a footer total; the bar chart of the same months is shown beside the list (dual panel) or in place of it (single panel, with back stack)',
})

# ---- IncomeVsExpensesActivity: started by the app only (no intent-filter, not exported)
e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'IncomeVsExpensesActivity.<init>', 'INTENT',
  'case R.id.menu_report_income_vs_expenses: startActivity(new Intent(this, IncomeVsExpensesActivity.class))',
  gui=['Open the navigation drawer and tap Income vs. Expenses'],
  evidence='SRC home/MainActivity.java:589, 609, 682-684; SRC home/MainActivity.java:918-921 (drawer child, always added); SRC home/MainActivity.java:967-981 (onChildClick posts this method after 200 ms, line 978); SRC AndroidManifest.xml:287-288; FW-SRC core/java/android/app/ActivityThread.java:2669-2670; FW-SRC core/java/android/app/Instrumentation.java:1170-1175')

e('MainActivity.onClickCardViewIncomesVsExpenses', 'IncomeVsExpensesActivity.<init>', 'INTENT',
  'onClickCardViewIncomesVsExpenses: startActivity(new Intent(this, IncomeVsExpensesActivity.class))',
  gui=['Tap the Income vs Expenses card on the home screen'],
  evidence='SRC home/MainActivity.java:832-834; the card GUI edge S_HOME -> this method is in label_080.py:131; SRC AndroidManifest.xml:287-288; FW-SRC core/java/android/app/ActivityThread.java:2669-2670; FW-SRC core/java/android/app/Instrumentation.java:1170-1175')

e('IncomeVsExpensesActivity.<init>', 'IncomeVsExpensesActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='SRC IncomeVsExpensesActivity.java:26, 33-35; FW-SRC core/java/android/app/Instrumentation.java:1212-1215; FW-SRC core/java/android/app/ActivityThread.java:2729-2731; FW-SRC core/java/android/app/Activity.java:6989-6999')

e('IncomeVsExpensesActivity.onCreate', 'S_INCOME_VS_EXPENSES', 'ENTERS',
  'the report is shown: onCreate inflates report_chart_fragments_activity and adds the list fragment to fragmentMain; the chart container fragmentChart exists only in dual panel (mIsDualPanel, line 46)',
  evidence='SRC IncomeVsExpensesActivity.java:36-54')

# ---- IncomeVsExpensesAdapter: rows are bound by the list when the report cursor has rows
e('IncomeVsExpensesListFragment.onLoadFinished', 'IncomeVsExpensesAdapter.newView', 'FRAMEWORK',
  'the report cursor has rows: onLoadFinished calls changeCursor (IncomeVsExpensesListFragment.java:162), which calls notifyDataSetChanged (CursorAdapter.java:381); the list lays out a row and calls getView (AbsListView.java:2365), which calls newView only when convertView is null (CursorAdapter.java:284-285)',
  needs_state=state_text('the income vs expenses query returns at least one row (the same cursor is checked at IncomeVsExpensesListFragment.java:183, data.getCount() > 0)', ('data',)),
  evidence='SRC IncomeVsExpensesListFragment.java:158-163, 183; FW-SRC core/java/android/widget/CursorAdapter.java:284-285, 348-350, 365-381; FW-SRC core/java/android/widget/AbsListView.java:2348, 2365; INFERRED observer path from notifyDataSetChanged to the list layout (AbsListView.java:6406-6407 read only as the entry point)')

e('IncomeVsExpensesListFragment.onLoadFinished', 'IncomeVsExpensesAdapter.bindView', 'FRAMEWORK',
  'the same route: each row the list lays out calls getView, which calls bindView (CursorAdapter.java:289) with the report cursor',
  needs_state=state_text('the income vs expenses query returns at least one row (the same cursor is checked at IncomeVsExpensesListFragment.java:183, data.getCount() > 0)', ('data',)),
  evidence='SRC IncomeVsExpensesListFragment.java:158-163, 183; FW-SRC core/java/android/widget/CursorAdapter.java:289, 348-350, 365-381; FW-SRC core/java/android/widget/AbsListView.java:2365; INFERRED observer path as for newView')

# ---- IncomeVsExpensesChartFragment: lifecycle chain from the fragment transaction in showChartInternal
e('IncomeVsExpensesChartFragment.<init>', 'IncomeVsExpensesChartFragment.onCreate', 'LIFECYCLE',
  'the fragment manager calls onCreate after the chart transaction is committed (showChartInternal creates the fragment at IncomeVsExpensesListFragment.java:513 and commits at 520-529)',
  evidence='SRC IncomeVsExpensesListFragment.java:508-529; SRC IncomeVsExpensesChartFragment.java:116-118; INFERRED androidx Fragment lifecycle (library source not in the dataset or fw_src, not read)')

e('IncomeVsExpensesChartFragment.onCreate', 'IncomeVsExpensesChartFragment.onCreateView', 'LIFECYCLE',
  'the fragment manager calls onCreateView after onCreate',
  evidence='SRC IncomeVsExpensesChartFragment.java:116-158; INFERRED androidx Fragment lifecycle (library source not read)')

e('IncomeVsExpensesChartFragment.onCreateView', 'IncomeVsExpensesChartFragment.onResume', 'LIFECYCLE',
  'the fragment manager resumes the fragment after its view is created; the second route is the explicit call at IncomeVsExpensesListFragment.java:518 (auto CALL record, no edge written, D7)',
  evidence='SRC IncomeVsExpensesChartFragment.java:139-164; INFERRED androidx Fragment lifecycle (library source not read)')

e('IncomeVsExpensesChartFragment.onResume', 'IncomeVsExpensesChartFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state when the activity leaves the foreground, after the fragment has been resumed (same pattern as label_010.py:47)',
  evidence='SRC IncomeVsExpensesChartFragment.java:160-180; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- GUI edges from the report page S_INCOME_VS_EXPENSES (page -> method)
gui('S_INCOME_VS_EXPENSES', 'IncomeVsExpensesChartFragment.onOptionsItemSelected', 'Tap the Up arrow in the toolbar while the chart is shown',
  evidence='SRC IncomeVsExpensesChartFragment.java:136, 166-173; SRC common/MmxBaseFragmentActivity.java:55, 107-130 (home branch returns only when mDisplayHomeAsUpEnabled is true, and it is false here); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected), 3597-3601 (returns false); INFERRED androidx FragmentActivity dispatch to the fragment and the toolbar Up click reaching onMenuItemSelected (androidx not read)')

gui('S_INCOME_VS_EXPENSES', 'IncomeVsExpensesChartFragment.onValueSelected', 'Tap a bar of the chart',
  evidence='SRC IncomeVsExpensesChartFragment.java:145, 210-213; INFERRED MPAndroidChart library (com.github.mikephil.charting, not in the dataset) calls OnChartValueSelectedListener.onValueSelected when a tap highlights a bar')

gui('S_INCOME_VS_EXPENSES', 'IncomeVsExpensesChartFragment.onNothingSelected', 'Tap the chart where no bar is highlighted',
  evidence='SRC IncomeVsExpensesChartFragment.java:145, 215-218; INFERRED MPAndroidChart library (not in the dataset) calls onNothingSelected')

# ---- part 105 (2026-10-29)
# ================================================================== batch 105 (label_105): reports.IncomeVsExpensesListFragment (16 methods, and the anonymous classes $1 to $4 with 8 methods) and reports.PayeeReportAdapter (3 methods). 27 methods in all.
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_105.md (27 REACHABLE, 0 UNREACHABLE).
# Grep and sed evidence: graphs/MMEX/parts/label_105.grep.txt.
# This file writes 12 e() edges and 2 gui() edges (14 edges), 0 SCREENS keys (S_INCOME_VS_EXPENSES is defined by batch 104 at label_104.py:7-8, so it is not redefined here), 0 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). These sources belong to other batches and are interim until those batches merge: IncomeVsExpensesActivity.onCreate (batch 104), MmxBaseFragmentActivity.onSaveInstanceState (common/, other batch), PayeeReportFragment.onLoadFinished (batch 106).
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here (D7).
# The dual-panel Runnable $1.run is gated by the device layout (env kind hardware: the fragmentChart view exists only in the sw600dp-land and sw720dp-port layouts), not by a setting, so it stays REACHABLE with that gate (D19).
# Framework claims cite FW-SRC lines printed for this batch; androidx claims (LoaderManager, Fragment) are INFERRED because the library is not in the dataset.

# ---- 1. the fragment is added by the activity (the activity is batch 104)

e('IncomeVsExpensesActivity.onCreate', 'IncomeVsExpensesListFragment.onActivityCreated', 'LIFECYCLE',
  'the activity adds the list fragment in onCreate when fragmentMain is empty; the fragment manager then calls onActivityCreated',
  evidence='SRC reports/IncomeVsExpensesActivity.java:31 (field initializer), 46 (mIsDualPanel), 50-53 (replace and commit when fragmentMain is empty); INFERRED androidx Fragment lifecycle (library not read)')

e('IncomeVsExpensesListFragment.onActivityCreated', 'IncomeVsExpensesListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'setHasOptionsMenu(true) at line 87 makes the framework build the options menu through onCreateOptionsMenu',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:87, 220-222; INFERRED androidx Fragment options-menu dispatch (library not read)')

# ---- 2. the loaders (LoaderManager is androidx: INFERRED)

e('IncomeVsExpensesListFragment.onActivityCreated', 'IncomeVsExpensesListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader(ID_LOADER_YEARS) at line 113: the LoaderManager calls onCreateLoader for the years loader (id 2)',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:113, 142-146; INFERRED androidx LoaderManager (library not read; LoaderManager.java is not in fw_src)')

e('IncomeVsExpensesListFragment.startLoader', 'IncomeVsExpensesListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader(ID_LOADER_REPORT) at line 410: the LoaderManager calls onCreateLoader for the report loader (id 1) with the year list in the bundle',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:401-410, 119-140; INFERRED androidx LoaderManager (library not read)')

e('IncomeVsExpensesListFragment.onCreateLoader', 'IncomeVsExpensesListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader returned by onCreateLoader (line 140 for the report, line 146 for the years) delivers its cursor, and the LoaderManager calls onLoadFinished',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:135-146, 158-162, 199-212; INFERRED androidx Loader delivery (library not read)')

e('IncomeVsExpensesListFragment.onLoadFinished', 'IncomeVsExpensesListFragment.onLoaderReset', 'FRAMEWORK',
  'the LoaderManager resets a loader that has delivered data (restartLoader in startLoader at line 410, or the fragment is destroyed); onLoaderReset then sets the adapter cursor to null',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:152-155, 410; INFERRED androidx LoaderManager reset path (LoaderManager.java is not in fw_src)')

# ---- 3. the state save (the activity's base class is in common/, another batch)

e('MmxBaseFragmentActivity.onSaveInstanceState', 'IncomeVsExpensesListFragment.onSaveInstanceState', 'LIFECYCLE',
  'the activity saves its state (a configuration change, or the activity is stopped); the fragment manager saves the list fragment, which writes the selected years into the bundle',
  evidence='SRC common/MmxBaseFragmentActivity.java:151-156 (Icepick.saveInstanceState at 155; this source is in another batch, so the edge is interim); SRC reports/IncomeVsExpensesListFragment.java:253-265; INFERRED androidx FragmentManager save path (library not read)')

# ---- 4. the year dialog (AlertDialog is framework source, read in fw_src)

e('IncomeVsExpensesListFragment.showDialogYears', 'IncomeVsExpensesListFragment$2.onClick', 'FRAMEWORK',
  'the OK button of the period dialog: setPositiveButton stores the listener, and a tap runs it; it resets mYearsSelected from checkedItems and restarts the report loader (startLoader, line 308)',
  guard='the user taps OK (android.R.string.ok) in the period dialog that menu_period opens (IncomeVsExpensesListFragment.java:244, 297-312)',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:291-312 (dialog; OK body 297-310, startLoader at 308, show at 312); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:160-166 (ButtonHandler calls onClick at 166); auto_calls.json impl map: $2 is onClick(DialogInterface;I)')

e('IncomeVsExpensesListFragment.showDialogYears', 'IncomeVsExpensesListFragment$3.onClick', 'FRAMEWORK',
  'a tap on a year row of the multi-choice list: the listener stores the new checked state in checkedItems, which the OK listener reads later',
  guard='the period dialog is open and the user taps a year row',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:291-296 (multi-choice body; checkedItems[which] = isChecked at 294); FW-SRC core/java/android/app/AlertDialog.java:834-838 (setMultiChoiceItems stores the listener at 837); FW-SRC core/java/com/android/internal/app/AlertController.java:1149-1156 (row tap calls mOnCheckboxClickListener.onClick at 1155); auto_calls.json impl map: $3 is onClick(DialogInterface;IZ)')

# ---- 5. the dual-panel chart (the Runnable is posted only when mIsDualPanel is true)

e('IncomeVsExpensesListFragment.onLoadFinished', 'IncomeVsExpensesListFragment$1.run', 'FRAMEWORK',
  'the report loader has data and the device shows the dual-panel layout: a Handler posts the Runnable with a 1000 ms delay, and the Runnable calls showChart on the main looper',
  env=env_text('tablet layout with the fragmentChart view (the sw600dp landscape or sw720dp portrait layout): IncomeVsExpensesActivity.java:46 sets mIsDualPanel only when fragmentChart exists (res layout-sw600dp-land line 38, layout-sw720dp-port line 40)', ('hardware',)),
  guard='mIsDualPanel is true (IncomeVsExpensesListFragment.java:188); the post runs only then',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:188-196 (guard 188; new Handler 189; postDelayed 190-195 with 1000 at 195; run calls showChart at 193); FW-SRC core/java/android/os/Handler.java:427-430 (postDelayed queues through sendMessageDelayed), 789-791 (handleCallback runs callback.run); SRC reports/IncomeVsExpensesActivity.java:46; res layout-sw600dp-land/report_chart_fragments_activity.xml:38 and layout-sw720dp-port/report_chart_fragments_activity.xml:40')

# ---- 6. the payee report adapter (the fragment is batch 106; the cursor change is in BaseReportFragment, batch 103)

e('PayeeReportFragment.onLoadFinished', 'PayeeReportAdapter.newView', 'FRAMEWORK',
  'the payee report cursor has rows: changeCursor hands the cursor to the list, which lays out a row, and CursorAdapter.getView calls newView when no row view can be reused',
  needs_state=state_text('the payee report query returns at least one row (the list lays out a row only then)', ('data',)),
  evidence='SRC reports/PayeeReportFragment.java:129-130 (super.onLoadFinished); SRC reports/BaseReportFragment.java:142-144 (changeCursor at 144; batch 103); FW-SRC core/java/android/widget/CursorAdapter.java:284-285 (newView when convertView is null), 348-353 (changeCursor), 365-381 (swap and notifyDataSetChanged)')

e('PayeeReportFragment.onLoadFinished', 'PayeeReportAdapter.bindView', 'FRAMEWORK',
  'the same route as newView: CursorAdapter.getView calls bindView for each row it lays out',
  needs_state=state_text('the payee report query returns at least one row (the list lays out a row only then)', ('data',)),
  evidence='SRC reports/PayeeReportFragment.java:129-130; SRC reports/BaseReportFragment.java:142-144; FW-SRC core/java/android/widget/CursorAdapter.java:289 (bindView), 348-353, 365-381; INFERRED ListView draw path (AbsListView.getView not read for this batch)')

# ---- 7. the list and the menu (GUI edges from the report page S_INCOME_VS_EXPENSES, written by batch 104)

gui('S_INCOME_VS_EXPENSES', 'IncomeVsExpensesListFragment.onOptionsItemSelected',
  'Tap a menu item: the Up button (android.R.id.home), sort ascending or descending, the chart (menu_chart; the item is hidden in the dual-panel layout), or the period choice (menu_period)',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:234-245 (ids tested at 235, 237, 241, 243); SRC res/menu/menu_report_income_vs_expenses.xml:21 (menu_chart), 26 (menu_sort), 33 (menu_sort_asceding), 37 (menu_sort_desceding), 43 (menu_period); SRC reports/IncomeVsExpensesListFragment.java:228 (chart item hidden when mIsDualPanel)')

gui('S_INCOME_VS_EXPENSES', 'IncomeVsExpensesListFragment$4.onItemClick',
  'Tap a row of the list: a month opens the search for that month, and the year total row opens the whole year; the footer row is ignored',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:363-368 (listener set at 363; a footer row returns at 368), 369-389 (date range), 391-392 (getSearchIntent and startActivity)')

# ---- part 106 (2026-10-29)
# ================================================================== batch 106 (label_106): PayeeReportFragment (+ $1), PayeesReportActivity, PieChartFragment (+ $1)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_106.md. Class-file and grep evidence: graphs/MMEX/parts/label_106.grep.txt.
# Edges below have a batch 106 method (or S_PAYEE_REPORT) as destination (D1). Sources outside this batch are interim until those batches merge:
# MainActivity.onDrawerMenuAndOptionMenuSelected (another batch), BaseReportFragment.onCreate, BaseReportFragment.onActivityCreated, BaseReportFragment.onCreateLoader (batch 103).
# CALL edges already in auto_calls.json are not written here (D7).
# All 32 methods are REACHABLE, so there are no UNREACHABLE entries and no sup pairs.

SCREENS.update({
    'S_PAYEE_REPORT': 'Payee report (PayeesReportActivity hosts PayeeReportFragment): total per payee for the selected period with a footer total; the options menu chooses the period, custom dates or the chart (single panel); a tap on a payee row opens the search results for that payee; the pie chart of the same totals is shown beside the list (dual panel) or in place of it (single panel)',
})

ENV_DUAL_PANEL = env_text(
    'tablet layout with the fragmentChart view (the sw600dp landscape or sw720dp portrait layout): PayeesReportActivity.java:44 sets mIsDualPanel only when fragmentChart exists (res layout-sw600dp-land line 38, layout-sw720dp-port line 40; the default layout has no fragmentChart)',
    ('hardware',))

STATE_TWO_SLICES = state_text(
    'the chart arguments hold at least two payee totals: Collections.sort (PieChartFragment.java:77) calls compare only for a list of two or more entries',
    ('data',))

# ---- activity: started by the app only (AndroidManifest.xml:289-291 has no intent-filter)

e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'PayeesReportActivity.<init>', 'INTENT',
  'case R.id.menu_report_payees: startActivity(new Intent(this, PayeesReportActivity.class)) (the Payee report item of the drawer or the options menu)',
  gui=['Open the navigation drawer or the options menu and tap Payee report'],
  evidence='SRC home/MainActivity.java:589 (method), 667-669 (case label and startActivity); SRC AndroidManifest.xml:289-291 (no intent-filter); SRC res/menu/menu_main.xml:106-108; FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (newActivity constructs the class)')

e('PayeesReportActivity.<init>', 'PayeesReportActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='SRC PayeesReportActivity.java:32-34; FW-SRC core/java/android/app/Instrumentation.java:1212-1215; FW-SRC core/java/android/app/ActivityThread.java:2729-2731')

e('PayeesReportActivity.onCreate', 'S_PAYEE_REPORT', 'ENTERS',
  'the report is shown: onCreate sets report_chart_fragments_activity as the layout (line 34), sets mIsDualPanel from the fragmentChart view (line 44) and adds PayeeReportFragment to fragmentMain (lines 46-50)',
  evidence='SRC PayeesReportActivity.java:32-52 (setContentView 34; mIsDualPanel 44; fragment 46; add and commit 50)')

# ---- PayeeReportFragment: lifecycle and framework dispatch from the base class (batch 103 sources)

e('BaseReportFragment.onCreate', 'PayeeReportFragment.onActivityCreated', 'LIFECYCLE',
  'the fragment manager calls onActivityCreated after onCreate (the fragment is committed in PayeesReportActivity.onCreate, line 50); the override calls super at line 95',
  evidence='SRC PayeeReportFragment.java:63-96; SRC reports/BaseReportFragment.java:67-72 (onCreate, batch 103); SRC PayeesReportActivity.java:46-50; INFERRED androidx Fragment lifecycle (library not read)')

e('BaseReportFragment.onActivityCreated', 'PayeeReportFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'setHasOptionsMenu(true) (BaseReportFragment.java:79) makes the framework build the options menu: it calls onCreateOptionsMenu on the fragment (PayeeReportFragment.java:195)',
  evidence='SRC reports/BaseReportFragment.java:75-79, 101-111; SRC reports/PayeeReportFragment.java:195-205; INFERRED androidx FragmentManager dispatches onCreateOptionsMenu (library not read); precedent label_103.py')

e('BaseReportFragment.onCreateLoader', 'PayeeReportFragment.onLoadFinished', 'FRAMEWORK',
  'the loader created by startLoader (restartLoader, BaseReportFragment.java:262) delivers its cursor and the LoaderManager calls onLoadFinished on this fragment (the override calls super at line 130)',
  evidence='SRC reports/BaseReportFragment.java:115-132, 261-263; SRC reports/PayeeReportFragment.java:129-130; INFERRED androidx LoaderManager delivers the result to LoaderCallbacks (library not read); precedent label_103.py (CategoriesReportFragment.onLoadFinished)')

e('PayeeReportFragment.onLoadFinished', 'PayeeReportFragment$1.run', 'FRAMEWORK',
  'in dual-panel mode onLoadFinished posts the Runnable with Handler.postDelayed (1000 ms); the Handler runs it through handleCallback and Runnable.run calls showChart',
  env=ENV_DUAL_PANEL,
  evidence='SRC reports/PayeeReportFragment.java:129-165 (data null check 132; guard 154; Handler 155-162); SRC reports/PayeesReportActivity.java:44; SRC res/layout-sw600dp-land/report_chart_fragments_activity.xml:38; SRC res/layout-sw720dp-port/report_chart_fragments_activity.xml:40; FW-SRC core/java/android/os/Handler.java:427-430 (postDelayed), 789-791 (handleCallback)')

# ---- user actions on the payee report page (GUI; page -> method, D6)

gui('S_PAYEE_REPORT', 'PayeeReportFragment.onQueryTextChange',
    'Type in the search box of the payee report (the list is filtered by the text)',
    evidence='SRC common/BaseListFragment.java:112-131 (SearchView listener; onPreQueryTextChange at 128), 221-231; SRC reports/PayeeReportFragment.java:99-126; INFERRED androidx SearchView calls the listener on each text change (not in fw_src)')

gui('S_PAYEE_REPORT', 'PayeeReportFragment.onListItemClick',
    'Tap a payee row in the report list (the search results for that payee open)',
    evidence='SRC reports/PayeeReportFragment.java:279-294 (showSearchActivityFor at 293); SRC core/AbsListFragment.java:42-46 (OnItemClickListener calls onListItemClick at 44); INFERRED the list view dispatches the item click to the listener (AdapterView not printed)')

gui('S_PAYEE_REPORT', 'PayeeReportFragment.onOptionsItemSelected',
    'Options menu: tap Show chart (single panel only, the item is hidden in dual panel) or one of the period items (passed to super, BaseReportFragment)',
    evidence='SRC reports/PayeeReportFragment.java:201 (itemChart visible only when not dual panel), 208-214 (menu_chart at 209-211; super at 213); SRC res/menu/menu_report.xml:21-25; INFERRED androidx dispatches the menu item to the fragment (library not read)')

# ---- PieChartFragment: lifecycle chain from the fragment transaction in PayeeReportFragment.showChart

e('PieChartFragment.<init>', 'PieChartFragment.onCreate', 'LIFECYCLE',
  'the fragment manager calls onCreate after the chart transaction is committed (showChart creates the fragment at PayeeReportFragment.java:250, replaces fragmentChart at 259 or fragmentMain at 261, and commits at 265)',
  evidence='SRC reports/PayeeReportFragment.java:248-266; SRC reports/PieChartFragment.java:125-127; INFERRED androidx Fragment lifecycle (library not read); precedent label_104.py (IncomeVsExpensesChartFragment)')

e('PieChartFragment.onCreate', 'PieChartFragment.onCreateView', 'LIFECYCLE',
  'the fragment manager calls onCreateView after onCreate',
  evidence='SRC reports/PieChartFragment.java:125-145; INFERRED androidx Fragment lifecycle (library not read)')

e('PieChartFragment.onCreateView', 'PieChartFragment.onResume', 'LIFECYCLE',
  'the fragment manager resumes the fragment after its view is created; the second route is the explicit call in showChart at PayeeReportFragment.java:255 (auto CALL record, no edge written, D7)',
  evidence='SRC reports/PieChartFragment.java:145-184; SRC reports/PayeeReportFragment.java:255; INFERRED androidx Fragment lifecycle (library not read)')

e('PieChartFragment.onResume', 'PieChartFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state when the activity leaves the foreground, after the fragment has been resumed (same pattern as label_104.py)',
  evidence='SRC reports/PieChartFragment.java:181-200; INFERRED androidx Fragment lifecycle (library not read); precedent label_104.py (IncomeVsExpensesChartFragment.onResume to onSaveInstanceState)')

# ---- PieChartFragment$1: comparator used by Collections.sort (libcore, INFERRED)

e('PieChartFragment.buildChart', 'PieChartFragment$1.compare', 'FRAMEWORK',
  'buildChart sorts the slices with an anonymous Comparator (line 77); Collections.sort calls compare for the pairs it compares, which needs at least two slices',
  needs_state=STATE_TWO_SLICES,
  evidence='SRC reports/PieChartFragment.java:74-82 (sort at 77; compare body 81); FW-SRC: Collections.java not in fw_src (grep H5); INFERRED Collections.sort calls the comparator (libcore not read)')

# ---- user actions on the chart (GUI; the chart is shown inside the same screen, D9)

gui('S_PAYEE_REPORT', 'PieChartFragment.onValueSelected',
    'Tap a slice of the pie chart (the slice value is shown in a toast)',
    evidence='SRC reports/PieChartFragment.java:170 (setOnChartValueSelectedListener(this)), 231-243; INFERRED MPAndroidChart library (not in the dataset) calls OnChartValueSelectedListener.onValueSelected on a tap on a slice')

gui('S_PAYEE_REPORT', 'PieChartFragment.onNothingSelected',
    'Tap the chart where no slice is highlighted',
    evidence='SRC reports/PieChartFragment.java:170, 246-248 (empty body); INFERRED MPAndroidChart library (not in the dataset) calls onNothingSelected')

gui('S_PAYEE_REPORT', 'PieChartFragment.onOptionsItemSelected',
    'Tap the Up arrow in the toolbar while the chart is shown (the activity does not handle Up, so the item reaches the fragments)',
    evidence='SRC reports/PieChartFragment.java:141 (setHasOptionsMenu), 187-193 (getActivity().onBackPressed() at 189); SRC common/MmxBaseFragmentActivity.java:55, 107-130 (home branch returns only when mDisplayHomeAsUpEnabled is true, and PayeesReportActivity never sets it); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450), 3597; INFERRED androidx fragment dispatch (library not read); precedent label_104.py (IncomeVsExpensesChartFragment.onOptionsItemSelected)')

# ---- part 107 (2026-10-29)
# batch 107 (label_107): ValuePieEntry (15 methods), CategorySub (8), ParameterizedWhereClause (1), SearchActivity (11).
# Result: 29 REACHABLE, 6 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_107.md).
# Grep evidence: graphs/MMEX/parts/label_107.grep.txt.
# Edges written here: 14 e() and 1 gui(). Every destination is a batch 107 method or S_SEARCH (D1). Auto CALL edges are not written (D7).
# Framework hops are INFERRED where the support-library code (FragmentState save and restore, AppCompat menu delegate) was not read.
# sup pairs: 2 (D14), for the auto CALLs out of ValuePieEntry.<init>(String,double), which is UNREACHABLE.

SCREENS.update({
    'S_SEARCH': 'Search page (SearchActivity): a search-parameters form in a fragment, with a search icon in the action bar; the results list is a separate page (AllDataListFragment)',
})

# ---- SearchActivity: entry by explicit intent (the manifest entry at AndroidManifest.xml:296-297 has no intent-filter)
e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'SearchActivity.<init>', 'INTENT',
  'the drawer menu opens the search page: startActivity(new Intent(MainActivity.this, SearchActivity.class))',
  evidence='SRC home/MainActivity.java:659 (enclosing method at 589)')

e('HomeFragment.onOptionsItemSelected', 'SearchActivity.<init>', 'INTENT',
  'the home options menu opens the search page: startActivity(new Intent(getActivity(), SearchActivity.class))',
  evidence='SRC home/HomeFragment.java:364-365 (enclosing method at 361)')

e('PayeeListFragment.onContextItemSelected', 'SearchActivity.<init>', 'INTENT',
  'the payee list context menu opens the search page with search parameters: IntentFactory.getSearchIntent, then startActivity',
  evidence='SRC fragment/PayeeListFragment.java:237-238 (enclosing method at 191); core/IntentFactory.java:54-60')

e('IncomeVsExpensesListFragment$4.onItemClick', 'SearchActivity.<init>', 'INTENT',
  'tapping a row of the income vs expenses report opens the search page with search parameters: IntentFactory.getSearchIntent, then startActivity',
  evidence='SRC reports/IncomeVsExpensesListFragment.java:391-392 (enclosing method at 365); core/IntentFactory.java:54-60')

e('SearchActivity.<init>', 'SearchActivity.onCreate', 'LIFECYCLE',
  'the framework creates the activity and calls onCreate',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate at 2729, 2731); FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate)')

e('SearchActivity.onCreate', 'SearchActivity.onResume', 'LIFECYCLE',
  'the framework calls onResume after onCreate',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3534-3556 (performResumeActivity calls performResume at 3556); FW-SRC core/java/android/app/Activity.java:7098-7107 (performResume calls callActivityOnResume at 7107); SRC search/SearchActivity.java:72-81')

e('SearchActivity.onCreate', 'S_SEARCH', 'ENTERS',
  'the search page is shown: onCreate sets the content view, gets or creates the search-parameters fragment (added to R.id.fragmentMain), and runs handleSearchRequest',
  evidence='SRC search/SearchActivity.java:55-70, 124-133')

e('SearchActivity.onCreate', 'SearchActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'after onCreate the action bar needs the options menu: the window calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  via='PhoneWindow builds the panel menu through the window callback; the AppCompat delegate between the window and the activity is not read (INFERRED)',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:631 (cb.onCreatePanelMenu); FW-SRC core/java/android/app/Activity.java:3386-3388; SRC search/SearchActivity.java:91-104')

# ---- SearchActivity: the category picker returns its result to the activity
e('CategoryListFragment.setResult', 'SearchActivity.onActivityResult', 'RESULT',
  'the category picker returns RESULT_OK with the chosen category; the framework delivers the result to the activity that started it (SearchParametersFragment starts the picker), and the override calls super so the fragment can read the result',
  via='INFERRED: the picker request is made from a fragment and the framework passes who == null to Activity.onActivityResult (Activity.java:7265-7266); the FragmentActivity dispatch to SearchParametersFragment is not read',
  evidence='SRC common/CategoryListFragment.java:313, 354; SRC search/SearchParametersFragment.java:204, 233-234; FW-SRC core/java/android/app/ActivityThread.java:4253-4266 (deliverResults); FW-SRC core/java/android/app/Activity.java:7259-7266 (dispatchActivityResult)')

# ---- category sent to the search page: the parcel write and read
e('CategoryListFragment.showSearchActivityFor', 'CategorySub.writeToParcel', 'FRAMEWORK',
  'the search intent carries the category: Parcels.wrap puts the SearchParameters wrapper in the intent extra; startActivity marshals the intent, Parcel.writeValue writes the wrapper as a Parcelable, the wrapper writes the category through Parcel.writeParcelable, which calls writeToParcel',
  via='the generated wrapper body is not in the source root and was not read; its write method is known only from auto_calls.json framework_calls (INFERRED)',
  evidence='SRC common/CategoryListFragment.java:733-739; FW-SRC core/java/android/os/Parcel.java:1673-1692 (writeValue, Parcelable branch), 1785-1791 (writeParcelable calls writeToParcel); auto_calls.json (framework_calls of SearchParameters$$Parcelable.write include Parcel.writeParcelable)')

e('CategoriesReportFragment.showSearchActivityFor', 'CategorySub.writeToParcel', 'FRAMEWORK',
  'the report search intent carries the category: Parcels.wrap puts the SearchParameters wrapper in the intent extra; startActivity marshals the intent, and the wrapper writes the category through Parcel.writeParcelable, which calls writeToParcel',
  via='the generated wrapper body is not read (INFERRED), as for the CategoryListFragment edge',
  evidence='SRC reports/CategoriesReportFragment.java:379-385 (called from onListItemClick at 293); FW-SRC core/java/android/os/Parcel.java:1673-1692, 1785-1791; auto_calls.json (framework_calls of SearchParameters$$Parcelable.write include Parcel.writeParcelable)')

e('SearchActivity.handleSearchRequest', 'CategorySub$1.createFromParcel', 'FRAMEWORK',
  'getParcelableExtra unparcels the SearchParameters wrapper from the intent; the wrapper reads the category through Parcel.readParcelable, which calls the CATEGORY CREATOR createFromParcel',
  via='the generated wrapper body is not read (INFERRED); its read method is known only from auto_calls.json framework_calls',
  evidence='SRC search/SearchActivity.java:156-157; SRC search/CategorySub.java:44-47; FW-SRC core/java/android/os/Parcel.java:2841-2851 (readParcelable calls createFromParcel); auto_calls.json (framework_calls of SearchParameters$$Parcelable.read include Parcel.readParcelable)')

# ---- ValuePieEntry: the chart values travel in the fragment arguments
e('PieChartFragment.setChartArguments', 'ValuePieEntry.writeToParcel', 'FRAMEWORK',
  'the framework parcels the fragment arguments that hold the chart values: Parcel.writeValue writes the ArrayList as VAL_LIST and each entry as VAL_PARCELABLE, which calls writeToParcel',
  via='the support-library FragmentState save path that parcels the arguments is not read (INFERRED); the list is stored with putSerializable, and writeValue reaches the List branch (Parcel.java:1717-1718) before any Serializable fallback, which is not read (INFERRED)',
  evidence='SRC reports/PieChartFragment.java:212-214; SRC reports/CategoriesReportFragment.java:331, 340; SRC reports/PayeeReportFragment.java:243, 252; FW-SRC core/java/android/os/Parcel.java:1673-1692, 1717-1718 (VAL_PARCELABLE before VAL_LIST), 917-927 (writeList calls writeValue); label_107.grep.txt sections 10-11')

e('PieChartFragment.buildChart', 'ValuePieEntry$1.createFromParcel', 'FRAMEWORK',
  'buildChart reads the chart values with getSerializable; the arguments Bundle was restored from a parcel, so unparcel runs first, readValue reads VAL_LIST and each VAL_PARCELABLE entry, and readParcelable calls the CREATOR createFromParcel',
  via='the restore that supplies the parcelled Bundle is not read (INFERRED)',
  evidence='SRC reports/PieChartFragment.java:74-75, 181-183; FW-SRC core/java/android/os/BaseBundle.java:1189-1192 (getSerializable unparcels); FW-SRC core/java/android/os/Bundle.java:1032-1034; FW-SRC core/java/android/os/Parcel.java:2744-2745, 2765-2766, 2369-2377, 3172-3180, 2841-2851')

# ---- SearchActivity: the search icon runs the search (GUI from the page)
gui('S_SEARCH', 'SearchActivity.onOptionsItemSelected', 'Tap the search icon in the action bar (searchMenuItem) to run the search',
    evidence='SRC search/SearchActivity.java:97-101 (menu_search inflated and searchMenuItem set), 107-120 (searchMenuItem at 113, performSearch at 114)')

# ================================================================== UNREACHABLE entries
UNREACHABLE['ValuePieEntry.<init>(String,double)'] = ('no_trigger_in_app',
  'No caller. The app builds the pie entries with the no-argument constructor (CategoriesReportFragment.java:310, PayeeReportFragment.java:225) and sets fields with setters; the parcel path uses the three-argument constructor (ValuePieEntry.java:104). auto_calls.json has no CALL record whose dst is this constructor. Its outgoing auto CALLs (setText at line 31, setValue at line 32) are suppressed by the sup pairs below (D14).',
  'reports/ValuePieEntry.java:30-33; reports/CategoriesReportFragment.java:310; reports/PayeeReportFragment.java:225; reports/ValuePieEntry.java:104; label_107.grep.txt sections 1-2',
  'SOURCE')

UNREACHABLE['ValuePieEntry.describeContents'] = ('framework_never_calls',
  'Returns 0. No app code calls it (label_107.grep.txt section 3). The framework calls describeContents only from the Bundle.hasFileDescriptors walk (Bundle.java:329-362, which calls describeContents on each Parcelable value) and from Bundle.describeContents (Bundle.java:1215-1218), which Intent.describeContents reaches through mExtras (Intent.java:9553). The chart values are fragment arguments, not an intent extra, and the restore path that might walk that Bundle was not read. INFERRED.',
  'reports/ValuePieEntry.java:84-86; label_107.grep.txt sections 3-6; FW-SRC core/java/android/os/Bundle.java:316-336, 1215-1218; FW-SRC core/java/android/content/Intent.java:9553',
  'INFERRED')

UNREACHABLE['ValuePieEntry$1.newArray'] = ('framework_never_calls',
  'CREATOR typed-array method. The framework calls it only from Parcel.createTypedArray (Parcel.java:2640-2645), which no app code calls (label_107.grep.txt section 8). The list path that the entries actually use (readArrayList, readListInternal) does not call newArray (Parcel.java:2369-2377, 3172-3180). INFERRED.',
  'reports/ValuePieEntry.java:97-100; label_107.grep.txt sections 8, 13; FW-SRC core/java/android/os/Parcel.java:2640-2645',
  'INFERRED')

UNREACHABLE['CategorySub.describeContents'] = ('framework_never_calls',
  'Returns 0. No app code calls it (label_107.grep.txt section 3). The Bundle.hasFileDescriptors walk sees the top-level intent-extra value, which is the generated SearchParameters$$Parcelable wrapper, and does not reach the nested CategorySub. Parcel.writeParcelable does not call describeContents (Parcel.java:1785-1791). The wrapper body is generated and not read, so its describeContents is INFERRED.',
  'search/CategorySub.java:57-59; label_107.grep.txt sections 3-7; FW-SRC core/java/android/os/Parcel.java:1785-1791; auto_calls.json (framework_calls of SearchParameters$$Parcelable.write)',
  'INFERRED')

UNREACHABLE['CategorySub$1.newArray'] = ('framework_never_calls',
  'CREATOR typed-array method. Only Parcel.createTypedArray calls it, and no app code builds or reads a typed array of CategorySub (label_107.grep.txt section 8). The category is wrapped by the generated SearchParameters wrapper, whose body is not read; whether that wrapper calls createTypedArray is INFERRED.',
  'search/CategorySub.java:51-53; label_107.grep.txt section 8; FW-SRC core/java/android/os/Parcel.java:2640-2645',
  'INFERRED')

UNREACHABLE['ParameterizedWhereClause.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor of a holder class with two list fields (Clause, Params). The only mention in the app source is the class declaration (label_107.grep.txt section 9). auto_calls.json has no CALL record whose dst is this constructor; its implementation record is <init> ()V with no caller. Nothing in the app creates a ParameterizedWhereClause, so no edge reaches it.',
  'search/ParameterizedWhereClause.java:24-27; label_107.grep.txt section 9; auto_calls.json (impl entry for ParameterizedWhereClause.<init>)',
  'SOURCE')

# ================================================================== sup pairs (D14)
sup(('ValuePieEntry.<init>(String,double)', 'ValuePieEntry.setText'),  # auto CALL at ValuePieEntry.java:31 from an unreachable constructor
    ('ValuePieEntry.<init>(String,double)', 'ValuePieEntry.setValue'))  # auto CALL at ValuePieEntry.java:32 from an unreachable constructor

# ---- part 108 (2026-10-29)
# ================================================================== batch 108 (label_108): SearchParameters.<init>, and its parceler wrapper SearchParameters$$Parcelable (with its $1 creator): 11 methods
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_108.md.
# Grep evidence for the UNREACHABLE claims and for the edge sites: graphs/MMEX/parts/label_108.grep.txt (blocks B1-B10).
# The wrapper classes are generated by parceler and are not in the source root (INFERRED). Parcels.wrap and Parcels.unwrap are parceler library reflection (INFERRED; library source not read).
# CALL edges already in auto_calls.json are not written here (D7). Those are the SearchParameters.<init> callers (CategoryListFragment, PayeeListFragment, IncomeVsExpensesListFragment, CategoriesReportFragment, PayeeReportFragment, SearchParametersFragment) and the wrapper's internal calls (createFromParcel -> <clinit>, <init>, read; <clinit> -> $1.<init>; writeToParcel -> write; read -> SearchParameters.<init>).
# No sup pairs: the two UNREACHABLE methods (describeContents, newArray) have no outgoing auto_calls records (grep B10).

# ---- Parcels.wrap sites: parceler looks the wrapper up by name (its static initialiser runs: <clinit>) and constructs it (<init>)

e('CategoryListFragment.showSearchActivityFor', 'SearchParameters$$Parcelable.<clinit>', 'CALL',
  'Parcels.wrap loads the generated wrapper class by name, which runs its static initialiser (it creates the CREATOR field)',
  cls='non_standard', via='Parcels.wrap(parameters) at CategoryListFragment.java:735 (parceler library reflection: class load by name; library source not read, INFERRED)',
  evidence='SRC common/CategoryListFragment.java:733-738; grep B8; INFERRED parceler library source not read')

e('CategoryListFragment.showSearchActivityFor', 'SearchParameters$$Parcelable.<init>', 'CALL',
  'Parcels.wrap constructs the wrapper around the SearchParameters created at CategoryListFragment.java:221',
  cls='non_standard', via='Parcels.wrap(parameters) at CategoryListFragment.java:735 (parceler library reflection: constructor call; library source not read, INFERRED)',
  evidence='SRC common/CategoryListFragment.java:221, 733-738; grep B8; INFERRED parceler library source not read')

e('IntentFactory.getSearchIntent', 'SearchParameters$$Parcelable.<clinit>', 'CALL',
  'Parcels.wrap loads the generated wrapper class by name (static initialiser runs)',
  cls='non_standard', via='Parcels.wrap(parameters) at IntentFactory.java:56 (parceler library reflection; library source not read, INFERRED)',
  evidence='SRC core/IntentFactory.java:54-56; grep B8; INFERRED parceler library source not read')

e('IntentFactory.getSearchIntent', 'SearchParameters$$Parcelable.<init>', 'CALL',
  'Parcels.wrap constructs the wrapper around the parameters passed in by the callers (PayeeListFragment.java:237, IncomeVsExpensesListFragment.java:391)',
  cls='non_standard', via='Parcels.wrap(parameters) at IntentFactory.java:56 (parceler library reflection; library source not read, INFERRED)',
  evidence='SRC core/IntentFactory.java:54-56; SRC fragment/PayeeListFragment.java:237; SRC reports/IncomeVsExpensesListFragment.java:391; grep B8, B9; INFERRED parceler library source not read')

e('CategoriesReportFragment.showSearchActivityFor', 'SearchParameters$$Parcelable.<clinit>', 'CALL',
  'Parcels.wrap loads the generated wrapper class by name (static initialiser runs)',
  cls='non_standard', via='Parcels.wrap(parameters) at CategoriesReportFragment.java:381 (parceler library reflection; library source not read, INFERRED)',
  evidence='SRC reports/CategoriesReportFragment.java:379-383; grep B8; INFERRED parceler library source not read')

e('CategoriesReportFragment.showSearchActivityFor', 'SearchParameters$$Parcelable.<init>', 'CALL',
  'Parcels.wrap constructs the wrapper around the SearchParameters built at CategoriesReportFragment.java:288',
  cls='non_standard', via='Parcels.wrap(parameters) at CategoriesReportFragment.java:381 (parceler library reflection; library source not read, INFERRED)',
  evidence='SRC reports/CategoriesReportFragment.java:288, 379-383; grep B8, B9; INFERRED parceler library source not read')

e('PayeeReportFragment.showSearchActivityFor', 'SearchParameters$$Parcelable.<clinit>', 'CALL',
  'Parcels.wrap loads the generated wrapper class by name (static initialiser runs)',
  cls='non_standard', via='Parcels.wrap(parameters) at PayeeReportFragment.java:319 (parceler library reflection; library source not read, INFERRED)',
  evidence='SRC reports/PayeeReportFragment.java:317-321; grep B8; INFERRED parceler library source not read')

e('PayeeReportFragment.showSearchActivityFor', 'SearchParameters$$Parcelable.<init>', 'CALL',
  'Parcels.wrap constructs the wrapper around the SearchParameters built at PayeeReportFragment.java:287',
  cls='non_standard', via='Parcels.wrap(parameters) at PayeeReportFragment.java:319 (parceler library reflection; library source not read, INFERRED)',
  evidence='SRC reports/PayeeReportFragment.java:287, 317-321; grep B8, B9; INFERRED parceler library source not read')

e('SearchParametersFragment.onSaveInstanceState', 'SearchParameters$$Parcelable.<clinit>', 'CALL',
  'Parcels.wrap loads the generated wrapper class by name (static initialiser runs) before the wrapper is put into the saved-state bundle',
  cls='non_standard', via='Parcels.wrap(searchParameters) at SearchParametersFragment.java:286 (parceler library reflection; library source not read, INFERRED)',
  evidence='SRC search/SearchParametersFragment.java:276-287; grep B8; INFERRED parceler library source not read')

e('SearchParametersFragment.onSaveInstanceState', 'SearchParameters$$Parcelable.<init>', 'CALL',
  'Parcels.wrap constructs the wrapper around the parameters returned by getSearchParameters (line 285)',
  cls='non_standard', via='Parcels.wrap(searchParameters) at SearchParametersFragment.java:286 (parceler library reflection; library source not read, INFERRED)',
  evidence='SRC search/SearchParametersFragment.java:276-287; grep B8; INFERRED parceler library source not read')

e('SearchParametersFragment.setSearchParameters', 'SearchParameters$$Parcelable.<clinit>', 'CALL',
  'Parcels.wrap loads the generated wrapper class by name (static initialiser runs) before it is put into the fragment arguments',
  cls='non_standard', via='Parcels.wrap(parameters) at SearchParametersFragment.java:340 (parceler library reflection; library source not read, INFERRED)',
  evidence='SRC search/SearchParametersFragment.java:337-341; grep B8; INFERRED parceler library source not read')

e('SearchParametersFragment.setSearchParameters', 'SearchParameters$$Parcelable.<init>', 'CALL',
  'Parcels.wrap constructs the wrapper around the parameters passed to setSearchParameters (callers: onCreate line 128, onOptionsItemSelected line 305, getWhereStatement line 330 and others)',
  cls='non_standard', via='Parcels.wrap(parameters) at SearchParametersFragment.java:340 (parceler library reflection; library source not read, INFERRED)',
  evidence='SRC search/SearchParametersFragment.java:337-341; grep B8; INFERRED parceler library source not read')

# ---- Parcels.unwrap sites: parceler calls getParcel on the wrapper and returns the SearchParameters

e('SearchActivity.handleSearchRequest', 'SearchParameters$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the wrapper taken from the intent extra (line 156) and returns the SearchParameters',
  cls='non_standard', via='Parcels.unwrap(searchParcel) at SearchActivity.java:157 (parceler library calls getParcel; library source not read, INFERRED)',
  evidence='SRC search/SearchActivity.java:151-157; grep B8; INFERRED parceler library source not read')

e('SearchParametersFragment.getSearchParameters', 'SearchParameters$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the wrapper taken from the fragment arguments (line 320) and returns the SearchParameters',
  cls='non_standard', via='Parcels.unwrap(searchParcel) at SearchParametersFragment.java:323 (parceler library calls getParcel; library source not read, INFERRED)',
  evidence='SRC search/SearchParametersFragment.java:316-324; grep B8; INFERRED parceler library source not read')

# ---- framework write path: the wrapper is inside a Bundle or Intent that the framework parcels; Parcel.writeValue -> writeParcelable calls the wrapper's writeToParcel

e('CategoryListFragment.showSearchActivityFor', 'SearchParameters$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the intent extra holds the wrapper; startActivity sends the intent and the framework parcels it: Intent.writeToParcel -> Parcel.writeBundle -> Bundle.writeToParcel -> writeArrayMapInternal -> writeValue -> writeParcelable, which calls the wrapper writeToParcel',
  cls='non_standard', via='intent.putExtra(..., Parcels.wrap(parameters)) at CategoryListFragment.java:735, then startActivity(intent) at 737; the IPC marshalling of the intent inside startActivity is INFERRED (not in fw_src); FW-SRC chain: Intent.java:9556, 9595; Parcel.java:872-878, 820, 838, 1697, 1785-1791; Bundle.java:1229-1232; BaseBundle.java:1507, 1542',
  evidence='SRC common/CategoryListFragment.java:733-737; FW-SRC core/java/android/content/Intent.java:9556, 9595; FW-SRC core/java/android/os/Parcel.java:872-878, 820-838, 1697, 1785-1791; FW-SRC core/java/android/os/Bundle.java:1229-1232; FW-SRC core/java/android/os/BaseBundle.java:1507, 1542; grep B7; INFERRED Binder/IPC marshalling of startActivity (not in fw_src)')

e('IntentFactory.getSearchIntent', 'SearchParameters$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the returned intent holds the wrapper; the callers start it, and the framework parcels it as in CategoryListFragment.showSearchActivityFor',
  cls='non_standard', via='intent.putExtra(..., Parcels.wrap(parameters)) at IntentFactory.java:56; startActivity(intent) at PayeeListFragment.java:238 and at IncomeVsExpensesListFragment.java:392 (after the getSearchIntent call at 391); IPC marshalling INFERRED; FW-SRC chain as in the CategoryListFragment edge',
  evidence='SRC core/IntentFactory.java:54-58; SRC fragment/PayeeListFragment.java:237-238; SRC reports/IncomeVsExpensesListFragment.java:391-392; FW-SRC core/java/android/content/Intent.java:9556, 9595; FW-SRC core/java/android/os/Parcel.java:872-878, 820-838, 1697, 1785-1791; FW-SRC core/java/android/os/Bundle.java:1229-1232; grep B7, B9; INFERRED Binder/IPC marshalling (not in fw_src)')

e('CategoriesReportFragment.showSearchActivityFor', 'SearchParameters$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the intent extra holds the wrapper; startActivity sends the intent and the framework parcels it (same chain as CategoryListFragment.showSearchActivityFor)',
  cls='non_standard', via='intent.putExtra(..., Parcels.wrap(parameters)) at CategoriesReportFragment.java:381, then startActivity(intent) at 383; IPC marshalling INFERRED; FW-SRC chain as in the CategoryListFragment edge',
  evidence='SRC reports/CategoriesReportFragment.java:379-383; FW-SRC core/java/android/content/Intent.java:9556, 9595; FW-SRC core/java/android/os/Parcel.java:872-878, 820-838, 1697, 1785-1791; FW-SRC core/java/android/os/Bundle.java:1229-1232; grep B7; INFERRED Binder/IPC marshalling (not in fw_src)')

e('PayeeReportFragment.showSearchActivityFor', 'SearchParameters$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the intent extra holds the wrapper; startActivity sends the intent and the framework parcels it (same chain as CategoryListFragment.showSearchActivityFor)',
  cls='non_standard', via='intent.putExtra(..., Parcels.wrap(parameters)) at PayeeReportFragment.java:319, then startActivity(intent) at 321; IPC marshalling INFERRED; FW-SRC chain as in the CategoryListFragment edge',
  evidence='SRC reports/PayeeReportFragment.java:317-321; FW-SRC core/java/android/content/Intent.java:9556, 9595; FW-SRC core/java/android/os/Parcel.java:872-878, 820-838, 1697, 1785-1791; FW-SRC core/java/android/os/Bundle.java:1229-1232; grep B7; INFERRED Binder/IPC marshalling (not in fw_src)')

e('SearchParametersFragment.onSaveInstanceState', 'SearchParameters$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the wrapper is put into the saved-state bundle (outState); when the framework saves state it parcels the bundle, and writeParcelable calls the wrapper writeToParcel',
  cls='non_standard', via='savedInstanceState.putParcelable(KEY_SEARCH_CRITERIA, Parcels.wrap(searchParameters)) at SearchParametersFragment.java:286; the framework parcelling the saved state is INFERRED (state-save path not read); FW-SRC: Bundle.java:1229-1232, Parcel.java:872-878, 1697, 1785-1791',
  evidence='SRC search/SearchParametersFragment.java:276-287; FW-SRC core/java/android/os/Bundle.java:1229-1232; FW-SRC core/java/android/os/Parcel.java:872-878, 1697, 1785-1791; INFERRED framework saves the outState bundle (not read)')

e('SearchParametersFragment.setSearchParameters', 'SearchParameters$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the wrapper is stored in the fragment arguments; when the framework saves fragment state it parcels the arguments bundle, and writeParcelable calls the wrapper writeToParcel',
  cls='non_standard', via='getArguments().putParcelable(KEY_SEARCH_CRITERIA, Parcels.wrap(parameters)) at SearchParametersFragment.java:340; the framework parcelling the fragment arguments is INFERRED (fragment state save not read); FW-SRC: Bundle.java:1229-1232, Parcel.java:872-878, 1697, 1785-1791',
  evidence='SRC search/SearchParametersFragment.java:337-341; FW-SRC core/java/android/os/Bundle.java:1229-1232; FW-SRC core/java/android/os/Parcel.java:872-878, 1697, 1785-1791; INFERRED framework saves the fragment arguments (not read)')

# ---- framework read path: Intent or Bundle getParcelable -> unparcel -> Parcel.readValue -> readParcelable -> readParcelableCreator -> creator.createFromParcel

e('SearchActivity.handleSearchRequest', 'SearchParameters$$Parcelable.<clinit>', 'FRAMEWORK',
  'readParcelableCreator reads the class named in the parcel and calls Field.get(null) on CREATOR, which initialises the wrapper class (static initialiser creates CREATOR)',
  cls='non_standard', via='intent.getParcelableExtra(EXTRA_SEARCH_PARAMETERS) at SearchActivity.java:156 -> Intent.java:7166-7168 -> Bundle.getParcelable -> unparcel (Bundle.java:938-939; BaseBundle.java:222) -> Parcel.readValue (Parcel.java:2728, 2744-2745) -> readParcelable (2841-2851) -> readParcelableCreator (2867; Class.forName 2888; getField 2894; f.get(null) 2907)',
  evidence='SRC search/SearchActivity.java:151-157; FW-SRC core/java/android/content/Intent.java:7166-7168; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/BaseBundle.java:222; FW-SRC core/java/android/os/Parcel.java:2728, 2744-2745, 2841-2851, 2867, 2888, 2894, 2907; INFERRED: the intent arrives from the sender in parcelled form (IPC, not in fw_src)')

e('SearchActivity.handleSearchRequest', 'SearchParameters$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the framework reads the creator of the wrapper and calls createFromParcel on it, which builds the wrapper and reads its fields',
  cls='non_standard', via='intent.getParcelableExtra(EXTRA_SEARCH_PARAMETERS) at SearchActivity.java:156 -> Intent.java:7166-7168 -> Bundle.getParcelable -> unparcel (Bundle.java:938-939; BaseBundle.java:222) -> Parcel.readValue -> readParcelable -> creator.createFromParcel (Parcel.java:2851)',
  evidence='SRC search/SearchActivity.java:151-157; FW-SRC core/java/android/content/Intent.java:7166-7168; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/BaseBundle.java:222; FW-SRC core/java/android/os/Parcel.java:2728, 2744-2745, 2841-2851; INFERRED: the intent arrives in parcelled form (IPC, not in fw_src)')

e('SearchParametersFragment.getSearchParameters', 'SearchParameters$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the fragment arguments hold the wrapper; when the arguments are unparcelled (after the fragment is restored from a saved parcel) the framework calls createFromParcel',
  guard='the arguments bundle is still parcelled: it has been written and read back, e.g. after the fragment is restored from saved state (INFERRED)',
  cls='non_standard', via='arguments.getParcelable(KEY_SEARCH_CRITERIA) at SearchParametersFragment.java:320 -> Bundle.getParcelable -> unparcel (Bundle.java:938-939; BaseBundle.java:222) -> Parcel.readValue -> readParcelable -> creator.createFromParcel (Parcel.java:2851)',
  evidence='SRC search/SearchParametersFragment.java:316-324; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/BaseBundle.java:222; FW-SRC core/java/android/os/Parcel.java:2728, 2744-2745, 2841-2851; INFERRED: the arguments are restored from a parcel (fragment state restore not read)')

# ================================================================== UNREACHABLE (batch 108). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['SearchParameters$$Parcelable.describeContents'] = ('framework_never_calls',
  'Parcelable.describeContents of the wrapper has no caller in the app or in the framework path that the app reaches. In fw_src the only callers of Parcelable.describeContents are the Bundle.hasFileDescriptors loop (Bundle.java:329, 338, 349, 362). That loop runs only on an unparcelled bundle: when mParcelledData is set, hasFileDescriptors calls Parcel.hasFileDescriptors instead (Bundle.java:321). The loop is entered only from Bundle.describeContents (Bundle.java:1215-1217, which has no caller in fw_src) and from Intent.hasFileDescriptors (Intent.java:6958-6959), whose callers are system_server services (ActivityStarter.java:681, 919; ActivityManagerService.java 4652 onward). Intent.describeContents (Intent.java:9552-9553) has no caller in fw_src. The app source never calls describeContents or hasFileDescriptors (grep B1), so the wrapper is never asked for its file-descriptor mask in the app process.',
  'grep B1, B3, B4, B7 in graphs/MMEX/parts/label_108.grep.txt; FW-SRC core/java/android/os/Bundle.java:316-330, 1215-1217; FW-SRC core/java/android/content/Intent.java:6958-6959, 9552-9553; FW-SRC services/core/java/com/android/server/am/ActivityStarter.java:681; INFERRED: the parceler library (generated wrapper method and any describeContents call it makes) not read; system_server cannot load the app wrapper class (Parcel.java:2888 Class.forName), so it never sees the wrapper',
  'INFERRED')

UNREACHABLE['SearchParameters$$Parcelable$1.newArray'] = ('no_trigger_in_app',
  'Parcelable.Creator.newArray of the wrapper creator is called only from Parcel.createTypedArray (Parcel.java:2645). createTypedArray is called in fw_src from FragmentManager (FragmentState and BackStackState CREATORs, FragmentManager.java:587, 589) and from MediaPlayer (TrackInfo.CREATOR, MediaPlayer.java:2465); readTypedArray (Parcel.java:2674) has no caller in fw_src. None of these passes the SearchParameters creator. The app source has no createTypedArray or readTypedArray call (grep B2), so the wrapper creator never reaches createTypedArray in the app.',
  'grep B2, B5, B6, B7 in graphs/MMEX/parts/label_108.grep.txt; FW-SRC core/java/android/os/Parcel.java:2638-2646, 2672-2676; FW-SRC core/java/android/app/FragmentManager.java:587, 589; FW-SRC media/java/android/media/MediaPlayer.java:2465; INFERRED: the generated $1 class (parceler library not read)',
  'INFERRED')

# no sup pairs (see the header comment)

# ---- part 109 (2026-10-29)
# ================================================================== batch 109 (label_109): SearchParametersFragment (+ $1, $2, $3, $4), SearchParametersFragment_MembersInjector
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_109.md. Class-file and grep evidence: graphs/MMEX/parts/label_109.grep.txt.
# Edges below have a batch 109 method (or S_SEARCH) as destination (D1). CALL edges already in auto_calls.json are not written here (D7).
# Already in graph_def.py and not repeated: INTENT $1.onClick -> PayeeActivity.<init>/<clinit> (lines 115-133); INTENT onAmountFromClicked and onAmountToClicked -> CalculatorActivity.<init> (lines 2185-2191); INTENT $2.onClick -> CategoryListActivity.<init>/<clinit> (lines 2420-2428).
# S_SEARCH is defined here. Batch 107 (SearchActivity, which hosts this fragment) must reuse the key S_SEARCH and write the ENTERS edge into it (D6). Until batch 107 is merged, a page-not-reachable error for S_SEARCH is expected (D8).
# The ButterKnife handlers onDateFromClicked, onDateToClicked, onAmountFromClicked and onAmountToClicked are reached through the generated SearchParametersFragment_ViewBinding$1..$4.doClick listeners (auto CALL records). Their page-to-listener GUI edges belong to the ViewBinding batch and are not written here.

SCREENS.update({
    'S_SEARCH': 'Search screen (SearchActivity hosts SearchParametersFragment): the form for the search parameters (account, currency, transaction type, status, dates, amounts, payee, category, transaction number, notes); the options menu Reset icon clears the form; the search itself is run by SearchActivity',
})

# ---- fragment lifecycle (androidx Fragment; library source not read: INFERRED)

e('SearchParametersFragment.<init>', 'SearchParametersFragment.onCreate', 'LIFECYCLE',
  'SearchActivity.createSearchFragment adds the fragment to the transaction (commit at line 130) and the FragmentManager then calls onCreate',
  evidence='SRC search/SearchActivity.java:124-130; SRC search/SearchParametersFragment.java:84-85, 119-121; INFERRED androidx Fragment lifecycle (library not read)')

e('SearchParametersFragment.onCreate', 'SearchParametersFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC search/SearchParametersFragment.java:119-133; INFERRED androidx Fragment lifecycle (library not read)')

e('SearchParametersFragment.onCreate', 'SearchParametersFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'setHasOptionsMenu(true) (line 125) makes the framework build the options menu: it calls onCreateOptionsMenu on the fragment',
  evidence='SRC search/SearchParametersFragment.java:119-125, 289-299; INFERRED androidx FragmentManager dispatches onCreateOptionsMenu (library not read); precedent label_103 (setHasOptionsMenu)')

e('SearchParametersFragment.onCreateView', 'SearchParametersFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework calls onSaveInstanceState on the fragment once its view has been created (the view exists before any state is saved)',
  evidence='SRC search/SearchParametersFragment.java:133-143, 275-287; INFERRED androidx Fragment saves state (library not read); same chain as label_103 (CategoriesReportFragment.onActivityCreated to BaseReportFragment.onSaveInstanceState)')

# ---- date pickers (framework DatePickerDialog; the dialog calls the listener on OK)

e('SearchParametersFragment.onDateFromClicked', 'SearchParametersFragment$3.onDateSet', 'FRAMEWORK',
  'the date-from dialog (built at line 348 with the listener $3, shown at 368): the OK button calls the listener onDateSet',
  evidence='SRC search/SearchParametersFragment.java:344-369 (listener 350-352, show 368); FW-SRC core/java/android/app/DatePickerDialog.java:88-91 (constructor passes the listener on), 122 (positive button is this), 136 (mDateSetListener = listener), 164-172 (OK calls mDateSetListener.onDateSet at 171); precedent label_007 (DatePickerDialog)')

e('SearchParametersFragment.onDateToClicked', 'SearchParametersFragment$4.onDateSet', 'FRAMEWORK',
  'the date-to dialog (built at line 375 with the listener $4, shown at 395): the OK button calls the listener onDateSet',
  evidence='SRC search/SearchParametersFragment.java:371-396 (listener 377-379, show 395); FW-SRC core/java/android/app/DatePickerDialog.java:88-91, 122, 136, 164-172 (OK calls mDateSetListener.onDateSet at 171); precedent label_007 (DatePickerDialog)')

# ---- results from the pickers and the calculator (RESULT; the result-setting method is the source, as in label_006 and label_099; D1 destination is onActivityResult)

e('PayeeListFragment.sendResultToActivity', 'SearchParametersFragment.onActivityResult', 'RESULT',
  'the payee list returns the payee id and name and finishes: setResult(RESULT_OK), and the framework delivers the result to onActivityResult of the fragment that started it (request code PAYEE)',
  guard='requestCode is RequestCodes.PAYEE (SearchParametersFragment.java:194, 242); data is not null and resultCode is not RESULT_CANCELED (SearchParametersFragment.java:236)',
  evidence='SRC fragment/PayeeListFragment.java:309-331 (sendResultToActivity call 316, setResult RESULT_OK 329, finish 331); SRC search/SearchParametersFragment.java:189-196, 233-243; FW-SRC core/java/android/app/ActivityThread.java:4253-4265; FW-SRC core/java/android/app/Activity.java:7259-7266; INFERRED androidx FragmentActivity forwards the result to the fragment (library not read)')

e('CategoryListFragment.setResult', 'SearchParametersFragment.onActivityResult', 'RESULT',
  'the category list returns the category and subcategory ids and names and finishes: setResult(RESULT_OK) when a row was picked, and the framework delivers the result to onActivityResult of the fragment (request code CATEGORY)',
  guard='requestCode is RequestCodes.CATEGORY (SearchParametersFragment.java:204, 246); data is not null and resultCode is not RESULT_CANCELED (SearchParametersFragment.java:236); RESULT_OK only when a row was picked (CategoryListFragment.java:354)',
  evidence='SRC common/CategoryListFragment.java:313-356 (setResult RESULT_OK at 354, RESULT_CANCELED at 356); SRC search/SearchParametersFragment.java:199-205, 233-255; FW-SRC core/java/android/app/ActivityThread.java:4253-4265; FW-SRC core/java/android/app/Activity.java:7259-7266; INFERRED androidx FragmentActivity forwards the result to the fragment (library not read)')

e('CalculatorActivity.returnResult', 'SearchParametersFragment.onActivityResult', 'RESULT',
  'the calculator returns the amount as text in RESULT_AMOUNT and finishes: setResult(RESULT_OK), and the framework delivers the result to onActivityResult of the fragment (request codes AMOUNT_FROM or AMOUNT_TO)',
  guard='requestCode is RequestCodes.AMOUNT_FROM or AMOUNT_TO (SearchParametersFragment.java:405, 415, 257, 265); data is not null and resultCode is not RESULT_CANCELED (SearchParametersFragment.java:236)',
  evidence='SRC common/CalculatorActivity.java:435-444 (putExtra RESULT_AMOUNT 442, setResult RESULT_OK 443, finish 444); SRC common/Calculator.java:77-83 (fragment path startActivityForResult at 81); SRC search/SearchParametersFragment.java:257-271; FW-SRC core/java/android/app/ActivityThread.java:4253-4265; FW-SRC core/java/android/app/Activity.java:7259-7266; precedent label_006 (CalculatorActivity.returnResult)')

# ---- user actions on the search screen (GUI; page -> method, D6)

gui('S_SEARCH', 'SearchParametersFragment$1.onClick',
    'Tap Select payee (textViewSelectPayee) in the search form: the payee list opens for picking',
    evidence='SRC search/SearchParametersFragment.java:189-196; SRC search/SearchParametersViewHolder.java:44 (txtSelectPayee from textViewSelectPayee); SRC res/layout/search_parameters_fragment.xml:177')

gui('S_SEARCH', 'SearchParametersFragment$2.onClick',
    'Tap Select category (textViewSelectCategory) in the search form: the category list opens for picking',
    evidence='SRC search/SearchParametersFragment.java:199-206, 715 (txtSelectCategory from textViewSelectCategory); SRC res/layout/search_parameters_fragment.xml:187')

gui('S_SEARCH', 'SearchParametersFragment.onOptionsItemSelected',
    'Options menu: tap the Reset icon (clearMenuItem) to clear every search field',
    evidence='SRC search/SearchParametersFragment.java:302-310; SRC res/menu/menu_clear.xml:25; INFERRED androidx dispatches the menu item to the fragment (library not read)')

# ---- Dagger members injector: only injectDateTimeUtilsLazy is reached (auto CALL from DaggerMmxComponent, not written here).
# The two sup pairs cut the auto records whose callers are UNREACHABLE in this batch (D14).

sup(('SearchParametersFragment_MembersInjector.create', 'SearchParametersFragment_MembersInjector.<init>'),
    ('SearchParametersFragment_MembersInjector.injectMembers', 'SearchParametersFragment_MembersInjector.injectDateTimeUtilsLazy'))

# ---- UNREACHABLE (no_trigger_in_app). Tuple: (kind, reason, evidence, confirmed_by). Evidence: graphs/MMEX/parts/label_109.grep.txt.

UNREACHABLE['SearchParametersFragment_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes one Provider). Its only caller is create, and create has no caller: the constant pool scan finds no class that refers to create or injectMembers (grep section 2). The only auto record with this destination is create -> <init> (section 3), which the sup pair cuts.',
  'label_109.grep.txt sections 1, 2 and 3; auto_calls record SearchParametersFragment_MembersInjector.java:25',
  'INFERRED')

UNREACHABLE['SearchParametersFragment_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory method. No class file refers to it (grep section 2). DaggerMmxComponent refers only to the static injectDateTimeUtilsLazy (section 2). No auto record has create as its destination (section 3).',
  'label_109.grep.txt sections 1, 2 and 3',
  'INFERRED')

UNREACHABLE['SearchParametersFragment_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance injector (takes a SearchParametersFragment). No class other than the injector refers to it (grep section 2). Its only in-class reference is from the synthetic bridge injectMembers(Object) (access 0x1041), and no class calls that bridge, so neither is reached. Its outgoing auto record injectMembers -> injectDateTimeUtilsLazy (line 30) is cut by the sup pair (section 3).',
  'label_109.grep.txt sections 2 and 3; auto_calls record SearchParametersFragment_MembersInjector.java:30',
  'INFERRED')

# ---- part 110 (2026-10-29)
# ================================================================== batch 110 (label_110): SearchParametersFragment_ViewBinding (10 methods), SearchParametersViewHolder (1), SearchParametersViewHolder_ViewBinding (2), AccountService (19)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_110.md. Class-file and grep evidence: graphs/MMEX/parts/label_110.grep.txt.
# Edges below have a batch 110 method as destination (D1). CALL edges already in auto_calls.json are not written here (D7).
# S_SEARCH is defined by batch 109 (label_109.py, SCREENS.update). This batch reuses that key and defines no page.
# The ButterKnife reflection calls are not in auto_calls.json, so they are written here (cls='non_standard').

# ---- ButterKnife bindings of the search screen (generated classes not in the source root: INFERRED)

e('SearchParametersFragment.onCreateView', 'SearchParametersFragment_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, view) builds the generated binding for the fragment, which binds the @OnClick listeners and the views',
  cls='non_standard', via='ButterKnife.bind(this, view) (library): the generated SearchParametersFragment_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC search/SearchParametersFragment.java:139 (ButterKnife.bind(this, view)); INFERRED ButterKnife generated binding; auto_calls.json records 3461-3464 start from the generated constructor (not from onCreateView)')

e('SearchParametersViewHolder.<init>', 'SearchParametersViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, view) in the holder constructor builds the generated binding for the holder views',
  cls='non_standard', via='ButterKnife.bind(this, view) (library): the generated SearchParametersViewHolder_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC search/SearchParametersViewHolder.java:35-37 (constructor; ButterKnife.bind at 36); INFERRED ButterKnife generated binding')

# ---- user actions on the search form (GUI; page -> method, D6). The listeners are generated by ButterKnife (INFERRED).

gui('S_SEARCH', 'SearchParametersFragment_ViewBinding$1.doClick',
    'Tap the From date field (textViewFromDate) in the search form: the date picker for the start date opens (onDateFromClicked)',
    cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
    evidence='SRC search/SearchParametersFragment.java:344-345 (onDateFromClicked); SRC res/layout/search_parameters_fragment.xml:154 (textViewFromDate); auto_calls.json:3478 ($1.doClick -> onDateFromClicked, SearchParametersFragment_ViewBinding.java:35)')

gui('S_SEARCH', 'SearchParametersFragment_ViewBinding$2.doClick',
    'Tap the To date field (textViewToDate) in the search form: the date picker for the end date opens (onDateToClicked)',
    cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
    evidence='SRC search/SearchParametersFragment.java:371-372 (onDateToClicked); SRC res/layout/search_parameters_fragment.xml:165 (textViewToDate); auto_calls.json:3481 ($2.doClick -> onDateToClicked, SearchParametersFragment_ViewBinding.java:43)')

gui('S_SEARCH', 'SearchParametersFragment_ViewBinding$3.doClick',
    'Tap the From amount field (textViewFromAmount) in the search form: the amount entry for the lower bound opens (onAmountFromClicked)',
    cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
    evidence='SRC search/SearchParametersFragment.java:398-399 (onAmountFromClicked); SRC res/layout/search_parameters_fragment.xml:122 (textViewFromAmount); auto_calls.json:3477 ($3.doClick -> onAmountFromClicked, SearchParametersFragment_ViewBinding.java:51)')

gui('S_SEARCH', 'SearchParametersFragment_ViewBinding$4.doClick',
    'Tap the To amount field (textViewToAmount) in the search form: the amount entry for the upper bound opens (onAmountToClicked)',
    cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
    evidence='SRC search/SearchParametersFragment.java:408-409 (onAmountToClicked); SRC res/layout/search_parameters_fragment.xml:135 (textViewToAmount); auto_calls.json:3503 ($4.doClick -> onAmountToClicked, SearchParametersFragment_ViewBinding.java:59)')

# ---- sup pairs (D14): the auto CALL records whose caller is UNREACHABLE in this batch are cut.
# Cut records: AccountService.createAccount (auto_calls 2570-2573) and AccountService.getAccountCurrencyCode (2596-2602).
# The two unbind methods have no outgoing auto record, so nothing is cut for them.

sup(('AccountService.createAccount', 'AccountRepository.save'),
    ('AccountService.createAccount', 'AccountRepository.<init>'),
    ('AccountService.createAccount', 'ServiceBase.getContext'),
    ('AccountService.createAccount', 'Account.create'))

sup(('AccountService.getAccountCurrencyCode', 'Currency.getCode'),
    ('AccountService.getAccountCurrencyCode', 'CurrencyService.getCurrency(Integer)'),
    ('AccountService.getAccountCurrencyCode', 'CurrencyService.<init>'),
    ('AccountService.getAccountCurrencyCode', 'ServiceBase.getContext'),
    ('AccountService.getAccountCurrencyCode', 'Account.getCurrencyId'),
    ('AccountService.getAccountCurrencyCode', 'RepositoryBase.first'),
    ('AccountService.getAccountCurrencyCode', 'AccountRepository.<init>'))

# ---- UNREACHABLE (no_trigger_in_app). Tuple: (kind, reason, evidence, confirmed_by). Evidence: graphs/MMEX/parts/label_110.grep.txt.

UNREACHABLE['SearchParametersFragment_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated unbind (not in the source root). Its only caller would be the Unbinder returned by ButterKnife.bind(this, view) at SearchParametersFragment.java:139, and that return value is discarded. No class in the app source refers to Unbinder or unbind (grep, section 1), and auto_calls has no record with unbind as source or destination (section 3).',
  'SRC search/SearchParametersFragment.java:139; label_110.grep.txt sections 1 and 3',
  'INFERRED')

UNREACHABLE['SearchParametersViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated unbind (not in the source root). Its only caller would be the Unbinder returned by ButterKnife.bind(this, view) at SearchParametersViewHolder.java:36, and that return value is discarded. No class in the app source refers to Unbinder or unbind (grep, section 1), and auto_calls has no record with unbind as source or destination (section 3).',
  'SRC search/SearchParametersViewHolder.java:36; label_110.grep.txt sections 1 and 3',
  'INFERRED')

UNREACHABLE['AccountService.createAccount'] = ('no_trigger_in_app',
  'Public method with no caller in the app: the only app-source match is its definition (AccountService.java:68). No reference in src/main/java, res or the manifest (grep, section 2), and auto_calls has no record with it as destination (section 3). The two JUnit test sources that call it are not app triggers. Its outgoing records 2570-2573 are cut by sup (D14).',
  'SRC servicelayer/AccountService.java:68-77; label_110.grep.txt sections 2 and 3',
  'SOURCE')

UNREACHABLE['AccountService.getAccountCurrencyCode'] = ('no_trigger_in_app',
  'Public method with no caller in the app: the only app-source match is its definition (AccountService.java:182). No reference in src/main/java, res or the manifest (grep, section 2), and auto_calls has no record with it as destination (section 3). The JUnit test sources are not app triggers. Its outgoing records 2596-2602 are cut by sup (D14).',
  'SRC servicelayer/AccountService.java:182-193; label_110.grep.txt sections 2 and 3',
  'SOURCE')

# ---- part 111 (2026-10-29)
# ================================================================== batch 111 (label_111): CategoryService (10), InfoService (7), InfoService_MembersInjector (4), PayeeService (7); 28 methods
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_111.md. Class-file and grep evidence: graphs/MMEX/parts/label_111.grep.txt.
# 21 methods are REACHABLE and 7 are UNREACHABLE. No e(...) edges are written: every incoming edge to a batch 111 method is an auto CALL record (D7).
# sup pairs cut the auto records whose caller is UNREACHABLE in this batch (D14): 3 from CategoryService.createNewSubcategory, 5 from PayeeService.loadByName,
# 1 from PayeeService.exists, 1 from InfoService_MembersInjector.create and 1 from InfoService_MembersInjector.injectMembers.
# InfoService.insertRaw(SQLiteDatabase,String,String) has no outgoing auto record, so it needs no sup pair.
# Sources outside this batch (D1, interim until those batches merge): CheckingTransactionEditActivity.handleIntent and externalIntegration (exported ACTION_INSERT activity),
# IntentDataParameters.parseData, SplitCategoriesAdapter.bindCategory, QifRecord.getSplitCategory, MainActivity.onCreate, Passcode.loadPasscode,
# MmxOpenHelper.initDatabase, initDateFormat and initBaseCurrency, MmexApplication, CategoryListFragment and PayeeListFragment (batches 029 and 073 are REACHABLE for these callers).

# ---- UNREACHABLE (no_trigger_in_app). Tuple: (kind, reason, evidence, confirmed_by). Evidence: graphs/MMEX/parts/label_111.grep.txt.

UNREACHABLE['CategoryService.createNewSubcategory'] = ('no_trigger_in_app',
  'No caller in the app. The only occurrence of the name in the source is its definition. The category dialogs call createNew, getList, update and isCategoryUsed, never createNewSubcategory. No auto record has it as destination. Its three outgoing records are cut by sup pairs.',
  'SRC servicelayer/CategoryService.java:71-87 (definition); label_111.grep.txt section 1 (createNewSubcategory: definition only); auto_calls 2548-2550 (outgoing only)',
  'SOURCE')

UNREACHABLE['InfoService.insertRaw(SQLiteDatabase,String,String)'] = ('no_trigger_in_app',
  'No caller. The only insertRaw call in the app is MmxOpenHelper.java:296, and its db argument is a SupportSQLiteDatabase, so the SupportSQLiteDatabase overload is resolved (auto_calls 1162). No auto record has this overload as destination. It has no outgoing auto record, so no sup pair is needed.',
  'SRC servicelayer/InfoService.java:63-70 (definition); SRC database/MmxOpenHelper.java:256 (db is SupportSQLiteDatabase), 296; label_111.grep.txt section 1 (insertRaw); auto_calls 1162',
  'SOURCE')

UNREACHABLE['PayeeService.exists'] = ('no_trigger_in_app',
  'No caller. The grep for exists( finds the definition (PayeeService.java:105) and no call to PayeeService.exists in the app (the other hits belong to File, Repository and Service classes). No auto record has it as destination. Its outgoing record exists -> loadByName (line 108, auto_calls 2665) is cut by a sup pair.',
  'SRC servicelayer/PayeeService.java:105-110; label_111.grep.txt section 1 (exists); auto_calls 2665 (outgoing only)',
  'SOURCE')

UNREACHABLE['PayeeService.loadByName'] = ('no_trigger_in_app',
  'Its only caller is exists (PayeeService.java:108), and exists has no caller. No other source line or auto record calls loadByName. Its five outgoing records (auto_calls 2653-2657) are cut by sup pairs.',
  'SRC servicelayer/PayeeService.java:43-63, 108; label_111.grep.txt section 1 (loadByName); auto_calls 2665 (incoming), 2653-2657 (outgoing)',
  'SOURCE')

UNREACHABLE['InfoService_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller is create (auto_calls 2683), and create has no caller: no class file refers to create, and DaggerMmxComponent refers only to injectRepository.',
  'label_111.grep.txt sections 1, 2, 3 and 4 (auto_calls 2683); class-file parse of InfoService_MembersInjector.class (method table and self references)',
  'INFERRED')

UNREACHABLE['InfoService_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory. No class file refers to it: the binary grep finds the class name only in DaggerMmxComponent.class and in the injector class, and the parse of DaggerMmxComponent.class has no reference to create. No auto record has create as destination.',
  'label_111.grep.txt sections 1, 2, 3 and 4 (auto_calls 2683 outgoing, cut by sup pair)',
  'INFERRED')

UNREACHABLE['InfoService_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance injector (takes an InfoService). No class file calls it: DaggerMmxComponent refers only to injectRepository. The only reference inside the class is the synthetic bridge injectMembers(Object) (access 0x1041), which nothing refers to. No auto record has injectMembers as destination. Its outgoing record to injectRepository (auto_calls 2684) is cut by a sup pair.',
  'label_111.grep.txt sections 2, 3 and 4 (auto_calls 2684 outgoing, cut by sup pair)',
  'INFERRED')

# ---- sup pairs (D14): the auto records whose caller is UNREACHABLE in this batch. Names are the exact auto_calls names.

sup(('CategoryService.createNewSubcategory', 'Dataset.getUri'),
    ('CategoryService.createNewSubcategory', 'ServiceBase.getContext'),
    ('CategoryService.createNewSubcategory', 'CategoryRepository.<init>'),
    ('PayeeService.loadByName', 'EntityBase.loadFromCursor'),
    ('PayeeService.loadByName', 'Payee.<init>()'),
    ('PayeeService.loadByName', 'PayeeRepository.getAllColumns'),
    ('PayeeService.loadByName', 'Dataset.getUri'),
    ('PayeeService.loadByName', 'ServiceBase.getContext'),
    ('PayeeService.exists', 'PayeeService.loadByName'),
    ('InfoService_MembersInjector.create', 'InfoService_MembersInjector.<init>'),
    ('InfoService_MembersInjector.injectMembers', 'InfoService_MembersInjector.injectRepository'))

# ---- part 112 (2026-10-29)
# ================================================================== batch 112 (label_112): RecurringTransactionService (17 methods), ServiceBase (2), QifExport (5), QifGenerator (2), QifHeader (6), QifRecord (8)
# Result: 36 REACHABLE, 4 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_112.md). Grep and auto_calls evidence: graphs/MMEX/parts/label_112.grep.txt (sections 1-9).
# No e() edges and no SCREENS: every REACHABLE route is an auto CALL record (auto_calls.json, bytecode-derived; D7). The routes start at callers in other batches (MainActivity, CheckingTransactionEditActivity, RecurringTransactionEditActivity, RecurringTransactionListFragment, AllDataListFragment).
# This file writes:
#   - UNREACHABLE entries for RecurringTransactionService.<init>(Context), RecurringTransactionService.load, RecurringTransactionService.getRecurrenceLocalizedName, QifHeader.createCreditCardHeader (SOURCE),
#   - 4 sup pairs (D14): the auto CALL records out of the UNREACHABLE methods.
# QifHeader.createCreditCardHeader has no CALL record out, so it has no sup pair. Its framework call (StringBuilder.<init>) and the framework calls of getRecurrenceLocalizedName (Context.getResources, Resources.getStringArray) are framework_calls, not CALL records to app methods, so they are not cut.

# ================================================================== RecurringTransactionService: UNREACHABLE (source evidence)

UNREACHABLE['RecurringTransactionService.<init>(Context)'] = ('no_trigger_in_app',
    'no caller: every constructor call in app source is the two-argument form (MainActivity.java:1281; CheckingTransactionEditActivity.java:238, 700; RecurringTransactionEditActivity.java:451; RecurringTransactionListFragment.java:312, 341); no subclass exists; no bytecode CALL record targets this constructor',
    'servicelayer/RecurringTransactionService.java:47-50; label_112.grep.txt sections 1, 2, 6, 7',
    'SOURCE')

UNREACHABLE['RecurringTransactionService.load'] = ('no_trigger_in_app',
    'no caller: no bytecode CALL record targets load, and in the five app files that name the service no call is made on a RecurringTransactionService variable (the .load calls there are on repository or database objects)',
    'servicelayer/RecurringTransactionService.java:167-169; label_112.grep.txt sections 3a-3d, 6, 7',
    'SOURCE')

UNREACHABLE['RecurringTransactionService.getRecurrenceLocalizedName'] = ('no_trigger_in_app',
    'no caller: the name occurs only at its declaration in the whole source root (every file type), and no bytecode CALL record targets it',
    'servicelayer/RecurringTransactionService.java:335-350; label_112.grep.txt sections 4, 6, 7, 9',
    'SOURCE')

# ================================================================== QifHeader: UNREACHABLE (source evidence)

UNREACHABLE['QifHeader.createCreditCardHeader'] = ('no_trigger_in_app',
    'private, no caller: the name occurs only at its declaration (QifHeader.java:131) in the whole source root, and no bytecode CALL record targets it; the body only returns the placeholder "not implemented" (line 142)',
    'servicelayer/qif/QifHeader.java:131-143; label_112.grep.txt sections 5, 7, 9',
    'SOURCE')

# ================================================================== sup (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('RecurringTransactionService.<init>(Context)', 'ServiceBase.<init>'))  # the unreachable constructor's call into the base constructor cannot run (RecurringTransactionService.java:48)
sup(('RecurringTransactionService.load', 'RecurringTransactionRepository.load'))  # load has no caller (RecurringTransactionService.java:168)
sup(('RecurringTransactionService.load', 'RecurringTransactionService.getRepository'))  # load has no caller (RecurringTransactionService.java:168)
sup(('RecurringTransactionService.getRecurrenceLocalizedName', 'ServiceBase.getContext'))  # getRecurrenceLocalizedName has no caller (RecurringTransactionService.java:345)

# ---- part 113 (2026-10-29)
# ================================================================== batch 113 (label_113): AppSettings (9 methods), AppSettings_Factory (4), AppSettings_MembersInjector (4), BaseSettingsFragmentActivity (4), BehaviourSettings (14), BehaviourSettingsActivity (3): 38 methods
# Result: 29 REACHABLE, 9 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_113.md). Grep and auto_calls evidence: graphs/MMEX/parts/label_113.grep.txt.
# Auto CALL records (auto_calls.json) are not rewritten here (D7). The routes that the auto data cannot give are written here:
#   - the Behaviour preference in SettingsFragment starts BehaviourSettingsActivity by an explicit intent (INTENT), then the activity lifecycle (LIFECYCLE), and the activity enters page S_BEHAVIOUR_SETTINGS (ENTERS),
#   - the SMS permission answer goes back to BehaviourSettingsActivity.onRequestPermissionsResult (FRAMEWORK, settings gate, D19),
#   - the EventBus subscriber BaseSettingsFragmentActivity.onEvent gets two ASYNC edges (the same routes as MmxBaseFragmentActivity.onEvent in batch 032).
# This file writes:
#   - SCREENS: S_BEHAVIOUR_SETTINGS (no settings page exists in the SCREENS keys; the activity is one screen, D9),
#   - e() edges whose destination this batch owns (D1),
#   - UNREACHABLE entries: AppSettings.getInvestmentSettings and BehaviourSettings.getIncomeExpensePeriod (SOURCE); AppSettings_Factory (4) and AppSettings_MembersInjector.create, .<init>, .injectMembers (INFERRED, generated code, evidence in label_113.grep.txt),
#   - sup pairs (D14): auto CALL records whose caller is UNREACHABLE in this batch.

SCREENS.update({
    'S_BEHAVIOUR_SETTINGS': 'Behaviour settings screen (BehaviourSettingsActivity hosts BehaviourSettingsFragment; the notification time and the SMS automation switch are set on this screen)',
})

# ---- BehaviourSettingsActivity: explicit intent from the settings list, lifecycle, the page, and the SMS permission answer

e('SettingsFragment$3.onPreferenceClick', 'BehaviourSettingsActivity.<init>', 'INTENT',
  'the Behaviour preference in the settings list starts BehaviourSettingsActivity with an explicit intent, and the framework instantiates the manifest-declared activity',
  evidence='SRC settings/SettingsFragment.java:87 (listener created), 89-93 (onPreferenceClick), 90 (startActivity(new Intent(getActivity(), BehaviourSettingsActivity.class))); SRC AndroidManifest.xml:253-255 (declared, no intent-filter, not exported)')

e('BehaviourSettingsActivity.<init>', 'BehaviourSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor of the activity (INFERRED framework launch order, not re-read in this batch)',
  evidence='SRC settings/BehaviourSettingsActivity.java:26-27 (class declaration, no explicit constructor), 29-33 (onCreate); INFERRED framework launch order (constructor, then onCreate)')

e('BehaviourSettingsActivity.onCreate', 'S_BEHAVIOUR_SETTINGS', 'ENTERS',
  'the activity shows the Behaviour settings page: onCreate installs BehaviourSettingsFragment through setSettingFragment',
  evidence='SRC settings/BehaviourSettingsActivity.java:29-33 (setSettingFragment(new BehaviourSettingsFragment()) at 32); SRC settings/BaseSettingsFragmentActivity.java:71-92')

e('BehaviourSettingsFragment$2.onPreferenceClick', 'BehaviourSettingsActivity.onRequestPermissionsResult', 'FRAMEWORK',
  'the SMS automation switch is turned on while RECEIVE_SMS is not granted: the fragment requests it with ActivityCompat.requestPermissions (request code 1), and the framework returns the answer to the activity',
  needs_state=state_text('the SMS automation switch is turned on while the RECEIVE_SMS permission is not granted', ('settings',)),
  evidence='SRC settings/BehaviourSettingsFragment.java:129 (onPreferenceClick), 138 (getBankSmsTrans), 140 (granted test), 144-147 (else branch: ActivityCompat.requestPermissions(getActivity(), ..., 1)); SRC settings/BehaviourSettingsActivity.java:36-39 (override, requestCode == 1); INFERRED framework answer path not re-read in this batch')

# ---- BaseSettingsFragmentActivity: EventBus subscriber, two ASYNC routes (the same routes that batch 032 writes for MmxBaseFragmentActivity.onEvent)

e('DebugTree.log', 'BaseSettingsFragmentActivity.onEvent', 'ASYNC',
  'a debug build logs an error through Timber while a settings activity is registered: DebugTree posts ErrorRaisedEvent and EventBus calls onEvent (the subclass inherits the registration from MmxBaseFragmentActivity.onStart)',
  env=env_text('an error is logged through Timber while a settings activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/DebugTree.java:45-46 (posts only when a subscriber exists); SRC MmexApplication.java:134-135 (DebugTree in the debug branch); SRC settings/BaseSettingsFragmentActivity.java:52-55 (@Subscribe onEvent(ErrorRaisedEvent)); SRC common/MmxBaseFragmentActivity.java:141 (register in onStart); INFERRED EventBus library source not read')

e('ScreenTree.log', 'BaseSettingsFragmentActivity.onEvent', 'ASYNC',
  'a release build logs an error through Timber while a settings activity is registered: ScreenTree posts ErrorRaisedEvent and EventBus calls onEvent (the debug build plants DebugTree instead)',
  env=env_text('an error is logged through Timber while a settings activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/ScreenTree.java:26-27; SRC MmexApplication.java:134-140 (ScreenTree in the else branch, release only); SRC settings/BaseSettingsFragmentActivity.java:52-55; SRC common/MmxBaseFragmentActivity.java:141; INFERRED EventBus library source not read')

# ================================================================== UNREACHABLE: source evidence (SOURCE)

UNREACHABLE['AppSettings.getInvestmentSettings'] = ('no_trigger_in_app',
    'no caller: the name occurs only at its declaration in the whole source root, and no bytecode CALL record targets it (auto_calls.json: 0 incoming records)',
    'settings/AppSettings.java:87-92; label_113.grep.txt sections 5',
    'SOURCE')

UNREACHABLE['BehaviourSettings.getIncomeExpensePeriod'] = ('no_trigger_in_app',
    'no caller: the only other occurrence in the source root is HomeFragment.java:252, a commented-out line; no bytecode CALL record targets it (auto_calls.json: 0 incoming records)',
    'settings/BehaviourSettings.java:61-65; label_113.grep.txt sections 5, 6',
    'SOURCE')

# ================================================================== UNREACHABLE: generated Dagger methods (INFERRED, D16)

UNREACHABLE['AppSettings_Factory.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is AppSettings_Factory.create (auto_calls.json: AppSettings_Factory.class bytecode line 35), and create has no caller',
    'AppSettings_Factory.class bytecode line 35 (generated; class file final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/settings/AppSettings_Factory.class); label_113.grep.txt sections 2, 3, 4',
    'INFERRED')

UNREACHABLE['AppSettings_Factory.create'] = ('no_trigger_in_app',
    'generated static factory with no caller: no source reference (label_113.grep.txt section 1), no incoming auto_calls record, and the component builds AppSettings through MmxModule_ProvideAppSettingsFactory (DaggerMmxComponent.java:189)',
    'AppSettings_Factory.class bytecode line 35 (generated); label_113.grep.txt sections 1-4',
    'INFERRED')

UNREACHABLE['AppSettings_Factory.get'] = ('no_trigger_in_app',
    'generated provider method with no caller: no incoming auto_calls record and no source reference; the component uses MmxModule_ProvideAppSettingsFactory (DaggerMmxComponent.java:189), not this factory',
    'AppSettings_Factory.class bytecode line 27-28 (generated); label_113.grep.txt sections 1-4',
    'INFERRED')

UNREACHABLE['AppSettings_Factory.newAppSettings'] = ('no_trigger_in_app',
    'generated method with no caller: no incoming auto_calls record and no source reference; it is reached only from AppSettings_Factory.get, which is itself unreachable',
    'AppSettings_Factory.class bytecode line 39 (generated); label_113.grep.txt sections 1-4',
    'INFERRED')

UNREACHABLE['AppSettings_MembersInjector.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is AppSettings_MembersInjector.create (auto_calls.json: AppSettings_MembersInjector.class bytecode line 23), and create has no caller',
    'AppSettings_MembersInjector.class bytecode line 23 (generated; class file final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/settings/AppSettings_MembersInjector.class); label_113.grep.txt sections 2, 3',
    'INFERRED')

UNREACHABLE['AppSettings_MembersInjector.create'] = ('no_trigger_in_app',
    'generated static factory with no caller: no source reference (label_113.grep.txt section 1) and no incoming auto_calls record; the component calls injectSharedPreferences directly (DaggerMmxComponent.java:511), not create or injectMembers',
    'AppSettings_MembersInjector.class bytecode line 23 (generated); label_113.grep.txt sections 1-3',
    'INFERRED')

UNREACHABLE['AppSettings_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'generated members-injector method with no caller: no incoming auto_calls record and no source reference; the component reaches injectSharedPreferences directly (DaggerMmxComponent.java:511), not through injectMembers',
    'AppSettings_MembersInjector.class bytecode line 28 (generated); label_113.grep.txt sections 1, 3, 4',
    'INFERRED')

# ================================================================== sup (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('AppSettings.getInvestmentSettings', 'InvestmentSettings.<init>'))  # the unreachable getter's call into the investment settings constructor (AppSettings.java:89)
sup(('AppSettings.getInvestmentSettings', 'SettingsBase.getContext'))  # AppSettings.java:89
sup(('BehaviourSettings.getIncomeExpensePeriod', 'SettingsBase.get(Integer,String)@BehaviourSettings'))  # BehaviourSettings.java:62
sup(('BehaviourSettings.getIncomeExpensePeriod', 'SettingsBase.getContext'))  # BehaviourSettings.java:63
sup(('AppSettings_Factory.create', 'AppSettings_Factory.<init>'))  # AppSettings_Factory.class bytecode line 35
sup(('AppSettings_Factory.get', 'AppSettings_MembersInjector.injectSharedPreferences'))  # AppSettings_Factory.class bytecode line 28
sup(('AppSettings_Factory.get', 'AppSettings.<init>'))  # AppSettings_Factory.class bytecode line 27
sup(('AppSettings_Factory.newAppSettings', 'AppSettings.<init>'))  # AppSettings_Factory.class bytecode line 39
sup(('AppSettings_MembersInjector.create', 'AppSettings_MembersInjector.<init>'))  # AppSettings_MembersInjector.class bytecode line 23
sup(('AppSettings_MembersInjector.injectMembers', 'AppSettings_MembersInjector.injectSharedPreferences'))  # AppSettings_MembersInjector.class bytecode line 28

# ---- part 114 (2026-10-29)
# ================================================================== batch 114 (label_114): BehaviourSettingsFragment (13 methods), BudgetSettings (4), BudgetSettingsActivity (2), BudgetSettingsFragment (5), DatabaseSettings (3), DatabaseSettingsActivity (2)
# Result: 28 REACHABLE, 1 UNREACHABLE, 0 INCOMPLETE (rows and printed lines: graphs/MMEX/parts/label_114.md). Grep evidence: graphs/MMEX/parts/label_114.grep.txt.
# The batch file header says 29 methods; its 36 lines are 29 method lines plus 7 comment lines. The 29 method lines are labelled here.
# Routes: the Settings list (SettingsFragment, anonymous classes $3, $5, $7) opens the Behaviour, Budget and Database settings activities. The activities create their fragments (auto CALL records). The fragment lifecycle edges are LIFECYCLE, as in label_005, label_010 and label_018.
# This file writes:
#   - SCREENS for S_BEHAVIOUR_SETTINGS, S_BUDGET_SETTINGS and S_DATABASE_SETTINGS (none existed in SCREENS; D9),
#   - INTENT edges into BudgetSettingsActivity.<init> and DatabaseSettingsActivity.<init> (their destinations are owned here; D1; the BehaviourSettingsActivity INTENT belongs to its own batch),
#   - LIFECYCLE edges into the three activity onCreate methods and the three fragment onCreate methods, plus the fragment chain onCreate -> onCreatePreferences -> onStart -> onStop,
#   - ENTERS edges from the two activity onCreate methods, GUI edges from S_BEHAVIOUR_SETTINGS, and one REGISTER edge for the time-picker lambda,
#   - 1 UNREACHABLE entry (BudgetSettings.setShowSimpleView) and 1 sup pair (D14).
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).

SCREENS.update({
    'S_BEHAVIOUR_SETTINGS': 'Behaviour settings screen (BehaviourSettingsActivity): the preference list from preferences_behaviour.xml, with the repeating transaction check (time picker) and the bank SMS automation preferences',
    'S_BUDGET_SETTINGS': 'Budget settings screen (BudgetSettingsActivity): the preference list from preferences_budget.xml, shown by BudgetSettingsFragment',
    'S_DATABASE_SETTINGS': 'Database settings screen (DatabaseSettingsActivity): the database preference list hosted by DatabaseSettingsFragment',
})

# ---- SettingsFragment start sites (INTENT edges into this batch's activities; dst owned here, D1)

e('SettingsFragment$5.onPreferenceClick', 'BudgetSettingsActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), BudgetSettingsActivity.class)) from the budget preference',
  gui=['Open Settings and tap the budget preference'],
  evidence='SRC settings/SettingsFragment.java:114-118 (anonymous class $5 is created at line 113: auto_calls SettingsFragment.onCreate -> SettingsFragment$5.<init>)')

e('SettingsFragment$7.onPreferenceClick', 'DatabaseSettingsActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), DatabaseSettingsActivity.class)) from the database preference',
  gui=['Open Settings and tap the database preference'],
  evidence='SRC settings/SettingsFragment.java:140-144 (anonymous class $7 is created at line 139: auto_calls SettingsFragment.onCreate -> SettingsFragment$7.<init>)')

# ---- BudgetSettingsActivity

e('BudgetSettingsActivity.<init>', 'BudgetSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_004 AboutActivity)',
  evidence='SRC settings/BudgetSettingsActivity.java:19-30; FW-SRC core/java/android/app/ActivityThread.java:2724-2731 (as cited in label_004, not read in this batch)')

e('BudgetSettingsActivity.onCreate', 'S_BUDGET_SETTINGS', 'ENTERS',
  'the Budget settings screen is shown',
  evidence='SRC settings/BudgetSettingsActivity.java:19-30 (setSettingFragment(new BudgetSettingsFragment()) at line 28)')

# ---- BudgetSettingsFragment (fragment lifecycle; library source not read: INFERRED)

e('BudgetSettingsFragment.<init>', 'BudgetSettingsFragment.onCreate', 'LIFECYCLE',
  'BaseSettingsFragmentActivity.setSettingFragment replaces the content with the fragment (line 78) and commits the transaction (line 91); the FragmentManager then calls onCreate',
  evidence='SRC settings/BaseSettingsFragmentActivity.java:70-92; SRC settings/BudgetSettingsActivity.java:19-30; INFERRED androidx Fragment lifecycle (library source not read; the same pattern as label_018)')

e('BudgetSettingsFragment.onCreate', 'BudgetSettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: the inherited PreferenceFragmentCompat code, not read)',
  evidence='SRC settings/BudgetSettingsFragment.java:19-60 (onCreatePreferences inflates R.xml.preferences_budget)')

e('BudgetSettingsFragment.onCreatePreferences', 'BudgetSettingsFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after the preference view is created (INFERRED androidx Fragment lifecycle)',
  evidence='SRC settings/BudgetSettingsFragment.java:19-60')

e('BudgetSettingsFragment.onStart', 'BudgetSettingsFragment.onStop', 'LIFECYCLE',
  'the user leaves the Budget settings screen and the framework stops the fragment (onResume and onPause are not methods of this class, so this edge skips them; INFERRED)',
  evidence='SRC settings/BudgetSettingsFragment.java:19-60')

# ---- BehaviourSettingsFragment (the activity creates it at BehaviourSettingsActivity.java:32; that CALL is auto)

e('BehaviourSettingsFragment.<init>', 'BehaviourSettingsFragment.onCreate', 'LIFECYCLE',
  'BehaviourSettingsActivity.onCreate calls setSettingFragment (line 32): the fragment is committed (BaseSettingsFragmentActivity.java:78, 91) and the FragmentManager then calls onCreate (INFERRED androidx Fragment lifecycle)',
  evidence='SRC settings/BehaviourSettingsActivity.java:19-40; SRC settings/BaseSettingsFragmentActivity.java:70-92; SRC settings/BehaviourSettingsFragment.java:39-166')

e('BehaviourSettingsFragment.onCreate', 'BehaviourSettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: the inherited PreferenceFragmentCompat code, not read); onCreatePreferences then calls initializeNotificationTime and initializeSmsAutomation (lines 57-58)',
  evidence='SRC settings/BehaviourSettingsFragment.java:45-59')

e('BehaviourSettingsFragment.onCreatePreferences', 'BehaviourSettingsFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after the preference view is created (INFERRED androidx Fragment lifecycle)',
  evidence='SRC settings/BehaviourSettingsFragment.java:52-66')

e('BehaviourSettingsFragment.onStart', 'BehaviourSettingsFragment.onStop', 'LIFECYCLE',
  'the user leaves the Behaviour settings screen and the framework stops the fragment (onResume and onPause are not methods of this class, so this edge skips them; INFERRED)',
  evidence='SRC settings/BehaviourSettingsFragment.java:62-73')

# ---- BehaviourSettingsFragment click listeners and the time-picker callback

e('S_BEHAVIOUR_SETTINGS', 'BehaviourSettingsFragment$1.onPreferenceClick', 'GUI',
  'the user taps the repeating transaction check preference (PreferenceConstants.PREF_REPEATING_TRANSACTION_CHECK, line 78): the listener calls showTimePicker',
  evidence='SRC settings/BehaviourSettingsFragment.java:77-89 (listener at 81, onPreferenceClick at 83, showTimePicker call at 84, setOnPreferenceClickListener at 88)')

e('S_BEHAVIOUR_SETTINGS', 'BehaviourSettingsFragment$2.onPreferenceClick', 'GUI',
  'the user taps the bank SMS automation preference (PreferenceConstants.PREF_SMS_AUTOMATIC_TRANSACTIONS, line 122): the listener checks the RECEIVE_SMS permission inside an SDK_INT >= 23 test (line 132) or turns the setting off',
  evidence='SRC settings/BehaviourSettingsFragment.java:118-164 (listener at 126, onPreferenceClick at 129-161, setBankSmsTrans at 154); the minSdk value was not read, so the SDK_INT test is not resolved')

e('BehaviourSettingsFragment.showTimePicker', 'BehaviourSettingsFragment.lambda$showTimePicker$0', 'REGISTER',
  'showTimePicker passes the lambda to a new TimePickerDialog (lines 101-106) and shows it (line 114); the dialog calls the lambda when the user sets the time',
  evidence='SRC settings/BehaviourSettingsFragment.java:91-115 (lambda at 101-104, setNotificationTime at 103)')

# ---- UNREACHABLE (D14 cut of its one outgoing auto record)

UNREACHABLE['BudgetSettings.setShowSimpleView'] = ('no_trigger_in_app',
    'no caller: the name occurs only at its declaration (BudgetSettings.java:45) in the whole source root, and no auto_calls.json record has it as dst; its one outgoing record (-> SettingsBase.set(Integer,boolean)@BudgetSettings, line 46) is cut by sup below',
    'settings/BudgetSettings.java:45-47; label_114.grep.txt section A',
    'SOURCE')

sup(('BudgetSettings.setShowSimpleView', 'SettingsBase.set(Integer,boolean)@BudgetSettings'))  # setShowSimpleView has no caller (BudgetSettings.java:46)

# ---- DatabaseSettingsActivity

e('DatabaseSettingsActivity.<init>', 'DatabaseSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_004 AboutActivity)',
  evidence='SRC settings/DatabaseSettingsActivity.java:19-30; FW-SRC core/java/android/app/ActivityThread.java:2724-2731 (as cited in label_004, not read in this batch)')

e('DatabaseSettingsActivity.onCreate', 'S_DATABASE_SETTINGS', 'ENTERS',
  'the Database settings screen is shown',
  evidence='SRC settings/DatabaseSettingsActivity.java:19-30 (setSettingFragment(new DatabaseSettingsFragment()) at line 28)')

# ---- part 115 (2026-10-29)
# ================================================================== batch 115 (label_115): DatabaseSettingsFragment (16 methods), DatabaseSettingsFragment$1 to $5 (10), DatabaseSettingsFragment_MembersInjector (5), GeneralSettings (9): 40 methods
# Result: 36 REACHABLE, 4 UNREACHABLE (rows: graphs/MMEX/parts/label_115.md). Grep and auto_calls evidence: graphs/MMEX/parts/label_115.grep.txt (sections 1-4).
# Page S_DATABASE_SETTINGS is defined in label_114.py (SCREENS.update, line 16) and entered from DatabaseSettingsActivity.onCreate (ENTERS, label_114.py line 106). This part reuses it: the five preference taps are GUI edges from the page, as in label_114.py lines 79-85.
# Other edges: LIFECYCLE from BaseSettingsFragmentActivity.setSettingFragment (tx.commit at line 91) to DatabaseSettingsFragment.onCreate; LIFECYCLE from onCreate to onCreatePreferences (the framework call is INFERRED, as in label_114.py line 47); RESULT from requestBackup to onActivityResult (the document picker returns the result).
# CALL edges come from auto_calls.json and are not written here. DatabaseSettingsFragment_MembersInjector is generated by Dagger and has no source file in the source root, so its UNREACHABLE entries are INFERRED (grep sections 1-3).

# ---- the fragment's lifecycle: setSettingFragment commits the transaction, the FragmentManager runs onCreate, then onCreatePreferences

e('DatabaseSettingsFragment.<init>', 'DatabaseSettingsFragment.onCreate', 'LIFECYCLE',
  'the fragment is committed: tx.commit() (line 91) makes the FragmentManager run onCreate; setSettingFragment is called from DatabaseSettingsActivity.onCreate (source call at DatabaseSettingsActivity.java:28)',
  evidence='SRC settings/BaseSettingsFragmentActivity.java:71-92 (tx.replace 78, tx.commit 91); SRC settings/DatabaseSettingsActivity.java:26-29 (setSettingFragment at 28); INFERRED androidx FragmentManager (library not in the dataset; source not read)')

e('DatabaseSettingsFragment.onCreate', 'DatabaseSettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: the inherited PreferenceFragmentCompat code, not read)',
  evidence='SRC settings/DatabaseSettingsFragment.java:62-63 (super.onCreate), 96-99 (empty body); auto_calls.json framework_calls DatabaseSettingsFragment.onCreate lists PreferenceFragmentCompat.onCreate; precedent label_114.py line 47')

# ---- the five preference taps: the page S_DATABASE_SETTINGS (label_114.py) shows the preferences; each listener is set in its initX method (CALL, auto)

e('S_DATABASE_SETTINGS', 'DatabaseSettingsFragment$1.onPreferenceClick', 'GUI',
  'the user taps the clear recent files preference (pref_clear_recent_files): the listener clears the recent list and shows the count',
  evidence='SRC settings/DatabaseSettingsFragment.java:113-128 (listener set at 113; onPreferenceClick 115-127); RES res/xml/preferences_database.xml:37')

e('S_DATABASE_SETTINGS', 'DatabaseSettingsFragment$2.onPreferenceClick', 'GUI',
  'the user taps the check schema preference (pref_db_check_schema): the listener runs checkSchema and shows a toast',
  evidence='SRC settings/DatabaseSettingsFragment.java:161-178 (listener 161-176; set at 178); RES res/xml/preferences_database.xml:52')

e('S_DATABASE_SETTINGS', 'DatabaseSettingsFragment$3.onPreferenceClick', 'GUI',
  'the user taps the check integrity preference (pref_database_check_integrity): the listener runs checkIntegrity and shows a toast',
  evidence='SRC settings/DatabaseSettingsFragment.java:187-209 (listener 187-207; set at 209); RES res/xml/preferences_database.xml:47')

e('S_DATABASE_SETTINGS', 'DatabaseSettingsFragment$4.onPreferenceClick', 'GUI',
  'the user taps the backup preference (pref_database_backup, PreferenceConstants.PREF_DATABASE_BACKUP): the listener calls requestBackup',
  evidence='SRC settings/DatabaseSettingsFragment.java:258-268 (listener 261-268); SRC settings/PreferenceConstants.java:46; RES res/xml/preferences_database.xml:42')

e('S_DATABASE_SETTINGS', 'DatabaseSettingsFragment$5.onPreferenceClick', 'GUI',
  'the user taps the fix duplicates preference (pref_db_fix_duplicates): the listener runs fixDuplicates and shows a toast',
  evidence='SRC settings/DatabaseSettingsFragment.java:280-305 (listener 284-302; set at 304); RES res/xml/preferences_database.xml:57')

# ---- the backup picker: requestBackup starts the document picker; the framework delivers the result to onActivityResult

e('DatabaseSettingsFragment.requestBackup', 'DatabaseSettingsFragment.onActivityResult', 'RESULT',
  'the document picker (ACTION_CREATE_DOCUMENT) returns: the framework delivers the result to onActivityResult with CODE_BACKUP and RESULT_OK',
  evidence='SRC settings/DatabaseSettingsFragment.java:212-232 (startActivityForResult 218; onActivityResult guard 225; backupDatabase 229); precedent label_018.py line 39 and label_006.py line 75')

# ---- UNREACHABLE: the generated MembersInjector methods and the setter have no caller (grep output: graphs/MMEX/parts/label_115.grep.txt)

UNREACHABLE['DatabaseSettingsFragment_MembersInjector.<init>'] = (
  'no_trigger_in_app',
  'generated constructor with no live caller: its only CALL record is from create (DatabaseSettingsFragment_MembersInjector.class bytecode line 31), and create is itself UNREACHABLE; no other CALL record targets the constructor',
  'generated by Dagger (no source file in the source root); auto_calls.json record at DatabaseSettingsFragment_MembersInjector.class bytecode line 31; label_115.grep.txt sections 2-3',
  'INFERRED')

UNREACHABLE['DatabaseSettingsFragment_MembersInjector.create'] = (
  'no_trigger_in_app',
  'generated static factory with no caller: no CALL record targets create; DaggerMmxComponent.class has no MembersInjector return descriptor (constant-pool count 0), and the component reaches the fragment through injectDatabaseSettingsFragment, which calls the static injectOpenHelper and injectMDatabases directly (DaggerMmxComponent.java:449, 451)',
  'generated by Dagger (no source file in the source root); no auto_calls.json record has create as dst; label_115.grep.txt sections 1-3',
  'INFERRED')

UNREACHABLE['DatabaseSettingsFragment_MembersInjector.injectMembers'] = (
  'no_trigger_in_app',
  'generated interface method with no caller: no CALL record targets injectMembers, and DaggerMmxComponent.class has no injectMembers name (constant-pool count 0); its two CALL records (lines 36, 37) are cut by sup',
  'generated by Dagger (no source file in the source root); auto_calls.json records at DatabaseSettingsFragment_MembersInjector.class bytecode line 36-37; label_115.grep.txt sections 2-3',
  'INFERRED')

UNREACHABLE['GeneralSettings.setApplicationLanguage'] = (
  'no_trigger_in_app',
  'public setter with no caller: the name occurs only at its declaration in the app source root (GeneralSettings.java:56) and in the compiled class; no CALL record targets it; its one CALL record (SettingsBase.set(Integer,String)@GeneralSettings, line 57) is cut by sup',
  'settings/GeneralSettings.java:56-58; label_115.grep.txt sections 1-3',
  'SOURCE')

# ---- auto edges that cannot run: their source is UNREACHABLE (D14)

sup(('DatabaseSettingsFragment_MembersInjector.create', 'DatabaseSettingsFragment_MembersInjector.<init>'))  # create has no caller (MembersInjector.java:31)
sup(('DatabaseSettingsFragment_MembersInjector.injectMembers', 'DatabaseSettingsFragment_MembersInjector.injectMDatabases'))  # injectMembers has no caller (MembersInjector.java:37)
sup(('DatabaseSettingsFragment_MembersInjector.injectMembers', 'DatabaseSettingsFragment_MembersInjector.injectOpenHelper'))  # injectMembers has no caller (MembersInjector.java:36)
sup(('GeneralSettings.setApplicationLanguage', 'SettingsBase.set(Integer,String)@GeneralSettings'))  # setApplicationLanguage has no caller (GeneralSettings.java:57)

# ---- part 116 (2026-10-29)
# ================================================================== batch 116 (label_116): GeneralSettingsActivity (3), GeneralSettingsFragment (7) and its listeners $1-$4 (8), InvestmentPreferencesViewHolder (1), InvestmentSettings (8), InvestmentSettingsActivity (2): 29 methods
# Result: 28 REACHABLE, 1 UNREACHABLE (InvestmentSettings.getPreferences), 0 INCOMPLETE. Rows and reasons: graphs/MMEX/parts/label_116.md. Grep and auto_calls evidence: graphs/MMEX/parts/label_116.grep.txt.
# The brief said 35 methods. batch_116.txt has 35 lines in total: 6 comment lines and 29 method lines. The 29 method lines are labelled here.
# This file writes 2 SCREENS keys (S_GENERAL_SETTINGS and S_INVESTMENT_SETTINGS; grep of graph_def.py and parts/*.py found no key for either screen), 15 e() edges, 1 UNREACHABLE entry and 1 sup pair.
# Every other REACHABLE route is an auto CALL record (auto_calls.json, bytecode-derived; D7) and is cited in the row, not written here.

SCREENS.update({
    'S_GENERAL_SETTINGS': 'General settings screen (GeneralSettingsActivity with GeneralSettingsFragment): application language, theme, default status, default payee and the anonymous usage data switch',
    'S_INVESTMENT_SETTINGS': 'Investment settings screen (InvestmentSettingsActivity with InvestmentSettingsFragment): asset allocation threshold, quote provider and exchange rate provider',
})

# ---- GeneralSettingsActivity: the two intents that open it, then the framework's lifecycle calls

e('SettingsFragment$10.onPreferenceClick', 'GeneralSettingsActivity.<init>', 'INTENT',
  'startActivityForResult(new Intent(getActivity(), GeneralSettingsActivity.class)) from the general preference',
  gui=['Open Settings and tap the general preference'],
  evidence='SRC settings/SettingsFragment.java:226-233 (listener; Intent at 229; startActivityForResult at 230)')

e('TutorialActivity.onCloseClicked', 'GeneralSettingsActivity.<init>', 'INTENT',
  'new Intent(this, GeneralSettingsActivity.class) and startActivityForResult from the Skip control of the tutorial (@OnClick R.id.skipTextView)',
  gui=['Tap the skip control on the tutorial screen'],
  evidence='SRC tutorial/TutorialActivity.java:90-96 (@OnClick at 90; Intent at 93; startActivityForResult at 95)')

e('GeneralSettingsActivity.<init>', 'GeneralSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC settings/GeneralSettingsActivity.java:28-31')

e('GeneralSettingsActivity.onCreate', 'S_GENERAL_SETTINGS', 'ENTERS',
  'the general settings screen is shown: setSettingFragment replaces the content with GeneralSettingsFragment',
  evidence='SRC settings/GeneralSettingsActivity.java:28-31 (setSettingFragment at 30); SRC settings/BaseSettingsFragmentActivity.java:71-78')

e('GeneralSettingsActivity.onCreate', 'GeneralSettingsActivity.onResume', 'LIFECYCLE',
  'the framework calls onResume after onCreate: ActivityThread.handleResumeActivity calls performResume (same chain as CalculatorActivity.onCreate, graph_def.py:2207)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3556, 3608; FW-SRC core/java/android/app/Activity.java:7098-7107; SRC settings/GeneralSettingsActivity.java:34-38')

# ---- GeneralSettingsFragment: the fragment transaction starts it, then super.onCreate reaches onCreatePreferences

e('GeneralSettingsFragment.<init>', 'GeneralSettingsFragment.onCreate', 'LIFECYCLE',
  'the fragment transaction (replace at line 78) is committed and the framework then runs the onCreate of the new fragment',
  evidence='SRC settings/BaseSettingsFragmentActivity.java:71-78; INFERRED androidx FragmentManager runs the fragment lifecycle after a commit (library not in the dataset)')

e('GeneralSettingsFragment.onCreate', 'GeneralSettingsFragment.onCreatePreferences', 'FRAMEWORK',
  'super.onCreate (PreferenceFragmentCompat.onCreate) calls onCreatePreferences',
  evidence='SRC settings/GeneralSettingsFragment.java:39-42 (super.onCreate at 40); INFERRED androidx PreferenceFragmentCompat.onCreate calls onCreatePreferences (library not in the dataset)')

# ---- GeneralSettingsFragment listeners: the framework calls onPreferenceChange when the user changes a value (GUI from the screen)

e('S_GENERAL_SETTINGS', 'GeneralSettingsFragment$1.onPreferenceChange', 'GUI',
  'the application language list preference changes: the listener updates the summary and restarts the activity',
  gui=['Change the application language on the general settings screen'],
  evidence='SRC settings/GeneralSettingsFragment.java:62-72 (listener set at 62; setSummaryListPreference at 66; restartActivity at 68)')

e('S_GENERAL_SETTINGS', 'GeneralSettingsFragment$2.onPreferenceChange', 'GUI',
  'the theme list preference changes: the listener restarts the activity',
  gui=['Change the theme on the general settings screen'],
  evidence='SRC settings/GeneralSettingsFragment.java:79-88 (listener set at 79; restartActivity at 84)')

e('S_GENERAL_SETTINGS', 'GeneralSettingsFragment$3.onPreferenceChange', 'GUI',
  'the default status list preference changes: the listener updates the summary',
  gui=['Change the default status on the general settings screen'],
  evidence='SRC settings/GeneralSettingsFragment.java:96-102 (listener set at 96; setSummaryListPreference at 99)')

e('S_GENERAL_SETTINGS', 'GeneralSettingsFragment$4.onPreferenceChange', 'GUI',
  'the default payee list preference changes: the listener updates the summary',
  gui=['Change the default payee option on the general settings screen'],
  evidence='SRC settings/GeneralSettingsFragment.java:110-116 (listener set at 110; setSummaryListPreference at 113)')

e('S_GENERAL_SETTINGS', 'GeneralSettingsFragment.lambda$initializeControls$0', 'GUI',
  'the anonymous usage data switch (pref_anonymous_usage) is toggled: the lambda sets the analytics opt-out',
  gui=['Toggle the anonymous usage data switch on the general settings screen'],
  evidence='SRC settings/GeneralSettingsFragment.java:122-128 (listener set at 122; setOptOut at 125)')

# ---- InvestmentSettingsActivity: the intent from the investment preference, then the lifecycle calls

e('SettingsFragment$4.onPreferenceClick', 'InvestmentSettingsActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), InvestmentSettingsActivity.class)) from the investment preference',
  gui=['Open Settings and tap the investment preference'],
  evidence='SRC settings/SettingsFragment.java:100-106 (listener; Intent at 103)')

e('InvestmentSettingsActivity.<init>', 'InvestmentSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC settings/InvestmentSettingsActivity.java:26-29')

e('InvestmentSettingsActivity.onCreate', 'S_INVESTMENT_SETTINGS', 'ENTERS',
  'the investment settings screen is shown: setSettingFragment replaces the content with InvestmentSettingsFragment',
  evidence='SRC settings/InvestmentSettingsActivity.java:26-29 (setSettingFragment at 28); SRC settings/BaseSettingsFragmentActivity.java:71-78')

# ================================================================== InvestmentSettings.getPreferences: UNREACHABLE (source and grep evidence)

UNREACHABLE['InvestmentSettings.getPreferences'] = ('no_trigger_in_app',
    'no caller reaches it: its only incoming auto records are receiver variants of the inherited SettingsBase get, set, getBooleanSetting and getIntSetting with receiver InvestmentSettings (the @InvestmentSettings nodes), and those variant chains have no entry, because no app code calls an inherited get, set, getBooleanSetting or getIntSetting on an InvestmentSettings receiver (every InvestmentSettings use constructs the object and calls only its own getters and setters; AppSettings.getInvestmentSettings has no caller)',
    'settings/InvestmentSettings.java:48-50; settings/SettingsBase.java:52, 72-149; label_116.grep.txt sections 1-5',
    'SOURCE')

# ================================================================== sup (D14): the auto CALL record out of the UNREACHABLE method

sup(('InvestmentSettings.getPreferences', 'SettingsBase.getContext'))  # getPreferences has no caller (InvestmentSettings.java:49 calls getContext)

# Open point for the builder, not cut here: the generic cha records SettingsBase.get, set, getBooleanSetting and getIntSetting -> InvestmentSettings.getPreferences (SettingsBase.java:72, 84, 90, 98, 112, 116, 129, 145, 149) are owned by the SettingsBase batch. If the builder keeps them, getPreferences would look reachable from the generic SettingsBase nodes. Not run here (the builder is not run).

# ---- sup for part 116 (2026-10-30): receiver cut, no InvestmentSettings receiver runs an inherited SettingsBase accessor (no caller of the @InvestmentSettings chains; graphs/MMEX/parts/label_116.grep.txt)
sup(('SettingsBase.get(String,String)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,String)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(Integer,String)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,boolean)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.getBooleanSetting(String,boolean)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,boolean)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.getIntSetting', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,int)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,String)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,boolean)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.getBooleanSetting(String,boolean)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.getIntSetting@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(Integer,String)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,int)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,String)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.set(String,boolean)@InvestmentSettings', 'InvestmentSettings.getPreferences'))

# ---- part 118 (2026-10-29)
# ================================================================== batch 118 (label_118): LookFeelPreferenceFragment (15 methods), LookFeelSettingsActivity (2)
# Result: 17 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE (rows and printed lines: graphs/MMEX/parts/label_118.md). Grep evidence: graphs/MMEX/parts/label_118.grep.txt.
# Route: SettingsFragment$2 (Settings list, Look and feel item) -INTENT-> LookFeelSettingsActivity.<init> -LIFECYCLE-> onCreate -ENTERS-> S_LOOK_FEEL.
# The activity's onCreate builds the fragment (auto CALL record), which runs onCreate and creates six listeners (auto CALL records).
# GUI edges from S_LOOK_FEEL go to the six onPreferenceChange listeners (D6).
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).
# No UNREACHABLE entries and no sup pairs in this batch.

SCREENS.update({
    'S_LOOK_FEEL': 'Look and feel settings screen (LookFeelSettingsActivity hosts LookFeelPreferenceFragment): the account visibility, transaction period, font and font size preferences from preferences_look_and_feel.xml',
})

# ---- Settings list start site (INTENT edge into this batch's activity; dst owned here, D1)

e('SettingsFragment$2.onPreferenceClick', 'LookFeelSettingsActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), LookFeelSettingsActivity.class)) from the look and feel preference',
  gui=['Open Settings and tap the look and feel preference'],
  evidence='SRC settings/SettingsFragment.java:74-80 (start at line 77; anonymous class $2 is created at line 74: auto_calls.json SettingsFragment.onCreate -> SettingsFragment$2.<init>, record at line 1575)')

# ---- LookFeelSettingsActivity

e('LookFeelSettingsActivity.<init>', 'LookFeelSettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_114 BudgetSettingsActivity)',
  evidence='SRC settings/LookFeelSettingsActivity.java:22-29')

e('LookFeelSettingsActivity.onCreate', 'S_LOOK_FEEL', 'ENTERS',
  'the look and feel settings screen is shown',
  evidence='SRC settings/LookFeelSettingsActivity.java:25-29 (setSettingFragment(new LookFeelPreferenceFragment()) at line 28)')

# ---- LookFeelPreferenceFragment

e('LookFeelPreferenceFragment.<init>', 'LookFeelPreferenceFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the fragment is created',
  evidence='SRC settings/LookFeelPreferenceFragment.java:45-171 (framework lifecycle INFERRED)')

e('LookFeelPreferenceFragment.onCreate', 'LookFeelPreferenceFragment.onCreatePreferences', 'LIFECYCLE',
  'the inherited PreferenceFragmentCompat.onCreate calls the overridden onCreatePreferences (INFERRED, not read)',
  evidence='SRC settings/LookFeelPreferenceFragment.java:173-176')

# ---- GUI edges from the look and feel page to the preference listeners (D6)

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$1.onPreferenceChange', 'GUI',
  'the user toggles Show open accounts',
  gui=['Open Settings > Look and feel and toggle the open accounts checkbox'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:63-70 (listener registered at line 63; method at 65-69)')

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$2.onPreferenceChange', 'GUI',
  'the user toggles Show favourite accounts',
  gui=['Open Settings > Look and feel and toggle the favourite accounts checkbox'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:82-89 (listener registered at line 82; method at 84-88)')

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$3.onPreferenceChange', 'GUI',
  'the user toggles Hide Reconciled Amounts',
  gui=['Open Settings > Look and feel and toggle Hide Reconciled Amounts'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:97-103 (listener at line 97; method at 99-102)')

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$4.onPreferenceChange', 'GUI',
  'the user picks a new period in Show transactions',
  gui=['Open Settings > Look and feel and pick a value in Show transactions'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:125-134 (listener at line 125; method at 127-133)')

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$5.onPreferenceChange', 'GUI',
  'the user picks a font',
  gui=['Open Settings > Look and feel and pick a font'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:141-153 (listener at line 141; method at 143-152)')

e('S_LOOK_FEEL', 'LookFeelPreferenceFragment$6.onPreferenceChange', 'GUI',
  'the user picks a font size',
  gui=['Open Settings > Look and feel and pick a font size'],
  evidence='SRC settings/LookFeelPreferenceFragment.java:160-169 (listener at line 160; method at 163-168)')

# ---- part 119 (2026-10-29)
# ================================================================== batch 119 (label_119): PerDatabaseFragment (10 methods), PerDatabaseFragment$1 to $8 (16), PreferenceConstants (2), SecuritySettingsActivity (2): 30 methods
# Result: 30 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE (rows and printed lines: graphs/MMEX/parts/label_119.md). Grep and auto_calls evidence: graphs/MMEX/parts/label_119.grep.txt.
# SCREENS: S_PER_DATABASE_SETTINGS (new; the per-database list is a separate screen in SettingsActivity, D9) and S_SECURITY_SETTINGS (new; no S_SECURITY* key exists).
# The settings list (SettingsFragment) has no SCREENS key, so this part does not write GUI edges from it.
# Edges: INTENT SettingsFragment$6 -> SecuritySettingsActivity.<init> (dst owned here, D1); LIFECYCLE chains; ENTERS; GUI from the two pages to the listeners; RESULT CurrencyListFragment.setResult -> PerDatabaseFragment.onActivityResult.
# Not written: CALL edges (D7: every app call in this batch is an auto CALL record); the INTENT from PerDatabaseFragment$5 and $8 into CurrencyListActivity.<init> (owned by the CurrencyListActivity batch, D1); the INTENT from SettingsFragment$1 into SettingsActivity.<init> (owned by the SettingsActivity batch).
# No UNREACHABLE entries: every method has a route (see label_119.md).

SCREENS.update({
    'S_PER_DATABASE_SETTINGS': 'Per-database settings screen (SettingsActivity hosting PerDatabaseFragment, opened from the per-database preference of the settings list): the preference list from preferences_per_database.xml with the user name, date format, base currency, financial year start, and default account',
    'S_SECURITY_SETTINGS': 'Security settings screen (SecuritySettingsActivity): the security preference list hosted by SecuritySettingsFragment, opened from the passcode preference of the settings list',
})

# ---- SettingsFragment passcode preference -> SecuritySettingsActivity (INTENT into this batch's activity)

e('SettingsFragment$6.onPreferenceClick', 'SecuritySettingsActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), SecuritySettingsActivity.class)) from the passcode preference',
  gui=['Open Settings and tap the security (passcode) preference'],
  evidence='SRC settings/SettingsFragment.java:124-131 (listener set at 126; onPreferenceClick 128-130; startActivity at 129); auto_calls: SettingsFragment.onCreate -> SettingsFragment$6.<init> (SettingsFragment.java:126)')

# ---- SecuritySettingsActivity: lifecycle and page

e('SecuritySettingsActivity.<init>', 'SecuritySettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_114 BudgetSettingsActivity)',
  evidence='SRC settings/SecuritySettingsActivity.java:22-30 (class declaration, no explicit constructor; onCreate at 25-29); INFERRED framework launch order (constructor, then onCreate)')

e('SecuritySettingsActivity.onCreate', 'S_SECURITY_SETTINGS', 'ENTERS',
  'the security settings screen is shown',
  evidence='SRC settings/SecuritySettingsActivity.java:25-29 (setSettingFragment(new SecuritySettingsFragment()) at line 28)')

# ---- PerDatabaseFragment: lifecycle and page (SettingsActivity.showFragment creates the fragment, auto CALL)

e('PerDatabaseFragment.<init>', 'PerDatabaseFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the fragment is committed by setSettingFragment (SettingsActivity.java:71)',
  evidence='SRC settings/PerDatabaseFragment.java:59-68 (constructor, onCreate); SRC settings/SettingsActivity.java:63 (new PerDatabaseFragment), 71 (setSettingFragment); INFERRED androidx FragmentManager (library not in the dataset; source not read)')

e('PerDatabaseFragment.onCreate', 'PerDatabaseFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: the inherited PreferenceFragmentCompat code, not read)',
  evidence='SRC settings/PerDatabaseFragment.java:64-68 (onCreate, super call), 70-75 (onCreatePreferences); same pattern as label_114.py line 47')

e('PerDatabaseFragment.onCreatePreferences', 'S_PER_DATABASE_SETTINGS', 'ENTERS',
  'the per-database preference list (preferences_per_database) is added and shown',
  evidence='SRC settings/PerDatabaseFragment.java:70-75 (addPreferencesFromResource at 71; initializeControls at 73)')

# ---- the page's preference changes and clicks (GUI from the page, D6)

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$1.onPreferenceChange', 'GUI',
  'the user changes the user name preference (pref_user_name); the listener saves it through MmexApplication.setUserName',
  evidence='SRC settings/PerDatabaseFragment.java:103-110 (listener set at 103; onPreferenceChange 105-109); auto_calls: $1.onPreferenceChange -> MmexApplication.setUserName (line 106)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$2.onPreferenceChange', 'GUI',
  'the user picks a date format (pref_date_format); the listener saves it with InfoService.setInfoValue and updates the summary',
  evidence='SRC settings/PerDatabaseFragment.java:125-135 (listener set at 125; onPreferenceChange 128-134); auto_calls: $2.onPreferenceChange -> InfoService.setInfoValue (line 129), -> getDateFormatFromMask (line 130)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$3.onPreferenceChange', 'GUI',
  'the user enters the financial year start day (pref_financial_year_startdate); the listener validates it, saves it, and shows a toast on a parse error',
  evidence='SRC settings/PerDatabaseFragment.java:151-175 (listener set at 151; onPreferenceChange 153-174); auto_calls: $3.onPreferenceChange -> UIHelper.showToast (line 158), -> InfoService.setInfoValue (line 166)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$4.onPreferenceChange', 'GUI',
  'the user picks the financial year start month (pref_financial_year_startmonth); the listener saves it with InfoService.setInfoValue',
  evidence='SRC settings/PerDatabaseFragment.java:203-219 (listener set at 203; onPreferenceChange 206-217); auto_calls: $4.onPreferenceChange -> InfoService.setInfoValue (line 210)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$5.onPreferenceClick', 'GUI',
  'the user taps the base currency preference (pref_base_currency); the currency list opens for a pick (ACTION_PICK, startActivityForResult at line 244); the result returns to onActivityResult',
  evidence='SRC settings/PerDatabaseFragment.java:238-248 (listener set at 238; onPreferenceClick 240-247; startActivityForResult at 244)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$6.onPreferenceChange', 'GUI',
  'the user picks the default account (pref_default_account); the listener loads the account name and saves the id in GeneralSettings',
  evidence='SRC settings/PerDatabaseFragment.java:297-311 (listener set at 297; onPreferenceChange 299-310); auto_calls: $6.onPreferenceChange -> AccountRepository.loadName (line 303), -> GeneralSettings.setDefaultAccountId (line 307)')

# ---- the base currency changed dialog (shown on this page, D9): its two buttons

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$7.onClick', 'GUI',
  'the OK button of the base currency changed dialog (showCurrencyChangeNotification); no action',
  evidence='SRC settings/PerDatabaseFragment.java:327-344 (dialog built at 327-335; positive listener 331-336; onClick 333-334); auto_calls: onActivityResult -> showCurrencyChangeNotification (line 90)')

e('S_PER_DATABASE_SETTINGS', 'PerDatabaseFragment$8.onClick', 'GUI',
  'the Open currencies button of the same dialog: CurrencyListActivity opens for editing (ACTION_EDIT)',
  evidence='SRC settings/PerDatabaseFragment.java:337-344 (neutral listener 337-344; onClick 339-343; setAction at 341)')

# ---- the currency pick result (RESULT, D1: the dst is owned here)

e('CurrencyListFragment.setResult', 'PerDatabaseFragment.onActivityResult', 'RESULT',
  'the currency list returns RESULT_OK with the picked currency id (ACTION_PICK, opened from the base currency preference, PerDatabaseFragment$5.onPreferenceClick)',
  evidence='SRC currency/list/CurrencyListFragment.java:297-321 (setResult; putExtra at 309; setResult(RESULT_OK) at 314); SRC settings/PerDatabaseFragment.java:77-93 (onActivityResult reads INTENT_RESULT_CURRENCYID at 82)')

# ---- part 117 (2026-10-29)
# ================================================================== batch 117 (label_117): InvestmentSettingsFragment (11 methods, its $1-$3 listeners 6), LookAndFeelSettings (10)
# Result: 27 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE (rows and printed lines: graphs/MMEX/parts/label_117.md). Grep evidence: graphs/MMEX/parts/label_117.grep.txt.
# The batch file header says 27 methods; the 27 method lines are labelled here.
# Routes: SettingsFragment$4 (batch 116) starts InvestmentSettingsActivity, which creates InvestmentSettingsFragment; the fragment lifecycle edges are LIFECYCLE, as in label_114. LookAndFeelSettings methods are reached through auto CALL records only.
# This file writes:
#   - 3 GUI edges from the existing key S_INVESTMENT_SETTINGS (graph_def.py:10424; no SCREENS key is added here) to the three preference listeners,
#   - LIFECYCLE edges: InvestmentSettingsFragment.<init> -> onCreate -> onCreatePreferences -> onStart -> onStop,
#   - 1 REGISTER edge (onStart -> onEvent) and 1 ASYNC edge (AmountInputDialog$7.onClick -> onEvent) for EventBus (cls non_standard, as in label_050 and label_033).
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7). No UNREACHABLE entry and no sup pair.

# ---- the investment settings screen: GUI edges from the page into this batch's listeners (dst owned here, D1, D6)

e('S_INVESTMENT_SETTINGS', 'InvestmentSettingsFragment$1.onPreferenceClick', 'GUI',
  'the asset allocation threshold row is tapped: the listener shows the amount dialog with requestId KEY_THRESHOLD',
  gui=['Open Settings, tap the investment preference, then tap the asset allocation threshold'],
  evidence='SRC settings/InvestmentSettingsFragment.java:111-119 (getInstance at 116, show at 117; printed this session)')

e('S_INVESTMENT_SETTINGS', 'InvestmentSettingsFragment$2.onPreferenceChange', 'GUI',
  'the quote provider list preference changes: the listener stores the provider and calls displayQuotesProvider (auto CALL, line 146)',
  gui=['Open Settings, tap the investment preference, then choose a quote provider'],
  evidence='SRC settings/InvestmentSettingsFragment.java:140-148 (printed this session)')

e('S_INVESTMENT_SETTINGS', 'InvestmentSettingsFragment$3.onPreferenceChange', 'GUI',
  'the exchange rate provider list preference changes: the listener stores the provider and calls displayExchangeRatesProvider (auto CALL, line 175)',
  gui=['Open Settings, tap the investment preference, then choose an exchange rate provider'],
  evidence='SRC settings/InvestmentSettingsFragment.java:169-177 (printed this session)')

# ---- fragment lifecycle (dst owned here; the framework calls these after the constructor and in order, INFERRED androidx lifecycle)

e('InvestmentSettingsFragment.<init>', 'InvestmentSettingsFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the fragment is constructed by InvestmentSettingsActivity.onCreate (setSettingFragment at line 28)',
  evidence='SRC settings/InvestmentSettingsActivity.java:20-32 (setSettingFragment at 28); SRC settings/InvestmentSettingsFragment.java:39-55')

e('InvestmentSettingsFragment.onCreate', 'InvestmentSettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: inherited PreferenceFragmentCompat code, not read)',
  evidence='SRC settings/InvestmentSettingsFragment.java:45-62')

e('InvestmentSettingsFragment.onCreatePreferences', 'InvestmentSettingsFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after the preference view is created (INFERRED androidx lifecycle)',
  evidence='SRC settings/InvestmentSettingsFragment.java:58-69')

e('InvestmentSettingsFragment.onStart', 'InvestmentSettingsFragment.onStop', 'LIFECYCLE',
  'the framework calls onStop when the user leaves the screen (INFERRED androidx lifecycle)',
  evidence='SRC settings/InvestmentSettingsFragment.java:65-76')

# ---- EventBus: onStart registers the fragment until onStop; the amount dialog OK button posts AmountEnteredEvent (D17 pattern)

e('InvestmentSettingsFragment.onStart', 'InvestmentSettingsFragment.onEvent', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe onEvent receives AmountEnteredEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at InvestmentSettingsFragment.java:68, @Subscribe on onEvent (line 80); library source not read, INFERRED',
  evidence='SRC settings/InvestmentSettingsFragment.java:65-86 (register at 68, unregister at 75, @Subscribe at 80)')

e('AmountInputDialog$7.onClick', 'InvestmentSettingsFragment.onEvent', 'ASYNC',
  'the amount dialog OK button posts AmountEnteredEvent on the EventBus; for the threshold dialog the event carries KEY_THRESHOLD and onEvent stores the amount',
  cls='non_standard', via='EventBus (greenrobot) post at AmountInputDialog.java:260 (auto record AmountInputDialog$7.onClick -> AmountEnteredEvent.<init>, line 260); subscriber registered in InvestmentSettingsFragment.onStart',
  evidence='SRC common/AmountInputDialog.java:252-264 (post at 260); SRC settings/InvestmentSettingsFragment.java:80-86; INFERRED EventBus delivery (library not read)')

# ---- part 122 (2026-10-29)
# ================================================================== batch 122 (label_122): SyncPreferencesActivity (3), CloudItemViewHolder (2), CloudItemViewHolder$1 (2), CloudStorageProviderEnum (2), SyncBroadcastReceiver (2), SyncCommon (2), SyncConstants (1)
# Result: 5 REACHABLE, 9 UNREACHABLE, 0 INCOMPLETE (rows: graphs/MMEX/parts/label_122.md). Grep evidence: graphs/MMEX/parts/label_122.grep.txt.
# Routes: the Settings list (SettingsFragment$8) starts SyncPreferencesActivity; its BROWSABLE manifest filter is an outside entry.
# SyncBroadcastReceiver is created by the alarm that SyncSchedulerBroadcastReceiver.startHeartbeat sets.
# CloudItemViewHolder, CloudStorageProviderEnum and SyncCommon have no caller in the source root (grep A1-A3).
# This file writes: SCREENS S_SYNC_SETTINGS (none existed; D9); INTENT and ENTRY into SyncPreferencesActivity.<init>; ENTRY into onNewIntent.
# It also writes LIFECYCLE and ENTERS edges, a FRAMEWORK edge into SyncBroadcastReceiver.<init> (dst owned here), and LIFECYCLE into onReceive.
# 3 sup cuts remove auto CALL records whose caller is UNREACHABLE in this batch (D14). 9 UNREACHABLE entries.
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).

SCREENS.update({
    'S_SYNC_SETTINGS': 'Synchronization settings screen (SyncPreferencesActivity), which hosts SyncPreferenceFragment',
})

# ---- Start sites into this batch's activity (dst owned here, D1)

e('SettingsFragment$8.onPreferenceClick', 'SyncPreferencesActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), SyncPreferencesActivity.class)) from the Synchronisation preference',
  gui=['Open Settings and tap the Synchronisation preference'],
  evidence='SRC settings/SettingsFragment.java:153-158 (anonymous class $8 is created at line 153: auto_calls SettingsFragment.onCreate -> SettingsFragment$8.<init>, line 153)')

e('S_ENTRY', 'SyncPreferencesActivity.<init>', 'ENTRY',
  'The manifest declares the activity with a BROWSABLE VIEW filter for scheme com.money.manager.ex, so an outside link starts it when no instance is running; the framework creates it by class name (INFERRED)',
  evidence='SRC AndroidManifest.xml:268-279 (activity android:name=".settings.SyncPreferencesActivity", singleTask, exported, intent-filter VIEW/DEFAULT/BROWSABLE, data scheme com.money.manager.ex)')

# ---- SyncPreferencesActivity lifecycle and page

e('SyncPreferencesActivity.<init>', 'SyncPreferencesActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_114 BudgetSettingsActivity)',
  evidence='SRC settings/SyncPreferencesActivity.java:28-38; INFERRED framework lifecycle (not read)')

e('SyncPreferencesActivity.onCreate', 'S_SYNC_SETTINGS', 'ENTERS',
  'the Synchronization settings screen is shown: setSettingFragment(new SyncPreferenceFragment())',
  evidence='SRC settings/SyncPreferencesActivity.java:33-38 (setSettingFragment at line 37)')

e('S_ENTRY', 'SyncPreferencesActivity.onNewIntent', 'ENTRY',
  'When the activity is already running (singleTask), an outside BROWSABLE VIEW intent with scheme com.money.manager.ex (for example an authentication redirect) is delivered to it, and the framework calls onNewIntent directly (INFERRED delivery)',
  evidence='SRC settings/SyncPreferencesActivity.java:41-57 (Javadoc, onNewIntent, Timber at 52, super call at 56); SRC AndroidManifest.xml:268-279; grep A5 (BaseSettingsFragmentActivity does not declare onNewIntent, so super is the framework method)')

# ---- SyncBroadcastReceiver: created by the alarm, then onReceive

e('SyncSchedulerBroadcastReceiver.startHeartbeat', 'SyncBroadcastReceiver.<init>', 'FRAMEWORK',
  'startHeartbeat schedules an inexact repeating AlarmManager alarm whose PendingIntent is a broadcast to SyncBroadcastReceiver; when the alarm fires, the system creates the receiver to deliver the broadcast',
  needs_state=state_text('sync is enabled and the sync interval is above 0 (SyncSchedulerBroadcastReceiver.java:76, 82)', ('settings',)),
  via='AlarmManager repeat with a broadcast PendingIntent (AlarmManager delivery not read: INFERRED)',
  evidence='SRC sync/SyncSchedulerBroadcastReceiver.java:52-53 (PendingIntent to SyncBroadcastReceiver), 67 (startHeartbeat call), 76 (isSyncEnabled gate), 82 (interval gate), 90-94 (setInexactRepeating with pendingIntent); SRC AndroidManifest.xml:107 (receiver, no intent-filter); SRC home/MainActivity.java:242 (onCreate calls initializeSync), 1210-1218 (initializeSync calls sync.startSyncServiceHeartbeat when interval != 0), sync/SyncManager.java:268-273 (startSyncServiceHeartbeat sends the START broadcast); pattern label_096 (RecurringTransactionBootReceiver.setAlarm to RecurringTransactionReceiver.<init>); grep A6 and label_122.grep.txt section D')

e('SyncBroadcastReceiver.<init>', 'SyncBroadcastReceiver.onReceive', 'LIFECYCLE',
  'the framework calls onReceive on the receiver instance it has just created (INFERRED framework dispatch)',
  evidence='SRC sync/SyncBroadcastReceiver.java:31-45')

# ---- Auto CALL records whose caller is UNREACHABLE in this batch (D14): cut so no live edge leaves an UNREACHABLE method

sup(('CloudItemViewHolder.<init>', 'CloudItemViewHolder.initialize'))
sup(('CloudItemViewHolder.initialize', 'CloudItemViewHolder$1.<init>'))
sup(('CloudItemViewHolder$1.onClick', 'ListItemClickedEvent.<init>'))

# ---- UNREACHABLE (no caller in the source root; grep A1-A4 and auto_calls.json, see label_122.grep.txt)

UNREACHABLE['CloudItemViewHolder.<init>'] = ('no_trigger_in_app',
    'no caller: the class name occurs only in its own file (grep A1), and no auto_calls.json record has the constructor as dst; its outgoing record to initialize is cut above',
    'sync/CloudItemViewHolder.java:36-40; label_122.grep.txt A1, B',
    'SOURCE')

UNREACHABLE['CloudItemViewHolder.initialize'] = ('no_trigger_in_app',
    'called only from the unreachable constructor (auto CALL, line 39); the click listener it registers is never set up; its outgoing record to $1.<init> is cut above',
    'sync/CloudItemViewHolder.java:47-57; label_122.grep.txt A1, B',
    'SOURCE')

UNREACHABLE['CloudItemViewHolder$1.<init>'] = ('no_trigger_in_app',
    'created only by CloudItemViewHolder.initialize (auto CALL, line 49), which is unreachable',
    'sync/CloudItemViewHolder.java:49-54; label_122.grep.txt A1, B',
    'SOURCE')

UNREACHABLE['CloudItemViewHolder$1.onClick'] = ('no_trigger_in_app',
    'view click listener set only by the unreachable initialize; no auto_calls.json record has it as dst; its CALL to ListItemClickedEvent.<init> is cut above (ListItemClickedEvent.<init> stays UNREACHABLE, label_033; its other caller is batch 050)',
    'sync/CloudItemViewHolder.java:50-53; label_122.grep.txt A1, B',
    'SOURCE')

UNREACHABLE['CloudStorageProviderEnum.<clinit>'] = ('no_trigger_in_app',
    'the enum name occurs only in its declaring file (grep A2), so no code path initialises the class; no auto_calls.json record has it as dst',
    'sync/CloudStorageProviderEnum.java:23-28; label_122.grep.txt A2, B',
    'SOURCE')

UNREACHABLE['CloudStorageProviderEnum.contains'] = ('no_trigger_in_app',
    'static helper with no caller: the enum name occurs only in its declaring file (grep A2), and no auto_calls.json calls record has contains as dst',
    'sync/CloudStorageProviderEnum.java:30-35; label_122.grep.txt A2, B',
    'SOURCE')

UNREACHABLE['SyncCommon.<init>'] = ('no_trigger_in_app',
    'no caller: the class name and getIntentForOpenDatabase occur only in SyncCommon.java (grep A3), so there is no subclass or instance; no auto_calls.json record has it as dst',
    'sync/SyncCommon.java:31; label_122.grep.txt A3, B',
    'SOURCE')

UNREACHABLE['SyncCommon.getIntentForOpenDatabase'] = ('no_trigger_in_app',
    'no caller in the source root (grep A3) and no auto_calls.json record has it as dst; its only app target MainActivity is reached only through this method, so no INTENT edge is written',
    'sync/SyncCommon.java:32-38; label_122.grep.txt A3, B',
    'SOURCE')

UNREACHABLE['SyncConstants.<init>'] = ('no_trigger_in_app',
    'no instance is created (grep A4 finds no new SyncConstants and no SyncConstants()); the class holds compile-time constants only; no auto_calls.json record has it as dst',
    'sync/SyncConstants.java:22; label_122.grep.txt A4, B',
    'SOURCE')

# ---- part 120 (2026-10-29)
# ================================================================== batch 120 (label_120): SecuritySettingsFragment (6 methods + 3 listeners x 2 = 12), SettingsActivity (4), SettingsActivity_MembersInjector (5), SettingsBase (18)
# Result: 34 REACHABLE, 5 UNREACHABLE, 0 INCOMPLETE (rows and printed lines: graphs/MMEX/parts/label_120.md). Grep evidence: graphs/MMEX/parts/label_120.grep.txt.
# Routes: SecuritySettingsActivity (batch 119) hosts SecuritySettingsFragment and owns the ENTERS edge to S_SECURITY_SETTINGS; the three listeners start PasscodeActivity, whose setResult returns to onActivityResult (RESULT edge written here). SettingsActivity is started by SettingsFragment$1 (batch 121), MainActivity.onDrawerMenuAndOptionMenuSelected and HomeFragment$2.onClick (INTENT edges written here); its settings-list branch is the page S_SETTINGS defined here.
# This file writes:
#   - SCREENS for S_SETTINGS (no part defines a settings-list page yet; batch 121 owns SettingsFragment and should reuse this key),
#   - INTENT edges into SettingsActivity.<init> (dst owned here, D1),
#   - LIFECYCLE edges for the fragment chain and the activity, GUI edges from S_SECURITY_SETTINGS, one RESULT edge, ENTERS from SettingsActivity.onCreate,
#   - 5 UNREACHABLE entries and 25 sup pairs cutting the outgoing auto records of the 5 unreachable methods (D14).
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).

SCREENS.update({
    'S_SETTINGS': 'Settings list screen (SettingsActivity hosting SettingsFragment): the main settings preference list opened from the drawer menu and the home welcome view, with one entry per settings section (general, look and feel, behaviour, investment, budget, security, database); the per-database entry opens the same activity with PerDatabaseFragment instead (S_PER_DATABASE_SETTINGS)',
})

# ---- SecuritySettingsFragment: fragment lifecycle (framework calls; INFERRED androidx Fragment lifecycle, library source not read)

e('SecuritySettingsFragment.<init>', 'SecuritySettingsFragment.onCreate', 'LIFECYCLE',
  'SecuritySettingsActivity.onCreate calls setSettingFragment(new SecuritySettingsFragment()) (auto CALL, line 28); the fragment is committed and the FragmentManager then calls onCreate (INFERRED androidx Fragment lifecycle)',
  evidence='SRC settings/SecuritySettingsActivity.java:8-30; SRC settings/BaseSettingsFragmentActivity.java:70-92; SRC settings/SecuritySettingsFragment.java:37-86')

e('SecuritySettingsFragment.onCreate', 'SecuritySettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'the framework calls onCreatePreferences after onCreate (INFERRED: inherited PreferenceFragmentCompat code, not read); the method body is empty',
  evidence='SRC settings/SecuritySettingsFragment.java:48-91')

e('SecuritySettingsFragment.onCreatePreferences', 'SecuritySettingsFragment.onResume', 'LIFECYCLE',
  'the framework calls onResume after the preference view is created (INFERRED androidx Fragment lifecycle); onResume enables or disables the three passcode preferences',
  evidence='SRC settings/SecuritySettingsFragment.java:89-166')

# ---- SecuritySettingsFragment: the three passcode preferences (D9: the fragment uses its host screen S_SECURITY_SETTINGS)

e('S_SECURITY_SETTINGS', 'SecuritySettingsFragment$1.onPreferenceClick', 'GUI',
  'the user taps the active passcode preference: the listener starts PasscodeActivity to enter a new passcode (startActivityPasscode, auto CALL line 60)',
  gui=['Open Settings > Security and tap the active passcode preference'],
  evidence='SRC settings/SecuritySettingsFragment.java:55-63 (listener created at 55; onPreferenceClick at 57-62, startActivityPasscode call at 60)')

e('S_SECURITY_SETTINGS', 'SecuritySettingsFragment$2.onPreferenceClick', 'GUI',
  'the user taps the edit passcode preference: the listener starts PasscodeActivity to enter the previous passcode (startActivityPasscode, auto CALL line 71)',
  gui=['Open Settings > Security and tap the edit passcode preference'],
  evidence='SRC settings/SecuritySettingsFragment.java:66-74 (listener created at 66; onPreferenceClick at 68-73)')

e('S_SECURITY_SETTINGS', 'SecuritySettingsFragment$3.onPreferenceClick', 'GUI',
  'the user taps the disable passcode preference: the listener starts PasscodeActivity to enter the current passcode before clearing it (startActivityPasscode, auto CALL line 82)',
  gui=['Open Settings > Security and tap the disable passcode preference'],
  evidence='SRC settings/SecuritySettingsFragment.java:77-85 (listener created at 77; onPreferenceClick at 79-84)')

# ---- SecuritySettingsFragment: result of PasscodeActivity (RESULT; dst owned here)

e('PasscodeActivity$1.onClick', 'SecuritySettingsFragment.onActivityResult', 'RESULT',
  'PasscodeActivity sets RESULT_OK with the entered passcode (setResult, line 125) and the framework delivers the result to the fragment that called startActivityForResult (startActivityPasscode, line 174)',
  evidence='SRC com/money/manager/ex/PasscodeActivity.java:98-128 (onClick of PasscodeActivity$1 starts at line 101; setResult at 125); SRC settings/SecuritySettingsFragment.java:94-175')

# ---- SettingsActivity: the settings list activity (dst owned here, D1; the sources belong to batches 121, MainActivity and HomeFragment)

e('SettingsFragment$1.onPreferenceClick', 'SettingsActivity.<init>', 'INTENT',
  'the per-database preference of the settings list starts SettingsActivity with the PerDatabaseFragment extra (EXTRA_FRAGMENT), so showFragment shows PerDatabaseFragment',
  gui=['Open Settings and tap the per-database preference'],
  evidence='SRC settings/SettingsFragment.java:56-64 (anonymous class $1 is created at line 59: auto_calls SettingsFragment.onCreate -> SettingsFragment$1.<init>; intent at line 62)')

e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'SettingsActivity.<init>', 'INTENT',
  'the Settings drawer item starts SettingsActivity without the extra, so showFragment shows SettingsFragment (the settings list)',
  gui=['Open the navigation drawer and choose Settings'],
  evidence='SRC home/MainActivity.java:665 (startActivity(new Intent(MainActivity.this, SettingsActivity.class)) in onDrawerMenuAndOptionMenuSelected, method at 589)')

e('HomeFragment$2.onClick', 'SettingsActivity.<init>', 'INTENT',
  'the home screen welcome view control starts SettingsActivity without the extra, so the settings list is shown',
  gui=['Home screen welcome view: tap the control that opens Settings'],
  evidence='SRC home/HomeFragment.java:595-600 (anonymous class $2 is created at line 596 in createWelcomeView: auto_calls HomeFragment.createWelcomeView -> HomeFragment$2.<init>; intent at line 599)')

e('SettingsActivity.<init>', 'SettingsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (the same activity pattern as label_004 AboutActivity)',
  evidence='SRC settings/SettingsActivity.java:31-46; FW-SRC core/java/android/app/ActivityThread.java:2724-2731 (as cited in label_004, not read in this batch)')

e('SettingsActivity.onCreate', 'SettingsActivity.onResume', 'LIFECYCLE',
  'the framework calls onResume after onCreate (INFERRED androidx activity lifecycle); onResume sets the title to R.string.settings',
  evidence='SRC settings/SettingsActivity.java:40-53')

e('SettingsActivity.onCreate', 'S_SETTINGS', 'ENTERS',
  'the settings list is shown: onCreate calls showFragment, which uses SettingsFragment unless the PerDatabaseFragment extra is present (the per-database branch is labelled in batch 119 as S_PER_DATABASE_SETTINGS)',
  evidence='SRC settings/SettingsActivity.java:40-72 (default SettingsFragment at lines 67-69)')

# ---- UNREACHABLE (each with a grep section in label_120.grep.txt)

UNREACHABLE['SettingsBase.get(String,int)'] = ('no_trigger_in_app',
    'no caller: no auto_calls.json record has SettingsBase.get(String,int) as dst (with or without a receiver variant); no call in the settings package passes a String key with an int default (AppSettings.java:104 is get(R.string.pref_sort_payee, 0), the Integer overload); its outgoing records (to each subclass getPreferences, line 129) are cut by sup below',
    'settings/SettingsBase.java:128-130; label_120.grep.txt section B',
    'SOURCE')

UNREACHABLE['SettingsBase.getBooleanSetting(String)'] = ('no_trigger_in_app',
    'no caller: no auto_calls.json record has the one-argument getBooleanSetting as dst; its only source reference is its own body calling the two-argument form (SettingsBase.java:107); every other call in the source root uses the two-argument form (SettingsBase.java:103; LookAndFeelSettings.java:52, 120)',
    'settings/SettingsBase.java:106-108; label_120.grep.txt section A',
    'SOURCE')

UNREACHABLE['SettingsActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
    'generated Dagger constructor: its only caller is SettingsActivity_MembersInjector.create (auto record, line 27), and create has no caller (see create); no app code builds the injector',
    'generated SettingsActivity_MembersInjector.java:27 (auto record); label_120.grep.txt section C',
    'SOURCE')

UNREACHABLE['SettingsActivity_MembersInjector.create'] = ('no_trigger_in_app',
    'generated Dagger factory: no auto_calls.json record has create as dst; DaggerMmxComponent.injectSettingsActivity (auto records at DaggerMmxComponent.java:433 and 435) calls the static helpers injectAppSettingsLazy and injectCoreLazy directly, so no MembersInjector instance is built; its outgoing record to <init> is cut by sup below',
    'generated SettingsActivity_MembersInjector.java:26-27 (auto record); DaggerMmxComponent.java:433-435 (auto records); label_120.grep.txt section C',
    'SOURCE')

UNREACHABLE['SettingsActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'generated MembersInjector method: no auto_calls.json record has injectMembers as dst, and only an injector instance (built by create, which has no caller) could call it through the interface; its outgoing records (to injectAppSettingsLazy at line 32 and injectCoreLazy at line 33) are cut by sup below',
    'generated SettingsActivity_MembersInjector.java:31-33 (auto records); label_120.grep.txt section C',
    'SOURCE')

# ---- sup pairs (D14): outgoing auto records of the five UNREACHABLE methods, one per exact (src, dst) in auto_calls.json

sup(('SettingsActivity_MembersInjector.create', 'SettingsActivity_MembersInjector.<init>'))
sup(('SettingsActivity_MembersInjector.injectMembers', 'SettingsActivity_MembersInjector.injectAppSettingsLazy'))
sup(('SettingsActivity_MembersInjector.injectMembers', 'SettingsActivity_MembersInjector.injectCoreLazy'))
sup(('SettingsBase.get(String,int)', 'AppSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'BehaviourSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'BudgetSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'GeneralSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'LookAndFeelSettings.getPreferences'))
sup(('SettingsBase.get(String,int)', 'SyncPreferences.getPreferences'))
sup(('SettingsBase.get(String,int)@AppSettings', 'AppSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@BehaviourSettings', 'BehaviourSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@BudgetSettings', 'BudgetSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@GeneralSettings', 'GeneralSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@InvestmentSettings', 'InvestmentSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@LookAndFeelSettings', 'LookAndFeelSettings.getPreferences'))
sup(('SettingsBase.get(String,int)@SyncPreferences', 'SyncPreferences.getPreferences'))
sup(('SettingsBase.getBooleanSetting(String)', 'SettingsBase.getBooleanSetting(String,boolean)'))
sup(('SettingsBase.getBooleanSetting(String)@AppSettings', 'SettingsBase.getBooleanSetting(String,boolean)@AppSettings'))
sup(('SettingsBase.getBooleanSetting(String)@BehaviourSettings', 'SettingsBase.getBooleanSetting(String,boolean)@BehaviourSettings'))
sup(('SettingsBase.getBooleanSetting(String)@BudgetSettings', 'SettingsBase.getBooleanSetting(String,boolean)@BudgetSettings'))
sup(('SettingsBase.getBooleanSetting(String)@GeneralSettings', 'SettingsBase.getBooleanSetting(String,boolean)@GeneralSettings'))
sup(('SettingsBase.getBooleanSetting(String)@InvestmentSettings', 'SettingsBase.getBooleanSetting(String,boolean)@InvestmentSettings'))
sup(('SettingsBase.getBooleanSetting(String)@LookAndFeelSettings', 'SettingsBase.getBooleanSetting(String,boolean)@LookAndFeelSettings'))
sup(('SettingsBase.getBooleanSetting(String)@SyncPreferences', 'SettingsBase.getBooleanSetting(String,boolean)@SyncPreferences'))

# ---- part 121 (2026-10-29)
# ================================================================== batch 121 (label_121): SettingsFragment (6 methods), SettingsFragment$1 to $10 (20), SyncPreferences (13); 39 methods
# Result: 38 REACHABLE, 1 UNREACHABLE, 0 INCOMPLETE (rows: graphs/MMEX/parts/label_121.md). Grep evidence: graphs/MMEX/parts/label_121.grep.txt.
# This file writes:
#   - LIFECYCLE from BaseSettingsFragmentActivity.setSettingFragment to SettingsFragment.onCreate (fragment commit; the pattern of label_115),
#   - LIFECYCLE from SettingsFragment.onCreate to onCreatePreferences (framework dispatch through PreferenceFragmentCompat.onCreate),
#   - RESULT from SettingsFragment$10.onPreferenceClick to SettingsFragment.onActivityResult (startActivityForResult at line 230),
#   - 10 GUI edges from S_SETTINGS to SettingsFragment$1..$10.onPreferenceClick (D6),
#   - 1 UNREACHABLE entry (SyncPreferences.clear) and 1 sup pair (D14).
# S_SETTINGS is not redefined here: label_120.py line 12 defines it (D9). No S_SETTINGS SCREENS entry is written by this file.
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).
# INTENT edges from the listeners to activities are not written here: their destinations belong to other batches (D1).

# ---- the settings list fragment: setSettingFragment commits it, the FragmentManager runs onCreate, then onCreatePreferences

e('SettingsFragment.<init>', 'SettingsFragment.onCreate', 'LIFECYCLE',
  'the settings list fragment is committed by SettingsActivity.showFragment (line 71); the FragmentManager then runs onCreate of SettingsFragment',
  evidence='SRC settings/BaseSettingsFragmentActivity.java:71-92 (tx.replace 78, tx.commit 91); SRC settings/SettingsActivity.java:68-71 (new SettingsFragment at 68, setSettingFragment at 71); INFERRED androidx FragmentManager (library not in the dataset; source not read)')

e('SettingsFragment.onCreate', 'SettingsFragment.onCreatePreferences', 'LIFECYCLE',
  'super.onCreate (line 48) is PreferenceFragmentCompat.onCreate, which calls the overridden onCreatePreferences (framework dispatch; INFERRED from the framework contract)',
  evidence='SRC settings/SettingsFragment.java:48 (super.onCreate), 195-198 (empty body); auto_calls.json framework_calls SettingsFragment.onCreate lists PreferenceFragmentCompat.onCreate')

# ---- the General settings listener returns its result to onActivityResult

e('SettingsFragment$10.onPreferenceClick', 'SettingsFragment.onActivityResult', 'RESULT',
  'startActivityForResult (line 230) starts GeneralSettingsActivity with REQUEST_GENERAL_PREFERENCES; the framework delivers the result to onActivityResult, which calls getActivity().recreate() (line 206)',
  evidence='SRC settings/SettingsFragment.java:226-232 (start at 230), 200-208 (onActivityResult; recreate at 206); precedent DatabaseSettingsFragment.requestBackup -> onActivityResult (graph_def.py line 10378)')

# ---- GUI edges from the settings list page (S_SETTINGS, label_120.py line 12) to each listener (D6)

e('S_SETTINGS', 'SettingsFragment$1.onPreferenceClick', 'GUI',
  'the user taps the per-database preference (R.string.pref_per_database, line 54): the listener starts SettingsActivity with EXTRA_FRAGMENT = PerDatabaseFragment (lines 62-64); the INTENT edge to SettingsActivity.<init> is batch 120\'s',
  evidence='SRC settings/SettingsFragment.java:59-67 (listener set at 59, onPreferenceClick 61, putExtra 63, startActivity 64)')

e('S_SETTINGS', 'SettingsFragment$2.onPreferenceClick', 'GUI',
  'the user taps the look and feel preference (PreferenceConstants.PREF_LOOK_FEEL, line 70): the listener starts LookFeelSettingsActivity (line 77)',
  evidence='SRC settings/SettingsFragment.java:70-80 (listener set at 74, onPreferenceClick 76, startActivity 77)')

e('S_SETTINGS', 'SettingsFragment$3.onPreferenceClick', 'GUI',
  'the user taps the behaviour preference (R.string.pref_behaviour, line 83): the listener starts BehaviourSettingsActivity (line 90)',
  evidence='SRC settings/SettingsFragment.java:83-93 (listener set at 87, onPreferenceClick 89, startActivity 90)')

e('S_SETTINGS', 'SettingsFragment$4.onPreferenceClick', 'GUI',
  'the user taps the investment preference (R.string.pref_investment, line 96): the listener starts InvestmentSettingsActivity (line 103)',
  evidence='SRC settings/SettingsFragment.java:96-106 (listener set at 100, onPreferenceClick 102, startActivity 103)')

e('S_SETTINGS', 'SettingsFragment$5.onPreferenceClick', 'GUI',
  'the user taps the budget preference (R.string.pref_budget, line 109): the listener starts BudgetSettingsActivity (line 116)',
  evidence='SRC settings/SettingsFragment.java:109-119 (listener set at 113, onPreferenceClick 115, startActivity 116)')

e('S_SETTINGS', 'SettingsFragment$6.onPreferenceClick', 'GUI',
  'the user taps the security preference (PreferenceConstants.PREF_SECURITY, line 122): the listener starts SecuritySettingsActivity (line 129)',
  evidence='SRC settings/SettingsFragment.java:122-132 (listener set at 126, onPreferenceClick 128, startActivity 129)')

e('S_SETTINGS', 'SettingsFragment$7.onPreferenceClick', 'GUI',
  'the user taps the database preference (PreferenceConstants.PREF_DATABASE, line 135): the listener starts DatabaseSettingsActivity (line 142)',
  evidence='SRC settings/SettingsFragment.java:135-145 (listener set at 139, onPreferenceClick 141, startActivity 142)')

e('S_SETTINGS', 'SettingsFragment$8.onPreferenceClick', 'GUI',
  'the user taps the synchronisation preference (R.string.pref_synchronization, line 149): the listener starts SyncPreferencesActivity (line 156); the INTENT edge is batch 122\'s',
  evidence='SRC settings/SettingsFragment.java:149-160 (listener set at 153, onPreferenceClick 155, startActivity 156)')

e('S_SETTINGS', 'SettingsFragment$9.onPreferenceClick', 'GUI',
  'the user taps the version preference (PreferenceConstants.PREF_VERSION_NAME, line 162): the listener starts AboutActivity (line 170)',
  evidence='SRC settings/SettingsFragment.java:162-174 (listener set at 166, onPreferenceClick 169, startActivity 170)')

e('S_SETTINGS', 'SettingsFragment$10.onPreferenceClick', 'GUI',
  'the user taps the general preference (PreferenceConstants.PREF_GENERAL, line 220): the listener starts GeneralSettingsActivity with startActivityForResult (line 230); the INTENT edge is batch 116\'s',
  evidence='SRC settings/SettingsFragment.java:217-233 (listener set at 226, onPreferenceClick 228, startActivityForResult 230)')

# ---- UNREACHABLE (D14 cut of its one outgoing auto record)

UNREACHABLE['SyncPreferences.clear'] = ('no_trigger_in_app',
    'no live caller: its only caller is SyncManager.resetPreferences (SyncManager.java:257, getPreferences().clear()); resetPreferences has no live caller: its only other mention in the source root is the reset listener at SyncPreferenceFragment.java:262, which is commented out, and no auto_calls.json record has it as dst; see label_121.grep.txt section A',
    'settings/SyncPreferences.java:40-42; sync/SyncManager.java:256-258; sync/SyncPreferenceFragment.java:252-276; label_121.grep.txt section A',
    'SOURCE')

sup(('SyncPreferences.clear', 'SyncPreferences.getPreferences'))  # clear has no caller; its one outgoing record (SyncPreferences.java:41) is cut (D14)
sup(('SyncManager.resetPreferences', 'SyncPreferences.clear'))  # resetPreferences has no live caller (D14); its call to clear (SyncManager.java:257) is cut

# ---- part 124 (2026-10-29)
# ================================================================== batch 124 (label_124): SyncNotificationFactory (8 methods); 8 methods
# Result: 3 REACHABLE, 5 UNREACHABLE (rows: graphs/MMEX/parts/label_124.md). Grep evidence: graphs/MMEX/parts/label_124.grep.txt.
# This file writes:
#   - 5 UNREACHABLE entries (kind no_trigger_in_app): the getters with no live caller,
#   - 8 sup cuts (D14) for the auto CALL records from those five UNREACHABLE getters to getContext and NotificationUtils.createNotificationChannel,
#   - 2 sup cuts (D20 pattern) for the auto CALL records from SyncService.showNotificationUploading and showNotificationUploadComplete into the two UNREACHABLE upload getters (the callers are in batch 126; the target owner cuts here).
# No edge is written. Every REACHABLE route is made of auto CALL records already in auto_calls.json (D7), so the build finds it (D4).
# Batch 126 (SyncService) must still: label SyncService.showNotificationUploading and SyncService.showNotificationUploadComplete UNREACHABLE (no caller in the source root),
#   and cut its own auto records into <init> from them (SyncService.java:252 and 168) (D14). Those two cuts are not written here (ownership, D1).

# ---- UNREACHABLE: the five getters with no live caller

UNREACHABLE['SyncNotificationFactory.getNotificationBuilderProgress'] = ('no_trigger_in_app',
    'no caller anywhere in the source root: the name occurs only at its declaration (grep A2); no auto_calls.json record has it as src or dst (grep B1); no class file other than SyncNotificationFactory.class names it (grep C1); it has no outgoing auto record',
    'sync/SyncNotificationFactory.java:145-150; label_124.grep.txt A2, B1, C1',
    'SOURCE')

UNREACHABLE['SyncNotificationFactory.getNotificationDownloadComplete'] = ('no_trigger_in_app',
    'no caller: the name occurs only at its declaration (grep A2); SyncService has no download-complete notification method and no auto record has it as dst (grep B1); its two outgoing records (getContext line 87, NotificationUtils.createNotificationChannel line 69) are cut below (D14)',
    'sync/SyncNotificationFactory.java:67-89; label_124.grep.txt A2, B1, C1',
    'SOURCE')

UNREACHABLE['SyncNotificationFactory.getNotificationForDownload'] = ('no_trigger_in_app',
    'no caller: the name occurs only at its declaration (grep A2); SyncService has no download notification method and no auto record has it as dst (grep B1); its two outgoing records (getContext line 59, NotificationUtils.createNotificationChannel line 50) are cut below (D14)',
    'sync/SyncNotificationFactory.java:48-62; label_124.grep.txt A2, B1, C1',
    'SOURCE')

UNREACHABLE['SyncNotificationFactory.getNotificationUploading'] = ('no_trigger_in_app',
    'its only caller is SyncService.showNotificationUploading (SyncService.java:251, call at 253, private). That method has no caller in the source root (grep A2: the name occurs only at line 251), so the getter has no live route; its incoming record (SyncService.java:253) is cut below (D20 pattern); its outgoing records (getContext line 105, NotificationUtils.createNotificationChannel line 96) are cut below (D14)',
    'sync/SyncNotificationFactory.java:94-108; sync/SyncService.java:251-253; label_124.grep.txt A2, B2, B3, C2',
    'SOURCE')

UNREACHABLE['SyncNotificationFactory.getNotificationUploadComplete'] = ('no_trigger_in_app',
    'its only caller is SyncService.showNotificationUploadComplete (SyncService.java:155, call at 168-169, private). That method has no caller in the source root (grep A2: the name occurs only at line 155), so the getter has no live route; its incoming record (SyncService.java:169) is cut below (D20 pattern); its outgoing records (getContext line 132, NotificationUtils.createNotificationChannel line 120) are cut below (D14)',
    'sync/SyncNotificationFactory.java:113-135; sync/SyncService.java:155-172; label_124.grep.txt A2, B2, B3, C2',
    'SOURCE')

# ---- D14: the outgoing auto CALL records of the five UNREACHABLE getters (caller unreachable in this batch)

sup(('SyncNotificationFactory.getNotificationForDownload', 'SyncNotificationFactory.getContext'))  # caller UNREACHABLE (D14); auto record line 59
sup(('SyncNotificationFactory.getNotificationForDownload', 'NotificationUtils.createNotificationChannel'))  # caller UNREACHABLE (D14); auto record line 50
sup(('SyncNotificationFactory.getNotificationDownloadComplete', 'SyncNotificationFactory.getContext'))  # caller UNREACHABLE (D14); auto record line 87
sup(('SyncNotificationFactory.getNotificationDownloadComplete', 'NotificationUtils.createNotificationChannel'))  # caller UNREACHABLE (D14); auto record line 69
sup(('SyncNotificationFactory.getNotificationUploading', 'SyncNotificationFactory.getContext'))  # caller UNREACHABLE (D14); auto record line 105
sup(('SyncNotificationFactory.getNotificationUploading', 'NotificationUtils.createNotificationChannel'))  # caller UNREACHABLE (D14); auto record line 96
sup(('SyncNotificationFactory.getNotificationUploadComplete', 'SyncNotificationFactory.getContext'))  # caller UNREACHABLE (D14); auto record line 132
sup(('SyncNotificationFactory.getNotificationUploadComplete', 'NotificationUtils.createNotificationChannel'))  # caller UNREACHABLE (D14); auto record line 120

# ---- D20 pattern: the incoming auto records of the two UNREACHABLE upload getters (their callers are batch 126's and have no caller themselves)

sup(('SyncService.showNotificationUploading', 'SyncNotificationFactory.getNotificationUploading'))  # SyncService.java:253; target UNREACHABLE, no caller of showNotificationUploading (grep A2)
sup(('SyncService.showNotificationUploadComplete', 'SyncNotificationFactory.getNotificationUploadComplete'))  # SyncService.java:169; target UNREACHABLE, no caller of showNotificationUploadComplete (grep A2)

# ---- part 125 (2026-10-29)
# ================================================================== batch 125 (label_125): SyncPreferenceFragment (15 methods), SyncPreferenceFragment$1 to $10 (20), SyncPreferenceFragment_MembersInjector (4), SyncPreferencesViewHolder (1); 40 methods
# Result: 24 REACHABLE, 16 UNREACHABLE, 0 INCOMPLETE (rows: graphs/MMEX/parts/label_125.md). Grep evidence: graphs/MMEX/parts/label_125.grep.txt.
# This file writes:
#   - LIFECYCLE from SyncPreferenceFragment.<init> to onCreate (D21: the fragment's own constructor, created by SyncPreferencesActivity.onCreate),
#   - LIFECYCLE from onCreate to onCreatePreferences (framework dispatch through PreferenceFragmentCompat.onCreate) and to onStart,
#   - LIFECYCLE from onStart to onStop, REGISTER from onStart to onEvent (EventBus.register at line 107),
#   - ASYNC from SyncServiceMessageHandler.handleMessage to onEvent (D1: this batch owns the destination; batch 126 owns the source and must not write it again),
#   - 6 GUI edges from S_SYNC_SETTINGS (batch 122 page) to the six preference listeners $3 to $8 (D6),
#   - 16 UNREACHABLE entries and 25 sup cuts (D14): every auto CALL record whose caller is UNREACHABLE in this batch.
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).
# The route into SyncPreferencesActivity.onCreate and the ENTERS edge to S_SYNC_SETTINGS are batch 122's.
# The injection chain DaggerMmxComponent.inject -> injectSyncPreferenceFragment -> injectMDatabases is batches 043 and 044's (auto CALL records).

# ---- the fragment lifecycle: the activity creates the fragment, the FragmentManager runs onCreate, then onStart

e('SyncPreferenceFragment.<init>', 'SyncPreferenceFragment.onCreate', 'LIFECYCLE',
  'the sync settings fragment is created by SyncPreferencesActivity.onCreate and committed by setSettingFragment; the FragmentManager then runs onCreate of SyncPreferenceFragment (same pattern as label_121 SettingsFragment.<init>)',
  evidence='SRC settings/SyncPreferencesActivity.java:33-38 (new SyncPreferenceFragment and setSettingFragment at 37); SRC sync/SyncPreferenceFragment.java:66-68, 75-80; INFERRED androidx FragmentManager (library source not read); D21')

e('SyncPreferenceFragment.onCreate', 'SyncPreferenceFragment.onCreatePreferences', 'LIFECYCLE',
  'super.onCreate (line 77) is PreferenceFragmentCompat.onCreate, which calls the overridden onCreatePreferences (framework dispatch; INFERRED from the framework contract)',
  evidence='SRC sync/SyncPreferenceFragment.java:76-80 (super.onCreate at 77), 82-91; auto_calls.json framework_calls, near line 72240: SyncPreferenceFragment.onCreate lists PreferenceFragmentCompat.onCreate')

e('SyncPreferenceFragment.onCreate', 'SyncPreferenceFragment.onStart', 'LIFECYCLE',
  'the framework starts the fragment after onCreate and the view creation (INFERRED androidx Fragment lifecycle; the pattern of label_003 PasscodeActivity.onCreate to onStart)',
  evidence='SRC sync/SyncPreferenceFragment.java:75-80, 102-108; INFERRED androidx Fragment lifecycle (library source not read)')

e('SyncPreferenceFragment.onStart', 'SyncPreferenceFragment.onStop', 'LIFECYCLE',
  'the framework stops the started fragment (INFERRED androidx Fragment lifecycle; the pattern of label_010 AccountTransactionListFragment.onResume to onStop)',
  evidence='SRC sync/SyncPreferenceFragment.java:102-115; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- EventBus: the fragment subscribes in onStart; the download-complete event reaches onEvent

e('SyncPreferenceFragment.onStart', 'SyncPreferenceFragment.onEvent', 'REGISTER',
  'EventBus.getDefault().register(this) makes onEvent a subscriber while the fragment is started; onStop unregisters it (line 114)',
  evidence='SRC sync/SyncPreferenceFragment.java:102-108 (register at 107), 110-115 (unregister at 114), 120-121 (@Subscribe onEvent(DbFileDownloadedEvent)); precedent label_010 AccountTransactionListFragment.onStart -> onEvent (REGISTER)')

e('SyncServiceMessageHandler.handleMessage', 'SyncPreferenceFragment.onEvent', 'ASYNC',
  'the sync service sends DOWNLOAD_COMPLETE to the handler (case at line 84) and the handler posts a new DbFileDownloadedEvent to EventBus (line 89); EventBus delivers it to the registered subscriber onEvent. The cloud download is the one forceDownload starts (the Download preference, line 236)',
  env=env_text('the cloud download that the Download preference starts (forceDownload) completes in the sync service; it needs the network and the cloud storage', ('network',)),
  evidence='SRC sync/SyncServiceMessageHandler.java:61 (handleMessage), 84-89 (post at 89); SRC sync/SyncPreferenceFragment.java:120-123; precedent label_032 DebugTree.log -> MmxBaseFragmentActivity.onEvent (ASYNC); the source handleMessage is batch 126 (not merged yet): this route is open until batch 126 merges (D4, D8)')

# ---- GUI edges from the synchronization settings page (S_SYNC_SETTINGS, label_122.py) to each preference listener (D6)

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$3.onPreferenceChange', 'GUI',
  'the user switches Synchronisation on or off (R.string.pref_sync_enabled, the first preference): the listener calls SyncManager.setEnabled and starts or stops the heartbeat',
  evidence='SRC sync/SyncPreferenceFragment.java:180-193 (listener set at 180, onPreferenceChange 182, setEnabled 185); SRC res/xml/preferences_sync.xml:21-23 (SwitchPreferenceCompat, key pref_sync_enabled)')

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$4.onPreferenceClick', 'GUI',
  'the user taps Remote file (R.string.pref_remote_file): the listener returns false, and the file-picker start (lines 201-202) is commented out, so the tap has no further route',
  evidence='SRC sync/SyncPreferenceFragment.java:197-206 (listener set at 197, onPreferenceClick 199, picker lines 201-202 commented, return at 204); SRC res/xml/preferences_sync.xml:39-42 (Preference, key pref_remote_file)')

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$5.onPreferenceChange', 'GUI',
  'the user chooses a sync interval (R.string.pref_sync_interval, ListPreference): the listener sets the interval, resets the alarm and starts the heartbeat when the interval is above 0',
  evidence='SRC sync/SyncPreferenceFragment.java:209-229 (listener set at 209, onPreferenceChange 211, setSyncInterval 215, startSyncServiceHeartbeat 225); SRC res/xml/preferences_sync.xml:28-34 (ListPreference, key pref_sync_interval)')

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$6.onPreferenceClick', 'GUI',
  'the user taps Download (R.string.pref_sync_download): the listener calls forceDownload (line 236) and returns true',
  evidence='SRC sync/SyncPreferenceFragment.java:233-239 (listener set at 233, onPreferenceClick 235, forceDownload 236); SRC res/xml/preferences_sync.xml:46-52 (PreferenceScreen, key pref_sync_download)')

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$7.onPreferenceClick', 'GUI',
  'the user taps Upload (R.string.pref_sync_upload): the listener calls forceUpload (line 246)',
  evidence='SRC sync/SyncPreferenceFragment.java:243-249 (listener set at 243, onPreferenceClick 245, forceUpload 246); SRC res/xml/preferences_sync.xml:53-59 (PreferenceScreen, key pref_sync_upload)')

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$8.onPreferenceClick', 'GUI',
  'the user taps Reset preferences (R.string.pref_reset_preferences): the listener only gets the SyncManager (line 255) and returns false; the logout and reset calls (lines 256-273) are commented out',
  evidence='SRC sync/SyncPreferenceFragment.java:252-276 (listener set at 252, getSyncManager 255, commented calls 256-273, return at 274); SRC res/xml/preferences_sync.xml:79-81 (Preference, key pref_reset_preferences)')

# ---- UNREACHABLE entries (grep evidence in label_125.grep.txt)

UNREACHABLE['SyncPreferenceFragment.onActivityResult'] = ('no_trigger_in_app',
    'Fragment.onActivityResult runs only for a request this fragment started with startActivityForResult. The only start in this fragment that sends REQUEST_REMOTE_FILE (1) is commented out (line 202), so no result with that code arrives; no other call site exists in the source root (grep B1, C1)',
    'sync/SyncPreferenceFragment.java:94-100, 201-202; label_125.grep.txt sections A, C',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment.handleFileSelection'] = ('no_trigger_in_app',
    'private; its only caller is onActivityResult (line 98), which has no live caller. Its auto CALL records (binaryDialog, startSyncServiceHeartbeat, getSyncManager, the two anonymous listeners) are cut below (D14)',
    'sync/SyncPreferenceFragment.java:130-163 (call at 98); label_125.grep.txt sections A, B',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment.checkIfLocalFileExistsAndDownload'] = ('no_trigger_in_app',
    'private; its only callers are the Action1 listener $1.call (line 159), which belongs to handleFileSelection (unreachable), and no other call site (grep B2). Its outgoing auto CALL records are cut below (D14)',
    'sync/SyncPreferenceFragment.java:279-305 (call at 159); label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment.getDatabases'] = ('no_trigger_in_app',
    'private accessor for mDatabases; its only callers are checkIfLocalFileExistsAndDownload (line 280) and saveDatabaseMetadata (line 338); both are unreachable, so getDatabases has no live caller (grep B2, B3)',
    'sync/SyncPreferenceFragment.java:172-174, 280, 338; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$1.<init>'] = ('no_trigger_in_app',
    'created only by handleFileSelection (auto CALL, line 148), which is unreachable; the object is never created',
    'sync/SyncPreferenceFragment.java:148-161; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$1.call'] = ('no_trigger_in_app',
    'the Action1 subscriber of the download confirmation (line 159, calls checkIfLocalFileExistsAndDownload); it runs only when the RxJava chain from handleFileSelection emits, which never starts (RxJava behaviour: INFERRED)',
    'sync/SyncPreferenceFragment.java:155-161 (call at 159); label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$2.<init>'] = ('no_trigger_in_app',
    'created only by handleFileSelection (auto CALL, line 146), which is unreachable',
    'sync/SyncPreferenceFragment.java:148-154; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$2.call'] = ('no_trigger_in_app',
    'the Func1 filter of the download confirmation (returns the user answer); it runs only from the RxJava chain of handleFileSelection, which never starts (INFERRED RxJava behaviour)',
    'sync/SyncPreferenceFragment.java:148-154; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$9.<init>'] = ('no_trigger_in_app',
    'created only by checkIfLocalFileExistsAndDownload (auto CALL, line 287), which is unreachable',
    'sync/SyncPreferenceFragment.java:286-301; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$9.call'] = ('no_trigger_in_app',
    'the Action1 subscriber of the file-exists prompt (line 298, calls forceDownload); it runs only from the RxJava chain built in checkIfLocalFileExistsAndDownload, which never runs (INFERRED RxJava behaviour)',
    'sync/SyncPreferenceFragment.java:294-300 (call at 298); label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$10.<init>'] = ('no_trigger_in_app',
    'created only by checkIfLocalFileExistsAndDownload (auto CALL, line 286), which is unreachable',
    'sync/SyncPreferenceFragment.java:286-293; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$10.call'] = ('no_trigger_in_app',
    'the Func1 filter of the file-exists prompt (returns the user answer); it runs only from the RxJava chain of checkIfLocalFileExistsAndDownload, which never runs (INFERRED RxJava behaviour)',
    'sync/SyncPreferenceFragment.java:287-293; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment.saveDatabaseMetadata'] = ('no_trigger_in_app',
    'private; its only call (line 140) is commented out, and no other reference in the source root calls it (grep B4). The same route is noted dead in batches 075 and 083. Its seven auto CALL records are cut below (D14)',
    'sync/SyncPreferenceFragment.java:140, 326-339; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment_MembersInjector.<init>'] = ('no_trigger_in_app',
    'Dagger-generated constructor; its only caller is create (auto CALL, line 25), which has no caller. DaggerMmxComponent refers to the injector class only through injectMDatabases (grep C2, C3); the generated class is INFERRED (D5, D12)',
    'sync/SyncPreferenceFragment_MembersInjector.class (<init>(Provider) at lines 19-21); label_125.grep.txt sections C, D',
    'INFERRED')

UNREACHABLE['SyncPreferenceFragment_MembersInjector.create'] = ('no_trigger_in_app',
    'Dagger-generated static factory; no caller: DaggerMmxComponent does not reference it (grep C2, C3). Its only outgoing record, to <init>, is cut below (D14)',
    'sync/SyncPreferenceFragment_MembersInjector.class (create(Provider) at line 25); label_125.grep.txt sections C, D',
    'INFERRED')

UNREACHABLE['SyncPreferenceFragment_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'Dagger-generated MembersInjector.injectMembers(SyncPreferenceFragment); no caller: DaggerMmxComponent calls only the static injectMDatabases (grep C2, C3). Its only outgoing record, to injectMDatabases, is cut below (D14); the bridge injectMembers(Object) is not in this batch',
    'sync/SyncPreferenceFragment_MembersInjector.class (injectMembers at lines 30-31); label_125.grep.txt sections C, D',
    'INFERRED')

# ---- sup cuts (D14): every auto CALL record whose caller is UNREACHABLE in this batch. Targets in other batches keep their other callers (grep E).

sup(('SyncPreferenceFragment.onActivityResult', 'SyncPreferenceFragment.handleFileSelection'))  # onActivityResult has no live caller; its call to handleFileSelection (line 98) is cut
sup(('SyncPreferenceFragment.handleFileSelection', 'SyncPreferenceFragment$1.<init>'))  # handleFileSelection is unreachable (line 148)
sup(('SyncPreferenceFragment.handleFileSelection', 'SyncPreferenceFragment$2.<init>'))  # handleFileSelection is unreachable (line 146)
sup(('SyncPreferenceFragment.handleFileSelection', 'UIHelper.binaryDialog(int,int,int,int)'))  # cross-batch (batch 040): the four-argument overload has one other caller, binaryDialog(int,int) in UIHelper.java:86, and batch 040 labels it UNREACHABLE
sup(('SyncPreferenceFragment.handleFileSelection', 'UIHelper.<init>'))  # handleFileSelection is unreachable (line 146); UIHelper.<init> has 98 callers in the graph
sup(('SyncPreferenceFragment.handleFileSelection', 'SyncManager.startSyncServiceHeartbeat'))  # handleFileSelection is unreachable (line 143); the method has three other callers
sup(('SyncPreferenceFragment.handleFileSelection', 'SyncPreferenceFragment.getSyncManager'))  # handleFileSelection is unreachable (line 143); getSyncManager has other live callers
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'SyncPreferenceFragment.forceDownload'))  # checkIfLocal is unreachable (line 303); forceDownload is reached from $6 (line 236)
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'SyncPreferenceFragment$9.<init>'))  # checkIfLocal is unreachable (line 287)
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'SyncPreferenceFragment$10.<init>'))  # checkIfLocal is unreachable (line 286)
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'UIHelper.binaryDialog(int,int)'))  # cross-batch (batch 040): the two-argument overload's only caller is checkIfLocal (line 286), so its label is UNREACHABLE (batch 040)
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'UIHelper.<init>'))  # checkIfLocal is unreachable (line 286); UIHelper.<init> has 98 callers in the graph
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'RecentDatabasesProvider.getCurrent'))  # checkIfLocal is unreachable (line 280); getCurrent has eight other callers
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'SyncPreferenceFragment.getDatabases'))  # checkIfLocal is unreachable (line 280)
sup(('SyncPreferenceFragment$1.call', 'SyncPreferenceFragment.checkIfLocalFileExistsAndDownload'))  # $1.call runs only from the unreachable chain; its call at line 159 is cut
sup(('SyncPreferenceFragment$9.call', 'SyncPreferenceFragment.forceDownload'))  # $9.call runs only from the unreachable chain; its call at line 298 is cut
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'RecentDatabasesProvider.add(DatabaseMetadata)'))  # saveDatabaseMetadata has no caller (line 140 is commented); RecentDatabasesProvider.add has three other callers
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'SyncPreferenceFragment.getDatabases'))  # saveDatabaseMetadata is unreachable (line 338)
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'DatabaseMetadataFactory.getInstance(String,String)'))  # saveDatabaseMetadata is unreachable (line 336); getInstance has one other caller
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'SettingsBase.set(Integer,String)@AppSettings'))  # saveDatabaseMetadata is unreachable (line 334); the set accessor has many callers
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'AppSettings.<init>'))  # saveDatabaseMetadata is unreachable (line 334); AppSettings.<init> has 49 callers
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'DatabaseManager.getDefaultDatabaseDirectory'))  # saveDatabaseMetadata is unreachable (line 330)
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'DatabaseManager.<init>'))  # saveDatabaseMetadata is unreachable (line 329); DatabaseManager.<init> has 13 callers
sup(('SyncPreferenceFragment_MembersInjector.create', 'SyncPreferenceFragment_MembersInjector.<init>'))  # create has no caller, so the edge cannot run (D14, D12)
sup(('SyncPreferenceFragment_MembersInjector.injectMembers', 'SyncPreferenceFragment_MembersInjector.injectMDatabases'))  # injectMembers has no caller; injectMDatabases stays reachable from injectSyncPreferenceFragment (batch 044)

# ---- part 123 (2026-10-29)
# ================================================================== batch 123 (label_123): SyncManager (31, incl. SyncManager$1.<init>), SyncManager_Factory (4), SyncManager_MembersInjector (5); 40 methods
# Result: 26 REACHABLE, 14 UNREACHABLE (rows in graphs/MMEX/parts/label_123.md). Evidence: graphs/MMEX/parts/label_123.grep.txt.
# This file writes only:
#   - 14 UNREACHABLE entries: 7 SyncManager methods with no live caller (SOURCE) and 7 Dagger-generated methods (INFERRED),
#   - 24 sup pairs (D14): auto CALL records whose caller is UNREACHABLE in this batch.
# No e() edges: every REACHABLE method already has an auto CALL record into it (auto_calls.json, USE_AUTO), or is reached through a hop
# already in graph_def.py (SyncManager.<init> -> DaggerMmxComponent.inject(SyncManager), batch 043; DaggerMmxComponent.injectSyncManager, batch 044).
# The 5 REACHABLE methods whose only live callers are in batch 125 (setEnabled, setSyncInterval, stopSyncServiceAlarm, triggerDownload,
# triggerUpload) get no edge here; their route runs through batch 125 (SyncPreferenceFragment$3, $5, forceDownload, forceUpload), not yet merged (D4, D8).
# The sup for SyncManager.resetPreferences -> SyncPreferences.clear is in label_121.py (batch 121), not repeated here.

# ------------------------------------------------------------------ UNREACHABLE: SyncManager methods with no live caller (SOURCE)

UNREACHABLE['SyncManager.resetPreferences'] = ('no_trigger_in_app',
    'no live caller: its only other mention is the call sync.resetPreferences() at SyncPreferenceFragment.java:262, inside a commented-out block of the reset listener; no auto_calls.json record has it as dst',
    'sync/SyncManager.java:256-258; sync/SyncPreferenceFragment.java:252-276; label_123.grep.txt section A',
    'SOURCE')

UNREACHABLE['SyncManager.abortScheduledUpload'] = ('no_trigger_in_app',
    'no caller: its only other mention is the call at SyncManager.java:220, which is commented out; no auto_calls.json record has it as dst',
    'sync/SyncManager.java:82-89, 220; label_123.grep.txt section B',
    'SOURCE')

UNREACHABLE['SyncManager.scheduleDelayedUpload'] = ('no_trigger_in_app',
    'no caller: its only other mention is the call at SyncManager.java:150, commented out inside dataChanged; no auto_calls.json record has it as dst',
    'sync/SyncManager.java:150, 496-504; label_123.grep.txt section C',
    'SOURCE')

UNREACHABLE['SyncManager.getPendingIntentForDelayedUpload'] = ('no_trigger_in_app',
    'its only callers are abortScheduledUpload (line 85) and scheduleDelayedUpload (line 497), both UNREACHABLE',
    'sync/SyncManager.java:85, 497, 506-520; label_123.grep.txt section D',
    'SOURCE')

UNREACHABLE['SyncManager.getAlarmManager'] = ('no_trigger_in_app',
    'its only callers are abortScheduledUpload (line 86) and scheduleDelayedUpload (line 498), both UNREACHABLE; SyncSchedulerBroadcastReceiver.getAlarmManager(Context) is a different method',
    'sync/SyncManager.java:86, 498, 521-523; label_123.grep.txt section E',
    'SOURCE')

UNREACHABLE['SyncManager.getExternalStorageDirectoryForSync'] = ('no_trigger_in_app',
    'no caller and no reference anywhere in the source root (only its declaration)',
    'sync/SyncManager.java:456-470; label_123.grep.txt section F',
    'SOURCE')

UNREACHABLE['SyncManager.areFileNamesSame'] = ('no_trigger_in_app',
    'no live caller: its only other mention is the call at SyncManager.java:315, commented out; no outgoing auto_calls.json record',
    'sync/SyncManager.java:315, 399-401; label_123.grep.txt section G',
    'SOURCE')

# ------------------------------------------------------------------ UNREACHABLE: Dagger-generated factory and members injector (INFERRED; grep evidence in label_123.grep.txt section H)

UNREACHABLE['SyncManager_Factory.get'] = ('no_trigger_in_app',
    'generated static factory method; no caller: no class file names SyncManager_Factory except itself, and no app source names it or a Provider<SyncManager>; its CALLs (lines 33-36) are cut by sup below',
    'SyncManager.java:68-72 (@Inject constructor, the reason Dagger generates the factory); auto_calls SyncManager_Factory.java:33-36; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_Factory.create'] = ('no_trigger_in_app',
    'generated static factory method; no caller (no auto_calls record and no reference in DaggerMmxComponent or the source); its CALL to Factory.<init> (line 44) is cut by sup below',
    'auto_calls SyncManager_Factory.java:44; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_Factory.newSyncManager'] = ('no_trigger_in_app',
    'generated factory method; no caller; its CALLs to SyncManager.<clinit> and SyncManager.<init> (line 48) are cut by sup below',
    'auto_calls SyncManager_Factory.java:48; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_Factory.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is Factory.create (auto record, line 44), which has no caller',
    'auto_calls SyncManager_Factory.java:44; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_MembersInjector.create'] = ('no_trigger_in_app',
    'generated static factory method; no caller: DaggerMmxComponent.class references only the two static injectors injectDateTimeUtilsLazy and injectMDatabases (constant-pool parse); its CALL to MembersInjector.<init> (line 30) is cut by sup below',
    'auto_calls SyncManager_MembersInjector.java:30; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_MembersInjector.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is MembersInjector.create (auto record, line 30), which has no caller',
    'auto_calls SyncManager_MembersInjector.java:30; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'generated instance method, reached only through the MembersInjector interface on an object that create would build; create has no caller and no injectMembers appears as a callee; its CALLs (lines 35-36) are cut by sup below',
    'auto_calls SyncManager_MembersInjector.java:35-36; label_123.grep.txt section H',
    'INFERRED')

# ------------------------------------------------------------------ sup pairs (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('SyncManager.resetPreferences', 'SyncManager.getPreferences'))  # resetPreferences has no caller, so its call to getPreferences (SyncManager.java:257) cannot run; its call to SyncPreferences.clear is cut in label_121.py
sup(('SyncManager.abortScheduledUpload', 'SyncManager.getPendingIntentForDelayedUpload'))  # abortScheduledUpload has no caller (SyncManager.java:85)
sup(('SyncManager.abortScheduledUpload', 'SyncManager.getAlarmManager'))  # abortScheduledUpload has no caller (SyncManager.java:86)
sup(('SyncManager.scheduleDelayedUpload', 'SyncManager.getPendingIntentForDelayedUpload'))  # scheduleDelayedUpload has no caller (SyncManager.java:497)
sup(('SyncManager.scheduleDelayedUpload', 'SyncManager.getAlarmManager'))  # scheduleDelayedUpload has no caller (SyncManager.java:498)
sup(('SyncManager.scheduleDelayedUpload', 'MmxDate.getMillis'))  # scheduleDelayedUpload has no caller (SyncManager.java:503); MmxDate.getMillis keeps its other caller SyncSchedulerBroadcastReceiver.startHeartbeat (batch 126)
sup(('SyncManager.scheduleDelayedUpload', 'MmxDate.<init>()'))  # scheduleDelayedUpload has no caller (SyncManager.java:503)
sup(('SyncManager.getPendingIntentForDelayedUpload', 'SyncManager.getContext'))  # getPendingIntentForDelayedUpload has only UNREACHABLE callers (SyncManager.java:516)
sup(('SyncManager.getPendingIntentForDelayedUpload', 'RecentDatabasesProvider.getCurrent'))  # getPendingIntentForDelayedUpload has only UNREACHABLE callers (SyncManager.java:507)
sup(('SyncManager.getPendingIntentForDelayedUpload', 'SyncManager.getDatabases'))  # getPendingIntentForDelayedUpload has only UNREACHABLE callers (SyncManager.java:507)
sup(('SyncManager.getAlarmManager', 'SyncManager.getContext'))  # getAlarmManager has only UNREACHABLE callers (SyncManager.java:522)
sup(('SyncManager.getExternalStorageDirectoryForSync', 'SyncManager.getContext'))  # getExternalStorageDirectoryForSync has no caller (SyncManager.java:468)
sup(('SyncManager.getExternalStorageDirectoryForSync', 'DatabaseManager.<init>'))  # getExternalStorageDirectoryForSync has no caller (SyncManager.java:459)
sup(('SyncManager.getExternalStorageDirectoryForSync', 'DatabaseManager.getDefaultDatabaseDirectory'))  # getExternalStorageDirectoryForSync has no caller (SyncManager.java:460)
sup(('SyncManager_Factory.get', 'SyncManager.<clinit>'))  # Factory.get has no caller (SyncManager_Factory.java:33)
sup(('SyncManager_Factory.get', 'SyncManager.<init>'))  # Factory.get has no caller (SyncManager_Factory.java:33)
sup(('SyncManager_Factory.get', 'SyncManager_MembersInjector.injectDateTimeUtilsLazy'))  # Factory.get has no caller (SyncManager_Factory.java:34)
sup(('SyncManager_Factory.get', 'SyncManager_MembersInjector.injectMDatabases'))  # Factory.get has no caller (SyncManager_Factory.java:36)
sup(('SyncManager_Factory.create', 'SyncManager_Factory.<init>'))  # Factory.create has no caller (SyncManager_Factory.java:44)
sup(('SyncManager_Factory.newSyncManager', 'SyncManager.<clinit>'))  # Factory.newSyncManager has no caller (SyncManager_Factory.java:48)
sup(('SyncManager_Factory.newSyncManager', 'SyncManager.<init>'))  # Factory.newSyncManager has no caller (SyncManager_Factory.java:48)
sup(('SyncManager_MembersInjector.create', 'SyncManager_MembersInjector.<init>'))  # MembersInjector.create has no caller (SyncManager_MembersInjector.java:30)
sup(('SyncManager_MembersInjector.injectMembers', 'SyncManager_MembersInjector.injectDateTimeUtilsLazy'))  # injectMembers has no caller (SyncManager_MembersInjector.java:35)
sup(('SyncManager_MembersInjector.injectMembers', 'SyncManager_MembersInjector.injectMDatabases'))  # injectMembers has no caller (SyncManager_MembersInjector.java:36)

# ---- part 126 (2026-10-29)
# ================================================================== batch 126 (label_126): SyncSchedulerBroadcastReceiver (4 methods), SyncService (12), SyncService$1 and $2 (2), SyncServiceMessage (3), SyncServiceMessageHandler (6), SyncServiceMessageHandler_MembersInjector (4), SyncService_MembersInjector (4); 35 methods
# Result: 23 REACHABLE, 12 UNREACHABLE (11 no_trigger_in_app, 1 branch_never_taken), 0 INCOMPLETE (rows: graphs/MMEX/parts/label_126.md). Grep evidence: graphs/MMEX/parts/label_126.grep.txt.
# This file writes:
#   - ENTRY from S_ENTRY to SyncSchedulerBroadcastReceiver.<init> (manifest lines 100-106: BOOT_COMPLETED, START_SYNC_SERVICE, STOP_SYNC_SERVICE),
#   - LIFECYCLE from the receiver <init> to onReceive (ActivityThread.handleReceiver, line 3187),
#   - INTENT from SyncManager.startSyncServiceHeartbeat and SyncManager.stopSyncServiceAlarm (batch 123 methods) to onReceive (D1: the destination is this batch's method),
#   - FRAMEWORK from SyncService.enqueueWork (JobIntentService, INFERRED) to SyncService.<init> and to onHandleWork,
#   - LIFECYCLE from SyncService.<init> to onCreate (ActivityThread.handleCreateService, line 3339) and from onHandleWork to onDestroy (INFERRED: JobIntentService stopSelf, ActivityThread line 3504),
#   - FRAMEWORK from SyncService.sendMessage to SyncServiceMessageHandler.handleMessage (Messenger delivery through Handler.dispatchMessage, Handler.java 97-106; the Messenger class is INFERRED),
#   - 9 sup() cuts (D14 for the UNREACHABLE callers; D18 for the branch that never runs),
#   - 12 UNREACHABLE entries.
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7). The auto CALL records into the batch's methods are: the receiver's startHeartbeat (67) and getAlarmManager (57); enqueueWork from SyncManager.invokeSyncService (batch 123, line 217); SyncService.onCreate -> DaggerMmxComponent.inject(SyncService) (line 86, cha); triggerSync (135); sendMessage (107, 128, 132, 185, 197, 210, 217); showNotificationForConflict (203); $1 and $2 (187, 199); SyncServiceMessage.<clinit> and <init> (107, 185, 65, 33); parse (62); closeDialog and getContext (112, 113); showProgressDialog (79); SyncServiceMessageHandler.<init> from invokeSyncService (batch 123, line 212); DaggerMmxComponent inject and inject-chain records (lines 323, 358, 554, 597).
# The batch's own MembersInjector records (create -> <init>, injectMembers -> inject calls) are the auto records cited in the UNREACHABLE evidence (D7, D14).
# Citation form for generated classes: 'ClassName.class bytecode line N' with the full path final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/.

# ---- the broadcast receiver: the manifest starts it on BOOT_COMPLETED and on the START and STOP actions; the framework creates it and calls onReceive

e('S_ENTRY', 'SyncSchedulerBroadcastReceiver.<init>', 'ENTRY',
  'the manifest registers SyncSchedulerBroadcastReceiver (exported) for BOOT_COMPLETED, START_SYNC_SERVICE and STOP_SYNC_SERVICE; the framework creates it when one of these broadcasts arrives',
  evidence='SRC AndroidManifest.xml:100-106 (receiver and intent-filter); FW-SRC core/java/android/app/ActivityThread.java:3141-3166 (handleReceiver; newInstance at 3166)')

e('SyncSchedulerBroadcastReceiver.<init>', 'SyncSchedulerBroadcastReceiver.onReceive', 'LIFECYCLE',
  'the framework calls onReceive on the new receiver instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3187 (receiver.onReceive)')

e('SyncManager.startSyncServiceHeartbeat', 'SyncSchedulerBroadcastReceiver.onReceive', 'INTENT',
  'startSyncServiceHeartbeat sends the ACTION_START broadcast (START_SYNC_SERVICE); the manifest filter delivers it to this receiver. The edge source is batch 123',
  evidence='SRC sync/SyncManager.java:268-281 (sendBroadcast of ACTION_START at 270-271); SRC sync/SyncSchedulerBroadcastReceiver.java:39-40 (action constants); AndroidManifest.xml:103')

e('SyncManager.stopSyncServiceAlarm', 'SyncSchedulerBroadcastReceiver.onReceive', 'INTENT',
  'stopSyncServiceAlarm sends the ACTION_STOP broadcast (STOP_SYNC_SERVICE); onReceive cancels the alarm and returns (lines 60-65). The edge source is batch 123',
  evidence='SRC sync/SyncManager.java:283-291 (sendBroadcast of ACTION_STOP at 285-286); SRC sync/SyncSchedulerBroadcastReceiver.java:40, 60-65; AndroidManifest.xml:104')

# ---- the sync service: JobIntentService.enqueueWork starts it (INFERRED androidx); the framework creates it and runs onCreate, then onHandleWork; onDestroy after the work

e('SyncService.enqueueWork', 'SyncService.<init>', 'FRAMEWORK',
  'the static enqueueWork (lines 151-153) hands the intent to JobIntentService.enqueueWork, which starts the service; the framework constructs it. The same pattern as the RecurringTransactionIntentService edges in graph_def.py',
  evidence='SRC sync/SyncService.java:151-153; FW-SRC core/java/android/app/ActivityThread.java:3311-3321 (handleCreateService; newInstance at 3321); INFERRED androidx JobIntentService (library not in the dataset; not read)')

e('SyncService.enqueueWork', 'SyncService.onHandleWork', 'FRAMEWORK',
  'JobIntentService delivers each queued intent to onHandleWork on its worker thread (INFERRED from the androidx contract)',
  evidence='SRC sync/SyncService.java:90 (onHandleWork), 151-153; INFERRED androidx JobIntentService (not read)')

e('SyncService.<init>', 'SyncService.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it constructs the service (handleCreateService)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3339 (service.onCreate); SRC sync/SyncService.java:79-87')

e('SyncService.onHandleWork', 'SyncService.onDestroy', 'LIFECYCLE',
  'when the queued work is done JobIntentService stops itself, and the framework then runs onDestroy (INFERRED androidx stopSelf path)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3499-3504 (handleStopService; s.onDestroy at 3504); FW-SRC core/java/android/app/Service.java:515; INFERRED androidx JobIntentService (not read)')

e('SyncService.sendMessage', 'SyncServiceMessageHandler.handleMessage', 'FRAMEWORK',
  'sendMessage hands a Message to the caller Messenger (SyncManager.invokeSyncService creates it, batch 123); the framework delivers it to the handler, which calls handleMessage. The Messenger exists only when the sync starts from an AppCompatActivity (SyncManager.java:210-213)',
  evidence='SRC sync/SyncService.java:222-236 (msg.what at 226; outMessenger.send at 229); FW-SRC core/java/os/Handler.java:97-106 (dispatchMessage calls handleMessage at 106); INFERRED android.os.Messenger (not in fw_src; not read)')

# ---- cuts. D14: an auto CALL edge whose caller is UNREACHABLE in this batch is cut, so the target has no live incoming edge from it.
#      The <init> cuts complete the SyncNotificationFactory cuts that batch 124 wrote for the getters (its file: SyncService.java:169 and 253).

sup(('SyncService.sendStartEvent', 'SyncStartingEvent.<init>'))  # D14: sendStartEvent has no live caller (label_126.grep.txt section A); the constructor is batch 127's
sup(('SyncService.sendStopEvent', 'SyncStoppingEvent.<init>'))  # D14: sendStopEvent has no live caller (section A); the constructor is batch 127's
sup(('SyncService.showNotificationUploading', 'SyncNotificationFactory.<init>'))  # D14: line 252 (the getter record at 253 is cut by batch 124)
sup(('SyncService.showNotificationUploadComplete', 'SyncNotificationFactory.<init>'))  # D14: line 168 (the getter record at 169 is cut by batch 124)
sup(('SyncServiceMessageHandler.handleMessage', 'SyncServiceMessageHandler.showProgressDialog'))  # D18 branch judgment: only the STARTING_DOWNLOAD case calls it (line 79), and no sender uses that code (section E)
sup(('SyncService_MembersInjector.create', 'SyncService_MembersInjector.<init>'))  # D14: create has no caller (section C), so its call into <init> cannot run
sup(('SyncService_MembersInjector.injectMembers', 'SyncService_MembersInjector.injectRecentDatabasesProvider'))  # D14: injectMembers has no caller (section C)
sup(('SyncServiceMessageHandler_MembersInjector.create', 'SyncServiceMessageHandler_MembersInjector.<init>'))  # D14: create has no caller (section C)
sup(('SyncServiceMessageHandler_MembersInjector.injectMembers', 'SyncServiceMessageHandler_MembersInjector.injectMDatabases'))  # D14: injectMembers has no caller (section C)

# ---- UNREACHABLE: source methods with no live caller (no_trigger_in_app, SOURCE)

UNREACHABLE['SyncService.sendStartEvent'] = ('no_trigger_in_app',
  'private method; its only call site (line 95) is commented out, and no other class calls it (label_126.grep.txt section A); auto_calls.json has no caller record',
  'SRC sync/SyncService.java:238-243 (EventBus post of SyncStartingEvent at 241); label_126.grep.txt section A',
  'SOURCE')

UNREACHABLE['SyncService.sendStopEvent'] = ('no_trigger_in_app',
  'private method; every call site (lines 108, 116, 186, 198) is commented out, and no other class calls it (label_126.grep.txt section A)',
  'SRC sync/SyncService.java:245-249 (EventBus post of SyncStoppingEvent at 247); SRC sync/SyncService.java:108, 116, 186, 198 (commented); label_126.grep.txt section A',
  'SOURCE')

UNREACHABLE['SyncService.showNotificationUploading'] = ('no_trigger_in_app',
  'private method with no call site in the app source (its only occurrence is the declaration at 251; label_126.grep.txt section A) and no caller record in auto_calls.json',
  'SRC sync/SyncService.java:251-259 (declaration at 251; constructor call at 252); label_126.grep.txt section A',
  'SOURCE')

UNREACHABLE['SyncService.showNotificationUploadComplete'] = ('no_trigger_in_app',
  'private method with no call site in the app source (its only occurrence is the declaration at 155; label_126.grep.txt section A) and no caller record in auto_calls.json',
  'SRC sync/SyncService.java:155-172 (declaration at 155; constructor call at 168); label_126.grep.txt section A',
  'SOURCE')

UNREACHABLE['SyncServiceMessageHandler.getDatabases'] = ('no_trigger_in_app',
  'private method whose only callers are in storeRecentDb (lines 148 and 153), and storeRecentDb is commented out (lines 145-154; its call at line 85 is commented out too); no caller record in auto_calls.json',
  'SRC sync/SyncServiceMessageHandler.java:131-133 (declaration at 131), 85, 145-154 (commented); label_126.grep.txt section A',
  'SOURCE')

# ---- UNREACHABLE: a branch that no sender reaches (branch_never_taken, SOURCE)

UNREACHABLE['SyncServiceMessageHandler.showProgressDialog'] = ('branch_never_taken',
  'called only from the STARTING_DOWNLOAD case of handleMessage (line 77-82, call at 79); no code in the app sends SyncServiceMessage.STARTING_DOWNLOAD, since the code appears only as a declaration and a case label (label_126.grep.txt sections B and E). The auto CALL at line 79 is cut (sup, D18)',
  'SRC sync/SyncServiceMessageHandler.java:77-82 (call at 79), 135-143 (declaration); SRC sync/SyncServiceMessage.java:28; label_126.grep.txt sections B and E',
  'SOURCE')

# ---- UNREACHABLE: Dagger-generated MembersInjector methods with no caller (no_trigger_in_app, INFERRED; D5, D12)

UNREACHABLE['SyncServiceMessageHandler_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (not in the source root). Its only caller is SyncServiceMessageHandler_MembersInjector.create, which has no caller record; no class file outside the owner references it (label_126.grep.txt section F)',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncServiceMessageHandler_MembersInjector.class bytecode line 25 (create -> <init>); auto_calls.json 42944-42947; label_126.grep.txt sections C and F',
  'INFERRED')

UNREACHABLE['SyncServiceMessageHandler_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (not in the source root). No caller record in auto_calls.json; no class file outside the owner references create (label_126.grep.txt section F, 0 external references)',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncServiceMessageHandler_MembersInjector.class bytecode line 25 (its only outgoing call); auto_calls.json 42944-42947; label_126.grep.txt sections C and F',
  'INFERRED')

UNREACHABLE['SyncServiceMessageHandler_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (not in the source root). No caller record for any receiver in auto_calls.json. The only reference in the build is a self-reference inside the class (INFERRED: the compiler bridge for MembersInjector<T>.injectMembers); the component calls injectMDatabases directly (DaggerMmxComponent.class bytecode line 554 record). label_126.grep.txt section F',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncServiceMessageHandler_MembersInjector.class bytecode line 30; auto_calls.json 42952-42955; label_126.grep.txt sections C and F',
  'INFERRED')

UNREACHABLE['SyncService_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (not in the source root). Its only caller is SyncService_MembersInjector.create, which has no caller record; no class file outside the owner references it (label_126.grep.txt section F)',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncService_MembersInjector.class bytecode line 21 (create -> <init>); auto_calls.json 42834-42837; label_126.grep.txt sections C and F',
  'INFERRED')

UNREACHABLE['SyncService_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (not in the source root). No caller record in auto_calls.json; no class file outside the owner references create (label_126.grep.txt section F, 0 external references)',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncService_MembersInjector.class bytecode line 21 (its only outgoing call); auto_calls.json 42834-42837; label_126.grep.txt sections C and F',
  'INFERRED')

UNREACHABLE['SyncService_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (not in the source root). No caller record for any receiver in auto_calls.json. The only reference in the build is a self-reference inside the class (INFERRED: the compiler bridge for MembersInjector<T>.injectMembers); the component calls injectRecentDatabasesProvider directly (DaggerMmxComponent.class bytecode line 597 record). label_126.grep.txt section F',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncService_MembersInjector.class bytecode line 26; auto_calls.json 42842-42845; label_126.grep.txt sections C and F',
  'INFERRED')

# ---- part 129 (2026-10-29)
# ================================================================== batch 129 (label_129): CheckingTransactionEditActivity_MembersInjector (4 methods), EditTransactionActivityConstants (1 method); 5 methods
# Result: 1 REACHABLE, 4 UNREACHABLE (rows: graphs/MMEX/parts/label_129.md). Grep evidence: graphs/MMEX/parts/label_129.grep.txt.
# This file writes:
#   - 4 UNREACHABLE entries (kind no_trigger_in_app): create, <init> and injectMembers of the generated MembersInjector (INFERRED), and EditTransactionActivityConstants.<init> (SOURCE),
#   - 2 sup cuts (D14) for the auto CALL records out of the UNREACHABLE methods: create -> <init> and injectMembers -> injectDatabase.
# No edge is written. The one REACHABLE method, injectDatabase, is reached only through auto CALL records (DaggerMmxComponent.injectCheckingTransactionEditActivity -> injectDatabase, D7), so the build finds it (D4).

# ---- UNREACHABLE: the generated MembersInjector factory, constructor and instance injector, and the constants class constructor

UNREACHABLE['CheckingTransactionEditActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
    'Dagger-generated constructor (not in the source root) whose only caller record is CheckingTransactionEditActivity_MembersInjector.create (auto record line 22), and create has no caller (grep B2, C1); no class file other than CheckingTransactionEditActivity_MembersInjector.class references <init> (grep C1)',
    'CheckingTransactionEditActivity_MembersInjector.class bytecode line 22 (final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/transactions/); label_129.grep.txt B1, B2, C1',
    'INFERRED')

UNREACHABLE['CheckingTransactionEditActivity_MembersInjector.create'] = ('no_trigger_in_app',
    'Dagger-generated static factory (not in the source root) with no caller record in auto_calls.json (grep B2) and no Methodref to create in any of the 825 class files (grep C1); no app source names the MembersInjector (grep A1)',
    'CheckingTransactionEditActivity_MembersInjector.class bytecode line 22 (final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/transactions/); label_129.grep.txt A1, B2, C1',
    'INFERRED')

UNREACHABLE['CheckingTransactionEditActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'Dagger-generated instance method (not in the source root) with no caller record in auto_calls.json for any receiver (grep B2, B3); its only Methodref is inside CheckingTransactionEditActivity_MembersInjector.class itself (grep C1), and the class is never instantiated (no Methodref to create or to <init> outside the class, grep C1), so no MembersInjector object reaches it; the component injects through injectDatabase directly (DaggerMmxComponent.class bytecode line 389)',
    'CheckingTransactionEditActivity_MembersInjector.class bytecode line 27 (final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/transactions/); label_129.grep.txt B1, B2, B3, C1',
    'INFERRED')

UNREACHABLE['EditTransactionActivityConstants.<init>'] = ('no_trigger_in_app',
    'Constants-only class (20 uncommented static final String fields, all literal, grep E4 and E6) with no explicit constructor (grep E1); no new EditTransactionActivityConstants in the source (grep A2); no class file in the build references EditTransactionActivityConstants at all, so no Methodref to <init> (grep C1); no auto_calls.json record has it as dst (grep B1)',
    'transactions/EditTransactionActivityConstants.java:23-48; label_129.grep.txt A2, B1, C1, E1, E4',
    'SOURCE')

# ---- D14: the outgoing auto CALL records of the UNREACHABLE methods (caller UNREACHABLE in this batch)

sup(('CheckingTransactionEditActivity_MembersInjector.create', 'CheckingTransactionEditActivity_MembersInjector.<init>'))  # caller UNREACHABLE (D14); auto record line 22
sup(('CheckingTransactionEditActivity_MembersInjector.injectMembers', 'CheckingTransactionEditActivity_MembersInjector.injectDatabase'))  # caller UNREACHABLE (D14); auto record line 27

# ---- part 127 (2026-10-29)
# ================================================================== batch 127 (label_127): Authenticator (8 methods), AuthenticatorService (3), StubSyncProvider (7), SyncAdapter (3), SyncAdapterService (4), SyncAdapterTrigger (4), DbFileDownloadedEvent (1), SyncStartingEvent (1), SyncStoppingEvent (1), DownloadWorker (2), SyncWorker (2), UploadWorker (2); 38 methods
# Result: 13 REACHABLE, 25 UNREACHABLE (rows: graphs/MMEX/parts/label_127.md). Grep evidence: graphs/MMEX/parts/label_127.grep.txt.
# This file writes:
#   - 9 edges: ENTRY from S_ENTRY to AuthenticatorService.<init> (other_app: the Add account UI) and to SyncAdapterService.<clinit> and <init> (other_app: a bind by the SyncAdapter action);
#     LIFECYCLE from each service constructor to onCreate and from onCreate to onBind; LIFECYCLE from StubSyncProvider.<init> to onCreate;
#     FRAMEWORK (non_standard) from AuthenticatorService.onBind to Authenticator.addAccount (the binder dispatch);
#   - 25 UNREACHABLE entries (4-element tuples);
#   - 2 sup cuts (D20 target-owner cut) for the constructor records of the two events. Their callers are batch 126's sendStartEvent and sendStopEvent, which have no live caller.
#     Batch 126 already writes both cuts (label_126.py:59-60) and graph_def.py:11526 has the stop one; they are repeated here because the constructors are this batch's (set semantics, harmless).
# No CALL edge is written (D7). The auto CALL records that touch this batch are five: SyncAdapterService.onCreate -> SyncAdapter.<init>(Context,boolean) (SyncAdapterService.java:57),
#   AuthenticatorService.onCreate -> Authenticator.<init> (AuthenticatorService.java:36) (both REACHABLE sources), SyncService.sendStartEvent -> SyncStartingEvent.<init> (SyncService.java:241),
#   SyncService.sendStopEvent -> SyncStoppingEvent.<init> (SyncService.java:247) (both cut above), SyncServiceMessageHandler.handleMessage -> DbFileDownloadedEvent.<init> (SyncServiceMessageHandler.java:89, REACHABLE through batch 126).
#   No record has an UNREACHABLE source inside this batch, so no D14 cut is needed here. Framework and library calls (framework_calls: ContentProvider.<init>, Worker.<init>, AbstractThreadedSyncAdapter.<init> and others) are not CALL records and are not cut.

# ---- ENTRY: the two manifest services that other apps or the system bind; the framework creates each one by class name

e('S_ENTRY', 'AuthenticatorService.<init>', 'ENTRY',
  'the Add account list in system settings shows MMEX (authenticator.xml label app_name); choosing it makes AccountManager bind AuthenticatorService, and the framework creates the service by class name',
  env=env_text('outside package: the system Settings app adds an account of type example.com (res/xml/authenticator.xml:20), and AccountManager binds AuthenticatorService (exported=false)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:455-465 (service, exported=false, intent-filter android.accounts.AccountAuthenticator); SRC res/xml/authenticator.xml:19-22; FW-SRC core/java/android/app/ActivityThread.java:3311-3321 (handleCreateService; newInstance at 3321); INFERRED AccountManagerService binds the authenticator (system_server, not read)')

e('AuthenticatorService.<init>', 'AuthenticatorService.onCreate', 'LIFECYCLE',
  'the framework calls onCreate on the new service (handleCreateService)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3339 (service.onCreate); SRC sync/adapter/AuthenticatorService.java:33-37')

e('AuthenticatorService.onCreate', 'AuthenticatorService.onBind', 'LIFECYCLE',
  'a client binds the created service, and the framework calls onBind (handleBindService)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3356-3366 (handleBindService; s.onBind at 3366); SRC sync/adapter/AuthenticatorService.java:42-45')

e('AuthenticatorService.onBind', 'Authenticator.addAccount', 'FRAMEWORK',
  'the system Add account flow calls addAccount through the binder that onBind returns (getIBinder, AuthenticatorService.java:44); addAccount returns null, so no account is created',
  cls='non_standard',
  via='AbstractAccountAuthenticator binder stub: onBind returns the IBinder from getIBinder, and the stub dispatches addAccount (the library and AccountManagerService are not in fw_src; INFERRED)',
  evidence='SRC sync/adapter/AuthenticatorService.java:42-45; SRC sync/adapter/Authenticator.java:43-46; INFERRED framework binder dispatch (AbstractAccountAuthenticator not read)')

e('StubSyncProvider.<init>', 'StubSyncProvider.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor, from attachInfo',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:6225-6239; FW-SRC core/java/android/content/ContentProvider.java:1891-1917; SRC sync/adapter/StubSyncProvider.java:36-39')

e('S_ENTRY', 'SyncAdapterService.<clinit>', 'ENTRY',
  'another app binds SyncAdapterService by its SyncAdapter action; the framework creates the service by class name, and the JVM initialises the class first',
  env=env_text('outside package: another app binds to SyncAdapterService by the android.content.SyncAdapter action (exported=true, no permission, process :sync)', ('other_app',)),
  cls='non_standard',
  via='intent resolved by action name android.content.SyncAdapter (AndroidManifest.xml:466-477); the framework creates the service (ActivityThread handleCreateService)',
  evidence='SRC AndroidManifest.xml:466-477; SRC sync/adapter/SyncAdapterService.java:41-43 (static initialisers: sSyncAdapter at 41, sSyncAdapterLock = new Object() at 43); FW-SRC core/java/android/app/ActivityThread.java:3321 (newInstance); INFERRED the JVM initialises the class at the first newInstance (Java language rule)')

e('S_ENTRY', 'SyncAdapterService.<init>', 'ENTRY',
  'another app binds SyncAdapterService by its SyncAdapter action; the framework creates the service by class name',
  env=env_text('outside package: another app binds to SyncAdapterService by the android.content.SyncAdapter action (exported=true, no permission, process :sync)', ('other_app',)),
  cls='non_standard',
  via='intent resolved by action name android.content.SyncAdapter (AndroidManifest.xml:466-477); the framework creates the service (ActivityThread handleCreateService)',
  evidence='SRC AndroidManifest.xml:466-477; FW-SRC core/java/android/app/ActivityThread.java:3321 (newInstance)')

e('SyncAdapterService.<init>', 'SyncAdapterService.onCreate', 'LIFECYCLE',
  'the framework calls onCreate on the new service (handleCreateService)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3339 (service.onCreate); SRC sync/adapter/SyncAdapterService.java:48-60')

e('SyncAdapterService.onCreate', 'SyncAdapterService.onBind', 'LIFECYCLE',
  'a client binds the created service, and the framework calls onBind (handleBindService)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3356-3366 (handleBindService; s.onBind at 3366); SRC sync/adapter/SyncAdapterService.java:66-75')

# ---- D20 target-owner cut: the two event constructors are this batch's; their only callers are batch 126's sendStartEvent and sendStopEvent, which have no live caller


# ---- UNREACHABLE: Authenticator overrides that the account framework calls only for an account of type example.com (no_trigger_in_app, INFERRED)

UNREACHABLE['Authenticator.confirmCredentials'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:48-51, 43-46; label_127.grep.txt E',
  'INFERRED')

UNREACHABLE['Authenticator.editProperties'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:38-41, 43-46; label_127.grep.txt E',
  'INFERRED')

UNREACHABLE['Authenticator.getAuthToken'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:53-56, 43-46; label_127.grep.txt E',
  'INFERRED')

UNREACHABLE['Authenticator.getAuthTokenLabel'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:58-61, 43-46; label_127.grep.txt E',
  'INFERRED')

UNREACHABLE['Authenticator.hasFeatures'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:68-71, 43-46; label_127.grep.txt E',
  'INFERRED')

UNREACHABLE['Authenticator.updateCredentials'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:63-66, 43-46; label_127.grep.txt E',
  'INFERRED')

# ---- UNREACHABLE: StubSyncProvider overrides (the provider is reached only through a call on the datasyncprovider authority; no_trigger_in_app, INFERRED)

UNREACHABLE['StubSyncProvider.delete'] = ('no_trigger_in_app',
  'the provider receives delete only from a ContentResolver or ContentProviderClient call on its authority (datasyncprovider, AndroidManifest.xml:392); no code makes such a call (grep D: the authority occurs only in the manifest). The sync framework uses the adapter authority (SyncAdapterService.AUTHORITY), not this one',
  'SRC sync/adapter/StubSyncProvider.java:70-73; SRC AndroidManifest.xml:390-394; label_127.grep.txt D',
  'INFERRED')

UNREACHABLE['StubSyncProvider.getType'] = ('no_trigger_in_app',
  'the provider receives getType only from a ContentResolver or ContentProviderClient call on its authority (datasyncprovider, AndroidManifest.xml:392); no code makes such a call (grep D: the authority occurs only in the manifest). The sync framework uses the adapter authority (SyncAdapterService.AUTHORITY), not this one',
  'SRC sync/adapter/StubSyncProvider.java:43-46; SRC AndroidManifest.xml:390-394; label_127.grep.txt D',
  'INFERRED')

UNREACHABLE['StubSyncProvider.insert'] = ('no_trigger_in_app',
  'the provider receives insert only from a ContentResolver or ContentProviderClient call on its authority (datasyncprovider, AndroidManifest.xml:392); no code makes such a call (grep D: the authority occurs only in the manifest). The sync framework uses the adapter authority (SyncAdapterService.AUTHORITY), not this one',
  'SRC sync/adapter/StubSyncProvider.java:63-67; SRC AndroidManifest.xml:390-394; label_127.grep.txt D',
  'INFERRED')

UNREACHABLE['StubSyncProvider.query'] = ('no_trigger_in_app',
  'the provider receives query only from a ContentResolver or ContentProviderClient call on its authority (datasyncprovider, AndroidManifest.xml:392); no code makes such a call (grep D: the authority occurs only in the manifest). The sync framework uses the adapter authority (SyncAdapterService.AUTHORITY), not this one',
  'SRC sync/adapter/StubSyncProvider.java:51-59; SRC AndroidManifest.xml:390-394; label_127.grep.txt D',
  'INFERRED')

UNREACHABLE['StubSyncProvider.update'] = ('no_trigger_in_app',
  'the provider receives update only from a ContentResolver or ContentProviderClient call on its authority (datasyncprovider, AndroidManifest.xml:392); no code makes such a call (grep D: the authority occurs only in the manifest). The sync framework uses the adapter authority (SyncAdapterService.AUTHORITY), not this one',
  'SRC sync/adapter/StubSyncProvider.java:77-83; SRC AndroidManifest.xml:390-394; label_127.grep.txt D',
  'INFERRED')

# ---- UNREACHABLE: SyncAdapter (the three-argument constructor has no caller; onPerformSync is the framework callback for an account that is never created)

UNREACHABLE['SyncAdapter.<init>(Context,boolean,boolean)'] = ('no_trigger_in_app',
  'no caller: the only construction in the source root is the two-argument new SyncAdapter(getApplicationContext(), true) at SyncAdapterService.java:57 (grep B), and the two-argument constructor calls the superclass directly (SyncAdapter.java:45), so the three-argument one is never invoked',
  'SRC sync/adapter/SyncAdapter.java:58-69 (super at 62); SRC sync/adapter/SyncAdapterService.java:57; label_127.grep.txt B',
  'SOURCE')

UNREACHABLE['SyncAdapter.onPerformSync'] = ('no_trigger_in_app',
  'the sync framework calls it only for a sync of an account of type com.money.manager.ex.sync, and that account is created only by SyncAdapterTrigger.CreateSyncAccount, which has no caller (grep A). runSync and schedulePeriodicSync (the requests that would start a sync) have no caller either (grep A). The body is a todo comment and a Timber.d log (SyncAdapter.java:85), so it does no work even if reached',
  'SRC sync/adapter/SyncAdapter.java:82-88 (Timber.d at 85); label_127.grep.txt A, B',
  'INFERRED')

# ---- UNREACHABLE: SyncAdapterTrigger (no caller for any method; its only calls are in comments)

UNREACHABLE['SyncAdapterTrigger.<init>'] = ('no_trigger_in_app',
  'the class has only the implicit default constructor (class at line 42); its only new SyncAdapterTrigger() in the source root is in a comment (line 39), so no code creates the trigger (grep A)',
  'SRC sync/adapter/SyncAdapterTrigger.java:42, 39 (comment); label_127.grep.txt A',
  'SOURCE')

UNREACHABLE['SyncAdapterTrigger.CreateSyncAccount'] = ('no_trigger_in_app',
  'its only call (line 38) is in a comment, and no other code in the source root calls it (grep A), so no account of type com.money.manager.ex.sync is created',
  'SRC sync/adapter/SyncAdapterTrigger.java:49-64 (addAccountExplicitly at 58), 38; label_127.grep.txt A, E',
  'SOURCE')

UNREACHABLE['SyncAdapterTrigger.runSync'] = ('no_trigger_in_app',
  'its only call (line 39) is in a comment, and no other code calls it (grep A), so the requestSync call it would make (line 110) never runs',
  'SRC sync/adapter/SyncAdapterTrigger.java:99-112 (requestSync at 110), 39; label_127.grep.txt A, D',
  'SOURCE')

UNREACHABLE['SyncAdapterTrigger.schedulePeriodicSync'] = ('no_trigger_in_app',
  'no caller in the source root: the name occurs only at its declaration (line 85; grep A), so the addPeriodicSync call it would make (line 91) never runs',
  'SRC sync/adapter/SyncAdapterTrigger.java:85-97 (addPeriodicSync at 91); label_127.grep.txt A',
  'SOURCE')

# ---- UNREACHABLE: the two event constructors (their only callers are batch 126's sendStartEvent and sendStopEvent, which have no live caller)

UNREACHABLE['SyncStartingEvent.<init>'] = ('no_trigger_in_app',
  'the only construction is in SyncService.sendStartEvent (SyncService.java:241), which has no live caller (batch 126: its call at line 95 is commented out, and no other class calls it); the constructor has no other call (grep G)',
  'SRC sync/events/SyncStartingEvent.java:24 (default constructor); SRC sync/SyncService.java:238-243; label_127.grep.txt G',
  'SOURCE')

UNREACHABLE['SyncStoppingEvent.<init>'] = ('no_trigger_in_app',
  'the only construction is in SyncService.sendStopEvent (SyncService.java:247), which has no live caller (batch 126: its calls at lines 108, 116, 186 and 198 are commented out, and no other class calls it); the constructor has no other call (grep G)',
  'SRC sync/events/SyncStoppingEvent.java:24 (default constructor); SRC sync/SyncService.java:245-249; label_127.grep.txt G',
  'SOURCE')

# ---- UNREACHABLE: the three Worker classes (no WorkRequest names them; no_trigger_in_app, SOURCE)

UNREACHABLE['DownloadWorker.<init>'] = ('no_trigger_in_app',
  'no code names DownloadWorker outside its own file (grep C); WorkManager creates a Worker only for a WorkRequest that names it, and src/main has no WorkRequest (grep C)',
  'SRC sync/jobmanager/DownloadWorker.java:30-33; label_127.grep.txt C',
  'SOURCE')

UNREACHABLE['DownloadWorker.doWork'] = ('no_trigger_in_app',
  'its only caller would be WorkManager running a DownloadWorker request, and no such request exists (grep C); the body returns Result.success() (DownloadWorker.java:36-39)',
  'SRC sync/jobmanager/DownloadWorker.java:36-39; label_127.grep.txt C',
  'SOURCE')

UNREACHABLE['SyncWorker.<init>'] = ('no_trigger_in_app',
  'no code names SyncWorker outside its own file (grep C); WorkManager creates a Worker only for a WorkRequest that names it, and src/main has no WorkRequest (grep C)',
  'SRC sync/jobmanager/SyncWorker.java:30-33; label_127.grep.txt C',
  'SOURCE')

UNREACHABLE['SyncWorker.doWork'] = ('no_trigger_in_app',
  'its only caller would be WorkManager running a SyncWorker request, and no such request exists (grep C); the body returns Result.success() (SyncWorker.java:36-39)',
  'SRC sync/jobmanager/SyncWorker.java:36-39; label_127.grep.txt C',
  'SOURCE')

UNREACHABLE['UploadWorker.<init>'] = ('no_trigger_in_app',
  'no code names UploadWorker outside its own file (grep C); WorkManager creates a Worker only for a WorkRequest that names it, and src/main has no WorkRequest (grep C)',
  'SRC sync/jobmanager/UploadWorker.java:30-33; label_127.grep.txt C',
  'SOURCE')

UNREACHABLE['UploadWorker.doWork'] = ('no_trigger_in_app',
  'its only caller would be WorkManager running an UploadWorker request, and no such request exists (grep C); the body returns Result.success() (UploadWorker.java:36-39)',
  'SRC sync/jobmanager/UploadWorker.java:36-39; label_127.grep.txt C',
  'SOURCE')

# ---- part 131 (2026-10-29)
# ================================================================== batch 131 (label_131): com.money.manager.ex.transactions.EditTransactionCommonFunctions (methods 41-80 of 115 in this class; 40 methods)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_131.md (40 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_131.grep.txt.
# This file writes 6 e() edges (FRAMEWORK, listener callbacks), 0 gui() edges, 0 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). Every other route is a CALL edge from auto_calls.json (USE_AUTO, D7) and is not written here.
# The callers of this batch's methods are in batches 128, 099, 130 and 132, which are not merged; those routes are interim (D8).
# A listener registered inside one of this batch's methods gets an edge from the registering method to the listener's callback (label_099.py convention). cls is standard.
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1 (the only framework evidence used here); INFERRED = a step whose source was not read.

# ---- account spinners (listener built in initAccountSelectors, set at 381 and 388)

e('EditTransactionCommonFunctions.initAccountSelectors', 'EditTransactionCommonFunctions$1.onItemSelected', 'FRAMEWORK',
  'the account spinner and the transfer-to spinner call onItemSelected when the user picks a row: AdapterView.fireOnSelected calls the listener',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:310-312 (listener creation), 381 (spinAccount.setOnItemSelectedListener), 388 (spinAccountTo.setOnItemSelectedListener); FW-SRC core/java/android/widget/AdapterView.java:412-413 (setOnItemSelectedListener stores the listener), 937-944 (fireOnSelected calls onItemSelected at 944); INFERRED: AbsSpinner.java is not in fw_src, so the path from the user pick to fireOnSelected is not read')

e('EditTransactionCommonFunctions.initAccountSelectors', 'EditTransactionCommonFunctions$1.onNothingSelected', 'FRAMEWORK',
  'the framework calls onNothingSelected when a spinner has no selected position: AdapterView.fireOnSelected calls the listener for a negative position',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:370-372 (empty onNothingSelected body), 381, 388 (listener set on both spinners); FW-SRC core/java/android/widget/AdapterView.java:945-947 (onNothingSelected called for a negative position); INFERRED: the code path that gives these spinners a negative position is not read')

# ---- remove-payee button (listener at 582)

e('EditTransactionCommonFunctions.initPayeeControls', 'EditTransactionCommonFunctions$10.onClick', 'FRAMEWORK',
  'the remove-payee button calls onClick on a tap: View.performClick calls the OnClickListener',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:582-592 (removePayeeButton.setOnClickListener at 582; onClick body 583-591); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls li.mOnClickListener.onClick(this) at 6294); INFERRED: the touch path to performClick is not read')

# ---- split button (listener at 599)

e('EditTransactionCommonFunctions.initSplitCategories', 'EditTransactionCommonFunctions$11.onClick', 'FRAMEWORK',
  'the split button calls onClick on a tap: View.performClick calls the OnClickListener, which calls isSplitSelected and then either the split form or the reset notice',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:599-623 (splitButton.setOnClickListener at 599; onClick body within 599-623); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED: the touch path to performClick is not read')

# ---- status spinner (listener at 646)

e('EditTransactionCommonFunctions.initStatusSelector', 'EditTransactionCommonFunctions$12.onItemSelected', 'FRAMEWORK',
  'the status spinner calls onItemSelected when the user picks a status: AdapterView.fireOnSelected calls the listener',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:646 (spinStatus.setOnItemSelectedListener), 646-657 (onItemSelected body); FW-SRC core/java/android/widget/AdapterView.java:412-413 (setOnItemSelectedListener stores the listener), 937-944 (fireOnSelected calls onItemSelected at 944); INFERRED: AbsSpinner.java is not in fw_src, as for $1')

e('EditTransactionCommonFunctions.initStatusSelector', 'EditTransactionCommonFunctions$12.onNothingSelected', 'FRAMEWORK',
  'the framework calls onNothingSelected when the status spinner has no selected position: AdapterView.fireOnSelected calls the listener for a negative position',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:659-661 (empty onNothingSelected body), 646 (listener set); FW-SRC core/java/android/widget/AdapterView.java:945-947 (onNothingSelected called for a negative position); INFERRED: AbsSpinner.java is not in fw_src, so the path to a negative position is not read')

# ---- part 132 (2026-10-29)
# ================================================================== batch 132 (label_132): EditTransactionCommonFunctions methods 81-115 of 115 (35 methods): the anonymous listener classes $2 to $9 and $13 to $19 (<init>, onClick, TextWatcher and lambda methods)
# Result: 35 REACHABLE, 0 UNREACHABLE (rows: graphs/MMEX/parts/label_132.md). Grep evidence: graphs/MMEX/parts/label_132.grep.txt.
# This file writes:
#   - 15 GUI edges (page -> method) from S_RECURRING_TRANSACTION_EDIT to the listeners and TextWatchers the user operates in the form (D1: each destination is a batch method);
#   - 5 FRAMEWORK edges (method -> listener): onActionCancelClick -> $16.onClick and $17.onClick, onTransferSelected -> $18.onClick, showSplitResetNotice -> $19.onClick (dialog buttons), and initTransactionNumberControls -> $14.onClick (View.callOnClick at line 725; no auto_calls.json record targets $14.onClick, grep G4).
# No UNREACHABLE entries (every method has a route) and no sup cuts (no UNREACHABLE caller in this batch).
# No CALL edge is written (D7): the 15 creation records (<init>) and the lambda record (EditTransactionCommonFunctions$5.onClick -> lambda$onClick$0) are already in auto_calls.json.
# S_RECURRING_TRANSACTION_EDIT is defined once, in label_099.py (graph_def.py:8885); this batch reuses it.
# CheckingTransactionEditActivity.initializeInputControls also calls the enclosing methods (grep G2); that editor has no page key in graph_def.py (grep G8), so its GUI edges are not written here (open item).

# ---- GUI edges from the form (page -> method): the user operates the control

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$2.onClick',
    'Tap the amount field (txtAmount); opens the Calculator for the amount',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:419; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:419-432 (listener 419; onClick 421-431; Calculator.forActivity 427, show 430); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$3.onClick',
    'Tap the amount-to field (txtAmountTo) of a transfer; opens the Calculator for the destination amount',
    needs_state=state_text('the amount-to row is shown only when the transaction type is Transfer (EditTransactionCommonFunctions.java:983); the type is chosen in this editing session', ('session',)),
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:436; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:436-448 (listener 436; onClick 438-447; Calculator.forActivity 444, show 446); SRC transactions/EditTransactionCommonFunctions.java:983 (tableRowAmountTo visible for Transfer); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$4.onClick',
    'Tap the category field (categoryTextView); opens CategoryListActivity, or the split categories form when split is selected',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:459; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:459-474 (listener 459; onClick 461-473; isSplitSelected branch 462-470; CategoryListActivity intent 464-466; showSplitCategoriesForm 469); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$5.onClick',
    'Tap the payment date text (dateTextView); opens the DatePickerDialog',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:488; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:488-509 (listener 488; onClick 490-508; DatePickerDialog built 498-504; show 507); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$6.onClick',
    'Tap the previous-day button (previousDayButton)',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:511; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:511-517 (listener 511; onClick 513-516; setDate 515); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$7.onClick',
    'Tap the next-day button (nextDayButton)',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:519; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:519-525 (listener 519; onClick 521-524; setDate 523); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$8.beforeTextChanged',
    'Type in the notes field (edtNotes): the framework calls beforeTextChanged before each change (empty body)',
    via='TextWatcher added at EditTransactionCommonFunctions.java:551; TextView.sendBeforeTextChanged calls beforeTextChanged (FW-SRC TextView.java:9309-9316)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:551-567 (addTextChangedListener 551; beforeTextChanged 553-555, empty body); FW-SRC core/java/android/widget/TextView.java:9309-9316 (sendBeforeTextChanged calls beforeTextChanged at 9314); INFERRED (source not read): a keystroke reaches sendBeforeTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$8.onTextChanged',
    'Type in the notes field (edtNotes): the framework calls onTextChanged after each change (empty body)',
    via='TextWatcher added at EditTransactionCommonFunctions.java:551; TextView.sendOnTextChanged calls onTextChanged (FW-SRC TextView.java:9359-9366)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:551-567 (onTextChanged 557-560, empty body); FW-SRC core/java/android/widget/TextView.java:9359-9366 (sendOnTextChanged calls onTextChanged at 9364); FW-SRC TextView.java:5397 (sendOnTextChanged call); INFERRED (source not read): a keystroke reaches sendOnTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$8.afterTextChanged',
    'Type in the notes field (edtNotes): the framework calls afterTextChanged, which marks the form dirty and stores the notes',
    via='TextWatcher added at EditTransactionCommonFunctions.java:551; TextView.sendAfterTextChanged calls afterTextChanged (FW-SRC TextView.java:9375-9382)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:551-567 (afterTextChanged 563-566; setDirty 564; setNotes 565); FW-SRC core/java/android/widget/TextView.java:9375-9382 (sendAfterTextChanged calls afterTextChanged at 9380); FW-SRC TextView.java:5403 (sendAfterTextChanged call); INFERRED (source not read): a keystroke reaches sendAfterTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$9.onClick',
    'Tap the payee field (txtSelectPayee) in the form; opens PayeeActivity',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:571; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:571-580 (listener 571; onClick 573-579; PayeeActivity intent 574-576); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$13.beforeTextChanged',
    'Type in the transaction number field (edtTransNumber): the framework calls beforeTextChanged before each change (empty body)',
    via='TextWatcher added at EditTransactionCommonFunctions.java:672; TextView.sendBeforeTextChanged calls beforeTextChanged (FW-SRC TextView.java:9309-9316)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:672-689 (addTextChangedListener 672; beforeTextChanged 674-676, empty body); FW-SRC core/java/android/widget/TextView.java:9309-9316 (sendBeforeTextChanged calls beforeTextChanged at 9314); INFERRED (source not read): a keystroke reaches sendBeforeTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$13.onTextChanged',
    'Type in the transaction number field (edtTransNumber): the framework calls onTextChanged after each change (empty body)',
    via='TextWatcher added at EditTransactionCommonFunctions.java:672; TextView.sendOnTextChanged calls onTextChanged (FW-SRC TextView.java:9359-9366)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:672-689 (onTextChanged 679-681, empty body); FW-SRC core/java/android/widget/TextView.java:9359-9366 (sendOnTextChanged calls onTextChanged at 9364); INFERRED (source not read): a keystroke reaches sendOnTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$13.afterTextChanged',
    'Type in the transaction number field (edtTransNumber): the framework calls afterTextChanged, which marks the form dirty and stores the number',
    via='TextWatcher added at EditTransactionCommonFunctions.java:672; TextView.sendAfterTextChanged calls afterTextChanged (FW-SRC TextView.java:9375-9382)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:672-689 (afterTextChanged 684-688; setDirty 685; setTransactionNumber 687); FW-SRC core/java/android/widget/TextView.java:9375-9382 (sendAfterTextChanged calls afterTextChanged at 9380); INFERRED (source not read): a keystroke reaches sendAfterTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$14.onClick',
    'Tap the transaction number button (btnTransNumber): fills the next number from the highest existing number of the account',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:691; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:691-722 (listener 691; onClick 693-721; cursor.close 720); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$15.onClick',
    'Tap the Withdrawal, Deposit or Transfer button: sets the transaction type, marks the form dirty and redraws the controls',
    via='View.OnClickListener at EditTransactionCommonFunctions.java:755, set on the three buttons at 769, 774 and 779; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:755-787 (listener 755; onClick 757-763; setDirty 758; changeTransactionTypeTo 762; buttons 767-779); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

# ---- FRAMEWORK edges (method -> listener): the dialog that the method builds; the framework calls the listener on a button tap

e('EditTransactionCommonFunctions.onActionCancelClick', 'EditTransactionCommonFunctions$16.onClick', 'FRAMEWORK',
  'the discard-changes dialog is shown; the user taps Discard and the framework calls the positive listener, which calls cancelActivity',
  needs_state=state_text('the dialog opens only when the form has unsaved changes (getDirty at EditTransactionCommonFunctions.java:823; in-memory flag)', ('session',)),
  via='DialogInterface.OnClickListener passed to setPositiveButton at EditTransactionCommonFunctions.java:827',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:822-846 (getDirty gate 823; setPositiveButton 827; onClick 829-831; cancelActivity 830); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:125-146 (mButtonHandler sends the button message); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167 (handleMessage calls onClick at 166); INFERRED (source not read): the path from Builder.show to the button handler')

e('EditTransactionCommonFunctions.onActionCancelClick', 'EditTransactionCommonFunctions$17.onClick', 'FRAMEWORK',
  'the discard-changes dialog is shown; the user taps Keep editing and the framework calls the negative listener, which dismisses the dialog',
  needs_state=state_text('the dialog opens only when the form has unsaved changes (getDirty at EditTransactionCommonFunctions.java:823; in-memory flag)', ('session',)),
  via='DialogInterface.OnClickListener passed to setNegativeButton at EditTransactionCommonFunctions.java:833',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:822-846 (getDirty gate 823; setNegativeButton 833; onClick 835-837; dismiss 836); FW-SRC core/java/android/app/AlertDialog.java:637-639 (setNegativeButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:125-146 (mButtonHandler sends the button message); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167 (handleMessage calls onClick at 166); INFERRED (source not read): the path from Builder.show to the button handler')

e('EditTransactionCommonFunctions.onTransferSelected', 'EditTransactionCommonFunctions$18.onClick', 'FRAMEWORK',
  'the no-accounts warning is shown; the user taps OK and the framework calls the positive listener, which dismisses the dialog',
  needs_state=state_text('the warning is shown only when the destination account is not set and the account list is empty (EditTransactionCommonFunctions.java:1470-1471), and there are no split categories (1448); database and in-memory state', ('data', 'session')),
  via='DialogInterface.OnClickListener passed to setPositiveButton at EditTransactionCommonFunctions.java:1476',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1446-1488 (hasSplitCategories guard 1448; setSplit 1467; account checks 1470-1471; setPositiveButton 1476; onClick 1478-1481; dismiss 1480); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167 (handleMessage calls onClick at 166); INFERRED (source not read): the path from Builder.show to the button handler')

e('EditTransactionCommonFunctions.showSplitResetNotice', 'EditTransactionCommonFunctions$19.onClick', 'FRAMEWORK',
  'the split reset notice is shown; the user taps OK and the framework calls the positive listener, which dismisses the dialog',
  needs_state=state_text('the notice is shown only when the transaction has two or more split records (EditTransactionCommonFunctions.java:608-618, default branch of the split button)', ('data', 'session')),
  via='DialogInterface.OnClickListener passed to setPositiveButton at EditTransactionCommonFunctions.java:1539',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1535-1547 (setPositiveButton 1539; onClick 1541-1544; dismiss 1543); SRC transactions/EditTransactionCommonFunctions.java:598-627 (split button; showSplitResetNotice call at 618); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167 (handleMessage calls onClick at 166); INFERRED (source not read): the path from Builder.show to the button handler')

e('EditTransactionCommonFunctions.initTransactionNumberControls', 'EditTransactionCommonFunctions$14.onClick', 'FRAMEWORK',
  'the button is clicked by code when auto transaction numbering is on: callOnClick runs the listener without a tap',
  needs_state=state_text('auto transaction number is on (settings: BehaviourSettings.getAutoTransactionNumber) and the transaction has no id (data), EditTransactionCommonFunctions.java:724', ('settings', 'data')),
  via='View.callOnClick at EditTransactionCommonFunctions.java:725 (framework dispatch, not a user tap)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:724-726 (if not hasId and auto number; callOnClick at 725); FW-SRC core/java/android/view/View.java:6315-6322 (callOnClick calls onClick at 6318); grep G4 (no auto_calls.json record targets EditTransactionCommonFunctions$14.onClick)')

# ---- part 134 (2026-10-29)
# ================================================================== batch 134 (label_134): SplitCategoriesAdapter (with its $1-$4 listeners), SplitItemFactory, SplitItemTouchCallback, SplitItemViewHolder, SplitItemViewHolder_ViewBinding (35 methods)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_134.md (31 REACHABLE, 4 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_134.grep.txt.
# This file writes 13 e() edges (12 FRAMEWORK, 1 CALL non_standard), 0 gui() edges, 4 UNREACHABLE entries and 1 sup pair.
# Edges are written only for destinations owned by this batch (D1). Every other route is a CALL edge from auto_calls.json (USE_AUTO, D7) and is not written here.
# The route into SplitCategoriesActivity.initRecyclerView (onCreate, batch 133, not merged) is interim (D8); the RecyclerView and touch-helper edges start from initRecyclerView.
# RecyclerView and ItemTouchHelper dispatch is INFERRED: androidx is not in fw_src (label_134.grep.txt Q20, Q27), so those edges cite the setter and attach lines only.
# Listener registrations inside this batch get a FRAMEWORK edge from the registering method to the listener callback (label_131 convention). View.performClick and TextView dispatch are cited from fw_src/android-8.1.0_r1 (Q21, Q22).
# ButterKnife: the generated SplitItemViewHolder_ViewBinding.<init> is built by ButterKnife.bind(this, itemView) by reflection, so one CALL edge with cls='non_standard' is written (label_008 convention).
# onMove and onItemMove are INCOMPLETE and have no edge here: their only route is the androidx ItemTouchHelper drag path, which is not in the repo (Q20, Q27).
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1; INFERRED = a step whose source was not read.

# ---- RecyclerView setup in SplitCategoriesActivity.initRecyclerView (lines 254-274; setAdapter 259, ItemTouchHelper 271-273)

e('SplitCategoriesActivity.initRecyclerView', 'SplitCategoriesAdapter.onCreateViewHolder', 'FRAMEWORK',
  'after setAdapter the RecyclerView asks the adapter to create each row holder through onCreateViewHolder',
  evidence='SRC transactions/SplitCategoriesActivity.java:259 (mRecyclerView.setAdapter(mAdapter)); INFERRED: androidx RecyclerView dispatches onCreateViewHolder (library not in fw_src or the source root, label_134.grep.txt Q20, Q27)')

e('SplitCategoriesActivity.initRecyclerView', 'SplitCategoriesAdapter.onBindViewHolder', 'FRAMEWORK',
  'after setAdapter the RecyclerView binds each visible row through onBindViewHolder',
  evidence='SRC transactions/SplitCategoriesActivity.java:259 (mRecyclerView.setAdapter(mAdapter)); INFERRED: androidx RecyclerView dispatches onBindViewHolder (library not in fw_src or the source root, label_134.grep.txt Q20, Q27)')

e('SplitCategoriesActivity.initRecyclerView', 'SplitCategoriesAdapter.getItemCount', 'FRAMEWORK',
  'after setAdapter the RecyclerView asks the adapter for its row count through getItemCount',
  evidence='SRC transactions/SplitCategoriesActivity.java:259 (mRecyclerView.setAdapter(mAdapter)); INFERRED: androidx RecyclerView calls getItemCount (library not in fw_src or the source root, label_134.grep.txt Q20, Q27)')

e('SplitCategoriesActivity.initRecyclerView', 'SplitItemTouchCallback.getMovementFlags', 'FRAMEWORK',
  'the ItemTouchHelper attached at line 273 asks the callback for the movement flags of a touched row through getMovementFlags',
  evidence='SRC transactions/SplitCategoriesActivity.java:271-273 (new SplitItemTouchCallback, new ItemTouchHelper, attachToRecyclerView); INFERRED: androidx ItemTouchHelper calls Callback.getMovementFlags (library not in fw_src or the source root, label_134.grep.txt Q17, Q20, Q27)')

e('SplitCategoriesActivity.initRecyclerView', 'SplitItemTouchCallback.isItemViewSwipeEnabled', 'FRAMEWORK',
  'the ItemTouchHelper asks the callback whether swipe is enabled for a touched row through isItemViewSwipeEnabled',
  evidence='SRC transactions/SplitCategoriesActivity.java:271-273 (new SplitItemTouchCallback, new ItemTouchHelper, attachToRecyclerView); INFERRED: androidx ItemTouchHelper calls Callback.isItemViewSwipeEnabled (library not in fw_src or the source root, label_134.grep.txt Q17, Q20, Q27)')

e('SplitCategoriesActivity.initRecyclerView', 'SplitItemTouchCallback.onSwiped', 'FRAMEWORK',
  'the ItemTouchHelper calls onSwiped when a swipe to START or END completes',
  evidence='SRC transactions/SplitCategoriesActivity.java:271-273 (new SplitItemTouchCallback, new ItemTouchHelper, attachToRecyclerView); SRC transactions/SplitItemTouchCallback.java:45-47 (swipe flags START | END); INFERRED: androidx ItemTouchHelper calls Callback.onSwiped (library not in fw_src or the source root, label_134.grep.txt Q17, Q20, Q24, Q27)')

# ---- listeners registered in SplitCategoriesAdapter (creation and setter lines in the source; dispatch in fw_src)

e('SplitCategoriesAdapter.initAmountControl', 'SplitCategoriesAdapter$1.onClick', 'FRAMEWORK',
  'a tap on the amount view calls onClick: View.performClick calls the OnClickListener',
  evidence='SRC transactions/SplitCategoriesAdapter.java:161 (viewHolder.txtAmount.setOnClickListener), 161-176 (onClick body); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls li.mOnClickListener.onClick(this) at 6294); INFERRED: the touch path to performClick is not read (label_134.grep.txt Q21, Q23)')

e('SplitCategoriesAdapter.initCategorySelector', 'SplitCategoriesAdapter$2.onClick', 'FRAMEWORK',
  'a tap on the category view calls onClick: View.performClick calls the OnClickListener',
  evidence='SRC transactions/SplitCategoriesAdapter.java:180 (listener set on the category view), 180-187 (onClick body); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED: the touch path to performClick is not read (label_134.grep.txt Q21, Q23)')

e('SplitCategoriesAdapter.initTransactionTypeButton', 'SplitCategoriesAdapter$3.onClick', 'FRAMEWORK',
  'a tap on the transaction type button calls onClick: View.performClick calls the OnClickListener',
  evidence='SRC transactions/SplitCategoriesAdapter.java:191 (listener set on the type button), 191-206 (onClick body; setTransactionType 203; notifyItemChanged 204); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED: the touch path to performClick is not read (label_134.grep.txt Q21, Q23)')

e('SplitCategoriesAdapter.initNotesControls', 'SplitCategoriesAdapter$4.beforeTextChanged', 'FRAMEWORK',
  'the framework calls beforeTextChanged before the notes text changes: TextView.sendBeforeTextChanged calls every TextWatcher',
  evidence='SRC transactions/SplitCategoriesAdapter.java:210 (addTextChangedListener), 210-214 (empty beforeTextChanged body); FW-SRC core/java/android/widget/TextView.java:9309-9316 (sendBeforeTextChanged calls list.get(i).beforeTextChanged at 9314); INFERRED: the path from a text change to sendBeforeTextChanged is not read (label_134.grep.txt Q22, Q23)')

e('SplitCategoriesAdapter.initNotesControls', 'SplitCategoriesAdapter$4.onTextChanged', 'FRAMEWORK',
  'the framework calls onTextChanged when the notes text changes: TextView.sendOnTextChanged calls every TextWatcher',
  evidence='SRC transactions/SplitCategoriesAdapter.java:210 (addTextChangedListener), 216-219 (empty onTextChanged body); FW-SRC core/java/android/widget/TextView.java:9359-9366 (sendOnTextChanged calls the watcher at 9364); INFERRED: the path from a text change to sendOnTextChanged is not read (label_134.grep.txt Q22, Q23)')

e('SplitCategoriesAdapter.initNotesControls', 'SplitCategoriesAdapter$4.afterTextChanged', 'FRAMEWORK',
  'the framework calls afterTextChanged after the notes text changes (typing, or setText in bindNotes): TextView.sendAfterTextChanged calls every TextWatcher',
  evidence='SRC transactions/SplitCategoriesAdapter.java:210 (addTextChangedListener), 221-228 (afterTextChanged body; split.setNotes at 226), 131 (setText in bindNotes); FW-SRC core/java/android/widget/TextView.java:9375-9382 (sendAfterTextChanged calls the watcher at 9380); INFERRED: the path from a text change to sendAfterTextChanged is not read (label_134.grep.txt Q22, Q23)')

# ---- generated binding built by ButterKnife (label_008 convention; cls non_standard)

e('SplitItemViewHolder.<init>', 'SplitItemViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, itemView) constructs the generated binding for this holder',
  cls='non_standard', via='ButterKnife.bind(this, itemView) (library): the generated SplitItemViewHolder_ViewBinding is constructed by reflection (INFERRED, library and generated source not read)',
  evidence='SRC transactions/SplitItemViewHolder.java:49 (ButterKnife.bind(this, itemView)); label_134.grep.txt Q16 (ButterKnife.bind grep), Q26 E4 (decoded constructor bytecode: invokestatic ButterKnife.bind, then the result is popped); method_list entry SplitItemViewHolder_ViewBinding.<init> (label_134.grep.txt Q14); INFERRED generated class not in the source root')

# ================================================================== UNREACHABLE (batch 134)

UNREACHABLE['SplitItemFactory.<init>'] = ('no_trigger_in_app',
  'SplitItemFactory declares no constructor, so the compiler adds an implicit public no-argument constructor; the class has only the static create method, and nothing creates an instance: no new SplitItemFactory in the source root, and no class file has a Methodref to SplitItemFactory.<init> (label_134.grep.txt Q6, Q7, Q8, Q26 E1)',
  'SRC transactions/SplitItemFactory.java:30-46 (public class, no constructor; static create at 32); label_134.grep.txt Q6, Q7, Q8, Q26 E1',
  'SOURCE')

UNREACHABLE['SplitItemViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'the Unbinder returned by ButterKnife.bind(this, itemView) is discarded (the decoded bytecode of SplitItemViewHolder.<init> pops it at offset 10, label_134.grep.txt Q26 E4), no app code names unbind (label_134.grep.txt Q15), and no class file has a Methodref to unbind (Q26 E3); the generated class has no outgoing auto_calls.json records (Q1). ButterKnife calling unbind is library behaviour, not read, so this is INFERRED',
  'SRC transactions/SplitItemViewHolder.java:42-50; label_134.grep.txt Q15, Q26 E3, E4, Q1',
  'INFERRED')
