# Repair Batch 10 Summary

STATUS: START 20:52
STATUS: DONE 20:55

## Methods Analyzed: 37

### REACHABLE: 36 methods

| Method | Evidence |
|--------|----------|
| MainActivityHelper$4.exists(HybridFile) | Called by Operations.rename via ErrorCallBack interface; SRC utils/MainActivityHelper.java:304-310 |
| MainActivityHelper$4.invalidName(HybridFile) | Called by Operations.rename via ErrorCallBack interface; SRC utils/MainActivityHelper.java:356-362 |
| MainActivityHelper$4.lambda$done$2(HybridFile,boolean) | Lambda posted to UI thread from done callback; SRC utils/MainActivityHelper.java:329-351 |
| MainActivityHelper$4.lambda$exists$0(HybridFile) | Lambda posted to UI thread from exists callback; SRC utils/MainActivityHelper.java:305-308 |
| MainActivityHelper$4.lambda$invalidName$3(HybridFile) | Lambda posted to UI thread from invalidName callback; SRC utils/MainActivityHelper.java:357-360 |
| MainActivityHelper$4.lambda$launchSAF$1(HybridFile,HybridFile) | Lambda posted to UI thread from launchSAF callback; SRC utils/MainActivityHelper.java:316-323 |
| MainActivityHelper$4.launchSAF(HybridFile,HybridFile) | Called by Operations.rename when SAF permission needed via ErrorCallBack interface; SRC utils/MainActivityHelper.java:316-323 |
| StreamSource.<init>(SmbFile,long) | Created by Streamer to serve SMB files over HTTP; SRC utils/SmbStreamer/StreamSource.java:23-30 |
| StreamSource.close() | Called by Streamer to close SMB input stream after serving; SRC utils/SmbStreamer/StreamSource.java:92-98 |
| StreamSource.getFile() | Called by Streamer to retrieve SmbFile for metadata; SRC utils/SmbStreamer/StreamSource.java:105-107 |
| StreamSource.getMimeType() | Called by Streamer for HTTP Content-Type header; SRC utils/SmbStreamer/StreamSource.java:99-101 |
| StreamSource.getName() | Called by Streamer for HTTP response headers; SRC utils/SmbStreamer/StreamSource.java:103-105 |
| StreamSource.open() | Called by Streamer to open SMB input stream before reading; SRC utils/SmbStreamer/StreamSource.java:64-72 |
| StreamSource.read() | Called by Streamer to read single byte from SMB stream; SRC utils/SmbStreamer/StreamSource.java:74-79 |
| StreamSource.read(byte[],int,int) | Called by Streamer to read buffer from SMB stream efficiently; SRC utils/SmbStreamer/StreamSource.java:81-85 |
| PrepareCopyTask$CopyNode.getConflictingFiles() | Called by onEndDialog to check for conflicts; SRC asynchronous/asynctasks/PrepareCopyTask.java:388-390 |
| PrepareCopyTask$CopyNode.getFilesToCopy() | Called by onEndDialog to get files for copy service; SRC asynchronous/asynctasks/PrepareCopyTask.java:384-386 |
| PrepareCopyTask$CopyNode.getPath() | Called by onEndDialog to determine destination directory; SRC asynchronous/asynctasks/PrepareCopyTask.java:380-382 |
| PrepareCopyTask$CopyNode.getUnvisitedChildNode(Set,CopyNode) | Called by goToNextNode for BFS traversal; SRC asynchronous/asynctasks/PrepareCopyTask.java:392-400 |
| PrepareCopyTask$CopyNode.goToNextNode() | Called by onEndDialog to process next directory in copy tree; SRC asynchronous/asynctasks/PrepareCopyTask.java:362-376 |
| PrepareCopyTask$CopyNode.hasStarted() | Called by onPostExecute to check if copy tree needs initialization; SRC asynchronous/asynctasks/PrepareCopyTask.java:378-380 |
| PrepareCopyTask$CopyNode.startCopy() | Called by onPostExecute to begin BFS traversal; SRC asynchronous/asynctasks/PrepareCopyTask.java:352-360 |
| MainFragment.addSearchResult(HybridFileParcelable,String) | Called by SearchWorkerFragment for each file found; SRC fragments/MainFragment.java:1611-1633 |
| MainFragment.addShortcut(LayoutElementParcelable) | Called from ActionMode callback for "Add shortcut" menu item; SRC fragments/MainFragment.java:1573-1608, called at line 749 |
| MainFragment.addTo(HybridFileParcelable) | Called by addSearchResult to convert HybridFile to LayoutElement; SRC fragments/MainFragment.java:1499-1549, called at line 1626 |
| MainFragment.goBackItemClick() | Called by onListItemClicked when back button clicked; SRC fragments/MainFragment.java:1359-1377, called at line 873 |
| MainFragment.hide(String) | Called from ActionMode callback for "Hide" menu item; SRC fragments/MainFragment.java:1551-1571, called at line 711 |
| MainFragment.onListItemClicked(boolean,int,LayoutElementParcelable,ImageView) | Called by RecyclerAdapter for item click events; SRC fragments/MainFragment.java:851-989 |
| MainFragment.onSearchCompleted(String) | Called by SearchWorkerFragment after search finishes; SRC fragments/MainFragment.java:1635-1648 |
| MainFragment$3.hideOption(int,Menu) | Called by onPrepareActionMode and onCreateActionMode to hide context menu items; SRC fragments/MainFragment.java:463-466 |
| MainFragment$3.initMenu(Menu) | Called by onCreateActionMode to setup menu icons; SRC fragments/MainFragment.java:472-479, called at line 494 |
| MainFragment$3.onActionItemClicked(ActionMode,MenuItem) | Android framework callback when ActionMode menu item selected; SRC fragments/MainFragment.java:633-754 |
| MainFragment$3.onCreateActionMode(ActionMode,Menu) | Android framework callback when ActionMode is created; SRC fragments/MainFragment.java:482-512 |
| MainFragment$3.onDestroyActionMode(ActionMode) | Android framework callback when ActionMode ends; SRC fragments/MainFragment.java:757-776 |
| MainFragment$3.onPrepareActionMode(ActionMode,Menu) | Android framework callback to update menu based on selection; SRC fragments/MainFragment.java:519-631 |
| MainFragment$3.showOption(int,Menu) | Called by onPrepareActionMode and onCreateActionMode to show context menu items; SRC fragments/MainFragment.java:468-471 |

### UNREACHABLE: 1 method

| Method | Reason |
|--------|--------|
| MainActivityHelper$4.launchSAF(HybridFile) | Empty callback method; Operations.rename uses launchSAF(HybridFile,HybridFile) overload instead; SRC utils/MainActivityHelper.java:312-314 (empty method body) |

### INCOMPLETE: 0 methods
