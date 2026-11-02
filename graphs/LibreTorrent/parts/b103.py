# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 103 part (FileManager dialog, nodes and spinner adapter). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b103_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

e('FileManagerDialog.onOptionsItemSelected', 'FileManagerDialog.openHomeDirectory', 'CALL', 'Menu home item opens the home directory', evidence='SRC ui/filemanager/FileManagerDialog.java:503-504; SRC ui/filemanager/FileManagerDialog.java:518-522')
e('FileManagerDialog$2.onItemSelected', 'FileManagerDialog.permissionDeniedToast', 'CALL', 'Spinner selection catch shows the denial toast', evidence='SRC ui/filemanager/FileManagerDialog.java:230-231; SRC ui/filemanager/FileManagerDialog.java:382-387')
e('FileManagerDialog.onCreate', 'FileManagerDialog.refreshDir', 'FRAMEWORK', 'Swipe-refresh listener runs refreshDir', cls='non_standard', via='SwipeRefreshLayout dispatch', evidence='INFERRED SwipeRefreshLayout dispatch; SRC ui/filemanager/FileManagerDialog.java:199; SRC ui/filemanager/FileManagerDialog.java:459-462')
e('FileManagerDialog.onCreate', 'FileManagerDialog.registerMediaReceiver', 'CALL', 'onCreate registers the media receiver', evidence='SRC ui/filemanager/FileManagerDialog.java:240; SRC ui/filemanager/FileManagerDialog.java:281-287')
e('FileManagerDialog$MediaReceiver.onReceive', 'FileManagerDialog.reloadSpinner', 'CALL', 'Media broadcast reloads the spinner', evidence='SRC ui/filemanager/FileManagerDialog.java:687-690; SRC ui/filemanager/FileManagerDialog.java:636-650')
e('FileManagerDialog.onOptionsItemSelected', 'FileManagerDialog.returnDirectoryUri', 'CALL', 'Menu ok item (non-SAVE mode) returns the directory uri', evidence='SRC ui/filemanager/FileManagerDialog.java:505-510; SRC ui/filemanager/FileManagerDialog.java:557-568')
e('FileManagerDialog.onItemClicked', 'FileManagerDialog.returnFileUri', 'CALL', 'File click in FILE_CHOOSER_MODE returns the file uri', evidence='SRC ui/filemanager/FileManagerDialog.java:452-455; SRC ui/filemanager/FileManagerDialog.java:593-604')
e('FileManagerDialog.onItemClicked', 'FileManagerDialog.saveCurDirectoryPath', 'CALL', 'File click saves the current directory path', evidence='SRC ui/filemanager/FileManagerDialog.java:454; SRC ui/filemanager/FileManagerDialog.java:464-472')
e('FileManagerDialog.handleAlertDialogEvent', 'FileManagerDialog.showCreateFolderErrDialog', 'CALL', 'Failed create-directory event shows the error dialog', evidence='SRC ui/filemanager/FileManagerDialog.java:331-332; SRC ui/filemanager/FileManagerDialog.java:389-402')
e('FileManagerDialog.lambda$onCreate$0', 'FileManagerDialog.showInputNameDialog', 'CALL', 'Add-fab click lambda shows the input-name dialog', evidence='SRC ui/filemanager/FileManagerDialog.java:172; SRC ui/filemanager/FileManagerDialog.java:243-256')
e('FileManagerDialog.createFile', 'FileManagerDialog.showReplaceFileDialog', 'CALL', 'createFile with an existing name shows the replace dialog', evidence='SRC ui/filemanager/FileManagerDialog.java:576-577; SRC ui/filemanager/FileManagerDialog.java:606-619')
e('FileManagerDialog.handleAlertDialogEvent', 'FileManagerDialog.showSendErrorDialog', 'CALL', 'IOException alert event shows the send-error dialog', evidence='SRC ui/filemanager/FileManagerDialog.java:341; SRC ui/filemanager/FileManagerDialog.java:370-380')
e('FileManagerDialog.onStart', 'FileManagerDialog.subscribeAdapter', 'CALL', 'onStart subscribes the child-nodes stream to the adapter', evidence='SRC ui/filemanager/FileManagerDialog.java:277; SRC ui/filemanager/FileManagerDialog.java:302-309')
e('FileManagerDialog.onStart', 'FileManagerDialog.subscribeAlertDialog', 'CALL', 'onStart subscribes the alert-dialog events', evidence='SRC ui/filemanager/FileManagerDialog.java:276; SRC ui/filemanager/FileManagerDialog.java:297-300')
e('FileManagerDialog.onDestroy', 'FileManagerDialog.unregisterMediaReceiver', 'CALL', 'onDestroy unregisters the media receiver', evidence='SRC ui/filemanager/FileManagerDialog.java:262; SRC ui/filemanager/FileManagerDialog.java:289-295')
e('FileManagerDialog.onCreate', 'FileManagerDialog$1.<init>', 'CALL', 'onCreate creates the filename TextWatcher', evidence='SRC ui/filemanager/FileManagerDialog.java:176; SRC ui/filemanager/FileManagerDialog.java:176-190')
e('FileManagerDialog.onCreate', 'FileManagerDialog$1.afterTextChanged', 'FRAMEWORK', 'TextWatcher dispatch clears the filename error', cls='non_standard', via='TextWatcher dispatch', evidence='INFERRED TextWatcher dispatch; SRC ui/filemanager/FileManagerDialog.java:176; SRC ui/filemanager/FileManagerDialog.java:186-189')
e('FileManagerDialog.onCreate', 'FileManagerDialog$1.beforeTextChanged', 'FRAMEWORK', 'TextWatcher dispatch into the empty before-change slot', cls='non_standard', via='TextWatcher dispatch', evidence='INFERRED TextWatcher dispatch; SRC ui/filemanager/FileManagerDialog.java:176; SRC ui/filemanager/FileManagerDialog.java:178-179')
e('FileManagerDialog.onCreate', 'FileManagerDialog$1.onTextChanged', 'FRAMEWORK', 'TextWatcher dispatch into the empty on-change slot', cls='non_standard', via='TextWatcher dispatch', evidence='INFERRED TextWatcher dispatch; SRC ui/filemanager/FileManagerDialog.java:176; SRC ui/filemanager/FileManagerDialog.java:182-183')
e('FileManagerDialog.onCreate', 'FileManagerDialog$2.<init>', 'CALL', 'onCreate creates the spinner selection listener', evidence='SRC ui/filemanager/FileManagerDialog.java:214; SRC ui/filemanager/FileManagerDialog.java:214-238')
e('FileManagerDialog.onCreate', 'FileManagerDialog$2.onItemSelected', 'FRAMEWORK', 'Spinner dispatch into the selection handler', cls='non_standard', via='Spinner dispatch', evidence='INFERRED Spinner dispatch; SRC ui/filemanager/FileManagerDialog.java:214; SRC ui/filemanager/FileManagerDialog.java:216-233')
e('FileManagerDialog.onCreate', 'FileManagerDialog$2.onNothingSelected', 'FRAMEWORK', 'Spinner dispatch into the empty no-selection slot', cls='non_standard', via='Spinner dispatch', evidence='INFERRED Spinner dispatch; SRC ui/filemanager/FileManagerDialog.java:214; SRC ui/filemanager/FileManagerDialog.java:236-237')
e('FileManagerDialog.<init>', 'FileManagerDialog$3.<init>', 'CALL', 'Field initialiser constructs the current-dir property callback', evidence='SRC ui/filemanager/FileManagerDialog.java:311-317')
e('FileManagerDialog.onStart', 'FileManagerDialog$3.onPropertyChanged', 'FRAMEWORK', 'Observable dispatch retitles the spinner on directory change', cls='non_standard', via='Observable dispatch', evidence='INFERRED Observable dispatch; SRC ui/filemanager/FileManagerDialog.java:278; SRC ui/filemanager/FileManagerDialog.java:314-316')
e('FileManagerDialog.<init>', 'FileManagerDialog$MediaReceiver.<init>', 'CALL', 'Field initialiser constructs the media receiver', evidence='SRC ui/filemanager/FileManagerDialog.java:111; SRC ui/filemanager/FileManagerDialog.java:682-684')
e('FileManagerDialog.registerMediaReceiver', 'FileManagerDialog$MediaReceiver.onReceive', 'FRAMEWORK', 'System broadcast dispatch reloads the spinner', cls='non_standard', via='System broadcast dispatch', evidence='INFERRED broadcast dispatch; SRC ui/filemanager/FileManagerDialog.java:281-287; SRC ui/filemanager/FileManagerDialog.java:687-690')
e('FileManagerViewModel.getChildItems', 'FileManagerNode.<init>', 'CALL', 'getChildItems builds parent, directory and file nodes', evidence='SRC ui/filemanager/FileManagerViewModel.java:127,134,136-137; SRC ui/filemanager/FileManagerNode.java:39-44')
e('FileManagerAdapter.lambda$static$0', 'FileManagerNode.compareTo', 'CALL', 'Directory-first comparator orders nodes by name', evidence='SRC ui/filemanager/FileManagerAdapter.java:57-61; SRC ui/filemanager/FileManagerNode.java:86-89')
e('FileManagerAdapter$1.areContentsTheSame', 'FileManagerNode.equals', 'CALL', 'Diff callback compares old and new nodes', evidence='SRC ui/filemanager/FileManagerAdapter.java:99-102; SRC ui/filemanager/FileManagerNode.java:92-105')
e('FileManagerAdapter$ViewHolder.bind', 'FileManagerNode.getName', 'CALL', 'Bind reads the node name for extension check and label', evidence='SRC ui/filemanager/FileManagerAdapter.java:138,154,157; SRC ui/filemanager/FileManagerNode.java:47-50')
e('FileManagerDialog.onItemClicked', 'FileManagerNode.getType', 'CALL', 'Item click branches on the node type', evidence='SRC ui/filemanager/FileManagerDialog.java:441,452; SRC ui/filemanager/FileManagerNode.java:59-62')
e('FileManagerAdapter$ViewHolder.bind', 'FileManagerNode.isDirectory', 'CALL', 'Bind branches the icon on directory-ness', evidence='SRC ui/filemanager/FileManagerAdapter.java:156; SRC ui/filemanager/FileManagerNode.java:80-83')
e('FileManagerAdapter$ViewHolder.bind', 'FileManagerNode.isEnabled', 'CALL', 'Bind enables the item view from the node flag', evidence='SRC ui/filemanager/FileManagerAdapter.java:135,137; SRC ui/filemanager/FileManagerNode.java:70-73')
e('FileManagerDialog.onCreate', 'FileManagerSpinnerAdapter.<clinit>', 'FRAMEWORK', 'First spinner-adapter construction initialises the class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC ui/filemanager/FileManagerDialog.java:208; SRC ui/filemanager/FileManagerSpinnerAdapter.java:42')
e('FileManagerDialog.onCreate', 'FileManagerSpinnerAdapter.<init>', 'CALL', 'onCreate constructs the storage spinner adapter', evidence='SRC ui/filemanager/FileManagerDialog.java:208; SRC ui/filemanager/FileManagerSpinnerAdapter.java:95-98')

UNREACHABLE.update({
    'FileManagerNode.setEnabled': ('no_trigger_in_app',
        'A1 2026-11-01 saved full-tree grep (src/main, java+res): 12 setEnabled hits, none on a FileManagerNode receiver (FileManagerAdapter.java:135 reads isEnabled() on itemView; ProxySettingsFragment hits are Preference receivers). auto_calls.json: exact dst FileManagerNode.setEnabled 0 edges. Nodes built fully formed via the 3-arg ctor (FileManagerViewModel.java:127,134,136).',
        'SRC ui/filemanager/FileManagerNode.java:75-78; SRC ui/filemanager/FileManagerViewModel.java:127,134,136-137',
        'INFERRED'),
    'FileManagerNode.setName': ('no_trigger_in_app',
        'A1 2026-11-01 saved full-tree grep: 17 setName hits, none on a FileManagerNode- or FileNode-typed receiver (other-class setters, interface decl FileNode.java:40, sibling FileTree.java:131, ViewModel/state receivers). auto_calls.json: exact dst FileManagerNode.setName and FileNode.setName 0 edges. Nodes built fully formed via the 3-arg ctor.',
        'SRC ui/filemanager/FileManagerNode.java:53-56; SRC ui/filemanager/FileManagerViewModel.java:127,134,136-137',
        'INFERRED'),
    'FileManagerNode.setType': ('no_trigger_in_app',
        'A1 2026-11-01 saved full-tree grep: 7 setType hits - definition, interface decl FileNode.java:44, sibling FileTree.java:159, four sharingIntent.setType Intent sites; no node receiver. auto_calls.json: exact dst FileManagerNode.setType and FileNode.setType 0 edges.',
        'SRC ui/filemanager/FileManagerNode.java:65-68',
        'INFERRED'),
    'FileManagerNode.toString': ('no_trigger_in_app',
        'Definition FileManagerNode.java:109-116. Fresh grep across the fetched filemanager files found NO toString() call on a FileManagerNode (the toString() calls in FileManagerDialog are on Editable/Exception objects, not on a node). auto_calls.json: exact dst FileManagerNode.toString 0 edges.',
        'SRC ui/filemanager/FileManagerNode.java:109-116',
        'INFERRED'),
    'FileManagerSpinnerAdapter.addItem': ('no_trigger_in_app',
        'A1 2026-11-01 saved full-tree grep: targeted ".addItem(" returns zero call sites; only definition at FileManagerSpinnerAdapter.java:105; FileManagerDialog.java:210,645 call plural addItems exclusively. auto_calls.json: exact dst addItem 0 edges, 2 addItems edges only.',
        'SRC ui/filemanager/FileManagerSpinnerAdapter.java:105-108; SRC ui/filemanager/FileManagerDialog.java:210,645',
        'INFERRED'),
})

# No part edge points at a method that is UNREACHABLE in this batch, and
# auto_calls.json + javap show no bytecode caller of this batch's
# UNREACHABLE methods, so no SUPPRESS entries apply.
SUPPRESS.update(set())
