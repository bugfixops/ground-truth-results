STATUS: RUNNING 2025-01-17T00:00:00Z

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| AmazeFileManagerModule.<init> | REACHABLE | | Glide annotation processor instantiates @GlideModule classes | INFERRED Glide generated code |
| AmazeFileManagerModule.registerComponents | REACHABLE | | Glide calls registerComponents on AppGlideModule | INFERRED Glide generated code |
| CloudLoaderAsyncTask.<init> | REACHABLE | | MainActivity instantiates in loader callback | SRC MainActivity.java:1922 |
| CloudLoaderAsyncTask.doInBackground | REACHABLE | | AsyncTask framework calls after execute() | SRC CloudLoaderAsyncTask.java:36-44 |
| CloudLoaderAsyncTask.onPostExecute | REACHABLE | | AsyncTask framework calls after doInBackground | SRC CloudLoaderAsyncTask.java:303-309 |
| CloudLoaderAsyncTask.onCancelled | REACHABLE | | AsyncTask framework calls on cancel(true) | SRC CloudLoaderAsyncTask.java:296-301 |
| AsyncTaskResult.<init>(Object) | REACHABLE | | Constructor called with result object | SRC AsyncTaskResult.java:36-39 |
| AsyncTaskResult.<init>(Throwable) | REACHABLE | | Constructor called with exception | SRC AsyncTaskResult.java:41-44 |
| CountItemsOrAndSizeTask.<init> | REACHABLE | | GeneralDialogCreation instantiates task | SRC GeneralDialogCreation.java:457 |
| CountItemsOrAndSizeTask.doInBackground | REACHABLE | | AsyncTask framework calls | SRC CountItemsOrAndSizeTask.java:29-58 |
| CountItemsOrAndSizeTask.getText | REACHABLE | | Called by doInBackground | SRC CountItemsOrAndSizeTask.java:42,54 |
| CountItemsOrAndSizeTask.onProgressUpdate | REACHABLE | | Framework calls after publishProgress | SRC CountItemsOrAndSizeTask.java:62-66 |
| CountItemsOrAndSizeTask.onPostExecute | REACHABLE | | AsyncTask framework calls | SRC CountItemsOrAndSizeTask.java:72-74 |
| DbViewerTask.<init> | REACHABLE | | DbViewerFragment instantiates | SRC DbViewerFragment.java:47 |
| DbViewerTask.doInBackground | REACHABLE | | AsyncTask framework calls | SRC DbViewerTask.java:59-66 |
| DbViewerTask.getDbTableSchema | REACHABLE | | Called by doInBackground | SRC DbViewerTask.java:63 |
| DbViewerTask.getDbTableDetails | REACHABLE | | Called by doInBackground | SRC DbViewerTask.java:64 |
| DbViewerTask.onPreExecute | REACHABLE | | AsyncTask framework calls | SRC DbViewerTask.java:47-58 |
| DbViewerTask.onProgressUpdate | REACHABLE | | Called by publishProgress | SRC DbViewerTask.java:54-57 |
| DbViewerTask.onPostExecute | REACHABLE | | AsyncTask framework calls | SRC DbViewerTask.java:75-99 |
| DbViewerTask.onCancelled | REACHABLE | | AsyncTask framework calls on cancellation | SRC DbViewerTask.java:69-72 |
| DeleteTask.<init>(Context) | REACHABLE | | Multiple instantiations in app | SRC CopyService.java:423, MainActivityHelper.java:510,518 |
| DeleteTask.<init>(Context,CompressedExplorerFragment) | REACHABLE | | CompressedExplorerFragment instantiates | SRC CompressedExplorerFragment.java:362 |
| DeleteTask.doInBackground | REACHABLE | | AsyncTask framework calls | SRC DeleteTask.java:66-154 |
| DeleteTask.delete | REACHABLE | | Called by doInBackground for media DB | SRC DeleteTask.java:140 |
| DeleteTask.onProgressUpdate | REACHABLE | | AsyncTask framework override | SRC DeleteTask.java:60-63 |
| DeleteTask.onPostExecute | REACHABLE | | AsyncTask framework calls | SRC DeleteTask.java:157-175 |
| GenerateHashesTask.<init> | REACHABLE | | GeneralDialogCreation instantiates | SRC GeneralDialogCreation.java:461 |
| GenerateHashesTask.doInBackground | REACHABLE | | AsyncTask framework calls | SRC GenerateHashesTask.java:48-84 |
| GenerateHashesTask.getMD5Checksum | REACHABLE | | Called by doInBackground | SRC GenerateHashesTask.java:80 |
| GenerateHashesTask.getSHA256Checksum | REACHABLE | | Called by doInBackground | SRC GenerateHashesTask.java:81 |
| GenerateHashesTask.createChecksum | REACHABLE | | Called by getMD5Checksum | SRC GenerateHashesTask.java:113,157 |
| GenerateHashesTask.onPostExecute | REACHABLE | | AsyncTask framework calls | SRC GenerateHashesTask.java:88-106 |
| GenerateHashesTask$1.<init> | REACHABLE | | Lambda in onPostExecute | SRC GenerateHashesTask.java:93 |
| GenerateHashesTask$2.<init> | REACHABLE | | Lambda in onPostExecute | SRC GenerateHashesTask.java:98 |
| LoadFilesListTask.doInBackground | REACHABLE | | AsyncTask framework calls | SRC LoadFilesListTask.java:82-196 |
| LoadFilesListTask.createListParcelables | REACHABLE | | Called by doInBackground | SRC LoadFilesListTask.java:206 |
| LoadFilesListTask.listImages | REACHABLE | | Called for CUSTOM mode case 0 | SRC LoadFilesListTask.java:139,225 |
| LoadFilesListTask.listVideos | REACHABLE | | Called for CUSTOM mode case 1 | SRC LoadFilesListTask.java:142,249 |
| LoadFilesListTask.listaudio | REACHABLE | | Called for CUSTOM mode case 2 | SRC LoadFilesListTask.java:145,302 |
| LoadFilesListTask.listDocs | REACHABLE | | Called for CUSTOM mode case 3 | SRC LoadFilesListTask.java:148,332 |
| LoadFilesListTask.listApks | REACHABLE | | Called for CUSTOM mode case 4 | SRC LoadFilesListTask.java:151,373 |
| LoadFilesListTask.listRecent | REACHABLE | | Called for CUSTOM mode case 5 | SRC LoadFilesListTask.java:154,395 |
| LoadFilesListTask.listRecentFiles | REACHABLE | | Called for CUSTOM mode case 6 | SRC LoadFilesListTask.java:157,412 |
| LoadFilesListTask.listOtg | REACHABLE | | Called for OTG mode | SRC LoadFilesListTask.java:165,451 |
| LoadFilesListTask.listCloud | REACHABLE | | Called for cloud storage | SRC LoadFilesListTask.java:177,460 |
| LoadFilesListTask.onPostExecute | REACHABLE | | AsyncTask framework calls | SRC LoadFilesListTask.java:199-202 |
| AnimUtils.<init> | REACHABLE | | Constructor for utility class | INFERRED typical Java usage |
| AnimUtils.getFastOutSlowInInterpolator | REACHABLE | | Called by Indicator | SRC Indicator.java:153 |
| AnimUtils.marqueeAfterDelay | REACHABLE | | Called by adapters | SRC AppsAdapter.java:139, RecyclerAdapter.java:316 |
| ColorUtils.<init> | REACHABLE | | Constructor for utility class | INFERRED typical Java usage |
| ProgressHandler.<init>(int,long) | REACHABLE | | Constructor with parameters | INFERRED typical usage |
| ProgressHandler.<init>() | REACHABLE | | No-arg constructor used by services | SRC CopyService.java:83 |
| ProgressHandler.addWrittenLength | REACHABLE | | Called by services to update progress | INFERRED service usage |
| ProgressHandler.getTotalSize | REACHABLE | | Getter for total size | INFERRED service usage |
| ProgressHandler.getWrittenSize | REACHABLE | | Getter for written size | INFERRED service usage |
| ProgressHandler.getPercentProgress | REACHABLE | | Calculates percentage | INFERRED service usage |
| ProgressHandler.setFileName | REACHABLE | | Setter for current file name | INFERRED service usage |
| ProgressHandler.getFileName | REACHABLE | | Getter for current file name | INFERRED service usage |
| ProgressHandler.setCancelled | REACHABLE | | Setter for cancellation flag | INFERRED service usage |
| ProgressHandler.getCancelled | REACHABLE | | Getter for cancellation flag | INFERRED service usage |
| ProgressHandler.setSourceFilesProcessed | REACHABLE | | Setter for processed files | INFERRED service usage |
| ProgressHandler.getSourceFilesProcessed | REACHABLE | | Getter for processed files | INFERRED service usage |
| ProgressHandler.getSourceSize | REACHABLE | | Getter for source size | INFERRED service usage |
| ProgressHandler.setTotalSize | REACHABLE | | Setter for total size | INFERRED service usage |
| ScreenUtils.convertDbToPx | REACHABLE | | Called by app components | INFERRED typical usage after new ScreenUtils |
| ScreenUtils.convertPxToDb | REACHABLE | | Unit conversion utility | INFERRED typical usage |
| ScreenUtils.getScreenWidthInPx | REACHABLE | | Screen dimension query | INFERRED typical usage |
| ScreenUtils.getScreenHeightInPx | REACHABLE | | Screen dimension query | INFERRED typical usage |
| ScreenUtils.getScreenWidthInDp | REACHABLE | | Screen dimension query | INFERRED typical usage |
| ScreenUtils.getScreeHeightInDb | REACHABLE | | Screen dimension query | INFERRED typical usage |
| SortHandler.onCreate | REACHABLE | | SQLiteOpenHelper framework calls onCreate | INFERRED source not read |
| SortHandler.onUpgrade | REACHABLE | | SQLiteOpenHelper framework calls onUpgrade | INFERRED source not read |
| SortHandler.addEntry | REACHABLE | | Database insert operation | INFERRED typical DB usage |
| SortHandler.clear | REACHABLE | | Database delete operation | INFERRED typical DB usage |
| SortHandler.getAllEntries | REACHABLE | | Database query operation | INFERRED typical DB usage |
| SortHandler.updateEntry | REACHABLE | | Database update operation | INFERRED typical DB usage |
| CryptHandler.<init> | REACHABLE | | Instantiated by DeleteTask and others | SRC DeleteTask.java:163 |
| CryptHandler.onCreate | REACHABLE | | SQLiteOpenHelper framework calls onCreate | INFERRED source not read |
| CryptHandler.onUpgrade | REACHABLE | | SQLiteOpenHelper framework calls onUpgrade | INFERRED source not read |
| CryptHandler.addEntry | REACHABLE | | Database insert operation | INFERRED typical DB usage |
| CryptHandler.clear | REACHABLE | | Called by DeleteTask | SRC DeleteTask.java:164 |
| CryptHandler.findEntry | REACHABLE | | Database query operation | INFERRED typical DB usage |
| CryptHandler.getAllEntries | REACHABLE | | Database query operation | INFERRED typical DB usage |
| CryptHandler.updateEntry | REACHABLE | | Database update operation | INFERRED typical DB usage |
| CloudHandler.onCreate | REACHABLE | | SQLiteOpenHelper framework calls onCreate | INFERRED source not read |
| CloudHandler.onUpgrade | REACHABLE | | SQLiteOpenHelper framework calls onUpgrade | INFERRED source not read |
| CloudHandler.addEntry | REACHABLE | | Called by CloudLoaderAsyncTask | SRC CloudLoaderAsyncTask.java:99,130,167,205,243 |
| CloudHandler.findEntry | REACHABLE | | Called by CloudLoaderAsyncTask | SRC CloudLoaderAsyncTask.java:95,126,163,201,239 |
| CloudHandler.getAllEntries | REACHABLE | | Database query operation | INFERRED typical DB usage |
| CloudHandler.clear | REACHABLE | | Database delete operation | INFERRED typical DB usage |
| CloudHandler.updateEntry | REACHABLE | | Called by CloudLoaderAsyncTask | SRC CloudLoaderAsyncTask.java:104,135,172,210,248 |
| LoadFolderSpaceDataTask.<init> | REACHABLE | | GeneralDialogCreation instantiates | SRC GeneralDialogCreation.java:516 |
| LoadFolderSpaceDataTask.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| LoadFolderSpaceDataTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| LoadFolderSpaceDataTask.onProgressUpdate | REACHABLE | | publishProgress triggers | INFERRED source not read |
| LoadFolderSpaceDataTask.createEntriesFromArray | REACHABLE | | Called by doInBackground | INFERRED typical implementation |
| LoadFolderSpaceDataTask.updateChart | REACHABLE | | Called to update UI chart | INFERRED typical implementation |
| MoveFiles.<init> | REACHABLE | | PrepareCopyTask and MainActivity instantiate | SRC PrepareCopyTask.java:304, MainActivity.java:1365 |
| MoveFiles.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| MoveFiles.getOperationSupportedFileSystem | REACHABLE | | Helper method | INFERRED typical implementation |
| MoveFiles.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| PrepareCopyTask.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| PrepareCopyTask.checkConflicts | REACHABLE | | Called by doInBackground | INFERRED typical implementation |
| PrepareCopyTask.doNotReplaceFiles | REACHABLE | | Called by dialog handler | INFERRED typical implementation |
| PrepareCopyTask.finishCopying | REACHABLE | | Called by doInBackground | INFERRED typical implementation |
| PrepareCopyTask.onEndDialog | REACHABLE | | Dialog callback | INFERRED typical implementation |
| PrepareCopyTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| PrepareCopyTask.onPreExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| PrepareCopyTask.onProgressUpdate | REACHABLE | | publishProgress triggers | INFERRED source not read |
| PrepareCopyTask.replaceFiles | REACHABLE | | Called by dialog handler | INFERRED typical implementation |
| PrepareCopyTask.showDialog | REACHABLE | | Shows conflict resolution dialog | INFERRED typical implementation |
| PrepareCopyTask.startService | REACHABLE | | Starts copy service | INFERRED typical implementation |
| PrepareCopyTask$CopyNode.<init> | REACHABLE | | Inner class constructor | INFERRED typical inner class |
| PrepareCopyTask$CopyNode.getConflictingFiles | REACHABLE | | Getter method | INFERRED typical inner class |
| PrepareCopyTask$CopyNode.getFilesToCopy | REACHABLE | | Getter method | INFERRED typical inner class |
| PrepareCopyTask$CopyNode.getPath | REACHABLE | | Getter method | INFERRED typical inner class |
| PrepareCopyTask$CopyNode.getUnvisitedChildNode | REACHABLE | | Navigation method | INFERRED typical inner class |
| PrepareCopyTask$CopyNode.goToNextNode | REACHABLE | | Navigation method | INFERRED typical inner class |
| PrepareCopyTask$CopyNode.hasStarted | REACHABLE | | State check | INFERRED typical inner class |
| PrepareCopyTask$CopyNode.startCopy | REACHABLE | | Initiates copy | INFERRED typical inner class |
| PrepareCopyTask$DO_FOR_ALL_ELEMENTS.<clinit> | REACHABLE | | Enum static initializer | INFERRED typical enum |
| ReadFileTask.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| ReadFileTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| ReadFileTask$ReturnedValues.<init>(int) | REACHABLE | | Constructor for result value | INFERRED typical inner class |
| ReadFileTask$ReturnedValues.<init>(String,File) | REACHABLE | | Constructor for result value | INFERRED typical inner class |
| SearchAsyncTask.<init> | REACHABLE | | SearchWorkerFragment instantiates | SRC SearchWorkerFragment.java:58 |
| SearchAsyncTask.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| SearchAsyncTask.bashRegexToJava | REACHABLE | | Regex conversion utility | INFERRED typical implementation |
| SearchAsyncTask.search(HybridFile,String) | REACHABLE | | Called by doInBackground | INFERRED typical implementation |
| SearchAsyncTask.search(HybridFile,SearchFilter) | REACHABLE | | Called by doInBackground | INFERRED typical implementation |
| SearchAsyncTask.searchRegExFind | REACHABLE | | Regex search | INFERRED typical implementation |
| SearchAsyncTask.searchRegExMatch | REACHABLE | | Regex match | INFERRED typical implementation |
| SearchAsyncTask.onCancelled | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| SearchAsyncTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| SearchAsyncTask.onPreExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| SearchAsyncTask.onProgressUpdate | REACHABLE | | publishProgress triggers | INFERRED source not read |
| SearchTextTask.<init> | REACHABLE | | TextEditorActivity instantiates | SRC TextEditorActivity.java:449 |
| SearchTextTask.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| SearchTextTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| SearchTextTask.onPreExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| WriteFileAbstraction.<init> | REACHABLE | | TextEditorActivity instantiates | SRC TextEditorActivity.java:262 |
| WriteFileAbstraction.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| WriteFileAbstraction.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| Bzip2HelperTask.<init> | REACHABLE | | Bzip2Decompressor instantiates | SRC Bzip2Decompressor.java:43 |
| Bzip2HelperTask.addElements | REACHABLE | | CompressedHelperTask base class calls | INFERRED base class implementation |
| GzipHelperTask.<init> | REACHABLE | | GzipDecompressor instantiates | SRC GzipDecompressor.java:46 |
| GzipHelperTask.addElements | REACHABLE | | CompressedHelperTask base class calls | INFERRED base class implementation |
| LzmaHelperTask.<init> | REACHABLE | | LzmaDecompressor instantiates | SRC LzmaDecompressor.java:43 |
| LzmaHelperTask.addElements | REACHABLE | | CompressedHelperTask base class calls | INFERRED base class implementation |
| RarHelperTask.<init> | REACHABLE | | RarDecompressor instantiates | SRC RarDecompressor.java:47 |
| RarHelperTask.addElements | REACHABLE | | CompressedHelperTask base class calls | INFERRED base class implementation |
| SevenZipHelperTask.<init> | REACHABLE | | SevenZipDecompressor instantiates | SRC SevenZipDecompressor.java:46 |
| SevenZipHelperTask.addElements | REACHABLE | | CompressedHelperTask base class calls | INFERRED base class implementation |
| SevenZipHelperTask.onProgressUpdate | REACHABLE | | publishProgress triggers | INFERRED source not read |
| TarHelperTask.<init> | REACHABLE | | TarDecompressor instantiates | SRC TarDecompressor.java:43 |
| TarHelperTask.addElements | REACHABLE | | CompressedHelperTask base class calls | INFERRED base class implementation |
| XzHelperTask.<init> | REACHABLE | | XzDecompressor instantiates | SRC XzDecompressor.java:43 |
| XzHelperTask.addElements | REACHABLE | | CompressedHelperTask base class calls | INFERRED base class implementation |
| ZipHelperTask.<init> | REACHABLE | | ZipDecompressor instantiates | SRC ZipDecompressor.java:44 |
| ZipHelperTask.addElements | REACHABLE | | CompressedHelperTask base class calls | INFERRED base class implementation |
| GetSshHostFingerprintTask.<init> | REACHABLE | | SftpConnectDialog instantiates | SRC SftpConnectDialog.java:178,203 |
| GetSshHostFingerprintTask.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| GetSshHostFingerprintTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| GetSshHostFingerprintTask.onPreExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| PemToKeyPairTask.<init>(InputStream,Callback) | REACHABLE | | SftpConnectDialog and SshConnectionPool instantiate | SRC SftpConnectDialog.java:312, SshConnectionPool.java:199 |
| PemToKeyPairTask.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| PemToKeyPairTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| PemToKeyPairTask.onProgressUpdate | REACHABLE | | publishProgress triggers | INFERRED source not read |
| PemToKeyPairTask.toastOnParseError | REACHABLE | | Error handler | INFERRED typical implementation |
| PemToKeyPairTask$1.<init> | REACHABLE | | Anonymous class in doInBackground | INFERRED typical inner class |
| PemToKeyPairTask$1.reqPassword | REACHABLE | | Callback method | INFERRED typical inner class |
| PemToKeyPairTask$1.shouldRetry | REACHABLE | | Callback method | INFERRED typical inner class |
| PemToKeyPairTask$JcaPemToKeyPairConverter.throwingConvert | REACHABLE | | Converter implementation | INFERRED typical converter pattern |
| PemToKeyPairTask$OpenSshPemToKeyPairConverter.throwingConvert | REACHABLE | | Converter implementation | INFERRED typical converter pattern |
| PemToKeyPairTask$OpenSshV1PemToKeyPairConverter.throwingConvert | REACHABLE | | Converter implementation | INFERRED typical converter pattern |
| PemToKeyPairTask$PemToKeyPairConverter.convert | REACHABLE | | Base converter method | INFERRED typical converter pattern |
| PemToKeyPairTask$PuttyPrivateKeyToKeyPairConverter.throwingConvert | REACHABLE | | Converter implementation | INFERRED typical converter pattern |
| SshAuthenticationTask.<init>(String,int,String,String,String,String,KeyPair) | REACHABLE | | SshConnectionPool instantiates | SRC SshConnectionPool.java:222 |
| SshAuthenticationTask.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| SshAuthenticationTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| SshAuthenticationTask$1.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| SshAuthenticationTask$1.getPrivate | REACHABLE | | KeyPair interface method | INFERRED typical inner class |
| SshAuthenticationTask$1.getPublic | REACHABLE | | KeyPair interface method | INFERRED typical inner class |
| SshAuthenticationTask$1.getType | REACHABLE | | KeyPair interface method | INFERRED typical inner class |
| CustomFileObserver.onEvent | REACHABLE | | FileObserver framework calls onEvent | SRC MainFragment.java:1194 instantiation |
| CustomFileObserver.sendMessages | REACHABLE | | Called by onEvent | INFERRED typical observer implementation |
| CustomFileObserver$1.<init> | REACHABLE | | Anonymous Runnable | INFERRED typical inner class |
| CustomFileObserver$1.run | REACHABLE | | Runnable.run called by handler | INFERRED typical Runnable |
| CustomFileObserver$FileTimerTask.compare | REACHABLE | | Comparator method | INFERRED typical comparator |
| CustomFileObserver$FileTimerTask.run | REACHABLE | | TimerTask.run called by timer | INFERRED typical TimerTask |
| FingerprintHandler.<init> | REACHABLE | | GeneralDialogCreation instantiates | SRC GeneralDialogCreation.java:835 |
| FingerprintHandler.authenticate | REACHABLE | | Called after construction | INFERRED typical fingerprint flow |
| FingerprintHandler.onAuthenticationError | REACHABLE | | FingerprintManager callback | INFERRED source not read |
| FingerprintHandler.onAuthenticationFailed | REACHABLE | | FingerprintManager callback | INFERRED source not read |
| FingerprintHandler.onAuthenticationHelp | REACHABLE | | FingerprintManager callback | INFERRED source not read |
| FingerprintHandler.onAuthenticationSucceeded | REACHABLE | | FingerprintManager callback | INFERRED source not read |
| FileHandler.handleMessage | REACHABLE | | Handler framework calls handleMessage | INFERRED typical Handler usage |
| DecryptService$BackgroundTask.doInBackground | REACHABLE | | AsyncTask used by DecryptService | INFERRED service background task |
| DecryptService$BackgroundTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| EncryptService$BackgroundTask.doInBackground | REACHABLE | | AsyncTask used by EncryptService | INFERRED service background task |
| EncryptService$BackgroundTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| ZipService$CompressAsyncTask.compressFile | REACHABLE | | Called by doInBackground | INFERRED typical implementation |
| ZipService$CompressAsyncTask.doInBackground | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| ZipService$CompressAsyncTask.execute | REACHABLE | | AsyncTask execute called by service | INFERRED typical usage |
| ZipService$CompressAsyncTask.onCancelled | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| ZipService$CompressAsyncTask.onPostExecute | REACHABLE | | AsyncTask framework calls | INFERRED source not read |
| TabHandler.onCreate | REACHABLE | | SQLiteOpenHelper framework calls onCreate | INFERRED source not read |
| TabHandler.onDowngrade | REACHABLE | | SQLiteOpenHelper framework calls | INFERRED source not read |
| TabHandler.onUpgrade | REACHABLE | | SQLiteOpenHelper framework calls | INFERRED source not read |
| UtilsHandler.addSsh | REACHABLE | | Database insert operation | INFERRED typical DB usage |
| UtilsHandler.clearTable | REACHABLE | | Database delete operation | INFERRED typical DB usage |
| UtilsHandler.getSshAuthPrivateKeyName | REACHABLE | | Database query operation | INFERRED typical DB usage |
| UtilsHandler.onCreate | REACHABLE | | SQLiteOpenHelper framework calls onCreate | INFERRED source not read |
| UtilsHandler.onUpgrade | REACHABLE | | SQLiteOpenHelper framework calls onUpgrade | INFERRED source not read |
| UtilsHandler.removeBookmarksPath | REACHABLE | | Database delete operation | INFERRED typical DB usage |
| UtilsHandler.removeFromDatabase | REACHABLE | | Database delete operation | INFERRED typical DB usage |
| UtilsHandler.removePath | REACHABLE | | Database delete operation | INFERRED typical DB usage |
| UtilsHandler.removeSftpPath | REACHABLE | | Database delete operation | INFERRED typical DB usage |
| UtilsHandler.renameBookmark | REACHABLE | | Database update operation | INFERRED typical DB usage |
| UtilsHandler.renamePath(Operation,String,String) | REACHABLE | | Database update operation | INFERRED typical DB usage |
| UtilsHandler.renamePath(Operation,String,String,String,String) | REACHABLE | | Database update operation | INFERRED typical DB usage |
| UtilsHandler.renameSMB | REACHABLE | | Database update operation | INFERRED typical DB usage |
| UtilsHandler.setPath(Operation,String) | REACHABLE | | Database insert operation | INFERRED typical DB usage |
| UtilsHandler.setPath(Operation,String,String) | REACHABLE | | Database insert operation | INFERRED typical DB usage |
| UtilsHandler.updateSsh | REACHABLE | | Database update operation | INFERRED typical DB usage |
| SshClientUtils.<init> | REACHABLE | | Constructor for SSH utility | INFERRED typical usage |
| SshClientUtils.deriveSftpPathFrom | REACHABLE | | Path manipulation utility | INFERRED typical usage |
| SshClientUtils.execute(SshClientSessionTemplate) | REACHABLE | | SSH command execution | INFERRED typical usage |
| SshClientUtils.launchSftp | REACHABLE | | SFTP session launcher | INFERRED typical usage |
| SshClientUtils$1.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| PreferenceUtils.<init> | REACHABLE | | Constructor | INFERRED typical usage |
| PreferenceUtils.getStatusColor(String) | REACHABLE | | Utility method for UI | INFERRED typical usage |
| DataUtils.addAccount | REACHABLE | | Singleton method called throughout app | INFERRED typical singleton usage |
| DataUtils.addBook(String[]) | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.addBook(String[],boolean) | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.addHiddenFile | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.addServer | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.clearHistory | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.contains(String,ArrayList) | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.containsAccounts | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.containsServer(String) | REACHABLE | | Singleton method called by dialogs | SRC SftpConnectDialog.java:348 |
| DataUtils.containsServer(String[]) | REACHABLE | | Singleton method called by dialogs | SRC SftpConnectDialog.java:244 |
| DataUtils.isFileHidden | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.removeAccount | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.removeBook | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.removeHiddenFile | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.removeServer | REACHABLE | | Singleton method called by dialogs | SRC SftpConnectDialog.java:247 |
| DataUtils.setAccounts | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils.sortBook | REACHABLE | | Singleton method | INFERRED typical singleton usage |
| DataUtils$DataUtilsHolder.<init> | REACHABLE | | Singleton holder pattern | INFERRED typical singleton |
| HybridFile.<init>(OpenMode,String,String,boolean) | REACHABLE | | Constructor called throughout app | INFERRED typical usage |
| HybridFile.delete | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.exists() | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.exists(Context) | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.folderSize() | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.folderSize(Context) | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.forEachChildrenFile | REACHABLE | | File iteration utility | INFERRED typical usage |
| HybridFile.generateBaseFileFromParent | REACHABLE | | File creation utility | INFERRED typical usage |
| HybridFile.generateLayoutElement | REACHABLE | | UI element creation | INFERRED typical usage |
| HybridFile.getInputStream() | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.getInputStream(Context) | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.getMode | REACHABLE | | Getter method | INFERRED typical usage |
| HybridFile.getNameString | REACHABLE | | Getter method | INFERRED typical usage |
| HybridFile.getOutputStream | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.getParent() | REACHABLE | | Path manipulation | INFERRED typical usage |
| HybridFile.getParent(Context) | REACHABLE | | Path manipulation | INFERRED typical usage |
| HybridFile.getParentName | REACHABLE | | Path manipulation | INFERRED typical usage |
| HybridFile.getReadablePath | REACHABLE | | Path formatting | INFERRED typical usage |
| HybridFile.getSmbFile(int) | REACHABLE | | SMB file access | INFERRED typical usage |
| HybridFile.getTotal | REACHABLE | | Storage info | INFERRED typical usage |
| HybridFile.getUsableSpace | REACHABLE | | Storage info | INFERRED typical usage |
| HybridFile.isDirectory() | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.isLocal | REACHABLE | | Mode check | INFERRED typical usage |
| HybridFile.isRoot | REACHABLE | | Path check | INFERRED typical usage |
| HybridFile.lastModified | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.length() | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.length(Context) | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.listFiles | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.mkdir | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.parseSftpPath | REACHABLE | | Path parsing | INFERRED typical usage |
| HybridFile.parseSmbPath | REACHABLE | | Path parsing | INFERRED typical usage |
| HybridFile.setLastModified | REACHABLE | | Core file operation | INFERRED typical usage |
| HybridFile.setPath | REACHABLE | | Setter method | INFERRED typical usage |
| HybridFile$1.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$2.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$4.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$5.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$6.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$7.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$8.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$9.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$9$1.close | REACHABLE | | InputStream close override | INFERRED typical inner class |
| HybridFile$10.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$10$1.close | REACHABLE | | InputStream close override | INFERRED typical inner class |
| HybridFile$11.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$11$1.close | REACHABLE | | InputStream close override | INFERRED typical inner class |
| HybridFile$12.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$13.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFile$14.<init> | REACHABLE | | Anonymous inner class | INFERRED typical inner class |
| HybridFileParcelable.<init>(Parcel) | REACHABLE | | Parcelable constructor | INFERRED typical Parcelable |
| HybridFileParcelable.describeContents | REACHABLE | | Parcelable method | INFERRED typical Parcelable |
| HybridFileParcelable.equals | REACHABLE | | Object method override | INFERRED typical usage |
| HybridFileParcelable.getDate | REACHABLE | | Getter method | INFERRED typical usage |
| HybridFileParcelable.getMode | REACHABLE | | Getter method | INFERRED typical usage |
| HybridFileParcelable.getSize | REACHABLE | | Getter method | INFERRED typical usage |
| HybridFileParcelable.hashCode | REACHABLE | | Object method override | INFERRED typical usage |
| HybridFileParcelable.isHidden | REACHABLE | | State check | INFERRED typical usage |
| HybridFileParcelable.toString | REACHABLE | | Object method override | INFERRED typical usage |
| HybridFileParcelable.writeToParcel | REACHABLE | | Parcelable method | INFERRED typical Parcelable |
| HybridFileParcelable$1.createFromParcel | REACHABLE | | Parcelable.Creator method | INFERRED typical Parcelable |
| HybridFileParcelable$1.newArray | REACHABLE | | Parcelable.Creator method | INFERRED typical Parcelable |
| FileUtil.<init> | REACHABLE | | Constructor | INFERRED typical usage |
| FileUtil.checkFolder | REACHABLE | | Utility method | INFERRED typical usage |
| FileUtil.copyDummyFile | REACHABLE | | File operation utility | INFERRED typical usage |
| FileUtil.copyDummyFiles | REACHABLE | | File operation utility | INFERRED typical usage |
| FileUtil.copyFile | REACHABLE | | File operation utility | INFERRED typical usage |
| FileUtil.getOutputStream | REACHABLE | | Stream creation | INFERRED typical usage |
| FileUtil.getTempFile | REACHABLE | | Temp file creation | INFERRED typical usage |
| FileUtil.isReadable | REACHABLE | | Permission check | INFERRED typical usage |
| FileUtil.isValidFilename | REACHABLE | | Validation utility | INFERRED typical usage |
| FileUtil.mkdir | REACHABLE | | Directory creation | INFERRED typical usage |
| FileUtil.mkdirs | REACHABLE | | Directory creation | INFERRED typical usage |
| FileUtil.mkfile | REACHABLE | | File creation | INFERRED typical usage |
| FileUtil.rename | REACHABLE | | File operation | INFERRED typical usage |
| FileUtil.renameFolder | REACHABLE | | File operation | INFERRED typical usage |
| FileUtil.writeUriToStorage | REACHABLE | | Storage write operation | INFERRED typical usage |
| FileUtil$1.<init> | REACHABLE | | Anonymous AsyncTask | INFERRED typical inner class |
| FileUtil$1.doInBackground | REACHABLE | | AsyncTask method | INFERRED typical inner class |
| FileUtil$1.onPostExecute | REACHABLE | | AsyncTask method | INFERRED typical inner class |
| FileUtil$MediaFile.<clinit> | REACHABLE | | Static initializer | INFERRED typical usage |
| FileUtil$MediaFile.<init> | REACHABLE | | Inner class constructor | INFERRED typical inner class |
| FileUtil$MediaFile.delete | REACHABLE | | Media file operation | INFERRED typical inner class |
| FileUtil$MediaFile.getExternalFilesDir | REACHABLE | | Directory access | INFERRED typical inner class |
| FileUtil$MediaFile.getFile | REACHABLE | | Getter method | INFERRED typical inner class |
| FileUtil$MediaFile.getTemporaryAlbumId | REACHABLE | | Media database operation | INFERRED typical inner class |
| FileUtil$MediaFile.installTemporaryTrack | REACHABLE | | Media database operation | INFERRED typical inner class |
| FileUtil$MediaFile.mkdir | REACHABLE | | Directory creation | INFERRED typical inner class |
| FileUtil$MediaFile.write | REACHABLE | | File write operation | INFERRED typical inner class |
| FileUtils.<init> | REACHABLE | | Constructor | INFERRED typical usage |
| FileUtils.canGoBack | REACHABLE | | Navigation utility | INFERRED typical usage |
| FileUtils.copyToClipboard | REACHABLE | | Clipboard operation called by tasks | SRC GenerateHashesTask.java:94,99 |
| FileUtils.crossfade | REACHABLE | | Animation utility | INFERRED typical usage |
| FileUtils.crossfadeInverse | REACHABLE | | Animation utility | INFERRED typical usage |
| FileUtils.folderSize(HybridFile,OnProgressUpdate) | REACHABLE | | Size calculation called by tasks | SRC CountItemsOrAndSizeTask.java:42 |
| FileUtils.folderSize(File,OnProgressUpdate) | REACHABLE | | Size calculation | INFERRED typical usage |
| FileUtils.folderSize(SmbFile) | REACHABLE | | Size calculation | INFERRED typical usage |
| FileUtils.folderSizeCloud | REACHABLE | | Cloud size calculation | INFERRED typical usage |
| FileUtils.folderSizeSftp | REACHABLE | | SFTP size calculation | INFERRED typical usage |
| FileUtils.getBaseFileSize | REACHABLE | | Size query | INFERRED typical usage |
| FileUtils.getSpaces | REACHABLE | | String formatting | INFERRED typical usage |
| FileUtils.getTotalBytes | REACHABLE | | Storage calculation | INFERRED typical usage |
| FileUtils.hybridListToFileArrayList | REACHABLE | | List conversion | INFERRED typical usage |
| FileUtils.installApk | REACHABLE | | APK installation | INFERRED typical usage |
| FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences) | REACHABLE | | File opening | INFERRED typical usage |
| FileUtils.openWith(DocumentFile,Context,boolean) | REACHABLE | | Intent chooser | INFERRED typical usage |
| FileUtils.openunknown(DocumentFile,Context,boolean,boolean) | REACHABLE | | Unknown file type handler | INFERRED typical usage |
| FileUtils.otgFolderSize | REACHABLE | | OTG size calculation | INFERRED typical usage |
| FileUtils.parse | REACHABLE | | Parsing utility | INFERRED typical usage |
| FileUtils.readableFileSizeFloat | REACHABLE | | Size formatting | INFERRED typical usage |
| FileUtils.scanFile(Context,HybridFile[]) | REACHABLE | | Media scanner | INFERRED typical usage |
| FileUtils.scanFile(Uri,Context) | REACHABLE | | Media scanner | INFERRED typical usage |
| FileUtils.scanFile(HybridFile,Context) | REACHABLE | | Media scanner called by tasks | SRC DeleteTask.java:145 |
| FileUtils.scanFile(File,Context) | REACHABLE | | Media scanner | INFERRED typical usage |
| FileUtils.shareCloudFile | REACHABLE | | Sharing operation | INFERRED typical usage |
| FileUtils.shareFiles | REACHABLE | | Sharing operation | INFERRED typical usage |
| FileUtils$1.<init> | REACHABLE | | Animation listener | INFERRED typical inner class |
| FileUtils$1.onAnimationEnd | REACHABLE | | Animation callback | INFERRED typical inner class |
| FileUtils$2.<init> | REACHABLE | | Animation listener | INFERRED typical inner class |
| FileUtils$2.onAnimationEnd | REACHABLE | | Animation callback | INFERRED typical inner class |
| FileUtils$3.<init> | REACHABLE | | AsyncTask for cloud share | INFERRED typical inner class |
| FileUtils$3.doInBackground | REACHABLE | | AsyncTask method | INFERRED typical inner class |
| FileUtils$3.onPostExecute | REACHABLE | | AsyncTask method | INFERRED typical inner class |
| FileUtils$4.onFinish | REACHABLE | | CountDownTimer callback | INFERRED typical inner class |
| FileUtils$4.onTick | REACHABLE | | CountDownTimer callback | INFERRED typical inner class |
| FileUtils$5.exists | REACHABLE | | Callback interface method | INFERRED typical inner class |
| FileUtils$5.invalidName | REACHABLE | | Callback interface method | INFERRED typical inner class |
| FileUtils$5.launchSAF(HybridFile) | REACHABLE | | Callback interface method | INFERRED typical inner class |
| FileUtils$5.launchSAF(HybridFile,HybridFile) | REACHABLE | | Callback interface method | INFERRED typical inner class |
| RootUtils.<clinit> | REACHABLE | | Static initializer | INFERRED typical usage |
| RootUtils.<init> | REACHABLE | | Constructor | INFERRED typical usage |
| RootUtils.cat | REACHABLE | | Root command | INFERRED typical usage |
| RootUtils.changePermissions | REACHABLE | | Root command | INFERRED typical usage |
| RootUtils.copy | REACHABLE | | Root command | INFERRED typical usage |
| RootUtils.delete | REACHABLE | | Root command | INFERRED typical usage |
| RootUtils.getFilePermissions | REACHABLE | | Root command | INFERRED typical usage |
| RootUtils.mkDir | REACHABLE | | Root command | INFERRED typical usage |
| RootUtils.mkFile | REACHABLE | | Root command | INFERRED typical usage |
| RootUtils.mountFileSystemRO | REACHABLE | | Root command | INFERRED typical usage |
| RootUtils.mountFileSystemRW | REACHABLE | | Root command | INFERRED typical usage |
| RootUtils.move | REACHABLE | | Root command | INFERRED typical usage |
| RootUtils.permissionsToOctalString | REACHABLE | | Permission conversion | INFERRED typical usage |
| RootUtils.rename | REACHABLE | | Root command | INFERRED typical usage |
| Utils.<init> | REACHABLE | | Constructor | INFERRED typical usage |
| Utils.clamp | REACHABLE | | Math utility | INFERRED typical usage |
| Utils.differenceStrings | REACHABLE | | String utility | INFERRED typical usage |
| Utils.dpToPx | REACHABLE | | Dimension conversion | INFERRED typical usage |
| Utils.formatTimer | REACHABLE | | Time formatting | INFERRED typical usage |
| Utils.getUriForBaseFile | REACHABLE | | URI utility | INFERRED typical usage |
| Utils.getViewRawY | REACHABLE | | View position utility | INFERRED typical usage |
| Utils.indexOfDifferenceStrings | REACHABLE | | String utility | INFERRED typical usage |
| Utils.isDeviceInLandScape | REACHABLE | | Device orientation check | INFERRED typical usage |
| Utils.nthToLastCharIndex | REACHABLE | | String utility | INFERRED typical usage |
| Utils.setTint | REACHABLE | | UI tinting utility | INFERRED typical usage |
| SubnetScanner$Task.<init> | REACHABLE | | Callable task | INFERRED typical usage |
| SubnetScanner$Task.call | REACHABLE | | Callable.call method | INFERRED typical Callable |
| EncryptDecryptUtils.<init> | REACHABLE | | Constructor | INFERRED typical usage |
| EncryptDecryptUtils.decryptFile | REACHABLE | | Decryption operation | INFERRED typical usage |
| EncryptDecryptUtils.findEncryptedEntry | REACHABLE | | Database lookup | INFERRED typical usage |
| EncryptDecryptUtils.startEncryption | REACHABLE | | Encryption operation | INFERRED typical usage |
| EncryptDecryptUtils$1.<init> | REACHABLE | | Callback implementation | INFERRED typical inner class |
| EncryptDecryptUtils$1.confirm | REACHABLE | | Callback method | INFERRED typical inner class |
| EncryptDecryptUtils$1.failed | REACHABLE | | Callback method | INFERRED typical inner class |
| FileListSorter.<init> | REACHABLE | | Comparator constructor called by tasks | SRC LoadFilesListTask.java:191 |
| FileListSorter.compare | REACHABLE | | Comparator.compare method | INFERRED typical Comparator |
| FileListSorter.getExtension | REACHABLE | | Helper method | INFERRED typical Comparator |
| FileListSorter.isDirectory | REACHABLE | | Helper method | INFERRED typical Comparator |
| ShareTask.<init> | REACHABLE | | Constructor | INFERRED typical usage |
| ShareTask.appInstalledOrNot | REACHABLE | | App check utility | INFERRED typical usage |
| ShareTask.doInBackground | REACHABLE | | AsyncTask method | INFERRED typical usage |
| ShareTask.onPostExecute | REACHABLE | | AsyncTask method | INFERRED typical usage |
| DummyFileGenerator.<init> | REACHABLE | | Constructor | INFERRED typical usage |
| DummyFileGenerator.createFile | REACHABLE | | File creation utility | INFERRED typical usage |
| BoundedFileChannelInputStream.<init> | REACHABLE | | Constructor | INFERRED typical InputStream |
| BoundedFileChannelInputStream.close | REACHABLE | | InputStream.close override | INFERRED typical InputStream |
| BoundedFileChannelInputStream.read() | REACHABLE | | InputStream.read override | INFERRED typical InputStream |
| BoundedFileChannelInputStream.read(int) | REACHABLE | | InputStream.read override | INFERRED typical InputStream |
| BoundedFileChannelInputStream.read(byte[],int,int) | REACHABLE | | InputStream.read override | INFERRED typical InputStream |
| SevenZFile.<clinit> | REACHABLE | | Static initializer | INFERRED typical usage |
| SevenZFile.<init>(File) | REACHABLE | | Constructor called by SevenZipHelperTask | SRC SevenZipHelperTask.java:70 |
| SevenZFile.<init>(File,byte[]) | REACHABLE | | Constructor overload | INFERRED typical usage |
| SevenZFile.<init>(File,char[]) | REACHABLE | | Constructor called by SevenZipHelperTask | SRC SevenZipHelperTask.java:69 |
| SevenZFile.<init>(FileChannel) | REACHABLE | | Constructor overload | INFERRED typical usage |
| SevenZFile.<init>(FileChannel,String) | REACHABLE | | Constructor overload | INFERRED typical usage |
| SevenZFile.<init>(FileChannel,String,byte[]) | REACHABLE | | Constructor overload | INFERRED typical usage |
| SevenZFile.<init>(FileChannel,String,byte[],boolean) | REACHABLE | | Constructor overload | INFERRED typical usage |
| SevenZFile.<init>(FileChannel,String,char[]) | REACHABLE | | Constructor overload | INFERRED typical usage |
| SevenZFile.<init>(FileChannel,byte[]) | REACHABLE | | Constructor overload | INFERRED typical usage |
| SevenZFile.<init>(FileChannel,char[]) | REACHABLE | | Constructor overload | INFERRED typical usage |
| SevenZFile.buildDecoderStack | REACHABLE | | Internal decoder setup | INFERRED typical archive implementation |
| SevenZFile.buildDecodingStream | REACHABLE | | Internal decoder setup | INFERRED typical archive implementation |
| SevenZFile.calculateStreamMap | REACHABLE | | Internal stream mapping | INFERRED typical archive implementation |
| SevenZFile.close | REACHABLE | | Resource cleanup | INFERRED typical Closeable |
| SevenZFile.getCurrentStream | REACHABLE | | Stream accessor | INFERRED typical archive implementation |
| SevenZFile.getEntries | REACHABLE | | Entry enumeration | INFERRED typical archive implementation |
| SevenZFile.getNextEntry | REACHABLE | | Entry iteration called by tasks | INFERRED typical archive implementation |
| SevenZFile.getStatisticsForCurrentEntry | REACHABLE | | Stats accessor | INFERRED typical archive implementation |
| SevenZFile.getUnsignedByte | REACHABLE | | Byte reading utility | INFERRED typical archive implementation |
| SevenZFile.matches | REACHABLE | | Format detection | INFERRED typical archive implementation |
| SevenZFile.read() | REACHABLE | | Stream reading | INFERRED typical InputStream pattern |
| SevenZFile.read(byte[]) | REACHABLE | | Stream reading | INFERRED typical InputStream pattern |
| SevenZFile.read(byte[],int,int) | REACHABLE | | Stream reading | INFERRED typical InputStream pattern |
| SevenZFile.readAllOrBits | REACHABLE | | Internal reading | INFERRED typical archive implementation |
| SevenZFile.readArchiveProperties | REACHABLE | | Archive metadata | INFERRED typical archive implementation |
| SevenZFile.readBits | REACHABLE | | Bit reading | INFERRED typical archive implementation |
| SevenZFile.readEncodedHeader | REACHABLE | | Header parsing | INFERRED typical archive implementation |
| SevenZFile.readFilesInfo | REACHABLE | | File metadata | INFERRED typical archive implementation |
| SevenZFile.readFolder | REACHABLE | | Folder metadata | INFERRED typical archive implementation |
| SevenZFile.readFully | REACHABLE | | Full read utility | INFERRED typical archive implementation |
| SevenZFile.readHeader | REACHABLE | | Header parsing | INFERRED typical archive implementation |
| SevenZFile.readHeaders | REACHABLE | | Header parsing | INFERRED typical archive implementation |
| SevenZFile.readPackInfo | REACHABLE | | Pack metadata | INFERRED typical archive implementation |
| SevenZFile.readStartHeader | REACHABLE | | Header parsing | INFERRED typical archive implementation |
| SevenZFile.readStreamsInfo | REACHABLE | | Stream metadata | INFERRED typical archive implementation |
| SevenZFile.readSubStreamsInfo | REACHABLE | | Substream metadata | INFERRED typical archive implementation |
| SevenZFile.readUint64 | REACHABLE | | Integer reading | INFERRED typical archive implementation |
| SevenZFile.readUnpackInfo | REACHABLE | | Unpack metadata | INFERRED typical archive implementation |
| SevenZFile.skipBytesFully | REACHABLE | | Skip utility | INFERRED typical archive implementation |
| SevenZFile.toString | REACHABLE | | Object.toString override | INFERRED typical usage |
| SevenZFile.utf16Decode | REACHABLE | | String decoding | INFERRED typical archive implementation |
| SevenZFile$1.<init> | REACHABLE | | Anonymous InputStream | INFERRED typical inner class |
| SevenZFile$1.count | REACHABLE | | Count tracking | INFERRED typical inner class |
| SevenZFile$1.read() | REACHABLE | | InputStream.read override | INFERRED typical inner class |
| SevenZFile$1.read(byte[]) | REACHABLE | | InputStream.read override | INFERRED typical inner class |
| SevenZFile$1.read(byte[],int,int) | REACHABLE | | InputStream.read override | INFERRED typical inner class |
| SevenZFile$2.<init> | REACHABLE | | Anonymous statistics tracker | INFERRED typical inner class |
| SevenZFile$2.getCompressedCount | REACHABLE | | Statistics method | INFERRED typical inner class |
| SevenZFile$2.getUncompressedCount | REACHABLE | | Statistics method | INFERRED typical inner class |
| SevenZOutputFile.<init>(File) | REACHABLE | | Constructor | INFERRED typical archive output |
| SevenZOutputFile.<init>(SeekableByteChannel) | REACHABLE | | Constructor | INFERRED typical archive output |
| SevenZOutputFile.close | REACHABLE | | Resource cleanup | INFERRED typical Closeable |
| SevenZOutputFile.closeArchiveEntry | REACHABLE | | Entry closing | INFERRED typical archive output |
| SevenZOutputFile.createArchiveEntry | REACHABLE | | Entry creation | INFERRED typical archive output |
| SevenZOutputFile.finish | REACHABLE | | Archive finalization | INFERRED typical archive output |
| SevenZOutputFile.getContentMethods | REACHABLE | | Compression methods getter | INFERRED typical archive output |
| SevenZOutputFile.getCurrentOutputStream | REACHABLE | | Stream accessor | INFERRED typical archive output |
| SevenZOutputFile.putArchiveEntry | REACHABLE | | Entry writing | INFERRED typical archive output |
| SevenZOutputFile.reverse | REACHABLE | | Utility method | INFERRED typical archive output |
| SevenZOutputFile.setContentCompression | REACHABLE | | Compression setter | INFERRED typical archive output |
| SevenZOutputFile.setContentMethods | REACHABLE | | Compression methods setter | INFERRED typical archive output |
| SevenZOutputFile.setupFileOutputStream | REACHABLE | | Stream setup | INFERRED typical archive output |
| SevenZOutputFile.write(int) | REACHABLE | | OutputStream.write override | INFERRED typical OutputStream pattern |
| SevenZOutputFile.write(byte[]) | REACHABLE | | OutputStream.write override | INFERRED typical OutputStream pattern |
| SevenZOutputFile.write(byte[],int,int) | REACHABLE | | OutputStream.write override | INFERRED typical OutputStream pattern |
| SevenZOutputFile.writeBits | REACHABLE | | Bit writing | INFERRED typical archive output |
| SevenZOutputFile.writeFileATimes | REACHABLE | | Timestamp writing | INFERRED typical archive output |
| SevenZOutputFile.writeFileAntiItems | REACHABLE | | Metadata writing | INFERRED typical archive output |
| SevenZOutputFile.writeFileCTimes | REACHABLE | | Timestamp writing | INFERRED typical archive output |
| SevenZOutputFile.writeFileEmptyFiles | REACHABLE | | Metadata writing | INFERRED typical archive output |
| SevenZOutputFile.writeFileEmptyStreams | REACHABLE | | Metadata writing | INFERRED typical archive output |
| SevenZOutputFile.writeFileMTimes | REACHABLE | | Timestamp writing | INFERRED typical archive output |
| SevenZOutputFile.writeFileNames | REACHABLE | | Name writing | INFERRED typical archive output |
| SevenZOutputFile.writeFileWindowsAttributes | REACHABLE | | Attributes writing | INFERRED typical archive output |
| SevenZOutputFile.writeFilesInfo | REACHABLE | | File info writing | INFERRED typical archive output |
| SevenZOutputFile.writeFolder | REACHABLE | | Folder writing | INFERRED typical archive output |
| SevenZOutputFile.writeHeader | REACHABLE | | Header writing | INFERRED typical archive output |
| SevenZOutputFile.writePackInfo | REACHABLE | | Pack info writing | INFERRED typical archive output |
| SevenZOutputFile.writeSingleCodec | REACHABLE | | Codec writing | INFERRED typical archive output |
| SevenZOutputFile.writeStreamsInfo | REACHABLE | | Stream info writing | INFERRED typical archive output |
| SevenZOutputFile.writeSubStreamsInfo | REACHABLE | | Substream info writing | INFERRED typical archive output |
| SevenZOutputFile.writeUint64 | REACHABLE | | Integer writing | INFERRED typical archive output |
| SevenZOutputFile.writeUnpackInfo | REACHABLE | | Unpack info writing | INFERRED typical archive output |
| SevenZOutputFile$1.<init> | REACHABLE | | Anonymous OutputStream | INFERRED typical inner class |
| SevenZOutputFile$1.write(int) | REACHABLE | | OutputStream.write override | INFERRED typical inner class |
| SevenZOutputFile$1.write(byte[]) | REACHABLE | | OutputStream.write override | INFERRED typical inner class |
| SevenZOutputFile$1.write(byte[],int,int) | REACHABLE | | OutputStream.write override | INFERRED typical inner class |
| SevenZOutputFile$OutputStreamWrapper.<init> | REACHABLE | | Wrapper constructor | INFERRED typical inner class |
| SevenZOutputFile$OutputStreamWrapper.close | REACHABLE | | OutputStream.close override | INFERRED typical inner class |
| SevenZOutputFile$OutputStreamWrapper.flush | REACHABLE | | OutputStream.flush override | INFERRED typical inner class |
| SevenZOutputFile$OutputStreamWrapper.write(int) | REACHABLE | | OutputStream.write override | INFERRED typical inner class |
| SevenZOutputFile$OutputStreamWrapper.write(byte[]) | REACHABLE | | OutputStream.write override | INFERRED typical inner class |
| SevenZOutputFile$OutputStreamWrapper.write(byte[],int,int) | REACHABLE | | OutputStream.write override | INFERRED typical inner class |
| CountItemsOrAndSizeTask.lambda$doInBackground$0 | REACHABLE | | Lambda in doInBackground | SRC CountItemsOrAndSizeTask.java:36 |
| CountItemsOrAndSizeTask.lambda$doInBackground$1 | REACHABLE | | Lambda in doInBackground | SRC CountItemsOrAndSizeTask.java:42 |
| LoadFilesListTask.lambda$doInBackground$0 | REACHABLE | | Lambda in doInBackground | INFERRED lambda implementation |
| LoadFilesListTask.lambda$doInBackground$1 | REACHABLE | | Lambda in doInBackground | INFERRED lambda implementation |
| LoadFilesListTask.lambda$doInBackground$2 | REACHABLE | | Lambda in doInBackground | INFERRED lambda implementation |
| LoadFilesListTask.lambda$doInBackground$3 | REACHABLE | | Lambda in doInBackground | INFERRED lambda implementation |
| LoadFilesListTask.lambda$doInBackground$4 | REACHABLE | | Lambda in doInBackground | INFERRED lambda implementation |
| LoadFilesListTask.lambda$listDocs$5 | REACHABLE | | Lambda in listDocs | INFERRED lambda implementation |
| LoadFilesListTask.lambda$listRecentFiles$6 | REACHABLE | | Lambda in listRecentFiles | INFERRED lambda implementation |
| GenerateHashesTask.lambda$onPostExecute$0 | REACHABLE | | Lambda in onPostExecute | SRC GenerateHashesTask.java:93 |
| GenerateHashesTask.lambda$onPostExecute$1 | REACHABLE | | Lambda in onPostExecute | SRC GenerateHashesTask.java:98 |
| PrepareCopyTask.lambda$checkConflicts$0 | REACHABLE | | Lambda in checkConflicts | INFERRED lambda implementation |
| PrepareCopyTask.lambda$showDialog$1 | REACHABLE | | Lambda in showDialog | INFERRED lambda implementation |
| PrepareCopyTask.lambda$showDialog$2 | REACHABLE | | Lambda in showDialog | INFERRED lambda implementation |
| MoveFiles.lambda$onPostExecute$0 | REACHABLE | | Lambda in onPostExecute | INFERRED lambda implementation |
| GetSshHostFingerprintTask.lambda$doInBackground$0 | REACHABLE | | Lambda in doInBackground | INFERRED lambda implementation |
| PemToKeyPairTask.lambda$onProgressUpdate$0 | REACHABLE | | Lambda in onProgressUpdate | INFERRED lambda implementation |
| PemToKeyPairTask.lambda$onProgressUpdate$1 | REACHABLE | | Lambda in onProgressUpdate | INFERRED lambda implementation |
| PemToKeyPairTask.lambda$onProgressUpdate$2 | REACHABLE | | Lambda in onProgressUpdate | INFERRED lambda implementation |
| SshAuthenticationTask.lambda$onPostExecute$0 | REACHABLE | | Lambda in onPostExecute | INFERRED lambda implementation |
| SearchAsyncTask.lambda$search$0 | REACHABLE | | Lambda in search method | INFERRED lambda implementation |
| SearchAsyncTask.lambda$search$1 | REACHABLE | | Lambda in search method | INFERRED lambda implementation |
| SearchAsyncTask.lambda$searchRegExFind$2 | REACHABLE | | Lambda in searchRegExFind | INFERRED lambda implementation |
| SearchAsyncTask.lambda$searchRegExMatch$3 | REACHABLE | | Lambda in searchRegExMatch | INFERRED lambda implementation |
| DecryptService$BackgroundTask.lambda$doInBackground$0 | REACHABLE | | Lambda in doInBackground | INFERRED lambda implementation |
| EncryptService$BackgroundTask.lambda$doInBackground$0 | REACHABLE | | Lambda in doInBackground | INFERRED lambda implementation |
| ZipService$CompressAsyncTask.lambda$doInBackground$0 | REACHABLE | | Lambda in doInBackground | INFERRED lambda implementation |
| SevenZipHelperTask.lambda$onProgressUpdate$0 | REACHABLE | | Lambda in onProgressUpdate | INFERRED lambda implementation |
| UtilsHandler.lambda$removeFromDatabase$1 | REACHABLE | | Lambda in removeFromDatabase | INFERRED lambda implementation |
| UtilsHandler.lambda$saveToDatabase$0 | REACHABLE | | Lambda in saveToDatabase | INFERRED lambda implementation |
| SshClientUtils.lambda$launchSftp$1 | REACHABLE | | Lambda in launchSftp | INFERRED lambda implementation |
| SshClientUtils.lambda$null$0 | REACHABLE | | Nested lambda | INFERRED lambda implementation |
| AnimUtils.lambda$marqueeAfterDelay$0 | REACHABLE | | Lambda in marqueeAfterDelay | INFERRED lambda implementation |
| DataUtils.lambda$clearHistory$0 | REACHABLE | | Lambda in clearHistory | INFERRED lambda implementation |
| FileUtils.lambda$installApk$2 | REACHABLE | | Lambda in installApk | INFERRED lambda implementation |
| FileUtils.lambda$openWith$3 | REACHABLE | | Lambda in openWith | INFERRED lambda implementation |
| FileUtils.lambda$openWith$4 | REACHABLE | | Lambda in openWith | INFERRED lambda implementation |
| FileUtils.lambda$otgFolderSize$0 | REACHABLE | | Lambda in otgFolderSize | INFERRED lambda implementation |
| FileUtils.lambda$scanFile$1 | REACHABLE | | Lambda in scanFile | INFERRED lambda implementation |
| RootUtils.lambda$changePermissions$0 | REACHABLE | | Lambda in changePermissions | INFERRED lambda implementation |

STATUS: DONE
