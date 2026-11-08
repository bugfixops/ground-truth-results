# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 81 part (AddTorrentMutableParams (storage) and AddTorrentViewModel). Hand-written edges only.
# Each evidence string cites lines printed in
# helper/a3-g16/scratch/b081_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
# Rows whose route already exists in merger-tree graph_def.py are
# listed in the .md Dependencies line and are NOT repeated here.

e('AddTorrentViewModel$2.lambda$onPropertyChanged$0', 'AddTorrentMutableParams.setStorageFreeSpace', 'CALL', 'Dir-path runnable refreshes the stored free space',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:357; SRC ui/addtorrent/AddTorrentMutableParams.java:100-104')
e('AddTorrentActivity.initLayout', 'AddTorrentPagerAdapter.getItemCount', 'FRAMEWORK', 'ViewPager2 queries the fragment count after setAdapter',
  cls='non_standard', via='FragmentStateAdapter dispatch', evidence='INFERRED adapter dispatch; SRC ui/addtorrent/AddTorrentActivity.java:289; SRC ui/addtorrent/AddTorrentPagerAdapter.java:53-55')
e('AddTorrentActivity.onCreate', 'AddTorrentViewModel.<clinit>', 'FRAMEWORK', 'First provider use runs the ViewModel class initialisation',
  cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation; SRC ui/addtorrent/AddTorrentActivity.java:104; SRC ui/addtorrent/AddTorrentViewModel.java:79')
e('AddTorrentActivity.onCreate', 'AddTorrentViewModel.<init>', 'CALL', 'Activity obtains the ViewModel from the provider',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:103-104; SRC ui/addtorrent/AddTorrentViewModel.java:128-147')
e('AddTorrentViewModel.addTorrent', 'AddTorrentViewModel.checkFreeSpace', 'CALL', 'Add-torrent checks free space before adding',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:495; SRC ui/addtorrent/AddTorrentViewModel.java:548-556')
e('AddTorrentViewModel.updateChildren', 'AddTorrentViewModel.getChildren', 'CALL', 'Update-children lists the children of the current directory',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:451; SRC ui/addtorrent/AddTorrentViewModel.java:411-423')
e('AddTorrentInfoFragment$2.onAddTagClick', 'AddTorrentViewModel.getCurrentTags', 'CALL', 'Add-tag click lists the current tags',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:166; SRC ui/addtorrent/AddTorrentViewModel.java:149-151')
e('AddTorrentActivity.observeDecodeState', 'AddTorrentViewModel.getDecodeState', 'CALL', 'Decode-state observer reads the decode state LiveData',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:307; SRC ui/addtorrent/AddTorrentViewModel.java:167-169')
e('AddTorrentViewModel.addTorrent', 'AddTorrentViewModel.getSelectedFileIndexes', 'CALL', 'Add-torrent collects the selected file indexes',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:487; SRC ui/addtorrent/AddTorrentViewModel.java:454-464')
e('AddTorrentViewModel.<init>', 'AddTorrentViewModel.lambda$new$0', 'CALL', 'Init filter lambda runs on engine-need-start emissions',
  cls='non_standard', via='Rx filter dispatch', evidence='INFERRED Rx dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:137')
e('AddTorrentViewModel.<init>', 'AddTorrentViewModel.lambda$new$1', 'CALL', 'Init subscribe lambda runs on engine-need-start emissions',
  cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:138')
e('AddTorrentViewModel.observeFetchedMetadata', 'AddTorrentViewModel.lambda$observeFetchedMetadata$3', 'CALL', 'Fetched-metadata success callback runs on Single success',
  cls='non_standard', via='Rx dispatch', evidence='INFERRED Rx dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:330-333')
e('AddTorrentViewModel.observeFetchedMetadata', 'AddTorrentViewModel.lambda$observeFetchedMetadata$4', 'CALL', 'Fetched-metadata error callback runs on Single error',
  cls='non_standard', via='Rx dispatch', evidence='INFERRED Rx dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:334')
e('AddTorrentViewModel.startDecode', 'AddTorrentViewModel.lambda$startDecode$2', 'CALL', 'Start-decode subscribe lambda runs the decode task',
  cls='non_standard', via='Rx dispatch', evidence='INFERRED Rx dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:188-194')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'AddTorrentViewModel.observeFetchedMetadata', 'CALL', 'Decode task observes the fetched metadata for a magnet',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:243; SRC ui/addtorrent/AddTorrentViewModel.java:328-335')
e('AddTorrentActivity.onCreate', 'AddTorrentViewModel.onCleared', 'FRAMEWORK', 'ViewModel cleared when its activity owner is destroyed',
  cls='non_standard', via='ViewModel lifecycle dispatch', evidence='INFERRED ViewModel lifecycle dispatch; SRC ui/addtorrent/AddTorrentActivity.java:104; SRC ui/addtorrent/AddTorrentViewModel.java:176-180')
e('AddTorrentActivity$1.onNotificationResult', 'AddTorrentViewModel.restartForegroundNotification', 'CALL', 'Notification-permission callback restarts the foreground notification',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:123; SRC ui/addtorrent/AddTorrentViewModel.java:171-173')
e('AddTorrentViewModel.lambda$startDecode$2', 'AddTorrentViewModel.startDecodeTask', 'CALL', 'Start-decode lambda starts the decode task',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:190; SRC ui/addtorrent/AddTorrentViewModel.java:197-200')
e('AddTorrentViewModel.makeFileTree', 'AddTorrentViewModel.updateChildren', 'CALL', 'Make-file-tree refreshes the children after building the tree',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:400; SRC ui/addtorrent/AddTorrentViewModel.java:450-452')
e('AddTorrentViewModel.makeFileTree', 'AddTorrentViewModel.updateCurDir', 'CALL', 'Make-file-tree sets the current directory to the tree root',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:400; SRC ui/addtorrent/AddTorrentViewModel.java:445-448')
e('AddTorrentViewModel.<init>', 'AddTorrentViewModel$1.<init>', 'CALL', 'Init field initialiser creates the info callback',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:337-346')
e('AddTorrentViewModel.<init>', 'AddTorrentViewModel$1.onPropertyChanged', 'REGISTER', 'Info callback registered on the info ObservableField',
  cls='non_standard', via='Data-binding Observable dispatch on info.set', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:140; SRC ui/addtorrent/AddTorrentViewModel.java:339-345')
e('AddTorrentViewModel.<init>', 'AddTorrentViewModel$2.<init>', 'CALL', 'Init field initialiser creates the dir-path callback',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:348-366')
e('AddTorrentViewModel$2.onPropertyChanged', 'AddTorrentViewModel$2.lambda$onPropertyChanged$0', 'CALL', 'Dir-path callback runnable runs on subscribe',
  cls='non_standard', via='Rx Completable dispatch', evidence='INFERRED Rx dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:355-364')
e('AddTorrentViewModel.<init>', 'AddTorrentViewModel$2.onPropertyChanged', 'REGISTER', 'Dir-path callback registered on the dir-path ObservableField',
  cls='non_standard', via='Data-binding Observable dispatch on getDirPath().set', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:141; SRC ui/addtorrent/AddTorrentViewModel.java:350-365')

# UNREACHABLE rows in this batch (see REPORT.md for the SUPPRESS recompute).
UNREACHABLE.update({
    'AddTorrentMutableParams.toString': ('no_trigger_in_app',
        'No app code calls toString on an AddTorrentMutableParams instance; the batch evidence records a 252-file-tree grep with only getter/setter/field uses of mutableParams, and toString calls on Uri/Exception objects only.',
        'SRC ui/addtorrent/AddTorrentMutableParams.java:156-170',
        'INFERRED'),
})

# Own-batch UNREACHABLE method, suppressed so bytecode auto edges
# cannot resurrect it (cf. b013 precedent). No REACHABLE method in
# this group calls it in bytecode (see REPORT.md SUPPRESS recompute).
SUPPRESS.update({
    'AddTorrentMutableParams.toString',
})
