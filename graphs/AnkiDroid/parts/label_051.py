# AnkiDroid batch 051 (LABEL helper). BackupManager (21 methods, including BackupManager$1), CollectionHelper (7 methods
# and CollectionHelper$LazyHolder.<init>) and CustomExceptionHandler (10 methods). The full row list is in
# graphs/AnkiDroid/parts/label_051.md.
#
# Route ownership:
# - The bytecode CALL edges, including the creation of the anonymous thread (BackupManager$1.<init>, BackupManager.java:174),
#   come from auto_calls.json. They are not written here.
# - The ASYNC edge from performBackupInBackground(String,int,boolean) into BackupManager$1.run (thread.start() at
#   BackupManager.java:202) is written here, because its source method is in this batch.
#
# UNREACHABLE entries: 15 (all no_trigger_in_app). The reasons repeat the reasons in label_051.md.

e('BackupManager.performBackupInBackground(String,int,boolean)', 'BackupManager$1.run', 'ASYNC',
  'the backup thread is started with thread.start() after the guards pass',
  env=None,
  evidence='SRC com/ichi2/anki/BackupManager.java:174-202',
  note='The guards are at BackupManager.java:105-164. The run body (zip of the collection, then deleteDeckBackups at line 193) is batch 051 as well. thread.start() is plain java.lang.Thread, not framework code.')

UNREACHABLE['BackupManager.<init>'] = ('no_trigger_in_app',
  "The constructor is private and the class is a static utility. No code in the source root creates a BackupManager (grep for new BackupManager finds nothing).",
  'com/ichi2/anki/BackupManager.java:60-62', 'SOURCE')

UNREACHABLE['BackupManager.deleteDeckBackups(File,int)'] = ('no_trigger_in_app',
  "No caller. The String overload (line 331) and the backup run body (line 193, a String path) bind to other overloads. No call in the source root passes a File to this overload.",
  'com/ichi2/anki/BackupManager.java:335-337, 330-332, 193', 'SOURCE')

UNREACHABLE['BackupManager.isActivated'] = ('no_trigger_in_app',
  "No caller in the source root (grep finds only the declaration). mUseBackups is set only at its declaration (line 53, true), so the method would return true if called.",
  'com/ichi2/anki/BackupManager.java:53, 65-67', 'SOURCE')

UNREACHABLE['BackupManager.performBackupInBackground(String,int)'] = ('no_trigger_in_app',
  "No caller. The one-argument call (DeckPicker.java:807) and the (String,boolean) call (DeckTask.java:814) bind to other overloads. The (String) and (String,boolean) overloads call (String,int,boolean) directly (lines 89 and 94).",
  'com/ichi2/anki/BackupManager.java:98-100, 88-95; com/ichi2/anki/DeckPicker.java:807; com/ichi2/async/DeckTask.java:814', 'SOURCE')

UNREACHABLE['CollectionHelper$LazyHolder.<init>'] = ('no_trigger_in_app',
  "The implicit constructor of the private holder class is never invoked. getInstance (line 76) reads the static field INSTANCE, which runs the holder static initializer, not an instance constructor. No other reference to LazyHolder exists in the source root.",
  'com/ichi2/anki/CollectionHelper.java:68-70, 75-77', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.<init>'] = ('no_trigger_in_app',
  "The class has no explicit constructor, so this is the default constructor. The only instantiation is in getInstance (line 50), and getInstance has no caller in src/main/java (the only reference, AnkiDroidApp.java:249, is commented out).",
  'com/ichi2/anki/CustomExceptionHandler.java:38, 48-51; com/ichi2/anki/AnkiDroidApp.java:249', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.collectInformation'] = ('no_trigger_in_app',
  "Private. Its only caller is the 4-arg uncaughtException (line 136). That method is reached only through the 3-arg and 2-arg overloads and the JVM dispatch, and no instance of the class is ever created (see <init>), so no route exists.",
  'com/ichi2/anki/CustomExceptionHandler.java:83-119, 136', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.getAvailableInternalMemorySize'] = ('no_trigger_in_app',
  "Private helper. Its only caller is collectInformation (line 113), which is unreachable (see collectInformation).",
  'com/ichi2/anki/CustomExceptionHandler.java:65-71, 113', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.getInstance'] = ('no_trigger_in_app',
  "Static accessor. The only reference to the class outside its own file is the commented-out call at AnkiDroidApp.java:249. grep of src/main/java for CustomExceptionHandler and UncaughtExceptionHandler finds no other caller.",
  'com/ichi2/anki/CustomExceptionHandler.java:48-55; com/ichi2/anki/AnkiDroidApp.java:249', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.getTotalInternalMemorySize'] = ('no_trigger_in_app',
  "Private helper. Its only caller is collectInformation (line 112), which is unreachable (see collectInformation).",
  'com/ichi2/anki/CustomExceptionHandler.java:74-80, 112', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.init'] = ('no_trigger_in_app',
  "Public, with no caller in src/main/java. It is the only place that calls Thread.setDefaultUncaughtExceptionHandler(this) (line 60), so the handler is never installed. It also needs an instance, and getInstance has no caller.",
  'com/ichi2/anki/CustomExceptionHandler.java:58-62; com/ichi2/anki/AnkiDroidApp.java:249', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.saveReportToFile'] = ('no_trigger_in_app',
  "Private. Its only caller is the 4-arg uncaughtException (line 192), which is unreachable (see uncaughtException(Thread,Throwable,String,String)).",
  'com/ichi2/anki/CustomExceptionHandler.java:200-217, 192', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.uncaughtException(Thread,Throwable)'] = ('no_trigger_in_app',
  "The @Override of Thread.UncaughtExceptionHandler. It runs only when this object is installed as a default or per-thread handler. No instance is ever created (getInstance has no caller), and init (the only installer, line 60) has no caller. No direct caller exists in src/main/java.",
  'com/ichi2/anki/CustomExceptionHandler.java:122-125, 58-62', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.uncaughtException(Thread,Throwable,String)'] = ('no_trigger_in_app',
  "Public overload. Its only caller in the class is the 2-arg uncaughtException (line 124). No caller exists outside the class, and the instance route is missing (see the 2-arg row).",
  'com/ichi2/anki/CustomExceptionHandler.java:128-130, 124', 'SOURCE')

UNREACHABLE['CustomExceptionHandler.uncaughtException(Thread,Throwable,String,String)'] = ('no_trigger_in_app',
  "Public overload. Its only caller in the class is the 3-arg overload (line 129). The one outside reference, AnkiDroidApp.java:249, is commented out. The body calls collectInformation (line 136) and saveReportToFile (line 192).",
  'com/ichi2/anki/CustomExceptionHandler.java:133-197; com/ichi2/anki/AnkiDroidApp.java:249', 'SOURCE')
