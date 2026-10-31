# batch 011 (label_011): com.money.manager.ex.account.AccountTransactionListFragment, methods 41-56 of 56 (16 methods); rows and printed lines: graphs/MMEX/parts/label_011.md
# Page S_ACCOUNT_TRANSACTIONS is defined in label_010.py and only reused here. CALL edges come from auto_calls.json, so no CALL edge is written here. Framework claims are INFERRED where the library source was not read; grep evidence is in label_011.grep.txt.

e('S_ACCOUNT_TRANSACTIONS', 'AccountTransactionListFragment$1.onClick', 'GUI',
  'tap the star icon in the account header: the account favourite flag is toggled and saved, and the star is redrawn (setImageViewFavorite)',
  gui=['Tap the star icon in the account header (account favourite)'],
  guard='an account is selected: the header row is hidden only when all accounts are selected (switchAccount, line 819)',
  evidence='SRC account/AccountTransactionListFragment.java:515-518, 519-531 (onClick), 819, 824 (headerRow); SRC res/layout/account_header_fragment.xml:52 (imageViewAccountFav)')

e('S_ACCOUNT_TRANSACTIONS', 'AccountTransactionListFragment$2.onClick', 'GUI',
  'tap the account icon in the account header: starts AccountEditActivity with ACTION_EDIT for this account (the Intent to that activity belongs to the activity batch and is not written here)',
  gui=['Tap the account icon in the account header (edit the account)'],
  guard='an account is selected: the header row is hidden only when all accounts are selected (switchAccount, line 819)',
  evidence='SRC account/AccountTransactionListFragment.java:536-544 (onClick 537-543; Intent 539-542); SRC res/layout/account_header_fragment.xml:43 (imageViewGotoAccount); SRC account/AccountTransactionListFragment.java:819, 824 (headerRow)')

e('S_ACCOUNT_TRANSACTIONS', 'AccountTransactionListFragment$3.onItemSelected', 'GUI',
  'choose an account in the account spinner of the action bar: the listener reads the chosen account and switches the list to it (switchAccount)',
  gui=['Choose an account in the account spinner in the action bar'],
  evidence='SRC account/AccountTransactionListFragment.java:454 (spinner found by R.id.spinner), 475-487 (initializeAccountsSelector: custom view R.layout.spinner at 481; loadAccountsInto at 487), 605-626 (listener set at 612; onItemSelected 614-626; switchAccount at 621)')

e('AccountTransactionListFragment.selectCurrentAccount', 'AccountTransactionListFragment$3.onNothingSelected', 'FRAMEWORK',
  'selectCurrentAccount sets the spinner selection to NOT_SET (-1) when the current account is not in the spinner list; the framework reports that selection change through onNothingSelected (the body at lines 629-631 is empty)',
  guard='the current account is missing from the spinner list, so position stays NOT_SET (lines 752-764)',
  evidence='SRC account/AccountTransactionListFragment.java:605-633 (onNothingSelected 628-631), 743-765 (setSelection at 764); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onNothingSelected for a negative position), 1103-1108 (change check); INFERRED selection reset on setAdapter (AbsSpinner is not in fw_src)')

UNREACHABLE['AccountTransactionListFragment.startCheckingAccountActivity()'] = (
  'branch_never_taken',
  'The only caller in the app is the switch case for R.id.menu_add_transaction_account in onOptionsItemSelected (lines 299-300). No menu the fragment shows can contain that item: the id is declared only in res/menu/menu_main.xml:35 and res/menu-v14/menu_main.xml:37, and no code or XML in final_java_only/MMEX refers to menu_main (label_011.grep.txt). The fragment inflates menu_period_picker_transactions, menu_transaction_status_selector and menu_transaction_filters (lines 237-244), and the all-data list adds its own menus, none of which declare the id. onPrepareOptionsMenu finds the item only to force it visible (lines 256-257), which does nothing when findItem returns null. So the case is never taken.',
  'account/AccountTransactionListFragment.java:237-244, 252-257, 286-300, 877-879; res/menu/menu_main.xml:35; res/menu-v14/menu_main.xml:37; graphs/MMEX/parts/label_011.grep.txt',
  'SOURCE')

UNREACHABLE['AccountTransactionListFragment.startCheckingAccountActivity(Integer)'] = (
  'no_trigger_in_app',
  'Its only caller is startCheckingAccountActivity() (line 878; auto_calls.json:44643-44650), and that method is itself UNREACHABLE (see the entry above). The grep over the source root finds no other caller of either overload (label_011.grep.txt).',
  'account/AccountTransactionListFragment.java:859-872, 877-879; auto_calls.json:44643-44650; graphs/MMEX/parts/label_011.grep.txt',
  'SOURCE')

sup(('AccountTransactionListFragment.onOptionsItemSelected', 'AccountTransactionListFragment.startCheckingAccountActivity()'))  # the switch case that calls it is never taken
sup(('AccountTransactionListFragment.startCheckingAccountActivity()', 'AccountTransactionListFragment.startCheckingAccountActivity(Integer)'))  # the caller cannot run
