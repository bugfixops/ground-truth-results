# Repair Batch 08 Summary

STATUS: START 20:36
STATUS: DONE 20:38

## Methods Analyzed: 36

### REACHABLE: 27 methods

| Method | Evidence |
|--------|----------|
| MainActivity.addConnection(boolean,String,String,String,String,String) | Called by SmbConnectDialog.lambda$onCreateView$4; SRC activities/MainActivity.java:1679-1707, ui/dialogs/SmbConnectDialog.java:278 |
| MainActivity.deleteConnection(String,String) | Called by SmbConnectDialog.lambda$onCreateView$5; SRC activities/MainActivity.java:1714-1725, ui/dialogs/SmbConnectDialog.java:284 |
| MainActivity.lambda$addConnection$9 | Called via AppConfig.runInBackground from addConnection; SRC activities/MainActivity.java:1697-1699 |
| MainActivity.lambda$deleteConnection$10 | Called via AppConfig.runInBackground from deleteConnection; SRC activities/MainActivity.java:1717-1720 |
| MainActivity.onCancelled() | Called by SearchWorkerFragment.executeSearch; SRC activities/MainActivity.java:1788-1791 (implements SearchAsyncHelper.HelperCallbacks) |
| MainActivity.onPostExecute(String) | Called by SearchWorkerFragment.executeSearch; SRC activities/MainActivity.java:1777-1781 |
| MainActivity.onPreExecute(String) | Called by SearchWorkerFragment.executeSearch; SRC activities/MainActivity.java:1771-1775 |
| MainActivity.onProgressUpdate(HybridFileParcelable,String) | Called by SearchWorkerFragment.executeSearch; SRC activities/MainActivity.java:1783-1786 |
| MainActivity.setPagingEnabled(boolean) | Called by MainFragment.onListItemClicked; SRC activities/MainActivity.java:1271-1273, fragments/MainFragment.java:488,765 |
| PrepareCopyTask.doNotReplaceFiles(String,ArrayList,ArrayList) | Called by onEndDialog and lambda$showDialog$1; SRC asynchronous/asynctasks/PrepareCopyTask.java:241-253 |
| PrepareCopyTask.lambda$checkConflicts$0(ArrayList,ArrayList,HybridFileParcelable) | Called by HybridFile.forEachChildrenFile; SRC asynchronous/asynctasks/PrepareCopyTask.java:142-148 |
| PrepareCopyTask.lambda$showDialog$1(CheckBox,String,ArrayList,ArrayList,MaterialDialog,DialogAction) | Called by MaterialDialog framework on Skip button; SRC asynchronous/asynctasks/PrepareCopyTask.java:200-204 |
| PrepareCopyTask.lambda$showDialog$2(CheckBox,String,ArrayList,ArrayList,MaterialDialog,DialogAction) | Called by MaterialDialog framework on Overwrite button; SRC asynchronous/asynctasks/PrepareCopyTask.java:205-209 |
| PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList) | Called by onPostExecute and recursively; SRC asynchronous/asynctasks/PrepareCopyTask.java:214-243 |
| PrepareCopyTask.onPostExecute(CopyNode) | Called by AsyncTask framework; SRC asynchronous/asynctasks/PrepareCopyTask.java:153-176 |
| PrepareCopyTask.onPreExecute() | Called by AsyncTask framework; SRC asynchronous/asynctasks/PrepareCopyTask.java:86-89 |
| PrepareCopyTask.replaceFiles(String,ArrayList,ArrayList) | Called by onEndDialog and lambda$showDialog$2; SRC asynchronous/asynctasks/PrepareCopyTask.java:255-263 |
| PrepareCopyTask.showDialog(String,ArrayList,ArrayList) | Called by onEndDialog; SRC asynchronous/asynctasks/PrepareCopyTask.java:179-213 |
| SubnetScanner.<clinit>() | Called by JVM when class loaded; SRC utils/SubnetScanner.java:65-67 |
| SubnetScanner.<init>(Context) | Called by SmbSearchDialog.startScan; SRC utils/SubnetScanner.java:77-82 |
| SubnetScanner.configure() | Called by <clinit>; SRC utils/SubnetScanner.java:69-74 |
| SubnetScanner.getResults() | Called by SmbSearchDialog.onScanComplete; SRC utils/SubnetScanner.java:202-204 |
| SubnetScanner.interrupt() | Called by SmbSearchDialog.onCancel; SRC utils/SubnetScanner.java:196-201 |
| SubnetScanner.onFound(ComputerParcelable) | Called by run() and tryWithBroadcast; SRC utils/SubnetScanner.java:155-162 |
| SubnetScanner.run() | Called by Thread.start framework; SRC utils/SubnetScanner.java:84-135 |
| SubnetScanner.setObserver(ScanObserver) | Called by SmbSearchDialog.startScan; SRC utils/SubnetScanner.java:191-194 |
| SubnetScanner.tryWithBroadcast() | Called by run(); SRC utils/SubnetScanner.java:137-153 |

### UNREACHABLE: 9 methods

| Method | Reason |
|--------|--------|
| ScrimInsetsRelativeLayout.<init>(Context) | View class is never instantiated; GREP: grep -r "new ScrimInsetsRelativeLayout" shows 0; grep -r "ScrimInsetsRelativeLayout" res/layout/ shows 0; SRC ui/views/ScrimInsetsRelativeLayout.java:41 |
| ScrimInsetsRelativeLayout.<init>(Context,AttributeSet) | No XML layouts reference this view; GREP: grep -r "ScrimInsetsRelativeLayout" res/layout/ shows 0; SRC ui/views/ScrimInsetsRelativeLayout.java:45 |
| ScrimInsetsRelativeLayout.<init>(Context,AttributeSet,int) | No XML layouts reference this view; GREP: grep -r "ScrimInsetsRelativeLayout" res/layout/ shows 0; SRC ui/views/ScrimInsetsRelativeLayout.java:50 |
| ScrimInsetsRelativeLayout.draw(Canvas) | View is never instantiated, so draw method never called; SRC ui/views/ScrimInsetsRelativeLayout.java:75 |
| ScrimInsetsRelativeLayout.fitSystemWindows(Rect) | View is never instantiated; SRC ui/views/ScrimInsetsRelativeLayout.java:65 |
| ScrimInsetsRelativeLayout.init(Context,AttributeSet,int) | View constructors are unreachable; SRC ui/views/ScrimInsetsRelativeLayout.java:55 |
| ScrimInsetsRelativeLayout.onAttachedToWindow() | View is never instantiated; SRC ui/views/ScrimInsetsRelativeLayout.java:111 |
| ScrimInsetsRelativeLayout.onDetachedFromWindow() | View is never instantiated; SRC ui/views/ScrimInsetsRelativeLayout.java:119 |
| ScrimInsetsRelativeLayout.setOnInsetsCallback(OnInsetsCallback) | View is never instantiated and method never called; GREP: grep -r "setOnInsetsCallback" shows 1 result (definition only); SRC ui/views/ScrimInsetsRelativeLayout.java:133 |

### INCOMPLETE: 0 methods
