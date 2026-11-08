# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 108 part (MainActivity and SessionLogFilterDialog). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b108_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Rows covered by existing graph_def edges are listed in the .md
# Dependencies line; every other REACHABLE row has an edge here.

e('MainActivity.onDrawerGroupsCreated', 'MainActivity.applyExpandState', 'CALL', 'Apply the stored expand state for a drawer group after its groups are created', cls='explicit', evidence='SRC ui/main/MainActivity.java:599; SRC ui/main/MainActivity.java:603-608')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$0', 'FRAMEWORK', 'Persist group state after a user collapse', guard='fromUser == true', cls='non_standard', via='ExpandableItemManager group listener', evidence='INFERRED expandable adapter listener dispatch; SRC ui/main/MainActivity.java:233-235')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$1', 'FRAMEWORK', 'Persist group state after a user expansion', guard='fromUser == true', cls='non_standard', via='ExpandableItemManager group listener', evidence='INFERRED expandable adapter listener dispatch; SRC ui/main/MainActivity.java:237-239')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$2', 'FRAMEWORK', 'Dispatch a click on the add-tag button', cls='standard', evidence='INFERRED framework click dispatch; SRC ui/main/MainActivity.java:273-275')
e('MainActivity.initDrawer', 'MainActivity.lambda$initDrawer$3', 'FRAMEWORK', 'Dispatch a click on the tags section header', cls='standard', evidence='INFERRED framework click dispatch; SRC ui/main/MainActivity.java:282-290')
e('MainActivity.initSearch', 'MainActivity.lambda$initSearch$13', 'FRAMEWORK', 'Dispatch a SearchView close event', cls='non_standard', via='SearchView close dispatch', evidence='INFERRED SearchView dispatch; SRC ui/main/MainActivity.java:709-712')
e('MainActivity.setInitSelection', 'MainActivity.lambda$setInitSelection$11', 'CALL', 'Test each drawer item against the stored tag ID', cls='non_standard', via='Rx filter dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:515-516')
e('MainActivity.setInitSelection', 'MainActivity.lambda$setInitSelection$12', 'CALL', 'Restore the matching stored tag selection and filter', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:518-525')
e('MainActivity.subscribeAlertDialog', 'MainActivity.lambda$subscribeAlertDialog$4', 'CALL', 'Deliver alert-dialog events to the dialog handler', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:408-434')
e('MainActivity.subscribeMsgViewModel', 'MainActivity.lambda$subscribeMsgViewModel$5', 'CALL', 'Show the blank fragment when torrent details close', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:442-444')
e('MainActivity.subscribeMsgViewModel', 'MainActivity.lambda$subscribeMsgViewModel$6', 'CALL', 'Show the blank fragment when the open torrent is deleted', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:449-455')
e('MainActivity.subscribeNeedStartEngine', 'MainActivity.lambda$subscribeNeedStartEngine$7', 'CALL', 'Pass through the need-start flag', cls='non_standard', via='Rx filter dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:466')
e('MainActivity.subscribeNeedStartEngine', 'MainActivity.lambda$subscribeNeedStartEngine$8', 'CALL', 'Start the engine when requested', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:467')
e('MainActivity.subscribeTags', 'MainActivity.lambda$subscribeTags$10', 'CALL', 'Restore the initial selection and submit the tag list', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:481-486')
e('MainActivity.subscribeTags', 'MainActivity.lambda$subscribeTags$9', 'CALL', 'Build the empty, no-tags and tag rows from the tag list', cls='non_standard', via='Rx flatMapSingle dispatch', evidence='INFERRED Rx dispatch; SRC ui/main/MainActivity.java:473-480')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No intra-group SUPPRESS pair: this batch has no UNREACHABLE method,
# and no REACHABLE method here calls a proposed-UNREACHABLE method in
# batches 108-112 in bytecode (see REPORT.md for the cross-group
# candidates examined and rejected, and for the reconciliation note).
SUPPRESS.update(set())
