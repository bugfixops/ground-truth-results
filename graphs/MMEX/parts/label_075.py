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
