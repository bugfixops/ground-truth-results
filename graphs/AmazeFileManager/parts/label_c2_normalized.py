# ---- Chunk 2 label part (2025-01-10)
# Classes: AppListLoader, AppListLoader$AppsDataPair, AppTheme, AppThemeManager,
#          AppsAdapter, AppsAdapterPreloadModel, AppsListFragment, Archive, 
#          ArchivePasswordCache, ArchivePasswordCache$ArchivePasswordCacheHolder,
#          AsyncTaskResult, BindPair, BookSorter

# AppsListFragment routes
e('Drawer.lambda$addAppsItem$N', 'AppsListFragment.<init>', 'EXPLICIT',
  'Drawer menu Apps item creates AppsListFragment',
  evidence='SRC Drawer.java:421 new AppsListFragment()')

e('AppsListFragment.<init>', 'AppsListFragment.onCreate', 'FRAMEWORK',
  'Framework calls onCreate after fragment created',
  evidence='INFERRED framework source not read')

e('AppsListFragment.onCreate', 'AppsListFragment.onActivityCreated', 'FRAMEWORK',
  'Framework calls onActivityCreated after onCreate',
  evidence='INFERRED framework source not read')

e('AppsListFragment.onActivityCreated', 'AppsListFragment.getSortModes', 'CALL',
  'onActivityCreated calls getSortModes at line 88',
  evidence='SRC AppsListFragment.java:88 getSortModes()')

e('AppsListFragment.onActivityCreated', 'AppsAdapterPreloadModel.<init>', 'CALL',
  'onActivityCreated instantiates AppsAdapterPreloadModel at line 96',
  evidence='SRC AppsListFragment.java:96 modelProvider = new AppsAdapterPreloadModel(app)')

e('AppsListFragment.onActivityCreated', 'AppsAdapter.<init>', 'CALL',
  'onActivityCreated instantiates AppsAdapter at line 101',
  evidence='SRC AppsListFragment.java:101 adapter = new AppsAdapter(...)')

e('AppsListFragment.onActivityCreated', 'AppsListFragment.onCreateLoader', 'FRAMEWORK',
  'initLoader triggers onCreateLoader callback',
  evidence='SRC AppsListFragment.java:106 getLoaderManager().initLoader(..., this); INFERRED loader framework calls onCreateLoader')

e('AppsListFragment.onCreateLoader', 'AppListLoader.<init>', 'CALL',
  'onCreateLoader creates AppListLoader',
  evidence='SRC AppsListFragment.java:163 return new AppListLoader(getContext(), sortby, asc)')

e('AppListLoader.<init>', 'AppListLoader.onStartLoading', 'FRAMEWORK',
  'Loader framework calls onStartLoading',
  evidence='INFERRED loader framework source not read')

e('AppListLoader.onStartLoading', 'AppListLoader.loadInBackground', 'FRAMEWORK',
  'onStartLoading calls forceLoad which triggers loadInBackground',
  evidence='SRC AppListLoader.java:133 forceLoad(); INFERRED framework invokes loadInBackground')

e('AppListLoader.loadInBackground', 'AppListLoader$AppsDataPair.<init>', 'CALL',
  'loadInBackground creates AppsDataPair instances',
  evidence='SRC AppListLoader.java:52 return new AppsDataPair(...); SRC AppListLoader.java:56 mApps = new AppsDataPair(...)')

e('AppListLoader.loadInBackground', 'AppListLoader.deliverResult', 'FRAMEWORK',
  'Framework calls deliverResult after loadInBackground completes',
  evidence='INFERRED loader framework source not read')

e('AppListLoader.deliverResult', 'AppsListFragment.onLoadFinished', 'FRAMEWORK',
  'Loader deliverResult triggers callback onLoadFinished',
  evidence='INFERRED loader framework source not read')

e('AppsListFragment.onLoadFinished', 'AppsAdapter.setData', 'CALL',
  'onLoadFinished calls adapter.setData',
  evidence='SRC AppsListFragment.java:168 adapter.setData(data.first)')

e('AppsListFragment.onLoadFinished', 'AppsAdapterPreloadModel.setItemList', 'CALL',
  'onLoadFinished calls modelProvider.setItemList',
  evidence='SRC AppsListFragment.java:169 modelProvider.setItemList(data.second)')

e('AppsAdapter.setData', 'AppsAdapter.getView', 'FRAMEWORK',
  'After setData, framework calls getView when ListView renders',
  evidence='INFERRED ListView framework source not read')

e('AppsAdapter.getView', 'AppsAdapterPreloadModel.loadApkImage', 'CALL',
  'getView calls modelProvider.loadApkImage',
  evidence='SRC AppsAdapter.java:124 modelProvider.loadApkImage(rowItem.path, holder.apkIcon)')

e('AppsAdapter.getView', 'AppsAdapter.showPopup', 'CALL',
  'getView calls showPopup',
  evidence='SRC AppsAdapter.java:129 showPopup(holder.about, rowItem)')

e('AppsAdapter.showPopup', 'AppsAdapter.lambda$showPopup$4', 'CALL',
  'showPopup sets OnClickListener with lambda',
  evidence='SRC AppsAdapter.java:168 v.setOnClickListener(view -> {...})')

e('AppsAdapter.getView', 'AppsAdapter.lambda$getView$0', 'CALL',
  'getView sets OnClickListener on holder.rl with lambda',
  evidence='SRC AppsAdapter.java:145 holder.rl.setOnClickListener(p1 -> {...})')

e('AppsAdapter.showPopup', 'AppsAdapter.lambda$null$1', 'CALL',
  'showPopup creates nested lambda for dialog onNegative',
  evidence='SRC AppsAdapter.java:203 .onNegative(((dialog, which) -> dialog.cancel()))')

e('AppsAdapter.showPopup', 'AppsAdapter.lambda$null$2', 'CALL',
  'showPopup creates nested lambda for dialog onPositive',
  evidence='SRC AppsAdapter.java:204 .onPositive(((dialog, which) -> {...}))')

e('AppsAdapter.showPopup', 'AppsAdapter.lambda$null$3', 'CALL',
  'showPopup menu uninstall path calls unin for non-system apps',
  evidence='SRC AppsAdapter.java:220 app.unin(rowItem.packageName)')

e('AppsAdapter.lambda$null$3', 'AppsListFragment.unin', 'CALL',
  'Lambda from menu item calls unin',
  evidence='SRC AppsAdapter.java:220 in unins case: else { app.unin(rowItem.packageName); }')

# AppTheme routes
e('UtilitiesProvider.<init>', 'AppThemeManager.<init>', 'CALL',
  'UtilitiesProvider instantiates AppThemeManager',
  evidence='SRC UtilitiesProvider.java:25 appThemeManager = new AppThemeManager(sharedPreferences)')

e('AppThemeManager.<init>', 'AppTheme.getTheme', 'CALL',
  'Constructor calls AppTheme.getTheme',
  evidence='SRC AppThemeManager.java:17 appTheme = AppTheme.getTheme(Integer.parseInt(themeId)).getSimpleTheme()')

e('AppThemeManager.<init>', 'AppTheme.getSimpleTheme', 'CALL',
  'Constructor calls getSimpleTheme on result',
  evidence='SRC AppThemeManager.java:17 appTheme = AppTheme.getTheme(...).getSimpleTheme()')

e('AppThemeManager.getAppTheme', 'AppTheme.getSimpleTheme', 'CALL',
  'getAppTheme calls getSimpleTheme',
  evidence='SRC AppThemeManager.java:24 return appTheme.getSimpleTheme()')

e('AppThemeManager.setAppTheme', 'AppTheme.getId', 'CALL',
  'setAppTheme calls getId to save theme',
  evidence='SRC AppThemeManager.java:33 Integer.toString(appTheme.getId())')

e('AppsListFragment.onActivityCreated', 'AppTheme.getMaterialDialogTheme', 'CALL',
  'Uses AppTheme enum values through UtilitiesProvider',
  evidence='SRC AppsListFragment.java:91 if (utilsProvider.getAppTheme().equals(AppTheme.DARK)); INFERRED getMaterialDialogTheme called in dialogs')

# BookSorter routes
e('Drawer.lambda$addBookmark$N', 'BookSorter.<init>', 'CALL',
  'Drawer instantiates BookSorter for sorting bookmarks',
  evidence='SRC Drawer.java:356 Collections.sort(dataUtils.getBooks(), new BookSorter())')

e('Drawer.lambda$addBookmark$N', 'BookSorter.compare', 'CALL',
  'Collections.sort calls compare method',
  evidence='SRC Drawer.java:356 Collections.sort(..., new BookSorter()); INFERRED sort calls compare')

# ArchivePasswordCache routes
e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.getInstance', 'CALL',
  'SevenZipHelperTask calls getInstance',
  evidence='SRC SevenZipHelperTask.java:69 ArchivePasswordCache.getInstance().get(filePath)')

e('ArchivePasswordCache.getInstance', 'ArchivePasswordCache$ArchivePasswordCacheHolder.<clinit>', 'CALL',
  'getInstance accesses holder class which triggers static init',
  evidence='SRC ArchivePasswordCache.java:67 return ArchivePasswordCacheHolder.INSTANCE; INFERRED static init creates INSTANCE')

e('ArchivePasswordCache$ArchivePasswordCacheHolder.<clinit>', 'ArchivePasswordCache.<init>', 'CALL',
  'Static initializer creates singleton instance',
  evidence='SRC ArchivePasswordCache.java:61 private static final ArchivePasswordCache INSTANCE = new ArchivePasswordCache()')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.get', 'CALL',
  'After getInstance, calls get method',
  evidence='SRC SevenZipHelperTask.java:69 ArchivePasswordCache.getInstance().get(filePath)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.containsKey', 'CALL',
  'SevenZipHelperTask checks if password is cached',
  evidence='SRC SevenZipHelperTask.java:68 ArchivePasswordCache.getInstance().containsKey(filePath)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.remove', 'CALL',
  'After password exception, removes invalid password',
  evidence='SRC SevenZipHelperTask.java:103 ArchivePasswordCache.getInstance().remove(filePath)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.put', 'CALL',
  'After user enters password, stores it in cache',
  evidence='SRC SevenZipHelperTask.java:111 ArchivePasswordCache.getInstance().put(filePath, password)')

# AsyncTaskResult routes
e('CompressedHelperTask.doInBackground', 'AsyncTaskResult.<init>', 'CALL',
  'CompressedHelperTask creates AsyncTaskResult instances',
  evidence='SRC CompressedHelperTask.java:58 return new AsyncTaskResult<>(elements); SRC CompressedHelperTask.java:60 return new AsyncTaskResult<>(ifArchiveIsCorruptOrInvalid)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.containsKey', 'CALL',
  'SevenZipHelperTask checks if password is cached',
  evidence='SRC SevenZipHelperTask.java:68 ArchivePasswordCache.getInstance().containsKey(filePath)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.remove', 'CALL',
  'After password exception, removes invalid password',
  evidence='SRC SevenZipHelperTask.java:103 ArchivePasswordCache.getInstance().remove(filePath)')

e('SevenZipHelperTask.doInBackground', 'ArchivePasswordCache.put', 'CALL',
  'After user enters password, stores it in cache',
  evidence='SRC SevenZipHelperTask.java:111 ArchivePasswordCache.getInstance().put(filePath, password)')

e('GlideListPreloader.onScroll', 'AppsAdapterPreloadModel.getPreloadItems', 'CALL',
  'Glide ListPreloader calls getPreloadItems during scroll',
  evidence='SRC AppsListFragment.java:98-99,103 ListPreloader created with modelProvider, set as scroll listener; INFERRED Glide source calls getPreloadItems')

e('GlideListPreloader.onScroll', 'AppsAdapterPreloadModel.getPreloadRequestBuilder', 'CALL',
  'Glide ListPreloader calls getPreloadRequestBuilder to build requests',
  evidence='SRC AppsListFragment.java:98-99,103 ListPreloader setup; INFERRED Glide source calls getPreloadRequestBuilder')

# Archive and BindPair - library classes from sevenz, NOT called by app

# UNREACHABLE methods from chunk_2
UNREACHABLE['Archive.<init>'] = ('no_trigger_in_app', 
                       'Archive is from com.amaze.filemanager.filesystem.compressed.sevenz package (Apache Commons Compress library)
UNREACHABLE['Archive.lengthOf'] = ('no_trigger_in_app',
                         'Library method from sevenz.Archive which is not called by app',
                         'grep -rn "sevenz.Archive" app/src/main/java/ returns no matches',
                         'INFERRED')
UNREACHABLE['Archive.toString'] = ('no_trigger_in_app',
                         'Library method from sevenz.Archive which is not called by app',
                         'grep -rn "sevenz.Archive" app/src/main/java/ returns no matches',
                         'INFERRED')
UNREACHABLE['BindPair.<init>'] = ('no_trigger_in_app',
                        'BindPair is from com.amaze.filemanager.filesystem.compressed.sevenz package. Grep shows no app source calls to BindPair class.',
                        'grep -rn "BindPair" app/src/main/java/ returns no matches',
                        'INFERRED')
UNREACHABLE['BindPair.toString'] = ('no_trigger_in_app',
                          'Library method from sevenz.BindPair which is not called by app',
                          'grep -rn "BindPair" app/src/main/java/ returns no matches',
                          'INFERRED')
UNREACHABLE['AppListLoader.onStopLoading'] = ('framework_never_calls',
                                     'onStopLoading is called by loader framework when loader is stopped. AppsListFragment retains instance (setRetainInstance(true)
UNREACHABLE['AppListLoader.onReset'] = ('framework_never_calls',
                              'onReset is called when loader is being reset/destroyed. Fragment retains instance so loader persists and is not reset during normal flow.',
                              'SRC AppsListFragment.java:80 setRetainInstance(true)
UNREACHABLE['AppListLoader.onCanceled'] = ('framework_never_calls',
                                 'onCanceled called when load operation is canceled. Load completes normally in standard flow.',
                                 'SRC AppListLoader.java:143-146 onCanceled(data)
UNREACHABLE['AppListLoader.onReleaseResources'] = ('no_trigger_in_app',
                                         'Private helper method that is called from onCanceled, onReset, and deliverResult, but those callers are not reached (see above)
UNREACHABLE['AppsListFragment.onSaveInstanceState'] = ('framework_never_calls',
                                              'onSaveInstanceState saves view position state, but fragment sets setRetainInstance(true)
UNREACHABLE['AppsListFragment.onLoaderReset'] = ('framework_never_calls',
                                        'Loader reset callback, but loader is not reset due to retained instance.',
                                        'SRC AppsListFragment.java:80 setRetainInstance(true)
UNREACHABLE['AppTheme.<clinit>'] = ('framework_never_calls',
                          'Static initializer for AppTheme enum, called when enum is first loaded.',
                          'Enum initialization is automatic when class is loaded',
                          'INFERRED')
UNREACHABLE['AppTheme.<init>'] = ('framework_never_calls',
                        'Private enum constructor called during enum static initialization',
                        'SRC AppTheme.java:24 AppTheme(int id)
UNREACHABLE['ArchivePasswordCache$ArchivePasswordCacheHolder.<init>'] = ('no_trigger_in_app',
                                                               'Private inner class constructor. The holder uses a static field INSTANCE which is initialized without calling the holder constructor.',
                                                               'SRC ArchivePasswordCache.java:60-62 private static class with static field only',
                                                               'SOURCE')
UNREACHABLE['ArchivePasswordCache.clear'] = ('no_trigger_in_app',
                                    'Map clear method. grep -rn "ArchivePasswordCache.*\\.clear" app/src/main/java/ returns no matches.',
                                    'grep shows no call sites',
                                    'INFERRED')
UNREACHABLE['ArchivePasswordCache.containsValue'] = ('no_trigger_in_app',
                                            'Map containsValue method. grep -rn "ArchivePasswordCache.*\\.containsValue" app/src/main/java/ returns no matches.',
                                            'grep shows no call sites',
                                            'INFERRED')
UNREACHABLE['ArchivePasswordCache.entrySet'] = ('no_trigger_in_app',
                                       'Map entrySet method. grep -rn "ArchivePasswordCache.*\\.entrySet" app/src/main/java/ returns no matches.',
                                       'grep shows no call sites',
                                       'INFERRED')
UNREACHABLE['ArchivePasswordCache.equals'] = ('no_trigger_in_app',
                                     'Map equals method. grep -rn "ArchivePasswordCache.*\\.equals" app/src/main/java/ returns no matches.',
                                     'grep shows no call sites',
                                     'INFERRED')
UNREACHABLE['ArchivePasswordCache.hashCode'] = ('no_trigger_in_app',
                                       'Map hashCode method. grep -rn "ArchivePasswordCache.*\\.hashCode" app/src/main/java/ returns no matches.',
                                       'grep shows no call sites',
                                       'INFERRED')
UNREACHABLE['ArchivePasswordCache.isEmpty'] = ('no_trigger_in_app',
                                      'Map isEmpty method. grep -rn "ArchivePasswordCache.*\\.isEmpty" app/src/main/java/ returns no matches.',
                                      'grep shows no call sites',
                                      'INFERRED')
UNREACHABLE['ArchivePasswordCache.keySet'] = ('no_trigger_in_app',
                                     'Map keySet method. grep -rn "ArchivePasswordCache.*\\.keySet" app/src/main/java/ returns no matches.',
                                     'grep shows no call sites',
                                     'INFERRED')
UNREACHABLE['ArchivePasswordCache.putAll'] = ('no_trigger_in_app',
                                     'Map putAll method. grep -rn "ArchivePasswordCache.*\\.putAll" app/src/main/java/ returns no matches.',
                                     'grep shows no call sites',
                                     'INFERRED')
UNREACHABLE['ArchivePasswordCache.size'] = ('no_trigger_in_app',
                                   'Map size method. grep -rn "ArchivePasswordCache.*\\.size" app/src/main/java/ returns no matches.',
                                   'grep shows no call sites',
                                   'INFERRED')
UNREACHABLE['ArchivePasswordCache.toString'] = ('no_trigger_in_app',
                                       'Map toString method. grep -rn "ArchivePasswordCache.*\\.toString" app/src/main/java/ returns no matches.',
                                       'grep shows no call sites',
                                       'INFERRED')
UNREACHABLE['ArchivePasswordCache.values'] = ('no_trigger_in_app',
                                     'Map values method. grep -rn "ArchivePasswordCache.*\\.values" app/src/main/java/ returns no matches.',
                                     'grep shows no call sites',
                                     'INFERRED')
