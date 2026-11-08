**REVISION 2026-11-01 (Stream A Phase 1c, APPLY DECISIONS — UNVERIFIED).** Applied DECISIONS.md mechanically and only: row 2 (D3b), row 5 (D3b), row 11 (D3c), row 27 (D3b), row 30 (D3b), row 33 (D3b). Finalize-as-GC-route F1 adopted (DECISIONS.md D3b): enclosing Callable is REACHABLE, JVM finalization is defined runtime dispatch; confirmed_by INFERRED, never SOURCE. Database-build assumption adopted as project rule, extended set (DECISIONS.md D3c): Room generated _Impl validation calls getRequiredConverters at database build on the printed build; confirmed_by INFERRED. Counts before: 34 REACHABLE / 0 UNREACHABLE / 6 OPEN; after: 40 REACHABLE / 0 UNREACHABLE / 0 OPEN (40 rows, mechanically counted from the label column). Rows deliberately left OPEN in this batch per DECISIONS.md: none. No other row was changed; no conflict with DECISIONS.md was found in this batch. Build: not run. C1: not run. Nothing merged, nothing pushed.

## REVISION 2026-11-01 — OPEN-close round 2, group G7 (batches 50-53), labels only

Counts before = counts after: 34 REACHABLE / 0 UNREACHABLE / 6 OPEN. Label changes in this pass: 0. The six OPEN rows are one converter row and five finalize rows; their conditional flips are recorded below and in the rows themselves. Nothing was flipped, because every OPEN row depends on a convention (converters (xiii) or finalize (vi)) that this pass does not decide. The 18 REACHABLE $ rows in this file already apply the SET treatment; under the STRICT identity rule they would revert to OPEN (part of the 46 revert-at-risk $ rows across batches 50-52: 50: 3, 51: 25, 52: 18). That revert is the merger's decision, not a change made here.

Set-membership verification (fresh prints, this pass).
Feed part. Row 1 ($8 call) is pinned: its plan call returns FeedChannel and getFeedByIdSingle (FeedDao.java:70, FeedRepositoryImpl.java:122) is the only Rx method returning a single FeedChannel; its <init> is batch-51 row 40. Rows 3-4 ($9 <init>/call) belong to the List-returning Callable set verified in batch 51 (observeAllFeeds :128, getAllFeedsSingle :140, observeItemsByFeedId :200, getItemsByFeedIdSingle :206, all called). No membership error found.
Tag part. TagInfoDao.java (64 lines) operations and TagRepositoryImpl.java calls, all verified: insert :39 / repository :40, update :42 / :45, delete :45 / :50, getByName :48 / :55, observeAll :51 / :60, observeByTorrentId :55 / :65, getByTorrentIdAsync :59 / :70, getByTorrentId :63 / :75. Every TagInfoDao operation is called at DAO-interface level by the repository.
- Bind-adapter set $1-$3 (rows 16-24): plan binds TagInfo, TagInfo, TagInfo. Adapters per entity plus operation type: insertion TagInfo (insert), update TagInfo (update), deletion TagInfo (delete). All three operations are called, so every $1-$3 row is a SET member regardless of which $N serves which adapter. No membership error found.
- Callable set $4-$6 (rows 25-33 except finalize rows): plan calls all return List, and the three List-returning Rx methods are observeAll (:60), observeByTorrentId (:65), and getByTorrentIdAsync (:70), all called. So every $4-$6 <init>/call row is a SET member; only their finalize rows stay OPEN (see below). The plain methods getByName (:55) and getByTorrentId (:75) are implemented inline and correctly generate no $ rows.

Conditional table (this batch, complete — 6 OPEN rows):
- Row 11 TagInfoDao_Impl.getRequiredConverters: stays OPEN. Conditional flip: REACHABLE INFERRED if and only if convention (xiii) is adopted on a printed Room dispatch showing Room calls DAO getRequiredConverters at database build, flipping together with 50/27, 51/6, and 53/4 (sibling 48/14 is the same family, outside this group).
- Rows 2, 5, 27, 30, 33 finalize (FeedDao_Impl$8, $9; TagInfoDao_Impl$4, $5, $6): stay OPEN. Conditional flip: REACHABLE INFERRED if and only if convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route. Enclosing Callables are REACHABLE rows (Feed $8: batch-51 row 40 and row 1 here; Feed $9: rows 3-4 here; Tag $4/$5/$6: rows 25-26, 28-29, 31-32 here), all SET members verified above, so membership is not in doubt; the blocker is purely the (vi) rule. These rows are NOT no_trigger_in_app and must never be flipped to UNREACHABLE on zero app-code hits.
- No other OPEN row exists in this batch.

Source for this pass (copies in ~/workspace/b50515253-openclose2-src/, connector-reconstructed 2026-11-01 05:18-05:21 copies copied verbatim, no new GitHub connector fetch in this pass because no needed file was missing locally; no fresh HTTP 429): AppDatabase.java SHA c673131c64be, FastResumeDao.java 3e6fcd70d6f2, FeedDao.java 2c8c954d738ca, TagInfoDao.java 61aee6239368, TorrentDao.java f24aab9a09ff2, FeedRepositoryImpl.java 1c5e193a62d1, TagRepositoryImpl.java d579b631ed85, TorrentRepositoryImpl.java fe8717338997. The core/storage/dao/ directory listing contains exactly those four DAO files, no generated Impl file. A grep over the round-2 source copies finds zero occurrences of finalize, getRequiredConverters, or Impl dispatch in app source; zero hits are never used as evidence of absence, and no generated source was printed, so no Impl identity is pinned individually. Framework note (recorded, not invented): the fw_src walked path fw_src/android-8.1.0_r1/libcore/ojluni/src/main/java/java/ contains only io and util, no lang/, hence no printed Object.java finalization dispatch exists in the branch; no framework citation is claimed. Build: not run. C1: not run. No push was made in this pass. No edit to graph_def.py, out/, PROGRESS_V2, AGENT_NOTES, tools/, or another agent's file. No project convention was decided in this pass.


## REVISION 2026-11-01 — OPEN-close pass (batches 50-52)

All OPEN rows in this file were re-derived from freshly printed source in this pass (source in ~/workspace/b505152-openclose-src/: AppDatabase.java, FastResumeDao.java, FeedDao.java, TagInfoDao.java, FeedRepositoryImpl.java, TagRepositoryImpl.java, TorrentRepositoryImpl.java, plus the core/storage/dao/ directory listing; one file at a time with ~25 s pauses, no fresh HTTP 429, no search_code result used as evidence). **Label changes in this file: 0.** Counts before = counts after: 34 REACHABLE / 0 UNREACHABLE / 6 OPEN. The OPEN rows stay OPEN for the reasons appended to their rows: getRequiredConverters rows need a printed Room dispatch or convention (xiii) decision; finalize rows need a convention (vi) decision or printed generated Callable source. Build: not run. C1: not run. No push was made in this pass. No edit to graph_def.py, out/, PROGRESS_V2, AGENT_NOTES, tools/, or another helper's file.

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 52 — merge-ready part — UNVERIFIED

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
- Scope: batch 52 only, LibreTorrent labels only, no other batch/app, no device replay, no Aegis.
- Prior work (the batch-52 WP1 proposal) was used as an INPUT / lead list only; every row below
  was re-judged against source freshly fetched in this pass (see "Printed source used"), and the
  changes vs that proposal are listed under "Changes vs the prior proposal". No proposal verdict
  was copied without a check.
- Labels are REACHABLE / UNREACHABLE / OPEN only. No UNREACHABLE row is claimed in this batch
  (no saved full-repo grep was run, so absence in printed files is never treated as absence in
  the app). `confirmed_by` is SOURCE or INFERRED only (never DYN, FW-MEMORY, or UNVERIFIED);
  OPEN rows carry "-" for `confirmed_by`, as in sibling merge-ready files.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 52 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
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

| 1 | `FeedDao_Impl$8.call` `()Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;` | REACHABLE | INFERRED | getFeedByIdSingle Callable `call()`. Pinned, not merely set-assigned: its descriptor returns `FeedChannel`, and `getFeedByIdSingle` (FeedDao.java:70, fresh) is the ONLY Rx method returning a single FeedChannel. Runs when the Single from FeedRepositoryImpl.getFeedByIdSingle (FeedRepositoryImpl.java:122, fresh; caller AddFeedViewModel.java:151, fresh) is subscribed; the Rx subscription step is unprinted library dispatch, hence INFERRED. No printed generated def. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 2 | `FeedDao_Impl$8.finalize` `()V` | REACHABLE | INFERRED | GC-only `finalize()` (convention (vi), as batch-51 rows 18/21/24): only the JVM GC can invoke it on the created Callable (batch-51 row 40). Not an app/framework route, but NOT `no_trigger_in_app` either. Needs a project rule on `finalize()`; never flipped to UNREACHABLE without a saved full-repo grep. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: enclosing Callable FeedDao_Impl$8.<init> (batch-51 row 40, pinned getFeedByIdSingle) is REACHABLE INFERRED on FeedRepositoryImpl.java fresh: getFeedByIdSingle :122; fresh-corpus grep over all 7 fresh files for finalize = zero hits; core/storage/dao/ lists no *_Impl.java, so no generated Callable definition and no printed finalize override exists in the tree; the fw_src upload is a flat selection of framework files and contains no java/lang/Object.java, so no printed JVM finalization dispatch either. Label unchanged: still OPEN pending convention (vi) — the project rule on whether JVM GC dispatch counts as a trigger-graph route, or printed generated source showing the Callable overrides finalize, is the named close-out. NOT no_trigger_in_app (the Callable is created on a printed route); never flipped to UNREACHABLE without a saved full-repo grep covering generated code, and a grep over app source alone cannot rule out GC dispatch.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route, together with the 10-row finalize set (51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33, 53/29, 53/32). Enclosing Callable membership verified in the round-2 note above. No label change; NOT no_trigger_in_app.] [APPLIED 2026-11-01 D3b: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
| 3 | `FeedDao_Impl$9.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/FeedDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | REACHABLE | INFERRED | Callable for a List-returning Rx query. Set note (batch-51 row 16, applies here and to row 4): the four List-returning Rx methods are `observeAllFeeds` (FeedDao.java:73), `getAllFeedsSingle` (:79), `observeItemsByFeedId` (:97) and `getItemsByFeedIdSingle` (:100) — all called via the repository with fresh callers (FeedViewModel.java:82,77; FeedItemsViewModel.java:84,89) — so every callable in the set is used, whichever `$N` maps to which method. Proposal lead order puts `$9` = observeAllFeeds (FeedRepositoryImpl.java:128, fresh; caller FeedViewModel.java:82, fresh); that assignment is NOT adopted as a label basis. `<init>` runs when the DAO method is called. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 4 | `FeedDao_Impl$9.call` `()Ljava/util/List;` | REACHABLE | INFERRED | Runs when the Flowable/Single from row 3's method is subscribed (Rx step INFERRED). No printed generated def. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 5 | `FeedDao_Impl$9.finalize` `()V` | REACHABLE | INFERRED | GC-only `finalize()` (as row 2; Callable created at row 3). Needs a project rule on `finalize()`; NOT `no_trigger_in_app`. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: enclosing Callable FeedDao_Impl$9.<init> (row 3) is REACHABLE INFERRED on the List-returning Rx repository set (FeedRepositoryImpl.java fresh: observeAllFeeds :128, getAllFeedsSingle :140, observeItemsByFeedId :200, getItemsByFeedIdSingle :206); fresh-corpus grep over all 7 fresh files for finalize = zero hits; core/storage/dao/ lists no *_Impl.java, so no generated Callable definition and no printed finalize override exists in the tree; the fw_src upload is a flat selection of framework files and contains no java/lang/Object.java, so no printed JVM finalization dispatch either. Label unchanged: still OPEN pending convention (vi) — the project rule on whether JVM GC dispatch counts as a trigger-graph route, or printed generated source showing the Callable overrides finalize, is the named close-out. NOT no_trigger_in_app (the Callable is created on a printed route); never flipped to UNREACHABLE without a saved full-repo grep covering generated code, and a grep over app source alone cannot rule out GC dispatch.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route, together with the 10-row finalize set (51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33, 53/29, 53/32). Enclosing Callable membership verified in the round-2 note above. No label change; NOT no_trigger_in_app.] [APPLIED 2026-11-01 D3b: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
| 6 | `TagInfoDao_Impl.<init>` `(Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Generated class, no printed def. Constructed when `tagInfoDao()` (AppDatabase.java:67, fresh) is first called; TagRepositoryImpl calls `db.tagInfoDao()` in every method (TagRepositoryImpl.java:40,45,50,55,60,65,70,75, fresh). Dispatch unprinted, hence INFERRED. |
| 7 | `TagInfoDao_Impl.delete` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | INFERRED | Generated implementation of `TagInfoDao.delete` (TagInfoDao.java:45, `@Delete`, fresh). Via TagRepositoryImpl.java:50, fresh; caller MainViewModel.java:187, fresh. Room dispatch unprinted, hence INFERRED. |
| 8 | `TagInfoDao_Impl.getByName` `(Ljava/lang/String;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;` | REACHABLE | INFERRED | Generated implementation of `TagInfoDao.getByName` (TagInfoDao.java:48, fresh). Via TagRepositoryImpl.java:55, fresh; caller AddTagViewModel.java:65, fresh. Room dispatch unprinted, hence INFERRED. |
| 9 | `TagInfoDao_Impl.getByTorrentId` `(Ljava/lang/String;)Ljava/util/List;` | REACHABLE | INFERRED | Generated implementation of `TagInfoDao.getByTorrentId` (TagInfoDao.java:63, fresh). Via TagRepositoryImpl.java:75, fresh; callers TorrentEngine.java:771,821, fresh. Room dispatch unprinted, hence INFERRED. |
| 10 | `TagInfoDao_Impl.getByTorrentIdAsync` `(Ljava/lang/String;)Lio/reactivex/Single;` | REACHABLE | INFERRED | Generated implementation of `TagInfoDao.getByTorrentIdAsync` (TagInfoDao.java:59, `Single<List<TagInfo>>`, fresh). Via TagRepositoryImpl.java:70, fresh; caller DetailTorrentViewModel.java:144, fresh. Its Callable is one of `$4-$6` (set note at row 25). Room dispatch unprinted, hence INFERRED. |
| 11 | `TagInfoDao_Impl.getRequiredConverters` `()Ljava/util/List;` | REACHABLE | INFERRED | Generated-only method; no printed app call and no printed Room call site for it. Same as batch-50 row 27 and batch-51 row 6: stays OPEN (batch-48/53 precedent), not INFERRED REACHABLE. Flip condition: a printed Room dispatch showing Room calls DAO `getRequiredConverters` at database build flips this to REACHABLE INFERRED, together with rows 50/27 and 51/6. Needs printed Room dispatch or a saved full-repo grep; never flipped on absence. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: AppDatabase.java (87 lines, SHA 5836e2a4) getInstance :69-79, buildDatabase :81-87 (Room.databaseBuilder...build()), abstract DAO getters :61-67; DAO interface prints contain no getRequiredConverters declaration; fresh-corpus grep over all 7 fresh files for getRequiredConverters = zero hits; core/storage/dao/ lists only FastResumeDao, FeedDao, TagInfoDao, TorrentDao interfaces — no *_Impl.java in the tree, so no generated Room dispatch is printed. Label unchanged: still OPEN pending convention (xiii) — a printed Room dispatch showing Room calls DAO getRequiredConverters at database build, or a project decision adopting the database-build assumption, is the named close-out; never flipped on absence, and never to UNREACHABLE without a saved full-repo grep covering generated code.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (xiii) is adopted on a printed Room dispatch showing Room calls DAO getRequiredConverters at database build, together with 50/27, 51/6, 52/11, 53/4. No label change in this pass; no convention decided.] [APPLIED 2026-11-01 D3c: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
| 12 | `TagInfoDao_Impl.insert` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | INFERRED | Generated implementation of `TagInfoDao.insert` (TagInfoDao.java:39, `@Insert`, fresh). Via TagRepositoryImpl.java:40, fresh; caller AddTagViewModel.java:69, fresh. Room dispatch unprinted, hence INFERRED. |
| 13 | `TagInfoDao_Impl.observeAll` `()Lio/reactivex/Flowable;` | REACHABLE | INFERRED | Generated implementation of `TagInfoDao.observeAll` (TagInfoDao.java:51, fresh). Via TagRepositoryImpl.java:60, fresh; callers MainViewModel.java:183, SelectTagViewModel.java:63, TorrentInfoProvider.java:298, fresh. Its Callable is one of `$4-$6` (set note at row 25). Room dispatch unprinted, hence INFERRED. |
| 14 | `TagInfoDao_Impl.observeByTorrentId` `(Ljava/lang/String;)Lio/reactivex/Flowable;` | REACHABLE | INFERRED | Generated implementation of `TagInfoDao.observeByTorrentId` (TagInfoDao.java:55, fresh). Via TagRepositoryImpl.java:65, fresh; callers DetailTorrentViewModel.java:148, TorrentInfoProvider.java:219, fresh. Its Callable is one of `$4-$6` (set note at row 25). Room dispatch unprinted, hence INFERRED. |
| 15 | `TagInfoDao_Impl.update` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | INFERRED | Generated implementation of `TagInfoDao.update` (TagInfoDao.java:42, `@Update`, fresh). Via TagRepositoryImpl.java:45, fresh; caller AddTagViewModel.java:71, fresh. Room dispatch unprinted, hence INFERRED. |
| 16 | `TagInfoDao_Impl$1.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TagInfoDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Insertion adapter for TagInfo, constructed in the `_Impl` constructor. `TagInfoDao` inserts TagInfo only via `insert` (TagInfoDao.java:39, fresh). Runs on every insert (TagRepositoryImpl.java:40, fresh; caller AddTagViewModel.java:69, fresh). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 17 | `TagInfoDao_Impl$1.bind` `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | INFERRED | Binds a TagInfo on every insert (same route as row 16). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 18 | `TagInfoDao_Impl$1.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Returns the TagInfo INSERT SQL on every insert (same route as row 16). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 19 | `TagInfoDao_Impl$2.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TagInfoDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Deletion-or-update adapter for TagInfo (bind descriptor cannot distinguish the two: both bind TagInfo). Both operations are called via the repository — delete (TagRepositoryImpl.java:50, fresh; caller MainViewModel.java:187, fresh) and update (TagRepositoryImpl.java:45, fresh; caller AddTagViewModel.java:71, fresh) — so `$2` runs whichever adapter it is; a `$2`/`$3` swap (declaration-order vs canonical-order generation) changes NO label. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 20 | `TagInfoDao_Impl$2.bind` `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | INFERRED | Binds a TagInfo on every delete (row 19 route) or on every update (if `$2` is the update adapter) — either way it runs, per row 19. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 21 | `TagInfoDao_Impl$2.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Returns the TagInfo DELETE SQL (row 19 route) or UPDATE SQL (if `$2` is the update adapter) on every delete/update — either way it runs, per row 19. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 22 | `TagInfoDao_Impl$3.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TagInfoDao_Impl;Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Update-or-deletion adapter for TagInfo (mirror of row 19: whichever adapter `$2` is, `$3` is the other, and both operations are called). Runs on update and/or delete (routes at row 19). No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 23 | `TagInfoDao_Impl$3.bind` `(Landroidx/sqlite/db/SupportSQLiteStatement;Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;)V` | REACHABLE | INFERRED | Binds a TagInfo on every update (row 22 route) or on every delete (if `$3` is the deletion adapter) — either way it runs, per row 22. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 24 | `TagInfoDao_Impl$3.createQuery` `()Ljava/lang/String;` | REACHABLE | INFERRED | Returns the TagInfo UPDATE SQL (row 22 route) or DELETE SQL (if `$3` is the deletion adapter) on every update/delete — either way it runs, per row 22. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 25 | `TagInfoDao_Impl$4.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TagInfoDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | REACHABLE | INFERRED | Callable for a List-returning Rx query. Set note (applies to `$4-$6` rows 25-33): the three List-returning Rx methods are `observeAll` (TagInfoDao.java:51), `observeByTorrentId` (:55) and `getByTorrentIdAsync` (:59, `Single<List<TagInfo>>`) — all called via the repository with fresh callers (TagRepositoryImpl.java:60,65,70; MainViewModel.java:183, SelectTagViewModel.java:63, TorrentInfoProvider.java:298,219; DetailTorrentViewModel.java:148,144) — so every callable in the set is used, whichever `$N` maps to which method; the individual assignment (proposal lead order: `$4` = observeAll, `$5` = observeByTorrentId, `$6` = getByTorrentIdAsync) is NOT adopted as a label basis. `<init>` runs when the DAO method is called. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 26 | `TagInfoDao_Impl$4.call` `()Ljava/util/List;` | REACHABLE | INFERRED | Runs when the Flowable/Single from row 25's method is subscribed (Rx step INFERRED). No printed generated def. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 27 | `TagInfoDao_Impl$4.finalize` `()V` | REACHABLE | INFERRED | GC-only `finalize()` (as row 2; Callable created at row 25). Needs a project rule on `finalize()`; NOT `no_trigger_in_app`. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: enclosing Callable TagInfoDao_Impl$4.<init> (row 25) is REACHABLE INFERRED on the List-returning Rx repository set (TagRepositoryImpl.java fresh: observeAll :60, observeByTorrentId :65, getByTorrentIdAsync :70); fresh-corpus grep over all 7 fresh files for finalize = zero hits; core/storage/dao/ lists no *_Impl.java, so no generated Callable definition and no printed finalize override exists in the tree; the fw_src upload is a flat selection of framework files and contains no java/lang/Object.java, so no printed JVM finalization dispatch either. Label unchanged: still OPEN pending convention (vi) — the project rule on whether JVM GC dispatch counts as a trigger-graph route, or printed generated source showing the Callable overrides finalize, is the named close-out. NOT no_trigger_in_app (the Callable is created on a printed route); never flipped to UNREACHABLE without a saved full-repo grep covering generated code, and a grep over app source alone cannot rule out GC dispatch.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route, together with the 10-row finalize set (51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33, 53/29, 53/32). Enclosing Callable membership verified in the round-2 note above. No label change; NOT no_trigger_in_app.] [APPLIED 2026-11-01 D3b: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
| 28 | `TagInfoDao_Impl$5.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TagInfoDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | REACHABLE | INFERRED | Callable for a List-returning Rx query (set note at row 25; proposal lead order: observeByTorrentId). Created when TagRepositoryImpl.observeByTorrentId runs (TagRepositoryImpl.java:65, fresh; callers DetailTorrentViewModel.java:148, TorrentInfoProvider.java:219, fresh) under the lead order, and under any set assignment its method is called. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 29 | `TagInfoDao_Impl$5.call` `()Ljava/util/List;` | REACHABLE | INFERRED | Runs when the Flowable from row 28's method is subscribed (Rx step INFERRED). No printed generated def. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 30 | `TagInfoDao_Impl$5.finalize` `()V` | REACHABLE | INFERRED | GC-only `finalize()` (as row 2; Callable created at row 28). Needs a project rule on `finalize()`; NOT `no_trigger_in_app`. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: enclosing Callable TagInfoDao_Impl$5.<init> (row 28) is REACHABLE INFERRED on the List-returning Rx repository set (TagRepositoryImpl.java fresh: observeAll :60, observeByTorrentId :65, getByTorrentIdAsync :70); fresh-corpus grep over all 7 fresh files for finalize = zero hits; core/storage/dao/ lists no *_Impl.java, so no generated Callable definition and no printed finalize override exists in the tree; the fw_src upload is a flat selection of framework files and contains no java/lang/Object.java, so no printed JVM finalization dispatch either. Label unchanged: still OPEN pending convention (vi) — the project rule on whether JVM GC dispatch counts as a trigger-graph route, or printed generated source showing the Callable overrides finalize, is the named close-out. NOT no_trigger_in_app (the Callable is created on a printed route); never flipped to UNREACHABLE without a saved full-repo grep covering generated code, and a grep over app source alone cannot rule out GC dispatch.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route, together with the 10-row finalize set (51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33, 53/29, 53/32). Enclosing Callable membership verified in the round-2 note above. No label change; NOT no_trigger_in_app.] [APPLIED 2026-11-01 D3b: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
| 31 | `TagInfoDao_Impl$6.<init>` `(Lorg/proninyaroslav/libretorrent/core/storage/dao/TagInfoDao_Impl;Landroidx/room/RoomSQLiteQuery;)V` | REACHABLE | INFERRED | Callable for a List-returning Rx query (set note at row 25; proposal lead order: getByTorrentIdAsync). Created when TagRepositoryImpl.getByTorrentIdAsync runs (TagRepositoryImpl.java:70, fresh; caller DetailTorrentViewModel.java:144, fresh) under the lead order, and under any set assignment its method is called. No printed generated def; INFERRED. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 32 | `TagInfoDao_Impl$6.call` `()Ljava/util/List;` | REACHABLE | INFERRED | Runs when the Single from row 31's method is subscribed (Rx step INFERRED). No printed generated def. Reverts to OPEN under the batch-53 strict `$N` rule. |
| 33 | `TagInfoDao_Impl$6.finalize` `()V` | REACHABLE | INFERRED | GC-only `finalize()` (as row 2; Callable created at row 31). Needs a project rule on `finalize()`; NOT `no_trigger_in_app`. [RE-CHECK 2026-11-01: Fresh 2026-11-01 re-check: enclosing Callable TagInfoDao_Impl$6.<init> (row 31) is REACHABLE INFERRED on the List-returning Rx repository set (TagRepositoryImpl.java fresh: observeAll :60, observeByTorrentId :65, getByTorrentIdAsync :70); fresh-corpus grep over all 7 fresh files for finalize = zero hits; core/storage/dao/ lists no *_Impl.java, so no generated Callable definition and no printed finalize override exists in the tree; the fw_src upload is a flat selection of framework files and contains no java/lang/Object.java, so no printed JVM finalization dispatch either. Label unchanged: still OPEN pending convention (vi) — the project rule on whether JVM GC dispatch counts as a trigger-graph route, or printed generated source showing the Callable overrides finalize, is the named close-out. NOT no_trigger_in_app (the Callable is created on a printed route); never flipped to UNREACHABLE without a saved full-repo grep covering generated code, and a grep over app source alone cannot rule out GC dispatch.] [OPEN-CLOSE2 2026-11-01: CONDITIONAL — flips to REACHABLE INFERRED iff convention (vi) adopts JVM GC dispatch of finalize() as a trigger-graph route, together with the 10-row finalize set (51/18, 51/21, 51/24, 52/2, 52/5, 52/27, 52/30, 52/33, 53/29, 53/32). Enclosing Callable membership verified in the round-2 note above. No label change; NOT no_trigger_in_app.] [APPLIED 2026-11-01 D3b: OPEN → REACHABLE INFERRED per DECISIONS.md; build/C1 not run.] |
| 34 | `TorrentDao.<init>` `()V` | REACHABLE | INFERRED | Abstract-class constructor, invoked by the generated `TorrentDao_Impl.<init>` (row 36) when Room builds the DAO on first `torrentDao()` call. TorrentRepositoryImpl calls `db.torrentDao()` at lines 57,62,67,72,77,82,87,127,132,137, all fresh. Same treatment as batch-48 `AppDatabase.<init>` (per proposal). Generated subclass ctor unprinted, hence INFERRED. |
| 35 | `TorrentDao.replaceTags` `(Ljava/lang/String;Ljava/util/List;)V` | REACHABLE | SOURCE | Hand-written `@Transaction` body TorrentDao.java:67-70 (fresh): `deleteTagsByTorrentId(torrentId)` (:68) and `addTags(infoList)` (:69). Called at TorrentRepositoryImpl.java:127 (fresh) inside `replaceTags` (TorrentRepositoryImpl.java:122-128, fresh); repository caller TorrentSessionImpl.java:287 (`repo.replaceTags(torrent.id, params.tags)`), fresh. |
| 36 | `TorrentDao_Impl.<init>` `(Landroidx/room/RoomDatabase;)V` | REACHABLE | INFERRED | Generated subclass constructor, created when `torrentDao()` is first called (same TorrentRepositoryImpl call sites as row 34, fresh). Generated source not in the upload, hence INFERRED. |
| 37 | `TorrentDao_Impl.add` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;)V` | REACHABLE | INFERRED | Generated implementation of `TorrentDao.add` (TorrentDao.java:40, `@Insert`, fresh). Via TorrentRepositoryImpl.java:57, fresh; caller TorrentSessionImpl.java:285, fresh. Room dispatch unprinted, hence INFERRED. |
| 38 | `TorrentDao_Impl.addTag` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/TorrentTagInfo;)V` | REACHABLE | INFERRED | Generated implementation of `TorrentDao.addTag` (TorrentDao.java:73, `@Insert`, fresh). Via TorrentRepositoryImpl.java:132, fresh; caller DetailTorrentViewModel.java:152, fresh. Room dispatch unprinted, hence INFERRED. |
| 39 | `TorrentDao_Impl.addTags` `(Ljava/util/List;)V` | REACHABLE | INFERRED | Generated implementation of `TorrentDao.addTags` (TorrentDao.java:61, `@Insert`, fresh). Called by `TorrentDao.replaceTags` (TorrentDao.java:69, fresh) inside the row-35 route; no direct repository call is printed, and none is needed — the transaction route is the route. Room dispatch unprinted, hence INFERRED. |
| 40 | `TorrentDao_Impl.delete` `(Lorg/proninyaroslav/libretorrent/core/model/data/entity/Torrent;)V` | REACHABLE | INFERRED | Generated implementation of `TorrentDao.delete` (TorrentDao.java:46, `@Delete`, fresh). Via TorrentRepositoryImpl.java:67, fresh; callers TorrentSessionImpl.java:313,386 and TorrentDownloadImpl.java:777, fresh. Room dispatch unprinted, hence INFERRED. |

## Counts (mechanically verified — see generator)

- Judged: **40 / 40**. REACHABLE proposed: **34**. UNREACHABLE proposed: **0**.
  OPEN: **6**. confirmed_by: SOURCE 1 / INFERRED 33 (OPEN rows carry "-").
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
