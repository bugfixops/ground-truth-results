# ---- Helper chunk_3 label part (2026-10-27)
# Classes: BottomBar and inner classes, BoundedFileChannelInputStream, Bzip2* classes, CLI
# 69 methods total from chunk_3.txt

# BottomBar routes
e('MainActivity.onCreate', 'AppBar.<init>', 'CONSTRUCTED', 'Activity created, appbar initialized',
  evidence='SRC activities/MainActivity.java:277,290')

e('AppBar.<init>', 'BottomBar.<init>', 'CONSTRUCTED', 'AppBar creates BottomBar in constructor',
  evidence='SRC ui/views/appbar/AppBar.java:33,36')

e('BottomBar.<init>', 'BottomBar$1.<init>', 'CONSTRUCTED', 'Anonymous CountDownTimer created in BottomBar constructor',
  evidence='SRC ui/views/appbar/BottomBar.java:111')

e('BottomBar.<init>', 'BottomBar$2.<init>', 'CONSTRUCTED', 'Anonymous GestureDetector.SimpleOnGestureListener created in BottomBar constructor',
  evidence='SRC ui/views/appbar/BottomBar.java:119')

e('MainFragment.onActivityCreated', 'BottomBar.setClickListener', 'CALL', 'Fragment lifecycle sets touch listeners',
  evidence='SRC fragments/MainFragment.java:267,281')

e('MainActivity.onFragmentChangedListener', 'BottomBar.setClickListener', 'CALL', 'Fragment change sets listeners',
  evidence='SRC activities/MainActivity.java:854')

e('BottomBar$2.onSingleTapConfirmed', 'BottomBar.showButtons', 'CALL', 'Gesture triggers button display',
  evidence='SRC ui/views/appbar/BottomBar.java:124,134,139')

e('BottomBar.showButtons', 'BottomBar$3.<init>', 'CONSTRUCTED', 'AnimatorListenerAdapter for forward navigation created',
  evidence='SRC ui/views/appbar/BottomBar.java:346')

e('BottomBar.showButtons', 'BottomBar$4.<init>', 'CONSTRUCTED', 'AnimatorListenerAdapter for backward navigation created',
  evidence='SRC ui/views/appbar/BottomBar.java:373')

e('BottomBar.showButtons', 'BottomBar$5.<init>', 'CONSTRUCTED', 'AnimatorListenerAdapter for initial path created',
  evidence='SRC ui/views/appbar/BottomBar.java:398')

e('BottomBar.showButtons', 'BottomBar$6.<init>', 'CONSTRUCTED', 'AnimatorListenerAdapter for different path slideout created',
  evidence='SRC ui/views/appbar/BottomBar.java:425')

e('BottomBar$6.onAnimationEnd', 'BottomBar$6$1.<init>', 'CONSTRUCTED', 'Nested AnimatorListenerAdapter for slidein created',
  evidence='SRC ui/views/appbar/BottomBar.java:446')

e('MainFragment.updateTabWithDb', 'BottomBar.updatePath', 'CALL', 'Fragment updates path display',
  evidence='SRC fragments/MainFragment.java:451')

e('TabFragment.onTabChanged', 'BottomBar.updatePath', 'CALL', 'Tab change updates path',
  evidence='SRC fragments/TabFragment.java:222,305')

e('CompressedExplorerFragment.updateBottomBar', 'BottomBar.updatePath', 'CALL', 'Compressed explorer updates path',
  evidence='SRC fragments/CompressedExplorerFragment.java:445')

e('MainFragment.reloadListElements', 'BottomBar.setPathText', 'CALL', 'Search UI updates path text',
  evidence='SRC fragments/MainFragment.java:1604,1625,1650')

e('MainFragment.reloadListElements', 'BottomBar.setFullPathText', 'CALL', 'Search UI updates full path text',
  evidence='SRC fragments/MainFragment.java:1605,1626,1651')

e('AppsListFragment.onViewCreated', 'BottomBar.setVisibility', 'CALL', 'Apps list hides bottom bar',
  evidence='SRC fragments/AppsListFragment.java:84')

e('FtpServerFragment.onViewCreated', 'BottomBar.setVisibility', 'CALL', 'FTP fragment hides bottom bar',
  evidence='SRC fragments/FtpServerFragment.java:157')

e('ProcessViewerFragment.onViewCreated', 'BottomBar.setVisibility', 'CALL', 'Process viewer hides bottom bar',
  evidence='SRC fragments/ProcessViewerFragment.java:143')

e('MainActivity.onFragmentChangedListener', 'BottomBar.resetClickListener', 'CALL', 'Fragment change resets listeners',
  evidence='SRC activities/MainActivity.java:892')

e('MainActivity.updateViews', 'BottomBar.setBackgroundColor', 'CALL', 'Theme change updates background',
  evidence='SRC activities/MainActivity.java:1475')

e('BottomBar.updatePath', 'BottomBar.showButtons', 'CALL', 'Path update may trigger button display',
  evidence='SRC ui/views/appbar/BottomBar.java:469')

e('BottomBar.updatePath', 'BottomBar.sendScroll', 'CALL', 'Path animation scrolls view',
  evidence='SRC ui/views/appbar/BottomBar.java:361,390,408,433,462')

e('BottomBar.showButtons', 'BottomBar.createArrow', 'CALL', 'Button generation creates arrow icons',
  evidence='SRC ui/views/appbar/BottomBar.java:232')

e('BottomBar.showButtons', 'BottomBar.createFolderButton', 'CALL', 'Button generation creates folder buttons',
  evidence='SRC ui/views/appbar/BottomBar.java:223')

e('BottomBar.onTouch', 'BottomBar$2.onDown', 'CALL', 'Touch delegated to gesture detector',
  evidence='INFERRED source not read')

e('BottomBar.onTouch', 'BottomBar$2.onSingleTapConfirmed', 'CALL', 'Touch delegated to gesture detector',
  evidence='INFERRED source not read')

e('BottomBar.onTouch', 'BottomBar$2.onLongPress', 'CALL', 'Touch delegated to gesture detector',
  evidence='INFERRED source not read')

e('BottomBar$1.onTick', 'BottomBar$1.onFinish', 'CALL', 'Timer lifecycle',
  evidence='INFERRED source not read')

e('BottomBar$3.onAnimationStart', 'BottomBar$3.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$3.onAnimationEnd', 'BottomBar$3.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$4.onAnimationStart', 'BottomBar$4.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$4.onAnimationEnd', 'BottomBar$4.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$5.onAnimationStart', 'BottomBar$5.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$5.onAnimationEnd', 'BottomBar$5.lambda$onAnimationEnd$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$6.onAnimationStart', 'BottomBar$6.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$6$1.onAnimationStart', 'BottomBar$6$1.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

e('BottomBar$6$1.onAnimationEnd', 'BottomBar$6$1.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='INFERRED source not read')

# Bzip2 routes
e('CompressedHelper.getExtractorInstance', 'Bzip2Extractor.<init>', 'CONSTRUCTED', 'Extractor created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:89,90,174')

e('ExtractService$DataHolder.run', 'CompressedHelper.getExtractorInstance', 'CALL', 'Extract service gets extractor',
  evidence='SRC asynchronous/services/ExtractService.java:259')

e('Bzip2Extractor.<init>', 'Bzip2Extractor.extractWithFilter', 'CALL', 'Extractor base class calls extractWithFilter',
  evidence='INFERRED source not read')

e('CompressedHelper.getCompressorInstance', 'Bzip2Decompressor.<init>', 'CONSTRUCTED', 'Decompressor created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:119,120,174')

e('CompressedExplorerFragment.onViewCreated', 'CompressedHelper.getCompressorInstance', 'CALL', 'Fragment gets decompressor',
  evidence='SRC fragments/CompressedExplorerFragment.java:215,243')

e('MainActivityHelper.openCompressed', 'CompressedHelper.getCompressorInstance', 'CALL', 'Helper opens compressed file',
  evidence='SRC utils/MainActivityHelper.java:528')

e('CompressedExplorerFragment.changePath', 'Bzip2Decompressor.changePath', 'CALL', 'Fragment navigates in archive',
  evidence='SRC fragments/CompressedExplorerFragment.java:411')

e('Bzip2Decompressor.changePath', 'Bzip2HelperTask.<init>', 'CONSTRUCTED', 'Decompressor creates async task',
  evidence='SRC filesystem/compressed/showcontents/helpers/Bzip2Decompressor.java:43')

e('Bzip2HelperTask.<init>', 'Bzip2HelperTask.addElements', 'CALL', 'AsyncTask doInBackground calls addElements',
  evidence='SRC asynchronous/asynctasks/compress/CompressedHelperTask.java:53')

e('Bzip2Extractor.extractWithFilter', 'Bzip2Extractor.extractEntry', 'CALL', 'Extraction loop processes entries',
  evidence='SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:68')

# SevenZ/BoundedFileChannelInputStream routes
e('CompressedHelper.getExtractorInstance', 'SevenZipExtractor.<init>', 'CONSTRUCTED', 'Extractor created for .7z files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:95,96,185')

e('CompressedHelper.getCompressorInstance', 'SevenZipDecompressor.<init>', 'CONSTRUCTED', 'Decompressor created for .7z files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:125,126,185')

e('SevenZFile.<init>', 'BoundedFileChannelInputStream.<init>', 'CONSTRUCTED', 'SevenZ reader creates bounded stream for header',
  evidence='SRC sevenz/SevenZFile.java:371,429,998')

e('BoundedFileChannelInputStream.<init>', 'BoundedFileChannelInputStream.read()I', 'CALL', 'Stream read methods invoked during decompression',
  evidence='INFERRED source not read')

e('BoundedFileChannelInputStream.<init>', 'BoundedFileChannelInputStream.read([BII)I', 'CALL', 'Stream read methods invoked during decompression',
  evidence='INFERRED source not read')

e('BoundedFileChannelInputStream.read()I', 'BoundedFileChannelInputStream.read(I)I', 'CALL', 'Public read calls private helper',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:47')

e('BoundedFileChannelInputStream.read([BII)I', 'BoundedFileChannelInputStream.read(I)I', 'CALL', 'Public read calls private helper',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:71')

# UNREACHABLE methods
UNREACHABLE_CHUNK_3 = {
    'BottomBar.areButtonsShowing': ('no_trigger_in_app', 'Method not called; appears to be unused helper', 'SRC ui/views/appbar/BottomBar.java:183-185; grep shows no callers', 'SOURCE'),
    
    'BottomBar$3.onAnimationCancel': ('framework_never_calls', 'Animation cancellation not triggered in app usage', 'SRC ui/views/appbar/BottomBar.java:368-371; animation cancel not reached', 'SOURCE'),
    
    'BottomBar$5.onAnimationCancel': ('framework_never_calls', 'Animation cancellation not triggered in app usage', 'SRC ui/views/appbar/BottomBar.java:418-421; animation cancel not reached', 'SOURCE'),
    
    'BottomBar$6.onAnimationCancel': ('framework_never_calls', 'Animation cancellation not triggered in app usage', 'SRC ui/views/appbar/BottomBar.java:470-473; animation cancel not reached', 'SOURCE'),
    
    'CLI.<init>': ('no_trigger_in_app', 'Command-line tool not instantiated by app', 'SRC sevenz/CLI.java:24; grep -rn "new CLI" shows no app usage', 'SOURCE'),
    
    'CLI.main': ('no_trigger_in_app', 'Command-line entry point not called by Android app', 'SRC sevenz/CLI.java:114; main method unused in app context', 'SOURCE'),
    
    'CLI.usage': ('no_trigger_in_app', 'Called only from unused CLI.main', 'SRC sevenz/CLI.java:132; only caller is CLI.main', 'SOURCE'),
    
    'CLI.grabMode': ('no_trigger_in_app', 'Called only from unused CLI.main', 'SRC sevenz/CLI.java:136; only caller is CLI.main', 'SOURCE'),
    
    'BoundedFileChannelInputStream.close': ('framework_never_calls', 'Close method explicitly empty; externally controlled', 'SRC sevenz/BoundedFileChannelInputStream.java:91-93; comment states nested channel controlled externally', 'SOURCE'),
}

