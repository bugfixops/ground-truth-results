# LibreTorrent batch 18 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED merge-ready part only. NOT verified for merge. NOT pushed. No edit to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's files.**

**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push, so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1 check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 18 only, 40 methods, no other batch, no other app, no device replay, no Aegis.
- No token, no git clone (a true git clone fails in this VM with no credential device — named missing check, not passed). Work is via the GitHub connector only, one file at a time with ~20 s pauses. No fresh HTTP 429 was hit in this pass. No connector `search_code` 0-result was used as evidence of absence.

## Membership — verified first, not guessed

Exactly the 40 batch-18 rows in `handoff/LIBRETORRENT_BATCH_PLAN.tsv` (local plan copy `~/workspace/agent27-plan.tsv`, plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`), all `TODO_CANDIDATE_REACHABLE`, in plan order:
1–2 `libretorrent.DataBinderMapperImpl$InnerBrLookup` / `$InnerLayoutIdLookup` `<clinit>`; 3–7 `MainApplication`; 8–19 `FeedParser`; 20–22 `HttpConnection`; 23–32 `InputFilterRange` + `$Builder`; 33–36 `RepositoryHelper`; 37–40 `TorrentBuilder`.

## Printed source — freshly fetched in this pass

Saved in `~/workspace/b171819-src/`, branch `work-2026-10-31`, one file at a time with pauses. SHA-256 values are of the saved connector text:

- `org/proninyaroslav/libretorrent/MainApplication.java` — 82 lines, SHA `3f984c43b5d89151e97e3c1eaf6387a7add77e4d64c211a7bf3f614625227b27`. No diff vs prior-session copy `~/workspace/b18-src/MainApplication.java`.
- `org/proninyaroslav/libretorrent/core/FeedParser.java` — 267 lines, SHA `325d0c2c2512e11bdb547630e378e3472c0a71cd8b05261ac913d2a6dee6a38b`. No diff vs `~/workspace/b18-src/FeedParser.java`.
- `org/proninyaroslav/libretorrent/service/FeedFetcherWorker.java` — 270 lines, SHA `4d5bffa59947ddfb9b4370e2eb7fbc2641ac9379a4c40e6dc35a1fdf763b020e`.
- `org/proninyaroslav/libretorrent/core/HttpConnection.java` — 125 lines, SHA `e78bade991bf4b92110893d8888cb8b7916faac927c5e663d3e3958f79bbdae0`. No diff vs `~/workspace/b18-src/HttpConnection.java`.
- `org/proninyaroslav/libretorrent/core/InputFilterRange.java` — 115 lines, SHA `7a3d081a22e9085908b3efd178fff43b010d2e415e47a39b0a390bebb85b8cd3`.
- `org/proninyaroslav/libretorrent/ui/log/LogSettingsFragment.java` — 101 lines, SHA `7cceab74df1851bebd4ce0c973a3bc4a00b7cc8d7a106bffc83f4bac91716439`.
- `org/proninyaroslav/libretorrent/ui/detailtorrent/DetailTorrentFragment.java` — 832 lines, SHA `580c1b0ce3da3ec74b2e1e7b356459326985008bc477f535d2b5876a0947e307`.
- `org/proninyaroslav/libretorrent/core/RepositoryHelper.java` — 76 lines, SHA `827c68c82655eb6b3f4bbc5ddd17bf7c0bcb51fbc207874bdb43db465020a7cc`.
- `org/proninyaroslav/libretorrent/core/TorrentBuilder.java` — 201 lines, SHA `4b02ea5ed479d57a7d9ba4423474da3f436e999302112dc0c48744798a13be8e`.
- `org/proninyaroslav/libretorrent/ui/createtorrent/CreateTorrentViewModel.java` — 406 lines, SHA `7f175b1db8ca5de2bfa0e0baa9b0037b3c54dad348fc7af9fa7d1d31380eb4d9`.
- `org/proninyaroslav/libretorrent/core/utils/Utils.java` — 926 lines, SHA `e2ca2ece8da2673be4c388d733f250d36c061dd231fac71889311e6ea0afd0e9`.

All line numbers in this file were grepped from the saved files themselves.

Prior work used as INPUT / lead list only: `~/workspace/libretorrent-batch18-recheck3.md` (38 REACHABLE proposed / 0 UNREACHABLE / 2 OPEN) and `~/workspace/libretorrent-batch18-recheck2.md` (the 10 InputFilterRange/Builder rows, attach site). Recheck 3's own scope statement is critical: in that session only the InputFilterRange attach sites and plan membership were re-printed; the other 38 rows were CARRIED FORWARD from earlier proposals, not independently re-verified. In THIS pass every row group was re-derived from fresh prints (MainApplication, FeedParser + FeedFetcherWorker, HttpConnection + Utils.fetchHttpUrl, InputFilterRange + both attach sites, RepositoryHelper + its fresh callers, TorrentBuilder + CreateTorrentViewModel) — so no row below rests on a carried-forward verdict, except for the two deliberate OPEN rows (1–2) and the two attach-site-only rows (26–27) whose missing evidence is named below.

## DELIBERATE CHANGE vs the carried-forward re-check 3 totals — read this first

Re-check 3 carried forward 38 REACHABLE / 0 / 2 OPEN. This file proposes **36 REACHABLE / 0 / 4 OPEN**. The difference is exactly rows 1–2:

- Rows 1–2 (`InnerBrLookup.<clinit>`, `InnerLayoutIdLookup.<clinit>`) were carried forward as REACHABLE INFERRED in the prior proposals, on a generated-mapper-load argument. In THIS pass they are judged **OPEN**, on the grounds that no generated mapper is printed anywhere in this pass, no printed mapper-load site was fetched, and batch 17's mapper rows (34–40) are OPEN on the same evidence. **This is a proposal, not an agreed decision, and it must be decided by the merger consistently with batch 17.** If the merger adopts the data-binding-load convention used for other generated Impl rows (e.g. batches 62–64, where Impl creation/rebind were INFERRED REACHABLE on a printed inflate/`setViewModel`), rows 1–2 flip to REACHABLE INFERRED and no other batch-18 row is affected by that flip; the totals then return to 38 / 0 / 2. If the merger requires a printed generated mapper or mapper-load site, rows 1–2 stay OPEN and batch 17 rows 34–40 stay OPEN on the same ground. Either way the two batches must be treated together — do not flip one without the other.

## Per-row judgements

`confirmed_by` here is PER-ROW (SOURCE = a printed direct app-code call site naming the method; INFERRED = unprinted framework/library/JVM dispatch with registration/show/entry printed). Under a WHOLE-ROUTE convention, all REACHABLE rows whose route crosses an unprinted dispatch (WorkManager → FeedFetcherWorker, framework → Application, framework EditText → filter, library → anonymous listener) would read INFERRED; labels are unaffected, only `confirmed_by` would change. That convention is recorded, not decided. OPEN rows carry no `confirmed_by` (shown as `—`).

| # | Method | Label proposed | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | libretorrent.DataBinderMapperImpl$InnerBrLookup.<clinit> `()V` | OPEN | — | See "Deliberate change" above. No generated mapper printed in this pass; no printed mapper-load site fetched; no saved full-repo grep for `DataBinderMapperImpl` / `InnerBrLookup`. Do NOT copy batch 12's `databinding.DataBinderMapperImpl` conclusion — different package/class. Flip condition: merger adopts the generated-mapper-load convention (then REACHABLE INFERRED) or a printed mapper/grep resolves it. |
| 2 | libretorrent.DataBinderMapperImpl$InnerLayoutIdLookup.<clinit> `()V` | OPEN | — | Same as row 1. Flip condition identical. |
| 3 | MainApplication.<clinit> `()V` | REACHABLE proposed | INFERRED | MainApplication.java:38 `TAG = MainApplication.class.getSimpleName()` (non-constant, so class initialisation is JVM work, not a line of app code) and explicit `static { AppCompatDelegate.setCompatVectorFromResourcesEnabled(true); }` at :40–42. Runs on first class load (framework Application instantiation, INFERRED dispatch). |
| 4 | MainApplication.<init> `()V` | REACHABLE proposed | INFERRED | No explicit constructor in the fresh 82-line file — implicit default constructor invoked by the framework when it instantiates the application class (INFERRED). |
| 5 | MainApplication.increaseCursorWindowSize `()V` | REACHABLE proposed | SOURCE | Def :74 (private, CursorWindow reflection). Call `onCreate` :68, reached via framework Application lifecycle (row 7). |
| 6 | MainApplication.lambda$onCreate$0 `(Ljava/lang/Thread;Ljava/lang/Throwable;)V` | REACHABLE proposed | INFERRED | Body at :62–64 `Thread.setDefaultUncaughtExceptionHandler((t, e) -> Log.e(TAG, "Uncaught exception in " + t + ": " + Log.getStackTraceString(e)))`. The lambda body is printed; its dispatch (invocation on an uncaught exception) is unprinted, hence INFERRED. Lambda numbering is source-order, not bytecode-verified; a swap would not change the label. Registration is conditional on `Thread.getDefaultUncaughtExceptionHandler() == null` (:61) — an ordinary condition, not a gate copied from code. |
| 7 | MainApplication.onCreate `()V` | REACHABLE proposed | INFERRED | Def :44–71 (ACRA init, handler registration :62, `increaseCursorWindowSize()` :68, `TorrentNotifier.getInstance(this).makeNotifyChans()` :70). Framework Application lifecycle entry — dispatch itself is INFERRED (no fw_src line printed). |
| 8 | FeedParser.<init> `(Landroid/content/Context;Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;)V` | REACHABLE proposed | SOURCE | Def FeedParser.java:62–82. Construction site FeedFetcherWorker.java:156 `parser = new FeedParser(getApplicationContext(), channel)`. WorkManager dispatch into FeedFetcherWorker is unprinted (whole-route caveat below), but the construction site itself is printed. |
| 9 | FeedParser.findDownloadUrl `(Lcom/ernieyu/feedparser/Item;)Ljava/lang/String;` | REACHABLE proposed | SOURCE | Def :141–161. Internal call `getItems` :102 (only when `downloadUrl == null` after `watchDownloadableLink`), via Worker:165 `parser.getItems()`. |
| 10 | FeedParser.getFirstNotNullLink `(Ljava/util/List;)Ljava/lang/String;` | REACHABLE proposed | SOURCE | Def :118–126. Internal call `getItems` :97. |
| 11 | FeedParser.getItems `()Ljava/util/List;` | REACHABLE proposed | SOURCE | Def :89–116. External call FeedFetcherWorker.java:165 `parser.getItems()`. |
| 12 | FeedParser.getTitle `()Ljava/lang/String;` | REACHABLE proposed | SOURCE | Def :84–87 (`feed.getTitle()`). External call FeedFetcherWorker.java:176 (when the channel name is empty). |
| 13 | FeedParser.isMagnetOrTorrent `(Ljava/lang/String;)Z` | REACHABLE proposed | SOURCE | Def :263–266 (private). Internal calls: `watchDownloadableLink` :134, `watchEnclosure` :176, `watchMediaContent` :203, `watchGuid` :257 — all inside the `getItems` chain above. |
| 14 | FeedParser.watchDownloadableLink `(Ljava/util/List;)Ljava/lang/String;` | REACHABLE proposed | SOURCE | Def :128–139. Internal call `getItems` :98. |
| 15 | FeedParser.watchEnclosure `(Lcom/ernieyu/feedparser/Item;)Ljava/lang/String;` | REACHABLE proposed | SOURCE | Def :168–181. Internal call `findDownloadUrl` :147. |
| 16 | FeedParser.watchGuid `(Lcom/ernieyu/feedparser/Item;)Ljava/lang/String;` | REACHABLE proposed | SOURCE | Def :254–261. Internal call `findDownloadUrl` :159. |
| 17 | FeedParser.watchMediaContent `(Lcom/ernieyu/feedparser/Item;)Ljava/lang/String;` | REACHABLE proposed | SOURCE | Def :188–208. Internal call `findDownloadUrl` :155. |
| 18 | FeedParser.watchMediaHash `(Lcom/ernieyu/feedparser/mediarss/MediaRss;)Ljava/lang/String;` | REACHABLE proposed | SOURCE | Def :215–229. Internal calls `watchMediaContent` :201 and :207. |
| 19 | FeedParser.watchTorrentInfoHash `(Lcom/ernieyu/feedparser/Item;)Ljava/lang/String;` | REACHABLE proposed | SOURCE | Def :236–247. Internal call `findDownloadUrl` :151. |
| 20 | HttpConnection.<init> `(Ljava/lang/String;)V` | REACHABLE proposed | SOURCE | Def HttpConnection.java (class :43, `implements Runnable`, ctor `new URL(url)`, `Utils.getSSLContext()`). Construction site Utils.java:472 `connection = new HttpConnection(url)`, inside `fetchHttpUrl` (:462–475). |
| 21 | HttpConnection.run `()V` | REACHABLE proposed | SOURCE | Def HttpConnection.java (redirect loop, listener callbacks, `conn.disconnect()` in `finally`). Direct call Utils.java:516 `connection.run()` — not a Thread start, so SOURCE, not INFERRED. |
| 22 | HttpConnection.setListener `(Lorg/proninyaroslav/libretorrent/core/HttpConnection$Listener;)V` | REACHABLE proposed | SOURCE | Def HttpConnection.java. Call Utils.java:477 `connection.setListener(new HttpConnection.Listener() { ... })`, before `run()` at :516. Listener method bodies (onConnectionCreated, onResponseHandle, onMovedPermanently, onIOException, onTooManyRedirects) are in Utils.java:478–511 and are not batch-18 rows. |
| 23 | InputFilterRange.<clinit> `()V` | REACHABLE proposed | INFERRED | Class :31. Static initialisers `PORT_FILTER` and `UNSIGNED_INT` (Builder `setMin(0)`/`setMax(65535)` and `setMin(0)`/`setMax(Integer.MAX_VALUE)` respectively, each `.build()`) run at JVM class initialisation on first use (INFERRED, no source line for `<clinit>` itself). First uses printed: LogSettingsFragment:60–63 (Builder) and DetailTorrentFragment:749 (`UNSIGNED_INT` field access). |
| 24 | InputFilterRange.<init> `(Ljava/lang/Integer;Ljava/lang/Integer;)V` | REACHABLE proposed | SOURCE | Def (private) InputFilterRange.java. Call `Builder.build()` :112 `return new InputFilterRange(min, max)`, reached at LogSettingsFragment:63 `.build()`. |
| 25 | InputFilterRange.filter `(Ljava/lang/CharSequence;IILandroid/text/Spanned;II)Ljava/lang/CharSequence;` | REACHABLE proposed | INFERRED | Def InputFilterRange.java (reads the `min`/`max` fields directly, calls `inRange()` at :73). The built filter is registered on the preference's EditText at LogSettingsFragment:70 `setOnBindEditTextListener((editText) -> editText.setFilters(maxFilter))`, and again on two EditTexts at DetailTorrentFragment:751/:760; Android's EditText framework then invokes `filter()` on text input — that framework dispatch is not a printed app line, hence INFERRED. Runs only when the user edits the max-log-size / speed-limit field — an ordinary condition, not a gate copied from code. |
| 26 | InputFilterRange.getMax `()Ljava/lang/Integer;` | OPEN | — | Def :59 (returns the `max` field). `filter()` and `inRange()` read the fields directly and never call `getMax()`. Fresh grep over ALL files printed in this pass found no `InputFilterRange.getMax()` call site outside InputFilterRange.java itself (the only `getMax*` hit elsewhere was the unrelated `Logger.getMaxStoredLogs`). That is a printed-subset check, NOT a saved full-repo grep, so the row stays OPEN, not UNREACHABLE. Resolution: a printed caller (→ REACHABLE) or a saved full-repo grep for `.getMax()` on InputFilterRange instances (→ UNREACHABLE proposal if none). |
| 27 | InputFilterRange.getMin `()Ljava/lang/Integer;` | OPEN | — | Def :53 (returns the `min` field). Same evidence and same resolution as row 26; no `getMin()` caller in the fresh corpus. Stays OPEN, not UNREACHABLE, pending a saved full-repo grep. |
| 28 | InputFilterRange.inRange `(I)Z` | REACHABLE proposed | SOURCE | Def :83 (private, reads fields directly). Internal call `filter()` :73 (SOURCE for the internal call; reaching `filter()` itself is INFERRED as in row 25). |
| 29 | InputFilterRange$Builder.<init> `()V` | REACHABLE proposed | SOURCE | No explicit constructor printed — implicit default constructor invoked by `new InputFilterRange.Builder()` at LogSettingsFragment:60, and by the `PORT_FILTER`/`UNSIGNED_INT` static initialisers. |
| 30 | InputFilterRange$Builder.build `()Lorg/proninyaroslav/libretorrent/core/InputFilterRange;` | REACHABLE proposed | SOURCE | Def :108–113 (throws if `min > max`, otherwise `new InputFilterRange(min, max)` at :112). Call LogSettingsFragment:63 `.build()`. |
| 31 | InputFilterRange$Builder.setMax `(I)Lorg/proninyaroslav/libretorrent/core/InputFilterRange$Builder;` | REACHABLE proposed | SOURCE | Def (returns `this`). Call LogSettingsFragment:62 `.setMax(Integer.MAX_VALUE)`. |
| 32 | InputFilterRange$Builder.setMin `(I)Lorg/proninyaroslav/libretorrent/core/InputFilterRange$Builder;` | REACHABLE proposed | SOURCE | Def (returns `this`). Call LogSettingsFragment:61 `.setMin(1)`. |
| 33 | RepositoryHelper.getFeedRepository `(Landroid/content/Context;)Lorg/proninyaroslav/libretorrent/core/storage/FeedRepository;` | REACHABLE proposed | SOURCE | Def RepositoryHelper.java:52 (`public synchronized static`). Call FeedFetcherWorker.java:77, reached via the worker route (whole-route caveat below). |
| 34 | RepositoryHelper.getSettingsRepository `(Landroid/content/Context;)Lorg/proninyaroslav/libretorrent/core/settings/SettingsRepository;` | REACHABLE proposed | SOURCE | Def RepositoryHelper.java:61. Calls: FeedFetcherWorker.java:78, LogSettingsFragment.java:57 (`pref = RepositoryHelper.getSettingsRepository(context)`), TorrentEngine.java:133, TorrentService.java:108. |
| 35 | RepositoryHelper.getTagRepository `(Landroid/content/Context;)Lorg/proninyaroslav/libretorrent/core/storage/TagRepository;` | REACHABLE proposed | SOURCE | Def RepositoryHelper.java:69. Call TorrentEngine.java:131. |
| 36 | RepositoryHelper.getTorrentRepository `(Landroid/content/Context;)Lorg/proninyaroslav/libretorrent/core/storage/TorrentRepository;` | REACHABLE proposed | SOURCE | Def RepositoryHelper.java:43. Call TorrentEngine.java:130. |
| 37 | TorrentBuilder.<init> `(Landroid/content/Context;)V` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:88–93. Construction site CreateTorrentViewModel.java:189 `new TorrentBuilder(getApplication())` in `makeBuilder()`. |
| 38 | TorrentBuilder.addTrackers `(Ljava/util/List;)Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:116–126. Call CreateTorrentViewModel.java:193 `.addTrackers(getAndValidateTrackers())` in `makeBuilder()`. |
| 39 | TorrentBuilder.addUrlSeeds `(Ljava/util/List;)Lorg/proninyaroslav/libretorrent/core/TorrentBuilder;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:127–133. Call CreateTorrentViewModel.java:194 `.addUrlSeeds(getAndValidateWebSeeds())` in `makeBuilder()`. |
| 40 | TorrentBuilder.build `()Lio/reactivex/Single;` | REACHABLE proposed | SOURCE | Def TorrentBuilder.java:173–178 (`subscribeProgress()` :175, `Single.fromCallable(() -> builder.generate().entry().bencode())` :177). Call CreateTorrentViewModel.java:171–173 `builder.build()` (subscribed). See batch 19 for the lambda$build$0, observeProgress, subscribeProgress, and setter rows of the same class. |

## Attach sites — printed fresh in this pass (InputFilterRange rows)

- Site A: LogSettingsFragment.java:59–70. `InputFilter[] maxFilter = new InputFilter[] { new InputFilterRange.Builder().setMin(1).setMax(Integer.MAX_VALUE).build()}` at :59–64 (Builder :60, `setMin(1)` :61, `setMax(Integer.MAX_VALUE)` :62, `build()` :63), `maxLogSize.setOnBindEditTextListener((editText) -> editText.setFilters(maxFilter))` at :70, import `InputFilterRange` at :32. The fragment-attach step (LogSettingsActivity → LogSettingsFragment via layout) was NOT printed in this pass; LogSettingsActivity.onCreate only sets the content view and toolbar (prior re-check 2 finding, not re-fetched here). See strict-entry below.
- Site B: DetailTorrentFragment.java:749–760. `InputFilter[] filter = new InputFilter[]{ InputFilterRange.UNSIGNED_INT}` at :749, `upload.setFilters(filter)` :751, `download.setFilters(filter)` :760, import `InputFilterRange` at :65. This site supports `<clinit>` / `filter` reachability in general but calls neither `getMin()` nor `getMax()`, so it does not change rows 26–27.
- Neither site calls `getMin()` or `getMax()`; `filter()` and `inRange()` read the fields directly.

## Counts — mechanically verified

- Total: 40 rows, sequence 1–40 intact, in plan order.
- REACHABLE proposed: 36 (rows 3–25, 28–40). Of these, SOURCE 30 / INFERRED 6 (rows 3, 4, 6, 7, 23, 25) under the per-row convention above.
- UNREACHABLE proposed: 0.
- OPEN: 4 (rows 1, 2, 26, 27).
- Verified for merge: 0 / 40.

## Changes vs the carried-forward re-check 3 totals

- Rows 1–2: REACHABLE INFERRED (carried forward) → OPEN (this pass) — see "Deliberate change" above; a proposal, not a decision.
- Rows 26–27: unchanged (OPEN in re-check 2, re-check 3, and here).
- All other rows: labels unchanged from the carried-forward totals, but now freshly re-derived (MainApplication, FeedParser, HttpConnection, RepositoryHelper, TorrentBuilder groups were NOT re-printed in re-check 3 and are freshly printed here; HttpConnection rows 20–22 are now closed by the freshly printed `Utils.fetchHttpUrl` chain — Utils.java:472/477/516 — not by a lead).
- The graph-vs-proposal conflict noted in the cross-check audit is NOT resolved here and must be reconciled at merge: `graph_def.py` lines 3096–3100 list `InputFilterRange.getMin/getMax` as UNREACHABLE, while these proposals keep them OPEN (no saved full-repo grep yet). Do not merge either verdict until the grep is saved.

## Conventions recorded, not decided

- Strict-entry: no printed launcher step was fetched in this pass for MainApplication (the application class itself — the framework instantiates it, so the caveat is in a different sense from activity/fragment rows), for FeedFetcherWorker (WorkManager dispatch unprinted), for LogSettingsFragment (fragment-attach step unprinted), or for CreateTorrentViewModel's dialog (dialog-display step unprinted). Under a strict printed-launcher rule the REACHABLE rows in each group revert to OPEN on that point alone. Not decided here.
- `confirmed_by`: per-row vs whole-route (above). Not decided here.
- Generated-mapper-load convention: rows 1–2 + batch 17 rows 34–40 must be decided together (above). Not decided here.
- InputFilterRange getters: rows 26–27 stay OPEN pending a saved full-repo grep; they are not flipped to UNREACHABLE on the printed-subset grep above.

## Still owed before merge

- Merger decision on the generated-mapper-load convention (rows 1–2 + batch 17 rows 34–40).
- Saved full-repo grep for rows 26–27 (`.getMin()` / `.getMax()` on InputFilterRange instances) before any UNREACHABLE verdict on them.
- Printed launcher / WorkManager / fragment-attach steps if the strict-entry rule applies.
- Main-agent spot-check (1 in 5), `py_compile`, build, Mac build/C1 — all not run, never claimed passed.
- No push made; pushes are held until verified and merged to [L] per the user's 23:09 EDT decision.
