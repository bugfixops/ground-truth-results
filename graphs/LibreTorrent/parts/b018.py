# Citation-form rework 2026-11-01: evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, edges, endpoints, SUPPRESS entries and line ranges unchanged; full relative paths remain in the .md and printed files.
# C02 conversion of helper/a3-fix-buildnames batch-18 part (2026-11-01).
# Base part verified against clone batch18-merge-ready.md: labels/kinds
# match exactly; counts R38 U2 O0; edges 24; SUPPRESS 2.
# STRONGER-EVIDENCE upgrades (tree graph_def.py holds SOURCE, part held
# INFERRED; kind/reason/ref unchanged; never downgraded):
#   InputFilterRange.getMax, InputFilterRange.getMin (2 keys: INFERRED -> SOURCE).
# HARNESS NOTE: check_part.py compares the part grade to the merge-ready
# grade (INFERRED for both rows), so the 2 upgrades above produce
# exactly 2 grade-mismatch FAIL lines and no other FAILs. Do NOT revert
# these grades to INFERRED at merge; the merger must either waive those
# 2 FAIL lines or patch the harness to accept SOURCE where the tree
# holds SOURCE.
# Greps: parts-staging/grep/18/ (2 files, one per UNREACHABLE row).
# Printed evidence: parts/b018_printed.txt (verbatim base printed file,
# 631,241 B, under 900 KB; copy pending only on the sandbox exec-write
# block - see REPORT-b018.md).

# Batch 18 part (MainApplication, FeedParser helpers, HttpConnection, InputFilterRange
# and its Builder, RepositoryHelper accessors, TorrentBuilder). Hand-written edges,
# UNREACHABLE entries and SUPPRESS strings only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b018_printed.txt. Source paths are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
#
# Routes into batch-18 methods that already exist in graph_def.py and are not
# repeated here: S_ENTRY -> MainApplication.<clinit> (104), S_ENTRY -> MainApplication.<init>
# (102), MainApplication.onCreate -> MainApplication.increaseCursorWindowSize (112),
# S_ENTRY -> MainApplication.onCreate (100), FeedFetcherWorker.fetchChannel -> FeedParser.<init>
# (2709), FeedParser.getItems -> FeedParser.findDownloadUrl (2781),
# FeedFetcherWorker.fetchChannel -> FeedParser.getItems (2711),
# FeedFetcherWorker.fetchChannel -> FeedParser.getTitle (2713),
# FeedParser.findDownloadUrl -> FeedParser.watchEnclosure (2783),
# FeedParser.findDownloadUrl -> FeedParser.watchGuid (3597),
# FeedParser.findDownloadUrl -> FeedParser.watchMediaContent (3595),
# FeedParser.watchMediaContent -> FeedParser.watchMediaHash (3611),
# FeedParser.findDownloadUrl -> FeedParser.watchTorrentInfoHash (2785),
# AppearanceSettingsFragment.onCreate -> RepositoryHelper.getSettingsRepository (2190),
# BehaviorSettingsFragment.onCreate -> RepositoryHelper.getSettingsRepository (2252),
# NetworkSettingsFragment.onCreate -> RepositoryHelper.getSettingsRepository (2314),
# StorageSettingsFragment.onCreate -> RepositoryHelper.getSettingsRepository (2430),
# LimitationsSettingsFragment.onCreate -> RepositoryHelper.getSettingsRepository (2498).

# Generated-mapper load (decision D8): the first DataBindingUtil use loads the mapper
# class, which loads its inner lookup classes (JVM class initialisation, INFERRED).
e('MainFragment.onCreateView', 'libretorrent.DataBinderMapperImpl$InnerBrLookup.<clinit>', 'FRAMEWORK', 'First DataBindingUtil inflate loads the generated mapper class and its inner lookup classes',
  cls='non_standard', via='JVM class initialization on first DataBindingUtil use',
  evidence='INFERRED generated mapper load (D8); SRC ui/main/MainFragment.java:119')
e('MainFragment.onCreateView', 'libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.<clinit>', 'FRAMEWORK', 'First DataBindingUtil inflate loads the generated mapper class and its inner lookup classes',
  cls='non_standard', via='JVM class initialization on first DataBindingUtil use',
  evidence='INFERRED generated mapper load (D8); SRC ui/main/MainFragment.java:119')

# MainApplication: the lambda is registered in onCreate and runs on an uncaught exception.
e('MainApplication.onCreate', 'MainApplication.lambda$onCreate$0', 'FRAMEWORK', 'Log an uncaught exception through the default handler registered in onCreate',
  cls='non_standard', via='Thread default uncaught-exception handler dispatch',
  evidence='INFERRED handler dispatch; SRC MainApplication.java:61-64')

# FeedParser: the item-link helpers the existing feed route does not reach.
e('FeedParser.getItems', 'FeedParser.getFirstNotNullLink', 'CALL', 'Pick the first non-empty item link as the article URL',
  cls='explicit', evidence='SRC FeedParser.java:97,118-126')
e('FeedParser.getItems', 'FeedParser.watchDownloadableLink', 'CALL', 'Look for a magnet or torrent link among the item links',
  cls='explicit', evidence='SRC FeedParser.java:98,128-139')
e('FeedParser.watchDownloadableLink', 'FeedParser.isMagnetOrTorrent', 'CALL', 'Test each item link for a magnet URI or .torrent suffix',
  cls='explicit', evidence='SRC FeedParser.java:134,263-266')

# HttpConnection: reached from Utils.fetchHttpUrl after the connectivity check.
e('Utils.fetchHttpUrl', 'HttpConnection.<init>', 'CALL', 'Create the HTTP connection once the network check passes',
  cls='explicit', evidence='SRC Utils.java:472; HttpConnection.java:66-70')
e('Utils.fetchHttpUrl', 'HttpConnection.setListener', 'CALL', 'Attach the response listener to the connection',
  cls='explicit', evidence='SRC Utils.java:477; HttpConnection.java:72-75')
e('Utils.fetchHttpUrl', 'HttpConnection.run', 'CALL', 'Run the HTTP request synchronously',
  cls='explicit', evidence='SRC Utils.java:512; HttpConnection.java:78-124')

# InputFilterRange: the port filter is built from the static initialisers and from the
# log-settings Builder chain; the framework invokes filter() on text input.
e('LogSettingsFragment.onCreate', 'InputFilterRange.<clinit>', 'FRAMEWORK', 'First Builder use in the log-settings editor initialises the filter class',
  cls='non_standard', via='JVM class initialization on first active use',
  evidence='INFERRED JVM class initialization; SRC ui/log/LogSettingsFragment.java:59-63; InputFilterRange.java:33-41')
e('InputFilterRange.<clinit>', 'InputFilterRange$Builder.<init>', 'CALL', 'Create the builder for the port range filter',
  cls='explicit', evidence='SRC InputFilterRange.java:33,38')
e('InputFilterRange.<clinit>', 'InputFilterRange$Builder.setMin', 'CALL', 'Set the lower bound of the port range',
  cls='explicit', evidence='SRC InputFilterRange.java:34,39')
e('InputFilterRange.<clinit>', 'InputFilterRange$Builder.setMax', 'CALL', 'Set the upper bound of the port range',
  cls='explicit', evidence='SRC InputFilterRange.java:35,40')
e('InputFilterRange.<clinit>', 'InputFilterRange$Builder.build', 'CALL', 'Build the port range filter',
  cls='explicit', evidence='SRC InputFilterRange.java:36,41')
e('InputFilterRange$Builder.build', 'InputFilterRange.<init>', 'CALL', 'Construct the range filter from the builder bounds',
  cls='explicit', evidence='SRC InputFilterRange.java:107-112')
e('LogSettingsFragment.onCreate', 'InputFilterRange.filter', 'FRAMEWORK', 'Filter each max-log-size edit through the registered range filter',
  guard='user edits the max-log-size field', cls='non_standard', via='framework EditText InputFilter dispatch after setFilters registration',
  evidence='INFERRED framework InputFilter dispatch; SRC ui/log/LogSettingsFragment.java:70; InputFilterRange.java:65-73')
e('InputFilterRange.filter', 'InputFilterRange.inRange', 'CALL', 'Check the parsed number against the range bounds',
  cls='explicit', evidence='SRC InputFilterRange.java:65-73,83-85')

# RepositoryHelper accessors that the existing routes do not reach.
e('FeedFetcherWorker.doWork', 'RepositoryHelper.getFeedRepository', 'CALL', 'Obtain the feed repository for the fetch run',
  cls='explicit', evidence='SRC service/FeedFetcherWorker.java:77; RepositoryHelper.java:52-59')
e('TorrentEngine.<init>', 'RepositoryHelper.getTagRepository', 'CALL', 'Obtain the tag repository for the engine',
  cls='explicit', evidence='SRC TorrentEngine.java:131; RepositoryHelper.java:69-75')
e('TorrentEngine.<init>', 'RepositoryHelper.getTorrentRepository', 'CALL', 'Obtain the torrent repository for the engine',
  cls='explicit', evidence='SRC TorrentEngine.java:128-135; RepositoryHelper.java:43-50')

# TorrentBuilder: constructed and configured in CreateTorrentViewModel.makeBuilder.
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.<init>', 'CALL', 'Construct the torrent builder for the create-torrent flow',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:189; TorrentBuilder.java:88-93')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.addTrackers', 'CALL', 'Add the validated trackers to the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:193; TorrentBuilder.java:116-126')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.addUrlSeeds', 'CALL', 'Add the validated web seeds to the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:194; TorrentBuilder.java:127-133')
e('CreateTorrentViewModel.buildTorrent', 'TorrentBuilder.build', 'CALL', 'Build the torrent file and subscribe to the result',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:171-173; TorrentBuilder.java:173-178')

# Getters with no caller: filter() and inRange() read the min/max fields directly, and
# a saved full-tree grep finds no getMin()/getMax() call anywhere in the app Java tree.
UNREACHABLE.update({
    'InputFilterRange.getMax': ('no_trigger_in_app',
        'No app code calls getMax on an InputFilterRange. filter() calls inRange(), and inRange() reads the min/max fields directly; a saved full-tree grep finds 0 getMin()/getMax() calls. getMax is not an InputFilter interface method, so framework dispatch cannot reach it.',
        'SRC InputFilterRange.java:59,65-86',
        'SOURCE'),
    'InputFilterRange.getMin': ('no_trigger_in_app',
        'No app code calls getMin on an InputFilterRange. filter() calls inRange(), and inRange() reads the min/max fields directly; a saved full-tree grep finds 0 getMin()/getMax() calls. getMin is not an InputFilter interface method, so framework dispatch cannot reach it.',
        'SRC InputFilterRange.java:53,65-86',
        'SOURCE'),
})

# Suppress bytecode auto edges into the two UNREACHABLE getters. Neither class is
# subclassed in the app, so there are no @Variant generated copies to add.
SUPPRESS.update({
    'InputFilterRange.getMax', 'InputFilterRange.getMin',
})
