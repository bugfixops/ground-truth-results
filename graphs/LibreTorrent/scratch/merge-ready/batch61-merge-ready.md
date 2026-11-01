# LibreTorrent batch 61 — merge-ready (UNVERIFIED, NOT merged)

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
Classes: DialogAddFeedChannelBindingImpl (rows 1-13, tail of that Impl),
DialogAddLinkBinding + DialogAddLinkBindingImpl (rows 14-28),
DialogAddTagBinding + DialogAddTagBindingImpl (rows 29-40).

## Counts — proposed, not verified
- REACHABLE proposed: 20 / 40, all INFERRED (generated-code dispatch)
- UNREACHABLE proposed: 0
- OPEN: 20 / 40
- Verified for merge: 0

## Judging rule used in this file (conventions recorded, NOT decided)
Same rule as batch 59 (see that file): generated Impl dispatch is INFERRED, never SOURCE;
hasPendingBindings / invalidateAll are OPEN (no printed caller); abstract getViewModel is
OPEN under convention (v) (batch 58/63/64 reading — rows 15 and 30 are CHANGED from the
prior proposal's REACHABLE on this convention, and flip back together with all other
binding getters if the merger adopts the batch 62/65 reading); anonymous $N rows are OPEN
under the batch 62-64 convention (as in the prior proposal for this batch); no row is
flipped to UNREACHABLE without a saved full-repo grep (rule F/C5).
Named onChange rows here are STRENGTHENED vs the prior proposal by fresh layout evidence:
dialog_add_link.xml two-way-binds @={viewModel.link} and binds showClipboardButton, and
dialog_add_tag.xml two-way-binds @={viewModel.state.name} with AddTagState setters that
notifyPropertyChanged — so post-registration changes for rows 22, 23 and 37 are printed,
not merely registered. Row 37 in particular closes the prior proposal's own revert
condition (it had flagged row 37 as reverting to OPEN without a printed post-registration
state change; that change is now printed via the two-way name binding + user typing).

## Shared routes (printed steps, cited once here and reused by row)
All paths under final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/
org/proninyaroslav/libretorrent/, branch work-2026-10-31, freshly fetched in this pass
(see "Files printed" below). Batch-60 route R5 (AddFeed) is reused for row 1;
see the batch-60 file for its full citations.

**R6 — Add-link dialog binding.**
ui/addlink/AddLinkDialog.java:184
`binding = DataBindingUtil.inflate(i, R.layout.dialog_add_link, null, false);`
:185 `binding.setViewModel(viewModel);` (binding field type DialogAddLinkBinding).
:187 initLayoutView. Layout res/layout/dialog_add_link.xml declares viewModel
(AddLinkViewModel), two-way-binds @={viewModel.link} (:28) and binds
@{viewModel.showClipboardButton ? …} (:41).

**R7 — Add-tag dialog binding.**
ui/addtag/AddTagDialog.java:128
`binding = DataBindingUtil.inflate(i, R.layout.dialog_add_tag, null, false);`
:129 `binding.setViewModel(viewModel);` (binding field type DialogAddTagBinding).
Layout res/layout/dialog_add_tag.xml declares viewModel (AddTagViewModel),
two-way-binds @={viewModel.state.name} (:27) and binds @{viewModel.state.color} (:68).
ui/addtag/AddTagState.java is a BaseObservable whose setName (:47-50) and setColor
(:57-60) call notifyPropertyChanged.

## Per-method table (all 40 rows, in plan order)

| # | Method (plan) | Proposed label | confirmed_by | Route / printed citations |
|---|---|---|---|---|

| 1 | DialogAddFeedChannelBindingImpl.setViewModel (Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedViewModel;)V | REACHABLE proposed | INFERRED | R5: AddFeedDialog.java:203 `binding.setViewModel(viewModel)` dispatches to this Impl method (generated dispatch, hence INFERRED). |
| 2 | DialogAddFeedChannelBindingImpl$1.<init> (Lorg/proninyaroslav/libretorrent/databinding/DialogAddFeedChannelBindingImpl;)V | OPEN | — | Same $N rule as batch-59 row 19 (batch 62-64 convention). No printed observable assignment for $1. |
| 3 | DialogAddFeedChannelBindingImpl$1.onChange ()V | OPEN | — | Same as row 2; no printed change event assignable to $1.onChange. |
| 4 | DialogAddFeedChannelBindingImpl$2.<init> (Lorg/proninyaroslav/libretorrent/databinding/DialogAddFeedChannelBindingImpl;)V | OPEN | — | Same $N rule as batch-59 row 19. No printed observable assignment for $2. |
| 5 | DialogAddFeedChannelBindingImpl$2.onChange ()V | OPEN | — | Same as row 4; no printed change event assignable to $2.onChange. |
| 6 | DialogAddFeedChannelBindingImpl$3.<init> (Lorg/proninyaroslav/libretorrent/databinding/DialogAddFeedChannelBindingImpl;)V | OPEN | — | Same $N rule as batch-59 row 19. No printed observable assignment for $3. |
| 7 | DialogAddFeedChannelBindingImpl$3.onChange ()V | OPEN | — | Same as row 6; no printed change event assignable to $3.onChange. |
| 8 | DialogAddFeedChannelBindingImpl$4.<init> (Lorg/proninyaroslav/libretorrent/databinding/DialogAddFeedChannelBindingImpl;)V | OPEN | — | Same $N rule as batch-59 row 19. No printed observable assignment for $4. |
| 9 | DialogAddFeedChannelBindingImpl$4.onChange ()V | OPEN | — | Same as row 8; no printed change event assignable to $4.onChange. |
| 10 | DialogAddFeedChannelBindingImpl$5.<init> (Lorg/proninyaroslav/libretorrent/databinding/DialogAddFeedChannelBindingImpl;)V | OPEN | — | Same $N rule as batch-59 row 19. No printed observable assignment for $5. |
| 11 | DialogAddFeedChannelBindingImpl$5.onChange ()V | OPEN | — | Same as row 10; no printed change event assignable to $5.onChange. |
| 12 | DialogAddFeedChannelBindingImpl$6.<init> (Lorg/proninyaroslav/libretorrent/databinding/DialogAddFeedChannelBindingImpl;)V | OPEN | — | Same $N rule as batch-59 row 19. No printed observable assignment for $6. |
| 13 | DialogAddFeedChannelBindingImpl$6.onChange ()V | OPEN | — | Same as row 12; no printed change event assignable to $6.onChange. |
| 14 | DialogAddLinkBinding.<init> (Ljava/lang/Object;Landroid/view/View;ILandroid/widget/ImageButton;Lcom/google/android/material/textfield/TextInputLayout;Lcom/google/android/material/textfield/TextInputEditText;)V | REACHABLE proposed | INFERRED | R6: super-call of DialogAddLinkBindingImpl ctor, mapper-created on AddLinkDialog.java:184 inflate. |
| 15 | DialogAddLinkBinding.getViewModel ()Lorg/proninyaroslav/libretorrent/ui/addlink/AddLinkViewModel; | OPEN | — | CHANGED vs prior proposal (which marked this REACHABLE via executeBindings): no printed caller; AddLinkDialog.java uses binding.setViewModel (:185) and binding.getRoot (:189/:225), never getViewModel. Same convention (v) note as batch-59 row 8 — flips to REACHABLE INFERRED only if the merger adopts the executeBindings-reads-getter convention used in batches 62/65. |
| 16 | DialogAddLinkBindingImpl.<clinit> ()V | REACHABLE proposed | INFERRED | R6: first use is the mapper creation on AddLinkDialog.java:184 inflate; class-init timing unprinted. |
| 17 | DialogAddLinkBindingImpl.<init>(DataBindingComponent,View) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V | REACHABLE proposed | INFERRED | R6: generated mapper return for the dialog_add_link layout inflated at AddLinkDialog.java:184. |
| 18 | DialogAddLinkBindingImpl.<init>(DataBindingComponent,View,Object[]) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V | REACHABLE proposed | INFERRED | R6: generated 2-arg ctor delegates to this 3-arg ctor (generated code, unprinted). |
| 19 | DialogAddLinkBindingImpl.executeBindings ()V | REACHABLE proposed | INFERRED | R6: generated lifecycle callback; runs on inflate (:184) and on rebind after setViewModel (:185). |
| 20 | DialogAddLinkBindingImpl.hasPendingBindings ()Z | OPEN | — | No printed caller (framework-internal check). Same resolver as batch-59 row 2. |
| 21 | DialogAddLinkBindingImpl.invalidateAll ()V | OPEN | — | No printed caller. Same resolver as batch-59 row 2. |
| 22 | DialogAddLinkBindingImpl.onChangeViewModelLink (Landroidx/databinding/ObservableField;I)Z | REACHABLE proposed | INFERRED | R6, STRENGTHENED vs prior proposal by fresh layout evidence: dialog_add_link.xml two-way-binds @={viewModel.link} (:28); and a post-registration change IS printed — AddLinkDialog.java initLayoutView (called at :187, after :185 setViewModel) calls initLinkFromClipboard() (:223), which sets link (AddLinkViewModel.java), and handleUrlClipItem (:144, clipboard event handler) also sets link. Dispatch to the Impl onChange is generated, hence INFERRED. |
| 23 | DialogAddLinkBindingImpl.onChangeViewModelShowClipboardButton (Landroidx/databinding/ObservableBoolean;I)Z | REACHABLE proposed | INFERRED | R6, STRENGTHENED vs prior proposal by fresh layout evidence: dialog_add_link.xml binds @{viewModel.showClipboardButton ? …} (:41); and a post-registration change IS printed — AddLinkDialog.java initLayoutView calls switchClipboardButton() (:222, after :185), which sets viewModel.showClipboardButton (:166) via clipListener (:158) / onFocusChanged (:161). INFERRED (generated dispatch). |
| 24 | DialogAddLinkBindingImpl.onFieldChange (ILjava/lang/Object;I)Z | REACHABLE proposed | INFERRED | R6: setViewModel printed (:185) binds observables (link + showClipboardButton, dialog_add_link.xml); onFieldChange is the generated callback. INFERRED. |
| 25 | DialogAddLinkBindingImpl.setVariable (ILjava/lang/Object;)Z | REACHABLE proposed | INFERRED | R6: generic variable dispatch for the Impl created at :184 and given a viewModel at :185; layout declares the viewModel variable (dialog_add_link.xml:7). |
| 26 | DialogAddLinkBindingImpl.setViewModel (Lorg/proninyaroslav/libretorrent/ui/addlink/AddLinkViewModel;)V | REACHABLE proposed | INFERRED | R6: AddLinkDialog.java:185 `binding.setViewModel(viewModel)` dispatches to this Impl method. |
| 27 | DialogAddLinkBindingImpl$1.<init> (Lorg/proninyaroslav/libretorrent/databinding/DialogAddLinkBindingImpl;)V | OPEN | — | Same $N rule as batch-59 row 19. Only $ callback in this Impl's plan rows; its observable mapping is unprinted, and rows 22-23 already carry the two named observables, so $1 cannot be assigned to either without the Impl body. |
| 28 | DialogAddLinkBindingImpl$1.onChange ()V | OPEN | — | Same as row 27; no printed change event assignable to $1.onChange. |
| 29 | DialogAddTagBinding.<init> (Ljava/lang/Object;Landroid/view/View;ILandroid/widget/RelativeLayout;Landroid/widget/ImageButton;Landroid/widget/TextView;Lorg/proninyaroslav/libretorrent/ui/customviews/ColorView;Lcom/google/android/material/textfield/TextInputEditText;Lcom/google/android/material/textfield/TextInputLayout;)V | REACHABLE proposed | INFERRED | R7: super-call of DialogAddTagBindingImpl ctor, mapper-created on AddTagDialog.java:128 inflate. |
| 30 | DialogAddTagBinding.getViewModel ()Lorg/proninyaroslav/libretorrent/ui/addtag/AddTagViewModel; | OPEN | — | CHANGED vs prior proposal (which marked this REACHABLE via executeBindings): no printed caller; AddTagDialog.java uses binding.setViewModel (:129) and binding.getRoot (:132), never getViewModel. Same convention (v) note as batch-59 row 8. |
| 31 | DialogAddTagBindingImpl.<clinit> ()V | REACHABLE proposed | INFERRED | R7: first use is the mapper creation on AddTagDialog.java:128 inflate; class-init timing unprinted. |
| 32 | DialogAddTagBindingImpl.<init>(DataBindingComponent,View) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;)V | REACHABLE proposed | INFERRED | R7: generated mapper return for the dialog_add_tag layout inflated at AddTagDialog.java:128. |
| 33 | DialogAddTagBindingImpl.<init>(DataBindingComponent,View,Object[]) (Landroidx/databinding/DataBindingComponent;Landroid/view/View;[Ljava/lang/Object;)V | REACHABLE proposed | INFERRED | R7: generated 2-arg ctor delegates to this 3-arg ctor (generated code, unprinted). |
| 34 | DialogAddTagBindingImpl.executeBindings ()V | REACHABLE proposed | INFERRED | R7: generated lifecycle callback; runs on inflate (:128) and on rebind after setViewModel (:129). |
| 35 | DialogAddTagBindingImpl.hasPendingBindings ()Z | OPEN | — | No printed caller (framework-internal check). Same resolver as batch-59 row 2. |
| 36 | DialogAddTagBindingImpl.invalidateAll ()V | OPEN | — | No printed caller. Same resolver as batch-59 row 2. |
| 37 | DialogAddTagBindingImpl.onChangeViewModelState (Lorg/proninyaroslav/libretorrent/ui/addtag/AddTagState;I)Z | REACHABLE proposed | INFERRED | R7, STRENGTHENED vs prior proposal (which flagged this as reverting to OPEN without a printed post-registration state change): that condition is now satisfied by fresh prints — dialog_add_tag.xml two-way-binds @={viewModel.state.name} (:27) and @{viewModel.state.color} (:68), and AddTagState.java is a BaseObservable whose setName (:47-50) and setColor (:57-60) call notifyPropertyChanged. User typing in the name field after the dialog shows therefore changes state.name post-registration and fires this generated callback. The pre-inflate mutations (AddTagDialog.java:121 setInitValues / :124 setRandomColor) are NOT the basis for this row. INFERRED (generated dispatch). |
| 38 | DialogAddTagBindingImpl.onFieldChange (ILjava/lang/Object;I)Z | REACHABLE proposed | INFERRED | R7: setViewModel printed (:129) binds the state observable (dialog_add_tag.xml:27/:68); onFieldChange is the generated callback. INFERRED. |
| 39 | DialogAddTagBindingImpl.setVariable (ILjava/lang/Object;)Z | REACHABLE proposed | INFERRED | R7: generic variable dispatch for the Impl created at :128, viewModel set at :129; layout declares the viewModel variable (dialog_add_tag.xml:6). |
| 40 | DialogAddTagBindingImpl.setViewModel (Lorg/proninyaroslav/libretorrent/ui/addtag/AddTagViewModel;)V | REACHABLE proposed | INFERRED | R7: AddTagDialog.java:129 `binding.setViewModel(viewModel)` dispatches to this Impl method. |

- **20 REACHABLE proposed / 0 UNREACHABLE proposed / 20 OPEN.**

## OPEN rows and what would resolve them (20 rows)
- Rows 2-13, 27, 28 ($N <init>/onChange): a printed generated Impl body assigning each
  $N to an observable, or a merger decision adopting the registration convention (then
  all $N rows in batches 59-61 flip to REACHABLE INFERRED).
- Rows 20, 21, 35, 36 (hasPendingBindings / invalidateAll): a printed call site, or a
  printed generated Impl body showing an internal caller.
- Rows 15, 30 (abstract getViewModel): a printed caller, or a merger decision adopting
  the executeBindings-reads-getter convention (then both flip to REACHABLE INFERRED
  together with batches 59/60 getViewModel rows).
- General resolver: printed generated mapper/Impl bodies, or a saved full-repo grep in
  rule-F/C5 form over generated binding sources. No OPEN row may be flipped to
  UNREACHABLE on the basis of not being found in the printed subset.

## Caveats restated
1. Strict-entry caveat: every REACHABLE row is anchored at a printed inflate +
   setViewModel site, NOT at the launcher. Who shows AddFeedDialog / AddLinkDialog /
   AddTagDialog was not printed in this session; under a strict launcher-entry rule all
   20 REACHABLE rows revert to OPEN.
2. Mapper caveat: DataBinderMapperImpl selection was not printed and is not in
   final_java_only. If the merger requires a printed mapper step, all Impl rows revert
   to OPEN (the batch-17 position).
3. Anonymous $N numbering and the generated 2-arg -> 3-arg ctor delegation are
   generated-code inferences, not bytecode-verified.
4. No row in this file is verified for merge: no build, sampler, grep, or C1 check was run.
   A merge step must re-derive every row from a full checkout, run the C1 checks, and
   spot-check at least 1 in 5 citations.

## Files printed (fresh, branch work-2026-10-31, saved in ~/workspace/b596061-src/)
- ui/addfeed/AddFeedDialog.java — SHA 6b35d852849a, 435 lines (binding :202-203; see batch-60 file)
- ui/addlink/AddLinkDialog.java — SHA 0777269a0602, 317 lines (binding :184-185/:187, link.set :144, showClipboardButton.set :166/:222)
- ui/addlink/AddLinkViewModel.java — SHA fc1f3696b7f2, 75 lines (link + showClipboardButton observables, initLinkFromClipboard)
- ui/addtag/AddTagDialog.java — SHA a8fd5111cc2a, 234 lines (binding :128-129, setInitValues :121, setRandomColor :124)
- ui/addtag/AddTagViewModel.java — SHA ae636919e74e, 79 lines (state field, setInitValues, setRandomColor)
- ui/addtag/AddTagState.java — SHA 3e03ed0e76cd0, 62 lines (BaseObservable, setName notify :49, setColor notify :59)
- res/layout/dialog_add_link.xml — SHA dbca5146b08e, 45 lines (viewModel variable, two-way link :28, showClipboardButton :41)
- res/layout/dialog_add_tag.xml — SHA 03af5311b359, 71 lines (viewModel variable, two-way state.name :27, state.color :68)
- handoff/LIBRETORRENT_BATCH_PLAN.tsv — local copy ~/workspace/agent27-plan.tsv (plan SHA above)
