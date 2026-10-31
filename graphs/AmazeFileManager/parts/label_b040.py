# ---- Helper batch_040 label part (2026-10-27)

# ImmutableEntry - simple data holder, constructed in SearchTextTask
e('SearchTextTask.doInBackground', 'ImmutableEntry.<init>', 'CALL',
  'SearchTextTask constructs ImmutableEntry to hold search result positions',
  evidence='SRC SearchTextTask.java:67-69 nodes.add(new MapEntry(new ImmutableEntry<>(i, i + params[0].length()), lineNumberReader.getLineNumber()))')

e('SearchTextTask.onPostExecute', 'ImmutableEntry.getKey', 'CALL',
  'SearchTextTask.onPostExecute accesses entry key to highlight text',
  evidence='SRC SearchTextTask.java:88 Map.Entry keyMapEntry = (Map.Entry) mapEntry.getKey()')

e('SearchTextTask.onPostExecute', 'ImmutableEntry.getValue', 'CALL',
  'SearchTextTask.onPostExecute accesses entry value (MapEntry holds line number)',
  evidence='SRC SearchTextTask.java:67-69 new MapEntry(..., lineNumberReader.getLineNumber())')

# Icons - file type and icon resolution
e('LayoutElementParcelable.<init>', 'Icons.getTypeOfFile', 'CALL',
  'LayoutElementParcelable constructor determines file type',
  evidence='SRC LayoutElementParcelable.java:79 filetype = Icons.getTypeOfFile(path, isDirectory)')

e('LayoutElementParcelable.<init>', 'Icons.loadMimeIcon', 'CALL',
  'LayoutElementParcelable constructor loads fallback icon',
  evidence='SRC LayoutElementParcelable.java:80 int fallbackIcon = Icons.loadMimeIcon(path, isDirectory)')

e('CompressedObjectParcelable.<init>', 'Icons.getTypeOfFile', 'CALL',
  'CompressedObjectParcelable constructor determines file type',
  evidence='SRC CompressedObjectParcelable.java:53 this.filetype = Icons.getTypeOfFile(path, directory)')

e('CompressedObjectParcelable.<init>', 'Icons.loadMimeIcon', 'CALL',
  'CompressedObjectParcelable constructor loads icon',
  evidence='SRC CompressedObjectParcelable.java:55 Icons.loadMimeIcon(path, directory)')

e('FileUtils.openFile', 'Icons.getTypeOfFile', 'CALL',
  'FileUtils.openFile determines file type to decide how to open it',
  evidence='SRC FileUtils.java:539 int mimeType = Icons.getTypeOfFile(path, isDirectory)')

e('Icons.getTypeOfFile', 'Icons.checkType', 'CALL',
  'Icons.getTypeOfFile calls checkType for MIME category matching',
  evidence='SRC Icons.java:278 return checkType(mime, check)')

e('Icons.<clinit>', 'Icons.putKeys', 'CALL',
  'Icons static initializer populates MIME map',
  evidence='SRC Icons.java:46 static { putKeys(APK, ...)')

e('Icons.putKeys', 'Icons.put', 'CALL',
  'Icons.putKeys calls put for each MIME type',
  evidence='SRC Icons.java:38-40 for (String type : mimeTypes) { put(type, resId); }')

e('LayoutElementParcelable.<init>', 'Icons.<clinit>', 'FRAMEWORK',
  'First reference to Icons class triggers static initializer',
  evidence='INFERRED from class loading - Icons.<clinit> runs before Icons.getTypeOfFile at LayoutElementParcelable.java:79')

# HybridFileParcelable - Parcelable file representation
e('LayoutElementParcelable.generateBaseFile', 'HybridFileParcelable.<init>', 'CALL',
  'LayoutElementParcelable.generateBaseFile constructs HybridFileParcelable',
  evidence='SRC LayoutElementParcelable.java:134 HybridFileParcelable baseFile=new HybridFileParcelable(desc, permissions, date, longSize, isDirectory)')

e('AppsAdapter.onMenuItemClick', 'HybridFileParcelable.<init>', 'CALL',
  'AppsAdapter creates HybridFileParcelable for uninstall',
  evidence='SRC AppsAdapter.java:188 final HybridFileParcelable f1 = new HybridFileParcelable(rowItem.path)')

e('RootHelper.generateBaseFileFromFile', 'HybridFileParcelable.<init>', 'CALL',
  'RootHelper generates HybridFileParcelable from File',
  evidence='SRC RootHelper.java:116-118 HybridFileParcelable baseFile = new HybridFileParcelable(x.getPath(), parseFilePermission(x), x.lastModified(), size, x.isDirectory())')

e('HybridFile.listFiles', 'HybridFileParcelable.<init>', 'CALL',
  'HybridFile.listFiles creates HybridFileParcelable for SFTP/SMB',
  evidence='SRC HybridFile.java:747 HybridFileParcelable f = new HybridFileParcelable(String.format("%s/%s", path, info.getName()))')

e('AbstractProgressiveService.finalizeNotification', 'HybridFileParcelable.writeToParcel', 'INTENT',
  'Service sends HybridFileParcelable ArrayList via Intent, triggering parcel write',
  evidence='SRC AbstractProgressiveService.java:245 intent.putExtra(MainActivity.TAG_INTENT_FILTER_FAILED_OPS, failedOps)')

e('MainActivity.onCreate', 'HybridFileParcelable.describeContents', 'FRAMEWORK',
  'Framework calls describeContents when parceling',
  evidence='INFERRED from Parcelable contract at MainActivity.java:313')

e('MainActivity.onCreate', 'HybridFileParcelable$1.createFromParcel', 'FRAMEWORK',
  'Framework uses CREATOR.createFromParcel when unparceling',
  evidence='INFERRED from Parcelable contract at MainActivity.java:313')

e('HybridFileParcelable$1.createFromParcel', 'HybridFileParcelable.<init>', 'CALL',
  'CREATOR constructs HybridFileParcelable from Parcel',
  evidence='SRC HybridFileParcelable.java:108 return new HybridFileParcelable(in)')

e('MainActivity.onCreate', 'HybridFileParcelable$1.newArray', 'FRAMEWORK',
  'Framework uses CREATOR.newArray when unparceling',
  evidence='INFERRED from Parcelable contract at MainActivity.java:313')

e('MainActivity.onCreate', 'HybridFileParcelable.<clinit>', 'FRAMEWORK',
  'First reference to HybridFileParcelable triggers static initializer',
  evidence='INFERRED from class loading - HybridFileParcelable.<clinit> runs when class loaded for CREATOR access')

# HybridFileParcelable setters
e('LayoutElementParcelable.generateBaseFile', 'HybridFileParcelable.setName', 'CALL',
  'LayoutElementParcelable.generateBaseFile sets name',
  evidence='SRC LayoutElementParcelable.java:137 baseFile.setName(title)')

e('RootHelper.generateBaseFileFromFile', 'HybridFileParcelable.setName', 'CALL',
  'RootHelper sets name after construction',
  evidence='SRC RootHelper.java:119 baseFile.setName(x.getName())')

e('HybridFile.listFiles', 'HybridFileParcelable.setDate', 'CALL',
  'HybridFile.listFiles sets date for SFTP files',
  evidence='SRC HybridFile.java:751 f.setDate(info.getAttributes().getMtime() * 1000)')

e('HybridFile.listFiles', 'HybridFileParcelable.setDirectory', 'CALL',
  'HybridFile.listFiles sets directory flag',
  evidence='SRC HybridFile.java:750 f.setDirectory(isDirectory)')

e('HybridFile.listFiles', 'HybridFileParcelable.setSize', 'CALL',
  'HybridFile.listFiles sets size',
  evidence='SRC HybridFile.java:752 f.setSize(isDirectory ? 0 : info.getAttributes().getSize())')

e('HybridFile.listFiles', 'HybridFileParcelable.setPermission', 'CALL',
  'HybridFile.listFiles sets permission',
  evidence='SRC HybridFile.java:753 f.setPermission(Integer.toString(FilePermission.toMask(info.getAttributes().getPermissions()), 8))')

e('FileUtils.putFileInArrayList', 'HybridFileParcelable.setLink', 'CALL',
  'FileUtils sets symlink target',
  evidence='SRC FileUtils.java:941 baseFile.setLink(link.toString())')

# HybridFileParcelable getters - all accessed polymorphically
e('TextEditorActivity.saveFile', 'HybridFileParcelable.getPath', 'CALL',
  'TextEditorActivity accesses path from HybridFileParcelable',
  evidence='SRC TextEditorActivity.java:302 mFile.hybridFileParcelable.getPath().contains(getExternalCacheDir().getPath())')

e('DatabaseViewerActivity.onCreate', 'HybridFileParcelable.getPath', 'CALL',
  'DatabaseViewerActivity uses getPath',
  evidence='SRC DatabaseViewerActivity.java:165 RootUtils.copy(pathFile.getPath(), ...)')

e('EditableFileAbstraction.<init>', 'HybridFileParcelable.getName', 'CALL',
  'EditableFileAbstraction constructor gets name from HybridFileParcelable',
  evidence='SRC EditableFileAbstraction.java:71 String tempN = hybridFileParcelable.getName(context)')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.getName', 'CALL',
  'LoadFilesListTask accesses baseFile.getName for LayoutElement',
  evidence='SRC LoadFilesListTask.java:247 LayoutElementParcelable layoutElement = new LayoutElementParcelable(c, baseFile.getName(), ...')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.getPermission', 'CALL',
  'LoadFilesListTask accesses baseFile.getPermission for LayoutElement',
  evidence='SRC LoadFilesListTask.java:249 baseFile.getPath(), baseFile.getPermission(), baseFile.getLink(), ...')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.getLink', 'CALL',
  'LoadFilesListTask accesses baseFile.getLink for LayoutElement',
  evidence='SRC LoadFilesListTask.java:249 baseFile.getPermission(), baseFile.getLink(), size, ...')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.getDate', 'CALL',
  'LoadFilesListTask accesses baseFile.getDate for LayoutElement',
  evidence='SRC LoadFilesListTask.java:250 longSize, false, baseFile.getDate() + "", baseFile.isDirectory(), ...')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.isDirectory', 'CALL',
  'LoadFilesListTask accesses baseFile.isDirectory for LayoutElement',
  evidence='SRC LoadFilesListTask.java:250 baseFile.getDate() + "", baseFile.isDirectory(), ...')

e('CopyService.checkFiles', 'HybridFileParcelable.getMode', 'CALL',
  'CopyService accesses baseFile.getMode for HybridFile construction',
  evidence='SRC CopyService.java:494 new HybridFile(baseFile.getMode(), baseFile.getPath())')

e('LoadFilesListTask.addToSmallestContainer', 'HybridFileParcelable.getSize', 'CALL',
  'LoadFilesListTask uses baseFile.getSize indirectly through size variable',
  evidence='INFERRED from LoadFilesListTask pattern - size field accessed via getter')

e('HybridFileParcelable.getName', 'HybridFileParcelable.isHidden', 'CALL',
  'HybridFileParcelable.isHidden checks if name starts with dot',
  evidence='SRC HybridFileParcelable.java:77 public boolean isHidden(){ return name.startsWith("."); }')

e('ArrayList.contains', 'HybridFileParcelable.equals', 'FRAMEWORK',
  'Collection operations call equals',
  evidence='INFERRED from ArrayList.contains when holding HybridFileParcelable')

e('HashMap.put', 'HybridFileParcelable.hashCode', 'FRAMEWORK',
  'HashMap operations call hashCode',
  evidence='INFERRED from HashMap usage with HybridFileParcelable')

# UNREACHABLE methods
UNREACHABLE_PART_B040 = {
    'ImmutableEntry.setValue': ('no_trigger_in_app', 'ImmutableEntry.setValue always throws UnsupportedOperationException per immutable contract - no caller attempts it', 'SRC ImmutableEntry.java:48-50 public final V setValue(V value) { throw new UnsupportedOperationException(); }', 'SOURCE'),
    
    'HybridFileParcelable.toString': ('no_trigger_in_app', 'HybridFileParcelable.toString not explicitly called in app code - only implicit via debugger', 'SRC HybridFileParcelable.java:139-145', 'INFERRED'),
    
    'Icons.<init>': ('no_trigger_in_app', 'Icons has only static members - no instance ever created', 'SRC Icons.java:29 public class Icons', 'INFERRED'),
    
    'HybridFileParcelable$1.<init>': ('framework_never_calls', 'Anonymous CREATOR constructor called once at class load for static field init', 'SRC HybridFileParcelable.java:105 public static final Creator<HybridFileParcelable> CREATOR = new Creator<HybridFileParcelable>() {...}', 'INFERRED'),
}

# Note: HybridFileParcelable.<clinit> and Icons.<clinit> are REACHABLE - they are static initializers
# that run when the class is first loaded. HybridFileParcelable.<clinit> initializes the CREATOR field,
# and Icons.<clinit> populates the MIME type map. Both are reached via class loading.
