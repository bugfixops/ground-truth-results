**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 77 — merge-ready file (UNVERIFIED, NOT merged)

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only. Never main or result.
Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to graph_def.py, out/, verification.csv, PROGRESS_V2, AGENT_NOTES,
tools/, or another worker's files. No build, sampler, grep, or C1 count is claimed:
build/C1/sampler/grep = NOT RUN in this session. Build and C1 run on the user's Mac
after a push; until then they are marked "not run", never passed.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 77 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from
the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`), all TODO_CANDIDATE_REACHABLE in the
plan, in plan order:
AddLinkDialog rows 1-24, AddLinkViewModel rows 25-27, AddTagActivity rows 28-33,
AddTagDialog rows 34-40.
Input, not result: `~/workspace/libretorrent-batch77-proposal.md` (Agent 28). Every row
below was re-judged from source freshly printed in this session; no proposal verdict
was copied as a result. One correction to the input is recorded below (row 8).

## Printed source used in this session — all fresh connector fetches, one file at a time with pauses, branch work-2026-10-31, saved in ~/workspace/b7778-src/

Base path for all files:
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
- `ui/addlink/AddLinkDialog.java` — 316 lines, SHA `571afec025b0eefc…`
- `ui/addlink/AddLinkViewModel.java` — 74 lines, SHA `33da38ff89be8d30…`
- `ui/addlink/AddLinkActivity.java` — 47 lines, SHA `c6d228e92b27e76d…` (NEW in this session; not in the input proposal — it closes the input's AddLinkDialog display gap)
- `ui/addtag/AddTagActivity.java` — 84 lines, SHA `6844ebea6ecc7595…` (file is 84 lines in this fresh print; the input said 85 — citations below use the fresh numbering, which differs from the input by at most 1 line in a few places; the routes are unchanged)
- `ui/addtag/AddTagDialog.java` — 233 lines, SHA `bef075da2e784d7c…` (input said 234; same 1-line numbering note)
- No fresh HTTP 429 was hit in this session. No search_code result was used as evidence of absence (no search was run).

## Entry trunk (freshly printed)

- AddLinkDialog entry IS now printed, closing the input's gap: `AddLinkActivity.onCreate:23-33`
  — `addLinkDialog = AddLinkDialog.newInstance();` at :31, `addLinkDialog.show(fm, TAG_ADD_LINK_DIALOG);`
  at :32, when no fragment with that tag is found. AddLinkDialog.onCreateDialog:171-191
  then calls initLayoutView:187 and (via initLayoutView:225) initAlertDialog.
  Row 8 is therefore upgraded from the input's INFERRED to SOURCE (see row 8).
- AddTagDialog entry IS printed: `AddTagActivity.onCreate:47-60` — `dialog = AddTagDialog.newInstance(initInfo);`
  at :58, `dialog.show(fm, TAG_DIALOG);` at :59, when no fragment with TAG_DIALOG is found.
  AddTagDialog.onCreateDialog:112-134 then calls initLayoutView:131 and initAlertDialog:132.
- Remaining strict-entry gap (recorded, not decided): who starts AddLinkActivity itself
  and who starts AddTagActivity itself (launcher / intent step) was NOT printed in this
  session. Under the anchor convention used here (activity/dialog/fragment anchor),
  the rows below are REACHABLE proposed. Under a strict launcher-entry rule, all
  40 rows would revert to OPEN, because every route here ultimately anchors at
  AddLinkActivity or AddTagActivity. This is a project convention the merger must
  decide; it is NOT decided in this file, and it changes no label under the anchor
  convention. Note the distinction: the dialog-display step itself is now printed
  for both dialogs, so the only remaining gap is the activity-starter step, not
  the dialog-show step.
- Lambda $n mapping: for the initAlertDialog lambdas the SET of bodies is printed
  (two View onClick bodies + one DialogInterface onShow body), but which $n is
  which body is NOT verified from printed source alone (the onShow body contains
  the two button registrations, so bytecode numbering need not follow source order).
  All lambda rows are therefore INFERRED, not SOURCE. The same applies to
  AddLinkDialog initAlertDialog $4/$5/$6, onResume$0, subscribeAlertDialog$1,
  initLayoutView$3 and new$2: signature + single candidate body match, but $n
  identity is still marked INFERRED for safety. A $n swap within a group would
  not change any label; the merger must confirm $n-to-body mapping against
  bytecode if it requires it.
- confirmed_by convention used here (per-row, as in the input proposal):
  SOURCE = a direct app-to-app call site naming the method is printed in app
  source (including a printed listener body that calls it, and a lifecycle
  method whose show/registration step is printed); INFERRED = the method is
  reached only through unprinted framework/library dispatch (DialogFragment
  lifecycle, view-click/key dispatch, Rx dispatch, JVM class initialisation)
  where the registration or show site is printed. Under the whole-route
  INFERRED convention used in some earlier batches (e.g. batch 14), all
  REACHABLE rows would flip to INFERRED; labels are unaffected. That
  convention choice is NOT decided here.

## Counts — mechanically verified after writing (40 rows, sequence 1-40 intact, no gaps, no duplicates)

- REACHABLE proposed: 40 / 40
- UNREACHABLE proposed: 0 / 40
- OPEN: 0 / 40
- confirmed_by: SOURCE 30, INFERRED 10
- Verified for merge: 0 / 40. Still required: main-agent spot-check (1 in 5),
  py_compile, build, Mac build/C1 — all NOT RUN here.

## Undecided conventions — flagged per row, NOT decided

- Strict-entry: applies to ALL 40 REACHABLE proposals (see trunk above).
- Lambda $n mapping: rows 1-7 (INFERRED throughout).
- <clinit> timing: row 34 INFERRED — TAG at AddTagDialog.java:57 is not a
  compile-time constant, so a <clinit> exists; it runs on first class use
  (AddTagActivity.onCreate:58 newInstance). Whether <clinit> counts as
  REACHABLE on first-use evidence alone is undecided project-wide; flagged,
  not decided.
- Framework-dispatch policy: rows 9, 12-15, 21, 28, 34 are SOURCE in this file
  on the per-row convention above (printed show/registration + standard
  DialogFragment/Activity dispatch), but under a stricter policy requiring a
  printed app-side call naming the method itself, lifecycle rows 9, 12-15
  and the implicit constructors 28, 35 would fall to INFERRED/OPEN. Flagged,
  not decided. No row is UNREACHABLE on this account.
- No migration-gate, binding-variant, binding-getViewModel, Room-finalize,
  or $N-mapping issue occurs in this row set (no such methods are in batch 77).

## Per-row table — freshly re-derived, UNVERIFIED, 0 verified for merge

Short prefix: `L/` = `ui/addlink/`, `T/` = `ui/addtag/`. All files under the
source root above.

| # | Method (batch row) | Proposed label | Kind / confirmed_by | Printed citations and route (fresh prints, this session) |
|---|---|---|---|---|
| 1 | `AddLinkDialog.lambda$initAlertDialog$4 (View)V` | REACHABLE proposed | INFERRED | `L/AddLinkDialog.java:228-246` initAlertDialog; setOnShowListener body at :238-245 registers an add-button onClick (-> addLink) and a cancel-button onClick (-> finish CANCEL). One of the two View onClick bodies; $n-to-body mapping unverified (see trunk). Chain: AddLinkActivity:31-32 newInstance+show -> onCreateDialog:171-191 -> initLayoutView:187,225 -> initAlertDialog:225. |
| 2 | `AddLinkDialog.lambda$initAlertDialog$5 (View)V` | REACHABLE proposed | — / INFERRED | Same as row 1: the other View onClick body in initAlertDialog:238-245. |
| 3 | `AddLinkDialog.lambda$initAlertDialog$6 (DialogInterface)V` | REACHABLE proposed | — / INFERRED | `L/AddLinkDialog.java:238-245`: the setOnShowListener body itself (DialogInterface arg), registered by alert.setOnShowListener; it installs the two button listeners. |
| 4 | `AddLinkDialog.lambda$initLayoutView$3 (View)V` | REACHABLE proposed | — / INFERRED | `L/AddLinkDialog.java:221`: clipboardButton.setOnClickListener((v) -> showClipboardDialog()); showClipboardDialog:248-259 shows ClipboardDialog. Called via initLayoutView:202, from onCreateDialog:187. |
| 5 | `AddLinkDialog.lambda$new$2 (Z)V` | REACHABLE proposed | — / INFERRED | `L/AddLinkDialog.java:160-161`: field onFocusChanged = (__) -> switchClipboardButton(); signature (Z)V matches ViewTreeObserver.OnWindowFocusChangeListener. Registered in onCreateDialog:189, removed in onDestroyView:197. Field-initialiser lambda, hence lambda$new. |
| 6 | `AddLinkDialog.lambda$onResume$0 (DialogInterface,int,KeyEvent)Z` | REACHABLE proposed | INFERRED | `L/AddLinkDialog.java:93-111` onResume: getDialog().setOnKeyListener lambda; BACK + ACTION_DOWN -> onBackPressed:103. |
| 7 | `AddLinkDialog.lambda$subscribeAlertDialog$1 (ClipboardDialog$Item)V` | REACHABLE proposed | — / INFERRED | `L/AddLinkDialog.java:130-137` subscribeAlertDialog (called from onStart:127): clipboardViewModel.observeSelectedItem().subscribe((item) -> { if TAG_CLIPBOARD_DIALOG, handleUrlClipItem(item.str) }); handleUrlClipItem sets viewModel.link and posts addLink. Rx dispatch itself not printed from source, hence INFERRED. |
| 8 | `AddLinkDialog.newInstance ()AddLinkDialog` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:73-81`: creates frag, setArguments, returns it. CORRECTION to input (was INFERRED, caller unprinted): caller IS now printed fresh — `L/AddLinkActivity.java:31` `addLinkDialog = AddLinkDialog.newInstance();` in onCreate:23-33, followed by show at :32. Upgrade to SOURCE. |
| 9 | `AddLinkDialog.onAttach (Context)V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:84-91`: super.onAttach + activity cast. Standard DialogFragment lifecycle dispatch after the printed show at AddLinkActivity:32. Lifecycle-policy flag applies. |
| 10 | `AddLinkDialog.onBackPressed ()V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:306-309`: finish(..., BACK); called from the onResume key listener:103, and from AddLinkActivity.onBackPressed (fresh print `L/AddLinkActivity.java:43-45`). |
| 11 | `AddLinkDialog.onCreateDialog (Bundle)Dialog` | REACHABLE proposed | SOURCE | `L/AddLinkDialog.java:171-191`: ViewModelProvider get AddLinkViewModel:176-177, binding inflate:186, initLayoutView:187, focus listener registration:189, returns alert:191. Framework calls it after the printed show at AddLinkActivity:32. |
| 12 | `AddLinkDialog.onDestroyView ()V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:195-199`: removes focus listener, super.onDestroyView. Standard lifecycle. |
| 13 | `AddLinkDialog.onResume ()V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:93-111`: installs back-key listener (row 6). |
| 14 | `AddLinkDialog.onStart ()V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:122-128`: subscribeClipboardManager:126 + subscribeAlertDialog:127. |
| 15 | `AddLinkDialog.onStop ()V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:113-119`: unsubscribeClipboardManager:117 + disposables.clear. |
| 16 | `AddLinkDialog.showClipboardDialog ()V` | REACHABLE proposed | SOURCE | `L/AddLinkDialog.java:248-259`: isAdded guard, child FragmentManager, ClipboardDialog.newInstance + show if absent. Called from row 4 click listener. |
| 17 | `AddLinkDialog.subscribeAlertDialog ()V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:130-137`; called from onStart:127. |
| 18 | `AddLinkDialog.subscribeClipboardManager ()V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:148-151`: addPrimaryClipChangedListener(clipListener); called from onStart:126. |
| 19 | `AddLinkDialog.switchClipboardButton ()V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:163-167`: Utils.getClipData -> viewModel.showClipboardButton.set(clip != null). Called from clipListener:158, onFocusChanged:160-161, initLayoutView:222. |
| 20 | `AddLinkDialog.unsubscribeClipboardManager ()V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:153-156`: removePrimaryClipChangedListener(clipListener); called from onStop:117. |
| 21 | `AddLinkDialog$1.<init> (AddLinkDialog)V` | REACHABLE proposed | INFERRED | Anonymous TextWatcher instantiated at `L/AddLinkDialog.java:205-219` inside initLayoutView (new TextWatcher(){...}); framework TextWatcher dispatch, hence INFERRED for the constructor's call path. |
| 22 | `AddLinkDialog$1.afterTextChanged (Editable)V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:214-218`: clears layoutLink error. Registered via addTextChangedListener:205. |
| 23 | `AddLinkDialog$1.beforeTextChanged (CharSequence,int,int,int)V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:208`: empty body; same registration as row 22. Empty does not mean unreachable — the framework callback exists and is registered. |
| 24 | `AddLinkDialog$1.onTextChanged (CharSequence,int,int,int)V` | REACHABLE proposed | — / SOURCE | `L/AddLinkDialog.java:211`: empty body; same registration as row 22. |
| 25 | `AddLinkViewModel.<init> (Application)V` | REACHABLE proposed | — / SOURCE | `L/AddLinkViewModel.java:40-43`: super(application). Obtained via provider.get(AddLinkViewModel.class) in AddLinkDialog.onCreateDialog:176-177. |
| 26 | `AddLinkViewModel.initLinkFromClipboard ()V` | REACHABLE proposed | SOURCE | `L/AddLinkViewModel.java:45-59`: clipboard text -> link.set if magnet/http/hash. Called from AddLinkDialog.initLayoutView:223. |
| 27 | `AddLinkViewModel.normalizeUrl (String)String` | REACHABLE proposed | — / SOURCE | `L/AddLinkViewModel.java:61-73`: hash -> normalizeMagnetHash, else NormalizeUrl.normalize. Called from AddLinkDialog.addLink:273 (printed in AddLinkDialog.java:260-287 flow). |
| 28 | `AddTagActivity.<init> ()V` | REACHABLE proposed | — / INFERRED | Implicit default constructor; no explicit constructor in `T/AddTagActivity.java`. Framework instantiates the activity (standard AppCompatActivity dispatch); start step not printed — see trunk caveat. |
| 29 | `AddTagActivity.onBackPressed ()V` | REACHABLE proposed | — / SOURCE | `T/AddTagActivity.java:73-75`: dialog.onBackPressed(); standard activity back dispatch, dialog is the AddTagDialog from onCreate:58. |
| 30 | `AddTagActivity.onColorSelected (int,int)V` | REACHABLE proposed | — / SOURCE | `T/AddTagActivity.java:78-80`: viewModel.state.setColor(color). Activity implements ColorPickerDialogListener; picker is shown from AddTagDialog.initLayoutView:153-155 with show(activity), so the library calls back into the activity (library dispatch itself not printed from source). |
| 31 | `AddTagActivity.onCreate (Bundle)V` | REACHABLE proposed | SOURCE | `T/AddTagActivity.java:47-60`: ViewModelProvider get AddTagViewModel:51-52, findFragmentByTag, else newInstance + show (row 35 route):58-59. |
| 32 | `AddTagActivity.onDialogDismissed (int)V` | REACHABLE proposed | — / SOURCE | `T/AddTagActivity.java:83-84`: empty body; ColorPickerDialogListener callback for the picker shown at AddTagDialog.java:153-155. Empty callback still reachable via the listener interface. |
| 33 | `AddTagActivity.onFragmentFinished (Fragment,Intent,ResultCode)V` | REACHABLE proposed | — / SOURCE | `T/AddTagActivity.java:64-70`: finish(). Called from AddTagDialog.finish:231 via ((FragmentCallback)activity).onFragmentFinished. |
| 34 | `AddTagDialog.<clinit> ()V` | REACHABLE proposed | — / INFERRED | `T/AddTagDialog.java:57`: TAG = AddTagDialog.class.getSimpleName() is not a compile-time constant, so a <clinit> exists; it runs on first class use, i.e. AddTagActivity.onCreate:58 newInstance. Class-load step INFERRED. <clinit>-timing flag applies. |
| 35 | `AddTagDialog.<init> ()V` | REACHABLE proposed | — / SOURCE | Implicit constructor, invoked by newInstance at `T/AddTagDialog.java:68` (new AddTagDialog()). |
| 36 | `AddTagDialog.addTag ()V` | REACHABLE proposed | SOURCE | `T/AddTagDialog.java:196-223`: checkName guard, viewModel.saveTag() subscribed on io/main, success -> finish OK, error -> TagAlreadyExists toast or error toast. Called from the positive-button click in initAlertDialog:187. |
| 37 | `AddTagDialog.checkName ()Z` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:159-170`: empty-name error handling. Called from addTag:197. |
| 38 | `AddTagDialog.finish (Intent,ResultCode)V` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:229-232`: alert.dismiss + FragmentCallback.onFragmentFinished (AddTagActivity row 33). Called from addTag success, cancel click, onBackPressed. |
| 39 | `AddTagDialog.initAlertDialog (View)V` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:172-194`: builder, title/add-vs-edit by getExistsTagId, onShow listener installing add/cancel buttons. Called from onCreateDialog:132. |
| 40 | `AddTagDialog.initLayoutView ()V` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:137-157`: name TextWatcher registration:138, color click -> ColorPickerDialog:153-155. Called from onCreateDialog:131. |

## What was NOT done in this session

- No UNREACHABLE label: no row lacks a printed caller/registration, and no saved
  full-repo grep was run, so no row is claimed unreachable on absence of evidence.
- Build (tools/build_graph.py), sampler (verify_sample.py), check_citations / check_routes /
  check_bytecode_lines, greps on graph_def.py, scan_unreachable, C1: NOT RUN — no full
  local checkout exists in this environment (git clone fails without login). Do not quote
  this file as passing any of them.
- Remaining for merge: printed starter of AddLinkActivity and of AddTagActivity, if the
  merger requires a strict launcher-entry route; confirmation of lambda $n-to-body
  mapping for the initAlertDialog lambdas against bytecode; then the usual one-part-at-a-time
  merge with py_compile + build on a full checkout, plus main-agent spot-check (1 in 5).

STATUS: MERGE-READY PROPOSAL ONLY, 0 VERIFIED FOR MERGE.
Counts: 40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN / 40 total.
