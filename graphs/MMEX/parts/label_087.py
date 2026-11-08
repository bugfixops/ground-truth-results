# ================================================================== batch 087 (label_087): 40 methods (graphs/MMEX/scratch/batches/batch_087.txt): InvestmentTransactionEditActivity_MembersInjector (4), InvestmentTransactionEditActivity_ViewBinding (11: its three methods and the listeners $1-$4 with their constructors and doClick), InvestmentTransactionViewHolder.<init>, PortfolioActivity (3), PortfolioCursorAdapter (3), PortfolioFragment (17: its 11 methods and the listeners $1 and $2), PortfolioItemDataViewHolder.<init>.
# Rows, printed lines and counts: graphs/MMEX/parts/label_087.md (33 REACHABLE, 7 UNREACHABLE, 0 INCOMPLETE).
# Grep and class-file evidence: graphs/MMEX/parts/label_087.grep.txt (sections 1-6).
# This file writes:
#   - 2 SCREENS keys (new; grep of graph_def.py and parts/*.py found no key for either screen): S_PORTFOLIO (the portfolio list; graph_def.py:3738 notes that the portfolio list has no key) and S_INVESTMENT_TRANSACTION_EDIT (the investment transaction edit screen). batch 086 owns the ENTERS edge into S_INVESTMENT_TRANSACTION_EDIT and must reuse this key (open point in label_087.md);
#   - 17 e() edges: 4 LIFECYCLE and 5 FRAMEWORK inside PortfolioFragment and its loader listener; 1 ENTERS from PortfolioFragment.onCreateView to S_PORTFOLIO; 2 GUI from S_PORTFOLIO (the row tap and the add button); 4 GUI from S_INVESTMENT_TRANSACTION_EDIT to the four ButterKnife listeners; 1 CALL (cls non_standard) from InvestmentTransactionEditActivity.onCreate to the ButterKnife binding constructor (ITEA.java:91, not in auto_calls.json);
#   - 7 sup pairs (D14a): the auto CALL records whose caller is UNREACHABLE in this batch (MembersInjector.create and injectMembers, and the five PortfolioActivity records);
#   - 7 UNREACHABLE entries: MembersInjector.<init>, create, injectMembers, ViewBinding.unbind (generated, INFERRED); PortfolioActivity.<clinit>, <init>, onCreate (app source, SOURCE).
# Not written: the INTENT edges into InvestmentTransactionEditActivity from PortfolioFragment.openEditInvestmentActivity (dst owned by batch 086, D1); the ENTERS edge from InvestmentTransactionEditActivity.onCreate (batch 086); the auto CALL records (D7); the FAB listener BaseListFragment$2 (batch 026).

SCREENS.update({'S_PORTFOLIO': 'The investment portfolio list (PortfolioFragment, shown in MainActivity by showPortfolioFragment in place of the home content): the stock rows of one investment account, the header row, and the add (floating action) button'})

SCREENS.update({'S_INVESTMENT_TRANSACTION_EDIT': 'The investment transaction edit screen (InvestmentTransactionEditActivity): the account, date, stock name, symbol and notes fields, and the number of shares, purchase price, commission and current price fields that open the calculator'})

# ---- PortfolioFragment lifecycle (androidx Fragment; library source not read: INFERRED)

e('PortfolioFragment.<init>', 'PortfolioFragment.onCreate', 'LIFECYCLE',
  'the fragment is created by newInstance (MainActivity.showPortfolioFragment, MainActivity.java:795) and the framework then calls onCreate (the inherited onAttach step is not in this batch)',
  evidence='SRC investment/PortfolioFragment.java:64, 76-86 (onCreate reads mAccountId from the arguments); SRC home/MainActivity.java:795-797; INFERRED androidx Fragment lifecycle (library source not read)')

e('PortfolioFragment.onCreate', 'PortfolioFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC investment/PortfolioFragment.java:89-95 (onCreateView inflates fragment_portfolio at 92); INFERRED androidx Fragment lifecycle (library source not read)')

e('PortfolioFragment.onCreateView', 'PortfolioFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after the view exists; onActivityCreated builds the adapter, the list and the loader',
  evidence='SRC investment/PortfolioFragment.java:98-122; INFERRED androidx Fragment lifecycle (library source not read)')

e('PortfolioFragment.onActivityCreated', 'PortfolioFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state (mAccountId) when it saves the instance state; the save is triggered by the framework (for example before the fragment stops), not by a fixed step after onActivityCreated, and the edge records the method as the next lifecycle method of this class in batch order (INFERRED)',
  evidence='SRC investment/PortfolioFragment.java:130-134; INFERRED androidx FragmentManager saves state through onSaveInstanceState (library source not read)')

# ---- PortfolioFragment loader callbacks (androidx LoaderManager; library not read: INFERRED). Same pattern as label_008 (AccountListFragment)

e('PortfolioFragment.initializeLoader', 'PortfolioFragment$2.onCreateLoader', 'FRAMEWORK',
  'initLoader starts the stock loader and the LoaderManager calls onCreateLoader (the loader query is built there, filtered on HELDAT = the account id)',
  evidence='SRC investment/PortfolioFragment.java:156-170 (initLoader at 158, onCreateLoader at 160); INFERRED androidx LoaderManager.initLoader calls the LoaderCallbacks (library not read)')

e('PortfolioFragment$2.onCreateLoader', 'PortfolioFragment$2.onLoadFinished', 'FRAMEWORK',
  'the loader (MmxCursorLoader) delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC investment/PortfolioFragment.java:160-172, 174; INFERRED androidx Loader delivers its result to the callbacks (library not read)')

e('PortfolioFragment$2.onLoadFinished', 'PortfolioFragment$2.onLoaderReset', 'FRAMEWORK',
  'a loader that has delivered data is reset and the LoaderManager calls onLoaderReset (the cursor is set to null)',
  evidence='SRC investment/PortfolioFragment.java:192-194; INFERRED androidx LoaderManager calls onLoaderReset when a loader with data is destroyed (library not read)')

# ---- the cursor adapter rows: changeCursor relays out the list and the framework calls getView, which calls newView (no scrap view) and bindView

e('PortfolioFragment$2.onLoadFinished', 'PortfolioCursorAdapter.newView', 'FRAMEWORK',
  'adapter.changeCursor(data) swaps in the cursor and notifies the list; on the relayout the framework calls getView, which calls newView for a row that has no scrap view (the first layout of the data)',
  evidence='SRC investment/PortfolioFragment.java:174-176 (changeCursor at 176); FW-SRC fw_src/android-8.1.0_r1/core/java/android/widget/CursorAdapter.java:348-353 (changeCursor calls swapCursor), 365-381 (swapCursor calls notifyDataSetChanged at 381), 276-289 (getView calls newView at 285 when convertView is null); androidx CursorAdapter not in the dataset: INFERRED to match this framework source (label_014.py evidence)')

e('PortfolioFragment$2.onLoadFinished', 'PortfolioCursorAdapter.bindView', 'FRAMEWORK',
  'the same relayout: the framework calls getView, which calls bindView for every visible row (the cursor columns are copied into the row views)',
  evidence='SRC investment/PortfolioFragment.java:174-176; SRC investment/PortfolioCursorAdapter.java:70 (bindView); FW-SRC fw_src/android-8.1.0_r1/core/java/android/widget/CursorAdapter.java:289 (getView calls bindView); INFERRED androidx CursorAdapter (library not read)')

# ---- the portfolio list page (new key S_PORTFOLIO, D9: a user-visible screen with its own list and button)

e('PortfolioFragment.onCreateView', 'S_PORTFOLIO', 'ENTERS',
  'the portfolio list is shown: onCreateView inflates the list (fragment_portfolio.xml, list at 52) and the add button (fab at 76); MainActivity.showPortfolioFragment puts the fragment in place of the home content',
  evidence='SRC investment/PortfolioFragment.java:89-95; SRC res/layout/fragment_portfolio.xml:52, 75-76; SRC home/MainActivity.java:791-797 (showPortfolioFragment calls showFragment at 797)')

e('S_PORTFOLIO', 'PortfolioFragment$1.onItemClick', 'GUI',
  'tap a stock row in the portfolio list: the header row is ignored; the stock row opens the edit screen for that stock (openEditInvestmentActivity)',
  gui=['Tap a stock row in the portfolio list (the header row is ignored)'],
  evidence='SRC investment/PortfolioFragment.java:140-149 (setOnItemClickListener at 140, onItemClick at 142, header skip at 144, openEditInvestmentActivity at 149); SRC res/layout/fragment_portfolio.xml:52 (android:id/list); auto_calls record PortfolioFragment$1.onItemClick -> PortfolioFragment.openEditInvestmentActivity (PortfolioFragment.java:149, via PortfolioFragment.access$000)')

e('S_PORTFOLIO', 'PortfolioFragment.onFloatingActionButtonClicked', 'GUI',
  'tap the add (floating action) button on the portfolio list: the edit screen opens with no stock (ACTION_INSERT, stock id null)',
  gui=['Tap the add (floating action) button (fab) on the portfolio list'],
  evidence='SRC investment/PortfolioFragment.java:125-126 (onFloatingActionButtonClicked calls openEditInvestmentActivity(null) at 126); SRC common/BaseListFragment.java:238-244 (the fab click listener calls onFloatingActionButtonClicked at 244); SRC res/layout/fragment_portfolio.xml:75-76 (fab)')

# ---- the investment transaction edit page (new key S_INVESTMENT_TRANSACTION_EDIT). Its ENTERS edge is owned by batch 086 (ITEA.onCreate)

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity_ViewBinding$1.doClick', 'GUI',
  'tap the number of shares field: the @OnClick listener of the generated binding calls onNumSharesClick, which opens the calculator for the shares',
  gui=['Tap the number of shares field (numSharesView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:211-212 (@OnClick at 211, method at 212); SRC res/layout/activity_investment_transaction_edit.xml:168 (numSharesView); auto_calls record InvestmentTransactionEditActivity_ViewBinding$1.doClick -> InvestmentTransactionEditActivity.onNumSharesClick (generated InvestmentTransactionEditActivity_ViewBinding.java:41); INFERRED ButterKnife listener')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity_ViewBinding$2.doClick', 'GUI',
  'tap the purchase price field: the @OnClick listener of the generated binding calls onPurchasePriceClick (returns early when no account is loaded), which opens the calculator for the purchase price',
  gui=['Tap the purchase price field (purchasePriceView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:221-223 (@OnClick at 221, method at 222, guard at 223); SRC res/layout/activity_investment_transaction_edit.xml:183 (purchasePriceView); auto_calls record InvestmentTransactionEditActivity_ViewBinding$2.doClick -> InvestmentTransactionEditActivity.onPurchasePriceClick (generated InvestmentTransactionEditActivity_ViewBinding.java:49); INFERRED ButterKnife listener')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity_ViewBinding$3.doClick', 'GUI',
  'tap the commission field: the @OnClick listener of the generated binding calls onCommissionClick, which opens the calculator for the commission',
  gui=['Tap the commission field (commissionView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:232-233 (@OnClick at 232, method at 233); SRC res/layout/activity_investment_transaction_edit.xml:217 (commissionView); auto_calls record InvestmentTransactionEditActivity_ViewBinding$3.doClick -> InvestmentTransactionEditActivity.onCommissionClick (generated InvestmentTransactionEditActivity_ViewBinding.java:57); INFERRED ButterKnife listener')

e('S_INVESTMENT_TRANSACTION_EDIT', 'InvestmentTransactionEditActivity_ViewBinding$4.doClick', 'GUI',
  'tap the current price field: the @OnClick listener of the generated binding calls onCurrentPriceClick, which opens the calculator for the current price',
  gui=['Tap the current price field (currentPriceView)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:240-241 (@OnClick at 240, method at 241); SRC res/layout/activity_investment_transaction_edit.xml:234 (currentPriceView); auto_calls record InvestmentTransactionEditActivity_ViewBinding$4.doClick -> InvestmentTransactionEditActivity.onCurrentPriceClick (generated InvestmentTransactionEditActivity_ViewBinding.java:65); INFERRED ButterKnife listener')

# ---- ButterKnife binding of the edit activity (CALL not in auto_calls.json: the call is made by reflection; INFERRED)

e('InvestmentTransactionEditActivity.onCreate', 'InvestmentTransactionEditActivity_ViewBinding.<init>(InvestmentTransactionEditActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for the activity, which binds the @OnClick handlers and the views (the two-argument constructor is an auto CALL record)',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated InvestmentTransactionEditActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC investment/InvestmentTransactionEditActivity.java:86-91 (onCreate; ButterKnife.bind(this) at 91; the return value is not kept); INFERRED ButterKnife generated binding (label_087.grep.txt sections 2, 3)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('InvestmentTransactionEditActivity_MembersInjector.create', 'InvestmentTransactionEditActivity_MembersInjector.<init>'),
    ('InvestmentTransactionEditActivity_MembersInjector.injectMembers', 'InvestmentTransactionEditActivity_MembersInjector.injectDateTimeUtilsLazy'),
    ('PortfolioActivity.<init>', 'MmxBaseFragmentActivity.<init>'),
    ('PortfolioActivity.onCreate', 'MmxBaseFragmentActivity.onCreate'),
    ('PortfolioActivity.onCreate', 'MmxBaseFragmentActivity.setContentView'),
    ('PortfolioActivity.onCreate', 'MmxBaseFragmentActivity.setDisplayHomeAsUpEnabled'),
    ('PortfolioActivity.onCreate', 'PortfolioFragment.newInstance'))

# ================================================================== UNREACHABLE (batch 087). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['InvestmentTransactionEditActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller record is create (auto_calls record InvestmentTransactionEditActivity_MembersInjector.java:25), and create has no caller: no class file refers to create or to this constructor (grep section 5), and DaggerMmxComponent refers only to the static injectDateTimeUtilsLazy. The app source has no reference to the class (section 1).',
  'python-printed auto_calls record InvestmentTransactionEditActivity_MembersInjector.java:25 (section 6); class-file parse (section 5); label_087.grep.txt section 1',
  'INFERRED')

UNREACHABLE['InvestmentTransactionEditActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated factory method (takes the Provider and returns a MembersInjector). No class file refers to create (section 5). The component calls the static injectDateTimeUtilsLazy directly (DaggerMmxComponent.java:396, section 6), not create. No app source reference (section 1).',
  'class-file parse (label_087.grep.txt section 5); python-printed auto_calls record DaggerMmxComponent.java:396 (section 6); label_087.grep.txt section 1',
  'INFERRED')

UNREACHABLE['InvestmentTransactionEditActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (takes the InvestmentTransactionEditActivity). No caller: no class file refers to it (section 5), and the component refers only to the static injectDateTimeUtilsLazy. Its only outgoing record, injectMembers -> injectDateTimeUtilsLazy (InvestmentTransactionEditActivity_MembersInjector.java:30), is cut by the sup pair above. The synthetic bridge injectMembers(Object) is not in this batch (open point in label_087.md).',
  'python-printed auto_calls record InvestmentTransactionEditActivity_MembersInjector.java:30 (section 6); class-file parse (section 5); label_087.grep.txt section 1',
  'INFERRED')

UNREACHABLE['InvestmentTransactionEditActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method. ButterKnife.bind(this) at InvestmentTransactionEditActivity.java:91 discards the returned Unbinder, the activity has no onDestroy and no unbind or Unbinder reference (section 2), and no class file refers to unbind (section 5). No auto_calls record has unbind as its destination (section 6).',
  'SRC investment/InvestmentTransactionEditActivity.java:86-91; label_087.grep.txt sections 1, 2, 5, 6',
  'INFERRED')

UNREACHABLE['PortfolioActivity.<clinit>'] = ('no_trigger_in_app',
  'Static initializer (FRAGMENT_TAG = PortfolioFragment.class.getSimpleName()). The class is never initialized: it has no start site. The manifest entry has no intent-filter (AndroidManifest.xml:352-354), no source file names PortfolioActivity except its own file, and no class file refers to it except its own (sections 1, 3, 4).',
  'SRC investment/PortfolioActivity.java:27-32 (class and FRAGMENT_TAG); AndroidManifest.xml:352-354; label_087.grep.txt sections 1, 3, 4',
  'SOURCE')

UNREACHABLE['PortfolioActivity.<init>'] = ('no_trigger_in_app',
  'Default constructor of an activity that has no start site (see PortfolioActivity.<clinit>). Its only outgoing record, the super call to MmxBaseFragmentActivity.<init> (PortfolioActivity.java:27), is cut by the sup pair above.',
  'SRC investment/PortfolioActivity.java:27; AndroidManifest.xml:352-354; label_087.grep.txt sections 1, 3, 4',
  'SOURCE')

UNREACHABLE['PortfolioActivity.onCreate'] = ('no_trigger_in_app',
  'Activity entry method of PortfolioActivity, which has no start site (see PortfolioActivity.<clinit>). Its outgoing records (PortfolioActivity.java:33, 35, 38, 49: the super call, setContentView, setDisplayHomeAsUpEnabled and PortfolioFragment.newInstance) are cut by the sup pairs above. The list reaches PortfolioFragment through MainActivity.showPortfolioFragment instead (MainActivity.java:795, outside this batch).',
  'SRC investment/PortfolioActivity.java:33-51; AndroidManifest.xml:352-354; label_087.grep.txt sections 1, 3, 4, 6',
  'SOURCE')
