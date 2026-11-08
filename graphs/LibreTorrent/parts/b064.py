# Citation-form rework 2026-11-01: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# C10 converter note 2026-11-01: edge evidence strings that began with a bare description
# (e.g. 'Generated ctor tail (compiled bytecode); ...') are prefixed 'INFERRED ' so the
# build's evidence-label rule (first token must be SRC/FW-SRC/INFERRED/...) passes;
# bytecode-derived edges are INFERRED evidence. No label, edge, endpoint, or citation changed.
# Batch 64 part (generated data-binding Impl methods: see .md for the Impl groups).
# Edge plan designed per method kind (mapper, ctor chain, rebind, listener,
# field-change) and assembled by scratch/gen_parts.py from the verified
# row/build-name tables; no edge is copied from graph_def.py. Every edge
# endpoint is an exact build name
# (tools/build_graph.py method_names over method_list.json, 4,732 names).
# Generated *BindingImpl source is absent from final_java_only; internal
# generated dispatch is confirmed in the compiled bytecode (javap -c -p)
# and in merger-tree auto_calls.json; each evidence string cites lines
# printed in scratch/b064_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.

e('SelectTagDialog.onCreateDialog', 'DialogSelectTagBindingImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/tag/SelectTagDialog.java:128')
e('DialogSelectTagBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogSelectTagBindingImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/tag/SelectTagDialog.java:128')
e('DrawerEmptyTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DrawerEmptyTagsListItemBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:64-68')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DrawerEmptyTagsListItemBindingImpl.<clinit>', 'CALL', 'Mapper instantiation loads the Impl class on first inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:272 (printed excerpt); SRC ui/main/drawer/TagsAdapter.java:64-68')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DrawerEmptyTagsListItemBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl on DataBindingUtil.inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:272 (printed excerpt); SRC ui/main/drawer/TagsAdapter.java:64-68')
e('DrawerEmptyTagsListItemBindingImpl.<init>(DataBindingComponent,View)', 'DrawerEmptyTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg ctor delegates to the 3-arg ctor via mapBindings', cls='non_standard', via='generated ctor delegation (bytecode invokespecial)', evidence='INFERRED Generated ctor delegation (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:64-68')
e('DrawerEmptyTagsListItemBindingImpl.invalidateAll', 'DrawerEmptyTagsListItemBindingImpl.executeBindings', 'CALL', 'Framework rebind runs executeBindings after invalidateAll requests a rebind', cls='non_standard', via='ViewDataBinding requestRebind dispatch (invalidateAll calls requestRebind in bytecode; framework runnable runs executeBindings)', evidence='INFERRED invalidateAll calls requestRebind (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:64-68')
e('drawer.TagsAdapter.onCreateViewHolder', 'DrawerEmptyTagsListItemBindingImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/main/drawer/TagsAdapter.java:64-68')
e('DrawerEmptyTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DrawerEmptyTagsListItemBindingImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:64-68')
e('DrawerNoTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DrawerNoTagsListItemBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:82-86')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DrawerNoTagsListItemBindingImpl.<clinit>', 'CALL', 'Mapper instantiation loads the Impl class on first inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:278 (printed excerpt); SRC ui/main/drawer/TagsAdapter.java:82-86')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DrawerNoTagsListItemBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl on DataBindingUtil.inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:278 (printed excerpt); SRC ui/main/drawer/TagsAdapter.java:82-86')
e('DrawerNoTagsListItemBindingImpl.<init>(DataBindingComponent,View)', 'DrawerNoTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg ctor delegates to the 3-arg ctor via mapBindings', cls='non_standard', via='generated ctor delegation (bytecode invokespecial)', evidence='INFERRED Generated ctor delegation (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:82-86')
e('DrawerNoTagsListItemBindingImpl.invalidateAll', 'DrawerNoTagsListItemBindingImpl.executeBindings', 'CALL', 'Framework rebind runs executeBindings after invalidateAll requests a rebind', cls='non_standard', via='ViewDataBinding requestRebind dispatch (invalidateAll calls requestRebind in bytecode; framework runnable runs executeBindings)', evidence='INFERRED invalidateAll calls requestRebind (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:82-86')
e('drawer.TagsAdapter.onCreateViewHolder', 'DrawerNoTagsListItemBindingImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/main/drawer/TagsAdapter.java:82-86')
e('DrawerNoTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DrawerNoTagsListItemBindingImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:82-86')
e('DrawerTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DrawerTagsListItemBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:73-77')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DrawerTagsListItemBindingImpl.<clinit>', 'CALL', 'Mapper instantiation loads the Impl class on first inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:284 (printed excerpt); SRC ui/main/drawer/TagsAdapter.java:73-77')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DrawerTagsListItemBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl on DataBindingUtil.inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:284 (printed excerpt); SRC ui/main/drawer/TagsAdapter.java:73-77')
e('DrawerTagsListItemBindingImpl.<init>(DataBindingComponent,View)', 'DrawerTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg ctor delegates to the 3-arg ctor via mapBindings', cls='non_standard', via='generated ctor delegation (bytecode invokespecial)', evidence='INFERRED Generated ctor delegation (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:73-77')
e('DrawerTagsListItemBindingImpl.invalidateAll', 'DrawerTagsListItemBindingImpl.executeBindings', 'CALL', 'Framework rebind runs executeBindings after invalidateAll requests a rebind', cls='non_standard', via='ViewDataBinding requestRebind dispatch (invalidateAll calls requestRebind in bytecode; framework runnable runs executeBindings)', evidence='INFERRED invalidateAll calls requestRebind (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:73-77')
e('drawer.TagsAdapter.onCreateViewHolder', 'DrawerTagsListItemBindingImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/main/drawer/TagsAdapter.java:73-77')
e('DrawerTagsListItemBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DrawerTagsListItemBindingImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/main/drawer/TagsAdapter.java:73-77')
e('FragmentAddTorrentFilesBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentAddTorrentFilesBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/addtorrent/AddTorrentFilesFragment.java:81')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentAddTorrentFilesBindingImpl.<clinit>', 'CALL', 'Mapper instantiation loads the Impl class on first inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:290 (printed excerpt); SRC ui/addtorrent/AddTorrentFilesFragment.java:81')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentAddTorrentFilesBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl on DataBindingUtil.inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:290 (printed excerpt); SRC ui/addtorrent/AddTorrentFilesFragment.java:81')
e('FragmentAddTorrentFilesBindingImpl.<init>(DataBindingComponent,View)', 'FragmentAddTorrentFilesBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg ctor delegates to the 3-arg ctor via mapBindings', cls='non_standard', via='generated ctor delegation (bytecode invokespecial)', evidence='INFERRED Generated ctor delegation (compiled bytecode); SRC ui/addtorrent/AddTorrentFilesFragment.java:81')
e('FragmentAddTorrentFilesBindingImpl.invalidateAll', 'FragmentAddTorrentFilesBindingImpl.executeBindings', 'CALL', 'Framework rebind runs executeBindings after invalidateAll requests a rebind', cls='non_standard', via='ViewDataBinding requestRebind dispatch (invalidateAll calls requestRebind in bytecode; framework runnable runs executeBindings)', evidence='INFERRED invalidateAll calls requestRebind (compiled bytecode); SRC ui/addtorrent/AddTorrentFilesFragment.java:81')
e('AddTorrentFilesFragment.onCreateView', 'FragmentAddTorrentFilesBindingImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/addtorrent/AddTorrentFilesFragment.java:81')
e('FragmentAddTorrentFilesBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentAddTorrentFilesBindingImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/addtorrent/AddTorrentFilesFragment.java:81')
e('FragmentAddTorrentFilesBindingImpl.onFieldChange', 'FragmentAddTorrentFilesBindingImpl.onChangeViewModelInfo', 'CALL', 'Generated onFieldChange lookupswitch dispatches to this onChange handler', cls='non_standard', via='generated field-change dispatch (bytecode lookupswitch)', evidence='INFERRED Field-change dispatch (compiled bytecode); SRC ui/addtorrent/AddTorrentFilesFragment.java:81')

# UNREACHABLE rows (9): kind no_trigger_in_app, INFERRED, per authoritative batch file.
UNREACHABLE.update({
    'DialogSelectTagBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No observable variable is set on this binding in printed host code, so no field-change dispatch fires.',
        'INFERRED host evidence SRC ui/tag/SelectTagDialog.java:128',
        'INFERRED'),
    'DialogSelectTagBindingImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/tag/SelectTagDialog.java:128',
        'INFERRED'),
    'DrawerEmptyTagsListItemBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No observable variable is set on this binding in printed host code, so no field-change dispatch fires.',
        'INFERRED host evidence SRC ui/main/drawer/TagsAdapter.java:64-68',
        'INFERRED'),
    'DrawerEmptyTagsListItemBindingImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/main/drawer/TagsAdapter.java:64-68',
        'INFERRED'),
    'DrawerNoTagsListItemBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No observable variable is set on this binding in printed host code, so no field-change dispatch fires.',
        'INFERRED host evidence SRC ui/main/drawer/TagsAdapter.java:82-86',
        'INFERRED'),
    'DrawerNoTagsListItemBindingImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/main/drawer/TagsAdapter.java:82-86',
        'INFERRED'),
    'DrawerTagsListItemBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No observable variable is set on this binding in printed host code, so no field-change dispatch fires.',
        'INFERRED host evidence SRC ui/main/drawer/TagsAdapter.java:73-77',
        'INFERRED'),
    'DrawerTagsListItemBindingImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/main/drawer/TagsAdapter.java:73-77',
        'INFERRED'),
    'FragmentAddTorrentFilesBinding.getViewModel': ('no_trigger_in_app',
        'No printed binding.getViewModel() call; hosts use their own viewModel field and setViewModel only.',
        'INFERRED host evidence SRC ui/addtorrent/AddTorrentFilesFragment.java:81 (setViewModel at :135); no printed call to this method',
        'INFERRED'),
})

# No SUPPRESS entries: recomputed auto_calls + bytecode scan found no
# REACHABLE caller of any UNREACHABLE method in this batch (see REPORT.md).
SUPPRESS.update(set())
