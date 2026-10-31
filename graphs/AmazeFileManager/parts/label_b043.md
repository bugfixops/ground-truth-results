STATUS: RUNNING 23:38

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| LoadFolderSpaceDataTask.<init> | REACHABLE | | Constructor called from GeneralDialogCreation.showPropertiesDialog | SRC ui/dialogs/GeneralDialogCreation.java:516 |
| LoadFolderSpaceDataTask.doInBackground | REACHABLE | | AsyncTask lifecycle method, framework calls when task executes | SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:53-64 |
| LoadFolderSpaceDataTask.onPostExecute | REACHABLE | | AsyncTask lifecycle method, framework calls after doInBackground | SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:85-93 |
| LoadFolderSpaceDataTask.onProgressUpdate | REACHABLE | | AsyncTask lifecycle method, framework calls on publishProgress | SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:68-80 |
| LoadFolderSpaceDataTask.createEntriesFromArray | REACHABLE | | Called from onProgressUpdate and doInBackground | SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:88-98 |
| LoadFolderSpaceDataTask.updateChart | REACHABLE | | Called from onProgressUpdate and onPostExecute | SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:100-118 |
| LruBitmapCache.<init> | REACHABLE | | Constructor called from AppConfig.getImageLoader (maxSize signature) via this() | SRC utils/application/AppConfig.java:223, utils/LruBitmapCache.java:22 |
| LruBitmapCache.<init> | REACHABLE | | Constructor with maxSize parameter called from no-arg constructor | SRC utils/LruBitmapCache.java:17-19 |
| LruBitmapCache.getDefaultCacheSize | REACHABLE | | Called from no-arg constructor | SRC utils/LruBitmapCache.java:22, 25-28 |
| LruBitmapCache.getBitmap | REACHABLE | | ImageLoader.ImageCache interface method, called by ImageLoader | SRC utils/LruBitmapCache.java:31-33 (INFERRED framework call from ImageLoader) |
| LruBitmapCache.putBitmap | REACHABLE | | ImageLoader.ImageCache interface method, called by ImageLoader | SRC utils/LruBitmapCache.java:36-38 (INFERRED framework call from ImageLoader) |
| LruBitmapCache.sizeOf | REACHABLE | | LruCache lifecycle method, overridden to calculate bitmap size | SRC utils/LruBitmapCache.java:40-44 (INFERRED framework call from LruCache) |
| LzmaDecompressor.<init> | REACHABLE | | Constructor called from CompressedHelper.getCompressorInstance for .tar.lzma files | SRC filesystem/compressed/CompressedHelper.java:124 |
| LzmaDecompressor.changePath | REACHABLE | | Decompressor abstract method, called from parent to navigate archive | SRC filesystem/compressed/showcontents/helpers/LzmaDecompressor.java:40-43 (INFERRED framework call from Decompressor) |
| LzmaHelperTask.<init> | REACHABLE | | Constructor called from LzmaDecompressor.changePath | SRC filesystem/compressed/showcontents/helpers/LzmaDecompressor.java:43 |
| LzmaHelperTask.addElements | REACHABLE | | CompressedHelperTask abstract method, framework calls to populate archive entries | SRC asynchronous/asynctasks/compress/LzmaHelperTask.java:52-72 (INFERRED framework call from CompressedHelperTask) |
| LzmaExtractor.<init> | REACHABLE | | Constructor called from CompressedHelper.getExtractorInstance for .tar.lzma files | SRC filesystem/compressed/CompressedHelper.java:94 |
| LzmaExtractor.extractWithFilter | REACHABLE | | Extractor abstract method, framework calls to extract archive | SRC filesystem/compressed/extractcontents/helpers/LzmaExtractor.java:48-75 (INFERRED framework call from Extractor) |
| LzmaExtractor.extractEntry | REACHABLE | | Private helper called from extractWithFilter | SRC filesystem/compressed/extractcontents/helpers/LzmaExtractor.java:77-99, called at line 74 |
| LZMADecoder.<init> | UNREACHABLE | no_trigger_in_app | Library class (Commons Compress sevenz) not called by app code | grep -rn "LZMADecoder" shows no matches in app source (INFERRED) |
| LZMADecoder.decode | UNREACHABLE | no_trigger_in_app | Library class (Commons Compress sevenz) not called by app code | grep -rn "LZMADecoder" shows no matches in app source (INFERRED) |
| LZMADecoder.encode | UNREACHABLE | no_trigger_in_app | Library class (Commons Compress sevenz) not called by app code | grep -rn "LZMADecoder" shows no matches in app source (INFERRED) |
| LZMADecoder.getDictionarySize | UNREACHABLE | no_trigger_in_app | Library class (Commons Compress sevenz) not called by app code | grep -rn "LZMADecoder" shows no matches in app source (INFERRED) |
| LZMADecoder.getOptions | UNREACHABLE | no_trigger_in_app | Library class (Commons Compress sevenz) not called by app code | grep -rn "LZMADecoder" shows no matches in app source (INFERRED) |
| LZMADecoder.getOptionsAsProperties | UNREACHABLE | no_trigger_in_app | Library class (Commons Compress sevenz) not called by app code | grep -rn "LZMADecoder" shows no matches in app source (INFERRED) |
| LZMADecoder.getOptionsFromCoder | UNREACHABLE | no_trigger_in_app | Library class (Commons Compress sevenz) not called by app code | grep -rn "LZMADecoder" shows no matches in app source (INFERRED) |
| LZMADecoder.numberOptionOrDefault | UNREACHABLE | no_trigger_in_app | Library class (Commons Compress sevenz) not called by app code | grep -rn "LZMADecoder" shows no matches in app source (INFERRED) |

STATUS: DONE 23:38
