STATUS: RUNNING 21:26

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| BottomBar$5.<init> | REACHABLE | | Created by BottomBar.showButtons via CONSTRUCTED edge | SRC ui/views/appbar/BottomBar.java:398 |
| BottomBar$5.onAnimationStart | REACHABLE | | Framework calls via animation lifecycle | SRC ui/views/appbar/BottomBar.java:400-404 |
| BottomBar$5.onAnimationEnd | REACHABLE | | Framework calls via animation lifecycle | SRC ui/views/appbar/BottomBar.java:407-414 |
| BottomBar$5.onAnimationCancel | UNREACHABLE | framework_never_calls | Animation cancellation not triggered in app usage | SRC ui/views/appbar/BottomBar.java:418-421 |
| BottomBar$5.lambda$onAnimationStart$0 | REACHABLE | | Called from onAnimationStart via lambda | SRC ui/views/appbar/BottomBar.java:404 |
| BottomBar$5.lambda$onAnimationEnd$1 | REACHABLE | | Called from onAnimationEnd via lambda | SRC ui/views/appbar/BottomBar.java:409-412 |
| BottomBar$6.<init> | REACHABLE | | Created by BottomBar.showButtons via CONSTRUCTED edge | SRC ui/views/appbar/BottomBar.java:425 |
| BottomBar$6.onAnimationStart | REACHABLE | | Framework calls via animation lifecycle | SRC ui/views/appbar/BottomBar.java:428-433 |
| BottomBar$6.onAnimationEnd | REACHABLE | | Framework calls via animation lifecycle | SRC ui/views/appbar/BottomBar.java:437-444 |
| BottomBar$6.onAnimationCancel | UNREACHABLE | framework_never_calls | Animation cancellation not triggered in app usage | SRC ui/views/appbar/BottomBar.java:470-473 |
| BottomBar$6.lambda$onAnimationStart$0 | REACHABLE | | Called from onAnimationStart via lambda | SRC ui/views/appbar/BottomBar.java:433 |
| BottomBar$6$1.<init> | REACHABLE | | Created by BottomBar$6.onAnimationEnd via CONSTRUCTED edge | SRC ui/views/appbar/BottomBar.java:446 |
| BottomBar$6$1.onAnimationStart | REACHABLE | | Framework calls via animation lifecycle | SRC ui/views/appbar/BottomBar.java:459-464 |
| BottomBar$6$1.onAnimationEnd | REACHABLE | | Framework calls via animation lifecycle | SRC ui/views/appbar/BottomBar.java:448-456 |
| BottomBar$6$1.lambda$onAnimationStart$1 | REACHABLE | | Called from onAnimationStart via lambda | SRC ui/views/appbar/BottomBar.java:464 |
| BottomBar$6$1.lambda$onAnimationEnd$0 | REACHABLE | | Called from onAnimationEnd via lambda | SRC ui/views/appbar/BottomBar.java:450-453 |
| BoundedFileChannelInputStream.<init> | REACHABLE | | Created by SevenZFile.readHeaders | SRC sevenz/BoundedFileChannelInputStream.java:34-40 |
| BoundedFileChannelInputStream.read | REACHABLE | | Called from SevenZFile during stream reading | SRC sevenz/BoundedFileChannelInputStream.java:42-48 |
| BoundedFileChannelInputStream.read | REACHABLE | | Overloaded: called with byte array during extraction | SRC sevenz/BoundedFileChannelInputStream.java:50-67 |
| BoundedFileChannelInputStream.read | REACHABLE | | Private helper method called from other read() methods | SRC sevenz/BoundedFileChannelInputStream.java:83-88 |
| BoundedFileChannelInputStream.close | UNREACHABLE | framework_never_calls | Close method explicitly empty; channel controlled externally | SRC sevenz/BoundedFileChannelInputStream.java:91-93 |
| Bzip2HelperTask.<init> | REACHABLE | | Created by Bzip2Decompressor.changePath | SRC asynchronous/asynctasks/compress/Bzip2HelperTask.java:38-45 |
| Bzip2HelperTask.addElements | REACHABLE | | Called from CompressedHelperTask.doInBackground | SRC asynchronous/asynctasks/compress/Bzip2HelperTask.java:48-75 |
| Bzip2Extractor.<init> | REACHABLE | | Created by CompressedHelper.getExtractorInstance | SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:40-42 |
| Bzip2Extractor.extractWithFilter | REACHABLE | | Called from Extractor base class lifecycle | SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:45-74 |
| Bzip2Extractor.extractEntry | REACHABLE | | Called from extractWithFilter for each archive entry | SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:76-97 |
| Bzip2Decompressor.<init> | REACHABLE | | Created by CompressedHelper.getCompressorInstance | SRC filesystem/compressed/showcontents/helpers/Bzip2Decompressor.java:30-32 |
| Bzip2Decompressor.changePath | REACHABLE | | Called by CompressedExplorerFragment during navigation | SRC filesystem/compressed/showcontents/helpers/Bzip2Decompressor.java:35-38 |
| CLI.<init> | UNREACHABLE | no_trigger_in_app | Command-line tool not instantiated by app; grep shows no constructor calls | SRC sevenz/CLI.java:24 |
| CLI.main | UNREACHABLE | no_trigger_in_app | Command-line entry point not called by Android app | SRC sevenz/CLI.java:114 |
| CLI.usage | UNREACHABLE | no_trigger_in_app | Called only from unused CLI.main | SRC sevenz/CLI.java:132 |
| CLI.grabMode | UNREACHABLE | no_trigger_in_app | Called only from unused CLI.main | SRC sevenz/CLI.java:136 |
| CLI$Mode.<clinit> | UNREACHABLE | no_trigger_in_app | Enum initializer, only accessed through unused CLI.main | SRC sevenz/CLI.java:29-50 |
| CLI$Mode.<init> | UNREACHABLE | no_trigger_in_app | Enum constructor, only accessed through unused CLI.main | SRC sevenz/CLI.java:57-60 |
| CLI$Mode.getMessage | UNREACHABLE | no_trigger_in_app | Called only from unused CLI enum modes | SRC sevenz/CLI.java:62-64 |
| CLI$Mode$1.<init> | UNREACHABLE | no_trigger_in_app | Enum constant for unused CLI.LIST mode | SRC sevenz/CLI.java:29-55 |
| CLI$Mode$1.getContentMethods | UNREACHABLE | no_trigger_in_app | Method of unused LIST mode | SRC sevenz/CLI.java:44-55 |
| CLI$Mode$1.takeAction | UNREACHABLE | no_trigger_in_app | Method of unused LIST mode | SRC sevenz/CLI.java:31-43 |
| CLI$Mode$2.<init> | UNREACHABLE | no_trigger_in_app | Enum constant for unused CLI.EXTRACT mode | SRC sevenz/CLI.java:56-94 |
| CLI$Mode$2.takeAction | UNREACHABLE | no_trigger_in_app | Method of unused EXTRACT mode | SRC sevenz/CLI.java:58-94 |

STATUS: DONE 21:26
