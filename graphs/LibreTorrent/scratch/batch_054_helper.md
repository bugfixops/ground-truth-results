# LibreTorrent batch 54 source audit

Membership is exactly the 40 batch 54 rows printed at the top of `batch_054_helper_printed.txt`. The evidence file contains the source for the default filesystem module, file descriptor wrapper, facade, module resolver, SAF filesystem, interfaces, and a source-root call-site search. Methods remain OPEN because complete app-entry-to-file-operation routes (including URI origin, resolver dispatch, and SAF selection) were not traced end-to-end. Local implementation calls do not alone establish those routes. No missing caller match is used as proof of unreachability.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `DefaultFsModule.getParentDirUri(Uri)Uri` | OPEN | `DefaultFsModule.java` source printed; full URI-origin and caller route unresolved. |
| 2 | `DefaultFsModule.makeFileSystemPath(Uri,String)String` | OPEN | `DefaultFsModule.java` source printed; full URI-origin and caller route unresolved. |
| 3 | `DefaultFsModule.openFD(Uri)FileDescriptorWrapper` | OPEN | `DefaultFsModule.java` source printed; complete file operation route unresolved. |
| 4 | `FileDescriptorWrapperImpl.<init>(Context,Uri)V` | OPEN | Constructor source printed; full SAF/default module construction route unresolved. |
| 5 | `FileDescriptorWrapperImpl.close()V` | OPEN | Method body printed; full descriptor acquisition/release route unresolved. |
| 6 | `FileDescriptorWrapperImpl.open(String)FileDescriptor` | OPEN | Method body printed; complete file-selection and descriptor-use route unresolved. |
| 7 | `FileSystemFacadeImpl.<clinit>()V` | OPEN | Class source/static setup printed; class initialization from an app entry not traced. |
| 8 | `FileSystemFacadeImpl.<init>(Context,FsModuleResolver)V` | OPEN | Constructor and resolver construction printed; full dependency construction route unresolved. |
| 9 | `FileSystemFacadeImpl.buildValidFatFilename(String)String` | OPEN | Body and internal uses printed; full route to callers unresolved. |
| 10 | `FileSystemFacadeImpl.cleanTempDir()V` | OPEN | Body and callers searched; full startup/cleanup route unresolved. |
| 11 | `FileSystemFacadeImpl.createFile(Uri,String,boolean)Uri` | OPEN | Body and callers printed; URI-origin and UI-to-storage route unresolved. |
| 12 | `FileSystemFacadeImpl.deleteFile(Uri)boolean` | OPEN | Body and callers printed; complete UI-to-storage route unresolved. |
| 13 | `FileSystemFacadeImpl.fileExists(Uri)boolean` | OPEN | Body and callers printed; complete URI-to-filesystem route unresolved. |
| 14 | `FileSystemFacadeImpl.getDefaultDownloadPath()String` | OPEN | Body and callers printed; session/settings entry route unresolved. |
| 15 | `FileSystemFacadeImpl.getDirAvailableBytes(Uri)long` | OPEN | Body and callers printed; complete URI-selection route unresolved. |
| 16 | `FileSystemFacadeImpl.getDirPath(Uri)String` | OPEN | Body and callers printed; URI origin and module routing unresolved. |
| 17 | `FileSystemFacadeImpl.getExtension(String)String` | OPEN | Body and internal uses printed; complete caller route unresolved. |
| 18 | `FileSystemFacadeImpl.getExtensionSeparator()String` | OPEN | Body and internal uses printed; complete caller route unresolved. |
| 19 | `FileSystemFacadeImpl.getFD(Uri)FileDescriptorWrapper` | OPEN | Body and callers printed; complete URI-to-descriptor route unresolved. |
| 20 | `FileSystemFacadeImpl.getFilePath(Uri)String` | OPEN | Body and callers printed; URI origin and module routing unresolved. |
| 21 | `FileSystemFacadeImpl.getFileUri(Uri,String)Uri` | OPEN | Overload body and callers printed; source URI and entry route unresolved. |
| 22 | `FileSystemFacadeImpl.getFileUri(String,Uri)Uri` | OPEN | Overload body and callers printed; destination and entry route unresolved. |
| 23 | `FileSystemFacadeImpl.getParentDirUri(Uri)Uri` | OPEN | Body and callers printed; URI origin and module routing unresolved. |
| 24 | `FileSystemFacadeImpl.getTempDir()File` | OPEN | Body and callers printed; full initialization/cleanup route unresolved. |
| 25 | `FileSystemFacadeImpl.getUserDirPath()String` | OPEN | Body and callers printed; complete settings/filesystem route unresolved. |
| 26 | `FileSystemFacadeImpl.isStorageReadable()boolean` | OPEN | Body and callers printed; complete startup/storage route unresolved. |
| 27 | `FileSystemFacadeImpl.isValidFatFilenameChar(char)boolean` | OPEN | Body and internal uses printed; complete path-to-caller route unresolved. |
| 28 | `FileSystemFacadeImpl.makeFileSystemPath(Uri)String` | OPEN | Overload body and callers printed; URI origin and module routing unresolved. |
| 29 | `FileSystemFacadeImpl.makeFileSystemPath(Uri,String)String` | OPEN | Overload body and callers printed; URI origin and module routing unresolved. |
| 30 | `FileSystemFacadeImpl.makeTempFile(String)File` | OPEN | Body and callers printed; complete temporary-file operation route unresolved. |
| 31 | `FileSystemFacadeImpl.normalizeFileSystemPath(String)String` | OPEN | Body and internal uses printed; complete caller route unresolved. |
| 32 | `FileSystemFacadeImpl.trimFilename(StringBuilder,int)V` | OPEN | Body and internal uses printed; complete caller route unresolved. |
| 33 | `FileSystemFacadeImpl.write(CharSequence,Charset,Uri)V` | OPEN | Body and callers printed; URI origin and file-write route unresolved. |
| 34 | `FileSystemFacadeImpl.write(byte[],Uri)V` | OPEN | Body and callers printed; URI origin and file-write route unresolved. |
| 35 | `FsModuleResolverImpl.<init>(Context)V` | OPEN | Constructor and uses printed; complete dependency injection/construction route unresolved. |
| 36 | `FsModuleResolverImpl.resolveFsByUri(Uri)FsModule` | OPEN | Resolver body and callers printed; full caller URI route unresolved. |
| 37 | `SafFileSystem.<clinit>()V` | OPEN | SAF class/static setup printed; initialization route from app entry not traced. |
| 38 | `SafFileSystem.<init>(Context)V` | OPEN | Constructor and `getInstance` context printed; complete application route unresolved. |
| 39 | `SafFileSystem.delete(Uri)boolean` | OPEN | Body and callers printed; URI-origin, permission, and caller route unresolved. |
| 40 | `SafFileSystem.exists(Uri)boolean` | OPEN | Body and callers printed; URI-origin and caller route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
