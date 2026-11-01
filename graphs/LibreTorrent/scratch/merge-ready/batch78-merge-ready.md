**CORRECTION 2026-11-01: push statements in this file are superseded — this file was pushed 2026-11-01 as commit 5e0983f to branch work-2026-10-31, UNVERIFIED, before [L]. Nothing in it is merged or verified for merge.**

# LibreTorrent batch 78 — merge-ready file (UNVERIFIED, NOT merged)

Repo: bugfixops/ground-truth-results, branch work-2026-10-31 only. Never main or result.
Pushed 2026-11-01 as 5e0983f (UNVERIFIED, before [L]). No edit to graph_def.py, out/, verification.csv, PROGRESS_V2, AGENT_NOTES,
tools/, or another worker's files. No build, sampler, grep, or C1 count is claimed:
build/C1/sampler/grep = NOT RUN in this session. Build and C1 run on the user's Mac
after a push; until then they are marked "not run", never passed.

## Membership — verified first, not guessed

Exactly the 40 rows for batch 78 in `handoff/LIBRETORRENT_BATCH_PLAN.tsv`, taken from
the local plan copy `~/workspace/agent27-plan.tsv` (4,732 rows total; plan blob SHA
`0104806dd666c840049b3db52823d4b384fa1c92`), all TODO_CANDIDATE_REACHABLE in the
plan, in plan order:
AddTagDialog rows 1-17, AddTagState rows 18-24, AddTagViewModel rows 25-30,
AddTorrentActivity rows 31-40.
Input, not result: `~/workspace/libretorrent-batch78-proposal.md` (Agent 28) and the
batch 77 file in this same session for the shared AddTagDialog/AddTagActivity
trunk. Every row below was re-judged from source freshly printed in this session;
no proposal verdict was copied as a result. No label changed from the input
proposal on re-derivation; two citation refinements are recorded below
(rows 33 and 35).

## Printed source used in this session — all fresh connector fetches, one file at a time with pauses, branch work-2026-10-31, saved in ~/workspace/b7778-src/

Base path for all files:
`final_java_only/LibreTorrent/app/LibreTorrent-#3.5.2/app/src/main/java/org/proninyaroslav/libretorrent/`
- `ui/addtag/AddTagDialog.java` — 233 lines, SHA `bef075da2e784d7c…`
- `ui/addtag/AddTagState.java` — 61 lines, SHA `1db66744e4a47eda…`
- `ui/addtag/AddTagViewModel.java` — 78 lines, SHA `37a8edbf24733718…`
- `ui/addtag/AddTagActivity.java` — 84 lines, SHA `6844ebea6ecc7595…`
- `ui/addtorrent/AddTorrentActivity.java` — 577 lines, SHA `41e027a5ac0998d0…`
- `ui/addlink/AddLinkDialog.java` — 316 lines, SHA `571afec025b0eefc…` (for the AddTorrentActivity entry: addLink)
- `ui/addlink/AddLinkActivity.java` — 47 lines, SHA `c6d228e92b27e76d…` (for the AddLinkDialog entry, which anchors the AddTorrentActivity entry)
- No fresh HTTP 429 was hit in this session. No search_code result was used as evidence of absence (no search was run).
- Line-number note: the fresh prints are 1 line shorter than the input's counts
  for AddTagDialog (233 vs 234), AddTagActivity (84 vs 85) and AddTorrentActivity
  (577 vs 578). Citations below use the fresh numbering; routes are unchanged.
  Two refinements vs the input: row 33's finish calls in addTorrent are at
  :375 (success) and :383 (TorrentAlreadyExists), not :375/:382; row 35's
  finish calls are at addTorrent:375/:383, handleAlertDialogEvent:255/:261,
  onOptionsItemSelected home:556, onBackPressed:575 — all freshly verified.

## Entry trunk (freshly printed)

- AddTagDialog entry IS printed: `AddTagActivity.onCreate:47-60` shows the dialog
  via AddTagDialog.newInstance + show (:58-59); AddTagDialog.onCreateDialog:112-134
  calls initLayoutView:131, initAlertDialog:132, and setInitValues:121 /
  setRandomColor:124. That anchors rows 1-17 (dialog lambdas + TextWatcher) and,
  via the dialog, rows 18-30 (AddTagState/AddTagViewModel, constructed and used
  through the dialog and its ViewModel).
- AddTorrentActivity entry IS printed: AddLinkDialog.addLink (`ui/addlink/AddLinkDialog.java:260-287`)
  builds `Intent(activity, AddTorrentActivity.class)` with TAG_URI extra at :283
  and `startActivity(i)` at :285; AddTorrentActivity.getUri (row 36) also handles
  an implicit intent (getData / EXTRA_TEXT). Framework instantiation then runs
  onCreate:97-140, which anchors rows 31-40. The AddLinkDialog entry itself is
  now also printed fresh (AddLinkActivity.onCreate:31-32, see batch 77 file),
  so the AddTorrentActivity chain is no longer dependent on an unprinted
  dialog-display step.
- Remaining strict-entry gap (recorded, not decided): who starts AddTagActivity
  itself and who starts AddLinkActivity itself (launcher / intent step) was NOT
  printed in this session. Under the anchor convention used here, the rows
  below are REACHABLE proposed. Under a strict launcher-entry rule, all 40
  rows would revert to OPEN, because every route here ultimately anchors at
  AddTagActivity or at AddLinkActivity -> AddLinkDialog -> AddTorrentActivity.
  This is a project convention the merger must decide; it is NOT decided in
  this file, and it changes no label under the anchor convention.
- Lambda $n mapping: the AddTagDialog initAlertDialog SET is printed (two View
  onClick bodies + one DialogInterface onShow body), but the plan signatures
  order them $2=(View), $3=(View), $4=(DialogInterface), i.e. the onShow body
  is $4, not the first in source order — so $n-to-body mapping is marked
  INFERRED for rows 3-5, not SOURCE. The same caution applies to AddTag
  lambda$addTag$5/$6 (rows 1-2): the success/error bodies are printed, the $n
  assignment follows the plan's signature order and is INFERRED. Rows 6-7
  (initLayoutView$1, onResume$0) each have a single candidate body in their
  method, but are still marked INFERRED for $n identity consistency. A $n swap
  within a group would not change any label; the merger must confirm
  $n-to-body mapping against bytecode if it requires it.
- confirmed_by convention used here (per-row, as in the input proposal):
  SOURCE = a direct app-to-app call site naming the method is printed in app
  source (including a printed listener body that calls it); INFERRED = the
  method is reached only through unprinted framework/library dispatch
  (DialogFragment/Activity lifecycle, view-click/key dispatch, Rx dispatch,
  JVM class initialisation) where the registration or entry is printed.
  Under the whole-route INFERRED convention used in some earlier batches
  (e.g. batch 14), all REACHABLE rows would flip to INFERRED; labels are
  unaffected. That convention choice is NOT decided here.

## Counts — mechanically verified after writing (40 rows, sequence 1-40 intact, no gaps, no duplicates)

- REACHABLE proposed: 40 / 40
- UNREACHABLE proposed: 0 / 40
- OPEN: 0 / 40
- confirmed_by: SOURCE 28, INFERRED 12
- Verified for merge: 0 / 40. Still required: main-agent spot-check (1 in 5),
  py_compile, build, Mac build/C1 — all NOT RUN here.

## Undecided conventions — flagged per row, NOT decided

- Strict-entry: applies to ALL 40 REACHABLE proposals (see trunk above).
- Lambda $n mapping: rows 1-7, 26 (INFERRED throughout).
- <clinit> timing: row 31 INFERRED — TAG at AddTorrentActivity.java:73 is not a
  compile-time constant, so a <clinit> exists; it runs on first class use,
  i.e. framework instantiation of the activity after AddLinkDialog.addLink
  startActivity. Whether <clinit> counts as REACHABLE on first-use evidence
  alone is undecided project-wide; flagged, not decided.
- Framework-dispatch policy: rows 9, 12-13, 14, 32 are SOURCE in this file on
  the per-row convention above (printed show/registration + standard
  DialogFragment/Activity dispatch), but under a stricter policy requiring a
  printed app-side call naming the method itself, lifecycle rows 9, 12-13
  and the implicit constructors 14, 32 would fall to INFERRED/OPEN. Flagged,
  not decided. No row is UNREACHABLE on this account.
- No migration-gate, binding-variant, binding-getViewModel, Room-finalize,
  or $N-mapping issue occurs in this row set (no such methods are in batch 78).

## Per-row table — freshly re-derived, UNVERIFIED, 0 verified for merge

Short prefix: `T/` = `ui/addtag/`, `A/` = `ui/addtorrent/`, `L/` = `ui/addlink/`.
All files under the source root above.

| # | Method (batch row) | Proposed label | Kind / confirmed_by | Printed citations and route (fresh prints, this session) |
|---|---|---|---|---|
| 1 | `AddTagDialog.lambda$addTag$5 ()V` | REACHABLE proposed | — / INFERRED | `T/AddTagDialog.java:200-205`: the subscribe success lambda in addTag: () -> finish(OK). Rx subscribe dispatch not printed from source, hence INFERRED; registration + body printed. Called via addTag (positive-button click, rows 3/4 set). |
| 2 | `AddTagDialog.lambda$addTag$6 (Throwable)V` | REACHABLE proposed | — / INFERRED | `T/AddTagDialog.java:200-221`: the subscribe error lambda in addTag: TagAlreadyExistsException -> "tag already exists" toast, else log + "add tag failed" toast. Same Rx caveat as row 1. |
| 3 | `AddTagDialog.lambda$initAlertDialog$2 (View)V` | REACHABLE proposed | — / INFERRED | One of the two View onClick bodies inside initAlertDialog:185-193 (add -> addTag, cancel -> finish CANCEL). $n-to-body mapping unverified (see trunk note). Installed by the onShow listener; initAlertDialog called from onCreateDialog:132. |
| 4 | `AddTagDialog.lambda$initAlertDialog$3 (View)V` | REACHABLE proposed | — / INFERRED | The other View onClick body inside initAlertDialog:185-193. Same caveat as row 3. |
| 5 | `AddTagDialog.lambda$initAlertDialog$4 (DialogInterface)V` | REACHABLE proposed | — / INFERRED | `T/AddTagDialog.java:185-193`: the setOnShowListener body itself (DialogInterface arg), which installs the add/cancel button listeners. $n follows plan signature order, not source order — INFERRED. |
| 6 | `AddTagDialog.lambda$initLayoutView$1 (View)V` | REACHABLE proposed | — / INFERRED | `T/AddTagDialog.java:153-155`: color.setOnClickListener((v) -> ColorPickerDialog.newBuilder().setColor(viewModel.state.getColor()).show(activity)). initLayoutView called from onCreateDialog:131; the picker callback lands in AddTagActivity.onColorSelected (batch 77 row 30). |
| 7 | `AddTagDialog.lambda$onResume$0 (DialogInterface,int,KeyEvent)Z` | REACHABLE proposed | — / INFERRED | `T/AddTagDialog.java:87-101` onResume: getDialog().setOnKeyListener lambda; BACK + ACTION_DOWN -> onBackPressed:94. |
| 8 | `AddTagDialog.newInstance (TagInfo)AddTagDialog` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:67-75`: new AddTagDialog, putParcelable TAG_INIT_INFO, setArguments. Called from AddTagActivity.onCreate:58 (printed, batch 77 file). |
| 9 | `AddTagDialog.onAttach (Context)V` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:78-85`: super.onAttach + activity cast. Standard DialogFragment lifecycle after the printed show at AddTagActivity:59. Lifecycle-policy flag applies. |
| 10 | `AddTagDialog.onBackPressed ()V` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:225-227`: finish(..., BACK). Called from onResume key listener:94 and AddTagActivity.onBackPressed (batch 77 row 29). |
| 11 | `AddTagDialog.onCreateDialog (Bundle)Dialog` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:112-134`: ViewModelProvider get AddTagViewModel:117-118, setInitValues:121 or setRandomColor:124, binding inflate, initLayoutView:131, initAlertDialog:132, returns alert. |
| 12 | `AddTagDialog.onResume ()V` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:87-101`: installs back-key listener (row 7). |
| 13 | `AddTagDialog.onStop ()V` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:104-108`: disposables.clear. Standard lifecycle. |
| 14 | `AddTagDialog$1.<init> (AddTagDialog)V` | REACHABLE proposed | — / INFERRED | Anonymous TextWatcher instantiated at `T/AddTagDialog.java:138-152` inside initLayoutView (new TextWatcher(){...}); framework dispatch, hence INFERRED for the constructor's call path. |
| 15 | `AddTagDialog$1.afterTextChanged (Editable)V` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:148-151`: clears nameLayout error. Registered via addTextChangedListener:138. |
| 16 | `AddTagDialog$1.beforeTextChanged (CharSequence,int,int,int)V` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:140-141`: empty body; same registration as row 15. Empty framework callback, still registered and reachable. |
| 17 | `AddTagDialog$1.onTextChanged (CharSequence,int,int,int)V` | REACHABLE proposed | — / SOURCE | `T/AddTagDialog.java:144-145`: empty body; same registration as row 15. |
| 18 | `AddTagState.<init> ()V` | REACHABLE proposed | — / SOURCE | Implicit constructor, invoked by AddTagViewModel.<init> at `T/AddTagViewModel.java:41` (state = new AddTagState()). |
| 19 | `AddTagState.getColor ()I` | REACHABLE proposed | — / SOURCE | `T/AddTagState.java:53-55`. Direct printed callers: AddTagDialog.onCreateDialog:123 (== -1 test), initLayoutView:154 (picker initial colour), AddTagViewModel.saveTag:59/61 (TagInfo construction). Data-binding @Bindable path not needed — direct calls suffice. |
| 20 | `AddTagState.getExistsTagId ()Long` | REACHABLE proposed | — / SOURCE | `T/AddTagState.java:33-35`. Direct printed callers: AddTagDialog.initAlertDialog:174/177 (add-vs-edit title/button), AddTagViewModel.saveTag:57 (insert-vs-update branch). |
| 21 | `AddTagState.getName ()String` | REACHABLE proposed | — / SOURCE | `T/AddTagState.java:43-45`. Direct printed callers: AddTagDialog.checkName:160 (empty test, via viewModel.state.getName()), AddTagViewModel.saveTag:59/61. |
| 22 | `AddTagState.setColor (int)V` | REACHABLE proposed | — / SOURCE | `T/AddTagState.java:57-60` (+ notifyPropertyChanged). Direct printed callers: AddTagActivity.onColorSelected:79, AddTagViewModel.setInitValues:48, setRandomColor:52. |
| 23 | `AddTagState.setExistsTagId (Long)V` | REACHABLE proposed | — / SOURCE | `T/AddTagState.java:37-40` (+ notifyPropertyChanged). Direct printed caller: AddTagViewModel.setInitValues:46. |
| 24 | `AddTagState.setName (String)V` | REACHABLE proposed | — / SOURCE | `T/AddTagState.java:47-50` (+ notifyPropertyChanged). Direct printed caller: AddTagViewModel.setInitValues:47. |
| 25 | `AddTagViewModel.<init> (Application)V` | REACHABLE proposed | — / SOURCE | `T/AddTagViewModel.java:38-43`: super + state = new AddTagState() + tagRepo lookup. Obtained via provider.get(AddTagViewModel.class) in AddTagActivity.onCreate:52 and AddTagDialog.onCreateDialog:117-118. |
| 26 | `AddTagViewModel.lambda$saveTag$0 (Long,TagInfo)Object` | REACHABLE proposed | — / INFERRED | `T/AddTagViewModel.java:63-74`: the Completable.fromCallable body in saveTag (captures existsTagId + info): getByName -> throw TagAlreadyExistsException (row 30) or insert, else update. Rx fromCallable dispatch not printed from source, hence INFERRED; subscribed in AddTagDialog.addTag:200. |
| 27 | `AddTagViewModel.saveTag ()Completable` | REACHABLE proposed | — / SOURCE | `T/AddTagViewModel.java:55-75`. Called from AddTagDialog.addTag:200. |
| 28 | `AddTagViewModel.setInitValues (TagInfo)V` | REACHABLE proposed | — / SOURCE | `T/AddTagViewModel.java:45-49`: setExistsTagId/setName/setColor from info. Called from AddTagDialog.onCreateDialog:121 when initInfo != null. |
| 29 | `AddTagViewModel.setRandomColor ()V` | REACHABLE proposed | — / SOURCE | `T/AddTagViewModel.java:51-53`: setColor(Utils.getRandomColor()). Called from AddTagDialog.onCreateDialog:124 when colour == -1. |
| 30 | `AddTagViewModel$TagAlreadyExistsException.<init> ()V` | REACHABLE proposed | — / SOURCE | Implicit constructor of the static exception class at `T/AddTagViewModel.java:77`. Thrown in the saveTag lambda:67; caught by instanceof in AddTagDialog.addTag error lambda:206. |
| 31 | `AddTorrentActivity.<clinit> ()V` | REACHABLE proposed | — / INFERRED | `A/AddTorrentActivity.java:73`: TAG = AddTorrentActivity.class.getSimpleName() is not a compile-time constant, so a <clinit> exists; it runs on first class use, i.e. framework instantiation of the activity after AddLinkDialog.addLink startActivity (`L/AddLinkDialog.java:283-285`). Class-load step INFERRED. <clinit>-timing flag applies. |
| 32 | `AddTorrentActivity.<init> ()V` | REACHABLE proposed | — / INFERRED | Implicit default constructor; no explicit constructor in `A/AddTorrentActivity.java`. Framework instantiates the activity (standard AppCompatActivity dispatch) after the printed startActivity / implicit-intent entry. |
| 33 | `AddTorrentActivity.addTorrent ()V` | REACHABLE proposed | — / SOURCE | `A/AddTorrentActivity.java:362-389`: empty-name Snackbar guard, viewModel.addTorrent() -> finish(), TorrentAlreadyExists -> toast + finish, else handleAddException:386. Called from onOptionsItemSelected:558 for the add menu item. Refinement vs input: finish calls at :375 (success) and :383 (TorrentAlreadyExists), freshly verified. |
| 34 | `AddTorrentActivity.fillMutableParams ()V` | REACHABLE proposed | — / SOURCE | `A/AddTorrentActivity.java:142-168`: copies four add-torrent preferences into viewModel.mutableParams. Called from onCreate:131. |
| 35 | `AddTorrentActivity.finish ()V` | REACHABLE proposed | — / SOURCE | `A/AddTorrentActivity.java:565-569`: viewModel.finish() + super.finish(). Called from addTorrent:375/383, handleAlertDialogEvent err-report branches:255/261, onOptionsItemSelected home:556, onBackPressed:575. Refinement vs input recorded above. |
| 36 | `AddTorrentActivity.getUri ()Uri` | REACHABLE proposed | — / SOURCE | `A/AddTorrentActivity.java:350-360`: getData, else EXTRA_TEXT, else TAG_URI parcelable extra. Called from observeDecodeState:310 (UNKNOWN branch -> startDecode). |
| 37 | `AddTorrentActivity.handleAddException (Throwable)V` | REACHABLE proposed | — / SOURCE | `A/AddTorrentActivity.java:391-421`: NoFilesSelected / FreeSpace Snackbars, else log + error dialog. Called directly from addTorrent catch:386. |
| 38 | `AddTorrentActivity.handleAlertDialogEvent (BaseAlertDialog$Event)V` | REACHABLE proposed | — / INFERRED | `A/AddTorrentActivity.java:237-275`: err-report dialog positive/negative -> finish, perm-denied dialog handling. Registered by method reference dialogViewModel.observeEvents().subscribe(this::handleAlertDialogEvent) at:189, subscribed in onStart:183 via subscribeAlertDialog:187-190. Rx/event dispatch not printed from source, hence INFERRED; body + registration printed. |
| 39 | `AddTorrentActivity.handleDecodeException (Throwable)V` | REACHABLE proposed | — / SOURCE | `A/AddTorrentActivity.java:452-540`: Decode / FetchLink / IllegalArgument / IOException / OutOfMemory branches, each showing an error dialog. Called directly from onStopDecode:341 when e != null (onStopDecode reached from observeDecodeState ERROR branch). |
| 40 | `AddTorrentActivity.initLayout ()V` | REACHABLE proposed | — / SOURCE | `A/AddTorrentActivity.java:277-305`: toolbar title + home-as-up, pager adapter, TabLayoutMediator attach. Called from onCreate:138. |

## What was NOT done in this session

- No UNREACHABLE label: every row has a printed caller, registration, or standard
  framework/library dispatch with a printed registration; no saved full-repo grep was
  run, so no row is claimed unreachable on absence of evidence.
- Build (tools/build_graph.py), sampler (verify_sample.py), check_citations / check_routes /
  check_bytecode_lines, greps on graph_def.py, scan_unreachable, C1: NOT RUN — no full
  local checkout exists in this environment (git clone fails without login). Do not quote
  this file as passing any of them.
- Remaining for merge: printed starter of AddTagActivity and of AddLinkActivity, if the
  merger requires a strict launcher-entry route; confirmation of lambda $n-to-body
  mapping for AddTagDialog initAlertDialog/addTag lambdas against bytecode; then the
  usual one-part-at-a-time merge with py_compile + build on a full checkout, plus
  main-agent spot-check (1 in 5).

STATUS: MERGE-READY PROPOSAL ONLY, 0 VERIFIED FOR MERGE.
Counts: 40 REACHABLE proposed / 0 UNREACHABLE proposed / 0 OPEN / 40 total.
