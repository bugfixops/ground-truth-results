# LibreTorrent batch 55 helper report

Membership is taken exclusively from `handoff/LIBRETORRENT_BATCH_PLAN.tsv` where batch is 55. Exact count: 40.

Summary: 0 REACHABLE, 0 UNREACHABLE, 40 OPEN. Source-local implementation bodies and helper calls do not by themselves establish a full entry-to-method route. Methods are left OPEN rather than upgrading the plan's generator candidates without that route.

| Plan row | JVM method | Descriptor | Status | Reason |
|---:|---|---|---|---|
| 1 | `SafFileSystem.getDir` | `(Landroidx/documentfile/provider/DocumentFile;Ljava/lang/String;Z)Landroidx/documentfile/provider/DocumentFile;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 2 | `SafFileSystem.getFile(DocumentFile,String,boolean)` | `(Landroidx/documentfile/provider/DocumentFile;Ljava/lang/String;Z)Landroidx/documentfile/provider/DocumentFile;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 3 | `SafFileSystem.getFile(FakePath,boolean)` | `(Lorg/proninyaroslav/libretorrent/core/system/SafFileSystem$FakePath;Z)Landroidx/documentfile/provider/DocumentFile;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 4 | `SafFileSystem.getFileUri(Uri,String,boolean)` | `(Landroid/net/Uri;Ljava/lang/String;Z)Landroid/net/Uri;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 5 | `SafFileSystem.getFileUri(FakePath,boolean)` | `(Lorg/proninyaroslav/libretorrent/core/system/SafFileSystem$FakePath;Z)Landroid/net/Uri;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 6 | `SafFileSystem.getInstance` | `(Landroid/content/Context;)Lorg/proninyaroslav/libretorrent/core/system/SafFileSystem;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 7 | `SafFileSystem.getParentDirUri` | `(Landroid/net/Uri;)Landroid/net/Uri;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 8 | `SafFileSystem.isSafPath` | `(Landroid/net/Uri;)Z` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 9 | `SafFileSystem.makeSafRootDir` | `(Landroid/net/Uri;)Landroid/net/Uri;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 10 | `SafFileSystem.stat(Uri)` | `(Landroid/net/Uri;)Lorg/proninyaroslav/libretorrent/core/system/SafFileSystem$Stat;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 11 | `SafFileSystem.stat(DocumentFile)` | `(Landroidx/documentfile/provider/DocumentFile;)Lorg/proninyaroslav/libretorrent/core/system/SafFileSystem$Stat;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 12 | `SafFileSystem.statSafRoot` | `(Landroid/net/Uri;)Lorg/proninyaroslav/libretorrent/core/system/SafFileSystem$Stat;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 13 | `SafFileSystem$FakePath.<init>` | `(Landroid/net/Uri;Ljava/lang/String;)V` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 14 | `SafFileSystem$FakePath.makeRelativePathNodes` | `()[Ljava/lang/String;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 15 | `SafFileSystem$FakePath.normalizeRelativePath` | `(Ljava/lang/String;)Ljava/lang/String;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 16 | `SafFileSystem$FakePath.safRoot` | `()Landroid/net/Uri;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 17 | `SafFileSystem$FakePath.serialize` | `()Ljava/lang/String;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 18 | `SafFileSystem$FakePath.toString` | `()Ljava/lang/String;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 19 | `SafFileSystem$Stat.<init>` | `(Ljava/lang/String;ZJJ)V` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 20 | `SafFsModule.<init>` | `(Landroid/content/Context;)V` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 21 | `SafFsModule.delete` | `(Landroid/net/Uri;)Z` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 22 | `SafFsModule.fileExists` | `(Landroid/net/Uri;)Z` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 23 | `SafFsModule.getAvailableBytes` | `(Ljava/io/FileDescriptor;)J` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 24 | `SafFsModule.getDirAvailableBytes` | `(Landroid/net/Uri;)J` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 25 | `SafFsModule.getDirPath` | `(Landroid/net/Uri;)Ljava/lang/String;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 26 | `SafFsModule.getFilePath` | `(Landroid/net/Uri;)Ljava/lang/String;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 27 | `SafFsModule.getFileUri(Uri,String,boolean)` | `(Landroid/net/Uri;Ljava/lang/String;Z)Landroid/net/Uri;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 28 | `SafFsModule.getFileUri(String,Uri)` | `(Ljava/lang/String;Landroid/net/Uri;)Landroid/net/Uri;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 29 | `SafFsModule.getParentDirUri` | `(Landroid/net/Uri;)Landroid/net/Uri;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 30 | `SafFsModule.makeFileSystemPath` | `(Landroid/net/Uri;Ljava/lang/String;)Ljava/lang/String;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 31 | `SafFsModule.openFD` | `(Landroid/net/Uri;)Lorg/proninyaroslav/libretorrent/core/system/FileDescriptorWrapper;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 32 | `SystemFacadeHelper.getFileSystemFacade` | `(Landroid/content/Context;)Lorg/proninyaroslav/libretorrent/core/system/FileSystemFacade;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 33 | `SystemFacadeHelper.getSystemFacade` | `(Landroid/content/Context;)Lorg/proninyaroslav/libretorrent/core/system/SystemFacade;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 34 | `SystemFacadeImpl.<init>` | `(Landroid/content/Context;)V` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 35 | `SystemFacadeImpl.getActiveNetworkInfo` | `()Landroid/net/NetworkInfo;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 36 | `SystemFacadeImpl.getAppVersionName` | `()Ljava/lang/String;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 37 | `SystemFacadeImpl.getNetworkCapabilities` | `()Landroid/net/NetworkCapabilities;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 38 | `SystemFacadeImpl.isActiveNetworkMetered` | `()Z` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 39 | `NormalizeUrl.<clinit>` | `()V` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |
| 40 | `NormalizeUrl.doNormalize` | `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/urlnormalizer/NormalizeUrl$Options;)Ljava/lang/String;` | OPEN | Source implementation/local calls are visible, but complete hand-authored route from an app entry is not established in this bounded audit. |

## Evidence checked
- `SafFileSystem.java` defines the SAF operations and nested `FakePath` / `Stat` helpers; method bodies include tree/document provider operations and internal helper calls.
- `SafFsModule.java` delegates filesystem operations to `SafFileSystem.getInstance(appContext)`.
- `SystemFacadeHelper.java` lazily constructs `SystemFacadeImpl` and the filesystem facade.
- `SystemFacadeImpl.java` implements Android network/app-version queries.
- `NormalizeUrl.java` contains static URL normalization code.
- These source-local links do not establish complete app-entry routes for the listed methods. No UNREACHABLE claim is supported by this bounded evidence.

