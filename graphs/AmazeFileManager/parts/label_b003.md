STATUS: RUNNING 21:18

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| AppTheme.\<clinit\> | REACHABLE | ENUM_INIT | Enum static initializer creates constants | SRC AppTheme.java:10-14 |
| AppTheme.\<init\> | REACHABLE | ENUM_CTOR | Enum constructor called by \<clinit\> and getTheme() | SRC AppTheme.java:22-24 |
| AppTheme.getTheme | REACHABLE | CALL | Static method called by UtilitiesProvider.getAppTheme() | SRC AppTheme.java:29-46, UtilitiesProvider.java:28-30 |
| AppTheme.getMaterialDialogTheme | REACHABLE | CALL | Called by many dialogs via themedActivity.getAppTheme().getMaterialDialogTheme() | SRC AppTheme.java:48-63, GeneralDialogCreation.java:131 |
| AppTheme.getSimpleTheme | REACHABLE | CALL | Called by AppThemeManager constructor and getAppTheme() | SRC AppTheme.java:74-88, AppThemeManager.java:16 |
| AppTheme.getId | REACHABLE | CALL | Called by AppThemeManager.setAppTheme() via getId() | SRC AppTheme.java:90-92, AppThemeManager.java:34 |
| AppThemeManager.\<init\> | REACHABLE | CALL | Constructor called by UtilitiesProvider.\<init\> | SRC AppThemeManager.java:14-18, UtilitiesProvider.java:25 |
| AppThemeManager.getAppTheme | REACHABLE | CALL | Called by UtilitiesProvider.getAppTheme() wrapper | SRC AppThemeManager.java:23-25, UtilitiesProvider.java:28-30 |
| AppThemeManager.setAppTheme | REACHABLE | CALL | Called when user changes theme in preferences | SRC AppThemeManager.java:31-35, PreferencesConstants delegation |
| AppsAdapter.\<init\> | REACHABLE | CALL | Constructor called by AppsListFragment.onActivityCreated() | SRC AppsAdapter.java:63-90, AppsListFragment.java:100-103 |
| AppsAdapter.getView | REACHABLE | LIFECYCLE | ArrayAdapter lifecycle method, called by ListView for each row | SRC AppsAdapter.java:95-138 |
| AppsAdapter.lambda$getView$0 | REACHABLE | LAMBDA | Click listener on app item row | SRC AppsAdapter.java:129-135 |
| AppsAdapter.lambda$null$1 | REACHABLE | LAMBDA | Color filter lambda in getView | SRC AppsAdapter.java:119-120 |
| AppsAdapter.lambda$null$2 | REACHABLE | LAMBDA | Marquee animation delay lambda | SRC AppsAdapter.java:124-128 |
| AppsAdapter.lambda$null$3 | REACHABLE | LAMBDA | Ellipsize setting lambda | SRC AppsAdapter.java:123-125 |
| AppsAdapter.lambda$showPopup$4 | REACHABLE | LAMBDA | PopupMenu item click listeners | SRC AppsAdapter.java:140-185 |
| AppsAdapter.setData | REACHABLE | CALL | Called by AppsListFragment.onLoadFinished() | SRC AppsAdapter.java:91-100, AppsListFragment.java:165 |
| AppsAdapter.showPopup | REACHABLE | CALL | Called by AppsAdapter.getView() | SRC AppsAdapter.java:139-185, AppsAdapter.java:120 |
| AppsAdapterPreloadModel.\<init\> | REACHABLE | CALL | Constructor called by AppsListFragment.onActivityCreated() | SRC AppsAdapterPreloadModel.java:25-28, AppsListFragment.java:96 |
| AppsAdapterPreloadModel.getPreloadItems | REACHABLE | FRAMEWORK | ListPreloader.PreloadModelProvider interface method, called by Glide | SRC AppsAdapterPreloadModel.java:35-40 |
| AppsAdapterPreloadModel.getPreloadRequestBuilder | REACHABLE | FRAMEWORK | ListPreloader.PreloadModelProvider interface method, called by Glide | SRC AppsAdapterPreloadModel.java:42-45 |
| AppsAdapterPreloadModel.loadApkImage | REACHABLE | CALL | Called by AppsAdapter.getView() to load icon | SRC AppsAdapterPreloadModel.java:47-49, AppsAdapter.java:115 |
| AppsAdapterPreloadModel.setItemList | REACHABLE | CALL | Called by AppsListFragment.onLoadFinished() | SRC AppsAdapterPreloadModel.java:30-32, AppsListFragment.java:167 |
| AppsListFragment.\<init\> | REACHABLE | CALL | Fragment constructor, called from Drawer navigation | SRC AppsListFragment.java:50, Drawer.java:421 (via menu item click) |
| AppsListFragment.getSortModes | REACHABLE | CALL | Called by AppsListFragment.onActivityCreated() | SRC AppsListFragment.java:155-165, AppsListFragment.java:91 |
| AppsListFragment.onActivityCreated | REACHABLE | LIFECYCLE | Fragment lifecycle, called after onViewCreated | SRC AppsListFragment.java:71-109 |
| AppsListFragment.onCreate | REACHABLE | LIFECYCLE | Fragment lifecycle, first lifecycle method | SRC AppsListFragment.java:65-70 |
| AppsListFragment.onCreateLoader | REACHABLE | CALLBACK | LoaderManager.LoaderCallbacks interface method | SRC AppsListFragment.java:167-169 |
| AppsListFragment.onLoadFinished | REACHABLE | CALLBACK | LoaderManager.LoaderCallbacks interface method, called when data loads | SRC AppsListFragment.java:171-183 |
| AppsListFragment.onLoaderReset | REACHABLE | CALLBACK | LoaderManager.LoaderCallbacks interface method | SRC AppsListFragment.java:185-187 |
| AppsListFragment.onSaveInstanceState | REACHABLE | LIFECYCLE | Fragment lifecycle method for state saving | SRC AppsListFragment.java:111-121 |
| AppsListFragment.unin | REACHABLE | CALL | Called by AppsAdapter lambda for uninstall action | SRC AppsListFragment.java:123-131, AppsAdapter.java:176 |
| Archive.\<init\> | UNREACHABLE | no_trigger_in_app | Private Archive class within apache commons 7z library; only used by SevenZFile (library code) | SRC Archive.java:43-48 |
| Archive.lengthOf | UNREACHABLE | no_trigger_in_app | Private static helper only called by Archive.toString() for toString() debug output | SRC Archive.java:36-53 |
| Archive.toString | UNREACHABLE | no_trigger_in_app | toString() implementation for library debugging; app never calls toString on Archive | SRC Archive.java:36-41 |

STATUS: DONE 21:18
