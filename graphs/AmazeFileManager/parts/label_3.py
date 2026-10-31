# ---- Helper 3 label part (2025-01-17)

# AmazeFileManagerModule - Glide annotation processor calls registerComponents
# This is a Glide @GlideModule annotated class

# CloudLoaderAsyncTask
e('MainActivity.onLoadFinished', 'CloudLoaderAsyncTask.<init>', 'CALL', 
  'MainActivity instantiates CloudLoaderAsyncTask in loader callback',
  evidence='SRC MainActivity.java:1922')
e('CloudLoaderAsyncTask.<init>', 'CloudLoaderAsyncTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground after execute()',
  evidence='INFERRED source not read')
e('CloudLoaderAsyncTask.doInBackground', 'CloudLoaderAsyncTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='INFERRED source not read')
e('CloudLoaderAsyncTask.doInBackground', 'CloudLoaderAsyncTask.onCancelled', 'FRAMEWORK',
  'AsyncTask framework calls onCancelled when cancel(true) is called',
  evidence='SRC CloudLoaderAsyncTask.java:52,56,61')

# AsyncTaskResult
# Generic container class - reachability depends on its usages

# CountItemsOrAndSizeTask
e('GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'CountItemsOrAndSizeTask.<init>', 'CALL',
  'Dialog creation instantiates CountItemsOrAndSizeTask',
  evidence='SRC GeneralDialogCreation.java:457')
e('CountItemsOrAndSizeTask.<init>', 'CountItemsOrAndSizeTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.getText', 'CALL',
  'doInBackground calls getText for formatting',
  evidence='SRC CountItemsOrAndSizeTask.java:42,54')
e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate',
  evidence='SRC CountItemsOrAndSizeTask.java:42')
e('CountItemsOrAndSizeTask.doInBackground', 'CountItemsOrAndSizeTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# DbViewerTask
e('DbViewerFragment.onCreateView', 'DbViewerTask.<init>', 'CALL',
  'DbViewerFragment instantiates DbViewerTask',
  evidence='SRC DbViewerFragment.java:47')
e('DbViewerTask.<init>', 'DbViewerTask.onPreExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPreExecute',
  evidence='INFERRED source not read')
e('DbViewerTask.<init>', 'DbViewerTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('DbViewerTask.doInBackground', 'DbViewerTask.getDbTableSchema', 'CALL',
  'doInBackground calls getDbTableSchema',
  evidence='SRC DbViewerTask.java:63')
e('DbViewerTask.doInBackground', 'DbViewerTask.getDbTableDetails', 'CALL',
  'doInBackground calls getDbTableDetails',
  evidence='SRC DbViewerTask.java:64')
e('DbViewerTask.doInBackground', 'DbViewerTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate',
  evidence='SRC DbViewerTask.java:137')
e('DbViewerTask.doInBackground', 'DbViewerTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')
e('DbViewerTask.doInBackground', 'DbViewerTask.onCancelled', 'FRAMEWORK',
  'isCancelled check can lead to onCancelled',
  evidence='SRC DbViewerTask.java:135,148')

# DeleteTask
e('CopyService.onStartCommand', 'DeleteTask.<init>(Context)', 'CALL',
  'CopyService instantiates DeleteTask',
  evidence='SRC CopyService.java:423')
e('MainActivityHelper.deleteFiles', 'DeleteTask.<init>(Context)', 'CALL',
  'MainActivityHelper instantiates DeleteTask',
  evidence='SRC MainActivityHelper.java:510,518')
e('CompressedExplorerFragment.onOptionsItemSelected', 'DeleteTask.<init>(Context,CompressedExplorerFragment)', 'CALL',
  'CompressedExplorerFragment instantiates DeleteTask with fragment',
  evidence='SRC CompressedExplorerFragment.java:362')
e('DeleteTask.<init>(Context)', 'DeleteTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('DeleteTask.doInBackground', 'DeleteTask.delete', 'CALL',
  'doInBackground calls delete for media database cleanup',
  evidence='SRC DeleteTask.java:140')
e('DeleteTask.doInBackground', 'DeleteTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress would trigger onProgressUpdate',
  evidence='INFERRED source not read')
e('DeleteTask.doInBackground', 'DeleteTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# GenerateHashesTask
e('GeneralDialogCreation.showPropertiesDialogWithoutPermissions', 'GenerateHashesTask.<init>', 'CALL',
  'Dialog creation instantiates GenerateHashesTask',
  evidence='SRC GeneralDialogCreation.java:461')
e('GenerateHashesTask.<init>', 'GenerateHashesTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('GenerateHashesTask.doInBackground', 'GenerateHashesTask.getMD5Checksum', 'CALL',
  'doInBackground calls getMD5Checksum',
  evidence='SRC GenerateHashesTask.java:80')
e('GenerateHashesTask.doInBackground', 'GenerateHashesTask.getSHA256Checksum', 'CALL',
  'doInBackground calls getSHA256Checksum',
  evidence='SRC GenerateHashesTask.java:81')
e('GenerateHashesTask.getMD5Checksum', 'GenerateHashesTask.createChecksum', 'CALL',
  'getMD5Checksum calls createChecksum',
  evidence='SRC GenerateHashesTask.java:113')
e('GenerateHashesTask.doInBackground', 'GenerateHashesTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# GenerateHashesTask$1 and $2 - anonymous inner classes created by lambda
e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask$1.<init>', 'CALL',
  'Lambda creates anonymous class for OnLongClickListener',
  evidence='SRC GenerateHashesTask.java:93')
e('GenerateHashesTask.onPostExecute', 'GenerateHashesTask$2.<init>', 'CALL',
  'Lambda creates anonymous class for OnLongClickListener',
  evidence='SRC GenerateHashesTask.java:98')

# LoadFilesListTask
e('MainFragment.loadlist', 'LoadFilesListTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground after instantiation',
  evidence='SRC MainFragment.java:1025')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.createListParcelables', 'CALL',
  'doInBackground calls createListParcelables',
  evidence='SRC LoadFilesListTask.java:228')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listImages', 'CALL',
  'Called when openmode is CUSTOM case 0',
  evidence='SRC LoadFilesListTask.java:139')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listVideos', 'CALL',
  'Called when openmode is CUSTOM case 1',
  evidence='SRC LoadFilesListTask.java:142')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listaudio', 'CALL',
  'Called when openmode is CUSTOM case 2',
  evidence='SRC LoadFilesListTask.java:145')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listDocs', 'CALL',
  'Called when openmode is CUSTOM case 3',
  evidence='SRC LoadFilesListTask.java:148')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listApks', 'CALL',
  'Called when openmode is CUSTOM case 4',
  evidence='SRC LoadFilesListTask.java:151')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listRecent', 'CALL',
  'Called when openmode is CUSTOM case 5',
  evidence='SRC LoadFilesListTask.java:154')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listRecentFiles', 'CALL',
  'Called when openmode is CUSTOM case 6',
  evidence='SRC LoadFilesListTask.java:157')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listOtg', 'CALL',
  'Called when openmode is OTG',
  evidence='SRC LoadFilesListTask.java:165')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.listCloud', 'CALL',
  'Called for cloud storage modes',
  evidence='SRC LoadFilesListTask.java:177')
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# AnimUtils
e('Indicator.<init>', 'AnimUtils.getFastOutSlowInInterpolator', 'CALL',
  'Indicator calls getFastOutSlowInInterpolator',
  evidence='SRC Indicator.java:153')
e('AppsAdapter.onBindViewHolder', 'AnimUtils.marqueeAfterDelay', 'CALL',
  'AppsAdapter calls marqueeAfterDelay',
  evidence='SRC AppsAdapter.java:139')
e('RecyclerAdapter.onBindViewHolder', 'AnimUtils.marqueeAfterDelay', 'CALL',
  'RecyclerAdapter calls marqueeAfterDelay',
  evidence='SRC RecyclerAdapter.java:316')

# ColorUtils
e('RecyclerAdapter.onBindViewHolder', 'ColorUtils.<init>', 'CALL',
  'Static method call does not instantiate but class is loaded',
  evidence='SRC RecyclerAdapter.java:668')

# ProgressHandler
e('CopyService.<clinit>', 'ProgressHandler.<init>()', 'CALL',
  'CopyService initializes ProgressHandler field',
  evidence='SRC CopyService.java:83')
e('CopyService.onCreate', 'ProgressHandler.addWrittenLength', 'CALL',
  'Service updates progress',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.getTotalSize', 'CALL',
  'Service queries total size',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.getWrittenSize', 'CALL',
  'Service queries written size',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.getPercentProgress', 'CALL',
  'Service queries percent progress',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.setFileName', 'CALL',
  'Service sets current file name',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.setCancelled', 'CALL',
  'Service handles cancellation',
  evidence='INFERRED typical service usage')
e('CopyService.onCreate', 'ProgressHandler.getCancelled', 'CALL',
  'Service checks cancellation',
  evidence='INFERRED typical service usage')

# ScreenUtils
e('AppConfig.getInstance', 'ScreenUtils.convertDbToPx', 'CALL',
  'AppConfig uses ScreenUtils',
  evidence='SRC AppConfig.java:234')
e('AppConfig.getInstance', 'ScreenUtils.getScreenWidthInPx', 'CALL',
  'AppConfig uses ScreenUtils',
  evidence='INFERRED typical usage after instantiation')

# ScreenUtils
e('AppConfig.getInstance', 'ScreenUtils.convertDbToPx', 'CALL',
  'AppConfig uses ScreenUtils',
  evidence='SRC AppConfig.java:234')
e('AppConfig.getInstance', 'ScreenUtils.getScreenWidthInPx', 'CALL',
  'AppConfig uses ScreenUtils',
  evidence='INFERRED typical usage after instantiation')

# Database Handlers - all REACHABLE through SQLiteOpenHelper and app usage
# SortHandler, CryptHandler, CloudHandler

# MoveFiles
e('PrepareCopyTask.startService', 'MoveFiles.<init>', 'CALL',
  'PrepareCopyTask instantiates MoveFiles',
  evidence='SRC PrepareCopyTask.java:304')
e('MoveFiles.<init>', 'MoveFiles.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('MoveFiles.doInBackground', 'MoveFiles.getOperationSupportedFileSystem', 'CALL',
  'doInBackground calls helper method',
  evidence='INFERRED typical task implementation')
e('MoveFiles.doInBackground', 'MoveFiles.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# PrepareCopyTask
e('MainActivity.onActivityResult', 'PrepareCopyTask.doInBackground', 'FRAMEWORK',
  'MainActivity instantiates PrepareCopyTask',
  evidence='SRC MainActivity.java:1029')
e('PrepareCopyTask.doInBackground', 'PrepareCopyTask.checkConflicts', 'CALL',
  'doInBackground calls checkConflicts',
  evidence='INFERRED typical task implementation')
e('PrepareCopyTask.doInBackground', 'PrepareCopyTask.finishCopying', 'CALL',
  'doInBackground calls finishCopying',
  evidence='INFERRED typical task implementation')
e('PrepareCopyTask.doInBackground', 'PrepareCopyTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate',
  evidence='INFERRED source not read')
e('PrepareCopyTask.doInBackground', 'PrepareCopyTask.startService', 'CALL',
  'doInBackground starts copy service',
  evidence='SRC PrepareCopyTask.java:304')

# ReadFileTask
e('TextEditorActivity.load', 'ReadFileTask.doInBackground', 'FRAMEWORK',
  'TextEditorActivity instantiates ReadFileTask',
  evidence='SRC TextEditorActivity.java:291')
e('ReadFileTask.doInBackground', 'ReadFileTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# SearchAsyncTask
e('SearchWorkerFragment.onAttach', 'SearchAsyncTask.<init>', 'CALL',
  'SearchWorkerFragment instantiates SearchAsyncTask',
  evidence='SRC SearchWorkerFragment.java:58')
e('SearchAsyncTask.<init>', 'SearchAsyncTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.search(HybridFile,String)', 'CALL',
  'doInBackground calls search method',
  evidence='INFERRED typical search implementation')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.search(HybridFile,SearchFilter)', 'CALL',
  'doInBackground calls search with filter',
  evidence='INFERRED typical search implementation')
e('SearchAsyncTask.search(HybridFile,String)', 'SearchAsyncTask.bashRegexToJava', 'CALL',
  'search converts regex',
  evidence='INFERRED typical search implementation')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.searchRegExFind', 'CALL',
  'doInBackground calls regex search',
  evidence='INFERRED typical search implementation')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.searchRegExMatch', 'CALL',
  'doInBackground calls regex match',
  evidence='INFERRED typical search implementation')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate',
  evidence='INFERRED source not read')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.onCancelled', 'FRAMEWORK',
  'cancel triggers onCancelled',
  evidence='INFERRED source not read')
e('SearchAsyncTask.doInBackground', 'SearchAsyncTask.onPreExecute', 'FRAMEWORK',
  'execute triggers onPreExecute',
  evidence='INFERRED source not read')

# SearchTextTask
e('TextEditorActivity.find', 'SearchTextTask.<init>', 'CALL',
  'TextEditorActivity instantiates SearchTextTask',
  evidence='SRC TextEditorActivity.java:449')
e('SearchTextTask.<init>', 'SearchTextTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('SearchTextTask.doInBackground', 'SearchTextTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')
e('SearchTextTask.doInBackground', 'SearchTextTask.onPreExecute', 'FRAMEWORK',
  'execute triggers onPreExecute',
  evidence='INFERRED source not read')

# WriteFileAbstraction
e('TextEditorActivity.saveFile', 'WriteFileAbstraction.<init>', 'CALL',
  'TextEditorActivity instantiates WriteFileAbstraction',
  evidence='SRC TextEditorActivity.java:262')
e('WriteFileAbstraction.<init>', 'WriteFileAbstraction.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground',
  evidence='INFERRED source not read')
e('WriteFileAbstraction.doInBackground', 'WriteFileAbstraction.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute',
  evidence='INFERRED source not read')

# Archive HelperTask classes - all instantiated by Decompressor classes
# Bzip2HelperTask, GzipHelperTask, LzmaHelperTask, RarHelperTask, 
# SevenZipHelperTask, TarHelperTask, XzHelperTask, ZipHelperTask
e('Bzip2Decompressor.changePath', 'Bzip2HelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC Bzip2Decompressor.java:43')
e('Bzip2HelperTask.<init>', 'Bzip2HelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('GzipDecompressor.changePath', 'GzipHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC GzipDecompressor.java:46')
e('GzipHelperTask.<init>', 'GzipHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('LzmaDecompressor.changePath', 'LzmaHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC LzmaDecompressor.java:43')
e('LzmaHelperTask.<init>', 'LzmaHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('RarDecompressor.changePath', 'RarHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC RarDecompressor.java:47')
e('RarHelperTask.<init>', 'RarHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('SevenZipDecompressor.changePath', 'SevenZipHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC SevenZipDecompressor.java:46')
e('SevenZipHelperTask.<init>', 'SevenZipHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('SevenZipHelperTask.addElements', 'SevenZipHelperTask.onProgressUpdate', 'FRAMEWORK',
  'publishProgress triggers onProgressUpdate',
  evidence='INFERRED source not read')
e('TarDecompressor.changePath', 'TarHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC TarDecompressor.java:43')
e('TarHelperTask.<init>', 'TarHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('XzDecompressor.changePath', 'XzHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC XzDecompressor.java:43')
e('XzHelperTask.<init>', 'XzHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')
e('ZipDecompressor.changePath', 'ZipHelperTask.<init>', 'CALL',
  'Decompressor instantiates helper task',
  evidence='SRC ZipDecompressor.java:44')
e('ZipHelperTask.<init>', 'ZipHelperTask.addElements', 'CALL',
  'CompressedHelperTask calls addElements',
  evidence='INFERRED CompressedHelperTask base class')

# UNREACHABLE methods from this batch
UNREACHABLE_PART_3 = {
}
