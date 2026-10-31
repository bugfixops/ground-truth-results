# ---- Helper batch_043 label part (2026-10-27)

# LoadFolderSpaceDataTask edges
e('GeneralDialogCreation.showPropertiesDialog', 'LoadFolderSpaceDataTask.<init>', 'EXPLICIT',
  'Constructor instantiated to load folder space data for properties dialog',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:516')

e('LoadFolderSpaceDataTask.<init>', 'LoadFolderSpaceDataTask.doInBackground', 'LIFECYCLE',
  'AsyncTask.execute triggers doInBackground on background thread',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:517 shows executeOnExecutor call; INFERRED framework lifecycle')

e('LoadFolderSpaceDataTask.doInBackground', 'LoadFolderSpaceDataTask.createEntriesFromArray', 'CALL',
  'doInBackground calls createEntriesFromArray to build pie chart entries',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:61')

e('LoadFolderSpaceDataTask.<init>', 'LoadFolderSpaceDataTask.onPostExecute', 'LIFECYCLE',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:77; INFERRED framework lifecycle')

e('LoadFolderSpaceDataTask.onPostExecute', 'LoadFolderSpaceDataTask.updateChart', 'CALL',
  'onPostExecute calls updateChart with final data',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:91')

e('LoadFolderSpaceDataTask.<init>', 'LoadFolderSpaceDataTask.onProgressUpdate', 'LIFECYCLE',
  'AsyncTask framework calls onProgressUpdate when publishProgress is called',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:67; INFERRED framework lifecycle')

e('LoadFolderSpaceDataTask.onProgressUpdate', 'LoadFolderSpaceDataTask.createEntriesFromArray', 'CALL',
  'onProgressUpdate calls createEntriesFromArray for intermediate updates',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:74')

e('LoadFolderSpaceDataTask.onProgressUpdate', 'LoadFolderSpaceDataTask.updateChart', 'CALL',
  'onProgressUpdate calls updateChart for progress display',
  evidence='SRC asynchronous/asynctasks/LoadFolderSpaceDataTask.java:77')

# LruBitmapCache edges
e('AppConfig.getImageLoader', 'LruBitmapCache.<init>', 'EXPLICIT',
  'No-arg constructor instantiated as ImageLoader.ImageCache implementation',
  evidence='SRC utils/application/AppConfig.java:223')

e('LruBitmapCache.<init>', 'LruBitmapCache.<init>', 'CALL',
  'No-arg constructor delegates to parameterized constructor via this()',
  evidence='SRC utils/LruBitmapCache.java:22')

e('LruBitmapCache.<init>', 'LruBitmapCache.getDefaultCacheSize', 'CALL',
  'No-arg constructor calls getDefaultCacheSize for cache size',
  evidence='SRC utils/LruBitmapCache.java:22')

e('LruBitmapCache.<init>', 'LruBitmapCache.getBitmap', 'FRAMEWORK',
  'ImageLoader calls getBitmap to retrieve cached bitmaps',
  evidence='SRC utils/LruBitmapCache.java:31 implements ImageLoader.ImageCache; INFERRED framework call')

e('LruBitmapCache.<init>', 'LruBitmapCache.putBitmap', 'FRAMEWORK',
  'ImageLoader calls putBitmap to cache bitmaps',
  evidence='SRC utils/LruBitmapCache.java:36 implements ImageLoader.ImageCache; INFERRED framework call')

e('LruBitmapCache.<init>', 'LruBitmapCache.sizeOf', 'FRAMEWORK',
  'LruCache framework calls sizeOf to calculate entry sizes',
  evidence='SRC utils/LruBitmapCache.java:40 overrides LruCache.sizeOf; INFERRED framework call')

# LzmaDecompressor edges
e('CompressedHelper.getCompressorInstance', 'LzmaDecompressor.<init>', 'EXPLICIT',
  'Constructor instantiated for .tar.lzma file types',
  evidence='SRC filesystem/compressed/CompressedHelper.java:124')

e('LzmaDecompressor.<init>', 'LzmaDecompressor.changePath', 'FRAMEWORK',
  'Parent Decompressor class calls changePath to navigate archive',
  evidence='SRC filesystem/compressed/showcontents/helpers/LzmaDecompressor.java:40; INFERRED framework call from Decompressor')

e('LzmaDecompressor.changePath', 'LzmaHelperTask.<init>', 'EXPLICIT',
  'changePath instantiates LzmaHelperTask for async archive processing',
  evidence='SRC filesystem/compressed/showcontents/helpers/LzmaDecompressor.java:43')

e('LzmaHelperTask.<init>', 'LzmaHelperTask.addElements', 'FRAMEWORK',
  'CompressedHelperTask framework calls addElements to populate archive entries',
  evidence='SRC asynchronous/asynctasks/compress/LzmaHelperTask.java:52; INFERRED framework call from CompressedHelperTask')

# LzmaExtractor edges
e('CompressedHelper.getExtractorInstance', 'LzmaExtractor.<init>', 'EXPLICIT',
  'Constructor instantiated for .tar.lzma file extraction',
  evidence='SRC filesystem/compressed/CompressedHelper.java:94')

e('LzmaExtractor.<init>', 'LzmaExtractor.extractWithFilter', 'FRAMEWORK',
  'Parent Extractor class calls extractWithFilter to extract archive',
  evidence='SRC filesystem/compressed/extractcontents/helpers/LzmaExtractor.java:48; INFERRED framework call from Extractor')

e('LzmaExtractor.extractWithFilter', 'LzmaExtractor.extractEntry', 'CALL',
  'extractWithFilter calls extractEntry for each archive entry',
  evidence='SRC filesystem/compressed/extractcontents/helpers/LzmaExtractor.java:74')

# UNREACHABLE methods from batch_043
UNREACHABLE['LZMADecoder.<init>'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.decode'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.encode'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.getDictionarySize'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.getOptions'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.getOptionsAsProperties'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.getOptionsFromCoder'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)

UNREACHABLE['LZMADecoder.numberOptionOrDefault'] = (
    'no_trigger_in_app',
    'Commons Compress sevenz library class not called by app; grep -rn "LZMADecoder" shows no matches in app source',
    'grep output: no matches',
    'INFERRED'
)
