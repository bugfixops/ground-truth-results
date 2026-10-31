# Repair batch 10: 37 methods
# Schema-2 edge entries for AmazeFileManager

EDGES = {}

# ============================================================================
# MainActivityHelper$4 is an anonymous inner class implementing Operations.ErrorCallBack
# in the MainActivityHelper.rename() method
# SRC utils/MainActivityHelper.java:270-325
# ============================================================================

# ============================================================================
# MainActivityHelper$4.exists
# ============================================================================
# REACHABLE: Callback from Operations.rename when target file already exists
# Evidence: SRC utils/MainActivityHelper.java:304-310
#   @Override
#   public void exists(HybridFile file) {
#       context.runOnUiThread(() -> {
#           if (toast != null) toast.cancel();
#           Toast.makeText(mainActivity, context.getString(R.string.fileexist), Toast.LENGTH_SHORT).show();
#       });
#   }

EDGES['E_rep10_001'] = {
    'src': 'Operations.rename',
    'dst': 'MainActivityHelper$4.exists(HybridFile)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Operations.rename calls exists callback when target file already exists',
    'evidence': 'SRC utils/MainActivityHelper.java:304 (ErrorCallBack interface)'
}

# ============================================================================
# MainActivityHelper$4.invalidName
# ============================================================================
# REACHABLE: Callback from Operations.rename when filename is invalid
# Evidence: SRC utils/MainActivityHelper.java:356-362
#   @Override
#   public void invalidName(final HybridFile file) {
#       context.runOnUiThread(() -> {
#           if (toast != null) toast.cancel();
#           Toast.makeText(context, context.getString(R.string.invalid_name) + ": " + file.getName(), Toast.LENGTH_LONG).show();
#       });
#   }

EDGES['E_rep10_002'] = {
    'src': 'Operations.rename',
    'dst': 'MainActivityHelper$4.invalidName(HybridFile)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Operations.rename calls invalidName callback when filename validation fails',
    'evidence': 'SRC utils/MainActivityHelper.java:356 (ErrorCallBack interface)'
}

# ============================================================================
# MainActivityHelper$4.lambda$done$2
# ============================================================================
# REACHABLE: Lambda invoked on UI thread from done callback
# Evidence: SRC utils/MainActivityHelper.java:329-351
#   @Override
#   public void done(final HybridFile hFile, final boolean b) {
#       context.runOnUiThread(() -> { ... });
#   }

EDGES['E_rep10_003'] = {
    'src': 'MainActivityHelper$4.done(HybridFile,boolean)',
    'dst': 'MainActivityHelper$4.lambda$done$2(HybridFile,boolean)',
    'kind': 'ASYNC',
    'origin': 'repair_rp10',
    'text': 'done callback posts lambda to UI thread',
    'evidence': 'SRC utils/MainActivityHelper.java:329'
}

EDGES['E_rep10_004'] = {
    'src': 'MainActivityHelper$4.lambda$done$2(HybridFile,boolean)',
    'dst': 'MainActivity.sendBroadcast',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Lambda sends broadcast to reload file list after successful rename',
    'evidence': 'SRC utils/MainActivityHelper.java:333-334'
}

EDGES['E_rep10_005'] = {
    'src': 'MainActivityHelper$4.lambda$done$2(HybridFile,boolean)',
    'dst': 'CryptHandler.<init>(Context)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Lambda creates CryptHandler to update encrypted file entry',
    'evidence': 'SRC utils/MainActivityHelper.java:338'
}

# ============================================================================
# MainActivityHelper$4.lambda$exists$0
# ============================================================================
# REACHABLE: Lambda invoked on UI thread from exists callback
# Evidence: SRC utils/MainActivityHelper.java:305-308
#   context.runOnUiThread(() -> {
#       if (toast != null) toast.cancel();
#       Toast.makeText(mainActivity, context.getString(R.string.fileexist), Toast.LENGTH_SHORT).show();
#   });

EDGES['E_rep10_006'] = {
    'src': 'MainActivityHelper$4.exists(HybridFile)',
    'dst': 'MainActivityHelper$4.lambda$exists$0(HybridFile)',
    'kind': 'ASYNC',
    'origin': 'repair_rp10',
    'text': 'exists callback posts lambda to UI thread to show toast',
    'evidence': 'SRC utils/MainActivityHelper.java:305'
}

EDGES['E_rep10_007'] = {
    'src': 'MainActivityHelper$4.lambda$exists$0(HybridFile)',
    'dst': 'Toast.makeText',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Lambda displays "file exists" toast message',
    'evidence': 'SRC utils/MainActivityHelper.java:307'
}

# ============================================================================
# MainActivityHelper$4.lambda$invalidName$3
# ============================================================================
# REACHABLE: Lambda invoked on UI thread from invalidName callback
# Evidence: SRC utils/MainActivityHelper.java:357-360
#   context.runOnUiThread(() -> {
#       if (toast != null) toast.cancel();
#       Toast.makeText(context, context.getString(R.string.invalid_name) + ": " + file.getName(), Toast.LENGTH_LONG).show();
#   });

EDGES['E_rep10_008'] = {
    'src': 'MainActivityHelper$4.invalidName(HybridFile)',
    'dst': 'MainActivityHelper$4.lambda$invalidName$3(HybridFile)',
    'kind': 'ASYNC',
    'origin': 'repair_rp10',
    'text': 'invalidName callback posts lambda to UI thread to show toast',
    'evidence': 'SRC utils/MainActivityHelper.java:357'
}

EDGES['E_rep10_009'] = {
    'src': 'MainActivityHelper$4.lambda$invalidName$3(HybridFile)',
    'dst': 'Toast.makeText',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Lambda displays "invalid name" toast message',
    'evidence': 'SRC utils/MainActivityHelper.java:359'
}

# ============================================================================
# MainActivityHelper$4.lambda$launchSAF$1
# ============================================================================
# REACHABLE: Lambda invoked on UI thread from launchSAF callback
# Evidence: SRC utils/MainActivityHelper.java:316-323
#   @Override
#   public void launchSAF(final HybridFile file, final HybridFile file1) {
#       context.runOnUiThread(() -> {
#           if (toast != null) toast.cancel();
#           mainActivity.oppathe = file.getPath();
#           mainActivity.oppathe1 = file1.getPath();
#           mainActivity.operation = DataUtils.RENAME;
#           guideDialogForLEXA(mainActivity.oppathe1);
#       });
#   }

EDGES['E_rep10_010'] = {
    'src': 'MainActivityHelper$4.launchSAF(HybridFile,HybridFile)',
    'dst': 'MainActivityHelper$4.lambda$launchSAF$1(HybridFile,HybridFile)',
    'kind': 'ASYNC',
    'origin': 'repair_rp10',
    'text': 'launchSAF callback posts lambda to UI thread',
    'evidence': 'SRC utils/MainActivityHelper.java:316'
}

EDGES['E_rep10_011'] = {
    'src': 'MainActivityHelper$4.lambda$launchSAF$1(HybridFile,HybridFile)',
    'dst': 'MainActivityHelper.guideDialogForLEXA(String)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Lambda calls guideDialogForLEXA to request SD card access',
    'evidence': 'SRC utils/MainActivityHelper.java:322'
}

# ============================================================================
# MainActivityHelper$4.launchSAF(HybridFile)
# ============================================================================
# REACHABLE: Callback from Operations.rename when SAF needed (single file)
# Evidence: SRC utils/MainActivityHelper.java:312-314
#   @Override
#   public void launchSAF(HybridFile file) {
#   }

UNREACHABLE = {}

UNREACHABLE['MainActivityHelper$4.launchSAF(HybridFile)'] = {
    'reason': 'Empty callback method; Operations.rename uses launchSAF(HybridFile,HybridFile) overload instead',
    'evidence': 'SRC utils/MainActivityHelper.java:312-314 (empty method body)'
}

# ============================================================================
# MainActivityHelper$4.launchSAF(HybridFile,HybridFile)
# ============================================================================
# REACHABLE: Callback from Operations.rename when SAF permission needed
# Evidence: SRC utils/MainActivityHelper.java:316-323

EDGES['E_rep10_012'] = {
    'src': 'Operations.rename',
    'dst': 'MainActivityHelper$4.launchSAF(HybridFile,HybridFile)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Operations.rename calls launchSAF when Storage Access Framework permission needed',
    'evidence': 'SRC utils/MainActivityHelper.java:316 (ErrorCallBack interface)'
}

# ============================================================================
# StreamSource.<init>
# ============================================================================
# REACHABLE: Created by Streamer to serve SMB files over HTTP
# Evidence: SRC utils/SmbStreamer/StreamSource.java:23-30
#   public StreamSource(SmbFile file,long l) {
#       super(l);
#       fp = 0;
#       mime = MimeTypeMap.getFileExtensionFromUrl(file.getName());
#       name = file.getName();
#       this.file = file;
#   }

EDGES['E_rep10_013'] = {
    'src': 'Streamer.serve',
    'dst': 'StreamSource.<init>(SmbFile,long)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Streamer creates StreamSource to serve SMB file content',
    'evidence': 'SRC utils/SmbStreamer/StreamSource.java:23 (instantiated for HTTP streaming)'
}

# ============================================================================
# StreamSource.close
# ============================================================================
# REACHABLE: Called to close SMB input stream after serving file
# Evidence: SRC utils/SmbStreamer/StreamSource.java:92-98
#   @Override
#   public void close() {
#       try {
#           input.close();
#       } catch (IOException e) {
#           e.printStackTrace();
#       }
#   }

EDGES['E_rep10_014'] = {
    'src': 'Streamer.serve',
    'dst': 'StreamSource.close()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Streamer calls close to cleanup SMB stream after serving',
    'evidence': 'SRC utils/SmbStreamer/StreamSource.java:92 (RandomAccessStream cleanup)'
}

# ============================================================================
# StreamSource.getFile
# ============================================================================
# REACHABLE: Returns underlying SmbFile for stream operations
# Evidence: SRC utils/SmbStreamer/StreamSource.java:105-107
#   public SmbFile getFile(){
#       return file;
#   }

EDGES['E_rep10_015'] = {
    'src': 'Streamer.serve',
    'dst': 'StreamSource.getFile()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Streamer retrieves SmbFile for metadata or operations',
    'evidence': 'SRC utils/SmbStreamer/StreamSource.java:105'
}

# ============================================================================
# StreamSource.getMimeType
# ============================================================================
# REACHABLE: Returns MIME type for HTTP Content-Type header
# Evidence: SRC utils/SmbStreamer/StreamSource.java:99-101
#   public String getMimeType(){
#       return mime;
#   }

EDGES['E_rep10_016'] = {
    'src': 'Streamer.serve',
    'dst': 'StreamSource.getMimeType()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Streamer calls getMimeType for HTTP response Content-Type header',
    'evidence': 'SRC utils/SmbStreamer/StreamSource.java:99'
}

# ============================================================================
# StreamSource.getName
# ============================================================================
# REACHABLE: Returns file name for HTTP headers
# Evidence: SRC utils/SmbStreamer/StreamSource.java:103-105
#   public String getName(){
#       return name;
#   }

EDGES['E_rep10_017'] = {
    'src': 'Streamer.serve',
    'dst': 'StreamSource.getName()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Streamer calls getName for HTTP response headers',
    'evidence': 'SRC utils/SmbStreamer/StreamSource.java:103'
}

# ============================================================================
# StreamSource.open
# ============================================================================
# REACHABLE: Opens SMB input stream before reading file data
# Evidence: SRC utils/SmbStreamer/StreamSource.java:64-72
#   public void open() throws IOException {
#       try {
#           input = file.getInputStream();
#           if(fp>0)
#               input.skip(fp);
#       } catch (Exception e) {
#           throw new IOException(e);
#       }
#   }

EDGES['E_rep10_018'] = {
    'src': 'Streamer.serve',
    'dst': 'StreamSource.open()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Streamer calls open to initialize SMB input stream before reading',
    'evidence': 'SRC utils/SmbStreamer/StreamSource.java:64'
}

# ============================================================================
# StreamSource.read()
# ============================================================================
# REACHABLE: Reads single byte from SMB stream for HTTP serving
# Evidence: SRC utils/SmbStreamer/StreamSource.java:74-79
#   @Override
#   public int read() throws IOException {
#       int read = input.read();
#       if(read != -1) fp++;
#       return read;
#   }

EDGES['E_rep10_019'] = {
    'src': 'Streamer.serve',
    'dst': 'StreamSource.read()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Streamer calls read to fetch byte from SMB file for HTTP response',
    'evidence': 'SRC utils/SmbStreamer/StreamSource.java:74'
}

# ============================================================================
# StreamSource.read(byte[],int,int)
# ============================================================================
# REACHABLE: Reads buffer from SMB stream for HTTP serving
# Evidence: SRC utils/SmbStreamer/StreamSource.java:81-85
#   public int read(byte[] bytes, int start, int offs) throws IOException {
#       int read =  input.read(bytes, start, offs);
#       fp += read;
#       return read;
#   }

EDGES['E_rep10_020'] = {
    'src': 'Streamer.serve',
    'dst': 'StreamSource.read(byte[],int,int)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'Streamer calls read with buffer to efficiently stream SMB file data',
    'evidence': 'SRC utils/SmbStreamer/StreamSource.java:81'
}

# ============================================================================
# PrepareCopyTask$CopyNode.getConflictingFiles
# ============================================================================
# REACHABLE: Returns list of files conflicting with copy operation
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:388-390
#   ArrayList<HybridFileParcelable> getConflictingFiles() {
#       return conflictingFiles;
#   }

EDGES['E_rep10_021'] = {
    'src': 'PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)',
    'dst': 'PrepareCopyTask$CopyNode.getConflictingFiles()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onEndDialog calls getConflictingFiles to check if conflicts exist',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:388 (accessor for conflict resolution)'
}

# ============================================================================
# PrepareCopyTask$CopyNode.getFilesToCopy
# ============================================================================
# REACHABLE: Returns list of files to copy in this node
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:384-386
#   ArrayList<HybridFileParcelable> getFilesToCopy() {
#       return filesToCopy;
#   }

EDGES['E_rep10_022'] = {
    'src': 'PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)',
    'dst': 'PrepareCopyTask$CopyNode.getFilesToCopy()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onEndDialog calls getFilesToCopy to initiate copy service',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:384 (accessor for service intent)'
}

# ============================================================================
# PrepareCopyTask$CopyNode.getPath
# ============================================================================
# REACHABLE: Returns destination path for this copy node
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:380-382
#   String getPath() {
#       return path;
#   }

EDGES['E_rep10_023'] = {
    'src': 'PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)',
    'dst': 'PrepareCopyTask$CopyNode.getPath()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onEndDialog calls getPath to determine destination directory',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:380'
}

# ============================================================================
# PrepareCopyTask$CopyNode.getUnvisitedChildNode
# ============================================================================
# REACHABLE: BFS helper to find next unvisited child node
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:392-400
#   private CopyNode getUnvisitedChildNode(Set<CopyNode> visited, CopyNode node) {
#       for (CopyNode n : node.nextNodes) {
#           if (!visited.contains(n)) {
#               return n;
#           }
#       }
#       return null;
#   }

EDGES['E_rep10_024'] = {
    'src': 'PrepareCopyTask$CopyNode.goToNextNode()',
    'dst': 'PrepareCopyTask$CopyNode.getUnvisitedChildNode(Set,CopyNode)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'goToNextNode calls getUnvisitedChildNode to traverse copy tree',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:368'
}

# ============================================================================
# PrepareCopyTask$CopyNode.goToNextNode
# ============================================================================
# REACHABLE: BFS traversal to next node in copy tree
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:362-376
#   CopyNode goToNextNode() {
#       if (queue.isEmpty())
#           return null;
#       else {
#           CopyNode node = queue.element();
#           CopyNode child;
#           if ((child = getUnvisitedChildNode(visited, node)) != null) {
#               visited.add(child);
#               queue.add(child);
#               return child;
#           } else {
#               queue.remove();
#               return goToNextNode();
#           }
#       }
#   }

EDGES['E_rep10_025'] = {
    'src': 'PrepareCopyTask.onEndDialog(String,ArrayList,ArrayList)',
    'dst': 'PrepareCopyTask$CopyNode.goToNextNode()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onEndDialog calls goToNextNode to process next directory in copy tree',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:362 (BFS iteration)'
}

# ============================================================================
# PrepareCopyTask$CopyNode.hasStarted
# ============================================================================
# REACHABLE: Checks if BFS traversal has been initialized
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:378-380
#   boolean hasStarted() {
#       return queue != null;
#   }

EDGES['E_rep10_026'] = {
    'src': 'PrepareCopyTask.onPostExecute(CopyNode)',
    'dst': 'PrepareCopyTask$CopyNode.hasStarted()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onPostExecute calls hasStarted to check if copy tree needs initialization',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:378'
}

# ============================================================================
# PrepareCopyTask$CopyNode.startCopy
# ============================================================================
# REACHABLE: Initializes BFS traversal of copy tree
# Evidence: SRC asynchronous/asynctasks/PrepareCopyTask.java:352-360
#   CopyNode startCopy() {
#       queue = new LinkedList<>();
#       visited = new HashSet<>();
#       queue.add(this);
#       visited.add(this);
#       return this;
#   }

EDGES['E_rep10_027'] = {
    'src': 'PrepareCopyTask.onPostExecute(CopyNode)',
    'dst': 'PrepareCopyTask$CopyNode.startCopy()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onPostExecute calls startCopy to begin BFS traversal',
    'evidence': 'SRC asynchronous/asynctasks/PrepareCopyTask.java:352'
}

# ============================================================================
# MainFragment.addSearchResult
# ============================================================================
# REACHABLE: Called by SearchWorkerFragment to add search result to UI
# Evidence: SRC fragments/MainFragment.java:1611-1633
#   public void addSearchResult(HybridFileParcelable a, String query) {
#       if (listView != null) {
#           ...
#           SEARCH_ADAPTER_ELEMENTS.add(addTo(a));
#       }
#   }

EDGES['E_rep10_028'] = {
    'src': 'SearchWorkerFragment.addSearchResult',
    'dst': 'MainFragment.addSearchResult(HybridFileParcelable,String)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'SearchWorkerFragment calls addSearchResult for each file found',
    'evidence': 'SRC fragments/MainFragment.java:1611 (called via HelperCallbacks)'
}

EDGES['E_rep10_029'] = {
    'src': 'MainFragment.addSearchResult(HybridFileParcelable,String)',
    'dst': 'MainFragment.addTo(HybridFileParcelable)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'addSearchResult calls addTo to convert HybridFile to LayoutElement',
    'evidence': 'SRC fragments/MainFragment.java:1626'
}

# ============================================================================
# MainFragment.addShortcut
# ============================================================================
# REACHABLE: Called from ActionMode to create home screen shortcut
# Evidence: SRC fragments/MainFragment.java:1573-1608
#   private void addShortcut(LayoutElementParcelable path) {
#       //Adding shortcut for MainActivity on Home screen
#       Intent shortcutIntent = new Intent(getActivity().getApplicationContext(), MainActivity.class);
#       ...
#   }

EDGES['E_rep10_030'] = {
    'src': 'MainFragment$3.onActionItemClicked(ActionMode,MenuItem)',
    'dst': 'MainFragment.addShortcut(LayoutElementParcelable)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'ActionMode callback calls addShortcut when user selects "Add shortcut" menu item',
    'evidence': 'SRC fragments/MainFragment.java:749 (R.id.addshortcut case)'
}

EDGES['E_rep10_031'] = {
    'src': 'MainFragment.addShortcut(LayoutElementParcelable)',
    'dst': 'FileUtils.scanFile(File[],Context)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'addShortcut calls scanFile for media scanner',
    'evidence': 'SRC fragments/MainFragment.java:1607'
}

# ============================================================================
# MainFragment.addTo
# ============================================================================
# REACHABLE: Converts HybridFileParcelable to LayoutElementParcelable for search results
# Evidence: SRC fragments/MainFragment.java:1499-1549
#   private LayoutElementParcelable addTo(HybridFileParcelable mFile) {
#       File f = new File(mFile.getPath());
#       String size = "";
#       ...
#   }

EDGES['E_rep10_032'] = {
    'src': 'MainFragment.addTo(HybridFileParcelable)',
    'dst': 'DataUtils.addHiddenFile(String)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'addTo checks if file is hidden',
    'evidence': 'SRC fragments/MainFragment.java:1520-1522'
}

# ============================================================================
# MainFragment.goBackItemClick
# ============================================================================
# REACHABLE: Called when user clicks back button in UI
# Evidence: SRC fragments/MainFragment.java:1359-1377
#   public void goBackItemClick() {
#       if (openMode == OpenMode.CUSTOM) {
#           loadlist(home, false, OpenMode.FILE);
#       } else { ... }
#   }

EDGES['E_rep10_033'] = {
    'src': 'MainFragment.onListItemClicked(boolean,int,LayoutElementParcelable,ImageView)',
    'dst': 'MainFragment.goBackItemClick()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onListItemClicked calls goBackItemClick when back button clicked',
    'evidence': 'SRC fragments/MainFragment.java:873'
}

EDGES['E_rep10_034'] = {
    'src': 'MainFragment.goBackItemClick()',
    'dst': 'DataUtils.addHistoryFile(String)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'goBackItemClick adds path to navigation history',
    'evidence': 'SRC fragments/MainFragment.java:1363-1373'
}

EDGES['E_rep10_035'] = {
    'src': 'MainFragment.goBackItemClick()',
    'dst': 'MainFragment.loadlist(String,boolean,OpenMode)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'goBackItemClick calls loadlist to navigate to parent directory',
    'evidence': 'SRC fragments/MainFragment.java:1362,1366,1371,1375'
}

# ============================================================================
# MainFragment.hide
# ============================================================================
# REACHABLE: Called from ActionMode to hide selected files
# Evidence: SRC fragments/MainFragment.java:1551-1571
#   public void hide(String path) {
#       dataUtils.addHiddenFile(path);
#       ...
#   }

EDGES['E_rep10_036'] = {
    'src': 'MainFragment$3.onActionItemClicked(ActionMode,MenuItem)',
    'dst': 'MainFragment.hide(String)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'ActionMode callback calls hide when user selects "Hide" menu item',
    'evidence': 'SRC fragments/MainFragment.java:711 (R.id.hide case)'
}

EDGES['E_rep10_037'] = {
    'src': 'MainFragment.hide(String)',
    'dst': 'DataUtils.addHiddenFile(String)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'hide calls addHiddenFile to persist hidden status',
    'evidence': 'SRC fragments/MainFragment.java:1554'
}

# ============================================================================
# MainFragment.onListItemClicked
# ============================================================================
# REACHABLE: Called by RecyclerAdapter when user clicks file/folder
# Evidence: SRC fragments/MainFragment.java:851-989
#   public void onListItemClicked(boolean isBackButton, int position, LayoutElementParcelable e, ImageView imageView) {
#       if (results) { ... } else { ... }
#   }

EDGES['E_rep10_038'] = {
    'src': 'RecyclerAdapter.onItemClick(int,View)',
    'dst': 'MainFragment.onListItemClicked(boolean,int,LayoutElementParcelable,ImageView)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'RecyclerAdapter calls onListItemClicked for item click events',
    'evidence': 'SRC fragments/MainFragment.java:851'
}

EDGES['E_rep10_039'] = {
    'src': 'MainFragment.onListItemClicked(boolean,int,LayoutElementParcelable,ImageView)',
    'dst': 'MainActivity.setPagingEnabled(boolean)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onListItemClicked calls setPagingEnabled when entering selection mode',
    'evidence': 'SRC fragments/MainFragment.java:488'
}

EDGES['E_rep10_040'] = {
    'src': 'MainFragment.onListItemClicked(boolean,int,LayoutElementParcelable,ImageView)',
    'dst': 'FileUtils.openFile(File,MainActivity,SharedPreferences)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onListItemClicked calls openFile to open clicked file',
    'evidence': 'SRC fragments/MainFragment.java:930'
}

# ============================================================================
# MainFragment.onSearchCompleted
# ============================================================================
# REACHABLE: Called by SearchWorkerFragment when search finishes
# Evidence: SRC fragments/MainFragment.java:1635-1648
#   public void onSearchCompleted(final String query) {
#       if (!results) {
#           // no results were found
#           getActivity().runOnUiThread(() -> { ... });
#       }
#   }

EDGES['E_rep10_041'] = {
    'src': 'SearchWorkerFragment.executeSearch',
    'dst': 'MainFragment.onSearchCompleted(String)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'SearchWorkerFragment calls onSearchCompleted after search finishes',
    'evidence': 'SRC fragments/MainFragment.java:1635 (via HelperCallbacks)'
}

# ============================================================================
# MainFragment$3 is the ActionMode.Callback anonymous inner class
# SRC fragments/MainFragment.java:461-776
# ============================================================================

# ============================================================================
# MainFragment$3.hideOption
# ============================================================================
# REACHABLE: Called from onPrepareActionMode to hide menu items
# Evidence: SRC fragments/MainFragment.java:463-466
#   private void hideOption(int id, Menu menu) {
#       MenuItem item = menu.findItem(id);
#       item.setVisible(false);
#   }

EDGES['E_rep10_042'] = {
    'src': 'MainFragment$3.onPrepareActionMode(ActionMode,Menu)',
    'dst': 'MainFragment$3.hideOption(int,Menu)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onPrepareActionMode calls hideOption to hide context menu items',
    'evidence': 'SRC fragments/MainFragment.java:538,540,541,564 (and many others)'
}

EDGES['E_rep10_043'] = {
    'src': 'MainFragment$3.onCreateActionMode(ActionMode,Menu)',
    'dst': 'MainFragment$3.hideOption(int,Menu)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onCreateActionMode calls hideOption to hide initial menu items',
    'evidence': 'SRC fragments/MainFragment.java:495-497'
}

# ============================================================================
# MainFragment$3.initMenu
# ============================================================================
# REACHABLE: Called from onCreateActionMode to initialize menu
# Evidence: SRC fragments/MainFragment.java:472-479
#   void initMenu(Menu menu) {
#       /* commented out icon setup */
#   }

EDGES['E_rep10_044'] = {
    'src': 'MainFragment$3.onCreateActionMode(ActionMode,Menu)',
    'dst': 'MainFragment$3.initMenu(Menu)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onCreateActionMode calls initMenu to setup menu icons',
    'evidence': 'SRC fragments/MainFragment.java:494'
}

# ============================================================================
# MainFragment$3.onActionItemClicked
# ============================================================================
# REACHABLE: Framework callback when user selects ActionMode menu item
# Evidence: SRC fragments/MainFragment.java:633-754
#   public boolean onActionItemClicked(ActionMode mode, MenuItem item) {
#       computeScroll();
#       ArrayList<LayoutElementParcelable> checkedItems = adapter.getCheckedItems();
#       switch (item.getItemId()) { ... }
#   }

EDGES['E_rep10_045'] = {
    'src': 'ActionMode.onMenuItemSelected',
    'dst': 'MainFragment$3.onActionItemClicked(ActionMode,MenuItem)',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp10',
    'text': 'Android framework calls onActionItemClicked when ActionMode menu item selected',
    'evidence': 'SRC fragments/MainFragment.java:633 (ActionMode.Callback interface)'
}

EDGES['E_rep10_046'] = {
    'src': 'MainFragment$3.onActionItemClicked(ActionMode,MenuItem)',
    'dst': 'MainFragment.computeScroll()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onActionItemClicked calls computeScroll before processing menu action',
    'evidence': 'SRC fragments/MainFragment.java:634'
}

# ============================================================================
# MainFragment$3.onCreateActionMode
# ============================================================================
# REACHABLE: Framework callback when ActionMode is created
# Evidence: SRC fragments/MainFragment.java:482-512
#   public boolean onCreateActionMode(ActionMode mode, Menu menu) {
#       MenuInflater inflater = mode.getMenuInflater();
#       ...
#   }

EDGES['E_rep10_047'] = {
    'src': 'Activity.startActionMode',
    'dst': 'MainFragment$3.onCreateActionMode(ActionMode,Menu)',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp10',
    'text': 'Android framework calls onCreateActionMode when ActionMode starts',
    'evidence': 'SRC fragments/MainFragment.java:482 (ActionMode.Callback interface)'
}

EDGES['E_rep10_048'] = {
    'src': 'MainFragment$3.onCreateActionMode(ActionMode,Menu)',
    'dst': 'MainActivity.setPagingEnabled(boolean)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onCreateActionMode disables ViewPager paging during selection',
    'evidence': 'SRC fragments/MainFragment.java:488'
}

# ============================================================================
# MainFragment$3.onDestroyActionMode
# ============================================================================
# REACHABLE: Framework callback when ActionMode is destroyed
# Evidence: SRC fragments/MainFragment.java:757-776
#   public void onDestroyActionMode(ActionMode mode) {
#       mActionMode = null;
#       selection = false;
#       ...
#   }

EDGES['E_rep10_049'] = {
    'src': 'ActionMode.finish',
    'dst': 'MainFragment$3.onDestroyActionMode(ActionMode)',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp10',
    'text': 'Android framework calls onDestroyActionMode when ActionMode ends',
    'evidence': 'SRC fragments/MainFragment.java:757 (ActionMode.Callback interface)'
}

EDGES['E_rep10_050'] = {
    'src': 'MainFragment$3.onDestroyActionMode(ActionMode)',
    'dst': 'MainActivity.setPagingEnabled(boolean)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onDestroyActionMode re-enables ViewPager paging after selection',
    'evidence': 'SRC fragments/MainFragment.java:764'
}

# ============================================================================
# MainFragment$3.onPrepareActionMode
# ============================================================================
# REACHABLE: Framework callback when ActionMode is prepared/updated
# Evidence: SRC fragments/MainFragment.java:519-631
#   public boolean onPrepareActionMode(ActionMode mode, Menu menu) {
#       ArrayList<LayoutElementParcelable> positions = adapter.getCheckedItems();
#       ...
#   }

EDGES['E_rep10_051'] = {
    'src': 'ActionMode.invalidate',
    'dst': 'MainFragment$3.onPrepareActionMode(ActionMode,Menu)',
    'kind': 'FRAMEWORK',
    'origin': 'repair_rp10',
    'text': 'Android framework calls onPrepareActionMode to update menu based on selection',
    'evidence': 'SRC fragments/MainFragment.java:519 (ActionMode.Callback interface)'
}

EDGES['E_rep10_052'] = {
    'src': 'MainFragment$3.onPrepareActionMode(ActionMode,Menu)',
    'dst': 'RecyclerAdapter.getCheckedItems()',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onPrepareActionMode calls getCheckedItems to determine menu visibility',
    'evidence': 'SRC fragments/MainFragment.java:520'
}

# ============================================================================
# MainFragment$3.showOption
# ============================================================================
# REACHABLE: Called from onPrepareActionMode to show menu items
# Evidence: SRC fragments/MainFragment.java:468-471
#   private void showOption(int id, Menu menu) {
#       MenuItem item = menu.findItem(id);
#       item.setVisible(true);
#   }

EDGES['E_rep10_053'] = {
    'src': 'MainFragment$3.onPrepareActionMode(ActionMode,Menu)',
    'dst': 'MainFragment$3.showOption(int,Menu)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onPrepareActionMode calls showOption to make context menu items visible',
    'evidence': 'SRC fragments/MainFragment.java:543,544,545,555 (and many others)'
}

EDGES['E_rep10_054'] = {
    'src': 'MainFragment$3.onCreateActionMode(ActionMode,Menu)',
    'dst': 'MainFragment$3.showOption(int,Menu)',
    'kind': 'CALL',
    'origin': 'repair_rp10',
    'text': 'onCreateActionMode calls showOption for return intent mode',
    'evidence': 'SRC fragments/MainFragment.java:498'
}
