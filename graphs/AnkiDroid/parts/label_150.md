STATUS: RUNNING 14:05

# Label part 150 (LABEL helper): AnkiDroid batch 150, 32 whole-class methods

Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, row 150. Method names: graphs/AnkiDroid/scratch/h150/methods.txt.
Source paths are relative to final_java_only/AnkiDroid/app/AnkiDroid-#4200/AnkiDroid/src/main/java/ (wildplot under com/wildplot/).

All 32 methods were already REACHABLE in other parts (overlap noted in each reason; labels and kinds copied, not relabelled). UNREACHABLE: 0.
Route gaps closed in parts/label_150.py (four e() edges): Sched$1.compare, Sched$DeckDueTreeNode.compareTo, Template$1.compare, StudyOptionsFragment.onDestroy.

| method | label | kind | reason | printed file:lines |
|---|---|---|---|---|
| ModelFieldEditor$4.<init> | REACHABLE | CALL | Overlap label_033. Auto CALL from the catch of deleteFieldDialog (sync-required delete dialog, line 258). MG272 missing. | com/ichi2/anki/ModelFieldEditor.java:240-274 (catch at 257); com/ichi2/libanki/Collection.java:364-374 |
| ModelFieldEditor$5$1.<init> | REACHABLE | CALL | Overlap label_033. Auto CALL from ModelFieldEditor$5.onPositive (line 319), in the catch branch of renameField (line 316). MG272. | com/ichi2/anki/ModelFieldEditor.java:300-319 (catch 316-319) |
| ModelFieldEditor$6$1.<init> | REACHABLE | CALL | Overlap label_034. Auto CALL in the catch of ConfirmModSchemaException in $6.onPositive (line 382). MG282. | com/ichi2/anki/ModelFieldEditor.java:366-382 |
| ModelFieldEditor$7.<init> | REACHABLE | CALL | Overlap label_034. Auto CALL in the catch of ConfirmModSchemaException in sortByField (line 465); sortByField is called from $9.onSelection (line 595). MG282. | com/ichi2/anki/ModelFieldEditor.java:456-465, 588-608 |
| ModelFieldEditor$9.onSelection | REACHABLE | GUI | Overlap label_033, label_034, label_138. Tap on a row of the field context menu (S_DLG_MODELEDITOR_CONTEXT); switch at 595-604. | com/ichi2/anki/ModelFieldEditor.java:588-608; com/ichi2/anki/dialogs/ModelEditorContextMenu.java:38-46 |
| Models.fieldNames | REACHABLE | - | Overlap label_090, label_093. Called from CardTemplateEditor.getDummyCard (line 531). Reached by the template preview (action_preview, else branch at 494) and by opening the template editor from ModelBrowser (170-171, 549-553). | com/ichi2/libanki/Models.java:490-503; com/ichi2/anki/CardTemplateEditor.java:478-495, 527-531; com/ichi2/anki/ModelBrowser.java:160-173, 549-553 |
| MultiScreenPart.getDrawables | REACHABLE | - | Overlap label_114. Read by PlotSheet.drawSingleMode (354-356) and prepareDrawables (486) once paint runs. ChartView.onDraw calls mPlotSheet.paint (70). isMultiMode is false (PlotSheet.java:60; no setter in source root). | com/wildplot/android/rendering/MultiScreenPart.java:99-101; com/wildplot/android/rendering/PlotSheet.java:60, 322-329, 352-357, 484-488; com/ichi2/anki/stats/ChartView.java:57-71 |
| MyAccount$4.<init> | REACHABLE | - | Overlap label_035. Constructed by initAllContentViews for the logout button of the logged-in view (auto CALL at 207). | com/ichi2/anki/MyAccount.java:205-215 |
| MyAccount$5.<init> | REACHABLE | - | Overlap label_035. Field initializer of loginListener, constructed with MyAccount.<init> (auto CALL at 221). | com/ichi2/anki/MyAccount.java:221-226 |
| NavigationDrawerActivity.enableDrawerSwipe | REACHABLE | - | Overlap label_036. Called by Reviewer.setWhiteboardVisibility (484) when the whiteboard is hidden and mHasDrawerSwipeConflicts is false (defaults at 57; set true at 500). | com/ichi2/anki/NavigationDrawerActivity.java:202-206; com/ichi2/anki/Reviewer.java:57-58, 474-487, 490-504 |
| NoteEditor$2.<init> | REACHABLE | - | Overlap label_013. Constructed in onCollectionLoaded for the Cards button listener. | com/ichi2/anki/NoteEditor.java:351-360 |
| NoteEditor$3.<init> | REACHABLE | - | Overlap label_013. Constructed in onCollectionLoaded for the deck spinner listener. | com/ichi2/anki/NoteEditor.java:469-483 |
| NoteEditor$4.<init> | REACHABLE | - | Overlap label_013. Constructed in onCollectionLoaded for the Tags button listener. | com/ichi2/anki/NoteEditor.java:518-532 |
| NoteEditor$8.<init> | REACHABLE | - | Overlap label_013. Constructed in registerExternalStorageListener (anonymous BroadcastReceiver). | com/ichi2/anki/NoteEditor.java:890-900 |
| NoteEditor$EditNoteTypeListener.<init> | REACHABLE | CALL | Overlap label_014. Auto CALL from onCollectionLoaded, edit-mode else branch (520-521). | com/ichi2/anki/NoteEditor.java:518-532 |
| NoteEditor$SetNoteTypeListener.<init> | REACHABLE | CALL | Overlap label_014. Auto CALL from onCollectionLoaded, add-mode branch (if mAddNote, 499-500). | com/ichi2/anki/NoteEditor.java:497-501 |
| NoteEditorRescheduleCard$1.onInput | REACHABLE | GUI | Overlap label_012, label_044, label_140. Input callback of the reschedule dialog: parseInt (30), then onRescheduleCard (31). Library dispatch of the callback is INFERRED. | com/ichi2/anki/dialogs/NoteEditorRescheduleCard.java:25-34; com/ichi2/anki/NoteEditor.java:973-980 |
| ReadText$1.onSelection | REACHABLE | GUI | Overlap label_053, label_140. Row picked in the Select TTS list: speak (121), MetaDB.storeLanguage (125), updateLanguage (127). Route: Reviewer.action_select_tts (211-216), then AbstractFlashcardViewer.showSelectTtsDialogue (2232-2243). | com/ichi2/anki/ReadText.java:112-131; com/ichi2/anki/Reviewer.java:211-216; com/ichi2/anki/AbstractFlashcardViewer.java:2232-2243 |
| Sched$1.compare | REACHABLE | CALL | Overlap label_098. Comparator for Collections.sort in _fillLrn (793-798); gate: two or more learning cards. Route gap closed in label_150.py. | com/ichi2/libanki/Sched.java:773-805 |
| Sched$DeckDueTreeNode.compareTo | REACHABLE | CALL | Overlap label_098. compareTo via Collections.sort(grps) in _groupChildren (443); gate: two or more decks. Route gap closed in label_150.py. | com/ichi2/libanki/Sched.java:432-446, 2502, 2532-2551 |
| SlidingTabLayout$TabClickListener.onClick | REACHABLE | GUI | Overlap label_075. Tap on a tab title; find the tab index (307-308), setCurrentItem (309). | com/ichi2/ui/SlidingTabLayout.java:303-315 |
| StudyOptionsFragment.onDestroy | REACHABLE | LIFECYCLE | Overlap label_038. Destroyed by FragmentManager when DeckPicker.loadStudyOptionsFragment replaces it (ft.replace at 1654). Route gap closed in label_150.py (FRAMEWORK edge; support-library source not read). | com/ichi2/anki/StudyOptionsFragment.java:195-202; com/ichi2/anki/DeckPicker.java:1651-1655, 365-367 |
| SyncErrorDialog$1.onPositive | REACHABLE | GUI | Overlap label_045, label_139. Log-in button calls the activity listener loginToSyncServer (81). | com/ichi2/anki/dialogs/SyncErrorDialog.java:76-84 |
| SyncErrorDialog$4.onPositive | REACHABLE | GUI | Overlap label_045. Confirm overwrite with the local collection: sync("upload") (139), dismissAllDialogFragments (140). | com/ichi2/anki/dialogs/SyncErrorDialog.java:134-143 |
| SyncErrorDialog$5.onPositive | REACHABLE | GUI | Overlap label_045. Confirm overwrite with the remote collection: sync("download") (153), dismiss (154). | com/ichi2/anki/dialogs/SyncErrorDialog.java:148-157 |
| SyncErrorDialog$7.onPositive | REACHABLE | GUI | Overlap label_045. Confirm overwrite with the local collection after a sanity error: sync("upload") (186), dismiss (187). | com/ichi2/anki/dialogs/SyncErrorDialog.java:182-190 |
| SyncErrorDialog$8.onPositive | REACHABLE | GUI | Overlap label_045. Confirm overwrite with the remote collection after a sanity error: sync("download") (199), dismiss (200). | com/ichi2/anki/dialogs/SyncErrorDialog.java:195-203 |
| SyncErrorDialog$9.onPositive | REACHABLE | GUI | Overlap label_045. Check-media button: mediaCheck (210), dismiss (211). | com/ichi2/anki/dialogs/SyncErrorDialog.java:206-214 |
| SyncErrorDialog.dismissAllDialogFragments | REACHABLE | CALL | Overlap label_045. Calls the activity listener dismissAllDialogFragments (299-301). Called from the callbacks of $3 (126), $4 (140), $5 (154), $7 (187), $8 (200), $9 (211). | com/ichi2/anki/dialogs/SyncErrorDialog.java:297-302, 122-128, 134-143, 148-157, 182-190, 195-203, 206-214 |
| TaskOperations.stopTaskGracefully | REACHABLE | - | Overlap nine parts (label_004, 006, 010, 026, 028, 038, 047, 049, 064). Static. Called by TranslationActivity.stopWorking (405) and LoadPronounciationActivity.stopAllTasks (474, 476, 478). cancel(true) only when the task is RUNNING (30-36). | com/ichi2/anki/runtimetools/TaskOperations.java:30-36; com/ichi2/anki/multimediacard/activity/TranslationActivity.java:399-414; com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:471-487 |
| Template$1.compare | REACHABLE | CALL | Overlap label_108. Comparator for Collections.sort at 229 (compare 233-238). MG1022 gate: a tag with two or more modifiers. Route gap closed in label_150.py. | com/ichi2/libanki/template/Template.java:199-240 |
| ViewAnimation.fade | REACHABLE | CALL | Overlap label_067. Auto CALL from AbstractFlashcardViewer.showLookupButtonIfNeeded (1221, 1224) and hideLookupButton (1233). | com/ichi2/anim/ViewAnimation.java:63-75; com/ichi2/anki/AbstractFlashcardViewer.java:1217-1236 |

Route edges written: parts/label_150.py, four e() calls (Sched._fillLrn -> Sched$1.compare; Sched._groupChildren -> Sched$DeckDueTreeNode.compareTo; Template.render_unescaped -> Template$1.compare; DeckPicker.loadStudyOptionsFragment -> StudyOptionsFragment.onDestroy).

STATUS: DONE 14:30
