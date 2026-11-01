**REVISION 2026-11-01 (Stream A Phase 1c, APPLY DECISIONS — UNVERIFIED).** Applied DECISIONS.md mechanically and only: row 6 (D3c), row 18 (D3b), row 21 (D3b), row 24 (D3b). Finalize-as-GC-route F1 adopted (DECISIONS.md D3b): enclosing Callable is REACHABLE, JVM finalization is defined runtime dispatch; confirmed_by INFERRED, never SOURCE. Database-build assumption adopted as project rule, extended set (DECISIONS.md D3c): Room generated _Impl validation calls getRequiredConverters at database build on the printed build; confirmed_by INFERRED. Counts before: 36 REACHABLE / 0 UNREACHABLE / 4 OPEN; after: 40 REACHABLE / 0 UNREACHABLE / 0 OPEN (40 rows, mechanically counted from the label column). Rows deliberately left OPEN in this batch per DECISIONS.md: none. No other row was changed; no conflict with DECISIONS.md was found in this batch. Build: not run. C1: not run. Nothing merged, nothing pushed.

## REVISION 2026-11-01 — OPEN-close round 2, group G7 (batches 50-53), labels only

Counts before = counts after: 36 REACHABLE / 0 UNREACHABLE / 4 OPEN. Label changes in this pass: 0. The four OPEN rows are one converter row and three finalize rows; their conditional flips are recorded below and in the rows themselves. Nothing was flipped, because every OPEN row depends on a convention (converters (xiii) or finalize (vi)) that this pass does not decide. The 25 REACHABLE $ rows in this file already apply the SET treatment; under the STRICT identity rule they would revert to OPEN (part of the 46 revert-at-risk $ rows across batches 50-52: 50: 3, 51: 25, 52: 18). That revert is the merger's decision, not a change made here.

Set-membership verification (fresh prints, this pass). FeedDao.java (110 lines) operations and FeedRepositoryImpl.java calls, all verified: addFeed :52 / repository :86, addFeeds :55 / :92, updateFeed :58 / :98, deleteFeed :61 / :104, deleteFeeds :64 / :110, getFeedById :67 / :116, getFeedByIdSingle :70 / :122, observeAllFeeds :73 / :128, getAllFeeds :76 / :134, getAllFeedsSingle :79 / :140, addItems :82 / :170, deleteItemsOlderThan :85 / :176, markAsRead :88 / :182, markAsUnread :91 / :188, markAsReadByFeedId :94 / :194, observeItemsByFeedId :97 / :200, getItemsByFeedIdSingle :100 / :206, getItemsIdByFeedId :103 / :212, findItemsExistingTitles :106 / :218, getItemsById :109 / :224. Every FeedDao operation is called at DAO-interface level by the repository.
- Bind-adapter set $1-$4 (rows 13-15, 25-27, 28-30, 31-33): plan binds FeedChannel, FeedItem, FeedChannel, FeedChannel. Adapters per entity plus operation type: insertion FeedChannel (serves addFeed and addFeeds), insertion FeedItem (addItems), update FeedChannel (updateFeed), deletion FeedChannel (serves deleteFeed and deleteFeeds). All four adapters' operations are called (repository lines above), so every $1-$4 row is a SET member regardless of which $N serves which adapter. No membership error found.
- Statement set $5-$7 (rows 34-39): the three void @Query methods with scalar parameters are deleteItemsOlderThan, markAsRead, and markAsUnread, all called (repository :176, :182, :188). markAsReadByFeedId (:194) takes an IN list, so Room compiles it inline in the Impl method instead of a SharedSQLiteStatement field; correctly, no $ row exists for it. The plain-select methods (getFeedById, getAllFeeds, getItemsIdByFeedId, findItemsExistingTitles, getItemsById) are implemented inline and generate no $ rows.
- Callable set $8-$12: row 40 ($8 <init>) plus batch-52 rows 1-5 ($8 call/finalize, $9 <init>/call/finalize) plus rows 16-24 ($10-$12). $8 is pinned, not merely set-assigned: its plan call returns FeedChannel, and getFeedByIdSingle is the only Rx method returning a single FeedChannel (repository :122). $9-$12 plan calls all return List, and the four List-returning Rx methods are observeAllFeeds (:128), getAllFeedsSingle (:140), observeItemsByFeedId (:200), and getItemsByFeedIdSingle (:206), all called. So every $9-$12 <init>/call row is a SET member; only their finalize rows stay OPEN (see below).

Conditional table (this batch, complete — 4 OPEN rows):
- Row 6 FeedDao_Impl.getRequiredConverters: stays OPEN. Conditional flip: REACHABLE INFERRED if and only if convention (xiii) is adopted on a printed Room dispatch showing Room calls DAO getRequiredConverters at database build, flipping together with 50/27, 52/11, and 53/4 (sibling 48/14 is the same family, outside this group).
- Rows 18, 21, 24 FeedDao_Impl$10/$11/$12.finalize: stay OPEN. Conditional flip: REACHABLE INFERRED if and only if convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route. Enclosing Callables are the REACHABLE rows 16, 19, 22 (SET members verified above), so membership is not in doubt; the blocker is purely the (vi) rule. These rows are NOT no_trigger_in_app (the Callables are created on printed routes) and must never be flipped to UNREACHABLE on zero app-code hits, because GC dispatch is by definition not an app-code call site.
- No other OPEN row exists in this batch.

Source for this pass (copies in ~/workspace/b50515253-openclose2-src/, connector-reconstructed 2026-11-01 05:18-05:21 copies copied verbatim, no new GitHub connector fetch in this pass because no needed file was missing locally; no fresh HTTP 429): AppDatabase.java SHA c673131c64be, FastResumeDao.java 3e6fcd70d6f2, FeedDao.java 2c8c954d738ca, TagInfoDao.java 61aee6239368, TorrentDao.java f24aab9a09ff2, FeedRepositoryImpl.java 1c5e193a62d1, TagRepositoryImpl.java d579b631ed85, TorrentRepositoryImpl.java fe8717338997. The core/storage/dao/ directory listing contains exactly those four DAO files, no generated Impl file. A grep over the round-2 source copies finds zero occurrences of finalize, getRequiredConverters, or Impl dispatch in app source; zero hits are never used as evidence of absence, and no generated source was printed, so no Impl identity is pinned individually. Framework note (recorded, not invented): the fw_src walked path fw_src/android-8.1.0_r1/libcore/ojluni/src/main/java/java/ contains only io and util, no lang/, hence no printed Object.java finalization dispatch exists in the branch; no framework citation is claimed. Build: not run. C1: not run. No push was made in this pass. No edit to graph_def.py, out/, PROGRESS_V2, AGENT_NOTES, tools/, or another agent's file. No project convention was decided in this pass.


## REVISION 2026-11-01 — OPEN-close pass (batches 50-52)

All OPEN rows in this file were re-derived from freshly printed source in this pass (source in ~/workspace/b505152-openclose-src/: AppDatabase.java, FastResumeDao.java, FeedDao.java, TagInfoDao.java, FeedRepositoryImpl.java, TagRepositoryImpl.java, TorrentRepositoryImpl.java, plus the core/storage/dao/ directory listing; one file at a time with ~25 s pauses, no fresh HTTP 429, no search_code result used as evidence). **Label changes in this file: 0.** Counts before = counts after: 36 REACHABLE / 0 UNREACHABLE / 4 OPEN. The OPEN rows stay OPEN for the reasons appended to their rows: getRequiredConverters rows need a printed Room dispatch or convention (xiii) decision; finalize rows need a convention (vi) decision or printed generated Callable source. Build: not run. C1: not run. No push was made in this pass. No edit to graph_def.py, out/, PROGRESS_V2, AGENT_NOTES, tools/, or another helper's file.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 51 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
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
| 6 | `FeedDao_Impl.getRequiredConverters` `()Ljava/util/List;` | REACHABLE | INFERRED | Generated-only method; no printed app call and no printed Room call site for it. Same as batch-50 row 27: stays OPEN (batch-48/53 precedent), not INFERRED REACHABLE. Flip condition: a printed Room dispatch showing Room calls DAO `getRequiredConverters` at database build flips this to REACHABLE INFERRED, together with rows 50/27 and 52/11. Needs printed Room dispatch or a saved full-repo grep; never flipped on absence. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: AppDatabase.java (87 lines, SHA 5836e2a4) getInstance :69-79, buildDatabase :81-87 (Room.databaseBuilder...build()), abstract DAO getters :61-67; DAO interface prints contain no getRequiredConverters declaration; fresh-corpus grep over all 7 fresh files for getRequiredConverters = zero hits; core/storage/dao/ lists only FastResumeDao, FeedDao, TagInfoDao, TorrentDao interfaces — no *_Impl.java in the tree, so no generated Room dispatch is printed. Label unchanged: still OPEN pending convention (xiii) — a printed Room dispatch showing Room calls DAO getRequiredConverters at database build, or a project decision adopting the database-build assumption, is the named close-out; never flipped on absence, and never to UNREACHABLE without a saved full-repo grep covering generated code.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (xiii) is adopted on a printed Room dispatch showing Room calls DAO getRequiredConverters at database build, together with 50/27, 51/6, 52/11, 53/4. No label change in this pass; no convention decided.] [APPLIED 2026-11-01 D3c: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
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
| 18 | `FeedDao_Impl$10.finalize` `()V` | REACHABLE | INFERRED | GC-only release of the RoomSQLiteQuery (Room Callable `finalize()` convention (vi), undecided project-wide): only the JVM garbage collector can invoke `finalize()` on a created Callable, nondeterministically, after the Callable is collected. That is not an app/framework route in the trigger-graph sense, but the Callable IS created (row 16), so this is NOT `no_trigger_in_app` either. Needs a project rule on `finalize()` before any label; never flipped to UNREACHABLE without a saved full-repo grep. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: enclosing Callable FeedDao_Impl$10.<init> (row 16) is REACHABLE INFERRED on the List-returning Rx repository set (FeedRepositoryImpl.java fresh: observeAllFeeds :128, getAllFeedsSingle :140, observeItemsByFeedId :200, getItemsByFeedIdSingle :206); fresh-corpus grep over all 7 fresh files for finalize = zero hits; core/storage/dao/ lists no *_Impl.java, so no generated Callable definition and no printed finalize override exists in the tree; the fw_src upload is a flat selection of framework files and contains no java/lang/Object.java, so no printed JVM finalization dispatch either. Label unchanged: still OPEN pending convention (vi) — the project rule on whether JVM GC dispatch counts as a trigger-graph route, or printed generated source showing the Callable overrides finalize, is the named close-out. NOT no_trigger_in_app (the Callable is created on a printed route); never flipped to UNREACHABLE without a saved full-repo grep covering generated code, and a grep over app source alone cannot rule out GC dispatch.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route, together with the 10-row finalize set (51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33, 53/29, 53/32). Enclosing Callable membership verified in the round-2 note above. No label change; NOT no_trigger_in_app.] [APPLIED 2026-11-01 D3b: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
| 19 | `FeedDao_Impl$11.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | REACHABLE | INFERRED | Callable for a List-returning Rx query (set note at row 16; proposal lead order: observeItemsByFeedId). Created when FeedRepositoryImpl.observeItemsByFeedId runs (FeedRepositoryImpl.java:200, fresh; caller FeedItemsViewModel.java:84, fresh) under the lead order, and under any set assignment its method is called. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 20 | `FeedDao_Impl$11.call` `()Ljava/util/List;` | REACHABLE | INFERRED | Runs when the Flowable from row 19's method is subscribed (Rx step INFERRED). No printed generated def. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 21 | `FeedDao_Impl$11.finalize` `()V` | REACHABLE | INFERRED | As row 18 (GC-only `finalize()`; Callable created at row 19). Needs a project rule on `finalize()`; NOT `no_trigger_in_app`. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: enclosing Callable FeedDao_Impl$11.<init> (row 19) is REACHABLE INFERRED on the List-returning Rx repository set (FeedRepositoryImpl.java fresh: observeAllFeeds :128, getAllFeedsSingle :140, observeItemsByFeedId :200, getItemsByFeedIdSingle :206); fresh-corpus grep over all 7 fresh files for finalize = zero hits; core/storage/dao/ lists no *_Impl.java, so no generated Callable definition and no printed finalize override exists in the tree; the fw_src upload is a flat selection of framework files and contains no java/lang/Object.java, so no printed JVM finalization dispatch either. Label unchanged: still OPEN pending convention (vi) — the project rule on whether JVM GC dispatch counts as a trigger-graph route, or printed generated source showing the Callable overrides finalize, is the named close-out. NOT no_trigger_in_app (the Callable is created on a printed route); never flipped to UNREACHABLE without a saved full-repo grep covering generated code, and a grep over app source alone cannot rule out GC dispatch.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route, together with the 10-row finalize set (51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33, 53/29, 53/32). Enclosing Callable membership verified in the round-2 note above. No label change; NOT no_trigger_in_app.] [APPLIED 2026-11-01 D3b: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
| 22 | `FeedDao_Impl$12.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | REACHABLE | INFERRED | Callable for a List-returning Rx query (set note at row 16; proposal lead order: getItemsByFeedIdSingle). Created when FeedRepositoryImpl.getItemsByFeedIdSingle runs (FeedRepositoryImpl.java:206, fresh; caller FeedItemsViewModel.java:89, fresh) under the lead order, and under any set assignment its method is called. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 23 | `FeedDao_Impl$12.call` `()Ljava/util/List;` | REACHABLE | INFERRED | Runs when the Single from row 22's method is subscribed (Rx step INFERRED). No printed generated def. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 24 | `FeedDao_Impl$12.finalize` `()V` | REACHABLE | INFERRED | As row 18 (GC-only `finalize()`; Callable created at row 22). Needs a project rule on `finalize()`; NOT `no_trigger_in_app`. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: enclosing Callable FeedDao_Impl$12.<init> (row 22) is REACHABLE INFERRED on the List-returning Rx repository set (FeedRepositoryImpl.java fresh: observeAllFeeds :128, getAllFeedsSingle :140, observeItemsByFeedId :200, getItemsByFeedIdSingle :206); fresh-corpus grep over all 7 fresh files for finalize = zero hits; core/storage/dao/ lists no *_Impl.java, so no generated Callable definition and no printed finalize override exists in the tree; the fw_src upload is a flat selection of framework files and contains no java/lang/Object.java, so no printed JVM finalization dispatch either. Label unchanged: still OPEN pending convention (vi) — the project rule on whether JVM GC dispatch counts as a trigger-graph route, or printed generated source showing the Callable overrides finalize, is the named close-out. NOT no_trigger_in_app (the Callable is created on a printed route); never flipped to UNREACHABLE without a saved full-repo grep covering generated code, and a grep over app source alone cannot rule out GC dispatch.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route, together with the 10-row finalize set (51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33, 53/29, 53/32). Enclosing Callable membership verified in the round-2 note above. No label change; NOT no_trigger_in_app.] [APPLIED 2026-11-01 D3b: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
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
