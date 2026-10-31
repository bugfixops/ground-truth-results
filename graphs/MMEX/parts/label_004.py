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
e('MainActivity.onDrawerMenuAndOptionMenuSelected', 'AboutActivity.<init>', 'INTENT',
  'case R.id.menu_about: startActivity(new Intent(MainActivity.this, AboutActivity.class))',
  gui=['Open the navigation drawer and tap About'],
  evidence='SRC home/MainActivity.java:688-690; SRC home/MainActivity.java:975-978; SRC home/MainActivity.java:1118-1120')

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
