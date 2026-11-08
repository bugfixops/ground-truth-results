# AnkiDroid batch 127 (LABEL helper). ActivityTransitionAnimation, AnkiActivity, AnkiDroidApp,
# AnkiDroidApp$ProductionCrashReportingTree, CollectionHelper, CollectionHelper$LazyHolder: 36 methods.
# The full row list is in graphs/AnkiDroid/parts/label_127.md.
#
# Route ownership:
# - Bytecode CALL edges between the methods of this batch and into them are written by the builder. They are not
#   repeated here.
# - Guard-less automatic CALL to suppress (not written here): AnkiDroidApp.onCreate -> AnkiDroidApp$ProductionCrashReportingTree.<init>.
#   The new at AnkiDroidApp.java:166 sits in the else branch of if (BuildConfig.DEBUG), which is never taken in the debug APK.
# - The S_ENTRY edge into AnkiDroidApp.onCreate is already in graph_def.py (lines 143-144) and is not repeated.
#
# Gates: no MG ids are used. No predefined ENV or STATE constant is needed for these two edges.

# --- Process start: the framework creates the Application, which initialises AnkiDroidApp first.
e('S_ENTRY', 'AnkiDroidApp.<clinit>', 'FRAMEWORK',
  'the process starts and the framework creates the Application, which initialises AnkiDroidApp first',
  env=None,
  evidence='FW-SRC core/java/android/app/Instrumentation.java:1099-1104; SRC com/ichi2/anki/AnkiDroidApp.java:119-139',
  note='Same route as the existing S_ENTRY to AnkiDroidApp.<init> (graph_def.py lines 310-314). The JVM class-initialisation step is not in fw_src: INFERRED.')

# --- Loader restart in startLoadingCollection; the loader framework calls back onCreateLoader.
e('AnkiActivity.startLoadingCollection', 'AnkiActivity.onCreateLoader', 'FRAMEWORK',
  'the collection loader is restarted and the loader framework calls back onCreateLoader',
  env=None,
  evidence='SRC com/ichi2/anki/AnkiActivity.java:254-262, 275-279',
  note='restartLoader (AnkiActivity.java:261) is not gated in startLoadingCollection. The support-library LoaderManager is not in fw_src: INFERRED.')

# --- UNREACHABLE: the crash reporting tree is only created in the release branch (BuildConfig.DEBUG is false there).
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.<clinit>'] = ('closed_by_configuration', 'The only construction of the tree is Timber.plant(new ProductionCrashReportingTree()) at AnkiDroidApp.java:166, in the else branch of if (BuildConfig.DEBUG) (AnkiDroidApp.java:155 and 164). The dataset APK is a debug build (final_java_only/AnkiDroid/app/DATASET.txt:4), so BuildConfig.DEBUG is true and that branch is never taken. No other reference to the class exists in the source root.', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-167, 383-386; final_java_only/AnkiDroid/app/DATASET.txt:4', 'SOURCE')

UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.<init>'] = ('closed_by_configuration', 'The constructor runs only from the new at AnkiDroidApp.java:166, in the else branch of if (BuildConfig.DEBUG) (AnkiDroidApp.java:155 and 164). The dataset APK is a debug build (final_java_only/AnkiDroid/app/DATASET.txt:4), so BuildConfig.DEBUG is true and that branch is never taken. The automatic CALL from AnkiDroidApp.onCreate to this constructor must be suppressed.', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-167, 383-386; final_java_only/AnkiDroid/app/DATASET.txt:4', 'SOURCE')
