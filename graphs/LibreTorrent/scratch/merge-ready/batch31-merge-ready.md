# LibreTorrent batch 31 — merge-ready (UNVERIFIED)

**Status: UNVERIFIED — proposal only, not verified for merge. Do not merge on this file alone.**
**App:** LibreTorrent. **Branch:** `work-2026-10-31` (GitHub connector only; no git clone — a true git clone fails in this VM with no credential device; that check is named missing, not passed).
**Membership:** verified against the local plan copy `~/workspace/agent27-plan.tsv` (plan SHA `0104806dd666c840049b3db52823d4b384fa1c92`): batch 31 = 40 rows, all `TODO_CANDIDATE_REACHABLE`, in plan order below. No merge-ready file for batch 31 existed before this pass.
**Prior proposal used as lead only:** `~/workspace/libretorrent-batch31-proposal.md` (9/0/31). Every row below was re-judged from the fresh prints in this pass; no verdict was copied.
**Build: not run. C1: not run.** (Build/C1 run on the user's Mac after a push; never claimed passed here.)
**No push.** Pushes are held until verified and merged to `[L]`.
**No edit** was made to `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's file.
**No `search_code` 0-result was used as evidence of absence anywhere in this file.** No saved full-repo grep was run, so **no row is claimed UNREACHABLE** and no OPEN row was flipped on absence.
**Do not conflate classes:** this batch's `TagInfo` is `core/model/data/entity/TagInfo` (Room entity). It is **not** `ui/main/drawer/TagItem` (batch 113) and **not** `ui/tag/TagItem` (batches 119–120); no verdict transfers between them. Batch 31 has **no TagInfo.hashCode row** — that method is a batch 3 row, judged there, not here.

## Counts (mechanically verified: 40 rows, sequence 1–40 intact, method + descriptor matching plan)

- **REACHABLE proposed: 13** (SOURCE 6 / INFERRED 7)
- **UNREACHABLE proposed: 0**
- **OPEN: 27**
- Total: 40. 0 rows verified for merge.

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
| 1 | FeedChannel.hashCode | `()I` | OPEN | — | Def FeedChannel.java:121–124 (`(int)(id ^ (id >>> 32))`). No printed hash-collection use of a FeedChannel in this pass. Stays OPEN. |
| 2 | FeedChannel.toString | `()Ljava/lang/String;` | OPEN | — | Def FeedChannel.java:134–146. No printed logging/concatenation caller in this pass. Stays OPEN. |
| 3 | FeedChannel.writeToParcel | `(Landroid/os/Parcel;I)V` | OPEN | — | Def FeedChannel.java:92–102. No printed app-side parcel site for a FeedChannel in this pass. Parcelable-trio policy: stays OPEN. |
| 4 | FeedChannel$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at FeedChannel.java:104–118. Field initializer runs at class init on first use: AddFeedViewModel.applyParams:173 `new FeedChannel(...)` (batch 30 row 38, freshly verified in this pass). **Correction vs prior proposal, which left this OPEN** ("no printed CREATOR invocation"): the CREATOR field initializer is not an invocation site — it runs when the class loads, and class loading on a printed route is printed evidence of first use. Flagged as a convention variant for the merger (see Conventions 3): reverts to OPEN only if the merger rejects the Creator-$1.\<init\> convention. |
| 5 | FeedChannel$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;` | OPEN | — | Def FeedChannel.java:108–111 (`return new FeedChannel(source);`). Framework dispatch only, no printed unparcel site. Stays OPEN. (Row 4 REACHABLE does not imply row 5 — $1.\<init\> runs at class init, createFromParcel only on unparcel.) |
| 6 | FeedChannel$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedChannel;` | OPEN | — | Def FeedChannel.java:114–117. Framework dispatch only. Stays OPEN. |
| 7 | FeedItem.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: FeedParser.getItems:109–110 `new FeedItem(...)` (row 8). Static CREATOR field at FeedItem.java:114 runs at class init. JVM timing unprinted, hence INFERRED. |
| 8 | FeedItem.\<init\>(long,String,String,String,long) | `(JLjava/lang/String;Ljava/lang/String;Ljava/lang/String;J)V` | REACHABLE | SOURCE | FeedParser.getItems:109–110 `FeedItem feedItem = new FeedItem(feedChannel.id, downloadUrl, articleUrl, item.getTitle(), pubDateTime);` — argument order matches the descriptor exactly (long feedId, String downloadUrl, String articleUrl, String title, long pubDate). Def FeedItem.java:75–80 (`@Ignore` 5-arg ctor). **Filename corrected vs prior proposal:** this is `core/FeedParser.java`, not `CoreFeedParser.java`. |
| 9 | FeedItem.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | OPEN | — | Def FeedItem.java:83–93. Only printed caller is its own CREATOR.createFromParcel:118–121, itself OPEN (row 17). Stays OPEN. |
| 10 | FeedItem.\<init\>(String,long,String,String,String,long) | `(Ljava/lang/String;JLjava/lang/String;Ljava/lang/String;Ljava/lang/String;J)V` | REACHABLE | SOURCE | Called by the 5-arg ctor's delegation, FeedItem.java:79 `this(feedId + "_" + title, feedId, downloadUrl, articleUrl, title, pubDate);`, reached via row 8. Def FeedItem.java:62–72 (primary 6-arg ctor). |
| 11 | FeedItem.describeContents | `()I` | OPEN | — | Def FeedItem.java:96–99. Framework marshalling only; no printed parcel site. Stays OPEN. |
| 12 | FeedItem.equals | `(Ljava/lang/Object;)Z` | OPEN | — | Def FeedItem.java:137–140 (identity or equal `id`). No printed `equals`/`contains` call on a FeedItem in this pass (the prior pass's FeedFetcherWorker filtering uses item id/title fields, not equals). Printed-subset check only, not a full-repo grep: stays OPEN. |
| 13 | FeedItem.hashCode | `()I` | OPEN | — | Def FeedItem.java:131–134 (`id.hashCode()`). No printed hash-collection use of a FeedItem in this pass. Stays OPEN. |
| 14 | FeedItem.toString | `()Ljava/lang/String;` | OPEN | — | Def FeedItem.java:144–156. No printed logging/concatenation caller in this pass. Stays OPEN. |
| 15 | FeedItem.writeToParcel | `(Landroid/os/Parcel;I)V` | OPEN | — | Def FeedItem.java:102–112. No printed app-side parcel site for a FeedItem in this pass. Stays OPEN. |
| 16 | FeedItem$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at FeedItem.java:114–128. Field initializer runs at class init on first use (row 8 route). **Correction vs prior proposal, which left this OPEN** — same Creator-$1.\<init\> convention as row 4, flagged for the merger. |
| 17 | FeedItem$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedItem;` | OPEN | — | Def FeedItem.java:118–121. Framework dispatch only, no printed unparcel site. Stays OPEN. |
| 18 | FeedItem$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/entity/FeedItem;` | OPEN | — | Def FeedItem.java:124–127. Framework dispatch only. Stays OPEN. |
| 19 | TagInfo.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use, and first use is freshly printed here: TorrentFilterCollection.tag:98 `state.tags.contains(tag)` and AddTorrentViewModel.removeTag:163 `tags.remove(info)` both dispatch to TagInfo.equals (row 24), which cannot run before the class loads. Static CREATOR field at TagInfo.java:69 runs at class init. **Correction vs prior proposal, which left this OPEN** on the reasoning that "only printed class references were type uses / the OPEN parcel ctor" — that reasoning missed the freshly verified equals triggers, which are printed uses on a REACHABLE-anchored route. Flagged as a convention variant (see Conventions 3): rows 19 and 27 stand/fall with row 24. **Not** bootstrapped by TorrentInfo Parcel ctor's `TagInfo.CREATOR` use at TorrentInfo.java:140 — that ctor is itself OPEN (batch 30 row 2), so it cannot bootstrap anything (dependency rule). |
| 20 | TagInfo.\<init\>(long,String,int) | `(JLjava/lang/String;I)V` | OPEN | — | Def TagInfo.java:38–42 (3-arg ctor). Grep of all files fetched in this pass finds no `new TagInfo(...)` site. Room-generated instantiation of this `@Entity` is not in the printed source, and entity status alone does not flip a ctor to REACHABLE (see Conventions 7). Stays OPEN; the named resolver is a printed construction site or printed generated Room code. |
| 21 | TagInfo.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | OPEN | — | Def TagInfo.java:51–55. Only printed caller is its own CREATOR.createFromParcel:71–73, itself OPEN (row 28). Stays OPEN. |
| 22 | TagInfo.\<init\>(String,int) | `(Ljava/lang/String;I)V` | OPEN | — | Def TagInfo.java:45–48 (2-arg `@Ignore` ctor). No printed caller in this pass. Stays OPEN. |
| 23 | TagInfo.describeContents | `()I` | OPEN | — | Def TagInfo.java:58–60. Framework marshalling only; no printed parcel site. Stays OPEN. |
| 24 | TagInfo.equals | `(Ljava/lang/Object;)Z` | REACHABLE | INFERRED | Library dispatch, two freshly printed triggers: TorrentFilterCollection.tag:98 `tag == null || state.tags.contains(tag)` (List.contains dispatches to element equals, TagInfo.java:82–91) and AddTorrentViewModel.removeTag:162–163 `tags.remove(info)` (List.remove dispatches to equals). **Confirmed_by correction vs prior proposal, which marked this SOURCE; label unchanged** — neither trigger names `equals` in app code, so this is INFERRED under the uniform library-dispatch treatment (same as batch 29 row 15, batch 30 row 25). |
| 25 | TagInfo.toString | `()Ljava/lang/String;` | OPEN | — | Def TagInfo.java:103–109. No printed logging/concatenation caller in this pass. Stays OPEN. |
| 26 | TagInfo.writeToParcel | `(Landroid/os/Parcel;I)V` | OPEN | — | Def TagInfo.java:63–67. No printed app-side parcel site for a TagInfo in this pass (AddTorrentParams parcel ctor, prior pass, is itself an OPEN row and cannot bootstrap this one). Stays OPEN. |
| 27 | TagInfo$1.\<init\> | `()V` | REACHABLE | INFERRED | Anonymous Creator at TagInfo.java:69–79. Field initializer runs at class init on first use (row 24 equals routes). **Correction vs prior proposal, which left this OPEN** — same Creator-$1.\<init\> convention as rows 4/16, flagged for the merger; stands/falls with row 24. |
| 28 | TagInfo$1.createFromParcel | `(Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;` | OPEN | — | Def TagInfo.java:71–73. Framework dispatch only, no printed unparcel site. Stays OPEN. |
| 29 | TagInfo$1.newArray | `(I)[Lorg/proninyaroslav/libretorrent/core/model/data/entity/TagInfo;` | OPEN | — | Def TagInfo.java:76–78. Framework dispatch only. Stays OPEN. |
| 30 | Torrent.\<clinit\> | `()V` | REACHABLE | INFERRED | Class init precedes first use: TorrentSessionImpl.addTorrent path:263 `new Torrent(...)` (row 32). Static CREATOR field at Torrent.java:157 runs at class init. JVM timing unprinted, hence INFERRED. |
| 31 | Torrent.\<init\>(Parcel) | `(Landroid/os/Parcel;)V` | OPEN | — | Def Torrent.java:104–117. Only printed caller is its own CREATOR.createFromParcel:160–163, itself OPEN (not a batch 31 row — Torrent `$1` trio rows live in another batch and are not judged here). Stays OPEN. |
| 32 | Torrent.\<init\>(String,Uri,String,boolean,long,boolean,boolean) | `(Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;ZJZZ)V` | REACHABLE | SOURCE | TorrentSessionImpl:263–270 `Torrent torrent = new Torrent(params.sha1hash, params.downloadPath, params.name, params.addPaused, System.currentTimeMillis(), params.sequentialDownload, params.firstLastPiecePriority);` — argument order matches the descriptor exactly. Def Torrent.java:72–87 (`@Ignore` 7-arg ctor). |
| 33 | Torrent.\<init\>(String,String,Uri,String,boolean,long,boolean,boolean) | `(Ljava/lang/String;Ljava/lang/String;Landroid/net/Uri;Ljava/lang/String;ZJZZ)V` | OPEN | — | Def Torrent.java:89–101 (8-arg ctor, delegates to the 7-arg ctor at:98 then sets magnet at:100). No printed 8-arg construction in this pass — the session uses the 7-arg ctor + `setMagnetUri` instead (row 39 at TorrentSessionImpl:277). The delegation inside the 8-arg ctor is not a caller of it. Stays OPEN. |
| 34 | Torrent.describeContents | `()I` | OPEN | — | Def Torrent.java:136–139. Framework marshalling only; no printed parcel site. Stays OPEN. (Torrent.writeToParcel is NOT a batch 31 row and is not judged here.) |
| 35 | Torrent.equals | `(Ljava/lang/Object;)Z` | OPEN | — | Def Torrent.java:179–182 (identity or equal `id`). No printed caller in this pass (repo lookups use id strings, e.g. TorrentSessionImpl:280 `repo.getTorrentById(torrent.id)`). Stays OPEN. |
| 36 | Torrent.getMagnet | `()Ljava/lang/String;` | REACHABLE | SOURCE | TorrentSessionImpl restore path:413–415 `if (path != null && torrent.isDownloadingMetadata()) { loadTask.putMagnet(torrent.getMagnet(), new File(path), ...); }`. Def Torrent.java:124–127. |
| 37 | Torrent.hashCode | `()I` | OPEN | — | Def Torrent.java:173–176 (`id.hashCode()`). No printed hash-collection use of a Torrent entity in this pass. Stays OPEN. |
| 38 | Torrent.isDownloadingMetadata | `()Z` | REACHABLE | SOURCE | TorrentSessionImpl:413 (restore path, with row 36), and independently :290 and :343 (session greps, this pass). Def Torrent.java:119–122. |
| 39 | Torrent.setMagnetUri | `(Ljava/lang/String;)V` | REACHABLE | SOURCE | TorrentSessionImpl:277 `torrent.setMagnetUri(params.source);`, inside the `params.fromMagnet` branch (bencode null) at:273–277. Def Torrent.java:129–133 (sets magnet, `downloadingMetadata = magnet != null`). The branch condition is a parameter, not a never-taken guard — the call site runs when a magnet add arrives without loaded bencode. |
| 40 | Torrent.toString | `()Ljava/lang/String;` | OPEN | — | Def Torrent.java:186–200. No printed logging/concatenation caller in this pass. Stays OPEN. |

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
