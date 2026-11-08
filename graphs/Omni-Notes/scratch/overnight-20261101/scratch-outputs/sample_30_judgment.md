# Omni-Notes — sample-30 route judgments (fresh, 2026-11-01 UTC)

- Draw: `python3 -I tools/verify_sample.py Omni-Notes 30 20261025` (seed 20261025).
- Routes printed step by step: `scratch/sample_30_routes.txt` (526 steps).
- Method: every step checked against freshly fetched branch source (app files under
  `final_java_only/Omni-Notes/app/Omni-Notes-#745/omniNotes/src/main/java/it/feio/android/omninotes/`,
  manifest + res XMLs, and `fw_src/android-8.1.0_r1/` AOSP files). Branch `verification.csv`
  path rows were read only as background; these verdicts are independent fresh judgments.
- Caveat (applies to all routes): 45 of the 526 route edges carry INFERRED evidence
  (library/generated code: androidx, MaterialDialogs, ButterKnife, EventBus, RxJava,
  SmartLocation, Glide). Those steps were judged on their claim text plus the surrounding
  app code, not on library source, which was not read. They are not counted as errors.
- Caveat (clinit convention, routes 9 and 23): steps of the form `X.<init> -> X.<clinit> ->
  X$1.<init>` are a modelling convention meaning "first use triggers class init"
  (the $1 CREATOR anonymous class is instantiated in static init). Temporally `<clinit>`
  runs before first use, not after the constructor; the edge direction is not a temporal
  claim. Reachability conclusions hold; these are judged correct with this note, not errors.

## Verdicts

| # | Stratum | Method | Verdict | Key evidence (fresh reads) |
|---|---------|--------|---------|----------------------------|
| 1 | NONSTD | DetailFragment.onCoordinatesResolved | correct | menu_attachment (1081) -> showAttachmentsPopup (1279) -> LOCATION -> displayLocationDialog (947) -> getLocation(impl) -> permission lambda -> GeocodeHelper oneFix+2s (91) -> onNext -> impl.onLocationRetrieved (2195) -> internet -> dialog -> positive-button lambda -> typed address -> getCoordinatesFromAddress direct() lambda (!empty guard, 164-170) -> onCoordinatesResolved |
| 2 | NONSTD | SpringImportHelper.lambda$importDataFromSpringpad$0 | correct* | importDataFromSpringpad sets ZipProgressesListener lambda then doImport (67-72). *Library invoking the lambda is INFERRED (standard listener pattern). |
| 3 | NONSTD | SqlParser.removeComments | correct | parseSqlFile(String) -> parseSqlFile(InputStream) -> removeComments (30-49) |
| 4 | NONSTD | DetailFragment.onLocationUnavailable | correct | onTouch edge swipe: SWIPE_MARGIN=30 edge, SWIPE_OFFSET=100 move (ConstantsBase 33-34) -> new DetailFragment -> init -> initViews -> initViewLocation -> auto-location branch PREF_AUTO_LOCATION + new note (700) -> getLocation(detailFragment) -> permission lambda -> GeocodeHelper -> onError (105) -> impl.onLocationUnavailable (2190) -> onLocationUnavailable -> showMessage |
| 5 | INFERRED | RecurrenceHelper.nextReminderFromRecurrenceRule(long,long,String) | correct | SnoozeActivity.onCreate INTENT_NOTE branch -> postpone -> ReminderPickers.pick -> onDateTimeRecurrenceSet -> onRecurrenceReminderPicked (ReminderPickers 60, 66) -> setNextRecurrentReminder -> 2-arg overload when rule non-empty (SnoozeActivity 55-60) -> 3-arg delegation (RecurrenceHelper 56-57) |
| 6 | INFERRED | Attachment.<init>(BaseAttachment) | correct | BackupHelper importNotes -> importNote -> getImportNote -> buildFromJson when non-empty (145-176) -> Note.buildFromJson (152-158: super + new Attachment per BaseAttachment) -> Attachment(BaseAttachment) ctor (42) |
| 7 | INFERRED | DbHelper.deleteNote(long,boolean) | WRONG | See "The one wrong route" below. Label REACHABLE is right; this drawn route is internally inconsistent. |
| 8 | INFERRED | NotificationsHelper.updateMessage(int,String) | correct | createNotification -> updateMessage(String) -> updateMessage(int,String) (166-167) |
| 9 | STATE | Tag$1.<init> | correct | Tag(String,Integer) (37) -> <clinit> -> Tag$1 (CREATOR anon class instantiated in static init, 65). Clinit-convention note above. |
| 10 | STATE | NotificationsHelper.show(long) | correct | show() -> show(0) -> show(long) (142-147); service createNotification path verified |
| 11 | STATE | ListFragment.lambda$null$11 | correct | CAB delete -> deleteNotes dialog OK (lambda$deleteNotes$12) -> BaseActivity.requestPassword (115-130: no locked note -> SUCCEED at once) -> validator callback lambda$null$11 -> deleteNotesExecute |
| 12 | ENV | IdeogramsWordCounter.<init> | correct | CountFactory.getWordCounter -> getCounterInstanceByLocale -> new IdeogramsWordCounter for ja_JP/zh_CN/zh_TW (29-48) |
| 13 | ENV | StorageHelper.getMimeTypeInternal(Context,String) | correct | popup FILES -> startGetContentAction (ACTION_GET_CONTENT) -> onActivityResult FILES -> onActivityResultManageReceivedFiles -> AttachmentTask -> getMimeTypeInternal(Uri) -> (String) (427-429) |
| 14 | ENV | SnoozeActivity.updateNoteReminder(long,Note) | correct | single-note branch -> manageNotification -> updateNoteReminder (102) -> ReminderHelper.addReminder 2-arg -> 3-arg -> AlarmManager.setExact (44-57) -> AlarmReceiver.onReceive -> createNotification -> notificationsHelper.show(note.get_id()) (53, 58, 136) |
| 15 | ENV | ListRemoteViewsFactory.color | correct | ListWidgetService.onGetViewFactory -> new ListRemoteViewsFactory (27-28) -> getViewAt -> color(note,row) (110, 120) -> settings_colors_widget pref (169-183) |
| 16 | ENV | PermissionsHelper.lambda$requestPermissionExecute$1 | correct* | requestPermission -> requestPermissionExecute when not granted -> RxPermissions subscribe lambda (37-60). *RxJava invoking the subscriber is INFERRED. |
| 17 | ENV | DataBackupIntentService.deleteData | correct | IntentService handler -> onHandleIntent dispatch by action (75-82) -> deleteData (154: backup-dir removal + createNotification 172-191) |
| 18 | LONG | Category.<init>(Parcel) | correct | categorize dialog -> "Add category" -> CategoryActivity -> Save -> setResult(RESULT_OK) (156-157) -> DetailFragment.onActivityResult CATEGORY reads Parcelable "category" (1438-1443) -> Parcel.readParcelableCreator finds static CREATOR by reflection (Parcel.java:2867-2900; writeParcelable :1785-1791) -> Category$1.createFromParcel -> new Category(in) (79-82) -> private ctor (26). saveCategory early-returns on empty name (138-141); route carries a typed-name guard on edges leaving saveCategory. |
| 19 | LONG | StorageHelper.createAttachmentFromUri(Context,Uri) | correct | CAB merge -> merge() -> NotesMergeEvent -> onEventAsync -> NotesHelper.mergeNotes -> addAttachments (keepMergedNotes -> createAttachmentFromUri per attachment, 70-73) -> 2-arg -> 3-arg (456-457) -> getMimeTypeInternal(Uri) (481) |
| 20 | LONG | DynamicNavigationLookupTable.<init> | correct | MainMenuTask doInBackground -> buildMainMenu -> checkSkippableItem -> getInstance (126) -> creates if null (45-50) |
| 21 | LONG | DetailFragment$3.onClick | correct | menu checklist_off (1094) -> toggleChecklist (1152: checklist active + checked>0 -> MaterialDialog) -> OK-button SingleButtonCallback onClick ($3) -> toggleChecklist2 |
| 22 | LONG | DbHelper.deleteCategory | correct | drawer long-press category -> CategoryMenuTask.buildCategoryMenuLongClickEvent (144) -> editTag (150) -> MainActivity.editTag (215-220) -> ListFragment.editCategory (1463-1467) -> CategoryActivity -> Delete (ButterKnife ViewBinding doClick, INFERRED generated code) -> deleteCategory (163) -> confirmation dialog (165-188) -> onPositive lambda$deleteCategory$0 (170-187) -> db.deleteCategory (180) |
| 23 | LONG | Attachment$1.<init> | correct | popup SKETCH -> takeSketch -> SketchFragment -> draw (SketchView.onTouch) -> Back -> SketchFragment.save() (getBitmap non-null guard: SketchView 204-207; save sets sketchUri, SketchFragment 209/219) -> popBackStack -> DetailFragment.onActivityCreated attaches sketch (385-388: sketchUri != null -> new Attachment(sketchUri, MIME_TYPE_SKETCH)) -> Attachment(Uri,String) ctor (31) -> <clinit> -> $1 (CREATOR anon, 85). Clinit-convention note above. |
| 24 | PLAIN | NotificationChannels.getChannels | correct | OmniNotes.onCreate -> initNotificationChannels (92) -> getChannels when SDK_INT > 26 (55-57, true on API 27) |
| 25 | PLAIN | OmniNotes.getSharedPreferences | correct | LogDelegate.d -> isFileLoggingEnabled -> getSharedPreferences with first-call null guard (92-94) |
| 26 | PLAIN | LanguageHelper.setLocale | correct | BaseActivity.attachBaseContext -> LanguageHelper.updateLanguage (45) -> setLocale (60) |
| 27 | PLAIN | BaseActivity.onCreate | correct | MainActivity.onCreate -> super.onCreate -> BaseActivity.onCreate; onResume -> LogDelegate.d chain consistent |
| 28 | PLAIN | MainActivity.initUI | correct | MainActivity.onCreate (93-108) -> initUI (101) |
| 29 | PLAIN | IntroActivity.mustRun | correct | MainActivity.onCreate:103 -> IntroActivity.mustRun() (static boolean: !debug && !tour-complete, intro/IntroActivity.java) -> startActivity IntroActivity when true |
| 30 | PLAIN | OmniNotes.enableStrictMode | correct | OmniNotes.onCreate -> enableStrictMode (90), guarded by initLeakCanary() false in the app's own process (83-85, 104-110: true only in LeakCanary's analyzer process) |

## Totals

- correct 29, fixed 0, wrong 1, unclear 0.
- Error rate = (fixed + wrong) / (correct + fixed + wrong) = (0 + 1) / (29 + 0 + 1) = **1/30 = 0.0333**.

## The one wrong route (DbHelper.deleteNote(long,boolean), 24 steps)

Drawn route: FAB long-press -> new note (S_DETAIL@NEW, ListFragment 266-285) -> Back ->
saveAndExit (MainActivity 271-276; DetailFragment 1547-1553) -> saveNote -> SaveNoteTask ->
onNoteSaved (1612) -> deleteMergedNotes (1616) -> NoteProcessorDelete -> deleteNote(Note) ->
deleteNote(Note,boolean) -> deleteNote(long,boolean), with STATE "the open note is the result
of Merge".

Why it fails, on fresh evidence: `deleteMergedNotes` does something only when
`mergedNotesIds != null` (DetailFragment 1627-1637). `mergedNotesIds` is set only from the
`"merged_notes"` intent extra (DetailFragment 508), which is put on the intent by the Merge
flow (ListFragment.onEventAsync 1755). A FAB-created new note never carries that extra, so
on the FAB path `deleteMergedNotes` is a no-op and the target is unreachable by this route.
The STATE ("open note is the result of Merge") contradicts the route's own steps 9-11
(FAB new note): a STATE cannot express how an editor was opened. The label REACHABLE is
still right — a real Merge path to this method exists — but this drawn best route is not
a consistent route to it. Fixing it properly needs its own editor context (e.g. @MERGE)
with its own Back/save chain, i.e. a graph-model change, not a one-edge edit; no local
graph fix was attempted (see DECISIONS.md). This matches the branch `readme_notes.md`
"Limits" section and the branch path row (result=wrong), independently re-derived here.

## Fixes applied

None. No route was judged "fixed" (an error found AND corrected in the local graph mirror).
The single wrong route is a documented modelling limit (above), not a correctable edge
error. The redrawn sample is therefore the same draw; see `scratch/sample_30_redrawn.txt`.
