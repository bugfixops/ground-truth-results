# Citation-form rework 2026-11-01: evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, edges, endpoints, SUPPRESS entries and line ranges unchanged; full relative paths remain in the .md and printed files.
# C02 conversion of helper/a3-fix-b019 batch-19 part (2026-11-01).
# This fixed copy supersedes the fix-buildnames b019; it carries the
# 3-edge TorrentMetaInfo ctor split, 35 edges total.
# Base part verified against clone batch19-merge-ready.md: labels/kinds
# match exactly; counts R33 U7 O0; edges 35; SUPPRESS 7.
# STRONGER-EVIDENCE upgrades (tree graph_def.py holds SOURCE, part held
# INFERRED; kind/reason/ref unchanged; never downgraded): all 7
# FixedRingBuffer UNREACHABLE keys (add(Iterable), contains,
# getAllocatedSize, indexOf, isFull, remove, removeAt): INFERRED -> SOURCE.
# HARNESS NOTE: check_part.py compares the part grade to the merge-ready
# grade (INFERRED for all 7 rows), so the 7 upgrades above produce
# exactly 7 grade-mismatch FAIL lines and no other FAILs. Do NOT revert
# these grades to INFERRED at merge; the merger must either waive those
# 7 FAIL lines or patch the harness to accept SOURCE where the tree
# holds SOURCE.
# Greps: parts-staging/grep/19/ (7 files, one per UNREACHABLE row).
# Printed evidence: parts/b019_printed.txt (verbatim base printed file,
# 23,400 B, under 900 KB; copy pending only on the sandbox exec-write
# block - see REPORT-b019.md).

# Batch 19 part (TorrentBuilder and its helpers, TorrentFileObserver, FixedRingBuffer,
# DecodeException, FetchLinkException). Hand-written edges, UNREACHABLE entries and
# SUPPRESS strings only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b019_printed.txt. Source paths are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/
#
# No batch-19 method has an incoming edge in graph_def.py, so no route is listed
# as a Dependency here; every REACHABLE row below has a new edge in this file.

# TorrentBuilder: built and configured in CreateTorrentViewModel; the Rx lambda and
# the libtorrent4j Listener callbacks run through unprinted dispatch (INFERRED).
e('TorrentBuilder.build', 'TorrentBuilder.lambda$build$0', 'FRAMEWORK', 'Run the generate/entry/bencode lambda when the build Single is subscribed',
  cls='non_standard', via='RxJava Single.fromCallable subscription dispatch',
  evidence='INFERRED Rx subscription dispatch; SRC TorrentBuilder.java:177; ui/createtorrent/CreateTorrentViewModel.java:171-173')
e('CreateTorrentViewModel.buildTorrent', 'TorrentBuilder.observeProgress', 'CALL', 'Observe build progress while building the torrent',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:166-169; TorrentBuilder.java:168-171')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.setAsPrivate', 'CALL', 'Set the private flag on the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:195; TorrentBuilder.java:134-139')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.setComment', 'CALL', 'Set the torrent comment on the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:197; TorrentBuilder.java:148-153')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.setCreator', 'CALL', 'Set the torrent creator on the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:196; TorrentBuilder.java:141-146')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.setFileNameFilter', 'CALL', 'Set the file-name filter predicate on the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:198; TorrentBuilder.java:155-160')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.setPieceSize', 'CALL', 'Set the piece size on the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:191; TorrentBuilder.java:109-114')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.setSeedPath', 'CALL', 'Set the seed path on the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:190; TorrentBuilder.java:94-101')
e('CreateTorrentViewModel.makeBuilder', 'TorrentBuilder.setTorrentVersion', 'CALL', 'Set the torrent version on the builder',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:192; TorrentBuilder.java:162-166')
e('TorrentBuilder.build', 'TorrentBuilder.subscribeProgress', 'CALL', 'Register the progress listener before generating the torrent',
  cls='explicit', evidence='SRC TorrentBuilder.java:175,180-200')
e('TorrentBuilder.subscribeProgress', 'TorrentBuilder$1.<init>', 'CALL', 'Construct the anonymous Listener registered with the libtorrent4j builder',
  cls='explicit', evidence='SRC TorrentBuilder.java:182')
e('TorrentBuilder.build', 'TorrentBuilder$1.accept', 'CALL', 'Test each file name against the file-name filter during generation',
  cls='non_standard', via='libtorrent4j TorrentBuilder.Listener callback dispatch during build',
  evidence='INFERRED library callback dispatch; SRC TorrentBuilder.java:182,184-192')
e('TorrentBuilder.build', 'TorrentBuilder$1.progress', 'CALL', 'Report generation progress through the progress Observable',
  cls='non_standard', via='libtorrent4j TorrentBuilder.Listener callback dispatch during build',
  evidence='INFERRED library callback dispatch; SRC TorrentBuilder.java:182,195-198')
e('TorrentBuilder$1.progress', 'TorrentBuilder$Progress.<init>', 'CALL', 'Publish a progress value for the current piece',
  cls='explicit', evidence='SRC TorrentBuilder.java:197; TorrentBuilder.java:65-69')
e('CreateTorrentViewModel.getTorrentVersionByIndex', 'TorrentBuilder$TorrentVersion.<clinit>', 'FRAMEWORK', 'First use of a TorrentVersion constant initialises the enum',
  cls='non_standard', via='JVM enum class initialization on first active use',
  evidence='INFERRED JVM enum initialization; SRC ui/createtorrent/CreateTorrentViewModel.java:338-349; TorrentBuilder.java:72-86')
e('TorrentBuilder$TorrentVersion.<clinit>', 'TorrentBuilder$TorrentVersion.<init>', 'CALL', 'Construct each enum constant during enum initialisation',
  cls='non_standard', via='JVM enum constant construction during <clinit>',
  evidence='INFERRED JVM enum construction; SRC TorrentBuilder.java:83-85')
e('TorrentBuilder.setTorrentVersion', 'TorrentBuilder$TorrentVersion.flag', 'CALL', 'Read the create flags of the chosen torrent version',
  cls='explicit', evidence='SRC TorrentBuilder.java:163; TorrentBuilder.java:79-81')
e('CreateTorrentViewModel.getAndValidateTrackers', 'TorrentBuilder$Tracker.<init>', 'CALL', 'Construct a tracker entry for each validated tracker URL',
  cls='explicit', evidence='SRC ui/createtorrent/CreateTorrentViewModel.java:275; TorrentBuilder.java:53-59')

# TorrentFileObserver: the anonymous subclass construction in makeTorrentFileObserver
# calls this super constructor.
e('TorrentEngine.makeTorrentFileObserver', 'TorrentFileObserver.<init>', 'CALL', 'Construct the anonymous file observer for the watch directory',
  cls='explicit', evidence='SRC TorrentEngine.java:1136-1137; TorrentFileObserver.java:35-37')

# FixedRingBuffer: held only by Logger; its reachable operations are Logger's buffer calls.
e('Logger.lazyGetInputBuf', 'FixedRingBuffer.<init>(int,int)', 'CALL', 'Allocate the input log buffer',
  cls='explicit', evidence='SRC Logger.java:68; FixedRingBuffer.java:50-64')
e('Logger.send', 'FixedRingBuffer.add(Object)', 'CALL', 'Append a log entry to the input buffer',
  cls='explicit', evidence='SRC Logger.java:104; FixedRingBuffer.java:86-99')
e('Logger.forceFilterBuf', 'FixedRingBuffer.clear', 'CALL', 'Clear the output buffer before refiltering',
  cls='explicit', evidence='SRC Logger.java:249; FixedRingBuffer.java:159-168')
e('Logger.swapBuffers', 'FixedRingBuffer.get', 'CALL', 'Read a buffered log entry while swapping buffers',
  cls='explicit', evidence='SRC Logger.java:152; FixedRingBuffer.java:150-158')
e('Logger.swapBuffers', 'FixedRingBuffer.isEmpty', 'CALL', 'Test whether the input buffer is empty before swapping',
  cls='explicit', evidence='SRC Logger.java:145; FixedRingBuffer.java:169-173')
e('Logger.forceFilterBuf', 'FixedRingBuffer.iterator', 'CALL', 'Iterate the input buffer in the enhanced-for loop',
  cls='non_standard', via='enhanced-for iterator dispatch',
  evidence='INFERRED compiler iterator dispatch; SRC Logger.java:250; FixedRingBuffer.java:209-213')
e('FixedRingBuffer.clear', 'FixedRingBuffer.resetHead', 'CALL', 'Reset the buffer head when clearing a non-empty buffer',
  cls='explicit', evidence='SRC FixedRingBuffer.java:166,190-195')
e('Logger.swapBuffers', 'FixedRingBuffer.size', 'CALL', 'Read the buffered entry count while swapping',
  cls='explicit', evidence='SRC Logger.java:150; FixedRingBuffer.java:65-74')
e('FixedRingBuffer.add(Object)', 'FixedRingBuffer.tryGrow', 'CALL', 'Grow the buffer when an append needs more capacity',
  cls='explicit', evidence='SRC FixedRingBuffer.java:88,196-208')
e('FixedRingBuffer.iterator', 'FixedRingBuffer$FixedRingBufferIterator.<init>', 'CALL', 'Construct the iterator returned by iterator()',
  cls='explicit', evidence='SRC FixedRingBuffer.java:211,214')
e('Logger.forceFilterBuf', 'FixedRingBuffer$FixedRingBufferIterator.hasNext', 'CALL', 'Advance the for-loop over the input buffer',
  cls='non_standard', via='enhanced-for iterator dispatch',
  evidence='INFERRED compiler iterator dispatch; SRC Logger.java:250; FixedRingBuffer.java:219')
e('Logger.forceFilterBuf', 'FixedRingBuffer$FixedRingBufferIterator.next', 'CALL', 'Read the next buffered entry in the for-loop',
  cls='non_standard', via='enhanced-for iterator dispatch',
  evidence='INFERRED compiler iterator dispatch; SRC Logger.java:250; FixedRingBuffer.java:225')

# Exception constructors: thrown from the printed sites below.
e('TorrentMetaInfo.<init>(byte[])', 'DecodeException.<init>(Exception)', 'CALL', 'Wrap a decode failure in a DecodeException',
  cls='explicit', evidence='SRC TorrentMetaInfo.java:69; DecodeException.java:35-39')
e('TorrentMetaInfo.<init>(TorrentInfo)', 'DecodeException.<init>(Exception)', 'CALL', 'Wrap a decode failure in a DecodeException',
  cls='explicit', evidence='SRC TorrentMetaInfo.java:79; DecodeException.java:35-39')
e('TorrentMetaInfo.<init>(FileInputStream)', 'DecodeException.<init>(Exception)', 'CALL', 'Wrap a decode failure in a DecodeException',
  cls='explicit', evidence='SRC TorrentMetaInfo.java:92; DecodeException.java:35-39')
e('Utils.fetchHttpUrl', 'FetchLinkException.<init>(Exception)', 'CALL', 'Wrap an HTTP connection construction failure',
  cls='explicit', evidence='SRC Utils.java:474; FetchLinkException.java:35-38')

# FixedRingBuffer operations with no caller: the only holder outside the class itself is
# Logger, whose buffer calls are exactly add(entry), isEmpty, size, get(i), clear and
# the for-each iterator; a saved full-tree grep finds no caller for any row below.
UNREACHABLE.update({
    'FixedRingBuffer.add(Iterable)': ('no_trigger_in_app',
        'No app code calls add(Iterable) on a FixedRingBuffer. Its body only calls add(e) for each element (self-use into a REACHABLE method, not a route into this one); Logger add calls pass a single LogEntry, never an Iterable. Plain custom method, not an interface or callback method.',
        'SRC FixedRingBuffer.java:80-85',
        'SOURCE'),
    'FixedRingBuffer.contains': ('no_trigger_in_app',
        'No app code calls contains on a FixedRingBuffer. The only holder is Logger, whose buffer calls are add(entry), isEmpty, size, get(i), clear and the for-each iterator; every tree-wide contains() hit is another receiver.',
        'SRC FixedRingBuffer.java:179-189',
        'SOURCE'),
    'FixedRingBuffer.getAllocatedSize': ('no_trigger_in_app',
        'No app code calls getAllocatedSize on a FixedRingBuffer; no caller exists outside the definition itself.',
        'SRC FixedRingBuffer.java:75-78',
        'SOURCE'),
    'FixedRingBuffer.indexOf': ('no_trigger_in_app',
        'No app code calls indexOf on a FixedRingBuffer; its only caller is remove(), itself UNREACHABLE in this batch, so the two flip together.',
        'SRC FixedRingBuffer.java:112-124',
        'SOURCE'),
    'FixedRingBuffer.isFull': ('no_trigger_in_app',
        'No app code calls isFull on a FixedRingBuffer; literally 0 isFull() hits tree-wide outside this file.',
        'SRC FixedRingBuffer.java:174-178',
        'SOURCE'),
    'FixedRingBuffer.remove': ('no_trigger_in_app',
        'No app code calls remove on a FixedRingBuffer; every tree-wide remove() hit is another receiver. It anchors indexOf and removeAt, which flip with it.',
        'SRC FixedRingBuffer.java:100-111',
        'SOURCE'),
    'FixedRingBuffer.removeAt': ('no_trigger_in_app',
        'No app code calls removeAt on a FixedRingBuffer; its only caller is remove(), itself UNREACHABLE in this batch.',
        'SRC FixedRingBuffer.java:125-149',
        'SOURCE'),
})

# Suppress bytecode auto edges into the UNREACHABLE FixedRingBuffer operations.
# FixedRingBuffer is not subclassed in the app, so there are no @Variant copies.
# Note: add(Iterable) is suppressed by its qualified name so the REACHABLE
# add(Object) overload keeps its hand edges in this file.
SUPPRESS.update({
    'FixedRingBuffer.add(Iterable)', 'FixedRingBuffer.contains', 'FixedRingBuffer.getAllocatedSize',
    'FixedRingBuffer.indexOf', 'FixedRingBuffer.isFull', 'FixedRingBuffer.remove', 'FixedRingBuffer.removeAt',
})
