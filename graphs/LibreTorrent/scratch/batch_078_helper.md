# LibreTorrent batch 78 source audit

Membership is exactly the 40 batch 78 rows printed at the top of `batch_078_helper_printed.txt`. Evidence is bounded to AddTagDialog lifecycle/actions, AddTagState/ViewModel methods, AddTorrentActivity lifecycle/URI/error handling, and source/manifest launch searches. All rows remain OPEN because complete UI-to-dialog/activity entry paths and every callback/branch through their target methods have not been traced end-to-end. Listener and Rx callback bodies printed in app source still need their parent registration/subscription paths verified. No candidate is labeled unreachable based on a missing caller match.

| # | Method | Finding | Printed source / unresolved route |
|---:|---|---|---|
| 1 | `AddTagDialog.lambda$addTag$5()V` | OPEN | `AddTagDialog.java:200+`; Rx success callback body printed; complete dialog entry and subscription path unresolved. |
| 2 | `AddTagDialog.lambda$addTag$6(Throwable)V` | OPEN | `AddTagDialog.java:200+`; Rx error callback body printed; complete dialog entry and subscription path unresolved. |
| 3 | `AddTagDialog.lambda$initAlertDialog$2(View)V` | OPEN | Alert button callback body printed; dialog launch and button dispatch path unresolved. |
| 4 | `AddTagDialog.lambda$initAlertDialog$3(View)V` | OPEN | Alert button callback body printed; dialog launch and button dispatch path unresolved. |
| 5 | `AddTagDialog.lambda$initAlertDialog$4(DialogInterface)V` | OPEN | Dismiss callback body printed; dialog lifecycle/dispatch route unresolved. |
| 6 | `AddTagDialog.lambda$initLayoutView$1(View)V` | OPEN | View click callback body printed; full dialog entry and click listener route unresolved. |
| 7 | `AddTagDialog.lambda$onResume$0(DialogInterface,int,KeyEvent)Z` | OPEN | Key listener body printed; dialog lifecycle and key dispatch route unresolved. |
| 8 | `AddTagDialog.newInstance(TagInfo)AddTagDialog` | OPEN | `AddTagDialog.java:67+`; factory and caller search printed; full caller UI route unresolved. |
| 9 | `AddTagDialog.onAttach(Context)V` | OPEN | `AddTagDialog.java:78+`; lifecycle override printed; framework callback entry not independently traced. |
| 10 | `AddTagDialog.onBackPressed()V` | OPEN | `AddTagDialog.java:225+`; callback body printed; key/back dispatch route unresolved. |
| 11 | `AddTagDialog.onCreateDialog(Bundle)Dialog` | OPEN | `AddTagDialog.java:112+`; body printed; fragment-manager/framework dialog route unresolved. |
| 12 | `AddTagDialog.onResume()V` | OPEN | `AddTagDialog.java:87+`; lifecycle and listener setup printed; framework callback route unresolved. |
| 13 | `AddTagDialog.onStop()V` | OPEN | `AddTagDialog.java:104+`; lifecycle cleanup printed; framework callback route unresolved. |
| 14 | `AddTagDialog$1.<init>(AddTagDialog)V` | OPEN | Anonymous `TextWatcher` construction printed; view/listener registration parent route unresolved. |
| 15 | `AddTagDialog$1.afterTextChanged(Editable)V` | OPEN | TextWatcher callback body printed; framework text-change dispatch route unresolved. |
| 16 | `AddTagDialog$1.beforeTextChanged(CharSequence,int,int,int)V` | OPEN | TextWatcher callback body printed; framework text-change dispatch route unresolved. |
| 17 | `AddTagDialog$1.onTextChanged(CharSequence,int,int,int)V` | OPEN | TextWatcher callback body printed; framework text-change dispatch route unresolved. |
| 18 | `AddTagState.<init>()V` | OPEN | `AddTagState.java` source printed; containing view-model/state construction route unresolved. |
| 19 | `AddTagState.getColor()int` | OPEN | `AddTagState.java:53+`; accessor body and callers printed; complete UI route unresolved. |
| 20 | `AddTagState.getExistsTagId()Long` | OPEN | `AddTagState.java:33+`; accessor body and callers printed; complete UI route unresolved. |
| 21 | `AddTagState.getName()String` | OPEN | `AddTagState.java:43+`; accessor body and callers printed; complete UI route unresolved. |
| 22 | `AddTagState.setColor(int)V` | OPEN | `AddTagState.java:57+`; setter body and callers printed; complete UI route unresolved. |
| 23 | `AddTagState.setExistsTagId(Long)V` | OPEN | `AddTagState.java:37+`; setter body and callers printed; complete UI route unresolved. |
| 24 | `AddTagState.setName(String)V` | OPEN | `AddTagState.java:47+`; setter body and callers printed; complete UI route unresolved. |
| 25 | `AddTagViewModel.<init>(Application)V` | OPEN | `AddTagViewModel.java:34+`; constructor/dependency setup printed; view-model provider route unresolved. |
| 26 | `AddTagViewModel.lambda$saveTag$0(Long,TagInfo)Object` | OPEN | `AddTagViewModel.java:55+`; repository transaction lambda printed; subscription/execution route unresolved. |
| 27 | `AddTagViewModel.saveTag()Completable` | OPEN | `AddTagViewModel.java:55+`; returned Rx operation and dialog subscriber printed; full dialog entry route unresolved. |
| 28 | `AddTagViewModel.setInitValues(TagInfo)V` | OPEN | `AddTagViewModel.java:45+`; method and dialog caller printed; complete dialog construction route unresolved. |
| 29 | `AddTagViewModel.setRandomColor()V` | OPEN | `AddTagViewModel.java:51+`; method and dialog caller printed; complete dialog entry route unresolved. |
| 30 | `AddTagViewModel$TagAlreadyExistsException.<init>()V` | OPEN | Exception declaration printed; route depends on storage/Rx error path not fully traced. |
| 31 | `AddTorrentActivity.<clinit>()V` | OPEN | Activity source/class constants printed; activity class initialization through an entry not traced. |
| 32 | `AddTorrentActivity.<init>()V` | OPEN | Activity source printed; Android activity instantiation route unresolved. |
| 33 | `AddTorrentActivity.addTorrent()V` | OPEN | `AddTorrentActivity.java:362+`; body and UI callback callers printed; full manifest/intent route unresolved. |
| 34 | `AddTorrentActivity.fillMutableParams()V` | OPEN | `AddTorrentActivity.java:142+`; lifecycle caller printed; complete activity entry route unresolved. |
| 35 | `AddTorrentActivity.finish()V` | OPEN | `AddTorrentActivity.java:565+`; override/body printed; framework/activity route unresolved. |
| 36 | `AddTorrentActivity.getUri()Uri` | OPEN | `AddTorrentActivity.java:350+`; URI extraction body printed; full incoming intent/manifest route unresolved. |
| 37 | `AddTorrentActivity.handleAddException(Throwable)V` | OPEN | `AddTorrentActivity.java:391+`; exception handling body printed; upstream add operation path unresolved. |
| 38 | `AddTorrentActivity.handleAlertDialogEvent(BaseAlertDialog.Event)V` | OPEN | `AddTorrentActivity.java:237+`; event handler/subscription context printed; event-bus/Rx delivery route unresolved. |
| 39 | `AddTorrentActivity.handleDecodeException(Throwable)V` | OPEN | `AddTorrentActivity.java:452+`; error handler body printed; decode failure branch and incoming URI route unresolved. |
| 40 | `AddTorrentActivity.initLayout()V` | OPEN | `AddTorrentActivity.java:277+`; body and lifecycle context printed; full activity entry route unresolved. |

Count: 40 plan rows = 40 OPEN, 0 REACHABLE labels, 0 UNREACHABLE labels. No graph edits or coverage evidence were used.
