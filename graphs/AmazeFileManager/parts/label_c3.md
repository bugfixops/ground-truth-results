STATUS: RUNNING 2026-10-27T21:07:05

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| BottomBar.<init> | REACHABLE | | Called from AppBar.<init> which is called from MainActivity.onCreate | SRC activities/MainActivity.java:290, ui/views/appbar/AppBar.java:36, ui/views/appbar/BottomBar.java:80 |
| BottomBar.setClickListener | REACHABLE | | Called from MainFragment.onActivityCreated and MainActivity.onFragmentChangedListener | SRC fragments/MainFragment.java:281, activities/MainActivity.java:854 |
| BottomBar.resetClickListener | REACHABLE | | Called from MainActivity.onFragmentChangedListener | SRC activities/MainActivity.java:892 |
| BottomBar.setPathText | REACHABLE | | Called from MainFragment.reloadListElements | SRC fragments/MainFragment.java:1604,1625,1650 |
| BottomBar.setFullPathText | REACHABLE | | Called from MainFragment.reloadListElements | SRC fragments/MainFragment.java:1605,1626,1651 |
| BottomBar.areButtonsShowing | UNREACHABLE | no_trigger_in_app | Method not called; unused helper | SRC ui/views/appbar/BottomBar.java:183-185; grep shows no callers |
| BottomBar.showButtons | REACHABLE | | Called from BottomBar$2.onSingleTapConfirmed and BottomBar.updatePath | SRC ui/views/appbar/BottomBar.java:134,139,469 |
| BottomBar.updatePath | REACHABLE | | Called from MainFragment.updateTabWithDb, TabFragment.onTabChanged, CompressedExplorerFragment.updateBottomBar | SRC fragments/MainFragment.java:451, fragments/TabFragment.java:222,305, fragments/CompressedExplorerFragment.java:445 |
| BottomBar.setBackgroundColor | REACHABLE | | Called from MainActivity.updateViews | SRC activities/MainActivity.java:1475 |
| BottomBar.setVisibility | REACHABLE | | Called from AppsListFragment, FtpServerFragment, ProcessViewerFragment | SRC fragments/AppsListFragment.java:84, fragments/FtpServerFragment.java:157, fragments/ProcessViewerFragment.java:143 |
| BottomBar.createArrow | REACHABLE | | Called from BottomBar.showButtons | SRC ui/views/appbar/BottomBar.java:232 |
| BottomBar.createFolderButton | REACHABLE | | Called from BottomBar.showButtons | SRC ui/views/appbar/BottomBar.java:223 |
| BottomBar.sendScroll | REACHABLE | | Called from BottomBar.updatePath animations | SRC ui/views/appbar/BottomBar.java:361,390,408,433,462 |
| BottomBar.onTouch | REACHABLE | | Set as touch listener via setClickListener | SRC ui/views/appbar/BottomBar.java:152 |
| BottomBar.lambda$showButtons$0 | REACHABLE | | Lambda from BottomBar.showButtons button root click | SRC ui/views/appbar/BottomBar.java:197 |
| BottomBar.lambda$showButtons$1 | REACHABLE | | Lambda from BottomBar.showButtons button storage click | SRC ui/views/appbar/BottomBar.java:217 |
| BottomBar.lambda$showButtons$2 | REACHABLE | | Lambda from BottomBar.showButtons folder button click | SRC ui/views/appbar/BottomBar.java:225 |
| BottomBar.lambda$showButtons$3 | REACHABLE | | Lambda from BottomBar.showButtons post action | SRC ui/views/appbar/BottomBar.java:235 |
| BottomBar.lambda$sendScroll$4 | REACHABLE | | Lambda from BottomBar.sendScroll | SRC ui/views/appbar/BottomBar.java:476 |
| BottomBar$1.<init> | REACHABLE | | Anonymous CountDownTimer created in BottomBar.<init> | SRC ui/views/appbar/BottomBar.java:111 |
| BottomBar$1.onTick | REACHABLE | | Framework calls timer tick | SRC ui/views/appbar/BottomBar.java:113 |
| BottomBar$1.onFinish | REACHABLE | | Framework calls timer finish | SRC ui/views/appbar/BottomBar.java:115 |
| BottomBar$2.<init> | REACHABLE | | Anonymous GestureDetector.SimpleOnGestureListener created in BottomBar.<init> | SRC ui/views/appbar/BottomBar.java:119 |
| BottomBar$2.onDown | REACHABLE | | Framework gesture detection | SRC ui/views/appbar/BottomBar.java:121 |
| BottomBar$2.onSingleTapConfirmed | REACHABLE | | Framework gesture detection | SRC ui/views/appbar/BottomBar.java:125 |
| BottomBar$2.onLongPress | REACHABLE | | Framework gesture detection | SRC ui/views/appbar/BottomBar.java:144 |
| BottomBar$3.<init> | REACHABLE | | AnimatorListenerAdapter created in BottomBar.updatePath forward navigation | SRC ui/views/appbar/BottomBar.java:346 |
| BottomBar$3.onAnimationStart | REACHABLE | | Framework animation lifecycle | SRC ui/views/appbar/BottomBar.java:356 |
| BottomBar$3.onAnimationEnd | REACHABLE | | Framework animation lifecycle | SRC ui/views/appbar/BottomBar.java:347 |
| BottomBar$3.onAnimationCancel | UNREACHABLE | framework_never_calls | Animation cancellation not triggered in app usage | SRC ui/views/appbar/BottomBar.java:368-371 |
| BottomBar$3.lambda$onAnimationStart$1 | REACHABLE | | Lambda from onAnimationStart | SRC ui/views/appbar/BottomBar.java:361 |
| BottomBar$3.lambda$onAnimationEnd$0 | REACHABLE | | Lambda from onAnimationEnd | SRC ui/views/appbar/BottomBar.java:350 |
| BottomBar$4.<init> | REACHABLE | | AnimatorListenerAdapter created in BottomBar.updatePath backward navigation | SRC ui/views/appbar/BottomBar.java:373 |
| BottomBar$4.onAnimationStart | REACHABLE | | Framework animation lifecycle | SRC ui/views/appbar/BottomBar.java:385 |
| BottomBar$4.onAnimationEnd | REACHABLE | | Framework animation lifecycle | SRC ui/views/appbar/BottomBar.java:375 |
| BottomBar$4.lambda$onAnimationStart$1 | REACHABLE | | Lambda from onAnimationStart | SRC ui/views/appbar/BottomBar.java:390 |
| BottomBar$4.lambda$onAnimationEnd$0 | REACHABLE | | Lambda from onAnimationEnd | SRC ui/views/appbar/BottomBar.java:378 |
| BottomBar$5.<init> | REACHABLE | | AnimatorListenerAdapter created in BottomBar.updatePath initial path | SRC ui/views/appbar/BottomBar.java:398 |
| BottomBar$5.onAnimationStart | REACHABLE | | Framework animation lifecycle | SRC ui/views/appbar/BottomBar.java:401 |
| BottomBar$5.onAnimationEnd | REACHABLE | | Framework animation lifecycle | SRC ui/views/appbar/BottomBar.java:410 |
| BottomBar$5.onAnimationCancel | UNREACHABLE | framework_never_calls | Animation cancellation not triggered in app usage | SRC ui/views/appbar/BottomBar.java:418-421 |
| BottomBar$5.lambda$onAnimationStart$0 | REACHABLE | | Lambda from onAnimationStart | SRC ui/views/appbar/BottomBar.java:408 |
| BottomBar$5.lambda$onAnimationEnd$1 | REACHABLE | | Lambda from onAnimationEnd | SRC ui/views/appbar/BottomBar.java:411 |
| BottomBar$6.<init> | REACHABLE | | AnimatorListenerAdapter created in BottomBar.updatePath different path | SRC ui/views/appbar/BottomBar.java:425 |
| BottomBar$6.onAnimationStart | REACHABLE | | Framework animation lifecycle | SRC ui/views/appbar/BottomBar.java:428 |
| BottomBar$6.onAnimationEnd | REACHABLE | | Framework animation lifecycle | SRC ui/views/appbar/BottomBar.java:437 |
| BottomBar$6.onAnimationCancel | UNREACHABLE | framework_never_calls | Animation cancellation not triggered in app usage | SRC ui/views/appbar/BottomBar.java:470-473 |
| BottomBar$6.lambda$onAnimationStart$0 | REACHABLE | | Lambda from onAnimationStart | SRC ui/views/appbar/BottomBar.java:433 |
| BottomBar$6$1.<init> | REACHABLE | | Nested AnimatorListenerAdapter created in BottomBar$6.onAnimationEnd | SRC ui/views/appbar/BottomBar.java:446 |
| BottomBar$6$1.onAnimationStart | REACHABLE | | Framework animation lifecycle | SRC ui/views/appbar/BottomBar.java:459 |
| BottomBar$6$1.onAnimationEnd | REACHABLE | | Framework animation lifecycle | SRC ui/views/appbar/BottomBar.java:448 |
| BottomBar$6$1.lambda$onAnimationStart$1 | REACHABLE | | Lambda from onAnimationStart | SRC ui/views/appbar/BottomBar.java:462 |
| BottomBar$6$1.lambda$onAnimationEnd$0 | REACHABLE | | Lambda from onAnimationEnd | SRC ui/views/appbar/BottomBar.java:451 |
| Bzip2HelperTask.<init> | REACHABLE | | Created by Bzip2Decompressor.changePath | SRC filesystem/compressed/showcontents/helpers/Bzip2Decompressor.java:43 |
| Bzip2HelperTask.addElements | REACHABLE | | Called from CompressedHelperTask.doInBackground | SRC asynchronous/asynctasks/compress/CompressedHelperTask.java:53 |
| Bzip2Extractor.<init> | REACHABLE | | Created by CompressedHelper.getExtractorInstance for .tar.bz2/.tbz files | SRC filesystem/compressed/CompressedHelper.java:90,174 |
| Bzip2Extractor.extractWithFilter | REACHABLE | | Called from Extractor base class | SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:49 |
| Bzip2Extractor.extractEntry | REACHABLE | | Called from Bzip2Extractor.extractWithFilter | SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:68 |
| Bzip2Decompressor.<init> | REACHABLE | | Created by CompressedHelper.getCompressorInstance for .tar.bz2/.tbz files | SRC filesystem/compressed/CompressedHelper.java:120,174 |
| Bzip2Decompressor.changePath | REACHABLE | | Called from CompressedExplorerFragment.changePath | SRC fragments/CompressedExplorerFragment.java:411 |
| BoundedFileChannelInputStream.<init> | REACHABLE | | Created by SevenZFile for reading 7z archives | SRC sevenz/SevenZFile.java:371,429,998 |
| BoundedFileChannelInputStream.read()I | REACHABLE | | Called during stream reading operations | SRC sevenz/BoundedFileChannelInputStream.java:44 |
| BoundedFileChannelInputStream.read(I)I | REACHABLE | | Private helper called from read()I and read([BII)I | SRC sevenz/BoundedFileChannelInputStream.java:83-88 |
| BoundedFileChannelInputStream.read([BII)I | REACHABLE | | Called during stream reading operations | SRC sevenz/BoundedFileChannelInputStream.java:59 |
| BoundedFileChannelInputStream.close | UNREACHABLE | framework_never_calls | Close method explicitly empty; channel controlled externally | SRC sevenz/BoundedFileChannelInputStream.java:91-93; comment states nested channel controlled externally |
| CLI.<init> | UNREACHABLE | no_trigger_in_app | Command-line tool not instantiated by app | SRC sevenz/CLI.java:24; grep shows no app usage |
| CLI.main | UNREACHABLE | no_trigger_in_app | Command-line entry point not called by Android app | SRC sevenz/CLI.java:114; main method unused in app context |
| CLI.usage | UNREACHABLE | no_trigger_in_app | Called only from unused CLI.main | SRC sevenz/CLI.java:132; only caller is CLI.main |
| CLI.grabMode | UNREACHABLE | no_trigger_in_app | Called only from unused CLI.main | SRC sevenz/CLI.java:136; only caller is CLI.main |

STATUS: DONE 21:17
