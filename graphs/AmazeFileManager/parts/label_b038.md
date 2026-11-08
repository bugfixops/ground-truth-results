STATUS: RUNNING 21:56

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| HybridFile.<init>(OpenMode,String) | REACHABLE | | Constructor called from MainFragment, LoadFilesListTask, many file operations | SRC HybridFile.java:70-73, MainFragment.java:279 |
| HybridFile.<init>(OpenMode,String,String,boolean) | REACHABLE | | Constructor with name/isDirectory called from CopyService for file operations | SRC HybridFile.java:75-90, CopyService.java:361,366,399 |
| HybridFile.generateMode(Context) | REACHABLE | | Called to determine file mode from path characteristics | SRC HybridFile.java:91-131 |
| HybridFile.setMode(OpenMode) | REACHABLE | | Setter called to change mode, used after generateMode | SRC HybridFile.java:132-134 |
| HybridFile.getMode() | REACHABLE | | Getter called from ItemPopupMenu, LoadFilesListTask | SRC HybridFile.java:136-138, ItemPopupMenu.java:82,87 |
| HybridFile.setPath(String) | REACHABLE | | Setter for path field | SRC HybridFile.java:140-142 |
| HybridFile.isLocal() | REACHABLE | | Mode check called from FileUtils, GeneralDialogCreation, Operations | SRC HybridFile.java:144-146, FileUtils.java:244,266 |
| HybridFile.isRoot() | REACHABLE | | Mode check called from filesystem operations | SRC HybridFile.java:148-150 |
| HybridFile.isSmb() | REACHABLE | | Mode check for SMB protocol, called throughout app | SRC HybridFile.java:152-154 |
| HybridFile.isSftp() | REACHABLE | | Mode check for SFTP protocol | SRC HybridFile.java:156-156 |
| HybridFile.isOtgFile() | REACHABLE | | Mode check for OTG files, called from FileUtils | SRC HybridFile.java:158-160, FileUtils.java:266 |
| HybridFile.isBoxFile() | REACHABLE | | Mode check for Box cloud storage | SRC HybridFile.java:162-164 |
| HybridFile.isDropBoxFile() | REACHABLE | | Mode check for Dropbox cloud storage | SRC HybridFile.java:166-168 |
| HybridFile.isOneDriveFile() | REACHABLE | | Mode check for OneDrive cloud storage | SRC HybridFile.java:170-172 |
| HybridFile.isGoogleDriveFile() | REACHABLE | | Mode check for Google Drive cloud storage | SRC HybridFile.java:174-176 |
| HybridFile.getFile() | REACHABLE | | Returns File object for local files | SRC HybridFile.java:178-180 |
| HybridFile.generateBaseFileFromParent() | REACHABLE | | Helper to get file info from parent directory listing | SRC HybridFile.java:182-189 |
| HybridFile.lastModified() | REACHABLE | | Gets last modified time, handles all file modes | SRC HybridFile.java:191-218 |
| HybridFile.length() | REACHABLE | | Deprecated length method without context | SRC HybridFile.java:220-250 |
| HybridFile.length(Context) | REACHABLE | | Gets file size, called from DecryptService, EncryptService, CloudUtil | SRC HybridFile.java:252-296, DecryptService.java:132 |
| HybridFile.getPath() | REACHABLE | | Heavily used getter for file path (246 callers found) | SRC HybridFile.java:298-300 |
| HybridFile.getName() | REACHABLE | | Deprecated getName without context | SRC HybridFile.java:305-322 |
| HybridFile.getName(Context) | REACHABLE | | Gets file name, called from GeneralDialogCreation, Drawer | SRC HybridFile.java:324-344, GeneralDialogCreation.java:380 |
| HybridFile.getSmbFile(int) | REACHABLE | | Gets SmbFile with timeout parameter | SRC HybridFile.java:345-352 |
| HybridFile.getSmbFile() | REACHABLE | | Gets SmbFile with default timeout | SRC HybridFile.java:354-360 |
| HybridFile.isCustomPath() | REACHABLE | | Checks for custom paths 0-6, called internally from generateMode and isSimpleFile | SRC HybridFile.java:362-370, called at HybridFile.java:98,1132 |
| HybridFile.getParent() | REACHABLE | | Deprecated getParent without context | SRC HybridFile.java:376-399 |
| HybridFile.getParent(Context) | REACHABLE | | Gets parent path, called from MainFragment | SRC HybridFile.java:401-425, MainFragment.java:1317 |
| HybridFile.getParentName() | REACHABLE | | Gets parent directory name | SRC HybridFile.java:427-434 |
| HybridFile.isDirectory() | REACHABLE | | Deprecated isDirectory without context | SRC HybridFile.java:440-478 |
| HybridFile.isDirectory(Context) | REACHABLE | | Checks if path is directory, called from GeneralDialogCreation | SRC HybridFile.java:480-546, GeneralDialogCreation.java:383,418 |
| HybridFile.folderSize() | REACHABLE | | Deprecated folderSize without context | SRC HybridFile.java:548-576 |
| HybridFile.folderSize(Context) | REACHABLE | | Gets folder size for all modes | SRC HybridFile.java:578-623 |
| HybridFile.getUsableSpace() | REACHABLE | | Gets free space on device/storage | SRC HybridFile.java:625-677 |
| HybridFile.getTotal(Context) | REACHABLE | | Gets total storage space | SRC HybridFile.java:679-731 |
| HybridFile.forEachChildrenFile(Context,boolean,OnFileFound) | REACHABLE | | Iterates children files for all modes | SRC HybridFile.java:733-803 |
| HybridFile.listFiles(Context,boolean) | REACHABLE | | Deprecated listFiles returning ArrayList | SRC HybridFile.java:805-876 |
| HybridFile.getReadablePath(String) | REACHABLE | | Parses path for display | SRC HybridFile.java:878-884 |
| HybridFile.parseSftpPath(String) | REACHABLE | | Helper to parse SFTP paths | SRC HybridFile.java:886-890 |
| HybridFile.parseSmbPath(String) | REACHABLE | | Helper to parse SMB paths | SRC HybridFile.java:892-896 |
| HybridFile.getInputStream() | REACHABLE | | Deprecated getInputStream without context | SRC HybridFile.java:902-931 |
| HybridFile.getInputStream(Context) | REACHABLE | | Gets InputStream for reading, called from CloudUtil | SRC HybridFile.java:943-1015, CloudUtil.java:139 |
| HybridFile.getOutputStream(Context) | REACHABLE | | Gets OutputStream for writing | SRC HybridFile.java:1017-1073 |
| HybridFile.exists() | REACHABLE | | Checks file existence without context | SRC HybridFile.java:1075-1117 |
| HybridFile.exists(Context) | REACHABLE | | Checks file existence, called from FileUtils | SRC HybridFile.java:1119-1126, FileUtils.java:244,266 |
| HybridFile.isSimpleFile() | REACHABLE | | Checks if file is simple local file (not directory/smb/otg/cloud) | SRC HybridFile.java:1131-1136 |
| HybridFile.setLastModified(long) | REACHABLE | | Sets last modified timestamp | SRC HybridFile.java:1138-1150 |
| HybridFile.mkdir(Context) | REACHABLE | | Creates directory for all modes, called from CopyService | SRC HybridFile.java:1154-1210, CopyService.java:446 |
| HybridFile.delete(Context,boolean) | REACHABLE | | Deletes file/directory, called from DeleteTask | SRC HybridFile.java:1212-1241, DeleteTask.java:133 |
| HybridFile.getNameString(Context) | REACHABLE | | Gets filename without extension | SRC HybridFile.java:1246-1253 |
| HybridFile.generateLayoutElement(Context,boolean) | REACHABLE | | Generates UI element for local/root files | SRC HybridFile.java:1257-1278 |

STATUS: DONE 22:00
