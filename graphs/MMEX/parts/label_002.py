# batch 002: MmexApplication (27 methods). Edges and UNREACHABLE entries only; the section-B edge S_ENTRY -> MmexApplication.<init> already exists in graph_def.py.

e('S_ENTRY', 'MmexApplication.<clinit>', 'ENTRY',
  'The process starts; the framework creates the Application class by name, which initializes the class (static fields) before the constructor',
  evidence='SRC AndroidManifest.xml:55; SRC MmexApplication.java:77; FW-SRC core/java/android/app/Instrumentation.java:1099-1103; JVM class initialization is not in fw_src: INFERRED, source not read')

e('MmexApplication.<init>', 'MmexApplication.attachBaseContext', 'LIFECYCLE',
  'The framework attaches the base context to the new Application before onCreate',
  evidence='SRC MmexApplication.java:216-218; FW-SRC core/java/android/app/Instrumentation.java:1099-1103 (app.attach(context)); Application.attach is not in fw_src: INFERRED, source not read')

e('MmexApplication.<init>', 'MmexApplication.onCreate', 'LIFECYCLE',
  'The framework calls Application.onCreate after attaching the base context (process start, before any component)',
  evidence='SRC MmexApplication.java:114-116; FW-SRC core/java/android/app/Instrumentation.java:1118-1120; FW-SRC core/java/android/app/LoadedApk.java:983-999; FW-SRC core/java/android/app/ActivityThread.java:5715-5740')

e('MmexApplication.onCreate', 'MmexApplication.lambda$onCreate$0', 'REGISTER',
  'onCreate passes the configuration lambda to the Amplitude client builder, which calls it while it builds the client',
  evidence='SRC MmexApplication.java:147-154; library com.amplitude.android is not in the dataset: its call of the lambda is INFERRED, source not read')

UNREACHABLE['MmexApplication.onTerminate'] = (
  'framework_never_calls',
  'The framework calls onTerminate only from the EXIT_APPLICATION handler, which runs only after ActivityThread.scheduleExit; the two ActivityManagerService callers of scheduleExit run only for pid <= 0 or the system_server pid, never for an app process (the other branches call killProcessQuiet or app.kill). No in-app caller.',
  'MmexApplication.java:207-214',
  'SOURCE')

UNREACHABLE['MmexApplication.killApplication'] = (
  'no_trigger_in_app',
  'Public static method that kills the process; the app src tree has no caller and no XML or reflective reference (grep shows only the definition at line 102).',
  'MmexApplication.java:99-105',
  'SOURCE')
