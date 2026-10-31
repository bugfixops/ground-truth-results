# ---- Helper batch_004 label part (2026-10-27)

# ArchivePasswordCache methods - singleton getInstance is entry point via SevenZipHelperTask
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.getInstance', 'ENTRY_POINT', 'public static method called from AsyncTask',
  evidence='SRC SevenZipHelperTask.java:68-69')
e('ArchivePasswordCache.getInstance', 'ArchivePasswordCacheHolder.<clinit>', 'FRAMEWORK', 'static initializer for holder class',
  evidence='SRC ArchivePasswordCache.java:65-67')
e('ArchivePasswordCacheHolder.<clinit>', 'ArchivePasswordCache.<init>', 'FRAMEWORK', 'constructor called from static initializer',
  evidence='SRC ArchivePasswordCache.java:66')

# ArchivePasswordCache methods accessed via getInstance result
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.containsKey', 'ENTRY_POINT', 'called on result from getInstance',
  evidence='SRC SevenZipHelperTask.java:68')
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.get', 'ENTRY_POINT', 'called on result from getInstance',
  evidence='SRC SevenZipHelperTask.java:69')
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.remove', 'ENTRY_POINT', 'called on result from getInstance',
  evidence='SRC SevenZipHelperTask.java:103')
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.put', 'ENTRY_POINT', 'called on result from getInstance',
  evidence='SRC SevenZipHelperTask.java:111')

# AsyncTaskResult constructors
e('CompressedHelperTask.doInBackground', 'AsyncTaskResult.<init>', 'ENTRY_POINT', 'constructor called with result',
  evidence='SRC CompressedHelperTask.java:58,60')
e('GetSshHostFingerprintTask.doInBackground', 'AsyncTaskResult.<init>', 'ENTRY_POINT', 'constructor called with result/exception',
  evidence='SRC GetSshHostFingerprintTask.java:87,97,101')

# BookSorter 
e('SftpConnectDialog.onItemClicked', 'BookSorter.<init>', 'ENTRY_POINT', 'new BookSorter() in Collections.sort call',
  evidence='SRC SftpConnectDialog.java:382')
e('Drawer.updateServers', 'BookSorter.<init>', 'ENTRY_POINT', 'new BookSorter() in Collections.sort call',
  evidence='SRC Drawer.java:296')
e('BookSorter.<init>', 'BookSorter.compare', 'FRAMEWORK', 'Comparator.compare called by Collections.sort',
  evidence='SRC BookSorter.java:1-19')

# BindPair is a library class (Apache commons_compress_7z) - check for app calls
# BindPair appears only in 7z decompression internally, likely not called from app code directly

UNREACHABLE_B004 = {
    # ArchivePasswordCache Map interface delegation methods - reachable through Map usage
    # All are already covered above in e() edges
    
    # BindPair - library class used internally by 7z decompression
    # Need to verify if it has any app call sites
    'com/amaze/filemanager/filesystem/compressed/sevenz/BindPair.<init>': 
        ('branch_never_taken', 'BindPair is a private library class in commons_compress_7z module; grep shows no app instantiation sites', 
         'SRC BindPair.java:20-26', 'INFERRED'),
    'com/amaze/filemanager/filesystem/compressed/sevenz/BindPair.toString': 
        ('no_trigger_in_app', 'library utility method, not called from app code',
         'SRC BindPair.java:28-30', 'INFERRED'),
         
    # ArchivePasswordCache unreachable Map methods (not called in reachable code)
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.clear': 
        ('no_trigger_in_app', 'Map interface method, no reachable code calls this',
         'SRC ArchivePasswordCache.java:119-120', 'SOURCE'),
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.containsValue': 
        ('no_trigger_in_app', 'Map interface method, no reachable code calls this',
         'SRC ArchivePasswordCache.java:85-87', 'SOURCE'),
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.entrySet': 
        ('no_trigger_in_app', 'Map interface method, not called from reachable code',
         'SRC ArchivePasswordCache.java:92-94', 'SOURCE'),
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.equals': 
        ('no_trigger_in_app', 'Map interface method, not called from reachable code',
         'SRC ArchivePasswordCache.java:138-140', 'SOURCE'),
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.hashCode': 
        ('no_trigger_in_app', 'Map interface method, not called from reachable code',
         'SRC ArchivePasswordCache.java:135-137', 'SOURCE'),
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.isEmpty': 
        ('no_trigger_in_app', 'Map interface method, not called from reachable code',
         'SRC ArchivePasswordCache.java:82-84', 'SOURCE'),
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.keySet': 
        ('no_trigger_in_app', 'Map interface method, not called from reachable code',
         'SRC ArchivePasswordCache.java:129-131', 'SOURCE'),
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.putAll': 
        ('no_trigger_in_app', 'Map interface method, not called from reachable code',
         'SRC ArchivePasswordCache.java:117-118', 'SOURCE'),
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.size': 
        ('no_trigger_in_app', 'Map interface method, not called from reachable code',
         'SRC ArchivePasswordCache.java:80-81', 'SOURCE'),
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.toString': 
        ('no_trigger_in_app', 'Map interface method, not called from reachable code',
         'SRC ArchivePasswordCache.java:133-134', 'SOURCE'),
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache.values': 
        ('no_trigger_in_app', 'Map interface method, not called from reachable code',
         'SRC ArchivePasswordCache.java:127-128', 'SOURCE'),
         
    # ArchivePasswordCacheHolder private constructor
    'com/amaze/filemanager/filesystem/compressed/ArchivePasswordCache$ArchivePasswordCacheHolder.<init>': 
        ('branch_never_taken', 'private constructor of holder class, never called',
         'SRC ArchivePasswordCache.java:62-63', 'SOURCE'),
}
