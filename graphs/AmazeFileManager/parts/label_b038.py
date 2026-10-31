# ---- Helper batch_038 label part (2026-10-27)
# HybridFile class - core file abstraction for all file types

# HybridFile constructors - heavily used throughout app
e('MainFragment.onActivityCreated', 'HybridFile.<init>(OpenMode,String)', 'CALL', 
  'MainFragment creates HybridFile for current path',
  evidence='SRC MainFragment.java:279 HybridFile f = new HybridFile(OpenMode.UNKNOWN, CURRENT_PATH);')

e('LoadFilesListTask.doInBackground', 'HybridFile.<init>(OpenMode,String)', 'CALL',
  'LoadFilesListTask creates HybridFile to load directory',
  evidence='SRC LoadFilesListTask.java:90 hFile = new HybridFile(OpenMode.UNKNOWN, path);')

e('CopyService.startService', 'HybridFile.<init>(OpenMode,String,String,boolean)', 'CALL',
  'CopyService creates HybridFile with name for copy target',
  evidence='SRC CopyService.java:361,366,399 hFile = new HybridFile(OpenMode.FILE, targetPath, sourceFiles.get(i).getName(), ...)');

# HybridFile internal constructor calls
e('HybridFile.<init>(OpenMode,String)', 'HybridFile.setMode', 'CALL',
  'Constructor sets initial mode',
  evidence='SRC HybridFile.java:72 this.mode = mode;')

e('HybridFile.<init>(OpenMode,String)', 'HybridFile.setPath', 'CALL',
  'Constructor sets path',
  evidence='SRC HybridFile.java:71 this.path = path;')

e('HybridFile.<init>(OpenMode,String,String,boolean)', 'HybridFile.setMode', 'CALL',
  'Second constructor also sets mode',
  evidence='SRC HybridFile.java:75-76 this(mode, path);')

e('LoadFilesListTask.doInBackground', 'HybridFile.generateMode', 'CALL',
  'LoadFilesListTask calls generateMode to determine file type from path',
  evidence='SRC LoadFilesListTask.java:91 hFile.generateMode(mContext);')

e('HybridFile.generateMode', 'HybridFile.isCustomPath', 'CALL',
  'generateMode checks for custom paths 0-6',
  evidence='SRC HybridFile.java:98 } else if (isCustomPath()) {')

e('HybridFile.generateMode', 'HybridFile.getFile', 'CALL',
  'generateMode gets File object to check readability',
  evidence='SRC HybridFile.java:116,120 if (rootmode && !getFile().canRead())')

# Mode getters
e('ItemPopupMenu.create', 'HybridFile.getMode', 'CALL',
  'ItemPopupMenu gets mode to determine sharing options',
  evidence='SRC ItemPopupMenu.java:82,87 switch (rowItem.getMode()) ... FileUtils.shareCloudFile(rowItem.desc, rowItem.getMode(), context);')

e('LoadFilesListTask.doInBackground', 'HybridFile.getMode', 'CALL',
  'LoadFilesListTask reads mode after generateMode',
  evidence='SRC LoadFilesListTask.java:92 openmode = hFile.getMode();')

# Mode checking methods - used extensively throughout app
e('FileUtils.scanFile', 'HybridFile.isLocal', 'CALL',
  'FileUtils checks if local file for MediaScanner',
  evidence='SRC FileUtils.java:244,266 if (hybridFiles[0].exists(context) && hybridFiles[0].isLocal()) ... if((hybridFile.isLocal() || hybridFile.isOtgFile()) && hybridFile.exists(context))')

e('GeneralDialogCreation.showPropertiesDialog', 'HybridFile.isLocal', 'CALL',
  'Properties dialog checks if local for folder size calculation',
  evidence='SRC GeneralDialogCreation.java:418 if (baseFile.isDirectory() && baseFile.isLocal())')

e('Operations.mkfile', 'HybridFile.isRoot', 'CALL',
  'Operations checks root mode',
  evidence='SRC Operations.java:162 if (file.isLocal() || file.isRoot())')

e('HybridFile.lastModified', 'HybridFile.isSmb', 'CALL',
  'lastModified switches on SMB mode',
  evidence='SRC HybridFile.java:201 case SMB:')

e('HybridFile.lastModified', 'HybridFile.isSftp', 'CALL',
  'lastModified switches on SFTP mode',
  evidence='SRC HybridFile.java:194 case SFTP:')

e('FileUtils.scanFile', 'HybridFile.isOtgFile', 'CALL',
  'FileUtils checks OTG mode',
  evidence='SRC FileUtils.java:266 if((hybridFile.isLocal() || hybridFile.isOtgFile())')

e('HybridFile.exists', 'HybridFile.isBoxFile', 'CALL',
  'exists checks for Box cloud mode',
  evidence='SRC HybridFile.java:1088 } else if (isBoxFile()) {')

e('HybridFile.exists', 'HybridFile.isDropBoxFile', 'CALL',
  'exists checks for Dropbox mode',
  evidence='SRC HybridFile.java:1084 } else if (isDropBoxFile()) {')

e('HybridFile.exists', 'HybridFile.isOneDriveFile', 'CALL',
  'exists checks for OneDrive mode',
  evidence='SRC HybridFile.java:1096 } else if (isOneDriveFile()) {')

e('HybridFile.exists', 'HybridFile.isGoogleDriveFile', 'CALL',
  'exists checks for Google Drive mode',
  evidence='SRC HybridFile.java:1092 } else if (isGoogleDriveFile()) {')

e('HybridFile.isSimpleFile', 'HybridFile.isCustomPath', 'CALL',
  'isSimpleFile excludes custom paths',
  evidence='SRC HybridFile.java:1132 return !isSmb() && !isOtgFile() && !isCustomPath()')

e('HybridFile.isSimpleFile', 'HybridFile.isSmb', 'CALL',
  'isSimpleFile checks not SMB',
  evidence='SRC HybridFile.java:1132 return !isSmb()')

e('HybridFile.isSimpleFile', 'HybridFile.isOtgFile', 'CALL',
  'isSimpleFile checks not OTG',
  evidence='SRC HybridFile.java:1132 && !isOtgFile()')

e('HybridFile.isSimpleFile', 'HybridFile.isSftp', 'CALL',
  'isSimpleFile checks not SFTP',
  evidence='SRC HybridFile.java:1135 && !isSftp();')

e('HybridFile.isSimpleFile', 'HybridFile.isOneDriveFile', 'CALL',
  'isSimpleFile checks not OneDrive',
  evidence='SRC HybridFile.java:1134 && !isOneDriveFile()')

e('HybridFile.isSimpleFile', 'HybridFile.isGoogleDriveFile', 'CALL',
  'isSimpleFile checks not Google Drive',
  evidence='SRC HybridFile.java:1134 && !isGoogleDriveFile()')

e('HybridFile.isSimpleFile', 'HybridFile.isDropBoxFile', 'CALL',
  'isSimpleFile checks not Dropbox',
  evidence='SRC HybridFile.java:1135 && !isDropBoxFile()')

e('HybridFile.isSimpleFile', 'HybridFile.isBoxFile', 'CALL',
  'isSimpleFile checks not Box',
  evidence='SRC HybridFile.java:1135 && !isBoxFile()')

# File property getters
e('MainFragment.loadlist', 'HybridFile.getParent', 'CALL',
  'MainFragment gets parent path for navigation',
  evidence='SRC MainFragment.java:1317 String parentPath = new HybridFile(openMode, CURRENT_PATH).getParent(getActivity());')

e('HybridFile.getParent', 'HybridFile.getName', 'CALL',
  'getParent uses getName to calculate parent',
  evidence='SRC HybridFile.java:398 return builder.substring(0, builder.length() - (getName().length() + 1));')

e('HybridFile.getParent', 'HybridFile.getSmbFile', 'CALL',
  'getParent gets SmbFile for SMB mode',
  evidence='SRC HybridFile.java:389 parentPath = new SmbFile(path).getParent();')

e('GeneralDialogCreation.showPropertiesDialog', 'HybridFile.getName', 'CALL',
  'Properties dialog gets filename',
  evidence='SRC GeneralDialogCreation.java:380 name = baseFile.getName(),')

e('HybridFile.getParentName', 'HybridFile.getName', 'CALL',
  'getParentName uses getName',
  evidence='SRC HybridFile.java:428-429 StringBuilder parentPath = new StringBuilder(builder.substring(0, builder.length() - (getName().length() + 1)));')

e('GeneralDialogCreation.showPropertiesDialog', 'HybridFile.isDirectory', 'CALL',
  'Properties dialog checks if directory',
  evidence='SRC GeneralDialogCreation.java:383,418 File nomediaFile = baseFile.isDirectory()? ... if (baseFile.isDirectory() && baseFile.isLocal())')

e('HybridFile.isDirectory', 'HybridFile.getFile', 'CALL',
  'isDirectory gets File for local mode',
  evidence='SRC HybridFile.java:458 isDirectory = new File(path).isDirectory();')

e('HybridFile.isDirectory', 'HybridFile.getSmbFile', 'CALL',
  'isDirectory gets SmbFile for SMB mode',
  evidence='SRC HybridFile.java:451 isDirectory = new SmbFile(path).isDirectory();')

e('DecryptService.onStartCommand', 'HybridFile.length', 'CALL',
  'DecryptService gets file size',
  evidence='SRC DecryptService.java:132 else totalSize = baseFile.length(context);')

e('HybridFile.length', 'HybridFile.generateBaseFileFromParent', 'CALL',
  'length gets file info from parent for root mode',
  evidence='SRC HybridFile.java:245 HybridFileParcelable baseFile = generateBaseFileFromParent();')

e('HybridFile.lastModified', 'HybridFile.generateBaseFileFromParent', 'CALL',
  'lastModified gets info from parent for root mode',
  evidence='SRC HybridFile.java:214 HybridFileParcelable baseFile = generateBaseFileFromParent();')

e('HybridFile.lastModified', 'HybridFile.getSmbFile', 'CALL',
  'lastModified gets SmbFile',
  evidence='SRC HybridFile.java:202 SmbFile smbFile = getSmbFile();')

e('HybridFile.length', 'HybridFile.getSmbFile', 'CALL',
  'length gets SmbFile',
  evidence='SRC HybridFile.java:233 SmbFile smbFile=getSmbFile();')

e('HybridFile.folderSize', 'HybridFile.getSmbFile', 'CALL',
  'folderSize gets SmbFile',
  evidence='SRC HybridFile.java:557 size = FileUtils.folderSize(new SmbFile(path));')

e('HybridFile.getUsableSpace', 'HybridFile.getSmbFile', 'CALL',
  'getUsableSpace gets SmbFile',
  evidence='SRC HybridFile.java:632 size = (new SmbFile(path).getDiskFreeSpace());')

e('CloudUtil.launchCloud', 'HybridFile.getInputStream', 'CALL',
  'CloudUtil gets input stream to stream file',
  evidence='SRC CloudUtil.java:139 streamer.setStreamSrc(baseFile.getInputStream(activity), baseFile.getName(), baseFile.length(activity));')

e('HybridFile.getInputStream', 'HybridFile.isSftp', 'CALL',
  'getInputStream checks SFTP mode',
  evidence='SRC HybridFile.java:904 if (isSftp()) {')

e('HybridFile.getInputStream', 'HybridFile.isSmb', 'CALL',
  'getInputStream checks SMB mode',
  evidence='SRC HybridFile.java:922 else if (isSmb()) {')

e('FileUtils.scanFile', 'HybridFile.exists', 'CALL',
  'FileUtils checks file existence before scanning',
  evidence='SRC FileUtils.java:244,266 if (hybridFiles[0].exists(context) && ... if((hybridFile.isLocal() || hybridFile.isOtgFile()) && hybridFile.exists(context))')

e('HybridFile.exists', 'HybridFile.isSftp', 'CALL',
  'exists checks for SFTP mode',
  evidence='SRC HybridFile.java:1076 if (isSftp()) {')

e('HybridFile.exists', 'HybridFile.isSmb', 'CALL',
  'exists checks for SMB mode',
  evidence='SRC HybridFile.java:1086 } else if (isSmb()) {')

e('HybridFile.exists', 'HybridFile.isLocal', 'CALL',
  'exists checks for local mode',
  evidence='SRC HybridFile.java:1100 } else if (isLocal()) {')

e('HybridFile.exists', 'HybridFile.isRoot', 'CALL',
  'exists checks for root mode',
  evidence='SRC HybridFile.java:1102 } else if (isRoot()) {')

e('HybridFile.exists', 'HybridFile.getSmbFile', 'CALL',
  'exists gets SmbFile with timeout',
  evidence='SRC HybridFile.java:1088 SmbFile smbFile = getSmbFile(2000);')

e('HybridFile.exists', 'HybridFile.getPath', 'CALL',
  'exists gets path',
  evidence='SRC HybridFile.java:1103 return RootHelper.fileExists(path);')

e('CopyService.startService', 'HybridFile.mkdir', 'CALL',
  'CopyService creates target directory',
  evidence='SRC CopyService.java:446 if (!targetFile.exists()) targetFile.mkdir(c);')

e('HybridFile.mkdir', 'HybridFile.isSftp', 'CALL',
  'mkdir checks SFTP mode',
  evidence='SRC HybridFile.java:1155 if(isSftp()) {')

e('HybridFile.mkdir', 'HybridFile.isSmb', 'CALL',
  'mkdir checks SMB mode',
  evidence='SRC HybridFile.java:1168 } else if (isSmb()) {')

e('HybridFile.mkdir', 'HybridFile.isOtgFile', 'CALL',
  'mkdir checks OTG mode',
  evidence='SRC HybridFile.java:1173 } else if (isOtgFile()) {')

e('HybridFile.mkdir', 'HybridFile.isDropBoxFile', 'CALL',
  'mkdir checks Dropbox mode',
  evidence='SRC HybridFile.java:1181 } else if (isDropBoxFile()) {')

e('HybridFile.mkdir', 'HybridFile.isBoxFile', 'CALL',
  'mkdir checks Box mode',
  evidence='SRC HybridFile.java:1189 } else if (isBoxFile()) {')

e('HybridFile.mkdir', 'HybridFile.isOneDriveFile', 'CALL',
  'mkdir checks OneDrive mode',
  evidence='SRC HybridFile.java:1197 } else if (isOneDriveFile()) {')

e('HybridFile.mkdir', 'HybridFile.isGoogleDriveFile', 'CALL',
  'mkdir checks Google Drive mode',
  evidence='SRC HybridFile.java:1205 } else if (isGoogleDriveFile()) {')

e('HybridFile.mkdir', 'HybridFile.getParent', 'CALL',
  'mkdir gets parent for OTG',
  evidence='SRC HybridFile.java:1176 DocumentFile parentDirectory = OTGUtil.getDocumentFile(getParent(context), context, false);')

e('HybridFile.mkdir', 'HybridFile.getName', 'CALL',
  'mkdir gets name for OTG',
  evidence='SRC HybridFile.java:1178 parentDirectory.createDirectory(getName(context));')

e('DeleteTask.doInBackground', 'HybridFile.delete', 'CALL',
  'DeleteTask deletes file',
  evidence='SRC DeleteTask.java:133 if (file.delete(cd, rootMode))')

e('HybridFile.delete', 'HybridFile.isSftp', 'CALL',
  'delete checks SFTP mode',
  evidence='SRC HybridFile.java:1213 if (isSftp()) {')

e('HybridFile.delete', 'HybridFile.isSmb', 'CALL',
  'delete checks SMB mode',
  evidence='SRC HybridFile.java:1226 } else if (isSmb()) {')

e('HybridFile.delete', 'HybridFile.isRoot', 'CALL',
  'delete checks root mode',
  evidence='SRC HybridFile.java:1234 if (isRoot() && rootmode) {')

e('HybridFile.delete', 'HybridFile.setMode', 'CALL',
  'delete sets ROOT mode before deleting',
  evidence='SRC HybridFile.java:1235 setMode(OpenMode.ROOT);')

e('HybridFile.delete', 'HybridFile.getPath', 'CALL',
  'delete gets path for RootUtils',
  evidence='SRC HybridFile.java:1236 RootUtils.delete(getPath());')

e('HybridFile.setLastModified', 'HybridFile.isSmb', 'CALL',
  'setLastModified checks SMB mode',
  evidence='SRC HybridFile.java:1139 if (isSmb()) {')

e('HybridFile.getReadablePath', 'HybridFile.isSftp', 'CALL',
  'getReadablePath checks SFTP',
  evidence='SRC HybridFile.java:879 if (isSftp())')

e('HybridFile.getReadablePath', 'HybridFile.isSmb', 'CALL',
  'getReadablePath checks SMB',
  evidence='SRC HybridFile.java:881 if (isSmb())')

e('HybridFile.getReadablePath', 'HybridFile.parseSftpPath', 'CALL',
  'getReadablePath parses SFTP path',
  evidence='SRC HybridFile.java:880 return parseSftpPath(path);')

e('HybridFile.getReadablePath', 'HybridFile.parseSmbPath', 'CALL',
  'getReadablePath parses SMB path',
  evidence='SRC HybridFile.java:882 return parseSmbPath(path);')

e('HybridFile.generateLayoutElement', 'HybridFile.isDirectory', 'CALL',
  'generateLayoutElement checks if directory',
  evidence='SRC HybridFile.java:1262 if (isDirectory()) {')

e('HybridFile.generateLayoutElement', 'HybridFile.folderSize', 'CALL',
  'generateLayoutElement gets folder size',
  evidence='SRC HybridFile.java:1265 "", folderSize() + "", 0, true')

e('HybridFile.generateLayoutElement', 'HybridFile.getFile', 'CALL',
  'generateLayoutElement gets File object',
  evidence='SRC HybridFile.java:1259,1270 File file = new File(path);')

# UNREACHABLE methods - none, all 51 methods are reachable

