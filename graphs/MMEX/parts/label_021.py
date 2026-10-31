# batch 021 (label_021): com.money.manager.ex.common.AllDataListFragment, methods 41-63 of 63 (23 methods): onTransactionStatusClicked to updateFooter (15 methods), and AllDataListFragment$1 to $4 (8 methods: <init> and onClick each).
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_021.md.
# Page S_ACCOUNT_TRANSACTIONS is defined in label_010.py and only reused here. The search results screen (SearchActivity, batch 107) hosts the same fragment too; no page is defined for it here.
# CALL edges come from auto_calls.json, so none are written here. Framework claims (AlertDialog, AlertController, AdapterView, AbsListView) were read from fw_src (FW-SRC). grep evidence: graphs/MMEX/parts/label_021.grep.txt.

# ---- the row tap: AllDataListFragment$1 is the item click listener set in onActivityCreated (line 158)

gui('S_ACCOUNT_TRANSACTIONS', 'AllDataListFragment$1.onItemClick', 'Tap a transaction row when no selection is active',
    evidence='SRC common/AllDataListFragment.java:157-169; FW-SRC core/java/android/widget/AbsListView.java:1133 (the click is not dispatched while a selection is active), 1157-1158 (super.performItemClick); FW-SRC core/java/android/widget/AdapterView.java:314-318 (the listener is called)')

# ---- the delete confirmation (showDialogDeleteCheckingAccount, line 704): the dialog buttons reach the listeners

e('AllDataListFragment.showDialogDeleteCheckingAccount', 'AllDataListFragment$3.onClick', 'FRAMEWORK',
  'the OK button: setPositiveButton stores the listener (AlertDialog.java:611-613); the alert button handler calls onClick when OK is tapped (AlertController.java:163-166; setButton stores the message at 344-348)',
  guard='the user taps OK (android.R.string.ok) in the delete confirmation dialog (lines 713-770)',
  evidence='SRC common/AllDataListFragment.java:704-778 (positive listener 713-770, show 777); FW-SRC android/app/AlertDialog.java:611-613; FW-SRC com/android/internal/app/AlertController.java:163-166, 344-348')

e('AllDataListFragment.showDialogDeleteCheckingAccount', 'AllDataListFragment$2.onClick', 'FRAMEWORK',
  'the Cancel button: setNegativeButton stores the listener (AlertDialog.java:637-640); the same button handler calls onClick (AlertController.java:163-166)',
  guard='the user taps Cancel (android.R.string.cancel) in the delete confirmation dialog (lines 771-776)',
  evidence='SRC common/AllDataListFragment.java:771-776; FW-SRC android/app/AlertDialog.java:637-640; FW-SRC com/android/internal/app/AlertController.java:163-166')

# ---- the status list (changeTransactionStatus, line 859): the list rows reach the listener

e('AllDataListFragment.changeTransactionStatus', 'AllDataListFragment$4.onClick', 'FRAMEWORK',
  'a status row: setAdapter stores the listener (AlertDialog.java:764-768); a tap on a row of the list calls onClick with the row position (AlertController.java:1138-1142)',
  guard='the user taps one of the five status rows (none, reconciled, follow up, duplicate, void) in the Change status dialog (lines 865-884)',
  evidence='SRC common/AllDataListFragment.java:859-914 (rows 865-884; setAdapter 891; onClick 893-908); FW-SRC android/app/AlertDialog.java:764-768; FW-SRC com/android/internal/app/AlertController.java:1138-1142')

# ---- auto edges that cannot run

# the status case of the action mode (AllDataMultiChoiceModeListener.java:81-87) cannot run: the action-mode menu has no status item (grep label_021.grep.txt, sections B and C)
sup(('AllDataMultiChoiceModeListener.onActionItemClicked', 'AllDataListFragment.onTransactionStatusClicked'))

# the edge from the dead method to setStatusCheckingAccount (line 422) cannot run; setStatusCheckingAccount stays reachable through AllDataListFragment$4.onClick (line 902)
sup(('AllDataListFragment.onTransactionStatusClicked', 'AllDataListFragment.setStatusCheckingAccount'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_021.grep.txt)

UNREACHABLE['AllDataListFragment.onTransactionStatusClicked'] = (
  'branch_never_taken',
  'its only caller is the status case of AllDataMultiChoiceModeListener.onActionItemClicked (line 87, cha edge through IAllDataMultiChoiceModeListenerCallbacks). That case needs a status item in the action-mode menu. The menu inflated for the mode (menu_all_data_adapter, AllDataListFragment.java:393) has only duplicate, change status, delete and select all. The status ids (menu_none, menu_reconciled, menu_follow_up, menu_duplicate, menu_void) are in menu_transaction_status_selector (options menu, AccountTransactionListFragment.java:240) and in the dialog rows of changeTransactionStatus (not a menu). The listener is created only at AllDataListFragment.java:152 and the callbacks are implemented only by AllDataListFragment, so no other menu reaches the case. The case never runs.',
  'common/AllDataListFragment.java:386-394, 419-426, 859-884; common/AllDataMultiChoiceModeListener.java:60-93; res/menu/menu_all_data_adapter.xml:22-44; res/menu/menu_transaction_status_selector.xml:30-46; grep label_021.grep.txt sections A-C',
  'SOURCE')
