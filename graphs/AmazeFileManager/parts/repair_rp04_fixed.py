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
