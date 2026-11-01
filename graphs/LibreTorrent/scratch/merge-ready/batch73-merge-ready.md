# LibreTorrent batch 73 — merge-ready part — UNVERIFIED

**Status: UNVERIFIED proposal only. NOT verified for merge. NOT pushed. No edit to
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
| 25 | FileItem.<clinit> ()V | OPEN | — | Definition printed (`FileItem:70–84` static CREATOR), but no printed first active use of the class in any file printed in the prior or this session, so class initialisation is not anchored. Re-checked this session: printed-corpus grep found no external construction site that would initialise the class. NOT UNREACHABLE: needs a saved full-repo grep. |
| 26 | FileItem.<init>(int,String,boolean,long) (ILjava/lang/String;ZJ)V | OPEN | — | Definition printed (`FileItem:39–45`). No printed `new FileItem(...)` site and no printed subclass in any file printed in the prior or this session. Re-checked this session: the only `new FileItem` hits in the printed corpus are CREATOR-internal (row 35). NOT UNREACHABLE without a saved full-repo grep. |
| 27 | FileItem.<init>(Parcel) (Landroid/os/Parcel;)V | OPEN | — | Definition printed (`FileItem:47–53`). Its only printed caller is `FileItem$1.createFromParcel` at `:76`, which itself has no printed framework parceling context (no printed `putParcelable`/Bundle/Intent site for a FileItem). NOT UNREACHABLE without a saved full-repo grep. |
| 28 | FileItem.compareTo (Lorg/proninyaroslav/libretorrent/ui/FileItem;)I | OPEN | — | Definition printed (`FileItem:115–118`). No printed sort site for FileItems. NOT UNREACHABLE without a saved full-repo grep. |
| 29 | FileItem.describeContents ()I | OPEN | — | Definition printed (`FileItem:56–59`). Framework parceling method with no printed parceling context (see row 27). NOT UNREACHABLE without a saved full-repo grep. |
| 30 | FileItem.equals (Ljava/lang/Object;)Z | OPEN | — | Definition printed (`FileItem:87–100`). No printed caller (collection, DiffUtil, or direct). NOT UNREACHABLE without a saved full-repo grep. |
| 31 | FileItem.hashCode ()I | OPEN | — | Definition printed (`FileItem:103–112`). No printed caller. NOT UNREACHABLE without a saved full-repo grep. |
| 32 | FileItem.toString ()Ljava/lang/String; | OPEN | — | Definition printed (`FileItem:121–130`). No printed caller; a logging/concatenation caller is plausible. NOT UNREACHABLE without a saved full-repo grep. |
| 33 | FileItem.writeToParcel (Landroid/os/Parcel;I)V | OPEN | — | Definition printed (`FileItem:62–68`). Framework parceling method with no printed parceling context (see row 27). NOT UNREACHABLE without a saved full-repo grep. |
| 34 | FileItem$1.<init> ()V | OPEN | — | Anonymous CREATOR instance created in the field initialiser at `FileItem:70–84`, which runs only on class initialisation (row 25, itself OPEN). NOT UNREACHABLE without a saved full-repo grep. |
| 35 | FileItem$1.createFromParcel (Landroid/os/Parcel;)Lorg/proninyaroslav/libretorrent/ui/FileItem; | OPEN | — | Body printed (`FileItem:74–77`, calls the Parcel ctor at `:76`), but framework CREATOR dispatch has no printed parceling context (see row 27). Contrast batches 82/92, where a printed SelectionTracker/storage parceling context anchored the equivalent rows — that convention is recorded, NOT adopted here without a printed parceling context. NOT UNREACHABLE without a saved full-repo grep. |
| 36 | FileItem$1.newArray (I)[Lorg/proninyaroslav/libretorrent/ui/FileItem; | OPEN | — | Body printed (`FileItem:80–83`), framework CREATOR dispatch only, no printed parceling context. NOT UNREACHABLE without a saved full-repo grep. |
| 37 | FragmentCallback.<clinit> ()V | REACHABLE proposed | INFERRED | Static `TAG = FragmentCallback.class.getSimpleName()` at `FragmentCallback:33` is non-constant. First printed active use: `AddFeedDialog.finish` casts to `FragmentCallback` at `AddFeedDialog:432` and passes `FragmentCallback.ResultCode` values at `:287/:392/:408/:421/:426`; `AddFeedActivity` implements the interface at `AddFeedActivity:37`. JVM interface initialisation is unprinted dispatch. |
| 38 | FragmentCallback$ResultCode.<clinit> ()V | REACHABLE proposed | INFERRED | Enum constants (OK, CANCEL, BACK) at `FragmentCallback:35–37`; first printed use is the `ResultCode` values passed in `AddFeedDialog.finish` calls (same lines as row 37). |
| 39 | ManageAllFilesWarningDialog.<init> ()V | OPEN | — | Its only printed construction is `new ManageAllFilesWarningDialog()` at `ManageAllFilesWarningDialog:34` inside `newInstance` (row 40), which is itself OPEN. **Closed-by-API-level lead, NOT a verdict:** the only printed `newInstance` caller is `Utils:713`, behind the early return at `Utils:704–707` (`SDK_INT < R` is true on the standard API 27 device, so the method returns before `:713`). Re-checked this session: no non-gated caller in the printed corpus. Per the task rule, OPEN is not flipped to UNREACHABLE without a saved full-repo grep — a grep that finds any non-gated caller flips rows 39–40 (and batch 74 row 1) to REACHABLE; a grep that finds none would support `closed_by_api_level`. Do not conflate with `Utils.showManageAllFilesWarningDialog` itself, which IS reached (`MainActivity:180`, `AddTorrentActivity:136` in other batches) — the method runs, but its dialog branch does not run at API 27. |
| 40 | ManageAllFilesWarningDialog.newInstance ()Lorg/proninyaroslav/libretorrent/ui/ManageAllFilesWarningDialog; | OPEN | — | Definition printed (`ManageAllFilesWarningDialog:33–40`). Only printed caller is `Utils.showManageAllFilesWarningDialog` at `Utils:713`, behind the API-27 early return described in row 39. Same grep caveat as row 39. NOT UNREACHABLE on this evidence. |

## Counts — mechanically verified

- 40 rows, sequence 1–40 intact, in plan order.
- **26 REACHABLE proposed / 0 UNREACHABLE proposed / 14 OPEN.**
- SOURCE 11 / INFERRED 15 among REACHABLE rows.
- **0 rows verified for merge.** Verification requires, in order: the main agent's
  1-in-5 spot-check of this part, `py_compile` + build on a full checkout, and the
  Mac build/C1 return — none of which has happened here.

## OPEN rows and what would resolve them

- Rows 25–36 (all FileItem rows): a saved full-repo grep for `FileItem`
  (constructor, CREATOR, and `putParcelable`/Bundle use sites) plus a print of
  whichever file-list adapter, if any, uses it. A printed parcel/unparcel site
  or a printed `new FileItem` / subclass site flips the corresponding rows to
  REACHABLE; a full-repo grep finding none would then support UNREACHABLE
  judgements — neither is claimed here. Do not reuse the batch 82 Parcelable
  convention to upgrade rows 27/35 without a printed parceling context.
- Rows 39–40 (ManageAllFilesWarningDialog): a saved full-repo grep for
  `ManageAllFilesWarningDialog.newInstance` callers. A non-gated caller flips
  rows 39–40 (and batch 74 row 1) to REACHABLE; no caller would support
  `closed_by_api_level` — neither is claimed here.

## Caveats for the merger

- **FileItem (rows 25–36) is the whole OPEN set apart from rows 39–40.** No
  file-list adapter or other caller file printed in the prior or this session
  names `FileItem`: a grep of the other batch proposals and of the local
  copies found no `new FileItem` or `extends FileItem` site, and
  `DownloadableFileItem` (batch 82) was not shown to extend `FileItem`.
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
