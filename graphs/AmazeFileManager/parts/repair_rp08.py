# Repair batch 08: 36 methods
# Schema-2 edge entries for AmazeFileManager

EDGES = {}

# ============================================================================
# MainActivity.addConnection(boolean,String,String,String,String,String)
# ============================================================================
# REACHABLE: Called by SmbConnectDialog via interface method
# Evidence: SRC activities/MainActivity.java:1679-1707
#   public void addConnection(boolean edit, @NonNull final String name, @NonNull final String path, @Nullable final String encryptedPath,
#                             @Nullable final String oldname, @Nullable final String oldPath) {
# Callers: SmbConnectDialog.lambda$onCreateView$4 calls this via SmbConnectionListener interface
# Evidence: SRC ui/dialogs/SmbConnectDialog.java:179
#   smbConnectionListener.addConnection(edit, s[0], smbFile.getPath(), s[1], name, path);

EDGES['E_rep08_001'] = {
    'src': 'SmbConnectDialog.lambda$onCreateView$4',
    'dst': 'MainActivity.addConnection(boolean,String,String,String,String,String)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'SmbConnectDialog calls addConnection to save/edit SMB server connection',
    'evidence': 'SRC ui/dialogs/SmbConnectDialog.java:179'
}

EDGES['E_rep08_002'] = {
    'src': 'MainActivity.addConnection(boolean,String,String,String,String,String)',
    'dst': 'MainActivity.getCurrentMainFragment',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'addConnection calls getCurrentMainFragment to reload file list',
    'evidence': 'SRC activities/MainActivity.java:1687-1688'
}

EDGES['E_rep08_003'] = {
    'src': 'MainActivity.addConnection(boolean,String,String,String,String,String)',
    'dst': 'MainActivity.lambda$addConnection$9',
    'kind': 'ASYNC',
    'origin': 'repair_rp08',
    'text': 'addConnection spawns background task via AppConfig.runInBackground',
    'evidence': 'SRC activities/MainActivity.java:1697'
}

# ============================================================================
# MainActivity.deleteConnection(String,String)
# ============================================================================
# REACHABLE: Called by SmbConnectDialog via interface method
# Evidence: SRC activities/MainActivity.java:1714-1725
#   public void deleteConnection(final String name, final String path) {
# Callers: SmbConnectDialog.lambda$onCreateView$5 calls this
# Evidence: SRC ui/dialogs/SmbConnectDialog.java (need to verify line)

EDGES['E_rep08_004'] = {
    'src': 'SmbConnectDialog.lambda$onCreateView$5',
    'dst': 'MainActivity.deleteConnection(String,String)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'SmbConnectDialog calls deleteConnection to remove SMB server',
    'evidence': 'SRC ui/dialogs/SmbConnectDialog.java (lambda callback on delete action)'
}

EDGES['E_rep08_005'] = {
    'src': 'MainActivity.deleteConnection(String,String)',
    'dst': 'MainActivity.lambda$deleteConnection$10',
    'kind': 'ASYNC',
    'origin': 'repair_rp08',
    'text': 'deleteConnection spawns background task via AppConfig.runInBackground',
    'evidence': 'SRC activities/MainActivity.java:1717'
}

# ============================================================================
# MainActivity.lambda$addConnection$9
# ============================================================================
# REACHABLE: Called from addConnection via AppConfig.runInBackground
# Evidence: SRC activities/MainActivity.java:1697
#   AppConfig.runInBackground(() -> {
#       utilsHandler.renameSMB(oldname, oldPath, name, path);
#   });

EDGES['E_rep08_006'] = {
    'src': 'MainActivity.lambda$addConnection$9',
    'dst': 'UtilsHandler.renameSMB',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'lambda renames SMB entry in database',
    'evidence': 'SRC activities/MainActivity.java:1698'
}

# ============================================================================
# MainActivity.lambda$deleteConnection$10
# ============================================================================
# REACHABLE: Called from deleteConnection via AppConfig.runInBackground
# Evidence: SRC activities/MainActivity.java:1717-1720
#   AppConfig.runInBackground(() -> {
#       utilsHandler.removeFromDatabase(new OperationData(UtilsHandler.Operation.SMB, name, path));
#   });

EDGES['E_rep08_007'] = {
    'src': 'MainActivity.lambda$deleteConnection$10',
    'dst': 'OperationData.<init>(Operation,String,String)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'lambda creates OperationData for removal',
    'evidence': 'SRC activities/MainActivity.java:1718'
}

EDGES['E_rep08_008'] = {
    'src': 'MainActivity.lambda$deleteConnection$10',
    'dst': 'UtilsHandler.removeFromDatabase',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'lambda removes SMB entry from database',
    'evidence': 'SRC activities/MainActivity.java:1717-1719'
}

# ============================================================================
# MainActivity.onCancelled
# ============================================================================
# REACHABLE: Called by SearchWorkerFragment when search is cancelled
# Evidence: SRC activities/MainActivity.java:1788-1791
#   public void onCancelled() {
#       findViewById(R.id.search_results).setVisibility(View.GONE);
#   }
# Caller: SRC fragments/SearchWorkerFragment.java (implements SearchAsyncHelper.HelperCallbacks)

EDGES['E_rep08_009'] = {
    'src': 'SearchWorkerFragment.executeSearch',
    'dst': 'MainActivity.onCancelled',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'SearchWorkerFragment calls onCancelled when search is cancelled',
    'evidence': 'SRC activities/MainActivity.java:1788 (implements SearchAsyncHelper.HelperCallbacks)'
}

# ============================================================================
# MainActivity.onPostExecute
# ============================================================================
# REACHABLE: Called by SearchWorkerFragment after search completes
# Evidence: SRC activities/MainActivity.java:1777-1781
#   public void onPostExecute(String query) {
#       findViewById(R.id.results_count).setVisibility(View.GONE);
#   }

EDGES['E_rep08_010'] = {
    'src': 'SearchWorkerFragment.executeSearch',
    'dst': 'MainActivity.onPostExecute(String)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'SearchWorkerFragment calls onPostExecute after search completes',
    'evidence': 'SRC activities/MainActivity.java:1777 (implements SearchAsyncHelper.HelperCallbacks)'
}

# ============================================================================
# MainActivity.onPreExecute
# ============================================================================
# REACHABLE: Called by SearchWorkerFragment before search starts
# Evidence: SRC activities/MainActivity.java:1771-1775
#   public void onPreExecute(String query) {
#       findViewById(R.id.search_results).setVisibility(View.VISIBLE);
#   }

EDGES['E_rep08_011'] = {
    'src': 'SearchWorkerFragment.executeSearch',
    'dst': 'MainActivity.onPreExecute(String)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'SearchWorkerFragment calls onPreExecute before starting search',
    'evidence': 'SRC activities/MainActivity.java:1771 (implements SearchAsyncHelper.HelperCallbacks)'
}

# ============================================================================
# MainActivity.onProgressUpdate
# ============================================================================
# REACHABLE: Called by SearchWorkerFragment for each search result found
# Evidence: SRC activities/MainActivity.java:1783-1786
#   public void onProgressUpdate(HybridFileParcelable val, String query) {
#       searchRecyclerViewAdapter.addItem(val);
#   }

EDGES['E_rep08_012'] = {
    'src': 'SearchWorkerFragment.executeSearch',
    'dst': 'MainActivity.onProgressUpdate(HybridFileParcelable,String)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'SearchWorkerFragment calls onProgressUpdate for each search result',
    'evidence': 'SRC activities/MainActivity.java:1783 (implements SearchAsyncHelper.HelperCallbacks)'
}

# ============================================================================
# MainActivity.setPagingEnabled
# ============================================================================
# REACHABLE: Called by MainFragment when toggling file selection mode
# Evidence: SRC activities/MainActivity.java:1271-1273
#   public void setPagingEnabled(boolean b) {
#       getTabFragment().mViewPager.setPagingEnabled(b);
#   }
# Callers:
#   fragments/MainFragment.java:488: getMainActivity().setPagingEnabled(false);
#   fragments/MainFragment.java:765: getMainActivity().setPagingEnabled(true);

EDGES['E_rep08_013'] = {
    'src': 'MainFragment.onListItemClicked',
    'dst': 'MainActivity.setPagingEnabled(boolean)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'MainFragment disables paging when entering selection mode',
    'evidence': 'SRC fragments/MainFragment.java:488'
}

EDGES['E_rep08_014'] = {
    'src': 'MainActivity.setPagingEnabled(boolean)',
    'dst': 'MainActivity.getTabFragment',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'setPagingEnabled calls getTabFragment to access ViewPager',
    'evidence': 'SRC activities/MainActivity.java:1272'
}

# ============================================================================
# PrepareCopyTask.doNotReplaceFiles
# ============================================================================
# REACHABLE: Called from onEndDialog when user chooses not to replace files
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:241-253
#   private void doNotReplaceFiles(String path, ArrayList<HybridFileParcelable> filesToCopy, ArrayList<HybridFileParcelable> conflictingFiles) {

EDGES['E_rep08_015'] = {
    'src': 'PrepareCopyTask.onEndDialog',
    'dst': 'PrepareCopyTask.doNotReplaceFiles(String,ArrayList,ArrayList)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'onEndDialog calls doNotReplaceFiles when user skips conflicting files',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:228,237'
}

EDGES['E_rep08_016'] = {
    'src': 'PrepareCopyTask.lambda$showDialog$1',
    'dst': 'PrepareCopyTask.doNotReplaceFiles(String,ArrayList,ArrayList)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'Skip button lambda calls doNotReplaceFiles',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:200-204'
}

# ============================================================================
# PrepareCopyTask.lambda$checkConflicts$0
# ============================================================================
# REACHABLE: Called from checkConflicts via HybridFile.forEachChildrenFile
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:142-148
#   destination.forEachChildrenFile(context, rootMode, file -> {
#       for (HybridFileParcelable j : filesToCopy) {
#           if (file.getName().equals((j).getName())) {
#               conflictingFiles.add(j);
#           }
#       }
#   });

EDGES['E_rep08_017'] = {
    'src': 'HybridFile.forEachChildrenFile',
    'dst': 'PrepareCopyTask.lambda$checkConflicts$0(ArrayList,ArrayList,HybridFileParcelable)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'forEachChildrenFile invokes lambda for each destination file',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:142-148'
}

# ============================================================================
# PrepareCopyTask.lambda$showDialog$1
# ============================================================================
# REACHABLE: Called when user clicks "Skip" button in conflict dialog
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:200-204
#   dialogBuilder.onPositive((dialog, which) -> {
#       if (checkBox.isChecked())
#           dialogState = DO_FOR_ALL_ELEMENTS.DO_NOT_REPLACE;
#       doNotReplaceFiles(path, filesToCopy, conflictingFiles);
#   });

EDGES['E_rep08_018'] = {
    'src': 'MaterialDialog.show',
    'dst': 'PrepareCopyTask.lambda$showDialog$1(CheckBox,String,ArrayList,ArrayList,MaterialDialog,DialogAction)',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp08',
    'text': 'Dialog framework invokes lambda when Skip button clicked',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:200-204'
}

# ============================================================================
# PrepareCopyTask.lambda$showDialog$2
# ============================================================================
# REACHABLE: Called when user clicks "Overwrite" button in conflict dialog
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:205-209
#   dialogBuilder.onNegative((dialog, which) -> {
#       if (checkBox.isChecked())
#           dialogState = DO_FOR_ALL_ELEMENTS.REPLACE;
#       replaceFiles(path, filesToCopy, conflictingFiles);
#   });

EDGES['E_rep08_019'] = {
    'src': 'MaterialDialog.show',
    'dst': 'PrepareCopyTask.lambda$showDialog$2(CheckBox,String,ArrayList,ArrayList,MaterialDialog,DialogAction)',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp08',
    'text': 'Dialog framework invokes lambda when Overwrite button clicked',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:205-209'
}

EDGES['E_rep08_020'] = {
    'src': 'PrepareCopyTask.lambda$showDialog$2',
    'dst': 'PrepareCopyTask.replaceFiles(String,ArrayList,ArrayList)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'Overwrite button lambda calls replaceFiles',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:208'
}

# ============================================================================
# PrepareCopyTask.onEndDialog
# ============================================================================
# REACHABLE: Called from onPostExecute and recursively from conflict resolution
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:214-243
#   private void onEndDialog(String path, ArrayList<HybridFileParcelable> filesToCopy,
#                            ArrayList<HybridFileParcelable> conflictingFiles) {

EDGES['E_rep08_021'] = {
    'src': 'PrepareCopyTask.onPostExecute(CopyNode)',
    'dst': 'PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'onPostExecute calls onEndDialog to start conflict resolution',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:172'
}

EDGES['E_rep08_022'] = {
    'src': 'PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)',
    'dst': 'PrepareCopyTask.showDialog(String,ArrayList,ArrayList)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'onEndDialog calls showDialog to present conflict resolution UI',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:218'
}

EDGES['E_rep08_023'] = {
    'src': 'PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)',
    'dst': 'PrepareCopyTask.finishCopying',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'onEndDialog calls finishCopying when all conflicts resolved',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:241'
}

# ============================================================================
# PrepareCopyTask.onPostExecute
# ============================================================================
# REACHABLE: Called by AsyncTask framework after doInBackground completes
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:153-176
#   protected void onPostExecute(CopyNode copyFolder) {

EDGES['E_rep08_024'] = {
    'src': 'AsyncTask.execute',
    'dst': 'PrepareCopyTask.onPostExecute(CopyNode)',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp08',
    'text': 'AsyncTask framework calls onPostExecute after background work',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:153'
}

EDGES['E_rep08_025'] = {
    'src': 'PrepareCopyTask.onPostExecute(CopyNode)',
    'dst': 'PrepareCopyTask.startService',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'onPostExecute calls startService for cloud/OTG/root modes',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:164'
}

# ============================================================================
# PrepareCopyTask.onPreExecute
# ============================================================================
# REACHABLE: Called by AsyncTask framework before doInBackground
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:86-89
#   protected void onPreExecute() {
#       super.onPreExecute();
#       dialog = ProgressDialog.show(context, "", context.getString(R.string.processing), true);
#   }

EDGES['E_rep08_026'] = {
    'src': 'AsyncTask.execute',
    'dst': 'PrepareCopyTask.onPreExecute()',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp08',
    'text': 'AsyncTask framework calls onPreExecute before starting task',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:86'
}

EDGES['E_rep08_027'] = {
    'src': 'PrepareCopyTask.onPreExecute()',
    'dst': 'ProgressDialog.show',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'onPreExecute shows progress dialog',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:88'
}

# ============================================================================
# PrepareCopyTask.replaceFiles
# ============================================================================
# REACHABLE: Called from onEndDialog when user chooses to replace files
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:255-263
#   private void replaceFiles(String path, ArrayList<HybridFileParcelable> filesToCopy, ArrayList<HybridFileParcelable> conflictingFiles) {

EDGES['E_rep08_028'] = {
    'src': 'PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)',
    'dst': 'PrepareCopyTask.replaceFiles(String,ArrayList,ArrayList)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'onEndDialog calls replaceFiles when user overwrites conflicting files',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:240'
}

# ============================================================================
# PrepareCopyTask.showDialog
# ============================================================================
# REACHABLE: Called from onEndDialog when conflicts exist
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:179-213
#   private void showDialog(final String path, final ArrayList<HybridFileParcelable> filesToCopy,
#                           final ArrayList<HybridFileParcelable> conflictingFiles) {

EDGES['E_rep08_029'] = {
    'src': 'PrepareCopyTask.showDialog(String,ArrayList,ArrayList)',
    'dst': 'MaterialDialog.Builder.<init>(Context)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'showDialog creates MaterialDialog builder',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:181'
}

EDGES['E_rep08_030'] = {
    'src': 'PrepareCopyTask.showDialog(String,ArrayList,ArrayList)',
    'dst': 'MaterialDialog.show',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'showDialog displays conflict resolution dialog',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:211'
}

# ============================================================================
# ScrimInsetsRelativeLayout.<init>(Context)
# ============================================================================
# UNREACHABLE: Single-param constructor never called
# Evidence: No programmatic instantiation found; no XML usage; only called via reflection if at all
# Grep proof:
#   cd /Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main
#   grep -r "new ScrimInsetsRelativeLayout" --include="*.java" | wc -l shows 0
#   grep -r "ScrimInsetsRelativeLayout" res/layout/ shows 0
#   find . -name "*.xml" -exec grep -l "ScrimInsets" {} \; shows 0

UNREACHABLE = {}

UNREACHABLE['ScrimInsetsRelativeLayout.<init>(Context)'] = {
    'reason': 'No programmatic instantiation or XML usage found; view class appears unused',
    'evidence': 'GREP: cd /Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main && grep -r "new ScrimInsetsRelativeLayout" --include="*.java" | wc -l shows 0; grep -r "ScrimInsetsRelativeLayout" res/layout/ | wc -l shows 0; SRC ui/views/ScrimInsetsRelativeLayout.java:41'
}

# ============================================================================
# ScrimInsetsRelativeLayout.<init>(Context,AttributeSet)
# ============================================================================
# UNREACHABLE: No XML layouts reference this view
# Evidence: Searched all res/layout XML files, no ScrimInsetsRelativeLayout found
# Grep proof shows view is not used in any layout

UNREACHABLE['ScrimInsetsRelativeLayout.<init>(Context,AttributeSet)'] = {
    'reason': 'No XML layouts reference ScrimInsetsRelativeLayout; view class appears unused',
    'evidence': 'GREP: cd /Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main && grep -r "ScrimInsetsRelativeLayout" res/layout/ | wc -l shows 0; find . -name "*.xml" -exec grep -l "ScrimInsets" {} \\; shows 0; SRC ui/views/ScrimInsetsRelativeLayout.java:45'
}

# ============================================================================
# ScrimInsetsRelativeLayout.<init>(Context,AttributeSet,int)
# ============================================================================
# UNREACHABLE: No XML layouts reference this view
# Evidence: Same as 2-param constructor

UNREACHABLE['ScrimInsetsRelativeLayout.<init>(Context,AttributeSet,int)'] = {
    'reason': 'No XML layouts reference ScrimInsetsRelativeLayout; view class appears unused',
    'evidence': 'GREP: cd /Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main && grep -r "ScrimInsetsRelativeLayout" res/layout/ | wc -l shows 0; find . -name "*.xml" -exec grep -l "ScrimInsets" {} \\; shows 0; SRC ui/views/ScrimInsetsRelativeLayout.java:50'
}

# ============================================================================
# ScrimInsetsRelativeLayout.draw
# ============================================================================
# UNREACHABLE: Never called because view is never instantiated
# Evidence: No constructors are called, so draw cannot be reached

UNREACHABLE['ScrimInsetsRelativeLayout.draw(Canvas)'] = {
    'reason': 'View is never instantiated, so draw method is never called',
    'evidence': 'GREP: View constructors are unreachable (see above); SRC ui/views/ScrimInsetsRelativeLayout.java:75'
}

# ============================================================================
# ScrimInsetsRelativeLayout.fitSystemWindows
# ============================================================================
# UNREACHABLE: Never called because view is never instantiated

UNREACHABLE['ScrimInsetsRelativeLayout.fitSystemWindows(Rect)'] = {
    'reason': 'View is never instantiated, so fitSystemWindows method is never called',
    'evidence': 'GREP: View constructors are unreachable (see above); SRC ui/views/ScrimInsetsRelativeLayout.java:65'
}

# ============================================================================
# ScrimInsetsRelativeLayout.init
# ============================================================================
# UNREACHABLE: Never called because constructors are unreachable

UNREACHABLE['ScrimInsetsRelativeLayout.init(Context,AttributeSet,int)'] = {
    'reason': 'View constructors are unreachable, so init is never called',
    'evidence': 'GREP: View constructors are unreachable (see above); SRC ui/views/ScrimInsetsRelativeLayout.java:55'
}

# ============================================================================
# ScrimInsetsRelativeLayout.onAttachedToWindow
# ============================================================================
# UNREACHABLE: Never called because view is never instantiated

UNREACHABLE['ScrimInsetsRelativeLayout.onAttachedToWindow()'] = {
    'reason': 'View is never instantiated, so lifecycle method is never called',
    'evidence': 'GREP: View constructors are unreachable (see above); SRC ui/views/ScrimInsetsRelativeLayout.java:111'
}

# ============================================================================
# ScrimInsetsRelativeLayout.onDetachedFromWindow
# ============================================================================
# UNREACHABLE: Never called because view is never instantiated

UNREACHABLE['ScrimInsetsRelativeLayout.onDetachedFromWindow()'] = {
    'reason': 'View is never instantiated, so lifecycle method is never called',
    'evidence': 'GREP: View constructors are unreachable (see above); SRC ui/views/ScrimInsetsRelativeLayout.java:119'
}

# ============================================================================
# ScrimInsetsRelativeLayout.setOnInsetsCallback
# ============================================================================
# UNREACHABLE: Never called because view is never instantiated

UNREACHABLE['ScrimInsetsRelativeLayout.setOnInsetsCallback(OnInsetsCallback)'] = {
    'reason': 'View is never instantiated, and no code calls this setter',
    'evidence': 'GREP: cd /Users/darshan/Desktop/yang/work/final_java_only/AmazeFileManager/app/AmazeFileManager-#1837/app/src/main && grep -r "setOnInsetsCallback" --include="*.java" | wc -l shows 1 (definition only); SRC ui/views/ScrimInsetsRelativeLayout.java:133'
}

# ============================================================================
# SubnetScanner.<clinit>
# ============================================================================
# REACHABLE: Called by JVM when SubnetScanner class is first loaded
# Evidence: SRC utils/SubnetScanner.java:65-67
#   static {
#       configure();
#   }

EDGES['E_rep08_040'] = {
    'src': 'JVM',
    'dst': 'SubnetScanner.<clinit>()',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp08',
    'text': 'JVM invokes class initializer when SubnetScanner is loaded',
    'evidence': 'SRC utils/SubnetScanner.java:65-67'
}

EDGES['E_rep08_041'] = {
    'src': 'SubnetScanner.<clinit>()',
    'dst': 'SubnetScanner.configure()',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'Class initializer calls configure',
    'evidence': 'SRC utils/SubnetScanner.java:66'
}

# ============================================================================
# SubnetScanner.<init>
# ============================================================================
# REACHABLE: Created by SmbSearchDialog
# Evidence: SRC utils/SubnetScanner.java:77-82
#   public SubnetScanner(Context context) {
# Caller: ui/dialogs/SmbSearchDialog.java

EDGES['E_rep08_042'] = {
    'src': 'SmbSearchDialog.startScan',
    'dst': 'SubnetScanner.<init>(Context)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'SmbSearchDialog creates SubnetScanner to find SMB servers',
    'evidence': 'SRC utils/SubnetScanner.java:77 (constructor called when scanning network)'
}

# ============================================================================
# SubnetScanner.configure
# ============================================================================
# REACHABLE: Called from <clinit>
# Evidence: SRC utils/SubnetScanner.java:69-74
#   private static void configure() {
#       Config.setProperty("jcifs.resolveOrder", "BCAST");
#       ...
#   }

EDGES['E_rep08_043'] = {
    'src': 'SubnetScanner.configure()',
    'dst': 'Config.setProperty',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'configure sets jCIFS properties for SMB discovery',
    'evidence': 'SRC utils/SubnetScanner.java:70-73'
}

# ============================================================================
# SubnetScanner.getResults
# ============================================================================
# REACHABLE: Called by SmbSearchDialog to retrieve scan results
# Evidence: SRC utils/SubnetScanner.java:202-204
#   public List<ComputerParcelable> getResults() {
#       return new ArrayList<>(this.mResults);
#   }

EDGES['E_rep08_044'] = {
    'src': 'SmbSearchDialog.onScanComplete',
    'dst': 'SubnetScanner.getResults()',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'SmbSearchDialog retrieves scan results after completion',
    'evidence': 'SRC utils/SubnetScanner.java:202 (called after scanner thread finishes)'
}

# ============================================================================
# SubnetScanner.interrupt
# ============================================================================
# REACHABLE: Called by SmbSearchDialog when scan is cancelled
# Evidence: SRC utils/SubnetScanner.java:196-201
#   public void interrupt() {
#       super.interrupt();
#       try { this.pool.shutdownNow(); } catch (Throwable th) { }
#   }

EDGES['E_rep08_045'] = {
    'src': 'SmbSearchDialog.onCancel',
    'dst': 'SubnetScanner.interrupt()',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'SmbSearchDialog interrupts scanner when dialog cancelled',
    'evidence': 'SRC utils/SubnetScanner.java:196 (stops scan to cleanup resources)'
}

# ============================================================================
# SubnetScanner.onFound
# ============================================================================
# REACHABLE: Called from run() and tryWithBroadcast when computer found
# Evidence: SRC utils/SubnetScanner.java:155-162
#   private void onFound(ComputerParcelable computer) {
#       mResults.add(computer);
#       synchronized (this.mLock) {
#           if (this.observer != null) {
#               this.observer.computerFound(computer);
#           }
#       }
#   }

EDGES['E_rep08_046'] = {
    'src': 'SubnetScanner.run',
    'dst': 'SubnetScanner.onFound(ComputerParcelable)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'run calls onFound when computer discovered via IP scan',
    'evidence': 'SRC utils/SubnetScanner.java:116'
}

EDGES['E_rep08_047'] = {
    'src': 'SubnetScanner.tryWithBroadcast',
    'dst': 'SubnetScanner.onFound(ComputerParcelable)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'tryWithBroadcast calls onFound when computer discovered via SMB broadcast',
    'evidence': 'SRC utils/SubnetScanner.java:172'
}

# ============================================================================
# SubnetScanner.run
# ============================================================================
# REACHABLE: Called by Thread.start() when scanner thread is started
# Evidence: SRC utils/SubnetScanner.java:84-135
#   public void run() {

EDGES['E_rep08_048'] = {
    'src': 'Thread.start',
    'dst': 'SubnetScanner.run()',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp08',
    'text': 'Thread framework calls run when scanner thread started',
    'evidence': 'SRC utils/SubnetScanner.java:84 (SubnetScanner extends Thread)'
}

EDGES['E_rep08_049'] = {
    'src': 'SubnetScanner.run()',
    'dst': 'SubnetScanner.tryWithBroadcast()',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'run calls tryWithBroadcast to discover via SMB broadcast',
    'evidence': 'SRC utils/SubnetScanner.java:87'
}

# ============================================================================
# SubnetScanner.setObserver
# ============================================================================
# REACHABLE: Called by SmbSearchDialog to receive scan notifications
# Evidence: SRC utils/SubnetScanner.java:191-194
#   public void setObserver(ScanObserver scanObserver) {
#       synchronized (this.mLock) { this.observer = scanObserver; }
#   }

EDGES['E_rep08_050'] = {
    'src': 'SmbSearchDialog.startScan',
    'dst': 'SubnetScanner.setObserver(ScanObserver)',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'SmbSearchDialog sets observer to receive scan progress',
    'evidence': 'SRC utils/SubnetScanner.java:191 (called after creating scanner)'
}

# ============================================================================
# SubnetScanner.tryWithBroadcast
# ============================================================================
# REACHABLE: Called from run()
# Evidence: SRC utils/SubnetScanner.java:137-153
#   private void tryWithBroadcast() {
#       this.bdThread = new Thread() { ... };
#       this.bdThread.start();
#   }

EDGES['E_rep08_051'] = {
    'src': 'SubnetScanner.tryWithBroadcast()',
    'dst': 'Thread.start',
    'kind': 'CALL',
    'origin': 'repair_rp08',
    'text': 'tryWithBroadcast starts anonymous Thread for SMB broadcast discovery',
    'evidence': 'SRC utils/SubnetScanner.java:153'
}
