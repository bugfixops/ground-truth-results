# AnkiDroid check-8 explained — all 169 scan_unreachable.py --callers lines

Source: `handoff/baseline_2026-11-01/AnkiDroid/8b_scan_callers.txt` (169 method lines + 1 summary line).
Each entry names the method, its UNREACHABLE kind, every bytecode caller from the scan, and the
helper explanation(s) covering it (audit PASS 2026-11-01; verdicts in `finish/work/AnkiDroid/audit/B4/AUDIT.md`).
Covering helpers: b4-plotsheet-prepare (PlotSheet.prepareDrawables, 38 lines), b4-decktask-cancelled
(DeckTask.onCancelled, 27 lines), b4-progress-draw (DeckTask$TaskListener.onProgressUpdate 16 +
PlotSheet.drawSingleMode 23 lines), b4-paint-sync (DrawableContainer.paint 11, Syncer.sync 6,
NoteService.importMediaToDirectory 7, MultimediaEditFieldActivity.done 4, AnkiDroidApp.onCreate 4,
MultimediaEditableNote.setField 3, Collection.close 3), b4-remainder (52 remainder-only + 11 mixed lines).
Partition: 106 sibling-only + 52 remainder-only + 11 mixed = 169. Per-base sum 142 (mixed lines counted
per caller base). Method-section pairs: 205 = 142 + 63. 0 routes, 0 label changes arise from B4.
The 8 paint-sync axis-paint pairs are VERIFY-ONLY: they already exist in graph_def_mod/01.py
multi-pair sup() blocks (:3699/:3700, :3711/:3712, :3795/:3796, :3799/:3800) and were NOT duplicated.
The ReliefLegend reason reword (getLegend() has no caller and ReliefDrawer is never constructed, so
the creation site never runs) is applied at graph_def_mod/01.py:3488-3490; the labels and the three
SUPPRESS entries stand. Shared-evidence pointers: plotsheet §0 (common dispatch evidence),
progress-draw shared-evidence sections, remainder counting-convention section — see the helper
files for full text. Section summaries below are the first substantive lines of each helper section.

### 1. AbstractFlashcardViewer$10.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 3. AbstractFlashcardViewer$10.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:3265` (answer/undo tasks never cancelled; the answer
  handler's tasks are ANSWER_CARD and UNDO).

### 2. AbstractFlashcardViewer$8.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 1. AbstractFlashcardViewer$8.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:3392` (shared `_CANCEL_REASON`/`_CANCEL_SOURCE` at
  :3385-3390: DISMISS and UPDATE_FACT tasks never cancelled).

### 3. AbstractFlashcardViewer$9.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 2. AbstractFlashcardViewer$9.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:3393` (same shared cancel reason as $8).
  - Listener: `mUpdateCardHandler`, `AbstractFlashcardViewer.java:511`,

### 4. AbstractFlashcardViewer.calculateDynamicFontSize [branch_never_taken]
Callers (scan): AbstractFlashcardViewer.updateCard (AbstractFlashcardViewer.java:2064); AbstractFlashcardViewer.updateCard@Previewer (AbstractFlashcardViewer.java:2064); AbstractFlashcardViewer.updateCard@Reviewer (AbstractFlashcardViewer.java:2064)
Explained by b4-remainder — ### 1. AbstractFlashcardViewer.calculateDynamicFontSize [branch_never_taken]:
  - Current reason (graph_def.py:3033): only call is in updateCard under
  `if (mCurrentCard == null)` (AbstractFlashcardViewer.java:2063-2064);
  both updateCard callers dereference or guard mCurrentCard first

### 5. AbstractFlashcardViewer.finishNoStorageAvailable [no_trigger_in_app]
Callers (scan): AbstractFlashcardViewer.onActivityResult (AbstractFlashcardViewer.java:1068); AbstractFlashcardViewer.onActivityResult@Previewer (AbstractFlashcardViewer.java:1068); AbstractFlashcardViewer.onActivityResult@Reviewer (AbstractFlashcardViewer.java:1068)
Explained by b4-remainder — ### 2. AbstractFlashcardViewer.finishNoStorageAvailable [no_trigger_in_app]:
  - Current reason (graph_def.py:3020): only caller is onActivityResult when
  resultCode == DeckPicker.RESULT_MEDIA_EJECTED (202); the only code that
  produces 202 is this method itself (its setResult at :1178), so the

### 6. AddContentApi$CompatV1.findDuplicateNotes [closed_by_configuration]
Callers (scan): AddContentApi.findDuplicateNotes(long,String) (AddContentApi.java:162); AddContentApi.findDuplicateNotes(long,List) (AddContentApi.java:177)
Explained by b4-remainder — ### 3. AddContentApi$CompatV1.findDuplicateNotes [closed_by_configuration]:
  - Current reason (graph_def_mod/01.py:7): overridden by
  CompatV2.findDuplicateNotes (AddContentApi.java:702-741); getCompat
  (:594) picks CompatV1 only when the host spec version is below 2, but

### 7. AddContentApi$CompatV1.insertNotes [closed_by_configuration]
Callers (scan): AddContentApi.addNotes (AddContentApi.java:151)
Explained by b4-remainder — ### 4. AddContentApi$CompatV1.insertNotes [closed_by_configuration]:
  - Current reason (graph_def_mod/01.py:2): overridden by
  CompatV2.insertNotes (AddContentApi.java:695-699); same getCompat /
  spec-2 argument as entry 3; CompatV2 does not call super.

### 8. AddContentApi$CompatV1.queryNotes [closed_by_configuration]
Callers (scan): AddContentApi.getNoteCount (AddContentApi.java:186)
Explained by b4-remainder — ### 5. AddContentApi$CompatV1.queryNotes [closed_by_configuration]:
  - Current reason (graph_def.py:6974): overridden by
  CompatV2.queryNotes (AddContentApi.java:689-692); same getCompat /
  spec-2 argument as entry 3; CompatV2 does not call super.

### 9. AddContentApi.hasReadWritePermission [closed_by_api_level]
Callers (scan): AddContentApi.previewNewNote (AddContentApi.java:263)
Explained by b4-remainder — ### 6. AddContentApi.hasReadWritePermission [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:12): only caller is previewNewNote
  (:263), guarded by `SDK_INT < M && !hasReadWritePermission()`; on
  API 27 SDK_INT (27) is not below M (23), so the call short-circuits

### 10. Anki2Importer._srcMediaData [no_trigger_in_app]
Callers (scan): Anki2Importer._importStaticMedia (Anki2Importer.java:591); Anki2Importer._mungeMedia (Anki2Importer.java:652)
Explained by b4-remainder — ### 7. Anki2Importer._srcMediaData [no_trigger_in_app]:
  - Current reason: protected body overridden by AnkiPackageImporter
  (AnkiPackageImporter.java:126-135); the two in-app call sites dispatch
  on an AnkiPackageImporter receiver; no main code constructs a plain

### 11. AnkiActivity.disableViewAnimation [branch_never_taken]
Callers (scan): AnkiActivity.enableViewAnimation (AnkiActivity.java:219)
Explained by b4-remainder — ### 8. AnkiActivity.disableViewAnimation [branch_never_taken]:
  - Current reason: only call is in enableViewAnimation (:219) inside the
  branch guarded by animationDisabled() (:218); animationDisabled reads
  the eInkDisplay preference with default false (AnkiActivity.java:115),

### 12. AnkiDroidApp$ProductionCrashReportingTree.<clinit> [closed_by_configuration]
Callers (scan): AnkiDroidApp.onCreate (AnkiDroidApp.java:166)
Explained by b4-paint-sync — ### 29. `AnkiDroidApp$ProductionCrashReportingTree.<clinit>`:
  - Kind + current reason: `closed_by_configuration` — only
  construction is the `new` at `AnkiDroidApp.java:166`, in the
  `else` branch of `if (BuildConfig.DEBUG)`; debug build, so the

### 13. AnkiDroidApp$ProductionCrashReportingTree.<init> [closed_by_configuration]
Callers (scan): AnkiDroidApp.onCreate (AnkiDroidApp.java:166)
Explained by b4-paint-sync — ### 30. `AnkiDroidApp$ProductionCrashReportingTree.<init>`:
  - Kind + current reason: `closed_by_configuration` — same as (29);
  the entry explicitly notes the automatic CALL from `onCreate`
  must be suppressed (`01.py:3980`).

### 14. AudioField.getImagePath [branch_never_taken]
Callers (scan): MultimediaEditFieldActivity.done (MultimediaEditFieldActivity.java:256); BasicImageFieldController.createUI (BasicImageFieldController.java:91); BasicImageFieldController.onActivityResult (BasicImageFieldController.java:178)
Explained by b4-paint-sync — ### 25. `AudioField.getImagePath`:
  - Kind + current reason: `branch_never_taken` — all interface call
  sites are inside an IMAGE type branch that an `AudioField` never
  takes (`01.py:211`).
Explained by b4-remainder — ### 53. AudioField.getImagePath [branch_never_taken]:
  - Current reason (graph_def_mod/01.py:211): all interface call sites
  are inside an IMAGE type branch that an AudioField never takes — the
  activity done (IMAGE test at :250), NoteService.importMediaToDirectory

### 15. AudioField.getText [branch_never_taken]
Callers (scan): BasicTextFieldController.createUI (BasicTextFieldController.java:73); BasicTextFieldController.createCloneButton (BasicTextFieldController.java:241)
Explained by b4-remainder — ### 48. AudioField.getText [branch_never_taken]:
  - Current reason (graph_def_mod/01.py:223): interface call sites in
  the text controller are guarded — the clone loop skips every field
  whose type is not TEXT before calling getText; the other calls are

### 16. AudioField.isModified [branch_never_taken]
Callers (scan): MultimediaEditableNote.setField (MultimediaEditableNote.java:108)
Explained by b4-paint-sync — ### 33. `AudioField.isModified`:
  - Kind + current reason: `branch_never_taken` — only caller is
  `setField`, inside the same-object guard; every setField caller
  passes a new object or a deserialized copy (`01.py:229`).

### 17. AudioField.setImagePath [branch_never_taken]
Callers (scan): BasicImageFieldController.onActivityResult (BasicImageFieldController.java:175); NoteService.importMediaToDirectory (NoteService.java:186)
Explained by b4-paint-sync — ### 18. `AudioField.setImagePath`:
  - Kind + current reason: `branch_never_taken` — call sites are the
  IMAGE branch of `importMediaToDirectory` and the IMAGE-only image
  controller; neither gives an `AudioField` receiver
Explained by b4-remainder — ### 54. AudioField.setImagePath [branch_never_taken]:
  - Current reason (graph_def_mod/01.py:241): call sites are the image
  branch of NoteService.importMediaToDirectory (case IMAGE) and the
  image controller (built only for IMAGE by the factory). Neither gives

### 18. AudioField.setText [branch_never_taken]
Callers (scan): NoteEditor$11$1.onMenuItemClick (NoteEditor.java:1170); BasicTextFieldController.onDone (BasicTextFieldController.java:341)
Explained by b4-remainder — ### 49. AudioField.setText [branch_never_taken]:
  - Current reason (graph_def_mod/01.py:253): interface call sites
  receive only TextField objects — the note editor text popup item (a
  new TextField), NoteService line 57 (TextField local), and the text

### 19. CardBrowser$13.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 4. CardBrowser$13.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:1748` (UPDATE_FACT task never cancelled; cancel callers
  are SEARCH_CARDS/RENDER_BROWSER_QA only).

### 20. CardBrowser$14.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 5. CardBrowser$14.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:1754` (DISMISS/suspend task never cancelled, same
  cancel-caller argument as $13).

### 21. CardBrowser$15.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 6. CardBrowser$15.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:1760` (DISMISS/delete task never cancelled, same
  cancel-caller argument as $13).

### 22. CardContentProvider.knownRogueClient [closed_by_api_level]
Callers (scan): CardContentProvider.shouldEnforceQueryOrInsertSecurity (CardContentProvider.java:199); CardContentProvider.shouldEnforceUpdateSecurity (CardContentProvider.java:204)
Explained by b4-remainder — ### 9. CardContentProvider.knownRogueClient [closed_by_api_level]:
  - Current reason (graph_def.py:2950): called from
  shouldEnforceQueryOrInsertSecurity (:199) and
  shouldEnforceUpdateSecurity (:204) only as the second operand after

### 23. CardTemplateEditor$1.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 7. CardTemplateEditor$1.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:5714` (ADD_TEMPLATE/REMOVE_TEMPLATE tasks never cancelled).
  - Listener: `mUpdateTemplateHandler`, `CardTemplateEditor.java:84`,

### 24. CardTemplateEditor$1.onProgressUpdate [no_trigger_in_app]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@CardTemplateEditor$1 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A1. CardTemplateEditor$1.onProgressUpdate:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def.py:5734`:
  ADD_TEMPLATE / REMOVE_TEMPLATE bodies (1028-1065) never call
  `publishProgress`; the only ProgressCallback is for the import task (750).

### 25. CardTemplateEditor$CardTemplateFragment$2.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 8. CardTemplateEditor$CardTemplateFragment$2.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:3575` (SAVE_MODEL task never cancelled).
  - Listener: `mSaveModelAndExitHandler` inside the named inner class

### 26. CardTemplateEditor$CardTemplateFragment$2.onProgressUpdate [no_trigger_in_app]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@CardTemplateEditor$CardTemplateFragment$2 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A2. CardTemplateEditor$CardTemplateFragment$2.onProgressUpdate:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def.py:3594`:
  SAVE_MODEL (1070-1079) never publishes; ProgressCallback built only in
  ImportAdd (750).

### 27. CompatV10.detagged [closed_by_api_level]
Callers (scan): DiffEngine.wrapBad (DiffEngine.java:1100); DiffEngine.wrapGood (DiffEngine.java:1104); DiffEngine.wrapMissing (DiffEngine.java:1108)
Explained by b4-remainder — ### 10. CompatV10.detagged [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1053): CompatV16 overrides it
  (CompatV16.java:34-37); base body runs only on API 10-15, not on the
  API 27 path (CompatHelper.java:35-36 selects CompatV21).

### 28. CompatV10.disableDatabaseWriteAheadLogging [closed_by_api_level]
Callers (scan): Collection.close(boolean) (Collection.java:313); DB.<init> (DB.java:76)
Explained by b4-paint-sync — ### 36. `CompatV10.disableDatabaseWriteAheadLogging`:
  - Kind + current reason: `closed_by_api_level` — overridden by
  `CompatV16`; on API 27 `CompatHelper` selects `CompatV21` and the
  nearest override up its chain is `CompatV16`, so this body never
Explained by b4-remainder — ### 55. CompatV10.disableDatabaseWriteAheadLogging [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:4054): overridden by
  CompatV16.disableDatabaseWriteAheadLogging (CompatV16.java:29-32),
  and no override calls super; on API 27 CompatHelper selects

### 29. CompatV10.enableCookiesForFileSchemePages [closed_by_api_level]
Callers (scan): AnkiDroidApp.onCreate (AnkiDroidApp.java:177)
Explained by b4-paint-sync — ### 31. `CompatV10.enableCookiesForFileSchemePages`:
  - Kind + current reason: `closed_by_api_level` — overridden by
  `CompatV12`; on API 27 the `CompatV12` body runs
  (`AnkiDroidApp.onCreate:177`) and this body never does

### 30. CompatV10.flushWebViewCookies [closed_by_api_level]
Callers (scan): AbstractFlashcardViewer.onPause (AbstractFlashcardViewer.java:931)
Explained by b4-remainder — ### 11. CompatV10.flushWebViewCookies [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1053): CompatV21 overrides it
  (CookieManager.flush); base body (CookieSyncManager.sync) does not
  run on API 27. Override verified: CompatV21.java:32.

### 31. CompatV10.getPreferenceSubscreenIntent [closed_by_api_level]
Callers (scan): DeckPicker.onCreate (DeckPicker.java:427); Preferences$7.onPreferenceClick (Preferences.java:339); Preferences$3.onPreferenceClick (Preferences.java:264)
Explained by b4-remainder — ### 12. CompatV10.getPreferenceSubscreenIntent [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1057): CompatV11 overrides it
  (CompatV11.java:40-49); base body does not run on API 11 and up,
  including API 27. Override verified: CompatV11.java:41.

### 32. CompatV10.isImmersiveSystemUiVisible [closed_by_api_level]
Callers (scan): Reviewer$1.onTouch (Reviewer.java:465); AbstractFlashcardViewer$MyGestureDetector.onFling (AbstractFlashcardViewer.java:2667); AbstractFlashcardViewer$MyGestureDetector.onSingleTapConfirmed (AbstractFlashcardViewer.java:2733)
Explained by b4-remainder — ### 13. CompatV10.isImmersiveSystemUiVisible [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1061): CompatV19 overrides it
  (CompatV19.java:90-93); base body (always false) does not run on
  API 27. Override verified: CompatV19.java:91.

### 33. CompatV10.openUrl [closed_by_api_level]
Callers (scan): AnkiActivity.openUrl (AnkiActivity.java:323)
Explained by b4-remainder — ### 14. CompatV10.openUrl [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1065): CompatV16 overrides it
  (Custom Tabs, CompatV16.java:76-87); base body does not run on API 27.
  Override verified: CompatV16.java:77.

### 34. CompatV10.prepareWebViewCookies [closed_by_api_level]
Callers (scan): AnkiDroidApp.onCreate (AnkiDroidApp.java:180)
Explained by b4-paint-sync — ### 32. `CompatV10.prepareWebViewCookies`:
  - Kind + current reason: `closed_by_api_level` — overridden by
  `CompatV21` (empty body); API 27 selects `CompatV21`, so the
  `V10` `CookieSyncManager` body never runs (`01.py:4058`).

### 35. CompatV10.restartActivityInvalidateBackstack [closed_by_api_level]
Callers (scan): NavigationDrawerActivity$2.onCheckedChanged (NavigationDrawerActivity.java:103); NavigationDrawerActivity.onActivityResult (NavigationDrawerActivity.java:231)
Explained by b4-remainder — ### 15. CompatV10.restartActivityInvalidateBackstack [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1069): CompatV11 overrides it
  (TaskStackBuilder restart, CompatV11.java:24-32); base body runs only
  on API 10. Override verified: CompatV11.java:24.

### 36. CompatV10.setFullScreen [closed_by_api_level]
Callers (scan): AbstractFlashcardViewer$21.handleMessage (AbstractFlashcardViewer.java:2767); Reviewer.onCollectionLoaded (Reviewer.java:119)
Explained by b4-remainder — ### 16. CompatV10.setFullScreen [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1073): CompatV19 overrides it
  (sticky immersive flags, no super call, CompatV19.java:25-26); base
  body does not run on API 27. Override verified: CompatV19.java:26.

### 37. CompatV10.setHTML5MediaAutoPlay [closed_by_api_level]
Callers (scan): AbstractFlashcardViewer.fillFlashcard (AbstractFlashcardViewer.java:2283); AbstractFlashcardViewer.fillFlashcard@Previewer (AbstractFlashcardViewer.java:2283)
Explained by b4-remainder — ### 17. CompatV10.setHTML5MediaAutoPlay [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1077): CompatV17 overrides it
  (CompatV17.java:13-16); empty base body does not run on API 27.
  Override verified: CompatV17.java:14.

### 38. CompatV10.setSelectableBackground [closed_by_api_level]
Callers (scan): DeckAdapter.onBindViewHolder (DeckAdapter.java:191)
Explained by b4-remainder — ### 18. CompatV10.setSelectableBackground [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1081): CompatV21 overrides it
  (ripple, CompatV21.java:14-21); base body does not run on API 27.
  Override verified: CompatV21.java:15.

### 39. CompatV10.setStatusBarColor [closed_by_api_level]
Callers (scan): CompatV19.setFullScreen (CompatV19.java:40)
Explained by b4-remainder — ### 19. CompatV10.setStatusBarColor [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1085): CompatV21 overrides it
  (CompatV21.java:36-39); empty base body does not run on API 27.
  Override verified: CompatV21.java:37

### 40. CompatV10.setTtsOnUtteranceProgressListener [closed_by_api_level]
Callers (scan): ReadText$3.onInit (ReadText.java:195)
Explained by b4-remainder — ### 20. CompatV10.setTtsOnUtteranceProgressListener [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:1089): CompatV15 overrides it
  (UtteranceProgressListener, CompatV15.java:13-30); base body
  (deprecated OnUtteranceCompletedListener) does not run on API 27.

### 41. CompatV10.updateWidgetDimensions [closed_by_api_level]
Callers (scan): AnkiDroidWidgetSmall$UpdateService.buildUpdate (AnkiDroidWidgetSmall.java:171); AnkiDroidWidgetSmall.onReceive (AnkiDroidWidgetSmall.java:72)
Explained by b4-remainder — ### 21. CompatV10.updateWidgetDimensions [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:4060): overridden by
  CompatV16.updateWidgetDimensions (CompatV16.java:42-43); API 27
  selects CompatV21, whose chain reaches CompatV16 first, so the empty

### 42. CompatV11.disableDatabaseWriteAheadLogging [closed_by_api_level]
Callers (scan): Collection.close(boolean) (Collection.java:313); DB.<init> (DB.java:76)
Explained by b4-paint-sync — ### 37. `CompatV11.disableDatabaseWriteAheadLogging`:
  - Kind + current reason: `closed_by_api_level` — shadowed by the
  `CompatV16` override, the nearest override above `CompatV21`,
  which does not call `super`; the `rawQuery` PRAGMA body never
Explained by b4-remainder — ### 56. CompatV11.disableDatabaseWriteAheadLogging [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:4062): shadowed by the CompatV16
  override (db.disableWriteAheadLogging), nearest override above
  CompatV21, which does not call super; on API 27 the rawQuery PRAGMA

### 43. CompatV15NookHdOrHdPlus.<init> [closed_by_api_level]
Callers (scan): CompatHelper.<init> (CompatHelper.java:34)
Explained by b4-remainder — ### 22. CompatV15NookHdOrHdPlus.<init> [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:4064): created only when
  isNookHdOrHdPlus() is true AND getSdkVersion() == 15
  (CompatHelper.java:33-34); API 27 fails the SDK test, so this

### 44. CompatV15NookHdOrHdPlus.disableDatabaseWriteAheadLogging [closed_by_api_level]
Callers (scan): Collection.close(boolean) (Collection.java:313); DB.<init> (DB.java:76)
Explained by b4-paint-sync — ### 38. `CompatV15NookHdOrHdPlus.disableDatabaseWriteAheadLogging`:
  - Kind + current reason: `closed_by_api_level` — only reachable
  through a `CompatV15NookHdOrHdPlus` instance, which API 27 never
  creates (needs SDK 15); the method is not on the API 21+
Explained by b4-remainder — ### 57. CompatV15NookHdOrHdPlus.disableDatabaseWriteAheadLogging [closed_by_api_level]:
  - Current reason (graph_def_mod/01.py:4066): only reachable through a
  CompatV15NookHdOrHdPlus instance, which API 27 never creates (needs
  SDK 15, CompatHelper.java:33-34); the method is not on the API 21+

### 45. Connection$CancelCallback.setConnectionManager [branch_never_taken]
Callers (scan): HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback) (HttpSyncer.java:231); HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)@FullSyncer (HttpSyncer.java:231); HttpSyncer.req(String,InputStream,int,JSONObject,CancelCallback)@RemoteMediaServer (HttpSyncer.java:231)
Explained by b4-remainder — ### 23. Connection$CancelCallback.setConnectionManager [branch_never_taken]:
  - Current reason: only call is inside `if (cancelCallback != null)`
  (HttpSyncer.java:230-232); the only 5-argument req call in the source
  root (HttpSyncer.java:148) passes the literal null, and other req

### 46. CustomStudyDialog$4.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 9. CustomStudyDialog$4.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:5350` (REBUILD_CRAM task never cancelled; the auto CALL
  edge from `DeckTask.onCancelled` must be suppressed).

### 47. CustomStudyDialog$4.onProgressUpdate [no_trigger_in_app]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@CustomStudyDialog$4 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A3. CustomStudyDialog$4.onProgressUpdate:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def.py:5364`:
  REBUILD_CRAM (728-733) calls only scheduler rebuild +
  `doInBackgroundUpdateValuesFromDeck`; no `publishProgress` in range.

### 48. DatabaseErrorDialog$2.<init> [branch_never_taken]
Callers (scan): DatabaseErrorDialog.onCreateDialog (DatabaseErrorDialog.java:105)
Explained by b4-remainder — ### 24. DatabaseErrorDialog$2.<init> [branch_never_taken]:
  - Current reason (graph_def.py:5562): the DB_ERROR case (id 1,
  DatabaseErrorDialog.java:96-127) is never entered; DIALOG_DB_ERROR
  (1) has no caller in the source root — ids passed are 0, 2-9 — and

### 49. DeckOptions$DeckPreferenceHack$Editor$2.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 10. DeckOptions$DeckPreferenceHack$Editor$2.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:3731` (conf-change handler tasks never cancelled).
  - Listener: `mConfChangeHandler` inside `DeckPreferenceHack$Editor`

### 50. DeckOptions$DeckPreferenceHack$Editor$2.onProgressUpdate [framework_never_calls]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@DeckOptions$DeckPreferenceHack$Editor$2 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A4. DeckOptions$DeckPreferenceHack$Editor$2.onProgressUpdate:
  - Kind + current reason: `framework_never_calls`. Graph `graph_def.py:3736`:
  no conf task publishes progress; conf-remove body 961-982 publish-free.
  - Caller printed: `DeckTask.java:1312`.

### 51. DeckOptions.addMissingValues [branch_never_taken]
Callers (scan): DeckOptions$DeckPreferenceHack.cacheValues (DeckOptions.java:132)
Explained by b4-remainder — ### 25. DeckOptions.addMissingValues [branch_never_taken]:
  - Current reason (graph_def.py:4112): only call is the JSONException
  catch in DeckPreferenceHack.cacheValues (try block
  DeckOptions.java:95-130); the standard configuration has every key

### 52. DeckPicker$13.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 14. DeckPicker$13.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:351` (UNDO task never cancelled).
  - Listener: inline anonymous listener in `undo()`,

### 53. DeckPicker$14.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 15. DeckPicker$14.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:357` (REPAIR_DECK task never cancelled; body empty).
  - Listener: inline anonymous listener in `repairDeck()`,

### 54. DeckPicker$14.onProgressUpdate [framework_never_calls]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@DeckPicker$14 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A6. DeckPicker$14.onProgressUpdate (= REPAIR_DECK listener):
  - Kind + current reason: `framework_never_calls`. Graph `graph_def.py:363`:
  `doInBackgroundRepairDeck` (687-694) calls no `publishProgress`.
  - Caller printed: `DeckTask.java:1312`.

### 55. DeckPicker$15.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 16. DeckPicker$15.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:369` (CHECK_DATABASE task never cancelled; body empty).
  - Listener: inline anonymous listener in `integrityCheck()`,

### 56. DeckPicker$15.onProgressUpdate [framework_never_calls]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@DeckPicker$15 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A7. DeckPicker$15.onProgressUpdate (= CHECK_DATABASE listener):
  - Kind + current reason: `framework_never_calls`. Graph `graph_def.py:375`:
  `doInBackgroundCheckDatabase` (667-684) calls no `publishProgress`.
  - Caller printed: `DeckTask.java:1312`.

### 57. DeckPicker$16.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 17. DeckPicker$16.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:381` (CHECK_MEDIA task never cancelled; body empty).
  - Listener: inline anonymous listener in `mediaCheck()`,

### 58. DeckPicker$16.onProgressUpdate [framework_never_calls]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@DeckPicker$16 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A8. DeckPicker$16.onProgressUpdate (= CHECK_MEDIA listener):
  - Kind + current reason: `framework_never_calls`. Graph `graph_def.py:387`
  (entry block; reason follows the same pattern as A6/A7).
  - Caller printed: `DeckTask.java:1312`.

### 59. DeckPicker$22.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 18. DeckPicker$22.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:728` (LOAD_DECK_COUNTS task never cancelled; body empty).
  - Listener: inline anonymous listener in `updateDeckList()`,

### 60. DeckPicker$22.onProgressUpdate [framework_never_calls]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@DeckPicker$22 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A9. DeckPicker$22.onProgressUpdate (= LOAD_DECK_COUNTS listener):
  - Kind + current reason: `framework_never_calls`. Graph `graph_def.py:734`:
  `doInBackgroundLoadDeckCounts` (480-491) calls no `publishProgress`.
  - Caller printed: `DeckTask.java:1312`.

### 61. DeckPicker$24.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 19. DeckPicker$24.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:740` (DELETE_DECK task never cancelled; body empty).
  - Listener: inline anonymous listener in `deleteDeck(long)`,

### 62. DeckPicker$24.onProgressUpdate [framework_never_calls]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@DeckPicker$24 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A10. DeckPicker$24.onProgressUpdate (= DELETE_DECK listener):
  - Kind + current reason: `framework_never_calls`. Graph `graph_def.py:746`:
  `doInBackgroundDeleteDeck` (719-725) calls no `publishProgress`.
  - Caller printed: `DeckTask.java:1312`.

### 63. DeckPicker$25.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 20. DeckPicker$25.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:752` (REBUILD/EMPTY filtered-deck tasks never cancelled;
  body empty).

### 64. DeckPicker$25.onProgressUpdate [framework_never_calls]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@DeckPicker$25 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A11. DeckPicker$25.onProgressUpdate (= mSimpleProgressListener):
  - Kind + current reason: `framework_never_calls`. Graph `graph_def.py:758`:
  REBUILD_CRAM (728-733) and EMPTY_CRAM (736-741) call no `publishProgress`.
  - Caller printed: `DeckTask.java:1312`.

### 65. DeckPicker$27.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 21. DeckPicker$27.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:764` (FIND_EMPTY_CARDS task never cancelled; body empty).
  - Listener: inline anonymous listener in `handleEmptyCards()`,

### 66. DeckPicker$27.onProgressUpdate [framework_never_calls]
Callers (scan): DeckTask.onProgressUpdate (DeckTask.java:354)
Explained by b4-remainder — ### 26. DeckPicker$27.onProgressUpdate [framework_never_calls]:
  - Current reason (graph_def.py:770): doInBackGroundFindEmptyCards
  (DeckTask.java:1228-1232) calls no publishProgress, so AsyncTask never
  dispatches onProgressUpdate for this task type; body is empty.

### 67. DeckPicker$5.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 11. DeckPicker$5.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:722` (IMPORT task never cancelled).
  - Listener: `mImportAddListener`, `DeckPicker.java:238`,

### 68. DeckPicker$6.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 12. DeckPicker$6.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:604` (IMPORT_REPLACE task never cancelled).
  - Listener: `mImportReplaceListener`, `DeckPicker.java:270`,

### 69. DeckPicker$7.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 13. DeckPicker$7.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:610` (EXPORT task never cancelled, same cancel-caller
  argument as $6).

### 70. DeckPicker$7.onProgressUpdate [framework_never_calls]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@DeckPicker$7 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A5. DeckPicker$7.onProgressUpdate (= mExportListener):
  - Kind + current reason: `framework_never_calls`. Graph `graph_def.py:616`:
  export task never publishes; `doInBackgroundExportApkg` (881-909) contains
  no `publishProgress`.

### 71. DeckPicker$8.<init> [closed_by_api_level]
Callers (scan): DeckPicker.onCreate (DeckPicker.java:399)
Explained by b4-remainder — ### 27. DeckPicker$8.<init> [closed_by_api_level]:
  - Current reason (graph_def.py:622): created only in the fallback else
  branch (DeckPicker.java:394-405), which runs only when
  findViewById(R.id.add_content_menu) returns null (:391); on the

### 72. DeckPicker.hasErrorFiles [no_trigger_in_app]
Callers (scan): DatabaseErrorDialog.onCreateDialog (DatabaseErrorDialog.java:126)
Explained by b4-remainder — ### 28. DeckPicker.hasErrorFiles [no_trigger_in_app]:
  - Current reason: only caller is DatabaseErrorDialog.java:126, inside
  case DIALOG_DB_ERROR (id 1); no code passes or sends id 1, so the
  case never runs and hasErrorFiles is never called.

### 73. DrawableContainer.isClusterable [branch_never_taken]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 1. DrawableContainer.isClusterable:
  - Kind + current reason: `[branch_never_taken]`, `01.py:3344`
  (branch_never_taken; returns false, DrawableContainer.java:65-68).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 74. FunctionDrawer.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 2. FunctionDrawer.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3356`
  (isClusterable), `:3358` (isCritical), `:3360` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 75. FunctionDrawer.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 2. FunctionDrawer.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3356`
  (isClusterable), `:3358` (isCritical), `:3360` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 76. FunctionDrawer.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 2. FunctionDrawer.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3356`
  (isClusterable), `:3358` (isCritical), `:3360` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B1. FunctionDrawer.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3360`:
  never instantiated; CHA edges at `PlotSheet.java:357` and `:499` cannot fire.
  - Caller printed: `PlotSheet.java:357` (see shared evidence).

### 77. FunctionDrawer.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B2. FunctionDrawer.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3362`:
  never instantiated; CHA edges at `PlotSheet.java:473` and
  `DrawableContainer.java:49` cannot fire.
Explained by b4-paint-sync — ### 1. `FunctionDrawer.paint`:
  - Kind + current reason: `no_trigger_in_app` — never instantiated;
  CHA edges `PlotSheet.drawSingleMode -> FunctionDrawer.paint`
  (`PlotSheet.java:473`) and `DrawableContainer.paint ->

### 78. FunctionDrawer_y.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 3. FunctionDrawer_y.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3388`
  (isClusterable), `:3390` (isCritical), `:3392` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 79. FunctionDrawer_y.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 3. FunctionDrawer_y.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3388`
  (isClusterable), `:3390` (isCritical), `:3392` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 80. FunctionDrawer_y.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 3. FunctionDrawer_y.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3388`
  (isClusterable), `:3390` (isCritical), `:3392` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B3. FunctionDrawer_y.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3392`:
  never instantiated; CHA edges at `PlotSheet.java:357` and `:499` cannot fire.
  - Caller printed: `PlotSheet.java:357`.

### 81. FunctionDrawer_y.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B4. FunctionDrawer_y.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3394`:
  never instantiated; CHA edges at `PlotSheet.java:473` and
  `DrawableContainer.java:49` cannot fire.
Explained by b4-paint-sync — ### 2. `FunctionDrawer_y.paint`:
  - Kind + current reason: `no_trigger_in_app` — same wording as (1)
  (`01.py:3394`).
  - Caller + lines printed: `DrawableContainer.paint`

### 82. GraphicsWrap.drawRect [branch_never_taken]
Callers (scan): BarGraph.drawBar(double,double,GraphicsWrap,RectangleWrap,double) (BarGraph.java:198)
Explained by b4-remainder — ### 29. GraphicsWrap.drawRect [branch_never_taken]:
  - Current reason: BarGraph.drawBar calls drawRect only in its else
  branch (BarGraph.java:193-199), which runs only when filling is
  false (:180); the only BarGraph construction is

### 83. Hook.runHook [branch_never_taken]
Callers (scan): Hooks.runHook (Hooks.java:121)
Explained by b4-remainder — ### 30. Hook.runHook [branch_never_taken]:
  - Current reason (graph_def_mod/01.py:2526): base body is empty
  (Hook.java:64-66); Hooks.runHook calls func.runHook (Hooks.java:121),
  but the only key dispatched through runHook is leech (Sched.java:1723),

### 84. HttpSyncer.applyChanges [no_trigger_in_app]
Callers (scan): Syncer.sync(Connection) (Syncer.java:170)
Explained by b4-paint-sync — ### 14. `HttpSyncer.applyChanges`:
  - Kind + current reason: `no_trigger_in_app` — base body returns
  null; only caller is `Syncer.java:170` on a `RemoteServer`
  (`01.py:2628`).

### 85. HttpSyncer.applyChunk [no_trigger_in_app]
Callers (scan): Syncer.sync(Connection) (Syncer.java:197)
Explained by b4-paint-sync — ### 16. `HttpSyncer.applyChunk`:
  - Kind + current reason: `no_trigger_in_app` — base body is empty;
  only caller is `Syncer.java:197` on a `RemoteServer`, which
  overrides `applyChunk` (`01.py:2633`).

### 86. HttpSyncer.chunk() [no_trigger_in_app]
Callers (scan): Syncer.sync(Connection) (Syncer.java:179)
Explained by b4-paint-sync — ### 15. `HttpSyncer.chunk()`:
  - Kind + current reason: `no_trigger_in_app` — base body returns
  null; only caller is `Syncer.java:179` on a `RemoteServer`, which
  overrides `chunk()`; `Syncer.java:192` calls Syncer's own `chunk()`

### 87. HttpSyncer.download [no_trigger_in_app]
Callers (scan): Connection.doInBackgroundSync (Connection.java:337)
Explained by b4-remainder — ### 31. HttpSyncer.download [no_trigger_in_app]:
  - Current reason (graph_def_mod/01.py:2648): base body returns null;
  only caller is Connection.java:337 on a FullSyncer
  (Connection.java:318), which overrides download

### 88. HttpSyncer.hostKey [no_trigger_in_app]
Callers (scan): Connection.doInBackgroundLogin (Connection.java:202)
Explained by b4-remainder — ### 32. HttpSyncer.hostKey [no_trigger_in_app]:
  - Current reason (graph_def_mod/01.py:2653): base body returns null;
  only caller is Connection.java:202 on a RemoteServer
  (Connection.java:199), which overrides hostKey

### 89. HttpSyncer.meta [no_trigger_in_app]
Callers (scan): Syncer.sync(Connection) (Syncer.java:89)
Explained by b4-paint-sync — ### 12. `HttpSyncer.meta`:
  - Kind + current reason: `no_trigger_in_app` — base body returns
  null; only caller is `Syncer.java:89` on a `RemoteServer`, which
  overrides `meta` (`01.py:2658`).

### 90. HttpSyncer.sanityCheck2 [no_trigger_in_app]
Callers (scan): Syncer.sync(Connection) (Syncer.java:204)
Explained by b4-paint-sync — ### 17. `HttpSyncer.sanityCheck2`:
  - Kind + current reason: `no_trigger_in_app` — base body returns
  null; only caller is `Syncer.java:204` on a `RemoteServer`, which
  overrides `sanityCheck2` (`01.py:2673`).

### 91. HttpSyncer.start [no_trigger_in_app]
Callers (scan): Syncer.sync(Connection) (Syncer.java:157)
Explained by b4-paint-sync — ### 13. `HttpSyncer.start`:
  - Kind + current reason: `no_trigger_in_app` — base body returns
  null; only caller is `Syncer.java:157` on a `RemoteServer`, which
  overrides `start` (`01.py:2678`).

### 92. HttpSyncer.upload [no_trigger_in_app]
Callers (scan): Connection.doInBackgroundSync (Connection.java:322)
Explained by b4-remainder — ### 33. HttpSyncer.upload [no_trigger_in_app]:
  - Current reason (graph_def_mod/01.py:2683): base body returns null;
  only caller is Connection.java:322 on a FullSyncer
  (Connection.java:318), which overrides upload

### 93. ImageField.getAudioPath [branch_never_taken]
Callers (scan): MultimediaEditFieldActivity.done (MultimediaEditFieldActivity.java:267); BasicAudioFieldController.createUI (BasicAudioFieldController.java:52); NoteService.importMediaToDirectory (NoteService.java:160)
Explained by b4-paint-sync — ### 19. `ImageField.getAudioPath`:
  - Kind + current reason: `branch_never_taken` — callers run only for
  AUDIO receivers (`done` AUDIO branch, import `case AUDIO`,
  `BasicAudioFieldController.createUI`); `ImageField.getType()` is
Explained by b4-paint-sync — ### 26. `ImageField.getAudioPath`:
  - Kind + current reason: `branch_never_taken` — see entry 19.
  - Caller + lines printed: `MultimediaEditFieldActivity.done`
  (`MultimediaEditFieldActivity.java:267`, AUDIO branch).
Explained by b4-remainder — ### 58. ImageField.getAudioPath [branch_never_taken]:
  - Current reason: returns null; callers run only for AudioField
  receivers — MultimediaEditFieldActivity.done under getType()==AUDIO
  (:261-267), NoteService.importMediaToDirectory under case AUDIO

### 94. ImageField.getText [branch_never_taken]
Callers (scan): BasicTextFieldController.createUI (BasicTextFieldController.java:73); BasicTextFieldController.createCloneButton (BasicTextFieldController.java:241)
Explained by b4-remainder — ### 50. ImageField.getText [branch_never_taken]:
  - Current reason (graph_def_mod/01.py:286): returns null; createUI
  (:73) runs on a TEXT-only controller (factory lines 38-39), and
  createCloneButton (:241) is guarded by getType()!=TEXT then continue

### 95. ImageField.isModified [branch_never_taken]
Callers (scan): MultimediaEditableNote.setField (MultimediaEditableNote.java:108)
Explained by b4-paint-sync — ### 34. `ImageField.isModified`:
  - Kind + current reason: `branch_never_taken` — same wording as
  (33), citing `NoteEditor` lines 1039, 1158, 1164, 1171 and
  `NoteService` lines 58, 86 (`01.py:287`).

### 96. ImageField.setAudioPath [branch_never_taken]
Callers (scan): BasicAudioFieldController$1.onRecordingFinish (BasicAudioFieldController.java:84); NoteService.importMediaToDirectory (NoteService.java:183)
Explained by b4-paint-sync — ### 20. `ImageField.setAudioPath`:
  - Kind + current reason: `branch_never_taken` — import call is
  inside `case AUDIO`, which an `ImageField` never reaches because
  `getType()` is IMAGE (`01.py:288`).
Explained by b4-remainder — ### 59. ImageField.setAudioPath [branch_never_taken]:
  - Current reason (graph_def_mod/01.py:288): returns false; callers are
  NoteService.importMediaToDirectory :183 (inside case AUDIO, which an
  ImageField never reaches because getType() is IMAGE) and

### 97. ImageField.setText [branch_never_taken]
Callers (scan): NoteEditor$11$1.onMenuItemClick (NoteEditor.java:1170); BasicTextFieldController.onDone (BasicTextFieldController.java:341)
Explained by b4-remainder — ### 51. ImageField.setText [branch_never_taken]:
  - Current reason (graph_def_mod/01.py:291): returns false; NoteEditor
  popup (:1170) receiver is the TextField created at :1169, and
  BasicTextFieldController.onDone (:341) receiver is a TextField from

### 98. Integral.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 4. Integral.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3298`
  (isClusterable), `:3300` (isCritical), `:3302` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 99. Integral.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 4. Integral.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3298`
  (isClusterable), `:3300` (isCritical), `:3302` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 100. Integral.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 4. Integral.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3298`
  (isClusterable), `:3300` (isCritical), `:3302` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B5. Integral.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3302`:
  class never instantiated; `:357` / `:499` see only drawables already in a sheet.
  - Caller printed: `PlotSheet.java:357`.

### 101. Integral.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B6. Integral.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3304`:
  class never instantiated; paint sites `:366` / `:473` paint only drawables
  already in a sheet.
Explained by b4-paint-sync — ### 3. `Integral.paint`:
  - Kind + current reason: `no_trigger_in_app` — class never
  instantiated; paint sites paint only drawables already in a sheet
  (`01.py:3304`).

### 102. LegendDrawable.isCritical [branch_never_taken]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 5. LegendDrawable.isCritical:
  - Kind + current reason: `[branch_never_taken]`, `01.py:3310`
  (branch_never_taken; isOnFrame false, isClusterable false).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 103. LinesPoints.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 6. LinesPoints.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3324`
  (isClusterable), `:3326` (isCritical), `:3328` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 104. LinesPoints.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 6. LinesPoints.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3324`
  (isClusterable), `:3326` (isCritical), `:3328` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 105. LinesPoints.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 6. LinesPoints.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3324`
  (isClusterable), `:3326` (isCritical), `:3328` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B7. LinesPoints.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3328`:
  class never instantiated; `:357` / `:499` only see drawables added to a sheet.
  - Caller printed: `PlotSheet.java:357`.

### 106. LinesPoints.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B8. LinesPoints.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3330`:
  class never instantiated; paint sites `:366` / `:473` only paint drawables
  added to a sheet.
Explained by b4-paint-sync — ### 4. `LinesPoints.paint`:
  - Kind + current reason: `no_trigger_in_app` — class never
  instantiated; paint sites paint only drawables added to a sheet
  (`01.py:3330`).

### 107. Lookup.getSearchStringTitle [closed_by_api_level]
Callers (scan): Reviewer.onCreateOptionsMenu (Reviewer.java:300)
Explained by b4-remainder — ### 34. Lookup.getSearchStringTitle [closed_by_api_level]:
  - Current reason: only caller is Reviewer.onCreateOptionsMenu
  (Reviewer.java:298-300), inside
  `if (!CompatHelper.isHoneycomb() && !mDisableClipboard)`; isHoneycomb

### 108. ModelBrowser$1.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 22. ModelBrowser$1.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:4366` (COUNT_MODELS task never cancelled; other
  `cancel(true)` calls act on non-DeckTask tasks).

### 109. ModelBrowser$1.onProgressUpdate [no_trigger_in_app]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@ModelBrowser$1 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A12. ModelBrowser$1.onProgressUpdate (= mLoadingModelsHandler):
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def.py:4378`:
  COUNT_MODELS (1089-1126) does not publish; body comment says the task
  does not publish updates.

### 110. ModelBrowser$2.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 23. ModelBrowser$2.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:4386` (DELETE_MODEL task never cancelled; body is a
  comment, "This decktask can not be interrupted", at :133-135).

### 111. ModelBrowser$2.onProgressUpdate [no_trigger_in_app]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@ModelBrowser$2 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A13. ModelBrowser$2.onProgressUpdate (= mDeleteModelHandler):
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def.py:4398`:
  DELETE_MODEL (1127-1139) does not publish; body comment as in A12.
  - Caller printed: `DeckTask.java:1312`.

### 112. ModelFieldEditor$8.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 24. ModelFieldEditor$8.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:4490` (no in-app event cancels a field task; the four
  field types all pass this handler and discard the returned task;

### 113. ModelFieldEditor$8.onProgressUpdate [no_trigger_in_app]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@ModelFieldEditor$8 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A14. ModelFieldEditor$8.onProgressUpdate (= mChangeFieldHandler):
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def.py:4495`:
  body comment "This decktask does not publish updates"; none of the four
  field bodies calls `publishProgress` (DeckTask.java:1144-1227).

### 114. MultimediaEditFieldActivity.createSpareMenu [closed_by_api_level]
Callers (scan): MultimediaEditFieldActivity.onCreate (MultimediaEditFieldActivity.java:104)
Explained by b4-remainder — ### 35. MultimediaEditFieldActivity.createSpareMenu [closed_by_api_level]:
  - Current reason (graph_def.py:6201): called only from onCreate
  (:104) inside the branch `SDK_INT <= GINGERBREAD_MR1` (:102); on
  API 27 that branch is not taken. Note: this graph reason is tagged

### 115. NoteEditor$1.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 25. NoteEditor$1.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:2470` (ADD_FACT task never cancelled).
  - Listener: `mSaveFactHandler`, `NoteEditor.java:184`,

### 116. PlotSheet.drawMultiMode [branch_never_taken]
Callers (scan): PlotSheet.paint (PlotSheet.java:325)
Explained by b4-remainder — ### 36. PlotSheet.drawMultiMode [branch_never_taken]:
  - Current reason: paint calls drawMultiMode only when isMultiMode is
  true; the field is set only by its initializer (false) and no setter
  exists; a root-wide grep finds only PlotSheet.java lines 60, 324,

### 117. PlotSheet.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 7. PlotSheet.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3563`
  (isClusterable), `:3564` (isCritical), `:3566` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 118. PlotSheet.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 7. PlotSheet.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3563`
  (isClusterable), `:3564` (isCritical), `:3566` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 119. PlotSheet.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 7. PlotSheet.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3563`
  (isClusterable), `:3564` (isCritical), `:3566` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B9. PlotSheet.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3566`:
  returns `false`; dispatch sites `:357` / `:499` run on screen-part
  drawables, and PlotSheet is never one of them.

### 120. PlotSheet.ticsCalcX [branch_never_taken]
Callers (scan): YGrid.paint (YGrid.java:155); XAxis.paint (XAxis.java:179)
Explained by b4-remainder — ### 37. PlotSheet.ticsCalcX [branch_never_taken]:
  - Current reason: called only under `if (isAutoTic)` in XAxis.paint
  and in YGrid.paint; isAutoTic is set only by the float and int
  constructors; ChartBuilder builds XAxis with the double constructor

### 121. PlotSheet.ticsCalcY [branch_never_taken]
Callers (scan): XGrid.paint (XGrid.java:159); YAxis.paint (YAxis.java:167)
Explained by b4-remainder — ### 38. PlotSheet.ticsCalcY [branch_never_taken]:
  - Current reason: called only under `if (isAutoTic)` in YAxis.paint
  and in XGrid.paint; isAutoTic is set only by the float and int
  constructors; ChartBuilder builds YAxis with the double constructor

### 122. PlotSheet.xToGraphicLog [branch_never_taken]
Callers (scan): PlotSheet.xToGraphic (PlotSheet.java:174)
Explained by b4-remainder — ### 39. PlotSheet.xToGraphicLog [branch_never_taken]:
  - Current reason: xToGraphic (:174) selects this method only when
  isLogX is true; isLogX starts false (:40); the only assignment of
  true is in setLogX (:693), and setLogX has no call in the source

### 123. PlotSheet.yToGraphicLog [branch_never_taken]
Callers (scan): PlotSheet.yToGraphic (PlotSheet.java:202)
Explained by b4-remainder — ### 40. PlotSheet.yToGraphicLog [branch_never_taken]:
  - Current reason: yToGraphic (:202) selects this method only when
  isLogY is true; isLogY starts false (:43); the only assignment of
  true is in setLogY (:697), and setLogY has no call in the source

### 124. PointDrawer2D.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 8. PointDrawer2D.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3437`
  (isClusterable), `:3438` (isCritical), `:3435` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 125. PointDrawer2D.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 8. PointDrawer2D.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3437`
  (isClusterable), `:3438` (isCritical), `:3435` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 126. PointDrawer2D.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 8. PointDrawer2D.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3437`
  (isClusterable), `:3438` (isCritical), `:3435` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B10. PointDrawer2D.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3435`:
  interface call at `:357` / `:499` reaches only an existing PointDrawer2D;
  none is created; body returns `false` (line 77).

### 127. PointDrawer2D.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B11. PointDrawer2D.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3433`:
  interface sites `DrawableContainer.java:49` and `PlotSheet.java:473` can
  only reach an object that exists; no PointDrawer2D is created.
Explained by b4-paint-sync — ### 5. `PointDrawer2D.paint`:
  - Kind + current reason: `no_trigger_in_app` — interface call sites
  can only reach an object that exists; no `PointDrawer2D` object is
  created (`01.py:3433`).

### 128. ReliefDrawer$ReliefLegend.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 14. ReliefDrawer$ReliefLegend.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3488`
  (isClusterable), `:3489` (isCritical), `:3490` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 129. ReliefDrawer$ReliefLegend.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 14. ReliefDrawer$ReliefLegend.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3488`
  (isClusterable), `:3489` (isCritical), `:3490` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 130. ReliefDrawer$ReliefLegend.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 14. ReliefDrawer$ReliefLegend.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3488`
  (isClusterable), `:3489` (isCritical), `:3490` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B12. ReliefDrawer$ReliefLegend.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3490`:
  no ReliefLegend object is created (see `getLegend`), so the CHA edges are
  not real routes.

### 131. ReliefDrawer$ReliefLegend.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B13. ReliefDrawer$ReliefLegend.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3491`:
  a ReliefLegend exists only after `getLegend`, which has no caller.
  - Caller printed: `PlotSheet.java:470-474` (and `:366`).
Explained by b4-paint-sync — ### 7. `ReliefDrawer$ReliefLegend.paint`:
  - Kind + current reason: `no_trigger_in_app` — a `ReliefLegend`
  object exists only after `getLegend`, which has no caller
  (`01.py:3491`).

### 132. ReliefDrawer.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 9. ReliefDrawer.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3471`
  (isClusterable), `:3472` (isCritical), `:3473` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 133. ReliefDrawer.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 9. ReliefDrawer.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3471`
  (isClusterable), `:3472` (isCritical), `:3473` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 134. ReliefDrawer.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 9. ReliefDrawer.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3471`
  (isClusterable), `:3472` (isCritical), `:3473` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B14. ReliefDrawer.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3473`:
  no ReliefDrawer is ever created, so the CHA edges are not real routes.
  - Caller printed: `PlotSheet.java:357`.

### 135. ReliefDrawer.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B15. ReliefDrawer.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3475`:
  the list never holds a ReliefDrawer, because none is created.
  - Caller printed: `PlotSheet.java:470-474` (and `:366`).
Explained by b4-paint-sync — ### 6. `ReliefDrawer.paint`:
  - Kind + current reason: `no_trigger_in_app` — the drawable lists
  never hold a `ReliefDrawer` because none is created
  (`01.py:3475`).

### 136. SlidingTabStrip.blendColors [branch_never_taken]
Callers (scan): SlidingTabStrip.onDraw (SlidingTabStrip.java:134)
Explained by b4-remainder — ### 41. SlidingTabStrip.blendColors [branch_never_taken]:
  - Current reason (graph_def_mod/01.py:1604): only call is at
  SlidingTabStrip.java:134, inside `color != nextColor` (:133); both
  colours come from the same colorizer, whose indicator array has one

### 137. StudyOptionsActivity.onRequireDeckListUpdate [branch_never_taken]
Callers (scan): StudyOptionsFragment$3.onPostExecute (StudyOptionsFragment.java:658); DeckPickerContextMenu$1.onSelection (DeckPickerContextMenu.java:154)
Explained by b4-remainder — ### 42. StudyOptionsActivity.onRequireDeckListUpdate [branch_never_taken]:
  - Current reason (graph_def.py:1231, quoted in the graph): two app call
  sites exist. StudyOptionsFragment.java:657-658 calls the listener
  only when `mFragmented && refreshDecklist` holds, and mFragmented is

### 138. StudyOptionsFragment$3.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 26. StudyOptionsFragment$3.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def.py:4851` (the three task types this fragment launches —
  23, 26, 27 — are never cancelled).

### 139. StudyOptionsFragment$3.onProgressUpdate [no_trigger_in_app]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@StudyOptionsFragment$3 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A15. StudyOptionsFragment$3.onProgressUpdate (= getDeckTaskListener result):
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def.py:4854`:
  the only three task types this fragment launches publish nothing.
  - Caller printed: `DeckTask.java:1312`.

### 140. SyncErrorDialog$2.<init> [branch_never_taken]
Callers (scan): SyncErrorDialog.onCreateDialog (SyncErrorDialog.java:90)
Explained by b4-remainder — ### 43. SyncErrorDialog$2.<init> [branch_never_taken]:
  - Current reason (graph_def.py:5931): created only in the case for id 1
  (DIALOG_CONNECTION_ERROR, SyncErrorDialog.java:86); no caller passes
  1 — newInstance is called with 0, 2, 6, 9, taps pass 3, 4, 7, 8, and

### 141. TextField.getAudioPath [branch_never_taken]
Callers (scan): MultimediaEditFieldActivity.done (MultimediaEditFieldActivity.java:267); BasicAudioFieldController.createUI (BasicAudioFieldController.java:52); NoteService.importMediaToDirectory (NoteService.java:160)
Explained by b4-paint-sync — ### 21. `TextField.getAudioPath`:
  - Kind + current reason: `branch_never_taken` — same AUDIO-only
  callers as (19); `TextField.getType()` is TEXT (`01.py:293`).
  - Caller + lines printed: `NoteService.importMediaToDirectory`
Explained by b4-paint-sync — ### 27. `TextField.getAudioPath`:
  - Kind + current reason: `branch_never_taken` — see entry 21.
  - Caller + lines printed: `MultimediaEditFieldActivity.done`
  (`MultimediaEditFieldActivity.java:267`, AUDIO branch).
Explained by b4-remainder — ### 60. TextField.getAudioPath [branch_never_taken]:
  - Current reason: returns null; callers are the same as entry 58 —
  MultimediaEditFieldActivity.done (:261-267, AUDIO branch),
  NoteService.importMediaToDirectory (:158-160, case AUDIO), and

### 142. TextField.getImagePath [branch_never_taken]
Callers (scan): MultimediaEditFieldActivity.done (MultimediaEditFieldActivity.java:256); BasicImageFieldController.createUI (BasicImageFieldController.java:91); BasicImageFieldController.onActivityResult (BasicImageFieldController.java:178)
Explained by b4-paint-sync — ### 28. `TextField.getImagePath`:
  - Kind + current reason: `branch_never_taken` — callers are `done`
  under `getType()==IMAGE`, the IMAGE-only image controller, and
  import `case IMAGE`; a `TextField` never reaches any of them
Explained by b4-remainder — ### 61. TextField.getImagePath [branch_never_taken]:
  - Current reason: returns null; callers are
  MultimediaEditFieldActivity.done (:256) under getType()==IMAGE
  (:250-251), BasicImageFieldController.createUI (:91) and

### 143. TextField.hasTemporaryMedia [branch_never_taken]
Callers (scan): NoteService.importMediaToDirectory (NoteService.java:177)
Explained by b4-paint-sync — ### 22. `TextField.hasTemporaryMedia`:
  - Kind + current reason: `branch_never_taken` — only call is import
  line 177 inside `if (tmpMediaPath != null)`; `tmpMediaPath` stays
  null for TEXT (`01.py:297`).

### 144. TextField.isModified [branch_never_taken]
Callers (scan): MultimediaEditableNote.setField (MultimediaEditableNote.java:108)
Explained by b4-paint-sync — ### 35. `TextField.isModified`:
  - Kind + current reason: `branch_never_taken` — same wording as
  (33) (`01.py:298`).
  - Caller + lines printed: `MultimediaEditableNote.setField`

### 145. TextField.setAudioPath [branch_never_taken]
Callers (scan): BasicAudioFieldController$1.onRecordingFinish (BasicAudioFieldController.java:84); NoteService.importMediaToDirectory (NoteService.java:183)
Explained by b4-paint-sync — ### 23. `TextField.setAudioPath`:
  - Kind + current reason: `branch_never_taken` — import call is
  `case AUDIO` inside the `tmpMediaPath` block that a TEXT field
  never enters (`01.py:299`).
Explained by b4-remainder — ### 62. TextField.setAudioPath [branch_never_taken]:
  - Current reason: returns false; callers are
  NoteService.importMediaToDirectory :183 (case AUDIO, inside the
  tmpMediaPath block that a TEXT field never enters, :171) and

### 146. TextField.setHasTemporaryMedia [branch_never_taken]
Callers (scan): BasicImageFieldController.onActivityResult (BasicImageFieldController.java:176); BasicAudioFieldController$1.onRecordingFinish (BasicAudioFieldController.java:85)
Explained by b4-remainder — ### 52. TextField.setHasTemporaryMedia [branch_never_taken]:
  - Current reason: body is empty; callers are
  BasicImageFieldController.onActivityResult :176 (receiver is an
  ImageField from factory lines 41-42) and

### 147. TextField.setImagePath [branch_never_taken]
Callers (scan): BasicImageFieldController.onActivityResult (BasicImageFieldController.java:175); NoteService.importMediaToDirectory (NoteService.java:186)
Explained by b4-paint-sync — ### 24. `TextField.setImagePath`:
  - Kind + current reason: `branch_never_taken` — import call is
  `case IMAGE` inside the `tmpMediaPath` block that a TEXT field
  never enters (`01.py:302`).
Explained by b4-remainder — ### 63. TextField.setImagePath [branch_never_taken]:
  - Current reason: returns false; callers are
  BasicImageFieldController.onActivityResult :172 and :175 (receiver
  always an ImageField from factory lines 41-42) and

### 148. TopLevelParser.f(double) [no_trigger_in_app]
Callers (scan): BarGraph.paint (BarGraph.java:133)
Explained by b4-remainder — ### 44. TopLevelParser.f(double) [no_trigger_in_app]:
  - Current reason: instance method (Function2D.f); a call through the
  Function2D interface reaches it only when the receiver is a
  TopLevelParser, and none is created; its in-class caller getFuncVal

### 149. UIUtils$1.onCancelled [no_trigger_in_app]
Callers (scan): DeckTask.onCancelled (DeckTask.java:369)
Explained by b4-decktask-cancelled — ## 27. UIUtils$1.onCancelled:
  - Kind + current reason: `no_trigger_in_app`; private copy
  `graph_def_mod/01.py:29` (SAVE_COLLECTION task never cancelled:
  `cancelTask(int)` is only called with SEARCH_CARDS or

### 150. UIUtils$1.onProgressUpdate [no_trigger_in_app]
Callers (scan): DeckTask$TaskListener.onProgressUpdate (DeckTask.java:1312); DeckTask$TaskListener.onProgressUpdate@UIUtils$1 (DeckTask.java:1312)
Explained by b4-progress-draw — ### A16. UIUtils$1.onProgressUpdate:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:31`:
  only SAVE_COLLECTION reaches this listener, and its body calls `col.save()`
  without `publishProgress`.

### 151. XAxis.drawDownwardsMarker [branch_never_taken]
Callers (scan): XAxis.drawImplicitMarker (XAxis.java:254); XAxis.drawExplicitMarkers (XAxis.java:278)
Explained by b4-remainder — ### 45. XAxis.drawDownwardsMarker [branch_never_taken]:
  - Current reason: both callers guard the call with markOnDownside;
  setOnFrame sets it to false at ChartBuilder.java:280 before paint,
  and the only later writer that sets it to true, unsetOnFrame, has no

### 152. XAxis.drawDownwardsMinorMarker [branch_never_taken]
Callers (scan): XAxis.drawMinorMarkers (XAxis.java:431)
Explained by b4-remainder — ### 46. XAxis.drawDownwardsMinorMarker [branch_never_taken]:
  - Current reason: only caller is drawMinorMarkers, which guards the
  call with markOnDownside; the guard is false for the same reason as
  entry 45 (setOnFrame runs before paint, unsetOnFrame has no caller).

### 153. XAxisBarGraph.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 10. XAxisBarGraph.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3657`
  (isClusterable), `:3658` (isCritical), `:3659` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 154. XAxisBarGraph.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 10. XAxisBarGraph.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3657`
  (isClusterable), `:3658` (isCritical), `:3659` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 155. XAxisBarGraph.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 10. XAxisBarGraph.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3657`
  (isClusterable), `:3658` (isCritical), `:3659` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B16. XAxisBarGraph.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3659`:
  reached only by dispatch at `:357` / `:499`; no XAxisBarGraph is ever added.
  - Caller printed: `PlotSheet.java:357`.

### 156. XAxisBarGraph.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B17. XAxisBarGraph.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3660`:
  reached only by dispatch at `DrawableContainer.java:49` and
  `PlotSheet.java:473`; no XAxisBarGraph is ever added to a drawable list.
Explained by b4-paint-sync — ### 8. `XAxisBarGraph.paint`:
  - Kind + current reason: `no_trigger_in_app` — reached only by
  dispatch in `DrawableContainer.paint` (line 49) and
  `PlotSheet.drawSingleMode` (line 473); no `XAxisBarGraph` is ever

### 157. XAxisHistoGram.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 11. XAxisHistoGram.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3676`
  (isClusterable), `:3677` (isCritical), `:3678` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 158. XAxisHistoGram.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 11. XAxisHistoGram.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3676`
  (isClusterable), `:3677` (isCritical), `:3678` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 159. XAxisHistoGram.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 11. XAxisHistoGram.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3676`
  (isClusterable), `:3677` (isCritical), `:3678` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B18. XAxisHistoGram.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3678`:
  reached only by dispatch at `:357` / `:499`; no XAxisHistoGram is ever added.
  - Caller printed: `PlotSheet.java:357`.

### 160. XAxisHistoGram.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B19. XAxisHistoGram.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3679`:
  reached only by dispatch at `DrawableContainer.java:49` and
  `PlotSheet.java:473`; no XAxisHistoGram is ever added.
Explained by b4-paint-sync — ### 9. `XAxisHistoGram.paint`:
  - Kind + current reason: `no_trigger_in_app` — same dispatch-only
  wording as (8) (`01.py:3679`).
  - Caller + lines printed: `DrawableContainer.paint`

### 161. YAxisBarGraph.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 12. YAxisBarGraph.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3752`
  (isClusterable), `:3753` (isCritical), `:3754` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 162. YAxisBarGraph.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 12. YAxisBarGraph.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3752`
  (isClusterable), `:3753` (isCritical), `:3754` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 163. YAxisBarGraph.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 12. YAxisBarGraph.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3752`
  (isClusterable), `:3753` (isCritical), `:3754` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B20. YAxisBarGraph.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3754`:
  no YAxisBarGraph is ever constructed or added (grep finds only its own file).
  - Caller printed: `PlotSheet.java:357`.

### 164. YAxisBarGraph.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B21. YAxisBarGraph.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3755`:
  screen route `ChartView.onDraw` -> `PlotSheet.paint` -> `drawSingleMode`
  ends at a missing instance: no YAxisBarGraph is ever constructed or added.
Explained by b4-paint-sync — ### 10. `YAxisBarGraph.paint`:
  - Kind + current reason: `no_trigger_in_app` — dispatch sites are
  `DrawableContainer.paint` line 49 and `PlotSheet.drawSingleMode`
  lines 366 and 473; route ends at a missing instance

### 165. YAxisHistoGram.isClusterable [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:519)
Explained by b4-plotsheet-prepare — ## 13. YAxisHistoGram.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3771`
  (isClusterable), `:3772` (isCritical), `:3773` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 166. YAxisHistoGram.isCritical [no_trigger_in_app]
Callers (scan): PlotSheet.prepareDrawables (PlotSheet.java:526)
Explained by b4-plotsheet-prepare — ## 13. YAxisHistoGram.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3771`
  (isClusterable), `:3772` (isCritical), `:3773` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,

### 167. YAxisHistoGram.isOnFrame [no_trigger_in_app]
Callers (scan): PlotSheet.drawSingleMode (PlotSheet.java:357); PlotSheet.prepareDrawables (PlotSheet.java:499)
Explained by b4-plotsheet-prepare — ## 13. YAxisHistoGram.isClusterable / .isCritical / .isOnFrame:
  - Kinds + current reasons: all `[no_trigger_in_app]`, `01.py:3771`
  (isClusterable), `:3772` (isCritical), `:3773` (isOnFrame).
  - Caller + lines printed: `PlotSheet.prepareDrawables`,
Explained by b4-progress-draw — ### B22. YAxisHistoGram.isOnFrame:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3773`:
  no YAxisHistoGram is ever constructed or added (grep finds only its own file).
  - Caller printed: `PlotSheet.java:357`.

### 168. YAxisHistoGram.paint [no_trigger_in_app]
Callers (scan): DrawableContainer.paint (DrawableContainer.java:49); PlotSheet.drawSingleMode (PlotSheet.java:473)
Explained by b4-progress-draw — ### B23. YAxisHistoGram.paint:
  - Kind + current reason: `no_trigger_in_app`. Graph `graph_def_mod/01.py:3774`:
  screen route as in B21 ends at a missing instance: no YAxisHistoGram is
  ever constructed or added.
Explained by b4-paint-sync — ### 11. `YAxisHistoGram.paint`:
  - Kind + current reason: `no_trigger_in_app` — same dispatch-only
  wording as (10) (`01.py:3774`).
  - Caller + lines printed: `DrawableContainer.paint`

### 169. libanki.Utils.incGuid [branch_never_taken]
Callers (scan): Anki2Importer._uniquifyNote (Anki2Importer.java:295)
Explained by b4-remainder — ### 47. libanki.Utils.incGuid [branch_never_taken]:
  - Current reason: Anki2Importer._uniquifyNote calls it at :295 only
  after the guard at :291-293 returns false when mDupeOnSchemaChange
  is false; the constructor sets that field to false
