# Batch 17 part (NanoHTTPD Response, ChunkedOutputStream, Status,
# ResponseException, SecureServerSocketFactory, ServerRunnable). Hand-written
# edges and UNREACHABLE entries only. Each evidence string cites lines printed
# in graphs/LibreTorrent/scratch/b017_printed.txt. Source paths are relative to
# final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/.
#
# The 7 libretorrent.DataBinderMapperImpl rows (TSV rows 644-650) are OPEN and
# have no entries here (generated class, no source in upload; see
# scratch/b017_generated_grep.txt).
#
# Route steps owned by other batches are written here so that each batch-17
# route is complete. The entry chain is already in graph_def.py: S_ENTRY ->
# MainActivity.onCreate (106), MainActivity.onStart -> subscribeNeedStartEngine
# (134), subscribeNeedStartEngine -> lambda$subscribeNeedStartEngine$8 (1824-1832),
# which calls MainViewModel.startEngine.

# ---- App start chain: MainViewModel -> TorrentEngine -> TorrentService -> session ----

e('MainViewModel.startEngine', 'TorrentEngine.start', 'CALL', 'Start the engine from the view model',
  cls='explicit', evidence='SRC org/proninyaroslav/libretorrent/ui/main/MainViewModel.java:158-159')

e('TorrentService.init', 'TorrentEngine.doStart', 'CALL', 'Start the engine core from the service init',
  cls='explicit', evidence='SRC org/proninyaroslav/libretorrent/service/TorrentService.java:116-117,131')

e('TorrentEngine.doStart', 'TorrentSessionImpl.start', 'CALL', 'Start the libtorrent session',
  cls='non_standard', via='TorrentSession interface field (TorrentEngine.java:100); TorrentSessionImpl implements it',
  evidence='SRC org/proninyaroslav/libretorrent/core/model/TorrentEngine.java:100,234-235,259; INFERRED interface dispatch to org/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl.java:862-863')

# ---- Session start -> engine listener -> streaming server start ----

e('TorrentSessionImpl.start', 'TorrentSessionImpl.onAfterStart', 'FRAMEWORK', 'libtorrent session start calls the onAfterStart hook',
  cls='non_standard', via='libtorrent4j SessionManager.start(SessionParams) calls the protected onAfterStart hook (library, not in upload)',
  evidence='INFERRED libtorrent4j SessionManager.start calls onAfterStart; SRC org/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl.java:907,990-991')

e('TorrentSessionImpl.onAfterStart', 'TorrentSessionImpl.lambda$onAfterStart$4', 'FRAMEWORK', 'Completable runs the notify lambda on the io scheduler',
  cls='non_standard', via='RxJava Completable.fromRunnable runs the Runnable on Schedulers.io() (library, not in upload)',
  evidence='INFERRED RxJava Completable.fromRunnable runs the lambda on subscribe; SRC org/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl.java:1009-1012')

e('TorrentSessionImpl.lambda$onAfterStart$4', 'TorrentSessionImpl.notifyListeners', 'CALL', 'Notify the registered engine listeners that the session started',
  cls='explicit', evidence='SRC org/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl.java:1009-1010')

e('TorrentSessionImpl.notifyListeners', 'TorrentEngine$5.onSessionStarted', 'CALL', 'Deliver onSessionStarted to the listener TorrentEngine registered',
  cls='standard', evidence='SRC org/proninyaroslav/libretorrent/core/model/session/TorrentSessionImpl.java:1447-1449; org/proninyaroslav/libretorrent/core/model/TorrentEngine.java:140,1265-1269; INFERRED anonymous class numbering gives TorrentEngine$5 (TSV lists TorrentEngine$5.lambda$onIpFilterParsed$8)')

e('TorrentEngine$5.onSessionStarted', 'TorrentEngine.handleOnSessionStarted', 'CALL', 'Handle session start in the engine',
  cls='explicit', evidence='SRC org/proninyaroslav/libretorrent/core/model/TorrentEngine.java:1267-1268')

e('TorrentEngine.handleOnSessionStarted', 'TorrentEngine.startStreamingServer', 'CALL', 'Start the streaming server when streaming is enabled',
  guard='if (enableStreaming): settings value pref_key_streaming_enable, default true',
  cls='explicit', evidence='SRC org/proninyaroslav/libretorrent/core/model/TorrentEngine.java:1056-1058; org/proninyaroslav/libretorrent/core/settings/SettingsRepositoryImpl.java:163,1265-1270')

e('TorrentEngine.startStreamingServer', 'TorrentStreamServer.start', 'CALL', 'Start the streaming HTTP server',
  cls='explicit', evidence='SRC org/proninyaroslav/libretorrent/core/model/TorrentEngine.java:1069-1071')

e('TorrentStreamServer.start', 'NanoHTTPD.start()', 'CALL', 'Start the NanoHTTPD base server',
  cls='explicit', evidence='SRC org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java:76-78')

# ---- NanoHTTPD start chain and listener thread ----

e('NanoHTTPD.start()', 'NanoHTTPD.start(int)', 'CALL', 'Start with the default socket read timeout',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1794-1795')

e('NanoHTTPD.start(int)', 'NanoHTTPD.start(int,boolean)', 'CALL', 'Start with the daemon flag',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1800-1801')

e('NanoHTTPD.start(int,boolean)', 'NanoHTTPD.createServerRunnable', 'CALL', 'Create the server runnable for the listener thread',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1814-1816')

e('NanoHTTPD.createServerRunnable', 'NanoHTTPD$ServerRunnable.<init>', 'CALL', 'Construct the server runnable',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1590-1591')

e('NanoHTTPD.start(int,boolean)', 'NanoHTTPD$ServerRunnable.run', 'FRAMEWORK', 'Listener thread runs the server runnable',
  cls='standard', evidence='INFERRED java.lang.Thread(Runnable).start() calls run(); SRC org/nanohttpd/NanoHTTPD.java:1817-1820')

e('NanoHTTPD$ServerRunnable.run', 'NanoHTTPD.createClientHandler', 'CALL', 'Create a client handler for each accepted socket',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1342-1347,1579-1581')

e('NanoHTTPD$ServerRunnable.run', 'NanoHTTPD$DefaultAsyncRunner.exec', 'CALL', 'Hand the accepted client to the async runner',
  cls='non_standard', via='AsyncRunner interface field asyncRunner; default DefaultAsyncRunner set in the NanoHTTPD constructor',
  evidence='INFERRED interface dispatch to DefaultAsyncRunner; SRC org/nanohttpd/NanoHTTPD.java:1347,1558-1561')

e('NanoHTTPD$DefaultAsyncRunner.exec', 'NanoHTTPD$ClientHandler.run', 'FRAMEWORK', 'Request processor thread runs the client handler',
  cls='standard', evidence='INFERRED java.lang.Thread(Runnable).start() calls run(); SRC org/nanohttpd/NanoHTTPD.java:332,336')

e('NanoHTTPD$ClientHandler.run', 'NanoHTTPD$HTTPSession.execute', 'CALL', 'Execute one HTTP request on the client session',
  guard='while (!this.acceptSocket.isClosed())', cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:173-175')

# ---- Request path: HTTPSession.execute and error paths ----

e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$HTTPSession.decodeHeader', 'CALL', 'Parse the request line and headers',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:703')

e('NanoHTTPD$HTTPSession.decodeHeader', 'NanoHTTPD$ResponseException.<init>(Status,String)', 'CALL', 'Report an empty request line or missing URI as BAD_REQUEST',
  guard='request line has no tokens, or the URI token is missing', cls='explicit',
  evidence='SRC org/nanohttpd/NanoHTTPD.java:502-507')

e('NanoHTTPD$HTTPSession.decodeHeader', 'NanoHTTPD$ResponseException.<init>(Status,String,Exception)', 'CALL', 'Report an IOException while reading the header as INTERNAL_ERROR',
  guard='IOException while reading the request header', cls='explicit',
  evidence='SRC org/nanohttpd/NanoHTTPD.java:537-538')

e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$ResponseException.<init>(Status,String)', 'CALL', 'Report an unparseable request method as BAD_REQUEST',
  guard='if (this.method == null)', cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:708-710')

e('NanoHTTPD$HTTPSession.execute', 'TorrentStreamServer.serve', 'CALL', 'Serve the request through the app override',
  cls='non_standard', via='virtual call serve(this) dispatches to the TorrentStreamServer override of serve(IHTTPSession)',
  evidence='SRC org/nanohttpd/NanoHTTPD.java:720; org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java:110-111')

e('TorrentStreamServer.serve', 'TorrentStreamServer.handleTorrent', 'CALL', 'Build the response for the requested torrent file',
  cls='explicit', evidence='SRC org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java:117')

e('TorrentStreamServer.serve', 'TorrentStreamServer$DLNAFileType.setHeaders', 'CALL', 'Add DLNA headers for a known file extension',
  guard='if (fileType != null)', cls='explicit',
  evidence='SRC org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java:115,118-119')

e('TorrentStreamServer$DLNAFileType.setHeaders', 'NanoHTTPD$Response.setMimeType', 'CALL', 'Set the DLNA file MIME type on the response',
  cls='explicit', evidence='SRC org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java:275-281')

e('TorrentStreamServer.handleTorrent', 'NanoHTTPD$Response$Status.<clinit>', 'FRAMEWORK', 'First use of a Status constant initializes the enum',
  cls='non_standard', via='JVM class initialization on first active use of Status (no app code calls <clinit>)',
  evidence='INFERRED JVM class initialization; SRC org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java:38-44,126-127')

e('NanoHTTPD$Response$Status.<clinit>', 'NanoHTTPD$Response$Status.<init>', 'CALL', 'Construct each enum constant',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1023-1025,1047')

e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.send', 'CALL', 'Send the response to the client',
  guard='else branch of if (r == null)', cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:720-731')

e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.setRequestMethod', 'CALL', 'Record the request method on the response',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:728')

e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD.useGzipWhenAccepted', 'CALL', 'Decide whether gzip is allowed for this response',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:729')

e('NanoHTTPD.useGzipWhenAccepted', 'NanoHTTPD$Response.getMimeType', 'CALL', 'Read the MIME type to decide on gzip',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1660-1661')

e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.setGzipEncoding', 'CALL', 'Set gzip encoding from MIME type and Accept-Encoding',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:726,729')

e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.setKeepAlive', 'CALL', 'Set keep-alive on the response',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:730')

e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.getHeader', 'CALL', 'Read the Connection header to decide on shutdown',
  guard='keepAlive is true (the !keepAlive test short-circuits when keepAlive is false)', cls='explicit',
  evidence='SRC org/nanohttpd/NanoHTTPD.java:733')

e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$ResponseException.getStatus', 'CALL', 'Read the status of a caught ResponseException',
  guard='catch (ResponseException re)', cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:748-749')

# ---- Response.send and body writing ----

e('NanoHTTPD$Response.send', 'NanoHTTPD$Response.headerAlreadySent', 'CALL', 'Check whether a content-length header was already set',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1208-1209')

e('NanoHTTPD$Response.send', 'NanoHTTPD$Response$Status.getDescription', 'CALL', 'Write the HTTP status line',
  cls='non_standard', via='IStatus interface dispatch: field status is IStatus (NanoHTTPD.java:1095) and Status implements IStatus',
  evidence='INFERRED interface dispatch; SRC org/nanohttpd/NanoHTTPD.java:1095,1192')

e('NanoHTTPD$Response.send', 'NanoHTTPD$Response.setChunkedTransfer', 'CALL', 'Use chunked transfer when gzip is applied',
  guard='if (encodeAsGzip)', cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1211-1213')

e('NanoHTTPD$Response.send', 'NanoHTTPD$Response.sendContentLengthHeaderIfNotAlreadyPresent', 'CALL', 'Write the content-length header for a plain body',
  guard='else if (!encodeAsGzip) after the chunked test fails', cls='explicit',
  evidence='SRC org/nanohttpd/NanoHTTPD.java:1216-1219')

e('NanoHTTPD$Response.send', 'NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding', 'CALL', 'Send the body with the selected transfer and encoding',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1223')

e('NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding', 'NanoHTTPD$Response$ChunkedOutputStream.<init>', 'CALL', 'Wrap the socket stream for chunked output',
  guard='if (this.requestMethod != Method.HEAD && this.chunkedTransfer)', cls='explicit',
  evidence='SRC org/nanohttpd/NanoHTTPD.java:1231-1232')

e('NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding', 'NanoHTTPD$Response$ChunkedOutputStream.finish', 'CALL', 'Write the chunked terminator',
  guard='if (this.requestMethod != Method.HEAD && this.chunkedTransfer)', cls='explicit',
  evidence='SRC org/nanohttpd/NanoHTTPD.java:1231-1234')

e('NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding', 'NanoHTTPD$Response.sendBodyWithCorrectEncoding', 'CALL', 'Send the body through the encoding step',
  guard='chunked branch (line 1233) or plain branch (line 1236)', cls='explicit',
  evidence='SRC org/nanohttpd/NanoHTTPD.java:1231-1237')

e('NanoHTTPD$Response.sendBodyWithCorrectEncoding', 'NanoHTTPD$Response.sendBody', 'CALL', 'Copy the body bytes to the output',
  guard='if (encodeAsGzip): gzip branch (1242); else plain branch (1245)', cls='explicit',
  evidence='SRC org/nanohttpd/NanoHTTPD.java:1240-1245')

e('NanoHTTPD$Response.sendBodyWithCorrectEncoding', 'NanoHTTPD$Response$ChunkedOutputStream.write(byte[])', 'FRAMEWORK', 'GZIP header is written through the chunked stream',
  guard='if (encodeAsGzip)', cls='non_standard',
  via='java.util.zip.GZIPOutputStream constructor writes its header with out.write(byte[]) (JDK, not in upload)',
  evidence='INFERRED GZIPOutputStream(OutputStream) header write; SRC org/nanohttpd/NanoHTTPD.java:1240-1241')

e('NanoHTTPD$Response$ChunkedOutputStream.write(byte[])', 'NanoHTTPD$Response$ChunkedOutputStream.write(byte[],int,int)', 'CALL', 'Delegate the byte array write',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1077-1078')

e('NanoHTTPD$Response.sendBody', 'NanoHTTPD$Response$ChunkedOutputStream.write(byte[],int,int)', 'FRAMEWORK', 'Compressed body bytes reach the chunked stream',
  guard='if (encodeAsGzip) and chunked transfer', cls='non_standard',
  via='GZIPOutputStream/DeflaterOutputStream writes deflated bytes to the wrapped stream with write(b,off,len) (JDK, not in upload)',
  evidence='INFERRED java.util.zip DeflaterOutputStream.deflate writes via out.write(b,off,len); SRC org/nanohttpd/NanoHTTPD.java:1271')

# ---- UNREACHABLE: no caller in the app or in NanoHTTPD (printed greps in scratch/b017_printed.txt) ----

UNREACHABLE.update({
    'NanoHTTPD$Response.getData': ('no_trigger_in_app', 'No call to getData() exists in NanoHTTPD.java or the app; send and sendBody read the data field directly.', 'SRC org/nanohttpd/NanoHTTPD.java:1147-1149; grep getData( over NanoHTTPD.java finds only the definition', 'SOURCE'),
    'NanoHTTPD$Response.getRequestMethod': ('no_trigger_in_app', 'No call to getRequestMethod() exists; send reads the requestMethod field directly.', 'SRC org/nanohttpd/NanoHTTPD.java:1161-1163,1216,1231; grep getRequestMethod() finds only the definition', 'SOURCE'),
    'NanoHTTPD$Response.getStatus': ('no_trigger_in_app', 'No call to Response.getStatus() exists; the getStatus() calls at 749 and 1741 are on ResponseException.', 'SRC org/nanohttpd/NanoHTTPD.java:1164-1165,749,1741; grep getStatus() finds no Response call', 'SOURCE'),
    'NanoHTTPD$Response.setData': ('no_trigger_in_app', 'No call to setData() exists; responses are built with constructors.', 'SRC org/nanohttpd/NanoHTTPD.java:1293-1295; grep setData( finds only the definition', 'SOURCE'),
    'NanoHTTPD$Response.setStatus': ('no_trigger_in_app', 'No call to setStatus() exists; the status is set in the constructor.', 'SRC org/nanohttpd/NanoHTTPD.java:1302-1303; grep setStatus( finds only the definition', 'SOURCE'),
    'NanoHTTPD$Response$ChunkedOutputStream.write(int)': ('no_trigger_in_app', 'No caller passes one int to a ChunkedOutputStream; the GZIP path uses write(byte[]) and write(byte[],int,int).', 'SRC org/nanohttpd/NanoHTTPD.java:1070-1075; write( calls at 885,954,1074,1078,1085-1089,1271', 'SOURCE'),
    'NanoHTTPD$Response$Status.getRequestStatus': ('no_trigger_in_app', 'No call to getRequestStatus() exists in NanoHTTPD.java or the app.', 'SRC org/nanohttpd/NanoHTTPD.java:1018,1055-1058; grep getRequestStatus finds no call', 'SOURCE'),
    'NanoHTTPD$SecureServerSocketFactory.create': ('no_trigger_in_app', 'Installed only by makeSecure, which has no caller under the source root; the default factory is DefaultServerSocketFactory.', 'SRC org/nanohttpd/NanoHTTPD.java:441-446,1531,1684-1685; grep makeSecure over the source root finds only the definition', 'SOURCE'),
})
