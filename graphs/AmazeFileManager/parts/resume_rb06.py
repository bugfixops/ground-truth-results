# ---- resume batch rb_06 (2025-01-19)

# CopyService methods
e('CopyService.onCreate', 'CopyService.onDestroy', 'LIFECYCLE', 'Service.onDestroy called by framework when service destroyed',
  evidence='SRC asynchronous/services/CopyService.java:215-216; FW-SRC core/java/android/app/Service.java:510-516')

e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'CopyService.setProgressListener', 'CALL', 
  'ProcessViewerFragment sets progress listener when service connects',
  evidence='SRC fragments/ProcessViewerFragment.java:416')

# CountItemsOrAndSizeTask lambda methods
e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.lambda$doInBackground$0', 'CALL',
  'doInBackground uses lambda to count files: file -> x.incrementAndGet()',
  evidence='SRC asynchronous/asynctasks/CountItemsOrAndSizeTask.java:41')

e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.lambda$doInBackground$1', 'CALL',
  'doInBackground uses lambda for progress callback: data -> publishProgress(new Pair<>(folderLength, data))',
  evidence='SRC asynchronous/asynctasks/CountItemsOrAndSizeTask.java:48')

e('CountItemsOrAndSizeTask.lambda$doInBackground$1', 'CountItemsOrAndSizeTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate on main thread',
  evidence='SRC asynchronous/asynctasks/CountItemsOrAndSizeTask.java:48,59; INFERRED AsyncTask framework behavior')

# DataUtils lambda method
e('DataUtils.clearHistory', 'DataUtils.lambda$clearHistory$0', 'ASYNC',
  'clearHistory runs lambda in background: () -> dataChangeListener.onHistoryCleared()',
  evidence='SRC utils/DataUtils.java:411')
