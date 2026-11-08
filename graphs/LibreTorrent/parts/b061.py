# Citation-form rework 2026-11-01: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Converter C09 delivery (2026-11-01): base = audited A3 output helper a3-g12 parts b061.
# Labels, kinds, grades, edges and SUPPRESS are unchanged from the audited base
# (verified by the official harness against the authoritative merge-ready batch file).
# Stronger-evidence rule (step b): all UNREACHABLE keys of this batch were checked
# against the merger tree graph_def.py (read-only); the tree holds none of them, so
# no grade changes; all grades remain as audited.
# Printed evidence: the delivered printed file carries the base printed content plus
# a converter header; the G12 -c key-dispatch excerpts are NOT relied on (auditor
# finding: they repeat ctor-body lines and do not demonstrate dispatch); the -p
# signature blocks and printed source lines are the relied evidence.
# Batch 61 part (DialogAddFeedChannelBindingImpl, DialogAddLinkBinding, DialogAddLinkBindingImpl, DialogAddTagBinding, DialogAddTagBindingImpl). Hand-written edges, UNREACHABLE entries and SUPPRESS strings only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b061_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Generated databinding Impl evidence is javap -c -p output: generated Impl source is
# absent from final_java_only, so the printed file carries the javap dump under a
# .java-named header for that class (labelled as javap, not source).

e('AddFeedDialog.onCreateDialog', 'DialogAddFeedChannelBindingImpl.setViewModel', 'CALL', 'Add-feed dialog binds its view model on creation',
  evidence='SRC ui/addfeed/AddFeedDialog.java:180,203')
e('DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddFeedChannelBindingImpl$1.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $1',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap 3-arg <init> -> DialogAddFeedChannelBindingImpl$1 <init>')
e('DialogAddFeedChannelBindingImpl.executeBindings', 'DialogAddFeedChannelBindingImpl$1.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $1 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogAddFeedChannelBindingImpl.java:javap executeBindings -> setListeners')
e('DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddFeedChannelBindingImpl$2.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $2',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap 3-arg <init> -> DialogAddFeedChannelBindingImpl$2 <init>')
e('DialogAddFeedChannelBindingImpl.executeBindings', 'DialogAddFeedChannelBindingImpl$2.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $2 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogAddFeedChannelBindingImpl.java:javap executeBindings -> setListeners')
e('DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddFeedChannelBindingImpl$3.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $3',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap 3-arg <init> -> DialogAddFeedChannelBindingImpl$3 <init>')
e('DialogAddFeedChannelBindingImpl.executeBindings', 'DialogAddFeedChannelBindingImpl$3.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $3 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogAddFeedChannelBindingImpl.java:javap executeBindings -> setListeners')
e('DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddFeedChannelBindingImpl$4.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $4',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap 3-arg <init> -> DialogAddFeedChannelBindingImpl$4 <init>')
e('DialogAddFeedChannelBindingImpl.executeBindings', 'DialogAddFeedChannelBindingImpl$4.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $4 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogAddFeedChannelBindingImpl.java:javap executeBindings -> setListeners')
e('DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddFeedChannelBindingImpl$5.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $5',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap 3-arg <init> -> DialogAddFeedChannelBindingImpl$5 <init>')
e('DialogAddFeedChannelBindingImpl.executeBindings', 'DialogAddFeedChannelBindingImpl$5.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $5 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogAddFeedChannelBindingImpl.java:javap executeBindings -> setListeners')
e('DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddFeedChannelBindingImpl$6.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $6',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap 3-arg <init> -> DialogAddFeedChannelBindingImpl$6 <init>')
e('DialogAddFeedChannelBindingImpl.executeBindings', 'DialogAddFeedChannelBindingImpl$6.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $6 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogAddFeedChannelBindingImpl.java:javap executeBindings -> setListeners')
e('DialogAddLinkBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddLinkBinding.<init>', 'CALL', 'Three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/DialogAddLinkBindingImpl.java:javap 3-arg <init> -> DialogAddLinkBinding <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DialogAddLinkBindingImpl.<clinit>', 'FRAMEWORK', 'Databinding mapper instantiation loads the Impl class, running its static initializer',
  evidence='INFERRED databinding mapper class load; SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DialogAddLinkBindingImpl 2-arg <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DialogAddLinkBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl for its layout id',
  evidence='SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DialogAddLinkBindingImpl 2-arg <init>')
e('DialogAddLinkBindingImpl.<init>(DataBindingComponent,View)', 'DialogAddLinkBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Two-arg Impl ctor delegates to the three-arg ctor via mapBindings',
  evidence='SRC databinding/DialogAddLinkBindingImpl.java:javap 2-arg <init> -> 3-arg <init>')
e('DialogAddLinkBindingImpl.invalidateAll', 'DialogAddLinkBindingImpl.executeBindings', 'FRAMEWORK', 'Rebind flow: invalidateAll requests a rebind and the framework runs executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (invalidateAll/requestRebind -> executePendingBindings -> executeBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DialogAddLinkBindingImpl.java:javap invalidateAll -> requestRebind')
e('DialogAddLinkBindingImpl.invalidateAll', 'DialogAddLinkBindingImpl.hasPendingBindings', 'FRAMEWORK', 'Rebind flow: the framework checks hasPendingBindings before running executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (executePendingBindings checks hasPendingBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DialogAddLinkBindingImpl.java:javap invalidateAll -> requestRebind')
e('DialogAddLinkBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddLinkBindingImpl.invalidateAll', 'CALL', 'Three-arg Impl ctor calls invalidateAll',
  evidence='SRC databinding/DialogAddLinkBindingImpl.java:javap 3-arg <init> -> invalidateAll')
e('DialogAddLinkBindingImpl.onFieldChange', 'DialogAddLinkBindingImpl.onChangeViewModelLink', 'CALL', 'onFieldChange dispatches to the onChangeViewModelLink handler for its field id',
  evidence='SRC databinding/DialogAddLinkBindingImpl.java:javap onFieldChange -> onChangeViewModelLink')
e('DialogAddLinkBindingImpl.onFieldChange', 'DialogAddLinkBindingImpl.onChangeViewModelShowClipboardButton', 'CALL', 'onFieldChange dispatches to the onChangeViewModelShowClipboardButton handler for its field id',
  evidence='SRC databinding/DialogAddLinkBindingImpl.java:javap onFieldChange -> onChangeViewModelShowClipboardButton')
e('DialogAddLinkBindingImpl.executeBindings', 'DialogAddLinkBindingImpl.onFieldChange', 'FRAMEWORK', 'Observable dispatch: executeBindings registers the observables and a change notifies onFieldChange', cls='non_standard', via='AndroidX databinding observable dispatch (executeBindings updateRegistration -> onFieldChange)',
  evidence='INFERRED databinding observable dispatch; SRC databinding/DialogAddLinkBindingImpl.java:javap executeBindings -> updateRegistration')
e('AddLinkDialog.onCreateDialog', 'DialogAddLinkBindingImpl.setViewModel', 'CALL', 'Add-link dialog binds its view model on creation',
  evidence='SRC ui/addlink/AddLinkDialog.java:171,185')
e('DialogAddLinkBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddLinkBindingImpl$1.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $1',
  evidence='SRC databinding/DialogAddLinkBindingImpl.java:javap 3-arg <init> -> DialogAddLinkBindingImpl$1 <init>')
e('DialogAddLinkBindingImpl.executeBindings', 'DialogAddLinkBindingImpl$1.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $1 listener on its widget and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/DialogAddLinkBindingImpl.java:javap executeBindings -> setListeners')
e('DialogAddTagBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddTagBinding.<init>', 'CALL', 'Three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/DialogAddTagBindingImpl.java:javap 3-arg <init> -> DialogAddTagBinding <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DialogAddTagBindingImpl.<clinit>', 'FRAMEWORK', 'Databinding mapper instantiation loads the Impl class, running its static initializer',
  evidence='INFERRED databinding mapper class load; SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DialogAddTagBindingImpl 2-arg <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DialogAddTagBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl for its layout id',
  evidence='SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DialogAddTagBindingImpl 2-arg <init>')
e('DialogAddTagBindingImpl.<init>(DataBindingComponent,View)', 'DialogAddTagBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Two-arg Impl ctor delegates to the three-arg ctor via mapBindings',
  evidence='SRC databinding/DialogAddTagBindingImpl.java:javap 2-arg <init> -> 3-arg <init>')
e('DialogAddTagBindingImpl.invalidateAll', 'DialogAddTagBindingImpl.executeBindings', 'FRAMEWORK', 'Rebind flow: invalidateAll requests a rebind and the framework runs executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (invalidateAll/requestRebind -> executePendingBindings -> executeBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DialogAddTagBindingImpl.java:javap invalidateAll -> requestRebind')
e('DialogAddTagBindingImpl.invalidateAll', 'DialogAddTagBindingImpl.hasPendingBindings', 'FRAMEWORK', 'Rebind flow: the framework checks hasPendingBindings before running executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (executePendingBindings checks hasPendingBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DialogAddTagBindingImpl.java:javap invalidateAll -> requestRebind')
e('DialogAddTagBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddTagBindingImpl.invalidateAll', 'CALL', 'Three-arg Impl ctor calls invalidateAll',
  evidence='SRC databinding/DialogAddTagBindingImpl.java:javap 3-arg <init> -> invalidateAll')
e('DialogAddTagBindingImpl.onFieldChange', 'DialogAddTagBindingImpl.onChangeViewModelState', 'CALL', 'onFieldChange dispatches to the onChangeViewModelState handler for its field id',
  evidence='SRC databinding/DialogAddTagBindingImpl.java:javap onFieldChange -> onChangeViewModelState')
e('DialogAddTagBindingImpl.executeBindings', 'DialogAddTagBindingImpl.onFieldChange', 'FRAMEWORK', 'Observable dispatch: executeBindings registers the observables and a change notifies onFieldChange', cls='non_standard', via='AndroidX databinding observable dispatch (executeBindings updateRegistration -> onFieldChange)',
  evidence='INFERRED databinding observable dispatch; SRC databinding/DialogAddTagBindingImpl.java:javap executeBindings -> updateRegistration')
e('AddTagDialog.onCreateDialog', 'DialogAddTagBindingImpl.setViewModel', 'CALL', 'Add-tag dialog binds its view model on creation',
  evidence='SRC ui/addtag/AddTagDialog.java:112,129')

# UNREACHABLE rows: no bytecode caller in auto_calls.json and no printed app trigger
# (recomputed for this batch; see REPORT.md). Labels, kinds and grades are copied
# unchanged from the authoritative merge-ready batch file.
UNREACHABLE.update({
    'DialogAddLinkBinding.getViewModel': ('no_trigger_in_app',
        'AddLinkDialog uses binding.setViewModel only, never getViewModel; generated executeBindings reads the mViewModel field directly.',
        'SRC ui/addlink/AddLinkDialog.java:171,185',
        'INFERRED'),
    'DialogAddLinkBindingImpl.setVariable': ('no_trigger_in_app',
        'No printed setVariable call site for this Impl; the view model is set through the typed setViewModel setter instead.',
        'SRC ui/addlink/AddLinkDialog.java:171,185',
        'INFERRED'),
    'DialogAddTagBinding.getViewModel': ('no_trigger_in_app',
        'AddTagDialog uses binding.setViewModel only, never getViewModel; generated executeBindings reads the mViewModel field directly.',
        'SRC ui/addtag/AddTagDialog.java:112,129',
        'INFERRED'),
    'DialogAddTagBindingImpl.setVariable': ('no_trigger_in_app',
        'No printed setVariable call site for this Impl; the view model is set through the typed setViewModel setter instead.',
        'SRC ui/addtag/AddTagDialog.java:112,129',
        'INFERRED'),
})

# SUPPRESS: no intra-group REACHABLE -> UNREACHABLE bytecode edge exists for this
# batch (recomputed from auto_calls.json + bytecode scan; cross-group candidates are
# listed in REPORT.md for merger reconciliation, not suppressed here).
SUPPRESS.update(set())
