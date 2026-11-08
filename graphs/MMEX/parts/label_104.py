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
