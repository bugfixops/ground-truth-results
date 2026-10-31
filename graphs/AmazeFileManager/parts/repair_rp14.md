STATUS: START 21:05

SmbSearchDialog$1.<init> | REACHABLE | CALL | Anonymous ScanObserver instance created in onCreateDialog | SRC ui/dialogs/SmbSearchDialog.java:81
SmbSearchDialog$1.computerFound | REACHABLE | FRAMEWORK | SubnetScanner callback when SMB server discovered | INFERRED SubnetScanner notifies observer; SRC ui/dialogs/SmbSearchDialog.java:82-90
SmbSearchDialog$1.lambda$computerFound$0 | REACHABLE | CALL | Lambda posted to UI thread from computerFound | SRC ui/dialogs/SmbSearchDialog.java:84-89
SmbSearchDialog$1.lambda$searchFinished$1 | REACHABLE | CALL | Lambda posted to UI thread from searchFinished | SRC ui/dialogs/SmbSearchDialog.java:93-105
SmbSearchDialog$1.searchFinished | REACHABLE | FRAMEWORK | SubnetScanner callback when scan completes | INFERRED SubnetScanner notifies observer; SRC ui/dialogs/SmbSearchDialog.java:91-106
FastScroller.<init>(Context,AttributeSet) | REACHABLE (already in graph_def.py) | - | Already labeled | -
FastScroller.<init>(Context,AttributeSet,int) | REACHABLE (already in graph_def.py) | - | Already labeled | -
FastScroller.getRelativeTouchPosition | REACHABLE (already in graph_def.py) | - | Already labeled | -
FastScroller.onTouchEvent | REACHABLE (already in graph_def.py) | - | Already labeled | -
FastScroller.setRecyclerViewPosition | REACHABLE (already in graph_def.py) | - | Already labeled | -
ThemedImageButton.<init>(Context) | REACHABLE | LIFECYCLE | Called from two-arg constructor chain | SRC ui/views/ThemedImageButton.java:13-15
ThemedImageButton.<init>(Context,AttributeSet) | REACHABLE | FRAMEWORK | Inflated from XML layout | SRC res/layout/namepathswitch_preference.xml; INFERRED LayoutInflater
ThemedImageButton.<init>(Context,AttributeSet,int) | UNREACHABLE | framework_never_calls | Three-arg constructor not used; XML uses two-arg | SRC ui/views/ThemedImageButton.java:19-22; no three-arg calls
ThemedImageButton.getAccessibilityClassName | REACHABLE | FRAMEWORK | Framework accessibility system callback | SRC ui/views/ThemedImageButton.java:29-32; INFERRED accessibility
ThemedImageButton.onSetAlpha | REACHABLE | FRAMEWORK | Framework View animation system callback | SRC ui/views/ThemedImageButton.java:24-27; INFERRED animation
Utils.<init> | REACHABLE (already in graph_def.py) | - | Already labeled | -
Utils.dpToPx | REACHABLE | CALL | Called from MainFragment for dimension conversion | SRC fragments/MainFragment.java:315
Utils.getViewRawY | REACHABLE | CALL | Called from FastScroller for touch calculation | SRC ui/views/FastScroller.java:147
Utils.isDeviceInLandScape | UNREACHABLE | no_trigger_in_app | Only usage is commented out | SRC utils/Utils.java:161-163; SRC ui/views/drawer/Drawer.java:161 commented
Utils.setTint | REACHABLE | CALL | Called from SmbConnectDialog and PrepareCopyTask | SRC ui/dialogs/SmbConnectDialog.java:161; SRC asynchronous/asynctasks/PrepareCopyTask.java:193
CloudIconDataFetcher.<init> | REACHABLE (already in graph_def.py) | - | Already labeled | -
CloudIconDataFetcher.cleanup | REACHABLE (already in graph_def.py) | - | Already labeled | -
CloudIconDataFetcher.getDataClass | REACHABLE (already in graph_def.py) | - | Already labeled | -
CloudIconDataFetcher.getDataSource | REACHABLE (already in graph_def.py) | - | Already labeled | -
CloudIconDataFetcher.loadData | REACHABLE (already in graph_def.py) | - | Already labeled | -
AboutActivity.<init> | INCOMPLETE | - | source only in flavor folder(s); DATASET.txt names no flavor (section 2.3) | src/fdroid and src/play only
AboutActivity.onClick | INCOMPLETE | - | source only in flavor folder(s); DATASET.txt names no flavor (section 2.3) | src/fdroid and src/play only
AboutActivity.onOptionsItemSelected | INCOMPLETE | - | source only in flavor folder(s); DATASET.txt names no flavor (section 2.3) | src/fdroid and src/play only
AboutActivity.openURL | INCOMPLETE | - | source only in flavor folder(s); DATASET.txt names no flavor (section 2.3) | src/fdroid and src/play only
ColorAdapter.<init> | REACHABLE (already in graph_def.py) | - | Already labeled | -
ColorAdapter.getColorResAt | REACHABLE (already in graph_def.py) | - | Already labeled | -
ColorAdapter.getView | REACHABLE (already in graph_def.py) | - | Already labeled | -
ColorAdapter.onItemClick | REACHABLE (already in graph_def.py) | - | Already labeled | -
SearchTextTask.<init> | REACHABLE (already in graph_def.py) | - | Already labeled | -
SearchTextTask.doInBackground | REACHABLE (already in graph_def.py) | - | Already labeled | -
SearchTextTask.onPostExecute | REACHABLE (already in graph_def.py) | - | Already labeled | -
SearchTextTask.onPreExecute | REACHABLE (already in graph_def.py) | - | Already labeled | -

STATUS: DONE 21:08
STATUS: INCOMPLETE AboutActivity.<init> AboutActivity.onClick AboutActivity.onOptionsItemSelected AboutActivity.openURL
