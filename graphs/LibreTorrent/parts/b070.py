# Citation-form rework 2026-11-01: evidence paths with a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS, line ranges unchanged (full paths remain in untouched .md/printed files).
# Batch 70 part (generated databinding Impl groups: ItemTorrentList, ItemTrackersList, TagsListItem; receivers BootReceiver, ConnectionReceiver, NotificationReceiver, PowerReceiver (head rows)).
# Hand-written edges only; rows covered by a pre-existing trunk edge are
# named on the .md Dependencies line and get no duplicate edge here.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b070_printed.txt (this helper's copy:
# scratch/b070_printed.txt).
# Labels/kinds come from the authoritative clone merge-ready batch file;
# nothing is flipped here (see REPORT.md for flagged rows).

e('TorrentListAdapter.onCreateViewHolder', 'ItemTorrentListBindingImpl.<clinit>', 'CALL', 'First reference to the generated Impl class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED class-init rule; SRC ui/main/TorrentListAdapter.java:79-80')
e('TorrentListAdapter.onCreateViewHolder', 'ItemTorrentListBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Inflate dispatches through the generated mapper to the Impl constructor', cls='non_standard', via='DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED generated mapper dispatch; SRC ui/main/TorrentListAdapter.java:79-80')
e('ItemTorrentListBindingImpl.<init>(DataBindingComponent,View)', 'ItemTorrentListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg Impl constructor chains to the 3-arg constructor', cls='explicit', evidence='INFERRED generated ctor chaining (javap: 2-arg ctor invokespecial 3-arg ctor); SRC ui/main/TorrentListAdapter.java:79-80')
e('ItemTorrentListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'ItemTorrentListBinding.<init>', 'CALL', 'Generated Impl constructor calls the base Binding constructor', cls='explicit', evidence='INFERRED generated super call (javap: 3-arg ctor invokespecial base <init>); SRC ui/main/TorrentListAdapter.java:79-80')
e('ItemTorrentListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'ItemTorrentListBindingImpl.invalidateAll', 'CALL', 'Generated Impl constructor invalidates all bindings after construction', cls='explicit', evidence='INFERRED generated ctor body (javap: 3-arg ctor invokevirtual invalidateAll); SRC ui/main/TorrentListAdapter.java:79-80')
e('ItemTorrentListBindingImpl.invalidateAll', 'ItemTorrentListBindingImpl.executeBindings', 'CALL', 'Invalidation requests a rebind, which runs the generated binding code', cls='non_standard', via='databinding library rebind dispatch (invalidateAll -> requestRebind -> executePendingBindings -> executeBindings)', evidence='INFERRED databinding rebind dispatch; SRC ui/main/TorrentListAdapter.java:79-80')
e('ItemTorrentListBindingImpl.invalidateAll', 'ItemTorrentListBindingImpl.hasPendingBindings', 'CALL', 'The library rebind path queries pending bindings before running them', cls='non_standard', via='databinding library rebind body queries hasPendingBindings', evidence='INFERRED databinding rebind dispatch; SRC ui/main/TorrentListAdapter.java:79-80')
e('TrackerListAdapter.onCreateViewHolder', 'ItemTrackersListBindingImpl.<clinit>', 'CALL', 'First reference to the generated Impl class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED class-init rule; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73-74')
e('TrackerListAdapter.onCreateViewHolder', 'ItemTrackersListBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Inflate dispatches through the generated mapper to the Impl constructor', cls='non_standard', via='DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED generated mapper dispatch; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73-74')
e('ItemTrackersListBindingImpl.<init>(DataBindingComponent,View)', 'ItemTrackersListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg Impl constructor chains to the 3-arg constructor', cls='explicit', evidence='INFERRED generated ctor chaining (javap: 2-arg ctor invokespecial 3-arg ctor); SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73-74')
e('ItemTrackersListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'ItemTrackersListBinding.<init>', 'CALL', 'Generated Impl constructor calls the base Binding constructor', cls='explicit', evidence='INFERRED generated super call (javap: 3-arg ctor invokespecial base <init>); SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73-74')
e('ItemTrackersListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'ItemTrackersListBindingImpl.invalidateAll', 'CALL', 'Generated Impl constructor invalidates all bindings after construction', cls='explicit', evidence='INFERRED generated ctor body (javap: 3-arg ctor invokevirtual invalidateAll); SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73-74')
e('ItemTrackersListBindingImpl.invalidateAll', 'ItemTrackersListBindingImpl.executeBindings', 'CALL', 'Invalidation requests a rebind, which runs the generated binding code', cls='non_standard', via='databinding library rebind dispatch (invalidateAll -> requestRebind -> executePendingBindings -> executeBindings)', evidence='INFERRED databinding rebind dispatch; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73-74')
e('ItemTrackersListBindingImpl.invalidateAll', 'ItemTrackersListBindingImpl.hasPendingBindings', 'CALL', 'The library rebind path queries pending bindings before running them', cls='non_standard', via='databinding library rebind body queries hasPendingBindings', evidence='INFERRED databinding rebind dispatch; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73-74')
e('tag.TagsAdapter.onCreateViewHolder', 'TagsListItemBindingImpl.<clinit>', 'CALL', 'First reference to the generated Impl class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED class-init rule; SRC ui/tag/TagsAdapter.java:48-53')
e('tag.TagsAdapter.onCreateViewHolder', 'TagsListItemBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Inflate dispatches through the generated mapper to the Impl constructor', cls='non_standard', via='DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED generated mapper dispatch; SRC ui/tag/TagsAdapter.java:48-53')
e('TagsListItemBindingImpl.<init>(DataBindingComponent,View)', 'TagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg Impl constructor chains to the 3-arg constructor', cls='explicit', evidence='INFERRED generated ctor chaining (javap: 2-arg ctor invokespecial 3-arg ctor); SRC ui/tag/TagsAdapter.java:48-53')
e('TagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'TagsListItemBinding.<init>', 'CALL', 'Generated Impl constructor calls the base Binding constructor', cls='explicit', evidence='INFERRED generated super call (javap: 3-arg ctor invokespecial base <init>); SRC ui/tag/TagsAdapter.java:48-53')
e('TagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'TagsListItemBindingImpl.invalidateAll', 'CALL', 'Generated Impl constructor invalidates all bindings after construction', cls='explicit', evidence='INFERRED generated ctor body (javap: 3-arg ctor invokevirtual invalidateAll); SRC ui/tag/TagsAdapter.java:48-53')
e('TagsListItemBindingImpl.invalidateAll', 'TagsListItemBindingImpl.executeBindings', 'CALL', 'Invalidation requests a rebind, which runs the generated binding code', cls='non_standard', via='databinding library rebind dispatch (invalidateAll -> requestRebind -> executePendingBindings -> executeBindings)', evidence='INFERRED databinding rebind dispatch; SRC ui/tag/TagsAdapter.java:48-53')
e('TagsListItemBindingImpl.invalidateAll', 'TagsListItemBindingImpl.hasPendingBindings', 'CALL', 'The library rebind path queries pending bindings before running them', cls='non_standard', via='databinding library rebind body queries hasPendingBindings', evidence='INFERRED databinding rebind dispatch; SRC ui/tag/TagsAdapter.java:48-53')
e('BootReceiver.onReceive', 'BootReceiver.isBootCompleted', 'CALL', 'Boot-completed branch tests the received action', cls='explicit', evidence='SRC receiver/BootReceiver.java:44')
e('TorrentEngine.<init>', 'ConnectionReceiver.<init>', 'CALL', 'Field initialiser constructs the connection receiver with the engine', cls='explicit', evidence='SRC TorrentEngine.java:109')
e('TorrentEngine.switchConnectionReceiver', 'ConnectionReceiver.getFilter', 'CALL', 'Dynamic registration builds the connectivity filter', cls='explicit', evidence='SRC TorrentEngine.java:1020')
e('TorrentEngine.switchConnectionReceiver', 'ConnectionReceiver.onReceive', 'CALL', 'Dynamically registered receiver delivers connectivity broadcasts', cls='non_standard', via='framework broadcast delivery after dynamic registration', evidence='INFERRED framework dispatch; SRC TorrentEngine.java:1020; SRC receiver/ConnectionReceiver.java:37-44')
e('TorrentEngine.<init>', 'PowerReceiver.<init>', 'CALL', 'Field initialiser constructs the power receiver with the engine', cls='explicit', evidence='SRC TorrentEngine.java:108')
e('TorrentEngine.switchPowerReceiver', 'PowerReceiver.getCustomFilter', 'CALL', 'Custom-battery-control branch registers with the custom filter', cls='explicit', evidence='SRC TorrentEngine.java:1001')

# UNREACHABLE rows in this batch (batch labels kept, not flipped).
UNREACHABLE.update({
    'ItemTorrentDownloadableFileBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/addtorrent/DownloadableFilesAdapter.java:60-61; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'ItemTorrentDownloadableFileBindingImpl.setVariable': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/addtorrent/DownloadableFilesAdapter.java:60-61; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'ItemTorrentListBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/main/TorrentListAdapter.java:79-80; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'ItemTorrentListBindingImpl.setVariable': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/main/TorrentListAdapter.java:79-80; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'ItemTrackersListBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73-74; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'ItemTrackersListBindingImpl.setVariable': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73-74; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'TagsListItemBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/tag/TagsAdapter.java:48-53; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'TagsListItemBindingImpl.setVariable': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/tag/TagsAdapter.java:48-53; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
})

# SUPPRESS: recomputed from auto_calls.json + javap scan for this batch's
# rows; the recomputation and any cross-group candidates are recorded in
# REPORT.md. No intra-group pair was found, so no entries apply here.
SUPPRESS.update(set())
