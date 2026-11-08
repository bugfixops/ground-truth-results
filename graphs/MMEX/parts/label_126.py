# ================================================================== batch 126 (label_126): SyncSchedulerBroadcastReceiver (4 methods), SyncService (12), SyncService$1 and $2 (2), SyncServiceMessage (3), SyncServiceMessageHandler (6), SyncServiceMessageHandler_MembersInjector (4), SyncService_MembersInjector (4); 35 methods
# Result: 23 REACHABLE, 12 UNREACHABLE (11 no_trigger_in_app, 1 branch_never_taken), 0 INCOMPLETE (rows: graphs/MMEX/parts/label_126.md). Grep evidence: graphs/MMEX/parts/label_126.grep.txt.
# This file writes:
#   - ENTRY from S_ENTRY to SyncSchedulerBroadcastReceiver.<init> (manifest lines 100-106: BOOT_COMPLETED, START_SYNC_SERVICE, STOP_SYNC_SERVICE),
#   - LIFECYCLE from the receiver <init> to onReceive (ActivityThread.handleReceiver, line 3187),
#   - INTENT from SyncManager.startSyncServiceHeartbeat and SyncManager.stopSyncServiceAlarm (batch 123 methods) to onReceive (D1: the destination is this batch's method),
#   - FRAMEWORK from SyncService.enqueueWork (JobIntentService, INFERRED) to SyncService.<init> and to onHandleWork,
#   - LIFECYCLE from SyncService.<init> to onCreate (ActivityThread.handleCreateService, line 3339) and from onHandleWork to onDestroy (INFERRED: JobIntentService stopSelf, ActivityThread line 3504),
#   - FRAMEWORK from SyncService.sendMessage to SyncServiceMessageHandler.handleMessage (Messenger delivery through Handler.dispatchMessage, Handler.java 97-106; the Messenger class is INFERRED),
#   - 9 sup() cuts (D14 for the UNREACHABLE callers; D18 for the branch that never runs),
#   - 12 UNREACHABLE entries.
# No CALL edge is written: every app-to-app call in this batch is already an auto CALL record (D7). The auto CALL records into the batch's methods are: the receiver's startHeartbeat (67) and getAlarmManager (57); enqueueWork from SyncManager.invokeSyncService (batch 123, line 217); SyncService.onCreate -> DaggerMmxComponent.inject(SyncService) (line 86, cha); triggerSync (135); sendMessage (107, 128, 132, 185, 197, 210, 217); showNotificationForConflict (203); $1 and $2 (187, 199); SyncServiceMessage.<clinit> and <init> (107, 185, 65, 33); parse (62); closeDialog and getContext (112, 113); showProgressDialog (79); SyncServiceMessageHandler.<init> from invokeSyncService (batch 123, line 212); DaggerMmxComponent inject and inject-chain records (lines 323, 358, 554, 597).
# The batch's own MembersInjector records (create -> <init>, injectMembers -> inject calls) are the auto records cited in the UNREACHABLE evidence (D7, D14).
# Citation form for generated classes: 'ClassName.class bytecode line N' with the full path final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/.

# ---- the broadcast receiver: the manifest starts it on BOOT_COMPLETED and on the START and STOP actions; the framework creates it and calls onReceive

e('S_ENTRY', 'SyncSchedulerBroadcastReceiver.<init>', 'ENTRY',
  'the manifest registers SyncSchedulerBroadcastReceiver (exported) for BOOT_COMPLETED, START_SYNC_SERVICE and STOP_SYNC_SERVICE; the framework creates it when one of these broadcasts arrives',
  evidence='SRC AndroidManifest.xml:100-106 (receiver and intent-filter); FW-SRC core/java/android/app/ActivityThread.java:3141-3166 (handleReceiver; newInstance at 3166)')

e('SyncSchedulerBroadcastReceiver.<init>', 'SyncSchedulerBroadcastReceiver.onReceive', 'LIFECYCLE',
  'the framework calls onReceive on the new receiver instance',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3187 (receiver.onReceive)')

e('SyncManager.startSyncServiceHeartbeat', 'SyncSchedulerBroadcastReceiver.onReceive', 'INTENT',
  'startSyncServiceHeartbeat sends the ACTION_START broadcast (START_SYNC_SERVICE); the manifest filter delivers it to this receiver. The edge source is batch 123',
  evidence='SRC sync/SyncManager.java:268-281 (sendBroadcast of ACTION_START at 270-271); SRC sync/SyncSchedulerBroadcastReceiver.java:39-40 (action constants); AndroidManifest.xml:103')

e('SyncManager.stopSyncServiceAlarm', 'SyncSchedulerBroadcastReceiver.onReceive', 'INTENT',
  'stopSyncServiceAlarm sends the ACTION_STOP broadcast (STOP_SYNC_SERVICE); onReceive cancels the alarm and returns (lines 60-65). The edge source is batch 123',
  evidence='SRC sync/SyncManager.java:283-291 (sendBroadcast of ACTION_STOP at 285-286); SRC sync/SyncSchedulerBroadcastReceiver.java:40, 60-65; AndroidManifest.xml:104')

# ---- the sync service: JobIntentService.enqueueWork starts it (INFERRED androidx); the framework creates it and runs onCreate, then onHandleWork; onDestroy after the work

e('SyncService.enqueueWork', 'SyncService.<init>', 'FRAMEWORK',
  'the static enqueueWork (lines 151-153) hands the intent to JobIntentService.enqueueWork, which starts the service; the framework constructs it. The same pattern as the RecurringTransactionIntentService edges in graph_def.py',
  evidence='SRC sync/SyncService.java:151-153; FW-SRC core/java/android/app/ActivityThread.java:3311-3321 (handleCreateService; newInstance at 3321); INFERRED androidx JobIntentService (library not in the dataset; not read)')

e('SyncService.enqueueWork', 'SyncService.onHandleWork', 'FRAMEWORK',
  'JobIntentService delivers each queued intent to onHandleWork on its worker thread (INFERRED from the androidx contract)',
  evidence='SRC sync/SyncService.java:90 (onHandleWork), 151-153; INFERRED androidx JobIntentService (not read)')

e('SyncService.<init>', 'SyncService.onCreate', 'LIFECYCLE',
  'the framework calls onCreate after it constructs the service (handleCreateService)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3339 (service.onCreate); SRC sync/SyncService.java:79-87')

e('SyncService.onHandleWork', 'SyncService.onDestroy', 'LIFECYCLE',
  'when the queued work is done JobIntentService stops itself, and the framework then runs onDestroy (INFERRED androidx stopSelf path)',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3499-3504 (handleStopService; s.onDestroy at 3504); FW-SRC core/java/android/app/Service.java:515; INFERRED androidx JobIntentService (not read)')

e('SyncService.sendMessage', 'SyncServiceMessageHandler.handleMessage', 'FRAMEWORK',
  'sendMessage hands a Message to the caller Messenger (SyncManager.invokeSyncService creates it, batch 123); the framework delivers it to the handler, which calls handleMessage. The Messenger exists only when the sync starts from an AppCompatActivity (SyncManager.java:210-213)',
  evidence='SRC sync/SyncService.java:222-236 (msg.what at 226; outMessenger.send at 229); FW-SRC core/java/os/Handler.java:97-106 (dispatchMessage calls handleMessage at 106); INFERRED android.os.Messenger (not in fw_src; not read)')

# ---- cuts. D14: an auto CALL edge whose caller is UNREACHABLE in this batch is cut, so the target has no live incoming edge from it.
#      The <init> cuts complete the SyncNotificationFactory cuts that batch 124 wrote for the getters (its file: SyncService.java:169 and 253).

sup(('SyncService.sendStartEvent', 'SyncStartingEvent.<init>'))  # D14: sendStartEvent has no live caller (label_126.grep.txt section A); the constructor is batch 127's
sup(('SyncService.sendStopEvent', 'SyncStoppingEvent.<init>'))  # D14: sendStopEvent has no live caller (section A); the constructor is batch 127's
sup(('SyncService.showNotificationUploading', 'SyncNotificationFactory.<init>'))  # D14: line 252 (the getter record at 253 is cut by batch 124)
sup(('SyncService.showNotificationUploadComplete', 'SyncNotificationFactory.<init>'))  # D14: line 168 (the getter record at 169 is cut by batch 124)
sup(('SyncServiceMessageHandler.handleMessage', 'SyncServiceMessageHandler.showProgressDialog'))  # D18 branch judgment: only the STARTING_DOWNLOAD case calls it (line 79), and no sender uses that code (section E)
sup(('SyncService_MembersInjector.create', 'SyncService_MembersInjector.<init>'))  # D14: create has no caller (section C), so its call into <init> cannot run
sup(('SyncService_MembersInjector.injectMembers', 'SyncService_MembersInjector.injectRecentDatabasesProvider'))  # D14: injectMembers has no caller (section C)
sup(('SyncServiceMessageHandler_MembersInjector.create', 'SyncServiceMessageHandler_MembersInjector.<init>'))  # D14: create has no caller (section C)
sup(('SyncServiceMessageHandler_MembersInjector.injectMembers', 'SyncServiceMessageHandler_MembersInjector.injectMDatabases'))  # D14: injectMembers has no caller (section C)

# ---- UNREACHABLE: source methods with no live caller (no_trigger_in_app, SOURCE)

UNREACHABLE['SyncService.sendStartEvent'] = ('no_trigger_in_app',
  'private method; its only call site (line 95) is commented out, and no other class calls it (label_126.grep.txt section A); auto_calls.json has no caller record',
  'SRC sync/SyncService.java:238-243 (EventBus post of SyncStartingEvent at 241); label_126.grep.txt section A',
  'SOURCE')

UNREACHABLE['SyncService.sendStopEvent'] = ('no_trigger_in_app',
  'private method; every call site (lines 108, 116, 186, 198) is commented out, and no other class calls it (label_126.grep.txt section A)',
  'SRC sync/SyncService.java:245-249 (EventBus post of SyncStoppingEvent at 247); SRC sync/SyncService.java:108, 116, 186, 198 (commented); label_126.grep.txt section A',
  'SOURCE')

UNREACHABLE['SyncService.showNotificationUploading'] = ('no_trigger_in_app',
  'private method with no call site in the app source (its only occurrence is the declaration at 251; label_126.grep.txt section A) and no caller record in auto_calls.json',
  'SRC sync/SyncService.java:251-259 (declaration at 251; constructor call at 252); label_126.grep.txt section A',
  'SOURCE')

UNREACHABLE['SyncService.showNotificationUploadComplete'] = ('no_trigger_in_app',
  'private method with no call site in the app source (its only occurrence is the declaration at 155; label_126.grep.txt section A) and no caller record in auto_calls.json',
  'SRC sync/SyncService.java:155-172 (declaration at 155; constructor call at 168); label_126.grep.txt section A',
  'SOURCE')

UNREACHABLE['SyncServiceMessageHandler.getDatabases'] = ('no_trigger_in_app',
  'private method whose only callers are in storeRecentDb (lines 148 and 153), and storeRecentDb is commented out (lines 145-154; its call at line 85 is commented out too); no caller record in auto_calls.json',
  'SRC sync/SyncServiceMessageHandler.java:131-133 (declaration at 131), 85, 145-154 (commented); label_126.grep.txt section A',
  'SOURCE')

# ---- UNREACHABLE: a branch that no sender reaches (branch_never_taken, SOURCE)

UNREACHABLE['SyncServiceMessageHandler.showProgressDialog'] = ('branch_never_taken',
  'called only from the STARTING_DOWNLOAD case of handleMessage (line 77-82, call at 79); no code in the app sends SyncServiceMessage.STARTING_DOWNLOAD, since the code appears only as a declaration and a case label (label_126.grep.txt sections B and E). The auto CALL at line 79 is cut (sup, D18)',
  'SRC sync/SyncServiceMessageHandler.java:77-82 (call at 79), 135-143 (declaration); SRC sync/SyncServiceMessage.java:28; label_126.grep.txt sections B and E',
  'SOURCE')

# ---- UNREACHABLE: Dagger-generated MembersInjector methods with no caller (no_trigger_in_app, INFERRED; D5, D12)

UNREACHABLE['SyncServiceMessageHandler_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (not in the source root). Its only caller is SyncServiceMessageHandler_MembersInjector.create, which has no caller record; no class file outside the owner references it (label_126.grep.txt section F)',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncServiceMessageHandler_MembersInjector.class bytecode line 25 (create -> <init>); auto_calls.json 42944-42947; label_126.grep.txt sections C and F',
  'INFERRED')

UNREACHABLE['SyncServiceMessageHandler_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (not in the source root). No caller record in auto_calls.json; no class file outside the owner references create (label_126.grep.txt section F, 0 external references)',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncServiceMessageHandler_MembersInjector.class bytecode line 25 (its only outgoing call); auto_calls.json 42944-42947; label_126.grep.txt sections C and F',
  'INFERRED')

UNREACHABLE['SyncServiceMessageHandler_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (not in the source root). No caller record for any receiver in auto_calls.json. The only reference in the build is a self-reference inside the class (INFERRED: the compiler bridge for MembersInjector<T>.injectMembers); the component calls injectMDatabases directly (DaggerMmxComponent.class bytecode line 554 record). label_126.grep.txt section F',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncServiceMessageHandler_MembersInjector.class bytecode line 30; auto_calls.json 42952-42955; label_126.grep.txt sections C and F',
  'INFERRED')

UNREACHABLE['SyncService_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Dagger-generated constructor (not in the source root). Its only caller is SyncService_MembersInjector.create, which has no caller record; no class file outside the owner references it (label_126.grep.txt section F)',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncService_MembersInjector.class bytecode line 21 (create -> <init>); auto_calls.json 42834-42837; label_126.grep.txt sections C and F',
  'INFERRED')

UNREACHABLE['SyncService_MembersInjector.create'] = ('no_trigger_in_app',
  'Dagger-generated static factory (not in the source root). No caller record in auto_calls.json; no class file outside the owner references create (label_126.grep.txt section F, 0 external references)',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncService_MembersInjector.class bytecode line 21 (its only outgoing call); auto_calls.json 42834-42837; label_126.grep.txt sections C and F',
  'INFERRED')

UNREACHABLE['SyncService_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'Dagger-generated instance method (not in the source root). No caller record for any receiver in auto_calls.json. The only reference in the build is a self-reference inside the class (INFERRED: the compiler bridge for MembersInjector<T>.injectMembers); the component calls injectRecentDatabasesProvider directly (DaggerMmxComponent.class bytecode line 597 record). label_126.grep.txt section F',
  'final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/sync/SyncService_MembersInjector.class bytecode line 26; auto_calls.json 42842-42845; label_126.grep.txt sections C and F',
  'INFERRED')
