# AnkiDroid batch 080 (LABEL helper). MethodLogger, Threads, VersionUtils, WidgetStatus (with UpdateDeckStatusAsyncTask),
# AnkiExporter and AnkiPackageExporter (APKG export). 34 methods; the full row list is in graphs/AnkiDroid/parts/label_080.md.
#
# Route ownership: the two INTENT edges from WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute are written here (the source
# is in this batch). The ASYNC edge into onPostExecute is written by the batch that contains WidgetStatus.update. Automatic CALL
# edges come from auto_calls.json and are not written here. Gate: STATE_SETTINGS (widget and notification preferences).
# No MG id is needed.

e('WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute', 'AnkiDroidWidgetSmall$UpdateService.<init>', 'INTENT',
  'the status task starts the small widget service when the widget preference is enabled',
  guard='sSmallWidgetEnabled is true (set in WidgetStatus.update from widgetSmallEnabled, WidgetStatus.java:55); the start is at WidgetStatus.java:106-110',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/widget/WidgetStatus.java:55, 106-110; SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:77',
  note='Explicit intent start (WidgetStatus.java:108-109). The framework creates the service through its constructor; the next hop UpdateService.onStart is the LIFECYCLE edge in label_018.py. Gate STATE_SETTINGS (widget preference). env None: the start needs no outside event.')

e('WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute', 'NotificationService.<init>', 'INTENT',
  'the status task starts the notification service when the notification preference is enabled',
  guard='sNotificationEnabled is true (set in WidgetStatus.update from minimumCardsDueForNotification, WidgetStatus.java:56); the start is at WidgetStatus.java:111-115',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/widget/WidgetStatus.java:56, 111-115; SRC com/ichi2/anki/services/NotificationService.java:37',
  note='Explicit intent start (WidgetStatus.java:113-114). The framework creates the service through its constructor; the next hops NotificationService.onCreate and onStartCommand are the FRAMEWORK edge in label_049.py. Gate STATE_SETTINGS (notification preference). env None: the start needs no outside event.')

UNREACHABLE['MethodLogger.<init>'] = ('no_trigger_in_app', 'Private constructor of a static utility class. grep for new MethodLogger over the source root finds nothing.', 'SRC com/ichi2/utils/MethodLogger.java:42-45', 'SOURCE')

UNREACHABLE['MethodLogger.log()'] = ('branch_never_taken', 'The seven callers in BaseAsyncTask are MethodLogger.log() calls inside if (DEBUG) blocks. DEBUG is the constant false, so the calls never run and javac emits no bytecode for them. No other caller exists in the source root.', 'SRC com/ichi2/async/BaseAsyncTask.java:27, 39-40, 47-48, 56-57, 66-67, 76-77, 86-87, 96-97; SRC com/ichi2/utils/MethodLogger.java:61-63', 'SOURCE')

UNREACHABLE['MethodLogger.log(String)'] = ('no_trigger_in_app', 'No call site. The source root has no call to log(String). MethodLogger.java:36 is a javadoc example, not code, and the BaseAsyncTask calls use log() with no argument.', 'SRC com/ichi2/utils/MethodLogger.java:36, 53-55; SRC com/ichi2/async/BaseAsyncTask.java:40', 'SOURCE')

UNREACHABLE['MethodLogger.logInternal'] = ('no_trigger_in_app', 'Private helper. Its callers are log(String), which has no call site, and log(), which is reached only under the constant-false DEBUG branch. No trigger in the app reaches it.', 'SRC com/ichi2/utils/MethodLogger.java:54, 62, 73-107', 'SOURCE')

UNREACHABLE['Threads.<init>'] = ('no_trigger_in_app', 'Private constructor of a static utility class. grep for new Threads over the source root finds nothing.', 'SRC com/ichi2/utils/Threads.java:26-27', 'SOURCE')

UNREACHABLE['Threads.newCurrentThreadChecker'] = ('no_trigger_in_app', 'Factory with no caller in the source root. grep for newCurrentThreadChecker finds only its declaration.', 'SRC com/ichi2/utils/Threads.java:59-60', 'SOURCE')

UNREACHABLE['Threads.newLazySingleThreadChecker'] = ('no_trigger_in_app', 'Factory with no caller in the source root. grep for newLazySingleThreadChecker finds only its declaration.', 'SRC com/ichi2/utils/Threads.java:69-70', 'SOURCE')

UNREACHABLE['Threads.newSingleThreadChecker'] = ('no_trigger_in_app', 'Factory with no caller in the source root. grep for newSingleThreadChecker and SingleThreadChecker finds only Threads.java.', 'SRC com/ichi2/utils/Threads.java:48-52', 'SOURCE')

UNREACHABLE['Threads$SingleThreadChecker.<init>'] = ('no_trigger_in_app', 'Private constructor. Its only callers are the three factories above (Threads.java:52, 60, 70), and none of those factories has a caller.', 'SRC com/ichi2/utils/Threads.java:52, 60, 70, 123-124', 'SOURCE')

UNREACHABLE['Threads$SingleThreadChecker.checkThread'] = ('no_trigger_in_app', 'No call site in the source root (grep for checkThread finds only Threads.java). The checker object is built only by the unreached factories.', 'SRC com/ichi2/utils/Threads.java:129-136', 'SOURCE')

UNREACHABLE['VersionUtils.<init>'] = ('no_trigger_in_app', 'No explicit constructor (VersionUtils.java:14 is the class line; the implicit constructor is never used). grep for new VersionUtils finds nothing, and every caller uses a static method.', 'SRC com/ichi2/utils/VersionUtils.java:14', 'SOURCE')

UNREACHABLE['WidgetStatus.<init>'] = ('no_trigger_in_app', 'Private constructor ("This class should not be instantiated"). grep for new WidgetStatus finds nothing.', 'SRC com/ichi2/widget/WidgetStatus.java:46-47', 'SOURCE')
