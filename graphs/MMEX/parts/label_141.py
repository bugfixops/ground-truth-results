# ================================================================== batch 141 (label_141): com.money.manager.ex.view widgets, RobotoView statics and ScrollAwareFABBehavior (36 methods in 7 classes)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_141.md (21 REACHABLE, 15 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_141.grep.txt.
# This file writes 7 e() edges (FRAMEWORK), 0 gui() edges, 15 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). Auto-record routes (parseAttributes, the RobotoView static methods and RobotoView.<clinit>) are CALL edges from auto_calls.json (D7) and are not written here.
# The four 2-argument Roboto constructors are reached only through XML inflation (LayoutInflater calls them, FW-SRC LayoutInflater.java:90-91). Each has one FRAMEWORK edge from the method that calls setContentView or inflate for the layout that holds the tag.
# Routes through other batches are interim (D8): CalculatorActivity.onCreate (label_027), AccountEditActivity.onCreate (label_006), SearchParametersFragment.onCreateView (label_109), SplitCategoriesActivity.onCreate (label_133), MmexApplication.onCreate (label_002).
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1 (the only framework evidence used here); INFERRED = a step whose source was not read.

# ---- XML inflation of the two-argument constructors (D6 is not involved: these are FRAMEWORK edges)

e('CalculatorActivity.onCreate', 'RobotoButton.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'setContentView inflates activity_calculator.xml, and LayoutInflater builds each RobotoButton tag with the (Context, AttributeSet) constructor',
  evidence='SRC common/CalculatorActivity.java:115 (setContentView(R.layout.activity_calculator)); res/layout/activity_calculator.xml:86 (RobotoButton tag); FW-SRC core/java/android/view/LayoutInflater.java:90-91 (constructor signature), 615 (getConstructor), 647 (newInstance); INFERRED: the path from AppCompat setContentView to LayoutInflater is not in fw_src')

e('CalculatorActivity.onCreate', 'RobotoTextView.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'setContentView inflates activity_calculator.xml, and LayoutInflater builds each RobotoTextView tag with the (Context, AttributeSet) constructor',
  evidence='SRC common/CalculatorActivity.java:115; res/layout/activity_calculator.xml:37 (RobotoTextView tag); FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615, 647; INFERRED: the AppCompat setContentView path is not in fw_src')

e('AccountEditActivity.onCreate', 'RobotoEditText.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'setContentView inflates activity_account_edit.xml, and LayoutInflater builds each RobotoEditText tag with the (Context, AttributeSet) constructor',
  evidence='SRC account/AccountEditActivity.java:138 (setContentView(R.layout.activity_account_edit)); res/layout/activity_account_edit.xml:52 (RobotoEditText tag); FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615, 647; INFERRED: the AppCompat setContentView path is not in fw_src')

e('SearchParametersFragment.onCreateView', 'RobotoCheckBox.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'onCreateView inflates search_parameters_fragment.xml, and LayoutInflater builds each RobotoCheckBox tag with the (Context, AttributeSet) constructor',
  evidence='SRC search/SearchParametersFragment.java:136 (inflater.inflate(R.layout.search_parameters_fragment, container, false)); res/layout/search_parameters_fragment.xml:64 (RobotoCheckBox tag); FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615, 647')

# ---- ScrollAwareFABBehavior: the coordinator layout builds the behaviour from app:layout_behavior, then dispatches nested scroll to it (INFERRED androidx)

e('SplitCategoriesActivity.onCreate', 'ScrollAwareFABBehavior.<init>', 'FRAMEWORK',
  'setContentView inflates activity_split_categories.xml; the coordinator layout builds the FAB behaviour named in app:layout_behavior with (Context, AttributeSet)',
  evidence='SRC transactions/SplitCategoriesActivity.java:100 (setContentView(R.layout.activity_split_categories)); res/layout/activity_split_categories.xml:77 (app:layout_behavior="com.money.manager.ex.view.behaviors.ScrollAwareFABBehavior"); SRC view/behaviors/ScrollAwareFABBehavior.java:38 (constructor); INFERRED: androidx CoordinatorLayout.LayoutParams creates the behaviour by reflection, source not read',
  cls='non_standard',
  via='androidx CoordinatorLayout builds the behaviour named in app:layout_behavior by reflection (INFERRED, source not read)')

e('ScrollAwareFABBehavior.<init>', 'ScrollAwareFABBehavior.onStartNestedScroll', 'FRAMEWORK',
  'the coordinator calls onStartNestedScroll on the behaviour it built when a child starts a nested scroll (NestedScrollView or RecyclerView)',
  evidence='SRC view/behaviors/ScrollAwareFABBehavior.java:47-54 (returns true for SCROLL_AXIS_VERTICAL at line 51); res/layout/activity_split_categories.xml:40 (NestedScrollView), 58 (RecyclerView); INFERRED: androidx CoordinatorLayout nested-scroll dispatch, source not read')

e('ScrollAwareFABBehavior.onStartNestedScroll', 'ScrollAwareFABBehavior.onNestedScroll', 'FRAMEWORK',
  'the coordinator calls onNestedScroll after onStartNestedScroll returned true, with the scroll deltas (hide and show at lines 62-66)',
  evidence='SRC view/behaviors/ScrollAwareFABBehavior.java:51-53 (returns true), 57-67 (onNestedScroll); INFERRED: androidx CoordinatorLayout dispatch, source not read')

# ---- UNREACHABLE entries: (kind, reason, evidence, confirmed_by)

UNREACHABLE['GestureWebView.<init>'] = ('no_trigger_in_app',
    'no code constructs GestureWebView: grep over src/main finds the name only in GestureWebView.java (no layout tag, no new expression)',
    'SRC view/GestureWebView.java:30, 33-38; grep Q1 (incoming 0); grep Q2 (only GestureWebView.java names the class)',
    'SOURCE')

UNREACHABLE['GestureWebView.initializeGestureDetector'] = ('no_trigger_in_app',
    'its only caller is GestureWebView.<init> (auto record line 37), which is UNREACHABLE',
    'SRC view/GestureWebView.java:37, 48-62; grep Q1 (incoming 1, from GestureWebView.<init>)',
    'SOURCE')

UNREACHABLE['GestureWebView.onTouchEvent'] = ('no_trigger_in_app',
    'touch dispatch reaches it only on a live GestureWebView instance, and no instance is constructed',
    'SRC view/GestureWebView.java:44-46; grep Q1 (incoming 0)',
    'SOURCE')

UNREACHABLE['GestureWebView$1.<init>'] = ('no_trigger_in_app',
    'the only auto record comes from initializeGestureDetector (line 49), which is UNREACHABLE',
    'SRC view/GestureWebView.java:49; grep Q1 (incoming 1)',
    'SOURCE')

UNREACHABLE['GestureWebView$1.onDown'] = ('no_trigger_in_app',
    'called only by the GestureDetector that initializeGestureDetector builds, and that method has no live caller',
    'SRC view/GestureWebView.java:50-52; grep Q1 (incoming 0)',
    'SOURCE')

UNREACHABLE['GestureWebView$1.onLongPress'] = ('no_trigger_in_app',
    'same as onDown: only the unreachable GestureDetector calls it',
    'SRC view/GestureWebView.java:54-57; grep Q1 (incoming 0)',
    'SOURCE')

UNREACHABLE['RobotoButton.<init>(Context)'] = ('framework_never_calls',
    'no app code calls the one-argument constructor (no new RobotoButton, no subclass), and LayoutInflater uses only (Context, AttributeSet)',
    'SRC view/RobotoButton.java:36-38; grep Q1 (incoming 0); grep Q2; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615, 647',
    'SOURCE')

UNREACHABLE['RobotoButton.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
    'no app caller uses the three-argument constructor (no new RobotoButton with three arguments, no subclass), and LayoutInflater never uses this signature',
    'SRC view/RobotoButton.java:75-78 (super at 76); grep Q1 (incoming 0); grep Q2; FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoCheckBox.<init>(Context)'] = ('framework_never_calls',
    'no app caller uses the one-argument constructor (no new RobotoCheckBox, no subclass), and LayoutInflater uses only (Context, AttributeSet)',
    'SRC view/RobotoCheckBox.java:38-40; grep Q1 (incoming 0); grep Q2; FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoCheckBox.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
    'no app caller uses the three-argument constructor, and LayoutInflater never uses this signature',
    'SRC view/RobotoCheckBox.java:77-80 (super at 78); grep Q1 (incoming 0); FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoEditText.<init>(Context)'] = ('framework_never_calls',
    'no app caller uses the one-argument constructor (no new RobotoEditText, no subclass), and LayoutInflater uses only (Context, AttributeSet)',
    'SRC view/RobotoEditText.java:34-36 (super at 35); grep Q1 (incoming 0); grep Q2; FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoEditText.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
    'no app caller uses the three-argument constructor, and LayoutInflater never uses this signature',
    'SRC view/RobotoEditText.java:71-74 (super at 72); grep Q1 (incoming 0); FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoTextView.<init>(Context)'] = ('framework_never_calls',
    'the only app construction (DashboardFragment.java:435) passes two arguments, and LayoutInflater uses only (Context, AttributeSet)',
    'SRC view/RobotoTextView.java:34-36 (super at 35); SRC DashboardFragment.java:435; grep Q1 (incoming 0); FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoTextView.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
    'no app caller uses the three-argument constructor, and LayoutInflater never uses this signature',
    'SRC view/RobotoTextView.java:73-76 (super at 74); grep Q1 (incoming 0); FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoView.<init>'] = ('no_trigger_in_app',
    'RobotoView declares only static members, no code writes new RobotoView, and no class extends it',
    'SRC view/RobotoView.java:37 (class declaration); grep Q1 (incoming 0); grep Q2 (no new RobotoView, no extends RobotoView)',
    'SOURCE')

# ---- sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch
sup(('GestureWebView.<init>', 'GestureWebView.initializeGestureDetector'))  # the constructor has no caller
sup(('GestureWebView.initializeGestureDetector', 'GestureWebView$1.<init>'))  # the builder has no live caller
