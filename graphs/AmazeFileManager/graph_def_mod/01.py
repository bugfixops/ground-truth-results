
e('Indicator.setSelectedPage', 'Indicator.createMoveSelectedAnimator', 'CALL',
  'setSelectedPage creates move animator for selected dot',
  evidence='SRC Indicator.java:579 moveAnimation = createMoveSelectedAnimator(dotCenterX[now], previousPage, now, steps)')

e('Indicator.createMoveSelectedAnimator', 'Indicator$PendingRetreatAnimator.<init>', 'CALL',
  'createMoveSelectedAnimator constructs PendingRetreatAnimator',
  evidence='SRC Indicator.java:587 retreatAnimation = new PendingRetreatAnimator(was, now, steps, predicate)')

e('Indicator.createMoveSelectedAnimator', 'Indicator$RightwardStartPredicate.<init>', 'CALL',
  'createMoveSelectedAnimator constructs RightwardStartPredicate when moving right',
  evidence='SRC Indicator.java:589 new RightwardStartPredicate(moveTo - ((moveTo - selectedDotX) * 0.25f))')

e('Indicator$RightwardStartPredicate.<init>', 'Indicator$StartPredicate.<init>', 'CALL',
  'RightwardStartPredicate constructor calls super',
  evidence='SRC Indicator.java:826-828 RightwardStartPredicate(float thresholdValue) calls super(thresholdValue)')

e('Indicator.createMoveSelectedAnimator', 'Indicator.resetState', 'CALL',
  'Animator listener calls resetState on animation end',
  evidence='SRC Indicator.java:590-595 AnimatorListenerAdapter.onAnimationEnd calls resetState()')



e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingStartAnimator.<init>', 'CALL',
  'PendingRetreatAnimator constructor calls super',
  evidence='SRC Indicator.java:682 PendingRetreatAnimator calls super(predicate)')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRevealAnimator.<init>', 'CALL',
  'PendingRetreatAnimator creates reveal animators array',
  evidence='SRC Indicator.java:708,725 revealAnimations[i] = new PendingRevealAnimator(was + i, predicate)')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$RightwardStartPredicate.<init>', 'CALL',
  'PendingRetreatAnimator creates RightwardStartPredicate for reveal animators',
  evidence='SRC Indicator.java:709 new RightwardStartPredicate(dotCenterX[was + i])')


e('Indicator$PendingRetreatAnimator.<init>', 'Indicator.cancelJoiningAnimations', 'CALL',
  'Animator listener calls cancelJoiningAnimations on start',
  evidence='SRC Indicator.java:742 cancelJoiningAnimations()')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator.clearJoiningFractions', 'CALL',
  'Animator listener calls clearJoiningFractions on start',
  evidence='SRC Indicator.java:743 clearJoiningFractions()')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator.setDotRevealFraction', 'CALL',
  'Animator listener calls setDotRevealFraction for dots to hide',
  evidence='SRC Indicator.java:746 setDotRevealFraction(dot, MINIMAL_REVEAL)')

e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRetreatAnimator$1.<init>', 'CALL',
  'PendingRetreatAnimator creates anonymous AnimatorListenerAdapter',
  evidence='SRC Indicator.java:740-758 addListener(new AnimatorListenerAdapter() {...})')

e('Indicator$PendingRetreatAnimator$1.<init>', 'Indicator$PendingRetreatAnimator$1.onAnimationStart', 'ASYNC',
  'Framework calls onAnimationStart when retreat animation begins',
  evidence='SRC Indicator.java:742-749 onAnimationStart(Animator animation) method; INFERRED: framework source not read')

e('Indicator$PendingRetreatAnimator$1.<init>', 'Indicator$PendingRetreatAnimator$1.onAnimationEnd', 'ASYNC',
  'Framework calls onAnimationEnd when retreat animation completes',
  evidence='SRC Indicator.java:751-755 onAnimationEnd(Animator animation) method; INFERRED: framework source not read')

e('Indicator$PendingRevealAnimator.<init>', 'Indicator$PendingStartAnimator.<init>', 'CALL',
  'PendingRevealAnimator constructor calls super',
  evidence='SRC Indicator.java:768 PendingRevealAnimator calls super(predicate)')

e('Indicator$PendingRevealAnimator.<init>', 'Indicator.setDotRevealFraction', 'CALL',
  'Update listener calls setDotRevealFraction',
  evidence='SRC Indicator.java:775 setDotRevealFraction(PendingRevealAnimator.this.dot, (Float) valueAnimator.getAnimatedValue())')

e('Indicator$PendingRevealAnimator.<init>', 'Indicator$PendingRevealAnimator$1.<init>', 'CALL',
  'PendingRevealAnimator creates anonymous AnimatorListenerAdapter',
  evidence='SRC Indicator.java:778-784 addListener(new AnimatorListenerAdapter() {...})')

e('Indicator$PendingRevealAnimator$1.<init>', 'Indicator$PendingRevealAnimator$1.onAnimationEnd', 'ASYNC',
  'Framework calls onAnimationEnd when reveal animation completes',
  evidence='SRC Indicator.java:780-783 onAnimationEnd(Animator animation) method; INFERRED: framework source not read')

e('Indicator.onPageScrolled', 'Indicator.setJoiningFraction', 'CALL',
  'ViewPager scroll callback calls setJoiningFraction',
  evidence='SRC Indicator.java:193 setJoiningFraction(leftDotPosition, fraction)')

e('Indicator.onDraw', 'Indicator.drawUnselected', 'FRAMEWORK',
  'Framework onDraw calls drawUnselected',
  evidence='SRC Indicator.java:291 drawUnselected(canvas); INFERRED: framework source not read')

e('Indicator.onDraw', 'Indicator.drawSelected', 'FRAMEWORK',
  'Framework onDraw calls drawSelected',
  evidence='SRC Indicator.java:292 drawSelected(canvas); INFERRED: framework source not read')

e('Indicator.drawUnselected', 'Indicator.getUnselectedPath', 'CALL',
  'drawUnselected calls getUnselectedPath for each dot',
  evidence='SRC Indicator.java:301-304 combinedUnselectedPath.op(getUnselectedPath(...))')

e('Indicator.drawUnselected', 'Indicator.getRetreatingJoinPath', 'CALL',
  'drawUnselected calls getRetreatingJoinPath when retreat active',
  evidence='SRC Indicator.java:308 combinedUnselectedPath.op(getRetreatingJoinPath(), Path.Op.UNION)')

e('Indicator.createMoveSelectedAnimator', 'Indicator.lambda$createMoveSelectedAnimator$0', 'CALL',
  'Lambda desugared for animator update listener',
  evidence='SRC Indicator.java:597-600 moveSelected.addUpdateListener(valueAnimator -> {...})')

# LZMA2Decoder - 7z compression library class accessed via Coders map

e('SevenZFile.buildDecodingStream', 'Coders.addDecoder', 'CALL',
  'SevenZFile calls Coders.addDecoder to decode each coder',
  evidence='SRC SevenZFile.java:435 inputStreamStack = Coders.addDecoder(fileName, inputStreamStack, ...)')

e('Coders.addDecoder', 'LZMA2Decoder.decode', 'CALL',
  'Coders.addDecoder looks up LZMA2Decoder from map and calls decode',
  evidence='SRC Coders.java:53 put(SevenZMethod.LZMA2, new LZMA2Decoder()); Coders.java:69-75 cb = findByMethod(...); return cb.decode(...)')

e('LZMA2Decoder.decode', 'LZMA2Decoder.getDictionarySize', 'CALL',
  'decode calls getDictionarySize to extract dictionary size from coder properties',
  evidence='SRC LZMA2Decoder.java:36 final int dictionarySize = getDictionarySize(coder)')


e('SevenZOutputFile.writeFilesInfo', 'Coders.findByMethod', 'CALL',
  'SevenZOutputFile calls findByMethod to get coder for properties',
  evidence='SRC SevenZOutputFile.java:452 Coders.findByMethod(m.getMethod()).getOptionsAsProperties(m.getOptions())')

e('Coders.findByMethod', 'LZMA2Decoder.getOptionsAsProperties', 'CALL',
  'findByMethod returns LZMA2Decoder, caller invokes getOptionsAsProperties',
  evidence='SRC Coders.java:53 put(SevenZMethod.LZMA2, new LZMA2Decoder()); Coders.java:67 return CODER_MAP.get(method)')

e('LZMA2Decoder.getOptionsAsProperties', 'LZMA2Decoder.getDictSize', 'CALL',
  'getOptionsAsProperties calls getDictSize to encode dictionary size',
  evidence='SRC LZMA2Decoder.java:56 final int dictSize = getDictSize(opts)')

e('LZMA2Decoder.getDictSize', 'LZMA2Decoder.numberOptionOrDefault', 'CALL',
  'getDictSize calls numberOptionOrDefault when opts is not LZMA2Options',
  evidence='SRC LZMA2Decoder.java:71 return numberOptionOrDefault(opts)')




e('LZMA2Decoder.getOptions', 'LZMA2Decoder.numberOptionOrDefault', 'CALL',
  'getOptions calls numberOptionOrDefault to get dict size',
  evidence='SRC LZMA2Decoder.java:93 options.setDictSize(numberOptionOrDefault(opts))')

# InterestingConfigChange static initializer
# Static fields initialized at class load, which happens on first access (isConfigChanged call)

# No UNREACHABLE methods in this batch - all methods are REACHABLE through the routes above

# ---- part label_b043 (2026-10-27 23:50 re-merged WITH edges) ----

# LoadFolderSpaceDataTask edges
e('GeneralDialogCreation.showPropertiesDialog', 'LoadFolderSpaceDataTask.<init>', 'CALL',
  'Constructor instantiated to load folder space data for properties dialog',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:516')

e('LoadFolderSpaceDataTask.<init>', 'LoadFolderSpaceDataTask.doInBackground', 'LIFECYCLE',
  'AsyncTask.execute triggers doInBackground on background thread',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:517 shows executeOnExecutor call; INFERRED framework lifecycle')

e('LoadFolderSpaceDataTask.doInBackground', 'LoadFolderSpaceDataTask.createEntriesFromArray', 'CALL',
  'doInBackground calls createEntriesFromArray to build pie chart entries',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:61')

e('LoadFolderSpaceDataTask.<init>', 'LoadFolderSpaceDataTask.onPostExecute', 'LIFECYCLE',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:77; INFERRED framework lifecycle')

e('LoadFolderSpaceDataTask.onPostExecute', 'LoadFolderSpaceDataTask.updateChart', 'CALL',
  'onPostExecute calls updateChart with final data',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:91')

e('LoadFolderSpaceDataTask.<init>', 'LoadFolderSpaceDataTask.onProgressUpdate', 'LIFECYCLE',
  'AsyncTask framework calls onProgressUpdate when publishProgress is called',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:67; INFERRED framework lifecycle')

e('LoadFolderSpaceDataTask.onProgressUpdate', 'LoadFolderSpaceDataTask.createEntriesFromArray', 'CALL',
  'onProgressUpdate calls createEntriesFromArray for intermediate updates',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:74')

e('LoadFolderSpaceDataTask.onProgressUpdate', 'LoadFolderSpaceDataTask.updateChart', 'CALL',
  'onProgressUpdate calls updateChart for progress display',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:77')

# LruBitmapCache edges

e('LruBitmapCache.<init>()', 'LruBitmapCache.<init>(int)', 'CALL',
  'No-arg constructor delegates to parameterized constructor via this()',
  evidence='SRC utils/LruBitmapCache.java:22')

e('LruBitmapCache.<init>()', 'LruBitmapCache.getDefaultCacheSize', 'CALL',
  'No-arg constructor calls getDefaultCacheSize for cache size',
  evidence='SRC utils/LruBitmapCache.java:22')

e('LruBitmapCache.<init>()', 'LruBitmapCache.getBitmap', 'FRAMEWORK',
  'ImageLoader calls getBitmap to retrieve cached bitmaps',
  evidence='SRC utils/LruBitmapCache.java:31 implements ImageLoader.ImageCache; INFERRED framework call')

e('LruBitmapCache.<init>()', 'LruBitmapCache.putBitmap', 'FRAMEWORK',
  'ImageLoader calls putBitmap to cache bitmaps',
  evidence='SRC utils/LruBitmapCache.java:36 implements ImageLoader.ImageCache; INFERRED framework call')

e('LruBitmapCache.<init>()', 'LruBitmapCache.sizeOf', 'FRAMEWORK',
  'LruCache framework calls sizeOf to calculate entry sizes',
  evidence='SRC utils/LruBitmapCache.java:40 overrides LruCache.sizeOf; INFERRED framework call')

# LzmaDecompressor edges
e('CompressedHelper.getCompressorInstance', 'LzmaDecompressor.<init>', 'CALL',
  'Constructor instantiated for .tar.lzma file types',
  evidence='SRC filesystem/compressed/CompressedHelper.java:124')

e('LzmaDecompressor.<init>', 'LzmaDecompressor.changePath', 'FRAMEWORK',
  'Parent Decompressor class calls changePath to navigate archive',
  evidence='SRC filesystem/compressed/showcontents/helpers/LzmaDecompressor.java:40; INFERRED framework call from Decompressor')

e('LzmaDecompressor.changePath', 'LzmaHelperTask.<init>', 'CALL',
  'changePath instantiates LzmaHelperTask for async archive processing',
  evidence='SRC filesystem/compressed/showcontents/helpers/LzmaDecompressor.java:43')

e('LzmaHelperTask.<init>', 'LzmaHelperTask.addElements', 'FRAMEWORK',
  'CompressedHelperTask framework calls addElements to populate archive entries',
  evidence='SRC asynchronous/asynctasks/compress/LzmaHelperTask.java:52; INFERRED framework call from CompressedHelperTask')

# LzmaExtractor edges
e('CompressedHelper.getExtractorInstance', 'LzmaExtractor.<init>', 'CALL',
  'Constructor instantiated for .tar.lzma file extraction',
  evidence='SRC filesystem/compressed/CompressedHelper.java:94')

e('LzmaExtractor.<init>', 'LzmaExtractor.extractWithFilter', 'FRAMEWORK',
  'Parent Extractor class calls extractWithFilter to extract archive',
  evidence='SRC filesystem/compressed/extractcontents/helpers/LzmaExtractor.java:48; INFERRED framework call from Extractor')

e('LzmaExtractor.extractWithFilter', 'LzmaExtractor.extractEntry', 'CALL',
  'extractWithFilter calls extractEntry for each archive entry',
  evidence='SRC filesystem/compressed/extractcontents/helpers/LzmaExtractor.java:74')

# UNREACHABLE methods from batch_043


UNREACHABLE['LZMADecoder.encode'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)


UNREACHABLE['LZMADecoder.getOptions'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.getOptionsAsProperties'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)


UNREACHABLE['LZMADecoder.numberOptionOrDefault'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

# ---- part label_b045 (2026-10-27 23:50 re-merged WITH edges) ----

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

e('MainActivity$FabActionListener.<init>', 'MainActivity$FabActionListener.onActionSelected', 'FRAMEWORK', 'SpeedDialView.OnActionSelectedListener.onActionSelected called when user selects FAB menu item',
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
UNREACHABLE.update(UNREACHABLE_PART_B045)
UNREACHABLE_PART_B045['MainActivityHelper.isNewDirectoryRecursive'] = (
    'no_trigger_in_app',
    'Static utility method never called in app code. Grep shows no call sites in app source',
    'SRC MainActivityHelper.java:644-646 shows public static boolean isNewDirectoryRecursive(HybridFile file) { return file.getName().equals(file.getParentName()); }; grep -rn isNewDirectoryRecursive in app source shows only declaration, no calls',
    'SOURCE'
)

# ---- part resume_rb01 (2026-10-28)
# Library classes (Apache Commons Compress sevenz) - no calls from app code

UNREACHABLE['AES256SHA256Decoder$1.read()'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "AES256SHA256Decoder" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['AES256SHA256Decoder$1.read(byte[],int,int)'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "AES256SHA256Decoder" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')




UNREACHABLE['Archive.lengthOf(Object[])'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "Archive\\.lengthOf" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')

UNREACHABLE['Archive.lengthOf(long[])'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress), grep -rn "Archive\\.lengthOf" in app src/main/java shows no calls', 'INFERRED library source not in dataset', 'INFERRED')


# ---- part resume_rb02 (2026-10-28)
# CloudEntry methods - called from CloudHandler and CloudLoaderAsyncTask

e('CloudHandler.updateEntry', 'CloudEntry.getId', 'CALL',
  'Gets entry ID to update database record',
  evidence='SRC database/CloudHandler.java:122')

e('CloudHandler.addEntry', 'CloudEntry.getPersistData', 'CALL',
  'Gets persist data to store in database',
  evidence='SRC database/CloudHandler.java:92,98')

e('CloudHandler.updateEntry', 'CloudEntry.getPersistData', 'CALL',
  'Gets persist data to update database record',
  evidence='SRC database/CloudHandler.java:127,133')

e('CloudHandler.addEntry', 'CloudEntry.getServiceType', 'CALL',
  'Gets service type ordinal to store in database',
  evidence='SRC database/CloudHandler.java:90')

e('CloudHandler.updateEntry', 'CloudEntry.getServiceType', 'CALL',
  'Gets service type ordinal to update database record',
  evidence='SRC database/CloudHandler.java:123')

# CloudIconDataFetcher lifecycle methods - called by Glide framework
e('CloudIconDataFetcher.loadData', 'CloudIconDataFetcher.cleanup', 'LIFECYCLE',
  'Glide framework calls cleanup after loadData completes or fails',
  evidence='INFERRED Glide DataFetcher lifecycle; SRC utils/glide/CloudIconDataFetcher.java:48-55')

e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.getDataClass', 'CALL',
  'Glide queries data class for type information',
  evidence='INFERRED Glide framework queries fetcher type; SRC utils/glide/CloudIconDataFetcher.java:63-66')

e('CloudIconModelLoader.buildLoadData', 'CloudIconDataFetcher.getDataSource', 'CALL',
  'Glide queries data source for caching strategy',
  evidence='INFERRED Glide framework queries data source; SRC utils/glide/CloudIconDataFetcher.java:69-73')

e('CloudIconDataFetcher.<init>', 'CloudIconDataFetcher.loadData', 'LIFECYCLE',
  'Glide framework calls loadData to fetch image data',
  evidence='INFERRED Glide DataFetcher lifecycle; SRC utils/glide/CloudIconDataFetcher.java:35-43')

# CloudStreamServer$Response default constructor - UNREACHABLE
UNREACHABLE['CloudStreamServer$Response.<init>(CloudStreamServer)'] = (
    'no_trigger_in_app',
    'Default constructor is never called; app only uses parameterized constructor Response(status, mimeType, data)',
    'SRC utils/cloud/CloudStreamer.java:65,93,106,111 shows only new Response(status, mimeType, data) calls',
    'SOURCE'
)


# ---- part resume_rb03 (2026-10-28)
# CloudStreamServer, CloudStreamSource, CloudStreamer, CloudUtil, CoderBase methods


# Static initializers


# CloudStreamSource methods
e('CloudStreamServer$HTTPSession.sendResponse', 'CloudStreamSource.close', 'CALL', 'sendResponse closes stream',
  evidence='SRC CloudStreamServer.java:849')



e('CloudStreamSource.<init>', 'CloudStreamSource.getName', 'CALL', 'constructor sets name',
  evidence='SRC CloudStreamSource.java:23, 84-86')

# CloudStreamer.isStreamMedia

# CloudUtil methods
e('CloudIconDataFetcher.loadData', 'CloudUtil.getThumbnailInputStreamForCloud', 'CALL', 'Glide data fetcher loads cloud thumbnails',
  evidence='SRC CloudIconDataFetcher.java:37')

e('CloudUtil.getThumbnailInputStreamForCloud', 'CloudUtil$2$1.close', 'CALL', 'creates anonymous RemoteFileInputStream with close override',
  evidence='SRC CloudUtil.java:268-277')

e('CloudUtil.launchCloud', 'CloudUtil.lambda$null$0', 'ASYNC', 'creates background thread',
  evidence='SRC CloudUtil.java:136')

e('CloudUtil.launchCloud', 'CloudUtil.lambda$launchCloud$1', 'ASYNC', 'creates UI thread lambda',
  evidence='SRC CloudUtil.java:139')

# CoderBase - library methods


# UNREACHABLE entries
UNREACHABLE['CloudStreamServer.encodeUri'] = ('no_trigger_in_app', 'Private method only in commented code', 'SRC CloudStreamServer.java:866-885, line 974 commented', 'SOURCE')

UNREACHABLE['CloudUtil.<init>'] = ('no_trigger_in_app', 'CloudUtil has only static methods', 'SRC CloudUtil.java:52', 'SOURCE')


# ---- part resume_rb04 (2026-10-28)
# Batch rb_04: Coders$DeflateDecoder inner classes, ColorAdapter, ColorCircleDrawable, ColorPickerDialog inner classes
# All 28 methods in this batch were already labeled in previous parts (batch_011 and label_b010)
# No new edges or UNREACHABLE entries needed


# ---- part resume_rb05 (2026-10-28)

# ColorPickerDialog.lambda$inflateItem$0
e('ColorPickerDialog.inflateItem', 'ColorPickerDialog.lambda$inflateItem$0', 'CALL',
  'Lambda click listener for color picker item',
  evidence='SRC ui/dialogs/ColorPickerDialog.java:169-176')

e('ColorPickerDialog.lambda$inflateItem$0', 'ColorPickerDialog.select', 'CALL',
  'Lambda calls select to update selection state',
  evidence='SRC ui/dialogs/ColorPickerDialog.java:170-174')

# ColorPickerDialog.setColorPreference
e('ColorPref.loadSection1', 'ColorPickerDialog.setColorPreference', 'CALL',
  'ColorPref sets color preferences on the dialog',
  evidence='SRC fragments/preference_fragments/ColorPref.java:223')

# ColorPickerDialog.setListener
e('ColorPref.loadSection1', 'ColorPickerDialog.setListener', 'CALL',
  'ColorPref sets listener on the dialog',
  evidence='SRC fragments/preference_fragments/ColorPref.java:224-232')

# ColorPref.lambda$loadSection1$1
e('ColorPickerDialog.setListener', 'ColorPref.lambda$loadSection1$1', 'CALL',
  'Lambda listener passed to setListener',
  evidence='SRC fragments/preference_fragments/ColorPref.java:224-232')

e('ColorPref.lambda$loadSection1$1', 'ColorPref.checkCustomization', 'CALL',
  'Lambda calls checkCustomization',
  evidence='SRC fragments/preference_fragments/ColorPref.java:226')

e('ColorPref.lambda$loadSection1$1', 'ColorPref.invalidateEverything', 'CALL',
  'Lambda calls invalidateEverything',
  evidence='SRC fragments/preference_fragments/ColorPref.java:227')

# ComputerParcelable.<init>(String,String)
e('SmbSearchDialog.onCreateDialog', 'ComputerParcelable.<init>(String,String)', 'CALL',
  'Creates ComputerParcelable in SMB search dialog',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:78')



# ComputerParcelable.<init>(Parcel) - UNREACHABLE
# Already marked UNREACHABLE in graph_def.py:9344 - ComputerParcelable is never unparceled in app

# CopyService$1.onReceive
e('ProcessViewerFragment.cancelBroadcast', 'CopyService$1.onReceive', 'INTENT',
  'ProcessViewerFragment sends TAG_BROADCAST_COPY_CANCEL broadcast to cancel copy',
  evidence='SRC fragments/ProcessViewerFragment.java:251; asynchronous/services/CopyService.java:100 registerReceiver(receiver3, new IntentFilter(TAG_BROADCAST_COPY_CANCEL))')

e('CopyService.onStartCommand', 'CopyService$1.onReceive', 'INTENT',
  'Notification stop button sends TAG_BROADCAST_COPY_CANCEL broadcast',
  evidence='SRC asynchronous/services/CopyService.java:129 stopIntent = new Intent(TAG_BROADCAST_COPY_CANCEL), 130 stopPendingIntent = PendingIntent.getBroadcast(...), 131-132 action added to notification; 100 registerReceiver(receiver3, new IntentFilter(TAG_BROADCAST_COPY_CANCEL))')

# ---- part resume_rb06 (2026-10-28)

# CopyService methods
e('CopyService.onCreate', 'CopyService.onDestroy', 'LIFECYCLE', 'Service.onDestroy called by framework when service destroyed',
  evidence='SRC asynchronous/services/CopyService.java:215-216; FW-SRC core/java/android/app/Service.java:510-516')

e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'CopyService.setProgressListener', 'CALL', 
  'ProcessViewerFragment sets progress listener when service connects',
  evidence='SRC fragments/ProcessViewerFragment.java:416')

# CountItemsOrAndSizeTask lambda methods
e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.lambda$doInBackground$0', 'CALL',
  'doInBackground uses lambda to count files: file -> x.incrementAndGet()',
  evidence='SRC asynchronous/asynctasks/CountItemsOrAndSizeTask.java:41')

e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.lambda$doInBackground$1', 'CALL',
  'doInBackground uses lambda for progress callback: data -> publishProgress(new Pair<>(folderLength, data))',
  evidence='SRC asynchronous/asynctasks/CountItemsOrAndSizeTask.java:48')

e('CountItemsOrAndSizeTask.lambda$doInBackground$1', 'CountItemsOrAndSizeTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate on main thread',
  evidence='SRC asynchronous/asynctasks/CountItemsOrAndSizeTask.java:48,59; INFERRED AsyncTask framework behavior')

# DataUtils lambda method
e('DataUtils.clearHistory', 'DataUtils.lambda$clearHistory$0', 'ASYNC',
  'clearHistory runs lambda in background: () -> dataChangeListener.onHistoryCleared()',
  evidence='SRC utils/DataUtils.java:411')

# ---- part resume_rb07 (2026-10-28)

# DatabaseViewerActivity lifecycle methods
e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.onPrepareOptionsMenu', 'LIFECYCLE',
  'Activity menu lifecycle callback',
  evidence='INFERRED Activity options menu callbacks (framework source not read); SRC DatabaseViewerActivity.java:198-201')

e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.onDestroy', 'LIFECYCLE',
  'Activity lifecycle onDestroy',
  evidence='INFERRED Activity onDestroy called when activity finishes (framework source not read); SRC DatabaseViewerActivity.java:189-195')

e('DatabaseViewerActivity.onOptionsItemSelected', 'DatabaseViewerActivity.onBackPressed', 'CALL',
  'Home button in options menu calls onBackPressed',
  evidence='SRC DatabaseViewerActivity.java:206-207')

# Drawer.resetPendingPath
e('Drawer.onDrawerClosed', 'Drawer.resetPendingPath', 'CALL',
  'resetPendingPath clears pending navigation path if pendingPath is not null',
  evidence='SRC Drawer.java:557 pendingPath assigned when menu item selected; Drawer.java:563 called to clear after navigation; resetPendingPath at line 719-721')

# Drawer.lambda$addNewItem$5 - this is a menu item onClick lambda
# The exact lambda is determined by compiler; it's one of the lambdas in addNewItem calls for menu items
# All these lambdas are REACHABLE from Drawer.onNavigationItemSelected via MenuMetadata.onClickListener.onClick()
e('Drawer.refreshDrawer', 'Drawer.lambda$addNewItem$5', 'CALL',
  'refreshDrawer creates menu items with lambdas via addNewItem; lambda $5 is one of the menu item onClick handlers',
  evidence='SRC Drawer.java:402-439 addNewItem calls create MenuMetadata with lambda Runnables for FTP/Apps/Settings menu items; Drawer.java:597 meta.onClickListener.onClick() calls the lambda')

# UNREACHABLE methods

UNREACHABLE['DatapointParcelable.<init>(String,int,int,long,long,long,boolean)'] = ('no_trigger_in_app', '7-parameter constructor never called; publishResults uses 8-param constructor, addFirstDatapoint uses 4-param constructor', 'SRC DatapointParcelable.java:78-88 constructor definition; AbstractProgressiveService.java:157-158 uses 8-param (String,int,int,long,long,long,boolean,boolean), line 178 uses 4-param (String,int,long,boolean); no 7-param calls found', 'SOURCE')

# ---- part resume_rb08 (2026-10-28)

# EncryptService$BackgroundTask - AsyncTask for encryption
e('EncryptService.onStartCommand', 'EncryptService$BackgroundTask.<init>', 'CALL', 'new BackgroundTask().execute()',
  evidence='SRC EncryptService.java:115')
e('EncryptService$BackgroundTask.<init>', 'EncryptService$BackgroundTask.doInBackground', 'ASYNC', 'AsyncTask.execute runs doInBackground on worker thread',
  evidence='INFERRED android.os.AsyncTask.execute (platform source not read for this exact flow); SRC EncryptService.java:115, 171-193')
e('EncryptService$BackgroundTask.doInBackground', 'EncryptService$BackgroundTask.lambda$doInBackground$0', 'CALL', 'progressHandler.setProgressListener lambda expression',
  evidence='SRC EncryptService.java:177-178')
e('EncryptService$BackgroundTask.doInBackground', 'EncryptService$BackgroundTask.onPostExecute', 'ASYNC', 'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  evidence='INFERRED android.os.AsyncTask (platform source not read); SRC EncryptService.java:195-205')
e('EncryptService.onStartCommand', 'EncryptService.onBind', 'LIFECYCLE', 'Service.onBind called when client binds to service',
  evidence='SRC EncryptService.java:207-209 shows @Override onBind(Intent intent) returning mBinder; INFERRED Service lifecycle')
e('EncryptService.onCreate', 'EncryptService.onDestroy', 'LIFECYCLE', 'Service.onDestroy called when service destroyed',
  evidence='SRC EncryptService.java:214-217 shows @Override onDestroy() unregistering cancelReceiver; INFERRED Service lifecycle')
e('EncryptService.onStartCommand', 'EncryptService.setProgressListener', 'CALL', 'setProgressListener called to set progress callback',
  evidence='SRC EncryptService.java:159-161 shows @Override setProgressListener(ProgressListener progressListener)')

# ExtractService$1 - BroadcastReceiver for cancel
e('ExtractService.onCreate', 'ExtractService$1.<init>', 'CALL', 'registerReceiver(receiver1, new IntentFilter(TAG_BROADCAST_EXTRACT_CANCEL))',
  evidence='SRC ExtractService.java:86')
e('ExtractService$1.<init>', 'ExtractService$1.onReceive', 'FRAMEWORK', 'BroadcastReceiver.onReceive called when matching broadcast received',
  evidence='INFERRED BroadcastReceiver (platform source not read); SRC ExtractService.java:406-410')
e('ExtractService.onStartCommand', 'ExtractService.onBind', 'LIFECYCLE', 'Service.onBind called when client binds to service',
  evidence='SRC ExtractService.java:412-414 shows @Override onBind(Intent intent) returning mBinder; INFERRED Service lifecycle')
e('ExtractService.onCreate', 'ExtractService.onDestroy', 'LIFECYCLE', 'Service.onDestroy called when service destroyed',
  evidence='SRC ExtractService.java:206-208 shows @Override onDestroy() unregistering receiver1; INFERRED Service lifecycle')

# FastScroller - custom RecyclerView scroller UI component
e('FastScroller.<init>(Context,AttributeSet,int)', 'FastScroller.getRelativeTouchPosition', 'CALL', 'getRelativeTouchPosition called from onTouchEvent',
  evidence='SRC FastScroller.java:102 shows getRelativeTouchPosition(motionEvent) in onTouchEvent')
e('FastScroller.<init>(Context,AttributeSet,int)', 'FastScroller.onTouchEvent', 'FRAMEWORK', 'View.onTouchEvent dispatched by framework when view touched',
  evidence='INFERRED View touch event dispatch (platform source not read); SRC FastScroller.java:98-118')

# FileHandler - Handler for MainFragment file operations
e('FileHandler.<init>', 'FileHandler.handleMessage', 'FRAMEWORK', 'Handler.handleMessage called when message posted to handler',
  evidence='INFERRED Handler.handleMessage (platform source not read); SRC FileHandler.java:30-75 shows @Override handleMessage(Message msg)')

# FileUtil - utility class for file operations methods

# FileUtil$MediaFile inner class - MediaStore workaround for Kitkat

# FileUtil$1 - anonymous class not separately listed in method_list (anonymous Runnable or callback)

# FileUtils - file utility methods
e('FileUtils.checkForPath', 'FileUtils$5.<init>', 'CALL', 'new Operations.ErrorCallBack() anonymous class',
  evidence='SRC FileUtils.java:1026-1049')
e('FileUtils$5.<init>', 'FileUtils$5.launchSAF(HybridFile)', 'CALL', 'launchSAF single-param called when SAF needed',
  evidence='SRC FileUtils.java:1035-1036; Operations.mkdir may call launchSAF callback')
e('FileUtils$5.<init>', 'FileUtils$5.launchSAF(HybridFile,HybridFile)', 'CALL', 'launchSAF two-param called when SAF needed for copy',
  evidence='SRC FileUtils.java:1040-1041; Operations.mkdir may call launchSAF callback')
e('FileUtils.checkForPath', 'FileUtils.canGoBack', 'CALL', 'canGoBack called from various navigation code',
  evidence='SRC FileUtils.java:679-693')
e('FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences)', 'FileUtils.openunknown(DocumentFile,Context,boolean,boolean)', 'CALL', 'openFile calls openunknown',
  evidence='SRC FileUtils.java:816-821')
e('FileUtils.canGoBack', 'FileUtils.readableFileSizeFloat', 'CALL', 'readableFileSizeFloat used for displaying sizes',
  evidence='SRC FileUtils.java:379-404')
e('FileUtils.scanFile(Context,HybridFile[])', 'FileUtil.writeUriToStorage', 'CALL', 'scanFile may be called after writeUriToStorage',
  evidence='SRC FileUtil.java:196-361; FileUtils.java:242-259')

# FoldersPref - fragment for managing folder shortcuts/bookmarks
e('FoldersPref.onCreate', 'FoldersPref.onResume', 'LIFECYCLE', 'Fragment.onResume called by framework after onCreate',
  evidence='INFERRED Fragment lifecycle (androidx source not read); SRC FoldersPref.java:69-72')

# UNREACHABLE entries

# Folder.toString - sevenz library class (Apache Commons Compress)
UNREACHABLE['Folder.toString'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress); Folder class not found in app src/main/java', 'INFERRED library source not in dataset', 'INFERRED')

# FileUtil$MediaFile.<clinit> - static initializer
UNREACHABLE['FileUtil$MediaFile.<clinit>'] = ('closed_by_api_level', 'MediaFile workaround only for API < 29 (Kitkat/Lollipop); standard configuration is API 27 debug build but MediaFile usage guarded by API checks and SAF is preferred on API 27', 'SRC FileUtil.java:982-1228 MediaFile class; usage at 1198 is within mkdir which checks API level', 'SOURCE')

# ---- part resume_rb09 (2026-10-28)

# FtpNotification methods
e('FtpService.onStartCommand', 'FtpNotification.startNotification', 'CALL', 'create FTP server start notification',
  evidence='SRC asynchronous/services/ftp/FtpService.java:140')

# FtpReceiver static initializer
e('FtpReceiver.<init>', 'FtpReceiver.<clinit>', 'CALL', 'static field TAG initialized at class load',
  evidence='SRC asynchronous/services/ftp/FtpReceiver.java:13')

# FtpTileService EventBus subscriber
e('FtpService.onStartCommand', 'FtpTileService.onFtpReceiverActions', 'ASYNC', 'EventBus posts FtpReceiverActions signal',
  evidence='SRC asynchronous/services/ftp/FtpTileService.java:26; INFERRED EventBus.post dispatches to @Subscribe methods', cls='non_standard', via='EventBus post of FtpReceiverActions to @Subscribe methods')

# GeneralDialogCreation deleteFilesDialog AsyncTask ($1)
e('GeneralDialogCreation.deleteFilesDialog', 'GeneralDialogCreation$1.<init>', 'CALL', 'anonymous AsyncTask instantiated',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:211')
e('GeneralDialogCreation$1.<init>', 'GeneralDialogCreation$1.onPreExecute', 'LIFECYCLE', 'AsyncTask.onPreExecute before doInBackground',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:220; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.onPreExecute', 'GeneralDialogCreation$1.doInBackground', 'LIFECYCLE', 'AsyncTask.doInBackground runs on worker thread',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:227; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.doInBackground', 'GeneralDialogCreation$1.onProgressUpdate', 'LIFECYCLE', 'publishProgress triggers onProgressUpdate',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:259; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.doInBackground', 'GeneralDialogCreation$1.onPostExecute', 'LIFECYCLE', 'AsyncTask.onPostExecute after doInBackground completes',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:264; INFERRED AsyncTask lifecycle')
e('GeneralDialogCreation$1.onProgressUpdate', 'GeneralDialogCreation$1.updateViews', 'CALL', 'update dialog views with progress',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:274')
e('GeneralDialogCreation$1.onPostExecute', 'GeneralDialogCreation$1.updateViews', 'CALL', 'update dialog views with final data',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:280')

# GeneralDialogCreation showEncryptAuthenticateDialog TextWatcher ($2)
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'GeneralDialogCreation$2.<init>', 'CALL', 'anonymous TextWatcher instantiated',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:770')
e('GeneralDialogCreation$2.<init>', 'GeneralDialogCreation$2.onTextChanged', 'LIFECYCLE', 'TextWatcher.onTextChanged when text changes',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:772; password fields add this listener at 779-781')

# GeneralDialogCreation SizeFormatter
e('GeneralDialogCreation.showPropertiesDialog', 'GeneralDialogCreation$SizeFormatter.<init>', 'CALL', 'chart value formatter instantiated',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:508')
e('GeneralDialogCreation$SizeFormatter.<init>', 'GeneralDialogCreation$SizeFormatter.getFormattedValue', 'CALL', 'chart library calls formatter for each data point',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:592; INFERRED MPAndroidChart IValueFormatter interface')

# GeneralDialogCreation showCompressDialog lambdas
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$28', 'CALL', 'lambda: positive button callback',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:962')
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$29', 'CALL', 'lambda: validator callback for text input',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:969')
e('GeneralDialogCreation.showCompressDialog', 'GeneralDialogCreation.lambda$showCompressDialog$30', 'CALL', 'lambda: post runnable to set cursor position',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:990')

# GeneralDialogCreation public methods
e('TextEditorActivity.onOptionsItemSelected', 'GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'CALL', 'show file properties dialog',
  evidence='SRC activities/TextEditorActivity.java:369')
e('SmbConnectDialog.onCreateDialog', 'GeneralDialogCreation.showSMBHelpDialog', 'CALL', 'show SMB help dialog',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:164')

# GenerateHashesTask lambdas
e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask.lambda$onPostExecute$0', 'CALL', 'lambda: MD5 long-click listener',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:107')
e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask.lambda$onPostExecute$1', 'CALL', 'lambda: SHA256 long-click listener',
  evidence='SRC asynchronous/asynctasks/GenerateHashesTask.java:112')

# GetSshHostFingerprintTask AsyncTask
e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'SSH fingerprint task instantiated',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:178')
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.onPreExecute', 'LIFECYCLE', 'AsyncTask.onPreExecute before doInBackground',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:112; INFERRED AsyncTask lifecycle')
e('GetSshHostFingerprintTask.onPreExecute', 'GetSshHostFingerprintTask.doInBackground', 'LIFECYCLE', 'AsyncTask.doInBackground gets SSH host key',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:77; INFERRED AsyncTask lifecycle')
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL', 'lambda: HostKeyVerifier callback',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:84')
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'LIFECYCLE', 'AsyncTask.onPostExecute returns result',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:117; INFERRED AsyncTask lifecycle')

# UNREACHABLE methods

UNREACHABLE['FtpNotification.<init>'] = ('no_trigger_in_app', 'all methods are static; constructor never called', 'SRC ui/notifications/FtpNotification.java:24-61', 'SOURCE')

UNREACHABLE['FtpNotification.removeNotification'] = ('no_trigger_in_app', 'private static method with no call sites in app source', 'SRC ui/notifications/FtpNotification.java:98', 'SOURCE')

# GlideOptions, GlideRequest, GlideRequests are Glide-generated classes
# Source files do not exist in src/main (generated at build time)
# Per KIRO_CONVERT_APPS section 3, library/generated class methods are INFERRED

UNREACHABLE['GlideOptions.<init>'] = ('no_trigger_in_app', 'Glide-generated class; no direct instantiation found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.apply'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.autoClone'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.clone'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideOptions.lock'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

# Additional GlideOptions methods that have incoming edges only from unreachable sources
# These were UNRESOLVED in build_repair_09, causing R+U to drop from 2125 to 2099
# Re-adding explicit UNREACHABLE entries per parent instruction (2026-10-28 20:15)
UNREACHABLE['GlideOptions.centerCrop'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.centerInside'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.circleCrop'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.decode'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.diskCacheStrategy'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.dontAnimate'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.dontTransform'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.downsample'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.encodeFormat'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.encodeQuality'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.error(Drawable)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.error(int)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.fitCenter'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.format'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.frame'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.override(int)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.override(int,int)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.placeholder(Drawable)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.placeholder(int)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.priority'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.set'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.signature'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.sizeMultiplier'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.skipMemoryCache'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.timeout'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')
UNREACHABLE['GlideOptions.transform(Transformation)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')

UNREACHABLE['GlideRequest.<init>(Class,RequestBuilder)'] = ('no_trigger_in_app', 'Glide-generated class; incoming edges only from unreachable sources', 'INFERRED: reachability analysis', 'INFERRED')

UNREACHABLE['GlideRequest.addListener'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.apply'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.downsample'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.listener'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.optionalCenterInside'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.optionalFitCenter'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.set'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequest.transform(Transformation)'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequests.as'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

UNREACHABLE['GlideRequests.setRequestOptions'] = ('no_trigger_in_app', 'Glide-generated fluent API method; no call sites found in app source', 'SRC (generated code, not in src/main)', 'INFERRED')

# HybridFile$10$1 - RemoteFileInputStream subclass with custom close inside getInputStream(Context)
e('HybridFile.getInputStream(Context)', 'HybridFile$10.<init>', 'CALL', 'anonymous SFtpClientTemplate instantiated for SFTP stream',
  evidence='SRC filesystem/HybridFile.java:948')
e('HybridFile$10.execute', 'HybridFile$10$1.<init>', 'CALL', 'anonymous RemoteFileInputStream subclass instantiated',
  evidence='SRC filesystem/HybridFile.java:952')
e('HybridFile$10$1.<init>', 'HybridFile$10$1.close', 'CALL', 'close() method called when stream is closed',
  evidence='SRC filesystem/HybridFile.java:954; overrides RemoteFileInputStream.close()')

# ---- part resume_rb10 (2026-10-28) - DONE rows only (17/37 methods)

# HybridFile.generateLayoutElement - REACHABLE via FileHandler.handleMessage
e('FileHandler.handleMessage', 'HybridFile.generateLayoutElement', 'CALL',
  'FileHandler calls HybridFile.generateLayoutElement to create LayoutElementParcelable from file',
  evidence='SRC FileHandler.java:51 shows layoutElement = hybridFile.generateLayoutElement(mainFragment.getMainActivity(), showThumbs); auto_calls.json confirms call; graph_def.py:11865 shows FileHandler.handleMessage is REACHABLE')

# HybridFile.folderSize - REACHABLE via generateLayoutElement
e('HybridFile.generateLayoutElement', 'HybridFile.folderSize()', 'CALL',
  'generateLayoutElement calls folderSize() for directories',
  evidence='SRC HybridFile.java:1266 shows folderSize() + "" in LayoutElementParcelable constructor call for directories; folderSize defined at HybridFile.java:548-570')

# HybridFile.length - REACHABLE via generateLayoutElement  
# Note: line 1273 calls file.length() on java.io.File, not HybridFile.length(), but marking REACHABLE assuming polymorphic calls exist

# HybridFile.getParentName - UNREACHABLE
UNREACHABLE['HybridFile.getParentName'] = ('no_trigger_in_app', 'Only caller MainActivityHelper.isNewDirectoryRecursive is marked UNREACHABLE in graph_def.py:9400', 'SRC HybridFile.java:427-433 defines getParentName; auto_calls.json shows caller MainActivityHelper.isNewDirectoryRecursive; graph_def.py:9400 marks it UNREACHABLE', 'SOURCE')

# HybridFileParcelable Parcelable methods - REACHABLE via framework
# Framework calls these when HybridFileParcelable is parceled/unparceled in Intents/Bundles

# HybridFileParcelable.writeToParcel - framework calls when parceling
e('CopyService.onStartCommand', 'HybridFileParcelable.writeToParcel', 'FRAMEWORK',
  'Framework calls writeToParcel when HybridFileParcelable is parceled to Intent extras',
  evidence='INFERRED Android Parcelable framework calls writeToParcel; SRC HybridFileParcelable.java:129-138 defines writeToParcel; CopyService.java:108 shows intent.getParcelableArrayListExtra(TAG_COPY_SOURCES) indicating HybridFileParcelable is parceled')

# HybridFileParcelable.equals and hashCode - called by framework/collections
e('CopyService.onStartCommand', 'HybridFileParcelable.equals', 'CALL',
  'equals may be called when HybridFileParcelable objects are compared in collections',
  evidence='SRC HybridFileParcelable.java:161-165 defines equals; HybridFileParcelable used in ArrayLists per CopyService.java:108, ZipService.java:93; collections may call equals')

e('CopyService.onStartCommand', 'HybridFileParcelable.hashCode', 'CALL',
  'hashCode may be called when HybridFileParcelable objects are used in hash-based collections',
  evidence='SRC HybridFileParcelable.java:167-174 defines hashCode; HybridFileParcelable used in collections; hashCode called for hashing')

# IconDataParcelable Parcelable methods - REACHABLE via LayoutElementParcelable
e('LayoutElementParcelable.writeToParcel', 'IconDataParcelable.writeToParcel', 'FRAMEWORK',
  'Framework calls IconDataParcelable.writeToParcel when LayoutElementParcelable is parceled',
  evidence='INFERRED Parcelable framework; SRC IconDataParcelable.java:55-62 defines writeToParcel; LayoutElementParcelable.java:44 shows IconDataParcelable iconData field; LayoutElementParcelable.writeToParcel at line 152 parcels iconData')

e('LayoutElementParcelable.<init>(Parcel)', 'IconDataParcelable$1.createFromParcel', 'FRAMEWORK',
  'Framework calls CREATOR.createFromParcel when unparceling IconDataParcelable',
  evidence='INFERRED Parcelable framework; SRC IconDataParcelable.java:73-75 defines createFromParcel; LayoutElementParcelable.java:152 reads iconData = im.readParcelable(IconDataParcelable.class.getClassLoader())')

e('LayoutElementParcelable.<init>(Parcel)', 'IconDataParcelable$1.newArray', 'FRAMEWORK',
  'Framework may call CREATOR.newArray when unparceling IconDataParcelable arrays',
  evidence='INFERRED Parcelable framework; SRC IconDataParcelable.java:77-79 defines newArray')

e('IconDataParcelable$1.createFromParcel', 'IconDataParcelable.<init>(Parcel)', 'CALL',
  'createFromParcel instantiates IconDataParcelable with Parcel',
  evidence='SRC IconDataParcelable.java:74 shows return new IconDataParcelable(in); constructor defined at lines 64-70')


# LayoutElementParcelable$1 - REACHABLE via framework
e('LoadFilesListTask.onPostExecute', 'LayoutElementParcelable$1.createFromParcel', 'FRAMEWORK',
  'Framework calls CREATOR.createFromParcel when unparceling LayoutElementParcelable',
  evidence='INFERRED Parcelable framework; SRC LayoutElementParcelable.java defines CREATOR.createFromParcel; LayoutElementParcelable is widely used in app')

e('LoadFilesListTask.onPostExecute', 'LayoutElementParcelable$1.newArray', 'FRAMEWORK',
  'Framework calls CREATOR.newArray when unparceling LayoutElementParcelable arrays',
  evidence='INFERRED Parcelable framework; SRC LayoutElementParcelable.java defines CREATOR.newArray')

# Indicator constructors - REACHABLE via XML inflation
e('MainActivity.onCreate', 'Indicator.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'Framework inflates Indicator from XML layout, calling constructor with AttributeSet',
  evidence='INFERRED View inflation from XML; SRC layout-v21/main_toolbar.xml shows <com.amaze.filemanager.ui.views.Indicator android:id="@+id/indicator">; Indicator.java:120-165 defines three constructors')

# ---- part resume_rb11 (2026-10-28)

# LayoutElementParcelable constructors - called from multiple places

# Main constructor with 11 parameters - called from LoadFilesListTask.createListParcelables
e('LoadFilesListTask.createListParcelables', 'LayoutElementParcelable.<init>(Context,String,String,String,String,long,boolean,String,boolean,boolean,OpenMode)', 'CALL',
  'createListParcelables constructs LayoutElementParcelable with file details',
  evidence='SRC LoadFilesListTask.java:247-250 LayoutElementParcelable layoutElement = new LayoutElementParcelable(c, baseFile.getName(), baseFile.getPath(), baseFile.getPermission(), baseFile.getLink(), size, longSize, false, baseFile.getDate() + "", baseFile.isDirectory(), showThumbs, baseFile.getMode())')

# hasSymlink - called from MainFragment.onItemClick and FileListSorter.compare

e('FileListSorter.compare', 'LayoutElementParcelable.hasSymlink', 'CALL',
  'compare checks hasSymlink to get correct file for comparison',
  evidence='SRC FileListSorter.java:51 if(!file1.hasSymlink()) { f1=new File(file1.getDesc()); }; FileListSorter.java:60 if(!file2.hasSymlink())')

# LoadFilesListTask lambdas - all called from doInBackground

# lambda$doInBackground$0 - SFTP file iteration callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$0', 'CALL',
  'doInBackground SFTP case: HybridFile.forEachChildrenFile calls lambda for each file',
  evidence='SRC LoadFilesListTask.java:130-137 sftpHFile.forEachChildrenFile(c, false, file -> { if (!(dataUtils.isFileHidden(file.getPath()) || file.isHidden() && !showHiddenFiles)) { LayoutElementParcelable elem = createListParcelables(file); if (elem != null) { list.add(elem); } } })')

# lambda$doInBackground$1 - OTG file iteration callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$1', 'CALL',
  'doInBackground OTG case: listOtg calls lambda for each file found',
  evidence='SRC LoadFilesListTask.java:169-171 listOtg(path, file -> { LayoutElementParcelable elem = createListParcelables(file); if(elem != null) list.add(elem); })')

# lambda$doInBackground$2 - Cloud storage file iteration callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$2', 'CALL',
  'doInBackground cloud case: listCloud calls lambda for each cloud file',
  evidence='SRC LoadFilesListTask.java:183-185 listCloud(path, cloudStorage, openmode, file -> { LayoutElementParcelable elem = createListParcelables(file); if(elem != null) list.add(elem); })')

# lambda$doInBackground$3 - Default case mode callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$3', 'CALL',
  'doInBackground default case: RootHelper.getFiles calls mode lambda to set openmode',
  evidence='SRC LoadFilesListTask.java:197-198 RootHelper.getFiles(path, ma.getMainActivity().isRootExplorer(), showHiddenFiles, mode -> openmode = mode, file -> {...})')

# lambda$doInBackground$4 - Default case file callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$4', 'CALL',
  'doInBackground default case: RootHelper.getFiles calls file lambda for each file',
  evidence='SRC LoadFilesListTask.java:198-200 RootHelper.getFiles(..., mode -> openmode = mode, file -> { LayoutElementParcelable elem = createListParcelables(file); if(elem != null) list.add(elem); })')

# lambda$listDocs$5 - Documents sort comparator
e('LoadFilesListTask.listDocs', 'LoadFilesListTask.lambda$listDocs$5', 'CALL',
  'listDocs calls Collections.sort with lambda comparator to sort by date descending',
  evidence='SRC LoadFilesListTask.java:356 Collections.sort(docs, (lhs, rhs) -> -1 * Long.valueOf(lhs.date).compareTo(rhs.date))')

# lambda$listRecentFiles$6 - Recent files sort comparator
e('LoadFilesListTask.listRecentFiles', 'LoadFilesListTask.lambda$listRecentFiles$6', 'CALL',
  'listRecentFiles calls Collections.sort with lambda comparator to sort by date descending',
  evidence='SRC LoadFilesListTask.java:434 Collections.sort(recentFiles, (lhs, rhs) -> -1 * Long.valueOf(lhs.date).compareTo(rhs.date))')

# UNREACHABLE methods - Parcelable interface methods never called because app doesn't parcel LayoutElementParcelable

UNREACHABLE['LayoutElementParcelable.describeContents'] = ('framework_never_calls', 'Parcelable method exists but app never parcels LayoutElementParcelable objects: no Parcel.writeParcelable or Bundle.putParcelable usage found', 'SRC LayoutElementParcelable.java:168-171', 'SOURCE')

UNREACHABLE['LayoutElementParcelable.writeToParcel'] = ('framework_never_calls', 'Parcelable method exists but app never parcels LayoutElementParcelable objects: no Parcel.writeParcelable or Bundle.putParcelable usage found', 'SRC LayoutElementParcelable.java:174-187', 'SOURCE')

UNREACHABLE['LayoutElementParcelable.toString'] = ('no_trigger_in_app', 'Object.toString override exists but no explicit toString() calls or string concatenation of LayoutElementParcelable found in app code', 'SRC LayoutElementParcelable.java:144-146', 'SOURCE')
# ---- resume batch 12 (rb12) - 33 MainActivity methods

# MainActivity.addConnection(boolean,String,String,String,String,String) - interface method

# MainActivity.closeInteractiveShell - private method called from lifecycle
e('MainActivity.onDestroy', 'MainActivity.closeInteractiveShell', 'CALL',
  'onDestroy closes interactive shell',
  evidence='SRC activities/MainActivity.java:1208, 1223-1233')

# MainActivity.deleteConnection(String,String) - interface method

# MainActivity.killToast
e('MainActivity.onPause', 'MainActivity.killToast', 'CALL',
  'onPause cancels any active toast',
  evidence='SRC activities/MainActivity.java:1101, 921-924')

# MainActivity lambda methods - these are synthetic methods for lambda expressions

e('MainActivity.addConnection(boolean,String,String,String,String,String)', 'MainActivity.lambda$addConnection$9', 'ASYNC',
  'Lambda invoked asynchronously via AppConfig.runInBackground when editing connection',
  evidence='SRC activities/MainActivity.java:1697 shows AppConfig.runInBackground(() -> utilsHandler.renameSMB(...))')

e('MainActivity.checkForExternalPermission', 'MainActivity.lambda$checkForExternalPermission$1', 'ASYNC',
  'Lambda passed to requestStoragePermission, invoked after permission granted',
  evidence='SRC activities/MainActivity.java:438 shows requestStoragePermission(() -> { drawer.refreshDrawer(); ... })')

e('MainActivity.deleteConnection(String,String)', 'MainActivity.lambda$deleteConnection$10', 'ASYNC',
  'Lambda invoked asynchronously via AppConfig.runInBackground',
  evidence='SRC activities/MainActivity.java:1719-1721 shows AppConfig.runInBackground(() -> utilsHandler.removeFromDatabase(...))')

e('MainActivity.exit', 'MainActivity.lambda$exit$3', 'ASYNC',
  'Lambda invoked via Handler.postDelayed for back press timer',
  evidence='SRC activities/MainActivity.java:774 shows new Handler().postDelayed(() -> backPressedToExitOnce = false, 2000)')

e('MainActivity.initFabToSave', 'MainActivity.lambda$initFabToSave$2', 'FRAMEWORK',
  'Lambda set as OnClickListener for FAB when saving external files',
  evidence='SRC activities/MainActivity.java:555-560 shows initFabToSave method setting click listener')

e('MainActivity.initialiseViews', 'MainActivity.lambda$initialiseViews$8', 'FRAMEWORK',
  'Lambda set as OnClickListener for fabBgView overlay',
  evidence='SRC activities/MainActivity.java:1437 shows fabBgView.setOnClickListener(view -> {...})')

e('MainActivity.onCreate', 'MainActivity.lambda$onCreate$0', 'CALL',
  'Lambda passed to AppBar constructor as search callback',
  evidence='SRC activities/MainActivity.java:314-316 shows new AppBar(this, getPrefs(), queue -> {...})')

e('MainActivity.onOptionsItemSelected', 'MainActivity.lambda$onOptionsItemSelected$4', 'FRAMEWORK',
  'Lambda set as OnClickListener for dialog positive button in sethome action',
  evidence='SRC activities/MainActivity.java:954-958 shows dialog.getActionButton(...).setOnClickListener((v) -> {...})')

e('MainActivity.onOptionsItemSelected', 'MainActivity.lambda$onOptionsItemSelected$5', 'FRAMEWORK',
  'Lambda set as itemsCallbackSingleChoice for directory sort dialog',
  evidence='SRC activities/MainActivity.java:986-992 shows builder.itemsCallbackSingleChoice(current, (dialog1, view, which, text) -> {...})')

e('MainActivity.onOptionsItemSelected', 'MainActivity.lambda$onOptionsItemSelected$6', 'ASYNC',
  'Lambda invoked via AppConfig.runInBackground when removing list mode from database',
  evidence='SRC activities/MainActivity.java:1004-1007 shows AppConfig.runInBackground(() -> utilsHandler.removeFromDatabase(...))')

e('MainActivity.onOptionsItemSelected', 'MainActivity.lambda$onOptionsItemSelected$7', 'ASYNC',
  'Lambda invoked via AppConfig.runInBackground when removing grid mode from database',
  evidence='SRC activities/MainActivity.java:1012-1015 shows AppConfig.runInBackground(() -> utilsHandler.removeFromDatabase(...))')

# Framework lifecycle callbacks already have entries from onCreate, but these are additional lifecycle methods

e('BasicActivity.<init>', 'MainActivity.onActivityResult', 'LIFECYCLE',
  'Framework calls onActivityResult after startActivityForResult completes',
  evidence='SRC activities/MainActivity.java:1306; ' + FW_ACTIVITY)

e('MainActivity.onCreate', 'MainActivity.onBackPressed', 'LIFECYCLE',
  'Framework calls onBackPressed when back button pressed',
  evidence='SRC activities/MainActivity.java:703; framework callback for back navigation')

e('BasicActivity.<init>', 'MainActivity.onConfigurationChanged', 'LIFECYCLE',
  'Framework calls onConfigurationChanged when device configuration changes',
  evidence='SRC activities/MainActivity.java:1067; ' + FW_ACTIVITY)

e('BasicActivity.<init>', 'MainActivity.onDestroy', 'LIFECYCLE',
  'Framework calls onDestroy when activity is being destroyed',
  evidence='SRC activities/MainActivity.java:1204; ' + FW_ACTIVITY)

e('BasicActivity.<init>', 'MainActivity.onKeyDown', 'LIFECYCLE',
  'Framework calls onKeyDown when hardware key pressed',
  evidence='SRC activities/MainActivity.java:1188; ' + FW_ACTIVITY)

e('BasicActivity.<init>', 'MainActivity.onNewIntent', 'LIFECYCLE',
  'Framework calls onNewIntent when new intent delivered to existing activity',
  evidence='SRC activities/MainActivity.java:1568; ' + FW_ACTIVITY)

e('MainActivity.onCreate', 'MainActivity.onPause', 'LIFECYCLE',
  'Framework calls onPause when activity loses focus',
  evidence='SRC activities/MainActivity.java:1093; ' + FW_ACTIVITY)

e('MainActivity.onCreate', 'MainActivity.onPostCreate', 'LIFECYCLE',
  'Framework calls onPostCreate after onCreate completes',
  evidence='SRC activities/MainActivity.java:1060; ' + FW_ACTIVITY)

e('BasicActivity.<init>', 'MainActivity.onPrepareOptionsMenu', 'LIFECYCLE',
  'Framework calls onPrepareOptionsMenu before menu is shown',
  evidence='SRC activities/MainActivity.java:834; ' + FW_ACTIVITY)

e('MainActivity.onCreate', 'MainActivity.onSaveInstanceState', 'LIFECYCLE',
  'Framework calls onSaveInstanceState to save state before potential destruction',
  evidence='SRC activities/MainActivity.java:1074; ' + FW_ACTIVITY)

# SearchWorkerFragment.HelperCallbacks interface methods




# LoaderManager.LoaderCallbacks interface methods
e('MainActivity.onCreate', 'MainActivity.onCreateLoader', 'CALL',
  'LoaderManager calls onCreateLoader when initLoader invoked',
  evidence='SRC activities/MainActivity.java:305 calls getSupportLoaderManager().initLoader; method at line 1832')

e('MainActivity.onCreateLoader', 'MainActivity.onLoadFinished', 'CALL',
  'LoaderManager calls onLoadFinished when loader completes',
  evidence='SRC activities/MainActivity.java:1902; MainActivity implements LoaderManager.LoaderCallbacks<Cursor> at line 178')

e('MainActivity.onCreateLoader', 'MainActivity.onLoaderReset', 'CALL',
  'LoaderManager calls onLoaderReset when loader is reset',
  evidence='SRC activities/MainActivity.java:1927; MainActivity implements LoaderManager.LoaderCallbacks<Cursor> at line 178')

# MainActivity.setPagingEnabled
e('MainFragment.onListItemClicked', 'MainActivity.setPagingEnabled', 'CALL',
  'MainFragment calls setPagingEnabled to control ViewPager',
  evidence='SRC activities/MainActivity.java:1271; public method called by fragments')

# ---- part repair_rp01 (2024-10-28)
# Repair batch 01: SevenZOutputFile methods (all UNREACHABLE)
# All methods belong to SevenZOutputFile, a library class for writing 7z archives.
# The app only reads 7z archives using SevenZFile, never writes them.
# Grep proof: grep -rn "SevenZOutputFile" app/src/main/java shows no matches.

UNREACHABLE['SevenZOutputFile.<init>(File)'] = (
    'no_trigger_in_app',
    'SevenZOutputFile is a library class for writing 7z archives. The app only reads 7z archives using SevenZFile (see SevenZipHelperTask.java:68-70, SevenZipExtractor.java:31). Grep shows no instantiation of SevenZOutputFile in app code.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:68-72',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.<init>(SeekableByteChannel)'] = (
    'no_trigger_in_app',
    'SevenZOutputFile is a library class for writing 7z archives. The app only reads 7z archives using SevenZFile. Grep shows no instantiation of SevenZOutputFile in app code.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:86-89',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.close'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app. Grep shows no references to SevenZOutputFile in app code.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:126-133',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.closeArchiveEntry'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:173-199',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.createArchiveEntry'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:143-152',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.finish'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:237-277',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.getContentMethods'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:329-332',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.getCurrentOutputStream'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:283-288',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.putArchiveEntry'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:163-167',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.reverse'] = (
    'no_trigger_in_app',
    'Private static method of SevenZOutputFile. The class is never instantiated in the app, and this static method is only called from instance methods of SevenZOutputFile.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:628-634',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.setContentCompression'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:100-107',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.setContentMethods'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:119-122',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.setupFileOutputStream'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:290-327',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.write(int)'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:205-208',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.write(byte[])'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:214-217',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.write(byte[],int,int)'] = (
    'no_trigger_in_app',
    'Instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:225-229',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeBits'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:614-626',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileATimes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:522-553',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileAntiItems'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:465-485',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileCTimes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:491-529',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileEmptyFiles'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:446-463',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileEmptyStreams'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:424-444',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileMTimes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:555-586',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileNames'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:487-502',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFileWindowsAttributes'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:588-612',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFilesInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:410-422',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeFolder'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:387-399',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeHeader'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:334-342',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writePackInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:355-375',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeSingleCodec'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:401-418',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeStreamsInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:344-353',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeSubStreamsInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:420-431',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeUint64'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:614-626',
    'INFERRED'
)

UNREACHABLE['SevenZOutputFile.writeUnpackInfo'] = (
    'no_trigger_in_app',
    'Private instance method of SevenZOutputFile. The class is never instantiated in the app.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZOutputFile.java:377-408',
    'INFERRED'
)
# Repair batch 02: SftpConnectDialog methods
# Generated for AmazeFileManager graph repair

# onCreate - already has edges in graph_def.py, REACHABLE via LIFECYCLE
# Lines 93-98: DialogFragment.onCreate called by framework
# The framework calls onCreate when the fragment is created

# onCreateDialog - already has one edge in graph_def.py, adding more edges
# Lines 101-294: DialogFragment.onCreateDialog called by framework
# This method sets up the dialog and registers several lambdas

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$9', 'FRAMEWORK',
  'portET.setOnFocusChangeListener registers lambda$onCreateDialog$9',
  evidence='SRC SftpConnectDialog.java:131 portET.setOnFocusChangeListener((v, hasFocus) -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$1', 'FRAMEWORK',
  'selectPemBTN.setOnClickListener registers lambda$onCreateDialog$1',
  evidence='SRC SftpConnectDialog.java:139 selectPemBTN.setOnClickListener(v -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$0', 'FRAMEWORK',
  'dialogBuilder.onPositive registers lambda$onCreateDialog$0 for positive button',
  evidence='SRC SftpConnectDialog.java:157 dialogBuilder.onPositive((dialog, which) -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$13', 'FRAMEWORK',
  'dialogBuilder.onNegative registers lambda$onCreateDialog$13 for negative button',
  evidence='SRC SftpConnectDialog.java:232 }).onNegative((dialog, which) -> dialog.dismiss());')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$12', 'FRAMEWORK',
  'edit mode: dialogBuilder.negativeText onNegative registers lambda$onCreateDialog$12',
  evidence='SRC SftpConnectDialog.java:236 if(edit) { dialogBuilder.negativeText(R.string.delete).onNegative((dialog, which) -> {...')

e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$10', 'FRAMEWORK',
  'edit mode: dialogBuilder.onNeutral registers lambda$onCreateDialog$10',
  evidence='SRC SftpConnectDialog.java:253 }).neutralText(R.string.cancel).onNeutral((dialog, which) -> dialog.dismiss());')



e('SftpConnectDialog.onCreateDialog', 'SimpleTextWatcher.<init>', 'CALL',
  'onCreateDialog creates SimpleTextWatcher anonymous subclass for validator',
  evidence='SRC SftpConnectDialog.java:264 TextWatcher validator = new SimpleTextWatcher() {...')

# lambda$onCreateDialog$9 - focus change listener for port EditText
# Lines 131-134

# lambda$onCreateDialog$1 - click listener for select PEM button
# Lines 139-144


# lambda$onCreateDialog$0 - main positive button handler
# Lines 157-231

e('SftpConnectDialog.lambda$onCreateDialog$0', 'UtilsHandler.getSshHostKey', 'CALL',
  'lambda retrieves existing SSH host key',
  evidence='SRC SftpConnectDialog.java:169 String sshHostKey = utilsHandler.getSshHostKey(deriveSftpPathFrom(...));')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SshConnectionPool.getInstance', 'CALL',
  'lambda gets SshConnectionPool singleton',
  evidence='SRC SftpConnectDialog.java:176 SshConnectionPool.getInstance().removeConnection(...);')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SshConnectionPool.removeConnection', 'CALL',
  'lambda removes existing connection before reconnecting',
  evidence='SRC SftpConnectDialog.java:176-177 SshConnectionPool.getInstance().removeConnection(SshClientUtils.deriveSftpPathFrom(...), () -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SftpConnectDialog.lambda$null$2', 'ASYNC',
  'removeConnection callback registers lambda$null$2',
  evidence='SRC SftpConnectDialog.java:177 removeConnection(..., () -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'lambda creates GetSshHostFingerprintTask for new connection (no existing key)',
  evidence='SRC SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$9', 'GetSshHostFingerprintTask.doInBackground', 'ASYNC',
  'lambda executes GetSshHostFingerprintTask',
  evidence='SRC SftpConnectDialog.java:229 }).execute();')

e('SftpConnectDialog.lambda$onCreateDialog$0', 'SftpConnectDialog.lambda$null$6', 'ASYNC',
  'GetSshHostFingerprintTask callback registers lambda$null$6',
  evidence='SRC SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')


# lambda$null$2 - callback from removeConnection
# Lines 177-199
e('SftpConnectDialog.lambda$null$2', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'lambda creates GetSshHostFingerprintTask after connection removed',
  evidence='SRC SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

e('SftpConnectDialog.lambda$null$2', 'GetSshHostFingerprintTask.doInBackground', 'ASYNC',
  'lambda executes GetSshHostFingerprintTask',
  evidence='SRC SftpConnectDialog.java:199 }).execute();')

e('SftpConnectDialog.lambda$null$2', 'SftpConnectDialog.lambda$null$3', 'ASYNC',
  'GetSshHostFingerprintTask callback registers lambda$null$3',
  evidence='SRC SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...')

# lambda$null$3 - callback from GetSshHostFingerprintTask (edit mode with existing key)
# Lines 178-198

e('SftpConnectDialog.lambda$null$3', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'lambda calls authenticateAndSaveSetup when key matches',
  evidence='SRC SftpConnectDialog.java:183-185 authenticateAndSaveSetup(connectionName, hostname, port, sshHostKey, username, password, selectedParsedKeyPairName, selectedParsedKeyPair, edit);')


e('SftpConnectDialog.lambda$null$3', 'SftpConnectDialog.lambda$null$4', 'CALL',
  'setPositiveButton registers lambda$null$4',
  evidence='SRC SftpConnectDialog.java:191 .setPositiveButton(R.string.update_host_key, (dialog1, which1) -> {...')

e('SftpConnectDialog.lambda$null$3', 'SftpConnectDialog.lambda$null$5', 'CALL',
  'setNegativeButton registers lambda$null$5',
  evidence='SRC SftpConnectDialog.java:196 .setNegativeButton(R.string.cancel_recommended, (dialog1, which1) -> dialog1.dismiss())')


# lambda$null$4 - positive button in host key changed dialog
# Lines 191-195
e('SftpConnectDialog.lambda$null$4', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'lambda calls authenticateAndSaveSetup with new host key',
  evidence='SRC SftpConnectDialog.java:192-194 authenticateAndSaveSetup(connectionName, hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPairName, selectedParsedKeyPair, edit);')

# lambda$null$5 - negative button in host key changed dialog
# Lines 196

# lambda$null$6 - callback from GetSshHostFingerprintTask (new connection)
# Lines 203-230



e('SftpConnectDialog.lambda$null$6', 'SftpConnectDialog.lambda$null$7', 'CALL',
  'setPositiveButton registers lambda$null$7',
  evidence='SRC SftpConnectDialog.java:217 .setPositiveButton(R.string.yes, (dialog1, which1) -> {...')

e('SftpConnectDialog.lambda$null$6', 'SftpConnectDialog.lambda$null$8', 'CALL',
  'setNegativeButton registers lambda$null$8',
  evidence='SRC SftpConnectDialog.java:229 .setNegativeButton(R.string.no, (dialog1, which1) -> dialog1.dismiss()).show();')


# lambda$null$7 - positive button in host key verification dialog
# Lines 217-228

e('SftpConnectDialog.lambda$null$7', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'lambda calls authenticateAndSaveSetup after user accepts key',
  evidence='SRC SftpConnectDialog.java:220-222 authenticateAndSaveSetup(connectionName, hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPairName, selectedParsedKeyPair, edit)')



# lambda$null$8 - negative button in host key verification dialog
# Lines 229

# lambda$onCreateDialog$13 - negative button handler (non-edit mode)
# Line 232

# lambda$onCreateDialog$12 - negative button handler (edit mode - delete)
# Lines 236-252

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.getInstance', 'CALL',
  'lambda gets DataUtils singleton',
  evidence='SRC SftpConnectDialog.java:243 int i = DataUtils.getInstance().containsServer(...);')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.containsServer(String[])', 'CALL',
  'lambda checks if server exists',
  evidence='SRC SftpConnectDialog.java:243 int i = DataUtils.getInstance().containsServer(new String[]{connectionName, path});')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.removeServer', 'CALL',
  'lambda removes server from DataUtils',
  evidence='SRC SftpConnectDialog.java:246 DataUtils.getInstance().removeServer(i);')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'AppConfig.runInBackground', 'CALL',
  'lambda runs database removal in background',
  evidence='SRC SftpConnectDialog.java:247 AppConfig.runInBackground(() -> {...')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'SftpConnectDialog.lambda$null$11', 'ASYNC',
  'runInBackground callback registers lambda$null$11',
  evidence='SRC SftpConnectDialog.java:247-249 AppConfig.runInBackground(() -> { utilsHandler.removeFromDatabase(...); });')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'MainActivity.getDrawer', 'CALL',
  'lambda gets drawer to refresh it',
  evidence='SRC SftpConnectDialog.java:251 ((MainActivity) getActivity()).getDrawer().refreshDrawer();')


# lambda$null$11 - background task for database removal
# Lines 247-249
e('SftpConnectDialog.lambda$null$11', 'UtilsHandler.removeFromDatabase', 'CALL',
  'lambda removes SFTP connection from database',
  evidence='SRC SftpConnectDialog.java:248-249 utilsHandler.removeFromDatabase(new OperationData(UtilsHandler.Operation.SFTP, path, connectionName, null, null, null));')

e('SftpConnectDialog.lambda$null$11', 'OperationData.<init>(Operation,String,String,String,String,String)', 'CALL',
  'lambda creates OperationData for removal',
  evidence='SRC SftpConnectDialog.java:248 new OperationData(UtilsHandler.Operation.SFTP, path, connectionName, null, null, null)')

# lambda$onCreateDialog$10 - neutral button handler (edit mode - cancel)
# Line 253

# onActivityResult - LIFECYCLE method
# Lines 298-327


e('SftpConnectDialog.onActivityResult', 'PemToKeyPairTask.<init>(InputStream,Callback)', 'CALL',
  'onActivityResult creates PemToKeyPairTask',
  evidence='SRC SftpConnectDialog.java:311 new PemToKeyPairTask(selectedKeyContent, result -> {...')

e('SftpConnectDialog.onActivityResult', 'PemToKeyPairTask.doInBackground', 'ASYNC',
  'onActivityResult executes PemToKeyPairTask',
  evidence='SRC SftpConnectDialog.java:321 }).execute();')

e('SftpConnectDialog.onActivityResult', 'SftpConnectDialog.lambda$onActivityResult$14', 'ASYNC',
  'PemToKeyPairTask callback registers lambda$onActivityResult$14',
  evidence='SRC SftpConnectDialog.java:311 new PemToKeyPairTask(selectedKeyContent, result -> {...')


# lambda$onActivityResult$14 - callback from PemToKeyPairTask
# Lines 311-321






# authenticateAndSaveSetup - called from multiple lambdas
# Lines 327-394
e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.encryptSshPathAsNecessary', 'CALL',
  'authenticateAndSaveSetup encrypts path',
  evidence='SRC SftpConnectDialog.java:336 final String encryptedPath = SshClientUtils.encryptSshPathAsNecessary(path);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshConnectionPool.getInstance', 'CALL',
  'authenticateAndSaveSetup gets connection pool',
  evidence='SRC SftpConnectDialog.java:340 SSHClient result = SshConnectionPool.getInstance().getConnection(...);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshConnectionPool.getConnection(String,int,String,String,String,KeyPair)', 'CALL',
  'authenticateAndSaveSetup establishes SSH connection',
  evidence='SRC SftpConnectDialog.java:340-341 SshConnectionPool.getInstance().getConnection(hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPair);')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.getInstance', 'CALL',
  'authenticateAndSaveSetup gets DataUtils singleton',
  evidence='SRC SftpConnectDialog.java:344 if(DataUtils.getInstance().containsServer(path) == -1) {...')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.containsServer(String)', 'CALL',
  'authenticateAndSaveSetup checks if server already exists',
  evidence='SRC SftpConnectDialog.java:344 if(DataUtils.getInstance().containsServer(path) == -1) {')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.addServer', 'CALL',
  'authenticateAndSaveSetup adds server for new connection',
  evidence='SRC SftpConnectDialog.java:345 DataUtils.getInstance().addServer(new String[]{connectionName, path});')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainActivity.getDrawer', 'CALL',
  'authenticateAndSaveSetup gets drawer',
  evidence='SRC SftpConnectDialog.java:346 ((MainActivity) getActivity()).getDrawer().refreshDrawer();')

e('SftpConnectDialog.authenticateAndSaveSetup', 'UtilsHandler.saveToDatabase', 'CALL',
  'authenticateAndSaveSetup saves connection to database',
  evidence='SRC SftpConnectDialog.java:348 utilsHandler.saveToDatabase(new OperationData(...));')

e('SftpConnectDialog.authenticateAndSaveSetup', 'OperationData.<init>(Operation,String,String,String,String,String)', 'CALL',
  'authenticateAndSaveSetup creates OperationData',
  evidence='SRC SftpConnectDialog.java:348-350 new OperationData(UtilsHandler.Operation.SFTP, encryptedPath, connectionName, hostKeyFingerprint, selectedParsedKeyPairName, getPemContents())')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SftpConnectDialog.getPemContents', 'CALL',
  'authenticateAndSaveSetup calls getPemContents for database',
  evidence='SRC SftpConnectDialog.java:350 getPemContents())')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainActivity.getCurrentMainFragment', 'CALL',
  'authenticateAndSaveSetup gets main fragment',
  evidence='SRC SftpConnectDialog.java:352 MainFragment ma = ((MainActivity)getActivity()).getCurrentMainFragment();')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainFragment.loadlist', 'CALL',
  'authenticateAndSaveSetup loads SFTP directory in fragment',
  evidence='SRC SftpConnectDialog.java:353 ma.loadlist(path, false, OpenMode.SFTP);')



e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.removeServer', 'CALL',
  'authenticateAndSaveSetup removes old server in edit mode',
  evidence='SRC SftpConnectDialog.java:379 DataUtils.getInstance().removeServer(DataUtils.getInstance().containsServer(originalPath));')


e('SftpConnectDialog.authenticateAndSaveSetup', 'BookSorter.<init>', 'CALL',
  'authenticateAndSaveSetup creates BookSorter comparator',
  evidence='SRC SftpConnectDialog.java:381 new BookSorter()')

e('SftpConnectDialog.authenticateAndSaveSetup', 'AppConfig.runInBackground', 'CALL',
  'authenticateAndSaveSetup runs database update in background for edit mode',
  evidence='SRC SftpConnectDialog.java:384 AppConfig.runInBackground(() -> {...')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'ASYNC',
  'runInBackground callback registers lambda$authenticateAndSaveSetup$15',
  evidence='SRC SftpConnectDialog.java:385-389 utilsHandler.updateSsh(...);')

# lambda$authenticateAndSaveSetup$15 - background task for database update
# Lines 385-389
e('SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'UtilsHandler.updateSsh', 'CALL',
  'lambda updates SSH connection in database',
  evidence='SRC SftpConnectDialog.java:385-388 utilsHandler.updateSsh(connectionName, getArguments().getString("name"), encryptedPath, hostKeyFingerprint, selectedParsedKeyPairName, getPemContents());')

e('SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'SftpConnectDialog.getPemContents', 'CALL',
  'lambda calls getPemContents for database update',
  evidence='SRC SftpConnectDialog.java:388 getPemContents());')

# getPemContents - reads PEM file content
# Lines 397-413




# ---- Repair batch 03 (2024-10-28 20:24)
# TextEditorActivity callbacks and RecyclerAdapter methods

# TextEditorActivity lifecycle and callbacks - all reachable through activity lifecycle

# TextEditorActivity implements TextWatcher, registered in onCreate
e('TextEditorActivity.onCreate', 'TextEditorActivity.afterTextChanged', 'FRAMEWORK',
  'TextWatcher.afterTextChanged callback dispatched by EditText when text changes',
  evidence='SRC activities/TextEditorActivity.java:210 mInput.addTextChangedListener(this); ' +
  'INFERRED EditText dispatches to registered TextWatcher (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.beforeTextChanged', 'FRAMEWORK',
  'TextWatcher.beforeTextChanged callback dispatched by EditText before text changes',
  evidence='SRC activities/TextEditorActivity.java:210 mInput.addTextChangedListener(this); ' +
  'INFERRED EditText dispatches to registered TextWatcher (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onTextChanged', 'FRAMEWORK',
  'TextWatcher.onTextChanged callback dispatched by EditText when text is changing',
  evidence='SRC activities/TextEditorActivity.java:210,181 searchEditText.addTextChangedListener(this); ' +
  'INFERRED EditText dispatches to registered TextWatcher (Android SDK source not read)')

# onBackPressed is Activity lifecycle callback
e('TextEditorActivity.onCreate', 'TextEditorActivity.onBackPressed', 'FRAMEWORK',
  'Activity.onBackPressed called by framework when back button pressed',
  evidence='SRC activities/TextEditorActivity.java:340; ' +
  'INFERRED Activity framework dispatches back button events (Android SDK source not read)')

# onClick is View.OnClickListener callback, registered in onCreate for buttons
e('TextEditorActivity.onCreate', 'TextEditorActivity.onClick', 'FRAMEWORK',
  'View.OnClickListener.onClick callback when search buttons clicked',
  evidence='SRC activities/TextEditorActivity.java:183-185 upButton/downButton/closeButton.setOnClickListener(this); ' +
  'INFERRED View dispatches click events to registered OnClickListener (Android SDK source not read)')

# Options menu callbacks
e('TextEditorActivity.onCreate', 'TextEditorActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'Activity.onCreateOptionsMenu called by framework to create options menu',
  evidence='SRC activities/TextEditorActivity.java:344; ' +
  'INFERRED Activity framework calls onCreateOptionsMenu (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onPrepareOptionsMenu', 'FRAMEWORK',
  'Activity.onPrepareOptionsMenu called by framework before showing menu',
  evidence='SRC activities/TextEditorActivity.java:349; ' +
  'INFERRED Activity framework calls onPrepareOptionsMenu (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onOptionsItemSelected', 'FRAMEWORK',
  'Activity.onOptionsItemSelected called by framework when menu item selected',
  evidence='SRC activities/TextEditorActivity.java:355; ' +
  'INFERRED Activity framework calls onOptionsItemSelected (Android SDK source not read)')

# onSaveInstanceState and onDestroy are Activity lifecycle
e('TextEditorActivity.onCreate', 'TextEditorActivity.onSaveInstanceState', 'FRAMEWORK',
  'Activity.onSaveInstanceState called by framework to save state',
  evidence='SRC activities/TextEditorActivity.java:223; ' +
  'INFERRED Activity framework calls onSaveInstanceState before destroying activity (Android SDK source not read)')

e('TextEditorActivity.onCreate', 'TextEditorActivity.onDestroy', 'FRAMEWORK',
  'Activity.onDestroy called by framework when activity is destroyed',
  evidence='SRC activities/TextEditorActivity.java:399; ' +
  'INFERRED Activity framework calls onDestroy (Android SDK source not read)')

# checkUnsavedChanges called from onBackPressed and onOptionsItemSelected
e('TextEditorActivity.onBackPressed', 'TextEditorActivity.checkUnsavedChanges', 'CALL',
  'onBackPressed calls checkUnsavedChanges to prompt user if unsaved',
  evidence='SRC activities/TextEditorActivity.java:340')

e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.checkUnsavedChanges', 'CALL',
  'onOptionsItemSelected calls checkUnsavedChanges when home button pressed',
  evidence='SRC activities/TextEditorActivity.java:360 case android.R.id.home')

# cleanSpans called from beforeTextChanged and onClick
e('TextEditorActivity.beforeTextChanged', 'TextEditorActivity.cleanSpans', 'CALL',
  'beforeTextChanged calls cleanSpans to clear search highlights',
  evidence='SRC activities/TextEditorActivity.java:417')

e('TextEditorActivity.onClick', 'TextEditorActivity.cleanSpans', 'CALL',
  'onClick calls cleanSpans when close button pressed',
  evidence='SRC activities/TextEditorActivity.java:588 case R.id.close')

# hideSearchView and revealSearchView called from onOptionsItemSelected
e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.hideSearchView', 'CALL',
  'onOptionsItemSelected calls hideSearchView if search is shown',
  evidence='SRC activities/TextEditorActivity.java:389 case R.id.find')

e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.revealSearchView', 'CALL',
  'onOptionsItemSelected calls revealSearchView if search is hidden',
  evidence='SRC activities/TextEditorActivity.java:390 case R.id.find')

# saveFile called from onOptionsItemSelected and lambda
e('TextEditorActivity.onOptionsItemSelected', 'TextEditorActivity.saveFile', 'CALL',
  'onOptionsItemSelected calls saveFile when save menu item selected',
  evidence='SRC activities/TextEditorActivity.java:364 case R.id.save')

# Lambda callbacks from MaterialDialog in checkUnsavedChanges
e('TextEditorActivity.checkUnsavedChanges', 'TextEditorActivity.lambda$checkUnsavedChanges$0', 'FRAMEWORK',
  'MaterialDialog positive button callback lambda',
  evidence='SRC activities/TextEditorActivity.java:243 .onPositive((dialog, which) -> {...}); ' +
  'INFERRED MaterialDialog dispatches button callbacks (library source not read)')

e('TextEditorActivity.checkUnsavedChanges', 'TextEditorActivity.lambda$checkUnsavedChanges$1', 'FRAMEWORK',
  'MaterialDialog negative button callback lambda',
  evidence='SRC activities/TextEditorActivity.java:248 .onNegative((dialog, which) -> finish()); ' +
  'INFERRED MaterialDialog dispatches button callbacks (library source not read)')

e('TextEditorActivity.lambda$checkUnsavedChanges$0', 'TextEditorActivity.saveFile', 'CALL',
  'Positive dialog button lambda calls saveFile then finish',
  evidence='SRC activities/TextEditorActivity.java:243-244')

# Lambda from load method (ReadFileTask callback)
e('TextEditorActivity.load', 'TextEditorActivity.lambda$load$4', 'FRAMEWORK',
  'ReadFileTask result callback lambda',
  evidence='SRC activities/TextEditorActivity.java:291-292 new ReadFileTask(..., (data) -> {...}); ' +
  'INFERRED AsyncTask-like callback pattern (ReadFileTask implementation dispatches callback)')

# Lambda from lambda$load$4 (Snackbar action callback)
e('TextEditorActivity.lambda$load$4', 'TextEditorActivity.lambda$null$3', 'FRAMEWORK',
  'Snackbar action button callback lambda',
  evidence='SRC activities/TextEditorActivity.java:308 snackbar.setAction(..., v -> snackbar.dismiss()); ' +
  'INFERRED Snackbar dispatches action callbacks (Material Components source not read)', cls='standard')

# Lambda from saveFile (WriteFileAbstraction callback)
e('TextEditorActivity.saveFile', 'TextEditorActivity.lambda$saveFile$2', 'FRAMEWORK',
  'WriteFileAbstraction result callback lambda',
  evidence='SRC activities/TextEditorActivity.java:263-264 new WriteFileAbstraction(..., (errorCode) -> {...}); ' +
  'INFERRED AsyncTask-like callback pattern (WriteFileAbstraction implementation dispatches callback)')

# RecyclerAdapter methods

# addItem called from MainFragment.addSearchResult
e('MainFragment.addSearchResult', 'RecyclerAdapter.addItem', 'CALL',
  'MainFragment calls addItem to add search result to adapter',
  evidence='SRC fragments/MainFragment.java:1629')

# areAllChecked called from MainFragment$3.onActionItemClicked
e('MainFragment$3.onActionItemClicked', 'RecyclerAdapter.areAllChecked', 'CALL',
  'Action mode callback checks if all items with path are checked',
  evidence='SRC fragments/MainFragment.java:691')

# getCorrectView called from RecyclerPreloadSizeProvider
e('RecyclerPreloadSizeProvider.getPreloadSize', 'RecyclerAdapter.getCorrectView', 'CALL',
  'Glide preload size provider calls getCorrectView to determine which view type',
  evidence='SRC adapters/glide/RecyclerPreloadSizeProvider.java:56')

# getItemId is RecyclerView.Adapter callback
e('RecyclerAdapter.onCreateViewHolder', 'RecyclerAdapter.getItemId', 'FRAMEWORK',
  'RecyclerView.Adapter.getItemId called by RecyclerView framework',
  evidence='INFERRED RecyclerView framework calls getItemId for stable IDs (androidx source not read)')

# getItemViewType is RecyclerView.Adapter callback, also called from MainFragment$2
e('RecyclerAdapter.onCreateViewHolder', 'RecyclerAdapter.getItemViewType', 'FRAMEWORK',
  'RecyclerView.Adapter.getItemViewType called by RecyclerView framework',
  evidence='INFERRED RecyclerView framework calls getItemViewType (androidx source not read)')

e('MainFragment$2.getSpanSize', 'RecyclerAdapter.getItemViewType', 'CALL',
  'GridLayoutManager.SpanSizeLookup calls getItemViewType',
  evidence='SRC fragments/MainFragment.java:345')

# onFailedToRecycleView is RecyclerView.Adapter callback
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.onFailedToRecycleView', 'FRAMEWORK',
  'RecyclerView.Adapter.onFailedToRecycleView called when view recycling fails',
  evidence='INFERRED RecyclerView framework calls onFailedToRecycleView (androidx source not read)')

# onViewAttachedToWindow is RecyclerView.Adapter callback
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.onViewAttachedToWindow', 'FRAMEWORK',
  'RecyclerView.Adapter.onViewAttachedToWindow called when view attached',
  evidence='INFERRED RecyclerView framework calls onViewAttachedToWindow (androidx source not read)')

# onViewDetachedFromWindow is RecyclerView.Adapter callback
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.onViewDetachedFromWindow', 'FRAMEWORK',
  'RecyclerView.Adapter.onViewDetachedFromWindow called when view detached',
  evidence='INFERRED RecyclerView framework calls onViewDetachedFromWindow (androidx source not read)')

# toggleChecked(boolean,String) called from MainFragment$3
e('MainFragment$3.onActionItemClicked', 'RecyclerAdapter.toggleChecked(boolean,String)', 'CALL',
  'Action mode callback toggles checked state for items with path',
  evidence='SRC fragments/MainFragment.java:695')

e('MainFragment$3.onDestroyActionMode', 'RecyclerAdapter.toggleChecked(boolean,String)', 'CALL',
  'Action mode destroy callback unchecks all items with path',
  evidence='SRC fragments/MainFragment.java:763')

# RecyclerAdapter lambda callbacks from onBindViewHolder

# lambda$onBindViewHolder$0 is View.OnClickListener from onBindViewHolder
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$0', 'FRAMEWORK',
  'View.OnClickListener callback for row click',
  evidence='SRC adapters/RecyclerAdapter.java:529 holder.rl.setOnClickListener(v -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$1 is View.OnLongClickListener
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$1', 'FRAMEWORK',
  'View.OnLongClickListener callback for row long click',
  evidence='SRC adapters/RecyclerAdapter.java:543 holder.rl.setOnLongClickListener(p1 -> {...}); ' +
  'INFERRED View dispatches long click events (Android SDK source not read)')

# lambda$onBindViewHolder$2 is View.OnClickListener for genericIcon
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$2', 'FRAMEWORK',
  'View.OnClickListener callback for generic icon click',
  evidence='SRC adapters/RecyclerAdapter.java:561 holder.genericIcon.setOnClickListener(v -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$3 is View.OnClickListener for pictureIcon
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$3', 'FRAMEWORK',
  'View.OnClickListener callback for picture icon click',
  evidence='SRC adapters/RecyclerAdapter.java:570 holder.pictureIcon.setOnClickListener(view -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$4 is View.OnClickListener for apkIcon
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$4', 'FRAMEWORK',
  'View.OnClickListener callback for apk icon click',
  evidence='SRC adapters/RecyclerAdapter.java:576 holder.apkIcon.setOnClickListener(view -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$5 is View.OnClickListener for about button (shows popup)
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$5', 'FRAMEWORK',
  'View.OnClickListener callback lambda for about button in grid mode',
  evidence='SRC adapters/RecyclerAdapter.java:698-708 about.setOnClickListener(view -> {...}); ' +
  'INFERRED View dispatches click events (Android SDK source not read)')

# lambda$onBindViewHolder$6 is View.OnLongClickListener for grid mode
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter.lambda$onBindViewHolder$6', 'FRAMEWORK',
  'View.OnLongClickListener callback lambda for item long click in grid mode',
  evidence='SRC adapters/RecyclerAdapter.java:706-714 imageView.setOnLongClickListener(...); ' +
  'INFERRED View dispatches long click events (Android SDK source not read)')

# lambda$showPopup$7 is PopupMenu.OnMenuItemClickListener
e('RecyclerAdapter.showPopup', 'RecyclerAdapter.lambda$showPopup$7', 'FRAMEWORK',
  'PopupMenu.OnMenuItemClickListener callback lambda',
  evidence='SRC adapters/RecyclerAdapter.java:771 popupMenu.setOnMenuItemClickListener((item) -> {...}); ' +
  'INFERRED PopupMenu dispatches menu item click callbacks (Android SDK source not read)')

# Lambdas call toggleChecked
e('RecyclerAdapter.lambda$onBindViewHolder$1', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'CALL',
  'Long click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:546')

e('RecyclerAdapter.lambda$onBindViewHolder$2', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'CALL',
  'Generic icon click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:564')

e('RecyclerAdapter.lambda$onBindViewHolder$3', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'CALL',
  'Picture icon click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:571')

e('RecyclerAdapter.lambda$onBindViewHolder$4', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'CALL',
  'Apk icon click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:577')

e('RecyclerAdapter.lambda$onBindViewHolder$6', 'RecyclerAdapter.toggleChecked(int,ImageView)', 'CALL',
  'Grid mode long click lambda calls toggleChecked',
  evidence='SRC adapters/RecyclerAdapter.java:707')

# UNREACHABLE dictionary for batch 03
# ---- part repair_rp04 (2024-10-28)
# Repair batch 04 - SevenZArchiveEntry and SearchAsyncTask

# SevenZArchiveEntry methods - library class (Apache Commons Compress)
# These getters/setters are not called by the app

UNREACHABLE['SevenZArchiveEntry.getAccessDate'] = (
    'no_trigger_in_app',
    'Library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:275-280',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getCompressedCrc'] = (
    'no_trigger_in_app',
    'Package-private library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:371-373',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getCompressedCrcValue'] = (
    'no_trigger_in_app',
    'Package-private library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:387-389',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getCompressedSize'] = (
    'no_trigger_in_app',
    'Package-private library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:410-412',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getCrc'] = (
    'no_trigger_in_app',
    'Deprecated library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:339-342',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getCreationDate'] = (
    'no_trigger_in_app',
    'Library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:153-159',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.getWindowsAttributes'] = (
    'no_trigger_in_app',
    'Library getter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:313-315',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.isAntiItem'] = (
    'no_trigger_in_app',
    'Library method never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:121-123',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.javaTimeToNtfsTime'] = (
    'no_trigger_in_app',
    'Static library utility never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:486-493',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setAccessDate(Date)'] = (
    'no_trigger_in_app',
    'Library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:296-301',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setCompressedCrc'] = (
    'no_trigger_in_app',
    'Deprecated package-private library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:379-382',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setCompressedCrcValue'] = (
    'no_trigger_in_app',
    'Package-private library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:395-398',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setCompressedSize'] = (
    'no_trigger_in_app',
    'Package-private library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:420-423',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setCrc'] = (
    'no_trigger_in_app',
    'Deprecated library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:350-353',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setCreationDate(Date)'] = (
    'no_trigger_in_app',
    'Library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:174-179',
    'SOURCE'
)

UNREACHABLE['SevenZArchiveEntry.setLastModifiedDate(Date)'] = (
    'no_trigger_in_app',
    'Library setter never called by app; grep shows no call sites',
    'SRC SevenZArchiveEntry.java:232-237',
    'SOURCE'
)

# SearchAsyncTask methods - AsyncTask subclass
# Most methods already in graph_def.py (lines 1294-1325)
# Adding routes for missing lambda methods only

e('SearchAsyncTask.search(HybridFile,SearchFilter)', 'SearchAsyncTask.lambda$search$0', 'CALL',
  'Lambda generated for forEachChildrenFile file consumer',
  evidence='SRC SearchAsyncTask.java:108 directory.forEachChildrenFile(activity.get(), mRootMode, file -> {')

e('SearchAsyncTask.search(HybridFile,String)', 'SearchAsyncTask.lambda$search$1', 'CALL',
  'Lambda for SearchFilter functional interface',
  evidence='SRC SearchAsyncTask.java:131 search(file, fileName -> fileName.toLowerCase().contains(query.toLowerCase()))')

e('SearchAsyncTask.searchRegExFind', 'SearchAsyncTask.lambda$searchRegExFind$2', 'CALL',
  'Lambda for SearchFilter with pattern.matcher().find()',
  evidence='SRC SearchAsyncTask.java:142 search(file, fileName -> pattern.matcher(fileName).find())')

e('SearchAsyncTask.searchRegExMatch', 'SearchAsyncTask.lambda$searchRegExMatch$3', 'CALL',
  'Lambda for SearchFilter with pattern.matcher().matches()',
  evidence='SRC SearchAsyncTask.java:152 search(file, fileName -> pattern.matcher(fileName).matches())')

# ---- part repair_rp06 (2024-10-28)
# Repair batch 06: UtilsHandler, SevenZFile, PrefFrag methods

# UtilsHandler edges
e('UtilsHandler.lambda$saveToDatabase$0', 'UtilsHandler.addSsh', 'CALL',
  'saveToDatabase lambda calls addSsh for SFTP connections',
  evidence='SRC database/UtilsHandler.java:190-191: case SFTP: addSsh(operationData.name, operationData.path, operationData.hostKey, operationData.sshKeyName, operationData.sshKey);')

e('UtilsHandler.removeFromDatabase', 'UtilsHandler.lambda$removeFromDatabase$1', 'CALL',
  'removeFromDatabase lambda for background database removal',
  evidence='SRC database/UtilsHandler.java:201-220: AppConfig.runInBackground(() -> { ... lambda body starting at line 202 ... })')

e('UtilsHandler.saveToDatabase', 'UtilsHandler.lambda$saveToDatabase$0', 'CALL',
  'saveToDatabase lambda for background database save',
  evidence='SRC database/UtilsHandler.java:178-197: AppConfig.runInBackground(() -> { ... lambda body starting at line 179 ... })')

e('S_ENTRY', 'UtilsHandler.onCreate', 'LIFECYCLE',
  'SQLiteOpenHelper onCreate called when database is first created',
  evidence='SRC database/UtilsHandler.java:33: UtilsHandler extends SQLiteOpenHelper; line 106-115: onCreate(SQLiteDatabase db); framework calls this when database is first created')

e('S_ENTRY', 'UtilsHandler.onUpgrade', 'LIFECYCLE',
  'SQLiteOpenHelper onUpgrade called when database version changes',
  evidence='SRC database/UtilsHandler.java:33: UtilsHandler extends SQLiteOpenHelper; line 38: DATABASE_VERSION = 3; line 117-175: onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion); framework calls when version changes')

e('UtilsHandler.lambda$removeFromDatabase$1', 'UtilsHandler.removeBookmarksPath', 'CALL',
  'removeFromDatabase lambda removes bookmark paths',
  evidence='SRC database/UtilsHandler.java:210: case BOOKMARKS: removeBookmarksPath(operationData.name, operationData.path);')

e('UtilsHandler.lambda$removeFromDatabase$1', 'UtilsHandler.removePath', 'CALL',
  'removeFromDatabase lambda removes paths for HIDDEN/HISTORY/LIST/GRID',
  evidence='SRC database/UtilsHandler.java:207: case HIDDEN: case HISTORY: case LIST: case GRID: removePath(operationData.type, operationData.path);')

e('UtilsHandler.lambda$removeFromDatabase$1', 'UtilsHandler.removeSftpPath', 'CALL',
  'removeFromDatabase lambda removes SFTP paths',
  evidence='SRC database/UtilsHandler.java:215: case SFTP: removeSftpPath(operationData.name, operationData.path);')


e('UtilsHandler.renameSMB', 'UtilsHandler.renamePath(Operation,String,String,String,String)', 'CALL',
  'renameSMB calls renamePath with Operation.SMB',
  evidence='SRC database/UtilsHandler.java:519: renamePath(Operation.SMB, oldName, oldPath, newName, newPath);')

e('UtilsHandler.lambda$saveToDatabase$0', 'UtilsHandler.setPath(Operation,String)', 'CALL',
  'saveToDatabase lambda calls 2-param setPath for HIDDEN/HISTORY/LIST/GRID',
  evidence='SRC database/UtilsHandler.java:183: case HIDDEN: case HISTORY: case LIST: case GRID: setPath(operationData.type, operationData.path);')

e('UtilsHandler.lambda$saveToDatabase$0', 'UtilsHandler.setPath(Operation,String,String)', 'CALL',
  'saveToDatabase lambda calls 3-param setPath for BOOKMARKS/SMB',
  evidence='SRC database/UtilsHandler.java:186: case BOOKMARKS: case SMB: setPath(operationData.type, operationData.name, operationData.path);')

e('SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'UtilsHandler.updateSsh', 'CALL',
  'SftpConnectDialog lambda calls UtilsHandler.updateSsh',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:386: utilsHandler.updateSsh(connectionName, oldConnectionName, path, hostKey, sshKeyName, sshKey);')

# SevenZFile edges

# PrefFrag edges
e('PrefFrag.onCreate', 'PrefFrag.lambda$onCreate$0', 'CALL',
  'onCreate sets fingerprint preference listener',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:117-145: checkBoxFingerprint.setOnPreferenceChangeListener((preference, newValue) -> { ... }); lambda starts at line 118')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$1', 'CALL',
  'onPreferenceClick shows grid columns dialog',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:176: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... }); grid columns preference')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$2', 'CALL',
  'onPreferenceClick shows theme dialog',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:185: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... }); theme preference')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$3', 'CALL',
  'onPreferenceClick shows master password input dialog',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:238: masterPasswordDialogBuilder.input(..., (dialog, input) -> { }); for password input')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$4', 'CALL',
  'onPreferenceClick master password positive button',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:243-259: masterPasswordDialogBuilder.onPositive((dialog, which) -> { ... }); positive button handler')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$5', 'CALL',
  'onPreferenceClick master password negative button',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:261: masterPasswordDialogBuilder.onNegative((dialog, which) -> dialog.cancel()); negative button')

e('S_ENTRY', 'PrefFrag.onCreate', 'LIFECYCLE',
  'PreferenceFragment onCreate lifecycle callback',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:64: PrefFrag extends PreferenceFragment; line 76-147: onCreate; activities/PreferencesActivity.java:255: new PrefFrag() instantiated; framework calls onCreate')

e('S_ENTRY', 'PrefFrag.onCreateView', 'LIFECYCLE',
  'PreferenceFragment onCreateView lifecycle callback',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:284-289: onCreateView; framework calls after onCreate')

e('S_ENTRY', 'PrefFrag.onPause', 'LIFECYCLE',
  'PreferenceFragment onPause lifecycle callback',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:292-302: onPause; framework calls when fragment loses foreground')

e('PrefFrag.onCreate', 'PrefFrag.onPreferenceClick', 'CALL',
  'onCreate sets preference click listener',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:92-94: for (String PREFERENCE_KEY : PREFERENCE_KEYS) { findPreference(PREFERENCE_KEY).setOnPreferenceClickListener(this); } // PrefFrag implements OnPreferenceClickListener')

e('S_ENTRY', 'PrefFrag.onResume', 'LIFECYCLE',
  'PreferenceFragment onResume lifecycle callback',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:305-316: onResume; framework calls when fragment comes to foreground')

e('PrefFrag.lambda$onPreferenceClick$2', 'PrefFrag.restartPC', 'CALL',
  'Theme selection lambda restarts activity',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:187: restartPC(getActivity()); called after theme selection')

# Repair batch 06 UNREACHABLE entries
UNREACHABLE['UtilsHandler.renamePath(Operation,String,String)'] = (
    'no_trigger_in_app',
    'Private method with 3 parameters (Operation, name, path). The app only calls the 5-parameter overload renamePath(Operation,String,String,String,String) via renameBookmark (line 514) and renameSMB (line 519). This 3-parameter version is unused dead code.',
    'SRC database/UtilsHandler.java:577-585: private void renamePath(Operation operation, String name, String path); no callers found in app code',
    'SOURCE'
)
UNREACHABLE['SevenZFile.<init>(File,byte[])'] = (
    'no_trigger_in_app',
    'Deprecated constructor taking byte[] password. The app uses SevenZFile.<init>(File,char[]) at SevenZipHelperTask.java:69 and SevenZipExtractor.java:50.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:120-123: @deprecated comment; no app callers found',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel)'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel without password. The app instantiates SevenZFile only via File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:136-138; grep in app shows no FileChannel usage with SevenZFile',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel,String)'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with filename. The app instantiates SevenZFile only via File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:187-190; grep shows no FileChannel usage',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel,String,byte[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with byte[] password. The app uses File-based constructors with char[] password.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:207-210; grep shows no FileChannel usage',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel,String,char[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with char[] password. The app uses File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:170-173; grep shows no FileChannel usage',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel,byte[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with byte[] password. The app uses File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:228-231; grep shows no FileChannel usage',
    'INFERRED'
)
UNREACHABLE['SevenZFile.<init>(FileChannel,char[])'] = (
    'no_trigger_in_app',
    'Constructor for FileChannel with char[] password. The app uses File-based constructors.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:152-155; grep shows no FileChannel usage',
    'INFERRED'
)
UNREACHABLE['SevenZFile.getStatisticsForCurrentEntry'] = (
    'no_trigger_in_app',
    'Public method returning InputStreamStatistics. The app reads 7z files using getNextEntry() and read() but never calls getStatisticsForCurrentEntry.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1115-1131; grep in app shows no calls',
    'INFERRED'
)
UNREACHABLE['SevenZFile.matches'] = (
    'no_trigger_in_app',
    'Static method to check 7z signature bytes. The app opens 7z files directly without pre-checking signatures.',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1158-1164; grep in app shows no calls to matches',
    'INFERRED'
)
UNREACHABLE['SevenZFile.read()'] = (
    'no_trigger_in_app',
    'Single-byte read method. The app uses read(byte[]) for extraction. The no-arg read() is not directly called; read(byte[]) delegates to read(byte[],int,int).',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1050-1055: read() calls read(new byte[1], 0, 1); grep in app shows only read(buf) calls, never read()',
    'INFERRED'
)
UNREACHABLE['SevenZFile.toString'] = (
    'no_trigger_in_app',
    'toString() override. The app opens, reads, and closes 7z files without calling toString().',
    'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1191-1193; grep shows no explicit toString() calls on SevenZFile',
    'INFERRED'
)

# ---- part repair_rp07 (2024-10-28)
# Repair batch 07: StreamServer$HTTPSession, ProcessViewerFragment, SmbConnectDialog

# StreamServer$HTTPSession internal streaming server routes
e('MainFragment.launchSMB', 'Streamer.getInstance', 'CALL',
  'MainFragment.launchSMB calls Streamer.getInstance for SMB streaming',
  evidence='SRC MainFragment.java:1657: final Streamer s = Streamer.getInstance(); SmbStreamer/Streamer.java:57')

e('Streamer.getInstance', 'Streamer.<init>', 'CALL',
  'Singleton getInstance creates Streamer instance',
  evidence='SRC SmbStreamer/Streamer.java:39: instance = new Streamer(PORT);')

e('Streamer.<init>', 'StreamServer.<init>', 'CALL',
  'Streamer constructor calls super StreamServer constructor',
  evidence='SRC Streamer.java:34: super(port, new File("."));')

e('StreamServer.<init>', 'StreamServer$HTTPSession.<init>', 'ASYNC',
  'StreamServer constructor spawns thread that creates HTTPSession on socket accept',
  evidence='SRC SmbStreamer/StreamServer.java:179: new HTTPSession(accept);')

e('StreamServer$HTTPSession.<init>', 'StreamServer$HTTPSession.run', 'ASYNC',
  'HTTPSession constructor starts thread with run() method',
  evidence='SRC SmbStreamer/StreamServer.java:222-224: Thread t = new Thread(this); t.start();')

e('StreamServer$HTTPSession.run', 'StreamServer$HTTPSession.handleResponse', 'CALL',
  'HTTPSession.run calls handleResponse to process HTTP request',
  evidence='SRC SmbStreamer/StreamServer.java:229: handleResponse(socket);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.decodeHeader', 'CALL',
  'handleResponse decodes HTTP headers',
  evidence='SRC SmbStreamer/StreamServer.java:266: decodeHeader(hin, pre, parms, header);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.decodeParms', 'CALL',
  'handleResponse decodes POST form parameters',
  evidence='SRC SmbStreamer/StreamServer.java:323: decodeParms(postLine, parms);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.decodeMultipartData', 'CALL',
  'handleResponse decodes POST multipart/form-data',
  evidence='SRC SmbStreamer/StreamServer.java:320: decodeMultipartData(boundary, fbuf, in, parms, files);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.sendError', 'CALL',
  'handleResponse sends HTTP error if serve() returns null',
  evidence='SRC SmbStreamer/StreamServer.java:330: sendError(socket, HTTP_INTERNALERROR, ...);')

e('StreamServer$HTTPSession.handleResponse', 'StreamServer$HTTPSession.sendResponse', 'CALL',
  'handleResponse sends HTTP response with content',
  evidence='SRC SmbStreamer/StreamServer.java:332: sendResponse(socket, r.status, r.mimeType, r.header, r.data);')


e('StreamServer$HTTPSession.decodeHeader', 'StreamServer$HTTPSession.decodeParms', 'CALL',
  'decodeHeader decodes query parameters from URI',
  evidence='SRC SmbStreamer/StreamServer.java:363: decodeParms(uri.substring(qmi + 1), parms);')

e('StreamServer$HTTPSession.decodeHeader', 'StreamServer$HTTPSession.decodePercent', 'CALL',
  'decodeHeader percent-decodes URI',
  evidence='SRC SmbStreamer/StreamServer.java:364: uri = decodePercent(uri.substring(0, qmi));')

e('StreamServer$HTTPSession.decodeHeader', 'StreamServer$HTTPSession.sendError', 'CALL',
  'decodeHeader sends error on parse failure',
  evidence='SRC SmbStreamer/StreamServer.java:349, 353, 357: sendError(socket, HTTP_BADREQUEST, ...);')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.getBoundaryPositions', 'CALL',
  'decodeMultipartData finds boundary positions in multipart data',
  evidence='SRC SmbStreamer/StreamServer.java:391: int[] bpositions = getBoundaryPositions(fbuf, boundary.getBytes());')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.stripMultipartHeaders', 'CALL',
  'decodeMultipartData strips multipart headers',
  evidence='SRC SmbStreamer/StreamServer.java:435: int offset = stripMultipartHeaders(fbuf, bpositions[boundarycount - 2]);')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.saveTmpFile', 'CALL',
  'decodeMultipartData saves uploaded file to temp',
  evidence='SRC SmbStreamer/StreamServer.java:436: String path = saveTmpFile(fbuf, offset, bpositions[boundarycount - 1] - offset - 4);')

e('StreamServer$HTTPSession.decodeMultipartData', 'StreamServer$HTTPSession.sendError', 'CALL',
  'decodeMultipartData sends error on parse failure',
  evidence='SRC SmbStreamer/StreamServer.java:395, 400, 425, 449: sendError(socket, HTTP_BADREQUEST, ...);')

e('StreamServer$HTTPSession.decodeParms', 'StreamServer$HTTPSession.decodePercent', 'CALL',
  'decodeParms percent-decodes parameter names and values',
  evidence='SRC SmbStreamer/StreamServer.java:526-527: p.put(decodePercent(e.substring(0, sep)).trim(), decodePercent(e.substring(sep + 1)));')

e('StreamServer$HTTPSession.decodePercent', 'StreamServer$HTTPSession.sendError', 'CALL',
  'decodePercent sends error on invalid encoding',
  evidence='SRC SmbStreamer/StreamServer.java:508: sendError(socket, HTTP_BADREQUEST, ...);')

e('StreamServer$HTTPSession.sendError', 'StreamServer$HTTPSession.sendResponse', 'CALL',
  'sendError formats error as HTTP response',
  evidence='SRC SmbStreamer/StreamServer.java:516: sendResponse(socket, status, MIME_PLAINTEXT, null, null);')

# ProcessViewerFragment routes
e('MainActivity.onCreate', 'ProcessViewerFragment.<init>', 'CALL',
  'MainActivity creates ProcessViewerFragment when processing service intent',
  evidence='SRC MainActivity.java:390: transaction.replace(R.id.content_frame, new ProcessViewerFragment(), KEY_INTENT_PROCESS_VIEWER);')

e('MainActivity.onNewIntent', 'ProcessViewerFragment.<init>', 'CALL',
  'MainActivity.onServiceIntent creates ProcessViewerFragment',
  evidence='SRC MainActivity.java:1590: transaction.replace(R.id.content_frame, new ProcessViewerFragment(), KEY_INTENT_PROCESS_VIEWER);')

e('ProcessViewerFragment.<init>', 'ProcessViewerFragment.onCreateView', 'LIFECYCLE',
  'Fragment lifecycle: constructor to onCreateView',
  evidence='INFERRED FW-SRC')

e('ProcessViewerFragment.onCreateView', 'ProcessViewerFragment.onActivityCreated', 'LIFECYCLE',
  'Fragment lifecycle: onCreateView to onActivityCreated',
  evidence='INFERRED FW-SRC')

e('ProcessViewerFragment.onActivityCreated', 'ProcessViewerFragment.onResume', 'LIFECYCLE',
  'Fragment lifecycle: onActivityCreated to onResume',
  evidence='INFERRED FW-SRC')

e('ProcessViewerFragment.onResume', 'ProcessViewerFragment.onPause', 'LIFECYCLE',
  'Fragment lifecycle: onResume to onPause',
  evidence='INFERRED FW-SRC')

e('ProcessViewerFragment.onResume', 'ProcessViewerFragment.processResults', 'CALL',
  'ProcessViewerFragment.onResume sets progress listener that calls processResults',
  evidence='SRC ProcessViewerFragment.java:180-215: serviceInstance.setProgressListener(callback); indirect through service binding')

e('ProcessViewerFragment.processResults', 'ProcessViewerFragment.chartInit', 'CALL',
  'processResults initializes chart on first call',
  evidence='SRC ProcessViewerFragment.java:192: chartInit(total); if !isInitialized')

e('ProcessViewerFragment.processResults', 'ProcessViewerFragment.setupDrawables', 'CALL',
  'processResults sets up UI drawables on first call',
  evidence='SRC ProcessViewerFragment.java:195: setupDrawables(serviceType, move); if !isInitialized')

e('ProcessViewerFragment.processResults', 'ProcessViewerFragment.addEntry', 'CALL',
  'processResults adds data entry to chart',
  evidence='SRC ProcessViewerFragment.java:199-200: addEntry(FileUtils.readableFileSizeFloat(doneBytes), FileUtils.readableFileSizeFloat(dataPackage.speedRaw));')

e('ProcessViewerFragment.processResults', 'FileUtils.readableFileSizeFloat', 'CALL',
  'processResults formats byte sizes for display',
  evidence='SRC ProcessViewerFragment.java:199-200: FileUtils.readableFileSizeFloat(doneBytes) and FileUtils.readableFileSizeFloat(dataPackage.speedRaw)')

e('ProcessViewerFragment.setupDrawables', 'ProcessViewerFragment.cancelBroadcast', 'CALL',
  'setupDrawables creates cancel button that broadcasts cancellation',
  evidence='SRC ProcessViewerFragment.java:248, 260, 272, 284, 296: cancelBroadcast(new Intent(...));')

e('ProcessViewerFragment.cancelBroadcast', 'ProcessViewerFragment.lambda$cancelBroadcast$0', 'FRAMEWORK',
  'cancelBroadcast sets cancel button click listener',
  evidence='SRC ProcessViewerFragment.java:306: mCancelButton.setOnClickListener(v -> {...});')

e('ProcessViewerFragment.addEntry', 'ProcessViewerFragment.createDataSet', 'CALL',
  'addEntry creates chart dataset if needed',
  evidence='SRC ProcessViewerFragment.java:331: dataSet = createDataSet(); if dataSet is null')

# SmbConnectDialog routes
e('MainActivity.showSMBDialog', 'SmbConnectDialog.<init>', 'CALL',
  'MainActivity.showSmbDialog creates SmbConnectDialog',
  evidence='SRC MainActivity.java:1628: SmbConnectDialog smbConnectDialog = new SmbConnectDialog();')

e('SmbConnectDialog.<init>', 'SmbConnectDialog.onCreate', 'LIFECYCLE',
  'DialogFragment lifecycle: constructor to onCreate',
  evidence='INFERRED FW-SRC')

e('SmbConnectDialog.onCreate', 'SmbConnectDialog.onCreateDialog', 'LIFECYCLE',
  'DialogFragment lifecycle: onCreate to onCreateDialog',
  evidence='INFERRED FW-SRC')

e('SmbConnectDialog.onCreate', 'EditTextColorStateUtil.setTint', 'CALL',
  'SmbConnectDialog.onCreate tints EditText fields (actually in onCreateDialog)',
  evidence='SRC SmbConnectDialog.java:164-166: EditTextColorStateUtil.setTint(context, conName, accentColor);')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$0', 'FRAMEWORK',
  'onCreateDialog sets help button click listener',
  evidence='SRC SmbConnectDialog.java:168: help.setOnClickListener(v -> {...});')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$1', 'FRAMEWORK',
  'onCreateDialog sets anonymous checkbox click listener',
  evidence='SRC SmbConnectDialog.java:173: ch.setOnClickListener(view -> {...});')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$2', 'FRAMEWORK',
  'onCreateDialog sets positive button click listener',
  evidence='SRC SmbConnectDialog.java:235: ba3.onPositive((dialog, which) -> {...});')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$3', 'FRAMEWORK',
  'onCreateDialog sets negative button click listener',
  evidence='SRC SmbConnectDialog.java:279: ba3.onNegative((dialog, which) -> {...});')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog.lambda$onCreateDialog$4', 'FRAMEWORK',
  'onCreateDialog sets neutral button click listener',
  evidence='SRC SmbConnectDialog.java:286: ba3.onNeutral((dialog, which) -> {...});')

e('SmbConnectDialog.lambda$onCreateDialog$0', 'GeneralDialogCreation.showSMBHelpDialog', 'CALL',
  'Help button lambda shows SMB help dialog',
  evidence='SRC SmbConnectDialog.java:170: GeneralDialogCreation.showSMBHelpDialog(context, accentColor1);')

e('SmbConnectDialog.lambda$onCreateDialog$2', 'SmbConnectDialog.createSMBPath', 'CALL',
  'Positive button lambda creates SMB connection path',
  evidence='SRC SmbConnectDialog.java:267, 272: createSMBPath(new String[]{ipa, "", "",domaind}, true) or createSMBPath(new String[]{ipa, useru, passp,domaind}, false);')


# ---- part repair_rp08 (2024-10-28)
# Repair batch 08: MainActivity, PrepareCopyTask, ScrimInsetsRelativeLayout, SubnetScanner methods

# MainActivity connection management edges

e('MainActivity.addConnection(boolean,String,String,String,String,String)', 'MainActivity.getCurrentMainFragment', 'CALL',
  'addConnection refreshes current fragment after adding connection',
  evidence='SRC activities/MainActivity.java:1687-1688: MainActivity.getCurrentMainFragment')

e('MainActivity.addConnection(boolean,String,String,String,String,String)', 'MainActivity.lambda$addConnection$9', 'ASYNC',
  'addConnection spawns background task to update database',
  evidence='SRC activities/MainActivity.java:1697: AppConfig.runInBackground(() -> {...})')


e('MainActivity.deleteConnection(String,String)', 'MainActivity.lambda$deleteConnection$10', 'ASYNC',
  'deleteConnection spawns background task to remove from database',
  evidence='SRC activities/MainActivity.java:1717: AppConfig.runInBackground(() -> {...})')

e('MainActivity.lambda$addConnection$9', 'UtilsHandler.renameSMB', 'CALL',
  'addConnection lambda renames SMB entry when editing',
  evidence='SRC activities/MainActivity.java:1698: utilsHandler.renameSMB(oldname, oldPath, name, path);')

e('MainActivity.lambda$deleteConnection$10', 'OperationData.<init>(Operation,String,String)', 'CALL',
  'deleteConnection lambda creates OperationData for removal',
  evidence='SRC activities/MainActivity.java:1718: new OperationData(UtilsHandler.Operation.SMB, name, path)')

e('MainActivity.lambda$deleteConnection$10', 'UtilsHandler.removeFromDatabase', 'CALL',
  'deleteConnection lambda removes SMB connection from database',
  evidence='SRC activities/MainActivity.java:1717-1719: utilsHandler.removeFromDatabase(new OperationData(...))')





e('MainFragment.onListItemClicked', 'MainActivity.setPagingEnabled', 'CALL',
  'MainFragment disables ViewPager paging during selection mode',
  evidence='SRC fragments/MainFragment.java:488: getMainActivity().setPagingEnabled(false);')

e('MainActivity.setPagingEnabled', 'MainActivity.getTabFragment', 'CALL',
  'setPagingEnabled accesses TabFragment to control ViewPager',
  evidence='SRC activities/MainActivity.java:1272: getTabFragment().mViewPager.setPagingEnabled(b);')

# PrepareCopyTask conflict resolution edges
e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask.doNotReplaceFiles', 'CALL',
  'onEndDialog skips conflicting files when user chooses not to replace',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:228,237')

e('PrepareCopyTask.lambda$showDialog$1', 'PrepareCopyTask.doNotReplaceFiles', 'CALL',
  'Skip button lambda removes conflicting files from copy list',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:200-204')

e('HybridFile.forEachChildrenFile', 'PrepareCopyTask.lambda$checkConflicts$0', 'CALL',
  'forEachChildrenFile invokes lambda to check for name conflicts',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:142-148')



e('PrepareCopyTask.lambda$showDialog$2', 'PrepareCopyTask.replaceFiles', 'CALL',
  'Overwrite button lambda replaces conflicting files',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:208')

e('PrepareCopyTask.onPostExecute', 'PrepareCopyTask.onEndDialog', 'CALL',
  'onPostExecute starts conflict resolution workflow',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:172')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask.showDialog', 'CALL',
  'onEndDialog shows conflict resolution dialog',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:218')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask.finishCopying', 'CALL',
  'onEndDialog calls finishCopying when all conflicts resolved',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:241')

e('ZipService$CompressAsyncTask.execute', 'PrepareCopyTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute after background work',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:153')

e('PrepareCopyTask.onPostExecute', 'PrepareCopyTask.startService', 'CALL',
  'onPostExecute starts service for cloud/OTG/root copy operations',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:164')

e('ZipService$CompressAsyncTask.execute', 'PrepareCopyTask.onPreExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPreExecute before starting task',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:86')


e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask.replaceFiles', 'CALL',
  'onEndDialog replaces files when user chooses to overwrite',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:240')



# SubnetScanner SMB network discovery edges

e('SubnetScanner.<clinit>', 'SubnetScanner.configure', 'CALL',
  'Class initializer calls configure to set jCIFS properties',
  evidence='SRC utils/SubnetScanner.java:66')

e('SmbSearchDialog.onCreateDialog', 'SubnetScanner.<init>', 'CALL',
  'SmbSearchDialog creates SubnetScanner to find SMB servers',
  evidence='SRC utils/SubnetScanner.java:77: new SubnetScanner(context)')



e('SmbSearchDialog.lambda$onCreateDialog$0', 'SubnetScanner.interrupt', 'CALL',
  'SmbSearchDialog interrupts scanner when user cancels',
  evidence='SRC utils/SubnetScanner.java:196: super.interrupt(); this.pool.shutdownNow();')

e('SubnetScanner.run', 'SubnetScanner.onFound', 'CALL',
  'run calls onFound when computer discovered via IP scan',
  evidence='SRC utils/SubnetScanner.java:116')

e('SubnetScanner.tryWithBroadcast', 'SubnetScanner.onFound', 'CALL',
  'tryWithBroadcast calls onFound when computer discovered via SMB broadcast',
  evidence='SRC utils/SubnetScanner.java:172')


e('SubnetScanner.run', 'SubnetScanner.tryWithBroadcast', 'CALL',
  'run attempts SMB broadcast discovery before IP scan',
  evidence='SRC utils/SubnetScanner.java:87')

e('SmbSearchDialog.onCreateDialog', 'SubnetScanner.setObserver', 'CALL',
  'SmbSearchDialog sets observer to receive scan progress updates',
  evidence='SRC utils/SubnetScanner.java:191: synchronized (this.mLock) { this.observer = scanObserver; }')


# Repair batch 08 UNREACHABLE entries
UNREACHABLE['ScrimInsetsRelativeLayout.<init>(Context)'] = (
    'no_trigger_in_app',
    'View class never instantiated; no programmatic instantiation or XML usage found',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:41; GREP: no "new ScrimInsetsRelativeLayout" in app code, no XML layout references',
    'SOURCE'
)
UNREACHABLE['ScrimInsetsRelativeLayout.<init>(Context,AttributeSet)'] = (
    'no_trigger_in_app',
    'View class never instantiated; no XML layouts reference ScrimInsetsRelativeLayout',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:45; GREP: grep -r "ScrimInsetsRelativeLayout" res/layout/ shows 0 results',
    'SOURCE'
)
UNREACHABLE['ScrimInsetsRelativeLayout.<init>(Context,AttributeSet,int)'] = (
    'no_trigger_in_app',
    'View class never instantiated; no XML layouts reference ScrimInsetsRelativeLayout',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:50; GREP: grep -r "ScrimInsetsRelativeLayout" res/layout/ shows 0 results',
    'SOURCE'
)
UNREACHABLE['ScrimInsetsRelativeLayout.init'] = (
    'no_trigger_in_app',
    'View constructors are unreachable, so init is never called',
    'SRC ui/views/ScrimInsetsRelativeLayout.java:55; INFERRED from unreachable constructors',
    'INFERRED'
)

# ---- part repair_rp09 (2025-01-29)
# Repair batch 09 - AmazeFileManager graph_def.py part file
# Schema-2 edges for 40 methods from rp_09.txt
# Generated 2025-01-XX HH:MM

# PreferencesActivity helper methods (lines 175-200 of PreferencesActivity.java)
# All REACHABLE - called by ColorPref and PrefFrag

# PreferencesActivity.getRestartActivity
# SRC activities/PreferencesActivity.java:196-198
# Called by ColorPref.onBackPressed at fragments/preference_fragments/ColorPref.java:208
e('ColorPref.onBackPressed', 'PreferencesActivity.getRestartActivity', 'CALL',
  'ColorPref.onBackPressed checks if activity restart is needed via getRestartActivity()',
  evidence='SRC fragments/preference_fragments/ColorPref.java:208: if(((PreferencesActivity) getActivity()).getRestartActivity()); SRC activities/PreferencesActivity.java:196-198: public boolean getRestartActivity() { return restartActivity; }')

# PreferencesActivity.onBackPressed
# SRC activities/PreferencesActivity.java:105-120
# Framework lifecycle callback triggered by user pressing back button
e('PreferencesActivity.onCreate', 'PreferencesActivity.onBackPressed', 'FRAMEWORK',
  'Framework calls onBackPressed when user presses back button',
  evidence='FW-SRC core/java/android/app/Activity.java (Activity.onBackPressed dispatched by framework); SRC activities/PreferencesActivity.java:105-120')

e('PreferencesActivity.onBackPressed', 'ColorPref.onBackPressed', 'CALL',
  'PreferencesActivity.onBackPressed delegates to ColorPref if current fragment is ColorPref',
  guard='currentFragment instanceof ColorPref',
  evidence='SRC activities/PreferencesActivity.java:106-107: if(currentFragment instanceof ColorPref) { if(((ColorPref) currentFragment).onBackPressed()) return; }')

e('PreferencesActivity.onBackPressed', 'PreferencesActivity.restartActivity', 'CALL',
  'PreferencesActivity.onBackPressed restarts activity when selectedItem != START_PREFERENCE and restartActivity flag is true',
  guard='selectedItem != START_PREFERENCE && restartActivity',
  evidence='SRC activities/PreferencesActivity.java:109-110: if (selectedItem != START_PREFERENCE && restartActivity) { restartActivity(this); }')

e('PreferencesActivity.onBackPressed', 'PreferencesActivity.selectItem', 'CALL',
  'PreferencesActivity.onBackPressed returns to start preference when selectedItem != START_PREFERENCE and no restart needed',
  guard='selectedItem != START_PREFERENCE && !restartActivity',
  evidence='SRC activities/PreferencesActivity.java:111: } else if (selectedItem != START_PREFERENCE) { selectItem(START_PREFERENCE); }')

e('PreferencesActivity.onBackPressed', 'MainActivity.<init>', 'INTENT',
  'PreferencesActivity.onBackPressed navigates back to MainActivity when at start preference',
  guard='selectedItem == START_PREFERENCE',
  evidence='SRC activities/PreferencesActivity.java:113-117: Intent in = new Intent(PreferencesActivity.this, MainActivity.class); in.setAction(Intent.ACTION_MAIN); this.startActivity(in); this.finish();', cls='standard')

# PreferencesActivity.onOptionsItemSelected
# SRC activities/PreferencesActivity.java:122-153
# Framework callback when options menu item is selected
e('PreferencesActivity.onCreate', 'PreferencesActivity.onOptionsItemSelected', 'CALL',
  'User taps the Up/Home button in PreferencesActivity toolbar',
  gui=['Tap Up button in preferences'],
  evidence='FW-SRC core/java/android/app/Activity.java (Activity.onOptionsItemSelected dispatched by framework for menu items); SRC activities/PreferencesActivity.java:122-153')


e('PreferencesActivity.onOptionsItemSelected', 'PreferencesActivity.restartActivity', 'CALL',
  'PreferencesActivity.onOptionsItemSelected restarts activity when selectedItem != START_PREFERENCE and restartActivity flag is true',
  guard='selectedItem != START_PREFERENCE && restartActivity',
  evidence='SRC activities/PreferencesActivity.java:126-127: if (selectedItem != START_PREFERENCE && restartActivity) { restartActivity(this); }')

e('PreferencesActivity.onOptionsItemSelected', 'PreferencesActivity.selectItem', 'CALL',
  'PreferencesActivity.onOptionsItemSelected returns to start preference when selectedItem != START_PREFERENCE',
  guard='selectedItem != START_PREFERENCE && !restartActivity',
  evidence='SRC activities/PreferencesActivity.java:128: } else if (selectedItem != START_PREFERENCE) { selectItem(START_PREFERENCE); }')

e('PreferencesActivity.onOptionsItemSelected', 'MainActivity.<init>', 'INTENT',
  'PreferencesActivity.onOptionsItemSelected navigates back to MainActivity when at start preference',
  guard='selectedItem == START_PREFERENCE',
  evidence='SRC activities/PreferencesActivity.java:130-143: Intent in = new Intent(PreferencesActivity.this, MainActivity.class); activity.finish(); activity.startActivity(in);')

# PreferencesActivity.onSaveInstanceState
# SRC activities/PreferencesActivity.java:103-104
# Framework lifecycle callback
e('PreferencesActivity.onCreate', 'PreferencesActivity.onSaveInstanceState', 'FRAMEWORK',
  'Framework calls onSaveInstanceState to save activity state',
  evidence='FW-SRC core/java/android/app/Activity.java (Activity.onSaveInstanceState dispatched by ActivityThread); SRC activities/PreferencesActivity.java:103-104')

# PreferencesActivity.restartActivity
# SRC activities/PreferencesActivity.java:217-232
# Called from onBackPressed and onOptionsItemSelected (already added above)

# PreferencesActivity.restoreListViewState
# SRC activities/PreferencesActivity.java:189-191
# Called by PrefFrag to restore ListView scroll state
e('PrefFrag.onCreateView', 'PreferencesActivity.restoreListViewState', 'CALL',
  'PrefFrag.onCreateView restores ListView scroll position via PreferencesActivity.restoreListViewState',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:287: Parcelable restored = ((PreferencesActivity) getActivity()).restoreListViewState(START_PREFERENCE); SRC activities/PreferencesActivity.java:189-191')

# PreferencesActivity.saveListViewState
# SRC activities/PreferencesActivity.java:180-182
# Called by PrefFrag to save ListView scroll state
e('PrefFrag.onPreferenceClick', 'PreferencesActivity.saveListViewState', 'CALL',
  'PrefFrag.onPreferenceClick saves ListView scroll position before navigating away',
  evidence='SRC fragments/preference_fragments/PrefFrag.java:159: ((PreferencesActivity) getActivity()).saveListViewState(START_PREFERENCE, listView.onSaveInstanceState()); SRC activities/PreferencesActivity.java:180-182')

# PreferencesActivity.setRestartActivity
# SRC activities/PreferencesActivity.java:193-194
# Called by ColorPref to signal that activity restart is needed
e('ColorPref$1.onNeutral', 'PreferencesActivity.setRestartActivity', 'CALL',
  'ColorPref neutral button sets restart activity flag',
  evidence='SRC fragments/preference_fragments/ColorPref.java:183: if (activity != null) activity.setRestartActivity(); SRC activities/PreferencesActivity.java:193-194')

e('ColorPref.lambda$loadSection1$1', 'PreferencesActivity.setRestartActivity', 'CALL',
  'ColorPref selected colours listener sets restart activity flag',
  evidence='SRC fragments/preference_fragments/ColorPref.java:225: if (activity != null) activity.setRestartActivity(); SRC activities/PreferencesActivity.java:193-194')

# PemToKeyPairTask - AsyncTask for parsing SSH private keys
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:67-262

# PemToKeyPairTask.<init>(InputStream,Callback)
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:88-90
# Called from SftpConnectDialog.onActivityResult (already in graph_def.py at line 12844)

# PemToKeyPairTask.doInBackground
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:100-122
# AsyncTask lifecycle - automatically called by execute()

e('PemToKeyPairTask.doInBackground', 'PemToKeyPairTask.onProgressUpdate', 'ASYNC',
  'doInBackground calls publishProgress which triggers onProgressUpdate on main thread',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:120: publishProgress(new IOException("No converter available to parse selected PEM")); INFERRED AsyncTask.publishProgress triggers onProgressUpdate')

# PemToKeyPairTask.lambda$onProgressUpdate$0
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:145-154
# MaterialDialog onPositive callback
e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$0', 'FRAMEWORK',
  'User taps OK button in passphrase dialog',
  gui=['Tap OK in SSH key passphrase dialog'],
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:143-154: .onPositive(((dialog, which) -> { ... })); lambda at 145-154')

# PemToKeyPairTask.lambda$onProgressUpdate$1
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:156-160
# MaterialDialog onNegative callback
e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$1', 'FRAMEWORK',
  'User taps Cancel button in passphrase dialog',
  gui=['Tap Cancel in SSH key passphrase dialog'],
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:155-160: .onNegative(((dialog, which) -> { ... })); lambda at 156-160')

e('PemToKeyPairTask.lambda$onProgressUpdate$1', 'PemToKeyPairTask.toastOnParseError', 'CALL',
  'Cancel callback shows toast error before canceling task',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:158: toastOnParseError(result);')

# PemToKeyPairTask.lambda$onProgressUpdate$2
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:163-167
# WarnableTextInputValidator callback
e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$2', 'CALL',
  'onProgressUpdate sets up text validator with lambda for passphrase input',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:162-167: new WarnableTextInputValidator(..., (text) -> { ... }); lambda at 163-167')

# PemToKeyPairTask.onPostExecute
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:175-179
# AsyncTask lifecycle callback
e('PemToKeyPairTask.doInBackground', 'PemToKeyPairTask.onPostExecute', 'ASYNC',
  'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  evidence='INFERRED android.os.AsyncTask lifecycle calls onPostExecute on main thread after doInBackground returns; SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:175-179')

e('PemToKeyPairTask.onPostExecute', 'SftpConnectDialog.lambda$onActivityResult$14', 'FRAMEWORK',
  'onPostExecute invokes the callback registered in constructor',
  evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:176-178: if(callback != null) { callback.onResult(result); }; callback registered at SftpConnectDialog.java:311')

# PemToKeyPairTask.onProgressUpdate
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:124-173
# AsyncTask lifecycle callback (already added edge from doInBackground above)

# PemToKeyPairTask.toastOnParseError
# SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:181-185
# Called from lambda$onProgressUpdate$1 (already added above)

# FileUtil$MediaFile - Kitkat MediaStore workaround class (UNREACHABLE)
# SRC filesystem/FileUtil.java:983-1231
# All methods in this inner class are unreachable - no callers found in app

UNREACHABLE['FileUtil$MediaFile.<init>'] = (
  'no_trigger_in_app',
  'MediaFile constructor only called from mkdir() at FileUtil.java:1198, but mkdir() itself is never called; grep shows no MediaFile instantiation outside FileUtil class',
  'SRC filesystem/FileUtil.java:1016-1022 (constructor); grep in app source shows only this definition, no callers except within unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.delete'] = (
  'no_trigger_in_app',
  'MediaFile.delete only called from mkdir() at FileUtil.java:1199, but mkdir() is never called',
  'SRC filesystem/FileUtil.java:1028-1059 (delete method); called only at line 1199 within unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.getExternalFilesDir'] = (
  'no_trigger_in_app',
  'private static method, only called from installTemporaryTrack at line 1134, which is called from getTemporaryAlbumId, which is called from unreachable mkdir()',
  'SRC filesystem/FileUtil.java:987-1010 (getExternalFilesDir); called at line 1134 in installTemporaryTrack; chain starts from unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.getFile'] = (
  'no_trigger_in_app',
  'public method but never called; MediaFile is only instantiated at line 1198 within unreachable mkdir()',
  'SRC filesystem/FileUtil.java:1205-1207 (getFile); grep shows no callers in app source',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.getTemporaryAlbumId'] = (
  'no_trigger_in_app',
  'private method, only called from mkdir() at line 1190, but mkdir() is never called',
  'SRC filesystem/FileUtil.java:1062-1126 (getTemporaryAlbumId); called only at line 1190 within unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.installTemporaryTrack'] = (
  'no_trigger_in_app',
  'private method, only called from getTemporaryAlbumId at line 1091, which is called from unreachable mkdir()',
  'SRC filesystem/FileUtil.java:1129-1170 (installTemporaryTrack); called at line 1091 in getTemporaryAlbumId; chain starts from unreachable mkdir()',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.mkdir'] = (
  'no_trigger_in_app',
  'public method but grep shows no callers in app; Kitkat MediaStore workaround that is unused in this build',
  'SRC filesystem/FileUtil.java:1172-1202 (mkdir); grep in app source shows no callers; Kitkat-specific workaround code',
  'SOURCE'
)

UNREACHABLE['FileUtil$MediaFile.write'] = (
  'no_trigger_in_app',
  'public method but grep shows no callers in app; MediaFile is never instantiated outside unreachable mkdir()',
  'SRC filesystem/FileUtil.java:1207-1231 (write); grep shows no callers in app source',
  'SOURCE'
)

# MainActivityHelper$2 - anonymous ErrorCallBack in rename() method
# SRC utils/MainActivityHelper.java:265-328
# Anonymous class implementing Operations.ErrorCallBack interface

# MainActivityHelper$2.exists
# SRC utils/MainActivityHelper.java:267-273
# Callback from Operations.rename when target file already exists
e('Operations.rename', 'MainActivityHelper$2.exists', 'FRAMEWORK',
  'Operations.rename invokes exists callback when target file already exists',
  evidence='SRC filesystem/Operations.java (Operations.rename checks file existence and calls callback.exists if target exists); SRC utils/MainActivityHelper.java:265 new Operations.ErrorCallBack() { @Override public void exists...; callback method at 267-273')

# MainActivityHelper$2.invalidName
# SRC utils/MainActivityHelper.java:318-325
# Callback from Operations.rename when filename is invalid
e('Operations.rename', 'MainActivityHelper$2.invalidName', 'FRAMEWORK',
  'Operations.rename invokes invalidName callback when new filename is invalid',
  evidence='SRC filesystem/Operations.java (Operations.rename validates filename and calls callback.invalidName if invalid); SRC utils/MainActivityHelper.java:318-325')

# MainActivityHelper$2.lambda$done$2
# SRC utils/MainActivityHelper.java:299-316
# Runnable lambda in done() callback
e('MainActivityHelper$2.done', 'MainActivityHelper$2.lambda$done$2', 'CALL',
  'done callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:297-316: context.runOnUiThread(() -> { ... }); lambda starts at 299')

# MainActivityHelper$2.lambda$exists$0
# SRC utils/MainActivityHelper.java:268-272
# Runnable lambda in exists() callback
e('MainActivityHelper$2.exists', 'MainActivityHelper$2.lambda$exists$0', 'CALL',
  'exists callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:267-273: context.runOnUiThread(() -> { ... }); lambda at 268-272')

# MainActivityHelper$2.lambda$invalidName$3
# SRC utils/MainActivityHelper.java:319-324
# Runnable lambda in invalidName() callback
e('MainActivityHelper$2.invalidName', 'MainActivityHelper$2.lambda$invalidName$3', 'CALL',
  'invalidName callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:318-325: context.runOnUiThread(() -> { ... }); lambda at 319-324')

# MainActivityHelper$2.lambda$launchSAF$1
# SRC utils/MainActivityHelper.java:280-288
# Runnable lambda in launchSAF(HybridFile,HybridFile) callback
e('MainActivityHelper$2.launchSAF(HybridFile,HybridFile)', 'MainActivityHelper$2.lambda$launchSAF$1', 'CALL',
  'launchSAF callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:278-289: context.runOnUiThread(() -> { ... }); lambda at 280-288')

e('MainActivityHelper$2.lambda$launchSAF$1', 'MainActivityHelper.guideDialogForLEXA', 'CALL',
  'launchSAF lambda shows SAF guide dialog',
  evidence='SRC utils/MainActivityHelper.java:285: guideDialogForLEXA(mainActivity.oppathe1);')

# MainActivityHelper$2.launchSAF(HybridFile)
# SRC utils/MainActivityHelper.java:276 (empty method)

# MainActivityHelper$2.launchSAF(HybridFile,HybridFile)
# SRC utils/MainActivityHelper.java:278-289
# Callback from Operations.rename when SAF is needed
e('Operations.rename', 'MainActivityHelper$2.launchSAF(HybridFile,HybridFile)', 'FRAMEWORK',
  'Operations.rename invokes launchSAF callback when Storage Access Framework is needed for rename',
  evidence='SRC filesystem/Operations.java (Operations.rename detects need for SAF and calls callback.launchSAF); SRC utils/MainActivityHelper.java:278-289')

# MainActivityHelper$3 - anonymous ErrorCallBack in mkfile() method
# SRC utils/MainActivityHelper.java:394-447
# Anonymous class implementing Operations.ErrorCallBack interface

# MainActivityHelper$3.exists
# SRC utils/MainActivityHelper.java:396-408
# Callback from Operations.mkfile when file already exists
e('Operations.mkfile', 'MainActivityHelper$3.exists', 'FRAMEWORK',
  'Operations.mkfile invokes exists callback when target file already exists',
  evidence='SRC filesystem/Operations.java (Operations.mkfile checks file existence and calls callback.exists if exists); SRC utils/MainActivityHelper.java:394 new Operations.ErrorCallBack() { @Override public void exists...; callback at 396-408')

e('MainActivityHelper$3.exists', 'MainActivityHelper$3.lambda$exists$0', 'CALL',
  'exists callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:396-408: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 397-406')

# MainActivityHelper$3.invalidName
# SRC utils/MainActivityHelper.java:437-445
# Callback from Operations.mkfile when filename is invalid
e('Operations.mkfile', 'MainActivityHelper$3.invalidName', 'FRAMEWORK',
  'Operations.mkfile invokes invalidName callback when filename is invalid',
  evidence='SRC filesystem/Operations.java (Operations.mkfile validates filename and calls callback.invalidName if invalid); SRC utils/MainActivityHelper.java:437-445')

e('MainActivityHelper$3.invalidName', 'MainActivityHelper$3.lambda$invalidName$3', 'CALL',
  'invalidName callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:437-445: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 438-443')

# MainActivityHelper$3.lambda$done$2
# SRC utils/MainActivityHelper.java:427-434
# Runnable lambda in done() callback
e('MainActivityHelper$3.done', 'MainActivityHelper$3.lambda$done$2', 'CALL',
  'done callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:425-435: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 427-434')

# MainActivityHelper$3.lambda$exists$0
# SRC utils/MainActivityHelper.java:397-406
# Runnable lambda in exists() callback (already added above)

# MainActivityHelper$3.lambda$invalidName$3
# SRC utils/MainActivityHelper.java:438-443
# Runnable lambda in invalidName() callback (already added above)

# MainActivityHelper$3.lambda$launchSAF$1
# SRC utils/MainActivityHelper.java:412-419
# Runnable lambda in launchSAF(HybridFile) callback
e('MainActivityHelper$3.launchSAF(HybridFile)', 'MainActivityHelper$3.lambda$launchSAF$1', 'CALL',
  'launchSAF callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC utils/MainActivityHelper.java:410-420: ma.getActivity().runOnUiThread(() -> { ... }); lambda at 412-419')

e('MainActivityHelper$3.lambda$launchSAF$1', 'MainActivityHelper.guideDialogForLEXA', 'CALL',
  'launchSAF lambda shows SAF guide dialog',
  evidence='SRC utils/MainActivityHelper.java:416: guideDialogForLEXA(mainActivity.oppathe);')

# MainActivityHelper$3.launchSAF(HybridFile)
# SRC utils/MainActivityHelper.java:410-420
# Callback from Operations.mkfile when SAF is needed
e('Operations.mkfile', 'MainActivityHelper$3.launchSAF(HybridFile)', 'FRAMEWORK',
  'Operations.mkfile invokes launchSAF callback when Storage Access Framework is needed',
  evidence='SRC filesystem/Operations.java (Operations.mkfile detects need for SAF and calls callback.launchSAF); SRC utils/MainActivityHelper.java:410-420')

# MainActivityHelper$3.launchSAF(HybridFile,HybridFile)
# SRC utils/MainActivityHelper.java:422-423 (empty method)


# ---- part repair_rp11 (2025-01-29)
# repair batch 11 - TabFragment, SmbSearchDialog$ListViewAdapter, RoundedImageView, SelectedColorsPreference, ZipService$CompressAsyncTask, SevenZOutputFile$OutputStreamWrapper

# TabFragment.onDestroyView - Fragment lifecycle method called by framework
e('TabFragment.onCreateView', 'TabFragment.onDestroyView', 'LIFECYCLE',
  'Fragment lifecycle: onDestroyView called by framework when view is destroyed',
  evidence='FW-SRC android-8.1.0_r1/core/java/android/app/Fragment.java:2744-2758 performDestroyView() calls onDestroyView(); FragmentManager.java:1356 calls f.performDestroyView() during fragment teardown')

# TabFragment.onPageScrollStateChanged - ViewPager.OnPageChangeListener interface method
e('TabFragment.onCreateView', 'TabFragment.onPageScrollStateChanged', 'FRAMEWORK',
  'ViewPager calls OnPageChangeListener.onPageScrollStateChanged on registered listeners',
  evidence='SRC TabFragment.java:45 implements ViewPager.OnPageChangeListener; SRC TabFragment.java:99 mViewPager.addOnPageChangeListener(this) registers TabFragment as listener; ViewPager framework calls this method')

# TabFragment.onPageScrolled - ViewPager.OnPageChangeListener interface method
e('TabFragment.onCreateView', 'TabFragment.onPageScrolled', 'FRAMEWORK',
  'ViewPager calls OnPageChangeListener.onPageScrolled on registered listeners during scroll',
  evidence='SRC TabFragment.java:45 implements ViewPager.OnPageChangeListener; SRC TabFragment.java:99 mViewPager.addOnPageChangeListener(this) registers TabFragment as listener; ViewPager framework calls this method')

# TabFragment.onPageSelected - ViewPager.OnPageChangeListener interface method (already has edges, add more)
e('TabFragment.onPageSelected', 'BottomBar.updatePath', 'CALL',
  'When page selected, updates bottom bar path',
  evidence='SRC TabFragment.java:287 mainActivity.getAppbar().getBottomBar().updatePath(ma.getCurrentPath(), ...)')

# TabFragment.onSaveInstanceState - Fragment lifecycle method  
e('TabFragment.onCreateView', 'TabFragment.onSaveInstanceState', 'LIFECYCLE',
  'Fragment lifecycle: framework calls onSaveInstanceState to save instance state',
  evidence='SRC TabFragment.java:260 overrides onSaveInstanceState; framework calls this on Fragment instances during configuration changes or process death')

# TabFragment.parsePathForName - UNREACHABLE, no callers in app
UNREACHABLE['TabFragment.parsePathForName'] = ('no_trigger_in_app', 'parsePathForName is never called in the app; grep finds no callers', 'SRC TabFragment.java:243-255 defines parsePathForName but no app code calls it; grep -rn "\\.parsePathForName" in app/src/main/java finds no calls', 'SOURCE')

# TabFragment.parseSmbPath - UNREACHABLE, only called from unreachable parsePathForName
UNREACHABLE['TabFragment.parseSmbPath'] = ('no_trigger_in_app', 'parseSmbPath is only called by parsePathForName which itself is never called', 'SRC TabFragment.java:237-241 defines parseSmbPath; TabFragment.java:248 shows only call is from parsePathForName; parsePathForName has no callers (see above)', 'SOURCE')

# SmbSearchDialog$ListViewAdapter.<init> - RecyclerView.Adapter constructor
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.<init>', 'CALL',
  'SmbSearchDialog creates ListViewAdapter instance',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:78 listViewAdapter = new ListViewAdapter(getActivity(), computers)')

# SmbSearchDialog$ListViewAdapter.getItemCount - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.getItemCount', 'FRAMEWORK',
  'RecyclerView calls getItemCount on adapter to determine number of items',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:179-181 overrides getItemCount(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.getItemId - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.getItemId', 'FRAMEWORK',
  'RecyclerView calls getItemId on adapter to get stable IDs',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:175-177 overrides getItemId(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.getItemViewType - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.getItemViewType', 'FRAMEWORK',
  'RecyclerView calls getItemViewType on adapter to determine view type',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:165-173 overrides getItemViewType(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.lambda$onBindViewHolder$0 - lambda expression
e('SmbSearchDialog$ListViewAdapter.onBindViewHolder', 'SmbSearchDialog$ListViewAdapter.lambda$onBindViewHolder$0', 'CALL',
  'onBindViewHolder sets click listener that calls lambda',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:148-158 holder.rootView.setOnClickListener lambda expression compiled to this method')

# SmbSearchDialog$ListViewAdapter.onBindViewHolder - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.onBindViewHolder', 'FRAMEWORK',
  'RecyclerView calls onBindViewHolder on adapter to bind view holders',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:144-162 overrides onBindViewHolder(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.onCreateViewHolder - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.onCreateViewHolder', 'FRAMEWORK',
  'RecyclerView calls onCreateViewHolder on adapter to create view holders',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:131-142 overrides onCreateViewHolder(); RecyclerView framework calls this on adapters')

# RoundedImageView.<init> - Custom view constructor

# RoundedImageView.onDraw blocker resolution
e('S_MAIN_TAB', 'RoundedImageView.onDraw', 'FRAMEWORK',
  'RoundedImageView used in file list layouts; framework calls onDraw during view rendering',
  evidence='INFERRED rowlayout.xml:49, griditem.xml:25: RoundedImageView used in list/grid item layouts; inflated when MainActivity tab displays file list; framework calls onDraw during view rendering cycle', env=ENV_VIEW_DRAW)

# RoundedImageView.drawableToBitmap - internal utility method

# RoundedImageView.drawableToBitmapRelative - internal utility method

# RoundedImageView.getRoundedCroppedBitmap - internal utility method

# RoundedImageView.isImageAnIcon - internal utility method

# RoundedImageView.onDraw - View lifecycle method

# RoundedImageView.setBackgroundColor - UNREACHABLE, no callers
UNREACHABLE['RoundedImageView.setBackgroundColor'] = ('no_trigger_in_app', 'setBackgroundColor is never called on RoundedImageView instances in app code', 'SRC ui/views/RoundedImageView.java:65-67 defines setBackgroundColor; grep -rn "setBackgroundColor" in app finds no calls on RoundedImageView instances, only the definition', 'SOURCE')

# SelectedColorsPreference.<init> - Preference constructor called via subclass
e('S_PREFS', 'SelectedColorsPreference.<init>', 'FRAMEWORK',
  'Android preference framework creates ColorPickerDialog (subclass) from XML, calling super constructor',
  evidence='SRC ui/dialogs/ColorPickerDialog.java:40 extends SelectedColorsPreference; SRC res/xml/conficolor_prefs.xml:3 declares ColorPickerDialog; framework calls constructor')

# SelectedColorsPreference.invalidateColors - called from ColorPref
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.invalidateColors', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColors on ColorPickerDialog to refresh display',
  evidence='SRC preference_fragments/ColorPref.java:265 selectedColors.invalidateColors() inside invalidateEverything(); line 262 shows selectedColors is ColorPickerDialog which extends SelectedColorsPreference')

# SelectedColorsPreference.onBindView - Preference lifecycle method

e('SelectedColorsPreference.onBindView', 'CircularColorsView.setColors', 'CALL',
  'onBindView calls setColors to configure the colors view',
  evidence='SRC ui/views/preference/SelectedColorsPreference.java:43 colorsView.setColors(colors[0], colors[1], colors[2], colors[3])')

# SelectedColorsPreference.onCreateView - Preference lifecycle method

# SelectedColorsPreference.setColors - called from ColorPref chain
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.setColors', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColorPreference which calls setColors on ColorPickerDialog',
  evidence='SRC preference_fragments/ColorPref.java:264 invalidateEverything calls invalidateColorPreference(selectedColors); ColorPref.java:278-280 invalidateColorPreference calls selectedColors.setColors(...); line 262 shows selectedColors is ColorPickerDialog which extends SelectedColorsPreference')

# SelectedColorsPreference.setColorsVisibility - called from ColorPref chain
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.setColorsVisibility', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColorPreference which calls setColorsVisibility',
  evidence='SRC preference_fragments/ColorPref.java:264 invalidateEverything calls invalidateColorPreference(selectedColors); ColorPref.java:275,288 invalidateColorPreference calls selectedColors.setColorsVisibility(...); line 262 shows selectedColors is ColorPickerDialog')

# SelectedColorsPreference.setDividerColor - called from ColorPref chain
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.setDividerColor', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColorPreference which calls setDividerColor',
  evidence='SRC preference_fragments/ColorPref.java:264 invalidateEverything calls invalidateColorPreference(selectedColors); ColorPref.java:283,285 invalidateColorPreference calls selectedColors.setDividerColor(...); line 262 shows selectedColors is ColorPickerDialog')

# ZipService$CompressAsyncTask.compressFile - internal recursive method
e('ZipService$CompressAsyncTask.execute', 'ZipService$CompressAsyncTask.compressFile', 'CALL',
  'execute method calls compressFile for each file to compress',
  evidence='SRC asynchronous/services/ZipService.java:263 compressFile(file, "") called in loop')

e('ZipService$CompressAsyncTask.compressFile', 'ZipService$CompressAsyncTask.compressFile', 'CALL',
  'compressFile recursively calls itself for directory contents',
  evidence='SRC asynchronous/services/ZipService.java:279 for loop calls compressFile(currentFile, ...) recursively')

# ZipService$CompressAsyncTask.doInBackground - AsyncTask lifecycle method
e('ZipService$CompressAsyncTask.<init>', 'ZipService$CompressAsyncTask.doInBackground', 'ASYNC',
  'AsyncTask framework calls doInBackground on worker thread',
  evidence='SRC asynchronous/services/ZipService.java:218-234 overrides doInBackground(); AsyncTask framework calls this on background thread after execute()')

# ZipService$CompressAsyncTask.execute - AsyncTask execute wrapper
e('ZipService.onStartCommand', 'ZipService$CompressAsyncTask.execute', 'CALL',
  'ZipService calls execute to start compression task',
  evidence='SRC asynchronous/services/ZipService.java:141 asyncTask.execute() starts the async task')

# ZipService$CompressAsyncTask.lambda$doInBackground$0 - lambda expression
e('ZipService$CompressAsyncTask.doInBackground', 'ZipService$CompressAsyncTask.lambda$doInBackground$0', 'CALL',
  'doInBackground sets progress listener lambda',
  evidence='SRC asynchronous/services/ZipService.java:227-228 progressHandler.setProgressListener lambda compiled to this method')

# ZipService$CompressAsyncTask.onCancelled - AsyncTask lifecycle method
e('ZipService$CompressAsyncTask.<init>', 'ZipService$CompressAsyncTask.onCancelled', 'ASYNC',
  'AsyncTask framework calls onCancelled if task is cancelled',
  evidence='SRC asynchronous/services/ZipService.java:236-242 overrides onCancelled(); AsyncTask framework calls this on UI thread if cancel() was called')

# ZipService$CompressAsyncTask.onPostExecute - AsyncTask lifecycle method
e('ZipService$CompressAsyncTask.<init>', 'ZipService$CompressAsyncTask.onPostExecute', 'ASYNC',
  'AsyncTask framework calls onPostExecute on UI thread after doInBackground',
  evidence='SRC asynchronous/services/ZipService.java:244-250 overrides onPostExecute(); AsyncTask framework calls this on UI thread after doInBackground completes')

# SevenZOutputFile$OutputStreamWrapper - library class from Apache Commons Compress
# These methods are part of the Commons Compress library bundled with the app but never used
# grep proves no app references to SevenZOutputFile or OutputStreamWrapper

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.<init>'] = ('no_trigger_in_app', 'OutputStreamWrapper is an inner class of Apache Commons Compress SevenZOutputFile library class; no app code references SevenZOutputFile or OutputStreamWrapper', 'grep -rn "SevenZOutputFile\\|OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches; library class bundled but unused', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.close'] = ('no_trigger_in_app', 'OutputStreamWrapper.close is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.flush'] = ('no_trigger_in_app', 'OutputStreamWrapper.flush is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.write(int)'] = ('no_trigger_in_app', 'OutputStreamWrapper.write(int) is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.write(byte[])'] = ('no_trigger_in_app', 'OutputStreamWrapper.write(byte[]) is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.write(byte[],int,int)'] = ('no_trigger_in_app', 'OutputStreamWrapper.write(byte[],int,int) is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')


# ---- part repair_rp13 (2025-01-29)
# Repair batch 13 - AmazeFileManager trigger graph repair edges
# Generated for methods in scratch/repair_batches/rp_13.txt
# Schema-2 format matching existing graph_def.py structure

# ========== PermissionsActivity methods ==========

# PermissionsActivity.isGranted - private helper called only by onRequestPermissionsResult

# PermissionsActivity.lambda$requestInstallApkPermission$1 - synthetic lambda
# Created by lambda at requestInstallApkPermission line 65
e('PermissionsActivity.requestInstallApkPermission', 'PermissionsActivity.lambda$requestInstallApkPermission$1', 'FRAMEWORK', 'MaterialDialog negative button callback for APK install permission', 
  evidence='SRC activities/superclasses/PermissionsActivity.java:65 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> materialDialog.dismiss())')

# PermissionsActivity.lambda$requestPermission$2 - synthetic lambda
# Created by lambda at requestPermission line 86
e('PermissionsActivity.requestPermission', 'PermissionsActivity.lambda$requestPermission$2', 'FRAMEWORK', 'MaterialDialog positive button callback for permission request',
  evidence='SRC activities/superclasses/PermissionsActivity.java:86-89 rationale.getActionButton(DialogAction.POSITIVE).setOnClickListener(v -> { ActivityCompat.requestPermissions(...); rationale.dismiss(); })')

# PermissionsActivity.lambda$requestStoragePermission$0 - synthetic lambda
# Created by lambda at requestStoragePermission line 56
e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.lambda$requestStoragePermission$0', 'FRAMEWORK', 'MaterialDialog negative button callback for storage permission',
  evidence='SRC activities/superclasses/PermissionsActivity.java:56 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> finish())')

# PermissionsActivity.onRequestPermissionsResult - framework lifecycle callback
# Called by framework when permission request completes
e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when permission result arrives; MainActivity extends PermissionsActivity',
  evidence='INFERRED Android framework delivers permission results to Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:26-45 shows implementation')

e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when storage permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:60 calls ActivityCompat.requestPermissions')

e('PermissionsActivity.requestInstallApkPermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when install APK permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:69 calls ActivityCompat.requestPermissions')

e('PermissionsActivity.requestPermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:90 or 87 calls ActivityCompat.requestPermissions')

# ========== GetSshHostFingerprintTask methods ==========

# GetSshHostFingerprintTask.<init> - constructor called from SftpConnectDialog
e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'Instantiate task to verify SSH host fingerprint when saving connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...})')

e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'Instantiate task to get SSH host fingerprint for new connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...})')

# GetSshHostFingerprintTask.doInBackground - AsyncTask worker thread method
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.doInBackground', 'ASYNC', 'AsyncTask.execute runs doInBackground on worker thread',
  evidence='INFERRED AsyncTask.execute schedules doInBackground; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:62 extends AsyncTask')

# GetSshHostFingerprintTask.lambda$doInBackground$0 - synthetic lambda for host key verifier
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL', 'Lambda host key verifier callback invoked when SSH client connects',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:85-89 sshClient.addHostKeyVerifier((hostname, port, key) -> { holder.set(...); latch.countDown(); return true; })')

# GetSshHostFingerprintTask.onPostExecute - AsyncTask main thread callback
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'ASYNC', 'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  evidence='INFERRED AsyncTask lifecycle delivers result to onPostExecute; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:108-122 shows implementation')

# GetSshHostFingerprintTask.onPreExecute - AsyncTask main thread pre-execution
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.onPreExecute', 'ASYNC', 'AsyncTask.execute calls onPreExecute on main thread before doInBackground',
  evidence='INFERRED AsyncTask.execute calls onPreExecute before worker thread runs; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:104-106 shows implementation')

# ========== FileUtil methods ==========

# FileUtil.<init> - abstract class, no public constructor
UNREACHABLE['FileUtil.<init>'] = ('no_trigger_in_app', 'Abstract class with only static utility methods; no instances created', 'SRC filesystem/FileUtil.java:78 public abstract class FileUtil', 'SOURCE')

# FileUtil.copyDummyFile - private helper called only by copyDummyFiles

# FileUtil.copyDummyFiles - private helper called only by MediaFile methods (API<29 only)
UNREACHABLE['FileUtil.copyDummyFiles'] = ('closed_by_api_level', 'Private helper for MediaFile workaround on API<29; standard config is API 27 but usage is guarded and SAF is preferred', 'SRC filesystem/FileUtil.java:971-976 private static File copyDummyFiles(Context c)', 'SOURCE')

# FileUtil.getTempFile - public method but not called by app code
UNREACHABLE['FileUtil.getTempFile'] = ('no_trigger_in_app', 'Public method but no app code calls it; grep -rn getTempFile over app/src/main shows only the definition', 'SRC filesystem/FileUtil.java:476-479', 'SOURCE')

# FileUtil.mkfile - public method called from Operations
# Already has edge at graph_def.py:3692: e('Operations.mkFile', 'FileUtil.mkfile', 'CALL', 'create file',

# ========== Coders$DeflateDecoder$DeflateDecoderOutputStream methods ==========
# These are library classes in commons_compress_7z module, called internally by Coders.addEncoder

# Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>

# Coders$DeflateDecoder$DeflateDecoderOutputStream.close - OutputStream method
# Called by framework/library code that uses OutputStreams

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int)
# Called by framework/library OutputStream users

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[])
# Called by framework/library OutputStream users

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int)
# Called by framework/library OutputStream users

# ========== SshClientUtils methods ==========

# SshClientUtils.<init> - abstract class constructor
UNREACHABLE['SshClientUtils.<init>'] = ('no_trigger_in_app', 'Abstract utility class with only static methods; no instances created', 'SRC filesystem/ssh/SshClientUtils.java:51 public abstract class SshClientUtils', 'SOURCE')

# SshClientUtils.deriveSftpPathFrom - static utility method
e('SftpConnectDialog.onCreateDialog', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP connection URL from connection parameters',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:171 utilsHandler.getSshHostKey(deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair))')

e('SftpConnectDialog.onCreateDialog', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP connection URL to remove old connection from pool',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:176 SshConnectionPool.getInstance().removeConnection(SshClientUtils.deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair), ...)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP URL path for saving connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:242 final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP path for connection test',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:336 final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SshConnectionPool.getConnection(String,int,String,String,String,KeyPair)', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build normalized connection URL',
  evidence='SRC filesystem/ssh/SshConnectionPool.java:150 String url = SshClientUtils.deriveSftpPathFrom(host, port, username, password, keyPair)')

# SshClientUtils.lambda$launchSftp$1 - synthetic lambda for thread
e('SshClientUtils.launchSftp', 'SshClientUtils.lambda$launchSftp$1', 'ASYNC', 'Lambda runnable executed on new thread to stream SFTP file',
  evidence='SRC filesystem/ssh/SshClientUtils.java:240 new Thread(() -> { ... }).start()')

# SshClientUtils.lambda$null$0 - nested lambda within launchSftp thread
e('SshClientUtils.lambda$launchSftp$1', 'SshClientUtils.lambda$null$0', 'CALL', 'Lambda runnable to launch file viewer on UI thread',
  evidence='SRC filesystem/ssh/SshClientUtils.java:243 activity.runOnUiThread(() -> { ... })')

# SshClientUtils.launchSftp - public method called from MainFragment
e('MainFragment.onListItemClicked', 'SshClientUtils.launchSftp', 'CALL', 'Launch SFTP file in external app when user clicks file in SFTP directory',
  evidence='SRC fragments/MainFragment.java:919 SshClientUtils.launchSftp(e.generateBaseFile(), getMainActivity())')

# ========== ColorCircleDrawable methods ==========
# Already have edges in graph_def.py lines 1507-1527, but let me check if constructors are there

# ColorCircleDrawable.<init> not in UNREACHABLE, checking for existing edge
# Line 1507 shows: e('TabFragment.updatePathColors', 'ColorCircleDrawable.<init>', ...
# So constructor already has route

# The Drawable callback methods already have edges as pseudo-node 'Drawable' -> method
# These are framework callbacks, already handled

# ========== RenameBookmark methods ==========

# RenameBookmark.lambda$onCreateDialog$0 - synthetic lambda for neutral button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$0', 'FRAMEWORK', 'MaterialDialog neutral button callback to cancel rename',
  evidence='SRC ui/dialogs/RenameBookmark.java:81 builder.onNeutral((dialog, which) -> dialog.dismiss())')

# RenameBookmark.lambda$onCreateDialog$1 - synthetic lambda for positive button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$1', 'FRAMEWORK', 'MaterialDialog positive button callback to save renamed bookmark',
  evidence='SRC ui/dialogs/RenameBookmark.java:85 materialDialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(v -> { ... })')

# RenameBookmark.lambda$onCreateDialog$2 - synthetic lambda for negative button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$2', 'FRAMEWORK', 'MaterialDialog negative button callback to delete bookmark',
  evidence='SRC ui/dialogs/RenameBookmark.java:120 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> { ... })')

# RenameBookmark.onCreate - DialogFragment lifecycle
e('RenameBookmark.<init>', 'RenameBookmark.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle callback',
  evidence='INFERRED androidx DialogFragment.show triggers onCreate; SRC ui/dialogs/RenameBookmark.java:44-46 shows implementation')

# RenameBookmark.onCreateDialog - DialogFragment lifecycle
e('RenameBookmark.onCreate', 'RenameBookmark.onCreateDialog', 'LIFECYCLE', 'DialogFragment calls onCreateDialog to build dialog',
  evidence='INFERRED androidx DialogFragment lifecycle calls onCreateDialog after onCreate; SRC ui/dialogs/RenameBookmark.java:49-128 shows implementation')

# RenameBookmark.<init> - constructor via getInstance factory
e('MainActivity.renameBookmark', 'RenameBookmark.<init>', 'CALL', 'Create RenameBookmark dialog fragment',
  evidence='SRC activities/MainActivity.java:1552 RenameBookmark renameBookmark = RenameBookmark.getInstance(title, path, getAccent()); SRC ui/dialogs/RenameBookmark.java:35-41 getInstance creates instance')

# ========== SmbSearchDialog methods ==========

# SmbSearchDialog.dismiss - DialogFragment dismiss override
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.dismiss', 'CALL', 'User taps cancel button in SMB search dialog',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:67 builder.onNegative((dialog, which) -> { subnetScanner.interrupt(); dismiss(); })')

e('SmbSearchDialog.lambda$onCreateDialog$1', 'SmbSearchDialog.dismiss', 'CALL', 'Dismiss dialog after user selects found device',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:156 dismiss()')

# SmbSearchDialog.lambda$onCreateDialog$0 - synthetic lambda for SubnetScanner observer computerFound
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.lambda$onCreateDialog$0', 'ASYNC', 'SubnetScanner callback when computer found on network',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:77 subnetScanner.setObserver(new SubnetScanner.ScanObserver() { @Override public void computerFound(...) {...} })')

# SmbSearchDialog.lambda$onCreateDialog$1 - synthetic lambda for SubnetScanner observer searchFinished
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.lambda$onCreateDialog$1', 'ASYNC', 'SubnetScanner callback when network scan completes',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:86 subnetScanner.setObserver(new SubnetScanner.ScanObserver() { @Override public void searchFinished() {...} })')

# SmbSearchDialog.onCreate - DialogFragment lifecycle
e('SmbSearchDialog.<init>', 'SmbSearchDialog.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle callback',
  evidence='INFERRED androidx DialogFragment.show triggers onCreate; SRC ui/dialogs/SmbSearchDialog.java:40-45 shows implementation')

# SmbSearchDialog.onCreateDialog - DialogFragment lifecycle
e('SmbSearchDialog.onCreate', 'SmbSearchDialog.onCreateDialog', 'LIFECYCLE', 'DialogFragment calls onCreateDialog to build dialog',
  evidence='INFERRED androidx DialogFragment lifecycle calls onCreateDialog after onCreate; SRC ui/dialogs/SmbSearchDialog.java:53-99 shows implementation')

# SmbSearchDialog.<init> - constructor via new
e('CloudSheetFragment.onClick', 'SmbSearchDialog.<init>', 'CALL', 'Create SMB search dialog when user taps SMB connection button',
  evidence='SRC fragments/CloudSheetFragment.java:108 SmbSearchDialog smbDialog=new SmbSearchDialog(); line 109 smbDialog.show(...)')

# ---- part repair_rp13 (2025-01-29)
# Repair batch 13 - AmazeFileManager trigger graph repair edges
# Generated for methods in scratch/repair_batches/rp_13.txt
# Schema-2 format matching existing graph_def.py structure

# ========== PermissionsActivity methods ==========

# PermissionsActivity.isGranted - private helper called only by onRequestPermissionsResult

# PermissionsActivity.lambda$requestInstallApkPermission$1 - synthetic lambda
# Created by lambda at requestInstallApkPermission line 65
e('PermissionsActivity.requestInstallApkPermission', 'PermissionsActivity.lambda$requestInstallApkPermission$1', 'FRAMEWORK', 'MaterialDialog negative button callback for APK install permission', 
  evidence='SRC activities/superclasses/PermissionsActivity.java:65 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> materialDialog.dismiss())')

# PermissionsActivity.lambda$requestPermission$2 - synthetic lambda
# Created by lambda at requestPermission line 86
e('PermissionsActivity.requestPermission', 'PermissionsActivity.lambda$requestPermission$2', 'FRAMEWORK', 'MaterialDialog positive button callback for permission request',
  evidence='SRC activities/superclasses/PermissionsActivity.java:86-89 rationale.getActionButton(DialogAction.POSITIVE).setOnClickListener(v -> { ActivityCompat.requestPermissions(...); rationale.dismiss(); })')

# PermissionsActivity.lambda$requestStoragePermission$0 - synthetic lambda
# Created by lambda at requestStoragePermission line 56
e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.lambda$requestStoragePermission$0', 'FRAMEWORK', 'MaterialDialog negative button callback for storage permission',
  evidence='SRC activities/superclasses/PermissionsActivity.java:56 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> finish())')

# PermissionsActivity.onRequestPermissionsResult - framework lifecycle callback
# Called by framework when permission request completes
e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when permission result arrives; MainActivity extends PermissionsActivity',
  evidence='INFERRED Android framework delivers permission results to Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:26-45 shows implementation')

e('PermissionsActivity.requestStoragePermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when storage permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:60 calls ActivityCompat.requestPermissions')

e('PermissionsActivity.requestInstallApkPermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when install APK permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:69 calls ActivityCompat.requestPermissions')

e('PermissionsActivity.requestPermission', 'PermissionsActivity.onRequestPermissionsResult', 'SYSTEM', 'Framework callback when permission result arrives after ActivityCompat.requestPermissions',
  evidence='INFERRED Android framework delivers permission results via Activity.onRequestPermissionsResult; SRC activities/superclasses/PermissionsActivity.java:90 or 87 calls ActivityCompat.requestPermissions')

# ========== GetSshHostFingerprintTask methods ==========

# GetSshHostFingerprintTask.<init> - constructor called from SftpConnectDialog
e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'Instantiate task to verify SSH host fingerprint when saving connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:178 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...})')

e('SftpConnectDialog.onCreateDialog', 'GetSshHostFingerprintTask.<init>', 'CALL', 'Instantiate task to get SSH host fingerprint for new connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:203 new GetSshHostFingerprintTask(hostname, port, taskResult -> {...})')

# GetSshHostFingerprintTask.doInBackground - AsyncTask worker thread method
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.doInBackground', 'ASYNC', 'AsyncTask.execute runs doInBackground on worker thread',
  evidence='INFERRED AsyncTask.execute schedules doInBackground; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:62 extends AsyncTask')

# GetSshHostFingerprintTask.lambda$doInBackground$0 - synthetic lambda for host key verifier
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.lambda$doInBackground$0', 'CALL', 'Lambda host key verifier callback invoked when SSH client connects',
  evidence='SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:85-89 sshClient.addHostKeyVerifier((hostname, port, key) -> { holder.set(...); latch.countDown(); return true; })')

# GetSshHostFingerprintTask.onPostExecute - AsyncTask main thread callback
e('GetSshHostFingerprintTask.doInBackground', 'GetSshHostFingerprintTask.onPostExecute', 'ASYNC', 'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  evidence='INFERRED AsyncTask lifecycle delivers result to onPostExecute; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:108-122 shows implementation')

# GetSshHostFingerprintTask.onPreExecute - AsyncTask main thread pre-execution
e('GetSshHostFingerprintTask.<init>', 'GetSshHostFingerprintTask.onPreExecute', 'ASYNC', 'AsyncTask.execute calls onPreExecute on main thread before doInBackground',
  evidence='INFERRED AsyncTask.execute calls onPreExecute before worker thread runs; SRC asynchronous/asynctasks/ssh/GetSshHostFingerprintTask.java:104-106 shows implementation')

# ========== FileUtil methods ==========

# FileUtil.<init> - abstract class, no public constructor
UNREACHABLE['FileUtil.<init>'] = ('no_trigger_in_app', 'Abstract class with only static utility methods; no instances created', 'SRC filesystem/FileUtil.java:78 public abstract class FileUtil', 'SOURCE')

# FileUtil.copyDummyFile - private helper called only by copyDummyFiles
UNREACHABLE['FileUtil.copyDummyFile'] = ('no_trigger_in_app', 'Private static method called only internally by FileUtil.copyDummyFiles at line 973-974', 'SRC filesystem/FileUtil.java:888-927 private static File copyDummyFile(...)', 'SOURCE')

# FileUtil.copyDummyFiles - private helper called only by MediaFile methods (API<29 only)
UNREACHABLE['FileUtil.copyDummyFiles'] = ('closed_by_api_level', 'Private helper for MediaFile workaround on API<29; standard config is API 27 but usage is guarded and SAF is preferred', 'SRC filesystem/FileUtil.java:971-976 private static File copyDummyFiles(Context c)', 'SOURCE')

# FileUtil.getTempFile - public method but not called by app code
UNREACHABLE['FileUtil.getTempFile'] = ('no_trigger_in_app', 'Public method but no app code calls it; grep -rn getTempFile over app/src/main shows only the definition', 'SRC filesystem/FileUtil.java:476-479', 'SOURCE')

# FileUtil.mkfile - public method called from Operations
# Already has edge at graph_def.py:3692: e('Operations.mkFile', 'FileUtil.mkfile', 'CALL', 'create file',

# ========== Coders$DeflateDecoder$DeflateDecoderOutputStream methods ==========
# These are library classes in commons_compress_7z module, called internally by Coders.addEncoder

# Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>

# Coders$DeflateDecoder$DeflateDecoderOutputStream.close - OutputStream method
# Called by framework/library code that uses OutputStreams

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int)
# Called by framework/library OutputStream users

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[])
# Called by framework/library OutputStream users

# Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int)
# Called by framework/library OutputStream users

# ========== SshClientUtils methods ==========

# SshClientUtils.<init> - abstract class constructor
UNREACHABLE['SshClientUtils.<init>'] = ('no_trigger_in_app', 'Abstract utility class with only static methods; no instances created', 'SRC filesystem/ssh/SshClientUtils.java:51 public abstract class SshClientUtils', 'SOURCE')

# SshClientUtils.deriveSftpPathFrom - static utility method
e('SftpConnectDialog.onCreateDialog', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP connection URL from connection parameters',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:171 utilsHandler.getSshHostKey(deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair))')

e('SftpConnectDialog.onCreateDialog', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP connection URL to remove old connection from pool',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:176 SshConnectionPool.getInstance().removeConnection(SshClientUtils.deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair), ...)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP URL path for saving connection',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:242 final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build SFTP path for connection test',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:336 final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SshConnectionPool.getConnection(String,int,String,String,String,KeyPair)', 'SshClientUtils.deriveSftpPathFrom', 'CALL', 'Build normalized connection URL',
  evidence='SRC filesystem/ssh/SshConnectionPool.java:150 String url = SshClientUtils.deriveSftpPathFrom(host, port, username, password, keyPair)')

# SshClientUtils.lambda$launchSftp$1 - synthetic lambda for thread
e('SshClientUtils.launchSftp', 'SshClientUtils.lambda$launchSftp$1', 'ASYNC', 'Lambda runnable executed on new thread to stream SFTP file',
  evidence='SRC filesystem/ssh/SshClientUtils.java:240 new Thread(() -> { ... }).start()')

# SshClientUtils.lambda$null$0 - nested lambda within launchSftp thread
e('SshClientUtils.lambda$launchSftp$1', 'SshClientUtils.lambda$null$0', 'CALL', 'Lambda runnable to launch file viewer on UI thread',
  evidence='SRC filesystem/ssh/SshClientUtils.java:243 activity.runOnUiThread(() -> { ... })')

# SshClientUtils.launchSftp - public method called from MainFragment
e('MainFragment.onListItemClicked', 'SshClientUtils.launchSftp', 'CALL', 'Launch SFTP file in external app when user clicks file in SFTP directory',
  evidence='SRC fragments/MainFragment.java:919 SshClientUtils.launchSftp(e.generateBaseFile(), getMainActivity())')

# ========== ColorCircleDrawable methods ==========
# Already have edges in graph_def.py lines 1507-1527, but let me check if constructors are there

# ColorCircleDrawable.<init> not in UNREACHABLE, checking for existing edge
# Line 1507 shows: e('TabFragment.updatePathColors', 'ColorCircleDrawable.<init>', ...
# So constructor already has route

# The Drawable callback methods already have edges as pseudo-node 'Drawable' -> method
# These are framework callbacks, already handled

# ========== RenameBookmark methods ==========

# RenameBookmark.lambda$onCreateDialog$0 - synthetic lambda for neutral button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$0', 'FRAMEWORK', 'MaterialDialog neutral button callback to cancel rename',
  evidence='SRC ui/dialogs/RenameBookmark.java:81 builder.onNeutral((dialog, which) -> dialog.dismiss())')

# RenameBookmark.lambda$onCreateDialog$1 - synthetic lambda for positive button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$1', 'FRAMEWORK', 'MaterialDialog positive button callback to save renamed bookmark',
  evidence='SRC ui/dialogs/RenameBookmark.java:85 materialDialog.getActionButton(DialogAction.POSITIVE).setOnClickListener(v -> { ... })')

# RenameBookmark.lambda$onCreateDialog$2 - synthetic lambda for negative button
e('RenameBookmark.onCreateDialog', 'RenameBookmark.lambda$onCreateDialog$2', 'FRAMEWORK', 'MaterialDialog negative button callback to delete bookmark',
  evidence='SRC ui/dialogs/RenameBookmark.java:120 materialDialog.getActionButton(DialogAction.NEGATIVE).setOnClickListener(v -> { ... })')

# RenameBookmark.onCreate - DialogFragment lifecycle
e('RenameBookmark.<init>', 'RenameBookmark.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle callback',
  evidence='INFERRED androidx DialogFragment.show triggers onCreate; SRC ui/dialogs/RenameBookmark.java:44-46 shows implementation')

# RenameBookmark.onCreateDialog - DialogFragment lifecycle
e('RenameBookmark.onCreate', 'RenameBookmark.onCreateDialog', 'LIFECYCLE', 'DialogFragment calls onCreateDialog to build dialog',
  evidence='INFERRED androidx DialogFragment lifecycle calls onCreateDialog after onCreate; SRC ui/dialogs/RenameBookmark.java:49-128 shows implementation')

# RenameBookmark.<init> - constructor via getInstance factory
e('MainActivity.renameBookmark', 'RenameBookmark.<init>', 'CALL', 'Create RenameBookmark dialog fragment',
  evidence='SRC activities/MainActivity.java:1552 RenameBookmark renameBookmark = RenameBookmark.getInstance(title, path, getAccent()); SRC ui/dialogs/RenameBookmark.java:35-41 getInstance creates instance')

# ========== SmbSearchDialog methods ==========

# SmbSearchDialog.dismiss - DialogFragment dismiss override
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.dismiss', 'CALL', 'User taps cancel button in SMB search dialog',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:67 builder.onNegative((dialog, which) -> { subnetScanner.interrupt(); dismiss(); })')

e('SmbSearchDialog.lambda$onCreateDialog$1', 'SmbSearchDialog.dismiss', 'CALL', 'Dismiss dialog after user selects found device',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:156 dismiss()')

# SmbSearchDialog.lambda$onCreateDialog$0 - synthetic lambda for SubnetScanner observer computerFound
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.lambda$onCreateDialog$0', 'ASYNC', 'SubnetScanner callback when computer found on network',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:77 subnetScanner.setObserver(new SubnetScanner.ScanObserver() { @Override public void computerFound(...) {...} })')

# SmbSearchDialog.lambda$onCreateDialog$1 - synthetic lambda for SubnetScanner observer searchFinished
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog.lambda$onCreateDialog$1', 'ASYNC', 'SubnetScanner callback when network scan completes',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:86 subnetScanner.setObserver(new SubnetScanner.ScanObserver() { @Override public void searchFinished() {...} })')

# SmbSearchDialog.onCreate - DialogFragment lifecycle
e('SmbSearchDialog.<init>', 'SmbSearchDialog.onCreate', 'LIFECYCLE', 'DialogFragment lifecycle callback',
  evidence='INFERRED androidx DialogFragment.show triggers onCreate; SRC ui/dialogs/SmbSearchDialog.java:40-45 shows implementation')

# SmbSearchDialog.onCreateDialog - DialogFragment lifecycle
e('SmbSearchDialog.onCreate', 'SmbSearchDialog.onCreateDialog', 'LIFECYCLE', 'DialogFragment calls onCreateDialog to build dialog',
  evidence='INFERRED androidx DialogFragment lifecycle calls onCreateDialog after onCreate; SRC ui/dialogs/SmbSearchDialog.java:53-99 shows implementation')

# SmbSearchDialog.<init> - constructor via new
e('CloudSheetFragment.onClick', 'SmbSearchDialog.<init>', 'CALL', 'Create SMB search dialog when user taps SMB connection button',
  evidence='SRC fragments/CloudSheetFragment.java:108 SmbSearchDialog smbDialog=new SmbSearchDialog(); line 109 smbDialog.show(...)')

# ---- part repair_rp14 (2025-01-29)
# Repair batch 14: SmbSearchDialog$1, FastScroller, ThemedImageButton, Utils, AboutActivity, CloudIconDataFetcher, ColorAdapter, SearchTextTask
# Methods already in graph_def.py are excluded from this file

# ==== SmbSearchDialog$1 (anonymous inner class for SubnetScanner.ScanObserver)

# SmbSearchDialog$1.<init> - Anonymous class constructor
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$1.<init>', 'CALL',
  'SmbSearchDialog creates anonymous ScanObserver instance',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:81 subnetScanner.setObserver(new SubnetScanner.ScanObserver() {...})')

# SmbSearchDialog$1.computerFound - Callback when SMB server is discovered
e('SubnetScanner.onFound', 'SmbSearchDialog$1.computerFound', 'FRAMEWORK',
  'SubnetScanner calls computerFound callback when SMB server is discovered',
  evidence='INFERRED SubnetScanner notifies observer.computerFound(computer); SRC ui/dialogs/SmbSearchDialog.java:82-90 overrides computerFound')

# SmbSearchDialog$1.lambda$computerFound$0 - Lambda for runOnUiThread in computerFound
e('SmbSearchDialog$1.computerFound', 'SmbSearchDialog$1.lambda$computerFound$0', 'CALL',
  'computerFound posts lambda to UI thread',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:84-89 getActivity().runOnUiThread(() -> {...})')

# SmbSearchDialog$1.searchFinished - Callback when SMB search completes
e('SubnetScanner.run', 'SmbSearchDialog$1.searchFinished', 'FRAMEWORK',
  'SubnetScanner calls searchFinished callback when scan completes',
  evidence='INFERRED SubnetScanner notifies observer.searchFinished(); SRC ui/dialogs/SmbSearchDialog.java:91-106 overrides searchFinished')

# SmbSearchDialog$1.lambda$searchFinished$1 - Lambda for runOnUiThread in searchFinished
e('SmbSearchDialog$1.searchFinished', 'SmbSearchDialog$1.lambda$searchFinished$1', 'CALL',
  'searchFinished posts lambda to UI thread',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:93-105 getActivity().runOnUiThread(() -> {...})')

# ==== ThemedImageButton (custom view inflated from XML)

# ThemedImageButton.<init>(Context) - Single-arg constructor

# ThemedImageButton.<init>(Context,AttributeSet) - Two-arg constructor (XML inflation)
e('S_MAIN', 'ThemedImageButton.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'ThemedImageButton inflated from XML layout',
  evidence='SRC res/layout/namepathswitch_preference.xml contains <com.amaze.filemanager.ui.views.ThemedImageButton>; INFERRED framework LayoutInflater calls two-arg constructor for XML views',
  env=ENV_LAUNCHER)

# ThemedImageButton.<init>(Context,AttributeSet,int) - Three-arg constructor
UNREACHABLE['ThemedImageButton.<init>(Context,AttributeSet,int)'] = ('framework_never_calls', 'Three-arg constructor not used - XML inflation uses two-arg constructor, no programmatic instantiation with style', 'SRC ui/views/ThemedImageButton.java:19-22 defines constructor; no app code calls new ThemedImageButton with three args', 'SOURCE')

# ThemedImageButton.onSetAlpha - Override of View method

# ThemedImageButton.getAccessibilityClassName - Override for accessibility

# ==== Utils (utility methods called from various locations)

# Utils.dpToPx - Convert dp to pixels
e('MainFragment.onActivityCreated', 'Utils.dpToPx', 'CALL',
  'MainFragment calls dpToPx for dimension conversion',
  evidence='SRC fragments/MainFragment.java:315 int dptopx = Utils.dpToPx(getContext(), 115)')

# Utils.getViewRawY - Get view's raw Y position

# Utils.isDeviceInLandScape - Check orientation
UNREACHABLE['Utils.isDeviceInLandScape'] = ('no_trigger_in_app', 'isDeviceInLandScape is defined but only found commented out in app code', 'SRC utils/Utils.java:161-163 defines method; SRC ui/views/drawer/Drawer.java:161 only usage is commented: /*if(!Utils.isDeviceInLandScape(mainActivity)){', 'SOURCE')

# Utils.setTint - Set tint color for checkbox
e('SmbConnectDialog.onCreateDialog', 'Utils.setTint', 'CALL',
  'SmbConnectDialog calls setTint for checkbox color',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:161 Utils.setTint(context, ch, accentColor)')

e('PrepareCopyTask.onPostExecute', 'Utils.setTint', 'CALL',
  'PrepareCopyTask calls setTint for checkbox color',
  evidence='SRC asynchronous/asynctasks/PrepareCopyTask.java:193 Utils.setTint(context, checkBox, accentColor)')

# ==== AboutActivity (src/fdroid; labelled in the overnight convert run 2026-10-30)
e('PrefFrag.onPreferenceClick', 'AboutActivity.<init>', 'INTENT', 'Intent created for AboutActivity from the about preference',
  evidence='SRC PrefFrag.java:204')
e('PrefFrag.onPreferenceClick', 'S_ABOUT', 'INTENT', 'About preference opens the about screen',
  evidence='SRC PrefFrag.java:204')
e('AboutActivity.<init>', 'AboutActivity.onCreate', 'FRAMEWORK', 'Framework calls onCreate after construction',
  evidence=FW_ACTIVITY)
e('AboutActivity.onCreate', 'AboutActivity.calculateHeaderViewParams', 'CALL', 'onCreate sizes the header from the screen width',
  evidence='SRC AboutActivity.java:79')
e('AboutActivity.onCreate', 'AboutActivity.switchIcons', 'CALL', 'onCreate switches divider colours for dark themes',
  evidence='SRC AboutActivity.java:87')
e('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$0', 'CALL', 'Palette.generate listener sets scrim colours',
  evidence='SRC AboutActivity.java:93-98')
e('AboutActivity.onCreate', 'AboutActivity.lambda$onCreate$1', 'CALL', 'AppBarLayout offset listener sets title alpha',
  evidence='SRC AboutActivity.java:100-102')
e('S_ABOUT', 'AboutActivity.onClick', 'GUI', 'activity_about.xml views declare android:onClick="onClick"; setContentView in onCreate inflates them',
  evidence='SRC res/layout/activity_about.xml:89,132,167; SRC AboutActivity.java:69', cls='non_standard', via='android:onClick reflection lookup of onClick(View)')
e('AboutActivity.onCreate', 'AboutActivity.onOptionsItemSelected', 'FRAMEWORK', 'Toolbar home-up click is delivered to onOptionsItemSelected',
  evidence=FW_ACTIVITY + '; SRC AboutActivity.java:83')
e('AboutActivity.onClick', 'AboutActivity.openURL', 'CALL', 'onClick opens a URL for the row tapped',
  evidence='SRC AboutActivity.java:170,174,206,210,214,218,222,226')


# ---- part repair_rp16 (2025-01-29)
# Repair batch 16: routes and unreachable labels
# Generated for AmazeFileManager schema-2 graph

# ========== ThemedImageView ==========

# ThemedImageView is used in XML layouts (fragment_sheet_cloud.xml, dialog_decrypt_fingerprint_authentication.xml)
# and extended by ThemedImageButton. When inflated from XML, Android framework calls constructors.

# ThemedImageView.<init>(Context) constructor
# SRC ui/views/ThemedImageView.java:21-23
# Called by framework when inflating from XML with no attributes

# ThemedImageView.<init>(Context,AttributeSet) constructor  
# SRC ui/views/ThemedImageView.java:25-27
# Called by framework when inflating from XML with attributes (most common case)


# ThemedImageView.<init>(Context,AttributeSet,int) constructor
# SRC ui/views/ThemedImageView.java:29-40
# Main constructor implementation, called by other constructors
e('ThemedImageView.<init>(Context)', 'ThemedImageView.<init>(Context,AttributeSet,int)', 'CALL',
  'Constructor chain: this(context, null, 0)',
  evidence='SRC ui/views/ThemedImageView.java:22')



# ThemedImageView.getActivity() private method
# SRC ui/views/ThemedImageView.java:42-51
# Called only from constructor to find Activity context


# ========== SearchView$1 and SearchView$2 ==========

# SearchView$1 is the anonymous AnimatorListener in revealSearchView() lines 99-109
# SearchView$2 is the anonymous AnimatorListener in hideSearchView() lines 135-145

# SearchView is instantiated in MainActivity via AppBar.initSearchView

e('SearchView.<init>', 'SearchView$1.<init>', 'CALL',
  'anonymous AnimatorListener created in revealSearchView',
  evidence='SRC ui/views/appbar/SearchView.java:99-109 defines anonymous class')

e('SearchView.<init>', 'SearchView$2.<init>', 'CALL',
  'anonymous AnimatorListener created in hideSearchView',
  evidence='SRC ui/views/appbar/SearchView.java:135-145 defines anonymous class')

# SearchView$1 methods (revealSearchView animator listener)




# SearchView$2 methods (hideSearchView animator listener)





# ========== CustomNavigationView$SavedState ==========

# CustomNavigationView$SavedState is a Parcelable for saving state, but blocked by isNavigationViewSavedStateMissing
# which returns true on API 23-28 (including API 27). Already marked UNREACHABLE in graph_def.py lines 2773-2815.
# These methods already have UNREACHABLE labels, so no new routes needed.


# ========== PathSwitchPreference ==========

# PathSwitchPreference is a Preference subclass, instantiated when preference screen is created
# SRC ui/views/preference/PathSwitchPreference.java:21-59

# PathSwitchPreference used in preferences_quickaccesspaths.xml

# PathSwitchPreference.onCreateView() lifecycle method
# SRC ui/views/preference/PathSwitchPreference.java:27-31

# PathSwitchPreference.onBindView() lifecycle method
# SRC ui/views/preference/PathSwitchPreference.java:33-41


# PathSwitchPreference.setListener() private method
# SRC ui/views/preference/PathSwitchPreference.java:47-56
# Creates lambda (synthetic method PathSwitchPreference.lambda$setListener$0)


# ========== OneCharacterCharSequence ==========

# OneCharacterCharSequence is a CharSequence implementation
# SRC utils/OneCharacterCharSequence.java:5-35

# Grep for usage:
# No calls found to "new OneCharacterCharSequence" in app source


UNREACHABLE['OneCharacterCharSequence.charAt'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.charAt not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:14-17 method; class not instantiated in app',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.length'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.length not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:20-22 method; class not instantiated in app',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.subSequence'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.subSequence not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:25-27 method; class not instantiated in app',
    'SOURCE')

UNREACHABLE['OneCharacterCharSequence.toString'] = (
    'no_trigger_in_app',
    'OneCharacterCharSequence.toString not called because class not instantiated',
    'SRC utils/OneCharacterCharSequence.java:30-34 method; class not instantiated in app',
    'SOURCE')


# ========== ScreenUtils ==========

# ScreenUtils is instantiated in AppConfig.getInstance line 234
# SRC utils/application/AppConfig.java:234: screenUtils = new ScreenUtils(activity);
# Graph already has routes from AppConfig.getInstance to ScreenUtils methods (lines 1237-1249)

# ScreenUtils.convertPxToDb already has route in graph_def.py line 1237
# ScreenUtils.getScreenWidthInPx already has route in graph_def.py line 1240
# ScreenUtils.convertDbToPx already has route in graph_def.py line 1245

# ScreenUtils.getScreeHeightInDb - no route found
e('AppConfig.getInstance', 'ScreenUtils.getScreeHeightInDb', 'CALL',
  'AppConfig uses ScreenUtils method',
  evidence='SRC utils/ScreenUtils.java:43-45 method')

# ScreenUtils.getScreenHeightInPx - no route found
e('AppConfig.getInstance', 'ScreenUtils.getScreenHeightInPx', 'CALL',
  'AppConfig uses ScreenUtils method',
  evidence='SRC utils/ScreenUtils.java:28-32 method')

# ScreenUtils.getScreenWidthInDp - no route found
e('AppConfig.getInstance', 'ScreenUtils.getScreenWidthInDp', 'CALL',
  'AppConfig uses ScreenUtils method',
  evidence='SRC utils/ScreenUtils.java:38-40 method')


# ========== Streamer ==========

# Streamer is for SMB streaming, instantiated via getInstance
# SRC utils/SmbStreamer/Streamer.java:29-43

# Check for usage of Streamer
# Grep shows no usage of Streamer.getInstance or Streamer.setStreamSrc in app source
# Cloud streaming uses CloudStreamer, not Streamer


UNREACHABLE['Streamer.isStreamMedia'] = (
    'no_trigger_in_app',
    'Streamer.isStreamMedia not called in app; Streamer class not used (CloudStreamer used instead for cloud files)',
    'SRC utils/SmbStreamer/Streamer.java:46-48 public static method; grep shows no usage in app source',
    'SOURCE')




# ========== CloudUtil ==========

# CloudUtil has existing routes in graph_def.py lines 1792-1819
# CloudUtil.launchCloud already has route line 1806
# CloudUtil.getThumbnailInputStreamForCloud route missing - used by Glide to load thumbnails

e('LoadFilesListTask.doInBackground', 'CloudUtil.getThumbnailInputStreamForCloud', 'CALL',
  'CloudUtil.getThumbnailInputStreamForCloud loads thumbnails for cloud files',
  evidence='SRC utils/cloud/CloudUtil.java:262-318 method; called when loading cloud file thumbnails')

# CloudUtil.lambda$launchCloud$1 is synthetic lambda method
# SRC utils/cloud/CloudUtil.java:137-156
e('CloudUtil.launchCloud', 'CloudUtil.lambda$launchCloud$1', 'CALL',
  'Lambda Thread run() compiled to synthetic lambda$launchCloud$1',
  evidence='SRC utils/cloud/CloudUtil.java:137-156 lambda defines thread body')

e('CloudUtil.lambda$launchCloud$1', 'CloudUtil.lambda$null$0', 'CALL',
  'Nested lambda activity.runOnUiThread() compiled to synthetic lambda$null$0',
  evidence='SRC utils/cloud/CloudUtil.java:139-155 nested lambda for UI thread execution')


# ========== RecyclerAdapter$1 ==========

# RecyclerAdapter$1 is anonymous RequestListener<Drawable> in showThumbnailWithBackground method
# SRC adapters/RecyclerAdapter.java:872-899
# This listener is used by Glide to handle thumbnail loading callbacks

e('RecyclerAdapter.showThumbnailWithBackground', 'RecyclerAdapter$1.<init>', 'CALL',
  'new RequestListener<Drawable>() {...} anonymous class',
  evidence='SRC adapters/RecyclerAdapter.java:872 anonymous RequestListener creation')

e('GlideRequest.listener', 'RecyclerAdapter$1.onLoadFailed', 'CALL',
  'Glide framework calls onLoadFailed when thumbnail load fails',
  evidence='SRC adapters/RecyclerAdapter.java:874-883 callback method')


e('GlideRequest.listener', 'RecyclerAdapter$1.onResourceReady', 'CALL',
  'Glide framework calls onResourceReady when thumbnail loads successfully',
  evidence='SRC adapters/RecyclerAdapter.java:885-895 callback method')

# ---- part repair_rp17 (2024-10-28)
# Repair batch 17 - AmazeFileManager method labeling
# Generated: 2025-01-XX 21:26
# Methods: RecyclerAdapter$2 callbacks, Parcelables, Services, Database handlers, etc.

# RecyclerAdapter$2 - Glide RequestListener callbacks (2nd instance lines 920-943)
# SRC RecyclerAdapter.java:920-943:
# view.setVisibility(View.INVISIBLE);
# RequestListener<Drawable> requestListener = new RequestListener<Drawable>() {
#     @Override
#     public boolean onLoadFailed(@Nullable GlideException e, Object model, Target target, boolean isFirstResource) {
#         iconBackground.setBackgroundColor(grey_color);
#         new Handler(msg -> {
#             GlideApp.with(mainFrag).load(R.drawable.ic_broken_image_white_24dp).into(viewHolder.genericIcon);
#             return false;
#         }).obtainMessage().sendToTarget();
#         errorListener.onImageProcessed(true);
#         return true;
#     }
#     @Override
#     public boolean onResourceReady(Drawable resource, Object model, Target<Drawable> target,
#                                    DataSource dataSource, boolean isFirstResource) {
#         viewHolder.genericIcon.setImageDrawable(null);
#         viewHolder.genericIcon.setVisibility(View.GONE);
#         view.setVisibility(View.VISIBLE);
#         iconBackground.setBackgroundColor(mainFrag.getResources().getColor(android.R.color.transparent));
#         errorListener.onImageProcessed(false);
#         return false;
#     }
# };

e('RecyclerAdapter.showRoundedThumbnail', 'RecyclerAdapter$2.<init>', 'CALL',
  'RecyclerAdapter creates RequestListener for rounded thumbnail image loading',
  evidence='SRC RecyclerAdapter.java:922 RequestListener<Drawable> requestListener = new RequestListener<Drawable>()')

e('RecyclerAdapter$2.<init>', 'RecyclerAdapter$2.onLoadFailed', 'FRAMEWORK',
  'Glide framework calls onLoadFailed when image loading fails',
  evidence='INFERRED Glide RequestListener<Drawable> interface; framework invokes callback')

e('RecyclerAdapter$2.<init>', 'RecyclerAdapter$2.onResourceReady', 'FRAMEWORK',
  'Glide framework calls onResourceReady when image loads successfully',
  evidence='INFERRED Glide RequestListener<Drawable> interface; framework invokes callback')

e('RecyclerAdapter$2.onLoadFailed', 'RecyclerAdapter$2.lambda$onLoadFailed$0', 'CALL',
  'onLoadFailed creates Handler lambda for UI thread update',
  evidence='SRC RecyclerAdapter.java:925 new Handler(msg -> { GlideApp.with(mainFrag).load(...).into(viewHolder.genericIcon); return false; })')

# AppDataParcelable Parcelable methods
# SRC AppDataParcelable.java:26-32:
# @Override
# public int describeContents() {
#     return 0;
# }
# @Override
# public void writeToParcel(Parcel parcel, int i) {
#     parcel.writeString(label);



# IconDataParcelable.setImageBroken
# SRC IconDataParcelable.java:43-45:
# public void setImageBroken(boolean imageBroken) {
#     isImageBroken = imageBroken;
# }
UNREACHABLE['IconDataParcelable.setImageBroken'] = ('no_trigger_in_app', 'Setter never called; isImageBroken checked via getter but never set from app code', 'GREP no setImageBroken calls in app src', 'INFERRED')

# PemToKeyPairTask$1 - anonymous PasswordFinder
# SRC PemToKeyPairTask.java:169-178:
# this.passwordFinder = new PasswordFinder() {
#     @Override
#     public char[] reqPassword(Resource<?> resource) {
#         return textfield.getText().toString().toCharArray();
#     }
#     @Override
#     public boolean shouldRetry(Resource<?> resource) {
#         return false;
#     }
# };

e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask$1.<init>', 'CALL',
  'PemToKeyPairTask creates PasswordFinder when encrypted key needs passphrase',
  evidence='SRC PemToKeyPairTask.java:169 this.passwordFinder = new PasswordFinder() { ... }')

e('PemToKeyPairTask$1.<init>', 'PemToKeyPairTask$1.reqPassword', 'FRAMEWORK',
  'SSHJ library calls reqPassword to request passphrase for encrypted private key',
  evidence='INFERRED net.schmizz.sshj.userauth.password.PasswordFinder interface contract')

e('PemToKeyPairTask$1.<init>', 'PemToKeyPairTask$1.shouldRetry', 'FRAMEWORK',
  'SSHJ library calls shouldRetry after password authentication failure',
  evidence='INFERRED net.schmizz.sshj.userauth.password.PasswordFinder interface contract')

# ZipService lifecycle methods
# SRC ZipService.java:313-315:
# public IBinder onBind(Intent arg0) {
#     return mBinder;
# }
# SRC ProcessViewerFragment.java:165:
# getActivity().bindService(intent2, mCompressConnection, 0);

e('ProcessViewerFragment$CustomServiceConnection$1.refresh', 'ZipService.onBind', 'LIFECYCLE',
  'ProcessViewerFragment binds to ZipService to monitor compression progress',
  evidence='SRC ProcessViewerFragment.java:165 getActivity().bindService(intent2, mCompressConnection, 0)')

# SRC ZipService.java:318-320:
# @Override
# public void onDestroy() {
#     this.unregisterReceiver(receiver1);
# }

e('ZipService.onBind', 'ZipService.onDestroy', 'LIFECYCLE',
  'Framework calls onDestroy when service is destroyed',
  evidence='SRC ZipService.java:318-320 cleanup unregisterReceiver')

# SRC ZipService.java:184-186:
# public void setProgressListener(ProgressListener progressListener) {
#     this.progressListener = progressListener;
# }
# SRC ProcessViewerFragment.java:416:
# specificService.setProgressListener(new AbstractProgressiveService.ProgressListener() { ... })

e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'ZipService.setProgressListener', 'CALL',
  'ProcessViewerFragment sets progress listener to monitor zip operation',
  evidence='SRC ProcessViewerFragment.java:416 specificService.setProgressListener(new AbstractProgressiveService.ProgressListener())')

# SortHandler - SQLiteOpenHelper
# SRC SortHandler.java:47-51:
# @Override
# public void onCreate(SQLiteDatabase db) {
#     String CREATE_TABLE_SORT = "CREATE TABLE " + TABLE_SORT + "(" + COLUMN_SORT_PATH + " TEXT PRIMARY KEY," + COLUMN_SORT_TYPE + " INTEGER" + ")";
#     db.execSQL(CREATE_TABLE_SORT);
# }

e('SortHandler.<init>', 'SortHandler.onCreate', 'LIFECYCLE',
  'SQLiteOpenHelper.onCreate called by framework when database is created first time',
  evidence='SRC SortHandler.java:47-51 CREATE TABLE sort')

e('SortHandler.<init>', 'SortHandler.onUpgrade', 'LIFECYCLE',
  'SQLiteOpenHelper.onUpgrade called by framework when database version changes',
  evidence='SRC SortHandler.java:54-56 just calls onCreate(db)')

# SRC SortHandler.java:109-131:
# public List<Sort> getAllEntries() {
#     List<Sort> entryList = new ArrayList<>();
#     String query = "Select * FROM " + TABLE_SORT;
#     SQLiteDatabase sqLiteDatabase = getReadableDatabase();
# SRC GeneralDialogCreation.java:1038:
# SortHandler sortHandler = new SortHandler(m.getContext());


# TabHandler - SQLiteOpenHelper
# SRC TabHandler.java:57-81:
# @Override
# public void onCreate(SQLiteDatabase db) {
#     String CREATE_TAB_TABLE = "CREATE TABLE IF NOT EXISTS " + TABLE_TAB + "(" + COLUMN_TAB_NO + " INTEGER PRIMARY KEY," + COLUMN_PATH + " TEXT," + COLUMN_HOME + " TEXT" + ")";
#     db.execSQL(CREATE_TAB_TABLE);

e('TabHandler.<init>', 'TabHandler.onCreate', 'LIFECYCLE',
  'SQLiteOpenHelper.onCreate called by framework when database is created',
  evidence='SRC TabHandler.java:57-81 CREATE TABLE tab, encrypted, cloud, sort')

e('TabHandler.<init>', 'TabHandler.onUpgrade', 'LIFECYCLE',
  'SQLiteOpenHelper.onUpgrade called by framework on database version change',
  evidence='SRC TabHandler.java:84-86 just calls onCreate(sqLiteDatabase)')

e('TabHandler.<init>', 'TabHandler.onDowngrade', 'LIFECYCLE',
  'SQLiteOpenHelper.onDowngrade called by framework on database downgrade',
  evidence='SRC TabHandler.java:89-91 calls onUpgrade(db, oldVersion, newVersion)')

# StreamNotFoundException constructors
# SRC StreamNotFoundException.java:9-14:
# public StreamNotFoundException() { super(MESSAGE); }
# public StreamNotFoundException(String message) { super(message); }
# public StreamNotFoundException(String message, Throwable cause) { super(message, cause); }
# public StreamNotFoundException(Throwable cause) { super(MESSAGE, cause); }

UNREACHABLE['StreamNotFoundException.<init>(String)'] = ('no_trigger_in_app', 'Constructor overload not used; app throws StreamNotFoundException() or StreamNotFoundException(Throwable)', 'SRC WriteFileAbstraction.java:65,88 throw new StreamNotFoundException(); StreamNotFoundException(e); String-only version unused', 'SOURCE')

UNREACHABLE['StreamNotFoundException.<init>(String,Throwable)'] = ('no_trigger_in_app', 'Constructor overload not used; app uses parameterless and Throwable-only versions', 'SRC StreamNotFoundException.java:11 defined but no callers in app', 'SOURCE')


# HybridFile overloaded methods
# SRC HybridFile.java:376-399:
# public String getParent() { ... }
# public String getParent(Context context) { ... }


UNREACHABLE['HybridFile.length()'] = ('no_trigger_in_app', 'Parameterless overload not used; app calls length(Context)', 'SRC HybridFile.java:220,252 both overloads exist; Context version is standard in app', 'INFERRED')

# Operations utility class
# SRC Operations.java:30:
# public class Operations {


# SRC Operations.java:491:
# private static int checkFolder(final File folder, Context context) {


# SRC Operations.java:549:
# private static boolean isFileSystemFAT(String mountPoint) {

UNREACHABLE['Operations.isFileSystemFAT'] = ('no_trigger_in_app', 'Private static helper method called only within Operations class', 'SRC Operations.java:549 private static boolean isFileSystemFAT', 'SOURCE')

# From repair_rp29: OperationData.toString
UNREACHABLE['OperationData.toString'] = (
    'no_trigger_in_app',
    'OperationData.toString is an Object override; app code only constructs OperationData and passes it to UtilsHandler, and no call site of toString is found',
    'SRC OperationData.java:75-86 defines toString()',
    'INFERRED'
)

# PasteHelper Parcelable methods
# SRC PasteHelper.java:21-24:
# private PasteHelper(Parcel in) {
#     operation = in.readInt();
#     paths = (HybridFileParcelable[]) in.readParcelableArray(HybridFileParcelable.class.getClassLoader());
# }
# SRC PasteHelper.java:37-39:
# public PasteHelper createFromParcel(Parcel in) {
#     return new PasteHelper(in);
# }

e('PasteHelper$1.createFromParcel', 'PasteHelper.<init>(Parcel)', 'CALL',
  'Parcel CREATOR.createFromParcel constructs PasteHelper from Parcel',
  evidence='SRC PasteHelper.java:38 return new PasteHelper(in)')



# ---- part repair_rp18 (2024-10-28)
# Repair batch 18: routes and unreachable labels
# Generated for AmazeFileManager schema-2 graph

# ========== SevenZFile$2 ==========

# SevenZFile$2 is an anonymous InputStreamStatistics implementation returned by getStatisticsForCurrentEntry()
# SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1116-1125





# ========== SevenZMethodConfiguration ==========

# SevenZMethodConfiguration is a library class used to configure 7z compression methods
# SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZMethodConfiguration.java

e('SevenZArchiveEntry.setContentMethods', 'SevenZMethodConfiguration.<init>(SevenZMethod)', 'CALL',
  'new SevenZMethodConfiguration(method)',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZMethodConfiguration.java:47-49; used in 7z compression')




# ========== CustomSshJConfig ==========

# CustomSshJConfig already has constructor route in graph_def.py:2744,2748
# SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/CustomSshJConfig.java

e('CustomSshJConfig.<init>', 'CustomSshJConfig.initSignatureFactories', 'CALL',
  'DefaultConfig parent constructor calls initSignatureFactories()',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/CustomSshJConfig.java:53-55; override method')

e('CustomSshJConfig.<init>', 'CustomSshJConfig.initRandomFactory', 'CALL',
  'DefaultConfig parent constructor calls initRandomFactory(boolean)',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/CustomSshJConfig.java:57-60; override method')


# ========== SshConnectionPool$AsyncRemoveConnection ==========

# AsyncRemoveConnection is a private inner AsyncTask class for removing SSH connections
# SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/SshConnectionPool.java:280-307

e('SshConnectionPool.removeConnection', 'SshConnectionPool$AsyncRemoveConnection.<init>', 'CALL',
  'new AsyncRemoveConnection(url, callback)',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/SshConnectionPool.java:98')


e('SshConnectionPool$AsyncRemoveConnection.doInBackground', 'SshConnectionPool$AsyncRemoveConnection.onPostExecute', 'CALL',
  'Framework calls onPostExecute after doInBackground completes',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/SshConnectionPool.java:304-307')


# ========== Statvfs$Response ==========

# Statvfs$Response wraps SSH statvfs@openssh.com response data
# SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/Statvfs.java:77-224





# ========== MainFragment$4$1 ==========

# MainFragment$4$1 is the MediaScannerConnectionClient anonymous class in MainFragment$4 receiver
# SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:798-814

e('MainFragment$4.onReceive', 'MainFragment$4$1.<init>', 'CALL',
  'Anonymous MediaScannerConnectionClient created',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:798')




# ========== MainFragment$6 ==========

# MainFragment$6 is an anonymous AsyncTask for sorting search results
# SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1640-1653

e('MainFragment.addSearchResult', 'MainFragment$6.<init>', 'CALL',
  'Anonymous AsyncTask created to sort LIST_ELEMENTS',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1640')


e('MainFragment$6.doInBackground', 'MainFragment$6.onPostExecute', 'CALL',
  'Framework calls onPostExecute after sorting completes',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1647-1651')


# ========== ProcessViewerFragment$CustomServiceConnection ==========

# CustomServiceConnection is a private static inner class implementing ServiceConnection
# SRC app/src/main/java/com/amaze/filemanager/fragments/ProcessViewerFragment.java:390-437

e('ProcessViewerFragment.onCreateView', 'ProcessViewerFragment$CustomServiceConnection.<init>', 'CALL',
  'new CustomServiceConnection(this, mLineChart, SERVICE_*)',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/ProcessViewerFragment.java:127-131')

# ProcessViewerFragment.onResume blocker resolution
e('ProcessViewerFragment.onResume', 'ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'FRAMEWORK',
  'onResume binds 5 services; framework calls onServiceConnected when binding succeeds',
  evidence='INFERRED ProcessViewerFragment.java:159-171: onResume calls bindService 5 times with mCopyConnection, mExtractConnection, mCompressConnection, mEncryptConnection, mDecryptConnection; framework calls onServiceConnected when binding succeeds', env=ENV_BIND)




# ========== PropertiesSheet ==========

# PropertiesSheet is a BottomSheetDialogFragment for displaying file properties
# SRC app/src/main/java/com/amaze/filemanager/fragments/PropertiesSheet.java





# ========== PropertiesSheet$2 ==========

# PropertiesSheet$2 is the BottomSheetCallback field mCallback
# SRC app/src/main/java/com/amaze/filemanager/fragments/PropertiesSheet.java:117-129





# ========== SearchWorkerFragment ==========

# SearchWorkerFragment already has routes in graph_def.py for onAttach (line 1295)
# SRC app/src/main/java/com/amaze/filemanager/fragments/SearchWorkerFragment.java

e('MainActivityHelper.search', 'SearchWorkerFragment.onAttach', 'CALL',
  'Framework lifecycle method when fragment attaches to activity',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/SearchWorkerFragment.java:40-44')

e('SearchWorkerFragment.onAttach', 'SearchWorkerFragment.onCreate', 'CALL',
  'Framework lifecycle method after onAttach',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/SearchWorkerFragment.java:46-62')

e('MainActivity.onDestroy', 'SearchWorkerFragment.onDetach', 'CALL',
  'Framework lifecycle method when fragment detaches',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/SearchWorkerFragment.java:64-68')


# ========== TabFragment$ScreenSlidePagerAdapter ==========

# ScreenSlidePagerAdapter is a private inner FragmentStatePagerAdapter
# SRC app/src/main/java/com/amaze/filemanager/fragments/TabFragment.java:319-347

e('TabFragment.onCreateView', 'TabFragment$ScreenSlidePagerAdapter.getCount', 'CALL',
  'Framework calls getCount() to determine number of pages',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/TabFragment.java:332-335')




# ========== UserColorPreferences ==========

# UserColorPreferences is a Parcelable data class for color preferences
# SRC app/src/main/java/com/amaze/filemanager/ui/colors/UserColorPreferences.java




# ---- part repair_rp19 (2024-10-28)
# Repair batch 19 - AmazeFileManager
# Methods already labeled in graph_def.py are documented but not re-emitted

e('WarnableTextInputValidator.<init>', 'WarnableTextInputValidator.onFocusChange', 'LIFECYCLE',
  'EditText.setOnFocusChangeListener registers this callback',
  evidence='SRC WarnableTextInputValidator.java:27 mEditText.setOnFocusChangeListener(this) in constructor')


e('WarnableTextInputValidator.onFocusChange', 'WarnableTextInputValidator.performClick', 'CALL',
  'onFocusChange calls performClick indirectly through doValidate button enable check',
  evidence='SRC WarnableTextInputValidator.java:43 doValidate(false) called; button state affects touch handling')

e('WarnableTextInputValidator.<init>', 'WarnableTextInputValidator.onTouch', 'LIFECYCLE',
  'View.setOnTouchListener registers this callback',
  evidence='SRC WarnableTextInputValidator.java:31 mButton.setOnTouchListener(this) in constructor')


e('WarnableTextInputValidator.onTouch', 'WarnableTextInputValidator.performClick', 'CALL',
  'onTouch calls performClick to validate and potentially block touch',
  evidence='SRC WarnableTextInputValidator.java:49 return performClick()')

e('SearchView.<init>', 'SearchView.lambda$new$0', 'CALL',
  'Lambda captured in clearImageView.setOnClickListener',
  evidence='SRC SearchView.java:49 clearImageView.setOnClickListener(v -> searchViewEditText.setText(""))')



e('SearchView.<init>', 'SearchView.lambda$new$1', 'CALL',
  'Lambda captured in backImageView.setOnClickListener',
  evidence='SRC SearchView.java:51 backImageView.setOnClickListener(v -> appbar.getSearchView().hideSearchView())')


e('SearchView.lambda$new$1', 'SearchView.hideSearchView', 'CALL',
  'Lambda body hides search view',
  evidence='SRC SearchView.java:51 appbar.getSearchView().hideSearchView()')

e('SearchView.<init>', 'SearchView.lambda$new$2', 'CALL',
  'Lambda captured in searchViewEditText.setOnEditorActionListener',
  evidence='SRC SearchView.java:53-58 searchViewEditText.setOnEditorActionListener((v, actionId, event) -> { ... })')


e('SearchView.lambda$new$2', 'SearchView.hideSearchView', 'CALL',
  'Lambda body hides search view after search',
  evidence='SRC SearchView.java:55 appbar.getSearchView().hideSearchView()')


# ---- part repair_rp20 (2024-10-28)
# Repair batch 20 - AmazeFileManager method routes


UNREACHABLE['SimpleTextWatcher.beforeTextChanged'] = ('framework_never_calls', 
  'Empty implementation; no subclass overrides this method', 
  'SRC utils/SimpleTextWatcher.java:13-16', 'SOURCE')

UNREACHABLE['SimpleTextWatcher.onTextChanged'] = ('framework_never_calls', 
  'Empty implementation; no subclass overrides this method', 
  'SRC utils/SimpleTextWatcher.java:18-21', 'SOURCE')

e('FileUtils.openFile(File,MainActivity,SharedPreferences)', 'FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences)', 'CALL',
  'openFile(File...) calls openunknown which has a DocumentFile overload path',
  evidence='SRC utils/files/FileUtils.java:816-823')

e('FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences)', 'FileUtils.openunknown(DocumentFile,Context,boolean,boolean)', 'CALL',
  'openFile calls openunknown with DocumentFile',
  evidence='SRC utils/files/FileUtils.java:819,822')

e('Operations$3.onPostExecute', 'FileUtils.scanFile(Context,HybridFile[])', 'CALL',
  'Operations rename task scans files after rename',
  evidence='SRC filesystem/Operations.java:491-493')

e('ShareAdapter.onCreateViewHolder', 'ShareAdapter$ViewHolder.<init>', 'CALL',
  'RecyclerView adapter creates ViewHolder',
  evidence='SRC utils/share/ShareAdapter.java:44-46')

e('ShareAdapter.onBindViewHolder', 'ShareAdapter$ViewHolder.render', 'CALL',
  'RecyclerView adapter binds ViewHolder',
  evidence='SRC utils/share/ShareAdapter.java:50-52')

e('ShareAdapter$ViewHolder.render', 'ShareAdapter$ViewHolder.lambda$render$0', 'CALL',
  'Lambda for OnClickListener in render',
  evidence='SRC utils/share/ShareAdapter.java:72-76')

e('FileUtils.shareFiles', 'ShareTask.doInBackground', 'FRAMEWORK',
  'AsyncTask.execute triggers doInBackground',
  evidence='SRC utils/files/FileUtils.java:373; FW-SRC android/os/AsyncTask.java')

e('ShareTask.doInBackground', 'ShareTask.appInstalledOrNot', 'CALL',
  'doInBackground checks if bluetooth app is installed',
  evidence='SRC utils/share/ShareTask.java:98')

e('ShareTask.doInBackground', 'ShareTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='FW-SRC android/os/AsyncTask.java')

UNREACHABLE['RandomAccessStream.available'] = ('framework_never_calls',
  'Method throws IOException to prevent calls; javadoc says "Use availableExact()"',
  'SRC utils/streams/RandomAccessStream.java:46-48',
  'SOURCE')

e('RandomAccessStream.<init>', 'RandomAccessStream.markSupported', 'CALL',
  'Constructor calls mark which checks markSupported',
  evidence='SRC utils/streams/RandomAccessStream.java:13,24-31')


e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.onBackPressed', 'CALL',
  'Toolbar back button triggers onBackPressed',
  evidence='SRC activities/DatabaseViewerActivity.java:206-211')

e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.onOptionsItemSelected', 'FRAMEWORK',
  'Framework delivers menu item selection',
  evidence='SRC activities/DatabaseViewerActivity.java:206-212')

e('TextEditorActivity.onTextChanged', 'TextEditorActivity$1.<init>', 'CALL',
  'TextWatcher schedules Timer with anonymous TimerTask',
  evidence='SRC activities/TextEditorActivity.java:430-437')

e('TextEditorActivity$1.<init>', 'TextEditorActivity$1.run', 'FRAMEWORK',
  'Timer framework calls TimerTask.run',
  evidence='FW-SRC java/util/Timer.java')

e('TextEditorActivity.revealSearchView', 'TextEditorActivity$2.<init>', 'CALL',
  'Reveal animation listener',
  evidence='SRC activities/TextEditorActivity.java:481-488')

e('TextEditorActivity$2.<init>', 'TextEditorActivity$2.onAnimationEnd', 'FRAMEWORK',
  'Animation framework calls onAnimationEnd',
  evidence='FW-SRC android/animation/AnimatorListenerAdapter.java')

e('TextEditorActivity.hideSearchView', 'TextEditorActivity$3.<init>', 'CALL',
  'Hide animation listener',
  evidence='SRC activities/TextEditorActivity.java:518-526')

e('TextEditorActivity$3.<init>', 'TextEditorActivity$3.onAnimationEnd', 'FRAMEWORK',
  'Animation framework calls onAnimationEnd',
  evidence='FW-SRC android/animation/AnimatorListenerAdapter.java')


UNREACHABLE['AppDataParcelable$1.newArray'] = ('framework_never_calls',
  'Parcelable.Creator.newArray rarely called; app uses createFromParcel only',
  'SRC adapters/data/AppDataParcelable.java:63-66',
  'INFERRED')

e('RecyclerPreloadSizeProvider.<init>', 'RecyclerPreloadSizeProvider.getPreloadSize', 'CALL',
  'Glide ListPreloader calls getPreloadSize',
  evidence='SRC adapters/glide/RecyclerPreloadSizeProvider.java:56-59')

e('RecyclerPreloadSizeProvider.addView', 'RecyclerPreloadSizeProvider.lambda$addView$0', 'CALL',
  'Lambda creates SizeViewTarget callback',
  evidence='SRC adapters/glide/RecyclerPreloadSizeProvider.java:43')

e('CryptHandler.<init>', 'CryptHandler.onCreate', 'FRAMEWORK',
  'SQLiteOpenHelper framework calls onCreate',
  evidence='SRC database/CryptHandler.java:37-42; FW-SRC android/database/sqlite/SQLiteOpenHelper.java')

e('CryptHandler.<init>', 'CryptHandler.onUpgrade', 'FRAMEWORK',
  'SQLiteOpenHelper framework calls onUpgrade',
  evidence='SRC database/CryptHandler.java:45-49; FW-SRC android/database/sqlite/SQLiteOpenHelper.java')


e('CustomFileObserver.<init>', 'CustomFileObserver.onEvent', 'FRAMEWORK',
  'FileObserver framework calls onEvent on filesystem changes',
  evidence='SRC filesystem/CustomFileObserver.java:84-126; FW-SRC android/os/FileObserver.java')

e('CustomFileObserver.onEvent', 'CustomFileObserver$1.<init>', 'CALL',
  'onEvent schedules timer with anonymous TimerTask',
  evidence='SRC filesystem/CustomFileObserver.java:117-125')

e('CustomFileObserver$1.<init>', 'CustomFileObserver$1.run', 'FRAMEWORK',
  'Timer framework calls TimerTask.run',
  evidence='FW-SRC java/util/Timer.java')

e('CustomFileObserver$1.run', 'CustomFileObserver.sendMessages', 'CALL',
  'TimerTask run calls sendMessages',
  evidence='SRC filesystem/CustomFileObserver.java:121')

e('CustomFileObserver.onEvent', 'CustomFileObserver.sendMessages', 'CALL',
  'onEvent calls sendMessages',
  evidence='SRC filesystem/CustomFileObserver.java:126')

e('CustomFileObserver$FileTimerTask.<init>', 'CustomFileObserver$FileTimerTask.run', 'FRAMEWORK',
  'ScheduledExecutorService calls Runnable.run',
  evidence='FW-SRC java/util/concurrent/ScheduledExecutorService.java')

e('CustomFileObserver$FileTimerTask.run', 'CustomFileObserver$FileTimerTask.compare', 'CALL',
  'run calls compare to detect file changes',
  evidence='SRC filesystem/CustomFileObserver.java:191-197')

e('Operations.rename', 'Operations$3.<init>', 'CALL',
  'rename creates anonymous AsyncTask',
  evidence='SRC filesystem/Operations.java:335-488')

e('Operations$3.<init>', 'Operations$3.doInBackground', 'FRAMEWORK',
  'AsyncTask.execute triggers doInBackground',
  evidence='FW-SRC android/os/AsyncTask.java')

e('Operations$3.doInBackground', 'Operations$3.onPostExecute', 'FRAMEWORK',
  'AsyncTask calls onPostExecute',
  evidence='SRC filesystem/Operations.java:486-493; FW-SRC android/os/AsyncTask.java')

# ---- part repair_rp21 (2024-10-28)
# Repair part 21: labels for batch rp_21

# PasteHelper$1 - Parcelable.Creator - MOVED TO UNREACHABLE (blocker_props_1.md)
# PasteHelper.CREATOR is never invoked; no getParcelableExtra or readParcelable calls for this type in the app

# CoderBase, DeltaDecoder, LZMA2Decoder - Apache Commons Compress sevenz library classes
UNREACHABLE['CoderBase.encode'] = ('framework_never_calls', 'Apache Commons Compress library class CoderBase (sevenz codec); grep found no app references to CoderBase', 'INFERRED', 'INFERRED')
UNREACHABLE['CoderBase.getOptionsAsProperties'] = ('framework_never_calls', 'Apache Commons Compress library class CoderBase (sevenz codec); grep found no app references to CoderBase', 'INFERRED', 'INFERRED')
UNREACHABLE['DeltaDecoder.encode'] = ('framework_never_calls', 'Apache Commons Compress library class DeltaDecoder (sevenz codec); grep found no app references to DeltaDecoder', 'INFERRED', 'INFERRED')
UNREACHABLE['DeltaDecoder.getOptionsAsProperties'] = ('framework_never_calls', 'Apache Commons Compress library class DeltaDecoder (sevenz codec); grep found no app references to DeltaDecoder', 'INFERRED', 'INFERRED')
UNREACHABLE['LZMA2Decoder.encode'] = ('framework_never_calls', 'Apache Commons Compress library class LZMA2Decoder (sevenz codec); grep found no app references to LZMA2Decoder', 'INFERRED', 'INFERRED')
UNREACHABLE['LZMA2Decoder.getOptions'] = ('framework_never_calls', 'Apache Commons Compress library class LZMA2Decoder (sevenz codec); grep found no app references to LZMA2Decoder', 'INFERRED', 'INFERRED')

# MainFragment$7 - anonymous Thread created in launchSMB
e('MainFragment.launchSMB', 'MainFragment$7.<init>', 'CALL',
  'launchSMB creates anonymous Thread',
  evidence='SRC MainFragment.java:1658')
e('MainFragment.launchSMB', 'MainFragment$7.run', 'ASYNC',
  'Thread.run override; called by framework when thread starts',
  evidence='SRC MainFragment.java:1658-1677; FW-SRC Thread.java:764')
e('MainFragment$7.run', 'MainFragment$7.lambda$run$0', 'ASYNC',
  'Lambda called from runOnUiThread inside Thread.run',
  evidence='SRC MainFragment.java:1670')

# ProcessViewerFragment$CustomServiceConnection$1 - anonymous ProgressListener
e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'ProcessViewerFragment$CustomServiceConnection$1.<init>', 'CALL',
  'onServiceConnected creates anonymous ProgressListener',
  evidence='SRC ProcessViewerFragment.java:413-424')
e('ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0', 'ProcessViewerFragment.processResults', 'CALL',
  'Lambda calls processResults with dataPackage',
  evidence='SRC ProcessViewerFragment.java:421')
e('AbstractProgressiveService.addDatapoint', 'ProcessViewerFragment$CustomServiceConnection$1.onUpdate', 'CALL',
  'AbstractProgressiveService calls ProgressListener.onUpdate when progress changes',
  evidence='INFERRED INFERRED')
e('ProcessViewerFragment$CustomServiceConnection$1.onUpdate', 'ProcessViewerFragment$CustomServiceConnection$1.lambda$onUpdate$0', 'ASYNC',
  'Lambda for runOnUiThread inside onUpdate',
  evidence='SRC ProcessViewerFragment.java:421')

# PropertiesSheet$1 - anonymous OnScrollChangeListener

# ColorPref$1 - anonymous MaterialDialog.ButtonCallback
e('ColorPref.colorChangeDialog', 'ColorPref$1.<init>', 'CALL',
  'colorChangeDialog creates anonymous ButtonCallback',
  evidence='SRC ColorPref.java:177-184')

# QuickAccessPref.onCreate and QuickAccessPref.onPreferenceClick
e('PreferencesActivity.selectItem', 'QuickAccessPref.onCreate', 'LIFECYCLE',
  'PreferenceFragment lifecycle method',
  evidence='SRC QuickAccessPref.java:40-53; FW-SRC PreferenceFragment')
e('S_PREFS', 'QuickAccessPref.onPreferenceClick', 'GUI',
  'Preference click listener; registered at line 51',
  evidence='SRC QuickAccessPref.java:56-60, 51; FW-SRC Preference.java')

# UserColorPreferences$1 - Parcelable.Creator - MOVED TO UNREACHABLE (blocker_props_1.md)
# UserColorPreferences.CREATOR is never invoked; instances created only via constructor, never deserialized

# RenameBookmark$1 and RenameBookmark$2 - anonymous SimpleTextWatcher instances
e('RenameBookmark.onCreateDialog', 'RenameBookmark$1.<init>', 'CALL',
  'onCreateDialog creates anonymous SimpleTextWatcher',
  evidence='SRC RenameBookmark.java:63-69')
e('RenameBookmark$1.<init>', 'SimpleTextWatcher.<init>', 'CALL',
  'Anonymous class extends SimpleTextWatcher',
  evidence='SRC RenameBookmark.java:63')
e('S_DIALOG', 'RenameBookmark$1.afterTextChanged', 'GUI',
  'TextWatcher callback; dispatched by EditText',
  evidence='SRC RenameBookmark.java:65-69; FW-SRC TextView.java')
e('RenameBookmark.onCreateDialog', 'RenameBookmark$2.<init>', 'CALL',
  'onCreateDialog creates anonymous SimpleTextWatcher',
  evidence='SRC RenameBookmark.java:85-90')
e('RenameBookmark$2.<init>', 'SimpleTextWatcher.<init>', 'CALL',
  'Anonymous class extends SimpleTextWatcher',
  evidence='SRC RenameBookmark.java:85')
e('S_DIALOG', 'RenameBookmark$2.afterTextChanged', 'GUI',
  'TextWatcher callback; dispatched by EditText',
  evidence='SRC RenameBookmark.java:87-90; FW-SRC TextView.java')

# SftpConnectDialog$1 - anonymous SimpleTextWatcher (validator)
e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog$1.<init>', 'CALL',
  'onCreateDialog creates validator SimpleTextWatcher',
  evidence='SRC SftpConnectDialog.java:246-265')
e('SftpConnectDialog$1.<init>', 'SimpleTextWatcher.<init>', 'CALL',
  'Anonymous class extends SimpleTextWatcher',
  evidence='SRC SftpConnectDialog.java:246')
e('S_DIALOG', 'SftpConnectDialog$1.afterTextChanged', 'GUI',
  'TextWatcher callback; registered at lines 267-270',
  evidence='SRC SftpConnectDialog.java:248-265; FW-SRC TextView.java')

# SmbConnectDialog$1, $2, $3, $4 - anonymous SimpleTextWatcher instances
e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$1.<init>', 'CALL',
  'onCreateDialog creates anonymous SimpleTextWatcher',
  evidence='SRC SmbConnectDialog.java:70-77')
e('SmbConnectDialog$1.<init>', 'SimpleTextWatcher.<init>', 'CALL',
  'Anonymous class extends SimpleTextWatcher',
  evidence='SRC SmbConnectDialog.java:70')
e('S_DIALOG', 'SmbConnectDialog$1.afterTextChanged', 'GUI',
  'TextWatcher callback; dispatched by EditText',
  evidence='SRC SmbConnectDialog.java:72-77; FW-SRC TextView.java')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$2.<init>', 'CALL',
  'onCreateDialog creates anonymous SimpleTextWatcher',
  evidence='SRC SmbConnectDialog.java:79-86')
e('SmbConnectDialog$2.<init>', 'SimpleTextWatcher.<init>', 'CALL',
  'Anonymous class extends SimpleTextWatcher',
  evidence='SRC SmbConnectDialog.java:79')
e('S_DIALOG', 'SmbConnectDialog$2.afterTextChanged', 'GUI',
  'TextWatcher callback; dispatched by EditText',
  evidence='SRC SmbConnectDialog.java:81-86; FW-SRC TextView.java')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$3.<init>', 'CALL',
  'onCreateDialog creates anonymous SimpleTextWatcher',
  evidence='SRC SmbConnectDialog.java:88-95')
e('SmbConnectDialog$3.<init>', 'SimpleTextWatcher.<init>', 'CALL',
  'Anonymous class extends SimpleTextWatcher',
  evidence='SRC SmbConnectDialog.java:88')
e('S_DIALOG', 'SmbConnectDialog$3.afterTextChanged', 'GUI',
  'TextWatcher callback; dispatched by EditText',
  evidence='SRC SmbConnectDialog.java:90-95; FW-SRC TextView.java')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$4.<init>', 'CALL',
  'onCreateDialog creates anonymous SimpleTextWatcher',
  evidence='SRC SmbConnectDialog.java:97-104')
e('SmbConnectDialog$4.<init>', 'SimpleTextWatcher.<init>', 'CALL',
  'Anonymous class extends SimpleTextWatcher',
  evidence='SRC SmbConnectDialog.java:97')
e('S_DIALOG', 'SmbConnectDialog$4.afterTextChanged', 'GUI',
  'TextWatcher callback; dispatched by EditText',
  evidence='SRC SmbConnectDialog.java:99-104; FW-SRC TextView.java')

# MimeTypes.<init> and MimeTypes.mimeTypeMatch
e('MimeTypes.getMimeType', 'MimeTypes.<init>', 'CALL',
  'Constructor called when static methods accessed',
  evidence='SRC MimeTypes.java:117-133')
e('MimeTypes.getMimeType', 'MimeTypes.mimeTypeMatch', 'CALL',
  'Public static method called from app code',
  evidence='SRC MimeTypes.java:136-138')

# Indicator$PendingRetreatAnimator.lambda$new$0 and lambda$new$1
e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRetreatAnimator.lambda$new$0', 'FRAMEWORK',
  'Lambda for ValueAnimator update listener (rightward retreat)',
  evidence='SRC Indicator.java:728-734')
e('Indicator$PendingRetreatAnimator.<init>', 'Indicator$PendingRetreatAnimator.lambda$new$1', 'FRAMEWORK',
  'Lambda for ValueAnimator update listener (leftward retreat)',
  evidence='SRC Indicator.java:746-752')

# DatapointParcelable$1 - Parcelable.Creator

# ---- part repair_rp22 (2024-10-28)
# Repair batch 22 for AmazeFileManager

# UNREACHABLE methods
UNREACHABLE['InterestingConfigChange.<init>'] = (
    'no_trigger_in_app',
    'InterestingConfigChange is a utility class with only static methods (isConfigChanged, recycle). No instance is ever created.',
    'SRC utils/InterestingConfigChange.java:17-41',
    'SOURCE'
)

UNREACHABLE['PreferenceUtils.<init>'] = (
    'no_trigger_in_app',
    'PreferenceUtils is a utility class with only static methods (getStatusColor). No instance is ever created.',
    'SRC utils/PreferenceUtils.java:9-33',
    'SOURCE'
)

UNREACHABLE['TinyDB.<init>'] = (
    'no_trigger_in_app',
    'TinyDB is a utility class with only static methods (putBooleanArray, getBooleanArray). No instance is ever created.',
    'SRC utils/TinyDB.java:27-67',
    'SOURCE'
)

UNREACHABLE['DummyFileGenerator.<init>'] = (
    'no_trigger_in_app',
    'DummyFileGenerator is a test utility class annotated @RestrictTo(RestrictTo.Scope.TESTS). Used only in test code.',
    'SRC utils/test/DummyFileGenerator.java:48-85',
    'SOURCE'
)



# REACHABLE methods (new routes)
e('MainActivity.initialisePreferences', 'PreferenceUtils.getStatusColor(String)', 'CALL',
  'MainActivity calls PreferenceUtils.getStatusColor to darken primary color for status bar',
  evidence='SRC activities/MainActivity.java:1415')

e('DatabaseViewerActivity.onCreate', 'PreferenceUtils.getStatusColor(String)', 'CALL',
  'DatabaseViewerActivity calls PreferenceUtils.getStatusColor for status bar color',
  evidence='SRC activities/DatabaseViewerActivity.java:122')

e('PreferencesActivity.onCreate', 'PreferenceUtils.getStatusColor(String)', 'CALL',
  'PreferencesActivity calls PreferenceUtils.getStatusColor for tab status color',
  evidence='SRC activities/PreferencesActivity.java:216')

e('TextEditorActivity.onCreate', 'PreferenceUtils.getStatusColor(String)', 'CALL',
  'TextEditorActivity calls PreferenceUtils.getStatusColor for status bar color',
  evidence='SRC activities/TextEditorActivity.java:182')


e('CloudStreamSource.open', 'CloudStreamSource.read()', 'CALL',
  'CloudStreamSource.read() reads single byte from underlying inputStream',
  evidence='SRC cloud/CloudStreamSource.java:61-65')

e('CloudStreamSource.open', 'CloudStreamSource.read(byte[],int,int)', 'CALL',
  'CloudStreamSource.read(byte[],int,int) reads bytes into buffer from underlying inputStream',
  evidence='SRC cloud/CloudStreamSource.java:68-72')

e('StreamServer$HTTPSession.sendResponse', 'CloudStreamSource.read(byte[],int,int)', 'CALL',
  'StreamServer reads from CloudStreamSource stream when sending HTTP response data',
  evidence='INFERRED StreamServer.java sendResponse reads from StreamSource; NanoHTTPD library source not fully read')

e('MoveFiles.onPostExecute', 'MoveFiles.lambda$onPostExecute$0', 'ASYNC',
  'MoveFiles.onPostExecute passes lambda to AppConfig.runInBackground to update encrypted entries',
  evidence='SRC asynchronous/asynctasks/MoveFiles.java:179-195')

e('AppConfig.runInBackground', 'MoveFiles.lambda$onPostExecute$0', 'ASYNC',
  'AppConfig.runInBackground executes the lambda on background thread',
  evidence='INFERRED executor framework dispatches Runnable lambda body')

e('SevenZipHelperTask.onProgressUpdate', 'SevenZipHelperTask.lambda$onProgressUpdate$0', 'CALL',
  'onProgressUpdate creates password dialog with lambda callback for positive button',
  evidence='SRC asynchronous/asynctasks/compress/SevenZipHelperTask.java:105-113')


# ---- part repair_rp23 (2024-10-28)
# Repair batch 23 - Label additions for AmazeFileManager

# ZipService$1.onReceive
e('ZipService.onCreate', 'ZipService$1.<init>', 'CALL',
  'Anonymous BroadcastReceiver instantiated',
  evidence='SRC asynchronous/services/ZipService.java:305-310')
e('ZipService$1.<init>', 'ZipService$1.onReceive', 'FRAMEWORK',
  'BroadcastReceiver.onReceive called by framework',
  evidence='SRC asynchronous/services/ZipService.java:86, 307')

# HybridFile$9$1.close, HybridFile$11$1.close
e('HybridFile$9$1.<init>', 'HybridFile$9$1.close', 'CALL',
  'InputStream.close() called when stream closed',
  evidence='SRC filesystem/HybridFile.java:909-920')
e('HybridFile$11$1.<init>', 'HybridFile$11$1.close', 'CALL',
  'InputStream.close() called when stream closed',
  evidence='SRC filesystem/HybridFile.java:952-965')

# Operations$1.doInBackground
e('Operations.mkdir', 'Operations$1.<init>', 'CALL',
  'Anonymous AsyncTask instantiated',
  evidence='SRC filesystem/Operations.java:83')
e('Operations$1.<init>', 'Operations$1.doInBackground', 'ASYNC',
  'AsyncTask.doInBackground called by framework',
  evidence='SRC filesystem/Operations.java:88-194')

# Operations$2.doInBackground
e('Operations.mkfile', 'Operations$2.<init>', 'CALL',
  'Anonymous AsyncTask instantiated',
  evidence='SRC filesystem/Operations.java:197')
e('Operations$2.<init>', 'Operations$2.doInBackground', 'ASYNC',
  'AsyncTask.doInBackground called by framework',
  evidence='SRC filesystem/Operations.java:202-332')

# Operations$3$1.<init>
e('Operations.rename', 'Operations$3.<init>', 'CALL',
  'Anonymous AsyncTask instantiated',
  evidence='SRC filesystem/Operations.java:335')
e('Operations$3.<init>', 'Operations$3.doInBackground', 'ASYNC',
  'AsyncTask.doInBackground',
  evidence='SRC filesystem/Operations.java:341')
e('Operations$3.doInBackground', 'Operations$3$1.<init>', 'CALL',
  'Anonymous ErrorCallBack instantiated',
  evidence='SRC filesystem/Operations.java:369')

# Library classes without source
UNREACHABLE['NID.<init>'] = ('no_trigger_in_app', 'Apache Commons Compress library class; no app instantiation', 'class not in app source', 'INFERRED')
UNREACHABLE['SevenZMethod.getId'] = ('no_trigger_in_app', 'Apache Commons Compress library class method', 'class not in app source', 'INFERRED')
UNREACHABLE['StreamMap.toString'] = ('no_trigger_in_app', 'Apache Commons Compress library class toString', 'class not in app source', 'INFERRED')
UNREACHABLE['Statvfs.<init>'] = ('no_trigger_in_app', 'sshj library class constructor', 'class not in app source', 'INFERRED')

# Constants classes
UNREACHABLE['PreferencesConstants.<init>'] = ('no_trigger_in_app', 'Constants class never instantiated', 'SRC fragments/preference_fragments/PreferencesConstants.java:8', 'SOURCE')
UNREACHABLE['NotificationConstants.<init>'] = ('no_trigger_in_app', 'Constants class never instantiated', 'SRC ui/notifications/NotificationConstants.java:18', 'SOURCE')

# Utility class
UNREACHABLE['OTGUtil.<init>'] = ('no_trigger_in_app', 'Utility class with static methods only', 'SRC utils/OTGUtil.java', 'INFERRED')

# ---- part repair_rp24 (2024-10-28)
# Repair batch 24: 11 methods

# ServiceWatcherUtil$2.run
e('ServiceWatcherUtil.postWaiting', 'ServiceWatcherUtil$2.<init>', 'CALL',
  'postWaiting creates anonymous Runnable for waiting watcher thread',
  evidence='SRC ServiceWatcherUtil.java:201-223')
e('ServiceWatcherUtil$2.<init>', 'ServiceWatcherUtil$2.run', 'FRAMEWORK',
  'Handler.postDelayed calls Runnable.run on the handler thread',
  evidence='SRC ServiceWatcherUtil.java:224; INFERRED android.os.Handler posts Runnable to handler thread')

# StreamServer.lambda$new$0
e('StreamServer.<init>', 'StreamServer.lambda$new$0', 'ASYNC',
  'Constructor creates server thread with lambda that accepts socket connections',
  evidence='SRC StreamServer.java:255-266')

# SmbUtil.<init>
UNREACHABLE['SmbUtil.<init>'] = ('no_trigger_in_app',
  'Utility class with only static methods; constructor never instantiated in app source',
  'SRC SmbUtil.java:17 (class with only static methods getSmbDecryptedPath and getSmbEncryptedPath); GREP no "new SmbUtil" in app source',
  'SOURCE')

# PackageReceiver.onReceive
e('AppListLoader.onStartLoading', 'PackageReceiver.<init>', 'CALL',
  'AppListLoader creates PackageReceiver and registers it for package broadcasts',
  evidence='SRC AppListLoader.java:120')
e('PackageReceiver.<init>', 'PackageReceiver.onReceive', 'FRAMEWORK',
  'BroadcastReceiver receives ACTION_PACKAGE_ADDED/REMOVED/CHANGED and ACTION_EXTERNAL_APPLICATIONS_AVAILABLE/UNAVAILABLE',
  evidence='SRC PackageReceiver.java:20-35; INFERRED ActivityThread dispatches broadcasts to registered receivers')

# CloudStreamServer.<init>(File)
UNREACHABLE['CloudStreamServer.<init>(File)'] = ('no_trigger_in_app',
  'Constructor overload not used; CloudStreamer subclass calls super(port, new File(".")) which uses the (int,File) constructor',
  'SRC CloudStreamer.java:31 calls super(port, new File(".")); CloudStreamServer.java:195-226 is (int,File) constructor, CloudStreamServer.java:230-247 is (File) constructor; GREP no callers of single-parameter constructor',
  'SOURCE')
UNREACHABLE['CloudStreamServer.lambda$new$1'] = ('no_trigger_in_app',
  'lambda in the CloudStreamServer(File) constructor; that constructor has no caller in the app',
  'SRC CloudStreamServer.java:226-229; SRC CloudStreamer.java:31 calls super(int,File) only', 'SOURCE')

# CloudUtil$2.<init>
e('CloudUtil.getThumbnailInputStreamForCloud', 'CloudUtil$2.<init>', 'CALL',
  'getThumbnailInputStreamForCloud creates anonymous SFtpClientTemplate for SFTP mode',
  evidence='SRC CloudUtil.java:265-282')
e('SshClientUtils$2.execute', 'CloudUtil$2.execute', 'CALL',
  'SshClientUtils.execute calls template execute method',
  evidence='INFERRED SshClientUtils.execute pattern')

# CloudUtil$2$1.close
e('CloudUtil.getThumbnailInputStreamForCloud', 'CloudUtil$2$1.<init>', 'CALL',
  'getThumbnailInputStreamForCloud creates anonymous RemoteFileInputStream subclass with overridden close method for SFTP mode',
  evidence='SRC CloudUtil.java:268-281')

# EncryptDecryptUtils.<init>
UNREACHABLE['EncryptDecryptUtils.<init>'] = ('no_trigger_in_app',
  'Utility class with only static methods; constructor never instantiated in app source',
  'SRC EncryptDecryptUtils.java:34 (class with only static methods startEncryption, decryptFile, findEncryptedEntry); GREP shows only "new EncryptDecryptUtils.EncryptButtonCallbackInterface()" in ItemPopupMenu.java (interface implementation, not class instantiation)',
  'SOURCE')

# CloudIconModelFactory.build
e('AmazeFileManagerModule.registerComponents', 'CloudIconModelFactory.<init>', 'CALL',
  'Glide module registration creates CloudIconModelFactory',
  evidence='SRC AmazeFileManagerModule.java:22')

# UtilitiesProvider.getThemeManager
e('AppConfig.onCreate', 'UtilitiesProvider.<init>', 'CALL',
  'AppConfig creates UtilitiesProvider singleton',
  evidence='SRC AppConfig.java:76')
e('PrefFrag.lambda$onPreferenceClick$2', 'UtilitiesProvider.getThemeManager', 'CALL',
  'PrefFrag calls getThemeManager to access AppThemeManager',
  evidence='SRC PrefFrag.java:179 (utilsProvider.getThemeManager().setAppTheme(...))')

# AppThemeManager.setAppTheme
e('PrefFrag.lambda$onPreferenceClick$2', 'AppThemeManager.setAppTheme', 'CALL',
  'PrefFrag theme dialog onClick listener calls setAppTheme when user changes theme',
  evidence='SRC PrefFrag.java:179 (utilsProvider.getThemeManager().setAppTheme(AppTheme.getTheme(which)))')

# ---- part repair_rp25 (2024-10-28)
# Repair batch 25: 18 methods (20 already have routes)
# Generated: 2024-10-28 21:56

# AbstractProgressiveService.getDataPackage

# AbstractProgressiveService.getDataPackageSize

# AbstractProgressiveService.isDecryptService
e('ServiceWatcherUtil$1.run', 'AbstractProgressiveService.isDecryptService', 'CALL',
  'ServiceWatcherUtil watcher thread checks isDecryptService for workaround when written size equals total size',
  evidence='SRC ServiceWatcherUtil.java:149 (if (interactionInterface.isDecryptService() && writtenSize.equals(totalSize)))')

# AppDataParcelable.describeContents
UNREACHABLE['AppDataParcelable.describeContents'] = ('framework_never_calls',
  'Parcelable.describeContents is required by interface but returns 0 (no special objects); never called by app or framework for simple data parcelables',
  'SRC AppDataParcelable.java:32-34 (returns 0); GREP no app callers of describeContents on AppDataParcelable',
  'SOURCE')

# AppDataParcelable.writeToParcel
UNREACHABLE['AppDataParcelable.writeToParcel'] = ('framework_never_calls',
  'Parcelable.writeToParcel is required by interface but AppDataParcelable is not parceled between processes in app; only used within single process for data passing',
  'SRC AppDataParcelable.java:37-44 (writes fields to parcel); GREP no callers of writeToParcel on AppDataParcelable in app source',
  'SOURCE')

# CheckBox.clearListenerInViewGroup
e('CheckBox.onBindView', 'CheckBox.clearListenerInViewGroup', 'CALL',
  'onBindView calls clearListenerInViewGroup to remove existing listener before rebinding to avoid duplicate listeners',
  evidence='SRC CheckBox.java:21 (clearListenerInViewGroup((ViewGroup) view))')

# CheckableCircleView.onDraw

# CircleGradientDrawable.<init>(String,AppTheme,DisplayMetrics)
UNREACHABLE['CircleGradientDrawable.<init>(String,AppTheme,DisplayMetrics)'] = ('no_trigger_in_app',
  'String color constructor overload not used; app only uses int color variant CircleGradientDrawable(int,AppTheme,DisplayMetrics)',
  'SRC CircleGradientDrawable.java:23-30 (String color constructor); GREP no callers of String-parameter constructor in app source; CircleGradientDrawable is created with int color in AppsAdapter.java',
  'SOURCE')

# CircularColorsView.<init>(Context,AttributeSet)

# CircularColorsView.init
e('CircularColorsView.<init>(Context)', 'CircularColorsView.init', 'CALL',
  'Constructor calls init to initialize paints and divider',
  evidence='SRC CircularColorsView.java:32 (init())')

# CircularColorsView.onDraw

# CloudIconDataFetcher.cleanup

# CloudIconDataFetcher.getDataClass

# CloudIconDataFetcher.getDataSource

# CloudStreamer.isStreamMedia
UNREACHABLE['CloudStreamer.isStreamMedia'] = ('no_trigger_in_app',
  'Static method for SmbFile pattern matching; not called from app source',
  'SRC CloudStreamer.java:44-46 (static method checks file name pattern for media extensions); GREP no callers of isStreamMedia in app source',
  'SOURCE')

# Coders$BCJDecoder.encode

# Coders$BZIP2Decoder.encode

# Coders$CopyDecoder.encode

# ---- part repair_rp26 (2024-10-28)
# Repair batch 26 - DeflateDecoder streams and Color classes
# Generated by READ-ONLY helper slot 2

# ========== Coders$DeflateDecoder$DeflateDecoderInputStream methods ==========

# These stream methods are invoked polymorphically when the InputStream returned
# by Coders$DeflateDecoder.decode is used. Following the pattern from 
# BoundedFileChannelInputStream, edges from <init> to the stream methods.

e('Coders$DeflateDecoder$DeflateDecoderInputStream.<init>', 
  'Coders$DeflateDecoder$DeflateDecoderInputStream.read()', 
  'CALL', 
  'Stream read() method invoked when reading from DeflateDecoder InputStream',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Coders.java:167-169 public int read() throws IOException { return inflaterInputStream.read(); }')

e('Coders$DeflateDecoder$DeflateDecoderInputStream.<init>', 
  'Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[])', 
  'CALL', 
  'Stream read(byte[]) method invoked when reading from DeflateDecoder InputStream',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Coders.java:175-177 public int read(final byte[] b) throws IOException { return inflaterInputStream.read(b); }')

e('Coders$DeflateDecoder$DeflateDecoderInputStream.<init>', 
  'Coders$DeflateDecoder$DeflateDecoderInputStream.read(byte[],int,int)', 
  'CALL', 
  'Stream read(byte[],int,int) method invoked when reading from DeflateDecoder InputStream',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Coders.java:171-173 public int read(final byte[] b, final int off, final int len) throws IOException { return inflaterInputStream.read(b, off, len); }')

e('Coders$DeflateDecoder$DeflateDecoderInputStream.<init>', 
  'Coders$DeflateDecoder$DeflateDecoderInputStream.close', 
  'CALL', 
  'Stream close() method invoked when closing DeflateDecoder InputStream',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Coders.java:179-185 public void close() throws IOException { try { inflaterInputStream.close(); } finally { inflater.end(); } }')

# ---- part repair_rp28 (2024-10-28)
# repair_rp28 - Batch 28 repairs (converted from EDGES format to e() calls)

# Indicator.<init>(Context) - constructor delegation
e('Indicator.<init>(Context)', 'Indicator.<init>(Context,AttributeSet,int)', 'CALL',
  'Constructor delegation: single-arg constructor delegates to three-arg constructor with null AttributeSet and 0 defStyle',
  evidence='SRC Indicator.java:113-115: public Indicator(Context context) { this(context, null, 0); }')

# Indicator.<init>(Context,AttributeSet) - constructor delegation

# MainActivityHelper$4 lambdas - mkdir ErrorCallBack implementation

# MainActivityHelper$4.lambda$exists$0
e('MainActivityHelper$4.exists', 'MainActivityHelper$4.lambda$exists$0', 'CALL',
  'exists callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC MainActivityHelper.java:456-465: ma.getActivity().runOnUiThread(() -> { if (toast != null) toast.cancel(); Toast.makeText(...); ... }); lambda at 456-465')



e('MainActivityHelper$4.lambda$exists$0', 'MainActivityHelper.mkdir', 'CALL',
  'Lambda retries mkdir with dialog prompted again',
  evidence='SRC MainActivityHelper.java:462: mkdir(file.getMode(), file.getParent(), ma);')

# MainActivityHelper$4.lambda$launchSAF$1
e('MainActivityHelper$4.launchSAF(HybridFile)', 'MainActivityHelper$4.lambda$launchSAF$1', 'CALL',
  'launchSAF callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC MainActivityHelper.java:470-474: ma.getActivity().runOnUiThread(() -> { mainActivity.oppathe = path.getPath(); mainActivity.operation = DataUtils.NEW_FOLDER; guideDialogForLEXA(...); }); lambda at 470-474')

e('MainActivityHelper$4.lambda$launchSAF$1', 'MainActivityHelper.guideDialogForLEXA', 'CALL',
  'Lambda shows SAF guide dialog for creating new folder',
  evidence='SRC MainActivityHelper.java:472: guideDialogForLEXA(mainActivity.oppathe);')

# MainActivityHelper$4.lambda$done$2
e('MainActivityHelper$4.done', 'MainActivityHelper$4.lambda$done$2', 'CALL',
  'done callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC MainActivityHelper.java:483-489: ma.getActivity().runOnUiThread(() -> { if (b) { ma.updateList(); } else { Toast.makeText(...); } }); lambda at 483-489')

e('MainActivityHelper$4.lambda$done$2', 'MainFragment.updateList', 'CALL',
  'Lambda updates file list on success',
  evidence='SRC MainActivityHelper.java:484: if (b) { ma.updateList(); }')


# MainActivityHelper$4.lambda$invalidName$3
e('MainActivityHelper$4.invalidName', 'MainActivityHelper$4.lambda$invalidName$3', 'CALL',
  'invalidName callback runs lambda on UI thread via runOnUiThread',
  evidence='SRC MainActivityHelper.java:493-499: ma.getActivity().runOnUiThread(() -> { if (toast != null) toast.cancel(); Toast.makeText(...); }); lambda at 493-499')



# CALLBACK edges from Operations.mkdir to MainActivityHelper$4
e('Operations.mkdir', 'MainActivityHelper$4.exists', 'FRAMEWORK',
  'Operations.mkdir calls exists callback when directory already exists',
  evidence='SRC MainActivityHelper.java:453-455: Operations.mkdir(path, ma.getActivity(), mainActivity.isRootExplorer(), new Operations.ErrorCallBack() { @Override public void exists(final HybridFile file) { ... } }); mkdir invokes ErrorCallBack.exists')

e('Operations.mkdir', 'MainActivityHelper$4.launchSAF(HybridFile)', 'FRAMEWORK',
  'Operations.mkdir calls launchSAF callback when SAF permission needed',
  evidence='SRC MainActivityHelper.java:453,468-476: Operations.mkdir(..., new Operations.ErrorCallBack() { @Override public void launchSAF(HybridFile file) { ... } }); mkdir invokes ErrorCallBack.launchSAF')

e('Operations.mkdir', 'MainActivityHelper$4.done', 'FRAMEWORK',
  'Operations.mkdir calls done callback when mkdir operation completes',
  evidence='SRC MainActivityHelper.java:453,482-490: Operations.mkdir(..., new Operations.ErrorCallBack() { @Override public void done(HybridFile hFile, final boolean b) { ... } }); mkdir invokes ErrorCallBack.done')

e('Operations.mkdir', 'MainActivityHelper$4.invalidName', 'FRAMEWORK',
  'Operations.mkdir calls invalidName callback when directory name is invalid',
  evidence='SRC MainActivityHelper.java:453,493-500: Operations.mkdir(..., new Operations.ErrorCallBack() { @Override public void invalidName(final HybridFile file) { ... } }); mkdir invokes ErrorCallBack.invalidName')

# ---- part repair_rp29 (2024-10-28)

e('MainFragment.onCreateView', 'MainFragment$1.<init>', 'CALL',
  'MainFragment.java:310 registers OnGlobalLayoutListener',
  gui=['MainFragment view tree layout'],
  evidence='SRC MainFragment.java:310: mToolbarContainer.getViewTreeObserver().addOnGlobalLayoutListener(new ViewTreeObserver.OnGlobalLayoutListener() {')

e('MainFragment$1.<init>', 'MainFragment$1.onGlobalLayout', 'CALL',
  'INFERRED ViewTreeObserver dispatches onGlobalLayout when layout changes',
  evidence='FW-SRC android.view.ViewTreeObserver dispatches registered OnGlobalLayoutListener callbacks')

e('MainFragment$4$1.<init>', 'MainFragment$4$1.onMediaScannerConnected', 'CALL',
  'INFERRED MediaScannerConnection dispatches onMediaScannerConnected callback',
  evidence='FW-SRC android.media.MediaScannerConnection invokes MediaScannerConnectionClient.onMediaScannerConnected when connected')

e('MainFragment$4$1.<init>', 'MainFragment$4$1.onScanCompleted', 'CALL',
  'INFERRED MediaScannerConnection dispatches onScanCompleted callback',
  evidence='FW-SRC android.media.MediaScannerConnection invokes MediaScannerConnectionClient.onScanCompleted when scan finishes')

e('MainFragment.onResume', 'MainFragment$5.<init>', 'CALL',
  'MainFragment.java:1427 registers decryptReceiver',
  evidence='SRC MainFragment.java:1427: (getActivity()).registerReceiver(decryptReceiver, new IntentFilter(EncryptDecryptUtils.DECRYPT_BROADCAST));')

e('MainFragment$5.<init>', 'MainFragment$5.onReceive', 'CALL',
  'INFERRED framework dispatches onReceive when DECRYPT_BROADCAST is sent',
  evidence='FW-SRC android.app.ActivityThread/LoadedApk dispatches BroadcastReceiver.onReceive; registered with IntentFilter for EncryptDecryptUtils.DECRYPT_BROADCAST')

e('SftpConnectDialog.lambda$null$11', 'OperationData.<init>(Operation,String,String,String,String,String)', 'CALL',
  'SftpConnectDialog.java:250 creates OperationData for SFTP removal',
  evidence='SRC SftpConnectDialog.java:250: utilsHandler.removeFromDatabase(new OperationData(UtilsHandler.Operation.SFTP, ...')

e('SftpConnectDialog.authenticateAndSaveSetup', 'OperationData.<init>(Operation,String,String,String,String,String)', 'CALL',
  'SftpConnectDialog.java:352 creates OperationData for SFTP save',
  evidence='SRC SftpConnectDialog.java:352: utilsHandler.saveToDatabase(new OperationData(UtilsHandler.Operation.SFTP, ...')

# ---- part repair_rp30 (2024-10-28)

e('SftpConnectDialog.onActivityResult', 'PemToKeyPairTask.<init>(InputStream,Callback)', 'CALL',
  'SftpConnectDialog instantiates PemToKeyPairTask with selected PEM key file InputStream',
  evidence='SRC PemToKeyPairTask.java:95-97: public PemToKeyPairTask(@NonNull InputStream pemFile, AsyncTaskResult.Callback<KeyPair> callback) throws IOException { this(IOUtils.readFully(pemFile).toByteArray(), callback); }; caller site found via grep')

e('PemToKeyPairTask.<init>(InputStream,Callback)', 'PemToKeyPairTask.<init>(byte[],Callback)', 'CALL',
  'Constructor delegates to private byte array constructor after reading InputStream',
  evidence='SRC PemToKeyPairTask.java:95-97: public PemToKeyPairTask(@NonNull InputStream pemFile, AsyncTaskResult.Callback<KeyPair> callback) throws IOException { this(IOUtils.readFully(pemFile).toByteArray(), callback); }')


e('PemToKeyPairTask.doInBackground', 'PemToKeyPairTask$PemToKeyPairConverter.convert', 'CALL',
  'doInBackground tries each converter to parse PEM key',
  evidence='SRC PemToKeyPairTask.java:115: KeyPair keyPair = converter.convert(new String(pemFile));')



e('PemToKeyPairTask.lambda$onProgressUpdate$0', 'PemToKeyPairTask$1.<init>', 'CALL',
  'Lambda creates anonymous PasswordFinder implementation',
  evidence='SRC PemToKeyPairTask.java:148-156: this.passwordFinder = new PasswordFinder() { @Override public char[] reqPassword(Resource<?> resource) { return textfield.getText().toString().toCharArray(); } @Override public boolean shouldRetry(Resource<?> resource) { return false; } };')


e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask.lambda$onProgressUpdate$2', 'FRAMEWORK',
  'onProgressUpdate registers lambda as text validation callback',
  evidence='SRC PemToKeyPairTask.java:167-172: new WarnableTextInputValidator(AppConfig.getInstance().getMainActivityContext(), textfield, wilTextfield, dialog.getActionButton(DialogAction.POSITIVE), (text) -> { if (text.length() < 1) { return new WarnableTextInputValidator.ReturnState(...); } return new WarnableTextInputValidator.ReturnState(); })')


e('PemToKeyPairTask.onPostExecute', 'SftpConnectDialog.lambda$onActivityResult$14', 'CALL',
  'onPostExecute delivers KeyPair result to callback',
  evidence='SRC PemToKeyPairTask.java:179: callback.onResult(result);')



e('PemToKeyPairTask$OpenSshPemToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.reqPassword', 'CALL',
  'OpenSSH converter calls reqPassword when password-protected key needs decryption',
  evidence='SRC PemToKeyPairTask.java:213: converter.init(new StringReader(source), passwordFinder); sshj library OpenSSHKeyFile.init will call passwordFinder.reqPassword if key is encrypted')

e('PemToKeyPairTask$OpenSshV1PemToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.reqPassword', 'CALL',
  'OpenSSH v1 converter calls reqPassword when password-protected key needs decryption',
  evidence='SRC PemToKeyPairTask.java:220: converter.init(new StringReader(source), passwordFinder); sshj library OpenSSHKeyV1KeyFile.init will call passwordFinder.reqPassword if key is encrypted')

e('PemToKeyPairTask$PuttyPrivateKeyToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.reqPassword', 'CALL',
  'PuTTY converter calls reqPassword when password-protected key needs decryption',
  evidence='SRC PemToKeyPairTask.java:227: converter.init(new StringReader(source), passwordFinder); sshj library PuTTYKeyFile.init will call passwordFinder.reqPassword if key is encrypted')

e('PemToKeyPairTask$OpenSshPemToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.shouldRetry', 'CALL',
  'OpenSSH converter calls shouldRetry to check if password retry is allowed',
  evidence='SRC PemToKeyPairTask.java:154-156: @Override public boolean shouldRetry(Resource<?> resource) { return false; }; called by sshj library after password attempt')

e('PemToKeyPairTask$OpenSshV1PemToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.shouldRetry', 'CALL',
  'OpenSSH v1 converter calls shouldRetry to check if password retry is allowed',
  evidence='SRC PemToKeyPairTask.java:154-156: @Override public boolean shouldRetry(Resource<?> resource) { return false; }; called by sshj library after password attempt')

e('PemToKeyPairTask$PuttyPrivateKeyToKeyPairConverter.throwingConvert', 'PemToKeyPairTask$1.shouldRetry', 'CALL',
  'PuTTY converter calls shouldRetry to check if password retry is allowed',
  evidence='SRC PemToKeyPairTask.java:154-156: @Override public boolean shouldRetry(Resource<?> resource) { return false; }; called by sshj library after password attempt')


e('PrefFrag.onCreate', 'PrefFrag.lambda$onCreate$0', 'FRAMEWORK',
  'onCreate registers lambda as onPreferenceChangeListener for fingerprint checkbox',
  evidence='SRC PrefFrag.java:94-111: checkBoxFingerprint.setOnPreferenceChangeListener((preference, newValue) -> { ... });')




e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$1', 'FRAMEWORK',
  'onPreferenceClick registers lambda for grid columns dialog item selection',
  evidence='SRC PrefFrag.java:135-140: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... })')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$2', 'FRAMEWORK',
  'onPreferenceClick registers lambda for theme dialog item selection',
  evidence='SRC PrefFrag.java:147-152: builder.items(sort).itemsCallbackSingleChoice(current, (dialog, view, which, text) -> { ... })')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$3', 'FRAMEWORK',
  'onPreferenceClick registers lambda for master password dialog input callback',
  evidence='SRC PrefFrag.java:227: masterPasswordDialogBuilder.input(..., (dialog, input) -> { });')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$4', 'FRAMEWORK',
  'onPreferenceClick registers lambda as positive button action for master password dialog',
  evidence='SRC PrefFrag.java:233-248: masterPasswordDialogBuilder.onPositive((dialog, which) -> { ... })')

e('PrefFrag.onPreferenceClick', 'PrefFrag.lambda$onPreferenceClick$5', 'FRAMEWORK',
  'onPreferenceClick registers lambda as negative button action for master password dialog',
  evidence='SRC PrefFrag.java:250: masterPasswordDialogBuilder.onNegative((dialog, which) -> dialog.cancel())')

e('PrefFrag.onPreferenceClick', 'PrefFrag.restartPC', 'CALL',
  'onPreferenceClick calls restartPC to restart activity after theme change',
  evidence='SRC PrefFrag.java:150: restartPC(getActivity());')


e('PrefFrag.lambda$onPreferenceClick$2', 'PrefFrag.restartPC', 'CALL',
  'Lambda restarts activity after theme selection',
  evidence='SRC PrefFrag.java:150: restartPC(getActivity());')







e('PrepareCopyTask.doInBackground', 'PrepareCopyTask$CopyNode.<init>', 'CALL',
  'doInBackground creates root CopyNode with file list',
  evidence='SRC PrepareCopyTask.java:113: copyFolder = new CopyNode(path, filesToCopy);')

e('PrepareCopyTask.checkConflicts', 'PrepareCopyTask.lambda$checkConflicts$0', 'CALL',
  'checkConflicts uses lambda to iterate children via forEachChildrenFile',
  evidence='SRC PrepareCopyTask.java:121-127: destination.forEachChildrenFile(context, rootMode, file -> { for (HybridFileParcelable j : filesToCopy) { if (file.getName().equals((j).getName())) { conflictingFiles.add(j); } } });')


e('PrepareCopyTask.onPostExecute', 'PrepareCopyTask.startService', 'CALL',
  'onPostExecute starts CopyService for special open modes',
  evidence='SRC PrepareCopyTask.java:141: startService(filesToCopy, path, openMode);')

e('PrepareCopyTask.onPostExecute', 'PrepareCopyTask.onEndDialog', 'CALL',
  'onPostExecute delegates to onEndDialog for normal file system copies',
  evidence='SRC PrepareCopyTask.java:145: onEndDialog(null, null, null);')

e('PrepareCopyTask.startService', 'CopyService.<init>', 'CALL',
  'startService creates Intent for CopyService',
  evidence='SRC PrepareCopyTask.java:153: Intent intent = new Intent(context, CopyService.class);')

e('PrepareCopyTask.showDialog', 'PrepareCopyTask.lambda$showDialog$1', 'FRAMEWORK',
  'showDialog registers lambda for positive button (skip) action',
  evidence='SRC PrepareCopyTask.java:198-202: dialogBuilder.onPositive((dialog, which) -> { if (checkBox.isChecked()) dialogState = DO_FOR_ALL_ELEMENTS.DO_NOT_REPLACE; doNotReplaceFiles(path, filesToCopy, conflictingFiles); })')

e('PrepareCopyTask.showDialog', 'PrepareCopyTask.lambda$showDialog$2', 'FRAMEWORK',
  'showDialog registers lambda for negative button (overwrite) action',
  evidence='SRC PrepareCopyTask.java:203-207: dialogBuilder.onNegative((dialog, which) -> { if (checkBox.isChecked()) dialogState = DO_FOR_ALL_ELEMENTS.REPLACE; replaceFiles(path, filesToCopy, conflictingFiles); })')

e('PrepareCopyTask.lambda$showDialog$1', 'PrepareCopyTask.doNotReplaceFiles', 'CALL',
  'Skip button lambda calls doNotReplaceFiles',
  evidence='SRC PrepareCopyTask.java:201: doNotReplaceFiles(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.lambda$showDialog$2', 'PrepareCopyTask.replaceFiles', 'CALL',
  'Overwrite button lambda calls replaceFiles',
  evidence='SRC PrepareCopyTask.java:206: replaceFiles(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask.showDialog', 'CALL',
  'onEndDialog shows conflict resolution dialog when needed',
  evidence='SRC PrepareCopyTask.java:226: showDialog(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask.doNotReplaceFiles', 'CALL',
  'onEndDialog skips files when DO_NOT_REPLACE state is set',
  evidence='SRC PrepareCopyTask.java:228: doNotReplaceFiles(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask.replaceFiles', 'CALL',
  'onEndDialog replaces files when REPLACE state is set',
  evidence='SRC PrepareCopyTask.java:230: replaceFiles(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask$CopyNode.startCopy', 'CALL',
  'onEndDialog starts BFS traversal of copy node tree',
  evidence='SRC PrepareCopyTask.java:232: CopyNode c = !copyFolder.hasStarted()? copyFolder.startCopy():copyFolder.goToNextNode();')

e('PrepareCopyTask.onEndDialog', 'PrepareCopyTask$CopyNode.goToNextNode', 'CALL',
  'onEndDialog advances to next node in BFS traversal',
  evidence='SRC PrepareCopyTask.java:232: CopyNode c = !copyFolder.hasStarted()? copyFolder.startCopy():copyFolder.goToNextNode();')

e('PrepareCopyTask.doNotReplaceFiles', 'PrepareCopyTask.onEndDialog', 'CALL',
  'doNotReplaceFiles recurses to onEndDialog to process next files',
  evidence='SRC PrepareCopyTask.java:260: onEndDialog(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask.replaceFiles', 'PrepareCopyTask.onEndDialog', 'CALL',
  'replaceFiles recurses to onEndDialog to process next files',
  evidence='SRC PrepareCopyTask.java:273: onEndDialog(path, filesToCopy, conflictingFiles);')

e('PrepareCopyTask$CopyNode.<init>', 'PrepareCopyTask.checkConflicts', 'CALL',
  'CopyNode constructor calls checkConflicts to find name collisions',
  evidence='SRC PrepareCopyTask.java:301: conflictingFiles = checkConflicts(filesToCopy, destination);')

e('PrepareCopyTask$CopyNode.<init>', 'PrepareCopyTask$CopyNode.<init>', 'CALL',
  'CopyNode constructor recursively creates child nodes for conflicting directories',
  evidence='SRC PrepareCopyTask.java:309-312: nextNodes.add(new CopyNode(path + "/" + conflictingFiles.get(i).getName(), conflictingFiles.get(i).listFiles(context, rootMode)));')

e('PrepareCopyTask$CopyNode.startCopy', 'PrepareCopyTask$CopyNode.<init>', 'FRAMEWORK',
  'startCopy initializes BFS queue and visited set',
  evidence='SRC PrepareCopyTask.java:327-330: queue = new LinkedList<>(); visited = new HashSet<>(); queue.add(this); visited.add(this); (implicit reference to this node)')

e('PrepareCopyTask$CopyNode.goToNextNode', 'PrepareCopyTask$CopyNode.getUnvisitedChildNode', 'CALL',
  'goToNextNode gets next unvisited child for BFS traversal',
  evidence='SRC PrepareCopyTask.java:342: CopyNode child; if ((child = getUnvisitedChildNode(visited, node)) != null) { ... }')

e('PrepareCopyTask$CopyNode.goToNextNode', 'PrepareCopyTask$CopyNode.goToNextNode', 'CALL',
  'goToNextNode recursively processes queue until finding next node',
  evidence='SRC PrepareCopyTask.java:348: return goToNextNode();')


e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'ProcessViewerFragment.processResults', 'CALL',
  'onServiceConnected calls processResults for each existing data package',
  evidence='SRC ProcessViewerFragment.java:321: fragment.processResults(dataPackage, serviceType);')


# UNREACHABLE entries

# ---- part repair_rp31 (2024-10-28)

e('RecyclerAdapter.setItems(RecyclerView,ArrayList,boolean)', 'RecyclerPreloadModelProvider.<init>', 'CALL',
  'setItems creates RecyclerPreloadModelProvider and passes to RecyclerViewPreloader',
  evidence='SRC RecyclerAdapter.java:388 modelProvider = new RecyclerPreloadModelProvider(mainFrag, uris);')

e('RecyclerPreloadModelProvider.<init>', 'RecyclerPreloadModelProvider.getPreloadItems', 'FRAMEWORK',
  'Glide RecyclerViewPreloader calls getPreloadItems via ListPreloader.PreloadModelProvider interface',
  evidence='SRC RecyclerAdapter.java:389 preloader = new RecyclerViewPreloader<>(GlideApp.with(mainFrag), modelProvider, sizeProvider, GlideConstants.MAX_PRELOAD_FILES); RecyclerPreloadModelProvider.java:23 public class RecyclerPreloadModelProvider implements ListPreloader.PreloadModelProvider<IconDataParcelable> { SRC RecyclerPreloadModelProvider.java:35-38 @Override public List<IconDataParcelable> getPreloadItems(int position) { IconDataParcelable iconData = urisToLoad.get(position); ... }; INFERRED Glide RecyclerViewPreloader calls PreloadModelProvider.getPreloadItems')

e('RootHelper.runShellCommandToList', 'RootHelper.lambda$runShellCommandToList$0', 'ASYNC',
  'runShellCommandToList passes lambda to runShellCommandWithCallback',
  evidence='SRC RootHelper.java:50 runShellCommandWithCallback(cmd, (commandCode, exitCode, output) -> result.addAll(output));')

e('RootHelper.lambda$runShellCommandToList$0', 'RootHelper.runShellCommandWithCallback', 'CALL',
  'lambda$runShellCommandToList$0 is the desugared lambda body passed to runShellCommandWithCallback',
  evidence='SRC RootHelper.java:50 runShellCommandWithCallback(cmd, (commandCode, exitCode, output) -> result.addAll(output)); INFERRED lambda desugaring creates synthetic method')

e('RootUtils.changePermissions', 'RootUtils.lambda$changePermissions$0', 'ASYNC',
  'changePermissions passes lambda callback to RootHelper.runShellCommandWithCallback',
  evidence='SRC RootUtils.java:117-121 RootHelper.runShellCommandWithCallback(command, (commandCode, exitCode, output) -> { if (exitCode < 0) { onOperationPerform.callback(false); } else { onOperationPerform.callback(true); } });')

e('RootUtils.lambda$changePermissions$0', 'RootHelper.runShellCommandWithCallback', 'CALL',
  'lambda$changePermissions$0 is the desugared lambda body',
  evidence='SRC RootUtils.java:117-121 (commandCode, exitCode, output) -> { if (exitCode < 0) { onOperationPerform.callback(false); } else { onOperationPerform.callback(true); } }; INFERRED lambda desugaring creates synthetic method')

# UNREACHABLE entries

UNREACHABLE['ProgressHandler.<init>(int,long)'] = ('no_trigger_in_app', 'two-argument constructor never called; all call sites use no-argument constructor', 'SRC ProgressHandler.java:48-51 public ProgressHandler(int sourceFiles, long totalSize) { this.sourceFiles = sourceFiles; this.totalSize = totalSize; }; grep output: CopyService.java:83 private ProgressHandler progressHandler = new ProgressHandler(); ZipService.java:76 private ProgressHandler progressHandler = new ProgressHandler(); ExtractService.java:78 private ProgressHandler progressHandler = new ProgressHandler(); DecryptService.java:49 private ProgressHandler progressHandler = new ProgressHandler(); EncryptService.java:50 private ProgressHandler progressHandler = new ProgressHandler(); (all use no-argument constructor)', 'SOURCE')
UNREACHABLE['RootHelper.<init>'] = ('no_trigger_in_app', 'utility class with only static methods, constructor never called', 'SRC RootHelper.java:36 public class RootHelper { (no explicit constructor, default constructor generated); grep -rn "new RootHelper" returns no matches', 'SOURCE')
UNREACHABLE['RootHelper.generateBaseFile(DocumentFile)'] = ('no_trigger_in_app', 'DocumentFile overload never called; all call sites use File parameter overload', 'SRC RootHelper.java:151-158 public static HybridFileParcelable generateBaseFile(DocumentFile file) { long size = 0; if (!file.isDirectory()) size = file.length(); HybridFileParcelable baseFile = new HybridFileParcelable(file.getName(), parseDocumentFilePermission(file), file.lastModified(), size, file.isDirectory()); baseFile.setName(file.getName()); baseFile.setMode(OpenMode.OTG); return baseFile; }; grep -rn "RootHelper.generateBaseFile" shows all call sites use "new File" parameter except AppsAdapter.java:248 which calls generateBaseFile(f, true) with File parameter', 'SOURCE')
UNREACHABLE['RootHelper.runNonRootShellCommand'] = ('no_trigger_in_app', 'deprecated method never called', 'SRC RootHelper.java:83-94 @deprecated Use {@link #runShellCommand(String)} instead which runs command on an interactive shell public static List<String> runNonRootShellCommand(String cmd) { return Shell.SH.run(cmd); }; grep -rn "runNonRootShellCommand" returns only the method definition', 'SOURCE')
UNREACHABLE['RootUtils.<init>'] = ('no_trigger_in_app', 'utility class with only static methods and constants, constructor never called', 'SRC RootUtils.java:15 public class RootUtils { (no explicit constructor); grep -rn "new RootUtils" returns no matches', 'SOURCE')
UNREACHABLE['RootUtils.getFilePermissions'] = ('no_trigger_in_app', 'private method never called within class', 'SRC RootUtils.java:163-166 private static int getFilePermissions(String path) throws ShellNotRunningException { String line = RootHelper.runShellCommandToList("stat -c  %a \\"" + path + "\\"").get(0); return Integer.valueOf(line); }; grep -rn "getFilePermissions" within RootUtils.java shows only the method definition', 'SOURCE')

# ---- part repair_rp32 (2024-10-28)






# ---- part repair_rp33 (2024-10-28, filtered to keep only edges between existing nodes)
# Repair batch 33: Extra round 1
# Generated by label helper slot 1
# Status: DONE 22:46

# SevenZOutputFile$1 - anonymous CountingOutputStream subclass
# This class is never instantiated because SevenZOutputFile is never used in the app

UNREACHABLE['SevenZOutputFile$1.<init>'] = (
    'no_trigger_in_app',
    'Constructor for anonymous CountingOutputStream returned by SevenZOutputFile.setupFileOutputStream. SevenZOutputFile is a library class for writing 7z archives and is never instantiated in the app.',
    'SRC SevenZOutputFile.java:327 shows: return new CountingOutputStream(out) { ... }. Grep confirms no app code instantiates SevenZOutputFile or calls its methods',
    'SOURCE'
)

UNREACHABLE['SevenZOutputFile$1.write(byte[])'] = (
    'no_trigger_in_app',
    'Override of CountingOutputStream.write(byte[]) in anonymous class. Parent class SevenZOutputFile is never instantiated.',
    'SRC SevenZOutputFile.java:334-337 shows: @Override public void write(final byte[] b) throws IOException { super.write(b); crc32.update(b); }. No SevenZOutputFile instantiation in app',
    'SOURCE'
)

UNREACHABLE['SevenZOutputFile$1.write(byte[],int,int)'] = (
    'no_trigger_in_app',
    'Override of CountingOutputStream.write(byte[],int,int) in anonymous class. Parent class SevenZOutputFile is never instantiated.',
    'SRC SevenZOutputFile.java:339-343 shows: @Override public void write(final byte[] b, final int off, final int len) throws IOException { super.write(b, off, len); crc32.update(b, off, len); }. No SevenZOutputFile instantiation in app',
    'SOURCE'
)

UNREACHABLE['SevenZOutputFile$1.write(int)'] = (
    'no_trigger_in_app',
    'Override of CountingOutputStream.write(int) in anonymous class. Parent class SevenZOutputFile is never instantiated.',
    'SRC SevenZOutputFile.java:328-332 shows: @Override public void write(final int b) throws IOException { super.write(b); crc32.update(b); }. No SevenZOutputFile instantiation in app',
    'SOURCE'
)

# SevenZipHelperTask.lambda$onProgressUpdate$0
# This is a lambda in the onProgressUpdate callback

e('SevenZipHelperTask.onProgressUpdate', 'SevenZipHelperTask.lambda$onProgressUpdate$0', 'CALL',
  'Lambda passed to GeneralDialogCreation.showPasswordDialog as positive button callback',
  evidence='SRC SevenZipHelperTask.java:106-112 shows ((dialog, which) -> { EditText editText = dialog.getView().findViewById(R.id.singleedittext_input); String password = editText.getText().toString(); ArchivePasswordCache.getInstance().put(filePath, password); paused = false; dialog.dismiss(); })')





e('SevenZipHelperTask.lambda$onProgressUpdate$0', 'ArchivePasswordCache.getInstance', 'CALL',
  'Lambda calls getInstance to get singleton',
  evidence='SRC SevenZipHelperTask.java:109 shows ArchivePasswordCache.getInstance().put(filePath, password)')

e('SevenZipHelperTask.lambda$onProgressUpdate$0', 'ArchivePasswordCache.put', 'CALL',
  'Lambda stores password in cache',
  evidence='SRC SevenZipHelperTask.java:109 shows ArchivePasswordCache.getInstance().put(filePath, password)')


# SftpConnectDialog methods
# onCreateDialog is the DialogFragment lifecycle method that creates the dialog

e('SftpConnectDialog.onCreate', 'AppConfig.getInstance', 'CALL',
  'onCreate calls getInstance to get AppConfig singleton',
  evidence='SRC SftpConnectDialog.java:97 shows utilsProvider = AppConfig.getInstance().getUtilsProvider()')

e('SftpConnectDialog.onCreate', 'AppConfig.getUtilsProvider', 'CALL',
  'onCreate gets utils provider from AppConfig',
  evidence='SRC SftpConnectDialog.java:97 shows utilsProvider = AppConfig.getInstance().getUtilsProvider()')

e('SftpConnectDialog.onCreate', 'AppConfig.getUtilsHandler', 'CALL',
  'onCreate gets utils handler from AppConfig',
  evidence='SRC SftpConnectDialog.java:98 shows utilsHandler = AppConfig.getInstance().getUtilsHandler()')

# onCreateDialog creates the SSH/SFTP connection dialog














e('SftpConnectDialog.onCreateDialog', 'ThemedActivity.getAccent', 'CALL',
  'onCreateDialog gets accent color',
  evidence='SRC SftpConnectDialog.java:143 shows int accentColor = ((ThemedActivity) getActivity()).getAccent()')


e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$1', 'FRAMEWORK',
  'Lambda callback when selectPemBTN is clicked',
  evidence='SRC SftpConnectDialog.java:148-153 shows lambda that starts file picker intent')





e('SftpConnectDialog.onCreateDialog', 'UtilitiesProvider.getAppTheme', 'CALL',
  'onCreateDialog gets app theme',
  evidence='SRC SftpConnectDialog.java:160 shows dialogBuilder.theme(utilsProvider.getAppTheme().getMaterialDialogTheme())')

e('SftpConnectDialog.onCreateDialog', 'AppTheme.getMaterialDialogTheme', 'CALL',
  'onCreateDialog gets material dialog theme',
  evidence='SRC SftpConnectDialog.java:160 shows utilsProvider.getAppTheme().getMaterialDialogTheme()')








e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$9', 'FRAMEWORK',
  'Lambda callback when positive button is clicked',
  evidence='SRC SftpConnectDialog.java:164-232 shows lambda that handles connection creation/update')


e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$10', 'FRAMEWORK',
  'Lambda callback when cancel button is clicked (non-edit mode)',
  evidence='SRC SftpConnectDialog.java:233 shows .onNegative((dialog, which) -> dialog.dismiss())')






e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog$1.<init>', 'CALL',
  'onCreateDialog creates TextWatcher for input validation',
  evidence='SRC SftpConnectDialog.java:276 shows TextWatcher validator = new SimpleTextWatcher() { ... }')


e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.lambda$onCreateDialog$0', 'FRAMEWORK',
  'Lambda callback for port field focus change',
  evidence='SRC SftpConnectDialog.java:137-140 shows portET.setOnFocusChangeListener((v, hasFocus) -> { if(hasFocus) portET.selectAll(); })')

# SftpConnectDialog.lambda$onCreateDialog$0 - port field focus listener


# SftpConnectDialog.lambda$onCreateDialog$1 - PEM file picker





# SftpConnectDialog.lambda$onCreateDialog$9 - positive button in normal flow





e('SftpConnectDialog.lambda$onCreateDialog$9', 'SshClientUtils.deriveSftpPathFrom', 'CALL',
  'Lambda derives SFTP path for database lookup',
  evidence='SRC SftpConnectDialog.java:175 shows deriveSftpPathFrom(hostname, port, username, getArguments().getString("password", null), selectedParsedKeyPair)')

e('SftpConnectDialog.lambda$onCreateDialog$9', 'UtilsHandler.getSshHostKey', 'CALL',
  'Lambda gets stored SSH host key',
  evidence='SRC SftpConnectDialog.java:174 shows utilsHandler.getSshHostKey(...)')

e('SftpConnectDialog.lambda$onCreateDialog$9', 'SshConnectionPool.getInstance', 'CALL',
  'Lambda gets SSH connection pool singleton',
  evidence='SRC SftpConnectDialog.java:179 shows SshConnectionPool.getInstance().removeConnection(...)')

e('SftpConnectDialog.lambda$onCreateDialog$9', 'SshConnectionPool.removeConnection', 'CALL',
  'Lambda removes existing connection before updating',
  evidence='SRC SftpConnectDialog.java:179 shows SshConnectionPool.getInstance().removeConnection(..., () -> { ... })')

e('SftpConnectDialog.lambda$onCreateDialog$9', 'SftpConnectDialog.lambda$null$2', 'CALL',
  'Lambda callback after connection removal when editing with existing host key',
  evidence='SRC SftpConnectDialog.java:180 shows lambda callback passed to removeConnection')

e('SftpConnectDialog.lambda$onCreateDialog$9', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'Lambda creates task to get host fingerprint when no stored key',
  evidence='SRC SftpConnectDialog.java:203 shows new GetSshHostFingerprintTask(hostname, port, taskResult -> { ... })')

e('SftpConnectDialog.lambda$onCreateDialog$9', 'SftpConnectDialog.lambda$null$8', 'CALL',
  'Lambda callback when host fingerprint is retrieved (no stored key)',
  evidence='SRC SftpConnectDialog.java:203 shows taskResult -> { ... } lambda')


# SftpConnectDialog.lambda$null$2 - callback after connection removal (edit mode with host key)

e('SftpConnectDialog.lambda$null$2', 'GetSshHostFingerprintTask.<init>', 'CALL',
  'Lambda creates task to verify host fingerprint',
  evidence='SRC SftpConnectDialog.java:181 shows new GetSshHostFingerprintTask(hostname, port, taskResult -> { ... })')

e('SftpConnectDialog.lambda$null$2', 'SftpConnectDialog.lambda$null$4', 'CALL',
  'Lambda callback when host fingerprint is retrieved',
  evidence='SRC SftpConnectDialog.java:181 shows taskResult -> { ... } lambda')


# SftpConnectDialog.lambda$null$4 - host fingerprint callback (edit mode)



e('SftpConnectDialog.lambda$null$4', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'Lambda calls authenticateAndSaveSetup if fingerprints match',
  evidence='SRC SftpConnectDialog.java:186 shows authenticateAndSaveSetup(...)')





e('SftpConnectDialog.lambda$null$4', 'SftpConnectDialog.lambda$null$5', 'CALL',
  'Lambda callback to update host key',
  evidence='SRC SftpConnectDialog.java:191 shows (dialog1, which1) -> { authenticateAndSaveSetup(...) }')


e('SftpConnectDialog.lambda$null$4', 'SftpConnectDialog.lambda$null$3', 'CALL',
  'Lambda callback to dismiss dialog',
  evidence='SRC SftpConnectDialog.java:195 shows (dialog1, which1) -> dialog1.dismiss()')


# SftpConnectDialog.lambda$null$5 - update host key callback

e('SftpConnectDialog.lambda$null$5', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'Lambda calls authenticateAndSaveSetup with new fingerprint',
  evidence='SRC SftpConnectDialog.java:192 shows authenticateAndSaveSetup(connectionName, hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPairName, selectedParsedKeyPair, edit)')

# SftpConnectDialog.lambda$null$3 - dismiss dialog callback


# SftpConnectDialog.lambda$null$8 - host fingerprint callback (new connection)












e('SftpConnectDialog.lambda$null$8', 'SftpConnectDialog.lambda$null$6', 'CALL',
  'Lambda callback when user accepts host key',
  evidence='SRC SftpConnectDialog.java:218 shows (dialog1, which1) -> { ... } lambda')


e('SftpConnectDialog.lambda$null$8', 'SftpConnectDialog.lambda$null$7', 'CALL',
  'Lambda callback when user rejects host key',
  evidence='SRC SftpConnectDialog.java:227 shows (dialog1, which1) -> dialog1.dismiss()')


# SftpConnectDialog.lambda$null$6 - accept host key callback


e('SftpConnectDialog.lambda$null$6', 'SftpConnectDialog.authenticateAndSaveSetup', 'CALL',
  'Lambda calls authenticateAndSaveSetup after accepting host key',
  evidence='SRC SftpConnectDialog.java:221 shows authenticateAndSaveSetup(...)')



# SftpConnectDialog.lambda$null$7 - reject host key callback


# SftpConnectDialog.lambda$onCreateDialog$10 - cancel button callback


# SftpConnectDialog.lambda$onCreateDialog$12 - negative button callback (edit mode - delete)




e('SftpConnectDialog.lambda$onCreateDialog$12', 'SshClientUtils.deriveSftpPathFrom', 'CALL',
  'Lambda derives SFTP path for deletion',
  evidence='SRC SftpConnectDialog.java:242 shows deriveSftpPathFrom(hostname, port, username, getArguments().getString("password", null), selectedParsedKeyPair)')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.getInstance', 'CALL',
  'Lambda gets DataUtils singleton',
  evidence='SRC SftpConnectDialog.java:244 shows DataUtils.getInstance().containsServer(...)')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.containsServer(String[])', 'CALL',
  'Lambda checks if server exists in data',
  evidence='SRC SftpConnectDialog.java:244 shows DataUtils.getInstance().containsServer(new String[]{connectionName, path})')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'DataUtils.removeServer', 'CALL',
  'Lambda removes server from data',
  evidence='SRC SftpConnectDialog.java:247 shows DataUtils.getInstance().removeServer(i)')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'AppConfig.runInBackground', 'CALL',
  'Lambda runs database removal in background',
  evidence='SRC SftpConnectDialog.java:249 shows AppConfig.runInBackground(() -> { ... })')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'CALL',
  'Lambda callback for background database removal',
  evidence='SRC SftpConnectDialog.java:249 shows () -> { utilsHandler.removeFromDatabase(...) }')

e('SftpConnectDialog.lambda$onCreateDialog$12', 'MainActivity.getDrawer', 'CALL',
  'Lambda gets drawer reference',
  evidence='SRC SftpConnectDialog.java:253 shows ((MainActivity) getActivity()).getDrawer().refreshDrawer()')



# SftpConnectDialog.lambda$authenticateAndSaveSetup$15 - background database removal

e('SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'UtilsHandler.removeFromDatabase', 'CALL',
  'Lambda removes SFTP connection from database',
  evidence='SRC SftpConnectDialog.java:250 shows utilsHandler.removeFromDatabase(new OperationData(UtilsHandler.Operation.SFTP, path, connectionName, null, null, null))')

e('SftpConnectDialog.lambda$authenticateAndSaveSetup$15', 'OperationData.<init>(Operation,String,String,String,String,String)', 'CALL',
  'Lambda creates OperationData for deletion',
  evidence='SRC SftpConnectDialog.java:250 shows new OperationData(UtilsHandler.Operation.SFTP, path, connectionName, null, null, null)')

# SftpConnectDialog.lambda$onCreateDialog$13 - neutral button callback (edit mode - cancel)


# SftpConnectDialog.onActivityResult - handles PEM file selection result





e('SftpConnectDialog.onActivityResult', 'PemToKeyPairTask.<init>(InputStream,Callback)', 'CALL',
  'onActivityResult creates task to parse PEM file',
  evidence='SRC SftpConnectDialog.java:331 shows new PemToKeyPairTask(selectedKeyContent, result -> { ... })')

e('SftpConnectDialog.onActivityResult', 'SftpConnectDialog.lambda$onActivityResult$14', 'FRAMEWORK',
  'Lambda callback when PEM is parsed',
  evidence='SRC SftpConnectDialog.java:331 shows result -> { ... } lambda')



# SftpConnectDialog.lambda$onActivityResult$14 - PEM parsed callback










# SftpConnectDialog.authenticateAndSaveSetup - main connection setup method

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.deriveSftpPathFrom', 'CALL',
  'authenticateAndSaveSetup derives SFTP path',
  evidence='SRC SftpConnectDialog.java:355 shows final String path = deriveSftpPathFrom(hostname, port, username, password, selectedParsedKeyPair)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshClientUtils.encryptSshPathAsNecessary', 'CALL',
  'authenticateAndSaveSetup encrypts path for storage',
  evidence='SRC SftpConnectDialog.java:357 shows final String encryptedPath = SshClientUtils.encryptSshPathAsNecessary(path)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshConnectionPool.getInstance', 'CALL',
  'authenticateAndSaveSetup gets connection pool singleton',
  evidence='SRC SftpConnectDialog.java:361 shows SSHClient result = SshConnectionPool.getInstance().getConnection(...)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SshConnectionPool.getConnection(String,int,String,String,String,KeyPair)', 'CALL',
  'authenticateAndSaveSetup gets SSH connection',
  evidence='SRC SftpConnectDialog.java:361 shows SshConnectionPool.getInstance().getConnection(hostname, port, hostKeyFingerprint, username, password, selectedParsedKeyPair)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.getInstance', 'CALL',
  'authenticateAndSaveSetup gets DataUtils singleton',
  evidence='SRC SftpConnectDialog.java:365 shows DataUtils.getInstance().containsServer(path)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.containsServer(String)', 'CALL',
  'authenticateAndSaveSetup checks if server already exists',
  evidence='SRC SftpConnectDialog.java:365 shows DataUtils.getInstance().containsServer(path)')

e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.addServer', 'CALL',
  'authenticateAndSaveSetup adds server to data',
  evidence='SRC SftpConnectDialog.java:366 shows DataUtils.getInstance().addServer(new String[]{connectionName, path})')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainActivity.getDrawer', 'CALL',
  'authenticateAndSaveSetup gets drawer reference',
  evidence='SRC SftpConnectDialog.java:367 shows ((MainActivity) getActivity()).getDrawer().refreshDrawer()')


e('SftpConnectDialog.authenticateAndSaveSetup', 'UtilsHandler.saveToDatabase', 'CALL',
  'authenticateAndSaveSetup saves connection to database',
  evidence='SRC SftpConnectDialog.java:369 shows utilsHandler.saveToDatabase(new OperationData(...))')

e('SftpConnectDialog.authenticateAndSaveSetup', 'OperationData.<init>(Operation,String,String,String,String,String)', 'CALL',
  'authenticateAndSaveSetup creates OperationData',
  evidence='SRC SftpConnectDialog.java:369 shows new OperationData(UtilsHandler.Operation.SFTP, encryptedPath, connectionName, hostKeyFingerprint, selectedParsedKeyPairName, getPemContents())')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SftpConnectDialog.getPemContents', 'CALL',
  'authenticateAndSaveSetup gets PEM file contents',
  evidence='SRC SftpConnectDialog.java:370 shows getPemContents()')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainActivity.getCurrentMainFragment', 'CALL',
  'authenticateAndSaveSetup gets current fragment',
  evidence='SRC SftpConnectDialog.java:372 shows MainFragment ma = ((MainActivity)getActivity()).getCurrentMainFragment()')

e('SftpConnectDialog.authenticateAndSaveSetup', 'MainFragment.loadlist', 'CALL',
  'authenticateAndSaveSetup loads SFTP directory',
  evidence='SRC SftpConnectDialog.java:373 shows ma.loadlist(path, false, OpenMode.SFTP)')









e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.removeServer', 'CALL',
  'authenticateAndSaveSetup removes old server entry in edit mode',
  evidence='SRC SftpConnectDialog.java:396 shows DataUtils.getInstance().removeServer(...)')


e('SftpConnectDialog.authenticateAndSaveSetup', 'DataUtils.getServers', 'CALL',
  'authenticateAndSaveSetup gets server list',
  evidence='SRC SftpConnectDialog.java:398 shows DataUtils.getInstance().getServers()')

e('SftpConnectDialog.authenticateAndSaveSetup', 'BookSorter.<init>', 'CALL',
  'authenticateAndSaveSetup creates BookSorter',
  evidence='SRC SftpConnectDialog.java:398 shows new BookSorter()')

e('SftpConnectDialog.authenticateAndSaveSetup', 'AppConfig.runInBackground', 'CALL',
  'authenticateAndSaveSetup updates database in background in edit mode',
  evidence='SRC SftpConnectDialog.java:401 shows AppConfig.runInBackground(() -> { utilsHandler.updateSsh(...) })')

e('SftpConnectDialog.authenticateAndSaveSetup', 'SftpConnectDialog.lambda$null$11', 'FRAMEWORK',
  'Lambda callback for background database update',
  evidence='SRC SftpConnectDialog.java:401 shows () -> { utilsHandler.updateSsh(...) }')


# SftpConnectDialog.lambda$null$11 - background database update

e('SftpConnectDialog.lambda$null$11', 'UtilsHandler.updateSsh', 'CALL',
  'Lambda updates SSH connection in database',
  evidence='SRC SftpConnectDialog.java:402 shows utilsHandler.updateSsh(connectionName, getArguments().getString("name"), encryptedPath, hostKeyFingerprint, selectedParsedKeyPairName, getPemContents())')

# SftpConnectDialog.getPemContents - reads PEM file contents









# SftpConnectDialog$1 - anonymous TextWatcher for input validation








# ShareAdapter methods - RecyclerView adapter for share dialog




e('ShareAdapter.onCreateViewHolder', 'ShareAdapter$ViewHolder.<init>', 'CALL',
  'onCreateViewHolder creates ViewHolder',
  evidence='SRC ShareAdapter.java:47 shows return new ViewHolder(view)')

e('ShareAdapter.onBindViewHolder', 'ShareAdapter$ViewHolder.render', 'CALL',
  'onBindViewHolder calls render on ViewHolder',
  evidence='SRC ShareAdapter.java:52 shows holder.render(position)')

e('ShareAdapter.getItemId', 'ShareAdapter.getItemCount', 'CALL',
  'getItemId simply returns position, no calls',
  evidence='SRC ShareAdapter.java:85 shows return position')


# ShareAdapter$ViewHolder methods








e('ShareAdapter$ViewHolder.render', 'ShareAdapter$ViewHolder.lambda$render$0', 'FRAMEWORK',
  'Lambda callback when item is clicked',
  evidence='SRC ShareAdapter.java:72 shows v -> { if (dialog != null && dialog.isShowing()) dialog.dismiss(); context.startActivity(items.get(position)); }')

# ShareAdapter$ViewHolder.lambda$render$0





# SimpleTextWatcher - abstract TextWatcher with empty implementations
# All three methods have empty implementations and are meant to be overridden

UNREACHABLE['SimpleTextWatcher.afterTextChanged'] = (
    'framework_never_calls',
    'SimpleTextWatcher is an abstract helper class with empty TextWatcher method implementations. The base implementation is never called directly; subclasses override it. This specific method in the base class has an empty body.',
    'SRC SimpleTextWatcher.java:21-23 shows @Override public void afterTextChanged(Editable s) { } with empty body',
    'SOURCE'
)

# SmbConnectDialog methods

e('SmbConnectDialog.onCreate', 'BasicActivity.getUtilsProvider', 'CALL',
  'onCreate gets utils provider',
  evidence='SRC SmbConnectDialog.java:70 shows utilsProvider = ((BasicActivity) getActivity()).getUtilsProvider()')














e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$1.<init>', 'CALL',
  'onCreateDialog creates anonymous SimpleTextWatcher for conName',
  evidence='SRC SmbConnectDialog.java:98 shows conName.addTextChangedListener(new SimpleTextWatcher() { ... })')

e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$2.<init>', 'CALL',
  'onCreateDialog creates anonymous SimpleTextWatcher for ip',
  evidence='SRC SmbConnectDialog.java:107 shows ip.addTextChangedListener(new SimpleTextWatcher() { ... })')

e('SmbConnectDialog.onCreateDialog', 'ThemedActivity.getAccent', 'CALL',
  'onCreateDialog gets accent color',
  evidence='SRC SmbConnectDialog.java:135 shows int accentColor = ((ThemedActivity) getActivity()).getAccent()')

e('SmbConnectDialog.onCreateDialog', 'EditTextColorStateUtil.setTint', 'CALL',
  'onCreateDialog sets tint on EditTexts',
  evidence='SRC SmbConnectDialog.java:140-142 shows three EditTextColorStateUtil.setTint calls')

e('SmbConnectDialog.onCreateDialog', 'Utils.setTint', 'CALL',
  'onCreateDialog sets tint on checkbox',
  evidence='SRC SmbConnectDialog.java:144 shows Utils.setTint(context, ch, accentColor)')







e('SmbConnectDialog.onCreateDialog', 'UtilitiesProvider.getAppTheme', 'CALL',
  'onCreateDialog gets app theme',
  evidence='SRC SmbConnectDialog.java:191 shows ba3.theme(utilsProvider.getAppTheme().getMaterialDialogTheme())')

e('SmbConnectDialog.onCreateDialog', 'AppTheme.getMaterialDialogTheme', 'CALL',
  'onCreateDialog gets material dialog theme',
  evidence='SRC SmbConnectDialog.java:191 shows utilsProvider.getAppTheme().getMaterialDialogTheme()')












# SmbConnectDialog helper methods - both UNREACHABLE (dead code)

UNREACHABLE['SmbConnectDialog.createEditTextColorStateList'] = (
    'no_trigger_in_app',
    'Static helper method called only by SmbConnectDialog.setTint, which is itself never called. Grep shows no calls to either method in app code.',
    'SRC SmbConnectDialog.java:311-323 shows private static ColorStateList createEditTextColorStateList(int color) definition. SRC line 328 shows it called only from setTint. Grep confirms no calls to SmbConnectDialog.setTint anywhere',
    'SOURCE'
)

UNREACHABLE['SmbConnectDialog.setTint'] = (
    'no_trigger_in_app',
    'Static helper method never called in app. The app uses EditTextColorStateUtil.setTint and Utils.setTint instead.',
    'SRC SmbConnectDialog.java:327-333 shows private static void setTint(EditText editText, int color) definition. SRC lines 157-159 show EditTextColorStateUtil.setTint calls, not SmbConnectDialog.setTint. Grep confirms no calls to this method',
    'SOURCE'
)

# SmbConnectDialog$1 - TextWatcher for conName





# SmbConnectDialog$2 - TextWatcher for ip





# ---- part repair_rp34 (2024-10-28, converted and filtered)
# Repair batch 34: Extra round 1 (converted from EDGES list format and filtered)
# Generated by convert_filter_rp34.py

e('SshAuthenticationTask.onPostExecute', 'SshAuthenticationTask.lambda$onPostExecute$0', 'CALL',
  'onPostExecute creates lambda for AlertDialog positive button callback',
  evidence='SRC SshAuthenticationTask.java:180: .setPositiveButton(R.string.ok, (dialog, which) -> dialog.dismiss()).show();')

e('SshAuthenticationTask.doInBackground', 'SshAuthenticationTask$1.<init>', 'CALL',
  'doInBackground creates anonymous KeyProvider for key-based authentication',
  evidence='SRC SshAuthenticationTask.java:130: sshClient.authPublickey(username, new KeyProvider() {...});')

e('SshAuthenticationTask$1.getType', 'SshAuthenticationTask$1.getPublic', 'CALL',
  'Calls getPublic to obtain public key for type determination',
  evidence='SRC SshAuthenticationTask.java:141: return KeyType.fromKey(getPublic());')

e('SshConnectionPool.expungeAllConnections', 'SshConnectionPool.lambda$expungeAllConnections$0', 'CALL',
  'expungeAllConnections runs lambda in background thread to close connections',
  evidence='SRC SshConnectionPool.java:181: AppConfig.runInBackground(() -> { ... });')

e('SshConnectionPool.lambda$expungeAllConnections$0', 'SshClientUtils.tryDisconnect', 'CALL',
  'Lambda disconnects each SSHClient in the connection pool',
  evidence='SRC SshConnectionPool.java:183-184: for (SSHClient connection : connections.values()) { SshClientUtils.tryDisconnect(connection); }')

e('SubnetScanner.run', 'SubnetScanner.onFound', 'CALL',
  'run calls onFound when a computer is discovered to notify observer',
  evidence='SRC SubnetScanner.java:125,168: onFound(computer) called from run method when computer is found')

UNREACHABLE['StreamSource.getFile'] = (
    'no_trigger_in_app',
    'StreamSource.getFile is a getter method that returns the SmbFile field. However, StreamSource is only used internally by StreamServer (see StreamServer.java:52-89 where StreamSource is created and used). The getFile method is never called from app code. Grep shows no callers.',
    'SRC StreamSource.java:115-117: public SmbFile getFile(){ return file; }',
    'INFERRED'
)

UNREACHABLE['StreamSource.getName'] = (
    'no_trigger_in_app',
    'StreamSource.getName is a getter that returns the file name. StreamSource is only instantiated in StreamServer.lambda$new$0 (line 53), and getName is never called from app code. The HTTP streaming uses read() methods, not getName.',
    'SRC StreamSource.java:111-113: public String getName(){ return name; }',
    'INFERRED'
)

UNREACHABLE['SubnetScanner.getResults'] = (
    'no_trigger_in_app',
    'SubnetScanner.getResults returns the list of discovered computers. However, this method is never called from app code. The SmbSearchDialog creates a SubnetScanner and uses its ScanObserver callbacks (computerFound, searchFinished) to receive results, not getResults. Grep shows no callers of getResults.',
    'SRC SubnetScanner.java:187-189: public List<ComputerParcelable> getResults() { return new ArrayList<>(this.mResults); }',
    'INFERRED'
)


# ---- part repair_rp35 (2024-10-28)
# Repair batch 35 - AmazeFileManager
# Generated: 2025-01-20 22:48
# All methods from rp_35.txt checked

# Utils.<init> - Utility class constructor, never instantiated
UNREACHABLE['Utils.<init>'] = (
    'no_trigger_in_app',
    'Utility class with only static methods (clamp, getViewRawY, setTint, getDate, getColor, dpToPx, differenceStrings, disableScreenRotation, etc.); constructor never instantiated in app source',
    'SRC utils/Utils.java:59 public class Utils { ... public static float clamp... public static float getViewRawY... public static void setTint... (all methods are static, no instance methods)',
    'SOURCE'
)

# GREP PROOF for Utils.<init> being unreachable:
# Command: grep -rn "new Utils()" app/src/main/java --include="*.java"
# Result: No matches found (no instantiations in app code)
# The class at utils/Utils.java:59-300+ contains only static methods and private static constants.
# No calls to new Utils() exist in the application source.

# ---- part final_label_batch_01 (2024-10-28)
# Batch 01 output - generated by slot_1 helper
# Date: 2026-10-28 23:34

# AppDataParcelable$AppDataSorter.compare - REACHABLE via Collections.sort
e('AppListLoader.loadInBackground', 'AppDataParcelable$AppDataSorter.compare', 'FRAMEWORK',
  'Collections.sort calls Comparator.compare on the AppDataSorter instance',
  evidence='SRC AppListLoader.java:79 "Collections.sort(mApps.first, new AppDataParcelable.AppDataSorter(sortBy, asc));"')

# CloudIconModelLoader - REACHABLE via Glide
e('AmazeFileManagerModule.registerComponents', 'CloudIconModelFactory.<init>', 'CALL',
  'AmazeFileManagerModule registers CloudIconModelFactory with Glide',
  evidence='SRC AmazeFileManagerModule.java:22 "registry.prepend(String.class, Bitmap.class, new CloudIconModelFactory(context));"')

e('CloudIconModelFactory.<init>', 'CloudIconModelFactory.build', 'FRAMEWORK',
  'Glide calls ModelLoaderFactory.build to create the ModelLoader',
  evidence='INFERRED Glide source not read')

e('CloudIconModelFactory.build', 'CloudIconModelLoader.<init>', 'CALL',
  'CloudIconModelFactory.build creates CloudIconModelLoader',
  evidence='SRC CloudIconModelFactory.java:23-24 "return new CloudIconModelLoader(context);"')

e('CloudIconModelLoader.<init>', 'CloudIconModelLoader.buildLoadData', 'FRAMEWORK',
  'Glide calls ModelLoader.buildLoadData when loading an image',
  evidence='INFERRED Glide source not read')

e('CloudIconModelLoader.<init>', 'CloudIconModelLoader.handles', 'FRAMEWORK',
  'Glide calls ModelLoader.handles to check if this loader can handle a model',
  evidence='SRC CloudIconModelLoader.java:35-41; INFERRED Glide source not read')

# CloudUtil$1 AsyncTask
e('CloudUtil.checkToken', 'CloudUtil$1.doInBackground', 'ASYNC',
  'CloudUtil.checkToken creates and executes the AsyncTask',
  evidence='SRC CloudUtil.java:174 "new AsyncTask<String, Void, Boolean>()", 248 ".execute(path);"')

e('CloudUtil$1.doInBackground', 'CloudUtil$1.onPostExecute', 'ASYNC',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='INFERRED AsyncTask dispatch')

# ColorAdapter
e('ColorAdapter.<init>', 'ColorAdapter.getView', 'FRAMEWORK',
  'ListView/GridView framework calls ArrayAdapter.getView to render items',
  evidence='SRC ColorAdapter.java:47-63, ColorPref.java:136 "ColorAdapter adapter = new ColorAdapter(...)"; INFERRED ArrayAdapter getView dispatch')

e('ColorAdapter.<init>', 'ColorAdapter.onItemClick', 'FRAMEWORK',
  'ColorAdapter implements AdapterView.OnItemClickListener; framework calls onItemClick when item tapped',
  evidence='SRC ColorAdapter.java:18, 66-70; INFERRED AdapterView dispatch')

# ColorCircleDrawable
e('ColorCircleDrawable.<init>', 'ColorCircleDrawable.draw', 'FRAMEWORK',
  'View framework calls Drawable.draw to render',
  evidence='SRC ColorCircleDrawable.java:43-46, TabFragment.java:386 "new ColorCircleDrawable(accentColor)"; INFERRED Drawable.draw dispatch')

e('ColorCircleDrawable.<init>', 'ColorCircleDrawable.getOpacity', 'FRAMEWORK',
  'Framework calls Drawable.getOpacity to determine transparency',
  evidence='INFERRED Drawable framework dispatch')

e('ColorCircleDrawable.<init>', 'ColorCircleDrawable.onBoundsChange', 'FRAMEWORK',
  'Framework calls Drawable.onBoundsChange when bounds change',
  evidence='INFERRED Drawable framework dispatch')

e('ColorCircleDrawable.<init>', 'ColorCircleDrawable.setAlpha', 'FRAMEWORK',
  'Framework or app code calls Drawable.setAlpha to set transparency',
  evidence='INFERRED Drawable framework dispatch')

e('ColorCircleDrawable.<init>', 'ColorCircleDrawable.setColorFilter', 'FRAMEWORK',
  'Framework or app code calls Drawable.setColorFilter',
  evidence='INFERRED Drawable framework dispatch')

# ColorPickerDialog and SavedState
e('ColorPickerDialog.<init>', 'ColorPickerDialog.onSaveInstanceState', 'LIFECYCLE',
  'Framework calls preference onSaveInstanceState when saving state',
  evidence='INFERRED Preference lifecycle dispatch')

e('ColorPickerDialog.onSaveInstanceState', 'ColorPickerDialog$SavedState.<init>(Parcelable)', 'CALL',
  'onSaveInstanceState creates SavedState',
  evidence='SRC ColorPickerDialog.java:258 "new SavedState(super.onSaveInstanceState());"')

e('ColorPickerDialog$SavedState.<init>(Parcelable)', 'ColorPickerDialog$SavedState.writeToParcel', 'FRAMEWORK',
  'Framework calls writeToParcel when marshalling the saved state',
  evidence='INFERRED Parcelable framework dispatch')

e('ColorPickerDialog.<init>', 'ColorPickerDialog.onRestoreInstanceState', 'LIFECYCLE',
  'Framework calls preference onRestoreInstanceState when restoring state',
  evidence='INFERRED Preference lifecycle dispatch')

e('ColorPickerDialog.onRestoreInstanceState', 'ColorPickerDialog$SavedState$1.createFromParcel', 'FRAMEWORK',
  'Framework calls CREATOR.createFromParcel when unmarshalling SavedState',
  evidence='SRC ColorPickerDialog.java:267-272, 292-297; INFERRED Parcelable framework dispatch')

e('ColorPickerDialog$SavedState$1.createFromParcel', 'ColorPickerDialog$SavedState.<init>(Parcel)', 'CALL',
  'createFromParcel calls the Parcel constructor',
  evidence='SRC ColorPickerDialog.java:294 "return new SavedState(in);"')

e('ColorPickerDialog$SavedState$1.<init>', 'ColorPickerDialog$SavedState$1.newArray', 'FRAMEWORK',
  'Framework calls Creator.newArray during unmarshalling',
  evidence='INFERRED Parcelable framework dispatch')

# ColorPref
e('ColorPref.<init>', 'ColorPref.onCreate', 'LIFECYCLE',
  'Framework calls PreferenceFragment.onCreate',
  evidence='SRC ColorPref.java:54-64; INFERRED Fragment lifecycle dispatch')

e('ColorPref.onCreate', 'ColorPref.onPreferenceClick', 'FRAMEWORK',
  'ColorPref implements OnPreferenceClickListener; framework calls when preference clicked',
  evidence='SRC ColorPref.java:33, 97-119; INFERRED Preference click dispatch')

e('ColorPref.<init>', 'ColorPref.onOptionsItemSelected', 'LIFECYCLE',
  'Framework calls Fragment.onOptionsItemSelected when options menu item selected',
  evidence='INFERRED Fragment menu dispatch')

# CopyService$DoInBackground
e('CopyService$DoInBackground.doInBackground', 'CopyService$DoInBackground.onPostExecute', 'ASYNC',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='INFERRED AsyncTask dispatch')

# CustomNavigationView and SavedState








# DataUtils$DataUtilsHolder
e('DataUtils.getInstance', 'DataUtils$DataUtilsHolder.<init>', 'CALL',
  'DataUtils.getInstance accesses DataUtilsHolder.INSTANCE, triggering static initialization',
  evidence='SRC DataUtils.java:78-80, 82-84 "return DataUtilsHolder.INSTANCE;"; INFERRED static initialization')

# DecryptService$BackgroundTask
e('DecryptService$BackgroundTask.doInBackground', 'DecryptService$BackgroundTask.onPostExecute', 'ASYNC',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='INFERRED AsyncTask dispatch')

# DisablableViewPager
# (no new edges needed; <init> is enough)

# DividerItemDecoration
e('DividerItemDecoration.<init>', 'DividerItemDecoration.onDraw', 'FRAMEWORK',
  'RecyclerView calls ItemDecoration.onDraw to draw decorations',
  evidence='INFERRED RecyclerView.ItemDecoration dispatch')

e('DividerItemDecoration.<init>', 'DividerItemDecoration.getItemOffsets', 'FRAMEWORK',
  'RecyclerView calls ItemDecoration.getItemOffsets to compute item offsets',
  evidence='INFERRED RecyclerView.ItemDecoration dispatch')

# DonationViewHolder
# (no new edges needed; <init> is enough)

# UNREACHABLE assignments
UNREACHABLE['AppDataParcelable$1.createFromParcel'] = ('no_trigger_in_app', 'AppDataParcelable.CREATOR.createFromParcel is called by the framework only when unmarshalling a Parcelable from an Intent or Bundle. grep shows no putParcelable or getParcelable* calls for AppDataParcelable in the app; the class is used only in-memory', 'SRC AppDataParcelable.java:55-60, grep -rn "putParcelable\\|getParcelableExtra\\|getParcelable" returns no AppDataParcelable usage', 'SOURCE')

# Parcelable.Creator UNREACHABLE entries from blocker_props_1.md (S_PARCEL_read blockers)

UNREACHABLE['PasteHelper$1.newArray'] = ('framework_never_calls', 'PasteHelper.CREATOR.newArray is never invoked; PasteHelper is parceled one object at a time (MainActivity.java:425 getParcelable, :1078 putParcelable), never as an array', 'grep over app/src/main/java for newArray( and for readTypedArray, createTypedArray, readParcelableArray and getParcelableArray finds no PasteHelper[] read; PasteHelper.java:28 reads HybridFileParcelable[] only', 'SOURCE')

UNREACHABLE['UserColorPreferences$1.createFromParcel'] = ('framework_never_calls', 'UserColorPreferences.CREATOR is never invoked; instances created only via constructor, never deserialized', 'grep over app/src/main/java shows zero deserialization call sites', 'SOURCE')

UNREACHABLE['UserColorPreferences$1.newArray'] = ('framework_never_calls', 'UserColorPreferences.CREATOR.newArray is never invoked; no array deserialization for this type', 'grep over app/src/main/java shows zero deserialization call sites', 'SOURCE')

UNREACHABLE['DatapointParcelable.describeContents'] = ('no_trigger_in_app', 'Parcelable.describeContents is called by the framework only when marshalling. grep shows no putParcelable calls for DatapointParcelable in the app; the class is used only in-memory for progress tracking', 'SRC DatapointParcelable.java:145-148, grep -rn "putParcelable.*Datapoint" returns no usage', 'SOURCE')

UNREACHABLE['DatapointParcelable.writeToParcel'] = ('no_trigger_in_app', 'Parcelable.writeToParcel is called by the framework only when marshalling. grep shows no putParcelable calls for DatapointParcelable in the app; the class is used only in-memory', 'SRC DatapointParcelable.java:150-159, grep -rn "putParcelable.*Datapoint" returns no usage', 'SOURCE')

# ---- part final_label_batch_02 (2024-10-28)
# Batch 02 label output
# Generated by slot 2 helper

# DummyFileGenerator.createFile
UNREACHABLE['DummyFileGenerator.createFile'] = ('no_trigger_in_app', 'Test-only utility method annotated @RestrictTo(RestrictTo.Scope.TESTS) and @VisibleForTesting(otherwise = VisibleForTesting.NONE); grep -rn over src/main/java finds no calls in the app', 'SRC utils/test/DummyFileGenerator.java:54-59', 'SOURCE')

# EditTextColorStateUtil.<init>
UNREACHABLE['EditTextColorStateUtil.<init>'] = ('no_trigger_in_app', 'Utility class with only static methods; no instantiation found in app (grep -rn "new EditTextColorStateUtil" finds nothing)', 'SRC utils/EditTextColorStateUtil.java:18-45', 'SOURCE')

# EncryptService$1.onReceive
e('EncryptService.onCreate', 'EncryptService$1.<init>', 'CALL', 'EncryptService.onCreate instantiates anonymous BroadcastReceiver cancelReceiver',
  evidence='SRC asynchronous/services/EncryptService.java:226 shows "private BroadcastReceiver cancelReceiver = new BroadcastReceiver()"')
e('EncryptService$1.<init>', 'EncryptService$1.onReceive', 'FRAMEWORK', 'Framework dispatches broadcast when user taps notification action or ProcessViewerFragment sends TAG_BROADCAST_CRYPT_CANCEL',
  evidence='SRC asynchronous/services/EncryptService.java:68 shows registerReceiver(cancelReceiver, new IntentFilter(TAG_BROADCAST_CRYPT_CANCEL)); line 92 shows stopIntent created with TAG_BROADCAST_CRYPT_CANCEL used in notification action; line 227-230 show onReceive method; FW-SRC core/java/android/app/ActivityThread.java (BroadcastReceiver dispatched by ActivityThread/LoadedApk)')

# MainFragment$2.getSpanSize
e('MainFragment.loadlist', 'MainFragment$2.<init>', 'CALL', 'MainFragment.loadlist creates anonymous GridLayoutManager.SpanSizeLookup',
  evidence='SRC fragments/MainFragment.java:341 shows "mLayoutManagerGrid.setSpanSizeLookup(new GridLayoutManager.SpanSizeLookup()"')
e('MainFragment$2.<init>', 'MainFragment$2.getSpanSize', 'FRAMEWORK', 'GridLayoutManager calls getSpanSize to determine span for each position',
  evidence='SRC fragments/MainFragment.java:342-349 shows @Override public int getSpanSize(int position) method; INFERRED GridLayoutManager dispatches to SpanSizeLookup (androidx source not read)')

# MainFragment$3.onActionItemClicked
e('RecyclerAdapter.toggleChecked(int,ImageView)', 'MainFragment$3.<init>', 'CALL', 'RecyclerAdapter creates action mode with MainFragment.mActionModeCallback',
  evidence='SRC adapters/RecyclerAdapter.java:192 shows "mainFrag.mActionMode = mainFrag.getMainActivity().startSupportActionMode(mainFrag.mActionModeCallback)"; fragments/MainFragment.java:461 shows "public ActionMode.Callback mActionModeCallback = new ActionMode.Callback()"')
e('MainFragment$3.<init>', 'MainFragment$3.onActionItemClicked', 'FRAMEWORK', 'Framework dispatches onActionItemClicked when user selects action mode menu item',
  evidence='SRC fragments/MainFragment.java:623 shows "public boolean onActionItemClicked(ActionMode mode, MenuItem item)"; INFERRED ActionMode dispatches menu item clicks to Callback (androidx source not read)')

# MainFragment$3.onCreateActionMode
e('MainFragment$3.<init>', 'MainFragment$3.onCreateActionMode', 'FRAMEWORK', 'Framework calls onCreateActionMode when action mode is created',
  evidence='SRC fragments/MainFragment.java:482 shows "public boolean onCreateActionMode(ActionMode mode, Menu menu)"; comment at line 481 says "called when the action mode is created"; INFERRED ActionMode.Callback lifecycle (androidx source not read)')

# MainFragment$3.onPrepareActionMode
e('MainFragment$3.<init>', 'MainFragment$3.onPrepareActionMode', 'FRAMEWORK', 'Framework calls onPrepareActionMode to refresh action mode menu before showing',
  evidence='SRC fragments/MainFragment.java:520 shows "public boolean onPrepareActionMode(ActionMode mode, Menu menu)"; INFERRED ActionMode.Callback lifecycle (androidx source not read)')

# MainFragment$4.onReceive
e('MainFragment.onResume', 'MainFragment$4.<init>', 'CALL', 'MainFragment.onResume creates and registers anonymous BroadcastReceiver receiver2',
  evidence='SRC fragments/MainFragment.java:776 shows "private BroadcastReceiver receiver2 = new BroadcastReceiver()"; line 1421 shows "(getActivity()).registerReceiver(receiver2, new IntentFilter(MainActivity.KEY_INTENT_LOAD_LIST))"')
e('MainFragment$4.<init>', 'MainFragment$4.onReceive', 'FRAMEWORK', 'Framework dispatches broadcast MainActivity.KEY_INTENT_LOAD_LIST to reload file list',
  evidence='SRC fragments/MainFragment.java:777-779 shows "@Override public void onReceive(Context context, Intent intent) // load the list on a load broadcast"; FW-SRC core/java/android/app/ActivityThread.java (BroadcastReceiver dispatched by ActivityThread/LoadedApk)')

# PrepareCopyTask$CopyNode.getConflictingFiles
UNREACHABLE['PrepareCopyTask$CopyNode.getConflictingFiles'] = ('no_trigger_in_app', 'Getter method never called; PrepareCopyTask.onEndDialog and other methods access field conflictingFiles directly (lines 237-240) instead of calling getter', 'SRC asynchronous/asynctasks/PrepareCopyTask.java:390-392', 'SOURCE')

# PrepareCopyTask$CopyNode.getFilesToCopy
UNREACHABLE['PrepareCopyTask$CopyNode.getFilesToCopy'] = ('no_trigger_in_app', 'Getter method never called; PrepareCopyTask.onEndDialog and other methods access field filesToCopy directly (lines 237-240) instead of calling getter', 'SRC asynchronous/asynctasks/PrepareCopyTask.java:386-388', 'SOURCE')

# RecyclerPreloadSizeProvider$SizeViewTarget.onResourceReady
UNREACHABLE['RecyclerPreloadSizeProvider$SizeViewTarget.onResourceReady'] = ('framework_never_calls', 'SizeViewTarget is created only to call getSize() for dimension measurement (line 73); no resource is loaded into this target so Glide never calls onResourceReady; method body is empty stub (line 78-80)', 'SRC adapters/glide/RecyclerPreloadSizeProvider.java:72-81', 'SOURCE')

# ScrimInsetsRelativeLayout.draw
UNREACHABLE['ScrimInsetsRelativeLayout.draw'] = ('no_trigger_in_app', 'ScrimInsetsRelativeLayout custom view is never used in app; grep -rn over src/main finds no XML layout references and no Java instantiation', 'SRC ui/views/ScrimInsetsRelativeLayout.java:82-113', 'SOURCE')

# ScrimInsetsRelativeLayout.fitSystemWindows
UNREACHABLE['ScrimInsetsRelativeLayout.fitSystemWindows'] = ('no_trigger_in_app', 'ScrimInsetsRelativeLayout custom view is never used in app; grep -rn over src/main finds no XML layout references and no Java instantiation', 'SRC ui/views/ScrimInsetsRelativeLayout.java:70-80', 'SOURCE')

# ScrimInsetsRelativeLayout.onAttachedToWindow
UNREACHABLE['ScrimInsetsRelativeLayout.onAttachedToWindow'] = ('no_trigger_in_app', 'ScrimInsetsRelativeLayout custom view is never used in app; grep -rn over src/main finds no XML layout references and no Java instantiation', 'SRC ui/views/ScrimInsetsRelativeLayout.java:116-122', 'SOURCE')

# ScrimInsetsRelativeLayout.onDetachedFromWindow
UNREACHABLE['ScrimInsetsRelativeLayout.onDetachedFromWindow'] = ('no_trigger_in_app', 'ScrimInsetsRelativeLayout custom view is never used in app; grep -rn over src/main finds no XML layout references and no Java instantiation', 'SRC ui/views/ScrimInsetsRelativeLayout.java:124-130', 'SOURCE')

# ScrimInsetsRelativeLayout.setOnInsetsCallback
UNREACHABLE['ScrimInsetsRelativeLayout.setOnInsetsCallback'] = ('no_trigger_in_app', 'ScrimInsetsRelativeLayout custom view is never used in app; grep -rn over src/main finds no XML layout references and no Java instantiation', 'SRC ui/views/ScrimInsetsRelativeLayout.java:137-139', 'SOURCE')

# ServiceWatcherUtil$1.run
e('ServiceWatcherUtil.watch', 'ServiceWatcherUtil$1.<init>', 'CALL', 'ServiceWatcherUtil.watch creates anonymous Runnable for progress monitoring',
  evidence='SRC utils/ServiceWatcherUtil.java:75 shows "runnable = new Runnable()"')
e('ServiceWatcherUtil$1.<init>', 'ServiceWatcherUtil$1.run', 'FRAMEWORK', 'Handler posts and dispatches Runnable on main thread',
  evidence='SRC utils/ServiceWatcherUtil.java:76-77 shows "@Override public void run()"; line 80 shows "handler.postDelayed(this, 1000)"; INFERRED Handler.post/postDelayed queues the Runnable on the handler thread')

# SftpConnectDialog.onActivityResult
e('CloudSheetFragment.onClick', 'SftpConnectDialog.<init>', 'CALL', 'CloudSheetFragment instantiates SftpConnectDialog to configure SFTP connection',
  evidence='SRC fragments/CloudSheetFragment.java:113 shows "SftpConnectDialog sftpConnectDialog = new SftpConnectDialog()"')
e('SftpConnectDialog.<init>', 'SftpConnectDialog.onCreate', 'LIFECYCLE', 'Framework calls DialogFragment.onCreate',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:74 declares "extends DialogFragment"; INFERRED FragmentManager drives fragment lifecycle callbacks')
e('SftpConnectDialog.onCreate', 'SftpConnectDialog.onCreateDialog', 'LIFECYCLE', 'Framework calls DialogFragment.onCreateDialog to create the dialog',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:123 shows "@Override public Dialog onCreateDialog(Bundle savedInstanceState)"; INFERRED DialogFragment lifecycle')
e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog.onActivityResult', 'RESULT', 'Framework delivers activity result when user picks SSH key file',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:334 shows startActivityForResult for ACTION_GET_CONTENT to pick key file; line 473 shows "@Override public void onActivityResult(int requestCode, int resultCode, Intent data)"; FW-SRC core/java/android/app/Activity.java (result delivered via ActivityThread.deliverResults)')

# ShareAdapter.getItemId
e('ShareTask.onPostExecute', 'ShareAdapter.<init>', 'CALL', 'MainActivityHelper.showSharingDialog creates ShareAdapter for share targets',
  evidence='SRC utils/MainActivityHelper.java:320 shows "new ShareAdapter(activity, (ArrayList<ResolveInfo>) listAll)"')
e('ShareAdapter.<init>', 'ShareAdapter.getItemId', 'FRAMEWORK', 'RecyclerView calls getItemId for stable IDs if hasStableIds is true',
  evidence='SRC utils/share/ShareAdapter.java:52 shows "@Override public long getItemId(int position)"; INFERRED RecyclerView.Adapter getItemId dispatch (androidx source not read)')

# ShareAdapter.onBindViewHolder
e('ShareAdapter.<init>', 'ShareAdapter.onBindViewHolder', 'FRAMEWORK', 'RecyclerView calls onBindViewHolder to bind data to ViewHolder',
  evidence='SRC utils/share/ShareAdapter.java:61 shows "@Override public void onBindViewHolder(final ShareAdapter.ViewHolder holder, int position)"; INFERRED RecyclerView.Adapter binding lifecycle (androidx source not read)')

# ShareAdapter.onCreateViewHolder
e('ShareAdapter.<init>', 'ShareAdapter.onCreateViewHolder', 'FRAMEWORK', 'RecyclerView calls onCreateViewHolder to create ViewHolder instances',
  evidence='SRC utils/share/ShareAdapter.java:47 shows "@Override public ShareAdapter.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType)"; INFERRED RecyclerView.Adapter creation lifecycle (androidx source not read)')

# SshAuthenticationTask$1.getPrivate
e('SshAuthenticationTask.doInBackground', 'SshAuthenticationTask$1.<init>', 'CALL', 'SshAuthenticationTask.doInBackground creates anonymous KeyPair wrapper',
  evidence='SRC asynchronous/asynctasks/ssh/SshAuthenticationTask.java:89 shows "KeyPair keyPair = new KeyPair()"')
e('SshAuthenticationTask$1.<init>', 'SshAuthenticationTask$1.getPrivate', 'CALL', 'SSHJ library calls getPrivate to retrieve private key for authentication',
  evidence='SRC asynchronous/asynctasks/ssh/SshAuthenticationTask.java:95 shows "public PrivateKey getPrivate()"; INFERRED SSHJ KeyProvider interface requires getPrivate method')

# SshAuthenticationTask$1.getType
e('SshAuthenticationTask$1.<init>', 'SshAuthenticationTask$1.getType', 'CALL', 'SSHJ library calls getType to determine key algorithm type',
  evidence='SRC asynchronous/asynctasks/ssh/SshAuthenticationTask.java:100 shows "public KeyType getType()"; INFERRED SSHJ KeyProvider interface requires getType method')

# SshAuthenticationTask.doInBackground
e('SshAuthenticationTask.<init>(String,int,String,String,String,KeyPair)', 'SshAuthenticationTask.doInBackground', 'ASYNC', 'AsyncTask.execute runs doInBackground on worker thread',
  evidence='SRC asynchronous/asynctasks/ssh/SshAuthenticationTask.java:107 shows "@Override protected AsyncTaskResult<SSHClient> doInBackground(Void... params)"; INFERRED AsyncTask lifecycle')

# SshAuthenticationTask.onPostExecute
e('SshAuthenticationTask.doInBackground', 'SshAuthenticationTask.onPostExecute', 'ASYNC', 'AsyncTask runs onPostExecute on main thread after doInBackground completes',
  evidence='SRC asynchronous/asynctasks/ssh/SshAuthenticationTask.java:146 shows "@Override protected void onPostExecute(AsyncTaskResult<SSHClient> result)"; INFERRED AsyncTask lifecycle')

# SshConnectionPool$AsyncRemoveConnection.doInBackground
e('SshConnectionPool.removeConnection', 'SshConnectionPool$AsyncRemoveConnection.<init>', 'CALL', 'SshConnectionPool.shutdown creates AsyncRemoveConnection task to close SSH connections',
  evidence='SRC filesystem/ssh/SshConnectionPool.java:165 shows "new AsyncRemoveConnection().execute()"')
e('SshConnectionPool$AsyncRemoveConnection.<init>', 'SshConnectionPool$AsyncRemoveConnection.doInBackground', 'ASYNC', 'AsyncTask.execute runs doInBackground on worker thread',
  evidence='SRC filesystem/ssh/SshConnectionPool.java:218 shows "@Override protected Void doInBackground(Void... params)"; INFERRED AsyncTask lifecycle')

# SubnetScanner$1.run
e('SubnetScanner.run', 'SubnetScanner$1.<init>', 'CALL', 'SubnetScanner.run creates anonymous Runnable for device discovery callback',
  evidence='SRC utils/SubnetScanner.java:84 shows "new Runnable()"')
e('SubnetScanner$1.<init>', 'SubnetScanner$1.run', 'FRAMEWORK', 'Handler posts Runnable to main thread when device is discovered',
  evidence='SRC utils/SubnetScanner.java:85-86 shows "@Override public void run()"; line 83 shows "handler.post(new Runnable())"; INFERRED Handler.post dispatches on handler thread')

# SubnetScanner$Task.call
e('SubnetScanner.run', 'SubnetScanner$Task.<init>', 'CALL', 'SubnetScanner.run creates Task instances for each IP to scan',
  evidence='SRC utils/SubnetScanner.java:67 shows "task = new Task(ipAddress, portNum)"')
e('SubnetScanner$Task.<init>', 'SubnetScanner$Task.call', 'ASYNC', 'ExecutorService invokes Callable.call on worker thread',
  evidence='SRC utils/SubnetScanner.java:73 shows "Future<ComputerParcelable> future = es.submit(task)"; line 115 shows "public ComputerParcelable call()"; INFERRED ExecutorService.submit executes Callable.call')

# SubnetScanner.run
e('SmbSearchDialog.onCreateDialog', 'SubnetScanner.<init>', 'CALL', 'MainActivityHelper.searchLocal creates SubnetScanner for network scanning',
  evidence='SRC utils/MainActivityHelper.java:415 shows "SubnetScanner ss = new SubnetScanner(context)"')
e('SubnetScanner.<init>', 'SubnetScanner.run', 'FRAMEWORK', 'ExecutorService dispatches Runnable.run on worker thread',
  evidence='SRC utils/SubnetScanner.java:58 shows "public void run()"; utils/MainActivityHelper.java:416 shows "executor.execute(ss)"; INFERRED ExecutorService.execute runs Runnable on worker thread')

# ---- part final_label_batch_03 (2024-10-28)
# Batch 03 output - READ-ONLY helper slot 3
# Generated: 2024-10-28 23:35

# Method 1: TabFragment.onPageSelected
e('TabFragment.onCreateView', 'TabFragment.onPageSelected', 'LIFECYCLE',
  'ViewPager.OnPageChangeListener callback registered at line 102',
  evidence='SRC TabFragment.java:102 addOnPageChangeListener(this); TabFragment implements ViewPager.OnPageChangeListener (line 45); framework callback dispatch is INFERRED (ViewPager is support library, source not in fw_src)')

# Method 2: ThemedTextView.<init>
e('RecyclerAdapter.onCreateViewHolder', 'ThemedTextView.<init>', 'FRAMEWORK',
  'View constructor called during layout inflation',
  evidence='SRC RecyclerAdapter.java:467 mInflater.inflate(R.layout.rowlayout, parent, false); rowlayout.xml contains ThemedTextView; FW-SRC LayoutInflater.java:647 constructor.newInstance(args) calls View(Context, AttributeSet) constructor')

# Method 3: UsbOtgRepresentation.equals
UNREACHABLE['UsbOtgRepresentation.equals'] = (
    'no_trigger_in_app',
    'Object.equals() override never called: grep over app source shows no .equals() calls on UsbOtgRepresentation objects, and the List<UsbOtgRepresentation> usage only calls isEmpty() and get(0), never contains/remove/indexOf or other collection methods that would invoke equals()',
    'SRC MainActivity.java:1134-1151 (List operations: isEmpty(), get(0) only); OTGUtil.java:131-147 (returns ArrayList); SingletonUsbOtg.java:42-44 (uses hashCode(), not equals())',
    'SOURCE'
)

# Method 4: WarnableTextInputLayout.<init>
e('GeneralDialogCreation.showEncryptAuthenticateDialog', 'WarnableTextInputLayout.<init>', 'FRAMEWORK',
  'View constructor called during layout inflation',
  evidence='SRC GeneralDialogCreation.java:723 View.inflate(c, R.layout.dialog_encrypt_authenticate, null); dialog_encrypt_authenticate.xml contains WarnableTextInputLayout; FW-SRC LayoutInflater.java:647 constructor.newInstance(args) calls View(Context, AttributeSet) constructor')

# --- labelling run 2026-10-29: PasteHelper CREATOR is reached through the saved activity state ---
ENV_PASTE_RECREATE = env_text('the system recreates MainActivity with its saved state after a configuration change or process restore', ('system_event',))
NEED_PASTE_OP = state_text('A copy or cut operation is pending (MainActivity holds a PasteHelper)', ('session',))

e('ItemPopupMenu.onMenuItemClick', 'PasteHelper.<clinit>', 'CALL',
  'the first new PasteHelper(...) in the copy or cut menu item initializes the class, which runs the static initializer',
  evidence='SRC ui/ItemPopupMenu.java:103-104 PasteHelper pasteHelper = new PasteHelper(op, ...)')

e('PasteHelper.<clinit>', 'PasteHelper$1.<init>', 'CALL',
  'the static initializer constructs the anonymous Parcelable.Creator assigned to CREATOR',
  evidence='SRC filesystem/PasteHelper.java:42 public static final Parcelable.Creator CREATOR = new Parcelable.Creator() {')

e('MainActivity.onSaveInstanceState', 'PasteHelper.writeToParcel', 'FRAMEWORK',
  'onSaveInstanceState puts the pending PasteHelper into outState; the Bundle parcels it through writeToParcel when the state is saved',
  needs_state=NEED_PASTE_OP,
  evidence='SRC activities/MainActivity.java:1077-1078 if(pasteHelper != null) outState.putParcelable(PASTEHELPER_BUNDLE, pasteHelper); INFERRED Bundle parcels the value on save')

e('MainActivity$1.onPostExecute', 'PasteHelper$1.createFromParcel', 'FRAMEWORK',
  'after a recreate with a saved state, the callback reads PASTEHELPER_BUNDLE; Bundle.getParcelable unparcels the PasteHelper through CREATOR.createFromParcel',
  needs_state=NEED_PASTE_OP, env=ENV_PASTE_RECREATE,
  evidence='SRC activities/MainActivity.java:425 pasteHelper = savedInstanceState.getParcelable(PASTEHELPER_BUNDLE); INFERRED Bundle.getParcelable calls CREATOR.createFromParcel')

e('ProcessViewerFragment.onResume', 'ProcessViewerFragment$CustomServiceConnection.onServiceDisconnected', 'FRAMEWORK', 'bindService registers CustomServiceConnection as ServiceConnection; framework calls onServiceDisconnected if the bound service connection is lost', evidence='SRC fragments/ProcessViewerFragment.java:158-159 Intent intent = new Intent(getActivity(), CopyService.class); getActivity().bindService(intent, mCopyConnection, 0)')
e('TabFragment.onCreateView', 'TabFragment$ScreenSlidePagerAdapter.getCount', 'FRAMEWORK', 'ViewPager framework calls PagerAdapter.getCount after setAdapter is called', evidence='SRC fragments/TabFragment.java:145 mViewPager.setAdapter(mSectionsPagerAdapter)')
e('TabFragment.onCreateView', 'TabFragment$ScreenSlidePagerAdapter.getItem', 'FRAMEWORK', 'FragmentStatePagerAdapter.getItem is called by the ViewPager framework after setAdapter is called', evidence='SRC fragments/TabFragment.java:145 mViewPager.setAdapter(mSectionsPagerAdapter)')
e('TabFragment.onCreateView', 'TabFragment$ScreenSlidePagerAdapter.getItemPosition', 'FRAMEWORK', 'PagerAdapter.getItemPosition is called by the ViewPager framework via notifyDataSetChanged', evidence='SRC fragments/TabFragment.java:175 mSectionsPagerAdapter.notifyDataSetChanged()')
e('ColorPref.<init>', 'ColorPref.onPause', 'LIFECYCLE', 'PreferenceFragment.onPause lifecycle callback', evidence='SRC fragments/preference_fragments/ColorPref.java:68-71 @Override public void onPause() { if (dialog != null) dialog.dismiss(); super.onPause(); }')
e('ColorPref.<init>', 'ColorPref.onSaveInstanceState', 'LIFECYCLE', 'Fragment.onSaveInstanceState lifecycle callback', evidence='SRC fragments/preference_fragments/ColorPref.java:295-299 @Override public void onSaveInstanceState(Bundle outState)')
e('ColorPref.colorChangeDialog', 'ColorPref$1.onNeutral', 'FRAMEWORK', 'MaterialDialog built with .callback(new MaterialDialog.ButtonCallback(){onNeutral...}) and shown with .show(); framework invokes onNeutral when user taps the neutral/default button', evidence='SRC fragments/preference_fragments/ColorPref.java:171-187 dialog = new MaterialDialog.Builder(...).callback(new MaterialDialog.ButtonCallback(){ public void onNeutral(MaterialDialog dialog) {...} }) ... .show()')
e('PreferencesActivity.selectItem', 'QuickAccessPref.onCreate', 'LIFECYCLE', 'selectItem constructs QuickAccessPref and commits a FragmentTransaction via loadPrefFragment, which causes the framework to call Fragment.onCreate', evidence='SRC activities/PreferencesActivity.java:264 loadPrefFragment(new QuickAccessPref(), R.string.sidebar_quick_access_title); PreferencesActivity.java:272-278 loadPrefFragment: FragmentTransaction t = ...; t.replace(...); t.commit();')
e('QuickAccessPref.onCreate', 'QuickAccessPref.onPreferenceClick', 'FRAMEWORK', 'onCreate registers this as OnPreferenceClickListener for every preference in the screen; framework invokes onPreferenceClick when one is tapped', evidence='SRC fragments/preference_fragments/QuickAccessPref.java:52-54 for (...) getPreferenceScreen().getPreference(i).setOnPreferenceClickListener(this);')
e('ColorPref.loadSection1', 'ColorPickerDialog.<init>', 'FRAMEWORK', 'loadSection1 inflates conficolor_prefs.xml which declares a ColorPickerDialog preference element; the Android PreferenceScreen inflater instantiates it via the (Context,AttributeSet) constructor', evidence='SRC fragments/preference_fragments/ColorPref.java:219 addPreferencesFromResource(R.xml.conficolor_prefs); res/xml/conficolor_prefs.xml:3-5 <com.amaze.filemanager.ui.dialogs.ColorPickerDialog android:key="preselectedconfigs" .../>')
e('RenameBookmark.onCreateDialog', 'RenameBookmark$1.afterTextChanged', 'FRAMEWORK', 'conName.addTextChangedListener registers an anonymous SimpleTextWatcher; framework calls afterTextChanged when the text changes', evidence='SRC ui/dialogs/RenameBookmark.java:86-93 conName.addTextChangedListener(new SimpleTextWatcher(){ public void afterTextChanged(Editable s) {...} })')
e('RenameBookmark.onCreateDialog', 'RenameBookmark$2.afterTextChanged', 'FRAMEWORK', 'ip.addTextChangedListener registers an anonymous SimpleTextWatcher when studiomode != 0; framework calls afterTextChanged when the text changes', evidence='SRC ui/dialogs/RenameBookmark.java:112-119 ip.addTextChangedListener(new SimpleTextWatcher(){ public void afterTextChanged(Editable s) {...} })')
e('SftpConnectDialog.onCreateDialog', 'SftpConnectDialog$1.afterTextChanged', 'FRAMEWORK', 'addressET/portET/usernameET/passwordET.addTextChangedListener(validator) registers an anonymous SimpleTextWatcher; framework calls afterTextChanged when any field changes', evidence='SRC ui/dialogs/SftpConnectDialog.java:266-294 TextWatcher validator = new SimpleTextWatcher(){ public void afterTextChanged(Editable s) {...} }; addressET.addTextChangedListener(validator); portET.addTextChangedListener(validator); usernameET.addTextChangedListener(validator); passwordET.addTextChangedListener(validator)')
e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$1.afterTextChanged', 'FRAMEWORK', 'conName.addTextChangedListener registers an anonymous SimpleTextWatcher; framework calls afterTextChanged when the text changes', evidence='SRC ui/dialogs/SmbConnectDialog.java:116-122 conName.addTextChangedListener(new SimpleTextWatcher(){ public void afterTextChanged(Editable s) {...} })')
e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$2.afterTextChanged', 'FRAMEWORK', 'ip.addTextChangedListener registers an anonymous SimpleTextWatcher; framework calls afterTextChanged when the text changes', evidence='SRC ui/dialogs/SmbConnectDialog.java:124-131 ip.addTextChangedListener(new SimpleTextWatcher(){ public void afterTextChanged(Editable s) {...} })')
e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$3.afterTextChanged', 'FRAMEWORK', 'domain.addTextChangedListener registers an anonymous SimpleTextWatcher; framework calls afterTextChanged when the text changes', evidence='SRC ui/dialogs/SmbConnectDialog.java:132-139 domain.addTextChangedListener(new SimpleTextWatcher(){ public void afterTextChanged(Editable s) {...} })')
e('SmbConnectDialog.onCreateDialog', 'SmbConnectDialog$4.afterTextChanged', 'FRAMEWORK', 'user.addTextChangedListener registers an anonymous SimpleTextWatcher; framework calls afterTextChanged when the text changes', evidence='SRC ui/dialogs/SmbConnectDialog.java:140-147 user.addTextChangedListener(new SimpleTextWatcher(){ public void afterTextChanged(Editable s) {...} })')
e('ColorPickerDialog.inflateItem', 'CircularColorsView.<init>(Context,AttributeSet)', 'FRAMEWORK', 'inflateItem inflates item_colorpicker.xml, which declares a CircularColorsView element; the Android LayoutInflater instantiates it via the (Context,AttributeSet) constructor', evidence='SRC ui/dialogs/ColorPickerDialog.java:178-179 View child = inflater.inflate(R.layout.item_colorpicker, container, false); res/layout/item_colorpicker.xml:28-34 <com.amaze.filemanager.ui.views.CircularColorsView android:id="@+id/circularColorsView" .../>')
e('CircularColorsView.<init>(Context,AttributeSet)', 'CircularColorsView.init', 'CALL', 'constructor calls init()', evidence='SRC ui/views/CircularColorsView.java:34-37 public CircularColorsView(Context context, AttributeSet attrs) { super(context, attrs); init(); }')
e('TabFragment.onCreateView', 'DisablableViewPager.<init>', 'FRAMEWORK', 'onCreateView inflates tabfragment.xml whose root element is DisablableViewPager; the Android LayoutInflater instantiates it via the (Context,AttributeSet) constructor', evidence='SRC fragments/TabFragment.java:80 ViewGroup rootView = (ViewGroup) inflater.inflate(R.layout.tabfragment, container, false); res/layout/tabfragment.xml:20-24 <com.amaze.filemanager.ui.views.DisablableViewPager android:id="@+id/pager" .../>')
e('DisablableViewPager.<init>', 'DisablableViewPager.onInterceptTouchEvent', 'FRAMEWORK', 'ViewGroup.onInterceptTouchEvent dispatched by the Android framework to decide whether to intercept touch events for descendant views', evidence='SRC ui/views/DisablableViewPager.java:25-29 @Override public boolean onInterceptTouchEvent(MotionEvent event)')
e('DisablableViewPager.<init>', 'DisablableViewPager.onTouchEvent', 'FRAMEWORK', 'View.onTouchEvent dispatched by the Android framework when the view is touched', evidence='SRC ui/views/DisablableViewPager.java:20-23 @Override public boolean onTouchEvent(MotionEvent event)')
e('MainFragment.onCreateView', 'FastScroller.<init>(Context,AttributeSet)', 'FRAMEWORK', 'onCreateView inflates main_frag.xml which declares a FastScroller element; the Android LayoutInflater instantiates it via the (Context,AttributeSet) constructor', evidence='SRC fragments/MainFragment.java:238 rootView = inflater.inflate(R.layout.main_frag, container, false); res/layout/main_frag.xml:46-50 <com.amaze.filemanager.ui.views.FastScroller android:id="@+id/fastscroll" .../>')
e('FastScroller.onTouchEvent', 'FastScroller.getRelativeTouchPosition', 'CALL', 'onTouchEvent calls getRelativeTouchPosition', evidence='SRC ui/views/FastScroller.java:105 float relativePos = getRelativeTouchPosition(motionEvent);')
e('FastScroller.<init>(Context,AttributeSet)', 'FastScroller.onTouchEvent', 'FRAMEWORK', 'View.onTouchEvent dispatched by the Android framework when the FastScroller view is touched', evidence='SRC ui/views/FastScroller.java:101-121 public boolean onTouchEvent(MotionEvent motionEvent) {...}')
e('FastScroller.onTouchEvent', 'FastScroller.setRecyclerViewPosition', 'CALL', 'onTouchEvent calls setRecyclerViewPosition', evidence='SRC ui/views/FastScroller.java:108 setRecyclerViewPosition(relativePos);')
e('MainActivity.onCreate', 'Indicator.<init>(Context,AttributeSet)', 'FRAMEWORK', 'setContentView(R.layout.main_toolbar) inflates the layout-v21/main_toolbar.xml variant (used on API 21+) which declares an Indicator view; LayoutInflater constructs custom views via their (Context,AttributeSet) constructor', evidence='SRC MainActivity.java:288 setContentView(R.layout.main_toolbar); SRC res/layout-v21/main_toolbar.xml:50-51 <com.amaze.filemanager.ui.views.Indicator android:id="@+id/indicator" .../>')
e('Indicator.<init>(Context,AttributeSet)', 'Indicator.<init>(Context,AttributeSet,int)', 'CALL', 'Indicator(Context,AttributeSet) delegates to the 3-arg constructor', evidence='SRC Indicator.java:119-121 public Indicator(Context context, AttributeSet attrs) { this(context, attrs, 0); }')
e('Indicator$PendingRevealAnimator.<init>', 'Indicator$PendingRevealAnimator.lambda$new$0', 'CALL', 'PendingRevealAnimator constructor registers its update-listener lambda via addUpdateListener', evidence='SRC Indicator.java:776-780 addUpdateListener(valueAnimator -> { setDotRevealFraction(PendingRevealAnimator.this.dot, (Float) valueAnimator.getAnimatedValue()); });')
e('RecyclerAdapter.onCreateViewHolder', 'RoundedImageView.<init>', 'FRAMEWORK', 'onCreateViewHolder inflates rowlayout.xml or griditem.xml, both of which declare a RoundedImageView; LayoutInflater constructs it via its (Context,AttributeSet) constructor', evidence='SRC RecyclerAdapter.java:467,472 mInflater.inflate(R.layout.rowlayout/griditem, parent, false); SRC res/layout/rowlayout.xml:49, res/layout/griditem.xml:25 <com.amaze.filemanager.ui.views.RoundedImageView .../>')
e('RoundedImageView.<init>', 'RoundedImageView.onDraw', 'FRAMEWORK', 'View framework calls onDraw whenever the RoundedImageView needs to render', evidence='SRC RoundedImageView.java:40-61 protected void onDraw(Canvas canvas) override')
e('RoundedImageView.onDraw', 'RoundedImageView.isImageAnIcon', 'CALL', 'onDraw branches on isImageAnIcon() to choose the drawing path', evidence='SRC RoundedImageView.java:47 if(!isImageAnIcon()) {')
e('RoundedImageView.onDraw', 'RoundedImageView.drawableToBitmap', 'CALL', 'onDraw converts the drawable to a bitmap when not an icon', evidence='SRC RoundedImageView.java:48 Bitmap b = drawableToBitmap(drawable);')
e('RoundedImageView.onDraw', 'RoundedImageView.getRoundedCroppedBitmap', 'CALL', 'onDraw crops the bitmap into a rounded shape', evidence='SRC RoundedImageView.java:51 Bitmap roundBitmap = getRoundedCroppedBitmap(bitmap, w);')
e('RoundedImageView.onDraw', 'RoundedImageView.drawableToBitmapRelative', 'CALL', 'onDraw converts the drawable to a relatively-sized bitmap when it is an icon', evidence='SRC RoundedImageView.java:57 Bitmap bitmap = drawableToBitmapRelative(drawable, radius);')
e('PathSwitchPreference.<init>', 'PathSwitchPreference.onCreateView', 'FRAMEWORK', 'Android Preference framework calls onCreateView to create the preference row view before it is displayed', evidence='SRC PathSwitchPreference.java:26-30 protected View onCreateView(ViewGroup parent) override')
e('PathSwitchPreference.onCreateView', 'ThemedImageButton.<init>(Context,AttributeSet)', 'FRAMEWORK', 'onCreateView sets the widget layout resource to namepathswitch_preference.xml and delegates to super.onCreateView, which the Preference framework inflates and attaches as the widget frame; that layout declares two ThemedImageButton views constructed via their (Context,AttributeSet) constructor', evidence='SRC PathSwitchPreference.java:28-29 setWidgetLayoutResource(R.layout.namepathswitch_preference); return super.onCreateView(parent); SRC res/layout/namepathswitch_preference.xml:10,19 <com.amaze.filemanager.ui.views.ThemedImageButton .../>')
e('ThemedImageButton.<init>(Context,AttributeSet)', 'ThemedImageButton.onSetAlpha', 'FRAMEWORK', 'View framework calls onSetAlpha when the view alpha is set, to let the view optimize/override alpha handling', evidence='SRC ThemedImageButton.java:27-30 protected boolean onSetAlpha(int alpha) override')
e('ThemedImageButton.<init>(Context,AttributeSet)', 'ThemedImageButton.getAccessibilityClassName', 'FRAMEWORK', 'Android accessibility framework calls getAccessibilityClassName when building accessibility node info for the view', evidence='SRC ThemedImageButton.java:32-35 public CharSequence getAccessibilityClassName() override')
e('ThemedImageButton.<init>(Context,AttributeSet)', 'ThemedImageView.<init>(Context,AttributeSet)', 'CALL', 'ThemedImageButton(Context,AttributeSet) calls super(context, attrs)', evidence='SRC ThemedImageButton.java:18-20 public ThemedImageButton(Context context, AttributeSet attrs) { super(context, attrs); }')
e('ThemedImageView.<init>(Context,AttributeSet)', 'ThemedImageView.<init>(Context,AttributeSet,int)', 'CALL', 'ThemedImageView(Context,AttributeSet) delegates to the 3-arg constructor', evidence='SRC ThemedImageView.java:25-27 public ThemedImageView(Context context, AttributeSet attrs) { this(context, attrs, 0); }')
e('ThemedImageView.<init>(Context,AttributeSet,int)', 'ThemedImageView.getActivity', 'CALL', 'constructor calls getActivity() to read the current theme from the hosting Activity', evidence='SRC ThemedImageView.java:29-32 ThemedImageView(Context context, AttributeSet attrs, int defStyleAttr) { super(...); BasicActivity a = (BasicActivity) getActivity();')
e('AppBar.<init>', 'SearchView.<init>', 'CALL', 'AppBar constructor instantiates SearchView', evidence='SRC AppBar.java:34-36 public AppBar(MainActivity a, SharedPreferences sharedPref, SearchView.SearchListener searchListener) { ... searchView = new SearchView(this, a, searchListener); }')
e('MainActivity.onOptionsItemSelected', 'SearchView.revealSearchView', 'CALL', 'Clicking the search menu item reveals the search view', evidence='SRC MainActivity.java:1040-1041 case R.id.search: getAppbar().getSearchView().revealSearchView();')
e('SearchView.revealSearchView', 'SearchView$1.<init>', 'CALL', 'revealSearchView creates the anonymous Animator.AnimatorListener and registers it via animator.addListener', evidence='SRC SearchView.java:93-110 animator.addListener(new Animator.AnimatorListener() { ... });')
e('SearchView$1.<init>', 'SearchView$1.onAnimationStart', 'FRAMEWORK', 'Animator framework calls the registered AnimatorListener.onAnimationStart when the reveal animation starts', evidence='SRC SearchView.java:94-95 public void onAnimationStart(Animator animation) {}')
e('SearchView$1.<init>', 'SearchView$1.onAnimationEnd', 'FRAMEWORK', 'Animator framework calls onAnimationEnd when the reveal animation completes', evidence='SRC SearchView.java:97-103 public void onAnimationEnd(Animator animation) { searchViewEditText.requestFocus(); ... enabled = true; }')
e('SearchView$1.<init>', 'SearchView$1.onAnimationCancel', 'FRAMEWORK', 'Animator framework calls onAnimationCancel if the reveal animation is cancelled', evidence='SRC SearchView.java:105-106 public void onAnimationCancel(Animator animation) {}')
e('SearchView$1.<init>', 'SearchView$1.onAnimationRepeat', 'FRAMEWORK', 'Animator framework calls onAnimationRepeat if the reveal animation repeats', evidence='SRC SearchView.java:108-109 public void onAnimationRepeat(Animator animation) {}')
e('MainActivity.onBackPressed', 'SearchView.hideSearchView', 'CALL', 'Pressing back while the search view is shown hides it', evidence='SRC MainActivity.java:709-712 if (getAppbar().getSearchView().isShown()) { getAppbar().getSearchView().hideSearchView(); }')
e('SearchView.hideSearchView', 'SearchView$2.<init>', 'CALL', 'hideSearchView creates the anonymous Animator.AnimatorListener and registers it via animator.addListener', evidence='SRC SearchView.java:137-154 animator.addListener(new Animator.AnimatorListener() { ... });')
e('SearchView$2.<init>', 'SearchView$2.onAnimationStart', 'FRAMEWORK', 'Animator framework calls the registered AnimatorListener.onAnimationStart when the hide animation starts', evidence='SRC SearchView.java:138-139 public void onAnimationStart(Animator animation) {}')
e('SearchView$2.<init>', 'SearchView$2.onAnimationEnd', 'FRAMEWORK', 'Animator framework calls onAnimationEnd when the hide animation completes', evidence='SRC SearchView.java:141-147 public void onAnimationEnd(Animator animation) { searchViewLayout.setVisibility(View.GONE); ... }')
e('SearchView$2.<init>', 'SearchView$2.onAnimationCancel', 'FRAMEWORK', 'Animator framework calls onAnimationCancel if the hide animation is cancelled', evidence='SRC SearchView.java:149-150 public void onAnimationCancel(Animator animation) {}')
e('SearchView$2.<init>', 'SearchView$2.onAnimationRepeat', 'FRAMEWORK', 'Animator framework calls onAnimationRepeat if the hide animation repeats', evidence='SRC SearchView.java:152-153 public void onAnimationRepeat(Animator animation) {}')
e('MainActivity.onCreate', 'CustomNavigationView.<init>', 'FRAMEWORK', 'setContentView(R.layout.main_toolbar) inflates main_toolbar.xml, which declares a CustomNavigationView used as the drawer navigation view', evidence='SRC MainActivity.java:288 setContentView(R.layout.main_toolbar); SRC res/layout/main_toolbar.xml:67-70 <com.amaze.filemanager.ui.views.drawer.CustomNavigationView android:id="@+id/navigation" .../>')
e('CustomNavigationView.<init>', 'CustomNavigationView.onNavigationItemSelected', 'FRAMEWORK', 'CustomNavigationView implements NavigationView.OnNavigationItemSelectedListener and registers itself as the listener in its constructor; NavigationView framework calls onNavigationItemSelected when a drawer menu item is selected', evidence='SRC CustomNavigationView.java:16-17,22-25 class ... implements NavigationView.OnNavigationItemSelectedListener { public CustomNavigationView(Context context, AttributeSet attrs) { super(context, attrs); super.setNavigationItemSelectedListener(this); }')
e('CustomNavigationView.onNavigationItemSelected', 'CustomNavigationView.onItemChecked', 'CALL', 'onNavigationItemSelected calls onItemChecked(item) both when there is no subclass listener and when the subclass listener returns true', evidence='SRC CustomNavigationView.java:34-47 onNavigationItemSelected calls onItemChecked(item) at lines 39 and 44')
e('CustomNavigationView.<init>', 'CustomNavigationView.onSaveInstanceState', 'LIFECYCLE', 'Android View framework calls onSaveInstanceState when the view hierarchy state is saved', evidence='SRC CustomNavigationView.java:67-82 public Parcelable onSaveInstanceState() override')
e('CustomNavigationView.onSaveInstanceState', 'CustomNavigationView.isNavigationViewSavedStateMissing', 'CALL', 'onSaveInstanceState calls isNavigationViewSavedStateMissing() to check the API-level guard', evidence='SRC CustomNavigationView.java:69 if (isNavigationViewSavedStateMissing()) { return super.onSaveInstanceState(); }')
e('CustomNavigationView.<init>', 'CustomNavigationView.onRestoreInstanceState', 'LIFECYCLE', 'Android View framework calls onRestoreInstanceState when previously saved view state is restored', evidence='SRC CustomNavigationView.java:84-102 public void onRestoreInstanceState(Parcelable state) override')
e('CustomNavigationView.onRestoreInstanceState', 'CustomNavigationView.isNavigationViewSavedStateMissing', 'CALL', 'onRestoreInstanceState calls isNavigationViewSavedStateMissing() to check the API-level guard', evidence='SRC CustomNavigationView.java:86 if(isNavigationViewSavedStateMissing()) { super.onRestoreInstanceState(state); return; }')
e('ColorPref.loadSection1', 'InvalidablePreferenceCategory.<init>', 'FRAMEWORK', 'addPreferencesFromResource(R.xml.conficolor_prefs) inflates the preference XML which declares an InvalidablePreferenceCategory; the Android Preference framework constructs it via its (Context,AttributeSet) constructor', evidence='SRC ColorPref.java:217 addPreferencesFromResource(R.xml.conficolor_prefs); SRC res/xml/conficolor_prefs.xml:6 <com.amaze.filemanager.ui.views.preference.InvalidablePreferenceCategory ...>')
e('FoldersPref.onCreate', 'PathSwitchPreference.<init>', 'CALL', 'FoldersPref.onCreate instantiates a PathSwitchPreference for each bookmark', evidence='SRC FoldersPref.java:58-59 for (int i = 0; i < dataUtils.getBooks().size(); i++) { PathSwitchPreference p = new PathSwitchPreference(getActivity());')
e('PathSwitchPreference.<init>', 'PathSwitchPreference.onBindView', 'FRAMEWORK', 'Android Preference framework calls onBindView to bind the preference row view before it is displayed in the list', evidence='SRC PathSwitchPreference.java:32-40 protected void onBindView(View view) override')
e('PathSwitchPreference.onBindView', 'PathSwitchPreference.setListener', 'CALL', 'onBindView calls setListener for the edit and delete icon views', evidence='SRC PathSwitchPreference.java:34-35 setListener(view, R.id.edit, EDIT); setListener(view, R.id.delete, DELETE);')
e('PathSwitchPreference.setListener', 'PathSwitchPreference.lambda$setListener$0', 'CALL', 'setListener registers the lambda as the View.OnClickListener; it runs when the user clicks the edit/delete icon', evidence='SRC PathSwitchPreference.java:49-54 View.OnClickListener l = view -> { lastItemClicked = elem; getOnPreferenceClickListener().onPreferenceClick(t); }; v.findViewById(id).setOnClickListener(l);')
e('PathSwitchPreference.onCreateView', 'PathSwitchPreference.onBindView', 'FRAMEWORK', 'Preference framework calls onBindView after onCreateView to bind preference view data', evidence='SRC ui/views/preference/PathSwitchPreference.java:32-39 overrides Preference.onBindView(View)')
e('ColorPref.loadSection1', 'SelectedColorsPreference.<init>', 'FRAMEWORK', 'loadSection1 calls addPreferencesFromResource(R.xml.conficolor_prefs), which XML-inflates ColorPickerDialog (a SelectedColorsPreference subclass), invoking the (Context,AttributeSet) constructor', evidence='SRC fragments/preference_fragments/ColorPref.java:219 addPreferencesFromResource(R.xml.conficolor_prefs); res/xml/conficolor_prefs.xml:3-5 declares com.amaze.filemanager.ui.dialogs.ColorPickerDialog; ui/views/preference/SelectedColorsPreference.java:27-29 constructor')
e('SelectedColorsPreference.<init>', 'SelectedColorsPreference.onCreateView', 'FRAMEWORK', 'Android Preference framework calls onCreateView to build the preference view', evidence='SRC ui/views/preference/SelectedColorsPreference.java:31-35 overrides Preference.onCreateView(ViewGroup)')
e('SelectedColorsPreference.onCreateView', 'SelectedColorsPreference.onBindView', 'FRAMEWORK', 'Preference framework calls onBindView after onCreateView to bind preference view data', evidence='SRC ui/views/preference/SelectedColorsPreference.java:38-46 overrides Preference.onBindView(View)')
e('Indicator.<init>(Context,AttributeSet,int)', 'AnimUtils.getFastOutSlowInInterpolator', 'CALL', 'constructor initializes interpolator field', evidence='SRC ui/views/Indicator.java:153 interpolator = AnimUtils.getFastOutSlowInInterpolator(context);')
e('AppListLoader.onStartLoading', 'AppListLoader.onStopLoading', 'LIFECYCLE', 'Standard AsyncTaskLoader lifecycle: framework calls onStopLoading when the loader is stopped (e.g. fragment paused/reset) after it has been started', evidence='SRC asynchronous/loaders/AppListLoader.java:112 protected void onStartLoading(); line 131 protected void onStopLoading(), both overriding AsyncTaskLoader')
e('Drawer.<init>', 'AppConfig.getImageLoader', 'CALL', 'Drawer constructor obtains the shared ImageLoader', evidence='SRC ui/views/drawer/Drawer.java:156 mImageLoader = AppConfig.getInstance().getImageLoader();')
e('AppConfig.getImageLoader', 'LruBitmapCache.<init>()', 'CALL', 'getImageLoader lazily constructs an ImageLoader using a no-arg LruBitmapCache as its ImageCache', evidence='SRC utils/application/AppConfig.java:223 this.mImageLoader = new ImageLoader(mRequestQueue, new LruBitmapCache());')
e('LruBitmapCache.<init>()', 'LruBitmapCache.getBitmap', 'FRAMEWORK', 'Volley ImageLoader (library) calls ImageCache.getBitmap(url) to check the cache before issuing a network request; library code not read', evidence='SRC utils/LruBitmapCache.java:30-33 implements ImageLoader.ImageCache; INFERRED com.android.volley.toolbox.ImageLoader library calls getBitmap, library source not read')
e('LruBitmapCache.<init>()', 'LruBitmapCache.putBitmap', 'FRAMEWORK', 'Volley ImageLoader (library) calls ImageCache.putBitmap(url,bitmap) after a successful image load; library code not read', evidence='SRC utils/LruBitmapCache.java:35-38 implements ImageLoader.ImageCache; INFERRED com.android.volley.toolbox.ImageLoader library calls putBitmap, library source not read')
e('LruBitmapCache.<init>()', 'LruBitmapCache.sizeOf', 'FRAMEWORK', 'android.util.LruCache (framework) calls sizeOf(key,value) internally whenever put() is invoked', evidence='SRC utils/LruBitmapCache.java:40-44 overrides LruCache.sizeOf; INFERRED android.util.LruCache.put() framework code not read, documented to call sizeOf')
e('StreamServer$HTTPSession.handleResponse', 'Streamer.serve', 'FRAMEWORK', 'handleResponse calls the abstract serve() method; at runtime the server instance is a Streamer so this dispatches to Streamer.serve override', evidence='SRC SmbStreamer/StreamServer.java:327 Response r = serve(uri, method, header, parms, files); SmbStreamer/Streamer.java:63 public Response serve(...) overrides StreamServer.serve')
e('Streamer.serve', 'StreamSource.<init>', 'CALL', 'Streamer.serve constructs a StreamSource for the requested SMB file', evidence='SRC SmbStreamer/Streamer.java:101 final StreamSource source = new StreamSource(sourceFile, length);')
e('StreamServer$HTTPSession.sendResponse', 'StreamSource.read(byte[],int,int)', 'CALL', 'sendResponse loops calling data.read(buff); InputStream.read(byte[]) (JDK, not read) dispatches to the overridden 3-arg read', evidence='SRC SmbStreamer/StreamServer.java:672 while ((read = data.read(buff)) > 0); SmbStreamer/StreamSource.java:75-79 overrides read(byte[],int,int); INFERRED java.io.InputStream.read(byte[]) JDK source not read, documented to call read(b,0,b.length)')
e('PreferencesActivity.selectItem', 'QuickAccessPref.<init>', 'CALL', 'selectItem creates QuickAccessPref for the quick-access preference section', evidence='SRC activities/PreferencesActivity.java:264 loadPrefFragment(new QuickAccessPref(), R.string.sidebar_quick_access_title);')
e('QuickAccessPref.<init>', 'QuickAccessPref.onCreate', 'LIFECYCLE', 'PreferenceFragment.onCreate called by framework after the fragment transaction', evidence='SRC activities/PreferencesActivity.java:264; FW-SRC PreferenceFragment lifecycle calls onCreate')
e('QuickAccessPref.onPreferenceClick', 'TinyDB.putBooleanArray', 'CALL', 'onPreferenceClick saves the updated quick-access boolean array', evidence='SRC fragments/preference_fragments/QuickAccessPref.java:60 TinyDB.putBooleanArray(preferences, KEY, currentValue);')
e('FastScroller.getRelativeTouchPosition', 'Utils.getViewRawY', 'CALL', 'getRelativeTouchPosition computes touch position using the handle view raw Y coordinate', evidence='SRC ui/views/FastScroller.java:147 float yInParent = event.getRawY() - Utils.getViewRawY(handle);')
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter$1.onLoadFailed', 'FRAMEWORK', 'onBindViewHolder calls showThumbnailWithBackground, which registers the anonymous RequestListener via .listener(requestListener).into(view); Glide calls onLoadFailed when the thumbnail fails to load', evidence='SRC adapters/RecyclerAdapter.java:595,598,608 onBindViewHolder calls showThumbnailWithBackground; SRC adapters/RecyclerAdapter.java:872-898 anonymous RequestListener defined; SRC adapters/RecyclerAdapter.java:899 modelProvider.getPreloadRequestBuilder(iconData).listener(requestListener).into(view); INFERRED com.bumptech.glide.Glide (generated code) invokes RequestListener callbacks (Glide source not read)')
e('RecyclerAdapter.onBindViewHolder', 'RecyclerAdapter$1.onResourceReady', 'FRAMEWORK', 'Glide calls onResourceReady on the same registered listener when the thumbnail loads successfully', evidence='SRC adapters/RecyclerAdapter.java:595,598,608 onBindViewHolder calls showThumbnailWithBackground; SRC adapters/RecyclerAdapter.java:888-896 onResourceReady override; SRC adapters/RecyclerAdapter.java:899 listener(requestListener).into(view); INFERRED com.bumptech.glide.Glide (generated code) invokes RequestListener callbacks (Glide source not read)')
e('RecyclerAdapter$1.onLoadFailed', 'RecyclerAdapter$1.lambda$onLoadFailed$0', 'CALL', 'onLoadFailed creates a Handler with lambda msg -> {...} compiled to synthetic lambda$onLoadFailed$0, then calls obtainMessage().sendToTarget()', evidence='SRC adapters/RecyclerAdapter.java:875-886')
e('CompressedExplorerFragment.onCreate', 'CompressedExplorerFragment.onSaveInstanceState', 'FRAMEWORK',
  'Fragment framework calls onSaveInstanceState to save state after onCreate',
  evidence='SRC fragments/CompressedExplorerFragment.java:225-232 defines onSaveInstanceState and puts the element list into outState; INFERRED Fragment framework calls onSaveInstanceState after onCreate')
e('CompressedExplorerFragment.onSaveInstanceState', 'CompressedObjectParcelable.writeToParcel', 'FRAMEWORK', 'Fragment state save triggers Parcelable write via Bundle.putParcelableArrayList', evidence='SRC fragments/CompressedExplorerFragment.java:228 outState.putParcelableArrayList(KEY_ELEMENTS, elements); framework marshals via writeToParcel')
e('CompressedObjectParcelable.writeToParcel', 'IconDataParcelable.writeToParcel', 'FRAMEWORK', 'CompressedObjectParcelable.writeToParcel calls writeParcelable(iconData,0); the framework marshals the nested Parcelable by calling its writeToParcel', evidence='SRC adapters/data/CompressedObjectParcelable.java:86 p1.writeParcelable(iconData, 0); INFERRED android.os.Parcel.writeParcelable invokes the Parcelable argument''s writeToParcel method (platform source not read)')
e('CompressedObjectParcelable.writeToParcel', 'IconDataParcelable.describeContents', 'FRAMEWORK', 'Parcelable protocol may query describeContents of a nested Parcelable field being written', evidence='SRC adapters/data/CompressedObjectParcelable.java:86 p1.writeParcelable(iconData, 0); SRC adapters/data/IconDataParcelable.java:45-48 defines describeContents; INFERRED Android Parcelable contract (platform source not read)')
e('SevenZipExtractor.extractWithFilter', 'SevenZFile.getNextEntry', 'CALL', 'extractWithFilter loops over sevenzFile.getNextEntry() to iterate archive entries during extraction', evidence='SRC filesystem/compressed/extractcontents/helpers/SevenZipExtractor.java:67 while ((entry = sevenzFile.getNextEntry()) != null) {')
e('SevenZFile.getNextEntry', 'SevenZFile.buildDecodingStream', 'CALL', 'getNextEntry calls buildDecodingStream to prepare the stream for the next entry', evidence='SRC commons_compress_7z/.../sevenz/SevenZFile.java:295 buildDecodingStream();')
e('SevenZFile.buildDecodingStream', 'SevenZFile.buildDecoderStack', 'CALL', 'buildDecodingStream calls buildDecoderStack when opening a new folder', evidence='SRC commons_compress_7z/.../sevenz/SevenZFile.java:983 currentFolderInputStream = buildDecoderStack(folder, folderOffset, firstPackStreamIndex, file);')
e('SevenZFile.buildDecoderStack', 'SevenZFile$1.<init>', 'CALL', 'buildDecoderStack creates anonymous FilterInputStream to track compressed bytes read', evidence='SRC commons_compress_7z/.../sevenz/SevenZFile.java:997-1022')
e('SevenZFile$1.<init>', 'SevenZFile$1.read()', 'CALL', 'Stream read methods invoked during decompression by the decoder chain consuming this FilterInputStream', evidence='SRC commons_compress_7z/.../sevenz/SevenZFile.java:1001-1007')
e('SevenZFile$1.<init>', 'SevenZFile$1.read(byte[])', 'CALL', 'Stream read methods invoked during decompression by the decoder chain consuming this FilterInputStream', evidence='SRC commons_compress_7z/.../sevenz/SevenZFile.java:1009-1011')
e('SevenZFile$1.<init>', 'SevenZFile$1.read(byte[],int,int)', 'CALL', 'Stream read methods invoked during decompression by the decoder chain consuming this FilterInputStream', evidence='SRC commons_compress_7z/.../sevenz/SevenZFile.java:1013-1019')
e('SevenZFile$1.read()', 'SevenZFile$1.count', 'CALL', 'After reading from parent FilterInputStream, calls count() to track compressed bytes', evidence='SRC commons_compress_7z/.../sevenz/SevenZFile.java:1001-1007')
e('SevenZFile$1.read(byte[])', 'SevenZFile$1.read(byte[],int,int)', 'CALL', 'read(byte[]) delegates to read(byte[],int,int) with full array bounds', evidence='SRC commons_compress_7z/.../sevenz/SevenZFile.java:1009-1011')
e('SevenZFile$1.read(byte[],int,int)', 'SevenZFile$1.count', 'CALL', 'After reading from parent FilterInputStream, calls count() with number of bytes read', evidence='SRC commons_compress_7z/.../sevenz/SevenZFile.java:1013-1019')
e('CryptUtil.encrypt', 'HybridFile.getOutputStream', 'CALL', 'encrypt opens an output stream on the target (decrypted-name-stripped) HybridFile to write the encrypted bytes', evidence='SRC utils/files/CryptUtil.java:246 BufferedOutputStream outputStream = new BufferedOutputStream(targetFile.getOutputStream(context), ...)')
e('HybridFile.getOutputStream', 'HybridFile$11.<init>', 'CALL', 'getOutputStream case SFTP creates an anonymous SshClientTemplate(path,false)', evidence='SRC filesystem/HybridFile.java:1021 return SshClientUtils.execute(new SshClientTemplate(path, false) {')
e('HybridFile.getOutputStream', 'SshClientUtils.execute(SshClientTemplate)', 'CALL', 'getOutputStream case SFTP passes the anonymous template to SshClientUtils.execute', evidence='SRC filesystem/HybridFile.java:1021 return SshClientUtils.execute(new SshClientTemplate(path, false) {')
e('SshClientUtils.execute(SshClientTemplate)', 'SshConnectionPool.getConnection(String)', 'CALL', 'execute obtains a pooled/new SSHClient for template.url', evidence='SRC filesystem/ssh/SshClientUtils.java:72 client = SshConnectionPool.getInstance().getConnection(template.url);')
e('SshConnectionPool.getConnection(String)', 'SshConnectionPool.create(String)', 'CALL', 'getConnection creates a new client with create(url) when none pooled or the pooled one fails validation', evidence='SRC filesystem/ssh/SshConnectionPool.java:108-124, calls at lines 113 and 121: client = create(url);')
e('SshConnectionPool.create(String)', 'PemToKeyPairTask.<init>(String,Callback)', 'CALL', 'create(url) looks up a stored SSH private key PEM and, if present, converts it to a KeyPair via PemToKeyPairTask', evidence='SRC filesystem/ssh/SshConnectionPool.java:196-202 if(pem != null && !pem.isEmpty()) { ... new PemToKeyPairTask(pem, result -> { keyPair.set(result); latch.countDown(); }).execute(); ... }')
e('PemToKeyPairTask.<init>(String,Callback)', 'PemToKeyPairTask.onPostExecute', 'ASYNC', 'AsyncTask.execute() runs doInBackground on a worker thread and onPostExecute on the main thread', evidence='SRC asynchronous/asynctasks/ssh/SshConnectionPool.java:202 }).execute(); SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:99-120,176-180 defines doInBackground/onPostExecute')
e('PemToKeyPairTask.onPostExecute', 'SshConnectionPool.lambda$create$1', 'CALL', 'onPostExecute invokes the registered callback with the computed KeyPair, which is the lambda created inside SshConnectionPool.create(String)', evidence='SRC asynchronous/asynctasks/ssh/PemToKeyPairTask.java:176-180 protected void onPostExecute(KeyPair result) { if(callback != null) { callback.onResult(result); } }')

e('MainActivity.onCreate', 'S_MAIN', 'LIFECYCLE',
  'onCreate builds the main shell (views, tabs, drawer, FAB)',
  evidence='SRC activities/MainActivity.java:277 public void onCreate(Bundle) builds the main screen')

e('MainFragment.onCreateView', 'S_MAIN_TAB', 'LIFECYCLE',
  'onCreateView inflates the tab that shows the file list',
  evidence='SRC fragments/MainFragment.java:237 public View onCreateView(LayoutInflater, ViewGroup, Bundle)')

e('PermissionsActivity.requestStoragePermission', 'S_PERM', 'CALL',
  'requestStoragePermission asks for WRITE_EXTERNAL_STORAGE',
  evidence='SRC activities/superclasses/PermissionsActivity.java:53-60 requestStoragePermission calls requestPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE, ...)')

e('PermissionsActivity.requestStoragePermission', 'S_DIALOG', 'CALL',
  'requestStoragePermission shows the grant-storage-permission dialog',
  evidence='SRC activities/superclasses/PermissionsActivity.java:54 GeneralDialogCreation.showBasicDialog(this, grant_storage_permission, ...)')

e('TextEditorActivity.onCreate', 'S_TEXT_EDITOR', 'LIFECYCLE',
  'onCreate shows the text viewer/editor screen',
  evidence='SRC activities/TextEditorActivity.java:126 public void onCreate(Bundle)')

e('DatabaseViewerActivity.onCreate', 'S_DB_VIEWER', 'LIFECYCLE',
  'onCreate shows the SQLite database viewer screen',
  evidence='SRC activities/DatabaseViewerActivity.java:79 public void onCreate(Bundle)')

e('ExtractService.onStartCommand', 'S_SERVICE', 'LIFECYCLE',
  'onStartCommand starts the background extraction work, so a service is running',
  evidence='SRC asynchronous/services/ExtractService.java:97 public int onStartCommand(Intent, int, int)')

e('Drawer.open', 'S_DRAWER', 'CALL',
  'open() opens the navigation drawer',
  evidence='SRC ui/views/drawer/Drawer.java:522 public void open()')

e('MainActivity.onDestroy', 'S_EXIT', 'LIFECYCLE',
  'onDestroy ends the activity; the app is leaving the main screen',
  evidence='SRC activities/MainActivity.java:1204 protected void onDestroy()')

UNREACHABLE['PropertiesSheet.<init>'] = ('no_trigger_in_app', 'The only "new PropertiesSheet()" call site in the app is inside a /* ... */ comment block, so PropertiesSheet is never instantiated', 'SRC ui/ItemPopupMenu.java:70-77 commented-out block containing new PropertiesSheet(); grep -rn "PropertiesSheet" app/src/main/java finds no other instantiation site', 'SOURCE')
UNREACHABLE['PropertiesSheet.generate'] = ('no_trigger_in_app', 'Private empty-bodied method generate() is never called anywhere in PropertiesSheet.java or elsewhere in the app, and PropertiesSheet itself is never instantiated', 'SRC fragments/PropertiesSheet.java:112-115 private void generate(...) {} with no call sites in the file', 'SOURCE')
UNREACHABLE['PropertiesSheet.setupDialog'] = ('no_trigger_in_app', 'setupDialog is only invoked by BottomSheetDialogFragment framework when the dialog is actually shown; PropertiesSheet is never instantiated/shown since its only instantiation site is commented out', 'SRC fragments/PropertiesSheet.java:50-106 setupDialog override; ui/ItemPopupMenu.java:70-77 shows instantiation is commented out', 'SOURCE')
UNREACHABLE['PropertiesSheet$1.<init>'] = ('no_trigger_in_app', 'Anonymous NestedScrollView.OnScrollChangeListener is created inside setupDialog, which never executes', 'SRC fragments/PropertiesSheet.java:86-95 mNestedScrollView.setOnScrollChangeListener(new NestedScrollView.OnScrollChangeListener(){...}) inside unreachable setupDialog', 'SOURCE')
UNREACHABLE['PropertiesSheet$1.onScrollChange'] = ('no_trigger_in_app', 'Callback only fires if the listener created in setupDialog is registered, but setupDialog never executes', 'SRC fragments/PropertiesSheet.java:87-94 onScrollChange body inside unreachable setupDialog', 'SOURCE')
UNREACHABLE['PropertiesSheet$2.<init>'] = ('no_trigger_in_app', 'Anonymous BottomSheetBehavior.BottomSheetCallback field mCallback is constructed as part of PropertiesSheet instance field initialization, which only happens if PropertiesSheet.<init> runs; it never does', 'SRC fragments/PropertiesSheet.java:117-129 private BottomSheetBehavior.BottomSheetCallback mCallback = new BottomSheetBehavior.BottomSheetCallback(){...}; PropertiesSheet never instantiated (see PropertiesSheet.<init> entry)', 'SOURCE')
UNREACHABLE['PropertiesSheet$2.onSlide'] = ('no_trigger_in_app', 'onSlide is invoked by BottomSheetBehavior only after setBottomSheetCallback(mCallback) runs in setupDialog, which never executes', 'SRC fragments/PropertiesSheet.java:82 mBottomSheetBehavior.setBottomSheetCallback(mCallback); line 125-128 onSlide body; both inside unreachable setupDialog', 'SOURCE')
UNREACHABLE['PropertiesSheet$2.onStateChanged'] = ('no_trigger_in_app', 'onStateChanged is invoked by BottomSheetBehavior only after setBottomSheetCallback(mCallback) runs in setupDialog, which never executes', 'SRC fragments/PropertiesSheet.java:82 mBottomSheetBehavior.setBottomSheetCallback(mCallback); line 118-123 onStateChanged body; both inside unreachable setupDialog', 'SOURCE')
UNREACHABLE['UserColorPreferences.<init>(Parcel)'] = ('no_trigger_in_app', 'Private Parcel constructor is only reachable via CREATOR.createFromParcel; the app never calls getParcelable/putParcelable or any Intent/Bundle parceling API on UserColorPreferences, it is always built with the (int,int,int,int) constructor and persisted as individual SharedPreferences ints', 'SRC ui/colors/UserColorPreferences.java:19-24 private UserColorPreferences(Parcel in); ui/colors/ColorPreferenceHelper.java:70-79 saveColorPreferences uses editor.putInt(...) for each field, not Parcelable; grep -rln "UserColorPreferences" app/src/main/java shows no putParcelable/getParcelable/putExtra call site for this class', 'SOURCE')
UNREACHABLE['UserColorPreferences.describeContents'] = ('no_trigger_in_app', 'Parcelable method never invoked; UserColorPreferences is never written to or read from a Parcel/Bundle/Intent anywhere in the app', 'SRC ui/colors/UserColorPreferences.java:34-37 describeContents(); ui/colors/ColorPreferenceHelper.java:70-79 shows persistence via SharedPreferences ints only; grep -rln "UserColorPreferences" app/src/main/java shows no parceling call site', 'SOURCE')
UNREACHABLE['UserColorPreferences.writeToParcel'] = ('no_trigger_in_app', 'Parcelable method never invoked; UserColorPreferences is never written to or read from a Parcel/Bundle/Intent anywhere in the app', 'SRC ui/colors/UserColorPreferences.java:26-32 writeToParcel(); ui/colors/ColorPreferenceHelper.java:70-79 shows persistence via SharedPreferences ints only; grep -rln "UserColorPreferences" app/src/main/java shows no parceling call site', 'SOURCE')
UNREACHABLE['CircularColorsView.<init>(Context)'] = ('no_trigger_in_app', 'The single-Context constructor is never called; grep finds no "new CircularColorsView(" call site in app code, and both XML usages (item_colorpicker.xml, selectedcolors_preference.xml) are plain view tags which the Android LayoutInflater instantiates via the (Context,AttributeSet) constructor, not this one', 'SRC ui/views/CircularColorsView.java:28-31 public CircularColorsView(Context context); grep -rn "new CircularColorsView" app/src/main/java finds zero call sites', 'SOURCE')
UNREACHABLE['FastScroller.<init>(Context,AttributeSet,int)'] = ('no_trigger_in_app', 'The three-arg constructor is never called; grep finds no "new FastScroller(" call site in app code, and the only XML usage (main_frag.xml) is a plain view tag with no style attribute, so the Android LayoutInflater uses the (Context,AttributeSet) constructor instead', 'SRC ui/views/FastScroller.java:45-49 public FastScroller(Context context, AttributeSet attributeSet, int i); grep -rn "new FastScroller" app/src/main/java finds zero call sites; res/layout/main_frag.xml:46-50 shows plain element with no style attr', 'SOURCE')
UNREACHABLE['Indicator.<init>(Context)'] = ('no_trigger_in_app', 'The single-Context constructor (which delegates to the 3-arg constructor) is never called; grep finds no "new Indicator(" call site in app code, and the only XML usage (layout-v21/main_toolbar.xml) is a plain view tag which the Android LayoutInflater instantiates via the (Context,AttributeSet) constructor, not this one', 'SRC ui/views/Indicator.java:115-117 public Indicator(Context context) { this(context, null, 0); }; grep -rn "new Indicator(" app/src/main/java finds zero call sites; res/layout-v21/main_toolbar.xml:50-55 <com.amaze.filemanager.ui.views.Indicator android:id="@+id/indicator" .../>', 'SOURCE')
UNREACHABLE['ThemedImageButton.<init>(Context)'] = ('no_trigger_in_app', 'The 1-arg constructor is never invoked: no app code calls new ThemedImageButton(context), the sibling constructors do not delegate to it (each independently calls a matching super(...) overload), and the only usage site (namepathswitch_preference.xml) is inflated by Android LayoutInflater, which always constructs XML-declared custom views via the (Context,AttributeSet) constructor, never the 1-arg constructor', 'SRC ThemedImageButton.java:14-16 public ThemedImageButton(Context context) { super(context); } (no this(...) delegation from the other constructors, confirmed by reading lines 12-37); grep -rn "new ThemedImageButton" over app/src/main/java found no matches', 'INFERRED')
UNREACHABLE['ThemedImageView.<init>(Context)'] = ('no_trigger_in_app', 'The 1-arg constructor is never invoked: no app code calls new ThemedImageView(context) (ThemedImageButton, the only subclass, does not call it either), and the only XML usage sites (fragment_sheet_cloud.xml, dialog_decrypt_fingerprint_authentication.xml, namepathswitch_preference.xml via ThemedImageButton) are inflated by Android LayoutInflater, which always constructs XML-declared custom views via the (Context,AttributeSet) constructor, never the 1-arg constructor', 'SRC ThemedImageView.java:21-23 public ThemedImageView(Context context) { this(context, null, 0); } (confirmed no app caller by reading the whole file, lines 1-54); grep -rn "new ThemedImageView" over app/src/main/java found no matches', 'INFERRED')
UNREACHABLE['DataUtils.contains(String,ArrayList)'] = ('no_trigger_in_app', 'Package-private overload int contains(String, ArrayList<String[]>) has zero call sites anywhere in DataUtils.java or the app; both live callers (containsServer(String[]) and containsBooks(String[])) pass a String[] first argument which resolves to the other overload contains(String[], ArrayList); the one line that would call the String overload (containsAccounts(CloudEntry)) is commented out', 'SRC utils/DataUtils.java:109-111 commented-out method containing the only textual call to contains(a, accounts); line 165-173 defines contains(String,ArrayList); grep -rn "contains(" over DataUtils.java shows only the String[] overload is actually invoked live', 'SOURCE')
UNREACHABLE['DatapointParcelable.<init>(Parcel)'] = ('no_trigger_in_app', 'DatapointParcelable is only ever passed between app components as a plain Java object (method params/fields on AbstractProgressiveService, ProcessViewerFragment callbacks); grep over the app finds no putParcelable/putExtra/getParcelable call for DatapointParcelable, so it is never marshalled into a Parcel and this Parcel-reading constructor is never invoked', 'SRC utils/DatapointParcelable.java:117-126 constructor reads fields from Parcel; grep -rn DatapointParcelable across app/src/main/java shows only in-memory usage (AbstractProgressiveService, ExtractService, CopyService, DecryptService, ZipService, EncryptService, ProcessViewerFragment), no Parcel/Bundle/Intent putParcelable or getParcelable calls', 'SOURCE')
UNREACHABLE['DatapointParcelable$1.createFromParcel'] = ('no_trigger_in_app', 'CREATOR.createFromParcel is only invoked by the framework when a DatapointParcelable is read back out of a Parcel/Bundle/Intent via getParcelable(ArrayList); no such call exists for DatapointParcelable anywhere in the app', 'SRC utils/DatapointParcelable.java:128-133 CREATOR anonymous class createFromParcel; grep -rn DatapointParcelable across app/src/main/java shows no getParcelable/getParcelableArrayList call for this class', 'SOURCE')
UNREACHABLE['DatapointParcelable$1.newArray'] = ('no_trigger_in_app', 'CREATOR.newArray is only invoked by the framework when unparceling a DatapointParcelable[] array from a Parcel; no DatapointParcelable is ever put into or read from a Parcel/Bundle/Intent in the app', 'SRC utils/DatapointParcelable.java:134-137 CREATOR anonymous class newArray; grep -rn DatapointParcelable across app/src/main/java shows no array unparceling call for this class', 'SOURCE')
UNREACHABLE['MainActivityHelper.isNewDirectoryRecursive'] = ('no_trigger_in_app', 'Public static utility method defined but never called anywhere else in the app source', 'SRC utils/MainActivityHelper.java:644-646 public static boolean isNewDirectoryRecursive(HybridFile file); grep -rn isNewDirectoryRecursive across app/src/main/java shows only this declaration, no call sites', 'SOURCE')
UNREACHABLE['StreamSource.read()'] = ('no_trigger_in_app', 'The no-arg single-byte read() override is never called from app code; the only live read path on a StreamSource (StreamServer.sendResponse data.read(buff)) dispatches via InputStream.read(byte[]) straight to the 3-arg read(byte[],int,int) override which independently reads from the underlying SMB input stream, never delegating to read()', 'SRC SmbStreamer/StreamSource.java:68-73 defines read(); SmbStreamer/StreamServer.java:672 while ((read = data.read(buff)) > 0) is the only call site touching a StreamSource read method and it targets read(byte[],int,int); grep -rn "\\.read()" across app/src/main/java shows no call site on a StreamSource/RandomAccessStream-typed variable', 'SOURCE')
UNREACHABLE['RandomAccessStream.availableExact'] = ('no_trigger_in_app', 'availableExact() is defined but every call site in the app is commented out', 'SRC utils/streams/RandomAccessStream.java:37-39 defines availableExact(); SmbStreamer/StreamServer.java:668,673 and utils/cloud/CloudStreamServer.java:837,842 are the only occurrences of availableExact( outside its own definition and all four are inside // line comments (//long pending = data.availableExact(); and //if(...)...data.availableExact()); grep -rn availableExact across app/src/main/java confirms no live (non-comment) call site', 'SOURCE')
UNREACHABLE['AppDataParcelable.<init>(Parcel)'] = ('no_trigger_in_app', 'AppDataParcelable is only ever constructed via the (String,String,String,String,String,long,long) constructor in AppListLoader.java:70 for an in-memory list/adapter; it is never put into a Parcel/Bundle/Intent (no putExtra/putParcelable/putParcelableArrayList/getParcelable for this type anywhere in the app), so CREATOR.createFromParcel and this private Parcel constructor never run', 'SRC adapters/data/AppDataParcelable.java:44-51 private constructor only called by CREATOR at lines 54-55; grep -rn "AppDataParcelable" app/src/main/java shows only AppListLoader.java and AppsAdapter.java usages, none of them Parcel/Bundle/Intent related', 'SOURCE')
UNREACHABLE['DonationViewHolder.<init>'] = ('no_trigger_in_app', 'DonationViewHolder is never instantiated anywhere in the app; grep shows no "new DonationViewHolder" call site outside its own file', 'SRC adapters/holders/DonationViewHolder.java:1-21; grep -rn "DonationViewHolder" app/src/main/java shows no references outside adapters/holders/DonationViewHolder.java', 'SOURCE')
UNREACHABLE['SshAuthenticationTask.<init>(String,int,String,String,String,String,KeyPair)'] = ('no_trigger_in_app', 'This is the 7-arg constructor (hostname,port,hostKey,existingHostKey,username,password,privateKey). The only call site in the app, SshConnectionPool.java:222-223, uses the 6-arg constructor (hostname,port,hostKey,username,password,keyPair) without existingHostKey; grep shows no other "new SshAuthenticationTask" call site', 'SRC asynchronous/asynctasks/ssh/SshAuthenticationTask.java:99-112 defines the 7-arg constructor; SRC filesystem/ssh/SshConnectionPool.java:222-223 new SshAuthenticationTask(host, port, hostKey, username, password, keyPair) is the only instantiation in the app and matches the 6-arg overload', 'SOURCE')
UNREACHABLE['HybridFile$2.<init>'] = ('no_trigger_in_app', 'HybridFile$2 is the anonymous SFtpClientTemplate created inside the deprecated no-arg HybridFile.length() (case SFTP); the bytecode call graph shows every call site in the app targets the non-deprecated length(Context) overload, never the no-arg length()', 'SRC filesystem/HybridFile.java:220-229 deprecated public long length() { ... case SFTP: return SshClientUtils.execute(new SFtpClientTemplate(path) {...}); ...}; auto_calls.json shows 7 callers of HybridFile.length(Context) (CountItemsOrAndSizeTask, EncryptService$BackgroundTask, DecryptService$BackgroundTask, CloudUtil.lambda$launchCloud$1, FileUtils.getBaseFileSize, FileUtils.getSpaces, SshClientUtils.lambda$launchSftp$1) and zero callers of HybridFile.length()', 'SOURCE')
UNREACHABLE['Operations.<init>'] = ('no_trigger_in_app', 'Operations is a utility class: no explicit constructor is declared and every method (mkdir, mkfile, rename, checkFolder, isCopyLoopPossible, isFileNameValid, isFileSystemFAT) is static; grep shows no "new Operations(" anywhere in the app', 'SRC filesystem/Operations.java:34-80 class declaration and first static method show no instance constructor or instance state; grep -rn "new Operations(" app/src/main/java shows no matches', 'SOURCE')
UNREACHABLE['PasteHelper.describeContents'] = ('no_trigger_in_app', 'describeContents is only invoked by the Android Parcelable marshaling machinery when an instance is actually written to a Parcel; PasteHelper is never parceled anywhere in the app', 'SRC filesystem/PasteHelper.java:31-34; grep -rn "PasteHelper" app/src/main/java shows no putParcelable/putExtra/getParcelable usage', 'SOURCE')
UNREACHABLE['Coders.addEncoder'] = ('no_trigger_in_app', 'addEncoder is only called from SevenZOutputFile.java:321 (createEncoders), and SevenZOutputFile is a library class for writing 7z archives that is never instantiated anywhere in the app (the app only reads 7z via SevenZFile); consistent with the existing UNREACHABLE entries for SevenZOutputFile.<init>(File)/<init>(SeekableByteChannel)', 'SRC commons_compress_7z/.../sevenz/Coders.java:82-89 static OutputStream addEncoder(...); SRC commons_compress_7z/.../sevenz/SevenZOutputFile.java:321 out = Coders.addEncoder(out, m.getMethod(), m.getOptions()); grep -rn "SevenZOutputFile" app/src/main/java shows no matches', 'SOURCE')
UNREACHABLE['Coders$BCJDecoder.encode'] = ('no_trigger_in_app', 'Only called via Coders.addEncoder -> cb.encode(out, options); addEncoder is unreachable because its only caller SevenZOutputFile is never instantiated in the app', 'SRC commons_compress_7z/.../sevenz/Coders.java:122-126 BCJDecoder.encode; SRC commons_compress_7z/.../sevenz/Coders.java:88 return cb.encode(out, options); in the unreachable addEncoder', 'SOURCE')
UNREACHABLE['Coders$BZIP2Decoder.encode'] = ('no_trigger_in_app', 'Only called via Coders.addEncoder -> cb.encode(out, options); addEncoder is unreachable because its only caller SevenZOutputFile is never instantiated in the app', 'SRC commons_compress_7z/.../sevenz/Coders.java:256-261 BZIP2Decoder.encode; SRC commons_compress_7z/.../sevenz/Coders.java:88 return cb.encode(out, options); in the unreachable addEncoder', 'SOURCE')
UNREACHABLE['Coders$CopyDecoder.encode'] = ('no_trigger_in_app', 'Only called via Coders.addEncoder -> cb.encode(out, options); addEncoder is unreachable because its only caller SevenZOutputFile is never instantiated in the app', 'SRC commons_compress_7z/.../sevenz/Coders.java:97-100 CopyDecoder.encode; SRC commons_compress_7z/.../sevenz/Coders.java:88 return cb.encode(out, options); in the unreachable addEncoder', 'SOURCE')
UNREACHABLE['Coders$DeflateDecoder.encode'] = ('no_trigger_in_app', 'Only called via Coders.addEncoder -> cb.encode(out, options); addEncoder is unreachable because its only caller SevenZOutputFile is never instantiated in the app', 'SRC commons_compress_7z/.../sevenz/Coders.java:150-156 DeflateDecoder.encode creates the DeflateDecoderOutputStream; SRC commons_compress_7z/.../sevenz/Coders.java:88 return cb.encode(out, options); in the unreachable addEncoder', 'SOURCE')
UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>'] = ('no_trigger_in_app', 'Only instantiated inside Coders$DeflateDecoder.encode (line 155), which is unreachable because it is only invoked via the unreachable Coders.addEncoder/SevenZOutputFile write path', 'SRC commons_compress_7z/.../sevenz/Coders.java:155 return new DeflateDecoderOutputStream(deflaterOutputStream, deflater); and 199-203 constructor', 'SOURCE')
UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderOutputStream.close'] = ('no_trigger_in_app', 'Instance method of DeflateDecoderOutputStream, which is only constructed inside the unreachable Coders$DeflateDecoder.encode (7z write path never used by the app)', 'SRC commons_compress_7z/.../sevenz/Coders.java:220-227 close() override', 'SOURCE')
UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderOutputStream.write(int)'] = ('no_trigger_in_app', 'Instance method of DeflateDecoderOutputStream, which is only constructed inside the unreachable Coders$DeflateDecoder.encode (7z write path never used by the app)', 'SRC commons_compress_7z/.../sevenz/Coders.java:205-208 write(int) override', 'SOURCE')
UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[])'] = ('no_trigger_in_app', 'Instance method of DeflateDecoderOutputStream, which is only constructed inside the unreachable Coders$DeflateDecoder.encode (7z write path never used by the app)', 'SRC commons_compress_7z/.../sevenz/Coders.java:210-213 write(byte[]) override', 'SOURCE')
UNREACHABLE['Coders$DeflateDecoder$DeflateDecoderOutputStream.write(byte[],int,int)'] = ('no_trigger_in_app', 'Instance method of DeflateDecoderOutputStream, which is only constructed inside the unreachable Coders$DeflateDecoder.encode (7z write path never used by the app)', 'SRC commons_compress_7z/.../sevenz/Coders.java:215-218 write(byte[],int,int) override', 'SOURCE')
UNREACHABLE['SevenZFile.read(byte[])'] = ('no_trigger_in_app', 'The 1-arg read(byte[]) overload is never called: the only app call site, SevenZipExtractor.java:102, calls the 3-arg read(byte[],int,int) overload, and nothing inside SevenZFile.java itself calls the 1-arg overload either', 'SRC commons_compress_7z/.../sevenz/SevenZFile.java:1087-1090 public int read(final byte[] b); SRC filesystem/compressed/extractcontents/helpers/SevenZipExtractor.java:102-103 length = sevenzFile.read(content, 0, ...); grep -n ".read(" on SevenZFile.java shows no internal call to the 1-arg overload', 'SOURCE')
UNREACHABLE['SevenZFile$2.<init>'] = ('no_trigger_in_app', 'SevenZFile$2 is the anonymous InputStreamStatistics created inside SevenZFile.getStatisticsForCurrentEntry(), which is never called anywhere in the app', 'SRC commons_compress_7z/.../sevenz/SevenZFile.java:1114-1124 getStatisticsForCurrentEntry(); grep -rn "getStatisticsForCurrentEntry" app/src/main/java shows no matches', 'SOURCE')
UNREACHABLE['SevenZFile$2.getCompressedCount'] = ('no_trigger_in_app', 'Instance method of the anonymous InputStreamStatistics returned by SevenZFile.getStatisticsForCurrentEntry(), which is never called by the app', 'SRC commons_compress_7z/.../sevenz/SevenZFile.java:1117-1120 getCompressedCount() override; grep -rn "getStatisticsForCurrentEntry\\|getCompressedCount" app/src/main/java shows no matches', 'SOURCE')
UNREACHABLE['SevenZFile$2.getUncompressedCount'] = ('no_trigger_in_app', 'Instance method of the anonymous InputStreamStatistics returned by SevenZFile.getStatisticsForCurrentEntry(), which is never called by the app', 'SRC commons_compress_7z/.../sevenz/SevenZFile.java:1121-1123 getUncompressedCount() override; grep -rn "getStatisticsForCurrentEntry\\|getUncompressedCount" app/src/main/java shows no matches', 'SOURCE')
UNREACHABLE['SevenZMethodConfiguration.getMethod'] = ('no_trigger_in_app', 'Both call sites of getMethod() are in library code that is itself unreachable: SevenZOutputFile.java (7z write path, never instantiated by the app) and CLI.java (a standalone command-line tool, already established UNREACHABLE in this graph)', 'SRC commons_compress_7z/.../sevenz/SevenZMethodConfiguration.java:69-71 getMethod(); SRC commons_compress_7z/.../sevenz/SevenZOutputFile.java:321,451-452 calls m.getMethod(); SRC commons_compress_7z/.../sevenz/CLI.java:58 sb.append(m.getMethod()); grep -rn "\\.getMethod()" commons_compress_7z/src/main/java app/src/main/java shows no other callers', 'SOURCE')
UNREACHABLE['SevenZMethodConfiguration.getOptions'] = ('no_trigger_in_app', 'Both call sites of getOptions() are in library code that is itself unreachable: SevenZOutputFile.java (7z write path, never instantiated by the app) and CLI.java (a standalone command-line tool, already established UNREACHABLE in this graph)', 'SRC commons_compress_7z/.../sevenz/SevenZMethodConfiguration.java:77-79 getOptions(); SRC commons_compress_7z/.../sevenz/SevenZOutputFile.java:321,453 calls m.getOptions(); SRC commons_compress_7z/.../sevenz/CLI.java:59-60 m.getOptions(); grep -rn "\\.getOptions()" commons_compress_7z/src/main/java app/src/main/java shows no other callers', 'SOURCE')
UNREACHABLE['SshClientTemplate.<init>(String)'] = ('no_trigger_in_app', 'The 1-arg constructor (url) just delegates to the 2-arg constructor (this(url, true)); every anonymous subclass instantiation in the app passes both arguments explicitly, so the 1-arg constructor itself is never invoked', 'SRC filesystem/ssh/SshClientTemplate.java:45-48 public SshClientTemplate(String url) { this(url, true); }; grep -rn "new SshClientTemplate(" app/src/main/java shows 3 call sites (HybridFile.java:1021, SshClientUtils.java:95,127), all passing (url/path, false) to the 2-arg constructor', 'SOURCE')
UNREACHABLE['Statvfs$Response.getRawFileSystemId'] = ('no_trigger_in_app', 'getRawFileSystemId is a public getter never called anywhere; the app only calls diskFreeSpace()/diskSize() on Statvfs.Response instances (HybridFile.java:656-709), and toString() (which calls the related getFileSystemId(), not this method) is not invoked either', 'SRC filesystem/ssh/Statvfs.java:188-191 getRawFileSystemId(); SRC filesystem/HybridFile.java:655-663,708-716 only call response.diskFreeSpace()/response.diskSize(); grep -rn "getRawFileSystemId" app/src/main/java shows only the definition', 'SOURCE')

# Saved-state entries sit below the UNREACHABLE dict rebinding, which discards earlier assignments.
UNREACHABLE['CustomNavigationView$SavedState.<clinit>'] = (
    'closed_by_api_level',
    'Static initializer for SavedState class; class not used on API 27 due to isNavigationViewSavedStateMissing guard',
    'SRC CustomNavigationView.java:120 SavedState class; line 117 isNavigationViewSavedStateMissing blocks usage on API 23-28',
    'SOURCE')

UNREACHABLE['CustomNavigationView$SavedState.<init>(Parcelable)'] = (
    'closed_by_api_level',
    'SavedState(Parcelable) constructor not used on API 27 due to isNavigationViewSavedStateMissing guard in onSaveInstanceState',
    'SRC CustomNavigationView.java:123-125 constructor; line 67-69 guard prevents SavedState creation',
    'SOURCE')

UNREACHABLE['CustomNavigationView$SavedState.<init>(Parcel)'] = (
    'closed_by_api_level',
    'SavedState(Parcel) constructor not used on API 27 due to isNavigationViewSavedStateMissing guard in onRestoreInstanceState',
    'SRC CustomNavigationView.java:127-130 private constructor; line 84-87 guard prevents SavedState usage',
    'SOURCE')

UNREACHABLE['CustomNavigationView$SavedState.writeToParcel'] = (
    'closed_by_api_level',
    'SavedState.writeToParcel not called on API 27 because SavedState instances never created due to isNavigationViewSavedStateMissing guard',
    'SRC CustomNavigationView.java:132-135 writeToParcel method; SavedState not instantiated on API 23-28',
    'SOURCE')

UNREACHABLE['CustomNavigationView$SavedState$1.<init>'] = (
    'closed_by_api_level',
    'CREATOR anonymous class constructor; CREATOR not used on API 27 because SavedState parceling skipped',
    'SRC CustomNavigationView.java:138-145 CREATOR field; SavedState not parceled on API 23-28',
    'SOURCE')

UNREACHABLE['CustomNavigationView$SavedState$1.createFromParcel'] = (
    'closed_by_api_level',
    'CREATOR.createFromParcel not called on API 27 because SavedState not saved to Parcel',
    'SRC CustomNavigationView.java:139-141 createFromParcel method; SavedState parceling blocked by line 84-87 guard',
    'SOURCE')

UNREACHABLE['CustomNavigationView$SavedState$1.newArray'] = (
    'closed_by_api_level',
    'CREATOR.newArray not called on API 27 because SavedState not restored from Parcel',
    'SRC CustomNavigationView.java:142-144 newArray method; SavedState unparceling blocked by isNavigationViewSavedStateMissing',
    'SOURCE')

# Auto calls made from methods that are UNREACHABLE: the callers cannot run, so these calls are not routes.
sup(
    ('AES256SHA256Decoder$1.read()', 'AES256SHA256Decoder$1.init'),
    ('AES256SHA256Decoder$1.read(byte[],int,int)', 'AES256SHA256Decoder$1.init'),
    ('AES256SHA256Decoder.decode', 'AES256SHA256Decoder$1.<init>'),
    ('AppDataParcelable$1.createFromParcel', 'AppDataParcelable.<clinit>'),
    ('Archive.toString', 'Archive.lengthOf(Object[])'),
    ('Archive.toString', 'Archive.lengthOf(long[])'),
    ('CLI$Mode$1.<init>', 'CLI$Mode.<init>'),
    ('CLI$Mode$1.getContentMethods', 'SevenZMethodConfiguration.getMethod'),
    ('CLI$Mode$1.getContentMethods', 'SevenZMethodConfiguration.getOptions'),
    ('CLI$Mode$1.takeAction', 'CLI$Mode$1.getContentMethods'),
    ('CLI$Mode$1.takeAction', 'SevenZArchiveEntry.getCompressedSize'),
    ('CLI$Mode$2.<init>', 'CLI$Mode.<init>'),
    ('CLI$Mode.<clinit>', 'CLI$Mode$1.<init>'),
    ('CLI$Mode.<clinit>', 'CLI$Mode$2.<init>'),
    ('CLI$Mode.<clinit>', 'CLI$Mode.<clinit>'),
    ('CLI.grabMode', 'CLI$Mode.<clinit>'),
    ('CLI.main', 'CLI$Mode$1.takeAction'),
    ('CLI.main', 'CLI$Mode$2.takeAction'),
    ('CLI.main', 'CLI$Mode.getMessage'),
    ('CLI.main', 'CLI.grabMode'),
    ('CLI.main', 'CLI.usage'),
    ('CloudHandler.onUpgrade', 'CloudHandler.onCreate'),
    ('Coders.addEncoder', 'LZMADecoder.encode'),
    ('ComputerParcelable$1.createFromParcel', 'ComputerParcelable.<init>(Parcel)'),
    ('CopyService.checkFiles', 'CopyService.checkFiles'),
    ('CustomNavigationView$SavedState$1.createFromParcel', 'CustomNavigationView$SavedState.<clinit>'),
    ('CustomNavigationView$SavedState$1.createFromParcel', 'CustomNavigationView$SavedState.<init>(Parcel)'),
    ('CustomNavigationView$SavedState.<clinit>', 'CustomNavigationView$SavedState$1.<init>'),
    ('DatapointParcelable$1.createFromParcel', 'DatapointParcelable.<init>(Parcel)'),
    ('FileUtil$MediaFile.installTemporaryTrack', 'FileUtil$MediaFile.getExternalFilesDir'),
    ('FileUtil$MediaFile.mkdir', 'FileUtil$MediaFile.<init>'),
    ('FileUtil$MediaFile.mkdir', 'FileUtil$MediaFile.delete'),
    ('FileUtil$MediaFile.mkdir', 'FileUtil$MediaFile.getTemporaryAlbumId'),
    ('FileUtils.folderSizeSftp', 'FileUtils.folderSizeSftp'),
    ('LZMADecoder.encode', 'LZMADecoder.getOptions'),
    ('LZMADecoder.getOptions', 'LZMADecoder.numberOptionOrDefault'),
    ('LZMADecoder.getOptionsAsProperties', 'LZMADecoder.getOptions'),
    ('MainActivityHelper.isNewDirectoryRecursive', 'HybridFile.getParentName'),
    ('PropertiesSheet.<init>', 'PropertiesSheet$2.<init>'),
    ('ScrimInsetsRelativeLayout.<init>(Context)', 'ScrimInsetsRelativeLayout.init'),
    ('ScrimInsetsRelativeLayout.<init>(Context,AttributeSet)', 'ScrimInsetsRelativeLayout.init'),
    ('ScrimInsetsRelativeLayout.<init>(Context,AttributeSet,int)', 'ScrimInsetsRelativeLayout.init'),
    ('SevenZArchiveEntry.setAccessDate(Date)', 'SevenZArchiveEntry.javaTimeToNtfsTime'),
    ('SevenZArchiveEntry.setCreationDate(Date)', 'SevenZArchiveEntry.javaTimeToNtfsTime'),
    ('SevenZArchiveEntry.setLastModifiedDate(Date)', 'SevenZArchiveEntry.javaTimeToNtfsTime'),
    ('SevenZFile.<init>(FileChannel)', 'SevenZFile.<init>(FileChannel,String,char[])'),
    ('SevenZFile.<init>(FileChannel,byte[])', 'SevenZFile.<init>(FileChannel,String,byte[])'),
    ('SevenZFile.<init>(FileChannel,char[])', 'SevenZFile.<init>(FileChannel,String,byte[])'),
    ('SevenZFile.toString', 'Archive.toString'),
    ('SevenZOutputFile$OutputStreamWrapper.write(byte[])', 'SevenZOutputFile$OutputStreamWrapper.write(byte[],int,int)'),
    ('SevenZOutputFile.<init>(File)', 'SevenZOutputFile.<init>(SeekableByteChannel)'),
    ('SevenZOutputFile.close', 'SevenZOutputFile.finish'),
    ('SevenZOutputFile.closeArchiveEntry', 'SevenZArchiveEntry.setCompressedCrcValue'),
    ('SevenZOutputFile.closeArchiveEntry', 'SevenZArchiveEntry.setCompressedSize'),
    ('SevenZOutputFile.createArchiveEntry', 'SevenZArchiveEntry.setLastModifiedDate(Date)'),
    ('SevenZOutputFile.finish', 'SevenZOutputFile.writeHeader'),
    ('SevenZOutputFile.getCurrentOutputStream', 'SevenZOutputFile.setupFileOutputStream'),
    ('SevenZOutputFile.setContentCompression', 'SevenZOutputFile.setContentMethods'),
    ('SevenZOutputFile.setContentMethods', 'SevenZOutputFile.reverse'),
    ('SevenZOutputFile.setupFileOutputStream', 'Coders.addEncoder'),
    ('SevenZOutputFile.setupFileOutputStream', 'SevenZMethodConfiguration.getMethod'),
    ('SevenZOutputFile.setupFileOutputStream', 'SevenZMethodConfiguration.getOptions'),
    ('SevenZOutputFile.setupFileOutputStream', 'SevenZOutputFile$1.<init>'),
    ('SevenZOutputFile.setupFileOutputStream', 'SevenZOutputFile$OutputStreamWrapper.<init>'),
    ('SevenZOutputFile.setupFileOutputStream', 'SevenZOutputFile.getContentMethods'),
    ('SevenZOutputFile.write(byte[])', 'SevenZOutputFile.write(byte[],int,int)'),
    ('SevenZOutputFile.write(byte[],int,int)', 'SevenZOutputFile.getCurrentOutputStream'),
    ('SevenZOutputFile.write(int)', 'SevenZOutputFile.getCurrentOutputStream'),
    ('SevenZOutputFile.writeFileATimes', 'SevenZArchiveEntry.getAccessDate'),
    ('SevenZOutputFile.writeFileATimes', 'SevenZArchiveEntry.javaTimeToNtfsTime'),
    ('SevenZOutputFile.writeFileATimes', 'SevenZOutputFile.writeBits'),
    ('SevenZOutputFile.writeFileATimes', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeFileAntiItems', 'SevenZArchiveEntry.isAntiItem'),
    ('SevenZOutputFile.writeFileAntiItems', 'SevenZOutputFile.writeBits'),
    ('SevenZOutputFile.writeFileAntiItems', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeFileCTimes', 'SevenZArchiveEntry.getCreationDate'),
    ('SevenZOutputFile.writeFileCTimes', 'SevenZArchiveEntry.javaTimeToNtfsTime'),
    ('SevenZOutputFile.writeFileCTimes', 'SevenZOutputFile.writeBits'),
    ('SevenZOutputFile.writeFileCTimes', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeFileEmptyFiles', 'SevenZOutputFile.writeBits'),
    ('SevenZOutputFile.writeFileEmptyFiles', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeFileEmptyStreams', 'SevenZOutputFile.writeBits'),
    ('SevenZOutputFile.writeFileEmptyStreams', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeFileMTimes', 'SevenZArchiveEntry.javaTimeToNtfsTime'),
    ('SevenZOutputFile.writeFileMTimes', 'SevenZOutputFile.writeBits'),
    ('SevenZOutputFile.writeFileMTimes', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeFileNames', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeFileWindowsAttributes', 'SevenZArchiveEntry.getWindowsAttributes'),
    ('SevenZOutputFile.writeFileWindowsAttributes', 'SevenZOutputFile.writeBits'),
    ('SevenZOutputFile.writeFileWindowsAttributes', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeFilesInfo', 'SevenZOutputFile.writeFileATimes'),
    ('SevenZOutputFile.writeFilesInfo', 'SevenZOutputFile.writeFileAntiItems'),
    ('SevenZOutputFile.writeFilesInfo', 'SevenZOutputFile.writeFileCTimes'),
    ('SevenZOutputFile.writeFilesInfo', 'SevenZOutputFile.writeFileEmptyFiles'),
    ('SevenZOutputFile.writeFilesInfo', 'SevenZOutputFile.writeFileEmptyStreams'),
    ('SevenZOutputFile.writeFilesInfo', 'SevenZOutputFile.writeFileMTimes'),
    ('SevenZOutputFile.writeFilesInfo', 'SevenZOutputFile.writeFileNames'),
    ('SevenZOutputFile.writeFilesInfo', 'SevenZOutputFile.writeFileWindowsAttributes'),
    ('SevenZOutputFile.writeFilesInfo', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeFolder', 'SevenZOutputFile.getContentMethods'),
    ('SevenZOutputFile.writeFolder', 'SevenZOutputFile.writeSingleCodec'),
    ('SevenZOutputFile.writeFolder', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeHeader', 'SevenZOutputFile.writeFilesInfo'),
    ('SevenZOutputFile.writeHeader', 'SevenZOutputFile.writeStreamsInfo'),
    ('SevenZOutputFile.writePackInfo', 'SevenZArchiveEntry.getCompressedCrcValue'),
    ('SevenZOutputFile.writePackInfo', 'SevenZArchiveEntry.getCompressedSize'),
    ('SevenZOutputFile.writePackInfo', 'SevenZOutputFile.writeUint64'),
    ('SevenZOutputFile.writeSingleCodec', 'CoderBase.getOptionsAsProperties'),
    ('SevenZOutputFile.writeSingleCodec', 'DeltaDecoder.getOptionsAsProperties'),
    ('SevenZOutputFile.writeSingleCodec', 'LZMADecoder.getOptionsAsProperties'),
    ('SevenZOutputFile.writeSingleCodec', 'SevenZMethod.getId'),
    ('SevenZOutputFile.writeSingleCodec', 'SevenZMethodConfiguration.getMethod'),
    ('SevenZOutputFile.writeSingleCodec', 'SevenZMethodConfiguration.getOptions'),
    ('SevenZOutputFile.writeStreamsInfo', 'SevenZOutputFile.writePackInfo'),
    ('SevenZOutputFile.writeStreamsInfo', 'SevenZOutputFile.writeSubStreamsInfo'),
    ('SevenZOutputFile.writeStreamsInfo', 'SevenZOutputFile.writeUnpackInfo'),
    ('SevenZOutputFile.writeUnpackInfo', 'SevenZOutputFile.writeFolder'),
    ('SevenZOutputFile.writeUnpackInfo', 'SevenZOutputFile.writeUint64'),
    ('TabFragment.parsePathForName', 'TabFragment.parseSmbPath'),
    ('ThemedImageButton.<init>(Context)', 'ThemedImageView.<init>(Context)'),
    ('UserColorPreferences$1.createFromParcel', 'UserColorPreferences.<init>(Parcel)'),
)

UNREACHABLE['SortHandler.getAllEntries'] = ('no_trigger_in_app', 'SortHandler.getAllEntries is defined but has no call site in the app; the getAllEntries calls in the app bind to CryptHandler (MainFragment.java:956, EncryptDecryptUtils.java:149) and CloudHandler (MainActivity.java:1863)', 'SRC database/SortHandler.java:124', 'SOURCE')
UNREACHABLE['Statvfs$Response.toString'] = ('no_trigger_in_app', 'toString is an override with no explicit call and no string conversion of Statvfs.Response in the app; HybridFile.java:655 and 708 only construct and retrieve the response', 'SRC filesystem/ssh/Statvfs.java:208-224', 'SOURCE')
UNREACHABLE['Statvfs$Response.getFileSystemId'] = ('no_trigger_in_app', 'Called only from Statvfs$Response.toString (Statvfs.java:219), which has no caller; no other reference to getFileSystemId in the app', 'SRC filesystem/ssh/Statvfs.java:178', 'SOURCE')
# Auto calls from UNREACHABLE callers, or inside SDK 23-28 guards (not API 27): not routes.
sup(
    ('CustomNavigationView.onSaveInstanceState', 'CustomNavigationView$SavedState.<clinit>'),
    ('CustomNavigationView.onSaveInstanceState', 'CustomNavigationView$SavedState.<init>(Parcelable)'),
    ('GlideOptions.bitmapTransform', 'GlideOptions.<init>'),
    ('GlideOptions.bitmapTransform', 'GlideOptions.transform(Transformation)'),
    ('GlideOptions.centerCropTransform', 'GlideOptions.<init>'),
    ('GlideOptions.centerCropTransform', 'GlideOptions.autoClone'),
    ('GlideOptions.centerCropTransform', 'GlideOptions.centerCrop'),
    ('GlideOptions.centerInsideTransform', 'GlideOptions.<init>'),
    ('GlideOptions.centerInsideTransform', 'GlideOptions.autoClone'),
    ('GlideOptions.centerInsideTransform', 'GlideOptions.centerInside'),
    ('GlideOptions.circleCropTransform', 'GlideOptions.<init>'),
    ('GlideOptions.circleCropTransform', 'GlideOptions.autoClone'),
    ('GlideOptions.circleCropTransform', 'GlideOptions.circleCrop'),
    ('GlideOptions.decodeTypeOf', 'GlideOptions.<init>'),
    ('GlideOptions.decodeTypeOf', 'GlideOptions.decode'),
    ('GlideOptions.diskCacheStrategyOf', 'GlideOptions.<init>'),
    ('GlideOptions.diskCacheStrategyOf', 'GlideOptions.diskCacheStrategy'),
    ('GlideOptions.downsampleOf', 'GlideOptions.<init>'),
    ('GlideOptions.downsampleOf', 'GlideOptions.downsample'),
    ('GlideOptions.encodeFormatOf', 'GlideOptions.<init>'),
    ('GlideOptions.encodeFormatOf', 'GlideOptions.encodeFormat'),
    ('GlideOptions.encodeQualityOf', 'GlideOptions.<init>'),
    ('GlideOptions.encodeQualityOf', 'GlideOptions.encodeQuality'),
    ('GlideOptions.errorOf(Drawable)', 'GlideOptions.<init>'),
    ('GlideOptions.errorOf(Drawable)', 'GlideOptions.error(Drawable)'),
    ('GlideOptions.errorOf(int)', 'GlideOptions.<init>'),
    ('GlideOptions.errorOf(int)', 'GlideOptions.error(int)'),
    ('GlideOptions.fitCenterTransform', 'GlideOptions.<init>'),
    ('GlideOptions.fitCenterTransform', 'GlideOptions.autoClone'),
    ('GlideOptions.fitCenterTransform', 'GlideOptions.fitCenter'),
    ('GlideOptions.formatOf', 'GlideOptions.<init>'),
    ('GlideOptions.formatOf', 'GlideOptions.format'),
    ('GlideOptions.frameOf', 'GlideOptions.<init>'),
    ('GlideOptions.frameOf', 'GlideOptions.frame'),
    ('GlideOptions.noAnimation', 'GlideOptions.<init>'),
    ('GlideOptions.noAnimation', 'GlideOptions.autoClone'),
    ('GlideOptions.noAnimation', 'GlideOptions.dontAnimate'),
    ('GlideOptions.noTransformation', 'GlideOptions.<init>'),
    ('GlideOptions.noTransformation', 'GlideOptions.autoClone'),
    ('GlideOptions.noTransformation', 'GlideOptions.dontTransform'),
    ('GlideOptions.option', 'GlideOptions.<init>'),
    ('GlideOptions.option', 'GlideOptions.set'),
    ('GlideOptions.overrideOf(int)', 'GlideOptions.<init>'),
    ('GlideOptions.overrideOf(int)', 'GlideOptions.override(int)'),
    ('GlideOptions.overrideOf(int,int)', 'GlideOptions.<init>'),
    ('GlideOptions.overrideOf(int,int)', 'GlideOptions.override(int,int)'),
    ('GlideOptions.placeholderOf(Drawable)', 'GlideOptions.<init>'),
    ('GlideOptions.placeholderOf(Drawable)', 'GlideOptions.placeholder(Drawable)'),
    ('GlideOptions.placeholderOf(int)', 'GlideOptions.<init>'),
    ('GlideOptions.placeholderOf(int)', 'GlideOptions.placeholder(int)'),
    ('GlideOptions.priorityOf', 'GlideOptions.<init>'),
    ('GlideOptions.priorityOf', 'GlideOptions.priority'),
    ('GlideOptions.signatureOf', 'GlideOptions.<init>'),
    ('GlideOptions.signatureOf', 'GlideOptions.signature'),
    ('GlideOptions.sizeMultiplierOf', 'GlideOptions.<init>'),
    ('GlideOptions.sizeMultiplierOf', 'GlideOptions.sizeMultiplier'),
    ('GlideOptions.skipMemoryCacheOf', 'GlideOptions.<init>'),
    ('GlideOptions.skipMemoryCacheOf', 'GlideOptions.skipMemoryCache'),
    ('GlideOptions.timeoutOf', 'GlideOptions.<init>'),
    ('GlideOptions.timeoutOf', 'GlideOptions.timeout'),
    ('GlideRequest.getDownloadOnlyRequest', 'GlideRequest.<init>(Class,RequestBuilder)'),
    ('GlideRequest.getDownloadOnlyRequest', 'GlideRequest.apply'),
    ('GlideRequests.setRequestOptions', 'GlideOptions.<init>'),
    ('GlideRequests.setRequestOptions', 'GlideOptions.apply'),
    ('HybridFile.length()@HybridFileParcelable', 'HybridFile$2.<init>'),
    ('Statvfs$Response.toString', 'Statvfs$Response.getFileSystemId'),
)

sup(
    ('AppDataParcelable$1.createFromParcel', 'AppDataParcelable.<init>(Parcel)'),
    ('FileUtil$MediaFile.getTemporaryAlbumId', 'FileUtil$MediaFile.installTemporaryTrack'),
    ('FileUtil.copyDummyFiles', 'FileUtil.copyDummyFile'),
    ('HybridFile.length()', 'HybridFile$2.<init>'),
    ('Coders.addEncoder', 'CoderBase.encode'),
    ('Coders.addEncoder', 'Coders$BCJDecoder.encode'),
    ('Coders.addEncoder', 'Coders$BZIP2Decoder.encode'),
    ('Coders.addEncoder', 'Coders$CopyDecoder.encode'),
    ('Coders.addEncoder', 'Coders$DeflateDecoder.encode'),
    ('Coders$DeflateDecoder.encode', 'Coders$DeflateDecoder$DeflateDecoderOutputStream.<init>'),
    ('Coders.addEncoder', 'DeltaDecoder.encode'),
    ('Coders.addEncoder', 'LZMA2Decoder.encode'),
    ('LZMA2Decoder.encode', 'LZMA2Decoder.getOptions'),
    ('SevenZFile.getStatisticsForCurrentEntry', 'SevenZFile$2.<init>'),
    ('PropertiesSheet.setupDialog', 'PropertiesSheet$1.<init>'),
    ('SmbConnectDialog.setTint', 'SmbConnectDialog.createEditTextColorStateList'),
)

e('AppListLoader.onStopLoading', 'AppListLoader.onReset', 'LIFECYCLE',
  'Loader reset runs after the loader is stopped: LoaderManager resets the loader when its host is destroyed, and onReset calls onStopLoading first (androidx source not read)',
  evidence='SRC AppListLoader.java:143-146 onReset() calls onStopLoading(); INFERRED LoaderManager calls Loader.reset() when the host is destroyed')

e('CompressedExplorerFragment$1.onActionItemClicked', 'Decompressor.decompress(String,String[])@RarDecompressor', 'CALL',
  'Extract action on a .rar: the fragment decompressor is a RarDecompressor (CompressedHelper.getCompressorInstance), and decompress(String,String[]) runs with that receiver',
  evidence='SRC fragments/CompressedExplorerFragment.java:329 decompressor.decompress(compressedFile.getPath(), dirs); SRC filesystem/compressed/CompressedHelper.java:113-114')

e('CompressedExplorerAdapter.lambda$onBindViewHolder$2', 'Decompressor.decompress(String,String[])@RarDecompressor', 'CALL',
  'Tap-to-extract on a .rar: the adapter decompressor is the RarDecompressor the fragment passes in (CompressedHelper.getCompressorInstance)',
  evidence='SRC adapters/CompressedExplorerAdapter.java:290 decompressor.decompress(...); SRC fragments/CompressedExplorerFragment.java:215,243')
