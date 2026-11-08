# Citation-form rework 2026-11-01: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Converter C09 delivery (2026-11-01): base = audited A3 output helper a3-g12 parts b062.
# Labels, kinds, grades, edges and SUPPRESS are unchanged from the audited base
# (verified by the official harness against the authoritative merge-ready batch file).
# Stronger-evidence rule (step b): all UNREACHABLE keys of this batch were checked
# against the merger tree graph_def.py (read-only); the tree holds none of them, so
# no grade changes; all grades remain as audited.
# Printed evidence: the delivered printed file carries the base printed content plus
# a converter header; the G12 -c key-dispatch excerpts are NOT relied on (auditor
# finding: they repeat ctor-body lines and do not demonstrate dispatch); the -p
# signature blocks and printed source lines are the relied evidence.
# Batch 62 part (DialogAddTagBindingImpl, DialogCreateTorrentBinding, DialogCreateTorrentBindingImpl, DialogErrorBinding, DialogErrorBindingImpl, DialogGoToFolderBinding). Hand-written edges, UNREACHABLE entries and SUPPRESS strings only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b062_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Generated databinding Impl evidence is javap -c -p output: generated Impl source is
# absent from final_java_only, so the printed file carries the javap dump under a
# .java-named header for that class (labelled as javap, not source).

e('DialogAddTagBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddTagBindingImpl$1.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $1',
  evidence='SRC databinding/DialogAddTagBindingImpl.java:javap 3-arg <init> -> DialogAddTagBindingImpl$1 <init>')
e('DialogAddTagBindingImpl.executeBindings', 'DialogAddTagBindingImpl$1.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $1 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogAddTagBindingImpl.java:javap executeBindings -> setListeners')
e('DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogCreateTorrentBinding.<init>', 'CALL', 'Three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap 3-arg <init> -> DialogCreateTorrentBinding <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DialogCreateTorrentBindingImpl.<clinit>', 'FRAMEWORK', 'Databinding mapper instantiation loads the Impl class, running its static initializer',
  evidence='INFERRED databinding mapper class load; SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DialogCreateTorrentBindingImpl 2-arg <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl for its layout id',
  evidence='SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DialogCreateTorrentBindingImpl 2-arg <init>')
e('DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View)', 'DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Two-arg Impl ctor delegates to the three-arg ctor via mapBindings',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap 2-arg <init> -> 3-arg <init>')
e('DialogCreateTorrentBindingImpl.invalidateAll', 'DialogCreateTorrentBindingImpl.executeBindings', 'FRAMEWORK', 'Rebind flow: invalidateAll requests a rebind and the framework runs executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (invalidateAll/requestRebind -> executePendingBindings -> executeBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DialogCreateTorrentBindingImpl.java:javap invalidateAll -> requestRebind')
e('DialogCreateTorrentBindingImpl.invalidateAll', 'DialogCreateTorrentBindingImpl.hasPendingBindings', 'FRAMEWORK', 'Rebind flow: the framework checks hasPendingBindings before running executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (executePendingBindings checks hasPendingBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DialogCreateTorrentBindingImpl.java:javap invalidateAll -> requestRebind')
e('DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogCreateTorrentBindingImpl.invalidateAll', 'CALL', 'Three-arg Impl ctor calls invalidateAll',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap 3-arg <init> -> invalidateAll')
e('DialogCreateTorrentBindingImpl.onFieldChange', 'DialogCreateTorrentBindingImpl.onChangeViewModelBuildProgress', 'CALL', 'onFieldChange dispatches to the onChangeViewModelBuildProgress handler for its field id',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap onFieldChange -> onChangeViewModelBuildProgress')
e('DialogCreateTorrentBindingImpl.onFieldChange', 'DialogCreateTorrentBindingImpl.onChangeViewModelMutableParams', 'CALL', 'onFieldChange dispatches to the onChangeViewModelMutableParams handler for its field id',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap onFieldChange -> onChangeViewModelMutableParams')
e('DialogCreateTorrentBindingImpl.onFieldChange', 'DialogCreateTorrentBindingImpl.onChangeViewModelState', 'CALL', 'onFieldChange dispatches to the onChangeViewModelState handler for its field id',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap onFieldChange -> onChangeViewModelState')
e('DialogCreateTorrentBindingImpl.executeBindings', 'DialogCreateTorrentBindingImpl.onFieldChange', 'FRAMEWORK', 'Observable dispatch: executeBindings registers the observables and a change notifies onFieldChange', cls='non_standard', via='AndroidX databinding observable dispatch (executeBindings updateRegistration -> onFieldChange)',
  evidence='INFERRED databinding observable dispatch; SRC databinding/DialogCreateTorrentBindingImpl.java:javap executeBindings -> updateRegistration')
e('CreateTorrentDialog.onCreateDialog', 'DialogCreateTorrentBindingImpl.setViewModel', 'CALL', 'Create-torrent dialog binds its view model on creation',
  evidence='SRC ui/createtorrent/CreateTorrentDialog.java:172,187')
e('DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogCreateTorrentBindingImpl$1.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $1',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap 3-arg <init> -> DialogCreateTorrentBindingImpl$1 <init>')
e('DialogCreateTorrentBindingImpl.executeBindings', 'DialogCreateTorrentBindingImpl$1.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $1 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogCreateTorrentBindingImpl.java:javap executeBindings -> setListeners')
e('DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogCreateTorrentBindingImpl$2.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $2',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap 3-arg <init> -> DialogCreateTorrentBindingImpl$2 <init>')
e('DialogCreateTorrentBindingImpl.executeBindings', 'DialogCreateTorrentBindingImpl$2.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $2 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogCreateTorrentBindingImpl.java:javap executeBindings -> setListeners')
e('DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogCreateTorrentBindingImpl$3.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $3',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap 3-arg <init> -> DialogCreateTorrentBindingImpl$3 <init>')
e('DialogCreateTorrentBindingImpl.executeBindings', 'DialogCreateTorrentBindingImpl$3.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $3 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogCreateTorrentBindingImpl.java:javap executeBindings -> setListeners')
e('DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogCreateTorrentBindingImpl$4.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $4',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap 3-arg <init> -> DialogCreateTorrentBindingImpl$4 <init>')
e('DialogCreateTorrentBindingImpl.executeBindings', 'DialogCreateTorrentBindingImpl$4.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $4 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogCreateTorrentBindingImpl.java:javap executeBindings -> setListeners')
e('DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogCreateTorrentBindingImpl$5.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $5',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap 3-arg <init> -> DialogCreateTorrentBindingImpl$5 <init>')
e('DialogCreateTorrentBindingImpl.executeBindings', 'DialogCreateTorrentBindingImpl$5.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $5 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogCreateTorrentBindingImpl.java:javap executeBindings -> setListeners')
e('DialogCreateTorrentBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogCreateTorrentBindingImpl$6.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $6',
  evidence='SRC databinding/DialogCreateTorrentBindingImpl.java:javap 3-arg <init> -> DialogCreateTorrentBindingImpl$6 <init>')
e('DialogCreateTorrentBindingImpl.executeBindings', 'DialogCreateTorrentBindingImpl$6.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $6 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogCreateTorrentBindingImpl.java:javap executeBindings -> setListeners')
e('DialogErrorBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogErrorBinding.<init>', 'CALL', 'Three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/DialogErrorBindingImpl.java:javap 3-arg <init> -> DialogErrorBinding <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DialogErrorBindingImpl.<clinit>', 'FRAMEWORK', 'Databinding mapper instantiation loads the Impl class, running its static initializer',
  evidence='INFERRED databinding mapper class load; SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DialogErrorBindingImpl 2-arg <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DialogErrorBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl for its layout id',
  evidence='SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DialogErrorBindingImpl 2-arg <init>')
e('DialogErrorBindingImpl.<init>(DataBindingComponent,View)', 'DialogErrorBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Two-arg Impl ctor delegates to the three-arg ctor via mapBindings',
  evidence='SRC databinding/DialogErrorBindingImpl.java:javap 2-arg <init> -> 3-arg <init>')
e('DialogErrorBindingImpl.invalidateAll', 'DialogErrorBindingImpl.executeBindings', 'FRAMEWORK', 'Rebind flow: invalidateAll requests a rebind and the framework runs executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (invalidateAll/requestRebind -> executePendingBindings -> executeBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DialogErrorBindingImpl.java:javap invalidateAll -> requestRebind')
e('DialogErrorBindingImpl.invalidateAll', 'DialogErrorBindingImpl.hasPendingBindings', 'FRAMEWORK', 'Rebind flow: the framework checks hasPendingBindings before running executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (executePendingBindings checks hasPendingBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DialogErrorBindingImpl.java:javap invalidateAll -> requestRebind')
e('DialogErrorBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogErrorBindingImpl.invalidateAll', 'CALL', 'Three-arg Impl ctor calls invalidateAll',
  evidence='SRC databinding/DialogErrorBindingImpl.java:javap 3-arg <init> -> invalidateAll')
e('ErrorReportDialog.onCreateDialog', 'DialogErrorBindingImpl.setDetailError', 'CALL', 'Error dialog binds its detail error on creation',
  evidence='SRC ui/errorreport/ErrorReportDialog.java:56,69')
e('DialogGoToFolderBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogGoToFolderBinding.<init>', 'CALL', 'Three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/DialogGoToFolderBindingImpl.java:javap 3-arg <init> -> DialogGoToFolderBinding <init>')

# UNREACHABLE rows: no bytecode caller in auto_calls.json and no printed app trigger
# (recomputed for this batch; see REPORT.md). Labels, kinds and grades are copied
# unchanged from the authoritative merge-ready batch file.
UNREACHABLE.update({
    'DialogCreateTorrentBinding.getViewModel': ('no_trigger_in_app',
        'CreateTorrentDialog uses binding.setViewModel only, never getViewModel; generated executeBindings reads the mViewModel field directly.',
        'SRC ui/createtorrent/CreateTorrentDialog.java:172,187',
        'INFERRED'),
    'DialogCreateTorrentBindingImpl.setVariable': ('no_trigger_in_app',
        'No printed setVariable call site for this Impl; the view model is set through the typed setViewModel setter instead.',
        'SRC ui/createtorrent/CreateTorrentDialog.java:172,187',
        'INFERRED'),
    'DialogErrorBinding.getDetailError': ('no_trigger_in_app',
        'ErrorReportDialog sets detailError through the typed setter; generated executeBindings reads the field, not the getter; no printed getter call.',
        'SRC ui/errorreport/ErrorReportDialog.java:56,69',
        'INFERRED'),
    'DialogErrorBindingImpl.onFieldChange': ('no_trigger_in_app',
        'detailError is a plain String, not an observable, so no observable registration exists for onFieldChange to fire on.',
        'SRC ui/errorreport/ErrorReportDialog.java:56,69',
        'INFERRED'),
    'DialogErrorBindingImpl.setVariable': ('no_trigger_in_app',
        'No printed setVariable call site for this Impl; the detail error is set through the typed setDetailError setter instead.',
        'SRC ui/errorreport/ErrorReportDialog.java:56,69',
        'INFERRED'),
})

# SUPPRESS: no intra-group REACHABLE -> UNREACHABLE bytecode edge exists for this
# batch (recomputed from auto_calls.json + bytecode scan; cross-group candidates are
# listed in REPORT.md for merger reconciliation, not suppressed here).
SUPPRESS.update(set())
