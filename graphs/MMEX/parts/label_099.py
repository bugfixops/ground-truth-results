# ================================================================== batch 099 (label_099): com.money.manager.ex.recurring.transactions.RecurringTransactionEditActivity (methods 1-40 of 41 in this class group; the 41st, RecurringTransactionEditActivity$4.onClick, is in another batch and its GUI edge is written there)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_099.md (40 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE).
# Grep and sed evidence: graphs/MMEX/parts/label_099.grep.txt.
# This file writes 20 e() edges and 5 gui() edges (25 edges), one SCREENS key, 0 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). The INTENT edge from RecurringTransactionListFragment is interim: that class belongs to batch 102, which is not merged.
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here (D7).
# REGISTER edges are skipped by reachability (label_032.py:13), so the onEvent methods are reached through their ASYNC posts.
# Framework claims cite FW-SRC lines printed for this batch; other claims are INFERRED where the source was not read.

SCREENS.update({
    'S_RECURRING_TRANSACTION_EDIT': 'Recurring transaction edit form (RecurringTransactionEditActivity): payment date with the day arrows, the frequency spinner, payments left, the shared transaction controls, save and cancel',
})

# ---- the intent into the activity, then the lifecycle calls

e('RecurringTransactionListFragment.startRecurringTransactionEditActivity', 'RecurringTransactionEditActivity.<init>', 'INTENT',
  'the recurring transaction list starts the editor: ACTION_EDIT with KEY_BILL_DEPOSITS_ID when an id is passed, otherwise ACTION_INSERT',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:447-458 (ACTION_EDIT with KEY_BILL_DEPOSITS_ID when the id is not null, else ACTION_INSERT; startActivityForResult); callers at 128 (FAB) and 204 (menu_edit); that class belongs to batch 102, which is not merged, so this INTENT edge is interim')

e('RecurringTransactionEditActivity.<init>', 'RecurringTransactionEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('RecurringTransactionEditActivity.onCreate', 'RecurringTransactionEditActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity: ActivityThread calls callCallActivityOnSaveInstanceState, which calls onSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3873-3876 (callCallActivityOnSaveInstanceState at 3875); FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState at 1496)')

# ---- the screen, and the options menu built by the window

e('RecurringTransactionEditActivity.onCreate', 'S_RECURRING_TRANSACTION_EDIT', 'ENTERS',
  'the recurring transaction edit form is shown',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:98 (setContentView R.layout.activity_edit_recurring_transaction)')

e('RecurringTransactionEditActivity.onCreate', 'RecurringTransactionEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:631 (cb.onCreatePanelMenu); FW-SRC core/java/android/app/Activity.java:3386-3388 (onCreatePanelMenu calls onCreateOptionsMenu at 3388); INFERRED: the AppCompat delegate between the window and the activity is not read')

# ---- Icepick: the generated helper and the icepick library are not in the dataset (INFERRED)

e('MmxBaseFragmentActivity.onCreate', 'RecurringTransactionEditActivity$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State fields: the library loads the generated helper RecurringTransactionEditActivity$$Icepick by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState, before super.onCreate at 76); SRC recurring/transactions/RecurringTransactionEditActivity.java:63 (import icepick.State), 90 (@State String mIntentAction); INFERRED: the icepick library and its reflection are not in the dataset, source not read')

e('MmxBaseFragmentActivity.onCreate', 'RecurringTransactionEditActivity$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState); SRC recurring/transactions/RecurringTransactionEditActivity.java:90 (@State field); INFERRED: the icepick library is not in the dataset, source not read')

e('MmxBaseFragmentActivity.onCreate', 'RecurringTransactionEditActivity$$Icepick.restore', 'FRAMEWORK',
  'Icepick calls the generated restore for the @State field mIntentAction',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState); SRC recurring/transactions/RecurringTransactionEditActivity.java:90 (@State field); INFERRED: the icepick library is not in the dataset, source not read')

e('MmxBaseFragmentActivity.onSaveInstanceState', 'RecurringTransactionEditActivity$$Icepick.save', 'FRAMEWORK',
  'Icepick calls the generated save for the @State field mIntentAction',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at MmxBaseFragmentActivity.java:155)',
  evidence='SRC common/MmxBaseFragmentActivity.java:155 (Icepick.saveInstanceState); SRC recurring/transactions/RecurringTransactionEditActivity.java:90 (@State field); INFERRED: the icepick library is not in the dataset, source not read')

# ---- frequency spinner: the framework clears its selection while the listener is attached

e('RecurringTransactionEditActivity.initializeControls', 'RecurringTransactionEditActivity$1.onNothingSelected', 'FRAMEWORK',
  'the framework calls onNothingSelected when the frequency spinner loses its selected row after the listener is attached; the initial setSelection (line 328) runs before the listener is set (line 329), so it does not reach this method',
  needs_state=state_text('the frequency spinner had a selected row and its data changes so that no row is selected (the spinner adapter is static, so this is doubtful)', ('data',)),
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:328-329 (setSelection, then setOnItemSelectedListener); 339-342 (onNothingSelected: setRecurrence NOT_SET at 340, showPaymentsLeft at 341); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onNothingSelected at 947 for a negative position); AbsSpinner.java is not in fw_src, so the path from the data change to fireOnSelected is INFERRED')

# ---- payment date picker: the OK button runs the lambda listener

e('RecurringTransactionEditActivity$2.onClick', 'RecurringTransactionEditActivity$2.lambda$onClick$0', 'FRAMEWORK',
  'the user taps OK in the date picker: DatePickerDialog calls the OnDateSetListener, which is this lambda, and the lambda calls setPaymentDate',
  gui=['Tap the payment date text, then tap OK in the date picker'],
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:360-363 (lambda listener; setPaymentDate at 362); 365-374 (DatePickerDialog built with the listener; show at 374); FW-SRC core/java/android/app/DatePickerDialog.java:164-171 (onDateSet at 171); INFERRED: the dialog button dispatch to DatePickerDialog.onClick is not read (AlertController not read)')

# ---- EventBus: the activity registers in onStart; the posts are ASYNC edges

e('MmxBaseFragmentActivity.onStart', 'RecurringTransactionEditActivity.onEvent(AmountEnteredEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at RecurringTransactionEditActivity.java:219',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC recurring/transactions/RecurringTransactionEditActivity.java:219-224; INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'RecurringTransactionEditActivity.onEvent(DialogNegativeClickedEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at RecurringTransactionEditActivity.java:231',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC recurring/transactions/RecurringTransactionEditActivity.java:231-234; INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'RecurringTransactionEditActivity.onEvent(DialogPositiveClickedEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at RecurringTransactionEditActivity.java:226',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); SRC recurring/transactions/RecurringTransactionEditActivity.java:226-229; INFERRED EventBus library not read')

e('AmountInputDialog$7.onClick', 'RecurringTransactionEditActivity.onEvent(AmountEnteredEvent)', 'ASYNC',
  'the amount dialog OK button posts AmountEnteredEvent on the EventBus, and the subscriber on the activity runs',
  cls='non_standard', via='EventBus (greenrobot) post at AmountInputDialog.java:260 (auto record AmountInputDialog$7.onClick -> AmountEnteredEvent.<init>, line 260); subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC common/AmountInputDialog.java:258-262 (post at 260); SRC recurring/transactions/RecurringTransactionEditActivity.java:219-224; INFERRED EventBus delivery (library not read)')

e('YesNoDialog$2.onClick', 'RecurringTransactionEditActivity.onEvent(DialogPositiveClickedEvent)', 'ASYNC',
  'the Yes button of the transfer warning posts DialogPositiveClickedEvent on the EventBus, and the subscriber on the activity runs',
  cls='non_standard', via='EventBus (greenrobot) post at YesNoDialog.java:73 (auto record YesNoDialog$2.onClick -> DialogPositiveClickedEvent.<init>, line 73); subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC transactions/YesNoDialog.java:65-83 (post at 73 in the positive listener, $2); SRC recurring/transactions/RecurringTransactionEditActivity.java:226-229; INFERRED EventBus delivery (library not read)')

e('YesNoDialog$1.onClick', 'RecurringTransactionEditActivity.onEvent(DialogNegativeClickedEvent)', 'ASYNC',
  'the No button of the transfer warning posts DialogNegativeClickedEvent on the EventBus, and the subscriber on the activity runs',
  cls='non_standard', via='EventBus (greenrobot) post at YesNoDialog.java:81 (auto record YesNoDialog$1.onClick -> DialogNegativeClickedEvent.<init>, line 81); subscriber registered in MmxBaseFragmentActivity.onStart',
  evidence='SRC transactions/YesNoDialog.java:65-83 (post at 81 in the negative listener, $1); SRC recurring/transactions/RecurringTransactionEditActivity.java:231-234; INFERRED EventBus delivery (library not read)')

# ---- results returned to onActivityResult (the framework calls it through dispatchActivityResult)

e('PayeeListFragment.sendResultToActivity', 'RecurringTransactionEditActivity.onActivityResult', 'RESULT',
  'the payee list returns the picked payee and finishes: setResult(RESULT_OK, result), and the framework calls onActivityResult',
  guard='the payee activity is started with ACTION_PICK (EditTransactionCommonFunctions.java:573-576), and the ACTION_PICK path calls sendResultToActivity (PayeeListFragment.java:309)',
  evidence='SRC fragment/PayeeListFragment.java:309 (setResult calls sendResultToActivity on the pick path), 324-331 (sendResultToActivity; setResult(RESULT_OK, result) at 329); SRC transactions/EditTransactionCommonFunctions.java:573-576 (PayeeActivity start); FW-SRC core/java/android/app/ActivityThread.java:4253-4266 (deliverResults calls dispatchActivityResult); INFERRED: the dispatchActivityResult to onActivityResult step (Activity.java near 7259-7266) is not printed for this batch')

e('CategoryListFragment.setResult', 'RecurringTransactionEditActivity.onActivityResult', 'RESULT',
  'the category list returns the picked category and finishes: setResult(RESULT_OK, result), and the framework calls onActivityResult',
  guard='the category activity is started with ACTION_PICK (EditTransactionCommonFunctions.java:461-466)',
  evidence='SRC common/CategoryListFragment.java:313 (setResult), 354 (RESULT_OK in the same method, per grep.txt section 6); SRC transactions/EditTransactionCommonFunctions.java:461-466 (CategoryListActivity start with ACTION_PICK); INFERRED: the framework dispatch step is as for PayeeListFragment (ActivityThread.java:4253-4266)')

e('SplitCategoriesActivity.onActionDoneClick', 'RecurringTransactionEditActivity.onActivityResult', 'RESULT',
  'the split categories editor returns the splits and finishes: setResult(RESULT_OK, result) in onActionDoneClick, and the framework calls onActivityResult',
  guard='the editor is started with RequestCodes.SPLIT_TX (EditTransactionCommonFunctions.java:1528, in showSplitCategoriesForm at 1511)',
  evidence='SRC transactions/SplitCategoriesActivity.java:149 (onActionDoneClick), 174 (setResult RESULT_OK); SRC transactions/EditTransactionCommonFunctions.java:1511-1528 (startActivityForResult with RequestCodes.SPLIT_TX at 1528); INFERRED: the framework dispatch step is as for PayeeListFragment (ActivityThread.java:4253-4266)')

# ---- GUI edges from the form S_RECURRING_TRANSACTION_EDIT (page -> method)

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity.onOptionsItemSelected',
    'Tap the up arrow or the save icon in the toolbar',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:166-175 (home 168-169; save 170-171); SRC core/MenuHelper.java:37 (save = 2), 87-89 (addSaveToolbarIcon); FW-SRC core/java/android/app/Activity.java:3450 (onOptionsItemSelected dispatch); INFERRED: the toolbar tap reaching onMenuItemSelected through AppCompat is not read')

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity.onBackPressed',
    'Press the Back key',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:201-204 (onBackPressed calls onActionCancelClick at 203); FW-SRC core/java/android/app/Activity.java:3001 (onBackPressed); INFERRED: the AppCompat key dispatch to onBackPressed is not read')

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity$1.onItemSelected',
    'Pick a frequency in the frequency spinner (spinnerFrequencies)',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:329-336 (listener; onItemSelected 331-336); SRC res/layout/activity_edit_recurring_transaction.xml:276 (spinnerFrequencies); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onItemSelected at 944); INFERRED: the drop-down click path to setSelection is not read')

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity$2.onClick',
    'Tap the payment date text (paymentDateTextView)',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:355-376 (listener 355; onClick 357-375; DatePickerDialog show at 374); SRC res/layout/activity_edit_recurring_transaction.xml:117 (paymentDateTextView)')

gui('S_RECURRING_TRANSACTION_EDIT', 'RecurringTransactionEditActivity$3.onClick',
    'Tap the previous-day button (paymentPreviousDayButton)',
    evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:382-388 (listener 382; onClick 384-387; setPaymentDate at 386); SRC res/layout/activity_edit_recurring_transaction.xml:108 (paymentPreviousDayButton)')

# RecurringTransactionEditActivity$4.onClick (the next-day button, layout line 127) is in another batch: its GUI edge is written there.
