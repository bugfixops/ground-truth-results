# r40 citation rework (2026-11-01): evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, grades, edges, endpoints, SUPPRESS entries and line ranges unchanged.
# C06 converter note (2026-11-01): bare 'core/...' SRC citations reworded to full-package 'org/proninyaroslav/libretorrent/core/...' (citation-only, merger no-increase rule for check 2); labels, kinds, grades, edges and SUPPRESS unchanged. Stronger-evidence check: merger tree holds no UNREACHABLE entry for these keys, so no grade change.
# Batch 41 part (TorrentSessionImpl inner-listener tail and load
# task; TorrentInputStream; TorrentStream). Hand-written edges and
# UNREACHABLE entries only. Each evidence string cites lines printed
# in graphs/LibreTorrent/scratch/b041_printed.txt. Source paths below
# are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/,
# except org/nanohttpd/ paths, which are relative to the same java root.
# Dependencies: none; every REACHABLE row below has an edge here.

e('TorrentSessionImpl$InnerListener.alert', 'TorrentSessionImpl$InnerListener.lambda$alert$1', 'CALL', 'ADD_TORRENT case notifies listeners through its second lambda', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentSessionImpl.java:1086-1087')
e('TorrentSessionImpl.onBeforeStart', 'TorrentSessionImpl$InnerListener.types', 'FRAMEWORK', 'Library types query on the inner listener registered on session start', cls='non_standard', via='libtorrent AlertListener types dispatch', evidence='INFERRED library dispatch; SRC TorrentSessionImpl.java:987; SRC TorrentSessionImpl.java:1064-1067')
e('TorrentSessionImpl.restoreTorrents', 'TorrentSessionImpl$LoadTorrentTask.<init>', 'CALL', 'Restore torrents creates a load task for the saved torrent', cls='explicit', evidence='SRC TorrentSessionImpl.java:412; SRC TorrentSessionImpl.java:1489')
e('TorrentSessionImpl$LoadTorrentTask.run', 'TorrentSessionImpl$LoadTorrentTask.lambda$run$0', 'CALL', 'Load task error path notifies listeners through its lambda', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentSessionImpl.java:1527-1528')
e('TorrentSessionImpl.restoreTorrents', 'TorrentSessionImpl$LoadTorrentTask.putMagnet', 'CALL', 'Restore torrents stores the magnet data on the load task', cls='explicit', evidence='SRC TorrentSessionImpl.java:414-419; SRC TorrentSessionImpl.java:1494')
e('TorrentSessionImpl.runNextLoadTorrentTask', 'TorrentSessionImpl$LoadTorrentTask.run', 'CALL', 'Load-task executor runs the queued load task', cls='non_standard', via='Executor dispatch', evidence='INFERRED executor dispatch; SRC TorrentSessionImpl.java:1472; SRC TorrentSessionImpl.java:1508-1530')
e('TorrentEngine.getTorrentInputStream', 'TorrentInputStream.<clinit>', 'CALL', 'First stream construction runs the stream class initialisation', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC TorrentEngine.java:759; SRC TorrentInputStream.java:62')
e('TorrentEngine.getTorrentInputStream', 'TorrentInputStream.<init>', 'CALL', 'Engine stream getter constructs the torrent input stream', cls='explicit', evidence='SRC TorrentEngine.java:759; SRC TorrentInputStream.java:97')
e('NanoHTTPD$Response.send', 'TorrentInputStream.close', 'CALL', 'Response send closes the response data stream', cls='non_standard', via='NanoHTTPD safeClose virtual dispatch to the data stream', evidence='INFERRED virtual dispatch; SRC org/nanohttpd/NanoHTTPD.java:1225; SRC TorrentInputStream.java:361')
e('TorrentInputStream.read(byte[],int,int)', 'TorrentInputStream.filePosToPiecePos', 'CALL', 'Three-arg read maps file positions to piece positions', cls='explicit', evidence='SRC TorrentInputStream.java:313; SRC TorrentInputStream.java:169')
e('NanoHTTPD$Response.send', 'TorrentInputStream.finalize', 'CALL', 'Response send is the last use of the stream, after which GC may finalise it', cls='non_standard', via='JVM GC finalizer dispatch', evidence='INFERRED GC dispatch; SRC org/nanohttpd/NanoHTTPD.java:1225; SRC TorrentInputStream.java:122-133')
e('TorrentInputStream$1.onPieceFinished', 'TorrentInputStream.pieceFinished', 'CALL', 'Stream listener callback wakes the waiting readers', cls='explicit', evidence='SRC TorrentInputStream.java:427; SRC TorrentInputStream.java:431')
e('NanoHTTPD$Response.sendBody', 'TorrentInputStream.read(byte[],int,int)', 'CALL', 'Response body send reads the stream data with the three-arg read', cls='non_standard', via='InputStream virtual dispatch to TorrentInputStream', evidence='SRC org/nanohttpd/NanoHTTPD.java:1267; SRC TorrentInputStream.java:257')
e('TorrentInputStream.read(byte[],int,int)', 'TorrentInputStream.readFromCache', 'CALL', 'Three-arg read serves pieces from the cache', cls='explicit', evidence='SRC TorrentInputStream.java:324; SRC TorrentInputStream.java:180')
e('TorrentInputStream$1.onReadPiece', 'TorrentInputStream.readPiece', 'CALL', 'Stream listener callback feeds a read piece into the stream', cls='explicit', evidence='SRC TorrentInputStream.java:418; SRC TorrentInputStream.java:436')
e('TorrentStreamServer.handleTorrent', 'TorrentInputStream.skip', 'CALL', 'Stream server range branch skips to the requested offset', cls='explicit', evidence='SRC TorrentStreamServer.java:207; SRC TorrentInputStream.java:375')
e('TorrentInputStream.read()', 'TorrentInputStream.toUnsignedByte', 'CALL', 'Single-byte read converts the cached byte to unsigned', cls='explicit', evidence='SRC TorrentInputStream.java:248; SRC TorrentInputStream.java:190')
e('TorrentInputStream.read(byte[],int,int)', 'TorrentInputStream.waitForPiece', 'CALL', 'Three-arg read waits for the needed piece', cls='explicit', evidence='SRC TorrentInputStream.java:335; SRC TorrentInputStream.java:135')
e('TorrentInputStream.read(byte[],int,int)', 'TorrentInputStream.waitForReadPieces', 'CALL', 'Three-arg read waits for the pieces being read', cls='explicit', evidence='SRC TorrentInputStream.java:342; SRC TorrentInputStream.java:150')
e('TorrentInputStream.<init>', 'TorrentInputStream$1.<init>', 'CALL', 'Stream constructor runs the anonymous listener field initialiser', cls='explicit', evidence='SRC TorrentInputStream.java:410; SRC TorrentInputStream.java:97')
e('TorrentDownloadImpl$InnerListener.lambda$alert$3', 'TorrentInputStream$1.onPieceFinished', 'CALL', 'Download piece-finished notify lambda tells the stream listener', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentDownloadImpl.java:260; SRC TorrentInputStream.java:422')
e('TorrentDownloadImpl.lambda$handleReadPiece$4', 'TorrentInputStream$1.onReadPiece', 'CALL', 'Download read-piece notify lambda tells the stream listener', cls='non_standard', via='notifyListeners callback dispatch', evidence='INFERRED listener dispatch; SRC TorrentDownloadImpl.java:453; SRC TorrentInputStream.java:413')
e('TorrentInputStream.read(byte[],int,int)', 'TorrentInputStream$Piece.<init>', 'CALL', 'Three-arg read creates a piece record for the piece being read', cls='explicit', evidence='SRC TorrentInputStream.java:303; SRC TorrentInputStream.java:79')
e('TorrentInputStream.read(byte[],int,int)', 'TorrentInputStream$ReadSession.<init>', 'CALL', 'Three-arg read creates a read session for the read', cls='explicit', evidence='SRC TorrentInputStream.java:290; SRC TorrentInputStream.java:64')
e('TorrentDownloadImpl.getStream', 'TorrentStream.<clinit>', 'CALL', 'First stream construction runs the stream class initialisation', cls='non_standard', via='JVM class initialisation on first use', evidence='INFERRED JVM dispatch; SRC TorrentDownloadImpl.java:1621-1624; SRC TorrentStream.java:93')
e('TorrentDownloadImpl.getStream', 'TorrentStream.<init>(String,int,int,int,int,long,long,int)', 'CALL', 'Download stream getter constructs the torrent stream record', cls='explicit', evidence='SRC TorrentDownloadImpl.java:1621-1624; SRC TorrentStream.java:40')
e('TorrentInputStream.read(byte[],int,int)', 'TorrentStream.bytesToPieceIndex', 'CALL', 'Three-arg read maps byte offsets to piece indexes', cls='explicit', evidence='SRC TorrentInputStream.java:285; SRC TorrentStream.java:68')
e('TorrentStream.<clinit>', 'TorrentStream$1.<init>', 'CALL', 'Stream class initialisation creates its parcelable creator', cls='explicit', evidence='SRC TorrentStream.java:93-95')

UNREACHABLE.update({
    'TorrentInputStream.markSupported': ('no_trigger_in_app',
        'Only stream holders are TorrentEngine creation and TorrentStreamServer use; the sole consumer, NanoHTTPD Response, reads with the 3-arg overload and never calls mark/markSupported on its data.',
        'SRC TorrentInputStream.java:405-408; SRC org/nanohttpd/NanoHTTPD.java:1267',
        'INFERRED'),
    'TorrentInputStream.read()': ('no_trigger_in_app',
        'Single-byte read has no caller: NanoHTTPD sendBody reads response data with the 3-arg overload only, and no wrapping stream exists in the tree.',
        'SRC TorrentInputStream.java:196; SRC org/nanohttpd/NanoHTTPD.java:1267',
        'INFERRED'),
    'TorrentInputStream.read(byte[])': ('no_trigger_in_app',
        'One-arg read has no caller: NanoHTTPD sendBody calls the 3-arg overload directly, so this delegating overload is never used.',
        'SRC TorrentInputStream.java:355-358; SRC org/nanohttpd/NanoHTTPD.java:1267',
        'INFERRED'),
    'TorrentInputStream$Piece.equals': ('no_trigger_in_app',
        'Private nested class Piece is never compared with equals: readPiece compares index fields directly, and no code outside TorrentInputStream.java can name Piece.',
        'SRC TorrentInputStream.java:90-94; SRC TorrentInputStream.java:436',
        'INFERRED'),
    'TorrentInputStream$Piece.hashCode': ('no_trigger_in_app',
        'Private nested class Piece is never hashed: no hash collection of Piece exists and no code outside TorrentInputStream.java can name Piece.',
        'SRC TorrentInputStream.java:84-88',
        'INFERRED'),
    'TorrentStream.<init>(Parcel)': ('no_trigger_in_app',
        'Only reached via CREATOR.createFromParcel, and no putParcelable/getParcelable site passes a TorrentStream anywhere in the app tree.',
        'SRC TorrentStream.java:55-66; SRC TorrentStream.java:96-100',
        'INFERRED'),
    'TorrentStream.describeContents': ('no_trigger_in_app',
        'Parcelable method called by the framework only when the object is parceled; no parceling site for a TorrentStream exists.',
        'SRC TorrentStream.java:73-77',
        'INFERRED'),
    'TorrentStream.equals': ('no_trigger_in_app',
        'No stream.equals call anywhere; server and stream code read stream fields directly, and no collection holds a TorrentStream.',
        'SRC TorrentStream.java:115-119',
        'INFERRED'),
    'TorrentStream.hashCode': ('no_trigger_in_app',
        'No hash caller and no hash-collection use of a TorrentStream anywhere in the tree.',
        'SRC TorrentStream.java:109-113',
        'INFERRED'),
    'TorrentStream.toString': ('no_trigger_in_app',
        'No log, concatenation or toString call on a stream: server code concatenates stream.id and stream.fileSize only.',
        'SRC TorrentStream.java:121-136',
        'INFERRED'),
    'TorrentStream.writeToParcel': ('no_trigger_in_app',
        'Parcelable method called by the framework only when the object is parceled; no parceling site for a TorrentStream exists.',
        'SRC TorrentStream.java:79-91',
        'INFERRED'),
    'TorrentStream$1.createFromParcel': ('no_trigger_in_app',
        'Framework Parcelable dispatch only; no unparcel site for a TorrentStream exists in the app tree.',
        'SRC TorrentStream.java:96-100',
        'INFERRED'),
})

# The Parcel ctor is the only UNREACHABLE method of this batch with a
# bytecode caller (its own creator, itself UNREACHABLE), so its auto
# edge is suppressed. The other eleven have no bytecode caller.
SUPPRESS.update({
    'TorrentStream.<init>(Parcel)',
})
