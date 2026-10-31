# batch 027 (label_027): com.money.manager.ex.common.CalculatorActivity (29 methods: the class, its anonymous listeners $1, $2, $3 and its Icepick helper $$Icepick) and the Dagger-generated CalculatorActivity_MembersInjector (5 methods). 34 methods in all.
# Rows and printed lines: graphs/MMEX/parts/label_027.md. grep evidence: graphs/MMEX/parts/label_027.grep.txt.
# CALL edges come from auto_calls.json (the calls inside CalculatorActivity and its listeners, the calls into Calculator, the Dagger static inject calls) and are not written here.
# Framework claims cite FW-SRC lines printed for this batch. The AppCompat menu step, the ButterKnife binding, the Dagger component and the Icepick library are not in fw_src: INFERRED.
# Every edge below has a batch 027 method (or S_CALCULATOR) as its destination. The Icepick edges start at MmxBaseFragmentActivity methods, which are another batch's rows.

SCREENS.update({
    'S_CALCULATOR': 'Full-screen calculator (CalculatorActivity): the number, operator, delete, clear and equals keys, and the save icon; it returns the entered amount to the caller',
})

# ---- entry: a caller starts the activity with Calculator.show (startActivityForResult). The framework then creates it.
# Calculator.java:70 builds the intent for CalculatorActivity.class; Calculator.java:77-83 starts it. The creation step is FW-SRC: Instrumentation.newActivity (Instrumentation.java:1170-1174) runs loadClass(...).newInstance(), which initialises the class and runs the constructor.

EV_START = ('SRC common/Calculator.java:70 (intent for CalculatorActivity.class), 77-83 (show: startActivityForResult at 79); '
            'FW-SRC core/java/android/app/ActivityThread.java:2669-2670 (mInstrumentation.newActivity); '
            'FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance() at 1174)')

e('AccountEditActivity$1.onClick', 'CalculatorActivity.<init>', 'INTENT',
  'the initial balance field opens the calculator for a result: Calculator.show (line 307) starts CalculatorActivity',
  evidence='SRC account/AccountEditActivity.java:301-309 (listener 301; onClick 303-308; Calculator.forActivity 304, currency 305, amount 306, show 307); ' + EV_START)

e('EditTransactionCommonFunctions$2.onClick', 'CalculatorActivity.<init>', 'INTENT',
  'a click listener opens the calculator for a result: Calculator.show (line 430) starts CalculatorActivity',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:427-430 (forActivity 427, currency 428, amount 429, show 430); ' + EV_START)

e('EditTransactionCommonFunctions$3.onClick', 'CalculatorActivity.<init>', 'INTENT',
  'a click listener opens the calculator for a result: Calculator.show (line 446) starts CalculatorActivity',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:444-446 (forActivity 444, currency 445, amount 445, show 446); ' + EV_START)

e('InvestmentTransactionEditActivity.onNumSharesClick', 'CalculatorActivity.<init>', 'INTENT',
  'the number-of-shares field opens the calculator: Calculator.show (line 218) starts CalculatorActivity',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:211-219 (@OnClick at 211; forActivity 215, amount 216, roundToCurrency 217, show 218); ' + EV_START)

e('InvestmentTransactionEditActivity.onPurchasePriceClick', 'CalculatorActivity.<init>', 'INTENT',
  'the purchase price field opens the calculator: Calculator.show (line 229) starts CalculatorActivity',
  guard='mAccount is not null (InvestmentTransactionEditActivity.java:223 returns early when it is null)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:221-230 (@OnClick at 221; guard 223; forActivity 225, roundToCurrency 226, amount 227, currency 228, show 229); ' + EV_START)

e('InvestmentTransactionEditActivity.onCommissionClick', 'CalculatorActivity.<init>', 'INTENT',
  'the commission field opens the calculator: Calculator.show (line 237) starts CalculatorActivity',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:232-238 (@OnClick at 232; forActivity 234, amount 235, currency 236, show 237); ' + EV_START)

e('InvestmentTransactionEditActivity.onCurrentPriceClick', 'CalculatorActivity.<init>', 'INTENT',
  'the current price field opens the calculator: Calculator.show (line 245) starts CalculatorActivity',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:240-246 (@OnClick at 240; forActivity 242, currency 243, amount 244, show 245); ' + EV_START)

e('PriceEditActivity.onPriceClick', 'CalculatorActivity.<init>', 'INTENT',
  'the price field opens the calculator: Calculator.show (line 140) starts CalculatorActivity',
  evidence='SRC investment/PriceEditActivity.java:135-140 (forActivity 137, amount 138, roundToCurrency 139, show 140); ' + EV_START)

e('SearchParametersFragment.onAmountFromClicked', 'CalculatorActivity.<init>', 'INTENT',
  'the from-amount field opens the calculator: Calculator.show (line 405, Calculator.forFragment) starts CalculatorActivity',
  evidence='SRC search/SearchParametersFragment.java:398-406 (@OnClick at 398; forFragment, amount and show on line 405); ' + EV_START)

e('SearchParametersFragment.onAmountToClicked', 'CalculatorActivity.<init>', 'INTENT',
  'the to-amount field opens the calculator: Calculator.show (line 415, Calculator.forFragment) starts CalculatorActivity',
  evidence='SRC search/SearchParametersFragment.java:408-416 (@OnClick at 408; forFragment, amount and show on line 415); ' + EV_START)

e('SplitCategoriesActivity.onEvent(AmountEntryRequestedEvent)', 'CalculatorActivity.<init>', 'INTENT',
  'an amount-entry request event opens the calculator: Calculator.show (line 210) starts CalculatorActivity',
  evidence='SRC transactions/SplitCategoriesActivity.java:205-211 (forActivity 207, currency 208, amount 209, show 210); ' + EV_START)

# ---- creation, lifecycle and menu

e('CalculatorActivity.<init>', 'CalculatorActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999)')

e('CalculatorActivity.onCreate', 'S_CALCULATOR', 'ENTERS',
  'onCreate sets the layout (line 115) and wires the keys through initializeControls (line 127): the calculator screen is shown',
  evidence='SRC common/CalculatorActivity.java:111-128 (setContentView at 115, ButterKnife.bind at 118, initializeControls at 127)')

e('CalculatorActivity.onCreate', 'CalculatorActivity.onResume', 'LIFECYCLE',
  'the framework calls onResume after onCreate: ActivityThread.handleResumeActivity calls performResume, which calls Instrumentation.callActivityOnResume',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3556 (r.activity.performResume() in handleResumeActivity, which starts at 3608); FW-SRC core/java/android/app/Activity.java:7098-7107 (performResume calls callActivityOnResume at 7107); FW-SRC core/java/android/app/Instrumentation.java:1353-1355 (callActivityOnResume calls onResume at 1355)')

e('CalculatorActivity.onCreate', 'CalculatorActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:631 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3388 (onCreatePanelMenu calls onCreateOptionsMenu at 3388); SRC common/CalculatorActivity.java:139 (addSaveToolbarIcon); INFERRED AppCompat decides when the panel is prepared (androidx not in fw_src)')

# ---- user actions on the calculator screen (page S_CALCULATOR)

e('S_CALCULATOR', 'CalculatorActivity$1.onClick', 'GUI',
  'a number key or the decimal key is tapped: the listener appends the key text and evaluates the expression',
  gui=['Tap a number key (0-9) or the decimal key'],
  evidence='SRC common/CalculatorActivity.java:88-93 (idButtonKeyNum), 314-331 (listener 314; onClick 316-325; setOnClickListener 330); SRC res/layout/activity_calculator.xml:154, 158 (buttonKeyNumDecimal, buttonKeyNum0); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED the touch dispatch to performClick (View input path not printed)')

e('S_CALCULATOR', 'CalculatorActivity$2.onClick', 'GUI',
  'an operator or parenthesis key is tapped: the listener appends the key text and evaluates the expression',
  gui=['Tap an operator key (+, /, -, x, parentheses)'],
  evidence='SRC common/CalculatorActivity.java:94-98 (idOperatorKeys), 333-346 (listener 333; onClick 335-341; setOnClickListener 345); SRC res/layout/activity_calculator.xml:91, 132 (buttonKeyLeftParenthesis, buttonKeyMultiplication); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED the touch dispatch to performClick (View input path not printed)')

e('S_CALCULATOR', 'CalculatorActivity$3.onClick', 'GUI',
  'the clear key (C) is tapped: the entry is emptied and the expression evaluated',
  gui=['Tap the clear key (C)'],
  evidence='SRC common/CalculatorActivity.java:348-357 (clear listener 350-357; onClick 352-356); SRC res/layout/activity_calculator.xml:87 (buttonKeyClear); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED the touch dispatch to performClick (View input path not printed)')

e('S_CALCULATOR', 'CalculatorActivity.onDeleteClicked', 'GUI',
  'the delete key (<=) runs the @OnClick handler: the last character is removed and the expression evaluated',
  gui=['Tap the delete key (<=)'],
  cls='non_standard', via='ButterKnife @OnClick(R.id.deleteButton) at CalculatorActivity.java:236, bound by the generated CalculatorActivity_ViewBinding (INFERRED: the library and generated source are not in the source root)',
  evidence='SRC common/CalculatorActivity.java:236-245 (@OnClick at 236, handler 237-245); SRC res/layout/activity_calculator.xml:99 (deleteButton); auto_calls.json record CalculatorActivity_ViewBinding$1.doClick -> onDeleteClicked (CalculatorActivity_ViewBinding.java:39) is the generated path (batch 028); INFERRED ButterKnife binding (library not read)')

e('S_CALCULATOR', 'CalculatorActivity.onEqualsClicked', 'GUI',
  'the equals key runs the @OnClick handler, which returns the entered amount',
  gui=['Tap the equals key (=)'],
  cls='non_standard', via='ButterKnife @OnClick(R.id.buttonKeyEqual) at CalculatorActivity.java:247, bound by the generated CalculatorActivity_ViewBinding (INFERRED: the library and generated source are not in the source root)',
  evidence='SRC common/CalculatorActivity.java:247-250 (@OnClick at 247, handler 248-250); SRC res/layout/activity_calculator.xml:162 (buttonKeyEqual); auto_calls.json record CalculatorActivity_ViewBinding$2.doClick -> onEqualsClicked (CalculatorActivity_ViewBinding.java:49) is the generated path (batch 028); INFERRED ButterKnife binding (library not read)')

e('S_CALCULATOR', 'CalculatorActivity.onOptionsItemSelected', 'GUI',
  'the framework calls onOptionsItemSelected for the save menu item (MenuHelper.save): returnResult runs',
  gui=['Tap the save (check) icon in the action bar'],
  evidence='SRC core/MenuHelper.java:37 (save id), 87-88 (save item added in addSaveToolbarIcon); SRC common/CalculatorActivity.java:139 (menu built), 145-151 (save branch calls returnResult at 149); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450)')

# ---- Icepick (generated helper CalculatorActivity$$Icepick; the icepick library is not in the dataset)

e('MmxBaseFragmentActivity.onCreate', 'CalculatorActivity$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State fields: the library loads the generated helper CalculatorActivity$$Icepick by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:58-76 (Icepick.restoreInstanceState at 74, super.onCreate at 76); SRC common/CalculatorActivity.java:51, 74-81 (icepick.State import and @State fields); the icepick library is not in the dataset (combined/report/com.money.manager.ex.common/CalculatorActivity$$Icepick.html: "Icepick.java was not found"): INFERRED, source not read')

e('MmxBaseFragmentActivity.onCreate', 'CalculatorActivity$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:58-76 (Icepick.restoreInstanceState at 74); SRC common/CalculatorActivity.java:74-81 (@State fields); the icepick library is not in the dataset: INFERRED, source not read')

e('MmxBaseFragmentActivity.onCreate', 'CalculatorActivity$$Icepick.restore', 'FRAMEWORK',
  'Icepick calls the generated restore for the @State fields (roundToCurrencyDecimals, mAmount, mCurrencyId, mExpression) when the activity is created with saved state, for example after a rotation; the app does not guard the call at line 74',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState, unguarded in the app source); SRC common/CalculatorActivity.java:74-81 (@State fields); the icepick library is not in the dataset: INFERRED, source not read')

e('MmxBaseFragmentActivity.onSaveInstanceState', 'CalculatorActivity$$Icepick.save', 'FRAMEWORK',
  'Icepick calls the generated save for the @State fields when the framework saves the activity state',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at MmxBaseFragmentActivity.java:155)',
  evidence='SRC common/MmxBaseFragmentActivity.java:151-156 (Icepick.saveInstanceState at 155); SRC common/CalculatorActivity.java:74-81 (@State fields); FW-SRC core/java/android/app/ActivityThread.java:4713-4722 (callCallActivityOnSaveInstanceState); FW-SRC core/java/android/app/Instrumentation.java:1385-1387 (callActivityOnSaveInstanceState calls performSaveInstanceState at 1386); FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState at 1496); the icepick library is not in the dataset: INFERRED, source not read')

# ---- Dagger MembersInjector: create and injectMembers have no caller, so their outgoing calls cannot run
# The component injects CalculatorActivity through the static injectX methods (DaggerMmxComponent.java:380-381, auto_calls records), not through a MembersInjector instance.

sup(('CalculatorActivity_MembersInjector.create', 'CalculatorActivity_MembersInjector.<init>'))  # create has no caller, so its call into <init> cannot run

sup(('CalculatorActivity_MembersInjector.injectMembers', 'CalculatorActivity_MembersInjector.injectFormatUtilitiesLazy'),  # injectMembers has no caller
    ('CalculatorActivity_MembersInjector.injectMembers', 'CalculatorActivity_MembersInjector.injectMCurrencyService'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_027.grep.txt)

UNREACHABLE['CalculatorActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (not in the source root). Its only caller record is CalculatorActivity_MembersInjector.create (auto_calls.json, CalculatorActivity_MembersInjector.java:31), and create has no caller record. The component calls the static injectFormatUtilitiesLazy and injectMCurrencyService methods instead (DaggerMmxComponent.java:380-381). No MembersInjector reference exists in the app source (label_027.grep.txt, section A)',
  'auto_calls.json (CalculatorActivity_MembersInjector.java:31; 0 callers of create); label_027.grep.txt sections A and B',
  'INFERRED')

UNREACHABLE['CalculatorActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (not in the source root) with no caller record in auto_calls.json (0 callers). The component does not call it: DaggerMmxComponent.injectCalculatorActivity calls the static inject methods directly (DaggerMmxComponent.java:380-381). No MembersInjector reference exists in the app source (label_027.grep.txt, section A)',
  'python-printed auto_calls query (0 callers); label_027.grep.txt sections A and B',
  'INFERRED')

UNREACHABLE['CalculatorActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (not in the source root) with no caller record for any receiver in auto_calls.json. The component reaches the fields through the static injectFormatUtilitiesLazy and injectMCurrencyService methods (DaggerMmxComponent.java:380-381), so this method never runs. Its two outgoing call records are cut by sup',
  'python-printed auto_calls query (0 callers); auto_calls.json (CalculatorActivity_MembersInjector.java:37-38, outgoing); label_027.grep.txt sections A and B',
  'INFERRED')
