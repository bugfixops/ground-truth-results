# Citation-form rework 2026-11-01: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 68 part (generated databinding Impl groups: FragmentFeed, FragmentFeedItems, FragmentMain, ItemFeedChannelList, ItemFeedItemsList (head rows 38-40)).
# Hand-written edges only; rows covered by a pre-existing trunk edge are
# named on the .md Dependencies line and get no duplicate edge here.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b068_printed.txt (this helper's copy:
# scratch/b068_printed.txt).
# Labels/kinds come from the authoritative clone merge-ready batch file;
# nothing is flipped here (see REPORT.md for flagged rows).

e('FeedFragment.onCreateView', 'FragmentFeedBindingImpl.<clinit>', 'CALL', 'First reference to the generated Impl class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED class-init rule; SRC ui/feeds/FeedFragment.java:99')
e('FeedFragment.onCreateView', 'FragmentFeedBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Inflate dispatches through the generated mapper to the Impl constructor', cls='non_standard', via='DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED generated mapper dispatch; SRC ui/feeds/FeedFragment.java:99')
e('FragmentFeedBindingImpl.<init>(DataBindingComponent,View)', 'FragmentFeedBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg Impl constructor chains to the 3-arg constructor', cls='explicit', evidence='INFERRED generated ctor chaining (javap: 2-arg ctor invokespecial 3-arg ctor); SRC ui/feeds/FeedFragment.java:99')
e('FragmentFeedBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentFeedBinding.<init>', 'CALL', 'Generated Impl constructor calls the base Binding constructor', cls='explicit', evidence='INFERRED generated super call (javap: 3-arg ctor invokespecial base <init>); SRC ui/feeds/FeedFragment.java:99')
e('FragmentFeedBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentFeedBindingImpl.invalidateAll', 'CALL', 'Generated Impl constructor invalidates all bindings after construction', cls='explicit', evidence='INFERRED generated ctor body (javap: 3-arg ctor invokevirtual invalidateAll); SRC ui/feeds/FeedFragment.java:99')
e('FragmentFeedBindingImpl.invalidateAll', 'FragmentFeedBindingImpl.executeBindings', 'CALL', 'Invalidation requests a rebind, which runs the generated binding code', cls='non_standard', via='databinding library rebind dispatch (invalidateAll -> requestRebind -> executePendingBindings -> executeBindings)', evidence='INFERRED databinding rebind dispatch; SRC ui/feeds/FeedFragment.java:99')
e('FragmentFeedBindingImpl.invalidateAll', 'FragmentFeedBindingImpl.hasPendingBindings', 'CALL', 'The library rebind path queries pending bindings before running them', cls='non_standard', via='databinding library rebind body queries hasPendingBindings', evidence='INFERRED databinding rebind dispatch; SRC ui/feeds/FeedFragment.java:99')
e('FeedItemsFragment.onCreateView', 'FragmentFeedItemsBindingImpl.<clinit>', 'CALL', 'First reference to the generated Impl class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED class-init rule; SRC ui/feeditems/FeedItemsFragment.java:111')
e('FeedItemsFragment.onCreateView', 'FragmentFeedItemsBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Inflate dispatches through the generated mapper to the Impl constructor', cls='non_standard', via='DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED generated mapper dispatch; SRC ui/feeditems/FeedItemsFragment.java:111')
e('FragmentFeedItemsBindingImpl.<init>(DataBindingComponent,View)', 'FragmentFeedItemsBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg Impl constructor chains to the 3-arg constructor', cls='explicit', evidence='INFERRED generated ctor chaining (javap: 2-arg ctor invokespecial 3-arg ctor); SRC ui/feeditems/FeedItemsFragment.java:111')
e('FragmentFeedItemsBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentFeedItemsBinding.<init>', 'CALL', 'Generated Impl constructor calls the base Binding constructor', cls='explicit', evidence='INFERRED generated super call (javap: 3-arg ctor invokespecial base <init>); SRC ui/feeditems/FeedItemsFragment.java:111')
e('FragmentFeedItemsBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentFeedItemsBindingImpl.invalidateAll', 'CALL', 'Generated Impl constructor invalidates all bindings after construction', cls='explicit', evidence='INFERRED generated ctor body (javap: 3-arg ctor invokevirtual invalidateAll); SRC ui/feeditems/FeedItemsFragment.java:111')
e('FragmentFeedItemsBindingImpl.invalidateAll', 'FragmentFeedItemsBindingImpl.executeBindings', 'CALL', 'Invalidation requests a rebind, which runs the generated binding code', cls='non_standard', via='databinding library rebind dispatch (invalidateAll -> requestRebind -> executePendingBindings -> executeBindings)', evidence='INFERRED databinding rebind dispatch; SRC ui/feeditems/FeedItemsFragment.java:111')
e('FragmentFeedItemsBindingImpl.invalidateAll', 'FragmentFeedItemsBindingImpl.hasPendingBindings', 'CALL', 'The library rebind path queries pending bindings before running them', cls='non_standard', via='databinding library rebind body queries hasPendingBindings', evidence='INFERRED databinding rebind dispatch; SRC ui/feeditems/FeedItemsFragment.java:111')
e('MainFragment.onCreateView', 'FragmentMainBindingImpl.<clinit>', 'CALL', 'First reference to the generated Impl class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED class-init rule; SRC ui/main/MainFragment.java:119')
e('MainFragment.onCreateView', 'FragmentMainBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Inflate dispatches through the generated mapper to the Impl constructor', cls='non_standard', via='DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED generated mapper dispatch; SRC ui/main/MainFragment.java:119')
e('FragmentMainBindingImpl.<init>(DataBindingComponent,View)', 'FragmentMainBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg Impl constructor chains to the 3-arg constructor', cls='explicit', evidence='INFERRED generated ctor chaining (javap: 2-arg ctor invokespecial 3-arg ctor); SRC ui/main/MainFragment.java:119')
e('FragmentMainBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentMainBinding.<init>', 'CALL', 'Generated Impl constructor calls the base Binding constructor', cls='explicit', evidence='INFERRED generated super call (javap: 3-arg ctor invokespecial base <init>); SRC ui/main/MainFragment.java:119')
e('FragmentMainBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentMainBindingImpl.invalidateAll', 'CALL', 'Generated Impl constructor invalidates all bindings after construction', cls='explicit', evidence='INFERRED generated ctor body (javap: 3-arg ctor invokevirtual invalidateAll); SRC ui/main/MainFragment.java:119')
e('FragmentMainBindingImpl.invalidateAll', 'FragmentMainBindingImpl.executeBindings', 'CALL', 'Invalidation requests a rebind, which runs the generated binding code', cls='non_standard', via='databinding library rebind dispatch (invalidateAll -> requestRebind -> executePendingBindings -> executeBindings)', evidence='INFERRED databinding rebind dispatch; SRC ui/main/MainFragment.java:119')
e('FragmentMainBindingImpl.invalidateAll', 'FragmentMainBindingImpl.hasPendingBindings', 'CALL', 'The library rebind path queries pending bindings before running them', cls='non_standard', via='databinding library rebind body queries hasPendingBindings', evidence='INFERRED databinding rebind dispatch; SRC ui/main/MainFragment.java:119')
e('FeedChannelListAdapter.onCreateViewHolder', 'ItemFeedChannelListBindingImpl.<clinit>', 'CALL', 'First reference to the generated Impl class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED class-init rule; SRC ui/feeds/FeedChannelListAdapter.java:82-85')
e('FeedChannelListAdapter.onCreateViewHolder', 'ItemFeedChannelListBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Inflate dispatches through the generated mapper to the Impl constructor', cls='non_standard', via='DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED generated mapper dispatch; SRC ui/feeds/FeedChannelListAdapter.java:82-85')
e('ItemFeedChannelListBindingImpl.<init>(DataBindingComponent,View)', 'ItemFeedChannelListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg Impl constructor chains to the 3-arg constructor', cls='explicit', evidence='INFERRED generated ctor chaining (javap: 2-arg ctor invokespecial 3-arg ctor); SRC ui/feeds/FeedChannelListAdapter.java:82-85')
e('ItemFeedChannelListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'ItemFeedChannelListBinding.<init>', 'CALL', 'Generated Impl constructor calls the base Binding constructor', cls='explicit', evidence='INFERRED generated super call (javap: 3-arg ctor invokespecial base <init>); SRC ui/feeds/FeedChannelListAdapter.java:82-85')
e('ItemFeedChannelListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'ItemFeedChannelListBindingImpl.invalidateAll', 'CALL', 'Generated Impl constructor invalidates all bindings after construction', cls='explicit', evidence='INFERRED generated ctor body (javap: 3-arg ctor invokevirtual invalidateAll); SRC ui/feeds/FeedChannelListAdapter.java:82-85')
e('ItemFeedChannelListBindingImpl.invalidateAll', 'ItemFeedChannelListBindingImpl.executeBindings', 'CALL', 'Invalidation requests a rebind, which runs the generated binding code', cls='non_standard', via='databinding library rebind dispatch (invalidateAll -> requestRebind -> executePendingBindings -> executeBindings)', evidence='INFERRED databinding rebind dispatch; SRC ui/feeds/FeedChannelListAdapter.java:82-85')
e('ItemFeedChannelListBindingImpl.invalidateAll', 'ItemFeedChannelListBindingImpl.hasPendingBindings', 'CALL', 'The library rebind path queries pending bindings before running them', cls='non_standard', via='databinding library rebind body queries hasPendingBindings', evidence='INFERRED databinding rebind dispatch; SRC ui/feeds/FeedChannelListAdapter.java:82-85')
e('FeedItemsAdapter.onCreateViewHolder', 'ItemFeedItemsListBindingImpl.<clinit>', 'CALL', 'First reference to the generated Impl class runs its static initialiser', cls='non_standard', via='JVM class-init on first reference through DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED class-init rule; SRC ui/feeditems/FeedItemsAdapter.java:67-70')
e('FeedItemsAdapter.onCreateViewHolder', 'ItemFeedItemsListBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Inflate dispatches through the generated mapper to the Impl constructor', cls='non_standard', via='DataBindingUtil.inflate + generated mapper dispatch', evidence='INFERRED generated mapper dispatch; SRC ui/feeditems/FeedItemsAdapter.java:67-70')
e('ItemFeedItemsListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'ItemFeedItemsListBinding.<init>', 'CALL', 'Generated Impl constructor calls the base Binding constructor', cls='explicit', evidence='INFERRED generated super call (javap: 3-arg ctor invokespecial base <init>); SRC ui/feeditems/FeedItemsAdapter.java:67-70')

# UNREACHABLE rows in this batch (batch labels kept, not flipped).
UNREACHABLE.update({
    'FragmentDetailTorrentTrackerListBindingImpl.setVariable': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:105; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'FragmentFeedBindingImpl.setVariable': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/feeds/FeedFragment.java:99; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'FragmentFeedBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/feeds/FeedFragment.java:99; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'FragmentFeedItemsBindingImpl.setVariable': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/feeditems/FeedItemsFragment.java:111; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'FragmentFeedItemsBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/feeditems/FeedItemsFragment.java:111; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'FragmentMainBindingImpl.setVariable': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/main/MainFragment.java:119; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'FragmentMainBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/main/MainFragment.java:119; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'ItemFeedChannelListBindingImpl.setVariable': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/feeds/FeedChannelListAdapter.java:82-85; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
    'ItemFeedChannelListBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No variable set on this binding: layout declares no data variable, no include parent passes a variable, and the batch round-2 grep over the 252-file app Java tree finds zero setVariable/onFieldChange hits; D4c closes this family as no_trigger_in_app INFERRED.',
        'INFERRED D4c (no-variable, no-parent binding); inflate site SRC ui/feeds/FeedChannelListAdapter.java:82-85; no setVariable/onFieldChange call on this binding in the printed corpus',
        'INFERRED'),
})

# SUPPRESS: recomputed from auto_calls.json + javap scan for this batch's
# rows; the recomputation and any cross-group candidates are recorded in
# REPORT.md. No intra-group pair was found, so no entries apply here.
SUPPRESS.update(set())
