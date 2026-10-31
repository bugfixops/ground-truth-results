# Repair batch 24: 11 methods
# Generated: 2024-10-28 21:39

# ServiceWatcherUtil$2.run
e('ServiceWatcherUtil.postWaiting', 'ServiceWatcherUtil$2.<init>', 'CALL',
  'postWaiting creates anonymous Runnable for waiting watcher thread',
  evidence='SRC ServiceWatcherUtil.java:201-223')
e('ServiceWatcherUtil$2.<init>', 'ServiceWatcherUtil$2.run', 'FRAMEWORK',
  'Handler.postDelayed calls Runnable.run on the handler thread',
  evidence='SRC ServiceWatcherUtil.java:224; INFERRED android.os.Handler posts Runnable to handler thread')

# StreamServer.lambda$new$0
e('StreamServer.<init>(int,File)', 'StreamServer.lambda$new$0', 'ASYNC',
  'Constructor creates server thread with lambda that accepts socket connections',
  evidence='SRC StreamServer.java:255-266')
e('Thread.run', 'StreamServer.lambda$new$0', 'CALL',
  'Thread.run executes lambda body',
  evidence='INFERRED Thread.run calls lambda')

# SmbUtil.<init>
UNREACHABLE['SmbUtil.<init>'] = ('no_trigger_in_app',
  'Utility class with only static methods; constructor never instantiated in app source',
  'SRC SmbUtil.java:17 (class with only static methods getSmbDecryptedPath and getSmbEncryptedPath); GREP no "new SmbUtil" in app source',
  'SOURCE')

# PackageReceiver.onReceive
e('AppListLoader.onStartLoading', 'PackageReceiver.<init>(AppListLoader)', 'CALL',
  'AppListLoader creates PackageReceiver and registers it for package broadcasts',
  evidence='SRC AppListLoader.java:120')
e('PackageReceiver.<init>(AppListLoader)', 'PackageReceiver.onReceive', 'FRAMEWORK',
  'BroadcastReceiver receives ACTION_PACKAGE_ADDED/REMOVED/CHANGED and ACTION_EXTERNAL_APPLICATIONS_AVAILABLE/UNAVAILABLE',
  evidence='SRC PackageReceiver.java:20-35; INFERRED ActivityThread dispatches broadcasts to registered receivers')

# CloudStreamServer.<init>(File)
UNREACHABLE['CloudStreamServer.<init>(File)'] = ('no_trigger_in_app',
  'Constructor overload not used; CloudStreamer subclass calls super(port, new File(".")) which uses the (int,File) constructor',
  'SRC CloudStreamer.java:31 calls super(port, new File(".")); CloudStreamServer.java:195-226 is (int,File) constructor, CloudStreamServer.java:230-247 is (File) constructor; GREP no callers of single-parameter constructor',
  'SOURCE')

# CloudUtil$2.<init> - this is the SFtpClientTemplate in getThumbnailInputStreamForCloud, not the Thread from launchCloud
# The existing graph_def.py line 1820 incorrectly maps CloudUtil$2 to the launchCloud Thread
# Correct mapping: CloudUtil$2 is the anonymous SFtpClientTemplate at CloudUtil.java:265
e('CloudUtil.getThumbnailInputStreamForCloud', 'CloudUtil$2.<init>', 'CALL',
  'getThumbnailInputStreamForCloud creates anonymous SFtpClientTemplate for SFTP mode',
  evidence='SRC CloudUtil.java:265-282')
e('SFtpClientTemplate.execute', 'CloudUtil$2.execute', 'CALL',
  'SshClientUtils.execute calls template execute method',
  evidence='INFERRED SshClientUtils.execute pattern')

# CloudUtil$2$1.close - already has edge, may need lambda init edge
e('CloudUtil.getThumbnailInputStreamForCloud', 'CloudUtil$2$1.<init>', 'CALL',
  'getThumbnailInputStreamForCloud creates anonymous RemoteFileInputStream subclass with overridden close method for SFTP mode',
  evidence='SRC CloudUtil.java:268-281')

# EncryptDecryptUtils.<init>
UNREACHABLE['EncryptDecryptUtils.<init>'] = ('no_trigger_in_app',
  'Utility class with only static methods; constructor never instantiated in app source',
  'SRC EncryptDecryptUtils.java:34 (class with only static methods startEncryption, decryptFile, findEncryptedEntry); GREP shows only "new EncryptDecryptUtils.EncryptButtonCallbackInterface()" in ItemPopupMenu.java (interface implementation, not class instantiation)',
  'SOURCE')

# CloudIconModelFactory.build - needs incoming edge to show how Glide framework calls it
e('AmazeFileManagerModule.registerComponents', 'CloudIconModelFactory.<init>(Context)', 'CALL',
  'Glide module registration creates CloudIconModelFactory',
  evidence='SRC AmazeFileManagerModule.java:22')
e('Glide.load', 'CloudIconModelFactory.build', 'FRAMEWORK',
  'Glide framework calls registered ModelLoaderFactory.build to create loader when loading images',
  evidence='INFERRED com.bumptech.glide.Glide (generated code) calls registered factories')

# UtilitiesProvider.getThemeManager - need to add route from AppConfig
e('AppConfig.onCreate', 'UtilitiesProvider.<init>(Context)', 'CALL',
  'AppConfig creates UtilitiesProvider singleton',
  evidence='SRC AppConfig.java:76')
e('PrefFrag.showThemeDialog', 'UtilitiesProvider.getThemeManager', 'CALL',
  'PrefFrag calls getThemeManager to access AppThemeManager',
  evidence='SRC PrefFrag.java:179 (utilsProvider.getThemeManager().setAppTheme(...))')

# AppThemeManager.setAppTheme - checking line 179 PrefFrag
e('PrefFrag.showThemeDialog', 'AppThemeManager.setAppTheme', 'CALL',
  'PrefFrag theme dialog onClick listener calls setAppTheme when user changes theme',
  evidence='SRC PrefFrag.java:179 (utilsProvider.getThemeManager().setAppTheme(AppTheme.getTheme(which)))')
