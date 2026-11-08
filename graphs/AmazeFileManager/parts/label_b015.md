STATUS: RUNNING 21:40

| Method | Label | Kind | Reason | Source Lines |
|--------|-------|------|--------|--------------|
| CompressedObjectParcelable.<clinit> | UNREACHABLE | framework_never_calls | No static initializer block; CREATOR initialized inline | SRC CompressedObjectParcelable.java:35-43,89 |
| CompressedObjectParcelable.<init> ()V | REACHABLE | | Go-back item constructor | SRC CompressedHelperTask.java:52 |
| CompressedObjectParcelable.<init> (Parcel) | REACHABLE | | Parcel constructor called by CREATOR | SRC CompressedObjectParcelable.java:92-93,101-119 |
| CompressedObjectParcelable.<init> (String,long,long,boolean) | REACHABLE | | Main constructor for archive entries | SRC ZipHelperTask.java:79, RarHelperTask.java:76, TarHelperTask.java:74 |
| CompressedObjectParcelable.describeContents | REACHABLE | | Parcelable interface method | SRC CompressedObjectParcelable.java:76-78 |
| CompressedObjectParcelable.equals | UNREACHABLE | no_trigger_in_app | Not called in app code | SRC CompressedObjectParcelable.java:146-154 |
| CompressedObjectParcelable.getNameForPath | REACHABLE | | Extract filename from path | SRC CompressedObjectParcelable.java:49,138-144 |
| CompressedObjectParcelable.writeToParcel | REACHABLE | | Parcelable write via Bundle | SRC CompressedObjectParcelable.java:80-91; CompressedExplorerFragment.java:228 |
| CompressedObjectParcelable$1.<init> | UNREACHABLE | framework_never_calls | Anonymous class instantiated inline | SRC CompressedObjectParcelable.java:89-91 |
| CompressedObjectParcelable$1.createFromParcel | REACHABLE | | Framework unmarshals Parcelable | SRC CompressedObjectParcelable.java:92-94; CompressedExplorerFragment.java:240 |
| CompressedObjectParcelable$1.newArray | UNREACHABLE | framework_never_calls | getParcelableArrayList uses ArrayList | SRC CompressedExplorerFragment.java:240 |
| CompressedObjectParcelable$Sorter.<init> | REACHABLE | | Sorter instantiated for Collections.sort | SRC CompressedHelperTask.java:56 |
| CompressedObjectParcelable$Sorter.compare | REACHABLE | | Comparator.compare called by sort | SRC CompressedObjectParcelable.java:125-134; CompressedHelperTask.java:56 |
| CompressedItemViewHolder.<init> | REACHABLE | | ViewHolder created by adapter | SRC CompressedExplorerAdapter.java:176,179 |
| CompressedHelperTask.<init> | REACHABLE | | AsyncTask subclass constructor | SRC ZipDecompressor.java:44, RarDecompressor.java:47, TarDecompressor.java:43 |
| CompressedHelperTask.doInBackground | REACHABLE | | AsyncTask background execution | SRC CompressedHelperTask.java:48-61; CompressedExplorerFragment.java:420 |
| CompressedHelperTask.onPostExecute | REACHABLE | | AsyncTask result delivery | SRC CompressedHelperTask.java:64-67 |
| CompressedHelper.<clinit> | UNREACHABLE | framework_never_calls | Static String constants inline | SRC CompressedHelper.java:56-66 |
| CompressedHelper.<init> | UNREACHABLE | no_trigger_in_app | Abstract class never instantiated | SRC CompressedHelper.java:53 |
| CompressedHelper.getCompressorInstance | REACHABLE | | Factory for decompressor | SRC CompressedExplorerFragment.java:215,243; MainActivityHelper.java:528 |
| CompressedHelper.getExtension | REACHABLE | | Extract file extension | SRC CompressedHelper.java:88,123,147,197-199 |
| CompressedHelper.getExtractorInstance | REACHABLE | | Factory for extractor | SRC ExtractService.java:259; CompressedHelper.java:82-107 |
| CompressedHelper.getFileName | REACHABLE | | Remove archive extension | SRC ExtractService.java:242; CompressedExplorerAdapter.java:274; CompressedHelper.java:155-167 |
| CompressedHelper.is7zip | REACHABLE | | Check 7zip extension | SRC CompressedHelper.java:140,149,185-187 |
| CompressedHelper.isBzippedTar | REACHABLE | | Check bzip2 tar extension | SRC CompressedHelper.java:134,149,177-179 |
| CompressedHelper.isEntryPathValid | REACHABLE | | Validate entry path security | SRC TarExtractor.java:60, RarExtractor.java:59, GzipExtractor.java:61, ZipExtractor.java:67; CompressedHelper.java:170-172 |
| CompressedHelper.isFileExtractable | REACHABLE | | Check if archive type supported | SRC Icons.java:204; GeneralDialogCreation.java:941; FileUtils.java:754; CompressedHelper.java:145-149 |
| CompressedHelper.isGzippedTar | REACHABLE | | Check gzip tar extension | SRC CompressedHelper.java:132,149,173-175 |
| CompressedHelper.isLzippedTar | REACHABLE | | Check lzma tar extension | SRC CompressedHelper.java:138,149,193-195 |
| CompressedHelper.isRar | REACHABLE | | Check rar extension | SRC CompressedHelper.java:128,149,181-183 |
| CompressedHelper.isTar | REACHABLE | | Check tar extension | SRC CompressedHelper.java:130,149,169-171 |
| CompressedHelper.isXzippedTar | REACHABLE | | Check xz tar extension | SRC CompressedHelper.java:136,149,189-191 |
| CompressedHelper.isZip | REACHABLE | | Check zip/jar/apk extension | SRC CompressedHelper.java:126,149,164-167 |

STATUS: DONE 21:45
