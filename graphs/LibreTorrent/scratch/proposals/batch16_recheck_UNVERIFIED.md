# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# LibreTorrent batch 16 re-check — proposal only, NOT verified, NOT pushed, NOT edited

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
No push, no repo edit, no token, no clone. Fetches were spaced, single-file,
via the GitHub connector.

## Files read (in order, one at a time)

- handoff/MUSE_HANDOVER.md
- handoff/KIRO_CONVERT_APPS.md (head)
- handoff/KIRO_CORRECTIONS.md
- handoff/SCHEMA_V2.md
- handoff/AGENT_BRIEF_V2.md (head)
- handoff/CONVERSION_RECIPE.md (head)
- graphs/LibreTorrent/AGENT_NOTES.md — "Stopped by the user (2026-10-31, about 18:10 EDT)"
  section: Claude run stopped mid-batch; batches 13–18 unverified; check whether
  parts/b016.md was merged into graph_def.py; out/build_report.txt may be older
  than graph_def.py.
- handoff/LIBRETORRENT_BATCH_PLAN.tsv, filtered to batch 16 only: exactly 40 rows,
  all status TODO_CANDIDATE_REACHABLE, all current_label
  "REACHABLE (generator candidate, no hand route yet)". Plan status is a
  candidate, not evidence.
- graphs/LibreTorrent/scratch/batch_016.md
- graphs/LibreTorrent/scratch/batch_016_helper_printed.txt
- graphs/LibreTorrent/parts/b016.md
- graphs/LibreTorrent/graph_def.py (fetched in full via connector; 563,300 chars
  in the returned text — not too large to check, so no guess is needed here)
- final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/nanohttpd/NanoHTTPD.java
  (1,851 lines, read and line-checked locally from the connector fetch)
- final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java
- final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/core/model/TorrentEngine.java
  (relevant sections only: streaming-server start, session listener)

## Counts — read carefully, two different counts

- Proposed labels with printed local evidence: 40/40
  - Proposed REACHABLE (local route segment only, see below): 24
  - Proposed UNREACHABLE no_trigger_in_app (pending full-repo grep): 16
- Strictly judged / verified for merge: 0/40
  - 24 OPEN: no complete hand route from a launcher/entry point was printed in
    this re-check (see "Why the 24 are OPEN, not judged REACHABLE").
  - 16 UNVERIFIED: a real full-repo grep is still required for any UNREACHABLE
    claim. Connector search was NOT used as evidence of absence, per the task.
- No batch 16 label in this report is verified for merge. Do not merge on this
  report alone.

## Why the 24 are OPEN, not judged REACHABLE

Printed local chain from server start onward (all NanoHTTPD.java unless noted):

- TorrentEngine.handleOnSessionStarted: TorrentEngine.java:1046,1056-1058 —
  `if (pref.enableStreaming()) startStreamingServer();`
- TorrentEngine.startStreamingServer: TorrentEngine.java:1063-1071 —
  `torrentStreamServer = new TorrentStreamServer(hostname, port);`
  `torrentStreamServer.start(appContext);`
- TorrentStreamServer.start: TorrentStreamServer.java:72-78 —
  `engine = TorrentEngine.getInstance(appContext); super.start();`
- NanoHTTPD.start() → start(timeout) → start(timeout, daemon):
  NanoHTTPD.java:1794-1795, 1800-1801, 1813-1820 —
  `myServerSocket = getServerSocketFactory().create();`
  `myThread = new Thread(serverRunnable); myThread.start();`
- ServerRunnable.run: NanoHTTPD.java:1332-1347 — accept loop,
  `NanoHTTPD.this.asyncRunner.exec(createClientHandler(finalAccept, inputStream));`
- DefaultAsyncRunner.exec: NanoHTTPD.java:330-336 —
  `Thread t = new Thread(clientHandler); … t.start();`
- ClientHandler.run: NanoHTTPD.java:168-175,188-192 —
  `tempFileManagerFactory.create(); new HTTPSession(…); session.execute();`
  finally `asyncRunner.closed(this);`
- HTTPSession.execute: NanoHTTPD.java:655-760 — see per-method rows below.

What is NOT printed in this re-check, and therefore blocks a judged REACHABLE:

1. The app entry → TorrentEngine.getInstance → TorrentSession start chain.
   TorrentEngine's constructor does register the listener
   (TorrentEngine.java:140 `session.addListener(engineListener)`, and
   1265-1268 `engineListener.onSessionStarted()` → `handleOnSessionStarted()`),
   but what starts the session and fires that listener is libtorrent-session
   library dispatch, not printed source in this re-check. Library dispatch must
   be explained, not assumed — so it is not assumed here.
2. The JVM Thread.start() → Runnable.run() links (ServerRunnable.run and
   ClientHandler.run) are JVM/library dispatch. The construction and start()
   lines are printed (NanoHTTPD.java:1817-1820, 330-336), but no printed line
   says "start() invokes run()". That link is therefore INFERRED, not SOURCE,
   for every method downstream of a thread start.

Consequence: the 24 have a solid printed route segment *conditional on the
streaming server running*, but no complete hand route from an entry point.
Under the strict rule in the task they stay OPEN / proposed-REACHABLE.
If the parent accepts "TorrentStreamServer.start as the entry" then the same
24 would be REACHABLE; that is a parent decision, not a conclusion of this
re-check.

## Why the 16 proposed UNREACHABLE do not depend on the upstream gap

TorrentStreamServer overrides serve and does not call super.serve:

- TorrentStreamServer.java:110-121 — `public Response serve(IHTTPSession session)`,
  `session.getUri()`, `handleTorrent(session)`, return. No `super.serve(...)`
  string occurs in that file, and no `parseBody` / `getMethod` /
  `getQueryParameterString` call occurs in that file.
- NanoHTTPD base serve: NanoHTTPD.java:1732-1746 —
  `Method method = session.getMethod();`
  `if (Method.PUT.equals(method) || Method.POST.equals(method)) session.parseBody(files);`
  `session.getParms(); session.getQueryParameterString(); session.getUri(); session.getHeaders();`
- HTTPSession.execute calls the virtual `serve(this)` at NanoHTTPD.java:720.
  With the app subclass installed, that dispatch goes to the override, not to
  base serve. That is ordinary Java override dispatch, stated here explicitly
  rather than assumed.

So even when the server is running, base-serve-only methods are not reached
through execute(). That argument is local and does not need the upstream
entry chain. It DOES still need a full-repo grep, because another app class
could call these methods directly, hold an IHTTPSession, or subclass
NanoHTTPD with its own serve. IHTTPSession itself declares getMethod,
getQueryParameterString, parseBody, getHeaders, getParms, getUri
(NanoHTTPD.java:969-987, interface declarations — declarations are not calls).

## Separable per-method table

Conventions in this table:
- "Proposed" = this re-check's proposal, not a verified label.
- confirmed_by is SOURCE only for a printed local call site / definition;
  INFERRED where the route relies on JVM thread dispatch, JVM class
  initialisation, or the unprinted session-listener dispatch.
  confirmed_by is never DYN, FW-MEMORY, or UNVERIFIED in this table.
- "Status" is separate from confirmed_by: OPEN = no complete entry route;
  UNVERIFIED = pending full-repo grep.
- Citations are org/nanohttpd/NanoHTTPD.java unless a file is named.
- No tool coverage was used as evidence.

| # | Method | Proposed label | Kind (UNREACHABLE only) | Route / reason | Citations (printed lines) | confirmed_by | Status |
|---|---|---|---|---|---|---|---|
| 1 | NanoHTTPD$CookieHandler.set(String,String,int) | UNREACHABLE (proposed) | no_trigger_in_app | Only caller in NanoHTTPD.java is CookieHandler.delete, which itself has no caller in NanoHTTPD.java. Grep must also prove delete is uncalled app-wide. | NanoHTTPD.java:252-254 (delete calls set), 283-285 (set definition) | SOURCE (local files only) | UNVERIFIED — pending full-repo grep incl. delete callers |
| 2 | NanoHTTPD$CookieHandler.set(Cookie) | UNREACHABLE (proposed) | no_trigger_in_app | No caller in NanoHTTPD.java; only the definition. Queue is read by unloadQueue, but nothing in the printed files adds via this setter. | NanoHTTPD.java:270-272, 294-297 (unloadQueue reads queue) | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 3 | NanoHTTPD$CookieHandler.unloadQueue | REACHABLE (proposed) / OPEN | — | execute() calls it after serve returns a non-null response. Method executes even with an empty queue (loop over queue). | NanoHTTPD.java:720 (serve), 723-727 (null check, unloadQueue) | INFERRED (route includes Thread.start→run and unprinted session-listener dispatch) | OPEN — no complete entry route |
| 4 | NanoHTTPD$DefaultAsyncRunner.<init> | REACHABLE (proposed) / OPEN | — | No explicit constructor body in NanoHTTPD.java (default constructor); constructed by the NanoHTTPD hostname/port constructor. | NanoHTTPD.java:1557-1561 (new DefaultAsyncRunner()) | INFERRED (upstream dispatch not printed) | OPEN — no complete entry route |
| 5 | NanoHTTPD$DefaultAsyncRunner.closeAll | REACHABLE (proposed) / OPEN | — | NanoHTTPD.stop() calls asyncRunner.closeAll(). Stop path: TorrentStreamServer.stop → super.stop → NanoHTTPD.stop; also startStreamingServer first calls stopStreamingServer. Requires a previously started server for the non-null branch. | NanoHTTPD.java:1837-1840; TorrentStreamServer.java:81-84; TorrentEngine.java:1063-1064,1079-1082 | INFERRED (upstream dispatch not printed) | OPEN — no complete entry route |
| 6 | NanoHTTPD$DefaultAsyncRunner.closed | REACHABLE (proposed) / OPEN | — | ClientHandler.run finally block calls it on every handler completion. | NanoHTTPD.java:188-192 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 7 | NanoHTTPD$DefaultAsyncRunner.exec | REACHABLE (proposed) / OPEN | — | ServerRunnable accept loop calls it for each accepted socket. exec itself creates a daemon Thread and starts it. | NanoHTTPD.java:1340-1347, 330-336 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 8 | NanoHTTPD$DefaultServerSocketFactory.<init> | REACHABLE (proposed) / OPEN | — | No explicit constructor body (default constructor); field initialiser constructs it when a NanoHTTPD is constructed. | NanoHTTPD.java:1531 | INFERRED (upstream dispatch not printed) | OPEN — no complete entry route |
| 9 | NanoHTTPD$DefaultServerSocketFactory.create | REACHABLE (proposed) / OPEN | — | NanoHTTPD.start(timeout, daemon) calls getServerSocketFactory().create() to obtain the listening socket. | NanoHTTPD.java:1813-1814, 1669 (getter, checked) | INFERRED (upstream dispatch not printed) | OPEN — no complete entry route |
| 10 | NanoHTTPD$DefaultTempFile.<init> | UNREACHABLE (proposed) | no_trigger_in_app | Only constructed by DefaultTempFileManager.createTempFile, which is itself only called from unreachable parseBody paths (see #15). | NanoHTTPD.java:350-352, 402-405, 865-877, 1732-1747 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 11 | NanoHTTPD$DefaultTempFile.delete | UNREACHABLE (proposed) | no_trigger_in_app | Only caller in NanoHTTPD.java is DefaultTempFileManager.clear iterating its list, and the list only gains entries via unreachable createTempFile. Note kind ambiguity (see below): clear() itself runs, but over an empty list in the app path. | NanoHTTPD.java:391-400 (clear loop), 355-359 (delete), 402-405 (only list entry point) | SOURCE (local files only) | UNVERIFIED — pending full-repo grep; kind to be confirmed (see note) |
| 12 | NanoHTTPD$DefaultTempFile.getName | UNREACHABLE (proposed) | no_trigger_in_app | Only callers in NanoHTTPD.java are getTmpBucket and saveTmpFile, both inside unreachable parseBody. | NanoHTTPD.java:362-364, 840-844, 944-956, 865-877 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 13 | NanoHTTPD$DefaultTempFileManager.<init> | REACHABLE (proposed) / OPEN | — | Constructed by DefaultTempFileManagerFactory.create, called by ClientHandler.run for each client. | NanoHTTPD.java:383-388, 411-415, 172 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 14 | NanoHTTPD$DefaultTempFileManager.clear | REACHABLE (proposed) / OPEN | — | execute() finally block calls tempFileManager.clear() on every request completion. The method itself executes; its loop body may not (see #11). | NanoHTTPD.java:752-754, 391-400 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 15 | NanoHTTPD$DefaultTempFileManager.createTempFile | UNREACHABLE (proposed) | no_trigger_in_app | Only callers in NanoHTTPD.java are getTmpBucket (parseBody, large-body branch) and saveTmpFile (parseBody paths), both inside unreachable parseBody. | NanoHTTPD.java:402-405, 842, 949, 865-877 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 16 | NanoHTTPD$DefaultTempFileManagerFactory.<init> | REACHABLE (proposed) / OPEN | — | No explicit constructor body (default constructor); constructed by the NanoHTTPD hostname/port constructor. | NanoHTTPD.java:1560 | INFERRED (upstream dispatch not printed) | OPEN — no complete entry route |
| 17 | NanoHTTPD$DefaultTempFileManagerFactory.create | REACHABLE (proposed) / OPEN | — | ClientHandler.run calls tempFileManagerFactory.create() before constructing the session. | NanoHTTPD.java:172, 411-415 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 18 | NanoHTTPD$HTTPSession.<init>(NanoHTTPD,TempFileManager,InputStream,OutputStream,InetAddress) | REACHABLE (proposed) / OPEN | — | Called by ClientHandler.run. Note: the plan descriptor's first NanoHTTPD argument is the inner-class synthetic outer reference; the source constructor at 484 takes (TempFileManager, InputStream, OutputStream, InetAddress) — 4 explicit args, 5 in bytecode. Not a mismatch. | NanoHTTPD.java:173, 484-490 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 19 | NanoHTTPD$HTTPSession.decodeHeader | REACHABLE (proposed) / OPEN | — | execute() calls it to parse the request line and headers. | NanoHTTPD.java:702-703, 494-542 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 20 | NanoHTTPD$HTTPSession.decodeMultipartFormData | UNREACHABLE (proposed) | no_trigger_in_app | Only caller in NanoHTTPD.java is parseBody's multipart branch, and parseBody is itself base-serve-only (see #33). | NanoHTTPD.java:544-547, 907-915, 1732-1747 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 21 | NanoHTTPD$HTTPSession.decodeParms | REACHABLE (proposed) / OPEN | — | decodeHeader calls it when the URI contains '?'. The normal app stream URL is /stream?file=…&torrent=… (TorrentStreamServer.java:90,93-104), so this branch is the live one. A second caller inside unreachable parseBody (urlencoded POST) is not needed. | NanoHTTPD.java:510-513, 637-654; TorrentStreamServer.java:90,129-142 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 22 | NanoHTTPD$HTTPSession.execute | REACHABLE (proposed) / OPEN | — | ClientHandler.run loops `session.execute()` while the socket is not closed. | NanoHTTPD.java:174-175, 655-760 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 23 | NanoHTTPD$HTTPSession.findHeaderEnd | REACHABLE (proposed) / OPEN | — | execute() calls it in the header-read loop. | NanoHTTPD.java:681-687, 761-775 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 24 | NanoHTTPD$HTTPSession.getAttributeFromContentHeader | UNREACHABLE (proposed) | no_trigger_in_app | Only caller in NanoHTTPD.java is parseBody's multipart branch, as arguments to decodeMultipartFormData. | NanoHTTPD.java:913-914, 936-939, 865-935 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 25 | NanoHTTPD$HTTPSession.getBodySize | UNREACHABLE (proposed) | no_trigger_in_app | Only executable caller in NanoHTTPD.java is parseBody. The line `// TODO: long body_size = getBodySize();` at NanoHTTPD.java:717 is a comment, not a call — do not count it. | NanoHTTPD.java:856-868, 717 (comment only), 1732-1747 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 26 | NanoHTTPD$HTTPSession.getBoundaryPositions | UNREACHABLE (proposed) | no_trigger_in_app | Only caller in NanoHTTPD.java is unreachable decodeMultipartFormData. | NanoHTTPD.java:546, 781-805, 544-547 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 27 | NanoHTTPD$HTTPSession.getHeaders | REACHABLE (proposed) / OPEN | — | TorrentStreamServer.handleTorrent calls httpSession.getHeaders(). (Base serve also calls it, but that path is bypassed and is not needed here.) | TorrentStreamServer.java:150; NanoHTTPD.java:821-822 | INFERRED (route includes Thread.start→run and serve virtual dispatch; app call site itself is SOURCE) | OPEN — no complete entry route |
| 28 | NanoHTTPD$HTTPSession.getMethod | UNREACHABLE (proposed) | no_trigger_in_app | Only executable caller in NanoHTTPD.java is base serve; TorrentStreamServer does not call it. Interface declaration at NanoHTTPD.java:974 is not a call. | NanoHTTPD.java:829-831, 1734, 1746; TorrentStreamServer.java:110-121 (no getMethod call) | SOURCE (local files only) | UNVERIFIED — pending full-repo grep, incl. any other IHTTPSession holder / NanoHTTPD subclass |
| 29 | NanoHTTPD$HTTPSession.getParms | REACHABLE (proposed) / OPEN | — | TorrentStreamServer.handleTorrent calls httpSession.getParms() and reads torrent/file params. | TorrentStreamServer.java:132,141; NanoHTTPD.java:833-834 | INFERRED (route includes Thread.start→run and serve virtual dispatch; app call site itself is SOURCE) | OPEN — no complete entry route |
| 30 | NanoHTTPD$HTTPSession.getQueryParameterString | UNREACHABLE (proposed) | no_trigger_in_app | Only executable caller in NanoHTTPD.java is base serve; TorrentStreamServer does not call it (it uses getParms instead). Interface declaration at NanoHTTPD.java:976 is not a call. | NanoHTTPD.java:837-839, 1745; TorrentStreamServer.java:110-142 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep, incl. any other IHTTPSession holder / NanoHTTPD subclass |
| 31 | NanoHTTPD$HTTPSession.getTmpBucket | UNREACHABLE (proposed) | no_trigger_in_app | Only caller in NanoHTTPD.java is parseBody's large-body branch; parseBody is base-serve-only. | NanoHTTPD.java:840-847, 876, 865-935 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 32 | NanoHTTPD$HTTPSession.getUri | REACHABLE (proposed) / OPEN | — | TorrentStreamServer.serve calls session.getUri(), and handleTorrent calls httpSession.getUri() again for the /stream check. | TorrentStreamServer.java:113,129; NanoHTTPD.java:849-850 | INFERRED (route includes Thread.start→run and serve virtual dispatch; app call sites themselves are SOURCE) | OPEN — no complete entry route |
| 33 | NanoHTTPD$HTTPSession.parseBody | UNREACHABLE (proposed) | no_trigger_in_app | Only caller in NanoHTTPD.java is base serve for PUT/POST; TorrentStreamServer's override does not call super.serve or parseBody. Interface declaration at NanoHTTPD.java:987 is not a call. | NanoHTTPD.java:865-935, 1732-1747; TorrentStreamServer.java:110-121 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep, incl. any other serve override |
| 34 | NanoHTTPD$HTTPSession.saveTmpFile | UNREACHABLE (proposed) | no_trigger_in_app | Only callers in NanoHTTPD.java are decodeMultipartFormData (file parts) and parseBody's PUT branch, both inside unreachable parseBody. | NanoHTTPD.java:606, 930, 944-963 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 35 | NanoHTTPD$HTTPSession.scipOverNewLine | UNREACHABLE (proposed) | no_trigger_in_app | Only caller in NanoHTTPD.java is unreachable decodeMultipartFormData. | NanoHTTPD.java:590, 625-630, 544-547 | SOURCE (local files only) | UNVERIFIED — pending full-repo grep |
| 36 | NanoHTTPD$Method.<clinit> | REACHABLE (proposed) / OPEN | — | No explicit <clinit> body; enum constants at 993-1002. First active use of Method is execute()'s Method.lookup call, which loads the enum class and triggers JVM class initialisation. That JVM rule is not printed source, hence INFERRED. | NanoHTTPD.java:993-1010, 708 | INFERRED (JVM class-initialisation rule + Thread.start→run dispatch) | OPEN — no complete entry route |
| 37 | NanoHTTPD$Method.lookup | REACHABLE (proposed) / OPEN | — | execute() calls Method.lookup(pre.get("method")) after decodeHeader, before serve. If lookup returns null, execute throws BAD_REQUEST — but lookup itself has executed. | NanoHTTPD.java:708-710, 1003-1010 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |
| 38 | NanoHTTPD$Response.<init> | REACHABLE (proposed) / OPEN | — | Protected constructor (NanoHTTPD.java:1122). Called by newFixedLengthResponse overloads (1696-1697, 1702-1713) and newChunkedResponse (1691), which TorrentStreamServer calls repeatedly, and by execute()'s error responses. | NanoHTTPD.java:1122-1134, 1696-1713; TorrentStreamServer.java:127,196,209,244 | INFERRED (route includes Thread.start→run and serve virtual dispatch; app call sites themselves are SOURCE) | OPEN — no complete entry route |
| 39 | NanoHTTPD$Response.addHeader | REACHABLE (proposed) / OPEN | — | TorrentStreamServer calls res.addHeader(...) for ETag, Accept-Ranges, Content-Length, Content-Range, Content-Disposition, etc. (UnloadQueue → addHeader is a second, queue-dependent path and is not needed here.) | TorrentStreamServer.java:197,209-214,245-248; NanoHTTPD.java:1144-1145 | INFERRED (route includes Thread.start→run and serve virtual dispatch; app call sites themselves are SOURCE) | OPEN — no complete entry route |
| 40 | NanoHTTPD$Response.close | REACHABLE (proposed) / OPEN | — | execute() finally block calls safeClose(r); safeClose closes a Closeable (NanoHTTPD.java:1511-1515), and Response implements Closeable with close() closing its data stream (1015, 1136-1139). Normal served responses (r != null) reach it; a null response skips it via the safeClose null check. | NanoHTTPD.java:752-753, 1511-1515, 1136-1139 | INFERRED (route includes Thread.start→run dispatch) | OPEN — no complete entry route |

## Prior-work discrepancies found (do not silently copy either)

- graphs/LibreTorrent/scratch/batch_016.md says: 40 rows, 0 REACHABLE,
  16 UNREACHABLE no_trigger_in_app, 24 OPEN. Its 16 match the 16 proposed
  UNREACHABLE above, and its 24 OPEN match the 24 proposed-REACHABLE/OPEN above.
- graphs/LibreTorrent/scratch/batch_016_helper_printed.txt ends with a summary
  line saying 24 REACHABLE, 16 UNREACHABLE, 0 OPEN — contradicting batch_016.md.
  This re-check sides with batch_016.md's OPEN classification under the strict
  entry-route rule, for the reasons in "Why the 24 are OPEN". The helper file's
  verbatim excerpts were still useful and were cross-checked against the actual
  NanoHTTPD.java / TorrentStreamServer.java / TorrentEngine.java lines above;
  where the helper summary ranges differed from the source (e.g. it summarised
  rather than quoted some ranges), this report cites the source lines actually
  read, not the helper summary.
- DefaultTempFile.delete kind ambiguity: clear() itself is on the live path,
  so a reviewer could argue branch_never_taken (the loop over an empty list)
  instead of no_trigger_in_app (no temp file ever enters the list). This report
  keeps the prior no_trigger_in_app proposal but flags it — do not treat the
  kind as settled until the grep + route review confirms it.

## parts/b016.md — merged or not?

- graphs/LibreTorrent/parts/b016.md fetched on branch work-2026-10-31 contains
  only: `STATUS: RUNNING 17:26`. No method rows, no labels. On its own it is
  NOT a merged part.
- graphs/LibreTorrent/graph_def.py DOES contain a batch-16 block, however:
  a comment "# S4 batch 16: unused cookie and request-body parsing helpers…",
  `_BATCH16_BODY_PATH_CLOSED`, and an UNREACHABLE.update with exactly the same
  16 methods as batch_016.md's UNREACHABLE set (CookieHandler.set x2,
  DefaultTempFile.<init>/delete/getName, DefaultTempFileManager.createTempFile,
  HTTPSession.decodeMultipartFormData/getAttributeFromContentHeader/getBodySize/
  getBoundaryPositions/getMethod/getQueryParameterString/getTmpBucket/parseBody/
  saveTmpFile/scipOverNewLine), each citing NanoHTTPD.java lines and
  scratch/batch_016_helper_printed.txt, marked SOURCE in graph_def.py.
- The other 24 batch-16 methods have NO UNREACHABLE label in graph_def.py
  (exact-name search: absent as labels) and NO hand edge found by exact short-name
  search (CookieHandler.unloadQueue, HTTPSession.execute/decodeHeader/decodeParms/
  findHeaderEnd/getHeaders/getParms/getUri, Method.lookup, Response.addHeader/close
  all 0 occurrences as edge names; DefaultAsyncRunner / DefaultTempFileManager
  occur once each only inside the older unrelated NanoHTTPD block, not as
  batch-16 edges). They may still be reached via bytecode AUTO edges in a build
  — that was not checked here and is not evidence either way.
- Conclusion: the 16 UNREACHABLE entries appear merged into graph_def.py, but
  the part file that should document that merge (parts/b016.md) is still only
  RUNNING with no rows. The merge provenance is therefore incomplete, and the
  16 remain UNVERIFIED pending grep regardless of their presence in graph_def.py.
  graph_def.py was fetchable via the connector, so this is a checked result,
  not a guess about file size.

## Blockers / what is still required before any batch-16 label is verified

1. Full-repo grep (local checkout required; not done here, and not replaced by
   connector search): over the app source folder, for each of the 16 proposed
   UNREACHABLE method names, plus CookieHandler.delete callers, plus any other
   NanoHTTPD subclass / serve override, plus any IHTTPSession holder calling
   getMethod / getQueryParameterString / parseBody, plus direct constructors of
   DefaultTempFile. Save the grep output in scratch/ before judging any of the
   16 as verified.
2. Complete entry route for the 24 OPEN methods: print the chain from a real
   entry point (launcher / MainApplication / MainActivity) through
   TorrentEngine.getInstance and TorrentSession start to engineListener
   onSessionStarted, explaining the session-library dispatch, and the
   Thread.start → run links. Until then they stay OPEN.
3. Confirm the DefaultTempFile.delete kind (no_trigger_in_app vs
   branch_never_taken) at route-review time.
4. Rebuild and run build / sampler / grep / C1 checks on a full local checkout
   before merging anything; out/build_report.txt may be older than graph_def.py
   (per AGENT_NOTES Stopped section).
5. Resolve the parts/b016.md provenance gap: either complete parts/b016.md with
   rows matching the graph_def.py block, or record why the graph_def.py block
   was added without a completed part file. No edit was made here, per the task.

## What was NOT done

- No push to any branch (not main, not 'result', not work-2026-10-31).
- No repo edit (graph_def.py, out/, progress, tools untouched).
- No token, no clone, no connector search_code used as absence evidence.
- No tool coverage used as evidence.
- No label in this report is presented as verified, and no build/sampler/grep/C1
  count is claimed.
