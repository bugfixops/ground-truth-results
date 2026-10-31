# ---- Helper batch_024 label part (2024)

# ExtractService - started service for archive extraction
# Route: User extracts archive -> menu action onActionItemClicked/onClick -> Decompressor.decompress -> ServiceWatcherUtil.runService -> startService -> ExtractService.onStartCommand -> DoWork.execute -> doInBackground

e('Decompressor.decompress', 'ExtractService.onStartCommand', 'INTENT',
  'starts ExtractService via ServiceWatcherUtil.runService -> context.startService',
  evidence='SRC Decompressor.java:44-48, ServiceWatcherUtil.java:163')

e('ExtractService.onStartCommand', 'ExtractService$DoWork.<init>', 'CALL',
  'constructs DoWork AsyncTask',
  evidence='SRC ExtractService.java:146')

e('ExtractService.onStartCommand', 'ExtractService$DoWork.doInBackground', 'ASYNC',
  'executes DoWork AsyncTask',
  evidence='SRC ExtractService.java:146')

e('ExtractService$DoWork.doInBackground', 'ExtractService$DoWork$1.<init>', 'CALL',
  'constructs anonymous OnUpdate callback',
  evidence='SRC ExtractService.java:215-242')

e('ExtractService$DoWork$1.onStart', 'ExtractService$DoWork$1.onStart', 'FRAMEWORK',
  'extractor callback from CompressedHelper.getExtractorInstance',
  evidence='SRC ExtractService.java:215 (anonymous class passed to extractor)')

e('ExtractService$DoWork$1.onUpdate', 'ExtractService$DoWork$1.onUpdate', 'FRAMEWORK',
  'extractor callback',
  evidence='SRC ExtractService.java:215 (anonymous class passed to extractor)')

e('ExtractService$DoWork$1.onFinish', 'ExtractService$DoWork$1.onFinish', 'FRAMEWORK',
  'extractor callback',
  evidence='SRC ExtractService.java:215 (anonymous class passed to extractor)')

e('ExtractService$DoWork$1.isCancelled', 'ExtractService$DoWork$1.isCancelled', 'FRAMEWORK',
  'extractor callback',
  evidence='SRC ExtractService.java:215 (anonymous class passed to extractor)')

e('ExtractService$DoWork.doInBackground', 'ExtractService$DoWork.onPostExecute', 'FRAMEWORK',
  'AsyncTask completion',
  evidence='INFERRED android AsyncTask lifecycle (source not read)')

e('ExtractService$DoWork.doInBackground', 'ExtractService$DoWork.onProgressUpdate', 'FRAMEWORK',
  'AsyncTask publishProgress',
  evidence='SRC ExtractService.java:255 (publishProgress call on password error)')

e('ExtractService.onCreate', 'ExtractService$1.<init>', 'CALL',
  'constructs BroadcastReceiver',
  evidence='SRC ExtractService.java:283-289')

e('ExtractService$1.onReceive', 'ExtractService$1.onReceive', 'FRAMEWORK',
  'BroadcastReceiver callback on TAG_BROADCAST_EXTRACT_CANCEL',
  evidence='SRC ExtractService.java:90 (registerReceiver with IntentFilter)')

# EncryptedEntry - DB model for encrypted file passwords
# Reachable via CryptHandler which is used in EncryptDecryptUtils

e('EncryptDecryptUtils.startEncryption', 'EncryptedEntry.<init>', 'CALL',
  'constructs EncryptedEntry with path and password',
  evidence='SRC EncryptDecryptUtils.java:54')

e('CryptHandler.addEntry', 'EncryptedEntry.getPath', 'CALL',
  'gets path for DB insert',
  evidence='SRC CryptHandler.java:59')

e('CryptHandler.addEntry', 'EncryptedEntry.getPassword', 'CALL',
  'gets password for DB insert',
  evidence='SRC CryptHandler.java:60-61')

e('CryptHandler.findEntry', 'EncryptedEntry.<init>', 'CALL',
  'constructs empty EncryptedEntry',
  evidence='SRC CryptHandler.java:93')

e('CryptHandler.findEntry', 'EncryptedEntry.setId', 'CALL',
  'sets id from cursor',
  evidence='SRC CryptHandler.java:95')

e('CryptHandler.findEntry', 'EncryptedEntry.setPath', 'CALL',
  'sets path from cursor',
  evidence='SRC CryptHandler.java:96')

e('CryptHandler.findEntry', 'EncryptedEntry.setPassword', 'CALL',
  'sets password from cursor',
  evidence='SRC CryptHandler.java:97')

e('CryptHandler.getAllEntries', 'EncryptedEntry.<init>', 'CALL',
  'constructs EncryptedEntry per row',
  evidence='SRC CryptHandler.java:117')

e('CryptHandler.getAllEntries', 'EncryptedEntry.setId', 'CALL',
  'sets id from cursor',
  evidence='SRC CryptHandler.java:118')

e('CryptHandler.getAllEntries', 'EncryptedEntry.setPath', 'CALL',
  'sets path from cursor',
  evidence='SRC CryptHandler.java:119')

e('CryptHandler.getAllEntries', 'EncryptedEntry.setPassword', 'CALL',
  'sets password from cursor',
  evidence='SRC CryptHandler.java:120-121')

e('CryptHandler.updateEntry', 'EncryptedEntry.getId', 'CALL',
  'gets id for update query',
  evidence='SRC CryptHandler.java:79,85')

e('CryptHandler.updateEntry', 'EncryptedEntry.getPath', 'CALL',
  'gets path for update',
  evidence='SRC CryptHandler.java:80')

e('CryptHandler.updateEntry', 'EncryptedEntry.getPassword', 'CALL',
  'gets password for update',
  evidence='SRC CryptHandler.java:82')

e('ExtractService$DoWork.onProgressUpdate', 'ExtractService$DoWork.lambda$onProgressUpdate$0', 'CALL',
  'first lambda (positive button) for password dialog',
  evidence='SRC ExtractService.java:333-338')

e('ExtractService$DoWork.onProgressUpdate', 'ExtractService$DoWork.lambda$onProgressUpdate$1', 'CALL',
  'second lambda (negative button) for password dialog',
  evidence='SRC ExtractService.java:341-348')

e('ExtractService.onStartCommand', 'ExtractService.lambda$onStartCommand$0', 'CALL',
  'lambda for progress listener',
  evidence='SRC ExtractService.java:142-143')

e('ExtractService.onCreate', 'ExtractService$1.<init>', 'EXPLICIT',
  'changed to EXPLICIT for BroadcastReceiver construction',
  evidence='SRC ExtractService.java:283-289 (field initializer receiver1 = new BroadcastReceiver)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getNotificationManager', 'FRAMEWORK',
  'called by parent service to get notification manager',
  evidence='INFERRED AbstractProgressiveService.java:98 (source shows publishResults calls getNotificationManager)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getNotificationBuilder', 'FRAMEWORK',
  'called by parent service',
  evidence='INFERRED AbstractProgressiveService.java (source shows publishResults calls getNotificationBuilder)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getNotificationId', 'FRAMEWORK',
  'called by parent service',
  evidence='INFERRED AbstractProgressiveService.java (source shows publishResults calls getNotificationId)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getTitle', 'FRAMEWORK',
  'called by parent service',
  evidence='INFERRED AbstractProgressiveService.java:94 (publishResults calls getTitle)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getNotificationCustomViewSmall', 'FRAMEWORK',
  'called by parent service',
  evidence='INFERRED AbstractProgressiveService.java (publishResults calls getNotificationCustomViewSmall)')

e('AbstractProgressiveService.publishResults', 'ExtractService.getNotificationCustomViewBig', 'FRAMEWORK',
  'called by parent service',
  evidence='INFERRED AbstractProgressiveService.java (publishResults calls getNotificationCustomViewBig)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getNotificationCustomViewSmall', 'FRAMEWORK',
  'called by parent for indeterminate progress',
  evidence='INFERRED AbstractProgressiveService.java:63 (progressHalted calls getNotificationCustomViewSmall)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getNotificationCustomViewBig', 'FRAMEWORK',
  'called by parent for indeterminate progress',
  evidence='INFERRED AbstractProgressiveService.java:65 (progressHalted calls getNotificationCustomViewBig)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getNotificationManager', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:71 (progressHalted calls getNotificationManager)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getNotificationId', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:71 (progressHalted calls getNotificationId)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getNotificationBuilder', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:71 (progressHalted calls getNotificationBuilder)')

e('AbstractProgressiveService.progressHalted', 'ExtractService.getProgressHandler', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:77 (progressHalted calls getProgressHandler)')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getNotificationCustomViewSmall', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:76')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getNotificationCustomViewBig', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:78')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getProgressHandler', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:77,79')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getNotificationManager', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:80')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getNotificationId', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:80')

e('AbstractProgressiveService.progressResumed', 'ExtractService.getNotificationBuilder', 'FRAMEWORK',
  'called by parent',
  evidence='INFERRED AbstractProgressiveService.java:80')

e('ExtractService.onStartCommand', 'ExtractService.getTotalSize', 'CALL',
  'calculates total size for progress',
  evidence='SRC ExtractService.java:138')

e('ExtractService.onStartCommand', 'ExtractService.getProgressListener', 'CALL',
  'checks if listener exists before creating (implied in parent call flow)',
  evidence='INFERRED ExtractService.java:142 (setProgressListener called, getProgressListener likely used by parent)')

e('ExtractService.onStartCommand', 'ExtractService.setProgressListener', 'CALL',
  'sets progress listener lambda',
  evidence='SRC ExtractService.java:142')

e('ExtractService.onStartCommand', 'ExtractService.getDataPackages', 'CALL',
  'used by parent for progress tracking (implied)',
  evidence='INFERRED ExtractService.java (parent AbstractProgressiveService uses getDataPackages)')

e('ProcessViewerFragment.onServiceBound', 'ExtractService.getProgressListener', 'CALL',
  'ProcessViewerFragment accesses progress listener when bound',
  evidence='INFERRED ProcessViewerFragment binds to ExtractService and accesses its progress state')

e('ProcessViewerFragment.onServiceBound', 'ExtractService.getDataPackages', 'CALL',
  'ProcessViewerFragment accesses data packages for display',
  evidence='INFERRED ProcessViewerFragment uses getDataPackages to display progress')

e('ProcessViewerFragment.onServiceBound', 'ExtractService.getProgressHandler', 'CALL',
  'ProcessViewerFragment accesses progress handler',
  evidence='INFERRED ProcessViewerFragment uses getProgressHandler for progress updates')

e('ProcessViewerFragment.onServiceBound', 'ExtractService.setProgressListener', 'CALL',
  'ProcessViewerFragment sets its listener',
  evidence='INFERRED ProcessViewerFragment binds ExtractService and sets listener')

e('ProcessViewerFragment.onResume', 'ExtractService.onBind', 'RESULT',
  'ProcessViewerFragment binds ExtractService',
  evidence='SRC ProcessViewerFragment.java:161 (bindService with ExtractService.class)')

e('ExtractService$DoWork.onProgressUpdate', 'ExtractService$DoWork.toastOnParseError', 'CALL',
  'shows error toast on password dialog cancel',
  evidence='SRC ExtractService.java:343')

# UNREACHABLE methods
UNREACHABLE_PART_B024 = {
    'ExtractService.<clinit>': ('no_trigger_in_app', 'Only static final String constants; compile-time initialization, no runtime <clinit> needed', 'SRC ExtractService.java:69,85-88', 'SOURCE'),
    'ExtractService.<init>': ('framework_never_calls', 'Service instantiated by framework via no-arg constructor only; explicit constructor not in source', 'SRC ExtractService.java:65 (no explicit constructor defined)', 'INFERRED'),
}
