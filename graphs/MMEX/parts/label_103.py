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
