**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 75 — merge-ready (UNVERIFIED)

**Status: UNVERIFIED merge-ready part only. 0 rows verified for merge. Nothing here has been merged into `graph_def.py`.**

- Repo: `bugfixops/ground-truth-results`, branch `work-2026-10-31` only (never `main` or `result`).
- Membership: exactly the 40 rows for batch 75 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, local copy `~/workspace/agent27-plan.tsv`, git blob SHA `0104806dd666c840049b3db52823d4b384fa1c92`. All 40 rows are `TODO_CANDIDATE_REACHABLE` in the plan: 29 AddFeedDialog methods, 8 AddFeedDialog$1/$2 anonymous-TextWatcher methods (4 each), 3 AddFeedMutableParams methods (`<init>`, `getFeedId`, `getFilter`). The remaining AddFeedMutableParams methods are batch 76.
- **Counts: 40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN** (SOURCE 37 / INFERRED 3: rows 11, 13, 14).
- Prior proposals were leads only. Every row below was re-judged against source freshly fetched in this pass (see below); no prior verdict was copied without a fresh check. No UNREACHABLE is claimed: no saved full-repo grep exists, and absence in the printed files is not evidence of absence. No `search_code` result was used anywhere, and no `search_code` 0 was used as evidence of absence.
- `confirmed_by` convention in this file (per-row, not whole-route): SOURCE = every step from the trunk to the method is printed app code or a standard framework edge (DialogFragment lifecycle, View/Dialog click/key/text listeners, DialogFragment show, fragment callback); INFERRED = the route crosses a library/framework dispatch not printed from its source (Rx subscribe, Thread.start, data-binding generated code, ViewModelProvider construction, class/enum initialisation). Under a whole-route convention, SOURCE rows crossing unprinted dispatch would read INFERRED; labels are unaffected.

## Freshly printed source in this pass (branch `work-2026-10-31`, GitHub connector only, one file at a time with ~25 s pauses, no fresh HTTP 429)

Saved in `~/workspace/b747576-src/` (repo base `final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/` unless noted):

- `ui/addfeed/AddFeedDialog.java` — 434 lines, git blob SHA `08423189…`
- `ui/addfeed/AddFeedViewModel.java` — 220 lines, SHA `197167f0…`
- `ui/addfeed/AddFeedMutableParams.java` — 118 lines, SHA `bd434f25…`
- `ui/addfeed/AddFeedActivity.java` — 94 lines, SHA `062c696d…`
- `src/main/AndroidManifest.xml` — 295 lines, SHA `875a8aa7…`
- `src/main/res/layout/dialog_add_feed_channel.xml` — 158 lines, SHA `c4a8306d…` (two-way bindings; cited only for batch 76 rows, noted here for completeness)

Line-count note: the prior proposals counted these files as 435 / 221 / 119 lines; the fresh files are 434 / 220 / 118 lines. The content lines cited below were all re-checked against the fresh files, so the 1-line differences are counting differences only (trailing line), except for one genuine citation correction recorded below.

## Shared trunk (freshly printed, cited once, reused by row)

- T1 — Dialog display. `AddFeedActivity.onCreate:47–68`: findFragmentByTag, if null then `AddFeedDialog.newInstance(feedId)` at `:61` (ACTION_EDIT_FEED) or `newInstance(uri)` at `:63`, then `addFeedDialog.show(fm, TAG_ADD_FEED_DIALOG)` at `:66`. Showing a DialogFragment is a standard framework edge; the framework then calls onAttach / onCreateDialog / onStart / onResume / onStop / onDestroyView.
- T2 — Dialog creation. `AddFeedDialog.onCreateDialog:180–209`: ViewModelProvider creation and `provider.get(AddFeedViewModel.class)` at `:185–186` (see correction below), getArguments feedId/uri at `:194–195`, `initParams(uri, feedId)` at `:199`, DataBindingUtil.inflate `dialog_add_feed_channel` at `:202–203`, `binding.setViewModel(viewModel)` at `:203`, `initLayoutView()` at `:205`, focus-listener registration at `:207`, returns alert at `:209`.
- T3 — Mode branch. `AddFeedDialog.initParams:130–137`: uri != null → `viewModel.initAddMode(uri)`; else feedId != −1 → `initEditMode(feedId)`; else `initAddModeFromClipboard()`.
- **Citation correction vs prior proposals:** the prior batch 75/76 proposals cited ViewModelProvider.get at `AddFeedDialog:195–196`. On the fresh file those lines are the getArguments calls (`:194–195`); the ViewModelProvider creation and `get()` calls are at `:185–186`. All other AddFeedDialog line citations in the prior proposals were confirmed unchanged on the fresh file.
- **Strict-entry caveat:** who starts AddFeedActivity (launcher / feeds UI intent) was NOT printed in this pass, so under a strict launcher-anchored rule every row below reverts to OPEN. The rows are proposed REACHABLE on the dialog-anchored trunk T1+T2, as in prior batches, and AddFeedActivity itself is manifest-declared exported with SEND/VIEW intent filters (`AndroidManifest.xml:179–200`), so under an external-entry rule the entry is closed. No row is claimed verified for merge.

## Lambda note (AddFeedDialog)

Descriptors distinguish most lambdas; individual $n-to-button mapping inside initAlertDialog is NOT verified from bytecode:

- $0 (Z)V: the only field-initialiser lambda, `AddFeedDialog` onFocusChanged `:112–113`, registered onCreateDialog `:207`, removed onDestroyView `:215`. By elimination this is $0.
- $1 (DialogInterface,int,KeyEvent)Z: onResume key listener `AddFeedDialog:146–157`, BACK + ACTION_DOWN → onBackPressed `:151`. Signature matches exactly.
- $2, $3 (View)V: initLayoutView click listeners, `AddFeedDialog:250` (end-icon → expandableLayout.toggle) and `:252` (clipboardButton → showClipboardDialog), in source order.
- $4–$7 (View)V: the four button click lambdas inside the onShow body, `AddFeedDialog:279` (edit → updateChannel), `:280` (delete → deleteFeedDialog), `:283` (add → addChannel), `:286–287` (cancel → finish CANCEL). Which $n is which button is NOT verified; the group route is the same for all four.
- $8 (DialogInterface)V: the setOnShowListener body itself, `AddFeedDialog:275–288`, registered `:275`; it installs the four button listeners above.
- $9 (BaseAlertDialog$Event)V: subscribeAlertDialog event lambda, `AddFeedDialog:303–326` (POSITIVE → deleteChannel `:313`; NEGATIVE → dismiss). Rx dispatch INFERRED.
- $10 (ClipboardDialog$Item)V: subscribeAlertDialog item lambda, `AddFeedDialog:325–332` (TAG_CLIPBOARD_DIALOG → handleUrlClipItem `:327`). Rx dispatch INFERRED.

## Table — one row per plan method, in plan order

| # | Method (plan signature) | Label | confirmed_by | Printed citation / route |
|---|---|---|---|---|
| 1 | `AddFeedDialog.initAlertDialog (Landroid/view/View;)V` | REACHABLE | SOURCE | `AddFeedDialog:255` called from initLayoutView; body `:258–288` builds alert, `:275` setOnShowListener. |
| 2 | `AddFeedDialog.initLayoutView ()V` | REACHABLE | SOURCE | `AddFeedDialog:205` called from onCreateDialog; body `:220–255`. |
| 3 | `AddFeedDialog.initParams (Landroid/net/Uri;J)V` | REACHABLE | SOURCE | `AddFeedDialog:199` called from onCreateDialog; body `:130–137`, see T3. |
| 4 | `AddFeedDialog.lambda$initAlertDialog$4 (Landroid/view/View;)V` | REACHABLE | SOURCE | One of the four button click lambdas, `AddFeedDialog:279/:280/:283/:286` (see lambda note); standard View click edge. |
| 5 | `AddFeedDialog.lambda$initAlertDialog$5 (Landroid/view/View;)V` | REACHABLE | SOURCE | Same group as row 4. |
| 6 | `AddFeedDialog.lambda$initAlertDialog$6 (Landroid/view/View;)V` | REACHABLE | SOURCE | Same group as row 4. |
| 7 | `AddFeedDialog.lambda$initAlertDialog$7 (Landroid/view/View;)V` | REACHABLE | SOURCE | Same group as row 4. |
| 8 | `AddFeedDialog.lambda$initAlertDialog$8 (Landroid/content/DialogInterface;)V` | REACHABLE | SOURCE | `AddFeedDialog:275` setOnShowListener body `:275–288`, installs rows 4–7 listeners; standard dialog listener edge. |
| 9 | `AddFeedDialog.lambda$initLayoutView$2 (Landroid/view/View;)V` | REACHABLE | SOURCE | `AddFeedDialog:250` end-icon click → expandableLayout.toggle(); standard View click edge. |
| 10 | `AddFeedDialog.lambda$initLayoutView$3 (Landroid/view/View;)V` | REACHABLE | SOURCE | `AddFeedDialog:252` clipboardButton click → showClipboardDialog(); standard View click edge. |
| 11 | `AddFeedDialog.lambda$new$0 (Z)V` | REACHABLE | INFERRED | `AddFeedDialog:112–113` field lambda, registered onCreateDialog `:207`, removed onDestroyView `:215`; framework focus-change dispatch not printed from `fw_src`, hence INFERRED. |
| 12 | `AddFeedDialog.lambda$onResume$1 (Landroid/content/DialogInterface;ILandroid/view/KeyEvent;)Z` | REACHABLE | SOURCE | `AddFeedDialog:146–157` key listener, BACK + ACTION_DOWN → onBackPressed `:151`; standard Dialog key edge. |
| 13 | `AddFeedDialog.lambda$subscribeAlertDialog$10 (Lorg/proninyaroslav/libretorrent/ui/ClipboardDialog$Item;)V` | REACHABLE | INFERRED | `AddFeedDialog:325–332` item lambda → handleUrlClipItem `:327`; Rx subscribe dispatch not printed, hence INFERRED. |
| 14 | `AddFeedDialog.lambda$subscribeAlertDialog$9 (Lorg/proninyaroslav/libretorrent/ui/BaseAlertDialog$Event;)V` | REACHABLE | INFERRED | `AddFeedDialog:303–326` event lambda → deleteChannel `:313` / dismiss; Rx subscribe dispatch not printed, hence INFERRED. |
| 15 | `AddFeedDialog.newInstance(long) (J)Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedDialog;` | REACHABLE | SOURCE | `AddFeedActivity:61` called from AddFeedActivity.onCreate (ACTION_EDIT_FEED branch); body `AddFeedDialog:89–98`. |
| 16 | `AddFeedDialog.newInstance(Uri) (Landroid/net/Uri;)Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedDialog;` | REACHABLE | SOURCE | `AddFeedActivity:63` called from AddFeedActivity.onCreate (else branch); body `AddFeedDialog:78–87`. |
| 17 | `AddFeedDialog.onAttach (Landroid/content/Context;)V` | REACHABLE | SOURCE | `AddFeedDialog:122–128`, super.onAttach + activity cast; standard DialogFragment lifecycle edge after show (`AddFeedActivity:66`). |
| 18 | `AddFeedDialog.onBackPressed ()V` | REACHABLE | SOURCE | `AddFeedDialog:424–426` finish BACK; called from row 12 lambda `:151` and from `AddFeedActivity.onBackPressed:92`. |
| 19 | `AddFeedDialog.onCreateDialog (Landroid/os/Bundle;)Landroid/app/Dialog;` | REACHABLE | SOURCE | `AddFeedDialog:180–209`; standard DialogFragment lifecycle edge after show (`AddFeedActivity:66`). |
| 20 | `AddFeedDialog.onDestroyView ()V` | REACHABLE | SOURCE | `AddFeedDialog:213–218`, removes focus listener `:215`; standard lifecycle edge. |
| 21 | `AddFeedDialog.onResume ()V` | REACHABLE | SOURCE | `AddFeedDialog:141–158`, installs key listener `:146`; standard lifecycle edge. |
| 22 | `AddFeedDialog.onStart ()V` | REACHABLE | SOURCE | `AddFeedDialog:170–177`, subscribeAlertDialog `:174` + subscribeClipboardManager `:175`; standard lifecycle edge. |
| 23 | `AddFeedDialog.onStop ()V` | REACHABLE | SOURCE | `AddFeedDialog:161–167`, unsubscribeClipboardManager `:165` + disposables.clear; standard lifecycle edge. |
| 24 | `AddFeedDialog.showClipboardDialog ()V` | REACHABLE | SOURCE | `AddFeedDialog:291–301`, child FragmentManager + ClipboardDialog.newInstance/show; called from row 10 click `:252`. |
| 25 | `AddFeedDialog.subscribeAlertDialog ()V` | REACHABLE | SOURCE | `AddFeedDialog:303–334`; called from onStart `:174`. |
| 26 | `AddFeedDialog.subscribeClipboardManager ()V` | REACHABLE | SOURCE | `AddFeedDialog:100–103`, addPrimaryClipChangedListener(clipListener) `:102`; called from onStart `:175`. |
| 27 | `AddFeedDialog.switchClipboardButton ()V` | REACHABLE | SOURCE | `AddFeedDialog:115–119`, Utils.getClipData → showClipboardButton.set; called directly initLayoutView `:253`, via clipListener `:110`, via row 11 lambda `:113`. |
| 28 | `AddFeedDialog.unsubscribeClipboardManager ()V` | REACHABLE | SOURCE | `AddFeedDialog:105–108`, removePrimaryClipChangedListener `:107`; called from onStop `:165`. |
| 29 | `AddFeedDialog.updateChannel ()V` | REACHABLE | SOURCE | `AddFeedDialog:395–409`, checkUrlField + viewModel.updateChannel `:400` + finish OK; called from edit-button click (row 4–7 group, `:279`). |
| 30 | `AddFeedDialog$1.<init> (Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedDialog;)V` | REACHABLE | SOURCE | `AddFeedDialog:222` explicit `new TextWatcher()` for binding.url, inside initLayoutView. |
| 31 | `AddFeedDialog$1.afterTextChanged (Landroid/text/Editable;)V` | REACHABLE | SOURCE | `AddFeedDialog:230–234`, clears layoutUrl error; registered `:222`; standard TextWatcher edge. |
| 32 | `AddFeedDialog$1.beforeTextChanged (Ljava/lang/CharSequence;III)V` | REACHABLE | SOURCE | `AddFeedDialog:224`, empty body; registered `:222`. Empty does not mean unreachable — the callback is registered. |
| 33 | `AddFeedDialog$1.onTextChanged (Ljava/lang/CharSequence;III)V` | REACHABLE | SOURCE | `AddFeedDialog:227`, empty body; registered `:222`. |
| 34 | `AddFeedDialog$2.<init> (Lorg/proninyaroslav/libretorrent/ui/addfeed/AddFeedDialog;)V` | REACHABLE | SOURCE | `AddFeedDialog:236` explicit `new TextWatcher()` for binding.filter, inside initLayoutView. |
| 35 | `AddFeedDialog$2.afterTextChanged (Landroid/text/Editable;)V` | REACHABLE | SOURCE | `AddFeedDialog:244–248`, clears layoutFilter error; registered `:236`; standard TextWatcher edge. |
| 36 | `AddFeedDialog$2.beforeTextChanged (Ljava/lang/CharSequence;III)V` | REACHABLE | SOURCE | `AddFeedDialog:238`, empty body; registered `:236`. |
| 37 | `AddFeedDialog$2.onTextChanged (Ljava/lang/CharSequence;III)V` | REACHABLE | SOURCE | `AddFeedDialog:241`, empty body; registered `:236`. |
| 38 | `AddFeedMutableParams.<init> ()V` | REACHABLE | SOURCE | Implicit default constructor (no explicit ctor in `AddFeedMutableParams:27–118`; fields `:29–35`); constructed `AddFeedViewModel:48` `new AddFeedMutableParams()`. |
| 39 | `AddFeedMutableParams.getFeedId ()J` | REACHABLE | SOURCE | `AddFeedMutableParams:37–40`; called `AddFeedViewModel:124` (deleteChannel), `:147` (fetchParams), `:166` (applyParams). |
| 40 | `AddFeedMutableParams.getFilter ()Ljava/lang/String;` | REACHABLE | SOURCE | `AddFeedMutableParams:96–99` (@Bindable); called `AddFeedViewModel:177` (applyParams, FeedChannel construction). Two-way binding in `dialog_add_feed_channel.xml:106` (`@={viewModel.mutableParams.filter}`) is an additional generated route, not needed for this row. |

## Counts

- REACHABLE proposed: 40 / 40 (SOURCE 37, INFERRED 3: rows 11, 13, 14)
- UNREACHABLE proposed: 0
- OPEN: 0
- Verified for merge: 0

## Not claimed / remaining for merge

- No UNREACHABLE claimed: no saved full-repo grep exists for any row, and absence in the printed files is not evidence of absence.
- Lambda $4–$7 individual button mapping must be confirmed against bytecode if the merger needs it; labels are unaffected (same group route).
- Strict-entry caveat above: launcher-to-AddFeedActivity step not printed; under a strict launcher rule all 40 revert to OPEN. Under an external-entry rule (AddFeedActivity is exported with SEND/VIEW filters), the entry is closed.
- Build: **not run**. C1: **not run** (Mac after push, never claimed passed). Main-agent spot-check (1 in 5) and `py_compile` are outstanding. Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]) (pushed UNVERIFIED before [L] at user request 2026-11-01). Nothing was edited in `graph_def.py`, `out/`, `PROGRESS_V2`, `AGENT_NOTES`, `tools/`, or another helper's file. No other batch was touched.
- AddFeedDialog.addChannel / deleteChannel / deleteFeedDialog / handleUrlClipItem / checkUrlField are callers in this batch's routes but are NOT batch-75 rows; they belong to other batches (batch 74) and were judged only as route steps here, not as batch verdicts.
