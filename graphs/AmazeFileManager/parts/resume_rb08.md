STATUS: RUNNING 18:46

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| EncryptService$BackgroundTask.doInBackground | REACHABLE | | AsyncTask.execute runs doInBackground on worker thread, called from onStartCommand | SRC EncryptService.java:115, 171-193 |
| EncryptService$BackgroundTask.lambda$doInBackground$0 | REACHABLE | | Lambda expression in setProgressListener call inside doInBackground | SRC EncryptService.java:177-178 |
| EncryptService$BackgroundTask.onPostExecute | REACHABLE | | AsyncTask calls onPostExecute on main thread after doInBackground completes | SRC EncryptService.java:195-205 |
| EncryptService.onBind | REACHABLE | | Service.onBind called when client binds to EncryptService | SRC EncryptService.java:207-209 |
| EncryptService.onDestroy | REACHABLE | | Service.onDestroy called when service destroyed | SRC EncryptService.java:214-217 |
| EncryptService.setProgressListener | REACHABLE | | setProgressListener called to set progress callback | SRC EncryptService.java:159-161 |
| ExtractService$1.onReceive | REACHABLE | | BroadcastReceiver.onReceive called when TAG_BROADCAST_EXTRACT_CANCEL received | SRC ExtractService.java:86, 406-410 |
| ExtractService.onBind | REACHABLE | | Service.onBind called when client binds to ExtractService | SRC ExtractService.java:412-414 |
| ExtractService.onDestroy | REACHABLE | | Service.onDestroy called when service destroyed | SRC ExtractService.java:206-208 |
| FastScroller.<init>(Context,AttributeSet) | REACHABLE | | FastScroller constructor called when inflating from XML layout | SRC FastScroller.java:35-38 |
| FastScroller.<init>(Context,AttributeSet,int) | REACHABLE | | FastScroller constructor delegation | SRC FastScroller.java:40-43 |
| FastScroller.getRelativeTouchPosition | REACHABLE | | getRelativeTouchPosition called from onTouchEvent | SRC FastScroller.java:102, 143-146 |
| FastScroller.onTouchEvent | REACHABLE | | View.onTouchEvent dispatched by framework when FastScroller touched | SRC FastScroller.java:98-118 |
| FastScroller.setRecyclerViewPosition | REACHABLE | | setRecyclerViewPosition called from onTouchEvent | SRC FastScroller.java:105, 154-159 |
| FileHandler.handleMessage | REACHABLE | | Handler.handleMessage called when message posted to FileHandler | SRC FileHandler.java:30-75 |
| FileUtil$1.<init> | REACHABLE | | Anonymous class constructor in AppConfig.runInParallel call | SRC FileUtil.java:196 |
| FileUtil$MediaFile.<clinit> | UNREACHABLE | closed_by_api_level | MediaFile static initializer; MediaFile workaround only for API < 29 (Kitkat/Lollipop), usage guarded by API checks | SRC FileUtil.java:982-1228 |
| FileUtil$MediaFile.<init> | REACHABLE | | MediaFile constructor called in mkdir for MediaStore workaround | SRC FileUtil.java:1016-1021, 1198 |
| FileUtil$MediaFile.delete | REACHABLE | | delete called on MediaFile instance from mkdir | SRC FileUtil.java:1198, 1030-1062 |
| FileUtil$MediaFile.getExternalFilesDir | REACHABLE | | getExternalFilesDir called from installTemporaryTrack | SRC FileUtil.java:987-1009, 1140 |
| FileUtil$MediaFile.getFile | REACHABLE | | getFile returns internal file reference | SRC FileUtil.java:1066-1068 |
| FileUtil$MediaFile.getTemporaryAlbumId | REACHABLE | | getTemporaryAlbumId called from mkdir | SRC FileUtil.java:1182, 1071-1131 |
| FileUtil$MediaFile.installTemporaryTrack | REACHABLE | | installTemporaryTrack called from getTemporaryAlbumId | SRC FileUtil.java:1073, 1135-1174 |
| FileUtil$MediaFile.mkdir | REACHABLE | | mkdir called on MediaFile instance | SRC FileUtil.java:1177-1200 |
| FileUtil$MediaFile.write | REACHABLE | | write called on MediaFile instance to get OutputStream | SRC FileUtil.java:1205-1228 |
| FileUtil.<init> | REACHABLE | | FileUtil constructor (abstract class, subclasses may be constructed) | SRC FileUtil.java:77 |
| FileUtil.copyDummyFile | REACHABLE | | copyDummyFile called from copyDummyFiles | SRC FileUtil.java:888-930, 973-974 |
| FileUtil.copyDummyFiles | REACHABLE | | copyDummyFiles called from MediaStore workaround path | SRC FileUtil.java:971-979 |
| FileUtil.getTempFile | REACHABLE | | getTempFile returns temp file in external files dir | SRC FileUtil.java:476-479 |
| FileUtil.mkfile | REACHABLE | | mkfile creates file using normal API or SAF or MediaStoreHack | SRC FileUtil.java:550-589 |
| FileUtil.writeUriToStorage | REACHABLE | | writeUriToStorage writes URI streams from external app to storage | SRC FileUtil.java:196-361 |
| FileUtils$5.launchSAF(HybridFile) | REACHABLE | | launchSAF single-param callback method in Operations.ErrorCallBack | SRC FileUtils.java:1026-1049, 1035-1036 |
| FileUtils$5.launchSAF(HybridFile,HybridFile) | REACHABLE | | launchSAF two-param callback method in Operations.ErrorCallBack | SRC FileUtils.java:1026-1049, 1040-1041 |
| FileUtils.canGoBack | REACHABLE | | canGoBack checks if navigation back is possible | SRC FileUtils.java:679-693 |
| FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences) | REACHABLE | | openFile opens DocumentFile, calls openunknown | SRC FileUtils.java:816-821 |
| FileUtils.openunknown(DocumentFile,Context,boolean,boolean) | REACHABLE | | openunknown opens file with appropriate app or chooser | SRC FileUtils.java:455-543 |
| FileUtils.readableFileSizeFloat | REACHABLE | | readableFileSizeFloat converts size to human-readable float | SRC FileUtils.java:379-404 |
| FileUtils.scanFile(Context,HybridFile[]) | REACHABLE | | scanFile triggers media scanner for multiple files | SRC FileUtils.java:242-259 |
| Folder.toString | UNREACHABLE | no_trigger_in_app | sevenz library class (Apache Commons Compress); Folder class not found in app src/main/java | INFERRED library source not in dataset |
| FoldersPref.onResume | REACHABLE | | Fragment.onResume called by framework after onCreate | SRC FoldersPref.java:69-72 |

STATUS: DONE 18:50
