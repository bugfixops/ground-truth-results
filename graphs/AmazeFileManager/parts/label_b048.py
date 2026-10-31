# ---- Helper batch_048 label part (2024)

# MainFragment$1 - OnGlobalLayoutListener set in onActivityCreated
e('MainFragment.onActivityCreated', 'MainFragment$1.<init>', 'CALL', 'MainFragment.onActivityCreated creates listener at line 310',
  evidence='SRC MainFragment.java:310')
e('MainFragment$1.<init>', 'ViewTreeObserver.OnGlobalLayoutListener.<init>', 'CALL', 'Anonymous class constructor chains to interface',
  evidence='SRC MainFragment.java:310')
e('ViewTreeObserver.addOnGlobalLayoutListener', 'MainFragment$1.onGlobalLayout', 'FRAMEWORK', 'Framework invokes listener callback when layout changes',
  evidence='SRC MainFragment.java:310')

# MainFragment$2 - SpanSizeLookup set in setGridLayoutSpanSizeLookup
e('MainFragment.setGridLayoutSpanSizeLookup', 'MainFragment$2.<init>', 'CALL', 'setGridLayoutSpanSizeLookup creates lookup at line 341',
  evidence='SRC MainFragment.java:341')
e('MainFragment$2.<init>', 'GridLayoutManager.SpanSizeLookup.<init>', 'CALL', 'Anonymous class constructor chains to parent',
  evidence='SRC MainFragment.java:341')
e('GridLayoutManager.getSpanSize', 'MainFragment$2.getSpanSize', 'FRAMEWORK', 'GridLayoutManager queries span size for grid items',
  evidence='SRC MainFragment.java:341-351')

# MainFragment$3 - ActionMode.Callback field, used by RecyclerAdapter
e('RecyclerAdapter.onBindViewHolder', 'MainFragment$3.<init>', 'CALL', 'RecyclerAdapter accesses mActionModeCallback field which instantiates callback',
  evidence='SRC RecyclerAdapter.java:192, MainFragment.java:461')
e('MainFragment$3.<init>', 'ActionMode.Callback.<init>', 'CALL', 'Anonymous class constructor chains to interface',
  evidence='SRC MainFragment.java:461')
e('AppCompatActivity.startSupportActionMode', 'MainFragment$3.onCreateActionMode', 'FRAMEWORK', 'Framework calls onCreateActionMode when action mode starts',
  evidence='SRC RecyclerAdapter.java:192, MainFragment.java:475-504')
e('AppCompatActivity.startSupportActionMode', 'MainFragment$3.onPrepareActionMode', 'FRAMEWORK', 'Framework calls onPrepareActionMode to update menu',
  evidence='SRC MainFragment.java:510-635')
e('ActionMode.invalidate', 'MainFragment$3.onPrepareActionMode', 'FRAMEWORK', 'ActionMode.invalidate triggers onPrepareActionMode',
  evidence='SRC MainFragment.java:510-635')
e('MainFragment$3.onActionItemClicked', 'MainFragment$3.onDestroyActionMode', 'CALL', 'onActionItemClicked finishes mode which triggers onDestroyActionMode',
  evidence='SRC MainFragment.java:638-747, 748-759')
e('MainFragment$3.onCreateActionMode', 'MainFragment$3.initMenu', 'CALL', 'onCreateActionMode calls initMenu at line 480',
  evidence='SRC MainFragment.java:480')
e('MainFragment$3.onCreateActionMode', 'MainFragment$3.hideOption', 'CALL', 'onCreateActionMode calls hideOption multiple times',
  evidence='SRC MainFragment.java:481-483')
e('MainFragment$3.onCreateActionMode', 'MainFragment$3.showOption', 'CALL', 'onCreateActionMode calls showOption at line 485',
  evidence='SRC MainFragment.java:485')
e('MainFragment$3.onPrepareActionMode', 'MainFragment$3.hideOption', 'CALL', 'onPrepareActionMode calls hideOption multiple times',
  evidence='SRC MainFragment.java:521-635')
e('MainFragment$3.onPrepareActionMode', 'MainFragment$3.showOption', 'CALL', 'onPrepareActionMode calls showOption multiple times',
  evidence='SRC MainFragment.java:521-635')

# MainFragment$4 - BroadcastReceiver registered in onResume
e('MainFragment.onResume', 'MainFragment$4.<init>', 'CALL', 'onResume accesses receiver2 field which instantiates receiver',
  evidence='SRC MainFragment.java:1421, 776')
e('MainFragment$4.<init>', 'BroadcastReceiver.<init>', 'CALL', 'Anonymous class constructor chains to parent',
  evidence='SRC MainFragment.java:776')
e('ContextWrapper.sendBroadcast', 'MainFragment$4.onReceive', 'SYSTEM', 'System delivers broadcast with KEY_INTENT_LOAD_LIST action to receiver',
  evidence='SRC MainFragment.java:1421, 777-825')

# MainFragment$4$1 - MediaScannerConnectionClient created in MainFragment$4.onReceive
e('MainFragment$4.onReceive', 'MainFragment$4$1.<init>', 'CALL', 'onReceive creates MediaScannerConnectionClient at line 798',
  evidence='SRC MainFragment.java:798')
e('MainFragment$4$1.<init>', 'MediaScannerConnection.MediaScannerConnectionClient.<init>', 'CALL', 'Anonymous class constructor chains to interface',
  evidence='SRC MainFragment.java:798')
e('MediaScannerConnection.connect', 'MainFragment$4$1.onMediaScannerConnected', 'FRAMEWORK', 'MediaScannerConnection calls onMediaScannerConnected when connected',
  evidence='SRC MainFragment.java:798-804')
e('MediaScannerConnection.scanFile', 'MainFragment$4$1.onScanCompleted', 'FRAMEWORK', 'MediaScannerConnection calls onScanCompleted after scan',
  evidence='SRC MainFragment.java:805-808')

# MainFragment$5 - BroadcastReceiver registered in onResume  
e('MainFragment.onResume', 'MainFragment$5.<init>', 'CALL', 'onResume accesses decryptReceiver field which instantiates receiver',
  evidence='SRC MainFragment.java:1427, 828')
e('MainFragment$5.<init>', 'BroadcastReceiver.<init>', 'CALL', 'Anonymous class constructor chains to parent',
  evidence='SRC MainFragment.java:828')
e('ContextWrapper.sendBroadcast', 'MainFragment$5.onReceive', 'SYSTEM', 'System delivers broadcast with DECRYPT_BROADCAST action to receiver',
  evidence='SRC MainFragment.java:1427, 829-836')

# MainFragment$6 - AsyncTask created in onSearchCompleted
e('MainFragment.onSearchCompleted', 'MainFragment$6.<init>', 'CALL', 'onSearchCompleted creates AsyncTask at line 1640',
  evidence='SRC MainFragment.java:1640')
e('MainFragment$6.<init>', 'AsyncTask.<init>', 'CALL', 'Anonymous class constructor chains to parent AsyncTask',
  evidence='SRC MainFragment.java:1640')
e('AsyncTask.executeOnExecutor', 'MainFragment$6.doInBackground', 'ASYNC', 'executeOnExecutor called at line 1653 runs doInBackground on thread pool',
  evidence='SRC MainFragment.java:1653, 1641-1645')
e('AsyncTask.executeOnExecutor', 'MainFragment$6.onPostExecute', 'ASYNC', 'AsyncTask framework calls onPostExecute after doInBackground completes',
  evidence='SRC MainFragment.java:1653, 1646-1651')

# MainFragment$7 - Thread created in launchSMB
e('MainFragment.launchSMB', 'MainFragment$7.<init>', 'CALL', 'launchSMB creates Thread at line 1658',
  evidence='SRC MainFragment.java:1658')
e('MainFragment$7.<init>', 'Thread.<init>', 'CALL', 'Anonymous class constructor chains to Thread',
  evidence='SRC MainFragment.java:1658')
e('Thread.start', 'MainFragment$7.run', 'ASYNC', 'Thread.start implicitly called after creation, invokes run method',
  evidence='SRC MainFragment.java:1658-1690')
e('Activity.runOnUiThread', 'MainFragment$7.lambda$run$0', 'ASYNC', 'run method calls runOnUiThread with lambda at line 1671',
  evidence='SRC MainFragment.java:1671')

# MapEntry - data holder created in SearchTextTask
e('SearchTextTask.doInBackground', 'MapEntry.<init>', 'CALL', 'SearchTextTask creates MapEntry instances at line 67',
  evidence='SRC SearchTextTask.java:67')

# MediaStoreHack - utility class methods
e('MainFragment.onListItemClicked', 'MediaStoreHack.getUriFromFile', 'CALL', 'MainFragment calls getUriFromFile at line 983',
  evidence='SRC MainFragment.java:983')
e('GenericCopyUtil.doCopy', 'MediaStoreHack.getInputStream', 'CALL', 'GenericCopyUtil calls getInputStream at line 173',
  evidence='SRC GenericCopyUtil.java:173')
e('GenericCopyUtil.doCopy', 'MediaStoreHack.getOutputStream', 'CALL', 'GenericCopyUtil calls getOutputStream at line 273',
  evidence='SRC GenericCopyUtil.java:273')
e('FileUtil.getDocumentFile', 'MediaStoreHack.getUriFromFile', 'CALL', 'FileUtil.getDocumentFile calls getUriFromFile at line 122',
  evidence='SRC FileUtil.java:122')
e('FileUtil.getOutputStream', 'MediaStoreHack.getOutputStream', 'CALL', 'FileUtil.getOutputStream calls MediaStoreHack.getOutputStream at line 184',
  evidence='SRC FileUtil.java:184')
e('FileUtil.scanFile', 'MediaStoreHack.getUriFromFile', 'CALL', 'FileUtil.scanFile calls getUriFromFile at line 392',
  evidence='SRC FileUtil.java:392')
e('FileUtil.mkdir', 'MediaStoreHack.mkdir', 'CALL', 'FileUtil.mkdir calls MediaStoreHack.mkdir at line 511',
  evidence='SRC FileUtil.java:511')
e('FileUtil.mkfile', 'MediaStoreHack.mkfile', 'CALL', 'FileUtil.mkfile calls MediaStoreHack.mkfile at line 581',
  evidence='SRC FileUtil.java:581')
e('MediaStoreHack.mkdir', 'MediaStoreHack.getTemporaryAlbumId', 'CALL', 'mkdir calls getTemporaryAlbumId at line 237',
  evidence='SRC MediaStoreHack.java:237')
e('MediaStoreHack.mkdir', 'MediaStoreHack.delete', 'CALL', 'mkdir calls delete at line 253',
  evidence='SRC MediaStoreHack.java:253')
e('MediaStoreHack.getTemporaryAlbumId', 'MediaStoreHack.installTemporaryTrack', 'CALL', 'getTemporaryAlbumId calls installTemporaryTrack at line 141',
  evidence='SRC MediaStoreHack.java:141')
e('MediaStoreHack.installTemporaryTrack', 'MediaStoreHack.getExternalFilesDir', 'CALL', 'installTemporaryTrack calls getExternalFilesDir at line 208',
  evidence='SRC MediaStoreHack.java:208')

# UNREACHABLE methods from this batch
UNREACHABLE_BATCH_048 = {
    'MediaStoreHack.<clinit>': ('framework_never_calls', 'No static initializer block in source, class has no static initialization code', 'SRC MediaStoreHack.java:1-280 shows no static block', 'SOURCE'),
    'MediaStoreHack.<init>': ('no_trigger_in_app', 'All MediaStoreHack methods are static, no constructor calls in app', 'SRC MediaStoreHack.java:1-280 shows only static methods; grep -rn "new MediaStoreHack" returns no results', 'SOURCE'),
}
