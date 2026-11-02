# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 107 part (LogSettings activity/fragment, LogSourceFactory, LogViewModel and SessionLogFilterDialog). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b107_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

e('LogActivity.showLogSettings', 'LogSettingsActivity.<clinit>', 'FRAMEWORK', 'First settings-activity use initialises the class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC ui/log/LogActivity.java:261; SRC ui/log/LogSettingsActivity.java:32')
e('LogActivity.showLogSettings', 'LogSettingsActivity.<init>', 'FRAMEWORK', 'Framework instantiates the settings activity after the intent', cls='non_standard', via='Framework activity instantiation', evidence='INFERRED framework instantiation; SRC ui/log/LogActivity.java:261')
e('LogSettingsActivity.onCreate', 'LogSettingsActivity.lambda$onCreate$0', 'FRAMEWORK', 'Toolbar navigation click finishes the settings activity', cls='non_standard', via='View click dispatch', evidence='INFERRED View click dispatch; SRC ui/log/LogSettingsActivity.java:47')
e('LogActivity.showLogSettings', 'LogSettingsActivity.onCreate', 'FRAMEWORK', 'Framework creates the settings activity after the intent', cls='non_standard', via='Framework activity lifecycle dispatch', evidence='INFERRED framework lifecycle dispatch; SRC ui/log/LogActivity.java:261; SRC ui/log/LogSettingsActivity.java:37-50')
e('LogSettingsActivity.onCreate', 'LogSettingsFragment.<clinit>', 'FRAMEWORK', 'FragmentContainerView inflation initialises the settings fragment class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC ui/log/LogSettingsActivity.java:42; SRC ui/log/LogSettingsFragment.java:39')
e('LogSettingsActivity.onCreate', 'LogSettingsFragment.<init>', 'FRAMEWORK', 'FragmentContainerView instantiates the settings fragment', cls='non_standard', via='Framework fragment instantiation', evidence='INFERRED framework fragment instantiation; SRC ui/log/LogSettingsActivity.java:42')
e('LogSettingsFragment.onCreate', 'LogSettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'onCreate binds the max-log-size preference listener', evidence='SRC ui/log/LogSettingsFragment.java:73; SRC ui/log/LogSettingsFragment.java:83-86')
e('LogSettingsFragment.onCreate', 'LogSettingsFragment.lambda$onCreate$0', 'FRAMEWORK', 'EditText-bind dispatch applies the max-log-size filter', cls='non_standard', via='EditText-bind dispatch', evidence='INFERRED EditText-bind dispatch; SRC ui/log/LogSettingsFragment.java:70')
e('LogSettingsActivity.onCreate', 'LogSettingsFragment.onCreate', 'FRAMEWORK', 'Fragment lifecycle dispatch creates the settings fragment', cls='non_standard', via='Framework fragment lifecycle dispatch', evidence='INFERRED framework fragment lifecycle dispatch; SRC ui/log/LogSettingsActivity.java:42; SRC ui/log/LogSettingsFragment.java:52-74')
e('LogSettingsFragment.onCreate', 'LogSettingsFragment.onCreatePreferences', 'FRAMEWORK', 'PreferenceFragmentCompat dispatch loads the log preferences', cls='non_standard', via='PreferenceFragmentCompat dispatch', evidence='INFERRED PreferenceFragmentCompat dispatch; SRC ui/log/LogSettingsFragment.java:52-74; SRC ui/log/LogSettingsFragment.java:78-81')
e('LogSettingsFragment.bindOnPreferenceChangeListener', 'LogSettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Preference-change dispatch persists the max log size', cls='non_standard', via='Preference-change dispatch', evidence='INFERRED preference-change dispatch; SRC ui/log/LogSettingsFragment.java:83-86; SRC ui/log/LogSettingsFragment.java:89-101')
e('LogViewModel.<init>', 'LogSourceFactory.<init>', 'CALL', 'ViewModel constructor builds the log source factory', evidence='SRC ui/log/LogViewModel.java:75; SRC ui/log/LogSourceFactory.java:32-35')
e('LogViewModel.observeLog', 'LogSourceFactory.create', 'FRAMEWORK', 'Paging dispatch creates the log data source for the builder', cls='non_standard', via='Paging dispatch', evidence='INFERRED Paging dispatch; SRC ui/log/LogViewModel.java:92-96; SRC ui/log/LogSourceFactory.java:39-42')
e('LogActivity.onCreate', 'LogViewModel.<init>', 'CALL', 'ViewModelProvider dispatch constructs the log ViewModel', cls='non_standard', via='ViewModelProvider dispatch', evidence='INFERRED ViewModelProvider dispatch; SRC ui/log/LogActivity.java:92; SRC ui/log/LogViewModel.java:65-78')
e('LogActivity.onItemClicked', 'LogViewModel.copyLogEntryToClipboard', 'CALL', 'Item click copies the log entry to the clipboard', evidence='SRC ui/log/LogActivity.java:463; SRC ui/log/LogViewModel.java:215-226')
e('LogActivity.updateToolbarSubtitle', 'LogViewModel.getLogEntriesCount', 'CALL', 'Toolbar subtitle reads the log entry count', evidence='SRC ui/log/LogActivity.java:445; SRC ui/log/LogViewModel.java:162-165')
e('LogActivity.saveLogPathChooseDialog', 'LogViewModel.getSaveLogFileName', 'CALL', 'Save dialog names the log file from the ViewModel', evidence='SRC ui/log/LogActivity.java:311; SRC ui/log/LogViewModel.java:191-197')
e('LogViewModel.<init>', 'LogViewModel.initMutableParams', 'CALL', 'ViewModel constructor restores the mutable log params', evidence='SRC ui/log/LogViewModel.java:77; SRC ui/log/LogViewModel.java:80-90')
e('LogActivity.pauseResumeLog', 'LogViewModel.logPausedManually', 'CALL', 'Pause-resume logic reads the manual-pause flag', evidence='SRC ui/log/LogActivity.java:266; SRC ui/log/LogViewModel.java:167-170')
e('LogActivity.toggleRecord', 'LogViewModel.logRecording', 'CALL', 'Toggle-record logic reads the recording flag', evidence='SRC ui/log/LogActivity.java:283; SRC ui/log/LogViewModel.java:186-189')
e('LogActivity.onCreate', 'LogViewModel.observeLog', 'CALL', 'onCreate observes the log LiveData', evidence='SRC ui/log/LogActivity.java:119; SRC ui/log/LogViewModel.java:92-96')
e('LogActivity.onDestroy', 'LogViewModel.onCleared', 'FRAMEWORK', 'ViewModelStore dispatch clears the log ViewModel', cls='non_standard', via='ViewModel lifecycle dispatch', evidence='INFERRED ViewModel lifecycle dispatch; SRC ui/log/LogActivity.java:150-156; SRC ui/log/LogViewModel.java:100-105')
e('LogActivity.toggleRecord', 'LogViewModel.pauseLog', 'CALL', 'Toggle-record stop path pauses the log', evidence='SRC ui/log/LogActivity.java:299; SRC ui/log/LogViewModel.java:140-143')
e('LogActivity.pauseResumeLog', 'LogViewModel.pauseLogManually', 'CALL', 'Pause branch pauses the log manually', evidence='SRC ui/log/LogActivity.java:268; SRC ui/log/LogViewModel.java:145-149')
e('LogActivity.resumeLog', 'LogViewModel.resumeLog', 'CALL', 'Activity resume wrapper resumes the ViewModel log', evidence='SRC ui/log/LogActivity.java:278; SRC ui/log/LogViewModel.java:151-154')
e('LogActivity.pauseResumeLog', 'LogViewModel.resumeLogManually', 'CALL', 'Resume branch resumes the log manually', evidence='SRC ui/log/LogActivity.java:270; SRC ui/log/LogViewModel.java:156-160')
e('LogActivity.lambda$new$4', 'LogViewModel.saveLog', 'CALL', 'Save-log callback enqueues the log save worker', evidence='SRC ui/log/LogActivity.java:327; SRC ui/log/LogViewModel.java:199-213')
e('LogActivity.toggleRecord', 'LogViewModel.startLogRecording', 'CALL', 'Toggle-record start branch starts recording', evidence='SRC ui/log/LogActivity.java:294; SRC ui/log/LogViewModel.java:172-177')
e('LogActivity.lambda$new$4', 'LogViewModel.stopLogRecording', 'CALL', 'Save-log non-OK branch stops recording', evidence='SRC ui/log/LogActivity.java:330; SRC ui/log/LogViewModel.java:179-184')
e('LogViewModel.<init>', 'LogViewModel$1.<init>', 'CALL', 'Field initialiser constructs the params callback', evidence='SRC ui/log/LogViewModel.java:107-110')
e('LogViewModel.initMutableParams', 'LogViewModel$1.onPropertyChanged', 'FRAMEWORK', 'Observable dispatch persists changed log params', cls='non_standard', via='Observable dispatch', evidence='INFERRED Observable dispatch; SRC ui/log/LogViewModel.java:89; SRC ui/log/LogViewModel.java:110-137')
e('LogActivity.showFilterDialog', 'SessionLogFilterDialog.<clinit>', 'FRAMEWORK', 'First filter-dialog use initialises the class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC ui/log/LogActivity.java:254-255; SRC ui/log/SessionLogFilterDialog.java:42')
e('SessionLogFilterDialog.newInstance', 'SessionLogFilterDialog.<init>', 'CALL', 'newInstance constructs the filter dialog fragment', evidence='SRC ui/log/SessionLogFilterDialog.java:51; SRC ui/log/SessionLogFilterDialog.java:49-57')
e('SessionLogFilterDialog.onCreateDialog', 'SessionLogFilterDialog.initLayoutView', 'CALL', 'onCreateDialog lays out the filter dialog', evidence='SRC ui/log/SessionLogFilterDialog.java:101; SRC ui/log/SessionLogFilterDialog.java:106-114')
e('SessionLogFilterDialog.initLayoutView', 'SessionLogFilterDialog.lambda$initLayoutView$1', 'FRAMEWORK', 'Negative-button click runs the back-press lambda', cls='non_standard', via='Dialog-button dispatch', evidence='INFERRED dialog-button dispatch; SRC ui/log/SessionLogFilterDialog.java:110')
e('SessionLogFilterDialog.onResume', 'SessionLogFilterDialog.lambda$onResume$0', 'FRAMEWORK', 'Back-key press runs the key lambda', cls='non_standard', via='Key dispatch', evidence='INFERRED key dispatch; SRC ui/log/SessionLogFilterDialog.java:74; SRC ui/log/SessionLogFilterDialog.java:74-85')
e('LogActivity.showFilterDialog', 'SessionLogFilterDialog.newInstance', 'CALL', 'Filter menu action creates the filter dialog instance', evidence='SRC ui/log/LogActivity.java:254; SRC ui/log/SessionLogFilterDialog.java:49-57')
e('LogActivity.showFilterDialog', 'SessionLogFilterDialog.onAttach', 'FRAMEWORK', 'DialogFragment dispatch attaches the shown filter dialog', cls='non_standard', via='DialogFragment lifecycle dispatch', evidence='INFERRED DialogFragment dispatch; SRC ui/log/LogActivity.java:255; SRC ui/log/SessionLogFilterDialog.java:60-66')
e('SessionLogFilterDialog.lambda$initLayoutView$1', 'SessionLogFilterDialog.onBackPressed', 'CALL', 'Negative-button lambda presses back on the filter dialog', evidence='SRC ui/log/SessionLogFilterDialog.java:110; SRC ui/log/SessionLogFilterDialog.java:116-119')
e('LogActivity.showFilterDialog', 'SessionLogFilterDialog.onCreateDialog', 'FRAMEWORK', 'DialogFragment dispatch creates the filter dialog', cls='non_standard', via='DialogFragment lifecycle dispatch', evidence='INFERRED DialogFragment dispatch; SRC ui/log/LogActivity.java:255; SRC ui/log/SessionLogFilterDialog.java:90-104')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No part edge points at a method that is UNREACHABLE in this batch, and
# auto_calls.json + javap show no bytecode caller of this batch's
# UNREACHABLE methods, so no SUPPRESS entries apply.
SUPPRESS.update(set())
