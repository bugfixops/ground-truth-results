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
