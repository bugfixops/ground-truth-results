# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# Converter C08 delivery 2026-11-01: audited A3 base part, unchanged except this header.
# Verified vs merge-ready batch56 (check_part PASS); stronger-evidence tree check: none of this batch's
# UNREACHABLE keys is present in the merger tree graph_def.py, so no evidence grade was changed.
# b057 note (recorded, not applied here): Utils.buildExactAlarmPermissionRequest SUPPRESS entries belong
# in the b074/b058 caller parts at merge time; this part does not suppress it.
# Batch 56 part (NormalizeUrl tail, PathResolver, PercentEncoder, BencodeFileTreeUtils, BindingAdapterUtils, DateUtils).
# Hand-written edges only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b056_printed.txt.
# Source paths below are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/.
# BindingAdapter rows are reached by generated data-binding dispatch from
# the printed layout attributes (layout file:line cited in the .md, not as
# an SRC citation, since check 8 covers .java files only).
# No pre-existing route is relied on; every REACHABLE row below has an edge here.

# NormalizeUrl tail through doNormalize (batch 55 row 40).
e('NormalizeUrl.doNormalize', 'NormalizeUrl.isMatch', 'CALL', 'Normalisation filters query keys through the match test', cls='explicit', evidence='SRC NormalizeUrl.java:278-282; SRC NormalizeUrl.java:304-315')
e('NormalizeUrl.doNormalize', 'NormalizeUrl.mapToQuery', 'CALL', 'Normalisation rebuilds the query string from the filtered map', cls='explicit', evidence='SRC NormalizeUrl.java:290-291; SRC NormalizeUrl.java:364-385')
e('DetailTorrentFragment.addTrackers', 'NormalizeUrl.normalize(String,Options)', 'CALL', 'Detail tracker normalisation runs the two-arg normalise', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:719-726; SRC NormalizeUrl.java:178-189')
e('NormalizeUrl.doNormalize', 'NormalizeUrl.parseQuery', 'CALL', 'Normalisation parses the query string unconditionally', cls='explicit', evidence='SRC NormalizeUrl.java:225; SRC NormalizeUrl.java:333-362')
e('NormalizeUrl.doNormalize', 'NormalizeUrl.urlToString', 'CALL', 'Normalisation rebuilds the URL string unconditionally', cls='explicit', evidence='SRC NormalizeUrl.java:290-291; SRC NormalizeUrl.java:387-414')
e('DetailTorrentFragment.addTrackers', 'NormalizeUrl$Options.<init>', 'CALL', 'Detail tracker normalisation builds an Options object', cls='explicit', evidence='SRC ui/detailtorrent/DetailTorrentFragment.java:719-720; SRC NormalizeUrl.java:42')
e('NormalizeUrl.doNormalize', 'NormalizeUrl$Options.<init>', 'CALL', 'Normalisation builds a default Options object when none is given', cls='explicit', evidence='SRC NormalizeUrl.java:197; SRC NormalizeUrl.java:42')

# PathResolver through doNormalize.
e('NormalizeUrl.doNormalize', 'PathResolver.resolve(String,String)', 'CALL', 'Normalisation resolves the path when one is present', cls='explicit', evidence='SRC NormalizeUrl.java:259; SRC PathResolver.java:27-34')
e('PathResolver.resolve(String,String)', 'PathResolver.merge', 'CALL', 'Two-part resolve merges the base and reference paths', cls='explicit', evidence='SRC PathResolver.java:27-34; SRC PathResolver.java:46-63')
e('PathResolver.resolve(String,String)', 'PathResolver.resolve(String[])', 'CALL', 'Two-part resolve delegates to the parts resolve', cls='explicit', evidence='SRC PathResolver.java:27-34; SRC PathResolver.java:72-108')
e('PathResolver.resolve(String[])', 'PathResolver.join', 'CALL', 'Parts resolve joins the resolved parts', cls='explicit', evidence='SRC PathResolver.java:72-108; SRC PathResolver.java:110-124')

# BencodeFileTreeUtils through the add-torrent ViewModel.
e('AddTorrentViewModel.makeFileTree', 'BencodeFileTreeUtils.buildFileTree', 'CALL', 'Add-torrent file tree build runs the bencode tree builder', cls='explicit', evidence='SRC ui/addtorrent/AddTorrentViewModel.java:368-379; SRC BencodeFileTreeUtils.java:46')
e('BencodeFileTreeUtils.buildFileTree', 'BencodeFileTreeUtils.makeObject', 'CALL', 'Bencode tree build creates a node object for each new path node', cls='explicit', evidence='SRC BencodeFileTreeUtils.java:102; SRC BencodeFileTreeUtils.java:119-126')

# BindingAdapterUtils through generated data-binding dispatch from the printed layout attributes.
e('FragmentDetailTorrentInfoBindingImpl.executeBindings', 'BindingAdapterUtils.formatDate', 'CALL', 'Generated info binding formats torrent dates through the adapter', cls='non_standard', via='generated data-binding dispatch from the printed formatDate attributes', evidence='INFERRED generated data-binding dispatch; SRC BindingAdapterUtils.java:50-51')
e('FragmentDetailTorrentStateBindingImpl.executeBindings', 'BindingAdapterUtils.formatETA', 'CALL', 'Generated state binding formats ETAs through the adapter', cls='non_standard', via='generated data-binding dispatch from the printed formatETA expression', evidence='INFERRED generated data-binding dispatch; SRC BindingAdapterUtils.java:68-71')
e('FragmentDetailTorrentStateBindingImpl.executeBindings', 'BindingAdapterUtils.formatFileSize', 'CALL', 'Generated state binding formats file sizes through the adapter', cls='non_standard', via='generated data-binding dispatch from the printed fileSize attributes', evidence='INFERRED generated data-binding dispatch; SRC BindingAdapterUtils.java:38-39')
e('FragmentDetailTorrentStateBindingImpl.executeBindings', 'BindingAdapterUtils.formatFloat', 'CALL', 'Generated state binding formats floats through the adapter', cls='non_standard', via='generated data-binding dispatch from the printed floatNum attributes', evidence='INFERRED generated data-binding dispatch; SRC BindingAdapterUtils.java:74-75')
e('FragmentDetailTorrentStateBindingImpl.executeBindings', 'BindingAdapterUtils.formatPieces', 'CALL', 'Generated state binding formats piece counts through the adapter', cls='non_standard', via='generated data-binding dispatch from the printed formatPieces expression', evidence='INFERRED generated data-binding dispatch; SRC BindingAdapterUtils.java:82')
e('FragmentDetailTorrentPiecesBindingImpl.executeBindings', 'BindingAdapterUtils.formatPiecesInfo', 'CALL', 'Generated pieces binding formats piece info through the adapter', cls='non_standard', via='generated data-binding dispatch from the printed formatPiecesInfo expression', evidence='INFERRED generated data-binding dispatch; SRC BindingAdapterUtils.java:102')
e('FragmentDetailTorrentStateBindingImpl.executeBindings', 'BindingAdapterUtils.formatProgress', 'CALL', 'Generated state binding formats progress through the adapter', cls='non_standard', via='generated data-binding dispatch from the printed formatProgress expression', evidence='INFERRED generated data-binding dispatch; SRC BindingAdapterUtils.java:57')
e('FragmentDetailTorrentStateBindingImpl.executeBindings', 'BindingAdapterUtils.formatSpeed', 'CALL', 'Generated state binding formats speeds through the adapter', cls='non_standard', via='generated data-binding dispatch from the printed formatSpeed expression', evidence='INFERRED generated data-binding dispatch; SRC BindingAdapterUtils.java:93')

# DateUtils through TorrentFilterCollection and the binding ETA route.
e('TorrentFilterCollection.dateAddedToday', 'DateUtils.<clinit>', 'CALL', 'First date-filter use initialises the DateUtils class', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC TorrentFilterCollection.java:47-53; SRC DateUtils.java:33-41')
e('TorrentFilterCollection.dateAddedMonth', 'DateUtils.endOfMonth', 'CALL', 'Month filter reads the month end through DateUtils', cls='explicit', evidence='SRC TorrentFilterCollection.java:79-83; SRC DateUtils.java:167-178')
e('TorrentFilterCollection.dateAddedToday', 'DateUtils.endOfToday', 'CALL', 'Today filter reads the day end through DateUtils', cls='explicit', evidence='SRC TorrentFilterCollection.java:47-53; SRC DateUtils.java:106-116')
e('TorrentFilterCollection.dateAddedWeek', 'DateUtils.endOfWeek', 'CALL', 'Week filter reads the week end through DateUtils', cls='explicit', evidence='SRC TorrentFilterCollection.java:67-73; SRC DateUtils.java:140-152')
e('TorrentFilterCollection.dateAddedYear', 'DateUtils.endOfYear', 'CALL', 'Year filter reads the year end through DateUtils', cls='explicit', evidence='SRC TorrentFilterCollection.java:87-93; SRC DateUtils.java:193-204')
e('TorrentFilterCollection.dateAddedYesterday', 'DateUtils.endOfYesterday', 'CALL', 'Yesterday filter reads the yesterday end through DateUtils', cls='explicit', evidence='SRC TorrentFilterCollection.java:57-63; SRC DateUtils.java:130-133')
e('BindingAdapterUtils.formatETA', 'DateUtils.formatElapsedTime(Context,long)', 'CALL', 'ETA formatting delegates to the two-arg elapsed-time formatter', cls='explicit', evidence='SRC BindingAdapterUtils.java:68-71; SRC DateUtils.java:43-46')
e('DateUtils.formatElapsedTime(Context,long)', 'DateUtils.formatElapsedTime(Context,StringBuilder,long)', 'CALL', 'Two-arg elapsed-time formatting delegates to the three-arg formatter', cls='explicit', evidence='SRC DateUtils.java:43-46; SRC DateUtils.java:48-90')
e('DateUtils.formatElapsedTime(Context,StringBuilder,long)', 'DateUtils.initFormatStrings', 'CALL', 'Elapsed-time formatting initialises its format strings', cls='explicit', evidence='SRC DateUtils.java:48-90; SRC DateUtils.java:92-104')
e('TorrentFilterCollection.dateAddedMonth', 'DateUtils.startOfMonth', 'CALL', 'Month filter reads the month start through DateUtils', cls='explicit', evidence='SRC TorrentFilterCollection.java:79-83; SRC DateUtils.java:180-191')
e('TorrentFilterCollection.dateAddedToday', 'DateUtils.startOfToday', 'CALL', 'Today filter reads the day start through DateUtils', cls='explicit', evidence='SRC TorrentFilterCollection.java:47-53; SRC DateUtils.java:118-128')
e('TorrentFilterCollection.dateAddedWeek', 'DateUtils.startOfWeek', 'CALL', 'Week filter reads the week start through DateUtils', cls='explicit', evidence='SRC TorrentFilterCollection.java:67-73; SRC DateUtils.java:154-165')
e('TorrentFilterCollection.dateAddedYear', 'DateUtils.startOfYear', 'CALL', 'Year filter reads the year start through DateUtils', cls='explicit', evidence='SRC TorrentFilterCollection.java:87-93; SRC DateUtils.java:206-217')

UNREACHABLE.update({
    'NormalizeUrl.join': ('branch_never_taken',
        'Only call site doNormalize :268, inside if (options.removeDirectoryIndex.length > 0) :263; default is empty (NormalizeUrl.java:90) and the saved 252-file grep finds zero assignments to removeDirectoryIndex, so the branch never runs.',
        'SRC NormalizeUrl.java:90,263-268',
        'INFERRED'),
    'NormalizeUrl.makeUserInfo': ('branch_never_taken',
        'Only call site urlToString :397, guarded user != null && !user.isEmpty() :396; doNormalize :232-234 nulls user/password whenever removeAuthentication is true, and the default is true (:100), so the guard never passes on a doNormalize route.',
        'SRC NormalizeUrl.java:100,232-234,396-397',
        'INFERRED'),
    'PercentEncoder.<clinit>': ('branch_never_taken',
        'Inherited from decode: the class first active use is decode, which sits behind the never-taken if (options.decode) branch in doNormalize :216; all 3 normalize callers set decode=false.',
        'SRC NormalizeUrl.java:216-217',
        'INFERRED'),
    'PercentEncoder.decode': ('branch_never_taken',
        'Only call site doNormalize :217, inside if (options.decode) :216; all 3 normalize callers tree-wide set decode=false (DetailTorrentFragment :720, CreateTorrentViewModel :309, AddLinkViewModel :68).',
        'SRC NormalizeUrl.java:216-217',
        'INFERRED'),
    'PercentEncoder.needsUnescaping': ('branch_never_taken',
        'Inherited from decode: only call site decode :35, and decode never runs (row 14).',
        'SRC PercentEncoder.java:33-35',
        'INFERRED'),
    'PercentEncoder.pow': ('branch_never_taken',
        'Inherited from decode/unhex: only call site unhex :111, and unhex runs only from decode, which never runs (row 14).',
        'SRC PercentEncoder.java:96-111',
        'INFERRED'),
    'PercentEncoder.unhex': ('branch_never_taken',
        'Inherited from decode: only call sites decode :54 and :79, and decode never runs (row 14).',
        'SRC PercentEncoder.java:33-79',
        'INFERRED'),
})

# SUPPRESS: the bytecode edge from this batch's REACHABLE urlToString into
# this batch's UNREACHABLE makeUserInfo (NormalizeUrl.java:397, inside the
# never-taken user guard). The other batch-56 UNREACHABLE methods are
# called by batch-55 doNormalize, so their SUPPRESS entries live in b055.
SUPPRESS.update({
    'NormalizeUrl.makeUserInfo',
})
