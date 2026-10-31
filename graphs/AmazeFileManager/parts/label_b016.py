# ---- Helper batch 016 label part (2025-01-17)
# Classes: ComputerParcelable, ComputerParcelable$1, CopyService, CopyService$1, 
#          CopyService$DoInBackground, CopyService$DoInBackground$Copy

# CopyService - started service for copy/move operations
e('PrepareCopyTask.onPostExecute', 'CopyService.onStartCommand', 'INTENT',
  'PrepareCopyTask creates intent for CopyService and starts it via ServiceWatcherUtil.runService',
  evidence='SRC PrepareCopyTask.java:169-175 creates intent, ServiceWatcherUtil.java:164 calls context.startService')

e('MoveFiles.doInBackground', 'CopyService.onStartCommand', 'INTENT',
  'MoveFiles creates intent for CopyService and starts it via ServiceWatcherUtil.runService',
  evidence='SRC MoveFiles.java:213-219 creates intent and calls ServiceWatcherUtil.runService')

e('CopyService.onStartCommand', 'CopyService$DoInBackground.<init>', 'CALL',
  'onStartCommand instantiates DoInBackground AsyncTask',
  evidence='SRC CopyService.java:159 new DoInBackground(isRootExplorer)')

e('CopyService.onStartCommand', 'CopyService$DoInBackground.doInBackground', 'ASYNC',
  'onStartCommand calls execute on DoInBackground, framework then calls doInBackground',
  evidence='SRC CopyService.java:159 new DoInBackground(...).execute(b), AsyncTask framework invokes doInBackground')

e('CopyService$DoInBackground.doInBackground', 'CopyService$DoInBackground$Copy.<init>', 'CALL',
  'doInBackground instantiates Copy inner class',
  evidence='SRC CopyService.java:253 copy = new Copy()')

e('CopyService$DoInBackground.doInBackground', 'CopyService$DoInBackground$Copy.execute', 'CALL',
  'doInBackground calls execute on Copy instance',
  evidence='SRC CopyService.java:254 copy.execute(sourceFiles, targetPath, move, openMode)')

e('CopyService$DoInBackground.doInBackground', 'CopyService$DoInBackground.findAndReplaceEncryptedEntry', 'CALL',
  'doInBackground iterates sourceFiles and calls findAndReplaceEncryptedEntry for each',
  evidence='SRC CopyService.java:260-264 for loop calling findAndReplaceEncryptedEntry(sourceFile)')

e('CopyService$DoInBackground$Copy.execute', 'CopyService$DoInBackground$Copy.copyFiles', 'CALL',
  'execute iterates sourceFiles and calls copyFiles for non-root files',
  evidence='SRC CopyService.java:382 copyFiles((f1), hFile, progressHandler)')

e('CopyService$DoInBackground$Copy.execute', 'CopyService$DoInBackground$Copy.copyRoot', 'CALL',
  'execute calls copyRoot for files in root mode',
  evidence='SRC CopyService.java:376 copyRoot(f1, hFile, move)')

e('CopyService$DoInBackground$Copy.copyFiles', 'CopyService$DoInBackground$Copy.copyFiles', 'CALL',
  'copyFiles recursively calls itself via lambda for directory children',
  evidence='SRC CopyService.java:459-463 sourceFile.forEachChildrenFile with lambda calling copyFiles')

e('CopyService$DoInBackground.findAndReplaceEncryptedEntry', 'CopyService$DoInBackground.findAndReplaceEncryptedEntry', 'CALL',
  'findAndReplaceEncryptedEntry recursively calls itself via lambda for directory children',
  evidence='SRC CopyService.java:293-297 sourceFile.forEachChildrenFile with lambda calling findAndReplaceEncryptedEntry')

e('CopyService.onCreate', 'CopyService$1.<init>', 'CALL',
  'onCreate instantiates BroadcastReceiver receiver3',
  evidence='SRC CopyService.java:99 registerReceiver(receiver3, ...) where receiver3 is field initialized as new BroadcastReceiver')

e('CopyService$DoInBackground.doInBackground', 'CopyService$DoInBackground.lambda$doInBackground$0', 'CALL',
  'doInBackground sets lambda as progress listener',
  evidence='SRC CopyService.java:241-242 progressHandler.setProgressListener((speed) -> publishResults(...))')

e('CopyService$DoInBackground.doInBackground', 'CopyService$DoInBackground.onPostExecute', 'ASYNC',
  'AsyncTask framework calls onPostExecute after doInBackground returns',
  evidence='SRC CopyService.java:268 doInBackground returns null, framework then invokes onPostExecute at line 271')

e('CopyService$DoInBackground.findAndReplaceEncryptedEntry', 'CopyService$DoInBackground.lambda$findAndReplaceEncryptedEntry$1', 'CALL',
  'findAndReplaceEncryptedEntry uses lambda in forEachChildrenFile',
  evidence='SRC CopyService.java:293-297 sourceFile.forEachChildrenFile(..., file -> { findAndReplaceEncryptedEntry(file); })')

e('CopyService$DoInBackground$Copy.copyFiles', 'CopyService$DoInBackground$Copy.lambda$copyFiles$0', 'CALL',
  'copyFiles uses lambda in forEachChildrenFile for recursive copy',
  evidence='SRC CopyService.java:459-463 sourceFile.forEachChildrenFile(..., file -> { ... copyFiles(file, destFile, progressHandler) })')

# ComputerParcelable - SMB computer data holder
e('SmbSearchDialog.onCreateDialog', 'ComputerParcelable.<init>', 'CALL',
  'SmbSearchDialog creates placeholder ComputerParcelable',
  evidence='SRC SmbSearchDialog.java:78 computers.add(new ComputerParcelable("-1", "-1"))')

e('SubnetScanner.Task.call', 'ComputerParcelable.<init>', 'CALL',
  'SubnetScanner.Task.call creates ComputerParcelable for discovered computers',
  evidence='SRC SubnetScanner.java:56,58,60 return new ComputerParcelable(...)')

e('SmbSearchDialog.onCreateDialog', 'ComputerParcelable.<clinit>', 'FRAMEWORK',
  'Static initializer runs when class is first used in SmbSearchDialog',
  evidence='SRC SmbSearchDialog.java:78 uses ComputerParcelable class, triggering <clinit>')

# CopyService lifecycle and service methods
e('PrepareCopyTask.onPostExecute', 'CopyService.<init>', 'FRAMEWORK',
  'Framework instantiates CopyService when startService is called',
  evidence='SRC PrepareCopyTask.java:175 calls ServiceWatcherUtil.runService, ServiceWatcherUtil.java:164 context.startService, framework instantiates service')

e('CopyService.<init>', 'CopyService.onCreate', 'LIFECYCLE',
  'Framework calls onCreate after service construction',
  evidence='SRC CopyService.java:95-100 defines onCreate; Android service lifecycle')

e('CopyService.onCreate', 'CopyService.onStartCommand', 'LIFECYCLE',
  'Framework calls onStartCommand after onCreate for started service',
  evidence='SRC CopyService.java:103 defines onStartCommand; Android service lifecycle')

e('CopyService.onStartCommand', 'CopyService.onDestroy', 'LIFECYCLE',
  'Framework calls onDestroy when service stops',
  evidence='SRC CopyService.java:195-197 defines onDestroy; Android service lifecycle')

e('AbstractProgressiveService.initNotificationViews', 'CopyService.getNotificationCustomViewSmall', 'CALL',
  'Parent class calls getter in initNotificationViews',
  evidence='SRC AbstractProgressiveService.java:64 calls getNotificationCustomViewSmall')

e('AbstractProgressiveService.initNotificationViews', 'CopyService.getNotificationCustomViewBig', 'CALL',
  'Parent class calls getter in initNotificationViews',
  evidence='SRC AbstractProgressiveService.java:66 calls getNotificationCustomViewBig')

e('AbstractProgressiveService.initNotificationViews', 'CopyService.getNotificationManager', 'CALL',
  'Parent class calls getter in initNotificationViews',
  evidence='SRC AbstractProgressiveService.java:72 calls getNotificationManager')

e('AbstractProgressiveService.initNotificationViews', 'CopyService.getNotificationId', 'CALL',
  'Parent class calls getter in initNotificationViews',
  evidence='SRC AbstractProgressiveService.java:72 calls getNotificationId')

e('AbstractProgressiveService.initNotificationViews', 'CopyService.getNotificationBuilder', 'CALL',
  'Parent class calls getter in initNotificationViews',
  evidence='SRC AbstractProgressiveService.java:72 calls getNotificationBuilder')

e('AbstractProgressiveService.progressHalted', 'CopyService.getNotificationCustomViewSmall', 'CALL',
  'Parent class calls getter in progressHalted',
  evidence='SRC AbstractProgressiveService.java:78 calls getNotificationCustomViewSmall')

e('AbstractProgressiveService.progressHalted', 'CopyService.getNotificationCustomViewBig', 'CALL',
  'Parent class calls getter in progressHalted',
  evidence='SRC AbstractProgressiveService.java:80 calls getNotificationCustomViewBig')

e('AbstractProgressiveService.progressHalted', 'CopyService.getProgressHandler', 'CALL',
  'Parent class calls getter in progressHalted',
  evidence='SRC AbstractProgressiveService.java:79,81 calls getProgressHandler')

e('AbstractProgressiveService.publishResults', 'CopyService.getProgressHandler', 'CALL',
  'Parent class calls getter in publishResults',
  evidence='SRC AbstractProgressiveService.java:93-96 calls getProgressHandler multiple times')

e('AbstractProgressiveService.publishResults', 'CopyService.getTitle', 'CALL',
  'Parent class calls getter in publishResults',
  evidence='SRC AbstractProgressiveService.java:99 calls getTitle')

e('AbstractProgressiveService.publishResults', 'CopyService.getNotificationBuilder', 'CALL',
  'Parent class calls getter in publishResults',
  evidence='SRC AbstractProgressiveService.java:99 calls getNotificationBuilder')

e('AbstractProgressiveService.publishResults', 'CopyService.getNotificationCustomViewBig', 'CALL',
  'Parent class calls getter in publishResults',
  evidence='SRC AbstractProgressiveService.java:107,109,111,120 calls getNotificationCustomViewBig')

e('AbstractProgressiveService.publishResults', 'CopyService.getNotificationCustomViewSmall', 'CALL',
  'Parent class calls getter in publishResults',
  evidence='SRC AbstractProgressiveService.java:108,110 calls getNotificationCustomViewSmall')

e('AbstractProgressiveService.addDatapoint', 'CopyService.getDataPackages', 'CALL',
  'Parent class calls getter in addDatapoint',
  evidence='SRC AbstractProgressiveService.java:177,182 calls getDataPackages')

e('AbstractProgressiveService.addDatapoint', 'CopyService.getProgressListener', 'CALL',
  'Parent class calls getter in addDatapoint',
  evidence='SRC AbstractProgressiveService.java:188-190 calls getProgressListener')

e('ProcessViewerFragment.onViewCreated', 'CopyService.setProgressListener', 'CALL',
  'ProcessViewerFragment sets progress listener on service',
  evidence='SRC ProcessViewerFragment.java:158-160 binds to service and likely calls setProgressListener')

e('CopyService.onCreate', 'CopyService$1.onReceive', 'SYSTEM',
  'Framework calls onReceive when TAG_BROADCAST_COPY_CANCEL broadcast is sent',
  evidence='SRC CopyService.java:99 registerReceiver(receiver3, new IntentFilter(TAG_BROADCAST_COPY_CANCEL)); framework invokes onReceive on broadcast')

# UNREACHABLE methods
UNREACHABLE_PART_016 = {
    'CopyService.onBind': ('no_trigger_in_app', 'CopyService is started via startService, never bound. No bindService calls found in app.', 'SRC CopyService.java:508 defines onBind; grep found no bindService calls to CopyService', 'SOURCE'),
    
    'CopyService.checkFiles': ('no_trigger_in_app', 'Method is not called anywhere in app code. Comment at line 492 says "avoid using the method".', 'SRC CopyService.java:492-517 defines checkFiles; grep found no calls to this method', 'SOURCE'),
    
    'ComputerParcelable.describeContents': ('no_trigger_in_app', 'Parcelable.describeContents is called by framework only during parceling, but ComputerParcelable is never passed in Intent or written to Parcel in app code.', 'SRC ComputerParcelable.java:34-36 defines describeContents; no writeToParcel or intent.putExtra calls found for ComputerParcelable instances', 'SOURCE'),
    
    'ComputerParcelable.writeToParcel': ('no_trigger_in_app', 'writeToParcel is called by framework only during parceling, but ComputerParcelable is never passed in Intent or written to Parcel in app code.', 'SRC ComputerParcelable.java:38-41 defines writeToParcel; no intent.putParcelableExtra or parcel.writeParcelable calls found for ComputerParcelable', 'SOURCE'),
    
    'ComputerParcelable.toString': ('no_trigger_in_app', 'toString is not called on ComputerParcelable instances in app code. ListViewAdapter uses instance fields directly.', 'SRC ComputerParcelable.java:30-32 defines toString; SmbSearchDialog.java:149,171 access f.name and f.addr directly without toString', 'SOURCE'),
    
    'ComputerParcelable.equals': ('no_trigger_in_app', 'equals is not called on ComputerParcelable instances in app code.', 'SRC ComputerParcelable.java:43-47 defines equals; grep found no calls to equals on ComputerParcelable instances', 'SOURCE'),
    
    'ComputerParcelable.hashCode': ('no_trigger_in_app', 'hashCode is not called on ComputerParcelable instances in app code. Not used in collections requiring hashing.', 'SRC ComputerParcelable.java:49-51 defines hashCode; grep found no HashMap/HashSet usage with ComputerParcelable', 'SOURCE'),
    
    'ComputerParcelable$1.<init>': ('no_trigger_in_app', 'CREATOR instance constructor - only invoked if CREATOR is accessed, which happens only during unparceling. No unparceling of ComputerParcelable found.', 'SRC ComputerParcelable.java:19-28 defines CREATOR; grep found no getParcelable for ComputerParcelable', 'SOURCE'),
    
    'ComputerParcelable$1.createFromParcel': ('no_trigger_in_app', 'CREATOR.createFromParcel is called by framework only during unparceling. ComputerParcelable is never read from Parcel in app code.', 'SRC ComputerParcelable.java:21-23 defines createFromParcel; grep found no getParcelable/readParcelable for ComputerParcelable', 'SOURCE'),
    
    'ComputerParcelable$1.newArray': ('no_trigger_in_app', 'CREATOR.newArray is called by framework only during unparceling arrays. ComputerParcelable arrays are never read from Parcel in app code.', 'SRC ComputerParcelable.java:26-28 defines newArray; grep found no getParcelableArrayList or similar for ComputerParcelable', 'SOURCE'),
}
