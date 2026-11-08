# ================================================================== batch 012 (label_012): AccountTransactionsListViewHolder, AccountTypes, CalculateRunningBalanceTask2, FilterDialogFragment (27 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_012.md.
# Every edge below has a batch 012 method as its destination, or is the ENTERS edge to the dialog page this batch defines.
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here.
# Framework claims cite FW-SRC lines printed for this batch; androidx DialogFragment claims are INFERRED (source not in the dataset).

SCREENS.update({
    'S_ACCOUNT_FILTER_DIALOG': 'Account filter dialog (FilterDialogFragment), opened from the filter item of the account transactions list menu: account name, record count, edit and favourite buttons, OK and Cancel',
})

# ---- dialog lifecycle and the screen

e('FilterDialogFragment.<init>', 'FilterDialogFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate for the fragment instance created by newInstance, when the dialog is shown (AccountTransactionListFragment.java:831)',
  evidence='SRC account/FilterDialogFragment.java:82-95 (onCreate reads the arguments at 85-89); androidx DialogFragment and FragmentManager are not in the dataset: INFERRED, source not read')

e('FilterDialogFragment.onCreate', 'FilterDialogFragment.onCreateDialog', 'LIFECYCLE',
  'the framework calls onCreateDialog after onCreate, when the dialog is shown',
  evidence='SRC account/FilterDialogFragment.java:111 (onCreateDialog); androidx DialogFragment calls onCreateDialog from its layout inflater path: not in the dataset, INFERRED, source not read')

e('FilterDialogFragment.onCreateDialog', 'S_ACCOUNT_FILTER_DIALOG', 'ENTERS',
  'the account filter dialog is shown',
  evidence='SRC account/FilterDialogFragment.java:135-136 (AlertDialog create and show at 135-136)')

# ---- AsyncTask: the background calculation and the result callback (framework)

e('AccountTransactionListFragment.populateRunningBalance', 'CalculateRunningBalanceTask2.doInBackground', 'FRAMEWORK',
  'task.execute() starts the AsyncTask: the framework runs doInBackground on its background worker',
  evidence='SRC account/AccountTransactionListFragment.java:644 (task.execute()); FW-SRC core/java/android/os/AsyncTask.java:594-595 (execute calls executeOnExecutor with sDefaultExecutor), 632-651 (executeOnExecutor; exec.execute(mFuture) at 651), 330-333 (the worker calls doInBackground at 333), 403 (abstract doInBackground)')

e('CalculateRunningBalanceTask2.doInBackground', 'CalculateRunningBalanceTask2.onPostExecute', 'FRAMEWORK',
  'the framework posts the result to the main thread, and finish calls onPostExecute when the task is not cancelled',
  evidence='FW-SRC core/java/android/os/AsyncTask.java:369-373 (postResult sends MESSAGE_POST_RESULT), 705-713 (handleMessage calls finish at 712), 691-696 (finish calls onPostExecute at 695); FW-SRC AsyncTask.java:429 (default onPostExecute); SRC account/CalculateRunningBalanceTask2.java:88-95 (doInBackground returns the result of runTask)')

# ---- GUI edges from the dialog page: the framework dispatches the button clicks

e('S_ACCOUNT_FILTER_DIALOG', 'FilterDialogFragment$1.onClick', 'GUI',
  'the OK button of the dialog: the listener body is empty (todo at line 124)',
  gui=['Tap OK (android.R.string.ok) in the account filter dialog'],
  evidence='SRC account/FilterDialogFragment.java:120-126 (positive listener 121-126); FW-SRC android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC com/android/internal/app/AlertController.java:1022-1023 (setButton with a null message), 347-349 (setButton builds the message), 128-147 (the button click sends the message), 166 (ButtonHandler calls onClick); the View click dispatch is not printed (source not read): INFERRED for that step')

e('S_ACCOUNT_FILTER_DIALOG', 'FilterDialogFragment$2.onClick', 'GUI',
  'the Cancel button of the dialog: dismisses the dialog',
  gui=['Tap Cancel (android.R.string.cancel) in the account filter dialog'],
  evidence='SRC account/FilterDialogFragment.java:127-132 (negative listener 127-132; dismiss at 130); FW-SRC android/app/AlertDialog.java:637-639 (setNegativeButton stores the listener); FW-SRC com/android/internal/app/AlertController.java:1026-1027, 347-349, 128-147, 166 (same dispatch as OK); the View click dispatch is not printed: INFERRED for that step')

e('S_ACCOUNT_FILTER_DIALOG', 'FilterDialogFragment$3.onClick', 'GUI',
  'the edit button in the dialog: the listener starts AccountEditActivity (the INTENT edge into the activity is written by batch 006)',
  gui=['Tap the edit button (R.id.editButton) in the account filter dialog'],
  evidence='SRC account/FilterDialogFragment.java:167-176 (editButton listener 168-176; intent 171-174; startActivity 174); the View click dispatch is not printed (source not read): INFERRED for that step')

e('S_ACCOUNT_FILTER_DIALOG', 'FilterDialogFragment$4.onClick', 'GUI',
  'the favourite button: toggles the account favourite flag, saves the account and redraws the star',
  gui=['Tap the favourite button (R.id.favouriteButton) in the account filter dialog'],
  evidence='SRC account/FilterDialogFragment.java:183-199 (favouriteButton listener 184-199; onClick 185-198; save at 192; alert at 194; showFavouriteStatus at 197); the View click dispatch is not printed (source not read): INFERRED for that step')

# ---- UNREACHABLE entries (kind, reason, source reference, confirmed_by)

UNREACHABLE['AccountTypes.equalsName'] = (
  'no_trigger_in_app',
  'Public instance method (case-insensitive comparison of the title). No caller in the app: its name occurs only at its declaration (AccountTypes.java:59) and at AccountStatuses.equalsName (AccountStatuses.java:39), a different method. grep finds no call site and no method reference (label_012.grep.txt). auto_calls.json has no call edge into it: the only entries are the outgoing framework call String.equalsIgnoreCase (framework_calls, lines 72968-72970) and the impl index (lines 90301-90303). Source is app code, so the label is SOURCE.',
  'AccountTypes.java:59-61; AccountStatuses.java:39; label_012.grep.txt; auto_calls.json:72968-72970, 90301-90303',
  'SOURCE')
