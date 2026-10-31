# batch 033 (label_033): WebViewActivity (+$1), AmountEnteredEvent, ListItemClickedEvent, AbsListFragment (+$1, $2), ContextMenuIds. Rows: graphs/MMEX/parts/label_033.md; grep: label_033.grep.txt.
# CALL edges come from auto_calls.json (none written here, except the sup cuts below). AmountEnteredEvent.<init> is reached through its auto CALL from AmountInputDialog$7.onClick (batch 024).

e('AccountListActivity.onCreate', 'AbsListFragment.onCreateView', 'FRAMEWORK',
  'the activity adds AccountListFragment in onCreate (fragment transaction, committed); the framework then creates the fragment view by calling onCreateView, which AccountListFragment inherits (no override: grep G11)',
  guard='no fragment with id R.id.content yet (AccountListActivity.java:54-55); a restored activity does not add it again',
  evidence='SRC account/AccountListActivity.java:47, 54-56; SRC core/AbsListFragment.java:77-80; SRC account/AccountListFragment.java (no onCreateView override; grep G11); INFERRED androidx FragmentManager calls onCreateView after the commit (library source not read)')

e('AbsListFragment.onViewCreated', 'AbsListFragment.onDestroyView', 'LIFECYCLE',
  'the framework calls onDestroyView when the fragment view is destroyed; the view exists only after onCreateView and onViewCreated have run (no onDestroyView override in AccountListFragment or BaseListFragment: grep G10)',
  guard='onViewCreated has run, so the view exists',
  evidence='SRC core/AbsListFragment.java:86-89, 95-102; SRC common/BaseListFragment.java:63-67 (super call at 66); INFERRED androidx Fragment calls onDestroyView when the view is destroyed (library source not read); pattern as graph_def.py:1299')

e('AbsListFragment.ensureList', 'AbsListFragment$2.run', 'FRAMEWORK',
  'ensureList posts mRequestFocus to the handler at its end (mHandler.post); the handler runs run() later on the main looper',
  evidence='SRC core/AbsListFragment.java:266-319 (ensureList; post at 318), 49-53 (run at 50-52); FW-SRC core/java/android/os/Handler.java:355-358 (post queues the runnable)')

gui('S_ACCOUNT_LIST', 'AbsListFragment$1.onItemClick', 'Tap a row of the account list; onListItemClick then opens the row context menu (AccountListFragment.java:256-259)',
  evidence='SRC core/AbsListFragment.java:41-46 (mOnClickListener; onItemClick calls onListItemClick at 44), 306 (setOnItemClickListener); FW-SRC core/java/android/widget/AdapterView.java:314-318 (performItemClick calls the listener at 318); FW-SRC core/java/android/widget/AbsListView.java:3122-3130 (performItemClick at 3127); INFERRED the touch-up path reaches performItemClick (source not read)')

# ---- auto CALL edges whose caller cannot run (UNREACHABLE in this batch): the exact edge is cut, so the targets have no live incoming edge

sup(('WebViewActivity.onCreate', 'WebViewActivity.handleIntent'))
sup(('WebViewActivity.onCreate', 'WebViewActivity.getProgressBar'))
sup(('WebViewActivity.updateProgress', 'WebViewActivity.getProgressBar'))
sup(('WebViewActivity.handleIntent', 'WebViewActivity.post'))
sup(('WebViewActivity.post', 'WebViewActivity.getWebView'))
sup(('WebViewActivity.getWebView', 'WebViewActivity$1.<init>'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_033.grep.txt)

UNREACHABLE['WebViewActivity.<init>'] = (
  'no_trigger_in_app',
  'implicit default constructor (WebViewActivity declares no constructor); the class is never instantiated because no start site names it: no startActivity, Intent or ComponentName refers to it, and its manifest entry has no intent-filter so no implicit intent resolves to it',
  'SRC common/WebViewActivity.java:42-43 (no declared constructor); SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2',
  'SOURCE')

UNREACHABLE['WebViewActivity.onCreate'] = (
  'no_trigger_in_app',
  'Activity lifecycle entry of WebViewActivity; the activity is never started (no start site, no intent-filter), so onCreate never runs',
  'SRC common/WebViewActivity.java:53-64; SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2',
  'SOURCE')

UNREACHABLE['WebViewActivity.onCreateOptionsMenu'] = (
  'no_trigger_in_app',
  'options-menu callback of WebViewActivity; the activity is never started (no start site, no intent-filter), so the menu is never created',
  'SRC common/WebViewActivity.java:66-71; SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2',
  'SOURCE')

UNREACHABLE['WebViewActivity.onOptionsItemSelected'] = (
  'no_trigger_in_app',
  'options-item callback of WebViewActivity; the activity is never started (no start site, no intent-filter), so no menu item is ever selected here',
  'SRC common/WebViewActivity.java:73-86; SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2',
  'SOURCE')

UNREACHABLE['WebViewActivity.updateProgress'] = (
  'no_trigger_in_app',
  'public progress setter called only by MyWebChromeClient.onProgressChanged (MyWebChromeClient.java:40), and MyWebChromeClient is created only in WebViewActivity.getWebView (WebViewActivity.java:131); the activity is never started',
  'SRC common/WebViewActivity.java:88-90; SRC core/MyWebChromeClient.java:29, 35-40; SRC common/WebViewActivity.java:131; grep label_033.grep.txt G1, G2, G12',
  'SOURCE')

UNREACHABLE['WebViewActivity.getProgressBar'] = (
  'no_trigger_in_app',
  'private helper called from onCreate (line 61) and from updateProgress (line 89); both are unreached because the activity is never started (no start site, no intent-filter)',
  'SRC common/WebViewActivity.java:61, 89, 92-95; SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2, G12',
  'SOURCE')

UNREACHABLE['WebViewActivity.getWebView'] = (
  'no_trigger_in_app',
  'private helper that builds the WebView (and the anonymous WebViewClient $1 and MyWebChromeClient); called only from post (line 152), which is called only from handleIntent (line 145); the activity is never started (no start site, no intent-filter)',
  'SRC common/WebViewActivity.java:97-131, 145, 152; SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2, G13',
  'SOURCE')

UNREACHABLE['WebViewActivity.handleIntent'] = (
  'no_trigger_in_app',
  'private helper called from onCreate (line 63) only; onCreate is unreached because the activity is never started (no start site, no intent-filter)',
  'SRC common/WebViewActivity.java:63, 137-147; SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2, G13',
  'SOURCE')

UNREACHABLE['WebViewActivity.post'] = (
  'no_trigger_in_app',
  'private helper called from handleIntent (line 145) only; handleIntent is unreached because the activity is never started (no start site, no intent-filter)',
  'SRC common/WebViewActivity.java:145, 149-152; SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2, G13',
  'SOURCE')

UNREACHABLE['WebViewActivity$1.<init>'] = (
  'no_trigger_in_app',
  'implicit constructor of the anonymous WebViewClient created in getWebView (line 111); getWebView is unreached because the activity is never started (no start site, no intent-filter)',
  'SRC common/WebViewActivity.java:111 (anonymous class creation); SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2',
  'SOURCE')

UNREACHABLE['WebViewActivity$1.shouldOverrideUrlLoading'] = (
  'no_trigger_in_app',
  'WebViewClient callback of the anonymous class created in getWebView (line 111); the WebView is never built because the activity is never started (no start site, no intent-filter)',
  'SRC common/WebViewActivity.java:111-117; SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2',
  'SOURCE')

UNREACHABLE['WebViewActivity$1.onPageFinished'] = (
  'no_trigger_in_app',
  'WebViewClient callback of the anonymous class created in getWebView (line 111); the WebView is never built because the activity is never started (no start site, no intent-filter)',
  'SRC common/WebViewActivity.java:111, 119-128; SRC AndroidManifest.xml:335-337; grep label_033.grep.txt G1, G2',
  'SOURCE')

UNREACHABLE['AbsListFragment.setSelection'] = (
  'no_trigger_in_app',
  'public setter with no caller in app source: no call to setSelection() on an AbsListFragment exists (grep G4 finds only the definition at AbsListFragment.java:124 and ExpandableListFragment.java:177, and ExpandableListFragment extends Fragment (ExpandableListFragment.java:48-49), not AbsListFragment; grep G5 shows qualified calls only on Spinner, EditText and ListView receivers)',
  'SRC core/AbsListFragment.java:124-127; SRC common/ExpandableListFragment.java:48-49, 177-180; grep label_033.grep.txt G4, G5',
  'SOURCE')

UNREACHABLE['AbsListFragment.getSelectedItemPosition'] = (
  'no_trigger_in_app',
  'public getter with no caller in app source: grep G3 finds only its definition and the ListView call inside it (AbsListFragment.java:132-135); the other getSelectedItemPosition calls in app/src are on spinner fields',
  'SRC core/AbsListFragment.java:132-135; grep label_033.grep.txt G3',
  'SOURCE')

UNREACHABLE['AbsListFragment.getSelectedItemId'] = (
  'no_trigger_in_app',
  'public getter with no caller in app source: grep G3 finds only its definition and the ListView call inside it (AbsListFragment.java:140-142); no getSelectedItemId call exists on any AbsListFragment receiver',
  'SRC core/AbsListFragment.java:140-143; grep label_033.grep.txt G3',
  'SOURCE')

UNREACHABLE['ListItemClickedEvent.<init>'] = (
  'no_trigger_in_app',
  'constructor called only from CloudItemViewHolder$1.onClick (CloudItemViewHolder.java:52) and CurrencyRecyclerListFragment.java:375; CloudItemViewHolder is never instantiated (grep G6: its name appears only in its own file and its constructor at :36 has no caller), and CurrencyRecyclerListFragment is created only by CurrencyRecyclerListActivity (createInstance, grep G7), which has no start site (manifest :359 has no intent-filter; MainActivity.java:644 is commented out). The subscriber at CurrencyRecyclerListFragment.java:266 does not construct the event',
  'SRC common/events/ListItemClickedEvent.java:26-30; SRC sync/CloudItemViewHolder.java:33, 36, 49-54; SRC currency/recycler/CurrencyRecyclerListFragment.java:74-80, 349-378; SRC currency/recycler/CurrencyRecyclerListActivity.java:27-44; SRC AndroidManifest.xml:359; SRC home/MainActivity.java:643-644; grep label_033.grep.txt G6, G7, G8',
  'SOURCE')
