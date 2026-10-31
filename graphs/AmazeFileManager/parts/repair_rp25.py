# Repair batch 25: 18 methods (20 already have routes)
# Generated: 2024-10-28 21:56

# AbstractProgressiveService.getDataPackage
e('ProcessViewerFragment.onServiceBound', 'AbstractProgressiveService.getDataPackage', 'CALL',
  'ProcessViewerFragment calls getDataPackage to retrieve data package at index i for display',
  evidence='SRC ProcessViewerFragment.java:161-165 (for loop calls specificService.getDataPackage(i))')

# AbstractProgressiveService.getDataPackageSize
e('ProcessViewerFragment.onServiceBound', 'AbstractProgressiveService.getDataPackageSize', 'CALL',
  'ProcessViewerFragment calls getDataPackageSize to determine iteration limit for data packages',
  evidence='SRC ProcessViewerFragment.java:163 (for (int i = 0; i < specificService.getDataPackageSize(); i++))')

# AbstractProgressiveService.isDecryptService
e('ServiceWatcherUtil$1.run', 'AbstractProgressiveService.isDecryptService', 'CALL',
  'ServiceWatcherUtil watcher thread checks isDecryptService for workaround when written size equals total size',
  evidence='SRC ServiceWatcherUtil.java:149 (if (interactionInterface.isDecryptService() && writtenSize.equals(totalSize)))')

# AppDataParcelable.describeContents
UNREACHABLE['AppDataParcelable.describeContents'] = ('framework_never_calls',
  'Parcelable.describeContents is required by interface but returns 0 (no special objects); never called by app or framework for simple data parcelables',
  'SRC AppDataParcelable.java:32-34 (returns 0); GREP no app callers of describeContents on AppDataParcelable',
  'SOURCE')

# AppDataParcelable.writeToParcel
UNREACHABLE['AppDataParcelable.writeToParcel'] = ('framework_never_calls',
  'Parcelable.writeToParcel is required by interface but AppDataParcelable is not parceled between processes in app; only used within single process for data passing',
  'SRC AppDataParcelable.java:37-44 (writes fields to parcel); GREP no callers of writeToParcel on AppDataParcelable in app source',
  'SOURCE')

# CheckBox.clearListenerInViewGroup
e('CheckBox.onBindView', 'CheckBox.clearListenerInViewGroup', 'CALL',
  'onBindView calls clearListenerInViewGroup to remove existing listener before rebinding to avoid duplicate listeners',
  evidence='SRC CheckBox.java:21 (clearListenerInViewGroup((ViewGroup) view))')

# CheckableCircleView.onDraw
e('View.draw', 'CheckableCircleView.onDraw', 'FRAMEWORK',
  'View framework calls onDraw when view needs to render; CheckableCircleView used in layouts',
  evidence='SRC CheckableCircleView.java:42-55 (onDraw implementation); INFERRED android.view.View dispatches draw to onDraw; CheckableCircleView instantiated from app layouts')

# CircleGradientDrawable.<init>(String,AppTheme,DisplayMetrics)
UNREACHABLE['CircleGradientDrawable.<init>(String,AppTheme,DisplayMetrics)'] = ('no_trigger_in_app',
  'String color constructor overload not used; app only uses int color variant CircleGradientDrawable(int,AppTheme,DisplayMetrics)',
  'SRC CircleGradientDrawable.java:23-30 (String color constructor); GREP no callers of String-parameter constructor in app source; CircleGradientDrawable is created with int color in AppsAdapter.java',
  'SOURCE')

# CircularColorsView.<init>(Context,AttributeSet)
e('LayoutInflater.createViewFromTag', 'CircularColorsView.<init>(Context,AttributeSet)', 'FRAMEWORK',
  'LayoutInflater inflates CircularColorsView from XML layouts using (Context,AttributeSet) constructor',
  evidence='SRC CircularColorsView.java:35-38 ((Context,AttributeSet) constructor calls init); XML item_colorpicker.xml and selectedcolors_preference.xml use <com.amaze.filemanager.ui.views.CircularColorsView>; INFERRED android.view.LayoutInflater uses AttributeSet constructor for custom views in XML')

# CircularColorsView.init
e('CircularColorsView.<init>(Context)', 'CircularColorsView.init', 'CALL',
  'Constructor calls init to initialize paints and divider',
  evidence='SRC CircularColorsView.java:32 (init())')
e('CircularColorsView.<init>(Context,AttributeSet)', 'CircularColorsView.init', 'CALL',
  'Constructor calls init to initialize paints and divider',
  evidence='SRC CircularColorsView.java:37 (init())')

# CircularColorsView.onDraw
e('View.draw', 'CircularColorsView.onDraw', 'FRAMEWORK',
  'View framework calls onDraw when view needs to render; CircularColorsView used in layouts',
  evidence='SRC CircularColorsView.java:57-89 (onDraw implementation); XML item_colorpicker.xml:5, selectedcolors_preference.xml use CircularColorsView; INFERRED android.view.View dispatches draw to onDraw')

# CloudIconDataFetcher.cleanup
e('Glide.into', 'CloudIconDataFetcher.cleanup', 'FRAMEWORK',
  'Glide framework calls DataFetcher.cleanup after loading completes or when request is cleared',
  evidence='SRC CloudIconDataFetcher.java:53-59 (cleanup closes input stream); INFERRED com.bumptech.glide.load.data.DataFetcher interface contract requires cleanup call')

# CloudIconDataFetcher.getDataClass
e('Glide.load', 'CloudIconDataFetcher.getDataClass', 'FRAMEWORK',
  'Glide framework calls getDataClass to determine data type returned by fetcher',
  evidence='SRC CloudIconDataFetcher.java:67-70 (returns Bitmap.class); INFERRED com.bumptech.glide.load.data.DataFetcher interface contract')

# CloudIconDataFetcher.getDataSource
e('Glide.load', 'CloudIconDataFetcher.getDataSource', 'FRAMEWORK',
  'Glide framework calls getDataSource to determine data origin for caching strategy',
  evidence='SRC CloudIconDataFetcher.java:73-77 (returns DataSource.REMOTE); INFERRED com.bumptech.glide.load.data.DataFetcher interface contract')

# CloudStreamer.isStreamMedia
UNREACHABLE['CloudStreamer.isStreamMedia'] = ('no_trigger_in_app',
  'Static method for SmbFile pattern matching; not called from app source',
  'SRC CloudStreamer.java:44-46 (static method checks file name pattern for media extensions); GREP no callers of isStreamMedia in app source',
  'SOURCE')

# Coders$BCJDecoder.encode
e('Coders.addEncoder', 'Coders$BCJDecoder.encode', 'CALL',
  'addEncoder calls BCJDecoder.encode when SevenZMethod is BCJ_*_FILTER variant',
  evidence='SRC Coders.java:85-92 (addEncoder gets CoderBase via findByMethod and calls encode); Coders.java:59-65 (BCJDecoder registered in CODER_MAP for BCJ_X86_FILTER, BCJ_PPC_FILTER, BCJ_IA64_FILTER, BCJ_ARM_FILTER, BCJ_ARM_THUMB_FILTER, BCJ_SPARC_FILTER); Coders.java:119-128 (BCJDecoder.encode implementation)')

# Coders$BZIP2Decoder.encode
e('Coders.addEncoder', 'Coders$BZIP2Decoder.encode', 'CALL',
  'addEncoder calls BZIP2Decoder.encode when SevenZMethod is BZIP2',
  evidence='SRC Coders.java:85-92 (addEncoder gets CoderBase via findByMethod and calls encode); Coders.java:54 (BZIP2Decoder registered in CODER_MAP for BZIP2); Coders.java:256-260 (BZIP2Decoder.encode implementation)')

# Coders$CopyDecoder.encode
e('Coders.addEncoder', 'Coders$CopyDecoder.encode', 'CALL',
  'addEncoder calls CopyDecoder.encode when SevenZMethod is COPY',
  evidence='SRC Coders.java:85-92 (addEncoder gets CoderBase via findByMethod and calls encode); Coders.java:51 (CopyDecoder registered in CODER_MAP for COPY); Coders.java:107-110 (CopyDecoder.encode returns out unchanged)')

