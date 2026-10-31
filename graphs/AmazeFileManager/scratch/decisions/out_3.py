e('FoldersPref.onCreate', 'PathSwitchPreference.<init>', 'CALL', 'FoldersPref constructs a PathSwitchPreference per bookmark and adds it to the preference screen', evidence='SRC fragments/preference_fragments/FoldersPref.java:59 PathSwitchPreference p = new PathSwitchPreference(getActivity()); line 65 getPreferenceScreen().addPreference(p)')

e('PathSwitchPreference.<init>', 'PathSwitchPreference.onCreateView', 'FRAMEWORK', 'Android Preference framework calls onCreateView to build the preference view once it is added to the screen', evidence='SRC ui/views/preference/PathSwitchPreference.java:26-29 overrides Preference.onCreateView(ViewGroup)')

e('PathSwitchPreference.onCreateView', 'PathSwitchPreference.onBindView', 'FRAMEWORK', 'Preference framework calls onBindView after onCreateView to bind preference view data', evidence='SRC ui/views/preference/PathSwitchPreference.java:32-39 overrides Preference.onBindView(View)')

e('PathSwitchPreference.onBindView', 'PathSwitchPreference.setListener', 'CALL', 'onBindView calls setListener(view, R.id.edit, EDIT) and setListener(view, R.id.delete, DELETE)', evidence='SRC ui/views/preference/PathSwitchPreference.java:34-35')

e('ColorPref.loadSection1', 'SelectedColorsPreference.<init>', 'FRAMEWORK', 'loadSection1 calls addPreferencesFromResource(R.xml.conficolor_prefs), which XML-inflates ColorPickerDialog (a SelectedColorsPreference subclass), invoking the (Context,AttributeSet) constructor', evidence='SRC fragments/preference_fragments/ColorPref.java:219 addPreferencesFromResource(R.xml.conficolor_prefs); res/xml/conficolor_prefs.xml:3-5 declares com.amaze.filemanager.ui.dialogs.ColorPickerDialog; ui/views/preference/SelectedColorsPreference.java:27-29 constructor')

e('SelectedColorsPreference.<init>', 'SelectedColorsPreference.onCreateView', 'FRAMEWORK', 'Android Preference framework calls onCreateView to build the preference view', evidence='SRC ui/views/preference/SelectedColorsPreference.java:31-35 overrides Preference.onCreateView(ViewGroup)')

e('SelectedColorsPreference.onCreateView', 'SelectedColorsPreference.onBindView', 'FRAMEWORK', 'Preference framework calls onBindView after onCreateView to bind preference view data', evidence='SRC ui/views/preference/SelectedColorsPreference.java:38-46 overrides Preference.onBindView(View)')

e('MainActivity.onCreate', 'Indicator.<init>(Context,AttributeSet)', 'FRAMEWORK', 'setContentView(R.layout.main_toolbar) inflates the layout containing an Indicator view, framework instantiates it via the 2-arg XML constructor', evidence='SRC activities/MainActivity.java:289 setContentView(R.layout.main_toolbar); res/layout-v21/main_toolbar.xml declares com.amaze.filemanager.ui.views.Indicator')

e('Indicator.<init>(Context,AttributeSet)', 'Indicator.<init>(Context,AttributeSet,int)', 'CALL', 'this(context, attrs, 0) constructor delegation', evidence='SRC ui/views/Indicator.java:119-121')

e('Indicator.<init>(Context,AttributeSet,int)', 'AnimUtils.getFastOutSlowInInterpolator', 'CALL', 'constructor initializes interpolator field', evidence='SRC ui/views/Indicator.java:153 interpolator = AnimUtils.getFastOutSlowInInterpolator(context);')

e('AppListLoader.onStartLoading', 'AppListLoader.onStopLoading', 'LIFECYCLE', 'Standard AsyncTaskLoader lifecycle: framework calls onStopLoading when the loader is stopped (e.g. fragment paused/reset) after it has been started', evidence='SRC asynchronous/loaders/AppListLoader.java:112 protected void onStartLoading(); line 131 protected void onStopLoading(), both overriding AsyncTaskLoader')

e('AppListLoader.onStopLoading', 'InterestingConfigChange.recycle', 'CALL', 'onStopLoading calls InterestingConfigChange.recycle() to reset static config-tracking state', evidence='SRC asynchronous/loaders/AppListLoader.java:160 InterestingConfigChange.recycle();')

e('Drawer.<init>', 'AppConfig.getImageLoader', 'CALL', 'Drawer constructor obtains the shared ImageLoader', evidence='SRC ui/views/drawer/Drawer.java:156 mImageLoader = AppConfig.getInstance().getImageLoader();')

e('AppConfig.getImageLoader', 'LruBitmapCache.<init>()', 'CALL', 'getImageLoader lazily constructs an ImageLoader using a no-arg LruBitmapCache as its ImageCache', evidence='SRC utils/application/AppConfig.java:223 this.mImageLoader = new ImageLoader(mRequestQueue, new LruBitmapCache());')

e('LruBitmapCache.<init>()', 'LruBitmapCache.getBitmap', 'FRAMEWORK', 'Volley ImageLoader (library) calls ImageCache.getBitmap(url) to check the cache before issuing a network request; library code not read', evidence='SRC utils/LruBitmapCache.java:30-33 implements ImageLoader.ImageCache; INFERRED com.android.volley.toolbox.ImageLoader library calls getBitmap, library source not read')

e('LruBitmapCache.<init>()', 'LruBitmapCache.putBitmap', 'FRAMEWORK', 'Volley ImageLoader (library) calls ImageCache.putBitmap(url,bitmap) after a successful image load; library code not read', evidence='SRC utils/LruBitmapCache.java:35-38 implements ImageLoader.ImageCache; INFERRED com.android.volley.toolbox.ImageLoader library calls putBitmap, library source not read')

e('LruBitmapCache.<init>()', 'LruBitmapCache.sizeOf', 'FRAMEWORK', 'android.util.LruCache (framework) calls sizeOf(key,value) internally whenever put() is invoked', evidence='SRC utils/LruBitmapCache.java:40-44 overrides LruCache.sizeOf; INFERRED android.util.LruCache.put() framework code not read, documented to call sizeOf')

e('StreamServer$HTTPSession.handleResponse', 'Streamer.serve', 'FRAMEWORK', 'handleResponse calls the abstract serve() method; at runtime the server instance is a Streamer so this dispatches to Streamer.serve override', evidence='SRC SmbStreamer/StreamServer.java:327 Response r = serve(uri, method, header, parms, files); SmbStreamer/Streamer.java:63 public Response serve(...) overrides StreamServer.serve')

e('Streamer.serve', 'StreamSource.<init>', 'CALL', 'Streamer.serve constructs a StreamSource for the requested SMB file', evidence='SRC SmbStreamer/Streamer.java:101 final StreamSource source = new StreamSource(sourceFile, length);')

e('StreamServer$HTTPSession.sendResponse', 'StreamSource.read(byte[],int,int)', 'CALL', 'sendResponse loops calling data.read(buff); InputStream.read(byte[]) (JDK, not read) dispatches to the overridden 3-arg read', evidence='SRC SmbStreamer/StreamServer.java:672 while ((read = data.read(buff)) > 0); SmbStreamer/StreamSource.java:75-79 overrides read(byte[],int,int); INFERRED java.io.InputStream.read(byte[]) JDK source not read, documented to call read(b,0,b.length)')

e('PreferencesActivity.selectItem', 'QuickAccessPref.<init>', 'CALL', 'selectItem creates QuickAccessPref for the quick-access preference section', evidence='SRC activities/PreferencesActivity.java:264 loadPrefFragment(new QuickAccessPref(), R.string.sidebar_quick_access_title);')

e('QuickAccessPref.<init>', 'QuickAccessPref.onCreate', 'LIFECYCLE', 'PreferenceFragment.onCreate called by framework after the fragment transaction', evidence='SRC activities/PreferencesActivity.java:264; FW-SRC PreferenceFragment lifecycle calls onCreate')

e('QuickAccessPref.onCreate', 'QuickAccessPref.onPreferenceClick', 'FRAMEWORK', 'onCreate registers this fragment as OnPreferenceClickListener for every preference row; framework calls onPreferenceClick when a row is tapped', evidence='SRC fragments/preference_fragments/QuickAccessPref.java:52-54 getPreferenceScreen().getPreference(i).setOnPreferenceClickListener(this);')

e('QuickAccessPref.onPreferenceClick', 'TinyDB.putBooleanArray', 'CALL', 'onPreferenceClick saves the updated quick-access boolean array', evidence='SRC fragments/preference_fragments/QuickAccessPref.java:60 TinyDB.putBooleanArray(preferences, KEY, currentValue);')

e('FastScroller.getRelativeTouchPosition', 'Utils.getViewRawY', 'CALL', 'getRelativeTouchPosition computes touch position using the handle view raw Y coordinate', evidence='SRC ui/views/FastScroller.java:147 float yInParent = event.getRawY() - Utils.getViewRawY(handle);')

UNREACHABLE['DataUtils.contains(String,ArrayList)'] = ('no_trigger_in_app', 'Package-private overload int contains(String, ArrayList<String[]>) has zero call sites anywhere in DataUtils.java or the app; both live callers (containsServer(String[]) and containsBooks(String[])) pass a String[] first argument which resolves to the other overload contains(String[], ArrayList); the one line that would call the String overload (containsAccounts(CloudEntry)) is commented out', 'SRC utils/DataUtils.java:109-111 commented-out method containing the only textual call to contains(a, accounts); line 165-173 defines contains(String,ArrayList); grep -rn "contains(" over DataUtils.java shows only the String[] overload is actually invoked live', 'SOURCE')

UNREACHABLE['DatapointParcelable.<init>(Parcel)'] = ('no_trigger_in_app', 'DatapointParcelable is only ever passed between app components as a plain Java object (method params/fields on AbstractProgressiveService, ProcessViewerFragment callbacks); grep over the app finds no putParcelable/putExtra/getParcelable call for DatapointParcelable, so it is never marshalled into a Parcel and this Parcel-reading constructor is never invoked', 'SRC utils/DatapointParcelable.java:117-126 constructor reads fields from Parcel; grep -rn DatapointParcelable across app/src/main/java shows only in-memory usage (AbstractProgressiveService, ExtractService, CopyService, DecryptService, ZipService, EncryptService, ProcessViewerFragment), no Parcel/Bundle/Intent putParcelable or getParcelable calls', 'SOURCE')

UNREACHABLE['DatapointParcelable$1.createFromParcel'] = ('no_trigger_in_app', 'CREATOR.createFromParcel is only invoked by the framework when a DatapointParcelable is read back out of a Parcel/Bundle/Intent via getParcelable(ArrayList); no such call exists for DatapointParcelable anywhere in the app', 'SRC utils/DatapointParcelable.java:128-133 CREATOR anonymous class createFromParcel; grep -rn DatapointParcelable across app/src/main/java shows no getParcelable/getParcelableArrayList call for this class', 'SOURCE')

UNREACHABLE['DatapointParcelable$1.newArray'] = ('no_trigger_in_app', 'CREATOR.newArray is only invoked by the framework when unparceling a DatapointParcelable[] array from a Parcel; no DatapointParcelable is ever put into or read from a Parcel/Bundle/Intent in the app', 'SRC utils/DatapointParcelable.java:134-137 CREATOR anonymous class newArray; grep -rn DatapointParcelable across app/src/main/java shows no array unparceling call for this class', 'SOURCE')

UNREACHABLE['MainActivityHelper.isNewDirectoryRecursive'] = ('no_trigger_in_app', 'Public static utility method defined but never called anywhere else in the app source', 'SRC utils/MainActivityHelper.java:644-646 public static boolean isNewDirectoryRecursive(HybridFile file); grep -rn isNewDirectoryRecursive across app/src/main/java shows only this declaration, no call sites', 'SOURCE')

UNREACHABLE['StreamSource.read()'] = ('no_trigger_in_app', 'The no-arg single-byte read() override is never called from app code; the only live read path on a StreamSource (StreamServer.sendResponse data.read(buff)) dispatches via InputStream.read(byte[]) straight to the 3-arg read(byte[],int,int) override which independently reads from the underlying SMB input stream, never delegating to read()', 'SRC SmbStreamer/StreamSource.java:68-73 defines read(); SmbStreamer/StreamServer.java:672 while ((read = data.read(buff)) > 0) is the only call site touching a StreamSource read method and it targets read(byte[],int,int); grep -rn "\\.read()" across app/src/main/java shows no call site on a StreamSource/RandomAccessStream-typed variable', 'SOURCE')

UNREACHABLE['RandomAccessStream.availableExact'] = ('no_trigger_in_app', 'availableExact() is defined but every call site in the app is commented out', 'SRC utils/streams/RandomAccessStream.java:37-39 defines availableExact(); SmbStreamer/StreamServer.java:668,673 and utils/cloud/CloudStreamServer.java:837,842 are the only occurrences of availableExact( outside its own definition and all four are inside // line comments (//long pending = data.availableExact(); and //if(...)...data.availableExact()); grep -rn availableExact across app/src/main/java confirms no live (non-comment) call site', 'SOURCE')
