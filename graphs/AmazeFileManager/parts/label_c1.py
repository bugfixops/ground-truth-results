# ---- Helper chunk_1 label part (2025-01-10)
# READ-ONLY labeling for AmazeFileManager chunk_1 classes
# Classes: AES256SHA256Decoder, AES256SHA256Decoder$1, AbstractProgressiveService,
#          AdvancedSearchPref, AmazeFileManagerModule, AnimUtils, ApkImageDataFetcher,
#          ApkImageModelLoader, ApkImageModelLoaderFactory, AppConfig, AppConfig$1,
#          AppConfig$CustomAsyncCallbacks, AppHolder
# Status: 54 methods COMPLETE (7 UNREACHABLE, 47 REACHABLE), 13 methods INCOMPLETE (AbstractProgressiveService)

# ===== REACHABLE EDGES =====

# AdvancedSearchPref
e('PreferencesActivity.selectItem', 'AdvancedSearchPref.<init>', 'DIRECT',
  'PreferencesActivity instantiates AdvancedSearchPref in selectItem',
  evidence='SRC PreferencesActivity.java:267')

e('AdvancedSearchPref.<init>', 'AdvancedSearchPref.onCreate', 'FRAMEWORK',
  'Framework calls onCreate on PreferenceFragment after instantiation',
  evidence='INFERRED framework lifecycle for PreferenceFragment')

# AmazeFileManagerModule (Glide)
e('GlideApp.<init>', 'AmazeFileManagerModule.<init>', 'FRAMEWORK',
  'Glide annotation processor generates code that instantiates @GlideModule classes',
  evidence='INFERRED Glide annotation processor for @GlideModule')

e('AmazeFileManagerModule.<init>', 'AmazeFileManagerModule.registerComponents', 'FRAMEWORK',
  'Glide framework calls registerComponents on AppGlideModule subclasses',
  evidence='INFERRED Glide framework lifecycle for AppGlideModule')

e('AmazeFileManagerModule.registerComponents', 'ApkImageModelLoaderFactory.<init>', 'DIRECT',
  'registerComponents creates ApkImageModelLoaderFactory',
  evidence='SRC AmazeFileManagerModule.java:22')

# AnimUtils
e('Indicator.<init>', 'AnimUtils.getFastOutSlowInInterpolator', 'DIRECT',
  'Indicator constructor calls AnimUtils.getFastOutSlowInInterpolator',
  evidence='SRC Indicator.java:153')

e('AppsAdapter.onBindViewHolder', 'AnimUtils.marqueeAfterDelay', 'DIRECT',
  'AppsAdapter.onBindViewHolder calls marqueeAfterDelay',
  evidence='SRC AppsAdapter.java:139')

e('AnimUtils.marqueeAfterDelay', 'AnimUtils.lambda$marqueeAfterDelay$0', 'DIRECT',
  'marqueeAfterDelay posts lambda to Handler',
  evidence='SRC AnimUtils.java:47-49')

# ApkImage Glide loaders
e('ApkImageModelLoaderFactory.build', 'ApkImageModelLoader.<init>', 'DIRECT',
  'Factory.build creates ApkImageModelLoader',
  evidence='SRC ApkImageModelLoaderFactory.java:23')

e('ApkImageModelLoaderFactory.<init>', 'ApkImageModelLoaderFactory.build', 'FRAMEWORK',
  'Glide calls build on ModelLoaderFactory',
  evidence='INFERRED Glide framework calls build on registered factories')

e('ApkImageModelLoaderFactory.<init>', 'ApkImageModelLoaderFactory.teardown', 'FRAMEWORK',
  'Glide calls teardown on ModelLoaderFactory during cleanup',
  evidence='INFERRED Glide framework lifecycle')

e('ApkImageModelLoader.<init>', 'ApkImageModelLoader.buildLoadData', 'FRAMEWORK',
  'Glide calls buildLoadData on ModelLoader to create LoadData',
  evidence='INFERRED Glide framework calls buildLoadData')

e('ApkImageModelLoader.<init>', 'ApkImageModelLoader.handles', 'FRAMEWORK',
  'Glide calls handles on ModelLoader to check if it can handle model',
  evidence='INFERRED Glide framework calls handles')

e('ApkImageModelLoader.buildLoadData', 'ApkImageDataFetcher.<init>', 'DIRECT',
  'buildLoadData creates ApkImageDataFetcher',
  evidence='SRC ApkImageModelLoader.java:27')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.loadData', 'FRAMEWORK',
  'Glide calls loadData on DataFetcher to fetch data',
  evidence='INFERRED Glide framework calls loadData')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.cleanup', 'FRAMEWORK',
  'Glide calls cleanup on DataFetcher after load completes',
  evidence='INFERRED Glide framework lifecycle')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.cancel', 'FRAMEWORK',
  'Glide calls cancel on DataFetcher if load cancelled',
  evidence='INFERRED Glide framework lifecycle')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.getDataClass', 'FRAMEWORK',
  'Glide calls getDataClass on DataFetcher to determine result type',
  evidence='INFERRED Glide framework calls getDataClass')

e('ApkImageDataFetcher.<init>', 'ApkImageDataFetcher.getDataSource', 'FRAMEWORK',
  'Glide calls getDataSource on DataFetcher to determine data source type',
  evidence='INFERRED Glide framework calls getDataSource')

# AppHolder
e('AppsAdapter.onCreateViewHolder', 'AppHolder.<init>', 'DIRECT',
  'AppsAdapter creates AppHolder in onCreateViewHolder',
  evidence='SRC AppsAdapter.java:114')

# AppConfig - Application class
e('Application.onCreate', 'AppConfig.<init>', 'FRAMEWORK',
  'Android framework instantiates Application subclass',
  evidence='INFERRED framework creates Application')

e('AppConfig.<init>', 'AppConfig.onCreate', 'FRAMEWORK',
  'Framework calls onCreate on Application after instantiation',
  evidence='INFERRED framework lifecycle for Application')

e('AppConfig.<init>', 'AppConfig.onTerminate', 'FRAMEWORK',
  'Framework calls onTerminate on Application during shutdown',
  evidence='INFERRED framework lifecycle for Application')

e('SftpConnectDialog.onCreateView', 'AppConfig.getInstance', 'DIRECT',
  'SftpConnectDialog calls getInstance to get AppConfig singleton',
  evidence='SRC SftpConnectDialog.java:97-98')

e('AppConfig.getInstance', 'AppConfig.getUtilsProvider', 'DIRECT',
  'Code calls getUtilsProvider after getInstance',
  evidence='SRC SftpConnectDialog.java:97')

e('AppConfig.getInstance', 'AppConfig.getUtilsHandler', 'DIRECT',
  'Code calls getUtilsHandler after getInstance',
  evidence='SRC SftpConnectDialog.java:98')

e('Drawer.<init>', 'AppConfig.getInstance', 'DIRECT',
  'Drawer constructor calls getInstance',
  evidence='SRC Drawer.java:156')

e('AppConfig.getInstance', 'AppConfig.getImageLoader', 'DIRECT',
  'Code calls getImageLoader after getInstance',
  evidence='SRC Drawer.java:156')

e('AppConfig.getInstance', 'AppConfig.getScreenUtils', 'DIRECT',
  'Code calls getScreenUtils after getInstance',
  evidence='SRC Drawer.java:243')

e('GeneralDialogCreation.showNameDialog', 'AppConfig.getInstance', 'DIRECT',
  'showNameDialog calls getInstance',
  evidence='SRC GeneralDialogCreation.java:889')

e('AppConfig.getInstance', 'AppConfig.getMainActivityContext', 'DIRECT',
  'Code calls getMainActivityContext after getInstance',
  evidence='SRC GeneralDialogCreation.java:889')

e('MainActivity.onCreate', 'AppConfig.setMainActivityContext', 'INFERRED',
  'MainActivity sets itself as main activity context',
  evidence='INFERRED MainActivity needs to register itself')

e('SftpConnectDialog.lambda$onCreateView$2', 'AppConfig.runInBackground', 'DIRECT',
  'SftpConnectDialog lambda calls runInBackground',
  evidence='SRC SftpConnectDialog.java:249')

e('UtilsHandler.addCommonBookmarks', 'AppConfig.runInBackground', 'DIRECT',
  'UtilsHandler calls runInBackground',
  evidence='SRC UtilsHandler.java:179')

e('LoadFilesListTask.onPostExecute', 'AppConfig.toast', 'DIRECT',
  'LoadFilesListTask calls toast(Context, int)',
  evidence='SRC LoadFilesListTask.java:189')

e('AppConfig.toast', 'AppConfig.runInApplicationThread', 'DIRECT',
  'toast calls runInApplicationThread to show on UI thread',
  evidence='SRC AppConfig.java:161, 183')

e('AppConfig.toast', 'AppConfig.lambda$toast$0', 'DIRECT',
  'toast(Context, int) creates lambda',
  evidence='SRC AppConfig.java:160-162')

e('AppConfig.toast', 'AppConfig.lambda$toast$1', 'DIRECT',
  'toast(Context, String) creates lambda',
  evidence='SRC AppConfig.java:182-184')

e('AppConfig.runInParallel', 'AppConfig$1.<init>', 'DIRECT',
  'runInParallel creates anonymous AsyncTask',
  evidence='SRC AppConfig.java:110-127')

e('AppConfig$1.<init>', 'AppConfig$1.onPreExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPreExecute',
  evidence='INFERRED AsyncTask lifecycle')

e('AppConfig$1.<init>', 'AppConfig$1.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED AsyncTask lifecycle')

e('AppConfig$1.<init>', 'AppConfig$1.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED AsyncTask lifecycle')

e('AppConfig$1.onPreExecute', 'AppConfig$CustomAsyncCallbacks.onPreExecute', 'DIRECT',
  'AsyncTask onPreExecute calls callbacks.onPreExecute',
  evidence='SRC AppConfig.java:115')

e('AppConfig$1.doInBackground', 'AppConfig$CustomAsyncCallbacks.doInBackground', 'DIRECT',
  'AsyncTask doInBackground calls callbacks.doInBackground',
  evidence='SRC AppConfig.java:119')

e('AppConfig$1.onPostExecute', 'AppConfig$CustomAsyncCallbacks.onPostExecute', 'DIRECT',
  'AsyncTask onPostExecute calls callbacks.onPostExecute',
  evidence='SRC AppConfig.java:125')

e('AppConfig.runInParallel', 'AppConfig$CustomAsyncCallbacks.<init>', 'INFERRED',
  'Caller must subclass CustomAsyncCallbacks to use runInParallel',
  evidence='INFERRED from API design; constructor called by subclass instantiation')

# Static initializer
e('AppConfig.<init>', 'AppConfig.<clinit>', 'FRAMEWORK',
  'JVM calls static initializer before first use of class',
  evidence='INFERRED JVM static initialization')

# ===== UNREACHABLE METHODS =====

UNREACHABLE_CHUNK_1 = {
    # AES256SHA256Decoder - Apache Commons Compress library class
    'AES256SHA256Decoder.<init>': (
        'framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'INFERRED'
    ),
    'AES256SHA256Decoder.decode': (
        'framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'INFERRED'
    ),
    'AES256SHA256Decoder$1.<init>': (
        'framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'INFERRED'
    ),
    'AES256SHA256Decoder$1.close': (
        'framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'INFERRED'
    ),
    'AES256SHA256Decoder$1.init': (
        'framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'INFERRED'
    ),
    'AES256SHA256Decoder$1.read': (
        'framework_never_calls',
        'Library class from org.apache.commons.compress.archivers.sevenz package; grep -rn "AES256SHA256Decoder" over app source shows no call sites; both read() overloads unreachable',
        'grep -rn "AES256SHA256Decoder" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java: no matches',
        'INFERRED'
    ),
    'AnimUtils.<init>': (
        'no_trigger_in_app',
        'Utility class with only static methods; constructor never explicitly called',
        'SRC AnimUtils.java:30 shows class declaration; no new AnimUtils() in app',
        'SOURCE'
    ),
}
