# LibreTorrent A1 — parcel evidence (helper only, NOT the merger)

Role: evidence helper for batches 21/22/28 parcel rows. No merge-ready file,
graph definition, parts file, verification file, PROGRESS file, or notes file
was edited. Nothing was pushed.

## Method and scope

- Branch tree read: `/home/hatch/workspace/finish/clone/` (work-2026-10-31, HEAD 6805252).
- App source root grepped (read-only):
  `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main`
  — 281 `.java` files under `java/`.
- Per class, `grep -rn` over that root for: the class name (section A);
  marshalling verbs in every file mentioning the class (section B);
  every marshalling site in the whole tree (section C);
  plus CREATOR use, direct Parcel calls, typed/array/serializable sites
  (section D, appended). Patterns for section C:
  `putExtra|putParcelable|putParcelableArrayList|writeParcelable|setArguments|getArguments|getParcelable|readParcelable`
  — 122 matching lines in the whole tree.
- Source paths below are shortened to
  `.../java/org/proninyaroslav/libretorrent/...`; line numbers are as printed
  by `grep`/`sed` and were actually read.
- Judgement rule applied (as given for this helper task):
  (a) a printed write/read site on a reachable route makes the method
  REACHABLE; (b) no site after the full grep makes it UNREACHABLE —
  kind `framework_never_calls` for newArray/describeContents,
  `no_trigger_in_app` otherwise.
- Result of the full grep: NO marshalling site for any of the three classes
  (see "Whole-tree negative result" below). Every row below therefore gets
  an UNREACHABLE proposal under rule (b). No row is proposed REACHABLE.

## Whole-tree negative result (applies to all 10 rows)

- Section B is EMPTY for all three classes: in the files that mention each
  class, there is not one line containing `putExtra`, `putParcelable`,
  `putParcelableArrayList`, `writeParcelable`, `setArguments`,
  `getArguments`, `getParcelable`, or `readParcelable`.
  - AddTorrentParams: 36 mentions in 6 files; section B empty.
  - AdvancedTorrentInfo: 33 mentions in 6 files; section B empty.
  - MagnetInfo: 27 mentions in 6 files; section B empty.
- Section C (whole tree, 122 lines) parcels only other payloads, for example:
  - `ui/addtag/AddTagDialog.java:71` — `args.putParcelable(TAG_INIT_INFO, initInfo);`
    where `initInfo` is a `TagInfo` (`ui/addtag/AddTagActivity.java:57`:
    `TagInfo initInfo = getIntent().getParcelableExtra(TAG_INIT_INFO);`).
  - `ui/addtorrent/AddTorrentActivity.java:359` — `return i.getParcelableExtra(TAG_URI);`
    (a `Uri`, not one of these three classes).
  - `ui/detailtorrent/DetailTorrentFragment.java:544` — `i.putExtra(FileManagerDialog.TAG_CONFIG, config);`
    (a `FileManagerConfig`).
  - `ui/addfeed/AddFeedDialog.java:83` — `args.putParcelable(TAG_URI, uri);` (a `Uri`).
  - Remaining section-C sites are `Uri`, `FileManagerConfig`, `TagInfo`,
    `PreferenceActivityConfig`, list/recycler state objects, and plain
    `String`/`long`/`boolean` extras. None names, imports, or passes an
    `AddTorrentParams`, `AdvancedTorrentInfo`, or `MagnetInfo`.
- Section D: no `CREATOR` use outside each class's own file
  (`(no CREATOR use)` for all three); no `createFromParcel` call and no
  `Parcel.obtain` call outside the definitions; the only `writeToParcel`
  occurrences are the definitions themselves plus `super.writeToParcel`
  calls inside other Parcelable subclasses (e.g.
  `core/model/data/AdvancedTorrentInfo.java:103` inside its own
  `writeToParcel`, `core/model/data/PeerInfo.java:152`,
  `core/model/data/TorrentInfo.java:151`) — none of these parcels an
  instance of the three classes.
- Saved proof files (this work dir only):
  - `grep_AddTorrentParams.txt` (209 lines: sections A–D)
  - `grep_AdvancedTorrentInfo.txt` (208 lines: sections A–D)
  - `grep_MagnetInfo.txt` (198 lines: sections A–D)

## Caveat for the merger (read before applying)

The batch files themselves record an opposite convention in places:
batch 21/22 notes say app-tree zero alone does not flip a row to
UNREACHABLE, and batch 28's revision note says the UNREACHABLE-on-tree-grep
conditional was rejected. The proposals below follow THIS helper task's
rule (b) explicitly. If the merger retains the earlier convention, all
10 rows stay OPEN instead. The evidence (zero sites) is the same either
way; only the convention choice differs. This helper does not decide that
convention — it reports the evidence and the rule-(b) proposal.

## Per-row evidence

Short source roots:
- ATP = `core/model/AddTorrentParams.java`
- ATI = `core/model/data/AdvancedTorrentInfo.java`
- MI = `core/model/data/MagnetInfo.java`
- AIP = `core/model/data/AbstractInfoParcel.java`

### 21/36 — AddTorrentParams.<init>(Parcel) — proposed UNREACHABLE, no_trigger_in_app

- Definition (printed): ATP:77 — `public AddTorrentParams(Parcel source) {`
  with field reads ATP:78–88, e.g. ATP:83
  `downloadPath = source.readParcelable(Uri.class.getClassLoader());`.
- Only printed caller: ATP:111–112, inside the CREATOR body itself:
  `public AddTorrentParams createFromParcel(Parcel source) {`
  `return new AddTorrentParams(source);`.
- No printed marshalling site: section B empty for AddTorrentParams;
  section C parcels only the payloads listed above; section D finds no
  CREATOR use and no `createFromParcel` call outside this definition.
- The objects ARE used without parcelling, e.g.
  `core/model/TorrentEngine.java:1187` (`AddTorrentParams params = new AddTorrentParams(`),
  `ui/addtorrent/AddTorrentViewModel.java:510`
  (`AddTorrentParams params = new AddTorrentParams(`),
  `service/FeedDownloaderWorker.java:178` (`return new AddTorrentParams(`) —
  all direct constructions passed as ordinary method arguments
  (e.g. `core/model/TorrentEngine.java:329` `addTorrent(@NonNull AddTorrentParams params,`).
- Proposed verdict: UNREACHABLE, `no_trigger_in_app`.
- Grep file: `grep_AddTorrentParams.txt`.

### 21/38 — AddTorrentParams.describeContents — proposed UNREACHABLE, framework_never_calls

- Definition (printed): ATP:91–93 — `public int describeContents() { return 0; }`.
- The framework calls `describeContents` only when the object is actually
  parcelled. No printed parcel site for AddTorrentParams exists (sections
  B/C/D as for 21/36); the only `writeParcelable` involving this class is
  ATP:102 `dest.writeParcelable(downloadPath, flags);`, which parcels its
  `Uri` field, not the `AddTorrentParams` itself.
- Proposed verdict: UNREACHABLE, `framework_never_calls`.
- Grep file: `grep_AddTorrentParams.txt`.

### 22/1 — AddTorrentParams.writeToParcel — proposed UNREACHABLE, no_trigger_in_app

- Definition (printed): ATP:96 — `public void writeToParcel(Parcel dest, int flags) {`,
  body ATP:97–107 (e.g. ATP:105 `dest.writeTypedList(tags);`).
- No printed caller: the whole-tree `writeToParcel` list in section D
  contains this definition and other classes' definitions only; no app
  code calls it, and no section-C site parcels an `AddTorrentParams`
  (which is what would trigger the framework to call it).
- Proposed verdict: UNREACHABLE, `no_trigger_in_app`.
- Grep file: `grep_AddTorrentParams.txt`.

### 22/3 — AddTorrentParams$1.createFromParcel — proposed UNREACHABLE, no_trigger_in_app

- Definition (printed): ATP:109–113 — CREATOR field
  `public static final Parcelable.Creator<AddTorrentParams> CREATOR = ...`,
  `public AddTorrentParams createFromParcel(Parcel source) {`
  `return new AddTorrentParams(source);`.
- No printed trigger: section D finds no use of `AddTorrentParams.CREATOR`
  and no `createFromParcel` call outside this definition; no section-C
  read site (`getParcelable*`/`readParcelable`) names this class.
  This is the sole caller of 21/36, so 21/36 and 22/3 stand or fall
  together — both are proposed UNREACHABLE here.
- Proposed verdict: UNREACHABLE, `no_trigger_in_app`.
- Grep file: `grep_AddTorrentParams.txt`.

### 28/23 — AdvancedTorrentInfo.<init>(Parcel) — proposed UNREACHABLE, no_trigger_in_app

- Definition (printed): ATI:76 — `public AdvancedTorrentInfo(Parcel source) {`,
  with `super(source);` (ATI:77) and field reads ATI:79–93.
- Only printed caller: ATI:123–126, inside the CREATOR body itself:
  `public AdvancedTorrentInfo createFromParcel(Parcel source)`
  `return new AdvancedTorrentInfo(source);`.
- No printed marshalling site: section B empty for AdvancedTorrentInfo;
  section C parcels only other payloads; section D finds no CREATOR use
  and no `createFromParcel` call outside this definition.
- Indirect-route check: ATI:34 `public class AdvancedTorrentInfo extends AbstractInfoParcel`.
  AIP has no CREATOR (AIP:31–52: only `writeToParcel` writing `parcelId`),
  so no framework dispatch via the parent class exists either.
  The object is held, not parcelled, e.g.
  `ui/detailtorrent/TorrentDetailsInfo.java:37`
  `private AdvancedTorrentInfo advancedInfo;` in a class that extends
  `BaseObservable` (TorrentDetailsInfo.java:32), not Parcelable; and
  `ui/detailtorrent/DetailTorrentViewModel.java:218`
  `public void updateInfo(AdvancedTorrentInfo advancedInfo) {`.
- Proposed verdict: UNREACHABLE, `no_trigger_in_app`.
- Grep file: `grep_AdvancedTorrentInfo.txt`.

### 28/26 — AdvancedTorrentInfo.describeContents — proposed UNREACHABLE, framework_never_calls

- Definition (printed): ATI:95–98 — `public int describeContents() { return 0; }`.
- As for 21/38: the framework calls this only when the object is parcelled,
  and no printed parcel site for AdvancedTorrentInfo exists (sections
  B/C/D as for 28/23).
- Proposed verdict: UNREACHABLE, `framework_never_calls`.
- Grep file: `grep_AdvancedTorrentInfo.txt`.

### 28/30 — AdvancedTorrentInfo.writeToParcel (Parcel, int) — proposed UNREACHABLE, no_trigger_in_app

- Definition (printed): ATI:101 — `public void writeToParcel(Parcel dest, int flags) {`,
  with ATI:103 `super.writeToParcel(dest, flags);` and field writes
  ATI:105–117.
- No printed caller or trigger: the whole-tree `writeToParcel` list
  (section D) contains only definitions and intra-class `super` calls;
  no section-C site parcels an `AdvancedTorrentInfo`. The
  `super.writeToParcel` at ATI:103 is inside this very method, not a
  site that parcels an `AdvancedTorrentInfo` instance.
- The object is produced and consumed without parcelling, e.g.
  `core/model/TorrentEngine.java:832`
  `public AdvancedTorrentInfo makeAdvancedInfoSync(@NonNull String id) {`
  and `:846` `return new AdvancedTorrentInfo(`.
- Proposed verdict: UNREACHABLE, `no_trigger_in_app`.
- Grep file: `grep_AdvancedTorrentInfo.txt`.

### 28/32 — AdvancedTorrentInfo$1.createFromParcel (Parcel) — proposed UNREACHABLE, no_trigger_in_app

- Definition (printed): ATI:119–126 — CREATOR field
  `public static final Parcelable.Creator<AdvancedTorrentInfo> CREATOR =`,
  `public AdvancedTorrentInfo createFromParcel(Parcel source)`
  `return new AdvancedTorrentInfo(source);`.
- No printed trigger: section D finds no use of
  `AdvancedTorrentInfo.CREATOR` and no `createFromParcel` call outside
  this definition; no section-C read site names this class. This is the
  sole caller of 28/23, so 28/23 and 28/32 stand or fall together — both
  proposed UNREACHABLE here.
- Proposed verdict: UNREACHABLE, `no_trigger_in_app`.
- Grep file: `grep_AdvancedTorrentInfo.txt`.

### 28/35 — MagnetInfo.<init>(Parcel) — proposed UNREACHABLE, no_trigger_in_app

- Definition (printed): MI:56 — `public MagnetInfo(Parcel s) {`, field reads
  MI:57–63, e.g. MI:60 `filePriorities = s.readArrayList(Priority.class.getClassLoader());`.
- Only printed caller: MI:83–86, inside the CREATOR body itself:
  `public MagnetInfo createFromParcel(Parcel source)`
  `return new MagnetInfo(source);`.
- No printed marshalling site: section B empty for MagnetInfo; section C
  parcels only other payloads; section D finds no CREATOR use and no
  `createFromParcel` call outside this definition.
- The object is used without parcelling, e.g.
  `core/model/session/TorrentSessionImpl.java:439`
  `return new MagnetInfo(uri, resParams.getInfoHashes().getBest().toHex(),`
  and `:450` `return new MagnetInfo(uri, sha1hash, name,`,
  consumed at `ui/addtorrent/AddTorrentViewModel.java:237–240`
  (`Pair<MagnetInfo, Single<TorrentMetaInfo>> res = v.engine.fetchMagnet(uri.toString());`
  `MagnetInfo magnetInfo = res.first;`).
- Proposed verdict: UNREACHABLE, `no_trigger_in_app`.
- Grep file: `grep_MagnetInfo.txt`.

### 28/37 — MagnetInfo.describeContents — proposed UNREACHABLE, framework_never_calls

- Definition (printed): MI:65–68 — `public int describeContents() { return 0; }`.
- As for 21/38 and 28/26: the framework calls this only when the object is
  parcelled, and no printed parcel site for MagnetInfo exists (sections
  B/C/D as for 28/35). Its `writeToParcel` (MI:71–77, not a row in this
  task) likewise has no printed caller in the files read.
- Proposed verdict: UNREACHABLE, `framework_never_calls`.
- Grep file: `grep_MagnetInfo.txt`.

## Counts printed in this task

- Rows judged: 10 (21/36, 21/38, 22/1, 22/3, 28/23, 28/26, 28/30, 28/32,
  28/35, 28/37).
- Proposed REACHABLE: 0. Proposed UNREACHABLE: 10
  (7 × `no_trigger_in_app`: 21/36, 22/1, 22/3, 28/23, 28/30, 28/32, 28/35;
  3 × `framework_never_calls`: 21/38, 28/26, 28/37).
  Note: 28/35 is counted in the 7; the split is 7 + 3 = 10.
- Undecided / guessed: 0. Every row was decided from the saved full grep;
  no row was flipped on absence alone without the grep file — the grep
  files above ARE the absence proof.
- Tree counts: 281 Java files grepped; 122 whole-tree marshalling-verb
  lines (section C pattern, including `readParcelable`); class mentions:
  AddTorrentParams 36 in 6 files, AdvancedTorrentInfo 33 in 6 files,
  MagnetInfo 27 in 6 files; section-B marshalling lines in
  class-mentioning files: 0 for all three classes.
- Files in this work dir: `EVIDENCE.md` plus
  `grep_AddTorrentParams.txt`, `grep_AdvancedTorrentInfo.txt`,
  `grep_MagnetInfo.txt`. No other file was written, and no file outside
  this work dir was modified.
