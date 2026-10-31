# batch 026 (label_026): com.money.manager.ex.common.BaseListFragment (abstract; 27 methods, including its anonymous listeners $1 and $2), BaseRecyclerListFragment.<init>, and com.money.manager.ex.common.Calculator (8 methods). Rows and printed lines: graphs/MMEX/parts/label_026.md.
# BaseListFragment has 10 direct subclasses (grep, label_026.grep.txt section G): PortfolioFragment, WatchlistItemsFragment, AllDataListFragment, PayeeListFragment, AccountListFragment, CurrencyListFragment, BudgetListFragment, RecurringTransactionListFragment, BudgetDetailFragment, and BaseReportFragment (whose subclasses are PayeeReportFragment and CategoriesReportFragment).
# Pages (existing SCREENS keys only, D9): S_PAYEE (graph_def.py:104), S_ACCOUNT_LIST (graph_def.py:906), S_BUDGETS (graph_def.py:1577). The currency, recurring, portfolio, watchlist, all-data and report lists have no key, so no GUI edge is written for them.
# CALL edges come from auto_calls.json (super calls, calls inside BaseListFragment, and receiver-variant records such as BaseListFragment.onActivityCreated@PayeeListFragment), so none are written here. The edges that cannot run are cut with sup below.
# androidx Fragment, SearchView, the options-menu dispatch and the com.melnykov FloatingActionButton are not in fw_src: those claims are INFERRED (library source not read). grep evidence: graphs/MMEX/parts/label_026.grep.txt.

# ---- fragment lifecycle (androidx Fragment; library source not read: INFERRED)

e('AbsListFragment.onCreateView', 'BaseListFragment.onViewCreated', 'LIFECYCLE',
  'the framework calls onViewCreated after the view is created by the inherited onCreateView (AbsListFragment inflates abs_list_fragment.xml). Receivers that do not override onViewCreated run this body; BudgetListFragment overrides it and calls super (119-120); CurrencyListFragment (154-156) and BudgetDetailFragment (121-123) override it without calling super, so this body does not run for them',
  evidence='SRC core/AbsListFragment.java:77-79; SRC common/BaseListFragment.java:62-67; SRC currency/list/CurrencyListFragment.java:154-156; SRC budget/BudgetDetailFragment.java:121-123; INFERRED androidx Fragment lifecycle (library not read)')

e('PayeeListFragment.onActivityCreated', 'BaseListFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after onActivityCreated; PayeeListFragment does not override onStart, so the inherited body runs (the wildcard tips dialog)',
  evidence='SRC fragment/PayeeListFragment.java:81-119 (no onStart in the class); SRC common/BaseListFragment.java:92-110; INFERRED androidx Fragment lifecycle (library not read)')

e('AccountListFragment.onActivityCreated', 'BaseListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'AccountListFragment.onActivityCreated calls setHasOptionsMenu(true) (line 71) and does not override onCreateOptionsMenu, so the framework builds the menu with the inherited body (search item, lines 114-133). The other receivers with a menu reach the body through their super calls (PayeeListFragment 124-125, CurrencyListFragment 161-162, RecurringTransactionListFragment 134-135, AllDataListFragment 301-302, BaseReportFragment 102). BudgetListFragment never calls setHasOptionsMenu, and WatchlistItemsFragment has it commented out (line 107), so neither builds this menu',
  evidence='SRC account/AccountListFragment.java:64-71 (no onCreateOptionsMenu in the class); SRC common/BaseListFragment.java:113-149; INFERRED androidx FragmentManager dispatches onCreateOptionsMenu to fragments with an options menu (library not read)')

e('BudgetDetailFragment.onViewCreated', 'BaseListFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onViewCreated; BudgetDetailFragment does not override onActivityCreated, so the inherited body runs (subtitle from getSubTitle)',
  evidence='SRC budget/BudgetDetailFragment.java:121-123 (onViewCreated, no onActivityCreated in the class); SRC common/BaseListFragment.java:69-90; INFERRED androidx Fragment lifecycle (library not read)')

# ---- user actions on the list pages (GUI). The dispatch from the view, the SearchView or the activity is INFERRED (androidx, not in fw_src).

gui('S_PAYEE', 'BaseListFragment$1.onQueryTextChange', 'Type in the search box of the payee picker',
  evidence='SRC common/BaseListFragment.java:119-130 (SearchView and listener at 120-130); SRC fragment/PayeeListFragment.java:86 (search menu shown); INFERRED androidx SearchView calls the listener on each text change (not in fw_src)')

gui('S_PAYEE', 'BaseListFragment$1.onQueryTextSubmit', 'Submit the search text on the payee picker (search key)',
  evidence='SRC common/BaseListFragment.java:122-124; SRC fragment/PayeeListFragment.java:86; INFERRED androidx SearchView calls onQueryTextSubmit on submit (not in fw_src)')

gui('S_ACCOUNT_LIST', 'BaseListFragment$1.onQueryTextChange', 'Type in the search box of the account list',
  evidence='SRC common/BaseListFragment.java:119-130; SRC account/AccountListFragment.java:68 (search menu shown); INFERRED androidx SearchView calls the listener on each text change (not in fw_src)')

gui('S_ACCOUNT_LIST', 'BaseListFragment$1.onQueryTextSubmit', 'Submit the search text on the account list (search key)',
  evidence='SRC common/BaseListFragment.java:122-124; SRC account/AccountListFragment.java:68; INFERRED androidx SearchView calls onQueryTextSubmit on submit (not in fw_src)')

gui('S_PAYEE', 'BaseListFragment$2.onClick', 'Tap the + button on the payee picker',
  evidence='SRC common/BaseListFragment.java:238-248 (fab found by R.id.fab at 239, listener at 241-246); SRC fragment/PayeeListFragment.java:117-118 (fab shown and attached), 431 (override); INFERRED the view dispatches the click to the listener (View not read)')

gui('S_ACCOUNT_LIST', 'BaseListFragment.onOptionsItemSelected', 'Tap the Up arrow in the account list',
  evidence='SRC common/BaseListFragment.java:151-161 (home: setResultAndFinish unless hosted by MainActivity); SRC account/AccountListActivity.java:45 (Up enabled; the activity has no onOptionsItemSelected); INFERRED androidx dispatches the Home item to the fragment (library not read)')

# No Up-arrow edge for S_BUDGETS: BudgetListFragment never calls setHasOptionsMenu (grep), so the framework does not dispatch the Up item to its onOptionsItemSelected. BudgetsActivity.onOptionsItemSelected (66-77) handles only the settings id and then calls super, so the Up arrow stays with the activity. INFERRED (androidx, library not read).

# ---- auto edges that cannot run

# The FAB listener (line 244) is one object shared by every FAB screen, and its CALL edges fan out by class hierarchy to all eight overrides. S_PAYEE is the only screen in this part that reaches the listener, so its PayeeListFragment edge stays. Account, Budget and AllData have their own GUI edges (batches 008, 018, 020); the other four overrides get GUI edges from their owning batches. The base body is cut because the report fragments hide the FAB (abs_list_fragment.xml:82-91; grep section E).
sup(('BaseListFragment$2.onClick', 'BaseListFragment.onFloatingActionButtonClicked'),  # line 244
    ('BaseListFragment$2.onClick', 'WatchlistItemsFragment.onFloatingActionButtonClicked'),
    ('BaseListFragment$2.onClick', 'PortfolioFragment.onFloatingActionButtonClicked'),
    ('BaseListFragment$2.onClick', 'RecurringTransactionListFragment.onFloatingActionButtonClicked'),
    ('BaseListFragment$2.onClick', 'CurrencyListFragment.onFloatingActionButtonClicked'),
    ('BaseListFragment$2.onClick', 'AccountListFragment.onFloatingActionButtonClicked'),
    ('BaseListFragment$2.onClick', 'BudgetListFragment.onFloatingActionButtonClicked'),
    ('BaseListFragment$2.onClick', 'AllDataListFragment.onFloatingActionButtonClicked'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_026.grep.txt)

UNREACHABLE['BaseListFragment.onFloatingActionButtonClicked'] = (
  'no_trigger_in_app',
  'public method with an empty body (lines 216-217). Its only caller is the click listener BaseListFragment$2.onClick (line 244). The eight subclasses that show the FAB (PayeeListFragment, AccountListFragment, CurrencyListFragment, RecurringTransactionListFragment, BudgetListFragment, AllDataListFragment, PortfolioFragment, WatchlistItemsFragment) override it without calling super, so a tap runs the override. The subclasses that do not override it are the report fragments (BaseReportFragment, PayeeReportFragment, CategoriesReportFragment). They inherit the FAB from abs_list_fragment.xml, which is android:visibility="gone" (lines 82-91), and no report code calls setFloatingActionButtonVisible, getFloatingActionButton or setVisibility on R.id.fab (grep section E). A gone view receives no tap (framework behaviour, INFERRED). BudgetDetailFragment does not call setupFloatingActionButton (its onViewCreated at line 121 has no super), so it has no listener',
  'SRC common/BaseListFragment.java:216-217, 238-248; SRC common/BaseListFragment.java:244 (only caller); SRC res/layout/abs_list_fragment.xml:82-91; grep label_026.grep.txt sections C, D, E, G',
  'INFERRED')

UNREACHABLE['BaseListFragment.setSearchHint'] = (
  'no_trigger_in_app',
  'public setter with no caller in the app source (grep section A): BaseListFragment.setSearchHint (line 194) is never called. The getter getSearchHint (line 190) is called at line 141 and returns the default empty string (line 57), so the hint is never set',
  'SRC common/BaseListFragment.java:57, 190-196; grep label_026.grep.txt section A',
  'SOURCE')

UNREACHABLE['BaseRecyclerListFragment.<init>'] = (
  'no_trigger_in_app',
  'public class with an empty body and no extends clause (lines 23-24). No subclass (no extends in the app folder, grep section B) and no new BaseRecyclerListFragment anywhere in the app folder (section B), so its implicit constructor never runs',
  'SRC common/BaseRecyclerListFragment.java:23-24; grep label_026.grep.txt section B',
  'SOURCE')
