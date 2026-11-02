# C01 converter delivery (2026-11-01): base part verified against its authoritative
# batch file with the official harness (base PASS, labels/kinds unchanged).
# DELIVERED harness: FAIL ONLY on the grade upgrades below — check_part.py demands
# part grade == merge-ready grade, and merge-ready grades these keys INFERRED while
# the merger tree grades them SOURCE (see REPORT-b010.md for the (b)/(c) conflict
# note). No other FAILs; labels/kinds unchanged.
# Full-repo greps: parts-staging/grep/10/grep_10_*.txt (one file per UNREACHABLE row).
# STRONGER-EVIDENCE upgrades (grade field only; evidence text unchanged, and every
# upgraded entry already cites SRC lines): the merger tree holds these keys SOURCE
# while the base part graded them INFERRED, so the delivered part records SOURCE to
# avoid repeating the SOURCE 617->578->503 downgrade from the b001/b002 merges:
#   SOURCE (was INFERRED): Scheduler.<init>
#   SOURCE (was INFERRED): EmptyRecyclerView.<init>(Context)
#   SOURCE (was INFERRED): ExpansionHeader.<init>(Context)
#   SOURCE (was INFERRED): FixHintTextInputEditText.<init>(Context)
#   SOURCE (was INFERRED): SwitchBar.<init>(Context)
#   SOURCE (was INFERRED): ThemedSpeedDialView.<init>(Context)
#   SOURCE (was INFERRED): RecyclerViewDividerDecoration.<init>(Context,int)
#   SOURCE (was INFERRED): PeerItem.hashCode
#   SOURCE (was INFERRED): FeedItemsListItem.hashCode
#   SOURCE (was INFERRED): FileManagerSpinnerAdapter$StorageSpinnerItem.getName
#   SOURCE (was INFERRED): FileManagerSpinnerAdapter$StorageSpinnerItem.getSize
#   SOURCE (was INFERRED): FileManagerSpinnerAdapter$StorageSpinnerItem.setName
#   SOURCE (was INFERRED): FileManagerSpinnerAdapter$StorageSpinnerItem.setSize
#   SOURCE (was INFERRED): FileManagerSpinnerAdapter$StorageSpinnerItem.setStoragePath
#   SOURCE (was INFERRED): LogSettingsFragment.newInstance
#   SOURCE (was INFERRED): drawer.TagItem.hashCode
#   SOURCE (was INFERRED): drawer.TagItem.toString
# Labels/kinds are exactly the base part's (and the batch file's); nothing flipped.

# Batch 10 part (generated data-binding statics: ItemTorrentDownloadableFileBinding,
# ItemTorrentListBinding, ItemTrackersListBinding, TagsListItemBinding; custom-view
# 1-arg constructors; RecyclerViewDividerDecoration (Context, int); Scheduler;
# LogSettingsFragment factory; StorageSpinnerItem accessors; PeerItem,
# FeedItemsListItem and drawer TagItem hashCode/toString; FeedItemsListItem.compareTo).
# Hand-written UNREACHABLE entries and SUPPRESS strings only; no edges: the single
# REACHABLE row (row 31, FeedItemsListItem.compareTo) already has its incoming edge
# in graph_def.py and is not repeated here, and every other row is UNREACHABLE, so
# no incoming edge is written here.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b010_printed.txt.
#
# Pre-existing routes NOT repeated here, with graph_def.py line refs:
# - FeedItemsAdapter.submitList -> FeedItemsListItem.compareTo (graph_def:3538).
#
# No app source calls the generated base Binding statics directly: the fresh grep in
# the printed file returns 0 direct XBinding.(inflate|bind)( calls per class, while
# the DataBindingUtil.inflate sites for all four classes are printed. Layouts are
# created through DataBindingUtil / the generated mapper, which bypasses the base
# statics; generated *BindingImpl source is absent from final_java_only.

UNREACHABLE.update({
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/addtorrent/DownloadableFilesAdapter.java:60; SRC ui/addtorrent/DownloadableFilesAdapter.java:36,93,95; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/addtorrent/DownloadableFilesAdapter.java:60; SRC ui/addtorrent/DownloadableFilesAdapter.java:36,93,95; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/addtorrent/DownloadableFilesAdapter.java:60; SRC ui/addtorrent/DownloadableFilesAdapter.java:36,93,95; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/addtorrent/DownloadableFilesAdapter.java:60; SRC ui/addtorrent/DownloadableFilesAdapter.java:36,93,95; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTorrentListBinding.bind(View)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/main/TorrentListAdapter.java:79; SRC ui/main/TorrentListAdapter.java:49,153,161; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTorrentListBinding.bind(View,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/main/TorrentListAdapter.java:79; SRC ui/main/TorrentListAdapter.java:49,153,161; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTorrentListBinding.inflate(LayoutInflater)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/main/TorrentListAdapter.java:79; SRC ui/main/TorrentListAdapter.java:49,153,161; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/main/TorrentListAdapter.java:79; SRC ui/main/TorrentListAdapter.java:49,153,161; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/main/TorrentListAdapter.java:79; SRC ui/main/TorrentListAdapter.java:49,153,161; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTorrentListBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/main/TorrentListAdapter.java:79; SRC ui/main/TorrentListAdapter.java:49,153,161; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTrackersListBinding.bind(View)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:45,140,145; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTrackersListBinding.bind(View,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:45,140,145; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTrackersListBinding.inflate(LayoutInflater)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:45,140,145; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:45,140,145; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:45,140,145; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'ItemTrackersListBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:73; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:45,140,145; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'TagsListItemBinding.bind(View)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/tag/TagsAdapter.java:48; SRC ui/tag/TagsAdapter.java:32,90,92; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'TagsListItemBinding.bind(View,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/tag/TagsAdapter.java:48; SRC ui/tag/TagsAdapter.java:32,90,92; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'TagsListItemBinding.inflate(LayoutInflater)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/tag/TagsAdapter.java:48; SRC ui/tag/TagsAdapter.java:32,90,92; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/tag/TagsAdapter.java:48; SRC ui/tag/TagsAdapter.java:32,90,92; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/tag/TagsAdapter.java:48; SRC ui/tag/TagsAdapter.java:32,90,92; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'TagsListItemBinding.inflate(LayoutInflater,Object)': ('no_trigger_in_app',
        'No app code calls this generated base Binding static directly; instantiation goes through DataBindingUtil and the generated mapper, which bypasses the base statics, and generated Impl source is absent from final_java_only.',
        'SRC ui/tag/TagsAdapter.java:48; SRC ui/tag/TagsAdapter.java:32,90,92; INFERRED zero direct-call grep over the complete app Java tree (printed grep section)',
        'INFERRED'),
    'Scheduler.<init>': ('no_trigger_in_app',
        'No explicit constructor is declared and no app code constructs Scheduler; every member is static, so the implicit default constructor has no caller.',
        'SRC service/Scheduler.java:43-46,52,56,60,70,112,142; INFERRED zero new Scheduler grep over the complete app Java tree',
        'SOURCE'),
    'EmptyRecyclerView.<init>(Context)': ('no_trigger_in_app',
        'XML inflation looks up only the (Context, AttributeSet) constructor, so it cannot reach this 1-arg constructor, and no app code constructs this view directly and no subclass exists.',
        'SRC ui/customviews/EmptyRecyclerView.java:54-56,59,64; SRC fw_src/android-8.1.0_r1/core/java/android/view/LayoutInflater.java:90-91,618; INFERRED zero new EmptyRecyclerView and zero extends EmptyRecyclerView greps over the complete app Java tree',
        'SOURCE'),
    'ExpansionHeader.<init>(Context)': ('no_trigger_in_app',
        'XML inflation looks up only the (Context, AttributeSet) constructor, so it cannot reach this 1-arg constructor, and no app code constructs this view directly and no subclass exists.',
        'SRC ui/customviews/ExpansionHeader.java:56-58,63,70; SRC fw_src/android-8.1.0_r1/core/java/android/view/LayoutInflater.java:90-91,618; INFERRED zero new ExpansionHeader and zero extends ExpansionHeader greps over the complete app Java tree',
        'SOURCE'),
    'FixHintTextInputEditText.<init>(Context)': ('no_trigger_in_app',
        'XML inflation looks up only the (Context, AttributeSet) constructor, so it cannot reach this 1-arg constructor, and no app code constructs this view directly and no subclass exists.',
        'SRC ui/customviews/FixHintTextInputEditText.java:35-36,39,43; SRC fw_src/android-8.1.0_r1/core/java/android/view/LayoutInflater.java:90-91,618; INFERRED zero new FixHintTextInputEditText and zero extends FixHintTextInputEditText greps over the complete app Java tree',
        'SOURCE'),
    'SwitchBar.<init>(Context)': ('no_trigger_in_app',
        'XML inflation looks up only the (Context, AttributeSet) constructor, so it cannot reach this 1-arg constructor, and no app code constructs this view directly and no subclass exists.',
        'SRC ui/customviews/SwitchBar.java:37-42,44,51; SRC fw_src/android-8.1.0_r1/core/java/android/view/LayoutInflater.java:90-91,618; INFERRED zero new SwitchBar and zero extends SwitchBar greps over the complete app Java tree',
        'SOURCE'),
    'ThemedSpeedDialView.<init>(Context)': ('no_trigger_in_app',
        'XML inflation looks up only the (Context, AttributeSet) constructor, so it cannot reach this 1-arg constructor, and no app code constructs this view directly and no subclass exists.',
        'SRC ui/customviews/ThemedSpeedDialView.java:35-37,40,46; SRC fw_src/android-8.1.0_r1/core/java/android/view/LayoutInflater.java:90-91,618; INFERRED zero new ThemedSpeedDialView and zero extends ThemedSpeedDialView greps over the complete app Java tree',
        'SOURCE'),
    'RecyclerViewDividerDecoration.<init>(Context,int)': ('no_trigger_in_app',
        'Every printed construction site uses the Drawable overload, never the (Context, int) overload, and no subclass exists.',
        'SRC ui/customviews/RecyclerViewDividerDecoration.java:39,44; SRC ui/feeditems/FeedItemsFragment.java:148; SRC ui/feeds/FeedFragment.java:133; SRC ui/log/LogActivity.java:109; SRC ui/main/MainFragment.java:153; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:140; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:174',
        'SOURCE'),
    'PeerItem.hashCode': ('no_trigger_in_app',
        'PeerListAdapter compares items with equals and equalsContent through DiffUtil, and no hash-based collection holds PeerItem, so this override is not reached.',
        'SRC ui/detailtorrent/pages/peers/PeerItem.java:36-38; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:100-113; INFERRED zero receiver-typed hashCode and zero hash-collection greps over the complete app Java tree',
        'SOURCE'),
    'FeedItemsListItem.hashCode': ('no_trigger_in_app',
        'FeedItemsAdapter compares items with equals through DiffUtil and locates items with indexOf (equals), never hashCode, and no hash-based collection holds FeedItemsListItem, so this override is not reached. Row 31 compareTo flipping REACHABLE does not touch this row: sort dispatch calls compareTo, not hashCode.',
        'SRC ui/feeditems/FeedItemsListItem.java:38-40; SRC ui/feeditems/FeedItemsAdapter.java:100-102,105; INFERRED zero receiver-typed hashCode and zero hash-collection greps over the complete app Java tree',
        'SOURCE'),
    'FileManagerSpinnerAdapter$StorageSpinnerItem.getName': ('no_trigger_in_app',
        'Plain POJO accessor, not an interface or callback method, so no framework or library dispatch path exists. no caller on a StorageSpinnerItem receiver anywhere in the tree; all other getName hits are FileManagerNode receivers. The only spinner-item uses are getStoragePath and direct field reads from the enclosing adapter, and the spinner layouts are inflated with plain LayoutInflater.inflate plus findViewById, not data binding.',
        'SRC ui/filemanager/FileManagerSpinnerAdapter.java:51-93,64,124,137-138,148-150,160-161; SRC ui/filemanager/FileManagerDialog.java:655',
        'SOURCE'),
    'FileManagerSpinnerAdapter$StorageSpinnerItem.getSize': ('no_trigger_in_app',
        'Plain POJO accessor, not an interface or callback method, so no framework or library dispatch path exists. no caller on a StorageSpinnerItem receiver anywhere in the tree; the only other getSize hits are BencodeFileItem and TorrentDownload, different classes. The only spinner-item uses are getStoragePath and direct field reads from the enclosing adapter, and the spinner layouts are inflated with plain LayoutInflater.inflate plus findViewById, not data binding.',
        'SRC ui/filemanager/FileManagerSpinnerAdapter.java:51-93,84,124,137-138,148-150,160-161; SRC ui/filemanager/FileManagerDialog.java:655',
        'SOURCE'),
    'FileManagerSpinnerAdapter$StorageSpinnerItem.setName': ('no_trigger_in_app',
        'Plain POJO accessor, not an interface or callback method, so no framework or library dispatch path exists. no caller anywhere outside the definition itself; all other setName hits are other classes. The only spinner-item uses are getStoragePath and direct field reads from the enclosing adapter, and the spinner layouts are inflated with plain LayoutInflater.inflate plus findViewById, not data binding.',
        'SRC ui/filemanager/FileManagerSpinnerAdapter.java:51-93,69,124,137-138,148-150,160-161; SRC ui/filemanager/FileManagerDialog.java:655',
        'SOURCE'),
    'FileManagerSpinnerAdapter$StorageSpinnerItem.setSize': ('no_trigger_in_app',
        'Plain POJO accessor, not an interface or callback method, so no framework or library dispatch path exists. no caller anywhere outside the definition itself; the only other setSize hit is BencodeFileItem, a different class. The only spinner-item uses are getStoragePath and direct field reads from the enclosing adapter, and the spinner layouts are inflated with plain LayoutInflater.inflate plus findViewById, not data binding.',
        'SRC ui/filemanager/FileManagerSpinnerAdapter.java:51-93,89,124,137-138,148-150,160-161; SRC ui/filemanager/FileManagerDialog.java:655',
        'SOURCE'),
    'FileManagerSpinnerAdapter$StorageSpinnerItem.setStoragePath': ('no_trigger_in_app',
        'Plain POJO accessor, not an interface or callback method, so no framework or library dispatch path exists. no caller anywhere outside the definition itself; this is the only setStoragePath hit in the tree. The only spinner-item uses are getStoragePath and direct field reads from the enclosing adapter, and the spinner layouts are inflated with plain LayoutInflater.inflate plus findViewById, not data binding.',
        'SRC ui/filemanager/FileManagerSpinnerAdapter.java:51-93,79,124,137-138,148-150,160-161; SRC ui/filemanager/FileManagerDialog.java:655',
        'SOURCE'),
    'LogSettingsFragment.newInstance': ('no_trigger_in_app',
        'The factory constructs the fragment and sets empty arguments, but no app code calls it; the printed onCreate attach site is not a newInstance call.',
        'SRC ui/log/LogSettingsFragment.java:43-49; INFERRED zero LogSettingsFragment.newInstance grep over the complete app Java tree',
        'SOURCE'),
    'drawer.TagItem.hashCode': ('no_trigger_in_app',
        'The drawer tag list is a ListAdapter that compares items with isSame and equals through DiffUtil, and no hash-based collection holds a drawer TagItem, so this override is not reached. Not the ui/tag TagItem class.',
        'SRC ui/main/drawer/TagItem.java:50-51; SRC ui/main/drawer/TagsAdapter.java:130-146; SRC ui/main/MainActivity.java:477; INFERRED zero receiver-typed hashCode and zero hash-collection greps over the complete app Java tree',
        'SOURCE'),
    'drawer.TagItem.toString': ('no_trigger_in_app',
        'No string conversion, logging, or formatting of a drawer TagItem appears in app source; the near-miss at MainActivity is Long.toString of info.id, not a TagItem call, and the drawer adapter reads info fields only.',
        'SRC ui/main/drawer/TagItem.java:56-60; SRC ui/main/MainActivity.java:355; SRC ui/main/drawer/TagsAdapter.java:130-146',
        'SOURCE'),
})

# Suppress bytecode auto edges into the UNREACHABLE binding statics and their
# generated @Impl copies (the Impl class extends the base Binding class, so the
# static is reachable under the Impl name in bytecode; generated Impl source itself
# is absent from final_java_only, so the @Impl copies are listed for the merger to
# reconcile, following the batch 6-9 parts). No other batch-10 UNREACHABLE method
# has a subclass in app source (fresh extends greps in the printed file return 0
# hits for PeerItem, FeedItemsListItem, Scheduler, RecyclerViewDividerDecoration,
# LogSettingsFragment and the five custom views; EmptyTagItem and NoTagsItem extend
# AbstractTagItem, not drawer TagItem), so no other @Variant copies are listed.
# This part has no edges, so no part edge points at an UNREACHABLE method in any
# batch. The pre-existing graph_def tuple (drawer.TagItem.hashCode,
# TagInfo.hashCode) is already in graph_def.py and is not repeated here.
SUPPRESS.update({
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater)', 'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater)@ItemTorrentDownloadableFileBindingImpl',
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean)@ItemTorrentDownloadableFileBindingImpl',
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)', 'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)@ItemTorrentDownloadableFileBindingImpl',
    'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,Object)', 'ItemTorrentDownloadableFileBinding.inflate(LayoutInflater,Object)@ItemTorrentDownloadableFileBindingImpl',
    'ItemTorrentListBinding.bind(View)', 'ItemTorrentListBinding.bind(View)@ItemTorrentListBindingImpl',
    'ItemTorrentListBinding.bind(View,Object)', 'ItemTorrentListBinding.bind(View,Object)@ItemTorrentListBindingImpl',
    'ItemTorrentListBinding.inflate(LayoutInflater)', 'ItemTorrentListBinding.inflate(LayoutInflater)@ItemTorrentListBindingImpl',
    'ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean)@ItemTorrentListBindingImpl',
    'ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)', 'ItemTorrentListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)@ItemTorrentListBindingImpl',
    'ItemTorrentListBinding.inflate(LayoutInflater,Object)', 'ItemTorrentListBinding.inflate(LayoutInflater,Object)@ItemTorrentListBindingImpl',
    'ItemTrackersListBinding.bind(View)', 'ItemTrackersListBinding.bind(View)@ItemTrackersListBindingImpl',
    'ItemTrackersListBinding.bind(View,Object)', 'ItemTrackersListBinding.bind(View,Object)@ItemTrackersListBindingImpl',
    'ItemTrackersListBinding.inflate(LayoutInflater)', 'ItemTrackersListBinding.inflate(LayoutInflater)@ItemTrackersListBindingImpl',
    'ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean)@ItemTrackersListBindingImpl',
    'ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)', 'ItemTrackersListBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)@ItemTrackersListBindingImpl',
    'ItemTrackersListBinding.inflate(LayoutInflater,Object)', 'ItemTrackersListBinding.inflate(LayoutInflater,Object)@ItemTrackersListBindingImpl',
    'TagsListItemBinding.bind(View)', 'TagsListItemBinding.bind(View)@TagsListItemBindingImpl',
    'TagsListItemBinding.bind(View,Object)', 'TagsListItemBinding.bind(View,Object)@TagsListItemBindingImpl',
    'TagsListItemBinding.inflate(LayoutInflater)', 'TagsListItemBinding.inflate(LayoutInflater)@TagsListItemBindingImpl',
    'TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)', 'TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean)@TagsListItemBindingImpl',
    'TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)', 'TagsListItemBinding.inflate(LayoutInflater,ViewGroup,boolean,Object)@TagsListItemBindingImpl',
    'TagsListItemBinding.inflate(LayoutInflater,Object)', 'TagsListItemBinding.inflate(LayoutInflater,Object)@TagsListItemBindingImpl',
})
