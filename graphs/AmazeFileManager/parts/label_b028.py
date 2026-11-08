# ---- Helper batch_028 label part (2026-10-27)
# FileUtils$1, FileUtils$2, FileUtils$3, FileUtils$4, FileUtils$5, FingerprintHandler, Folder

# FileUtils$1: AnimatorListenerAdapter for crossfade
# Constructor called from FileUtils.crossfade, callback invoked by framework
e('FileUtils.crossfade', 'FileUtils$1.<init>', 'CALL', 'creates animator listener for pathbar fade out',
  evidence='SRC files/FileUtils.java:294')
e('FileUtils$1.<init>', 'FileUtils$1.onAnimationEnd', 'FRAMEWORK', 'animation framework calls when fade animation completes',
  evidence='SRC files/FileUtils.java:296 defines AnimatorListenerAdapter.onAnimationEnd callback')

# FileUtils$2: AnimatorListenerAdapter for crossfadeInverse
# Constructor called from FileUtils.crossfadeInverse, callback invoked by framework
e('FileUtils.crossfadeInverse', 'FileUtils$2.<init>', 'CALL', 'creates animator listener for buttons fade out',
  evidence='SRC files/FileUtils.java:321')
e('FileUtils$2.<init>', 'FileUtils$2.onAnimationEnd', 'FRAMEWORK', 'animation framework calls when inverse fade animation completes',
  evidence='SRC files/FileUtils.java:323 defines AnimatorListenerAdapter.onAnimationEnd callback')

# FileUtils$3: AsyncTask for cloud file sharing
# Constructor called from FileUtils.shareCloudFile, methods invoked by AsyncTask framework
e('FileUtils.shareCloudFile', 'FileUtils$3.<init>', 'CALL', 'creates async task to get cloud share link',
  evidence='SRC files/FileUtils.java:333')
e('FileUtils$3.<init>', 'FileUtils$3.doInBackground', 'ASYNC', 'AsyncTask framework executes on background thread',
  evidence='SRC files/FileUtils.java:336-340 defines AsyncTask.doInBackground')
e('FileUtils$3.<init>', 'FileUtils$3.onPostExecute', 'ASYNC', 'AsyncTask framework calls on UI thread after background completes',
  evidence='SRC files/FileUtils.java:343-348 defines AsyncTask.onPostExecute')

# FileUtils$4: CountDownTimer for audio file easter egg
# Constructor called from FileUtils.openFile, callbacks invoked by CountDownTimer framework
e('FileUtils.openFile', 'FileUtils$4.<init>', 'CALL', 'creates countdown timer for studio easter egg',
  evidence='SRC files/FileUtils.java:768')
e('FileUtils$4.<init>', 'FileUtils$4.onTick', 'FRAMEWORK', 'CountDownTimer framework calls every second',
  evidence='SRC files/FileUtils.java:770-776 defines CountDownTimer.onTick')
e('FileUtils$4.<init>', 'FileUtils$4.onFinish', 'FRAMEWORK', 'CountDownTimer framework calls when timer finishes',
  evidence='SRC files/FileUtils.java:779-785 defines CountDownTimer.onFinish')

# FileUtils$5: Operations.ErrorCallBack interface implementation
# Constructor called from FileUtils.checkForPath, methods called back from Operations.mkdir
e('FileUtils.checkForPath', 'FileUtils$5.<init>', 'CALL', 'creates error callback for mkdir operation',
  evidence='SRC files/FileUtils.java:1027')
e('Operations.mkdir', 'FileUtils$5.exists', 'CALL', 'callback when file already exists',
  evidence='SRC filesystem/Operations.java:96,117,172 calls errorCallBack.exists(file); SRC files/FileUtils.java:1029-1031 defines empty callback')
e('Operations.mkdir', 'FileUtils$5.launchSAF', 'CALL', 'callback to launch SAF for SD card access (single HybridFile param)',
  evidence='SRC filesystem/Operations.java:165 calls errorCallBack.launchSAF(file); SRC files/FileUtils.java:1033-1035 defines empty callback')
e('Operations.mkdir', 'FileUtils$5.done', 'CALL', 'callback when mkdir operation completes',
  evidence='SRC filesystem/Operations.java:108,111,122,123,129,132,138,141,147,150,156,159,179 calls errorCallBack.done; SRC files/FileUtils.java:1042-1044 defines empty callback')
e('Operations.mkdir', 'FileUtils$5.invalidName', 'CALL', 'callback when filename is invalid',
  evidence='SRC filesystem/Operations.java:91 calls errorCallBack.invalidName(file); SRC files/FileUtils.java:1046-1048 defines empty callback')

# FingerprintHandler: Fingerprint authentication for file decryption (API 23+)
# Instantiated from GeneralDialogCreation.showDecryptFingerprintDialog (guarded by API >= M check)
e('GeneralDialogCreation.showDecryptFingerprintDialog', 'FingerprintHandler.<init>', 'CALL', 'creates fingerprint auth handler',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:835',
  guard='Build.VERSION.SDK_INT >= Build.VERSION_CODES.M at utils/files/EncryptDecryptUtils.java:107')
e('FingerprintHandler.<init>', 'FingerprintHandler.authenticate', 'CALL', 'initiates fingerprint authentication',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:836; SRC utils/FingerprintHandler.java:38-46')
e('FingerprintHandler.authenticate', 'FingerprintHandler.onAuthenticationError', 'FRAMEWORK', 'FingerprintManager callback on authentication error',
  evidence='SRC utils/FingerprintHandler.java:39,46 registers this as AuthenticationCallback; SRC utils/FingerprintHandler.java:51-53 defines callback')
e('FingerprintHandler.authenticate', 'FingerprintHandler.onAuthenticationHelp', 'FRAMEWORK', 'FingerprintManager callback on authentication help message',
  evidence='SRC utils/FingerprintHandler.java:39,46 registers this as AuthenticationCallback; SRC utils/FingerprintHandler.java:57-59 defines callback')
e('FingerprintHandler.authenticate', 'FingerprintHandler.onAuthenticationFailed', 'FRAMEWORK', 'FingerprintManager callback on authentication failure',
  evidence='SRC utils/FingerprintHandler.java:39,46 registers this as AuthenticationCallback; SRC utils/FingerprintHandler.java:63-66 defines callback')
e('FingerprintHandler.authenticate', 'FingerprintHandler.onAuthenticationSucceeded', 'FRAMEWORK', 'FingerprintManager callback on authentication success',
  evidence='SRC utils/FingerprintHandler.java:39,46 registers this as AuthenticationCallback; SRC utils/FingerprintHandler.java:70-74 defines callback')

# Folder: 7z archive structure (Apache Commons Compress library)
# Instantiated in SevenZFile.readHeaders
e('SevenZFile.readHeaders', 'Folder.<init>', 'CALL', 'creates Folder for 7z archive structure',
  evidence='SRC sevenz/SevenZFile.java:510,635')
e('SevenZFile.readStreamsInfo', 'Folder.getOrderedCoders', 'CALL', 'gets coders in stream processing order',
  evidence='SRC sevenz/SevenZFile.java:431')
e('SevenZFile.buildDecodingStream', 'Folder.getOrderedCoders', 'CALL', 'gets coders to build decoding stream',
  evidence='SRC sevenz/SevenZFile.java:1025')
e('Folder.getOrderedCoders', 'Folder.findBindPairForOutStream', 'CALL', 'finds bind pair for output stream in coder chain',
  evidence='SRC sevenz/Folder.java:59')
e('SevenZFile.readHeaders', 'Folder.findBindPairForInStream', 'CALL', 'finds bind pair for input stream',
  evidence='SRC sevenz/SevenZFile.java:695')
e('Folder.getUnpackSize', 'Folder.findBindPairForOutStream', 'CALL', 'checks if output stream is final',
  evidence='SRC sevenz/Folder.java:88')
e('SevenZFile.readStreamsInfo', 'Folder.getUnpackSize', 'CALL', 'gets total unpack size for folder',
  evidence='SRC sevenz/SevenZFile.java:440,442,586')
e('SevenZFile.buildDecodingStream', 'Folder.getUnpackSize', 'CALL', 'gets unpack size for stream setup',
  evidence='SRC sevenz/SevenZFile.java:1038')
e('SevenZFile.readStreamsInfo', 'Folder.getUnpackSizeForCoder', 'CALL', 'gets unpack size for specific coder',
  evidence='SRC sevenz/SevenZFile.java:436')
e('SevenZFile.buildDecodingStream', 'Folder.getUnpackSizeForCoder', 'CALL', 'gets coder unpack size for decoding',
  evidence='SRC sevenz/SevenZFile.java:1031')

# UNREACHABLE methods
# FileUtils$5.launchSAF(HybridFile,HybridFile) - two-parameter overload not called by Operations.mkdir
UNREACHABLE['FileUtils$5.launchSAF(HybridFile,HybridFile)'] = ('branch_never_taken', 'FileUtils$5 instance passed to Operations.mkdir at files/FileUtils.java:1027; mkdir only calls single-parameter launchSAF(file) at Operations.java:165, not two-parameter launchSAF(file,file1) which is only used by Operations.rename at Operations.java:441 with different callback instances', 'SRC files/FileUtils.java:1037-1039 defines two-param override; SRC filesystem/Operations.java:1027 passes to mkdir; SRC filesystem/Operations.java:165 mkdir calls single-param; SRC filesystem/Operations.java:441 rename calls two-param', 'SOURCE')

# Folder.toString() - debugging method not called
UNREACHABLE['Folder.toString'] = ('no_trigger_in_app', 'toString() is debugging/diagnostic method, no calls found in codebase', 'SRC sevenz/Folder.java:100-106 defines toString(); grep of commons_compress_7z shows no calls to folder.toString() or string concatenation with Folder', 'INFERRED')
