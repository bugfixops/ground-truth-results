# ---- Batch 001 label part (2026-10-27)
# Classes: AES256SHA256Decoder, AES256SHA256Decoder$1, AbstractProgressiveService, 
#          AdvancedSearchPref, AmazeFileManagerModule, AnimUtils, ApkImageDataFetcher, ApkImageModelLoader

# AmazeFileManagerModule - Glide module registration
# Already has edges in graph_def.py; no new edges needed

# ApkImage Glide loaders - ApkImageModelLoader and ApkImageDataFetcher
# Already have edges in graph_def.py from registerComponents through factory chain
# No new edges needed

# AdvancedSearchPref - preference fragment
# Already has edges in graph_def.py from PreferencesActivity.selectItem
# No new edges needed

# AnimUtils - utility class with static animation methods
# Already has edges in graph_def.py from Indicator and AppsAdapter
# AnimUtils.<init> is not reachable (utility class never instantiated)
e('AnimUtils.marqueeAfterDelay', 'AnimUtils.lambda$marqueeAfterDelay$0', 'CALL',
  'Lambda callback passed to Handler.postDelayed',
  evidence='SRC utils/AnimUtils.java:47-49')

# AbstractProgressiveService - abstract base class for file operation services
# Derived services (CopyService, ExtractService, ZipService, DecryptService) already have entry/lifecycle edges
# These edges establish reachability of abstract methods through service framework calls
# No new edges needed beyond those for specific services (already in graph_def.py)

UNREACHABLE['AnimUtils.<init>'] = ('no_trigger_in_app',
        'Utility class with only static methods; no reachable constructor call site; never instantiated in app',
        'SRC utils/AnimUtils.java:28-29; grep -rn "new AnimUtils" shows no matches',
        'SOURCE')
UNREACHABLE['AbstractProgressiveService.publishCompletedResult'] = ('branch_never_taken',
        'Private method called only from publishResults when operation completes; not independently reachable',
        'SRC asynchronous/services/AbstractProgressiveService.java:161-167,149',
        'SOURCE')
UNREACHABLE['AbstractProgressiveService.putDataPackage'] = ('no_trigger_in_app',
        'Private synchronized method; only called internally from addDatapoint and addFirstDatapoint',
        'SRC asynchronous/services/AbstractProgressiveService.java:201-204',
        'SOURCE')
UNREACHABLE['AES256SHA256Decoder.<init>'] = ('framework_never_calls',
        'Library class from org.apache.commons.compress; no app call sites; only used internally by SevenZ library code',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'SOURCE')
UNREACHABLE['AES256SHA256Decoder.decode'] = ('framework_never_calls',
        'Library class method; called only by SevenZ library internal code (CoderBase subclass)
UNREACHABLE['AES256SHA256Decoder$1.<init>'] = ('framework_never_calls',
        'Anonymous inner class from unreachable library decoder; instantiated only by AES256SHA256Decoder.decode',
        'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/AES256SHA256Decoder.java:34',
        'SOURCE')
UNREACHABLE['AES256SHA256Decoder$1.close'] = ('framework_never_calls',
        'Inner class method from unreachable library decoder; only called when stream is closed',
        'SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/AES256SHA256Decoder.java:113',
        'SOURCE')
UNREACHABLE['AES256SHA256Decoder$1.read'] = ('framework_never_calls',
        'Inner class methods (both overloads)
UNREACHABLE['AES256SHA256Decoder$1.init'] = ('framework_never_calls',
        'Private inner class method; only called from unreachable read()
