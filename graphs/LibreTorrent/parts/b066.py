# Citation-form rework 2026-11-01: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# C10 converter note 2026-11-01: edge evidence strings that began with a bare description
# (e.g. 'Generated ctor tail (compiled bytecode); ...') are prefixed 'INFERRED ' so the
# build's evidence-label rule (first token must be SRC/FW-SRC/INFERRED/...) passes;
# bytecode-derived edges are INFERRED evidence. No label, edge, endpoint, or citation changed.
# Batch 66 part (generated data-binding Impl methods: see .md for the Impl groups).
# Edge plan designed per method kind (mapper, ctor chain, rebind, listener,
# field-change) and assembled by scratch/gen_parts.py from the verified
# row/build-name tables; no edge is copied from graph_def.py. Every edge
# endpoint is an exact build name
# (tools/build_graph.py method_names over method_list.json, 4,732 names).
# Generated *BindingImpl source is absent from final_java_only; internal
# generated dispatch is confirmed in the compiled bytecode (javap -c -p)
# and in merger-tree auto_calls.json; each evidence string cites lines
# printed in scratch/b066_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.

e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentDetailTorrentBindingImpl.<clinit>', 'CALL', 'Mapper instantiation loads the Impl class on first inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:308 (printed excerpt); SRC ui/detailtorrent/DetailTorrentFragment.java:150')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentDetailTorrentBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl on DataBindingUtil.inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:308 (printed excerpt); SRC ui/detailtorrent/DetailTorrentFragment.java:150')
e('FragmentDetailTorrentBindingImpl.<init>(DataBindingComponent,View)', 'FragmentDetailTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg ctor delegates to the 3-arg ctor via mapBindings', cls='non_standard', via='generated ctor delegation (bytecode invokespecial)', evidence='INFERRED Generated ctor delegation (compiled bytecode); SRC ui/detailtorrent/DetailTorrentFragment.java:150')
e('FragmentDetailTorrentBindingImpl.invalidateAll', 'FragmentDetailTorrentBindingImpl.executeBindings', 'CALL', 'Framework rebind runs executeBindings after invalidateAll requests a rebind', cls='non_standard', via='ViewDataBinding requestRebind dispatch (invalidateAll calls requestRebind in bytecode; framework runnable runs executeBindings)', evidence='INFERRED invalidateAll calls requestRebind (compiled bytecode); SRC ui/detailtorrent/DetailTorrentFragment.java:150')
e('DetailTorrentFragment.onCreateView', 'FragmentDetailTorrentBindingImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/detailtorrent/DetailTorrentFragment.java:150')
e('FragmentDetailTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentDetailTorrentBindingImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/detailtorrent/DetailTorrentFragment.java:150')
e('FragmentDetailTorrentFilesBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentDetailTorrentFilesBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentDetailTorrentFilesBindingImpl.<clinit>', 'CALL', 'Mapper instantiation loads the Impl class on first inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:314 (printed excerpt); SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentDetailTorrentFilesBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl on DataBindingUtil.inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:314 (printed excerpt); SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114')
e('FragmentDetailTorrentFilesBindingImpl.<init>(DataBindingComponent,View)', 'FragmentDetailTorrentFilesBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg ctor delegates to the 3-arg ctor via mapBindings', cls='non_standard', via='generated ctor delegation (bytecode invokespecial)', evidence='INFERRED Generated ctor delegation (compiled bytecode); SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114')
e('FragmentDetailTorrentFilesBindingImpl.invalidateAll', 'FragmentDetailTorrentFilesBindingImpl.executeBindings', 'CALL', 'Framework rebind runs executeBindings after invalidateAll requests a rebind', cls='non_standard', via='ViewDataBinding requestRebind dispatch (invalidateAll calls requestRebind in bytecode; framework runnable runs executeBindings)', evidence='INFERRED invalidateAll calls requestRebind (compiled bytecode); SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114')
e('DetailTorrentFilesFragment.onCreateView', 'FragmentDetailTorrentFilesBindingImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114')
e('FragmentDetailTorrentFilesBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentDetailTorrentFilesBindingImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114')
e('FragmentDetailTorrentFilesBindingImpl.onFieldChange', 'FragmentDetailTorrentFilesBindingImpl.onChangeViewModelInfo', 'CALL', 'Generated onFieldChange lookupswitch dispatches to this onChange handler', cls='non_standard', via='generated field-change dispatch (bytecode lookupswitch)', evidence='INFERRED Field-change dispatch (compiled bytecode); SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114')
e('FragmentDetailTorrentFilesBindingImpl.executeBindings', 'FragmentDetailTorrentFilesBindingImpl.onFieldChange', 'CALL', 'Observable notify dispatches to onFieldChange after executeBindings registers the observables', cls='non_standard', via='executeBindings updateRegistration + framework WeakListener dispatch (updateRegistration in executeBindings bytecode)', evidence='INFERRED updateRegistration in executeBindings (compiled bytecode); SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114')
e('DetailTorrentFilesFragment.onViewCreated', 'FragmentDetailTorrentFilesBindingImpl.setViewModel', 'CALL', 'Host sets the viewModel on the binding', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:201')
e('FragmentDetailTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentDetailTorrentInfoBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentDetailTorrentInfoBindingImpl.<clinit>', 'CALL', 'Mapper instantiation loads the Impl class on first inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:320 (printed excerpt); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentDetailTorrentInfoBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl on DataBindingUtil.inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:320 (printed excerpt); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('FragmentDetailTorrentInfoBindingImpl.<init>(DataBindingComponent,View)', 'FragmentDetailTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg ctor delegates to the 3-arg ctor via mapBindings', cls='non_standard', via='generated ctor delegation (bytecode invokespecial)', evidence='INFERRED Generated ctor delegation (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('FragmentDetailTorrentInfoBindingImpl.invalidateAll', 'FragmentDetailTorrentInfoBindingImpl.executeBindings', 'CALL', 'Framework rebind runs executeBindings after invalidateAll requests a rebind', cls='non_standard', via='ViewDataBinding requestRebind dispatch (invalidateAll calls requestRebind in bytecode; framework runnable runs executeBindings)', evidence='INFERRED invalidateAll calls requestRebind (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('DetailTorrentInfoFragment.onCreateView', 'FragmentDetailTorrentInfoBindingImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('FragmentDetailTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentDetailTorrentInfoBindingImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('FragmentDetailTorrentInfoBindingImpl.onFieldChange', 'FragmentDetailTorrentInfoBindingImpl.onChangeViewModelInfo', 'CALL', 'Generated onFieldChange lookupswitch dispatches to this onChange handler', cls='non_standard', via='generated field-change dispatch (bytecode lookupswitch)', evidence='INFERRED Field-change dispatch (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('FragmentDetailTorrentInfoBindingImpl.onFieldChange', 'FragmentDetailTorrentInfoBindingImpl.onChangeViewModelMutableParams', 'CALL', 'Generated onFieldChange lookupswitch dispatches to this onChange handler', cls='non_standard', via='generated field-change dispatch (bytecode lookupswitch)', evidence='INFERRED Field-change dispatch (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('FragmentDetailTorrentInfoBindingImpl.executeBindings', 'FragmentDetailTorrentInfoBindingImpl.onFieldChange', 'CALL', 'Observable notify dispatches to onFieldChange after executeBindings registers the observables', cls='non_standard', via='executeBindings updateRegistration + framework WeakListener dispatch (updateRegistration in executeBindings bytecode)', evidence='INFERRED updateRegistration in executeBindings (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('DetailTorrentInfoFragment.onCreateView', 'FragmentDetailTorrentInfoBindingImpl.setViewModel', 'CALL', 'Host sets the viewModel on the binding', cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:105')
e('FragmentDetailTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentDetailTorrentInfoBindingImpl$1.<init>', 'CALL', 'Generated Impl 3-arg ctor creates the $1 InverseBindingListener', cls='non_standard', via='generated listener creation (bytecode invokespecial)', evidence='INFERRED Listener creation (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('FragmentDetailTorrentInfoBindingImpl.executeBindings', 'FragmentDetailTorrentInfoBindingImpl$1.onChange', 'CALL', 'View change events invoke the $1 InverseBindingListener attached by executeBindings', cls='non_standard', via='two-way binding listener dispatch (executeBindings attaches the listener; view events invoke onChange)', evidence='INFERRED Listener attached in executeBindings (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('FragmentDetailTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentDetailTorrentInfoBindingImpl$2.<init>', 'CALL', 'Generated Impl 3-arg ctor creates the $2 InverseBindingListener', cls='non_standard', via='generated listener creation (bytecode invokespecial)', evidence='INFERRED Listener creation (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('FragmentDetailTorrentInfoBindingImpl.executeBindings', 'FragmentDetailTorrentInfoBindingImpl$2.onChange', 'CALL', 'View change events invoke the $2 InverseBindingListener attached by executeBindings', cls='non_standard', via='two-way binding listener dispatch (executeBindings attaches the listener; view events invoke onChange)', evidence='INFERRED Listener attached in executeBindings (compiled bytecode); SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100')
e('FragmentDetailTorrentPeerListBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentDetailTorrentPeerListBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:84')

# UNREACHABLE rows (8): kind no_trigger_in_app, INFERRED, per authoritative batch file.
UNREACHABLE.update({
    'FragmentDetailTorrentBindingImpl.onChangeAppbar': ('no_trigger_in_app',
        'No appbar variable is set on this binding in printed host code (layout declares no variable), so no appbar change fires.',
        'INFERRED host evidence SRC ui/detailtorrent/DetailTorrentFragment.java:150',
        'INFERRED'),
    'FragmentDetailTorrentBindingImpl.onFieldChange': ('no_trigger_in_app',
        'No observable variable is set on this binding in printed host code, so no field-change dispatch fires.',
        'INFERRED host evidence SRC ui/detailtorrent/DetailTorrentFragment.java:150',
        'INFERRED'),
    'FragmentDetailTorrentBindingImpl.setLifecycleOwner': ('no_trigger_in_app',
        'No app code calls setLifecycleOwner on this binding; the single tree-wide setLifecycleOwner call targets DialogCreateTorrentBinding, not this binding.',
        'INFERRED host evidence SRC ui/detailtorrent/DetailTorrentFragment.java:150',
        'INFERRED'),
    'FragmentDetailTorrentBindingImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/detailtorrent/DetailTorrentFragment.java:150',
        'INFERRED'),
    'FragmentDetailTorrentFilesBinding.getViewModel': ('no_trigger_in_app',
        'No printed binding.getViewModel() call; hosts use their own viewModel field and setViewModel only.',
        'INFERRED host evidence SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114 (setViewModel at :201); no printed call to this method',
        'INFERRED'),
    'FragmentDetailTorrentFilesBindingImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:114 (setViewModel at :201); no printed call to this method',
        'INFERRED'),
    'FragmentDetailTorrentInfoBinding.getViewModel': ('no_trigger_in_app',
        'No printed binding.getViewModel() call; hosts use their own viewModel field and setViewModel only.',
        'INFERRED host evidence SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100 (setViewModel at :105); no printed call to this method',
        'INFERRED'),
    'FragmentDetailTorrentInfoBindingImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100 (setViewModel at :105); no printed call to this method',
        'INFERRED'),
})

# SUPPRESS: one entry (see below); the base scan found no REACHABLE caller, but pre-test
# showed one auto edge into UNREACHABLE onChangeAppbar from UNREACHABLE onFieldChange.
# C10: suppress the bytecode auto edge into UNREACHABLE onChangeAppbar
# (auto edge E634fc6ed in pre-test: onFieldChange -> onChangeAppbar, where the
# caller onFieldChange is itself UNREACHABLE in this batch, so no route is lost;
# without this the build warns 'UNREACHABLE but has incoming edges').
SUPPRESS.update({'FragmentDetailTorrentBindingImpl.onChangeAppbar'})
