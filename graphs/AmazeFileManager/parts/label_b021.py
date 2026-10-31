# ---- Helper batch_021 label part (2025-01-18)

# DecryptService$BackgroundTask methods
e('DecryptService.onStartCommand', 'DecryptService$BackgroundTask.<init>', 'CALL', 
  'onStartCommand creates BackgroundTask instance',
  evidence='SRC DecryptService.java:118')

e('DecryptService$BackgroundTask.<init>', 'AsyncTask.<init>', 'CALL',
  'BackgroundTask extends AsyncTask, constructor chains to parent',
  evidence='SRC DecryptService.java:123')

e('DecryptService.onStartCommand', 'DecryptService$BackgroundTask.execute', 'ASYNC',
  'onStartCommand executes the AsyncTask',
  evidence='SRC DecryptService.java:118')

e('AsyncTask.execute', 'DecryptService$BackgroundTask.doInBackground', 'FRAMEWORK',
  'AsyncTask framework calls doInBackground on background thread',
  evidence='FW-SRC core/java/android/os/AsyncTask.java:333')

e('DecryptService$BackgroundTask.doInBackground', 'DecryptService$BackgroundTask.lambda$doInBackground$0', 'CALL',
  'doInBackground sets progress listener with lambda',
  evidence='SRC DecryptService.java:138-139')

e('AsyncTask.finish', 'DecryptService$BackgroundTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute when doInBackground completes',
  evidence='FW-SRC core/java/android/os/AsyncTask.java:695')

# DeltaDecoder methods (7z library)
e('Coders.<clinit>', 'DeltaDecoder.<init>', 'CALL',
  'Coders static initializer creates DeltaDecoder instance for DELTA_FILTER method',
  evidence='SRC sevenz/Coders.java:64')

e('Coders.addDecoder', 'DeltaDecoder.decode', 'CALL',
  'Coders.addDecoder invokes decode when processing 7z archives with delta encoding',
  evidence='SRC sevenz/Coders.java:73')

e('DeltaDecoder.decode', 'DeltaDecoder.getOptionsFromCoder', 'CALL',
  'decode calls private getOptionsFromCoder(Coder) to extract delta distance',
  evidence='SRC sevenz/DeltaDecoder.java:36')

e('DeltaDecoder.getOptionsFromCoder', 'DeltaDecoder.getOptionsFromCoder', 'CALL',
  'public getOptionsFromCoder(Coder,InputStream) calls private getOptionsFromCoder(Coder)',
  evidence='SRC sevenz/DeltaDecoder.java:59')

e('Coders.addEncoder', 'DeltaDecoder.encode', 'CALL',
  'Coders.addEncoder invokes encode when creating 7z archives with delta encoding',
  evidence='SRC sevenz/Coders.java:84')

e('Coders.addEncoder', 'DeltaDecoder.getOptionsAsProperties', 'CALL',
  'Coders.addEncoder calls getOptionsAsProperties to serialize delta options',
  evidence='SRC sevenz/SevenZOutputFile.java:452')

e('SevenZFile.buildDecodingStream', 'DeltaDecoder.getOptionsFromCoder', 'CALL',
  'SevenZFile.buildDecodingStream calls getOptionsFromCoder(Coder,InputStream) during stream setup',
  evidence='SRC sevenz/SevenZFile.java:1033')

# DisablableViewPager methods
e('LayoutInflater.inflate', 'DisablableViewPager.<init>', 'FRAMEWORK',
  'LayoutInflater instantiates DisablableViewPager from tabfragment.xml layout',
  evidence='SRC res/layout/tabfragment.xml:20-36, SRC TabFragment.java:95')

e('ViewPager.onTouchEvent', 'DisablableViewPager.onTouchEvent', 'FRAMEWORK',
  'Framework calls onTouchEvent when user touches the view',
  evidence='INFERRED androidx ViewPager touch event dispatch, source not read')

e('ViewPager.onInterceptTouchEvent', 'DisablableViewPager.onInterceptTouchEvent', 'FRAMEWORK',
  'Framework calls onInterceptTouchEvent to determine if ViewPager should intercept touch',
  evidence='INFERRED androidx ViewPager touch interception, source not read')

e('TabFragment.onCreateView', 'DisablableViewPager.setPagingEnabled', 'CALL',
  'TabFragment can call setPagingEnabled to enable/disable paging',
  evidence='SRC DisablableViewPager.java:32')

# DividerItemDecoration methods
e('DividerItemDecoration.<clinit>', 'DividerItemDecoration.<clinit>', 'CALL',
  'Class initializer defines ATTRS array',
  evidence='SRC DividerItemDecoration.java:19-21')

e('MainFragment.onCreateView', 'DividerItemDecoration.<init>', 'CALL',
  'MainFragment creates DividerItemDecoration instance',
  evidence='SRC MainFragment.java:304-305')

e('RecyclerView.draw', 'DividerItemDecoration.onDraw', 'FRAMEWORK',
  'RecyclerView framework calls onDraw to render dividers',
  evidence='INFERRED androidx RecyclerView ItemDecoration lifecycle, source not read')

e('DividerItemDecoration.onDraw', 'DividerItemDecoration.drawVertical', 'CALL',
  'onDraw calls drawVertical to draw divider lines',
  evidence='SRC DividerItemDecoration.java:48')

e('RecyclerView.measureChild', 'DividerItemDecoration.getItemOffsets', 'FRAMEWORK',
  'RecyclerView framework calls getItemOffsets to compute item spacing',
  evidence='INFERRED androidx RecyclerView ItemDecoration lifecycle, source not read')

# UNREACHABLE methods from this batch
UNREACHABLE_B021 = {
    'DonationViewHolder.<init>': ('no_trigger_in_app', 'DonationViewHolder is never instantiated in any adapter; grep shows no references outside the class definition itself', 'SRC DonationViewHolder.java:1-20 shows class definition with no usages in codebase', 'SOURCE'),
}
