# Batch 4 follow-up route research

This follows the 20 OPEN entries in `scratch/batch_004.md`. It adds caller-path evidence only; it does not change `graph_def.py` or assign final labels. Commands and printed source excerpts are in `scratch/batch_004_routes_printed.txt`.

| Method | Route finding | Source evidence |
|---|---|---|
| `UriConverter.<init>()V` | No app constructor path found; remains OPEN because `AppDatabase.java:53` registers `UriConverter` with Room. Both converter methods are static, but generated Room behavior was not inspected. | `UriConverter.java:27-39`; `AppDatabase.java:53`; no `new UriConverter` occurrence in Java source. |
| `DefaultFsModule.getName(Uri)` | No route found. Resolver returns `defaultModule`, but no source call dispatches to `FsModule.getName`. | `FsModuleResolverImpl.java:35-49`; `rg` found no module `getName` caller. |
| `DefaultFsModule.lastModified(Uri)` | No route found: only potential app caller is facade dispatch; no caller into `FileSystemFacade.lastModified` appears in source. | `DefaultFsModule.java:113-118`; `FileSystemFacadeImpl.java:160-166`; exact `lastModified(` search output. |
| `FileSystemFacadeImpl.isStorageWritable()` | No route found. Its sole app caller is private `makeTorrentDataDir`, reachable only through private `getTorrentDataDir`, for which no caller exists. | `FileSystemFacadeImpl.java:172-178`; `TorrentRepositoryImpl.java:145-155,163-170`; exact call search. |
| `FileSystemFacadeImpl.isValidFatFilename(String)` | No route found; implementation and interface declaration only. | `FileSystemFacadeImpl.java:331-335`; exact call search. |
| `FileSystemFacadeImpl.lastModified(Uri)` | No entry-to-method route found; no source calls this facade method. Its downstream interface dispatch does not establish an entry. | `FileSystemFacadeImpl.java:160-166`; exact `lastModified(` results. |
| `SafFileSystem.delete(FakePath)` | No route found. `SafFsModule` calls `delete(Uri)`, a different overload. | `SafFileSystem.java:310-323`; `SafFsModule.java:83-89`. |
| `SafFileSystem.exists(FakePath)` | No route found. `SafFsModule` calls `exists(Uri)`, a different overload. | `SafFileSystem.java:329-366`; `SafFsModule.java:135-139`. |
| `SafFileSystem.mkdirs(FakePath)` | No app caller found. | `SafFileSystem.java:504-530`; whole Java source search for `FakePath` shows declaration only for this method. |
| `SafFileSystem.openFD(Uri,String)` | Only called by the two overloads below; neither outer overload has an app caller. | `SafFileSystem.java:382-422`; exact `openFD(` search. |
| `SafFileSystem.openFD(Uri,String,String)` | No app caller found. | `SafFileSystem.java:382-390`; exact overload search. |
| `SafFileSystem.openFD(FakePath,String)` | No app caller found. | `SafFileSystem.java:394-402`; exact overload search. |
| `SafFileSystem.stat(Uri,String)` | No caller found. `SafFsModule` calls the one-argument `stat(Uri)` overload. | `SafFileSystem.java:426-440,459-470`; `SafFsModule.java:45-52,141-148`. |
| `SafFileSystem.stat(FakePath)` | No app caller found. | `SafFileSystem.java:472-485`; whole Java source search for `FakePath` has no invocation. |
| `SafFileSystem$FakePath.deserialize(String)` | Declaration only in supplied app Java source. | `SafFileSystem.java:118-130`; exact `FakePath`/`deserialize` search. |
| `SafFileSystem$FakePath.isFakePath(String)` | Declaration only in supplied app Java source. | `SafFileSystem.java:157-160`; exact `FakePath` search. |
| `SafFileSystem$FakePath.relativePath()` | Declaration only; file code uses `makeRelativePathNodes()` instead. | `SafFileSystem.java:152-155`; exact `relativePath(` search. |
| `SafFsModule.getName(Uri)` | No route found. Resolver returns the module, but no facade or app code invokes this interface method. | `SafFsModule.java:45-52`; `FsModuleResolverImpl.java:35-49`; exact module dispatch search. |
| `SafFsModule.lastModified(Uri)` | No entry-to-method route found. The only dispatcher is `FileSystemFacadeImpl.lastModified`, for which no app caller exists. | `SafFsModule.java:141-148`; `FileSystemFacadeImpl.java:160-166`; exact `lastModified(` results. |

Result: Of the 19 OPEN entries in `batch_004.md`, 18 have no caller path in the supplied app Java source; the `UriConverter` constructor stays OPEN because its class is registered in Room metadata but no constructor path is present in source. These are route-search findings for integration review, not edits to the graph.
