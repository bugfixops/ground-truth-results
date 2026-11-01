# LibreTorrent batch 59 — merge-ready (UNVERIFIED, NOT merged)

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only. Never main or result.
No push made — pushes are held until verified and merged to [L]. No edit to graph_def.py, out/,
PROGRESS_V2, AGENT_NOTES, tools/, or another helper's file.
Build: not run. C1: not run (they run on the user's Mac after a push), never claimed passed.
No sampler or full-repo grep was run. No search_code result was used as evidence for any row,
and no search_code 0 was used as evidence of absence.
True git clone: MISSING check, never passed — a git clone fails in this VM (no credential
device); all source below was fetched via the GitHub connector only, one file at a time
with ~25-30 s pauses. No fresh HTTP 429 was hit in this pass; one transient HTTP 503 on a
single file fetch was followed by a single spaced retry of the remaining files (not a loop).
Prior proposals are leads only — every row below was re-judged from printed source.

## Membership — mechanically verified
Exactly 40 rows, sequence 1-40 intact, in plan order, method + JVM descriptor copied
mechanically from handoff/LIBRETORRENT_BATCH_PLAN.tsv (local copy
~/workspace/agent27-plan.tsv, git blob SHA 0104806dd666c840049b3db52823d4b384fa1c92),
all TODO_CANDIDATE_REACHABLE. Plan labels are candidates, not evidence.
Classes: ActivityFilemanagerDialogBindingImpl (6), ActivityLogBinding (2),
ActivityLogBindingImpl (12), AddTorrentInfoBinding (2), AddTorrentInfoBindingImpl (18).

## Counts — proposed, not verified
- REACHABLE proposed: 23 / 40, all INFERRED (generated-code dispatch)
- UNREACHABLE proposed: 0
- OPEN: 17 / 40
- Verified for merge: 0

## Judging rule used in this file (conventions recorded, NOT decided)
All rows are Android data-binding generated classes. Their bodies and
libretorrent.DataBinderMapperImpl are NOT in final_java_only, so no row here is SOURCE:
every REACHABLE row is INFERRED on a printed inflate/setContentView + setViewModel site
plus a printed layout, with generated mapper/Impl dispatch unprinted.
- Abstract Binding.<init>: REACHABLE INFERRED — runs as the super-call of the Impl ctor.
- Impl <clinit> / <init>(2-arg) / <init>(3-arg): REACHABLE INFERRED — class init on first
  use; the 2-arg Impl ctor is what the generated mapper returns for the printed layout,
  and the generated 2-arg ctor delegates to the 3-arg ctor.
- Impl executeBindings: REACHABLE INFERRED — generated lifecycle callback for the binding
  created at the printed inflate site (wave convention, applied uniformly even to the
  appbar Impl in batch 60; see batch-60 rows 11-12 for where that convention stops).
- Impl setViewModel / setVariable: REACHABLE INFERRED where the printed site sets the
  viewModel AND the layout declares the viewModel variable with @{...} expressions.
- Impl onFieldChange: REACHABLE INFERRED where the printed site sets the viewModel AND
  the layout binds an observable of that viewModel.
- Named Impl onChangeViewModel*: REACHABLE INFERRED where the printed site sets the
  viewModel, the layout binds the named observable, and a change to that observable is
  printed (user interaction with a two-way-bound view, an event handler, or an async
  callback). Batch-59 row 29 is flagged weak on this rule (no info-set site printed).
- Impl hasPendingBindings / invalidateAll: OPEN — no printed caller anywhere in this pass.
- Abstract Binding.getViewModel: OPEN — no printed caller. Convention (v), recorded not
  decided: this file follows batches 58/63/64 (generated executeBindings reads the
  mViewModel field, not the getter). Batches 62/65 and the batch-61 prior proposal use
  the opposite convention (getter read by executeBindings); under that convention the
  getViewModel rows in batches 59-61 flip together to REACHABLE INFERRED. The merger
  must pick ONE convention for all binding getters (including batch 80 row 23 and
  batch 84 row 40, same family).
- Anonymous Impl $N.<init> / $N.onChange: OPEN — Impl bodies unprinted, so no $N row
  can be assigned to a printed observable or change event. Convention recorded not
  decided: this file follows batches 62-64 ($N OPEN). The batch-59/60 prior proposals
  used the opposite convention ($N REACHABLE on executeBindings registration); under
  that convention the $N rows in batches 59-61 flip together to REACHABLE INFERRED.
  $N numbering is generated-class declaration order, NOT bytecode-verified.
- No row is flipped to UNREACHABLE: absence from the printed subset is not evidence,
  and no saved full-repo grep exists for these generated names (rule F/C5 class-name
  grep required before any UNREACHABLE claim).

## Shared routes (printed steps, cited once here and reused by row)
All paths under final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/
org/proninyaroslav/libretorrent/, branch work-2026-10-31, freshly fetched in this pass
(see "Files printed" below), except where a row says otherwise.

**R1 — FileManager dialog/activity binding.**
ui/filemanager/FileManagerDialog.java:142 `binding = DataBindingUtil.setContentView(this, R.layout.activity_filemanager_dialog);`
:143 `binding.setViewModel(viewModel);` (binding field type ActivityFilemanagerDialogBinding).
Layout res/layout/activity_filemanager_dialog.xml declares viewModel (FileManagerViewModel)
and binds viewModel.config.showMode (:74/:94).

**R2 — Log activity binding.**
ui/log/LogActivity.java:93 `binding = DataBindingUtil.setContentView(this, R.layout.activity_log);`
:94 `binding.setViewModel(viewModel);` (binding field type ActivityLogBinding).
Layout res/layout/activity_log.xml declares viewModel (LogViewModel) and two-way-binds
@={viewModel.mutableParams.logging} on the enableLog SwitchBar.
LogActivity.java:172 registers its paramsCallback in onStart; LogViewModel.java:56 declares
mutableParams (a LogMutableParams observable).

**R3 — AddTorrent info included binding.**
ui/addtorrent/AddTorrentInfoFragment.java:93
`binding = DataBindingUtil.inflate(inflater, R.layout.fragment_add_torrent_info, container, false);`
:102-103 viewModel obtained + `binding.setViewModel(viewModel);` (outer binding
FragmentAddTorrentInfoBinding). :104-105 `binding.info.<view>` — the outer binding exposes
field `info` of type AddTorrentInfoBinding, i.e. the included add_torrent_info layout's
binding object exists once the fragment layout is inflated.
Layout res/layout/add_torrent_info.xml declares viewModel (AddTorrentViewModel) and binds
viewModel.info.* and viewModel.mutableParams.* expressions.

## Per-method table (all 40 rows, in plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|

| 1 | ActivityFilemanagerDialogBindingImpl.executeBindings ()V | REACHABLE proposed | INFERRED | R1: FileManagerDialog.java:142 setContentView(activity_filemanager_dialog) + :143 setViewModel; executeBindings is the generated lifecycle callback for the binding created there. |
| 2 | ActivityFilemanagerDialogBindingImpl.hasPendingBindings ()Z | OPEN | — | No printed caller. Generated Impl body unprinted; hasPendingBindings is a framework-internal query. Resolves with a printed call site or printed generated Impl body showing an internal caller. NOT UNREACHABLE (no saved full-repo grep). |
| 3 | ActivityFilemanagerDialogBindingImpl.invalidateAll ()V | OPEN | — | No printed caller. Same resolver as row 2. |
| 4 | ActivityFilemanagerDialogBindingImpl.onFieldChange (ILjava/lang/Object;I)Z | REACHABLE proposed | INFERRED | R1: setViewModel printed (:143) and layout binds viewModel.config.showMode (activity_filemanager_dialog.xml:74/:94); onFieldChange is the generated observable-change callback for that binding. Generated dispatch unprinted, hence INFERRED. |
| 5 | ActivityFilemanagerDialogBindingImpl.setVariable (ILjava/lang/Object;)Z | REACHABLE proposed | INFERRED | R1: generated setViewModel (:143 dispatch) calls setVariable(BR.viewModel, …); layout declares the viewModel variable (activity_filemanager_dialog.xml:8). |
| 6 | ActivityFilemanagerDialogBindingImpl.setViewModel (Lorg/proninyaroslav/libretorrent/ui/filemanager/FileManagerViewModel;)V | REACHABLE proposed | INFERRED | R1: FileManagerDialog.java:143 `binding.setViewModel(viewModel)` dispatches to this Impl method (generated dispatch, hence INFERRED). |
| 7 | ActivityLogBinding.<init> (Ljava/lang/Object;Landroid/view/View;ILandroid/widget/RelativeLayout;Landroid/widget/TextView;Lorg/proninyaroslav/libretorrent/ui/customviews/SwitchBar;Lcom/google/android/material/floatingactionbutton/FloatingActionButton;Lcom/google/android/material/floatingactionbutton/FloatingActionButton;Lorg/proninyaroslav/libretorrent/ui/customviews/EmptyRecyclerView;Landroid/widget/RelativeLayout;)V | REACHABLE proposed | INFERRED | R2: super-call of ActivityLogBindingImpl ctor, reached via LogActivity.java:93 setContentView. |
| 8 | ActivityLogBinding.getViewModel ()Lorg/proninyaroslav/libretorrent/ui/log/LogViewModel; | OPEN | — | No printed caller; LogActivity.java uses binding.rootLayout/logList/fab fields, never getViewModel. Resolves with a printed caller. Convention (v): flips to REACHABLE INFERRED only if the merger adopts the executeBindings-reads-getter convention used in batches 62/65; this file follows the batch 58/63/64 convention (executeBindings reads the mViewModel field, not the getter). |
| 9 | ActivityLogBindingImpl.<clinit> ()V | REACHABLE proposed | INFERRED | R2: first use is LogActivity.java:93 (setContentView for activity_log); class-init timing is the unprinted JVM rule. |
| 10 | ActivityLogBindingImpl.<init>(DataBindingComponent,View) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V | REACHABLE proposed | INFERRED | R2: generated mapper return for the activity_log layout inflated at LogActivity.java:93. |
| 11 | ActivityLogBindingImpl.<init>(DataBindingComponent,View,Object[]) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V | REACHABLE proposed | INFERRED | R2: generated 2-arg ctor delegates to this 3-arg ctor (generated code, unprinted). |
| 12 | ActivityLogBindingImpl.executeBindings ()V | REACHABLE proposed | INFERRED | R2: generated lifecycle callback for the binding created at LogActivity.java:93. |
| 13 | ActivityLogBindingImpl.hasPendingBindings ()Z | OPEN | — | No printed caller. Same resolver as row 2. |
| 14 | ActivityLogBindingImpl.invalidateAll ()V | OPEN | — | No printed caller. Same resolver as row 2. |
| 15 | ActivityLogBindingImpl.onChangeViewModelMutableParams (Lorg/proninyaroslav/libretorrent/ui/log/LogMutableParams;I)Z | REACHABLE proposed | INFERRED | R2, STRENGTHENED vs prior proposal by fresh layout evidence: activity_log.xml declares viewModel (LogViewModel) and two-way-binds @={viewModel.mutableParams.logging} on the enableLog SwitchBar; toggling that switch after the activity shows calls mutableParams.setLogging, which notifies, firing this generated callback. LogActivity.java:172 registers its own paramsCallback in onStart, and LogViewModel.java:56 declares mutableParams. Dispatch to the Impl callback is generated, hence INFERRED. |
| 16 | ActivityLogBindingImpl.onFieldChange (ILjava/lang/Object;I)Z | REACHABLE proposed | INFERRED | R2: setViewModel printed (:94) binds observables (mutableParams.logging two-way binding, activity_log.xml); onFieldChange is the generated callback. INFERRED (generated dispatch). |
| 17 | ActivityLogBindingImpl.setVariable (ILjava/lang/Object;)Z | REACHABLE proposed | INFERRED | R2: generated setViewModel (:94 dispatch) calls setVariable. |
| 18 | ActivityLogBindingImpl.setViewModel (Lorg/proninyaroslav/libretorrent/ui/log/LogViewModel;)V | REACHABLE proposed | INFERRED | R2: LogActivity.java:94 `binding.setViewModel(viewModel)` dispatches to this Impl method. |
| 19 | ActivityLogBindingImpl$1.<init> (Lorg/proninyaroslav/libretorrent/databinding/ActivityLogBindingImpl;)V | OPEN | — | Impl body unprinted; which observable $1 registers for is unprinted, and no printed change event is assignable to $1. $ numbering is generated-class declaration order, NOT bytecode-verified. Resolves with printed generated Impl body. NOT UNREACHABLE (no saved full-repo grep). Convention: this file follows batches 62-64 ($N OPEN); under the batch-59-proposal registration convention these rows would flip to REACHABLE INFERRED — merger must pick one $N convention project-wide. |
| 20 | ActivityLogBindingImpl$1.onChange ()V | OPEN | — | Same as row 19; no printed change event assignable to $1.onChange. |
| 21 | AddTorrentInfoBinding.<init> (Ljava/lang/Object;Landroid/view/View;ILandroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/CheckBox;Landroid/widget/TextView;Landroid/widget/ImageButton;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/TextView;Landroid/widget/CheckBox;Landroid/widget/LinearLayout;Lcom/google/android/material/textfield/TextInputLayout;Landroid/widget/LinearLayout;Landroid/widget/LinearLayout;Landroid/widget/LinearLayout;Lcom/google/android/material/textfield/TextInputEditText;Landroid/widget/TextView;Landroid/widget/CheckBox;Landroid/widget/TextView;Landroid/widget/CheckBox;Lorg/proninyaroslav/libretorrent/ui/tag/TorrentTagsList;Landroid/widget/TextView;)V | REACHABLE proposed | INFERRED | R3: super-call of AddTorrentInfoBindingImpl ctor, reached via AddTorrentInfoFragment.java:93 inflate + :104 binding.info access. |
| 22 | AddTorrentInfoBinding.getViewModel ()Lorg/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentViewModel; | OPEN | — | No printed caller; AddTorrentInfoFragment.java uses binding.info.<view> fields, never getViewModel. Same convention (v) note as row 8. |
| 23 | AddTorrentInfoBindingImpl.<clinit> ()V | REACHABLE proposed | INFERRED | R3: first use is the included binding created during AddTorrentInfoFragment.java:93 inflate; class-init timing unprinted. |
| 24 | AddTorrentInfoBindingImpl.<init>(DataBindingComponent,View) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V | REACHABLE proposed | INFERRED | R3: generated mapper/included-binding creation for add_torrent_info during the fragment inflate (:93), evidenced by binding.info (:104). |
| 25 | AddTorrentInfoBindingImpl.<init>(DataBindingComponent,View,Object[]) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V | REACHABLE proposed | INFERRED | R3: generated 2-arg ctor delegates to this 3-arg ctor (generated code, unprinted). |
| 26 | AddTorrentInfoBindingImpl.executeBindings ()V | REACHABLE proposed | INFERRED | R3: generated lifecycle callback for the included binding created at :93. |
| 27 | AddTorrentInfoBindingImpl.hasPendingBindings ()Z | OPEN | — | No printed caller. Same resolver as batch-59 row 2. |
| 28 | AddTorrentInfoBindingImpl.invalidateAll ()V | OPEN | — | No printed caller. Same resolver as batch-59 row 2. |
| 29 | AddTorrentInfoBindingImpl.onChangeViewModelInfo (Landroidx/databinding/ObservableField;I)Z | REACHABLE proposed | INFERRED | R3, WEAK FLAG: outer binding setViewModel printed (:103) and add_torrent_info.xml binds viewModel.info.* expressions (:151/:178/:214/:236/:247/:259/:269/:285/:309), so the generated Impl registers this callback for the info observable; but the AddTorrentViewModel info-set site itself was NOT printed in this pass (AddTorrentViewModel.java not fetched). Reverts to OPEN if the merger requires a printed info-set site. INFERRED (generated dispatch). |
| 30 | AddTorrentInfoBindingImpl.onChangeViewModelMutableParams (Lorg/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentMutableParams;I)Z | REACHABLE proposed | INFERRED | R3: outer binding setViewModel printed (:103); add_torrent_info.xml binds viewModel.mutableParams.* (:73/:187); and a post-binding change IS printed — AddTorrentInfoFragment.java:160 `viewModel.mutableParams.getDirPath().set(data.getData())` in the chooseDir activity-result handler. INFERRED (generated dispatch). |
| 31 | AddTorrentInfoBindingImpl.onFieldChange (ILjava/lang/Object;I)Z | REACHABLE proposed | INFERRED | R3: setViewModel printed (:103) binds observables (info + mutableParams, add_torrent_info.xml); onFieldChange is the generated callback. INFERRED. |
| 32 | AddTorrentInfoBindingImpl.setVariable (ILjava/lang/Object;)Z | REACHABLE proposed | INFERRED | R3: generated setViewModel propagation calls setVariable on the included binding. |
| 33 | AddTorrentInfoBindingImpl.setViewModel (Lorg/proninyaroslav/libretorrent/ui/addtorrent/AddTorrentViewModel;)V | REACHABLE proposed | INFERRED | R3: viewModel propagation from the outer binding's printed setViewModel (:103) to the included binding (generated code). |
| 34 | AddTorrentInfoBindingImpl$1.<init> (Lorg/proninyaroslav/libretorrent/databinding/AddTorrentInfoBindingImpl;)V | OPEN | — | Same $N rule as row 19 (batch 62-64 convention). No printed observable assignment for $1. |
| 35 | AddTorrentInfoBindingImpl$1.onChange ()V | OPEN | — | Same as row 34; no printed change event assignable to $1.onChange. |
| 36 | AddTorrentInfoBindingImpl$2.<init> (Lorg/proninyaroslav/libretorrent/databinding/AddTorrentInfoBindingImpl;)V | OPEN | — | Same $N rule as row 19. No printed observable assignment for $2. |
| 37 | AddTorrentInfoBindingImpl$2.onChange ()V | OPEN | — | Same as row 36; no printed change event assignable to $2.onChange. |
| 38 | AddTorrentInfoBindingImpl$3.<init> (Lorg/proninyaroslav/libretorrent/databinding/AddTorrentInfoBindingImpl;)V | OPEN | — | Same $N rule as row 19. No printed observable assignment for $3. |
| 39 | AddTorrentInfoBindingImpl$3.onChange ()V | OPEN | — | Same as row 38; no printed change event assignable to $3.onChange. |
| 40 | AddTorrentInfoBindingImpl$4.<init> (Lorg/proninyaroslav/libretorrent/databinding/AddTorrentInfoBindingImpl;)V | OPEN | — | Same $N rule as row 19. No printed observable assignment for $4 (its onChange is batch 60 row 1, also OPEN here). |

- **23 REACHABLE proposed / 0 UNREACHABLE proposed / 17 OPEN.**

## OPEN rows and what would resolve them (17 rows)
- Rows 2, 3, 13, 14, 27, 28 (hasPendingBindings / invalidateAll): a printed call site,
  or a printed generated Impl body showing an internal caller.
- Rows 8, 22 (abstract getViewModel): a printed caller of the getter, or a merger
  decision adopting the executeBindings-reads-getter convention (then both flip to
  REACHABLE INFERRED together with batches 60/61 getViewModel rows).
- Rows 19, 20, 34, 35, 36, 37, 38, 39, 40 ($N <init>/onChange): a printed generated Impl
  body assigning each $N to an observable, or a merger decision adopting the
  registration convention (then all $N rows in batches 59-61 flip to REACHABLE INFERRED).
- General resolver: printed generated mapper/Impl bodies, or a saved full-repo grep in
  rule-F/C5 form over generated binding sources. No OPEN row may be flipped to
  UNREACHABLE on the basis of not being found in the printed subset.

## Caveats restated
1. Strict-entry caveat: every REACHABLE row is anchored at a printed inflate/setContentView
   + setViewModel site, NOT at the launcher. Who starts FileManagerDialog / LogActivity /
   AddTorrentInfoFragment was not printed in this session; under a strict launcher-entry
   rule all 23 REACHABLE rows revert to OPEN.
2. Mapper caveat: DataBinderMapperImpl selection (layout id -> Impl class) was not printed
   and is not in final_java_only. If the merger requires a printed mapper step, all Impl
   rows revert to OPEN (the batch-17 position).
3. Anonymous $N numbering and the generated 2-arg -> 3-arg ctor delegation are
   generated-code inferences, not bytecode-verified.
4. Batch-59 row 29 (onChangeViewModelInfo) is the weakest REACHABLE row: no AddTorrentViewModel
   info-set site was printed in this pass; it reverts to OPEN if the merger requires one.
5. No row in this file is verified for merge: no build, sampler, grep, or C1 check was run.
   A merge step must re-derive every row from a full checkout, run the C1 checks, and
   spot-check at least 1 in 5 citations.

## Files printed (fresh, branch work-2026-10-31, saved in ~/workspace/b596061-src/)
- ui/filemanager/FileManagerDialog.java — SHA 19c4b6e5f9d6, 692 lines (binding :142-143)
- ui/log/LogActivity.java — SHA 6c8af391d966, 471 lines (binding :93-94, paramsCallback :172)
- ui/log/LogViewModel.java — SHA ab1c1caa08b8, 228 lines (mutableParams :56)
- ui/addtorrent/AddTorrentInfoFragment.java — SHA e8175fb22117, 244 lines (binding :93/:102-105, dirPath.set :160)
- res/layout/activity_filemanager_dialog.xml — SHA 5d5e877794e5, 113 lines (viewModel variable, config expressions :74/:94)
- res/layout/activity_log.xml — SHA 1eb00a71ac96, 80 lines (viewModel variable, two-way mutableParams.logging)
- res/layout/add_torrent_info.xml — SHA 73b010cd2d4b, 313 lines (viewModel variable, info/mutableParams expressions)
- handoff/LIBRETORRENT_BATCH_PLAN.tsv — local copy ~/workspace/agent27-plan.tsv (plan SHA above)
