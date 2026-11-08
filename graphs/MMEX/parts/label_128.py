# ================================================================== batch 128 (label_128): AttachmentAdapter (4 methods), AttachmentAdapter$ViewHolder (4), CheckingTransactionEditActivity (27), CheckingTransactionEditActivity$$Icepick (4); 39 methods
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_128.md (39 REACHABLE, 0 UNREACHABLE, 0 INCOMPLETE; one flagged row).
# Grep evidence: graphs/MMEX/parts/label_128.grep.txt.
# This file writes 33 e() edges and 3 gui() edges (36 edges), one SCREENS key, 0 UNREACHABLE entries and 0 sup pairs.
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here (D7).
# REGISTER edges are skipped by reachability (label_032.py:13), so the onEvent methods are reached through their ASYNC posts.
# The flagged row: onEvent(AmountEnteredEvent) has only a static ASYNC route (no AmountInputDialog is shown on this screen).

SCREENS.update({
    'S_CHECKING_TRANSACTION_EDIT': 'Transaction edit form (CheckingTransactionEditActivity): account, payee, category, amount, transaction type, status, notes, attachments, split categories, save and cancel',
})

# ---- entry and the intents into the activity (the constructor is the destination)

e('S_ENTRY', 'CheckingTransactionEditActivity.<init>', 'ENTRY',
  'another app sends an EDIT or INSERT intent to the exported CheckingTransactionEditActivity',
  env=env_text('outside package: another app sends an EDIT or INSERT intent to CheckingTransactionEditActivity (exported=true, no data element in the filter)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:181-188; FW-SRC core/java/android/app/ActivityThread.java:2644 (performLaunchActivity)')

e('HomeFragment$1.onClick', 'CheckingTransactionEditActivity.<init>', 'INTENT',
  'the add button (floating action button) on the home screen starts the editor with ACTION_INSERT',
  gui=['Tap the add button (floating action button) on the home screen'],
  evidence='SRC home/HomeFragment.java:185-191 (intent 188, ACTION_INSERT 190, startActivity 191)')

e('HomeFragment.onEvent', 'CheckingTransactionEditActivity.<init>', 'INTENT',
  'the balance amount dialog on the home screen returns an amount, and onEvent starts the editor with ACTION_INSERT and the account as data',
  gui=['Tap the balance of an account on the home screen, then enter an amount'],
  evidence='SRC home/HomeFragment.java:491-527 (intent 513, ACTION_INSERT 514, setData 524, startActivity 526); SRC home/HomeFragment.java:545 (AmountInputDialog show site); SRC common/AmountInputDialog.java:258-262 (AmountEnteredEvent post)')

e('SingleAccountWidget.initializeNewTransactionCommand', 'CheckingTransactionEditActivity.<init>', 'INTENT',
  'the account widget add button starts the editor through a PendingIntent with ACTION_INSERT',
  cls='non_standard', via='PendingIntent.getActivity at SingleAccountWidget.java:225 (the launcher starts the activity on a widget tap)',
  evidence='SRC widget/SingleAccountWidget.java:211-225 (intent 212, ACTION_INSERT 213, PendingIntent.getActivity 225)')

e('ButtonAddTransactionWidgetProvider.onUpdate', 'CheckingTransactionEditActivity.<init>', 'INTENT',
  'the add-transaction widget button starts the editor through a PendingIntent with ACTION_INSERT',
  cls='non_standard', via='PendingIntent.getActivity at ButtonAddTransactionWidgetProvider.java:41 (the launcher starts the activity on a widget tap)',
  evidence='SRC widget/ButtonAddTransactionWidgetProvider.java:32-41 (intent 38, ACTION_INSERT 39, PendingIntent 41)')

e('AllDataListFragment.startEditAccountTransactionActivity', 'CheckingTransactionEditActivity.<init>', 'INTENT',
  'the all-data list opens an existing transaction with ACTION_EDIT, or a new one with ACTION_INSERT',
  gui=['Tap a transaction row in the all-data list (or the add button)'],
  evidence='SRC common/AllDataListFragment.java:785-801 (intent 787; ACTION_EDIT or ACTION_INSERT)')

e('AllDataListFragment.showDuplicateTransactionView', 'CheckingTransactionEditActivity.<init>', 'INTENT',
  'the duplicate view starts the editor for each chosen row with ACTION_PASTE',
  gui=['Choose the duplicate action on a transaction in the all-data list'],
  evidence='SRC common/AllDataListFragment.java:916-929 (intents at 924; ACTION_PASTE; startActivities at 929)')

e('AccountTransactionListFragment.startCheckingAccountActivity(Integer)', 'CheckingTransactionEditActivity.<init>', 'INTENT',
  'the account transaction list opens the editor for a checking account transaction (ACTION_EDIT with the id)',
  gui=['Tap a transaction in the account transaction list, or the add button'],
  evidence='SRC account/AccountTransactionListFragment.java:859-871 (intent 861)')

e('RecurringTransactionListFragment.showCreateTransactionActivity', 'CheckingTransactionEditActivity.<init>', 'INTENT',
  'the recurring list creates a transaction from a scheduled one: ACTION_INSERT with the KEY_BDID_ID extra',
  gui=['Choose the create-transaction action on a scheduled transaction in the recurring list'],
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:427-436 (intent 432; ACTION_INSERT 433; KEY_BDID_ID 434; startActivityForResult 436)')

e('SmsReceiverTransactions.onReceive', 'CheckingTransactionEditActivity.<init>', 'INTENT',
  'a bank SMS starts the editor with ACTION_INSERT or ACTION_EDIT when the bank SMS setting is on',
  needs_state=state_text('the bank SMS transaction setting is on (behav_settings.getBankSmsTrans at line 117)', ('settings',)),
  evidence='SRC notifications/SmsReceiverTransactions.java:97-451 (bank SMS gate 117; t_intent 200; ACTION_INSERT 303; ACTION_EDIT 345, 349, 392; startActivity 407, 417)')

# ---- lifecycle and the screen

e('CheckingTransactionEditActivity.<init>', 'CheckingTransactionEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('CheckingTransactionEditActivity.onCreate', 'S_CHECKING_TRANSACTION_EDIT', 'ENTERS',
  'the transaction edit form is shown',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:95 (setContentView)')

e('CheckingTransactionEditActivity.onCreate', 'CheckingTransactionEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:631 (cb.onCreatePanelMenu); FW-SRC core/java/android/app/Activity.java:3386-3388 (onCreatePanelMenu calls onCreateOptionsMenu); INFERRED: the AppCompat delegate between window and activity is not read')

e('CheckingTransactionEditActivity.onCreate', 'CheckingTransactionEditActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity: ActivityThread calls callCallActivityOnSaveInstanceState, which calls onSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3873-3876 (callCallActivityOnSaveInstanceState at 3875); FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState at 1496)')

# ---- Icepick: the generated helper and the icepick library are not in the dataset (INFERRED)

e('MmxBaseFragmentActivity.onCreate', 'CheckingTransactionEditActivity$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State fields: the library loads the generated helper CheckingTransactionEditActivity$$Icepick by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState, before super.onCreate at 76); SRC transactions/CheckingTransactionEditActivity.java:70 (import icepick.State), 82 (@State String mIntentAction); grep.txt sections 1-3; INFERRED: the icepick library and its reflection are not in the dataset, source not read')

e('MmxBaseFragmentActivity.onCreate', 'CheckingTransactionEditActivity$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74; SRC transactions/CheckingTransactionEditActivity.java:82 (@State field); INFERRED: the icepick library is not in the dataset, source not read')

e('MmxBaseFragmentActivity.onCreate', 'CheckingTransactionEditActivity$$Icepick.restore', 'FRAMEWORK',
  'Icepick calls the generated restore for the @State field mIntentAction',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74; SRC transactions/CheckingTransactionEditActivity.java:82 (@State field); grep.txt section 2; INFERRED: the icepick library is not in the dataset, source not read')

e('MmxBaseFragmentActivity.onSaveInstanceState', 'CheckingTransactionEditActivity$$Icepick.save', 'FRAMEWORK',
  'Icepick calls the generated save for the @State field mIntentAction',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at MmxBaseFragmentActivity.java:155)',
  evidence='SRC common/MmxBaseFragmentActivity.java:152-155 (Icepick.saveInstanceState at 155); SRC transactions/CheckingTransactionEditActivity.java:82 (@State field); INFERRED: the icepick library is not in the dataset, source not read')

# ---- attachments: the RecyclerView calls the adapter (androidx RecyclerView not read)

e('EditTransactionCommonFunctions.initAttachmentControls', 'AttachmentAdapter.getItemCount', 'FRAMEWORK',
  'RecyclerView asks the adapter for the item count during layout',
  cls='non_standard', via='androidx RecyclerView after setAdapter at EditTransactionCommonFunctions.java:749',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:729-750 (setAdapter 749, setLayoutManager 750); SRC transactions/AttachmentAdapter.java:59-61; INFERRED: RecyclerView source not read')

e('EditTransactionCommonFunctions.initAttachmentControls', 'AttachmentAdapter.onCreateViewHolder', 'FRAMEWORK',
  'RecyclerView creates a row holder for each visible attachment row',
  cls='non_standard', via='androidx RecyclerView after setAdapter at EditTransactionCommonFunctions.java:749',
  needs_state=state_text('the transaction has at least one attachment (the list is non-empty)', ('data',)),
  evidence='SRC transactions/EditTransactionCommonFunctions.java:729-750; SRC transactions/AttachmentAdapter.java:46-49; INFERRED: RecyclerView source not read')

e('EditTransactionCommonFunctions.initAttachmentControls', 'AttachmentAdapter.onBindViewHolder', 'FRAMEWORK',
  'RecyclerView binds each visible attachment row to its attachment',
  cls='non_standard', via='androidx RecyclerView after setAdapter at EditTransactionCommonFunctions.java:749',
  needs_state=state_text('the transaction has at least one attachment (the list is non-empty)', ('data',)),
  evidence='SRC transactions/EditTransactionCommonFunctions.java:729-750; SRC transactions/AttachmentAdapter.java:52-56; INFERRED: RecyclerView source not read')

# ---- default payee: the executor and the UI-thread refresh in handleIntent

e('CheckingTransactionEditActivity.handleIntent', 'CheckingTransactionEditActivity.lambda$handleIntent$1', 'FRAMEWORK',
  'the default payee branch submits the body to a single-thread executor, which runs it on a background thread',
  cls='non_standard', via='java.util.concurrent executor (Executors.newSingleThreadExecutor at line 514; executor.execute at 516)',
  needs_state=state_text('the default payee setting is "L" (last payee used), the intent action is ACTION_INSERT, and no payee is set yet', ('settings', 'data')),
  evidence='SRC transactions/CheckingTransactionEditActivity.java:512-516 (setting check, executor); auto records of lambda$handleIntent$1 from lines 518-526')

e('CheckingTransactionEditActivity.lambda$handleIntent$1', 'CheckingTransactionEditActivity.lambda$handleIntent$0', 'FRAMEWORK',
  'the background body calls runOnUiThread with the refresh lambda, which runs on the UI thread',
  cls='non_standard', via='Activity.runOnUiThread (fw_src core/java/android/app/Activity.java:6170-6176)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:528-532; FW-SRC core/java/android/app/Activity.java:6170-6176; auto records of lambda$handleIntent$0 (lines 530-531)')

# ---- results: the child activity setResult is delivered to onActivityResult

e('CalculatorActivity.returnResult', 'CheckingTransactionEditActivity.onActivityResult', 'RESULT',
  'the amount calculator returns the amount: setResult(RESULT_OK), and the framework calls onActivityResult',
  guard='the calculator is started by Calculator.forActivity(getActivity()) with RequestCodes.AMOUNT (EditTransactionCommonFunctions.java:427-430 and 444)',
  evidence='SRC common/CalculatorActivity.java:435-445 (setResult 443); SRC transactions/EditTransactionCommonFunctions.java:427-430, 444; FW-SRC core/java/android/app/ActivityThread.java:4253-4266 (deliverResults); INFERRED: the dispatch to onActivityResult is not printed for this batch')

e('PayeeListFragment.sendResultToActivity', 'CheckingTransactionEditActivity.onActivityResult', 'RESULT',
  'the payee picker returns the chosen payee: setResult(RESULT_OK), and the framework calls onActivityResult',
  guard='the payee activity is started with ACTION_PICK (EditTransactionCommonFunctions.java:573-576)',
  evidence='SRC fragment/PayeeListFragment.java:309, 324-331 (setResult RESULT_OK at 329); SRC transactions/EditTransactionCommonFunctions.java:573-576; FW-SRC core/java/android/app/ActivityThread.java:4253-4266; INFERRED: the dispatch to onActivityResult is not printed for this batch')

e('CategoryListFragment.setResult', 'CheckingTransactionEditActivity.onActivityResult', 'RESULT',
  'the category list returns the chosen category: setResult(RESULT_OK), and the framework calls onActivityResult',
  guard='the category activity is started with ACTION_PICK (EditTransactionCommonFunctions.java:461-466)',
  evidence='SRC common/CategoryListFragment.java:313 (setResult), 354 (RESULT_OK); SRC transactions/EditTransactionCommonFunctions.java:461-466; FW-SRC core/java/android/app/ActivityThread.java:4253-4266; INFERRED: the dispatch to onActivityResult is not printed for this batch')

e('SplitCategoriesActivity.onActionDoneClick', 'CheckingTransactionEditActivity.onActivityResult', 'RESULT',
  'the split categories editor returns the splits: setResult(RESULT_OK) in onActionDoneClick, and the framework calls onActivityResult',
  guard='the editor is started with RequestCodes.SPLIT_TX (EditTransactionCommonFunctions.java:1511-1528)',
  evidence='SRC transactions/SplitCategoriesActivity.java:149-177 (setResult RESULT_OK at 174); SRC transactions/EditTransactionCommonFunctions.java:1511-1528; FW-SRC core/java/android/app/ActivityThread.java:4253-4266; INFERRED: the dispatch to onActivityResult is not printed for this batch')

# ---- EventBus: the activity registers in onStart; the posts are ASYNC edges

e('MmxBaseFragmentActivity.onStart', 'CheckingTransactionEditActivity.onEvent(AmountEnteredEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at CheckingTransactionEditActivity.java:206-207',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'CheckingTransactionEditActivity.onEvent(DialogNegativeClickedEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at CheckingTransactionEditActivity.java:222-223',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); INFERRED EventBus library not read')

e('MmxBaseFragmentActivity.onStart', 'CheckingTransactionEditActivity.onEvent(DialogPositiveClickedEvent)', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited); EventBus calls the subscriber until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141; @Subscribe at CheckingTransactionEditActivity.java:217-218',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141; unregister at 146 in onStop); INFERRED EventBus library not read')

e('AmountInputDialog$7.onClick', 'CheckingTransactionEditActivity.onEvent(AmountEnteredEvent)', 'ASYNC',
  'the amount dialog OK button posts AmountEnteredEvent on the EventBus, and the subscriber on the activity runs (static route only: no AmountInputDialog is shown on this screen; see the flagged row in label_128.md)',
  cls='non_standard', via='EventBus (greenrobot) post at AmountInputDialog.java:260 (grep.txt section 4: class AmountInputDialog$7 posts AmountEnteredEvent)',
  evidence='SRC common/AmountInputDialog.java:258-262 (post at 260); SRC transactions/CheckingTransactionEditActivity.java:206-210; SRC transactions/EditTransactionCommonFunctions.java:410 (commented out), 427, 444; INFERRED EventBus delivery (library not read)')

e('YesNoDialog$2.onClick', 'CheckingTransactionEditActivity.onEvent(DialogPositiveClickedEvent)', 'ASYNC',
  'the Yes button of the transfer warning posts DialogPositiveClickedEvent on the EventBus, and the subscriber on the activity runs',
  cls='non_standard', via='EventBus (greenrobot) post at YesNoDialog.java:73 (grep.txt section 4: class YesNoDialog$2 posts DialogPositiveClickedEvent)',
  evidence='SRC transactions/YesNoDialog.java:65-83 (post at 73, positive listener); SRC transactions/CheckingTransactionEditActivity.java:217-220; INFERRED EventBus delivery (library not read)')

e('YesNoDialog$1.onClick', 'CheckingTransactionEditActivity.onEvent(DialogNegativeClickedEvent)', 'ASYNC',
  'the No button of the transfer warning posts DialogNegativeClickedEvent on the EventBus, and the subscriber on the activity runs',
  cls='non_standard', via='EventBus (greenrobot) post at YesNoDialog.java:81 (grep.txt section 4: class YesNoDialog$1 posts DialogNegativeClickedEvent)',
  evidence='SRC transactions/YesNoDialog.java:65-83 (post at 81, negative listener); SRC transactions/CheckingTransactionEditActivity.java:222-225; INFERRED EventBus delivery (library not read)')

# ---- GUI edges from the form S_CHECKING_TRANSACTION_EDIT (page -> method)

gui('S_CHECKING_TRANSACTION_EDIT', 'CheckingTransactionEditActivity.onOptionsItemSelected',
    'Tap the up arrow or the save icon in the toolbar',
    evidence='SRC transactions/CheckingTransactionEditActivity.java:150-159 (home 153; save 155); SRC core/MenuHelper.java:37, 88; FW-SRC core/java/android/app/Activity.java:3450 (onOptionsItemSelected dispatch); INFERRED: the AppCompat toolbar path is not read')

gui('S_CHECKING_TRANSACTION_EDIT', 'CheckingTransactionEditActivity.onBackPressed',
    'Press the Back key',
    evidence='SRC transactions/CheckingTransactionEditActivity.java:189-191 (onBackPressed calls onActionCancelClick at 190); FW-SRC core/java/android/app/Activity.java:2975-2980 (onKeyUp calls onBackPressed at 2980); INFERRED: the key path to onKeyUp is not read')

gui('S_CHECKING_TRANSACTION_EDIT', 'AttachmentAdapter$ViewHolder.lambda$bind$0',
    'Tap an attachment row in the attachments list',
    evidence='SRC transactions/AttachmentAdapter.java:74-78 (click listener at 77); SRC transactions/EditTransactionCommonFunctions.java:749-750 (the attachments list is set up on this form)')
