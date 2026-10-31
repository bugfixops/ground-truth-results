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
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3187 (receiver.onReceive); SRC core/RecurringTransactionBootReceiver.java:40-47')

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
