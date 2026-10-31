# ---- resume batch 11 (rb_11) label part

# LayoutElementParcelable constructors - called from multiple places

# Main constructor with 11 parameters - called from LoadFilesListTask.createListParcelables
e('LoadFilesListTask.createListParcelables', 'LayoutElementParcelable.<init>(Context,String,String,String,String,long,boolean,String,boolean,boolean,OpenMode)', 'CALL',
  'createListParcelables constructs LayoutElementParcelable with file details',
  evidence='SRC LoadFilesListTask.java:247-250 LayoutElementParcelable layoutElement = new LayoutElementParcelable(c, baseFile.getName(), baseFile.getPath(), baseFile.getPermission(), baseFile.getLink(), size, longSize, false, baseFile.getDate() + "", baseFile.isDirectory(), showThumbs, baseFile.getMode())')

# hasSymlink - called from MainFragment.onItemClick and FileListSorter.compare
e('MainFragment.onItemClick', 'LayoutElementParcelable.hasSymlink', 'CALL',
  'onItemClick checks hasSymlink to determine correct path',
  evidence='SRC MainFragment.java:891 String path = !e.hasSymlink()? e.desc:e.symlink')

e('FileListSorter.compare', 'LayoutElementParcelable.hasSymlink', 'CALL',
  'compare checks hasSymlink to get correct file for comparison',
  evidence='SRC FileListSorter.java:51 if(!file1.hasSymlink()) { f1=new File(file1.getDesc()); }; FileListSorter.java:60 if(!file2.hasSymlink())')

# toString - may be called for logging/debugging but no direct app usage found
# Leaving it out since no printed call site

# LoadFilesListTask lambdas - all called from doInBackground

# lambda$doInBackground$0 - SFTP file iteration callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$0', 'CALL',
  'doInBackground SFTP case: HybridFile.forEachChildrenFile calls lambda for each file',
  evidence='SRC LoadFilesListTask.java:130-137 sftpHFile.forEachChildrenFile(c, false, file -> { if (!(dataUtils.isFileHidden(file.getPath()) || file.isHidden() && !showHiddenFiles)) { LayoutElementParcelable elem = createListParcelables(file); if (elem != null) { list.add(elem); } } })')

# lambda$doInBackground$1 - OTG file iteration callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$1', 'CALL',
  'doInBackground OTG case: listOtg calls lambda for each file found',
  evidence='SRC LoadFilesListTask.java:169-171 listOtg(path, file -> { LayoutElementParcelable elem = createListParcelables(file); if(elem != null) list.add(elem); })')

# lambda$doInBackground$2 - Cloud storage file iteration callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$2', 'CALL',
  'doInBackground cloud case: listCloud calls lambda for each cloud file',
  evidence='SRC LoadFilesListTask.java:183-185 listCloud(path, cloudStorage, openmode, file -> { LayoutElementParcelable elem = createListParcelables(file); if(elem != null) list.add(elem); })')

# lambda$doInBackground$3 - Default case mode callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$3', 'CALL',
  'doInBackground default case: RootHelper.getFiles calls mode lambda to set openmode',
  evidence='SRC LoadFilesListTask.java:197-198 RootHelper.getFiles(path, ma.getMainActivity().isRootExplorer(), showHiddenFiles, mode -> openmode = mode, file -> {...})')

# lambda$doInBackground$4 - Default case file callback
e('LoadFilesListTask.doInBackground', 'LoadFilesListTask.lambda$doInBackground$4', 'CALL',
  'doInBackground default case: RootHelper.getFiles calls file lambda for each file',
  evidence='SRC LoadFilesListTask.java:198-200 RootHelper.getFiles(..., mode -> openmode = mode, file -> { LayoutElementParcelable elem = createListParcelables(file); if(elem != null) list.add(elem); })')

# lambda$listDocs$5 - Documents sort comparator
e('LoadFilesListTask.listDocs', 'LoadFilesListTask.lambda$listDocs$5', 'CALL',
  'listDocs calls Collections.sort with lambda comparator to sort by date descending',
  evidence='SRC LoadFilesListTask.java:356 Collections.sort(docs, (lhs, rhs) -> -1 * Long.valueOf(lhs.date).compareTo(rhs.date))')

# lambda$listRecentFiles$6 - Recent files sort comparator
e('LoadFilesListTask.listRecentFiles', 'LoadFilesListTask.lambda$listRecentFiles$6', 'CALL',
  'listRecentFiles calls Collections.sort with lambda comparator to sort by date descending',
  evidence='SRC LoadFilesListTask.java:434 Collections.sort(recentFiles, (lhs, rhs) -> -1 * Long.valueOf(lhs.date).compareTo(rhs.date))')

# UNREACHABLE methods - Parcelable interface methods never called because app doesn't parcel LayoutElementParcelable
UNREACHABLE['LayoutElementParcelable.<init>(Parcel)'] = ('framework_never_calls', 'Parcelable constructor exists but app never parcels LayoutElementParcelable objects: grep -rn "putParcelable.*LayoutElement|writeParcelable.*LayoutElement" over app source shows no usage', 'SRC LayoutElementParcelable.java:149-167', 'SOURCE')

UNREACHABLE['LayoutElementParcelable.describeContents'] = ('framework_never_calls', 'Parcelable method exists but app never parcels LayoutElementParcelable objects: no Parcel.writeParcelable or Bundle.putParcelable usage found', 'SRC LayoutElementParcelable.java:168-171', 'SOURCE')

UNREACHABLE['LayoutElementParcelable.writeToParcel'] = ('framework_never_calls', 'Parcelable method exists but app never parcels LayoutElementParcelable objects: no Parcel.writeParcelable or Bundle.putParcelable usage found', 'SRC LayoutElementParcelable.java:174-187', 'SOURCE')

UNREACHABLE['LayoutElementParcelable.toString'] = ('no_trigger_in_app', 'Object.toString override exists but no explicit toString() calls or string concatenation of LayoutElementParcelable found in app code', 'SRC LayoutElementParcelable.java:144-146', 'SOURCE')
