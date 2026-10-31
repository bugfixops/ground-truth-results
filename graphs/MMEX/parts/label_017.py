# ================================================================== batch 017 (label_017): com.money.manager.ex.budget.BudgetEditActivity (with $1, $2), its ButterKnife binding (with $1, $2), BudgetEditViewHolder and its ButterKnife binding (30 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_017.md.
# Every edge below has a batch 017 method as its destination, or is the ENTERS edge to the page this batch defines (S_BUDGET_EDIT).
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here, except the two ButterKnife constructor calls that the bytecode does not record.
# Framework and library claims are INFERRED where the library source was not read (AppCompat, ButterKnife, AlertDialog). grep evidence: graphs/MMEX/parts/label_017.grep.txt.

SCREENS.update({
    'S_BUDGET_EDIT': 'Budget edit (BudgetEditActivity): the budget name, year and month fields, the save icon and the Up arrow in the toolbar, and the year and month pickers',
})

# ---- entry into the activity: started by the budget list only (not exported and no intent filter: AndroidManifest.xml:357, so no ENTRY edge)

e('BudgetListFragment.editBudget', 'BudgetEditActivity.<init>', 'INTENT',
  'editBudget starts BudgetEditActivity with ACTION_EDIT and the budget id (KEY_BUDGET_ID) through startActivityForResult',
  gui=['Open the context menu of a budget row in the budget list and choose Edit'],
  guard='the context-menu item is EDIT (switch case at line 189)',
  evidence='SRC budget/BudgetListFragment.java:186-190 (switch on the menu id; editBudget at 190), 238-244 (intent 239-241; startActivityForResult 243); SRC AndroidManifest.xml:357')

e('BudgetListFragment.createBudget', 'BudgetEditActivity.<init>', 'INTENT',
  'createBudget starts BudgetEditActivity with ACTION_INSERT through startActivityForResult',
  gui=['Tap the add button (floating action button) on the budget list'],
  evidence='SRC budget/BudgetListFragment.java:218-221 (onFloatingActionButtonClicked calls createBudget at 220), 246-250 (intent 247-248; startActivityForResult 249)')

e('BudgetEditActivity.<init>', 'BudgetEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/Instrumentation.java:1143 (newActivity), 1212-1215 (callActivityOnCreate); FW-SRC core/java/android/app/ActivityThread.java:2669, 2729-2731; SRC budget/BudgetEditActivity.java:43-44, 52-54')

# ---- the screen: onCreate sets the layout and fills the fields

e('BudgetEditActivity.onCreate', 'S_BUDGET_EDIT', 'ENTERS',
  'the budget edit form is shown: onCreate sets the layout (line 55) and binds the model to the fields (lines 61-62)',
  evidence='SRC budget/BudgetEditActivity.java:55, 61-62; SRC res/layout/activity_budget_edit.xml:65 (toolbar), 134 (budgetNameTextView), 173 (budgetYearTextView), 213 (budgetMonthTextView)')

# ---- ButterKnife bindings: the generated classes are built by reflection in ButterKnife.bind (library and generated source not read)

e('BudgetEditActivity.onCreate', 'BudgetEditActivity_ViewBinding.<init>(BudgetEditActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for this activity, which binds the @OnClick handlers and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated BudgetEditActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC budget/BudgetEditActivity.java:57; INFERRED ButterKnife generated binding (library and generated source not read); no auto_calls record has onCreate as src with this destination (label_017.grep.txt)')

e('BudgetEditViewHolder.<init>', 'BudgetEditViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, activity) builds the generated binding for the holder, which binds the three text views',
  cls='non_standard', via='ButterKnife.bind(this, activity) (library): the generated BudgetEditViewHolder_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC budget/BudgetEditViewHolder.java:33-35 (bind at 34); INFERRED ButterKnife generated binding (library and generated source not read); no auto_calls record has BudgetEditViewHolder.<init> as src (label_017.grep.txt)')

e('S_BUDGET_EDIT', 'BudgetEditActivity_ViewBinding$1.doClick', 'GUI',
  'tap the year field (budgetYearTextView): the @OnClick listener attached by the generated binding calls onSelectYear',
  gui=['Tap the year field of the budget'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class)',
  evidence='SRC budget/BudgetEditActivity.java:98 (@OnClick budgetYearTextView); SRC res/layout/activity_budget_edit.xml:173; auto_calls.json:57838-57839 (doClick calls onSelectYear); auto_calls.json:57862-57863 (the binding constructor creates $1)')

e('S_BUDGET_EDIT', 'BudgetEditActivity_ViewBinding$2.doClick', 'GUI',
  'tap the month field (budgetMonthTextView): the @OnClick listener attached by the generated binding calls onSelectMonth',
  gui=['Tap the month field of the budget'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class)',
  evidence='SRC budget/BudgetEditActivity.java:129 (@OnClick budgetMonthTextView); SRC res/layout/activity_budget_edit.xml:213; auto_calls.json:57414-57415 (doClick calls onSelectMonth); auto_calls.json:57854-57855 (the binding constructor creates $2)')

# ---- options menu: the framework builds it after setContentView hands the toolbar to setSupportActionBar (AppCompat step INFERRED)

e('BudgetEditActivity.onCreate', 'BudgetEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'setContentView gives the toolbar to setSupportActionBar, and the framework then builds the options menu through onCreatePanelMenu, which calls onCreateOptionsMenu',
  guard='the layout has the toolbar (R.id.toolbar at activity_budget_edit.xml:65)',
  evidence='SRC common/MmxBaseFragmentActivity.java:99-104 (setContentView; setSupportActionBar at 103); SRC res/layout/activity_budget_edit.xml:65; FW-SRC core/java/android/app/Activity.java:3386-3388 (onCreatePanelMenu calls onCreateOptionsMenu); FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:631; INFERRED AppCompat builds the action-bar menu after setSupportActionBar (AppCompat not read)')

e('S_BUDGET_EDIT', 'BudgetEditActivity.onOptionsItemSelected', 'GUI',
  'tap the save icon in the toolbar (it runs onActionDoneClick, which saves the budget) or the Up arrow (the home item, logged and passed to the base class)',
  gui=['Tap the save icon in the toolbar, or the Up arrow'],
  guard='the save icon exists: onCreateOptionsMenu adds it (line 80)',
  evidence='SRC budget/BudgetEditActivity.java:76-83 (save icon via MenuHelper at 79-80), 86-96 (home at 88-91; save at 92-93); SRC core/MenuHelper.java:37 (save = 2), 87-94 (addSaveToolbarIcon; menu.add at 88); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected); INFERRED AppCompat dispatches the item to onOptionsItemSelected (library not read)')

# ---- the picker dialogs: the OK buttons reach the listeners (AlertDialog positive-button dispatch INFERRED)

e('S_BUDGET_EDIT', 'BudgetEditActivity$1.onClick', 'GUI',
  'tap OK in the year picker: the listener sets the year on the model and refreshes the year and the name',
  gui=['Tap OK in the year picker dialog'],
  guard='the year picker is open: onSelectYear shows it (line 126)',
  evidence='SRC budget/BudgetEditActivity.java:113-126 (AlertDialog built and shown; positive button 116-124; onClick 118-123); INFERRED AlertDialog positive-button dispatch (AlertController not read)')

e('S_BUDGET_EDIT', 'BudgetEditActivity$2.onClick', 'GUI',
  'tap OK in the month picker: the listener sets the month on the model and refreshes the month and the name',
  gui=['Tap OK in the month picker dialog'],
  guard='the month picker is open: onSelectMonth shows it (line 156)',
  evidence='SRC budget/BudgetEditActivity.java:143-156 (AlertDialog built and shown; positive button 146-154; onClick 148-153); INFERRED AlertDialog positive-button dispatch (AlertController not read)')

# ================================================================== UNREACHABLE (batch 017)

UNREACHABLE['BudgetEditActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root): ButterKnife.bind(this) at BudgetEditActivity.java:57 discards the Unbinder it returns (no unbind or Unbinder use in the source root), BudgetEditActivity has no onDestroy, and no call record in auto_calls.json has unbind as its destination (label_017.grep.txt)',
  'SRC budget/BudgetEditActivity.java:52-63; label_017.grep.txt; python-printed auto_calls query (0 unbind destinations in the calls section)',
  'INFERRED')

UNREACHABLE['BudgetEditViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root): ButterKnife.bind(this, activity) at BudgetEditViewHolder.java:34 discards the Unbinder it returns, BudgetEditViewHolder has no unbind or onDestroy, and no call record in auto_calls.json has unbind as its destination (label_017.grep.txt)',
  'SRC budget/BudgetEditViewHolder.java:33-35; label_017.grep.txt; python-printed auto_calls query (0 unbind destinations in the calls section)',
  'INFERRED')

sup(('MmxBaseFragmentActivity$2.onClick', 'BudgetEditActivity.onActionDoneClick'))  # the done listener is installed only by CurrencyEditActivity (BudgetsActivity's toolbar.xml has no action_done view), and BudgetEditActivity has neither the call nor an action_done view
