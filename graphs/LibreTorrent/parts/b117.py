# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 117 part (limitations, network, proxy and scheduling sections). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b117_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Rows covered by an existing graph_def edge are listed in the .md
# Dependencies line instead of receiving a duplicate edge here.

e('NetworkSettingsFragment.newInstance', 'NetworkSettingsFragment.<clinit>', 'FRAMEWORK', 'First use of the fragment class initialises its static TAG field', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation on first use; SRC ui/settings/sections/NetworkSettingsFragment.java:77-82; SRC ui/settings/sections/NetworkSettingsFragment.java:70')
e('ProxySettingsFragment.newInstance', 'ProxySettingsFragment.<clinit>', 'FRAMEWORK', 'First use of the fragment class initialises its static TAG field', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation on first use; SRC ui/settings/sections/ProxySettingsFragment.java:56-61; SRC ui/settings/sections/ProxySettingsFragment.java:49')
e('ProxySettingsFragment.onCreate', 'ProxySettingsFragment.bindOnPreferenceChangeListener', 'CALL', 'Register the fragment as the preference change listener', cls='explicit', evidence='SRC ui/settings/sections/ProxySettingsFragment.java:109,118,131,139,147,157,167; SRC ui/settings/sections/ProxySettingsFragment.java:177-179')
e('ProxySettingsFragment.onPreferenceChange', 'ProxySettingsFragment.enableOrDisablePreferences', 'CALL', 'Enable or disable the proxy fields for the new proxy type', cls='explicit', evidence='SRC ui/settings/sections/ProxySettingsFragment.java:213; SRC ui/settings/sections/ProxySettingsFragment.java:182-204')
e('ProxySettingsFragment.onCreate', 'ProxySettingsFragment.lambda$onCreate$1', 'FRAMEWORK', 'Dialog binding applies the port filter to the port field', cls='non_standard', via='AndroidX EditTextPreference dialog-binding dispatch', evidence='INFERRED AndroidX EditTextPreference dialog-binding dispatch; SRC ui/settings/sections/ProxySettingsFragment.java:129-131')
e('ProxySettingsFragment.onCreate', 'ProxySettingsFragment.lambda$onCreate$2', 'FRAMEWORK', 'Dialog binding masks the password field', cls='non_standard', via='AndroidX EditTextPreference dialog-binding dispatch', evidence='INFERRED AndroidX EditTextPreference dialog-binding dispatch; SRC ui/settings/sections/ProxySettingsFragment.java:165-167')
e('ProxySettingsFragment.onPreferenceChange', 'ProxySettingsFragment.lambda$onPreferenceChange$3', 'FRAMEWORK', 'Dialog binding refreshes the password summary from the new value', cls='non_standard', via='AndroidX EditTextPreference dialog-binding dispatch', evidence='INFERRED AndroidX EditTextPreference dialog-binding dispatch; SRC ui/settings/sections/ProxySettingsFragment.java:232-234')
e('ProxySettingsFragment.onViewCreated', 'ProxySettingsFragment.lambda$onViewCreated$0', 'FRAMEWORK', 'Save button applies the proxy settings', cls='non_standard', via='Android framework View click dispatch', evidence='INFERRED Android framework View click dispatch; SRC ui/settings/sections/ProxySettingsFragment.java:74-78')
e('ProxySettingsFragment.newInstance', 'ProxySettingsFragment.onCreatePreferences', 'FRAMEWORK', 'Framework loads the proxy preference screen', cls='non_standard', via='AndroidX FragmentManager lifecycle dispatch', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/ProxySettingsFragment.java:172-174')
e('ProxySettingsFragment.newInstance', 'ProxySettingsFragment.onDestroy', 'FRAMEWORK', 'Framework destroys the proxy fragment after use', cls='non_standard', via='AndroidX FragmentManager lifecycle dispatch', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/ProxySettingsFragment.java:82-93')
e('ProxySettingsFragment.bindOnPreferenceChangeListener', 'ProxySettingsFragment.onPreferenceChange', 'FRAMEWORK', 'Framework delivers the proxy preference change to the fragment', cls='non_standard', via='AndroidX Preference change dispatch', evidence='INFERRED AndroidX Preference change dispatch; SRC ui/settings/sections/ProxySettingsFragment.java:177-179; SRC ui/settings/sections/ProxySettingsFragment.java:206-245')
e('ProxySettingsFragment.newInstance', 'ProxySettingsFragment.onViewCreated', 'FRAMEWORK', 'Framework creates the proxy fragment view', cls='non_standard', via='AndroidX FragmentManager lifecycle dispatch', evidence='INFERRED AndroidX FragmentManager lifecycle dispatch; SRC ui/settings/sections/ProxySettingsFragment.java:66-79')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No REACHABLE method in this batch calls an UNREACHABLE method
# in bytecode (recomputed from auto_calls.json + javap; see REPORT.md),
# so no SUPPRESS entries apply.
SUPPRESS.update(set())
