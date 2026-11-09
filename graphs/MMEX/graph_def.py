# MMEX 2024.06.14 (package com.money.manager.ex, final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java),
# instrumented debug build (DATASET.txt; the flavor is not named there: src/main only). Schema 2.
# Section A: helpers, ENV and STATE gate texts. Section B: manifest entry points and process start.
# Later sections (one per batch of classes, see graphs/MMEX/AGENT_NOTES.md) are added as parts.

TITLE = 'MMEX 2024.06.14 trigger graph'
USE_AUTO = True
STRICT = True

ENV_KINDS_OF, STATE_KINDS_OF = {}, {}


def env_text(text, kinds):
    ENV_KINDS_OF[text] = list(kinds)
    return text


def state_text(text, kinds):
    STATE_KINDS_OF[text] = list(kinds)
    return text


def gui(src, dst, text, kind='GUI', **kw):
    e(src, dst, kind, text, gui=[text], **kw)


def sup(*pairs):
    for p in pairs:
        SUPPRESS.add(p)


# W7 review of f06dcbb2, items 2-3: hand edges dropped by (src, dst).
# Item 2 (Q-R6-4): ScreenTree and SysLogTree are planted only in the BuildConfig.DEBUG else branch (MmexApplication.java:134-140);
# the dataset APK is the instrumented debug build, so they are UNREACHABLE closed_by_configuration (as AnkiDroid's
# ProductionCrashReportingTree) and every hand edge into or out of them is dropped.
# Item 3 (Q-R6-3): the checking editor's split list only holds SplitCategory objects (loadTransaction reads SplitCategoriesRepository,
# CheckingTransactionEditActivity.java:397-399; createSplitCategoriesFromRecurringTransaction copies into new SplitCategory
# objects, :232-249; the split form makes items of the editor's own entity name), so it never writes or unwraps a
# SplitRecurringCategory parcel.
_R7_HAND_DROPS = {
    ('CheckingTransactionEditActivity.restoreInstanceState', 'SplitRecurringCategory$$Parcelable$1.createFromParcel'),
    ('CheckingTransactionEditActivity.restoreInstanceState', 'SplitRecurringCategory$$Parcelable.getParcel'),
    ('CheckingTransactionEditActivity.onSaveInstanceState', 'SplitRecurringCategory$$Parcelable.writeToParcel'),
}
_R7_RELEASE_TREES = ('ScreenTree.', 'SysLogTree.')
_r7_append_edge = e


def _r7_filter_edge(src, dst, *args, **kwargs):
    if (src, dst) in _R7_HAND_DROPS:
        return
    if src.split('@')[0].startswith(_R7_RELEASE_TREES) or dst.split('@')[0].startswith(_R7_RELEASE_TREES):
        return
    return _r7_append_edge(src, dst, *args, **kwargs)


e = _r7_filter_edge


# D22: classes for default edges whose text names a library (REVIEW list)
_DI = 'Dagger 2: generated component DaggerMmxComponent (generated class, INFERRED)'
_BIND = 'ButterKnife @OnClick: generated binding class %s (INFERRED)'
_RX = 'RxJava: the library calls the Subscriber/Action callback (INFERRED)'
_EB = 'EventBus (greenrobot): '
HAND_CLASS = {
    ('S_ENTRY', 'AccountEditActivity.<init>', 'ENTRY'): ('non_standard', 'intent resolved by action name: ACTION_EDIT or ACTION_INSERT (AndroidManifest.xml:227-234)'),
    ('AmountInputDialog$7.onClick', 'HomeFragment.onEvent', 'ASYNC'): ('non_standard', _EB + 'post(AmountEnteredEvent) delivered to @Subscribe onEvent'),
    ('HomeFragment.onStart', 'HomeFragment.onEvent', 'REGISTER'): ('non_standard', _EB + 'register(this) in onStart; @Subscribe onEvent(AmountEnteredEvent)'),
    ('SyncPreferenceFragment.onStart', 'SyncPreferenceFragment.onEvent', 'REGISTER'): ('non_standard', _EB + 'register(this) in onStart; @Subscribe onEvent(DbFileDownloadedEvent)'),
    ('SyncServiceMessageHandler.handleMessage', 'SyncPreferenceFragment.onEvent', 'ASYNC'): ('non_standard', _EB + 'post(DbFileDownloadedEvent) delivered to @Subscribe onEvent'),
    ('S_HOME', 'MainActivity.onClickCardViewIncomesVsExpenses', 'GUI'): ('non_standard', 'XML android:onClick (res/layout/home_fragment.xml:127)'),
    ('S_SELECT_DATABASE', 'SelectDatabaseActivity.onCreateDatabaseClick', 'GUI'): ('non_standard', _BIND % 'SelectDatabaseActivity_ViewBinding'),
    ('S_SELECT_DATABASE', 'SelectDatabaseActivity.onOpenDatabaseClick', 'GUI'): ('non_standard', _BIND % 'SelectDatabaseActivity_ViewBinding'),
    ('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$1.onNext', 'FRAMEWORK'): ('non_standard', _RX),
    ('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$1.onCompleted', 'FRAMEWORK'): ('non_standard', _RX),
    ('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$1.onError', 'FRAMEWORK'): ('non_standard', _RX),
    ('MorningstarPriceUpdater.processInParallel', 'MorningstarPriceUpdater$2.call', 'FRAMEWORK'): ('non_standard', _RX),
    ('CalculatorActivity.onCreate', 'S_CALCULATOR', 'ENTERS'): ('page', None),
    ('InvestmentTransactionEditActivity.onNumSharesClick', 'CalculatorActivity.<init>', 'INTENT'): ('standard', None),
    ('InvestmentTransactionEditActivity.onPurchasePriceClick', 'CalculatorActivity.<init>', 'INTENT'): ('standard', None),
    ('InvestmentTransactionEditActivity.onCommissionClick', 'CalculatorActivity.<init>', 'INTENT'): ('standard', None),
    ('InvestmentTransactionEditActivity.onCurrentPriceClick', 'CalculatorActivity.<init>', 'INTENT'): ('standard', None),
    ('SearchParametersFragment.onAmountFromClicked', 'CalculatorActivity.<init>', 'INTENT'): ('standard', None),
    ('SearchParametersFragment.onAmountToClicked', 'CalculatorActivity.<init>', 'INTENT'): ('standard', None),
    ('SelectDatabaseActivity.onCreateDatabaseClick', 'PasswordActivity.<init>', 'INTENT'): ('standard', None),
    ('SelectDatabaseActivity.onOpenDatabaseClick', 'PasswordActivity.<init>', 'INTENT'): ('standard', None),
    ('CurrencyListFragment.onActivityCreated', 'CurrencyListFragment.onStart', 'LIFECYCLE'): ('standard', None),
    ('CurrencyListFragment.onStart', 'CurrencyListFragment.onStop', 'LIFECYCLE'): ('standard', None),
    ('AmountInputDialog.onCreateDialog', 'AmountInputDialog$7.onClick', 'FRAMEWORK'): ('standard', None),
    ('WatchlistItemsFragment.onContextItemSelected', 'PriceEditActivity.<init>', 'INTENT'): ('standard', None),
    ('RecurringTransactionListFragment.<init>', 'RecurringTransactionListFragment.onCreate', 'LIFECYCLE'): ('standard', None),
    ('TutorialActivity.onCloseClicked', 'GeneralSettingsActivity.<init>', 'INTENT'): ('standard', None),
}


def CLASSIFY(x):
    cls = x['src'].split('(')[0].rsplit('.', 1)[0]
    if x['kind'] == 'CALL' and cls.startswith('DaggerMmxComponent'):
        return ('non_standard', _DI)
    if x['kind'] == 'CALL' and '_ViewBinding' in cls:
        return ('non_standard', _BIND % cls)
    return HAND_CLASS.get((x['src'], x['dst'], x['kind']))


# ================================================================== A. ENV and STATE gate texts

ENV_OTHER_APP_VIEW = env_text(
    'outside package: another app opens a file with MMEX (an ACTION_VIEW intent that the MainActivity VIEW filter accepts)',
    ('other_app',))

SCREENS = {
    'S_ENTRY': 'Outside the app: launcher, a .db file opened from another app, a widget tap or update, the sync adapter, or the system starting a component',
}

# ================================================================== B. entry points and process start

e('S_ENTRY', 'MmexApplication.<init>', 'ENTRY',
  'The process starts (the app is about to run any component)',
  gui=['Tap the MMEX launcher icon, or any component of the app is started by the system'],
  evidence='SRC AndroidManifest.xml:55; FW-SRC core/java/android/app/ActivityThread.java:5715-5722, 5740')

e('S_ENTRY', 'MainActivity.<init>', 'ENTRY',
  'The MAIN / LAUNCHER activity is started from the launcher',
  gui=['Tap the MMEX icon in the launcher'],
  evidence='SRC AndroidManifest.xml:136-143 (MAIN + LAUNCHER intent filter of com.money.manager.ex.home.MainActivity)')

e('S_ENTRY', 'MainActivity.<init>', 'ENTRY',
  'A .db file is opened with MMEX from another app (VIEW intent accepted by the browsable filter)',
  env=ENV_OTHER_APP_VIEW,
  evidence='SRC AndroidManifest.xml:145-149 (VIEW + DEFAULT + BROWSABLE filter of MainActivity)')

e('S_ENTRY', 'MmxContentProvider.<init>', 'ENTRY',
  'The process starts; the provider (exported=false) is installed before Application.onCreate',
  evidence='SRC AndroidManifest.xml:375-378; FW-SRC core/java/android/app/ActivityThread.java:5715-5722')

e('S_ENTRY', 'StubSyncProvider.<init>', 'ENTRY',
  'The process starts; the sync stub provider (exported=false) is installed before Application.onCreate',
  evidence='SRC AndroidManifest.xml:390-394; FW-SRC core/java/android/app/ActivityThread.java:5715-5722')

# ---- part 002 (2026-10-29)
# batch 002: MmexApplication (27 methods). Edges and UNREACHABLE entries only; the section-B edge S_ENTRY -> MmexApplication.<init> already exists in graph_def.py.

e('S_ENTRY', 'MmexApplication.<clinit>', 'ENTRY',
  'The process starts; the framework creates the Application class by name, which initializes the class (static fields) before the constructor',
  evidence='SRC AndroidManifest.xml:55; SRC MmexApplication.java:77; FW-SRC core/java/android/app/Instrumentation.java:1099-1103; JVM class initialization is not in fw_src: INFERRED, source not read')

e('MmexApplication.<init>', 'MmexApplication.attachBaseContext', 'LIFECYCLE',
  'The framework attaches the base context to the new Application before onCreate',
  evidence='SRC MmexApplication.java:216-218; FW-SRC core/java/android/app/Instrumentation.java:1099-1103 (app.attach(context)); Application.attach is not in fw_src: INFERRED, source not read')

e('MmexApplication.<init>', 'MmexApplication.onCreate', 'LIFECYCLE',
  'The framework calls Application.onCreate after attaching the base context (process start, before any component)',
  evidence='SRC MmexApplication.java:114-116; FW-SRC core/java/android/app/Instrumentation.java:1118-1120; FW-SRC core/java/android/app/LoadedApk.java:983-999; FW-SRC core/java/android/app/ActivityThread.java:5715-5740')

e('MmexApplication.onCreate', 'MmexApplication.lambda$onCreate$0', 'REGISTER',
  'onCreate passes the configuration lambda to the Amplitude client builder, which calls it while it builds the client',
  evidence='SRC MmexApplication.java:147-154; library com.amplitude.android is not in the dataset: its call of the lambda is INFERRED, source not read')

UNREACHABLE['MmexApplication.onTerminate'] = (
  'framework_never_calls',
  'The framework calls onTerminate only from the EXIT_APPLICATION handler, which runs only after ActivityThread.scheduleExit; the two ActivityManagerService callers of scheduleExit run only for pid <= 0 or the system_server pid, never for an app process (the other branches call killProcessQuiet or app.kill). No in-app caller.',
  'MmexApplication.java:207-214',
  'SOURCE')

UNREACHABLE['MmexApplication.killApplication'] = (
  'no_trigger_in_app',
  'Public static method that kills the process; the app src tree has no caller and no XML or reflective reference (grep shows only the definition at line 102).',
  'MmexApplication.java:99-105',
  'SOURCE')

# ---- part 004 (2026-10-29)
# ================================================================== batch 004 (label_004): PayeeActivity, About*
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_004.md.
# Every edge below has a batch 004 method as its destination; the sources belong to other batches.

SCREENS.update({
    'S_PAYEE': 'Payee picker (PayeeActivity), opened from a payee field or by another app sending an ACTION_PICK or ACTION_EDIT intent',
    'S_ABOUT_ACTIVITY': 'About screen (AboutActivity): tab bar with About, Changelog, Credits and Libraries',
    'S_ABOUT_TAB': 'About tab of the About screen: feedback and logcat links, the Send logcat button and the project links',
})

# ---- PayeeActivity
e('S_ENTRY', 'PayeeActivity.<init>', 'ENTRY',
  'another app sends an ACTION_PICK or ACTION_EDIT intent to the exported PayeeActivity',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to PayeeActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:190-197; FW-SRC core/java/android/app/ActivityThread.java:2665-2672')

e('SearchParametersFragment$1.onClick', 'PayeeActivity.<init>', 'INTENT',
  'startActivityForResult(ACTION_PICK) starts PayeeActivity when the payee field is tapped',
  gui=['Tap the payee field on the search screen'],
  evidence='SRC search/SearchParametersFragment.java:189-196')

e('EditTransactionCommonFunctions$9.onClick', 'PayeeActivity.<init>', 'INTENT',
  'startActivityForResult(ACTION_PICK) starts PayeeActivity when the payee field is tapped in the transaction editor',
  gui=['Tap the payee field in the transaction editor'],
  evidence='SRC transactions/EditTransactionCommonFunctions.java:571-580')

e('S_ENTRY', 'PayeeActivity.<clinit>', 'ENTRY',
  'the first PayeeActivity instance (the exported-intent start above) initialises the class',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to PayeeActivity (exported=true)', ('other_app',)),
  evidence='SRC PayeeActivity.java:35; SRC AndroidManifest.xml:190-197; INFERRED the JVM runs a static initialiser before the first instance (Java language rule, not read from a source)')

e('SearchParametersFragment$1.onClick', 'PayeeActivity.<clinit>', 'INTENT',
  'the first PayeeActivity instance (the start above) initialises the class',
  gui=['Tap the payee field on the search screen'],
  evidence='SRC PayeeActivity.java:35; SRC search/SearchParametersFragment.java:189-196; INFERRED the JVM runs a static initialiser before the first instance (Java language rule, not read from a source)')

e('EditTransactionCommonFunctions$9.onClick', 'PayeeActivity.<clinit>', 'INTENT',
  'the first PayeeActivity instance (the start above) initialises the class',
  gui=['Tap the payee field in the transaction editor'],
  evidence='SRC PayeeActivity.java:35; SRC transactions/EditTransactionCommonFunctions.java:571-580; INFERRED the JVM runs a static initialiser before the first instance (Java language rule, not read from a source)')

e('PayeeActivity.<init>', 'PayeeActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC PayeeActivity.java:39-62')

e('PayeeActivity.onCreate', 'S_PAYEE', 'ENTERS',
  'the payee picker is shown',
  evidence='SRC PayeeActivity.java:39-62')

e('PayeeActivity.onCreate', 'PayeeActivity.onKeyUp', 'FRAMEWORK',
  'the activity is in front and the user releases Back: the framework dispatches the key-up event to onKeyUp',
  gui=['Press Back while the payee list is shown'],
  evidence='FW-SRC core/java/android/app/Activity.java:3255-3272; FW-SRC core/java/android/view/KeyEvent.java:2709-2715; SRC PayeeActivity.java:64-76')

# ---- AboutActivity
# B6-DRAWER: plain dispatcher -> AboutActivity.<init> partitioned to @GROUP in graph_def_mod/03.py (plain edge deleted).

e('SettingsFragment$9.onPreferenceClick', 'AboutActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AboutActivity.class)) from the info preference',
  gui=['Open Settings and tap the info preference'],
  evidence='SRC settings/SettingsFragment.java:166-172')

e('AboutActivity.<init>', 'AboutActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC about/AboutActivity.java:38-56')

e('AboutActivity.onCreate', 'S_ABOUT_ACTIVITY', 'ENTERS',
  'the About screen is shown',
  evidence='SRC about/AboutActivity.java:38-56')

e('AboutActivity.onCreate', 'AboutActivity.setTheme', 'CALL',
  'super.onCreate (MmxBaseFragmentActivity) calls setTheme() unconditionally; dispatch selects the AboutActivity override',
  evidence='SRC common/MmxBaseFragmentActivity.java:57-58; SRC about/AboutActivity.java:70-77')

e('AboutActivity.onCreate', 'AboutTabAdapter.getCount', 'FRAMEWORK',
  'the ViewPager reads the page count when the adapter is set',
  evidence='SRC about/AboutActivity.java:45-51; INFERRED androidx ViewPager calls getCount when the adapter is set (androidx source not read)')

e('AboutActivity.onCreate', 'AboutTabAdapter.getItem', 'FRAMEWORK',
  'the ViewPager asks the adapter for page 0 when the About screen is shown',
  evidence='SRC about/AboutActivity.java:45-51; INFERRED androidx ViewPager and FragmentPagerAdapter call getItem for the first page (androidx source not read)')

e('S_ABOUT_ACTIVITY', 'AboutTabAdapter.getItem', 'GUI',
  'swipe to or tap a tab title (About, Changelog, Credits, Libraries)',
  gui=['Swipe to or tap a tab title (About, Changelog, Credits, Libraries)'],
  evidence='SRC about/AboutActivity.java:44-55; INFERRED androidx ViewPager and material TabLayout call getItem on a tab change (library source not read)')

e('AboutActivity.onCreate', 'AboutTabAdapter.getPageTitle', 'FRAMEWORK',
  'TabLayout.setupWithViewPager reads the tab titles',
  evidence='SRC about/AboutActivity.java:54-55; INFERRED material TabLayout.setupWithViewPager calls getPageTitle (material source not read)')

e('AboutActivity.onCreate', 'AboutActivity.onRestoreInstanceState', 'LIFECYCLE',
  'the activity is recreated with its saved state after a rotation (the About activity does not handle configuration changes)',
  env=env_text('screen rotation: a configuration change the About activity does not handle, so the framework recreates it', ('hardware',)),
  evidence='SRC AndroidManifest.xml:216-218; FW-SRC core/java/android/app/ActivityThread.java:2747-2751; FW-SRC core/java/android/app/Instrumentation.java:1259-1262; INFERRED the relaunch path that recreates the activity is not read (ActivityThread relaunch source not read)')

e('AboutActivity.onCreate', 'AboutActivity.onSaveInstanceState', 'LIFECYCLE',
  'the user presses Home: the framework saves the instance state of the paused activity',
  gui=['Press Home while About is shown'],
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3855-3876, 4700-4722; FW-SRC core/java/android/app/Instrumentation.java:1385-1386; FW-SRC core/java/android/app/Activity.java:1495-1496; SRC about/AboutActivity.java:58-62')

# ---- AboutChangelogFragment: no creation site reachable from the app (UNREACHABLE, no edges)
UNREACHABLE['AboutChangelogFragment.<init>'] = ('no_trigger_in_app', 'the class is never instantiated: its only creation site is AboutChangelogFragment.newInstance, which has no caller; the only reference in the app outside the class is the commented-out line AboutTabAdapter.java:54; no layout or manifest names the class (label_004.grep.txt)', 'SRC about/AboutChangelogFragment.java:29-37; SRC about/AboutTabAdapter.java:53-55; grep label_004.grep.txt', 'SOURCE')
UNREACHABLE['AboutChangelogFragment.newInstance'] = ('no_trigger_in_app', 'no caller in the app: the only call site is commented out at AboutTabAdapter.java:54, and the active case 1 returns WebChangelogFragment.newInstance()', 'SRC about/AboutChangelogFragment.java:32-37; SRC about/AboutTabAdapter.java:53-55; grep label_004.grep.txt', 'SOURCE')
UNREACHABLE['AboutChangelogFragment.onCreateView'] = ('no_trigger_in_app', 'the fragment is never created (see AboutChangelogFragment.newInstance and AboutChangelogFragment.<init>), so no lifecycle callback reaches onCreateView', 'SRC about/AboutChangelogFragment.java:39-43', 'SOURCE')

sup(('AboutChangelogFragment.newInstance', 'AboutChangelogFragment.<init>'))  # newInstance has no caller, so the bytecode call into <init> cannot run

# ---- AboutCreditsFragment
e('AboutCreditsFragment.<init>', 'AboutCreditsFragment.onCreateView', 'LIFECYCLE',
  'the ViewPager adds the Credits page and the framework calls onCreateView',
  evidence='SRC about/AboutCreditsFragment.java:44-47; INFERRED androidx Fragment lifecycle calls onCreateView after the constructor (androidx source not read)')

e('AboutCreditsFragment.onCreateView', 'AboutCreditsFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onCreateView',
  evidence='SRC about/AboutCreditsFragment.java:49-63; INFERRED androidx Fragment lifecycle calls onActivityCreated after onCreateView (androidx source not read)')

# ---- AboutFragment
e('AboutFragment.<init>', 'AboutFragment.onCreateView', 'LIFECYCLE',
  'the ViewPager adds the About page and the framework calls onCreateView',
  evidence='SRC about/AboutFragment.java:61-64; INFERRED androidx Fragment lifecycle calls onCreateView after the constructor (androidx source not read)')

e('AboutFragment.onCreateView', 'S_ABOUT_TAB', 'ENTERS',
  'the About tab is shown and onCreateView sets up its links and buttons',
  evidence='SRC about/AboutFragment.java:61-64, 88-199')

e('S_ABOUT_TAB', 'AboutFragment$1.onClick', 'GUI',
  'tap the feedback link on the About tab',
  gui=['Tap the feedback link on the About tab'],
  evidence='SRC about/AboutFragment.java:88-101; INFERRED javac source-order numbering (class file names not read)')

e('S_ABOUT_TAB', 'AboutFragment$2.onClick', 'GUI',
  'tap the logcat link on the About tab',
  gui=['Tap the logcat link on the About tab'],
  evidence='SRC about/AboutFragment.java:181-189; INFERRED javac source-order numbering (class file names not read)')

e('S_ABOUT_TAB', 'AboutFragment$3.onClick', 'GUI',
  'tap the Send logcat button on the About tab',
  gui=['Tap the Send logcat button on the About tab'],
  evidence='SRC about/AboutFragment.java:193-199; INFERRED javac source-order numbering (class file names not read)')

e('S_ABOUT_TAB', 'AboutFragment$OnClickListenerUrl.onClick', 'GUI',
  'tap the issue tracker link on the About tab',
  gui=['Tap the issue tracker link on the About tab'],
  evidence='SRC about/AboutFragment.java:116-122; SRC about/AboutFragment.java:207-218')

e('S_ABOUT_TAB', 'AboutFragment$OnClickListenerUrl.onClick', 'GUI',
  'tap the MMEX website link on the About tab',
  gui=['Tap the MMEX website link on the About tab'],
  evidence='SRC about/AboutFragment.java:125-137; SRC about/AboutFragment.java:207-218')

e('S_ABOUT_TAB', 'AboutFragment$OnClickListenerUrl.onClick', 'GUI',
  'tap the report link (textViewLinkWebSite) on the About tab',
  gui=['Tap the report link on the About tab'],
  evidence='SRC about/AboutFragment.java:140-152; SRC about/AboutFragment.java:207-218')

e('S_ABOUT_TAB', 'AboutFragment$OnClickListenerUrl.onClick', 'GUI',
  'tap the Google+ image on the About tab',
  gui=['Tap the Google+ image on the About tab'],
  evidence='SRC about/AboutFragment.java:154-158; SRC about/AboutFragment.java:207-218')

e('S_ABOUT_TAB', 'AboutFragment$OnClickListenerUrl.onClick', 'GUI',
  'tap the GitHub image on the About tab',
  gui=['Tap the GitHub image on the About tab'],
  evidence='SRC about/AboutFragment.java:160-164; SRC about/AboutFragment.java:207-218')

e('S_ABOUT_TAB', 'AboutFragment$OnClickListenerUrl.onClick', 'GUI',
  'tap the Twitter image on the About tab',
  gui=['Tap the Twitter image on the About tab'],
  evidence='SRC about/AboutFragment.java:165-169; SRC about/AboutFragment.java:207-218')

e('S_ABOUT_TAB', 'AboutFragment$OnClickListenerUrl.onClick', 'GUI',
  'tap the GPLv2 licence link on the About tab',
  gui=['Tap the licence link on the About tab'],
  evidence='SRC about/AboutFragment.java:171-176; SRC about/AboutFragment.java:207-218')

UNREACHABLE['AboutFragment.useProcessBuilder'] = ('no_trigger_in_app', 'private method with no call in the app: the name occurs only at its declaration (label_004.grep.txt); its own comment says the approach still needs to be tried out', 'SRC about/AboutFragment.java:287-293; grep label_004.grep.txt', 'SOURCE')

# ---- part 003 (2026-10-29)
# ================================================================== batch 003 (label_003): MmxContentProvider, MmxContentProvider_MembersInjector, PasscodeActivity, PasscodeActivity$1, PasscodeActivity$FingerprintException, PasscodeActivity_ViewBinding
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_003.md.
# Edges end on a batch 003 method or on the screen S_PASSCODE; their sources may belong to other batches.
# Bytecode calls between methods come from auto_calls.json (USE_AUTO); only the edges the bytecode cannot see are written here.
# The Dagger and ButterKnife classes are generated and the EventBus and ButterKnife libraries were not read: INFERRED.

SCREENS.update({
    'S_PASSCODE': 'Passcode screen (PasscodeActivity): digit keys and the backspace key; the fingerprint prompt appears when the device has a fingerprint sensor',
})

# ---- MmxContentProvider: process start, lifecycle, and the resolver calls from RepositoryBase
e('S_ENTRY', 'MmxContentProvider.<clinit>', 'ENTRY',
  'the process starts and ActivityThread installs the manifest provider; the class is initialised at the first newInstance',
  evidence='SRC AndroidManifest.xml:375-378; FW-SRC core/java/android/app/ActivityThread.java:5720-5722, 6225-6228; INFERRED the JVM initialises a class at its first newInstance (Java language rule, not read from a source)')

e('MmxContentProvider.<init>', 'MmxContentProvider.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor, from attachInfo',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:6225-6239; FW-SRC core/java/android/content/ContentProvider.java:1891-1917; SRC MmxContentProvider.java:98-103')

e('RepositoryBase.delete', 'MmxContentProvider.delete', 'FRAMEWORK',
  'a record is deleted: RepositoryBase.delete calls ContentResolver.delete on the MMEX URI and the provider receives the call',
  evidence='SRC datalayer/RepositoryBase.java:226-228; FW-SRC core/java/android/content/ContentResolver.java:1627-1636; FW-SRC core/java/android/content/ContentProvider.java:333-341')

e('RepositoryBase.insert', 'MmxContentProvider.insert', 'FRAMEWORK',
  'a record is inserted: RepositoryBase.insert calls ContentResolver.insert on the MMEX URI and the provider receives the call',
  evidence='SRC datalayer/RepositoryBase.java:156-160; FW-SRC core/java/android/content/ContentResolver.java:1532-1539; FW-SRC core/java/android/content/ContentProvider.java:264-265')

e('RepositoryBase.update(EntityBase,String,String[])', 'MmxContentProvider.update', 'FRAMEWORK',
  'a record is updated: RepositoryBase.update calls ContentResolver.update on the MMEX URI and the provider receives the call',
  evidence='SRC datalayer/RepositoryBase.java:183-190; FW-SRC core/java/android/content/ContentResolver.java:1662-1672; FW-SRC core/java/android/content/ContentProvider.java:348-357')

e('RepositoryBase.openCursor(String[],String,String[],String)', 'MmxContentProvider.query', 'FRAMEWORK',
  'a cursor is opened: RepositoryBase.openCursor calls ContentResolver.query on the MMEX URI and the provider receives the call',
  evidence='SRC datalayer/RepositoryBase.java:73-75; FW-SRC core/java/android/content/ContentResolver.java:753-755; FW-SRC core/java/android/content/ContentProvider.java:228-229, 240-241')

# ---- PasscodeActivity: who starts it
e('MainActivity.onStart', 'PasscodeActivity.<init>', 'INTENT',
  'MainActivity.onStart starts PasscodeActivity for the passcode when a passcode is saved and this session is not authenticated yet',
  needs_state=state_text('a passcode is saved (settings) and the session is not authenticated yet', ('settings', 'session')),
  evidence='SRC home/MainActivity.java:252-260; SRC Passcode.java:70-72; FW-SRC core/java/android/app/Instrumentation.java:1143-1148')

e('RecurringTransactionListActivity.onCreate', 'PasscodeActivity.<init>', 'INTENT',
  'the recurring transactions screen opened from a notification starts PasscodeActivity first when a passcode is set',
  env=env_text('the user taps the recurring transaction notification (the activity is started with INTENT_EXTRA_LAUNCH_NOTIFICATION)', ('system_event',)),
  needs_state=state_text('a passcode is set (settings)', ('settings',)),
  evidence='SRC recurring/transactions/RecurringTransactionListActivity.java:48-56')

e('SecuritySettingsFragment.startActivityPasscode', 'PasscodeActivity.<init>', 'INTENT',
  'the Security settings start PasscodeActivity from the active-passcode preference',
  gui=['Open Settings, Security, and change the active-passcode preference'],
  evidence='SRC settings/SecuritySettingsFragment.java:55-60, 168-175')

e('PasscodeActivity.<init>', 'PasscodeActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2728-2731; FW-SRC core/java/android/app/Instrumentation.java:1212-1215; FW-SRC core/java/android/app/Activity.java:989-990; SRC PasscodeActivity.java:82')

e('PasscodeActivity.onCreate', 'PasscodeActivity.onStart', 'LIFECYCLE',
  'the framework starts the activity after onCreate (performStart)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2740-2741; FW-SRC core/java/android/app/Activity.java:7014-7019; FW-SRC core/java/android/app/Instrumentation.java:1333-1335; SRC PasscodeActivity.java:203-207')

e('PasscodeActivity.onStart', 'PasscodeActivity.onStop', 'LIFECYCLE',
  'the user presses Home while the passcode screen is shown: the framework stops the activity',
  gui=['Press Home while the passcode screen is shown'],
  evidence='FW-SRC core/java/android/app/Activity.java:7159-7181; FW-SRC core/java/android/app/Instrumentation.java:1374-1376; FW-SRC core/java/android/app/Activity.java:1856-1860; SRC PasscodeActivity.java:209-213')

# ---- PasscodeActivity: the screen, its digit keys and the backspace key
e('PasscodeActivity.onCreate', 'S_PASSCODE', 'ENTERS',
  'the passcode screen is shown (onCreate sets up the digit keys and the backspace key)',
  evidence='SRC PasscodeActivity.java:82-141')

e('S_PASSCODE', 'PasscodeActivity$1.onClick', 'GUI',
  'tap a digit key (buttonPasscode0 to 9): the shared click listener handles the digit',
  gui=['Tap a digit key on the passcode screen'],
  evidence='SRC PasscodeActivity.java:99, 134-141; FW-SRC core/java/android/view/View.java:6143-6144, 6289-6294')

# ---- PasscodeActivity: EventBus subscriber (library, INFERRED)
e('PasscodeActivity.onStart', 'PasscodeActivity.onEvent', 'REGISTER',
  'the activity is registered on EventBus in onStart; an error logged through Timber posts ErrorRaisedEvent, which calls onEvent',
  env=env_text('an error is logged through Timber while the activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): register(this) in onStart, @Subscribe onEvent(ErrorRaisedEvent) (library source not read, INFERRED)',
  evidence='SRC PasscodeActivity.java:203-207, 214-218; SRC log/DebugTree.java:45-46; SRC log/ScreenTree.java:26-27; SRC log/CrashReportingTree.java:56 (not planted in the debug build); SRC MmexApplication.java:134-139; INFERRED EventBus library source not read')

# ---- PasscodeActivity: ButterKnife binding (generated class, INFERRED)
e('PasscodeActivity.onCreate', 'PasscodeActivity_ViewBinding.<init>(PasscodeActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for this activity, which binds the @OnClick handler and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated PasscodeActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC PasscodeActivity.java:95-97; INFERRED ButterKnife generated binding (library and generated source not read)')

e('S_PASSCODE', 'PasscodeActivity_ViewBinding$1.doClick', 'GUI',
  'tap the backspace key: the listener attached by the generated binding calls onBackspaceClick',
  gui=['Tap the backspace key on the passcode screen'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class)',
  evidence='SRC PasscodeActivity.java:220-221; INFERRED generated class PasscodeActivity_ViewBinding.java (not in the source root; bytecode edges in auto_calls at lines 30 and 33)')

# ================================================================== UNREACHABLE (batch 003)
UNREACHABLE['MmxContentProvider.getType'] = ('no_trigger_in_app',
  'the framework calls it only when some ContentResolver.getType call names an MMEX URI; the app has no such call (label_003.grep.txt), no getUri() call site is on a line that builds an Intent or putExtra (label_003.grep.txt), and the provider is exported=false',
  'SRC MmxContentProvider.java:342-345; FW-SRC core/java/android/content/ContentProvider.java:249-252; SRC AndroidManifest.xml:375-378; label_003.grep.txt',
  'SOURCE')

UNREACHABLE['MmxContentProvider.logQuery'] = ('no_trigger_in_app',
  'private method with no call site: the name occurs only at its declaration in the app source (label_003.grep.txt) and has no bytecode caller',
  'SRC MmxContentProvider.java:428-454; label_003.grep.txt',
  'SOURCE')

sup(('MmxContentProvider_MembersInjector.create', 'MmxContentProvider_MembersInjector.<init>'))  # create has no caller, so the bytecode call into <init> cannot run

UNREACHABLE['MmxContentProvider_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (not in the source root) whose only caller record is MmxContentProvider_MembersInjector.create, and create has no caller record in auto_calls.json; no MembersInjector reference in the app source (label_003.grep.txt)',
  'python-printed auto_calls record MmxContentProvider_MembersInjector.java:24; label_003.grep.txt',
  'INFERRED')

UNREACHABLE['MmxContentProvider_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (not in the source root) with no caller record in auto_calls.json; no MembersInjector reference in the app source (label_003.grep.txt)',
  'python-printed auto_calls query (0 callers); label_003.grep.txt',
  'INFERRED')

UNREACHABLE['MmxContentProvider_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (not in the source root) with no caller record for any receiver in auto_calls.json; the component injects the provider through injectOpenHelper directly (DaggerMmxComponent.java:526)',
  'python-printed auto_calls queries; MmxContentProvider_MembersInjector.java:29; label_003.grep.txt',
  'INFERRED')

UNREACHABLE['PasscodeActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root): ButterKnife.bind(this) at PasscodeActivity.java:96 discards the returned Unbinder, PasscodeActivity has no onDestroy, and no caller record exists in auto_calls.json (label_003.grep.txt)',
  'SRC PasscodeActivity.java:95-97; label_003.grep.txt; python-printed auto_calls query (0 callers)',
  'INFERRED')

# ---- part 001 (2026-10-29)
# batch 001: HelpActivity (3 methods) and the generated data-binding classes (16 methods).
# Edges and UNREACHABLE entries only. Rows and printed lines: graphs/MMEX/parts/label_001.md.
# Every edge below has a batch 001 method as its destination.

SCREENS.update({
    'S_HELP': 'Help page (HelpActivity): a WebView showing a help page from a raw file or a URL, opened by another app',
})

# ---- HelpActivity
e('S_ENTRY', 'HelpActivity.<init>', 'ENTRY',
  'another app starts the exported HelpActivity with the custom action WEB_VIEW_URL or WEB_VIEW_RAW_FILE and a file: URI',
  env=env_text('outside package: another app sends an intent with the custom action WEB_VIEW_URL or WEB_VIEW_RAW_FILE and a file: URI to the exported HelpActivity (AndroidManifest.xml:301-313)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:301-313; FW-SRC core/java/android/app/Instrumentation.java:1170-1175; FW-SRC core/java/android/app/ActivityThread.java:2669-2670; intent matching (IntentFilter) is not in fw_src: INFERRED, source not read')

e('HelpActivity.<init>', 'HelpActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='SRC HelpActivity.java:36-38; FW-SRC core/java/android/app/Instrumentation.java:1212-1215; FW-SRC core/java/android/app/ActivityThread.java:2729-2731; FW-SRC core/java/android/app/Activity.java:6989-6999')

e('HelpActivity.onCreate', 'S_HELP', 'ENTERS',
  'the help page is shown: onCreate loads the raw file or the URL from the intent into the WebView',
  evidence='SRC HelpActivity.java:36-64')

e('HelpActivity.onCreate', 'HelpActivity.onKeyDown', 'FRAMEWORK',
  'the help page is in front and the user presses Back: the framework dispatches the key-down event to onKeyDown',
  gui=['Press Back while the help page is shown'],
  evidence='FW-SRC core/java/android/app/Activity.java:3255-3274; FW-SRC core/java/android/view/KeyEvent.java:2684-2692; SRC HelpActivity.java:66-75')

# ---- data-binding library and generated classes: no trigger in the app
UNREACHABLE['databinding.DataBinderMapperImpl.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the data-binding library generated subclass of MergedDataBinderMapper. It is created only by the library DataBindingUtil, which no app class references, and no res layout has a <layout> root. Library source not read, so this is INFERRED.',
  'label_001.grep.txt:4-8, 35-44, 75; auto_calls.json:4-13',
  'INFERRED')

UNREACHABLE['baseAdapters.BR.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the library constants class androidx.databinding.library.baseAdapters.BR. Its fields are constants; only its own class file mentions it and no source file mentions baseAdapters. Library class: source not read, so this is INFERRED.',
  'label_001.grep.txt:21-22, 52-53, 73',
  'INFERRED')

UNREACHABLE['ex.BR.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the generated com.money.manager.ex.BR constants class. BudgetViewModel reads BR.year, name and month as constants and never constructs BR; no auto_calls.json edge reaches ex.BR.<init>. Generated class: source not read, so this is INFERRED.',
  'BudgetViewModel.java:23, 81-94; label_001.grep.txt:9-20, 54-56, 72',
  'INFERRED')

UNREACHABLE['Constants.<init>'] = (
  'no_trigger_in_app',
  'Constants has only literal static final fields and no explicit constructor. No new Constants and no Constants() call exists in the source, and no auto_calls.json edge reaches Constants.<init>.',
  'Constants.java:17-56; label_001.grep.txt:24-26',
  'SOURCE')

sup(('databinding.DataBinderMapperImpl.<init>', 'ex.DataBinderMapperImpl.<clinit>'),
    ('databinding.DataBinderMapperImpl.<init>', 'ex.DataBinderMapperImpl.<init>'),
    ('ex.DataBinderMapperImpl.getLayoutId', 'ex.DataBinderMapperImpl$InnerLayoutIdLookup.<clinit>'),
    ('ex.DataBinderMapperImpl.convertBrIdToString', 'ex.DataBinderMapperImpl$InnerBrLookup.<clinit>'))  # these callers are UNREACHABLE, so the bytecode calls cannot run

UNREACHABLE['ex.DataBinderMapperImpl.<clinit>'] = (
  'no_trigger_in_app',
  'Static initializer of the generated mapper. It runs only on first use of the mapper class; the only bytecode route is the androidx mapper constructor (auto_calls.json:4-5), which needs DataBindingUtil, and no app code uses it. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:4-5; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the generated mapper, called only from the androidx mapper constructor (auto_calls.json:12-13), which is reached only through the library DataBindingUtil (no app code uses it). Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:12-13; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.collectDependencies'] = (
  'no_trigger_in_app',
  'Method of the generated mapper. No auto_calls.json caller edge, and no app source or class file calls it; it is reached only through the library mapper machinery, which needs DataBindingUtil. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json (no caller edge); label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.convertBrIdToString'] = (
  'no_trigger_in_app',
  'Method of the generated mapper. No caller edge in auto_calls.json; its only outgoing edge is InnerBrLookup.<clinit> (lines 1150-1151). It is reached only through the library mapper machinery, which needs DataBindingUtil. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1150-1151; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)'] = (
  'no_trigger_in_app',
  'Method of the generated mapper, called only by the library DataBindingUtil binding calls (inflate or bind). No app code calls those, and no auto_calls.json caller edge exists. Generated class: source not read, so this is INFERRED.',
  'label_001.grep.txt:4-8, 39-44; auto_calls.json (no caller edge)',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View[],int)'] = (
  'no_trigger_in_app',
  'Second overload of the generated mapper getDataBinder, called only by the library DataBindingUtil binding calls (inflate or bind). No app code calls those, and no auto_calls.json caller edge exists. Generated class: source not read, so this is INFERRED.',
  'label_001.grep.txt:4-8, 39-44; auto_calls.json (no caller edge)',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl.getLayoutId'] = (
  'no_trigger_in_app',
  'Method of the generated mapper. No caller edge in auto_calls.json; its only outgoing edge is InnerLayoutIdLookup.<clinit> (lines 1142-1143). It is reached only through the library DataBindingUtil, which no app code uses. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1142-1143; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl$InnerBrLookup.<clinit>'] = (
  'no_trigger_in_app',
  'Static initializer of the nested BR lookup. The only edge into it is the call from convertBrIdToString (auto_calls.json:1150-1151), which has no app caller. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1150-1151; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl$InnerBrLookup.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the nested BR lookup. No edge in the auto_calls.json calls section reaches it; the only edge into the lookup is the <clinit> call at line 1151. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1150-1151; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl$InnerLayoutIdLookup.<clinit>'] = (
  'no_trigger_in_app',
  'Static initializer of the nested layout-id lookup. The only edge into it is the call from getLayoutId (auto_calls.json:1142-1143), which has no app caller. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1142-1143; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['ex.DataBinderMapperImpl$InnerLayoutIdLookup.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the nested layout-id lookup. No edge in the auto_calls.json calls section reaches it; the only edge into the lookup is the <clinit> call at line 1143. Generated class: source not read, so this is INFERRED.',
  'auto_calls.json:1142-1143; label_001.grep.txt:4-8, 39-44',
  'INFERRED')

UNREACHABLE['DataBindingTriggerClass.<init>'] = (
  'no_trigger_in_app',
  'Constructor of the generated marker class that carries the BindingBuildInfo annotation. No source file and no other app class file mentions it, and no auto_calls.json edge reaches it. Library and generated class: source not read, so the claim that no code instantiates it is INFERRED.',
  'label_001.grep.txt:32-33, 45-46, 74',
  'INFERRED')

# ---- part 005 (2026-10-29)
# batch 005: WebChangelogFragment (5 methods), the Changelog tab of the About screen. Edges only; rows and printed lines: graphs/MMEX/parts/label_005.md.
# The bytecode CALL edges AboutTabAdapter.getItem -> newInstance, newInstance -> <init> and onCreateView -> loadChangelog are in auto_calls.json, so none is written here (D7).
# No UNREACHABLE entry: all five methods have a route. The Changelog tab has no page of its own (the About screen is S_ABOUT_ACTIVITY, part 004), so no new page and no ENTERS edge.

e('WebChangelogFragment.<init>', 'WebChangelogFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor, when the Changelog fragment is added to the tab pager',
  evidence='SRC about/WebChangelogFragment.java:39-41, 58-66; INFERRED androidx Fragment lifecycle calls onCreate after the constructor (androidx source not read)')

e('WebChangelogFragment.onCreate', 'WebChangelogFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC about/WebChangelogFragment.java:58-77; INFERRED androidx Fragment lifecycle calls onCreateView after onCreate (androidx source not read)')

# ---- part 006 (2026-10-29)
# ================================================================== batch 006 (label_006): com.money.manager.ex.account.AccountEditActivity (40 of its 52 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_006.md.
# Every edge below has a batch 006 method as its destination (or is the ENTERS edge to the screen this batch defines).
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here.
# Framework claims cite FW-SRC lines printed for this batch; other claims are INFERRED where the source was not read.

SCREENS.update({
    'S_ACCOUNT_EDIT': 'Account edit form (AccountEditActivity): account fields, the type and status spinners, the favourite and default toggles, save and cancel',
})

# ---- entry and intent edges into the activity

e('S_ENTRY', 'AccountEditActivity.<init>', 'ENTRY',
  'another app sends an ACTION_EDIT or ACTION_INSERT intent to the exported AccountEditActivity',
  env=env_text('outside package: another app sends an ACTION_EDIT or ACTION_INSERT intent to AccountEditActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:227-234; FW-SRC core/java/android/app/ActivityThread.java:2665-2670; FW-SRC core/java/android/app/Instrumentation.java:1143-1148; how the framework matches an implicit intent to this filter is not printed: INFERRED, source not read')

e('HomeFragment.onContextItemSelected', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AccountEditActivity.class)) with KEY_ACCOUNT_ID and ACTION_EDIT',
  gui=['Open the context menu of an account on the home screen and choose Edit'],
  guard='the menu title equals R.string.edit (HomeFragment.java:462)',
  evidence='SRC home/HomeFragment.java:450-469 (account check 455; EDIT check 462; intent 463-466; startActivity 466)')

e('HomeFragment$3.onClick', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AccountEditActivity.class)) with ACTION_INSERT',
  gui=['Tap the add account button (R.id.buttonAddAccount) on the welcome view'],
  needs_state=state_text('the account list is empty, so the welcome view with the add account button is shown (HomeFragment.java:793-794)', ('account',)),
  evidence='SRC home/HomeFragment.java:611-623 (btnAddAccount listener 614-622; intent 618-620); SRC home/HomeFragment.java:790-796 (welcome view visible when the list is empty, 793-794)')

e('WatchlistFragment$7.onClick', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AccountEditActivity.class)) with KEY_ACCOUNT_ID and ACTION_EDIT',
  gui=['Tap the goto-account icon (R.id.imageViewGotoAccount) in the watchlist header'],
  evidence='SRC investment/watchlist/WatchlistFragment.java:572-581 (listener 573-581; intent 576-579)')

e('FilterDialogFragment$3.onClick', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AccountEditActivity.class)) with KEY_ACCOUNT_ID and ACTION_EDIT',
  gui=['Tap the edit button (R.id.editButton) in the account filter dialog'],
  evidence='SRC account/FilterDialogFragment.java:164-176 (editButton listener 168-175; intent 171-174)')

e('AccountTransactionListFragment$2.onClick', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(new Intent(getActivity(), AccountEditActivity.class)) with KEY_ACCOUNT_ID and ACTION_EDIT',
  gui=['Tap the goto-account icon (R.id.imageViewGotoAccount) in the account transaction list header'],
  evidence='SRC account/AccountTransactionListFragment.java:534-544 (listener 536-544; intent 539-542)')

e('AccountListFragment.startAccountListEditActivity(Integer)', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(intent) with KEY_ACCOUNT_ID and ACTION_EDIT, when accountId is not null',
  gui=['Open the context menu of an account in the account list and choose Edit'],
  guard='accountId is not null (AccountListFragment.java:306); the EDIT case is at AccountListFragment.java:127-128',
  evidence='SRC account/AccountListFragment.java:115-130 (EDIT case 127-128); SRC account/AccountListFragment.java:302-314 (intent 304; EDIT 306-308; startActivity 313)')

e('AccountListFragment.startAccountListEditActivity(Integer)', 'AccountEditActivity.<init>', 'INTENT',
  'startActivity(intent) with ACTION_INSERT, when accountId is null',
  gui=['Tap the add (floating action) button on the account list'],
  guard='accountId is null (AccountListFragment.java:309-310); reached from onFloatingActionButtonClicked (250-251) through the no-argument overload (293-294)',
  evidence='SRC account/AccountListFragment.java:248-253 (onFloatingActionButtonClicked 250-251); SRC account/AccountListFragment.java:291-314 (no-argument overload 293-294; INSERT 309-310; startActivity 313)')

# ---- lifecycle, framework, screen and result edges

e('AccountEditActivity.<init>', 'AccountEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1216; FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('AccountEditActivity.onCreate', 'S_ACCOUNT_EDIT', 'ENTERS',
  'the account edit form is shown',
  evidence='SRC account/AccountEditActivity.java:138 (setContentView R.layout.activity_account_edit)')

e('AccountEditActivity.onCreate', 'AccountEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:615-640 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu at 3388)')

e('AccountEditActivity.onCreate', 'AccountEditActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity when it is paused: ActivityThread.performPauseActivity calls callCallActivityOnSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3855-3876 (callCallActivityOnSaveInstanceState at 3875); FW-SRC core/java/android/app/ActivityThread.java:4713-4722; FW-SRC core/java/android/app/Instrumentation.java:1385-1386; FW-SRC core/java/android/app/Activity.java:1495-1501 (onSaveInstanceState at 1496)')

e('CurrencyListFragment.setResult', 'AccountEditActivity.onActivityResult', 'RESULT',
  'the currency list returns the checked currency and finishes: setResult(RESULT_OK), and the framework calls onActivityResult',
  guard='requestCode is RequestCodes.CURRENCY and resultCode is RESULT_OK (AccountEditActivity.java:150, 153); pick mode with a checked row (CurrencyListFragment.java:300-305)',
  evidence='SRC currency/list/CurrencyListFragment.java:298-320 (checked row loop 304-306; RESULT_OK at 314); SRC currency/list/CurrencyListFragment.java:330-341 (onListItemClick calls setResultAndFinish at 339); SRC common/BaseListFragment.java:177-180 (setResultAndFinish calls setResult and finish); SRC account/AccountEditActivity.java:393-395 (startActivityForResult with RequestCodes.CURRENCY); FW-SRC core/java/android/app/ActivityThread.java:4253-4264 (deliverResults calls dispatchActivityResult at 4264); FW-SRC core/java/android/app/Activity.java:7259-7266 (onActivityResult at 7266)')

e('CalculatorActivity.returnResult', 'AccountEditActivity.onActivityResult', 'RESULT',
  'the calculator returns the amount (save menu or equals key) and finishes: setResult(RESULT_OK), and the framework calls onActivityResult',
  guard='requestCode is RequestCodes.AMOUNT and resultCode is RESULT_OK (AccountEditActivity.java:150, 168-169)',
  evidence='SRC common/CalculatorActivity.java:435-445 (setResult RESULT_OK and finish at 443-444); SRC common/CalculatorActivity.java:145-150 (save menu calls returnResult at 149) and 247-250 (equals key calls returnResult at 249); SRC common/Calculator.java:77-83 (startActivityForResult at 79); SRC account/AccountEditActivity.java:304-307 (Calculator show with RequestCodes.AMOUNT); FW-SRC core/java/android/app/ActivityThread.java:4253-4264; FW-SRC core/java/android/app/Activity.java:7259-7266')

# ---- GUI edges from the screen

e('S_ACCOUNT_EDIT', 'AccountEditActivity.onOptionsItemSelected', 'GUI',
  'the framework calls onOptionsItemSelected for the save menu item (MenuHelper.save)',
  gui=['Tap the save (check) icon in the action bar'],
  evidence='SRC MenuHelper.java:37, 87-92 (save item added at 88); SRC account/AccountEditActivity.java:177-182 (menu built at 179); FW-SRC core/java/android/app/Activity.java:3439-3455 (onMenuItemSelected calls onOptionsItemSelected at 3450)')

e('S_ACCOUNT_EDIT', 'AccountEditActivity$1.onClick', 'GUI',
  'the calculator opens for the initial balance: Calculator.show(RequestCodes.AMOUNT)',
  gui=['Tap the initial balance amount (txtInitialBalance)'],
  evidence='SRC account/AccountEditActivity.java:301-309 (listener 301; onClick 303-308; Calculator show 304-307)')

e('S_ACCOUNT_EDIT', 'AccountEditActivity$2.onItemSelected', 'GUI',
  'an account type is picked in the account type spinner: mAccount.setType(...)',
  gui=['Choose an account type in the account type spinner'],
  guard='position is in range of mAccountTypeValues (AccountEditActivity.java:359)',
  evidence='SRC account/AccountEditActivity.java:356-364 (listener 356; onItemSelected 358-364); FW-SRC core/java/android/widget/Spinner.java:1184-1186 (drop-down click calls setSelection); FW-SRC core/java/android/widget/AdapterView.java:903-922 (selectionChanged dispatches the selection); FW-SRC core/java/android/widget/AdapterView.java:937-949 (fireOnSelected calls onItemSelected at 944); the setSelection path in AdapterView and AbsSpinner is not printed (source not read): INFERRED for that step')

e('S_ACCOUNT_EDIT', 'AccountEditActivity$3.onItemSelected', 'GUI',
  'an account status is picked in the status spinner: mAccount.setStatus(...)',
  gui=['Choose an account status (Open or Closed) in the status spinner'],
  guard='position is in range of mAccountStatusValues (AccountEditActivity.java:375)',
  evidence='SRC account/AccountEditActivity.java:372-380 (listener 372; onItemSelected 374-380); FW-SRC core/java/android/widget/Spinner.java:1184-1186; FW-SRC core/java/android/widget/AdapterView.java:903-922, 937-949; the setSelection path in AdapterView and AbsSpinner is not printed (source not read): INFERRED for that step')

e('S_ACCOUNT_EDIT', 'AccountEditActivity$10.onClick', 'GUI',
  'the favourite flag is toggled: setFavorite(!getFavorite()) and displayFavouriteStatus',
  gui=['Tap the favourite star icon (imageViewAccountFav)', 'Tap the favourite label (favouriteAccountTextView)'],
  evidence='SRC account/AccountEditActivity.java:531-542 (listener 532-539; onClick 535-538; setOnClickListener 540-541)')

# ---- Icepick (generated helper; the library is not in the dataset)

e('MmxBaseFragmentActivity.onCreate', 'AccountEditActivity$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State fields: the library loads the generated helper AccountEditActivity$$Icepick by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:58-76 (Icepick.restoreInstanceState at 74); SRC account/AccountEditActivity.java:59, 87, 92 (import and @State fields); the icepick library and its reflection are not in the dataset: INFERRED, source not read')

e('MmxBaseFragmentActivity.onCreate', 'AccountEditActivity$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:58-76 (Icepick.restoreInstanceState at 74); the icepick library is not in the dataset: INFERRED, source not read')

e('MmxBaseFragmentActivity.onCreate', 'AccountEditActivity$$Icepick.restore', 'FRAMEWORK',
  'Icepick calls the generated restore for the @State fields (mCurrencyName, mIsDefault)',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:58-76 (Icepick.restoreInstanceState at 74); SRC account/AccountEditActivity.java:87, 92 (@State fields); the icepick library is not in the dataset: INFERRED, source not read')

e('MmxBaseFragmentActivity.onSaveInstanceState', 'AccountEditActivity$$Icepick.save', 'FRAMEWORK',
  'Icepick calls the generated save for the @State fields (mCurrencyName, mIsDefault)',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at MmxBaseFragmentActivity.java:155)',
  evidence='SRC common/MmxBaseFragmentActivity.java:152-156 (Icepick.saveInstanceState at 155); SRC account/AccountEditActivity.java:87, 92 (@State fields); the icepick library is not in the dataset: INFERRED, source not read')

# ---- UNREACHABLE entries (kind, reason, source reference, confirmed_by)

sup(('MmxBaseFragmentActivity$1.onClick', 'AccountEditActivity.onActionCancelClick'))  # the cancel listener is registered only by CurrencyEditActivity (BudgetsActivity's toolbar.xml has no action_cancel), never on an AccountEditActivity

UNREACHABLE['AccountEditActivity.onActionCancelClick'] = (
  'no_trigger_in_app',
  'Overrides MmxBaseFragmentActivity.onActionCancelClick. The only app caller is the cancel listener that showStandardToolbarActions(View,int,int) registers (MmxBaseFragmentActivity.java:213-219). This activity does not register that listener: the call at AccountEditActivity.java:140 is commented out. The other callers of showStandardToolbarActions (CurrencyEditActivity.java:83, BudgetsActivity.java:48) belong to other activities. The cancel code in MmxBaseFragmentActivity.onOptionsItemSelected (118-122) is commented out, and the home branch (109-116) finishes the activity without calling it. No in-app route remains.',
  'account/AccountEditActivity.java:138-141, 212-216; common/MmxBaseFragmentActivity.java:107-131, 209-219; currency/CurrencyEditActivity.java:83; budget/BudgetsActivity.java:48',
  'SOURCE')

UNREACHABLE['AccountEditActivity$2.onNothingSelected'] = (
  'branch_never_taken',
  'AdapterView.fireOnSelected calls onNothingSelected only when the selected position is negative (AdapterView.java:941-947). The account type spinner gets its adapter from the fixed, non-empty accounttype_items array (7 items, arrays.xml:76-84) at AccountEditActivity.java:317, and the only setSelection call uses a position found in the value list (AccountEditActivity.java:319-321). The AbsSpinner and AdapterView.setSelection code is not printed (source not read), so the claim that a non-empty spinner always gets a valid selection is INFERRED.',
  'account/AccountEditActivity.java:317, 319-321, 356-370 (onNothingSelected 368-369); res/values/arrays.xml:76-84; FW-SRC core/java/android/widget/AdapterView.java:937-949',
  'INFERRED')

UNREACHABLE['AccountEditActivity$3.onNothingSelected'] = (
  'branch_never_taken',
  'Same reason for the account status spinner: fireOnSelected calls onNothingSelected only for a negative selected position (AdapterView.java:941-947). The adapter is set from fixed, non-empty arrays (accountstatus_items, 2 items, arrays.xml:91-94; accountstatus_values, arrays.xml:87-90) at AccountEditActivity.java:331-333, and the only setSelection call uses an index found in the value list (AccountEditActivity.java:336-337). The AbsSpinner and AdapterView.setSelection code is not printed (source not read): INFERRED.',
  'account/AccountEditActivity.java:331-337, 372-385 (onNothingSelected 383-384); res/values/arrays.xml:87-94; FW-SRC core/java/android/widget/AdapterView.java:937-949',
  'INFERRED')

# ---- part 007 (2026-10-29)
# ================================================================== batch 007 (label_007): com.money.manager.ex.account.AccountEditActivity (methods 41-52 of 52)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_007.md.
# Every edge below has a batch 007 method as its destination. Its source is the page S_ACCOUNT_EDIT (defined in part 006).
# The listener constructors ($4.<init> to $9.<init>) and the bytecode calls out of them are in auto_calls.json, so no CALL edge is written here.
# No method of this batch is UNREACHABLE, so there are no UNREACHABLE entries and no sup pairs.

# ---- AccountEditActivity$4: the currency field

e('S_ACCOUNT_EDIT', 'AccountEditActivity$4.onClick', 'GUI',
  'the currency field is tapped: startActivityForResult(ACTION_PICK) opens CurrencyListActivity with RequestCodes.CURRENCY',
  gui=['Tap the currency field (textViewSelectCurrency) on the account form'],
  evidence='SRC account/AccountEditActivity.java:390-397 (listener 390; onClick 392-396; startActivityForResult 395); res/layout/activity_account_edit.xml:138')

# ---- AccountEditActivity$5: the initial date text and the date picker

e('S_ACCOUNT_EDIT', 'AccountEditActivity$5.onClick', 'GUI',
  'the initial date text is tapped: a DatePickerDialog opens on the account initial date, with the listener from the field initialiser',
  gui=['Tap the date text between the two arrows on the account form'],
  evidence='SRC account/AccountEditActivity.java:400-421 (listener 400; onClick 407-420; DatePickerDialog 411-419); SRC account/AccountEditViewHolder.java:60 (txtInitialDate is textViewDate); res/layout/activity_account_edit.xml:207-215')

e('AccountEditActivity$5.onClick', 'AccountEditActivity$5.lambda$$0', 'FRAMEWORK',
  'the user taps OK in the date picker: DatePickerDialog.onClick calls the OnDateSetListener, which is this lambda, and the lambda body runs',
  gui=['Tap the date text, then tap OK in the date picker'],
  evidence='SRC account/AccountEditActivity.java:401-405 (lambda listener); SRC account/AccountEditActivity.java:411-417 (DatePickerDialog built with the listener); FW-SRC core/java/android/app/DatePickerDialog.java:88-90 (public constructor passes the listener on), 122 (BUTTON_POSITIVE set to this), 136 (listener stored), 164-172 (BUTTON_POSITIVE calls mDateSetListener.onDateSet at 171); INFERRED the dialog button dispatch to DatePickerDialog.onClick is not printed (AlertController not read)')

# ---- AccountEditActivity$6: previous-day arrow

e('S_ACCOUNT_EDIT', 'AccountEditActivity$6.onClick', 'GUI',
  'the previous-day arrow is tapped: the initial date moves back one day (MmxDate.minusDays(1)) and showDate runs',
  gui=['Tap the left arrow beside the initial date'],
  evidence='SRC account/AccountEditActivity.java:423-430 (listener 423; onClick 425-429); res/layout/activity_account_edit.xml:197-204 (previousDayButton)')

# ---- AccountEditActivity$7: next-day arrow

e('S_ACCOUNT_EDIT', 'AccountEditActivity$7.onClick', 'GUI',
  'the next-day arrow is tapped: the initial date moves forward one day (MmxDate.plusDays(1)) and showDate runs',
  gui=['Tap the right arrow beside the initial date'],
  evidence='SRC account/AccountEditActivity.java:432-439 (listener 432; onClick 434-438); res/layout/activity_account_edit.xml:218-222 (nextDayButton)')

# ---- AccountEditActivity$8: default-account checkbox

e('S_ACCOUNT_EDIT', 'AccountEditActivity$8.onCheckedChanged', 'GUI',
  'the default-account checkbox is tapped: the CheckBox changes its checked state and calls the listener, which sets mIsDefault and calls displayDefaultAccount',
  gui=['Tap the default-account checkbox'],
  evidence='SRC account/AccountEditActivity.java:512-518 (listener 512; onCheckedChanged 513-518); res/layout/activity_account_edit.xml:75-78 (defaultAccountCheckbox); INFERRED the CheckBox toggle and the call to the listener are not in fw_src (CompoundButton.java not read)')

# ---- AccountEditActivity$9: default-account text

e('S_ACCOUNT_EDIT', 'AccountEditActivity$9.onClick', 'GUI',
  'the default-account label text is tapped: mIsDefault is inverted and displayDefaultAccount runs',
  gui=['Tap the default-account label text next to the checkbox'],
  evidence='SRC account/AccountEditActivity.java:521-528 (listener 521; onClick 523-527); res/layout/activity_account_edit.xml:81-84 (defaultAccountText)')

# ---- part 009 (2026-10-29)
# ================================================================== batch 009 (label_009): AccountStatuses (5 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_009.md.
# No e(...) edge is written here: the four REACHABLE methods get their only incoming edges from
# auto_calls.json (USE_AUTO adds them, D7), and every caller is a method of another batch.

# ---- AccountStatuses.equalsName: no caller in the app (grep output: label_009.grep.txt)
UNREACHABLE['AccountStatuses.equalsName'] = (
  'no_trigger_in_app',
  'Public instance method (case-insensitive title comparison). No caller in the app: its name occurs only at its declaration and at AccountTypes.equalsName, a different method. No auto_calls.json call edge reaches it, and no layout or manifest names it.',
  'AccountStatuses.java:39-41; AccountTypes.java:59; label_009.grep.txt; auto_calls.json:72633-72635, 90036-90037',
  'SOURCE')

# ---- part 010 (2026-10-29)
# ================================================================== batch 010 (label_010): com.money.manager.ex.account.AccountTransactionListFragment (40 of its 56 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_010.md.
# Every edge below has a batch 010 method as its destination, except the ASYNC edge whose source is CalculateRunningBalanceTask2.onPostExecute (batch 012 owns that method and its route) and the GUI and ENTERS edges from the page this batch defines.
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here, except three interface forwards from AllDataListFragment that the bytecode does not record.
# Framework and library claims are INFERRED where the library source was not read (androidx Fragment, LoaderManager, EventBus, AppCompat).

# ---- screen: the account transaction list. Batch 011 reuses this key and does not redefine it.

SCREENS.update({
    'S_ACCOUNT_TRANSACTIONS': 'Account transaction list (AccountTransactionListFragment): the account header with the balances, the transaction list, the account spinner in the action bar, and the options menu (period, status, filters, add transaction, export to CSV)',
})

e('AccountTransactionListFragment.onCreateView', 'S_ACCOUNT_TRANSACTIONS', 'ENTERS',
  'the account transaction list is shown: the header is added and the transaction list fragment is placed in R.id.fragmentMain',
  evidence='SRC account/AccountTransactionListFragment.java:163, 170-174, 181; SRC account/AccountTransactionListFragment.java:850 (transaction.replace into R.id.fragmentMain)')

# ---- lifecycle of the fragment (androidx Fragment; library source not read: INFERRED)

e('AccountTransactionListFragment.<init>', 'AccountTransactionListFragment.onAttach', 'LIFECYCLE',
  'the FragmentManager attaches the fragment when the transaction that adds it commits (MainActivity.showFragment, MainActivity.java:768-773)',
  evidence='SRC account/AccountTransactionListFragment.java:102-103; SRC home/MainActivity.java:768-773; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onAttach', 'AccountTransactionListFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after onAttach',
  evidence='SRC account/AccountTransactionListFragment.java:129-136; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onCreate', 'AccountTransactionListFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC account/AccountTransactionListFragment.java:136, 155; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onCreateView', 'AccountTransactionListFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onCreateView',
  evidence='SRC account/AccountTransactionListFragment.java:155, 187; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onActivityCreated', 'AccountTransactionListFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after onActivityCreated',
  evidence='SRC account/AccountTransactionListFragment.java:187, 198; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onStart', 'AccountTransactionListFragment.onResume', 'LIFECYCLE',
  'the framework calls onResume after onStart',
  evidence='SRC account/AccountTransactionListFragment.java:198, 205; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onResume', 'AccountTransactionListFragment.onStop', 'LIFECYCLE',
  'the user leaves the screen: the framework pauses and then stops the fragment (the pause is not a method of this class)',
  evidence='SRC account/AccountTransactionListFragment.java:205, 218; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onResume', 'AccountTransactionListFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state when the activity leaves the foreground (the state is saved before the fragment stops)',
  evidence='SRC account/AccountTransactionListFragment.java:384-392; INFERRED androidx FragmentManager saves state through onSaveInstanceState (library source not read)')

e('AccountTransactionListFragment.onStop', 'AccountTransactionListFragment.onDestroy', 'LIFECYCLE',
  'the fragment is removed from its container (for example when MainActivity shows another fragment) and the framework destroys it',
  evidence='SRC account/AccountTransactionListFragment.java:218, 395; SRC home/MainActivity.java:768-773; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- EventBus: registered in onStart, the balance task posts the event from onPostExecute (library: INFERRED)

e('AccountTransactionListFragment.onStart', 'AccountTransactionListFragment.onEvent', 'REGISTER',
  'the fragment registers itself on EventBus in onStart; the @Subscribe method onEvent receives RunningBalanceCalculatedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at line 201, unregister at line 221, @Subscribe at line 409 (library source not read, INFERRED)',
  evidence='SRC account/AccountTransactionListFragment.java:198-202, 218-222, 407-413; INFERRED EventBus library source not read')

e('CalculateRunningBalanceTask2.onPostExecute', 'AccountTransactionListFragment.onEvent', 'ASYNC',
  'the balance task posts RunningBalanceCalculatedEvent on EventBus when it finishes; the registered fragment receives it in onEvent',
  guard='the fragment is registered: onStart has run and onStop has not (lines 201 and 221)',
  cls='non_standard', via='EventBus post at CalculateRunningBalanceTask2.java:99 to the subscriber registered in onStart (library source not read, INFERRED)',
  evidence='SRC account/CalculateRunningBalanceTask2.java:97-100 (post at 99); SRC account/AccountTransactionListFragment.java:409-413; INFERRED EventBus library source not read')

# ---- options menu: the page's menu items, the menu opening, and the framework rebuild after invalidateOptionsMenu

e('S_ACCOUNT_TRANSACTIONS', 'AccountTransactionListFragment.onOptionsItemSelected', 'GUI',
  'tap an options menu item of the account transaction list: period, transaction status, filter, add transaction or export to CSV',
  gui=['Tap an item of the options menu (period, status, filter, add transaction, export to CSV) on the account transaction list'],
  evidence='SRC account/AccountTransactionListFragment.java:237-245 (menu resources inflated), 286-320 (item dispatch); INFERRED androidx FragmentManager dispatches onOptionsItemSelected to the fragment (library source not read)')

e('S_ACCOUNT_TRANSACTIONS', 'AccountTransactionListFragment.onPrepareOptionsMenu', 'GUI',
  'open the options menu of the account transaction list: the framework prepares it before it is shown',
  gui=['Open the options menu of the account transaction list (overflow icon)'],
  evidence='SRC account/AccountTransactionListFragment.java:252-283; INFERRED androidx FragmentManager dispatches onPrepareOptionsMenu to the fragment (library source not read)')

e('AccountTransactionListFragment.refreshSettings', 'AccountTransactionListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'refreshSettings calls getActivity().invalidateOptionsMenu(), so the host activity rebuilds its options menu and the framework calls the fragment onCreateOptionsMenu',
  guard='the fragment has its options menu enabled: setHasOptionsMenu(true) at line 181',
  evidence='SRC account/AccountTransactionListFragment.java:181, 881-888 (invalidateOptionsMenu at 887); FW-SRC core/java/android/app/Activity.java:3512-3516 (platform invalidateOptionsMenu calls invalidatePanelMenu); INFERRED AppCompat delegate and androidx FragmentManager dispatch (library source not read)')

e('AccountTransactionListFragment.refreshSettings', 'AccountTransactionListFragment.onPrepareOptionsMenu', 'FRAMEWORK',
  'the same invalidateOptionsMenu call (line 887) makes the framework prepare the rebuilt options menu through onPrepareOptionsMenu',
  guard='the fragment has its options menu enabled: setHasOptionsMenu(true) at line 181',
  evidence='SRC account/AccountTransactionListFragment.java:181, 881-888; FW-SRC core/java/android/app/Activity.java:3512-3516; INFERRED AppCompat delegate and androidx FragmentManager dispatch (library source not read)')

# ---- loader callbacks. AllDataListFragment forwards its loader events to this fragment (the parent set at line 847).
# The bytecode of AllDataListFragment does not record these interface calls, so they are written here as CALL edges.

e('AllDataListFragment.onCreateLoader', 'AccountTransactionListFragment.onCreateLoader', 'CALL',
  'AllDataListFragment forwards onCreateLoader to this fragment, the parent set by setSearResultFragmentLoaderCallbacks (line 847)',
  guard='the parent callbacks are set: showTransactionsFragment runs before the list loads (lines 837-847)',
  evidence='SRC common/AllDataListFragment.java:219-221 (forward at 221); SRC account/AccountTransactionListFragment.java:847; interface call, not recorded in auto_calls.json')

# B6-SEARCH: plain AllDataListFragment.onLoadFinished -> AccountTransactionListFragment.onLoadFinished partitioned to @AccountTransactionListFragment in graph_def_mod/03.py (plain edge deleted; shared src lets a Search prefix claim the host onLoadFinished).

e('AllDataListFragment.onLoaderReset', 'AccountTransactionListFragment.onLoaderReset', 'CALL',
  'AllDataListFragment forwards onLoaderReset to this fragment (line 255); this fragment does nothing there',
  guard='the parent callbacks are set (line 847)',
  evidence='SRC common/AllDataListFragment.java:253-255 (forward at 255); SRC account/AccountTransactionListFragment.java:349-351; interface call, not recorded in auto_calls.json')

e('AccountTransactionListFragment.onLoadFinished', 'AccountTransactionListFragment.onCreateLoader', 'FRAMEWORK',
  'getLoaderManager().restartLoader(ID_LOADER_SUMMARY, null, this) creates the summary loader through onCreateLoader (the loader manager calls the callbacks)',
  evidence='SRC account/AccountTransactionListFragment.java:370-373 (restartLoader at 373); INFERRED androidx LoaderManager.restartLoader calls LoaderCallbacks.onCreateLoader (library source not read)')

# ---- UNREACHABLE: no caller in the app (grep output: graphs/MMEX/parts/label_010.grep.txt)

UNREACHABLE['AccountTransactionListFragment.populateRunningBalanceRx'] = ('no_trigger_in_app',
  'private method with no caller in the app: the only occurrence of the name in the source root is its declaration (label_010.grep.txt). Its body only builds the query (line 653) and stops; the running balance is populated by populateRunningBalance (line 375), so nothing calls this method',
  'SRC account/AccountTransactionListFragment.java:649-656; grep label_010.grep.txt', 'SOURCE')

sup(('AccountTransactionListFragment.populateRunningBalanceRx', 'AccountTransactionListFragment.prepareQuery'))  # the bytecode call from this unreachable method cannot run

# ---- part 008 (2026-10-29)
# ================================================================== batch 008 (label_008): AccountListActivity, AccountListFragment (with its $1, $2, $3 listeners), AccountEditViewHolder and its ButterKnife binding, AccountSpinnerAdapter
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_008.md.
# Every edge below has a batch 008 method as its destination. GUI edges start on the page S_ACCOUNT_LIST; ENTERS edges end on it.
# Already in auto_calls.json, so not written here: AccountListActivity.onCreate -> AccountListFragment.<init> (AccountListActivity.java:47),
# AccountEditActivity.initializeControls -> AccountEditViewHolder.<init> (AccountEditActivity.java:294), the AccountListFragment action calls
# (startAccountListEditActivity, showDeleteConfirmationDialog, setResult), the $1/$2/$3 constructors, and the BaseListFragment calls that reach getSubTitle.
# AccountSpinnerAdapter is never instantiated in the app, so it has no incoming edge and no sup pair is needed.

SCREENS.update({
    'S_ACCOUNT_LIST': 'Account list: AccountListActivity (another app sends PICK or EDIT) or the Accounts screen opened from the navigation drawer; account names, the search box, the + button, and an Edit or Delete menu for each account',
})

# ---- AccountListActivity: started only by another app (exported PICK or EDIT intent, manifest 198-203); no in-app start (label_008.grep.txt)

e('S_ENTRY', 'AccountListActivity.<init>', 'ENTRY',
  'another app sends an ACTION_PICK or ACTION_EDIT intent to the exported AccountListActivity',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to AccountListActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:198-203; FW-SRC core/java/android/app/ActivityThread.java:2665-2672; FW-SRC core/java/android/app/Instrumentation.java:1143-1148')

e('S_ENTRY', 'AccountListActivity.<clinit>', 'ENTRY',
  'the first AccountListActivity instance (the exported-intent start above) initialises the class; FRAGMENTTAG (line 37) is computed at run time, so the static initialiser runs',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to AccountListActivity (exported=true)', ('other_app',)),
  evidence='SRC account/AccountListActivity.java:35-37; SRC AndroidManifest.xml:198-203; INFERRED the JVM runs a static initialiser before the first instance (Java language rule, not read from a source)')

e('AccountListActivity.<init>', 'AccountListActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC account/AccountListActivity.java:39-57')

e('AccountListActivity.onCreate', 'S_ACCOUNT_LIST', 'ENTERS',
  'the account list is shown in the activity',
  evidence='SRC account/AccountListActivity.java:47-55')

e('AccountListActivity.onCreate', 'AccountListFragment.onActivityCreated', 'FRAMEWORK',
  'the fragment is committed (line 55); the FragmentManager calls onActivityCreated later, in the fragment lifecycle',
  evidence='SRC account/AccountListActivity.java:47-55; INFERRED androidx FragmentManager calls onActivityCreated after the transaction commits (library not read)')

gui('S_ACCOUNT_LIST', 'AccountListActivity.onKeyUp', 'Press Back while the activity opened by another app is in front',
  evidence='FW-SRC core/java/android/app/Activity.java:3255-3272; FW-SRC core/java/android/view/KeyEvent.java:2709-2715; SRC account/AccountListActivity.java:59-68')

# ---- AccountListFragment: the drawer route (MainActivity drawer item menu_account, auto_calls) -> showFragment(Class) -> reflection

e('MainActivity.showFragment(Class)', 'AccountListFragment.<init>', 'CALL',
  'the drawer item Accounts (R.id.menu_account) calls showFragment(AccountListFragment.class), which creates the fragment with classFragment.newInstance()',
  cls='non_standard', via='Class.newInstance reflection in MainActivity.showFragment(Class) (MainActivity.java:743)',
  gui=['Open the navigation drawer and tap Accounts'],
  evidence='SRC home/MainActivity.java:633-634 (case R.id.menu_account); SRC home/MainActivity.java:734-752 (newInstance at 743); SRC home/MainActivity.java:863-866 (drawer item menu_account)')

# W4 REAUDIT (Kiro, MMEX-03): the plain edge MainActivity.showFragment_Internal -> AccountListFragment.onActivityCreated
# is replaced by the @ACCOUNTS clone at the end of this file. The shared helper commits whatever fragment its caller
# passed, so the plain edge let the Portfolio event route (a PortfolioFragment) reach the account list.

e('AccountListFragment.onActivityCreated', 'S_ACCOUNT_LIST', 'ENTERS',
  'the Accounts list is shown in the main screen (the fragment is set up in onActivityCreated)',
  evidence='SRC account/AccountListFragment.java:63-96')

# ---- AccountListFragment: loader lifecycle (androidx LoaderManager; library not read)

e('AccountListFragment.onActivityCreated', 'AccountListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader starts the account loader and the LoaderManager calls onCreateLoader; restartLoader (lines 216 and 277) calls it again after a search or a delete',
  evidence='SRC account/AccountListFragment.java:90, 216, 277; INFERRED androidx LoaderManager.initLoader calls the LoaderCallbacks (library not read)')

e('AccountListFragment.onCreateLoader', 'AccountListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader (MmxCursorLoader) delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC account/AccountListFragment.java:157-175; SRC common/MmxCursorLoader.java:32; INFERRED androidx Loader delivers its result to the callbacks (library not read)')

e('AccountListFragment.onLoadFinished', 'AccountListFragment.onLoaderReset', 'FRAMEWORK',
  'a loader that has delivered data is reset (fragment destroyed or loader restarted) and the LoaderManager calls onLoaderReset',
  evidence='SRC account/AccountListFragment.java:178-184; INFERRED androidx LoaderManager calls onLoaderReset when a loader with data is destroyed (library not read; FW-SRC has no LoaderManager.java)')

# ---- AccountListFragment: the context menu (registered in onActivityCreated, line 84)

e('AccountListFragment.onListItemClick', 'AccountListFragment.onCreateContextMenu', 'FRAMEWORK',
  'openContextMenu(v) (line 259) asks the framework to show the context menu; the framework calls the fragment, the listener set by registerForContextMenu (line 84), to fill the menu',
  evidence='SRC account/AccountListFragment.java:84, 255-260; FW-SRC core/java/android/app/Activity.java:3791-3793; FW-SRC core/java/android/view/View.java:6448-6449 and 12578-12588; FW-SRC core/java/android/view/ViewGroup.java:860-866; FW-SRC core/java/com/android/internal/policy/DecorView.java:796-797 (window-level path after that not read); FW-SRC core/java/android/app/Fragment.java:1937-1938 (registerForContextMenu sets the listener; androidx version INFERRED)')

gui('S_ACCOUNT_LIST', 'AccountListFragment.onContextItemSelected', 'Tap Edit or Delete in the menu of an account row',
  evidence='SRC account/AccountListFragment.java:114-152; FW-SRC core/java/android/app/Activity.java:3466-3473 (FEATURE_CONTEXT_MENU: onContextItemSelected at 3470, then mFragments.dispatchContextItemSelected at 3473); INFERRED androidx FragmentManager dispatches the item to the fragment (library not read)')

# ---- AccountListFragment: user actions on the list

gui('S_ACCOUNT_LIST', 'AccountListFragment.onListItemClick', 'Tap an account row',
  evidence='SRC account/AccountListFragment.java:255-260; auto_calls record AbsListFragment$1.onItemClick -> AccountListFragment.onListItemClick (AbsListFragment.java:44)')

gui('S_ACCOUNT_LIST', 'AccountListFragment.onFloatingActionButtonClicked', 'Tap the + button',
  evidence='SRC account/AccountListFragment.java:94-95, 250-252; auto_calls record BaseListFragment$2.onClick -> AccountListFragment.onFloatingActionButtonClicked (BaseListFragment.java:244)')

gui('S_ACCOUNT_LIST', 'AccountListFragment.onQueryTextChange', 'Type in the search box of the account list',
  evidence='SRC account/AccountListFragment.java:214-218; auto_calls record BaseListFragment.onPreQueryTextChange@AccountListFragment -> AccountListFragment.onQueryTextChange (BaseListFragment.java:226)')

# ---- AccountListFragment$1, $2, $3: the dialog listeners of the delete flow
# $1 = OK of the in-use message (captures only the fragment, descriptor (AccountListFragment)V); $2 = Cancel of the delete confirmation
# (captures only the fragment); $3 = OK of the delete confirmation (captures accountId, descriptor (AccountListFragment,I)V, and calls AccountRepository.delete).
# The auto_calls line table puts the $3 constructor at line 268 and the $2 constructor at line 269; the source order is the listener order, so the table is not used for the citation.

gui('S_ACCOUNT_LIST', 'AccountListFragment$1.onClick', 'Tap Delete on an account that is used, then tap OK on the message',
  evidence='SRC account/AccountListFragment.java:131-145 (isAccountUsed 133; OK listener 138-143; dismiss 141); method_list descriptor AccountListFragment$1.<init>(Lcom/money/manager/ex/account/AccountListFragment;)V')

gui('S_ACCOUNT_LIST', 'AccountListFragment$2.onClick', 'Tap Delete on an account, then tap Cancel on the confirmation',
  evidence='SRC account/AccountListFragment.java:280-285 (negative listener; cancel at 283); method_list descriptor AccountListFragment$2.<init>(Lcom/money/manager/ex/account/AccountListFragment;)V')

gui('S_ACCOUNT_LIST', 'AccountListFragment$3.onClick', 'Tap Delete on an account, then tap OK on the confirmation',
  evidence='SRC account/AccountListFragment.java:269-279 (positive listener; delete 273; restart 277); auto_calls record AccountListFragment$3.onClick -> AccountRepository.delete (AccountListFragment.java:273); method_list descriptor AccountListFragment$3.<init>(Lcom/money/manager/ex/account/AccountListFragment;I)V')

# ---- AccountEditViewHolder: the ButterKnife binding is built by reflection (library and generated source not read)

e('AccountEditViewHolder.<init>', 'AccountEditViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, parent) constructs the generated binding for this holder',
  cls='non_standard', via='ButterKnife.bind(this, parent) (library): the generated AccountEditViewHolder_ViewBinding is constructed by reflection (INFERRED, library and generated source not read)',
  evidence='SRC account/AccountEditViewHolder.java:38-40; method_list descriptor AccountEditViewHolder_ViewBinding.<init>(Lcom/money/manager/ex/account/AccountEditViewHolder;Landroid/view/View;)V; INFERRED generated class not in the source root')

# ================================================================== UNREACHABLE (batch 008)

UNREACHABLE['AccountEditViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root): ButterKnife.bind(this, parent) at AccountEditViewHolder.java:39 discards the returned Unbinder, the holder never calls unbind, and no caller record exists in auto_calls.json (label_008.grep.txt)',
  'SRC account/AccountEditViewHolder.java:38-40; label_008.grep.txt; python-printed auto_calls query (0 callers)',
  'INFERRED')

UNREACHABLE['AccountSpinnerAdapter.<init>'] = ('no_trigger_in_app',
  'the class is never instantiated in the app: the only mention outside its own file is the todo comment at SingleAccountWidgetConfigureActivity.java:142, so the constructor has no caller (label_008.grep.txt)',
  'SRC account/AccountSpinnerAdapter.java:30; SRC widget/SingleAccountWidgetConfigureActivity.java:142; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getCount'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:76; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getDropDownView'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:45; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getItem'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:88; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getItemId'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:99; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getItemViewType'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:149; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getView'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:133; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.getViewTypeCount'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:168; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.hasStableIds'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:110; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.isEmpty'] = ('no_trigger_in_app',
  'SpinnerAdapter override on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:179; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.registerDataSetObserver'] = ('no_trigger_in_app',
  'DataSetObserver registration on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:55; label_008.grep.txt',
  'SOURCE')

UNREACHABLE['AccountSpinnerAdapter.unregisterDataSetObserver'] = ('no_trigger_in_app',
  'DataSetObserver unregistration on an instance that is never created (AccountSpinnerAdapter.<init> has no caller, label_008.grep.txt); no layout or other class names the adapter',
  'SRC account/AccountSpinnerAdapter.java:66; label_008.grep.txt',
  'SOURCE')

# ---- part 012 (2026-10-29)
# ================================================================== batch 012 (label_012): AccountTransactionsListViewHolder, AccountTypes, CalculateRunningBalanceTask2, FilterDialogFragment (27 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_012.md.
# Every edge below has a batch 012 method as its destination, or is the ENTERS edge to the dialog page this batch defines.
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here.
# Framework claims cite FW-SRC lines printed for this batch; androidx DialogFragment claims are INFERRED (source not in the dataset).

SCREENS.update({
    'S_ACCOUNT_FILTER_DIALOG': 'Account filter dialog (FilterDialogFragment), opened from the filter item of the account transactions list menu: account name, record count, edit and favourite buttons, OK and Cancel',
})

# ---- dialog lifecycle and the screen

e('FilterDialogFragment.<init>', 'FilterDialogFragment.onCreate', 'LIFECYCLE',
  'the framework calls onCreate for the fragment instance created by newInstance, when the dialog is shown (AccountTransactionListFragment.java:831)',
  evidence='SRC account/FilterDialogFragment.java:82-95 (onCreate reads the arguments at 85-89); androidx DialogFragment and FragmentManager are not in the dataset: INFERRED, source not read')

e('FilterDialogFragment.onCreate', 'FilterDialogFragment.onCreateDialog', 'LIFECYCLE',
  'the framework calls onCreateDialog after onCreate, when the dialog is shown',
  evidence='SRC account/FilterDialogFragment.java:111 (onCreateDialog); androidx DialogFragment calls onCreateDialog from its layout inflater path: not in the dataset, INFERRED, source not read')

e('FilterDialogFragment.onCreateDialog', 'S_ACCOUNT_FILTER_DIALOG', 'ENTERS',
  'the account filter dialog is shown',
  evidence='SRC account/FilterDialogFragment.java:135-136 (AlertDialog create and show at 135-136)')

# ---- AsyncTask: the background calculation and the result callback (framework)

e('AccountTransactionListFragment.populateRunningBalance', 'CalculateRunningBalanceTask2.doInBackground', 'FRAMEWORK',
  'task.execute() starts the AsyncTask: the framework runs doInBackground on its background worker',
  evidence='SRC account/AccountTransactionListFragment.java:644 (task.execute()); FW-SRC core/java/android/os/AsyncTask.java:594-595 (execute calls executeOnExecutor with sDefaultExecutor), 632-651 (executeOnExecutor; exec.execute(mFuture) at 651), 330-333 (the worker calls doInBackground at 333), 403 (abstract doInBackground)')

e('CalculateRunningBalanceTask2.doInBackground', 'CalculateRunningBalanceTask2.onPostExecute', 'FRAMEWORK',
  'the framework posts the result to the main thread, and finish calls onPostExecute when the task is not cancelled',
  evidence='FW-SRC core/java/android/os/AsyncTask.java:369-373 (postResult sends MESSAGE_POST_RESULT), 705-713 (handleMessage calls finish at 712), 691-696 (finish calls onPostExecute at 695); FW-SRC AsyncTask.java:429 (default onPostExecute); SRC account/CalculateRunningBalanceTask2.java:88-95 (doInBackground returns the result of runTask)')

# ---- GUI edges from the dialog page: the framework dispatches the button clicks

e('S_ACCOUNT_FILTER_DIALOG', 'FilterDialogFragment$1.onClick', 'GUI',
  'the OK button of the dialog: the listener body is empty (todo at line 124)',
  gui=['Tap OK (android.R.string.ok) in the account filter dialog'],
  evidence='SRC account/FilterDialogFragment.java:120-126 (positive listener 121-126); FW-SRC android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC com/android/internal/app/AlertController.java:1022-1023 (setButton with a null message), 347-349 (setButton builds the message), 128-147 (the button click sends the message), 166 (ButtonHandler calls onClick); the View click dispatch is not printed (source not read): INFERRED for that step')

e('S_ACCOUNT_FILTER_DIALOG', 'FilterDialogFragment$2.onClick', 'GUI',
  'the Cancel button of the dialog: dismisses the dialog',
  gui=['Tap Cancel (android.R.string.cancel) in the account filter dialog'],
  evidence='SRC account/FilterDialogFragment.java:127-132 (negative listener 127-132; dismiss at 130); FW-SRC android/app/AlertDialog.java:637-639 (setNegativeButton stores the listener); FW-SRC com/android/internal/app/AlertController.java:1026-1027, 347-349, 128-147, 166 (same dispatch as OK); the View click dispatch is not printed: INFERRED for that step')

e('S_ACCOUNT_FILTER_DIALOG', 'FilterDialogFragment$3.onClick', 'GUI',
  'the edit button in the dialog: the listener starts AccountEditActivity (the INTENT edge into the activity is written by batch 006)',
  gui=['Tap the edit button (R.id.editButton) in the account filter dialog'],
  evidence='SRC account/FilterDialogFragment.java:167-176 (editButton listener 168-176; intent 171-174; startActivity 174); the View click dispatch is not printed (source not read): INFERRED for that step')

e('S_ACCOUNT_FILTER_DIALOG', 'FilterDialogFragment$4.onClick', 'GUI',
  'the favourite button: toggles the account favourite flag, saves the account and redraws the star',
  gui=['Tap the favourite button (R.id.favouriteButton) in the account filter dialog'],
  evidence='SRC account/FilterDialogFragment.java:183-199 (favouriteButton listener 184-199; onClick 185-198; save at 192; alert at 194; showFavouriteStatus at 197); the View click dispatch is not printed (source not read): INFERRED for that step')

# ---- UNREACHABLE entries (kind, reason, source reference, confirmed_by)

UNREACHABLE['AccountTypes.equalsName'] = (
  'no_trigger_in_app',
  'Public instance method (case-insensitive comparison of the title). No caller in the app: its name occurs only at its declaration (AccountTypes.java:59) and at AccountStatuses.equalsName (AccountStatuses.java:39), a different method. grep finds no call site and no method reference (label_012.grep.txt). auto_calls.json has no call edge into it: the only entries are the outgoing framework call String.equalsIgnoreCase (framework_calls, lines 72968-72970) and the impl index (lines 90301-90303). Source is app code, so the label is SOURCE.',
  'AccountTypes.java:59-61; AccountStatuses.java:39; label_012.grep.txt; auto_calls.json:72968-72970, 90301-90303',
  'SOURCE')

# ---- part 011 (2026-10-29)
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

# ---- part 014 (2026-10-29)
# ================================================================== batch 014 (label_014): AllDataAdapter, AllDataViewHolder (24 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_014.md.
# Every edge below has a batch 014 method as its destination (newView or bindView).
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here.
# Framework claims cite FW-SRC lines printed for this batch. The app imports androidx.cursoradapter.widget.CursorAdapter
# (AllDataAdapter.java:47), which is not in the dataset: its claims are INFERRED from the android.widget.CursorAdapter source.

# ---- all-data list: changeCursor relays out the list, the framework calls getView -> newView / bindView

e('AllDataListFragment.onLoadFinished', 'AllDataAdapter.newView', 'FRAMEWORK',
  'adapter.changeCursor(data) (AllDataListFragment.java:269) swaps in the new cursor and notifies the list; the list relayouts and the framework calls getView, which calls newView for a row that has no scrap view (the first layout of the data)',
  evidence='SRC common/AllDataListFragment.java:266-269 (changeCursor at 269); androidx CursorAdapter: not in the dataset, INFERRED to match FW-SRC core/java/android/widget/CursorAdapter.java:348-353 (changeCursor calls swapCursor), 365-381 (swapCursor calls notifyDataSetChanged at 381), 276-289 (getView calls newView at 285 when convertView is null); FW-SRC core/java/android/widget/BaseAdapter.java:51-53 (notifyDataSetChanged); DataSetObservable is not in fw_src: INFERRED that notifyChanged calls onChanged on each observer; FW-SRC core/java/android/widget/AdapterView.java:833-848 (AdapterDataSetObserver.onChanged calls requestLayout at 848); FW-SRC core/java/android/widget/ListView.java:578-579 (observer registered in setAdapter), 1624 (layoutChildren), 1784-1803 (fill methods), 2037-2052 (makeAndAddView calls obtainView at 2052); FW-SRC core/java/android/widget/AbsListView.java:2151-2164 (onLayout calls layoutChildren at 2164), 2335-2368 (obtainView calls getView at 2348 and 2365), 6796-6807 (getScrapView returns null when no scrap view is kept; retrieveFromScrap not printed: INFERRED that it returns null for an empty list)')

e('AllDataListFragment.onLoadFinished', 'AllDataAdapter.bindView', 'FRAMEWORK',
  'adapter.changeCursor(data) (AllDataListFragment.java:269) notifies the list; on the relayout the framework calls getView, which calls bindView for every visible row',
  evidence='SRC common/AllDataListFragment.java:266-269; androidx CursorAdapter INFERRED as above; FW-SRC core/java/android/widget/CursorAdapter.java:276-289 (getView calls bindView at 289), 365-381 (swapCursor calls notifyDataSetChanged at 381); FW-SRC core/java/android/widget/BaseAdapter.java:51-53; FW-SRC core/java/android/widget/AdapterView.java:833-848; FW-SRC core/java/android/widget/ListView.java:578-579, 1624, 1784-1803, 2037-2052; FW-SRC core/java/android/widget/AbsListView.java:2151-2164, 2335-2368')

# ---- recurring list: setListAdapter gives the list a new adapter; the framework calls getView -> newView / bindView

e('RecurringTransactionListFragment.onLoadFinished', 'AllDataAdapter.newView', 'FRAMEWORK',
  'setListAdapter(adapter) (RecurringTransactionListFragment.java:252) gives the list a new adapter; ListView.setAdapter resets the list and the list relayouts, and the framework calls getView, which calls newView for a row that has no scrap view',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:250-252; SRC AbsListFragment.java:253-257 (setListAdapter calls mList.setAdapter at 257); FW-SRC core/java/android/widget/ListView.java:552-558 (setAdapter: resetList at 557, mRecycler.clear at 558), 570 (super.setAdapter), 578-579 (observer), 603 (requestLayout); FW-SRC core/java/android/widget/AbsListView.java:2151-2164, 2335-2368 (getView at 2365 with scrapView from getScrapView at 2364), 6796-6807 (getScrapView returns null when no scrap view is kept; retrieveFromScrap not printed: INFERRED that it returns null for an empty list); FW-SRC core/java/android/widget/CursorAdapter.java:276-289 (getView calls newView at 285 when convertView is null); FW-SRC core/java/android/widget/ListView.java:1624, 1784-1803, 2037-2052; androidx CursorAdapter INFERRED as above')

e('RecurringTransactionListFragment.onLoadFinished', 'AllDataAdapter.bindView', 'FRAMEWORK',
  'setListAdapter(adapter) (RecurringTransactionListFragment.java:252) gives the list a new adapter; the list relayouts and the framework calls getView, which calls bindView for every visible row',
  evidence='SRC recurring/transactions/RecurringTransactionListFragment.java:250-252; SRC AbsListFragment.java:253-257; FW-SRC core/java/android/widget/ListView.java:552-558, 570, 578-579, 603; FW-SRC core/java/android/widget/AbsListView.java:2151-2164, 2335-2368; FW-SRC core/java/android/widget/CursorAdapter.java:276-289 (getView calls bindView at 289); androidx CursorAdapter INFERRED as above')

# ---- part 015 (2026-10-29)
# ================================================================== batch 015 (label_015): CategoryExpandableListAdapter (17 methods and its $1 listener), CategoryListItemViewHolderChild.<init>, CategoryListItemViewHolderGroup.<init>, MoneySimpleCursorAdapter (4 methods)

# ---- screen: the category list opened to pick a category (ACTION_PICK). Batches 029 and 030 reuse this key and do not redefine it.

SCREENS.update({
    'S_CATEGORY_LIST': 'Category list (CategoryListFragment): the expandable list of categories and subcategories. Opened to pick a category (ACTION_PICK), each top-level category row shows a selector icon',
})

# ---- picker mode: the selector icon of a top-level category row (shown only when the list was opened with ACTION_PICK)

e('S_CATEGORY_LIST', 'CategoryExpandableListAdapter$1.onClick', 'GUI',
  'tap the selector icon of a top-level category row in the category list opened to pick a category',
  gui=['Tap the selector icon on a top-level category row of the category list opened to pick a category'],
  guard='the list was opened with ACTION_PICK, so the selector is shown (CategoryListFragment.java:431; CategoryExpandableListAdapter.java:181)',
  evidence='SRC adapter/CategoryExpandableListAdapter.java:181-198 (selector visible and click listener set only when mShowSelector); SRC common/CategoryListFragment.java:431 (showSelector = mAction.equals(ACTION_PICK))')

# ---- framework-dispatched adapter callbacks. ExpandableListFragment.setListAdapter hands the adapter to the list view
# (mList.setAdapter, line 164). The framework then calls the callbacks below (ExpandableListView and its connector are not in
# fw_src and were not read: INFERRED). No auto_calls.json edge reaches these methods, so each gets one FRAMEWORK edge here.

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getChildView', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the view of each visible subcategory row',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getGroupView', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the view of each visible category row',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getChildId', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the id of each subcategory row',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getGroupId', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the id of each category row',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getGroup', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the category object at each group position',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.getGroupCount', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter for the number of category rows',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.hasStableIds', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter whether its ids are stable',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('ExpandableListFragment.setListAdapter', 'CategoryExpandableListAdapter.isChildSelectable', 'FRAMEWORK',
  'the list view takes the adapter (mList.setAdapter, line 164); the framework then asks the adapter whether a subcategory row is selectable',
  guard='the list view exists: mList is not null (ExpandableListFragment.java:163)',
  evidence='SRC common/ExpandableListFragment.java:160-164; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

# ---- MoneySimpleCursorAdapter.setViewText: the androidx SimpleCursorAdapter calls it while it binds each row of the account list.
# AccountListFragment.onLoadFinished gives the adapter its cursor (changeCursor, line 192). Library source not read: INFERRED.

e('AccountListFragment.onLoadFinished', 'MoneySimpleCursorAdapter.setViewText', 'FRAMEWORK',
  'the account loader delivers its cursor; onLoadFinished calls changeCursor (line 192) and the androidx SimpleCursorAdapter binds each row, calling setViewText for the mapped text view',
  guard='the cursor is from the account loader: loader.getId() == LOADER_ACCOUNT (AccountListFragment.java:188)',
  evidence='SRC account/AccountListFragment.java:187-192, 78-82 (text1 mapping at line 81); INFERRED androidx SimpleCursorAdapter.changeCursor -> bindView -> setViewText (library source not read)')

# ---- part 016 (2026-10-29)
# batch 016 (label_016): BudgetAdapter (17 methods), BudgetAdapter_MembersInjector (4), BudgetDetailFragment (10) and BudgetDetailFragment$1 (4); rows and printed lines: graphs/MMEX/parts/label_016.md.
# Page S_BUDGET_DETAIL is defined here (no budget page exists yet). CALL edges come from auto_calls.json, so none are written here. Dagger members are generated code (not in the source root): INFERRED; grep evidence in label_016.grep.txt.

SCREENS.update({
    'S_BUDGET_DETAIL': 'Budget detail (BudgetDetailFragment): the categories and subcategories of one budget, with the budgeted amount, the period, the actual amount and the amount available',
})

# ---- fragment lifecycle (androidx Fragment and BaseListFragment; library source not read: INFERRED)

e('BudgetDetailFragment.<init>', 'BudgetDetailFragment.onCreate', 'LIFECYCLE',
  'BudgetsActivity.showFragment commits the transaction that adds the fragment (line 175), and the FragmentManager then calls onCreate (onAttach is an androidx method and is not in this class)',
  evidence='SRC budget/BudgetDetailFragment.java:68, 78; SRC budget/BudgetsActivity.java:137, 140, 149-175; INFERRED androidx Fragment lifecycle (library source not read)')

e('BudgetDetailFragment.onCreate', 'BudgetDetailFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC budget/BudgetDetailFragment.java:78, 88; INFERRED androidx Fragment lifecycle (library source not read)')

e('BudgetDetailFragment.onCreateView', 'BudgetDetailFragment.onViewCreated', 'LIFECYCLE',
  'the framework calls onViewCreated after onCreateView; onViewCreated starts the budget loader (displayBudget)',
  evidence='SRC budget/BudgetDetailFragment.java:88, 121-122; INFERRED androidx Fragment lifecycle (library source not read)')

e('BudgetDetailFragment.onViewCreated', 'BudgetDetailFragment.onDestroyView', 'LIFECYCLE',
  'the framework destroys the view when the fragment is removed or replaced (BudgetsActivity.showFragment replaces R.id.fragmentMain or R.id.fragmentDetail) or the activity is destroyed',
  evidence='SRC budget/BudgetDetailFragment.java:113-118; SRC budget/BudgetsActivity.java:162, 165; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- the screen: the column header and the adapter are set up in onCreateView

e('BudgetDetailFragment.onCreateView', 'S_BUDGET_DETAIL', 'ENTERS',
  'the budget detail list is shown: the column header is added to the list and the BudgetAdapter is set on it (setUpAdapter, line 105)',
  evidence='SRC budget/BudgetDetailFragment.java:101-105, 145; SRC budget/BudgetAdapter.java:71-83')

# ---- loader callbacks (androidx LoaderManager; library not read: INFERRED)

e('BudgetDetailFragment.displayBudget', 'BudgetDetailFragment$1.onCreateLoader', 'FRAMEWORK',
  'initLoader (line 132) starts the budget detail loader and the LoaderManager calls onCreateLoader',
  evidence='SRC budget/BudgetDetailFragment.java:127-132, 149-160; INFERRED androidx LoaderManager.initLoader calls LoaderCallbacks.onCreateLoader (library not read)')

e('BudgetDetailFragment$1.onCreateLoader', 'BudgetDetailFragment$1.onLoadFinished', 'FRAMEWORK',
  'the loader (MmxCursorLoader, line 159) delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC budget/BudgetDetailFragment.java:151-159, 165; SRC common/MmxCursorLoader.java:39; INFERRED androidx Loader delivers its result to the callbacks (library not read)')

e('BudgetDetailFragment$1.onLoadFinished', 'BudgetDetailFragment$1.onLoaderReset', 'FRAMEWORK',
  'a loader that has delivered data is reset (fragment destroyed or loader restarted) and the LoaderManager calls onLoaderReset',
  evidence='SRC budget/BudgetDetailFragment.java:165-169, 180-184; INFERRED androidx LoaderManager calls onLoaderReset when a loader with data is destroyed (library not read)')

# ---- the list draws the rows after the cursor is set: changeCursor notifies the list, and the adapter views are made through CursorAdapter.getView

e('BudgetDetailFragment$1.onLoadFinished', 'BudgetAdapter.newView', 'FRAMEWORK',
  'adapter.changeCursor (line 169) notifies the list, which asks the adapter for row views; CursorAdapter.getView calls newView when there is no view to reuse',
  guard='the loader delivered a cursor: changeCursor (line 169) makes the adapter valid and it has rows',
  evidence='SRC budget/BudgetDetailFragment.java:165-169; SRC budget/BudgetAdapter.java:92-96; FW-SRC core/java/android/widget/CursorAdapter.java:276-289 (getView calls newView at 285 when convertView is null, then bindView at 289), 348-381 (changeCursor, swapCursor, notifyDataSetChanged at 381); INFERRED androidx CursorAdapter and ListView draw path (not in fw_src)')

e('BudgetDetailFragment$1.onLoadFinished', 'BudgetAdapter.bindView', 'FRAMEWORK',
  'the same notification: CursorAdapter.getView calls bindView for each visible row after changeCursor (line 169)',
  guard='the loader delivered a cursor: changeCursor (line 169) makes the adapter valid and it has rows',
  evidence='SRC budget/BudgetDetailFragment.java:165-169; SRC budget/BudgetAdapter.java:98-99; FW-SRC core/java/android/widget/CursorAdapter.java:276-289 (bindView at 289); INFERRED androidx CursorAdapter and ListView draw path (not in fw_src)')

# ---- auto edges that cannot run: their source has no caller or is UNREACHABLE (see the entries below)

sup(('BudgetAdapter.getAmountForSubCategory', 'BudgetAdapter.loadTotalFor'))  # getAmountForSubCategory has no caller, so this bytecode call cannot run
sup(('BudgetAdapter_MembersInjector.create', 'BudgetAdapter_MembersInjector.<init>'))  # create has no caller, so the constructor call cannot run
sup(('BudgetAdapter_MembersInjector.injectMembers', 'BudgetAdapter_MembersInjector.injectDatabaseLazy'))  # injectMembers has no caller, so this call cannot run

# ---- UNREACHABLE: no caller in the app (grep output: graphs/MMEX/parts/label_016.grep.txt)

UNREACHABLE['BudgetAdapter.getAmountForSubCategory'] = (
  'no_trigger_in_app',
  'private method with no caller in the app: its only occurrences in the source root are the declaration (line 260) and a commented-out call in getActualAmount (line 214). getActualAmount calls getAmountForCategory in both branches (lines 210 and 213), and the bytecode call graph has no edge into it (label_016.grep.txt)',
  'budget/BudgetAdapter.java:204-217, 255-263; grep label_016.grep.txt',
  'SOURCE')

UNREACHABLE['BudgetAdapter_MembersInjector.<init>'] = (
  'no_trigger_in_app',
  'constructor of the Dagger members injector, reached only from create (auto_calls.json:58029-58036). create has no caller (see BudgetAdapter_MembersInjector.create), so the constructor never runs. Generated code: INFERRED.',
  'auto_calls.json:58029-58036; graphs/MMEX/parts/label_016.grep.txt',
  'INFERRED')

UNREACHABLE['BudgetAdapter_MembersInjector.create'] = (
  'no_trigger_in_app',
  'static factory of the Dagger members injector with no caller: no edge in the bytecode call graph has it as a callee (grep: no dst match). The component injects statically: injectBudgetAdapter calls injectDatabaseLazy directly (auto_calls.json:19175-19182), so no injector object is built. Generated code, not in the source root: INFERRED.',
  'auto_calls.json:58029-58036, 19175-19182; graphs/MMEX/parts/label_016.grep.txt',
  'INFERRED')

UNREACHABLE['BudgetAdapter_MembersInjector.injectMembers'] = (
  'no_trigger_in_app',
  'instance method of the Dagger members injector. It is reached only through the MembersInjector interface on an injector object that create would make, and create has no caller. No call to any injectMembers appears in the bytecode call graph (grep: no dst match), and the component injects statically through injectDatabaseLazy (auto_calls.json:19175-19182). Generated code: INFERRED.',
  'auto_calls.json:58037-58044, 19175-19182; graphs/MMEX/parts/label_016.grep.txt',
  'INFERRED')

# ---- part 013 (2026-10-29)
# ================================================================== batch 013 (label_013): StatusFilter (its parceler wrapper and creator), TransactionFilter (its wrapper and creator), RunningBalanceCalculatedEvent.<init>
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_013.md.
# Grep evidence for the no-caller UNREACHABLE claims: graphs/MMEX/parts/label_013.grep.txt.
# The parceler wrappers (StatusFilter$$Parcelable, TransactionFilter$$Parcelable and their $1 creators) are generated by parceler and are not in the source root (INFERRED).
# The edges written here are the hops the bytecode does not record: Parcels.wrap and Parcels.unwrap (parceler reflection and interface calls, INFERRED), and the framework parcel round trip of the FilterDialogFragment arguments (FW-SRC lines in the evidence).
# CALL edges already in auto_calls.json are not written here (D7).
# The sup pairs drop the bytecode calls that start in an UNREACHABLE method (they cannot run), as label_010.py does.

# ---- FilterDialogFragment.newInstance wraps the filter with Parcels.wrap (FilterDialogFragment.java:73)

e('FilterDialogFragment.newInstance', 'TransactionFilter$$Parcelable.<clinit>', 'CALL',
  'Parcels.wrap loads the generated wrapper class by name, which runs its static initialiser (it creates the CREATOR field)',
  cls='non_standard', via='Parcels.wrap(filter) at FilterDialogFragment.java:73 (parceler library reflection: class load by name; library source not read, INFERRED)',
  evidence='SRC account/FilterDialogFragment.java:68-73; label_013.grep.txt (Parcels.wrap block); INFERRED parceler library source not read')

e('FilterDialogFragment.newInstance', 'TransactionFilter$$Parcelable.<init>', 'CALL',
  'Parcels.wrap constructs the wrapper around the filter (mFilter, created at AccountTransactionListFragment.java:143 and passed in by showFilterDialog)',
  cls='non_standard', via='Parcels.wrap(filter) at FilterDialogFragment.java:73 (parceler library reflection: constructor call; library source not read, INFERRED)',
  evidence='SRC account/FilterDialogFragment.java:68-73; SRC account/AccountTransactionListFragment.java:828-830; INFERRED parceler library source not read')

# ---- FilterDialogFragment.onCreate unwraps the filter with Parcels.unwrap (FilterDialogFragment.java:86)

e('FilterDialogFragment.onCreate', 'TransactionFilter$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the wrapper read from the arguments and returns the TransactionFilter',
  cls='non_standard', via='Parcels.unwrap(getArguments().getParcelable(ARG_TX_FILTER)) at FilterDialogFragment.java:86 (parceler library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC account/FilterDialogFragment.java:82-86; INFERRED parceler library source not read')

# ---- the framework parcel round trip of the dialog arguments (FilterDialogFragment.java:73 puts the wrapper in the arguments)

e('FilterDialogFragment.newInstance', 'TransactionFilter$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the dialog arguments hold the wrapper; when the framework saves the dialog state the bundle is parcelled, and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard', via='args.putParcelable(ARG_TX_FILTER, Parcels.wrap(filter)) at FilterDialogFragment.java:73; the FragmentManager saves the arguments (androidx, INFERRED: library source not read); Parcel.writeValue calls writeParcelable (FW-SRC Parcel.java:1697, 1785-1791), which calls p.writeToParcel (FW-SRC Parcel.java:1791)',
  evidence='SRC account/FilterDialogFragment.java:72-76; FW-SRC core/java/android/os/Parcel.java:1697, 1785-1791; INFERRED androidx FragmentManager saves the arguments (library not read)')

# B6-EVENT: plain FilterDialogFragment.onCreate -> TransactionFilter$$Parcelable$1.createFromParcel partitioned to @RESTORED in graph_def_mod/03.py (plain edge deleted; false for fresh Bundle — FW-SRC Bundle.java:938-939 returns the map object without creator).

# ---- sup: bytecode calls that start in an UNREACHABLE method cannot run, so they are dropped

sup(('StatusFilter.add', 'TransactionStatuses.<clinit>'), ('StatusFilter.add', 'TransactionStatuses.getCode'), ('StatusFilter.add', 'TransactionStatuses.from'),
    ('StatusFilter.remove', 'TransactionStatuses.<clinit>'), ('StatusFilter.remove', 'TransactionStatuses.getCode'), ('StatusFilter.remove', 'TransactionStatuses.from'),
    ('StatusFilter.contains(String)', 'TransactionStatuses.<clinit>'), ('StatusFilter.contains(String)', 'TransactionStatuses.getCode'), ('StatusFilter.contains(String)', 'TransactionStatuses.from'),
    ('StatusFilter$$Parcelable.writeToParcel', 'StatusFilter$$Parcelable.write'),
    ('StatusFilter$$Parcelable$1.createFromParcel', 'StatusFilter$$Parcelable.<clinit>'), ('StatusFilter$$Parcelable$1.createFromParcel', 'StatusFilter$$Parcelable.<init>'), ('StatusFilter$$Parcelable$1.createFromParcel', 'StatusFilter$$Parcelable.read'))

# ================================================================== UNREACHABLE (batch 013)

UNREACHABLE['StatusFilter.add'] = ('no_trigger_in_app',
  'public instance method with no caller in the app: AccountTransactionListFragment calls only getSqlParameters (line 679) and contains(int) (line 799) on transactionStatus; it touches the filter list directly at lines 391, 579, 583 and 706 (ArrayList calls, not StatusFilter.add); no auto_calls.json record has StatusFilter.add as dst (label_013.grep.txt, StatusFilter and transactionStatus blocks)',
  'SRC account/StatusFilter.java:64-69; SRC account/AccountTransactionListFragment.java:391, 579, 583, 679, 706, 799; label_013.grep.txt',
  'SOURCE')

UNREACHABLE['StatusFilter.remove'] = ('no_trigger_in_app',
  'public instance method with no caller in the app: AccountTransactionListFragment calls only getSqlParameters (line 679) and contains(int) (line 799) on transactionStatus; it touches the filter list directly at lines 391, 579, 583 and 706 (ArrayList calls, not StatusFilter.remove); no auto_calls.json record has StatusFilter.remove as dst (label_013.grep.txt, StatusFilter and transactionStatus blocks)',
  'SRC account/StatusFilter.java:71-76; SRC account/AccountTransactionListFragment.java:391, 579, 583, 679, 706, 799; label_013.grep.txt',
  'SOURCE')

UNREACHABLE['StatusFilter.contains(String)'] = ('no_trigger_in_app',
  'public method with no caller in the app: the only call on transactionStatus with a status (line 799) passes an int menu id, so the contains(int) overload is chosen; no call passes a String (label_013.grep.txt); the only auto_calls.json dst record for StatusFilter.contains is contains(int)',
  'SRC account/StatusFilter.java:78-83; SRC account/AccountTransactionListFragment.java:797-799; label_013.grep.txt; auto_calls.json:44541',
  'SOURCE')

UNREACHABLE['StatusFilter$$Parcelable.<init>'] = ('no_trigger_in_app',
  'the constructor that wraps a StatusFilter. Its only in-app caller is StatusFilter$$Parcelable$1.createFromParcel (auto_calls.json:44797), and that creator is reached only through a parcel that holds a top-level StatusFilter wrapper. No such wrapper is built: StatusFilter is never passed to Parcels.wrap (label_013.grep.txt, Parcels block) and is held only as a nested field of TransactionFilter',
  'generated class not in the source root; label_013.grep.txt; auto_calls.json:44797; SRC account/TransactionFilter.java:34',
  'INFERRED')

UNREACHABLE['StatusFilter$$Parcelable.describeContents'] = ('framework_never_calls',
  'Bundle.hasFileDescriptors (FW-SRC Bundle.java:316-371) calls describeContents on the Parcelable values it checks (lines 329, 338, 349, 362), and Bundle.describeContents (Bundle.java:1215-1221) calls it at 1217. A StatusFilter wrapper is never placed in any bundle (StatusFilter is never passed to Parcels.wrap, label_013.grep.txt), and no app code calls describeContents (label_013.grep.txt, empty block). Whether any framework path reaches it is INFERRED (framework paths beyond these lines not read)',
  'FW-SRC core/java/android/os/Bundle.java:316-371, 1215-1221; label_013.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['StatusFilter$$Parcelable.getParcel'] = ('no_trigger_in_app',
  'returns the wrapped StatusFilter. Its only possible callers are Parcels.unwrap on a StatusFilter wrapper read from a bundle. The only app unwrap of a TransactionFilter wrapper is FilterDialogFragment.java:86 (line 87 unwraps the Account wrapper), and no StatusFilter wrapper is ever built, so no unwrap reaches a StatusFilter wrapper (label_013.grep.txt, Parcels block). No auto_calls.json record has getParcel as dst (the dst records for StatusFilter$$Parcelable are listed in label_013.grep.txt)',
  'label_013.grep.txt; SRC account/FilterDialogFragment.java:86-87',
  'INFERRED')

UNREACHABLE['StatusFilter$$Parcelable.writeToParcel'] = ('no_trigger_in_app',
  'the Parcelable write method. The framework calls it only from Parcel.writeParcelable (FW-SRC Parcel.java:1785-1791) for a wrapper object written into a parcel. No StatusFilter wrapper is written (no Parcels.wrap of a StatusFilter, label_013.grep.txt), and no auto_calls.json record has it as dst. Its only app call is to StatusFilter$$Parcelable.write (line 45), which is an outgoing call from this unreachable method (suppressed in label_013.py)',
  'FW-SRC core/java/android/os/Parcel.java:1785-1791; label_013.grep.txt; auto_calls.json:44765 (outgoing call to write, dst line); generated class not in the source root',
  'INFERRED')

UNREACHABLE['StatusFilter$$Parcelable$1.createFromParcel'] = ('no_trigger_in_app',
  'the framework calls createFromParcel only through Parcel.readParcelable (FW-SRC Parcel.java:2841-2851), for a parcel that names StatusFilter$$Parcelable as its creator class. That name is written only by Parcel.writeParcelable of a top-level StatusFilter wrapper, which never happens (label_013.grep.txt). No auto_calls.json record has createFromParcel as dst (label_013.grep.txt)',
  'FW-SRC core/java/android/os/Parcel.java:1785-1791, 2841-2851; label_013.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['StatusFilter$$Parcelable$1.newArray'] = ('framework_never_calls',
  'Creator method for typed arrays of StatusFilter wrappers. The framework calls it only when it reads a typed array of this class, and no array of StatusFilter wrappers is built or parcelled (label_013.grep.txt, newArray block: the only StatusFilter match is commented out at StatusFilter.java:59-60)',
  'SRC account/StatusFilter.java:59-60 (commented out); label_013.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['TransactionFilter$$Parcelable.describeContents'] = ('framework_never_calls',
  'Bundle.hasFileDescriptors (FW-SRC Bundle.java:316-371) calls describeContents on the Parcelable values it checks (lines 329, 338, 349, 362), and Bundle.describeContents (Bundle.java:1215-1221) calls it at 1217. No app code calls describeContents (label_013.grep.txt, empty block). The TransactionFilter wrapper is in the FilterDialogFragment arguments (FilterDialogFragment.java:73); whether the framework checks that bundle for file descriptors is INFERRED (framework and androidx paths beyond these lines not read)',
  'FW-SRC core/java/android/os/Bundle.java:316-371, 1215-1221; SRC account/FilterDialogFragment.java:73; label_013.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['TransactionFilter$$Parcelable$1.newArray'] = ('framework_never_calls',
  'Creator method for typed arrays of TransactionFilter wrappers. No array of TransactionFilter wrappers is built or parcelled (label_013.grep.txt: the TransactionFilter block has no array use, and the newArray matches in the source root belong to other classes)',
  'label_013.grep.txt; generated class not in the source root',
  'INFERRED')

# ---- part 017 (2026-10-29)
# ================================================================== batch 017 (label_017): com.money.manager.ex.budget.BudgetEditActivity (with $1, $2), its ButterKnife binding (with $1, $2), BudgetEditViewHolder and its ButterKnife binding (30 methods)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_017.md.
# Every edge below has a batch 017 method as its destination, or is the ENTERS edge to the page this batch defines (S_BUDGET_EDIT).
# CALL edges come from auto_calls.json (USE_AUTO) and are not written here, except the two ButterKnife constructor calls that the bytecode does not record.
# Framework and library claims are INFERRED where the library source was not read (AppCompat, ButterKnife, AlertDialog). grep evidence: graphs/MMEX/parts/label_017.grep.txt.

SCREENS.update({
    'S_BUDGET_EDIT': 'Budget edit (BudgetEditActivity): the budget name, year and month fields, the save icon and the Up arrow in the toolbar, and the year and month pickers',
})

# ---- entry into the activity: started by the budget list only (not exported and no intent filter: AndroidManifest.xml:357, so no ENTRY edge)

e('BudgetListFragment.editBudget', 'BudgetEditActivity.<init>', 'INTENT',
  'editBudget starts BudgetEditActivity with ACTION_EDIT and the budget id (KEY_BUDGET_ID) through startActivityForResult',
  gui=['Open the context menu of a budget row in the budget list and choose Edit'],
  guard='the context-menu item is EDIT (switch case at line 189)',
  evidence='SRC budget/BudgetListFragment.java:186-190 (switch on the menu id; editBudget at 190), 238-244 (intent 239-241; startActivityForResult 243); SRC AndroidManifest.xml:357')

e('BudgetListFragment.createBudget', 'BudgetEditActivity.<init>', 'INTENT',
  'createBudget starts BudgetEditActivity with ACTION_INSERT through startActivityForResult',
  gui=['Tap the add button (floating action button) on the budget list'],
  evidence='SRC budget/BudgetListFragment.java:218-221 (onFloatingActionButtonClicked calls createBudget at 220), 246-250 (intent 247-248; startActivityForResult 249)')

e('BudgetEditActivity.<init>', 'BudgetEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/Instrumentation.java:1143 (newActivity), 1212-1215 (callActivityOnCreate); FW-SRC core/java/android/app/ActivityThread.java:2669, 2729-2731; SRC budget/BudgetEditActivity.java:43-44, 52-54')

# ---- the screen: onCreate sets the layout and fills the fields

e('BudgetEditActivity.onCreate', 'S_BUDGET_EDIT', 'ENTERS',
  'the budget edit form is shown: onCreate sets the layout (line 55) and binds the model to the fields (lines 61-62)',
  evidence='SRC budget/BudgetEditActivity.java:55, 61-62; SRC res/layout/activity_budget_edit.xml:65 (toolbar), 134 (budgetNameTextView), 173 (budgetYearTextView), 213 (budgetMonthTextView)')

# ---- ButterKnife bindings: the generated classes are built by reflection in ButterKnife.bind (library and generated source not read)

e('BudgetEditActivity.onCreate', 'BudgetEditActivity_ViewBinding.<init>(BudgetEditActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for this activity, which binds the @OnClick handlers and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated BudgetEditActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC budget/BudgetEditActivity.java:57; INFERRED ButterKnife generated binding (library and generated source not read); no auto_calls record has onCreate as src with this destination (label_017.grep.txt)')

e('BudgetEditViewHolder.<init>', 'BudgetEditViewHolder_ViewBinding.<init>', 'CALL',
  'ButterKnife.bind(this, activity) builds the generated binding for the holder, which binds the three text views',
  cls='non_standard', via='ButterKnife.bind(this, activity) (library): the generated BudgetEditViewHolder_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC budget/BudgetEditViewHolder.java:33-35 (bind at 34); INFERRED ButterKnife generated binding (library and generated source not read); no auto_calls record has BudgetEditViewHolder.<init> as src (label_017.grep.txt)')

e('S_BUDGET_EDIT', 'BudgetEditActivity_ViewBinding$1.doClick', 'GUI',
  'tap the year field (budgetYearTextView): the @OnClick listener attached by the generated binding calls onSelectYear',
  gui=['Tap the year field of the budget'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class)',
  evidence='SRC budget/BudgetEditActivity.java:98 (@OnClick budgetYearTextView); SRC res/layout/activity_budget_edit.xml:173; auto_calls.json:57838-57839 (doClick calls onSelectYear); auto_calls.json:57862-57863 (the binding constructor creates $1)')

e('S_BUDGET_EDIT', 'BudgetEditActivity_ViewBinding$2.doClick', 'GUI',
  'tap the month field (budgetMonthTextView): the @OnClick listener attached by the generated binding calls onSelectMonth',
  gui=['Tap the month field of the budget'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class)',
  evidence='SRC budget/BudgetEditActivity.java:129 (@OnClick budgetMonthTextView); SRC res/layout/activity_budget_edit.xml:213; auto_calls.json:57414-57415 (doClick calls onSelectMonth); auto_calls.json:57854-57855 (the binding constructor creates $2)')

# ---- options menu: the framework builds it after setContentView hands the toolbar to setSupportActionBar (AppCompat step INFERRED)

e('BudgetEditActivity.onCreate', 'BudgetEditActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'setContentView gives the toolbar to setSupportActionBar, and the framework then builds the options menu through onCreatePanelMenu, which calls onCreateOptionsMenu',
  guard='the layout has the toolbar (R.id.toolbar at activity_budget_edit.xml:65)',
  evidence='SRC common/MmxBaseFragmentActivity.java:99-104 (setContentView; setSupportActionBar at 103); SRC res/layout/activity_budget_edit.xml:65; FW-SRC core/java/android/app/Activity.java:3386-3388 (onCreatePanelMenu calls onCreateOptionsMenu); FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:631; INFERRED AppCompat builds the action-bar menu after setSupportActionBar (AppCompat not read)')

e('S_BUDGET_EDIT', 'BudgetEditActivity.onOptionsItemSelected', 'GUI',
  'tap the save icon in the toolbar (it runs onActionDoneClick, which saves the budget) or the Up arrow (the home item, logged and passed to the base class)',
  gui=['Tap the save icon in the toolbar, or the Up arrow'],
  guard='the save icon exists: onCreateOptionsMenu adds it (line 80)',
  evidence='SRC budget/BudgetEditActivity.java:76-83 (save icon via MenuHelper at 79-80), 86-96 (home at 88-91; save at 92-93); SRC MenuHelper.java:37 (save = 2), 87-94 (addSaveToolbarIcon; menu.add at 88); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected); INFERRED AppCompat dispatches the item to onOptionsItemSelected (library not read)')

# ---- the picker dialogs: the OK buttons reach the listeners (AlertDialog positive-button dispatch INFERRED)

e('S_BUDGET_EDIT', 'BudgetEditActivity$1.onClick', 'GUI',
  'tap OK in the year picker: the listener sets the year on the model and refreshes the year and the name',
  gui=['Tap OK in the year picker dialog'],
  guard='the year picker is open: onSelectYear shows it (line 126)',
  evidence='SRC budget/BudgetEditActivity.java:113-126 (AlertDialog built and shown; positive button 116-124; onClick 118-123); INFERRED AlertDialog positive-button dispatch (AlertController not read)')

e('S_BUDGET_EDIT', 'BudgetEditActivity$2.onClick', 'GUI',
  'tap OK in the month picker: the listener sets the month on the model and refreshes the month and the name',
  gui=['Tap OK in the month picker dialog'],
  guard='the month picker is open: onSelectMonth shows it (line 156)',
  evidence='SRC budget/BudgetEditActivity.java:143-156 (AlertDialog built and shown; positive button 146-154; onClick 148-153); INFERRED AlertDialog positive-button dispatch (AlertController not read)')

# ================================================================== UNREACHABLE (batch 017)

UNREACHABLE['BudgetEditActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root): ButterKnife.bind(this) at BudgetEditActivity.java:57 discards the Unbinder it returns (no unbind or Unbinder use in the source root), BudgetEditActivity has no onDestroy, and no call record in auto_calls.json has unbind as its destination (label_017.grep.txt)',
  'SRC budget/BudgetEditActivity.java:52-63; label_017.grep.txt; python-printed auto_calls query (0 unbind destinations in the calls section)',
  'INFERRED')

UNREACHABLE['BudgetEditViewHolder_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root): ButterKnife.bind(this, activity) at BudgetEditViewHolder.java:34 discards the Unbinder it returns, BudgetEditViewHolder has no unbind or onDestroy, and no call record in auto_calls.json has unbind as its destination (label_017.grep.txt)',
  'SRC budget/BudgetEditViewHolder.java:33-35; label_017.grep.txt; python-printed auto_calls query (0 unbind destinations in the calls section)',
  'INFERRED')

sup(('MmxBaseFragmentActivity$2.onClick', 'BudgetEditActivity.onActionDoneClick'))  # the done listener is installed only by CurrencyEditActivity (BudgetsActivity's toolbar.xml has no action_done view), and BudgetEditActivity has neither the call nor an action_done view

# ---- part 019 (2026-10-29)
# batch 019 (label_019): BudgetViewModel (9 methods), BudgetsActivity (11) and BudgetSelectedEvent (1); rows and printed lines: graphs/MMEX/parts/label_019.md.
# Page S_BUDGETS is defined here (no budget-list page exists yet). CALL edges come from auto_calls.json, so none are written here; the BudgetViewModel methods are reached through BudgetEditActivity (another batch). Framework and EventBus claims are INFERRED where the library source was not read; grep evidence is in label_019.grep.txt.

SCREENS.update({
    'S_BUDGETS': 'Budgets screen (BudgetsActivity): the budget list (BudgetListFragment) opened from the navigation drawer; tapping a budget row shows its detail, and the Up arrow closes the screen',
})

# ---- BudgetsActivity: started from the navigation drawer, then the framework calls onCreate

# B6-DRAWER: plain dispatcher -> BudgetsActivity.<init> partitioned to @GROUP in graph_def_mod/03.py (plain edge deleted).

e('BudgetsActivity.<init>', 'BudgetsActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC budget/BudgetsActivity.java:41-53')

e('BudgetsActivity.onCreate', 'S_BUDGETS', 'ENTERS',
  'the budget list is shown: the layout is set and createFragments adds BudgetListFragment to R.id.fragmentMain',
  evidence='SRC budget/BudgetsActivity.java:45, 52, 106-130 (fragment transaction at 120-122)')

e('BudgetsActivity.onCreate', 'BudgetsActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options panel: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu (the toolbar becomes the action bar at line 47)',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:615-640 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu called at 3388); SRC budget/BudgetsActivity.java:47, 57-63; INFERRED AppCompat decides when the panel is prepared (androidx not in fw_src)')

e('BudgetsActivity.onCreate', 'BudgetsActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state from the pause path: performPauseActivity calls callCallActivityOnSaveInstanceState, which calls onSaveInstanceState',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3855-3876 (callCallActivityOnSaveInstanceState at 3875); FW-SRC core/java/android/app/Activity.java:1495-1501 (onSaveInstanceState called at 1496); SRC budget/BudgetsActivity.java:87-92')

# ---- Up arrow: the toolbar sends android.R.id.home to the options callback

e('S_BUDGETS', 'BudgetsActivity.onOptionsItemSelected', 'GUI',
  'tap the Up (back) arrow in the toolbar: the framework passes android.R.id.home to onOptionsItemSelected; the override calls super, which finishes the activity',
  gui=['Tap the Up (back) arrow at the left of the Budgets toolbar'],
  evidence='SRC budget/BudgetsActivity.java:50 (setDisplayHomeAsUpEnabled), 66-78 (override, super at 77); SRC common/MmxBaseFragmentActivity.java:107-116 (home branch for the Up arrow, finish at 114); FW-SRC core/java/android/app/Activity.java:3439-3455 (onMenuItemSelected calls onOptionsItemSelected at 3450); INFERRED AppCompat toolbar navigation click sends android.R.id.home to the window callback (androidx not in fw_src)')

# ---- EventBus: MmxBaseFragmentActivity.onStart registers the activity; BudgetsActivity.onEvent is the @Subscribe method

e('MmxBaseFragmentActivity.onStart', 'BudgetsActivity.onEvent', 'REGISTER',
  'the activity is registered on EventBus in onStart (inherited by BudgetsActivity); tapping a budget row posts BudgetSelectedEvent (BudgetListFragment.onListItemClick), and EventBus calls onEvent until onStop unregisters',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141, @Subscribe on BudgetsActivity.onEvent (line 82); library source not read, INFERRED',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (onStart register at 141; onStop unregister at 146); SRC budget/BudgetsActivity.java:82-85 (@Subscribe at 82); SRC budget/BudgetListFragment.java:208-215 (post at 215); INFERRED EventBus library source not read')

# ---- part 018 (2026-10-29)
# batch 018 (label_018): BudgetListFragment (18 methods) and BudgetListFragment$1 (2), BudgetNameParser (6), BudgetPeriodEnum.<clinit>, BudgetPeriods (7), BudgetQuery (3), BudgetService (3); rows and printed lines: graphs/MMEX/parts/label_018.md.
# The list is shown on page S_BUDGETS, defined in label_019.py (BudgetsActivity hosts this fragment), so no page is defined here. S_BUDGET_DETAIL is defined in label_016.py and is not redefined. CALL edges come from auto_calls.json, so none are written here.
# Framework and androidx claims are INFERRED where the library source was not read. grep evidence for the no-caller claims is in label_018.grep.txt.

# ---- fragment lifecycle (androidx Fragment; library source not read: INFERRED)

e('BudgetListFragment.<init>', 'BudgetListFragment.onCreate', 'LIFECYCLE',
  'BudgetsActivity.createFragments commits the transaction that adds the fragment (replace at line 121, commit at line 122), and the FragmentManager then calls onCreate',
  evidence='SRC budget/BudgetsActivity.java:117, 121-122; SRC budget/BudgetListFragment.java:63-64, 95-98; INFERRED androidx Fragment lifecycle (library source not read)')

# B6-SEARCH: plain AbsListFragment.onCreateView -> BudgetListFragment.onViewCreated partitioned to @BudgetListFragment in graph_def_mod/03.py (plain edge deleted; shared src lets ANY prefix claim Budget onViewCreated).

e('BudgetListFragment.onViewCreated', 'BudgetListFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onViewCreated; onActivityCreated shows the + button, attaches it to the list and registers the list for the context menu',
  evidence='SRC budget/BudgetListFragment.java:85-92, 119-123; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- loader callbacks (androidx LoaderManager; library not read: INFERRED)

e('BudgetListFragment.displayBudgets', 'BudgetListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader (line 235) starts the budget loader and the LoaderManager calls onCreateLoader',
  guard='loader id == LOADER_BUDGETS (BudgetListFragment.java:131, initLoader at :235)',
  evidence='SRC budget/BudgetListFragment.java:52-53, 235; INFERRED androidx LoaderManager.initLoader calls LoaderCallbacks.onCreateLoader (library not read)')

e('BudgetListFragment.onActivityResult', 'BudgetListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader (line 114) after a budget edit starts the loader again, and the LoaderManager calls onCreateLoader through the callbacks',
  evidence='SRC budget/BudgetListFragment.java:107-116; INFERRED androidx LoaderManager.restartLoader creates the loader through the callbacks (library not read)')

e('BudgetListFragment.onCreateLoader', 'BudgetListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader (MmxCursorLoader, line 136) delivers its cursor and the LoaderManager calls onLoadFinished',
  guard='loader id == LOADER_BUDGETS (BudgetListFragment.java:143)',
  evidence='SRC budget/BudgetListFragment.java:127-139, 141-152; INFERRED androidx Loader delivers its result to the callbacks (library not read)')

e('BudgetListFragment.onLoadFinished', 'BudgetListFragment.onLoaderReset', 'FRAMEWORK',
  'a loader that has delivered data is reset (the fragment is destroyed, or restartLoader at line 114 replaces it) and the LoaderManager calls onLoaderReset',
  guard='loader id == LOADER_BUDGETS (BudgetListFragment.java:157)',
  evidence='SRC budget/BudgetListFragment.java:141-159; INFERRED androidx LoaderManager calls onLoaderReset when a loader with data is destroyed (library not read)')

# ---- result of the editor: BudgetEditActivity sets RESULT_OK when the budget is saved (batch 017 owns the activity)

e('BudgetEditActivity.onActionDoneClick', 'BudgetListFragment.onActivityResult', 'RESULT',
  'the budget editor saves and finishes: setResult(RESULT_OK) (line 67), and the framework calls onActivityResult of the fragment that started it (startActivityForResult, lines 243 and 249)',
  guard='the result is not RESULT_CANCELED (line 111) and the request is REQUEST_EDIT_BUDGET (line 113)',
  evidence='SRC budget/BudgetEditActivity.java:65-73 (setResult 67, finish 68); SRC budget/BudgetListFragment.java:107-116, 238-250; INFERRED androidx Fragment.startActivityForResult dispatches the result to the fragment (library not read)')

# ---- the row menu: long-press a row (the list is registered for the menu in onActivityCreated, line 91)

gui('S_BUDGETS','BudgetListFragment.onCreateContextMenu', 'Long-press a budget row to open its menu',
  evidence='SRC budget/BudgetListFragment.java:91, 163-179; FW-SRC core/java/android/view/View.java:12578-12588 (the context menu listener is called with the menu at 12588); FW-SRC core/java/android/app/Fragment.java:1937-1939 (registerForContextMenu; androidx version INFERRED); the long-press gesture step is INFERRED (source not read)')

gui('S_BUDGETS','BudgetListFragment.onContextItemSelected', 'Tap Edit or Delete in the menu of a budget row',
  evidence='SRC budget/BudgetListFragment.java:176-177 (Edit and Delete items), 181-203; FW-SRC core/java/android/app/Activity.java:3466-3473 (FEATURE_CONTEXT_MENU: onContextItemSelected, then mFragments.dispatchContextItemSelected); INFERRED androidx FragmentManager dispatches the item to the fragment (library not read)')

# ---- user actions on the list

gui('S_BUDGETS','BudgetListFragment.onListItemClick', 'Tap a budget row',
  evidence='SRC budget/BudgetListFragment.java:207-216; auto_calls record AbsListFragment$1.onItemClick -> BudgetListFragment.onListItemClick (SRC AbsListFragment.java:44)')

gui('S_BUDGETS','BudgetListFragment.onFloatingActionButtonClicked', 'Tap the + button',
  evidence='SRC budget/BudgetListFragment.java:218-221; SRC common/BaseListFragment.java:238-248 (listener 241-246, call at 244); SRC res/layout/abs_list_fragment.xml:83 (@+id/fab); auto_calls record BaseListFragment$2.onClick -> BudgetListFragment.onFloatingActionButtonClicked (BaseListFragment.java:244)')

# ---- the delete confirmation: an AlertDialog built in confirmDelete (no screen of its own)

e('BudgetListFragment.confirmDelete', 'BudgetListFragment$1.onClick', 'FRAMEWORK',
  'the dialog has an OK button: when the user taps OK the framework calls the OK listener (the alert button handler calls onClick)',
  guard='the user taps OK (android.R.string.ok) in the delete confirmation dialog (lines 256-262)',
  evidence='SRC budget/BudgetListFragment.java:252-264 (listener 256-262; show 264); FW-SRC android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC com/android/internal/app/AlertController.java:166 (the button handler calls onClick); the View click dispatch is not printed (source not read): INFERRED for that step')

# ---- auto edges that cannot run

# COPY is never added to the row menu (the add is commented out at line 178), so the COPY case never runs
sup(('BudgetListFragment.onContextItemSelected', 'BudgetService.copy'))  # the case at lines 195-198 never runs
sup(('BudgetListFragment.onContextItemSelected', 'BudgetService.<init>'))  # same COPY case (line 196); BudgetService.<init> stays reachable through BudgetListFragment$1.onClick (line 259)
# BudgetPeriods.getPeriodTranslationForEnum(Context,String) has no caller, so its two bytecode calls cannot run
sup(('BudgetPeriods.getPeriodTranslationForEnum(Context,String)', 'BudgetPeriods.getEnum'))  # getEnum stays reachable through BudgetAdapter.getBudgetPeriodFor (line 241)
sup(('BudgetPeriods.getPeriodTranslationForEnum(Context,String)', 'BudgetPeriods.getPeriodTranslationForEnum(Context,BudgetPeriodEnum)'))  # the enum overload stays reachable through BudgetAdapter.bindView (line 119)

# ---- BudgetNameParser (6 methods), BudgetPeriodEnum.<clinit>, BudgetPeriods.<clinit>, BudgetQuery (3), BudgetService.delete, BudgetListFragment$1.<init> and the other
# methods reached only through auto edges need no edge here: their routes are in label_018.md.

# ---- UNREACHABLE: no caller in the app (grep output: graphs/MMEX/parts/label_018.grep.txt)

UNREACHABLE['BudgetPeriods.<init>'] = (
  'no_trigger_in_app',
  'implicit default constructor of a class whose members are all static: BudgetPeriods is used only through its static methods (BudgetAdapter.java:119, 135, 136, 241). The source root has no "new BudgetPeriods" and no other creation site, and auto_calls.json has no edge into the constructor (label_018.grep.txt)',
  'budget/BudgetPeriods.java:29, 39-157; budget/BudgetAdapter.java:119, 135, 136, 241; grep label_018.grep.txt',
  'SOURCE')

UNREACHABLE['BudgetPeriods.getPeriodTranslationForEnum(Context,String)'] = (
  'no_trigger_in_app',
  'public static overload with no caller: its name occurs only at its declaration (line 66). The other call in the source root, BudgetAdapter.java:119, passes a BudgetPeriodEnum and resolves to the enum overload. auto_calls.json has no edge into it (label_018.grep.txt)',
  'budget/BudgetPeriods.java:66-68; budget/BudgetAdapter.java:119; grep label_018.grep.txt',
  'SOURCE')

UNREACHABLE['BudgetQuery.getAllColumns'] = (
  'no_trigger_in_app',
  'public override of the abstract Dataset.getAllColumns. No call site in the source root reaches it: every call goes through a concrete type (repositories and QueryXxx datasets, label_018.grep.txt), and none is typed as Dataset or BudgetQuery. MmxContentProvider casts query results to Dataset (lines 160, 203, 241, 394) and never calls getAllColumns on them. auto_calls.json has no edge into it.',
  'budget/BudgetQuery.java:52-64; database/Dataset.java:52; grep label_018.grep.txt',
  'SOURCE')

UNREACHABLE['BudgetService.copy'] = (
  'branch_never_taken',
  'the body is empty (only a todo, line 47). Its only caller is the COPY case of BudgetListFragment.onContextItemSelected (lines 195-198; the auto edge at line 197 is removed by sup). No COPY item is added to the row menu: the add is commented out at line 178, and COPY is referenced only at ContextMenuIds.java:27 and in that switch case. So the case never runs.',
  'budget/BudgetService.java:46-48; budget/BudgetListFragment.java:176-178, 195-198; core/ContextMenuIds.java:27',
  'SOURCE')

# ---- part 022 (2026-10-29)
# batch 022 (label_022): com.money.manager.ex.common.AllDataMultiChoiceModeListener (7 methods: <init>, setListener, onPrepareActionMode, onDestroyActionMode, onCreateActionMode, onActionItemClicked, onItemCheckedStateChanged); rows and printed lines: graphs/MMEX/parts/label_022.md.
# The list is shown on page S_ACCOUNT_TRANSACTIONS, defined in label_010.py (AccountTransactionListFragment hosts AllDataListFragment), so no page is defined here and no SCREENS entry is added.
# CALL edges come from auto_calls.json (the constructor and setListener from AllDataListFragment.onActivityCreated, onDestroyActionMode from AllDataListFragment.onDestroy, and the listener's calls back into the fragment), so none are written here.
# ActionMode and the action-bar callbacks are not in fw_src, so the framework steps that go beyond the printed AbsListView code are INFERRED. grep evidence: graphs/MMEX/parts/label_022.grep.txt.

# ---- the selection action mode (the list is a multi-choice modal list: AllDataListFragment.java:154-155)

# long-press a row: in multi-choice modal mode AbsListView takes over the long press, starts the action mode through its wrapper (which forwards onCreateActionMode to this listener), and checks the pressed row
gui('S_ACCOUNT_TRANSACTIONS', 'AllDataMultiChoiceModeListener.onCreateActionMode', 'Long-press a transaction row to start multi-select mode',
  evidence='SRC common/AllDataListFragment.java:154-155 (CHOICE_MODE_MULTIPLE_MODAL and the listener); FW-SRC core/java/android/widget/AbsListView.java:1218-1220 (setChoiceMode makes the list long-clickable), 3226-3229 (performLongPress starts the action mode at 3228), 6454-6458 (wrapper forwards onCreateActionMode to this listener and returns true); the long-press gesture step is INFERRED (source not read)')

# tap a row while the mode is on: performItemClick hands the check change to the wrapper, which forwards it to this listener; the long-press that starts the mode also checks its row through setItemChecked (line 3229)
gui('S_ACCOUNT_TRANSACTIONS', 'AllDataMultiChoiceModeListener.onItemCheckedStateChanged', 'Tap a transaction row while multi-select mode is on (checks or unchecks the row)',
  evidence='FW-SRC core/java/android/widget/AbsListView.java:1130-1132 (performItemClick calls the wrapper while the mode is active), 1068-1071 (setItemChecked calls it), 6489-6491 (wrapper forwards to this listener); SRC common/AllDataListFragment.java:440 (fragment callback that the listener calls at line 104)')

# tap an icon in the action bar of the mode: the framework dispatches the item to this listener; the menu is inflated by the fragment in onMultiChoiceCreated (line 393)
gui('S_ACCOUNT_TRANSACTIONS', 'AllDataMultiChoiceModeListener.onActionItemClicked', 'Tap an icon in the selection action bar (select all, change status, duplicate, delete)',
  evidence='SRC common/AllDataListFragment.java:392-394 (inflates R.menu.menu_all_data_adapter); SRC res/menu/menu_all_data_adapter.xml:23, 29, 35, 41 (the four items); FW-SRC core/java/android/widget/AbsListView.java:6469-6470 (wrapper forwards onActionItemClicked to this listener); INFERRED the action bar dispatches the tap to the callback (ActionMode implementation not in fw_src)')

# ---- batch-internal framework edges (the framework calls the ActionMode callbacks; ActionMode implementation not in fw_src: INFERRED)

e('AllDataMultiChoiceModeListener.onCreateActionMode', 'AllDataMultiChoiceModeListener.onPrepareActionMode', 'FRAMEWORK',
  'after onCreateActionMode returns true the framework prepares the mode, which calls onPrepareActionMode; the mode is invalidated again when the checked count changes (AbsListView line 5510)',
  guard='onCreateActionMode returns true (line 50)',
  evidence='SRC common/AllDataMultiChoiceModeListener.java:48-50; FW-SRC core/java/android/widget/AbsListView.java:6455-6458 (wrapper returns true), 6464-6465 (wrapper forwards prepare), 5509-5510 (invalidate on checked count change); INFERRED ActionMode start and invalidate call the prepare callback (ActionMode implementation not in fw_src)')

e('AllDataMultiChoiceModeListener.onActionItemClicked', 'AllDataMultiChoiceModeListener.onDestroyActionMode', 'FRAMEWORK',
  'a handled item finishes the mode: mode.finish() (line 96) makes the framework call onDestroyActionMode',
  guard='the item was handled: result is true (the cases at lines 71, 75, 79 and 88; menu_select_all keeps the mode open at line 67)',
  evidence='SRC common/AllDataMultiChoiceModeListener.java:95-97; INFERRED ActionMode.finish calls the callback onDestroyActionMode (ActionMode implementation not in fw_src)')

e('AllDataMultiChoiceModeListener.onItemCheckedStateChanged', 'AllDataMultiChoiceModeListener.onDestroyActionMode', 'FRAMEWORK',
  'when the last checked row is unchecked the wrapper finishes the mode, and the framework calls onDestroyActionMode',
  guard='no row is checked after the callback (getCheckedItemCount() is 0, AbsListView line 6494)',
  evidence='FW-SRC core/java/android/widget/AbsListView.java:6491 (wrapper forwards to this listener), 6494-6495 (finish when no row is checked); INFERRED ActionMode.finish calls the callback onDestroyActionMode (ActionMode implementation not in fw_src)')

# ---- auto edge that cannot run: the status case of onActionItemClicked (lines 81-88) needs a menu item with a status id, and menu_all_data_adapter.xml has none (label_022.grep.txt, section C)
sup(('AllDataMultiChoiceModeListener.onActionItemClicked', 'AllDataListFragment.onTransactionStatusClicked'))  # auto_calls.json edge at its record line 37218-37219; batch 020 owns the destination and no other call site exists in the source root (label_022.grep.txt, section B)

# ---- part 021 (2026-10-29)
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

# ---- part 024 (2026-10-29)
# batch 024 (label_024): com.money.manager.ex.common.AmountInputDialog, methods 41-43 of 43: $6.onClick, $7.<init>, $7.onClick.
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_024.md.
# This batch defines and reuses no page (batch 023 defines none either).
# The three methods are reached from AmountInputDialog.onCreateDialog (batch 023). $7.<init> has its CALL edge in auto_calls.json (lines 35414-35416), so none is written here.
# The two button listeners are framework callbacks: AlertDialog.Builder stores them, and AlertController calls onClick on a tap. Framework lines were read from fw_src (FW-SRC).
# Which listener is which: the body of AmountInputDialog$7.onClick holds evalExpression (line 258) and the EventBus post (line 260), the OK body of source lines 255-264; the body of AmountInputDialog$6.onClick holds only DialogInterface.dismiss, the Cancel body of source lines 265-270 (auto_calls.json 70666-70668 and 71119-71126). grep evidence: graphs/MMEX/parts/label_024.grep.txt.

# ---- the buttons: onCreateDialog stores the listeners, the framework calls onClick on a tap

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$6.onClick', 'FRAMEWORK',
  'the Cancel button: setNegativeButton stores the listener (AlertDialog.java:637-641); AlertParams.apply sets the button with it (AlertController.java:1025-1027); setButton keeps the message with the listener (AlertController.java:344-360); a tap runs mButtonHandler, which sends the message (AlertController.java:125-147); ButtonHandler.handleMessage calls onClick (AlertController.java:160-167)',
  guard='the user taps Cancel (android.R.string.cancel) in the amount input dialog (the listener at lines 265-270)',
  evidence='SRC common/AmountInputDialog.java:265-270; auto_calls.json:70666-70668 (AmountInputDialog$6.onClick calls only DialogInterface.dismiss); FW-SRC core/java/android/app/AlertDialog.java:637-641; FW-SRC core/java/com/android/internal/app/AlertController.java:1025-1027, 344-360, 125-147, 160-167')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$7.onClick', 'FRAMEWORK',
  'the OK button: setPositiveButton stores the listener (AlertDialog.java:611-613); AlertParams.apply sets the button with it (AlertController.java:1021-1024); setButton keeps the message with the listener (AlertController.java:344-355); a tap runs mButtonHandler, which sends the message (AlertController.java:125-147); ButtonHandler.handleMessage calls onClick (AlertController.java:160-167)',
  guard='the user taps OK (android.R.string.ok) in the amount input dialog (the listener at lines 255-264); the body returns before the post when evalExpression() is false (line 258)',
  evidence='SRC common/AmountInputDialog.java:255-264; auto_calls.json:39342-39363 (AmountInputDialog$7.onClick calls evalExpression at line 258 and EventBus.post with AmountEnteredEvent at line 260); auto_calls.json:71119-71126; FW-SRC core/java/android/app/AlertDialog.java:611-613; FW-SRC core/java/com/android/internal/app/AlertController.java:1021-1024, 344-355, 125-147, 160-167')

# ---- part 025 (2026-10-29)
# batch 025 (label_025): com.money.manager.ex.common.BaseExpandableListFragment (abstract; 26 methods: the class, its anonymous listeners $1 and $2); rows and printed lines: graphs/MMEX/parts/label_025.md.
# The only subclass is CategoryListFragment (CategoryListFragment.java:72-73). The list is shown on page S_CATEGORY_LIST, defined at graph_def.py:1214 and only reused here. Its ENTERS edge is written by batches 028, 029, 030 and 080, so no ENTERS edge is written here.
# CALL edges come from auto_calls.json (the super calls of CategoryListFragment, the calls inside this class, and the receiver-variant records "...@CategoryListFragment"), so none are written here. The edges that cannot run are cut with sup below.
# androidx Fragment, SearchView and the options-menu dispatch are not in fw_src: those claims are INFERRED (library source not read). grep evidence: graphs/MMEX/parts/label_025.grep.txt.

# ---- fragment lifecycle (androidx Fragment; library source not read: INFERRED). CategoryListFragment overrides none of onCreate, onCreateView, onViewCreated, onStart, onCreateOptionsMenu or onOptionsItemSelected (grep of CategoryListFragment.java), so the framework calls these inherited bodies on a CategoryListFragment instance.

e('CategoryListFragment.<init>', 'BaseExpandableListFragment.onCreate', 'LIFECYCLE',
  'the framework creates the fragment (CategoryListActivity creates it at line 43) and calls onCreate; CategoryListFragment does not override onCreate, so the inherited body runs',
  evidence='SRC common/CategoryListFragment.java:72-73 (class declaration, no onCreate); SRC common/CategoryListActivity.java:43; SRC common/BaseExpandableListFragment.java:61-70; INFERRED androidx Fragment lifecycle (library not read)')

e('ExpandableListFragment.onCreateView', 'BaseExpandableListFragment.onViewCreated', 'LIFECYCLE',
  'the framework calls onViewCreated after the view is created by the inherited onCreateView (ExpandableListFragment inflates expandable_list_fragment)',
  evidence='SRC common/ExpandableListFragment.java:99 (onCreateView inflates the layout), 133-135; SRC common/BaseExpandableListFragment.java:224-236; INFERRED androidx Fragment lifecycle (library not read)')

e('CategoryListFragment.onActivityCreated', 'BaseExpandableListFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after onActivityCreated',
  evidence='SRC common/CategoryListFragment.java:97-98; SRC common/BaseExpandableListFragment.java:95-111; INFERRED androidx Fragment lifecycle (library not read)')

e('CategoryListFragment.onActivityCreated', 'BaseExpandableListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'CategoryListFragment.onActivityCreated calls setHasOptionsMenu(true) (line 113); the activity then builds its options menu and the fragment adds its own items in onCreateOptionsMenu',
  evidence='SRC common/CategoryListFragment.java:113; SRC common/BaseExpandableListFragment.java:120-155; INFERRED androidx FragmentManager dispatches onCreateOptionsMenu to fragments that have an options menu (library not read)')

# ---- user actions on the category list (page S_CATEGORY_LIST). The items of the fragment's options menu: menu_query_mode (search, line 123) and the Up arrow (android.R.id.home, line 160).

gui('S_CATEGORY_LIST', 'BaseExpandableListFragment.onOptionsItemSelected', 'Tap the Up arrow in the action bar',
  evidence='SRC common/BaseExpandableListFragment.java:158-164 (home: setResultAndFinish, unless hosted by MainActivity); SRC common/CategoryListFragment.java:113; INFERRED androidx FragmentManager dispatches the selected item to the fragment (library not read)')

gui('S_CATEGORY_LIST', 'BaseExpandableListFragment$1.onQueryTextChange', 'Type in the search box',
  evidence='SRC common/BaseExpandableListFragment.java:129-143 (SearchView created and listener set at 131); INFERRED androidx SearchView calls the listener on each text change (SearchView not in fw_src)')

gui('S_CATEGORY_LIST', 'BaseExpandableListFragment$1.onQueryTextSubmit', 'Submit the search text (search key on the keyboard)',
  evidence='SRC common/BaseExpandableListFragment.java:131-135; INFERRED androidx SearchView calls onQueryTextSubmit on submit (SearchView not in fw_src)')

gui('S_CATEGORY_LIST', 'BaseExpandableListFragment$2.onClick', 'Tap the + button (floating action button) on the category list',
  evidence='SRC common/BaseExpandableListFragment.java:224-232 (fab found by R.id.fab at 225, listener at 227-232); SRC res/layout/expandable_list_fragment.xml:66-67 (@+id/fab); SRC common/CategoryListFragment.java:140-141 (fab made visible and attached); INFERRED the view dispatches the click to the listener (View not read)')

# ---- auto edges that cannot run

# menu_query_mode on API 27: the branch at line 167 (SDK_INT < HONEYCOMB) is false, so onMenuItemSearchClick is never called from here; the plain edge (line 168) and its receiver variant are both cut
sup(('BaseExpandableListFragment.onOptionsItemSelected', 'BaseExpandableListFragment.onMenuItemSearchClick'),  # line 168
    ('BaseExpandableListFragment.onOptionsItemSelected@CategoryListFragment', 'BaseExpandableListFragment.onMenuItemSearchClick@CategoryListFragment'))  # the receiver variant of the same call (line 168)

# CategoryListFragment.onQueryTextChange (line 230) overrides the base method and does not call super, so the base body never runs; the receiver edge to the override (auto record, line 210) stays
sup(('BaseExpandableListFragment.onPreQueryTextChange', 'BaseExpandableListFragment.onQueryTextChange'))  # line 210

# CategoryListFragment.setResult (line 313) overrides the base method and does not call super; the receiver edge to the override (setResultAndFinish@CategoryListFragment -> CategoryListFragment.setResult, line 262) stays
sup(('BaseExpandableListFragment.setResultAndFinish', 'BaseExpandableListFragment.setResult'))  # line 262

# CategoryListFragment.onFloatingActionButtonClickListener (line 367) overrides the base method and does not call super; the cha edge to the override (auto record, line 230) stays
sup(('BaseExpandableListFragment$2.onClick', 'BaseExpandableListFragment.onFloatingActionButtonClickListener'))  # line 230

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_025.grep.txt)

UNREACHABLE['BaseExpandableListFragment.onMenuItemSearchClick'] = (
  'closed_by_api_level',
  'protected method called only from the menu_query_mode case of onOptionsItemSelected, under if (Build.VERSION.SDK_INT < Build.VERSION_CODES.HONEYCOMB) (lines 166-168). The standard configuration is API 27 (handoff/SCHEMA_V2.md:38), so the condition is false and the call never runs. The HONEYCOMB constant is not printed from fw_src (Build.java is not in fw_src); its value (11) is INFERRED from the public Android API levels. The name occurs only at its declaration (line 175) and at line 168 (label_025.grep.txt, section A). Both auto edges into it (line 168, plain and receiver variant) are cut by sup',
  'SRC common/BaseExpandableListFragment.java:158-173, 175; handoff/SCHEMA_V2.md:38; grep label_025.grep.txt sections A, G',
  'INFERRED')

UNREACHABLE['BaseExpandableListFragment.onFloatingActionButtonClickListener'] = (
  'no_trigger_in_app',
  'public method with an empty body (lines 293-294). Its only subclass, CategoryListFragment, overrides it (lines 367-369) without calling super, so every call on a CategoryListFragment receiver runs the override and this body never runs. The FAB listener (BaseExpandableListFragment$2.onClick, line 230) reaches the override through the cha edge, which stays; the exact edge to this body is cut by sup. The name occurs in this file at lines 230 and 293 only (label_025.grep.txt, section B)',
  'SRC common/BaseExpandableListFragment.java:227-231, 293-294; SRC common/CategoryListFragment.java:367-369; grep label_025.grep.txt sections B, G',
  'SOURCE')

UNREACHABLE['BaseExpandableListFragment.onQueryTextChange'] = (
  'no_trigger_in_app',
  'protected method whose base body returns true (lines 213-215). Its only subclass, CategoryListFragment, overrides it (lines 230-237) without calling super. The call in onPreQueryTextChange (line 210) runs on a CategoryListFragment receiver, so it dispatches to the override. The plain edge to this body (line 210) is cut by sup; the receiver edge to the override stays. In this file the name also appears in the SearchView listener method at line 138, which is a different method (label_025.grep.txt, section D)',
  'SRC common/BaseExpandableListFragment.java:206-215; SRC common/CategoryListFragment.java:230-237; grep label_025.grep.txt sections D, G',
  'SOURCE')

UNREACHABLE['BaseExpandableListFragment.setResult'] = (
  'no_trigger_in_app',
  'protected method with an empty body (lines 257-258). Its only caller in this class is setResultAndFinish (line 262), which runs on a CategoryListFragment receiver, and the only subclass CategoryListFragment overrides setResult (line 313) without calling super. So the override runs and this body never does. The plain edge from setResultAndFinish to this body (line 262) is cut by sup; the receiver edge to the override stays. The other setResult() declarations in the source root belong to BaseListFragment, PayeeListFragment, AccountListFragment and CurrencyListFragment, which are not subclasses of this class (label_025.grep.txt, sections C, C2, E)',
  'SRC common/BaseExpandableListFragment.java:257-265; SRC common/CategoryListFragment.java:313; grep label_025.grep.txt sections C, C2, E, G',
  'SOURCE')

# ---- part 023 (2026-10-29)
# batch 023 (label_023): com.money.manager.ex.common.AmountInputDialog, methods 1-40 of 43: the constructor, the instance and static methods, the generated helper AmountInputDialog$$Icepick (4 methods), the listeners $1-$5 (<init> and onClick each) and AmountInputDialog$6.<init>.
# The other three (AmountInputDialog$6.onClick, $7.<init>, $7.onClick) are in batch 024: graphs/MMEX/parts/label_024.py.
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_023.md. grep evidence: graphs/MMEX/parts/label_023.grep.txt.
# No page is defined. SCREENS has no home, settings or price-edit key, so the entry taps belong to the batches that own those screens. The keypad, delete and clear keys reach their listeners through FRAMEWORK edges from onCreateDialog, as in label_021.py.
# CALL edges come from auto_calls.json and are not written here. androidx DialogFragment and the icepick library are not in the dataset: INFERRED. The generated helper has no source in the app source root (grep section B).

# ---- the three callers outside this batch: each one calls show(), so the framework runs onCreate (LIFECYCLE)

e('HomeFragment.startBalanceAccount', 'AmountInputDialog.onCreate', 'LIFECYCLE',
  'the balance account amount dialog is shown: dialog.show (HomeFragment.java:548) makes the fragment manager run onCreate',
  evidence='SRC home/HomeFragment.java:545-548 (getInstance 545-546, setTargetFragment 547, show 548); INFERRED androidx DialogFragment.show (library not in the dataset; source not read)')

e('InvestmentSettingsFragment$1.onPreferenceClick', 'AmountInputDialog.onCreate', 'LIFECYCLE',
  'the asset allocation threshold dialog is shown: show (InvestmentSettingsFragment.java:117) makes the fragment manager run onCreate',
  evidence='SRC settings/InvestmentSettingsFragment.java:111-119 (getInstance 116, show 117); INFERRED androidx DialogFragment.show (library not in the dataset; source not read)')

e('EditPriceDialog$7.onClick', 'AmountInputDialog.onCreate', 'LIFECYCLE',
  'the amount field of the price edit dialog shows the amount dialog: show (EditPriceDialog.java:260) makes the fragment manager run onCreate',
  evidence='SRC investment/EditPriceDialog.java:256-263 (getInstance 259, show 260); INFERRED androidx DialogFragment.show (library not in the dataset; source not read)')

# ---- the dialog lifecycle (androidx DialogFragment: library not in the dataset, INFERRED)

e('AmountInputDialog.onCreate', 'AmountInputDialog.onCreateDialog', 'LIFECYCLE',
  'the framework calls onCreateDialog after onCreate, to build the dialog it shows',
  evidence='SRC common/AmountInputDialog.java:138-153 (onCreate), 155-156 (onCreateDialog); precedent label_012.py line 17; INFERRED androidx DialogFragment (library not in the dataset; source not read)')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog.onResume', 'LIFECYCLE',
  'the framework resumes the dialog fragment once the dialog has been created and shown',
  evidence='SRC common/AmountInputDialog.java:155-276 (onCreateDialog), 278-282 (onResume); INFERRED androidx Fragment lifecycle (library not in the dataset; source not read)')

e('AmountInputDialog.onResume', 'AmountInputDialog.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state through onSaveInstanceState (on rotation, or when the host activity stops)',
  evidence='SRC common/AmountInputDialog.java:278-295; precedent label_010.py line 47; INFERRED androidx FragmentManager (library not in the dataset; source not read)')

# ---- the keypad, the clear and equals keys, and the delete key: onCreateDialog stores the listeners; the framework calls onClick on a tap

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$1.onClick', 'FRAMEWORK',
  'a digit or decimal key is tapped: setOnClickListener stores the listener on each key, and performClick calls onClick',
  guard='the user taps a digit key (buttonKeyNum0-9) or the decimal key (buttonKeyNumDecimal) of the keypad (lines 178-181)',
  evidence='SRC common/AmountInputDialog.java:164-181 (listener 164-177; set on each key 178-181); FW-SRC core/java/android/view/View.java:6143-6147 (setOnClickListener stores the listener at 6147), 6289-6296 (performClick calls onClick at 6294)')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$2.onClick', 'FRAMEWORK',
  'an operator key is tapped: setOnClickListener stores the listener on each key, and performClick calls onClick',
  guard='the user taps an operator key (add, divide, less, multiplication, left or right parenthesis) (lines 193-196)',
  evidence='SRC common/AmountInputDialog.java:183-196 (listener 183-192; set on each key 193-196); FW-SRC core/java/android/view/View.java:6143-6147, 6289-6296')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$3.onClick', 'FRAMEWORK',
  'the clear key is tapped: setOnClickListener stores the listener, and performClick calls onClick',
  guard='the user taps the clear key (buttonKeyClear) (line 200)',
  evidence='SRC common/AmountInputDialog.java:198-207 (clear listener set at 200-207); FW-SRC core/java/android/view/View.java:6143-6147, 6289-6296')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$4.onClick', 'FRAMEWORK',
  'the equals key is tapped: setOnClickListener stores the listener, and performClick calls onClick',
  guard='the user taps the equals key (buttonKeyEqual) (line 211)',
  evidence='SRC common/AmountInputDialog.java:209-218 (equals listener set at 211-218); FW-SRC core/java/android/view/View.java:6143-6147, 6289-6296')

e('AmountInputDialog.onCreateDialog', 'AmountInputDialog$5.onClick', 'FRAMEWORK',
  'the delete key is tapped: setOnClickListener stores the listener, and performClick calls onClick',
  guard='the user taps the delete key (deleteButton); the listener is set only when the view exists (line 222), and both layouts define it',
  evidence='SRC common/AmountInputDialog.java:220-235 (guard 222, listener set at 223-234); RES layout/input_amount_dialog.xml:91 and RES layout-land/input_amount_dialog.xml:186 (deleteButton); FW-SRC core/java/android/view/View.java:6143-6147, 6289-6296')

# ---- icepick (@State on mAmount, line 122): the library loads the generated helper AmountInputDialog$$Icepick by reflection.
# The helper is not in the source root (label_023.grep.txt section B); the icepick library is not in the dataset: INFERRED for every edge below.

e('AmountInputDialog.restoreSavedInstanceState', 'AmountInputDialog$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State field mAmount: the library loads the generated helper by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at AmountInputDialog.java:417)',
  guard='onCreate received a non-null savedInstanceState (AmountInputDialog.java:148-150)',
  evidence='SRC common/AmountInputDialog.java:47 (import icepick.Icepick), 122 (@State mAmount), 417 (Icepick.restoreInstanceState); the icepick library and the helper are not in the dataset: INFERRED, source not read')

e('AmountInputDialog.restoreSavedInstanceState', 'AmountInputDialog$$Icepick.<init>', 'FRAMEWORK',
  'the library creates an instance of the generated helper by reflection when it restores the state',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at AmountInputDialog.java:417)',
  guard='onCreate received a non-null savedInstanceState (AmountInputDialog.java:148-150)',
  evidence='SRC common/AmountInputDialog.java:417; the icepick library is not in the dataset: INFERRED, source not read')

e('AmountInputDialog.restoreSavedInstanceState', 'AmountInputDialog$$Icepick.restore', 'FRAMEWORK',
  'Icepick restores the @State field mAmount: the library calls the generated restore by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at AmountInputDialog.java:417)',
  guard='onCreate received a non-null savedInstanceState (AmountInputDialog.java:148-150)',
  evidence='SRC common/AmountInputDialog.java:122 (@State mAmount), 417 (Icepick.restoreInstanceState); the icepick library is not in the dataset: INFERRED, source not read')

e('AmountInputDialog.onSaveInstanceState', 'AmountInputDialog$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick saves the @State field mAmount: the library loads the generated helper by reflection, which runs its static initialiser first (on a first save, before any restore)',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at AmountInputDialog.java:294)',
  evidence='SRC common/AmountInputDialog.java:47 (import icepick.Icepick), 122 (@State mAmount), 294 (Icepick.saveInstanceState); the icepick library and the helper are not in the dataset: INFERRED, source not read')

e('AmountInputDialog.onSaveInstanceState', 'AmountInputDialog$$Icepick.<init>', 'FRAMEWORK',
  'the library creates an instance of the generated helper by reflection when it saves the state',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at AmountInputDialog.java:294)',
  evidence='SRC common/AmountInputDialog.java:294; the icepick library is not in the dataset: INFERRED, source not read')

e('AmountInputDialog.onSaveInstanceState', 'AmountInputDialog$$Icepick.save', 'FRAMEWORK',
  'Icepick saves the @State field mAmount: the library calls the generated save by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at AmountInputDialog.java:294)',
  evidence='SRC common/AmountInputDialog.java:122 (@State mAmount), 294 (Icepick.saveInstanceState); the icepick library is not in the dataset: INFERRED, source not read')

# ---- UNREACHABLE: overloads of getInstance with no live caller (grep output: graphs/MMEX/parts/label_023.grep.txt, sections A and C)

UNREACHABLE['AmountInputDialog.getInstance(int,Money)'] = (
  'no_trigger_in_app',
  'public static overload with no caller in the app. Every reference to AmountInputDialog under the source root is listed in the grep (20 hits): the three external callers use other overloads (HomeFragment.java:545-546 the 4-argument int form, InvestmentSettingsFragment.java:116 the String 2-argument form, EditPriceDialog.java:259 the String 4-argument form), and the only 3-argument call is commented out (EditTransactionCommonFunctions.java:410). No CALL edge into this overload exists in auto_calls.json. Its outgoing auto edge (line 64) cannot run and is removed by sup.',
  'SRC common/AmountInputDialog.java:62-65; SRC home/HomeFragment.java:545-546; SRC settings/InvestmentSettingsFragment.java:116; SRC investment/EditPriceDialog.java:259; SRC transactions/EditTransactionCommonFunctions.java:410 (commented); grep label_023.grep.txt sections A and C',
  'SOURCE')

UNREACHABLE['AmountInputDialog.getInstance(int,Money,int)'] = (
  'no_trigger_in_app',
  'public static overload whose only call site is commented out: transactions/EditTransactionCommonFunctions.java:410 begins with // (the dialog line and its show call at 411 are both comments). No live call in the app and no CALL edge into it in auto_calls.json. Its outgoing auto edge (line 73) cannot run and is removed by sup.',
  'SRC common/AmountInputDialog.java:71-74; SRC transactions/EditTransactionCommonFunctions.java:404-412 (410-411 commented); grep label_023.grep.txt sections A and C',
  'SOURCE')

UNREACHABLE['AmountInputDialog.getInstance(String,Money,int)'] = (
  'no_trigger_in_app',
  'public static overload with no caller: the String callers use the 2-argument form (InvestmentSettingsFragment.java:116) and the 4-argument form (EditPriceDialog.java:259); no call with three arguments exists (grep sections A and C), and no CALL edge into it exists in auto_calls.json. Its outgoing auto edge (line 77) cannot run and is removed by sup.',
  'SRC common/AmountInputDialog.java:76-78; SRC settings/InvestmentSettingsFragment.java:116; SRC investment/EditPriceDialog.java:259; grep label_023.grep.txt sections A and C',
  'SOURCE')

# ---- auto edges that cannot run: their source is one of the UNREACHABLE overloads above (their bodies never run)

sup(('AmountInputDialog.getInstance(int,Money)', 'AmountInputDialog.getInstance(String,Money,Integer,boolean)'))  # auto edge at line 64
sup(('AmountInputDialog.getInstance(int,Money,int)', 'AmountInputDialog.getInstance(String,Money,Integer,boolean)'))  # auto edge at line 73
sup(('AmountInputDialog.getInstance(String,Money,int)', 'AmountInputDialog.getInstance(String,Money,Integer,boolean)'))  # auto edge at line 77

# ---- part 020 (2026-10-29)
# ================================================================== batch 020 (label_020): com.money.manager.ex.common.AllDataListFragment (methods 1-40 of 63)
# Rows, printed source lines and the reason for each label: graphs/MMEX/parts/label_020.md.
# Grep evidence for the two UNREACHABLE methods and the menu and library claims: graphs/MMEX/parts/label_020.grep.txt.
# Page S_ACCOUNT_TRANSACTIONS is defined in label_010.py and only reused here. The search results screen (SearchActivity, batch 107) hosts the same fragment too; no page key is defined for it here, so its entry edges start from SearchActivity methods.
# CALL edges come from auto_calls.json and are not written here. Framework and library claims (androidx Fragment, FragmentManager, LoaderManager, FragmentActivity options dispatch) are INFERRED: the androidx source is not read. FW-SRC is cited where the platform source applies.

# ---- lifecycle of the list fragment. On the account screen it is a child of AccountTransactionListFragment (child FragmentManager, line 835);
# on the search screen SearchActivity adds it to the activity FragmentManager (SearchActivity.java:205, commit at 212).

e('AccountTransactionListFragment.showTransactionsFragment', 'AllDataListFragment.onCreate', 'FRAMEWORK',
  'the child FragmentManager runs the replace when the transaction commits (line 851): the framework attaches the new fragment and calls its onCreate',
  evidence='SRC account/AccountTransactionListFragment.java:835-851 (getChildFragmentManager 835; newInstance 837; setAutoStarLoader 846; replace 850; commit 851); INFERRED androidx FragmentManager (library source not read)')

e('SearchActivity.showSearchResultsFragment', 'AllDataListFragment.onCreate', 'FRAMEWORK',
  'the search results fragment is added to R.id.fragmentDetail and the transaction commits (SearchActivity.java:205, 212); the framework calls onCreate of the new fragment',
  evidence='SRC search/SearchActivity.java:183 (newInstance), 205 (add), 212 (commit); INFERRED androidx FragmentManager (library source not read)')

e('AllDataListFragment.onCreate', 'AllDataListFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC common/AllDataListFragment.java:204-214; INFERRED androidx Fragment lifecycle (library source not read)')

e('AllDataListFragment.onCreateView', 'AllDataListFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onCreateView (the view exists; the list and the adapter are set up in it)',
  evidence='SRC common/AllDataListFragment.java:128-130, 211-214; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onStop', 'AllDataListFragment.onStop', 'FRAMEWORK',
  'the child list fragment stops when its parent stops (parent onStop at line 218)',
  guard='the account screen is shown: the list is a child of AccountTransactionListFragment',
  evidence='SRC account/AccountTransactionListFragment.java:218 (parent onStop); SRC common/AllDataListFragment.java:341-358; INFERRED androidx FragmentManager dispatches the stop to child fragments (library source not read)')

e('AllDataListFragment.onStop', 'AllDataListFragment.onDestroy', 'LIFECYCLE',
  'the framework destroys the fragment after it stops (its container is removed or the parent is destroyed)',
  evidence='SRC common/AllDataListFragment.java:328-333, 341-343; INFERRED androidx Fragment lifecycle (library source not read)')

e('AccountTransactionListFragment.onResume', 'AllDataListFragment.onResume', 'FRAMEWORK',
  'the child list fragment resumes when its parent resumes (parent onResume at line 205)',
  guard='the account screen is resumed (the parent is visible)',
  evidence='SRC account/AccountTransactionListFragment.java:205 (parent onResume); SRC common/AllDataListFragment.java:335-339; INFERRED androidx FragmentManager dispatches the resume to child fragments (library source not read)')

e('SearchActivity.onResume', 'AllDataListFragment.onResume', 'FRAMEWORK',
  'the search screen resumes: super.onResume (SearchActivity.java:74) makes the framework dispatch onResume to the fragments of the activity',
  guard='the search results fragment is in the activity FragmentManager (added at SearchActivity.java:205)',
  evidence='SRC search/SearchActivity.java:72-80 (super.onResume at 74; loadData at 79); SRC common/AllDataListFragment.java:335-339; INFERRED androidx FragmentActivity dispatches onResume to its fragments (library source not read)')

# ---- options menu. The fragment has an options menu (setHasOptionsMenu at line 208). On the account screen the parent calls onCreateOptionsMenu (auto edge at AccountTransactionListFragment.java:248).

e('SearchActivity.onCreateOptionsMenu', 'AllDataListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options panel: onCreatePanelMenu calls the activity onCreateOptionsMenu (SearchActivity.java:91-104), then the fragments with an options menu add their items; on the search screen this adds menu_alldata_operations (line 323)',
  guard='the fragment has its options menu enabled: setHasOptionsMenu(true) at AllDataListFragment.java:208',
  evidence='SRC search/SearchActivity.java:91-104 (inflate at 97); SRC common/AllDataListFragment.java:204-209, 300-326 (search-only inflation at 318-323); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreatePanelMenu calls onCreateOptionsMenu at 3388); INFERRED androidx FragmentActivity dispatch to fragments (library source not read)')

e('SearchActivity.onOptionsItemSelected', 'AllDataListFragment.onOptionsItemSelected', 'FRAMEWORK',
  'an item that is not the Up arrow or the search item: the default branch returns super (SearchActivity.java:118), and the framework then dispatches the item to the fragments; the QIF item of the search screen reaches this fragment',
  guard='the item is menu_qif_export (added by onCreateOptionsMenu on the search screen); the home and search cases return before this',
  evidence='SRC search/SearchActivity.java:107-120 (default super at 118); SRC common/AllDataListFragment.java:360-374; FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450), 3597-3599 (the Activity body returns mParent.onOptionsItemSelected); INFERRED androidx FragmentActivity dispatch to fragments (library source not read)')

# ---- loader. loadData(Bundle) restarts the loader; the LoaderManager then calls the callbacks (LoaderManager is androidx: INFERRED).

e('AllDataListFragment.loadData(Bundle)', 'AllDataListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader (line 532) starts the loader for ID_LOADER_ALL_DATA_DETAIL and the LoaderManager calls onCreateLoader with the arguments',
  evidence='SRC common/AllDataListFragment.java:521-533 (restartLoader at 532); INFERRED androidx LoaderManager calls the callbacks (library source not read)')

e('AllDataListFragment.loadData(Bundle)', 'AllDataListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader finishes its query and the LoaderManager delivers the cursor to onLoadFinished on the main thread',
  guard='the query started by restartLoader (line 532) completes',
  evidence='SRC common/AllDataListFragment.java:521-533 (restartLoader at 532); INFERRED androidx LoaderManager delivers results to the callbacks (library source not read)')

e('AllDataListFragment.loadData(Bundle)', 'AllDataListFragment.onLoaderReset', 'FRAMEWORK',
  'restartLoader destroys the loader that already exists for the same id, and the LoaderManager calls onLoaderReset for it',
  guard='a loader for ID_LOADER_ALL_DATA_DETAIL already delivered its data (the second and later loadData calls)',
  evidence='SRC common/AllDataListFragment.java:521-533 (restartLoader at 532); INFERRED androidx LoaderManager resets an old loader on restart (library source not read)')

# ---- user actions on the account screen: the + button (the list shows it when the fragment is built with the floating button flag)

gui('S_ACCOUNT_TRANSACTIONS', 'AllDataListFragment.onFloatingActionButtonClicked', 'Tap the + button on the account transaction list',
    evidence='SRC common/AllDataListFragment.java:191-196 (the button is shown when ARG_SHOW_FLOATING_BUTTON is true, set by newInstance(int) at 92), 381-384; SRC account/AccountTransactionListFragment.java:837; SRC common/BaseListFragment.java:238-248 (listener 241-246, call at 244); auto_calls.json record BaseListFragment$2.onClick -> AllDataListFragment.onFloatingActionButtonClicked (BaseListFragment.java:244, cha)')

# ---- auto edges that cannot run: the export case of the menu of this fragment, and the export case of the parent (cross-batch sources)

# line 365: the export case in onOptionsItemSelected is never taken (menu_export_to_csv is in no shown menu; grep sections B-E)
sup(('AllDataListFragment.onOptionsItemSelected', 'AllDataListFragment.exportDataToCSVFile()'))

# line 465: the zero-argument overload calls the prefix overload, but the zero-argument overload itself cannot run
sup(('AllDataListFragment.exportDataToCSVFile()', 'AllDataListFragment.exportDataToCSVFile(String)'))

# line 305 (AccountTransactionListFragment.java:303-306): the parent's export case is never taken either; batch 010 owns the source, this batch owns the destination
sup(('AccountTransactionListFragment.onOptionsItemSelected', 'AllDataListFragment.exportDataToCSVFile(String)'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_020.grep.txt)

UNREACHABLE['AllDataListFragment.exportDataToCSVFile()'] = (
  'branch_never_taken',
  'Its only caller is the export case of AllDataListFragment.onOptionsItemSelected (line 364-365). That case needs R.id.menu_export_to_csv to be the id of an item in a menu the fragment is shown with. The id is declared only in res/menu/menu_main.xml:60, res/menu-v14/menu_main.xml:65 and res/menu/menu_search_transaction.xml:30, and no Java in the source root inflates menu_main or menu_search_transaction (grep sections B-D). The menus that are actually shown here do not declare it: the account screen inflates menu_period_picker_transactions, menu_transaction_status_selector and menu_transaction_filters (AccountTransactionListFragment.java:237-244); the search screen inflates menu_search (SearchActivity.java:97, no export id; section F) and menu_alldata_operations (only menu_qif_export, section G); the action mode inflates menu_all_data_adapter (line 393). The export case never runs.',
  'common/AllDataListFragment.java:360-374 (case 364-367), 461-466; account/AccountTransactionListFragment.java:237-244; search/SearchActivity.java:97; common/AllDataListFragment.java:318-323, 393; res/menu/menu_alldata_operations.xml:23; graphs/MMEX/parts/label_020.grep.txt sections A-G, O',
  'SOURCE')

UNREACHABLE['AllDataListFragment.exportDataToCSVFile(String)'] = (
  'branch_never_taken',
  'Its callers are exportDataToCSVFile() (line 465), which cannot run (see the entry above), and the case R.id.menu_export_to_csv of AccountTransactionListFragment.onOptionsItemSelected (AccountTransactionListFragment.java:303-305). That case cannot run either: the parent fragment inflates only menu_period_picker_transactions, menu_transaction_status_selector and menu_transaction_filters (lines 237-244), and none of them declares the id (grep sections A-B). No other caller exists in the source root (section A).',
  'common/AllDataListFragment.java:461-477; account/AccountTransactionListFragment.java:237-248, 303-306; graphs/MMEX/parts/label_020.grep.txt sections A, B, E',
  'SOURCE')

# ---- part 027 (2026-10-29)
# batch 027 (label_027): com.money.manager.ex.common.CalculatorActivity (29 methods: the class, its anonymous listeners $1, $2, $3 and its Icepick helper $$Icepick) and the Dagger-generated CalculatorActivity_MembersInjector (5 methods). 34 methods in all.
# Rows and printed lines: graphs/MMEX/parts/label_027.md. grep evidence: graphs/MMEX/parts/label_027.grep.txt.
# CALL edges come from auto_calls.json (the calls inside CalculatorActivity and its listeners, the calls into Calculator, the Dagger static inject calls) and are not written here.
# Framework claims cite FW-SRC lines printed for this batch. The AppCompat menu step, the ButterKnife binding, the Dagger component and the Icepick library are not in fw_src: INFERRED.
# Every edge below has a batch 027 method (or S_CALCULATOR) as its destination. The Icepick edges start at MmxBaseFragmentActivity methods, which are another batch's rows.

SCREENS.update({
    'S_CALCULATOR': 'Full-screen calculator (CalculatorActivity): the number, operator, delete, clear and equals keys, and the save icon; it returns the entered amount to the caller',
})

# ---- entry: a caller starts the activity with Calculator.show (startActivityForResult). The framework then creates it.
# Calculator.java:70 builds the intent for CalculatorActivity.class; Calculator.java:77-83 starts it. The creation step is FW-SRC: Instrumentation.newActivity (Instrumentation.java:1170-1174) runs loadClass(...).newInstance(), which initialises the class and runs the constructor.

EV_START = ('SRC common/Calculator.java:70 (intent for CalculatorActivity.class), 77-83 (show: startActivityForResult at 79); '
            'FW-SRC core/java/android/app/ActivityThread.java:2669-2670 (mInstrumentation.newActivity); '
            'FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance() at 1174)')

e('AccountEditActivity$1.onClick', 'CalculatorActivity.<init>', 'INTENT',
  'the initial balance field opens the calculator for a result: Calculator.show (line 307) starts CalculatorActivity',
  evidence='SRC account/AccountEditActivity.java:301-309 (listener 301; onClick 303-308; Calculator.forActivity 304, currency 305, amount 306, show 307); ' + EV_START)

e('EditTransactionCommonFunctions$2.onClick', 'CalculatorActivity.<init>', 'INTENT',
  'a click listener opens the calculator for a result: Calculator.show (line 430) starts CalculatorActivity',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:427-430 (forActivity 427, currency 428, amount 429, show 430); ' + EV_START)

e('EditTransactionCommonFunctions$3.onClick', 'CalculatorActivity.<init>', 'INTENT',
  'a click listener opens the calculator for a result: Calculator.show (line 446) starts CalculatorActivity',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:444-446 (forActivity 444, currency 445, amount 445, show 446); ' + EV_START)



e('PriceEditActivity.onPriceClick', 'CalculatorActivity.<init>', 'INTENT',
  'the price field opens the calculator: Calculator.show (line 140) starts CalculatorActivity',
  evidence='SRC investment/PriceEditActivity.java:135-140 (forActivity 137, amount 138, roundToCurrency 139, show 140); ' + EV_START)

e('SearchParametersFragment.onAmountFromClicked', 'CalculatorActivity.<init>', 'INTENT',
  'the from-amount field opens the calculator: Calculator.show (line 405, Calculator.forFragment) starts CalculatorActivity',
  evidence='SRC search/SearchParametersFragment.java:398-406 (@OnClick at 398; forFragment, amount and show on line 405); ' + EV_START)

e('SearchParametersFragment.onAmountToClicked', 'CalculatorActivity.<init>', 'INTENT',
  'the to-amount field opens the calculator: Calculator.show (line 415, Calculator.forFragment) starts CalculatorActivity',
  evidence='SRC search/SearchParametersFragment.java:408-416 (@OnClick at 408; forFragment, amount and show on line 415); ' + EV_START)

# B6-RESULT1-R3: plain Split.onEvent -> Calculator.<init> partitioned to @SPLIT INTENT in graph_def_mod/03.py (plain edge deleted; built id was E20490343 as computed in spec).

# ---- creation, lifecycle and menu

e('CalculatorActivity.<init>', 'CalculatorActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999)')

e('CalculatorActivity.onCreate', 'S_CALCULATOR', 'ENTERS',
  'onCreate sets the layout (line 115) and wires the keys through initializeControls (line 127): the calculator screen is shown',
  evidence='SRC common/CalculatorActivity.java:111-128 (setContentView at 115, ButterKnife.bind at 118, initializeControls at 127)')

e('CalculatorActivity.onCreate', 'CalculatorActivity.onResume', 'LIFECYCLE',
  'the framework calls onResume after onCreate: ActivityThread.handleResumeActivity calls performResume, which calls Instrumentation.callActivityOnResume',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3556 (r.activity.performResume() in handleResumeActivity, which starts at 3608); FW-SRC core/java/android/app/Activity.java:7098-7107 (performResume calls callActivityOnResume at 7107); FW-SRC core/java/android/app/Instrumentation.java:1353-1355 (callActivityOnResume calls onResume at 1355)')

e('CalculatorActivity.onCreate', 'CalculatorActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:631 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3388 (onCreatePanelMenu calls onCreateOptionsMenu at 3388); SRC common/CalculatorActivity.java:139 (addSaveToolbarIcon); INFERRED AppCompat decides when the panel is prepared (androidx not in fw_src)')

# ---- user actions on the calculator screen (page S_CALCULATOR)

e('S_CALCULATOR', 'CalculatorActivity$1.onClick', 'GUI',
  'a number key or the decimal key is tapped: the listener appends the key text and evaluates the expression',
  gui=['Tap a number key (0-9) or the decimal key'],
  evidence='SRC common/CalculatorActivity.java:88-93 (idButtonKeyNum), 314-331 (listener 314; onClick 316-325; setOnClickListener 330); SRC res/layout/activity_calculator.xml:154, 158 (buttonKeyNumDecimal, buttonKeyNum0); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED the touch dispatch to performClick (View input path not printed)')

e('S_CALCULATOR', 'CalculatorActivity$2.onClick', 'GUI',
  'an operator or parenthesis key is tapped: the listener appends the key text and evaluates the expression',
  gui=['Tap an operator key (+, /, -, x, parentheses)'],
  evidence='SRC common/CalculatorActivity.java:94-98 (idOperatorKeys), 333-346 (listener 333; onClick 335-341; setOnClickListener 345); SRC res/layout/activity_calculator.xml:91, 132 (buttonKeyLeftParenthesis, buttonKeyMultiplication); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED the touch dispatch to performClick (View input path not printed)')

e('S_CALCULATOR', 'CalculatorActivity$3.onClick', 'GUI',
  'the clear key (C) is tapped: the entry is emptied and the expression evaluated',
  gui=['Tap the clear key (C)'],
  evidence='SRC common/CalculatorActivity.java:348-357 (clear listener 350-357; onClick 352-356); SRC res/layout/activity_calculator.xml:87 (buttonKeyClear); FW-SRC core/java/android/view/View.java:6289-6294 (performClick calls the listener at 6294); INFERRED the touch dispatch to performClick (View input path not printed)')

e('S_CALCULATOR', 'CalculatorActivity.onDeleteClicked', 'GUI',
  'the delete key (<=) runs the @OnClick handler: the last character is removed and the expression evaluated',
  gui=['Tap the delete key (<=)'],
  cls='non_standard', via='ButterKnife @OnClick(R.id.deleteButton) at CalculatorActivity.java:236, bound by the generated CalculatorActivity_ViewBinding (INFERRED: the library and generated source are not in the source root)',
  evidence='SRC common/CalculatorActivity.java:236-245 (@OnClick at 236, handler 237-245); SRC res/layout/activity_calculator.xml:99 (deleteButton); auto_calls.json record CalculatorActivity_ViewBinding$1.doClick -> onDeleteClicked (CalculatorActivity_ViewBinding.java:39) is the generated path (batch 028); INFERRED ButterKnife binding (library not read)')

e('S_CALCULATOR', 'CalculatorActivity.onEqualsClicked', 'GUI',
  'the equals key runs the @OnClick handler, which returns the entered amount',
  gui=['Tap the equals key (=)'],
  cls='non_standard', via='ButterKnife @OnClick(R.id.buttonKeyEqual) at CalculatorActivity.java:247, bound by the generated CalculatorActivity_ViewBinding (INFERRED: the library and generated source are not in the source root)',
  evidence='SRC common/CalculatorActivity.java:247-250 (@OnClick at 247, handler 248-250); SRC res/layout/activity_calculator.xml:162 (buttonKeyEqual); auto_calls.json record CalculatorActivity_ViewBinding$2.doClick -> onEqualsClicked (CalculatorActivity_ViewBinding.java:49) is the generated path (batch 028); INFERRED ButterKnife binding (library not read)')

e('S_CALCULATOR', 'CalculatorActivity.onOptionsItemSelected', 'GUI',
  'the framework calls onOptionsItemSelected for the save menu item (MenuHelper.save): returnResult runs',
  gui=['Tap the save (check) icon in the action bar'],
  evidence='SRC MenuHelper.java:37 (save id), 87-88 (save item added in addSaveToolbarIcon); SRC common/CalculatorActivity.java:139 (menu built), 145-151 (save branch calls returnResult at 149); FW-SRC core/java/android/app/Activity.java:3439-3450 (onMenuItemSelected calls onOptionsItemSelected at 3450)')

# ---- Icepick (generated helper CalculatorActivity$$Icepick; the icepick library is not in the dataset)

e('MmxBaseFragmentActivity.onCreate', 'CalculatorActivity$$Icepick.<clinit>', 'FRAMEWORK',
  'Icepick restores the @State fields: the library loads the generated helper CalculatorActivity$$Icepick by reflection, which runs its static initialiser first',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:58-76 (Icepick.restoreInstanceState at 74, super.onCreate at 76); SRC common/CalculatorActivity.java:51, 74-81 (icepick.State import and @State fields); the icepick library is not in the dataset (combined/report/com.money.manager.ex.common/CalculatorActivity$$Icepick.html: "Icepick.java was not found"): INFERRED, source not read')

e('MmxBaseFragmentActivity.onCreate', 'CalculatorActivity$$Icepick.<init>', 'FRAMEWORK',
  'Icepick creates an instance of the generated helper by reflection',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:58-76 (Icepick.restoreInstanceState at 74); SRC common/CalculatorActivity.java:74-81 (@State fields); the icepick library is not in the dataset: INFERRED, source not read')

e('MmxBaseFragmentActivity.onCreate', 'CalculatorActivity$$Icepick.restore', 'FRAMEWORK',
  'Icepick calls the generated restore for the @State fields (roundToCurrencyDecimals, mAmount, mCurrencyId, mExpression) when the activity is created with saved state, for example after a rotation; the app does not guard the call at line 74',
  cls='non_standard', via='icepick library reflection (Icepick.restoreInstanceState at MmxBaseFragmentActivity.java:74)',
  evidence='SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState, unguarded in the app source); SRC common/CalculatorActivity.java:74-81 (@State fields); the icepick library is not in the dataset: INFERRED, source not read')

e('MmxBaseFragmentActivity.onSaveInstanceState', 'CalculatorActivity$$Icepick.save', 'FRAMEWORK',
  'Icepick calls the generated save for the @State fields when the framework saves the activity state',
  cls='non_standard', via='icepick library reflection (Icepick.saveInstanceState at MmxBaseFragmentActivity.java:155)',
  evidence='SRC common/MmxBaseFragmentActivity.java:151-156 (Icepick.saveInstanceState at 155); SRC common/CalculatorActivity.java:74-81 (@State fields); FW-SRC core/java/android/app/ActivityThread.java:4713-4722 (callCallActivityOnSaveInstanceState); FW-SRC core/java/android/app/Instrumentation.java:1385-1387 (callActivityOnSaveInstanceState calls performSaveInstanceState at 1386); FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState at 1496); the icepick library is not in the dataset: INFERRED, source not read')

# ---- Dagger MembersInjector: create and injectMembers have no caller, so their outgoing calls cannot run
# The component injects CalculatorActivity through the static injectX methods (DaggerMmxComponent.java:380-381, auto_calls records), not through a MembersInjector instance.

sup(('CalculatorActivity_MembersInjector.create', 'CalculatorActivity_MembersInjector.<init>'))  # create has no caller, so its call into <init> cannot run

sup(('CalculatorActivity_MembersInjector.injectMembers', 'CalculatorActivity_MembersInjector.injectFormatUtilitiesLazy'),  # injectMembers has no caller
    ('CalculatorActivity_MembersInjector.injectMembers', 'CalculatorActivity_MembersInjector.injectMCurrencyService'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_027.grep.txt)

UNREACHABLE['CalculatorActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (not in the source root). Its only caller record is CalculatorActivity_MembersInjector.create (auto_calls.json, CalculatorActivity_MembersInjector.java:31), and create has no caller record. The component calls the static injectFormatUtilitiesLazy and injectMCurrencyService methods instead (DaggerMmxComponent.java:380-381). No MembersInjector reference exists in the app source (label_027.grep.txt, section A)',
  'auto_calls.json (CalculatorActivity_MembersInjector.java:31; 0 callers of create); label_027.grep.txt sections A and B',
  'INFERRED')

UNREACHABLE['CalculatorActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (not in the source root) with no caller record in auto_calls.json (0 callers). The component does not call it: DaggerMmxComponent.injectCalculatorActivity calls the static inject methods directly (DaggerMmxComponent.java:380-381). No MembersInjector reference exists in the app source (label_027.grep.txt, section A)',
  'python-printed auto_calls query (0 callers); label_027.grep.txt sections A and B',
  'INFERRED')

UNREACHABLE['CalculatorActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (not in the source root) with no caller record for any receiver in auto_calls.json. The component reaches the fields through the static injectFormatUtilitiesLazy and injectMCurrencyService methods (DaggerMmxComponent.java:380-381), so this method never runs. Its two outgoing call records are cut by sup',
  'python-printed auto_calls query (0 callers); auto_calls.json (CalculatorActivity_MembersInjector.java:37-38, outgoing); label_027.grep.txt sections A and B',
  'INFERRED')

# ---- part 029 (2026-10-29)
# batch 029 (label_029): com.money.manager.ex.common.CategoryListFragment, methods 1-40 of 43 (the class, its constructor, the anonymous listeners $1-$8 and their constructors). Batch 030 holds $8.onChildClick, $9.<init> and $9.onGroupClick. Rows and printed lines: graphs/MMEX/parts/label_029.md.
# Page S_CATEGORY_LIST is defined at graph_def.py:1214 and reused here (D9). Its ENTERS edge is written here, from onActivityCreated (the list is set up and shown there).
# CALL edges come from auto_calls.json (the constructors, the calls inside this class, the listener <init> records, the receiver records "...@CategoryListFragment"), so none are written here.
# Library classes (androidx Fragment, LoaderManager, the context menu dispatch, the fragment state save) are not in fw_src: those claims are INFERRED (source not read). FW-SRC is cited only for printed ranges (AbsListView, View, AlertDialog, AlertController).
# No sup cut in this batch: every auto edge out of the methods of this batch can run on API 27 (see label_029.md).
# No UNREACHABLE entry in this batch: every method has a route (see label_029.md, all rows REACHABLE). grep output: graphs/MMEX/parts/label_029.grep.txt.

# ---- lifecycle and loader callbacks (androidx; library source not read: INFERRED where stated)

e('CategoryListActivity.onCreate', 'CategoryListFragment.onActivityCreated', 'LIFECYCLE',
  'the activity adds the fragment in onCreate (fragment transaction, committed); the framework then calls onActivityCreated on it',
  guard='the fragment is not yet in the fragment manager (CategoryListActivity.java:65); a restored fragment is not added again',
  evidence='SRC common/CategoryListActivity.java:63-70 (fragment added and committed); SRC common/CategoryListFragment.java:96-98; INFERRED androidx FragmentManager calls onActivityCreated after the commit (library source not read)')

e('CategoryListFragment.onActivityCreated', 'S_CATEGORY_LIST', 'ENTERS',
  'the category list screen is shown: onActivityCreated sets up the list, the search menu, the context menu and the + button (lines 101-144)',
  evidence='SRC common/CategoryListFragment.java:96-145; SRC common/CategoryListActivity.java:63-70')

e('CategoryListFragment.onActivityCreated', 'CategoryListFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state (checked ids and the filter) while the fragment is alive, for example when the activity is stopped',
  evidence='SRC common/CategoryListFragment.java:96-98, 239-247; INFERRED androidx FragmentManager saves state through onSaveInstanceState (library source not read)')

e('CategoryListFragment.onActivityCreated', 'CategoryListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader(ID_LOADER_CATEGORYSUB, null, this) asks the LoaderManager for the loader; when no loader exists yet, the callbacks get onCreateLoader',
  evidence='SRC common/CategoryListFragment.java:79, 138; INFERRED androidx LoaderManager.initLoader calls LoaderCallbacks.onCreateLoader (library source not read)')

e('CategoryListFragment.restartLoader', 'CategoryListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader(ID_LOADER_CATEGORYSUB) asks the LoaderManager to create a new loader for the new query, so onCreateLoader runs again',
  evidence='SRC common/CategoryListFragment.java:443-445; INFERRED androidx LoaderManager.restartLoader creates the new loader (library source not read)')

e('CategoryListFragment.onCreateLoader', 'CategoryListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader returned at line 275 delivers its cursor to the callbacks when the load finishes; onLoadFinished runs with that cursor',
  evidence='SRC common/CategoryListFragment.java:252-275, 289-290; INFERRED androidx Loader delivers the result to LoaderCallbacks.onLoadFinished (library source not read)')

e('CategoryListFragment.restartLoader', 'CategoryListFragment.onLoaderReset', 'FRAMEWORK',
  'restarting the loader resets the previous one first, so the callbacks get onLoaderReset',
  guard='a loader for id 0 exists already (initLoader ran in onActivityCreated, line 138)',
  evidence='SRC common/CategoryListFragment.java:138, 280-286, 443-445; INFERRED androidx LoaderManager.restartLoader destroys the old loader and calls onLoaderReset (library source not read)')

# ---- user actions on the category list (page S_CATEGORY_LIST)

gui('S_CATEGORY_LIST', 'CategoryListFragment.onCreateContextMenu', 'Long-press a category or subcategory row of the list',
  evidence='SRC common/CategoryListFragment.java:130 (registerForContextMenu on the list), 159-178; FW-SRC core/java/android/widget/AbsListView.java:3223-3246 (performLongPress shows the menu for the child), 3291-3301; FW-SRC core/java/android/view/View.java:12578-12589 (createContextMenu calls the registered listener at 12588); INFERRED the step from showContextMenuForChild to createContextMenu (source not read); INFERRED ExpandableListView long-press (not in fw_src)')

gui('S_CATEGORY_LIST', 'CategoryListFragment.onContextItemSelected', 'Tap Edit, Delete or View transactions in the menu of a row',
  evidence='SRC common/CategoryListFragment.java:175-177 (menu items), 180-227 (switch on the item); INFERRED the context menu item is dispatched to the fragment that registered the menu (androidx; library source not read)')

# ---- dialog buttons: the dialog-creating method calls the listener through AlertDialog (FRAMEWORK, as in label_024)

e('CategoryListFragment.showDialogDeleteCategorySub', 'CategoryListFragment$1.onClick', 'FRAMEWORK',
  'the cannot-delete dialog shows an OK button; the click dismisses the dialog',
  needs_state=state_text('the row is a subcategory (subCategId > 0, line 455) or the category is used by account transactions (CategoryService.isCategoryUsed true, line 457)', ('data',)),
  evidence='SRC common/CategoryListFragment.java:455-472; SRC servicelayer/CategoryService.java:143-147; FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:125-147, 160-167, 344-362, 1021-1023')

e('CategoryListFragment.showDialogDeleteCategorySub', 'CategoryListFragment$2.onClick', 'FRAMEWORK',
  'the confirm delete dialog shows a Cancel button; the click cancels the dialog',
  needs_state=state_text('the row is a category (subCategId <= 0, line 455) and no account transaction uses it (CategoryService.isCategoryUsed false, line 457)', ('data',)),
  evidence='SRC common/CategoryListFragment.java:455-457, 477-506; SRC servicelayer/CategoryService.java:143-147; FW-SRC core/java/com/android/internal/app/AlertController.java:1025-1027, 125-147, 160-167')

e('CategoryListFragment.showDialogDeleteCategorySub', 'CategoryListFragment$3.onClick', 'FRAMEWORK',
  'the confirm delete dialog shows an OK button; the click deletes the category row and restarts the loader',
  needs_state=state_text('the row is a category (subCategId <= 0, line 455) and no account transaction uses it (CategoryService.isCategoryUsed false, line 457)', ('data',)),
  evidence='SRC common/CategoryListFragment.java:455-457, 477-499 (delete at 487-492, restartLoader at 497); SRC servicelayer/CategoryService.java:143-147; FW-SRC core/java/com/android/internal/app/AlertController.java:1021-1023, 125-147, 160-167')

e('CategoryListFragment.showDialogEditCategoryName', 'CategoryListFragment$4.onClick', 'FRAMEWORK',
  'the category name dialog shows a Cancel button; the click cancels the dialog',
  evidence='SRC common/CategoryListFragment.java:560-565; FW-SRC core/java/com/android/internal/app/AlertController.java:1025-1027, 125-147, 160-167')

e('CategoryListFragment.showDialogEditCategoryName', 'CategoryListFragment$5.onClick', 'FRAMEWORK',
  'the category name dialog shows an OK button; the click inserts or updates the category and restarts the loader',
  evidence='SRC common/CategoryListFragment.java:534-559 (createNew 543, update 550, restartLoader 557); FW-SRC core/java/com/android/internal/app/AlertController.java:1021-1023, 125-147, 160-167')

e('CategoryListFragment.showDialogEditSubCategoryName', 'CategoryListFragment$6.onClick', 'FRAMEWORK',
  'the subcategory dialog shows a Cancel button; the click cancels the dialog',
  evidence='SRC common/CategoryListFragment.java:650-655; FW-SRC core/java/com/android/internal/app/AlertController.java:1025-1027, 125-147, 160-167')

e('CategoryListFragment.showDialogEditSubCategoryName', 'CategoryListFragment$7.onClick', 'FRAMEWORK',
  'the subcategory dialog shows an OK button; the click inserts or updates the subcategory row and restarts the loader',
  evidence='SRC common/CategoryListFragment.java:614-649 (returns early at 620-621; restartLoader 647); FW-SRC core/java/com/android/internal/app/AlertController.java:1021-1023, 125-147, 160-167')

e('CategoryListFragment.showTypeSelectorDialog', 'CategoryListFragment$10.onClick', 'FRAMEWORK',
  'the type dialog shows a neutral Cancel button; the click dismisses the dialog',
  evidence='SRC common/CategoryListFragment.java:724-729 (setNeutralButton at 724); FW-SRC core/java/com/android/internal/app/AlertController.java:1029-1030, 125-147, 160-167')

e('CategoryListFragment.showTypeSelectorDialog', 'CategoryListFragment$11.onClick', 'FRAMEWORK',
  'a row of the single-choice type list is tapped (category or subcategory); the matching add dialog opens',
  evidence='SRC common/CategoryListFragment.java:707-721 (which == 0 at 714; showDialogEditCategoryName 715, showDialogEditSubCategoryName 717); FW-SRC core/java/com/android/internal/app/AlertController.java:1134-1146 (single-choice item click calls the listener at 1142)')

# ---- part 028 (2026-10-29)
# batch 028 (label_028): com.money.manager.ex.common.CalculatorActivity_ViewBinding (7 methods: its two constructors, unbind, and the listener classes $1 and $2 with their constructors and doClick) and com.money.manager.ex.common.CategoryListActivity (4 methods: <clinit>, <init>, onCreate, onKeyUp). 11 methods in all.
# Rows and printed lines: graphs/MMEX/parts/label_028.md. grep evidence: graphs/MMEX/parts/label_028.grep.txt.
# CALL edges between the generated methods and the in-app calls come from auto_calls.json and are not written here. The ButterKnife reflection call from CalculatorActivity.onCreate is not in auto_calls.json, so it is written here (cls='non_standard').
# ButterKnife and the generated classes are not in the source root: their claims are INFERRED.
# Page S_CALCULATOR is defined in label_027.py (batch 027, not merged yet). Page S_CATEGORY_LIST is defined at graph_def.py:1214.
# No ENTERS edge is written here. The ENTERS edge to S_CATEGORY_LIST is written by label_029.py (CategoryListFragment.onActivityCreated, graph_def.py:2311).
# batch 027 also writes S_CALCULATOR -> CalculatorActivity.onDeleteClicked and -> CalculatorActivity.onEqualsClicked directly (label_027.py). Both routes are kept here; the orchestrator decides whether to drop batch 027's two edges (see the batch 028 report).

# ---- CategoryListActivity: entry from another app (exported=true, PICK and EDIT filters)

e('S_ENTRY', 'CategoryListActivity.<init>', 'ENTRY',
  'another app sends an ACTION_PICK or ACTION_EDIT intent to the exported CategoryListActivity',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to CategoryListActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:204-209 (exported=true; PICK and EDIT filters); FW-SRC core/java/android/app/ActivityThread.java:2669-2670 (mInstrumentation.newActivity); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance() at 1174)')

e('S_ENTRY', 'CategoryListActivity.<clinit>', 'ENTRY',
  'the first CategoryListActivity instance (the exported-intent start above) initialises the class',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to CategoryListActivity (exported=true)', ('other_app',)),
  evidence='SRC common/CategoryListActivity.java:41 (FRAGMENTTAG is built by a method call, so it is not a compile-time constant and the class has a static initialiser); SRC AndroidManifest.xml:204-209; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

# ---- in-app callers that start CategoryListActivity for a pick (ACTION_PICK). The class initialiser edge is INFERRED (Java language rule), as for PayeeActivity.

e('EditTransactionCommonFunctions$4.onClick', 'CategoryListActivity.<init>', 'INTENT',
  'tap the category field in the transaction editor when no split is selected: startActivityForResult(ACTION_PICK) starts CategoryListActivity',
  gui=['Tap the category field in the transaction editor'],
  guard='no split categories are selected: the intent is built only when isSplitSelected() is false (EditTransactionCommonFunctions.java:462)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:459-466 (setOnClickListener 459; isSplitSelected 462; new Intent 464; ACTION_PICK 465; startActivityForResult 466); FW-SRC core/java/android/app/Instrumentation.java:1170-1174')

e('EditTransactionCommonFunctions$4.onClick', 'CategoryListActivity.<clinit>', 'INTENT',
  'the first CategoryListActivity instance (the start above) initialises the class',
  gui=['Tap the category field in the transaction editor'],
  guard='no split categories are selected: the intent is built only when isSplitSelected() is false (EditTransactionCommonFunctions.java:462)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:459-466; SRC common/CategoryListActivity.java:41; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

e('SearchParametersFragment$2.onClick', 'CategoryListActivity.<init>', 'INTENT',
  'tap the category field on the search screen: startActivityForResult(ACTION_PICK) starts CategoryListActivity',
  gui=['Tap the category field on the search screen'],
  evidence='SRC search/SearchParametersFragment.java:199-205 (listener set at 199; onClick 201; new Intent 202; ACTION_PICK 203; startActivityForResult 204); FW-SRC core/java/android/app/Instrumentation.java:1170-1174')

e('SearchParametersFragment$2.onClick', 'CategoryListActivity.<clinit>', 'INTENT',
  'the first CategoryListActivity instance (the start above) initialises the class',
  gui=['Tap the category field on the search screen'],
  evidence='SRC search/SearchParametersFragment.java:199-205; SRC common/CategoryListActivity.java:41; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

e('SplitCategoriesActivity.showCategorySelector', 'CategoryListActivity.<init>', 'INTENT',
  'a category request event (CategoryRequestedEvent) makes the split screen start CategoryListActivity with ACTION_PICK',
  evidence='SRC transactions/SplitCategoriesActivity.java:213-216 (onEvent(CategoryRequestedEvent) calls showCategorySelector at 215); SRC transactions/SplitCategoriesActivity.java:307-314 (new Intent 308; ACTION_PICK 309; startActivityForResult 314); FW-SRC core/java/android/app/Instrumentation.java:1170-1174')

e('SplitCategoriesActivity.showCategorySelector', 'CategoryListActivity.<clinit>', 'INTENT',
  'the first CategoryListActivity instance (the start above) initialises the class',
  evidence='SRC transactions/SplitCategoriesActivity.java:307-314; SRC common/CategoryListActivity.java:41; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

# ---- creation, lifecycle and the Back key

e('CategoryListActivity.<init>', 'CategoryListActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999)')

gui('S_CATEGORY_LIST', 'CategoryListActivity.onKeyUp', 'Press Back while the category list is in front',
  evidence='FW-SRC core/java/android/app/Activity.java:3255-3272 (dispatchKeyEvent passes the key to event.dispatch at 3272); FW-SRC core/java/android/view/KeyEvent.java:2709-2715 (ACTION_UP calls receiver.onKeyUp at 2715); SRC common/CategoryListActivity.java:73-84 (onKeyUp 74; KEYCODE_BACK 75; setResultAndFinish 80)')

# ---- ButterKnife binding of CalculatorActivity (generated class not in the source root: INFERRED)

e('CalculatorActivity.onCreate', 'CalculatorActivity_ViewBinding.<init>(CalculatorActivity)', 'CALL',
  'ButterKnife.bind(this) builds the generated binding for the activity, which binds the @OnClick handlers and the views',
  cls='non_standard', via='ButterKnife.bind(this) (library): the generated CalculatorActivity_ViewBinding is built by reflection (INFERRED, library and generated source not read)',
  evidence='SRC common/CalculatorActivity.java:118 (ButterKnife.bind(this)); INFERRED ButterKnife generated binding (label_028.grep.txt section D: the generated report says the source file was not found)')

e('S_CALCULATOR', 'CalculatorActivity_ViewBinding$1.doClick', 'GUI',
  'tap the delete key (<=): the @OnClick listener of the generated binding calls onDeleteClicked',
  gui=['Tap the delete key (<=)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC common/CalculatorActivity.java:236-237 (@OnClick(R.id.deleteButton) at 236; onDeleteClicked at 237); SRC res/layout/activity_calculator.xml:98-100 (deleteButton); auto_calls.json:39476-39477 (CalculatorActivity_ViewBinding$1.doClick -> CalculatorActivity.onDeleteClicked); INFERRED ButterKnife listener')

e('S_CALCULATOR', 'CalculatorActivity_ViewBinding$2.doClick', 'GUI',
  'tap the equals key (=): the @OnClick listener of the generated binding calls onEqualsClicked, which returns the entered amount',
  gui=['Tap the equals key (=)'],
  cls='non_standard', via='ButterKnife @OnClick listener attached by the generated binding (INFERRED, generated class and library not read)',
  evidence='SRC common/CalculatorActivity.java:247-248 (@OnClick(R.id.buttonKeyEqual) at 247; onEqualsClicked at 248); SRC res/layout/activity_calculator.xml:161-164 (buttonKeyEqual at 162); auto_calls.json:37800-37801 (CalculatorActivity_ViewBinding$2.doClick -> CalculatorActivity.onEqualsClicked); INFERRED ButterKnife listener')

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_028.grep.txt)

UNREACHABLE['CalculatorActivity_ViewBinding.unbind'] = ('no_trigger_in_app',
  'ButterKnife-generated method (not in the source root). ButterKnife.bind(this) at CalculatorActivity.java:118 discards the returned Unbinder, CalculatorActivity has no onDestroy, and no caller record for unbind exists in auto_calls.json (0 callers). No Unbinder reference exists in the app source (label_028.grep.txt sections A-C)',
  'SRC common/CalculatorActivity.java:118; label_028.grep.txt sections A-C; python-printed auto_calls query (0 callers)',
  'INFERRED')

# ---- part 030 (2026-10-29)
# batch 030 (label_030): com.money.manager.ex.common.CategoryListFragment, methods 41-43 of 43: CategoryListFragment$8.onChildClick, CategoryListFragment$9.<init>, CategoryListFragment$9.onGroupClick. Rows and printed lines: graphs/MMEX/parts/label_030.md.
# Both listeners are installed in addListClickHandlers only when the list was opened with ACTION_PICK (CategoryListFragment.java:661-662 and 681-682). The page S_CATEGORY_LIST is defined at graph_def.py:1214 and reused here (D9).
# No ENTERS edge is written to S_CATEGORY_LIST: its ENTERS edge is in batch 029 (label_029.py:15), and batches 028 and 029 own the decision about it.
# CALL edges come from auto_calls.json: the listener constructor record (auto_calls.json:38846-38849) and the calls inside the two listeners (auto_calls.json:34974-35012 and 36998-37028). None are written here (D7). No auto edge out of these methods is blocked on API 27, so no sup cut is written.
# ExpandableListView is not in fw_src, so the dispatch of a row click to the listener is INFERRED (grep: graphs/MMEX/parts/label_030.grep.txt, section A).
# ExpandableListFragment.java:364 (mList.setOnChildClickListener(this)) would replace the picker listener if it ran after CategoryListFragment.java:662. It sits in onContentChanged, which no app code calls (grep: label_030.grep.txt, section C; the androidx Fragment base is not read: INFERRED).
# No UNREACHABLE entry in this batch: each method has a route through the picker (label_030.md).

# ---- user actions on the category list in picker mode (page S_CATEGORY_LIST). The picker is opened by tapping the category field of the transaction editor (EditTransactionCommonFunctions.java:459-466).

gui('S_CATEGORY_LIST', 'CategoryListFragment$8.onChildClick', 'Tap a subcategory row in the category list opened to pick a category',
  guard='the list was opened with ACTION_PICK, so the child-click listener is installed (CategoryListFragment.java:661-662)',
  evidence='SRC common/CategoryListFragment.java:661-662, 665-676 (the listener sets the chosen sub-category at 671 and calls setResultAndFinish at 675); SRC transactions/EditTransactionCommonFunctions.java:459-466 (the category field opens the picker with ACTION_PICK at 465); SRC common/CategoryListActivity.java:56-57 (the intent action becomes mAction); INFERRED ExpandableListView calls OnChildClickListener on a child-row click (ExpandableListView not in fw_src, not read)')

gui('S_CATEGORY_LIST', 'CategoryListFragment$9.onGroupClick', 'Tap a top-level category row in the category list opened to pick a category',
  guard='the list was opened with ACTION_PICK, so the group-click listener is installed (CategoryListFragment.java:661, 681-682)',
  evidence='SRC common/CategoryListFragment.java:681-684, 686-698 (the category is marked at 690; setResultAndFinish is called at 695 only when the category has no sub-categories, see 693-694); SRC transactions/EditTransactionCommonFunctions.java:459-466 (picker opened with ACTION_PICK); SRC common/CategoryListActivity.java:56-57; INFERRED ExpandableListView calls OnGroupClickListener on a group-row click (ExpandableListView not in fw_src, not read)')

# ---- part 031 (2026-10-29)
# batch 031 (label_031): com.money.manager.ex.common.CommonSplitCategoryLogic (static utility class, 5 methods) and com.money.manager.ex.common.ExpandableListFragment (21 methods, including the class constructor) with its anonymous listeners $1 and $2 (4 methods). 30 methods in all; rows and printed lines: graphs/MMEX/parts/label_031.md. grep evidence: graphs/MMEX/parts/label_031.grep.txt.
# ExpandableListFragment extends androidx Fragment (ExpandableListFragment.java:48-49). androidx is not in fw_src, so the lifecycle claims are INFERRED (library not read). No app code creates an ExpandableListFragment directly (grep.txt section A). Its subclasses are BaseExpandableListFragment (BaseExpandableListFragment.java:46) and CategoryListFragment (CategoryListFragment.java:73, through Base).
# The list is shown on page S_CATEGORY_LIST (graph_def.py:1214). The page is reused here, not redefined (D9).
# CALL edges come from graphs/MMEX/auto_calls.json (D7) and are not written here. grep.txt section C lists every auto record into this batch. The three e() edges and one gui() edge below have no auto record (checked in grep.txt sections C and D).
# No sup() cut is needed: no auto CALL record enters an UNREACHABLE method of this batch. The auto CALL edges that leave the UNREACHABLE bodies (setSelection, getSelectedId, getSelectedPosition, onContentChanged) point to methods that are also reached from other routes.

# ---- fragment lifecycle (androidx Fragment; library not read: INFERRED)

e('BaseExpandableListFragment.onCreate', 'ExpandableListFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate; BaseExpandableListFragment and CategoryListFragment do not override onCreateView (BaseExpandableListFragment.java:114 is commented out), so the inherited body runs',
  evidence='SRC common/BaseExpandableListFragment.java:61-70, 114; SRC common/ExpandableListFragment.java:98-100; SRC common/CategoryListFragment.java:72-73; grep label_031.grep.txt section A; INFERRED androidx Fragment lifecycle (library not read)')

e('BaseExpandableListFragment.onViewCreated', 'ExpandableListFragment.onDestroyView', 'LIFECYCLE',
  'the framework destroys the view after it was created in onViewCreated, when the fragment leaves the screen (the activity finishes or the fragment is removed); no subclass overrides onDestroyView',
  evidence='SRC common/ExpandableListFragment.java:140-144; SRC common/BaseExpandableListFragment.java:224-236; grep label_031.grep.txt section A (onDestroyView lines); precedent graph_def.py:1299 (BudgetDetailFragment.onViewCreated -> onDestroyView); INFERRED androidx Fragment lifecycle (library not read)')

# ---- framework dispatch of the Handler runnable (android.os.Handler is in fw_src)

e('ExpandableListFragment.ensureList', 'ExpandableListFragment$1.run', 'FRAMEWORK',
  'ensureList posts mRequestFocus to mHandler (created at line 56); the Handler dispatches the message callback on the looper of the thread that created it, which runs the runnable when the message reaches the front of the queue',
  evidence='SRC common/ExpandableListFragment.java:56, 58-62, 329; SRC fw_src/android-8.1.0_r1/core/java/android/os/Handler.java:355 (post), 596 (sendMessageDelayed), 97-99 (dispatchMessage calls handleCallback), 789-790 (handleCallback runs message.callback.run()); SRC fw_src/android-8.1.0_r1/core/java/android/os/Looper.java:164 (msg.target.dispatchMessage); INFERRED the fragment is created on the main thread (androidx lifecycle, library not read)')

# ---- user actions on the category list (page S_CATEGORY_LIST)

gui('S_CATEGORY_LIST', 'ExpandableListFragment$2.onItemClick', 'Tap a row of the category list (plain item click)',
  evidence='SRC common/ExpandableListFragment.java:64-68, 321 (ensureList registers the listener); SRC fw_src/android-8.1.0_r1/core/java/android/widget/AdapterView.java:290, 314-318 (performItemClick calls the listener); SRC common/CategoryListFragment.java:662-665, 681 (child and group listeners set in ACTION_PICK mode); INFERRED ExpandableListView is not in fw_src (ListView.java is), so whether a tap on a group or child row reaches this AdapterView listener is not read')

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_031.grep.txt sections A, B, C)

UNREACHABLE['CommonSplitCategoryLogic.<init>'] = (
  'no_trigger_in_app',
  'implicit default constructor of a class that has only static methods (CommonSplitCategoryLogic.java:31, no constructor declared). The class is never instantiated: the references in the app source root are import lines, the class declaration and static calls (grep.txt section A), and no subclass exists. No auto record enters <init> (section C). The constructor never runs',
  'SRC common/CommonSplitCategoryLogic.java:31; grep label_031.grep.txt sections A, C',
  'SOURCE')

UNREACHABLE['ExpandableListFragment.getSelectedId'] = (
  'no_trigger_in_app',
  'public method (lines 187-190), a getter for callers. Its name occurs in the app source root only at the declaration and in its body (ExpandableListFragment.java:187, 189), so no app caller exists (grep.txt section A). No auto record enters it (section C). Its body (mList.getSelectedId()) is never reached. Its only outgoing auto record is a CALL to ensureList (section C, line 188), which is not a reason to run it',
  'SRC common/ExpandableListFragment.java:187-190; grep label_031.grep.txt sections A, C',
  'SOURCE')

UNREACHABLE['ExpandableListFragment.getSelectedPosition'] = (
  'no_trigger_in_app',
  'public method (lines 182-185), a getter for callers. Its name occurs in the app source root only at the declaration and in its body (ExpandableListFragment.java:182, 184), so no app caller exists (grep.txt section A). No auto record enters it (section C). Its body (mList.getSelectedPosition()) is never reached. Its only outgoing auto record is a CALL to ensureList (section C, line 183), which is not a reason to run it',
  'SRC common/ExpandableListFragment.java:182-185; grep label_031.grep.txt sections A, C',
  'SOURCE')

UNREACHABLE['ExpandableListFragment.setSelection'] = (
  'no_trigger_in_app',
  'public method (lines 177-180). In the app source root its name occurs at the declaration and body (ExpandableListFragment.java:177, 179) and in spinner and EditText calls. AbsListFragment.setSelection (SRC AbsListFragment.java:124) belongs to another class hierarchy: this fragment extends androidx Fragment (lines 48-49). No caller on an ExpandableListFragment receiver and no auto record enters it (grep.txt sections A, C)',
  'SRC common/ExpandableListFragment.java:48-49, 177-180; SRC AbsListFragment.java:124; grep label_031.grep.txt sections A, C',
  'SOURCE')

UNREACHABLE['ExpandableListFragment.onChildClick'] = (
  'no_trigger_in_app',
  'public @Override (lines 344-348) of OnChildClickListener, returns false. The fragment becomes the child listener only in onContentChanged (line 364), and onContentChanged has no caller (grep.txt section A). CategoryListFragment sets its own child listener (anonymous class at CategoryListFragment.java:662-665) in ACTION_PICK mode, and no subclass overrides onChildClick. The body never runs',
  'SRC common/ExpandableListFragment.java:344-348, 354-372; SRC common/CategoryListFragment.java:662-665; grep label_031.grep.txt sections A, C; INFERRED the androidx Fragment does not call onContentChanged (library not read)',
  'INFERRED')

UNREACHABLE['ExpandableListFragment.onGroupExpand'] = (
  'no_trigger_in_app',
  'public @Override (lines 332-336), empty TODO body. The fragment becomes the group-expand listener only in onContentChanged (line 365), and onContentChanged has no caller (grep.txt section A). No other class registers this fragment, and no subclass overrides onGroupExpand (HomeFragment.java:724 is an anonymous listener in another class). The body never runs',
  'SRC common/ExpandableListFragment.java:332-336, 354-372; SRC home/HomeFragment.java:724; grep label_031.grep.txt sections A, C; INFERRED the androidx Fragment does not call onContentChanged (library not read)',
  'INFERRED')

UNREACHABLE['ExpandableListFragment.onGroupCollapse'] = (
  'no_trigger_in_app',
  'public @Override (lines 338-342), empty TODO body. The fragment becomes the group-collapse listener only in onContentChanged (line 366), and onContentChanged has no caller (grep.txt section A). No other class registers this fragment, and no subclass overrides onGroupCollapse (HomeFragment.java:712 is an anonymous listener in another class). The body never runs',
  'SRC common/ExpandableListFragment.java:338-342, 354-372; SRC home/HomeFragment.java:712; grep label_031.grep.txt sections A, C; INFERRED the androidx Fragment does not call onContentChanged (library not read)',
  'INFERRED')

UNREACHABLE['ExpandableListFragment.onContentChanged'] = (
  'no_trigger_in_app',
  'public method without @Override (lines 354-372). The app source root has no caller: its only occurrence is the declaration (grep.txt section A). Its body would register this fragment as the child, group-expand and group-collapse listener (lines 364-366) and reset the adapter (line 369). The superclass androidx Fragment is not read, and it is INFERRED that the framework never calls an app method of this name',
  'SRC common/ExpandableListFragment.java:354-372; grep label_031.grep.txt sections A, C; INFERRED androidx Fragment (library not read)',
  'INFERRED')

UNREACHABLE['ExpandableListFragment.onCreateContextMenu'] = (
  'no_trigger_in_app',
  'public @Override (lines 350-352), empty body. The only registration is registerForContextMenu(getExpandableListView()) in CategoryListFragment (CategoryListFragment.java:130). That makes the fragment the list listener (android.app.Fragment.registerForContextMenu sets view.setOnCreateContextMenuListener(this), fw_src Fragment.java:1937-1938; the androidx version is not read). View dispatches to that listener (View.java:12587-12588), and the receiver is a CategoryListFragment, whose override (CategoryListFragment.java:159-178) does not call super (grep.txt section A: the super.onCreateContextMenu lines are in other classes; section C: no auto record). No ExpandableListFragment instance is created directly (section A), so the base body never runs',
  'SRC common/ExpandableListFragment.java:350-352; SRC common/CategoryListFragment.java:130, 159-178; fw_src/android-8.1.0_r1/core/java/android/app/Fragment.java:1937-1938; fw_src/android-8.1.0_r1/core/java/android/view/View.java:12587-12588; grep label_031.grep.txt sections A, C',
  'SOURCE')

# ---- part 032 (2026-10-29)
# batch 032 (label_032): com.money.manager.ex.common.MmxBaseFragmentActivity (26 methods, including the anonymous listeners $1 and $2 and the two lambdas), MmxCursorLoader (3) and MoneyParcelConverter (3). Rows and printed lines: graphs/MMEX/parts/label_032.md. grep evidence: graphs/MMEX/parts/label_032.grep.txt.
# Scratch (not evidence): graphs/MMEX/scratch/batch032_auto_hits.txt lists the auto_calls.json records for this batch.
# CALL edges come from auto_calls.json (the super calls of the subclasses, the calls inside this class, the anonymous listeners, the Money$$Parcelable calls), so none are written here.
# Written here: the edges that auto data cannot give (EventBus, the activity lifecycle, the loader thread), and the currency edit page S_CURRENCY_EDIT with its GUI edges to the two listeners (no screen key existed for that form, grep of graph_def.py and parts found none).

# ---- EventBus subscriber in the base activity (greenrobot EventBus: library source not read, INFERRED)

e('MmxBaseFragmentActivity.onStart', 'MmxBaseFragmentActivity.onEvent', 'REGISTER',
  'the activity registers itself on EventBus in onStart; EventBus calls the @Subscribe method onEvent for ErrorRaisedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at MmxBaseFragmentActivity.java:141, @Subscribe onEvent(ErrorRaisedEvent) at 167-168 (library source not read, INFERRED)',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-146 (register at 141, unregister at 146), 167-171 (@Subscribe at 167); SRC log/DebugTree.java:45-46; SRC log/ScreenTree.java:26-27; INFERRED EventBus library source not read')

# REGISTER edges are skipped by reachability, so the two ASYNC edges below carry the route from the Timber trees to onEvent.
e('DebugTree.log', 'MmxBaseFragmentActivity.onEvent', 'ASYNC',
  'a debug build logs an error through Timber while the activity is registered: DebugTree posts ErrorRaisedEvent and EventBus calls onEvent',
  env=env_text('an error is logged through Timber while the activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/DebugTree.java:45-46 (posts only when a subscriber exists); SRC MmexApplication.java:134-135 (DebugTree is planted in the debug branch); SRC common/MmxBaseFragmentActivity.java:167-168; INFERRED EventBus library source not read')

e('ScreenTree.log', 'MmxBaseFragmentActivity.onEvent', 'ASYNC',
  'a release build logs an error through Timber while the activity is registered: ScreenTree posts ErrorRaisedEvent and EventBus calls onEvent (the debug build plants DebugTree instead)',
  env=env_text('an error is logged through Timber while the activity is registered (DebugTree or ScreenTree posts ErrorRaisedEvent)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(ErrorRaisedEvent) to the @Subscribe method onEvent (library dispatch, INFERRED)',
  evidence='SRC log/ScreenTree.java:26-27; SRC MmexApplication.java:134-140 (ScreenTree is planted in the else branch, release only); SRC common/MmxBaseFragmentActivity.java:167-168; INFERRED EventBus library source not read')

# ---- activity lifecycle (framework, source read in fw_src)

e('MmxBaseFragmentActivity.onStart', 'MmxBaseFragmentActivity.onStop', 'LIFECYCLE',
  'the framework stops the activity after onStart when it leaves the foreground (the Home key, or another activity opens on top); no subclass overrides onStop, so this inherited body runs',
  evidence='SRC common/MmxBaseFragmentActivity.java:134-149; grep label_032.grep.txt section G (no subclass of MmxBaseFragmentActivity declares onStop); FW-SRC core/java/android/app/Activity.java:7159 (performStop), 7181 (callActivityOnStop); FW-SRC core/java/android/app/Instrumentation.java:1374-1375')

# ---- loader thread (androidx CursorLoader: library not read, INFERRED)

e('MmxCursorLoader.<init>(Context,Uri,Select)', 'MmxCursorLoader.loadInBackground', 'ASYNC',
  'the LoaderManager starts the loader that the three-argument constructor creates, and the loader calls loadInBackground to query the data off the UI thread',
  cls='non_standard', via='androidx CursorLoader (AsyncTaskLoader): startLoading runs loadInBackground on a worker thread (library not read, INFERRED)',
  evidence='SRC common/MmxCursorLoader.java:32-33, 39-43, 46-53; SRC home/HomeFragment.java:266 (creates the loader in onCreateLoader); INFERRED androidx CursorLoader source not read')

# ---- currency edit form: the cancel and done buttons (page S_CURRENCY_EDIT; its ENTERS edge is written by the batch that owns CurrencyEditActivity.onCreate)

SCREENS.update({
    'S_CURRENCY_EDIT': 'Currency edit form (CurrencyEditActivity): its fields, and the cancel and done buttons from action_buttons.xml (currency_edit_activity.xml:208; that layout has no toolbar)',
})

e('S_CURRENCY_EDIT', 'MmxBaseFragmentActivity$1.onClick', 'GUI',
  'the user taps the cancel button on the currency edit form: the listener calls onActionCancelClick, which CurrencyEditActivity overrides and which finishes the activity',
  evidence='SRC currency/CurrencyEditActivity.java:63-66, 83; SRC common/MmxBaseFragmentActivity.java:102, 176-179, 185-191, 209-219; SRC res/layout/currency_edit_activity.xml:208; SRC res/layout/action_buttons.xml:22, 28; SRC res/layout/actionbar_button_cancel_done.xml:30')

e('S_CURRENCY_EDIT', 'MmxBaseFragmentActivity$2.onClick', 'GUI',
  'the user taps the done button on the currency edit form: the listener calls onActionDoneClick, which CurrencyEditActivity overrides; it saves and finishes when save() succeeds',
  evidence='SRC currency/CurrencyEditActivity.java:69-76; SRC common/MmxBaseFragmentActivity.java:176-179, 185-191, 222-226; SRC res/layout/actionbar_button_cancel_done.xml:46')

# ---- auto edges that cannot run: cut the exact edge only; the cha edges to the overrides stay (label_025.py convention)
# $1 and $2 are created only where the view has action_cancel or action_done (showStandardToolbarActions(View,int,int), lines 211-227). The toolbar of BudgetsActivity (toolbar.xml) has neither, so at runtime only CurrencyEditActivity creates them, and it overrides both callbacks (CurrencyEditActivity.java:63 and 69).

sup(('MmxBaseFragmentActivity$1.onClick', 'MmxBaseFragmentActivity.onActionCancelClick'))  # line 217
sup(('MmxBaseFragmentActivity$2.onClick', 'MmxBaseFragmentActivity.onActionDoneClick'))  # line 225

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_032.grep.txt)

UNREACHABLE['MmxBaseFragmentActivity.onPermissionGranted'] = (
  'no_trigger_in_app',
  'public method that launches openDocumentLauncher (line 271). Nothing in src/main calls it: grep finds only the declaration (Java, res and manifest), and it is not an XML onClick target. With no caller the launcher is never started, so its callback lambda$onCreate$0 never runs',
  'SRC common/MmxBaseFragmentActivity.java:265-272; grep label_032.grep.txt section A',
  'SOURCE')

UNREACHABLE['MmxBaseFragmentActivity.openDirectoryPicker'] = (
  'no_trigger_in_app',
  'public method that launches directoryPickerLauncher (line 277). Nothing in src/main calls it: grep finds only the declaration (Java, res and manifest). With no caller the launcher is never started, so its callback lambda$onCreate$1 never runs',
  'SRC common/MmxBaseFragmentActivity.java:274-278; grep label_032.grep.txt section B',
  'SOURCE')

UNREACHABLE['MmxBaseFragmentActivity.lambda$onCreate$0'] = (
  'no_trigger_in_app',
  'result callback of openDocumentLauncher (registered at line 78). The callback runs only after openDocumentLauncher.launch(), which is called only from onPermissionGranted (line 271), and that method has no caller (grep section A). The REGISTER edge from onCreate (auto lambdas record, line 78) does not make it reachable. The androidx ActivityResult dispatch is INFERRED (library not read)',
  'SRC common/MmxBaseFragmentActivity.java:78-85, 271; grep label_032.grep.txt sections A, C, I',
  'INFERRED')

UNREACHABLE['MmxBaseFragmentActivity.lambda$onCreate$1'] = (
  'no_trigger_in_app',
  'result callback of directoryPickerLauncher (registered at line 87). The callback runs only after directoryPickerLauncher.launch() at line 277, which is called only from openDirectoryPicker, and that method has no caller (grep section B). The REGISTER edge from onCreate (auto lambdas record, line 87) does not make it reachable. The androidx ActivityResult dispatch is INFERRED (library not read)',
  'SRC common/MmxBaseFragmentActivity.java:87-95, 277; grep label_032.grep.txt sections B, C, I',
  'INFERRED')

UNREACHABLE['MmxBaseFragmentActivity.onActionCancelClick'] = (
  'no_trigger_in_app',
  'base body returns true (lines 234-236). Its only call in the base class is the exact call at line 217 in the cancel listener $1.onClick. $1 is created only where the view has action_cancel: CurrencyEditActivity through action_buttons.xml (grep F). The BudgetsActivity toolbar (toolbar.xml) has no such view. CurrencyEditActivity overrides onActionCancelClick (line 63), so the override runs on that receiver. No super.onActionCancelClick call exists (grep section D). The exact edge $1.onClick to this body is cut by sup; the cha edges to the overrides stay',
  'SRC common/MmxBaseFragmentActivity.java:209-236; SRC currency/CurrencyEditActivity.java:63; SRC budget/BudgetsActivity.java:48; grep label_032.grep.txt sections D, F',
  'SOURCE')

UNREACHABLE['MmxCursorLoader.<init>(Context)'] = (
  'no_trigger_in_app',
  'one-argument constructor (lines 35-37). Every new MmxCursorLoader in src/main passes three arguments (context, uri and query), and no class extends MmxCursorLoader (grep section E). With no caller the constructor never runs',
  'SRC common/MmxCursorLoader.java:35-37; grep label_032.grep.txt section E',
  'SOURCE')

# ---- part 033 (2026-10-29)
# batch 033 (label_033): WebViewActivity (+$1), AmountEnteredEvent, ListItemClickedEvent, AbsListFragment (+$1, $2), ContextMenuIds. Rows: graphs/MMEX/parts/label_033.md; grep: label_033.grep.txt.
# CALL edges come from auto_calls.json (none written here, except the sup cuts below). AmountEnteredEvent.<init> is reached through its auto CALL from AmountInputDialog$7.onClick (batch 024).

e('AccountListActivity.onCreate', 'AbsListFragment.onCreateView', 'FRAMEWORK',
  'the activity adds AccountListFragment in onCreate (fragment transaction, committed); the framework then creates the fragment view by calling onCreateView, which AccountListFragment inherits (no override: grep G11)',
  guard='no fragment with id R.id.content yet (AccountListActivity.java:54-55); a restored activity does not add it again',
  evidence='SRC account/AccountListActivity.java:47, 54-56; SRC AbsListFragment.java:77-80; SRC account/AccountListFragment.java (no onCreateView override; grep G11); INFERRED androidx FragmentManager calls onCreateView after the commit (library source not read)')

e('AbsListFragment.onViewCreated', 'AbsListFragment.onDestroyView', 'LIFECYCLE',
  'the framework calls onDestroyView when the fragment view is destroyed; the view exists only after onCreateView and onViewCreated have run (no onDestroyView override in AccountListFragment or BaseListFragment: grep G10)',
  guard='onViewCreated has run, so the view exists',
  evidence='SRC AbsListFragment.java:86-89, 95-102; SRC common/BaseListFragment.java:63-67 (super call at 66); INFERRED androidx Fragment calls onDestroyView when the view is destroyed (library source not read); pattern as graph_def.py:1299')

e('AbsListFragment.ensureList', 'AbsListFragment$2.run', 'FRAMEWORK',
  'ensureList posts mRequestFocus to the handler at its end (mHandler.post); the handler runs run() later on the main looper',
  evidence='SRC AbsListFragment.java:266-319 (ensureList; post at 318), 49-53 (run at 50-52); FW-SRC core/java/android/os/Handler.java:355-358 (post queues the runnable)')

gui('S_ACCOUNT_LIST', 'AbsListFragment$1.onItemClick', 'Tap a row of the account list; onListItemClick then opens the row context menu (AccountListFragment.java:256-259)',
  evidence='SRC AbsListFragment.java:41-46 (mOnClickListener; onItemClick calls onListItemClick at 44), 306 (setOnItemClickListener); FW-SRC core/java/android/widget/AdapterView.java:314-318 (performItemClick calls the listener at 318); FW-SRC core/java/android/widget/AbsListView.java:3122-3130 (performItemClick at 3127); INFERRED the touch-up path reaches performItemClick (source not read)')

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
  'SRC AbsListFragment.java:124-127; SRC common/ExpandableListFragment.java:48-49, 177-180; grep label_033.grep.txt G4, G5',
  'SOURCE')

UNREACHABLE['AbsListFragment.getSelectedItemPosition'] = (
  'no_trigger_in_app',
  'public getter with no caller in app source: grep G3 finds only its definition and the ListView call inside it (AbsListFragment.java:132-135); the other getSelectedItemPosition calls in app/src are on spinner fields',
  'SRC AbsListFragment.java:132-135; grep label_033.grep.txt G3',
  'SOURCE')

UNREACHABLE['AbsListFragment.getSelectedItemId'] = (
  'no_trigger_in_app',
  'public getter with no caller in app source: grep G3 finds only its definition and the ListView call inside it (AbsListFragment.java:140-142); no getSelectedItemId call exists on any AbsListFragment receiver',
  'SRC AbsListFragment.java:140-143; grep label_033.grep.txt G3',
  'SOURCE')

UNREACHABLE['ListItemClickedEvent.<init>'] = (
  'no_trigger_in_app',
  'constructor called only from CloudItemViewHolder$1.onClick (CloudItemViewHolder.java:52) and CurrencyRecyclerListFragment.java:375; CloudItemViewHolder is never instantiated (grep G6: its name appears only in its own file and its constructor at :36 has no caller), and CurrencyRecyclerListFragment is created only by CurrencyRecyclerListActivity (createInstance, grep G7), which has no start site (manifest :359 has no intent-filter; MainActivity.java:644 is commented out). The subscriber at CurrencyRecyclerListFragment.java:266 does not construct the event',
  'SRC common/events/ListItemClickedEvent.java:26-30; SRC sync/CloudItemViewHolder.java:33, 36, 49-54; SRC currency/recycler/CurrencyRecyclerListFragment.java:74-80, 349-378; SRC currency/recycler/CurrencyRecyclerListActivity.java:27-44; SRC AndroidManifest.xml:359; SRC home/MainActivity.java:643-644; grep label_033.grep.txt G6, G7, G8',
  'SOURCE')

# ---- part 035 (2026-10-29)
# batch 035 (label_035): com.money.manager.ex.core DateRange, DateRange$$Parcelable (and $1), DefinedDateRange (and $1), DefinedDateRangeName, DefinedDateRanges: 35 methods, 22 REACHABLE, 13 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_035.md; grep output: graphs/MMEX/parts/label_035.grep.txt.
# No e() edges: REACHABLE rows rest on auto_calls.json CALL records and on the batch 010, 011 and 013 edges (label_013.py:30, 35). The sup cut below drops the auto records that start in the UNREACHABLE methods.

sup(('DateRange$$Parcelable.writeToParcel', 'DateRange$$Parcelable.write'))
sup(('DateRange$$Parcelable$1.createFromParcel', 'DateRange$$Parcelable.<clinit>'), ('DateRange$$Parcelable$1.createFromParcel', 'DateRange$$Parcelable.<init>'), ('DateRange$$Parcelable$1.createFromParcel', 'DateRange$$Parcelable.read'))
sup(('DefinedDateRange$1.createFromParcel', 'DefinedDateRange.<clinit>'), ('DefinedDateRange$1.createFromParcel', 'DefinedDateRange.<init>(Parcel)'))
sup(('DefinedDateRange.<init>(Parcel)', 'DefinedDateRangeName.<clinit>'))

# ================================================================== UNREACHABLE (batch 035)

UNREACHABLE['DateRange$$Parcelable.<init>'] = ('no_trigger_in_app',
  'Constructor of the DateRange wrapper. Its only CALL record is from DateRange$$Parcelable$1.createFromParcel (auto_calls.json:16078-16079), which is itself UNREACHABLE. No other method creates a wrapper.',
  'auto_calls.json:16078-16079; label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DateRange$$Parcelable.describeContents'] = ('framework_never_calls',
  'Bundle.hasFileDescriptors calls describeContents on the Parcelable values it checks, and Bundle.describeContents calls it at Bundle.java:1217. The dialog bundle holds the TransactionFilter wrapper (FilterDialogFragment.java:73), never a DateRange wrapper, so nothing calls this method. No auto record names it.',
  'FW-SRC core/java/android/os/Bundle.java:316-371, 1215-1221; SRC account/FilterDialogFragment.java:73; label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DateRange$$Parcelable.getParcel'] = ('framework_never_calls',
  'ParcelWrapper accessor. Parcels.unwrap calls it on a DateRange wrapper, and no DateRange wrapper is ever created or unwrapped: the only DateRange$$Parcelable entry points reached are the static write and read (auto_calls.json:46224-46225, 46256-46257). FilterDialogFragment.java:86-87 unwraps the TransactionFilter wrapper (line 86) and an Account wrapper (line 87), never a DateRange wrapper. No auto record names it.',
  'SRC account/FilterDialogFragment.java:86-87; auto_calls.json:46224-46225, 46256-46257; label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DateRange$$Parcelable.writeToParcel'] = ('framework_never_calls',
  'Parcel.writeParcelable calls writeToParcel only for a DateRange wrapper it is given. No DateRange wrapper is ever parcelled (no Parcels.wrap of a DateRange in label_035.grep.txt), and TransactionFilter$$Parcelable.write calls the static DateRange$$Parcelable.write instead (auto_calls.json:46224-46225). Its only auto edge, to write (auto_calls.json:16208-16209), is dropped by the sup line above.',
  'FW-SRC core/java/android/os/Parcel.java:1785-1791; auto_calls.json:16208-16209, 46224-46225; label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DateRange$$Parcelable$1.createFromParcel'] = ('framework_never_calls',
  'Parcel.readParcelable calls createFromParcel only for a DateRange wrapper that was written with writeParcelable. None is (see DateRange$$Parcelable.writeToParcel), so the creator never runs. Its outgoing auto records (auto_calls.json:16070-16088) are dropped by the sup line above.',
  'FW-SRC core/java/android/os/Parcel.java:2841-2851; auto_calls.json:16070-16088; label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DateRange$$Parcelable$1.newArray'] = ('framework_never_calls',
  'Creator method for typed arrays of DateRange wrappers. The framework calls it only when it reads a typed array of this class, and no such array is built or parcelled (label_035.grep.txt). No auto record names it.',
  'SRC core/DateRange.java:26-37 (no parcel code in the source class); label_035.grep.txt; generated class not in the source root',
  'INFERRED')

UNREACHABLE['DefinedDateRange.<init>(Parcel)'] = ('framework_never_calls',
  'Constructor used only by the CREATOR (DefinedDateRange$1.createFromParcel, auto_calls.json:17274-17275), which is UNREACHABLE: no DefinedDateRange is ever parcelled (label_035.grep.txt parcel-related block). The edge to DefinedDateRangeName.<clinit> (auto_calls.json:17442-17443) is dropped by the sup line above.',
  'SRC core/DefinedDateRange.java:49-54; auto_calls.json:17274-17275, 17442-17443; FW-SRC core/java/android/os/Parcel.java:2841-2851; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRange.describeContents'] = ('framework_never_calls',
  'Parcelable describeContents for DefinedDateRange. Only the framework calls it, and no app code puts a DefinedDateRange into a Parcel or Bundle (label_035.grep.txt parcel-related block). The only creation site is DefinedDateRanges.java:163. No auto record names it.',
  'SRC core/DefinedDateRange.java:77-78; SRC core/DefinedDateRanges.java:162-170; FW-SRC core/java/android/os/Bundle.java:316-371; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRange.writeToParcel'] = ('framework_never_calls',
  'Parcelable writeToParcel for DefinedDateRange. Only Parcel.writeParcelable calls it, and no DefinedDateRange is parcelled (see DefinedDateRange.describeContents). No auto record names it as a caller.',
  'SRC core/DefinedDateRange.java:82-87; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRange$1.createFromParcel'] = ('framework_never_calls',
  'CREATOR method for DefinedDateRange. Parcel.readParcelable calls it only for a DefinedDateRange that was written with writeParcelable, and none is. Its outgoing auto records (auto_calls.json:17266-17267, 17274-17275) are dropped by the sup line above.',
  'SRC core/DefinedDateRange.java:58-60; FW-SRC core/java/android/os/Parcel.java:2841-2851; auto_calls.json:17266-17275; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRange$1.newArray'] = ('framework_never_calls',
  'CREATOR typed-array method for DefinedDateRange. Called only when a typed array of DefinedDateRange is read, and none is built or parcelled (label_035.grep.txt).',
  'SRC core/DefinedDateRange.java:62-65; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRanges.contains'] = ('no_trigger_in_app',
  'Public method with no caller. The only app-side match for contains( in files that reference DefinedDateRanges is AccountTransactionListFragment.java:799, which is StatusFilter.contains on transactionStatus, not this method. No auto_calls.json CALL record names it.',
  'SRC core/DefinedDateRanges.java:79-81; SRC account/AccountTransactionListFragment.java:799; label_035.grep.txt',
  'SOURCE')

UNREACHABLE['DefinedDateRanges.getByNameId'] = ('no_trigger_in_app',
  'Public method with no caller: its only occurrence in the app source is the definition at DefinedDateRanges.java:50. No auto_calls.json CALL record names it.',
  'SRC core/DefinedDateRanges.java:50-55; label_035.grep.txt',
  'SOURCE')

# ---- part 034 (2026-10-29)
# batch 034 (label_034): com.money.manager.ex.core.Core (18 methods), Core$1 and Core$2 (4), Core_Factory (4), Core_MembersInjector (5): 31 methods. Rows and printed lines: graphs/MMEX/parts/label_034.md.
# Evidence: graphs/MMEX/parts/label_034.grep.txt. CALL edges come from auto_calls.json and are not written here. Dagger-generated classes have no source: their labels are INFERRED.

e('Core.alert(int,int)', 'Core$1.onClick', 'FRAMEWORK',
  'the OK button of the no-network dialog is pressed: the dialog keeps the listener and calls its onClick',
  evidence='SRC Core.java:82-100 (setPositiveButton with the listener at 93, onClick at 95-97, show at 99); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:709-710 (positive button click handler), 125-147 (mButtonHandler sends the message), 160-167 (handleMessage calls onClick at 166), 1021-1023 (setButton with the listener)')

sup(('Core_MembersInjector.create', 'Core_MembersInjector.<init>'))  # create has no caller, so its call into <init> cannot run
sup(('Core_MembersInjector.injectMembers', 'Core_MembersInjector.injectOpenHelper'),  # injectMembers has no caller
    ('Core_MembersInjector.injectMembers', 'Core_MembersInjector.injectAppSettingsLazy'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_034.grep.txt)

UNREACHABLE['Core.isToDisplayChangelog'] = ('no_trigger_in_app',
  'No live caller. The only source reference is commented out (MainActivity.java:1495, inside the comment block of handleDeviceRotation). No caller record exists in auto_calls.json. Its caller Core.showChangelog is UNREACHABLE too',
  'SRC Core.java:271-274; SRC home/MainActivity.java:1493-1497 (commented call); label_034.grep.txt sections B and D',
  'SOURCE')

UNREACHABLE['Core.showChangelog'] = ('no_trigger_in_app',
  'No live caller. The only source reference is commented out (MainActivity.java:1496). No caller record exists in auto_calls.json. It creates the changelog dialog and its listener Core$2 (Core.java:325-326)',
  'SRC Core.java:318-337; SRC home/MainActivity.java:1496 (commented call); label_034.grep.txt sections B and D',
  'SOURCE')

UNREACHABLE['Core$2.<init>'] = ('no_trigger_in_app',
  'Created only in Core.showChangelog (the listener at Core.java:325-326). showChangelog has no caller, so this cannot run',
  'SRC Core.java:318-337; label_034.grep.txt section D (showChangelog -> Core$2.<init> at 325)',
  'SOURCE')

UNREACHABLE['Core$2.onClick'] = ('no_trigger_in_app',
  'The OK listener of the changelog dialog (Core.java:328-331). Its only creator is Core.showChangelog, which has no caller. No FRAMEWORK edge is written because the creator has no route',
  'SRC Core.java:318-337',
  'SOURCE')

UNREACHABLE['Core_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (no source in the source root). Its only caller record is Core_MembersInjector.create (Core_MembersInjector.java:28), and create has no caller. The component calls the static injectOpenHelper and injectAppSettingsLazy methods instead (DaggerMmxComponent.java:518-519). No MembersInjector<Core> reference exists in the app source',
  'auto_calls.json (Core_MembersInjector.java:28; 0 caller records for create); label_034.grep.txt sections A, C and D',
  'INFERRED')

UNREACHABLE['Core_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory with no caller record in auto_calls.json and no app source reference. The component does not call it (DaggerMmxComponent.java:518-519)',
  'auto_calls.json (0 caller records); label_034.grep.txt sections A and D',
  'INFERRED')

UNREACHABLE['Core_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method reached only through a MembersInjector<Core> reference, which no app code uses (section A). No caller record for any receiver in auto_calls.json (section D). The component calls the static methods directly (DaggerMmxComponent.java:518-519). Its two outgoing records (Core_MembersInjector.java:33-34) are cut by sup',
  'auto_calls.json (0 caller records; outgoing 33-34); label_034.grep.txt sections A, C and D',
  'INFERRED')

sup(('Core_Factory.get', 'Core.<init>'), ('Core_Factory.get', 'Core_MembersInjector.injectOpenHelper'), ('Core_Factory.get', 'Core_MembersInjector.injectAppSettingsLazy'), ('Core_Factory.newCore', 'Core.<init>'))
sup(('Core.showChangelog', 'Core$2.<init>'))

UNREACHABLE['Core_Factory.get'] = ('no_trigger_in_app',
  'Dagger-generated Provider<Core>.get (dagger.internal.Factory implements Provider). Its only wrapper is DoubleCheck around the Lazy<Core> of SettingsActivity.coreLazy, which calls get only when the Lazy is read. No app source calls coreLazy.get() or any get() on a Provider<Core>. Its three outgoing records are cut by sup above',
  'SRC settings/SettingsActivity.java:37 (the only Lazy<Core> injection point; no coreLazy.get call); label_034.grep.txt sections A, C, D; Core_Factory.class and DaggerMmxComponent.class (Provider<Core> constant pool; javap not installed)',
  'INFERRED')

UNREACHABLE['Core_Factory.newCore'] = ('no_trigger_in_app',
  'Dagger-generated static method with no caller record in auto_calls.json and no app source reference. The component calls create (DaggerMmxComponent.java:192), not newCore. Its only outgoing record (Core_Factory.java:47) is cut by sup above',
  'auto_calls Core_Factory.java:47 (0 caller records); label_034.grep.txt sections A, C, D; DaggerMmxComponent.java:192',
  'INFERRED')

# ---- part 037 (2026-10-29)
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
  'SRC IntentFactory.java:37 (no constructor declared); label_037.grep.txt (IntentFactory block; auto_calls count 0)',
  'SOURCE')

UNREACHABLE['MenuHelper.add'] = ('no_trigger_in_app',
  'Public instance method (MenuHelper.java:97-105) with no caller. No auto_calls.json record names it, and no MenuHelper variable calls .add( in the 11 files that build one. The menu.add( calls in the same files are android.view.Menu.add, not this method.',
  'SRC MenuHelper.java:97-105; label_037.grep.txt (MenuHelper.add block; auto_calls count 0)',
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

# ---- part 038 (2026-10-29)
# ================================================================== batch 038 (label_038): com.money.manager.ex.core Passcode, Passcode_MembersInjector, RecurringTransactionBootReceiver, RequestCodes, SearchViewFormatter, ToolbarSpinnerAdapter: 35 methods, 24 REACHABLE, 11 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_038.md; grep output: graphs/MMEX/parts/label_038.grep.txt.
# Edges here: S_ENTRY to RecurringTransactionBootReceiver.<init> (manifest BOOT_COMPLETED receiver), LIFECYCLE from that <init> to onReceive, INTENT from MainActivity.populateScheduledTransactions to onReceive (explicit broadcast), and GUI from S_ACCOUNT_TRANSACTIONS to ToolbarSpinnerAdapter.getDropDownView (the account spinner). Every other REACHABLE row rests on auto_calls.json CALL records, which are not written again here (D7).

# The two sup cuts: the outgoing auto records of the UNREACHABLE Passcode_MembersInjector.create (to its constructor, label_003.py:106 precedent) and of Passcode_MembersInjector.injectMembers (to injectInfoRepositorySqlLazy, label_035.py precedent). Neither bytecode call can run because nothing calls create or injectMembers (label_038.grep.txt section 7).
sup(('Passcode_MembersInjector.create', 'Passcode_MembersInjector.<init>'),
    ('Passcode_MembersInjector.injectMembers', 'Passcode_MembersInjector.injectInfoRepositorySqlLazy'))

# ================================================================== batch 038: ENTRY, LIFECYCLE, INTENT and GUI edges

e('S_ENTRY', 'RecurringTransactionBootReceiver.<init>', 'ENTRY',
  'The system delivers BOOT_COMPLETED to the receiver declared in the manifest (the app holds RECEIVE_BOOT_COMPLETED), and the framework creates the receiver by class name',
  evidence='SRC AndroidManifest.xml:26, 108-112; FW-SRC core/java/android/app/ActivityThread.java:3141-3166 (handleReceiver creates the receiver with loadClass(component).newInstance())')

e('RecurringTransactionBootReceiver.<init>', 'RecurringTransactionBootReceiver.onReceive', 'LIFECYCLE',
  'The framework calls onReceive on the receiver it has just created',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3187 (receiver.onReceive); SRC RecurringTransactionBootReceiver.java:40-47')

e('MainActivity.populateScheduledTransactions', 'RecurringTransactionBootReceiver.onReceive', 'INTENT',
  'MainActivity sends an explicit broadcast to the receiver each time MainActivity.onCreate runs (onCreate calls populateScheduledTransactions at line 244)',
  evidence='SRC home/MainActivity.java:244, 1245-1246 (Intent to RecurringTransactionBootReceiver.class, sendBroadcast); FW-SRC core/java/android/app/ActivityThread.java:3187')

gui('S_ACCOUNT_TRANSACTIONS', 'ToolbarSpinnerAdapter.getDropDownView',
  'Tap the account spinner in the action bar to open its list of accounts',
  evidence='SRC account/AccountTransactionListFragment.java:475-487 (spinner custom view; loadAccountsInto at 487), 605-609; SRC servicelayer/AccountService.java:273, 282 (ToolbarSpinnerAdapter set on the spinner); FW-SRC core/java/android/widget/Spinner.java:541, 993-994 (the popup adapter delegates getDropDownView to the adapter)')

# ================================================================== UNREACHABLE (batch 038)

UNREACHABLE['Passcode_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (not in the source root; the class file is in build/intermediates, label_038.grep.txt section 4). Its only caller record is Passcode_MembersInjector.create, and create has no caller record in auto_calls.json. The app source has no reference to Passcode_MembersInjector (section 3).',
  'python-printed auto_calls record Passcode_MembersInjector.java:23 (label_038.grep.txt section 7); label_038.grep.txt sections 3, 4',
  'INFERRED')

UNREACHABLE['Passcode_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (not in the source root). No caller record exists in auto_calls.json (section 7). The component calls the static injectX method directly (DaggerMmxComponent.injectPasscode, DaggerMmxComponent.java:561), not create. No app source reference (section 3).',
  'python-printed auto_calls query, 0 callers (label_038.grep.txt section 7); label_038.grep.txt sections 3, 4',
  'INFERRED')

UNREACHABLE['Passcode_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (not in the source root) with no caller record in auto_calls.json (section 7). The component uses the static injectInfoRepositorySqlLazy at DaggerMmxComponent.java:561 instead, so nothing calls injectMembers.',
  'python-printed auto_calls query, 0 callers (label_038.grep.txt section 7); python-printed record Passcode_MembersInjector.java:28; label_038.grep.txt sections 3, 4',
  'INFERRED')

UNREACHABLE['RequestCodes.<init>'] = ('no_trigger_in_app',
  'Default constructor of a class that only holds public static final int request codes (RequestCodes.java:25-46). No source file contains new RequestCodes or a RequestCodes() call (label_038.grep.txt section 5), and no auto record names it. Other classes read the constants statically (section 5, 11 files).',
  'SRC core/RequestCodes.java:25-46; label_038.grep.txt sections 5, 7',
  'SOURCE')

UNREACHABLE['SearchViewFormatter.setEditorActionListener'] = ('no_trigger_in_app',
  'Builder setter with no caller. Its only occurrence in the app source is the definition (SearchViewFormatter.java:96-99); the two fragments that use the formatter never call it, and no auto record has it as dst.',
  'SRC core/SearchViewFormatter.java:96-99; label_038.grep.txt sections 1, 2, 7',
  'SOURCE')

UNREACHABLE['SearchViewFormatter.setInputType'] = ('no_trigger_in_app',
  'Builder setter with no caller. The only setInputType call in the source is view.setInputType(mInputType) at SearchViewFormatter.java:143, which calls the search view, not this setter. BaseListFragment and BaseExpandableListFragment never call the formatter setter.',
  'SRC core/SearchViewFormatter.java:86-89, 143; SRC common/BaseListFragment.java:135-143; SRC common/BaseExpandableListFragment.java:145-152; label_038.grep.txt sections 1, 2, 7',
  'SOURCE')

UNREACHABLE['SearchViewFormatter.setSearchBackGroundResource'] = ('no_trigger_in_app',
  'Builder setter with no caller. Its only occurrence in the app source is the definition (SearchViewFormatter.java:49-52), and no auto record has it as dst.',
  'SRC core/SearchViewFormatter.java:49-52; label_038.grep.txt sections 1, 7',
  'SOURCE')

UNREACHABLE['SearchViewFormatter.setSearchCollapsedIconResource'] = ('no_trigger_in_app',
  'Builder setter with no caller. Its only occurrence in the app source is the definition (SearchViewFormatter.java:101-104), and no auto record has it as dst.',
  'SRC core/SearchViewFormatter.java:101-104; label_038.grep.txt sections 1, 7',
  'SOURCE')

UNREACHABLE['SearchViewFormatter.setSearchHintColorResource'] = ('no_trigger_in_app',
  'Builder setter with no live caller. Its only occurrences are the definition (SearchViewFormatter.java:71-74) and two commented-out calls (BaseListFragment.java:139, BaseExpandableListFragment.java:150).',
  'SRC core/SearchViewFormatter.java:71-74; SRC common/BaseListFragment.java:139; SRC common/BaseExpandableListFragment.java:150; label_038.grep.txt sections 1, 7',
  'SOURCE')

UNREACHABLE['SearchViewFormatter.setSearchHintTextResource'] = ('no_trigger_in_app',
  'Builder setter with no caller. Its only occurrence in the app source is the definition (SearchViewFormatter.java:81-84). BaseListFragment sets the hint text with setSearchHintText (line 141), a different method.',
  'SRC core/SearchViewFormatter.java:81-84; SRC common/BaseListFragment.java:141; label_038.grep.txt sections 1, 7',
  'SOURCE')

UNREACHABLE['SearchViewFormatter.setSearchVoiceIconResource'] = ('no_trigger_in_app',
  'Builder setter with no caller. Its only occurrence in the app source is the definition (SearchViewFormatter.java:61-64), and no auto record has it as dst.',
  'SRC core/SearchViewFormatter.java:61-64; label_038.grep.txt sections 1, 7',
  'SOURCE')

# ---- part 039 (2026-10-29)
# batch 039 (label_039): com.money.manager.ex.core TransactionStatuses (6 methods: <clinit>, <init>, contains, from, get, getCode) and TransactionTypes (4 methods: <clinit>, <init>, contains, getCode). 10 methods: 7 REACHABLE, 3 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_039.md; grep output: graphs/MMEX/parts/label_039.grep.txt.
# No e() edges: REACHABLE rows rest on auto_calls.json CALL records (the build adds them). No new sup pairs: the three callers of TransactionStatuses.from (StatusFilter.add, remove, contains(String)) are already cut by the batch 013 sup at graph_def.py:1410-1412, and TransactionStatuses.contains and TransactionTypes.contains have no incoming edge at all.

# ================================================================== UNREACHABLE (batch 039)

UNREACHABLE['TransactionStatuses.contains'] = ('no_trigger_in_app',
  'Public instance method with no caller. No app code calls TransactionStatuses.contains: the only .contains( call on a status value is AccountTransactionListFragment.java:799, on mFilter.transactionStatus, which is a StatusFilter (TransactionFilter.java:34), so that call is StatusFilter.contains(int). No auto_calls.json CALL record has TransactionStatuses.contains as dst (label_039.grep.txt sections A, C, E).',
  'SRC core/TransactionStatuses.java:64-75; SRC account/AccountTransactionListFragment.java:799; SRC account/TransactionFilter.java:34; label_039.grep.txt',
  'SOURCE')

UNREACHABLE['TransactionStatuses.from'] = ('no_trigger_in_app',
  'Static lookup by name. Its only callers are StatusFilter.add (line 65), StatusFilter.remove (line 72) and StatusFilter.contains(String) (line 79). All three are UNREACHABLE in batch 013 (no caller; graph_def.py:1418, 1423, 1428), and their CALL edges into from are already cut by the sup at graph_def.py:1410-1412, so from has no live incoming edge. No other call site in the source root (label_039.grep.txt sections A, D, G).',
  'SRC core/TransactionStatuses.java:29-39; SRC account/StatusFilter.java:64-66, 71-73, 78-80; graph_def.py:1410-1412, 1418, 1423, 1428; auto_calls.json:46104-46105, 46128-46129, 46152-46153; label_039.grep.txt',
  'SOURCE')

UNREACHABLE['TransactionTypes.contains'] = ('no_trigger_in_app',
  'Public instance method with no caller. No app code calls TransactionTypes.contains: every .contains( call in the source root has a receiver whose name is not a TransactionTypes value (receiver names found by grep include mAccountIdList, categories, currencies and mFilter.transactionStatus; none is a TransactionTypes value). No auto_calls.json CALL record has TransactionTypes.contains as dst (label_039.grep.txt sections A, C, E).',
  'SRC core/TransactionTypes.java:41-52; label_039.grep.txt',
  'SOURCE')

# ---- part 042 (2026-10-29)
# ================================================================== batch 042 (label_042): com.money.manager.ex.core.file.TextFileExport, 10 methods: 10 REACHABLE, 0 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_042.md; grep output: graphs/MMEX/parts/label_042.grep.txt.
# No e() edges and no sup pairs. Every REACHABLE row rests on auto_calls.json CALL records (D7): the constructors of QifExport (QifExport.java:37) and PriceCsvExport (PriceCsvExport.java:45), and the calls of export(String,String,String) at QifExport.java:65 and PriceCsvExport.java:68. Those two subclasses are in batches 112 and 088, not merged yet, so the build shows "no path" errors for these 10 methods until they merge (D4, D8).
# No UNREACHABLE entries, so no edge from an UNREACHABLE caller needs a cut here. No new SCREENS keys: no page is entered by this class.

# ---- part 041 (2026-10-29)
# batch 041 (label_041): core/bundlers PriceDownloadedEventBundler (3 methods), core/database DatabaseManager (8), core/docstorage DocFileMetadata (1), FileStorageHelper (21) and its inner classes FileStorageHelper$1, $2, $3 (4): 37 methods, 33 REACHABLE, 4 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_041.md; grep output: graphs/MMEX/parts/label_041.grep.txt.
# CALL edges come from auto_calls.json (none written here, D7). The one edge written here is FRAMEWORK: Handler.postDelayed runs FileStorageHelper$3.run, and no auto record reaches run.
# The sup cut is for an auto CALL record whose caller is UNREACHABLE in this batch (D14a): deleteRemoteFile to getContext. The edge from EditPriceDialog$$Icepick.<clinit> (batch 085) to PriceDownloadedEventBundler.<init> is cut in batch 085 (D14a).
# get and put have no incoming edge at all. The Icepick helper that would call them is never loaded, because EditPriceDialog is never constructed (grep sections 5, 6, 9 of label_041.grep.txt), so no edge is written into them.

# ================================================================== FRAMEWORK edge (batch 041)

e('FileStorageHelper.pollNewRemoteTimestamp', 'FileStorageHelper$3.run', 'FRAMEWORK',
  'pollNewRemoteTimestamp queues the runnable on a main-looper Handler with a 2 s delay; the framework runs run() when the delay ends (run then polls again through the same handler while the remote timestamp is unchanged)',
  evidence='SRC FileStorageHelper.java:402-431 (Handler 407, Runnable 408, run 410-428, self-repeat postDelayed 419, first postDelayed(runnable, milliseconds) at 431); FW-SRC core/java/android/os/Handler.java:427-429 (postDelayed calls sendMessageDelayed), 596 (sendMessageDelayed)')

# ================================================================== sup cuts (batch 041)

sup(('FileStorageHelper.deleteRemoteFile', 'FileStorageHelper.getContext'))

# ================================================================== UNREACHABLE (batch 041)

UNREACHABLE['PriceDownloadedEventBundler.<init>'] = ('no_trigger_in_app',
  'Implicit constructor of the Icepick bundler for the @State field mPrice of EditPriceDialog (EditPriceDialog.java:83). Its only caller is the generated static initialiser EditPriceDialog$$Icepick.<clinit> (auto CALL record, EditPriceDialog$$Icepick.java:16). That initialiser runs only when Icepick loads the helper for a saved or restored EditPriceDialog (EditPriceDialog.java:105, 174). EditPriceDialog has no creation site: its constructor (EditPriceDialog.java:89) has no caller record, the only other mention of new EditPriceDialog is commented out (WatchlistItemsFragment.java:255), and no app source or resource names it (grep sections 5, 6, 9). The dialog never exists, so the helper never loads.',
  'SRC investment/EditPriceDialog.java:83, 89, 103-105, 171-174; SRC investment/watchlist/WatchlistItemsFragment.java:255; SRC core/bundlers/PriceDownloadedEventBundler.java:33; label_041.grep.txt sections 3, 5, 6, 9',
  'INFERRED')

UNREACHABLE['PriceDownloadedEventBundler.get'] = ('no_trigger_in_app',
  'Read method of the Icepick bundler for mPrice (PriceDownloadedEventBundler.java:41-44). The caller is the Icepick library helper (Helper.getWithBundler, library not in the dataset) reached from the generated restore method EditPriceDialog$$Icepick.restore. Restore runs only from Icepick.restoreInstanceState in EditPriceDialog.onCreateDialog (EditPriceDialog.java:104-105), and that dialog is never constructed (see PriceDownloadedEventBundler.<init>). No auto CALL record reaches get (grep section 9).',
  'SRC core/bundlers/PriceDownloadedEventBundler.java:41-44; SRC investment/EditPriceDialog.java:103-105; label_041.grep.txt sections 3, 4, 5, 9',
  'INFERRED')

UNREACHABLE['PriceDownloadedEventBundler.put'] = ('no_trigger_in_app',
  'Write method of the Icepick bundler for mPrice (PriceDownloadedEventBundler.java:36-38). The caller is the Icepick library helper (Helper.putWithBundler, library not in the dataset) reached from the generated save method EditPriceDialog$$Icepick.save. Save runs only from Icepick.saveInstanceState in EditPriceDialog.onSaveInstanceState (EditPriceDialog.java:171-174), and that dialog is never constructed (see PriceDownloadedEventBundler.<init>). No auto CALL record reaches put (grep section 9).',
  'SRC core/bundlers/PriceDownloadedEventBundler.java:36-38; SRC investment/EditPriceDialog.java:171-174; label_041.grep.txt sections 3, 4, 5, 9',
  'INFERRED')

UNREACHABLE['FileStorageHelper.deleteRemoteFile'] = ('no_trigger_in_app',
  'Private method with no caller. Its only occurrence in the app source is the definition at FileStorageHelper.java:325 (grep section 1). The javadoc at 320-324 says it was meant for a temp file upload, and no call site exists. No auto CALL record has it as dst (grep section 9). The inner classes FileStorageHelper$1 to $3 do not contain the name (grep section 2), so no accessor calls it. Its one outgoing call, to getContext at line 326, is cut above with sup.',
  'SRC FileStorageHelper.java:320-333; label_041.grep.txt sections 1, 2, 9',
  'SOURCE')

# ---- part 036 (2026-10-29)
# label_036.py: batch 036 (39 methods in 7 classes): ExportToCsvFile, FilterDatePeriods,
# FormatUtilities, FormatUtilities_Factory, FormatUtilities_MembersInjector, HttpMethods, InfoKeys.
# Evidence: graphs/MMEX/parts/label_036.md (table) and label_036.grep.txt (sections A-J).
#
# Edges: one CALL edge covers the Dagger Lazy hop into FormatUtilities_Factory.get (INFERRED).
# sup() cuts auto CALL edges whose caller cannot run (all 13 callers are UNREACHABLE in this batch
# or in batch 020/033, as the table rows say). Generated Dagger code is not in final_java_only, so
# the FormatUtilities_* UNREACHABLE rows are INFERRED.

e('CalculatorActivity.getFormattedAmount', 'FormatUtilities_Factory.get', 'CALL',
  'formatUtilitiesLazy.get() (Dagger Lazy<FormatUtilities> injected at CalculatorActivity.java:101) '
  'runs the factory provider FormatUtilities_Factory.get',
  cls='non_standard', via='Dagger Lazy<FormatUtilities>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='INFERRED common/CalculatorActivity.java:101, 208; label_036.grep.txt E; generated code not in final_java_only')

sup(('AllDataListFragment.exportDataToCSVFile(String)', 'ExportToCsvFile.setPrefixName'))
sup(('AllDataListFragment.exportDataToCSVFile(String)', 'ExportToCsvFile.<init>'))
sup(('ExportToCsvFile.doInBackground', 'ExportToCsvFile.runTask'))
sup(('ExportToCsvFile.onPreExecute', 'ExportToCsvFile.getPrefixName'))
sup(('FilterDatePeriods.get', 'FilterDatePeriods.getCode'))
sup(('FilterDatePeriods.<clinit>', 'FilterDatePeriods.<init>'))
sup(('WebViewActivity.handleIntent', 'HttpMethods.<clinit>'))
sup(('FormatUtilities.getValueFormattedInBaseCurrency', 'FormatUtilities.format(Money,Currency)'))
sup(('FormatUtilities.getValueFormattedInBaseCurrency', 'CurrencyService.getBaseCurrency'))
sup(('FormatUtilities.getValueFormattedInBaseCurrency', 'FormatUtilities.getCurrencyService'))
sup(('FormatUtilities_MembersInjector.create', 'FormatUtilities_MembersInjector.<init>'))
sup(('FormatUtilities_MembersInjector.injectMembers', 'FormatUtilities_MembersInjector.injectCurrencyService'))
sup(('FormatUtilities_Factory.newFormatUtilities', 'FormatUtilities.<init>(MmexApplication)'))

UNREACHABLE['ExportToCsvFile.<init>'] = (
    'branch_never_taken',
    'only creator AllDataListFragment.exportDataToCSVFile(String) is UNREACHABLE in batch 020 (branch_never_taken)',
    'common/AllDataListFragment.java:474; graphs/MMEX/parts/label_020.md',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.doInBackground'] = (
    'framework_never_calls',
    'AsyncTask worker callback; runs only after execute(), whose only caller path is UNREACHABLE',
    'core/ExportToCsvFile.java:57; common/AllDataListFragment.java:476; FW-SRC core/java/android/os/AsyncTask.java:594-595',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.getPrefixName'] = (
    'framework_never_calls',
    'only caller onPreExecute; onPreExecute runs only from executeOnExecutor after execute(), which is UNREACHABLE',
    'core/ExportToCsvFile.java:93; FW-SRC core/java/android/os/AsyncTask.java:648',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.onPostExecute'] = (
    'framework_never_calls',
    'AsyncTask callback reached through finish after doInBackground, which never runs',
    'core/ExportToCsvFile.java:66; FW-SRC core/java/android/os/AsyncTask.java:695',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.onPreExecute'] = (
    'framework_never_calls',
    'AsyncTask callback reached only via executeOnExecutor after execute(), which is UNREACHABLE; no class file references it',
    'core/ExportToCsvFile.java:79; FW-SRC core/java/android/os/AsyncTask.java:648',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.runTask'] = (
    'framework_never_calls',
    'only caller doInBackground, which never runs',
    'core/ExportToCsvFile.java:60',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.setPrefixName'] = (
    'branch_never_taken',
    'only caller exportDataToCSVFile(String) is UNREACHABLE in batch 020 (branch_never_taken)',
    'common/AllDataListFragment.java:475; graphs/MMEX/parts/label_020.md',
    'SOURCE')
UNREACHABLE['FilterDatePeriods.<clinit>'] = (
    'no_trigger_in_app',
    'enum static init; no class outside FilterDatePeriods.java uses the enum, so the first active use never happens',
    'core/FilterDatePeriods.java:25; label_036.grep.txt A, G',
    'SOURCE')
UNREACHABLE['FilterDatePeriods.<init>'] = (
    'no_trigger_in_app',
    'enum constructor, called only from <clinit>, which never runs',
    'core/FilterDatePeriods.java:39; label_036.grep.txt A',
    'SOURCE')
UNREACHABLE['FilterDatePeriods.contains'] = (
    'no_trigger_in_app',
    'no caller: no class file or auto record references it',
    'core/FilterDatePeriods.java:53; label_036.grep.txt G, H',
    'SOURCE')
UNREACHABLE['FilterDatePeriods.get'] = (
    'no_trigger_in_app',
    'no caller outside FilterDatePeriods.java',
    'core/FilterDatePeriods.java:28; label_036.grep.txt A',
    'SOURCE')
UNREACHABLE['FilterDatePeriods.getCode'] = (
    'no_trigger_in_app',
    'only caller get, which has no caller',
    'core/FilterDatePeriods.java:45; label_036.grep.txt A',
    'SOURCE')
UNREACHABLE['FormatUtilities.getValueFormattedInBaseCurrency'] = (
    'no_trigger_in_app',
    'no caller in app source; only a commented-out call in PriceEditModel.java:62',
    'core/FormatUtilities.java:305; investment/PriceEditModel.java:62; label_036.grep.txt E, G',
    'SOURCE')
UNREACHABLE['FormatUtilities_Factory.newFormatUtilities'] = (
    'no_trigger_in_app',
    'generated static helper with no caller; no class file or auto record references it',
    'auto_calls.json:16312-16313; label_036.grep.txt E, G',
    'INFERRED')
UNREACHABLE['FormatUtilities_MembersInjector.<init>'] = (
    'no_trigger_in_app',
    'generated constructor, called only from create, which has no caller',
    'auto_calls.json:16054-16055; batch036_cp_scan.txt line 61',
    'INFERRED')
UNREACHABLE['FormatUtilities_MembersInjector.create'] = (
    'no_trigger_in_app',
    'generated static factory helper with no caller; no class file references it',
    'auto_calls.json:16054-16055; label_036.grep.txt G',
    'INFERRED')
UNREACHABLE['FormatUtilities_MembersInjector.injectMembers'] = (
    'no_trigger_in_app',
    'generated entry point with no caller; Dagger calls injectCurrencyService directly',
    'auto_calls.json:16062-16063, 19136-19137; batch036_cp_scan.txt line 63',
    'INFERRED')
UNREACHABLE['HttpMethods.<clinit>'] = (
    'no_trigger_in_app',
    'enum init on first use HttpMethods.POST (WebViewActivity.java:144) in handleIntent, which is UNREACHABLE in batch 033',
    'common/WebViewActivity.java:144; auto_calls.json:37110-37111; graphs/MMEX/parts/label_033.md',
    'SOURCE')
UNREACHABLE['InfoKeys.<init>'] = (
    'no_trigger_in_app',
    'implicit constructor; no new InfoKeys in source and no class file references it',
    'core/InfoKeys.java:23; label_036.grep.txt C, G',
    'SOURCE')

# ---- part 040 (2026-10-29)
# batch 040 (label_040): core/UIHelper (19 methods), UIHelper$1 family (8), UIHelper$2 and $3 (4),
# UIHelper_MembersInjector (4), core/bundlers/MoneyBundler (3): 38 methods, 25 REACHABLE, 13 UNREACHABLE, 0 UNRESOLVED.
# Rows and printed lines: graphs/MMEX/parts/label_040.md. Grep output: graphs/MMEX/parts/label_040.grep.txt.
# CALL edges come from auto_calls.json (none written here, D7). Edges written here: 2 FRAMEWORK edges (runOnUiThread runnables)
# and 4 FRAMEWORK edges into MoneyBundler.get and put from the Icepick helpers (D1: this batch owns those destinations).
# sup cuts: 8 auto CALL records whose caller is UNREACHABLE in this batch (D14).
# The icepick library (not in dataset), the generated helpers and Dagger classes (not in source root) are INFERRED (D5, D16).

# ================================================================== FRAMEWORK edges (runOnUiThread runnables)

e('UIHelper.showToast(int,int)', 'UIHelper$2.run', 'FRAMEWORK',
  'showToast(int,int) passes the anonymous Runnable to Activity.runOnUiThread; the framework runs run() on the UI thread',
  evidence='SRC UIHelper.java:226-231 (runOnUiThread 226, run 228-230); FW-SRC core/java/android/app/Activity.java:6170-6176 (runOnUiThread hands the action to the UI thread, directly or via mHandler.post)')

e('UIHelper.showToast(String,int)', 'UIHelper$3.run', 'FRAMEWORK',
  'showToast(String,int) passes the anonymous Runnable to Activity.runOnUiThread; the framework runs run() on the UI thread',
  evidence='SRC UIHelper.java:240-245 (runOnUiThread 240, run 242-244); FW-SRC core/java/android/app/Activity.java:6170-6176')

# ================================================================== icepick edges into MoneyBundler (INFERRED: icepick library not in dataset)

e('CalculatorActivity$$Icepick.restore', 'MoneyBundler.get', 'FRAMEWORK',
  'Icepick restores the @State field mAmount through the custom bundler: the library calls get(key, bundle) from the generated restore method',
  cls='non_standard', via='icepick library Helper.getWithBundler (library not in dataset); restore is started by MmxBaseFragmentActivity.onCreate:74 (batch 027, label_027.py:127)',
  evidence='SRC MoneyBundler.java:38-41 (get); SRC common/CalculatorActivity.java:76 (@State(MoneyBundler.class) mAmount); SRC common/MmxBaseFragmentActivity.java:74 (Icepick.restoreInstanceState, no app-side guard); icepick library and CalculatorActivity$$Icepick not in the source root: INFERRED, source not read')

e('CalculatorActivity$$Icepick.save', 'MoneyBundler.put', 'FRAMEWORK',
  'Icepick saves the @State field mAmount through the custom bundler: the library calls put(key, value, bundle) from the generated save method',
  cls='non_standard', via='icepick library Helper.putWithBundler (library not in dataset); save is started by MmxBaseFragmentActivity.onSaveInstanceState:155 (batch 027, label_027.py:132)',
  evidence='SRC MoneyBundler.java:33-35 (put); SRC common/CalculatorActivity.java:76; SRC common/MmxBaseFragmentActivity.java:151-156 (Icepick.saveInstanceState at 155); icepick library not in the source root: INFERRED, source not read')

e('AmountInputDialog$$Icepick.restore', 'MoneyBundler.get', 'FRAMEWORK',
  'Icepick restores the @State field mAmount through the custom bundler: the library calls get(key, bundle) from the generated restore method',
  cls='non_standard', via='icepick library Helper.getWithBundler (library not in dataset); restore is started by AmountInputDialog.restoreSavedInstanceState (batch 023, label_023.py:77) from Icepick.restoreInstanceState at AmountInputDialog.java:417',
  guard='onCreate received a non-null savedInstanceState (AmountInputDialog.java:148-150), as in batch 023',
  evidence='SRC MoneyBundler.java:38-41 (get); SRC common/AmountInputDialog.java:122 (@State mAmount), 417 (Icepick.restoreInstanceState); icepick library not in the dataset: INFERRED, source not read')

e('AmountInputDialog$$Icepick.save', 'MoneyBundler.put', 'FRAMEWORK',
  'Icepick saves the @State field mAmount through the custom bundler: the library calls put(key, value, bundle) from the generated save method',
  cls='non_standard', via='icepick library Helper.putWithBundler (library not in dataset); save is started by AmountInputDialog.onSaveInstanceState (batch 023, label_023.py:93) from Icepick.saveInstanceState at AmountInputDialog.java:294',
  evidence='SRC MoneyBundler.java:33-35 (put); SRC common/AmountInputDialog.java:122 (@State mAmount), 294 (Icepick.saveInstanceState); icepick library not in the dataset: INFERRED, source not read')

# ================================================================== sup cuts (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('UIHelper.binaryDialog(int,int)', 'UIHelper.binaryDialog(int,int,int,int)'),
    ('UIHelper.binaryDialog(int,int,int,int)', 'UIHelper$1.<init>'),
    ('UIHelper$1.call', 'UIHelper$1$1.<init>'),
    ('UIHelper$1.call', 'UIHelper$1$2.<init>'),
    ('UIHelper$1.call', 'UIHelper$1$3.<init>'),
    ('UIHelper$1.call', 'UIHelper.getContext'),
    ('UIHelper_MembersInjector.create', 'UIHelper_MembersInjector.<init>'),
    ('UIHelper_MembersInjector.injectMembers', 'UIHelper_MembersInjector.injectAppSettingsLazy'))

# ================================================================== UNREACHABLE (batch 040)

UNREACHABLE['UIHelper.binaryDialog(int,int)'] = ('no_trigger_in_app',
  'Two-argument overload. Its only app caller is SyncPreferenceFragment.checkIfLocalFileExistsAndDownload (line 286). That method runs only from handleFileSelection (line 159), which runs only from onActivityResult (lines 97-98) when requestCode == REQUEST_REMOTE_FILE (1). The only sender of code 1 is the commented-out startActivityForResult at SyncPreferenceFragment.java:202, and grep finds no other use of REQUEST_REMOTE_FILE. The dialog is never shown. The auto CALL to the four-argument overload is cut with sup.',
  'SRC sync/SyncPreferenceFragment.java:63, 97-98, 130, 159, 202, 279, 286; SRC UIHelper.java:85-87; label_040.grep.txt sections 1-2. The framework dispatch to onActivityResult is INFERRED; the absence of any active sender is SOURCE.',
  'SOURCE')

UNREACHABLE['UIHelper.binaryDialog(int,int,int,int)'] = ('no_trigger_in_app',
  'Four-argument overload. Callers: binaryDialog(int,int) (UIHelper.java:86, same batch, sup-cut) and SyncPreferenceFragment.handleFileSelection (lines 145-146). handleFileSelection has no live caller (see binaryDialog(int,int)). This method builds the Observable whose OnSubscribe is UIHelper$1.',
  'SRC UIHelper.java:85-91; SRC sync/SyncPreferenceFragment.java:130, 145-146, 202; label_040.grep.txt sections 1-2',
  'SOURCE')

UNREACHABLE['UIHelper$1.<init>'] = ('no_trigger_in_app',
  'Anonymous OnSubscribe created only in binaryDialog(int,int,int,int) at UIHelper.java:91. That method has no live caller (see above), so the object is never created.',
  'SRC UIHelper.java:91; label_040.grep.txt section 1',
  'SOURCE')

UNREACHABLE['UIHelper$1.call'] = ('no_trigger_in_app',
  'OnSubscribe.call (UIHelper.java:93). It runs only when the rx Observable.create library call subscribes to the Observable from binaryDialog(int,int,int,int), which is never built. Its auto CALLs to getContext (94) and to UIHelper$1$1.<init> (97), UIHelper$1$2.<init> (96) and UIHelper$1$3.<init> (116) are cut with sup.',
  'SRC UIHelper.java:91-126; label_040.grep.txt section 1; rx Observable.create is a library call: INFERRED',
  'INFERRED')

UNREACHABLE['UIHelper$1$1.<init>'] = ('no_trigger_in_app',
  'Positive-button OnClickListener created in UIHelper$1.call (UIHelper.java:97). That method is unreachable (see UIHelper$1.call), so the listener is never created.',
  'SRC UIHelper.java:97; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper$1$1.onClick'] = ('no_trigger_in_app',
  'Positive-button click handler (UIHelper.java:99-102). It runs only for an AlertDialog built in UIHelper$1.call, which never runs.',
  'SRC UIHelper.java:97-103; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper$1$2.<init>'] = ('no_trigger_in_app',
  'Negative-button OnClickListener created in UIHelper$1.call (UIHelper.java:96). That method is unreachable (see UIHelper$1.call), so the listener is never created.',
  'SRC UIHelper.java:96; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper$1$2.onClick'] = ('no_trigger_in_app',
  'Negative-button click handler (UIHelper.java:106-109). It runs only for an AlertDialog built in UIHelper$1.call, which never runs.',
  'SRC UIHelper.java:104-110; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper$1$3.<init>'] = ('no_trigger_in_app',
  'Action0 cleanup object created in UIHelper$1.call (UIHelper.java:116). That method is unreachable (see UIHelper$1.call), so the object is never created.',
  'SRC UIHelper.java:116; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper$1$3.call'] = ('no_trigger_in_app',
  'Subscription cleanup action that dismisses the dialog (UIHelper.java:118-120). It runs only when the subscription from UIHelper$1.call is unsubscribed, which never happens.',
  'SRC UIHelper.java:116-121; label_040.grep.txt section 1',
  'INFERRED')

UNREACHABLE['UIHelper_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger factory method (generated, not in the source root). Its only auto record is create -> <init> (UIHelper_MembersInjector.java:22). No record has create as dst (grep section 6; auto_calls.json method index at line 82242 only). DaggerMmxComponent.injectUIHelper calls the static injectAppSettingsLazy directly (DaggerMmxComponent.java:578), not create. The create -> <init> edge is cut with sup.',
  'label_040.grep.txt sections 6 and 15; auto_calls.json (create -> <init> record); DaggerMmxComponent.java:338, 578',
  'INFERRED')

UNREACHABLE['UIHelper_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Generated constructor (not in the source root). Its only caller is UIHelper_MembersInjector.create (auto record, UIHelper_MembersInjector.java:22), and create has no caller (see above). The create -> <init> edge is cut with sup.',
  'label_040.grep.txt sections 6 and 15; auto_calls.json (create -> <init> record)',
  'INFERRED')

UNREACHABLE['UIHelper_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Instance member injector (generated). No record has it as dst (grep section 6). The component injects UIHelper through the static injectAppSettingsLazy (DaggerMmxComponent.java:578), not through injectMembers. Its auto CALL to injectAppSettingsLazy (UIHelper_MembersInjector.java:27) is cut with sup.',
  'label_040.grep.txt sections 6 and 15; auto_calls.json (injectMembers -> injectAppSettingsLazy record); DaggerMmxComponent.java:578',
  'INFERRED')

# ---- part 044 (2026-10-29)
# ================================================================== batch 044 (label_044): com.money.manager.ex.core.ioc DaggerMmxComponent: 3 inject(X) overloads, 31 injectX methods, 5 DaggerMmxComponent$Builder methods: 39 methods, 36 REACHABLE, 3 UNREACHABLE. Rows and printed lines: graphs/MMEX/parts/label_044.md; grep output: graphs/MMEX/parts/label_044.grep.txt.
# Edges: none written here. Every REACHABLE row rests on auto_calls.json CALL records (inject(X) <- class <init> or lifecycle, injectX <- inject(X) in batch 043, Builder.* <- MmexApplication.initializeDependencyInjection), which are not written again (D7). Dagger-generated classes have no source in the source root: their labels are INFERRED.

# The outgoing auto records of the UNREACHABLE injectEditPriceDialog (DaggerMmxComponent.java:488-489) are cut in batch 085
# (EditPriceDialog_MembersInjector.injectDateTimeUtilsLazy) and batch 140 (MmxDateTimeUtils_Factory), D14(a): those targets merge later.

# ================================================================== UNREACHABLE (batch 044)

UNREACHABLE['DaggerMmxComponent.injectEditPriceDialog'] = ('no_trigger_in_app',
  'Dagger-generated static member injector for EditPriceDialog (DaggerMmxComponent.java:280 inside the generated inject(EditPriceDialog) path). Its only caller record is inject(EditPriceDialog), and that is called only from EditPriceDialog.<init> (EditPriceDialog.java:91). Nothing in the app constructs EditPriceDialog: no "new EditPriceDialog", no EditPriceDialog.newInstance, no manifest or resource reference. Framework re-creation of a fragment needs an earlier instance, so none can be re-created either',
  'auto_calls EditPriceDialog.<init> -> inject(EditPriceDialog) (EditPriceDialog.java:91) and inject(EditPriceDialog) -> injectEditPriceDialog (DaggerMmxComponent.java:280); label_044.grep.txt sections 1, 2 (no construction site)',
  'INFERRED')

UNREACHABLE['DaggerMmxComponent$Builder.dbModule'] = ('no_trigger_in_app',
  'Dagger-generated builder setter for DbModule. No caller record exists for it in auto_calls.json. MmexApplication.initializeDependencyInjection calls only builder(), mmxModule(...) and build() (MmexApplication.java:202-204). Builder.build creates a default DbModule itself when none was set (DaggerMmxComponent.java:623), so the setter is never needed',
  'auto_calls.json (0 caller records for Builder.dbModule; Builder.build -> DbModule.<init> at DaggerMmxComponent.java:623); MmexApplication.java:202-204; label_044.grep.txt sections 1, 2',
  'INFERRED')

UNREACHABLE['DaggerMmxComponent$Builder.repositoryModule'] = ('no_trigger_in_app',
  'Dagger-generated builder setter for RepositoryModule. No caller record exists for it in auto_calls.json, and MmexApplication.java:202-204 does not call it. Builder.build creates a default RepositoryModule itself when none was set (DaggerMmxComponent.java:626), so the setter is never needed',
  'auto_calls.json (0 caller records for Builder.repositoryModule; Builder.build -> RepositoryModule.<init> at DaggerMmxComponent.java:626); MmexApplication.java:202-204; label_044.grep.txt sections 1, 2',
  'INFERRED')

# ---- part 045 (2026-10-29)
# label_045.py: batch 045 (39 methods in 9 classes): DbModule, DbModule$1, DbModule_ProvideDatabaseFactory,
# DbModule_ProvideOpenHelperFactory, DbModule_ProvideSqlBriteFactory, MmxModule, MmxModule_ProvideAppContextFactory,
# MmxModule_ProvideAppSettingsFactory, MmxModule_ProvideApplicationFactory, MmxModule_ProvideSharedPreferencesFactory.
# Evidence: graphs/MMEX/parts/label_045.md (table) and label_045.grep.txt (sections A-D).
#
# Labels: 32 REACHABLE (routes through auto CALL edges and merged rows, plus the e() hops below) and
# 7 UNREACHABLE (the Dagger proxyProvideX static helpers: generated, no caller in SRC or any class file).
# The auto CALL edges already present (factory get -> provideX, proxy -> provideX, create -> <init>, initialize -> create,
# injectX chains) are not repeated here. None of the e() pairs below exists in auto_calls.json (checked before writing).
# Every Dagger/Lazy/Provider hop is cls='non_standard' with via=...

# --- Dagger Provider<T>.get() hops between generated factories and their providers (generated code not in SRC: INFERRED)

e('DbModule_ProvideDatabaseFactory.get', 'DbModule_ProvideSqlBriteFactory.get', 'CALL',
  'DbModule_ProvideDatabaseFactory.get passes the result of its Provider<SqlBrite> argument into DbModule.provideDatabase',
  cls='non_standard',
  via='Dagger Provider<SqlBrite>.get: generated factory calls its argument provider (generated code, INFERRED; not read)',
  evidence='INFERRED DbModule.java:61 provideDatabase(SqlBrite sqlBrite, MmxOpenHelper helper) takes a SqlBrite argument; generated factory not in SRC')

e('DbModule_ProvideDatabaseFactory.get', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'DbModule_ProvideDatabaseFactory.get passes the result of its Provider<MmxOpenHelper> argument into DbModule.provideDatabase',
  cls='non_standard',
  via='Dagger Provider<MmxOpenHelper>.get: generated factory calls its argument provider (generated code, INFERRED; not read)',
  evidence='INFERRED DbModule.java:61 provideDatabase(SqlBrite sqlBrite, MmxOpenHelper helper) takes an MmxOpenHelper argument; generated factory not in SRC')

e('DbModule_ProvideOpenHelperFactory.get', 'MmxModule_ProvideApplicationFactory.get', 'CALL',
  'DbModule_ProvideOpenHelperFactory.get passes the result of its Provider<MmexApplication> argument into DbModule.provideOpenHelper',
  cls='non_standard',
  via='Dagger Provider<MmexApplication>.get: generated factory calls its argument provider (generated code, INFERRED; not read)',
  evidence='INFERRED DbModule.java:46 provideOpenHelper(MmexApplication app) takes an MmexApplication argument; generated factory not in SRC')

e('MmxModule_ProvideAppSettingsFactory.get', 'MmxModule_ProvideApplicationFactory.get', 'CALL',
  'MmxModule_ProvideAppSettingsFactory.get passes the result of its Provider<MmexApplication> argument into MmxModule.provideAppSettings',
  cls='non_standard',
  via='Dagger Provider<MmexApplication>.get: generated factory calls its argument provider (generated code, INFERRED; not read)',
  evidence='INFERRED MmxModule.java:67 provideAppSettings(MmexApplication application) takes an MmexApplication argument; generated factory not in SRC')

# --- Dagger Lazy<T>.get() consumer sites (SRC call site; DoubleCheck calls the factory provider: library/generated, INFERRED)

e('MmxContentProvider.insert', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxContentProvider.insert calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC MmxContentProvider.java:88 (field Lazy<MmxOpenHelper> openHelper), :168 (openHelper.get().getWritableDatabase()) inside insert (151)')

e('MmxContentProvider.update', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxContentProvider.update calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC MmxContentProvider.java:88 (field Lazy<MmxOpenHelper> openHelper), :198 (openHelper.get().getWritableDatabase()) inside update (191)')

e('MmxContentProvider.delete', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxContentProvider.delete calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC MmxContentProvider.java:88 (field Lazy<MmxOpenHelper> openHelper), :247 (openHelper.get().getWritableDatabase()) inside delete (228)')

e('MmxContentProvider.query_internal', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxContentProvider.query_internal calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC MmxContentProvider.java:88 (field Lazy<MmxOpenHelper> openHelper), :384 (openHelper.get().getReadableDatabase()) inside query_internal (372)')

e('DatabaseSettingsFragment.onCreate', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'DatabaseSettingsFragment.onCreate calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC settings/DatabaseSettingsFragment.java:58 (field Lazy<MmxOpenHelper> openHelper), :85 (openHelper.get().getSQLiteVersion()) inside onCreate (62)')

e('DatabaseSettingsFragment.refreshDbVersion', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'DatabaseSettingsFragment.refreshDbVersion calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC settings/DatabaseSettingsFragment.java:58 (field Lazy<MmxOpenHelper> openHelper), :136 (openHelper.get().getReadableDatabase()) inside refreshDbVersion (131)')

e('Core.getLastPayeeUsed', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'Core.getLastPayeeUsed calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC Core.java:71 (field Lazy<MmxOpenHelper> openHelper), :147 (openHelper.get().getReadableDatabase().query(sql)) inside getLastPayeeUsed (135)')

e('MmxDatabaseUtils.checkIntegrity', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxDatabaseUtils.checkIntegrity calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC utils/MmxDatabaseUtils.java:101 (field Lazy<MmxOpenHelper> openHelper), :114 (openHelper.get().getReadableDatabase()) inside checkIntegrity (113)')

e('MmxDatabaseUtils.getTableNamesFromDb', 'DbModule_ProvideOpenHelperFactory.get', 'CALL',
  'MmxDatabaseUtils.getTableNamesFromDb calls openHelper.get() (Lazy<MmxOpenHelper>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<MmxOpenHelper>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC utils/MmxDatabaseUtils.java:101 (field Lazy<MmxOpenHelper> openHelper), :339 (openHelper.get().getReadableDatabase()) inside getTableNamesFromDb (338)')

e('BudgetAdapter.loadTotalFor', 'DbModule_ProvideDatabaseFactory.get', 'CALL',
  'BudgetAdapter.loadTotalFor calls databaseLazy.get() (Lazy<BriteDatabase>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<BriteDatabase>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC budget/BudgetAdapter.java:85 (field Lazy<BriteDatabase> databaseLazy), :278 (databaseLazy.get().query(query)) inside loadTotalFor (265)')

e('UIHelper.getThemeId', 'MmxModule_ProvideAppSettingsFactory.get', 'CALL',
  'UIHelper.getThemeId calls appSettingsLazy.get() (Lazy<AppSettings>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<AppSettings>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC UIHelper.java:78 (field Lazy<AppSettings> appSettingsLazy), :178 (appSettingsLazy.get().getGeneralSettings().getTheme()) inside getThemeId (175)')

e('AppSettings.getPreferences', 'MmxModule_ProvideSharedPreferencesFactory.get', 'CALL',
  'AppSettings.getPreferences calls sharedPreferences.get() (Lazy<SharedPreferences>), which runs the factory provider',
  cls='non_standard',
  via='Dagger Lazy<SharedPreferences>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='SRC settings/AppSettings.java:44 (field Lazy<SharedPreferences> sharedPreferences), :57 (return sharedPreferences.get()) inside getPreferences (56)')

# --- Dagger component paths to providers whose Context/MmexApplication argument is supplied by a provider (INFERRED)

e('DaggerMmxComponent.getCurrencyService', 'MmxModule_ProvideAppContextFactory.get', 'CALL',
  'DaggerMmxComponent.getCurrencyService passes the Context from the provideAppContext provider into CurrencyService_Factory.newCurrencyService',
  cls='non_standard',
  via='Dagger Provider<Context>.get: generated component calls the DoubleCheck-wrapped provider (generated code, INFERRED; not read)',
  evidence='INFERRED DaggerMmxComponent.java:159 calls CurrencyService_Factory.newCurrencyService, whose descriptor takes android.content.Context (CurrencyService_Factory.class, label_045.grep.txt B); DaggerMmxComponent.class references MmxModule_ProvideAppContextFactory (grep B)')

e('BudgetAdapter.loadTotalFor', 'DbModule$1.log', 'CALL',
  'BudgetAdapter.loadTotalFor runs a BriteDatabase.query; with logging enabled the SqlBrite Logger (DbModule$1.log) receives the message',
  cls='non_standard',
  via='SqlBrite BriteDatabase.query calls the Logger.log callback when setLoggingEnabled(true) (library behaviour, INFERRED; library source not read)',
  evidence='SRC budget/BudgetAdapter.java:278 (databaseLazy.get().query(query)); SRC DbModule.java:55-57 (Logger.log body), :69 (db.setLoggingEnabled(true))')

# --- sup(): cut the 7 auto proxy -> provide CALL edges (callers are UNREACHABLE; generated, no caller)

sup(('DbModule_ProvideDatabaseFactory.proxyProvideDatabase', 'DbModule.provideDatabase'))
sup(('DbModule_ProvideOpenHelperFactory.proxyProvideOpenHelper', 'DbModule.provideOpenHelper'))
sup(('DbModule_ProvideSqlBriteFactory.proxyProvideSqlBrite', 'DbModule.provideSqlBrite'))
sup(('MmxModule_ProvideAppContextFactory.proxyProvideAppContext', 'MmxModule.provideAppContext'))
sup(('MmxModule_ProvideAppSettingsFactory.proxyProvideAppSettings', 'MmxModule.provideAppSettings'))
sup(('MmxModule_ProvideApplicationFactory.proxyProvideApplication', 'MmxModule.provideApplication'))
sup(('MmxModule_ProvideSharedPreferencesFactory.proxyProvideSharedPreferences', 'MmxModule.provideSharedPreferences'))

# --- UNREACHABLE: generated Dagger proxy helpers with no caller (grep A: 0 SRC hits; grep B: name only in its own factory class)

UNREACHABLE['DbModule_ProvideDatabaseFactory.proxyProvideDatabase'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in DbModule_ProvideDatabaseFactory.class (grep B)',
    'DbModule_ProvideDatabaseFactory.java:47; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['DbModule_ProvideOpenHelperFactory.proxyProvideOpenHelper'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in DbModule_ProvideOpenHelperFactory.class (grep B)',
    'DbModule_ProvideOpenHelperFactory.java:37; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['DbModule_ProvideSqlBriteFactory.proxyProvideSqlBrite'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in DbModule_ProvideSqlBriteFactory.class (grep B)',
    'DbModule_ProvideSqlBriteFactory.java:30; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['MmxModule_ProvideAppContextFactory.proxyProvideAppContext'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in MmxModule_ProvideAppContextFactory.class (grep B)',
    'MmxModule_ProvideAppContextFactory.java:30; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['MmxModule_ProvideAppSettingsFactory.proxyProvideAppSettings'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in MmxModule_ProvideAppSettingsFactory.class (grep B)',
    'MmxModule_ProvideAppSettingsFactory.java:39; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['MmxModule_ProvideApplicationFactory.proxyProvideApplication'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in MmxModule_ProvideApplicationFactory.class (grep B)',
    'MmxModule_ProvideApplicationFactory.java:30; label_045.grep.txt A, B',
    'INFERRED')
UNREACHABLE['MmxModule_ProvideSharedPreferencesFactory.proxyProvideSharedPreferences'] = (
    'no_trigger_in_app',
    'generated Dagger static proxy with no caller: 0 hits in app source (grep A) and the name appears only in MmxModule_ProvideSharedPreferencesFactory.class (grep B)',
    'MmxModule_ProvideSharedPreferencesFactory.java:31; label_045.grep.txt A, B',
    'INFERRED')

# ---- part 043 (2026-10-29)
# batch 043 (label_043): com.money.manager.ex.core.ioc.DaggerMmxComponent, methods 1-40 of 79 (40 methods). Rows and printed lines: graphs/MMEX/parts/label_043.md.
# Evidence: graphs/MMEX/parts/label_043.grep.txt. CALL edges come from auto_calls.json and are not written here.
# DaggerMmxComponent is Dagger-generated and has no source file in the source root: its labels are INFERRED.
# "SRC <path>" in the citations means final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/<path>.

# inject(EditPriceDialog) has no caller, so its call into injectEditPriceDialog cannot run.
sup(('DaggerMmxComponent.inject(EditPriceDialog)', 'DaggerMmxComponent.injectEditPriceDialog'))

# ---- UNREACHABLE (grep output: graphs/MMEX/parts/label_043.grep.txt)

UNREACHABLE['DaggerMmxComponent.inject(StockRepositorySql)'] = ('no_trigger_in_app',
  'No live caller. The only reference to this injection in app source is commented out (datalayer/StockRepositorySql.java:43). auto_calls.json has no caller record for it, and every live iocComponent.inject call in app source passes this (grep section A)',
  'SRC datalayer/StockRepositorySql.java:43 (commented call); auto_calls.json (no caller record); label_043.grep.txt section A',
  'SOURCE')

UNREACHABLE['DaggerMmxComponent.inject(StockHistoryRepositorySql)'] = ('no_trigger_in_app',
  'No live caller. The only reference to this injection in app source is commented out (datalayer/StockHistoryRepositorySql.java:49). auto_calls.json has no caller record for it, and every live iocComponent.inject call in app source passes this (grep section A)',
  'SRC datalayer/StockHistoryRepositorySql.java:49 (commented call); auto_calls.json (no caller record); label_043.grep.txt section A',
  'SOURCE')

UNREACHABLE['DaggerMmxComponent.inject(EditPriceDialog)'] = ('no_trigger_in_app',
  'No live caller. No app code instantiates EditPriceDialog. The only reference to its constructor outside the class, WatchlistItemsFragment.java:255, is commented out, and PriceEditActivity.java:198-204 and WatchlistItemsFragment.java:246-252 only read or write ARG_ constants. auto_calls.json has zero records that call EditPriceDialog.<init>; its only EditPriceDialog.<init> record is the outgoing call to DaggerMmxComponent.inject(EditPriceDialog) at EditPriceDialog.java:91',
  'SRC investment/EditPriceDialog.java:69,89-91; investment/watchlist/WatchlistItemsFragment.java:246-252,255 (255 commented); investment/PriceEditActivity.java:198-204; label_043.grep.txt sections C and F',
  'SOURCE')

UNREACHABLE['DaggerMmxComponent.inject(ISecurityPriceUpdater)'] = ('no_trigger_in_app',
  'No live caller. SRC MmxComponent.java:96 declares inject(ISecurityPriceUpdater), but no call site uses it: every live iocComponent.inject call in app source passes this, and the one class that implements ISecurityPriceUpdater and injects itself (MorningstarPriceUpdater.java:66) resolves to inject(MorningstarPriceUpdater). auto_calls.json has no caller record',
  'SRC MmxComponent.java:96; investment/morningstar/MorningstarPriceUpdater.java:66; label_043.grep.txt section A',
  'SOURCE')

# ---- part 046 (2026-10-29)
# label_046.py: batch 046 (40 methods in 7 classes): RepositoryModule (3), RepositoryModule_ProvideStockHistoryRepositoryFactory (4),
# RepositoryModule_ProvideStockRepositoryFactory (4), CurrencyChartActivity (5), CurrencyEditActivity (9), CurrencyEditViewHolder (2),
# CurrencyRepository (13). Result: 35 REACHABLE, 5 UNREACHABLE, 0 UNRESOLVED.
# Rows and printed lines: graphs/MMEX/parts/label_046.md. Grep evidence: graphs/MMEX/parts/label_046.grep.txt.
# Auto CALL records (auto_calls.json) are not rewritten here. This file writes:
#   - 8 edges that auto data cannot give (INTENT starts, LIFECYCLE, FRAMEWORK menu, ENTERS screen),
#   - 2 non-standard CALL edges into the Dagger factory get() methods (Lazy hop, INFERRED),
#   - 4 sup pairs: auto CALL records whose caller is UNREACHABLE in this batch and whose callee is also in batch 046 (D14).
# Edges into a method of this batch are written here (destination owner, D1).
# The Dagger generated classes and the DoubleCheck/Lazy hop are INFERRED (generated code not read in the source root).

# ================================================================== CurrencyChartActivity (screen entry, lifecycle, menu)

e('CurrencyListFragment.onContextItemSelected', 'CurrencyChartActivity.<init>', 'INTENT',
  'context-menu item 1 (chart) of the currency list builds an Intent for CurrencyChartActivity (ACTION_VIEW, symbol and base-currency extras) and starts it',
  evidence='SRC currency/list/CurrencyListFragment.java:155 (registerForContextMenu), 257-262 (case 1: Intent, extras, startActivity); SRC AndroidManifest.xml:320-323 (CurrencyChartActivity, no intent filter); FW-SRC core/java/android/app/Instrumentation.java:1170-1176 (newActivity: loadClass().newInstance()); FW-SRC core/java/android/app/ActivityThread.java:2669 (newActivity call). Source batch 049 is not merged; this edge is written here because the destination is in batch 046.')

e('CurrencyChartActivity.<init>', 'CurrencyChartActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1214; FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('CurrencyChartActivity.onCreate', 'CurrencyChartActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu for the window: PhoneWindow calls onCreatePanelMenu, which calls onCreateOptionsMenu (inflates menu_currency_chart)',
  evidence='FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:615-640 (cb.onCreatePanelMenu at 631); FW-SRC core/java/android/app/Activity.java:3386-3393 (onCreateOptionsMenu at 3388); SRC res/menu/menu_currency_chart.xml (item action_settings, showAsAction never)')

e('CurrencyChartActivity.onCreateOptionsMenu', 'CurrencyChartActivity.onOptionsItemSelected', 'FRAMEWORK',
  'the user selects an item of the chart options menu (action_settings, in the overflow): the framework calls onOptionsItemSelected. No S_ screen key exists for the chart screen (no new constants), so the edge starts at the menu builder; this is a decision for the coordinator (see label_046.md)',
  evidence='FW-SRC core/java/android/app/Activity.java:3439-3455 (onMenuItemSelected calls onOptionsItemSelected at 3450); SRC currency/CurrencyChartActivity.java:61-74; SRC res/menu/menu_currency_chart.xml:17-18')

# ================================================================== CurrencyEditActivity (entry, lifecycle, screen)

e('CurrencyUIFeatures.startCurrencyEditActivity', 'CurrencyEditActivity.<init>', 'INTENT',
  'startCurrencyEditActivity builds an Intent for CurrencyEditActivity (ACTION_EDIT with KEY_CURRENCY_ID, or ACTION_INSERT when the id is null) and starts it',
  evidence='SRC currency/CurrencyUIFeatures.java:213-225 (Intent 215, ACTION_EDIT 219, ACTION_INSERT 221, startActivity 224); callers: SRC currency/list/CurrencyListFragment.java:245 (case 0, edit), 326 (FAB, insert); SRC currency/recycler/CurrencyRecyclerListFragment.java:173 (batch 050); SRC AndroidManifest.xml:219-226 (exported, EDIT/INSERT filters)')

e('CurrencyEditActivity.<init>', 'CurrencyEditActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1216; FW-SRC core/java/android/app/Activity.java:6993-7000 (performCreate calls onCreate)')

e('CurrencyEditActivity.onCreate', 'S_CURRENCY_EDIT', 'ENTERS',
  'the currency edit form is shown',
  evidence='SRC currency/CurrencyEditActivity.java:82 (setContentView R.layout.currency_edit_activity), 83 (showStandardToolbarActions)')

e('CurrencyEditActivity.onCreate', 'CurrencyEditActivity.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the state of the activity when it is paused (and on configuration change); the saved bundle is passed back to onCreate',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3855-3876 (performPauseActivity calls callCallActivityOnSaveInstanceState at 3875); FW-SRC core/java/android/app/ActivityThread.java:4713-4722; FW-SRC core/java/android/app/Instrumentation.java:1385-1386; FW-SRC core/java/android/app/Activity.java:1495-1496 (performSaveInstanceState calls onSaveInstanceState)')

# ================================================================== Dagger factory get() (Lazy hop; INFERRED)

e('MorningstarPriceUpdater.savePrice', 'RepositoryModule_ProvideStockRepositoryFactory.get', 'CALL',
  'savePrice calls stockRepository.get(), a Dagger Lazy<StockRepositorySql>; the Lazy runs the factory provider get(), which calls RepositoryModule.provideStockRepository',
  cls='non_standard', via='Dagger Lazy<StockRepositorySql>.get: DoubleCheck calls the generated factory provider get (library and generated code INFERRED; not read)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:75 (@Inject Lazy<StockRepositorySql>), 278, 281 (stockRepository.get()); 190 (savePrice called from MorningstarPriceUpdater$2.call); SRC RepositoryModule.java:32-35; auto record RepositoryModule_ProvideStockRepositoryFactory.get -> RepositoryModule.provideStockRepository (factory line 29)')

e('MorningstarPriceUpdater.savePrice', 'RepositoryModule_ProvideStockHistoryRepositoryFactory.get', 'CALL',
  'savePrice calls stockHistoryRepository.get(), a Dagger Lazy<StockHistoryRepositorySql>; the Lazy runs the factory provider get(), which calls RepositoryModule.provideStockHistoryRepository',
  cls='non_standard', via='Dagger Lazy<StockHistoryRepositorySql>.get: DoubleCheck calls the generated factory provider get (library and generated code INFERRED; not read)',
  evidence='SRC investment/morningstar/MorningstarPriceUpdater.java:76 (@Inject Lazy<StockHistoryRepositorySql>), 284 (stockHistoryRepository.get()); 190; SRC RepositoryModule.java:37-40; auto record RepositoryModule_ProvideStockHistoryRepositoryFactory.get -> RepositoryModule.provideStockHistoryRepository (factory line 29)')

# ================================================================== sup cuts (D14): auto CALL records whose caller is UNREACHABLE and whose callee is in batch 046

sup(('CurrencyRepository.load', 'CurrencyRepository.first'),
    ('CurrencyRepository.first', 'CurrencyRepository.query'),
    ('RepositoryModule_ProvideStockRepositoryFactory.proxyProvideStockRepository', 'RepositoryModule.provideStockRepository'),
    ('RepositoryModule_ProvideStockHistoryRepositoryFactory.proxyProvideStockHistoryRepository', 'RepositoryModule.provideStockHistoryRepository'))
# Not written here (callee in a later batch, that batch writes them): CurrencyRepository.load -> WhereStatementGenerator.<init>,
# addStatement(String,String,Integer), getWhere (batch 053); CurrencyRepository.query -> Currency.fromCursor (batch 065) and
# RepositoryBase.openCursor(String[],String,String[]) (batch 056).

# ================================================================== UNREACHABLE (batch 046)

UNREACHABLE['CurrencyRepository.load'] = ('no_trigger_in_app',
  'Public helper with no caller. No auto record has it as dst, and no source file calls CurrencyRepository.load (grep label_046.grep.txt section B). Its auto CALL to first (CurrencyRepository.java:58) is cut with sup; its auto CALLs to WhereStatementGenerator (55-58) are cut by batch 053.',
  'SRC currency/CurrencyRepository.java:54-59; label_046.grep.txt sections B and H',
  'SOURCE')

UNREACHABLE['CurrencyRepository.first'] = ('no_trigger_in_app',
  'Its only caller is load (auto CALL at CurrencyRepository.java:58), which has no caller, so first is never reached. The auto CALL to query (136) is cut with sup.',
  'SRC currency/CurrencyRepository.java:135-137, 58; auto_calls record load -> first (58); label_046.grep.txt section B',
  'SOURCE')

UNREACHABLE['CurrencyRepository.query'] = ('no_trigger_in_app',
  'Its only caller is first (auto CALL at CurrencyRepository.java:136), which is UNREACHABLE. Its auto CALLs to Currency.fromCursor (147, batch 065) and RepositoryBase.openCursor (140, batch 056) are cut by those batches.',
  'SRC currency/CurrencyRepository.java:139-153, 136; auto_calls records (grep section B); label_046.grep.txt section B',
  'SOURCE')

UNREACHABLE['RepositoryModule_ProvideStockRepositoryFactory.proxyProvideStockRepository'] = ('no_trigger_in_app',
  'Dagger proxy static method on the generated factory. No auto record has it as dst. DaggerMmxComponent.initialize calls the factory create (DaggerMmxComponent.java:196), not this proxy. Its auto CALL to RepositoryModule.provideStockRepository (factory line 40) is cut with sup.',
  'auto_calls record proxyProvideStockRepository -> RepositoryModule.provideStockRepository (RepositoryModule_ProvideStockRepositoryFactory.java:40); DaggerMmxComponent.java:196; out/build_report.txt:602; label_046.grep.txt section C',
  'INFERRED')

UNREACHABLE['RepositoryModule_ProvideStockHistoryRepositoryFactory.proxyProvideStockHistoryRepository'] = ('no_trigger_in_app',
  'Dagger proxy static method on the generated factory. No auto record has it as dst. DaggerMmxComponent.initialize calls the factory create (DaggerMmxComponent.java:199), not this proxy. Its auto CALL to RepositoryModule.provideStockHistoryRepository (factory line 40) is cut with sup.',
  'auto_calls record proxyProvideStockHistoryRepository -> RepositoryModule.provideStockHistoryRepository (RepositoryModule_ProvideStockHistoryRepositoryFactory.java:40); DaggerMmxComponent.java:199; out/build_report.txt:600; label_046.grep.txt section C',
  'INFERRED')

# The Done and Cancel listeners of MmxBaseFragmentActivity are shared by every toolbar screen, and their auto CALL edges
# fan out by class hierarchy. A CurrencyEditActivity receiver runs only its own override, so the other overrides are cut here.
# Each cut target keeps its own route through its onOptionsItemSelected edge.
sup(('MmxBaseFragmentActivity$2.onClick', 'CheckingTransactionEditActivity.onActionDoneClick'),
    ('MmxBaseFragmentActivity$2.onClick', 'RecurringTransactionEditActivity.onActionDoneClick'),
    ('MmxBaseFragmentActivity$2.onClick', 'AccountEditActivity.onActionDoneClick'),
    ('MmxBaseFragmentActivity$2.onClick', 'SplitCategoriesActivity.onActionDoneClick'),
    ('MmxBaseFragmentActivity$2.onClick', 'InvestmentTransactionEditActivity.onActionDoneClick'),
    ('MmxBaseFragmentActivity$1.onClick', 'CheckingTransactionEditActivity.onActionCancelClick'),
    ('MmxBaseFragmentActivity$1.onClick', 'RecurringTransactionEditActivity.onActionCancelClick'),
    ('MmxBaseFragmentActivity$1.onClick', 'AccountEditActivity.onActionCancelClick'),
    ('MmxBaseFragmentActivity$1.onClick', 'InvestmentTransactionEditActivity.onActionCancelClick'))

# ---- part 026 (2026-10-29)
# batch 026 (label_026): com.money.manager.ex.common.BaseListFragment (abstract; 27 methods, including its anonymous listeners $1 and $2), BaseRecyclerListFragment.<init>, and com.money.manager.ex.common.Calculator (8 methods). Rows and printed lines: graphs/MMEX/parts/label_026.md.
# BaseListFragment has 10 direct subclasses (grep, label_026.grep.txt section G): PortfolioFragment, WatchlistItemsFragment, AllDataListFragment, PayeeListFragment, AccountListFragment, CurrencyListFragment, BudgetListFragment, RecurringTransactionListFragment, BudgetDetailFragment, and BaseReportFragment (whose subclasses are PayeeReportFragment and CategoriesReportFragment).
# Pages (existing SCREENS keys only, D9): S_PAYEE (graph_def.py:104), S_ACCOUNT_LIST (graph_def.py:906), S_BUDGETS (graph_def.py:1577). The currency, recurring, portfolio, watchlist, all-data and report lists have no key, so no GUI edge is written for them.
# CALL edges come from auto_calls.json (super calls, calls inside BaseListFragment, and receiver-variant records such as BaseListFragment.onActivityCreated@PayeeListFragment), so none are written here. The edges that cannot run are cut with sup below.
# androidx Fragment, SearchView, the options-menu dispatch and the com.melnykov FloatingActionButton are not in fw_src: those claims are INFERRED (library source not read). grep evidence: graphs/MMEX/parts/label_026.grep.txt.

# ---- fragment lifecycle (androidx Fragment; library source not read: INFERRED)

e('AbsListFragment.onCreateView', 'BaseListFragment.onViewCreated', 'LIFECYCLE',
  'the framework calls onViewCreated after the view is created by the inherited onCreateView (AbsListFragment inflates abs_list_fragment.xml). Receivers that do not override onViewCreated run this body; BudgetListFragment overrides it and calls super (119-120); CurrencyListFragment (154-156) and BudgetDetailFragment (121-123) override it without calling super, so this body does not run for them',
  evidence='SRC AbsListFragment.java:77-79; SRC common/BaseListFragment.java:62-67; SRC currency/list/CurrencyListFragment.java:154-156; SRC budget/BudgetDetailFragment.java:121-123; INFERRED androidx Fragment lifecycle (library not read)')

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

# ---- part 048 (2026-10-29)
# label_048.py: batch 048 (39 methods in 4 class groups): CurrencyUIFeatures (11), CurrencyUIFeatures$1 to $11 (24),
# ExchangeRateUpdaterFactory (2), CurrencyDeletionConfirmedEvent.<init> (1), ExchangeRateUpdateConfirmedEvent.<init> (1).
# Result: 33 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE. Rows and printed lines: graphs/MMEX/parts/label_048.md.
# Grep evidence: graphs/MMEX/parts/label_048.grep.txt (sections A to F).
# Auto CALL records (auto_calls.json) are not rewritten here. This file writes:
#   - 7 FRAMEWORK edges from the dialog-building methods to their OK and Cancel listeners (AlertDialog, AlertController),
#   - 4 non_standard CALL edges from importCurrencies to the RxJava Callable and Subscriber methods (library, INFERRED),
#   - 13 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE and whose callee is in batch 048.
#     4 pairs start in showActiveInactiveSelectorForUpdate or its listener $9.onClick (same batch).
#     9 pairs start in CurrencyRecyclerListFragment methods of batch 050 (the fragment has no start site).
# EventBus POST edges from $3.onClick and $7.onClick go to the @Subscribe methods of batches 049 and 050, which write them (D1).

# ================================================================== dialog listeners (FRAMEWORK)

e('CurrencyUIFeatures.notifyCurrencyCanNotBeDeleted', 'CurrencyUIFeatures$1.onClick', 'FRAMEWORK',
  'the cannot-delete-currency dialog is shown; the user taps OK and the framework calls the positive listener, which dismisses the dialog',
  evidence='SRC currency/CurrencyUIFeatures.java:76-80 (setPositiveButton at 76, onClick dismisses at 79); FW-SRC core/java/android/app/AlertDialog.java:611-613 (setPositiveButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167 (handleMessage calls onClick at 166)')

e('CurrencyUIFeatures.showDialogDeleteCurrency', 'CurrencyUIFeatures$3.onClick', 'FRAMEWORK',
  'the delete-currency dialog is shown; the user taps OK and the framework calls the positive listener, which posts CurrencyDeletionConfirmedEvent',
  evidence='SRC currency/CurrencyUIFeatures.java:120-125 (setPositiveButton at 120, post at 123); FW-SRC core/java/android/app/AlertDialog.java:611-613; FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

e('CurrencyUIFeatures.showDialogDeleteCurrency', 'CurrencyUIFeatures$2.onClick', 'FRAMEWORK',
  'the delete-currency dialog is shown; the user taps Cancel and the framework calls the negative listener, which calls dialog.cancel()',
  evidence='SRC currency/CurrencyUIFeatures.java:126-131 (setNegativeButton at 126, cancel at 129); FW-SRC core/java/android/app/AlertDialog.java:637-639 (setNegativeButton stores the listener); FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

e('CurrencyUIFeatures.showDialogImportAllCurrencies', 'CurrencyUIFeatures$5.onClick', 'FRAMEWORK',
  'the import-all-currencies dialog is shown; the user taps OK and the framework calls the positive listener, which calls importCurrencies',
  evidence='SRC currency/CurrencyUIFeatures.java:143-148 (setPositiveButton at 143, importCurrencies at 146); FW-SRC core/java/android/app/AlertDialog.java:611-613; FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

e('CurrencyUIFeatures.showDialogImportAllCurrencies', 'CurrencyUIFeatures$4.onClick', 'FRAMEWORK',
  'the import-all-currencies dialog is shown; the user taps Cancel and the framework calls the negative listener, which calls dialog.cancel()',
  evidence='SRC currency/CurrencyUIFeatures.java:149-154 (setNegativeButton at 149, cancel at 152); FW-SRC core/java/android/app/AlertDialog.java:637-639; FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

e('CurrencyUIFeatures.showDialogUpdateExchangeRates', 'CurrencyUIFeatures$7.onClick', 'FRAMEWORK',
  'the update-exchange-rates dialog is shown; the user taps OK and the framework calls the positive listener, which posts ExchangeRateUpdateConfirmedEvent(true)',
  evidence='SRC currency/CurrencyUIFeatures.java:166-171 (setPositiveButton at 166, post at 169); FW-SRC core/java/android/app/AlertDialog.java:611-613; FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

e('CurrencyUIFeatures.showDialogUpdateExchangeRates', 'CurrencyUIFeatures$6.onClick', 'FRAMEWORK',
  'the update-exchange-rates dialog is shown; the user taps Cancel and the framework calls the negative listener, which calls dialog.cancel()',
  evidence='SRC currency/CurrencyUIFeatures.java:172-177 (setNegativeButton at 172, cancel at 175); FW-SRC core/java/android/app/AlertDialog.java:637-639; FW-SRC core/java/com/android/internal/app/AlertController.java:160-167')

# ================================================================== importCurrencies (RxJava, library not read: INFERRED)

e('CurrencyUIFeatures.importCurrencies', 'CurrencyUIFeatures$11.call', 'CALL',
  'importCurrencies subscribes to Observable.fromCallable; RxJava runs call() on the io scheduler, which imports the currencies from the system locales',
  cls='non_standard', via='RxJava 1 (library, INFERRED, not read): Observable.fromCallable(Callable) runs Callable.call when subscribed on Schedulers.io() (subscribeOn at CurrencyUIFeatures.java:239)',
  evidence='SRC currency/CurrencyUIFeatures.java:233-240 (fromCallable, subscribeOn); auto_calls records CurrencyUIFeatures$11.call -> CurrencyUIFeatures.getService and CurrencyService.importCurrenciesFromSystemLocales (236)')

e('CurrencyUIFeatures.importCurrencies', 'CurrencyUIFeatures$10.onNext', 'CALL',
  'the Subscriber receives the Boolean result of call() on the main thread; the onNext body is empty',
  cls='non_standard', via='RxJava 1 (library, INFERRED, not read): Subscriber.onNext delivered after observeOn(AndroidSchedulers.mainThread()) (CurrencyUIFeatures.java:240)',
  evidence='SRC currency/CurrencyUIFeatures.java:241-256 (subscribe with Subscriber, onNext at 254-256)')

e('CurrencyUIFeatures.importCurrencies', 'CurrencyUIFeatures$10.onCompleted', 'CALL',
  'after call() finishes without an error RxJava calls onCompleted on the main thread, which closes the progress dialog',
  cls='non_standard', via='RxJava 1 (library, INFERRED, not read): Subscriber.onCompleted after observeOn(AndroidSchedulers.mainThread())',
  evidence='SRC currency/CurrencyUIFeatures.java:243-246; auto_calls record CurrencyUIFeatures$10.onCompleted -> DialogUtils.closeProgressDialog (244)')

e('CurrencyUIFeatures.importCurrencies', 'CurrencyUIFeatures$10.onError', 'CALL',
  'RxJava calls onError with the exception and onError logs it',
  cls='non_standard', via='RxJava 1 (library, INFERRED, not read): Subscriber.onError delivers the exception thrown by Callable.call',
  guard='call() throws, so RxJava delivers the exception to onError instead of onNext and onCompleted',
  evidence='SRC currency/CurrencyUIFeatures.java:248-251 (onError, Timber.e at 250)')

# ================================================================== sup cuts (D14a)

# Caller showActiveInactiveSelectorForUpdate is UNREACHABLE in this batch (its only caller is in an unreachable fragment).
# Its auto CALLs to its two listeners and to getContext are cut here; the one auto CALL out of the dead listener $9.onClick is cut too.
sup(('CurrencyUIFeatures.showActiveInactiveSelectorForUpdate', 'CurrencyUIFeatures$9.<init>'),
    ('CurrencyUIFeatures.showActiveInactiveSelectorForUpdate', 'CurrencyUIFeatures$8.<init>'),
    ('CurrencyUIFeatures.showActiveInactiveSelectorForUpdate', 'CurrencyUIFeatures.getContext'),
    ('CurrencyUIFeatures$9.onClick', 'ExchangeRateUpdateConfirmedEvent.<init>'))

# Callers in batch 050 (CurrencyRecyclerListFragment): the fragment is UNREACHABLE because CurrencyRecyclerListActivity has no start site
# (AndroidManifest.xml:359 has no intent-filter; the only Intent, MainActivity.java:644, is commented out). Their auto CALLs into batch 048
# are cut here, because the owner of the target writes the cut (D14a). Batch 050 must label these three callers UNREACHABLE; if it does not,
# remove these nine pairs and restore the edges.
sup(('CurrencyRecyclerListFragment.onOptionsItemSelected', 'CurrencyUIFeatures.<init>'),
    ('CurrencyRecyclerListFragment.onOptionsItemSelected', 'CurrencyUIFeatures.showDialogImportAllCurrencies'),
    ('CurrencyRecyclerListFragment.onOptionsItemSelected', 'CurrencyUIFeatures.showActiveInactiveSelectorForUpdate'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyUIFeatures.<init>'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyUIFeatures.startCurrencyEditActivity'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyUIFeatures.notifyCurrencyCanNotBeDeleted'),
    ('CurrencyRecyclerListFragment.onContextItemSelected', 'CurrencyUIFeatures.showDialogDeleteCurrency'),
    ('CurrencyRecyclerListFragment.onEvent(PriceDownloadedEvent)', 'CurrencyUIFeatures.<init>'),
    ('CurrencyRecyclerListFragment.onEvent(PriceDownloadedEvent)', 'CurrencyUIFeatures.onPriceDownloaded'))

# ================================================================== UNREACHABLE (batch 048)

UNREACHABLE['CurrencyUIFeatures.showActiveInactiveSelectorForUpdate'] = ('no_trigger_in_app',
  'Its only caller is CurrencyRecyclerListFragment.onOptionsItemSelected (CurrencyRecyclerListFragment.java:311). That fragment is created only by CurrencyRecyclerListActivity.onCreate (line 41), and nothing starts that activity: the manifest entry (AndroidManifest.xml:359) has no intent-filter and the only Intent for it (MainActivity.java:644) is commented out. The currency menu starts CurrencyListActivity instead (MainActivity.java:643). Its auto CALLs are cut by sup above.',
  'SRC currency/CurrencyUIFeatures.java:185-211; recycler/CurrencyRecyclerListFragment.java:311; recycler/CurrencyRecyclerListActivity.java:41; AndroidManifest.xml:359; MainActivity.java:641-646; label_048.grep.txt sections B, E',
  'SOURCE')

UNREACHABLE['CurrencyUIFeatures$8.<init>'] = ('no_trigger_in_app',
  'Constructed only inside showActiveInactiveSelectorForUpdate, which is UNREACHABLE. Its auto CALL (CurrencyUIFeatures.java:195) is cut by sup above.',
  'SRC currency/CurrencyUIFeatures.java:203-208; auto_calls record showActiveInactiveSelectorForUpdate -> CurrencyUIFeatures$8.<init>; label_048.grep.txt section D',
  'SOURCE')

UNREACHABLE['CurrencyUIFeatures$8.onClick'] = ('no_trigger_in_app',
  'Empty positive listener of the single-choice dialog built by showActiveInactiveSelectorForUpdate, which is UNREACHABLE, so the dialog is never shown and the framework never calls this listener. The class file has no post or dismiss call (section C).',
  'SRC currency/CurrencyUIFeatures.java:203-208; label_048.grep.txt section C',
  'SOURCE')

UNREACHABLE['CurrencyUIFeatures$9.<init>'] = ('no_trigger_in_app',
  'Constructed only inside showActiveInactiveSelectorForUpdate, which is UNREACHABLE. Its auto CALL (CurrencyUIFeatures.java:194) is cut by sup above.',
  'SRC currency/CurrencyUIFeatures.java:195-202; auto_calls record showActiveInactiveSelectorForUpdate -> CurrencyUIFeatures$9.<init>; label_048.grep.txt section D',
  'SOURCE')

UNREACHABLE['CurrencyUIFeatures$9.onClick'] = ('no_trigger_in_app',
  'Single-choice listener of the dialog built by showActiveInactiveSelectorForUpdate, which is UNREACHABLE, so no click is delivered. Its auto CALL to ExchangeRateUpdateConfirmedEvent.<init> (CurrencyUIFeatures.java:199) is cut by sup above, so that event constructor is not reached from here.',
  'SRC currency/CurrencyUIFeatures.java:197-201; auto_calls record CurrencyUIFeatures$9.onClick -> ExchangeRateUpdateConfirmedEvent.<init> (199); label_048.grep.txt sections C, D',
  'SOURCE')

UNREACHABLE['ExchangeRateUpdaterFactory.<init>'] = ('no_trigger_in_app',
  'The class has only static members and no source in the source root constructs it (section B is empty for new ExchangeRateUpdaterFactory). No auto record has it as destination, so the implicit default constructor is never called.',
  'SRC currency/ExchangeRateUpdaterFactory.java:33 (no constructor declared); label_048.grep.txt section B',
  'SOURCE')

# ---- part 050 (2026-10-29)
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

# ---- part 051 (2026-10-29)
# ================================================================== batch 051 (label_051): RecyclerItemClickListener (4 methods),
# RecyclerItemClickListener$1 (2), Dataset (7), DatasetType.<clinit> (1), MmxOpenHelper (19), PasswordActivity (4), PasswordActivity$1 (2).
# Result: 30 REACHABLE, 9 UNREACHABLE (see the .md rows). Rows and printed lines: graphs/MMEX/parts/label_051.md.
# Auto CALL records (auto_calls.json) are not rewritten here. This file writes:
#   - INTENT, LIFECYCLE, ENTERS and GUI edges for PasswordActivity (the password screen),
#   - FRAMEWORK edge for the finalizer of MmxOpenHelper, non_standard CALL edges for the SQLite callbacks of MmxOpenHelper (library, INFERRED),
#   - UNREACHABLE entries for the RecyclerItemClickListener chain (its only construction site is in batch 050), hasPassword, setPassword
#     and the base Dataset.setValueFromCursor,
#   - 2 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.
# The screen S_PASSWORD is new (grep of parts and graph_def: no S_PASSWORD before this part).

SCREENS.update({
    'S_PASSWORD': 'Password screen (PasswordActivity): one password field (txtPassword) and the OK button (btnSubmit); it is shown before a database opens',
})

# ================================================================== PasswordActivity: who starts it (INTENT)

e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'PasswordActivity.<init>', 'INTENT',
  'the drawer or option menu starts PasswordActivity: the recent-database item (intent built at line 599, started for a result at 601), menu_open_database (619) and menu_create_database (627)',
  evidence='SRC home/MainActivity.java:597-601, 618-628 (the same switch as case menu_home); FW-SRC core/java/android/app/Instrumentation.java:1143-1148 (newActivity creates the instance with clazz.newInstance())')

e('MainActivity.handleIntent', 'PasswordActivity.<init>', 'INTENT',
  'a .db file is opened from another app: handleIntent starts PasswordActivity when the VIEW intent carries data',
  env=env_text('outside package: another app opens a file with MMEX (an ACTION_VIEW intent that the MainActivity VIEW filter accepts)', ('other_app',)),
  evidence='SRC home/MainActivity.java:210 (handleIntent is called from onCreate, 179-245), 1184-1197 (the start is inside the intent.getData() != null branch at 1189); FW-SRC core/java/android/app/Instrumentation.java:1143-1148')

e('SelectDatabaseActivity.onCreateDatabaseClick', 'PasswordActivity.<init>', 'INTENT',
  'tap the create-database button on the select-database screen (@OnClick createDatabaseButton)',
  gui=['Tap the Create database button on the select-database screen'],
  evidence='SRC home/SelectDatabaseActivity.java:99-101; FW-SRC core/java/android/app/Instrumentation.java:1143-1148')

e('SelectDatabaseActivity.onOpenDatabaseClick', 'PasswordActivity.<init>', 'INTENT',
  'tap the open-database button on the select-database screen (@OnClick openDatabaseButton)',
  gui=['Tap the Open database button on the select-database screen'],
  evidence='SRC home/SelectDatabaseActivity.java:106-108; FW-SRC core/java/android/app/Instrumentation.java:1143-1148')

# ================================================================== PasswordActivity: lifecycle, the screen, the OK button

e('PasswordActivity.<init>', 'PasswordActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/Instrumentation.java:1212 (callActivityOnCreate); FW-SRC core/java/android/app/Activity.java:6989-6999 (performCreate calls onCreate)')

e('PasswordActivity.onCreate', 'S_PASSWORD', 'ENTERS',
  'the password screen is shown (onCreate inflates activity_password and finds the OK button)',
  evidence='SRC database/PasswordActivity.java:39-48; SRC res/layout/activity_password.xml:47-60 (txtPassword at 48, btnSubmit at 57)')

gui('S_PASSWORD', 'PasswordActivity$1.onClick', 'Tap the OK button (btnSubmit) with the password typed in the password field',
    evidence='SRC res/layout/activity_password.xml:48, 56-60; SRC database/PasswordActivity.java:51-58')

# ================================================================== MmxOpenHelper: framework and library callbacks

e('MmxOpenHelper.<init>', 'MmxOpenHelper.finalize', 'FRAMEWORK',
  'the garbage collector finalises the helper object after it is no longer reachable (the ART finalizer calls finalize on objects whose class overrides it)',
  evidence='SRC database/MmxOpenHelper.java:309-312 (finalize overrides Object.finalize); INFERRED ART finalizer (libcore not read)')

_CALLBACK_TRIGGER = {
    'onCreate': 'opening a database file that does not exist yet runs onCreate (the table script and the initial data)',
    'onOpen': 'every open of the database runs onOpen (write-ahead logging is turned off)',
    'onUpgrade': 'opening a database whose stored version is older than databaseVersion runs onUpgrade',
}
for _src in ('MmxOpenHelper.getReadableDatabase', 'MmxOpenHelper.getWritableDatabase'):
    for _cb, _why in _CALLBACK_TRIGGER.items():
        e(_src, 'MmxOpenHelper.' + _cb, 'CALL',
          _why + ' (the SQLCipher open is done by the library, so this is INFERRED)',
          evidence='SRC database/MmxOpenHelper.java:132-142 (getReadableDatabase: factory and create at 134, 140) or 144-154 (getWritableDatabase at 152); library androidx SupportSQLiteOpenHelper.Callback and net.sqlcipher SupportFactory not read: INFERRED',
          cls='non_standard',
          via='androidx.sqlite SupportSQLiteOpenHelper.Callback, invoked by the SQLCipher SupportFactory helper (library, INFERRED, not read)')

# ================================================================== UNREACHABLE: RecyclerItemClickListener chain and dead helpers

UNREACHABLE['RecyclerItemClickListener.<init>'] = ('no_trigger_in_app',
    'its only construction site is CurrencyRecyclerListFragment.initializeList (batch 050, CurrencyRecyclerListFragment.java:369) and that fragment has no start: CurrencyRecyclerListActivity is started nowhere (manifest line 359 has no intent-filter; the only start, MainActivity.java:644, is commented out)',
    'RecyclerItemClickListener.java:41-48; CurrencyRecyclerListFragment.java:369; AndroidManifest.xml:359; MainActivity.java:644 (commented)', 'SOURCE')

UNREACHABLE['RecyclerItemClickListener.onInterceptTouchEvent'] = ('no_trigger_in_app',
    'the listener is registered only at CurrencyRecyclerListFragment.java:369 (addOnItemTouchListener) in the unreachable fragment; the CHA call to CurrencyRecyclerListFragment$1.onItemClick is cut by sup below',
    'RecyclerItemClickListener.java:50-58; CurrencyRecyclerListFragment.java:369', 'SOURCE')

UNREACHABLE['RecyclerItemClickListener.onRequestDisallowInterceptTouchEvent'] = ('no_trigger_in_app',
    'empty body; the RecyclerView calls it only for the registered listener, which is unreachable (see the constructor)',
    'RecyclerItemClickListener.java:62-63; CurrencyRecyclerListFragment.java:369', 'SOURCE')

UNREACHABLE['RecyclerItemClickListener.onTouchEvent'] = ('no_trigger_in_app',
    'empty body; the RecyclerView calls it only for the registered listener, which is unreachable (see the constructor)',
    'RecyclerItemClickListener.java:60; CurrencyRecyclerListFragment.java:369', 'SOURCE')

UNREACHABLE['RecyclerItemClickListener$1.<init>'] = ('no_trigger_in_app',
    'constructed only in RecyclerItemClickListener.<init> (line 43), which is itself unreachable; the auto CALL is cut by sup below',
    'RecyclerItemClickListener.java:43', 'SOURCE')

UNREACHABLE['RecyclerItemClickListener$1.onSingleTapUp'] = ('no_trigger_in_app',
    'called by the GestureDetector only while onInterceptTouchEvent runs (line 53); that method is unreachable',
    'RecyclerItemClickListener.java:43-46, 53', 'SOURCE')

UNREACHABLE['Dataset.setValueFromCursor'] = ('no_trigger_in_app',
    'both call sites have the static type QueryAccountBills, which overrides the method; the auto CALL records resolve exactly to the override and no override calls super, so the base body never runs',
    'Dataset.java:122; HomeFragment.java:822-823; AccountRepository.java:71, 84; QueryAccountBills.java:209; auto_calls.json (AccountRepository.loadAccountBills -> QueryAccountBills.setValueFromCursor, AccountRepository.java:84, exact)', 'SOURCE')

UNREACHABLE['MmxOpenHelper.hasPassword'] = ('no_trigger_in_app',
    'no caller anywhere in the source root (grep for hasPassword over final_java_only/.../src/main: the definition at MmxOpenHelper.java:161 is the only match)',
    'MmxOpenHelper.java:161-163', 'SOURCE')

UNREACHABLE['MmxOpenHelper.setPassword'] = ('no_trigger_in_app',
    'no caller on MmxOpenHelper: PasswordActivity.returnPassword sets the password on MmexApplication (PasswordActivity.java:65), and MmxOpenHelper reads it from MmexApplication at its constructor (MmxOpenHelper.java:70)',
    'MmxOpenHelper.java:156-158; PasswordActivity.java:65; MmexApplication.java:90; grep of src/main for setPassword', 'SOURCE')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE here

sup(('RecyclerItemClickListener.<init>', 'RecyclerItemClickListener$1.<init>'))

# ---- part 047 (2026-10-29)
# label_047.py: batch 047 (34 methods in 4 class groups): CurrencyService (24), CurrencyService$1 (2),
# CurrencyService_Factory (4), CurrencyService_MembersInjector (4).
# Result: 26 REACHABLE, 8 UNREACHABLE, 0 INCOMPLETE. Rows and printed lines: graphs/MMEX/parts/label_047.md.
# Grep evidence: graphs/MMEX/parts/label_047.grep.txt (sections A to C).
# Auto CALL records (auto_calls.json) are not rewritten here. This file writes:
#   - 1 non_standard CALL edge from getUsedCurrencies to the anonymous Comparator's compare (JDK sort, INFERRED),
#   - 8 UNREACHABLE entries (4 CurrencyService, 1 Factory, 3 MembersInjector),
#   - 19 sup pairs (D14a): auto CALL records whose caller is one of the 8 UNREACHABLE methods above.
# The DaggerMmxComponent edges that reach the Factory and MembersInjector methods are owned by the batch holding DaggerMmxComponent (not this batch).

# ================================================================== Collections.sort comparator (JDK, library not read: INFERRED)

e('CurrencyService.getUsedCurrencies', 'CurrencyService$1.compare', 'CALL',
  'getUsedCurrencies sorts the used currencies with the anonymous Comparator; the JDK sort calls compare on it',
  cls='non_standard', via='JDK Collections.sort(List, Comparator) calls Comparator.compare (library, INFERRED, not read)',
  evidence='SRC currency/CurrencyService.java:159-164 (new Comparator at 159, compare at 161-163, getName call at 162); auto_calls records CurrencyService.getUsedCurrencies -> CurrencyService$1.<init> (159) and CurrencyService$1.compare -> Currency.getName (162)')

# ================================================================== UNREACHABLE (batch 047)

UNREACHABLE['CurrencyService.getCurrency(String)'] = ('no_trigger_in_app',
  'No caller in the app: no auto CALL record has it as destination (label_047.grep.txt section C). The only literal call is in the unit-test helper DataHelpers.java:91 (src/test, not in the app graph). Its callee getIdForCode is also UNREACHABLE, so its auto CALL records are cut by sup below.',
  'SRC currency/CurrencyService.java:105-108; label_047.grep.txt sections A, C',
  'SOURCE')

UNREACHABLE['CurrencyService.getIdForCode'] = ('no_trigger_in_app',
  'Its only caller is getCurrency(String), which is UNREACHABLE (auto CALL at CurrencyService.java:106; no other record). Its outgoing auto CALL records are cut by sup below.',
  'SRC currency/CurrencyService.java:128-141; auto_calls record CurrencyService.getCurrency(String) -> CurrencyService.getIdForCode (106); label_047.grep.txt section C',
  'SOURCE')

UNREACHABLE['CurrencyService.getSymbolFor'] = ('no_trigger_in_app',
  'No caller in the app: no auto CALL record has it as destination; the only mention outside its own definition is the commented-out test line CurrencyServiceTests.java:77; the class directory names it only in CurrencyService.class (label_047.grep.txt sections A, B, C).',
  'SRC currency/CurrencyService.java:123-126; label_047.grep.txt sections A, B, C',
  'SOURCE')

UNREACHABLE['CurrencyService.getUnusedCurrencies'] = ('no_trigger_in_app',
  'Its only callers are in CurrencyRecyclerListFragment (CurrencyRecyclerListFragment.java:254 and 391), and that fragment is never created: CurrencyRecyclerListActivity has no start site (AndroidManifest.xml:359 has no intent-filter; the only Intent for it, MainActivity.java:644, is commented out). Batch 050 owns CurrencyRecyclerListFragment and must confirm there is no start site. If batch 050 finds one, change this entry and remove the eight sup pairs below.',
  'SRC currency/CurrencyService.java:169-184; recycler/CurrencyRecyclerListFragment.java:254, 391; recycler/CurrencyRecyclerListActivity.java:41; AndroidManifest.xml:359; MainActivity.java:644; label_047.grep.txt sections A, C',
  'SOURCE')

e('FormatUtilities_Factory.get', 'CurrencyService_Factory.get', 'CALL',
  'FormatUtilities_Factory.get calls currencyServiceProvider.get() at bytecode offset 25 (javax.inject.Provider, invokeinterface); the Provider is the CurrencyService_Factory instance built in DaggerMmxComponent',
  evidence='INFERRED generated FormatUtilities_Factory.class in app/build/intermediates/javac/debug/classes/com/money/manager/ex/core/: get offset 25 (offset as read in batch 055); the currencyServiceProvider Fieldref is in batch036_cp_scan.txt line 54; target is generated CurrencyService_Factory.class',
  cls='non_standard',
  via='javax.inject.Provider currencyServiceProvider (generated field), whose runtime class is CurrencyService_Factory')

UNREACHABLE['CurrencyService_MembersInjector.create'] = ('no_trigger_in_app',
  'No caller: no auto CALL record names it. DaggerMmxComponent injects CurrencyService by calling injectMRepository directly (DaggerMmxComponent.java:374), not through a MembersInjector instance. Its outgoing record to <init> is cut by sup below.',
  'generated: CurrencyService_MembersInjector.class in the class directory; auto_calls: no record has create as destination (grep.txt section C: 0 incoming); its only outgoing record is create -> <init> (CurrencyService_MembersInjector.java:21); DaggerMmxComponent.java:374 is the injectMRepository call, not create; label_047.grep.txt sections B, C',
  'INFERRED')

UNREACHABLE['CurrencyService_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Its only caller is CurrencyService_MembersInjector.create, which is UNREACHABLE (auto CALL at CurrencyService_MembersInjector.java:21; no other record).',
  'auto_calls record CurrencyService_MembersInjector.create -> <init> (CurrencyService_MembersInjector.java:21); label_047.grep.txt section C',
  'INFERRED')

UNREACHABLE['CurrencyService_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'MembersInjector.injectMembers runs only through a MembersInjector<CurrencyService> instance, and none is created or held (create has no caller, and the component calls injectMRepository directly). No auto CALL record names it. Its outgoing record to injectMRepository (CurrencyService_MembersInjector.java:26) is cut by sup below.',
  'generated: CurrencyService_MembersInjector.class in the class directory; auto_calls record CurrencyService_MembersInjector.java:26; label_047.grep.txt sections B, C',
  'INFERRED')

# ================================================================== sup cuts (D14a): outgoing auto CALL records of the UNREACHABLE methods above

sup(('CurrencyService.getCurrency(String)', 'CurrencyService.getCurrency(Integer)'),
    ('CurrencyService.getCurrency(String)', 'CurrencyService.getIdForCode'),
    ('CurrencyService.getSymbolFor', 'Currency.getCode'),
    ('CurrencyService.getSymbolFor', 'CurrencyService.getCurrency(Integer)'),
    ('CurrencyService.getIdForCode', 'Currency.getCurrencyId'),
    ('CurrencyService.getIdForCode', 'CurrencyRepository.loadCurrency(String)'),
    ('CurrencyService.getIdForCode', 'CurrencyService.getRepository'),
    ('CurrencyService.getUnusedCurrencies', 'CurrencyService.getUsedCurrencies'),
    ('CurrencyService.getUnusedCurrencies', 'Currency.getCurrencyId'),
    ('CurrencyService.getUnusedCurrencies', 'CurrencyRepository.getAllColumns'),
    ('CurrencyService.getUnusedCurrencies', 'Select.<init>(String[])'),
    ('CurrencyService.getUnusedCurrencies', 'Select.where(String)'),
    ('CurrencyService.getUnusedCurrencies', 'Select.orderBy'),
    ('CurrencyService.getUnusedCurrencies', 'RepositoryBase.query(Class,Select)'),
    ('CurrencyService.getUnusedCurrencies', 'CurrencyService.getRepository'),
    ('CurrencyService_MembersInjector.create', 'CurrencyService_MembersInjector.<init>'),
    ('CurrencyService_MembersInjector.injectMembers', 'CurrencyService_MembersInjector.injectMRepository'))

# ---- part 053 (2026-10-29)
# ================================================================== batch 053 (label_053): QueryCategorySubCategory (13 methods),
# QueryReportIncomeVsExpenses (3), SQLDataSet (2), SQLTypeTransaction.<clinit> (1), TableAssets (2), TransactionStatus (3),
# ViewMobileData (4), WhereStatementGenerator (11). 39 methods: 30 REACHABLE, 9 UNREACHABLE.
# Rows and printed lines: graphs/MMEX/parts/label_053.md.
# No e() edges and no SCREENS: every REACHABLE row rests on an auto_calls.json CALL record, which the build adds.
# This file writes:
#   - UNREACHABLE entries for: QueryCategorySubCategory.getCategSubName, setCategSubName and setValueFromCursor (no caller
#     reaches them), SQLDataSet.getAllColumns, TableAssets.<init> and getAllColumns, TransactionStatus.<init>,
#     ViewMobileData.getAllColumns, and ViewMobileData.setWhere (its only call sits in a branch that never runs),
#   - 13 sup pairs: auto CALL records whose caller is UNREACHABLE (D14a), plus the never-taken-branch cut for
#     QueryReportIncomeVsExpenses.initialize -> ViewMobileData.setWhere (a judgment call, flagged in the report), and the three
#     CurrencyRepository.load -> WhereStatementGenerator records that batch 046 deferred here (CurrencyRepository.load is
#     UNREACHABLE in batch 046, label_046.py:62-80).

# ================================================================== QueryCategorySubCategory: UNREACHABLE

UNREACHABLE['QueryCategorySubCategory.getCategSubName'] = ('no_trigger_in_app',
    'Getter with no caller. No source file calls it, and no auto record has it as dst. CATEGSUBNAME appears only as an SQL alias in the query resource, not as a call',
    'QueryCategorySubCategory.java:66-68; res/raw/query_categorysubcategory.sql:6, 17', 'SOURCE')

UNREACHABLE['QueryCategorySubCategory.setCategSubName'] = ('no_trigger_in_app',
    'Its only caller is setValueFromCursor (line 105), which has no caller, so this setter is never reached; the auto CALL is cut by sup below',
    'QueryCategorySubCategory.java:105 (auto record setValueFromCursor -> setCategSubName)', 'SOURCE')

UNREACHABLE['QueryCategorySubCategory.setValueFromCursor'] = ('no_trigger_in_app',
    'Override of the protected Dataset.setValueFromCursor (Dataset.java:122). No caller: no auto record (exact or cha) has it as dst. The base method is called only on receivers typed QueryAccountBills, which resolve to that class override (HomeFragment.java:822-823, AccountRepository.java:84)',
    'QueryCategorySubCategory.java:91-106; Dataset.java:122; auto_calls.json (no record with this dst)', 'SOURCE')

# ================================================================== SQLDataSet, TableAssets, TransactionStatus, ViewMobileData: UNREACHABLE

UNREACHABLE['SQLDataSet.getAllColumns'] = ('no_trigger_in_app',
    'Returns null (stub). No caller: no auto record (exact or cha) has it as dst. The abstract Dataset.getAllColumns has no call site that could dispatch here',
    'SQLDataSet.java:27-30; auto_calls.json (no record)', 'SOURCE')

UNREACHABLE['TableAssets.<init>'] = ('no_trigger_in_app',
    'The class is never instantiated (no new TableAssets in the app source) and no auto record has the constructor as dst. Its two auto CALLs (Dataset.<init>, DatasetType.<clinit>) are cut by sup below',
    'TableAssets.java:30-32; grep of the app source (no new TableAssets)', 'SOURCE')

UNREACHABLE['TableAssets.getAllColumns'] = ('no_trigger_in_app',
    'Returns the column list. No caller: the class is never instantiated and no auto record has it as dst',
    'TableAssets.java:34-37', 'SOURCE')

UNREACHABLE['TransactionStatus.<init>'] = ('no_trigger_in_app',
    'Implicit default constructor: the class declares no constructor and only static members are used (getStatusAsString and getBackgroundColorFromStatus are static). No new TransactionStatus in the app source, and no auto record has it as dst',
    'TransactionStatus.java:29, 34, 75; grep of the app source (no new TransactionStatus)', 'SOURCE')

UNREACHABLE['ViewMobileData.getAllColumns'] = ('no_trigger_in_app',
    'Returns the column list. No caller: no auto record (exact or cha) has it as dst',
    'ViewMobileData.java:72-79; auto_calls.json (no record)', 'SOURCE')

UNREACHABLE['ViewMobileData.setWhere'] = ('branch_never_taken',
    'Its only caller is QueryReportIncomeVsExpenses.initialize (line 50), inside the guard if(!TextUtils.isEmpty(whereStatement)) at line 49. initialize is called only from the constructor (line 33) with null, and TextUtils.isEmpty(null) is true, so the guarded call never runs. The auto CALL (line 50) is cut by sup below as a call in a branch that never runs',
    'ViewMobileData.java:81-83; QueryReportIncomeVsExpenses.java:33, 46-50; TextUtils.isEmpty(null) is true (Android API contract; framework source not in fw_src)', 'INFERRED')

# ================================================================== sup (D14a and never-taken branch)

sup(('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.getAllColumns'),
    ('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.setCategId'),
    ('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.setCategName'),
    ('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.setCategSubName'),
    ('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.setSubCategId'),
    ('QueryCategorySubCategory.setValueFromCursor', 'QueryCategorySubCategory.setSubcategoryName'),
    ('TableAssets.<init>', 'Dataset.<init>'),
    ('TableAssets.<init>', 'DatasetType.<clinit>'),
    ('QueryReportIncomeVsExpenses.initialize', 'ViewMobileData.setWhere'),
    ('ViewMobileData.setWhere', 'ViewMobileData.initialize'),
    ('CurrencyRepository.load', 'WhereStatementGenerator.<init>'),
    ('CurrencyRepository.load', 'WhereStatementGenerator.addStatement(String,String,Integer)'),
    ('CurrencyRepository.load', 'WhereStatementGenerator.getWhere'))

# ---- part 049 (2026-10-29)
# batch 049 (label_049): com.money.manager.ex.currency.list.CurrencyListActivity (4 methods), CurrencyListAdapter (3),
# CurrencyListFragment (26, including its implicit <init>), CurrencyListFragment$1 (4) and
# com.money.manager.ex.currency.recycler.CurrencyContentObserver (3). 40 methods in all.
# Rows and printed lines: graphs/MMEX/parts/label_049.md.
# CALL edges between the batch methods and to other classes come from auto_calls.json, including the receiver-variant
# records BaseListFragment.onActivityCreated@CurrencyListFragment, BaseListFragment.onPreQueryTextChange@CurrencyListFragment
# and BaseListFragment.setResultAndFinish@CurrencyListFragment, so none are written here except the sup cut below.
# androidx Fragment, LoaderManager, CursorAdapter, SearchView and the options-menu dispatch are not in fw_src: those claims are INFERRED.
# The class initialiser and the INTENT edges into it follow the batch 028 pattern.

SCREENS.update({
    'S_CURRENCY_LIST': 'Currency list (CurrencyListActivity with CurrencyListFragment): the list of currencies, opened from the main menu, from the account editor, or by another app (ACTION_PICK or ACTION_EDIT)',
})

# ---- entry from another app (exported=true, PICK and EDIT filters) and the in-app intents

e('S_ENTRY', 'CurrencyListActivity.<init>', 'ENTRY',
  'another app sends an ACTION_PICK or ACTION_EDIT intent to the exported CurrencyListActivity',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to CurrencyListActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:205-215 (exported=true; PICK and EDIT filters at 210-214); FW-SRC core/java/android/app/ActivityThread.java:2665-2672 (mInstrumentation.newActivity); FW-SRC core/java/android/app/Instrumentation.java:1170-1174 (loadClass(className).newInstance())')

e('S_ENTRY', 'CurrencyListActivity.<clinit>', 'ENTRY',
  'the first CurrencyListActivity instance (the exported-intent start above) initialises the class',
  env=env_text('outside package: another app sends an ACTION_PICK or ACTION_EDIT intent to CurrencyListActivity (exported=true)', ('other_app',)),
  evidence='SRC currency/list/CurrencyListActivity.java:39 (FRAGMENTTAG = CurrencyListActivity.class.getSimpleName() + "_Fragment" is a method call, so the class has a static initialiser); SRC AndroidManifest.xml:205-215; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'CurrencyListActivity.<init>', 'INTENT',
  'the Currencies item of the main menu starts CurrencyListActivity with ACTION_EDIT',
  gui=['Tap Currencies in the main menu (drawer or options menu)'],
  evidence='SRC home/MainActivity.java:641-646 (case R.id.menu_currency at 641; new Intent 643; ACTION_EDIT 645; startActivity 646); FW-SRC core/java/android/app/Instrumentation.java:1170-1174')

e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'CurrencyListActivity.<clinit>', 'INTENT',
  'the first CurrencyListActivity instance (the start above) initialises the class',
  gui=['Tap Currencies in the main menu (drawer or options menu)'],
  evidence='SRC home/MainActivity.java:641-646; SRC currency/list/CurrencyListActivity.java:39; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

e('AccountEditActivity$4.onClick', 'CurrencyListActivity.<init>', 'INTENT',
  'tap the currency field in the account editor: startActivityForResult(ACTION_PICK) starts CurrencyListActivity',
  gui=['Tap the currency field in the account editor'],
  evidence='SRC account/AccountEditActivity.java:390-395 (setOnClickListener 390; new Intent 393; ACTION_PICK 394; startActivityForResult 395); FW-SRC core/java/android/app/Instrumentation.java:1170-1174')

e('AccountEditActivity$4.onClick', 'CurrencyListActivity.<clinit>', 'INTENT',
  'the first CurrencyListActivity instance (the start above) initialises the class',
  gui=['Tap the currency field in the account editor'],
  evidence='SRC account/AccountEditActivity.java:390-395; SRC currency/list/CurrencyListActivity.java:39; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; INFERRED the JVM initialises the class before the first instance (Java language rule, not read from a source)')

# ---- lifecycle: activity and fragment (framework; androidx Fragment is INFERRED)

e('CurrencyListActivity.<init>', 'CurrencyListActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2729-2731 (callActivityOnCreate after newActivity at 2669); FW-SRC core/java/android/app/Instrumentation.java:1212-1214 (callActivityOnCreate calls performCreate at 1214); FW-SRC core/java/android/app/Activity.java:6993-6999 (performCreate calls onCreate at 6999)')

e('CurrencyListFragment.<init>', 'CurrencyListFragment.onCreate', 'LIFECYCLE',
  'the fragment manager calls onCreate after the constructor, for the fragment that CurrencyListActivity.onCreate adds (commit at 63-66)',
  evidence='SRC currency/list/CurrencyListActivity.java:50, 63-66; SRC currency/list/CurrencyListFragment.java:86-101 (onCreate); INFERRED androidx FragmentManager calls onCreate after the constructor (library not read)')

e('CurrencyListFragment.onCreate', 'CurrencyListFragment.onCreateView', 'LIFECYCLE',
  'the framework calls onCreateView after onCreate',
  evidence='SRC currency/list/CurrencyListFragment.java:86-108 (onCreate 86-101; onCreateView 103-108); INFERRED androidx Fragment lifecycle (library not read)')

e('AbsListFragment.onCreateView', 'CurrencyListFragment.onViewCreated', 'LIFECYCLE',
  'the framework calls onViewCreated after the view is created by the inherited onCreateView (AbsListFragment inflates abs_list_fragment.xml). CurrencyListFragment overrides onViewCreated without calling super (154-156), so the BaseListFragment body that label_026 writes does not run for this receiver',
  evidence='SRC AbsListFragment.java:74-80 (onCreateView); SRC currency/list/CurrencyListFragment.java:153-156 (onViewCreated, no super); SRC common/BaseListFragment.java:62-67; INFERRED androidx Fragment lifecycle (library not read)')

e('CurrencyListFragment.onViewCreated', 'CurrencyListFragment.onActivityCreated', 'LIFECYCLE',
  'the framework calls onActivityCreated after onViewCreated',
  evidence='SRC currency/list/CurrencyListFragment.java:153-156 (onViewCreated), 124-151 (onActivityCreated); INFERRED androidx Fragment lifecycle (library not read)')

e('CurrencyListActivity.onCreate', 'CurrencyListFragment.onActivityCreated', 'LIFECYCLE',
  'the fragment that CurrencyListActivity.onCreate adds (commit at 63-66) gets its onActivityCreated call after the activity has created it, the same pattern as batch 029',
  evidence='SRC currency/list/CurrencyListActivity.java:50, 63-66; SRC currency/list/CurrencyListFragment.java:124-151; INFERRED androidx FragmentManager (library not read)')

e('CurrencyListFragment.onActivityCreated', 'CurrencyListFragment.onStart', 'LIFECYCLE',
  'the framework calls onStart after onActivityCreated; onStart registers the fragment on EventBus (line 114)',
  evidence='SRC currency/list/CurrencyListFragment.java:110-115 (onStart), 124-151; INFERRED androidx Fragment lifecycle (library not read)')

e('CurrencyListFragment.onStart', 'CurrencyListFragment.onStop', 'LIFECYCLE',
  'the framework stops the fragment after onStart when the activity leaves the foreground; onStop unregisters EventBus (line 121)',
  evidence='SRC currency/list/CurrencyListFragment.java:117-122 (onStop); INFERRED androidx Fragment lifecycle (library not read)')

# ---- the screen (ENTERS): the activity and the fragment both show the currency list

e('CurrencyListActivity.onCreate', 'S_CURRENCY_LIST', 'ENTERS',
  'the activity creates the currency list fragment and commits it to the content view (add and commit at 63-66)',
  evidence='SRC currency/list/CurrencyListActivity.java:41-67 (fragment at 50; add and commit at 63-66)')

e('CurrencyListFragment.onActivityCreated', 'S_CURRENCY_LIST', 'ENTERS',
  'the fragment is attached and its list is set up (adapter 139, loader 145) once the activity has created it',
  evidence='SRC currency/list/CurrencyListFragment.java:124-151 (adapter 139; loadData 145)')

# ---- framework dispatch (FRAMEWORK): options menu, context menu, loader and adapter callbacks

e('CurrencyListFragment.onActivityCreated', 'CurrencyListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'onActivityCreated calls setHasOptionsMenu(true) (line 136), so the framework builds the options menu through onCreateOptionsMenu, which calls super (162) and adds its items',
  evidence='SRC currency/list/CurrencyListFragment.java:136, 160-173 (super 161-162); SRC common/BaseListFragment.java:113-149 (the inherited body reached by the super call); INFERRED androidx FragmentManager dispatches onCreateOptionsMenu to fragments with an options menu (library not read)')

e('CurrencyListFragment.onListItemClick', 'CurrencyListFragment.onCreateContextMenu', 'FRAMEWORK',
  'the row tap calls openContextMenu (line 336); the framework then calls onCreateContextMenu for the list (registered for the context menu at line 155)',
  evidence='SRC currency/list/CurrencyListFragment.java:155 (registerForContextMenu), 215-229 (onCreateContextMenu), 329-341 (openContextMenu 336); INFERRED View.openContextMenu dispatch (android.view.View not read in this batch)')

e('CurrencyListFragment.loadData', 'CurrencyListFragment$1.onCreateLoader', 'FRAMEWORK',
  'initLoader (line 499) starts the currency loader and the LoaderManager calls onCreateLoader',
  evidence='SRC currency/list/CurrencyListFragment.java:498-500 (initLoader at 499, this.loaderCallbacks); INFERRED androidx LoaderManager.initLoader calls LoaderCallbacks.onCreateLoader (library not read)')

e('CurrencyListFragment.reloadData', 'CurrencyListFragment$1.onCreateLoader', 'FRAMEWORK',
  'restartLoader (reloadData, 502-504) calls onCreateLoader again for the restarted loader',
  evidence='SRC currency/list/CurrencyListFragment.java:502-504 (restartLoader); INFERRED androidx LoaderManager.restartLoader calls onCreateLoader (library not read); same pattern as label_008 (AccountListFragment)')

e('CurrencyListFragment$1.onCreateLoader', 'CurrencyListFragment$1.onLoadFinished', 'FRAMEWORK',
  'the loader (MmxCursorLoader, line 459) delivers its cursor and the LoaderManager calls onLoadFinished',
  evidence='SRC currency/list/CurrencyListFragment.java:459 (new MmxCursorLoader); INFERRED androidx LoaderManager delivers the result to onLoadFinished (library not read); same pattern as label_016 and label_008')

e('CurrencyListFragment$1.onLoadFinished', 'CurrencyListFragment$1.onLoaderReset', 'FRAMEWORK',
  'a loader that has delivered data is reset (fragment destroyed or loader restarted) and the LoaderManager calls onLoaderReset',
  evidence='SRC currency/list/CurrencyListFragment.java:465-472 (onLoaderReset), 474-489 (onLoadFinished); INFERRED androidx LoaderManager calls onLoaderReset (library not read); same pattern as label_008')

e('CurrencyListFragment$1.onLoadFinished', 'CurrencyListAdapter.newView', 'FRAMEWORK',
  'adapter.changeCursor(data) (line 479) swaps in the new cursor and notifies the list; on the relayout the framework calls getView, which calls newView for a row with no scrap view',
  evidence='SRC currency/list/CurrencyListFragment.java:477, 479; SRC currency/list/CurrencyListAdapter.java:29, 35 (extends androidx CursorAdapter); same chain as label_014.py:11-12 (the FW-SRC CursorAdapter and ListView lines cited there); androidx CursorAdapter is not in the dataset, INFERRED')

e('CurrencyListFragment$1.onLoadFinished', 'CurrencyListAdapter.bindView', 'FRAMEWORK',
  'the same relayout (changeCursor at 479) makes the framework call getView, which calls bindView for every visible row',
  evidence='SRC currency/list/CurrencyListFragment.java:479; SRC currency/list/CurrencyListAdapter.java:29, 35; same chain as label_014.py:14-16; androidx CursorAdapter INFERRED as in label_014')

# ---- EventBus (greenrobot): REGISTER edges are skipped by reachability; the ASYNC edges below carry the route to each handler

e('CurrencyListFragment.onStart', 'CurrencyListFragment.onEvent(PriceDownloadedEvent)', 'REGISTER',
  'onStart registers the fragment on EventBus; EventBus calls the @Subscribe method for PriceDownloadedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at CurrencyListFragment.java:114; @Subscribe at 354 (onEvent(PriceDownloadedEvent)); library dispatch INFERRED',
  evidence='SRC currency/list/CurrencyListFragment.java:110-122 (register at 114, unregister at 121), 354-358; INFERRED EventBus library source not read')

e('CurrencyListFragment.onStart', 'CurrencyListFragment.onEvent(ExchangeRateUpdateConfirmedEvent)', 'REGISTER',
  'onStart registers the fragment on EventBus; EventBus calls the @Subscribe method for ExchangeRateUpdateConfirmedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at CurrencyListFragment.java:114; @Subscribe at 360 (onEvent(ExchangeRateUpdateConfirmedEvent)); library dispatch INFERRED',
  evidence='SRC currency/list/CurrencyListFragment.java:110-122 (register at 114, unregister at 121), 360-369; INFERRED EventBus library source not read')

e('CurrencyListFragment.onStart', 'CurrencyListFragment.onEvent(CurrencyDeletionConfirmedEvent)', 'REGISTER',
  'onStart registers the fragment on EventBus; EventBus calls the @Subscribe method for CurrencyDeletionConfirmedEvent until onStop unregisters it',
  cls='non_standard', via='EventBus (greenrobot): register(this) at CurrencyListFragment.java:114; @Subscribe at 371 (onEvent(CurrencyDeletionConfirmedEvent)); library dispatch INFERRED',
  evidence='SRC currency/list/CurrencyListFragment.java:110-122 (register at 114, unregister at 121), 371-380; INFERRED EventBus library source not read')

# ---- EventBus posters (ASYNC): each post dispatches to the @Subscribe method

e('CurrencyUIFeatures$3.onClick', 'CurrencyListFragment.onEvent(CurrencyDeletionConfirmedEvent)', 'ASYNC',
  'the user confirms the currency deletion dialog: the listener posts CurrencyDeletionConfirmedEvent and EventBus calls the subscriber',
  gui=['Confirm the currency deletion dialog'],
  cls='non_standard', via='EventBus (greenrobot): post(new CurrencyDeletionConfirmedEvent(...)) at CurrencyUIFeatures.java:123 to the @Subscribe method (library dispatch INFERRED)',
  evidence='SRC currency/CurrencyUIFeatures.java:113-134 (showDialogDeleteCurrency; the listener is $3.onClick), 123 (post); SRC currency/list/CurrencyListFragment.java:371-372 (@Subscribe, decl); INFERRED EventBus library source not read')

e('CurrencyUIFeatures$7.onClick', 'CurrencyListFragment.onEvent(ExchangeRateUpdateConfirmedEvent)', 'ASYNC',
  'the user confirms the exchange rate update: the listener posts ExchangeRateUpdateConfirmedEvent(true) and EventBus calls the subscriber',
  gui=['Confirm the exchange rate update dialog'],
  cls='non_standard', via='EventBus (greenrobot): post(new ExchangeRateUpdateConfirmedEvent(true)) at CurrencyUIFeatures.java:169 to the @Subscribe method (library dispatch INFERRED)',
  evidence='SRC currency/CurrencyUIFeatures.java:159-180 (showDialogUpdateExchangeRates; the listener is $7.onClick), 169 (post); SRC currency/list/CurrencyListFragment.java:360-361 (@Subscribe, decl); INFERRED EventBus library source not read')

e('FixerService.onContentDownloaded', 'CurrencyListFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'a Fixer price download finishes: the service posts PriceDownloadedEvent and EventBus calls the subscriber while the currency list is started',
  env=env_text('a Fixer price download finishes while the currency list is started (registered on EventBus between onStart and onStop)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(new PriceDownloadedEvent(...)) at FixerService.java:120 to the @Subscribe method (library dispatch INFERRED)',
  evidence='SRC investment/prices/FixerService.java:100 (onContentDownloaded), 120 (post); SRC currency/list/CurrencyListFragment.java:354-355 (@Subscribe, decl); INFERRED EventBus library source not read')

e('YqlSecurityPriceUpdaterRetrofit.onContentDownloaded', 'CurrencyListFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'a YQL price download finishes: the updater posts PriceDownloadedEvent and EventBus calls the subscriber while the currency list is started',
  env=env_text('a YQL price download finishes while the currency list is started (registered on EventBus between onStart and onStop)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(new PriceDownloadedEvent(...)) at YqlSecurityPriceUpdaterRetrofit.java:130 to the @Subscribe method (library dispatch INFERRED)',
  evidence='SRC investment/yql/YqlSecurityPriceUpdaterRetrofit.java:113 (onContentDownloaded), 130 (post); SRC currency/list/CurrencyListFragment.java:354-355 (@Subscribe, decl); INFERRED EventBus library source not read')

e('YahooCsvQuoteDownloaderRetrofit.onContentDownloaded', 'CurrencyListFragment.onEvent(PriceDownloadedEvent)', 'ASYNC',
  'a Yahoo CSV price download finishes and parses: the downloader posts PriceDownloadedEvent and EventBus calls the subscriber while the currency list is started',
  env=env_text('a Yahoo CSV price download finishes while the currency list is started (registered on EventBus between onStart and onStop)', ('other',)),
  cls='non_standard', via='EventBus (greenrobot): post(event) at YahooCsvQuoteDownloaderRetrofit.java:124 to the @Subscribe method (library dispatch INFERRED)',
  evidence='SRC investment/yahoocsv/YahooCsvQuoteDownloaderRetrofit.java:103 (onContentDownloaded), 116 (parse), 123-125 (post at 124); SRC currency/list/CurrencyListFragment.java:354-355 (@Subscribe, decl); INFERRED EventBus library source not read')

# ---- user actions on the currency list (GUI from S_CURRENCY_LIST)

gui('S_CURRENCY_LIST', 'CurrencyListActivity.onKeyUp', 'press Back while the currency list is in front',
  evidence='SRC currency/list/CurrencyListActivity.java:69-80 (onKeyUp 70; KEYCODE_BACK 75; setResultAndFinish 76); FW-SRC core/java/android/app/Activity.java:3255-3272 (dispatchKeyEvent passes the key to event.dispatch); FW-SRC core/java/android/view/KeyEvent.java:2709-2715 (ACTION_UP calls receiver.onKeyUp)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onListItemClick', 'tap a currency row in the list',
  evidence='SRC AbsListFragment.java:40-47 (onItemClick calls onListItemClick at 44); SRC currency/list/CurrencyListFragment.java:329-341 (openContextMenu 336; setResultAndFinish 339)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onCreateContextMenu', 'long-press a currency row (the list is registered for the context menu at line 155)',
  evidence='SRC currency/list/CurrencyListFragment.java:155 (registerForContextMenu), 215-229 (onCreateContextMenu); INFERRED View long-press dispatch (android.view.View not read in this batch)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onContextItemSelected', 'tap an item of the row context menu (chart, edit, update rate or delete)',
  evidence='SRC currency/list/CurrencyListFragment.java:231-283 (edit 245; getService and update rate 266; delete dialog 278); label_046.py:14 (the chart item, case 1 at 257-262)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onOptionsItemSelected', 'tap an options menu item (import all currencies, update exchange rates, reload)',
  evidence='SRC currency/list/CurrencyListFragment.java:183-211 (showDialogImportAllCurrencies 189; showDialogUpdateExchangeRates 193; reloadData 206); INFERRED androidx options-menu dispatch (library not read)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onPrepareOptionsMenu', 'open the options menu (the framework prepares it before it is shown)',
  evidence='SRC currency/list/CurrencyListFragment.java:175-181; INFERRED androidx calls onPrepareOptionsMenu before it shows the menu (library not read)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onQueryTextChange', 'type in the search box of the currency list',
  evidence='SRC common/BaseListFragment.java:224-227 (onPreQueryTextChange returns onQueryTextChange at 226); SRC currency/list/CurrencyListFragment.java:287-295 (reloadData 293); INFERRED androidx SearchView calls the listener (not in fw_src)')

gui('S_CURRENCY_LIST', 'CurrencyListFragment.onFloatingActionButtonClicked', 'tap the + button on the currency list',
  evidence='SRC currency/list/CurrencyListFragment.java:323-327 (startCurrencyEditActivity 326); SRC common/BaseListFragment.java:238-248 (FAB listener at 241-246, call at 244); the listener edge to this override is cut in label_026.py:54, so this GUI edge is the route')

# ---- UNREACHABLE: batch 049 methods with no trigger in the app

UNREACHABLE['CurrencyListFragment.initializeSwipeToRefresh'] = (
  'no_trigger_in_app',
  'method with an empty body (lines 494-496). Its only call, at line 105 in onCreateView, is commented out, so no caller exists and no auto CALL record has it as destination',
  'SRC currency/list/CurrencyListFragment.java:103-108 (105 commented out), 494-496 (empty body)',
  'SOURCE')

UNREACHABLE['CurrencyContentObserver.<init>'] = (
  'no_trigger_in_app',
  'the only creator is CurrencyRecyclerListFragment.onCreate (line 93), which is UNREACHABLE (batch 050). The CALL from that method to this constructor is cut in label_050.py:44. auto_calls.json has one CALL record with this constructor as destination, and its source is that UNREACHABLE method, so the constructor never runs',
  'SRC currency/recycler/CurrencyContentObserver.java:35-37; SRC currency/recycler/CurrencyRecyclerListFragment.java:93; label_050.py:44; auto_calls.json (one CALL record with dst CurrencyContentObserver.<init>)',
  'SOURCE')

UNREACHABLE['CurrencyContentObserver.onChange(boolean)'] = (
  'no_trigger_in_app',
  'reached only by the framework ContentObserver dispatch, and that needs a registered instance. The instance is never built (see CurrencyContentObserver.<init> above). Registration sits in CurrencyRecyclerListFragment.onPause (line 137), which is UNREACHABLE. No auto CALL record has this method as destination',
  'SRC currency/recycler/CurrencyContentObserver.java:39-42 (41 is the call to onChange(boolean,Uri)); SRC currency/recycler/CurrencyRecyclerListFragment.java:137; auto_calls.json (no record with dst CurrencyContentObserver.onChange(boolean))',
  'SOURCE')

UNREACHABLE['CurrencyContentObserver.onChange(boolean,Uri)'] = (
  'no_trigger_in_app',
  'the only in-app caller is onChange(boolean) at line 41 (auto CALL record), which is UNREACHABLE. This method never runs. The CALL edge from onChange(boolean) is cut by the sup below',
  'SRC currency/recycler/CurrencyContentObserver.java:41 (the call), 44-50 (the method body; logs only at 49); auto_calls.json CALL record CurrencyContentObserver.onChange(boolean) to onChange(boolean,Uri), line 41',
  'SOURCE')

# sup cut owned by this batch: the caller onChange(boolean) is UNREACHABLE, so its CALL to onChange(boolean,Uri) is cut
sup(('CurrencyContentObserver.onChange(boolean)', 'CurrencyContentObserver.onChange(boolean,Uri)'))  # line 41

# ---- part 052 (2026-10-29)
# ================================================================== batch 052 (label_052): QueryAccountBills (24 methods),
# QueryAllData (2), QueryBillDeposits (3, including <clinit>).
# Result: 26 REACHABLE, 3 UNREACHABLE (see the .md rows). Rows and printed lines: graphs/MMEX/parts/label_052.md.
# This file writes:
#   - no e() edges: every route into these methods is an auto CALL record (auto_calls.json) or a route owned by another batch,
#   - UNREACHABLE entries: getFavoriteAcct and getStatus (no caller), getFilterAccountSelection (the framework never binds
#     the widget RemoteViewsService that calls it; checked against fw_src android-8.1.0_r1, see the reason and the open point),
#   - 4 sup pairs (D14a): auto CALL records whose caller is getFilterAccountSelection, which is UNREACHABLE in this batch.
# getFavoriteAcct and getStatus are getters with no outgoing CALL record, so they have no sup pairs.

UNREACHABLE['QueryAccountBills.getFavoriteAcct'] = ('no_trigger_in_app',
    'no caller: the only occurrence of getFavoriteAcct() in the app source is its definition; auto_calls.json has no CALL record with it as src or dst; the field is written by setFavoriteAcct (called from setValueFromCursor, line 220) and never read',
    'QueryAccountBills.java:141, 220', 'SOURCE')

UNREACHABLE['QueryAccountBills.getStatus'] = ('no_trigger_in_app',
    'no caller: no getStatus() call in the app resolves to QueryAccountBills (the receivers are Account, AccountTransaction, RecurringTransaction, ITransactionEntity and TransactionStatuses; QueryAccountBills extends Dataset and does not implement ITransactionEntity); auto_calls.json has no CALL record with it as dst; the field is written by setStatus (called from setValueFromCursor, line 223) and never read',
    'QueryAccountBills.java:169, 223; MainActivity.java:1271; CalculateRunningBalanceTask2.java:145', 'SOURCE')

UNREACHABLE['QueryAccountBills.getFilterAccountSelection'] = ('framework_never_calls',
    'the only caller is AllAccountBillsViewFactory.onDataSetChanged (line 113), which runs only when the framework binds the widget RemoteViewsService. The host binds it through AppWidgetManager.bindRemoteViewsService (fw_src RemoteViewsAdapter.java:178); AppWidgetServiceImpl.bindRemoteViewsService refuses a service that does not declare BIND_REMOTEVIEWS (fw_src AppWidgetServiceImpl.java:1251, 3608-3611). AccountBillsWidgetService declares BIND_JOB_SERVICE (AndroidManifest.xml:402-403), so the bind throws SecurityException, which RemoteViewsAdapter catches (lines 184-188). onGetViewFactory (AccountBillsWidgetService.java:26-27) and onDataSetChanged therefore never run. Checked against fw_src android-8.1.0_r1 only (see the open point).',
    'QueryAccountBills.java:155; AllAccountBillsViewFactory.java:108-113; AccountBillsWidgetService.java:26-27; AndroidManifest.xml:402-403; fw_src RemoteViewsAdapter.java:178, 184-188; fw_src AppWidgetServiceImpl.java:1251, 3608-3611', 'INFERRED')

# auto CALL records with src = QueryAccountBills.getFilterAccountSelection (auto_calls.json, 4 records): cut by sup because the caller is UNREACHABLE.
sup(('QueryAccountBills.getFilterAccountSelection', 'LookAndFeelSettings.getViewFavouriteAccounts'))
sup(('QueryAccountBills.getFilterAccountSelection', 'LookAndFeelSettings.getViewOpenAccounts'))
sup(('QueryAccountBills.getFilterAccountSelection', 'AppSettings.getLookAndFeelSettings'))
sup(('QueryAccountBills.getFilterAccountSelection', 'AppSettings.<init>'))

# ---- part 056 (2026-10-29)
# ================================================================== batch 056 (label_056): RepositoryBase (16 methods),
# Select (8), SplitCategoriesRepository (7), SplitRecurringCategoriesRepository (8).
# Result: 30 REACHABLE, 9 UNREACHABLE (see the .md rows). Rows and printed lines: graphs/MMEX/parts/label_056.md.
# Every bytecode CALL of this batch is already in auto_calls.json (D7), so this file writes no e() edges and no SCREENS.
# This file writes:
#   - UNREACHABLE entries for the 4 base-class helpers with no caller (add, bulkInsert, bulkUpdate, bulkDelete),
#     query(Class,String), Select.where(String,long[]), the two getAllColumns overrides and the recurring loadSplitCategoriesFor,
#   - 17 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.

# ================================================================== UNREACHABLE: base class and Select

UNREACHABLE['RepositoryBase.add'] = ('no_trigger_in_app',
    'the base add has no caller: PayeeService.createNew calls the PayeeRepository.add override (PayeeService.java:98) and no auto CALL record resolves to RepositoryBase.add; its body only forwards to insert',
    'datalayer/RepositoryBase.java:87-89; servicelayer/PayeeService.java:98', 'SOURCE')

UNREACHABLE['RepositoryBase.bulkDelete'] = ('no_trigger_in_app',
    'protected batch helper with no caller: grep of src/main finds only its definition, and no auto CALL record targets it',
    'datalayer/RepositoryBase.java:234-245', 'SOURCE')

UNREACHABLE['RepositoryBase.bulkInsert'] = ('no_trigger_in_app',
    'protected batch helper with no caller: grep of src/main finds only its definition, and no auto CALL record targets it',
    'datalayer/RepositoryBase.java:149-151', 'SOURCE')

UNREACHABLE['RepositoryBase.bulkUpdate'] = ('no_trigger_in_app',
    'protected batch helper with no caller: grep of src/main finds only its definition, and no auto CALL record targets it',
    'datalayer/RepositoryBase.java:213-224', 'SOURCE')

UNREACHABLE['RepositoryBase.query(Class,String)'] = ('no_trigger_in_app',
    'protected query with a String selection and no caller: both query call sites in src/main (CategoryService.java:118, CurrencyService.java:183) pass a Select and resolve to query(Class,Select); no auto CALL record targets query(Class,String)',
    'datalayer/RepositoryBase.java:168-171; servicelayer/CategoryService.java:116-118; currency/CurrencyService.java:179-183', 'SOURCE')

UNREACHABLE['Select.where(String,long[])'] = ('no_trigger_in_app',
    'the long varargs overload has no caller: no auto CALL record targets it and grep of src/main finds no where call with a long argument',
    'datalayer/Select.java:75-85', 'SOURCE')

# ================================================================== UNREACHABLE: Split repositories

UNREACHABLE['SplitCategoriesRepository.getAllColumns'] = ('no_trigger_in_app',
    'column-list override with no caller: no auto CALL record targets the Split override; the getAllColumns call sites resolve to other classes (for example QueryAccountBills.getAllColumns, HomeFragment.java:243)',
    'datalayer/SplitCategoriesRepository.java:40-49; home/HomeFragment.java:243', 'SOURCE')

UNREACHABLE['SplitRecurringCategoriesRepository.getAllColumns'] = ('no_trigger_in_app',
    'column-list override with no caller: no auto CALL record targets the recurring override; the getAllColumns call sites resolve to other classes',
    'datalayer/SplitRecurringCategoriesRepository.java:40-49', 'SOURCE')

UNREACHABLE['SplitRecurringCategoriesRepository.loadSplitCategoriesFor'] = ('no_trigger_in_app',
    'no caller: the loadSplitCategoriesFor call sites in src/main are on SplitCategoriesRepository only (CheckingTransactionEditActivity.java:399, QifRecord.java:145); no auto CALL record targets the recurring version',
    'datalayer/SplitRecurringCategoriesRepository.java:56-74; transactions/CheckingTransactionEditActivity.java:399; servicelayer/qif/QifRecord.java:145', 'SOURCE')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE here

sup(('RepositoryBase.add', 'RepositoryBase.insert'))
sup(('RepositoryBase.bulkInsert', 'Dataset.getUri'))
sup(('RepositoryBase.bulkInsert', 'RepositoryBase.getContext'))
sup(('RepositoryBase.bulkUpdate', 'MmxContentProvider.<clinit>'))
sup(('RepositoryBase.bulkUpdate', 'MmxContentProvider.getAuthority'))
sup(('RepositoryBase.bulkUpdate', 'RepositoryBase.getContext'))
sup(('RepositoryBase.bulkDelete', 'MmxContentProvider.<clinit>'))
sup(('RepositoryBase.bulkDelete', 'MmxContentProvider.getAuthority'))
sup(('RepositoryBase.bulkDelete', 'RepositoryBase.getContext'))
sup(('RepositoryBase.query(Class,String)', 'RepositoryBase.query(Class,Select)'))
sup(('RepositoryBase.query(Class,String)', 'Select.where(String)'))
sup(('RepositoryBase.query(Class,String)', 'Select.<init>()'))
sup(('SplitRecurringCategoriesRepository.loadSplitCategoriesFor', 'SplitRecurringCategory.<clinit>'))
sup(('SplitRecurringCategoriesRepository.loadSplitCategoriesFor', 'SplitRecurringCategory.loadFromCursor'))
sup(('SplitRecurringCategoriesRepository.loadSplitCategoriesFor', 'SplitRecurringCategory.<init>'))
sup(('SplitRecurringCategoriesRepository.loadSplitCategoriesFor', 'Dataset.getUri'))
sup(('SplitRecurringCategoriesRepository.loadSplitCategoriesFor', 'RepositoryBase.getContext'))

# ---- part 057 (2026-10-29)
# ================================================================== batch 057 (label_057): SqlRepositoryBase (8 methods),
# StockHistoryRepository (14, incl. $UpdateType.<clinit>/<init>), StockHistoryRepositorySql (5),
# StockHistoryRepositorySql_Factory (3).
# Result: 24 REACHABLE, 6 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_057.md).
# No e() edges in this part: every REACHABLE route uses auto_calls.json CALL records (USE_AUTO, D7)
# or edges whose destination belongs to another batch (EventBus posts, the Dagger Lazy hop, the
# PriceEditActivity intent, the settings screens).
# This file writes:
#   - UNREACHABLE entries: StockHistoryRepository.getAllColumns and deleteAutomaticPriceHistory (SOURCE),
#     addStockHistoryRecord(PriceDownloadedEvent) (SOURCE: its only caller is in the never-built EditPriceDialog),
#     and the three generated StockHistoryRepositorySql_Factory methods (INFERRED; grep evidence in label_057.grep.txt, D5),
#   - 5 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.

# ================================================================== UNREACHABLE: source-level dead methods

UNREACHABLE['StockHistoryRepository.getAllColumns'] = ('no_trigger_in_app',
    'no call site has a StockHistoryRepository receiver: every getAllColumns() call in app src is on another class (PortfolioFragment.java:165 StockRepository, WatchlistItemsFragment.java:305 mStockRepository, and the other repositories); no caller of the abstract Dataset.getAllColumns is bound to this class',
    'datalayer/StockHistoryRepository.java:65-74', 'SOURCE')

UNREACHABLE['StockHistoryRepository.deleteAutomaticPriceHistory'] = ('no_trigger_in_app',
    'no caller anywhere in app src: grep for deleteAutomaticPriceHistory finds only its definition; the purge menu calls deleteAllPriceHistory instead (WatchlistFragment.java:264, 622)',
    'datalayer/StockHistoryRepository.java:192-199', 'SOURCE')

UNREACHABLE['StockHistoryRepository.addStockHistoryRecord(PriceDownloadedEvent)'] = ('no_trigger_in_app',
    'the only caller is EditPriceDialog$2.onClick (auto CALL, EditPriceDialog.java:134); EditPriceDialog is never constructed in app src: the only construction is commented out (WatchlistItemsFragment.java:255-261), the other references read its ARG_ constants (PriceEditActivity.java:198-204, WatchlistItemsFragment.java:246-252) or declare its injector (MmxComponent.java:90); no reference in other src/main files (manifest, layouts)',
    'datalayer/StockHistoryRepository.java:76-78', 'SOURCE')

# ================================================================== UNREACHABLE: generated Dagger factory (INFERRED, D16 precedent)

UNREACHABLE['StockHistoryRepositorySql_Factory.create'] = ('no_trigger_in_app',
    'generated by Dagger for the @Inject constructor of StockHistoryRepositorySql (datalayer/StockHistoryRepositorySql.java:45-46); the component binds StockHistoryRepositorySql through the explicit @Provides method RepositoryModule.provideStockHistoryRepository (RepositoryModule.java:38-39, factory RepositoryModule_ProvideStockHistoryRepositoryFactory referenced by DaggerMmxComponent.class); DaggerMmxComponent.class does not reference StockHistoryRepositorySql_Factory and app src has 0 references to it',
    'generated: build/intermediates/javac/debug/classes/com/money/manager/ex/datalayer/StockHistoryRepositorySql_Factory.class', 'INFERRED')

UNREACHABLE['StockHistoryRepositorySql_Factory.get'] = ('no_trigger_in_app',
    'generated Dagger factory get(); the only caller would be the component, which binds the type through RepositoryModule_ProvideStockHistoryRepositoryFactory instead (see create); no auto CALL record has get as dst',
    'generated: build/intermediates/javac/debug/classes/com/money/manager/ex/datalayer/StockHistoryRepositorySql_Factory.class (auto_calls line 21)', 'INFERRED')

UNREACHABLE['StockHistoryRepositorySql_Factory.<init>'] = ('no_trigger_in_app',
    'generated Dagger factory constructor; only reached from create(), which has no caller (see create); no auto CALL record has <init> of the factory as dst from a live caller',
    'generated: build/intermediates/javac/debug/classes/com/money/manager/ex/datalayer/StockHistoryRepositorySql_Factory.class (auto_calls line 25)', 'INFERRED')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE here

sup(('StockHistoryRepository.addStockHistoryRecord(PriceDownloadedEvent)', 'StockHistoryRepository.addStockHistoryRecord(String,Money,Date)'))
sup(('StockHistoryRepository.deleteAutomaticPriceHistory', 'Dataset.getUri'))
sup(('StockHistoryRepository.deleteAutomaticPriceHistory', 'RepositoryBase.getContext'))
sup(('StockHistoryRepositorySql_Factory.create', 'StockHistoryRepositorySql_Factory.<init>'))
sup(('StockHistoryRepositorySql_Factory.get', 'StockHistoryRepositorySql.<init>'))

# ---- part 054 (2026-10-29)
# ================================================================== batch 054 (label_054): AccountRepository (13 methods),
# AccountTransactionRepository (5), AttachmentRepository (7), BudgetEntryRepository (5), BudgetRepository (5), CategoryRepository (5).
# Result: 33 REACHABLE, 7 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_054.md).
# No e() or GUI edges are written here. Every REACHABLE route runs through auto CALL records (auto_calls.json, USE_AUTO) and through
# the ENTRY, INTENT, GUI and EventBus edges that the owning batches write (CheckingTransactionEditActivity, AccountEditActivity,
# BudgetListFragment, HomeFragment, ...). A CALL edge into any owned method would duplicate an auto record (D7), so none is written.
# No SCREENS key is defined: no edge of this batch starts or ends on a page.
# UNREACHABLE: AttachmentRepository.add, delete, load, save, getAllColumns and BudgetEntryRepository.load, getAllColumns.
# Each has no caller in the app source: the two classes are used only through their constructors, loadAttachmentsFor,
# getKeyForCategories and loadForYear, and every getAllColumns() call in app source has a concrete non-target receiver
# (no Dataset or RepositoryBase receiver, so the abstract Dataset.getAllColumns does not dispatch to these overrides).
# Application classes only (no library or generated method), so no label_054.grep.txt is written.
# sup (D14a): the 14 auto CALL records whose caller is one of the UNREACHABLE methods of this batch are cut.

UNREACHABLE['AttachmentRepository.add'] = ('no_trigger_in_app',
    'never called: the only uses of AttachmentRepository in app source are the constructor sites (MmxContentProvider.java:114, CheckingTransactionEditActivity.java:403) and loadAttachmentsFor (line 404)',
    'datalayer/AttachmentRepository.java:51-53; MmxContentProvider.java:114; CheckingTransactionEditActivity.java:403-404', 'SOURCE')

UNREACHABLE['AttachmentRepository.delete'] = ('no_trigger_in_app',
    'never called: no call site of delete(int) in app source; the instance uses above are the constructor and loadAttachmentsFor only',
    'datalayer/AttachmentRepository.java:55-60; MmxContentProvider.java:114; CheckingTransactionEditActivity.java:403-404', 'SOURCE')

UNREACHABLE['AttachmentRepository.getAllColumns'] = ('no_trigger_in_app',
    'its only direct caller is AttachmentRepository.load (line 66), itself UNREACHABLE; no virtual getAllColumns() call reaches this override (every receiver in app source is a concrete non-Attachment type)',
    'datalayer/AttachmentRepository.java:40-49, 62-71; auto_calls.json (AttachmentRepository.load -> AttachmentRepository.getAllColumns, line 66)', 'SOURCE')

UNREACHABLE['AttachmentRepository.load'] = ('no_trigger_in_app',
    'never called: no call site of load(Integer) in app source; loadAttachmentsFor reads the attachments by a query and does not use load',
    'datalayer/AttachmentRepository.java:62-71; CheckingTransactionEditActivity.java:403-404', 'SOURCE')

UNREACHABLE['AttachmentRepository.save'] = ('no_trigger_in_app',
    'never called: no call site of save(Attachment) in app source',
    'datalayer/AttachmentRepository.java:93-96; CheckingTransactionEditActivity.java:403-404', 'SOURCE')

UNREACHABLE['BudgetEntryRepository.getAllColumns'] = ('no_trigger_in_app',
    'no getAllColumns() call on a BudgetEntryRepository or on a Dataset/RepositoryBase receiver in app source; loadForYear builds its own query and no auto_calls.json record targets this method',
    'datalayer/BudgetEntryRepository.java:44; auto_calls.json (no record with this dst)', 'SOURCE')

UNREACHABLE['BudgetEntryRepository.load'] = ('no_trigger_in_app',
    'never called: the class is used only through its constructor (MmxContentProvider.java:108, BudgetAdapter.java:251), the static getKeyForCategories (BudgetAdapter.java:226, 239) and loadForYear (BudgetAdapter.java:252); no load(int) call',
    'datalayer/BudgetEntryRepository.java:52-64; BudgetAdapter.java:226, 239, 251-252; MmxContentProvider.java:108', 'SOURCE')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('AttachmentRepository.add', 'RepositoryBase.insert'),
    ('AttachmentRepository.delete', 'MmxDatabaseUtils.<clinit>'),
    ('AttachmentRepository.delete', 'RepositoryBase.delete'),
    ('AttachmentRepository.delete', 'MmxDatabaseUtils.getArgsForId'),
    ('AttachmentRepository.load', 'MmxDatabaseUtils.<clinit>'),
    ('AttachmentRepository.load', 'RepositoryBase.first'),
    ('AttachmentRepository.load', 'MmxDatabaseUtils.getArgsForId'),
    ('AttachmentRepository.load', 'AttachmentRepository.getAllColumns'),
    ('AttachmentRepository.save', 'RepositoryBase.update(EntityBase,String)'),
    ('AttachmentRepository.save', 'Attachment.getId'),
    ('BudgetEntryRepository.load', 'RepositoryBase.first'),
    ('BudgetEntryRepository.load', 'WhereStatementGenerator.getWhere'),
    ('BudgetEntryRepository.load', 'WhereStatementGenerator.addStatement(String,String,Integer)'),
    ('BudgetEntryRepository.load', 'WhereStatementGenerator.<init>'))

# ---- part 058 (2026-10-29)
# ================================================================== batch 058 (label_058): StockRepository (12 methods),
# StockRepositorySql (6), StockRepositorySql_Factory (3), StockRepository_Factory (3).
# Result: 14 REACHABLE, 10 UNREACHABLE (rows in graphs/MMEX/parts/label_058.md). Generated-class evidence: graphs/MMEX/parts/label_058.grep.txt.
# This file writes only:
#   - UNREACHABLE entries for 4 source methods with no caller (load(Integer[]), loadForSymbols, getEntities, StockRepositorySql.delete),
#   - UNREACHABLE entries for the 6 Dagger-generated factory methods (INFERRED),
#   - 18 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.
# No e() edges: every REACHABLE method already has an auto CALL record into it (auto_calls.json, USE_AUTO), and the Lazy hop
# into StockRepositorySql.<init> is already in graph_def.py (batch 046, line 3675). No ENV_/STATE_ constants, no imports.

# ------------------------------------------------------------------ UNREACHABLE: source methods with no caller

UNREACHABLE['StockRepository.load(Integer[])'] = ('no_trigger_in_app',
    'public, but no caller anywhere: the app loads a stock by an int id (InvestmentTransactionEditActivity.java:107, load(int)) and never by an id array; the auto CALLs out of this method are cut by sup below',
    'StockRepository.java:92 (decl), 95-109 (body); grep of the source root: no caller',
    'SOURCE')

UNREACHABLE['StockRepository.loadForSymbols'] = ('no_trigger_in_app',
    'public, but no caller anywhere (the name occurs only at its declaration, StockRepository.java:114); the auto CALLs out of this method are cut by sup below',
    'StockRepository.java:114 (decl), 117-126 (body); grep of the source root: no caller',
    'SOURCE')

UNREACHABLE['StockRepository.getEntities'] = ('no_trigger_in_app',
    'private helper; its only callers are load(Integer[]) (line 109) and loadForSymbols (line 126), both unreachable above; its auto CALL to Stock.from (line 192) is cut by sup below',
    'StockRepository.java:189 (decl), 192; callers at lines 109 and 126',
    'SOURCE')

UNREACHABLE['StockRepositorySql.delete'] = ('no_trigger_in_app',
    'delete(int) has no caller: no auto_calls record into it and no source call on a StockRepositorySql receiver; it does not override SqlRepositoryBase.delete(String, String...), so the base overload does not reach it; its CALL to SqlRepositoryBase.delete is cut by sup below',
    'StockRepositorySql.java:47-50; SqlRepositoryBase.java:50',
    'SOURCE')

# ------------------------------------------------------------------ UNREACHABLE: Dagger-generated factories (INFERRED; grep evidence in label_058.grep.txt)

UNREACHABLE['StockRepository_Factory.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is StockRepository_Factory.create (auto record, line 25), which has no caller',
    'StockRepository.java:44 (@Inject constructor, the reason Dagger generates the factory); auto_calls StockRepository_Factory.java:25',
    'INFERRED')

UNREACHABLE['StockRepository_Factory.create'] = ('no_trigger_in_app',
    'generated factory method; no auto_calls record into it and no source reference; DaggerMmxComponent.initialize (auto records) calls no StockRepository factory',
    'auto_calls StockRepository_Factory.java:25 (its own CALL, cut by sup); label_058.grep.txt',
    'INFERRED')

UNREACHABLE['StockRepository_Factory.get'] = ('no_trigger_in_app',
    'generated factory method; no caller; its CALL to StockRepository.<init> (line 21) is cut by sup below',
    'auto_calls StockRepository_Factory.java:21; label_058.grep.txt',
    'INFERRED')

UNREACHABLE['StockRepositorySql_Factory.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is StockRepositorySql_Factory.create (auto record, line 25), which has no caller; Dagger uses the RepositoryModule provider for StockRepositorySql instead',
    'StockRepositorySql.java:39 (@Inject constructor, the reason Dagger generates the factory); auto_calls StockRepositorySql_Factory.java:25',
    'INFERRED')

UNREACHABLE['StockRepositorySql_Factory.create'] = ('no_trigger_in_app',
    'generated factory method; no auto_calls record into it and no source reference; DaggerMmxComponent.initialize builds the StockRepositorySql provider with RepositoryModule_ProvideStockRepositoryFactory.create (auto line 196) instead',
    'auto_calls StockRepositorySql_Factory.java:25 (its own CALL, cut by sup); label_058.grep.txt',
    'INFERRED')

UNREACHABLE['StockRepositorySql_Factory.get'] = ('no_trigger_in_app',
    'generated factory method; no caller; its CALL to StockRepositorySql.<init> (line 21) is cut by sup below',
    'auto_calls StockRepositorySql_Factory.java:21; label_058.grep.txt',
    'INFERRED')

# ------------------------------------------------------------------ sup (D14a): auto CALL records whose caller is UNREACHABLE here

sup(
    # load(Integer[]): six callees
    ('StockRepository.load(Integer[])', 'MmxDatabaseUtils.<clinit>'),
    ('StockRepository.load(Integer[])', 'StockRepository.getEntities'),
    ('StockRepository.load(Integer[])', 'RepositoryBase.openCursor(String[],String,String[],String)'),
    ('StockRepository.load(Integer[])', 'MmxDatabaseUtils.makePlaceholders'),
    ('StockRepository.load(Integer[])', 'MmxDatabaseUtils.<init>'),
    ('StockRepository.load(Integer[])', 'RepositoryBase.getContext'),
    # loadForSymbols: the same six callees
    ('StockRepository.loadForSymbols', 'MmxDatabaseUtils.<clinit>'),
    ('StockRepository.loadForSymbols', 'StockRepository.getEntities'),
    ('StockRepository.loadForSymbols', 'RepositoryBase.openCursor(String[],String,String[],String)'),
    ('StockRepository.loadForSymbols', 'MmxDatabaseUtils.makePlaceholders'),
    ('StockRepository.loadForSymbols', 'MmxDatabaseUtils.<init>'),
    ('StockRepository.loadForSymbols', 'RepositoryBase.getContext'),
    # getEntities, StockRepositorySql.delete
    ('StockRepository.getEntities', 'Stock.from'),
    ('StockRepositorySql.delete', 'SqlRepositoryBase.delete'),
    # generated factories
    ('StockRepository_Factory.get', 'StockRepository.<init>'),
    ('StockRepository_Factory.create', 'StockRepository_Factory.<init>'),
    ('StockRepositorySql_Factory.get', 'StockRepositorySql.<init>'),
    ('StockRepositorySql_Factory.create', 'StockRepositorySql_Factory.<init>'),
)

# ---- part 055 (2026-10-29)
# ================================================================== batch 055 (label_055)
# CurrencyRepositorySql (2), CurrencyRepositorySql_Factory (4), InfoRepositorySql (5), InfoRepositorySql_Factory (3),
# PayeeRepository (6), QueryAllDataRepository (4), RecurringTransactionRepository (7). 31 methods.
# Result: 28 REACHABLE, 3 UNREACHABLE (see the .md rows). Rows and printed lines: graphs/MMEX/parts/label_055.md.
# Auto CALL records (auto_calls.json) are not rewritten here (D7). This file writes:
#   - 4 non_standard CALL edges for the Dagger Provider and Lazy hops into the generated factories
#     (these get() calls are not source calls, so auto_calls.json has no record for them),
#   - 3 UNREACHABLE entries (app source, no caller anywhere in src/main),
#   - 1 sup pair (D14a): the auto CALL from the UNREACHABLE QueryAllDataRepository.add.
# Open point: CurrencyService_Factory.get is batch 047's; label_047.py:40 says UNREACHABLE, but the bytecode shows
# FormatUtilities_Factory.get -> CurrencyService_Factory.get (offset 25). The edge belongs to batch 047 (D1: owner by destination).

# ================================================================== CurrencyRepositorySql_Factory.get: Provider hop

e('CurrencyService_Factory.get', 'CurrencyRepositorySql_Factory.get', 'CALL',
  'CurrencyService_Factory.get calls its repository Provider (mRepositoryProvider.get); the Provider is the CurrencyRepositorySql_Factory instance built in DaggerMmxComponent.initialize',
  evidence='INFERRED app/build/intermediates/javac/debug/classes/com/money/manager/ex/currency/CurrencyService_Factory.class: get offset 8 contextProvider.get, offset 25 mRepositoryProvider.get (invokeinterface Provider.get), offset 33 injectMRepository; core/ioc/DaggerMmxComponent.class initialize offset 86 (CurrencyRepositorySql_Factory.create), 89 putfield, 98 getfield (passed to CurrencyService_Factory.create)',
  cls='non_standard',
  via='javax.inject.Provider mRepositoryProvider (generated field), whose runtime class is CurrencyRepositorySql_Factory')

# ================================================================== InfoRepositorySql_Factory.get: Lazy hops

e('MmxDatabaseUtils.fixDuplicates', 'InfoRepositorySql_Factory.get', 'CALL',
  'fixDuplicates calls infoRepositorySqlLazy.get() (line 158); the Lazy wraps the InfoRepositorySql_Factory Provider, so get() runs the factory get before loadAll and delete',
  evidence='SRC utils/MmxDatabaseUtils.java:102 (@Inject Lazy field), 158 (get), 159 (loadAll), 169 (delete); GEN core/ioc/DaggerMmxComponent.class injectMmxDatabaseUtils offset 24 getfield infoRepositorySqlProvider, 27 DoubleCheck.lazy, 30 MembersInjector.injectInfoRepositorySqlLazy',
  cls='non_standard',
  via='dagger.internal.DoubleCheck (the Lazy), then javax.inject.Provider.get on InfoRepositorySql_Factory')

e('Passcode.savePasscode', 'InfoRepositorySql_Factory.get', 'CALL',
  'savePasscode calls infoRepositorySqlLazy.get() (line 158) before insert or update; savePasscode is reached from setPasscode (line 80)',
  evidence='SRC Passcode.java:47 (@Inject Lazy field), 78-80 (setPasscode calls savePasscode), 153-158 (savePasscode, get at 158); GEN core/ioc/DaggerMmxComponent.class injectPasscode offset 2 getfield infoRepositorySqlProvider, 5 DoubleCheck.lazy, 8 MembersInjector.injectInfoRepositorySqlLazy',
  cls='non_standard',
  via='dagger.internal.DoubleCheck (the Lazy), then javax.inject.Provider.get on InfoRepositorySql_Factory')

e('Passcode.clearPasscode_Internal', 'InfoRepositorySql_Factory.get', 'CALL',
  'clearPasscode_Internal calls infoRepositorySqlLazy.get() (line 136) before the delete; reached from clearPasscode (line 85)',
  evidence='SRC Passcode.java:83-85 (clearPasscode calls clearPasscode_Internal), 135-136 (get at 136), 137 onward (repo.delete with Info.INFONAME); GEN core/ioc/DaggerMmxComponent.class injectPasscode offsets 2-8 (same Lazy wiring as above)',
  cls='non_standard',
  via='dagger.internal.DoubleCheck (the Lazy), then javax.inject.Provider.get on InfoRepositorySql_Factory')

# ================================================================== UNREACHABLE: app source with no caller

UNREACHABLE['QueryAllDataRepository.add'] = ('no_trigger_in_app',
    'no caller: QueryAllDataRepository is constructed in one place (CalculateRunningBalanceTask2.java:182) and only query() is called on it; add(AccountTransactionDisplay) is a plain method that calls insert(entity.contentValues), not an override, and no auto CALL record names it',
    'datalayer/QueryAllDataRepository.java:55-57; account/CalculateRunningBalanceTask2.java:182-183; grep of src/main: QueryAllDataRepository appears in 2 files only', 'SOURCE')

UNREACHABLE['QueryAllDataRepository.getAllColumns'] = ('no_trigger_in_app',
    'no caller: the override is reached only by a getAllColumns() call whose receiver is QueryAllDataRepository, and there is none (the getAllColumns() call sites in src/main have other receiver types, e.g. QueryAllData at AllDataListFragment.java:243); no CHA or exact auto record names it',
    'datalayer/QueryAllDataRepository.java:40-53; common/AllDataListFragment.java:243; account/CalculateRunningBalanceTask2.java:182-183', 'SOURCE')

UNREACHABLE['RecurringTransactionRepository.getAllColumns'] = ('no_trigger_in_app',
    'no caller: RecurringTransactionRepository is used only for constructor, load, first, insert, update and delete in its call sites (MmxContentProvider, MainActivity, RecurringTransactionService, CheckingTransactionEditActivity, RecurringTransactionEditActivity, RecurringTransactionListFragment); the only getAllColumns() call near them is on QueryBillDeposits (RecurringTransactionListFragment.java:224); no CHA or exact auto record names it',
    'datalayer/RecurringTransactionRepository.java:39-57; recurring/transactions/RecurringTransactionListFragment.java:224', 'SOURCE')

# ================================================================== sup (D14a): auto CALL whose caller is UNREACHABLE here

sup(('QueryAllDataRepository.add', 'RepositoryBase.insert'))

# ---- part 060 (2026-10-29)
# ================================================================== batch 060 (label_060): Account$$Parcelable.writeToParcel,
# Account$$Parcelable$1.<init>, Account$$Parcelable$1.createFromParcel, Account$$Parcelable$1.newArray (Account methods 41-44 of 44).
# Result: 3 REACHABLE, 1 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_060.md). The generated class is not in the source root;
# its methods were read from the build class files (constant-pool strings, INFERRED). Grep evidence: graphs/MMEX/parts/label_060.grep.txt.
# Edges written here: the two parcel round trips of the AccountEditActivity saved state (the save in onSaveInstanceState,
# the restore in restoreInstanceState). The Parceler library is not read, so the wrap and unwrap hops are INFERRED.
# $1.<init> is REACHABLE only through the auto CALL record Account$$Parcelable.<clinit> -> Account$$Parcelable$1.<init>
# (auto_calls.json:24976-24978); <clinit> belongs to batch 059 (open point in label_060.md).
# No CALL edge is written (D7): every CALL into an owned method here is an auto record.
# No sup pairs (D14a): no auto CALL record starts in newArray (none does), and no UNREACHABLE method of this batch has an auto record.

# ---- saved state: AccountEditActivity.onSaveInstanceState wraps mAccount and the framework parcels the bundle (AccountEditActivity.java:204)

e('AccountEditActivity.onSaveInstanceState', 'Account$$Parcelable.writeToParcel', 'FRAMEWORK',
  'Parcels.wrap(mAccount) puts an Account wrapper in the saved-state bundle; when the framework saves the state, the bundle is parcelled and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard', via='outState.putParcelable(KEY_ACCOUNT_ENTITY, Parcels.wrap(mAccount)) at AccountEditActivity.java:204; the framework parcels the saved-state bundle (Bundle.writeToParcel, FW-SRC Bundle.java:1229, sent by ActivityThread activityStopped, FW-SRC ActivityThread.java:3930-3935); Parcel.writeValue calls writeParcelable (FW-SRC Parcel.java:1785-1791), which calls p.writeToParcel (FW-SRC Parcel.java:1791). Parcels.wrap returns the generated wrapper (parceler library not read, INFERRED)',
  evidence='SRC account/AccountEditActivity.java:196-209 (line 204); FW-SRC core/java/android/os/Parcel.java:1785-1791; FW-SRC core/java/android/os/Bundle.java:1229; FW-SRC core/java/android/app/ActivityThread.java:3930-3935; label_060.grep.txt block A; INFERRED parceler library not read')

# ---- saved state: AccountEditActivity.restoreInstanceState unwraps the saved Account (AccountEditActivity.java:587)

e('AccountEditActivity.restoreInstanceState', 'Account$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle holds the Account wrapper; the first getParcelable unparcels the bundle, and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='the activity is recreated from a saved state: onCreate calls restoreInstanceState (line 103) only when savedInstanceState is not null (line 102)',
  cls='non_standard', via='savedInstanceState.getParcelable(KEY_ACCOUNT_ENTITY) at AccountEditActivity.java:587 calls unparcel (FW-SRC core/java/android/os/Bundle.java:938-939); Parcel.readValue calls readParcelable (FW-SRC Parcel.java:2744-2745, 2841-2851), which reads the CREATOR field (FW-SRC Parcel.java:2894) and calls creator.createFromParcel (FW-SRC Parcel.java:2851)',
  evidence='SRC account/AccountEditActivity.java:102-103, 586-599 (line 587); FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2744-2745, 2841-2851, 2894; label_060.grep.txt block A')

# ================================================================== UNREACHABLE: the typed-array creator (no typed array of Account wrappers is parcelled)

UNREACHABLE['Account$$Parcelable$1.newArray'] = ('framework_never_calls',
  'CREATOR typed-array method. The framework calls it only from Parcel.createTypedArray(Creator) (FW-SRC Parcel.java:2640-2645, c.newArray(N) at 2645), that is, when app code reads a typed array of Account wrappers with this creator. No app code builds or reads such an array: the Account arrays and lists in the source root are declarations and service return values, none parcelled (label_060.grep.txt blocks B and C), and no app code names Account$$Parcelable.CREATOR (block D, empty). No auto_calls.json record has newArray as dst or $1.newArray as src. The Parceler library is not read: whether it calls newArray itself is INFERRED',
  'FW-SRC core/java/android/os/Parcel.java:2640-2645; label_060.grep.txt blocks B, C, D; generated class not in the source root (build class file: newArray descriptor (I)[Lcom/money/manager/ex/domainmodel/Account$$Parcelable;, label_060.grep.txt constant-pool block)',
  'INFERRED')

# ---- part 059 (2026-10-29)
# ================================================================== batch 059 (label_059): Account (34 methods) and
# Account$$Parcelable (6 methods: <clinit>, <init>, describeContents, getParcel, read, write).
# Result: 38 REACHABLE, 2 UNREACHABLE (Account.getType SOURCE; Account$$Parcelable.describeContents INFERRED).
# Rows and printed lines: graphs/MMEX/parts/label_059.md. Grep evidence for the generated UNREACHABLE row: graphs/MMEX/parts/label_059.grep.txt.
# The class is domainmodel/Account (the brief named ex/Account; the batch file and source use domainmodel).
# Most Account routes are the auto CALL records from AccountEditActivity and are not rewritten here (D7).
# This file writes:
#   - two library CALL edges from WatchlistFragment.onSaveInstanceState (Parcels.wrap, INFERRED) and one from
#     WatchlistFragment.onCreate (Parcels.unwrap, INFERRED); they reach the generated wrapper Account$$Parcelable,
#   - UNREACHABLE entries for Account.getType (no caller) and Account$$Parcelable.describeContents (framework never calls it),
#   - 3 sup pairs (D14a): the auto CALL records from the UNREACHABLE Account.getType (Account.java:120, 121).
# Interim (D8): Account$$Parcelable.read and write are reached through Account$$Parcelable$1.createFromParcel and
# Account$$Parcelable.writeToParcel, which are in batch 060; WatchlistFragment is in a batch that is not merged yet.

e('WatchlistFragment.onSaveInstanceState', 'Account$$Parcelable.<clinit>', 'CALL',
  'the watchlist fragment is saved: onSaveInstanceState puts Parcels.wrap(mAccount) into the state, the library creates the generated wrapper, and the first use of the class runs its static initializer',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): creates Account$$Parcelable, which initialises the class',
  evidence='SRC investment/watchlist/WatchlistFragment.java:276-281 (putParcelable of Parcels.wrap at 280); generated Account$$Parcelable.java is not in the tree: auto_calls.json record <clinit> -> Account$$Parcelable$1.<init> at Account$$Parcelable.java:23')

e('WatchlistFragment.onSaveInstanceState', 'Account$$Parcelable.<init>', 'CALL',
  'the same save path: Parcels.wrap calls the wrapper constructor with the Account (the restore path is the other caller, createFromParcel -> <init> at Account$$Parcelable.java:28, batch 060)',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): new Account$$Parcelable(Account)',
  evidence='SRC investment/watchlist/WatchlistFragment.java:280; generated Account$$Parcelable.java not in the tree: auto_calls.json record Account$$Parcelable$1.createFromParcel -> Account$$Parcelable.<init> at Account$$Parcelable.java:28')

e('WatchlistFragment.onCreate', 'Account$$Parcelable.getParcel', 'CALL',
  'the watchlist fragment is restored with a saved state (savedInstanceState non-null, line 120): Parcels.unwrap casts the wrapper and calls getParcel to get the Account',
  cls='non_standard',
  via='org.parceler.Parcels.unwrap (library, not read; INFERRED): calls getParcel on the ParcelWrapper',
  evidence='SRC investment/watchlist/WatchlistFragment.java:120-121 (condition at 120, Parcels.unwrap at 121)')

UNREACHABLE['Account.getType'] = ('no_trigger_in_app',
    'no app code calls Account.getType: the getType() call sites in app source are Dataset.getType (MmxContentProvider.java:161, 204, 242, 397, 433), NetworkInfo.getType (NetworkUtils.java:66) and the Gson TypeToken getType (RecentDatabasesProvider.java:208); auto_calls.json has no record into Account.getType; its three outgoing auto CALL records (Account.java:120, 121) are cut by the sup below (D14a)',
    'Account.java:119-122; MmxContentProvider.java:161; NetworkUtils.java:66; label_059.grep.txt section 5', 'SOURCE')

UNREACHABLE['Account$$Parcelable.describeContents'] = ('framework_never_calls',
    'the generated describeContents returns 0 and no app code calls describeContents or hasFileDescriptors (grep: definitions only); the framework calls it only in the unparcelled-map walk of Bundle.hasFileDescriptors (Bundle.java:316-362, calls at 329, 338, 349, 362), which Bundle.describeContents (1217) and Intent.describeContents (Intent.java:9553) reach, and Intent.describeContents has no caller in core/java or services/core/java; the system_server callers (AMS.java:4652, 4797, 5030, 7453, 7588) hold parcelled bundles and intents, so the walk does not run on this class there (INFERRED)',
    'Bundle.java:316-362; Bundle.java:1208-1220; Intent.java:9553; AMS.java:7453; label_059.grep.txt sections 1-4', 'INFERRED')

sup(('Account.getType', 'Account.getTypeName'),
    ('Account.getType', 'AccountTypes.<clinit>'),
    ('Account.getType', 'AccountTypes.get'))

# ---- part 061 (2026-10-29)
# ================================================================== batch 061 (label_061): AccountTransaction (38 methods),
# AccountTransaction$$Parcelable.<clinit> and <init> (2 generated methods; the .java is not in the source root).
# Result: 38 REACHABLE, 2 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_061.md; grep evidence: graphs/MMEX/parts/label_061.grep.txt).
# No e() or GUI edges are written here (D7): every REACHABLE route runs through auto CALL records (auto_calls.json) from route nodes
# owned by other batches: CheckingTransactionEditActivity (onCreate, handleIntent, loadTransaction, saveData, saveTransaction,
# onSaveInstanceState, restoreInstanceState), EditTransactionCommonFunctions (initializeInputControls callees, validateData, the TextWatchers),
# MainActivity.populateScheduledTransactions, AccountTransactionRepository (load, insert, update) and RepositoryBase (first, query).
# The two Parcelable methods are entered by the auto CALL from AccountTransaction$$Parcelable$1.createFromParcel (batch 062) at
# AccountTransaction$$Parcelable.java:28; the FRAMEWORK edge into that creator belongs to batch 062 (D1).
# UNREACHABLE: AccountTransaction.<init>(ContentValues) and AccountTransaction.getFollowUpId (no caller, no bytecode reference).
# sup (D14a): the 2 auto CALL records whose caller is UNREACHABLE in this batch are cut (both match auto_calls.json).

# ================================================================== UNREACHABLE

UNREACHABLE['AccountTransaction.<init>(ContentValues)'] = ('no_trigger_in_app',
    'no caller. The only construction in app source is the no-argument new AccountTransaction() at AccountTransaction.java:57. RepositoryBase.first and RepositoryBase.query build entities with resultType.newInstance() (RepositoryBase.java:109, 134), which calls the no-argument constructor. No other build class both names AccountTransaction and holds the (Landroid/content/ContentValues;)V descriptor (grep evidence in label_061.grep.txt). No auto_calls.json record has this dst. Its one outgoing auto CALL (line 79, EntityBase.<init>(ContentValues)) is cut by sup below',
    'AccountTransaction.java:57, 78-80; RepositoryBase.java:109, 134', 'SOURCE')

UNREACHABLE['AccountTransaction.getFollowUpId'] = ('no_trigger_in_app',
    'no caller. The only mentions in app source are the getter declaration (line 179) and the call setFollowUpId(Constants.NOT_SET) in the no-argument constructor (line 75, a setter call). No auto_calls.json record has this dst, no build class other than AccountTransaction.class names getFollowUpId, and the generated wrapper does not reference it (grep evidence in label_061.grep.txt). Its one outgoing auto CALL (line 180, EntityBase.getInt) is cut by sup below',
    'AccountTransaction.java:75, 179-181', 'SOURCE')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('AccountTransaction.<init>(ContentValues)', 'EntityBase.<init>(ContentValues)'),
    ('AccountTransaction.getFollowUpId', 'EntityBase.getInt'))

# ---- part 062 (2026-10-29)
# ================================================================== batch 062 (label_062): AccountTransaction$$Parcelable.describeContents,
# getParcel, read, write, writeToParcel, AccountTransaction$$Parcelable$1.<init>, createFromParcel, newArray (AccountTransaction methods 41-48 of 48).
# Result: 6 REACHABLE, 2 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_062.md). The generated classes are not in the source root;
# their methods were read from the build class files (constant-pool strings, INFERRED). Grep evidence: graphs/MMEX/parts/label_062.grep.txt.
# Edges written here: the two parcel round trips of the CheckingTransactionEditActivity saved state (save in onSaveInstanceState,
# restore in restoreInstanceState). The Parceler library is not read, so the wrap and unwrap hops are INFERRED.
# read, write and $1.<init> are REACHABLE through auto CALL records (auto_calls.json); $1.<init> is called by <clinit>, which belongs to batch 061.
# No CALL edge is written (D7): every bytecode CALL into an owned method here is an auto record.
# No sup pairs (D14a): no auto CALL record starts in describeContents or newArray.

# ---- saved state: CheckingTransactionEditActivity.onSaveInstanceState wraps the transaction and the framework parcels the bundle (line 167)

e('CheckingTransactionEditActivity.onSaveInstanceState', 'AccountTransaction$$Parcelable.writeToParcel', 'FRAMEWORK',
  'Parcels.wrap(mCommon.transactionEntity) puts an AccountTransaction wrapper in the saved-state bundle; when the framework saves the state, the bundle is parcelled and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard', via='outState.putParcelable(KEY_TRANSACTION_ENTITY, Parcels.wrap(mCommon.transactionEntity)) at transactions/CheckingTransactionEditActivity.java:166-167; the framework parcels the saved-state bundle (Bundle.writeToParcel, FW-SRC core/java/android/os/Bundle.java:1229, sent by ActivityThread activityStopped, FW-SRC core/java/android/app/ActivityThread.java:3930-3935); Parcel.writeParcelable calls p.writeToParcel (FW-SRC core/java/android/os/Parcel.java:1785-1791). Parcels.wrap returns the generated wrapper (parceler library not read, INFERRED)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:162-167, 390-395, 776 (runtime type AccountTransaction); FW-SRC core/java/android/os/Parcel.java:1785-1791; FW-SRC core/java/android/os/Bundle.java:1229; FW-SRC core/java/android/app/ActivityThread.java:3930-3935; label_062.grep.txt blocks A and F; INFERRED parceler library not read')

# ---- saved state: CheckingTransactionEditActivity.restoreInstanceState unparcels the saved transaction (line 648) and unwraps it (line 649)

e('CheckingTransactionEditActivity.restoreInstanceState', 'AccountTransaction$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle holds the AccountTransaction wrapper; the first getParcelable unparcels the bundle, and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='the restore runs only when onCreate gets a saved bundle: onCreate calls restoreInstanceState (line 107) only when savedInstanceState is not null (line 106)',
  cls='non_standard', via='savedInstanceState.getParcelable(KEY_TRANSACTION_ENTITY) at transactions/CheckingTransactionEditActivity.java:648 calls unparcel (FW-SRC core/java/android/os/Bundle.java:938-939); Parcel.readParcelable reads the CREATOR field (FW-SRC core/java/android/os/Parcel.java:2894) and calls creator.createFromParcel (FW-SRC core/java/android/os/Parcel.java:2841-2851)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:106-107, 647-649; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_062.grep.txt blocks A and F; INFERRED parceler library not read')

e('CheckingTransactionEditActivity.restoreInstanceState', 'AccountTransaction$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the wrapper read from the saved bundle and returns the AccountTransaction',
  guard='the same guard as the createFromParcel edge: restoreInstanceState runs only when onCreate gets a saved bundle (lines 106-107)',
  cls='non_standard', via='Parcels.unwrap(parcelTx) at transactions/CheckingTransactionEditActivity.java:649 (parceler library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:106-107, 647-649; label_062.grep.txt blocks A and F; INFERRED parceler library not read')

# ================================================================== UNREACHABLE: describeContents and the typed-array creator

UNREACHABLE['AccountTransaction$$Parcelable.describeContents'] = ('framework_never_calls',
  'generated describeContents returns 0. No app code calls describeContents (label_062.grep.txt block C, empty). The framework reaches it only through Bundle.hasFileDescriptors walking an unparcelled map (Bundle.java:324-336) and Bundle.describeContents (Bundle.java:1215-1218). The saved-state bundle is checked in ActivityManagerService.activityStopped (line 7453) after binder parcelling, when mParcelledData is set, so that check does not call describeContents on the wrapper (INFERRED: the binder and ActivityThread marshalling path is not read). No auto record names it',
  'FW-SRC core/java/android/os/Bundle.java:316-336, 1215-1218; FW-SRC services/core/java/com/android/server/am/ActivityManagerService.java:7447-7453; label_062.grep.txt blocks C and G',
  'INFERRED')

UNREACHABLE['AccountTransaction$$Parcelable$1.newArray'] = ('framework_never_calls',
  'CREATOR typed-array method. The framework calls it only from Parcel.createTypedArray(Creator) (FW-SRC core/java/android/os/Parcel.java:2640-2645, c.newArray(N) at 2645), that is, when app code reads a typed array of AccountTransaction wrappers. No app code does: the source root has no createTypedArray, writeTypedArray or CREATOR reference, and its newArray implementations are DefinedDateRange, CategorySub and ValuePieEntry only (label_062.grep.txt block B). No auto_calls.json record has newArray as dst or $1.newArray as src. Whether the Parceler library calls newArray is INFERRED (library not read)',
  'FW-SRC core/java/android/os/Parcel.java:2640-2645; label_062.grep.txt blocks B and E; generated class not in the source root (build class file descriptor (I)[Lcom/money/manager/ex/domainmodel/AccountTransaction$$Parcelable;, block E)',
  'INFERRED')

# ---- part 063 (2026-10-29)
# ================================================================== batch 063 (label_063): Attachment (10 methods), Budget (5),
# Budget$$Parcelable (7), Budget$$Parcelable$1 (3), BudgetEntry.<init> (1).
# Result: 9 REACHABLE, 17 UNREACHABLE (rows: graphs/MMEX/parts/label_063.md).
# No e() edges and no SCREENS: every REACHABLE route is an auto CALL record (auto_calls.json) whose caller is reached in another batch.
# This file writes:
#   - UNREACHABLE entries for Attachment.<init>(ContentValues), the Attachment getters and setters with no caller, and the generated Parceler family,
#   - 13 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.
# The generated family is evidenced in graphs/MMEX/parts/label_063.grep.txt (D5, INFERRED).

# ================================================================== Attachment: UNREACHABLE (source evidence)

UNREACHABLE['Attachment.<init>(ContentValues)'] = ('no_trigger_in_app',
    'no source caller: the only "new Attachment(" in app source is the no-arg call at AttachmentRepository.java:83; RepositoryBase and SqlRepositoryBase create entities with newInstance(), which calls only the no-arg constructor',
    'Attachment.java:39-41; AttachmentRepository.java:83; RepositoryBase.java:109, 134; SqlRepositoryBase.java:84', 'SOURCE')

UNREACHABLE['Attachment.getId'] = ('no_trigger_in_app',
    'its only caller is AttachmentRepository.save (auto CALL line 94), and save is UNREACHABLE in batch 054 (no save call on an AttachmentRepository in app source); the cut of save -> getId is owned by batch 054 (label_054.py line 54)',
    'Attachment.java:43-45; AttachmentRepository.java:93-96; parts/label_054.py:54', 'SOURCE')

UNREACHABLE['Attachment.getRefId'] = ('no_trigger_in_app',
    'no caller: getRefId appears only at its definition in app source (label_063.grep.txt section 5)',
    'Attachment.java:59-61; label_063.grep.txt section 5', 'SOURCE')

UNREACHABLE['Attachment.setFilename'] = ('no_trigger_in_app',
    'no caller: setFilename appears only at its definition in app source (label_063.grep.txt section 5)',
    'Attachment.java:55-57; label_063.grep.txt section 5', 'SOURCE')

UNREACHABLE['Attachment.setId'] = ('no_trigger_in_app',
    'no caller on an Attachment: the setId call sites in app source are on other types (Account, Category, Budget, Payee, split and transaction classes); Attachment extends EntityBase and implements no interface with setId',
    'Attachment.java:26-27, 47-49; label_063.grep.txt section 5', 'SOURCE')

UNREACHABLE['Attachment.setRefId'] = ('no_trigger_in_app',
    'no caller: setRefId appears only at its definition in app source (label_063.grep.txt section 5)',
    'Attachment.java:63-65; label_063.grep.txt section 5', 'SOURCE')

UNREACHABLE['Attachment.setRefType'] = ('no_trigger_in_app',
    'no caller: setRefType appears only at its definition in app source (label_063.grep.txt section 5)',
    'Attachment.java:71-73; label_063.grep.txt section 5', 'SOURCE')

# ================================================================== Budget$$Parcelable and $1: UNREACHABLE (generated by Parceler, INFERRED)
# No entry route: Parcels.wrap and unwrap never receive a Budget (label_063.grep.txt section 3), no other @Parcel class has a Budget field
# (section 4), and no class file names Budget$$Parcelable except the two generated classes themselves (section 1). Parceler is a library, not read: INFERRED.

UNREACHABLE['Budget$$Parcelable.<clinit>'] = ('no_trigger_in_app',
    'static initialiser of the generated class: it runs only when the class is first loaded, which needs a Parcels.wrap or unwrap naming Budget (none) or a class file naming the generated class (none)',
    'Budget.java:26; label_063.grep.txt sections 1, 3, 4; auto_calls.json (Budget$$Parcelable.<clinit> -> Budget$$Parcelable$1.<init>, generated line 23)', 'INFERRED')

UNREACHABLE['Budget$$Parcelable.<init>'] = ('no_trigger_in_app',
    'generated constructor: its only caller is Budget$$Parcelable$1.createFromParcel (auto CALL line 28), which is itself UNREACHABLE; the family is never instantiated',
    'auto_calls.json (Budget$$Parcelable$1.createFromParcel -> Budget$$Parcelable.<init>, generated line 28); label_063.grep.txt sections 1, 3', 'INFERRED')

UNREACHABLE['Budget$$Parcelable.describeContents'] = ('no_trigger_in_app',
    'Parcelable method that the framework calls only on a Budget$$Parcelable instance; no such instance is created, and no call record targets it',
    'Budget.java:26; label_063.grep.txt sections 1, 3, 4', 'INFERRED')

UNREACHABLE['Budget$$Parcelable.getParcel'] = ('no_trigger_in_app',
    'generated helper that wraps the Budget; no call record targets it, and no Budget$$Parcelable instance is created',
    'label_063.grep.txt sections 1, 3; auto_calls.json (no record with this dst)', 'INFERRED')

UNREACHABLE['Budget$$Parcelable.read'] = ('no_trigger_in_app',
    'called only by Budget$$Parcelable$1.createFromParcel (auto CALL line 28), which is UNREACHABLE; its auto CALL to Budget.<init> (line 78) is cut by sup below',
    'auto_calls.json (Budget$$Parcelable$1.createFromParcel -> Budget$$Parcelable.read, generated line 28; Budget$$Parcelable.read -> Budget.<init>, line 78)', 'INFERRED')

UNREACHABLE['Budget$$Parcelable.write'] = ('no_trigger_in_app',
    'called only by Budget$$Parcelable.writeToParcel (auto CALL line 45), which is UNREACHABLE',
    'auto_calls.json (Budget$$Parcelable.writeToParcel -> Budget$$Parcelable.write, generated line 45)', 'INFERRED')

UNREACHABLE['Budget$$Parcelable.writeToParcel'] = ('no_trigger_in_app',
    'Parcelable callback that the framework calls only on a Budget$$Parcelable instance, which is never created (no Parcels.wrap of Budget); its auto CALL to write is cut by sup below',
    'label_063.grep.txt sections 1, 3; auto_calls.json (generated line 45)', 'INFERRED')

UNREACHABLE['Budget$$Parcelable$1.<init>'] = ('no_trigger_in_app',
    'CREATOR constructor: its only caller is Budget$$Parcelable.<clinit> (auto CALL line 23), which is UNREACHABLE',
    'auto_calls.json (Budget$$Parcelable.<clinit> -> Budget$$Parcelable$1.<init>, generated line 23)', 'INFERRED')

UNREACHABLE['Budget$$Parcelable$1.createFromParcel'] = ('no_trigger_in_app',
    'CREATOR callback: the framework calls it only when a Budget$$Parcelable name is read from a parcel, which needs a Budget parcel (none is written); its auto CALLs to <clinit>, <init> and read (line 28) are cut by sup below',
    'auto_calls.json (generated line 28, three records); label_063.grep.txt sections 1, 3', 'INFERRED')

UNREACHABLE['Budget$$Parcelable$1.newArray'] = ('no_trigger_in_app',
    'CREATOR array factory: the framework calls it only when an array of Budget$$Parcelable is read, and none is written; no call record targets it',
    'label_063.grep.txt sections 1, 3; auto_calls.json (no record with this dst)', 'INFERRED')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('Attachment.<init>(ContentValues)', 'EntityBase.<init>(ContentValues)'))
sup(('Attachment.getId', 'EntityBase.getInt'))
sup(('Attachment.getRefId', 'EntityBase.getInt'))
sup(('Attachment.setFilename', 'EntityBase.setString'))
sup(('Attachment.setId', 'EntityBase.setInt'))
sup(('Attachment.setRefId', 'EntityBase.setInt'))
sup(('Attachment.setRefType', 'EntityBase.setString'))
sup(('Budget$$Parcelable.writeToParcel', 'Budget$$Parcelable.write'))
sup(('Budget$$Parcelable.read', 'Budget.<init>'))
sup(('Budget$$Parcelable.<clinit>', 'Budget$$Parcelable$1.<init>'))
sup(('Budget$$Parcelable$1.createFromParcel', 'Budget$$Parcelable.<clinit>'))
sup(('Budget$$Parcelable$1.createFromParcel', 'Budget$$Parcelable.<init>'))
sup(('Budget$$Parcelable$1.createFromParcel', 'Budget$$Parcelable.read'))

# ---- part 064 (2026-10-29)
# ================================================================== batch 064 (label_064): Category (8 methods),
# Category$$Parcelable (7), Category$$Parcelable$1 (3). 18 methods in total.
# Result: 6 REACHABLE, 12 UNREACHABLE (see the .md rows). Rows and printed lines: graphs/MMEX/parts/label_064.md.
# Evidence for the generated and library rows: graphs/MMEX/parts/label_064.grep.txt.
# Auto CALL records (auto_calls.json) are not rewritten here. This file writes:
#   - UNREACHABLE entries for Category.<init>(ContentValues) and Category.setParentId (SOURCE),
#     and for the ten Category$$Parcelable and Category$$Parcelable$1 methods (INFERRED, generated code),
#   - 8 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.
# No e() edges: the REACHABLE methods are reached by auto CALL records (D7). No SCREENS entry: the pages used
# (S_CATEGORY_LIST, S_BUDGET_DETAIL) are defined by batches 015, 016 and 029.

# ================================================================== UNREACHABLE: Category (source)

UNREACHABLE['Category.<init>(ContentValues)'] = ('no_trigger_in_app',
    'no caller: the only construction in src/main is new Category() (no-arg, CategoryListFragment.java:399); the class scan finds 0 invokes of this constructor; RepositoryBase.newInstance is the no-arg resultType.newInstance() (RepositoryBase.java:109, 134); its auto CALL to EntityBase.<init>(ContentValues) is cut by sup below',
    'Category.java:39-41; Category.java:40 (auto record); CategoryListFragment.java:399; RepositoryBase.java:109, 134; label_064.grep.txt', 'SOURCE')

UNREACHABLE['Category.setParentId'] = ('no_trigger_in_app',
    'no caller: the only source reference is the definition (grep setParentId over src/main); the class scan finds 0 invokes of Category.setParentId in any class; no setter reflection (grep getMethod/getDeclaredMethod); its auto CALL to EntityBase.setInt is cut by sup below',
    'Category.java:55-57; Category.java:56 (auto record); label_064.grep.txt', 'SOURCE')

# ================================================================== UNREACHABLE: Category$$Parcelable and $1 (generated, INFERRED)

UNREACHABLE['Category$$Parcelable.<clinit>'] = ('no_trigger_in_app',
    'the static initializer runs on first use of the class; the class is never used: no class outside the group references Category$$Parcelable (class-file scan), and no Parcels.wrap call takes a Category (23 Parcels.wrap lines, none with a Category argument). Its auto CALL to $1.<init> is cut by sup below',
    'Category$$Parcelable.java:23 (generated; LineNumberTable of Category$$Parcelable.class, not on disk); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable.<init>'] = ('no_trigger_in_app',
    'the constructor of the wrapper (Category argument); called only by Category$$Parcelable$1.createFromParcel (auto CALL, line 28), which is itself unreachable; that auto CALL is cut by sup below',
    'Category$$Parcelable.java:39-41 (generated); Category$$Parcelable.java:28 (auto record); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable.describeContents'] = ('framework_never_calls',
    'Parcelable method of the wrapper; no Category is ever wrapped (grep and class-file scan, see the grep file), so no parcel of this class is written and the framework never calls it here (same shape as Account$$Parcelable.describeContents, batch 059)',
    'Category$$Parcelable.java:60 (generated); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable.getParcel'] = ('no_trigger_in_app',
    'generated accessor of the wrapper (the erased bridge getParcel()Object is at line 12); its callers would be Parcels.unwrap or a @Parcel field holding a Category, and the class scan finds none (no class outside the group references Category$$Parcelable)',
    'Category$$Parcelable.java:65 (generated), bridge :12; label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable.read'] = ('no_trigger_in_app',
    'called only by Category$$Parcelable$1.createFromParcel (auto CALL, line 28), which is unreachable; the body (lines 69-83) would build a Category through Category.<init>() (auto CALL at line 78, cut by sup below)',
    'Category$$Parcelable.java:69-83 (generated); Category$$Parcelable.java:78 and :28 (auto records); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable.write'] = ('no_trigger_in_app',
    'called only by writeToParcel (auto CALL, line 45), which is unreachable; the auto record is cut by sup below',
    'Category$$Parcelable.java:49-56 (generated); Category$$Parcelable.java:45 (auto record)', 'INFERRED')

UNREACHABLE['Category$$Parcelable.writeToParcel'] = ('no_trigger_in_app',
    'the Parcelable.writeToParcel body; the framework calls it only when a Category$$Parcelable is written to a Parcel (Parcels.wrap or putParcelable), which never happens (no Category is wrapped, see the grep file). Its auto CALL to write is cut by sup below',
    'Category$$Parcelable.java:45-46 (generated); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable$1.<init>'] = ('no_trigger_in_app',
    'the CREATOR constructor; created only by the static initializer Category$$Parcelable.<clinit> (auto CALL, line 23), which is unreachable; the auto record is cut by sup below',
    'Category$$Parcelable.java:23 (generated; LineNumberTable of Category$$Parcelable$1.class)', 'INFERRED')

UNREACHABLE['Category$$Parcelable$1.createFromParcel'] = ('no_trigger_in_app',
    'the CREATOR callback; the framework calls it only for a parcel that holds a Category$$Parcelable, which is never written (see the grep file); its three auto CALLs (to <clinit>, <init> and read, line 28) are cut by sup below',
    'Category$$Parcelable.java:28 (generated; LineNumberTable of Category$$Parcelable$1.class); label_064.grep.txt', 'INFERRED')

UNREACHABLE['Category$$Parcelable$1.newArray'] = ('no_trigger_in_app',
    'the CREATOR array factory; the framework calls it only for arrays of Category$$Parcelable, which never occur (no reference to this CREATOR outside the group)',
    'Category$$Parcelable.java:33 (generated; the erased bridge newArray(I)Object is at :23); label_064.grep.txt', 'INFERRED')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE here

sup(('Category.<init>(ContentValues)', 'EntityBase.<init>(ContentValues)'))
sup(('Category.setParentId', 'EntityBase.setInt'))
sup(('Category$$Parcelable.writeToParcel', 'Category$$Parcelable.write'))
sup(('Category$$Parcelable.read', 'Category.<init>()'))
sup(('Category$$Parcelable.<clinit>', 'Category$$Parcelable$1.<init>'))
sup(('Category$$Parcelable$1.createFromParcel', 'Category$$Parcelable.<clinit>'))
sup(('Category$$Parcelable$1.createFromParcel', 'Category$$Parcelable.<init>'))
sup(('Category$$Parcelable$1.createFromParcel', 'Category$$Parcelable.read'))

# ---- part 065 (2026-10-29)
# batch 065: Currency (24 methods). All routes are auto CALL records or edges of other batches (D1, D7), so no e() here.
# Only Currency.getCentName is UNREACHABLE (no caller in the source). Its auto CALL to EntityBase.getString is cut (D14a).

UNREACHABLE['Currency.getCentName'] = ('no_trigger_in_app',
    'no caller: the only references are the definition and the setter call CurrencyEditActivity.java:222; no getCentName call in src/main (label_065.grep.txt)',
    'Currency.java:59-61; CurrencyEditActivity.java:222', 'SOURCE')

sup(('Currency.getCentName', 'EntityBase.getString'))
# Cut deferred to this batch by label_046.py (its caller CurrencyRepository.query is UNREACHABLE there).
sup(('CurrencyRepository.query', 'Currency.fromCursor'))

# ---- part 067 (2026-10-29)
# ================================================================== batch 067 (label_067): Payee (9 methods)
# Result: 8 REACHABLE, 1 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_067.md).
# No e() edges: every bytecode CALL into a Payee method is already an auto record (D7). The REACHABLE rows
# take their routes from the exported CheckingTransactionEditActivity INSERT and EDIT paths (owned by other batches).
# One sup pair (D14a): the auto CALL record whose caller is UNREACHABLE in this batch.
# No SCREENS and no grep file: the one UNREACHABLE claim is a SOURCE fact (the grep is quoted in the reason).

# ================================================================== UNREACHABLE: the ContentValues constructor

UNREACHABLE['Payee.<init>(ContentValues)'] = ('no_trigger_in_app',
    'no caller: no new Payee(...) with an argument exists in the app source (grep over src/main/java: 5 hits, all the no-arg new Payee() at Core.java:151, PayeeService.java:56 and :94, PayeeListFragment.java:206, PayeeReportFragment.java:302; src/test has one more, DataHelpers.java:61, which is not in the app); reflection creates entities with the no-arg constructor only (Class.newInstance at RepositoryBase.java:109 and :134, SqlRepositoryBase.java:84); no auto CALL record has it as dst. Its own auto CALL to EntityBase.<init>(ContentValues) is cut by the sup below',
    'domainmodel/Payee.java:37-39; datalayer/RepositoryBase.java:109, 134; datalayer/SqlRepositoryBase.java:84; auto_calls.json record Payee.java:38',
    'SOURCE')

# ================================================================== sup (D14a): auto CALL record whose caller is UNREACHABLE here

sup(('Payee.<init>(ContentValues)', 'EntityBase.<init>(ContentValues)'))

# ---- part 066 (2026-10-29)
# ================================================================== batch 066 (label_066): EntityBase (16 methods), EntityBase$$Parcelable (7),
# EntityBase$$Parcelable$1 (3), Info (6).
# Result: 21 REACHABLE, 11 UNREACHABLE (rows: graphs/MMEX/parts/label_066.md).
# No e() edges and no SCREENS: every REACHABLE route is an auto CALL record (auto_calls.json) whose caller is reached in another batch
# (EntityBase.getDouble, getDate, setDate, getContentValues, Info.getId), or a route already listed in the owner batch (label_066.md).
# This file writes:
#   - UNREACHABLE entries for EntityBase.<init>(ContentValues) and the generated Parceler family (INFERRED, D5),
#   - 6 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.
# The generated family is evidenced in graphs/MMEX/parts/label_066.grep.txt (sections 1-9).
# The four ContentValues-constructor callers are cut by their owners (label_061.py, label_063.py, label_064.py; Payee in batch 067).

# ================================================================== EntityBase.<init>(ContentValues): UNREACHABLE (source evidence)

UNREACHABLE['EntityBase.<init>(ContentValues)'] = ('no_trigger_in_app',
    'protected constructor with no reachable caller: its four callers are the ContentValues constructors of AccountTransaction (AccountTransaction.java:79), '
    'Attachment (Attachment.java:40), Category (Category.java:40) and Payee (Payee.java:38). None of those four has a caller: no auto_calls.json record targets them, '
    'and every constructor call in app source is the no-argument form (label_066.grep.txt sections 6 and 7)',
    'SRC domainmodel/EntityBase.java:49; label_066.grep.txt sections 6, 7; sup cuts owned by label_061.py, label_063.py, label_064.py (Payee: batch 067)',
    'SOURCE')

# ================================================================== EntityBase$$Parcelable and $1: UNREACHABLE (generated by Parceler, INFERRED)
# No entry route: no EntityBase object is ever wrapped (no Parcels.wrap names an EntityBase; every wrapped runtime class is a @Parcel subclass), and no
# EntityBase-typed field exists in any @Parcel class (label_066.grep.txt sections 3, 4, 5). Parceler is a library, not read: INFERRED.
# Precedents: label_013.py (StatusFilter$$Parcelable), label_063.py (Budget$$Parcelable).

UNREACHABLE['EntityBase$$Parcelable.<clinit>'] = ('no_trigger_in_app',
    'static initialiser of the generated class: it runs only when the class is first loaded, which needs a Parcels.wrap or unwrap that names an EntityBase object (none) '
    'or a class file that names the generated class (only the two generated class files, label_066.grep.txt section 1). Its auto CALL to EntityBase$$Parcelable$1.<init> '
    '(generated line 23) is cut by sup below',
    'SRC domainmodel/EntityBase.java:38; auto_calls.json (EntityBase$$Parcelable.<clinit> -> EntityBase$$Parcelable$1.<init>, line 23); label_066.grep.txt sections 1, 3, 4, 5, 7',
    'INFERRED')

UNREACHABLE['EntityBase$$Parcelable.<init>'] = ('no_trigger_in_app',
    'generated constructor: its only caller is EntityBase$$Parcelable$1.createFromParcel (auto CALL, generated line 28), which is itself UNREACHABLE; the family is never instantiated',
    'auto_calls.json (EntityBase$$Parcelable$1.createFromParcel -> EntityBase$$Parcelable.<init>, generated line 28); label_066.grep.txt sections 1, 3, 7',
    'INFERRED')

UNREACHABLE['EntityBase$$Parcelable.describeContents'] = ('framework_never_calls',
    'Parcelable method that the framework calls on a wrapper object in a bundle or parcel: Bundle.hasFileDescriptors (FW-SRC Bundle.java:316-371, calls at lines 329, 338, 349, 362) '
    'and Bundle.describeContents (FW-SRC Bundle.java:1215-1217) call describeContents on Parcelable values. No EntityBase wrapper is placed in a bundle or parcel '
    '(no Parcels.wrap of an EntityBase object, label_066.grep.txt sections 3 and 5), and no app code calls describeContents (label_066.grep.txt section 2). '
    'Framework paths beyond these lines are not read (INFERRED)',
    'FW-SRC core/java/android/os/Bundle.java:316-371, 1215-1217; label_066.grep.txt sections 2, 3, 5, 8',
    'INFERRED')

UNREACHABLE['EntityBase$$Parcelable.getParcel'] = ('no_trigger_in_app',
    'returns the wrapped EntityBase. Its only possible callers are Parcels.unwrap (parceler library reflection) on an EntityBase wrapper read from a bundle; no such wrapper is written '
    '(label_066.grep.txt sections 3 and 5), and no auto_calls.json record has getParcel as dst',
    'label_066.grep.txt sections 3, 5, 7',
    'INFERRED')

UNREACHABLE['EntityBase$$Parcelable.read'] = ('no_trigger_in_app',
    'called only by EntityBase$$Parcelable$1.createFromParcel (auto CALL, generated line 28), which is UNREACHABLE. Its auto CALL to EntityBase.<init>() (generated line 78) is cut by sup below',
    'auto_calls.json (EntityBase$$Parcelable$1.createFromParcel -> EntityBase$$Parcelable.read, line 28; EntityBase$$Parcelable.read -> EntityBase.<init>(), line 78); label_066.grep.txt section 7',
    'INFERRED')

UNREACHABLE['EntityBase$$Parcelable.write'] = ('no_trigger_in_app',
    'called only by EntityBase$$Parcelable.writeToParcel (auto CALL, generated line 45), which is UNREACHABLE',
    'auto_calls.json (EntityBase$$Parcelable.writeToParcel -> EntityBase$$Parcelable.write, generated line 45); label_066.grep.txt section 7',
    'INFERRED')

UNREACHABLE['EntityBase$$Parcelable.writeToParcel'] = ('no_trigger_in_app',
    'Parcelable callback that the framework calls only from Parcel.writeParcelable (FW-SRC Parcel.java:1785-1791) for a wrapper written into a parcel. '
    'No EntityBase wrapper is written (label_066.grep.txt sections 3 and 5), and no auto_calls.json record has it as dst. Its only app call is to '
    'EntityBase$$Parcelable.write (generated line 45), which is cut by sup below',
    'FW-SRC core/java/android/os/Parcel.java:1785-1791; auto_calls.json (generated line 45); label_066.grep.txt sections 3, 5, 7',
    'INFERRED')

UNREACHABLE['EntityBase$$Parcelable$1.<init>'] = ('no_trigger_in_app',
    'CREATOR constructor: its only caller is EntityBase$$Parcelable.<clinit> (auto CALL, generated line 23), which is UNREACHABLE',
    'auto_calls.json (EntityBase$$Parcelable.<clinit> -> EntityBase$$Parcelable$1.<init>, generated line 23); label_066.grep.txt section 7',
    'INFERRED')

UNREACHABLE['EntityBase$$Parcelable$1.createFromParcel'] = ('no_trigger_in_app',
    'CREATOR callback: the framework calls it only through Parcel.readParcelable (FW-SRC Parcel.java:2841-2851) when a parcel names EntityBase$$Parcelable as its creator class. '
    'That name is written only by Parcel.writeParcelable of a top-level EntityBase wrapper, which never happens (label_066.grep.txt sections 3 and 5). '
    'Its auto CALLs to <clinit>, <init> and read (generated line 28) are cut by sup below',
    'FW-SRC core/java/android/os/Parcel.java:2841-2851; auto_calls.json (generated line 28, three records); label_066.grep.txt sections 3, 5, 7',
    'INFERRED')

UNREACHABLE['EntityBase$$Parcelable$1.newArray'] = ('framework_never_calls',
    'CREATOR array factory: the framework calls it only when it reads a typed array of EntityBase$$Parcelable wrappers, and no such array is written or read '
    '(no EntityBase wrapper is written, label_066.grep.txt sections 3 and 5); no auto_calls.json record targets it',
    'label_066.grep.txt sections 3, 5, 7; generated class not in the source root',
    'INFERRED')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('EntityBase$$Parcelable.writeToParcel', 'EntityBase$$Parcelable.write'))
sup(('EntityBase$$Parcelable.read', 'EntityBase.<init>()'))
sup(('EntityBase$$Parcelable.<clinit>', 'EntityBase$$Parcelable$1.<init>'))
sup(('EntityBase$$Parcelable$1.createFromParcel', 'EntityBase$$Parcelable.<clinit>'))
sup(('EntityBase$$Parcelable$1.createFromParcel', 'EntityBase$$Parcelable.<init>'))
sup(('EntityBase$$Parcelable$1.createFromParcel', 'EntityBase$$Parcelable.read'))

# ---- part 068 (2026-10-29)
# ================================================================== batch 068 (label_068): RecurringTransaction, methods 1-40 of 57
# Result: 38 REACHABLE, 2 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_068.md).
# No e() edges and no SCREENS: every REACHABLE route is an auto CALL record (auto_calls.json, bytecode-derived) whose caller is reached in another batch.
# This file writes:
#   - UNREACHABLE entries for RecurringTransaction.getPaymentDateString and RecurringTransaction.setPaymentDate(String) (SOURCE),
#   - 2 sup pairs (D14a): their auto CALL records to EntityBase.getString and EntityBase.setString.
# Grep evidence: graphs/MMEX/parts/label_068.grep.txt (sections 1-3).

# ================================================================== RecurringTransaction: UNREACHABLE (source evidence)

UNREACHABLE['RecurringTransaction.getPaymentDateString'] = ('no_trigger_in_app',
    'no caller in app source: the name appears only at its definition (no XML or data-binding reference either); no bytecode CALL record targets it',
    'domainmodel/RecurringTransaction.java:212-214; label_068.grep.txt section 1', 'SOURCE')

UNREACHABLE['RecurringTransaction.setPaymentDate(String)'] = ('no_trigger_in_app',
    'no call site passes a String: the call sites in app source pass a Date (RecurringTransactionEditActivity.java:362, 386, 394, 404, 626, 635 and RecurringTransactionService.java:426), and no bytecode CALL record targets this overload',
    'domainmodel/RecurringTransaction.java:216-218; RecurringTransactionEditActivity.java:362, 386, 394, 404, 626, 635; RecurringTransactionService.java:426; label_068.grep.txt section 2', 'SOURCE')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('RecurringTransaction.getPaymentDateString', 'EntityBase.getString'))
sup(('RecurringTransaction.setPaymentDate(String)', 'EntityBase.setString'))

# ---- part 069 (2026-10-29)
# ================================================================== batch 069 (label_069): RecurringTransaction setters and the Parceler classes
# RecurringTransaction$$Parcelable (<clinit>, <init>, describeContents, getParcel, read, write, writeToParcel) and
# RecurringTransaction$$Parcelable$1 (<init>, createFromParcel, newArray). RecurringTransaction methods 41-57 of 57 (17 methods).
# Result: 15 REACHABLE, 2 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_069.md). The generated classes are not in the source root;
# their methods were read from the build class files (constant pool and bytecode, INFERRED). Grep evidence: graphs/MMEX/parts/label_069.grep.txt.
# Edges written here: the saved-state round trip of RecurringTransactionEditActivity (save in onSaveInstanceState, restore in restoreInstanceState).
# The Parceler library is not read, so the wrap and unwrap hops are INFERRED.
# The setters and the bytecode-reached Parceler methods are REACHABLE through auto_calls.json records; no CALL edge is written for them (D7).
# No sup pairs (D14a): no auto CALL record starts in describeContents or newArray (grep block E). No gui() calls: the setter routes are auto records.

# ---- saved state: RecurringTransactionEditActivity.onSaveInstanceState wraps the transaction and the framework parcels the bundle (line 181)

e('RecurringTransactionEditActivity.onSaveInstanceState', 'RecurringTransaction$$Parcelable.writeToParcel', 'FRAMEWORK',
  'Parcels.wrap(mCommon.transactionEntity) puts a RecurringTransaction wrapper in the saved-state bundle; when the framework saves the state, the bundle is parcelled and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard', via='outState.putParcelable(KEY_MODEL, Parcels.wrap(mCommon.transactionEntity)) at recurring/transactions/RecurringTransactionEditActivity.java:181; the framework parcels the saved-state bundle (Bundle.writeToParcel, FW-SRC core/java/android/os/Bundle.java:1229, sent by ActivityThread activityStopped, FW-SRC core/java/android/app/ActivityThread.java:3930-3935); Parcel.writeParcelable calls p.writeToParcel (FW-SRC core/java/android/os/Parcel.java:1785-1791). Parcels.wrap returns the generated wrapper (parceler library not read, INFERRED)',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:178-181, 399-404, 442 (runtime type RecurringTransaction); FW-SRC core/java/android/os/Parcel.java:1785-1791; FW-SRC core/java/android/os/Bundle.java:1229; FW-SRC core/java/android/app/ActivityThread.java:3930-3935; label_069.grep.txt blocks A, F, H; INFERRED parceler library not read')

# ---- saved state: RecurringTransactionEditActivity.restoreInstanceState unparcels the saved transaction (line 549) and unwraps it (line 549)

e('RecurringTransactionEditActivity.restoreInstanceState', 'RecurringTransaction$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle holds the RecurringTransaction wrapper; the first getParcelable unparcels the bundle, and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='the restore runs only when onCreate gets a saved bundle: onCreate calls restoreInstanceState at line 109 only when savedInstanceState is not null (line 108)',
  cls='non_standard', via='savedInstanceState.getParcelable(KEY_MODEL) at recurring/transactions/RecurringTransactionEditActivity.java:549 calls unparcel (FW-SRC core/java/android/os/Bundle.java:938-939); Parcel.readParcelable reads the CREATOR field (FW-SRC core/java/android/os/Parcel.java:2894) and calls creator.createFromParcel (FW-SRC core/java/android/os/Parcel.java:2841-2851)',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:102, 107-110, 547-549; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_069.grep.txt blocks A, F, H; INFERRED parceler library not read')

e('RecurringTransactionEditActivity.restoreInstanceState', 'RecurringTransaction$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the wrapper read from the saved bundle and returns the RecurringTransaction',
  guard='the same guard as the createFromParcel edge: restoreInstanceState runs only when onCreate gets a saved bundle (lines 108-109)',
  cls='non_standard', via='Parcels.unwrap(savedInstanceState.getParcelable(KEY_MODEL)) at recurring/transactions/RecurringTransactionEditActivity.java:549 (parceler library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:108-109, 547-549; label_069.grep.txt blocks A, E, F; INFERRED parceler library not read')

# ================================================================== UNREACHABLE: describeContents and the typed-array creator

UNREACHABLE['RecurringTransaction$$Parcelable.describeContents'] = ('framework_never_calls',
  'generated describeContents returns 0 (class file bytes 03 ac: iconst_0, ireturn). No app code calls it: the SRC scan finds only definitions (DefinedDateRange, CategorySub, ValuePieEntry; StatusFilter is commented out) and no call site (label_069.grep.txt block C). The framework calls describeContents on Parcelable values only in Bundle.java (lines 329, 338, 349, 362) and Intent.java:9553 (block D). The walk at Bundle.java:324-340 runs only when mParcelledData is null; the icicle that ActivityManagerService.activityStopped checks (line 7453) is parcelled, so that walk does not reach this wrapper (INFERRED: the binder path is not read). No auto record names it',
  'FW-SRC core/java/android/os/Bundle.java:316-340; FW-SRC services/core/java/com/android/server/am/ActivityManagerService.java:7448-7455; label_069.grep.txt blocks C, D, E, F, H',
  'INFERRED')

UNREACHABLE['RecurringTransaction$$Parcelable$1.newArray'] = ('framework_never_calls',
  'CREATOR typed-array method (bytecode 1b bd 00 07 b0: iload_1, anewarray, areturn). The framework calls Creator.newArray only from Parcel.createTypedArray (FW-SRC core/java/android/os/Parcel.java:2645, c.newArray(N)); the other 33 newArray hits in core/java and services/core/java are definitions (label_069.grep.txt block D). createTypedArray is not called from app source (block C has no createTypedArray or readTypedArray hit), so no typed array of RecurringTransaction wrappers is read. No auto_calls.json record has newArray as dst or $1.newArray as src (block E). Whether the Parceler library calls newArray is INFERRED (library not read)',
  'FW-SRC core/java/android/os/Parcel.java:2640-2646; label_069.grep.txt blocks C, D, E, F, H',
  'INFERRED')

# ---- part 070 (2026-10-29)
# ================================================================== batch 070 (label_070): SplitCategory (19 methods),
# SplitCategory$$Parcelable (7 methods), SplitCategory$$Parcelable$1 (3 methods). 29 methods in total.
# Result: 24 REACHABLE, 5 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_070.md).
# SplitCategory is a @Parcel class. Its Parceler class SplitCategory$$Parcelable and the CREATOR $1 are generated at build time,
# so they are not in the source root; their methods were read from the build class files (constant-pool strings, INFERRED).
# Grep and class-file evidence: graphs/MMEX/parts/label_070.grep.txt.
# Edges written here (D1, destinations owned by this batch):
#   - FRAMEWORK writeToParcel from the five Parcels.wrap sites of the split lists,
#   - FRAMEWORK createFromParcel from the five Parcels.unwrap sites (restore paths and intent extras),
#   - CALL non_standard getParcel from the same five unwrap sites (Parcels.unwrap calls the generated getParcel; library not read, INFERRED).
# The Parceler library is not read, so the wrap, unwrap and element hops are INFERRED.
# write, read, $$Parcelable.<init>, $$Parcelable.<clinit> and $1.<init> are REACHABLE through auto CALL records (auto_calls.json).
# No CALL edge duplicates an auto record (D7): no auto record names getParcel.
# sup pairs (D14a): the three auto CALL records whose caller is UNREACHABLE here (getAccountId, setAccountId, getTransId).

# ================================================================== the wrap sites (FRAMEWORK writeToParcel)

_WRITE_SITES = (
    ('CheckingTransactionEditActivity.onSaveInstanceState',
     'transactions/CheckingTransactionEditActivity.java:175-177',
     'saved state: the split lists are wrapped into the saved-state bundle; when the framework saves the state it parcels the bundle and writes the element wrappers',
     'SRC transactions/CheckingTransactionEditActivity.java:162-177'),
    ('RecurringTransactionEditActivity.onSaveInstanceState',
     'recurring/transactions/RecurringTransactionEditActivity.java:191-192',
     'saved state of the recurring editor: the same wrap of the split lists into the saved-state bundle',
     'SRC recurring/transactions/RecurringTransactionEditActivity.java:178-192'),
    ('SplitCategoriesActivity.onSaveInstanceState',
     'transactions/SplitCategoriesActivity.java:184-187',
     'saved state of the split screen: the adapter list and the deleted list are wrapped into the saved-state bundle',
     'SRC transactions/SplitCategoriesActivity.java:181-187'),
    ('SplitCategoriesActivity.onActionDoneClick',
     'transactions/SplitCategoriesActivity.java:172-173',
     'the split screen returns the list to its caller in a result intent; the result extras are parcelled when the result is delivered',
     'SRC transactions/SplitCategoriesActivity.java:149-173; INFERRED intent extras are parcelled when the result crosses the binder (Intent.writeToParcel not read)'),
    ('EditTransactionCommonFunctions.showSplitCategoriesForm',
     'transactions/EditTransactionCommonFunctions.java:1522-1523',
     'the split screen is started with the list in its intent extras; the extras are parcelled when the activity starts',
     'SRC transactions/EditTransactionCommonFunctions.java:1511-1523; INFERRED intent extras are parcelled on startActivity (Intent.writeToParcel not read)'),
)
for _src, _where, _why, _ev in _WRITE_SITES:
    e(_src, 'SplitCategory$$Parcelable.writeToParcel', 'FRAMEWORK', _why,
      cls='non_standard',
      via='Parcels.wrap at ' + _where + '; Parcel.writeParcelable calls writeToParcel on the element wrapper (FW-SRC core/java/android/os/Parcel.java:1785-1791)',
      evidence=_ev + '; FW-SRC core/java/android/os/Parcel.java:1785-1791; FW-SRC core/java/android/os/Bundle.java:1229; INFERRED the parceler library writes each element wrapper with writeParcelable (library not read)')

# ================================================================== the unwrap sites (FRAMEWORK createFromParcel, CALL getParcel)

_READ_SITES = (
    ('CheckingTransactionEditActivity.restoreInstanceState',
     'transactions/CheckingTransactionEditActivity.java:655-657',
     'saved state: restoreInstanceState reads the split lists from the saved-state bundle; the framework reads the element wrapper with its CREATOR, which calls createFromParcel',
     'SRC transactions/CheckingTransactionEditActivity.java:647-657'),
    ('RecurringTransactionEditActivity.restoreInstanceState',
     'recurring/transactions/RecurringTransactionEditActivity.java:555-556',
     'saved state of the recurring editor: the same read of the split lists from the saved-state bundle',
     'SRC recurring/transactions/RecurringTransactionEditActivity.java:547-556'),
    ('SplitCategoriesActivity.onCreate',
     'transactions/SplitCategoriesActivity.java:91-92',
     'the split screen restores its saved lists in onCreate when the saved bundle is not null',
     'SRC transactions/SplitCategoriesActivity.java:82-97'),
    ('SplitCategoriesActivity.handleIntent',
     'transactions/SplitCategoriesActivity.java:247-251',
     'the split screen reads the lists from its start intent extras',
     'SRC transactions/SplitCategoriesActivity.java:236-251; INFERRED intent getParcelableExtra unparcels as Bundle.getParcelable (Intent not read)'),
    ('EditTransactionCommonFunctions.onActivityResult',
     'transactions/EditTransactionCommonFunctions.java:890-895',
     'the result of the split screen is read back from its result intent extras',
     'SRC transactions/EditTransactionCommonFunctions.java:848-895; INFERRED intent getParcelableExtra unparcels as Bundle.getParcelable (Intent not read)'),
)
for _src, _where, _why, _ev in _READ_SITES:
    e(_src, 'SplitCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK', _why,
      cls='non_standard',
      via='Parcels.unwrap at ' + _where + '; the framework unparcels the Parcelable (Bundle.getParcelable, FW-SRC core/java/android/os/Bundle.java:938-939) and Parcel.readParcelable calls creator.createFromParcel (FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894)',
      evidence=_ev + '; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; INFERRED the parceler library reads the lists from the wrapper (library not read)')
    e(_src, 'SplitCategory$$Parcelable.getParcel', 'CALL',
      'Parcels.unwrap calls getParcel on each element wrapper and returns the SplitCategory list',
      cls='non_standard',
      via='Parcels.unwrap at ' + _where + ' (the parceler library calls the generated getParcel; library source not read, INFERRED)',
      evidence=_ev + '; INFERRED parceler library not read')

# ================================================================== UNREACHABLE: the accessors with no caller

UNREACHABLE['SplitCategory.getAccountId'] = ('no_trigger_in_app',
    'no caller: ISplitTransaction declares getAccountId (line 35), but no call site in the source root has a split-typed receiver; the getAccountId() call sites are on Account, AccountTransaction, RecurringTransaction and AccountTransactionDisplay receivers; no auto_calls.json record has dst SplitCategory.getAccountId or ISplitTransaction.getAccountId; its one auto record (src SplitCategory.getAccountId) is cut by sup below',
    'domainmodel/SplitCategory.java:87-90; database/ISplitTransaction.java:35; label_070.grep.txt sections 3, 4', 'SOURCE')

UNREACHABLE['SplitCategory.setAccountId'] = ('no_trigger_in_app',
    'no caller: the only declarations are ISplitTransaction.java:36 and SplitCategory.java:92; the setAccountId call sites are on transactionEntity (ITransactionEntity, implemented by AccountTransaction and RecurringTransaction, auto cha records), and SplitCategory does not implement ITransactionEntity; its one auto record (src SplitCategory.setAccountId) is cut by sup below',
    'domainmodel/SplitCategory.java:92-95; database/ISplitTransaction.java:36; database/ITransactionEntity.java:50; label_070.grep.txt sections 3, 4', 'SOURCE')

UNREACHABLE['SplitCategory.getTransId'] = ('no_trigger_in_app',
    'no caller: getTransId is not declared on ISplitTransaction, its only definitions in the source root are SplitCategory.java:132 and SplitRecurringCategory.java:134, and no call site or auto_calls.json record names it; its one auto record (src SplitCategory.getTransId) is cut by sup below',
    'domainmodel/SplitCategory.java:132-134; domainmodel/SplitRecurringCategory.java:134; label_070.grep.txt section 3', 'SOURCE')

# ================================================================== UNREACHABLE: generated describeContents and the typed-array creator

UNREACHABLE['SplitCategory$$Parcelable.describeContents'] = ('framework_never_calls',
    'generated describeContents returns 0 (INFERRED from the class file). No app code calls describeContents (label_070.grep.txt section 2, no call site). The framework calls it on Parcelable values it receives directly (Bundle values and Intent extras through hasFileDescriptors, FW-SRC core/java/android/os/Bundle.java:316-336, 1215-1218). The element wrappers of the split lists sit inside the list wrapper, not as direct bundle or intent values, so the framework does not call describeContents on them (INFERRED: the list wrapper is not read). No auto record names it',
    'FW-SRC core/java/android/os/Bundle.java:316-336, 1215-1218; label_070.grep.txt sections 2, 5', 'INFERRED')

UNREACHABLE['SplitCategory$$Parcelable$1.newArray'] = ('framework_never_calls',
    'CREATOR typed-array method. The framework calls it only from Parcel.createTypedArray(Creator) (FW-SRC core/java/android/os/Parcel.java:2640-2645), that is, when app code reads a typed array of SplitCategory wrappers. No app code does: the source root has no createTypedArray or writeTypedArray call, and its newArray implementations are DefinedDateRange, CategorySub and ValuePieEntry only (label_070.grep.txt section 2). No auto_calls.json record has newArray as dst or $1.newArray as src. Whether the Parceler library calls newArray is INFERRED (library not read)',
    'FW-SRC core/java/android/os/Parcel.java:2640-2645; label_070.grep.txt sections 2, 5', 'INFERRED')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE here

sup(('SplitCategory.getAccountId', 'EntityBase.getInt'),
    ('SplitCategory.setAccountId', 'EntityBase.setInt'),
    ('SplitCategory.getTransId', 'EntityBase.getInt'))

# ---- part 071 (2026-10-29)
# ================================================================== batch 071 (label_071): SplitRecurringCategory (19 methods),
# SplitRecurringCategory$$Parcelable (7) and SplitRecurringCategory$$Parcelable$1 (3).
# Result: 24 REACHABLE, 5 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_071.md). Grep evidence: graphs/MMEX/parts/label_071.grep.txt.
# Accessors, create, setters, loadFromCursor and <clinit> need no edge here: their routes are auto CALL records (auto_calls.json).
# The generated Parceler classes are not in the source root; their methods were read from the build class files (INFERRED).
# Edges written here (every destination is in this batch, D1):
#   - FRAMEWORK edges for the split-list parcel round trips: the split form Intent, the activity result, the checking editor's
#     saved state, and the split screen's own Intent, saved state and result;
#   - non_standard CALL edges to getParcel from the Parcels.unwrap sites (the parceler library calls it; INFERRED);
#   - UNREACHABLE entries for the three accessors with no caller and for the two generated framework callbacks;
#   - sup pairs (D14a): the auto CALL records of the UNREACHABLE accessors into EntityBase.

# ---- split form: showSplitCategoriesForm puts the split list in the Intent that starts SplitCategoriesActivity

e('EditTransactionCommonFunctions.showSplitCategoriesForm', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the split form Intent carries Parcels.wrap(splitsToShow); startActivityForResult marshals the Intent, the wrapper parcels the list, and each SplitRecurringCategory element is written through its generated writeToParcel',
  cls='non_standard',
  via='intent.putExtra(KEY_SPLIT_TRANSACTION, Parcels.wrap(splitsToShow)) at transactions/EditTransactionCommonFunctions.java:1522; getActivity().startActivityForResult at 1528; Parcel.writeParcelable calls p.writeToParcel (FW-SRC core/java/android/os/Parcel.java:1785-1791); the list wrapper element writes are parceler library code (INFERRED)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1511-1529; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

# ---- checking editor saved state: onSaveInstanceState wraps the split list; restoreInstanceState unwraps it

e('CheckingTransactionEditActivity.onSaveInstanceState', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the saved-state bundle holds Parcels.wrap(mCommon.mSplitTransactions); when the framework saves the state, the bundle is parcelled and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard',
  via='outState.putParcelable(KEY_SPLIT_TRANSACTION, Parcels.wrap(mCommon.mSplitTransactions)) at transactions/CheckingTransactionEditActivity.java:175 (method starts at 162); framework parcelling as in batch 062 (FW-SRC core/java/android/os/Parcel.java:1785-1791; Bundle.java:1229)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:162-178; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

e('CheckingTransactionEditActivity.restoreInstanceState', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle holds the split list wrapper; the first getParcelable unparcels it and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='the restore runs only when onCreate gets a saved bundle: onCreate calls restoreInstanceState (line 107) only when savedInstanceState is not null (line 106)',
  cls='non_standard',
  via='savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION) at transactions/CheckingTransactionEditActivity.java:655 (the deleted list at 657); Bundle.getParcelable unparcels (FW-SRC core/java/android/os/Bundle.java:938-939); Parcel.readParcelable calls creator.createFromParcel (FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:106-107, 647-660; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block F; INFERRED parceler library not read')

e('CheckingTransactionEditActivity.restoreInstanceState', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on each split list wrapper read from the saved bundle and returns the list of SplitRecurringCategory',
  guard='the same guard as the createFromParcel edge: restoreInstanceState runs only when onCreate gets a saved bundle (lines 106-107)',
  cls='non_standard',
  via='Parcels.unwrap(...getParcelable(KEY_SPLIT_TRANSACTION)) at transactions/CheckingTransactionEditActivity.java:655 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/CheckingTransactionEditActivity.java:106-107, 647-660; label_071.grep.txt block F; INFERRED parceler library not read')

# ---- activity result: EditTransactionCommonFunctions.onActivityResult unwraps the split lists returned by SplitCategoriesActivity

e('EditTransactionCommonFunctions.onActivityResult', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the result Intent carries the split list wrapper; getParcelableExtra unparcels it and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='the SPLIT_TX request branch: case RequestCodes.SPLIT_TX (line 889)',
  cls='non_standard',
  via='data.getParcelableExtra(SplitCategoriesActivity.INTENT_RESULT_SPLIT_TRANSACTION) at transactions/EditTransactionCommonFunctions.java:890 (the deleted list at 893); Bundle unparcel and Parcel.readParcelable as in the restore edge (FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:848, 889-896; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block F; INFERRED parceler library not read')

e('EditTransactionCommonFunctions.onActivityResult', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the split list wrapper returned by SplitCategoriesActivity and returns the list',
  guard='the SPLIT_TX request branch (line 889)',
  cls='non_standard',
  via='mSplitTransactions = Parcels.unwrap(data.getParcelableExtra(...)) at transactions/EditTransactionCommonFunctions.java:890 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:889-896; label_071.grep.txt block F; INFERRED parceler library not read')

# ---- split screen: SplitCategoriesActivity receives the Intent, restores its saved state, returns the result and saves its state

e('SplitCategoriesActivity.handleIntent', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the split form Intent carries the split list wrapper; getParcelableExtra unparcels it and the framework reads the wrapper with its CREATOR',
  cls='non_standard',
  via='intent.getParcelableExtra(KEY_SPLIT_TRANSACTION) at transactions/SplitCategoriesActivity.java:247 (the deleted list at 251); FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894',
  evidence='SRC transactions/SplitCategoriesActivity.java:236-252; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.handleIntent', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the split list wrapper read from the form Intent',
  cls='non_standard',
  via='Parcels.unwrap(intent.getParcelableExtra(KEY_SPLIT_TRANSACTION)) at transactions/SplitCategoriesActivity.java:247 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/SplitCategoriesActivity.java:236-252; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.onCreate', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the saved-state bundle of the split screen holds the split list wrapper; the first getParcelable unparcels it and the framework reads it with the CREATOR',
  guard='the restore runs only when onCreate gets a saved bundle (line 90)',
  cls='non_standard',
  via='savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION) at transactions/SplitCategoriesActivity.java:91 (the deleted list at 92); FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894',
  evidence='SRC transactions/SplitCategoriesActivity.java:82-93; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.onCreate', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the split list wrapper read from the split screen saved state',
  guard='the same guard as the createFromParcel edge (line 90)',
  cls='non_standard',
  via='Parcels.unwrap(savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION)) at transactions/SplitCategoriesActivity.java:91 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC transactions/SplitCategoriesActivity.java:82-93; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.onActionDoneClick', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the edited split list goes back to the caller in the result Intent built with Parcels.wrap; setResult hands it to the caller, which marshals the Intent and calls writeToParcel on each wrapper',
  cls='non_standard',
  via='result.putExtra(INTENT_RESULT_SPLIT_TRANSACTION, Parcels.wrap(allSplitTransactions)) at transactions/SplitCategoriesActivity.java:172; setResult(RESULT_OK, result) at 174; FW-SRC core/java/android/os/Parcel.java:1785-1791',
  evidence='SRC transactions/SplitCategoriesActivity.java:149-175; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

e('SplitCategoriesActivity.onSaveInstanceState', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the split screen saved state holds Parcels.wrap of the split list; when the framework saves the state, the bundle is parcelled and writeToParcel runs',
  cls='non_standard',
  via='outState.putParcelable(KEY_SPLIT_TRANSACTION, Parcels.wrap(mAdapter.splitTransactions)) at transactions/SplitCategoriesActivity.java:184 (the deleted list at 187); FW-SRC core/java/android/os/Parcel.java:1785-1791',
  evidence='SRC transactions/SplitCategoriesActivity.java:181-189; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block F; INFERRED parceler library not read')

# ---- recurring editor saved state: RecurringTransactionEditActivity.onSaveInstanceState wraps the split lists (lines 191-192);
#      restoreInstanceState (line 547, called under the guard at line 108) unwraps them (lines 555-556)

e('RecurringTransactionEditActivity.onSaveInstanceState', 'SplitRecurringCategory$$Parcelable.writeToParcel', 'FRAMEWORK',
  'the recurring editor saved state holds Parcels.wrap of the split list and of the deleted list; when the framework saves the state, the bundle is parcelled and Parcel.writeParcelable calls writeToParcel',
  cls='non_standard',
  via='outState.putParcelable(KEY_SPLIT_TRANSACTION, Parcels.wrap(mCommon.mSplitTransactions)) at recurring/transactions/RecurringTransactionEditActivity.java:191 (the deleted list at 192; the method starts at 178); FW-SRC core/java/android/os/Parcel.java:1785-1791',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:178, 191-192; FW-SRC core/java/android/os/Parcel.java:1785-1791; label_071.grep.txt block A and block F; INFERRED parceler library not read')

e('RecurringTransactionEditActivity.restoreInstanceState', 'SplitRecurringCategory$$Parcelable$1.createFromParcel', 'FRAMEWORK',
  'the recurring editor saved state holds the split list wrapper; the first getParcelable unparcels the bundle and the framework reads the wrapper with its CREATOR, which calls createFromParcel',
  guard='restoreInstanceState runs only when onCreate gets a saved bundle: the call at line 109 is under the check at line 108',
  cls='non_standard',
  via='savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION) at recurring/transactions/RecurringTransactionEditActivity.java:555 (the deleted list at 556; the method starts at 547); FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:96-109, 547-556; FW-SRC core/java/android/os/Bundle.java:938-939; FW-SRC core/java/android/os/Parcel.java:2841-2851, 2894; label_071.grep.txt block A and block F; INFERRED parceler library not read')

e('RecurringTransactionEditActivity.restoreInstanceState', 'SplitRecurringCategory$$Parcelable.getParcel', 'CALL',
  'Parcels.unwrap calls getParcel on the split list wrapper read from the recurring editor saved state and returns the list',
  guard='the same guard as the createFromParcel edge (line 108)',
  cls='non_standard',
  via='Parcels.unwrap(savedInstanceState.getParcelable(KEY_SPLIT_TRANSACTION)) at recurring/transactions/RecurringTransactionEditActivity.java:555 (library calls the generated getParcel; library source not read, INFERRED)',
  evidence='SRC recurring/transactions/RecurringTransactionEditActivity.java:108-109, 555; label_071.grep.txt block A; INFERRED parceler library not read')

# ---- the wrap site of the split form also starts the generated class: Parcels.wrap creates SplitRecurringCategory$$Parcelable
#      for the elements, so its static initializer and constructor run here (library, INFERRED; same convention as batch 059)

e('EditTransactionCommonFunctions.showSplitCategoriesForm', 'SplitRecurringCategory$$Parcelable.<clinit>', 'CALL',
  'the split form is opened with the split list: Parcels.wrap(splitsToShow) makes the library create the generated wrapper, and the first use of the class runs its static initializer, which creates SplitRecurringCategory$$Parcelable$1',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): creates SplitRecurringCategory$$Parcelable, which initialises the class',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1522 (Parcels.wrap); generated SplitRecurringCategory$$Parcelable.java is not in the source root: auto_calls.json record <clinit> -> SplitRecurringCategory$$Parcelable$1.<init> at SplitRecurringCategory$$Parcelable.java:23')

e('EditTransactionCommonFunctions.showSplitCategoriesForm', 'SplitRecurringCategory$$Parcelable.<init>', 'CALL',
  'the same wrap: Parcels.wrap calls the wrapper constructor with each SplitRecurringCategory element of the list',
  cls='non_standard',
  via='org.parceler.Parcels.wrap (library, not read; INFERRED): new SplitRecurringCategory$$Parcelable(SplitRecurringCategory)',
  evidence='SRC transactions/EditTransactionCommonFunctions.java:1522; generated class not in the source root: auto_calls.json record SplitRecurringCategory$$Parcelable$1.createFromParcel -> SplitRecurringCategory$$Parcelable.<init> at SplitRecurringCategory$$Parcelable.java:28')

# ================================================================== UNREACHABLE: accessors with no caller

UNREACHABLE['SplitRecurringCategory.getAccountId'] = ('no_trigger_in_app',
    'no caller: no auto_calls.json record has SplitRecurringCategory.getAccountId as dst (no exact record, and no cha record from the ISplitTransaction interface), and every getAccountId() call in the source root is on a transaction, recurring, account or adapter receiver (label_071.grep.txt block D)',
    'domainmodel/SplitRecurringCategory.java:89-91; database/ISplitTransaction.java:35; domainmodel/SplitCategory.java:87; label_071.grep.txt block D',
    'SOURCE')

UNREACHABLE['SplitRecurringCategory.setAccountId'] = ('no_trigger_in_app',
    'no caller: no auto_calls.json record has SplitRecurringCategory.setAccountId as dst, and every setAccountId( call in the source root is on a transaction entity, the adapter or the own class of another type (label_071.grep.txt block D)',
    'domainmodel/SplitRecurringCategory.java:94-96; database/ISplitTransaction.java:36; label_071.grep.txt block D',
    'SOURCE')

UNREACHABLE['SplitRecurringCategory.getTransId'] = ('no_trigger_in_app',
    'no caller: getTransId is not declared on ISplitTransaction, its only definitions are SplitRecurringCategory.java:134 and SplitCategory.java:132, and no call site or auto_calls.json record names it; the repository filters on the TRANSID column constant instead (datalayer/SplitRecurringCategoriesRepository.java:58)',
    'domainmodel/SplitRecurringCategory.java:134-136; domainmodel/SplitCategory.java:132; datalayer/SplitRecurringCategoriesRepository.java:58; label_071.grep.txt block D',
    'SOURCE')

# ================================================================== UNREACHABLE: generated Parceler callbacks the framework never calls here

UNREACHABLE['SplitRecurringCategory$$Parcelable.describeContents'] = ('framework_never_calls',
    'generated describeContents returns 0 (INFERRED from the build class file). No app code calls describeContents (label_071.grep.txt block C: every match is a definition). The framework calls it only inside the Bundle.hasFileDescriptors map walk, which runs when the bundle is unparcelled (Bundle.java:316-336; the call is at line 329). The Intent check that runs on startActivityForResult is in system_server (ActivityStarter.startActivityMayWait, ActivityStarter.java:681-682) and there the extras are still parcelled (mParcelledData is set, Bundle.java:320-321), so no wrapper is asked for its contents; the saved-state check (ActivityManagerService.java:7453) runs after binder parcelling, the same case as batch 062. No auto record names it',
    'FW-SRC services/core/java/com/android/server/am/ActivityStarter.java:672-682; FW-SRC core/java/android/content/Intent.java:6958-6959; FW-SRC core/java/android/os/Bundle.java:316-336, 1215-1220; FW-SRC services/core/java/com/android/server/am/ActivityManagerService.java:7453; label_071.grep.txt blocks C and G',
    'INFERRED')

UNREACHABLE['SplitRecurringCategory$$Parcelable$1.newArray'] = ('framework_never_calls',
    'CREATOR typed-array method. The framework calls it only from Parcel.createTypedArray(Creator) (FW-SRC core/java/android/os/Parcel.java:2640-2645, c.newArray(N) at 2645), that is, when app code reads a typed array of SplitRecurringCategory wrappers. No app code does: the source root has no createTypedArray, writeTypedArray or readTypedArray call (label_071.grep.txt block B), and no auto_calls.json record has newArray as dst. Whether the parceler library calls newArray is INFERRED (library not read)',
    'FW-SRC core/java/android/os/Parcel.java:2640-2645; label_071.grep.txt blocks B and E',
    'INFERRED')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('SplitRecurringCategory.getAccountId', 'EntityBase.getInt'),
    ('SplitRecurringCategory.setAccountId', 'EntityBase.setInt'),
    ('SplitRecurringCategory.getTransId', 'EntityBase.getInt'))

# ---- part 072 (2026-10-29)
# ================================================================== batch 072 (label_072): Stock (26 methods), Stock$$Parcelable (7 methods),
# Stock$$Parcelable$1 (3 methods). Total 36.
# Result: 24 REACHABLE, 12 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_072.md).
# No e() edges and no SCREENS: every REACHABLE route is an auto CALL record (auto_calls.json) whose caller is reached in this batch or another batch.
# This file writes:
#   - UNREACHABLE entries for Stock.create(String,String,String,String), Stock.setPurchaseDate(String) (no reachable caller, SOURCE),
#     and the generated Parceler family (no entry route, INFERRED, D5),
#   - 12 sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch.
# The generated family is evidenced in graphs/MMEX/parts/label_072.grep.txt (sections 1, 3, 4, 7).

# ================================================================== Stock: UNREACHABLE (source evidence)

UNREACHABLE['Stock.create(String,String,String,String)'] = ('no_trigger_in_app',
    'no caller: the Stock.create call sites in app source are the no-arg call at InvestmentTransactionEditActivity.java:109 and the call at Stock.java:63 inside this method; none passes four arguments',
    'domainmodel/Stock.java:62-71; investment/InvestmentTransactionEditActivity.java:109; label_072.grep.txt sections 6, 6b', 'SOURCE')

UNREACHABLE['Stock.setPurchaseDate(String)'] = ('no_trigger_in_app',
    'no reachable caller: its only caller is Stock.create(String,String,String,String) (Stock.java:65), which has no caller; the app source uses the Date overload (Stock.java:49; InvestmentTransactionEditActivity.java:446)',
    'domainmodel/Stock.java:149-151, 65; investment/InvestmentTransactionEditActivity.java:443-446; label_072.grep.txt section 5', 'SOURCE')

# ================================================================== Stock$$Parcelable and $1: UNREACHABLE (generated by Parceler, INFERRED)
# No entry route: Parcels.wrap and unwrap never receive a Stock (label_072.grep.txt section 1), no @Parcel class has a Stock field
# (sections 2, 4), and no class file names Stock$$Parcelable except the two generated classes (section 3). Parceler is a library, not read: INFERRED.

UNREACHABLE['Stock$$Parcelable.<clinit>'] = ('no_trigger_in_app',
    'static initialiser of the generated class: it runs only when the class is first loaded, which needs a Parcels.wrap or unwrap naming Stock (none) or a class file naming the generated class (only the generated pair itself)',
    'domainmodel/Stock.java:36; label_072.grep.txt sections 1, 3, 4; auto_calls.json (Stock$$Parcelable.<clinit> -> Stock$$Parcelable$1.<init>, generated line 23)', 'INFERRED')

UNREACHABLE['Stock$$Parcelable.<init>'] = ('no_trigger_in_app',
    'generated constructor: its only caller is Stock$$Parcelable$1.createFromParcel (auto CALL line 28), which is itself UNREACHABLE; the family is never instantiated',
    'auto_calls.json (Stock$$Parcelable$1.createFromParcel -> Stock$$Parcelable.<init>, generated line 28); label_072.grep.txt sections 1, 3', 'INFERRED')

UNREACHABLE['Stock$$Parcelable.describeContents'] = ('no_trigger_in_app',
    'Parcelable method that the framework calls only on a Stock$$Parcelable instance; no such instance is created, and no call record targets it',
    'domainmodel/Stock.java:36; label_072.grep.txt sections 1, 3, 4; auto_calls.json (no record with this dst)', 'INFERRED')

UNREACHABLE['Stock$$Parcelable.getParcel'] = ('no_trigger_in_app',
    'generated helper that wraps the Stock; no call record targets it, and no Stock$$Parcelable instance is created',
    'label_072.grep.txt sections 1, 3; auto_calls.json (no record with this dst)', 'INFERRED')

UNREACHABLE['Stock$$Parcelable.read'] = ('no_trigger_in_app',
    'called only by Stock$$Parcelable$1.createFromParcel (auto CALL line 28), which is UNREACHABLE; its auto CALL to Stock.<init> (line 78) is cut by sup below',
    'auto_calls.json (Stock$$Parcelable$1.createFromParcel -> Stock$$Parcelable.read, generated line 28; Stock$$Parcelable.read -> Stock.<init>, line 78)', 'INFERRED')

UNREACHABLE['Stock$$Parcelable.write'] = ('no_trigger_in_app',
    'called only by Stock$$Parcelable.writeToParcel (auto CALL line 45), which is UNREACHABLE',
    'auto_calls.json (Stock$$Parcelable.writeToParcel -> Stock$$Parcelable.write, generated line 45)', 'INFERRED')

UNREACHABLE['Stock$$Parcelable.writeToParcel'] = ('no_trigger_in_app',
    'Parcelable callback that the framework calls only on a Stock$$Parcelable instance, which is never created (no Parcels.wrap of Stock); its auto CALL to write is cut by sup below',
    'label_072.grep.txt sections 1, 3; auto_calls.json (generated line 45)', 'INFERRED')

UNREACHABLE['Stock$$Parcelable$1.<init>'] = ('no_trigger_in_app',
    'CREATOR constructor: its only caller is Stock$$Parcelable.<clinit> (auto CALL line 23), which is UNREACHABLE',
    'auto_calls.json (Stock$$Parcelable.<clinit> -> Stock$$Parcelable$1.<init>, generated line 23)', 'INFERRED')

UNREACHABLE['Stock$$Parcelable$1.createFromParcel'] = ('no_trigger_in_app',
    'CREATOR callback: the framework calls it only when a Stock$$Parcelable name is read from a parcel, which needs a Stock parcel (none is written); its auto CALLs to <clinit>, <init> and read (line 28) are cut by sup below',
    'auto_calls.json (generated line 28, three records); label_072.grep.txt sections 1, 3', 'INFERRED')

UNREACHABLE['Stock$$Parcelable$1.newArray'] = ('no_trigger_in_app',
    'CREATOR array factory: the framework calls it only when an array of Stock$$Parcelable is read, and none is written; no call record targets it',
    'label_072.grep.txt sections 1, 3; auto_calls.json (no record with this dst)', 'INFERRED')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('Stock.create(String,String,String,String)', 'Stock.create()'))
sup(('Stock.create(String,String,String,String)', 'Stock.setPurchaseDate(String)'))
sup(('Stock.create(String,String,String,String)', 'Stock.setName'))
sup(('Stock.create(String,String,String,String)', 'Stock.setPurchasePrice'))
sup(('Stock.create(String,String,String,String)', 'Stock.setCurrentPrice'))
sup(('Stock.setPurchaseDate(String)', 'EntityBase.setString'))
sup(('Stock$$Parcelable.<clinit>', 'Stock$$Parcelable$1.<init>'))
sup(('Stock$$Parcelable.writeToParcel', 'Stock$$Parcelable.write'))
sup(('Stock$$Parcelable.read', 'Stock.<init>'))
sup(('Stock$$Parcelable$1.createFromParcel', 'Stock$$Parcelable.<clinit>'))
sup(('Stock$$Parcelable$1.createFromParcel', 'Stock$$Parcelable.<init>'))
sup(('Stock$$Parcelable$1.createFromParcel', 'Stock$$Parcelable.read'))

# ---- part 073 (2026-10-29)
# ================================================================== batch 073 (label_073): StockHistory (5 methods),
# PayeeListFragment (20 methods) and PayeeListFragment$1 to $4 (8 methods): 33 in total (graphs/MMEX/scratch/batches/batch_073.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_073.md.
# Edges written here: the PayeeListFragment routes the framework or the user starts (lifecycle, options menu, loaders, context menu,
# row tap, search box, sort menu), the dialog OK and Cancel listeners, and one judgement cut (sup) on the shared list listener.
# StockHistory has no e() edges: its callers are auto CALL records (auto_calls.json), so none are written here (D7).
# PayeeListFragment$N.<init> and the lambda are auto records (CALL and REGISTER); no edge is written for them here.
# UNREACHABLE: StockHistory.<init>(Parcel) and StockHistory.getHistId, both SOURCE (no caller in the app source root).
# No grep file: neither UNREACHABLE claim depends on a library or generated class.
# Dialog listeners: $1 and $3 are the Cancel bodies, $2 and $4 are the OK bodies. The class files decide this:
# $1 and $3 hold only dialog.cancel(), $2 holds PayeeRepository.delete and restartLoader (and captures payeeId, <init>(PayeeListFragment,int)),
# $4 holds PayeeService.createNew, PayeeService.update and restartLoader.

# ---- lifecycle: PayeeActivity.onCreate adds this fragment (PayeeActivity.java:56-61), then the framework calls onActivityCreated
e('PayeeActivity.onCreate', 'PayeeListFragment.onActivityCreated', 'FRAMEWORK',
  'PayeeActivity.onCreate adds this fragment with a fragment transaction and commits it (lines 56-61); the framework then calls onActivityCreated on it. Same route as AccountListActivity.onCreate to AccountListFragment.onActivityCreated (graph_def.py:929)',
  evidence='SRC final_java_only/MMEX/app/MMEX-#v2024.06.14/app/src/main/java/com/money/manager/ex/PayeeActivity.java:56-61; SRC fragment/PayeeListFragment.java:81; INFERRED androidx FragmentManager calls onActivityCreated after commit (library not read)')

e('PayeeListFragment.onActivityCreated', 'PayeeListFragment.onCreateOptionsMenu', 'FRAMEWORK',
  'onActivityCreated calls setHasOptionsMenu(true) (line 93); the activity then builds its options menu and the framework calls the fragment onCreateOptionsMenu, which this class overrides (line 124). Pattern: AccountListFragment.onActivityCreated (graph_def.py:3752)',
  evidence='SRC fragment/PayeeListFragment.java:93, 124-126; INFERRED androidx options menu dispatch (library not read)')

e('PayeeListFragment.onActivityCreated', 'PayeeListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader (line 114) registers this fragment as the LoaderCallbacks, so the LoaderManager calls onCreateLoader. Pattern: graph_def.py:954',
  evidence='SRC fragment/PayeeListFragment.java:114; INFERRED androidx LoaderManager calls LoaderCallbacks (library not read)')

e('PayeeListFragment.onCreateLoader', 'PayeeListFragment.onLoadFinished', 'FRAMEWORK',
  'the loader delivers its cursor to onLoadFinished when the load completes. Pattern: graph_def.py:958',
  evidence='SRC fragment/PayeeListFragment.java:255-263 (MmxCursorLoader), 274-296; INFERRED androidx Loader delivery (library not read)')

# ---- loader restart: restartLoader (lines 454-456) is called by the sort menu, the search box and the dialog OK buttons
e('PayeeListFragment.restartLoader', 'PayeeListFragment.onCreateLoader', 'FRAMEWORK',
  'restartLoader asks the LoaderManager to restart the loader, which calls onCreateLoader again. Pattern: graph_def.py:2323',
  evidence='SRC fragment/PayeeListFragment.java:454-456; INFERRED androidx LoaderManager (library not read)')

e('PayeeListFragment.restartLoader', 'PayeeListFragment.onLoaderReset', 'FRAMEWORK',
  'the restart destroys the previous loader, which calls onLoaderReset on the callbacks. Pattern: graph_def.py:2331',
  evidence='SRC fragment/PayeeListFragment.java:454-456; INFERRED androidx LoaderManager (library not read)')

# ---- context menu: a plain row tap outside picker mode opens the row menu (line 450)
e('PayeeListFragment.onListItemClick', 'PayeeListFragment.onCreateContextMenu', 'FRAMEWORK',
  'a row tap outside picker mode calls getActivity().openContextMenu(v) (line 450), and the framework then calls onCreateContextMenu. Pattern: AccountListFragment.onListItemClick (graph_def.py:968)',
  evidence='SRC fragment/PayeeListFragment.java:437-452 (openContextMenu at 450); INFERRED Activity.openContextMenu dispatch (framework source not read)')

# ---- dialogs: showDialogDeletePayee (context menu DELETE on an unused payee) and showDialogEditPayeeName (EDIT, FAB)
e('PayeeListFragment.showDialogDeletePayee', 'PayeeListFragment$2.onClick', 'FRAMEWORK',
  'the OK button of the delete dialog: setPositiveButton stores the listener (source lines 339-349) and the framework calls its onClick on a tap. Body: PayeeRepository.delete, Toast, restartLoader. Pattern: label_024.py:10-15',
  evidence='SRC fragment/PayeeListFragment.java:334-349; build class fragment/PayeeListFragment$2.class (constant pool: PayeeRepository, delete, restartLoader, Toast; <init>(PayeeListFragment,int) captures payeeId); INFERRED AlertDialog stores and calls the listener (FW-SRC not read)')

e('PayeeListFragment.showDialogDeletePayee', 'PayeeListFragment$1.onClick', 'FRAMEWORK',
  'the Cancel button of the delete dialog: setNegativeButton stores the listener (lines 350-355) and the framework calls its onClick on a tap. Body: dialog.cancel() only',
  evidence='SRC fragment/PayeeListFragment.java:350-355; build class fragment/PayeeListFragment$1.class (constant pool: cancel only; <init>(PayeeListFragment) captures nothing)')

e('PayeeListFragment.showDialogEditPayeeName', 'PayeeListFragment$4.onClick', 'FRAMEWORK',
  'the OK button of the edit dialog: setPositiveButton stores the listener (lines 375-412) and the framework calls its onClick on a tap. Body: createNew (insert) or update, sendResultToActivity on a PICK intent, restartLoader',
  evidence='SRC fragment/PayeeListFragment.java:375-412; build class fragment/PayeeListFragment$4.class (constant pool: PayeeService createNew and update, restartLoader, access$100, and a reference to the synthetic PayeeListFragment$5 holder); INFERRED AlertDialog stores and calls the listener (FW-SRC not read)')

e('PayeeListFragment.showDialogEditPayeeName', 'PayeeListFragment$3.onClick', 'FRAMEWORK',
  'the Cancel button of the edit dialog: setNegativeButton stores the listener (lines 414-419) and the framework calls its onClick on a tap. Body: dialog.cancel() only',
  evidence='SRC fragment/PayeeListFragment.java:414-419; build class fragment/PayeeListFragment$3.class (constant pool: cancel only)')

# ---- GUI edges from the one screen S_PAYEE (PayeeActivity.onCreate ENTERS it, graph_def.py:144)
gui('S_PAYEE', 'PayeeListFragment.onOptionsItemSelected',
    'Tap Sort by name or Sort by usage in the payee options menu (menu_sort_name, menu_sort_usage), or the Up arrow (android.R.id.home)',
    evidence='SRC fragment/PayeeListFragment.java:147-173; SRC res/menu/menu_payee.xml:30, 33 (ids menu_sort_name, menu_sort_usage); auto_calls PayeeListFragment.onOptionsItemSelected -> restartLoader (line 164); pattern graph_def.py:3777')

gui('S_PAYEE', 'PayeeListFragment.onCreateContextMenu',
    'Long-press a payee row (the list is registered for the context menu at line 104)',
    evidence='SRC fragment/PayeeListFragment.java:104, 177-188; INFERRED long-press on a registered view opens its context menu (Android source not read); pattern graph_def.py:2338')

gui('S_PAYEE', 'PayeeListFragment.onContextItemSelected',
    'Tap Edit, Delete or View transactions in the menu of a payee row',
    evidence='SRC fragment/PayeeListFragment.java:185-187 (menu items), 190-241 (EDIT 213, DELETE 217, VIEW_TRANSACTIONS 232); INFERRED the framework dispatches the chosen item to the fragment; pattern graph_def.py:2341')

gui('S_PAYEE', 'PayeeListFragment.onListItemClick',
    'Tap a payee row: in picker mode the payee is returned to the caller, otherwise the row menu opens',
    evidence='SRC AbsListFragment.java:41-46 (onItemClick calls onListItemClick at 44), 306; SRC fragment/PayeeListFragment.java:437-452; the shared-listener CHA record to this method is cut by sup below; pattern graph_def.py:2691')

gui('S_PAYEE', 'PayeeListFragment.onQueryTextChange',
    'Type in the search box of the payee list',
    evidence='SRC common/BaseListFragment.java:119-130; SRC fragment/PayeeListFragment.java:298-306; auto_calls record BaseListFragment.onPreQueryTextChange@PayeeListFragment -> PayeeListFragment.onQueryTextChange (BaseListFragment.java:226); INFERRED androidx SearchView calls the listener (not in fw_src); pattern graph_def.py:983-984')

# ---- judgement cut (same kind as the batch 026 FAB cut and the batch 046 listener cut): AbsListFragment$1.onItemClick is the
# shared list listener, and its CHA record fans out to every list's onListItemClick, so a tap on another list would reach this method.
# The payee-list route is the gui edge above.
sup(('AbsListFragment$1.onItemClick', 'PayeeListFragment.onListItemClick'))  # auto_calls.json, AbsListFragment.java:44, dispatch cha

# ---- UNREACHABLE: StockHistory (both are SOURCE: no caller in the app source root)
UNREACHABLE['StockHistory.<init>(Parcel)'] = ('no_trigger_in_app',
  'protected Parcel constructor with no caller. The class has no CREATOR and does not implement Parcelable (StockHistory.java:21-61), so no parcel is ever read into a StockHistory. The only object creation in app source is the no-arg new StockHistory() at StockHistoryRepository.java:183',
  'SRC domainmodel/StockHistory.java:50-52; SRC datalayer/StockHistoryRepository.java:183 (no-arg call only); source grep for "StockHistory(" and "StockHistory.CREATOR" in final_java_only app src/main/java finds only the declaration and that call',
  'SOURCE')

UNREACHABLE['StockHistory.getHistId'] = ('no_trigger_in_app',
  'public getter with no caller: the grep of app src/main/java for getHistId finds only its declaration (StockHistory.java:54-56). Nothing calls it, so the value is never read',
  'SRC domainmodel/StockHistory.java:54-56; source grep for getHistId in final_java_only app src/main/java (declaration only)',
  'SOURCE')

# ---- part 074 (2026-10-29)
# ================================================================== batch 074 (label_074): TipsDialogFragment (22 methods),
# TipsDialogFragment$1 (2 methods), TipsDialogFragment$2 (2 methods): 26 in total (graphs/MMEX/scratch/batches/batch_074.txt).
# Rows, printed lines and counts: graphs/MMEX/parts/label_074.md. Result: 26 REACHABLE, 0 UNREACHABLE.
# Every method is reached through the wildcard tip route: BaseListFragment.onStart (lines 100-107) or
# BaseExpandableListFragment.onStart (lines 101-108), gated by the settings state pref_text_search_type false (default true).
# This file writes:
#   - 2 LIFECYCLE edges from the two onStart callers into TipsDialogFragment.onCreate (the framework runs onCreate after show),
#   - the dialog lifecycle edges: onCreate to onCreateDialog, onCreateDialog to onSaveInstanceState,
#   - the two listener edges from onCreateDialog (checkbox and OK), and OK onClick to onDismiss.
# The auto CALL records (getters, setters, show, the listener <init> methods) are not written as edges (D7).
# No gui() edges (the dialog belongs to no single page, D6, D9). No sup pairs (no UNREACHABLE caller). No UNREACHABLE entries.
# No grep file: no library or generated class is UNREACHABLE.

# ---- show: the two onStart callers run the framework's onCreate (show is in the auto CALL records, D7)

e('BaseListFragment.onStart', 'TipsDialogFragment.onCreate', 'LIFECYCLE',
  'the wildcard tip is shown: show (BaseListFragment.java:106) makes the fragment manager run onCreate; show runs super.show only when mCanShow is true (TipsDialogFragment.java:134)',
  guard='mCanShow is true: the lookupswildcard key in PREF_DIALOG is not stored false (TipsDialogFragment.java:68); it is stored false only after the user ticks the do-not-show-again checkbox and taps OK (line 124)',
  needs_state=state_text('pref_text_search_type is false (the text search type switch is off; BaseListFragment.java:97-100; the default is on, preferences_behaviour.xml:52-57) and the wildcard tip is not yet shown (isShowTipsWildcard false, line 100)', ('settings',)),
  evidence='SRC fragment/TipsDialogFragment.java:66-72, 132-135; common/BaseListFragment.java:97-107; res/xml/preferences_behaviour.xml:52-57; INFERRED androidx DialogFragment.show commits a transaction and the fragment manager calls onCreate (library not read)')

e('BaseExpandableListFragment.onStart', 'TipsDialogFragment.onCreate', 'LIFECYCLE',
  'the wildcard tip is shown from the expandable list (category screen): show (BaseExpandableListFragment.java:107) makes the fragment manager run onCreate; show runs super.show only when mCanShow is true (TipsDialogFragment.java:134)',
  guard='mCanShow is true: the lookupswildcard key in PREF_DIALOG is not stored false (TipsDialogFragment.java:68); it is stored false only after the user ticks the do-not-show-again checkbox and taps OK (line 124)',
  needs_state=state_text('pref_text_search_type is false (the text search type switch is off; BaseExpandableListFragment.java:97-101; the default is on, preferences_behaviour.xml:52-57) and the wildcard tip is not yet shown (isShowTipsWildcard false, line 101)', ('settings',)),
  evidence='SRC fragment/TipsDialogFragment.java:66-72, 132-135; common/BaseExpandableListFragment.java:97-108; common/CategoryListFragment.java:111; res/xml/preferences_behaviour.xml:52-57; INFERRED androidx DialogFragment.show commits a transaction and the fragment manager calls onCreate (library not read)')

# ---- the dialog lifecycle (androidx DialogFragment: library not in the dataset, INFERRED)

e('TipsDialogFragment.onCreate', 'TipsDialogFragment.onCreateDialog', 'LIFECYCLE',
  'the framework calls onCreateDialog after onCreate, to build the dialog it shows',
  evidence='SRC fragment/TipsDialogFragment.java:74-87 (onCreate), 89-90 (onCreateDialog); precedent label_023.py line 23; INFERRED androidx DialogFragment (library not read)')

e('TipsDialogFragment.onCreateDialog', 'TipsDialogFragment.onSaveInstanceState', 'LIFECYCLE',
  'the framework saves the fragment state (on rotation, or when the host activity stops) while the dialog is shown; onCreateDialog is the last app callback before that (no onResume override here, unlike AmountInputDialog, graph_def.py:1938)',
  evidence='SRC fragment/TipsDialogFragment.java:89-153 (onCreateDialog 89-130; onSaveInstanceState 145-153); INFERRED androidx FragmentManager saves state through onSaveInstanceState (library not read)')

# ---- the listeners: onCreateDialog stores them, the framework calls them on a change or a tap

e('TipsDialogFragment.onCreateDialog', 'TipsDialogFragment$1.onCheckedChanged', 'FRAMEWORK',
  'the checkbox listener is stored by setOnCheckedChangeListener (line 106); the framework calls onCheckedChanged when the checkbox changes; body setCheckDontShowAgain (line 110)',
  guard='the user ticks or unticks the do-not-show-again checkbox (checkBoxDontShow, visible by default: setVisibleDontShowAgain runs only in the restore branch)',
  evidence='SRC fragment/TipsDialogFragment.java:103-112; res/layout/dialog_tips.xml:51-53; INFERRED Android CompoundButton listener dispatch (framework source not read in this batch)')

e('TipsDialogFragment.onCreateDialog', 'TipsDialogFragment$2.onClick', 'FRAMEWORK',
  'the OK button: setNeutralButton stores the listener (line 119); a tap runs the button handler, which calls onClick (the same dispatch as label_024.py, AlertController.java:125-167)',
  guard='the user taps OK (android.R.string.ok) in the tips dialog (the listener at lines 121-127)',
  evidence='SRC fragment/TipsDialogFragment.java:119-128; auto_calls.json (TipsDialogFragment$2.onClick calls getKey and isCheckDontShowAgain at line 124, no other app callee); precedent label_024.py lines 10-30')

e('TipsDialogFragment$2.onClick', 'TipsDialogFragment.onDismiss', 'FRAMEWORK',
  'dialog.dismiss() (line 126) ends the dialog; the framework calls onDismiss (line 137), which writes the PREF_DIALOG value again (line 140)',
  guard='the OK button was tapped; the dialog is not cancelable (line 118), so OK is the only dismiss route from the user',
  evidence='SRC fragment/TipsDialogFragment.java:118, 126, 137-143; INFERRED androidx DialogFragment dismiss calls onDismiss (library not read)')

# ---- part 076 (2026-10-29)
# ================================================================== batch 076 (label_076)
# Rows, printed lines and counts: graphs/MMEX/parts/label_076.md (32 REACHABLE, 6 UNREACHABLE, 0 INCOMPLETE).
# Grep evidence for the library-based UNREACHABLE rows: graphs/MMEX/parts/label_076.grep.txt (sections 1 and 2).
# This file writes:
#   - 1 FRAMEWORK edge: AllDataListFragment.changeTransactionStatus -> DrawerMenuItemAdapter.getView (the Change status dialog rows);
#   - 9 FRAMEWORK edges: HomeFragment.renderAccountsList -> the HomeAccountsExpandableAdapter callbacks that no auto record reaches
#     (the label_015 pattern: the list view takes the adapter at setAdapter, then the framework calls each callback);
#   - 6 UNREACHABLE entries: DrawerMenuItem.withDivider (SOURCE); DrawerMenuItemRecyclerAdapter.<init> and add (SOURCE);
#     getItemCount, onBindViewHolder, onCreateViewHolder (RecyclerView overrides, INFERRED).
# Not written: CALL edges (D7: every other route is an auto CALL record); GUI edges (S_HOME and S_ALL_DATA are not in SCREENS);
#   sup pairs (D14a: no auto CALL record has an UNREACHABLE caller in this batch; queried auto_calls.json).
# env_text and state_text: only the child-row gate below is inline (D2, no new constants).

# ---- the Change status dialog (batch 021 route): AlertDialog shows the adapter as its row list
e('AllDataListFragment.changeTransactionStatus', 'DrawerMenuItemAdapter.getView', 'FRAMEWORK',
  'the Change status dialog shows the adapter as its row list: setAdapter stores it, the dialog installs it in its ListView, and the list view asks the adapter for each visible row view',
  guard='the dialog is created and shown (AllDataListFragment.java:912-913), so its rows are laid out',
  evidence='SRC common/AllDataListFragment.java:860, 891, 912-913; FW android/app/AlertDialog.java:425, 764; FW com/android/internal/app/AlertController.java:255, 891-892; FW android/widget/AbsListView.java:2335-2365 (obtainView calls mAdapter.getView at 2348, 2365); INFERRED Dialog.show calls onCreate (Dialog.java not read)')

# ---- the home accounts list: renderAccountsList gives the adapter to the expandable list (mExpandableListView.setAdapter, line 814)
e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getGroupView', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the header view of each group',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getGroupCount', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the number of groups',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getGroup', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the group object at each group position',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getGroupId', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the id of each group',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getChildrenCount', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the number of child rows of each group',
  evidence='SRC home/HomeFragment.java:811-814; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

e('HomeFragment.renderAccountsList', 'HomeAccountsExpandableAdapter.getChildId', 'FRAMEWORK',
  'the list view takes the adapter (mExpandableListView.setAdapter, HomeFragment.java:814); the framework then asks the adapter for the id of each child row',
  needs_state=state_text('a child row exists: the account type group holds at least one account (mAccountsByType, HomeAccountsExpandableAdapter.java:77)', ('data',)),
  evidence='SRC home/HomeFragment.java:811-814; SRC home/HomeAccountsExpandableAdapter.java:76-78; INFERRED ExpandableListView and ExpandableListConnector call the adapter (framework source not in fw_src, not read)')

# ---- check-4 EDIT (MMEX B3a+B3b, auditor PASSED 2026-11-01; MMEX-D2)
# Applied by tools/build_graph.py to every edge before ids are made.
# B3a: generated-class bytecode citations (criterion corrected per B3a_RULE.md)
#   -> INFERRED generated <Class> (no source in the upload; bytecode call).
# B3b Part B: FIX_LINES verbatim from merger/check4_fixlines.json (true --emit keys).
# B3b Part A: MmxContentProvider.onCreate :105 -> true new X( lines (true dsts carry .<init>).
# Triple-keyed for B3b so the :105 <clinit> edges (BudgetQuery, QueryBillDeposits) are untouched.
import re as _b3_re
_B3_BYTECODE = _b3_re.compile(r'^SRC (\S+?\.java):(\d+(?:-\d+)?) \(bytecode\)$')
def _b3_generated(_b):
    return (_b == 'DaggerMmxComponent.java' or '$$' in _b
            or _b.endswith('_ViewBinding.java') or _b.endswith('_Factory.java')
            or _b.endswith('_MembersInjector.java')
            or ('_Provide' in _b and _b.endswith('Factory.java')))
_B3_FIXLINES = {
    ('AboutActivity.onCreate', 'AboutTabAdapter.<init>', 'SRC AboutActivity.java:50 (bytecode)'): 'SRC AboutActivity.java:45-50 (bytecode line was 50)',
    ('AccountTransactionListFragment.onCreateLoader', 'MmxCursorLoader.<init>(Context,Uri,Select)', 'SRC AccountTransactionListFragment.java:342 (bytecode)'): 'SRC AccountTransactionListFragment.java:341 (bytecode line was 342)',
    ('AccountTransactionListFragment.populateRunningBalance', 'CalculateRunningBalanceTask2.<init>', 'SRC AccountTransactionListFragment.java:642 (bytecode)'): 'SRC AccountTransactionListFragment.java:641 (bytecode line was 642)',
    ('BaseReportFragment.onCreateLoader', 'MmxCursorLoader.<init>(Context,Uri,Select)', 'SRC BaseReportFragment.java:128 (bytecode)'): 'SRC BaseReportFragment.java:127 (bytecode line was 128)',
    ('BaseReportFragment.onCreateLoader', 'SQLDataSet.<init>', 'SRC BaseReportFragment.java:127 (bytecode)'): 'SRC BaseReportFragment.java:128 (bytecode line was 127)',
    ('BaseReportFragment.onCreateLoader@CategoriesReportFragment', 'MmxCursorLoader.<init>(Context,Uri,Select)', 'SRC BaseReportFragment.java:128 (bytecode)'): 'SRC BaseReportFragment.java:127 (bytecode line was 128)',
    ('BaseReportFragment.onCreateLoader@CategoriesReportFragment', 'SQLDataSet.<init>', 'SRC BaseReportFragment.java:127 (bytecode)'): 'SRC BaseReportFragment.java:128 (bytecode line was 127)',
    ('BaseReportFragment.onCreateLoader@PayeeReportFragment', 'MmxCursorLoader.<init>(Context,Uri,Select)', 'SRC BaseReportFragment.java:128 (bytecode)'): 'SRC BaseReportFragment.java:127 (bytecode line was 128)',
    ('BaseReportFragment.onCreateLoader@PayeeReportFragment', 'SQLDataSet.<init>', 'SRC BaseReportFragment.java:127 (bytecode)'): 'SRC BaseReportFragment.java:128 (bytecode line was 127)',
    ('MmexApplication.initializeDependencyInjection', 'MmxModule.<init>', 'SRC MmexApplication.java:202 (bytecode)'): 'SRC MmexApplication.java:203 (bytecode line was 202)',
    ('MmxContentProvider.onCreate', 'AccountRepository.<init>', 'SRC MmxContentProvider.java:105 (bytecode)'): 'SRC MmxContentProvider.java:106 (bytecode line was 105)',
    ('MmxContentProvider.onCreate', 'AccountTransactionRepository.<init>', 'SRC MmxContentProvider.java:105 (bytecode)'): 'SRC MmxContentProvider.java:107 (bytecode line was 105)',
    ('SearchParametersFragment.assembleWhereClause', 'MmxDate.<init>(Date)', 'SRC SearchParametersFragment.java:465 (bytecode)'): 'SRC SearchParametersFragment.java:466 (bytecode line was 465)',
}
_B3_PARTA = {
    'AttachmentRepository.<init>': 114,
    'BudgetEntryRepository.<init>': 108,
    'BudgetQuery.<init>': 125,
    'BudgetRepository.<init>': 109,
    'CategoryRepository.<init>': 110,
    'CurrencyRepository.<init>': 111,
    'PayeeRepository.<init>': 113,
    'QueryAccountBills.<init>': 120,
    'QueryAllData.<init>': 122,
    'QueryBillDeposits.<init>': 123,
    'QueryCategorySubCategory.<init>': 121,
    'QueryReportIncomeVsExpenses.<init>': 124,
    'RecurringTransactionRepository.<init>': 115,
    'SQLDataSet.<init>': 127,
    'SplitCategoriesRepository.<init>': 116,
    'SplitRecurringCategoriesRepository.<init>': 117,
    'StockHistoryRepository.<init>': 119,
    'StockRepository.<init>': 118,
    'ViewMobileData.<init>': 126,
}
def EDIT(x):
    _ev = x.get('evidence') or ''
    _key = (x.get('src'), x.get('dst'), _ev)
    if _key in _B3_FIXLINES:
        x['evidence'] = _B3_FIXLINES[_key]
        return
    if x.get('src') == 'MmxContentProvider.onCreate' and _ev == 'SRC MmxContentProvider.java:105 (bytecode)' and x.get('dst') in _B3_PARTA:
        x['evidence'] = 'SRC MmxContentProvider.java:%d (bytecode)' % _B3_PARTA[x['dst']]
        return
    _m = _B3_BYTECODE.match(_ev)
    if _m:
        _base = _m.group(1).split('/')[-1]
        if _b3_generated(_base):
            x['evidence'] = 'INFERRED generated %s (no source in the upload; bytecode call)' % _base[:-5]

# ---- graph_def_mod loader (handoff/connector_kit/split_graph_def.py)
# The rest of this graph is in graph_def_mod/NN.py (each file below 1 MB, so the GitHub connector can read and write it).
# The modules run in name order, in this same namespace, exactly as if they were one file. GDIR is set by tools/build_graph.py.
import os as _gdmod_os
for _gdmod_name in sorted(_gdmod_os.listdir(_gdmod_os.path.join(GDIR, 'graph_def_mod'))):
    if _gdmod_name.endswith('.py'):
        _gdmod_path = _gdmod_os.path.join(GDIR, 'graph_def_mod', _gdmod_name)
        exec(compile(open(_gdmod_path, encoding='utf-8').read(), _gdmod_path, 'exec'))
del _gdmod_os, _gdmod_name, _gdmod_path


# ---- W2 REAUDIT: baseline and setup-only screens (appended after the
# graph_def_mod loader, so EDIT below wraps the effective EDIT) ----
# Baseline for MMEX: one checking account exists (the setup account); every
# setting is at its default. Baseline state never counts as state, so the
# gates the baseline already satisfies are cleared in EDIT below, with the
# reason recorded in the edge note. The first-run tutorial page goes into
# SETUP_ONLY (it is shown before the app actually runs, MainActivity.java:
# 1478-1482); its gate text itself is kept. Per-gate decisions and source
# evidence: graphs/MMEX/scratch/reaudit/state_gates.csv.
SETUP_ONLY = {'S_TUTORIAL'}

_W2_CLEARED = {
    'at least one account exists, so the account list shows rows (HomeFragment.java:793), and the row group is expanded (group expansion is saved in settings, HomeFragment.java:719 and 731)':
        'baseline: one checking account exists, so the account rows show, and account groups are expanded by default (HomeFragment.java:793; HomeFragment.java:754)',
    'at least one account exists, so the group headers are shown (HomeFragment.java:793), and the group is expanded (its saved setting is true, HomeFragment.java:754)':
        'baseline: one checking account exists, so the group headers show, and account groups are expanded by default (HomeFragment.java:793; HomeFragment.java:754)',
    'at least one account exists, so the group headers are shown (HomeFragment.java:793), and the group is collapsed (its saved setting is false, HomeFragment.java:719)':
        'baseline: one checking account exists, so the group headers show; collapsing a group is a tap on its header on the same screen (HomeFragment.java:793; HomeFragment.java:710)',
    'a child row exists: the account type group holds at least one account (mAccountsByType, HomeAccountsExpandableAdapter.java:77)':
        'baseline: the setup checking account sits in its account-type group, so that group holds at least one account and has a child row (HomeAccountsExpandableAdapter.java:76-77)',
    'the quote provider setting is YahooYql (the default when the setting is unset)':
        'baseline: the quote provider is unset in a fresh database, and the unset default is YahooYql (InvestmentSettings.java:75; InvestmentSettings.java:79-80)',
    'the repeating transaction notifications setting is on (default on, BehaviourSettings.java:42)':
        'baseline: the repeating transaction notifications setting defaults to on (BehaviourSettings.java:41-42)',
    'sync is enabled and the sync interval is above 0 (SyncSchedulerBroadcastReceiver.java:76, 82)':
        'baseline: sync defaults to enabled with a 30-minute interval (SyncPreferences.java:58; SyncPreferences.java:62)',
}
_W2_ORIG_EDIT = EDIT


def EDIT(x):
    _W2_ORIG_EDIT(x)
    _t = x.get('needs_state')
    if _t in _W2_CLEARED:
        x['needs_state'] = None
        x['state_kinds'] = []
        x['note'] = ((x.get('note') + ' | ') if x.get('note') else '') + _W2_CLEARED[_t]


# ---- W4 REAUDIT (Kiro): rapid type analysis for bytecode cha edges (brief W1 T2) ----
RTA = True


# ---- W4 REAUDIT (Kiro): MMEX-03, showFragment_Internal cloned per caller ----
# MainActivity.showFragment_Internal (MainActivity.java:1446-1466) commits the fragment its caller passed. Only the
# drawer case R.id.menu_account (MainActivity.java:633-634; drawer child item at 863-866) passes an AccountListFragment
# (created by showFragment(Class) with newInstance, line 743), so the edge to AccountListFragment.onActivityCreated is
# moved onto an @ACCOUNTS copy of the helper chain, as was done for @RECURRING (graph_def_mod/03.py). The
# AccountListActivity route (an exported entry) keeps its own edge (AccountListActivity.java:47-55).
e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'MainActivity.showFragment(Class)@ACCOUNTS', 'CALL',
  'the Accounts drawer case calls showFragment(AccountListFragment.class)',
  guard='item id == R.id.menu_account',
  evidence='SRC home/MainActivity.java:633-634 (case; showFragment call)')
e('MainActivity.showFragment(Class)@ACCOUNTS', 'MainActivity.showFragment(Fragment)@ACCOUNTS', 'CALL',
  'showFragment(Class) creates (or finds) the account-list fragment and shows it via showFragment(Fragment)',
  guard='fragmentClass != null AND resulting fragment != null',
  evidence='SRC home/MainActivity.java:734-752 (null guard 735; newInstance 743; showFragment(fragment) 751)')
e('MainActivity.showFragment(Fragment)@ACCOUNTS', 'MainActivity.showFragment(Fragment,String)@ACCOUNTS', 'CALL',
  'showFragment(Fragment) shows the fragment with its class name as tag',
  evidence='SRC home/MainActivity.java:758-759')
e('MainActivity.showFragment(Fragment,String)@ACCOUNTS', 'MainActivity.showFragment_Internal@ACCOUNTS', 'CALL',
  'showFragment(Fragment,String) shows the fragment via showFragment_Internal',
  evidence='SRC home/MainActivity.java:768-770 (showFragment_Internal call 770)')
e('MainActivity.showFragment_Internal@ACCOUNTS', 'AccountListFragment.onActivityCreated', 'FRAMEWORK',
  'the Accounts drawer item reaches showFragment_Internal with the account-list fragment, which replaces fragmentMain and commits; the framework then calls onActivityCreated',
  guard='fragment not already added',
  evidence='SRC home/MainActivity.java:1446-1466 (not-added guard 1448; replace 1462; commit 1466); SRC home/MainActivity.java:633-634; INFERRED androidx FragmentManager calls onActivityCreated after the commit (library not read)')


# ---- W5 REAUDIT (Kiro): library inherits through reflective creation (brief W1 T3) ----
ESR_CREATION = True

# W5 (Kiro): edges a library or reflection makes, set to non_standard (decisions: graphs/MMEX/scratch/reaudit/library_edges.csv)
_W5_NONSTD = {
    ('CalculatorActivity.onCreate', 'RobotoButton.<init>(Context,AttributeSet)', 'FRAMEWORK'):
        'XML inflation: LayoutInflater builds this view from its XML tag through the (Context, AttributeSet) constructor (layout XML cited in the evidence)',
    ('SearchParametersFragment.onCreateView', 'RobotoCheckBox.<init>(Context,AttributeSet)', 'FRAMEWORK'):
        'XML inflation: LayoutInflater builds this view from its XML tag through the (Context, AttributeSet) constructor (layout XML cited in the evidence)',
}
_W5_ORIG_EDIT = globals().get('EDIT')


def EDIT(x):
    if _W5_ORIG_EDIT:
        _W5_ORIG_EDIT(x)
    _via = _W5_NONSTD.get((x['src'], x['dst'], x['kind']))
    if _via and x.get('edge_class') != 'non_standard':
        x['edge_class'] = 'non_standard'
        x['via'] = _via


# ---- W6 REAUDIT (Kiro): outside data the route consumes ----
# Each entry puts an env gate on the edge that consumes data from outside the app; decisions and the
# pattern sweep: graphs/MMEX/scratch/reaudit/outside_data.csv.
_W6_ENV = {
    ('YqlSecurityPriceUpdaterRetrofit.downloadPrices', 'YqlSecurityPriceUpdaterRetrofit$1.onResponse', 'FRAMEWORK'):
        ('network: the Yahoo YQL price server answers the Retrofit request (yql.getPrices(query).enqueue, YqlSecurityPriceUpdaterRetrofit.java:89-103)', ['network']),
    ('DatabaseSettingsFragment.requestBackup', 'DatabaseSettingsFragment.onActivityResult', 'RESULT'):
        ('other_app: the system document creator returns the backup file location (ACTION_CREATE_DOCUMENT, DatabaseSettingsFragment.java:213-218)', ['other_app']),
}
_W6_ORIG_EDIT = globals().get('EDIT')


def EDIT(x):
    if _W6_ORIG_EDIT:
        _W6_ORIG_EDIT(x)
    _g = _W6_ENV.get((x['src'], x['dst'], x['kind']))
    if _g and not x.get('env'):
        x['env'], x['env_kinds'] = _g[0], list(_g[1])
# W6 (Kiro), network and servers: rules matched on the edge (decisions in outside_data.csv).
_W6_RULES = [
    ('YahooCsvQuoteDownloaderRetrofit.downloadPrices', 'YahooCsvQuoteDownloaderRetrofit$1.onResponse', 'FRAMEWORK',
     'network: the Yahoo CSV quote server answers the Retrofit request (service.getPrice(symbol).enqueue, YahooCsvQuoteDownloaderRetrofit.java:70-84)', ['network']),
    ('FixerService.downloadPrices', 'FixerService$1.onResponse', 'FRAMEWORK',
     'network: the Fixer exchange-rate server answers the Retrofit request (service.getPrices(...).enqueue, FixerService.java:78-93)', ['network']),
    ('FixerService.downloadPrices', 'FixerService$1.onFailure', 'FRAMEWORK',
     'network: the exchange-rate request is sent and fails before a response (no connection, timeout or server error; FixerService.java:83-93)', ['network']),
    ('MmxOpenHelper.getReadableDatabase', 'MmxOpenHelper.onUpgrade', 'CALL',
     'data only an older app version writes: a database file with an older schema version; SQLiteOpenHelper calls onUpgrade only when the stored version is lower (MmxOpenHelper.onUpgrade; FW-SRC core/java/android/database/sqlite/SQLiteOpenHelper.java:354-365)', ['other']),
]
_W6B_ORIG_EDIT = globals().get('EDIT')


def EDIT(x):
    if _W6B_ORIG_EDIT:
        _W6B_ORIG_EDIT(x)
    if x.get('env'):
        return
    for _src, _dst, _kind, _text, _kinds in _W6_RULES:
        if x['kind'] == _kind and x['src'].split('@')[0] == _src and x['dst'].split('@')[0] == _dst:
            x['env'], x['env_kinds'] = _text, list(_kinds)
            return


# ---- W7 REAUDIT (Kiro), round 1: guard decisions written on the edges ----
# Decisions and the pre-screen: graphs/MMEX/scratch/reaudit/guard_decisions.csv and guard_steps.csv
# (tools_dev/guard_prescreen.py). Each entry: (src, dst, kind) -> (needs_state text, kinds).
_W7_STATE = {
    ('S_PAYEE_REPORT', 'PieChartFragment.onValueSelected', 'GUI'):
        ('the payee report has at least one row: transactions with payees exist (showChart returns early when the adapter, its cursor or its first row is missing, PayeeReportFragment.java:216-221)', ['data']),
    ('CheckingTransactionEditActivity.handleIntent', 'CheckingTransactionEditActivity.loadScheduledTransaction', 'CALL'):
        ('a recurring (scheduled) transaction exists and its id comes with the ACTION_INSERT intent (KEY_BDID_ID > NOT_SET, CheckingTransactionEditActivity.java:494-497)', ['data']),
    ('InvestmentTransactionEditActivity.save', 'StockRepository.insert', 'CALL'):
        ('a new stock is saved in the portfolio of an Investment account: an Investment account exists (the baseline has one checking account) and the stock has no id yet (InvestmentTransactionEditActivity.java:429-434)', ['data']),
}
_W7_ORIG_EDIT = globals().get('EDIT')


def EDIT(x):
    if _W7_ORIG_EDIT:
        _W7_ORIG_EDIT(x)
    _g = _W7_STATE.get((x['src'], x['dst'], x['kind']))
    if _g and not x.get('needs_state'):
        x['needs_state'], x['state_kinds'] = _g[0], list(_g[1])


# ---- W7 REAUDIT (Kiro), round 2: judged guard steps ----
# Each STATE or ENV row of scratch/reaudit/w7_judged.csv (written with tools_dev/guard_judge.py from the printed
# source, tools_dev/guard_print.py) puts its gate on every edge with the same src, dst and kind that has no gate of
# that type yet (only edges whose trigger contains the row's match text, when it has one). NONE and DEAD rows change nothing here (DEAD rows get their UNREACHABLE entries by hand).
import csv as _w7j_csv
import os as _w7j_os
_W7J = {}
_w7j_path = _w7j_os.path.join(GDIR, 'scratch', 'reaudit', 'w7_judged.csv')
if _w7j_os.path.exists(_w7j_path):
    for _r in _w7j_csv.DictReader(open(_w7j_path, encoding='utf-8')):
        if _r['decision'] in ('STATE', 'ENV'):
            _W7J.setdefault((_r['src'], _r['dst'], _r['kind']), []).append(
                (_r['decision'], _r['text'], [k for k in _r['kinds'].split('+') if k], _r.get('match') or ''))
_W7J_ORIG_EDIT = EDIT


def EDIT(x):
    _W7J_ORIG_EDIT(x)
    for _g in _W7J.get((x['src'], x['dst'], x['kind']), ()):
        if _g[3] and _g[3] not in (x.get('trigger') or ''):
            continue
        if _g[0] == 'STATE' and not x.get('needs_state'):
            x['needs_state'], x['state_kinds'] = _g[1], list(_g[2])
        elif _g[0] == 'ENV' and not x.get('env'):
            x['env'], x['env_kinds'] = _g[1], list(_g[2])
# W7 round 2 (and a W3 miss): the four home-screen widget receivers are started only by the launcher's AppWidget host
# (APPWIDGET_UPDATE, AndroidManifest.xml widget receivers); their ENTRY edges had no env gate, so 385 best routes into
# CheckingTransactionEditActivity started there instead of in the app (the app's own add button reaches it too).
_W7_WIDGET_ORIG_EDIT = EDIT


def EDIT(x):
    _W7_WIDGET_ORIG_EDIT(x)
    if (x['kind'] == 'ENTRY' and x['src'] == 'S_ENTRY' and x['dst'] in (
            'ButtonAddTransactionWidgetProvider.<init>', 'AccountBillsWidgetProvider.<init>',
            'SummaryWidgetProvider.<init>', 'SingleAccountWidget.<init>') and not x.get('env')):
        x['env'] = ('outside package: the user adds the MMEX widget to the home screen, and the launcher\'s AppWidget host '
                    'sends APPWIDGET_UPDATE to the widget receiver (AndroidManifest.xml widget receivers)')
        x['env_kinds'] = ['other_app']
# W8 re-verification (found on the DatabaseMetadataFactory.getInstance route): every variant of
# SyncManager.invokeSyncService returns at once unless the current database has a remote file
# (SyncManager.java:188-192), which only a database opened from a cloud document provider has. The W7 pre-screen
# listed only the @SYNC variant; the gate now sits on every invokeSyncService variant's outgoing steps.
_W8_SYNC_ORIG_EDIT = EDIT
_W8_REMOTE = ('outside package: the database was opened from a cloud document provider (the recent-database entry has '
              'a remote file, SyncManager.java:188-192), and the provider is reachable')


def EDIT(x):
    _W8_SYNC_ORIG_EDIT(x)
    if x['src'].startswith('SyncManager.invokeSyncService@') and not x.get('env'):
        x['env'], x['env_kinds'] = _W8_REMOTE, ['other_app', 'network']
# Review 2 fix 3 (Kiro): the shared list listener AbsListFragment$1.onItemClick is entered only from the account list
# (S_ACCOUNT_LIST), and it dispatches to the fragment that owns the list (AbsListFragment.java:42-45). Its CHA fan-out to
# the other lists' onListItemClick let an account-row tap reach BudgetListFragment (58 routes, the DbModule route of the
# W8 sample). Same judgement cut as the payee list above: each of those lists reaches its own onListItemClick through
# its own page edge. Those page edges get the row their list needs.
sup(('AbsListFragment$1.onItemClick', 'BudgetListFragment.onListItemClick'),
    ('AbsListFragment$1.onItemClick', 'PayeeReportFragment.onListItemClick'),
    ('AbsListFragment$1.onItemClick', 'RecurringTransactionListFragment.onListItemClick'),
    ('AbsListFragment$1.onItemClick', 'CategoriesReportFragment.onListItemClick'),
    ('AbsListFragment$1.onItemClick', 'CurrencyListFragment.onListItemClick'),
    ('AbsListFragment$1.onItemClick', 'AbsListFragment.onListItemClick'))
_R2_ROWS_ORIG_EDIT = EDIT
_R2_ROWS = {
    'S_RECURRING_LIST': ('a recurring transaction exists (a row of the recurring list); the baseline has none', 'data'),
    'S_PAYEE_REPORT': ('a payee with transactions exists (a row of the payee report); the baseline has none', 'data'),
    'S_CATEGORIES_REPORT': ('transactions with categories exist (a row of the categories report); the baseline account has no transactions', 'data'),
}


def EDIT(x):
    _R2_ROWS_ORIG_EDIT(x)
    if x['kind'] == 'GUI' and x['src'] in _R2_ROWS and x['dst'].endswith('.onListItemClick') and not x.get('needs_state'):
        x['needs_state'], x['state_kinds'] = _R2_ROWS[x['src']][0], [_R2_ROWS[x['src']][1]]

# ---- Review 6 fix 1 (Kiro, 2026-11-07): gates on the routes the build actually uses ----
# (a) SearchActivity.handleSearchRequest does anything only when the intent carries EXTRA_SEARCH_PARAMETERS
# (SearchActivity.java:151-162). Only the Search item of a category row (CategoryListFragment.java:732-737), the
# category and payee reports (CategoriesReportFragment.java:381, PayeeReportFragment.java:319), the payee list
# (PayeeListFragment.java:237-238 through IntentFactory.getSearchIntent) and the income/expense report
# (IncomeVsExpensesListFragment.java:391-392) pass it; the search menu and the drawer pass none. Those callers now
# start the SearchActivity@PARAMS variant, and every step out of handleSearchRequest starts at its @PARAMS variant,
# so the plain search page no longer reaches setSearchParameters, performSearch or the parcel reads.
_R6_PARAMS = 'SearchActivity.<init>@PARAMS'
for _s, _ref in (('CategoryListFragment.showSearchActivityFor', 'common/CategoryListFragment.java:732-737'),
                 ('CategoriesReportFragment.showSearchActivityFor', 'reports/CategoriesReportFragment.java:378-383'),
                 ('PayeeReportFragment.showSearchActivityFor', 'reports/PayeeReportFragment.java:316-321')):
    e(_s, _R6_PARAMS, 'INTENT', 'the Search item starts SearchActivity with the search parameters (EXTRA_SEARCH_PARAMETERS)',
      evidence='SRC %s (putExtra EXTRA_SEARCH_PARAMETERS, startActivity)' % _ref)
e(_R6_PARAMS, 'SearchActivity.onCreate@PARAMS', 'LIFECYCLE', 'the framework calls onCreate after it creates the activity instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2722-2731 (callActivityOnCreate)')
e('SearchActivity.onCreate@PARAMS', 'SearchActivity.handleSearchRequest@PARAMS', 'CALL',
  'onCreate reads the search request of the intent; this intent carries search parameters',
  evidence='SRC search/SearchActivity.java:69, 151-162')
e('SearchActivity.onCreate', 'SearchActivity.handleSearchRequest', 'CALL', 'onCreate reads the search request of the intent',
  evidence='SRC search/SearchActivity.java:69')  # the plain call (the hand variant above makes the builder skip the bytecode copy)
_R6_PARAMS_RETARGET = {('PayeeListFragment.onContextItemSelected', 'SearchActivity.<init>', 'INTENT'),
                       ('IncomeVsExpensesListFragment$4.onItemClick', 'SearchActivity.<init>', 'INTENT')}
# (b) MainActivity.populateScheduledTransactions: the loop over due recurring transactions (MainActivity.java:1262-1281)
# runs only when one is due; some of its bytecode steps had no gate (the W7 row E00ecbc65 had deferred it to them).
_R6_DUE = ('a recurring transaction is due (DAYSLEFT <= 0) and the repeating-transaction notification is on (default on); '
           'the baseline has no recurring transactions (MainActivity.java:1236-1262)')
import re as _r6_re
_R6_ORIG_EDIT = EDIT


def EDIT(x):
    _R6_ORIG_EDIT(x)
    if (x['src'], x['dst'], x['kind']) in _R6_PARAMS_RETARGET:
        x['dst'] = _R6_PARAMS
    if x['src'] == 'SearchActivity.handleSearchRequest':
        x['src'] = 'SearchActivity.handleSearchRequest@PARAMS'
    if (x['src'], x['dst']) == ('RecurringTransactionListFragment.onLoadFinished', 'AllDataAdapter.newView') and not x.get('needs_state'):
        # (c) the recurring list makes a row view only for a stored recurring transaction, as its bindView step says
        x['needs_state'], x['state_kinds'] = ('a recurring transaction exists: the recurring list makes a row view only for a '
                                              'stored recurring transaction (RecurringTransactionListFragment.onLoadFinished); '
                                              'the baseline has none'), ['data']
    if x['src'] == 'MainActivity.populateScheduledTransactions' and not x.get('needs_state'):
        _m = _r6_re.search(r'MainActivity\.java:(\d+)', x.get('evidence') or '')
        if _m and 1262 <= int(_m.group(1)) <= 1281:
            x['needs_state'], x['state_kinds'] = _R6_DUE, ['data']
# W7 r6-p19 DEAD steps (Ee74e5fb3, E0676831e and the handleIntent setters): the checking editor's transactionEntity is always an
# AccountTransaction (AccountTransaction.create() at CheckingTransactionEditActivity.java:99, AccountTransactionRepository at :390-394,
# its own parcel at :649), so the calls on it in onCreate and handleIntent never dispatch to RecurringTransaction. Only these
# callers are cut; loadScheduledTransactionInternal really reads a RecurringTransaction (:431-450) and keeps its edges.
for _m in ('setAccountId', 'getAccountId', 'getAccountToId', 'setCategoryId', 'getPayeeId', 'setPayeeId', 'setDate', 'setNotes',
           'setTransactionNumber', 'setAmount', 'setTransactionType', 'setAmountTo', 'getAmount', 'setAccountToId', 'setStatus', 'getStatus'):
    sup(('CheckingTransactionEditActivity.handleIntent', 'RecurringTransaction.' + _m))
for _m in ('setCategoryId', 'setPayeeId', 'getPayeeId'):
    sup(('CheckingTransactionEditActivity.lambda$handleIntent$1', 'RecurringTransaction.' + _m))
sup(('CheckingTransactionEditActivity.onCreate', 'RecurringTransaction.getTransactionType'),
    ('CheckingTransactionEditActivity.onCreate@FRAG', 'RecurringTransaction.getTransactionType'))
# W7 r6-p21 DEAD step Eec0a63c9: duplicateTransaction (ACTION_PASTE, after loadTransaction) resets the ids of the splits that
# loadTransaction read through SplitCategoriesRepository (CheckingTransactionEditActivity.java:397-399), which are SplitCategory
# objects, so the call never dispatches to SplitRecurringCategory.
sup(('CheckingTransactionEditActivity.duplicateTransaction', 'SplitRecurringCategory.setId'))
# W7 r6-p25 DEAD step E33a348fe: the Categories report's category branch runs only for a menu item with a negative id
# (CategoriesReportFragment.java:167), and no menu in the app adds one (resource ids, MenuHelper ids from 2, ContextMenuIds 1-9).
sup(('CategoriesReportFragment.onOptionsItemSelected', 'BaseReportFragment.getWhereClause'))
# W7 r6-p26 step E4e937842, re-judged after the review of f06dcbb2 (item 4, Q-R6-5): initBaseCurrency runs from every onCreate
# (MmxOpenHelper.java:98-99). A new database made in the app has no BASECURRENCYID row (tables_v1.sql inserts only DATAVERSION),
# but a database file made by the desktop app and opened through Open database can reach onCreate (user_version 0; executeRawSql
# swallows the errors of each create statement, MmxOpenHelper.java:169-189) with a base currency row already there, so the update
# branch (:300-302) runs. The edge carries that outside-file gate instead of being cut.
e('MmxOpenHelper.initBaseCurrency', 'InfoService.updateRaw(SupportSQLiteDatabase,int,String,Integer)', 'CALL', 'Direct call',
  env=env_text('a database file made by the desktop app, with a base currency row, opened through Open database', ('other_app',)),
  evidence='SRC database/MmxOpenHelper.java:302 (bytecode)')
# W7 r6-p30 DEAD step E5a1dd2c0: CurrencyListActivity.onCreate checks mPreviousOrientation on a fragment it has just made
# (CurrencyListActivity.java:50-56), and the field starts at NOT_SET (CurrencyListFragment.java:76), so the branch never runs.
sup(('CurrencyListActivity.onCreate', 'ActivityUtils.forceCurrentOrientation'))
# W7 r6-p31/p32 DEAD steps: RepositoryBase.first(Class,...) makes the class it is given (RepositoryBase.java:100-111), and the app
# passes only Account, AccountTransaction, Attachment, Budget, BudgetEntry, Category, Payee and Stock (grep of first(X.class);
# CurrencyRepository and StockHistoryRepository read their rows through their own queries). The CHA copies into the other
# loadFromCursor overrides never run.
for _c in ('AccountTransactionDisplay', 'IncomeVsExpenseReportEntity', 'SplitCategory', 'SplitRecurringCategory', 'StockHistory', 'Currency'):
    sup(('RepositoryBase.first', _c + '.loadFromCursor'))
# W7 review of f06dcbb2, item 2 (Q-R6-4 answered): the release-only loggers, labelled as AnkiDroid's ProductionCrashReportingTree.
# Their hand edges are dropped by _r7_filter_edge near the top; the auto copies are suppressed here.
sup(('MmexApplication.onCreate', 'ScreenTree.<init>'), ('MmexApplication.onCreate', 'SysLogTree.<init>'), 'ScreenTree.log', 'SysLogTree.log')
for _m in ('ScreenTree.<init>', 'ScreenTree.log', 'SysLogTree.<init>', 'SysLogTree.log'):
    UNREACHABLE[_m] = (
        'closed_by_configuration', 'the tree is planted only in the else branch of BuildConfig.DEBUG (MmexApplication.java:134-140); '
        'the dataset APK is the instrumented debug build (DATASET.txt), so BuildConfig.DEBUG is true and the else branch never runs',
        'SRC MmexApplication.java:134-140', 'SOURCE')
