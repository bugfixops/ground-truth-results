# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 85 part (CreateTorrentViewModel tail, ColorView, EmptyRecyclerView, ExpansionHeader head). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b085_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

e('CreateTorrentViewModel.makeBuilder', 'CreateTorrentViewModel.getPieceSizeByIndex', 'CALL', 'Torrent builder reads the piece size for the index', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:177-209; SRC ui/createtorrent/CreateTorrentViewModel.java:333-335')
e('CreateTorrentDialog.lambda$initAlertDialog$7', 'CreateTorrentViewModel.getState', 'CALL', 'Build-state observer setup reads the state LiveData', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:291-322; SRC ui/createtorrent/CreateTorrentViewModel.java:126-129')
e('CreateTorrentViewModel.makeBuilder', 'CreateTorrentViewModel.getTorrentVersionByIndex', 'CALL', 'Torrent builder reads the torrent version for the index', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:177-209; SRC ui/createtorrent/CreateTorrentViewModel.java:338-351')
e('CreateTorrentViewModel.lambda$downloadTorrent$4', 'CreateTorrentViewModel.lambda$downloadTorrent$3', 'CALL', 'Outer create lambda subscribes the engine-running lambda', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:352-388')
e('CreateTorrentViewModel.downloadTorrent', 'CreateTorrentViewModel.lambda$downloadTorrent$4', 'CALL', 'Download creates the completable that adds the torrent', cls='non_standard', via='Rx Completable.create dispatch', evidence='INFERRED Rx dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:352-388')
e('CreateTorrentViewModel.makeBuilder', 'CreateTorrentViewModel.lambda$makeBuilder$2', 'CALL', 'Torrent builder passes its file-name filter to the builder', cls='non_standard', via='TorrentBuilder file-filter dispatch during build', evidence='INFERRED library dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:177-209')
e('CreateTorrentViewModel.<init>', 'CreateTorrentViewModel.lambda$new$0', 'CALL', 'ViewModel constructor filters for engine start need', cls='non_standard', via='Rx filter dispatch', evidence='INFERRED Rx dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:101-116')
e('CreateTorrentViewModel.<init>', 'CreateTorrentViewModel.lambda$new$1', 'CALL', 'ViewModel constructor subscribes engine start', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:101-116')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.makeBuilder', 'CALL', 'Build builds its torrent builder', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:151-176; SRC ui/createtorrent/CreateTorrentViewModel.java:177-209')
e('CreateTorrentViewModel.makeBuilder', 'CreateTorrentViewModel.makeCreator', 'CALL', 'Torrent builder reads the creator string', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:177-209; SRC ui/createtorrent/CreateTorrentViewModel.java:252-262')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.makePercentProgress', 'CALL', 'Build subscribes progress updates', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:151-176; SRC ui/createtorrent/CreateTorrentViewModel.java:242-245')
e('CreateTorrentViewModel.getAndValidateTrackers', 'CreateTorrentViewModel.normalizeAndValidateUrl', 'CALL', 'Tracker validation normalizes each url', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:264-279; SRC ui/createtorrent/CreateTorrentViewModel.java:306-321')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.onBuildError', 'CALL', 'Build reports a builder exception', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:151-176; SRC ui/createtorrent/CreateTorrentViewModel.java:228-240')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.onBuildSuccess', 'CALL', 'Build subscribes the success handler', cls='non_standard', via='Rx subscribe dispatch', evidence='INFERRED Rx dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:151-176; SRC ui/createtorrent/CreateTorrentViewModel.java:211-226')
e('CreateTorrentDialog.onStop', 'CreateTorrentViewModel.onCleared', 'CALL', 'Host destroy clears the ViewModel', cls='non_standard', via='ViewModel lifecycle dispatch when the host is destroyed', evidence='INFERRED framework dispatch; SRC ui/createtorrent/CreateTorrentDialog.java:125-131; SRC ui/createtorrent/CreateTorrentViewModel.java:118-124')
e('CreateTorrentViewModel.buildTorrent', 'CreateTorrentViewModel.resetPercentProgress', 'CALL', 'Build resets the percent progress', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:151-176; SRC ui/createtorrent/CreateTorrentViewModel.java:247-250')
e('CreateTorrentDialog$3.onItemSelected', 'CreateTorrentViewModel.setPiecesSizeIndex', 'CALL', 'Piece-size spinner selection sets the ViewModel index', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:228-234; SRC ui/createtorrent/CreateTorrentViewModel.java:136-142')
e('CreateTorrentDialog$4.onItemSelected', 'CreateTorrentViewModel.setTorrentVersionIndex', 'CALL', 'Torrent-version spinner selection sets the ViewModel index', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentDialog.java:242-248; SRC ui/createtorrent/CreateTorrentViewModel.java:144-150')
e('CreateTorrentViewModel.<init>', 'CreateTorrentViewModel$1.<init>', 'CALL', 'ViewModel field initializer constructs the seed-path callback', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:391-404; SRC ui/createtorrent/CreateTorrentViewModel.java:101-116')
e('CreateTorrentViewModel.<init>', 'CreateTorrentViewModel$1.onPropertyChanged', 'CALL', 'ViewModel constructor registers the seed-path callback', cls='non_standard', via='Data-binding Observable callback dispatch', evidence='INFERRED databinding dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:101-116; SRC ui/createtorrent/CreateTorrentViewModel.java:391-404')
e('CreateTorrentViewModel.<init>', 'CreateTorrentViewModel$BuildState.<init>', 'CALL', 'ViewModel constructor posts the initial build state', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:101-116; SRC ui/createtorrent/CreateTorrentViewModel.java:74-78')
e('CreateTorrentViewModel.<init>', 'CreateTorrentViewModel$BuildState$Status.<clinit>', 'CALL', 'First build-state use initializes the status enum', cls='non_standard', via='JVM enum class-load dispatch', evidence='INFERRED class-load dispatch; SRC ui/createtorrent/CreateTorrentViewModel.java:101-116; SRC ui/createtorrent/CreateTorrentViewModel.java:69')
e('CreateTorrentViewModel.getAndValidateTrackers', 'CreateTorrentViewModel$InvalidTrackerException.<init>', 'CALL', 'Tracker validation throws on an invalid tracker url', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:264-279; SRC ui/createtorrent/CreateTorrentViewModel.java:85-89')
e('CreateTorrentViewModel.getAndValidateWebSeeds', 'CreateTorrentViewModel$InvalidWebSeedException.<init>', 'CALL', 'Web-seed validation throws on an invalid web-seed url', cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:281-295; SRC ui/createtorrent/CreateTorrentViewModel.java:95-99')
e('tag.TagsAdapter.onCreateViewHolder', 'ColorView.<init>', 'CALL', 'Tag list inflation constructs the color view', cls='non_standard', via='LayoutInflater 2-arg constructor dispatch', evidence='INFERRED inflater dispatch; SRC ui/tag/TagsAdapter.java:46-56; SRC ui/customviews/ColorView.java:43-75')
e('ColorView.<init>', 'ColorView.onDraw', 'CALL', 'Inflated color view draws its circles', cls='non_standard', via='Framework View draw dispatch after inflation', evidence='INFERRED framework dispatch; SRC ui/customviews/ColorView.java:43-75; SRC ui/customviews/ColorView.java:84-91')
e('ColorView.<init>', 'ColorView.onSizeChanged', 'CALL', 'Inflated color view receives its size', cls='non_standard', via='Framework View layout dispatch after inflation', evidence='INFERRED framework dispatch; SRC ui/customviews/ColorView.java:43-75; SRC ui/customviews/ColorView.java:76-81')
e('tag.TagsAdapter$ViewHolder.bind', 'ColorView.setColor', 'CALL', 'Tag binding paints the tag color', cls='explicit', evidence='SRC ui/tag/TagsAdapter.java:97-106; SRC ui/customviews/ColorView.java:95-99')
e('MainFragment.onCreateView', 'EmptyRecyclerView.<init>(Context,AttributeSet)', 'CALL', 'Main layout inflation constructs the torrent list view', cls='non_standard', via='LayoutInflater 2-arg constructor dispatch', evidence='INFERRED inflater dispatch; SRC ui/main/MainFragment.java:115-122; SRC ui/customviews/EmptyRecyclerView.java:59-61')
e('EmptyRecyclerView.setAdapter', 'EmptyRecyclerView.checkEmpty', 'CALL', 'Adapter set refreshes the empty view', cls='explicit', evidence='SRC ui/customviews/EmptyRecyclerView.java:80-92; SRC ui/customviews/EmptyRecyclerView.java:69-78')
e('MainFragment.onViewCreated', 'EmptyRecyclerView.setAdapter', 'CALL', 'Main fragment sets the torrent list adapter', cls='explicit', evidence='SRC ui/main/MainFragment.java:125-167; SRC ui/customviews/EmptyRecyclerView.java:80-92')
e('MainFragment.onViewCreated', 'EmptyRecyclerView.setEmptyView', 'CALL', 'Main fragment sets the torrent list empty view', cls='explicit', evidence='SRC ui/main/MainFragment.java:125-167; SRC ui/customviews/EmptyRecyclerView.java:94-97')
e('EmptyRecyclerView.<init>(Context,AttributeSet)', 'EmptyRecyclerView$1.<init>', 'CALL', 'View field initializer constructs the adapter observer', cls='explicit', evidence='SRC ui/customviews/EmptyRecyclerView.java:33-52; SRC ui/customviews/EmptyRecyclerView.java:59-61')
e('EmptyRecyclerView.setAdapter', 'EmptyRecyclerView$1.onChanged', 'CALL', 'Adapter observer refreshes on data change', cls='non_standard', via='RecyclerView observer dispatch', evidence='INFERRED observer dispatch; SRC ui/customviews/EmptyRecyclerView.java:80-92; SRC ui/customviews/EmptyRecyclerView.java:36-38')
e('EmptyRecyclerView.setAdapter', 'EmptyRecyclerView$1.onItemRangeInserted', 'CALL', 'Adapter observer refreshes on item insert', cls='non_standard', via='RecyclerView observer dispatch', evidence='INFERRED observer dispatch; SRC ui/customviews/EmptyRecyclerView.java:80-92; SRC ui/customviews/EmptyRecyclerView.java:42-44')
e('EmptyRecyclerView.setAdapter', 'EmptyRecyclerView$1.onItemRangeRemoved', 'CALL', 'Adapter observer refreshes on item removal', cls='non_standard', via='RecyclerView observer dispatch', evidence='INFERRED observer dispatch; SRC ui/customviews/EmptyRecyclerView.java:80-92; SRC ui/customviews/EmptyRecyclerView.java:48-50')
e('DrawerExpandableAdapter.onCreateGroupViewHolder', 'ExpansionHeader.<init>(Context,AttributeSet)', 'CALL', 'Drawer group-header inflation constructs the header', cls='non_standard', via='LayoutInflater 2-arg constructor dispatch', evidence='INFERRED inflater dispatch; SRC ui/main/drawer/DrawerExpandableAdapter.java:74-81; SRC ui/customviews/ExpansionHeader.java:63-67')

# Three UNREACHABLE rows in this batch.
UNREACHABLE.update({
    'ColorView.getColor': ('no_trigger_in_app',
        'No caller on a ColorView receiver in the 252-file app tree; binding.color sites are setColor and setOnClickListener only, and both ColorView layouts have no data block.',
        'SRC ui/customviews/ColorView.java:102-104',
        'INFERRED'),
    'EmptyRecyclerView.<init>(Context,AttributeSet,int)': ('no_trigger_in_app',
        'LayoutInflater looks up only the 2-arg ctor; the 2-arg ctor calls super only, never this(...,int); saved 252-file grep found 0 constructions, 0 extends, 0 reflection lookups.',
        'SRC ui/customviews/EmptyRecyclerView.java:64-66',
        'INFERRED'),
    'ExpansionHeader.<init>(Context,AttributeSet,int)': ('no_trigger_in_app',
        'LayoutInflater looks up only the 2-arg ctor; the 2-arg ctor calls super only, never this(...,int); saved 252-file grep found 0 constructions, 0 extends, 0 reflection lookups.',
        'SRC ui/customviews/ExpansionHeader.java:70-74',
        'INFERRED'),
})

# No auto edge points at this batch's UNREACHABLE overloads: the
# overload-aware auto_calls recompute found zero calls into
# getColor or either 3-arg ctor, and no REACHABLE method in this
# group calls them in bytecode, so no SUPPRESS entries apply here.
SUPPRESS.update(set())
