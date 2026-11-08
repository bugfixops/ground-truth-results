# Repair batch 18: routes and unreachable labels
# Generated for AmazeFileManager schema-2 graph

# ========== SevenZFile$2 ==========

# SevenZFile$2 is an anonymous InputStreamStatistics implementation returned by getStatisticsForCurrentEntry()
# SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1116-1125

e('SevenZFile.getStatisticsForCurrentEntry', 'SevenZFile$2.<init>', 'CALL',
  'Anonymous InputStreamStatistics created and returned',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1116-1125')

e('AndroidInputStreamStatistics.getCompressedCount', 'SevenZFile$2.getCompressedCount', 'CALL',
  'Framework calls getCompressedCount on InputStreamStatistics',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1119-1121')

e('AndroidInputStreamStatistics.getUncompressedCount', 'SevenZFile$2.getUncompressedCount', 'CALL',
  'Framework calls getUncompressedCount on InputStreamStatistics',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZFile.java:1123-1125')


# ========== SevenZMethodConfiguration ==========

# SevenZMethodConfiguration is a library class used to configure 7z compression methods
# SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZMethodConfiguration.java

e('SevenZArchiveEntry.setContentMethods', 'SevenZMethodConfiguration.<init>(SevenZMethod)', 'CALL',
  'new SevenZMethodConfiguration(method)',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZMethodConfiguration.java:47-49; used in 7z compression')

e('SevenZOutputFile.setContentMethods', 'SevenZMethodConfiguration.getMethod', 'CALL',
  'Retrieves the compression method from configuration',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZMethodConfiguration.java:71-73')

e('SevenZOutputFile.setContentMethods', 'SevenZMethodConfiguration.getOptions', 'CALL',
  'Retrieves the compression options from configuration',
  evidence='SRC commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/SevenZMethodConfiguration.java:79-81')


# ========== CustomSshJConfig ==========

# CustomSshJConfig already has constructor route in graph_def.py:2744,2748
# SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/CustomSshJConfig.java

e('CustomSshJConfig.<init>', 'CustomSshJConfig.initSignatureFactories', 'CALL',
  'DefaultConfig parent constructor calls initSignatureFactories()',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/CustomSshJConfig.java:53-55; override method')

e('CustomSshJConfig.<init>', 'CustomSshJConfig.initRandomFactory', 'CALL',
  'DefaultConfig parent constructor calls initRandomFactory(boolean)',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/CustomSshJConfig.java:57-60; override method')


# ========== SshConnectionPool$AsyncRemoveConnection ==========

# AsyncRemoveConnection is a private inner AsyncTask class for removing SSH connections
# SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/SshConnectionPool.java:280-307

e('SshConnectionPool.removeConnection', 'SshConnectionPool$AsyncRemoveConnection.<init>', 'CALL',
  'new AsyncRemoveConnection(url, callback)',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/SshConnectionPool.java:98')

e('AndroidAsyncTask.execute', 'SshConnectionPool$AsyncRemoveConnection.doInBackground', 'CALL',
  'Framework calls doInBackground when AsyncTask executes',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/SshConnectionPool.java:294-302')

e('SshConnectionPool$AsyncRemoveConnection.doInBackground', 'SshConnectionPool$AsyncRemoveConnection.onPostExecute', 'CALL',
  'Framework calls onPostExecute after doInBackground completes',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/SshConnectionPool.java:304-307')


# ========== Statvfs$Response ==========

# Statvfs$Response wraps SSH statvfs@openssh.com response data
# SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/Statvfs.java:77-224

e('SshClientSessionTemplate.execute', 'Statvfs$Response.getFileSystemId', 'CALL',
  'Caller retrieves filesystem ID wrapped in BigInteger',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/Statvfs.java:192-195')

e('SshClientSessionTemplate.execute', 'Statvfs$Response.getRawFileSystemId', 'CALL',
  'Caller retrieves raw filesystem ID as long',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/Statvfs.java:202-205')

e('SshClientUtils.execute', 'Statvfs$Response.toString', 'CALL',
  'toString() for debugging/logging',
  evidence='SRC app/src/main/java/com/amaze/filemanager/filesystem/ssh/Statvfs.java:217-224')


# ========== MainFragment$4$1 ==========

# MainFragment$4$1 is the MediaScannerConnectionClient anonymous class in MainFragment$4 receiver
# SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:798-814

e('MainFragment$4.onReceive', 'MainFragment$4$1.<init>', 'CALL',
  'Anonymous MediaScannerConnectionClient created',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:798')

e('AndroidMediaScannerConnection.connect', 'MainFragment$4$1.onMediaScannerConnected', 'CALL',
  'Framework callback when MediaScanner connects',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:800-803')

e('AndroidMediaScannerConnection.scanFile', 'MainFragment$4$1.onScanCompleted', 'CALL',
  'Framework callback when MediaScanner completes scanning',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:805-809')


# ========== MainFragment$6 ==========

# MainFragment$6 is an anonymous AsyncTask for sorting search results
# SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1640-1653

e('MainFragment.addSearchResult', 'MainFragment$6.<init>', 'CALL',
  'Anonymous AsyncTask created to sort LIST_ELEMENTS',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1640')

e('AndroidAsyncTask.execute', 'MainFragment$6.doInBackground', 'CALL',
  'Framework calls doInBackground to sort results',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1642-1645')

e('MainFragment$6.doInBackground', 'MainFragment$6.onPostExecute', 'CALL',
  'Framework calls onPostExecute after sorting completes',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/MainFragment.java:1647-1651')


# ========== ProcessViewerFragment$CustomServiceConnection ==========

# CustomServiceConnection is a private static inner class implementing ServiceConnection
# SRC app/src/main/java/com/amaze/filemanager/fragments/ProcessViewerFragment.java:390-437

e('ProcessViewerFragment.onCreateView', 'ProcessViewerFragment$CustomServiceConnection.<init>', 'CALL',
  'new CustomServiceConnection(this, mLineChart, SERVICE_*)',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/ProcessViewerFragment.java:127-131')

e('AndroidContext.bindService', 'ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'CALL',
  'Framework callback when service binds',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/ProcessViewerFragment.java:404-432')

e('AndroidContext.unbindService', 'ProcessViewerFragment$CustomServiceConnection.onServiceDisconnected', 'CALL',
  'Framework callback when service disconnects',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/ProcessViewerFragment.java:435')


# ========== PropertiesSheet ==========

# PropertiesSheet is a BottomSheetDialogFragment for displaying file properties
# SRC app/src/main/java/com/amaze/filemanager/fragments/PropertiesSheet.java

e('MainFragment.showProperties', 'PropertiesSheet.<init>', 'CALL',
  'new PropertiesSheet() created by fragment manager',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/PropertiesSheet.java:29')

e('PropertiesSheet.<init>', 'PropertiesSheet.generate', 'CALL',
  'generate(BottomSheetCallback) initializes properties',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/PropertiesSheet.java:112-116')

e('AndroidFragment.show', 'PropertiesSheet.setupDialog', 'CALL',
  'Framework lifecycle method called when dialog is set up',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/PropertiesSheet.java:49-108')


# ========== PropertiesSheet$2 ==========

# PropertiesSheet$2 is the BottomSheetCallback field mCallback
# SRC app/src/main/java/com/amaze/filemanager/fragments/PropertiesSheet.java:117-129

e('PropertiesSheet.setupDialog', 'PropertiesSheet$2.<init>', 'CALL',
  'Field initializer creates BottomSheetCallback',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/PropertiesSheet.java:117; setBottomSheetCallback(mCallback) at line 82')

e('AndroidBottomSheetBehavior.setState', 'PropertiesSheet$2.onSlide', 'CALL',
  'Framework callback when bottom sheet slides',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/PropertiesSheet.java:126-128')

e('AndroidBottomSheetBehavior.setState', 'PropertiesSheet$2.onStateChanged', 'CALL',
  'Framework callback when bottom sheet state changes',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/PropertiesSheet.java:119-123')


# ========== SearchWorkerFragment ==========

# SearchWorkerFragment already has routes in graph_def.py for onAttach (line 1295)
# SRC app/src/main/java/com/amaze/filemanager/fragments/SearchWorkerFragment.java

e('MainActivity.search', 'SearchWorkerFragment.onAttach', 'CALL',
  'Framework lifecycle method when fragment attaches to activity',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/SearchWorkerFragment.java:40-44')

e('SearchWorkerFragment.onAttach', 'SearchWorkerFragment.onCreate', 'CALL',
  'Framework lifecycle method after onAttach',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/SearchWorkerFragment.java:46-62')

e('MainActivity.onDestroy', 'SearchWorkerFragment.onDetach', 'CALL',
  'Framework lifecycle method when fragment detaches',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/SearchWorkerFragment.java:64-68')


# ========== TabFragment$ScreenSlidePagerAdapter ==========

# ScreenSlidePagerAdapter is a private inner FragmentStatePagerAdapter
# SRC app/src/main/java/com/amaze/filemanager/fragments/TabFragment.java:319-347

e('TabFragment.initViewPager', 'TabFragment$ScreenSlidePagerAdapter.getCount', 'CALL',
  'Framework calls getCount() to determine number of pages',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/TabFragment.java:332-335')

e('AndroidViewPager.setCurrentItem', 'TabFragment$ScreenSlidePagerAdapter.getItem', 'CALL',
  'Framework calls getItem(position) to create fragment at position',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/TabFragment.java:342-346')

e('AndroidViewPager.notifyDataSetChanged', 'TabFragment$ScreenSlidePagerAdapter.getItemPosition', 'CALL',
  'Framework calls getItemPosition() to refresh adapter',
  evidence='SRC app/src/main/java/com/amaze/filemanager/fragments/TabFragment.java:321-327')


# ========== UserColorPreferences ==========

# UserColorPreferences is a Parcelable data class for color preferences
# SRC app/src/main/java/com/amaze/filemanager/ui/colors/UserColorPreferences.java

e('AndroidIntent.getParcelableExtra', 'UserColorPreferences.<init>(Parcel)', 'CALL',
  'Framework calls Parcelable constructor to deserialize',
  evidence='SRC app/src/main/java/com/amaze/filemanager/ui/colors/UserColorPreferences.java:20-25; CREATOR.createFromParcel line 42')

e('AndroidIntent.putParcelableExtra', 'UserColorPreferences.describeContents', 'CALL',
  'Framework calls describeContents() for Parcelable protocol',
  evidence='SRC app/src/main/java/com/amaze/filemanager/ui/colors/UserColorPreferences.java:34-36')

e('AndroidIntent.putParcelableExtra', 'UserColorPreferences.writeToParcel', 'CALL',
  'Framework calls writeToParcel() to serialize',
  evidence='SRC app/src/main/java/com/amaze/filemanager/ui/colors/UserColorPreferences.java:27-32')
