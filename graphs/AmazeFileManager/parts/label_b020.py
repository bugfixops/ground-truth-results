# ---- Helper batch_020 label part (2025-01-11)

# DataUtils$DataUtilsHolder methods
# The singleton holder is accessed via DataUtils.getInstance() which is called from many places
e('DataUtils.getInstance', 'DataUtils$DataUtilsHolder.<clinit>', 'CALL',
  'getInstance accesses the static INSTANCE field, triggering class init',
  evidence='SRC DataUtils.java:82-83 getInstance returns DataUtilsHolder.INSTANCE')

# DatapointParcelable methods
# DatapointParcelable is constructed in AbstractProgressiveService
e('AbstractProgressiveService.publishResults', 'DatapointParcelable.<clinit>', 'CALL',
  'First construction of DatapointParcelable triggers class initialization',
  evidence='SRC AbstractProgressiveService.java:157-159 new DatapointParcelable triggers <clinit>')

e('AbstractProgressiveService.publishResults', 'DatapointParcelable.<init>', 'CALL',
  'publishResults creates DatapointParcelable with 8 parameters (desc="(Ljava/lang/String;IIJJJZZ)V")',
  evidence='SRC AbstractProgressiveService.java:157-159 new DatapointParcelable(fileName, ..., move, isComplete)')

e('AbstractProgressiveService.addFirstDatapoint', 'DatapointParcelable.<init>', 'CALL',
  'addFirstDatapoint creates DatapointParcelable with 4 parameters (desc="(Ljava/lang/String;IJZ)V")',
  evidence='SRC AbstractProgressiveService.java:178 new DatapointParcelable(name, amountOfFiles, totalBytes, move)')

# DatapointParcelable$1 is the CREATOR field implementation
e('DatapointParcelable.<clinit>', 'DatapointParcelable$1.<init>', 'CALL',
  'CREATOR field initialization creates the anonymous Creator instance',
  evidence='SRC DatapointParcelable.java:126-138 CREATOR = new Creator<DatapointParcelable>()')

# DbViewerFragment methods
# DbViewerFragment is instantiated in DatabaseViewerActivity
e('DatabaseViewerActivity.onOptionsItemSelected', 'DbViewerFragment.<init>', 'CALL',
  'DatabaseViewerActivity listener creates DbViewerFragment for each table',
  evidence='SRC DatabaseViewerActivity.java:135 new DbViewerFragment()')

e('DbViewerFragment.<init>', 'DbViewerFragment.onCreateView', 'LIFECYCLE',
  'Fragment lifecycle calls onCreateView after instantiation',
  evidence='SRC DbViewerFragment.java:33-35 onCreateView inflates layout and initializes views')

e('DbViewerFragment.onCreateView', 'DbViewerFragment.onActivityCreated', 'LIFECYCLE',
  'Fragment lifecycle calls onActivityCreated after onCreateView',
  evidence='SRC DbViewerFragment.java:54-57 onActivityCreated sets theme colors')

e('DbViewerFragment.onActivityCreated', 'DbViewerFragment.onDetach', 'LIFECYCLE',
  'Fragment lifecycle calls onDetach when fragment is destroyed',
  evidence='SRC DbViewerFragment.java:69-73 onDetach closes cursors')

# DecryptService methods
# DecryptService is started via Intent from EncryptDecryptUtils
e('EncryptDecryptUtils.decryptFile', 'DecryptService.<init>', 'INTENT',
  'Framework instantiates DecryptService when started via Intent',
  evidence='SRC EncryptDecryptUtils.java:67 new Intent(main.getContext(), DecryptService.class)')

e('EncryptDecryptUtils.decryptFile', 'DecryptService.onStartCommand', 'INTENT',
  'decryptFile starts DecryptService with Intent',
  evidence='SRC EncryptDecryptUtils.java:67 new Intent(main.getContext(), DecryptService.class)')

e('DecryptService.onStartCommand', 'DecryptService.onCreate', 'LIFECYCLE',
  'Service lifecycle calls onCreate before onStartCommand',
  evidence='SRC DecryptService.java:64-68 onCreate registers broadcast receiver')

e('DecryptService.onCreate', 'DecryptService$1.<init>', 'CALL',
  'onCreate references cancelReceiver field which is initialized',
  evidence='SRC DecryptService.java:214-221 cancelReceiver = new BroadcastReceiver()')

e('DecryptService.onStartCommand', 'DecryptService$BackgroundTask.<init>', 'ASYNC',
  'onStartCommand creates and executes BackgroundTask',
  evidence='SRC DecryptService.java:118 new DecryptService.BackgroundTask().execute()')

e('DecryptService.onStartCommand', 'DecryptService.getNotificationManager', 'CALL',
  'Service implementation calls getNotificationManager',
  evidence='SRC DecryptService.java:186-188 getNotificationManager returns notificationManager')

e('DecryptService.onStartCommand', 'DecryptService.getNotificationBuilder', 'CALL',
  'Service implementation calls getNotificationBuilder',
  evidence='SRC DecryptService.java:191-193 getNotificationBuilder returns notificationBuilder')

e('DecryptService.onStartCommand', 'DecryptService.getNotificationId', 'CALL',
  'Service implementation calls getNotificationId',
  evidence='SRC DecryptService.java:196-198 getNotificationId returns DECRYPT_ID')

e('DecryptService.onStartCommand', 'DecryptService.getTitle', 'CALL',
  'Service implementation calls getTitle for notification',
  evidence='SRC DecryptService.java:202-204 getTitle returns R.string.crypt_decrypting')

e('DecryptService.onStartCommand', 'DecryptService.getNotificationCustomViewSmall', 'CALL',
  'Service implementation calls getNotificationCustomViewSmall',
  evidence='SRC DecryptService.java:207-209 getNotificationCustomViewSmall returns customSmallContentViews')

e('DecryptService.onStartCommand', 'DecryptService.getNotificationCustomViewBig', 'CALL',
  'Service implementation calls getNotificationCustomViewBig',
  evidence='SRC DecryptService.java:212-214 getNotificationCustomViewBig returns customBigContentViews')

e('DecryptService.onStartCommand', 'DecryptService.getDataPackages', 'CALL',
  'Service implementation calls getDataPackages',
  evidence='SRC DecryptService.java:217-219 getDataPackages returns dataPackages list')

e('DecryptService.onStartCommand', 'DecryptService.getProgressHandler', 'CALL',
  'Service implementation calls getProgressHandler',
  evidence='SRC DecryptService.java:222-224 getProgressHandler returns progressHandler')

e('DecryptService.onStartCommand', 'DecryptService.isDecryptService', 'CALL',
  'Service implementation calls isDecryptService',
  evidence='SRC DecryptService.java:227-229 isDecryptService returns true')

e('ProcessViewerFragment.onResume', 'DecryptService.onBind', 'SYSTEM',
  'ProcessViewerFragment binds to DecryptService',
  evidence='SRC ProcessViewerFragment.java:170 bindService with DecryptService.class intent')

e('DecryptService.onStartCommand', 'DecryptService.setProgressListener', 'CALL',
  'ProcessViewerFragment sets progress listener on bound service',
  evidence='SRC DecryptService.java:233-235 setProgressListener stores listener')

e('DecryptService.onStartCommand', 'DecryptService.getProgressListener', 'CALL',
  'Service calls getProgressListener when progress updates',
  evidence='SRC DecryptService.java:231-233 getProgressListener returns progressListener')

e('DecryptService.onCreate', 'DecryptService.onDestroy', 'LIFECYCLE',
  'Service lifecycle calls onDestroy when service stops',
  evidence='SRC DecryptService.java:238-241 onDestroy unregisters receiver')

e('DecryptService$1.<init>', 'DecryptService$1.onReceive', 'FRAMEWORK',
  'Framework calls onReceive when cancel broadcast sent',
  evidence='SRC DecryptService.java:217-220 onReceive handles TAG_BROADCAST_CRYPT_CANCEL')

# Decompressor methods
# Decompressor is abstract base class; concrete implementations are called
e('CompressedHelper.getCompressorInstance', 'Decompressor.setFilePath', 'CALL',
  'getCompressorInstance calls setFilePath after creating decompressor',
  evidence='SRC CompressedHelper.java:131 decompressor.setFilePath(file.getPath())')

e('MainActivityHelper.extractFile', 'Decompressor.decompress', 'CALL',
  'extractFile calls decompress with single path parameter',
  evidence='SRC MainActivityHelper.java:529 decompressor.decompress(file.getPath())')

e('CompressedExplorerFragment.extractFiles', 'Decompressor.decompress', 'CALL',
  'extractFiles calls decompress with directory array parameter',
  evidence='SRC CompressedExplorerFragment.java:329 decompressor.decompress(compressedFile.getPath(), dirs)')

e('Decompressor.decompress', 'Decompressor.realRelativeDirectory', 'CALL',
  'decompress calls realRelativeDirectory for each subdirectory',
  evidence='SRC Decompressor.java:58-60 realRelativeDirectory(subDirectories[i])')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_B020 = {
    'DataUtils$DataUtilsHolder.<init>': ('no_trigger_in_app', 'Private constructor never called; singleton uses static INSTANCE field only', 'SRC DataUtils.java:78-80 private static class DataUtilsHolder with static INSTANCE field', 'SOURCE'),
    'DatapointParcelable.<init>(Landroid/os/Parcel;)V': ('no_trigger_in_app', 'Parcel constructor only called from createFromParcel which is never called', 'SRC DatapointParcelable.java:120-129 constructor reads from Parcel; grep shows no getParcelable for DatapointParcelable', 'SOURCE'),
    'DatapointParcelable.describeContents': ('no_trigger_in_app', 'Parcelable method never called; DatapointParcelable stored in lists not parceled through Intents', 'SRC DatapointParcelable.java:142-144 describeContents returns 0; grep shows no putParcelable/getParcelable for DatapointParcelable', 'SOURCE'),
    'DatapointParcelable.writeToParcel': ('no_trigger_in_app', 'Parcelable method never called; DatapointParcelable stored in lists not parceled through Intents', 'SRC DatapointParcelable.java:147-155 writeToParcel writes fields to Parcel; grep shows no putParcelable for DatapointParcelable', 'SOURCE'),
    'DatapointParcelable$1.createFromParcel': ('no_trigger_in_app', 'CREATOR method never called; DatapointParcelable never unparceled from Intents', 'SRC DatapointParcelable.java:129-131 createFromParcel creates from Parcel; grep shows no getParcelable for DatapointParcelable', 'SOURCE'),
    'DatapointParcelable$1.newArray': ('no_trigger_in_app', 'CREATOR method never called; DatapointParcelable arrays never unparceled', 'SRC DatapointParcelable.java:134-136 newArray creates array; grep shows no array unparceling for DatapointParcelable', 'SOURCE'),
    'Decompressor.<init>': ('no_trigger_in_app', 'Abstract class constructor called only by subclass constructors, which are already in the graph', 'SRC Decompressor.java:23-25 protected constructor takes Context; subclasses call super() which is covered by subclass edges', 'SOURCE'),
}
