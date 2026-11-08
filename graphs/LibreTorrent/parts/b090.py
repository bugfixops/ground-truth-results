# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 90 part (MsgDetailTorrentViewModel, TorrentDetailsInfo, TorrentDetailsMutableParams, DetailTorrentInfoFragment). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b090_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.
# Build names are exact (tools/build_graph.py method_names on method_list.json);
# no method in this batch is overloaded, so no .py edge carries params.
# Labels/kinds follow the merge-ready label cells (Phase 3 L1 verdict applied
# for rows 16 and 28; the batch file's older OPEN prose is superseded by
# those cells, as its own prose-fix note states).

e('DetailTorrentFilesFragment$4.onCreateActionMode', 'MsgDetailTorrentViewModel.fragmentInActionMode', 'CALL', 'Action-mode creation reports action mode active', cls='explicit', evidence='SRC ui/detailtorrent/pages/files/DetailTorrentFilesFragment.java:388; SRC ui/detailtorrent/MsgDetailTorrentViewModel.java:31-34')
e('DetailTorrentFragment.subscribeMsgViewModel', 'MsgDetailTorrentViewModel.observeFragmentInActionMode', 'CALL', 'Message-ViewModel subscription observes the action-mode state', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:280; SRC ui/detailtorrent/MsgDetailTorrentViewModel.java:36-39')
e('DetailTorrentViewModel.<init>', 'TorrentDetailsInfo.<init>', 'CALL', 'ViewModel field initialiser constructs the details info', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:91')
e('DetailTorrentViewModel$2.onPropertyChanged', 'TorrentDetailsInfo.getAdvancedInfo', 'CALL', 'Info callback reads the advanced info', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:471; SRC ui/detailtorrent/TorrentDetailsInfo.java:66-69')
e('DetailTorrentInfoFragment.onCreateView', 'TorrentDetailsInfo.getDirName', 'FRAMEWORK', 'Generated data binding reads the directory name for the info layout', cls='non_standard', via='generated databinding dispatch (fragment inflates and sets the ViewModel here)', evidence='INFERRED databinding dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:99-105; SRC ui/detailtorrent/TorrentDetailsInfo.java:78-81')
e('DetailTorrentViewModel.makeFileTree', 'TorrentDetailsInfo.getMetaInfo', 'CALL', 'File-tree build reads the meta-info', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:536; SRC ui/detailtorrent/TorrentDetailsInfo.java:102-105')
e('DetailTorrentViewModel.checkFreeSpace', 'TorrentDetailsInfo.getStorageFreeSpace', 'CALL', 'Free-space check reads the stored free space', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:426; SRC ui/detailtorrent/TorrentDetailsInfo.java:90-93')
e('DetailTorrentViewModel.updateInfo(Torrent,TorrentInfo)', 'TorrentDetailsInfo.getTorrent', 'CALL', 'Info update checks the previous torrent', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:207; SRC ui/detailtorrent/TorrentDetailsInfo.java:42-45')
e('DetailTorrentViewModel.checkParamsChanged', 'TorrentDetailsInfo.getTorrentInfo', 'CALL', 'Params change reads the torrent info', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:480; SRC ui/detailtorrent/TorrentDetailsInfo.java:54-57')
e('DetailTorrentViewModel.updateInfo(AdvancedTorrentInfo)', 'TorrentDetailsInfo.setAdvancedInfo', 'CALL', 'Advanced-info update stores the advanced info', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:219; SRC ui/detailtorrent/TorrentDetailsInfo.java:71-74')
e('DetailTorrentViewModel$1.lambda$onPropertyChanged$0', 'TorrentDetailsInfo.setDirName', 'CALL', 'Params-change runnable stores the directory name', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:454; SRC ui/detailtorrent/TorrentDetailsInfo.java:83-86')
e('DetailTorrentViewModel.updateInfo(TorrentMetaInfo)', 'TorrentDetailsInfo.setMetaInfo', 'CALL', 'Meta-info update stores the meta-info', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:200; SRC ui/detailtorrent/TorrentDetailsInfo.java:107-110')
e('DetailTorrentViewModel$1.lambda$onPropertyChanged$0', 'TorrentDetailsInfo.setStorageFreeSpace', 'CALL', 'Params-change runnable stores the free space', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:453; SRC ui/detailtorrent/TorrentDetailsInfo.java:95-98')
e('DetailTorrentViewModel.updateInfo(Torrent,TorrentInfo)', 'TorrentDetailsInfo.setTorrent', 'CALL', 'Info update stores the torrent', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:209; SRC ui/detailtorrent/TorrentDetailsInfo.java:47-50')
e('DetailTorrentViewModel.updateInfo(Torrent,TorrentInfo)', 'TorrentDetailsInfo.setTorrentInfo', 'CALL', 'Info update stores the torrent info', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:210; SRC ui/detailtorrent/TorrentDetailsInfo.java:59-62')
e('DetailTorrentViewModel.<init>', 'TorrentDetailsMutableParams.<init>', 'CALL', 'ViewModel field initialiser constructs the mutable params', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:92')
e('DetailTorrentViewModel$1.onPropertyChanged', 'TorrentDetailsMutableParams.getDirPath', 'CALL', 'Params-change callback reads the directory path', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:447; SRC ui/detailtorrent/TorrentDetailsMutableParams.java:62-65')
e('DetailTorrentViewModel.checkParamsChanged', 'TorrentDetailsMutableParams.getName', 'CALL', 'Params change reads the torrent name', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:486; SRC ui/detailtorrent/TorrentDetailsMutableParams.java:38-41')
e('DetailTorrentViewModel.checkParamsChanged', 'TorrentDetailsMutableParams.isFirstLastPiecePriority', 'CALL', 'Params change reads the first-last-piece flag', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:513; SRC ui/detailtorrent/TorrentDetailsMutableParams.java:86-89')
e('DetailTorrentViewModel.checkParamsChanged', 'TorrentDetailsMutableParams.isPrioritiesChanged', 'CALL', 'Params change reads the priorities-changed flag', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:504; SRC ui/detailtorrent/TorrentDetailsMutableParams.java:74-77')
e('DetailTorrentViewModel.checkParamsChanged', 'TorrentDetailsMutableParams.isSequentialDownload', 'CALL', 'Params change reads the sequential-download flag', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:498; SRC ui/detailtorrent/TorrentDetailsMutableParams.java:50-53')
e('DetailTorrentViewModel.initMutableParams', 'TorrentDetailsMutableParams.setDirPath', 'CALL', 'Mutable-params initialisation stores the directory path', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:438; SRC ui/detailtorrent/TorrentDetailsMutableParams.java:67-70')
e('DetailTorrentViewModel.initMutableParams', 'TorrentDetailsMutableParams.setFirstLastPiecePriority', 'CALL', 'Mutable-params initialisation stores the first-last-piece flag', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:440; SRC ui/detailtorrent/TorrentDetailsMutableParams.java:91-94')
e('DetailTorrentViewModel.initMutableParams', 'TorrentDetailsMutableParams.setName', 'CALL', 'Mutable-params initialisation stores the name', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:437; SRC ui/detailtorrent/TorrentDetailsMutableParams.java:43-46')
e('DetailTorrentViewModel.lambda$applyPriority$4', 'TorrentDetailsMutableParams.setPrioritiesChanged', 'CALL', 'Apply-priority subscription marks priorities changed', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:334; SRC ui/detailtorrent/TorrentDetailsMutableParams.java:79-82')
e('DetailTorrentViewModel.initMutableParams', 'TorrentDetailsMutableParams.setSequentialDownload', 'CALL', 'Mutable-params initialisation stores the sequential flag', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentViewModel.java:439; SRC ui/detailtorrent/TorrentDetailsMutableParams.java:55-58')
e('DetailTorrentInfoFragment.newInstance', 'DetailTorrentInfoFragment.<clinit>', 'CALL', 'First construction of the info fragment runs its class initialisation', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:81-88; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:69-72')
e('DetailTorrentInfoFragment.newInstance', 'DetailTorrentInfoFragment.<init>', 'CALL', 'Info fragment factory constructs the fragment', cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:82')
e('DetailTorrentInfoFragment.subscribeAlertDialog', 'DetailTorrentInfoFragment.checkNameField', 'CALL', 'Alert-dialog subscription validates the edited name', cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:226; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:259-272')
e('DetailTorrentInfoFragment.subscribeAlertDialog', 'DetailTorrentInfoFragment.initEditNameDialog', 'CALL', 'Alert-dialog shown event initialises the edit-name dialog', cls='explicit', evidence='SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:218; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:294-323')
e('DetailTorrentInfoFragment.showChooseDirDialog', 'DetailTorrentInfoFragment.lambda$new$2', 'CALL', 'Choose-directory result callback handles the picked directory', cls='non_standard', via='ActivityResult dispatch (launcher launched here; result callback runs on return)', evidence='INFERRED ActivityResult dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:185-194; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:117-131')
e('DetailTorrentInfoFragment$1.onAddTagClick', 'DetailTorrentInfoFragment.lambda$new$3', 'CALL', 'Select-tag result callback handles the picked tag', cls='non_standard', via='ActivityResult dispatch (launcher launched here; result callback runs on return)', evidence='INFERRED ActivityResult dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:157-165; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:132-145')
e('DetailTorrentInfoFragment.onCreateView', 'DetailTorrentInfoFragment.lambda$onCreateView$0', 'CALL', 'Folder-chooser button click opens the choose-directory dialog', cls='non_standard', via='view click dispatch', evidence='INFERRED view click dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:110')
e('DetailTorrentInfoFragment.onCreateView', 'DetailTorrentInfoFragment.lambda$onCreateView$1', 'CALL', 'Edit-name button click opens the edit-name dialog', cls='non_standard', via='view click dispatch', evidence='INFERRED view click dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:111')
e('DetailTorrentInfoFragment.subscribeAlertDialog', 'DetailTorrentInfoFragment.lambda$subscribeAlertDialog$4', 'CALL', 'Alert-dialog subscription consumer handles dialog events', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:211-242')
e('DetailPagerAdapter.createFragment', 'DetailTorrentInfoFragment.newInstance', 'CALL', 'Pager creates the info fragment for its position', cls='explicit', evidence='SRC ui/detailtorrent/DetailPagerAdapter.java:55-56; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:81-88')
e('DetailPagerAdapter.createFragment', 'DetailTorrentInfoFragment.onAttach', 'FRAMEWORK', 'ViewPager2 attaches the info fragment', cls='non_standard', via='ViewPager2 fragment lifecycle dispatch', evidence='INFERRED fragment lifecycle dispatch; SRC ui/detailtorrent/DetailPagerAdapter.java:53-56; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:91-97')
e('DetailPagerAdapter.createFragment', 'DetailTorrentInfoFragment.onCreateView', 'FRAMEWORK', 'ViewPager2 creates the info fragment view', cls='non_standard', via='ViewPager2 fragment lifecycle dispatch', evidence='INFERRED fragment lifecycle dispatch; SRC ui/detailtorrent/DetailPagerAdapter.java:53-56; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:99-115')

# UNREACHABLE rows (Phase 3 L1 verdicts; kind + confirmed_by from the
# merge-ready label/kind/confirmed_by cells).
UNREACHABLE.update({
    "TorrentDetailsInfo.toString": ("no_trigger_in_app",
        "Definition TorrentDetailsInfo.java:115-125. No printed caller in any freshly printed file; the openclose round-2 252-file app-Java grep shows no .toString() call or concatenation site on this type. Implicit toString dispatch is the undecided project-wide question, resolved for this row by the Phase 3 L1 verdict (label/kind cells govern).",
        "SRC ui/detailtorrent/TorrentDetailsInfo.java:115-125",
        "INFERRED"),
    "TorrentDetailsMutableParams.toString": ("no_trigger_in_app",
        "Definition TorrentDetailsMutableParams.java:99-109. ViewModel uses mutableParams only via field access, property callbacks and setters, never toString; the openclose round-2 252-file app-Java grep shows no .toString() call or concatenation site on this type. Resolved for this row by the Phase 3 L1 verdict (label/kind cells govern).",
        "SRC ui/detailtorrent/TorrentDetailsMutableParams.java:99-109",
        "INFERRED"),
})

# No part edge points at a method that is UNREACHABLE in any batch, and
# auto_calls.json contains no call into either UNREACHABLE method above
# (checked; javap confirms no invoke of these toString methods in the
# detail-torrent bytecode tree). No REACHABLE method of this batch calls
# an UNREACHABLE method in bytecode, so no SUPPRESS entry applies and no
# cross-group pair is left unreported.
SUPPRESS.update(set())
