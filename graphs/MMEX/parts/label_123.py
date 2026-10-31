# ================================================================== batch 123 (label_123): SyncManager (31, incl. SyncManager$1.<init>), SyncManager_Factory (4), SyncManager_MembersInjector (5); 40 methods
# Result: 26 REACHABLE, 14 UNREACHABLE (rows in graphs/MMEX/parts/label_123.md). Evidence: graphs/MMEX/parts/label_123.grep.txt.
# This file writes only:
#   - 14 UNREACHABLE entries: 7 SyncManager methods with no live caller (SOURCE) and 7 Dagger-generated methods (INFERRED),
#   - 24 sup pairs (D14): auto CALL records whose caller is UNREACHABLE in this batch.
# No e() edges: every REACHABLE method already has an auto CALL record into it (auto_calls.json, USE_AUTO), or is reached through a hop
# already in graph_def.py (SyncManager.<init> -> DaggerMmxComponent.inject(SyncManager), batch 043; DaggerMmxComponent.injectSyncManager, batch 044).
# The 5 REACHABLE methods whose only live callers are in batch 125 (setEnabled, setSyncInterval, stopSyncServiceAlarm, triggerDownload,
# triggerUpload) get no edge here; their route runs through batch 125 (SyncPreferenceFragment$3, $5, forceDownload, forceUpload), not yet merged (D4, D8).
# The sup for SyncManager.resetPreferences -> SyncPreferences.clear is in label_121.py (batch 121), not repeated here.

# ------------------------------------------------------------------ UNREACHABLE: SyncManager methods with no live caller (SOURCE)

UNREACHABLE['SyncManager.resetPreferences'] = ('no_trigger_in_app',
    'no live caller: its only other mention is the call sync.resetPreferences() at SyncPreferenceFragment.java:262, inside a commented-out block of the reset listener; no auto_calls.json record has it as dst',
    'sync/SyncManager.java:256-258; sync/SyncPreferenceFragment.java:252-276; label_123.grep.txt section A',
    'SOURCE')

UNREACHABLE['SyncManager.abortScheduledUpload'] = ('no_trigger_in_app',
    'no caller: its only other mention is the call at SyncManager.java:220, which is commented out; no auto_calls.json record has it as dst',
    'sync/SyncManager.java:82-89, 220; label_123.grep.txt section B',
    'SOURCE')

UNREACHABLE['SyncManager.scheduleDelayedUpload'] = ('no_trigger_in_app',
    'no caller: its only other mention is the call at SyncManager.java:150, commented out inside dataChanged; no auto_calls.json record has it as dst',
    'sync/SyncManager.java:150, 496-504; label_123.grep.txt section C',
    'SOURCE')

UNREACHABLE['SyncManager.getPendingIntentForDelayedUpload'] = ('no_trigger_in_app',
    'its only callers are abortScheduledUpload (line 85) and scheduleDelayedUpload (line 497), both UNREACHABLE',
    'sync/SyncManager.java:85, 497, 506-520; label_123.grep.txt section D',
    'SOURCE')

UNREACHABLE['SyncManager.getAlarmManager'] = ('no_trigger_in_app',
    'its only callers are abortScheduledUpload (line 86) and scheduleDelayedUpload (line 498), both UNREACHABLE; SyncSchedulerBroadcastReceiver.getAlarmManager(Context) is a different method',
    'sync/SyncManager.java:86, 498, 521-523; label_123.grep.txt section E',
    'SOURCE')

UNREACHABLE['SyncManager.getExternalStorageDirectoryForSync'] = ('no_trigger_in_app',
    'no caller and no reference anywhere in the source root (only its declaration)',
    'sync/SyncManager.java:456-470; label_123.grep.txt section F',
    'SOURCE')

UNREACHABLE['SyncManager.areFileNamesSame'] = ('no_trigger_in_app',
    'no live caller: its only other mention is the call at SyncManager.java:315, commented out; no outgoing auto_calls.json record',
    'sync/SyncManager.java:315, 399-401; label_123.grep.txt section G',
    'SOURCE')

# ------------------------------------------------------------------ UNREACHABLE: Dagger-generated factory and members injector (INFERRED; grep evidence in label_123.grep.txt section H)

UNREACHABLE['SyncManager_Factory.get'] = ('no_trigger_in_app',
    'generated static factory method; no caller: no class file names SyncManager_Factory except itself, and no app source names it or a Provider<SyncManager>; its CALLs (lines 33-36) are cut by sup below',
    'SyncManager.java:68-72 (@Inject constructor, the reason Dagger generates the factory); auto_calls SyncManager_Factory.java:33-36; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_Factory.create'] = ('no_trigger_in_app',
    'generated static factory method; no caller (no auto_calls record and no reference in DaggerMmxComponent or the source); its CALL to Factory.<init> (line 44) is cut by sup below',
    'auto_calls SyncManager_Factory.java:44; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_Factory.newSyncManager'] = ('no_trigger_in_app',
    'generated factory method; no caller; its CALLs to SyncManager.<clinit> and SyncManager.<init> (line 48) are cut by sup below',
    'auto_calls SyncManager_Factory.java:48; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_Factory.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is Factory.create (auto record, line 44), which has no caller',
    'auto_calls SyncManager_Factory.java:44; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_MembersInjector.create'] = ('no_trigger_in_app',
    'generated static factory method; no caller: DaggerMmxComponent.class references only the two static injectors injectDateTimeUtilsLazy and injectMDatabases (constant-pool parse); its CALL to MembersInjector.<init> (line 30) is cut by sup below',
    'auto_calls SyncManager_MembersInjector.java:30; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_MembersInjector.<init>'] = ('no_trigger_in_app',
    'generated constructor; its only caller is MembersInjector.create (auto record, line 30), which has no caller',
    'auto_calls SyncManager_MembersInjector.java:30; label_123.grep.txt section H',
    'INFERRED')

UNREACHABLE['SyncManager_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'generated instance method, reached only through the MembersInjector interface on an object that create would build; create has no caller and no injectMembers appears as a callee; its CALLs (lines 35-36) are cut by sup below',
    'auto_calls SyncManager_MembersInjector.java:35-36; label_123.grep.txt section H',
    'INFERRED')

# ------------------------------------------------------------------ sup pairs (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('SyncManager.resetPreferences', 'SyncManager.getPreferences'))  # resetPreferences has no caller, so its call to getPreferences (SyncManager.java:257) cannot run; its call to SyncPreferences.clear is cut in label_121.py
sup(('SyncManager.abortScheduledUpload', 'SyncManager.getPendingIntentForDelayedUpload'))  # abortScheduledUpload has no caller (SyncManager.java:85)
sup(('SyncManager.abortScheduledUpload', 'SyncManager.getAlarmManager'))  # abortScheduledUpload has no caller (SyncManager.java:86)
sup(('SyncManager.scheduleDelayedUpload', 'SyncManager.getPendingIntentForDelayedUpload'))  # scheduleDelayedUpload has no caller (SyncManager.java:497)
sup(('SyncManager.scheduleDelayedUpload', 'SyncManager.getAlarmManager'))  # scheduleDelayedUpload has no caller (SyncManager.java:498)
sup(('SyncManager.scheduleDelayedUpload', 'MmxDate.getMillis'))  # scheduleDelayedUpload has no caller (SyncManager.java:503); MmxDate.getMillis keeps its other caller SyncSchedulerBroadcastReceiver.startHeartbeat (batch 126)
sup(('SyncManager.scheduleDelayedUpload', 'MmxDate.<init>()'))  # scheduleDelayedUpload has no caller (SyncManager.java:503)
sup(('SyncManager.getPendingIntentForDelayedUpload', 'SyncManager.getContext'))  # getPendingIntentForDelayedUpload has only UNREACHABLE callers (SyncManager.java:516)
sup(('SyncManager.getPendingIntentForDelayedUpload', 'RecentDatabasesProvider.getCurrent'))  # getPendingIntentForDelayedUpload has only UNREACHABLE callers (SyncManager.java:507)
sup(('SyncManager.getPendingIntentForDelayedUpload', 'SyncManager.getDatabases'))  # getPendingIntentForDelayedUpload has only UNREACHABLE callers (SyncManager.java:507)
sup(('SyncManager.getAlarmManager', 'SyncManager.getContext'))  # getAlarmManager has only UNREACHABLE callers (SyncManager.java:522)
sup(('SyncManager.getExternalStorageDirectoryForSync', 'SyncManager.getContext'))  # getExternalStorageDirectoryForSync has no caller (SyncManager.java:468)
sup(('SyncManager.getExternalStorageDirectoryForSync', 'DatabaseManager.<init>'))  # getExternalStorageDirectoryForSync has no caller (SyncManager.java:459)
sup(('SyncManager.getExternalStorageDirectoryForSync', 'DatabaseManager.getDefaultDatabaseDirectory'))  # getExternalStorageDirectoryForSync has no caller (SyncManager.java:460)
sup(('SyncManager_Factory.get', 'SyncManager.<clinit>'))  # Factory.get has no caller (SyncManager_Factory.java:33)
sup(('SyncManager_Factory.get', 'SyncManager.<init>'))  # Factory.get has no caller (SyncManager_Factory.java:33)
sup(('SyncManager_Factory.get', 'SyncManager_MembersInjector.injectDateTimeUtilsLazy'))  # Factory.get has no caller (SyncManager_Factory.java:34)
sup(('SyncManager_Factory.get', 'SyncManager_MembersInjector.injectMDatabases'))  # Factory.get has no caller (SyncManager_Factory.java:36)
sup(('SyncManager_Factory.create', 'SyncManager_Factory.<init>'))  # Factory.create has no caller (SyncManager_Factory.java:44)
sup(('SyncManager_Factory.newSyncManager', 'SyncManager.<clinit>'))  # Factory.newSyncManager has no caller (SyncManager_Factory.java:48)
sup(('SyncManager_Factory.newSyncManager', 'SyncManager.<init>'))  # Factory.newSyncManager has no caller (SyncManager_Factory.java:48)
sup(('SyncManager_MembersInjector.create', 'SyncManager_MembersInjector.<init>'))  # MembersInjector.create has no caller (SyncManager_MembersInjector.java:30)
sup(('SyncManager_MembersInjector.injectMembers', 'SyncManager_MembersInjector.injectDateTimeUtilsLazy'))  # injectMembers has no caller (SyncManager_MembersInjector.java:35)
sup(('SyncManager_MembersInjector.injectMembers', 'SyncManager_MembersInjector.injectMDatabases'))  # injectMembers has no caller (SyncManager_MembersInjector.java:36)
