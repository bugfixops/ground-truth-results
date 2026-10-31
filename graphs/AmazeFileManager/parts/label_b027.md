STATUS: RUNNING 21:46

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| FileUtils.folderSize(File,OnProgressUpdate) | REACHABLE | | Called from CountItemsOrAndSizeTask, HybridFile, PropertiesSheet | SRC CountItemsOrAndSizeTask.java:48; HybridFile.java:563,599; PropertiesSheet.java:71 |
| FileUtils.folderSize(HybridFile,OnProgressUpdate) | REACHABLE | | Called from CountItemsOrAndSizeTask | SRC CountItemsOrAndSizeTask.java:48 |
| FileUtils.folderSize(SmbFile) | REACHABLE | | Called from HybridFile for SMB mode | SRC HybridFile.java:556,592 |
| FileUtils.folderSizeSftp | UNREACHABLE | no_trigger_in_app | Not called by app; HybridFile uses client.size() directly for SFTP | SRC FileUtils.java:150-165; HybridFile.java:578-620 shows SFTP uses client.size() |
| FileUtils.folderSizeCloud | REACHABLE | | Called from HybridFile for cloud storage | SRC HybridFile.java:612 |
| FileUtils.otgFolderSize | REACHABLE | | Called from HybridFile for OTG mode | SRC HybridFile.java:606 |
| FileUtils.getTotalBytes | REACHABLE | | Called from MoveFiles, PrepareCopyTask, CopyService, ZipService | SRC MoveFiles.java:86; PrepareCopyTask.java:118; CopyService.java:237; ZipService.java:217 |
| FileUtils.getBaseFileSize | UNREACHABLE | no_trigger_in_app | Private method called only internally by getTotalBytes and otgFolderSize | SRC FileUtils.java:205-212; internal calls at lines 190,200 |
| FileUtils.scanFile(File,Context) | REACHABLE | | Called from DeleteTask, MoveFiles, MainFragment | SRC DeleteTask.java:155; MoveFiles.java:176,177; MainFragment.java:817,1564 |
| FileUtils.scanFile(Uri,Context) | UNREACHABLE | no_trigger_in_app | Private overload; called only internally from public scanFile methods | SRC FileUtils.java:230-233; internal call at line 273 |
| FileUtils.scanFile(Context,HybridFile[]) | REACHABLE | | Called from Operations | SRC Operations.java:484 |
| FileUtils.scanFile(HybridFile,Context) | REACHABLE | | Called from CopyService, GenericCopyUtil | SRC CopyService.java:437; GenericCopyUtil.java:316 |
| FileUtils.crossfade | REACHABLE | | Called from BottomBar for UI animation | SRC BottomBar.java:135,141 |
| FileUtils.crossfadeInverse | REACHABLE | | Called from BottomBar for inverse animation | SRC BottomBar.java:119 |
| FileUtils.shareCloudFile | REACHABLE | | Called from ItemPopupMenu, MainFragment | SRC ItemPopupMenu.java:87; MainFragment.java:678 |
| FileUtils.shareFiles | REACHABLE | | Called from ItemPopupMenu, MainFragment, AppsAdapter | SRC ItemPopupMenu.java:92; MainFragment.java:682; AppsAdapter.java:185 |
| FileUtils.readableFileSizeFloat | REACHABLE | | Called from ProcessViewerFragment | SRC ProcessViewerFragment.java:201,202,380 |
| FileUtils.installApk | REACHABLE | | Called from GeneralDialogCreation | SRC GeneralDialogCreation.java:916 |
| FileUtils.openunknown(File,Context,boolean,boolean) | REACHABLE | | Called from FileUtils.openFile, MainFragment, TextEditorActivity | SRC FileUtils.java:795; MainFragment.java:743; TextEditorActivity.java:380 |
| FileUtils.openunknown(DocumentFile,Context,boolean,boolean) | REACHABLE | | Called from FileUtils.openFile for OTG | SRC FileUtils.java:822 |
| FileUtils.applyNewDocFlag | UNREACHABLE | no_trigger_in_app | Private helper called only internally by openunknown methods | SRC FileUtils.java:484-493; internal calls at lines 432,436,465,469,600,645 |
| FileUtils.normalizeMediaPath | REACHABLE | | Called internally from fileToContentUri | SRC FileUtils.java:519 |
| FileUtils.fileToContentUri(Context,File,Intent) | REACHABLE | | Called from openunknown, openWith | SRC FileUtils.java:423,591 |
| FileUtils.fileToContentUri(Context,String,boolean,String) | UNREACHABLE | no_trigger_in_app | Private overload; called only internally by public fileToContentUri | SRC FileUtils.java:535-586; internal calls at lines 522,526 |
| FileUtils.openWith(File,Context,boolean) | REACHABLE | | Called from ItemPopupMenu, FileUtils.openFile, FileUtils.openunknown | SRC ItemPopupMenu.java:130; FileUtils.java:798,444 |
| FileUtils.openWith(DocumentFile,Context,boolean) | REACHABLE | | Called from FileUtils.openFile, FileUtils.openunknown for OTG | SRC FileUtils.java:823,479 |
| FileUtils.canGoBack | REACHABLE | | Called from MainFragment | SRC MainFragment.java:1302,1384 |
| FileUtils.getSpaces | REACHABLE | | Called from LoadFolderSpaceDataTask | SRC LoadFolderSpaceDataTask.java:56 |
| FileUtils.copyToClipboard | REACHABLE | | Called from GeneralDialogCreation, GenerateHashesTask, shareCloudFile | SRC GeneralDialogCreation.java:432,438,444,450; GenerateHashesTask.java:102,108; FileUtils.java:346 |
| FileUtils.getFolderNamesInPath | REACHABLE | | Called from BottomBar | SRC BottomBar.java:203 |
| FileUtils.getPathsInPath | REACHABLE | | Called from BottomBar | SRC BottomBar.java:204 |
| FileUtils.canListFiles | REACHABLE | | Called from RootHelper, MainActivity | SRC RootHelper.java:327; MainActivity.java:684 |
| FileUtils.openFile(File,MainActivity,SharedPreferences) | REACHABLE | | Called from MainActivity, Drawer, CompressedExplorerFragment, MainFragment | SRC MainActivity.java:417,747,1579; Drawer.java:540; CompressedExplorerFragment.java:394; MainFragment.java:833,933 |
| FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences) | REACHABLE | | Called from MainFragment for OTG files | SRC MainFragment.java:922 |
| FileUtils.isSelfDefault | UNREACHABLE | no_trigger_in_app | Private helper called only internally by openFile | SRC FileUtils.java:801-811; internal call at line 748 |
| FileUtils.toHybridFileConcurrentRadixTree | REACHABLE | | Called from GeneralDialogCreation | SRC GeneralDialogCreation.java:1120 |
| FileUtils.toHybridFileArrayList | REACHABLE | | Called from GeneralDialogCreation via static import | SRC GeneralDialogCreation.java:1098 |
| FileUtils.parseName | REACHABLE | | Called from RootHelper | SRC RootHelper.java:232,300 |
| FileUtils.getLinkPosition | UNREACHABLE | no_trigger_in_app | Private helper called only internally by parseName | SRC FileUtils.java:950-955; internal call at line 926 |
| FileUtils.getColonPosition | UNREACHABLE | no_trigger_in_app | Private helper called only internally by parseName | SRC FileUtils.java:957-962; internal call at line 916 |
| FileUtils.parse | REACHABLE | | Called from GeneralDialogCreation | SRC GeneralDialogCreation.java:1147 |
| FileUtils.isStorage | REACHABLE | | Called from BottomBar | SRC BottomBar.java:216 |
| FileUtils.isPathAccessible | REACHABLE | | Called from GeneralDialogCreation, Tab, FoldersPref | SRC GeneralDialogCreation.java:1187; Tab.java:42; FoldersPref.java:172,240 |
| FileUtils.isRoot | REACHABLE | | Called internally from isPathAccessible | SRC FileUtils.java:998 |
| FileUtils.hybridListToFileArrayList | REACHABLE | | Called from ZipService | SRC ZipService.java:227 |
| FileUtils.checkForPath | REACHABLE | | Called from Drawer | SRC Drawer.java:569 |
| FileUtils.lambda$otgFolderSize$0 | REACHABLE | | Lambda in otgFolderSize | SRC FileUtils.java:190 |
| FileUtils.lambda$scanFile$1 | REACHABLE | | Lambda in scanFile | SRC FileUtils.java:243 |
| FileUtils.lambda$installApk$2 | REACHABLE | | Lambda in installApk | SRC FileUtils.java:391 |
| FileUtils.lambda$openWith$3 | REACHABLE | | Lambda in openWith(File) | SRC FileUtils.java:593 |
| FileUtils.lambda$openWith$4 | REACHABLE | | Lambda in openWith(DocumentFile) | SRC FileUtils.java:638 |
| FileUtils$1.<init> | REACHABLE | | Constructor for crossfade listener | SRC FileUtils.java:289 |
| FileUtils$1.onAnimationEnd | REACHABLE | | Animation callback | SRC FileUtils.java:291 |
| FileUtils$2.<init> | REACHABLE | | Constructor for crossfadeInverse listener | SRC FileUtils.java:319 |
| FileUtils$2.onAnimationEnd | REACHABLE | | Animation callback | SRC FileUtils.java:321 |
| FileUtils$3.<init> | REACHABLE | | Constructor for shareCloudFile AsyncTask | SRC FileUtils.java:333 |
| FileUtils$3.doInBackground | REACHABLE | | AsyncTask background execution | SRC FileUtils.java:336 |
| FileUtils$3.onPostExecute | REACHABLE | | AsyncTask completion | SRC FileUtils.java:343 |
| FileUtils$4.<init> | REACHABLE | | Constructor for openFile timer | SRC FileUtils.java:768 |
| FileUtils$4.onTick | REACHABLE | | Timer tick callback | SRC FileUtils.java:770 |
| FileUtils$4.onFinish | REACHABLE | | Timer finish callback | SRC FileUtils.java:779 |
| FileUtils$5.<init> | REACHABLE | | Constructor for checkForPath callback | SRC FileUtils.java:1027 |
| FileUtils$5.exists | REACHABLE | | Callback for existing file | SRC FileUtils.java:1029 |
| FileUtils$5.launchSAF | REACHABLE | | Callback for SAF launch (single file) | SRC FileUtils.java:1033-1035 |
| FileUtils$5.launchSAF | REACHABLE | | Callback for SAF launch (two files) | SRC FileUtils.java:1037-1039 |
| FileUtils$5.done | REACHABLE | | Callback for completion | SRC FileUtils.java:1042 |
| FileUtils$5.invalidName | REACHABLE | | Callback for invalid name | SRC FileUtils.java:1046 |
| FileUtils.<init> | UNREACHABLE | no_trigger_in_app | Utility class never instantiated | SRC FileUtils.java:96 class has only static methods |
| FileUtils.<clinit> | UNREACHABLE | framework_never_calls | Static initializer; auto-runs on class load | SRC FileUtils.java:494-499 static fields |

STATUS: DONE 21:52
