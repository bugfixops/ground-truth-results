# ================================================================== batch 096 (label_096): 33 methods (graphs/MMEX/AGENT_NOTES.md batch table, row 096): ExceptionHandler (15: constructors, e, getters, showMessage, uncaughtException, sendEmail, anonymous Runnable $1), FileLoggingTree (2), ScreenTree (2), SysLogTree (2), RecurringTransactionIntentService (4), RecurringTransactionReceiver (2), RecurringTransactionNotifications (6).
# Rows, printed lines and counts: graphs/MMEX/parts/label_096.md (22 REACHABLE, 11 UNREACHABLE, 0 INCOMPLETE).
# Grep and sed evidence: graphs/MMEX/parts/label_096.grep.txt (sections 1-16).
# This file writes:
#   - 0 SCREENS keys (no GUI method in this batch; the toast is a Handler post, not a page);
#   - 9 e() edges, each with a destination in this batch (D1): 1 FRAMEWORK from batch 038 RecurringTransactionBootReceiver.setAlarm into RecurringTransactionReceiver.<init> (the alarm broadcast); 1 LIFECYCLE from that <init> to onReceive; 2 FRAMEWORK from RecurringTransactionIntentService.enqueueWork (JobIntentService) to its <init> and onHandleWork; 1 FRAMEWORK (Handler.post) from ExceptionHandler.showMessage(String,int) to $1.run; 4 CALL (cls non_standard, release-only Timber trees) from the two Timber.e call sites in RecurringTransactionNotifications (lines 56 and 127) to ScreenTree.log and SysLogTree.log;
#   - 11 UNREACHABLE entries: 9 for ExceptionHandler (app source, SOURCE) and 2 for FileLoggingTree (never planted, SOURCE);
#   - 12 sup pairs (D14): the auto CALL records whose caller is UNREACHABLE in this batch (e(Exception,String), e(Throwable,String), uncaughtException, getAppVersionInformation, getAppVersion, getAppBuildNumber).
# Not written (D7): every other auto CALL record into or inside this batch (for example MmexApplication.onCreate -> ScreenTree.<init> and SysLogTree.<init>; FormatUtilities and RecurringTransactionListFragment -> ExceptionHandler.<init>(Context,Object) and showMessage; MainActivity -> RecurringTransactionNotifications; Receiver.onReceive -> IntentService.enqueueWork and <clinit>; ExceptionHandler$1.<init>; $1.run -> getLogcat). They come from graphs/MMEX/auto_calls.json and carry no needs_state.
# Known gaps: (a) the auto record ExceptionHandler$1.run -> getLogcat sits in the catch block (lines 118-119, the exception path only) and is shown as a normal route; (b) the Timber.e call at RecurringTransactionBootReceiver.java:45 (batch 038 call site, merged) is not written here: it would also dispatch to ScreenTree and SysLogTree, and the batch 096 routes do not depend on it; (c) the settings gate sits on the two receiver edges only, not on the auto records.

# ================================================================== alarm route from the boot receiver (batch 038 setAlarm) into the notification receiver

e('RecurringTransactionBootReceiver.setAlarm', 'RecurringTransactionReceiver.<init>', 'FRAMEWORK',
  'setAlarm schedules a daily repeating AlarmManager alarm whose PendingIntent is a broadcast to RecurringTransactionReceiver; when the alarm fires the system creates the receiver instance to deliver the broadcast',
  needs_state=state_text('the repeating transaction notifications setting is on (default on, BehaviourSettings.java:42)', ('settings',)),
  env=env_text('the daily alarm fires at the notification time (the hour set in the settings)', ('time',)),
  via='AlarmManager repeat with a broadcast PendingIntent (AlarmManager delivery and the framework are not read: INFERRED)',
  evidence='SRC core/RecurringTransactionBootReceiver.java:49-53 (notify gate), 56-57 (intent and PendingIntent.getBroadcast), 59-78 (hour and calendar), 79-84 (cancel at 81, setRepeating at 83-84); SRC notifications/RecurringTransactionReceiver.java:31-39; SRC settings/BehaviourSettings.java:41-43; INFERRED AlarmManager delivery (not read)')

e('RecurringTransactionReceiver.<init>', 'RecurringTransactionReceiver.onReceive', 'LIFECYCLE',
  'the system calls onReceive on the new receiver instance; onReceive reads the notification setting and returns when it is off, otherwise it enqueues the job service (lines 37-38)',
  guard='the setting is on (lines 33-35; the default is true)',
  needs_state=state_text('the repeating transaction notifications setting is on (default on, BehaviourSettings.java:42)', ('settings',)),
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3185-3188 (receiver.onReceive at 3187); SRC notifications/RecurringTransactionReceiver.java:31-39')

# ================================================================== the job service (JobIntentService, androidx library not read: INFERRED)

e('RecurringTransactionIntentService.enqueueWork', 'RecurringTransactionIntentService.<init>', 'FRAMEWORK',
  'JobIntentService.enqueueWork queues the work for this service; the system creates the job service instance to run it',
  via='androidx JobIntentService (library not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionIntentService.java:33, 46-48 (the static enqueueWork calls JobIntentService.enqueueWork with JOB_ID); SRC AndroidManifest.xml:398-400 (service with BIND_JOB_SERVICE); INFERRED androidx JobIntentService (library not read)')

e('RecurringTransactionIntentService.enqueueWork', 'RecurringTransactionIntentService.onHandleWork', 'FRAMEWORK',
  'the JobIntentService worker delivers the queued intent to onHandleWork, which builds the notifications object and calls notifyRepeatingTransaction (lines 42-43; these two CALL records are in auto_calls.json)',
  via='JobIntentService worker thread (library not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionIntentService.java:39-48; INFERRED androidx JobIntentService dispatch (library not read)')

# ================================================================== the toast Runnable (Handler.post on the main looper; framework source read)

e('ExceptionHandler.showMessage(String,int)', 'ExceptionHandler$1.run', 'FRAMEWORK',
  'the handler posts the anonymous Runnable to the main looper; the main thread runs it and shows the toast (line 117)',
  guard='mContext is not null (line 111; showMessage returns before the post otherwise)',
  via='Handler.post queues a message with the Runnable as its callback; dispatchMessage runs handleCallback, which calls callback.run() (FW-SRC Handler.java:355-357, 97-99, 789-790)',
  evidence='SRC log/ExceptionHandler.java:110-117 (Handler on the main looper at 113, post at 114, run body at 115-117); FW-SRC core/java/android/os/Handler.java:355-357, 97-99, 789-790')

# ================================================================== Timber calls in batch 096 dispatch to the release-only trees (library dispatch INFERRED)

e('RecurringTransactionNotifications.notifyRepeatingTransaction', 'ScreenTree.log', 'CALL',
  'the Timber.e call in the catch block (line 56) hands the exception to the planted trees; in the release build the planted ScreenTree.log runs and posts ErrorRaisedEvent when a subscriber exists',
  guard='release build only: ScreenTree is planted in the else branch (MmexApplication.java:136-139); the debug build plants DebugTree instead (line 135)',
  env=env_text('an exception is thrown while the recurring transaction notification is built or shown (the catch at line 55)', ('other',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 56) calls each planted Tree.log (library source not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionNotifications.java:52-58 (Timber.e at 56); SRC MmexApplication.java:134-140; SRC log/ScreenTree.java:15-32 (post at 26-27); INFERRED Timber dispatch (library not read)')

e('RecurringTransactionNotifications.notifyRepeatingTransaction', 'SysLogTree.log', 'CALL',
  'the same Timber.e call (line 56) hands the exception to the planted trees; in the release build the planted SysLogTree.log writes the message to the system log',
  guard='release build only: SysLogTree is planted in the else branch (MmexApplication.java:136-139); the debug build plants DebugTree instead (line 135)',
  env=env_text('an exception is thrown while the recurring transaction notification is built or shown (the catch at line 55)', ('other',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 56) calls each planted Tree.log (library source not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionNotifications.java:52-58 (Timber.e at 56); SRC MmexApplication.java:134-140; SRC log/SysLogTree.java:13-15 (Log.println at 14); INFERRED Timber dispatch (library not read)')

e('RecurringTransactionNotifications.showNotification', 'ScreenTree.log', 'CALL',
  'the Timber.e call in the catch block (line 127) hands the exception to the planted trees; in the release build the planted ScreenTree.log runs and posts ErrorRaisedEvent when a subscriber exists',
  guard='release build only: ScreenTree is planted in the else branch (MmexApplication.java:136-139); the debug build plants DebugTree instead (line 135)',
  env=env_text('an exception is thrown while the notification is created or posted (the catch at line 126)', ('other',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 127) calls each planted Tree.log (library source not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionNotifications.java:82-129 (catch at 126, Timber.e at 127); SRC MmexApplication.java:134-140; SRC log/ScreenTree.java:15-32 (post at 26-27); INFERRED Timber dispatch (library not read)')

e('RecurringTransactionNotifications.showNotification', 'SysLogTree.log', 'CALL',
  'the same Timber.e call (line 127) hands the exception to the planted trees; in the release build the planted SysLogTree.log writes the message to the system log',
  guard='release build only: SysLogTree is planted in the else branch (MmexApplication.java:136-139); the debug build plants DebugTree instead (line 135)',
  env=env_text('an exception is thrown while the notification is created or posted (the catch at line 126)', ('other',)),
  cls='non_standard', via='Timber static dispatch: Timber.e (line 127) calls each planted Tree.log (library source not read: INFERRED)',
  evidence='SRC notifications/RecurringTransactionNotifications.java:82-129 (catch at 126, Timber.e at 127); SRC MmexApplication.java:134-140; SRC log/SysLogTree.java:13-15 (Log.println at 14); INFERRED Timber dispatch (library not read)')

# ================================================================== UNREACHABLE entries (app source, SOURCE: grep evidence in label_096.grep.txt)

UNREACHABLE['ExceptionHandler.<init>(Context)'] = ('no_trigger_in_app',
  'no caller: the app constructs ExceptionHandler only with two arguments (FormatUtilities.java:110, RecurringTransactionListFragment.java:185)',
  'SRC log/ExceptionHandler.java:47-50; label_096.grep.txt sections 1-2', 'SOURCE')

UNREACHABLE['ExceptionHandler.e(Exception,String)'] = ('no_trigger_in_app',
  'no caller: the two call sites use showMessage only (FormatUtilities.java:111, RecurringTransactionListFragment.java:186), and no other class calls e(...)',
  'SRC log/ExceptionHandler.java:72-74; label_096.grep.txt sections 2-3', 'SOURCE')

UNREACHABLE['ExceptionHandler.e(Throwable,String)'] = ('no_trigger_in_app',
  'its only caller is e(Exception,String) (line 73), which has no caller; the auto records from this method (lines 79-82) are cut by the sup pairs below',
  'SRC log/ExceptionHandler.java:72-86; label_096.grep.txt section 16', 'SOURCE')

UNREACHABLE['ExceptionHandler.getAppBuildNumber'] = ('no_trigger_in_app',
  'callers are e(Throwable,String) (line 79) and getAppVersionInformation (line 217), and both are UNREACHABLE',
  'SRC log/ExceptionHandler.java:235-243, 79, 217; label_096.grep.txt sections 5-6', 'SOURCE')

UNREACHABLE['ExceptionHandler.getAppVersion'] = ('no_trigger_in_app',
  'callers are e(Throwable,String) (line 79) and getAppVersionInformation (line 213), and both are UNREACHABLE',
  'SRC log/ExceptionHandler.java:225-233, 79, 213; label_096.grep.txt sections 5-6', 'SOURCE')

UNREACHABLE['ExceptionHandler.getAppVersionInformation'] = ('no_trigger_in_app',
  'its only caller is uncaughtException (line 138), which is UNREACHABLE',
  'SRC log/ExceptionHandler.java:208-223, 138; label_096.grep.txt sections 5-6', 'SOURCE')

UNREACHABLE['ExceptionHandler.getContext'] = ('no_trigger_in_app',
  'callers are getAppVersionInformation (line 209), getAppVersion (line 228) and getAppBuildNumber (line 237), all UNREACHABLE; no class outside the file calls it (grep section 3)',
  'SRC log/ExceptionHandler.java:68-70, 209, 228, 237; label_096.grep.txt sections 3 and 6', 'SOURCE')

UNREACHABLE['ExceptionHandler.sendEmail'] = ('no_trigger_in_app',
  'its only caller is uncaughtException (line 182), which is UNREACHABLE',
  'SRC log/ExceptionHandler.java:193-206, 182; label_096.grep.txt sections 5-6', 'SOURCE')

UNREACHABLE['ExceptionHandler.uncaughtException'] = ('framework_never_calls',
  'nothing registers the handler as the default or a thread uncaught handler (grep section 4); the only mention is the commented line 61; the framework would call it only after such a registration (INFERRED)',
  'SRC log/ExceptionHandler.java:40, 61, 125-126; label_096.grep.txt section 4', 'SOURCE')

UNREACHABLE['FileLoggingTree.<init>'] = ('no_trigger_in_app',
  'never constructed: the app plants DebugTree (debug) or ScreenTree and SysLogTree (release) only (MmexApplication.java:134-140); no other reference to FileLoggingTree in src/main (grep section 7)',
  'SRC log/FileLoggingTree.java:31-32; SRC MmexApplication.java:134-140; label_096.grep.txt section 7', 'SOURCE')

UNREACHABLE['FileLoggingTree.log'] = ('no_trigger_in_app',
  'never planted, so Timber never dispatches to it (grep section 7)',
  'SRC log/FileLoggingTree.java:35-47; label_096.grep.txt section 7', 'SOURCE')

# ================================================================== sup pairs (D14): auto CALL records whose caller is UNREACHABLE in this batch

sup(('ExceptionHandler.e(Exception,String)', 'ExceptionHandler.e(Throwable,String)'),
    ('ExceptionHandler.e(Throwable,String)', 'ExceptionHandler.showMessage(String)'),
    ('ExceptionHandler.e(Throwable,String)', 'ExceptionHandler.getLogcat'),
    ('ExceptionHandler.e(Throwable,String)', 'ExceptionHandler.getAppBuildNumber'),
    ('ExceptionHandler.e(Throwable,String)', 'ExceptionHandler.getAppVersion'),
    ('ExceptionHandler.uncaughtException', 'ExceptionHandler.sendEmail'),
    ('ExceptionHandler.uncaughtException', 'ExceptionHandler.getAppVersionInformation'),
    ('ExceptionHandler.getAppVersionInformation', 'ExceptionHandler.getAppBuildNumber'),
    ('ExceptionHandler.getAppVersionInformation', 'ExceptionHandler.getAppVersion'),
    ('ExceptionHandler.getAppVersionInformation', 'ExceptionHandler.getContext'),
    ('ExceptionHandler.getAppVersion', 'ExceptionHandler.getContext'),
    ('ExceptionHandler.getAppBuildNumber', 'ExceptionHandler.getContext'))
