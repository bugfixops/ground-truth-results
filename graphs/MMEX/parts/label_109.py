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
