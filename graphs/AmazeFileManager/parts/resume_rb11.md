STATUS: RUNNING 18:58

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| LayoutElementParcelable.<init>(Context,String,String,String,String,long,boolean,String,boolean,boolean,OpenMode) | REACHABLE | | Called from LoadFilesListTask.createListParcelables and other methods | SRC LoadFilesListTask.java:247; MainFragment.java:1476,1486,1505,1527; HybridFile.java:1265,1269 |
| LayoutElementParcelable.<init>(Parcel) | UNREACHABLE | framework_never_calls | Parcelable constructor exists but app never parcels LayoutElementParcelable objects (not put into Bundles/Intents) | SRC LayoutElementParcelable.java:149-167 defines constructor; grep -rn "putParcelable.*LayoutElement\|writeParcelable.*LayoutElement" over app source shows no usage |
| LayoutElementParcelable.describeContents | UNREACHABLE | framework_never_calls | Parcelable method exists but app never parcels LayoutElementParcelable objects | SRC LayoutElementParcelable.java:168-171 implements method; grep shows no parcel usage |
| LayoutElementParcelable.hasSymlink | REACHABLE | | Called from MainFragment.onItemClick and FileListSorter.compare | SRC LayoutElementParcelable.java:139-141; MainFragment.java:891 !e.hasSymlink(); FileListSorter.java:51,60 file.hasSymlink() |
| LayoutElementParcelable.toString | UNREACHABLE | no_trigger_in_app | Object.toString override exists but no explicit toString() calls or string concatenation found | SRC LayoutElementParcelable.java:144-146 defines method; grep -rn "\.toString()" over app shows no calls on LayoutElementParcelable instances |
| LayoutElementParcelable.writeToParcel | UNREACHABLE | framework_never_calls | Parcelable method exists but app never parcels LayoutElementParcelable objects | SRC LayoutElementParcelable.java:174-187 implements method; grep shows no parcel usage |
| LoadFilesListTask.lambda$doInBackground$0 | REACHABLE | | Lambda in doInBackground SFTP case, called by HybridFile.forEachChildrenFile callback | SRC LoadFilesListTask.java:130-137 sftpHFile.forEachChildrenFile(c, false, file -> {...}) |
| LoadFilesListTask.lambda$doInBackground$1 | REACHABLE | | Lambda in doInBackground OTG case, called by listOtg callback | SRC LoadFilesListTask.java:169-171 listOtg(path, file -> {...}) |
| LoadFilesListTask.lambda$doInBackground$2 | REACHABLE | | Lambda in doInBackground cloud case, called by listCloud callback | SRC LoadFilesListTask.java:183-185 listCloud(path, cloudStorage, openmode, file -> {...}) |
| LoadFilesListTask.lambda$doInBackground$3 | REACHABLE | | First lambda in doInBackground default case for mode callback | SRC LoadFilesListTask.java:197-198 RootHelper.getFiles(path, ..., mode -> openmode = mode, ...) |
| LoadFilesListTask.lambda$doInBackground$4 | REACHABLE | | Second lambda in doInBackground default case for file callback | SRC LoadFilesListTask.java:198-200 RootHelper.getFiles(..., file -> {...}) |
| LoadFilesListTask.lambda$listDocs$5 | REACHABLE | | Lambda in listDocs for sorting documents by date | SRC LoadFilesListTask.java:356 Collections.sort(docs, (lhs, rhs) -> -1 * Long.valueOf(lhs.date).compareTo(rhs.date)) |
| LoadFilesListTask.lambda$listRecentFiles$6 | REACHABLE | | Lambda in listRecentFiles for sorting recent files by date | SRC LoadFilesListTask.java:434 Collections.sort(recentFiles, (lhs, rhs) -> -1 * Long.valueOf(lhs.date).compareTo(rhs.date)) |

STATUS: DONE 18:58
