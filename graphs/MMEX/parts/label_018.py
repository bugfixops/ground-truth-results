# batch 018 (label_018): BudgetListFragment (18 methods) and BudgetListFragment$1 (2), BudgetNameParser (6), BudgetPeriodEnum.<clinit>, BudgetPeriods (7), BudgetQuery (3), BudgetService (3); rows and printed lines: graphs/MMEX/parts/label_018.md.
# The list is shown on page S_BUDGETS, defined in label_019.py (BudgetsActivity hosts this fragment), so no page is defined here. S_BUDGET_DETAIL is defined in label_016.py and is not redefined. CALL edges come from auto_calls.json, so none are written here.
# Framework and androidx claims are INFERRED where the library source was not read. grep evidence for the no-caller claims is in label_018.grep.txt.

# ---- fragment lifecycle (androidx Fragment; library source not read: INFERRED)

e('BudgetListFragment.<init>', 'BudgetListFragment.onCreate', 'LIFECYCLE',
  'BudgetsActivity.createFragments commits the transaction that adds the fragment (replace at line 121, commit at line 122), and the FragmentManager then calls onCreate',
  evidence='SRC budget/BudgetsActivity.java:117, 121-122; SRC budget/BudgetListFragment.java:63-64, 95-98; INFERRED androidx Fragment lifecycle (library source not read)')

e('AbsListFragment.onCreateView', 'BudgetListFragment.onViewCreated', 'LIFECYCLE',
  'the framework calls onViewCreated after the view is created by the inherited onCreateView (AbsListFragment inflates abs_list_fragment)',
  evidence='SRC core/AbsListFragment.java:77-79; SRC budget/BudgetListFragment.java:119-123; INFERRED androidx Fragment lifecycle (library source not read)')

e('BudgetListFragment.onViewCreated', 'BudgetListFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onViewCreated; onActivityCreated shows the + button, attaches it to the list and registers the list for the context menu',
  evidence='SRC budget/BudgetListFragment.java:85-92, 119-123; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- loader callbacks (androidx LoaderManager; library not read: INFERRED)

e('BudgetListFragment.displayBudgets', 'BudgetListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader (line 235) starts the budget loader and the LoaderManager calls onCreateLoader',
  evidence='SRC budget/BudgetListFragment.java:52-53, 235; INFERRED androidx LoaderManager.initLoader calls LoaderCallbacks.onCreateLoader (library not read)')

e('BudgetListFragment.onActivityResult', 'BudgetListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader (line 114) after a budget edit starts the loader again, and the LoaderManager calls onCreateLoader through the callbacks',
  evidence='SRC budget/BudgetListFragment.java:107-116; INFERRED androidx LoaderManager.restartLoader creates the loader through the callbacks (library not read)')

e('BudgetListFragment.onCreateLoader', 'BudgetListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader (MmxCursorLoader, line 136) delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC budget/BudgetListFragment.java:127-139, 141-152; INFERRED androidx Loader delivers its result to the callbacks (library not read)')

e('BudgetListFragment.onLoadFinished', 'BudgetListFragment.onLoaderReset', 'FRAMEWORK',
  'a loader that has delivered data is reset (the fragment is destroyed, or restartLoader at line 114 replaces it) and the LoaderManager calls onLoaderReset',
  evidence='SRC budget/BudgetListFragment.java:141-159; INFERRED androidx LoaderManager calls onLoaderReset when a loader with data is destroyed (library not read)')

# ---- result of the editor: BudgetEditActivity sets RESULT_OK when the budget is saved (batch 017 owns the activity)

e('BudgetEditActivity.onActionDoneClick', 'BudgetListFragment.onActivityResult', 'RESULT',
  'the budget editor saves and finishes: setResult(RESULT_OK) (line 67), and the framework calls onActivityResult of the fragment that started it (startActivityForResult, lines 243 and 249)',
  guard='the result is not RESULT_CANCELED (line 111) and the request is REQUEST_EDIT_BUDGET (line 113)',
  evidence='SRC budget/BudgetEditActivity.java:65-73 (setResult 67, finish 68); SRC budget/BudgetListFragment.java:107-116, 238-250; INFERRED androidx Fragment.startActivityForResult dispatches the result to the fragment (library not read)')

# ---- the row menu: long-press a row (the list is registered for the menu in onActivityCreated, line 91)

gui('S_BUDGETS','BudgetListFragment.onCreateContextMenu', 'Long-press a budget row to open its menu',
  evidence='SRC budget/BudgetListFragment.java:91, 163-179; FW-SRC core/java/android/view/View.java:12578-12588 (the context menu listener is called with the menu at 12588); FW-SRC core/java/android/app/Fragment.java:1937-1939 (registerForContextMenu; androidx version INFERRED); the long-press gesture step is INFERRED (source not read)')

gui('S_BUDGETS','BudgetListFragment.onContextItemSelected', 'Tap Edit or Delete in the menu of a budget row',
  evidence='SRC budget/BudgetListFragment.java:176-177 (Edit and Delete items), 181-203; FW-SRC core/java/android/app/Activity.java:3466-3473 (FEATURE_CONTEXT_MENU: onContextItemSelected, then mFragments.dispatchContextItemSelected); INFERRED androidx FragmentManager dispatches the item to the fragment (library not read)')

# ---- user actions on the list

gui('S_BUDGETS','BudgetListFragment.onListItemClick', 'Tap a budget row',
  evidence='SRC budget/BudgetListFragment.java:207-216; auto_calls record AbsListFragment$1.onItemClick -> BudgetListFragment.onListItemClick (core/AbsListFragment.java:44)')

gui('S_BUDGETS','BudgetListFragment.onFloatingActionButtonClicked', 'Tap the + button',
  evidence='SRC budget/BudgetListFragment.java:218-221; SRC common/BaseListFragment.java:238-248 (listener 241-246, call at 244); SRC res/layout/abs_list_fragment.xml:83 (@+id/fab); auto_calls record BaseListFragment$2.onClick -> BudgetListFragment.onFloatingActionButtonClicked (BaseListFragment.java:244)')

# ---- the delete confirmation: an AlertDialog built in confirmDelete (no screen of its own)

e('BudgetListFragment.confirmDelete', 'BudgetListFragment$1.onClick', 'FRAMEWORK',
  'the dialog has an OK button: when the user taps OK the framework calls the OK listener (the alert button handler calls onClick)',
  guard='the user taps OK (android.R.string.ok) in the delete confirmation dialog (lines 256-262)',
  evidence='SRC budget/BudgetListFragment.java:252-264 (listener 256-262; show 264); FW-SRC android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC com/android/internal/app/AlertController.java:166 (the button handler calls onClick); the View click dispatch is not printed (source not read): INFERRED for that step')

# ---- auto edges that cannot run

# COPY is never added to the row menu (the add is commented out at line 178), so the COPY case never runs
sup(('BudgetListFragment.onContextItemSelected', 'BudgetService.copy'))  # the case at lines 195-198 never runs
sup(('BudgetListFragment.onContextItemSelected', 'BudgetService.<init>'))  # same COPY case (line 196); BudgetService.<init> stays reachable through BudgetListFragment$1.onClick (line 259)
# BudgetPeriods.getPeriodTranslationForEnum(Context,String) has no caller, so its two bytecode calls cannot run
sup(('BudgetPeriods.getPeriodTranslationForEnum(Context,String)', 'BudgetPeriods.getEnum'))  # getEnum stays reachable through BudgetAdapter.getBudgetPeriodFor (line 241)
sup(('BudgetPeriods.getPeriodTranslationForEnum(Context,String)', 'BudgetPeriods.getPeriodTranslationForEnum(Context,BudgetPeriodEnum)'))  # the enum overload stays reachable through BudgetAdapter.bindView (line 119)

# ---- BudgetNameParser (6 methods), BudgetPeriodEnum.<clinit>, BudgetPeriods.<clinit>, BudgetQuery (3), BudgetService.delete, BudgetListFragment$1.<init> and the other
# methods reached only through auto edges need no edge here: their routes are in label_018.md.

# ---- UNREACHABLE: no caller in the app (grep output: graphs/MMEX/parts/label_018.grep.txt)

UNREACHABLE['BudgetPeriods.<init>'] = (
  'no_trigger_in_app',
  'implicit default constructor of a class whose members are all static: BudgetPeriods is used only through its static methods (BudgetAdapter.java:119, 135, 136, 241). The source root has no "new BudgetPeriods" and no other creation site, and auto_calls.json has no edge into the constructor (label_018.grep.txt)',
  'budget/BudgetPeriods.java:29, 39-157; budget/BudgetAdapter.java:119, 135, 136, 241; grep label_018.grep.txt',
  'SOURCE')

UNREACHABLE['BudgetPeriods.getPeriodTranslationForEnum(Context,String)'] = (
  'no_trigger_in_app',
  'public static overload with no caller: its name occurs only at its declaration (line 66). The other call in the source root, BudgetAdapter.java:119, passes a BudgetPeriodEnum and resolves to the enum overload. auto_calls.json has no edge into it (label_018.grep.txt)',
  'budget/BudgetPeriods.java:66-68; budget/BudgetAdapter.java:119; grep label_018.grep.txt',
  'SOURCE')

UNREACHABLE['BudgetQuery.getAllColumns'] = (
  'no_trigger_in_app',
  'public override of the abstract Dataset.getAllColumns. No call site in the source root reaches it: every call goes through a concrete type (repositories and QueryXxx datasets, label_018.grep.txt), and none is typed as Dataset or BudgetQuery. MmxContentProvider casts query results to Dataset (lines 160, 203, 241, 394) and never calls getAllColumns on them. auto_calls.json has no edge into it.',
  'budget/BudgetQuery.java:52-64; database/Dataset.java:52; grep label_018.grep.txt',
  'SOURCE')

UNREACHABLE['BudgetService.copy'] = (
  'branch_never_taken',
  'the body is empty (only a todo, line 47). Its only caller is the COPY case of BudgetListFragment.onContextItemSelected (lines 195-198; the auto edge at line 197 is removed by sup). No COPY item is added to the row menu: the add is commented out at line 178, and COPY is referenced only at ContextMenuIds.java:27 and in that switch case. So the case never runs.',
  'budget/BudgetService.java:46-48; budget/BudgetListFragment.java:176-178, 195-198; core/ContextMenuIds.java:27',
  'SOURCE')
