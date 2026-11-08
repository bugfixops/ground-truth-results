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
