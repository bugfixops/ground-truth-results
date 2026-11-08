# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# C12 converter delivery (2026-11-01): audited A3 base copied unchanged except this header.
# No UNREACHABLE rows: stronger-evidence rule (b) is vacuous; no grade changes.
# No merger notes for this batch. Delivered printed evidence: parts/b079_printed.txt (fresh, from clone tree).
# Batch 79 part (AddTorrentActivity callbacks and AddTorrent fragments (part 1)). Hand-written edges only.
# Each evidence string cites lines printed in
# helper/a3-g16/scratch/b079_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
# Rows whose route already exists in merger-tree graph_def.py are
# listed in the .md Dependencies line and are NOT repeated here.

e('AddTorrentActivity.onCreate', 'AddTorrentActivity$1.<init>', 'CALL', 'Activity creates its permission callback in onCreate',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:105-129')
e('PermissionManager.lambda$new$1', 'AddTorrentActivity$1.onNotificationResult', 'RESULT', 'Runtime permission result delivered to the activity callback',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/PermissionManager.java:70-92; SRC ui/addtorrent/AddTorrentActivity.java:120-125')
e('PermissionManager.lambda$new$0', 'AddTorrentActivity$1.onStorageResult', 'RESULT', 'Manage-all-files settings result delivered to the activity callback',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/PermissionManager.java:60-68; SRC ui/addtorrent/AddTorrentActivity.java:107-118')
e('AddTorrentActivity.<init>', 'AddTorrentActivity$2.<init>', 'CALL', 'Field initialiser creates the mutable-params change callback',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:201-203')
e('AddTorrentActivity.subscribeParamsChanged', 'AddTorrentActivity$2.onPropertyChanged', 'REGISTER', 'Params-changed callback registered on the mutable params',
  cls='non_standard', via='Data-binding Observable dispatch on notifyPropertyChanged', evidence='SRC ui/addtorrent/AddTorrentActivity.java:193-195; SRC ui/addtorrent/AddTorrentActivity.java:204-233')
e('AddTorrentFilesFragment.newInstance', 'AddTorrentFilesFragment.<clinit>', 'FRAMEWORK', 'First use of the fragment class runs its static initialisers',
  cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation; SRC ui/addtorrent/AddTorrentFilesFragment.java:55,57,68-76')
e('AddTorrentFilesFragment.onStart', 'AddTorrentFilesFragment.onResume', 'LIFECYCLE', 'Fragment resumes after starting',
  evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:104-109; SRC ui/addtorrent/AddTorrentFilesFragment.java:174-180')
e('AddTorrentFilesFragment.onResume', 'AddTorrentFilesFragment.onSaveInstanceState', 'LIFECYCLE', 'Instance state saved after resume, before stop',
  evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:174-180; SRC ui/addtorrent/AddTorrentFilesFragment.java:156-162')
e('AddTorrentFilesFragment.onResume', 'AddTorrentFilesFragment.onStop', 'LIFECYCLE', 'Fragment stops after resume',
  evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:174-180; SRC ui/addtorrent/AddTorrentFilesFragment.java:96-101')
e('AddTorrentFilesFragment.onViewCreated', 'AddTorrentFilesFragment.onViewStateRestored', 'LIFECYCLE', 'View state restored after the view is created',
  evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:128-141; SRC ui/addtorrent/AddTorrentFilesFragment.java:165-171')
e('AddTorrentInfoFragment.newInstance', 'AddTorrentInfoFragment.<clinit>', 'FRAMEWORK', 'First use of the fragment class runs its static initialisers',
  cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation; SRC ui/addtorrent/AddTorrentInfoFragment.java:65,67,74-81')
e('PermissionManager.lambda$new$1', 'AddTorrentActivity$1.onStorageResult', 'RESULT', 'Runtime permission storage result delivered to the activity callback',
  cls='non_standard', via='AndroidX Activity Result API', evidence='INFERRED AndroidX ActivityResultLauncher dispatch; SRC ui/PermissionManager.java:70-85; SRC ui/addtorrent/AddTorrentActivity.java:107-118')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No UNREACHABLE rows in this batch and no REACHABLE method of this
# group calls an UNREACHABLE method in bytecode (see REPORT.md),
# so no SUPPRESS entries apply.
SUPPRESS.update(set())
