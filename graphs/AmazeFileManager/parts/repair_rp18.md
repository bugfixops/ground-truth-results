# Repair batch 18: 39 methods

STATUS: START 21:23

| Method | Label | Evidence Lines |
|--------|-------|----------------|
| SevenZFile$2.<init> | REACHABLE | SRC commons_compress_7z/.../SevenZFile.java:1116-1125; returned by getStatisticsForCurrentEntry |
| SevenZFile$2.getCompressedCount | REACHABLE | SRC commons_compress_7z/.../SevenZFile.java:1119-1121; framework callback |
| SevenZFile$2.getUncompressedCount | REACHABLE | SRC commons_compress_7z/.../SevenZFile.java:1123-1125; framework callback |
| SevenZMethodConfiguration.<init>(SevenZMethod) | REACHABLE | SRC commons_compress_7z/.../SevenZMethodConfiguration.java:47-49; used in 7z compression |
| SevenZMethodConfiguration.getMethod | REACHABLE | SRC commons_compress_7z/.../SevenZMethodConfiguration.java:71-73; called by 7z output |
| SevenZMethodConfiguration.getOptions | REACHABLE | SRC commons_compress_7z/.../SevenZMethodConfiguration.java:79-81; called by 7z output |
| CustomSshJConfig.<init> | REACHABLE | Already has route in graph_def.py:2744,2748 |
| CustomSshJConfig.initRandomFactory | REACHABLE | SRC app/.../CustomSshJConfig.java:57-60; parent constructor calls override |
| CustomSshJConfig.initSignatureFactories | REACHABLE | SRC app/.../CustomSshJConfig.java:53-55; parent constructor calls override |
| SshConnectionPool$AsyncRemoveConnection.<init> | REACHABLE | SRC app/.../SshConnectionPool.java:98; new AsyncRemoveConnection(url, callback) |
| SshConnectionPool$AsyncRemoveConnection.doInBackground | REACHABLE | SRC app/.../SshConnectionPool.java:294-302; framework AsyncTask callback |
| SshConnectionPool$AsyncRemoveConnection.onPostExecute | REACHABLE | SRC app/.../SshConnectionPool.java:304-307; framework AsyncTask callback |
| Statvfs$Response.getFileSystemId | REACHABLE | SRC app/.../Statvfs.java:192-195; called by SSH operations |
| Statvfs$Response.getRawFileSystemId | REACHABLE | SRC app/.../Statvfs.java:202-205; called by SSH operations |
| Statvfs$Response.toString | REACHABLE | SRC app/.../Statvfs.java:217-224; for debugging/logging |
| MainFragment$4$1.<init> | REACHABLE | SRC app/.../MainFragment.java:798; anonymous MediaScannerConnectionClient |
| MainFragment$4$1.onMediaScannerConnected | REACHABLE | SRC app/.../MainFragment.java:800-803; framework callback |
| MainFragment$4$1.onScanCompleted | REACHABLE | SRC app/.../MainFragment.java:805-809; framework callback |
| MainFragment$6.<init> | REACHABLE | SRC app/.../MainFragment.java:1640; anonymous AsyncTask for sorting |
| MainFragment$6.doInBackground | REACHABLE | SRC app/.../MainFragment.java:1642-1645; framework AsyncTask callback |
| MainFragment$6.onPostExecute | REACHABLE | SRC app/.../MainFragment.java:1647-1651; framework AsyncTask callback |
| ProcessViewerFragment$CustomServiceConnection.<init> | REACHABLE | SRC app/.../ProcessViewerFragment.java:127-131; created in onCreateView |
| ProcessViewerFragment$CustomServiceConnection.onServiceConnected | REACHABLE | SRC app/.../ProcessViewerFragment.java:404-432; framework ServiceConnection callback |
| ProcessViewerFragment$CustomServiceConnection.onServiceDisconnected | REACHABLE | SRC app/.../ProcessViewerFragment.java:435; framework ServiceConnection callback |
| PropertiesSheet.<init> | REACHABLE | SRC app/.../PropertiesSheet.java:29; fragment instantiation |
| PropertiesSheet.generate | REACHABLE | SRC app/.../PropertiesSheet.java:112-116; called during initialization |
| PropertiesSheet.setupDialog | REACHABLE | SRC app/.../PropertiesSheet.java:49-108; framework lifecycle method |
| PropertiesSheet$2.<init> | REACHABLE | SRC app/.../PropertiesSheet.java:117; field mCallback initializer |
| PropertiesSheet$2.onSlide | REACHABLE | SRC app/.../PropertiesSheet.java:126-128; framework BottomSheetCallback |
| PropertiesSheet$2.onStateChanged | REACHABLE | SRC app/.../PropertiesSheet.java:119-123; framework BottomSheetCallback |
| SearchWorkerFragment.onAttach | REACHABLE | SRC app/.../SearchWorkerFragment.java:40-44; framework lifecycle method |
| SearchWorkerFragment.onCreate | REACHABLE | SRC app/.../SearchWorkerFragment.java:46-62; framework lifecycle method |
| SearchWorkerFragment.onDetach | REACHABLE | SRC app/.../SearchWorkerFragment.java:64-68; framework lifecycle method |
| TabFragment$ScreenSlidePagerAdapter.getCount | REACHABLE | SRC app/.../TabFragment.java:332-335; framework PagerAdapter method |
| TabFragment$ScreenSlidePagerAdapter.getItem | REACHABLE | SRC app/.../TabFragment.java:342-346; framework PagerAdapter method |
| TabFragment$ScreenSlidePagerAdapter.getItemPosition | REACHABLE | SRC app/.../TabFragment.java:321-327; framework PagerAdapter method |
| UserColorPreferences.<init>(Parcel) | REACHABLE | SRC app/.../UserColorPreferences.java:20-25; framework Parcelable protocol |
| UserColorPreferences.describeContents | REACHABLE | SRC app/.../UserColorPreferences.java:34-36; framework Parcelable protocol |
| UserColorPreferences.writeToParcel | REACHABLE | SRC app/.../UserColorPreferences.java:27-32; framework Parcelable protocol |

STATUS: DONE 21:26

