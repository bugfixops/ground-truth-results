# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 109 part (MainActivity anonymous classes and MainFragment entry). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b109_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Rows covered by existing graph_def edges are listed in the .md
# Dependencies line; every other REACHABLE row has an edge here.

e('MainActivity.onCreate', 'MainActivity$1.<init>', 'CALL', 'Create the main screen permission-result callback', cls='explicit', evidence='SRC ui/main/MainActivity.java:153')
e('PermissionManager.lambda$new$1', 'MainActivity$1.onNotificationResult', 'RESULT', 'Deliver the notification permission result to the callback', cls='non_standard', via='PermissionManager result dispatch', evidence='INFERRED PermissionManager dispatch; SRC ui/PermissionManager.java:87; SRC ui/main/MainActivity.java:167-171')
e('PermissionManager.lambda$new$1', 'MainActivity$1.onStorageResult', 'RESULT', 'Deliver the storage permission result to the callback', cls='non_standard', via='PermissionManager result dispatch', evidence='INFERRED PermissionManager dispatch; SRC ui/PermissionManager.java:81; SRC ui/main/MainActivity.java:155-165')
e('MainActivity.initLayout', 'MainActivity$2.<init>', 'CALL', 'Create the non-scrolling layout manager for the drawer list', cls='explicit', evidence='SRC ui/main/MainActivity.java:198-203')
e('MainActivity.initDrawer', 'MainActivity$2.canScrollVertically', 'FRAMEWORK', 'Ask the drawer layout manager whether it can scroll vertically', cls='non_standard', via='RecyclerView layout dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/main/MainActivity.java:198-203; SRC ui/main/MainActivity.java:254')
e('MainActivity.<init>', 'MainActivity$3.<init>', 'CALL', 'Create the drawer tag click listener field', cls='non_standard', via='field-initialiser construction during enclosing construction', evidence='SRC ui/main/MainActivity.java:295')
e('MainActivity$3.onTagMenuClicked', 'MainActivity$3.lambda$onTagMenuClicked$0', 'CALL', 'Reset the drawer selection after deleting the selected tag', cls='non_standard', via='Rx subscribe success dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:326-339')
e('MainActivity$3.onTagMenuClicked', 'MainActivity$3.lambda$onTagMenuClicked$1', 'CALL', 'Show an error when tag deletion fails', cls='non_standard', via='Rx subscribe error dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:341-345')
e('drawer.TagsAdapter$ItemViewHolder.lambda$bind$1', 'MainActivity$3.onTagMenuClicked', 'CALL', 'Deliver a tag menu click to the drawer listener', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:198-203; SRC ui/main/MainActivity.java:316-323')
e('drawer.TagsAdapter$ItemViewHolder.lambda$bind$0', 'MainActivity$3.onTagSelected', 'CALL', 'Deliver a tag selection to the drawer listener', cls='explicit', evidence='SRC ui/main/drawer/TagsAdapter.java:192-195; SRC ui/main/MainActivity.java:297-311')
e('MainActivity.initSearch', 'MainActivity$4.<init>', 'CALL', 'Create the search query text listener', cls='explicit', evidence='SRC ui/main/MainActivity.java:714')
e('MainActivity.initSearch', 'MainActivity$4.onQueryTextChange', 'FRAMEWORK', 'Deliver search text changes to the query listener', cls='non_standard', via='SearchView text-change dispatch', evidence='INFERRED SearchView dispatch; SRC ui/main/MainActivity.java:714-727')
e('MainActivity.initSearch', 'MainActivity$4.onQueryTextSubmit', 'FRAMEWORK', 'Deliver a submitted search query to the query listener', cls='non_standard', via='SearchView submit dispatch', evidence='INFERRED SearchView dispatch; SRC ui/main/MainActivity.java:714-727')
e('MainActivity.onCreate', 'MainFragment.<clinit>', 'FRAMEWORK', 'Initialise the main fragment class on first use', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation; SRC ui/main/MainActivity.java:182-185; SRC ui/main/MainFragment.java:88')
e('MainActivity$3.lambda$onTagMenuClicked$1', 'MainFragment.getCoordinatorLayout', 'CALL', 'Anchor the tag-deletion error message to the main coordinator layout', cls='explicit', evidence='SRC ui/main/MainActivity.java:339-344; SRC ui/main/MainFragment.java:109-111')
e('MainFragment.deleteTorrents', 'MainFragment.lambda$deleteTorrents$12', 'CALL', 'Map each selected torrent to its torrent ID', cls='non_standard', via='Rx map dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:578-582')
e('MainFragment.deleteTorrents', 'MainFragment.lambda$deleteTorrents$13', 'CALL', 'Delete the collected torrent IDs with the chosen file option', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:581-583')
e('MainFragment.forceAnnounceTorrents', 'MainFragment.lambda$forceAnnounceTorrents$16', 'CALL', 'Map each selected torrent to its torrent ID', cls='non_standard', via='Rx map dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:613-615')
e('MainFragment.forceAnnounceTorrents', 'MainFragment.lambda$forceAnnounceTorrents$17', 'CALL', 'Announce the collected torrent IDs', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:616')
e('MainFragment.forceRecheckTorrents', 'MainFragment.lambda$forceRecheckTorrents$14', 'CALL', 'Map each selected torrent to its torrent ID', cls='non_standard', via='Rx map dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:602-604')
e('MainFragment.forceRecheckTorrents', 'MainFragment.lambda$forceRecheckTorrents$15', 'CALL', 'Recheck the collected torrent IDs', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:605')
e('MainFragment.getAllTorrentsSingle', 'MainFragment.lambda$getAllTorrentsSingle$6', 'CALL', 'Filter, map and sort the torrent info list', cls='non_standard', via='Rx flatMap dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainFragment.java:336-343')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No intra-group SUPPRESS pair: this batch has no UNREACHABLE method,
# and no REACHABLE method here calls a proposed-UNREACHABLE method in
# batches 108-112 in bytecode (see REPORT.md for the cross-group
# candidates examined and rejected, and for the reconciliation note).
SUPPRESS.update(set())
