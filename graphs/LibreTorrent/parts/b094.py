# Citation-form rework 2026-11-02: checked for core/services/data/libcore/packages citations; none present, no citation change; nothing else changed.
# Batch 94 part (Peers $1 / PeerItem / PeerListAdapter + Pieces fragment + PiecesView + Trackers head). Hand-written edges only.
# Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b094_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# Authoritative batch source: clone
# graphs/LibreTorrent/scratch/merge-ready/batch94-merge-ready.md (verified identical to the
# helper input copy; batches 93-97 are not A1-affected, so the clone copy is current).
# Rows covered by an existing graph_def edge are named in the .md Dependencies
# line instead of being re-edged here.
# SUPPRESS: callee-string entries for this batch's UNREACHABLE methods. They suppress
# the CHA interface-dispatch auto edges from every KeyProvider.getKey/getPosition into
# these Selectable methods (intra-group pairs from batches 93/96 plus the cross-group
# CHA pairs from TorrentListAdapter and FeedChannelListAdapter KeyProviders, all listed
# in REPORT.md for merger reconciliation). No other auto edge is suppressed.

e('DetailTorrentPeersFragment.onViewCreated', 'DetailTorrentPeersFragment$1.canReuseUpdatedViewHolder', 'FRAMEWORK', 'RecyclerView animator dispatch for the animator set on the peer list', cls='non_standard', via='RecyclerView ItemAnimator dispatch', evidence='INFERRED RecyclerView dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:132-138; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:134-136')
e('PeerListAdapter$1.areItemsTheSame', 'PeerItem.equals', 'CALL', 'DiffUtil identity check compares peer items', cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:110-115; SRC ui/detailtorrent/pages/peers/PeerItem.java:47-54')
e('PeerListAdapter$1.areContentsTheSame', 'PeerItem.equalsContent', 'CALL', 'DiffUtil contents check compares peer item contents', cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:103-108; SRC ui/detailtorrent/pages/peers/PeerItem.java:41-45')
e('DetailTorrentPeersFragment.onViewCreated', 'PeerListAdapter.<clinit>', 'FRAMEWORK', 'First adapter construction initialises the adapter class', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:126; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:45')
e('DetailTorrentPeersFragment.onViewCreated', 'PeerListAdapter.<init>', 'CALL', 'Peers fragment builds its adapter', cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:126; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:50-55')
e('DetailTorrentPeersFragment.onViewCreated', 'PeerListAdapter.onCreateViewHolder', 'FRAMEWORK', 'RecyclerView creates peer rows for the adapter set on the list', cls='non_standard', via='AndroidX RecyclerView adapter dispatch', evidence='INFERRED AndroidX RecyclerView adapter dispatch; SRC ui/detailtorrent/pages/peers/DetailTorrentPeersFragment.java:126,142; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:59-68')
e('PeerListAdapter.<clinit>', 'PeerListAdapter$1.<init>', 'FRAMEWORK', 'Static diffCallback field initialisation creates the anonymous DiffUtil callback', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:100-116')
e('PeerListAdapter.submitList', 'PeerListAdapter$1.areContentsTheSame', 'FRAMEWORK', 'ListAdapter differ runs the DiffUtil contents check on the submitted list', cls='non_standard', via='ListAdapter submitList DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:77-83; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:103-108')
e('PeerListAdapter.submitList', 'PeerListAdapter$1.areItemsTheSame', 'FRAMEWORK', 'ListAdapter differ runs the DiffUtil identity check on the submitted list', cls='non_standard', via='ListAdapter submitList DiffUtil dispatch', evidence='INFERRED DiffUtil dispatch; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:77-83; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:110-115')
e('PeerListAdapter.onCreateViewHolder', 'PeerListAdapter$ViewHolder.<init>', 'CALL', 'ViewHolder construction on holder creation', cls='explicit', evidence='SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:67; SRC ui/detailtorrent/pages/peers/PeerListAdapter.java:126-132')
e('DetailTorrentPiecesFragment.newInstance', 'DetailTorrentPiecesFragment.<clinit>', 'FRAMEWORK', 'First fragment construction initialises the fragment class', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:59-66; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:47-52')
e('DetailTorrentPiecesFragment.onCreateView', 'PiecesView.<init>(Context,AttributeSet)', 'FRAMEWORK', 'Layout inflation of fragment_detail_torrent_pieces uses the 2-arg ctor (no style attribute)', cls='non_standard', via='Android layout inflation dispatch', evidence='INFERRED layout inflation dispatch; SRC ui/detailtorrent/pages/pieces/DetailTorrentPiecesFragment.java:71; SRC ui/detailtorrent/pages/pieces/PiecesView.java:57-62')
e('PiecesView.<init>(Context,AttributeSet)', 'PiecesView.create', 'CALL', '2-arg constructor builds the piece paints', cls='explicit', evidence='SRC ui/detailtorrent/pages/pieces/PiecesView.java:61; SRC ui/detailtorrent/pages/pieces/PiecesView.java:71-88')
e('PiecesView.setPieces', 'PiecesView.onDraw', 'FRAMEWORK', 'setPieces invalidates the view, scheduling a draw', cls='non_standard', via='View invalidate dispatch', evidence='INFERRED View invalidate dispatch; SRC ui/detailtorrent/pages/pieces/PiecesView.java:89-99; SRC ui/detailtorrent/pages/pieces/PiecesView.java:119-141')
e('PiecesView.setPieces', 'PiecesView.onMeasure', 'FRAMEWORK', 'setPieces requests layout on length change, scheduling a measure', cls='non_standard', via='View requestLayout dispatch', evidence='INFERRED View requestLayout dispatch; SRC ui/detailtorrent/pages/pieces/PiecesView.java:98; SRC ui/detailtorrent/pages/pieces/PiecesView.java:104-117')
e('DetailTorrentTrackersFragment.newInstance', 'DetailTorrentTrackersFragment.<clinit>', 'FRAMEWORK', 'First fragment construction initialises the fragment class', cls='non_standard', via='JVM class-init on first reference', evidence='INFERRED class-init rule; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:93-100; SRC ui/detailtorrent/pages/trackers/DetailTorrentTrackersFragment.java:71-77')

UNREACHABLE.update({
    'PeerListAdapter.getItemKey': ('no_trigger_in_app',
        'Selectable implementation, PeerListAdapter.java:86-93. No KeyProvider ever holds a PeerListAdapter: the peers fragment builds no SelectionTracker/KeyProvider, and the only selectable.getItemKey call sites in the saved full-tree grep are the four KeyProvider getKey methods of adapters that own one.',
        'Saved full-tree greps grep_selectable_methods.txt, grep_Selectable_all.txt, grep_selectiontracker.txt; batch-94 ROUND 2 flip, re-checked complete-tree + XML',
        'INFERRED'),
})
UNREACHABLE.update({
    'PeerListAdapter.getItemPosition': ('no_trigger_in_app',
        'Selectable implementation, PeerListAdapter.java:95-100. Same as getItemKey: no KeyProvider ever holds a PeerListAdapter; the only selectable.getItemPosition call sites are the four KeyProvider getPosition methods.',
        'Saved full-tree greps grep_selectable_methods.txt, grep_Selectable_all.txt, grep_selectiontracker.txt; batch-94 ROUND 2 flip, re-checked complete-tree + XML',
        'INFERRED'),
})
UNREACHABLE.update({
    'PiecesView.<init>(Context,AttributeSet,int)': ('no_trigger_in_app',
        'Definition PiecesView.java:64-69. The sole declaring layout carries no style attribute so inflation uses the 2-arg ctor, the 2-arg ctor does not chain to the 3-arg ctor, and the saved grep finds 0 new PiecesView( hits in the 252-file tree.',
        'Saved greps grep_new_PiecesView.txt, grep_class_PiecesView.txt; batch-94 ROUND 2 flip, re-checked complete-tree + XML',
        'INFERRED'),
})

SUPPRESS.update({
    'PeerListAdapter.getItemKey',
    'PeerListAdapter.getItemPosition',
})
