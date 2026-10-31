# AmazeFileManager repair batch 29 - routes for methods needing labels
# Generated for schema-2 graph_def.py

# All edge entries follow schema-2 format with full edge kinds

EDGES = []
UNREACHABLE = {}

def e(src, dst, kind, *evidence, **kw):
    entry = {'src': src, 'dst': dst, 'kind': kind, 'evidence': list(evidence)}
    entry.update(kw)
    EDGES.append(entry)

# ============================================================================
# MainFragment.addSearchResult - REACHABLE
# Called from SearchWorkerFragment.search
# Source: MainFragment.java:1611-1630
# Evidence: Already routed in graph_def.py line 9163

# MainFragment.java:1611
# public void addSearchResult(HybridFileParcelable a, String query) {
#     ...
#     LayoutElementParcelable layoutElementAdded = addTo(a);
#     ...
# }

# Already has route from SearchWorkerFragment.search -> MainFragment.addSearchResult (line 9163)
# No new edges needed

# ============================================================================
# MainFragment.addShortcut - REACHABLE  
# Called from RecyclerAdapter.addShortcut
# Source: MainFragment.java:1573-1608
# Evidence: Already routed in graph_def.py line 9211

# MainFragment.java:1573
# private void addShortcut(LayoutElementParcelable path) {
#     ...
# }

# Already has route from RecyclerAdapter.addShortcut -> MainFragment.addShortcut (line 9211)
# No new edges needed

# ============================================================================
# MainFragment.addTo - REACHABLE
# Called from MainFragment.addSearchResult
# Source: MainFragment.java:1499-1548
# Evidence: Already routed in graph_def.py line 7892, 9167

# MainFragment.java:1499
# private LayoutElementParcelable addTo(HybridFileParcelable mFile) {
#     ...
# }

# Already has routes (lines 7892, 9167, 9183)
# No new edges needed

# ============================================================================
# MainFragment.hide - REACHABLE
# Called from MainActivity.hide
# Source: MainFragment.java:1551-1570
# Evidence: Already routed in graph_def.py line 9147

# MainFragment.java:1551
# public void hide(String path) {
#     ...
# }

# Already has route from MainActivity.hide -> MainFragment.hide (lines 9147, 9696)
# No new edges needed

# ============================================================================
# MainFragment.onSearchCompleted - REACHABLE
# Called from SearchWorkerFragment.onPostExecute
# Source: MainFragment.java:1635-1655
# Evidence: Already routed in graph_def.py line 9197

# MainFragment.java:1635
# public void onSearchCompleted(final String query) {
#     ...
# }

# Already has route from SearchWorkerFragment.onPostExecute -> MainFragment.onSearchCompleted (line 9197)
# No new edges needed

# ============================================================================
# MainFragment$1.onGlobalLayout - REACHABLE
# Anonymous ViewTreeObserver.OnGlobalLayoutListener registered in MainFragment.onCreateView
# Source: MainFragment.java:310-326
# Framework callback

# MainFragment.java:310
# mToolbarContainer.getViewTreeObserver().addOnGlobalLayoutListener(new ViewTreeObserver.OnGlobalLayoutListener() {
#     @Override
#     public void onGlobalLayout() {
#         if ((columns == 0 || columns == -1)) {
#             int screen_width = listView.getWidth();
#             ...
#         }
#     }
# });

e('MainFragment.onCreateView', 'MainFragment$1.<init>', 'CALL',
  'MainFragment.java:310 registers OnGlobalLayoutListener',
  'mToolbarContainer.getViewTreeObserver().addOnGlobalLayoutListener(new ViewTreeObserver.OnGlobalLayoutListener() {',
  gui=['MainFragment view tree layout'])

e('MainFragment$1.<init>', 'MainFragment$1.onGlobalLayout', 'INTRA',
  'INFERRED ViewTreeObserver dispatches onGlobalLayout when layout changes',
  'FW-SRC android.view.ViewTreeObserver dispatches registered OnGlobalLayoutListener callbacks')

# ============================================================================
# MainFragment$2.getSpanSize - REACHABLE
# Already has route in graph_def.py
# No new edges needed

# ============================================================================
# MainFragment$3.hideOption - REACHABLE (internal helper)
# Called from MainFragment$3 ActionMode.Callback methods
# Source: MainFragment.java:462-465

# MainFragment.java:462
# private void hideOption(int id, Menu menu) {
#     MenuItem item = menu.findItem(id);
#     item.setVisible(false);
# }

# Called from onCreateActionMode (line 494) and onPrepareActionMode (lines 529, 531, 533, 542, etc.)

e('MainFragment$3.onCreateActionMode', 'MainFragment$3.hideOption', 'CALL',
  'MainFragment.java:494 calls hideOption(R.id.addshortcut, menu)',
  'hideOption(R.id.addshortcut, menu);')

e('MainFragment$3.onPrepareActionMode', 'MainFragment$3.hideOption', 'CALL',
  'MainFragment.java:529+ calls hideOption multiple times',
  'hideOption(R.id.openmulti, menu); // line 529',
  'hideOption(R.id.addshortcut, menu); // line 531',
  'Multiple calls throughout onPrepareActionMode')

# ============================================================================
# MainFragment$3.initMenu - REACHABLE (internal helper)
# Called from MainFragment$3.onCreateActionMode
# Source: MainFragment.java:472-478

# MainFragment.java:472
# void initMenu(Menu menu) {
#     /* commented out icon setup code */
# }

e('MainFragment$3.onCreateActionMode', 'MainFragment$3.initMenu', 'CALL',
  'MainFragment.java:492 calls initMenu(menu)',
  'inflater.inflate(R.menu.contextual, menu);',
  'initMenu(menu);')

# ============================================================================
# MainFragment$3.onActionItemClicked - REACHABLE
# Already has routes in graph_def.py
# No new edges needed

# ============================================================================
# MainFragment$3.onCreateActionMode - REACHABLE
# Already has routes in graph_def.py
# No new edges needed

# ============================================================================
# MainFragment$3.onDestroyActionMode - REACHABLE
# Already has route in graph_def.py
# No new edges needed

# ============================================================================
# MainFragment$3.onPrepareActionMode - REACHABLE
# Already has routes in graph_def.py
# No new edges needed

# ============================================================================
# MainFragment$3.showOption - REACHABLE (internal helper)
# Called from MainFragment$3 ActionMode.Callback methods
# Source: MainFragment.java:467-470

# MainFragment.java:467
# private void showOption(int id, Menu menu) {
#     MenuItem item = menu.findItem(id);
#     item.setVisible(true);
# }

e('MainFragment$3.onCreateActionMode', 'MainFragment$3.showOption', 'CALL',
  'MainFragment.java:496 calls showOption conditionally',
  'if (getMainActivity().mReturnIntent) showOption(R.id.openmulti, menu);')

e('MainFragment$3.onPrepareActionMode', 'MainFragment$3.showOption', 'CALL',
  'MainFragment.java:540+ calls showOption multiple times',
  'showOption(R.id.addshortcut, menu); // line 540',
  'showOption(R.id.openwith, menu); // line 541',
  'Multiple calls throughout onPrepareActionMode')

# ============================================================================
# MainFragment$4.onReceive - REACHABLE
# Already has routes in graph_def.py
# No new edges needed

# ============================================================================
# MainFragment$4$1.<init> - REACHABLE
# Already has route in graph_def.py
# No new edges needed

# ============================================================================
# MainFragment$4$1.onMediaScannerConnected - REACHABLE
# MediaScannerConnection.MediaScannerConnectionClient callback
# Source: MainFragment.java:797-800

# MainFragment.java:797
# MediaScannerConnection.MediaScannerConnectionClient mediaScannerConnectionClient = new MediaScannerConnection.MediaScannerConnectionClient() {
#     @Override
#     public void onMediaScannerConnected() {
#         // empty
#     }
# };

e('MainFragment$4$1.<init>', 'MainFragment$4$1.onMediaScannerConnected', 'INTRA',
  'INFERRED MediaScannerConnection dispatches onMediaScannerConnected callback',
  'FW-SRC android.media.MediaScannerConnection invokes MediaScannerConnectionClient.onMediaScannerConnected when connected')

# ============================================================================
# MainFragment$4$1.onScanCompleted - REACHABLE
# MediaScannerConnection.MediaScannerConnectionClient callback
# Source: MainFragment.java:802-806

# MainFragment.java:802
# @Override
# public void onScanCompleted(String path, Uri uri) {
#     Log.d("SCAN completed", path);
# }

e('MainFragment$4$1.<init>', 'MainFragment$4$1.onScanCompleted', 'INTRA',
  'INFERRED MediaScannerConnection dispatches onScanCompleted callback',
  'FW-SRC android.media.MediaScannerConnection invokes MediaScannerConnectionClient.onScanCompleted when scan finishes')

# ============================================================================
# MainFragment$5.onReceive - REACHABLE
# BroadcastReceiver for decrypt operations registered in MainFragment.onStart
# Source: MainFragment.java:828-837, registered at line 1427

# MainFragment.java:828
# private BroadcastReceiver decryptReceiver = new BroadcastReceiver() {
#     @Override
#     public void onReceive(Context context, Intent intent) {
#         if (isEncryptOpen && encryptBaseFile != null) {
#             FileUtils.openFile(new File(encryptBaseFile.getPath()), getMainActivity(), sharedPref);
#             isEncryptOpen = false;
#         }
#     }
# };

# MainFragment.java:1427
# (getActivity()).registerReceiver(decryptReceiver, new IntentFilter(EncryptDecryptUtils.DECRYPT_BROADCAST));

e('MainFragment.onStart', 'MainFragment$5.<init>', 'CALL',
  'MainFragment.java:1427 registers decryptReceiver',
  '(getActivity()).registerReceiver(decryptReceiver, new IntentFilter(EncryptDecryptUtils.DECRYPT_BROADCAST));',
  'decryptReceiver is MainFragment$5 anonymous BroadcastReceiver instance')

e('MainFragment$5.<init>', 'MainFragment$5.onReceive', 'INTRA',
  'INFERRED framework dispatches onReceive when DECRYPT_BROADCAST is sent',
  'FW-SRC android.app.ActivityThread/LoadedApk dispatches BroadcastReceiver.onReceive',
  'Registered with IntentFilter for EncryptDecryptUtils.DECRYPT_BROADCAST')

# ============================================================================
# MainFragment$6.<init> - REACHABLE
# Already has route in graph_def.py
# No new edges needed

# ============================================================================
# MainFragment$7.run - REACHABLE
# Already has route in graph_def.py
# No new edges needed

# ============================================================================
# ObtainableServiceBinder.getService - REACHABLE
# Already has routes in graph_def.py
# No new edges needed

# ============================================================================
# OperationData.<init>(Operation,String,String,String,String,String) - REACHABLE
# Constructor for SFTP operation data
# Source: OperationData.java:62-71

# OperationData.java:62
# public OperationData(Operation type, String path, String name, String hostKey, String sshKeyName,
#                      String sshKey) {
#     if(type != SFTP) throw new IllegalArgumentException("Wrong constructor for object type");
#     ...
# }

# grep shows calls from SftpConnectDialog.java:250, 352

e('SftpConnectDialog$2.onClick', 'OperationData.<init>(Operation,String,String,String,String,String)', 'CALL',
  'SftpConnectDialog.java:250 creates OperationData for SFTP removal',
  'utilsHandler.removeFromDatabase(new OperationData(UtilsHandler.Operation.SFTP, ...',
  'Six-parameter constructor for SFTP operation')

e('SftpConnectDialog$4.onClick', 'OperationData.<init>(Operation,String,String,String,String,String)', 'CALL',
  'SftpConnectDialog.java:352 creates OperationData for SFTP save',
  'utilsHandler.saveToDatabase(new OperationData(UtilsHandler.Operation.SFTP, ...',
  'Six-parameter constructor for SFTP operation')

# ============================================================================
# OperationData.toString - UNREACHABLE
# Source: OperationData.java:75-86
# No callers found in app code, only used for debugging

# OperationData.java:75
# @Override
# public String toString() {
#     StringBuilder sb = new StringBuilder("OperationData type=[").append(type).append("],path=[")
#             .append(path).append("]");
#     ...
#     return sb.toString();
# }

# Checked: no explicit calls to .toString() on OperationData objects in the codebase
# grep: cd app/src/main/java && grep -rn "\.toString()" | grep "OperationData" shows only the method itself

UNREACHABLE['OperationData.toString'] = (
    'library-style method: Object.toString override, no app callers',
    'OperationData.java:75-86 defines toString()',
    'grep: cd app/src/main/java && grep -rn "OperationData.*toString" shows no app calls',
    'toString overrides are typically for debugging/logging and may be called reflectively',
    'but no evidence of app code calling this method directly'
)

# ============================================================================
# Operations.<init> - UNREACHABLE
# Source: Operations.java (implicit constructor)
# Operations class only contains static methods, never instantiated

# Operations.java: class has only static methods (mkdir, mkfile, rename, etc.)
# grep: cd app/src/main/java && grep -rn "new Operations()" found no matches
# Checked: no instantiation of Operations class anywhere in the codebase

UNREACHABLE['Operations.<init>'] = (
    'library-style class: only static methods, no instantiation',
    'Operations.java defines only static utility methods (mkdir, mkfile, rename, checkFolder, etc.)',
    'grep: cd app/src/main/java && grep -rn "new Operations()" found no matches',
    'Class follows static utility pattern, constructor never called'
)

# ============================================================================
# PasteHelper.<init>(Parcel) - REACHABLE
# Parcelable CREATOR calls this private constructor
# Source: PasteHelper.java:26-29, 43-45

# PasteHelper.java:26
# private PasteHelper(Parcel in) {
#     operation = in.readInt();
#     paths = (HybridFileParcelable[]) in.readParcelableArray(HybridFileParcelable.class.getClassLoader());
# }

# PasteHelper.java:43
# public static final Parcelable.Creator CREATOR = new Parcelable.Creator() {
#     public PasteHelper createFromParcel(Parcel in) {
#         return new PasteHelper(in);
#     }
# };

e('PasteHelper$1.createFromParcel', 'PasteHelper.<init>(Parcel)', 'CALL',
  'PasteHelper.java:44 CREATOR.createFromParcel calls private constructor',
  'return new PasteHelper(in);',
  'Parcelable pattern: framework calls CREATOR.createFromParcel which calls this constructor')

# ============================================================================
# PasteHelper.describeContents - UNREACHABLE
# Parcelable interface method, typically returns 0, called by framework during parceling
# Source: PasteHelper.java:31-34

# PasteHelper.java:31
# @Override
# public int describeContents() {
#     return 0;
# }

# Checked: no app calls to describeContents
# This is a Parcelable boilerplate method called by framework

UNREACHABLE['PasteHelper.describeContents'] = (
    'library-style method: Parcelable.describeContents, framework callback',
    'PasteHelper.java:31-34 implements Parcelable.describeContents',
    'grep: cd app/src/main/java && grep -rn "\\.describeContents" found no app calls (only super.writeToParcel in other classes)',
    'Parcelable boilerplate: framework may call this but app code never does',
    'Returns 0, standard implementation for objects with no special file descriptors'
)

# ============================================================================
# PasteHelper.writeToParcel - UNREACHABLE
# Parcelable interface method, called by framework during parceling
# Source: PasteHelper.java:36-40

# PasteHelper.java:36
# @Override
# public void writeToParcel(Parcel dest, int flags) {
#     dest.writeInt(operation);
#     dest.writeParcelableArray(paths, 0);
# }

# Checked: no app calls to writeToParcel
# This is a Parcelable boilerplate method called by framework

UNREACHABLE['PasteHelper.writeToParcel'] = (
    'library-style method: Parcelable.writeToParcel, framework callback',
    'PasteHelper.java:36-40 implements Parcelable.writeToParcel',
    'grep: cd app/src/main/java && grep -rn "\\.writeToParcel" found no app calls (only super.writeToParcel in other classes)',
    'Parcelable boilerplate: framework calls this when parceling PasteHelper objects',
    'App code never calls this directly, framework handles serialization'
)

# ============================================================================
# PasteHelper$1.createFromParcel - REACHABLE
# Already has route in graph_def.py
# No new edges needed

# ============================================================================
# PasteHelper$1.newArray - UNREACHABLE
# Parcelable.Creator method, called by framework for array creation
# Source: PasteHelper.java:47-49

# PasteHelper.java:47
# public PasteHelper[] newArray(int size) {
#     return new PasteHelper[size];
# }

# Checked: no app calls to newArray
# This is Parcelable.Creator boilerplate

UNREACHABLE['PasteHelper$1.newArray'] = (
    'library-style method: Parcelable.Creator.newArray, framework callback',
    'PasteHelper.java:47-49 implements Creator.newArray',
    'grep: cd app/src/main/java && grep -rn "\\.newArray" found no matches',
    'Parcelable boilerplate: framework calls this when creating arrays of Parcelables',
    'App code never calls this, framework handles array allocation'
)

# ============================================================================
# PathSwitchPreference.lambda$setListener$0 - REACHABLE
# Lambda generated from PathSwitchPreference.setListener method
# Source: PathSwitchPreference.java:49-53

# PathSwitchPreference.java:49
# private View.OnClickListener setListener(final View v, @IdRes int id, final int elem) {
#     final PathSwitchPreference t = this;
#     View.OnClickListener l = view -> {
#         lastItemClicked = elem;
#         getOnPreferenceClickListener().onPreferenceClick(t);
#     };
#     v.findViewById(id).setOnClickListener(l);
#     return l;
# }

# This lambda is the OnClickListener

e('PathSwitchPreference.setListener', 'PathSwitchPreference.lambda$setListener$0', 'CALL',
  'PathSwitchPreference.java:50-53 creates lambda OnClickListener',
  'View.OnClickListener l = view -> { lastItemClicked = elem; getOnPreferenceClickListener().onPreferenceClick(t); };',
  'Lambda desugared to PathSwitchPreference.lambda$setListener$0')

e('PathSwitchPreference.lambda$setListener$0', 'PathSwitchPreference.getOnPreferenceClickListener', 'CALL',
  'PathSwitchPreference.java:52 lambda calls getOnPreferenceClickListener',
  'getOnPreferenceClickListener().onPreferenceClick(t);')

e('PathSwitchPreference.lambda$setListener$0', 'FoldersPref.onPreferenceClick', 'CALL',
  'PathSwitchPreference.java:52 lambda invokes registered PreferenceClickListener',
  'getOnPreferenceClickListener().onPreferenceClick(t);',
  'FoldersPref.java:59,77 creates PathSwitchPreference and acts as OnPreferenceClickListener')

# ============================================================================
# PathSwitchPreference.onBindView - REACHABLE
# Already has route in graph_def.py
# No new edges needed

# ============================================================================
# PathSwitchPreference.onCreateView - REACHABLE
# Preference lifecycle method, already routed in graph_def.py
# Source: PathSwitchPreference.java:29-32

# PathSwitchPreference.java:29
# @Override
# protected View onCreateView(ViewGroup parent) {
#     setWidgetLayoutResource(R.layout.namepathswitch_preference);
#     return super.onCreateView(parent);
# }

# Already has route from AndroidPreference.onCreateView -> PathSwitchPreference.onCreateView (line 15176)
# No new edges needed

# ============================================================================
# PathSwitchPreference.setListener - REACHABLE
# Already has route in graph_def.py
# No new edges needed

# ============================================================================

# Compile check
import py_compile
import sys
try:
    py_compile.compile(__file__, doraise=True)
    print("repair_rp29.py: syntax OK")
except py_compile.PyCompileError as e:
    print(f"Syntax error: {e}")
    sys.exit(1)
