# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# LibreTorrent batch 17 — re-check (UNVERIFIED proposal, NOT merged, NOT pushed)

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
Method: connector only, spaced single-file fetches, no token, no clone, no push, no edit to the repo, no edit to graph_def.py, out/, progress, or tools/.
Status of this report: UNVERIFIED proposal. No build, sampler, full-repo grep, or C1 check was run in this session, and no such count is claimed. Nothing was pushed or edited in the repo.

## Read first (in order, one file at a time)

- `handoff/MUSE_HANDOVER.md` — rules: REACHABLE only with a hand route from an entry point; UNREACHABLE needs exactly one kind, a reason, and a source reference; `confirmed_by` is SOURCE only where lines were printed, otherwise INFERRED, never DYN / FW-MEMORY / UNVERIFIED; tool coverage, old generated graphs, and build REACHABLE counts are never evidence.
- `handoff/KIRO_CONVERT_APPS.md`, `handoff/KIRO_CORRECTIONS.md`, `handoff/SCHEMA_V2.md`, `handoff/AGENT_BRIEF_V2.md`, `handoff/CONVERSION_RECIPE.md` — read as named by the handover.
- `graphs/LibreTorrent/AGENT_NOTES.md`, "Stopped by the user (2026-10-31, about 18:10 EDT)" section: the Claude run was stopped mid-batch, batches 13–18 are to be treated as unverified, and re-checked from printed source before being relied on. Its "Blocked" section also notes the batch-12 `databinding.DataBinderMapperImpl.<init>` OPEN_NO_SOURCE row — a different class from batch 17's `libretorrent.DataBinderMapperImpl` (see below).
- `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, batch == 17 only: exactly 40 rows, lines 610–649 in the plan file as fetched, all status `TODO_CANDIDATE_REACHABLE` / current label "REACHABLE (generator candidate, no hand route yet)". Those are candidates, not evidence.

## Source roots printed for this batch

- `SRC = final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`
- NanoHTTPD source printed in full (1,851 lines): `SRC/org/nanohttpd/NanoHTTPD.java`
- App streaming server printed in full (284 lines): `SRC/org/proninyaroslav/libretorrent/core/model/stream/TorrentStreamServer.java`
- TorrentEngine printed in relevant part: `SRC/org/proninyaroslav/libretorrent/core/model/TorrentEngine.java`
- Package directory listing printed for `SRC/org/proninyaroslav/libretorrent/` — entries: `JacocoInstrument`, `MainApplication.java`, `core`, `receiver`, `service`, `ui`. No `DataBinderMapperImpl.java` and no `databinding/` subdirectory in that listing.

## Shared hand route (NanoHTTPD / streaming trunk)

All 24 REACHABLE proposals below use this trunk; the method-specific step is in the table.

1. `TorrentEngine.handleOnSessionStarted` — `TorrentEngine.java:1046-1058`: `boolean enableStreaming = pref.enableStreaming(); if (enableStreaming) startStreamingServer();` — STATE settings gate `pref.enableStreaming()`.
2. `TorrentEngine.startStreamingServer` — `TorrentEngine.java:1063-1071`: `torrentStreamServer = new TorrentStreamServer(hostname, port); torrentStreamServer.start(appContext);`
3. `TorrentStreamServer` constructor — `TorrentStreamServer.java:67-69`: `super(host, port)` (= `NanoHTTPD.<init>(String,int)`).
4. `TorrentStreamServer.start` — `TorrentStreamServer.java:72-78`: `super.start()`.
5. `NanoHTTPD.start()` — `NanoHTTPD.java:1794-1795` → `start(timeout)` → `start(timeout, daemon)` — `NanoHTTPD.java:1812-1822`: `this.myServerSocket = this.getServerSocketFactory().create(); ServerRunnable serverRunnable = createServerRunnable(timeout); this.myThread = new Thread(serverRunnable); this.myThread.start();`
6. `ServerRunnable.run` — `NanoHTTPD.java:1332-1356`: socket accept loop → `NanoHTTPD.this.asyncRunner.exec(createClientHandler(finalAccept, inputStream))`.
7. `ClientHandler.run` — `NanoHTTPD.java:168-176`: `HTTPSession session = new HTTPSession(...); while (...) session.execute();`
8. `HTTPSession.execute` — `NanoHTTPD.java:722-733` (serve and response-send part): `r = serve(this);` … `r.setRequestMethod(this.method); r.setGzipEncoding(useGzipWhenAccepted(r) && ...); r.setKeepAlive(keepAlive); r.send(this.outputStream);` … `r.getHeader("connection")` check at :733. The `serve(this)` call dispatches virtually to `TorrentStreamServer.serve` (`TorrentStreamServer.java:111-120`), which calls `handleTorrent` (:117) and, when the extension is in `DLNA_FILE_TYPES` (`mp4`/`avi`/`mkv`, :62-70), `fileType.setHeaders(res)` (:119-120).
9. `Response.send` — `NanoHTTPD.java:1185-1227` — internal chain: `send` → `sendBodyWithCorrectTransferAndEncoding` (:1223) → `sendBodyWithCorrectEncoding` (:1233/:1236) → `sendBody` (:1243/:1246), with `headerAlreadySent` (:1205, :1208), `setChunkedTransfer(true)` (:1213, gzip branch), and `sendContentLengthHeaderIfNotAlreadyPresent` (:1219, non-gzip branch).

Why every REACHABLE below is `INFERRED`, not `SOURCE`: each method's immediate call site was printed, but the full route passes through at least one step not printed from framework/JVM source — `Thread.start()` → `ServerRunnable.run` / `ClientHandler` thread dispatch, and/or the virtual `serve(this)` dispatch to `TorrentStreamServer.serve`. Under the schema definition (SOURCE only when every edge claim cites a printed source line), that makes the whole route INFERRED. No REACHABLE row in this batch is claimed as pure SOURCE.

## Separable per-method table

Columns: # | Method (plan) | Descriptor | Proposed label | Kind / confirmed_by | Printed citations / route step.
"Pending grep" on UNREACHABLE rows means: the claim is a proposal only; a real full-repo grep is still required before merge, and the row flips if a caller is found. Connector `search_code` returned 0 / incomplete_results for probes in this session and was NOT used as evidence of absence.

| # | Method | Descriptor | Proposed label | Kind / confirmed_by | Printed citations / route step |
|---|---|---|---|---|---|
| 1 | NanoHTTPD$Response.getData | ()Ljava/io/InputStream; | Proposed UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:1147-1149. No printed caller in NanoHTTPD.java, TorrentStreamServer.java, or TorrentEngine.java excerpts printed; `sendBody` reads `this.data` directly (:1266-1271), not via `getData()`. Pending full-repo grep; flips if a caller is found. |
| 2 | NanoHTTPD$Response.getHeader | (Ljava/lang/String;)Ljava/lang/String; | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1150-1156. Call HTTPSession.execute :733 `r.getHeader("connection")`, via shared trunk steps 1–8. |
| 3 | NanoHTTPD$Response.getMimeType | ()Ljava/lang/String; | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1158-1160. Call `useGzipWhenAccepted` NanoHTTPD.java:1661 `r.getMimeType()`, called from HTTPSession.execute :729, via shared trunk. |
| 4 | NanoHTTPD$Response.getRequestMethod | ()Lorg/nanohttpd/NanoHTTPD$Method; | Proposed UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:1161-1163. No printed caller in the files printed; the field is written by `setRequestMethod` (:1299-1301, called at execute :728) and read directly as `this.requestMethod` in `send` (:1217, :1231, :1240), not via this getter. Pending full-repo grep; flips if found. |
| 5 | NanoHTTPD$Response.getStatus | ()Lorg/nanohttpd/NanoHTTPD$Response$IStatus; | Proposed UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:1164-1166. No printed caller for this getter in the files printed. Do not confuse with `ResponseException.getStatus` (:1317), called at execute :749 and base-serve catch :1741. `send` uses `this.status.getDescription()` directly (:1192). Pending full-repo grep; flips if found. |
| 6 | NanoHTTPD$Response.headerAlreadySent | (Ljava/util/Map;Ljava/lang/String;)Z | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1173-1179 (private static). Calls inside `send` :1205 (`"connection"`) and :1208 (`"content-length"`), via shared trunk step 9. |
| 7 | NanoHTTPD$Response.send | (Ljava/io/OutputStream;)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1185-1227 (protected). Calls HTTPSession.execute :731 (normal response), :746 (IOException path), :750 (ResponseException path), via shared trunk step 8. |
| 8 | NanoHTTPD$Response.sendBody | (Ljava/io/OutputStream;J)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1262-1275 (private). Calls `sendBodyWithCorrectEncoding` :1243 (gzip branch) and :1246 (plain branch), via `send` :1223. |
| 9 | NanoHTTPD$Response.sendBodyWithCorrectEncoding | (Ljava/io/OutputStream;J)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1239-1247 (private). Calls `sendBodyWithCorrectTransferAndEncoding` :1233 (chunked branch) and :1236 (plain branch), via `send` :1223. |
| 10 | NanoHTTPD$Response.sendBodyWithCorrectTransferAndEncoding | (Ljava/io/OutputStream;J)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1230-1237 (private). Call `send` :1223, via shared trunk step 9. |
| 11 | NanoHTTPD$Response.sendContentLengthHeaderIfNotAlreadyPresent | (Ljava/io/PrintWriter;Ljava/util/Map;J)J | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1277-1288 (protected static). Call `send` :1219, taken when not chunked and not gzip-encoded; e.g. fixed-length octet-stream responses from `TorrentStreamServer.handleTorrent` (:209, :244) reach `send` with `encodeAsGzip` false (useGzipWhenAccepted :1661 is text-only). |
| 12 | NanoHTTPD$Response.setChunkedTransfer | (Z)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1290-1292. Call `send` :1213 when `encodeAsGzip` is true; gzip is set at execute :729 via `useGzipWhenAccepted` (:1661, true for `text/` mime types, e.g. `MIME_PLAINTEXT` responses from handleTorrent). ENV gate: client `accept-encoding` containing `gzip` (execute :728-729). |
| 13 | NanoHTTPD$Response.setData | (Ljava/io/InputStream;)V | Proposed UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:1293-1295. No printed caller in the files printed; the field is set directly by the `Response` constructor (:1134-1146) and by `newFixedLengthResponse`/`newChunkedResponse` via that constructor (:1691, :1697). Pending full-repo grep; flips if found. |
| 14 | NanoHTTPD$Response.setGzipEncoding | (Z)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1167-1169. Call HTTPSession.execute :729, via shared trunk step 8. |
| 15 | NanoHTTPD$Response.setKeepAlive | (Z)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1170-1172. Call HTTPSession.execute :730, via shared trunk step 8. |
| 16 | NanoHTTPD$Response.setMimeType | (Ljava/lang/String;)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1296-1298. Call `DLNAFileType.setHeaders` TorrentStreamServer.java:281 `res.setMimeType(this.mimeType)`, called from `TorrentStreamServer.serve` :119-120 when the URI extension is mp4/avi/mkv, via virtual `serve(this)` dispatch from execute. |
| 17 | NanoHTTPD$Response.setRequestMethod | (Lorg/nanohttpd/NanoHTTPD$Method;)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1299-1301. Call HTTPSession.execute :728 `r.setRequestMethod(this.method)`, via shared trunk step 8. |
| 18 | NanoHTTPD$Response.setStatus | (Lorg/nanohttpd/NanoHTTPD$Response$IStatus;)V | Proposed UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:1302-1304. No printed caller in the files printed; the field is set directly by the `Response` constructor (:1134) and responses are created through `newFixedLengthResponse` with a status argument. Pending full-repo grep; flips if found. |
| 19 | NanoHTTPD$Response$ChunkedOutputStream.<init> | (Ljava/io/OutputStream;)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1066-1068 (private static class, :1065). Call `sendBodyWithCorrectTransferAndEncoding` :1232, chunked branch (chunked when `contentLength < 0` per constructor :1144, or when `send` sets chunked on gzip at :1213), via `send`. |
| 20 | NanoHTTPD$Response$ChunkedOutputStream.finish | ()V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1088-1090. Call `sendBodyWithCorrectTransferAndEncoding` :1234, immediately after the chunked `sendBodyWithCorrectEncoding` call, via `send`. |
| 21 | NanoHTTPD$Response$ChunkedOutputStream.write(int) | (I)V | Proposed UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:1070-1075. No printed caller in NanoHTTPD.java: the only `OutputStream.write` inside `sendBody` is the 3-arg form (:1271), and `ChunkedOutputStream.write(byte[])` itself delegates to the 3-arg form (:1078). This class is private to `Response`, so a direct caller would have to be inside NanoHTTPD.java, but the rule still requires a real full-repo grep before merge; flips if a caller is found (including via an `OutputStream` reference held elsewhere in the file). |
| 22 | NanoHTTPD$Response$ChunkedOutputStream.write(byte[]) | ([B)V | Proposed UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:1077-1079. No printed caller in NanoHTTPD.java; `sendBody` uses the 3-arg form (:1271) and `write(byte[])` only delegates to it (:1078). Same pending-grep caveat as #21. |
| 23 | NanoHTTPD$Response$ChunkedOutputStream.write(byte[],int,int) | ([BII)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1081-1087. Call `sendBody` :1271 `outputStream.write(buff, 0, read)` where `outputStream` is the `ChunkedOutputStream` in the chunked branch (`sendBodyWithCorrectTransferAndEncoding` :1232-1233 → `sendBodyWithCorrectEncoding` :1233), via `send`. |
| 24 | NanoHTTPD$Response$Status.<clinit> | ()V | REACHABLE | — / INFERRED | Enum constants NanoHTTPD.java:1024-1045. First use triggers JVM enum initialisation (INFERRED step, no FW-SRC line printed): constants are referenced by static import in TorrentStreamServer.java:38-44 and used throughout `handleTorrent` (:127-256), reached via shared trunk step 8. |
| 25 | NanoHTTPD$Response$Status.<init> | (Ljava/lang/String;IILjava/lang/String;)V | REACHABLE | — / INFERRED | Enum constructor NanoHTTPD.java:1049-1052 (`Status(int, String)` in source; the plan descriptor adds the synthetic enum name/ordinal parameters). Invoked implicitly once per constant during #24's `<clinit>` (INFERRED JVM step). |
| 26 | NanoHTTPD$Response$Status.getDescription | ()Ljava/lang/String; | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1052-1054. Call `send` :1192 `this.status.getDescription()`, via shared trunk step 9. This is the `IStatus.getDescription` implementation (:1017). |
| 27 | NanoHTTPD$Response$Status.getRequestStatus | ()I | Proposed UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:1056-1058 (`IStatus.getRequestStatus` :1018). No printed caller in the files printed; `send` uses `getDescription()`, not this method. Pending full-repo grep; flips if found. |
| 28 | NanoHTTPD$ResponseException.<init>(Status,String) | (Lorg/nanohttpd/NanoHTTPD$Response$Status;Ljava/lang/String;)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1309-1312. Throw sites e.g. `HTTPSession.decodeHeader` :503, :507, and execute :710, via ClientHandler → `session.execute()` (shared trunk steps 6–7). |
| 29 | NanoHTTPD$ResponseException.<init>(Status,String,Exception) | (Lorg/nanohttpd/NanoHTTPD$Response$Status;Ljava/lang/String;Ljava/lang/Exception;)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1313-1316. Throw sites e.g. NanoHTTPD.java:538 and :622, in code reached from `HTTPSession.execute` (decode/serve path). |
| 30 | NanoHTTPD$ResponseException.getStatus | ()Lorg/nanohttpd/NanoHTTPD$Response$Status; | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1317-1319. Calls HTTPSession.execute catch :749 `re.getStatus()` (builds the error response) and base-serve catch :1741, via shared trunk. |
| 31 | NanoHTTPD$SecureServerSocketFactory.create | ()Ljava/net/ServerSocket; | Proposed UNREACHABLE | no_trigger_in_app / INFERRED | Def NanoHTTPD.java:441-455 (class :433). The only installer printed is `makeSecure` (:1685: `new SecureServerSocketFactory(...)`), and no printed caller of `makeSecure` (or of `setServerSocketFactory` :1672) appears in the files printed; `start(timeout, daemon)` :1812 calls `getServerSocketFactory().create()` virtually, but the factory actually installed on the printed trunk is the default one, not this secure factory. Pending full-repo grep for `makeSecure` / `setServerSocketFactory` callers; flips if a secure factory is ever installed. |
| 32 | NanoHTTPD$ServerRunnable.<init> | (Lorg/nanohttpd/NanoHTTPD;I)V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1328-1330 (private). Call `createServerRunnable` :1590-1592, called from `start(timeout, daemon)` :1816, via shared trunk step 5. |
| 33 | NanoHTTPD$ServerRunnable.run | ()V | REACHABLE | — / INFERRED | Def NanoHTTPD.java:1332-1356. Reached by `new Thread(serverRunnable).start()` at `start(timeout, daemon)` :1818-1822; the Thread → `run()` dispatch itself is INFERRED (no FW-SRC thread-dispatch line printed). |
| 34 | libretorrent.DataBinderMapperImpl.<clinit> | ()V | OPEN | — / none | No definition printed: no `DataBinderMapperImpl.java` in the printed `SRC/org/proninyaroslav/libretorrent/` listing, and no `databinding/` subdirectory there. See DataBinderMapperImpl note below. Not judged. |
| 35 | libretorrent.DataBinderMapperImpl.<init> | ()V | OPEN | — / none | Same as #34. Not judged. Distinct from batch 12's `databinding.DataBinderMapperImpl.<init>` (see note). |
| 36 | libretorrent.DataBinderMapperImpl.collectDependencies | ()Ljava/util/List; | OPEN | — / none | Same as #34. Not judged. |
| 37 | libretorrent.DataBinderMapperImpl.convertBrIdToString | (I)Ljava/lang/String; | OPEN | — / none | Same as #34. Not judged. |
| 38 | libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View,int) | (Landroidx/databinding/DataBindingComponent;Landroid/view/View;I)Landroidx/databinding/ViewDataBinding; | OPEN | — / none | Same as #34. Not judged. |
| 39 | libretorrent.DataBinderMapperImpl.getDataBinder(DataBindingComponent,View[],int) | (Landroidx/databinding/DataBindingComponent;[Landroid/view/View;I)Landroidx/databinding/ViewDataBinding; | OPEN | — / none | Same as #34. Not judged. |
| 40 | libretorrent.DataBinderMapperImpl.getLayoutId | (Ljava/lang/String;)I | OPEN | — / none | Same as #34. Not judged. |

## Counts

- Batch 17 total: 40
- Proposed REACHABLE: 24 (#2, #3, #6–#12, #14–#17, #19, #20, #23–#26, #28–#30, #32, #33)
- Proposed UNREACHABLE (all `no_trigger_in_app` / INFERRED, all pending a real full-repo grep): 9 (#1, #4, #5, #13, #18, #21, #22, #27, #31)
- OPEN / not judged: 7 (#34–#40, all `libretorrent.DataBinderMapperImpl`)
- Proposed labelled: 33 / 40. Verified-judged (build + full-repo grep + C1 passed): 0 / 40 — this report is a proposal only.
- UNREACHABLE kinds used: exactly one kind per UNREACHABLE proposal (`no_trigger_in_app`); no `branch_never_taken`, `framework_never_calls`, `closed_by_configuration`, or `closed_by_api_level` row was needed in this batch.
- No row uses tool coverage, a build REACHABLE count, or an old generated graph as evidence. No row is marked `confirmed_by` SOURCE, DYN, FW-MEMORY, or UNVERIFIED.

## DataBinderMapperImpl note (batch 17 vs batch 12 — not conflated)

- Batch 17's class is `libretorrent.DataBinderMapperImpl` (plan rows 643–649; package `org.proninyaroslav.libretorrent`, i.e. the app's own package).
- Batch 12's blocked row is `databinding.DataBinderMapperImpl.<init>` — a different fully-qualified class, and its AGENT_NOTES "Blocked" entry says the upload has no `databinding/DataBinderMapperImpl.java` and that `libretorrent.DataBinderMapperImpl` exists only in build output.
- For batch 17, the printed package listing for `SRC/org/proninyaroslav/libretorrent/` contains no `DataBinderMapperImpl.java` and no `databinding/` subdirectory. That is consistent with a build-generated Android data-binding mapper (generated at compile time, not present in the `src/main/java` upload), but it is NOT, by itself, proof of reachability or unreachability: a generated mapper is normally loaded by the data-binding framework when a data-bound layout inflates, which would need printed app/layout evidence that was not fetched in this batch.
- Therefore all 7 batch-17 mapper rows stay OPEN. Before any label: (a) locate the generated mapper in build output or a generated-sources listing, (b) print the app code / layouts that trigger data binding for this package, and (c) run a full-repo grep for `DataBinderMapperImpl` references. Do not copy the batch-12 `databinding.*` conclusion onto these rows.

## Blockers / what still needs doing before merge

1. Full-repo grep (real, over the source folder, output saved in scratch/) for every proposed-UNREACHABLE method and for `makeSecure` / `setServerSocketFactory` (row #31) — required by the rules for generated/library classes and, per this task, for any UNREACHABLE claim. Connector `search_code` probes returned 0 with `incomplete_results: true` and were not used as evidence.
2. Build + sampler + C1 checks, and a check of whether any batch-17 route duplicates or conflicts with existing `graph_def.py` edges (not done; repo not edited).
3. DataBinderMapperImpl rows (#34–#40): generated-source location + data-binding trigger evidence (see note above).
4. Upstream entry: `TorrentEngineListener.onSessionStarted` → `handleOnSessionStarted` (TorrentEngine.java:1267-1269 → :1046) is a libtorrent session callback; its framework/session dispatch was not printed from FW-SRC, which is why the whole streaming trunk is INFERRED. If a future re-check prints that dispatch, the REACHABLE rows' immediate call sites are already printed and only the trunk's confirmed_by would change.
5. No push was made and no repo file was edited, per task. This report lives only in the workspace file below.
