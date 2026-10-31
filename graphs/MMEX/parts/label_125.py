# ================================================================== batch 125 (label_125): SyncPreferenceFragment (15 methods), SyncPreferenceFragment$1 to $10 (20), SyncPreferenceFragment_MembersInjector (4), SyncPreferencesViewHolder (1); 40 methods
# Result: 24 REACHABLE, 16 UNREACHABLE, 0 INCOMPLETE (rows: graphs/MMEX/parts/label_125.md). Grep evidence: graphs/MMEX/parts/label_125.grep.txt.
# This file writes:
#   - LIFECYCLE from SyncPreferenceFragment.<init> to onCreate (D21: the fragment's own constructor, created by SyncPreferencesActivity.onCreate),
#   - LIFECYCLE from onCreate to onCreatePreferences (framework dispatch through PreferenceFragmentCompat.onCreate) and to onStart,
#   - LIFECYCLE from onStart to onStop, REGISTER from onStart to onEvent (EventBus.register at line 107),
#   - ASYNC from SyncServiceMessageHandler.handleMessage to onEvent (D1: this batch owns the destination; batch 126 owns the source and must not write it again),
#   - 6 GUI edges from S_SYNC_SETTINGS (batch 122 page) to the six preference listeners $3 to $8 (D6),
#   - 16 UNREACHABLE entries and 25 sup cuts (D14): every auto CALL record whose caller is UNREACHABLE in this batch.
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7).
# The route into SyncPreferencesActivity.onCreate and the ENTERS edge to S_SYNC_SETTINGS are batch 122's.
# The injection chain DaggerMmxComponent.inject -> injectSyncPreferenceFragment -> injectMDatabases is batches 043 and 044's (auto CALL records).

# ---- the fragment lifecycle: the activity creates the fragment, the FragmentManager runs onCreate, then onStart

e('SyncPreferenceFragment.<init>', 'SyncPreferenceFragment.onCreate', 'LIFECYCLE',
  'the sync settings fragment is created by SyncPreferencesActivity.onCreate and committed by setSettingFragment; the FragmentManager then runs onCreate of SyncPreferenceFragment (same pattern as label_121 SettingsFragment.<init>)',
  evidence='SRC settings/SyncPreferencesActivity.java:33-38 (new SyncPreferenceFragment and setSettingFragment at 37); SRC sync/SyncPreferenceFragment.java:66-68, 75-80; INFERRED androidx FragmentManager (library source not read); D21')

e('SyncPreferenceFragment.onCreate', 'SyncPreferenceFragment.onCreatePreferences', 'LIFECYCLE',
  'super.onCreate (line 77) is PreferenceFragmentCompat.onCreate, which calls the overridden onCreatePreferences (framework dispatch; INFERRED from the framework contract)',
  evidence='SRC sync/SyncPreferenceFragment.java:76-80 (super.onCreate at 77), 82-91; auto_calls.json framework_calls, near line 72240: SyncPreferenceFragment.onCreate lists PreferenceFragmentCompat.onCreate')

e('SyncPreferenceFragment.onCreate', 'SyncPreferenceFragment.onStart', 'LIFECYCLE',
  'the framework starts the fragment after onCreate and the view creation (INFERRED androidx Fragment lifecycle; the pattern of label_003 PasscodeActivity.onCreate to onStart)',
  evidence='SRC sync/SyncPreferenceFragment.java:75-80, 102-108; INFERRED androidx Fragment lifecycle (library source not read)')

e('SyncPreferenceFragment.onStart', 'SyncPreferenceFragment.onStop', 'LIFECYCLE',
  'the framework stops the started fragment (INFERRED androidx Fragment lifecycle; the pattern of label_010 AccountTransactionListFragment.onResume to onStop)',
  evidence='SRC sync/SyncPreferenceFragment.java:102-115; INFERRED androidx Fragment lifecycle (library source not read)')

# ---- EventBus: the fragment subscribes in onStart; the download-complete event reaches onEvent

e('SyncPreferenceFragment.onStart', 'SyncPreferenceFragment.onEvent', 'REGISTER',
  'EventBus.getDefault().register(this) makes onEvent a subscriber while the fragment is started; onStop unregisters it (line 114)',
  evidence='SRC sync/SyncPreferenceFragment.java:102-108 (register at 107), 110-115 (unregister at 114), 120-121 (@Subscribe onEvent(DbFileDownloadedEvent)); precedent label_010 AccountTransactionListFragment.onStart -> onEvent (REGISTER)')

e('SyncServiceMessageHandler.handleMessage', 'SyncPreferenceFragment.onEvent', 'ASYNC',
  'the sync service sends DOWNLOAD_COMPLETE to the handler (case at line 84) and the handler posts a new DbFileDownloadedEvent to EventBus (line 89); EventBus delivers it to the registered subscriber onEvent. The cloud download is the one forceDownload starts (the Download preference, line 236)',
  env=env_text('the cloud download that the Download preference starts (forceDownload) completes in the sync service; it needs the network and the cloud storage', ('network',)),
  evidence='SRC sync/SyncServiceMessageHandler.java:61 (handleMessage), 84-89 (post at 89); SRC sync/SyncPreferenceFragment.java:120-123; precedent label_032 DebugTree.log -> MmxBaseFragmentActivity.onEvent (ASYNC); the source handleMessage is batch 126 (not merged yet): this route is open until batch 126 merges (D4, D8)')

# ---- GUI edges from the synchronization settings page (S_SYNC_SETTINGS, label_122.py) to each preference listener (D6)

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$3.onPreferenceChange', 'GUI',
  'the user switches Synchronisation on or off (R.string.pref_sync_enabled, the first preference): the listener calls SyncManager.setEnabled and starts or stops the heartbeat',
  evidence='SRC sync/SyncPreferenceFragment.java:180-193 (listener set at 180, onPreferenceChange 182, setEnabled 185); SRC res/xml/preferences_sync.xml:21-23 (SwitchPreferenceCompat, key pref_sync_enabled)')

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$4.onPreferenceClick', 'GUI',
  'the user taps Remote file (R.string.pref_remote_file): the listener returns false, and the file-picker start (lines 201-202) is commented out, so the tap has no further route',
  evidence='SRC sync/SyncPreferenceFragment.java:197-206 (listener set at 197, onPreferenceClick 199, picker lines 201-202 commented, return at 204); SRC res/xml/preferences_sync.xml:39-42 (Preference, key pref_remote_file)')

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$5.onPreferenceChange', 'GUI',
  'the user chooses a sync interval (R.string.pref_sync_interval, ListPreference): the listener sets the interval, resets the alarm and starts the heartbeat when the interval is above 0',
  evidence='SRC sync/SyncPreferenceFragment.java:209-229 (listener set at 209, onPreferenceChange 211, setSyncInterval 215, startSyncServiceHeartbeat 225); SRC res/xml/preferences_sync.xml:28-34 (ListPreference, key pref_sync_interval)')

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$6.onPreferenceClick', 'GUI',
  'the user taps Download (R.string.pref_sync_download): the listener calls forceDownload (line 236) and returns true',
  evidence='SRC sync/SyncPreferenceFragment.java:233-239 (listener set at 233, onPreferenceClick 235, forceDownload 236); SRC res/xml/preferences_sync.xml:46-52 (PreferenceScreen, key pref_sync_download)')

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$7.onPreferenceClick', 'GUI',
  'the user taps Upload (R.string.pref_sync_upload): the listener calls forceUpload (line 246)',
  evidence='SRC sync/SyncPreferenceFragment.java:243-249 (listener set at 243, onPreferenceClick 245, forceUpload 246); SRC res/xml/preferences_sync.xml:53-59 (PreferenceScreen, key pref_sync_upload)')

e('S_SYNC_SETTINGS', 'SyncPreferenceFragment$8.onPreferenceClick', 'GUI',
  'the user taps Reset preferences (R.string.pref_reset_preferences): the listener only gets the SyncManager (line 255) and returns false; the logout and reset calls (lines 256-273) are commented out',
  evidence='SRC sync/SyncPreferenceFragment.java:252-276 (listener set at 252, getSyncManager 255, commented calls 256-273, return at 274); SRC res/xml/preferences_sync.xml:79-81 (Preference, key pref_reset_preferences)')

# ---- UNREACHABLE entries (grep evidence in label_125.grep.txt)

UNREACHABLE['SyncPreferenceFragment.onActivityResult'] = ('no_trigger_in_app',
    'Fragment.onActivityResult runs only for a request this fragment started with startActivityForResult. The only start in this fragment that sends REQUEST_REMOTE_FILE (1) is commented out (line 202), so no result with that code arrives; no other call site exists in the source root (grep B1, C1)',
    'sync/SyncPreferenceFragment.java:94-100, 201-202; label_125.grep.txt sections A, C',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment.handleFileSelection'] = ('no_trigger_in_app',
    'private; its only caller is onActivityResult (line 98), which has no live caller. Its auto CALL records (binaryDialog, startSyncServiceHeartbeat, getSyncManager, the two anonymous listeners) are cut below (D14)',
    'sync/SyncPreferenceFragment.java:130-163 (call at 98); label_125.grep.txt sections A, B',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment.checkIfLocalFileExistsAndDownload'] = ('no_trigger_in_app',
    'private; its only callers are the Action1 listener $1.call (line 159), which belongs to handleFileSelection (unreachable), and no other call site (grep B2). Its outgoing auto CALL records are cut below (D14)',
    'sync/SyncPreferenceFragment.java:279-305 (call at 159); label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment.getDatabases'] = ('no_trigger_in_app',
    'private accessor for mDatabases; its only callers are checkIfLocalFileExistsAndDownload (line 280) and saveDatabaseMetadata (line 338); both are unreachable, so getDatabases has no live caller (grep B2, B3)',
    'sync/SyncPreferenceFragment.java:172-174, 280, 338; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$1.<init>'] = ('no_trigger_in_app',
    'created only by handleFileSelection (auto CALL, line 148), which is unreachable; the object is never created',
    'sync/SyncPreferenceFragment.java:148-161; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$1.call'] = ('no_trigger_in_app',
    'the Action1 subscriber of the download confirmation (line 159, calls checkIfLocalFileExistsAndDownload); it runs only when the RxJava chain from handleFileSelection emits, which never starts (RxJava behaviour: INFERRED)',
    'sync/SyncPreferenceFragment.java:155-161 (call at 159); label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$2.<init>'] = ('no_trigger_in_app',
    'created only by handleFileSelection (auto CALL, line 146), which is unreachable',
    'sync/SyncPreferenceFragment.java:148-154; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$2.call'] = ('no_trigger_in_app',
    'the Func1 filter of the download confirmation (returns the user answer); it runs only from the RxJava chain of handleFileSelection, which never starts (INFERRED RxJava behaviour)',
    'sync/SyncPreferenceFragment.java:148-154; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$9.<init>'] = ('no_trigger_in_app',
    'created only by checkIfLocalFileExistsAndDownload (auto CALL, line 287), which is unreachable',
    'sync/SyncPreferenceFragment.java:286-301; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$9.call'] = ('no_trigger_in_app',
    'the Action1 subscriber of the file-exists prompt (line 298, calls forceDownload); it runs only from the RxJava chain built in checkIfLocalFileExistsAndDownload, which never runs (INFERRED RxJava behaviour)',
    'sync/SyncPreferenceFragment.java:294-300 (call at 298); label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$10.<init>'] = ('no_trigger_in_app',
    'created only by checkIfLocalFileExistsAndDownload (auto CALL, line 286), which is unreachable',
    'sync/SyncPreferenceFragment.java:286-293; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment$10.call'] = ('no_trigger_in_app',
    'the Func1 filter of the file-exists prompt (returns the user answer); it runs only from the RxJava chain of checkIfLocalFileExistsAndDownload, which never runs (INFERRED RxJava behaviour)',
    'sync/SyncPreferenceFragment.java:287-293; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment.saveDatabaseMetadata'] = ('no_trigger_in_app',
    'private; its only call (line 140) is commented out, and no other reference in the source root calls it (grep B4). The same route is noted dead in batches 075 and 083. Its seven auto CALL records are cut below (D14)',
    'sync/SyncPreferenceFragment.java:140, 326-339; label_125.grep.txt sections B, D',
    'SOURCE')

UNREACHABLE['SyncPreferenceFragment_MembersInjector.<init>'] = ('no_trigger_in_app',
    'Dagger-generated constructor; its only caller is create (auto CALL, line 25), which has no caller. DaggerMmxComponent refers to the injector class only through injectMDatabases (grep C2, C3); the generated class is INFERRED (D5, D12)',
    'sync/SyncPreferenceFragment_MembersInjector.class (<init>(Provider) at lines 19-21); label_125.grep.txt sections C, D',
    'INFERRED')

UNREACHABLE['SyncPreferenceFragment_MembersInjector.create'] = ('no_trigger_in_app',
    'Dagger-generated static factory; no caller: DaggerMmxComponent does not reference it (grep C2, C3). Its only outgoing record, to <init>, is cut below (D14)',
    'sync/SyncPreferenceFragment_MembersInjector.class (create(Provider) at line 25); label_125.grep.txt sections C, D',
    'INFERRED')

UNREACHABLE['SyncPreferenceFragment_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'Dagger-generated MembersInjector.injectMembers(SyncPreferenceFragment); no caller: DaggerMmxComponent calls only the static injectMDatabases (grep C2, C3). Its only outgoing record, to injectMDatabases, is cut below (D14); the bridge injectMembers(Object) is not in this batch',
    'sync/SyncPreferenceFragment_MembersInjector.class (injectMembers at lines 30-31); label_125.grep.txt sections C, D',
    'INFERRED')

# ---- sup cuts (D14): every auto CALL record whose caller is UNREACHABLE in this batch. Targets in other batches keep their other callers (grep E).

sup(('SyncPreferenceFragment.onActivityResult', 'SyncPreferenceFragment.handleFileSelection'))  # onActivityResult has no live caller; its call to handleFileSelection (line 98) is cut
sup(('SyncPreferenceFragment.handleFileSelection', 'SyncPreferenceFragment$1.<init>'))  # handleFileSelection is unreachable (line 148)
sup(('SyncPreferenceFragment.handleFileSelection', 'SyncPreferenceFragment$2.<init>'))  # handleFileSelection is unreachable (line 146)
sup(('SyncPreferenceFragment.handleFileSelection', 'UIHelper.binaryDialog(int,int,int,int)'))  # cross-batch (batch 040): the four-argument overload has one other caller, binaryDialog(int,int) in UIHelper.java:86, and batch 040 labels it UNREACHABLE
sup(('SyncPreferenceFragment.handleFileSelection', 'UIHelper.<init>'))  # handleFileSelection is unreachable (line 146); UIHelper.<init> has 98 callers in the graph
sup(('SyncPreferenceFragment.handleFileSelection', 'SyncManager.startSyncServiceHeartbeat'))  # handleFileSelection is unreachable (line 143); the method has three other callers
sup(('SyncPreferenceFragment.handleFileSelection', 'SyncPreferenceFragment.getSyncManager'))  # handleFileSelection is unreachable (line 143); getSyncManager has other live callers
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'SyncPreferenceFragment.forceDownload'))  # checkIfLocal is unreachable (line 303); forceDownload is reached from $6 (line 236)
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'SyncPreferenceFragment$9.<init>'))  # checkIfLocal is unreachable (line 287)
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'SyncPreferenceFragment$10.<init>'))  # checkIfLocal is unreachable (line 286)
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'UIHelper.binaryDialog(int,int)'))  # cross-batch (batch 040): the two-argument overload's only caller is checkIfLocal (line 286), so its label is UNREACHABLE (batch 040)
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'UIHelper.<init>'))  # checkIfLocal is unreachable (line 286); UIHelper.<init> has 98 callers in the graph
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'RecentDatabasesProvider.getCurrent'))  # checkIfLocal is unreachable (line 280); getCurrent has eight other callers
sup(('SyncPreferenceFragment.checkIfLocalFileExistsAndDownload', 'SyncPreferenceFragment.getDatabases'))  # checkIfLocal is unreachable (line 280)
sup(('SyncPreferenceFragment$1.call', 'SyncPreferenceFragment.checkIfLocalFileExistsAndDownload'))  # $1.call runs only from the unreachable chain; its call at line 159 is cut
sup(('SyncPreferenceFragment$9.call', 'SyncPreferenceFragment.forceDownload'))  # $9.call runs only from the unreachable chain; its call at line 298 is cut
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'RecentDatabasesProvider.add(DatabaseMetadata)'))  # saveDatabaseMetadata has no caller (line 140 is commented); RecentDatabasesProvider.add has three other callers
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'SyncPreferenceFragment.getDatabases'))  # saveDatabaseMetadata is unreachable (line 338)
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'DatabaseMetadataFactory.getInstance(String,String)'))  # saveDatabaseMetadata is unreachable (line 336); getInstance has one other caller
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'SettingsBase.set(Integer,String)@AppSettings'))  # saveDatabaseMetadata is unreachable (line 334); the set accessor has many callers
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'AppSettings.<init>'))  # saveDatabaseMetadata is unreachable (line 334); AppSettings.<init> has 49 callers
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'DatabaseManager.getDefaultDatabaseDirectory'))  # saveDatabaseMetadata is unreachable (line 330)
sup(('SyncPreferenceFragment.saveDatabaseMetadata', 'DatabaseManager.<init>'))  # saveDatabaseMetadata is unreachable (line 329); DatabaseManager.<init> has 13 callers
sup(('SyncPreferenceFragment_MembersInjector.create', 'SyncPreferenceFragment_MembersInjector.<init>'))  # create has no caller, so the edge cannot run (D14, D12)
sup(('SyncPreferenceFragment_MembersInjector.injectMembers', 'SyncPreferenceFragment_MembersInjector.injectMDatabases'))  # injectMembers has no caller; injectMDatabases stays reachable from injectSyncPreferenceFragment (batch 044)
