STATUS: START 20:23

| Method | Label | Evidence Lines |
|--------|-------|----------------|
| SevenZArchiveEntry.getAccessDate | UNREACHABLE | SRC SevenZArchiveEntry.java:275-280; grep -rn "\.getAccessDate()" app/src/main/java shows no app callers |
| SevenZArchiveEntry.getCompressedCrc | UNREACHABLE | SRC SevenZArchiveEntry.java:371-373; grep -rn "\.getCompressedCrc" app/src/main/java shows no app callers |
| SevenZArchiveEntry.getCompressedCrcValue | UNREACHABLE | SRC SevenZArchiveEntry.java:387-389; grep -rn "\.getCompressedCrcValue" app/src/main/java shows no app callers |
| SevenZArchiveEntry.getCompressedSize | UNREACHABLE | SRC SevenZArchiveEntry.java:410-412; grep -rn "\.getCompressedSize" app/src/main/java shows no app callers |
| SevenZArchiveEntry.getCrc | UNREACHABLE | SRC SevenZArchiveEntry.java:339-342; grep -rn "\.getCrc" app/src/main/java shows no app callers |
| SevenZArchiveEntry.getCreationDate | UNREACHABLE | SRC SevenZArchiveEntry.java:153-159; grep -rn "\.getCreationDate" app/src/main/java shows no app callers |
| SevenZArchiveEntry.getWindowsAttributes | UNREACHABLE | SRC SevenZArchiveEntry.java:313-315; grep -rn "\.getWindowsAttributes" app/src/main/java shows no app callers |
| SevenZArchiveEntry.isAntiItem | UNREACHABLE | SRC SevenZArchiveEntry.java:121-123; grep -rn "\.isAntiItem" app/src/main/java shows no app callers |
| SevenZArchiveEntry.javaTimeToNtfsTime | UNREACHABLE | SRC SevenZArchiveEntry.java:486-493; grep -rn "javaTimeToNtfsTime" app/src/main/java shows no app callers |
| SevenZArchiveEntry.setAccessDate(Date) | UNREACHABLE | SRC SevenZArchiveEntry.java:296-301; grep -rn "\.setAccessDate" app/src/main/java shows no app callers |
| SevenZArchiveEntry.setCompressedCrc | UNREACHABLE | SRC SevenZArchiveEntry.java:379-382; grep -rn "\.setCompressedCrc" app/src/main/java shows no app callers |
| SevenZArchiveEntry.setCompressedCrcValue | UNREACHABLE | SRC SevenZArchiveEntry.java:395-398; grep -rn "\.setCompressedCrcValue" app/src/main/java shows no app callers |
| SevenZArchiveEntry.setCompressedSize | UNREACHABLE | SRC SevenZArchiveEntry.java:420-423; grep -rn "\.setCompressedSize" app/src/main/java shows no app callers |
| SevenZArchiveEntry.setCrc | UNREACHABLE | SRC SevenZArchiveEntry.java:350-353; grep -rn "\.setCrc" app/src/main/java shows no app callers |
| SevenZArchiveEntry.setCreationDate(Date) | UNREACHABLE | SRC SevenZArchiveEntry.java:174-179; grep -rn "\.setCreationDate" app/src/main/java shows no app callers |
| SevenZArchiveEntry.setLastModifiedDate(Date) | UNREACHABLE | SRC SevenZArchiveEntry.java:232-237; grep -rn "\.setLastModifiedDate" app/src/main/java shows no app callers |
| SearchAsyncTask.<init> | REACHABLE | Already in graph_def.py:1295 |
| SearchAsyncTask.bashRegexToJava | REACHABLE | Already in graph_def.py:1307 |
| SearchAsyncTask.doInBackground | REACHABLE | Already in graph_def.py:1298 |
| SearchAsyncTask.lambda$search$0 | REACHABLE | SRC SearchAsyncTask.java:108 directory.forEachChildrenFile(activity.get(), mRootMode, file -> { |
| SearchAsyncTask.lambda$search$1 | REACHABLE | SRC SearchAsyncTask.java:131 search(file, fileName -> fileName.toLowerCase().contains(query.toLowerCase())) |
| SearchAsyncTask.lambda$searchRegExFind$2 | REACHABLE | SRC SearchAsyncTask.java:142 search(file, fileName -> pattern.matcher(fileName).find()) |
| SearchAsyncTask.lambda$searchRegExMatch$3 | REACHABLE | SRC SearchAsyncTask.java:152 search(file, fileName -> pattern.matcher(fileName).matches()) |
| SearchAsyncTask.onCancelled | REACHABLE | Already in graph_def.py:1322 |
| SearchAsyncTask.onPostExecute | REACHABLE | Already in graph_def.py:1319 |
| SearchAsyncTask.onPreExecute | REACHABLE | Already in graph_def.py:1325 |
| SearchAsyncTask.onProgressUpdate | REACHABLE | Already in graph_def.py:1316 |
| SearchAsyncTask.search(HybridFile,SearchFilter) | REACHABLE | Already in graph_def.py:1304 |
| SearchAsyncTask.search(HybridFile,String) | REACHABLE | Already in graph_def.py:1301 |
| SearchAsyncTask.searchRegExFind | REACHABLE | Already in graph_def.py:1310 |
| SearchAsyncTask.searchRegExMatch | REACHABLE | Already in graph_def.py:1313 |

STATUS: DONE 20:25
