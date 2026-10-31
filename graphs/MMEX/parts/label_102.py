# ================================================================== batch 102 (label_102): RecurringTransactionListFragment (22 methods), its anonymous listeners $1 to $5 (13 methods), RecurringTransactionListFragment_MembersInjector (4) and RecurringTransactionViewHolder.<init> (1). 40 methods (graphs/MMEX/scratch/batches/batch_102.txt).
# Rows: graphs/MMEX/parts/label_102.md (36 REACHABLE, 4 UNREACHABLE, 0 INCOMPLETE). Grep and class-file evidence: graphs/MMEX/parts/label_102.grep.txt (sections 1-5).
# SCREENS: none written here. S_RECURRING_LIST is already defined by batch 101 (label_101.py, merged into graph_def.py:8999) and is reused.
# Edges with a batch 102 method as destination (D1) are written here. ENTERS edges start from this batch's onActivityCreated, which owns the source.
# Not written (D7): every auto_calls.json CALL record, for example RecurringTransactionListActivity.onCreate -> RecurringTransactionListFragment.<init> (line 64), BaseListFragment$2.onClick -> onFloatingActionButtonClicked (cut by label_026 sup), and the Dagger chain DaggerMmxComponent.inject -> injectRecurringTransactionListFragment -> injectDateTimeUtilsLazy.
# Not written: the INTENT edge startRecurringTransactionEditActivity -> RecurringTransactionEditActivity.<init> (batch 099 writes it, label_099.py:16).

# ---- activity and drawer routes into the fragment

e('RecurringTransactionListActivity.onCreate', 'RecurringTransactionListFragment.onActivityCreated', 'FRAMEWORK',
  'the activity adds the fragment in a transaction (lines 66-67) and the framework calls onActivityCreated after the activity onCreate',
  evidence='SRC recurring/transactions/RecurringTransactionListActivity.java:64-67; INFERRED androidx FragmentManager commits the transaction and calls onActivityCreated (library not read); precedent label_008.py:48-50 (FRAMEWORK commit -> onActivityCreated)')

e('MainActivity.showFragment_Internal', 'RecurringTransactionListFragment.onActivityCreated', 'FRAMEWORK',
  'the drawer item (MainActivity.java:651-652) reaches showFragment_Internal, which replaces fragmentMain and commits; the framework then calls onActivityCreated',
  evidence='SRC home/MainActivity.java:1446-1466 (replace at 1462, addToBackStack at 1464, commit at 1466); INFERRED androidx FragmentManager calls onActivityCreated after the commit (library not read); precedent label_008.py:48-50 (AccountListFragment)')

e('MainActivity.showFragment(Class)', 'RecurringTransactionListFragment.<init>', 'CALL',
  'the drawer item menu_recurring_transaction calls showFragment(RecurringTransactionListFragment.class), which creates the fragment with classFragment.newInstance()',
  cls='non_standard', via='Class.newInstance reflection in MainActivity.showFragment(Class) (MainActivity.java:743)',
  evidence='SRC home/MainActivity.java:651-652 (case R.id.menu_recurring_transaction); SRC home/MainActivity.java:741-745 (newInstance at 743); precedent label_008.py:42-46 (AccountListFragment.<init>)')

e('RecurringTransactionListFragment.<init>', 'RecurringTransactionListFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the fragment is created; onCreate injects the Dagger component (line 120) and sets the options menu (line 122)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:117-123; INFERRED androidx Fragment lifecycle (library not read); same pattern as label_087.py (LIFECYCLE <init> -> onCreate)')

# ---- onActivityCreated: options menu, loader chain, page entry

e('RecurringTransactionListFragment.onActivityCreated', 'RecurringTransactionListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'setHasOptionsMenu(true) at line 101 makes the framework build the options menu with this fragment; onCreateOptionsMenu inflates menu_item_calendar (line 138) and calls super (line 135)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:101, 134-144; INFERRED androidx FragmentManager builds the options menu (library not read)')

e('RecurringTransactionListFragment.onActivityCreated', 'RecurringTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader(ID_LOADER_REPEATING, null, this) at line 109 starts the loader and the LoaderManager calls onCreateLoader',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:109, 218-232 (onCreateLoader builds the MmxCursorLoader at 228); INFERRED androidx LoaderManager.initLoader calls the LoaderCallbacks (library not read); precedent graph_def.py:950-962 (AccountListFragment loader chain)')

e('RecurringTransactionListFragment.onCreateLoader', 'RecurringTransactionListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:218-232, 246-262; INFERRED androidx Loader delivers its result to the callbacks (library not read)')

e('RecurringTransactionListFragment.onLoadFinished', 'RecurringTransactionListFragment.onLoaderReset', 'FRAMEWORK',
  'the LoaderManager resets the loader when it is restarted (restartLoader at lines 272, 290, 316 and 343) and calls onLoaderReset',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:235-243, 272, 290, 316-317, 343-344; INFERRED androidx LoaderManager resets and calls onLoaderReset (library not read); precedent graph_def.py:950-962 (AccountListFragment.onLoadFinished -> onLoaderReset)')

# ---- restarts that call onCreateLoader again (FRAMEWORK, destination is this batch's onCreateLoader)

e('RecurringTransactionListFragment.onQueryTextChange', 'RecurringTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader at line 272 reloads the list with the search text and the LoaderManager calls onCreateLoader again',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:267-274; grep.txt section 4 (restartLoader at 272); INFERRED androidx LoaderManager.restartLoader calls the callbacks (library not read)')

e('RecurringTransactionListFragment.onActivityResult', 'RecurringTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader at line 290 reloads the list after RESULT_OK and the LoaderManager calls onCreateLoader again',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:277-292; INFERRED androidx LoaderManager.restartLoader calls the callbacks (library not read)')

e('RecurringTransactionListFragment$2.onClick', 'RecurringTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader at lines 316-317 reloads the list after the delete and the LoaderManager calls onCreateLoader again',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:309-319; grep.txt section 2b ($2 refers to LoaderManager.restartLoader); INFERRED androidx LoaderManager.restartLoader calls the callbacks (library not read)')

e('RecurringTransactionListFragment$4.onClick', 'RecurringTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader at lines 343-344 reloads the list after moveNextOccurrence and the LoaderManager calls onCreateLoader again',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:338-346; grep.txt section 2b ($4 refers to LoaderManager.restartLoader); INFERRED androidx LoaderManager.restartLoader calls the callbacks (library not read)')

# ---- page entry: the list page S_RECURRING_LIST (key defined by batch 101)

e('RecurringTransactionListFragment.onActivityCreated', 'S_RECURRING_LIST', 'ENTERS',
  'the list page is shown when onActivityCreated builds the list; both the activity route and the drawer route reach this method',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:94-114; SRC recurring/transactions/RecurringTransactionListActivity.java:64-67; SRC home/MainActivity.java:651-652, 1462')

# ---- calendar: the Caldroid library callback after the view is created (library not in the repo)

e('RecurringTransactionListFragment.showCaldroidFragment', 'RecurringTransactionListFragment$5.onCaldroidViewCreated', 'FRAMEWORK',
  'the Caldroid library calls onCaldroidViewCreated after it creates the calendar view for the fragment; the listener is set at line 380 and the fragment is shown at line 384',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:357-387 (getCalendarListener at 380; replace(R.id.fragmentMain) at 384); SRC same file 406-408 (empty body); INFERRED Caldroid library callback (library not in the repo; grep.txt section 1)')

# ---- result of the edit forms: RESULT edges into this batch's onActivityResult

e('RecurringTransactionEditActivity.onActionDoneClick', 'RecurringTransactionListFragment.onActivityResult', 'RESULT',
  'the edit form saves, calls setResult(RESULT_OK) and finishes; the result returns to the activity that started it, and the fragment (started at line 458) receives it in onActivityResult',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:207-211 (setResult at 210); SRC recurring/transactions/RecurringTransactionListFragment.java:447-459 (startActivityForResult at 458); INFERRED androidx FragmentActivity dispatches the result to the fragment (library not read); precedent graph_def.py:1656 (BudgetListFragment RESULT edge)')

e('CheckingTransactionEditActivity.onActionDoneClick', 'RecurringTransactionListFragment.onActivityResult', 'RESULT',
  'the checking transaction editor opened for a new transaction saves, calls setResult(RESULT_OK) and finishes; the fragment started it at line 437 and receives the result in onActivityResult',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:194-197 (setResult at 196); SRC recurring/transactions/RecurringTransactionListFragment.java:427-438 (startActivityForResult at 437); INFERRED androidx FragmentActivity dispatches the result to the fragment (library not read)')

# ---- GUI edges from the list page S_RECURRING_LIST (D6, D9: dialogs and calendar belong to the list page)

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onFloatingActionButtonClicked', 'Tap the add (floating action) button',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:126-129 (startRecurringTransactionEditActivity at 128); the FAB click listener BaseListFragment$2.onClick (BaseListFragment.java:244) is cut by label_026.py sup, and its comment says the owning batch writes this GUI edge')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onListItemClick', 'Tap a bill or deposit row (the row opens its context menu)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:156-161 (openContextMenu(v) at 160); auto_calls record AbsListFragment$1.onItemClick -> onListItemClick (AbsListFragment.java:44) is not repeated (D7)')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onCreateContextMenu', 'Long-press a row (registerForContextMenu is called at line 102)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:102, 164-176 (contextmenu_repeating_transactions inflated at 174); res/menu/contextmenu_repeating_transactions.xml:20, 24, 28, 32')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onContextItemSelected', 'Tap an item of the row context menu',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:179-213 (branches at 196, 200, 204, 208); res/menu/contextmenu_repeating_transactions.xml:20, 24, 28, 32')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onOptionsItemSelected', 'Tap the calendar icon in the action bar (menuCalendar)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:147-153 (menuCalendar check at 149; showCaldroidFragment at 150); res/menu/menu_item_calendar.xml:22')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment.onQueryTextChange', 'Type in the search box of the list',
  evidence='SRC common/BaseListFragment.java:128 (BaseListFragment$1.onQueryTextChange, auto_calls 4602); SRC recurring/transactions/RecurringTransactionListFragment.java:267-274; auto_calls record BaseListFragment.onPreQueryTextChange@RecurringTransactionListFragment -> onQueryTextChange (line 226) is not repeated (D7)')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$1.onClick', 'Tap Cancel in the delete confirmation dialog (the dialog is shown on the list page, D9)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:320-325 (negative button; dialog.cancel() at 323); grep.txt section 2b ($1 refers only to DialogInterface.cancel)')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$2.onClick', 'Tap OK in the delete confirmation dialog (deletes the bill or deposit and reloads the list)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:309-319 (RecurringTransactionService delete at 313; restartLoader at 316-317); grep.txt section 2b')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$3.onClick', 'Tap Cancel in the skip next occurrence dialog',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:347-352 (dialog.cancel() at 350); grep.txt section 2b ($3 refers only to DialogInterface.cancel)')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$4.onClick', 'Tap OK in the skip next occurrence dialog (moves to the next occurrence and reloads the list)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:338-346 (moveNextOccurrence at 342; restartLoader at 343-344); grep.txt section 2b')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$5.onSelectDate', 'Tap a date in the calendar (the calendar replaces the list in fragmentMain, D9)',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:393-396 (comment only, empty body); SRC same file 384 (replace in fragmentMain); INFERRED Caldroid library calls onSelectDate on a tap (library not in the repo)')

gui('S_RECURRING_LIST', 'RecurringTransactionListFragment$5.onLongClickDate', 'Long-press a date in the calendar',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:402-404 (empty body); INFERRED Caldroid library calls onLongClickDate on a long press (library not in the repo)')

# ================================================================== sup pairs (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('RecurringTransactionListFragment_MembersInjector.create', 'RecurringTransactionListFragment_MembersInjector.<init>'),
    ('RecurringTransactionListFragment_MembersInjector.injectMembers', 'RecurringTransactionListFragment_MembersInjector.injectDateTimeUtilsLazy'))

# ================================================================== UNREACHABLE (batch 102). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['RecurringTransactionListFragment_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller is create (auto_calls record RecurringTransactionListFragment_MembersInjector.java:25), and create has no caller: no class file refers to create (grep.txt section 2c).',
  'grep.txt sections 2c and 3; python-printed auto_calls record RecurringTransactionListFragment_MembersInjector.java:25',
  'INFERRED')

UNREACHABLE['RecurringTransactionListFragment_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated factory method. No class file refers to create (grep.txt section 2c: none), and no app source names the injector (grep.txt section 1: no hits). DaggerMmxComponent calls the static injectDateTimeUtilsLazy directly (DaggerMmxComponent.java:466), not create.',
  'grep.txt sections 1, 2c and 3; DaggerMmxComponent.java:466 (auto_calls record)',
  'INFERRED')

UNREACHABLE['RecurringTransactionListFragment_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated typed instance method (the synthetic bridge injectMembers(Object) is not in this batch, same convention as batch 087). No class file refers to it (grep.txt section 2c), so its only outgoing record injectMembers -> injectDateTimeUtilsLazy (MembersInjector.java:30) is cut by the sup pair.',
  'grep.txt sections 2c and 3; python-printed auto_calls record RecurringTransactionListFragment_MembersInjector.java:30',
  'INFERRED')

UNREACHABLE['RecurringTransactionListFragment$5.onChangeMonth'] = ('no_trigger_in_app',
  'Caldroid month-change callback with an empty body (lines 398-400). The calendar is set with SHOW_NAVIGATION_ARROWS and ENABLE_SWIPE both false (lines 372-373), and no app code calls moveToDate, prevMonth or nextMonth (grep.txt section 1), so no user or app action changes the month. The library behaviour itself is INFERRED because the library is not in the repo.',
  'SRC recurring/transactions/RecurringTransactionListFragment.java:372-373, 398-400; grep.txt section 1 (no hits for moveToDate, prevMonth, nextMonth)',
  'INFERRED')
