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
  evidence='SRC home/MainActivity.java:252-260; SRC core/Passcode.java:70-72; FW-SRC core/java/android/app/Instrumentation.java:1143-1148')

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
