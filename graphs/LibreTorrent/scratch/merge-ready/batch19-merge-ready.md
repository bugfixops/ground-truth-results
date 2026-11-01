# LibreTorrent batch 19 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED merge-ready part only. NOT verified for merge. NOT pushed. No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's files.**

**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 19 only, 40 methods, no other batch, no other app, no device replay, no Aegis.
- No token, no git clone (a true git clone fails in this VM with no credential device — named missing check, not passed). Work is via the GitHub connector only, one file at a time with ~20 s pauses. No fresh HTTP 429 was hit in this pass. No connector `search_code` 0-result was used as evidence of absence.

## Membership — verified first, not guessed

Exactly the 40 batch-19 rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (local plan copy `~/workspace/agent27-plan.tsv`, plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`, in plan order:
1–18 `TorrentBuilder` (incl. `$1` anonymous Listener, `Progress`, `TorrentVersion`, `Tracker`); 19 `TorrentFileObserver`; 20–38 `FixedRingBuffer` (incl. `FixedRingBufferIterator`); 39–40 exception ctors.

Note: the 1-arg `FixedRingBuffer(int)` ctor is NOT in batch 19 (only `(int,int)` is, row 20). It delegates to `(int,int)` inside the file, but that row is not judged here and no verdict is copied to or from it.

## Printed source — freshly fetched in this pass

Saved in `~/workspace/b171819-src/`, branch `work-2026-10-31`, one file at a time with pauses. SHA-256 values are of the saved connector text:

- `org/proninyaroslav/libretorrent/core/TorrentBuilder.java` — 201 lines, SHA `4b02ea5ed479d57a7d9ba4423474da3f436e999302112dc0c48744798a13be8e`.
- `org/proninyaroslav/libretorrent/ui/createtorrent/CreateTorrentViewModel.java` — 406 lines, SHA `7f175b1db8ca5de2bfa0e0baa9b0037b3c54dad348fc7af9fa7d1d31380eb4d9`.
- `org/proninyaroslav/libretorrent/core/model/TorrentEngine.java` — 1,658 lines, SHA `5845b68c9b83bb6a84fb329074c135eeae58652426204485f9265dd9be7c6cd2`.
- `org/proninyaroslav/libretorrent/core/TorrentFileObserver.java` — 41 lines, SHA `a72366246d660672173a03c5e66911d26154d85160e8e75c1def5ef644b5d054`.
- `org/proninyaroslav/libretorrent/core/collections/FixedRingBuffer.java` — 230 lines, SHA `cb7d1b3aa2bbea8492ebc04595278e97c16d7caa699ed95968ab71eaa2cfc6e0`.
- `org/proninyaroslav/libretorrent/core/logger/Logger.java` — 538 lines, SHA `026218bcf9d1ed9f54838daef5336688057f8830a26d631f2ab1d1bd2d9c0a42`.
- `org/proninyaroslav/libretorrent/core/exception/DecodeException.java` — 40 lines, SHA `492869c6cb583928266c35ff17e0cde3dd9a27daa77c825d9f4b9cb689a9058b`.
- `org/proninyaroslav/libretorrent/core/exception/FetchLinkException.java` — 39 lines, SHA `171984d8990dbfebb055fcdb75fff31d2b28e01430e058eccdbb69e2a400d307`.
- `org/proninyaroslav/libretorrent/core/model/data/metainfo/TorrentMetaInfo.java` — 210 lines, SHA `e30d2ff36485e7cd6286c843de7c09a64bc51b5b6fde078e9122d3d74d21e111`.
- `org/proninyaroslav/libretorrent/core/utils/Utils.java` — 926 lines, SHA `e2ca2ece8da2673be4c388d733f250d36c061dd231fac71889311e6ea0afd0e9`.

Prior work used as INPUT / lead list only: `~/workspace/libretorrent-batch19-proposal.md` with its Agent 4 update (33 REACHABLE proposed / 0 UNREACHABLE / 7 OPEN). Every row below was re-checked against the fresh prints above; no verdict was copied without that re-check. In this pass, unlike the proposal pass, ALL of the following were freshly printed (not local-corpus only): the TorrentBuilder chain, the TorrentFileObserver definition and its TorrentEngine call sites, the FixedRingBuffer definition and its Logger call sites, and both exception definitions with their construction sites.

## Shared routes — freshly printed

**TorrentBuilder route (rows 1–18).** `CreateTorrentDialog` → `CreateTorrentViewModel.buildTorrent()` :151–175 (`makeBuilder()` :157, `builder.observeProgress()` :166–169, `builder.build()` :171–173, subscribed) → `makeBuilder()` :177+ (`new TorrentBuilder(getApplication())` :189, `.setSeedPath(seedPath)` :190, `.setPieceSize(...)` :191, `.setTorrentVersion(getTorrentVersionByIndex(...))` :192, `.addTrackers(getAndValidateTrackers())` :193, `.addUrlSeeds(getAndValidateWebSeeds())` :194, `.setAsPrivate(...)` :195, `.setCreator(makeCreator())` :196, `.setComment(...)` :197, `.setFileNameFilter(...)` :198+). The dialog-display step that shows `CreateTorrentDialog` itself was NOT printed in this pass — see strict-entry below. `getAndValidateTrackers()` constructs `new TorrentBuilder.Tracker(url, tier++)` at :275. `getTorrentVersionByIndex()` :338–348 returns HYBRID / V1_ONLY / V2_ONLY.

**TorrentFileObserver route (row 19).** `TorrentEngine.handleOnSessionStarted()` (session-start trunk, batch 17) → `startWatchDir()` :1116 (called :1054 when `pref.watchDir()` is true, and :1583/:1590 on watch-dir preference change) → `makeTorrentFileObserver()` :1136–1137 (`return new TorrentFileObserver(pathToDir) { ... onEvent ... }` — an anonymous subclass, so the abstract ctor runs) → `TorrentFileObserver.<init>(String)` :35–37 (`super(pathToDir, mask)`).

**Logger → FixedRingBuffer route (rows 20–38).** `Logger.java`: import `FixedRingBuffer` :25, fields `inputBuf`/`outputBuf` :43–44, `lazyGetInputBuf()` :65–68 (`new FixedRingBuffer<>(calcInitBufCapacity(maxStoredLogs), maxStoredLogs)` :68, 2-arg ctor only), `lazyGetOutputBuf()` :86–89 (same 2-arg construction :89), `Logger.send` calls `lazyGetInputBuf().add(entry)` :104, `swapBuffers` uses `inputBuf.isEmpty()` :145, `inputBuf.size()` :150, `inputBuf.get(i)` :152, `outputBuf.add(entry)` :154, `forceFilterBuf` uses `outputBuf.clear()` :249, `for (LogEntry entry: inputBuf)` :250 (enhanced-for = `iterator()`), `outputBuf.add(entry)` :253, `getEntries`/`getEntry`/`write`/`getNumEntries` use `outputBuf.size()` / `get(i)` at :287, :290, :309, :312, :337, :387, :418, :436, :453. Upstream (prior proposal, not re-fetched here, and NOT cited as fresh evidence for any row): `TorrentSessionImpl` SessionLogger → `Logger.send`; UI `LogViewModel`/`LogDataSource` Logger API only, no direct buffer use.

**Exception routes (rows 39–40).** See rows 39–40.

## Per-row judgements

`confirmed_by` here is PER-ROW (SOURCE = a printed direct app-code call site naming the method, including a printed internal call from a REACHABLE method in the same class; INFERRED = unprinted library/Rx/JVM dispatch with registration/subscription printed). Under a WHOLE-ROUTE convention, rows whose route crosses an unprinted dispatch (Rx subscription, library Listener callback, enhanced-for iterator dispatch, JVM enum init) would read INFERRED; labels are unaffected, only `confirmed_by` would change. That convention is recorded, not decided. OPEN rows carry no `confirmed_by` (shown as `—`).

| # | Method | Label proposed | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | TorrentBuilder.lambda$build$0 `()[B` | REACHABLE proposed | INFERRED | TorrentBuilder.java:177 `Single.fromCallable(() -> builder.generate().entry().bencode())` — the `() -> ...` lambda body is printed (SOURCE body), but its execution happens on Rx subscription (CreateTorrentViewModel.java:171–173 `builder.build()` subscribed) through unprinted Rx dispatch, hence INFERRED. Lambda numbering is source-order, not bytecode-verified. |
| 2 | TorrentBuilder.observeProgress `()Lio/reactivex/Observable;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:168–171. Call CreateTorrentViewModel.java:166–169 (`builder.observeProgress()` in `buildTorrent()`). |
| 3 | TorrentBuilder.setAsPrivate `(Z)Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:134–139. Call CreateTorrentViewModel.java:195 (in `makeBuilder()`). |
| 4 | TorrentBuilder.setComment `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:148–153. Call CreateTorrentViewModel.java:197 (in `makeBuilder()`). |
| 5 | TorrentBuilder.setCreator `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:141–146. Call CreateTorrentViewModel.java:196 (in `makeBuilder()`). |
| 6 | TorrentBuilder.setFileNameFilter `(Lio/reactivex/functions/Predicate;)Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:155–160. Call CreateTorrentViewModel.java:198+ (in `makeBuilder()`). |
| 7 | TorrentBuilder.setPieceSize `(I)Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:109–114. Call CreateTorrentViewModel.java:191 (in `makeBuilder()`). |
| 8 | TorrentBuilder.setSeedPath `(Landroid/net/Uri;)Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:94–101. Call CreateTorrentViewModel.java:190 (in `makeBuilder()`). |
| 9 | TorrentBuilder.setTorrentVersion `(Lorg/proninyaroslav/libretorrent/core/TorrentBuilder$TorrentVersion;)Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:162–166 (calls `version.flag()` at :163). Call CreateTorrentViewModel.java:192 (in `makeBuilder()`). |
| 10 | TorrentBuilder.subscribeProgress `()V` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:180–200 (private). Internal call `build()` :175. |
| 11 | TorrentBuilder$1.<init> `(Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;)V` | REACHABLE proposed | SOURCE | Anonymous `Listener` constructed at TorrentBuilder.java:182 (`builder.listener(new org.libtorrent4j.TorrentBuilder.Listener() { ... })`), inside `subscribeProgress()` (row 10). No explicit ctor printed — implicit ctor invoked by that `new` expression. |
| 12 | TorrentBuilder$1.accept `(Ljava/lang/String;)Z` | REACHABLE proposed | INFERRED | Body TorrentBuilder.java:184–192 (fileNameFilter test). Library-callback dispatch: registered at :182, invoked by the libtorrent4j builder during `build()` — dispatch itself unprinted, hence INFERRED. |
| 13 | TorrentBuilder$1.progress `(II)V` | REACHABLE proposed | INFERRED | Body TorrentBuilder.java:195–198 (`progress.onNext(new Progress(pieceIndex, numPieces))` at :197). Library-callback dispatch as row 12, hence INFERRED. |
| 14 | TorrentBuilder$Progress.<init> `(II)V` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:65–69 (static final class :60–69). Construction site TorrentBuilder.java:197 (inside row 13's `progress()`). |
| 15 | TorrentBuilder$TorrentVersion.<clinit> `()V` | REACHABLE proposed | INFERRED | Enum TorrentBuilder.java:72–86, constants :73–75 (HYBRID / V1_ONLY / V2_ONLY). `<clinit>` is JVM-generated; first use triggers JVM enum initialisation (INFERRED). Returned by CreateTorrentViewModel.java:338–348 `getTorrentVersionByIndex()`, called from `makeBuilder()` :192. |
| 16 | TorrentBuilder$TorrentVersion.<init> `(Ljava/lang/String;ILorg/libtorrent4j/swig/create_flags_t;)V` | REACHABLE proposed | INFERRED | Def TorrentBuilder.java:83–85. Invoked implicitly once per constant during row 15's `<clinit>` (INFERRED JVM step). Plan descriptor adds synthetic enum name/ordinal parameters. |
| 17 | TorrentBuilder$TorrentVersion.flag `()Lorg/libtorrent4j/swig/create_flags_t;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:79–81. Call TorrentBuilder.java:163 (`version.flag()` inside `setTorrentVersion`, row 9). |
| 18 | TorrentBuilder$Tracker.<init> `(Ljava/lang/String;I)V` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:53–59 (static class :48–59). Construction site CreateTorrentViewModel.java:275 `new TorrentBuilder.Tracker(url, tier++)` in `getAndValidateTrackers()`, called from `makeBuilder()` :193. |
| 19 | TorrentFileObserver.<init> `(Ljava/lang/String;)V` | REACHABLE proposed | SOURCE | Def TorrentFileObserver.java:35–37 (abstract class :30, `super(pathToDir, mask)` :37). Construction site TorrentEngine.java:1137 (anonymous subclass inside `makeTorrentFileObserver()` :1136), called :1124 in `startWatchDir()` :1116, called :1054 from `handleOnSessionStarted()` when `pref.watchDir()` is true, and :1583/:1590 on watch-dir preference change. |
| 20 | FixedRingBuffer.<init>(int,int) `(II)V` | REACHABLE proposed | SOURCE | Def FixedRingBuffer.java:50–64 (1-arg ctor :45–49 delegates to this one, but that 1-arg ctor is not a batch-19 row). Construction sites Logger.java:68 and :89 (both `new FixedRingBuffer<>(...)`). |
| 21 | FixedRingBuffer.add(Iterable) `(Ljava/lang/Iterable;)V` | OPEN | — | Def FixedRingBuffer.java:80–85 (for-each calls `add(e)`). No printed EXTERNAL caller in the files freshly printed in this pass; internal self-use (this method calling `add(Object)`) does not make it REACHABLE. Stays OPEN pending a saved full-repo grep, not UNREACHABLE. |
| 22 | FixedRingBuffer.add(Object) `(Ljava/lang/Object;)V` | REACHABLE proposed | SOURCE | Def FixedRingBuffer.java:86–99 (calls `tryGrow()` :88). Calls Logger.java:104 (`lazyGetInputBuf().add(entry)`), :154, :253. |
| 23 | FixedRingBuffer.clear `()V` | REACHABLE proposed | SOURCE | Def FixedRingBuffer.java:159–168 (calls `isEmpty()` then `resetHead()` :166). Call Logger.java:249 (`outputBuf.clear()` in `forceFilterBuf`). |
| 24 | FixedRingBuffer.contains `(Ljava/lang/Object;)Z` | OPEN | — | Def FixedRingBuffer.java:179–189. No printed caller in the files freshly printed in this pass. Stays OPEN pending a saved full-repo grep, not UNREACHABLE. |
| 25 | FixedRingBuffer.get `(I)Ljava/lang/Object;` | REACHABLE proposed | SOURCE | Def FixedRingBuffer.java:150–158. Calls Logger.java:152 (`inputBuf.get(i)`), :290, :312, :436 (and :387/:418 for `size()`/index use — the `get(i)` sites are :152, :290, :312, :436). |
| 26 | FixedRingBuffer.getAllocatedSize `()I` | OPEN | — | Def FixedRingBuffer.java:75–78 (`return elements.length`). No printed caller in the files freshly printed in this pass. Stays OPEN pending a saved full-repo grep, not UNREACHABLE. |
| 27 | FixedRingBuffer.indexOf `(Ljava/lang/Object;)I` | OPEN | — | Def FixedRingBuffer.java:112–124. Its only printed caller is `remove()` (FixedRingBuffer.java, inside `remove(Object)`), and `remove()` itself is OPEN (row 31) — a chain through an untriggered method is not a route. Stays OPEN pending a saved full-repo grep, not UNREACHABLE. |
| 28 | FixedRingBuffer.isEmpty `()Z` | REACHABLE proposed | SOURCE | Def FixedRingBuffer.java:169–173. Call Logger.java:145 (`inputBuf.isEmpty()` in `swapBuffers`). Also called internally by `clear()` (row 23), but the Logger call alone suffices. |
| 29 | FixedRingBuffer.isFull `()Z` | OPEN | — | Def FixedRingBuffer.java:174–178. No printed caller in the files freshly printed in this pass. Stays OPEN pending a saved full-repo grep, not UNREACHABLE. |
| 30 | FixedRingBuffer.iterator `()Ljava/util/Iterator;` | REACHABLE proposed | INFERRED | Def FixedRingBuffer.java:209–213 (`return new FixedRingBufferIterator()` :211). The printed trigger is Logger.java:250 `for (LogEntry entry: inputBuf)` — the enhanced-for loop is printed, but the compiler's `iterator()` call itself is INFERRED, hence INFERRED. |
| 31 | FixedRingBuffer.remove `(Ljava/lang/Object;)Ljava/lang/Object;` | OPEN | — | Def FixedRingBuffer.java:100–111 (calls `indexOf()` then `removeAt()`). No printed EXTERNAL caller in the files freshly printed in this pass; internal self-use does not make it REACHABLE, and its internal calls do not make rows 27/32 REACHABLE either. Stays OPEN pending a saved full-repo grep, not UNREACHABLE. |
| 32 | FixedRingBuffer.removeAt `(I)Ljava/lang/Object;` | OPEN | — | Def FixedRingBuffer.java:125–149. Its only printed caller is `remove()` (row 31, OPEN) — not a route. Stays OPEN pending a saved full-repo grep, not UNREACHABLE. |
| 33 | FixedRingBuffer.resetHead `()V` | REACHABLE proposed | SOURCE | Def FixedRingBuffer.java:190–195 (private). Internal call `clear()` :166, and `clear()` is REACHABLE via Logger.java:249 (row 23) — so this row runs when `clear()` runs on a non-empty buffer. |
| 34 | FixedRingBuffer.size `()I` | REACHABLE proposed | SOURCE | Def FixedRingBuffer.java:65–74. Calls Logger.java:150 (`inputBuf.size()`), :287, :309, :387, :418, :453. |
| 35 | FixedRingBuffer.tryGrow `()V` | REACHABLE proposed | SOURCE | Def FixedRingBuffer.java:196–208 (private). Internal call `add(Object)` :88, and `add(Object)` is REACHABLE via Logger (row 22) — so this row runs on every `add(Object)`. |
| 36 | FixedRingBuffer$FixedRingBufferIterator.<init> `(Lorg/proninyaroslav/libretorrent/core/collections/FixedRingBuffer;)V` | REACHABLE proposed | SOURCE | Private class FixedRingBuffer.java:214+, ctor invoked at FixedRingBuffer.java:211 inside `iterator()` (row 30), reached via Logger.java:250 for-loop. |
| 37 | FixedRingBuffer$FixedRingBufferIterator.hasNext `()Z` | REACHABLE proposed | INFERRED | Def FixedRingBuffer.java:219+ (`index < size()`). Reached via the Logger.java:250 for-loop dispatch (INFERRED compiler step), as row 30. |
| 38 | FixedRingBuffer$FixedRingBufferIterator.next `()Ljava/lang/Object;` | REACHABLE proposed | INFERRED | Def FixedRingBuffer.java:225+ (`get(index++)`). Reached via the Logger.java:250 for-loop dispatch (INFERRED compiler step), as row 30. |
| 39 | DecodeException.<init>(Exception) `(Ljava/lang/Exception;)V` | REACHABLE proposed | SOURCE | Def DecodeException.java:35–39 (`super(e)`). Construction sites TorrentMetaInfo.java:69 (byte[] ctor), :79 (TorrentInfo ctor), :92 (FileInputStream ctor), all `throw new DecodeException(e)` in catch (Exception e). Route (prior proposal, construction sites now freshly printed): AddTorrent decode path → `new TorrentMetaInfo(is)` → :92 on failure; also TorrentEngine addTorrentCompletable double-wrap (prior lead, TorrentEngine.java:387 in the proposal's numbering — NOT re-grepped in this pass, so it is not cited as a fresh row-39 route; the three TorrentMetaInfo sites suffice). Do NOT conflate with the String ctor (DecodeException.java:30) or the no-arg ctor (:28) — neither is this row. |
| 40 | FetchLinkException.<init>(Exception) `(Ljava/lang/Exception;)V` | REACHABLE proposed | SOURCE | Def FetchLinkException.java:35–38 (`super(e)`). Construction site Utils.java:474 `throw new FetchLinkException(e)` in `fetchHttpUrl()` :462–475, on `new HttpConnection(url)` failure at :472. Route: AddTorrent decode path → http/https branch → `Utils.fetchHttpUrl` → :474 on connection-construction failure. Do NOT conflate with the String-ctor sites in Utils.java:467, :493, :509, :522 — those are a different overload and are not this row. This row also closes batch 18's HttpConnection chain (Utils.java:472/477/516). |

## Counts — mechanically verified

- Total: 40 rows, sequence 1–40 intact, in plan order.
- REACHABLE proposed: 33 (rows 1–20, 22, 23, 25, 28, 30, 33–40). Breakdown: TorrentBuilder group 18/18 (rows 1–18), TorrentFileObserver 1/1 (row 19), FixedRingBuffer 12/19 (rows 20, 22, 23, 25, 28, 30, 33, 34, 35, 36, 37, 38), exceptions 2/2 (rows 39–40). Of the 33, SOURCE 25 / INFERRED 8 (rows 1, 12, 13, 15, 16, 30, 37, 38) under the per-row convention above.
- UNREACHABLE proposed: 0.
- OPEN: 7 (rows 21, 24, 26, 27, 29, 31, 32 — all FixedRingBuffer, all pending a saved full-repo grep).
- Verified for merge: 0 / 40.

## Changes vs the proposal (Agent 4 update)

Labels: NONE. The counts match the Agent 4 update exactly (33 / 0 / 7, with TorrentFileObserver resolved to REACHABLE SOURCE and the same 7 FixedRingBuffer rows OPEN). What changed is the evidence base: every row group was re-derived from fresh prints in this pass (TorrentBuilder + CreateTorrentViewModel, TorrentFileObserver + TorrentEngine call sites, FixedRingBuffer + Logger call sites, both exception definitions + construction sites) instead of resting on the prior-session local corpus. The one lead NOT carried forward as fresh evidence: the TorrentEngine.java:387 double-wrap site for row 39 is named as a prior lead only, not re-grepped here; it is not needed, because the three TorrentMetaInfo construction sites are freshly printed and suffice.

## Conventions recorded, not decided

- Strict-entry: TorrentBuilder rows anchor at CreateTorrentViewModel.makeBuilder/buildTorrent; the dialog-display step that shows CreateTorrentDialog was not printed in this pass, so under a strict printed-launcher-to-dialog rule all 18 TorrentBuilder rows revert to OPEN. TorrentFileObserver and FixedRingBuffer rows anchor at the session-start trunk (batch 17) and Logger use; no printed launcher step was fetched for them in this pass, so under a strict printed-launcher rule they revert to OPEN on that point alone. Not decided here.
- `confirmed_by`: per-row vs whole-route (above). Not decided here.
- Internal-call rule: rows 33 (resetHead) and 35 (tryGrow) and 36 (Iterator <init>) are REACHABLE on a printed internal call from a REACHABLE method, while rows 27/32 are OPEN because their only caller (row 31, remove) is itself OPEN. The distinction is: an internal call from a REACHABLE method is a route; an internal call from an OPEN method is not. Recorded for the merger to apply consistently.
- OPEN rows stay OPEN: no FixedRingBuffer OPEN row was flipped to UNREACHABLE on the printed-subset absence (Logger + TorrentBuilder files only) — a saved full-repo grep is still owed for all 7.

## Still owed before merge

- Saved full-repo grep for the 7 FixedRingBuffer OPEN rows (21, 24, 26, 27, 29, 31, 32) before any UNREACHABLE verdict on them.
- Printed dialog-display step (CreateTorrentDialog) and launcher step if the strict-entry rule applies.
- The graph-vs-proposal conflict noted in the cross-check audit is NOT resolved here and must be reconciled at merge: the FixedRingBuffer OPEN set in proposals is already UNREACHABLE in `graph_def.py` — "OPEN" here means "not yet re-derived by Muse", not "unlabelled in graph_def". Do not duplicate-merge.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — all not run, never claimed passed.
- No push made; pushes are held until verified and merged to [L] per the user's 23:09 EDT decision.
