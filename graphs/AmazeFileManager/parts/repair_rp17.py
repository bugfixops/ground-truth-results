# Repair batch 17 - AmazeFileManager method labeling
# Generated: 2025-01-XX 21:26
# Methods: RecyclerAdapter$2 callbacks, Parcelables, Services, Database handlers, etc.

# RecyclerAdapter$2 - Glide RequestListener callbacks (2nd instance lines 920-943)
# SRC RecyclerAdapter.java:920-943:
# view.setVisibility(View.INVISIBLE);
# RequestListener<Drawable> requestListener = new RequestListener<Drawable>() {
#     @Override
#     public boolean onLoadFailed(@Nullable GlideException e, Object model, Target target, boolean isFirstResource) {
#         iconBackground.setBackgroundColor(grey_color);
#         new Handler(msg -> {
#             GlideApp.with(mainFrag).load(R.drawable.ic_broken_image_white_24dp).into(viewHolder.genericIcon);
#             return false;
#         }).obtainMessage().sendToTarget();
#         errorListener.onImageProcessed(true);
#         return true;
#     }
#     @Override
#     public boolean onResourceReady(Drawable resource, Object model, Target<Drawable> target,
#                                    DataSource dataSource, boolean isFirstResource) {
#         viewHolder.genericIcon.setImageDrawable(null);
#         viewHolder.genericIcon.setVisibility(View.GONE);
#         view.setVisibility(View.VISIBLE);
#         iconBackground.setBackgroundColor(mainFrag.getResources().getColor(android.R.color.transparent));
#         errorListener.onImageProcessed(false);
#         return false;
#     }
# };

e('RecyclerAdapter.showRoundedThumbnail', 'RecyclerAdapter$2.<init>', 'CALL',
  'RecyclerAdapter creates RequestListener for rounded thumbnail image loading',
  evidence='SRC RecyclerAdapter.java:922 RequestListener<Drawable> requestListener = new RequestListener<Drawable>()')

e('RecyclerAdapter$2.<init>', 'RecyclerAdapter$2.onLoadFailed', 'FRAMEWORK',
  'Glide framework calls onLoadFailed when image loading fails',
  evidence='INFERRED Glide RequestListener<Drawable> interface; framework invokes callback')

e('RecyclerAdapter$2.<init>', 'RecyclerAdapter$2.onResourceReady', 'FRAMEWORK',
  'Glide framework calls onResourceReady when image loads successfully',
  evidence='INFERRED Glide RequestListener<Drawable> interface; framework invokes callback')

e('RecyclerAdapter$2.onLoadFailed', 'RecyclerAdapter$2.lambda$onLoadFailed$0', 'CALL',
  'onLoadFailed creates Handler lambda for UI thread update',
  evidence='SRC RecyclerAdapter.java:925 new Handler(msg -> { GlideApp.with(mainFrag).load(...).into(viewHolder.genericIcon); return false; })')

# AppDataParcelable Parcelable methods
# SRC AppDataParcelable.java:26-32:
# @Override
# public int describeContents() {
#     return 0;
# }
# @Override
# public void writeToParcel(Parcel parcel, int i) {
#     parcel.writeString(label);

e('AppDataParcelable.<init>(Parcel)', 'AppDataParcelable.describeContents', 'FRAMEWORK',
  'Framework calls describeContents during parceling operations',
  evidence='INFERRED Android Parcelable contract; SRC AppDataParcelable.java:26-28')

e('AppDataParcelable.<init>(Parcel)', 'AppDataParcelable.writeToParcel', 'FRAMEWORK',
  'Framework calls writeToParcel to serialize object state',
  evidence='SRC AppDataParcelable.java:31-38 parcel.writeString/writeLong fields')

# IconDataParcelable.setImageBroken
# SRC IconDataParcelable.java:43-45:
# public void setImageBroken(boolean imageBroken) {
#     isImageBroken = imageBroken;
# }
UNREACHABLE['IconDataParcelable.setImageBroken'] = ('no_trigger_in_app', 'Setter never called; isImageBroken checked via getter but never set from app code', 'GREP no setImageBroken calls in app src', 'INFERRED')

# PemToKeyPairTask$1 - anonymous PasswordFinder
# SRC PemToKeyPairTask.java:169-178:
# this.passwordFinder = new PasswordFinder() {
#     @Override
#     public char[] reqPassword(Resource<?> resource) {
#         return textfield.getText().toString().toCharArray();
#     }
#     @Override
#     public boolean shouldRetry(Resource<?> resource) {
#         return false;
#     }
# };

e('PemToKeyPairTask.onProgressUpdate', 'PemToKeyPairTask$1.<init>', 'CALL',
  'PemToKeyPairTask creates PasswordFinder when encrypted key needs passphrase',
  evidence='SRC PemToKeyPairTask.java:169 this.passwordFinder = new PasswordFinder() { ... }')

e('PemToKeyPairTask$1.<init>', 'PemToKeyPairTask$1.reqPassword', 'FRAMEWORK',
  'SSHJ library calls reqPassword to request passphrase for encrypted private key',
  evidence='INFERRED net.schmizz.sshj.userauth.password.PasswordFinder interface contract')

e('PemToKeyPairTask$1.<init>', 'PemToKeyPairTask$1.shouldRetry', 'FRAMEWORK',
  'SSHJ library calls shouldRetry after password authentication failure',
  evidence='INFERRED net.schmizz.sshj.userauth.password.PasswordFinder interface contract')

# ZipService lifecycle methods
# SRC ZipService.java:313-315:
# public IBinder onBind(Intent arg0) {
#     return mBinder;
# }
# SRC ProcessViewerFragment.java:165:
# getActivity().bindService(intent2, mCompressConnection, 0);

e('ProcessViewerFragment.refreshView', 'ZipService.onBind', 'LIFECYCLE',
  'ProcessViewerFragment binds to ZipService to monitor compression progress',
  evidence='SRC ProcessViewerFragment.java:165 getActivity().bindService(intent2, mCompressConnection, 0)')

# SRC ZipService.java:318-320:
# @Override
# public void onDestroy() {
#     this.unregisterReceiver(receiver1);
# }

e('ZipService.onBind', 'ZipService.onDestroy', 'LIFECYCLE',
  'Framework calls onDestroy when service is destroyed',
  evidence='SRC ZipService.java:318-320 cleanup unregisterReceiver')

# SRC ZipService.java:184-186:
# public void setProgressListener(ProgressListener progressListener) {
#     this.progressListener = progressListener;
# }
# SRC ProcessViewerFragment.java:416:
# specificService.setProgressListener(new AbstractProgressiveService.ProgressListener() { ... })

e('ProcessViewerFragment$CustomServiceConnection.onServiceConnected', 'ZipService.setProgressListener', 'CALL',
  'ProcessViewerFragment sets progress listener to monitor zip operation',
  evidence='SRC ProcessViewerFragment.java:416 specificService.setProgressListener(new AbstractProgressiveService.ProgressListener())')

# SortHandler - SQLiteOpenHelper
# SRC SortHandler.java:47-51:
# @Override
# public void onCreate(SQLiteDatabase db) {
#     String CREATE_TABLE_SORT = "CREATE TABLE " + TABLE_SORT + "(" + COLUMN_SORT_PATH + " TEXT PRIMARY KEY," + COLUMN_SORT_TYPE + " INTEGER" + ")";
#     db.execSQL(CREATE_TABLE_SORT);
# }

e('SortHandler.<init>', 'SortHandler.onCreate', 'LIFECYCLE',
  'SQLiteOpenHelper.onCreate called by framework when database is created first time',
  evidence='SRC SortHandler.java:47-51 CREATE TABLE sort')

e('SortHandler.<init>', 'SortHandler.onUpgrade', 'LIFECYCLE',
  'SQLiteOpenHelper.onUpgrade called by framework when database version changes',
  evidence='SRC SortHandler.java:54-56 just calls onCreate(db)')

# SRC SortHandler.java:109-131:
# public List<Sort> getAllEntries() {
#     List<Sort> entryList = new ArrayList<>();
#     String query = "Select * FROM " + TABLE_SORT;
#     SQLiteDatabase sqLiteDatabase = getReadableDatabase();
# SRC GeneralDialogCreation.java:1038:
# SortHandler sortHandler = new SortHandler(m.getContext());

e('GeneralDialogCreation.showSortDialog', 'SortHandler.getAllEntries', 'CALL',
  'Sort dialog queries all sort preferences',
  evidence='INFERRED from SortHandler usage pattern; SRC GeneralDialogCreation.java:1038 new SortHandler')

# TabHandler - SQLiteOpenHelper
# SRC TabHandler.java:57-81:
# @Override
# public void onCreate(SQLiteDatabase db) {
#     String CREATE_TAB_TABLE = "CREATE TABLE IF NOT EXISTS " + TABLE_TAB + "(" + COLUMN_TAB_NO + " INTEGER PRIMARY KEY," + COLUMN_PATH + " TEXT," + COLUMN_HOME + " TEXT" + ")";
#     db.execSQL(CREATE_TAB_TABLE);

e('TabHandler.<init>', 'TabHandler.onCreate', 'LIFECYCLE',
  'SQLiteOpenHelper.onCreate called by framework when database is created',
  evidence='SRC TabHandler.java:57-81 CREATE TABLE tab, encrypted, cloud, sort')

e('TabHandler.<init>', 'TabHandler.onUpgrade', 'LIFECYCLE',
  'SQLiteOpenHelper.onUpgrade called by framework on database version change',
  evidence='SRC TabHandler.java:84-86 just calls onCreate(sqLiteDatabase)')

e('TabHandler.<init>', 'TabHandler.onDowngrade', 'LIFECYCLE',
  'SQLiteOpenHelper.onDowngrade called by framework on database downgrade',
  evidence='SRC TabHandler.java:89-91 calls onUpgrade(db, oldVersion, newVersion)')

# StreamNotFoundException constructors
# SRC StreamNotFoundException.java:9-14:
# public StreamNotFoundException() { super(MESSAGE); }
# public StreamNotFoundException(String message) { super(message); }
# public StreamNotFoundException(String message, Throwable cause) { super(message, cause); }
# public StreamNotFoundException(Throwable cause) { super(MESSAGE, cause); }

UNREACHABLE['StreamNotFoundException.<init>(String)'] = ('no_trigger_in_app', 'Constructor overload not used; app throws StreamNotFoundException() or StreamNotFoundException(Throwable)', 'SRC WriteFileAbstraction.java:65,88 throw new StreamNotFoundException(); StreamNotFoundException(e); String-only version unused', 'SOURCE')

UNREACHABLE['StreamNotFoundException.<init>(String,Throwable)'] = ('no_trigger_in_app', 'Constructor overload not used; app uses parameterless and Throwable-only versions', 'SRC StreamNotFoundException.java:11 defined but no callers in app', 'SOURCE')

UNREACHABLE['StreamNotFoundException.<init>(Throwable)'] = ('no_trigger_in_app', 'Constructor overload not used; app uses parameterless version', 'SRC WriteFileAbstraction.java:65,88 shows only new StreamNotFoundException() and StreamNotFoundException(RuntimeException)', 'SOURCE')

# HybridFile overloaded methods
# SRC HybridFile.java:376-399:
# public String getParent() { ... }
# public String getParent(Context context) { ... }

UNREACHABLE['HybridFile.getParent()'] = ('no_trigger_in_app', 'Parameterless overload not used; app calls getParent(Context)', 'GREP no getParent() calls without Context parameter', 'INFERRED')

UNREACHABLE['HybridFile.length()'] = ('no_trigger_in_app', 'Parameterless overload not used; app calls length(Context)', 'SRC HybridFile.java:220,252 both overloads exist; Context version is standard in app', 'INFERRED')

# Operations utility class
# SRC Operations.java:30:
# public class Operations {

e('GeneralDialogCreation.mkDir', 'Operations.<init>', 'CALL',
  'Operations instantiated for filesystem operations',
  evidence='INFERRED Operations is utility class; SRC Operations.java:30 class definition')

# SRC Operations.java:491:
# private static int checkFolder(final File folder, Context context) {

UNREACHABLE['Operations.checkFolder'] = ('no_trigger_in_app', 'Private static helper method called only within Operations class', 'SRC Operations.java:491 private static int checkFolder', 'SOURCE')

# SRC Operations.java:549:
# private static boolean isFileSystemFAT(String mountPoint) {

UNREACHABLE['Operations.isFileSystemFAT'] = ('no_trigger_in_app', 'Private static helper method called only within Operations class', 'SRC Operations.java:549 private static boolean isFileSystemFAT', 'SOURCE')

# PasteHelper Parcelable methods
# SRC PasteHelper.java:21-24:
# private PasteHelper(Parcel in) {
#     operation = in.readInt();
#     paths = (HybridFileParcelable[]) in.readParcelableArray(HybridFileParcelable.class.getClassLoader());
# }
# SRC PasteHelper.java:37-39:
# public PasteHelper createFromParcel(Parcel in) {
#     return new PasteHelper(in);
# }

e('PasteHelper$1.createFromParcel', 'PasteHelper.<init>(Parcel)', 'CALL',
  'Parcel CREATOR.createFromParcel constructs PasteHelper from Parcel',
  evidence='SRC PasteHelper.java:38 return new PasteHelper(in)')

e('PasteHelper.<init>(Parcel)', 'PasteHelper.describeContents', 'FRAMEWORK',
  'Framework calls describeContents during Parcelable operations',
  evidence='INFERRED Android Parcelable contract; SRC PasteHelper.java:27-29')

e('PasteHelper.<init>(Parcel)', 'PasteHelper.writeToParcel', 'FRAMEWORK',
  'Framework calls writeToParcel to serialize PasteHelper state',
  evidence='SRC PasteHelper.java:32-35 dest.writeInt(operation); dest.writeParcelableArray(paths, 0)')
