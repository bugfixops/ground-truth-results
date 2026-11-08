# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 114 part (tag holders, PreferenceActivity and SettingsFragment). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b114_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Rows covered by an existing graph_def edge are listed in the .md
# Dependencies line instead of receiving a duplicate edge here.

e('drawer.TagsAdapter.onBindViewHolder', 'drawer.TagsAdapter$ItemViewHolder.bind(AbstractTagItem,OnClickListener)', 'CALL', 'Bind a tag row through the abstract holder overload', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:99; SRC ui/main/drawer/TagsAdapter.java:177-184')
e('drawer.TagsAdapter.onBindViewHolder', 'drawer.TagsAdapter$NoTagsItemViewHolder.bind(AbstractTagItem,OnClickListener)', 'CALL', 'Bind a no-tags row through the abstract holder overload', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:99; SRC ui/main/drawer/TagsAdapter.java:282-289')
e('SettingsFragment.startActivity', 'PreferenceActivity.<clinit>', 'FRAMEWORK', 'First use of PreferenceActivity initialises its static fields', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation on first use; SRC ui/settings/SettingsFragment.java:234; SRC ui/settings/PreferenceActivity.java:45,47')
e('PreferenceActivity.onCreate', 'PreferenceActivity.onOptionsItemSelected', 'FRAMEWORK', 'Framework delivers the options-menu selection to the activity', cls='non_standard', via='Android framework menu dispatch', evidence='INFERRED Android framework menu dispatch; SRC ui/settings/PreferenceActivity.java:125-131')
e('SettingsFragment.startActivity', 'PreferenceActivityConfig.<clinit>', 'FRAMEWORK', 'First use of PreferenceActivityConfig initialises its static CREATOR field', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation on first use; SRC ui/settings/SettingsFragment.java:235; SRC ui/settings/PreferenceActivityConfig.java:79-93')
e('PreferenceActivityConfig$1.createFromParcel', 'PreferenceActivityConfig.<init>(Parcel)', 'CALL', 'Rebuild the config from its parcelled strings', cls='explicit', evidence='SRC ui/settings/PreferenceActivityConfig.java:85; SRC ui/settings/PreferenceActivity.java:69; SRC ui/settings/PreferenceActivityConfig.java:40-44')
e('SettingsFragment.startActivity', 'PreferenceActivityConfig.<init>(String,String)', 'CALL', 'Build the section config for the PreferenceActivity intent', cls='explicit', evidence='SRC ui/settings/SettingsFragment.java:235-237; SRC ui/settings/PreferenceActivityConfig.java:34-38')
e('SettingsFragment.startActivity', 'PreferenceActivityConfig.describeContents', 'FRAMEWORK', 'Framework marshals the config parcel and reads its contents descriptor', cls='non_standard', via='Android framework Parcel marshalling dispatch', evidence='INFERRED Android framework Parcel marshalling dispatch; SRC ui/settings/SettingsFragment.java:239-240; SRC ui/settings/PreferenceActivityConfig.java:67-70')
e('PreferenceActivity.onCreate', 'PreferenceActivityConfig.getFragment', 'CALL', 'Read the section fragment name back from the config', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:70; SRC ui/settings/PreferenceActivityConfig.java:51-54')
e('PreferenceActivity.onCreate', 'PreferenceActivityConfig.getTitle', 'CALL', 'Read the section title back from the config', cls='explicit', evidence='SRC ui/settings/PreferenceActivity.java:71; SRC ui/settings/PreferenceActivityConfig.java:61-64')
e('SettingsFragment.startActivity', 'PreferenceActivityConfig.writeToParcel', 'FRAMEWORK', 'Framework writes the config parcel on putExtra/startActivity', cls='non_standard', via='Android framework Parcel marshalling dispatch', evidence='INFERRED Android framework Parcel marshalling dispatch; SRC ui/settings/SettingsFragment.java:239-240; SRC ui/settings/PreferenceActivityConfig.java:73-77')
e('PreferenceActivityConfig.<clinit>', 'PreferenceActivityConfig$1.<init>', 'CALL', 'Create the anonymous Parcelable Creator for the static CREATOR field', cls='explicit', evidence='SRC ui/settings/PreferenceActivityConfig.java:79-93')
e('PreferenceActivity.onCreate', 'PreferenceActivityConfig$1.createFromParcel', 'FRAMEWORK', 'Framework unmarshals the config parcel through its Creator', cls='non_standard', via='Android framework Parcel unmarshalling dispatch', evidence='INFERRED Android framework Parcel unmarshalling dispatch; SRC ui/settings/PreferenceActivity.java:69; SRC ui/settings/PreferenceActivityConfig.java:83-86')
e('SettingsActivity.onCreate', 'SettingsFragment.<clinit>', 'FRAMEWORK', 'First use of the settings host fragment initialises its static fields', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation on first use; SRC ui/settings/SettingsActivity.java:49; SRC ui/settings/SettingsFragment.java:49,51-58')

UNREACHABLE.update({
    'PreferenceActivityConfig.setFragment': ('no_trigger_in_app',
        'A1 evidence: saved full-tree grep finds no config.setFragment call site; configs are built only via the 2-arg ctor (SettingsFragment.java:235-237) and read only via getters (PreferenceActivity.java:70-71); auto_calls.json exact dst 0 edges. Definition PreferenceActivityConfig.java:46-49.',
        'SRC ui/settings/PreferenceActivityConfig.java:46-49',
        'INFERRED'),
    'PreferenceActivityConfig.setTitle': ('no_trigger_in_app',
        'A1 evidence: saved full-tree grep finds no config.setTitle call site; every other setTitle hit is a different receiver (toolbar.setTitle at PreferenceActivity.java:76 is not this method); receiver reads only getTitle() (PreferenceActivity.java:71); auto_calls.json exact dst 0 edges. Definition PreferenceActivityConfig.java:56-59.',
        'SRC ui/settings/PreferenceActivityConfig.java:56-59',
        'INFERRED'),
    'PreferenceActivityConfig$1.newArray': ('no_trigger_in_app',
        'Framework calls newArray only when unmarshalling a Parcelable array; the only printed parcel sites are the single extra (SettingsFragment.java:239 / PreferenceActivity.java:69); no getParcelableArrayExtra site in any printed file. Definition PreferenceActivityConfig.java:89-92.',
        'SRC ui/settings/PreferenceActivityConfig.java:89-92',
        'INFERRED'),
})

# No REACHABLE method in this batch calls an UNREACHABLE method
# in bytecode (recomputed from auto_calls.json + javap; see REPORT.md),
# so no SUPPRESS entries apply.
SUPPRESS.update(set())
