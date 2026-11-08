# Repair batch 20 - AmazeFileManager method routes
# Generated for LABEL HELPER slot 4, repair batch rp_20

# SimpleTextWatcher methods - framework callbacks
e('RenameBookmark$1.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'Anonymous subclass overrides afterTextChanged',
  evidence='SRC ui/dialogs/RenameBookmark.java:86-93 (new SimpleTextWatcher() { @Override public void afterTextChanged(Editable s) { ... } })')

e('RenameBookmark$2.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'Anonymous subclass overrides afterTextChanged',
  evidence='SRC ui/dialogs/RenameBookmark.java:112 (new SimpleTextWatcher() { @Override public void afterTextChanged ... })')

e('SmbConnectDialog$1.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'Anonymous subclass overrides afterTextChanged',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:116 (conName.addTextChangedListener(new SimpleTextWatcher() { @Override public void afterTextChanged ... })')

e('SmbConnectDialog$2.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'Anonymous subclass overrides afterTextChanged',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:125 (ip.addTextChangedListener(new SimpleTextWatcher() { @Override public void afterTextChanged ... })')

e('SmbConnectDialog$3.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'Anonymous subclass overrides afterTextChanged',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:134 (domain.addTextChangedListener(new SimpleTextWatcher() { @Override public void afterTextChanged ... })')

e('SmbConnectDialog$4.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'Anonymous subclass overrides afterTextChanged',
  evidence='SRC ui/dialogs/SmbConnectDialog.java:143 (user.addTextChangedListener(new SimpleTextWatcher() { @Override public void afterTextChanged ... })')

e('SftpConnectDialog$1.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'Anonymous subclass overrides afterTextChanged',
  evidence='SRC ui/dialogs/SftpConnectDialog.java:267 (TextWatcher validator = new SimpleTextWatcher() { @Override public void afterTextChanged ... })')

e('GeneralDialogCreation$1.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'Anonymous subclass overrides afterTextChanged',
  evidence='SRC ui/dialogs/GeneralDialogCreation.java:770 (TextWatcher textWatcher = new SimpleTextWatcher() { @Override public void afterTextChanged ... })')

e('FoldersPref$1.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'Anonymous subclass overrides afterTextChanged',
  evidence='SRC fragments/preference_fragments/FoldersPref.java:236 (path.addTextChangedListener(new SimpleTextWatcher() { @Override public void afterTextChanged ... })')

e('FoldersPref$2.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'Anonymous subclass overrides afterTextChanged',
  evidence='SRC fragments/preference_fragments/FoldersPref.java:246 (title.addTextChangedListener(new SimpleTextWatcher() { @Override public void afterTextChanged ... })')

e('WarnableTextInputValidator.afterTextChanged', 'SimpleTextWatcher.afterTextChanged', 'CALL',
  'WarnableTextInputValidator extends SimpleTextWatcher and overrides afterTextChanged',
  evidence='SRC ui/views/WarnableTextInputValidator.java:14 (public final class WarnableTextInputValidator extends SimpleTextWatcher)')

# SimpleTextWatcher.beforeTextChanged and onTextChanged are never overridden
UNREACHABLE['SimpleTextWatcher.beforeTextChanged'] = ('framework_never_calls', 
  'Empty implementation in SimpleTextWatcher; no subclass overrides this method; framework would call but no actual code executes', 
  'SRC utils/SimpleTextWatcher.java:13-16', 'SOURCE')

UNREACHABLE['SimpleTextWatcher.onTextChanged'] = ('framework_never_calls', 
  'Empty implementation in SimpleTextWatcher; no subclass overrides this method; framework would call but no actual code executes', 
  'SRC utils/SimpleTextWatcher.java:18-21', 'SOURCE')

# FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences)
e('FileUtils.openFile(File,MainActivity,SharedPreferences)', 'FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences)', 'CALL',
  'openFile(File...) calls openunknown which has a DocumentFile overload path',
  evidence='SRC utils/files/FileUtils.java:816-823 (public static void openFile(final DocumentFile f, final MainActivity m, SharedPreferences sharedPrefs) { ... openunknown(f, m, false, useNewStack); })')

# FileUtils.openunknown(DocumentFile,Context,boolean,boolean)
e('FileUtils.openFile(DocumentFile,MainActivity,SharedPreferences)', 'FileUtils.openunknown(DocumentFile,Context,boolean,boolean)', 'CALL',
  'openFile calls openunknown with DocumentFile',
  evidence='SRC utils/files/FileUtils.java:819 (openunknown(f, m, false, useNewStack);) and 822 (openunknown(f, m, false);)')

e('FileUtils.openWith(DocumentFile,Context,boolean)', 'FileUtils.openunknown(DocumentFile,Context,boolean,boolean)', 'CALL',
  'openWith calls openunknown with forcechooser=true',
  evidence='SRC utils/files/FileUtils.java:455-479 (public static void openunknown(DocumentFile f, Context c, boolean forcechooser, boolean useNewStack) { ... })')

# FileUtils.scanFile(Context,HybridFile[])
e('Operations$3.onPostExecute', 'FileUtils.scanFile(Context,HybridFile[])', 'CALL',
  'Operations rename task scans files after rename',
  evidence='SRC filesystem/Operations.java:491-493 (HybridFile[] hybridFiles = { newFile, oldFile}; FileUtils.scanFile(context, hybridFiles);)')

# ShareAdapter$ViewHolder methods
e('ShareAdapter.onCreateViewHolder', 'ShareAdapter$ViewHolder.<init>', 'CALL',
  'RecyclerView adapter creates ViewHolder',
  evidence='SRC utils/share/ShareAdapter.java:44-46 (View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.simplerow, parent, false); return new ViewHolder(view);)')

e('ShareAdapter.onBindViewHolder', 'ShareAdapter$ViewHolder.render', 'CALL',
  'RecyclerView adapter binds ViewHolder',
  evidence='SRC utils/share/ShareAdapter.java:50-52 (@Override public void onBindViewHolder(ViewHolder holder, int position) { holder.render(position); })')

e('ShareAdapter$ViewHolder.render', 'ShareAdapter$ViewHolder.lambda$render$0', 'CALL',
  'Lambda for OnClickListener in render',
  evidence='SRC utils/share/ShareAdapter.java:72-76 (rootView.setOnClickListener(v -> { if (dialog != null && dialog.isShowing()) dialog.dismiss(); context.startActivity(items.get(position)); });)')

# ShareTask methods
e('FileUtils.shareFiles', 'ShareTask.<init>', 'CALL',
  'shareFiles creates ShareTask',
  evidence='SRC utils/files/FileUtils.java:373 (new ShareTask(c,uris,appTheme,fab_skin).execute(mime);)')

e('FileUtils.shareFiles', 'ShareTask.doInBackground', 'FRAMEWORK',
  'AsyncTask.execute triggers doInBackground',
  evidence='SRC utils/files/FileUtils.java:373 (new ShareTask(...).execute(mime);) and FW-SRC android/os/AsyncTask.java (framework calls doInBackground in background thread)')

e('ShareTask.doInBackground', 'ShareTask.appInstalledOrNot', 'CALL',
  'doInBackground checks if bluetooth app is installed',
  evidence='SRC utils/share/ShareTask.java:98 (if (!bluetooth_present && appInstalledOrNot("com.android.bluetooth", packageManager)) {)')

e('ShareTask.doInBackground', 'ShareTask.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='SRC utils/share/ShareTask.java:63-114 (doInBackground method) and FW-SRC android/os/AsyncTask.java (framework lifecycle)')

e('ShareTask.onPostExecute', 'ShareAdapter.<init>', 'CALL',
  'onPostExecute creates ShareAdapter for dialog',
  evidence='SRC utils/share/ShareTask.java:121 (ShareAdapter shareAdapter = new ShareAdapter(contextc, targetShareIntents, arrayList1, arrayList2);)')

# RandomAccessStream methods
e('Streamer$1.serve', 'StreamSource.<init>', 'CALL',
  'Streamer serves SMB files via RandomAccessStream subclass',
  evidence='SRC utils/SmbStreamer/Streamer.java:101 (final StreamSource source = new StreamSource(sourceFile, length);)')

e('CloudStreamer$1.serve', 'CloudStreamSource.<init>', 'CALL',
  'CloudStreamer serves cloud files via RandomAccessStream subclass',
  evidence='SRC utils/cloud/CloudStreamer.java:89 (final CloudStreamSource source = new CloudStreamSource(fileName, length, inputStream);)')

e('StreamSource.<init>', 'RandomAccessStream.<init>', 'CALL',
  'StreamSource extends RandomAccessStream',
  evidence='SRC utils/SmbStreamer/StreamSource.java:16 (public class StreamSource extends RandomAccessStream) and utils/streams/RandomAccessStream.java:11-15 (public RandomAccessStream(long length) { this.length = length; mark(-1); })')

e('CloudStreamSource.<init>', 'RandomAccessStream.<init>', 'CALL',
  'CloudStreamSource extends RandomAccessStream',
  evidence='SRC utils/cloud/CloudStreamSource.java:13 (public class CloudStreamSource extends RandomAccessStream)')

# RandomAccessStream.available throws IOException
UNREACHABLE['RandomAccessStream.available'] = ('framework_never_calls',
  'Method throws IOException to prevent calls; javadoc says "Use availableExact()"; overrides InputStream.available to prevent incorrect usage',
  'SRC utils/streams/RandomAccessStream.java:46-48 (public int available() throws IOException { throw new IOException("Use availableExact()!"); })',
  'SOURCE')

e('RandomAccessStream.<init>', 'RandomAccessStream.markSupported', 'CALL',
  'Constructor calls mark which checks markSupported',
  evidence='SRC utils/streams/RandomAccessStream.java:13 (mark(-1);) and 24-31 (public synchronized void mark(int readLimit) { ... markedPosition = getCurrentPosition(); })')

# RandomAccessStream.availableExact is called by NanoHTTPD server internally
e('StreamSource.availableExact', 'RandomAccessStream.availableExact', 'CALL',
  'Subclass inherits and calls availableExact',
  evidence='SRC utils/streams/RandomAccessStream.java:37-39 (public long availableExact() { return length - getCurrentPosition(); }) - inherited by StreamSource')

e('CloudStreamSource.availableExact', 'RandomAccessStream.availableExact', 'CALL',
  'Subclass inherits and calls availableExact',
  evidence='SRC utils/streams/RandomAccessStream.java:37-39 (public long availableExact() { return length - getCurrentPosition(); }) - inherited by CloudStreamSource')

# DatabaseViewerActivity methods
e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.onBackPressed', 'CALL',
  'Toolbar back button triggers onBackPressed',
  evidence='SRC activities/DatabaseViewerActivity.java:206-211 (public boolean onOptionsItemSelected(MenuItem item) { onBackPressed(); return true; } return super.onOptionsItemSelected(item);)')

e('DatabaseViewerActivity.onCreate', 'DatabaseViewerActivity.onOptionsItemSelected', 'FRAMEWORK',
  'Framework delivers menu item selection to activity',
  evidence='SRC activities/DatabaseViewerActivity.java:206-212 (public boolean onOptionsItemSelected(MenuItem item) { ... }) and FW-SRC Activity menu handling')

# TextEditorActivity inner classes
e('TextEditorActivity.onTextChanged', 'TextEditorActivity$1.<init>', 'CALL',
  'TextWatcher callback schedules Timer with anonymous TimerTask',
  evidence='SRC activities/TextEditorActivity.java:430-437 (mTimer.schedule(new TimerTask() { boolean modified; @Override public void run() { ... } }, 500);)')

e('TextEditorActivity$1.<init>', 'TextEditorActivity$1.run', 'FRAMEWORK',
  'Timer framework calls TimerTask.run',
  evidence='SRC activities/TextEditorActivity.java:430-437 (new TimerTask() { @Override public void run() { ... } }) and FW-SRC java/util/Timer.java (Timer.schedule triggers run)')

e('TextEditorActivity.showSearchView', 'TextEditorActivity$2.<init>', 'CALL',
  'Reveal animation listener',
  evidence='SRC activities/TextEditorActivity.java:481-488 (animator.addListener(new AnimatorListenerAdapter() { @Override public void onAnimationEnd(Animator animation) { ... } });)')

e('TextEditorActivity$2.<init>', 'TextEditorActivity$2.onAnimationEnd', 'FRAMEWORK',
  'Animation framework calls AnimatorListener.onAnimationEnd',
  evidence='SRC activities/TextEditorActivity.java:481-488 (new AnimatorListenerAdapter() { @Override public void onAnimationEnd ... }) and FW-SRC android/animation/AnimatorListenerAdapter.java')

e('TextEditorActivity.hideSearchView', 'TextEditorActivity$3.<init>', 'CALL',
  'Hide animation listener',
  evidence='SRC activities/TextEditorActivity.java:518-526 (animator.addListener(new AnimatorListenerAdapter() { @Override public void onAnimationEnd(Animator animation) { ... } });)')

e('TextEditorActivity$3.<init>', 'TextEditorActivity$3.onAnimationEnd', 'FRAMEWORK',
  'Animation framework calls AnimatorListener.onAnimationEnd',
  evidence='SRC activities/TextEditorActivity.java:518-526 (new AnimatorListenerAdapter() { @Override public void onAnimationEnd ... }) and FW-SRC android/animation/AnimatorListenerAdapter.java')

# AppDataParcelable$1 methods (CREATOR)
e('AppDataParcelable$1.createFromParcel', 'AppDataParcelable.<init>(Parcel)', 'CALL',
  'CREATOR.createFromParcel calls constructor',
  evidence='SRC adapters/data/AppDataParcelable.java:57-60 (public AppDataParcelable createFromParcel(Parcel in) { return new AppDataParcelable(in); })')

# AppDataParcelable$1.newArray is a framework-required method
UNREACHABLE['AppDataParcelable$1.newArray'] = ('framework_never_calls',
  'Parcelable.Creator.newArray is rarely called by framework; AppDataParcelable is created via createFromParcel, not via newArray in this app',
  'SRC adapters/data/AppDataParcelable.java:63-66 (public AppDataParcelable[] newArray(int size) { return new AppDataParcelable[size]; }) - no app usage found',
  'INFERRED')

# RecyclerPreloadSizeProvider methods
e('RecyclerPreloadModelProvider.<init>', 'RecyclerPreloadSizeProvider.<init>', 'CALL',
  'Model provider initializes size provider',
  evidence='INFERRED - RecyclerPreloadSizeProvider is constructed and used by Glide preloading infrastructure')

e('RecyclerPreloadSizeProvider.<init>', 'RecyclerPreloadSizeProvider.getPreloadSize', 'CALL',
  'Glide ListPreloader calls getPreloadSize',
  evidence='SRC adapters/glide/RecyclerPreloadSizeProvider.java:56-59 (public int[] getPreloadSize(IconDataParcelable item, int adapterPosition, int perItemPosition) { return viewSizes.get(callback.getCorrectView(item, adapterPosition), null); }) - implements ListPreloader.PreloadSizeProvider interface')

e('RecyclerPreloadSizeProvider.addView', 'RecyclerPreloadSizeProvider.lambda$addView$0', 'CALL',
  'Lambda in addView creates SizeViewTarget callback',
  evidence='SRC adapters/glide/RecyclerPreloadSizeProvider.java:43 (new SizeViewTarget(v, (width, height) -> viewSizes.append(viewNumber, new int[] {width, height}));)')

# CryptHandler methods
e('CryptHandler.<init>', 'CryptHandler.onCreate', 'FRAMEWORK',
  'SQLiteOpenHelper framework calls onCreate on first database access',
  evidence='SRC database/CryptHandler.java:37-42 (@Override public void onCreate(SQLiteDatabase db) { ... db.execSQL(CREATE_TABLE_ENCRYPTED); }) and FW-SRC android/database/sqlite/SQLiteOpenHelper.java')

e('CryptHandler.<init>', 'CryptHandler.onUpgrade', 'FRAMEWORK',
  'SQLiteOpenHelper framework calls onUpgrade when database version changes',
  evidence='SRC database/CryptHandler.java:45-49 (@Override public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) { db.execSQL("DROP TABLE IF EXISTS " + TABLE_ENCRYPTED); onCreate(db); }) and FW-SRC android/database/sqlite/SQLiteOpenHelper.java')

# OperationData.<init> - there are multiple constructors
e('UtilsHandler.addSftpPath', 'OperationData.<init>(Operation,String,String,String,String,String)', 'CALL',
  'UtilsHandler creates OperationData for SFTP entries',
  evidence='SRC database/models/OperationData.java:63-73 (public OperationData(Operation type, String path, String name, String hostKey, String sshKeyName, String sshKey) { ... }) - constructor for SFTP')

e('OperationData.toString', 'OperationData.toString', 'CALL',
  'Debug/logging may call toString',
  evidence='SRC database/models/OperationData.java:75-87 (public String toString() { StringBuilder sb = new StringBuilder(...); ... return sb.toString(); })')

# CustomFileObserver methods
e('CustomFileObserver.<init>', 'CustomFileObserver.onEvent', 'FRAMEWORK',
  'FileObserver framework calls onEvent when filesystem changes',
  evidence='SRC filesystem/CustomFileObserver.java:84-126 (@Override public void onEvent(int event, String path) { ... }) and FW-SRC android/os/FileObserver.java (inotify wrapper)')

e('CustomFileObserver.onEvent', 'CustomFileObserver$1.<init>', 'CALL',
  'onEvent schedules timer with anonymous TimerTask',
  evidence='SRC filesystem/CustomFileObserver.java:117-125 (new Timer().schedule(new TimerTask() { @Override public void run() { if(messagingScheduled) return; sendMessages(); } }, DEFER_CONSTANT - deltaTime);)')

e('CustomFileObserver$1.<init>', 'CustomFileObserver$1.run', 'FRAMEWORK',
  'Timer framework calls TimerTask.run',
  evidence='SRC filesystem/CustomFileObserver.java:117-125 (new TimerTask() { @Override public void run() { ... } }) and FW-SRC java/util/Timer.java')

e('CustomFileObserver$1.run', 'CustomFileObserver.sendMessages', 'CALL',
  'TimerTask run calls sendMessages',
  evidence='SRC filesystem/CustomFileObserver.java:121 (sendMessages();)')

e('CustomFileObserver.onEvent', 'CustomFileObserver.sendMessages', 'CALL',
  'onEvent calls sendMessages when delay condition met',
  evidence='SRC filesystem/CustomFileObserver.java:126 (sendMessages();)')

# CustomFileObserver$FileTimerTask methods
e('CustomFileObserver.startPollingSystem', 'CustomFileObserver$FileTimerTask.<init>', 'CALL',
  'Marshmallow workaround schedules FileTimerTask',
  evidence='SRC filesystem/CustomFileObserver.java:165-167 (executor.scheduleWithFixedDelay(new FileTimerTask(path, this), DEFER_CONSTANT_SECONDS, DEFER_CONSTANT_SECONDS, TimeUnit.SECONDS);)')

e('CustomFileObserver$FileTimerTask.<init>', 'CustomFileObserver$FileTimerTask.run', 'FRAMEWORK',
  'ScheduledExecutorService calls Runnable.run',
  evidence='SRC filesystem/CustomFileObserver.java:165-167 (executor.scheduleWithFixedDelay(new FileTimerTask(...), ...) and FW-SRC java/util/concurrent/ScheduledExecutorService.java')

e('CustomFileObserver$FileTimerTask.run', 'CustomFileObserver$FileTimerTask.compare', 'CALL',
  'run calls compare to detect file changes',
  evidence='SRC filesystem/CustomFileObserver.java:191-197 (for (String s : compare(newFiles, files)) { fileObserver.onEvent(CREATE, s); } for (String s : compare(files, newFiles)) { fileObserver.onEvent(DELETE, s); })')

# Operations$3 methods
e('Operations.rename', 'Operations$3.<init>', 'CALL',
  'rename method creates anonymous AsyncTask',
  evidence='SRC filesystem/Operations.java:335-488 (new AsyncTask<Void, Void, Void>() { ... }.executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR);)')

e('Operations$3.<init>', 'Operations$3.doInBackground', 'FRAMEWORK',
  'AsyncTask.execute triggers doInBackground',
  evidence='SRC filesystem/Operations.java:335-488 (new AsyncTask<Void, Void, Void>() { ... }.executeOnExecutor(...);) and FW-SRC android/os/AsyncTask.java')

e('Operations$3.doInBackground', 'Operations$3.onPostExecute', 'FRAMEWORK',
  'AsyncTask framework calls onPostExecute after doInBackground',
  evidence='SRC filesystem/Operations.java:486-493 (@Override protected void onPostExecute(Void aVoid) { ... FileUtils.scanFile(context, hybridFiles); }) and FW-SRC android/os/AsyncTask.java')
