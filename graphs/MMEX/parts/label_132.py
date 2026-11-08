# ================================================================== batch 132 (label_132): EditTransactionCommonFunctions methods 81-115 of 115 (35 methods): the anonymous listener classes $2 to $9 and $13 to $19 (<init>, onClick, TextWatcher and lambda methods)
# Result: 35 REACHABLE, 0 UNREACHABLE (rows: graphs/MMEX/parts/label_132.md). Grep evidence: graphs/MMEX/parts/label_132.grep.txt.
# This file writes:
#   - 15 GUI edges (page -> method) from S_RECURRING_TRANSACTION_EDIT to the listeners and TextWatchers the user operates in the form (D1: each destination is a batch method);
#   - 5 FRAMEWORK edges (method -> listener): onActionCancelClick -> $16.onClick and $17.onClick, onTransferSelected -> $18.onClick, showSplitResetNotice -> $19.onClick (dialog buttons), and initTransactionNumberControls -> $14.onClick (View.callOnClick at line 725; no auto_calls.json record targets $14.onClick, grep G4).
# No UNREACHABLE entries (every method has a route) and no sup cuts (no UNREACHABLE caller in this batch).
# No CALL edge is written (D7): the 15 creation records (<init>) and the lambda record (EditTransactionCommonFunctions$5.onClick -> lambda$onClick$0) are already in auto_calls.json.
# S_RECURRING_TRANSACTION_EDIT is defined once, in label_099.py (graph_def.py:8885); this batch reuses it.
# CheckingTransactionEditActivity.initializeInputControls also calls the enclosing methods (grep G2); that editor has no page key in graph_def.py (grep G8), so its GUI edges are not written here (open item).

# ---- GUI edges from the form (page -> method): the user operates the control

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$2.onClick',
    'Tap the amount field (txtAmount); opens the Calculator for the amount',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:419; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:419-432 (listener 419; onClick 421-431; Calculator.forActivity 427, show 430); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$3.onClick',
    'Tap the amount-to field (txtAmountTo) of a transfer; opens the Calculator for the destination amount',
    needs_state=state_text('the amount-to row is shown only when the transaction type is Transfer (EditTransactionCommonFunctions.java:983); the type is chosen in this editing session', ('session',)),
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:436; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:436-448 (listener 436; onClick 438-447; Calculator.forActivity 444, show 446); SRC transactions/EditTransactionCommonFunctions.java:983 (tableRowAmountTo visible for Transfer); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$4.onClick',
    'Tap the category field (categoryTextView); opens CategoryListActivity, or the split categories form when split is selected',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:459; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:459-474 (listener 459; onClick 461-473; isSplitSelected branch 462-470; CategoryListActivity intent 464-466; showSplitCategoriesForm 469); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$5.onClick',
    'Tap the payment date text (dateTextView); opens the DatePickerDialog',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:488; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:488-509 (listener 488; onClick 490-508; DatePickerDialog built 498-504; show 507); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$6.onClick',
    'Tap the previous-day button (previousDayButton)',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:511; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:511-517 (listener 511; onClick 513-516; setDate 515); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$7.onClick',
    'Tap the next-day button (nextDayButton)',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:519; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:519-525 (listener 519; onClick 521-524; setDate 523); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$8.beforeTextChanged',
    'Type in the notes field (edtNotes): the framework calls beforeTextChanged before each change (empty body)',
    via='TextWatcher added at EditTransactionCommonFunctions.java:551; TextView.sendBeforeTextChanged calls beforeTextChanged (FW-SRC TextView.java:9309-9316)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:551-567 (addTextChangedListener 551; beforeTextChanged 553-555, empty body); FW-SRC core/java/android/widget/TextView.java:9309-9316 (sendBeforeTextChanged calls beforeTextChanged at 9314); INFERRED (source not read): a keystroke reaches sendBeforeTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$8.onTextChanged',
    'Type in the notes field (edtNotes): the framework calls onTextChanged after each change (empty body)',
    via='TextWatcher added at EditTransactionCommonFunctions.java:551; TextView.sendOnTextChanged calls onTextChanged (FW-SRC TextView.java:9359-9366)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:551-567 (onTextChanged 557-560, empty body); FW-SRC core/java/android/widget/TextView.java:9359-9366 (sendOnTextChanged calls onTextChanged at 9364); FW-SRC TextView.java:5397 (sendOnTextChanged call); INFERRED (source not read): a keystroke reaches sendOnTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$8.afterTextChanged',
    'Type in the notes field (edtNotes): the framework calls afterTextChanged, which marks the form dirty and stores the notes',
    via='TextWatcher added at EditTransactionCommonFunctions.java:551; TextView.sendAfterTextChanged calls afterTextChanged (FW-SRC TextView.java:9375-9382)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:551-567 (afterTextChanged 563-566; setDirty 564; setNotes 565); FW-SRC core/java/android/widget/TextView.java:9375-9382 (sendAfterTextChanged calls afterTextChanged at 9380); FW-SRC TextView.java:5403 (sendAfterTextChanged call); INFERRED (source not read): a keystroke reaches sendAfterTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$9.onClick',
    'Tap the payee field (txtSelectPayee) in the form; opens PayeeActivity',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:571; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:571-580 (listener 571; onClick 573-579; PayeeActivity intent 574-576); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$13.beforeTextChanged',
    'Type in the transaction number field (edtTransNumber): the framework calls beforeTextChanged before each change (empty body)',
    via='TextWatcher added at EditTransactionCommonFunctions.java:672; TextView.sendBeforeTextChanged calls beforeTextChanged (FW-SRC TextView.java:9309-9316)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:672-689 (addTextChangedListener 672; beforeTextChanged 674-676, empty body); FW-SRC core/java/android/widget/TextView.java:9309-9316 (sendBeforeTextChanged calls beforeTextChanged at 9314); INFERRED (source not read): a keystroke reaches sendBeforeTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$13.onTextChanged',
    'Type in the transaction number field (edtTransNumber): the framework calls onTextChanged after each change (empty body)',
    via='TextWatcher added at EditTransactionCommonFunctions.java:672; TextView.sendOnTextChanged calls onTextChanged (FW-SRC TextView.java:9359-9366)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:672-689 (onTextChanged 679-681, empty body); FW-SRC core/java/android/widget/TextView.java:9359-9366 (sendOnTextChanged calls onTextChanged at 9364); INFERRED (source not read): a keystroke reaches sendOnTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$13.afterTextChanged',
    'Type in the transaction number field (edtTransNumber): the framework calls afterTextChanged, which marks the form dirty and stores the number',
    via='TextWatcher added at EditTransactionCommonFunctions.java:672; TextView.sendAfterTextChanged calls afterTextChanged (FW-SRC TextView.java:9375-9382)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:672-689 (afterTextChanged 684-688; setDirty 685; setTransactionNumber 687); FW-SRC core/java/android/widget/TextView.java:9375-9382 (sendAfterTextChanged calls afterTextChanged at 9380); INFERRED (source not read): a keystroke reaches sendAfterTextChanged')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$14.onClick',
    'Tap the transaction number button (btnTransNumber): fills the next number from the highest existing number of the account',
    via='View.OnClickListener set at EditTransactionCommonFunctions.java:691; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:691-722 (listener 691; onClick 693-721; cursor.close 720); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

gui('S_RECURRING_TRANSACTION_EDIT', 'EditTransactionCommonFunctions$15.onClick',
    'Tap the Withdrawal, Deposit or Transfer button: sets the transaction type, marks the form dirty and redraws the controls',
    via='View.OnClickListener at EditTransactionCommonFunctions.java:755, set on the three buttons at 769, 774 and 779; performClick calls onClick (FW-SRC View.java:6289-6295)',
    evidence='SRC transactions/EditTransactionCommonFunctions.java:755-787 (listener 755; onClick 757-763; setDirty 758; changeTransactionTypeTo 762; buttons 767-779); FW-SRC core/java/android/view/View.java:6289-6295 (performClick calls onClick at 6294); INFERRED (source not read): the tap that reaches performClick')

# ---- FRAMEWORK edges (method -> listener): the dialog that the method builds; the framework calls the listener on a button tap

e('EditTransactionCommonFunctions.onActionCancelClick', 'EditTransactionCommonFunctions$16.onClick', 'FRAMEWORK',
  'the discard-changes dialog is shown; the user taps Discard and the framework calls the positive listener, which calls cancelActivity',
  needs_state=state_text('the dialog opens only when the form has unsaved changes (getDirty at EditTransactionCommonFunctions.java:823; in-memory flag)', ('session',)),
  via='DialogInterface.OnClickListener passed to setPositiveButton at EditTransactionCommonFunctions.java:827',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:822-846 (getDirty gate 823; setPositiveButton 827; onClick 829-831; cancelActivity 830); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:125-146 (mButtonHandler sends the button message); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167 (handleMessage calls onClick at 166); INFERRED (source not read): the path from Builder.show to the button handler')

e('EditTransactionCommonFunctions.onActionCancelClick', 'EditTransactionCommonFunctions$17.onClick', 'FRAMEWORK',
  'the discard-changes dialog is shown; the user taps Keep editing and the framework calls the negative listener, which dismisses the dialog',
  needs_state=state_text('the dialog opens only when the form has unsaved changes (getDirty at EditTransactionCommonFunctions.java:823; in-memory flag)', ('session',)),
  via='DialogInterface.OnClickListener passed to setNegativeButton at EditTransactionCommonFunctions.java:833',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:822-846 (getDirty gate 823; setNegativeButton 833; onClick 835-837; dismiss 836); FW-SRC core/java/android/app/AlertDialog.java:637-639 (setNegativeButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:125-146 (mButtonHandler sends the button message); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167 (handleMessage calls onClick at 166); INFERRED (source not read): the path from Builder.show to the button handler')

e('EditTransactionCommonFunctions.onTransferSelected', 'EditTransactionCommonFunctions$18.onClick', 'FRAMEWORK',
  'the no-accounts warning is shown; the user taps OK and the framework calls the positive listener, which dismisses the dialog',
  needs_state=state_text('the warning is shown only when the destination account is not set and the account list is empty (EditTransactionCommonFunctions.java:1470-1471), and there are no split categories (1448); database and in-memory state', ('data', 'session')),
  via='DialogInterface.OnClickListener passed to setPositiveButton at EditTransactionCommonFunctions.java:1476',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1446-1488 (hasSplitCategories guard 1448; setSplit 1467; account checks 1470-1471; setPositiveButton 1476; onClick 1478-1481; dismiss 1480); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167 (handleMessage calls onClick at 166); INFERRED (source not read): the path from Builder.show to the button handler')

e('EditTransactionCommonFunctions.showSplitResetNotice', 'EditTransactionCommonFunctions$19.onClick', 'FRAMEWORK',
  'the split reset notice is shown; the user taps OK and the framework calls the positive listener, which dismisses the dialog',
  needs_state=state_text('the notice is shown only when the transaction has two or more split records (EditTransactionCommonFunctions.java:608-618, default branch of the split button)', ('data', 'session')),
  via='DialogInterface.OnClickListener passed to setPositiveButton at EditTransactionCommonFunctions.java:1539',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1535-1547 (setPositiveButton 1539; onClick 1541-1544; dismiss 1543); SRC transactions/EditTransactionCommonFunctions.java:598-627 (split button; showSplitResetNotice call at 618); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167 (handleMessage calls onClick at 166); INFERRED (source not read): the path from Builder.show to the button handler')

e('EditTransactionCommonFunctions.initTransactionNumberControls', 'EditTransactionCommonFunctions$14.onClick', 'FRAMEWORK',
  'the button is clicked by code when auto transaction numbering is on: callOnClick runs the listener without a tap',
  needs_state=state_text('auto transaction number is on (settings: BehaviourSettings.getAutoTransactionNumber) and the transaction has no id (data), EditTransactionCommonFunctions.java:724', ('settings', 'data')),
  via='View.callOnClick at EditTransactionCommonFunctions.java:725 (framework dispatch, not a user tap)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:724-726 (if not hasId and auto number; callOnClick at 725); FW-SRC core/java/android/view/View.java:6315-6322 (callOnClick calls onClick at 6318); grep G4 (no auto_calls.json record targets EditTransactionCommonFunctions$14.onClick)')
