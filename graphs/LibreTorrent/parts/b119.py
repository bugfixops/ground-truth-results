# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 119 part (SelectTagDialog, SelectTagViewModel, ui/tag TagItem,
# ui/tag TagsAdapter, TorrentTagsList). Hand-written edges only for rows not
# already covered by an existing graph_def edge; the remaining rows are
# listed in the .md Dependencies line with their graph_def edges.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b119_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.

# Dialog: key listener lambda forwards Back presses to onBackPressed.
e('SelectTagDialog.onResume', 'SelectTagDialog.lambda$onResume$0', 'CALL', 'Dialog key-listener lambda handles Back key presses', cls='non_standard', via='Dialog key-listener dispatch', evidence='INFERRED key dispatch; SRC ui/tag/SelectTagDialog.java:87-96; SRC ui/tag/SelectTagDialog.java:83-97')
# Dialog: host activity forwards its Back press to the dialog.
e('SelectTagActivity.onBackPressed', 'SelectTagDialog.onBackPressed', 'CALL', 'Host activity forwards Back press to the tag dialog', evidence='SRC ui/tag/SelectTagActivity.java:69-70; SRC ui/tag/SelectTagDialog.java:186-189')
# Dialog lifecycle: creation resumes the dialog.
e('SelectTagDialog.onCreateDialog', 'SelectTagDialog.onResume', 'LIFECYCLE', 'Resume tag dialog after creation', evidence='SRC ui/tag/SelectTagDialog.java:115-136; SRC ui/tag/SelectTagDialog.java:83-97')
# Dialog lifecycle: creation starts the dialog.
e('SelectTagDialog.onCreateDialog', 'SelectTagDialog.onStart', 'LIFECYCLE', 'Start tag dialog after creation', evidence='SRC ui/tag/SelectTagDialog.java:115-136; SRC ui/tag/SelectTagDialog.java:100-104')
# Dialog lifecycle: resume stops the dialog, disposing subscriptions.
e('SelectTagDialog.onResume', 'SelectTagDialog.onStop', 'LIFECYCLE', 'Stop tag dialog after resume, disposing subscriptions', evidence='SRC ui/tag/SelectTagDialog.java:83-97; SRC ui/tag/SelectTagDialog.java:107-111')
# ViewModel is obtained through ViewModelProvider, never constructed directly.
e('SelectTagDialog.onCreateDialog', 'SelectTagViewModel.<init>', 'CALL', 'ViewModelProvider creates the tag ViewModel', cls='non_standard', via='ViewModelProvider.get dispatch', evidence='INFERRED ViewModelProvider dispatch; SRC ui/tag/SelectTagDialog.java:121; SRC ui/tag/SelectTagViewModel.java:41-45')
# Rx filter method reference excludes already-selected tags.
e('SelectTagDialog.subscribeTags', 'SelectTagViewModel.filterExcludeTags', 'CALL', 'Tag stream filters out already-selected tags', cls='non_standard', via='Rx filter method-reference dispatch', evidence='INFERRED Rx dispatch; SRC ui/tag/SelectTagDialog.java:169-173; SRC ui/tag/SelectTagViewModel.java:58-60')
# Rx map method reference wraps each TagInfo in a TagItem.
e('SelectTagDialog.lambda$subscribeTags$4', 'tag.TagItem.<init>', 'CALL', 'Tag stream maps each TagInfo to a TagItem', cls='non_standard', via='Rx map method-reference dispatch', evidence='INFERRED Rx dispatch; SRC ui/tag/SelectTagDialog.java:169-173; SRC ui/tag/TagItem.java:30-32')
# DiffUtil content comparison delegates to TagItem.equals.
e('tag.TagsAdapter$1.areContentsTheSame', 'tag.TagItem.equals', 'CALL', 'DiffUtil content check compares TagItems by equality', evidence='SRC ui/tag/TagsAdapter.java:68-73; SRC ui/tag/TagItem.java:39-46')
# DiffUtil identity comparison delegates to TagItem.isSame.
e('tag.TagsAdapter$1.areItemsTheSame', 'tag.TagItem.isSame', 'CALL', 'DiffUtil identity check compares TagItems by id', evidence='SRC ui/tag/TagsAdapter.java:76-81; SRC ui/tag/TagItem.java:34-36')
# Adapter class initialisation on first use via new TagsAdapter (diffCallback field).
e('SelectTagDialog.onCreateDialog', 'tag.TagsAdapter.<clinit>', 'FRAMEWORK', 'Initialize diffCallback before first adapter use', evidence='SRC ui/tag/SelectTagDialog.java:130; SRC ui/tag/TagsAdapter.java:65-82')
# RecyclerView creates row holders through the dialog's adapter.
e('SelectTagDialog.onCreateDialog', 'tag.TagsAdapter.onBindViewHolder', 'CALL', 'RecyclerView binds visible tag rows through the adapter', cls='non_standard', via='RecyclerView holder dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/tag/SelectTagDialog.java:130,138-142; SRC ui/tag/TagsAdapter.java:58-63')
e('SelectTagDialog.onCreateDialog', 'tag.TagsAdapter.onCreateViewHolder', 'CALL', 'RecyclerView creates tag row holders through the adapter', cls='non_standard', via='RecyclerView holder dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/tag/SelectTagDialog.java:130,138-142; SRC ui/tag/TagsAdapter.java:46-55')
# Static diffCallback field initialiser instantiates the anonymous callback.
e('tag.TagsAdapter.<clinit>', 'tag.TagsAdapter$1.<init>', 'CALL', 'Static diffCallback initialiser instantiates the anonymous ItemCallback', evidence='SRC ui/tag/TagsAdapter.java:65-66')
# DiffUtil runs during submitList for content and identity checks.
e('SelectTagDialog.subscribeTags', 'tag.TagsAdapter$1.areContentsTheSame', 'CALL', 'ListAdapter submitList runs DiffUtil content checks', cls='non_standard', via='ListAdapter submitList DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/tag/SelectTagDialog.java:174; SRC ui/tag/TagsAdapter.java:68-73')
e('SelectTagDialog.subscribeTags', 'tag.TagsAdapter$1.areItemsTheSame', 'CALL', 'ListAdapter submitList runs DiffUtil identity checks', cls='non_standard', via='ListAdapter submitList DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/tag/SelectTagDialog.java:174; SRC ui/tag/TagsAdapter.java:76-81')
# Row holder construction from the inflated item binding.
e('tag.TagsAdapter.onCreateViewHolder', 'tag.TagsAdapter$ViewHolder.<init>', 'CALL', 'Row holder wraps the inflated item binding', evidence='SRC ui/tag/TagsAdapter.java:54; SRC ui/tag/TagsAdapter.java:92-96')
# Detail screen layout inflates the TorrentTagsList view (2-arg ctor).
e('DetailTorrentInfoFragment.onCreateView', 'TorrentTagsList.<init>(Context,AttributeSet)', 'CALL', 'Detail info layout inflates the tags list view', cls='non_standard', via='LayoutInflater inflation dispatch', evidence='INFERRED LayoutInflater dispatch; SRC ui/detailtorrent/pages/DetailTorrentInfoFragment.java:100,112')
# 2-arg constructor initialises the list with its add-tag button.
e('TorrentTagsList.<init>(Context,AttributeSet)', 'TorrentTagsList.init', 'CALL', 'Tags list constructor initialises the list', evidence='SRC ui/tag/TorrentTagsList.java:32; SRC ui/tag/TorrentTagsList.java:35-38')
# List initialisation builds the add-tag button.
e('TorrentTagsList.init', 'TorrentTagsList.buildAddTagButton', 'CALL', 'Tags list initialisation builds the add-tag button', evidence='SRC ui/tag/TorrentTagsList.java:36; SRC ui/tag/TorrentTagsList.java:78-87')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

# No REACHABLE method in this batch calls a proposed-UNREACHABLE method in
# bytecode (recomputed from auto_calls.json + javap; see REPORT.md), so no
# SUPPRESS entries apply. Note: tag.TagItem.hashCode (batch 11 row 7,
# UNREACHABLE) calls TagInfo.hashCode, but its caller is itself
# UNREACHABLE, so it is not a REACHABLE-to-UNREACHABLE pair.
SUPPRESS.update(set())
