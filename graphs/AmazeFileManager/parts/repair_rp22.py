# Repair batch 22 for AmazeFileManager
# Methods from graphs/AmazeFileManager/scratch/repair_batches/rp_22.txt

# ==== UNREACHABLE methods ====

UNREACHABLE['InterestingConfigChange.<init>'] = (
    'no_trigger_in_app',
    'InterestingConfigChange is a utility class with only static methods (isConfigChanged, recycle). No instance is ever created.',
    'SRC utils/InterestingConfigChange.java:17-41',
    'SOURCE'
)

UNREACHABLE['PreferenceUtils.<init>'] = (
    'no_trigger_in_app',
    'PreferenceUtils is a utility class with only static methods (getStatusColor). No instance is ever created.',
    'SRC utils/PreferenceUtils.java:9-33',
    'SOURCE'
)

UNREACHABLE['TinyDB.<init>'] = (
    'no_trigger_in_app',
    'TinyDB is a utility class with only static methods (putBooleanArray, getBooleanArray). No instance is ever created.',
    'SRC utils/TinyDB.java:27-67',
    'SOURCE'
)

UNREACHABLE['DummyFileGenerator.<init>'] = (
    'no_trigger_in_app',
    'DummyFileGenerator is a test utility class annotated @RestrictTo(RestrictTo.Scope.TESTS). Used only in test code.',
    'SRC utils/test/DummyFileGenerator.java:48-85',
    'SOURCE'
)

UNREACHABLE['DummyFileGenerator.createFile(File,int)'] = (
    'no_trigger_in_app',
    'DummyFileGenerator.createFile is a test utility method annotated @RestrictTo(RestrictTo.Scope.TESTS). Used only in test code.',
    'SRC utils/test/DummyFileGenerator.java:53-85',
    'SOURCE'
)

UNREACHABLE['DonationViewHolder.<init>(View)'] = (
    'no_trigger_in_app',
    'DonationViewHolder is a RecyclerView.ViewHolder subclass but is never instantiated by any adapter.',
    'SRC adapters/holders/DonationViewHolder.java:10-21',
    'SOURCE'
)

# ==== REACHABLE methods (new routes) ====

e('MainActivity.initialisePreferences', 'PreferenceUtils.getStatusColor(String)', 'CALL',
  'MainActivity calls PreferenceUtils.getStatusColor to darken primary color for status bar',
  evidence='SRC activities/MainActivity.java:1415')

e('DatabaseViewerActivity.onCreate', 'PreferenceUtils.getStatusColor(String)', 'CALL',
  'DatabaseViewerActivity calls PreferenceUtils.getStatusColor for status bar color',
  evidence='SRC activities/DatabaseViewerActivity.java:122')

e('PreferencesActivity.onCreate', 'PreferenceUtils.getStatusColor(String)', 'CALL',
  'PreferencesActivity calls PreferenceUtils.getStatusColor for tab status color',
  evidence='SRC activities/PreferencesActivity.java:216')

e('TextEditorActivity.onCreate', 'PreferenceUtils.getStatusColor(String)', 'CALL',
  'TextEditorActivity calls PreferenceUtils.getStatusColor for status bar color',
  evidence='SRC activities/TextEditorActivity.java:182')

e('QuickAccessPref.onPreferenceClick', 'TinyDB.putBooleanArray(SharedPreferences,String,Boolean[])', 'CALL',
  'QuickAccessPref calls TinyDB.putBooleanArray to save preference array',
  evidence='SRC fragments/preference_fragments/QuickAccessPref.java:60')

e('CloudStreamSource.open', 'CloudStreamSource.read()', 'CALL',
  'CloudStreamSource.read() reads single byte from underlying inputStream',
  evidence='SRC cloud/CloudStreamSource.java:61-65')

e('CloudStreamSource.open', 'CloudStreamSource.read(byte[],int,int)', 'CALL',
  'CloudStreamSource.read(byte[],int,int) reads bytes into buffer from underlying inputStream',
  evidence='SRC cloud/CloudStreamSource.java:68-72')

e('StreamServer$HTTPSession.sendResponse', 'CloudStreamSource.read(byte[],int,int)', 'CALL',
  'StreamServer reads from CloudStreamSource stream when sending HTTP response data',
  evidence='INFERRED StreamServer.java sendResponse reads from StreamSource; NanoHTTPD library source not fully read')

e('MoveFiles.onPostExecute(Boolean)', 'MoveFiles.lambda$onPostExecute$0', 'ASYNC',
  'MoveFiles.onPostExecute passes lambda to AppConfig.runInBackground to update encrypted entries',
  evidence='SRC asynchronous/asynctasks/MoveFiles.java:179-195')

e('AppConfig.runInBackground', 'MoveFiles.lambda$onPostExecute$0', 'ASYNC',
  'AppConfig.runInBackground executes the lambda on background thread',
  evidence='INFERRED executor framework dispatches Runnable lambda body')

e('SevenZipHelperTask.onProgressUpdate(IOException[])', 'SevenZipHelperTask.lambda$onProgressUpdate$0(MaterialDialog,DialogAction)', 'CALL',
  'onProgressUpdate creates password dialog with lambda callback for positive button',
  evidence='SRC asynchronous/asynctasks/compress/SevenZipHelperTask.java:105-113')

e('MaterialDialog', 'SevenZipHelperTask.lambda$onProgressUpdate$0(MaterialDialog,DialogAction)', 'GUI',
  'MaterialDialog framework calls lambda when positive button clicked',
  evidence='INFERRED MaterialDialog library dispatches onClick callback')

# Already-REACHABLE methods (no new routes):
# InterestingConfigChange.recycle (graph_def.py:11004)
# CloudStreamer.isStreamMedia (graph_def.py:11645)
# CloudStreamer.setStreamSrc (graph_def.py:1796,5535)
# CloudIconModelLoader.buildLoadData (graph_def.py:1846,2120,5362,5401,7121,11596,11600)
# CloudIconModelLoader.handles (graph_def.py:7142)
# CompressedObjectParcelable.writeToParcel (graph_def.py:7538)
# RecyclerPreloadModelProvider.getPreloadItems (graph_def.py:402)
# CopyService.setProgressListener (graph_def.py:11745)
# DecryptService.onBind (graph_def.py:2932)
