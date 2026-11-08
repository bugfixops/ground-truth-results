# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# Batch-19 caller hunt — LibreTorrent (printed evidence only)

Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only.
Source root used for every path below:
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/`
(prefix omitted in the per-file paths for brevity; all paths are under
`org/proninyaroslav/libretorrent/` unless stated otherwise)

Method: ONE spaced, single-file-at-a-time sequence through the GitHub
connector (`get_file_contents`, one file per call, with sleeps between).
No files were edited, nothing was pushed, and no label was decided for
any other batch.

Important negative-evidence caveat: an early `search_code` query for
`FixedRingBuffer` returned `total_count: 0, incomplete_results: true`.
Per the task rules that is NOT evidence of absence — and it proved
misleading here, because a direct file read then found `FixedRingBuffer`
in `Logger.java` (see Group 1). The search result is therefore
disregarded, not cited as absence.

---

## Group 1 — FixedRingBuffer — FOUND, in Logger

### Target (already printed in full, re-read to confirm)
- `core/collections/FixedRingBuffer.java` — `public class FixedRingBuffer<E>
  implements Iterable<E>`, with ctors `FixedRingBuffer(int capacity)` and
  `FixedRingBuffer(int initCapacity, int capacity)`, and methods
  `size()`, `getAllocatedSize()`, `add(Iterable<E>)`, `add(E)`,
  `remove(E)`, `indexOf(E)`, `removeAt(int)`, `get(int)`, `clear()`,
  `isEmpty()`, `isFull()`, `contains(E)`, `iterator()` (plus private
  `resetHead()`, `tryGrow()` and inner `FixedRingBufferIterator`).

### Construction site (printed)
- `core/logger/Logger.java`
  - line 25: `import org.proninyaroslav.libretorrent.core.collections.FixedRingBuffer;`
  - lines 43–44: fields
    `protected FixedRingBuffer<LogEntry> inputBuf;`
    `protected FixedRingBuffer<LogEntry> outputBuf;`
  - lines 65–68, `lazyGetInputBuf()`:
    `inputBuf = new FixedRingBuffer<>(calcInitBufCapacity(maxStoredLogs), maxStoredLogs);`
    — the 2-arg ctor only; no 1-arg `new FixedRingBuffer(...)` was
    printed in Logger.
  - lines 86–89, `lazyGetOutputBuf()`:
    `outputBuf = new FixedRingBuffer<>(calcInitBufCapacity(maxStoredLogs), maxStoredLogs);`
  - lines 94–97: `calcInitBufCapacity(int capacity)` returns
    `(int) Math.floor(capacity / 2.0)` — so the init capacity is half
    the max, and the capacity is `maxStoredLogs`.
  - Construction is lazy, not in `Logger(int maxStoredLogs)` (lines
    57–63, which only stores `maxStoredLogs`). The buffers are created
    on first `lazyGetInputBuf()` / `lazyGetOutputBuf()` call, and set
    back to `null` at lines 492–493 (in `clean()`, context not fully
    printed beyond those lines).

### Which FixedRingBuffer methods Logger actually uses (all printed)
- `add(E)` — line 104 `lazyGetInputBuf().add(entry);` in
  `Logger.send(LogEntry)` (lines 99–104); line 154
  `outputBuf.add(entry);` in `swapBuffers()`; line 253
  `outputBuf.add(entry);` in `forceFilterBuf()`.
  The `add(Iterable<E>)` overload was NOT printed as used in Logger.
- `isEmpty()` — line 145 `if (inputBuf.isEmpty())` in `swapBuffers()`.
  (Line 164 `!newEntries.isEmpty()` is an `ArrayList`, not a buffer.)
- `size()` — line 150 `inputBuf.size()`; line 287, 309, 387, 418, 453
  `outputBuf.size()` / `lazyGetOutputBuf().size()` in `getEntries()`,
  `getEntry()`, `stopRecording()`, `write()`, `getNumEntries()`;
  line 337 in `startRecording()`.
- `get(int)` — line 152 `inputBuf.get(i)`; line 290
  `outputBuf.get(i)`; line 312 `outputBuf.get(pos)`; line 436
  `buf.get(i)` in private `write(FixedRingBuffer<LogEntry> buf, ...)`.
- `clear()` — line 249 `outputBuf.clear();` in `forceFilterBuf()`.
- `iterator()` — line 250, implicit only:
  `for (LogEntry entry : inputBuf)` in `forceFilterBuf()` — this is an
  enhanced-for over the buffer, i.e. a printed use of `iterator()`,
  whose `hasNext()`/`next()` in turn call `get()` inside
  `FixedRingBuffer` itself. No explicit `.iterator()` call was printed
  in Logger.

### FixedRingBuffer methods NOT printed as used by Logger
In the Logger file as printed, there is NO use of:
`contains(E)`, `indexOf(E)`, `remove(E)`, `removeAt(int)`,
`isFull()`, `getAllocatedSize()`, or `add(Iterable<E>)`.
(The line 233 `.remove(...)` in Logger is `filters.remove(name)` on a
`HashMap`, not a buffer call, and is excluded.)
This is a statement about Logger only. Other, unprinted files could in
principle use those methods; see "What remains unprinted" below. It is
NOT a claim that those methods are globally unused.

Internal self-use inside `FixedRingBuffer.java` itself (not an app
caller) is separate: e.g. `remove(E)` calls `indexOf`/`removeAt`,
`iterator().next()` calls `get()`, `size()` is used by several methods,
`clear()` calls `isEmpty()`/`size()`/`resetHead()`, `add(E)` calls
`tryGrow()`. The 1-arg ctor also delegates to the 2-arg ctor inside
the same file. None of that is an external caller.

### Caller chain back toward an entry point (printed)
1. `core/model/session/TorrentSessionImpl.java`
   - line 170, ctor: `this.sessionLogger = new SessionLogger();`
   - lines 179–182: `getLogger()` returns `sessionLogger`.
   - lines 1102–1103, alert handling: `if (settings.logging)
     sessionLogger.send(alert);`
2. `core/model/session/SessionLogger.java`
   - line 32: `class SessionLogger extends Logger`
   - lines 111–115: `SessionLogger()` calls `super(1);`
     (later `setMaxStoredLogs(settings.maxLogSize)` at
     `TorrentSessionImpl.java:1413`, printed only as that one line).
   - lines 117, 165–166: `send(Alert<?> alert)` builds a `LogEntry`
     for LOG / DHT_LOG / PEER_LOG / PORTMAP_LOG / TORRENT_LOG alerts
     and calls `send(entry);` — i.e. `Logger.send(LogEntry)`.
   - SessionLogger itself contains NO `FixedRingBuffer`, `inputBuf`,
     or `outputBuf` reference (printed grep: all empty).
3. `core/logger/Logger.java`
   - `send(LogEntry)` line 104: `lazyGetInputBuf().add(entry);`
     — this is the first printed buffer write, and it triggers the
     lazy `new FixedRingBuffer<>(...)` at line 68.
   - A background thread started at lines 70–71
     (`new Thread(this::periodicSwapBuffers)`) runs
     `periodicSwapBuffers()` → `swapBuffers()` (lines 113–154),
     which moves filtered entries from `inputBuf` to `outputBuf`
     via `isEmpty()` / `size()` / `get(i)` / `add(entry)`.
4. UI log viewing (printed, Logger API only, not direct buffer use):
   - `core/model/TorrentEngine.java` lines 957–959:
     `getSessionLogger()` returns `session.getLogger();`
   - `ui/log/LogViewModel.java` line 72:
     `Logger sessionLogger = engine.getSessionLogger();`
   - `ui/log/LogDataSource.java` lines 66, 70, 104, 107:
     `logger.getNumEntries()` and `logger.getEntries(...)`,
     which in Logger are lines 445–453 (`outputBuf.size()`) and
     271–290 (`outputBuf.size()` / `outputBuf.get(i)`).
   - `ui/log/LogSourceFactory.java` — Logger field only, no
     `FixedRingBuffer` (printed).

So: session alerts → `SessionLogger.send` → `Logger.send` →
`FixedRingBuffer.add`, with the ring buffers then drained through
`get`/`size`/`clear`/iteration for the log UI and for
`write(...)`/`stopRecording()`.

### Evidence status for Group 1
Printed hand route found (construction + use in Logger). No other
construction site was printed in this hunt.

---

## Group 2 — DecodeException(Exception) — FOUND, multiple sites

### Target (printed in full)
- `core/exception/DecodeException.java`
  - lines 26–39: `public class DecodeException extends Exception`
  - line 28: `DecodeException()`; lines 30–33: `DecodeException(String)`;
  - lines 35–39, the group ctor:
    ```
    public DecodeException(Exception e)
    {
        super(e.getMessage());
        super.setStackTrace(e.getStackTrace());
    }
    ```

### Construction sites for the (Exception) ctor (all printed)
All four sites below use the exact form `throw new DecodeException(e);`
inside a `catch (Exception e)` block, i.e. the (Exception) ctor, not
the String ctor.

1. `core/model/data/metainfo/TorrentMetaInfo.java` — the torrent-file
   decode path itself:
   - lines 63–70, `TorrentMetaInfo(@NonNull byte[] data)`:
     ```
     try { getMetaInfo(TorrentInfo.bdecode(data)); }
     catch (Exception e) { throw new DecodeException(e); }   // line 69
     ```
   - lines 73–80, `TorrentMetaInfo(TorrentInfo info)`:
     ```
     try { getMetaInfo(info); }
     catch (Exception e) { throw new DecodeException(e); }   // line 79
     ```
   - lines 83–96, `TorrentMetaInfo(FileInputStream is)`:
     ```
     try { chan = is.getChannel();
           getMetaInfo(new TorrentInfo(chan.map(...))); }
     catch (Exception e) { throw new DecodeException(e); }   // line 92
     finally { IOUtils.closeQuietly(chan); }
     ```

2. `core/model/TorrentEngine.java` — a second, wrapping site:
   - lines 374–394, `addTorrentCompletable(@NonNull Uri file,
     @Nullable Uri savePath)`:
     ```
     TorrentMetaInfo info = null;
     try (FileDescriptorWrapper w = fs.getFD(file)) {
         ...
         try (FileInputStream is = new FileInputStream(outFd)) {
             info = new TorrentMetaInfo(is);                 // line 384
         } catch (Exception e) {
             throw new DecodeException(e);                   // line 387
         }
         addTorrentSync(file, info, savePath);
     } catch (Exception e) {
         handleAddTorrentError(...);
     }
     ```
     Note the double wrap: `new TorrentMetaInfo(is)` at line 384 can
     already throw `DecodeException` from `TorrentMetaInfo.java:92`,
     and the outer `catch (Exception e)` at line 386 then wraps it
     again at line 387. Both sites are printed; this does not change
     the fact that line 387 is a `new DecodeException(e)` site.

### Other printed DecodeException references (NOT construction sites)
- `TorrentEngine.java` line 36: import; line 407: `addTorrentSync`
  declares `throws ... DecodeException ...`; line 466:
  `catch (DecodeException e)` in `sendInfoToEmitter` (after
  `new TorrentMetaInfo(bencode)` at line 464, whose own ctor throws at
  `TorrentMetaInfo.java:69`); line 633: `catch (DecodeException e)`
  in `getTorrentMetaInfo`; line 1181: another `throws DecodeException`
  declaration (in a second `addTorrentSync` overload, context printed
  only as that declaration line).
- `core/model/session/TorrentSession.java` line 65: `throws
  DecodeException` declaration only; no construction.
- `core/model/session/TorrentSessionImpl.java` line 257: `throws
  DecodeException` declaration only; line 299:
  `TorrentMetaInfo info = new TorrentMetaInfo(is);` inside
  `addTorrent(...)` with only a `FileNotFoundException` catch
  (lines 303–305) — i.e. a `DecodeException` from that ctor propagates
  via the declared `throws`, it is NOT re-wrapped there with
  `new DecodeException(`.
- `core/model/session/TorrentDownloadImpl.java` lines 1186–1201:
  `getTorrentMetaInfo() throws DecodeException` builds
  `new TorrentMetaInfo(ti)` / `new TorrentMetaInfo(name, hash)` —
  no `new DecodeException(` printed there.
- `ui/addtorrent/AddTorrentViewModel.java` line 281:
  `readTorrentFile(Uri uri) throws IOException, DecodeException`,
  line 293: `v.info.set(new TorrentMetaInfo(is));` — again propagation,
  not construction.
- `ui/addtorrent/AddTorrentActivity.java` line 460:
  `if (e instanceof DecodeException)` — error-dialog handling only.

### Caller chain back toward an entry point (printed)
File-decode route:
- `ui/addtorrent/AddTorrentActivity.java` lines 305–312,
  `observeDecodeState()`: on `UNKNOWN` state, `viewModel.startDecode(uri)`.
- `ui/addtorrent/AddTorrentViewModel.java` lines 182–200:
  `startDecode(Uri)` → (once engine running) `startDecodeTask(uri)`
  → `new TorrentDecodeTask(this).executeOnExecutor(...)`.
- Same file, lines 217–272, `TorrentDecodeTask.doInBackground`:
  for a file/content URI it sets the source, then line 272
  `readTorrentFile(Uri.parse(tmpSource))`; for an http/https URI it
  first fetches (see Group 3) and then also reaches line 272.
- Lines 281–293, `readTorrentFile`: `new TorrentMetaInfo(is)` at
  line 293 → `TorrentMetaInfo(FileInputStream)` ctor →
  `new DecodeException(e)` at `TorrentMetaInfo.java:92` on failure;
  the exception is caught as `Throwable` at lines 274–275, posted as
  an ERROR decode state, and shown by `AddTorrentActivity.java:460`
  as the decode-error dialog.
Magnet/bencode route:
- `TorrentEngine.java` lines 461–471, `sendInfoToEmitter`:
  `new TorrentMetaInfo(bencode)` at line 464 →
  `new DecodeException(e)` at `TorrentMetaInfo.java:69` on failure,
  caught at line 466 and sent to `emitter.onError(e)`.
Engine file-add route:
- `TorrentEngine.java` `addTorrent(Uri)` (lines 359–361) →
  `addTorrentCompletable` (lines 374–394) → line 384 →
  `TorrentMetaInfo.java:92`, then line 387 re-wrap, then
  `handleAddTorrentError` at lines 391–392.

### Evidence status for Group 2
Printed hand routes found, in the torrent-file decode path
(`TorrentMetaInfo` ctors + `TorrentEngine.addTorrentCompletable`).

---

## Group 3 — FetchLinkException(Exception) — FOUND, in Utils.fetchHttpUrl

### Target (printed in full)
- `core/exception/FetchLinkException.java`
  - lines 26–39: `public class FetchLinkException extends Exception`
  - line 28: `FetchLinkException()`; lines 30–33:
    `FetchLinkException(String message)`;
  - lines 35–38, the group ctor:
    ```
    public FetchLinkException(Exception e)
    {
        super(e);
    }
    ```

### Construction site for the (Exception) ctor (printed)
- `core/utils/Utils.java`
  - line 65: import of `FetchLinkException`.
  - lines 462–463: `public static byte[] fetchHttpUrl(@NonNull Context
    context, @NonNull String url) throws FetchLinkException {`
  - lines 471–475:
    ```
    try {
        connection = new HttpConnection(url);
    } catch (Exception e) {
        throw new FetchLinkException(e);   // line 474 — the (Exception) ctor
    }
    ```
  This is the ONLY (Exception)-ctor site printed in this hunt.

### Other FetchLinkException sites in the same method (String ctor, NOT this group)
- line 467: `throw new FetchLinkException("No network connection");`
- line 493: `errorArray.add(new FetchLinkException("Failed to fetch link, response code: " + code));`
- line 509: `errorArray.add(new FetchLinkException("Too many redirects"));`
- line 522: `throw new FetchLinkException(s.toString());`
  (after collecting errors from the `HttpConnection.Listener`
  callbacks at lines 477–511; `connection.run()` at line 512).
These are listed only to avoid confusing them with line 474.

### Other printed FetchLinkException references (NOT construction sites)
- `TorrentEngine.java`: no `FetchLinkException` reference at all
  (printed grep empty); its magnet path is `fetchMagnet` /
  `createFetchMagnetSingle` (lines 415–459), not a link fetch.
- `ui/addtorrent/AddTorrentActivity.java` line 50: import;
  lines 476–490: `else if (e instanceof FetchLinkException)` —
  fetch-error dialog (`error_fetch_link`) handling only.
- `ui/addlink/AddLinkViewModel.java`, `AddLinkDialog.java`,
  `AddLinkActivity.java`: no `FetchLinkException` and no
  `fetchHttpUrl` printed.

### Caller chain back toward an entry point (printed)
1. `ui/addtorrent/AddTorrentActivity.java` lines 305–312,
   `observeDecodeState()`: on `UNKNOWN` state,
   `viewModel.startDecode(uri)` (line 312).
2. `ui/addtorrent/AddTorrentViewModel.java` lines 182–200:
   `startDecode(Uri)` → `startDecodeTask(uri)` →
   `TorrentDecodeTask.executeOnExecutor(...)`.
3. Same file, lines 217–264, `TorrentDecodeTask.doInBackground`:
   http/https branch (lines 249–264):
   ```
   v.decodeState.postValue(new DecodeState(Status.FETCHING_HTTP));
   File httpTmp = v.fs.makeTempFile(".torrent");          // line 253
   byte[] response = Utils.fetchHttpUrl(v.getApplication(), uri.toString());  // line 254
   org.apache.commons.io.FileUtils.writeByteArrayToFile(httpTmp, response);
   ... v.mutableParams.setSource(... httpTmp ...);
   ```
   then line 272 `readTorrentFile(...)` decodes the downloaded file.
   Any `Throwable` (including a `FetchLinkException` from line 254)
   is caught at lines 274–275, returned, and posted as an ERROR
   decode state (lines 300–308), which `AddTorrentActivity.java:476`
   renders as the fetch-link error dialog.
4. `core/utils/Utils.java` lines 462–475, `fetchHttpUrl`:
   no-network → String ctor at line 467; `new HttpConnection(url)`
   throwing → (Exception) ctor at line 474; HTTP error / redirect
   errors collected and re-thrown as a String-ctor exception at
   line 522.

So the torrent/magnet link fetch path for the (Exception) ctor is:
AddTorrent UI → `startDecode` → `TorrentDecodeTask` http/https branch
→ `Utils.fetchHttpUrl` → `new HttpConnection(url)` failure →
`new FetchLinkException(e)` at `Utils.java:474`.

### Evidence status for Group 3
Printed hand route found, in the torrent-link (http/https) fetch path.

---

## Files actually checked in this hunt (single-file sequence)

Target / definition files, all printed in full or by grep + context:
- `core/collections/FixedRingBuffer.java`
- `core/exception/DecodeException.java`
- `core/exception/FetchLinkException.java`
- `core/model/data/metainfo/TorrentMetaInfo.java`
- `core/logger/Logger.java`
- `core/model/session/SessionLogger.java`

Caller / candidate files, each printed and grepped for all three
symbols (`FixedRingBuffer`, `DecodeException`, `FetchLinkException`)
unless noted:
- `core/model/TorrentEngine.java` — FixedRingBuffer: none;
  DecodeException: import + 387 (construction) + throws/catches;
  FetchLinkException: none.
- `core/model/session/TorrentSession.java` — FixedRingBuffer: none;
  DecodeException: throws declaration only; FetchLinkException: none.
- `core/model/session/TorrentSessionImpl.java` — FixedRingBuffer:
  none; DecodeException: throws declaration only;
  FetchLinkException: none.
- `core/model/session/TorrentDownloadImpl.java` — FixedRingBuffer:
  none; DecodeException: throws declaration only;
  FetchLinkException: none.
- `core/TorrentBuilder.java`, `core/FeedParser.java`,
  `core/HttpConnection.java` — all three symbols: none.
- `core/utils/Utils.java` — FixedRingBuffer: none;
  DecodeException: none; FetchLinkException: 474 (Exception ctor)
  + String-ctor sites 467, 493, 509, 522.
- `ui/addlink/AddLinkViewModel.java`, `ui/addlink/AddLinkDialog.java`,
  `ui/addlink/AddLinkActivity.java` — all three symbols: none
  (AddLinkDialog also grepped for `fetch`: none).
- `ui/addtorrent/AddTorrentViewModel.java` — FixedRingBuffer: none;
  FetchLinkException: none directly, but `fetchHttpUrl` call at 254;
  DecodeException: throws declaration at 281.
- `ui/addtorrent/AddTorrentActivity.java` — FixedRingBuffer: none;
  `startDecode` at 312; DecodeException handling at 460;
  FetchLinkException handling at 476.
- `ui/detailtorrent/DetailTorrentViewModel.java` —
  FixedRingBuffer: none.
- `ui/log/LogViewModel.java` — FixedRingBuffer: none; Logger via
  `engine.getSessionLogger()` at 72.
- `ui/log/LogDataSource.java`, `ui/log/LogSourceFactory.java` —
  FixedRingBuffer: none; Logger API use only.

Directory listings printed (names only, to locate the files above):
`core/`, `core/model/`, `core/model/session/`, `core/collections/`,
`core/exception/`, `core/utils/`, `ui/`, `ui/addlink/`,
`ui/addtorrent/`, `ui/detailtorrent/`, `ui/log/`,
`org/proninyaroslav/libretorrent/`.
Note: an earlier attempt to read
`core/model/TorrentSession.java` failed (no such file) — the real file
is `core/model/session/TorrentSession.java`, which was then checked.

## What remains unprinted / not claimed
- The full app tree was NOT exhaustively printed. A second
  `FixedRingBuffer` construction site, a second
  `FetchLinkException(Exception)` site, or additional
  `DecodeException(Exception)` sites in files not listed above
  cannot be ruled out from this hunt, and none is claimed.
- Conversely, the three routes above ARE printed, so none of the
  three groups is "NOT FOUND" on this evidence.
- For FixedRingBuffer, only Logger's usage was printed in full
  detail. Whether any unprinted file uses `contains`, `indexOf`,
  `remove`, `removeAt`, `isFull`, `getAllocatedSize`, or
  `add(Iterable)` remains unprinted — the report above states only
  that Logger does not use them.
- For DecodeException, the String-ctor and no-arg ctor sites were
  not hunted (the group was the Exception ctor only); `TorrentEngine`
  line 387's double-wrap behaviour is noted from printed lines only.
- No repo file was edited and nothing was pushed, per the task.
- `search_code` for `FixedRingBuffer` gave `total_count: 0,
  incomplete_results: true` and was disregarded as evidence, per
  the task rules.
