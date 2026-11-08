# Citation-form rework 2026-11-01: evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, edges, endpoints, SUPPRESS entries and line ranges unchanged; full relative paths remain in the .md and printed files.
# C02 conversion of helper/a3-g3 batch-17 part (2026-11-01).
# Base part verified against merger/staging-A1 batch17-merge-ready.md:
# labels/kinds match exactly; counts R30 U10 O0; edges 31; SUPPRESS 10.
# No TorrentService.init -> TorrentEngine.doStart edge (this b017
# supersedes the old merger-tree draft b017).
# STRONGER-EVIDENCE upgrades (tree graph_def.py holds SOURCE, part held
# INFERRED; kind/reason/ref unchanged; never downgraded):
#   NanoHTTPD$Response.getData, getRequestMethod, getStatus, setData,
#   setStatus, NanoHTTPD$Response$Status.getRequestStatus,
#   NanoHTTPD$SecureServerSocketFactory.create  (7 keys: INFERRED -> SOURCE).
# Kept INFERRED (no tree SOURCE entry): ChunkedOutputStream.write(int),
# write(byte[]), libretorrent.DataBinderMapperImpl.convertBrIdToString.
# HARNESS NOTE: check_part.py compares the part grade to the merge-ready
# grade (INFERRED for all 10 rows), so the 7 upgrades above produce
# exactly 7 grade-mismatch FAIL lines and no other FAILs. The harness
# checks are otherwise all satisfied. Do NOT revert these grades to
# INFERRED at merge; the merger must either waive those 7 FAIL lines or
# patch the harness to accept SOURCE where the tree holds SOURCE.
# Greps: parts-staging/grep/17/ (10 files, one per UNREACHABLE row).
# Printed evidence: parts/b017_printed.txt (trimmed to the ranges cited
# by this part plus the mapper bytecode appendix; base printed file
# exceeds 900 KB, so a verbatim copy is not deliverable).

# Batch 17 part (NanoHTTPD Response, ChunkedOutputStream, Status,
# ResponseException, SecureServerSocketFactory, ServerRunnable, plus the
# libretorrent generated mapper). Hand-written edges, UNREACHABLE entries
# and SUPPRESS strings only. Each evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b017_printed.txt.
#
# Pre-existing routes are NOT repeated here; they are listed with line refs
# in parts/b017.md Dependencies (none: no batch-17 REACHABLE row already has
# an incoming edge in graph_def.py). This file replaces the superseded
# draft parts/b017.py wholesale; no draft content is preserved except the
# route facts re-verified against the printed source below.

# Response accessors and setters on the live execute/send path.
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.getHeader', 'CALL', 'Read the connection header to decide keep-alive shutdown',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:733; org/nanohttpd/NanoHTTPD.java:1150-1156')
e('NanoHTTPD.useGzipWhenAccepted', 'NanoHTTPD$Response.getMimeType', 'CALL', 'Read the response MIME type for the gzip decision',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1661; org/nanohttpd/NanoHTTPD.java:1158-1160')
e('NanoHTTPD$Response.send', 'NanoHTTPD$Response.headerAlreadySent', 'CALL', 'Check whether connection and content-length headers are already present',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1205,1208; org/nanohttpd/NanoHTTPD.java:1173-1179')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.send', 'CALL', 'Send the response on the normal and catch paths',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:731,746,750; org/nanohttpd/NanoHTTPD.java:1183-1229')
e('NanoHTTPD$Response.sendBodyWithCorrectEncoding', 'NanoHTTPD$Response.sendBody', 'CALL', 'Write the response body, gzipped or plain',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1242,1245; org/nanohttpd/NanoHTTPD.java:1261-1275')
e('NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding', 'NanoHTTPD$Response.sendBodyWithCorrectEncoding', 'CALL', 'Apply the correct encoding for chunked or plain transfer',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1233,1236; org/nanohttpd/NanoHTTPD.java:1239-1247')
e('NanoHTTPD$Response.send', 'NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding', 'CALL', 'Transfer the body with chunking when chunked transfer is set',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1223; org/nanohttpd/NanoHTTPD.java:1230-1237')
e('NanoHTTPD$Response.send', 'NanoHTTPD$Response.sendContentLengthHeaderIfNotAlreadyPresent', 'CALL', 'Write the content-length header in the non-chunked, non-gzip branch',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1219; org/nanohttpd/NanoHTTPD.java:1277-1288')
e('NanoHTTPD$Response.send', 'NanoHTTPD$Response.setChunkedTransfer', 'CALL', 'Enable chunked transfer when gzip encoding is set',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1213; org/nanohttpd/NanoHTTPD.java:1290-1292')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.setGzipEncoding', 'CALL', 'Set gzip encoding from the accepted-encoding check',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:729; org/nanohttpd/NanoHTTPD.java:1167-1169')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.setKeepAlive', 'CALL', 'Set keep-alive from the HTTP version and connection header',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:730; org/nanohttpd/NanoHTTPD.java:1170-1172')
e('TorrentStreamServer$DLNAFileType.setHeaders', 'NanoHTTPD$Response.setMimeType', 'CALL', 'Set the DLNA file MIME type on the response',
  cls='explicit', evidence='SRC TorrentStreamServer.java:281; org/nanohttpd/NanoHTTPD.java:1296-1298')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.setRequestMethod', 'CALL', 'Record the request method on the response',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:728; org/nanohttpd/NanoHTTPD.java:1299-1301')

# Chunked output: created and finished by the transfer step; the 3-arg
# write is the form sendBody uses on the chunked stream.
e('NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding', 'NanoHTTPD$Response$ChunkedOutputStream.<init>', 'CALL', 'Wrap the output stream for chunked transfer',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1232; org/nanohttpd/NanoHTTPD.java:1066-1068')
e('NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding', 'NanoHTTPD$Response$ChunkedOutputStream.finish', 'CALL', 'Finish the chunked stream after the chunked body',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1234; org/nanohttpd/NanoHTTPD.java:1088-1090')
e('NanoHTTPD$Response.sendBody', 'NanoHTTPD$Response$ChunkedOutputStream.write(byte[],int,int)', 'CALL', 'Write body bytes through the chunked stream',
  cls='non_standard', via='OutputStream virtual dispatch to ChunkedOutputStream in the chunked branch',
  evidence='INFERRED virtual dispatch in the chunked branch; SRC org/nanohttpd/NanoHTTPD.java:1271; org/nanohttpd/NanoHTTPD.java:1081-1087')

# Status enum: first constant use triggers <clinit>, which constructs
# each constant; send reads the description.
e('TorrentStreamServer.handleTorrent', 'NanoHTTPD$Response$Status.<clinit>', 'FRAMEWORK', 'JVM enum initialization before first Status constant use',
  cls='non_standard', via='JVM class initialization before first enum constant use',
  evidence='INFERRED JVM enum initialization; SRC TorrentStreamServer.java:38-44; org/nanohttpd/NanoHTTPD.java:1023-1045')
e('NanoHTTPD$Response$Status.<clinit>', 'NanoHTTPD$Response$Status.<init>', 'FRAMEWORK', 'JVM constructs each Status constant during enum initialization',
  cls='non_standard', via='JVM enum constant construction during <clinit>',
  evidence='INFERRED JVM enum constant construction; SRC org/nanohttpd/NanoHTTPD.java:1047-1050')
e('NanoHTTPD$Response.send', 'NanoHTTPD$Response$Status.getDescription', 'CALL', 'Write the status line description',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1192; org/nanohttpd/NanoHTTPD.java:1052-1054')

# ResponseException: thrown by decodeHeader and execute; execute reads
# the status in its catch path.
e('NanoHTTPD$HTTPSession.decodeHeader', 'NanoHTTPD$ResponseException.<init>(Status,String)', 'CALL', 'Throw a bad-request response exception for malformed headers',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:503,507; org/nanohttpd/NanoHTTPD.java:1309-1312')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$ResponseException.<init>(Status,String)', 'CALL', 'Throw a response exception for a null serve result or bad method',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:710,724; org/nanohttpd/NanoHTTPD.java:1309-1312')
e('NanoHTTPD$HTTPSession.decodeHeader', 'NanoHTTPD$ResponseException.<init>(Status,String,Exception)', 'CALL', 'Throw a response exception with the decoding IOException as cause',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:538; org/nanohttpd/NanoHTTPD.java:1313-1316')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$ResponseException.getStatus', 'CALL', 'Read the exception status to build the error response',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:749; org/nanohttpd/NanoHTTPD.java:1317-1319')

# ServerRunnable: created by createServerRunnable and run by the
# listener thread started in NanoHTTPD.start.
e('NanoHTTPD.createServerRunnable', 'NanoHTTPD$ServerRunnable.<init>', 'CALL', 'Construct the server runnable for the listener thread',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1591; org/nanohttpd/NanoHTTPD.java:1328-1330')
e('NanoHTTPD.start(int,boolean)', 'NanoHTTPD$ServerRunnable.run', 'FRAMEWORK', 'Listener thread runs the server runnable',
  cls='non_standard', via='java.lang.Thread(Runnable).start() calls run()',
  evidence='INFERRED Thread dispatch; SRC org/nanohttpd/NanoHTTPD.java:1817-1820; org/nanohttpd/NanoHTTPD.java:1332-1356')

# Generated mapper: the merged (databinding) mapper ctor constructs and
# registers the libretorrent mapper (bytecode entries in the printed
# appendix), and later databinding requests dispatch through the merged
# mapper to this mapper's dispatch entries. The generated mapper source
# itself is absent from the upload, so every step here is INFERRED.
e('databinding.DataBinderMapperImpl.<init>', 'libretorrent.DataBinderMapperImpl.<clinit>', 'FRAMEWORK', 'JVM class initialization when the merged mapper ctor references the libretorrent mapper',
  cls='non_standard', via='JVM class initialization on first reference',
  evidence='SRC DataBinderMapperImpl.java:5 (bytecode); INFERRED merged-mapper registration')
e('databinding.DataBinderMapperImpl.<init>', 'libretorrent.DataBinderMapperImpl.<init>', 'CALL', 'Construct the libretorrent mapper when the merged mapper is constructed',
  cls='explicit', evidence='SRC DataBinderMapperImpl.java:5 (bytecode); INFERRED merged-mapper registration')
e('databinding.DataBinderMapperImpl.<init>', 'libretorrent.DataBinderMapperImpl.collectDependencies', 'CALL', 'Collect the mapper dependencies during merged-mapper registration',
  cls='non_standard', via='MergedDataBinderMapper.addMapper dispatch to the registered mapper',
  evidence='INFERRED addMapper dispatch during merged-mapper construction; SRC org/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentActivity.java:102')
e('databinding.DataBinderMapperImpl.<init>', 'libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int)', 'CALL', 'Dispatch a View bind request through the merged mapper to this mapper',
  cls='non_standard', via='MergedDataBinderMapper dispatch to the registered mapper',
  evidence='INFERRED merged-mapper dispatch; SRC org/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentActivity.java:102')
e('databinding.DataBinderMapperImpl.<init>', 'libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View[],int)', 'CALL', 'Dispatch a View[] bind request through the merged mapper to this mapper',
  cls='non_standard', via='MergedDataBinderMapper dispatch to the registered mapper',
  evidence='INFERRED merged-mapper dispatch; SRC org/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentActivity.java:102')
e('databinding.DataBinderMapperImpl.<init>', 'libretorrent.DataBinderMapperImpl.getLayoutId', 'CALL', 'Dispatch a layout-id request through the merged mapper to this mapper',
  cls='non_standard', via='MergedDataBinderMapper dispatch to the registered mapper',
  evidence='INFERRED merged-mapper dispatch; SRC org/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentActivity.java:102')

UNREACHABLE.update({
    'NanoHTTPD$Response.getData': ('no_trigger_in_app',
        'Definition at Response.java:1147-1149. sendBody reads this.data directly (:1266-1271), not via getData(). No printed getData() caller exists.',
        'SRC org/nanohttpd/NanoHTTPD.java:1147-1149,1266-1271',
        'SOURCE'),
    'NanoHTTPD$Response.getRequestMethod': ('no_trigger_in_app',
        'Definition at Response.java:1161-1163. The field is written by setRequestMethod (:1299-1301, called from execute :728) and read directly as this.requestMethod in send (:1216, :1231), not via this getter. No printed getter caller exists.',
        'SRC org/nanohttpd/NanoHTTPD.java:1161-1163,1216,1231',
        'SOURCE'),
    'NanoHTTPD$Response.getStatus': ('no_trigger_in_app',
        'Definition at Response.java:1164-1166. Not to be confused with ResponseException.getStatus (:1317, batch-17 row 30). send uses this.status.getDescription() directly (:1192). No printed getter caller exists.',
        'SRC org/nanohttpd/NanoHTTPD.java:1164-1166,1192',
        'SOURCE'),
    'NanoHTTPD$Response.setData': ('no_trigger_in_app',
        'Definition at Response.java:1293-1295. No printed caller; the field is set directly by the Response constructor (:1134-1146) and via newFixedLengthResponse/newChunkedResponse through that constructor.',
        'SRC org/nanohttpd/NanoHTTPD.java:1293-1295,1134-1146',
        'SOURCE'),
    'NanoHTTPD$Response.setStatus': ('no_trigger_in_app',
        'Definition at Response.java:1302-1304. No printed caller; the field is set directly by the Response constructor (:1134).',
        'SRC org/nanohttpd/NanoHTTPD.java:1302-1304,1134',
        'SOURCE'),
    'NanoHTTPD$Response$ChunkedOutputStream.write(int)': ('no_trigger_in_app',
        'Definition at ChunkedOutputStream.java:1070-1075. Its body calls write(data, 0, 1) at :1074 (3-arg form). No printed caller calls write(int) in the files freshly printed.',
        'SRC org/nanohttpd/NanoHTTPD.java:1070-1075,1074',
        'INFERRED'),
    'NanoHTTPD$Response$ChunkedOutputStream.write(byte[])': ('no_trigger_in_app',
        'Definition at ChunkedOutputStream.java:1077-1079. Its body calls write(b, 0, b.length) at :1078 (3-arg form). No printed caller: sendBody uses the 3-arg form at :1271, not this 1-arg byte[] form, and no other freshly printed file calls it on a ChunkedOutputStream.',
        'SRC org/nanohttpd/NanoHTTPD.java:1077-1079,1271',
        'INFERRED'),
    'NanoHTTPD$Response$Status.getRequestStatus': ('no_trigger_in_app',
        'Definition at Status.java:1056-1058 (IStatus.getRequestStatus :1018). No printed caller; send uses getDescription(), not this method.',
        'SRC org/nanohttpd/NanoHTTPD.java:1056-1058,1192',
        'SOURCE'),
    'NanoHTTPD$SecureServerSocketFactory.create': ('no_trigger_in_app',
        'Definition at SecureServerSocketFactory.java:441-455. The only printed installer is makeSecure at :1684 (and setServerSocketFactory at :1672); no printed caller of makeSecure or setServerSocketFactory exists. start :1814 calls getServerSocketFactory().create() virtually, but the factory installed on the printed trunk is the default one (field initializer :1531, DefaultServerSocketFactory.create :426-428).',
        'SRC org/nanohttpd/NanoHTTPD.java:441-455,1684,1672,1814,1531,426-428',
        'SOURCE'),
    'libretorrent.DataBinderMapperImpl.convertBrIdToString': ('no_trigger_in_app',
        'Generated mapper method with no source in the upload. Its only library caller sits behind DataBindingUtil.convertBrIdToString, a documented logging utility the app never invokes; bytecode callers of this method are 0, and an app-source grep for convertBrIdToString finds 0 hits. Unlike collectDependencies, it has no printed library caller on an app-reached path.',
        'INFERRED auto_calls.json callers 0; app-source grep 0 hits; see b017_printed generated-class grep sections',
        'INFERRED'),
})

# No batch-17 UNREACHABLE class has a subclass in the app source
# (Response, ChunkedOutputStream, Status, SecureServerSocketFactory, and
# the generated mapper are never extended), so there are no @Variant
# generated copies beyond the base names. SUPPRESS covers the bytecode
# auto edges into these methods.
SUPPRESS.update({
    'NanoHTTPD$Response.getData',
    'NanoHTTPD$Response.getRequestMethod',
    'NanoHTTPD$Response.getStatus',
    'NanoHTTPD$Response.setData',
    'NanoHTTPD$Response.setStatus',
    'NanoHTTPD$Response$ChunkedOutputStream.write(int)',
    'NanoHTTPD$Response$ChunkedOutputStream.write(byte[])',
    'NanoHTTPD$Response$Status.getRequestStatus',
    'NanoHTTPD$SecureServerSocketFactory.create',
    'libretorrent.DataBinderMapperImpl.convertBrIdToString',
})
