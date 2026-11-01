# LibreTorrent batch 51 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler or full-repo grep was run or is claimed.
No connector `search_code` result was used as evidence for any row, and no `search_code` 0-result
was used as evidence of absence. No token was used and no git clone was attempted: a true git clone
fails in this VM (no credential device for https://github.com) — that check is named missing,
never passed. Work is via the GitHub connector only, branch `work-2026-10-31` only (never `main`
or `result`).

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only.
- Scope: batch 51 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Prior work (the batch-51 WP1 proposal) was used as an INPUT / lead list only; every row below
  was re-judged against source freshly fetched in this pass (see "Printed source used"), and the
  changes vs that proposal are listed under "Changes vs the prior proposal". No proposal verdict
  was copied without a check.
- Labels are REACHABLE / UNREACHABLE / OPEN only. No UNREACHABLE row is claimed in this batch
  (no saved full-repo grep was run, so absence in printed files is never treated as absence in
  the app). `confirmed_by` is SOURCE or INFERRED only (never DYN, FW-MEMORY, or UNVERIFIED);
  OPEN rows carry "-" for `confirmed_by`, as in sibling merge-ready files.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 51 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`; that SHA is the git blob SHA of the file, whose
raw sha1 is `afedc8af26f…` — see the batch 14-16 merge-ready note resolving the raw-vs-blob
hash question), all `TODO_CANDIDATE_REACHABLE`, in plan order. The tables below are generated
from that TSV, so method names, JVM descriptors and plan order cannot drift by hand-typing.

## Printed source used

Base path (omitted in citations):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`

Fresh connector fetches in THIS pass, branch `work-2026-10-31`, one file at a time with
~25 s pauses, saved in `~/workspace/b505152-src/` (no fresh HTTP 429 hit in this pass;
24 fetches, all succeeded):
- `core/storage/dao/FeedDao.java` — full, 111 lines, SHA `9731e3915ade0044238914f2987f17d942005256` (byte-identical to the prior print: same SHA as the batch-51 proposal).
- `core/storage/FeedRepositoryImpl.java` — full, 227 lines, SHA `20f94942d1147a21f97775ce882ad526068cd8` (same SHA as the batch-51 proposal).
- `core/storage/dao/TagInfoDao.java` — full, 65 lines, SHA `bb5bde7d4ee14d3e101be512ad7b164e1a5e27a2` (same SHA as the batch-52 proposal).
- `core/storage/TagRepositoryImpl.java` — full, 78 lines, SHA `434de891292f346091a6955e4d64fe83059450a7` (same SHA as the batch-52 proposal).
- `core/storage/dao/TorrentDao.java` — full, 78 lines, SHA `1a079658ca7f8fc36d609e4e61c21a8f08e7def8` (same SHA as the batch-52 proposal and the batch-53 fresh fetch; batch 53 counted 77 lines — a trailing-newline counting difference, not a content difference).
- `core/storage/TorrentRepositoryImpl.java` — full, 173 lines, SHA `0f01eff0a7613bfa2ecdb3052e7914ba9f00bd54` (same SHA as the batch-50/52 proposals; proposals counted 172 lines — trailing-newline counting difference only).
- `core/storage/AppDatabase.java` — full, 87 lines, SHA `5836e2a40fd320b5196669e7ea6b9afabba961c8` (same SHA as the batch-50 proposal).
- `core/RepositoryHelper.java` — full, 77 lines, SHA `9b68b203ecf60a00bd27ed62afd58e9534cdbd4e`.
- `core/storage/converter/UriConverter.java` — full, 41 lines, SHA `9ec30aed333d988d684dfa580a49865c45b255a1` (same SHA as the batch-50 proposal; proposal counted 40 lines — trailing-newline counting difference only).
- `core/storage/dao/FastResumeDao.java` — full, 19 lines, SHA `3031a9e5dbb331492184048329913b2708f1afcc`.
- `core/model/data/entity/Torrent.java` — full, 202 lines, SHA `9dbe96bf15d2398823497b2a04bbbd7d012de9c8` (same SHA as the batch-29-31 fresh fetch).
- `ui/addfeed/AddFeedViewModel.java` — full, 221 lines, SHA `197167f05c997de2704028b6442bc4f83fca565` (same SHA as the batch-29-31 fresh fetch).
- `ui/feeds/FeedViewModel.java` — full, 173 lines, SHA `c72f614afd02a3df5661d72532693d7444c8a388`.
- `ui/feeditems/FeedItemsViewModel.java` — full, 156 lines, SHA `d034625f971d3c07754cb693aff50f36a2663aef`.
- `service/FeedFetcherWorker.java` — full, 271 lines, SHA `fedbafe8adcb768bacc3d2ef5b37b58ea2fd9ab6`.
- `service/FeedDownloaderWorker.java` — full, 216 lines, SHA `f45dda6f9626f405b3f799a6408fa35f3e73075f` (same SHA prefix as the batch-22 fresh fetch).
- `ui/detailtorrent/DetailTorrentViewModel.java` — full, 611 lines, SHA `6e4ef82f455957298bfb6bf4513c4a35c799a1a6` (same SHA as the batch-89-90 fresh fetch).
- `ui/main/MainViewModel.java` — full, 190 lines, SHA `73938fbb508da1f1fa3459ed5e1d764523f8191b`.
- `ui/addtag/AddTagViewModel.java` — full, 79 lines, SHA `c134a04c1360e216d93eeeab346948bbf32a23c0`.
- `ui/tag/SelectTagViewModel.java` — full, 66 lines, SHA `a48d0983611d0b6baae27cf84dc9d164713a3540`.
- `core/model/TorrentInfoProvider.java` — full, 499 lines, SHA `188fbd964517efc6bb13b2e042941cc451d7e698` (same SHA as the batch-29-31 fresh fetch, which counted 498 lines — trailing-newline counting difference only).
- `core/model/session/TorrentSessionImpl.java` — full, 1721 lines, SHA `aef9618cb29cae4ade30d51d968f2d3b0f5182dd` (same SHA as the batch-29-31 fresh fetch, which counted 1720 lines — trailing-newline counting difference only).
- `core/model/session/TorrentDownloadImpl.java` — full, 1712 lines, SHA `30024b5d27ff357262557d35bac99281b54ae8f8` (same SHA as the batch-29-31 fresh fetch, which counted 1711 lines — trailing-newline counting difference only).
- `core/model/TorrentEngine.java` — full, 1659 lines, SHA `17d06efe1076675af0c41a6c929e8d2f04eabb68` (same SHA as the batch-71 fresh fetch, which counted 1658 lines — trailing-newline counting difference only).

No other file is cited. In particular, no row below rests on a local-copy line number: every
definition line and every repository-method caller line cited was freshly fetched in this pass.
The one exception class is the generated Room code itself (`*_Impl`, `*_Impl$N`): it is not in
`final_java_only` (generated at build time), so no definition line is cited for any `_Impl` row;
each such verdict rests on the printed interface/abstract method + the printed repository
delegation + Room's generated-dispatch rule, and is INFERRED, never SOURCE.

## Route anchors (printed, fresh)

1. **Repository construction.** `RepositoryHelper.getTorrentRepository` (:43-47) constructs
   `new TorrentRepositoryImpl(appContext, AppDatabase.getInstance(appContext))`;
   `getFeedRepository` (:52-56) constructs `new FeedRepositoryImpl(...)`;
   `getTagRepository` (:69-72) constructs `new TagRepositoryImpl(...)`.
   Printed callers, all fresh: `TorrentEngine.java:130-131`, `DetailTorrentViewModel.java:109,114`,
   `MainViewModel.java:74`, `AddTagViewModel.java:42`, `FeedViewModel.java:64`,
   `FeedItemsViewModel.java:59`, `AddFeedViewModel.java:63`, `SelectTagViewModel.java:44`,
   `FeedFetcherWorker.java:77`, `FeedDownloaderWorker.java:79`.
2. **Database / DAO access.** `AppDatabase.java` declares the abstract DAO accessors
   `torrentDao()` (:61), `fastResumeDao()` (:63), `feedDao()` (:65), `tagInfoDao()` (:67),
   registers `UriConverter` via `@TypeConverters({UriConverter.class})` (:53), and builds the
   database via `Room.databaseBuilder(...)` in `buildDatabase` (:81-85) called from
   `getInstance` (:69-74). At runtime Room returns the generated `*_Impl` for each accessor;
   that step is library-generated, hence every `*_Impl` row below is INFERRED, never SOURCE.
3. **Room-generated classes are not in the upload.** `FastResumeDao_Impl.java`,
   `FeedDao_Impl.java`, `TagInfoDao_Impl.java` and `TorrentDao_Impl.java` do not exist under
   `final_java_only/` (generated at build time from the DAO interfaces / abstract class).
   If the merger requires a printed generated file, the `_Impl` rows revert to OPEN — they
   are not SOURCE, and this file does not claim otherwise.
4. **Strict-entry caveat.** Routes anchor at ViewModels / Workers / Engine / Session /
   RepositoryHelper, not at a printed launcher entry. Under a strict launcher-entry rule all
   REACHABLE rows below revert to OPEN; the proposed counts follow the sibling-batch
   (e.g. batches 22/23, 48-50) anchor convention, not the strict rule.

## Undecided conventions recorded per row, NOT decided

- **Strict-entry:** see anchor 4 above. No launcher step was freshly printed in this pass.
- **`confirmed_by` (per-row, not whole-route):** SOURCE = a printed direct app-code call site
  naming the method (for hand-written repository methods: the printed repository body plus a
  printed ViewModel/Worker/Engine/Session caller); INFERRED = reached only through unprinted
  framework/library/generated dispatch (Room dispatch to `_Impl`, Rx subscription, JVM class
  initialisation) where the interface call / registration / first use IS printed. Under a
  whole-route INFERRED convention, SOURCE rows whose route crosses unprinted dispatch would
  read INFERRED; labels are unaffected, only `confirmed_by` would change.
- **Room `$N` mapping (convention (vii)):** for `FeedDao_Impl$N` (batch 51) and
  `TagInfoDao_Impl$N` (batch 52) this file uses the SET argument, not the individual
  assignment: every generated helper in each set is used because every underlying DAO
  operation is called on a freshly printed route (see the per-row set notes), so a swap
  within a set changes no label. The proposal lead orders (declaration order / canonical
  Room order) are recorded as leads only. The one exception is pinned, not set-assigned:
  `FeedDao_Impl$8.call` returns `FeedChannel`, and `getFeedByIdSingle` is the only Rx method
  returning a single FeedChannel. If the merger adopts the batch-53 strict rule — a `$N`
  row needs printed generated source or bytecode identifying that `$N` — then the strict-`$N`
  revert lists below apply, and the merger must reconcile that rule project-wide with
  batches 51-52 (set argument) vs batch 53 (OPEN on the same ground).
- **Room Callable `finalize()` (convention (vi)):** all `finalize()` rows stay OPEN (GC-only
  reasoning in each row). A project rule is still needed; they are NOT `no_trigger_in_app`.
- **`getRequiredConverters` treatment:** rows 50/27, 51/6, 52/11 stay OPEN (no printed call,
  Room dispatch for them not printed), following the batch-48/53 precedent. The batch 50-52
  proposals marked them REACHABLE INFERRED on a database-build assumption; if the merger
  adopts that assumption instead, those three rows flip together to REACHABLE INFERRED.
- **`<clinit>` on first-use evidence (convention (ix)):** batch-50 row 6 rests on a printed
  first use (construction at RepositoryHelper.java:46-47) plus a non-constant
  `TAG = getSimpleName()` (TorrentRepositoryImpl.java:41). Whether that evidence alone
  suffices project-wide is undecided; the row is INFERRED, not SOURCE.
- **Migration gate (convention (iii)):** does not arise in these batches (no migration rows).
- **Binding `getViewModel` (convention (v)), binding-variant config (iv), FragmentCallback
  (viii):** no such rows occur in batches 50-52.

## Changes vs the prior proposals (deliberate, flagged — not silent)

- Batch 50: 40/0/0 → **39/0/1**. Row 27 `FastResumeDao_Impl.getRequiredConverters`
  REACHABLE INFERRED → OPEN (no printed call; batch-48/53 precedent; flip condition in row).
  All other 39 verdicts unchanged, but their evidence base is upgraded: every repository
  delegation AND every repository-method caller line is freshly fetched in this pass,
  whereas the proposal relied on shared-local-corpus caller prints for the ViewModel /
  Worker / Engine / Session lines.
- Batch 51: 37/0/3 → **36/0/4**. Row 6 `FeedDao_Impl.getRequiredConverters`
  REACHABLE INFERRED → OPEN (same reason). All other 39 verdicts unchanged; same evidence
  upgrade (the proposal's repository delegations were fresh, but its repository-method
  callers were batch-49-printed — every one of those caller lines is freshly fetched here
  and matches the proposal's numbers exactly).
- Batch 52: 35/0/5 → **34/0/6**. Row 11 `TagInfoDao_Impl.getRequiredConverters`
  REACHABLE INFERRED → OPEN (same reason). All other 39 verdicts unchanged; same evidence
  upgrade (proposal's repository delegations were fresh, its callers batch-49/50-printed —
  every caller line is freshly fetched here and matches exactly).
- Strict-`$N` revert lists (if the merger adopts the batch-53 rule, these REACHABLE rows
  revert to OPEN; the counts under that rule are in parentheses):
  - Batch 50: rows 28, 29, 30 (FastResumeDao_Impl$1 trio) → counts become 36/0/4.
  - Batch 51: rows 13, 14, 15, 16, 17, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33,
    34, 35, 36, 37, 38, 39, 40 (25 rows) → counts become 11/0/29.
  - Batch 52: rows 1, 3, 4, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29, 31, 32
    (18 rows) → counts become 16/0/24.
  - Combined under the strict rule: 63/0/57 out of 120 (vs 109/0/11 under the set argument).

## Per-row verdicts

| # | Method | Label | confirmed_by | Printed route / citation |
|---|---|---|---|---|

| 1 | `FeedDao_Impl.getFeedById` `(J)Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;` | REACHABLE | INFERRED | Generated implementation of `FeedDao.getFeedById` (FeedDao.java:67, fresh). Via FeedRepositoryImpl.java:116, fresh; callers AddFeedViewModel.java:131 and FeedFetcherWorker.java:150, fresh. Room dispatch unprinted, hence INFERRED. |
| 2 | `FeedDao_Impl.getFeedByIdSingle` `(J)Lio/reactivex/Single;` | REACHABLE | INFERRED | Generated implementation of `FeedDao.getFeedByIdSingle` (FeedDao.java:70, fresh). Via FeedRepositoryImpl.java:122, fresh; caller AddFeedViewModel.java:151, fresh. Its Callable is `$8` (batch 52 rows 1-2). Room dispatch unprinted, hence INFERRED. |
| 3 | `FeedDao_Impl.getItemsByFeedIdSingle` `(J)Lio/reactivex/Single;` | REACHABLE | INFERRED | Generated implementation of `FeedDao.getItemsByFeedIdSingle` (FeedDao.java:100, fresh). Via FeedRepositoryImpl.java:206, fresh; caller FeedItemsViewModel.java:89, fresh. Its Callable is one of `$10-$12` (set note below). Room dispatch unprinted, hence INFERRED. |
| 4 | `FeedDao_Impl.getItemsById` `([Ljava/lang/String;)Ljava/util/List;` | REACHABLE | INFERRED | Generated implementation of `FeedDao.getItemsById` (FeedDao.java:109, fresh). Via FeedRepositoryImpl.java:224, fresh; caller FeedDownloaderWorker.java:100, fresh. Room dispatch unprinted, hence INFERRED. |
| 5 | `FeedDao_Impl.getItemsIdByFeedId` `(J)Ljava/util/List;` | REACHABLE | INFERRED | Generated implementation of `FeedDao.getItemsIdByFeedId` (FeedDao.java:103, fresh). Via FeedRepositoryImpl.java:212, fresh; caller FeedFetcherWorker.java:191, fresh. Room dispatch unprinted, hence INFERRED. |
| 6 | `FeedDao_Impl.getRequiredConverters` `()Ljava/util/List;` | OPEN | - | Generated-only method; no printed app call and no printed Room call site for it. Same as batch-50 row 27: stays OPEN (batch-48/53 precedent), not INFERRED REACHABLE. Flip condition: a printed Room dispatch showing Room calls DAO `getRequiredConverters` at database build flips this to REACHABLE INFERRED, together with rows 50/27 and 52/11. Needs printed Room dispatch or a saved full-repo grep; never flipped on absence. |
| 7 | `FeedDao_Impl.markAsRead` `(Ljava/lang/String;)V` | REACHABLE | INFERRED | Generated implementation of `FeedDao.markAsRead` (FeedDao.java:88; query `UPDATE FeedItem SET read = 1 WHERE id = :itemId`, FeedDao.java:43, fresh). Via FeedRepositoryImpl.java:182, fresh; callers FeedFetcherWorker.java:221 and FeedItemsViewModel.java:124, fresh. Room dispatch unprinted, hence INFERRED. |
| 8 | `FeedDao_Impl.markAsReadByFeedId` `(Ljava/util/List;)V` | REACHABLE | INFERRED | Generated implementation of `FeedDao.markAsReadByFeedId` (FeedDao.java:94; query `UPDATE FeedItem SET read = 1 WHERE feedId IN (:feedId)`, FeedDao.java:45, fresh). Via FeedRepositoryImpl.java:194, fresh; callers FeedItemsViewModel.java:118 and FeedViewModel.java:149, fresh. No `$` adapter row exists for it: its SQL depends on the list size, so Room compiles it inline in the method instead of a SharedSQLiteStatement field. Room dispatch unprinted, hence INFERRED. |
| 9 | `FeedDao_Impl.markAsUnread` `(Ljava/lang/String;)V` | REACHABLE | INFERRED | Generated implementation of `FeedDao.markAsUnread` (FeedDao.java:91; query `UPDATE FeedItem SET read = 0 WHERE id = :itemId`, FeedDao.java:44, fresh). Via FeedRepositoryImpl.java:188, fresh; caller FeedItemsViewModel.java:131, fresh. Room dispatch unprinted, hence INFERRED. |
| 10 | `FeedDao_Impl.observeAllFeeds` `()Lio/reactivex/Flowable;` | REACHABLE | INFERRED | Generated implementation of `FeedDao.observeAllFeeds` (FeedDao.java:73, fresh). Via FeedRepositoryImpl.java:128, fresh; caller FeedViewModel.java:82, fresh. Its Callable is one of `$9-$12` (set note below; proposal lead order puts it at `$9`, batch 52 rows 3-5). Room dispatch unprinted, hence INFERRED. |
| 11 | `FeedDao_Impl.observeItemsByFeedId` `(J)Lio/reactivex/Flowable;` | REACHABLE | INFERRED | Generated implementation of `FeedDao.observeItemsByFeedId` (FeedDao.java:97, fresh). Via FeedRepositoryImpl.java:200, fresh; caller FeedItemsViewModel.java:84, fresh. Its Callable is one of `$10-$12` (set note below). Room dispatch unprinted, hence INFERRED. |
| 12 | `FeedDao_Impl.updateFeed` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;)I` | REACHABLE | INFERRED | Generated implementation of `FeedDao.updateFeed` (FeedDao.java:58, `@Update`, fresh). Via FeedRepositoryImpl.java:98, fresh; callers AddFeedViewModel.java:190 and FeedFetcherWorker.java:160,181, fresh. Room dispatch unprinted, hence INFERRED. |
| 13 | `FeedDao_Impl$1.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Insertion adapter for FeedChannel, constructed in the `_Impl` constructor. Bind descriptor pins the entity: `FeedDao` inserts FeedChannel only via `addFeed`/`addFeeds` (FeedDao.java:52,55, fresh). Runs on every addFeed/addFeeds (FeedRepositoryImpl.java:86,92, fresh; callers AddFeedViewModel.java:189, FeedViewModel.java:144, fresh). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 14 | `FeedDao_Impl$1.bind` `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;)V` | REACHABLE | INFERRED | Binds a FeedChannel on every addFeed/addFeeds insert (same route as row 13). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 15 | `FeedDao_Impl$1.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Returns the FeedChannel INSERT SQL on every addFeed/addFeeds insert (same route as row 13). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 16 | `FeedDao_Impl$10.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | REACHABLE | INFERRED | Callable for a List-returning Rx query. Set note (applies to `$10-$12` rows 16-24 and batch-52 `$9` rows 3-4): the four List-returning Rx methods are `getAllFeedsSingle` (FeedDao.java:79), `observeItemsByFeedId` (:97), `getItemsByFeedIdSingle` (:100) and `observeAllFeeds` (:73) — all called via the repository with fresh callers (FeedViewModel.java:77,82; FeedItemsViewModel.java:84,89) — so every callable in the set is used, whichever `$N` maps to which method; the individual `$10`/`$11`/`$12` assignment (proposal lead order: `$10` = getAllFeedsSingle, `$11` = observeItemsByFeedId, `$12` = getItemsByFeedIdSingle) is NOT adopted as a label basis. `<init>` runs when the DAO method is called. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 17 | `FeedDao_Impl$10.call` `()Ljava/util/List;` | REACHABLE | INFERRED | Runs when the Single/Flowable from row 16's method is subscribed; the Rx subscription step is unprinted library dispatch, hence INFERRED. No printed generated def. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 18 | `FeedDao_Impl$10.finalize` `()V` | OPEN | - | GC-only release of the RoomSQLiteQuery (Room Callable `finalize()` convention (vi), undecided project-wide): only the JVM garbage collector can invoke `finalize()` on a created Callable, nondeterministically, after the Callable is collected. That is not an app/framework route in the trigger-graph sense, but the Callable IS created (row 16), so this is NOT `no_trigger_in_app` either. Needs a project rule on `finalize()` before any label; never flipped to UNREACHABLE without a saved full-repo grep. |
| 19 | `FeedDao_Impl$11.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | REACHABLE | INFERRED | Callable for a List-returning Rx query (set note at row 16; proposal lead order: observeItemsByFeedId). Created when FeedRepositoryImpl.observeItemsByFeedId runs (FeedRepositoryImpl.java:200, fresh; caller FeedItemsViewModel.java:84, fresh) under the lead order, and under any set assignment its method is called. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 20 | `FeedDao_Impl$11.call` `()Ljava/util/List;` | REACHABLE | INFERRED | Runs when the Flowable from row 19's method is subscribed (Rx step INFERRED). No printed generated def. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 21 | `FeedDao_Impl$11.finalize` `()V` | OPEN | - | As row 18 (GC-only `finalize()`; Callable created at row 19). Needs a project rule on `finalize()`; NOT `no_trigger_in_app`. |
| 22 | `FeedDao_Impl$12.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | REACHABLE | INFERRED | Callable for a List-returning Rx query (set note at row 16; proposal lead order: getItemsByFeedIdSingle). Created when FeedRepositoryImpl.getItemsByFeedIdSingle runs (FeedRepositoryImpl.java:206, fresh; caller FeedItemsViewModel.java:89, fresh) under the lead order, and under any set assignment its method is called. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 23 | `FeedDao_Impl$12.call` `()Ljava/util/List;` | REACHABLE | INFERRED | Runs when the Single from row 22's method is subscribed (Rx step INFERRED). No printed generated def. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 24 | `FeedDao_Impl$12.finalize` `()V` | OPEN | - | As row 18 (GC-only `finalize()`; Callable created at row 22). Needs a project rule on `finalize()`; NOT `no_trigger_in_app`. |
| 25 | `FeedDao_Impl$2.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Insertion adapter for FeedItem, constructed in the `_Impl` constructor. Bind descriptor pins the entity: `FeedDao` inserts FeedItem only via `addItems` (FeedDao.java:82, fresh). Runs on every addItems (FeedRepositoryImpl.java:170, fresh; caller FeedFetcherWorker.java:172, fresh). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 26 | `FeedDao_Impl$2.bind` `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedItem;)V` | REACHABLE | INFERRED | Binds a FeedItem on every addItems insert (same route as row 25). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 27 | `FeedDao_Impl$2.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Returns the FeedItem INSERT SQL on every addItems insert (same route as row 25). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 28 | `FeedDao_Impl$3.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Deletion-or-update adapter for FeedChannel (bind descriptor cannot distinguish the two: both bind FeedChannel). Both operations are called via the repository — delete (FeedRepositoryImpl.java:104,110, fresh; callers AddFeedViewModel.java:133, FeedViewModel.java:87, fresh) and update (FeedRepositoryImpl.java:98, fresh; callers AddFeedViewModel.java:190, FeedFetcherWorker.java:160,181, fresh) — so `$3` runs whichever adapter it is; a `$3`/`$4` swap (declaration-order vs canonical-order generation) changes NO label. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 29 | `FeedDao_Impl$3.bind` `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;)V` | REACHABLE | INFERRED | Binds a FeedChannel on every deleteFeed/deleteFeeds delete (row 28 route) or on every updateFeed update (if `$3` is the update adapter) — either way it runs, per row 28. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 30 | `FeedDao_Impl$3.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Returns the FeedChannel DELETE SQL (row 28 route) or UPDATE SQL (if `$3` is the update adapter) on every delete/update — either way it runs, per row 28. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 31 | `FeedDao_Impl$4.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Update-or-deletion adapter for FeedChannel (mirror of row 28: whichever adapter `$3` is, `$4` is the other, and both operations are called). Runs on updateFeed and/or deleteFeed/deleteFeeds (routes at row 28). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 32 | `FeedDao_Impl$4.bind` `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;)V` | REACHABLE | INFERRED | Binds a FeedChannel on every updateFeed update (row 31 route) or on every delete (if `$4` is the deletion adapter) — either way it runs, per row 31. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 33 | `FeedDao_Impl$4.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Returns the FeedChannel UPDATE SQL (row 31 route) or DELETE SQL (if `$4` is the deletion adapter) on every update/delete — either way it runs, per row 31. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 34 | `FeedDao_Impl$5.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | SharedSQLiteStatement field, constructed in the `_Impl` constructor. CreateQuery-only shape. Set note (applies to `$5-$7` rows 34-39): the three `@Query` statements that are not Rx and not plain selects are `deleteItemsOlderThan` (FeedDao.java:85), `markAsRead` (:88) and `markAsUnread` (:91) — all called via the repository with fresh callers (FeedRepositoryImpl.java:176,182,188; FeedFetcherWorker.java:209,221; FeedItemsViewModel.java:124,131) — so every statement field in the set is used, whichever `$N` maps to which statement; the individual assignment (proposal lead order: `$5` = deleteItemsOlderThan, `$6` = markAsRead, `$7` = markAsUnread) is NOT adopted as a label basis. `createQuery()` runs when the statement is acquired. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 35 | `FeedDao_Impl$5.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Returns the statement SQL (one of the three queries at row 34) when that statement is acquired. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 36 | `FeedDao_Impl$6.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | SharedSQLiteStatement field (set note at row 34; proposal lead order: markAsRead). Constructed in the `_Impl` constructor; runs on its statement's method (all three called, per row 34). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 37 | `FeedDao_Impl$6.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Returns the statement SQL (one of the three queries at row 34) when that statement is acquired. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 38 | `FeedDao_Impl$7.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | SharedSQLiteStatement field (set note at row 34; proposal lead order: markAsUnread). Constructed in the `_Impl` constructor; runs on its statement's method (all three called, per row 34). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 39 | `FeedDao_Impl$7.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Returns the statement SQL (one of the three queries at row 34) when that statement is acquired. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 40 | `FeedDao_Impl$8.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | REACHABLE | INFERRED | getFeedByIdSingle Callable, created when FeedRepositoryImpl.getFeedByIdSingle runs (FeedRepositoryImpl.java:122, fresh; caller AddFeedViewModel.java:151, fresh). Its `call()` is batch-52 row 1 and its `finalize()` is batch-52 row 2. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |

## Counts (mechanically verified — see generator)

- Judged: **40 / 40**. REACHABLE proposed: **36**. UNREACHABLE proposed: **0**.
  OPEN: **4**. confirmed_by: SOURCE 0 / INFERRED 36 (OPEN rows carry "-").
- Verified for merge: **0**.
- Not claimed: build, sampler, grep, C1, `py_compile`, main-agent spot-check (1 in 5).
  Build and C1 run on the user's Mac after a push; both are marked "not run" here.
- Still owed before merge: (1) a saved full-repo grep for every OPEN row before any
  OPEN → UNREACHABLE flip (none is flipped on absence here); (2) a project decision on
  the Room `$N` mapping (set argument vs batch-53 strict rule) and on Room Callable
  `finalize()`; (3) a project decision on the `getRequiredConverters` treatment
  (rows 50/27, 51/6, 52/11 judged together); (4) a printed launcher step if the
  strict-entry rule is applied; (5) main-agent spot-check (1 in 5), `py_compile`,
  build, and Mac build/C1.
