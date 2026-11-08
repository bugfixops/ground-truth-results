# ---- Batch 003 label part (2026-10-27)
# Classes: AppTheme, AppThemeManager, AppsAdapter, AppsAdapterPreloadModel, AppsListFragment, Archive

# ---- AppTheme enum ----
# Enum static methods - reachable through getTheme() callers
e('UtilitiesProvider.getAppTheme', 'AppTheme.getTheme', 'CALL',
  'UtilitiesProvider.getAppTheme() calls AppTheme.getTheme()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/provider/UtilitiesProvider.java:28-30')

e('AppTheme.getTheme', 'AppTheme.<init>', 'CALL',
  'getTheme() returns enum constant (implicitly calls <init> via constructor)',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/theme/AppTheme.java:29-46')

e('AppTheme.<clinit>', 'AppTheme.<init>', 'CALL',
  'Enum <clinit> creates enum constants via <init>',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/theme/AppTheme.java:10-14')

e('AppTheme.getSimpleTheme', 'AppTheme.getId', 'CALL',
  'getSimpleTheme() may call getId() through getTheme()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/theme/AppTheme.java:74-88')

# getMaterialDialogTheme is called by many activities, reachable through AppTheme methods
e('UtilitiesProvider.getAppTheme', 'AppTheme.getMaterialDialogTheme', 'CALL',
  'Called from ThemedActivity.getAppTheme().getMaterialDialogTheme()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/ui/dialogs/GeneralDialogCreation.java:131')

# ---- AppThemeManager ----
e('UtilitiesProvider.<init>', 'AppThemeManager.<init>', 'CALL',
  'UtilitiesProvider creates AppThemeManager instance',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/provider/UtilitiesProvider.java:25')

e('UtilitiesProvider.getAppTheme', 'AppThemeManager.getAppTheme', 'CALL',
  'UtilitiesProvider.getAppTheme() delegates to AppThemeManager.getAppTheme()',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/provider/UtilitiesProvider.java:28-30')

e('PreferencesConstants.FRAGMENT_THEME', 'AppThemeManager.setAppTheme', 'CALL',
  'Called when preferences change - reached through preference listener',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/utils/theme/AppThemeManager.java:34')

# ---- AppsAdapter ----
e('AppsListFragment.onActivityCreated', 'AppsAdapter.<init>', 'CALL',
  'onActivityCreated creates AppsAdapter instance',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:100-103')

e('AppsAdapter.<init>', 'AppsAdapter.getView', 'LIFECYCLE',
  'ArrayAdapter lifecycle - getView is called by ListView when rendering rows',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:64-93')

e('AppsAdapter.getView', 'AppsAdapter.lambda$getView$0', 'CALL',
  'getView sets click listener which invokes lambda',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:129-135')

e('AppsAdapter.getView', 'AppsAdapter.showPopup', 'CALL',
  'getView calls showPopup to set up menu',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:120')

e('AppsAdapter.showPopup', 'AppsAdapter.lambda$showPopup$4', 'CALL',
  'showPopup creates menu with lambdas for click handlers',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:140-185')

e('AppsAdapter.getView', 'AppsAdapter.lambda$null$1', 'CALL',
  'Lambdas used in getView for color filter logic',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:119-120')

e('AppsAdapter.getView', 'AppsAdapter.lambda$null$2', 'CALL',
  'Lambda for marquee animation delay',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:124-128')

e('AppsAdapter.getView', 'AppsAdapter.lambda$null$3', 'CALL',
  'Lambda for ellipsize setting',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:123-125')

e('AppsListFragment.onLoadFinished', 'AppsAdapter.setData', 'CALL',
  'onLoadFinished calls setData to update adapter with new app list',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:165')

# ---- AppsAdapterPreloadModel ----
e('AppsListFragment.onActivityCreated', 'AppsAdapterPreloadModel.<init>', 'CALL',
  'onActivityCreated creates AppsAdapterPreloadModel for Glide preloading',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:96')

e('AppsAdapterPreloadModel.<init>', 'AppsAdapterPreloadModel.getPreloadRequestBuilder', 'LIFECYCLE',
  'Constructor stores request, getPreloadRequestBuilder() is called by Glide preloader',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/glide/AppsAdapterPreloadModel.java:27-28')

e('AppsListFragment.onLoadFinished', 'AppsAdapterPreloadModel.setItemList', 'CALL',
  'onLoadFinished calls setItemList to update items for preloading',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/fragments/AppsListFragment.java:167')

e('AppsAdapterPreloadModel.getPreloadRequestBuilder', 'AppsAdapterPreloadModel.getPreloadItems', 'FRAMEWORK',
  'Glide preloader calls both getPreloadItems and getPreloadRequestBuilder',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/glide/AppsAdapterPreloadModel.java:35-40')

e('AppsAdapter.getView', 'AppsAdapterPreloadModel.loadApkImage', 'CALL',
  'getView calls loadApkImage to load app icon via Glide',
  evidence='SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main/java/com/amaze/filemanager/adapters/AppsAdapter.java:115')

# ---- AppsListFragment ----
# Already modeled in graph_def.py with entry from Drawer.onNavigationItemSelected
# Additional methods are lifecycle and loader callbacks

# ---- Archive (7z library) ----
# Archive is a helper class within the commons_compress_7z library
# It is instantiated and used by SevenZFile (from the same library)
# The app does NOT directly use Archive - it only uses SevenZFile
# Therefore Archive methods are only called from the 7z library, not from app code

UNREACHABLE['Archive.<init>'] = (
    'no_trigger_in_app',
    'Archive is internal to apache commons 7z library; only SevenZFile instantiates it from library code',
    'SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Archive.java:43',
    'SOURCE'
)
UNREACHABLE['Archive.lengthOf'] = (
    'no_trigger_in_app',
    'Private static helper method used only by Archive.toString(), which is toString only used by library',
    'SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Archive.java:40-53',
    'SOURCE'
)
UNREACHABLE['Archive.toString'] = (
    'no_trigger_in_app',
    'toString() is only called by library debugging; app never calls toString on Archive instances',
    'SRC final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/commons_compress_7z/src/main/java/com/amaze/filemanager/filesystem/compressed/sevenz/Archive.java:36-41',
    'SOURCE'
)
