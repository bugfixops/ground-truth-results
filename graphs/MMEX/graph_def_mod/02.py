
UNREACHABLE['SplitItemTouchCallback.onMove'] = ('framework_never_calls',
  'the androidx ItemTouchHelper calls Callback.onMove only while a drag is in progress (INFERRED, library not read); getMovementFlags returns dragFlags = 0, so no drag direction is offered, and no auto_calls.json record reaches onMove (0 incoming)',
  'SRC transactions/SplitItemTouchCallback.java:43 (dragFlags = 0), 47 (swipe flags only), 60-71 (onMove body); label_134.grep.txt Q1, Q17, Q18, Q20, Q27',
  'INFERRED')

UNREACHABLE['SplitCategoriesAdapter.onItemMove'] = ('framework_never_calls',
  'its only caller is SplitItemTouchCallback.onMove (auto CALL record at SplitItemTouchCallback.java:69), which is UNREACHABLE; the body has no statement (every line commented out)',
  'SRC transactions/SplitCategoriesAdapter.java:236-249 (body commented out); transactions/SplitItemTouchCallback.java:69; label_134.grep.txt Q1',
  'INFERRED')

sup(('SplitItemTouchCallback.onMove', 'SplitCategoriesAdapter.onItemMove'))  # D14a: caller UNREACHABLE; auto CALL record at SplitItemTouchCallback.java:69

# ---- part 128 (2026-10-29)
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

# ---- part 130 (2026-10-29)
# ================================================================== batch 130 (label_130): EditTransactionCommonFunctions (methods 1-40 of 115); 40 methods
# Result: 39 REACHABLE, 1 UNREACHABLE (rows: graphs/MMEX/parts/label_130.md). Grep evidence: graphs/MMEX/parts/label_130.grep.txt.
# This file writes:
#   - 1 UNREACHABLE entry (kind no_trigger_in_app, SOURCE): hasAttachments (its only definition is at line 260-262; no caller anywhere),
#   - 1 sup cut (D14) for the auto CALL record out of the UNREACHABLE method: hasAttachments -> getAttachments (auto record line 261).
# No e() edge is written: every caller of the other 39 methods is either an auto CALL record (already in auto_calls.json, D7) or an edge owned by another batch
# (D1: edges are owned by the destination batch; AGENT_NOTES.md has no "Ownership rule (cross-batch edges)" section, so D1 is the rule used).
# Routes that are not auto CALL records (EVENT, GUI, ENTRY, LIFECYCLE framework steps) are in label_130.md only; their unprinted platform steps are marked INFERRED there.

# ---- UNREACHABLE: hasAttachments has no caller anywhere in the app source or the build

UNREACHABLE['EditTransactionCommonFunctions.hasAttachments'] = ('no_trigger_in_app',
    'Only definition in the app source (transactions/EditTransactionCommonFunctions.java:260-262, returns !getAttachments().isEmpty()); grep over the app source finds no caller (label_130.grep.txt hasAttachments grep); the javac debug class grep finds no reference (exit 1); auto_calls.json has no record with dst hasAttachments (n=0, label_130.grep.txt auto query). Its only outgoing record is to getAttachments at line 261, which is cut by sup (D14)',
    'transactions/EditTransactionCommonFunctions.java:260-262 (261); label_130.grep.txt (hasAttachments grep; javac debug classes grep; auto query n=0)',
    'SOURCE')

# ---- D14: the outgoing auto CALL record of the UNREACHABLE method (caller UNREACHABLE in this batch)

sup(('EditTransactionCommonFunctions.hasAttachments', 'EditTransactionCommonFunctions.getAttachments'))  # caller UNREACHABLE (D14); auto record line 261

# ---- part 133 (2026-10-29)
# ================================================================== batch 133 (label_133): transactions.EditTransactionCommonFunctions_MembersInjector (5 methods), EditTransactionViewHolder (1), EditTransactionViewHolder_ViewBinding (2), IntentDataParameters (3), SplitCategoriesActivity (18), SplitCategoriesActivity$1 (2), SplitCategoriesActivity_ViewBinding (3), SplitCategoriesActivity_ViewBinding$1 (2); 36 methods
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_133.md (31 REACHABLE, 5 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence, with the printed output of each grep for a generated or library claim: graphs/MMEX/parts/label_133.grep.txt.
# This file writes 18 e() edges (INTENT 1, LIFECYCLE 2, ENTERS 1, FRAMEWORK 1, GUI 3, RESULT 2, REGISTER 3, ASYNC 3, CALL 2), 0 gui() edges, 5 UNREACHABLE entries and 3 sup pairs.
# Edges are written only where the destination is owned by this batch (D1). Every other route is a CALL edge from auto_calls.json (USE_AUTO, D7) and is not written here.
# Callers outside this batch are interim (D8): the owner of EditTransactionCommonFunctions.showSplitCategoriesForm is not merged; CategoryListFragment.setResult and CalculatorActivity.returnResult are in common/; the three EventBus posters are in SplitCategoriesAdapter (batch 134); the route through HomeFragment.onEvent(AmountEnteredEvent) is batch 024 (AGENT_NOTES D14(b)); CheckingTransactionEditActivity and RecurringTransactionEditActivity are not merged.
# S_SPLIT_CATEGORIES is defined here, because no split screen key existed (grep G12 in label_133.grep.txt). Batch 134 may reuse it.
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1 (the only framework evidence used here); INFERRED = a step whose source or library was not read (EventBus, ButterKnife, AppCompat, Dagger generated code beyond the auto_calls records).

SCREENS.update({
    'S_SPLIT_CATEGORIES': 'Split categories form (SplitCategoriesActivity): one row per split with its amount, category, transaction type and notes; the add button; the save icon in the action bar; the invalid amount dialog',
})

# ---- entry, lifecycle and screen edges

e('EditTransactionCommonFunctions.showSplitCategoriesForm', 'SplitCategoriesActivity.<init>', 'INTENT',
  'startActivityForResult(new Intent(getContext(), SplitCategoriesActivity.class), RequestCodes.SPLIT_TX) with the split rows, currency and transaction type as extras',
  gui=['Tap the split button on the transaction edit form while the transaction is not split yet', 'Tap the category field on the transaction edit form while the transaction is already split'],
  guard='the split button takes the splitting branch (EditTransactionCommonFunctions.java:602-605); the category field takes the split branch (EditTransactionCommonFunctions.java:462-469)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1519-1528 (intent 1519; startActivityForResult 1528); 598-605 (split button listener; showSplitCategoriesForm at 605); 455-469 (category field listener; showSplitCategoriesForm at 469, reached through access$700 per auto_calls.json); SRC transactions/SplitCategoriesActivity.java:57 (auto_calls.json record to MmxBaseFragmentActivity.<init>); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (newActivity creates the instance through newInstance at 1174); FW-SRC core/java/android/app/ActivityThread.java:2667-2671 (newActivity at 2669-2670). INTERIM: the owner of showSplitCategoriesForm is not merged (D8)')

e('SplitCategoriesActivity.<init>', 'SplitCategoriesActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6989-7000 (performCreate calls onCreate at 6997 and 6999)')

e('SplitCategoriesActivity.onCreate', 'S_SPLIT_CATEGORIES', 'ENTERS',
  'the split categories form is shown',
  evidence='SRC transactions/SplitCategoriesActivity.java:100 (setContentView R.layout.activity_split_categories); SRC res/layout/activity_split_categories.xml:68-69 (the fab view)')

e('SplitCategoriesActivity.onCreate', 'SplitCategoriesActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='SRC transactions/SplitCategoriesActivity.java:108-115 (onCreateOptionsMenu; addSaveToolbarIcon at 112); FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:626-633 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3392 (onCreateOptionsMenu at 3388); INFERRED: the activity extends the AppCompat base, and the AppCompat delegate path to onCreatePanelMenu is not in fw_src and was not read')

e('SplitCategoriesActivity.onCreate', 'SplitCategoriesActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity: ActivityThread.callCallActivityOnSaveInstanceState calls onSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:4713-4722 (callCallActivityOnSaveInstanceState); FW-SRC core/java/android/app/Instrumentation.java:1385-1386; FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState at 1496); SRC transactions/SplitCategoriesActivity.java:180-189 (body)')

# ---- GUI edges from the screen

e('S_SPLIT_CATEGORIES', 'SplitCategoriesActivity.onOptionsItemSelected', 'GUI',
  'the framework calls onOptionsItemSelected for the save menu item; the save item calls onActionDoneClick',
  gui=['Tap the save (check) icon in the action bar of the split categories form'],
  evidence='SRC transactions/SplitCategoriesActivity.java:112 (addSaveToolbarIcon), 117-123 (onOptionsItemSelected; MenuHelper.save at 119-120 returns onActionDoneClick); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450); INFERRED: the AppCompat dispatch from the action bar to onOptionsItemSelected is not in fw_src')

e('S_SPLIT_CATEGORIES', 'SplitCategoriesActivity_ViewBinding$1.doClick', 'GUI',
  'the user taps the add button (R.id.fab): the generated @OnClick listener calls onFabClick, which adds a split row',
  gui=['Tap the add (floating action) button on the split categories form'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated SplitCategoriesActivity_ViewBinding (INFERRED: the ButterKnife library and the generated code are not read beyond the auto_calls.json record at line 36)',
  evidence='SRC transactions/SplitCategoriesActivity.java:191-194 (@OnClick(R.id.fab) onFabClick); SRC res/layout/activity_split_categories.xml:68-69 (fab id); auto_calls.json record SplitCategoriesActivity_ViewBinding$1.doClick -> SplitCategoriesActivity.onFabClick (SplitCategoriesActivity_ViewBinding.java:36)')

e('S_SPLIT_CATEGORIES', 'SplitCategoriesActivity$1.onClick', 'GUI',
  'the user taps OK in the invalid amount dialog: the dialog closes through dialog.dismiss',
  gui=['Tap OK in the invalid amount dialog after a negative amount was returned for a split row'],
  needs_state=state_text('a negative amount is returned from the calculator for a split row, so showInvalidAmountDialog runs (SplitCategoriesActivity.java:276-278)', ('data',)),
  evidence='SRC transactions/SplitCategoriesActivity.java:317-329 (showInvalidAmountDialog: setPositiveButton(android.R.string.ok) with the listener at 321; onClick 323-326; dismiss at 325; show at 328); SRC transactions/SplitCategoriesActivity.java:20 (import android.app.AlertDialog: the framework dialog); SRC transactions/SplitCategoriesActivity.java:276-279 (negative amount gate); FW-SRC core/java/com/android/internal/app/AlertController.java:709-710 (mButtonPositive.setOnClickListener(mButtonHandler)), 125-146 (mButtonHandler click message at 140), 160-166 (handleMessage calls the OnClickListener at 166)')

# ---- ButterKnife binding (generated classes; the library is not read: INFERRED, D22)

e('SplitCategoriesActivity.onCreate', 'SplitCategoriesActivity_ViewBinding.<init>(SplitCategoriesActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for this activity, which binds the @OnClick handler and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated SplitCategoriesActivity_ViewBinding is built by reflection (INFERRED, library not read)',
  evidence='SRC transactions/SplitCategoriesActivity.java:52 (import butterknife.ButterKnife), 101 (ButterKnife.bind(this); the returned Unbinder is discarded); label_133.grep.txt G5 and G6 (build class SplitCategoriesActivity_ViewBinding.class); label_133.grep.txt auto_calls query (0 incoming records to the constructor)')

e('EditTransactionViewHolder.<init>', 'EditTransactionViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, view) builds the generated binding for this view holder',
  cls='non_standard', via='ButterKnife.bind(this, view) (library): reflection builds EditTransactionViewHolder_ViewBinding (INFERRED, library not read)',
  evidence='SRC transactions/EditTransactionViewHolder.java:37 (import butterknife.ButterKnife), 45 (ButterKnife.bind(this, view); the returned Unbinder is discarded); label_133.grep.txt G5 and G6; label_133.grep.txt auto_calls query (0 incoming records to the constructor)')

# ---- EventBus: the activity subscribes in the base onStart, the three posters are in batch 134 (library dispatch: INFERRED)

e('MmxBaseFragmentActivity.onStart', 'SplitCategoriesActivity.onEvent(AmountEntryRequestedEvent)', 'REGISTER',
  'the activity registers itself on EventBus in onStart; EventBus calls the @Subscribe method onEvent(AmountEntryRequestedEvent) when the event is posted',
  cls='non_standard', via='EventBus (greenrobot): register(this) in the base onStart; @Subscribe onEvent(AmountEntryRequestedEvent) at SplitCategoriesActivity.java:205-211 (library source not read, INFERRED)',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (onStart at 134, register at 141, unregister at 146); SRC transactions/SplitCategoriesActivity.java:205-211 (@Subscribe and body); INFERRED: EventBus library source not read')

e('MmxBaseFragmentActivity.onStart', 'SplitCategoriesActivity.onEvent(CategoryRequestedEvent)', 'REGISTER',
  'the activity registers itself on EventBus in onStart; EventBus calls the @Subscribe method onEvent(CategoryRequestedEvent) when the event is posted',
  cls='non_standard', via='EventBus (greenrobot): register(this) in the base onStart; @Subscribe onEvent(CategoryRequestedEvent) at SplitCategoriesActivity.java:213-216 (library source not read, INFERRED)',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146; SRC transactions/SplitCategoriesActivity.java:213-216 (@Subscribe and body); INFERRED: EventBus library source not read')

e('MmxBaseFragmentActivity.onStart', 'SplitCategoriesActivity.onEvent(SplitItemRemovedEvent)', 'REGISTER',
  'the activity registers itself on EventBus in onStart; EventBus calls the @Subscribe method onEvent(SplitItemRemovedEvent) when the event is posted',
  cls='non_standard', via='EventBus (greenrobot): register(this) in the base onStart; @Subscribe onEvent(SplitItemRemovedEvent) at SplitCategoriesActivity.java:200-203 (library source not read, INFERRED)',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146; SRC transactions/SplitCategoriesActivity.java:200-203 (@Subscribe and body); INFERRED: EventBus library source not read')

e('SplitCategoriesAdapter$1.onClick', 'SplitCategoriesActivity.onEvent(AmountEntryRequestedEvent)', 'ASYNC',
  'the user taps the amount of a split row: the listener posts AmountEntryRequestedEvent and EventBus calls onEvent, which opens the calculator for that row',
  cls='non_standard', via='EventBus (greenrobot): post(AmountEntryRequestedEvent) to the @Subscribe method (library dispatch, INFERRED)',
  evidence='SRC transactions/SplitCategoriesAdapter.java:161 (txtAmount.setOnClickListener), 174 (EventBus.getDefault().post(new AmountEntryRequestedEvent(...))); SRC transactions/SplitCategoriesActivity.java:205-211 (subscriber); the adapter belongs to batch 134 and its listener is not labelled here; INFERRED: EventBus library dispatch not read')

e('SplitCategoriesAdapter$2.onClick', 'SplitCategoriesActivity.onEvent(CategoryRequestedEvent)', 'ASYNC',
  'the user taps the category of a split row: the listener posts CategoryRequestedEvent and EventBus calls onEvent, which opens the category selector',
  cls='non_standard', via='EventBus (greenrobot): post(CategoryRequestedEvent) to the @Subscribe method (library dispatch, INFERRED)',
  evidence='SRC transactions/SplitCategoriesAdapter.java:180 (txtSelectCategory.setOnClickListener), 185 (post of CategoryRequestedEvent); SRC transactions/SplitCategoriesActivity.java:213-216 (subscriber); INFERRED: EventBus library dispatch not read')

e('SplitCategoriesAdapter.onItemDismiss', 'SplitCategoriesActivity.onEvent(SplitItemRemovedEvent)', 'ASYNC',
  'a row is swiped away: the item touch callback calls onItemDismiss, which posts SplitItemRemovedEvent, and EventBus calls onEvent, which removes the row',
  cls='non_standard', via='ItemTouchHelper callback (library) calls onItemDismiss; EventBus post to the @Subscribe method (library dispatch, INFERRED)',
  evidence='SRC transactions/SplitCategoriesAdapter.java:252-255 (onItemDismiss; post of SplitItemRemovedEvent at 255); SRC transactions/SplitCategoriesActivity.java:200-203 (subscriber); SRC transactions/SplitCategoriesActivity.java:271 (SplitItemTouchCallback created in initRecyclerView, auto_calls.json); INFERRED: the ItemTouchHelper dispatch to onItemDismiss is library code and was not read')

# ---- result edges (startActivityForResult from this activity; the result is set in another class)

e('CategoryListFragment.setResult', 'SplitCategoriesActivity.onActivityResult', 'RESULT',
  'the category list returns the checked category: setResult(RESULT_OK, result) and finish, and the framework calls onActivityResult with REQUEST_PICK_CATEGORY',
  guard='requestCode is REQUEST_PICK_CATEGORY (SplitCategoriesActivity.java:131) and resultCode is RESULT_OK with data non-null (SplitCategoriesActivity.java:129); the RESULT_OK branch needs ACTION_PICK and a checked category (CategoryListFragment.java:314, 324, 351-354)',
  evidence='SRC common/CategoryListFragment.java:313-359 (protected setResult; ACTION_PICK at 314; checked category at 321-324; RESULT_OK at 354; RESULT_CANCELED at 356); SRC common/BaseListFragment.java:177-180 (setResultAndFinish calls setResult at 178, then finish); SRC transactions/SplitCategoriesActivity.java:69 (REQUEST_PICK_CATEGORY = 1), 314 (startActivityForResult with REQUEST_PICK_CATEGORY); FW-SRC core/java/android/app/ActivityThread.java:4253-4265 (deliverResults calls dispatchActivityResult at 4264-4265); FW-SRC core/java/android/app/Activity.java:7259-7266 (onActivityResult at 7266)')

e('CalculatorActivity.returnResult', 'SplitCategoriesActivity.onActivityResult', 'RESULT',
  'the calculator returns the amount and finishes: setResult(RESULT_OK, result), and the framework calls onActivityResult with the row request code plus the amount offset',
  guard='requestCode >= amountRequestOffset (SplitCategoriesActivity.java:142) and resultCode is RESULT_OK with data non-null (SplitCategoriesActivity.java:129); the request code is the row request id plus 1000 (SplitCategoriesActivity.java:79, 207-210; Calculator.java:79 passes it to startActivityForResult)',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult: setResult(RESULT_OK) at 443, finish at 444); SRC common/Calculator.java:79 (activity.startActivityForResult(intent, requestCode)); SRC transactions/SplitCategoriesActivity.java:79 (amountRequestOffset = 1000), 207-210 (Calculator show with event.requestId + amountRequestOffset); FW-SRC core/java/android/app/ActivityThread.java:4253-4265; FW-SRC core/java/android/app/Activity.java:7259-7266')

# ---- UNREACHABLE entries (kind, reason, source reference, confirmed_by)

UNREACHABLE['EditTransactionCommonFunctions_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (build class transactions/EditTransactionCommonFunctions_MembersInjector.class, not in the source root). Its only caller record is EditTransactionCommonFunctions_MembersInjector.create (auto_calls.json, line 31), and create has no caller record (the auto_calls query in label_133.grep.txt shows 0 incoming records). The app source has no reference to the MembersInjector name (grep G2)',
  'auto_calls.json record EditTransactionCommonFunctions_MembersInjector.java:31; label_133.grep.txt G2, G3 and the auto_calls query',
  'INFERRED')

UNREACHABLE['EditTransactionCommonFunctions_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (not in the source root) with no caller record in auto_calls.json: the name occurs only as the source of records, never as a destination (0 incoming records). The app source has no MembersInjector reference (grep G2)',
  'label_133.grep.txt G2, G3 and the auto_calls query (0 incoming records)',
  'INFERRED')

UNREACHABLE['EditTransactionCommonFunctions_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (not in the source root) with no caller record for any receiver in auto_calls.json (0 incoming records). The component calls the static injectors directly (DaggerMmxComponent.java:569 and 571), not injectMembers',
  'auto_calls.json records DaggerMmxComponent.java:569, 571; label_133.grep.txt G2, G3 and the auto_calls query (0 incoming records)',
  'INFERRED')

UNREACHABLE['EditTransactionViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated Unbinder method (build class EditTransactionViewHolder_ViewBinding.class defines it; grep G4). The constructor is called from EditTransactionViewHolder.<init> at line 45, which discards the returned binding, so no unbind call exists. The transactions/ source has no unbind (grep G1), and no auto_calls.json record has unbind as a source or destination (0 records)',
  'SRC transactions/EditTransactionViewHolder.java:45; label_133.grep.txt G1, G4 and the unbind query (0 records)',
  'INFERRED')

UNREACHABLE['SplitCategoriesActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated Unbinder method (build class SplitCategoriesActivity_ViewBinding.class defines it; grep G4). The constructor is called from SplitCategoriesActivity.onCreate at line 101, which discards the returned binding, and SplitCategoriesActivity declares no onDestroy (grep G13). The transactions/ source has no unbind (grep G1), and no auto_calls.json record has unbind as a source or destination (0 records)',
  'SRC transactions/SplitCategoriesActivity.java:101; label_133.grep.txt G1, G4, G13 and the unbind query (0 records)',
  'INFERRED')

# ---- auto edges that cannot run: cut the exact edge only (D14); the MembersInjector injectors stay reachable through DaggerMmxComponent

sup(('EditTransactionCommonFunctions_MembersInjector.create', 'EditTransactionCommonFunctions_MembersInjector.<init>'))  # create has no caller, so the bytecode call at auto_calls.json line 31 cannot run
sup(('EditTransactionCommonFunctions_MembersInjector.injectMembers', 'EditTransactionCommonFunctions_MembersInjector.injectDateTimeUtilsLazy'))  # injectMembers has no caller; auto_calls.json line 38
sup(('EditTransactionCommonFunctions_MembersInjector.injectMembers', 'EditTransactionCommonFunctions_MembersInjector.injectMDatabases'))  # injectMembers has no caller; auto_calls.json line 37

# ---- part 137 (2026-10-29)
# ================================================================== batch 137 (label_137): MmxDatabaseUtils (20 methods), MmxDatabaseUtils_Factory (4), MmxDatabaseUtils_MembersInjector (6); 30 methods
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_137.md (18 REACHABLE, 12 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_137.grep.txt.
# This file writes 0 e() edges, 0 gui() edges, 12 UNREACHABLE entries and 21 sup pairs.
# Every route into this batch is a CALL edge from auto_calls.json (USE_AUTO, D7), so none is written here. Batch 137 owns no framework callback.
# The callers of this batch's methods are in batches 115, 080, 077, 041, 040, 123, 054, 055, 049 and 044 (all merged), so no route is interim (D8).
# sup() cuts the auto CALL records whose caller is UNREACHABLE in this batch, so the bytecode edge cannot run (D14). The sup pairs are listed by group below.
# Evidence labels: SRC = printed line of the source tree; INFERRED = generated Dagger code or javac behaviour, source not read (not in the repo).

# ---- createDatabase group: no caller for the public overloads; createDatabase_Internal and its callees never run

sup(('MmxDatabaseUtils.createDatabase()', 'MmxDatabaseUtils.createDatabase(String)'))  # createDatabase() has no caller
sup(('MmxDatabaseUtils.createDatabase(String)', 'MmxDatabaseUtils.createDatabase_Internal'))  # createDatabase(String) has no caller
sup(('MmxDatabaseUtils.createDatabase_Internal', 'MmxDatabaseUtils.cleanupFilename'))  # createDatabase_Internal has no caller
sup(('MmxDatabaseUtils.createDatabase_Internal', 'DatabaseManager.getDefaultDatabaseDirectory'))
sup(('MmxDatabaseUtils.createDatabase_Internal', 'DatabaseManager.<init>'))
sup(('MmxDatabaseUtils.createDatabase_Internal', 'AppSettings.getDatabaseSettings'))
sup(('MmxDatabaseUtils.createDatabase_Internal', 'AppSettings.<init>'))
sup(('MmxDatabaseUtils.createDatabase_Internal', 'DatabaseSettings.setDatabasePath'))
sup(('MmxDatabaseUtils.createDatabase_Internal', 'MmxDatabaseUtils.getContext'))

# ---- Dagger factory (generated, INFERRED): no caller of create, get or newMmxDatabaseUtils

sup(('MmxDatabaseUtils_Factory.create', 'MmxDatabaseUtils_Factory.<init>'))  # create has no caller
sup(('MmxDatabaseUtils_Factory.get', 'MmxDatabaseUtils.<clinit>'))  # get has no caller
sup(('MmxDatabaseUtils_Factory.get', 'MmxDatabaseUtils.<init>'))
sup(('MmxDatabaseUtils_Factory.get', 'MmxDatabaseUtils_MembersInjector.injectMDatabasesLazy'))
sup(('MmxDatabaseUtils_Factory.get', 'MmxDatabaseUtils_MembersInjector.injectOpenHelper'))
sup(('MmxDatabaseUtils_Factory.get', 'MmxDatabaseUtils_MembersInjector.injectInfoRepositorySqlLazy'))
sup(('MmxDatabaseUtils_Factory.newMmxDatabaseUtils', 'MmxDatabaseUtils.<clinit>'))  # newMmxDatabaseUtils has no caller
sup(('MmxDatabaseUtils_Factory.newMmxDatabaseUtils', 'MmxDatabaseUtils.<init>'))

# ---- Dagger members injector (generated, INFERRED): create has no caller, so the injector object is never built; injectMembers has no caller

sup(('MmxDatabaseUtils_MembersInjector.create', 'MmxDatabaseUtils_MembersInjector.<init>'))  # create has no caller
sup(('MmxDatabaseUtils_MembersInjector.injectMembers', 'MmxDatabaseUtils_MembersInjector.injectInfoRepositorySqlLazy'))  # injectMembers has no caller
sup(('MmxDatabaseUtils_MembersInjector.injectMembers', 'MmxDatabaseUtils_MembersInjector.injectOpenHelper'))
sup(('MmxDatabaseUtils_MembersInjector.injectMembers', 'MmxDatabaseUtils_MembersInjector.injectMDatabasesLazy'))

# ---- UNREACHABLE: SOURCE = no caller in the app source (grep output: graphs/MMEX/parts/label_137.grep.txt)

UNREACHABLE['MmxDatabaseUtils.createDatabase()'] = (
  'no_trigger_in_app',
  'public no-argument overload with no caller. No createDatabase call on an MmxDatabaseUtils receiver exists in the source root: the createDatabase calls in the app are FileStorageHelper.createDatabase(Intent) (SelectDatabaseActivity.java:83, MainActivity.java:331). Its only callee is createDatabase(String).',
  'utils/MmxDatabaseUtils.java:133-135; grep label_137.grep.txt',
  'SOURCE')

UNREACHABLE['MmxDatabaseUtils.createDatabase(String)'] = (
  'no_trigger_in_app',
  'public overload whose only caller is createDatabase(), which has no caller. Its only callee is createDatabase_Internal (line 147).',
  'utils/MmxDatabaseUtils.java:143-152; grep label_137.grep.txt',
  'SOURCE')

UNREACHABLE['MmxDatabaseUtils.createDatabase_Internal'] = (
  'no_trigger_in_app',
  'private; its only caller is createDatabase(String) (line 147), which is UNREACHABLE. Its callees (cleanupFilename, DatabaseManager, AppSettings, DatabaseSettings, getContext at lines 264-285) never run.',
  'utils/MmxDatabaseUtils.java:261-288; auto_calls createDatabase_Internal records (lines 264, 267, 285); grep label_137.grep.txt',
  'SOURCE')

UNREACHABLE['MmxDatabaseUtils.cleanupFilename'] = (
  'no_trigger_in_app',
  'private; its only caller is createDatabase_Internal (line 264), which is UNREACHABLE. No other auto record into it.',
  'utils/MmxDatabaseUtils.java:264, 290-303; grep label_137.grep.txt',
  'SOURCE')

UNREACHABLE['MmxDatabaseUtils.isEncryptedDatabase'] = (
  'no_trigger_in_app',
  'public static with no caller: the grep of the source root finds only its declaration, and no auto record has it as callee.',
  'utils/MmxDatabaseUtils.java:74-76; grep label_137.grep.txt',
  'SOURCE')

# ---- UNREACHABLE: INFERRED = generated Dagger code (not in the repo; source not read); no caller in auto_calls.json or the bytecode

UNREACHABLE['MmxDatabaseUtils_Factory.<init>'] = (
  'no_trigger_in_app',
  'constructor of the Dagger factory, reached only from MmxDatabaseUtils_Factory.create (auto record at line 53). create has no caller, so the constructor never runs. Generated code: INFERRED, source not read.',
  'auto_calls.json (create -> <init>, MmxDatabaseUtils_Factory.java:53); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_Factory.create'] = (
  'no_trigger_in_app',
  'static factory of the Dagger factory with no caller: no auto record has it as callee, and DaggerMmxComponent.class has no reference to MmxDatabaseUtils_Factory (binary grep count 0). MmxComponent declares only inject(MmxDatabaseUtils) at line 101, with no provision method, so the component never asks for a factory. Generated code: INFERRED, source not read.',
  'core/ioc/MmxComponent.java:101; auto_calls.json; graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_Factory.get'] = (
  'no_trigger_in_app',
  'instance method of the Dagger factory with no caller: no auto record has it as callee, and no class in the build references MmxDatabaseUtils_Factory except the factory itself. Its CALLs (lines 38-43) are cut by sup. Generated code: INFERRED, source not read.',
  'auto_calls.json (get -> <clinit>, <init>, injectX at lines 38-43); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_Factory.newMmxDatabaseUtils'] = (
  'no_trigger_in_app',
  'generated helper of the Dagger factory with no caller. Its CALLs to MmxDatabaseUtils.<clinit> and <init> (line 58) are cut by sup. Generated code: INFERRED, source not read.',
  'auto_calls.json (newMmxDatabaseUtils -> <clinit>, <init>, line 58); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_MembersInjector.<init>'] = (
  'no_trigger_in_app',
  'constructor of the Dagger members injector, reached only from MmxDatabaseUtils_MembersInjector.create (auto record at line 36). create has no caller. Generated code: INFERRED, source not read.',
  'auto_calls.json (create -> <init>, MmxDatabaseUtils_MembersInjector.java:36); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_MembersInjector.create'] = (
  'no_trigger_in_app',
  'static factory of the Dagger members injector with no caller: no auto record has it as callee. DaggerMmxComponent.injectMmxDatabaseUtils calls the three static injectX methods directly (DaggerMmxComponent.java:533, 535, 537), so no injector object is built. Generated code: INFERRED, source not read.',
  'auto_calls.json (DaggerMmxComponent.injectMmxDatabaseUtils -> injectX at 533, 535, 537); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

UNREACHABLE['MmxDatabaseUtils_MembersInjector.injectMembers'] = (
  'no_trigger_in_app',
  'instance method reached only through the MembersInjector interface on an injector object, which only create would build; create has no caller. No auto record has injectMembers as callee. Its three CALLs (lines 42-44) are cut by sup. Generated code: INFERRED, source not read.',
  'auto_calls.json (injectMembers -> injectX at lines 42-44); graphs/MMEX/parts/label_137.grep.txt',
  'INFERRED')

# ---- part 135 (2026-10-29)
# ================================================================== batch 135 (label_135): YesNoDialog (7 methods, listeners $1 and $2), the five transactions/events classes (5), TutorialAccountsFragment (3), TutorialActivity (7), TutorialActivity_ViewBinding with $1 (5), TutorialFinancialOverviewFragment (4), TutorialGlobalFragment (4), TutorialPagerAdapter (4): 39 methods
# Result: 36 REACHABLE, 3 UNREACHABLE (YesNoDialog.getPurpose, TutorialActivity_ViewBinding.unbind, TutorialPagerAdapter.getPageTitle). getPageTitle is settled as framework_never_calls on INFERRED library behaviour and is flagged for the parent to review.
# Rows and reasons: graphs/MMEX/parts/label_135.md. Grep and auto_calls evidence: graphs/MMEX/parts/label_135.grep.txt.
# This file writes 1 SCREENS key (S_TUTORIAL; grep of graph_def.py and parts/*.py found no key for it), 20 e() edges and 3 UNREACHABLE entries.
# No sup pair is written. YesNoDialog.getPurpose has no auto_calls record in either direction. TutorialActivity_ViewBinding.unbind has 0 callers and outgoing auto records only to library calls (IllegalStateException.<init>, View.setOnClickListener); those edges are never reached, so no cut is needed.
# Every other REACHABLE route is an auto CALL record (auto_calls.json, bytecode-derived; D7) and is cited in the row, not written here.
# The five event constructors have no edge here: their CALL records come from YesNoDialog$1/$2.onClick and SplitCategoriesAdapter (batch 134, interim D8).

SCREENS.update({
    'S_TUTORIAL': 'Tutorial screen (TutorialActivity): five swipeable pages (accounts, transactions, global, financial overview, sync), the Skip control and the options menu',
})

MENU_KEY = env_text('the device has a hardware menu key: this theme has no action bar, so the options menu opens only from the menu key', ('hardware',))

# ---- TutorialActivity: first-run start, lifecycle, pager, skip control, result and options menu

e('MainActivity.showTutorial', 'TutorialActivity.<init>', 'INTENT',
  'startActivity(new Intent(this, TutorialActivity.class)) with FLAG_ACTIVITY_CLEAR_TOP: the first-run tutorial, started from showPrerequisite',
  needs_state=state_text('first run: the tutorial has not been dismissed (getShowTutorial is true; the default is true, BehaviourSettings.java:86-88)', ('settings',)),
  evidence='SRC home/MainActivity.java:812-817 (showTutorial; Intent 813, startActivity 816); SRC home/MainActivity.java:184 (showPrerequisite call), 1351-1353 (isTutorialNeeded), 1478-1482 (showTutorial at 1481); SRC settings/BehaviourSettings.java:86-88; SRC AndroidManifest.xml:314-319 (no intent-filter)')

e('TutorialActivity.<init>', 'TutorialActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate); SRC tutorial/TutorialActivity.java:49-73')

e('TutorialActivity.onCreate', 'S_TUTORIAL', 'ENTERS',
  'the tutorial screen is shown: setContentView (activity_tutorial) and the pager adapter are set',
  evidence='SRC tutorial/TutorialActivity.java:55, 61-63')

e('TutorialActivity.onCreate', 'TutorialActivity_ViewBinding.<init>(TutorialActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for this activity, which binds the @OnClick skip handler',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated TutorialActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC tutorial/TutorialActivity.java:57; INFERRED ButterKnife generated binding (library and generated source not read); precedent graph_def.py:409-412 (PasscodeActivity)')

e('TutorialActivity.onCreate', 'TutorialPagerAdapter.getItem', 'FRAMEWORK',
  'the ViewPager asks the adapter for the first page when the adapter is set',
  evidence='SRC tutorial/TutorialActivity.java:61-63; INFERRED androidx ViewPager and FragmentStatePagerAdapter call getItem for the first page (androidx source not read); precedent graph_def.py:225 (AboutActivity.onCreate -> AboutTabAdapter.getItem)')

e('TutorialActivity.onCreate', 'TutorialPagerAdapter.getCount', 'FRAMEWORK',
  'the ViewPager reads the page count when the adapter is set (5 pages)',
  evidence='SRC tutorial/TutorialPagerAdapter.java:63-65; SRC tutorial/TutorialActivity.java:63; INFERRED androidx PagerAdapter (library not read); precedent graph_def.py:221')

e('S_TUTORIAL', 'TutorialPagerAdapter.getItem', 'GUI',
  'swipe between the tutorial pages: the ViewPager asks for the page fragment',
  gui=['Swipe between the tutorial pages'],
  evidence='SRC tutorial/TutorialActivity.java:61-63; INFERRED androidx ViewPager calls getItem on a page change (library source not read); precedent graph_def.py:229')

e('TutorialActivity.onCloseClicked', 'TutorialActivity.onActivityResult', 'RESULT',
  'the framework delivers the result of GeneralSettingsActivity (started for result at line 95) when it finishes; GeneralSettingsActivity calls no setResult, so the result code is RESULT_CANCELED, and this handler does not check resultCode',
  guard='requestCode is REQUEST_GENERAL_PREFERENCES (TutorialActivity.java:79)',
  evidence='SRC tutorial/TutorialActivity.java:76-96; grep section 8 (no setResult or finish in settings/GeneralSettingsActivity.java and settings/BaseSettingsFragmentActivity.java); FW-SRC core/java/android/app/ActivityThread.java:4253-4265 (deliverResults); FW-SRC core/java/android/app/Activity.java:7259-7266 (dispatchActivityResult calls onActivityResult)')

e('S_TUTORIAL', 'TutorialActivity_ViewBinding$1.doClick', 'GUI',
  'tap the Skip control (skipTextView): the listener attached by the generated binding calls onCloseClicked',
  gui=['Tap Skip on the tutorial screen'],
  cls='non_standard', via='ButterKnife @OnClick binding (generated class TutorialActivity_ViewBinding$1, INFERRED, library and generated source not read)',
  evidence='SRC tutorial/TutorialActivity.java:90-91 (@OnClick at 90); SRC res/layout/activity_tutorial.xml:46 (skipTextView); auto TutorialActivity_ViewBinding$1.doClick -> TutorialActivity.onCloseClicked (TutorialActivity_ViewBinding.java:34)')

e('S_TUTORIAL', 'TutorialActivity.onCreateOptionsMenu', 'GUI',
  'press the menu key: PhoneWindow.preparePanel calls the callback onCreatePanelMenu, which calls onCreateOptionsMenu (the menu is inflated at TutorialActivity.java:101)',
  gui=['Press the hardware menu key'], env=MENU_KEY,
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:1916-1918 (KEYCODE_MENU opens the options panel), 580 (preparePanel), 631 (cb.onCreatePanelMenu); FW-SRC core/java/android/app/Activity.java:3386-3390 (onCreatePanelMenu calls onCreateOptionsMenu); SRC tutorial/TutorialActivity.java:98-103; SRC res/menu/menu_tutorial.xml; SRC AndroidManifest.xml:314-319 (NoTitleBar.Fullscreen theme)')

e('S_TUTORIAL', 'TutorialActivity.onOptionsItemSelected', 'GUI',
  'tap the settings item (action_settings) in the options menu: Activity.onMenuItemSelected calls onOptionsItemSelected',
  gui=['Press the hardware menu key and tap the settings item'], env=MENU_KEY,
  evidence='FW-SRC core/java/android/app/Activity.java:3439-3450 (onOptionsItemSelected at 3450); SRC tutorial/TutorialActivity.java:105-118 (action_settings at 113, returns true at 114)')

# ---- YesNoDialog: created in EditTransactionCommonFunctions.onTransferSelected; AlertDialog buttons dispatch to the listeners

e('YesNoDialog.<init>', 'YesNoDialog.onCreateDialog', 'LIFECYCLE',
  'the DialogFragment calls onCreateDialog when the dialog is shown (dialog.show at EditTransactionCommonFunctions.java:1459)',
  needs_state=state_text('the transaction has split categories (hasSplitCategories, EditTransactionCommonFunctions.java:1448)', ('data',)),
  evidence='SRC transactions/YesNoDialog.java:58-85; SRC transactions/EditTransactionCommonFunctions.java:1446-1460; INFERRED androidx DialogFragment calls onCreateDialog after show (library not in the dataset)')

e('YesNoDialog.onCreateDialog', 'YesNoDialog$1.onClick', 'FRAMEWORK',
  'the No (negative) button of the AlertDialog: AlertController mButtonHandler sends the click and handleMessage calls the listener',
  evidence='FW-SRC core/java/com/android/internal/app/AlertController.java:125-145 (mButtonHandler.onClick), 158-168 (handleMessage calls the OnClickListener); SRC transactions/YesNoDialog.java:76-83 (setNegativeButton at 76); auto YesNoDialog$1.onClick -> DialogNegativeClickedEvent.<init> (YesNoDialog.java:81)')

e('YesNoDialog.onCreateDialog', 'YesNoDialog$2.onClick', 'FRAMEWORK',
  'the Yes (positive) button of the AlertDialog: same AlertController path as the No button',
  evidence='FW-SRC core/java/com/android/internal/app/AlertController.java:125-145, 158-168; SRC transactions/YesNoDialog.java:68-75 (setPositiveButton at 68); auto YesNoDialog$2.onClick -> DialogPositiveClickedEvent.<init> (YesNoDialog.java:73)')

# ---- TutorialAccountsFragment, TutorialFinancialOverviewFragment, TutorialGlobalFragment: lifecycle after the constructor (D21)

e('TutorialAccountsFragment.<init>', 'TutorialAccountsFragment.onCreate', 'LIFECYCLE',
  'the fragment manager runs the fragment lifecycle after the instance is created by getItem',
  evidence='SRC tutorial/TutorialAccountsFragment.java:34-41; INFERRED androidx FragmentStatePagerAdapter instantiates the fragment and runs its lifecycle (library not read)')

e('TutorialAccountsFragment.onCreate', 'TutorialAccountsFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC tutorial/TutorialAccountsFragment.java:39-56; INFERRED androidx Fragment lifecycle (library not read)')

e('TutorialFinancialOverviewFragment.<init>', 'TutorialFinancialOverviewFragment.onCreate', 'LIFECYCLE',
  'the fragment manager runs the fragment lifecycle after the instance is created by newInstance',
  evidence='SRC tutorial/TutorialFinancialOverviewFragment.java:49-60; INFERRED androidx Fragment lifecycle (library not read)')

e('TutorialFinancialOverviewFragment.onCreate', 'TutorialFinancialOverviewFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC tutorial/TutorialFinancialOverviewFragment.java:53-67; INFERRED androidx Fragment lifecycle (library not read)')

e('TutorialGlobalFragment.<init>', 'TutorialGlobalFragment.onCreate', 'LIFECYCLE',
  'the fragment manager runs the fragment lifecycle after the instance is created by newInstance',
  evidence='SRC tutorial/TutorialGlobalFragment.java:50-61; INFERRED androidx Fragment lifecycle (library not read)')

e('TutorialGlobalFragment.onCreate', 'TutorialGlobalFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC tutorial/TutorialGlobalFragment.java:54-68; INFERRED androidx Fragment lifecycle (library not read)')

# ---- UNREACHABLE: no caller in the source root, no auto_calls record

UNREACHABLE['YesNoDialog.getPurpose'] = ('no_trigger_in_app',
  'no caller in the source root: the grep matches only the definition, the getter has no auto_calls record, and nothing reads mPurpose through it',
  'SRC transactions/YesNoDialog.java:53-55; label_135.grep.txt section 1',
  'SOURCE')

UNREACHABLE['TutorialActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root): ButterKnife.bind(this) at TutorialActivity.java:57 discards the returned Unbinder, TutorialActivity has no onDestroy, and no caller exists in the source root (label_135.grep.txt section 2) or in auto_calls.json (0 callers)',
  'SRC tutorial/TutorialActivity.java:57; label_135.grep.txt section 2; python-printed auto_calls query (0 callers)',
  'INFERRED')

UNREACHABLE['TutorialPagerAdapter.getPageTitle'] = ('framework_never_calls',
  'the framework calls getPageTitle only from a title widget (TabLayout, PagerTitleStrip, PagerTabStrip; androidx source not read, INFERRED); the tutorial layout has no title widget and no class in the tutorial package creates one, so the call never happens',
  'SRC tutorial/TutorialPagerAdapter.java:68-70; SRC res/layout/activity_tutorial.xml (widget tags); label_135.grep.txt section 3',
  'INFERRED')

# ---- part 136 (2026-10-29)
# ================================================================== batch 136 (label_136): 32 methods in 8 classes
# tutorial/TutorialSyncFragment (4 methods), tutorial/TutorialTransactionsFragment (4), utils/ActivityUtils (3), utils/AlertDialogWrapper (11),
# utils/DialogUtils (3), utils/DrawableUtils (3), utils/ListUtils (2), utils/MathUtils (2)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_136.md (18 REACHABLE, 14 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_136.grep.txt.
# This file writes 4 e() edges (LIFECYCLE, fragment callbacks), 14 UNREACHABLE entries and 1 sup pair.
# Edges are written only for destinations owned by this batch (D1). Every other route is a CALL edge from auto_calls.json (D7) and is not written here.
# The tutorial route (MainActivity -> TutorialActivity -> TutorialPagerAdapter.getItem -> newInstance) is in batch 135 (not merged): interim (D8).
# The AlertDialogWrapper callers are in batch 074 (TipsDialogFragment.onCreateDialog) and batch 085 (EditPriceDialog.onCreateDialog).
# The DialogUtils callers are in batch 126 (SyncServiceMessageHandler.closeDialog) and batch 048 (CurrencyUIFeatures, onCompleted).
# The commented-out DialogUtils call in PriceUpdaterBase (batch 091, line 65) is not live. Batch 130 owns no caller (checked in grep G7).
# The fragment LIFECYCLE edges start at each fragment's own <init> (D21). androidx Fragment lifecycle is INFERRED (library source not read).
# UNREACHABLE: the entries with no_trigger_in_app have no call site in the app source (grep G1, G2). ActivityUtils.restoreOrientation is branch_never_taken (its guard is always false).
# The sup pair cuts the auto edge from CurrencyListActivity.onCreate into the UNREACHABLE restoreOrientation (D14). It does not cut forceCurrentOrientation, which is REACHABLE.
# Evidence labels: SRC = printed line of the source tree; INFERRED = a step whose source was not read.

# ---- tutorial fragments: LIFECYCLE from each fragment's own <init> (D21)

e('TutorialSyncFragment.<init>', 'TutorialSyncFragment.onCreate', 'LIFECYCLE',
  'the FragmentManager adds the fragment to the tutorial pager and calls onCreate after the constructor',
  evidence='SRC tutorial/TutorialSyncFragment.java:49-51 (constructor), 53-60 (onCreate); SRC tutorial/TutorialPagerAdapter.java:52-54 (newInstance for page 4; batch 135, interim D8); INFERRED androidx Fragment lifecycle (library source not read)')

e('TutorialSyncFragment.<init>', 'TutorialSyncFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after the constructor; it inflates fragment_tutorial_sync',
  evidence='SRC tutorial/TutorialSyncFragment.java:49-51 (constructor), 62-68 (onCreateView, inflate at 66); INFERRED androidx Fragment lifecycle (library source not read)')

e('TutorialTransactionsFragment.<init>', 'TutorialTransactionsFragment.onCreate', 'LIFECYCLE',
  'the FragmentManager adds the fragment to the tutorial pager and calls onCreate after the constructor',
  evidence='SRC tutorial/TutorialTransactionsFragment.java:50-52 (constructor), 54-61 (onCreate); SRC tutorial/TutorialPagerAdapter.java:43-45 (newInstance for page 1; batch 135, interim D8); INFERRED androidx Fragment lifecycle (library source not read)')

e('TutorialTransactionsFragment.<init>', 'TutorialTransactionsFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after the constructor; it inflates fragment_tutorial_transactions',
  evidence='SRC tutorial/TutorialTransactionsFragment.java:50-52 (constructor), 63-68 (onCreateView, inflate at 67); INFERRED androidx Fragment lifecycle (library source not read)')

# ---- UNREACHABLE (rows in graphs/MMEX/parts/label_136.md)

UNREACHABLE['ActivityUtils.<init>'] = ('no_trigger_in_app',
  'no code constructs ActivityUtils: the class is used only through its static methods',
  'SRC utils/ActivityUtils.java:27; SRC currency/list/CurrencyListActivity.java:56, 58 (static calls only); grep G1 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['ActivityUtils.restoreOrientation'] = ('branch_never_taken',
  'the only caller (CurrencyListActivity.onCreate) calls it only under mPreviousOrientation != Constants.NOT_SET; the fragment is created fresh at line 50 and the field starts at NOT_SET, so the guard is never true',
  'SRC currency/list/CurrencyListActivity.java:50, 55, 58; SRC currency/list/CurrencyListFragment.java:76, 250; SRC Constants.java:22; SRC utils/ActivityUtils.java:60-65', 'SOURCE')

UNREACHABLE['AlertDialogWrapper.setIcon'] = ('no_trigger_in_app',
  'its only caller EditPriceDialog.onCreateDialog is UNREACHABLE (batch 085): the app never constructs EditPriceDialog',
  'SRC investment/EditPriceDialog.java:114-116; label_085.md row EditPriceDialog.onCreateDialog', 'SOURCE')

UNREACHABLE['AlertDialogWrapper.setMessage'] = ('no_trigger_in_app',
  'no call site: neither AlertDialogWrapper caller (EditPriceDialog, TipsDialogFragment) calls setMessage',
  'SRC utils/AlertDialogWrapper.java:57-60; SRC investment/EditPriceDialog.java:114-116; SRC fragment/TipsDialogFragment.java:115-129; grep G2 and auto_calls (no record)', 'SOURCE')

UNREACHABLE['AlertDialogWrapper.setNegativeButton'] = ('no_trigger_in_app',
  'its only caller EditPriceDialog.onCreateDialog is UNREACHABLE (batch 085)',
  'SRC utils/AlertDialogWrapper.java:62-65; SRC investment/EditPriceDialog.java:143; label_085.md row EditPriceDialog.onCreateDialog', 'SOURCE')

UNREACHABLE['AlertDialogWrapper.setPositiveButton'] = ('no_trigger_in_app',
  'its only caller EditPriceDialog.onCreateDialog is UNREACHABLE (batch 085)',
  'SRC utils/AlertDialogWrapper.java:72-75; SRC investment/EditPriceDialog.java:126; label_085.md row EditPriceDialog.onCreateDialog', 'SOURCE')

UNREACHABLE['AlertDialogWrapper.setTitle(int)'] = ('no_trigger_in_app',
  'no call site: both callers pass a CharSequence (EditPriceDialog.java:115, TipsDialogFragment.java:116), so the int overload is never selected',
  'SRC utils/AlertDialogWrapper.java:42-45; SRC investment/EditPriceDialog.java:115; SRC fragment/TipsDialogFragment.java:116; auto_calls setTitle(CharSequence) records', 'SOURCE')

UNREACHABLE['DialogUtils.<init>'] = ('no_trigger_in_app',
  'no code constructs DialogUtils: the class is used only through its static method closeProgressDialog',
  'SRC utils/DialogUtils.java:29; SRC sync/SyncServiceMessageHandler.java:127; SRC currency/CurrencyUIFeatures.java:244; grep G1 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['DialogUtils.closeProgressBar'] = ('no_trigger_in_app',
  'no call site: the only mention in the app source is the definition (grep G2)',
  'SRC utils/DialogUtils.java:39-45; grep G2 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['DrawableUtils.<init>'] = ('no_trigger_in_app',
  'no code constructs DrawableUtils; both methods are static',
  'SRC utils/DrawableUtils.java:26; grep G1 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['DrawableUtils.scaleImage(Context,Drawable,float)'] = ('no_trigger_in_app',
  'no call site in the app source (grep G2 finds only the definitions; auto_calls has no record)',
  'SRC utils/DrawableUtils.java:44-61; grep G2 and G5 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['DrawableUtils.scaleImage(Context,Drawable,int,int)'] = ('no_trigger_in_app',
  'no call site in the app source (grep G2 finds only the definitions; auto_calls has no record)',
  'SRC utils/DrawableUtils.java:28-42; grep G2 and G5 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['MathUtils.<init>'] = ('no_trigger_in_app',
  'no code constructs MathUtils; its only method is static',
  'SRC utils/MathUtils.java:26; grep G1 in label_136.grep.txt', 'SOURCE')

UNREACHABLE['MathUtils.Round'] = ('no_trigger_in_app',
  'no call site in the app source: the text "Round(" appears only in the definition (grep G2)',
  'SRC utils/MathUtils.java:28-30; grep G2 and G5 in label_136.grep.txt', 'SOURCE')

# ---- sup: cut the auto edge from a REACHABLE caller into an UNREACHABLE method (D14)
# forceCurrentOrientation is not cut: it is REACHABLE through CurrencyListFragment.java:250.

sup(('CurrencyListActivity.onCreate', 'ActivityUtils.restoreOrientation'))  # auto_calls.json, CurrencyListActivity.java:58; the guard at line 55 is never true (see UNREACHABLE)

# ---- part 138 (2026-10-29)
# ================================================================== batch 138 (label_138): com.money.manager.ex.utils.MmxDate (methods 1-40 of 56 in this class; 40 methods)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_138.md (34 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_138.grep.txt.
# This file writes 0 e() edges, 0 gui() edges, 6 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). The six UNREACHABLE methods have no auto CALL records into them.
# getHour and getMinute keep their outgoing auto CALL records (to getHourOfDay and getMinuteOfHour, REACHABLE, owned by no other batch), so no sup pair is written (D14(a), D18, D20).
# Routes through batch 139 (MmxDate.setTimeToBeginningOfDay, MmxDate.java:317-318) are interim (D8): setHour (row 40) uses that hop.
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1; INFERRED = a step whose source was not read.

UNREACHABLE['MmxDate.<init>(Calendar)'] = (
  'no_trigger_in_app',
  'Constructor taking a Calendar. zero auto CALL records target it (auto_calls.json has no dst MmxDate.<init>(Calendar)). None of the 106 source "new MmxDate(" sites passes a Calendar: the single-argument sites pass Date, String or long values, and the Calendar-typed locals in the six files that also build an MmxDate (IncomeVsExpensesListFragment.java:489-493, InvestmentTransactionEditActivity.java:348-349, MmxDateTimeUtils.java:151-152) are not passed to a constructor.',
  'label_138.grep.txt S1 (106 hits of new MmxDate( in the source root), S2 continued ("MmxDate.<init>(Calendar) incoming 0"), S2b, S2c; MmxDate.java:94-96',
  'SOURCE')

UNREACHABLE['MmxDate.getCalendar'] = (
  'no_trigger_in_app',
  'Accessor returning the internal Calendar. zero auto CALL records target it, and the source root has no ".getCalendar()" call (python3 -I grep, 0 hits). Nothing in the app reads the Calendar back out of an MmxDate.',
  'label_138.grep.txt S2 ("\\.getCalendar\\(\\)  hits: 0"), S2 continued ("MmxDate.getCalendar incoming 0"); MmxDate.java:167-169',
  'SOURCE')

UNREACHABLE['MmxDate.getHour'] = (
  'no_trigger_in_app',
  'Alias of getHourOfDay. zero auto CALL records target it, and the source root has no ".getHour()" call (python3 -I grep, 0 hits). Its outgoing edge to MmxDate.getHourOfDay (REACHABLE, MmxDate.java:180) is an auto record and is kept; no sup is written for it.',
  'label_138.grep.txt S2 ("\\.getHour\\(\\)  hits: 0"), S2 continued ("MmxDate.getHour incoming 0"); MmxDate.java:179-181',
  'SOURCE')

UNREACHABLE['MmxDate.getMinute'] = (
  'no_trigger_in_app',
  'Alias of getMinuteOfHour. zero auto CALL records target it, and the source root has no ".getMinute()" call (python3 -I grep, 0 hits). Its outgoing edge to MmxDate.getMinuteOfHour (REACHABLE, MmxDate.java:192) is an auto record and is kept; no sup is written for it.',
  'label_138.grep.txt S2 ("\\.getMinute\\(\\)  hits: 0"), S2 continued ("MmxDate.getMinute incoming 0"); MmxDate.java:191-193',
  'SOURCE')

UNREACHABLE['MmxDate.setCalendar'] = (
  'no_trigger_in_app',
  'Setter replacing the internal Calendar. zero auto CALL records target it, and the source root has no ".setCalendar(" call (python3 -I grep, 0 hits).',
  'label_138.grep.txt S2 ("\\.setCalendar\\(  hits: 0"), S2 continued ("MmxDate.setCalendar incoming 0"); MmxDate.java:267-270',
  'SOURCE')

UNREACHABLE['MmxDate.setDate'] = (
  'no_trigger_in_app',
  'Setter for day of month taking an int. zero auto CALL records target MmxDate.setDate(int). The 8 source ".setDate(" hits all call entity setters with a Date argument (MainActivity.java:1267 accountTrx.setDate(scheduledTrx.getPaymentDate()); EditTransactionCommonFunctions.java:484 and 1549-1552 with Date values; CheckingTransactionEditActivity.java:262, 286, 436, 576; SmsReceiverTransactions.java:236), so none binds to the int overload.',
  'label_138.grep.txt S2 ("\\.setDate\\(  hits: 8"), S2 continued ("MmxDate.setDate incoming 0"); MainActivity.java:1267; EditTransactionCommonFunctions.java:484, 1549-1552; MmxDate.java:272-275',
  'SOURCE')

# ---- part 139 (2026-10-29)
# ================================================================== batch 139 (label_139): com.money.manager.ex.utils.MmxDate (methods 41-56 of 56; 16 methods)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_139.md (13 REACHABLE, 3 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_139.grep.txt.
# This file writes 0 e() edges, 0 gui() edges, 3 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). Every route into this batch is a CALL record from auto_calls.json (USE_AUTO, D7), so none is written here.
# The routes start in other batches: the S_CATEGORIES_REPORT page (graph_def.py:9322), the S_INCOME_VS_EXPENSES listener (graph_def.py:9509, batch 105), the Morningstar Rx callbacks (batch 090), the DatabaseSettingsActivity and FileStorageHelper paths and the MainActivity lifecycle. Those routes are interim where another batch is unmerged (D8).
# The three UNREACHABLE methods have no caller record in auto_calls.json and no call site in the app tree (SOURCE).

UNREACHABLE['MmxDate.setTime'] = ('no_trigger_in_app',
  'No call site in the app folder. The only occurrence of setTime( is the declaration in MmxDate, and the setTime( calls in InvestmentTransactionEditActivity are on java.util.Calendar. auto_calls.json has no record whose dst is MmxDate.setTime, and no method reference or subclass reaches it.',
  'SRC utils/MmxDate.java:337-340 (declaration); investment/InvestmentTransactionEditActivity.java:348-349 (java.util.Calendar); label_139.grep.txt section A (setTime( grep) and section C (0 incoming records)',
  'SOURCE')

UNREACHABLE['MmxDate.setTimeToEndOfDay'] = ('no_trigger_in_app',
  'The name occurs only at its declaration in the app tree. No call site and no auto_calls.json record has this callee, so no caller can reach the method.',
  'SRC utils/MmxDate.java:326-335 (declaration); label_139.grep.txt section A (grep over the MMEX tree: declaration only) and section C (0 incoming records)',
  'SOURCE')

UNREACHABLE['MmxDate.toIsoDateShortTimeString'] = ('no_trigger_in_app',
  'The name occurs only at its declaration in the app source. The other hits in the MMEX tree are JaCoCo HTML coverage reports, which are not code. No call site and no auto_calls.json record has this callee.',
  'SRC utils/MmxDate.java:374-377 (declaration); label_139.grep.txt section A (grep: declaration in the app source and in JaCoCo HTML only) and section C (0 incoming records)',
  'SOURCE')

# ---- part 140 (2026-10-29)
# ================================================================== batch 140 (label_140): utils and view classes, 38 methods in 7 classes
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_140.md (31 REACHABLE, 7 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_140.grep.txt.
# This file writes 1 e() edge (CALL, non_standard: the Provider hop from a Lazy<MmxDateTimeUtils> read to MmxDateTimeUtils_Factory.get), 0 gui() edges, 7 UNREACHABLE entries and 2 sup pairs.
# Edges are written only for destinations owned by this batch (D1). Every other route is a CALL edge from auto_calls.json (USE_AUTO, D7) and is not written here.
# Dagger: MmxDateTimeUtils_Factory.get is the Provider behind the Lazy<MmxDateTimeUtils> fields (D16). It is REACHABLE because app code reads those Lazy fields from REACHABLE methods (precedent: batch 036 FormatUtilities_Factory.get, batch 047 CurrencyService_Factory.get). The generated classes are INFERRED (D5).
# D14a: the two DateDisplay constructors are UNREACHABLE, so their auto CALL records into DateDisplay.initialize are cut with sup.
# Not written: the TipsDialogFragment.onCreateDialog -> MmxFileUtils.getRawAsString record (TipsDialogFragment.java:100). Its source is a batch 074 method, not a batch 140 method, and getRawAsString stays REACHABLE through 13 other callers. See label_140.grep.txt Q5 and the report.
# Not written: the cuts of DaggerMmxComponent.injectEditPriceDialog into MmxDateTimeUtils_Factory.<clinit> and .create (AGENT_NOTES lines 345, 357). Their source is not a batch 140 method, and both destinations are REACHABLE.
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1; INFERRED = a step whose source was not read.

# ---- Dagger Provider get (Lazy<MmxDateTimeUtils> read in EditTransactionCommonFunctions.getUserDateFormat)

e('EditTransactionCommonFunctions.getUserDateFormat', 'MmxDateTimeUtils_Factory.get', 'CALL',
  'getUserDateFormat calls dateTimeUtilsLazy.get() (the Lazy<MmxDateTimeUtils> field); the Lazy is a DoubleCheck around the factory, which calls its provider get()',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:113 (@Inject Lazy<MmxDateTimeUtils> field), 1405 (dateTimeUtilsLazy.get().getUserDatePattern inside getUserDateFormat, auto record); auto_calls.json record DaggerMmxComponent.java:572 (injectEditTransactionCommonFunctions calls MmxDateTimeUtils_Factory.create; the generated source is not under final_java_only, grep Q4); INFERRED: generated DoubleCheck and Factory code not read (D5); label_140.grep.txt Q4',
  cls='non_standard',
  via='DoubleCheck around the generated Lazy<MmxDateTimeUtils> built by DaggerMmxComponent; its provider is the MmxDateTimeUtils_Factory instance')

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_140.grep.txt, sections Q1-Q3)

UNREACHABLE['MmxFileUtils.copy'] = ('no_trigger_in_app',
  'No caller. The public static method is never called in the app source: the name occurs only at its declaration (BudgetService.copy(int) is a different method). No auto record has it as dst',
  'SRC utils/MmxFileUtils.java:59; grep Q2 (copy( search over the source root); Q1 (0 incoming)',
  'SOURCE')

UNREACHABLE['MmxFileUtils.getContext'] = ('no_trigger_in_app',
  'No caller. The only MmxFileUtils instance is built at SelectDatabaseActivity.java:63 and only requestExternalStoragePermissions is called on it (line 64). No line calls getContext() on an MmxFileUtils receiver; requestPermission reads the field directly (MmxFileUtils.java:158). No auto record has it as dst',
  'SRC utils/MmxFileUtils.java:131; SRC home/SelectDatabaseActivity.java:63-64; grep Q2 (fileUtils and MmxFileUtils search); Q1 (0 incoming)',
  'SOURCE')

UNREACHABLE['NotificationUtils.<init>'] = ('no_trigger_in_app',
  'No caller. There is no new NotificationUtils in the source root (the only textual hit is a comment at SmsReceiverTransactions.java:1063), and the class has only static members, so the implicit constructor is never called. No auto record has it as dst',
  'SRC utils/NotificationUtils.java:35-90 (static members only); grep Q2 (new NotificationUtils search); Q1 (0 incoming)',
  'SOURCE')

UNREACHABLE['SpinnerHelper.<init>'] = ('no_trigger_in_app',
  'No caller. There is no new SpinnerHelper in the source root, and the class has only the static getPosition method, so the implicit constructor is never called. No auto record has it as dst',
  'SRC utils/SpinnerHelper.java:25-40 (static method only); grep Q2 (new SpinnerHelper search); Q1 (0 incoming)',
  'SOURCE')

UNREACHABLE['DateDisplay.<init>(Context)'] = ('no_trigger_in_app',
  'No caller. There is no new DateDisplay in the source root (the constructor lines are declarations). The only layout reference to the class is commented out (activity_price_edit.xml:144-149), and so is the @BindView field (EditPriceViewHolder.java:39). No layout names the class, so LayoutInflater.createView (FW-SRC LayoutInflater.java:592-615) never builds it',
  'SRC view/DateDisplay.java:32; SRC res/layout/activity_price_edit.xml:144-149 (commented); SRC investment/EditPriceViewHolder.java:39 (commented); FW-SRC core/java/android/view/LayoutInflater.java:592-615; grep Q2, Q3',
  'SOURCE')

UNREACHABLE['DateDisplay.<init>(Context,AttributeSet)'] = ('no_trigger_in_app',
  'No caller. Same as DateDisplay.<init>(Context): no new DateDisplay in the source root and no layout tag names the class (the commented XML at activity_price_edit.xml:144-149). The three-argument constructor at DateDisplay.java:38-42 is commented out',
  'SRC view/DateDisplay.java:44, 38-42 (commented); SRC res/layout/activity_price_edit.xml:144-149 (commented); FW-SRC core/java/android/view/LayoutInflater.java:592-615; grep Q2, Q3',
  'SOURCE')

UNREACHABLE['DateDisplay.initialize'] = ('no_trigger_in_app',
  'Its only callers are the two constructors (DateDisplay.java:35 and 52), and both are UNREACHABLE. R.layout.control_datedisplay (DateDisplay.java:61) is used nowhere else in the source root',
  'SRC view/DateDisplay.java:35, 52, 55-61; grep Q2, Q3; Q1 (2 incoming, both from the UNREACHABLE constructors)',
  'SOURCE')

# ---- sup pairs (D14a): auto CALL records whose caller is an UNREACHABLE batch 140 method and whose destination is batch 140 (DateDisplay.initialize)

sup(('DateDisplay.<init>(Context)', 'DateDisplay.initialize'))  # the constructor has no caller, so its call to initialize cannot run
sup(('DateDisplay.<init>(Context,AttributeSet)', 'DateDisplay.initialize'))  # same

# ---- part 141 (2026-10-29)
# ================================================================== batch 141 (label_141): com.money.manager.ex.view widgets, RobotoView statics and ScrollAwareFABBehavior (36 methods in 7 classes)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_141.md (21 REACHABLE, 15 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_141.grep.txt.
# This file writes 7 e() edges (FRAMEWORK), 0 gui() edges, 15 UNREACHABLE entries and 0 sup pairs.
# Edges are written only for destinations owned by this batch (D1). Auto-record routes (parseAttributes, the RobotoView static methods and RobotoView.<clinit>) are CALL edges from auto_calls.json (D7) and are not written here.
# The four 2-argument Roboto constructors are reached only through XML inflation (LayoutInflater calls them, FW-SRC LayoutInflater.java:90-91). Each has one FRAMEWORK edge from the method that calls setContentView or inflate for the layout that holds the tag.
# Routes through other batches are interim (D8): CalculatorActivity.onCreate (label_027), AccountEditActivity.onCreate (label_006), SearchParametersFragment.onCreateView (label_109), SplitCategoriesActivity.onCreate (label_133), MmexApplication.onCreate (label_002).
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1 (the only framework evidence used here); INFERRED = a step whose source was not read.

# ---- XML inflation of the two-argument constructors (D6 is not involved: these are FRAMEWORK edges)

e('CalculatorActivity.onCreate', 'RobotoButton.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'setContentView inflates activity_calculator.xml, and LayoutInflater builds each RobotoButton tag with the (Context, AttributeSet) constructor',
  evidence='SRC common/CalculatorActivity.java:115 (setContentView(R.layout.activity_calculator)); res/layout/activity_calculator.xml:86 (RobotoButton tag); FW-SRC core/java/android/view/LayoutInflater.java:90-91 (constructor signature), 615 (getConstructor), 647 (newInstance); INFERRED: the path from AppCompat setContentView to LayoutInflater is not in fw_src')

e('CalculatorActivity.onCreate', 'RobotoTextView.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'setContentView inflates activity_calculator.xml, and LayoutInflater builds each RobotoTextView tag with the (Context, AttributeSet) constructor',
  evidence='SRC common/CalculatorActivity.java:115; res/layout/activity_calculator.xml:37 (RobotoTextView tag); FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615, 647; INFERRED: the AppCompat setContentView path is not in fw_src')

e('AccountEditActivity.onCreate', 'RobotoEditText.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'setContentView inflates activity_account_edit.xml, and LayoutInflater builds each RobotoEditText tag with the (Context, AttributeSet) constructor',
  evidence='SRC account/AccountEditActivity.java:138 (setContentView(R.layout.activity_account_edit)); res/layout/activity_account_edit.xml:52 (RobotoEditText tag); FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615, 647; INFERRED: the AppCompat setContentView path is not in fw_src')

e('SearchParametersFragment.onCreateView', 'RobotoCheckBox.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'onCreateView inflates search_parameters_fragment.xml, and LayoutInflater builds each RobotoCheckBox tag with the (Context, AttributeSet) constructor',
  evidence='SRC search/SearchParametersFragment.java:136 (inflater.inflate(R.layout.search_parameters_fragment, container, false)); res/layout/search_parameters_fragment.xml:64 (RobotoCheckBox tag); FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615, 647')

# ---- ScrollAwareFABBehavior: the coordinator layout builds the behaviour from app:layout_behavior, then dispatches nested scroll to it (INFERRED androidx)

e('SplitCategoriesActivity.onCreate', 'ScrollAwareFABBehavior.<init>', 'FRAMEWORK',
  'setContentView inflates activity_split_categories.xml; the coordinator layout builds the FAB behaviour named in app:layout_behavior with (Context, AttributeSet)',
  evidence='SRC transactions/SplitCategoriesActivity.java:100 (setContentView(R.layout.activity_split_categories)); res/layout/activity_split_categories.xml:77 (app:layout_behavior="com.money.manager.ex.view.behaviors.ScrollAwareFABBehavior"); SRC view/behaviors/ScrollAwareFABBehavior.java:38 (constructor); INFERRED: androidx CoordinatorLayout.LayoutParams creates the behaviour by reflection, source not read',
  cls='non_standard',
  via='androidx CoordinatorLayout builds the behaviour named in app:layout_behavior by reflection (INFERRED, source not read)')

e('ScrollAwareFABBehavior.<init>', 'ScrollAwareFABBehavior.onStartNestedScroll', 'FRAMEWORK',
  'the coordinator calls onStartNestedScroll on the behaviour it built when a child starts a nested scroll (NestedScrollView or RecyclerView)',
  evidence='SRC view/behaviors/ScrollAwareFABBehavior.java:47-54 (returns true for SCROLL_AXIS_VERTICAL at line 51); res/layout/activity_split_categories.xml:40 (NestedScrollView), 58 (RecyclerView); INFERRED: androidx CoordinatorLayout nested-scroll dispatch, source not read')

e('ScrollAwareFABBehavior.onStartNestedScroll', 'ScrollAwareFABBehavior.onNestedScroll', 'FRAMEWORK',
  'the coordinator calls onNestedScroll after onStartNestedScroll returned true, with the scroll deltas (hide and show at lines 62-66)',
  evidence='SRC view/behaviors/ScrollAwareFABBehavior.java:51-53 (returns true), 57-67 (onNestedScroll); INFERRED: androidx CoordinatorLayout dispatch, source not read')

# ---- UNREACHABLE entries: (kind, reason, evidence, confirmed_by)

UNREACHABLE['GestureWebView.<init>'] = ('no_trigger_in_app',
    'no code constructs GestureWebView: grep over src/main finds the name only in GestureWebView.java (no layout tag, no new expression)',
    'SRC view/GestureWebView.java:30, 33-38; grep Q1 (incoming 0); grep Q2 (only GestureWebView.java names the class)',
    'SOURCE')

UNREACHABLE['GestureWebView.initializeGestureDetector'] = ('no_trigger_in_app',
    'its only caller is GestureWebView.<init> (auto record line 37), which is UNREACHABLE',
    'SRC view/GestureWebView.java:37, 48-62; grep Q1 (incoming 1, from GestureWebView.<init>)',
    'SOURCE')

UNREACHABLE['GestureWebView.onTouchEvent'] = ('no_trigger_in_app',
    'touch dispatch reaches it only on a live GestureWebView instance, and no instance is constructed',
    'SRC view/GestureWebView.java:44-46; grep Q1 (incoming 0)',
    'SOURCE')

UNREACHABLE['GestureWebView$1.<init>'] = ('no_trigger_in_app',
    'the only auto record comes from initializeGestureDetector (line 49), which is UNREACHABLE',
    'SRC view/GestureWebView.java:49; grep Q1 (incoming 1)',
    'SOURCE')

UNREACHABLE['GestureWebView$1.onDown'] = ('no_trigger_in_app',
    'called only by the GestureDetector that initializeGestureDetector builds, and that method has no live caller',
    'SRC view/GestureWebView.java:50-52; grep Q1 (incoming 0)',
    'SOURCE')

UNREACHABLE['GestureWebView$1.onLongPress'] = ('no_trigger_in_app',
    'same as onDown: only the unreachable GestureDetector calls it',
    'SRC view/GestureWebView.java:54-57; grep Q1 (incoming 0)',
    'SOURCE')

UNREACHABLE['RobotoButton.<init>(Context)'] = ('framework_never_calls',
    'no app code calls the one-argument constructor (no new RobotoButton, no subclass), and LayoutInflater uses only (Context, AttributeSet)',
    'SRC view/RobotoButton.java:36-38; grep Q1 (incoming 0); grep Q2; FW-SRC core/java/android/view/LayoutInflater.java:90-91, 615, 647',
    'SOURCE')

UNREACHABLE['RobotoButton.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
    'no app caller uses the three-argument constructor (no new RobotoButton with three arguments, no subclass), and LayoutInflater never uses this signature',
    'SRC view/RobotoButton.java:75-78 (super at 76); grep Q1 (incoming 0); grep Q2; FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoCheckBox.<init>(Context)'] = ('framework_never_calls',
    'no app caller uses the one-argument constructor (no new RobotoCheckBox, no subclass), and LayoutInflater uses only (Context, AttributeSet)',
    'SRC view/RobotoCheckBox.java:38-40; grep Q1 (incoming 0); grep Q2; FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoCheckBox.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
    'no app caller uses the three-argument constructor, and LayoutInflater never uses this signature',
    'SRC view/RobotoCheckBox.java:77-80 (super at 78); grep Q1 (incoming 0); FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoEditText.<init>(Context)'] = ('framework_never_calls',
    'no app caller uses the one-argument constructor (no new RobotoEditText, no subclass), and LayoutInflater uses only (Context, AttributeSet)',
    'SRC view/RobotoEditText.java:34-36 (super at 35); grep Q1 (incoming 0); grep Q2; FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoEditText.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
    'no app caller uses the three-argument constructor, and LayoutInflater never uses this signature',
    'SRC view/RobotoEditText.java:71-74 (super at 72); grep Q1 (incoming 0); FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoTextView.<init>(Context)'] = ('framework_never_calls',
    'the only app construction (DashboardFragment.java:435) passes two arguments, and LayoutInflater uses only (Context, AttributeSet)',
    'SRC view/RobotoTextView.java:34-36 (super at 35); SRC DashboardFragment.java:435; grep Q1 (incoming 0); FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoTextView.<init>(Context,AttributeSet,int)'] = ('framework_never_calls',
    'no app caller uses the three-argument constructor, and LayoutInflater never uses this signature',
    'SRC view/RobotoTextView.java:73-76 (super at 74); grep Q1 (incoming 0); FW-SRC core/java/android/view/LayoutInflater.java:90-91',
    'SOURCE')

UNREACHABLE['RobotoView.<init>'] = ('no_trigger_in_app',
    'RobotoView declares only static members, no code writes new RobotoView, and no class extends it',
    'SRC view/RobotoView.java:37 (class declaration); grep Q1 (incoming 0); grep Q2 (no new RobotoView, no extends RobotoView)',
    'SOURCE')

# ---- sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch
sup(('GestureWebView.<init>', 'GestureWebView.initializeGestureDetector'))  # the constructor has no caller
sup(('GestureWebView.initializeGestureDetector', 'GestureWebView$1.<init>'))  # the builder has no live caller

# ---- part 142 (2026-10-29)
# ================================================================== batch 142 (label_142): com.money.manager.ex.view.recycler (ContextMenuRecyclerView, CursorRecyclerViewAdapter, DividerItemDecoration, RecyclerViewContextMenuInfo; 26 methods)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_142.md (0 REACHABLE, 26 UNREACHABLE, 0 INCOMPLETE).
# Grep, query and printed-line evidence: graphs/MMEX/parts/label_142.grep.txt (sections S1, S3, S4, S5, S6, S7).
# This file writes 0 e() edges, 0 gui() edges, 26 UNREACHABLE entries and 6 sup pairs.
# Edges are written only for destinations owned by this batch (D1). The batch has no REACHABLE route, so no e() edge is needed.
# The sup pairs cut the six auto CALL records from UNREACHABLE batch-142 callers into UNREACHABLE batch-142 targets (D14(a)). The two batch-050 records into DividerItemDecoration are already cut in graph_def.py:4057 and 4060 and are not repeated here.
# Library and framework dispatch (androidx RecyclerView.Adapter and ItemDecoration callbacks, android.database.DataSetObserver) was not read; no label relies on it, and each such row says so.
# Evidence labels: SRC = printed line of the source tree; FW-SRC = printed line of fw_src/android-8.1.0_r1; INFERRED = a step whose source was not read.

# ---- ContextMenuRecyclerView (never constructed: its only XML use is in a fragment that is never created)

UNREACHABLE['ContextMenuRecyclerView.<init>(Context)'] = (
  'no_trigger_in_app',
  'No new ContextMenuRecyclerView( in app/src. LayoutInflater looks up the (Context,AttributeSet) constructor for the XML tag, not this one. The tag is inflated only by CurrencyRecyclerListFragment.onCreateView, which never runs because the fragment is never created (CurrencyRecyclerListActivity is never started).',
  'label_142.grep.txt S1 (no new ContextMenuRecyclerView); S4 ContextMenuRecyclerView.java:44-46; S4 layout fragment_currency_recycler_list.xml:28; S4 CurrencyRecyclerListFragment.java:99; S4 CurrencyRecyclerListActivity.java:41; S4 AndroidManifest.xml:359 (no intent-filter); S4 MainActivity.java:644 (commented out); S3 FW-SRC LayoutInflater.java:90-91, 615',
  'SOURCE')

UNREACHABLE['ContextMenuRecyclerView.<init>(Context,AttributeSet)'] = (
  'no_trigger_in_app',
  'LayoutInflater calls this constructor for XML tag fragment_currency_recycler_list.xml:28. That XML is inflated only in CurrencyRecyclerListFragment.onCreateView (line 99), which never runs because the fragment is never created (the activity is never started).',
  'label_142.grep.txt S4 ContextMenuRecyclerView.java:40-42; S4 layout xml:28; S4 CurrencyRecyclerListFragment.java:99; S4 CurrencyRecyclerListActivity.java:41; S4 AndroidManifest.xml:359; S4 MainActivity.java:644; S3 FW-SRC LayoutInflater.java:90-91, 615',
  'SOURCE')

UNREACHABLE['ContextMenuRecyclerView.<init>(Context,AttributeSet,int)'] = (
  'no_trigger_in_app',
  'No caller at all. No new site in app/src, and LayoutInflater looks up only the (Context,AttributeSet) constructor. The class is only used from the XML tag, which is never inflated.',
  'label_142.grep.txt S1 (no new ContextMenuRecyclerView); S4 ContextMenuRecyclerView.java:36-38; S3 FW-SRC LayoutInflater.java:90-91, 615; activity and fragment chain as in the first entry',
  'SOURCE')

UNREACHABLE['ContextMenuRecyclerView.getContextMenuInfo'] = (
  'no_trigger_in_app',
  'Overrides View.getContextMenuInfo (FW-SRC View.java:12610), which View.createContextMenu calls at 12579. No ContextMenuRecyclerView instance exists (the fragment chain above), so no context menu is built on it.',
  'label_142.grep.txt S4 ContextMenuRecyclerView.java:48-50; S3 FW-SRC View.java:12578-12579, 12610; S4 CurrencyRecyclerListFragment.java:99; S4 CurrencyRecyclerListActivity.java:41',
  'SOURCE')

UNREACHABLE['ContextMenuRecyclerView.showContextMenuForChild'] = (
  'no_trigger_in_app',
  'Overrides ViewGroup.showContextMenuForChild(View) (FW-SRC ViewGroup.java:860, parent recursion at 866). No ContextMenuRecyclerView instance exists (the fragment chain above). Its auto CALL to RecyclerViewContextMenuInfo.<init> (line 58) is internal to batch 142 and is cut by a sup below.',
  'label_142.grep.txt S4 ContextMenuRecyclerView.java:53-61 (new RecyclerViewContextMenuInfo at 58); S3 FW-SRC ViewGroup.java:859-860, 866; S5 record ContextMenuRecyclerView.java:58 exact',
  'SOURCE')

# ---- CursorRecyclerViewAdapter (abstract; no subclass and no instance in app/src)

UNREACHABLE['CursorRecyclerViewAdapter.<init>'] = (
  'no_trigger_in_app',
  'The class is abstract, has no subclass, and has no new site in app/src. No file outside its own names the type or wildcard-imports the package, so no adapter instance is built. Its auto CALL to NotifyingDataSetObserver.<init> (line 40) is internal and cut by a sup below.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:27-28, 36-44; S1; S5 record CursorRecyclerViewAdapter.java:40 exact; S6 (package listing and no outside mention)',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.changeCursor'] = (
  'no_trigger_in_app',
  'Public method of an abstract class with no instance. The in-tree changeCursor calls are on other adapter types in other packages, which cannot be CursorRecyclerViewAdapter because no file outside its own names it. Its auto CALL to swapCursor (line 100) is internal and cut by a sup below.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:99-104; S5 record line 100 exact; S6 (changeCursor call sites and package check)',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.getContext'] = (
  'no_trigger_in_app',
  'No adapter instance exists (see CursorRecyclerViewAdapter.<init>). mContext is set only in onCreateViewHolder (line 79), which never runs.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:46-48, 79; S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.getCursor'] = (
  'no_trigger_in_app',
  'No adapter instance exists (see CursorRecyclerViewAdapter.<init>).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:50-52; S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.getItemCount'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.Adapter.getItemCount (androidx source not read; not relied on). No adapter instance exists (see CursorRecyclerViewAdapter.<init>).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:54-60; S5 framework_calls (Cursor.getCount); S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.getItemId'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.Adapter.getItemId (androidx source not read; not relied on). No adapter instance exists (see CursorRecyclerViewAdapter.<init>).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:62-68; S5 framework_calls (Cursor.moveToPosition, Cursor.getLong); S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.onBindViewHolder'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.Adapter.onBindViewHolder (androidx source not read; not relied on). No adapter instance exists (see CursorRecyclerViewAdapter.<init>). Its call at line 92 goes to the abstract onBindViewHolder(VH,Cursor), which has no code (line 75).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:75, 84-93; S5 framework_calls (Cursor.moveToPosition); S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.onCreateViewHolder'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.Adapter.onCreateViewHolder (androidx source not read; not relied on). No adapter instance exists (see CursorRecyclerViewAdapter.<init>). The body (lines 79-81) would only set mContext and return null.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:77-82; S5 framework_calls (ViewGroup.getContext); S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.setHasStableIds'] = (
  'no_trigger_in_app',
  'No adapter instance exists (see CursorRecyclerViewAdapter.<init>). The body ignores its argument and passes true to super (line 72).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:70-73; S5 framework_calls (RecyclerView$Adapter.setHasStableIds); S1; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter.swapCursor'] = (
  'no_trigger_in_app',
  'Called in-tree only from changeCursor (line 100), which is itself unreached. No adapter instance exists (see CursorRecyclerViewAdapter.<init>). The auto record from changeCursor is cut by a sup below.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:111-134 (registerDataSetObserver at 122; notifyDataSetChanged at 126 and 130); S5 record line 100 exact; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter$NotifyingDataSetObserver.<init>'] = (
  'no_trigger_in_app',
  'Implicit constructor of a private inner class (no declared constructor). Its only construction is in the outer constructor at line 40, which never runs (no adapter instance). Its auto CALL from line 40 is cut by a sup below.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:36-44 (new at 40), 136-137; S5 record line 40 exact; S6',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter$NotifyingDataSetObserver.onChanged'] = (
  'no_trigger_in_app',
  'No observer is ever registered. Observers are registered only at lines 42 and 122, on an adapter that is never built. Overrides android.database.DataSetObserver.onChanged, whose source is not in fw_src (source not read; not relied on).',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:139-144 (method at 140), 42, 122; S3 (DataSetObserver.java not present in fw_src); S5 framework_calls',
  'SOURCE')

UNREACHABLE['CursorRecyclerViewAdapter$NotifyingDataSetObserver.onInvalidated'] = (
  'no_trigger_in_app',
  'Same as onChanged: no observer is ever registered, because the adapter is never built. DataSetObserver source not read; not relied on.',
  'label_142.grep.txt S4 CursorRecyclerViewAdapter.java:146-152 (method at 147), 42, 122; S3; S5 framework_calls',
  'SOURCE')

# ---- DividerItemDecoration (constructed only in CurrencyRecyclerListFragment.java:366, which never runs)

UNREACHABLE['DividerItemDecoration.<clinit>'] = (
  'no_trigger_in_app',
  'The class is initialized on first active use (JVM class initialization). Its only use in app/src is new DividerItemDecoration at CurrencyRecyclerListFragment.java:366, in code that never runs. The batch 050 auto CALL from initializeList is cut in graph_def.py:4057.',
  'label_142.grep.txt S4 DividerItemDecoration.java:31-36; S4 CurrencyRecyclerListFragment.java:366; S1; S5 record (batch 050 caller, cut at graph_def.py:4057); S4 CurrencyRecyclerListActivity.java:41',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.<init>'] = (
  'no_trigger_in_app',
  'The only construction is CurrencyRecyclerListFragment.java:366, in unreached code. Its auto CALL to setOrientation (line 44) is cut by a sup below. The batch 050 CALL from initializeList is cut in graph_def.py:4060.',
  'label_142.grep.txt S4 DividerItemDecoration.java:40-45; S4 CurrencyRecyclerListFragment.java:366; S1; S5 records (line 44 and batch 050 caller); graph_def.py:4060',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.drawHorizontal'] = (
  'no_trigger_in_app',
  'Called in-app only from onDraw (line 57). onDraw has no instance behind it (see DividerItemDecoration.onDraw). The auto CALL from onDraw is cut by a sup below.',
  'label_142.grep.txt S4 DividerItemDecoration.java:53-59, 74-87; S5 record line 57 exact',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.drawVertical'] = (
  'no_trigger_in_app',
  'Called in-app only from onDraw (line 55). onDraw has no instance behind it (see DividerItemDecoration.onDraw). The auto CALL from onDraw is cut by a sup below.',
  'label_142.grep.txt S4 DividerItemDecoration.java:53-59, 60-73; S5 record line 55 exact',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.getItemOffsets'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.ItemDecoration.getItemOffsets (androidx source not read; not relied on). The only DividerItemDecoration instance would come from the unreached fragment code at CurrencyRecyclerListFragment.java:366.',
  'label_142.grep.txt S4 DividerItemDecoration.java:88-95 (@Override at 88, method 89-95); S4 CurrencyRecyclerListFragment.java:366; S5 framework_calls (Rect.set)',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.onDraw'] = (
  'no_trigger_in_app',
  'Overrides RecyclerView.ItemDecoration.onDraw (androidx source not read; not relied on). No instance exists (see DividerItemDecoration.<init>). Its auto CALLs to drawVertical (line 55) and drawHorizontal (line 57) are internal and cut by sups below.',
  'label_142.grep.txt S4 DividerItemDecoration.java:52-59; S5 records lines 55 and 57 exact',
  'SOURCE')

UNREACHABLE['DividerItemDecoration.setOrientation'] = (
  'no_trigger_in_app',
  'Called in-app only from the constructor (line 44), which is unreached (see DividerItemDecoration.<init>). The auto CALL from line 44 is cut by a sup below. The other setOrientation call in app/src is DateDisplay.java:56 on a LinearLayout, not this class.',
  'label_142.grep.txt S4 DividerItemDecoration.java:46-51, 44; S5 record line 44 exact; S7 (setOrientation call sites)',
  'SOURCE')

# ---- RecyclerViewContextMenuInfo (constructed only by ContextMenuRecyclerView.showContextMenuForChild, which has no instance)

UNREACHABLE['RecyclerViewContextMenuInfo.<init>'] = (
  'no_trigger_in_app',
  'The only construction is ContextMenuRecyclerView.java:58 (auto CALL, internal to batch 142, cut by a sup below). That method has no instance behind it (see ContextMenuRecyclerView.showContextMenuForChild). The casts at CurrencyRecyclerListFragment.java:150 and :163 do not construct the class.',
  'label_142.grep.txt S4 RecyclerViewContextMenuInfo.java:25-31; S4 ContextMenuRecyclerView.java:58; S1 (fragment lines 150 and 163 are casts); S5 record line 58 exact',
  'SOURCE')

# ================================================================== sup cuts (D14a): auto CALL records from UNREACHABLE batch-142 callers into UNREACHABLE batch-142 targets

sup(('ContextMenuRecyclerView.showContextMenuForChild', 'RecyclerViewContextMenuInfo.<init>'),
    ('CursorRecyclerViewAdapter.<init>', 'CursorRecyclerViewAdapter$NotifyingDataSetObserver.<init>'),
    ('CursorRecyclerViewAdapter.changeCursor', 'CursorRecyclerViewAdapter.swapCursor'),
    ('DividerItemDecoration.<init>', 'DividerItemDecoration.setOrientation'),
    ('DividerItemDecoration.onDraw', 'DividerItemDecoration.drawHorizontal'),
    ('DividerItemDecoration.onDraw', 'DividerItemDecoration.drawVertical'))

# ---- part 143 (2026-10-29)
# ================================================================== batch 143 (label_143): 31 methods in four classes
# com.money.manager.ex.viewmodels.AccountTransactionDisplay (19), IncomeVsExpenseReportEntity (8),
# com.money.manager.ex.widget.AccountBillsWidgetProvider (2), AccountBillsWidgetService (2).
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_143.md (26 REACHABLE, 5 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_143.grep.txt.
# This file writes 2 e() edges (ENTRY and LIFECYCLE for the widget receiver), 0 gui() edges,
# 5 UNREACHABLE entries (3 getters with no caller, 2 widget service methods the framework never runs) and 4 sup pairs (D14a).
# The 19 AccountTransactionDisplay methods and the 5 IncomeVsExpenseReportEntity methods that are REACHABLE get their
# routes from auto CALL records (auto_calls.json, D7). Those records have callers in batches 012, 104, 105, 110 and 112,
# which are not merged, so the routes are interim (D8).
# The two sup pairs for getExpenses/getIncome/getTransfers cut the auto CALL records to EntityBase.getMoney; those records
# have an UNREACHABLE caller, so they are cut here (the same pattern as label_052.py).

# ---- widget receiver (AccountBillsWidgetProvider): manifest ENTRY, then the framework path to onUpdate

e('S_ENTRY', 'AccountBillsWidgetProvider.<init>', 'ENTRY',
  'the framework creates the widget receiver by class name because the manifest declares it exported with the APPWIDGET_UPDATE intent-filter; the framework then calls onReceive on that receiver',
  evidence='SRC AndroidManifest.xml:89-99; FW-SRC core/java/android/app/ActivityThread.java:3141-3166 (handleReceiver: loadClass(component).newInstance() at 3166), 3187 (receiver.onReceive); the matching of the intent-filter to the broadcast is not in fw_src: INFERRED, source not read')

e('AccountBillsWidgetProvider.<init>', 'AccountBillsWidgetProvider.onUpdate', 'LIFECYCLE',
  'the framework calls onReceive on the receiver it has just created; AppWidgetProvider.onReceive calls this.onUpdate when the action is ACTION_APPWIDGET_UPDATE',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:57-68 (onReceive; this.onUpdate at 66); FW-SRC core/java/android/app/ActivityThread.java:3187; SRC widget/AccountBillsWidgetProvider.java:40-77 (the override)')

# ---- UNREACHABLE: income report getters with no caller (source root)

UNREACHABLE['IncomeVsExpenseReportEntity.getExpenses'] = ('no_trigger_in_app',
    'no caller: the only occurrence of getExpenses in the app source is its declaration (grep Q3); auto_calls.json has no CALL record with it as dst; the Expenses column is loaded by loadFromCursor (line 50) and never read through this getter',
    'IncomeVsExpenseReportEntity.java:66-68, 50; label_143.grep.txt Q1, Q3, Q4', 'SOURCE')

UNREACHABLE['IncomeVsExpenseReportEntity.getIncome'] = ('no_trigger_in_app',
    'no caller: the only occurrence of getIncome in the app source is its declaration (grep Q3; HomeFragment.java:252 is a comment and BehaviourSettings.getIncomeExpensePeriod is a different method); auto_calls.json has no CALL record with it as dst; the Income column is loaded at line 49 and never read through this getter',
    'IncomeVsExpenseReportEntity.java:62-64, 49; label_143.grep.txt Q1, Q3, Q4', 'SOURCE')

UNREACHABLE['IncomeVsExpenseReportEntity.getTransfers'] = ('no_trigger_in_app',
    'no caller: the only occurrence of getTransfers in the app source is its declaration (grep Q3); auto_calls.json has no CALL record with it as dst; the Transfers column is loaded at line 51 and never read through this getter',
    'IncomeVsExpenseReportEntity.java:70-72, 51; label_143.grep.txt Q1, Q3, Q4', 'SOURCE')

# ---- UNREACHABLE: widget service (framework never binds it, see label_052 for the same chain)

UNREACHABLE['AccountBillsWidgetService.<init>'] = ('framework_never_calls',
    'the framework creates the service only when it binds it, through RemoteViewsService.onBind (fw_src RemoteViewsService.java:235-243). The bind is refused: AppWidgetServiceImpl.enforceServiceExistsAndRequiresBindRemoteViewsPermission rejects a service that does not declare BIND_REMOTEVIEWS (fw_src AppWidgetServiceImpl.java:1251, 3598-3612), and the manifest declares BIND_JOB_SERVICE for this service (AndroidManifest.xml:401-403). RemoteViewsAdapter catches the SecurityException (fw_src RemoteViewsAdapter.java:178, 184-188). The app has no other route into the class (no intent-filter). The client-side AppWidgetManager.bindRemoteViewsService is not in fw_src: INFERRED.',
    'AccountBillsWidgetService.java:22-23; AndroidManifest.xml:401-403; fw_src RemoteViewsService.java:235-243; fw_src RemoteViewsAdapter.java:176-188; fw_src AppWidgetServiceImpl.java:1251, 3598-3612', 'INFERRED')

UNREACHABLE['AccountBillsWidgetService.onGetViewFactory'] = ('framework_never_calls',
    'the only caller is RemoteViewsService.onBind (fw_src RemoteViewsService.java:241), which runs only when the framework binds the service; the bind is refused (see AccountBillsWidgetService.<init>), so onGetViewFactory never runs and AllAccountBillsViewFactory is never created by this path',
    'AccountBillsWidgetService.java:25-28; fw_src RemoteViewsService.java:235-243; fw_src AppWidgetServiceImpl.java:1251, 3598-3612', 'INFERRED')

# auto CALL records whose caller is UNREACHABLE in this batch (auto_calls.json), cut by sup (D14a)
sup(('IncomeVsExpenseReportEntity.getExpenses', 'EntityBase.getMoney'))
sup(('IncomeVsExpenseReportEntity.getIncome', 'EntityBase.getMoney'))
sup(('IncomeVsExpenseReportEntity.getTransfers', 'EntityBase.getMoney'))
sup(('AccountBillsWidgetService.onGetViewFactory', 'AllAccountBillsViewFactory.<init>'))

# ---- part 145 (2026-10-29)
# ================================================================== batch 145 (label_145): Parceler wrapper Money$$Parcelable and its $1 creator (10 methods, 1 class)
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_145.md (4 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_145.grep.txt.
# This file writes 0 e() edges, 0 gui() edges, 6 UNREACHABLE entries and 4 sup pairs.
# No e() edge is written: every route into this batch is an auto CALL record in auto_calls.json (D7). The live routes come from SearchParameters$$Parcelable.write (line 66) and .read (line 124), owned by batch 108 (merged).
# Each Money$$Parcelable method is generated Parceler code, so each UNREACHABLE entry is confirmed_by INFERRED (D16) and rests on the grep and class-file output in label_145.grep.txt (D5).
# sup pairs (D14a): the auto CALL records from the two UNREACHABLE callers in this batch are cut. createFromParcel (row 9) has three records at line 27, and writeToParcel (row 7) has one at line 44. The targets stay reachable through the live SearchParameters routes.

# ---- UNREACHABLE entries: (kind, reason, evidence, confirmed_by)

UNREACHABLE['Money$$Parcelable.<init>'] = ('framework_never_calls',
    'the only caller is Money$$Parcelable$1.createFromParcel (auto record line 27); the framework calls that creator only for a parcel that names this class, and no Money$$Parcelable is ever written (no app Parcels.wrap takes a Money)',
    'grep A1 (wrap and unwrap arguments), A2 (no Money$$Parcelable in app source), C1, C3 (line 27); FW-SRC Parcel.java:2841-2851, 2867 (grep D1)',
    'INFERRED')

UNREACHABLE['Money$$Parcelable.describeContents'] = ('framework_never_calls',
    'the framework calls it only from Bundle.hasFileDescriptors, for a Parcelable value in a bundle; no Money$$Parcelable is put in a bundle (the only Parcelable put of a wrapped Money is the dead PriceDownloadedEventBundler.java:37 wrap of a PriceDownloadedEvent)',
    'grep B3 (putParcelable sites), A1, C3 (no auto record calls it); FW-SRC Bundle.java:316-332 (grep D1)',
    'INFERRED')

UNREACHABLE['Money$$Parcelable.getParcel'] = ('no_trigger_in_app',
    'the ParcelWrapper accessor that Parcels.unwrap calls on a wrapper object; no app Parcels.unwrap receives a Money wrapper, and no app code makes a Money$$Parcelable (library behaviour INFERRED)',
    'grep A1 (distinct argument list), A2, C2 (public 0x0001 with bridge 0x1041), C3 (no auto record calls it)',
    'INFERRED')

UNREACHABLE['Money$$Parcelable.writeToParcel'] = ('framework_never_calls',
    'Parcel.writeParcelable calls it only for a Money$$Parcelable instance, and none is created; its auto call to write (line 44) is cut by sup',
    'grep A1, A2, C1, C3 (line 44); FW-SRC Parcel.java:1785-1791 (grep D1)',
    'INFERRED')

UNREACHABLE['Money$$Parcelable$1.createFromParcel'] = ('framework_never_calls',
    'the framework calls it through Parcel.readParcelable (Parcel.java:2842, 2851) only for a parcel that names this class, and none is written (see Money$$Parcelable.<init>); its three auto calls (line 27) are cut by sup',
    'grep A1, A2, C2, C3 (line 27); FW-SRC Parcel.java:2841-2851, 2867 (grep D1)',
    'INFERRED')

UNREACHABLE['Money$$Parcelable$1.newArray'] = ('framework_never_calls',
    'the framework calls a Creator newArray only from Parcel.createTypedArray, and the app has no createTypedArray, readTypedArray or writeTypedArray call',
    'grep B1 (count 0), C2 (public 0x0001); FW-SRC Parcel.java:2640-2645 (grep D1)',
    'INFERRED')

# ---- sup pairs (D14a): auto CALL records from the UNREACHABLE callers in this batch

sup(('Money$$Parcelable$1.createFromParcel', 'Money$$Parcelable.<clinit>'))  # createFromParcel is UNREACHABLE (row 9), so its auto call at line 27 cannot run
sup(('Money$$Parcelable$1.createFromParcel', 'Money$$Parcelable.<init>'))  # same record family, line 27: <init> is UNREACHABLE (row 2)
sup(('Money$$Parcelable$1.createFromParcel', 'Money$$Parcelable.read'))  # same record family, line 27: read stays REACHABLE through SearchParameters$$Parcelable.read (line 124)
sup(('Money$$Parcelable.writeToParcel', 'Money$$Parcelable.write'))  # writeToParcel is UNREACHABLE (row 7), so its auto call at line 44 cannot run; write stays REACHABLE through SearchParameters$$Parcelable.write (line 66)

# ---- part 144 (2026-10-29)
# ================================================================== batch 144 (label_144): com.money.manager.ex.widget (40 methods in 5 classes)
# AllAccountBillsViewFactory (12), ButtonAddTransactionWidgetProvider (2), SingleAccountWidget (16),
# SingleAccountWidgetConfigureActivity incl. $1 (8), SummaryWidgetProvider (2).
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_144.md (27 REACHABLE, 13 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_144.grep.txt (sections S1-S19).
# This file writes 13 e() edges (ENTRY from S_ENTRY, LIFECYCLE from the receiver and activity <init>, FRAMEWORK for the configure listener), 0 gui() edges,
# 13 UNREACHABLE entries and 9 sup pairs (D14a).
# Key decision (orchestrator's question): AllAccountBillsViewFactory.onDataSetChanged is never called, so it is UNREACHABLE (case "never-called").
#   Its only construction is AccountBillsWidgetService.onGetViewFactory (AccountBillsWidgetService.java:27; grep S1), which batch 143 labels UNREACHABLE.
#   The framework binds the service only through RemoteViewsAdapter.bind (RemoteViewsAdapter.java:178), and AppWidgetServiceImpl refuses a service
#   that lacks BIND_REMOTEVIEWS (AppWidgetServiceImpl.java:1251, 3608-3611); the manifest gives BIND_JOB_SERVICE (AndroidManifest.xml:403).
#   The SecurityException is caught (RemoteViewsAdapter.java:184-186), so onGetViewFactory and onDataSetChanged never run.
#   The live case does not apply, so batch 052's label for QueryAccountBills.getFilterAccountSelection stays framework_never_calls and does not change.
# Configure activity: REACHABLE through the exported APPWIDGET_CONFIGURE intent-filter (ENTRY with env other_app, as PayeeActivity in label_004).
#   The provider names no android:configure (widget_info_single_account.xml:28 is commented out), which closes only the framework's own host start; loadAccounts stays UNREACHABLE.
# Cross-batch: the 12 sup pairs cut auto records whose destinations belong to other batches (CurrencyService.<init>, CurrencyService.getCurrencyFormatted,
#   Dataset.getUri, QueryAccountBills.<init>, Account.getName, AccountService.getAccountList(), AccountService.<init>). Those destinations keep any other route.
# The existing graph INTENT edges from SingleAccountWidget.initializeNewTransactionCommand (graph_def.py:12127) and ButtonAddTransactionWidgetProvider.onUpdate
#   (graph_def.py:12132) to CheckingTransactionEditActivity.<init> are not duplicated here (grep S17).

# ---- widget receivers (manifest ENTRY, then the framework path to each callback)

e('S_ENTRY', 'SummaryWidgetProvider.<init>', 'ENTRY',
  'the framework creates the widget receiver by class name because the manifest declares it exported with the APPWIDGET_UPDATE intent-filter; the framework then calls onReceive on it',
  evidence='SRC AndroidManifest.xml:78-88 (receiver name 79, APPWIDGET_UPDATE 82); SRC widget/SummaryWidgetProvider.java:35 (class declaration, implicit constructor); FW-SRC core/java/android/app/ActivityThread.java:3141, 3166 (handleReceiver loads the class by name and creates it), 3187 (receiver.onReceive)')

e('SummaryWidgetProvider.<init>', 'SummaryWidgetProvider.onUpdate', 'LIFECYCLE',
  'the framework calls onReceive on the receiver it has just created; AppWidgetProvider.onReceive calls this.onUpdate for ACTION_APPWIDGET_UPDATE',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:66 (onUpdate dispatch); FW-SRC services/appwidget/java/com/android/server/appwidget/AppWidgetServiceImpl.java:2283-2286 (sendUpdateIntentLocked, setComponent 2286); SRC widget/SummaryWidgetProvider.java:38-39 (override)')

e('S_ENTRY', 'ButtonAddTransactionWidgetProvider.<init>', 'ENTRY',
  'the framework creates the widget receiver by class name because the manifest declares it exported with the APPWIDGET_UPDATE intent-filter; the framework then calls onReceive on it',
  evidence='SRC AndroidManifest.xml:67-77 (receiver name 68, APPWIDGET_UPDATE 71); SRC widget/ButtonAddTransactionWidgetProvider.java:30 (class declaration, implicit constructor); FW-SRC core/java/android/app/ActivityThread.java:3141, 3166, 3187')

e('ButtonAddTransactionWidgetProvider.<init>', 'ButtonAddTransactionWidgetProvider.onUpdate', 'LIFECYCLE',
  'the framework calls onReceive on the receiver it has just created; AppWidgetProvider.onReceive calls this.onUpdate for ACTION_APPWIDGET_UPDATE',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:66; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2283-2286 (setComponent 2286); SRC widget/ButtonAddTransactionWidgetProvider.java:31-32 (override)')

e('S_ENTRY', 'SingleAccountWidget.<init>', 'ENTRY',
  'the framework creates the widget receiver by class name because the manifest declares it exported with the APPWIDGET_UPDATE intent-filter; the framework then calls onReceive on it',
  evidence='SRC AndroidManifest.xml:114-124 (receiver name 115, APPWIDGET_UPDATE 118); SRC widget/SingleAccountWidget.java:48 (class declaration, implicit constructor); FW-SRC core/java/android/app/ActivityThread.java:3141, 3166, 3187')

e('SingleAccountWidget.<init>', 'SingleAccountWidget.onUpdate', 'LIFECYCLE',
  'AppWidgetProvider.onReceive calls this.onUpdate for ACTION_APPWIDGET_UPDATE',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:66; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2283-2286 (setComponent 2286); SRC widget/SingleAccountWidget.java:69-70 (override)')

e('SingleAccountWidget.<init>', 'SingleAccountWidget.onDeleted', 'LIFECYCLE',
  'AppWidgetProvider.onReceive calls this.onDeleted for ACTION_APPWIDGET_DELETED; the framework sends it with setComponent to this provider, so the manifest filter (APPWIDGET_UPDATE only) does not gate it',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:73; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2290-2292 (sendDeletedIntentLocked, setComponent 2292); SRC widget/SingleAccountWidget.java:78-79 (override)')

e('SingleAccountWidget.<init>', 'SingleAccountWidget.onEnabled', 'LIFECYCLE',
  'AppWidgetProvider.onReceive calls this.onEnabled for ACTION_APPWIDGET_ENABLED; the framework sends it with setComponent when the first widget of this provider is added',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:85; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2277-2279 (sendEnableIntentLocked, setComponent 2279); SRC widget/SingleAccountWidget.java:87-88 (override)')

e('SingleAccountWidget.<init>', 'SingleAccountWidget.onDisabled', 'LIFECYCLE',
  'AppWidgetProvider.onReceive calls this.onDisabled for ACTION_APPWIDGET_DISABLED; the framework sends it with setComponent when the last widget of this provider is removed',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:87; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2297-2299 (sendDisabledIntentLocked, setComponent 2299); SRC widget/SingleAccountWidget.java:92-93 (override)')

e('SingleAccountWidget.<init>', 'SingleAccountWidget.onAppWidgetOptionsChanged', 'LIFECYCLE',
  'AppWidgetProvider.onReceive calls this.onAppWidgetOptionsChanged for ACTION_APPWIDGET_OPTIONS_CHANGED; the framework sends it with setComponent, so the manifest filter (APPWIDGET_UPDATE only) does not gate it',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:81 (dispatch); FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2303-2305 (sendOptionsChangedIntentLocked, setComponent 2305); SRC widget/SingleAccountWidget.java:97-98 (override)')

# ---- configure activity: exported with the APPWIDGET_CONFIGURE intent-filter, so another app can start it

e('S_ENTRY', 'SingleAccountWidgetConfigureActivity.<init>', 'ENTRY',
  'another app sends an APPWIDGET_CONFIGURE intent to the exported SingleAccountWidgetConfigureActivity',
  env=env_text('outside package: another app sends an APPWIDGET_CONFIGURE intent to SingleAccountWidgetConfigureActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:327-329 (exported=true; APPWIDGET_CONFIGURE intent-filter); SRC widget/SingleAccountWidgetConfigureActivity.java:50; FW-SRC core/java/android/app/ActivityThread.java:2665-2672')

e('SingleAccountWidgetConfigureActivity.<init>', 'SingleAccountWidgetConfigureActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC widget/SingleAccountWidgetConfigureActivity.java:54-55 (onCreate override)')

e('SingleAccountWidgetConfigureActivity.onCreate', 'SingleAccountWidgetConfigureActivity$1.onClick', 'FRAMEWORK',
  'onCreate sets the field listener on add_button (line 65); View.performClick calls it when the button is tapped',
  evidence='SRC widget/SingleAccountWidgetConfigureActivity.java:65 (setOnClickListener(mOnClickListener)), 86-87 (field and onClick); FW-SRC core/java/android/view/View.java:6294 (performClick)')

# ---- UNREACHABLE entries: (kind, reason, evidence, confirmed_by)

# AllAccountBillsViewFactory: the factory is built only by AccountBillsWidgetService.onGetViewFactory, which is UNREACHABLE (batch 143).

UNREACHABLE['AllAccountBillsViewFactory.<init>'] = ('framework_never_calls',
    'its only construction is AccountBillsWidgetService.onGetViewFactory (AccountBillsWidgetService.java:27), which is UNREACHABLE (batch 143): RemoteViewsService.onBind calls onGetViewFactory only after a bind that the framework refuses (see onDataSetChanged). No other new AllAccountBillsViewFactory exists in the app source (grep S1). Its auto CALL to CurrencyService.<init> (line 47) is cut by sup.',
    'AccountBillsWidgetService.java:26-27; AllAccountBillsViewFactory.java:43; grep S1, S2; FW-SRC core/java/android/widget/RemoteViewsService.java:241 (onGetViewFactory called from onBind)',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.getContext'] = ('no_trigger_in_app',
    'no code in the widget package calls getContext() (the only occurrence is the declaration), and the factory is never reached as an object (see <init>), so no caller can reach this getter.',
    'AllAccountBillsViewFactory.java:130; grep S7 (getContext() occurs only at line 130)',
    'SOURCE')

UNREACHABLE['AllAccountBillsViewFactory.getCount'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory that a bound RemoteViewsService creates, and that bind never happens (see onDataSetChanged). Its auto CALL to getCountInternal (line 53) is cut by sup.',
    'AllAccountBillsViewFactory.java:50-53; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8, S9',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.getCountInternal'] = ('no_trigger_in_app',
    'private; its only caller is getCount (line 53, the only call in the class, grep S7), which is UNREACHABLE (see getCount).',
    'AllAccountBillsViewFactory.java:53, 60; grep S7, S8',
    'SOURCE')

UNREACHABLE['AllAccountBillsViewFactory.getItemId'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged).',
    'AllAccountBillsViewFactory.java:68-69; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.getLoadingView'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged).',
    'AllAccountBillsViewFactory.java:73-74; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.getViewAt'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged). Its auto CALL to CurrencyService.getCurrencyFormatted (line 85) is cut by sup.',
    'AllAccountBillsViewFactory.java:78-79, 85; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8, S9',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.getViewTypeCount'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged).',
    'AllAccountBillsViewFactory.java:93-94; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.hasStableIds'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged).',
    'AllAccountBillsViewFactory.java:98-99; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.onCreate'] = ('framework_never_calls',
    'RemoteViewsFactory callback: RemoteViewsService.onBind calls factory.onCreate only after onGetViewFactory returns a factory (lines 241-243), and that path never runs (see onDataSetChanged). The body is empty.',
    'AllAccountBillsViewFactory.java:103-104; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8, S14',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.onDataSetChanged'] = ('framework_never_calls',
    'Never-called path (the case decided for this batch). The only factory instance is created in AccountBillsWidgetService.onGetViewFactory (AccountBillsWidgetService.java:27; grep S1). The framework calls onDataSetChanged only on an adapter bound through RemoteViewsAdapter.bind (RemoteViewsAdapter.java:178; the factory callback sites are 230 and 1156). The bind goes through AppWidgetServiceImpl, which requires the service to declare BIND_REMOTEVIEWS (enforce at AppWidgetServiceImpl.java:1251; check and throw at 3608-3611). AccountBillsWidgetService declares BIND_JOB_SERVICE (AndroidManifest.xml:403; grep S4), so the bind throws SecurityException, which RemoteViewsAdapter catches (lines 184-186). No bind happens, so onGetViewFactory, onCreate and onDataSetChanged never run. The sups cut its three auto CALLs: QueryAccountBills.getFilterAccountSelection (line 113, the batch 052 caller), Dataset.getUri (116) and QueryAccountBills.<init> (112).',
    'AllAccountBillsViewFactory.java:107-108, 112-116; AccountBillsWidgetService.java:26-27; AndroidManifest.xml:401-403; FW-SRC RemoteViewsAdapter.java:172-190 (bind 178, catch 184-186), 230, 1156; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:1209-1251 (enforce 1251), 3598-3611; grep S1, S4, S14, S14b',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.onDestroy'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged).',
    'AllAccountBillsViewFactory.java:123-124; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8',
    'INFERRED')

# SingleAccountWidgetConfigureActivity: only loadAccounts is UNREACHABLE; the rest of the class is REACHABLE through the ENTRY above.

UNREACHABLE['SingleAccountWidgetConfigureActivity.loadAccounts'] = ('no_trigger_in_app',
    'private; the only mention in the app source is the commented-out call at line 83 (todo), so it has no live caller. Its auto CALLs (lines 133, 134, 139) are cut by sup.',
    'SingleAccountWidgetConfigureActivity.java:131, 83; grep S6',
    'SOURCE')

# ---- sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('AllAccountBillsViewFactory.onDataSetChanged', 'QueryAccountBills.getFilterAccountSelection'))  # the orchestrator's sup (dead case)
sup(('AllAccountBillsViewFactory.onDataSetChanged', 'Dataset.getUri'))
sup(('AllAccountBillsViewFactory.onDataSetChanged', 'QueryAccountBills.<init>'))
sup(('AllAccountBillsViewFactory.<init>', 'CurrencyService.<init>'))
sup(('AllAccountBillsViewFactory.getCount', 'AllAccountBillsViewFactory.getCountInternal'))
sup(('AllAccountBillsViewFactory.getViewAt', 'CurrencyService.getCurrencyFormatted'))
sup(('SingleAccountWidgetConfigureActivity.loadAccounts', 'Account.getName'))
sup(('SingleAccountWidgetConfigureActivity.loadAccounts', 'AccountService.getAccountList()'))
sup(('SingleAccountWidgetConfigureActivity.loadAccounts', 'AccountService.<init>'))

# ---- part 146 (2026-10-29)
# ================================================================== part 146 (label_146): dispatch edges for four frontier methods
# Written by the orchestrator, not by a helper (2026-10-31). No methods are owned here: no UNREACHABLE entries, no sups.
# REGISTER edges are skipped by reachability (tools/build_graph.py bfs and cheapest), so each subscriber or callback that
# was reached only through a REGISTER edge needs a dispatch edge from the method that runs the call.

# ---- PasscodeActivity.onEvent(ErrorRaisedEvent): the Timber trees post the event (DebugTree.java:46, ScreenTree.java:27)

e('DebugTree.log', 'PasscodeActivity.onEvent', 'ASYNC',
  'a debug build logs an error through Timber while the passcode activity is registered: DebugTree posts ErrorRaisedEvent and EventBus calls onEvent',
  env=env_text('an error is logged through Timber while the passcode activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/DebugTree.java:45-46 (posts only when a subscriber exists); SRC MmexApplication.java:134-135 (DebugTree in the debug branch); SRC PasscodeActivity.java:202-215 (onStart registers; @Subscribe onEvent(ErrorRaisedEvent) at 214-215); INFERRED EventBus library source not read')

e('ScreenTree.log', 'PasscodeActivity.onEvent', 'ASYNC',
  'a release build logs an error through Timber while the passcode activity is registered: ScreenTree posts ErrorRaisedEvent and EventBus calls onEvent (the debug build plants DebugTree instead)',
  env=env_text('an error is logged through Timber while the passcode activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/ScreenTree.java:26-27; SRC MmexApplication.java:134-140 (ScreenTree in the release branch); SRC PasscodeActivity.java:202-215; INFERRED EventBus library source not read')

# ---- BudgetsActivity.onEvent(BudgetSelectedEvent): a budget row tap posts the event (BudgetListFragment.java:215)

e('BudgetListFragment.onListItemClick', 'BudgetsActivity.onEvent', 'ASYNC',
  'tapping a budget row posts BudgetSelectedEvent, and EventBus calls the @Subscribe method onEvent while the activity is registered',
  cls='non_standard', via='EventBus (greenrobot): post(BudgetSelectedEvent) at BudgetListFragment.java:215 to the @Subscribe method BudgetsActivity.onEvent (library dispatch, INFERRED)',
  evidence='SRC budget/BudgetListFragment.java:208-215 (onListItemClick posts at 215); SRC budget/BudgetsActivity.java:82-83 (@Subscribe onEvent(BudgetSelectedEvent)); INFERRED EventBus library source not read')

# ---- MmexApplication.lambda$onCreate$0: the Amplitude configuration block, called while the client is built

e('MmexApplication.onCreate', 'MmexApplication.lambda$onCreate$0', 'CALL',
  'onCreate calls the Amplitude factory with the configuration block, and the library calls the block while it builds the client',
  cls='non_standard', via='AmplitudeKt.Amplitude (com.amplitude.android) calls the Kotlin configuration block (library source not in the dataset, INFERRED)',
  evidence='SRC MmexApplication.java:147-154 (AmplitudeKt.Amplitude with the lambda); library com.amplitude.android is not in the dataset: its call of the block is INFERRED, source not read')

# ---- BehaviourSettingsFragment.lambda$showTimePicker$0: the TimePickerDialog OnTimeSetListener, called when the user sets the time

e('BehaviourSettingsFragment.showTimePicker', 'BehaviourSettingsFragment.lambda$showTimePicker$0', 'FRAMEWORK',
  'the framework TimePickerDialog calls the listener lambda when the user sets the time in the dialog that showTimePicker shows (line 114)',
  cls='non_standard', via='android.app.TimePickerDialog calls its OnTimeSetListener (framework source not in fw_src, INFERRED)',
  evidence='SRC settings/BehaviourSettingsFragment.java:101-106 (lambda and TimePickerDialog construction), 114 (show); the TimePickerDialog source is not in fw_src: INFERRED')

# ---- part 147 (2026-10-29)
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
