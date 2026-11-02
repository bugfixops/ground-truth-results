# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 111 part (MainFragment action mode, MainViewModel and MsgMainViewModel). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b111_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Rows covered by existing graph_def edges are listed in the .md
# Dependencies line; every other REACHABLE row has an edge here.

e('MainFragment.<init>', 'MainFragment$3.<init>', 'CALL', 'Create the contextual action-mode callback field', cls='non_standard', via='field-initialiser construction during enclosing construction', evidence='SRC ui/main/MainFragment.java:457')
e('MainFragment$2.onSelectionChanged', 'MainFragment$3.onActionItemClicked', 'FRAMEWORK', 'Dispatch contextual menu selections to the action-mode callback', cls='non_standard', via='ActionMode menu-item dispatch', evidence='INFERRED ActionMode dispatch; SRC ui/main/MainFragment.java:168-185; SRC ui/main/MainFragment.java:475-492')
e('MainFragment$2.onSelectionChanged', 'MainFragment$3.onCreateActionMode', 'FRAMEWORK', 'Create the contextual action mode when a torrent is selected', cls='non_standard', via='ActionMode creation dispatch', evidence='INFERRED ActionMode dispatch; SRC ui/main/MainFragment.java:168-185; SRC ui/main/MainFragment.java:466-473')
e('MainFragment$2.onSelectionChanged', 'MainFragment$3.onDestroyActionMode', 'FRAMEWORK', 'Tear down the contextual action mode when the selection clears', cls='non_standard', via='ActionMode teardown dispatch', evidence='INFERRED ActionMode dispatch; SRC ui/main/MainFragment.java:175-179; SRC ui/main/MainFragment.java:494-498')
e('MainFragment$2.onSelectionChanged', 'MainFragment$3.onPrepareActionMode', 'FRAMEWORK', 'Prepare the contextual action mode before display', cls='non_standard', via='ActionMode prepare dispatch', evidence='INFERRED ActionMode dispatch; SRC ui/main/MainFragment.java:168-185; SRC ui/main/MainFragment.java:460-463')
e('MainFragment.onViewCreated', 'MainViewModel.<init>', 'FRAMEWORK', 'Instantiate the main ViewModel through its provider', cls='non_standard', via='ViewModelProvider instantiation', evidence='INFERRED ViewModelProvider dispatch; SRC ui/main/MainFragment.java:131-133; SRC ui/main/MainViewModel.java:69-76')
e('MainActivity$3.onTagMenuClicked', 'MainViewModel.deleteTag', 'CALL', 'Delete the selected tag', cls='explicit', evidence='SRC ui/main/MainActivity.java:326-329; SRC ui/main/MainViewModel.java:186-187')
e('MainFragment.getAllTorrentsSingle', 'MainViewModel.getAllTorrentsInfoSingle', 'CALL', 'Read the torrent info list as a single', cls='explicit', evidence='SRC ui/main/MainFragment.java:335; SRC ui/main/MainViewModel.java:81-83')
e('MainFragment.observeTorrents', 'MainViewModel.getFilter', 'CALL', 'Read the current torrent filter for the torrent list', cls='explicit', evidence='SRC ui/main/MainFragment.java:291; SRC ui/main/MainViewModel.java:118-123')
e('MainFragment.observeTorrents', 'MainViewModel.getSorting', 'CALL', 'Read the current torrent sorting for the torrent list', cls='explicit', evidence='SRC ui/main/MainFragment.java:293; SRC ui/main/MainViewModel.java:95-97')
e('MainViewModel.deleteTag', 'MainViewModel.lambda$deleteTag$2', 'CALL', 'Run the tag deletion on the Completable', cls='non_standard', via='Rx Completable.fromRunnable dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainViewModel.java:186-187')
e('MainViewModel.getFilter', 'MainViewModel.lambda$getFilter$1', 'CALL', 'Test each torrent against the combined filters', cls='non_standard', via='Rx filter-operator dispatch of the returned predicate', evidence='INFERRED Rx dispatch; SRC ui/main/MainViewModel.java:118-123; SRC ui/main/MainFragment.java:291')
e('MainViewModel.lambda$getFilter$1', 'MainViewModel.lambda$new$0', 'CALL', 'Test the torrent name against the search query', cls='explicit', evidence='SRC ui/main/MainViewModel.java:121; SRC ui/main/MainViewModel.java:60-67')
e('MainFragment.observeTorrents', 'MainViewModel.observeAllTorrentsInfo', 'CALL', 'Observe the torrent info list', cls='explicit', evidence='SRC ui/main/MainFragment.java:287; SRC ui/main/MainViewModel.java:77-79')
e('MainFragment.subscribeForceSortAndFilter', 'MainViewModel.observeForceSortAndFilter', 'CALL', 'Observe forced sort-and-filter events', cls='explicit', evidence='SRC ui/main/MainFragment.java:327; SRC ui/main/MainViewModel.java:134-136')
e('MainActivity.subscribeNeedStartEngine', 'MainViewModel.observeNeedStartEngine', 'CALL', 'Observe whether the engine needs starting', cls='explicit', evidence='SRC ui/main/MainActivity.java:464; SRC ui/main/MainViewModel.java:154-156')
e('MainActivity.subscribeTags', 'MainViewModel.observeTags', 'CALL', 'Observe the tag list', cls='explicit', evidence='SRC ui/main/MainActivity.java:471; SRC ui/main/MainViewModel.java:182-184')
e('MainFragment.subscribeTorrentsDeleted', 'MainViewModel.observeTorrentsDeleted', 'CALL', 'Observe torrent deletion events', cls='explicit', evidence='SRC ui/main/MainFragment.java:352; SRC ui/main/MainViewModel.java:85-87')
e('MainFragment.onViewCreated', 'MsgMainViewModel.<init>', 'FRAMEWORK', 'Instantiate the main message ViewModel through its provider', cls='non_standard', via='ViewModelProvider instantiation', evidence='INFERRED ViewModelProvider dispatch; SRC ui/main/MainFragment.java:131-133')
e('MainFragment.subscribeMsgViewModel', 'MsgMainViewModel.observeTorrentDetailsClosed', 'CALL', 'Observe torrent-details-closed events', cls='explicit', evidence='SRC ui/main/MainFragment.java:370; SRC ui/main/MsgMainViewModel.java:48-51')
e('MainActivity.subscribeMsgViewModel', 'MsgMainViewModel.observeTorrentDetailsOpened', 'CALL', 'Observe torrent-details-opened events', cls='explicit', evidence='SRC ui/main/MainActivity.java:438-440; SRC ui/main/MsgMainViewModel.java:38-41')
e('MainActivity.onFragmentFinished', 'MsgMainViewModel.torrentDetailsClosed', 'CALL', 'Publish the details-closed event when a two-pane detail fragment finishes', cls='explicit', evidence='SRC ui/main/MainActivity.java:806-811; SRC ui/main/MsgMainViewModel.java:43-46')
e('MainFragment.onViewCreated', 'TorrentListAdapter.<clinit>', 'FRAMEWORK', 'Initialise the torrent-list adapter class on first use', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation; SRC ui/main/MainFragment.java:136; SRC ui/main/TorrentListAdapter.java:308-323')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No intra-group SUPPRESS pair: this batch has no UNREACHABLE method,
# and no REACHABLE method here calls a proposed-UNREACHABLE method in
# batches 108-112 in bytecode (see REPORT.md for the cross-group
# candidates examined and rejected, and for the reconciliation note).
SUPPRESS.update(set())
