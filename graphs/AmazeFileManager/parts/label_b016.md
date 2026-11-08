STATUS: RUNNING 21:40

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| CopyService.<init> | REACHABLE | | Framework instantiates service when startService called | SRC CopyService.java:66 class declaration; framework constructs service |
| CopyService.onCreate | REACHABLE | | Service lifecycle method called by framework after construction | SRC CopyService.java:95-100 |
| CopyService.onStartCommand | REACHABLE | | Service started via startService from PrepareCopyTask and MoveFiles | SRC PrepareCopyTask.java:169-175, MoveFiles.java:213-219, ServiceWatcherUtil.java:164 context.startService |
| CopyService.onBind | UNREACHABLE | no_trigger_in_app | CopyService is started via startService, never bound. No bindService calls found. | SRC CopyService.java:508, grep found no bindService calls to CopyService |
| CopyService.onDestroy | REACHABLE | | Service lifecycle method called by framework when service stops | SRC CopyService.java:195-197 |
| CopyService.getNotificationManager | REACHABLE | | Called from parent AbstractProgressiveService.initNotificationViews and progressHalted | SRC AbstractProgressiveService.java:72 getNotificationManager() |
| CopyService.getNotificationBuilder | REACHABLE | | Called from parent AbstractProgressiveService methods | SRC AbstractProgressiveService.java:72,99 getNotificationBuilder() |
| CopyService.getNotificationId | REACHABLE | | Called from parent AbstractProgressiveService.initNotificationViews | SRC AbstractProgressiveService.java:72 getNotificationId() |
| CopyService.getNotificationCustomViewSmall | REACHABLE | | Called from parent AbstractProgressiveService.initNotificationViews and publishResults | SRC AbstractProgressiveService.java:64,78,108,110 getNotificationCustomViewSmall() |
| CopyService.getNotificationCustomViewBig | REACHABLE | | Called from parent AbstractProgressiveService.initNotificationViews and publishResults | SRC AbstractProgressiveService.java:66,80,107,109,111,120 getNotificationCustomViewBig() |
| CopyService.getTitle | REACHABLE | | Called from parent AbstractProgressiveService.publishResults | SRC AbstractProgressiveService.java:99 getTitle(move) |
| CopyService.getProgressListener | REACHABLE | | Called from parent AbstractProgressiveService.addDatapoint | SRC AbstractProgressiveService.java:188-190 getProgressListener() |
| CopyService.setProgressListener | REACHABLE | | Called from ProcessViewerFragment when binding to service | SRC ProcessViewerFragment.java:158-160 binds to service, AbstractProgressiveService.java:52 abstract declaration |
| CopyService.getDataPackages | REACHABLE | | Called from parent AbstractProgressiveService.addDatapoint | SRC AbstractProgressiveService.java:177,182 getDataPackages() |
| CopyService.getProgressHandler | REACHABLE | | Called from parent AbstractProgressiveService.progressHalted and publishResults | SRC AbstractProgressiveService.java:79,81,93-96 getProgressHandler() |
| CopyService.checkFiles | UNREACHABLE | no_trigger_in_app | Method not called anywhere. Comment at line 492 says "avoid using the method". | SRC CopyService.java:492-517 defines checkFiles, grep found no calls |
| CopyService$1.<init> | REACHABLE | | BroadcastReceiver field receiver3 is instantiated when class loads | SRC CopyService.java:99 registerReceiver(receiver3, ...) where receiver3 is field |
| CopyService$1.onReceive | REACHABLE | | Framework calls when TAG_BROADCAST_COPY_CANCEL broadcast sent | SRC CopyService.java:99 registerReceiver with IntentFilter, ProcessViewerFragment.java:251 sends broadcast |
| CopyService$DoInBackground.<init> | REACHABLE | | Instantiated in CopyService.onStartCommand | SRC CopyService.java:159 new DoInBackground(isRootExplorer) |
| CopyService$DoInBackground.doInBackground | REACHABLE | | AsyncTask lifecycle method, framework calls after execute() | SRC CopyService.java:159 execute(b), framework invokes doInBackground; CopyService.java:230-268 |
| CopyService$DoInBackground.onPostExecute | REACHABLE | | AsyncTask lifecycle method, framework calls after doInBackground returns | SRC CopyService.java:268 doInBackground returns null, framework calls onPostExecute at 271-281 |
| CopyService$DoInBackground.findAndReplaceEncryptedEntry | REACHABLE | | Called from doInBackground for each source file | SRC CopyService.java:260-264 for loop calling findAndReplaceEncryptedEntry |
| CopyService$DoInBackground.lambda$doInBackground$0 | REACHABLE | | Lambda set as progress listener in doInBackground | SRC CopyService.java:241-242 setProgressListener((speed) -> publishResults(...)) |
| CopyService$DoInBackground.lambda$findAndReplaceEncryptedEntry$1 | REACHABLE | | Lambda used in forEachChildrenFile within findAndReplaceEncryptedEntry | SRC CopyService.java:293-297 forEachChildrenFile(..., file -> findAndReplaceEncryptedEntry(file)) |
| CopyService$DoInBackground$Copy.<init> | REACHABLE | | Instantiated in DoInBackground.doInBackground | SRC CopyService.java:253 copy = new Copy() |
| CopyService$DoInBackground$Copy.execute | REACHABLE | | Called from DoInBackground.doInBackground | SRC CopyService.java:254 copy.execute(sourceFiles, targetPath, move, openMode) |
| CopyService$DoInBackground$Copy.copyFiles | REACHABLE | | Called from execute for each source file and recursively for directories | SRC CopyService.java:382 copyFiles((f1), hFile, progressHandler), 463 recursive call |
| CopyService$DoInBackground$Copy.copyRoot | REACHABLE | | Called from execute when source or target is in root mode | SRC CopyService.java:376 copyRoot(f1, hFile, move) |
| CopyService$DoInBackground$Copy.lambda$copyFiles$0 | REACHABLE | | Lambda in copyFiles forEachChildrenFile for recursive directory copy | SRC CopyService.java:459-463 forEachChildrenFile(..., file -> copyFiles(file, ...)) |
| ComputerParcelable.<init> (String,String) | REACHABLE | | Public constructor called from SmbSearchDialog and SubnetScanner.Task.call | SRC SmbSearchDialog.java:78 new ComputerParcelable("-1","-1"), SubnetScanner.java:56,58,60 new ComputerParcelable(...) |
| ComputerParcelable.<init> (Parcel) | UNREACHABLE | no_trigger_in_app | Private Parcel constructor only called from CREATOR.createFromParcel, which is never invoked (no unparceling) | SRC ComputerParcelable.java:54-57 private constructor, grep found no getParcelable for ComputerParcelable |
| ComputerParcelable.<clinit> | REACHABLE | | Static initializer runs when class first used | SRC SmbSearchDialog.java:78 uses ComputerParcelable, triggering <clinit> for CREATOR field |
| ComputerParcelable.describeContents | UNREACHABLE | no_trigger_in_app | Parcelable method only called during parceling, but ComputerParcelable never parceled in app | SRC ComputerParcelable.java:34-36, grep found no writeToParcel or putExtra for ComputerParcelable |
| ComputerParcelable.writeToParcel | UNREACHABLE | no_trigger_in_app | Called by framework only during parceling, but ComputerParcelable never passed in Intent or parceled | SRC ComputerParcelable.java:38-41, grep found no putParcelableExtra for ComputerParcelable |
| ComputerParcelable.toString | UNREACHABLE | no_trigger_in_app | toString not called on instances; ListViewAdapter accesses fields directly | SRC ComputerParcelable.java:30-32, SmbSearchDialog.java:149,171 access f.name/f.addr directly |
| ComputerParcelable.equals | UNREACHABLE | no_trigger_in_app | equals not called on ComputerParcelable instances in app code | SRC ComputerParcelable.java:43-47, grep found no equals calls |
| ComputerParcelable.hashCode | UNREACHABLE | no_trigger_in_app | hashCode not called; not used in collections requiring hashing | SRC ComputerParcelable.java:49-51, grep found no HashMap/HashSet with ComputerParcelable |
| ComputerParcelable$1.<init> | UNREACHABLE | no_trigger_in_app | CREATOR constructor only invoked during unparceling, which never happens | SRC ComputerParcelable.java:19-28 CREATOR field, grep found no getParcelable |
| ComputerParcelable$1.createFromParcel | UNREACHABLE | no_trigger_in_app | CREATOR method called only during unparceling, ComputerParcelable never read from Parcel | SRC ComputerParcelable.java:21-23, grep found no getParcelable/readParcelable |
| ComputerParcelable$1.newArray | UNREACHABLE | no_trigger_in_app | CREATOR method called only when unparceling arrays, never happens in app | SRC ComputerParcelable.java:26-28, grep found no getParcelableArrayList for ComputerParcelable |

STATUS: DONE 21:44
