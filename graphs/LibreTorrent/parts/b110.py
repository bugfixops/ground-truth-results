# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 110 part (MainFragment lambdas and lifecycle). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b110_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Rows covered by existing graph_def edges are listed in the .md
# Dependencies line; every other REACHABLE row has an edge here.

e('MainFragment.getAllTorrentsSingle', 'MainFragment.lambda$getAllTorrentsSingle$7', 'CALL', 'Log torrent info list errors', cls='non_standard', via='Rx subscribe error dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:345-348')
e('MainFragment.initFabSpeedDial', 'MainFragment.lambda$initFabSpeedDial$11', 'FRAMEWORK', 'Dispatch a floating-action-menu selection', cls='non_standard', via='SpeedDial action-selection dispatch', evidence='INFERRED SpeedDial widget dispatch; SRC ui/main/MainFragment.java:416-430')
e('MainFragment.<init>', 'MainFragment.lambda$new$18', 'FRAMEWORK', 'Deliver the torrent-file picker result to the field callback', cls='non_standard', via='Activity Result dispatch', evidence='INFERRED Activity Result dispatch; SRC ui/main/MainFragment.java:619-637')
e('MainFragment.observeTorrents', 'MainFragment.lambda$observeTorrents$1', 'CALL', 'Filter, map and sort the torrent info list', cls='non_standard', via='Rx flatMapSingle dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:289-297')
e('MainFragment.observeTorrents', 'MainFragment.lambda$observeTorrents$2', 'CALL', 'Log torrent info list errors', cls='non_standard', via='Rx subscribe error dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:298-300')
e('MainFragment.showAddTorrentMenu', 'MainFragment.lambda$showAddTorrentMenu$0', 'FRAMEWORK', 'Register and open the context menu after the window is displayed', cls='non_standard', via='View post dispatch', evidence='INFERRED View dispatch; SRC ui/main/MainFragment.java:216-220')
e('MainFragment.subscribeAlertDialog', 'MainFragment.lambda$subscribeAlertDialog$3', 'CALL', 'Delete the selected torrents on positive dialog confirmation', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:304-323')
e('MainFragment.subscribeForceSortAndFilter', 'MainFragment.lambda$subscribeForceSortAndFilter$4', 'CALL', 'Pass through the forced sort-and-filter flag', cls='non_standard', via='Rx filter dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:327-328')
e('MainFragment.subscribeForceSortAndFilter', 'MainFragment.lambda$subscribeForceSortAndFilter$5', 'CALL', 'Refresh the torrent list on a forced sort or filter update', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:330')
e('MainFragment.subscribeMsgViewModel', 'MainFragment.lambda$subscribeMsgViewModel$10', 'CALL', 'Clear the open-torrent mark when details close in two-pane mode', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:370-376')
e('MainFragment.subscribeTorrentsDeleted', 'MainFragment.lambda$subscribeTorrentsDeleted$8', 'CALL', 'Match a deleted torrent ID against the opened item', cls='non_standard', via='Rx filter dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:354-362')
e('MainFragment.subscribeTorrentsDeleted', 'MainFragment.lambda$subscribeTorrentsDeleted$9', 'CALL', 'Clear the open-torrent mark when the open torrent is deleted', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:363-366')
e('MainFragment.subscribeAdapter', 'MainFragment.observeTorrents', 'CALL', 'Observe the torrent info list for the adapter', cls='explicit', evidence='SRC ui/main/MainFragment.java:282; SRC ui/main/MainFragment.java:285-300')
e('MainFragment.onStart', 'MainFragment.onResume', 'LIFECYCLE', 'Resume the fragment after start', cls='standard', evidence='SRC ui/main/MainFragment.java:233-241; SRC ui/main/MainFragment.java:253-257')
e('MainFragment.onResume', 'MainFragment.onSaveInstanceState', 'LIFECYCLE', 'Save the fragment list state and selection for a resumed fragment', cls='standard', evidence='SRC ui/main/MainFragment.java:253-257; SRC ui/main/MainFragment.java:271-277')
e('MainFragment.onStart', 'MainFragment.onStop', 'LIFECYCLE', 'Stop the fragment after it leaves the started state', cls='standard', evidence='SRC ui/main/MainFragment.java:233-241; SRC ui/main/MainFragment.java:245-249')
e('MainFragment.onViewCreated', 'MainFragment.onViewStateRestored', 'LIFECYCLE', 'Restore the saved torrent list state after view creation', cls='standard', evidence='SRC ui/main/MainFragment.java:125; SRC ui/main/MainFragment.java:262-267')
e('MainFragment.onViewCreated', 'MainFragment$1.<init>', 'CALL', 'Create the torrent-list item animator', cls='explicit', evidence='SRC ui/main/MainFragment.java:141-147')
e('MainFragment.onViewCreated', 'MainFragment$1.canReuseUpdatedViewHolder', 'FRAMEWORK', 'Ask the installed animator whether an updated holder can be reused', cls='non_standard', via='RecyclerView item-animation dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/main/MainFragment.java:141-150')
e('MainFragment.onViewCreated', 'MainFragment$2.<init>', 'CALL', 'Create the selection observer and register it with the tracker', cls='explicit', evidence='SRC ui/main/MainFragment.java:165-166')
e('MainFragment.onViewCreated', 'MainFragment$2.onSelectionChanged', 'FRAMEWORK', 'Dispatch selection changes to the registered observer', cls='non_standard', via='SelectionTracker observer dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/main/MainFragment.java:165-185')
e('MainFragment.onViewCreated', 'MainFragment$2.onSelectionRestored', 'FRAMEWORK', 'Dispatch a restored selection to the registered observer', cls='non_standard', via='SelectionTracker restore dispatch', evidence='INFERRED SelectionTracker dispatch; SRC ui/main/MainFragment.java:165-195')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No intra-group SUPPRESS pair: this batch has no UNREACHABLE method,
# and no REACHABLE method here calls a proposed-UNREACHABLE method in
# batches 108-112 in bytecode (see REPORT.md for the cross-group
# candidates examined and rejected, and for the reconciliation note).
SUPPRESS.update(set())
