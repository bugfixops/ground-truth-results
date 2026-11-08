# batch 028 (label_028): com.money.manager.ex.common.CalculatorActivity_ViewBinding (7 methods: its two constructors, unbind, and the listener classes $1 and $2 with their constructors and doClick) and com.money.manager.ex.common.CategoryListActivity (4 methods: <clinit>, <init>, onCreate, onKeyUp). 11 methods in all.
# Rows and printed lines: graphs/MMEX/parts/label_028.md. grep evidence: graphs/MMEX/parts/label_028.grep.txt.
# CALL edges between the generated methods and the in-app calls come from auto_calls.json and are not written here. The ButterKnife reflection call from CalculatorActivity.onCreate is not in auto_calls.json, so it is written here (cls='non_standard').
# ButterKnife and the generated classes are not in the source root: their claims are INFERRED.
# Page S_CALCULATOR is defined in label_027.py (batch 027, not merged yet). Page S_CATEGORY_LIST is defined at graph_def.py:1214.
# No ENTERS edge is written here. The ENTERS edge to S_CATEGORY_LIST is written by label_029.py (CategoryListFragment.onActivityCreated, graph_def.py:2311).
# batch 027 also writes S_CALCULATOR -> CalculatorActivity.onDeleteClicked and -> CalculatorActivity.onEqualsClicked directly (label_027.py). Both routes are kept here; the orchestrator decides whether to drop batch 027's two edges (see the batch 028 report).

# ---- CategoryListActivity: entry from another app (exported=true, PICK and EDIT filters)

e('S_ENTRY', 'CategoryListActivity.<init>', 'ENTRY',
  'another app sends an ACTION_PICK or ACTION_EDIT intent to the exported CategoryListActivity',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to CategoryListActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:204-209 (exported=true; PICK and EDIT filters); FW-SRC core/java/android/app/ActivityThread.java:2669-2670 (mInstrumentation.newActivity); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance() at 1174)')

e('S_ENTRY', 'CategoryListActivity.<clinit>', 'ENTRY',
  'the first CategoryListActivity instance (the exported-intent start above) initialises the class',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to CategoryListActivity (exported=true)', ('other_app',)),
  evidence='SRC common/CategoryListActivity.java:41 (FRAGMENTTAG is built by a method call, so it is not a compile-time constant and the class has a static initialiser); SRC AndroidManifest.xml:204-209; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

# ---- in-app callers that start CategoryListActivity for a pick (ACTION_PICK). The class initialiser edge is INFERRED (Java language rule), as for PayeeActivity.

e('EditTransactionCommonFunctions$4.onClick', 'CategoryListActivity.<init>', 'INTENT',
  'tap the category field in the transaction editor when no split is selected: startActivityForResult(ACTION_PICK) starts CategoryListActivity',
  gui=['Tap the category field in the transaction editor'],
  guard='no split categories are selected: the intent is built only when isSplitSelected() is false (EditTransactionCommonFunctions.java:462)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:459-466 (setOnClickListener 459; isSplitSelected 462; new Intent 464; ACTION_PICK 465; startActivityForResult 466); FW-SRC core/java/android/app/Instrumentation.java:1170-1174')

e('EditTransactionCommonFunctions$4.onClick', 'CategoryListActivity.<clinit>', 'INTENT',
  'the first CategoryListActivity instance (the start above) initialises the class',
  gui=['Tap the category field in the transaction editor'],
  guard='no split categories are selected: the intent is built only when isSplitSelected() is false (EditTransactionCommonFunctions.java:462)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:459-466; SRC common/CategoryListActivity.java:41; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

e('SearchParametersFragment$2.onClick', 'CategoryListActivity.<init>', 'INTENT',
  'tap the category field on the search screen: startActivityForResult(ACTION_PICK) starts CategoryListActivity',
  gui=['Tap the category field on the search screen'],
  evidence='SRC search/SearchParametersFragment.java:199-205 (listener set at 199; onClick 201; new Intent 202; ACTION_PICK 203; startActivityForResult 204); FW-SRC core/java/android/app/Instrumentation.java:1170-1174')

e('SearchParametersFragment$2.onClick', 'CategoryListActivity.<clinit>', 'INTENT',
  'the first CategoryListActivity instance (the start above) initialises the class',
  gui=['Tap the category field on the search screen'],
  evidence='SRC search/SearchParametersFragment.java:199-205; SRC common/CategoryListActivity.java:41; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

e('SplitCategoriesActivity.showCategorySelector', 'CategoryListActivity.<init>', 'INTENT',
  'a category request event (CategoryRequestedEvent) makes the split screen start CategoryListActivity with ACTION_PICK',
  evidence='SRC transactions/SplitCategoriesActivity.java:213-216 (onEvent(CategoryRequestedEvent) calls showCategorySelector at 215); SRC transactions/SplitCategoriesActivity.java:307-314 (new Intent 308; ACTION_PICK 309; startActivityForResult 314); FW-SRC core/java/android/app/Instrumentation.java:1170-1174')

e('SplitCategoriesActivity.showCategorySelector', 'CategoryListActivity.<clinit>', 'INTENT',
  'the first CategoryListActivity instance (the start above) initialises the class',
  evidence='SRC transactions/SplitCategoriesActivity.java:307-314; SRC common/CategoryListActivity.java:41; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

# ---- creation, lifecycle and the Back key

e('CategoryListActivity.<init>', 'CategoryListActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999)')

gui('S_CATEGORY_LIST', 'CategoryListActivity.onKeyUp', 'Press Back while the category list is in front',
  evidence='FW-SRC core/java/android/app/Activity.java:3255-3272 (dispatchKeyEvent passes the key to event.dispatch at 3272); FW-SRC core/java/android/view/KeyEvent.java:2709-2715 (ACTION_UP calls receiver.onKeyUp at 2715); SRC common/CategoryListActivity.java:73-84 (onKeyUp 74; KEYCODE_BACK 75; setResultAndFinish 80)')

# ---- ButterKnife binding of CalculatorActivity (generated class not in the source root: INFERRED)

e('CalculatorActivity.onCreate', 'CalculatorActivity_ViewBinding.<init>(CalculatorActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for the activity, which binds the @OnClick handlers and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated CalculatorActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC common/CalculatorActivity.java:118 (ButterKnife.bind(this)); INFERRED ButterKnife generated binding (label_028.grep.txt section D: the generated report says the source file was not found)')

e('S_CALCULATOR', 'CalculatorActivity_ViewBinding$1.doClick', 'GUI',
  'tap the delete key (<=): the @OnClick listener of the generated binding calls onDeleteClicked',
  gui=['Tap the delete key (<=)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC common/CalculatorActivity.java:236-237 (@OnClick(R.id.deleteButton) at 236; onDeleteClicked at 237); SRC res/layout/activity_calculator.xml:98-100 (deleteButton); auto_calls.json:39476-39477 (CalculatorActivity_ViewBinding$1.doClick -> CalculatorActivity.onDeleteClicked); INFERRED ButterKnife listener')

e('S_CALCULATOR', 'CalculatorActivity_ViewBinding$2.doClick', 'GUI',
  'tap the equals key (=): the @OnClick listener of the generated binding calls onEqualsClicked, which returns the entered amount',
  gui=['Tap the equals key (=)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC common/CalculatorActivity.java:247-248 (@OnClick(R.id.buttonKeyEqual) at 247; onEqualsClicked at 248); SRC res/layout/activity_calculator.xml:161-164 (buttonKeyEqual at 162); auto_calls.json:37800-37801 (CalculatorActivity_ViewBinding$2.doClick -> CalculatorActivity.onEqualsClicked); INFERRED ButterKnife listener')

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_028.grep.txt)

UNREACHABLE['CalculatorActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root). ButterKnife.bind(this) at CalculatorActivity.java:118 discards the returned Unbinder, CalculatorActivity has no onDestroy, and no caller record for unbind exists in auto_calls.json (0 callers). No Unbinder reference exists in the app source (label_028.grep.txt sections A-C)',
  'SRC common/CalculatorActivity.java:118; label_028.grep.txt sections A-C; python-printed auto_calls query (0 callers)',
  'INFERRED')
