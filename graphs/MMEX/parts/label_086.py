# ================================================================== batch 086 (label_086): 40 methods of com.money.manager.ex.investment: ExchangeRateProviders (3: <clinit>, indexOf, names), InvestmentTransactionEditActivity (27), and its listeners $1-$4 (10: constructors, onItemSelected, onNothingSelected, onClick, lambda$onClick$0).
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_086.md (38 REACHABLE, 2 UNREACHABLE, 0 INCOMPLETE).
# This file writes 13 e() edges and 2 UNREACHABLE entries. It defines no SCREENS key: S_INVESTMENT_TRANSACTION_EDIT is defined by label_087.py:13 and reused here.
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here. The ButterKnife GUI edges into InvestmentTransactionEditActivity_ViewBinding$1-$4.doClick are owned by batch 087 (label_087.py:75-97).
# Framework claims cite FW-SRC lines printed for this batch; other claims are INFERRED where the source was not read.

# ---- entry edges into the activity: the intents from the two list screens, then the framework's lifecycle calls

e('PortfolioFragment.openEditInvestmentActivity', 'InvestmentTransactionEditActivity.<init>', 'INTENT',
  'the portfolio list opens the editor: a stock row tap passes the stock id, the add button passes none (openEditInvestmentActivity)',
  evidence='SRC investment/PortfolioFragment.java:198-204 (Intent at 199; setAction at 202; startActivity at 203); SRC investment/PortfolioFragment.java:124-127 (add button calls openEditInvestmentActivity(null) at 126); SRC investment/PortfolioFragment.java:147-150 (stock row calls it at 149)')

e('WatchlistItemsFragment.openEditInvestmentActivity', 'InvestmentTransactionEditActivity.<init>', 'INTENT',
  'the watchlist add button opens the editor for a new stock (openEditInvestmentActivity, started at 469); no other part names this method',
  evidence='SRC investment/watchlist/WatchlistItemsFragment.java:465-470 (Intent at 466; setAction at 468; startActivity at 469); SRC investment/watchlist/WatchlistItemsFragment.java:343-346 (onFloatingActionButtonClicked calls it at 345)')

e('InvestmentTransactionEditActivity.<init>', 'InvestmentTransactionEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1216; FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('InvestmentTransactionEditActivity.onCreate', 'S_INVESTMENT_TRANSACTION_EDIT', 'ENTERS',
  'the investment transaction edit screen is shown',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:88 (setContentView R.layout.activity_investment_transaction_edit)')

e('InvestmentTransactionEditActivity.onCreate', 'InvestmentTransactionEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:628-632 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu at 3388); INFERRED: the AppCompat delegate between the window and the activity is not read')

# ---- toolbar save and the back key: GUI edges from the page

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity.onOptionsItemSelected', 'GUI',
  'the save icon is tapped: onOptionsItemSelected runs onActionDoneClick (save branch)',
  gui=['Tap the save icon in the toolbar'],
  guard='item id is MenuHelper.save (InvestmentTransactionEditActivity.java:175)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:169-180 (save branch at 175-176; onActionDoneClick at 176; other items to super at 179); SRC core/MenuHelper.java:37 (save = 2), 87-89 (addSaveToolbarIcon adds the item at 88); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450); INFERRED: the toolbar tap reaching onMenuItemSelected through AppCompat is not read')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity.onBackPressed', 'GUI',
  'the back key is pressed: Activity.onKeyUp calls onBackPressed, which runs onActionCancelClick',
  gui=['Press the back key'],
  guard='targetSdkVersion >= ECLAIR (FW-SRC core/java/android/app/Activity.java:2977)',
  evidence='FW-SRC core/java/android/app/Activity.java:2975-2985 (onKeyUp calls onBackPressed at 2980); FW-SRC core/java/android/app/Activity.java:3001-3003 (onBackPressed); SRC investment/InvestmentTransactionEditActivity.java:182-185 (onBackPressed calls onActionCancelClick at 184); INFERRED: the AppCompat key dispatch to onKeyUp is not read')

# ---- account spinner, date text and the two day arrows (listeners set up in initAccountSelectors and initDateControl)

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity$1.onItemSelected', 'GUI',
  'an account is picked in the account spinner: the stock is held at that account and the form is marked dirty',
  gui=['Choose an account in the account spinner'],
  evidence='SRC investment/InvestmentTransactionEditActivity.java:322-339 (listener 322; onItemSelected 324-333: Account.from 327, setDirty 330, setHeldAt 331; setOnItemSelectedListener 339); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onItemSelected for a valid position at 944); FW-SRC core/java/android/widget/Spinner.java:1184-1186 (drop-down click calls setSelection); INFERRED: the AdapterView and AbsSpinner setSelection path is not read')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity$2.onClick', 'GUI',
  'the date text is tapped: the date picker dialog opens',
  gui=['Tap the date text (textViewDate)'],
  evidence='SRC investment/InvestmentTransactionEditActivity.java:345-369 (listener 345; onClick 347-368; DatePickerDialog built at 358-364; show at 367); SRC investment/InvestmentTransactionViewHolder.java:34 (dateView is textViewDate)')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity$3.onClick', 'GUI',
  'the previous-day arrow is tapped: setDate runs with the purchase date minus one day',
  gui=['Tap the previous-day arrow (previousDayButton)'],
  evidence='SRC investment/InvestmentTransactionEditActivity.java:376-382 (listener 376; minusDays(1) at 379; setDate at 380); SRC investment/InvestmentTransactionViewHolder.java:39 (previousDayButton); SRC res/layout/activity_investment_transaction_edit.xml:72 (previousDayButton)')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity$4.onClick', 'GUI',
  'the next-day arrow is tapped: setDate runs with the purchase date plus one day',
  gui=['Tap the next-day arrow (nextDayButton)'],
  evidence='SRC investment/InvestmentTransactionEditActivity.java:383-389 (listener 383; plusDays(1) at 386; setDate at 387); SRC investment/InvestmentTransactionViewHolder.java:40 (nextDayButton); SRC res/layout/activity_investment_transaction_edit.xml:92 (nextDayButton)')

e('InvestmentTransactionEditActivity$2.onClick', 'InvestmentTransactionEditActivity$2.lambda$onClick$0', 'FRAMEWORK',
  'the user taps OK in the date picker: DatePickerDialog calls the OnDateSetListener, which is this lambda, and the lambda runs setDirty',
  gui=['Tap the date text, then tap OK in the date picker'],
  evidence='SRC investment/InvestmentTransactionEditActivity.java:351-356 (lambda listener; setDirty at 352); SRC investment/InvestmentTransactionEditActivity.java:358-364 (DatePickerDialog built with the listener); FW-SRC core/java/android/app/DatePickerDialog.java:120-123 (BUTTON_POSITIVE set at 122), 164-174 (mDateSetListener.onDateSet at 171); INFERRED: the dialog button dispatch to DatePickerDialog.onClick is not read (AlertController not read)')

# ---- the calculator result returned to the editor

e('CalculatorActivity.returnResult', 'InvestmentTransactionEditActivity.onActivityResult', 'RESULT',
  'a calculator result is returned: returnResult sets RESULT_OK and finishes, and the framework delivers the result to the editor, whose onActivityResult stores the amount in the field that was tapped',
  evidence='SRC common/CalculatorActivity.java:435-445 (returnResult; setResult(RESULT_OK) at 443; finish at 444; called at 149 and 249); SRC investment/InvestmentTransactionEditActivity.java:119-158 (onActivityResult; Calculator.getAmountFromResult at 125; switch on the four request codes); FW-SRC core/java/android/app/ActivityThread.java:4253-4264 (deliverResults); FW-SRC core/java/android/app/Activity.java:7259-7266 (dispatchActivityResult)')

# ---- UNREACHABLE entries (each has a reason, evidence and basis; a method with no caller in the app)

UNREACHABLE['ExchangeRateProviders.indexOf'] = (
  'no_trigger_in_app',
  'indexOf has no caller in the app: its only occurrence in the source root is its own declaration, and no auto_calls.json record targets it. No other part of graph_def.py or parts/*.py mentions it.',
  'SRC investment/ExchangeRateProviders.java:43-51 (declaration); grep of the source root finds ExchangeRateProviders in four files and indexOf only at ExchangeRateProviders.java:43; no auto_calls.json record with dst ExchangeRateProviders.indexOf',
  'SOURCE')

UNREACHABLE['InvestmentTransactionEditActivity$1.onNothingSelected'] = (
  'branch_never_taken',
  'The framework calls onNothingSelected only for a negative selected position (fireOnSelected, AdapterView.java:946-947), and only when selectionChanged is reached from checkSelectionChanged (1103-1108). The editor never sets a negative selection: its only setSelection (InvestmentTransactionEditActivity.java:275) is guarded by accountIndex >= 0 (line 274). The account adapter is loaded once (line 314) before the listener is attached (line 339), and initAccountSelectors has one caller (line 294). AccountService.loadInvestmentAccountsToSpinner is not read, so whether it can empty a selected spinner is unverified.',
  'SRC investment/InvestmentTransactionEditActivity.java:273-275 (guarded setSelection), 308-316 (loader at 314), 322-339 (listener; onNothingSelected 336-337; attached at 339); FW-SRC core/java/android/widget/AdapterView.java:944-947, 1103-1108',
  'INFERRED')
