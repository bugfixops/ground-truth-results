**REVISION 2026-11-01 (Stream A Phase 1c, APPLY DECISIONS — UNVERIFIED).** Applied DECISIONS.md mechanically and only: row 27 (D3c). Database-build assumption adopted as project rule, extended set (DECISIONS.md D3c): Room generated _Impl validation calls getRequiredConverters at database build on the printed build; confirmed_by INFERRED. Counts before: 39 REACHABLE / 0 UNREACHABLE / 1 OPEN; after: 40 REACHABLE / 0 UNREACHABLE / 0 OPEN (40 rows, mechanically counted from the label column). Rows deliberately left OPEN in this batch per DECISIONS.md: none. No other row was changed; no conflict with DECISIONS.md was found in this batch. Build: not run. C1: not run. Nothing merged, nothing pushed.

## REVISION 2026-11-01 — OPEN-close round 2, group G7 (batches 50-53), labels only

Counts before = counts after: 39 REACHABLE / 0 UNREACHABLE / 1 OPEN. Label changes in this pass: 0. The single OPEN row is a converter row; its conditional flip is recorded below and in the row itself. Nothing in this file was flipped, because every OPEN row in this group depends on a project convention (SET-vs-STRICT, finalize (vi), or converters (xiii)) that this pass does not decide.

Set-membership verification (fresh prints, this pass). FastResumeDao.java (18 lines): add :14 (@Insert), getByTorrentId :17 (@Query plain select, implemented inline, no helper class). TorrentRepositoryImpl.java calls both: addFastResume :92 (db.fastResumeDao().add), getFastResumeById :97 (db.fastResumeDao().getByTorrentId). The plan descriptor for row 29 binds FastResume, so the single bind-adapter set is exactly FastResumeDao_Impl$1 (rows 28-30): one insertion adapter for the DAO's only insert. There is no second insert, no Rx method, and no void @Query method in FastResumeDao, so there is no second $ class, no statement set, and no Callable set. Rows 28-30 are already REACHABLE INFERRED under the SET treatment; under the STRICT identity rule they would revert to OPEN (3 of the 46 revert-at-risk $ rows across batches 50-52 in this group: 50: 3, 51: 25, 52: 18). That revert is the merger's decision, not a change made here.

Conditional table (this batch, complete — 1 OPEN row):
- Row 27 FastResumeDao_Impl.getRequiredConverters: stays OPEN. Conditional flip: REACHABLE INFERRED if and only if convention (xiii) is adopted on a printed Room dispatch showing Room calls DAO getRequiredConverters at database build. It flips together with 51/6, 52/11, and 53/4 (the four DAO converter rows in this group; sibling batch 48 row 14 AppDatabase_Impl.getRequiredTypeConverters belongs to the same family but is outside this group). No app-code call exists in the printed source, and no Room dispatch was printed, so the row is not flipped on a database-build assumption.
- No other OPEN row exists in this batch. Group OPEN accounting: converters 4 + finalize 10 + batch-53 SET 21 = 35 OPEN rows across batches 50-53, and every one is accounted for in its batch's conditional table.

Source for this pass (copies in ~/workspace/b50515253-openclose2-src/, connector-reconstructed 2026-11-01 05:18-05:21 copies copied verbatim, no new GitHub connector fetch in this pass because no needed file was missing locally; no fresh HTTP 429): AppDatabase.java SHA c673131c64be, FastResumeDao.java 3e6fcd70d6f2, FeedDao.java 2c8c954d738ca, TagInfoDao.java 61aee6239368, TorrentDao.java f24aab9a09ff2, FeedRepositoryImpl.java 1c5e193a62d1, TagRepositoryImpl.java d579b631ed85, TorrentRepositoryImpl.java fe8717338997. The core/storage/dao/ directory listing contains exactly those four DAO files, no generated Impl file. A grep over the round-2 source copies finds zero occurrences of finalize, getRequiredConverters, or Impl dispatch in app source; zero hits are never used as evidence of absence, and no generated source was printed, so no Impl identity is pinned individually. Framework note (recorded, not invented): the fw_src walked path fw_src/android-8.1.0_r1/libcore/ojluni/src/main/java/java/ contains only io and util, no lang/, hence no printed Object.java finalization dispatch exists in the branch; no framework citation is claimed. Build: not run. C1: not run. No push was made in this pass. No edit to graph_def.py, out/, PROGRESS_V2, AGENT_NOTES, tools/, or another agent's file. No project convention was decided in this pass.


## REVISION 2026-11-01 — OPEN-close pass (batches 50-52)

All OPEN rows in this file were re-derived from freshly printed source in this pass (source in ~/workspace/b505152-openclose-src/: AppDatabase.java, FastResumeDao.java, FeedDao.java, TagInfoDao.java, FeedRepositoryImpl.java, TagRepositoryImpl.java, TorrentRepositoryImpl.java, plus the core/storage/dao/ directory listing; one file at a time with ~25 s pauses, no fresh HTTP 429, no search_code result used as evidence). **Label changes in this file: 0.** Counts before = counts after: 39 REACHABLE / 0 UNREACHABLE / 1 OPEN. The OPEN rows stay OPEN for the reasons appended to their rows: getRequiredConverters rows need a printed Room dispatch or convention (xiii) decision; finalize rows need a convention (vi) decision or printed generated Callable source. Build: not run. C1: not run. No push was made in this pass. No edit to graph_def.py, out/, PROGRESS_V2, AGENT_NOTES, tools/, or another helper's file.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 50 — merge-ready part — UNVERIFIED

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
- Scope: batch 50 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Prior work (the batch-50 WP1 proposal) was used as an INPUT / lead list only; every row below
  was re-judged against source freshly fetched in this pass (see "Printed source used"), and the
  changes vs that proposal are listed under "Changes vs the prior proposal". No proposal verdict
  was copied without a check.
- Labels are REACHABLE / UNREACHABLE / OPEN only. No UNREACHABLE row is claimed in this batch
  (no saved full-repo grep was run, so absence in printed files is never treated as absence in
  the app). `confirmed_by` is SOURCE or INFERRED only (never DYN, FW-MEMORY, or UNVERIFIED);
  OPEN rows carry "-" for `confirmed_by`, as in sibling merge-ready files.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 50 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
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

| 1 | `TagRepositoryImpl.getByTorrentIdAsync` `(Ljava/lang/String;)Lio/reactivex/Single;` | REACHABLE | SOURCE | Def TagRepositoryImpl.java:69-70 (`db.tagInfoDao().getByTorrentIdAsync`). Caller DetailTorrentViewModel.java:144 (`tagRepo.getByTorrentIdAsync(torrentId)`), fresh. |
| 2 | `TagRepositoryImpl.insert` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | SOURCE | Def TagRepositoryImpl.java:39-41 (`db.tagInfoDao().insert`). Caller AddTagViewModel.java:69 (`tagRepo.insert(info)`), fresh. |
| 3 | `TagRepositoryImpl.observeAll` `()Lio/reactivex/Flowable;` | REACHABLE | SOURCE | Def TagRepositoryImpl.java:59-61 (`db.tagInfoDao().observeAll`). Callers MainViewModel.java:183, SelectTagViewModel.java:63, TorrentInfoProvider.java:298, all fresh. |
| 4 | `TagRepositoryImpl.observeByTorrentId` `(Ljava/lang/String;)Lio/reactivex/Flowable;` | REACHABLE | SOURCE | Def TagRepositoryImpl.java:64-66 (`db.tagInfoDao().observeByTorrentId`). Callers DetailTorrentViewModel.java:148, TorrentInfoProvider.java:219, fresh. |
| 5 | `TagRepositoryImpl.update` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | SOURCE | Def TagRepositoryImpl.java:44-46 (`db.tagInfoDao().update`). Caller AddTagViewModel.java:71 (`tagRepo.update(info)`), fresh. |
| 6 | `TorrentRepositoryImpl.<clinit>` `()V` | REACHABLE | INFERRED | No source def (JVM static initialiser; non-constant TAG = `getSimpleName()` at TorrentRepositoryImpl.java:41, fresh). Runs on first use of the class; class constructed at RepositoryHelper.java:46-47, fresh. <clinit>-on-first-use convention (ix) is undecided project-wide; here first use (construction) IS printed. |
| 7 | `TorrentRepositoryImpl.<init>` `(Landroid/content/Context;Lorg/proninyaroslav/libretorrent/core/storage/AppDatabase;)V` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:50-53. Constructed at RepositoryHelper.java:46-47, via `getTorrentRepository` called by TorrentEngine.java:130 and DetailTorrentViewModel.java:109, all fresh. |
| 8 | `TorrentRepositoryImpl.addFastResume` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/FastResume;)V` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:91-93 (`db.fastResumeDao().add`). Caller TorrentDownloadImpl.java:520 (`repo.addFastResume(new FastResume(...))`), fresh. Also the printed caller for row 25. |
| 9 | `TorrentRepositoryImpl.addTag` `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:131-133 (`db.torrentDao().addTag`). Caller DetailTorrentViewModel.java:152 (`repo.addTag(torrentId, info)`), fresh. Also the route for row 38. |
| 10 | `TorrentRepositoryImpl.addTorrent` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;)V` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:56-58 (`db.torrentDao().add`). Caller TorrentSessionImpl.java:285 (`repo.addTorrent(torrent)`), fresh. Also the route for row 37. |
| 11 | `TorrentRepositoryImpl.deleteTag` `(Ljava/lang/String;Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:136-138 (`db.torrentDao().deleteTag`). Caller DetailTorrentViewModel.java:156 (`repo.deleteTag(torrentId, info)`), fresh. |
| 12 | `TorrentRepositoryImpl.deleteTorrent` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;)V` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:66-68 (`db.torrentDao().delete`). Callers TorrentSessionImpl.java:313,386 and TorrentDownloadImpl.java:777, fresh. |
| 13 | `TorrentRepositoryImpl.getAllTorrents` `()Ljava/util/List;` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:86-88 (`db.torrentDao().getAllTorrents`). Callers TorrentEngine.java:817 and TorrentSessionImpl.java:401, fresh. |
| 14 | `TorrentRepositoryImpl.getFastResumeById` `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/FastResume;` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:96-98 (`db.fastResumeDao().getByTorrentId`). Caller TorrentSessionImpl.java:1686 (`repo.getFastResumeById(id)`), fresh. Also the printed caller for row 26. |
| 15 | `TorrentRepositoryImpl.getSessionFile` `()Ljava/lang/String;` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:109-119 (reads `TORRENT_SESSION_FILE` = `session`, :44, via FileDataModel). Caller TorrentSessionImpl.java:1195 (`repo.getSessionFile()`), fresh. |
| 16 | `TorrentRepositoryImpl.getTorrentById` `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:71-73 (`db.torrentDao().getTorrentById`). Callers TorrentEngine.java:767,840 and TorrentSessionImpl.java:280,335,384, fresh. |
| 17 | `TorrentRepositoryImpl.getTorrentByIdSingle` `(Ljava/lang/String;)Lio/reactivex/Single;` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:76-78 (`db.torrentDao().getTorrentByIdSingle`). Callers TorrentEngine.java:1307,1330,1349,1401,1426, fresh. |
| 18 | `TorrentRepositoryImpl.observeTorrentById` `(Ljava/lang/String;)Lio/reactivex/Flowable;` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:81-83 (`db.torrentDao().observeTorrentById`). Caller DetailTorrentViewModel.java:176 (`repo.observeTorrentById(torrentId)`), fresh. |
| 19 | `TorrentRepositoryImpl.replaceTags` `(Ljava/lang/String;Ljava/util/List;)V` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:122-128 (`db.torrentDao().replaceTags`). Caller TorrentSessionImpl.java:287 (`repo.replaceTags(torrent.id, params.tags)`), fresh. |
| 20 | `TorrentRepositoryImpl.saveSession` `([B)V` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:101-106 (writes `FileDataModel.TORRENT_SESSION_FILE`). Caller TorrentSessionImpl.java:1234 (`repo.saveSession(b)`), fresh. |
| 21 | `TorrentRepositoryImpl.updateTorrent` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;)V` | REACHABLE | SOURCE | Def TorrentRepositoryImpl.java:61-63 (`db.torrentDao().update`). Callers TorrentEngine.java:1262 and TorrentSessionImpl.java:1524, fresh. |
| 22 | `UriConverter.fromUri` `(Landroid/net/Uri;)Ljava/lang/String;` | REACHABLE | INFERRED | Def UriConverter.java:36-39 (`@TypeConverter`, `return uri.toString()`), fresh. No app code calls `fromUri` by name: Room invokes it when writing a `Uri`-typed entity field to a String column. Field printed: `Torrent.downloadPath` is `Uri` (Torrent.java:57, fresh); Torrent rows are written by row 10 (addTorrent, TorrentSessionImpl:285, fresh); converter registered at AppDatabase.java:53, fresh. Dispatch unprinted, hence INFERRED. Distinct from batch-4 `UriConverter.<init>` (OPEN there): converter methods are static, so no construction is needed for this route. |
| 23 | `UriConverter.toUri` `(Ljava/lang/String;)Landroid/net/Uri;` | REACHABLE | INFERRED | Def UriConverter.java:30-33 (`@TypeConverter`, `Uri.parse(uriStr)`), fresh. Read direction of row 22: Room invokes it when reading the `downloadPath` String column back into a `Uri` (rows 13/16/17 routes, all fresh). Converter registered at AppDatabase.java:53, fresh. Dispatch unprinted, hence INFERRED. |
| 24 | `FastResumeDao_Impl.<init>` `(Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Generated class, no printed def (not in `final_java_only`). Room constructs `FastResumeDao_Impl` when `fastResumeDao()` (AppDatabase.java:63, fresh) is first called; that accessor is called at TorrentRepositoryImpl.java:92,97 (rows 8, 14, fresh). Dispatch unprinted, hence INFERRED. |
| 25 | `FastResumeDao_Impl.add` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/FastResume;)V` | REACHABLE | INFERRED | Generated implementation of `FastResumeDao.add` (FastResumeDao.java:14, `@Insert`, fresh). Via TorrentRepositoryImpl.java:92 (row 8, fresh); upstream caller TorrentDownloadImpl.java:520, fresh. Room dispatch unprinted, hence INFERRED. |
| 26 | `FastResumeDao_Impl.getByTorrentId` `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/FastResume;` | REACHABLE | INFERRED | Generated implementation of `FastResumeDao.getByTorrentId` (FastResumeDao.java:17, `@Query`, fresh). Via TorrentRepositoryImpl.java:97 (row 14, fresh); upstream caller TorrentSessionImpl.java:1686, fresh. Room dispatch unprinted, hence INFERRED. |
| 27 | `FastResumeDao_Impl.getRequiredConverters` `()Ljava/util/List;` | REACHABLE | INFERRED | Generated-only method; no printed app call and no printed Room call site for it. Room dispatch for `getRequiredConverters` was not printed, so this stays OPEN, not INFERRED REACHABLE (batch-48/53 precedent for the equivalent converter method). Flip condition: a printed Room dispatch showing Room calls DAO `getRequiredConverters` at database build flips this to REACHABLE INFERRED. This DIFFERS from the batch-50 proposal (REACHABLE INFERRED on a database-build assumption); merger must pick one treatment for rows 50/27, 51/6, 52/11 together. Needs printed Room dispatch or a saved full-repo grep; never flipped on absence. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: AppDatabase.java (87 lines, SHA 5836e2a4) getInstance :69-79, buildDatabase :81-87 (Room.databaseBuilder...build()), abstract DAO getters :61-67; DAO interface prints contain no getRequiredConverters declaration; fresh-corpus grep over all 7 fresh files for getRequiredConverters = zero hits; core/storage/dao/ lists only FastResumeDao, FeedDao, TagInfoDao, TorrentDao interfaces — no *_Impl.java in the tree, so no generated Room dispatch is printed. Label unchanged: still OPEN pending convention (xiii) — a printed Room dispatch showing Room calls DAO getRequiredConverters at database build, or a project decision adopting the database-build assumption, is the named close-out; never flipped on absence, and never to UNREACHABLE without a saved full-repo grep covering generated code.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (xiii) is adopted on a printed Room dispatch showing Room calls DAO getRequiredConverters at database build, together with 50/27, 51/6, 52/11, 53/4. No label change in this pass; no convention decided.] [APPLIED 2026-11-01 D3c: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
| 28 | `FastResumeDao_Impl$1.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FastResumeDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Generated insertion-adapter inner class used by `add()` (row 25). `FastResumeDao` has only one `@Insert` method (`add`, FastResumeDao.java:14, fresh), so `$1` identity is pinned by elimination, not merely by order — but it is NOT pinned by printed generated source, so under the batch-53 strict `$N` rule this row reverts to OPEN (see strict-`$N` list). Constructor runs when the adapter is created for the first insert. No printed def; INFERRED. |
| 29 | `FastResumeDao_Impl$1.bind` `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/FastResume;)V` | REACHABLE | INFERRED | Generated adapter method binding a `FastResume` row's values into the insert statement; runs on every `add()` (row 25 route). No printed def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 30 | `FastResumeDao_Impl$1.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Generated adapter method returning the `INSERT INTO FastResume ...` SQL; runs when the adapter is created for `add()` (row 25 route). No printed def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 31 | `FeedDao_Impl.<init>` `(Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Generated class, no printed def. Constructed when `feedDao()` (AppDatabase.java:65, fresh) is first called; that accessor is called by every `FeedRepositoryImpl` method (e.g. FeedRepositoryImpl.java:86,92,104, fresh). Dispatch unprinted, hence INFERRED. |
| 32 | `FeedDao_Impl.addFeed` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;)J` | REACHABLE | INFERRED | Generated implementation of `FeedDao.addFeed` (FeedDao.java:52, `@Insert`, fresh). Via FeedRepositoryImpl.java:86, fresh; caller AddFeedViewModel.java:189, fresh. Room dispatch unprinted, hence INFERRED. |
| 33 | `FeedDao_Impl.addFeeds` `(Ljava/util/List;)[J` | REACHABLE | INFERRED | Generated implementation of `FeedDao.addFeeds` (FeedDao.java:55, fresh). Via FeedRepositoryImpl.java:92, fresh; caller FeedViewModel.java:144, fresh. Room dispatch unprinted, hence INFERRED. |
| 34 | `FeedDao_Impl.addItems` `(Ljava/util/List;)V` | REACHABLE | INFERRED | Generated implementation of `FeedDao.addItems` (FeedDao.java:82, fresh). Via FeedRepositoryImpl.java:170, fresh; caller FeedFetcherWorker.java:172, fresh. Room dispatch unprinted, hence INFERRED. |
| 35 | `FeedDao_Impl.deleteFeed` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;)V` | REACHABLE | INFERRED | Generated implementation of `FeedDao.deleteFeed` (FeedDao.java:61, `@Delete`, fresh). Via FeedRepositoryImpl.java:104, fresh; caller AddFeedViewModel.java:133, fresh. Room dispatch unprinted, hence INFERRED. |
| 36 | `FeedDao_Impl.deleteFeeds` `(Ljava/util/List;)V` | REACHABLE | INFERRED | Generated implementation of `FeedDao.deleteFeeds` (FeedDao.java:64, fresh). Via FeedRepositoryImpl.java:110, fresh; caller FeedViewModel.java:87, fresh. Room dispatch unprinted, hence INFERRED. |
| 37 | `FeedDao_Impl.deleteItemsOlderThan` `(J)V` | REACHABLE | INFERRED | Generated implementation of `FeedDao.deleteItemsOlderThan` (FeedDao.java:85; query `DELETE FROM FeedItem WHERE fetchDate < :keepDateBorderTime`, FeedDao.java:42, fresh). Via FeedRepositoryImpl.java:176, fresh; caller FeedFetcherWorker.java:209, fresh. Room dispatch unprinted, hence INFERRED. |
| 38 | `FeedDao_Impl.findItemsExistingTitles` `(Ljava/util/List;)Ljava/util/List;` | REACHABLE | INFERRED | Generated implementation of `FeedDao.findItemsExistingTitles` (FeedDao.java:106; query `SELECT title FROM FeedItem WHERE title IN (:titles)`, FeedDao.java:48, fresh). Via FeedRepositoryImpl.java:218, fresh; caller FeedFetcherWorker.java:202, fresh. Room dispatch unprinted, hence INFERRED. |
| 39 | `FeedDao_Impl.getAllFeeds` `()Ljava/util/List;` | REACHABLE | INFERRED | Generated implementation of `FeedDao.getAllFeeds` (FeedDao.java:76; query `SELECT * FROM FeedChannel`, FeedDao.java:40, fresh). Via FeedRepositoryImpl.java:134, fresh; caller FeedFetcherWorker.java:100, fresh. Room dispatch unprinted, hence INFERRED. |
| 40 | `FeedDao_Impl.getAllFeedsSingle` `()Lio/reactivex/Single;` | REACHABLE | INFERRED | Generated implementation of `FeedDao.getAllFeedsSingle` (FeedDao.java:79, same query, fresh). Via FeedRepositoryImpl.java:140, fresh; caller FeedViewModel.java:77, fresh. Room dispatch unprinted, hence INFERRED. |

## Counts (mechanically verified — see generator)

- Judged: **40 / 40**. REACHABLE proposed: **39**. UNREACHABLE proposed: **0**.
  OPEN: **1**. confirmed_by: SOURCE 20 / INFERRED 19 (OPEN rows carry "-").
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
