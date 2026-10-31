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
