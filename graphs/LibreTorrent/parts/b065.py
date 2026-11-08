# Citation-form rework 2026-11-01: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# C10 converter note 2026-11-01: edge evidence strings that began with a bare description
# (e.g. 'Generated ctor tail (compiled bytecode); ...') are prefixed 'INFERRED ' so the
# build's evidence-label rule (first token must be SRC/FW-SRC/INFERRED/...) passes;
# bytecode-derived edges are INFERRED evidence. No label, edge, endpoint, or citation changed.
# Batch 65 part (generated data-binding Impl methods: see .md for the Impl groups).
# Edge plan designed per method kind (mapper, ctor chain, rebind, listener,
# field-change) and assembled by scratch/gen_parts.py from the verified
# row/build-name tables; no edge is copied from graph_def.py. Every edge
# endpoint is an exact build name
# (tools/build_graph.py method_names over method_list.json, 4,732 names).
# Generated *BindingImpl source is absent from final_java_only; internal
# generated dispatch is confirmed in the compiled bytecode (javap -c -p)
# and in merger-tree auto_calls.json; each evidence string cites lines
# printed in scratch/b065_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.

e('FragmentAddTorrentFilesBindingImpl.onFieldChange', 'FragmentAddTorrentFilesBindingImpl.onChangeViewModelMutableParams', 'CALL', 'Generated onFieldChange lookupswitch dispatches to this onChange handler', cls='non_standard', via='generated field-change dispatch (bytecode lookupswitch)', evidence='INFERRED Field-change dispatch (compiled bytecode); SRC ui/addtorrent/AddTorrentFilesFragment.java:81')
e('FragmentAddTorrentFilesBindingImpl.executeBindings', 'FragmentAddTorrentFilesBindingImpl.onFieldChange', 'CALL', 'Observable notify dispatches to onFieldChange after executeBindings registers the observables', cls='non_standard', via='executeBindings updateRegistration + framework WeakListener dispatch (updateRegistration in executeBindings bytecode)', evidence='INFERRED updateRegistration in executeBindings (compiled bytecode); SRC ui/addtorrent/AddTorrentFilesFragment.java:81')
e('AddTorrentFilesFragment.onViewCreated', 'FragmentAddTorrentFilesBindingImpl.setViewModel', 'CALL', 'Host sets the viewModel on the binding', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentFilesFragment.java:135')
e('FragmentAddTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentAddTorrentInfoBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentAddTorrentInfoBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingSw600dpLandImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentAddTorrentInfoBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentAddTorrentInfoBindingImpl.<clinit>', 'CALL', 'Mapper instantiation loads the Impl class on first inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:299 (printed excerpt); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentAddTorrentInfoBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl on DataBindingUtil.inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:299 (printed excerpt); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingImpl.<init>(DataBindingComponent,View)', 'FragmentAddTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg ctor delegates to the 3-arg ctor via mapBindings', cls='non_standard', via='generated ctor delegation (bytecode invokespecial)', evidence='INFERRED Generated ctor delegation (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingImpl.invalidateAll', 'FragmentAddTorrentInfoBindingImpl.executeBindings', 'CALL', 'Framework rebind runs executeBindings after invalidateAll requests a rebind', cls='non_standard', via='ViewDataBinding requestRebind dispatch (invalidateAll calls requestRebind in bytecode; framework runnable runs executeBindings)', evidence='INFERRED invalidateAll calls requestRebind (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('AddTorrentInfoFragment.onCreateView', 'FragmentAddTorrentInfoBindingImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentAddTorrentInfoBindingImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingImpl.onFieldChange', 'FragmentAddTorrentInfoBindingImpl.onChangeInfo', 'CALL', 'Generated onFieldChange lookupswitch dispatches to this onChange handler', cls='non_standard', via='generated field-change dispatch (bytecode lookupswitch)', evidence='INFERRED Field-change dispatch (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingImpl.executeBindings', 'FragmentAddTorrentInfoBindingImpl.onFieldChange', 'CALL', 'Observable notify dispatches to onFieldChange after executeBindings registers the observables', cls='non_standard', via='executeBindings updateRegistration + framework WeakListener dispatch (updateRegistration in executeBindings bytecode)', evidence='INFERRED updateRegistration in executeBindings (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('AddTorrentInfoFragment.onViewCreated', 'FragmentAddTorrentInfoBindingImpl.setViewModel', 'CALL', 'Host sets the viewModel on the binding', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:103')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.<clinit>', 'CALL', 'Mapper instantiation loads the Impl class on first inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:302 (printed excerpt); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl on DataBindingUtil.inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:302 (printed excerpt); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View)', 'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg ctor delegates to the 3-arg ctor via mapBindings', cls='non_standard', via='generated ctor delegation (bytecode invokespecial)', evidence='INFERRED Generated ctor delegation (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingLargeLandNotouchImpl.invalidateAll', 'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.executeBindings', 'CALL', 'Framework rebind runs executeBindings after invalidateAll requests a rebind', cls='non_standard', via='ViewDataBinding requestRebind dispatch (invalidateAll calls requestRebind in bytecode; framework runnable runs executeBindings)', evidence='INFERRED invalidateAll calls requestRebind (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('AddTorrentInfoFragment.onCreateView', 'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingLargeLandNotouchImpl.onFieldChange', 'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.onChangeInfo', 'CALL', 'Generated onFieldChange lookupswitch dispatches to this onChange handler', cls='non_standard', via='generated field-change dispatch (bytecode lookupswitch)', evidence='INFERRED Field-change dispatch (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingLargeLandNotouchImpl.executeBindings', 'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.onFieldChange', 'CALL', 'Observable notify dispatches to onFieldChange after executeBindings registers the observables', cls='non_standard', via='executeBindings updateRegistration + framework WeakListener dispatch (updateRegistration in executeBindings bytecode)', evidence='INFERRED updateRegistration in executeBindings (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('AddTorrentInfoFragment.onViewCreated', 'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.setViewModel', 'CALL', 'Host sets the viewModel on the binding', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:103')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentAddTorrentInfoBindingSw600dpLandImpl.<clinit>', 'CALL', 'Mapper instantiation loads the Impl class on first inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:296 (printed excerpt); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'FragmentAddTorrentInfoBindingSw600dpLandImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl on DataBindingUtil.inflate', cls='explicit', evidence='INFERRED DataBinderMapperImpl.getDataBinder dispatch, auto_calls DataBinderMapperImpl.java:296 (printed excerpt); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingSw600dpLandImpl.<init>(DataBindingComponent,View)', 'FragmentAddTorrentInfoBindingSw600dpLandImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Generated 2-arg ctor delegates to the 3-arg ctor via mapBindings', cls='non_standard', via='generated ctor delegation (bytecode invokespecial)', evidence='INFERRED Generated ctor delegation (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingSw600dpLandImpl.invalidateAll', 'FragmentAddTorrentInfoBindingSw600dpLandImpl.executeBindings', 'CALL', 'Framework rebind runs executeBindings after invalidateAll requests a rebind', cls='non_standard', via='ViewDataBinding requestRebind dispatch (invalidateAll calls requestRebind in bytecode; framework runnable runs executeBindings)', evidence='INFERRED invalidateAll calls requestRebind (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('AddTorrentInfoFragment.onCreateView', 'FragmentAddTorrentInfoBindingSw600dpLandImpl.hasPendingBindings', 'CALL', 'DataBinding framework rebind-status poll after inflate', cls='non_standard', via='framework rebind-status poll (query API; no app bytecode caller)', evidence='INFERRED framework poll; SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingSw600dpLandImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentAddTorrentInfoBindingSw600dpLandImpl.invalidateAll', 'CALL', 'Generated Impl 3-arg ctor ends with invalidateAll()', cls='non_standard', via='generated ctor tail (bytecode invokevirtual)', evidence='INFERRED Generated ctor tail (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingSw600dpLandImpl.onFieldChange', 'FragmentAddTorrentInfoBindingSw600dpLandImpl.onChangeInfo', 'CALL', 'Generated onFieldChange lookupswitch dispatches to this onChange handler', cls='non_standard', via='generated field-change dispatch (bytecode lookupswitch)', evidence='INFERRED Field-change dispatch (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('FragmentAddTorrentInfoBindingSw600dpLandImpl.executeBindings', 'FragmentAddTorrentInfoBindingSw600dpLandImpl.onFieldChange', 'CALL', 'Observable notify dispatches to onFieldChange after executeBindings registers the observables', cls='non_standard', via='executeBindings updateRegistration + framework WeakListener dispatch (updateRegistration in executeBindings bytecode)', evidence='INFERRED updateRegistration in executeBindings (compiled bytecode); SRC ui/addtorrent/AddTorrentInfoFragment.java:93')
e('AddTorrentInfoFragment.onViewCreated', 'FragmentAddTorrentInfoBindingSw600dpLandImpl.setViewModel', 'CALL', 'Host sets the viewModel on the binding', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:103')
e('FragmentDetailTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'FragmentDetailTorrentBinding.<init>', 'CALL', 'Generated Impl 3-arg ctor super-call to the base Binding ctor', cls='non_standard', via='generated super-call (bytecode invokespecial)', evidence='INFERRED Generated super-call (compiled bytecode); SRC ui/detailtorrent/DetailTorrentFragment.java:150')

# UNREACHABLE rows (8): kind no_trigger_in_app, INFERRED, per authoritative batch file.
UNREACHABLE.update({
    'FragmentAddTorrentFilesBindingImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/addtorrent/AddTorrentFilesFragment.java:81 (setViewModel at :135); no printed call to this method',
        'INFERRED'),
    'FragmentAddTorrentInfoBinding.getViewModel': ('no_trigger_in_app',
        'No printed binding.getViewModel() call; hosts use their own viewModel field and setViewModel only.',
        'INFERRED host evidence SRC ui/addtorrent/AddTorrentInfoFragment.java:93 (setViewModel at :103); no printed call to this method',
        'INFERRED'),
    'FragmentAddTorrentInfoBindingImpl.setLifecycleOwner': ('no_trigger_in_app',
        'No app code calls setLifecycleOwner on this binding; the single tree-wide setLifecycleOwner call targets DialogCreateTorrentBinding, not this binding.',
        'INFERRED host evidence SRC ui/addtorrent/AddTorrentInfoFragment.java:93 (setViewModel at :103); no printed call to this method',
        'INFERRED'),
    'FragmentAddTorrentInfoBindingImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/addtorrent/AddTorrentInfoFragment.java:93 (setViewModel at :103); no printed call to this method',
        'INFERRED'),
    'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.setLifecycleOwner': ('no_trigger_in_app',
        'No app code calls setLifecycleOwner on this binding; the single tree-wide setLifecycleOwner call targets DialogCreateTorrentBinding, not this binding.',
        'INFERRED host evidence SRC ui/addtorrent/AddTorrentInfoFragment.java:93 (setViewModel at :103); no printed call to this method',
        'INFERRED'),
    'FragmentAddTorrentInfoBindingLargeLandNotouchImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/addtorrent/AddTorrentInfoFragment.java:93 (setViewModel at :103); no printed call to this method',
        'INFERRED'),
    'FragmentAddTorrentInfoBindingSw600dpLandImpl.setLifecycleOwner': ('no_trigger_in_app',
        'No app code calls setLifecycleOwner on this binding; the single tree-wide setLifecycleOwner call targets DialogCreateTorrentBinding, not this binding.',
        'INFERRED host evidence SRC ui/addtorrent/AddTorrentInfoFragment.java:93 (setViewModel at :103); no printed call to this method',
        'INFERRED'),
    'FragmentAddTorrentInfoBindingSw600dpLandImpl.setVariable': ('no_trigger_in_app',
        'App code calls the typed setViewModel, never setVariable; no printed setVariable call.',
        'INFERRED host evidence SRC ui/addtorrent/AddTorrentInfoFragment.java:93 (setViewModel at :103); no printed call to this method',
        'INFERRED'),
})

# No SUPPRESS entries: recomputed auto_calls + bytecode scan found no
# REACHABLE caller of any UNREACHABLE method in this batch (see REPORT.md).
SUPPRESS.update(set())
