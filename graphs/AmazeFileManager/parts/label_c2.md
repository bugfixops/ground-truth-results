STATUS: RUNNING 2025-01-10

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| AppsListFragment.<init> | REACHABLE | | Instantiated from Drawer menu Apps item | SRC Drawer.java:421 new AppsListFragment() |
| AppsListFragment.onCreate | REACHABLE | | Framework calls after fragment created | INFERRED framework calls onCreate |
| AppsListFragment.onActivityCreated | REACHABLE | | Framework calls after onCreate | SRC AppsListFragment.java:81-116 method |
| AppsListFragment.getSortModes | REACHABLE | | Called from onActivityCreated | SRC AppsListFragment.java:88 getSortModes() |
| AppsListFragment.onCreateLoader | REACHABLE | | Loader framework callback from initLoader | SRC AppsListFragment.java:106 initLoader; SRC AppsListFragment.java:163 onCreateLoader |
| AppsListFragment.onLoadFinished | REACHABLE | | Loader framework callback after loadInBackground | SRC AppsListFragment.java:167-176 method |
| AppsListFragment.unin | REACHABLE | | Called from AppsAdapter menu lambda | SRC AppsAdapter.java:220 app.unin(rowItem.packageName) |
| AppsListFragment.onSaveInstanceState | UNREACHABLE | framework_never_calls | Fragment sets setRetainInstance(true) so instance retained, onSaveInstanceState not called for config changes | SRC AppsListFragment.java:80 setRetainInstance(true); SRC AppsListFragment.java:118-128 method |
| AppsListFragment.onLoaderReset | UNREACHABLE | framework_never_calls | Loader not reset due to retained fragment instance | SRC AppsListFragment.java:80 setRetainInstance(true); SRC AppsListFragment.java:178-180 method |
| AppListLoader.<init> | REACHABLE | | Instantiated from onCreateLoader | SRC AppsListFragment.java:163 new AppListLoader(...) |
| AppListLoader.loadInBackground | REACHABLE | | Loader framework calls after forceLoad | SRC AppListLoader.java:133 forceLoad(); INFERRED framework invokes loadInBackground |
| AppListLoader.deliverResult | REACHABLE | | Framework calls after loadInBackground completes | SRC AppListLoader.java:96-112 method |
| AppListLoader.onStartLoading | REACHABLE | | Loader framework calls onStartLoading | SRC AppListLoader.java:114-133 method |
| AppListLoader.onStopLoading | UNREACHABLE | framework_never_calls | Fragment retains instance so loader persists, not stopped | SRC AppsListFragment.java:80 setRetainInstance(true); SRC AppListLoader.java:138-140 method |
| AppListLoader.onCanceled | UNREACHABLE | framework_never_calls | Load completes normally, not canceled | SRC AppListLoader.java:143-146 method |
| AppListLoader.onReset | UNREACHABLE | framework_never_calls | Loader not reset due to retained instance | SRC AppsListFragment.java:80 setRetainInstance(true); SRC AppListLoader.java:148-161 method |
| AppListLoader.onReleaseResources | UNREACHABLE | no_trigger_in_app | Private helper called from unreachable methods (onCanceled, onReset, deliverResult), body is empty | SRC AppListLoader.java:167-170 private void onReleaseResources() { /* empty */ } |
| AppListLoader$AppsDataPair.<init> | REACHABLE | | Instantiated in loadInBackground | SRC AppListLoader.java:52,56 new AppsDataPair(...) |
| AppsAdapter.<init> | REACHABLE | | Instantiated in AppsListFragment.onActivityCreated | SRC AppsListFragment.java:101 adapter = new AppsAdapter(...) |
| AppsAdapter.setData | REACHABLE | | Called from onLoadFinished | SRC AppsListFragment.java:168 adapter.setData(data.first) |
| AppsAdapter.getView | REACHABLE | | Framework calls getView when ListView renders | INFERRED ListView framework calls getView |
| AppsAdapter.showPopup | REACHABLE | | Called from getView | SRC AppsAdapter.java:129 showPopup(holder.about, rowItem) |
| AppsAdapter.lambda$getView$0 | REACHABLE | | Lambda set as OnClickListener in getView | SRC AppsAdapter.java:145 holder.rl.setOnClickListener(p1 -> {...}) |
| AppsAdapter.lambda$showPopup$4 | REACHABLE | | Lambda set as OnClickListener in showPopup | SRC AppsAdapter.java:168 v.setOnClickListener(view -> {...}) |
| AppsAdapter.lambda$null$1 | REACHABLE | | Nested lambda for MaterialDialog onNegative | SRC AppsAdapter.java:203 .onNegative(((dialog, which) -> dialog.cancel())) |
| AppsAdapter.lambda$null$2 | REACHABLE | | Nested lambda for MaterialDialog onPositive | SRC AppsAdapter.java:204 .onPositive(((dialog, which) -> {...})) |
| AppsAdapter.lambda$null$3 | REACHABLE | | Lambda in showPopup menu uninstall case | SRC AppsAdapter.java:220 in else: app.unin(rowItem.packageName) |
| AppsAdapterPreloadModel.<init> | REACHABLE | | Instantiated in AppsListFragment.onActivityCreated | SRC AppsListFragment.java:96 modelProvider = new AppsAdapterPreloadModel(app) |
| AppsAdapterPreloadModel.setItemList | REACHABLE | | Called from onLoadFinished | SRC AppsListFragment.java:169 modelProvider.setItemList(data.second) |
| AppsAdapterPreloadModel.getPreloadItems | REACHABLE | | Glide ListPreloader calls during scroll | SRC AppsListFragment.java:98-99,103 ListPreloader setup with modelProvider; INFERRED Glide calls method |
| AppsAdapterPreloadModel.getPreloadRequestBuilder | REACHABLE | | Glide ListPreloader calls to build requests | SRC AppsListFragment.java:98-99,103 ListPreloader setup; INFERRED Glide calls method |
| AppsAdapterPreloadModel.loadApkImage | REACHABLE | | Called from AppsAdapter.getView | SRC AppsAdapter.java:124 modelProvider.loadApkImage(rowItem.path, holder.apkIcon) |
| AsyncTaskResult.<init> | REACHABLE | | Instantiated in multiple AsyncTask subclasses | SRC CompressedHelperTask.java:58,60; SRC GetSshHostFingerprintTask.java:87,97,101; SRC SshAuthenticationTask.java:127,147,152,155,158 |
| BookSorter.<init> | REACHABLE | | Instantiated for Collections.sort in multiple places | SRC Drawer.java:356 new BookSorter(); SRC SftpConnectDialog.java:382; SRC MainActivity.java:1707; SRC DataUtils.java:315 |
| BookSorter.compare | REACHABLE | | Collections.sort calls compare | SRC Drawer.java:356 Collections.sort(..., new BookSorter()); INFERRED sort calls compare |
| AppTheme.<clinit> | UNREACHABLE | framework_never_calls | Enum static initializer, called when enum class loaded | Enum initialization automatic |
| AppTheme.<init> | UNREACHABLE | framework_never_calls | Private enum constructor called during enum initialization | SRC AppTheme.java:24 private constructor |
| AppTheme.getTheme | REACHABLE | | Called from AppThemeManager constructor | SRC AppThemeManager.java:17 AppTheme.getTheme(Integer.parseInt(themeId)) |
| AppTheme.getMaterialDialogTheme | REACHABLE | | Called when creating MaterialDialog instances | SRC GeneralDialogCreation.java:131,157,194,387,467,624,etc multiple call sites |
| AppTheme.getSimpleTheme | REACHABLE | | Called from AppThemeManager | SRC AppThemeManager.java:17 .getSimpleTheme(); SRC AppThemeManager.java:24 return appTheme.getSimpleTheme() |
| AppTheme.getId | REACHABLE | | Called from AppThemeManager.setAppTheme | SRC AppThemeManager.java:33 Integer.toString(appTheme.getId()) |
| AppThemeManager.<init> | REACHABLE | | Instantiated by UtilitiesProvider | SRC UtilitiesProvider.java:25 appThemeManager = new AppThemeManager(sharedPreferences) |
| AppThemeManager.getAppTheme | REACHABLE | | Called throughout app to get current theme | Used in AppsListFragment.java:91, AppsAdapter.java and many others |
| AppThemeManager.setAppTheme | REACHABLE | | Called to change app theme | SRC AppThemeManager.java:31-35 method |
| ArchivePasswordCache.<init> | REACHABLE | | Private constructor called from singleton holder | SRC ArchivePasswordCache.java:54,61 private constructor, holder creates INSTANCE |
| ArchivePasswordCache.getInstance | REACHABLE | | Called to access singleton | SRC SevenZipHelperTask.java:68,103,111; SRC SevenZipExtractor.java:49; SRC ZipExtractor.java:59,102; SRC ExtractService.java:330,337 |
| ArchivePasswordCache.get | REACHABLE | | Called after getInstance to retrieve password | SRC SevenZipHelperTask.java:69 .getInstance().get(filePath) |
| ArchivePasswordCache.put | REACHABLE | | Called to store password in cache | SRC SevenZipHelperTask.java:111 .getInstance().put(filePath, password); SRC ExtractService.java:337 |
| ArchivePasswordCache.remove | REACHABLE | | Called to remove invalid password | SRC SevenZipHelperTask.java:103 .getInstance().remove(filePath); SRC ExtractService.java:330 |
| ArchivePasswordCache.containsKey | REACHABLE | | Called to check if password cached | SRC SevenZipHelperTask.java:68 .getInstance().containsKey(filePath); SRC SevenZipExtractor.java:49; SRC ZipExtractor.java:59,102 |
| ArchivePasswordCache.clear | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep -rn "ArchivePasswordCache.*\\.clear" app/src shows no matches |
| ArchivePasswordCache.containsValue | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep shows no matches |
| ArchivePasswordCache.entrySet | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep shows no matches |
| ArchivePasswordCache.equals | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep shows no matches |
| ArchivePasswordCache.hashCode | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep shows no matches |
| ArchivePasswordCache.isEmpty | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep shows no matches |
| ArchivePasswordCache.keySet | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep shows no matches |
| ArchivePasswordCache.putAll | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep shows no matches |
| ArchivePasswordCache.size | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep shows no matches |
| ArchivePasswordCache.toString | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep shows no matches |
| ArchivePasswordCache.values | UNREACHABLE | no_trigger_in_app | Map method not called by app | grep shows no matches |
| ArchivePasswordCache$ArchivePasswordCacheHolder.<clinit> | REACHABLE | | Static initializer triggered when holder accessed | SRC ArchivePasswordCache.java:67 return ArchivePasswordCacheHolder.INSTANCE; INFERRED static init |
| ArchivePasswordCache$ArchivePasswordCacheHolder.<init> | UNREACHABLE | no_trigger_in_app | Private inner class constructor, not explicitly called, only static INSTANCE field used | SRC ArchivePasswordCache.java:60-62 static class with static field |
| Archive.<init> | UNREACHABLE | no_trigger_in_app | sevenz library class not called by app, app uses junrar.Archive for RAR and SevenZFile for 7z | grep -rn "sevenz.Archive" app/src returns no matches |
| Archive.lengthOf | UNREACHABLE | no_trigger_in_app | sevenz library method, Archive class not used | grep shows no sevenz.Archive usage |
| Archive.toString | UNREACHABLE | no_trigger_in_app | sevenz library method, Archive class not used | grep shows no sevenz.Archive usage |
| BindPair.<init> | UNREACHABLE | no_trigger_in_app | sevenz library class not called by app | grep -rn "BindPair" app/src returns no matches |
| BindPair.toString | UNREACHABLE | no_trigger_in_app | sevenz library method, BindPair class not used | grep shows no BindPair usage |

STATUS: DONE 21:17
