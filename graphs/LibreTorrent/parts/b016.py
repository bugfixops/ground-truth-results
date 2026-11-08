# Citation-form rework 2026-11-01: evidence citations whose path contains a core/services/data/libcore/packages component rewritten to basename-only form; labels, kinds, edges, endpoints, SUPPRESS entries and line ranges unchanged; full relative paths remain in the .md and printed files.
# C02 converter delivery (2026-11-01) — batch 16, from audited A3 base part.
# Full-repo greps for every UNREACHABLE row: parts-staging/grep/16/ (one file per row, triaged; no live caller found, no label flipped).
# STRONGER-EVIDENCE UPGRADES (mandatory rule; tree graph_def.py inline grade SOURCE > part INFERRED): 16 key(s) INFERRED -> SOURCE:
#   UPGRADED NanoHTTPD$CookieHandler.set(String,String,int) (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$CookieHandler.set(Cookie) (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$DefaultTempFile.<init> (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$DefaultTempFile.delete (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$DefaultTempFile.getName (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$DefaultTempFileManager.createTempFile (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$HTTPSession.decodeMultipartFormData (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$HTTPSession.getAttributeFromContentHeader (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$HTTPSession.getBodySize (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$HTTPSession.getBoundaryPositions (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$HTTPSession.getMethod (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$HTTPSession.getQueryParameterString (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$HTTPSession.getTmpBucket (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$HTTPSession.parseBody (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$HTTPSession.saveTmpFile (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
#   UPGRADED NanoHTTPD$HTTPSession.scipOverNewLine (tree: SOURCE; merge-ready: INFERRED; kind/reason/ref unchanged)
# HARNESS NOTE: check_part.py compares part grade to merge-ready grade with equality, so each upgrade above
#   produces exactly one 'confirmed_by mismatch' FAIL line in the harness run. All other harness checks pass.
#   The upgrade is deliberate (user order 2026-11-01 ~18:41: keep stronger evidence; b001/b002 SOURCE 617->578->503
#   regression must not repeat). Merger/auditor waiver required for those FAIL lines, or patch the harness to
#   accept SOURCE where the tree holds SOURCE. Do NOT revert these grades to INFERRED at merge.
# Batch 16 part (NanoHTTPD remainder: CookieHandler setters,
# DefaultAsyncRunner, DefaultServerSocketFactory, DefaultTempFile and
# DefaultTempFileManager and factory, HTTPSession, Method, Response).
# Hand-written edges, UNREACHABLE entries and SUPPRESS strings only. Each
# evidence string cites lines printed in
# graphs/LibreTorrent/scratch/b016_printed.txt.
#
# Pre-existing routes are NOT repeated here; they are listed with line refs
# in parts/b016.md Dependencies (none: no batch-16 REACHABLE row already has
# an incoming edge in graph_def.py).

# CookieHandler: unloadQueue runs from execute; the setters do not.
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$CookieHandler.unloadQueue', 'CALL', 'Flush queued cookies into the response headers',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:727; org/nanohttpd/NanoHTTPD.java:294-297')

# Async runner and socket factory: installed by the NanoHTTPD ctor and
# driven by start/stop and the listener thread.
e('NanoHTTPD.<init>(String,int)', 'NanoHTTPD$DefaultAsyncRunner.<init>', 'CALL', 'Install the default async runner',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1561')
e('NanoHTTPD.stop', 'NanoHTTPD$DefaultAsyncRunner.closeAll', 'CALL', 'Close all running client handlers on stop',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1840; org/nanohttpd/NanoHTTPD.java:319-324')
e('NanoHTTPD$ClientHandler.run', 'NanoHTTPD$DefaultAsyncRunner.closed', 'CALL', 'Deregister the finished client handler',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:192; org/nanohttpd/NanoHTTPD.java:326-328')
e('NanoHTTPD$ServerRunnable.run', 'NanoHTTPD$DefaultAsyncRunner.exec', 'CALL', 'Hand the accepted client to the async runner',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1347; org/nanohttpd/NanoHTTPD.java:330-336')
e('TorrentStreamServer.<init>', 'NanoHTTPD$DefaultServerSocketFactory.<init>', 'CALL', 'Install the default server socket factory at construction',
  cls='non_standard', via='JVM field initialization during superclass construction',
  evidence='INFERRED field initialization during construction; SRC org/nanohttpd/NanoHTTPD.java:1531; TorrentStreamServer.java:67-69')
e('NanoHTTPD.start(int,boolean)', 'NanoHTTPD$DefaultServerSocketFactory.create', 'CALL', 'Create the listening server socket',
  cls='non_standard', via='ServerSocketFactory interface dispatch to DefaultServerSocketFactory',
  evidence='INFERRED interface dispatch; SRC org/nanohttpd/NanoHTTPD.java:1814; org/nanohttpd/NanoHTTPD.java:426-428')

# Temp files: the manager and its factory run on the live path; the
# createTempFile subtree runs only from the dead parseBody path.
e('NanoHTTPD$DefaultTempFileManagerFactory.create', 'NanoHTTPD$DefaultTempFileManager.<init>', 'CALL', 'Create the per-client temp file manager',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:413-415; org/nanohttpd/NanoHTTPD.java:383-390')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$DefaultTempFileManager.clear', 'CALL', 'Clear temp files when the session finishes',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:754; org/nanohttpd/NanoHTTPD.java:391-401')
e('NanoHTTPD.<init>(String,int)', 'NanoHTTPD$DefaultTempFileManagerFactory.<init>', 'CALL', 'Install the default temp file manager factory',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1560')
e('NanoHTTPD$ClientHandler.run', 'NanoHTTPD$DefaultTempFileManagerFactory.create', 'CALL', 'Create the temp file manager for this client',
  cls='non_standard', via='TempFileManagerFactory interface dispatch to DefaultTempFileManagerFactory',
  evidence='INFERRED interface dispatch; SRC org/nanohttpd/NanoHTTPD.java:172; org/nanohttpd/NanoHTTPD.java:413-415')

# HTTPSession: constructed and executed by ClientHandler.run; its
# decode/getter methods run on the live serve path, while the parseBody
# subtree never runs because base serve is overridden.
e('NanoHTTPD$ClientHandler.run', 'NanoHTTPD$HTTPSession.<init>(NanoHTTPD,TempFileManager,InputStream,OutputStream,InetAddress)', 'CALL', 'Create the session for this client connection',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:173; org/nanohttpd/NanoHTTPD.java:484-492')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$HTTPSession.decodeHeader', 'CALL', 'Decode the request header into parms and headers',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:703; org/nanohttpd/NanoHTTPD.java:494-540')
e('NanoHTTPD$HTTPSession.decodeHeader', 'NanoHTTPD$HTTPSession.decodeParms', 'CALL', 'Decode the query string parameters',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:513; org/nanohttpd/NanoHTTPD.java:637-653')
e('NanoHTTPD$ClientHandler.run', 'NanoHTTPD$HTTPSession.execute', 'CALL', 'Execute the session in the keep-alive loop',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:175; org/nanohttpd/NanoHTTPD.java:655-760')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$HTTPSession.findHeaderEnd', 'CALL', 'Find the byte index separating header from body',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:683; org/nanohttpd/NanoHTTPD.java:761-780')
e('TorrentStreamServer.handleTorrent', 'NanoHTTPD$HTTPSession.getHeaders', 'CALL', 'Read the request headers for torrent handling',
  cls='explicit', evidence='SRC TorrentStreamServer.java:150; org/nanohttpd/NanoHTTPD.java:821-823')
e('TorrentStreamServer.handleTorrent', 'NanoHTTPD$HTTPSession.getParms', 'CALL', 'Read the request parameters for torrent handling',
  cls='explicit', evidence='SRC TorrentStreamServer.java:132; org/nanohttpd/NanoHTTPD.java:833-835')
e('TorrentStreamServer.serve', 'NanoHTTPD$HTTPSession.getUri', 'CALL', 'Read the request URI to route the serve call',
  cls='explicit', evidence='SRC TorrentStreamServer.java:113; org/nanohttpd/NanoHTTPD.java:849-851')
e('TorrentStreamServer.handleTorrent', 'NanoHTTPD$HTTPSession.getUri', 'CALL', 'Read the request URI to check the stream path',
  cls='explicit', evidence='SRC TorrentStreamServer.java:129; org/nanohttpd/NanoHTTPD.java:849-851')

# Method enum and Response: first Method use triggers enum init and the
# lookup; Response objects are built by the fixed-length factory and
# their headers/close run on the live path.
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Method.<clinit>', 'FRAMEWORK', 'JVM enum initialization before first Method use',
  cls='non_standard', via='JVM class initialization before first enum use',
  evidence='INFERRED JVM class initialization; SRC org/nanohttpd/NanoHTTPD.java:708; org/nanohttpd/NanoHTTPD.java:993-1001')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Method.lookup', 'CALL', 'Look up the request method enum value',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:708; org/nanohttpd/NanoHTTPD.java:1003-1014')
e('NanoHTTPD.newFixedLengthResponse(IStatus,String,InputStream,long)', 'NanoHTTPD$Response.<init>', 'CALL', 'Build the fixed-length response object',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:1697; org/nanohttpd/NanoHTTPD.java:1122-1135')
e('NanoHTTPD$CookieHandler.unloadQueue', 'NanoHTTPD$Response.addHeader', 'CALL', 'Add each queued cookie as a Set-Cookie header',
  cls='explicit', evidence='SRC org/nanohttpd/NanoHTTPD.java:296; org/nanohttpd/NanoHTTPD.java:1144-1146')
e('TorrentStreamServer$DLNAFileType.setHeaders', 'NanoHTTPD$Response.addHeader', 'CALL', 'Add the DLNA headers for mp4/avi/mkv responses',
  cls='explicit', evidence='SRC TorrentStreamServer.java:277-280; org/nanohttpd/NanoHTTPD.java:1144-1146')
e('NanoHTTPD$HTTPSession.execute', 'NanoHTTPD$Response.close', 'CALL', 'Close the response in the session finally block via safeClose',
  cls='non_standard', via='safeClose virtual dispatch to Closeable.close()',
  evidence='INFERRED virtual dispatch through safeClose; SRC org/nanohttpd/NanoHTTPD.java:753; org/nanohttpd/NanoHTTPD.java:1136-1143')

UNREACHABLE.update({
    'NanoHTTPD$CookieHandler.set(String,String,int)': ('no_trigger_in_app',
        'Definition at CookieHandler.java:283-285 (new Cookie + getHTTPTime at :284). Its only printed caller is delete :253, and delete has no printed caller (batch 15 row 38).',
        'SRC org/nanohttpd/NanoHTTPD.java:283-285,252-254',
        'SOURCE'),
    'NanoHTTPD$CookieHandler.set(Cookie)': ('no_trigger_in_app',
        'Definition at CookieHandler.java:270-272 (queue.add). No printed caller at all in the fresh corpus.',
        'SRC org/nanohttpd/NanoHTTPD.java:270-272',
        'SOURCE'),
    'NanoHTTPD$DefaultTempFile.<init>': ('no_trigger_in_app',
        'Definition at DefaultTempFile.java:350-353 (File.createTempFile at :351). It is constructed only by DefaultTempFileManager.createTempFile :402-406, which is called only from the parseBody subtree (getTmpBucket :842, saveTmpFile :949); parseBody never runs in the app path.',
        'SRC org/nanohttpd/NanoHTTPD.java:350-353,402-406,842,949',
        'SOURCE'),
    'NanoHTTPD$DefaultTempFile.delete': ('branch_never_taken',
        'Definition at DefaultTempFile.java:355-360 (safeClose fstream, file.delete). Its caller DefaultTempFileManager.clear() :391-401 does run (HTTPSession.execute finally :754), but clear iterates tempFiles, which gains entries only via createTempFile (dead path above), so the loop never iterates in the printed app path.',
        'SRC org/nanohttpd/NanoHTTPD.java:355-360,391-401,754',
        'SOURCE'),
    'NanoHTTPD$DefaultTempFile.getName': ('no_trigger_in_app',
        'Definition at DefaultTempFile.java:362-364 (file.getAbsolutePath()). Printed callers are getTmpBucket :843 and saveTmpFile :951/:955, both in the dead parseBody subtree.',
        'SRC org/nanohttpd/NanoHTTPD.java:362-364,843,951,955',
        'SOURCE'),
    'NanoHTTPD$DefaultTempFileManager.createTempFile': ('no_trigger_in_app',
        'Definition at DefaultTempFileManager.java:402-406 (new DefaultTempFile, tempFiles.add). Printed callers are getTmpBucket :842 and saveTmpFile :949, both in the dead parseBody subtree.',
        'SRC org/nanohttpd/NanoHTTPD.java:402-406,842,949',
        'SOURCE'),
    'NanoHTTPD$HTTPSession.decodeMultipartFormData': ('no_trigger_in_app',
        'Definition at HTTPSession.java:544+. Its only printed caller is parseBody :913, which never runs in the app path.',
        'SRC org/nanohttpd/NanoHTTPD.java:544,913',
        'SOURCE'),
    'NanoHTTPD$HTTPSession.getAttributeFromContentHeader': ('no_trigger_in_app',
        'Definition at HTTPSession.java:936+. Its only printed callers are parseBody :913/:914, which never runs in the app path.',
        'SRC org/nanohttpd/NanoHTTPD.java:936,913,914',
        'SOURCE'),
    'NanoHTTPD$HTTPSession.getBodySize': ('no_trigger_in_app',
        'Definition at HTTPSession.java:856+. Its only printed caller is parseBody :868 (the :717 TODO comment is not a call); parseBody never runs in the app path.',
        'SRC org/nanohttpd/NanoHTTPD.java:856,868',
        'SOURCE'),
    'NanoHTTPD$HTTPSession.getBoundaryPositions': ('no_trigger_in_app',
        'Definition at HTTPSession.java:781+. Its only printed caller is decodeMultipartFormData :546, which is itself parseBody-only.',
        'SRC org/nanohttpd/NanoHTTPD.java:781,546',
        'SOURCE'),
    'NanoHTTPD$HTTPSession.getMethod': ('no_trigger_in_app',
        'Definition at HTTPSession.java:829+. Its only printed caller is base serve(IHTTPSession) :1734, which TorrentStreamServer overrides and never calls via super; TorrentStreamServer.handleTorrent never calls getMethod.',
        'SRC org/nanohttpd/NanoHTTPD.java:829,1734; TorrentStreamServer.java:111-120',
        'SOURCE'),
    'NanoHTTPD$HTTPSession.getQueryParameterString': ('no_trigger_in_app',
        'Definition at HTTPSession.java:837+. Its only printed caller is base serve(IHTTPSession) :1745, which TorrentStreamServer overrides and never calls via super; TorrentStreamServer parses params via getParms, not the query string.',
        'SRC org/nanohttpd/NanoHTTPD.java:837,1745',
        'SOURCE'),
    'NanoHTTPD$HTTPSession.getTmpBucket': ('no_trigger_in_app',
        'Definition at HTTPSession.java:840-844 (createTempFile :842, getName :843). Its only printed caller is parseBody :876, which never runs in the app path.',
        'SRC org/nanohttpd/NanoHTTPD.java:840-844,876',
        'SOURCE'),
    'NanoHTTPD$HTTPSession.parseBody': ('no_trigger_in_app',
        'Definition at HTTPSession.java:865+. Its only printed caller is base serve(IHTTPSession) :1737 (PUT/POST branch), which TorrentStreamServer overrides and never calls via super; the full TorrentStreamServer.java (284 lines) contains no parseBody call. If a saved grep finds a live parseBody caller, this row and rows 10, 12, 15, 20, 24, 25, 26, 31, 34, 35 must be re-judged together.',
        'SRC org/nanohttpd/NanoHTTPD.java:865,1737; TorrentStreamServer.java:111-120',
        'SOURCE'),
    'NanoHTTPD$HTTPSession.saveTmpFile': ('no_trigger_in_app',
        'Definition at HTTPSession.java:944+ (createTempFile :949, getName :951/:955). Printed callers are decodeMultipartFormData :606 and parseBody :930, both in the dead parseBody subtree.',
        'SRC org/nanohttpd/NanoHTTPD.java:944,606,930',
        'SOURCE'),
    'NanoHTTPD$HTTPSession.scipOverNewLine': ('no_trigger_in_app',
        'Definition at HTTPSession.java:625+. Its only printed caller is decodeMultipartFormData :590, which is itself parseBody-only.',
        'SRC org/nanohttpd/NanoHTTPD.java:625,590',
        'SOURCE'),
})

# No batch-16 UNREACHABLE class has a subclass in the app source
# (HTTPSession, DefaultTempFile, DefaultTempFileManager, and CookieHandler
# are never extended), so there are no @Variant generated copies beyond
# the base names. SUPPRESS covers the bytecode auto edges into these
# methods, including base serve -> parseBody (:1737), base serve ->
# getMethod/:getQueryParameterString, parseBody-subtree internal calls,
# and delete -> set(String,String,int) (:253).
SUPPRESS.update({
    'NanoHTTPD$CookieHandler.set(String,String,int)',
    'NanoHTTPD$CookieHandler.set(Cookie)',
    'NanoHTTPD$DefaultTempFile.<init>',
    'NanoHTTPD$DefaultTempFile.delete',
    'NanoHTTPD$DefaultTempFile.getName',
    'NanoHTTPD$DefaultTempFileManager.createTempFile',
    'NanoHTTPD$HTTPSession.decodeMultipartFormData',
    'NanoHTTPD$HTTPSession.getAttributeFromContentHeader',
    'NanoHTTPD$HTTPSession.getBodySize',
    'NanoHTTPD$HTTPSession.getBoundaryPositions',
    'NanoHTTPD$HTTPSession.getMethod',
    'NanoHTTPD$HTTPSession.getQueryParameterString',
    'NanoHTTPD$HTTPSession.getTmpBucket',
    'NanoHTTPD$HTTPSession.parseBody',
    'NanoHTTPD$HTTPSession.saveTmpFile',
    'NanoHTTPD$HTTPSession.scipOverNewLine',
})
