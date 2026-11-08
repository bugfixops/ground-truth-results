# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 116 part (appearance, behavior, feed and limitations sections). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b116_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Rows covered by an existing graph_def edge are listed in the .md
# Dependencies line instead of receiving a duplicate edge here.

e('BehaviorSettingsFragment.newInstance', 'BehaviorSettingsFragment.<clinit>', 'FRAMEWORK', 'First use of the fragment class initialises its static TAG field', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation on first use; SRC ui/settings/sections/BehaviorSettingsFragment.java:53-59; SRC ui/settings/sections/BehaviorSettingsFragment.java:45')
e('FeedSettingsFragment.newInstance', 'FeedSettingsFragment.<clinit>', 'FRAMEWORK', 'First use of the fragment class initialises its static TAG field', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation on first use; SRC ui/settings/sections/FeedSettingsFragment.java:42-48; SRC ui/settings/sections/FeedSettingsFragment.java:38')
e('LimitationsSettingsFragment.newInstance', 'LimitationsSettingsFragment.<clinit>', 'FRAMEWORK', 'First use of the fragment class initialises its static TAG field', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation on first use; SRC ui/settings/sections/LimitationsSettingsFragment.java:44-49; SRC ui/settings/sections/LimitationsSettingsFragment.java:40')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# SUPPRESS: initLegacyNotifySettings: auto calls edge from AppearanceSettingsFragment.onCreate (this batch, row 3, AppearanceSettingsFragment.java:119) into the UNREACHABLE b115/38 method, gated off at API 27; also listed in b115 so the suppress exists whichever part merges first.
SUPPRESS.update({
    'AppearanceSettingsFragment.initLegacyNotifySettings',
})
