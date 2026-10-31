# batch 037 (label_037): com.money.manager.ex.core IntentFactory (5 methods), MenuHelper (8), MoneyManagerBackupAgentHelper (2), MyWebChromeClient (2), NumericHelper (11), NumericPatternGenerator (2): 30 methods, 22 REACHABLE, 8 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_037.md; grep output: graphs/MMEX/parts/label_037.grep.txt.
# No e() edges for the in-app REACHABLE rows: they rest on auto_calls.json CALL records and on the caller batches named in label_037.md. The backup agent is started by the system (no app caller), so its two entry edges are written here.
# The auto CALL MyWebChromeClient.onProgressChanged -> WebViewActivity.updateProgress is cut here: its caller is UNREACHABLE in this batch, and its destination is UNREACHABLE in batch 033.

# ================================================================== REACHABLE entry edges (batch 037)

e('S_ENTRY', 'MoneyManagerBackupAgentHelper.<init>', 'ENTRY',
  'the system starts the backup agent of the package for a backup or restore run; the framework creates it with newInstance',
  env=env_text('the system backup manager runs a backup or restore for this package (AndroidManifest.xml:56 allowBackup=true, line 57 backupAgent)', ('system_event',)),
  evidence='SRC AndroidManifest.xml:56-57; FW-SRC core/java/android/app/ActivityThread.java:1740-1743 (CREATE_BACKUP_AGENT), 3208 (handleCreateBackupAgent), 3256 (loadClass and newInstance); INFERRED the system sends CREATE_BACKUP_AGENT when a backup runs (the backup scheduler is not read)')

e('MoneyManagerBackupAgentHelper.<init>', 'MoneyManagerBackupAgentHelper.onCreate', 'LIFECYCLE',
  'the framework calls onCreate on the agent after it attaches the context',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3256-3263 (newInstance, attach, onCreate)')

# ================================================================== cut (dst owned by batch 037)

# The auto CALL WebViewActivity.getWebView -> MyWebChromeClient.<init> would give an UNREACHABLE method an incoming edge (build warning). getWebView is UNREACHABLE (batch 033), so the edge is dead; the cut only removes the warning.
sup(('WebViewActivity.getWebView', 'MyWebChromeClient.<init>'))
sup(('MyWebChromeClient.onProgressChanged', 'WebViewActivity.updateProgress'))

# ================================================================== UNREACHABLE (batch 037)

UNREACHABLE['IntentFactory.<init>'] = ('no_trigger_in_app',
  'Implicit constructor of IntentFactory. Nothing creates an IntentFactory: no new IntentFactory in the app source and no auto_calls.json record names the constructor. Its four methods are static (IntentFactory.java:38, 54, 67, 80), so no instance is needed.',
  'SRC core/IntentFactory.java:37 (no constructor declared); label_037.grep.txt (IntentFactory block; auto_calls count 0)',
  'SOURCE')

UNREACHABLE['MenuHelper.add'] = ('no_trigger_in_app',
  'Public instance method (MenuHelper.java:97-105) with no caller. No auto_calls.json record names it, and no MenuHelper variable calls .add( in the 11 files that build one. The menu.add( calls in the same files are android.view.Menu.add, not this method.',
  'SRC core/MenuHelper.java:97-105; label_037.grep.txt (MenuHelper.add block; auto_calls count 0)',
  'SOURCE')

UNREACHABLE['MyWebChromeClient.<init>'] = ('no_trigger_in_app',
  'The only creation site is WebViewActivity.getWebView (WebViewActivity.java:131). Batch 033 labels getWebView UNREACHABLE: WebViewActivity has no start site, its manifest entry has no intent-filter, and no class extends it. The auto edge from getWebView is cut by the sup line above.',
  'SRC common/WebViewActivity.java:131; SRC AndroidManifest.xml:335-337; label_033.md (getWebView row); label_037.grep.txt (MyWebChromeClient block)',
  'SOURCE')

UNREACHABLE['MyWebChromeClient.onProgressChanged'] = ('framework_never_calls',
  'WebChromeClient callback. The WebView calls it only for the client set at WebViewActivity.java:132, and that WebView exists only if WebViewActivity.getWebView runs, which batch 033 shows never happens. No auto_calls.json record names it. Its outgoing edge to WebViewActivity.updateProgress is dead (its source is UNREACHABLE).',
  'SRC core/MyWebChromeClient.java:35-45; SRC common/WebViewActivity.java:131-132; label_033.md (updateProgress row); label_037.grep.txt (MyWebChromeClient block)',
  'INFERRED')

UNREACHABLE['NumericHelper.getCurrencyService'] = ('no_trigger_in_app',
  'Public instance accessor with no caller. No auto_calls.json record names it, and no call on a NumericHelper receiver exists. The getCurrencyService() calls in the app are FormatUtilities methods (FormatUtilities.java:73, 107, 184, 290, 306); FormatUtilities does not extend NumericHelper (FormatUtilities.java:43).',
  'SRC core/NumericHelper.java:137-142; SRC core/FormatUtilities.java:43, 298; label_037.grep.txt (getCurrencyService block)',
  'SOURCE')

UNREACHABLE['NumericHelper.toString'] = ('no_trigger_in_app',
  'Static NumericHelper.toString(Integer) with no caller: no auto_calls.json record, no NumericHelper.toString reference, and no static import of it. The name appears only at its definition.',
  'SRC core/NumericHelper.java:46-52; label_037.grep.txt (toString block; auto_calls count 0)',
  'SOURCE')

UNREACHABLE['NumericHelper.tryParse'] = ('no_trigger_in_app',
  'Public instance method with no caller. No auto_calls.json record names it, and the only .tryParse( calls in the app are Ints.tryParse (PerDatabaseFragment.java:191, LookFeelPreferenceFragment.java:144, SyncPreferences.java:65), which is another class.',
  'SRC core/NumericHelper.java:76-85; label_037.grep.txt (tryParse block; auto_calls count 0)',
  'SOURCE')

UNREACHABLE['NumericPatternGenerator.<init>'] = ('no_trigger_in_app',
  'Implicit constructor: the class declares no constructor (NumericPatternGenerator.java:22-41), and no code creates an instance. getPattern is static (NumericPatternGenerator.java:24), so no instance is needed.',
  'SRC core/NumericPatternGenerator.java:22-41; label_037.grep.txt (NumericPatternGenerator block; auto_calls count 0)',
  'SOURCE')
