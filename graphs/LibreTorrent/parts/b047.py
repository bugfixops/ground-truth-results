# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# LibreTorrent part b047 — converter C07 delivery.
# Base: audited A3 output helper/a3-g9/parts/b047.py (content below verbatim apart
# from this header; labels/kinds verified against the authoritative batch file:
# clone/graphs/LibreTorrent/scratch/merge-ready/batch47-merge-ready.md).
# Stronger-evidence rule (b): checked the merger tree's graph_def.py (read-only) for
# every UNREACHABLE key in this part. The tree holds NO UNREACHABLE grade for any key
# in this part, so NO grade changes were made and no SOURCE was downgraded to INFERRED;
# every UNREACHABLE grade below stands exactly as audited.
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/47/ (see REPORT-b047.md).
# Branch head at pre-test: f8676c8a (LibreTorrent b007 landed; merger-tree MERGED_PARTS
# tail b007.py matched the head's last part, so the pre-test base was not moving).
# This part does NOT claim F1. Merger adds nothing from this header; the merger owns
# MERGED_PARTS and the push.
# Batch 47 part (SettingsRepositoryImpl watch-dir + Default fallbacks + BaseSorting/TorrentSorting). Hand-written edges only, plus Dependencies for rows already covered by graph_def edges.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b047_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
# Routes into the Dependencies rows already exist in graph_def.py and are not
# repeated here; they are named in the .md Dependencies line.

e('TorrentEngine.handleOnSessionStarted', 'SettingsRepositoryImpl.watchDir()', 'CALL', 'Session-started handler reads the watch-dir flag', cls='explicit', evidence='SRC TorrentEngine.java:1053; SRC SettingsRepositoryImpl.java:773')
e('TorrentEngine.makeTorrentFileObserver', 'SettingsRepositoryImpl.watchDirDeleteFile()', 'CALL', 'Watch-dir file observer deletes a watched file when the flag is set', cls='explicit', evidence='SRC TorrentEngine.java:1152; SRC SettingsRepositoryImpl.java:799')
e('SettingsRepositoryImpl.dirToWatch()', 'SettingsRepositoryImpl$Default.<clinit>', 'CALL', 'First Default access runs the nested-class initialiser', cls='non_standard', via='JVM class initialisation on first Default access (fallback call in dirToWatch)', evidence='SRC SettingsRepositoryImpl.java:786-788')
e('SettingsRepositoryImpl.dirToWatch()', 'SettingsRepositoryImpl$Default.dirToWatch', 'CALL', 'Watched-dir getter falls back to the default path', cls='explicit', evidence='SRC SettingsRepositoryImpl.java:786-788')
e('SettingsRepositoryImpl.encryptInConnectionsMode()', 'SettingsRepositoryImpl$Default.encryptInConnectionsMode', 'CALL', 'Incoming-encryption getter falls back to the default mode', cls='explicit', evidence='SRC SettingsRepositoryImpl.java:643-645')
e('SettingsRepositoryImpl.encryptOutConnectionsMode()', 'SettingsRepositoryImpl$Default.encryptOutConnectionsMode', 'CALL', 'Outgoing-encryption getter falls back to the default mode', cls='explicit', evidence='SRC SettingsRepositoryImpl.java:656-658')
e('SettingsRepositoryImpl.foregroundNotifySorting()', 'SettingsRepositoryImpl$Default.foregroundNotifySorting', 'CALL', 'Foreground-sorting getter falls back to the default value', cls='explicit', evidence='SRC SettingsRepositoryImpl.java:373-376')
e('SettingsRepositoryImpl.foregroundNotifyStatusFilter()', 'SettingsRepositoryImpl$Default.foregroundNotifyStatusFilter', 'CALL', 'Foreground-filter getter falls back to the default value', cls='explicit', evidence='SRC SettingsRepositoryImpl.java:355-358')
e('SettingsRepositoryImpl.moveAfterDownloadIn()', 'SettingsRepositoryImpl$Default.moveAfterDownloadIn', 'CALL', 'Move-destination getter falls back to the default path', cls='explicit', evidence='SRC SettingsRepositoryImpl.java:734-736')
e('SettingsRepositoryImpl.saveTorrentFilesIn()', 'SettingsRepositoryImpl$Default.saveTorrentFilesIn', 'CALL', 'Torrent-file destination getter falls back to the default path', cls='explicit', evidence='SRC SettingsRepositoryImpl.java:760-762')
e('SettingsRepositoryImpl.saveTorrentsIn()', 'SettingsRepositoryImpl$Default.saveTorrentsIn', 'CALL', 'Torrent save-dir getter falls back to the default path', cls='explicit', evidence='SRC SettingsRepositoryImpl.java:708-710')
e('SettingsRepositoryImpl.theme()', 'SettingsRepositoryImpl$Default.theme', 'CALL', 'Theme getter falls back to the default theme', cls='explicit', evidence='SRC SettingsRepositoryImpl.java:329-331')
e('TorrentSorting.<init>', 'BaseSorting.<init>', 'CALL', 'Sorting constructor chains to the base sorting constructor', cls='explicit', evidence='SRC TorrentSorting.java:113-116; SRC BaseSorting.java:52-56')
e('TorrentSortingComparator.compare', 'BaseSorting.getColumnName', 'CALL', 'Comparator reads the sorting column name', cls='explicit', evidence='SRC TorrentSortingComparator.java:43; SRC BaseSorting.java:63-66')
e('TorrentSortingComparator.compare', 'BaseSorting.getDirection', 'CALL', 'Comparator reads the sorting direction', cls='explicit', evidence='SRC TorrentSortingComparator.java:44; SRC BaseSorting.java:58-61')
e('MainViewModel.<init>', 'BaseSorting$Direction.<clinit>', 'CALL', 'Default comparator construction first uses a Direction constant', cls='non_standard', via='JVM enum initialisation on first Direction use', evidence='SRC ui/main/MainViewModel.java:51-52')
e('Utils.getForegroundNotifySorting', 'TorrentSorting.<init>', 'CALL', 'Foreground-notify sorting builds a default sorting', cls='explicit', evidence='SRC Utils.java:892-922')
e('MainViewModel.<init>', 'TorrentSorting$SortingColumns.<clinit>', 'CALL', 'Default comparator construction first uses a SortingColumns constant', cls='non_standard', via='JVM enum initialisation on first SortingColumns use', evidence='SRC ui/main/MainViewModel.java:51-52')
e('TorrentSortingComparator.compare', 'TorrentSorting$SortingColumns.fromValue', 'CALL', 'Comparator resolves the column name to a SortingColumns value', cls='explicit', evidence='SRC TorrentSortingComparator.java:43')
e('TorrentSorting$SortingColumns.<clinit>', 'TorrentSorting$SortingColumns$1.<init>', 'CALL', 'Enum initialisation creates the none anonymous subclass instance', cls='non_standard', via='JVM enum initialisation creates the anonymous subclass instance', evidence='SRC TorrentSorting.java:28-35')
e('TorrentSortingComparator.compare', 'TorrentSorting$SortingColumns$1.compare', 'CALL', 'Comparator dispatch reaches the none branch', cls='non_standard', via='virtual dispatch through SortingColumns.compare to the none anonymous subclass', evidence='SRC TorrentSortingComparator.java:43-44; SRC TorrentSorting.java:28-35')
e('TorrentSorting$SortingColumns.<clinit>', 'TorrentSorting$SortingColumns$2.<init>', 'CALL', 'Enum initialisation creates the name anonymous subclass instance', cls='non_standard', via='JVM enum initialisation creates the anonymous subclass instance', evidence='SRC TorrentSorting.java:36-46')
e('TorrentSortingComparator.compare', 'TorrentSorting$SortingColumns$2.compare', 'CALL', 'Comparator dispatch reaches the name branch', cls='non_standard', via='virtual dispatch through SortingColumns.compare to the name anonymous subclass', evidence='SRC TorrentSortingComparator.java:43-44; SRC TorrentSorting.java:36-46')
e('TorrentSorting$SortingColumns.<clinit>', 'TorrentSorting$SortingColumns$3.<init>', 'CALL', 'Enum initialisation creates the size anonymous subclass instance', cls='non_standard', via='JVM enum initialisation creates the anonymous subclass instance', evidence='SRC TorrentSorting.java:47-57')
e('TorrentSortingComparator.compare', 'TorrentSorting$SortingColumns$3.compare', 'CALL', 'Comparator dispatch reaches the size branch', cls='non_standard', via='virtual dispatch through SortingColumns.compare to the size anonymous subclass', evidence='SRC TorrentSortingComparator.java:43-44; SRC TorrentSorting.java:47-57')
e('TorrentSorting$SortingColumns.<clinit>', 'TorrentSorting$SortingColumns$4.<init>', 'CALL', 'Enum initialisation creates the progress anonymous subclass instance', cls='non_standard', via='JVM enum initialisation creates the anonymous subclass instance', evidence='SRC TorrentSorting.java:58-68')
e('TorrentSortingComparator.compare', 'TorrentSorting$SortingColumns$4.compare', 'CALL', 'Comparator dispatch reaches the progress branch', cls='non_standard', via='virtual dispatch through SortingColumns.compare to the progress anonymous subclass', evidence='SRC TorrentSortingComparator.java:43-44; SRC TorrentSorting.java:58-68')
e('TorrentSorting$SortingColumns.<clinit>', 'TorrentSorting$SortingColumns$5.<init>', 'CALL', 'Enum initialisation creates the ETA anonymous subclass instance', cls='non_standard', via='JVM enum initialisation creates the anonymous subclass instance', evidence='SRC TorrentSorting.java:69-79')
e('TorrentSortingComparator.compare', 'TorrentSorting$SortingColumns$5.compare', 'CALL', 'Comparator dispatch reaches the ETA branch', cls='non_standard', via='virtual dispatch through SortingColumns.compare to the ETA anonymous subclass', evidence='SRC TorrentSortingComparator.java:43-44; SRC TorrentSorting.java:69-79')
e('TorrentSorting$SortingColumns.<clinit>', 'TorrentSorting$SortingColumns$6.<init>', 'CALL', 'Enum initialisation creates the peers anonymous subclass instance', cls='non_standard', via='JVM enum initialisation creates the anonymous subclass instance', evidence='SRC TorrentSorting.java:80-90')
e('TorrentSortingComparator.compare', 'TorrentSorting$SortingColumns$6.compare', 'CALL', 'Comparator dispatch reaches the peers branch', cls='non_standard', via='virtual dispatch through SortingColumns.compare to the peers anonymous subclass', evidence='SRC TorrentSortingComparator.java:43-44; SRC TorrentSorting.java:80-90')
e('TorrentSorting$SortingColumns.<clinit>', 'TorrentSorting$SortingColumns$7.<init>', 'CALL', 'Enum initialisation creates the dateAdded anonymous subclass instance', cls='non_standard', via='JVM enum initialisation creates the anonymous subclass instance', evidence='SRC TorrentSorting.java:91-101')
e('TorrentSortingComparator.compare', 'TorrentSorting$SortingColumns$7.compare', 'CALL', 'Comparator dispatch reaches the dateAdded branch', cls='non_standard', via='virtual dispatch through SortingColumns.compare to the dateAdded anonymous subclass', evidence='SRC TorrentSortingComparator.java:43-44; SRC TorrentSorting.java:91-101')
e('Utils.getForegroundNotifySorting', 'TorrentSortingComparator.<init>', 'CALL', 'Foreground-notify sorting builds a comparator', cls='explicit', evidence='SRC Utils.java:892-922')

UNREACHABLE.update({
    'SettingsRepositoryImpl.vibrationNotify()': ('closed_by_api_level',
        'Only call statements are gated: AppearanceSettingsFragment.java:187 inside initLegacyNotifySettings (SDK < O gate :118-119, false at API 27) and TorrentNotifier.java:286 inside applyLegacyNotifySettings (early return :276 at SDK >= O, before :286). At API 27 neither statement executes.',
        'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:187; SRC ui/TorrentNotifier.java:276; SRC ui/TorrentNotifier.java:286; SRC SettingsRepositoryImpl.java:316-318',
        'INFERRED'),
    'SettingsRepositoryImpl.vibrationNotify(boolean)': ('closed_by_api_level',
        'Only call statement is AppearanceSettingsFragment.java:247 (onPreferenceChange branch) whose listener is bound only inside initLegacyNotifySettings (:188), gated at SDK < O (:118-119). At API 27 the branch never fires.',
        'SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:188; SRC ui/settings/sections/AppearanceSettingsFragment.java:247; SRC SettingsRepositoryImpl.java:322-328',
        'INFERRED'),
    'SettingsRepositoryImpl$Default.ledIndicatorColorNotify': ('closed_by_api_level',
        'Sole call statement is the fallback argument inside getter ledIndicatorColorNotify() at :342-344 (Default.ledIndicatorColorNotify(appContext)); that getter is itself closed_by_api_level (batch 44 row 17: AppearanceSettingsFragment.java:180 gated :118-119, TorrentNotifier.java:290 after early return :276), so the fallback argument is never evaluated at API 27. Flips together with batch 44 row 17.',
        'SRC SettingsRepositoryImpl.java:342-344; SRC ui/settings/sections/AppearanceSettingsFragment.java:118-119; SRC ui/settings/sections/AppearanceSettingsFragment.java:180; SRC ui/TorrentNotifier.java:276; SRC ui/TorrentNotifier.java:290',
        'INFERRED'),
    'BaseSorting.toString': ('no_trigger_in_app',
        'No explicit .toString() on a BaseSorting/TorrentSorting object, no Log/concat/String.valueOf site for a sorting object in the app tree (saved full-tree grep, batch file); only getColumnName()/getDirection() are ever read on sorting objects (TorrentSortingComparator.java:43-44). Whole-tree bytecode scan for this task confirms zero invokers of BaseSorting.toString.',
        'SRC TorrentSortingComparator.java:43-44; SRC BaseSorting.java:70-76',
        'INFERRED'),
})

# Suppress bytecode auto edges into the UNREACHABLE methods below.
# Each entry is a method a REACHABLE method calls in bytecode
# (auto_calls.json + class-file invoke scan); the call sites are
# gated at API 27, so the auto edge must not revive the method.
# SettingsRepositoryImpl.vibrationNotify(): bytecode caller TorrentNotifier.applyLegacyNotifySettings (REACHABLE, batch 74); gated at API 27, see UNREACHABLE evidence
# SettingsRepositoryImpl.vibrationNotify(boolean): bytecode caller AppearanceSettingsFragment.onPreferenceChange (REACHABLE) :247
SUPPRESS.update({
    'SettingsRepositoryImpl.vibrationNotify()',
    'SettingsRepositoryImpl.vibrationNotify(boolean)',
})
