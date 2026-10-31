# label_050.py: batch 050 (39 methods in 4 class groups): CurrencyListItemViewHolder (1), CurrencyRecyclerListActivity (3),
# CurrencyRecyclerListFragment (26) and CurrencyRecyclerListFragment$1 (2), CurrencySection (7).
# Result: 1 REACHABLE, 38 UNREACHABLE, 0 INCOMPLETE. Rows and printed lines: graphs/MMEX/parts/label_050.md.
# Grep evidence: graphs/MMEX/parts/label_050.grep.txt.
# Root cause of the 38 UNREACHABLE labels (no_trigger_in_app): CurrencyRecyclerListActivity has no start site.
#   AndroidManifest.xml:359 declares it with no intent-filter and no exported flag; the only Intent that names it (MainActivity.java:644) is commented out.
#   The fragment is created only by createInstance, called only from the activity's onCreate (line 41). Its listeners, EventBus
#   subscribers (registered in onStart, line 219) and CurrencySection (built in loadData) therefore never exist in a running app.
# REACHABLE: CurrencyListItemViewHolder.<init> is reached through CurrencyListAdapter.newView (currency/list/CurrencyListAdapter.java:51),
#   on the exported CurrencyListActivity route (MainActivity.java:643). It has no UNREACHABLE entry here.
#
# e() edges: none in this file. Every direct call from a batch 050 method is already an auto_calls record (D7). The calls that are
#   not auto records (library dispatch into CurrencySection overrides, RecyclerView dispatch into $1.onItemClick, EventBus delivery
#   to the subscribers) all start or end in an UNREACHABLE method here, so writing them would make an UNREACHABLE method reachable.
#
# sup cuts (D14a, 58 pairs): 57 auto records whose caller is a batch 050 method, plus 1 cha record whose callee is
#   CurrencyRecyclerListFragment$1.onItemClick (caller RecyclerItemClickListener.onInterceptTouchEvent, batch 051; written here because
#   the destination is owned by this batch, D1). The 9 auto records from the three fragment callers into batch 048 targets
#   (onOptionsItemSelected, onContextItemSelected, onEvent(PriceDownloadedEvent)) are already cut in graphs/MMEX/parts/label_048.py lines 79-87 and are not repeated.
#
# Orchestrator notes:
#   (a) Done. The three callers are UNREACHABLE (onOptionsItemSelected, onContextItemSelected, onEvent(PriceDownloadedEvent)), so the nine label_048 cuts stay.
#   (b) Not in this batch. CloudItemViewHolder$1.onClick is in batch 122 (batch_122.txt). Its ListItemClickedEvent.<init> edge is for batch 033 and 122.
#   (c) Not written. The EventBus edges from CurrencyUIFeatures$3.onClick and $7.onClick to onEvent(CurrencyDeletionConfirmedEvent)
#       and onEvent(ExchangeRateUpdateConfirmedEvent) would point into UNREACHABLE subscribers (the fragment never registers).
#       label_048.py header expects batch 050 to write them. Orchestrator decision needed.

# ================================================================== sup cuts (D14a)

sup(('CurrencyRecyclerListActivity.<init>', 'MmxBaseFragmentActivity.<init>'),
    ('CurrencyRecyclerListActivity.onCreate', 'CurrencyRecyclerListFragment.createInstance'),
    ('CurrencyRecyclerListActivity.onCreate', 'MmxBaseFragmentActivity.setContentView'),
    ('CurrencyRecyclerListActivity.onCreate', 'MmxBaseFragmentActivity.onCreate'),
    ('CurrencySection.getItemViewHolder', 'CurrencyListItemViewHolder.<init>'),
    ('CurrencySection.onBindItemViewHolder', 'Currency.getBaseConversionRate'),
    ('CurrencySection.onBindItemViewHolder', 'Currency.getName'),
    ('CurrencySection.onBindItemViewHolder', 'CurrencySection.getItemAtPosition'),
    ('CurrencySection.getHeaderViewHolder', 'CurrencyListItemViewHolder.<init>'),
    ('CurrencyRecyclerListFragment$1.onItemClick', 'ListItemClickedEvent.<init>'),
    ('CurrencyRecyclerListFragment$1.onItemClick', 'Currency.getName'),
    ('CurrencyRecyclerListFragment$1.onItemClick', 'Currency.getCurrencyId'),
    ('CurrencyRecyclerListFragment$1.onItemClick', 'CurrencyRecyclerListFragment.getCurrencyAtPosition'),
    ('CurrencyRecyclerListFragment.createInstance', 'CurrencyRecyclerListFragment.<init>'),
    ('CurrencyRecyclerListFragment.onCreate', 'CurrencyContentObserver.<init>'),
    ('CurrencyRecyclerListFragment.onViewCreated', 'CurrencyRecyclerListFragment.getRecyclerView'),
    ('CurrencyRecyclerListFragment.onActivityCreated', 'CurrencyRecyclerListFragment.initializeList'),
    ('CurrencyRecyclerListFragment.onActivityCreated', 'BehaviourSettings.getFilterInSelectors'),
    ('CurrencyRecyclerListFragment.onActivityCreated', 'AppSettings.getBehaviourSettings'),
    ('CurrencyRecyclerListFragment.onActivityCreated', 'AppSettings.<init>'),
    ('CurrencyRecyclerListFragment.onPause', 'Dataset.getUri'),
    ('CurrencyRecyclerListFragment.onPause', 'CurrencyRepository.<init>'),
    ('CurrencyRecyclerListFragment.onCreateContextMenu', 'Currency.getName'),
    ('CurrencyRecyclerListFragment.onCreateContextMenu', 'CurrencyRecyclerListFragment.getCurrencyAtPosition'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyService.isCurrencyUsed'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyService.<init>'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyService.updateExchangeRate'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyRecyclerListFragment.getService'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyService.getBaseCurrencyCode'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'Currency.getCode'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'Currency.getCurrencyId'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyRecyclerListFragment.getCurrencyAtPosition'),
    ('CurrencyRecyclerListFragment.onEvent(PriceDownloadedEvent)', 'UIHelper.showToast(String)'),
    ('CurrencyRecyclerListFragment.onEvent(PriceDownloadedEvent)', 'UIHelper.<init>'),
    ('CurrencyRecyclerListFragment.onEvent(AllPricesDownloadedEvent)', 'CurrencyRecyclerListFragment.getAdapter'),
    ('CurrencyRecyclerListFragment.onEvent(AllPricesDownloadedEvent)', 'CurrencyRecyclerListFragment.loadData'),
    ('CurrencyRecyclerListFragment.onEvent(ExchangeRateUpdateConfirmedEvent)', 'CurrencyService.updateExchangeRates'),
    ('CurrencyRecyclerListFragment.onEvent(ExchangeRateUpdateConfirmedEvent)', 'CurrencyRecyclerListFragment.getService'),
    ('CurrencyRecyclerListFragment.onEvent(ExchangeRateUpdateConfirmedEvent)', 'CurrencyService.getUnusedCurrencies'),
    ('CurrencyRecyclerListFragment.onEvent(ExchangeRateUpdateConfirmedEvent)', 'CurrencyService.getUsedCurrencies'),
    ('CurrencyRecyclerListFragment.onEvent(CurrencyDeletionConfirmedEvent)', 'CurrencyRecyclerListFragment.getAdapter'),
    ('CurrencyRecyclerListFragment.onEvent(CurrencyDeletionConfirmedEvent)', 'CurrencyRepository.delete'),
    ('CurrencyRecyclerListFragment.onEvent(CurrencyDeletionConfirmedEvent)', 'CurrencyRepository.<init>'),
    ('CurrencyRecyclerListFragment.getAdapter', 'CurrencyRecyclerListFragment.getRecyclerView'),
    ('CurrencyRecyclerListFragment.getCurrencyAtPosition', 'CurrencySection.getItemAtPosition'),
    ('CurrencyRecyclerListFragment.getCurrencyAtPosition', 'CurrencyRecyclerListFragment.getAdapter'),
    ('CurrencyRecyclerListFragment.getService', 'CurrencyService.<init>'),
    ('CurrencyRecyclerListFragment.initializeList', 'DividerItemDecoration.<clinit>'),
    ('CurrencyRecyclerListFragment.initializeList', 'RecyclerItemClickListener.<init>'),
    ('CurrencyRecyclerListFragment.initializeList', 'CurrencyRecyclerListFragment$1.<init>'),
    ('CurrencyRecyclerListFragment.initializeList', 'DividerItemDecoration.<init>'),
    ('CurrencyRecyclerListFragment.initializeList', 'CurrencyRecyclerListFragment.loadData'),
    ('CurrencyRecyclerListFragment.initializeList', 'CurrencyRecyclerListFragment.getRecyclerView'),
    ('CurrencyRecyclerListFragment.loadData', 'CurrencySection.<init>'),
    ('CurrencyRecyclerListFragment.loadData', 'CurrencyService.getUnusedCurrencies'),
    ('CurrencyRecyclerListFragment.loadData', 'CurrencyService.getUsedCurrencies'),
    ('CurrencyRecyclerListFragment.loadData', 'CurrencyService.<init>'),
    ('RecyclerItemClickListener.onInterceptTouchEvent', 'CurrencyRecyclerListFragment$1.onItemClick'))

# ================================================================== UNREACHABLE (batch 050)

UNREACHABLE['CurrencyRecyclerListActivity.<clinit>'] = ('no_trigger_in_app',
  'Static field FRAGMENTTAG is set when the class is first used. Nothing starts CurrencyRecyclerListActivity: the manifest entry has no intent-filter and no exported flag (AndroidManifest.xml:359), and the only Intent for it (MainActivity.java:644) is commented out. The currency menu starts CurrencyListActivity instead (MainActivity.java:643).',
  'SRC recycler/CurrencyRecyclerListActivity.java:30; AndroidManifest.xml:359; home/MainActivity.java:641-646; label_050.grep.txt section CurrencyRecyclerListActivity',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListActivity.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor of an activity with no start site (see CurrencyRecyclerListActivity.<clinit>). Its auto CALL to MmxBaseFragmentActivity.<init> is cut by sup above.',
  'SRC recycler/CurrencyRecyclerListActivity.java:27-28; AndroidManifest.xml:359; home/MainActivity.java:644',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListActivity.onCreate'] = ('no_trigger_in_app',
  'Lifecycle method of an activity that nothing starts (see CurrencyRecyclerListActivity.<clinit>). Its auto CALLs (createInstance, setContentView, MmxBaseFragmentActivity.onCreate) are cut by sup above.',
  'SRC recycler/CurrencyRecyclerListActivity.java:32-46; AndroidManifest.xml:359; home/MainActivity.java:643-644',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.<init>'] = ('no_trigger_in_app',
  'Implicit default constructor (the class declares none). The fragment is created only by createInstance (line 78), which is called only from CurrencyRecyclerListActivity.onCreate (line 41). That activity has no start site, so the fragment never exists in a running app.',
  'SRC recycler/CurrencyRecyclerListFragment.java:74-78; recycler/CurrencyRecyclerListActivity.java:41; label_050.grep.txt section CurrencyRecyclerListFragment',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.createInstance'] = ('no_trigger_in_app',
  'Its only caller is CurrencyRecyclerListActivity.onCreate (line 41), which is unreachable (no start site). Its auto CALL to the constructor is cut by sup above.',
  'SRC recycler/CurrencyRecyclerListFragment.java:77-83; recycler/CurrencyRecyclerListActivity.java:41; label_050.grep.txt section CurrencyRecyclerListFragment',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.getAdapter'] = ('no_trigger_in_app',
  'Private helper. Its callers are fragment methods that are unreachable (getCurrencyAtPosition, onEvent(AllPricesDownloadedEvent), onEvent(CurrencyDeletionConfirmedEvent)). Its auto CALLs are cut by sup above.',
  'SRC recycler/CurrencyRecyclerListFragment.java:325-327, 330-331',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.getCurrencyAtPosition'] = ('no_trigger_in_app',
  'Private helper. Its callers are the anonymous click listener $1.onItemClick (line 372), onCreateContextMenu and onContextItemSelected. All of them are in unreachable code, so the helper is never called.',
  'SRC recycler/CurrencyRecyclerListFragment.java:329-336, 372',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.getRecyclerView'] = ('no_trigger_in_app',
  'Private helper. Its callers are initializeList (line 352), onViewCreated, and getAdapter. All of them are in unreachable code.',
  'SRC recycler/CurrencyRecyclerListFragment.java:338-340, 352',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.getService'] = ('no_trigger_in_app',
  'Private lazy getter. Its callers are onContextItemSelected and onEvent(ExchangeRateUpdateConfirmedEvent). Both are unreachable, so the service is never created here.',
  'SRC recycler/CurrencyRecyclerListFragment.java:342-347',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.initializeList'] = ('no_trigger_in_app',
  'Called only from onActivityCreated, which is unreachable (the fragment is never created in-app). Its auto CALLs (RecyclerItemClickListener and $1 constructors, loadData, DividerItemDecoration, getRecyclerView) are cut by sup above.',
  'SRC recycler/CurrencyRecyclerListFragment.java:349-378 (anonymous listener 369-377); label_050.grep.txt section CurrencyRecyclerListFragment',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.loadData'] = ('no_trigger_in_app',
  'Called from initializeList (line 361) and from onEvent(AllPricesDownloadedEvent). Both are unreachable. It builds the two CurrencySection objects at lines 387 and 391, which are therefore never built in-app.',
  'SRC recycler/CurrencyRecyclerListFragment.java:380-393; 361; 387; 391',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onActivityCreated'] = ('no_trigger_in_app',
  'Fragment lifecycle callback (androidx dispatch INFERRED). It runs only for a fragment instance added by CurrencyRecyclerListActivity.onCreate (lines 41-44), and that activity has no start site.',
  'SRC recycler/CurrencyRecyclerListFragment.java:111-129; recycler/CurrencyRecyclerListActivity.java:41-44',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onContextItemSelected'] = ('no_trigger_in_app',
  'Context-menu callback (dispatch INFERRED) on a fragment that never exists in-app. Its auto CALLs into batch 048 (CurrencyUIFeatures.<init>, startCurrencyEditActivity, notifyCurrencyCanNotBeDeleted, showDialogDeleteCurrency) are cut in label_048.py lines 79-87; the rest are cut by sup above.',
  'SRC recycler/CurrencyRecyclerListFragment.java:161-211; graphs/MMEX/parts/label_048.py:79-87',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onCreate'] = ('no_trigger_in_app',
  'Fragment lifecycle callback on a fragment that is never created in-app (see CurrencyRecyclerListFragment.<init>). Its auto CALL to CurrencyContentObserver.<init> is cut by sup above.',
  'SRC recycler/CurrencyRecyclerListFragment.java:88-94; recycler/CurrencyRecyclerListActivity.java:41',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onCreateContextMenu'] = ('no_trigger_in_app',
  'Context-menu creation callback (dispatch INFERRED) on a fragment that is never created in-app. Its auto CALLs are cut by sup above.',
  'SRC recycler/CurrencyRecyclerListFragment.java:148-159',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onCreateOptionsMenu'] = ('no_trigger_in_app',
  'Options-menu callback (dispatch INFERRED) on a fragment that is never created in-app.',
  'SRC recycler/CurrencyRecyclerListFragment.java:293-299',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onCreateView'] = ('no_trigger_in_app',
  'Fragment view callback (dispatch INFERRED) on a fragment that is never created in-app.',
  'SRC recycler/CurrencyRecyclerListFragment.java:96-103',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onEvent(ListItemClickedEvent)'] = ('no_trigger_in_app',
  'EventBus subscriber. The fragment registers in onStart (line 219) only if it exists, and it never does in-app, so no post reaches this method. The post at line 375 sits in the unreachable click listener.',
  'SRC recycler/CurrencyRecyclerListFragment.java:265-270; 216-220 (register at 219); 369-377',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onEvent(CurrencyDeletionConfirmedEvent)'] = ('no_trigger_in_app',
  'EventBus subscriber on a fragment that is never registered in-app (onStart at line 219 never runs). The post from CurrencyUIFeatures$3.onClick (batch 048) cannot reach it. See orchestrator note (c) in the header.',
  'SRC recycler/CurrencyRecyclerListFragment.java:272-289; 216-220',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onEvent(ExchangeRateUpdateConfirmedEvent)'] = ('no_trigger_in_app',
  'EventBus subscriber on a fragment that is never registered in-app (onStart at line 219 never runs). The post from CurrencyUIFeatures$7.onClick (batch 048) cannot reach it. See orchestrator note (c) in the header.',
  'SRC recycler/CurrencyRecyclerListFragment.java:246-258; 216-220',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onEvent(AllPricesDownloadedEvent)'] = ('no_trigger_in_app',
  'EventBus subscriber on a fragment that is never registered in-app (onStart at line 219 never runs).',
  'SRC recycler/CurrencyRecyclerListFragment.java:239-244; 216-220',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onEvent(PriceDownloadedEvent)'] = ('no_trigger_in_app',
  'EventBus subscriber on a fragment that is never registered in-app (onStart at line 219 never runs). Its auto CALLs into batch 048 (CurrencyUIFeatures.<init>, onPriceDownloaded) are cut in label_048.py lines 79-87.',
  'SRC recycler/CurrencyRecyclerListFragment.java:229-237; 216-220; graphs/MMEX/parts/label_048.py:79-87',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onEvent(SubscriberExceptionEvent)'] = ('no_trigger_in_app',
  'EventBus subscriber on a fragment that is never registered in-app (onStart at line 219 never runs).',
  'SRC recycler/CurrencyRecyclerListFragment.java:260-263; 216-220',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onOptionsItemSelected'] = ('no_trigger_in_app',
  'Options-menu callback (dispatch INFERRED) on a fragment that is never created in-app. Line 311 calls showActiveInactiveSelectorForUpdate (batch 048); its auto CALLs into batch 048 are cut in label_048.py lines 79-81.',
  'SRC recycler/CurrencyRecyclerListFragment.java:301-315 (call at 311); graphs/MMEX/parts/label_048.py:79-81',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onPause'] = ('no_trigger_in_app',
  'Fragment lifecycle callback on a fragment that is never created in-app. Its auto CALLs (Dataset.getUri, CurrencyRepository.<init>) are cut by sup above.',
  'SRC recycler/CurrencyRecyclerListFragment.java:131-138',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onResume'] = ('no_trigger_in_app',
  'Fragment lifecycle callback on a fragment that is never created in-app.',
  'SRC recycler/CurrencyRecyclerListFragment.java:140-146',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onStart'] = ('no_trigger_in_app',
  'Registers the fragment with EventBus (line 219). It never runs because the fragment is never created in-app, so the six subscribers in this class are never registered.',
  'SRC recycler/CurrencyRecyclerListFragment.java:215-220; label_050.grep.txt section EventBus register',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onStop'] = ('no_trigger_in_app',
  'Unregisters the fragment from EventBus (line 226). It never runs because the fragment is never created in-app.',
  'SRC recycler/CurrencyRecyclerListFragment.java:222-227',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment.onViewCreated'] = ('no_trigger_in_app',
  'Fragment view callback on a fragment that is never created in-app. Its auto CALL to getRecyclerView is cut by sup above.',
  'SRC recycler/CurrencyRecyclerListFragment.java:105-109',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment$1.<init>'] = ('no_trigger_in_app',
  'Anonymous listener, created only in initializeList (line 369). initializeList is unreachable, so the listener is never installed. Its auto CALL is cut by sup above.',
  'SRC recycler/CurrencyRecyclerListFragment.java:369-377',
  'SOURCE')

UNREACHABLE['CurrencyRecyclerListFragment$1.onItemClick'] = ('no_trigger_in_app',
  'Click listener installed only by initializeList (line 369), which is unreachable. The only other incoming edge is RecyclerItemClickListener.onInterceptTouchEvent (batch 051, cha dispatch INFERRED, auto_calls record RecyclerItemClickListener.java:54), and that edge is cut here by sup above. Its auto CALLs are cut by sup above too.',
  'SRC recycler/CurrencyRecyclerListFragment.java:369-377; 370-376; auto_calls record RecyclerItemClickListener.onInterceptTouchEvent -> CurrencyRecyclerListFragment$1.onItemClick',
  'SOURCE')

UNREACHABLE['CurrencySection.<init>'] = ('no_trigger_in_app',
  'Constructed only in CurrencyRecyclerListFragment.loadData (lines 387 and 391), which is unreachable. Its auto CALLs are cut by sup above.',
  'SRC recycler/CurrencySection.java:38-51; recycler/CurrencyRecyclerListFragment.java:387, 391',
  'SOURCE')

UNREACHABLE['CurrencySection.getContentItemsTotal'] = ('no_trigger_in_app',
  'Section override called by the sectioned adapter (library dispatch INFERRED). The section is never constructed in-app, so the adapter never holds it.',
  'SRC recycler/CurrencySection.java:56-59; recycler/CurrencyRecyclerListFragment.java:387, 391',
  'SOURCE')

UNREACHABLE['CurrencySection.getHeaderViewHolder'] = ('no_trigger_in_app',
  'Section override (library dispatch INFERRED). The section is never constructed in-app. Its auto CALL to CurrencyListItemViewHolder.<init> (line 81) is cut by sup above; that holder class stays REACHABLE through CurrencyListAdapter.newView.',
  'SRC recycler/CurrencySection.java:79-82',
  'SOURCE')

UNREACHABLE['CurrencySection.getItemAtPosition'] = ('no_trigger_in_app',
  'Called from onBindItemViewHolder (line 71) and from CurrencyRecyclerListFragment.getCurrencyAtPosition. Both are unreachable, because the section is never constructed in-app.',
  'SRC recycler/CurrencySection.java:91-94; recycler/CurrencySection.java:71',
  'SOURCE')

UNREACHABLE['CurrencySection.getItemViewHolder'] = ('no_trigger_in_app',
  'Section override (library dispatch INFERRED). The section is never constructed in-app. Its auto CALL to CurrencyListItemViewHolder.<init> (line 63) is cut by sup above.',
  'SRC recycler/CurrencySection.java:61-64',
  'SOURCE')

UNREACHABLE['CurrencySection.onBindHeaderViewHolder'] = ('no_trigger_in_app',
  'Section override (library dispatch INFERRED). The section is never constructed in-app.',
  'SRC recycler/CurrencySection.java:84-89',
  'SOURCE')

UNREACHABLE['CurrencySection.onBindItemViewHolder'] = ('no_trigger_in_app',
  'Section override (library dispatch INFERRED). The section is never constructed in-app. Its auto CALLs (Currency.getName, Currency.getBaseConversionRate, CurrencySection.getItemAtPosition) are cut by sup above.',
  'SRC recycler/CurrencySection.java:66-77',
  'SOURCE')
