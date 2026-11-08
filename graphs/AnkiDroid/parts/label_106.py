# AnkiDroid batch 106 (LABEL helper). TextImporter (4 methods), FullSyncer (4), HttpSyncer (26) and
# HttpSyncer$ProgressByteEntity (6). The full row list is in graphs/AnkiDroid/parts/label_106.md.
#
# Route ownership:
# - Automatic CALL edges from auto_calls.json are not repeated here. Exact CALL pairs whose target is a base
#   HttpSyncer method that the runtime receiver overrides point at the wrong node; they are named as suppress
#   candidates in the final answer (Connection.java:202, 322, 337; Syncer.java:89, 157, 170, 179, 197, 204, 212, 909).
#   The MediaSyncer.java:108 pair to base finish is live (RemoteMediaServer does not override finish).
# - The three FRAMEWORK edges start from the base req(...CancelCallback) node. The receiver variants
#   (@FullSyncer, @RemoteMediaServer) do not get them here.
#
# Gate: ENV_NETWORK on the three FRAMEWORK edges. No MG id is used and no MISSING GATE note is needed.

# --- ProgressByteEntity callbacks reached from the HTTP client while it sends the request body (req, HttpSyncer.java:210-236).
e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'HttpSyncer$ProgressByteEntity.writeTo', 'FRAMEWORK',
  'the HTTP client sends the request and writes the multipart body through the request entity',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:210, 213, 235-236; INFERRED (Apache HttpClient 4.x source not read)',
  note='The request entity is set at HttpSyncer.java:213 and executed at :236. The body is written by writeTo (HttpSyncer.java:393-406), which calls publishProgress (:400). The library dispatch is INFERRED (library source not read).')

e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'HttpSyncer$ProgressByteEntity.getContentLength', 'FRAMEWORK',
  'the HTTP client reads the request body length for the Content-Length header while it sends the request',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:210, 213, 235-236; INFERRED (Apache HttpClient 4.x source not read)',
  note='getContentLength returns mLength (HttpSyncer.java:416-418), set from the temp file length in the constructor (:383). The library dispatch is INFERRED (library source not read).')

e('HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)', 'HttpSyncer$ProgressByteEntity.isRepeatable', 'FRAMEWORK',
  'the HTTP client asks whether the request body can be replayed when it retries or re-authenticates the request',
  env=ENV_NETWORK,
  cls='non_standard',
  via=['Apache HttpClient 4.x DefaultHttpClient.execute (library source not read)'],
  evidence='SRC com/ichi2/libanki/sync/HttpSyncer.java:210, 213, 235-236; INFERRED (Apache HttpClient 4.x source not read)',
  note='isRepeatable returns false (HttpSyncer.java:421-424). The route exists only on a library retry or re-authentication of the same request. The library dispatch is INFERRED (library source not read).')

# --- TextImporter: a stub whose only constructions are in the androidTest ImportTest.
UNREACHABLE['TextImporter.<init>'] = ('no_trigger_in_app',
  'Stub importer constructor. Only the androidTest ImportTest constructs TextImporter; the app source root has no call site.',
  'SRC com/ichi2/libanki/importer/TextImporter.java:10-12; SRC AnkiDroid/src/androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:228, 276',
  'SOURCE')

UNREACHABLE['TextImporter.initMapping'] = ('no_trigger_in_app',
  'Empty stub body. Called only from the androidTest ImportTest on a TextImporter, which the app never constructs.',
  'SRC com/ichi2/libanki/importer/TextImporter.java:19-21; SRC AnkiDroid/src/androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:229, 277',
  'SOURCE')

UNREACHABLE['TextImporter.run'] = ('no_trigger_in_app',
  'Empty stub body. Called only from the androidTest ImportTest on a TextImporter, which the app never constructs.',
  'SRC com/ichi2/libanki/importer/TextImporter.java:14-17; SRC AnkiDroid/src/androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:230, 248, 253, 278',
  'SOURCE')

UNREACHABLE['TextImporter.setImportMode'] = ('no_trigger_in_app',
  'Empty stub body. Called only from the androidTest ImportTest on a TextImporter, which the app never constructs.',
  'SRC com/ichi2/libanki/importer/TextImporter.java:23-25; SRC AnkiDroid/src/androidTest/java/com.ichi2.anki.tests/libanki/ImportTest.java:247, 252',
  'SOURCE')

# --- HttpSyncer base bodies. HttpSyncer is never instantiated (no "new HttpSyncer" in the source root); every runtime
# receiver is a RemoteServer or FullSyncer, and each one overrides the method, so the base body never runs.
UNREACHABLE['HttpSyncer.applyChanges'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Syncer.java:170 on a RemoteServer (Connection.java:280-281), which overrides applyChanges.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:327-329; SRC com/ichi2/libanki/sync/Syncer.java:170; SRC com/ichi2/libanki/sync/RemoteServer.java:74-77; SRC com/ichi2/async/Connection.java:280-281',
  'SOURCE')

UNREACHABLE['HttpSyncer.applyChunk'] = ('no_trigger_in_app',
  'Base body is empty. Its only caller is Syncer.java:197 on a RemoteServer, which overrides applyChunk.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:372-373; SRC com/ichi2/libanki/sync/Syncer.java:197; SRC com/ichi2/libanki/sync/RemoteServer.java:93-96',
  'SOURCE')

UNREACHABLE['HttpSyncer.chunk()'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Syncer.java:179 on a RemoteServer, which overrides chunk(). Syncer.java:192 calls Syncer own chunk().',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:342-344; SRC com/ichi2/libanki/sync/Syncer.java:179, 192; SRC com/ichi2/libanki/sync/RemoteServer.java:86-90',
  'SOURCE')

UNREACHABLE['HttpSyncer.chunk(JSONObject)'] = ('no_trigger_in_app',
  'Base body returns null. No caller: every chunk call is the no-argument form (Syncer.java:179, 192).',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:337-339; SRC com/ichi2/libanki/sync/Syncer.java:179, 192, 497',
  'SOURCE')

UNREACHABLE['HttpSyncer.download'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Connection.java:337 on a FullSyncer (Connection.java:318), which overrides download.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:357-359; SRC com/ichi2/async/Connection.java:318, 337; SRC com/ichi2/libanki/sync/FullSyncer.java:76-80',
  'SOURCE')

UNREACHABLE['HttpSyncer.hostKey'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Connection.java:202 on a RemoteServer (Connection.java:199), which overrides hostKey.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:322-324; SRC com/ichi2/async/Connection.java:199, 202; SRC com/ichi2/libanki/sync/RemoteServer.java:43-54',
  'SOURCE')

UNREACHABLE['HttpSyncer.meta'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Syncer.java:89 on a RemoteServer, which overrides meta.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:352-354; SRC com/ichi2/libanki/sync/Syncer.java:89; SRC com/ichi2/libanki/sync/RemoteServer.java:57-71',
  'SOURCE')

UNREACHABLE['HttpSyncer.register'] = ('no_trigger_in_app',
  'Base body returns null. No caller in the source root. The string "register" is only compared in req (HttpSyncer.java:201).',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:444-446, 201',
  'SOURCE')

UNREACHABLE['HttpSyncer.req(String,int,InputStream)'] = ('no_trigger_in_app',
  'No caller. Every req call in the source root passes a String first, then an InputStream with or without an int after it. No call site passes an int before the InputStream.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:137-139; SRC com/ichi2/libanki/sync/FullSyncer.java:80, 159; SRC com/ichi2/libanki/sync/RemoteMediaServer.java:133; SRC com/ichi2/libanki/sync/RemoteServer.java:50, 67, 108, 120',
  'SOURCE')

UNREACHABLE['HttpSyncer.sanityCheck2'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Syncer.java:204 on a RemoteServer, which overrides sanityCheck2.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:367-369; SRC com/ichi2/libanki/sync/Syncer.java:204; SRC com/ichi2/libanki/sync/RemoteServer.java:99-102',
  'SOURCE')

UNREACHABLE['HttpSyncer.start'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Syncer.java:157 on a RemoteServer, which overrides start.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:332-334; SRC com/ichi2/libanki/sync/Syncer.java:157; SRC com/ichi2/libanki/sync/RemoteServer.java:80-83',
  'SOURCE')

UNREACHABLE['HttpSyncer.upload'] = ('no_trigger_in_app',
  'Base body returns null. Its only caller is Connection.java:322 on a FullSyncer (Connection.java:318), which overrides upload.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:362-364; SRC com/ichi2/async/Connection.java:318, 322; SRC com/ichi2/libanki/sync/FullSyncer.java:143-159',
  'SOURCE')

# --- ProgressByteEntity: the two methods no app code calls. Library dispatch is INFERRED (Apache HttpClient 4.x source not read).
UNREACHABLE['HttpSyncer$ProgressByteEntity.getContent'] = ('framework_never_calls',
  'INFERRED (Apache HttpClient 4.x source not read): the request body is read through writeTo, not getContent. App code calls getContent only on response entities.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:409-412; SRC com/ichi2/async/Connection.java:223; SRC com/ichi2/libanki/sync/FullSyncer.java:84; INFERRED (Apache HttpClient 4.x source not read)',
  'SOURCE')

UNREACHABLE['HttpSyncer$ProgressByteEntity.isStreaming'] = ('framework_never_calls',
  'INFERRED (Apache HttpClient 4.x source not read): returns false (HttpSyncer.java:427-430), and the send path uses writeTo and getContentLength. No app code calls it.',
  'SRC com/ichi2/libanki/sync/HttpSyncer.java:427-430, 210, 236; INFERRED (Apache HttpClient 4.x source not read)',
  'SOURCE')
