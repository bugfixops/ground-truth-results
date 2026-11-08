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
