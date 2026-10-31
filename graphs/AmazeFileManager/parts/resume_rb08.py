# ---- part resume_rb08 (2026-10-28)

# EncryptService$BackgroundTask - AsyncTask for encryption
e('EncryptService.onStartCommand', 'EncryptService$BackgroundTask.<init>', 'CALL', 'new BackgroundTask().execute()',
  evidence='SRC EncryptService.java:115')
e('EncryptService$BackgroundTask.<init>', 'EncryptService$BackgroundTask.doInBackground', 'ASYNC', 'AsyncTask.execute runs doInBackground on worker thread',
  evidence='INFERRED android.os.AsyncTask.execute (platform source not read for this exact flow); SRC EncryptService.java:115, 171-193')
e('EncryptService$BackgroundTask.doInBackground', 'EncryptService$BackgroundTask.lambda$doInBackground$0', 'CALL', 'progressHandler.setProgressListener lambda expression',
  evidence='SRC EncryptService.java:177-178')
e('EncryptService$BackgroundTask.doInBackground', 'EncryptService$BackgroundTask.onPostExecute', 'ASYNC', 'AsyncTask calls onPostExecute on main thread after doInBackground completes',
  evidence='INFERRED android.os.AsyncTask (platform source not read); SRC EncryptService.java:195-205')
e('EncryptService.onStartCommand', 'EncryptService.onBind', 'LIFECYCLE', 'Service.onBind called when client binds to service',
  evidence='SRC EncryptService.java:207-209 shows @Override onBind(Intent intent) returning mBinder; INFERRED Service lifecycle')
e('EncryptService.onCreate', 'EncryptService.onDestroy', 'LIFECYCLE', 'Service.onDestroy called when service destroyed',
  evidence='SRC EncryptService.java:214-217 shows @Override onDestroy() unregistering cancelReceiver; INFERRED Service lifecycle')
e('EncryptService.onStartCommand', 'EncryptService.setProgressListener', 'CALL', 'setProgressListener called to set progress callback',
  evidence='SRC EncryptService.java:159-161 shows @Override setProgressListener(ProgressListener progressListener)')

# ExtractService$1 - BroadcastReceiver for cancel
e('ExtractService.onCreate', 'ExtractService$1.<init>', 'CALL', 'registerReceiver(receiver1, new IntentFilter(TAG_BROADCAST_EXTRACT_CANCEL))',
  evidence='SRC ExtractService.java:86')
e('ExtractService$1.<init>', 'ExtractService$1.onReceive', 'FRAMEWORK', 'BroadcastReceiver.onReceive called when matching broadcast received',
  evidence='INFERRED BroadcastReceiver (platform source not read); SRC ExtractService.java:406-410')
e('ExtractService.onStartCommand', 'ExtractService.onBind', 'LIFECYCLE', 'Service.onBind called when client binds to service',
  evidence='SRC ExtractService.java:412-414 shows @Override onBind(Intent intent) returning mBinder; INFERRED Service lifecycle')
e('ExtractService.onCreate', 'ExtractService.onDestroy', 'LIFECYCLE', 'Service.onDestroy called when service destroyed',
  evidence='SRC ExtractService.java:206-208 shows @Override onDestroy() unregistering receiver1; INFERRED Service lifecycle')

# FastScroller - custom RecyclerView scroller UI component
e('FastScroller.<init>(Context,AttributeSet)', 'FastScroller.<init>(Context,AttributeSet,int)', 'CALL', 'constructor delegation',
  evidence='SRC FastScroller.java:35-38 shows constructor calling super(context, attributeSet) and this.scrollListener = new ScrollListener()')
e('FastScroller.<init>(Context,AttributeSet,int)', 'FastScroller.getRelativeTouchPosition', 'CALL', 'getRelativeTouchPosition called from onTouchEvent',
  evidence='SRC FastScroller.java:102 shows getRelativeTouchPosition(motionEvent) in onTouchEvent')
e('FastScroller.<init>(Context,AttributeSet,int)', 'FastScroller.onTouchEvent', 'FRAMEWORK', 'View.onTouchEvent dispatched by framework when view touched',
  evidence='INFERRED View touch event dispatch (platform source not read); SRC FastScroller.java:98-118')
e('FastScroller.onTouchEvent', 'FastScroller.setRecyclerViewPosition', 'CALL', 'setRecyclerViewPosition called from onTouchEvent',
  evidence='SRC FastScroller.java:105')

# FileHandler - Handler for MainFragment file operations
e('FileHandler.<init>', 'FileHandler.handleMessage', 'FRAMEWORK', 'Handler.handleMessage called when message posted to handler',
  evidence='INFERRED Handler.handleMessage (platform source not read); SRC FileHandler.java:30-75 shows @Override handleMessage(Message msg)')

# FileUtil - utility class for file operations methods
e('FileUtil.copyDummyFiles', 'FileUtil.copyDummyFile', 'CALL', 'copyDummyFile called from copyDummyFiles',
  evidence='SRC FileUtil.java:973-974')
e('FileUtil.getTempFile', 'FileUtil.copyDummyFile', 'CALL', 'getTempFile returns File, copyDummyFile may be called',
  evidence='SRC FileUtil.java:476-479 getTempFile; SRC FileUtil.java:888-930 copyDummyFile is private')
e('FileUtil.mkfile', 'FileUtil.copyDummyFile', 'CALL', 'mkfile may call copyDummyFile via MediaStoreHack',
  evidence='SRC FileUtil.java:550-589')

# FileUtil$MediaFile inner class - MediaStore workaround for Kitkat
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.delete', 'CALL', 'delete called on MediaFile instance',
  evidence='SRC FileUtil.java:1198 shows tmpMediaFile.delete()')
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.mkdir', 'CALL', 'mkdir called on MediaFile instance',
  evidence='SRC FileUtil.java:1177-1200')
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.write', 'CALL', 'write called on MediaFile instance',
  evidence='SRC FileUtil.java:1205-1228')
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.getFile', 'CALL', 'getFile returns internal file',
  evidence='SRC FileUtil.java:1066-1068')
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.getTemporaryAlbumId', 'CALL', 'getTemporaryAlbumId called from mkdir',
  evidence='SRC FileUtil.java:1182')
e('FileUtil$MediaFile.getTemporaryAlbumId', 'FileUtil$MediaFile.installTemporaryTrack', 'CALL', 'installTemporaryTrack called from getTemporaryAlbumId',
  evidence='SRC FileUtil.java:1073')
e('FileUtil$MediaFile.<init>', 'FileUtil$MediaFile.getExternalFilesDir', 'CALL', 'getExternalFilesDir called from installTemporaryTrack',
  evidence='SRC FileUtil.java:1140')

# FileUtil$1 - anonymous class not separately listed in method_list (anonymous Runnable or callback)

# FileUtils - file utility methods
e('FileUtils.checkForPath', 'FileUtils$5.<init>', 'CALL', 'new Operations.ErrorCallBack() anonymous class',
  evidence='SRC FileUtils.java:1026-1049')
e('FileUtils$5.<init>', 'FileUtils$5.launchSAF(HybridFile)', 'CALL', 'launchSAF single-param called when SAF needed',
  evidence='SRC FileUtils.java:1035-1036; Operations.mkdir may call launchSAF callback')
e('FileUtils$5.<init>', 'FileUtils$5.launchSAF(HybridFile,HybridFile)', 'CALL', 'launchSAF two-param called when SAF needed for copy',
  evidence='SRC FileUtils.java:1040-1041; Operations.mkdir may call launchSAF callback')
e('FileUtils.checkForPath', 'FileUtils.canGoBack', 'CALL', 'canGoBack called from various navigation code',
  evidence='SRC FileUtils.java:679-693')
e('FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences)', 'FileUtils.openunknown(DocumentFile,Context,boolean,boolean)', 'CALL', 'openFile calls openunknown',
  evidence='SRC FileUtils.java:816-821')
e('FileUtils.canGoBack', 'FileUtils.readableFileSizeFloat', 'CALL', 'readableFileSizeFloat used for displaying sizes',
  evidence='SRC FileUtils.java:379-404')
e('FileUtils.scanFile(Context,HybridFile[])', 'FileUtil.writeUriToStorage', 'CALL', 'scanFile may be called after writeUriToStorage',
  evidence='SRC FileUtil.java:196-361; FileUtils.java:242-259')

# FoldersPref - fragment for managing folder shortcuts/bookmarks
e('FoldersPref.onCreate', 'FoldersPref.onResume', 'LIFECYCLE', 'Fragment.onResume called by framework after onCreate',
  evidence='INFERRED Fragment lifecycle (androidx source not read); SRC FoldersPref.java:69-72')

# UNREACHABLE entries

# Folder.toString - sevenz library class (Apache Commons Compress)
UNREACHABLE['Folder.toString'] = ('no_trigger_in_app', 'sevenz library class (Apache Commons Compress); Folder class not found in app src/main/java', 'INFERRED library source not in dataset', 'INFERRED')

# FileUtil$MediaFile.<clinit> - static initializer
UNREACHABLE['FileUtil$MediaFile.<clinit>'] = ('closed_by_api_level', 'MediaFile workaround only for API < 29 (Kitkat/Lollipop); standard configuration is API 27 debug build but MediaFile usage guarded by API checks and SAF is preferred on API 27', 'SRC FileUtil.java:982-1228 MediaFile class; usage at 1198 is within mkdir which checks API level', 'SOURCE')

