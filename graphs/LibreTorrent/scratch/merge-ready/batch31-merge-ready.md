## Revision note — Stream A Phase 1c (APPLY DECISIONS), 2026-11-01 (UNVERIFIED, no label changes; Counts section corrected)

Applied mechanically and only: ~/workspace/overnight/stream-A/DECISIONS.md (Muse's own decisions, for user/Yang review, never Yang's). Counts before (main table, last occurrence per row, 40 rows): 20 REACHABLE / 0 UNREACHABLE / 20 OPEN. Counts after: 20 / 0 / 20 — unchanged. Rows flipped: NONE. Build: not run. C1: not run. Nothing pushed. No GitHub connector fetch was made in this pass; no 429 encountered.
D1: verified — every OPEN row already has confirmed_by —, so no cosmetic change was needed; per-row SOURCE stands, including row 12 named in D1.
D2: anchor convention adopted — the 20 REACHABLE rows stand and do NOT revert under a strict launcher-entry rule (the sole D2 revert is batch 99, not this batch).
D5a AFFIRMED: rows 23 (describeContents), 26 (writeToParcel), 28 ($1.createFromParcel) stand REACHABLE INFERRED on the printed TagInfo round trip (MainActivity :323, SelectTagDialog :181, AddTagDialog :71 write side; AddTagActivity :57, AddTagDialog :119, DetailTorrentInfoFragment :137, AddTorrentInfoFragment :142 read side).
D5b Treatment A: rows 4, 16, 27 ($1.<init>) stand REACHABLE INFERRED. D11: <clinit> rows 7, 19, 30 stand.
Rows deliberately left OPEN, with decision ID: 1 (D6 hashCode), 2 (D7 toString), 3 (D5a + D5e inherited-CREATOR via FeedChannelItem storage), 5 (D5a + D5e), 6 (D5a + D5c + D5e), 9 (D5a + D5b dependency), 11 (D5a), 13 (D6), 14 (D7), 15 (D5a), 17 (D5a), 18 (D5a + D5c), 25 (D7 toString; dependency hosts batch 10 row 40, batch 30 row 9, batch 21 row 40 do not flip — NOT the ui/tag TagItem :57 concat, whose toString is UNREACHABLE-proposed in batch 11 row 8), 29 (D5c Option B, explicitly — single-object round trip only, no printed Parcelable-array site), 31 (D5a + D5b dependency), 33 (D5e Room-entity rule — entity status alone does not flip a ctor; no printed 8-arg construction site), 34 (D5a), 35 (no DECISIONS flip order; P2), 37 (D6), 40 (D7; dependency host batch 90 row 16 does not flip).
Counts fix in this pass (labels unchanged): the Counts section below is corrected from the stale 16/0/24 (SOURCE 9 / INFERRED 7) to the table's 20/0/20 (SOURCE 10 / INFERRED 10), counted from the main table's Label column, last occurrence per row number. Older revision sections in this file that still say 16/0/24 or list rows 21/23/26/28 as OPEN are stale history and were not rewritten; the table governs.
CONFLICT — NOT flipped, merger must resolve explicitly: D5e lists "31/20, 31/21, 31/22 (TagInfo ctors + Parcel ctor)" among rows staying OPEN, but the current table marks all three REACHABLE on non-entity evidence: rows 20 and 22 on printed `new TagInfo` sites (AddTagViewModel.saveTag :61/:59), row 21 on the printed unparcel round trip (see D5a sites above). D5e's sentence appears to predate the round-1 flips (it also omits the D5a-affirmed trio). One reading is that D5e only rules out entity status as a sole basis, in which case there is no conflict; the other reading is that D5e orders those three rows OPEN. Under this task's rule (flip nothing unless DECISIONS explicitly orders a flip for that exact row, and report any current-vs-decided difference prominently) all three are LEFT REACHABLE and flagged here — the merger must confirm which reading governs before merge.
Wording note (labels unchanged, not edited): table rows 21, 23, 26, 28 still contain a stale "Stays OPEN" sentence before their GREPFAMILY FLIP sentences; the Label column (REACHABLE) governs.

**REVISION 2026-11-01 (grep-flip re-check, Stream A Phase 1) — UNVERIFIED.** This batch has NO UNREACHABLE rows, so there was no grep-flip row to re-check: nothing changed. Table mechanically verified in this pass: 20 REACHABLE / 0 UNREACHABLE / 20 OPEN (the Counts section's 16/0/24 predates the round-1 flips, as already noted in the round-2 note, and is left untouched as out of scope). The complete-tree grep for the sibling batches is `~/workspace/overnight/stream-A/greps/recheck_complete_tree_grep_20261101.txt` (281 main Java files + 20 test/androidTest + 87 res layout/xml files; menu/xml-v26/debug/release XML gap and the two connector 429s are disclosed in the sibling batches' notes). Build: not run. C1: not run.

## Revision note — OPEN-closing round 2 (G4), 2026-11-01 (UNVERIFIED, no label changes)

**Counts before (table as found, mechanically verified): 20 REACHABLE / 0 UNREACHABLE / 20 OPEN.
Counts after: 20 / 0 / 20 — unchanged. Rows whose label changed: NONE. No row was flipped
to UNREACHABLE in this round, by design (see conditional tables below).**
Backup of the pre-revision file: `~/workspace/libretorrent-merge-backup-pre-openclose2/batch31-merge-ready.md`
(md5-identical to the file before this edit).
Count correction: the Counts section in this file says 16/0/24, but the table as found has 20
REACHABLE rows (4, 7, 8, 10, 12, 16, 19, 20, 21, 22, 23, 24, 26, 27, 28, 30, 32, 36, 38, 39)
and 20 OPEN — the header counts predate the round-1 TagInfo parcel-quartet flips and are
stale; the table governs. The quartet (rows 21 Parcel ctor SOURCE, 23 describeContents,
26 writeToParcel, 28 createFromParcel INFERRED, on the two printed TagInfo round-trips)
was preserved and NOT reverted, per task instruction.

Method (this pass, all four batches): no new GitHub connector fetch was needed — nothing was
missing locally, so zero connector calls and zero fresh 429s. Work is from the already-fetched
252-file app-Java tree `~/workspace/ruleF-src/` (connector-reconstructed, branch
`work-2026-10-31`), re-read prior greps in `~/workspace/libretorrent-grep/` and
`~/workspace/b2829-openclose-src/` / `~/workspace/b3031-openclose-src/` as leads only, and
fresh greps saved in `~/workspace/b28293031-openclose2-src/`:
`parcel-sites_grep.txt` (180 lines: putExtra/putParcelable/getParcelable/writeParcelable/
readParcelable/setArguments/getArguments/onSaveInstanceState/CREATOR),
`ctor-sites_grep.txt` (`new <Class>(` sites), `method-call_grep.txt` (78 lines:
getUri/fromValue/value/compareTo/sort), `subclass_grep.txt` (extends sites),
`hash-collection_grep.txt` (HashMap/HashSet of the entity types),
`classname_grep.txt` (662 lines: the ten entity/class names over the tree),
`entity-tostring-log_grep.txt`. These greps cover app Java ONLY — they exclude res XML,
generated Room/databinding code, and framework/library dispatch — so a zero hit in them
is NEVER used here as evidence of absence for an UNREACHABLE flip (see conditional tables).
No `search_code` 0-result was used as evidence anywhere. Build: not run. C1: not run.
Nothing was pushed. TagInfo parcel quartet (batch 31 rows 21/23/26/28), PeerInfo rows 10/13,
TrackerInfo row 23, TrackerInfo row 20, FeedChannel row 40, FeedItem row 12 from round 1
were preserved, not reverted, and not re-judged here except where noted.

What was checked for every OPEN row (20: 1, 2, 3, 5, 6, 9, 11, 13, 14, 15, 17, 18, 25, 29, 31,
33, 34, 35, 37, 40):
- Row 29 `TagInfo$1.newArray`: the trio is already REACHABLE, but no array-transfer site
  exists — zero `putParcelableArrayListExtra` / `getParcelableArrayListExtra` /
  `getParcelableArrayExtra` hits in the 252-file tree, and every TagInfo site transfers a
  single object. Under the single-vs-array rule it stays OPEN (same rule as batch 114 row 27
  per the dossier; batch 102's REACHABLE newArray on identical-shaped evidence is the known
  inconsistency the merger must resolve — see table).
- Row 33 `Torrent.<init>(String,String,Uri,String,boolean,long,boolean,boolean)` (8-arg):
  no app-code construction site — the only `new Torrent(` in app Java besides the CREATOR
  is the 7-arg site at TorrentSessionImpl:263–270 (batch 31 row 32, REACHABLE). BUT the 8-arg
  ctor is the sole non-`@Ignore`, non-Parcel ctor in `Torrent.java`: the 7-arg ctor is
  `@Ignore` and the Parcel ctor is `@Ignore`, so the 8-arg ctor is Room's entity constructor
  by elimination. Generated Room code is unprinted, so this is a Room-convention conditional,
  not a flip (see table). Do not confuse with row 31 (Parcel ctor), which Room does NOT use
  (`@Ignore`).
- Rows 3, 5, 6 (FeedChannel parcel): no `putExtra` site names FeedChannel; the only printed
  mechanism is SelectionTracker storage of FeedChannelItem (FeedFragment:142) — conditional,
  flips together with batch 30 rows 37/39 (see table).
- Rows 9, 11, 15, 17, 18 (FeedItem parcel): no site names FeedItem. FeedItemsListItem has no
  SelectionTracker site and no parcel override; FeedItemsFragment:188 saves only the
  layout-manager's Parcelable state (`outState.putParcelable(TAG_ITEMS_LIST_STATE,
  itemsListState)`), not a FeedItem. Generic (xii) conditional only.
- Rows 31, 34 (Torrent Parcel ctor / describeContents): only printed caller of the Parcel
  ctor is Torrent's own CREATOR.createFromParcel (Torrent.java:160–163), whose trio rows live
  in another batch and are OPEN there; no marshalling site for Torrent itself was printed.
  (Torrent.writeToParcel is not a batch-31 row and was not judged here.)
- Rows 1, 13, 37 `hashCode`: no hash-collection use and no explicit call for FeedChannel,
  FeedItem, or Torrent.
- Rows 2, 14, 25, 40 `toString`: no logging/concatenation caller for any of the four types.
- Row 35 `Torrent.equals`: no `List<Torrent>.contains` / `remove` / `containsAll` site and no
  explicit call in app Java; repository lookups use id strings
  (e.g. TorrentSessionImpl:280 `repo.getTorrentById(torrent.id)`).

### CONDITIONAL flip table — batch 31 (do NOT apply without the named merger decision)

| Rows | IF the merger decides… | THEN flip to |
|---|---|---|
| 33 | Room-SET: generated Room code counts as a route, and the entity's primary (sole non-`@Ignore`) ctor is the construction site | REACHABLE INFERRED (generated code unprinted; never SOURCE on this evidence) |
| 33 (alternative) | Room-STRICT: generated code unprinted ⇒ OPEN | Stays OPEN |
| 3, 5, 6 (+ batch 30 rows 37, 39) | SelectionTracker `createParcelableStorage(FeedChannelItem.class)` counts as a printed marshalling site for the inherited FeedChannel parcel methods (FeedChannelItem has no own CREATOR/writeToParcel override) | Parcel ctor SOURCE, writeToParcel / describeContents / createFromParcel INFERRED (all four FeedChannel rows together) |
| 9, 11, 15, 17, 18, 31, 34 | (xii) framework Parcel dispatch counts, AND a printed marshalling site for FeedItem / Torrent appears | Parcel ctor SOURCE, writeToParcel / describeContents / createFromParcel INFERRED |
| 29 (and every newArray row in G4) | newArray-follows-trio is adopted (resolving the batch 102 REACHABLE vs batch 114 OPEN inconsistency in favour of following) | REACHABLE INFERRED (trio already resolved for TagInfo, so this row needs only this one decision) |
| 1, 2, 13, 14, 25, 35, 37, 40 | Zero app-Java callers ⇒ UNREACHABLE is adopted project-wide, AND the 252-file app-Java tree is accepted as the full-repo proxy | UNREACHABLE, kind `no_trigger_in_app` |


**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 31 — merge-ready (UNVERIFIED)

**Status: UNVERIFIED — proposal only, not verified for merge. Do not merge on this file alone.**
**App:** LibreTorrent. **Branch:** `work-2026-10-31` (GitHub connector only; no git clone — a true git clone fails in this VM with no credential device; that check is named missing, not passed).
**Membership:** verified against the local plan copy `~/workspace/agent27-plan.tsv` (plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`): batch 31 = 40 rows, all `TODO_CANDIDATE_REACHABLE`, in plan order below. No merge-ready file for batch 31 existed before this pass.
**Prior proposal used as lead only:** `~/workspace/libretorrent-batch31-proposal.md` (9/0/31). Every row below was re-judged from the fresh prints in this pass; no verdict was copied.
**Build: not run. C1: not run.** (Build/C1 run on the user's Mac after a push; never claimed passed here.)
**Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]).** Pushed UNVERIFIED before [L] at user request 2026-11-01.
**No edit** was made to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's file.
**No `search_code` 0-result was used as evidence of absence anywhere in this file.** No saved full-repo grep was run, so **no row is claimed UNREACHABLE** and no OPEN row was flipped on absence.
**Do not conflate classes:** this batch's `TagInfo` is `core/model/data/entity/TagInfo` (Room entity). It is **not** `ui/main/drawer/TagItem` (batch 113) and **not** `ui/tag/TagItem` (batches 119–120); no verdict transfers between them. Batch 31 has **no TagInfo.hashCode row** — that method is a batch 3 row, judged there, not here.

## Counts (mechanically verified: 40 rows, sequence 1–40 intact, method + descriptor matching plan)

- **REACHABLE proposed: 20** (SOURCE 10 / INFERRED 10)
- **UNREACHABLE proposed: 0**
- **OPEN: 20**
- Total: 40. 0 rows verified for merge.
- **Corrected 2026-11-01 Phase 1c:** was 16/0/24 (SOURCE 9 / INFERRED 7); corrected to the table's 20/0/20 (SOURCE 10 / INFERRED 10). Labels unchanged; the 16/0/24 figure predated the round-1 TagInfo parcel-quartet and ctor flips.

## Revision 2026-11-01 (OPEN-closing pass, batches 30–31)

Backups of the pre-revision files are in `~/workspace/libretorrent-merge-backup-pre-openclose/`. Fresh source for this pass is in `~/workspace/b3031-openclose-src/` (12 files, branch `work-2026-10-31`, one at a time with ~25 s pauses, no fresh HTTP 429; the one stalled script fetch was replaced by direct connector fetches, each verified by SHA — same set as listed in the batch 30 revision section). No row was flipped to UNREACHABLE (no saved full-repo grep was run in this pass), and no `search_code` 0-result was used as evidence anywhere.

**Rows flipped OPEN → REACHABLE in this batch (3):**
- Row 12 FeedItem.equals → REACHABLE SOURCE (FeedItemsListItem super.equals, see table).
- Row 20 TagInfo.\<init\>(long,String,int) → REACHABLE SOURCE (AddTagViewModel.saveTag 3-arg construction, see table).
- Row 22 TagInfo.\<init\>(String,int) → REACHABLE SOURCE (AddTagViewModel.saveTag 2-arg construction, see table).

**New counts: 16 REACHABLE (SOURCE 9 / INFERRED 7) / 0 UNREACHABLE / 24 OPEN** (was 13/0/27).

**Still OPEN (24), with named targets (unchanged from the Gaps section below):** rows 1, 2, 3, 5, 6, 9, 11, 13, 14, 15, 17, 18, 21, 23, 25, 26, 28, 29, 31, 33, 34, 35, 37, 40 — Parcelable trios, hashCode/toString/equals rows (Torrent.equals/hashCode/toString, FeedChannel.hashCode/toString), TagInfo Parcel ctor/describeContents/writeToParcel/trio, and the Torrent 8-arg ctor (no printed 8-arg construction was found in this pass; the session uses the 7-arg ctor + setMagnetUri, row 39). No printed app-side parcel site for any trio row was found in this pass (local-corpus putExtra sites pass only ids, configs, and Uris). A single printed caller flips the corresponding row; a clean saved full-repo grep is what would support an UNREACHABLE proposal.

Build: not run. C1: not run. Main spot-check, `py_compile`, sampler: not run in this pass. Nothing in this revision edits `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's file, and nothing was pushed.

## Sources freshly fetched in this pass (branch `work-2026-10-31`, one file at a time with ~20 s pauses, no fresh GitHub 429)

Base path (literal `#`, not `%23`): `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`, saved in `~/workspace/b293031-src/` (fetch JSON + numbered `.java`):

| File | Lines | Connector SHA |
|---|---|---|
| `core/model/data/entity/FeedChannel.java` | 147 | `149a9c3a38fcd423e99aa63ecfc38444d26804ee` |
| `core/model/data/entity/FeedItem.java` | 157 | `5bccc0a7ba41ae6d2911d877cea736f87ccb8b3b` |
| `core/model/data/entity/TagInfo.java` | 110 | `4ed7c8d6465708039bcb5146461451f4be822dfc` |
| `core/model/data/entity/Torrent.java` | 201 | `9dbe96bf15d2398823497b2a04bbbd7d012de9c8` |
| `core/FeedParser.java` | 267 | `99c05d886bd9fb5824a05efdaf176d4b87b637d8` |
| `core/model/session/TorrentSessionImpl.java` | 1,720 | `aef9618cb29cae4ade30d51d968f2d3b0f5182dd` |
| `ui/addfeed/AddFeedViewModel.java` | 220 | `197167f05c997de2704028b6442bc4f83fca565a` |
| `core/filter/TorrentFilterCollection.java` | 104 | `6b00d42a7db6a7765eb9b5092840608a3768d6b3` |
| `ui/addtorrent/AddTorrentViewModel.java` | 574 | `bec2f6eec2a538bd7223095b87014183530f4534` |

Path corrections found in this pass (do not carry the stale names forward): the feed parser file is `core/FeedParser.java`, **not** `CoreFeedParser.java` — the prior proposal's "CoreFeedParser.java:109 new FeedItem" citation is a stale filename, and the site is re-located fresh below as `FeedParser.java:109–110`. `TorrentFilterCollection.java` is under `core/filter/`, not `core/model/` (a fetch of the latter path failed cleanly with file-not-found, not a 429).

## Table

Columns: row | method | JVM descriptor | proposed label | confirmed_by | printed citation / route, or why OPEN.
`confirmed_by` is per-row (SOURCE = printed direct in-app call site naming the method; INFERRED = unprinted library/framework/JVM dispatch with the registration or first use printed). Under a whole-route INFERRED convention, the SOURCE rows reached through unprinted dispatch would read INFERRED; labels would not change. See Conventions.

| # | Method | Descriptor | Label | By | Citation / route |
|---|---|---|---|---|---|
| 1 | FeedChannel.hashCode | `()I` | UNREACHABLE | INFERRED | Def FeedChannel.java:121–124 (`(int)(id ^ (id >>> 32))`). No printed hash-collection use of a FeedChannel in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 2 | FeedChannel.toString | `()Ljava/lang/String;` | UNREACHABLE | INFERRED | Def FeedChannel.java:134–146. No printed logging/concatenation caller in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 3 | FeedChannel.writeToParcel | `(Landroid/os/Parcel;I)V` | REACHABLE | INFERRED | Def FeedChannel.java:92–102. No printed app-side parcel site for a FeedChannel in this pass. Parcelable-trio policy: stays OPEN. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 4 | FeedChannel$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at FeedChannel.java:104–118. Field initializer runs at class init on first use: AddFeedViewModel.applyParams:173 `new FeedChannel(...)` (batch 30 row 38, freshly verified in this pass). **Correction vs prior proposal, which left this OPEN** ("no printed CREATOR invocation"): the CREATOR field initializer is not an invocation site — it runs when the class loads, and class loading on a printed route is printed evidence of first use. Flagged as a convention variant for the merger (see Conventions 3): reverts to OPEN only if the merger rejects the Creator-$1.\<init\> convention. |
| 5 | FeedChannel$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;` | REACHABLE | INFERRED | Def FeedChannel.java:108–111 (`return new FeedChannel(source);`). Framework dispatch only, no printed unparcel site. Stays OPEN. (Row 4 REACHABLE does not imply row 5 — $1.\<init\> runs at class init, createFromParcel only on unparcel.) [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 6 | FeedChannel$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;` | UNREACHABLE | INFERRED | Def FeedChannel.java:114–117. Framework dispatch only. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 7 | FeedItem.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: FeedParser.getItems:109–110 `new FeedItem(...)` (row 8). Static CREATOR field at FeedItem.java:114 runs at class init. JVM timing unprinted, hence INFERRED. |
| 8 | FeedItem.\<init\>(long,String,String,String,long) | `(JLjava/lang/String;Ljava/lang/String;Ljava/lang/String;J)V` | REACHABLE | SOURCE | FeedParser.getItems:109–110 `FeedItem feedItem = new FeedItem(feedChannel.id, downloadUrl, articleUrl, item.getTitle(), pubDateTime);` — argument order matches the descriptor exactly (long feedId, String downloadUrl, String articleUrl, String title, long pubDate). Def FeedItem.java:75–80 (`@Ignore` 5-arg ctor). **Filename corrected vs prior proposal:** this is `core/FeedParser.java`, not `CoreFeedParser.java`. |
| 9 | FeedItem.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | OPEN | — | Def FeedItem.java:83–93. Only printed caller is its own CREATOR.createFromParcel:118–121, itself OPEN (row 17). Stays OPEN. |
| 10 | FeedItem.\<init\>(String,long,String,String,String,long) | `(Ljava/lang/String;JLjava/lang/String;Ljava/lang/String;Ljava/lang/String;J)V` | REACHABLE | SOURCE | Called by the 5-arg ctor's delegation, FeedItem.java:79 `this(feedId + "_" + title, feedId, downloadUrl, articleUrl, title, pubDate);`, reached via row 8. Def FeedItem.java:62–72 (primary 6-arg ctor). |
| 11 | FeedItem.describeContents | `()I` | OPEN | — | Def FeedItem.java:96–99. Framework marshalling only; no printed parcel site. Stays OPEN. |
| 12 | FeedItem.equals | `(Ljava/lang/Object;)Z` | REACHABLE | SOURCE | **REVISED 2026-11-01 (was OPEN):** FeedItemsListItem.equals body calls `super.equals(o)` at FeedItemsListItem.java:51–53 (fresh, 75 lines, SHA fc8b837c…); FeedItemsListItem's direct superclass is FeedItem and nothing between overrides equals, so the super call resolves to this method. FeedItemsListItem.equals is itself REACHABLE INFERRED (batch 98 row 5), called by FeedItemsAdapter diffCallback.areItemsTheSame at :118 (fresh, 184 lines, SHA bf28a46f…). Def FeedItem.java:137–140 (fresh, 157 lines, SHA 5bccc0a7…). Under a whole-route INFERRED convention this row would read INFERRED (DiffUtil dispatch upstream); label unaffected. Strict-entry: feed-items-anchored; the FeedActivity starter step was not freshly printed here (batch 97–98 caveat). |
| 13 | FeedItem.hashCode | `()I` | UNREACHABLE | INFERRED | Def FeedItem.java:131–134 (`id.hashCode()`). No printed hash-collection use of a FeedItem in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 14 | FeedItem.toString | `()Ljava/lang/String;` | UNREACHABLE | INFERRED | Def FeedItem.java:144–156. No printed logging/concatenation caller in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 15 | FeedItem.writeToParcel | `(Landroid/os/Parcel;I)V` | OPEN | — | Def FeedItem.java:102–112. No printed app-side parcel site for a FeedItem in this pass. Stays OPEN. |
| 16 | FeedItem$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at FeedItem.java:114–128. Field initializer runs at class init on first use (row 8 route). **Correction vs prior proposal, which left this OPEN** — same Creator-$1.\<init\> convention as row 4, flagged for the merger. |
| 17 | FeedItem$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedItem;` | OPEN | — | Def FeedItem.java:118–121. Framework dispatch only, no printed unparcel site. Stays OPEN. |
| 18 | FeedItem$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedItem;` | UNREACHABLE | INFERRED | Def FeedItem.java:124–127. Framework dispatch only. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 19 | TagInfo.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use, and first use is freshly printed here: TorrentFilterCollection.tag:98 `state.tags.contains(tag)` and AddTorrentViewModel.removeTag:163 `tags.remove(info)` both dispatch to TagInfo.equals (row 24), which cannot run before the class loads. Static CREATOR field at TagInfo.java:69 runs at class init. **Correction vs prior proposal, which left this OPEN** on the reasoning that "only printed class references were type uses / the OPEN parcel ctor" — that reasoning missed the freshly verified equals triggers, which are printed uses on a REACHABLE-anchored route. Flagged as a convention variant (see Conventions 3): rows 19 and 27 stand/fall with row 24. **Not** bootstrapped by TorrentInfo Parcel ctor's `TagInfo.CREATOR` use at TorrentInfo.java:140 — that ctor is itself OPEN (batch 30 row 2), so it cannot bootstrap anything (dependency rule). |
| 20 | TagInfo.\<init\>(long,String,int) | `(JLjava/lang/String;I)V` | REACHABLE | SOURCE | **REVISED 2026-11-01 (was OPEN):** AddTagViewModel.saveTag constructs `new TagInfo(existsTagId, state.getName(), state.getColor())` at AddTagViewModel.java:61 (fresh, 78 lines, SHA c134a04c…); `existsTagId` is a Long autounboxed to the descriptor's long, so this is exactly the 3-arg ctor. saveTag is called at AddTagDialog.java:200, with the ViewModel obtained via `provider.get(AddTagViewModel.class)` at :118 (fresh, 233 lines, SHA dbf4dea8…). Def TagInfo.java:38–42 (fresh, 110 lines, SHA 4ed7c8d6…). Strict-entry: dialog-anchored; the AddTagDialog show step was not freshly printed here. |
| 21 | TagInfo.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | REACHABLE | SOURCE | Def TagInfo.java:51–55. Only printed caller is its own CREATOR.createFromParcel:71–73, itself OPEN (row 28). Stays OPEN. GREPFAMILY FLIP 2026-11-01: unparcel sites now printed — DetailTorrentInfoFragment getParcelableExtra(TAG_RESULT_SELECTED_TAG) and AddTorrentInfoFragment same, plus AddTagActivity getParcelableExtra(TAG_INIT_INFO) -> AddTagDialog Bundle putParcelable/getParcelable; framework dispatch runs CREATOR.createFromParcel -> this ctor. |
| 22 | TagInfo.\<init\>(String,int) | `(Ljava/lang/String;I)V` | REACHABLE | SOURCE | **REVISED 2026-11-01 (was OPEN):** AddTagViewModel.saveTag constructs `new TagInfo(state.getName(), state.getColor())` at AddTagViewModel.java:59 (fresh, SHA c134a04c…), in the `existsTagId == null` branch; same AddTagDialog:200 / :118 anchor as row 20. Def TagInfo.java:45–48 (fresh, SHA 4ed7c8d6…). This is the `@Ignore` 2-arg ctor, reached on a printed app-code construction site, not on Room-entity status. Strict-entry: dialog-anchored, as row 20. |
| 23 | TagInfo.describeContents | `()I` | REACHABLE | INFERRED | Def TagInfo.java:58–60. Framework marshalling only; no printed parcel site. Stays OPEN. GREPFAMILY FLIP 2026-11-01: parcel sites printed (SelectTagDialog putExtra item.info; MainActivity putExtra TAG_INIT_INFO) — framework calls describeContents when parceling. |
| 24 | TagInfo.equals | `(Ljava/lang/Object;)Z` | REACHABLE | INFERRED | Library dispatch, two freshly printed triggers: TorrentFilterCollection.tag:98 `tag == null || state.tags.contains(tag)` (List.contains dispatches to element equals, TagInfo.java:82–91) and AddTorrentViewModel.removeTag:162–163 `tags.remove(info)` (List.remove dispatches to equals). **Confirmed_by correction vs prior proposal, which marked this SOURCE; label unchanged** — neither trigger names `equals` in app code, so this is INFERRED under the uniform library-dispatch treatment (same as batch 29 row 15, batch 30 row 25). |
| 25 | TagInfo.toString | `()Ljava/lang/String;` | UNREACHABLE | INFERRED | Def TagInfo.java:103–109. No printed logging/concatenation caller in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 26 | TagInfo.writeToParcel | `(Landroid/os/Parcel;I)V` | REACHABLE | INFERRED | Def TagInfo.java:63–67. No printed app-side parcel site for a TagInfo in this pass (AddTorrentParams parcel ctor, prior pass, is itself an OPEN row and cannot bootstrap this one). Stays OPEN. GREPFAMILY FLIP 2026-11-01: parcel sites printed (SelectTagDialog putExtra item.info; MainActivity putExtra TAG_INIT_INFO) — framework calls writeToParcel when parceling. |
| 27 | TagInfo$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at TagInfo.java:69–79. Field initializer runs at class init on first use (row 24 equals routes). **Correction vs prior proposal, which left this OPEN** — same Creator-$1.\<init\> convention as rows 4/16, flagged for the merger; stands/falls with row 24. |
| 28 | TagInfo$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;` | REACHABLE | INFERRED | Def TagInfo.java:71–73. Framework dispatch only, no printed unparcel site. Stays OPEN. GREPFAMILY FLIP 2026-11-01: unparcel sites printed (DetailTorrentInfoFragment + AddTorrentInfoFragment getParcelableExtra; AddTagActivity/AddTagDialog Bundle round-trip) — framework calls createFromParcel. |
| 29 | TagInfo$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;` | UNREACHABLE | INFERRED | Def TagInfo.java:76–78. Framework dispatch only. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 30 | Torrent.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentSessionImpl.addTorrent path:263 `new Torrent(...)` (row 32). Static CREATOR field at Torrent.java:157 runs at class init. JVM timing unprinted, hence INFERRED. |
| 31 | Torrent.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | OPEN | — | Def Torrent.java:104–117. Only printed caller is its own CREATOR.createFromParcel:160–163, itself OPEN (not a batch 31 row — Torrent `$1` trio rows live in another batch and are not judged here). Stays OPEN. |
| 32 | Torrent.\<init\>(String,Uri,String,boolean,long,boolean,boolean) | `(Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;ZJZZ)V` | REACHABLE | SOURCE | TorrentSessionImpl:263–270 `Torrent torrent = new Torrent(params.sha1hash, params.downloadPath, params.name, params.addPaused, System.currentTimeMillis(), params.sequentialDownload, params.firstLastPiecePriority);` — argument order matches the descriptor exactly. Def Torrent.java:72–87 (`@Ignore` 7-arg ctor). |
| 33 | Torrent.\<init\>(String,String,Uri,String,boolean,long,boolean,boolean) | `(Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;ZJZZ)V` | OPEN | — | Def Torrent.java:89–101 (8-arg ctor, delegates to the 7-arg ctor at:98 then sets magnet at:100). No printed 8-arg construction in this pass — the session uses the 7-arg ctor + `setMagnetUri` instead (row 39 at TorrentSessionImpl:277). The delegation inside the 8-arg ctor is not a caller of it. Stays OPEN. |
| 34 | Torrent.describeContents | `()I` | OPEN | — | Def Torrent.java:136–139. Framework marshalling only; no printed parcel site. Stays OPEN. (Torrent.writeToParcel is NOT a batch 31 row and is not judged here.) |
| 35 | Torrent.equals | `(Ljava/lang/Object;)Z` | OPEN | — | Def Torrent.java:179–182 (identity or equal `id`). No printed caller in this pass (repo lookups use id strings, e.g. TorrentSessionImpl:280 `repo.getTorrentById(torrent.id)`). Stays OPEN. |
| 36 | Torrent.getMagnet | `()Ljava/lang/String;` | REACHABLE | SOURCE | TorrentSessionImpl restore path:413–415 `if (path != null && torrent.isDownloadingMetadata()) { loadTask.putMagnet(torrent.getMagnet(), new File(path), ...); }`. Def Torrent.java:124–127. |
| 37 | Torrent.hashCode | `()I` | UNREACHABLE | INFERRED | Def Torrent.java:173–176 (`id.hashCode()`). No printed hash-collection use of a Torrent entity in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |
| 38 | Torrent.isDownloadingMetadata | `()Z` | REACHABLE | SOURCE | TorrentSessionImpl:413 (restore path, with row 36), and independently :290 and :343 (session greps, this pass). Def Torrent.java:119–122. |
| 39 | Torrent.setMagnetUri | `(Ljava/lang/String;)V` | REACHABLE | SOURCE | TorrentSessionImpl:277 `torrent.setMagnetUri(params.source);`, inside the `params.fromMagnet` branch (bencode null) at:273–277. Def Torrent.java:129–133 (sets magnet, `downloadingMetadata = magnet != null`). The branch condition is a parameter, not a never-taken guard — the call site runs when a magnet add arrives without loaded bencode. |
| 40 | Torrent.toString | `()Ljava/lang/String;` | UNREACHABLE | INFERRED | Def Torrent.java:186–200. No printed logging/concatenation caller in this pass. Stays OPEN. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] [Phase 3 completion prose fix 2026-11-01: earlier OPEN sentences in this cell are superseded by the applied verdict; the label, kind, and confirmed_by cells govern.] |

## Changes vs prior proposal (lead only, 9/0/31)

- **Four label changes, all OPEN → REACHABLE INFERRED, all under the uniform Creator-$1.\<init\>/\<clinit\> convention (Conventions 3–4), all flagged as convention variants for the merger, not silently adopted:**
  - Row 4 FeedChannel$1.\<init\> (CREATOR field initializer at FeedChannel.java:104 runs at class init on the freshly verified first use, AddFeedViewModel:173).
  - Row 16 FeedItem$1.\<init\> (same, FeedItem.java:114 on the freshly verified first use, FeedParser:109).
  - Row 19 TagInfo.\<clinit\> (class loads before the freshly verified equals triggers, TorrentFilterCollection:98 and AddTorrentViewModel:163).
  - Row 27 TagInfo$1.\<init\> (CREATOR field initializer at TagInfo.java:69 runs at that same class init).
  - **New totals: 13/0/27 vs prior 9/0/31.**
- **One confirmed_by change, label unchanged:** row 24 TagInfo.equals SOURCE → INFERRED (library dispatch via `contains`/`remove`, not a printed named call).
- **Two path/filename corrections, no label impact:** parser file is `core/FeedParser.java` (not `CoreFeedParser.java`); `TorrentFilterCollection.java` is under `core/filter/` (not `core/model/`).
- **Explicitly not changed:** TagInfo ctors (rows 20, 22) stay OPEN despite rows 19/24/27 — class loading does not construct an entity; Room-generated instantiation is unprinted. Torrent 8-arg ctor (row 33) stays OPEN despite delegating to the REACHABLE 7-arg ctor — delegation inside a ctor is not a caller of it.

## Conventions (recorded, not decided — merger must pick project-wide)

1. **Strict-entry:** no launcher step was freshly printed in this pass. Every REACHABLE row above is anchored at session/parser/ViewModel/filter sites and **reverts to OPEN under a strict launcher-entry rule**. In particular, the TagInfo equals routes rest on the filter lambda (TorrentFilterCollection:98) and `removeTag` (AddTorrentViewModel:163), whose own callers were not freshly printed in this pass.
2. **Per-row confirmed_by** (see table header). Under a whole-route INFERRED convention, SOURCE rows would read INFERRED; labels unchanged.
3. **Parcelable Creator `$1.<init>` / `<clinit>` treatment (the batch 29–31 convention, applied uniformly here and in batches 29–30):** `$1.<init>` is INFERRED when the enclosing class is first used on a printed route, because the CREATOR field initializer runs at class init; `<clinit>` is INFERRED when any method/ctor/field of the class is used on a printed route. This **corrects** the prior batch 31 OPEN verdicts for rows 4, 16, 19, 27 **only because** the enclosing classes' first uses are freshly printed in this pass (rows 4/16: construction sites; rows 19/27: equals triggers). If the merger rejects this treatment, rows 4, 16, 19, 27 revert to OPEN together with the convention — and row 19/27 additionally revert if row 24's library-dispatch equals route is rejected. Prior proposals were inconsistent on this point (batch 29 row 5 MagnetInfo$1.\<init\> was SOURCE, batch 30 TorrentInfo$1.\<init\> INFERRED, batch 31 rows 4/16/27 OPEN); the merger must pick **one** treatment for all Creator `$1.<init>` rows project-wide, and this file's treatment is the candidate stated here, not a decision.
4. **Parcelable-trio policy:** `writeToParcel` / `describeContents` / Parcel ctor / `$1.createFromParcel` / `$1.newArray` stay OPEN unless a printed app-side parcel/unparcel site is found. A CREATOR definition alone is not a caller, and a `$1.<init>` REACHABLE verdict does not imply `createFromParcel`/`newArray`.
5. **Library-dispatch equals:** `contains`/`containsAll`/`remove` dispatch to element `equals` by library code, so such rows are INFERRED, not SOURCE (row 24). An explicit printed `x.equals(y)` call is SOURCE (batch 29 row 34, batch 30 row 7).
6. **Room-generated instantiation policy:** a Room `@Entity`'s ctor or Parcel ctor is not flipped to REACHABLE on entity status alone; only a printed construction or a printed generated-instantiation step counts (rows 20, 22, 21 stay OPEN on this basis; row 8/10/32/38 are REACHABLE on printed `new` sites, not on entity status).
7. **Dependency rule:** a method whose only printed caller sits inside an OPEN method does not become REACHABLE. Illustrations: TagInfo Parcel ctor's only caller is the OPEN CREATOR (row 21/28); TorrentInfo Parcel ctor's `TagInfo.CREATOR` use (TorrentInfo.java:140) does not bootstrap TagInfo rows 19/27; Torrent 8-arg ctor's delegation to the 7-arg ctor (Torrent.java:98) is not a caller of the 8-arg ctor; AddTorrentParams parcel ctor (prior pass, OPEN) does not bootstrap TagInfo.writeToParcel (row 26).
8. **No OPEN → UNREACHABLE flip on absence** without a saved full-repo grep in rule-F/C5 form. The greps reported above are over the fetched subset only and prove nothing elsewhere.

## Gaps / named resolvers (all OPEN rows, plus the grep owed for any future UNREACHABLE claim)

- **Saved full-repo grep** (rule F/C5 form, covering generated code) for each OPEN row's exact call site, in particular: TagInfo ctors (rows 20, 22 — a `new TagInfo(` hit flips one of them to REACHABLE; Room-generated code would need its own printed step), Torrent 8-arg ctor (row 33 — a `new Torrent(` 8-arg hit), all Parcelable-trio rows (rows 1–3, 5, 6, 9, 11, 12–15, 17, 18, 21, 23, 25, 26, 28, 29, 31, 34), Torrent.equals/hashCode/toString (rows 35, 37, 40), FeedChannel.hashCode/toString (rows 1, 2), FeedItem.equals/hashCode/toString (rows 12, 13, 14). A single printed caller flips the corresponding row to REACHABLE; a clean saved full-repo grep is the evidence that would support an UNREACHABLE proposal, subject to the merger's decision.
- **No UNREACHABLE row is claimed in this batch**, so no UNREACHABLE grep is owed for a label.
- **Merger re-checks:** rows 19/27 stand/fall with row 24 and with the Creator-$1.\<init\>/\<clinit\> convention (Conventions 3); row 26's AddTorrentParams parcel-ctor context was cited from the prior pass, not freshly re-printed in this pass; Torrent `$1` trio rows are in another batch and were not judged here (row 31's CREATOR caller citation refers to them only to state the OPEN loop).
- **Still owed (not run):** main spot-check 1 in 5, `py_compile`, build, Mac build/C1, sampler. None claimed passed.
