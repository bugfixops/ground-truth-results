# Citation-form rework 2026-11-01: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Converter C09 delivery (2026-11-01): base = audited A3 output helper a3-g12 parts b060.
# Labels, kinds, grades, edges and SUPPRESS are unchanged from the audited base
# (verified by the official harness against the authoritative merge-ready batch file).
# Stronger-evidence rule (step b): all UNREACHABLE keys of this batch were checked
# against the merger tree graph_def.py (read-only); the tree holds none of them, so
# no grade changes; all grades remain as audited.
# Printed evidence: the delivered printed file carries the base printed content plus
# a converter header; the G12 -c key-dispatch excerpts are NOT relied on (auditor
# finding: they repeat ctor-body lines and do not demonstrate dispatch); the -p
# signature blocks and printed source lines are the relied evidence.
# Batch 60 part (AddTorrentInfoBindingImpl, DetailTorrentAppbarBinding, DetailTorrentAppbarBindingImpl, DetailTorrentAppbarBindingLargeLandNotouchImpl, DetailTorrentAppbarBindingSw600dpLandImpl, DialogAddFeedChannelBinding, DialogAddFeedChannelBindingImpl). Hand-written edges, UNREACHABLE entries and SUPPRESS strings only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b060_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Generated databinding Impl evidence is javap -c -p output: generated Impl source is
# absent from final_java_only, so the printed file carries the javap dump under a
# .java-named header for that class (labelled as javap, not source).

e('AddTorrentInfoBindingImpl.executeBindings', 'AddTorrentInfoBindingImpl$4.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $4 listener and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/AddTorrentInfoBindingImpl.java:javap executeBindings -> setListeners')
e('AddTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[])', 'AddTorrentInfoBindingImpl$5.<init>', 'CALL', 'Three-arg Impl ctor creates the two-way inverse-listener $5',
  evidence='SRC databinding/AddTorrentInfoBindingImpl.java:javap 3-arg <init> -> AddTorrentInfoBindingImpl$5 <init>')
e('AddTorrentInfoBindingImpl.executeBindings', 'AddTorrentInfoBindingImpl$5.onChange', 'FRAMEWORK', 'Two-way inverse-listener dispatch: executeBindings installs the $5 listener and a user edit/toggle fires onChange', cls='non_standard', via='AndroidX two-way inverse binding listener dispatch (executeBindings setListeners -> onChange)',
  evidence='INFERRED two-way inverse binding listener dispatch; SRC databinding/AddTorrentInfoBindingImpl.java:javap executeBindings -> setListeners')
e('DetailTorrentAppbarBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DetailTorrentAppbarBinding.<init>', 'CALL', 'Variant three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/DetailTorrentAppbarBindingImpl.java:javap 3-arg <init> -> DetailTorrentAppbarBinding <init>')
e('DetailTorrentAppbarBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View,Object[])', 'DetailTorrentAppbarBinding.<init>', 'CALL', 'Variant three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/DetailTorrentAppbarBindingLargeLandNotouchImpl.java:javap 3-arg <init> -> DetailTorrentAppbarBinding <init>')
e('DetailTorrentAppbarBindingSw600dpLandImpl.<init>(DataBindingComponent,View,Object[])', 'DetailTorrentAppbarBinding.<init>', 'CALL', 'Variant three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/DetailTorrentAppbarBindingSw600dpLandImpl.java:javap 3-arg <init> -> DetailTorrentAppbarBinding <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DetailTorrentAppbarBindingImpl.<clinit>', 'FRAMEWORK', 'Databinding mapper instantiation loads the Impl class, running its static initializer',
  evidence='INFERRED databinding mapper class load; SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DetailTorrentAppbarBindingImpl 2-arg <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DetailTorrentAppbarBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl for its layout id',
  evidence='SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DetailTorrentAppbarBindingImpl 2-arg <init>')
e('DetailTorrentAppbarBindingImpl.<init>(DataBindingComponent,View)', 'DetailTorrentAppbarBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Two-arg Impl ctor delegates to the three-arg ctor via mapBindings',
  evidence='SRC databinding/DetailTorrentAppbarBindingImpl.java:javap 2-arg <init> -> 3-arg <init>')
e('DetailTorrentAppbarBindingImpl.invalidateAll', 'DetailTorrentAppbarBindingImpl.executeBindings', 'FRAMEWORK', 'Rebind flow: invalidateAll requests a rebind and the framework runs executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (invalidateAll/requestRebind -> executePendingBindings -> executeBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DetailTorrentAppbarBindingImpl.java:javap invalidateAll -> requestRebind')
e('FragmentDetailTorrentBindingImpl.hasPendingBindings', 'DetailTorrentAppbarBindingImpl.hasPendingBindings', 'CALL', 'Parent binding propagates to the included binding (hasPendingBindings)',
  evidence='SRC databinding/FragmentDetailTorrentBindingImpl.java:javap FragmentDetailTorrentBindingImpl.hasPendingBindings -> DetailTorrentAppbarBindingImpl.hasPendingBindings')
e('DetailTorrentAppbarBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DetailTorrentAppbarBindingImpl.invalidateAll', 'CALL', 'Three-arg Impl ctor calls invalidateAll',
  evidence='SRC databinding/DetailTorrentAppbarBindingImpl.java:javap 3-arg <init> -> invalidateAll')
e('FragmentDetailTorrentBindingImpl.invalidateAll', 'DetailTorrentAppbarBindingImpl.invalidateAll', 'CALL', 'Parent binding propagates to the included binding (invalidateAll)',
  evidence='SRC databinding/FragmentDetailTorrentBindingImpl.java:javap FragmentDetailTorrentBindingImpl.invalidateAll -> DetailTorrentAppbarBindingImpl.invalidateAll')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DetailTorrentAppbarBindingLargeLandNotouchImpl.<clinit>', 'FRAMEWORK', 'Databinding mapper instantiation loads the Impl class, running its static initializer',
  evidence='INFERRED databinding mapper class load; SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DetailTorrentAppbarBindingLargeLandNotouchImpl 2-arg <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DetailTorrentAppbarBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl for its layout id',
  evidence='SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DetailTorrentAppbarBindingLargeLandNotouchImpl 2-arg <init>')
e('DetailTorrentAppbarBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View)', 'DetailTorrentAppbarBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Two-arg Impl ctor delegates to the three-arg ctor via mapBindings',
  evidence='SRC databinding/DetailTorrentAppbarBindingLargeLandNotouchImpl.java:javap 2-arg <init> -> 3-arg <init>')
e('DetailTorrentAppbarBindingLargeLandNotouchImpl.invalidateAll', 'DetailTorrentAppbarBindingLargeLandNotouchImpl.executeBindings', 'FRAMEWORK', 'Rebind flow: invalidateAll requests a rebind and the framework runs executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (invalidateAll/requestRebind -> executePendingBindings -> executeBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DetailTorrentAppbarBindingLargeLandNotouchImpl.java:javap invalidateAll -> requestRebind')
e('FragmentDetailTorrentBindingImpl.hasPendingBindings', 'DetailTorrentAppbarBindingLargeLandNotouchImpl.hasPendingBindings', 'CALL', 'Parent binding propagates to the included binding (hasPendingBindings)',
  evidence='SRC databinding/FragmentDetailTorrentBindingImpl.java:javap FragmentDetailTorrentBindingImpl.hasPendingBindings -> DetailTorrentAppbarBindingLargeLandNotouchImpl.hasPendingBindings')
e('DetailTorrentAppbarBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View,Object[])', 'DetailTorrentAppbarBindingLargeLandNotouchImpl.invalidateAll', 'CALL', 'Three-arg Impl ctor calls invalidateAll',
  evidence='SRC databinding/DetailTorrentAppbarBindingLargeLandNotouchImpl.java:javap 3-arg <init> -> invalidateAll')
e('FragmentDetailTorrentBindingImpl.invalidateAll', 'DetailTorrentAppbarBindingLargeLandNotouchImpl.invalidateAll', 'CALL', 'Parent binding propagates to the included binding (invalidateAll)',
  evidence='SRC databinding/FragmentDetailTorrentBindingImpl.java:javap FragmentDetailTorrentBindingImpl.invalidateAll -> DetailTorrentAppbarBindingLargeLandNotouchImpl.invalidateAll')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DetailTorrentAppbarBindingSw600dpLandImpl.<clinit>', 'FRAMEWORK', 'Databinding mapper instantiation loads the Impl class, running its static initializer',
  evidence='INFERRED databinding mapper class load; SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DetailTorrentAppbarBindingSw600dpLandImpl 2-arg <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DetailTorrentAppbarBindingSw600dpLandImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl for its layout id',
  evidence='SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DetailTorrentAppbarBindingSw600dpLandImpl 2-arg <init>')
e('DetailTorrentAppbarBindingSw600dpLandImpl.<init>(DataBindingComponent,View)', 'DetailTorrentAppbarBindingSw600dpLandImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Two-arg Impl ctor delegates to the three-arg ctor via mapBindings',
  evidence='SRC databinding/DetailTorrentAppbarBindingSw600dpLandImpl.java:javap 2-arg <init> -> 3-arg <init>')
e('DetailTorrentAppbarBindingSw600dpLandImpl.invalidateAll', 'DetailTorrentAppbarBindingSw600dpLandImpl.executeBindings', 'FRAMEWORK', 'Rebind flow: invalidateAll requests a rebind and the framework runs executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (invalidateAll/requestRebind -> executePendingBindings -> executeBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DetailTorrentAppbarBindingSw600dpLandImpl.java:javap invalidateAll -> requestRebind')
e('FragmentDetailTorrentBindingImpl.hasPendingBindings', 'DetailTorrentAppbarBindingSw600dpLandImpl.hasPendingBindings', 'CALL', 'Parent binding propagates to the included binding (hasPendingBindings)',
  evidence='SRC databinding/FragmentDetailTorrentBindingImpl.java:javap FragmentDetailTorrentBindingImpl.hasPendingBindings -> DetailTorrentAppbarBindingSw600dpLandImpl.hasPendingBindings')
e('DetailTorrentAppbarBindingSw600dpLandImpl.<init>(DataBindingComponent,View,Object[])', 'DetailTorrentAppbarBindingSw600dpLandImpl.invalidateAll', 'CALL', 'Three-arg Impl ctor calls invalidateAll',
  evidence='SRC databinding/DetailTorrentAppbarBindingSw600dpLandImpl.java:javap 3-arg <init> -> invalidateAll')
e('FragmentDetailTorrentBindingImpl.invalidateAll', 'DetailTorrentAppbarBindingSw600dpLandImpl.invalidateAll', 'CALL', 'Parent binding propagates to the included binding (invalidateAll)',
  evidence='SRC databinding/FragmentDetailTorrentBindingImpl.java:javap FragmentDetailTorrentBindingImpl.invalidateAll -> DetailTorrentAppbarBindingSw600dpLandImpl.invalidateAll')
e('DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddFeedChannelBinding.<init>', 'CALL', 'Three-arg Impl ctor calls its base Binding ctor (super)',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap 3-arg <init> -> DialogAddFeedChannelBinding <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DialogAddFeedChannelBindingImpl.<clinit>', 'FRAMEWORK', 'Databinding mapper instantiation loads the Impl class, running its static initializer',
  evidence='INFERRED databinding mapper class load; SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DialogAddFeedChannelBindingImpl 2-arg <init>')
e('libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View)', 'CALL', 'Mapper instantiates the Impl for its layout id',
  evidence='SRC libretorrent/DataBinderMapperImpl.java:javap getDataBinder -> DialogAddFeedChannelBindingImpl 2-arg <init>')
e('DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View)', 'DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[])', 'CALL', 'Two-arg Impl ctor delegates to the three-arg ctor via mapBindings',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap 2-arg <init> -> 3-arg <init>')
e('DialogAddFeedChannelBindingImpl.invalidateAll', 'DialogAddFeedChannelBindingImpl.executeBindings', 'FRAMEWORK', 'Rebind flow: invalidateAll requests a rebind and the framework runs executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (invalidateAll/requestRebind -> executePendingBindings -> executeBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DialogAddFeedChannelBindingImpl.java:javap invalidateAll -> requestRebind')
e('DialogAddFeedChannelBindingImpl.invalidateAll', 'DialogAddFeedChannelBindingImpl.hasPendingBindings', 'FRAMEWORK', 'Rebind flow: the framework checks hasPendingBindings before running executeBindings', cls='non_standard', via='AndroidX databinding rebind dispatch (executePendingBindings checks hasPendingBindings)',
  evidence='INFERRED databinding rebind dispatch; SRC databinding/DialogAddFeedChannelBindingImpl.java:javap invalidateAll -> requestRebind')
e('DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[])', 'DialogAddFeedChannelBindingImpl.invalidateAll', 'CALL', 'Three-arg Impl ctor calls invalidateAll',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap 3-arg <init> -> invalidateAll')
e('DialogAddFeedChannelBindingImpl.onFieldChange', 'DialogAddFeedChannelBindingImpl.onChangeViewModelMutableParams', 'CALL', 'onFieldChange dispatches to the onChangeViewModelMutableParams handler for its field id',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap onFieldChange -> onChangeViewModelMutableParams')
e('DialogAddFeedChannelBindingImpl.onFieldChange', 'DialogAddFeedChannelBindingImpl.onChangeViewModelShowClipboardButton', 'CALL', 'onFieldChange dispatches to the onChangeViewModelShowClipboardButton handler for its field id',
  evidence='SRC databinding/DialogAddFeedChannelBindingImpl.java:javap onFieldChange -> onChangeViewModelShowClipboardButton')
e('DialogAddFeedChannelBindingImpl.executeBindings', 'DialogAddFeedChannelBindingImpl.onFieldChange', 'FRAMEWORK', 'Observable dispatch: executeBindings registers the observables and a change notifies onFieldChange', cls='non_standard', via='AndroidX databinding observable dispatch (executeBindings updateRegistration -> onFieldChange)',
  evidence='INFERRED databinding observable dispatch; SRC databinding/DialogAddFeedChannelBindingImpl.java:javap executeBindings -> updateRegistration')

# UNREACHABLE rows: no bytecode caller in auto_calls.json and no printed app trigger
# (recomputed for this batch; see REPORT.md). Labels, kinds and grades are copied
# unchanged from the authoritative merge-ready batch file.
UNREACHABLE.update({
    'DetailTorrentAppbarBindingImpl.onFieldChange': ('no_trigger_in_app',
        'detail_torrent_appbar.xml declares no <data> block and no @{...} expressions, so no observable exists for onFieldChange to fire on.',
        'INFERRED layout analysis in batch file (all three appbar layouts)',
        'INFERRED'),
    'DetailTorrentAppbarBindingImpl.setVariable': ('no_trigger_in_app',
        'detail_torrent_appbar.xml declares no <data> variable, so the generated outer Impl has no variable to propagate via setVariable.',
        'INFERRED layout analysis in batch file (all three appbar layouts)',
        'INFERRED'),
    'DetailTorrentAppbarBindingLargeLandNotouchImpl.onFieldChange': ('no_trigger_in_app',
        'detail_torrent_appbar (large-land-notouch) layout declares no <data> block and no @{...} expressions, so no observable exists for onFieldChange to fire on.',
        'INFERRED layout analysis in batch file (all three appbar layouts)',
        'INFERRED'),
    'DetailTorrentAppbarBindingLargeLandNotouchImpl.setVariable': ('no_trigger_in_app',
        'detail_torrent_appbar (large-land-notouch) layout declares no <data> variable, so no variable exists to propagate via setVariable.',
        'INFERRED layout analysis in batch file (all three appbar layouts)',
        'INFERRED'),
    'DetailTorrentAppbarBindingSw600dpLandImpl.onFieldChange': ('no_trigger_in_app',
        'detail_torrent_appbar (sw600dp-land) layout declares no <data> block and no @{...} expressions, so no observable exists for onFieldChange to fire on.',
        'INFERRED layout analysis in batch file (all three appbar layouts)',
        'INFERRED'),
    'DetailTorrentAppbarBindingSw600dpLandImpl.setVariable': ('no_trigger_in_app',
        'detail_torrent_appbar (sw600dp-land) layout declares no <data> variable, so no variable exists to propagate via setVariable.',
        'INFERRED layout analysis in batch file (all three appbar layouts)',
        'INFERRED'),
    'DialogAddFeedChannelBinding.getViewModel': ('no_trigger_in_app',
        'AddFeedDialog uses binding.setViewModel and binding.getRoot only, never getViewModel; generated executeBindings reads the mViewModel field directly.',
        'SRC ui/addfeed/AddFeedDialog.java:180,203',
        'INFERRED'),
    'DialogAddFeedChannelBindingImpl.setVariable': ('no_trigger_in_app',
        'No printed setVariable call site for this Impl; the view model is set through the typed setViewModel setter instead.',
        'SRC ui/addfeed/AddFeedDialog.java:180,203',
        'INFERRED'),
})

# SUPPRESS: no intra-group REACHABLE -> UNREACHABLE bytecode edge exists for this
# batch (recomputed from auto_calls.json + bytecode scan; cross-group candidates are
# listed in REPORT.md for merger reconciliation, not suppressed here).
SUPPRESS.update(set())
