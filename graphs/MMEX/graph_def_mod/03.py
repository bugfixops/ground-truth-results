# ==================================================================
# B6 FIX-PHASE EDGES (2026-11-01) — all B6 fix ADDs and sup() calls.
# Placement note (merger): graph_def.py's tail loader execs
# graph_def_mod/*.py in name order in the same namespace, so this file
# loads AFTER 01.py/02.py. The drawer spec asked for its edges appended
# to 02.py as "last-loaded"; 03.py preserves that property (it IS the
# last-loaded module) and keeps every B6 fix edge in one auditable
# file, as the result1 spec requires. Deletions and in-place guard
# edits live in their home files (graph_def.py, graph_def_mod/01.py),
# not here. Sections below are one per fix group, in application
# order. No label changes anywhere in this file.
# ==================================================================

# ==================================================================
# B6-DRAWER: group-click / child-click partition (drawer spec)
# One variant node, MainActivity.onDrawerMenuAndOptionMenuSelected@GROUP,
# fed ONLY by MainActivity$3$1.run. The hand feeder suppresses the auto
# edge $3$1.run -> plain dispatcher (base-pair rule), so the plain
# dispatcher becomes the de-facto CHILD variant (fed only by $4$1.run).
# NO @CHILD node is created (see drawer spec B.1). The three plain
# INTENT edges below are deleted in their home files as
# partition-replacements (same dst/kind, group-only guard on @GROUP).
# ==================================================================

# Feeder (drawer spec B.2). Side effects to expect on rebuild: auto
# $3$1.run -> plain dispatcher GONE; @GROUP gains auto CALL edges to
# showFragment(Class), SyncManager, FileStorageHelper, etc.
e('MainActivity$3$1.run', 'MainActivity.onDrawerMenuAndOptionMenuSelected@GROUP', 'CALL',
  'the group-click Runnable run() calls onDrawerMenuAndOptionMenuSelected(item) with the tapped group item; this hand edge feeds only the @GROUP variant',
  evidence='SRC home/MainActivity.java:953-957 (postDelayed Runnable created at 953, run() at 955, dispatcher call at 957); SRC home/MainActivity.java:950-951 (item is the tapped group row, getGroup(groupPosition))')

# ADD 2 — Budgets (replaces deleted plain edge Ec72b7276, graph_def.py:1627).
e('MainActivity.onDrawerMenuAndOptionMenuSelected@GROUP', 'BudgetsActivity.<init>', 'INTENT',
  'case R.id.menu_budgets: startActivity(new Intent(this, BudgetsActivity.class)) — group tap only: Budgets is a group with null children, so only the group-click chain can supply menu_budgets',
  gui=['Open the navigation drawer and tap Budgets'],
  guard='the tapped group has null children (MainActivity.java:889-890) and its item id is R.id.menu_budgets (MainActivity.java:1090-1093); item id is non-null (MainActivity.java:607)',
  evidence='SRC home/MainActivity.java:654-657 (case); SRC home/MainActivity.java:936-963 (group-click chain: null-children check 941-942, group item 950-951, postDelayed Runnable 953, dispatcher call 957); SRC home/MainActivity.java:889-890 (Budgets null children); SRC home/MainActivity.java:1090-1093 (drawer item menu_budgets); SRC AndroidManifest.xml:324-326 (no intent filter)')

# ADD 3 — About (replaces deleted plain edge E1760f123, graph_def.py:199).
e('MainActivity.onDrawerMenuAndOptionMenuSelected@GROUP', 'AboutActivity.<init>', 'INTENT',
  'case R.id.menu_about: startActivity(new Intent(MainActivity.this, AboutActivity.class)) — group tap only: About is the Help group with null children, so only the group-click chain can supply menu_about',
  gui=['Open the navigation drawer and tap About'],
  guard='the tapped group has null children (MainActivity.java:927-928) and its item id is R.id.menu_about (MainActivity.java:1118-1120); item id is non-null (MainActivity.java:607)',
  evidence='SRC home/MainActivity.java:688-690 (case); SRC home/MainActivity.java:936-963 (group-click chain); SRC home/MainActivity.java:927-928 (Help null children); SRC home/MainActivity.java:1118-1120 (drawer item menu_about)')

# ADD 4 — Settings (replaces deleted plain edge Edcb3f4b6, graph_def_mod/01.py:4767;
# also carries the step-8 guard correction: item non-null + == menu_settings).
e('MainActivity.onDrawerMenuAndOptionMenuSelected@GROUP', 'SettingsActivity.<init>', 'INTENT',
  'case R.id.menu_settings: startActivity(new Intent(MainActivity.this, SettingsActivity.class)) — group tap only: Settings is a group with null children, so only the group-click chain can supply menu_settings',
  gui=['Open the navigation drawer and choose Settings'],
  guard='item id is non-null and equal to R.id.menu_settings (MainActivity.java:607, 664-665); the tapped group has null children (MainActivity.java:924-925) and its group item is menu_settings (MainActivity.java:1107)',
  evidence='SRC home/MainActivity.java:664-665 (case); SRC home/MainActivity.java:607 (null-id return); SRC home/MainActivity.java:936-963 (group-click chain); SRC home/MainActivity.java:924-925 (Settings null children); SRC home/MainActivity.java:1107 (drawer item menu_settings)')

# ADD 5 — Search (companion, NOT a replacement: plain edge graph_def_mod/01.py:3438 kept).
e('MainActivity.onDrawerMenuAndOptionMenuSelected@GROUP', 'SearchActivity.<init>', 'INTENT',
  'case R.id.menu_search_transaction: startActivity(new Intent(MainActivity.this, SearchActivity.class)) — group tap only: Search transaction is a group with null children',
  gui=['Open the navigation drawer and tap Search'],
  guard='the tapped group has null children (MainActivity.java:892-893) and its item id is R.id.menu_search_transaction (MainActivity.java:1096)',
  evidence='SRC home/MainActivity.java:658-660 (case); SRC home/MainActivity.java:936-963 (group-click chain); SRC home/MainActivity.java:892-893 (Search null children); SRC home/MainActivity.java:1096 (drawer item menu_search_transaction)')

# ADD 6 — PasswordActivity, create-database branch only (companion, NOT a
# replacement: plain shared edge graph_def.py:4279 kept). Open-database is
# deliberately excluded: the Open-database group row HAS children
# (:852-854) so a group tap returns false at :942; the menu_open_database
# item reaching the dispatcher is the "Other" CHILD row (:1152-1155),
# covered by the kept plain edge via the untouched child chain.
e('MainActivity.onDrawerMenuAndOptionMenuSelected@GROUP', 'PasswordActivity.<init>', 'INTENT',
  'case R.id.menu_create_database: startActivity(new Intent(MainActivity.this, PasswordActivity.class)) — group tap only: Create database is a group with null children',
  gui=['Open the navigation drawer and tap Create database'],
  guard='the tapped group has null children (MainActivity.java:856-857) and its item id is R.id.menu_create_database (MainActivity.java:1064)',
  evidence='SRC home/MainActivity.java:626-631 (create case: startActivity at 627, showCreateFilePicker at 629); SRC home/MainActivity.java:936-963 (group-click chain); SRC home/MainActivity.java:856-857 (Create-database null children); SRC home/MainActivity.java:1064 (drawer item menu_create_database)')

# Drawer guard corrections: hand replacements of AUTO edges (the hand edge's
# base pair suppresses the auto edge; same endpoints, only the id changes).

# About step 11 (drawer spec D.2): AboutTabAdapter.getItem -> AboutFragment.newInstance.
e('AboutTabAdapter.getItem', 'AboutFragment.newInstance', 'CALL',
  'the adapter returns AboutFragment.newInstance(position) for the first page',
  guard='position == 0 (AboutTabAdapter.java:51)',
  evidence='SRC about/AboutTabAdapter.java:51-52 (case 0 returns AboutFragment.newInstance(position)); SRC about/AboutActivity.java:45-51 (ViewPager adapter with 4 titles; first page shown)')

# About step 12 (drawer spec D.2): AboutFragment.newInstance -> AboutFragment.<init>.
e('AboutFragment.newInstance', 'AboutFragment.<init>', 'CALL',
  'newInstance constructs a fresh AboutFragment only when no cached instance exists',
  guard='mInstance == null (AboutFragment.java:55)',
  evidence='SRC about/AboutFragment.java:54-56 (newInstance: if (mInstance == null) mInstance = new AboutFragment())')

# DefinedDateRange step 16 (drawer spec D.3): LookFeelPreferenceFragment.onCreate -> DefinedDateRanges.<init>.
e('LookFeelPreferenceFragment.onCreate', 'DefinedDateRanges.<init>', 'CALL',
  'onCreate builds the DefinedDateRanges that supply the show-transactions entries',
  guard='the show-transactions ListPreference exists (non-null) (LookFeelPreferenceFragment.java:109-114: findPreference at 109-110, null check at 111, new DefinedDateRanges at 114)',
  evidence='SRC settings/LookFeelPreferenceFragment.java:109-114 (findPreference, null check, construction inside the check); SRC res/xml/preferences_look_and_feel.xml:34 (pref_show_transaction key)')

# ==================================================================
# B6-RESULT1 ROUTE 2: EditTransactionCommonFunctions.resetCategory
# (result1 spec §2; apply order: Route 2 FIRST — Route 3 reuses its
# @CHECKING chain). Plain Split chain fully partitioned: no plain path
# remains. Plain hand edges NOT in the DELETE list stay as dead edges
# (src unreachable, no BFS effect) per spec §2.3.
# ==================================================================

# sup() — partitioned auto pairs (each also suppressed by the hand
# variant edge's base pair; belt-and-braces per spec §0.2).
sup(('CheckingTransactionEditActivity.initializeInputControls', 'EditTransactionCommonFunctions.initSplitCategories'),
    ('RecurringTransactionEditActivity.initializeControls', 'EditTransactionCommonFunctions.initSplitCategories'),
    ('EditTransactionCommonFunctions$11.onClick', 'EditTransactionCommonFunctions.showSplitCategoriesForm'),
    ('EditTransactionCommonFunctions$4.onClick', 'EditTransactionCommonFunctions.showSplitCategoriesForm'),
    ('SplitCategoriesActivity.onOptionsItemSelected', 'SplitCategoriesActivity.onActionDoneClick'))

# ---- CHECKING split-button chain (sampled route) ----
e('CheckingTransactionEditActivity.initializeInputControls', 'EditTransactionCommonFunctions.initSplitCategories@CHECKING', 'CALL',
  'the Checking editor initialises the split button: initializeInputControls calls mCommon.initSplitCategories (Checking-hosted helper instance)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:351-373 (initializeInputControls; initSplitCategories at 370); variant @CHECKING: Checking host only')

e('EditTransactionCommonFunctions.initSplitCategories@CHECKING', 'EditTransactionCommonFunctions$11.onClick@CHECKING', 'FRAMEWORK',
  'the split button calls onClick on a tap: View.performClick calls the OnClickListener (Checking-hosted split button)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:599-623 (splitButton.setOnClickListener at 599; onClick body within 599-623); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED: the touch path to performClick is not read; variant @CHECKING')

e('EditTransactionCommonFunctions$11.onClick@CHECKING', 'EditTransactionCommonFunctions.showSplitCategoriesForm@CHECKING', 'CALL',
  'the split button takes the splitting branch and opens the split categories form (Checking host)',
  guard='the split button takes the splitting branch (EditTransactionCommonFunctions.java:602-605); splitting = !isSplitSelected() at 602, if (splitting) at 604, showSplitCategoriesForm at 605',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:602-605 (bytecode); variant @CHECKING: split-button entry ONLY; the category-field entry is the separate K edge below')

e('EditTransactionCommonFunctions.showSplitCategoriesForm@CHECKING', 'SplitCategoriesActivity.<init>@CHECKING', 'INTENT',
  'startActivityForResult(new Intent(getContext(), SplitCategoriesActivity.class), RequestCodes.SPLIT_TX) with the split rows, currency and transaction type as extras (Checking host)',
  gui=['Tap the split button on the transaction edit form while the transaction is not split yet'],
  guard='the split button takes the splitting branch (EditTransactionCommonFunctions.java:602-605); the editor is the Checking editor (variant @CHECKING)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1519-1528 (intent 1519; startActivityForResult 1528); FW-SRC core/java/android/app/Instrumentation.java:1170-1174; FW-SRC core/java/android/app/ActivityThread.java:2667-2671; variant @CHECKING')

e('SplitCategoriesActivity.<init>@CHECKING', 'SplitCategoriesActivity.onCreate@CHECKING', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance (Checking-started split form)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6989-7000 (performCreate calls onCreate at 6997 and 6999); variant @CHECKING')

e('SplitCategoriesActivity.onCreate@CHECKING', 'S_SPLIT_CATEGORIES@CHECKING', 'ENTERS',
  'the split categories form is shown (Checking-started)',
  evidence='SRC transactions/SplitCategoriesActivity.java:100 (setContentView R.layout.activity_split_categories); SRC res/layout/activity_split_categories.xml:68-69 (the fab view); variant @CHECKING')

e('S_SPLIT_CATEGORIES@CHECKING', 'SplitCategoriesActivity.onOptionsItemSelected@CHECKING', 'GUI',
  'the framework calls onOptionsItemSelected for the save menu item; the save item calls onActionDoneClick (Checking-started split form)',
  gui=['Tap the save (check) icon in the action bar of the split categories form'],
  guard='item.getItemId() == MenuHelper.save (SplitCategoriesActivity.java:119)',
  evidence='SRC transactions/SplitCategoriesActivity.java:112 (addSaveToolbarIcon), 117-123 (onOptionsItemSelected; MenuHelper.save at 119-120 returns onActionDoneClick); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450); INFERRED: the AppCompat dispatch from the action bar to onOptionsItemSelected is not in fw_src; variant @CHECKING')

e('SplitCategoriesActivity.onOptionsItemSelected@CHECKING', 'SplitCategoriesActivity.onActionDoneClick@CHECKING', 'CALL',
  'the save menu item calls onActionDoneClick (Checking-started split form)',
  evidence='SRC transactions/SplitCategoriesActivity.java:120 (bytecode); variant @CHECKING')

e('SplitCategoriesActivity.onActionDoneClick@CHECKING', 'CheckingTransactionEditActivity.onActivityResult', 'RESULT',
  'the split categories editor returns the splits and finishes: setResult(RESULT_OK, result) in onActionDoneClick, and the framework calls onActivityResult of the Checking editor that started it',
  guard='setResult(RESULT_OK) and finish in onActionDoneClick (SplitCategoriesActivity.java:174-175; requires every split categorised and total non-negative, :149-175); the editor was started with RequestCodes.SPLIT_TX (EditTransactionCommonFunctions.java:1511-1528)',
  evidence='SRC transactions/SplitCategoriesActivity.java:149-177 (setResult RESULT_OK at 174); SRC transactions/EditTransactionCommonFunctions.java:1511-1528; FW-SRC core/java/android/app/ActivityThread.java:4253-4266; variant @CHECKING: Checking recipient only')

# ---- RECURRING split-button chain (mirror; same texts with host substituted) ----
e('RecurringTransactionEditActivity.initializeControls', 'EditTransactionCommonFunctions.initSplitCategories@RECURRING', 'CALL',
  'the Recurring editor initialises the split button: initializeControls calls mCommon.initSplitCategories (Recurring-hosted helper instance)',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:280-304 (initializeControls; initSplitCategories at 300); variant @RECURRING: Recurring host only')

e('EditTransactionCommonFunctions.initSplitCategories@RECURRING', 'EditTransactionCommonFunctions$11.onClick@RECURRING', 'FRAMEWORK',
  'the split button calls onClick on a tap: View.performClick calls the OnClickListener (Recurring-hosted split button)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:599-623 (splitButton.setOnClickListener at 599; onClick body within 599-623); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED: the touch path to performClick is not read; variant @RECURRING')

e('EditTransactionCommonFunctions$11.onClick@RECURRING', 'EditTransactionCommonFunctions.showSplitCategoriesForm@RECURRING', 'CALL',
  'the split button takes the splitting branch and opens the split categories form (Recurring host)',
  guard='the split button takes the splitting branch (EditTransactionCommonFunctions.java:602-605); splitting = !isSplitSelected() at 602, if (splitting) at 604, showSplitCategoriesForm at 605',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:602-605 (bytecode); variant @RECURRING: split-button entry ONLY')

e('EditTransactionCommonFunctions.showSplitCategoriesForm@RECURRING', 'SplitCategoriesActivity.<init>@RECURRING', 'INTENT',
  'startActivityForResult(new Intent(getContext(), SplitCategoriesActivity.class), RequestCodes.SPLIT_TX) with the split rows, currency and transaction type as extras (Recurring host)',
  gui=['Tap the split button on the transaction edit form while the transaction is not split yet'],
  guard='the split button takes the splitting branch (EditTransactionCommonFunctions.java:602-605); the editor is the Recurring editor (variant @RECURRING)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1519-1528 (intent 1519; startActivityForResult 1528); FW-SRC core/java/android/app/Instrumentation.java:1170-1174; FW-SRC core/java/android/app/ActivityThread.java:2667-2671; variant @RECURRING')

e('SplitCategoriesActivity.<init>@RECURRING', 'SplitCategoriesActivity.onCreate@RECURRING', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance (Recurring-started split form)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6989-7000 (performCreate calls onCreate at 6997 and 6999); variant @RECURRING')

e('SplitCategoriesActivity.onCreate@RECURRING', 'S_SPLIT_CATEGORIES@RECURRING', 'ENTERS',
  'the split categories form is shown (Recurring-started)',
  evidence='SRC transactions/SplitCategoriesActivity.java:100 (setContentView R.layout.activity_split_categories); SRC res/layout/activity_split_categories.xml:68-69 (the fab view); variant @RECURRING')

e('S_SPLIT_CATEGORIES@RECURRING', 'SplitCategoriesActivity.onOptionsItemSelected@RECURRING', 'GUI',
  'the framework calls onOptionsItemSelected for the save menu item; the save item calls onActionDoneClick (Recurring-started split form)',
  gui=['Tap the save (check) icon in the action bar of the split categories form'],
  guard='item.getItemId() == MenuHelper.save (SplitCategoriesActivity.java:119)',
  evidence='SRC transactions/SplitCategoriesActivity.java:112 (addSaveToolbarIcon), 117-123 (onOptionsItemSelected; MenuHelper.save at 119-120 returns onActionDoneClick); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450); INFERRED: the AppCompat dispatch from the action bar to onOptionsItemSelected is not in fw_src; variant @RECURRING')

e('SplitCategoriesActivity.onOptionsItemSelected@RECURRING', 'SplitCategoriesActivity.onActionDoneClick@RECURRING', 'CALL',
  'the save menu item calls onActionDoneClick (Recurring-started split form)',
  evidence='SRC transactions/SplitCategoriesActivity.java:120 (bytecode); variant @RECURRING')

e('SplitCategoriesActivity.onActionDoneClick@RECURRING', 'RecurringTransactionEditActivity.onActivityResult', 'RESULT',
  'the split categories editor returns the splits and finishes: setResult(RESULT_OK, result) in onActionDoneClick, and the framework calls onActivityResult of the Recurring editor that started it',
  guard='setResult(RESULT_OK) and finish in onActionDoneClick (SplitCategoriesActivity.java:174-175; requires every split categorised and total non-negative, :149-175); the editor was started with RequestCodes.SPLIT_TX (EditTransactionCommonFunctions.java:1511-1528)',
  evidence='SRC transactions/SplitCategoriesActivity.java:149 (onActionDoneClick), 174 (setResult RESULT_OK); SRC transactions/EditTransactionCommonFunctions.java:1511-1528 (startActivityForResult with RequestCodes.SPLIT_TX at 1528); FW-SRC core/java/android/app/ActivityThread.java:4253-4266; variant @RECURRING: Recurring recipient only')

# ---- Category-field entry (Recurring page only; see spec note) ----
# The category-field listener $4.onClick (:461-473) reaches
# showSplitCategoriesForm at :469 when isSplitSelected(). Its ONLY
# page-GUI edge in the graph is from S_RECURRING_TRANSACTION_EDIT
# (mod01:5709); there is NO gui edge from S_CHECKING_TRANSACTION_EDIT
# to $4.onClick, so no Checking category variant is modelled here.
# $4's other branch (CategoryListActivity INTENT, graph_def.py:2453/2459)
# is untouched. $4's path to show@RECURRING via the Recurring page is 17
# (to $4) + 1 = 18 steps to show@RECURRING, then 27 to resetCategory —
# it cannot hijack the sampled 17-step split-button route.
e('EditTransactionCommonFunctions$4.onClick', 'EditTransactionCommonFunctions.showSplitCategoriesForm@RECURRING', 'CALL',
  'the category field takes the split branch and opens the split categories form (Recurring host, category-field entry)',
  guard='the category field takes the split branch (EditTransactionCommonFunctions.java:462-469); isSplitSelected() is true at 462, showSplitCategoriesForm at 469',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:459-473 (listener 459; onClick 461-473; isSplitSelected branch 462-470; showSplitCategoriesForm 469, reached through access$700 per auto_calls.json); variant @RECURRING: category-field entry only')

# ---- Split variant mirrors (result1 spec §2.5; 12 per host, REQUIRED) ----
# Each mirror is the plain hand edge with ONLY the src (and, for page
# edges, the page) variant-substituted; trigger, gui, guard, cls, via,
# needs_state, and evidence copied VERBATIM from the plain edge.
# Without them the 11 methods in spec §2.8 lose their only path.

# -- from SplitCategoriesActivity.onCreate@CHECKING --
e('SplitCategoriesActivity.onCreate@CHECKING', 'SplitCategoriesActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='SRC transactions/SplitCategoriesActivity.java:108-115 (onCreateOptionsMenu; addSaveToolbarIcon at 112); FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:626-633 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3392 (onCreateOptionsMenu at 3388); INFERRED: the activity extends the AppCompat base, and the AppCompat delegate path to onCreatePanelMenu is not in fw_src and was not read')

e('SplitCategoriesActivity.onCreate@CHECKING', 'SplitCategoriesActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity: ActivityThread.callCallActivityOnSaveInstanceState calls onSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:4713-4722 (callCallActivityOnSaveInstanceState); FW-SRC core/java/android/app/Instrumentation.java:1385-1386; FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState at 1496); SRC transactions/SplitCategoriesActivity.java:180-189 (body)')

e('SplitCategoriesActivity.onCreate@CHECKING', 'SplitCategoriesActivity_ViewBinding.<init>(SplitCategoriesActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for this activity, which binds the @OnClick handler and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated SplitCategoriesActivity_ViewBinding is built by reflection (INFERRED, library not read)',
  evidence='SRC transactions/SplitCategoriesActivity.java:52 (import butterknife.ButterKnife), 101 (ButterKnife.bind(this); the returned Unbinder is discarded); label_133.grep.txt G5 and G6 (build class SplitCategoriesActivity_ViewBinding.class); label_133.grep.txt auto_calls query (0 incoming records to the constructor)')

e('SplitCategoriesActivity.onCreate@CHECKING', 'ScrollAwareFABBehavior.<init>', 'FRAMEWORK',
  'setContentView inflates activity_split_categories.xml; the coordinator layout builds the FAB behaviour named in app:layout_behavior with (Context, AttributeSet)',
  evidence='SRC transactions/SplitCategoriesActivity.java:100 (setContentView(R.layout.activity_split_categories)); res/layout/activity_split_categories.xml:77 (app:layout_behavior="com.money.manager.ex.view.behaviors.ScrollAwareFABBehavior"); SRC view/behaviors/ScrollAwareFABBehavior.java:38 (constructor); INFERRED: androidx CoordinatorLayout.LayoutParams creates the behaviour by reflection, source not read',
  cls='non_standard',
  via='androidx CoordinatorLayout builds the behaviour named in app:layout_behavior by reflection (INFERRED, source not read)')

e('SplitCategoriesActivity.onCreate@CHECKING', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle of the split screen holds the split list wrapper; the first getParcelable unparcels it and the framework reads it with the CREATOR',
  guard='the restore runs only when onCreate gets a saved bundle (line 90)',
  cls='non_standard',
  via='savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION) at transactions/SplitCategoriesActivity.java:91 (the deleted list at 92); FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894',
  evidence='SRC transactions/SplitCategoriesActivity.java:82-93; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.onCreate@CHECKING', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the split list wrapper read from the split screen saved state',
  guard='the same guard as the createFromParcel edge (line 90)',
  cls='non_standard',
  via='Parcels.unwrap(savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION)) at transactions/SplitCategoriesActivity.java:91 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/SplitCategoriesActivity.java:82-93; label_071.grep.txt block F; INFERRED parceler library not read')

# -- from S_SPLIT_CATEGORIES@CHECKING --
e('S_SPLIT_CATEGORIES@CHECKING', 'SplitCategoriesActivity_ViewBinding$1.doClick', 'GUI',
  'the user taps the add button (R.id.fab): the generated @OnClick listener calls onFabClick, which adds a split row',
  gui=['Tap the add (floating action) button on the split categories form'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated SplitCategoriesActivity_ViewBinding (INFERRED: the ButterKnife library and the generated code are not read beyond the auto_calls.json record at line 36)',
  evidence='SRC transactions/SplitCategoriesActivity.java:191-194 (@OnClick(R.id.fab) onFabClick); SRC res/layout/activity_split_categories.xml:68-69 (fab id); auto_calls.json record SplitCategoriesActivity_ViewBinding$1.doClick -> SplitCategoriesActivity.onFabClick (SplitCategoriesActivity_ViewBinding.java:36)')

e('S_SPLIT_CATEGORIES@CHECKING', 'SplitCategoriesActivity$1.onClick', 'GUI',
  'the user taps OK in the invalid amount dialog: the dialog closes through dialog.dismiss',
  gui=['Tap OK in the invalid amount dialog after a negative amount was returned for a split row'],
  needs_state=state_text('a negative amount is returned from the calculator for a split row, so showInvalidAmountDialog runs (SplitCategoriesActivity.java:276-278)', ('data',)),
  evidence='SRC transactions/SplitCategoriesActivity.java:317-329 (showInvalidAmountDialog: setPositiveButton(android.R.string.ok) with the listener at 321; onClick 323-326; dismiss at 325; show at 328); SRC transactions/SplitCategoriesActivity.java:20 (import android.app.AlertDialog: the framework dialog); SRC transactions/SplitCategoriesActivity.java:276-279 (negative amount gate); FW-SRC core/java/com/android/internal/app/AlertController.java:709-710 (mButtonPositive.setOnClickListener(mButtonHandler)), 125-146 (mButtonHandler click message at 140), 160-166 (handleMessage calls the OnClickListener at 166)')

# -- from showSplitCategoriesForm@CHECKING --
e('EditTransactionCommonFunctions.showSplitCategoriesForm@CHECKING', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the split form Intent carries Parcels.wrap(splitsToShow); startActivityForResult marshals the Intent, the wrapper parcels the list, and each SplitRecurringCategory element is written through its generated writeToParcel',
  cls='non_standard',
  via='intent.putExtra(KEY_SPLIT_TRANSACTION, Parcels.wrap(splitsToShow)) at transactions/EditTransactionCommonFunctions.java:1522; getActivity().startActivityForResult at 1528; Parcel.writeParcelable calls p.writeToParcel (FW-SRC core/java/android/os/Parcel.java:1785-1791); the list wrapper element writes are parceler library code (INFERRED)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1511-1529; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

e('EditTransactionCommonFunctions.showSplitCategoriesForm@CHECKING', 'SplitRecurringCategory$$Parcelable.<clinit>', 'CALL',
  'the split form is opened with the split list: Parcels.wrap(splitsToShow) makes the library create the generated wrapper, and the first use of the class runs its static initializer, which creates SplitRecurringCategory$$Parcelable$1',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): creates SplitRecurringCategory$$Parcelable, which initialises the class',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1522 (Parcels.wrap); generated SplitRecurringCategory$$Parcelable.java is not in the source root: auto_calls.json record <clinit> -> SplitRecurringCategory$$Parcelable$1.<init> at SplitRecurringCategory$$Parcelable.java:23')

e('EditTransactionCommonFunctions.showSplitCategoriesForm@CHECKING', 'SplitRecurringCategory$$Parcelable.<init>', 'CALL',
  'the same wrap: Parcels.wrap calls the wrapper constructor with each SplitRecurringCategory element of the list',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): new SplitRecurringCategory$$Parcelable(SplitRecurringCategory)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1522; generated class not in the source root: auto_calls.json record SplitRecurringCategory$$Parcelable$1.createFromParcel -> SplitRecurringCategory$$Parcelable.<init> at SplitRecurringCategory$$Parcelable.java:28')

# -- from SplitCategoriesActivity.onActionDoneClick@CHECKING --
e('SplitCategoriesActivity.onActionDoneClick@CHECKING', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the edited split list goes back to the caller in the result Intent built with Parcels.wrap; setResult hands it to the caller, which marshals the Intent and calls writeToParcel on each wrapper',
  cls='non_standard',
  via='result.putExtra(INTENT_RESULT_SPLIT_TRANSACTION, Parcels.wrap(allSplitTransactions)) at transactions/SplitCategoriesActivity.java:172; setResult(RESULT_OK, result) at 174; FW-SRC core/java/android/os/Parcel.java:1785-1791',
  evidence='SRC transactions/SplitCategoriesActivity.java:149-175; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

# -- from SplitCategoriesActivity.onCreate@RECURRING --
e('SplitCategoriesActivity.onCreate@RECURRING', 'SplitCategoriesActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='SRC transactions/SplitCategoriesActivity.java:108-115 (onCreateOptionsMenu; addSaveToolbarIcon at 112); FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:626-633 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3392 (onCreateOptionsMenu at 3388); INFERRED: the activity extends the AppCompat base, and the AppCompat delegate path to onCreatePanelMenu is not in fw_src and was not read')

e('SplitCategoriesActivity.onCreate@RECURRING', 'SplitCategoriesActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity: ActivityThread.callCallActivityOnSaveInstanceState calls onSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:4713-4722 (callCallActivityOnSaveInstanceState); FW-SRC core/java/android/app/Instrumentation.java:1385-1386; FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState at 1496); SRC transactions/SplitCategoriesActivity.java:180-189 (body)')

e('SplitCategoriesActivity.onCreate@RECURRING', 'SplitCategoriesActivity_ViewBinding.<init>(SplitCategoriesActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for this activity, which binds the @OnClick handler and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated SplitCategoriesActivity_ViewBinding is built by reflection (INFERRED, library not read)',
  evidence='SRC transactions/SplitCategoriesActivity.java:52 (import butterknife.ButterKnife), 101 (ButterKnife.bind(this); the returned Unbinder is discarded); label_133.grep.txt G5 and G6 (build class SplitCategoriesActivity_ViewBinding.class); label_133.grep.txt auto_calls query (0 incoming records to the constructor)')

e('SplitCategoriesActivity.onCreate@RECURRING', 'ScrollAwareFABBehavior.<init>', 'FRAMEWORK',
  'setContentView inflates activity_split_categories.xml; the coordinator layout builds the FAB behaviour named in app:layout_behavior with (Context, AttributeSet)',
  evidence='SRC transactions/SplitCategoriesActivity.java:100 (setContentView(R.layout.activity_split_categories)); res/layout/activity_split_categories.xml:77 (app:layout_behavior="com.money.manager.ex.view.behaviors.ScrollAwareFABBehavior"); SRC view/behaviors/ScrollAwareFABBehavior.java:38 (constructor); INFERRED: androidx CoordinatorLayout.LayoutParams creates the behaviour by reflection, source not read',
  cls='non_standard',
  via='androidx CoordinatorLayout builds the behaviour named in app:layout_behavior by reflection (INFERRED, source not read)')

e('SplitCategoriesActivity.onCreate@RECURRING', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle of the split screen holds the split list wrapper; the first getParcelable unparcels it and the framework reads it with the CREATOR',
  guard='the restore runs only when onCreate gets a saved bundle (line 90)',
  cls='non_standard',
  via='savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION) at transactions/SplitCategoriesActivity.java:91 (the deleted list at 92); FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894',
  evidence='SRC transactions/SplitCategoriesActivity.java:82-93; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.onCreate@RECURRING', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the split list wrapper read from the split screen saved state',
  guard='the same guard as the createFromParcel edge (line 90)',
  cls='non_standard',
  via='Parcels.unwrap(savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION)) at transactions/SplitCategoriesActivity.java:91 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/SplitCategoriesActivity.java:82-93; label_071.grep.txt block F; INFERRED parceler library not read')

# -- from S_SPLIT_CATEGORIES@RECURRING --
e('S_SPLIT_CATEGORIES@RECURRING', 'SplitCategoriesActivity_ViewBinding$1.doClick', 'GUI',
  'the user taps the add button (R.id.fab): the generated @OnClick listener calls onFabClick, which adds a split row',
  gui=['Tap the add (floating action) button on the split categories form'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated SplitCategoriesActivity_ViewBinding (INFERRED: the ButterKnife library and the generated code are not read beyond the auto_calls.json record at line 36)',
  evidence='SRC transactions/SplitCategoriesActivity.java:191-194 (@OnClick(R.id.fab) onFabClick); SRC res/layout/activity_split_categories.xml:68-69 (fab id); auto_calls.json record SplitCategoriesActivity_ViewBinding$1.doClick -> SplitCategoriesActivity.onFabClick (SplitCategoriesActivity_ViewBinding.java:36)')

e('S_SPLIT_CATEGORIES@RECURRING', 'SplitCategoriesActivity$1.onClick', 'GUI',
  'the user taps OK in the invalid amount dialog: the dialog closes through dialog.dismiss',
  gui=['Tap OK in the invalid amount dialog after a negative amount was returned for a split row'],
  needs_state=state_text('a negative amount is returned from the calculator for a split row, so showInvalidAmountDialog runs (SplitCategoriesActivity.java:276-278)', ('data',)),
  evidence='SRC transactions/SplitCategoriesActivity.java:317-329 (showInvalidAmountDialog: setPositiveButton(android.R.string.ok) with the listener at 321; onClick 323-326; dismiss at 325; show at 328); SRC transactions/SplitCategoriesActivity.java:20 (import android.app.AlertDialog: the framework dialog); SRC transactions/SplitCategoriesActivity.java:276-279 (negative amount gate); FW-SRC core/java/com/android/internal/app/AlertController.java:709-710 (mButtonPositive.setOnClickListener(mButtonHandler)), 125-146 (mButtonHandler click message at 140), 160-166 (handleMessage calls the OnClickListener at 166)')

# -- from showSplitCategoriesForm@RECURRING --
e('EditTransactionCommonFunctions.showSplitCategoriesForm@RECURRING', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the split form Intent carries Parcels.wrap(splitsToShow); startActivityForResult marshals the Intent, the wrapper parcels the list, and each SplitRecurringCategory element is written through its generated writeToParcel',
  cls='non_standard',
  via='intent.putExtra(KEY_SPLIT_TRANSACTION, Parcels.wrap(splitsToShow)) at transactions/EditTransactionCommonFunctions.java:1522; getActivity().startActivityForResult at 1528; Parcel.writeParcelable calls p.writeToParcel (FW-SRC core/java/android/os/Parcel.java:1785-1791); the list wrapper element writes are parceler library code (INFERRED)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1511-1529; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

e('EditTransactionCommonFunctions.showSplitCategoriesForm@RECURRING', 'SplitRecurringCategory$$Parcelable.<clinit>', 'CALL',
  'the split form is opened with the split list: Parcels.wrap(splitsToShow) makes the library create the generated wrapper, and the first use of the class runs its static initializer, which creates SplitRecurringCategory$$Parcelable$1',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): creates SplitRecurringCategory$$Parcelable, which initialises the class',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1522 (Parcels.wrap); generated SplitRecurringCategory$$Parcelable.java is not in the source root: auto_calls.json record <clinit> -> SplitRecurringCategory$$Parcelable$1.<init> at SplitRecurringCategory$$Parcelable.java:23')

e('EditTransactionCommonFunctions.showSplitCategoriesForm@RECURRING', 'SplitRecurringCategory$$Parcelable.<init>', 'CALL',
  'the same wrap: Parcels.wrap calls the wrapper constructor with each SplitRecurringCategory element of the list',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): new SplitRecurringCategory$$Parcelable(SplitRecurringCategory)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1522; generated class not in the source root: auto_calls.json record SplitRecurringCategory$$Parcelable$1.createFromParcel -> SplitRecurringCategory$$Parcelable.<init> at SplitRecurringCategory$$Parcelable.java:28')

# -- from SplitCategoriesActivity.onActionDoneClick@RECURRING --
e('SplitCategoriesActivity.onActionDoneClick@RECURRING', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the edited split list goes back to the caller in the result Intent built with Parcels.wrap; setResult hands it to the caller, which marshals the Intent and calls writeToParcel on each wrapper',
  cls='non_standard',
  via='result.putExtra(INTENT_RESULT_SPLIT_TRANSACTION, Parcels.wrap(allSplitTransactions)) at transactions/SplitCategoriesActivity.java:172; setResult(RESULT_OK, result) at 174; FW-SRC core/java/android/os/Parcel.java:1785-1791',
  evidence='SRC transactions/SplitCategoriesActivity.java:149-175; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

# ==================================================================
# B6-RESULT1 ROUTE 1: Passcode.savePasscode (result1 spec §1)
# Partition: plain onActivityResult claims setPasscode visit-agnostically,
# but :118 fires only on the REINSERT visit (requestCode==10). The plain
# auto edge is partitioned (sup) and replaced by the @REINSERT hand edge.
# Plain RESULT E5c156fe7 (first visit) and plain INTENT E9ac9395c (first
# launch) are KEPT. Guard edits (§1.6) come in the result1 guard phase,
# after Route 3 structural (spec §4 order).
# ==================================================================

sup(('SecuritySettingsFragment.onActivityResult', 'Passcode.setPasscode'))  # auto CALL, SecuritySettingsFragment.java:118; PARTITION: plain onActivityResult claims setPasscode visit-agnostically, but :118 fires only on the REINSERT visit (requestCode==10, :109-124). Replaced by the @REINSERT hand edge below. Plain onActivityResult's other auto edges (getPasscode :141, clearPasscode :144, startActivityPasscode :132, showToast, UIHelper.<init>, Passcode.<init>) are NOT suppressed (different dsts) and stay.

e('SecuritySettingsFragment.onActivityResult', 'SecuritySettingsFragment.startActivityPasscode@REINSERT', 'CALL',
  'the INSERT branch of onActivityResult starts a second PasscodeActivity so the passcode can be re-entered: the entered passcode is stored, then startActivityPasscode is called with REQUEST_REINSERT_PASSCODE',
  guard='requestCode == REQUEST_INSERT_PASSCODE (1), resultCode == RESULT_OK and data != null (SecuritySettingsFragment.java:97-98, 103-107)',
  evidence='SRC settings/SecuritySettingsFragment.java:97-98, 103-107 (case REQUEST_INSERT_PASSCODE at 103; store at 105; startActivityPasscode at 106); variant @REINSERT: this edge is the INSERT-branch call only, not the EDIT-branch call at 132')

e('SecuritySettingsFragment.startActivityPasscode@REINSERT', 'PasscodeActivity.<init>@REINSERT', 'INTENT',
  'the second PasscodeActivity visit: startActivityPasscode builds the Intent for PasscodeActivity and calls startActivityForResult with REQUEST_REINSERT_PASSCODE',
  gui=['Re-enter the same passcode when prompted'],
  guard='request == REQUEST_REINSERT_PASSCODE (10) (SecuritySettingsFragment.java:43, passed at 106)',
  evidence='SRC settings/SecuritySettingsFragment.java:168-175 (Intent at 169; action at 171; startActivityForResult at 174); SRC settings/SecuritySettingsFragment.java:43 (REQUEST_REINSERT_PASSCODE = 10)')

e('PasscodeActivity.<init>@REINSERT', 'PasscodeActivity.onCreate@REINSERT', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor, on the second PasscodeActivity visit',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2728-2731; FW-SRC core/java/android/app/Instrumentation.java:1212-1215; FW-SRC core/java/android/app/Activity.java:6993-7000; SRC PasscodeActivity.java:82; variant @REINSERT: second visit only')

e('PasscodeActivity.onCreate@REINSERT', 'S_PASSCODE@REINSERT', 'ENTERS',
  'the passcode screen is shown a second time (onCreate sets up the digit keys and the backspace key)',
  evidence='SRC PasscodeActivity.java:82-141; variant @REINSERT: second visit only; plain S_PASSCODE is already on the path and cannot be revisited')

e('S_PASSCODE@REINSERT', 'PasscodeActivity$1.onClick@REINSERT', 'GUI',
  'tap a digit key (buttonPasscode0 to 9): the shared click listener handles the digit, on the second passcode screen',
  gui=['Tap a digit key on the passcode screen'],
  evidence='SRC PasscodeActivity.java:99, 134-141; FW-SRC core/java/android/view/View.java:6143-6144, 6289-6294; variant @REINSERT: second visit only')

e('PasscodeActivity$1.onClick@REINSERT', 'SecuritySettingsFragment.onActivityResult@REINSERT', 'RESULT',
  'the second passcode entry returns the five digits: setResult(RESULT_OK, result) and finish(), and the framework delivers the result to the fragment that called startActivityForResult',
  guard='the focused field is editTextPasscode5 (PasscodeActivity.java:116); resultCode is RESULT_OK and data is non-null (SecuritySettingsFragment.java:97-98)',
  evidence='SRC PasscodeActivity.java:99-131 (click listener, setResult at 125, finish at 126); SRC settings/SecuritySettingsFragment.java:94-175; variant @REINSERT: second result only')

e('SecuritySettingsFragment.onActivityResult@REINSERT', 'Passcode.setPasscode', 'CALL',
  'the REINSERT branch of onActivityResult saves the passcode once the re-entered passcode matches the stored one',
  guard='requestCode == REQUEST_REINSERT_PASSCODE (10), resultCode == RESULT_OK, data != null, stored passcode != null and equal to sentPasscode (SecuritySettingsFragment.java:97-98, 112, 117)',
  evidence='SRC settings/SecuritySettingsFragment.java:118 (bytecode); variant @REINSERT: this call fires only on the second visit; the plain auto edge for this pair is partitioned (see sup above)')

# PLAIN-PRESERVING hand edge (REQUIRED, spec §0.2): the hand edge to
# startActivityPasscode@REINSERT has base pair (onActivityResult,
# startActivityPasscode), which would otherwise suppress the plain auto
# edge from the EDIT branch (:132). This hand edge restores the plain
# EDIT-branch call; it does NOT restore the partitioned setPasscode call.
e('SecuritySettingsFragment.onActivityResult', 'SecuritySettingsFragment.startActivityPasscode', 'CALL',
  'the EDIT branch of onActivityResult starts PasscodeActivity to enter the previous passcode, after verifying it against the stored passcode',
  guard='requestCode == REQUEST_EDIT_PASSCODE (2), resultCode == RESULT_OK, data != null, stored passcode verified (SecuritySettingsFragment.java:126-132)',
  evidence='SRC settings/SecuritySettingsFragment.java:126-132 (EDIT branch; getPasscode at 129; startActivityPasscode at 132); plain hand duplicate of the auto record at 132, required because the @REINSERT hand edge suppresses that auto pair')

# ==================================================================
# B6-RESULT1 ROUTE 3: SplitCategoriesActivity$1.<init> (result1 spec §3)
# REUSES the Route 2 @CHECKING Split chain (§2.4) — do not duplicate it.
# Prefix steps 1-10 are Route 2's desired route; the adapter path
# branches from onCreate@CHECKING via initRecyclerView (fan-out), NOT
# from the S_SPLIT_CATEGORIES@CHECKING page. Partition: plain Calculator
# -> Split.onActivityResult deleted; the handler itself is variant-tagged
# (@AMOUNT) because plain onActivityResult -> onAmountEntered (auto :145)
# is branch-agnostic and a Category-delivered route would otherwise be a
# candidate shortest path to $1. Plain Calculator chain stays live
# (AccountEdit prefix), so no Calculator mirrors are needed.
# ==================================================================

sup(('SplitCategoriesActivity.onActivityResult', 'SplitCategoriesActivity.onAmountEntered'))  # auto CALL :145; PARTITION: plain handler claims onAmountEntered visit-agnostically, but :145 fires only in the >=1000 amount branch (:142-145). Replaced by the @AMOUNT hand edge below. Plain handler's other autos (getAmountFromResult :144, setCategoryId :137) are NOT suppressed.

e('SplitCategoriesActivity.onEvent(AmountEntryRequestedEvent)', 'CalculatorActivity.<init>@SPLIT', 'INTENT',
  'an amount-entry request event opens the calculator: Calculator.show (line 210) starts CalculatorActivity (Split-launched calculator only)',
  guard='requestCode is event.requestId + amountRequestOffset (SplitCategoriesActivity.java:207-210; amountRequestOffset = 1000 at :79)',
  evidence='SRC transactions/SplitCategoriesActivity.java:205-211 (forActivity 207, currency 208, amount 209, show 210); SRC common/Calculator.java:70 (intent for CalculatorActivity.class), 77-83 (show: startActivityForResult at 79); FW-SRC core/java/android/app/ActivityThread.java:2669-2670 (mInstrumentation.newActivity); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance() at 1174); variant @SPLIT: Split-launched calculator only; plain onEvent -> plain Calculator edge (graph_def.py:2238) is deleted')

e('CalculatorActivity.<init>@SPLIT', 'CalculatorActivity.onCreate@SPLIT', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor (Split-launched calculator)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999); variant @SPLIT')

e('CalculatorActivity.onCreate@SPLIT', 'S_CALCULATOR@SPLIT', 'ENTERS',
  'onCreate sets the layout (line 115) and wires the keys through initializeControls (line 127): the calculator screen is shown (Split-launched calculator)',
  cls='page',  # reviewed: ENTERS is a page edge; 'ButterKnife' appears only in the evidence citation of a neighbouring onCreate line (bind at 118), not in this edge's mechanism (setContentView shows the page)
  evidence='SRC common/CalculatorActivity.java:111-128 (setContentView at 115, ButterKnife.bind at 118, initializeControls at 127); variant @SPLIT')

e('S_CALCULATOR@SPLIT', 'CalculatorActivity.onEqualsClicked@SPLIT', 'GUI',
  'the equals key runs the @OnClick handler, which returns the entered amount (Split-launched calculator)',
  gui=['Tap the equals key on the calculator'],
  cls='non_standard', via='ButterKnife @OnClick(R.id.buttonKeyEqual) at CalculatorActivity.java:247, bound by the generated CalculatorActivity_ViewBinding (INFERRED: the library and generated source are not in the source root)',
  evidence='SRC common/CalculatorActivity.java:247-250 (@OnClick at 247, handler 248-250); SRC res/layout/activity_calculator.xml:162 (buttonKeyEqual); auto_calls.json record CalculatorActivity_ViewBinding$2.doClick -> onEqualsClicked (CalculatorActivity_ViewBinding.java:49) is the generated path (batch 028); INFERRED ButterKnife binding (library not read); variant @SPLIT')

e('CalculatorActivity.onEqualsClicked@SPLIT', 'CalculatorActivity.returnResult@SPLIT', 'CALL',
  'the equals key returns the entered amount (Split-launched calculator)',
  evidence='SRC common/CalculatorActivity.java:249 (bytecode); variant @SPLIT')

# PLAIN-PRESERVING hand edge (REQUIRED, spec §0.2): the hand edge above
# has base pair (onEqualsClicked, returnResult), which would otherwise
# suppress the plain auto edge at :249 and break every plain equals-key
# Calculator route (AccountEdit, Investment, Price, Search). This hand
# edge restores the plain equals-key call exactly.
e('CalculatorActivity.onEqualsClicked', 'CalculatorActivity.returnResult', 'CALL',
  'the equals key returns the entered amount (plain calculator: equals-key call)',
  cls='explicit',  # reviewed: direct bytecode CALL at :249; '@OnClick' appears only in the evidence citation of the handler's annotation, not in this edge's mechanism (the binding edge is separately non_standard)
  evidence='SRC common/CalculatorActivity.java:247-250 (@OnClick at 247, handler 248-250, returnResult at 249); plain hand duplicate of the auto record at 249, required because the @SPLIT hand edge suppresses that auto pair')

e('CalculatorActivity.returnResult@SPLIT', 'SplitCategoriesActivity.onActivityResult@AMOUNT', 'RESULT',
  'the calculator returns the amount and finishes: setResult(RESULT_OK, result), and the framework calls onActivityResult with the row request code plus the amount offset (Split-launched calculator only)',
  guard='requestCode >= amountRequestOffset (SplitCategoriesActivity.java:142) and resultCode is RESULT_OK with data non-null (SplitCategoriesActivity.java:129); the request code is the row request id plus 1000 (SplitCategoriesActivity.java:79, 207-210; Calculator.java:79 passes it to startActivityForResult)',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult: setResult(RESULT_OK) at 443, finish at 444); SRC common/Calculator.java:79 (activity.startActivityForResult(intent, requestCode)); SRC transactions/SplitCategoriesActivity.java:79 (amountRequestOffset = 1000), 207-210 (Calculator show with event.requestId + amountRequestOffset); FW-SRC core/java/android/app/ActivityThread.java:4253-4265; FW-SRC core/java/android/app/Activity.java:7259-7266; variant @SPLIT -> @AMOUNT: Split-launched amount result only')

e('SplitCategoriesActivity.onActivityResult@AMOUNT', 'SplitCategoriesActivity.onAmountEntered', 'CALL',
  'the amount branch of onActivityResult enters the returned amount for the split row (Split-launched calculator result only)',
  guard='resultCode == RESULT_OK, data != null, requestCode >= amountRequestOffset (SplitCategoriesActivity.java:129, 142)',
  evidence='SRC transactions/SplitCategoriesActivity.java:129, 142-145 (RESULT_OK + data guard at 129; amount branch at 142; onAmountEntered at 145); variant @AMOUNT: amount-branch handler only; plain auto edge for this pair is partitioned (see sup in §3.4)')

# ==================================================================
# B6-RESULT1 GUARD PHASE (result1 spec §4 step 4; §1.6, §2.6, §3.6)
# Applied after all three structural blocks. Guard/gui/evidence edits
# change edge ids (content hash) but not costs or node sequences.
# The E5c156fe7 guard edit and the merged widget-edge edit live in
# their home files (01.py/02.py), not here. This section holds only
# the §3.6 hand replacement (auto edges have no hand call to edit).
# ==================================================================

# §3.6 step 17 (hand replacement, route-neutral by construction: same
# src/dst/kind/cost as auto Ed4b0a689; only the id changes). The hand
# edge's base pair suppresses the auto edge. Simulation-untested (the
# simulation kept the auto edge) — the merger verifies the $1 node
# sequence is unchanged after rebuild.
# onAmountEntered's other auto dsts (getStorageAmount :287, setAmount
# :288) are untouched (different pairs) — the positive-amount branch
# survives.
e('SplitCategoriesActivity.onAmountEntered', 'SplitCategoriesActivity.showInvalidAmountDialog', 'CALL',
  'a negative returned amount opens the invalid amount dialog instead of updating the split row',
  guard='amount.toDouble() < 0 (SplitCategoriesActivity.java:277)',
  evidence='SRC transactions/SplitCategoriesActivity.java:276-279 (negative amount gate at 277; showInvalidAmountDialog at 278)')

# ==================================================================
# B6-RESULT2 ROUTE 2 (Split): drawer-recurring variant chain (PRIMARY)
# (result2 spec §2). Drawer item definitively GROUP (group list :1084 +
# null at the Recurring position + onGroupClick false when children
# exist, :941-942) — so the case edge is fed by the $3 group dispatcher,
# NOT $4. Complements (does not duplicate) the drawer @GROUP design:
# @GROUP covers the 5 INTENT cases; @RECURRING covers the showFragment
# CALL case. F1 and the drawer feeder share the base pair
# ($3$1.run, dispatcher) and suppress the same auto edge (redundant,
# harmless). DELETE: plain E00164e96 (mod/01.py:2917) — on the portfolio
# prefix showFragment_Internal replaces with a PortfolioFragment, so
# the plain destination cannot run; on the drawer prefix it can.
# ==================================================================

# F1 (feed) — COLLISION: base pair equals auto pair :957 (E61edcf43),
# so re-assert R2a below is mandatory.
e('MainActivity$3$1.run', 'MainActivity.onDrawerMenuAndOptionMenuSelected@RECURRING', 'CALL',
  'the drawer group tap posts the item Runnable with a 200 ms delay; the framework runs run() when the delay ends, and run() calls onDrawerMenuAndOptionMenuSelected for the recurring-transactions group item',
  guard='item != null',
  evidence='SRC home/MainActivity.java:952-957 (item null check 952; postDelayed 953; run 955; call 957); FW-SRC core/java/android/os/Handler.java:427-429, 596, 97-99, 789-790 (postDelayed -> run)')

# D2 (case edge) — COLLISION: base pair equals auto pair :652 (E30b9c1bd); re-assert R2b mandatory.
e('MainActivity.onDrawerMenuAndOptionMenuSelected@RECURRING', 'MainActivity.showFragment(Class)@RECURRING', 'CALL',
  'the recurring-transactions drawer case calls showFragment(RecurringTransactionListFragment.class)',
  guard='item id == R.id.menu_recurring_transaction',
  evidence='SRC home/MainActivity.java:651-652 (case; showFragment call)')

# D3 — COLLISION: base pair equals auto pair :751 (Eba881ea2); re-assert R2c mandatory.
e('MainActivity.showFragment(Class)@RECURRING', 'MainActivity.showFragment(Fragment)@RECURRING', 'CALL',
  'showFragment(Class) creates (or finds) the recurring-list fragment and shows it via showFragment(Fragment)',
  guard='fragmentClass != null AND resulting fragment != null',
  evidence='SRC home/MainActivity.java:734-752 (null guard 735; newInstance 743; showFragment(fragment) 751)')

# D4 — COLLISION: base pair equals auto pair :759 (E7b84acc7); re-assert R2d mandatory.
e('MainActivity.showFragment(Fragment)@RECURRING', 'MainActivity.showFragment(Fragment,String)@RECURRING', 'CALL',
  'showFragment(Fragment) shows the fragment with its class name as tag',
  evidence='SRC home/MainActivity.java:758-759')

# D5 — COLLISION: base pair equals auto pair :770 (E3a76a2a8); re-assert R2e mandatory.
e('MainActivity.showFragment(Fragment,String)@RECURRING', 'MainActivity.showFragment_Internal@RECURRING', 'CALL',
  'showFragment(Fragment,String) shows the fragment via showFragment_Internal',
  evidence='SRC home/MainActivity.java:768-770 (showFragment_Internal call 770)')

# D6 — no auto collision (auto from plain Internal goes only to isDualPanel).
e('MainActivity.showFragment_Internal@RECURRING', 'RecurringTransactionListFragment.onActivityCreated', 'FRAMEWORK',
  'the drawer item (MainActivity.java:651-652) reaches showFragment_Internal with the recurring-list fragment, which replaces fragmentMain and commits; the framework then calls onActivityCreated',
  guard='fragment not already added',
  evidence='SRC home/MainActivity.java:1446-1466 (not-added guard 1448; replace 1462; commit 1466); SRC home/MainActivity.java:651-652; INFERRED androidx FragmentManager calls onActivityCreated after the commit (library not read)')

# RE-ASSERTS (mandatory; each restores the plain pair as a hand edge
# with trigger 'Direct call' and matching 'SRC ... (bytecode)' evidence,
# so the plain graph is bit-for-bit preserved — same edge ids as the
# suppressed auto edges). Without them the plain showFragment chain
# loses its only chain incoming and hand edge E02664d9b
# (showFragment_Internal -> AccountListFragment.onActivityCreated) is
# stranded. STOP condition: verify all five plain pairs exist post-build.
e('MainActivity$3$1.run', 'MainActivity.onDrawerMenuAndOptionMenuSelected', 'CALL',
  'Direct call',
  evidence='SRC MainActivity.java:957 (bytecode)')
e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'MainActivity.showFragment(Class)', 'CALL',
  'Direct call',
  evidence='SRC MainActivity.java:652 (bytecode)')
e('MainActivity.showFragment(Class)', 'MainActivity.showFragment(Fragment)', 'CALL',
  'Direct call',
  evidence='SRC MainActivity.java:751 (bytecode)')
e('MainActivity.showFragment(Fragment)', 'MainActivity.showFragment(Fragment,String)', 'CALL',
  'Direct call',
  evidence='SRC MainActivity.java:759 (bytecode)')
e('MainActivity.showFragment(Fragment,String)', 'MainActivity.showFragment_Internal', 'CALL',
  'Direct call',
  evidence='SRC MainActivity.java:770 (bytecode)')

# ==================================================================
# B6-RESULT2 ROUTE 1: TransactionStatuses.<init> (result2 spec §1)
# DELETE: plain RESULT E99cd6390 (mod/01.py:2984) — the widget launch
# (step 3) is a PendingIntent, not startActivityForResult, so setResult
# +finish has no result recipient, and RecurringTransactionListFragment
# is never created on the widget route. Only the fragment launch
# (showCreateTransactionActivity, :437) creates a result recipient.
# Sibling RESULT edge E253e0762 (RecurringTransactionEditActivity ->
# onActivityResult, mod/01.py:2980) is UNTOUCHED (different launch).
# PREDICTED PRINTED route is NOT the 27-step RESULT route: after
# partition, cheapest BFS returns a 15-step search/all-data route (via
# AllDataListFragment.onLoadFinished -> bindView); the RESULT route
# remains valid but non-shortest. Do NOT delete real loader/bindView
# edges to force it.
# ==================================================================

# V1 — plain pair is hand edge graph_def_mod/02.py:69 (kept).
e('RecurringTransactionListFragment.showCreateTransactionActivity', 'CheckingTransactionEditActivity.<init>@FRAG', 'INTENT',
  'the recurring list creates a transaction from a scheduled one and starts the editor FOR RESULT: ACTION_INSERT with the KEY_BDID_ID extra',
  gui=['Choose the create-transaction action on a scheduled transaction in the recurring list'],
  guard='repo.load(scheduledTransactionId) != null',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:427-438 (intent 432; ACTION_INSERT 433; KEY_BDID_ID 434; startActivityForResult 437)')

# V2 — no collision (auto from plain .<init> goes only to MmxBaseFragmentActivity.<init>).
e('CheckingTransactionEditActivity.<init>@FRAG', 'CheckingTransactionEditActivity.onCreate@FRAG', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

# V3 — variant screen REQUIRED: routing through the PLAIN screen would
# leak (plain screen's GUI edge to plain onOptionsItemSelected + a new
# GUI edge to the variant handler would let the widget path reach the
# variant RESULT edge — reproduced in simulation: with a plain screen
# the widget route survived at 14 steps). No auto collision (ENTERS,
# screen dst). Build validation: base(S_...@FRAG) is the known screen;
# GUI page -> method; ENTERS ends on a page.
e('CheckingTransactionEditActivity.onCreate@FRAG', 'S_CHECKING_TRANSACTION_EDIT@FRAG', 'ENTERS',
  'the fragment-launched transaction edit form is shown',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:95 (setContentView)')

# V4
e('S_CHECKING_TRANSACTION_EDIT@FRAG', 'CheckingTransactionEditActivity.onOptionsItemSelected@FRAG', 'GUI',
  'Tap the save icon in the toolbar of the fragment-launched edit form',
  gui=['Tap the save icon in the toolbar of the fragment-launched edit form'],
  guard='item id == MenuHelper.save',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:150-159 (save case 154-155); SRC MenuHelper.java:37 (save = 2)')

# V5 — COLLISION: base pair (onOptionsItemSelected, onActionDoneClick)
# equals auto pair (bytecode :155); re-assert R1 below is mandatory.
e('CheckingTransactionEditActivity.onOptionsItemSelected@FRAG', 'CheckingTransactionEditActivity.onActionDoneClick@FRAG', 'CALL',
  'the save menu item calls onActionDoneClick',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:155')

# V6 — no collision (auto from plain onActionDoneClick goes only to saveData).
e('CheckingTransactionEditActivity.onActionDoneClick@FRAG', 'RecurringTransactionListFragment.onActivityResult', 'RESULT',
  'the fragment-launched editor saves, calls setResult(RESULT_OK) and finishes; the fragment started it at line 437 and receives the result in onActivityResult',
  guard='saveData() == true AND resultCode == RESULT_OK',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:194-197 (saveData 195; setResult 196); SRC recurring/transactions/RecurringTransactionListFragment.java:277-292 (RESULT_OK branch 280; restartLoader 290); SRC recurring/transactions/RecurringTransactionListFragment.java:427-438 (startActivityForResult 437); INFERRED androidx FragmentActivity dispatches the result to the fragment (library not read)')

# R1 (MANDATORY RE-ASSERT): restores the plain pair as a hand edge
# after V5's collision. Without R1, plain onActionDoneClick loses its
# ONLY incoming edge (built JSON confirms: its sole incoming is
# E49e398a6) and every plain-Checking save path breaks. STOP if R1
# cannot be applied: do not apply V5 alone. (Trigger as specified;
# the pair existing is the requirement, not id equality with E49e398a6.)
e('CheckingTransactionEditActivity.onOptionsItemSelected', 'CheckingTransactionEditActivity.onActionDoneClick', 'CALL',
  'the save menu item calls onActionDoneClick',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:155 (bytecode)')

# Result2 step-21 guard correction (auto edge Eba4c84fa -> hand
# replacement; same src/dst/kind, guard added, id renumbers).
e('RecurringTransactionEditActivity.saveSplitCategories', 'SplitRecurringCategoriesRepository.insert', 'CALL',
  'saveSplitCategories inserts each split category that has no id yet',
  guard='hasSplitCategories() == true AND (split item id == null OR split item id == Constants.NOT_SET)',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:571-580 (hasSplitCategories 571; if 572; loop 573; id check 578; insert 580)')

# ==================================================================
# B6-SEARCH ROUTE 1: BudgetListFragment.onLoaderReset (search spec §R1)
# SKIPPED as drawer duplicates (already applied in the drawer group):
# R1-C (feeder $3$1.run -> dispatcher@GROUP) + R1-D (@GROUP Budgets
# INTENT edge) + R1-Del2 (delete Ec72b7276). The drawer @GROUP Budgets
# edge carries the guard with the CORRECTED citation (null :889-890,
# not the search spec's :887, which is Recurring's entry — drawer spec
# + merger's own sed; citation error only, topology unaffected).
# DELETE: plain Ef021d80a (graph_def.py:1667). KEPT deliberately:
# AbsListFragment.onCreateView -> BaseListFragment.onViewCreated
# (E1543fb3c, correct for AllData) and -> CurrencyListFragment
# .onViewCreated (Eec09daf3).
# ==================================================================

# R1-A: the missing link (BudgetListFragment.onCreate has NO outgoing
# edge in the built graph; without it the Budget-instance path is dead).
e('BudgetListFragment.onCreate', 'AbsListFragment.onCreateView@BudgetListFragment', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate; BudgetListFragment defines no onCreateView, so the inherited AbsListFragment body runs on this BudgetListFragment instance (created by BudgetsActivity.createFragments)',
  evidence='SRC budget/BudgetsActivity.java:117, 121-122; SRC budget/BudgetListFragment.java:95-98, 101-105 (onCreateView commented out); SRC AbsListFragment.java:77-79; INFERRED androidx Fragment lifecycle (library source not read)')

# R1-B: receiver-partitioned delivery of onViewCreated (same text as
# the plain edge it replaces, with the receiver fixed).
e('AbsListFragment.onCreateView@BudgetListFragment', 'BudgetListFragment.onViewCreated', 'LIFECYCLE',
  'the framework calls onViewCreated after the view is created by the inherited onCreateView (AbsListFragment inflates abs_list_fragment) on this BudgetListFragment instance',
  evidence='SRC AbsListFragment.java:77-79; SRC budget/BudgetListFragment.java:119-123; INFERRED androidx Fragment lifecycle (library source not read)')

# ==================================================================
# B6-SEARCH ROUTE 2: AllDataListFragment.displayRunningBalances
# (search spec §R2). Partition starts at loadData(Bundle)@host (R2-A),
# NOT at onLoadFinished alone — simulation caught that a
# onLoadFinished-only partition still lets the Search prefix feed the
# variant chain. R2-A + R2-B + R2-C must be applied together.
# DELETE: plain E2179223e (graph_def.py:916). KEPT deliberately: plain
# loadData(Bundle) -> plain onLoadFinished (Edd70e50d) and all plain
# onLoadFinished body edges (Search-hosted AllData methods keep their
# plain path). Follow-up NOT edited (flagged, not approved): parallel
# plain forwards onCreateLoader (~:915) and onLoaderReset (:925-929)
# have the SAME host-instance defect but do not affect this target.
# ==================================================================

# R2-A: host-only feed into the child instance's loadData. NOTE (merger
# reconciliation): the spec claims the plain edge loadTransactions ->
# loadData(Bundle) (Ed8e6a9c0, auto) is "KEPT" — that is WRONG under the
# base-pair rule (R2-A's base pair equals the auto pair, so the auto is
# suppressed). The plain re-assert below restores the pair bit-for-bit
# (trigger 'Direct call' + auto evidence ':331 (bytecode)' exactly),
# preserving the spec's intent (Search-hosted AllData methods keep their
# plain path). Spec citation nit (noted, not silently corrected):
# R2-A's evidence parenthetical says "call 330" but the auto record
# puts the plain call at :331; the cited range :327-331 covers both.
e('AccountTransactionListFragment.loadTransactions', 'AllDataListFragment.loadData(Bundle)@AccountTransactionListFragment', 'CALL',
  'the account host loads its child AllData fragment: loadTransactions calls loadData(arguments) on mAllDataListFragment, the instance created in showTransactionsFragment',
  guard='mAllDataListFragment != null (AccountTransactionListFragment.java:328; set in showTransactionsFragment at :837)',
  evidence='SRC account/AccountTransactionListFragment.java:327-331 (guard 328, call 330), 834-850 (instance 837, setter 847, commit 850)')

# R2-B: loader delivery on the child instance (mirrors plain FRAMEWORK
# Edd70e50d on the variant node).
e('AllDataListFragment.loadData(Bundle)@AccountTransactionListFragment', 'AllDataListFragment.onLoadFinished@AccountTransactionListFragment', 'FRAMEWORK',
  'the loader started by restartLoader (ID_LOADER_ALL_DATA_DETAIL) on the host child instance delivers its cursor to that instance onLoadFinished',
  evidence='SRC common/AllDataListFragment.java:521-533 (restartLoader at 532); SRC common/AllDataListFragment.java:262 (onLoadFinished); INFERRED androidx LoaderManager delivers results to the callbacks (library source not read)')

# R2-C: the forward, on the host instance only.
e('AllDataListFragment.onLoadFinished@AccountTransactionListFragment', 'AccountTransactionListFragment.onLoadFinished', 'CALL',
  'the child AllData fragment forwards the loader result to its parent callbacks (the account host) at line 264',
  guard='parent != null: parent is the account host, set by setSearResultFragmentLoaderCallbacks(this) in showTransactionsFragment (AccountTransactionListFragment.java:847)',
  evidence='SRC common/AllDataListFragment.java:262-265 (forward at 264), 482-484 (getter); SRC account/AccountTransactionListFragment.java:837-850 (setter at 847); interface call, not recorded in auto_calls.json')

# R2 re-assert (merger reconciliation, see R2-A note): restores the
# plain loadTransactions -> loadData(Bundle) pair bit-for-bit (same id
# Ed8e6a9c0) after R2-A's base-pair suppression. STOP condition: verify
# Ed8e6a9c0 still exists post-build; without it Search-hosted AllData
# routes lose their plain loadData path.
e('AccountTransactionListFragment.loadTransactions', 'AllDataListFragment.loadData(Bundle)', 'CALL',
  'Direct call',
  evidence='SRC AccountTransactionListFragment.java:331 (bytecode)')

# R2 guard corrections (AUTO edges -> hand replacements in this file;
# same src/dst/kind, guard added, ids renumber — guard-only changes).
e('AccountTransactionListFragment.onLoadFinished', 'AccountTransactionListFragment.populateRunningBalance', 'CALL',
  'the loader result for the detail loader populates the running balance',
  guard='loader id == AllDataListFragment.ID_LOADER_ALL_DATA_DETAIL (AccountTransactionListFragment.java:370-375)',
  evidence='SRC account/AccountTransactionListFragment.java:370-375 (loader-id check; populateRunningBalance call at 375)')
e('AccountTransactionListFragment.onEvent', 'AllDataListFragment.displayRunningBalances', 'CALL',
  'the running-balance event shows the running balances on the child AllData fragment',
  guard='mAllDataListFragment != null (set at AccountTransactionListFragment.java:837; contrast the null-guarded use at :328)',
  evidence='SRC account/AccountTransactionListFragment.java:412 (displayRunningBalances call); SRC account/AccountTransactionListFragment.java:837 (mAllDataListFragment set)')

# ==================================================================
# B6-SEARCH ROUTE 3: Core.resolveColorAttribute (search spec §R3)
# Payee drawer item is a CHILD (childReports :896-899), so child-click
# is CORRECT here — the opposite of route 1 — and the payee case must
# live on the child variant, never @GROUP. Under the drawer design the
# payee case stays on PLAIN (which IS the child variant post-drawer),
# achieving the spec's goal (payee reachable ONLY via child origin)
# WITHOUT a @CHILD node. SKIPPED as superseded: R3-F (dispatcher@CHILD
# feeder), R3-G (payee case on @CHILD), R3-Del3 (delete E3e34477a) —
# applying R3-F would suppress auto $4$1.run -> plain dispatcher and,
# combined with the drawer feeder's suppression of $3$1.run -> plain,
# strand every plain case edge. Predicted 18-step route then uses the
# plain dispatcher (not @CHILD) at steps 5-7, same count.
# DELETE: R3-Del1 E6fab2c3b (mod/01.py:3350) + R3-Del2 E7f8589cf
# (mod/01.py:3358). KEPT deliberately: plain startLoader ->
# onCreateLoader (E3756fffc, Categories chain), plain onCreateLoader ->
# CategoriesReportFragment.onLoadFinished (Eb0a3bd39), plain onCreate ->
# CategoriesReportFragment.onActivityCreated (E643d0400), @Categories
# onActivityCreated -> plain startLoader (E057603ab). NOTE (merger
# reconciliation): R3-C SUPPRESSES auto Edf4d25c9 (@Payee
# onActivityCreated -> plain startLoader) via the receiver-variant
# exact-src rule — the spec's "kept as a side branch" language is
# superseded by the build rule; this is BENIGN (kills an unnamed
# Payee->Categories splice; Categories survives via E057603ab).
# Verify Categories methods still route post-build.
# ==================================================================

# R3-A: the missing lifecycle link (PayeeReportFragment.<init> has no
# edge to any onCreate node; mirrors CategoriesReportFragment.<init> ->
# BaseReportFragment.onCreate (E4aa92041) on the Payee variant node).
e('PayeeReportFragment.<init>', 'BaseReportFragment.onCreate@PayeeReportFragment', 'LIFECYCLE',
  'the framework calls onCreate after the constructor on this PayeeReportFragment instance (committed in PayeesReportActivity.onCreate); the body is the inherited BaseReportFragment.onCreate',
  evidence='SRC reports/PayeesReportActivity.java:46-50 (new fragment 46, add guarded by findFragmentById==null 49, commit 50); SRC reports/BaseReportFragment.java:67-72 (onCreate); INFERRED androidx Fragment lifecycle (library source not read)')

# R3-B: variant lifecycle delivery (mirrors the plain edge it replaces,
# graph_def_mod/01.py:3355-3357, with the variant src).
e('BaseReportFragment.onCreate@PayeeReportFragment', 'PayeeReportFragment.onActivityCreated', 'LIFECYCLE',
  'the fragment manager calls onActivityCreated after onCreate on this PayeeReportFragment instance (the fragment is committed in PayeesReportActivity.onCreate, line 50); the override sets the PayeeReportAdapter before calling super at line 95',
  evidence='SRC reports/PayeeReportFragment.java:63-96 (adapter 92-93, super 95); SRC reports/BaseReportFragment.java:67-72 (onCreate); SRC reports/PayeesReportActivity.java:46-50; INFERRED androidx Fragment lifecycle (library source not read)')

# R3-C: the Payee fragment's own loader start, on the variant node.
# The super call PayeeReportFragment.onActivityCreated ->
# BaseReportFragment.onActivityCreated@PayeeReportFragment already exists
# (auto CALL Ee5898424); this is its outgoing loader start.
e('BaseReportFragment.onActivityCreated@PayeeReportFragment', 'BaseReportFragment.startLoader@PayeeReportFragment', 'CALL',
  'onActivityCreated on a PayeeReportFragment receiver starts the loader with the saved instance state',
  evidence='SRC reports/BaseReportFragment.java:74-97 (onActivityCreated on a PayeeReportFragment receiver; startLoader at 97); SRC reports/PayeeReportFragment.java:95 (super call)')

# R3-D: LoaderManager restart on the Payee variant (mirrors plain
# FRAMEWORK E3756fffc on variant nodes).
e('BaseReportFragment.startLoader@PayeeReportFragment', 'BaseReportFragment.onCreateLoader@PayeeReportFragment', 'FRAMEWORK',
  'restartLoader (ID_LOADER, args, this) on a PayeeReportFragment receiver creates the loader through that receiver callbacks onCreateLoader',
  evidence='SRC reports/BaseReportFragment.java:261-263 (restartLoader with this); SRC reports/BaseReportFragment.java:115-132 (onCreateLoader); INFERRED androidx LoaderManager.restartLoader calls LoaderCallbacks.onCreateLoader (library not read)')

# R3-E: loader delivery on the Payee variant (mirrors the plain edge it
# replaces, graph_def_mod/01.py:3363-3365, with the variant src).
# Variant onCreateLoader@Payee already exists as a src
# (citation-correction keys at graph_def.py:6219-6220) but had NO
# incoming delivery edge — R3-D/R3-E supply it. Loader-id condition
# (onCreateLoader id check :118) is cited in evidence, not a guard.
e('BaseReportFragment.onCreateLoader@PayeeReportFragment', 'PayeeReportFragment.onLoadFinished', 'FRAMEWORK',
  'the loader created by startLoader (restartLoader, BaseReportFragment.java:262) delivers its cursor and the LoaderManager calls onLoadFinished on this PayeeReportFragment (the override calls super at line 130)',
  evidence='SRC reports/BaseReportFragment.java:115-132, 261-263; SRC reports/PayeeReportFragment.java:129-130; INFERRED androidx LoaderManager delivers the result to LoaderCallbacks (library not read)')

# ==================================================================
# B6-EVENT ROUTE 1: DateRange.<init> (event spec §R1)
# DELETE: plain E87fb73c0 (graph_def.py:1441) — false for fresh Bundle
# (FW-SRC Bundle.java:938-939 returns the map object without creator;
# creators run only on parcelled readback, Parcel.java:2841-2851).
# Option B rejected with proof (only new DateRange(...) is the 2-arg
# ctor, MmxDateTimeUtils.java:137; DateRange.java:29-33 shows no this()
# delegation). KEPT: fresh-path edges :1435 (getParcel) and :1442
# (writeToParcel). Variant edge kind FRAMEWORK, NOT REGISTER (REGISTER
# edges are skipped by BFS). No-revisit compliance: plain onCreate is
# visited at step 19, so the recreation uses the unvisited variant node
# onCreate@RESTORED (base() still resolves it for validation/verdicts).
# ==================================================================

e('FilterDialogFragment.onCreate', 'FilterDialogFragment.onCreate@RESTORED', 'FRAMEWORK',
  'after the dialog is shown, a FragmentManager save/restore event (e.g. configuration change) parcels the dialog arguments Bundle and restores the dialog, so the framework runs onCreate a second time on the restored instance',
  guard='the dialog was shown (AccountTransactionListFragment.java:831) and a save/restore event intervenes between the first onCreate and the restored onCreate; the restored arguments Bundle is parcelled data, not the fresh map object placed by newInstance',
  cls='non_standard',
  via='androidx FragmentManager save/restore (library source not read, INFERRED)',
  evidence='SRC account/FilterDialogFragment.java:70-77 (newInstance sets fresh arguments at 73-76), 85-86 (onCreate reads arguments); SRC account/AccountTransactionListFragment.java:830-831 (newInstance at 830, show at 831); FW-SRC core/java/android/os/Bundle.java:938-939 (unparcel then map lookup); FW-SRC core/java/android/os/Parcel.java:2841-2851 (creator.createFromParcel on parcelled readback); INFERRED androidx FragmentManager saves and restores the arguments (library not read)')
e('FilterDialogFragment.onCreate@RESTORED', 'TransactionFilter$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the restored onCreate reads the parcelled arguments with getArguments().getParcelable(ARG_TX_FILTER); unparcel reads the parcelled wrapper through its creator',
  guard='the restored arguments Bundle holds parcelled data AND the restored filter dateRange is non-null (TransactionFilter.java:33; DateRange.java:27-29), else generated read would not construct a DateRange',
  cls='non_standard',
  via='getArguments().getParcelable(ARG_TX_FILTER) at FilterDialogFragment.java:86 calls unparcel (FW-SRC core/java/android/os/Bundle.java:938-939); Parcel.readValue calls readParcelable (FW-SRC core/java/android/os/Parcel.java:2744-2745, 2841-2851), which calls creator.createFromParcel (FW-SRC core/java/android/os/Parcel.java:2851)',
  evidence='SRC account/FilterDialogFragment.java:85-86; SRC account/TransactionFilter.java:33 (public DateRange dateRange); SRC DateRange.java:27-29 (@Parcel, no-arg ctor); FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2744-2745, 2841-2851')

# R1 guard correction (AUTO edge E2207076a -> hand replacement).
e('AccountTransactionListFragment.isFilterSelected', 'AccountTransactionListFragment.showFilterDialog', 'CALL',
  'isFilterSelected calls showFilterDialog when the tapped item is the filter item',
  guard='item id == R.id.menuTransactionFilters (AccountTransactionListFragment.java:596-598)',
  evidence='SRC account/AccountTransactionListFragment.java:593-600 (call at 598); SRC account/AccountTransactionListFragment.java:237-245 (filter menu inflated at 244)')

# ==================================================================
# B6-EVENT ROUTE 2: WatchlistItemsFragment.getAccount (event spec §R2)
# PARTITION (not outright deletion — coordinator decision
# MMEX-B6-WatchlistPartition): DELETE plain Ea9af2cd3 (mod/01.py:1986)
# + ADD the @RETURNED variant edge below. The delivery itself is real
# (post :120 + @Subscribe :290-293 + registration :131); what is false
# is only the linear reading (post delivered while the currency-list
# activity is foreground and MainActivity's fragment is stopped). The
# real delivery needs return-interleaving (user returns to the
# MainActivity watchlist, fragment re-registers in onStart, BEFORE the
# Retrofit response arrives) — priced as a session needs_state, so the
# partitioned Fixer path (0,1,25) loses to onResume (0,1,20) on steps.
# Fallback (coordinator decision ONLY, NOT applied): outright deletion
# if return-interleaving is ruled out of the model. The variant edge
# must NOT be kind REGISTER (skipped by BFS). Auto CALL
# onEvent(PriceDownloadedEvent) -> onPriceDownloaded (:292) fans out
# from the variant source, so the Price tail continues with plain
# downstream nodes. No ADD needed for the own-flow path (all edges
# already exist).
# ==================================================================

# DELETION 2026-11-02 (routes 8+18 design): the @RETURNED variant edge below was DELETED (it was the partitioned form of plain Ea9af2cd3). Reason: no Fixer prefix ever creates, shows, starts, or registers a WatchlistFragment, so the Fixer post has no watchlist recipient; the Fixer post still reaches the currency list (graph_def.py:4666) and the Watchlist still receives its own security updaters' posts. History kept: the partition rationale above is superseded, not erased.

# R2 guard corrections (AUTO edges -> hand replacements).
e('WatchlistFragment.onPriceDownloaded', 'WatchlistFragment.completePriceUpdate', 'CALL',
  'onPriceDownloaded calls completePriceUpdate once every expected price has arrived',
  guard='symbol non-empty AND mUpdateCounter == mToUpdateTotal on entry to the check (WatchlistFragment.java:333, :343-345)',
  evidence='SRC investment/watchlist/WatchlistFragment.java:330-345 (early return on empty symbol at 333; counter check at 343-345; call at 345)')
e('WatchlistItemsFragment.displayHeaderData', 'WatchlistItemsFragment.getAccount', 'CALL',
  'displayHeaderData calls getAccount to fill the cash-balance header for the shown account',
  guard='accountId != Constants.NOT_SET (WatchlistItemsFragment.java:431)',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:425-439 (early return when accountId == NOT_SET at 431-434; call at 439)')

# ==================================================================
# B6-EVENT ROUTE 3: SyncPreferenceFragment.onEvent (event spec §R3)
# DELETE 3 manual edges (mod/01.py:5314 E9ec99f56 sendMessage ->
# handleMessage FRAMEWORK; :5008 E1982f6fc handleMessage -> SyncPref
# onEvent ASYNC; :741 Ef4a05204 handleMessage -> MainActivity onEvent
# ASYNC) + CUT 2 auto edges via sup() below. Union coverage: all 7 real
# sendMessage sites covered exactly once (:128/:210 DOWNLOAD; :107/:132/
# :185/:197/:217 OTHER). Deliberately NO handleMessage@OTHER -> onEvent
# edge (that absence is the fix). Known harmless residue: auto CALLs
# from plain handleMessage fan out from BOTH variant sources, leaving
# handleMessage@OTHER -> DbFileDownloadedEvent.<init> (constructor only,
# no delivery — cannot be cut with sup() since the plain pair must stay
# for @DOWNLOAD). Plain sendMessage/handleMessage nodes become
# unreachable as plain nodes, but both base methods stay REACHABLE via
# variants (first_variant). Coordinator decision MMEX-B6-SyncDrawn
# named the 11-step triggerSync DOWNLOAD path as the drawn route, but
# the actual drawn shortest path is the 10-step direct DOWNLOAD path
# (see fix_log §8 post-audit correction: that drawn path is
# message-incorrect on the SYNC prefix and the route stays WRONG in
# the table; the 11-step triggerSync remote-only branch is the valid
# non-drawn alternative, not the drawn route). The 23-step drawer route
# remains a valid guarded alternative, NOT the drawn shortest path —
# REGISTER edges are skipped by BFS by design.
# ==================================================================

sup(('SyncService.onHandleWork', 'SyncService.sendMessage'))  # E060e9c23: single auto record at :132 (UPLOAD site) over-approximates sites :107, :128, :132
sup(('SyncService.triggerSync', 'SyncService.sendMessage'))  # E87011444: single auto record at :217 (local-only UPLOAD site) over-approximates sites :185, :197, :210, :217


# DOWNLOAD branch: SYNC action, remote-modified only (SyncService.java:207-210).
e('SyncService.triggerSync', 'SyncService.sendMessage@DOWNLOAD', 'CALL',
  'triggerSync takes the remote-modified-only branch: pullDatabase, then sendMessage with DOWNLOAD_COMPLETE',
  guard='isRemoteModified AND NOT isLocalModified (SyncService.java:207-210)',
  evidence='SRC sync/SyncService.java:180-181 (isLocalModified, isRemoteModified), 207-210 (remote-only branch; pullDatabase and sendMessage DOWNLOAD_COMPLETE at 210)')

# OTHER branch: triggerSync sites that are not DOWNLOAD.
e('SyncService.triggerSync', 'SyncService.sendMessage@OTHER', 'CALL',
  'triggerSync sends a message that is not DOWNLOAD_COMPLETE: FILE_NOT_CHANGED, CONFLICT, or UPLOAD_COMPLETE',
  guard='neither-modified (FILE_NOT_CHANGED, SyncService.java:183-185) OR both-modified (CONFLICT, SyncService.java:195-197) OR local-only (UPLOAD_COMPLETE, SyncService.java:214-217)',
  evidence='SRC sync/SyncService.java:183-185 (neither-modified), 195-197 (both-modified), 214-217 (local-only; pushDatabase and sendMessage UPLOAD_COMPLETE at 217)')
# Messenger delivery, split by code identity (messenger non-null guard on both).
e('SyncService.sendMessage@DOWNLOAD', 'SyncServiceMessageHandler.handleMessage@DOWNLOAD', 'FRAMEWORK',
  'sendMessage hands a Message with what == DOWNLOAD_COMPLETE code to the caller Messenger; the framework delivers it to the handler, which parses DOWNLOAD_COMPLETE and posts DbFileDownloadedEvent',
  guard='outMessenger non-null (SyncManager.java:209-212 creates it when the caller context is an AppCompatActivity) AND msg.what == DOWNLOAD_COMPLETE code (SyncService.java:226; SyncServiceMessage.java:26)',
  evidence='SRC sync/SyncService.java:222-236 (msg.what at 226; outMessenger.send at 229); SRC sync/SyncManager.java:209-212 (Messenger created for AppCompatActivity context); SRC sync/SyncServiceMessageHandler.java:61-63 (handleMessage; parse at 62; null return at 63); FW-SRC core/java/android/os/Handler.java:97-106 (dispatchMessage calls handleMessage at 106); INFERRED android.os.Messenger (not in fw_src; not read)')
e('SyncService.sendMessage@OTHER', 'SyncServiceMessageHandler.handleMessage@OTHER', 'FRAMEWORK',
  'sendMessage hands a Message with what != DOWNLOAD_COMPLETE code to the caller Messenger; the framework delivers it to the handler, which handles that code (dialog close and/or toast) and posts nothing to DbFileDownloadedEvent subscribers',
  guard='outMessenger non-null (SyncManager.java:209-212) AND msg.what != DOWNLOAD_COMPLETE code (SyncService.java:226)',
  evidence='SRC sync/SyncService.java:222-236 (msg.what at 226; outMessenger.send at 229); SRC sync/SyncManager.java:209-212; SRC sync/SyncServiceMessageHandler.java:61-110 (switch over codes; only DOWNLOAD_COMPLETE posts at 89); FW-SRC core/java/android/os/Handler.java:97-106; INFERRED android.os.Messenger (not in fw_src; not read)')
# Posts, DOWNLOAD only (NO handleMessage@OTHER -> onEvent edge).
e('SyncServiceMessageHandler.handleMessage@DOWNLOAD', 'SyncPreferenceFragment.onEvent', 'ASYNC',
  'the sync service sends DOWNLOAD_COMPLETE to the handler (case at line 84) and the handler posts a new DbFileDownloadedEvent to EventBus (line 89); EventBus delivers it to the registered subscriber onEvent',
  guard='the subscriber is registered at delivery: SyncPreferenceFragment.onStart has run (register at SyncPreferenceFragment.java:107) and onStop has not (unregister at :114); AND the sync was started with an Activity context, so a Messenger/handler exist (SyncManager.java:209-212 creates the Messenger only when the caller context is an AppCompatActivity; SyncService.java:222-223 returns without sending when the Messenger is null) — i.e. the sync is in flight while the fragment is open because either the sync-on-start service is still running when the user opens the Sync preferences, or a menu-sync triggered in MainActivity is still in flight when the user opens the Sync preferences. Heartbeat-triggered syncs are EXCLUDED: a broadcast receiver’s context is never an AppCompatActivity, so no Messenger exists on that path (see DESIGN §2.5 item 3).',
  needs_state=state_text('the user opened the Sync preferences (SettingsFragment.java:156 -> SyncPreferencesActivity.java:37 setSettingFragment(new SyncPreferenceFragment())) and the fragment is still started, so its onStart registration (SyncPreferenceFragment.java:107) is live while an Activity-context sync (sync-on-start, or menu-sync still in flight) is in flight', ('session',)),
  env=env_text('a sync (sync-on-start, or menu-sync still in flight) whose remote file is the only modified file completes a cloud download in the sync service; it needs the network and the cloud storage', ('network',)),
  cls='non_standard',
  via='EventBus (greenrobot) post at SyncServiceMessageHandler.java:89 to the @Subscribe method onEvent(DbFileDownloadedEvent) (library dispatch, INFERRED)',
  evidence='SRC sync/SyncServiceMessageHandler.java:61 (handleMessage), 84-89 (post at 89); SRC sync/SyncPreferenceFragment.java:103-108 (register at 107), 111-114 (unregister at 114), 120-123 (@Subscribe onEvent); SRC settings/SettingsFragment.java:148-157 (SyncPreferencesActivity start at 156); SRC settings/SyncPreferencesActivity.java:34-37 (setSettingFragment at 37); SRC settings/BaseSettingsFragmentActivity.java:71-91 (transaction replace at 78, tx.commit() at 91); SRC sync/SyncManager.java:209-212 (Messenger only for AppCompatActivity context); SRC sync/SyncService.java:222-223 (null Messenger returns without sending); SRC home/MainActivity.java:1210-1224 (sync-on-start trigger at 1224), 610-616 (menu_sync trigger at 615); INFERRED EventBus library dispatch (library source not read)')
e('SyncServiceMessageHandler.handleMessage@DOWNLOAD', 'MainActivity.onEvent(DbFileDownloadedEvent)', 'ASYNC',
  'the sync service reports DOWNLOAD_COMPLETE: the handler posts DbFileDownloadedEvent, and MainActivity uses the downloaded database file',
  guard='MainActivity is still started at delivery: MmxBaseFragmentActivity.onStart has run (register at MmxBaseFragmentActivity.java:141) and onStop has not (unregister at :146); AND the sync was started with an Activity context (sync-on-start or menu-sync), so a Messenger exists (SyncManager.java:209-212). Heartbeat-triggered syncs are excluded for MainActivity too: no Messenger exists on the receiver path, so sendMessage returns without sending (SyncService.java:222-223) and no post reaches MainActivity either (see DESIGN §2.5 item 3).',
  needs_state=state_text('MainActivity is still started when the handler posts, so its MmxBaseFragmentActivity.onStart registration is live', ('session',)),
  cls='non_standard',
  via='EventBus (greenrobot) post at SyncServiceMessageHandler.java:89; subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC sync/SyncServiceMessageHandler.java:84-90 (post at 89); SRC sync/SyncService.java:125-129 (download route); SRC home/MainActivity.java:526-530 (529 useDownloadedDatabase); SRC common/MmxBaseFragmentActivity.java:134-148 (register at 141; unregister at 146); SRC sync/SyncManager.java:209-212 (Messenger only for AppCompatActivity context); SRC sync/SyncService.java:222-223 (null Messenger returns without sending); INFERRED EventBus delivery (library source not read)')

# R3 guard corrections (AUTO edges -> hand replacements; old ids retire,
# step counts unchanged). Steps 4-6 (launch-SYNC edges) + SYNC-branch
# guard on onHandleWork -> triggerSync (auto E4ee94586).
e('MainActivity.initializeSync', 'SyncManager.triggerSynchronization@MAIN', 'CALL',
  'initializeSync triggers synchronization on app start when sync is enabled',
  guard='sync active AND sync-on-start preference true AND dbUpdateCheckDone false (MainActivity.java:1212, :1222-1224)',
  evidence='SRC home/MainActivity.java:1210-1224 (early return if !sync.isActive() at 1212; trigger only if syncOnStart && !dbUpdateCheckDone at 1222-1224; call at 1224)')
e('SyncManager.triggerSynchronization', 'SyncManager.invokeSyncService@SYNC', 'CALL',
  'triggerSynchronization invokes the sync service with the SYNC action after validating paths',
  guard='sync active AND local path non-empty AND remote path non-empty (SyncManager.java:332-348)',
  evidence='SRC sync/SyncManager.java:332-348 (isActive return at 333; empty-localPath return; empty-remotePath return; invokeSyncService(INTENT_ACTION_SYNC) at 348)')

# ==================================================================
# B6-RESULT2 ROUTE 3: DatabaseManager.getContext — DECISION: FALL BACK
# TO WRONG-WITH-REASON (no graph partition applied). Full investigation
# recorded in fix_log §9 + MERGER_REPORT. Summary of why the
# caller-partition does NOT yield a correct drawn route without a
# 32-edge rework (messy; task-authorized fallback):
# - The 3-edge sketch (showCurrent -> @MAIN dead-end + backup ->
#   @BACKUP -> plain tail) leaves 6 contradicted env-free callers on
#   plain; BFS would pick triggerSync/initializeSync (0,0,9),
#   contradicted — still wrong.
# - Full fix needs: 6 dead-ends (showCurrent, createDefaultEntry,
#   createWelcomeView, onOpenDatabaseClick, useDownloadedDatabase,
#   createDbInstance) + triggerSync prefix-partition (4 MainActivity
#   feeders -> @MAIN + 10 mirrors + 10 re-asserts, because mirrors
#   suppress plain outs) + backup feeding variant = ~32 edges, with
#   blast risk to the sync subtree. Caller list is MESSY (6 uniformly
#   contradicted + 1 mixed caller) — fallback criterion met.
# - The printed 8-step MainActivity route stays WRONG at step 5 (J10
#   guard-contradiction proof); the backup (1,0,7) and broadcast
#   (0,1,11) prefixes remain VALID non-shortest alternatives,
#   documented in the final table, not drawn.
# Guards below (result2 §3(f)) apply REGARDLESS of the decision (task
# order step 6): they make the step-3/step-5 contradiction EXPLICIT in
# the edge text. All three are AUTO edges -> hand replacements here
# (same src/dst/kind, guard added, ids renumber; routes unchanged).
# ==================================================================

# Step 3 (retained edge Ec1f7c9c2).
e('MainActivity.onCreate', 'MainActivity.showCurrentDatabasePath', 'CALL',
  'onCreate shows the current database path after the prerequisite check passes',
  guard='!showPrerequisite() (home/MainActivity.java:184-187; definition :1478-1499)',
  evidence='SRC home/MainActivity.java:184-187 (prerequisite gate; finish + return if true), 223 (showCurrentDatabasePath call); SRC home/MainActivity.java:1478-1499 (showPrerequisite definition)')
# Step 5 (retained edge E12cf38a6). This guard CONTRADICTS the step-3
# guard on the MainActivity prefix (file exists at :184, nothing between
# :184 and :223 removes it) and is satisfiable on the backup/broadcast
# prefixes — the contradiction is the wrong-with-reason proof.
e('DatabaseManager.getDatabasePath', 'DatabaseManager.getDefaultDatabasePath', 'CALL',
  'getDatabasePath falls through to the default path when no stored database is usable',
  guard='stored database path is empty OR its file does not exist (core/database/DatabaseManager.java:44-49 early return; fall-through call :54)',
  evidence='SRC DatabaseManager.java:44-54 (early return when stored path non-empty and file exists :44-49; fall-through call :54)')
# Step 7 (retained edge Ed1acc672).
e('DatabaseManager.getDefaultDatabaseDirectory', 'DatabaseManager.getPackageDirectory', 'CALL',
  'getDefaultDatabaseDirectory falls back to the package directory when no external storage directory is available',
  guard='getDbExternalStorageDirectory() == null AND getExternalFilesDirectory() == null (core/database/DatabaseManager.java:90-94; call :97)',
  evidence='SRC DatabaseManager.java:90-97 (external lookups :90-94; getPackageDirectory call :97)')

# ==================================================================
# B6 GUARD GROUP: 46-recorded-corrections pass, applied LAST (after all
# structural groups, so no helper blast-radius grep is invalidated).
# SCOPE (see fix_log §10 for the full accounting): the 19 guard
# corrections for the 6 FIXED routes (J8 route 24, J9 routes 25-27, J10
# routes 28 + 30 — extracted EXACTLY from b6-j8/j9/j10 JUDGMENTS.md),
# PLUS 3 verified extras for still-existing unguarded edges (E346a1795,
# E87646b1f, E303c403e). All are topology-safe (same src/dst/kind/cost;
# only ids change). The "46" first-draw fixed-step total includes steps
# on WRONG/UNCLEAR routes whose edges were deleted, partitioned, or
# already guard-corrected by the structural specs (drawer/result1/
# result2/search/event/getContext §9) — those are NOT re-applied here
# (moot or already covered); contested Ec1f72a40 (judgments disagree:
# correct vs fixed) is NOT applied. The redraw judging wave verdicts
# any remaining fixed steps fresh.
# All edges below are AUTO (trigger 'Direct call' in the built graph)
# -> hand replacements here (base-pair suppression of the auto edge).
# ==================================================================

# J8 route 24 step 5 (E8d177cd8).
e('CurrencyService.getCurrencyFormatted', 'FormatUtilities.format(Money,Currency)', 'CALL',
  'getCurrencyFormatted formats the value with the currency for the given id',
  guard='getCurrency(currencyId) non-null (CurrencyService.java:297-309; null yields value.toString() at :301-303 / String.valueOf at :312, format call only at :309)',
  evidence='SRC currency/CurrencyService.java:297-309 (currencyId null check :297, getCurrency :298, null returns :301-303, format call :309)')
# J8 route 24 step 7 (E646649f4).
e('FormatUtilities.format(Money,boolean,Currency)', 'FormatUtilities.format(Money,int,String,String)', 'CALL',
  'format forwards to the scale/pattern overload with the currency',
  guard='currency non-null (FormatUtilities.java:157; null returns "n/a")',
  evidence='SRC FormatUtilities.java:157-160 (null check :157, forwarding call :159-160)')
# J9 route 25 step 4 (E01dadb8d).
e('SingleAccountWidget.updateAppWidget', 'SingleAccountWidget.displayAccountInfo', 'CALL',
  'updateAppWidget shows the account info for the configured default account',
  guard='defaultAccountId != null (SingleAccountWidget.java:174)',
  evidence='SRC widget/SingleAccountWidget.java:171-176 (settings lookup :172, null check :174, displayAccountInfo call :176)')
# J9 route 25 step 7 (E77e56ae9).
e('AccountRepository.load', 'AccountRepository.first', 'CALL',
  'load returns the first account matching the where clause for the given id',
  guard='id != Constants.NOT_SET (AccountRepository.java:52; NOT_SET = -1)',
  evidence='SRC datalayer/AccountRepository.java:51-57 (load :51, NOT_SET early return :52, first call :57)')
# J9 route 26 step 4 (E7df96df4).
e('MainActivity.populateScheduledTransactions', 'RecurringTransactionRepository.load', 'CALL',
  'populateScheduledTransactions loads each due scheduled transaction to show its notification',
  guard='isScheduledTransactionStarted == false on entry AND behaviour setting getNotificationRecurringTransaction() == true AND the QueryBillDeposits cursor is non-null AND cursor.moveToNext() == true (at least one bill with DAYSLEFT <= 0) (MainActivity.java:1234-1248, :1259, :1261)',
  evidence='SRC home/MainActivity.java:1231-1264 (showNotification flag :1233-1236, early return :1248, cursor query :1254-1258, null return :1259, moveToNext loop :1261, load call :1264)')
# J9 route 26 step 5 (E13c469c9).
e('RecurringTransactionRepository.load', 'RecurringTransactionRepository.first', 'CALL',
  'load returns the first bill deposit matching the where clause for the given id',
  guard='id != Constants.NOT_SET (RecurringTransactionRepository.java:64; NOT_SET = -1)',
  evidence='SRC datalayer/RecurringTransactionRepository.java:63-69 (load :63, NOT_SET early return :64, first call :69)')
# J9 route 26 step 10 (Ee4aac71b).
e('MmxContentProvider.query_internal', 'MmxContentProvider.prepareQuery', 'CALL',
  'query_internal prepares the query for a dataset source',
  guard='openHelper readable database != null AND getObjectFromUri(uri) instanceof Dataset (MmxContentProvider.java:385-388, :393)',
  evidence='SRC MmxContentProvider.java:372-395 (query_internal :372, getObjectFromUri :380, readable database :384, null return :385-388, instanceof check :393, prepareQuery call :395)')
# J9 route 27 step 4 (Ece9412e4; same populate guard as route 26 step 4).
e('MainActivity.populateScheduledTransactions', 'RecurringTransactionService.moveNextOccurrence', 'CALL',
  'populateScheduledTransactions moves each due scheduled transaction to its next occurrence',
  guard='isScheduledTransactionStarted == false on entry AND behaviour setting getNotificationRecurringTransaction() == true AND the QueryBillDeposits cursor is non-null AND cursor.moveToNext() == true (at least one bill with DAYSLEFT <= 0) (MainActivity.java:1234-1248, :1259, :1261)',
  evidence='SRC home/MainActivity.java:1234-1248, :1254-1261 (same guarded loop as route 26 step 4), :1281-1282 (service construction + moveNextOccurrence call)')
# J9 route 27 step 5 (E3ab2d8d8).
e('RecurringTransactionService.moveNextOccurrence', 'RecurringTransactionRepository.update', 'CALL',
  'moveNextOccurrence saves the recurring transaction with its next occurrence date',
  guard='getRecurringTransaction() != null AND tx.getRecurrenceInt() != null AND Recurrence.valueOf(recurrenceType) != null AND recurrence != ONCE (RecurringTransactionService.java:178-203)',
  evidence='SRC servicelayer/RecurringTransactionService.java:176-240 (moveNextOccurrence :176, null throws :178-186, valueOf null throw :192-196, ONCE delete + return :200-203, update call :240)')
# J9 route 27 step 9 (E1fba06fc).
e('MmxContentProvider.update', 'MmxContentProvider.logUpdate', 'CALL',
  'update logs the change for a table dataset',
  guard='getObjectFromUri(uri) instanceof Dataset AND dataset.getType() == DatasetType.TABLE (MmxContentProvider.java:202, :204)',
  evidence='SRC MmxContentProvider.java:191-205 (update :191, getObjectFromUri :194, instanceof check :202, TABLE check :204, logUpdate call :205)')
# J10 route 28 step 3 (E4b075bc9). Joint condition with step 4: only a
# stored EMPTY (non-null) UID satisfies both steps (null fails step 4's
# exists check; non-empty fails step 3) — recorded in the route table,
# not by narrowing this edge's guard (the judgment's exact guard text
# is kept verbatim).
e('MainActivity.onCreate', 'InfoService.setInfoValue', 'CALL',
  'onCreate generates and stores a UID for this install when none is set',
  guard='!showPrerequisite() (MainActivity.java:184-187) AND (uid == null OR uid.isEmpty()) where uid = getInfoValue(UID) (MainActivity.java:228-233)',
  evidence='SRC home/MainActivity.java:184-187 (prerequisite gate), 226-233 (UID read :228, setInfoValue call :233); SRC servicelayer/InfoService.java:139 (exists check)')
# J10 route 28 step 4 (E92362eb1).
e('InfoService.setInfoValue', 'InfoRepositorySql.update', 'CALL',
  'setInfoValue updates the existing info row for the key',
  guard='exists, i.e. getInfoValue(key) != null (InfoService.java:139, :144-145)',
  evidence='SRC servicelayer/InfoService.java:139 (exists assignment), :144-145 (if (exists) update call)')
# J10 route 28 step 6 (Ee62bd7f4).
e('SqlRepositoryBase.update', 'SqlRepositoryBase.notifySync', 'CALL',
  'update notifies sync listeners when a row was actually changed',
  guard='updateResult != 0 (SqlRepositoryBase.java:117-118)',
  evidence='SRC datalayer/SqlRepositoryBase.java:110-118 (database.update :110-115, result check :117, notifySync call :118)')
# J10 route 28 step 8 (Ecd227379).
e('SyncManager.dataChanged', 'SyncPreferences.getUploadImmediately', 'CALL',
  'dataChanged checks whether an immediate upload is configured',
  guard='isSyncEnabled() (SyncManager.java:131) AND !TextUtils.isEmpty(getRemotePath()) (:134-135) AND !mAutoUploadDisabled (:141) AND canSync() (:142-145)',
  evidence='SRC sync/SyncManager.java:131-149 (isSyncEnabled :131, remote check :134-135, auto-upload flag :141, canSync :142-145, getUploadImmediately call :149)')
# J10 route 30 step 3 (Ee3d2a3b0). Already-configured-database +
# intent-file case, NOT cold-start (J10 compatibility note: cold-start
# fails showPrerequisite and never reaches handleIntent).
e('MainActivity.onCreate', 'MainActivity.handleIntent', 'CALL',
  'onCreate handles the launch intent after the prerequisite check passes',
  guard='!showPrerequisite() (MainActivity.java:184-187; tutorial not needed and a database available)',
  evidence='SRC home/MainActivity.java:184-187 (prerequisite gate), 210 (handleIntent call)')
# J10 route 30 step 4 (Ebb8946c0).
e('MainActivity.handleIntent', 'MainActivity.changeDatabase', 'CALL',
  'handleIntent switches to the database named by the launch intent file URI',
  guard='intent != null (MainActivity.java:1186) AND intent.getData() != null (:1189) AND no exception from URLDecoder.decode / DatabaseMetadataFactory.getInstance (:1192-1198)',
  evidence='SRC home/MainActivity.java:1186-1202 (intent null check :1186, getData check :1189, try block :1192-1200, exception path :1201-1202)')
# J10 route 30 step 6 (Ebbe1d06e).
e('MmxDatabaseUtils.useDatabase', 'MmexApplication.initDb', 'CALL',
  'useDatabase initializes the app database instance for a valid database file',
  guard='isValidDbFile(database.localPath) (MmxDatabaseUtils.java:204-206; definition :78-89: file exists, name ends .mmb or .emb, readable, writable) AND recent-databases add succeeds (:213-215)',
  evidence='SRC utils/MmxDatabaseUtils.java:202-219 (validity check :204-206, add :213-215, initDb call :219)')
# Extra: HomeFragment account-bills loader guard (E303c403e; judged
# fixed in the HomeFragment route judgment; still-existing AUTO edge).
e('HomeFragment.onLoadFinished', 'HomeFragment.renderAccountsList', 'CALL',
  'onLoadFinished renders the account list for the account-bills loader result',
  guard='loader.getId() == LOADER_ACCOUNT_BILLS (HomeFragment.java:288-291)',
  evidence='SRC home/HomeFragment.java:287-291 (loader-id switch :287-288, LOADER_ACCOUNT_BILLS branch :288-291, renderAccountsList call :291)')
# D-G7 correction (post-audit): the 46th first-draw fixed-step instance,
# unaccounted in the §10 reconciliation above (b6-j2 route 3,
# SqlRepositoryBase.first, step 14). AUTO edge E6ec96bae (Watchlist
# $4.onClick -> MorningstarPriceUpdater.downloadPrices, guard None) ->
# hand replacement here (base-pair suppression of the auto edge).
# The Yahoo sibling edges from the same onClick stay unguarded: they
# are separate dispatch targets, and this guard applies to the
# Morningstar target only.
e('WatchlistFragment$4.onClick', 'MorningstarPriceUpdater.downloadPrices', 'CALL',
  'the watchlist price-update dialog calls the configured security price updater; the Morningstar implementation runs only when Morningstar is the configured quote provider',
  guard='InvestmentSettings.getQuoteProvider() == QuoteProviders.Morningstar (SecurityPriceUpdaterFactory.java:38-42: getQuoteProvider at :38, switch at :40, Morningstar branch :41-42)',
  evidence='SRC investment/SecurityPriceUpdaterFactory.java:38-42 (getQuoteProvider :38; switch :40; Morningstar branch :41-42); SRC investment/watchlist/WatchlistFragment.java:472-474 (getUpdaterInstance :472-473; interface downloadPrices call :474)')

# B6-RESULT: InvestmentTransactionEditActivity calculator partitioned to
# @NUM_SHARES / @PURCHASE_PRICE / @COMMISSION / @CURRENT_PRICE (routes 8+18
# design 2026-11-02). The plain RESULT edge (01.py) and the four plain INTENT
# edges (graph_def.py) are deleted with this section; the four chains below
# are the only ITEA calculator paths. Plain equals-key routes (AccountEdit,
# PriceEdit, Checking, Search) keep the plain edge at 03.py:463.
e('InvestmentTransactionEditActivity.onNumSharesClick', 'CalculatorActivity.<init>@NUM_SHARES', 'INTENT',
  'the num shares field opens the calculator: Calculator.show starts CalculatorActivity (NUM_SHARES-launched calculator only)',
  guard='the launch uses REQUEST_NUM_SHARES (= 1) (InvestmentTransactionEditActivity.java)',
  cls='standard',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:211-219 (@OnClick at 211; forActivity 215, amount 216, roundToCurrency 217, show 218); SRC common/Calculator.java:70 (intent for CalculatorActivity.class), 77-83 (show: startActivityForResult at 79); FW-SRC core/java/android/app/ActivityThread.java:2669-2670 (mInstrumentation.newActivity); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance() at 1174); variant @NUM_SHARES')
e('CalculatorActivity.<init>@NUM_SHARES', 'CalculatorActivity.onCreate@NUM_SHARES', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor (NUM_SHARES-launched calculator)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999); variant @NUM_SHARES')
e('CalculatorActivity.onCreate@NUM_SHARES', 'S_CALCULATOR@NUM_SHARES', 'ENTERS',
  'onCreate sets the layout (line 115) and wires the keys through initializeControls (line 127): the calculator screen is shown (NUM_SHARES-launched calculator)',
  cls='page',
  evidence='SRC common/CalculatorActivity.java:111-128 (setContentView at 115, ButterKnife.bind at 118, initializeControls at 127); variant @NUM_SHARES')
e('S_CALCULATOR@NUM_SHARES', 'CalculatorActivity.onEqualsClicked@NUM_SHARES', 'GUI',
  'the equals key runs the @OnClick handler, which returns the entered amount (NUM_SHARES-launched calculator)',
  gui=['Tap the equals key on the calculator'],
  cls='non_standard', via='ButterKnife @OnClick(R.id.buttonKeyEqual) at CalculatorActivity.java:247, bound by the generated CalculatorActivity_ViewBinding (INFERRED: the library and generated source are not in the source root)',
  evidence='SRC common/CalculatorActivity.java:247-250 (@OnClick at 247, handler 248-250); SRC res/layout/activity_calculator.xml:162 (buttonKeyEqual); auto_calls.json record CalculatorActivity_ViewBinding$2.doClick -> onEqualsClicked (CalculatorActivity_ViewBinding.java:49) is the generated path (batch 028); INFERRED ButterKnife binding (library not read); variant @NUM_SHARES')
e('CalculatorActivity.onEqualsClicked@NUM_SHARES', 'CalculatorActivity.returnResult@NUM_SHARES', 'CALL',
  'the equals key returns the entered amount (NUM_SHARES-launched calculator)',
  evidence='SRC common/CalculatorActivity.java:249 (bytecode); variant @NUM_SHARES')
e('CalculatorActivity.returnResult@NUM_SHARES', 'InvestmentTransactionEditActivity.onActivityResult@NUM_SHARES', 'RESULT',
  'the calculator returns the amount and finishes: setResult(RESULT_OK) at 443, finish at 444, and the framework delivers the result to the editor that started it (NUM_SHARES-launched calculator only)',
  guard='requestCode is REQUEST_NUM_SHARES (= 1) and resultCode is RESULT_OK with data non-null (InvestmentTransactionEditActivity.java:119-158; cancelled or null-data early return at 123; NUM_SHARES branch at 128-132: mStock.setNumberOfShares at 129, showNumberOfShares at 130)',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult: setResult(RESULT_OK) at 443, finish at 444); SRC common/Calculator.java:79 (activity.startActivityForResult(intent, requestCode)); SRC investment/InvestmentTransactionEditActivity.java:119-158 (onActivityResult; Calculator.getAmountFromResult at 125; switch on the four request codes); FW-SRC core/java/android/app/ActivityThread.java:4253-4265; FW-SRC core/java/android/app/Activity.java:7259-7266; variant @NUM_SHARES')
e('InvestmentTransactionEditActivity.onPurchasePriceClick', 'CalculatorActivity.<init>@PURCHASE_PRICE', 'INTENT',
  'the purchase price field opens the calculator: Calculator.show starts CalculatorActivity (PURCHASE_PRICE-launched calculator only)',
  guard='mAccount is not null (InvestmentTransactionEditActivity.java:223 returns early when it is null); the launch uses REQUEST_PURCHASE_PRICE (= 2) (InvestmentTransactionEditActivity.java)',
  cls='standard',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:221-230 (@OnClick at 221; guard 223; forActivity 225, roundToCurrency 226, amount 227, currency 228, show 229); SRC common/Calculator.java:70 (intent for CalculatorActivity.class), 77-83 (show: startActivityForResult at 79); FW-SRC core/java/android/app/ActivityThread.java:2669-2670 (mInstrumentation.newActivity); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance() at 1174); variant @PURCHASE_PRICE')
e('CalculatorActivity.<init>@PURCHASE_PRICE', 'CalculatorActivity.onCreate@PURCHASE_PRICE', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor (PURCHASE_PRICE-launched calculator)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999); variant @PURCHASE_PRICE')
e('CalculatorActivity.onCreate@PURCHASE_PRICE', 'S_CALCULATOR@PURCHASE_PRICE', 'ENTERS',
  'onCreate sets the layout (line 115) and wires the keys through initializeControls (line 127): the calculator screen is shown (PURCHASE_PRICE-launched calculator)',
  cls='page',
  evidence='SRC common/CalculatorActivity.java:111-128 (setContentView at 115, ButterKnife.bind at 118, initializeControls at 127); variant @PURCHASE_PRICE')
e('S_CALCULATOR@PURCHASE_PRICE', 'CalculatorActivity.onEqualsClicked@PURCHASE_PRICE', 'GUI',
  'the equals key runs the @OnClick handler, which returns the entered amount (PURCHASE_PRICE-launched calculator)',
  gui=['Tap the equals key on the calculator'],
  cls='non_standard', via='ButterKnife @OnClick(R.id.buttonKeyEqual) at CalculatorActivity.java:247, bound by the generated CalculatorActivity_ViewBinding (INFERRED: the library and generated source are not in the source root)',
  evidence='SRC common/CalculatorActivity.java:247-250 (@OnClick at 247, handler 248-250); SRC res/layout/activity_calculator.xml:162 (buttonKeyEqual); auto_calls.json record CalculatorActivity_ViewBinding$2.doClick -> onEqualsClicked (CalculatorActivity_ViewBinding.java:49) is the generated path (batch 028); INFERRED ButterKnife binding (library not read); variant @PURCHASE_PRICE')
e('CalculatorActivity.onEqualsClicked@PURCHASE_PRICE', 'CalculatorActivity.returnResult@PURCHASE_PRICE', 'CALL',
  'the equals key returns the entered amount (PURCHASE_PRICE-launched calculator)',
  evidence='SRC common/CalculatorActivity.java:249 (bytecode); variant @PURCHASE_PRICE')
e('CalculatorActivity.returnResult@PURCHASE_PRICE', 'InvestmentTransactionEditActivity.onActivityResult@PURCHASE_PRICE', 'RESULT',
  'the calculator returns the amount and finishes: setResult(RESULT_OK) at 443, finish at 444, and the framework delivers the result to the editor that started it (PURCHASE_PRICE-launched calculator only)',
  guard='requestCode is REQUEST_PURCHASE_PRICE (= 2) and resultCode is RESULT_OK with data non-null (InvestmentTransactionEditActivity.java:119-158; cancelled or null-data early return at 123; PURCHASE_PRICE branch at 134-145: mStock.setPurchasePrice at 135, showPurchasePrice at 136)',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult: setResult(RESULT_OK) at 443, finish at 444); SRC common/Calculator.java:79 (activity.startActivityForResult(intent, requestCode)); SRC investment/InvestmentTransactionEditActivity.java:119-158 (onActivityResult; Calculator.getAmountFromResult at 125; switch on the four request codes); FW-SRC core/java/android/app/ActivityThread.java:4253-4265; FW-SRC core/java/android/app/Activity.java:7259-7266; variant @PURCHASE_PRICE')
e('InvestmentTransactionEditActivity.onCommissionClick', 'CalculatorActivity.<init>@COMMISSION', 'INTENT',
  'the commission field opens the calculator: Calculator.show starts CalculatorActivity (COMMISSION-launched calculator only)',
  guard='the launch uses REQUEST_COMMISSION (= 3) (InvestmentTransactionEditActivity.java)',
  cls='standard',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:232-238 (@OnClick at 232; forActivity 234, amount 235, currency 236, show 237); SRC common/Calculator.java:70 (intent for CalculatorActivity.class), 77-83 (show: startActivityForResult at 79); FW-SRC core/java/android/app/ActivityThread.java:2669-2670 (mInstrumentation.newActivity); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance() at 1174); variant @COMMISSION')
e('CalculatorActivity.<init>@COMMISSION', 'CalculatorActivity.onCreate@COMMISSION', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor (COMMISSION-launched calculator)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999); variant @COMMISSION')
e('CalculatorActivity.onCreate@COMMISSION', 'S_CALCULATOR@COMMISSION', 'ENTERS',
  'onCreate sets the layout (line 115) and wires the keys through initializeControls (line 127): the calculator screen is shown (COMMISSION-launched calculator)',
  cls='page',
  evidence='SRC common/CalculatorActivity.java:111-128 (setContentView at 115, ButterKnife.bind at 118, initializeControls at 127); variant @COMMISSION')
e('S_CALCULATOR@COMMISSION', 'CalculatorActivity.onEqualsClicked@COMMISSION', 'GUI',
  'the equals key runs the @OnClick handler, which returns the entered amount (COMMISSION-launched calculator)',
  gui=['Tap the equals key on the calculator'],
  cls='non_standard', via='ButterKnife @OnClick(R.id.buttonKeyEqual) at CalculatorActivity.java:247, bound by the generated CalculatorActivity_ViewBinding (INFERRED: the library and generated source are not in the source root)',
  evidence='SRC common/CalculatorActivity.java:247-250 (@OnClick at 247, handler 248-250); SRC res/layout/activity_calculator.xml:162 (buttonKeyEqual); auto_calls.json record CalculatorActivity_ViewBinding$2.doClick -> onEqualsClicked (CalculatorActivity_ViewBinding.java:49) is the generated path (batch 028); INFERRED ButterKnife binding (library not read); variant @COMMISSION')
e('CalculatorActivity.onEqualsClicked@COMMISSION', 'CalculatorActivity.returnResult@COMMISSION', 'CALL',
  'the equals key returns the entered amount (COMMISSION-launched calculator)',
  evidence='SRC common/CalculatorActivity.java:249 (bytecode); variant @COMMISSION')
e('CalculatorActivity.returnResult@COMMISSION', 'InvestmentTransactionEditActivity.onActivityResult@COMMISSION', 'RESULT',
  'the calculator returns the amount and finishes: setResult(RESULT_OK) at 443, finish at 444, and the framework delivers the result to the editor that started it (COMMISSION-launched calculator only)',
  guard='requestCode is REQUEST_COMMISSION (= 3) and resultCode is RESULT_OK with data non-null (InvestmentTransactionEditActivity.java:119-158; cancelled or null-data early return at 123; COMMISSION branch at 146-149: mStock.setCommission at 147, showCommission at 148)',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult: setResult(RESULT_OK) at 443, finish at 444); SRC common/Calculator.java:79 (activity.startActivityForResult(intent, requestCode)); SRC investment/InvestmentTransactionEditActivity.java:119-158 (onActivityResult; Calculator.getAmountFromResult at 125; switch on the four request codes); FW-SRC core/java/android/app/ActivityThread.java:4253-4265; FW-SRC core/java/android/app/Activity.java:7259-7266; variant @COMMISSION')
e('InvestmentTransactionEditActivity.onCurrentPriceClick', 'CalculatorActivity.<init>@CURRENT_PRICE', 'INTENT',
  'the current price field opens the calculator: Calculator.show starts CalculatorActivity (CURRENT_PRICE-launched calculator only)',
  guard='the launch uses REQUEST_CURRENT_PRICE (= 4) (InvestmentTransactionEditActivity.java)',
  cls='standard',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:240-246 (@OnClick at 240; forActivity 242, currency 243, amount 244, show 245); SRC common/Calculator.java:70 (intent for CalculatorActivity.class), 77-83 (show: startActivityForResult at 79); FW-SRC core/java/android/app/ActivityThread.java:2669-2670 (mInstrumentation.newActivity); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance() at 1174); variant @CURRENT_PRICE')
e('CalculatorActivity.<init>@CURRENT_PRICE', 'CalculatorActivity.onCreate@CURRENT_PRICE', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor (CURRENT_PRICE-launched calculator)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999); variant @CURRENT_PRICE')
e('CalculatorActivity.onCreate@CURRENT_PRICE', 'S_CALCULATOR@CURRENT_PRICE', 'ENTERS',
  'onCreate sets the layout (line 115) and wires the keys through initializeControls (line 127): the calculator screen is shown (CURRENT_PRICE-launched calculator)',
  cls='page',
  evidence='SRC common/CalculatorActivity.java:111-128 (setContentView at 115, ButterKnife.bind at 118, initializeControls at 127); variant @CURRENT_PRICE')
e('S_CALCULATOR@CURRENT_PRICE', 'CalculatorActivity.onEqualsClicked@CURRENT_PRICE', 'GUI',
  'the equals key runs the @OnClick handler, which returns the entered amount (CURRENT_PRICE-launched calculator)',
  gui=['Tap the equals key on the calculator'],
  cls='non_standard', via='ButterKnife @OnClick(R.id.buttonKeyEqual) at CalculatorActivity.java:247, bound by the generated CalculatorActivity_ViewBinding (INFERRED: the library and generated source are not in the source root)',
  evidence='SRC common/CalculatorActivity.java:247-250 (@OnClick at 247, handler 248-250); SRC res/layout/activity_calculator.xml:162 (buttonKeyEqual); auto_calls.json record CalculatorActivity_ViewBinding$2.doClick -> onEqualsClicked (CalculatorActivity_ViewBinding.java:49) is the generated path (batch 028); INFERRED ButterKnife binding (library not read); variant @CURRENT_PRICE')
e('CalculatorActivity.onEqualsClicked@CURRENT_PRICE', 'CalculatorActivity.returnResult@CURRENT_PRICE', 'CALL',
  'the equals key returns the entered amount (CURRENT_PRICE-launched calculator)',
  evidence='SRC common/CalculatorActivity.java:249 (bytecode); variant @CURRENT_PRICE')
e('CalculatorActivity.returnResult@CURRENT_PRICE', 'InvestmentTransactionEditActivity.onActivityResult@CURRENT_PRICE', 'RESULT',
  'the calculator returns the amount and finishes: setResult(RESULT_OK) at 443, finish at 444, and the framework delivers the result to the editor that started it (CURRENT_PRICE-launched calculator only)',
  guard='requestCode is REQUEST_CURRENT_PRICE (= 4) and resultCode is RESULT_OK with data non-null (InvestmentTransactionEditActivity.java:119-158; cancelled or null-data early return at 123; CURRENT_PRICE branch at 151-155: mStock.setCurrentPrice at 152, showCurrentPrice at 153)',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult: setResult(RESULT_OK) at 443, finish at 444); SRC common/Calculator.java:79 (activity.startActivityForResult(intent, requestCode)); SRC investment/InvestmentTransactionEditActivity.java:119-158 (onActivityResult; Calculator.getAmountFromResult at 125; switch on the four request codes); FW-SRC core/java/android/app/ActivityThread.java:4253-4265; FW-SRC core/java/android/app/Activity.java:7259-7266; variant @CURRENT_PRICE')

# B6-GUARD: showPrerequisite guard on MainActivity.onCreate ->
# MainActivity.populateScheduledTransactions (routes 15 + 26 step 3,
# route 27 step 3): hand replacement of AUTO edge Ec1f84c25; trigger and
# evidence verbatim, only the guard is added, so the id change is the
# sole diff. Primary (full four-conjunct) guard text per audit-approved
# design section (c)(i); no cls/via/gui/needs_state/env (matches the
# AUTO edge, which has gui [] and via null, and the sibling
# E73c83312 hand edge, which carries no cls/via).
e('MainActivity.onCreate', 'MainActivity.populateScheduledTransactions', 'CALL',
  'Direct call',
  guard='!showPrerequisite() (MainActivity.java:184-187; definition :1478-1499: no tutorial needed (:1351-1353) and a database available (:1338-1348: stored path non-empty, not an unpassworded .emb file, and the file exists))',
  evidence='SRC MainActivity.java:244 (bytecode)')

# ==================================================================
# B6-SYNC-V2: action-partition chain (Sync re-feed v2, amended package
# section 2.3 additions + 2.2 suppressions). A1 is the D5 retarget in
# place above; R-S9a is the 04.py retarget. S1/S2 suppress auto edges
# only (belt-and-braces; base-pair suppression already kills them
# once A2/A3 exist).
sup(('SyncManager.triggerDownload', 'SyncManager.invokeSyncService'),
    ('SyncManager.triggerUpload', 'SyncManager.invokeSyncService'))

# A2.
e('SyncManager.triggerDownload', 'SyncManager.invokeSyncService@DOWNLOAD', 'CALL',
  'triggerDownload invokes the sync service with the DOWNLOAD action',
  evidence='SRC sync/SyncManager.java:356-357 (triggerDownload; invokeSyncService(INTENT_ACTION_DOWNLOAD) at 357)')
# A3.
e('SyncManager.triggerUpload', 'SyncManager.invokeSyncService@UPLOAD', 'CALL',
  'triggerUpload invokes the sync service with the UPLOAD action',
  evidence='SRC sync/SyncManager.java:360-361 (triggerUpload; invokeSyncService(INTENT_ACTION_UPLOAD) at 361)')
# A4.
e('SyncManager.invokeSyncService@SYNC', 'SyncService.enqueueWork@SYNC', 'CALL',
  'invokeSyncService enqueues work for the sync service with the SYNC action and the caller Messenger',
  guard='remote file preference non-empty (SyncManager.java:190-192)',
  evidence='SRC sync/SyncManager.java:188-192 (remoteFile validation; return if empty at 190-192); SRC sync/SyncManager.java:209-217 (Messenger at 209-212; enqueueWork at 217); SRC IntentFactory.java:38-52 (setAction at 42 preserves the SYNC action)')
# A5.
e('SyncManager.invokeSyncService@DOWNLOAD', 'SyncService.enqueueWork@DOWNLOAD', 'CALL',
  'invokeSyncService enqueues work for the sync service with the DOWNLOAD action and the caller Messenger',
  guard='remote file preference non-empty (SyncManager.java:190-192)',
  evidence='SRC sync/SyncManager.java:188-192 (remoteFile validation; return if empty at 190-192); SRC sync/SyncManager.java:209-217 (Messenger at 209-212; enqueueWork at 217); SRC IntentFactory.java:38-52 (setAction at 42 preserves the DOWNLOAD action)')
# A6.
e('SyncManager.invokeSyncService@UPLOAD', 'SyncService.enqueueWork@UPLOAD', 'CALL',
  'invokeSyncService enqueues work for the sync service with the UPLOAD action and the caller Messenger',
  guard='remote file preference non-empty (SyncManager.java:190-192)',
  evidence='SRC sync/SyncManager.java:188-192 (remoteFile validation; return if empty at 190-192); SRC sync/SyncManager.java:209-217 (Messenger at 209-212; enqueueWork at 217); SRC IntentFactory.java:38-52 (setAction at 42 preserves the UPLOAD action)')
# A7.
e('SyncService.enqueueWork@SYNC', 'SyncService.onHandleWork@SYNC', 'FRAMEWORK',
  'JobIntentService delivers the queued SYNC-action intent to onHandleWork on its worker thread (INFERRED from the androidx contract)',
  evidence='SRC sync/SyncService.java:90 (onHandleWork), 151-153 (enqueueWork); INFERRED androidx JobIntentService (not read)')
# A8.
e('SyncService.enqueueWork@DOWNLOAD', 'SyncService.onHandleWork@DOWNLOAD', 'FRAMEWORK',
  'JobIntentService delivers the queued DOWNLOAD-action intent to onHandleWork on its worker thread (INFERRED from the androidx contract)',
  evidence='SRC sync/SyncService.java:90 (onHandleWork), 151-153 (enqueueWork); INFERRED androidx JobIntentService (not read)')
# A9.
e('SyncService.enqueueWork@UPLOAD', 'SyncService.onHandleWork@UPLOAD', 'FRAMEWORK',
  'JobIntentService delivers the queued UPLOAD-action intent to onHandleWork on its worker thread (INFERRED from the androidx contract)',
  evidence='SRC sync/SyncService.java:90 (onHandleWork), 151-153 (enqueueWork); INFERRED androidx JobIntentService (not read)')
# A10.
e('SyncService.onHandleWork@SYNC', 'SyncService.triggerSync', 'CALL',
  'onHandleWork takes the SYNC branch and calls triggerSync',
  guard='action == INTENT_ACTION_SYNC (SyncService.java:134-135)',
  evidence='SRC sync/SyncService.java:124-125 (switch), 134-135 (SYNC case calls triggerSync)')
# A11.
e('SyncService.onHandleWork@DOWNLOAD', 'SyncService.sendMessage@DOWNLOAD', 'CALL',
  'onHandleWork takes the DOWNLOAD branch: pullDatabase, then sendMessage with DOWNLOAD_COMPLETE',
  guard='action == INTENT_ACTION_DOWNLOAD (SyncService.java:126-128)',
  evidence='SRC sync/SyncService.java:124-129 (switch at 124; DOWNLOAD case at 126; pullDatabase at 127; sendMessage DOWNLOAD_COMPLETE at 128)')
# A12.
e('SyncService.onHandleWork@UPLOAD', 'SyncService.sendMessage@OTHER', 'CALL',
  'onHandleWork takes the UPLOAD branch: pushDatabase, then sendMessage with UPLOAD_COMPLETE',
  guard='action == INTENT_ACTION_UPLOAD (SyncService.java:130-132)',
  evidence='SRC sync/SyncService.java:130-132 (UPLOAD case; pushDatabase at 131; sendMessage UPLOAD_COMPLETE at 132)')
# A13 (three offline edges, one per action variant).
e('SyncService.onHandleWork@SYNC', 'SyncService.sendMessage@OTHER', 'CALL',
  'onHandleWork finds the device offline before the action switch and sends NOT_ON_WIFI',
  guard='device offline (SyncService.java:104-108)',
  evidence='SRC sync/SyncService.java:104-108 (offline check and sendMessage NOT_ON_WIFI at 107)')
e('SyncService.onHandleWork@DOWNLOAD', 'SyncService.sendMessage@OTHER', 'CALL',
  'onHandleWork finds the device offline before the action switch and sends NOT_ON_WIFI',
  guard='device offline (SyncService.java:104-108)',
  evidence='SRC sync/SyncService.java:104-108 (offline check and sendMessage NOT_ON_WIFI at 107)')
e('SyncService.onHandleWork@UPLOAD', 'SyncService.sendMessage@OTHER', 'CALL',
  'onHandleWork finds the device offline before the action switch and sends NOT_ON_WIFI',
  guard='device offline (SyncService.java:104-108)',
  evidence='SRC sync/SyncService.java:104-108 (offline check and sendMessage NOT_ON_WIFI at 107)')
# A14 (service-lifecycle mirrors).
e('SyncService.enqueueWork@SYNC', 'SyncService.<init>', 'FRAMEWORK',
  'JobIntentService creates the service instance for the queued intent (INFERRED androidx contract)',
  evidence='SRC sync/SyncService.java:151-153; FW-SRC core/java/android/app/ActivityThread.java:3311-3321 (handleCreateService; newInstance at 3321); INFERRED androidx JobIntentService (library not in the dataset; not read)')
e('SyncService.onHandleWork@SYNC', 'SyncService.onDestroy', 'LIFECYCLE',
  'when the queued work is done JobIntentService stops itself, and the framework then runs onDestroy (INFERRED androidx stopSelf path)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3499-3504 (handleStopService; s.onDestroy at 3504); FW-SRC core/java/android/app/Service.java:515; INFERRED androidx JobIntentService (not read)')
e('SyncService.onHandleWork@DOWNLOAD', 'SyncService.onDestroy', 'LIFECYCLE',
  'when the queued work is done JobIntentService stops itself, and the framework then runs onDestroy (INFERRED androidx stopSelf path)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3499-3504 (handleStopService; s.onDestroy at 3504); FW-SRC core/java/android/app/Service.java:515; INFERRED androidx JobIntentService (not read)')
e('SyncService.onHandleWork@UPLOAD', 'SyncService.onDestroy', 'LIFECYCLE',
  'when the queued work is done JobIntentService stops itself, and the framework then runs onDestroy (INFERRED androidx stopSelf path)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3499-3504 (handleStopService; s.onDestroy at 3504); FW-SRC core/java/android/app/Service.java:515; INFERRED androidx JobIntentService (not read)')
