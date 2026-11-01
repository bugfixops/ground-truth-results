# LibreTorrent batch 60 — merge-ready (UNVERIFIED, NOT merged)

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
Row 1 continues batch 59: AddTorrentInfoBindingImpl$4.onChange.
Classes: AddTorrentInfoBindingImpl$4/$5 (3), DetailTorrentAppbarBinding (1),
DetailTorrentAppbarBindingImpl (8), DetailTorrentAppbarBindingLargeLandNotouchImpl (8),
DetailTorrentAppbarBindingSw600dpLandImpl (8), DialogAddFeedChannelBinding (2),
DialogAddFeedChannelBindingImpl (10).

## Counts — proposed, not verified
- REACHABLE proposed: 14 / 40, all INFERRED (generated-code dispatch)
- UNREACHABLE proposed: 0
- OPEN: 26 / 40
- Verified for merge: 0

## Judging rule used in this file (conventions recorded, NOT decided)
Same rule as batch 59 (see that file): generated Impl dispatch is INFERRED, never SOURCE;
hasPendingBindings / invalidateAll are OPEN (no printed caller); abstract getViewModel is
OPEN under convention (v) (batch 58/63/64 reading; flips with all other binding getters
if the merger adopts the batch 62/65 reading); anonymous $N rows are OPEN under the
batch 62-64 convention (flips together with batches 59/61 $N rows if the merger adopts
the batch-59/60-proposal registration convention); no row is flipped to UNREACHABLE
without a saved full-repo grep (rule F/C5).
Two batch-60-specific points, both decided on FRESH layout evidence in this pass:
- Base appbar Impl onFieldChange / setVariable (rows 11-12) are OPEN, changed from the
  prior proposal's REACHABLE: freshly printed res/layout/detail_torrent_appbar.xml
  (29 lines) declares NO <data> block and NO @{...} expressions — only a Toolbar and a
  TabLayout with static attributes. A variable/observable row cannot run without a
  variable/observable. The appbar Impl creation/lifecycle rows (5-8) still stand on the
  printed inflate + <include>, under the wave convention that executeBindings stands on
  a printed inflate; if the merger instead requires a bound expression for executeBindings
  too, row 8 flips to OPEN with rows 11-12.
- Config-qualified appbar Impls (rows 13-28) stay OPEN, as in the prior proposal.
  Convention (iv), recorded not decided: they are selected only under matching device
  configurations (large-land-notouch, sw600dp-land). Under a single fixed portrait-phone
  config they are candidates for UNREACHABLE closed_by_configuration — but that config
  was NOT printed in this pass, so it is not claimed here; do NOT flip them on the
  default-phone argument alone.

## Shared routes (printed steps, cited once here and reused by row)
All paths under final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/
org/proninyaroslav/libretorrent/, branch work-2026-10-31, freshly fetched in this pass
(see "Files printed" below). Batch-59 route R3 (AddTorrentInfo) is reused for rows 1-3;
see the batch-59 file for its full citations.

**R4 — Detail fragment appbar binding (base variant only).**
ui/detailtorrent/DetailTorrentFragment.java:150
`binding = DataBindingUtil.inflate(inflater, R.layout.fragment_detail_torrent, container, false);`
(outer binding FragmentDetailTorrentBinding). :171 `binding.appbar.toolbar.inflateMenu(…)`,
:172/:174/:178/:188 binding.appbar.toolbar/tabLayout uses — the outer binding exposes
field `appbar` of type DetailTorrentAppbarBinding, so the included detail_torrent_appbar
layout's binding object exists once the fragment layout is inflated (confirmed by
res/layout/fragment_detail_torrent.xml:10-12 <include layout="@layout/detail_torrent_appbar"
android:id="@+id/appbar">). Its runtime Impl for the default configuration is
DetailTorrentAppbarBindingImpl; creation and field access are generated code, hence INFERRED.
DetailTorrentActivity itself was NOT re-printed here and is not claimed as evidence
(the prior proposal printed it using plain setContentView, not binding the appbar).

**R5 — Add-feed dialog binding.**
ui/addfeed/AddFeedDialog.java:202
`binding = DataBindingUtil.inflate(i, R.layout.dialog_add_feed_channel, null, false);`
:203 `binding.setViewModel(viewModel);` (binding field type DialogAddFeedChannelBinding).
Layout res/layout/dialog_add_feed_channel.xml declares viewModel (AddFeedViewModel) and
binds viewModel.showClipboardButton (:69) and viewModel.mutableParams.* (:87/:96/:153).

## Per-method table (all 40 rows, in plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|

| 1 | AddTorrentInfoBindingImpl$4.onChange ()V | OPEN | — | Same $N rule as batch-59 row 19 (batch 62-64 convention): Impl body unprinted, no printed observable assignment for $4.onChange. Under the batch-59/60-proposal registration convention this row would flip to REACHABLE INFERRED — merger must pick one $N convention project-wide. (Its <init> is batch-59 row 40, also OPEN here.) |
| 2 | AddTorrentInfoBindingImpl$5.<init> (Lorg/proninyaroslav/libretorrent/databinding/AddTorrentInfoBindingImpl;)V | OPEN | — | Same $N rule as batch-59 row 19. No printed observable assignment for $5. |
| 3 | AddTorrentInfoBindingImpl$5.onChange ()V | OPEN | — | Same as row 2; no printed change event assignable to $5.onChange. |
| 4 | DetailTorrentAppbarBinding.<init> (Ljava/lang/Object;Landroid/view/View;ILcom/google/android/material/tabs/TabLayout;Landroidx/appcompat/widget/Toolbar;)V | REACHABLE proposed | INFERRED | R4: super-call of DetailTorrentAppbarBindingImpl ctor, reached via DetailTorrentFragment.java:150 inflate + :171 binding.appbar access. |
| 5 | DetailTorrentAppbarBindingImpl.<clinit> ()V | REACHABLE proposed | INFERRED | R4: first use is the included appbar binding created during DetailTorrentFragment.java:150 inflate (fragment_detail_torrent.xml:10-12 <include layout="@layout/detail_torrent_appbar" android:id="@+id/appbar">); class-init timing unprinted. |
| 6 | DetailTorrentAppbarBindingImpl.<init>(DataBindingComponent,View) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V | REACHABLE proposed | INFERRED | R4: generated mapper/included-binding creation for detail_torrent_appbar (default config) during the fragment inflate (:150), evidenced by binding.appbar (:171). |
| 7 | DetailTorrentAppbarBindingImpl.<init>(DataBindingComponent,View,Object[]) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V | REACHABLE proposed | INFERRED | R4: generated 2-arg ctor delegates to this 3-arg ctor (generated code, unprinted). |
| 8 | DetailTorrentAppbarBindingImpl.executeBindings ()V | REACHABLE proposed | INFERRED | R4: generated lifecycle callback for the included binding created at :150. (Wave convention: executeBindings stands on the printed inflate even though this layout declares no expressions; see rows 11-12 for the contrasting variable/observable rows.) |
| 9 | DetailTorrentAppbarBindingImpl.hasPendingBindings ()Z | OPEN | — | No printed caller. Same resolver as batch-59 row 2. |
| 10 | DetailTorrentAppbarBindingImpl.invalidateAll ()V | OPEN | — | No printed caller. Same resolver as batch-59 row 2. |
| 11 | DetailTorrentAppbarBindingImpl.onFieldChange (ILjava/lang/Object;I)Z | OPEN | — | CHANGED vs prior proposal (which marked this REACHABLE): fresh detail_torrent_appbar.xml (29 lines) declares NO <data> block and NO @{...} expressions — only a Toolbar and a TabLayout with static attributes. With no variable and no observable bound, no observable registration exists for onFieldChange to fire on. Resolves with a layout variant that binds an observable, or a printed generated Impl body showing a registration. NOT UNREACHABLE (no saved full-repo grep; and the class is still created, rows 5-8). |
| 12 | DetailTorrentAppbarBindingImpl.setVariable (ILjava/lang/Object;)Z | OPEN | — | CHANGED vs prior proposal (which marked this REACHABLE): same fresh layout evidence as row 11 — with no <data> variable declared, the generated outer Impl has no variable to propagate to this included binding via setVariable. Resolves as row 11. NOT UNREACHABLE (no saved full-repo grep). |
| 13 | DetailTorrentAppbarBindingLargeLandNotouchImpl.<clinit> ()V | OPEN | — | Config-qualified variant (LargeLandNotouch): no printed mapper/layout-selection step and no printed standard-device configuration selects this variant, so it stays OPEN — NOT UNREACHABLE (a large-screen landscape device could select it) and NOT REACHABLE (the default phone configuration selects the base Impl, rows 5-8). Resolver: printed DataBinderMapperImpl layout-selection step, or the variant layout XML + standard API 27 device config, or a saved full-repo grep. Convention (iv), recorded not decided: under a single fixed portrait-phone config these rows are candidates for UNREACHABLE closed_by_configuration — that config was NOT printed in this pass, so it is not claimed here. |
| 14 | DetailTorrentAppbarBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V | OPEN | — | Same as row 13. |
| 15 | DetailTorrentAppbarBindingLargeLandNotouchImpl.<init>(DataBindingComponent,View,Object[]) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V | OPEN | — | Same as row 13. |
| 16 | DetailTorrentAppbarBindingLargeLandNotouchImpl.executeBindings ()V | OPEN | — | Same as row 13. |
| 17 | DetailTorrentAppbarBindingLargeLandNotouchImpl.hasPendingBindings ()Z | OPEN | — | Same as row 13 (also no printed caller, as with all hasPendingBindings rows). |
| 18 | DetailTorrentAppbarBindingLargeLandNotouchImpl.invalidateAll ()V | OPEN | — | Same as row 13 (also no printed caller, as with all invalidateAll rows). |
| 19 | DetailTorrentAppbarBindingLargeLandNotouchImpl.onFieldChange (ILjava/lang/Object;I)Z | OPEN | — | Same as row 13. |
| 20 | DetailTorrentAppbarBindingLargeLandNotouchImpl.setVariable (ILjava/lang/Object;)Z | OPEN | — | Same as row 13. |
| 21 | DetailTorrentAppbarBindingSw600dpLandImpl.<clinit> ()V | OPEN | — | Config-qualified variant (Sw600dpLand): same as row 13, for the sw600dp-land variant. |
| 22 | DetailTorrentAppbarBindingSw600dpLandImpl.<init>(DataBindingComponent,View) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V | OPEN | — | Same as row 21. |
| 23 | DetailTorrentAppbarBindingSw600dpLandImpl.<init>(DataBindingComponent,View,Object[]) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V | OPEN | — | Same as row 21. |
| 24 | DetailTorrentAppbarBindingSw600dpLandImpl.executeBindings ()V | OPEN | — | Same as row 21. |
| 25 | DetailTorrentAppbarBindingSw600dpLandImpl.hasPendingBindings ()Z | OPEN | — | Same as row 21 (also no printed caller). |
| 26 | DetailTorrentAppbarBindingSw600dpLandImpl.invalidateAll ()V | OPEN | — | Same as row 21 (also no printed caller). |
| 27 | DetailTorrentAppbarBindingSw600dpLandImpl.onFieldChange (ILjava/lang/Object;I)Z | OPEN | — | Same as row 21. |
| 28 | DetailTorrentAppbarBindingSw600dpLandImpl.setVariable (ILjava/lang/Object;)Z | OPEN | — | Same as row 21. |
| 29 | DialogAddFeedChannelBinding.<init> (Ljava/lang/Object;Landroid/view/View;ILandroid/widget/CheckBox;Landroid/widget/ImageButton;Landroid/view/View;Landroid/widget/CheckBox;Lnet/cachapa/expandablelayout/ExpandableLayout;Lcom/google/android/material/textfield/TextInputEditText;Lcom/google/android/material/textfield/TextInputLayout;Lcom/google/android/material/textfield/TextInputLayout;Lcom/google/android/material/textfield/TextInputLayout;Lcom/google/android/material/textfield/TextInputEditText;Lcom/google/android/material/textfield/TextInputEditText;Landroid/widget/CheckBox;)V | REACHABLE proposed | INFERRED | R5: super-call of DialogAddFeedChannelBindingImpl ctor, reached via AddFeedDialog.java:202 inflate. |
| 30 | DialogAddFeedChannelBinding.getViewModel ()Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedViewModel; | OPEN | — | No printed caller; AddFeedDialog.java uses binding.setViewModel (:203) and binding.getRoot (:207/:255), never getViewModel. Same convention (v) note as batch-59 row 8. |
| 31 | DialogAddFeedChannelBindingImpl.<clinit> ()V | REACHABLE proposed | INFERRED | R5: first use is AddFeedDialog.java:202 (inflate for dialog_add_feed_channel); class-init timing unprinted. |
| 32 | DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V | REACHABLE proposed | INFERRED | R5: generated mapper return for the dialog_add_feed_channel layout inflated at AddFeedDialog.java:202. |
| 33 | DialogAddFeedChannelBindingImpl.<init>(DataBindingComponent,View,Object[]) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V | REACHABLE proposed | INFERRED | R5: generated 2-arg ctor delegates to this 3-arg ctor (generated code, unprinted). |
| 34 | DialogAddFeedChannelBindingImpl.executeBindings ()V | REACHABLE proposed | INFERRED | R5: generated lifecycle callback for the binding created at :202. |
| 35 | DialogAddFeedChannelBindingImpl.hasPendingBindings ()Z | OPEN | — | No printed caller. Same resolver as batch-59 row 2. |
| 36 | DialogAddFeedChannelBindingImpl.invalidateAll ()V | OPEN | — | No printed caller. Same resolver as batch-59 row 2. |
| 37 | DialogAddFeedChannelBindingImpl.onChangeViewModelMutableParams (Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedMutableParams;I)Z | REACHABLE proposed | INFERRED | R5: AddFeedDialog.java:203 setViewModel binds AddFeedViewModel; dialog_add_feed_channel.xml binds viewModel.mutableParams.* (:87/:96/:153); and a post-registration change IS printed — AddFeedViewModel.java fetchParams subscribe handler sets mutableParams url/name/autoDownload/filter/regexFilter (:156-160, async repo callback, after dialog creation). INFERRED (generated dispatch). |
| 38 | DialogAddFeedChannelBindingImpl.onChangeViewModelShowClipboardButton (Landroidx/databinding/ObservableBoolean;I)Z | REACHABLE proposed | INFERRED | R5: dialog_add_feed_channel.xml binds @{viewModel.showClipboardButton ? …} (:69); and a post-registration change IS printed — AddFeedDialog.java initLayoutView calls switchClipboardButton() (:253, after :203 setViewModel), which sets viewModel.showClipboardButton (:118) via clipListener (:110) / onFocusChanged (:113). INFERRED (generated dispatch). |
| 39 | DialogAddFeedChannelBindingImpl.onFieldChange (ILjava/lang/Object;I)Z | REACHABLE proposed | INFERRED | R5: setViewModel printed (:203) binds observables (mutableParams + showClipboardButton, dialog_add_feed_channel.xml); onFieldChange is the generated callback. INFERRED. |
| 40 | DialogAddFeedChannelBindingImpl.setVariable (ILjava/lang/Object;)Z | REACHABLE proposed | INFERRED | R5: generated setViewModel (:203 dispatch) calls setVariable. (Impl setViewModel itself is batch-61 row 1.) |

- **14 REACHABLE proposed / 0 UNREACHABLE proposed / 26 OPEN.**

## OPEN rows and what would resolve them (26 rows)
- Rows 1, 2, 3 ($N): a printed generated Impl body assigning each $N to an observable,
  or a merger decision adopting the registration convention (then these flip to
  REACHABLE INFERRED together with batches 59/61 $N rows).
- Rows 9, 10, 35, 36 (hasPendingBindings / invalidateAll): a printed call site, or a
  printed generated Impl body showing an internal caller.
- Rows 11, 12 (base appbar onFieldChange / setVariable): a layout variant of
  detail_torrent_appbar that declares a <data> variable / binds an observable, or a
  printed generated Impl body showing a registration/variable propagation.
- Rows 13-28 (config-qualified appbar Impls): a printed mapper layout-selection step,
  the variant layout XML + standard-device config, or a saved full-repo grep
  establishing variant use. Do NOT flip these to UNREACHABLE on the default-phone
  argument alone — configuration selection is a printed-evidence question, and the
  standard device config was not printed in this session.
- Row 30 (abstract getViewModel): a printed caller, or a merger decision adopting the
  executeBindings-reads-getter convention (then it flips with all other binding getters).
- General resolver: printed generated mapper/Impl bodies, or a saved full-repo grep in
  rule-F/C5 form over generated binding sources. No OPEN row may be flipped to
  UNREACHABLE on the basis of not being found in the printed subset.

## Caveats restated
1. Strict-entry caveat: every REACHABLE row is anchored at a printed inflate site, NOT at
   the launcher. Who shows DetailTorrentFragment / AddFeedDialog / AddTorrentInfoFragment
   was not printed in this session; under a strict launcher-entry rule all 14 REACHABLE
   rows revert to OPEN.
2. Mapper caveat: DataBinderMapperImpl selection was not printed and is not in
   final_java_only. If the merger requires a printed mapper step, all Impl rows revert
   to OPEN (the batch-17 position).
3. Row 8 flag: DetailTorrentAppbarBindingImpl.executeBindings stands on the printed
   inflate under the wave convention; if the merger requires a bound expression for
   executeBindings too, row 8 flips to OPEN with rows 11-12 (the appbar layout binds
   nothing).
4. Anonymous $N numbering and the generated 2-arg -> 3-arg ctor delegation are
   generated-code inferences, not bytecode-verified.
5. No row in this file is verified for merge: no build, sampler, grep, or C1 check was run.
   A merge step must re-derive every row from a full checkout, run the C1 checks, and
   spot-check at least 1 in 5 citations.

## Files printed (fresh, branch work-2026-10-31, saved in ~/workspace/b596061-src/)
- ui/detailtorrent/DetailTorrentFragment.java — SHA cf768af003d1, 833 lines (binding :150/:171-188)
- ui/addfeed/AddFeedDialog.java — SHA 6b35d852849a, 435 lines (binding :202-203, switchClipboardButton :118/:253)
- ui/addfeed/AddFeedViewModel.java — SHA fb906d6eb61d, 221 lines (mutableParams :48, fetchParams setters :156-160, showClipboardButton :49)
- res/layout/fragment_detail_torrent.xml — SHA 6f6485366b20, 22 lines (<include detail_torrent_appbar :10-12)
- res/layout/detail_torrent_appbar.xml — SHA eabab26c96df, 29 lines (NO <data>, NO @{...} expressions)
- res/layout/dialog_add_feed_channel.xml — SHA 08ece079dd1b, 158 lines (viewModel variable, showClipboardButton :69, mutableParams :87/:96/:153)
- Batch-59 route R3 files (AddTorrentInfoFragment, add_torrent_info.xml) — see batch-59 file
- handoff/LIBRETORRENT_BATCH_PLAN.tsv — local copy ~/workspace/agent27-plan.tsv (plan SHA above)
