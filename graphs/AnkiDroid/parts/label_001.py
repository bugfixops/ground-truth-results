# AnkiDroid batch 001 (LABEL helper). Writes the S_ENTRY edges whose destination is a method in this
# batch, plus one edge between two methods of this batch: IntentHandler$1.<init> -> IntentHandler$1.onPositive
# (FRAMEWORK, as directed by the coordinator). Other edges between methods of this batch are not written here:
# the route into each method passes through nodes owned by other batches
# (see graphs/AnkiDroid/scratch/conflicts_001.md).
# ENV_CONFIG_CHANGE is the constant requested by the coordinator; it is added at merge.

e('S_ENTRY', 'AnkiDroidApp.<init>', 'FRAMEWORK',
  'process start: the framework creates the Application object',
  env=None,
  note='Default constructor of AnkiDroidApp. The S_ENTRY to AnkiDroidApp.onCreate edge already exists in graph_def.py (line 142).',
  evidence='FW-SRC core/java/android/app/LoadedApk.java:983-984; FW-SRC core/java/android/app/Instrumentation.java:1099-1102; SRC com/ichi2/anki/AnkiDroidApp.java:111')

e('S_ENTRY', 'IntentHandler.<init>', 'FRAMEWORK',
  'launcher, VIEW .apkg, or DO_SYNC intent starts the IntentHandler activity',
  env=None,
  note='Default constructor of the IntentHandler activity. The S_ENTRY to IntentHandler.onCreate edges already exist in graph_def.py (lines 138-140).',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2669-2670; FW-SRC core/java/android/app/Instrumentation.java:1170-1174; SRC com/ichi2/anki/IntentHandler.java:36; SRC AndroidManifest.xml:85-89')

e('S_ENTRY', 'AnkiDroidApp.onConfigurationChanged', 'SYSTEM',
  'system configuration change (rotation or locale) delivered to the Application',
  env=ENV_CONFIG_CHANGE,
  note='NEW CONST ENV_CONFIG_CHANGE',
  evidence='SRC com/ichi2/anki/AnkiDroidApp.java:204-209; FW-SRC core/java/android/app/ActivityThread.java:5040')

e('IntentHandler$1.<init>', 'IntentHandler$1.onPositive', 'FRAMEWORK',
  'the user taps the positive button of the dialog that IntentHandler.onCreate builds with the callback IntentHandler$1 (registered in its constructor)',
  env=None,
  note='Written as FRAMEWORK, not REGISTER: the builder does not follow REGISTER edges for reachability, so REGISTER would leave onPositive unreachable. IntentHandler$1.<init> is the anonymous ButtonCallback creation at IntentHandler.java:118; its batch owner is unknown (see conflicts_001.md).',
  evidence='SRC com/ichi2/anki/IntentHandler.java:118; SRC com/ichi2/anki/IntentHandler.java:120')

UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.createTag'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.e(String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.e(Throwable,String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.formatString'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.i(String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.i(Throwable,String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.w(String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
UNREACHABLE['AnkiDroidApp$ProductionCrashReportingTree.w(Throwable,String,Object[])'] = ('closed_by_configuration', 'the planted tree is the release tree; the dataset APK is the debug build (DATASET.txt apk line), so BuildConfig.DEBUG is true and the else branch never runs', 'SRC com/ichi2/anki/AnkiDroidApp.java:155-166', 'SOURCE')
