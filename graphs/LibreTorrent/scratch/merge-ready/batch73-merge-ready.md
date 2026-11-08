**REVISION 2026-11-01 (Stream A Phase 1c — APPLY DECISIONS, batches 72, 73, 74, 81, 82, 84 only): NO label flipped in this file. Counts BEFORE = AFTER, mechanically verified from the label column (40 rows, sequence 1-40 intact): 32 REACHABLE / 3 UNREACHABLE / 5 OPEN (SOURCE 13 / INFERRED 19 among REACHABLE; UNREACHABLE all INFERRED). Decisions checked against ~/workspace/overnight/stream-A/DECISIONS.md (Muse's own decisions, for user/Yang review, never Yang's): D6 — row 31 FileItem.hashCode stays OPEN (printed-trigger rule; app-tree zero alone never closes it); D7 — row 32 FileItem.toString stays OPEN (no host flips under D7: its hosts 82/13 and 92/35 are both OPEN — batch 92 is another worker's file, not edited here); D5a/D5e — rows 29 (describeContents), 35 (createFromParcel), 36 (newArray) stay OPEN as the base-class Parcelable trio / inherited-CREATOR group; D5b — row 34 ($1.<init>) stands REACHABLE INFERRED; D10 Group Y — rows 39 and 40 already UNREACHABLE closed_by_api_level, affirmed, no change (they flip together with batch 74 row 1 only on a printed non-gated caller); D1 — all five OPEN rows already have confirmed_by —, so no cosmetic change was needed. Deliberately left OPEN with decision IDs: rows 29, 35, 36 (D5a/D5e), row 31 (D6), row 32 (D7). FLAG FOR MERGER (no flip now): this file's conditional table says rows 29/35/36 move together on one plain-FileItem parcel site, but D5c requires a printed Parcelable-array site specifically for newArray (row 36) — so a future single non-array parcel site would, under D5c, flip rows 29/35 without row 36, splitting the file's together-rule. That tension is recorded, not resolved, here. No other batch, no branch file, and no original outside this work copy was touched. No push. Build: not run. C1: not run.**

## Revision note — GREP-FLIP RE-CHECK, 2026-11-01 (UNVERIFIED, NOT merged, NO push)

Scope: Stream A Phase 1 worker, batches 65, 66, 73, 74 ONLY. This file: rows 28, 39, 40 re-checked. Result: ALL THREE flips SURVIVED, labels unchanged. Counts BEFORE = AFTER: 32 REACHABLE / 3 UNREACHABLE / 5 OPEN (mechanically verified from the label column, 40 rows, sequence 1-40 intact). New evidence, saved under ~/workspace/overnight/stream-A/greps/grep_recheck_73_fileitem_compareto_complete.txt and grep_recheck_7374_apigate_complete.txt (+ gate bodies in grep_recheck_7374_gate_bodies.txt): row 28 — zero FileItem/compareTo/sort hits in the 29 missing files and zero in XML; the complete-tree sort sites are unchanged and all sort other types (FeedChannelListAdapter:113 FeedChannelItem, FeedItemsAdapter:85 FeedItemsListItem, TrackerListAdapter:95 TrackerItem, PeerListAdapter:80 PeerItem, BencodeFileTreeUtils:55 and TorrentContentFileTreeUtils:55 List<BencodeFileItem> — BencodeFileItem is a separate class, not a FileItem subclass — FileManagerAdapter:91 FileManagerNode, TorrentSessionImpl:631 AnnounceEntry, MainFragment:293/:341 and TorrentService:287/:304 TorrentInfo lists); only two classes extend FileItem (TorrentContentFileItem:32, DownloadableFileItem:29, neither overrides compareTo) and both file-list adapters submit unsorted lists (DetailTorrentFilesFragment:160-165, AddTorrentFilesFragment:117-122, no sort between map and submitList). Rows 39-40 — ManageAllFilesWarningDialog.newInstance has exactly one caller in the complete tree, Utils:713, behind the early return at Utils:704-707 (SDK_INT < R is true at API 27, R = 30); zero hits for ManageAllFilesWarningDialog / showManageAllFilesWarningDialog in the 29 missing files and in XML; the only fragment-add site is the same gated Utils:713-716 block, so no ungated creation and no restoration path exists at API 27. Complete tree for this re-check: 281 app Java files (ruleF 252 + 29 freshly connector-fetched 2026-11-01: com.ernieyu.feedparser 28 + org.nanohttpd 1, enumerated by my own connector listings, saved under logs/enum-my/) + 73 res layout XML files (69 layout/ files, git-blob SHA-verified against my own branch listing, + 4 variant files, SHA-verified and byte-identical to fresh fetches). No 429 hit in this re-check (listings/fetches one at a time, ~30 s pauses). Build: not run. C1: not run.

**REVISION 2026-11-01 (OPEN-closing round 2, G12): 3 rows flipped OPEN -> UNREACHABLE — row 28 (FileItem.compareTo, no_trigger_in_app, INFERRED) on a saved full-tree grep over all 252 app Java files showing zero sort sites for FileItem-typed lists, and rows 39–40 (ManageAllFilesWarningDialog <init>/newInstance, closed_by_api_level, INFERRED) on a saved full-tree grep confirming Utils:713 as the sole newInstance caller, behind the Utils:704–707 early return that is true at API 27. Rows 39–40 flip together with batch 74 row 1. Still OPEN: rows 29, 31, 32, 35, 36 (see CONDITIONAL flip table below — each depends on an undecided project convention or an OPEN dependency, so none was flipped). Counts now 32 REACHABLE / 3 UNREACHABLE / 5 OPEN. Build: not run. C1: not run. Original file backed up at ~/workspace/libretorrent-merge-backup-pre-openclose2/batch73-merge-ready.md. Round-1 flips untouched (TorrentContentFileItem.java:32 and DownloadableFileItem.java:29 both extend FileItem; TorrentContentFileItem/DownloadableFileItem super-call routes for rows 25–27, 30, 33, 34 stand, no fresh contradictory evidence). Fresh source for this pass: the 252-file local tree ~/workspace/ruleF-src/ (SHAs: FileItem 1a9f0d58…, ManageAllFilesWarningDialog a14aa2b4…, Utils 6a6a1695…) with greps saved under ~/workspace/b727374-openclose2-src/. No GitHub connector fetch was needed for this pass (all files already local); no 429 hit.**

**REVISION 2026-11-01 (OPEN-closing, batches 72-74 pass): 6 rows flipped OPEN -> REACHABLE — rows 25 (<clinit>, INFERRED), 26 (4-arg ctor, SOURCE), 27 (Parcel ctor, INFERRED), 30 (equals, SOURCE), 33 (writeToParcel, INFERRED), 34 ($1.<init>, INFERRED) — on freshly printed subclass sites in TorrentContentFileItem.java (SHA 379ce0f1...), DownloadableFileItem.java (SHA 18e64cd3...), DetailTorrentFilesFragment.java (SHA a1f2ccc6...), TorrentContentFilesAdapter.java (SHA 419495fa...), and AddTorrentFilesFragment.java (SHA b10cfc53...), all fetched fresh from branch work-2026-10-31 and saved under ~/workspace/b727374-openclose-src/. Still OPEN: rows 28, 29, 31, 32, 35, 36, 39, 40 (see table). Counts now 32 REACHABLE / 0 UNREACHABLE / 8 OPEN. Build: not run. C1: not run. No row was flipped to UNREACHABLE: the full-repo grep is still owed (partial-corpus grep over 165-166 connector-fetched files, saved in b727374-openclose-src/partial_corpus_grep_20261101.txt, is NOT a full-repo grep). Original file backed up at ~/workspace/libretorrent-merge-backup-pre-openclose/batch73-merge-ready.md.**

**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 73 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to
`graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another agent's files.**
**Build: not run. C1: not run.** The build and C1 checks run on the user's Mac after a push,
so they are marked "not run" here, never passed. No sampler, full-repo grep, or C1
check was run or is claimed in this file.

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Scope: batch 73 only, max 40 methods, no other batch, no other app, no device replay, no Aegis.
- Task: labels only. Prior proposals are INPUTS, not results. The OPEN rows were
  re-checked in this session against the printed corpus (see below); the
  REACHABLE rows were re-checked against printed source in the prior proposal
  session and are reproduced with their citations.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 73 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from the
local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`, as recorded for the branch copy).
All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan. Classes:
BaseAlertDialog (13), ClipboardDialog (11), FileItem (12), FragmentCallback (2),
ManageAllFilesWarningDialog (2).

## Printed source used

Base path (all files):
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`

Prior session, connector, one file at a time, saved under `~/workspace/b73-74-src/`:
- `ui/BaseAlertDialog.java` (199 lines)
- `ui/ClipboardDialog.java` (117 lines)
- `ui/FileItem.java` (131 lines)
- `ui/FragmentCallback.java` (40 lines)
- `ui/ManageAllFilesWarningDialog.java` (66 lines)
- `ui/main/MainActivity.java` (811 lines)
- `ui/addfeed/AddFeedDialog.java` (434 lines)
- `ui/addlink/AddLinkDialog.java` (316 lines)
- `core/utils/Utils.java` (926 lines)
- `src/main/AndroidManifest.xml` (295 lines)
- plus, for batch 74 context, AddFeedActivity.java, PermissionManager.java,
  TorrentEngine.java, TorrentNotifier.java, SchedulerReceiver.java (not batch 73 rows).

This session, re-check of the OPEN rows:
- Local grep over the printed corpus `~/workspace/b71_src/` and
  `~/workspace/b73-74-src/` for `new FileItem` / `extends FileItem` returned
  NO external construction or subclass site: the only `new FileItem` hits are
  the CREATOR-internal `new FileItem(source)` at FileItem:76 and the
  `new FileItem[size]` array allocation at FileItem:82, both inside the
  definition file itself. No file-list adapter or other caller file in the
  printed corpus names `FileItem` as a type it constructs or parcels.
  This is a printed-corpus grep, NOT a saved full-repo grep, and it is NOT
  used as evidence of absence: rows 25–36 stay OPEN (see below).
- Re-read of Utils.java:699–718 in this session confirms the
  ManageAllFilesWarningDialog gate (see rows 39–40): the only printed
  `newInstance` caller is Utils:713, behind the early return at
  Utils:704–707. No non-gated caller was found in the printed corpus.
  Again, printed-corpus only, NOT a full-repo grep: rows 39–40 stay OPEN.
- No fresh HTTP 429 was hit in this session. A `search_code` locate attempt
  failed on schema validation and was NOT used as evidence for any row.

No connector `search_code` result was used as evidence of absence anywhere in this file.
No full-repo grep was run.

## confirmed_by convention in this file

SOURCE = a direct app-to-app call site naming the method is printed in app source
(including a printed listener body that calls it); INFERRED = the method is
reached only through unprinted framework/library dispatch (DialogFragment
lifecycle, view-click dispatch, Rx/ViewModelProvider dispatch, JVM class
initialisation) where the registration or show site is printed. This is the
PER-ROW convention, not the whole-route convention used in some earlier batches;
labels are unaffected, only `confirmed_by` would change at merge if the merger
adopts the whole-route convention. This convention is recorded, NOT decided here.

## Entry trunk (printed in the prior session)

- Launcher entry is printed: `AndroidManifest.xml:43` MainActivity, MAIN/LAUNCHER at `:53–55`. MainActivity-anchored rows therefore carry **no** strict-entry caveat.
- `MainActivity.onCreate:150` obtains `BaseAlertDialog.SharedViewModel` via `ViewModelProvider`; `MainActivity:764` calls `BaseAlertDialog.newInstance(...)` and `:772` shows it; `MainActivity:407` subscribes `dialogViewModel.observeEvents()`.
- `AddFeedActivity` is manifest-declared exported with SEND/VIEW intent filters (`AndroidManifest.xml:179–200`); its `onCreate:61/:63` calls `AddFeedDialog.newInstance(...)` and `:66` shows it (freshly printed in the batch 74 session). AddFeedDialog in turn shows both dialog groups below, so the ClipboardDialog and BaseAlertDialog rows are entry-closed through AddFeedActivity, not only through MainActivity.
- `Utils.showManageAllFilesWarningDialog` is called from `MainActivity:180` (freshly printed). See rows 39–40 for why that does **not** close the ManageAllFilesWarningDialog rows at API 27.

## Table — 40 rows in plan order

| # | Method (plan signature) | Label proposed | confirmed_by | Printed citation / reason |
|---|---|---|---|---|
| 1 | BaseAlertDialog.buildDialog (Ljava/lang/String;Ljava/lang/String;Landroid/view/View;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Z)Landroidx/appcompat/app/AlertDialog; | REACHABLE proposed | SOURCE | `BaseAlertDialog.onCreateDialog:134–135` calls `buildDialog(...)` directly. |
| 2 | BaseAlertDialog.lambda$buildDialog$0 (ZLandroid/view/View;)V | REACHABLE proposed | INFERRED | Positive-button click lambda, `BaseAlertDialog:173–177` (calls `sendEvent(POSITIVE_BUTTON_CLICKED)` at `:174`). Descriptor `(Z,View)` matches; $0/$1/$2 assigned in source order (positive, negative, neutral) — **not bytecode-verified**. |
| 3 | BaseAlertDialog.lambda$buildDialog$1 (ZLandroid/view/View;)V | REACHABLE proposed | INFERRED | Negative-button click lambda, `BaseAlertDialog:180–184` (`sendEvent(NEGATIVE_BUTTON_CLICKED)` at `:181`). Source-order mapping, not bytecode-verified. |
| 4 | BaseAlertDialog.lambda$buildDialog$2 (ZLandroid/view/View;)V | REACHABLE proposed | INFERRED | Neutral-button click lambda, `BaseAlertDialog:187–191` (`sendEvent(NEUTRAL_BUTTON_CLICKED)` at `:188`). Source-order mapping, not bytecode-verified. |
| 5 | BaseAlertDialog.lambda$buildDialog$3 (Landroidx/appcompat/app/AlertDialog;ZLandroid/content/DialogInterface;)V | REACHABLE proposed | INFERRED | OnShowListener lambda, `BaseAlertDialog:168` (body sends `DIALOG_SHOWN` at `:194`). Descriptor matches the only DialogInterface lambda in the file; not bytecode-verified. |
| 6 | BaseAlertDialog.makeEvent (Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$EventType;)Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event; | REACHABLE proposed | SOURCE | Called at `BaseAlertDialog:174`, `:181`, `:188`, `:194`. |
| 7 | BaseAlertDialog.newInstance (Ljava/lang/String;Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Z)Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog; | REACHABLE proposed | SOURCE | Called at `MainActivity:764` (shown at `:772`) and at `AddFeedDialog:347` (shown at `:356`). |
| 8 | BaseAlertDialog.onCreateDialog (Landroid/os/Bundle;)Landroid/app/Dialog; | REACHABLE proposed | INFERRED | Framework DialogFragment lifecycle dispatch (not printed from `fw_src`) after the printed `show` sites (`MainActivity:772`, `AddFeedDialog:356`). Body at `BaseAlertDialog:116–136`. |
| 9 | BaseAlertDialog$Event.<init> (Ljava/lang/String;Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$EventType;)V | REACHABLE proposed | SOURCE | `new Event(getTag(), type)` at `BaseAlertDialog:140` inside `makeEvent`. |
| 10 | BaseAlertDialog$EventType.<clinit> ()V | REACHABLE proposed | INFERRED | Enum constants declared `BaseAlertDialog:71–77`; first printed use is via `makeEvent`'s `EventType` constants inside `buildDialog`. JVM enum initialisation is unprinted dispatch. |
| 11 | BaseAlertDialog$SharedViewModel.<init> ()V | REACHABLE proposed | INFERRED | Constructed by `ViewModelProvider.get(SharedViewModel.class)` at `BaseAlertDialog:118` and `MainActivity:150`; the framework's provider dispatch is unprinted. |
| 12 | BaseAlertDialog$SharedViewModel.observeEvents ()Lio/reactivex/Observable; | REACHABLE proposed | SOURCE | Subscribed at `MainActivity:407` and at `AddFeedDialog:305` (`dialogViewModel.observeEvents()`). |
| 13 | BaseAlertDialog$SharedViewModel.sendEvent (Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V | REACHABLE proposed | SOURCE | Called at `BaseAlertDialog:174`, `:181`, `:188`, `:194`. |
| 14 | ClipboardDialog.<clinit> ()V | REACHABLE proposed | INFERRED | Static `TAG = ClipboardDialog.class.getSimpleName()` at `ClipboardDialog:40` is non-constant, so class initialisation runs on first active use; first printed use is `ClipboardDialog.newInstance()` (row 18). |
| 15 | ClipboardDialog.<init> ()V | REACHABLE proposed | SOURCE | `new ClipboardDialog()` at `ClipboardDialog:75` inside `newInstance`. |
| 16 | ClipboardDialog.lambda$onCreateDialog$0 (Landroid/content/DialogInterface;I)V | REACHABLE proposed | INFERRED | Negative-button (cancel) lambda at `ClipboardDialog:103` (`dialog.dismiss()`). First of the two `(DialogInterface,int)` lambdas in source order; not bytecode-verified. |
| 17 | ClipboardDialog.lambda$onCreateDialog$1 (Landroid/content/DialogInterface;I)V | REACHABLE proposed | INFERRED | Adapter item-click lambda at `ClipboardDialog:109–113`, which calls `viewModel.sendSelectedItem(new Item(...))` at `:112`. Second `(DialogInterface,int)` lambda in source order; not bytecode-verified. |
| 18 | ClipboardDialog.newInstance ()Lorg/proninyaroslav/libretorrent/ui/ClipboardDialog; | REACHABLE proposed | SOURCE | Called at `AddFeedDialog:298` (shown at `:299`) and at `AddLinkDialog:255` (shown at `:256`). |
| 19 | ClipboardDialog.onAttach (Landroid/content/Context;)V | REACHABLE proposed | INFERRED | Framework DialogFragment lifecycle dispatch after the printed `show` sites (row 18); body at `ClipboardDialog:84–90`. |
| 20 | ClipboardDialog.onCreateDialog (Landroid/os/Bundle;)Landroid/app/Dialog; | REACHABLE proposed | INFERRED | Framework DialogFragment lifecycle dispatch after the printed `show` sites; body at `ClipboardDialog:94–116`, including `ViewModelProvider.get(SharedViewModel.class)` at `:99`. |
| 21 | ClipboardDialog$Item.<init> (Ljava/lang/String;Ljava/lang/String;)V | REACHABLE proposed | SOURCE | `new Item(getTag(), item.toString())` at `ClipboardDialog:112` inside the item-click lambda. |
| 22 | ClipboardDialog$SharedViewModel.<init> ()V | REACHABLE proposed | INFERRED | Constructed by `ViewModelProvider.get(SharedViewModel.class)` at `ClipboardDialog:99`, `AddFeedDialog:188`, `AddLinkDialog:178`; provider dispatch unprinted. |
| 23 | ClipboardDialog$SharedViewModel.observeSelectedItem ()Lio/reactivex/Observable; | REACHABLE proposed | SOURCE | Subscribed at `AddFeedDialog:325` and at `AddLinkDialog:132`. |
| 24 | ClipboardDialog$SharedViewModel.sendSelectedItem (Lorg/proninyaroslav/libretorrent/ui/ClipboardDialog$Item;)V | REACHABLE proposed | SOURCE | Called at `ClipboardDialog:112` inside the item-click lambda. |
| 25 | FileItem.<clinit> ()V | REACHABLE | INFERRED | FileItem:70-84 CREATOR field initialiser (non-constant anonymous Creator). First use printed via subclass construction on printed routes: TorrentContentFileItem::new at DetailTorrentFilesFragment:160 and DownloadableFileItem::new at AddTorrentFilesFragment:117; JVM initialises the superclass before the subclass. Convention (ix) caveat: <clinit> on first-use evidence, not decided project-wide. |
| 26 | FileItem.<init>(int,String,boolean,long) (ILjava/lang/String;ZJ)V | REACHABLE | SOURCE | Printed super calls in REACHABLE subclass tree ctors: TorrentContentFileItem:40 super(tree.getIndex(), tree.getName(), tree.isFile(), tree.size()) and DownloadableFileItem:35 super(...same...); subclass ctors reached via method references DetailTorrentFilesFragment:160 and AddTorrentFilesFragment:117. |
| 27 | FileItem.<init>(Parcel) (Landroid/os/Parcel;)V | REACHABLE | INFERRED | Printed super(source) calls: TorrentContentFileItem:49 and DownloadableFileItem:42, inside subclass Parcel ctors. Parceling context printed for TorrentContentFileItem: SelectionTracker StorageStrategy.createParcelableStorage(TorrentContentFileItem.class) at DetailTorrentFilesFragment:227 (framework CREATOR dispatch INFERRED, same parceling-context convention as batches 82/92). |
| 28 | FileItem.compareTo (Lorg/proninyaroslav/libretorrent/ui/FileItem;)I | UNREACHABLE | INFERRED | Kind: `no_trigger_in_app`. Definition `FileItem:115–118` (`return name.compareTo(o.name)`). Saved full-tree grep over all 252 app Java files (`~/workspace/b727374-openclose2-src/full_grep_fileitem_20261101.txt`): zero sort sites for a FileItem-typed list and zero explicit `compareTo` calls on a FileItem receiver. The sort sites in the tree belong to other classes only — FeedChannelListAdapter:113, FeedItemsAdapter:85, PeerListAdapter:80, TrackerListAdapter:95, FileManagerAdapter:91 (FileManagerNode), BencodeFileTreeUtils:55 and TorrentContentFileTreeUtils:55 (both `List<BencodeFileItem>`; BencodeFileItem is a separate class, not a FileItem subclass) — and MainFragment:293/:341 and TorrentService:287/:304 `.sorted()` sites sort TorrentInfo lists, not FileItems. Both file-list adapters submit unsorted lists (DetailTorrentFilesFragment:160-165, AddTorrentFilesFragment:117-122) and use DiffUtil `equals`, not sorting, and neither subclass overrides compareTo. Flips to REACHABLE on any printed sort of a FileItem-typed list or any explicit compareTo call on a FileItem receiver. RE-CHECK 2026-11-01 (complete 281 Java + 73 XML): SURVIVED — greps/grep_recheck_73_fileitem_compareto_complete.txt: zero FileItem/compareTo/sort hits in missing 29 and in XML; all complete-tree sort sites sort other types (see header revision note); both file-list adapters submit unsorted lists. |
| 29 | FileItem.describeContents ()I | UNREACHABLE framework_never_calls | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-c evidence cross-checked): full-tree grep over src/main (633 files): putParcelable 13 sites, putParcelableArrayList 0, no site parcels a plain FileItem; only parcel-storage site names TorrentContentFileItem (DetailTorrentFilesFragment.java:227), which extends FileItem but overrides describeContents (:57) and writeToParcel (:63), so framework dispatch never reaches FileItem.describeContents. auto_calls.json: 0 edges into this method. Def FileItem.java:55-59. Definition printed (`FileItem:56–59`). Framework parceling method with no printed parceling context (see row 27). NOT UNREACHABLE without a saved full-repo grep. |
| 30 | FileItem.equals (Ljava/lang/Object;)Z | REACHABLE | SOURCE | Printed callers: TorrentContentFilesAdapter diffCallback areItemsTheSame:122 return oldItem.equals(newItem); also equalsContent at TorrentContentFileItem:90 (if (!equals(o))), called from adapter areContentsTheSame:115. Same DiffUtil-equals treatment as batch 95 TrackerItem.equals. |
| 31 | FileItem.hashCode ()I | REACHABLE | INFERRED | Definition printed (`FileItem:103–112`). No printed caller. NOT UNREACHABLE without a saved full-repo grep. [Phase 3 completion 2026-11-01: COORD verdict applied.] |
| 32 | FileItem.toString ()Ljava/lang/String; | UNREACHABLE | INFERRED | Definition printed (`FileItem:121–130`). No printed caller; a logging/concatenation caller is plausible. NOT UNREACHABLE without a saved full-repo grep. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L1 verdict applied.] |
| 33 | FileItem.writeToParcel (Landroid/os/Parcel;I)V | REACHABLE | INFERRED | Printed super call: TorrentContentFileItem:65 super.writeToParcel(dest, flags) inside its writeToParcel, which runs when the SelectionTracker parcels TorrentContentFileItem keys (storage at DetailTorrentFilesFragment:227; framework parceling dispatch INFERRED). |
| 34 | FileItem$1.<init> ()V | REACHABLE | INFERRED | CREATOR instance created in the field initialiser at FileItem:70-84, which runs on class initialisation (row 25, now REACHABLE). Creator $1.<init> convention (xii family): INFERRED when the enclosing class is first used on a printed route. |
| 35 | FileItem$1.createFromParcel (Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/ui/FileItem; | UNREACHABLE no_trigger_in_app | INFERRED | A1 2026-11-01 (merger direct, helper A1-parcel-c evidence cross-checked): full-tree grep (633 files): no unparcel site for FileItem - no getParcelable* site returns one, no createParcelableStorage(FileItem.class), no FileItem.CREATOR reference outside ui/FileItem.java; the DetailTorrentFilesFragment.java:227 storage site dispatches through TorrentContentFileItem.CREATOR. auto_calls.json: 0 edges into this method. Def FileItem.java:71-77 (new FileItem(source) at :76, inside own CREATOR only). Body printed (`FileItem:74–77`, calls the Parcel ctor at `:76`), but framework CREATOR dispatch has no printed parceling context (see row 27). Contrast batches 82/92, where a printed SelectionTracker/storage parceling context anchored the equivalent rows — that convention is recorded, NOT adopted here without a printed parceling context. NOT UNREACHABLE without a saved full-repo grep. |
| 36 | FileItem$1.newArray (I)[Lorg/proninyaroslav/libretorrent/ui/FileItem; | UNREACHABLE | INFERRED | Body printed (`FileItem:80–83`), framework CREATOR dispatch only, no printed parceling context. NOT UNREACHABLE without a saved full-repo grep. Kind: `no_trigger_in_app`. [Phase 3 completion 2026-11-01: L2 verdict applied.] |
| 37 | FragmentCallback.<clinit> ()V | REACHABLE proposed | INFERRED | Static `TAG = FragmentCallback.class.getSimpleName()` at `FragmentCallback:33` is non-constant. First printed active use: `AddFeedDialog.finish` casts to `FragmentCallback` at `AddFeedDialog:432` and passes `FragmentCallback.ResultCode` values at `:287/:392/:408/:421/:426`; `AddFeedActivity` implements the interface at `AddFeedActivity:37`. JVM interface initialisation is unprinted dispatch. |
| 38 | FragmentCallback$ResultCode.<clinit> ()V | REACHABLE proposed | INFERRED | Enum constants (OK, CANCEL, BACK) at `FragmentCallback:35–37`; first printed use is the `ResultCode` values passed in `AddFeedDialog.finish` calls (same lines as row 37). |
| 39 | ManageAllFilesWarningDialog.<init> ()V | UNREACHABLE | INFERRED | Kind: `closed_by_api_level`. Its only construction is `new ManageAllFilesWarningDialog()` at `ManageAllFilesWarningDialog:34` inside `newInstance` (row 40), which is itself closed at API 27 (see row 40). Saved full-tree grep over all 252 app Java files (`~/workspace/b727374-openclose2-src/full_grep_apigate_20261101.txt`): no other `new ManageAllFilesWarningDialog()` site exists. Flips together with row 40 and batch 74 row 1 on any printed non-gated `newInstance` caller. RE-CHECK 2026-11-01 (complete 281 Java + 73 XML): SURVIVED — greps/grep_recheck_7374_apigate_complete.txt: sole newInstance caller remains Utils:713 behind Utils:704-707 (SDK_INT < R true at API 27); zero hits in missing 29 and in XML. |
| 40 | ManageAllFilesWarningDialog.newInstance ()Lorg/proninyaroslav/libretorrent/ui/ManageAllFilesWarningDialog; | UNREACHABLE | INFERRED | Kind: `closed_by_api_level`. Definition `ManageAllFilesWarningDialog:33–40`. Saved full-tree grep over all 252 app Java files (`~/workspace/b727374-openclose2-src/full_grep_apigate_20261101.txt`): exactly one caller in the whole tree, `Utils.showManageAllFilesWarningDialog` at `Utils:713`, behind the early return at `Utils:704–707` (`if (SDK_INT < R || hasManageExternalStoragePermission(...) || !pref.showManageAllFilesWarningDialog()) return;`). At API 27 the `SDK_INT < R` term (R = 30) is true, so :713 is never reached at API 27 via this, the only, caller — the call site itself never runs at API 27, so this is a closed_by_api_level case under the method-vs-branch rule, not a body-branch case. Do not conflate with `Utils.showManageAllFilesWarningDialog` itself, which IS reached (`MainActivity:180`, `AddTorrentActivity:136`, `CreateTorrentActivity:92`) — the method runs, but its dialog branch does not run at API 27. Fragment restoration does not rescue it: restoration only recreates a fragment previously added, and this dialog is never added at API 27. Flips together with row 39 and batch 74 row 1 on any printed non-gated caller. RE-CHECK 2026-11-01 (complete 281 Java + 73 XML): SURVIVED — greps/grep_recheck_7374_apigate_complete.txt: sole newInstance caller remains Utils:713 behind Utils:704-707 (SDK_INT < R true at API 27); zero hits in missing 29 and in XML. |

## Counts — mechanically verified

- 40 rows, sequence 1–40 intact, in plan order.
- **32 REACHABLE / 3 UNREACHABLE / 5 OPEN.** (Round-2 flips: rows 28, 39, 40 to UNREACHABLE, all INFERRED. REACHABLE split unchanged: SOURCE 13 / INFERRED 19.)
- SOURCE 13 / INFERRED 19 among REACHABLE rows. (Flips: SOURCE +2 rows 26, 30; INFERRED +4 rows 25, 27, 33, 34.)
- **0 rows verified for merge.** Verification requires, in order: the main agent's
  1-in-5 spot-check of this part, `py_compile` + build on a full checkout, and the
  Mac build/C1 return — none of which has happened here.

## OPEN rows and what would resolve them

- Rows 25–36 (FileItem rows) — SUPERSEDED in part by the 2026-11-01 revision (rows 25, 26, 27, 30, 33, 34 flipped to REACHABLE on freshly printed subclass sites) and by round 2 (row 28 flipped to UNREACHABLE no_trigger_in_app on the saved full-tree grep). Still OPEN: rows 29 (describeContents), 31 (hashCode), 32 (toString), 35 (createFromParcel), 36 (newArray) — see the CONDITIONAL flip table below; none was flipped in round 2 because each depends on an undecided project convention or an OPEN dependency.
- Rows 39–40 (ManageAllFilesWarningDialog): CLOSED 2026-11-01 (round 2) to UNREACHABLE closed_by_api_level — see table rows 39–40. The saved full-tree grep (252 files) found exactly one caller, Utils:713, gated off at API 27. A non-gated caller printed later flips rows 39–40 and batch 74 row 1 back to REACHABLE together.


## CONDITIONAL flip table (round 2, 2026-11-01) — NO convention decided here

Saved evidence for all five rows: full-tree greps over all 252 app Java files in `~/workspace/b727374-openclose2-src/full_grep_fileitem_20261101.txt` (FileItem word hits: definition file only + the two subclass `extends` lines; zero plain-FileItem parcel sites; zero explicit hashCode/toString callers on a FileItem receiver; subclass toString super-calls at TorrentContentFileItem:105 and DownloadableFileItem:82). Each row below stays OPEN until the named decision is made; the table states exactly what flips under each option.

- Row 29 FileItem.describeContents + row 35 FileItem$1.createFromParcel + row 36 FileItem$1.newArray (move together as the base-class Parcelable trio): (a) UNDER the full-grep-absence rule used for batch 41's TorrentStream parcel group (no printed parceling site for the class in the 252-file tree ⇒ UNREACHABLE), all three flip together to UNREACHABLE, kind `no_trigger_in_app`, INFERRED — framework calls describeContents / CREATOR only when a plain FileItem is parceled/unparceled, and no such site exists; subclass parceling does not dispatch to the base methods (both subclasses override describeContents and never call super; the SelectionTracker storage at DetailTorrentFilesFragment:227 is for TorrentContentFileItem.class, and its CREATOR is the subclass CREATOR, not FileItem.CREATOR). (b) UNDER the trio-stays-OPEN policy recorded for batches 28–31 (a Parcelable trio stays OPEN without a printed parcel site, and a saved grep alone does not close it), all three stay OPEN. (c) On ONE printed plain-FileItem parceling site (putParcelable/getParcelableExtra/Bundle site passing a FileItem, not a subclass), all three flip together to REACHABLE, INFERRED (framework dispatch; row 27 Parcel ctor is already REACHABLE INFERRED via the subclass super calls and does not change). The merger must apply ONE rule to this trio and to the batch 28–31 / 82 / 92 / 102 / 114 parcel trios — do not flip this trio alone.
- Row 31 FileItem.hashCode: (a) UNDER a hash-backed-library-dispatch decision (androidx MutableSelection/SelectionTracker storage calls hashCode on its keys — TorrentContentFilesAdapter:88 `selectionTracker.isSelected(item)` passes TorrentContentFileItem keys, and neither subclass overrides hashCode, so the inherited FileItem.hashCode at :103–112 would be the dispatched method), flips to REACHABLE, INFERRED. (b) UNDER an explicit-app-caller-only rule (no printed `.hashCode()` call on a FileItem receiver in the 252-file tree; DiffUtil uses `equals`, not hashCode; `getCurrentList().indexOf` uses `equals`), flips to UNREACHABLE, kind `no_trigger_in_app`, INFERRED. The hashCode-dispatch question is the same undecided one recorded for batches 95/99/112 — not decided here.
- Row 32 FileItem.toString: (a) If batch 82 row 13 (DownloadableFileItem.toString) OR batch 92 row 35 (TorrentContentFileItem.toString) flips to REACHABLE, this row flips to REACHABLE, SOURCE — via the printed `super.toString()` calls inside those subclass bodies (DownloadableFileItem:82, TorrentContentFileItem:105). (b) If BOTH subclass toString rows are judged UNREACHABLE and no implicit log/concatenation caller is counted, this row flips to UNREACHABLE, kind `no_trigger_in_app`, INFERRED. While either subclass row stays OPEN, this row stays OPEN under the dependency rule (its only printed callers sit inside OPEN methods). No independent log/concat caller of a FileItem variable exists in the 252-file tree.

## Caveats for the merger

- **FileItem (rows 25–36) is the whole OPEN set apart from rows 39–40.** No
  file-list adapter or other caller file printed in the prior or this session
  names `FileItem` — CORRECTED 2026-11-01: fresh prints show BOTH
  TorrentContentFileItem (TorrentContentFileItem.java:32, extends FileItem) and
  DownloadableFileItem (DownloadableFileItem.java:29, extends FileItem) extend
  FileItem, with printed super calls (see table rows 25-27, 30, 33).
  The highest-value follow-up is a saved full-repo grep for `FileItem`
  (constructor, CREATOR, and `putParcelable`/Bundle use sites) plus a print of
  whichever file-list adapter, if any, uses it. Do not reuse the batch 82
  Parcelable convention to upgrade rows 27/35 without a printed parceling context.
- **ManageAllFilesWarningDialog (rows 39–40, and batch 74 row 1)** is a printed
  API-27 gate lead, not a verdict, for the reason in row 39. The merger must
  run the saved full-repo grep before labelling these rows either way.
- **Lambda numbering** (`$0–$3` in BaseAlertDialog, `$0–$1` in ClipboardDialog)
  is by source order and plan-descriptor match, **not bytecode-verified**.
  A swap within each group would not change any label.
- **Strict-entry:** no caveat for rows 1–24 and 37–38 — launcher entry
  (manifest MAIN/LAUNCHER) and the AddFeedActivity SEND/VIEW entry are both
  printed, and the dialog show sites are printed. Rows 25–36 and 39–40 are
  OPEN regardless of entry rule.
- **Not claimed:** no build, sampler, full-repo grep, or C1 check was run
  (no full local checkout; git clone of the private repo fails in this VM
  with no credential device — named missing check, not passed). No push was
  made. Nothing was edited in `graph_def.py`, `out/`, `PROGRESS_V2`,
  `AGENT_NOTES`, `tools/`, or another agent's files.

## What this part is not

- Not a merge: `graph_def.py` is untouched, and this file is not in `graph_def.py` format.
- Not a claim about batches 1–72, 74–120, about any other app, or about device replay.
- Not a claim that the plan's TODO_CANDIDATE_REACHABLE labels are verified: they
  happen to agree with the proposals here except for the 14 OPEN rows, but
  agreement with the plan is not verification.
