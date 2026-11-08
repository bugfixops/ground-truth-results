# ---- Helper batch_027 label part (2026-10-27)
# FileUtils - 53 methods

# FileUtils.folderSize(File,OnProgressUpdate) - called from CountItemsOrAndSizeTask, HybridFile, PropertiesSheet
e('CountItemsOrAndSizeTask.doInBackground', 'FileUtils.folderSize', 'CALL', 'computes folder size',
  evidence='SRC CountItemsOrAndSizeTask.java:48')
e('HybridFile.folderSize', 'FileUtils.folderSize', 'CALL', 'delegates to FileUtils for File mode',
  evidence='SRC HybridFile.java:563,599')
e('PropertiesSheet.updateViews', 'FileUtils.folderSize', 'CALL', 'gets folder size for display',
  evidence='SRC PropertiesSheet.java:71')

# FileUtils.folderSize(HybridFile,OnProgressUpdate) - called from CountItemsOrAndSizeTask
e('CountItemsOrAndSizeTask.doInBackground', 'FileUtils.folderSize', 'CALL', 'computes hybrid file folder size',
  evidence='SRC CountItemsOrAndSizeTask.java:48')

# FileUtils.folderSize(SmbFile) - called from HybridFile
e('HybridFile.folderSize', 'FileUtils.folderSize', 'CALL', 'computes SMB folder size',
  evidence='SRC HybridFile.java:556,592')

# FileUtils.folderSizeCloud - called from HybridFile
e('HybridFile.folderSize', 'FileUtils.folderSizeCloud', 'CALL', 'computes cloud storage folder size',
  evidence='SRC HybridFile.java:612')

# FileUtils.otgFolderSize - called from HybridFile
e('HybridFile.folderSize', 'FileUtils.otgFolderSize', 'CALL', 'computes OTG folder size',
  evidence='SRC HybridFile.java:606')

# FileUtils.getTotalBytes - called from MoveFiles, PrepareCopyTask, CopyService, ZipService
e('MoveFiles.doInBackground', 'FileUtils.getTotalBytes', 'CALL', 'calculates total bytes for move operation',
  evidence='SRC MoveFiles.java:86')
e('PrepareCopyTask.doInBackground', 'FileUtils.getTotalBytes', 'CALL', 'calculates total bytes for copy operation',
  evidence='SRC PrepareCopyTask.java:118')
e('CopyService.onStartCommand', 'FileUtils.getTotalBytes', 'CALL', 'calculates total size of files to copy',
  evidence='SRC CopyService.java:237')
e('ZipService.onStartCommand', 'FileUtils.getTotalBytes', 'CALL', 'calculates total bytes for zip operation',
  evidence='SRC ZipService.java:217')

# FileUtils.scanFile(File,Context) - called from DeleteTask, MoveFiles, MainFragment
e('DeleteTask.doInBackground', 'FileUtils.scanFile', 'CALL', 'triggers media scan after deletion',
  evidence='SRC DeleteTask.java:155')
e('MoveFiles.doInBackground', 'FileUtils.scanFile', 'CALL', 'triggers media scan after move',
  evidence='SRC MoveFiles.java:176,177')
e('MainFragment.addShortcut', 'FileUtils.scanFile', 'CALL', 'scans file for media',
  evidence='SRC MainFragment.java:817,1564')

# FileUtils.scanFile(Context,HybridFile[]) - called from Operations
e('Operations.deleteFile', 'FileUtils.scanFile', 'CALL', 'triggers media scan for hybrid files',
  evidence='SRC Operations.java:484')

# FileUtils.scanFile(HybridFile,Context) - called from CopyService, GenericCopyUtil and internally
e('CopyService.onCopyDone', 'FileUtils.scanFile', 'CALL', 'scans copied file',
  evidence='SRC CopyService.java:437')
e('GenericCopyUtil.finishCopy', 'FileUtils.scanFile', 'CALL', 'scans file after copy completion',
  evidence='SRC GenericCopyUtil.java:316')

# FileUtils.crossfade - called from BottomBar
e('BottomBar.updatePath', 'FileUtils.crossfade', 'CALL', 'animates UI transition',
  evidence='SRC BottomBar.java:135,141')

# FileUtils.crossfadeInverse - called from BottomBar
e('BottomBar.updatePath', 'FileUtils.crossfadeInverse', 'CALL', 'animates inverse UI transition',
  evidence='SRC BottomBar.java:119')

# FileUtils.shareCloudFile - called from ItemPopupMenu, MainFragment
e('ItemPopupMenu.onMenuItemClick', 'FileUtils.shareCloudFile', 'CALL', 'shares cloud file link',
  evidence='SRC ItemPopupMenu.java:87')
e('MainFragment.generalShare', 'FileUtils.shareCloudFile', 'CALL', 'shares cloud file from main fragment',
  evidence='SRC MainFragment.java:678')

# FileUtils.shareFiles - called from ItemPopupMenu, MainFragment, AppsAdapter
e('ItemPopupMenu.onMenuItemClick', 'FileUtils.shareFiles', 'CALL', 'shares files via intent',
  evidence='SRC ItemPopupMenu.java:92')
e('MainFragment.generalShare', 'FileUtils.shareFiles', 'CALL', 'shares files from main fragment',
  evidence='SRC MainFragment.java:682')
e('AppsAdapter.onClick', 'FileUtils.shareFiles', 'CALL', 'shares app files',
  evidence='SRC AppsAdapter.java:185')

# FileUtils.readableFileSizeFloat - called from ProcessViewerFragment
e('ProcessViewerFragment.addEntry', 'FileUtils.readableFileSizeFloat', 'CALL', 'formats file size for display',
  evidence='SRC ProcessViewerFragment.java:201,202,380')

# FileUtils.installApk - called from GeneralDialogCreation
e('GeneralDialogCreation.showPackageDialog', 'FileUtils.installApk', 'CALL', 'installs APK file',
  evidence='SRC GeneralDialogCreation.java:916')

# FileUtils.openunknown(File,Context,boolean,boolean) - called from FileUtils.openFile, MainFragment, TextEditorActivity
e('FileUtils.openFile', 'FileUtils.openunknown', 'CALL', 'opens file with unknown type',
  evidence='SRC FileUtils.java:795,420')
e('MainFragment.onClick', 'FileUtils.openunknown', 'CALL', 'opens file from main fragment',
  evidence='SRC MainFragment.java:743')
e('TextEditorActivity.loadedFile', 'FileUtils.openunknown', 'CALL', 'opens file after editing',
  evidence='SRC TextEditorActivity.java:380')

# FileUtils.openunknown(DocumentFile,Context,boolean,boolean) - called from FileUtils.openFile
e('FileUtils.openFile', 'FileUtils.openunknown', 'CALL', 'opens OTG file with unknown type',
  evidence='SRC FileUtils.java:822,455')

# FileUtils.normalizeMediaPath - only called internally by fileToContentUri
e('FileUtils.fileToContentUri', 'FileUtils.normalizeMediaPath', 'CALL', 'normalizes path for media query',
  evidence='SRC FileUtils.java:519,500')

# FileUtils.fileToContentUri(Context,File,Intent) - called from openunknown, openWith
e('FileUtils.openunknown', 'FileUtils.fileToContentUri', 'CALL', 'converts file to content URI',
  evidence='SRC FileUtils.java:423,516')
e('FileUtils.openWith', 'FileUtils.fileToContentUri', 'CALL', 'gets content URI for file',
  evidence='SRC FileUtils.java:591,516')

# FileUtils.openWith(File,Context,boolean) - called from ItemPopupMenu, FileUtils.openFile
e('ItemPopupMenu.onMenuItemClick', 'FileUtils.openWith', 'CALL', 'opens file with app chooser',
  evidence='SRC ItemPopupMenu.java:130')
e('FileUtils.openFile', 'FileUtils.openWith', 'CALL', 'shows app chooser',
  evidence='SRC FileUtils.java:798,588')
e('FileUtils.openunknown', 'FileUtils.openWith', 'CALL', 'fallback when no app found',
  evidence='SRC FileUtils.java:444,420')

# FileUtils.openWith(DocumentFile,Context,boolean) - called from FileUtils.openFile, FileUtils.openunknown
e('FileUtils.openFile', 'FileUtils.openWith', 'CALL', 'opens OTG file with chooser',
  evidence='SRC FileUtils.java:823,634')
e('FileUtils.openunknown', 'FileUtils.openWith', 'CALL', 'fallback for OTG file',
  evidence='SRC FileUtils.java:479,455')

# FileUtils.canGoBack - called from MainFragment
e('MainFragment.goBack', 'FileUtils.canGoBack', 'CALL', 'checks if navigation back is possible',
  evidence='SRC MainFragment.java:1302,1384')

# FileUtils.getSpaces - called from LoadFolderSpaceDataTask
e('LoadFolderSpaceDataTask.doInBackground', 'FileUtils.getSpaces', 'CALL', 'gets storage space info',
  evidence='SRC LoadFolderSpaceDataTask.java:56')

# FileUtils.copyToClipboard - called from GeneralDialogCreation, GenerateHashesTask, shareCloudFile
e('GeneralDialogCreation.showPropertiesDialog', 'FileUtils.copyToClipboard', 'CALL', 'copies properties to clipboard',
  evidence='SRC GeneralDialogCreation.java:432,438,444,450')
e('GenerateHashesTask.onPostExecute', 'FileUtils.copyToClipboard', 'CALL', 'copies hash to clipboard',
  evidence='SRC GenerateHashesTask.java:102,108')
e('FileUtils.shareCloudFile', 'FileUtils.copyToClipboard', 'CALL', 'copies cloud link to clipboard',
  evidence='SRC FileUtils.java:346,332')

# FileUtils.getFolderNamesInPath - called from BottomBar
e('BottomBar.updatePath', 'FileUtils.getFolderNamesInPath', 'CALL', 'gets folder names for breadcrumb',
  evidence='SRC BottomBar.java:203')

# FileUtils.getPathsInPath - called from BottomBar
e('BottomBar.updatePath', 'FileUtils.getPathsInPath', 'CALL', 'gets paths for breadcrumb navigation',
  evidence='SRC BottomBar.java:204')

# FileUtils.canListFiles - called from RootHelper, MainActivity
e('RootHelper.getFilesList', 'FileUtils.canListFiles', 'CALL', 'checks if directory is readable',
  evidence='SRC RootHelper.java:327')
e('MainActivity.getStorageDirectories', 'FileUtils.canListFiles', 'CALL', 'validates storage directories',
  evidence='SRC MainActivity.java:684')

# FileUtils.openFile(File,MainActivity,SharedPreferences) - called from MainActivity, Drawer, CompressedExplorerFragment, MainFragment
e('MainActivity.onNewIntent', 'FileUtils.openFile', 'CALL', 'opens file from intent',
  evidence='SRC MainActivity.java:417,747,1579')
e('Drawer.onClickListener', 'FileUtils.openFile', 'CALL', 'opens file from drawer',
  evidence='SRC Drawer.java:540')
e('CompressedExplorerFragment.open', 'FileUtils.openFile', 'CALL', 'opens extracted file',
  evidence='SRC CompressedExplorerFragment.java:394')
e('MainFragment.onListItemClicked', 'FileUtils.openFile', 'CALL', 'opens clicked file',
  evidence='SRC MainFragment.java:833,933')

# FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences) - called from MainFragment
e('MainFragment.onListItemClicked', 'FileUtils.openFile', 'CALL', 'opens OTG file',
  evidence='SRC MainFragment.java:922')

# FileUtils.toHybridFileConcurrentRadixTree - called from GeneralDialogCreation
e('GeneralDialogCreation.showHiddenDialog', 'FileUtils.toHybridFileConcurrentRadixTree', 'CALL', 'converts hidden files tree',
  evidence='SRC GeneralDialogCreation.java:1120')

# FileUtils.toHybridFileArrayList - called from GeneralDialogCreation (static import)
e('GeneralDialogCreation.showHistoryDialog', 'FileUtils.toHybridFileArrayList', 'CALL', 'converts history list',
  evidence='SRC GeneralDialogCreation.java:1098')

# FileUtils.parseName - called from RootHelper
e('RootHelper.getFilesList', 'FileUtils.parseName', 'CALL', 'parses ls output line',
  evidence='SRC RootHelper.java:232,300')

# FileUtils.parse - called from GeneralDialogCreation
e('GeneralDialogCreation.showPermissionsDialog', 'FileUtils.parse', 'CALL', 'parses permission string',
  evidence='SRC GeneralDialogCreation.java:1147')

# FileUtils.isStorage - called from BottomBar
e('BottomBar.updatePath', 'FileUtils.isStorage', 'CALL', 'checks if path is storage root',
  evidence='SRC BottomBar.java:216')

# FileUtils.isPathAccessible - called from GeneralDialogCreation, Tab, FoldersPref
e('GeneralDialogCreation.showSMBDialog', 'FileUtils.isPathAccessible', 'CALL', 'validates path accessibility',
  evidence='SRC GeneralDialogCreation.java:1187')
e('Tab.getTab', 'FileUtils.isPathAccessible', 'CALL', 'checks if tab path is accessible',
  evidence='SRC Tab.java:42')
e('FoldersPref.onPreferenceChange', 'FileUtils.isPathAccessible', 'CALL', 'validates folder preference',
  evidence='SRC FoldersPref.java:172,240')

# FileUtils.isRoot - called internally from isPathAccessible
e('FileUtils.isPathAccessible', 'FileUtils.isRoot', 'CALL', 'checks if path is root',
  evidence='SRC FileUtils.java:998')

# FileUtils.hybridListToFileArrayList - called from ZipService
e('ZipService.onStartCommand', 'FileUtils.hybridListToFileArrayList', 'CALL', 'converts for zip operation',
  evidence='SRC ZipService.java:227')

# FileUtils.checkForPath - called from Drawer
e('Drawer.onBookmarkClick', 'FileUtils.checkForPath', 'CALL', 'verifies bookmark path exists',
  evidence='SRC Drawer.java:569')

# Lambdas - reached when their enclosing methods are called
e('FileUtils.otgFolderSize', 'FileUtils.lambda$otgFolderSize$0', 'CALL', 'lambda for OTG file size calculation',
  evidence='SRC FileUtils.java:190')
e('FileUtils.scanFile', 'FileUtils.lambda$scanFile$1', 'CALL', 'lambda for async media scan',
  evidence='SRC FileUtils.java:243')
e('FileUtils.installApk', 'FileUtils.lambda$installApk$2', 'CALL', 'lambda for permission callback',
  evidence='SRC FileUtils.java:391')
e('FileUtils.openWith', 'FileUtils.lambda$openWith$3', 'CALL', 'lambda for file type selection',
  evidence='SRC FileUtils.java:593')
e('FileUtils.openWith', 'FileUtils.lambda$openWith$4', 'CALL', 'lambda for DocumentFile type selection',
  evidence='SRC FileUtils.java:638')

# Inner classes - anonymous classes and their methods
e('FileUtils.crossfade', 'FileUtils$1.<init>', 'CALL', 'creates animator listener',
  evidence='SRC FileUtils.java:289')
e('FileUtils$1.<init>', 'FileUtils$1.onAnimationEnd', 'FRAMEWORK', 'animation callback',
  evidence='SRC FileUtils.java:291 defines AnimatorListenerAdapter callback')
e('FileUtils.crossfadeInverse', 'FileUtils$2.<init>', 'CALL', 'creates animator listener',
  evidence='SRC FileUtils.java:319')
e('FileUtils$2.<init>', 'FileUtils$2.onAnimationEnd', 'FRAMEWORK', 'animation callback',
  evidence='SRC FileUtils.java:321 defines AnimatorListenerAdapter callback')
e('FileUtils.shareCloudFile', 'FileUtils$3.<init>', 'CALL', 'creates async task',
  evidence='SRC FileUtils.java:333')
e('FileUtils$3.<init>', 'FileUtils$3.doInBackground', 'FRAMEWORK', 'async task execution',
  evidence='SRC FileUtils.java:336 defines AsyncTask.doInBackground')
e('FileUtils$3.<init>', 'FileUtils$3.onPostExecute', 'FRAMEWORK', 'async task completion',
  evidence='SRC FileUtils.java:343 defines AsyncTask.onPostExecute')
e('FileUtils.openFile', 'FileUtils$4.<init>', 'CALL', 'creates countdown timer',
  evidence='SRC FileUtils.java:768')
e('FileUtils$4.<init>', 'FileUtils$4.onTick', 'FRAMEWORK', 'timer tick callback',
  evidence='SRC FileUtils.java:770 defines CountDownTimer.onTick')
e('FileUtils$4.<init>', 'FileUtils$4.onFinish', 'FRAMEWORK', 'timer finish callback',
  evidence='SRC FileUtils.java:779 defines CountDownTimer.onFinish')
e('FileUtils.checkForPath', 'FileUtils$5.<init>', 'CALL', 'creates error callback',
  evidence='SRC FileUtils.java:1027')
e('FileUtils$5.<init>', 'FileUtils$5.exists', 'CALL', 'callback for existing file',
  evidence='SRC FileUtils.java:1029 defines ErrorCallBack.exists')
e('FileUtils$5.<init>', 'FileUtils$5.launchSAF', 'CALL', 'callback for SAF launch (single file)',
  evidence='SRC FileUtils.java:1033-1035 defines ErrorCallBack.launchSAF(HybridFile)')
e('FileUtils$5.<init>', 'FileUtils$5.launchSAF', 'CALL', 'callback for SAF launch (two files)',
  evidence='SRC FileUtils.java:1037-1039 defines ErrorCallBack.launchSAF(HybridFile, HybridFile)')
e('FileUtils$5.<init>', 'FileUtils$5.done', 'CALL', 'callback for completion',
  evidence='SRC FileUtils.java:1042 defines ErrorCallBack.done')
e('FileUtils$5.<init>', 'FileUtils$5.invalidName', 'CALL', 'callback for invalid name',
  evidence='SRC FileUtils.java:1046 defines ErrorCallBack.invalidName')

# UNREACHABLE methods (no app callers)
UNREACHABLE_PART_B027 = {
    # Constructor and static initializer
    'FileUtils.<init>': ('no_trigger_in_app', 'Utility class constructor; class has only static methods, never instantiated', 'SRC FileUtils.java:96 class declaration shows utility pattern with only static methods', 'SOURCE'),
    
    'FileUtils.<clinit>': ('framework_never_calls', 'Static initializer runs automatically when class loads; triggered by first FileUtils method call', 'SRC FileUtils.java:494-499 static field initialization', 'SOURCE'),
    
    # folderSizeSftp is not called by app - SFTP uses client.size() directly
    'FileUtils.folderSizeSftp': ('no_trigger_in_app', 'Method not called by app code; HybridFile.folderSize uses SshClientUtils with client.size() for SFTP, not this method', 'SRC FileUtils.java:150-165; HybridFile.java:578-620 shows SFTP case uses client.size() not FileUtils.folderSizeSftp', 'SOURCE'),
    
    # Private helper methods called only internally
    'FileUtils.getBaseFileSize': ('no_trigger_in_app', 'Private method called only internally by getTotalBytes and otgFolderSize', 'SRC FileUtils.java:205-212; internal calls at lines 190,200', 'SOURCE'),
    
    'FileUtils.scanFile': ('no_trigger_in_app', 'Private overload taking Uri; called only internally from public scanFile methods', 'SRC FileUtils.java:230-233; internal call at line 273', 'SOURCE'),
    
    'FileUtils.applyNewDocFlag': ('no_trigger_in_app', 'Private helper called only internally by openunknown methods', 'SRC FileUtils.java:484-493; internal calls at lines 432,436,465,469,600,645', 'SOURCE'),
    
    'FileUtils.fileToContentUri': ('no_trigger_in_app', 'Private overload with volume parameter; called only internally by public fileToContentUri', 'SRC FileUtils.java:535-586; internal calls at lines 522,526', 'SOURCE'),
    
    'FileUtils.isSelfDefault': ('no_trigger_in_app', 'Private helper called only internally by openFile(File,MainActivity,SharedPreferences)', 'SRC FileUtils.java:801-811; internal call at line 748', 'SOURCE'),
    
    'FileUtils.getLinkPosition': ('no_trigger_in_app', 'Private helper called only internally by parseName', 'SRC FileUtils.java:950-955; internal call at line 926', 'SOURCE'),
    
    'FileUtils.getColonPosition': ('no_trigger_in_app', 'Private helper called only internally by parseName', 'SRC FileUtils.java:957-962; internal call at line 916', 'SOURCE'),
    

}
