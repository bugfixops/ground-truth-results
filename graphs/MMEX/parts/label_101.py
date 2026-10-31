# batch 101 (label_101): RecurringTransactionEditActivity_MembersInjector (5 methods: <init>, create, injectDatabase, injectDateUtils, injectMembers)
# and RecurringTransactionListActivity (4 methods: <clinit>, <init>, onActivityResult, onCreate). 9 methods in all.
# Rows and printed source lines: graphs/MMEX/parts/label_101.md. Grep and record output: graphs/MMEX/parts/label_101.grep.txt.
# CALL edges between batch methods and to other classes come from auto_calls.json. The injectDatabase and injectDateUtils
# records from DaggerMmxComponent (DaggerMmxComponent.java:418-419) are already there, so no edges are written for them (D7).
# The Dagger-generated MembersInjector class is not in the app source and its methods are INFERRED.
# PendingIntent.java is not in fw_src (grep section 7), so the notification tap route is INFERRED.

SCREENS.update({
    'S_RECURRING_LIST': 'Recurring transactions list (RecurringTransactionListActivity with RecurringTransactionListFragment): the scheduled bills and deposits; the only in-app start site is the due-bill notification (grep section 5)',
})

# ---- route from the due-bill notification (posted by RecurringTransactionNotifications.showNotification)
e('RecurringTransactionNotifications.showNotification', 'RecurringTransactionListActivity.<clinit>', 'INTENT',
  'the user taps the due-bill notification: the PendingIntent built in showNotification starts RecurringTransactionListActivity, and the class is initialised',
  env=env_text('the user taps the recurring transaction notification (the activity is started with INTENT_EXTRA_LAUNCH_NOTIFICATION)', ('system_event',)),
  needs_state=state_text('a due bill exists: the query at RecurringTransactionNotifications.java:68-78 returns a row, and the notification setting is on (MainActivity.java:1236-1237 gates the poster)', ('data', 'settings')),
  evidence='SRC RecurringTransactionNotifications.java:75-78 and 90-94; SRC RecurringTransactionListActivity.java:38 (static FRAGMENTTAG initialiser); FW-SRC core/java/android/app/Instrumentation.java:1143-1148 (clazz.newInstance); INFERRED PendingIntent.getActivity delivers the Intent (PendingIntent.java not in fw_src)')

e('RecurringTransactionNotifications.showNotification', 'RecurringTransactionListActivity.<init>', 'INTENT',
  'the framework creates the RecurringTransactionListActivity instance from the notification PendingIntent (no intent-filter, not exported)',
  env=env_text('the user taps the recurring transaction notification (the activity is started with INTENT_EXTRA_LAUNCH_NOTIFICATION)', ('system_event',)),
  needs_state=state_text('a due bill exists: the query at RecurringTransactionNotifications.java:68-78 returns a row, and the notification setting is on (MainActivity.java:1236-1237 gates the poster)', ('data', 'settings')),
  evidence='SRC RecurringTransactionNotifications.java:90-94; SRC AndroidManifest.xml:235 (no intent-filter); SRC RecurringTransactionListActivity.java:33; FW-SRC core/java/android/app/Instrumentation.java:1143-1148 (clazz.newInstance); INFERRED PendingIntent.getActivity delivers the Intent (PendingIntent.java not in fw_src)')

# ---- framework lifecycle and the list screen
e('RecurringTransactionListActivity.<init>', 'RecurringTransactionListActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor (callActivityOnCreate, then performCreate)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2728-2731 (callActivityOnCreate); FW-SRC core/java/android/app/Instrumentation.java:1212-1215 (performCreate); FW-SRC core/java/android/app/Activity.java:989-990 (onCreate); SRC RecurringTransactionListActivity.java:43')

e('RecurringTransactionListActivity.onCreate', 'S_RECURRING_LIST', 'ENTERS',
  'the recurring transactions list is shown: onCreate sets the base toolbar layout and the list fragment',
  evidence='SRC RecurringTransactionListActivity.java:43-69 (setContentView at 45; RecurringTransactionListFragment at 64)')

# ---- passcode gate: onCreate starts PasscodeActivity for a result, and the result comes back to onActivityResult
e('RecurringTransactionListActivity.onCreate', 'RecurringTransactionListActivity.onActivityResult', 'FRAMEWORK',
  'the passcode screen started at line 56 returns its result: the framework calls onActivityResult',
  needs_state=state_text('a passcode is set (settings): onCreate starts PasscodeActivity only when hasPasscode is true (RecurringTransactionListActivity.java:50-56)', ('settings',)),
  evidence='SRC RecurringTransactionListActivity.java:48-58 and 72; FW-SRC core/java/android/app/ActivityThread.java:4253-4265 (deliverResults) and 4312 (its call site); FW-SRC core/java/android/app/Activity.java:7259-7266 (dispatchActivityResult calls onActivityResult)')

# ================================================================== sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('RecurringTransactionEditActivity_MembersInjector.create', 'RecurringTransactionEditActivity_MembersInjector.<init>'),
    ('RecurringTransactionEditActivity_MembersInjector.injectMembers', 'RecurringTransactionEditActivity_MembersInjector.injectDateUtils'),
    ('RecurringTransactionEditActivity_MembersInjector.injectMembers', 'RecurringTransactionEditActivity_MembersInjector.injectDatabase'))

# ================================================================== UNREACHABLE (batch 101). Tuple: (kind, reason, evidence, confirmed_by)

UNREACHABLE['RecurringTransactionEditActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (takes the Provider). Its only caller record is create (auto_calls record at RecurringTransactionEditActivity_MembersInjector.java:27), and create has no caller: the app source has no reference to the generated class, and no auto_calls record has create as destination.',
  'SRC app source grep for the injector name: no output (label_101.grep.txt section 1); INFERRED class-file grep (section 2); auto_calls record RecurringTransactionEditActivity_MembersInjector.java:27 (section 3)',
  'INFERRED')

UNREACHABLE['RecurringTransactionEditActivity_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (takes the Provider and returns a MembersInjector). The component does not call it: DaggerMmxComponent.injectRecurringTransactionEditActivity calls the static injectDatabase and injectDateUtils directly (DaggerMmxComponent.java:418-419). No app source reference.',
  'SRC app source grep: no output (label_101.grep.txt section 1); INFERRED class-file grep (section 2); auto_calls records DaggerMmxComponent.java:418-419 (section 3)',
  'INFERRED')

UNREACHABLE['RecurringTransactionEditActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method of the MembersInjector interface. No caller: DaggerMmxComponent.class has no injectMembers string (count 0), and the app source has no reference. Its two outgoing CALL records (lines 33-34) are cut by sup. Its callees stay REACHABLE through the component.',
  'SRC app source grep: no output (label_101.grep.txt section 1); INFERRED class-file grep count 0 (section 2); auto_calls records RecurringTransactionEditActivity_MembersInjector.java:33-34 (section 3)',
  'INFERRED')
