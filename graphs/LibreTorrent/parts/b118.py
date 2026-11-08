# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 118 part (scheduling/storage/streaming settings fragments, AddTagButton,
# SelectTagActivity, SelectTagDialog.<clinit>). Hand-written edges only for rows
# not already covered by an existing graph_def edge; the remaining rows are
# listed in the .md Dependencies line with their graph_def edges.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b118_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.

# Scheduling: Rx event lambda runs when the dialog ViewModel emits.
e('SchedulingSettingsFragment.subscribeAlertDialog', 'SchedulingSettingsFragment.lambda$subscribeAlertDialog$0', 'CALL', 'Alert-dialog event lambda checks the exact-alarm dialog tag and requests the permission', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/settings/sections/SchedulingSettingsFragment.java:129-141')
# Scheduling: alarm that cannot be set shows the exact-alarm permission dialog.
e('SchedulingSettingsFragment.onPreferenceChange', 'SchedulingSettingsFragment.showExactAlarmPermissionDialog', 'CALL', 'Unsettable start/stop alarm shows the exact-alarm permission dialog', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:201,214,224,230; SRC ui/settings/sections/SchedulingSettingsFragment.java:143-161')
# Scheduling: start subscribes to dialog events.
e('SchedulingSettingsFragment.onStart', 'SchedulingSettingsFragment.subscribeAlertDialog', 'CALL', 'Fragment start subscribes to alert-dialog events', evidence='SRC ui/settings/sections/SchedulingSettingsFragment.java:126; SRC ui/settings/sections/SchedulingSettingsFragment.java:129-141')
# Scheduling: tapping a TimePreference shows its dialog through the framework callback.
e('SchedulingSettingsFragment.onCreatePreferences', 'SchedulingSettingsFragment.onDisplayPreferenceDialog', 'CALL', 'Framework shows the TimePreference dialog when its preference is tapped', cls='non_standard', via='PreferenceFragmentCompat dialog dispatch', evidence='INFERRED framework dialog dispatch; SRC ui/settings/sections/SchedulingSettingsFragment.java:175-189')
# Storage: class initialisation on first use via newInstance (TAG field).
e('StorageSettingsFragment.newInstance', 'StorageSettingsFragment.<clinit>', 'FRAMEWORK', 'Initialize TAG before first storage settings use', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:54; SRC ui/settings/sections/StorageSettingsFragment.java:64-69')
# Storage: framework saves the dir-chooser binding preference.
e('StorageSettingsFragment.onViewCreated', 'StorageSettingsFragment.onSaveInstanceState', 'LIFECYCLE', 'Save dir-chooser binding preference during state save', evidence='SRC ui/settings/sections/StorageSettingsFragment.java:73-79; SRC ui/settings/sections/StorageSettingsFragment.java:209-214')
# Streaming: class initialisation on first use via newInstance (TAG field).
e('StreamingSettingsFragment.newInstance', 'StreamingSettingsFragment.<clinit>', 'FRAMEWORK', 'Initialize TAG before first streaming settings use', evidence='SRC ui/settings/sections/StreamingSettingsFragment.java:39; SRC ui/settings/sections/StreamingSettingsFragment.java:43-48')
# Streaming: port edit-text bind lambda applies the port filter.
e('StreamingSettingsFragment.onCreate', 'StreamingSettingsFragment.lambda$onCreate$0', 'CALL', 'Port edit-text bind lambda applies the port filter', cls='non_standard', via='EditTextPreference onBindEditText dispatch', evidence='INFERRED bind dispatch; SRC ui/settings/sections/StreamingSettingsFragment.java:80; SRC ui/settings/sections/StreamingSettingsFragment.java:52-86')
# Tags list builds its add-tag button with the 1-arg constructor.
e('TorrentTagsList.buildAddTagButton', 'AddTagButton.<init>(Context)', 'CALL', 'Tags list builds its add-tag button', evidence='SRC ui/tag/TorrentTagsList.java:79; SRC ui/tag/AddTagButton.java:37-41')
# 1-arg constructor initialises the button text, icon and colours.
e('AddTagButton.<init>(Context)', 'AddTagButton.init', 'CALL', 'Button constructor initialises text, icon and colours', evidence='SRC ui/tag/AddTagButton.java:40; SRC ui/tag/AddTagButton.java:59-78')
# System Back while the chooser activity is active reaches its handler.
e('SelectTagActivity.onCreate', 'SelectTagActivity.onBackPressed', 'CALL', 'Back press while the tag chooser activity is active forwards to its handler', cls='non_standard', via='system Back dispatch', evidence='INFERRED Back dispatch; SRC ui/tag/SelectTagActivity.java:69-70')
# SelectTagDialog: class initialisation on first use via newInstance (TAG field).
e('SelectTagDialog.newInstance', 'SelectTagDialog.<clinit>', 'FRAMEWORK', 'Initialize TAG before first tag dialog use', evidence='SRC ui/tag/SelectTagDialog.java:52; SRC ui/tag/SelectTagDialog.java:63-71')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No REACHABLE method in this batch calls a proposed-UNREACHABLE method in
# bytecode (recomputed from auto_calls.json + javap; see REPORT.md), so no
# SUPPRESS entries apply. The stale base-level candidate
# AddTagButton.<init>(Context) is overload-cleared: only the 2-arg and 3-arg
# ctors are UNREACHABLE (batch 11 rows 5-6); the 1-arg ctor is REACHABLE here.
SUPPRESS.update(set())
