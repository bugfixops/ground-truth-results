| method | verdict | edges or kind | source file:lines | confirmed_by |
|---|---|---|---|---|
| PathSwitchPreference.onBindView | REACHABLE | FoldersPref.onCreate -CALL-> PathSwitchPreference.<init> -FRAMEWORK-> onCreateView -FRAMEWORK-> onBindView | FoldersPref.java:59,65; PathSwitchPreference.java:26-39 | SOURCE |
| PathSwitchPreference.onCreateView | REACHABLE | PathSwitchPreference.<init> -FRAMEWORK-> onCreateView | PathSwitchPreference.java:26-29 | SOURCE |
| PathSwitchPreference.setListener | REACHABLE | PathSwitchPreference.onBindView -CALL-> setListener | PathSwitchPreference.java:34-35 | SOURCE |
| SelectedColorsPreference.<init> | REACHABLE | ColorPref.loadSection1 -FRAMEWORK-> SelectedColorsPreference.<init> (XML inflate of ColorPickerDialog subclass) | ColorPref.java:219; conficolor_prefs.xml:3-5; SelectedColorsPreference.java:27-29 | SOURCE |
| SelectedColorsPreference.onBindView | REACHABLE | SelectedColorsPreference.onCreateView -FRAMEWORK-> onBindView | SelectedColorsPreference.java:38-46 | SOURCE |
| SelectedColorsPreference.onCreateView | REACHABLE | SelectedColorsPreference.<init> -FRAMEWORK-> onCreateView | SelectedColorsPreference.java:31-35 | SOURCE |
| AnimUtils.getFastOutSlowInInterpolator | REACHABLE | MainActivity.onCreate -FRAMEWORK-> Indicator.<init>(Context,AttributeSet) -CALL-> Indicator.<init>(Context,AttributeSet,int) -CALL-> AnimUtils.getFastOutSlowInInterpolator | MainActivity.java:289; main_toolbar.xml; Indicator.java:119-121,153 | SOURCE |
| DataUtils.contains(String,ArrayList) | UNREACHABLE | no_trigger_in_app | DataUtils.java:109-111,165-173 | SOURCE |
| DatapointParcelable.<init>(Parcel) | UNREACHABLE | no_trigger_in_app | DatapointParcelable.java:117-126 | SOURCE |
| DatapointParcelable$1.createFromParcel | UNREACHABLE | no_trigger_in_app | DatapointParcelable.java:128-133 | SOURCE |
| DatapointParcelable$1.newArray | UNREACHABLE | no_trigger_in_app | DatapointParcelable.java:134-137 | SOURCE |
| InterestingConfigChange.recycle | REACHABLE | AppListLoader.onStartLoading -LIFECYCLE-> onStopLoading -CALL-> InterestingConfigChange.recycle | AppListLoader.java:112,131,160 | SOURCE |
| LruBitmapCache.getBitmap | REACHABLE | Drawer.<init> -CALL-> AppConfig.getImageLoader -CALL-> LruBitmapCache.<init>() -FRAMEWORK-> getBitmap | Drawer.java:156; AppConfig.java:223; LruBitmapCache.java:30-33 | SOURCE (framework hop INFERRED, Volley lib not read) |
| LruBitmapCache.putBitmap | REACHABLE | LruBitmapCache.<init>() -FRAMEWORK-> putBitmap | LruBitmapCache.java:35-38 | SOURCE (framework hop INFERRED, Volley lib not read) |
| LruBitmapCache.sizeOf | REACHABLE | LruBitmapCache.<init>() -FRAMEWORK-> sizeOf | LruBitmapCache.java:40-44 | SOURCE (framework hop INFERRED, LruCache lib not read) |
| MainActivityHelper.isNewDirectoryRecursive | UNREACHABLE | no_trigger_in_app | MainActivityHelper.java:644-646 | SOURCE |
| StreamSource.read() | UNREACHABLE | no_trigger_in_app | StreamSource.java:68-73; StreamServer.java:672 | SOURCE |
| StreamSource.read(byte[],int,int) | REACHABLE | StreamServer$HTTPSession.handleResponse -FRAMEWORK-> Streamer.serve -CALL-> StreamSource.<init>; StreamServer$HTTPSession.sendResponse -CALL-> StreamSource.read(byte[],int,int) | StreamServer.java:327,672; Streamer.java:63,101; StreamSource.java:75-79 | SOURCE (InputStream.read(byte[]) JDK hop INFERRED) |
| TinyDB.putBooleanArray | REACHABLE | PreferencesActivity.selectItem -CALL-> QuickAccessPref.<init> -LIFECYCLE-> onCreate -FRAMEWORK-> onPreferenceClick -CALL-> TinyDB.putBooleanArray | PreferencesActivity.java:264; QuickAccessPref.java:52-54,60 | SOURCE |
| Utils.getViewRawY | REACHABLE | FastScroller.getRelativeTouchPosition -CALL-> Utils.getViewRawY | FastScroller.java:147 | SOURCE |
| RandomAccessStream.availableExact | UNREACHABLE | no_trigger_in_app | RandomAccessStream.java:37-39; StreamServer.java:668,673; CloudStreamServer.java:837,842 (all commented out) | SOURCE |
