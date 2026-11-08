# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# C12 converter delivery (2026-11-01): audited A3 base copied unchanged except this header.
# No UNREACHABLE rows: stronger-evidence rule (b) is vacuous; no grade changes.
# Merger note recorded in REPORT-b080.md, NOT applied: row 23 getDirName stands STRONGER than INFERRED-only (layout binding directly confirmed at fragment_add_torrent_info.xml:73 + @Bindable getter + onViewCreated:102 binding set; only generated executeBindings mechanics is INFERRED) — kept as audited. Delivered printed evidence: parts/b080_printed.txt (fresh, from clone tree).
# Batch 80 part (AddTorrentInfoFragment and AddTorrentMutableParams). Hand-written edges only.
# Each evidence string cites lines printed in
# helper/a3-g16/scratch/b080_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
# Rows whose route already exists in merger-tree graph_def.py are
# listed in the .md Dependencies line and are NOT repeated here.

e('AddTorrentInfoFragment.onViewCreated', 'AddTorrentInfoFragment.lambda$onViewCreated$0', 'FRAMEWORK', 'Folder-chooser button click dispatched to the click lambda',
  cls='non_standard', via='View click dispatch', evidence='INFERRED View click dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:105; SRC ui/addtorrent/AddTorrentInfoFragment.java:192-213')
e('AddTorrentInfoFragment.onStart', 'AddTorrentInfoFragment.onStop', 'LIFECYCLE', 'Fragment stops after starting',
  evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:124-128; SRC ui/addtorrent/AddTorrentInfoFragment.java:131-135')
e('AddTorrentInfoFragment.onViewCreated', 'AddTorrentInfoFragment$1.<init>', 'CALL', 'View-created constructs the name TextWatcher',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:106-119')
e('AddTorrentInfoFragment.onViewCreated', 'AddTorrentInfoFragment$1.beforeTextChanged', 'FRAMEWORK', 'TextWatcher beforeTextChanged dispatched on name-field text change',
  cls='non_standard', via='TextWatcher dispatch', evidence='INFERRED TextWatcher dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:106-109')
e('AddTorrentInfoFragment.onViewCreated', 'AddTorrentInfoFragment$1.onTextChanged', 'FRAMEWORK', 'TextWatcher onTextChanged dispatched on name-field text change',
  cls='non_standard', via='TextWatcher dispatch', evidence='INFERRED TextWatcher dispatch; SRC ui/addtorrent/AddTorrentInfoFragment.java:106-113')
e('AddTorrentInfoFragment.<init>', 'AddTorrentInfoFragment$2.<init>', 'CALL', 'Field initialiser creates the tags listener',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:163-183')
e('AddTorrentViewModel.<init>', 'AddTorrentMutableParams.<init>', 'CALL', 'ViewModel field initialiser creates the mutable params',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:81')
e('AddTorrentInfoFragment.onViewCreated', 'AddTorrentMutableParams.getDirName', 'CALL', 'Generated databinding executeBindings reads the dirName getter',
  cls='non_standard', via='Generated databinding executeBindings read', evidence='INFERRED generated databinding read; SRC ui/addtorrent/AddTorrentInfoFragment.java:102; SRC ui/addtorrent/AddTorrentMutableParams.java:82-86')
e('AddTorrentInfoFragment.showChooseDirDialog', 'AddTorrentMutableParams.getDirPath', 'CALL', 'Choose-dir dialog reads the current dir path',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentInfoFragment.java:200; SRC ui/addtorrent/AddTorrentMutableParams.java:77-80')
e('AddTorrentActivity.addTorrent', 'AddTorrentMutableParams.getName', 'CALL', 'Add-torrent reads the torrent name',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:364; SRC ui/addtorrent/AddTorrentMutableParams.java:66-69')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'AddTorrentMutableParams.getSource', 'CALL', 'Decode task reads the torrent source',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:269; SRC ui/addtorrent/AddTorrentMutableParams.java:45-48')
e('AddTorrentViewModel.checkFreeSpace', 'AddTorrentMutableParams.getStorageFreeSpace', 'CALL', 'Free-space check reads the stored free space',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:552; SRC ui/addtorrent/AddTorrentMutableParams.java:95-98')
e('AddTorrentActivity$2.onPropertyChanged', 'AddTorrentMutableParams.isFirstLastPiecePriority', 'CALL', 'Params-changed callback reads first-last-piece priority',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:230; SRC ui/addtorrent/AddTorrentMutableParams.java:143-146')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'AddTorrentMutableParams.isFromMagnet', 'CALL', 'Decode task reads the from-magnet flag',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:270; SRC ui/addtorrent/AddTorrentMutableParams.java:55-58')
e('AddTorrentActivity$2.onPropertyChanged', 'AddTorrentMutableParams.isIgnoreFreeSpace', 'CALL', 'Params-changed callback reads ignore-free-space',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:223; SRC ui/addtorrent/AddTorrentMutableParams.java:131-134')
e('AddTorrentActivity$2.onPropertyChanged', 'AddTorrentMutableParams.isSequentialDownload', 'CALL', 'Params-changed callback reads sequential download',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:209; SRC ui/addtorrent/AddTorrentMutableParams.java:107-110')
e('AddTorrentActivity$2.onPropertyChanged', 'AddTorrentMutableParams.isStartAfterAdd', 'CALL', 'Params-changed callback reads start-after-add',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:216; SRC ui/addtorrent/AddTorrentMutableParams.java:119-122')
e('AddTorrentViewModel$2.lambda$onPropertyChanged$0', 'AddTorrentMutableParams.setDirName', 'CALL', 'Dir-path runnable writes the directory name',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:358; SRC ui/addtorrent/AddTorrentMutableParams.java:88-91')
e('AddTorrentActivity.fillMutableParams', 'AddTorrentMutableParams.setFirstLastPiecePriority', 'CALL', 'Fill-params writes first-last-piece priority from prefs',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:161; SRC ui/addtorrent/AddTorrentMutableParams.java:148-151')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'AddTorrentMutableParams.setFromMagnet', 'CALL', 'Decode task marks the params as from-magnet',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:235; SRC ui/addtorrent/AddTorrentMutableParams.java:60-63')
e('AddTorrentActivity.fillMutableParams', 'AddTorrentMutableParams.setIgnoreFreeSpace', 'CALL', 'Fill-params writes ignore-free-space from prefs',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:155; SRC ui/addtorrent/AddTorrentMutableParams.java:136-139')
e('AddTorrentViewModel$1.onPropertyChanged', 'AddTorrentMutableParams.setName', 'CALL', 'Info callback writes the decoded torrent name',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:344; SRC ui/addtorrent/AddTorrentMutableParams.java:71-74')
e('AddTorrentActivity.fillMutableParams', 'AddTorrentMutableParams.setSequentialDownload', 'CALL', 'Fill-params writes sequential download from prefs',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:143; SRC ui/addtorrent/AddTorrentMutableParams.java:112-115')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'AddTorrentMutableParams.setSource', 'CALL', 'Decode task writes the torrent source',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:227; SRC ui/addtorrent/AddTorrentMutableParams.java:50-53')
e('AddTorrentActivity.fillMutableParams', 'AddTorrentMutableParams.setStartAfterAdd', 'CALL', 'Fill-params writes start-after-add from prefs',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentActivity.java:149; SRC ui/addtorrent/AddTorrentMutableParams.java:124-127')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No UNREACHABLE rows in this batch and no REACHABLE method of this
# group calls an UNREACHABLE method in bytecode (see REPORT.md),
# so no SUPPRESS entries apply.
SUPPRESS.update(set())
