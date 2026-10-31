# ---- Helper B006 label part (2026-10-27)

# BottomBar$5 edges
e('BottomBar.showButtons', 'BottomBar$5.<init>', 'CONSTRUCTED', 'AnimatorListenerAdapter for initial path created',
  evidence='SRC ui/views/appbar/BottomBar.java:398')
e('BottomBar$5.<init>', 'BottomBar$5.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:401')
e('BottomBar$5.<init>', 'BottomBar$5.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:410')
e('BottomBar$5.onAnimationStart', 'BottomBar$5.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:404')
e('BottomBar$5.onAnimationEnd', 'BottomBar$5.lambda$onAnimationEnd$1', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:409-412')

# BottomBar$6 edges
e('BottomBar.showButtons', 'BottomBar$6.<init>', 'CONSTRUCTED', 'AnimatorListenerAdapter for different path slideout created',
  evidence='SRC ui/views/appbar/BottomBar.java:425')
e('BottomBar$6.<init>', 'BottomBar$6.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:428')
e('BottomBar$6.<init>', 'BottomBar$6.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:437')
e('BottomBar$6.onAnimationStart', 'BottomBar$6.lambda$onAnimationStart$0', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:433')
e('BottomBar$6.onAnimationEnd', 'BottomBar$6$1.<init>', 'CONSTRUCTED', 'Nested AnimatorListenerAdapter for slidein created',
  evidence='SRC ui/views/appbar/BottomBar.java:446')

# BottomBar$6$1 edges
e('BottomBar$6$1.<init>', 'BottomBar$6$1.onAnimationStart', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:459')
e('BottomBar$6$1.<init>', 'BottomBar$6$1.onAnimationEnd', 'FRAMEWORK', 'Framework animation lifecycle',
  evidence='SRC ui/views/appbar/BottomBar.java:448')
e('BottomBar$6$1.onAnimationStart', 'BottomBar$6$1.lambda$onAnimationStart$1', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:464')
e('BottomBar$6$1.onAnimationEnd', 'BottomBar$6$1.lambda$onAnimationEnd$0', 'CALL', 'Lambda from animation listener',
  evidence='SRC ui/views/appbar/BottomBar.java:450-453')

# BoundedFileChannelInputStream edges
e('SevenZFile.readHeaders', 'BoundedFileChannelInputStream.<init>', 'CALL', 'Created by SevenZFile for reading 7z archives',
  evidence='SRC sevenz/SevenZFile.java:371,429,998')
e('BoundedFileChannelInputStream.<init>', 'BoundedFileChannelInputStream.read', 'CALL', 'Called during stream reading',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:44,59')
e('BoundedFileChannelInputStream.read', 'BoundedFileChannelInputStream.read', 'CALL', 'Private helper calls',
  evidence='SRC sevenz/BoundedFileChannelInputStream.java:83-88')

# Bzip2HelperTask edges
e('Bzip2Decompressor.changePath', 'Bzip2HelperTask.<init>', 'CALL', 'Created by Bzip2Decompressor.changePath',
  evidence='SRC filesystem/compressed/showcontents/helpers/Bzip2Decompressor.java:43')
e('Bzip2HelperTask.<init>', 'Bzip2HelperTask.addElements', 'CALL', 'Called from CompressedHelperTask.doInBackground',
  evidence='SRC asynchronous/asynctasks/compress/CompressedHelperTask.java:53')

# Bzip2Extractor edges
e('CompressedHelper.getExtractorInstance', 'Bzip2Extractor.<init>', 'CALL', 'Created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:90,174')
e('Bzip2Extractor.<init>', 'Bzip2Extractor.extractWithFilter', 'CALL', 'Called from Extractor base class',
  evidence='SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:49')
e('Bzip2Extractor.extractWithFilter', 'Bzip2Extractor.extractEntry', 'CALL', 'Called from extractWithFilter',
  evidence='SRC filesystem/compressed/extractcontents/helpers/Bzip2Extractor.java:68')

# Bzip2Decompressor edges
e('CompressedHelper.getCompressorInstance', 'Bzip2Decompressor.<init>', 'CALL', 'Created for .tar.bz2/.tbz files',
  evidence='SRC filesystem/compressed/CompressedHelper.java:120,174')
e('CompressedExplorerFragment.changePath', 'Bzip2Decompressor.changePath', 'CALL', 'Fragment navigation calls changePath',
  evidence='SRC fragments/CompressedExplorerFragment.java:411')

# UNREACHABLE methods from batch_006
UNREACHABLE_B006 = {
    'BottomBar$5.onAnimationCancel': ('framework_never_calls',
        'Animation cancellation not triggered in app usage',
        'SRC ui/views/appbar/BottomBar.java:418-421',
        'SOURCE'),
    'BottomBar$6.onAnimationCancel': ('framework_never_calls',
        'Animation cancellation not triggered in app usage',
        'SRC ui/views/appbar/BottomBar.java:470-473',
        'SOURCE'),
    'BoundedFileChannelInputStream.close': ('framework_never_calls',
        'Close method explicitly empty; channel controlled externally',
        'SRC sevenz/BoundedFileChannelInputStream.java:91-93; comment states nested channel controlled externally',
        'SOURCE'),
    'CLI.<init>': ('no_trigger_in_app',
        'Command-line tool not instantiated by app',
        'SRC sevenz/CLI.java:24; grep shows no app usage',
        'SOURCE'),
    'CLI.main': ('no_trigger_in_app',
        'Command-line entry point not called by Android app',
        'SRC sevenz/CLI.java:114; main method unused in app context',
        'SOURCE'),
    'CLI.usage': ('no_trigger_in_app',
        'Called only from unused CLI.main',
        'SRC sevenz/CLI.java:132; only caller is CLI.main',
        'SOURCE'),
    'CLI.grabMode': ('no_trigger_in_app',
        'Called only from unused CLI.main',
        'SRC sevenz/CLI.java:136; only caller is CLI.main',
        'SOURCE'),
    'CLI$Mode.<clinit>': ('no_trigger_in_app',
        'Enum initializer only accessed through unused CLI.main',
        'SRC sevenz/CLI.java:29-50; enum constants never instantiated',
        'SOURCE'),
    'CLI$Mode.<init>': ('no_trigger_in_app',
        'Enum constructor only accessed through unused CLI.main',
        'SRC sevenz/CLI.java:57-60; enum not instantiated in app',
        'SOURCE'),
    'CLI$Mode.getMessage': ('no_trigger_in_app',
        'Called only from unused CLI enum modes',
        'SRC sevenz/CLI.java:62-64; only caller is unused enum',
        'SOURCE'),
    'CLI$Mode$1.<init>': ('no_trigger_in_app',
        'Enum constant for unused CLI.LIST mode',
        'SRC sevenz/CLI.java:29-55; LIST mode never used',
        'SOURCE'),
    'CLI$Mode$1.getContentMethods': ('no_trigger_in_app',
        'Method of unused LIST mode',
        'SRC sevenz/CLI.java:44-55; only called from LIST takeAction',
        'SOURCE'),
    'CLI$Mode$1.takeAction': ('no_trigger_in_app',
        'Method of unused LIST mode',
        'SRC sevenz/CLI.java:31-43; LIST never instantiated',
        'SOURCE'),
    'CLI$Mode$2.<init>': ('no_trigger_in_app',
        'Enum constant for unused CLI.EXTRACT mode',
        'SRC sevenz/CLI.java:56-94; EXTRACT mode never used',
        'SOURCE'),
    'CLI$Mode$2.takeAction': ('no_trigger_in_app',
        'Method of unused EXTRACT mode',
        'SRC sevenz/CLI.java:58-94; only called from EXTRACT enum',
        'SOURCE'),
}
