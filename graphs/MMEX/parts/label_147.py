# ================================================================== part 147 (label_147): receiver-variant and dialog-listener edges for the nine frontier methods
# Written by the orchestrator (2026-10-31). No methods are owned here: no UNREACHABLE entries, no sups.
# The reached copies (X@Recv, auto_calls.json) are linked from the plain node that calls them, because hand edges keyed on a
# plain name are not followed from a receiver-variant node (tools/build_graph.py add_auto_edges). The report options menu is
# reached from the copy, so its FRAMEWORK edges name the copy as the source.

# ---- report options menu: the receiver copy of BaseReportFragment.onActivityCreated sets the menu flag (BaseReportFragment.java:79)

e('BaseReportFragment.onActivityCreated@CategoriesReportFragment', 'CategoriesReportFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'the categories report sets setHasOptionsMenu(true) in onActivityCreated, so the framework builds the options menu and calls onCreateOptionsMenu on the fragment',
  evidence='SRC reports/BaseReportFragment.java:74-79 (onActivityCreated on a CategoriesReportFragment receiver; setHasOptionsMenu at 79); SRC reports/CategoriesReportFragment.java:102-113 (onCreateOptionsMenu; super at 104); auto_calls.json record CategoriesReportFragment.onActivityCreated -> BaseReportFragment.onActivityCreated@CategoriesReportFragment (line 55523); INFERRED androidx FragmentManager dispatches onCreateOptionsMenu (library not read)')

e('BaseReportFragment.onActivityCreated@PayeeReportFragment', 'PayeeReportFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'the payee report sets setHasOptionsMenu(true) in onActivityCreated, so the framework builds the options menu and calls onCreateOptionsMenu on the fragment',
  evidence='SRC reports/BaseReportFragment.java:74-79 (onActivityCreated on a PayeeReportFragment receiver; setHasOptionsMenu at 79); SRC reports/PayeeReportFragment.java:194-196 (onCreateOptionsMenu; super at 196); auto_calls.json record PayeeReportFragment.onActivityCreated -> BaseReportFragment.onActivityCreated@PayeeReportFragment (line 55891); INFERRED androidx FragmentManager dispatches onCreateOptionsMenu (library not read)')

# ---- category picker: the base class finishes and filters through the overridable hooks; CategoryListFragment overrides them

e('BaseExpandableListFragment.setResultAndFinish', 'BaseExpandableListFragment.setResultAndFinish@CategoryListFragment', 'CALL',
  'the category picker finishes through setResultAndFinish on a CategoryListFragment instance: the home arrow, or a category row tap; the base method calls setResult, which CategoryListFragment overrides',
  cls='standard',
  evidence='SRC common/BaseExpandableListFragment.java:158-164 (home arrow calls setResultAndFinish at 164), 260-265 (setResultAndFinish calls this.setResult at 262); SRC common/CategoryListFragment.java:313 (setResult override), 661-698 (row taps call setResultAndFinish at 675 and 695)')

e('BaseExpandableListFragment.onPreQueryTextChange', 'BaseExpandableListFragment.onPreQueryTextChange@CategoryListFragment', 'CALL',
  'the user types in the category picker search box: onPreQueryTextChange calls onQueryTextChange, which CategoryListFragment overrides without calling super',
  cls='standard',
  evidence='SRC common/BaseExpandableListFragment.java:206-215 (onPreQueryTextChange calls onQueryTextChange at 210; base body returns true at 213-215); SRC common/CategoryListFragment.java:230 (onQueryTextChange override); INFERRED androidx SearchView calls the listener on each text change (library not read), the same listener convention as the existing edges at graph_def.py 1899-1902')

# ---- account picker: the Back key in AccountListActivity and the home arrow both finish through setResultAndFinish

e('BaseListFragment.setResultAndFinish', 'BaseListFragment.setResultAndFinish@AccountListFragment', 'CALL',
  'the account picker finishes through setResultAndFinish on an AccountListFragment instance: the Back key in AccountListActivity, or the home arrow; the base method calls setResult, which AccountListFragment overrides',
  cls='standard',
  evidence='SRC account/AccountListActivity.java:60-68 (onKeyUp calls fragment.setResultAndFinish at 64); SRC common/BaseListFragment.java:151-161 (home arrow at 157), 177-180 (setResultAndFinish calls setResult at 178); SRC account/AccountListFragment.java:221 (setResult override, ACTION_PICK at 223)')

# ---- payee context menu: the DELETE warning dialog's OK button runs the listener lambda

e('PayeeListFragment.onContextItemSelected', 'PayeeListFragment.lambda$onContextItemSelected$0', 'FRAMEWORK',
  'deleting a payee that transactions use shows a warning dialog, and its OK button calls the listener that dismisses it',
  needs_state=state_text('a transaction uses the payee, so PayeeService.isPayeeUsed is true and the warning dialog is shown (data)', ('data',)),
  evidence='SRC fragment/PayeeListFragment.java:217-229 (DELETE: isPayeeUsed at 219; AlertDialog.Builder with the positive-button lambda at 226; show at 228); FW-SRC core/java/com/android/internal/app/AlertController.java:1022 (dialog.setButton for BUTTON_POSITIVE), 127-130 (click posts the message), 149-166 (ButtonHandler calls the OnClickListener)')

# ---- date field: the DatePickerDialog listener lambda runs when the positive button is tapped

e('EditTransactionCommonFunctions$5.onClick', 'EditTransactionCommonFunctions$5.lambda$onClick$0', 'FRAMEWORK',
  'the user taps the date field, the date picker opens, and the positive button calls the OnDateSetListener lambda that sets the date',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:488-496 (anonymous $5 at 488; onClick at 490; the listener lambda at 493-496), 507 (datePicker.show()); FW-SRC core/java/android/app/DatePickerDialog.java:122-123 (positive button with this as listener), 164-171 (onClick calls mDateSetListener.onDateSet on BUTTON_POSITIVE); FW-SRC core/java/com/android/internal/app/AlertController.java:127-130, 149-166 (button click reaches the listener)')
