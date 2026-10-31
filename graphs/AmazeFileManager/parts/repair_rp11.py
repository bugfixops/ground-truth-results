# repair batch 11 - TabFragment, SmbSearchDialog$ListViewAdapter, RoundedImageView, SelectedColorsPreference, ZipService$CompressAsyncTask, SevenZOutputFile$OutputStreamWrapper

# TabFragment.onDestroyView - Fragment lifecycle method called by framework
e('TabFragment.onCreateView', 'TabFragment.onDestroyView', 'LIFECYCLE',
  'Fragment lifecycle: onDestroyView called by framework when view is destroyed',
  evidence='FW-SRC android-8.1.0_r1/core/java/android/app/Fragment.java:2744-2758 performDestroyView() calls onDestroyView(); FragmentManager.java:1356 calls f.performDestroyView() during fragment teardown')

# TabFragment.onPageScrollStateChanged - ViewPager.OnPageChangeListener interface method
e('TabFragment.onCreateView', 'TabFragment.onPageScrollStateChanged', 'FRAMEWORK',
  'ViewPager calls OnPageChangeListener.onPageScrollStateChanged on registered listeners',
  evidence='SRC TabFragment.java:45 implements ViewPager.OnPageChangeListener; SRC TabFragment.java:99 mViewPager.addOnPageChangeListener(this) registers TabFragment as listener; ViewPager framework calls this method')

# TabFragment.onPageScrolled - ViewPager.OnPageChangeListener interface method
e('TabFragment.onCreateView', 'TabFragment.onPageScrolled', 'FRAMEWORK',
  'ViewPager calls OnPageChangeListener.onPageScrolled on registered listeners during scroll',
  evidence='SRC TabFragment.java:45 implements ViewPager.OnPageChangeListener; SRC TabFragment.java:99 mViewPager.addOnPageChangeListener(this) registers TabFragment as listener; ViewPager framework calls this method')

# TabFragment.onPageSelected - ViewPager.OnPageChangeListener interface method (already has edges, add more)
e('TabFragment.onPageSelected', 'BottomBar.updatePath', 'CALL',
  'When page selected, updates bottom bar path',
  evidence='SRC TabFragment.java:287 mainActivity.getAppbar().getBottomBar().updatePath(ma.getCurrentPath(), ...)')

# TabFragment.onSaveInstanceState - Fragment lifecycle method  
e('TabFragment.onCreateView', 'TabFragment.onSaveInstanceState', 'LIFECYCLE',
  'Fragment lifecycle: framework calls onSaveInstanceState to save instance state',
  evidence='SRC TabFragment.java:260 overrides onSaveInstanceState; framework calls this on Fragment instances during configuration changes or process death')

# TabFragment.parsePathForName - UNREACHABLE, no callers in app
UNREACHABLE['TabFragment.parsePathForName'] = ('no_trigger_in_app', 'parsePathForName is never called in the app; grep finds no callers', 'SRC TabFragment.java:243-255 defines parsePathForName but no app code calls it; grep -rn "\\.parsePathForName" in app/src/main/java finds no calls', 'SOURCE')

# TabFragment.parseSmbPath - UNREACHABLE, only called from unreachable parsePathForName
UNREACHABLE['TabFragment.parseSmbPath'] = ('no_trigger_in_app', 'parseSmbPath is only called by parsePathForName which itself is never called', 'SRC TabFragment.java:237-241 defines parseSmbPath; TabFragment.java:248 shows only call is from parsePathForName; parsePathForName has no callers (see above)', 'SOURCE')

# SmbSearchDialog$ListViewAdapter.<init> - RecyclerView.Adapter constructor
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.<init>', 'CALL',
  'SmbSearchDialog creates ListViewAdapter instance',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:78 listViewAdapter = new ListViewAdapter(getActivity(), computers)')

# SmbSearchDialog$ListViewAdapter.getItemCount - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.getItemCount', 'FRAMEWORK',
  'RecyclerView calls getItemCount on adapter to determine number of items',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:179-181 overrides getItemCount(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.getItemId - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.getItemId', 'FRAMEWORK',
  'RecyclerView calls getItemId on adapter to get stable IDs',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:175-177 overrides getItemId(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.getItemViewType - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.getItemViewType', 'FRAMEWORK',
  'RecyclerView calls getItemViewType on adapter to determine view type',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:165-173 overrides getItemViewType(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.lambda$onBindViewHolder$0 - lambda expression
e('SmbSearchDialog$ListViewAdapter.onBindViewHolder', 'SmbSearchDialog$ListViewAdapter.lambda$onBindViewHolder$0', 'CALL',
  'onBindViewHolder sets click listener that calls lambda',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:148-158 holder.rootView.setOnClickListener lambda expression compiled to this method')

# SmbSearchDialog$ListViewAdapter.onBindViewHolder - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.onBindViewHolder', 'FRAMEWORK',
  'RecyclerView calls onBindViewHolder on adapter to bind view holders',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:144-162 overrides onBindViewHolder(); RecyclerView framework calls this on adapters')

# SmbSearchDialog$ListViewAdapter.onCreateViewHolder - RecyclerView.Adapter method
e('SmbSearchDialog.onCreateDialog', 'SmbSearchDialog$ListViewAdapter.onCreateViewHolder', 'FRAMEWORK',
  'RecyclerView calls onCreateViewHolder on adapter to create view holders',
  evidence='SRC ui/dialogs/SmbSearchDialog.java:131-142 overrides onCreateViewHolder(); RecyclerView framework calls this on adapters')

# RoundedImageView.<init> - Custom view constructor
e('S_UNKNOWN', 'RoundedImageView.<init>', 'FRAMEWORK',
  'Android framework inflates RoundedImageView from XML layouts',
  evidence='SRC ui/views/RoundedImageView.java:32-37 constructor(Context,AttributeSet); framework calls this when inflating custom views from XML')

# RoundedImageView.drawableToBitmap - internal utility method
e('RoundedImageView.onDraw', 'RoundedImageView.drawableToBitmap', 'CALL',
  'onDraw calls drawableToBitmap to convert drawable to bitmap',
  evidence='SRC ui/views/RoundedImageView.java:44 Bitmap b = drawableToBitmap(drawable)')

# RoundedImageView.drawableToBitmapRelative - internal utility method
e('RoundedImageView.onDraw', 'RoundedImageView.drawableToBitmapRelative', 'CALL',
  'onDraw calls drawableToBitmapRelative for icon images',
  evidence='SRC ui/views/RoundedImageView.java:55 Bitmap bitmap = drawableToBitmapRelative(drawable, radius)')

# RoundedImageView.getRoundedCroppedBitmap - internal utility method
e('RoundedImageView.onDraw', 'RoundedImageView.getRoundedCroppedBitmap', 'CALL',
  'onDraw calls getRoundedCroppedBitmap to create rounded bitmap',
  evidence='SRC ui/views/RoundedImageView.java:47 Bitmap roundBitmap = getRoundedCroppedBitmap(bitmap, w)')

# RoundedImageView.isImageAnIcon - internal utility method
e('RoundedImageView.onDraw', 'RoundedImageView.isImageAnIcon', 'CALL',
  'onDraw calls isImageAnIcon to check if image should be treated as icon',
  evidence='SRC ui/views/RoundedImageView.java:43 if(!isImageAnIcon())')

# RoundedImageView.onDraw - View lifecycle method
e('RoundedImageView.<init>', 'RoundedImageView.onDraw', 'FRAMEWORK',
  'Android View framework calls onDraw to render the view',
  evidence='SRC ui/views/RoundedImageView.java:40-58 overrides onDraw(Canvas); View framework calls this when view needs to be drawn')

# RoundedImageView.setBackgroundColor - UNREACHABLE, no callers
UNREACHABLE['RoundedImageView.setBackgroundColor'] = ('no_trigger_in_app', 'setBackgroundColor is never called on RoundedImageView instances in app code', 'SRC ui/views/RoundedImageView.java:65-67 defines setBackgroundColor; grep -rn "setBackgroundColor" in app finds no calls on RoundedImageView instances, only the definition', 'SOURCE')

# SelectedColorsPreference.<init> - Preference constructor called via subclass
e('S_PREFERENCES', 'SelectedColorsPreference.<init>', 'FRAMEWORK',
  'Android preference framework creates ColorPickerDialog (subclass) from XML, calling super constructor',
  evidence='SRC ui/dialogs/ColorPickerDialog.java:40 extends SelectedColorsPreference; SRC res/xml/conficolor_prefs.xml:3 declares ColorPickerDialog; framework calls constructor')

# SelectedColorsPreference.invalidateColors - called from ColorPref
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.invalidateColors', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColors on ColorPickerDialog to refresh display',
  evidence='SRC preference_fragments/ColorPref.java:265 selectedColors.invalidateColors() inside invalidateEverything(); line 262 shows selectedColors is ColorPickerDialog which extends SelectedColorsPreference')

# SelectedColorsPreference.onBindView - Preference lifecycle method
e('SelectedColorsPreference.onCreateView', 'SelectedColorsPreference.onBindView', 'FRAMEWORK',
  'Preference framework calls onBindView after onCreateView to bind data',
  evidence='SRC ui/views/preference/SelectedColorsPreference.java:38-46 overrides onBindView(); framework calls this after onCreateView')

e('SelectedColorsPreference.onBindView', 'CircularColorsView.setColors', 'CALL',
  'onBindView calls setColors to configure the colors view',
  evidence='SRC ui/views/preference/SelectedColorsPreference.java:43 colorsView.setColors(colors[0], colors[1], colors[2], colors[3])')

# SelectedColorsPreference.onCreateView - Preference lifecycle method
e('SelectedColorsPreference.<init>', 'SelectedColorsPreference.onCreateView', 'FRAMEWORK',
  'Preference framework calls onCreateView to create preference view',
  evidence='SRC ui/views/preference/SelectedColorsPreference.java:32-35 overrides onCreateView(); framework calls this on Preference instances')

# SelectedColorsPreference.setColors - called from ColorPref chain
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.setColors', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColorPreference which calls setColors on ColorPickerDialog',
  evidence='SRC preference_fragments/ColorPref.java:264 invalidateEverything calls invalidateColorPreference(selectedColors); ColorPref.java:278-280 invalidateColorPreference calls selectedColors.setColors(...); line 262 shows selectedColors is ColorPickerDialog which extends SelectedColorsPreference')

# SelectedColorsPreference.setColorsVisibility - called from ColorPref chain
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.setColorsVisibility', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColorPreference which calls setColorsVisibility',
  evidence='SRC preference_fragments/ColorPref.java:264 invalidateEverything calls invalidateColorPreference(selectedColors); ColorPref.java:275,288 invalidateColorPreference calls selectedColors.setColorsVisibility(...); line 262 shows selectedColors is ColorPickerDialog')

# SelectedColorsPreference.setDividerColor - called from ColorPref chain
e('ColorPref.invalidateEverything', 'SelectedColorsPreference.setDividerColor', 'CALL',
  'ColorPref.invalidateEverything calls invalidateColorPreference which calls setDividerColor',
  evidence='SRC preference_fragments/ColorPref.java:264 invalidateEverything calls invalidateColorPreference(selectedColors); ColorPref.java:283,285 invalidateColorPreference calls selectedColors.setDividerColor(...); line 262 shows selectedColors is ColorPickerDialog')

# ZipService$CompressAsyncTask.compressFile - internal recursive method
e('ZipService$CompressAsyncTask.execute', 'ZipService$CompressAsyncTask.compressFile', 'CALL',
  'execute method calls compressFile for each file to compress',
  evidence='SRC asynchronous/services/ZipService.java:263 compressFile(file, "") called in loop')

e('ZipService$CompressAsyncTask.compressFile', 'ZipService$CompressAsyncTask.compressFile', 'CALL',
  'compressFile recursively calls itself for directory contents',
  evidence='SRC asynchronous/services/ZipService.java:279 for loop calls compressFile(currentFile, ...) recursively')

# ZipService$CompressAsyncTask.doInBackground - AsyncTask lifecycle method
e('ZipService$CompressAsyncTask.<init>', 'ZipService$CompressAsyncTask.doInBackground', 'ASYNC',
  'AsyncTask framework calls doInBackground on worker thread',
  evidence='SRC asynchronous/services/ZipService.java:218-234 overrides doInBackground(); AsyncTask framework calls this on background thread after execute()')

# ZipService$CompressAsyncTask.execute - AsyncTask execute wrapper
e('ZipService.onStartCommand', 'ZipService$CompressAsyncTask.execute', 'CALL',
  'ZipService calls execute to start compression task',
  evidence='SRC asynchronous/services/ZipService.java:141 asyncTask.execute() starts the async task')

# ZipService$CompressAsyncTask.lambda$doInBackground$0 - lambda expression
e('ZipService$CompressAsyncTask.doInBackground', 'ZipService$CompressAsyncTask.lambda$doInBackground$0', 'CALL',
  'doInBackground sets progress listener lambda',
  evidence='SRC asynchronous/services/ZipService.java:227-228 progressHandler.setProgressListener lambda compiled to this method')

# ZipService$CompressAsyncTask.onCancelled - AsyncTask lifecycle method
e('ZipService$CompressAsyncTask.<init>', 'ZipService$CompressAsyncTask.onCancelled', 'ASYNC',
  'AsyncTask framework calls onCancelled if task is cancelled',
  evidence='SRC asynchronous/services/ZipService.java:236-242 overrides onCancelled(); AsyncTask framework calls this on UI thread if cancel() was called')

# ZipService$CompressAsyncTask.onPostExecute - AsyncTask lifecycle method
e('ZipService$CompressAsyncTask.<init>', 'ZipService$CompressAsyncTask.onPostExecute', 'ASYNC',
  'AsyncTask framework calls onPostExecute on UI thread after doInBackground',
  evidence='SRC asynchronous/services/ZipService.java:244-250 overrides onPostExecute(); AsyncTask framework calls this on UI thread after doInBackground completes')

# SevenZOutputFile$OutputStreamWrapper - library class from Apache Commons Compress
# These methods are part of the Commons Compress library bundled with the app but never used
# grep proves no app references to SevenZOutputFile or OutputStreamWrapper

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.<init>'] = ('no_trigger_in_app', 'OutputStreamWrapper is an inner class of Apache Commons Compress SevenZOutputFile library class; no app code references SevenZOutputFile or OutputStreamWrapper', 'grep -rn "SevenZOutputFile\\|OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches; library class bundled but unused', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.close'] = ('no_trigger_in_app', 'OutputStreamWrapper.close is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.flush'] = ('no_trigger_in_app', 'OutputStreamWrapper.flush is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.write(int)'] = ('no_trigger_in_app', 'OutputStreamWrapper.write(int) is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.write(byte[])'] = ('no_trigger_in_app', 'OutputStreamWrapper.write(byte[]) is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

UNREACHABLE['SevenZOutputFile$OutputStreamWrapper.write(byte[],int,int)'] = ('no_trigger_in_app', 'OutputStreamWrapper.write(byte[],int,int) is never called; class itself is never instantiated in app', 'grep -rn "OutputStreamWrapper" in final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main finds no matches', 'SOURCE')

