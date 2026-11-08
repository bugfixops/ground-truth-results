# batch 016 (label_016): BudgetAdapter (17 methods), BudgetAdapter_MembersInjector (4), BudgetDetailFragment (10) and BudgetDetailFragment$1 (4); rows and printed lines: graphs/MMEX/parts/label_016.md.
# Page S_BUDGET_DETAIL is defined here (no budget page exists yet). CALL edges come from auto_calls.json, so none are written here. Dagger members are generated code (not in the source root): INFERRED; grep evidence in label_016.grep.txt.

SCREENS.update({
    'S_BUDGET_DETAIL': 'Budget detail (BudgetDetailFragment): the categories and subcategories of one budget, with the budgeted amount, the period, the actual amount and the amount available',
})

# ---- fragment lifecycle (androidx Fragment and BaseListFragment; library source not read: INFERRED)

e('BudgetDetailFragment.<init>', 'BudgetDetailFragment.onCreate', 'LIFECYCLE',
  'BudgetsActivity.showFragment commits the transaction that adds the fragment (line 175), and the FragmentManager then calls onCreate (onAttach is an androidx method and is not in this class)',
  evidence='SRC budget/BudgetDetailFragment.java:68, 78; SRC budget/BudgetsActivity.java:137, 140, 149-175; INFERRED androidx Fragment lifecycle (library source not read)')

e('BudgetDetailFragment.onCreate', 'BudgetDetailFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC budget/BudgetDetailFragment.java:78, 88; INFERRED androidx Fragment lifecycle (library source not read)')

e('BudgetDetailFragment.onCreateView', 'BudgetDetailFragment.onViewCreated', 'LIFECYCLE',
  'the framework calls onViewCreated after onCreateView; onViewCreated starts the budget loader (displayBudget)',
  evidence='SRC budget/BudgetDetailFragment.java:88, 121-122; INFERRED androidx Fragment lifecycle (library source not read)')

e('BudgetDetailFragment.onViewCreated', 'BudgetDetailFragment.onDestroyView', 'LIFECYCLE',
  'the framework destroys the view when the fragment is removed or replaced (BudgetsActivity.showFragment replaces R.id.fragmentMain or R.id.fragmentDetail) or the activity is destroyed',
  evidence='SRC budget/BudgetDetailFragment.java:113-118; SRC budget/BudgetsActivity.java:162, 165; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- the screen: the column header and the adapter are set up in onCreateView

e('BudgetDetailFragment.onCreateView', 'S_BUDGET_DETAIL', 'ENTERS',
  'the budget detail list is shown: the column header is added to the list and the BudgetAdapter is set on it (setUpAdapter, line 105)',
  evidence='SRC budget/BudgetDetailFragment.java:101-105, 145; SRC budget/BudgetAdapter.java:71-83')

# ---- loader callbacks (androidx LoaderManager; library not read: INFERRED)

e('BudgetDetailFragment.displayBudget', 'BudgetDetailFragment$1.onCreateLoader', 'FRAMEWORK',
  'initLoader (line 132) starts the budget detail loader and the LoaderManager calls onCreateLoader',
  evidence='SRC budget/BudgetDetailFragment.java:127-132, 149-160; INFERRED androidx LoaderManager.initLoader calls LoaderCallbacks.onCreateLoader (library not read)')

e('BudgetDetailFragment$1.onCreateLoader', 'BudgetDetailFragment$1.onLoadFinished', 'FRAMEWORK',
  'the loader (MmxCursorLoader, line 159) delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC budget/BudgetDetailFragment.java:151-159, 165; SRC common/MmxCursorLoader.java:39; INFERRED androidx Loader delivers its result to the callbacks (library not read)')

e('BudgetDetailFragment$1.onLoadFinished', 'BudgetDetailFragment$1.onLoaderReset', 'FRAMEWORK',
  'a loader that has delivered data is reset (fragment destroyed or loader restarted) and the LoaderManager calls onLoaderReset',
  evidence='SRC budget/BudgetDetailFragment.java:165-169, 180-184; INFERRED androidx LoaderManager calls onLoaderReset when a loader with data is destroyed (library not read)')

# ---- the list draws the rows after the cursor is set: changeCursor notifies the list, and the adapter views are made through CursorAdapter.getView

e('BudgetDetailFragment$1.onLoadFinished', 'BudgetAdapter.newView', 'FRAMEWORK',
  'adapter.changeCursor (line 169) notifies the list, which asks the adapter for row views; CursorAdapter.getView calls newView when there is no view to reuse',
  guard='the loader delivered a cursor: changeCursor (line 169) makes the adapter valid and it has rows',
  evidence='SRC budget/BudgetDetailFragment.java:165-169; SRC budget/BudgetAdapter.java:92-96; FW-SRC core/java/android/widget/CursorAdapter.java:276-289 (getView calls newView at 285 when convertView is null, then bindView at 289), 348-381 (changeCursor, swapCursor, notifyDataSetChanged at 381); INFERRED androidx CursorAdapter and ListView draw path (not in fw_src)')

e('BudgetDetailFragment$1.onLoadFinished', 'BudgetAdapter.bindView', 'FRAMEWORK',
  'the same notification: CursorAdapter.getView calls bindView for each visible row after changeCursor (line 169)',
  guard='the loader delivered a cursor: changeCursor (line 169) makes the adapter valid and it has rows',
  evidence='SRC budget/BudgetDetailFragment.java:165-169; SRC budget/BudgetAdapter.java:98-99; FW-SRC core/java/android/widget/CursorAdapter.java:276-289 (bindView at 289); INFERRED androidx CursorAdapter and ListView draw path (not in fw_src)')

# ---- auto edges that cannot run: their source has no caller or is UNREACHABLE (see the entries below)

sup(('BudgetAdapter.getAmountForSubCategory', 'BudgetAdapter.loadTotalFor'))  # getAmountForSubCategory has no caller, so this bytecode call cannot run
sup(('BudgetAdapter_MembersInjector.create', 'BudgetAdapter_MembersInjector.<init>'))  # create has no caller, so the constructor call cannot run
sup(('BudgetAdapter_MembersInjector.injectMembers', 'BudgetAdapter_MembersInjector.injectDatabaseLazy'))  # injectMembers has no caller, so this call cannot run

# ---- UNREACHABLE: no caller in the app (grep output: graphs/MMEX/parts/label_016.grep.txt)

UNREACHABLE['BudgetAdapter.getAmountForSubCategory'] = (
  'no_trigger_in_app',
  'private method with no caller in the app: its only occurrences in the source root are the declaration (line 260) and a commented-out call in getActualAmount (line 214). getActualAmount calls getAmountForCategory in both branches (lines 210 and 213), and the bytecode call graph has no edge into it (label_016.grep.txt)',
  'budget/BudgetAdapter.java:204-217, 255-263; grep label_016.grep.txt',
  'SOURCE')

UNREACHABLE['BudgetAdapter_MembersInjector.<init>'] = (
  'no_trigger_in_app',
  'constructor of the Dagger members injector, reached only from create (auto_calls.json:58029-58036). create has no caller (see BudgetAdapter_MembersInjector.create), so the constructor never runs. Generated code: INFERRED.',
  'auto_calls.json:58029-58036; graphs/MMEX/parts/label_016.grep.txt',
  'INFERRED')

UNREACHABLE['BudgetAdapter_MembersInjector.create'] = (
  'no_trigger_in_app',
  'static factory of the Dagger members injector with no caller: no edge in the bytecode call graph has it as a callee (grep: no dst match). The component injects statically: injectBudgetAdapter calls injectDatabaseLazy directly (auto_calls.json:19175-19182), so no injector object is built. Generated code, not in the source root: INFERRED.',
  'auto_calls.json:58029-58036, 19175-19182; graphs/MMEX/parts/label_016.grep.txt',
  'INFERRED')

UNREACHABLE['BudgetAdapter_MembersInjector.injectMembers'] = (
  'no_trigger_in_app',
  'instance method of the Dagger members injector. It is reached only through the MembersInjector interface on an injector object that create would make, and create has no caller. No call to any injectMembers appears in the bytecode call graph (grep: no dst match), and the component injects statically through injectDatabaseLazy (auto_calls.json:19175-19182). Generated code: INFERRED.',
  'auto_calls.json:58037-58044, 19175-19182; graphs/MMEX/parts/label_016.grep.txt',
  'INFERRED')
