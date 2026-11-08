# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 82 part (AddTorrentViewModel internals, DownloadableFileItem/Adapter, CreateTorrentActivity). Hand-written edges only.
# Each evidence string cites lines printed in
# helper/a3-g16/scratch/b082_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
# Rows whose route already exists in merger-tree graph_def.py are
# listed in the .md Dependencies line and are NOT repeated here.

e('AddTorrentViewModel.<init>', 'AddTorrentViewModel$DecodeState.<init>(Status)', 'CALL', 'Init creates the UNKNOWN decode state',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:142; SRC ui/addtorrent/AddTorrentViewModel.java:123-125')
e('AddTorrentViewModel$DecodeState.<init>(Status)', 'AddTorrentViewModel$DecodeState.<init>(Status,Throwable)', 'CALL', 'One-arg state constructor delegates to the two-arg constructor',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:124; SRC ui/addtorrent/AddTorrentViewModel.java:118-121')
e('AddTorrentViewModel.<init>', 'AddTorrentViewModel$Status.<clinit>', 'FRAMEWORK', 'First use of a Status constant runs the enum class initialisation',
  cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation; SRC ui/addtorrent/AddTorrentViewModel.java:103-112,142')
e('AddTorrentViewModel.startDecodeTask', 'AddTorrentViewModel$TorrentDecodeTask.<init>', 'CALL', 'Start-decode-task creates the decode task',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:198; SRC ui/addtorrent/AddTorrentViewModel.java:205-209')
e('AddTorrentViewModel.startDecodeTask', 'AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'FRAMEWORK', 'AsyncTask dispatch runs doInBackground after executeOnExecutor',
  cls='non_standard', via='AsyncTask framework dispatch', evidence='INFERRED AsyncTask dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:199; SRC ui/addtorrent/AddTorrentViewModel.java:217-279')
e('AddTorrentViewModel.startDecodeTask', 'AddTorrentViewModel$TorrentDecodeTask.onPostExecute', 'FRAMEWORK', 'AsyncTask dispatch runs onPostExecute after doInBackground',
  cls='non_standard', via='AsyncTask framework dispatch', evidence='INFERRED AsyncTask dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:199; SRC ui/addtorrent/AddTorrentViewModel.java:301-325')
e('AddTorrentViewModel.startDecodeTask', 'AddTorrentViewModel$TorrentDecodeTask.onPreExecute', 'FRAMEWORK', 'AsyncTask dispatch runs onPreExecute before doInBackground',
  cls='non_standard', via='AsyncTask framework dispatch', evidence='INFERRED AsyncTask dispatch; SRC ui/addtorrent/AddTorrentViewModel.java:199; SRC ui/addtorrent/AddTorrentViewModel.java:212-214')
e('AddTorrentViewModel$TorrentDecodeTask.doInBackground', 'AddTorrentViewModel$TorrentDecodeTask.readTorrentFile', 'CALL', 'Decode task reads the torrent file from its background work',
  cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:272; SRC ui/addtorrent/AddTorrentViewModel.java:281-298')
e('AddTorrentFilesFragment.lambda$subscribeAdapter$0', 'DownloadableFileItem.<clinit>', 'FRAMEWORK', 'First DownloadableFileItem use runs its class initialisation',
  cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation; SRC ui/addtorrent/AddTorrentFilesFragment.java:117; SRC ui/addtorrent/DownloadableFileItem.java:61-75')
e('AddTorrentFilesFragment.lambda$subscribeAdapter$0', 'DownloadableFileItem.<init>(BencodeFileTree)', 'CALL', 'Adapter subscription maps each child to a DownloadableFileItem',
  cls='non_standard', via='Rx map dispatch', evidence='INFERRED Rx dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:113-119; SRC ui/addtorrent/DownloadableFileItem.java:33-38')
e('DownloadableFileItem.<clinit>', 'DownloadableFileItem$1.<init>', 'CALL', 'Class initialiser creates the CREATOR instance',
  cls='explicit', evidence='SRC ui/addtorrent/DownloadableFileItem.java:61-62')
e('AddTorrentFilesFragment.onViewCreated', 'DownloadableFilesAdapter.<clinit>', 'FRAMEWORK', 'First adapter use runs its class initialisation',
  cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation; SRC ui/addtorrent/AddTorrentFilesFragment.java:139; SRC ui/addtorrent/DownloadableFilesAdapter.java:44')
e('AddTorrentFilesFragment.onViewCreated', 'DownloadableFilesAdapter.onCreateViewHolder', 'FRAMEWORK', 'RecyclerView creates view holders after setAdapter',
  cls='non_standard', via='RecyclerView dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:140; SRC ui/addtorrent/DownloadableFilesAdapter.java:57-65')
e('DownloadableFilesAdapter.<clinit>', 'DownloadableFilesAdapter$1.<init>', 'CALL', 'Class initialiser creates the diff callback',
  cls='explicit', evidence='SRC ui/addtorrent/DownloadableFilesAdapter.java:74-90')
e('AddTorrentFilesFragment.lambda$subscribeAdapter$1', 'DownloadableFilesAdapter$1.areContentsTheSame', 'CALL', 'Submit-list DiffUtil check compares old and new contents',
  cls='non_standard', via='DiffUtil dispatch on submitList', evidence='INFERRED DiffUtil dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:122; SRC ui/addtorrent/DownloadableFilesAdapter.java:50,77-81')
e('AddTorrentFilesFragment.lambda$subscribeAdapter$1', 'DownloadableFilesAdapter$1.areItemsTheSame', 'CALL', 'Submit-list DiffUtil check compares item identity',
  cls='non_standard', via='DiffUtil dispatch on submitList', evidence='INFERRED DiffUtil dispatch; SRC ui/addtorrent/AddTorrentFilesFragment.java:122; SRC ui/addtorrent/DownloadableFilesAdapter.java:50,84-88')
e('DownloadableFilesAdapter.onCreateViewHolder', 'DownloadableFilesAdapter$ViewHolder.<init>', 'CALL', 'View-holder creation constructs the holder',
  cls='explicit', evidence='SRC ui/addtorrent/DownloadableFilesAdapter.java:65; SRC ui/addtorrent/DownloadableFilesAdapter.java:95-99')
e('CreateTorrentActivity.onCreate', 'CreateTorrentDialog.<clinit>', 'FRAMEWORK', 'First dialog use runs its class initialisation',
  cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM class initialisation; SRC ui/createtorrent/CreateTorrentActivity.java:83-86; SRC ui/createtorrent/CreateTorrentDialog.java:71')

# UNREACHABLE rows in this batch (see REPORT.md for the SUPPRESS recompute).
UNREACHABLE.update({
    'DownloadableFileItem.<init>(Parcel)': ('no_trigger_in_app',
        'No site parcels or unparcels a DownloadableFileItem; the sole caller of the parcel constructor is its own CREATOR, which is never framework-dispatched without a parcel site.',
        'SRC ui/addtorrent/DownloadableFileItem.java:40-44,61-68; SRC ui/addtorrent/AddTorrentFilesFragment.java:117,122',
        'INFERRED'),
    'DownloadableFileItem.describeContents': ('framework_never_calls',
        'The framework calls describeContents only while parceling an instance, and no site parcels a DownloadableFileItem.',
        'SRC ui/addtorrent/DownloadableFileItem.java:47-51',
        'INFERRED'),
    'DownloadableFileItem.toString': ('no_trigger_in_app',
        'No printed caller, logging, or concatenation site uses a DownloadableFileItem as text; FilesFragment/Adapter use item.name/isFile field-by-field only.',
        'SRC ui/addtorrent/DownloadableFileItem.java:79-85; SRC ui/addtorrent/AddTorrentFilesFragment.java:183-192',
        'INFERRED'),
    'DownloadableFileItem.writeToParcel': ('no_trigger_in_app',
        'writeToParcel runs only when an instance is parceled, and no site parcels a DownloadableFileItem.',
        'SRC ui/addtorrent/DownloadableFileItem.java:53-59',
        'INFERRED'),
    'DownloadableFileItem$1.createFromParcel': ('no_trigger_in_app',
        'No unparcel site returns a DownloadableFileItem and no CREATOR reference exists outside the file.',
        'SRC ui/addtorrent/DownloadableFileItem.java:61-68',
        'INFERRED'),
    'DownloadableFileItem$1.newArray': ('no_trigger_in_app',
        'No parcel site and no array-extra site names this class anywhere in the tree.',
        'SRC ui/addtorrent/DownloadableFileItem.java:71-74',
        'INFERRED'),
})

# Own-batch UNREACHABLE methods, suppressed so bytecode auto edges
# cannot resurrect them (cf. b013 precedent). The only auto edge
# into one of them is from another UNREACHABLE method of this
# batch (createFromParcel -> parcel ctor); no REACHABLE method in
# this group calls any of them in bytecode (see REPORT.md).
SUPPRESS.update({
    'DownloadableFileItem.<init>(Parcel)',
    'DownloadableFileItem.describeContents',
    'DownloadableFileItem.toString',
    'DownloadableFileItem.writeToParcel',
    'DownloadableFileItem$1.createFromParcel',
    'DownloadableFileItem$1.newArray',
})
