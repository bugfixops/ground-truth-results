# ---- Helper batch_015 label part (2024-01-18)

# CompressedObjectParcelable - Parcelable data class for archive entries
e('CompressedExplorerFragment.onSaveInstanceState', 'CompressedObjectParcelable.writeToParcel', 'FRAMEWORK', 'Fragment state save triggers Parcelable write via Bundle.putParcelableArrayList',
  evidence='SRC CompressedExplorerFragment.java:228 calls putParcelableArrayList(KEY_ELEMENTS, elements); framework marshals via writeToParcel')

e('CompressedExplorerFragment.onRestoreInstanceState', 'CompressedObjectParcelable$1.createFromParcel', 'FRAMEWORK', 'Fragment state restore via Bundle.getParcelableArrayList triggers CREATOR.createFromParcel',
  evidence='SRC CompressedExplorerFragment.java:240 elements = savedInstanceState.getParcelableArrayList(KEY_ELEMENTS); framework unmarshals using CREATOR')

e('CompressedObjectParcelable$1.createFromParcel', 'CompressedObjectParcelable.<init>', 'CALL', 'CREATOR.createFromParcel calls private Parcel constructor',
  evidence='SRC CompressedObjectParcelable.java:92-93 createFromParcel returns new CompressedObjectParcelable(in)')

e('CompressedHelperTask.doInBackground', 'CompressedObjectParcelable$Sorter.<init>', 'CALL', 'Sort task results before returning',
  evidence='SRC CompressedHelperTask.java:56 Collections.sort(elements, new CompressedObjectParcelable.Sorter())')

e('CompressedObjectParcelable$Sorter.<init>', 'CompressedObjectParcelable$Sorter.compare', 'FRAMEWORK', 'Collections.sort calls Comparator.compare',
  evidence='SRC CompressedHelperTask.java:56 Collections.sort triggers compare via Comparator interface')

# Archive entry constructors called from all HelperTask subclasses
e('ZipHelperTask.addElements', 'CompressedObjectParcelable.<init>', 'CALL', 'Zip archive listing creates entry objects',
  evidence='SRC ZipHelperTask.java:79 wholelist.add(new CompressedObjectParcelable(entry.getFileName(), entry.getLastModFileTime(), entry.getUncompressedSize(), entry.isDirectory()))')

e('RarHelperTask.addElements', 'CompressedObjectParcelable.<init>', 'CALL', 'RAR archive listing creates entry objects',
  evidence='SRC RarHelperTask.java:76 elements.add(new CompressedObjectParcelable(RarDecompressor.convertName(rarArchive), 0, rarArchive.getDataSize(), rarArchive.isDirectory()))')

e('TarHelperTask.addElements', 'CompressedObjectParcelable.<init>', 'CALL', 'TAR archive listing creates entry objects',
  evidence='SRC TarHelperTask.java:74 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('GzipHelperTask.addElements', 'CompressedObjectParcelable.<init>', 'CALL', 'Gzipped TAR listing creates entry objects',
  evidence='SRC GzipHelperTask.java:81 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('Bzip2HelperTask.addElements', 'CompressedObjectParcelable.<init>', 'CALL', 'Bzipped TAR listing creates entry objects',
  evidence='SRC Bzip2HelperTask.java:69 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('XzHelperTask.addElements', 'CompressedObjectParcelable.<init>', 'CALL', 'XZ TAR listing creates entry objects',
  evidence='SRC XzHelperTask.java:69 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('LzmaHelperTask.addElements', 'CompressedObjectParcelable.<init>', 'CALL', 'LZMA TAR listing creates entry objects',
  evidence='SRC LzmaHelperTask.java:69 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('SevenZipHelperTask.addElements', 'CompressedObjectParcelable.<init>', 'CALL', '7zip listing creates entry objects',
  evidence='SRC SevenZipHelperTask.java:79 elements.add(new CompressedObjectParcelable(entry.getName(), ...))')

e('CompressedHelperTask.doInBackground', 'CompressedObjectParcelable.<init>', 'CALL', 'Creates go-back item when navigating archive subdirectories',
  evidence='SRC CompressedHelperTask.java:52 if (createBackItem) elements.add(0, new CompressedObjectParcelable())')

e('CompressedObjectParcelable.<init>', 'CompressedObjectParcelable.getNameForPath', 'CALL', 'Constructor extracts filename from path',
  evidence='SRC CompressedObjectParcelable.java:49 this.name = getNameForPath(path)')

e('CompressedObjectParcelable.<init>', 'CompressedObjectParcelable.describeContents', 'FRAMEWORK', 'Parcelable interface may call describeContents',
  evidence='SRC CompressedObjectParcelable.java:47 constructor path; framework Parcelable protocol')

# CompressedItemViewHolder - RecyclerView ViewHolder for archive entry list
e('CompressedExplorerAdapter.onCreateViewHolder', 'CompressedItemViewHolder.<init>', 'CALL', 'Adapter creates ViewHolder instances',
  evidence='SRC CompressedExplorerAdapter.java:176 return new CompressedItemViewHolder(v); and line 179 CompressedItemViewHolder vh = new CompressedItemViewHolder(v)')

# CompressedHelperTask - AsyncTask base for archive listing
e('ZipDecompressor.changePath', 'CompressedHelperTask.<init>', 'CALL', 'Zip decompressor creates listing task',
  evidence='SRC ZipDecompressor.java:44 return new ZipHelperTask(context, filePath, path, addGoBackItem, onFinish); ZipHelperTask extends CompressedHelperTask')

e('RarDecompressor.changePath', 'CompressedHelperTask.<init>', 'CALL', 'RAR decompressor creates listing task',
  evidence='SRC RarDecompressor.java:47 return new RarHelperTask(filePath, path, addGoBackItem, onFinish); RarHelperTask extends CompressedHelperTask')

e('TarDecompressor.changePath', 'CompressedHelperTask.<init>', 'CALL', 'TAR decompressor creates listing task',
  evidence='SRC TarDecompressor.java:43 return new TarHelperTask(filePath, path, addGoBackItem, onFinish); TarHelperTask extends CompressedHelperTask')

e('CompressedHelperTask.<init>', 'CompressedHelperTask.doInBackground', 'ASYNC', 'AsyncTask.execute calls doInBackground',
  evidence='SRC CompressedExplorerFragment.java:420 decompressor.changePath returns task.execute(); AsyncTask protocol')

e('CompressedHelperTask.doInBackground', 'CompressedHelperTask.onPostExecute', 'ASYNC', 'AsyncTask framework calls onPostExecute after doInBackground',
  evidence='SRC CompressedHelperTask.java:48-68 doInBackground returns result; AsyncTask protocol invokes onPostExecute')

# CompressedHelper - Factory for archive type detection and handler instantiation
e('CompressedExplorerFragment.onCreateView', 'CompressedHelper.getCompressorInstance', 'CALL', 'Fragment opens archive and gets decompressor',
  evidence='SRC CompressedExplorerFragment.java:215 decompressor = CompressedHelper.getCompressorInstance(getContext(), compressedFile)')

e('CompressedExplorerFragment.onRestoreInstanceState', 'CompressedHelper.getCompressorInstance', 'CALL', 'Fragment restore recreates decompressor',
  evidence='SRC CompressedExplorerFragment.java:243 decompressor = CompressedHelper.getCompressorInstance(getContext(), compressedFile)')

e('MainActivityHelper.tryOpeningAsArchive', 'CompressedHelper.getCompressorInstance', 'CALL', 'Try opening file as archive',
  evidence='SRC MainActivityHelper.java:528 Decompressor decompressor = CompressedHelper.getCompressorInstance(mainActivity, file)')

e('ExtractService.onStartCommand', 'CompressedHelper.getExtractorInstance', 'CALL', 'Extract service gets extractor for archive',
  evidence='SRC ExtractService.java:259 CompressedHelper.getExtractorInstance(extractService.getApplicationContext(), ...)')

e('ExtractService.onStartCommand', 'CompressedHelper.getFileName', 'CALL', 'Extract service determines output folder name',
  evidence='SRC ExtractService.java:242 String extractDirName = CompressedHelper.getFileName(f.getName())')

e('CompressedExplorerAdapter.onBindViewHolder', 'CompressedHelper.getFileName', 'CALL', 'Adapter extracts base filename for cache path',
  evidence='SRC CompressedExplorerAdapter.java:274 String fileName = CompressedHelper.getFileName(compressedExplorerFragment.compressedFile.getName())')

e('Icons.loadMimeIcon', 'CompressedHelper.isFileExtractable', 'CALL', 'Icon loading checks if file is archive',
  evidence='SRC Icons.java:204 if(CompressedHelper.isFileExtractable(path)) return R.drawable.ic_compressed_white_24dp')

e('GeneralDialogCreation.showExtractDialog', 'CompressedHelper.isFileExtractable', 'CALL', 'Dialog checks if file is extractable',
  evidence='SRC GeneralDialogCreation.java:941 if (!CompressedHelper.isFileExtractable(f.getPath()))')

e('FileUtils.openFile', 'CompressedHelper.isFileExtractable', 'CALL', 'File open handler checks for archive type',
  evidence='SRC FileUtils.java:754 } else if (defaultHandler && CompressedHelper.isFileExtractable(f.getPath()))')

e('CompressedHelper.getCompressorInstance', 'CompressedHelper.getExtension', 'CALL', 'Compressor factory gets file extension',
  evidence='SRC CompressedHelper.java:123 String type = getExtension(file.getPath())')

e('CompressedHelper.getExtractorInstance', 'CompressedHelper.getExtension', 'CALL', 'Extractor factory gets file extension',
  evidence='SRC CompressedHelper.java:88 String type = getExtension(file.getPath())')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.getExtension', 'CALL', 'Extractability check gets extension',
  evidence='SRC CompressedHelper.java:147 String type = getExtension(path)')

e('CompressedHelper.getFileName', 'CompressedHelper.getExtension', 'CALL', 'Filename extraction may check extension type',
  evidence='SRC CompressedHelper.java:158 compressedName = compressedName.toLowerCase(); followed by extension checks')

e('CompressedHelper.getExtension', 'CompressedHelper.isZip', 'CALL', 'Type detection checks if ZIP',
  evidence='SRC CompressedHelper.java:126 if (isZip(type)); isZip at lines 164-167')

e('CompressedHelper.getExtension', 'CompressedHelper.isRar', 'CALL', 'Type detection checks if RAR',
  evidence='SRC CompressedHelper.java:128 } else if (isRar(type)); isRar at lines 181-183')

e('CompressedHelper.getExtension', 'CompressedHelper.isTar', 'CALL', 'Type detection checks if TAR',
  evidence='SRC CompressedHelper.java:130 } else if(isTar(type)); isTar at lines 169-171')

e('CompressedHelper.getExtension', 'CompressedHelper.isGzippedTar', 'CALL', 'Type detection checks if gzipped TAR',
  evidence='SRC CompressedHelper.java:132 } else if(isGzippedTar(type)); isGzippedTar at lines 173-175')

e('CompressedHelper.getExtension', 'CompressedHelper.isBzippedTar', 'CALL', 'Type detection checks if bzipped TAR',
  evidence='SRC CompressedHelper.java:134 } else if(isBzippedTar(type)); isBzippedTar at lines 177-179')

e('CompressedHelper.getExtension', 'CompressedHelper.isXzippedTar', 'CALL', 'Type detection checks if XZ TAR',
  evidence='SRC CompressedHelper.java:136 } else if(isXzippedTar(type)); isXzippedTar at lines 189-191')

e('CompressedHelper.getExtension', 'CompressedHelper.isLzippedTar', 'CALL', 'Type detection checks if LZMA TAR',
  evidence='SRC CompressedHelper.java:138 } else if(isLzippedTar(type)); isLzippedTar at lines 193-195')

e('CompressedHelper.getExtension', 'CompressedHelper.is7zip', 'CALL', 'Type detection checks if 7zip',
  evidence='SRC CompressedHelper.java:140 } else if(is7zip(type)); is7zip at lines 185-187')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isZip', 'CALL', 'Extractability checks ZIP',
  evidence='SRC CompressedHelper.java:149 return isZip(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isTar', 'CALL', 'Extractability checks TAR',
  evidence='SRC CompressedHelper.java:149 ... || isTar(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isRar', 'CALL', 'Extractability checks RAR',
  evidence='SRC CompressedHelper.java:149 ... || isRar(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isGzippedTar', 'CALL', 'Extractability checks gzipped TAR',
  evidence='SRC CompressedHelper.java:149 ... || isGzippedTar(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.is7zip', 'CALL', 'Extractability checks 7zip',
  evidence='SRC CompressedHelper.java:149 ... || is7zip(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isBzippedTar', 'CALL', 'Extractability checks bzipped TAR',
  evidence='SRC CompressedHelper.java:149 ... || isBzippedTar(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isXzippedTar', 'CALL', 'Extractability checks XZ TAR',
  evidence='SRC CompressedHelper.java:149 ... || isXzippedTar(type) || ...')

e('CompressedHelper.isFileExtractable', 'CompressedHelper.isLzippedTar', 'CALL', 'Extractability checks LZMA TAR',
  evidence='SRC CompressedHelper.java:149 ... || isLzippedTar(type)')

# Extractor and decompressor paths call isEntryPathValid
e('TarExtractor.extract', 'CompressedHelper.isEntryPathValid', 'CALL', 'TAR extractor validates entry paths',
  evidence='SRC TarExtractor.java:60 if(CompressedHelper.isEntryPathValid(tarArchiveEntry.getName()))')

e('RarExtractor.extract', 'CompressedHelper.isEntryPathValid', 'CALL', 'RAR extractor validates entry paths',
  evidence='SRC RarExtractor.java:59 if(CompressedHelper.isEntryPathValid(header.getFileNameString()))')

e('GzipExtractor.extract', 'CompressedHelper.isEntryPathValid', 'CALL', 'Gzip extractor validates entry paths',
  evidence='SRC GzipExtractor.java:61 if(CompressedHelper.isEntryPathValid(tarArchiveEntry.getName()))')

e('ZipExtractor.extract', 'CompressedHelper.isEntryPathValid', 'CALL', 'Zip extractor validates entry paths',
  evidence='SRC ZipExtractor.java:67 if(CompressedHelper.isEntryPathValid(fileHeader.getFileName()))')

e('GzipHelperTask.addElements', 'CompressedHelper.isEntryPathValid', 'CALL', 'Gzip listing task validates entry paths',
  evidence='SRC GzipHelperTask.java:70 if (!CompressedHelper.isEntryPathValid(name))')

e('RarHelperTask.addElements', 'CompressedHelper.isEntryPathValid', 'CALL', 'RAR listing task validates entry paths',
  evidence='SRC RarHelperTask.java:68 if (!CompressedHelper.isEntryPathValid(name))')

e('ZipHelperTask.addElements', 'CompressedHelper.isEntryPathValid', 'CALL', 'Zip listing task validates entry paths',
  evidence='SRC ZipHelperTask.java:75 if (!CompressedHelper.isEntryPathValid(entry.getFileName()))')

e('TarHelperTask.addElements', 'CompressedHelper.isEntryPathValid', 'CALL', 'TAR listing task validates entry paths',
  evidence='SRC TarHelperTask.java:64 if (!CompressedHelper.isEntryPathValid(name))')

# UNREACHABLE entries
UNREACHABLE = {}
UNREACHABLE['CompressedObjectParcelable.<clinit>'] = ('framework_never_calls', 'No static fields needing initialization; CREATOR initialized inline', 'SRC CompressedObjectParcelable.java:35-43,89 class has no static initializer block; CREATOR field initialized at declaration', 'SOURCE')
UNREACHABLE['CompressedObjectParcelable.equals'] = ('no_trigger_in_app', 'Method defined but not called; instances not compared in app code', 'SRC CompressedObjectParcelable.java:146-154 defines equals; no call sites found in app', 'INFERRED')
UNREACHABLE['CompressedObjectParcelable$1.<init>'] = ('framework_never_calls', 'Anonymous CREATOR instantiated inline at field declaration only', 'SRC CompressedObjectParcelable.java:89-91 CREATOR = new Parcelable.Creator<>() initializes inline', 'SOURCE')
UNREACHABLE['CompressedObjectParcelable$1.newArray'] = ('framework_never_calls', 'Creator.newArray only for typed arrays; Bundle.getParcelableArrayList uses ArrayList', 'SRC CompressedExplorerFragment.java:240 getParcelableArrayList; framework does not call newArray for ArrayList', 'INFERRED')
UNREACHABLE['CompressedHelper.<clinit>'] = ('framework_never_calls', 'All static fields are inline String constants', 'SRC CompressedHelper.java:56-66 static final String constants initialized inline', 'SOURCE')
UNREACHABLE['CompressedHelper.<init>'] = ('no_trigger_in_app', 'Abstract class with all static methods; never instantiated', 'SRC CompressedHelper.java:53 public abstract class CompressedHelper', 'SOURCE')
