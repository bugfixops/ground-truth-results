# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 95 part (DetailTorrentTrackersFragment + TrackerItem + TrackerListAdapter head). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b095_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Authoritative batch source: clone
# graphs/LibreTorrent/scratch/merge-ready/batch95-merge-ready.md (verified identical to the
# helper input copy; batches 93-97 are not A1-affected, so the clone copy is current).
# Rows covered by an existing graph_def edge are named in the .md Dependencies
# line instead of being re-edged here.
# SUPPRESS: recomputed from auto_calls.json + javap for this batch (see REPORT.md).
# No auto CALL edge runs from a REACHABLE method in batches 93-97 into an
# UNREACHABLE method owned by this batch, so no SUPPRESS entry applies here.

e('DetailTorrentTrackersFragment$2.onSelectionChanged', 'DetailTorrentTrackersFragment.setActionModeTitle', 'CALL', 'Selection change updates the action-mode title', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:195; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:290-293')
e('DetailTorrentTrackersFragment.onViewCreated', 'DetailTorrentTrackersFragment$1.<init>', 'CALL', 'View creation instantiates the anonymous DefaultItemAnimator', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:166-171')
e('DetailTorrentTrackersFragment.onViewCreated', 'DetailTorrentTrackersFragment$1.canReuseUpdatedViewHolder', 'FRAMEWORK', 'RecyclerView animator dispatch for the animator set on the tracker list', cls='non_standard', via='RecyclerView ItemAnimator dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:166-176; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:168-170')
e('DetailTorrentTrackersFragment.onViewCreated', 'DetailTorrentTrackersFragment$2.<init>', 'CALL', 'View creation registers the anonymous SelectionObserver', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:187; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:187-220')
e('DetailTorrentTrackersFragment.<init>', 'DetailTorrentTrackersFragment$3.<init>', 'CALL', 'Fragment construction initialises the actionModeCallback field', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:93-100; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:295')
e('TrackerListAdapter$1.areItemsTheSame', 'TrackerItem.equals', 'CALL', 'DiffUtil identity check compares tracker items', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:125-130; SRC ui/detailtorrent/pages/trackers/TrackerItem.java:45-53')
e('TrackerListAdapter$1.areContentsTheSame', 'TrackerItem.equalsContent', 'CALL', 'DiffUtil contents check compares tracker item contents', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:118-123; SRC ui/detailtorrent/pages/trackers/TrackerItem.java:39-43')
e('TrackerListAdapter.onBindViewHolder', 'TrackerItem.hashCode', 'FRAMEWORK', 'SelectionTracker isSelected key-hash dispatch on bind', cls='non_standard', via='SelectionTracker isSelected key-hash dispatch', evidence='INFERRED SelectionTracker key-hash dispatch; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:82-92; SRC ui/detailtorrent/pages/trackers/TrackerItem.java:34-37')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter.<clinit>', 'FRAMEWORK', 'First adapter construction initialises the adapter class', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:160; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:54')
e('DetailTorrentTrackersFragment.onViewCreated', 'TrackerListAdapter.<init>', 'CALL', 'Trackers fragment builds its adapter', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:160; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:58-61')
e('TrackerListAdapter$KeyProvider.getKey', 'TrackerListAdapter.getItemKey', 'CALL', 'KeyProvider delegates to the adapter Selectable method', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:239-242; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:101-108')
e('TrackerListAdapter$KeyProvider.getPosition', 'TrackerListAdapter.getItemPosition', 'CALL', 'KeyProvider delegates to the adapter Selectable method', cls='explicit', evidence='SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:245-248; SRC ui/detailtorrent/pages/trackers/TrackerListAdapter.java:110-113')
e('DetailTorrentTrackersFragment.onStop', 'DetailTorrentTrackersFragment.onDetach', 'LIFECYCLE', 'Fragment detaches after stop', cls='non_standard', via='Android lifecycle sequence', evidence='INFERRED lifecycle sequence; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:129-135; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:120-127')
e('DetailTorrentTrackersFragment.onStart', 'DetailTorrentTrackersFragment.onResume', 'LIFECYCLE', 'Fragment resumes after start', cls='non_standard', via='Android lifecycle sequence', evidence='INFERRED lifecycle sequence; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:137-144; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:250-256')
e('DetailTorrentTrackersFragment.onViewCreated', 'DetailTorrentTrackersFragment.onSaveInstanceState', 'LIFECYCLE', 'Fragment saves its instance state after view creation', cls='non_standard', via='Android lifecycle sequence', evidence='INFERRED lifecycle sequence; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:146-229; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:231-239')
e('DetailTorrentTrackersFragment.onResume', 'DetailTorrentTrackersFragment.onStop', 'LIFECYCLE', 'Fragment stops after resume', cls='non_standard', via='Android lifecycle sequence', evidence='INFERRED lifecycle sequence; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:250-256; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:129-135')
e('DetailTorrentTrackersFragment.onViewCreated', 'DetailTorrentTrackersFragment.onViewStateRestored', 'LIFECYCLE', 'Fragment restores its view state after view creation', cls='non_standard', via='Android lifecycle sequence', evidence='INFERRED lifecycle sequence; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:146-229; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:241-248')

# No UNREACHABLE rows in this batch; nothing to list here.
UNREACHABLE.update({})

SUPPRESS.update(set())
