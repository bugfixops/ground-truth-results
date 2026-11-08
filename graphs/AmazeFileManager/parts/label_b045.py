# ---- Helper batch_045 label part (2025-01-18)

# MainActivity$2 (anonymous BroadcastReceiver - receiver2)
# Created at line 1610, registered in onResume at line 1120
e('MainActivity.onResume', 'MainActivity$2.<init>', 'CALL', 'Create receiver2 instance for failed operations broadcast',
  evidence='SRC MainActivity.java:1610-1620 shows private BroadcastReceiver receiver2 = new BroadcastReceiver() declaration; 1120 shows registerReceiver(receiver2, new IntentFilter(TAG_INTENT_FILTER_GENERAL))')

e('MainActivity$2.<init>', 'MainActivity$2.onReceive', 'FRAMEWORK', 'BroadcastReceiver.onReceive called by Android framework when intent with TAG_INTENT_FILTER_GENERAL action is broadcast',
  evidence='SRC MainActivity.java:1612 shows @Override public void onReceive(Context context, Intent i); framework calls onReceive when broadcast matches filter')

e('MainActivity$2.onReceive', 'MainActivityHelper.showFailedOperationDialog', 'CALL', 'Show dialog for failed operations extracted from intent',
  evidence='SRC MainActivity.java:1613-1617 shows if (i.getStringArrayListExtra(TAG_INTENT_FILTER_FAILED_OPS) != null) { ArrayList<HybridFileParcelable> failedOps = i.getParcelableArrayListExtra(TAG_INTENT_FILTER_FAILED_OPS); if (failedOps != null) { mainActivityHelper.showFailedOperationDialog(failedOps, mainActivity); }')

# MainActivity$3 (anonymous BroadcastReceiver - mOtgReceiver)
# Created at line 1171, registered in updateUsbInformation at line 1165
e('MainActivity.updateUsbInformation', 'MainActivity$3.<init>', 'CALL', 'Create mOtgReceiver instance for USB OTG device attach/detach',
  evidence='SRC MainActivity.java:1171-1186 shows BroadcastReceiver mOtgReceiver = new BroadcastReceiver declaration; 1165 shows registerReceiver(mOtgReceiver, otgFilter)')

e('MainActivity$3.<init>', 'MainActivity$3.onReceive', 'FRAMEWORK', 'BroadcastReceiver.onReceive called by Android framework when USB device attached or detached',
  evidence='SRC MainActivity.java:1172-1173 shows @Override public void onReceive(Context context, Intent intent); framework calls onReceive on USB attach/detach')

# MainActivity$FabActionListener (inner class implementing SpeedDialView.OnActionSelectedListener)
# Created at line 1935, instantiated in initialiseFab at line 1508
e('MainActivity.initialiseFab', 'MainActivity$FabActionListener.<init>', 'CALL', 'Create FabActionListener for floating action button menu',
  evidence='SRC MainActivity.java:1508 shows floatingActionButton.setOnActionSelectedListener(new FabActionListener(this)); 1935 shows FabActionListener(MainActivity mainActivity) constructor')

e('MainActivity$FabActionListener.<init>', 'MainActivity$FabActionListener.onActionSelected', 'GUI', 'SpeedDialView.OnActionSelectedListener.onActionSelected called when user selects FAB menu item',
  evidence='SRC MainActivity.java:1940-1941 shows @Override public boolean onActionSelected(SpeedDialActionItem actionItem); GUI callback when FAB item selected')

e('MainActivity$FabActionListener.onActionSelected', 'MainActivityHelper.mkdir', 'CALL', 'Create new folder when menu_new_folder FAB item selected',
  evidence='SRC MainActivity.java:1945-1948 shows case R.id.menu_new_folder: mainActivity.mainActivityHelper.mkdir(ma.openMode, path, ma); break;')

e('MainActivity$FabActionListener.onActionSelected', 'MainActivityHelper.mkfile', 'CALL', 'Create new file when menu_new_file FAB item selected',
  evidence='SRC MainActivity.java:1949-1951 shows case R.id.menu_new_file: mainActivity.mainActivityHelper.mkfile(ma.openMode, path, ma); break;')

# MainActivityHelper methods
# Constructor called from MainActivity.onCreate
e('MainActivity.onCreate', 'MainActivityHelper.<init>', 'CALL', 'Instantiate MainActivityHelper in MainActivity.onCreate',
  evidence='SRC MainActivity.java:184 shows public MainActivityHelper mainActivityHelper; mainActivityHelper is initialized in onCreate. MainActivityHelper.java:82-85 shows public MainActivityHelper(MainActivity mainActivity) { this.mainActivity = mainActivity; accentColor = mainActivity.getAccent(); }')

# MainActivityHelper.showFailedOperationDialog - called from multiple places
e('MainActivity.onActivityResult', 'MainActivityHelper.showFailedOperationDialog', 'CALL', 'Show failed operations dialog after activity result',
  evidence='SRC MainActivity.java:315 shows mainActivityHelper.showFailedOperationDialog(failedOps, this); in onActivityResult; 1583,1616 show other calls')

# MainActivityHelper.search - called from AppBar search callback
e('AppBar.<init>', 'MainActivityHelper.search', 'CALL', 'Search invoked from AppBar search queue',
  evidence='SRC MainActivity.java:291-293 shows appbar = new AppBar(this, getPrefs(), queue -> { if(!queue.isEmpty()) { mainActivityHelper.search(getPrefs(), queue); } }); in onCreate')

# MainActivityHelper.checkFolder - called from onActivityResult
e('MainActivity.onActivityResult', 'MainActivityHelper.checkFolder', 'CALL', 'Check folder write permissions after SAF result',
  evidence='SRC MainActivity.java:565 shows int result = mainActivityHelper.checkFolder(folder, MainActivity.this); and 573 shows mainActivityHelper.checkFolder(folder, MainActivity.this);')

# MainActivityHelper.extractFile - called from multiple places
e('MainActivity.onOptionsItemSelected', 'MainActivityHelper.extractFile', 'CALL', 'Extract compressed file from menu',
  evidence='SRC MainActivity.java:1037 shows mainActivityHelper.extractFile(((CompressedExplorerFragment) fragment1).compressedFile); in onOptionsItemSelected for R.id.extract case')

e('MainActivity.onActivityResult', 'MainActivityHelper.extractFile', 'CALL', 'Extract file after SAF permission granted',
  evidence='SRC MainActivity.java:1383 shows mainActivityHelper.extractFile(new File(oppathe)); in onActivityResult when operation == DataUtils.EXTRACT')

# MainActivityHelper.compressFiles - called from onActivityResult
e('MainActivity.onActivityResult', 'MainActivityHelper.compressFiles', 'CALL', 'Compress files after SAF permission granted',
  evidence='SRC MainActivity.java:1386 shows mainActivityHelper.compressFiles(new File(oppathe), oparrayList); in onActivityResult when operation == DataUtils.COMPRESS')

# MainActivityHelper.mkDir - called from onActivityResult
e('MainActivity.onActivityResult', 'MainActivityHelper.mkDir', 'CALL', 'Create directory after SAF permission granted',
  evidence='SRC MainActivity.java:1370-1371 shows mainActivityHelper.mkDir(RootHelper.generateBaseFile(new File(oppathe), true), getCurrentMainFragment()); in onActivityResult when operation == DataUtils.NEW_FOLDER')

# MainActivityHelper.mkFile - called from onActivityResult
e('MainActivity.onActivityResult', 'MainActivityHelper.mkFile', 'CALL', 'Create file after SAF permission granted',
  evidence='SRC MainActivity.java:1380 shows mainActivityHelper.mkFile(new HybridFile(OpenMode.FILE, oppathe), getCurrentMainFragment()); in onActivityResult when operation == DataUtils.NEW_FILE')

# MainActivityHelper.rename - called from onActivityResult
e('MainActivity.onActivityResult', 'MainActivityHelper.rename', 'CALL', 'Rename file/folder after SAF permission granted',
  evidence='SRC MainActivity.java:1375-1376 shows mainActivityHelper.rename(ma.openMode, (oppathe), (oppathe1), this, rootMode); in onActivityResult when operation == DataUtils.RENAME')

# MainActivityHelper.mkdir - called from FabActionListener
# Already traced above from FabActionListener.onActionSelected

# MainActivityHelper.mkfile - called from FabActionListener
# Already traced above from FabActionListener.onActionSelected

# MainActivityHelper.mk - private helper for mkdir/mkfile
e('MainActivityHelper.mkdir', 'MainActivityHelper.mk', 'CALL', 'Show input dialog for folder name',
  evidence='SRC MainActivityHelper.java:136-137 shows mkdir method at line 136, line 137 calls mk(R.string.newfolder, "", lambda, validator)')

e('MainActivityHelper.mkfile', 'MainActivityHelper.mk', 'CALL', 'Show input dialog for file name',
  evidence='SRC MainActivityHelper.java:162-163 shows mkfile method at line 162, line 163 calls mk(R.string.newfile, NEW_FILE_TXT_EXTENSION, lambda, validator)')

# MainActivityHelper.getIntegralNames - called from BottomBar
e('BottomBar.updatePath', 'MainActivityHelper.getIntegralNames', 'CALL', 'Get localized name for integral path (images, videos, etc)',
  evidence='SRC BottomBar.java:314 shows newPath = mainActivityHelper.getIntegralNames(news);')

# MainActivityHelper.guideDialogForLEXA - called from rename, mkFile, mkDir callbacks
e('MainActivityHelper.rename', 'MainActivityHelper.guideDialogForLEXA', 'CALL', 'Show SAF guide dialog when rename needs storage access',
  evidence='SRC MainActivityHelper.java:286-288 shows launchSAF callback calling guideDialogForLEXA(mainActivity.oppathe1);')

e('MainActivityHelper.mkFile', 'MainActivityHelper.guideDialogForLEXA', 'CALL', 'Show SAF guide dialog when mkFile needs storage access',
  evidence='SRC MainActivityHelper.java:411-413 shows launchSAF callback calling guideDialogForLEXA(mainActivity.oppathe);')

e('MainActivityHelper.mkDir', 'MainActivityHelper.guideDialogForLEXA', 'CALL', 'Show SAF guide dialog when mkDir needs storage access',
  evidence='SRC MainActivityHelper.java:468-470 shows launchSAF callback calling guideDialogForLEXA(mainActivity.oppathe);')

e('MainActivityHelper.checkFolder', 'MainActivityHelper.guideDialogForLEXA', 'CALL', 'Show SAF guide dialog when folder check determines SAF needed',
  evidence='SRC MainActivityHelper.java:347-349 shows if (!FileUtil.isWritableNormalOrSaf(folder, context)) { guideDialogForLEXA(folder.getPath()); return CAN_CREATE_FILES; }')

# MainActivityHelper.triggerStorageAccessFramework - called from guideDialogForLEXA
e('MainActivityHelper.guideDialogForLEXA', 'MainActivityHelper.triggerStorageAccessFramework', 'CALL', 'Trigger SAF when user confirms guide dialog',
  evidence='SRC MainActivityHelper.java:249 shows .onPositive((dialog, which)->triggerStorageAccessFramework())')

# MainActivityHelper.deleteFiles - called from GeneralDialogCreation
e('GeneralDialogCreation.showDeleteDialog', 'MainActivityHelper.deleteFiles', 'CALL', 'Delete files when user confirms delete dialog',
  evidence='SRC GeneralDialogCreation.java:201 shows mainActivity.mainActivityHelper.deleteFiles(itemsToDelete);')

# Parse methods called from BottomBar
e('BottomBar.updatePath', 'MainActivityHelper.parseSftpPath', 'CALL', 'Parse SFTP path for display',
  evidence='SRC BottomBar.java:305 shows newPath = mainActivityHelper.parseSftpPath(news);')

e('BottomBar.updatePath', 'MainActivityHelper.parseSmbPath', 'CALL', 'Parse SMB path for display',
  evidence='SRC BottomBar.java:308 shows newPath = mainActivityHelper.parseSmbPath(news);')

e('BottomBar.updatePath', 'MainActivityHelper.parseOTGPath', 'CALL', 'Parse OTG path for display',
  evidence='SRC BottomBar.java:311 shows newPath = mainActivityHelper.parseOTGPath(news);')

e('BottomBar.updatePath', 'MainActivityHelper.parseCloudPath', 'CALL', 'Parse cloud path for display',
  evidence='SRC BottomBar.java:320 shows newPath = mainActivityHelper.parseCloudPath(openmode, news);')

# MainActivityHelper.addSearchFragment - static method called from search
e('MainActivityHelper.search', 'MainActivityHelper.addSearchFragment', 'CALL', 'Add search worker fragment to fragment manager',
  evidence='SRC MainActivityHelper.java:605-608 shows addSearchFragment(fm, new SearchWorkerFragment(), fpath, query, ma.openMode, mainActivity.isRootExplorer(), sharedPrefs.getBoolean(SearchWorkerFragment.KEY_REGEX, false), sharedPrefs.getBoolean(SearchWorkerFragment.KEY_REGEX_MATCHES, false));')

# MainActivityHelper$1 (anonymous BroadcastReceiver - mNotificationReceiver)
# Created in MainActivityHelper as field, registered in MainActivity.onResume
e('MainActivity.onResume', 'MainActivityHelper$1.onReceive', 'FRAMEWORK', 'BroadcastReceiver.onReceive called by framework when media mounted/unmounted',
  evidence='SRC MainActivityHelper.java:102-120 shows public final BroadcastReceiver mNotificationReceiver = new BroadcastReceiver() { @Override public void onReceive(Context context, Intent intent) { if (intent != null) { if (intent.getAction().equals(Intent.ACTION_MEDIA_MOUNTED)) { ... } else if (intent.getAction().equals(Intent.ACTION_MEDIA_UNMOUNTED)) { ... } } } }; MainActivity.java:1119 shows registerReceiver(mainActivityHelper.mNotificationReceiver, newFilter);')

# Lambda methods in MainActivityHelper
# These are synthetic lambda methods generated by the compiler for lambda expressions

e('MainActivityHelper.mkdir', 'MainActivityHelper.lambda$mkdir$0', 'CALL', 'Lambda callback when user confirms folder creation dialog',
  evidence='SRC MainActivityHelper.java:137-140 shows mk call with lambda (dialog, which) -> { EditText textfield = dialog.getCustomView().findViewById(R.id.singleedittext_input); mkDir(new HybridFile(openMode, path + "/" + textfield.getText().toString()), ma); dialog.dismiss(); }; compiler generates lambda$mkdir$0')

e('MainActivityHelper.mkdir', 'MainActivityHelper.lambda$mkdir$1', 'CALL', 'Lambda validator for folder name input',
  evidence='SRC MainActivityHelper.java:141-151 shows validator lambda (text) -> { boolean isValidFilename = FileUtil.isValidFilename(text); ... }; compiler generates lambda$mkdir$1')

e('MainActivityHelper.mkfile', 'MainActivityHelper.lambda$mkfile$2', 'CALL', 'Lambda callback when user confirms file creation dialog',
  evidence='SRC MainActivityHelper.java:163-166 shows mk call with lambda (dialog, which) -> { EditText textfield = dialog.getCustomView().findViewById(R.id.singleedittext_input); mkFile(new HybridFile(openMode, path + "/" + textfield.getText().toString()), ma); dialog.dismiss(); }; compiler generates lambda$mkfile$2')

e('MainActivityHelper.mkfile', 'MainActivityHelper.lambda$mkfile$3', 'CALL', 'Lambda validator for file name input',
  evidence='SRC MainActivityHelper.java:167-187 shows validator lambda (text) -> { boolean isValidFilename = FileUtil.isValidFilename(text); ... }; compiler generates lambda$mkfile$3')

e('MainActivityHelper.guideDialogForLEXA', 'MainActivityHelper.lambda$guideDialogForLEXA$4', 'CALL', 'Lambda for positive button in LEXA guide dialog',
  evidence='SRC MainActivityHelper.java:249 shows .onPositive((dialog, which)->triggerStorageAccessFramework()); compiler generates lambda$guideDialogForLEXA$4')

e('MainActivityHelper.guideDialogForLEXA', 'MainActivityHelper.lambda$guideDialogForLEXA$5', 'CALL', 'Lambda for negative button in LEXA guide dialog',
  evidence='SRC MainActivityHelper.java:250 shows .onNegative((dialog, which)->Toast.makeText(mainActivity, R.string.error, Toast.LENGTH_SHORT).show()); compiler generates lambda$guideDialogForLEXA$5')

e('MainActivityHelper.lambda$mkdir$0', 'MainActivityHelper.mkDir', 'CALL', 'Create directory after dialog confirmation',
  evidence='SRC MainActivityHelper.java:139 shows mkDir(new HybridFile(openMode, path + "/" + textfield.getText().toString()), ma);')

e('MainActivityHelper.lambda$mkfile$2', 'MainActivityHelper.mkFile', 'CALL', 'Create file after dialog confirmation',
  evidence='SRC MainActivityHelper.java:165 shows mkFile(new HybridFile(openMode, path + "/" + textfield.getText().toString()), ma);')

e('MainActivityHelper.lambda$guideDialogForLEXA$4', 'MainActivityHelper.triggerStorageAccessFramework', 'CALL', 'Trigger SAF from lambda',
  evidence='SRC MainActivityHelper.java:249 shows .onPositive((dialog, which)->triggerStorageAccessFramework())')

# UNREACHABLE methods
UNREACHABLE_PART_B045 = {}
UNREACHABLE_PART_B045['MainActivityHelper.isNewDirectoryRecursive'] = (
    'no_trigger_in_app',
    'Static utility method never called in app code. Grep shows no call sites in app source',
    'SRC MainActivityHelper.java:644-646 shows public static boolean isNewDirectoryRecursive(HybridFile file) { return file.getName().equals(file.getParentName()); }; grep -rn isNewDirectoryRecursive in app source shows only declaration, no calls',
    'SOURCE'
)
