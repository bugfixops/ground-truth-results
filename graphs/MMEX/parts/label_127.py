# ================================================================== batch 127 (label_127): Authenticator (8 methods), AuthenticatorService (3), StubSyncProvider (7), SyncAdapter (3), SyncAdapterService (4), SyncAdapterTrigger (4), DbFileDownloadedEvent (1), SyncStartingEvent (1), SyncStoppingEvent (1), DownloadWorker (2), SyncWorker (2), UploadWorker (2); 38 methods
# Result: 13 REACHABLE, 25 UNREACHABLE (rows: graphs/MMEX/parts/label_127.md). Grep evidence: graphs/MMEX/parts/label_127.grep.txt.
# This file writes:
#   - 9 edges: ENTRY from S_ENTRY to AuthenticatorService.<init> (other_app: the Add account UI) and to SyncAdapterService.<clinit> and <init> (other_app: a bind by the SyncAdapter action);
#     LIFECYCLE from each service constructor to onCreate and from onCreate to onBind; LIFECYCLE from StubSyncProvider.<init> to onCreate;
#     FRAMEWORK (non_standard) from AuthenticatorService.onBind to Authenticator.addAccount (the binder dispatch);
#   - 25 UNREACHABLE entries (4-element tuples);
#   - 2 sup cuts (D20 target-owner cut) for the constructor records of the two events. Their callers are batch 126's sendStartEvent and sendStopEvent, which have no live caller.
#     Batch 126 already writes both cuts (label_126.py:59-60) and graph_def.py:11526 has the stop one; they are repeated here because the constructors are this batch's (set semantics, harmless).
# No CALL edge is written (D7). The auto CALL records that touch this batch are five: SyncAdapterService.onCreate -> SyncAdapter.<init>(Context,boolean) (SyncAdapterService.java:57),
#   AuthenticatorService.onCreate -> Authenticator.<init> (AuthenticatorService.java:36) (both REACHABLE sources), SyncService.sendStartEvent -> SyncStartingEvent.<init> (SyncService.java:241),
#   SyncService.sendStopEvent -> SyncStoppingEvent.<init> (SyncService.java:247) (both cut above), SyncServiceMessageHandler.handleMessage -> DbFileDownloadedEvent.<init> (SyncServiceMessageHandler.java:89, REACHABLE through batch 126).
#   No record has an UNREACHABLE source inside this batch, so no D14 cut is needed here. Framework and library calls (framework_calls: ContentProvider.<init>, Worker.<init>, AbstractThreadedSyncAdapter.<init> and others) are not CALL records and are not cut.

# ---- ENTRY: the two manifest services that other apps or the system bind; the framework creates each one by class name

e('S_ENTRY', 'AuthenticatorService.<init>', 'ENTRY',
  'the Add account list in system settings shows MMEX (authenticator.xml label app_name); choosing it makes AccountManager bind AuthenticatorService, and the framework creates the service by class name',
  env=env_text('outside package: the system Settings app adds an account of type example.com (res/xml/authenticator.xml:20), and AccountManager binds AuthenticatorService (exported=false)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:455-465 (service, exported=false, intent-filter android.accounts.AccountAuthenticator); SRC res/xml/authenticator.xml:19-22; FW-SRC core/java/android/app/ActivityThread.java:3311-3321 (handleCreateService; newInstance at 3321); INFERRED AccountManagerService binds the authenticator (system_server, not read)')

e('AuthenticatorService.<init>', 'AuthenticatorService.onCreate', 'LIFECYCLE',
  'the framework calls onCreate on the new service (handleCreateService)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3339 (service.onCreate); SRC sync/adapter/AuthenticatorService.java:33-37')

e('AuthenticatorService.onCreate', 'AuthenticatorService.onBind', 'LIFECYCLE',
  'a client binds the created service, and the framework calls onBind (handleBindService)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3356-3366 (handleBindService; s.onBind at 3366); SRC sync/adapter/AuthenticatorService.java:42-45')

e('AuthenticatorService.onBind', 'Authenticator.addAccount', 'FRAMEWORK',
  'the system Add account flow calls addAccount through the binder that onBind returns (getIBinder, AuthenticatorService.java:44); addAccount returns null, so no account is created',
  cls='non_standard',
  via='AbstractAccountAuthenticator binder stub: onBind returns the IBinder from getIBinder, and the stub dispatches addAccount (the library and AccountManagerService are not in fw_src; INFERRED)',
  evidence='SRC sync/adapter/AuthenticatorService.java:42-45; SRC sync/adapter/Authenticator.java:43-46; INFERRED framework binder dispatch (AbstractAccountAuthenticator not read)')

e('StubSyncProvider.<init>', 'StubSyncProvider.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after the constructor, from attachInfo',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:6225-6239; FW-SRC core/java/android/content/ContentProvider.java:1891-1917; SRC sync/adapter/StubSyncProvider.java:36-39')

e('S_ENTRY', 'SyncAdapterService.<clinit>', 'ENTRY',
  'another app binds SyncAdapterService by its SyncAdapter action; the framework creates the service by class name, and the JVM initialises the class first',
  env=env_text('outside package: another app binds to SyncAdapterService by the android.content.SyncAdapter action (exported=true, no permission, process :sync)', ('other_app',)),
  cls='non_standard',
  via='intent resolved by action name android.content.SyncAdapter (AndroidManifest.xml:466-477); the framework creates the service (ActivityThread handleCreateService)',
  evidence='SRC AndroidManifest.xml:466-477; SRC sync/adapter/SyncAdapterService.java:41-43 (static initialisers: sSyncAdapter at 41, sSyncAdapterLock = new Object() at 43); FW-SRC core/java/android/app/ActivityThread.java:3321 (newInstance); INFERRED the JVM initialises the class at the first newInstance (Java language rule)')

e('S_ENTRY', 'SyncAdapterService.<init>', 'ENTRY',
  'another app binds SyncAdapterService by its SyncAdapter action; the framework creates the service by class name',
  env=env_text('outside package: another app binds to SyncAdapterService by the android.content.SyncAdapter action (exported=true, no permission, process :sync)', ('other_app',)),
  cls='non_standard',
  via='intent resolved by action name android.content.SyncAdapter (AndroidManifest.xml:466-477); the framework creates the service (ActivityThread handleCreateService)',
  evidence='SRC AndroidManifest.xml:466-477; FW-SRC core/java/android/app/ActivityThread.java:3321 (newInstance)')

e('SyncAdapterService.<init>', 'SyncAdapterService.onCreate', 'LIFECYCLE',
  'the framework calls onCreate on the new service (handleCreateService)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3339 (service.onCreate); SRC sync/adapter/SyncAdapterService.java:48-60')

e('SyncAdapterService.onCreate', 'SyncAdapterService.onBind', 'LIFECYCLE',
  'a client binds the created service, and the framework calls onBind (handleBindService)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3356-3366 (handleBindService; s.onBind at 3366); SRC sync/adapter/SyncAdapterService.java:66-75')

# ---- D20 target-owner cut: the two event constructors are this batch's; their only callers are batch 126's sendStartEvent and sendStopEvent, which have no live caller


# ---- UNREACHABLE: Authenticator overrides that the account framework calls only for an account of type example.com (no_trigger_in_app, INFERRED)

UNREACHABLE['Authenticator.confirmCredentials'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:48-51, 43-46; label_127.grep.txt E',
  'INFERRED')

UNREACHABLE['Authenticator.editProperties'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:38-41, 43-46; label_127.grep.txt E',
  'INFERRED')

UNREACHABLE['Authenticator.getAuthToken'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:53-56, 43-46; label_127.grep.txt E',
  'INFERRED')

UNREACHABLE['Authenticator.getAuthTokenLabel'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:58-61, 43-46; label_127.grep.txt E',
  'INFERRED')

UNREACHABLE['Authenticator.hasFeatures'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:68-71, 43-46; label_127.grep.txt E',
  'INFERRED')

UNREACHABLE['Authenticator.updateCredentials'] = ('no_trigger_in_app',
  'the account framework calls it only for an existing account of type example.com; addAccount returns null and creates no account (Authenticator.java:43-46), and no code adds an account of that type (grep E: the only account creation is SyncAdapterTrigger.CreateSyncAccount, type com.money.manager.ex.sync, which has no caller)',
  'SRC sync/adapter/Authenticator.java:63-66, 43-46; label_127.grep.txt E',
  'INFERRED')

# ---- UNREACHABLE: StubSyncProvider overrides (the provider is reached only through a call on the datasyncprovider authority; no_trigger_in_app, INFERRED)

UNREACHABLE['StubSyncProvider.delete'] = ('no_trigger_in_app',
  'the provider receives delete only from a ContentResolver or ContentProviderClient call on its authority (datasyncprovider, AndroidManifest.xml:392); no code makes such a call (grep D: the authority occurs only in the manifest). The sync framework uses the adapter authority (SyncAdapterService.AUTHORITY), not this one',
  'SRC sync/adapter/StubSyncProvider.java:70-73; SRC AndroidManifest.xml:390-394; label_127.grep.txt D',
  'INFERRED')

UNREACHABLE['StubSyncProvider.getType'] = ('no_trigger_in_app',
  'the provider receives getType only from a ContentResolver or ContentProviderClient call on its authority (datasyncprovider, AndroidManifest.xml:392); no code makes such a call (grep D: the authority occurs only in the manifest). The sync framework uses the adapter authority (SyncAdapterService.AUTHORITY), not this one',
  'SRC sync/adapter/StubSyncProvider.java:43-46; SRC AndroidManifest.xml:390-394; label_127.grep.txt D',
  'INFERRED')

UNREACHABLE['StubSyncProvider.insert'] = ('no_trigger_in_app',
  'the provider receives insert only from a ContentResolver or ContentProviderClient call on its authority (datasyncprovider, AndroidManifest.xml:392); no code makes such a call (grep D: the authority occurs only in the manifest). The sync framework uses the adapter authority (SyncAdapterService.AUTHORITY), not this one',
  'SRC sync/adapter/StubSyncProvider.java:63-67; SRC AndroidManifest.xml:390-394; label_127.grep.txt D',
  'INFERRED')

UNREACHABLE['StubSyncProvider.query'] = ('no_trigger_in_app',
  'the provider receives query only from a ContentResolver or ContentProviderClient call on its authority (datasyncprovider, AndroidManifest.xml:392); no code makes such a call (grep D: the authority occurs only in the manifest). The sync framework uses the adapter authority (SyncAdapterService.AUTHORITY), not this one',
  'SRC sync/adapter/StubSyncProvider.java:51-59; SRC AndroidManifest.xml:390-394; label_127.grep.txt D',
  'INFERRED')

UNREACHABLE['StubSyncProvider.update'] = ('no_trigger_in_app',
  'the provider receives update only from a ContentResolver or ContentProviderClient call on its authority (datasyncprovider, AndroidManifest.xml:392); no code makes such a call (grep D: the authority occurs only in the manifest). The sync framework uses the adapter authority (SyncAdapterService.AUTHORITY), not this one',
  'SRC sync/adapter/StubSyncProvider.java:77-83; SRC AndroidManifest.xml:390-394; label_127.grep.txt D',
  'INFERRED')

# ---- UNREACHABLE: SyncAdapter (the three-argument constructor has no caller; onPerformSync is the framework callback for an account that is never created)

UNREACHABLE['SyncAdapter.<init>(Context,boolean,boolean)'] = ('no_trigger_in_app',
  'no caller: the only construction in the source root is the two-argument new SyncAdapter(getApplicationContext(), true) at SyncAdapterService.java:57 (grep B), and the two-argument constructor calls the superclass directly (SyncAdapter.java:45), so the three-argument one is never invoked',
  'SRC sync/adapter/SyncAdapter.java:58-69 (super at 62); SRC sync/adapter/SyncAdapterService.java:57; label_127.grep.txt B',
  'SOURCE')

UNREACHABLE['SyncAdapter.onPerformSync'] = ('no_trigger_in_app',
  'the sync framework calls it only for a sync of an account of type com.money.manager.ex.sync, and that account is created only by SyncAdapterTrigger.CreateSyncAccount, which has no caller (grep A). runSync and schedulePeriodicSync (the requests that would start a sync) have no caller either (grep A). The body is a todo comment and a Timber.d log (SyncAdapter.java:85), so it does no work even if reached',
  'SRC sync/adapter/SyncAdapter.java:82-88 (Timber.d at 85); label_127.grep.txt A, B',
  'INFERRED')

# ---- UNREACHABLE: SyncAdapterTrigger (no caller for any method; its only calls are in comments)

UNREACHABLE['SyncAdapterTrigger.<init>'] = ('no_trigger_in_app',
  'the class has only the implicit default constructor (class at line 42); its only new SyncAdapterTrigger() in the source root is in a comment (line 39), so no code creates the trigger (grep A)',
  'SRC sync/adapter/SyncAdapterTrigger.java:42, 39 (comment); label_127.grep.txt A',
  'SOURCE')

UNREACHABLE['SyncAdapterTrigger.CreateSyncAccount'] = ('no_trigger_in_app',
  'its only call (line 38) is in a comment, and no other code in the source root calls it (grep A), so no account of type com.money.manager.ex.sync is created',
  'SRC sync/adapter/SyncAdapterTrigger.java:49-64 (addAccountExplicitly at 58), 38; label_127.grep.txt A, E',
  'SOURCE')

UNREACHABLE['SyncAdapterTrigger.runSync'] = ('no_trigger_in_app',
  'its only call (line 39) is in a comment, and no other code calls it (grep A), so the requestSync call it would make (line 110) never runs',
  'SRC sync/adapter/SyncAdapterTrigger.java:99-112 (requestSync at 110), 39; label_127.grep.txt A, D',
  'SOURCE')

UNREACHABLE['SyncAdapterTrigger.schedulePeriodicSync'] = ('no_trigger_in_app',
  'no caller in the source root: the name occurs only at its declaration (line 85; grep A), so the addPeriodicSync call it would make (line 91) never runs',
  'SRC sync/adapter/SyncAdapterTrigger.java:85-97 (addPeriodicSync at 91); label_127.grep.txt A',
  'SOURCE')

# ---- UNREACHABLE: the two event constructors (their only callers are batch 126's sendStartEvent and sendStopEvent, which have no live caller)

UNREACHABLE['SyncStartingEvent.<init>'] = ('no_trigger_in_app',
  'the only construction is in SyncService.sendStartEvent (SyncService.java:241), which has no live caller (batch 126: its call at line 95 is commented out, and no other class calls it); the constructor has no other call (grep G)',
  'SRC sync/events/SyncStartingEvent.java:24 (default constructor); SRC sync/SyncService.java:238-243; label_127.grep.txt G',
  'SOURCE')

UNREACHABLE['SyncStoppingEvent.<init>'] = ('no_trigger_in_app',
  'the only construction is in SyncService.sendStopEvent (SyncService.java:247), which has no live caller (batch 126: its calls at lines 108, 116, 186 and 198 are commented out, and no other class calls it); the constructor has no other call (grep G)',
  'SRC sync/events/SyncStoppingEvent.java:24 (default constructor); SRC sync/SyncService.java:245-249; label_127.grep.txt G',
  'SOURCE')

# ---- UNREACHABLE: the three Worker classes (no WorkRequest names them; no_trigger_in_app, SOURCE)

UNREACHABLE['DownloadWorker.<init>'] = ('no_trigger_in_app',
  'no code names DownloadWorker outside its own file (grep C); WorkManager creates a Worker only for a WorkRequest that names it, and src/main has no WorkRequest (grep C)',
  'SRC sync/jobmanager/DownloadWorker.java:30-33; label_127.grep.txt C',
  'SOURCE')

UNREACHABLE['DownloadWorker.doWork'] = ('no_trigger_in_app',
  'its only caller would be WorkManager running a DownloadWorker request, and no such request exists (grep C); the body returns Result.success() (DownloadWorker.java:36-39)',
  'SRC sync/jobmanager/DownloadWorker.java:36-39; label_127.grep.txt C',
  'SOURCE')

UNREACHABLE['SyncWorker.<init>'] = ('no_trigger_in_app',
  'no code names SyncWorker outside its own file (grep C); WorkManager creates a Worker only for a WorkRequest that names it, and src/main has no WorkRequest (grep C)',
  'SRC sync/jobmanager/SyncWorker.java:30-33; label_127.grep.txt C',
  'SOURCE')

UNREACHABLE['SyncWorker.doWork'] = ('no_trigger_in_app',
  'its only caller would be WorkManager running a SyncWorker request, and no such request exists (grep C); the body returns Result.success() (SyncWorker.java:36-39)',
  'SRC sync/jobmanager/SyncWorker.java:36-39; label_127.grep.txt C',
  'SOURCE')

UNREACHABLE['UploadWorker.<init>'] = ('no_trigger_in_app',
  'no code names UploadWorker outside its own file (grep C); WorkManager creates a Worker only for a WorkRequest that names it, and src/main has no WorkRequest (grep C)',
  'SRC sync/jobmanager/UploadWorker.java:30-33; label_127.grep.txt C',
  'SOURCE')

UNREACHABLE['UploadWorker.doWork'] = ('no_trigger_in_app',
  'its only caller would be WorkManager running an UploadWorker request, and no such request exists (grep C); the body returns Result.success() (UploadWorker.java:36-39)',
  'SRC sync/jobmanager/UploadWorker.java:36-39; label_127.grep.txt C',
  'SOURCE')
