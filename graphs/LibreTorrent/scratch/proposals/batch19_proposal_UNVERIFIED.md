# UNVERIFIED PROPOSAL — has NOT passed build, sampler, full-repo grep, or C1 checks; re-check from printed source before relying/merging.

# LibreTorrent batch 19 — proposal, UNVERIFIED, NOT merged

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only.
Membership: exactly 40 rows in handoff/LIBRETORRENT_BATCH_PLAN.tsv (SHA 0104806dd666c840049b3db52823d4b384fa1c92), all TODO_CANDIDATE_REACHABLE — candidates, not evidence.
Status: UNVERIFIED proposal. No build, sampler, full-repo grep, or C1 check was run for this batch, and no such count is claimed. No graph_def.py / out/ edit was made, nothing was pushed by the helpers in this stage.
Rules: confirmed_by SOURCE only where lines were printed, otherwise INFERRED, never DYN / FW-MEMORY / UNVERIFIED. Tool coverage, old generated graphs, and build REACHABLE counts are never evidence. Connector search_code 0/incomplete is NOT evidence of absence — in this batch it returned 0 for FixedRingBuffer and was proved misleading by a direct read of Logger.java, and is disregarded.

## Counts (proposal, not verified)
- Judged: 32 / 40 REACHABLE proposed, 0 UNREACHABLE proposed, 8 OPEN.
- TorrentBuilder group: 18 / 18 REACHABLE proposed.
- TorrentFileObserver: 0 / 1, OPEN.
- FixedRingBuffer group: 12 / 19 REACHABLE proposed, 7 OPEN.
- Exception group: 2 / 2 REACHABLE proposed.

## TorrentBuilder group — 18 REACHABLE proposed

Shared printed route:
- CreateTorrentDialog.java:546 calls its own buildTorrent(); :338-345 `viewModel.buildTorrent()`.
- CreateTorrentViewModel.java: buildTorrent() calls makeBuilder(), then builder.observeProgress() and builder.build().
- CreateTorrentViewModel.makeBuilder() calls, in order: `new TorrentBuilder(getApplication())`, `.setSeedPath(seedPath)`, `.setPieceSize(...)`, `.setTorrentVersion(getTorrentVersionByIndex(...))`, `.addTrackers(getAndValidateTrackers())`, `.addUrlSeeds(...)`, `.setAsPrivate(...)`, `.setCreator(makeCreator())`, `.setComment(...)`, `.setFileNameFilter(...)`.
- TorrentBuilder.java: setSeedPath :94-101, setPieceSize :109-114, setAsPrivate :134-139, setCreator :141-146, setComment :148-153, setFileNameFilter :155-160, setTorrentVersion :162-166 (calls version.flag() :163), observeProgress :168-171, build :173-178, subscribeProgress :180-200 (creates anonymous Listener :182-199).
- Tracker.<init> :55-59; constructed in CreateTorrentViewModel.getAndValidateTrackers() as `new TorrentBuilder.Tracker(url, tier++)`.
- Progress.<init> :65-69; constructed in TorrentBuilder$1.progress :197.
- TorrentVersion enum :72-86; constants :73-75, flag() :79-81, ctor :83-85. Returned by CreateTorrentViewModel.getTorrentVersionByIndex() (HYBRID / V1_ONLY / V2_ONLY); flag() called by setTorrentVersion :163.
- TorrentBuilder$1.<init> / accept / progress: anonymous Listener :182-199; accept :184-192, progress :195-198. Library callback dispatch INFERRED, bodies SOURCE.
- lambda$build$0: Single.fromCallable lambda in build() :177 `() -> builder.generate().entry().bencode()`; executed when subscribed in CreateTorrentViewModel.buildTorrent(). Rx dispatch INFERRED, lambda body SOURCE.

| # | Method | Label | confirmed_by | Citations |
|---|---|---|---|---|
| 1 | TorrentBuilder.lambda$build$0 | REACHABLE | SOURCE body / INFERRED Rx dispatch | TorrentBuilder.java:177; subscribed CreateTorrentViewModel.buildTorrent() |
| 2 | TorrentBuilder.observeProgress | REACHABLE | SOURCE | TorrentBuilder.java:168-171; called buildTorrent() |
| 3 | TorrentBuilder.setAsPrivate | REACHABLE | SOURCE | TorrentBuilder.java:134-139; called makeBuilder() |
| 4 | TorrentBuilder.setComment | REACHABLE | SOURCE | TorrentBuilder.java:148-153; called makeBuilder() |
| 5 | TorrentBuilder.setCreator | REACHABLE | SOURCE | TorrentBuilder.java:141-146; called makeBuilder() |
| 6 | TorrentBuilder.setFileNameFilter | REACHABLE | SOURCE | TorrentBuilder.java:155-160; called makeBuilder() |
| 7 | TorrentBuilder.setPieceSize | REACHABLE | SOURCE | TorrentBuilder.java:109-114; called makeBuilder() |
| 8 | TorrentBuilder.setSeedPath | REACHABLE | SOURCE | TorrentBuilder.java:94-101; called makeBuilder() |
| 9 | TorrentBuilder.setTorrentVersion | REACHABLE | SOURCE | TorrentBuilder.java:162-166; called makeBuilder() |
| 10 | TorrentBuilder.subscribeProgress | REACHABLE | SOURCE | TorrentBuilder.java:180-200; called build() :175 |
| 11 | TorrentBuilder$1.<init> | REACHABLE | SOURCE | TorrentBuilder.java:182-199 |
| 12 | TorrentBuilder$1.accept | REACHABLE | INFERRED (library callback) | TorrentBuilder.java:184-192; registered :182 |
| 13 | TorrentBuilder$1.progress | REACHABLE | INFERRED (library callback) | TorrentBuilder.java:195-198; registered :182; constructs Progress :197 |
| 14 | TorrentBuilder$Progress.<init> | REACHABLE | SOURCE | TorrentBuilder.java:65-69; constructed :197 |
| 15 | TorrentBuilder$TorrentVersion.<clinit> | REACHABLE | INFERRED (JVM enum init) | TorrentBuilder.java:72-75; returned by getTorrentVersionByIndex() |
| 16 | TorrentBuilder$TorrentVersion.<init> | REACHABLE | INFERRED (JVM enum init) | TorrentBuilder.java:83-85 |
| 17 | TorrentBuilder$TorrentVersion.flag | REACHABLE | SOURCE | TorrentBuilder.java:79-81; called setTorrentVersion :163 |
| 18 | TorrentBuilder$Tracker.<init> | REACHABLE | SOURCE | TorrentBuilder.java:55-59; constructed getAndValidateTrackers() |

Caveat, not hidden: the dialog-display step that shows CreateTorrentDialog itself was not printed in this session; the route is anchored at CreateTorrentDialog.buildTorrent() :338-345/:546, a standard DialogFragment button path. Under a strict entry-route rule requiring a printed launcher-to-dialog step, these 18 would be OPEN, not REACHABLE — the same caveat as batch 16.

## TorrentFileObserver — 1 OPEN
- TorrentFileObserver.<init>(String) : core/TorrentFileObserver.java, abstract class extending android.os.FileObserver, ctor calls super(pathToDir, mask) where mask = CREATE | MOVED_TO | MODIFY | ATTRIB. No subclass construction site was printed in this session. Abstract-class ctor runs only via a subclass, so without a printed subclass it is OPEN, not judged, not UNREACHABLE.

## FixedRingBuffer group — 12 REACHABLE proposed, 7 OPEN

Printed route (caller hunt, spaced single-file):
- core/logger/Logger.java: fields inputBuf/outputBuf :43-44; lazyGetInputBuf() :65-68 `new FixedRingBuffer<>(calcInitBufCapacity(maxStoredLogs), maxStoredLogs)`; lazyGetOutputBuf() :86-89 same; calcInitBufCapacity :94-97.
- Logger.send(LogEntry) :99-104 calls lazyGetInputBuf().add(entry) :104.
- Logger.swapBuffers() :113-154 uses inputBuf.isEmpty() :145, inputBuf.size() :150, inputBuf.get(i) :152, outputBuf.add(entry) :154.
- Logger.forceFilterBuf() : outputBuf.add(entry) :253, outputBuf.clear() :249, `for (LogEntry entry : inputBuf)` :250 (enhanced-for = iterator()).
- Logger.getEntries()/getEntry()/stopRecording()/write()/getNumEntries() use outputBuf.size() / get(i) at :287, :290, :309, :312, :337, :387, :418, :436, :453.
- Upstream: TorrentSessionImpl.java:170 `new SessionLogger()`, :1102-1103 sessionLogger.send(alert) when settings.logging; SessionLogger.java:32 extends Logger, :111-115 super(1), :117/:165-166 send(alert) -> send(entry) -> Logger.send. UI: TorrentEngine.java:957-959 getSessionLogger(), LogViewModel.java:72, LogDataSource.java:66/70/104/107 getNumEntries()/getEntries() — Logger API only, no direct buffer use.
- Internal self-use in FixedRingBuffer.java itself: add(Object) calls tryGrow(); clear() calls isEmpty()/resetHead(); iterator() returns new FixedRingBufferIterator; iterator.next() calls get(index++).

| Method | Label | confirmed_by | Citations |
|---|---|---|---|
| FixedRingBuffer.<init>(int,int) | REACHABLE | SOURCE | Logger.java:68, :89 |
| FixedRingBuffer.add(Object) | REACHABLE | SOURCE | Logger.java:104, :154, :253 |
| FixedRingBuffer.clear | REACHABLE | SOURCE | Logger.java:249 (forceFilterBuf) |
| FixedRingBuffer.get | REACHABLE | SOURCE | Logger.java:152, :290, :312, :436 |
| FixedRingBuffer.isEmpty | REACHABLE | SOURCE | Logger.java:145 |
| FixedRingBuffer.iterator | REACHABLE | SOURCE (for-loop) / INFERRED (compiler iterator call) | Logger.java:250 |
| FixedRingBuffer.size | REACHABLE | SOURCE | Logger.java:150, :287, :309, :387, :418, :453 |
| FixedRingBuffer.tryGrow | REACHABLE | SOURCE (internal) | FixedRingBuffer.add(Object) calls tryGrow() |
| FixedRingBuffer.resetHead | REACHABLE | SOURCE (internal) | FixedRingBuffer.clear() calls resetHead() |
| FixedRingBuffer$FixedRingBufferIterator.<init> | REACHABLE | SOURCE (internal) | FixedRingBuffer.iterator() returns new FixedRingBufferIterator |
| FixedRingBuffer$FixedRingBufferIterator.hasNext | REACHABLE | INFERRED (for-loop dispatch) | Logger.java:250 for-loop over inputBuf |
| FixedRingBuffer$FixedRingBufferIterator.next | REACHABLE | INFERRED (for-loop dispatch) | Logger.java:250 for-loop; next() calls get() internally |

OPEN (Logger does not use them, and no other caller was printed — this is NOT a global-unused claim, pending a full-repo grep):
- FixedRingBuffer.add(Iterable) — add(Object) is used, the Iterable overload was not printed as used.
- FixedRingBuffer.contains, indexOf, remove, removeAt, isFull, getAllocatedSize — no printed Logger use; remove() internally calls indexOf()/removeAt(), but remove() itself was not printed as called, so those stay OPEN, not REACHABLE via internal self-use alone.
- Note: the 1-arg FixedRingBuffer(int) ctor is NOT in batch 19 (only (int,int) is); it delegates to (int,int) inside the file, but that row is not judged here.

## Exception group — 2 REACHABLE proposed

- DecodeException.<init>(Exception) — REACHABLE, SOURCE. core/exception/DecodeException.java:35-39. Construction sites printed: core/model/data/metainfo/TorrentMetaInfo.java:69 (byte[] ctor), :79 (TorrentInfo ctor), :92 (FileInputStream ctor), all `throw new DecodeException(e)` in catch (Exception e); plus TorrentEngine.java:387 in addTorrentCompletable (double-wrap of TorrentMetaInfo.java:92). Route: AddTorrentActivity.java:305-312 observeDecodeState -> viewModel.startDecode(uri); AddTorrentViewModel.java:182-200 startDecode -> TorrentDecodeTask; :217-272 doInBackground -> :281-293 readTorrentFile -> new TorrentMetaInfo(is) :293 -> TorrentMetaInfo.java:92 on failure; also TorrentEngine.java:461-471 sendInfoToEmitter new TorrentMetaInfo(bencode) :464 -> TorrentMetaInfo.java:69.
- FetchLinkException.<init>(Exception) — REACHABLE, SOURCE. core/exception/FetchLinkException.java:35-38 super(e). Construction site printed: core/utils/Utils.java:474 `throw new FetchLinkException(e)` in fetchHttpUrl() :462-475, on `new HttpConnection(url)` failure. Route: AddTorrentActivity observeDecodeState -> AddTorrentViewModel.startDecode -> TorrentDecodeTask http/https branch :249-264, Utils.fetchHttpUrl :254, then readTorrentFile :272; error caught :274-275 and rendered as fetch-link dialog at AddTorrentActivity.java:476. String-ctor sites in Utils.java:467, :493, :509, :522 are NOT this row and are not conflated with it.

## What remains for batch 19
- 8 OPEN rows need a full-repo grep / printed subclass or caller before any UNREACHABLE verdict: TorrentFileObserver subclass, and FixedRingBuffer add(Iterable)/contains/indexOf/remove/removeAt/isFull/getAllocatedSize in any file other than Logger.
- No batch is verified for merge; no build/sampler/grep/C1 count is claimed. Next: batch 20 in plan order, then WP2/WP3 in parallel without bursting the connector, WP4 only after WP1 reaches [L], WP5/WP6 only after WP6 gates.
- Full caller-hunt evidence: [batch19_caller_hunt.md](sandbox://workspace/batch19_caller_hunt.md)
