# AnkiDroid batch 012 (LABEL helper): NoteEditor part 1, 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_012.md.
#
# Result: all 40 methods are REACHABLE, so this part has no UNREACHABLE entries.
# Edges written here (15): INTENT 3 (the launches in this batch), RESULT 3, FRAMEWORK 4, GUI 2, ASYNC 3.
# INTENT check, done for each launch: the Intent names an explicit component, so no framework gate applies.
# Missing gates are notes only (MISSING GATE MGn). MG65 to MG72 are used here.
# Route ownership: NoteEditor$1 (the DeckTask TaskListener), NoteEditor$2, $4, $5, $6, $8, $9, $11, $13, the
# SetNoteTypeListener and EditNoteTypeListener classes belong to other batches; their auto CALL edges are not
# written here. The NoteEditorRescheduleCard$1.onInput listener belongs to the dialog batch. The
# AnkiActivity.onLoadFinished -> NoteEditor.onCollectionLoaded edge belongs to the AnkiActivity part.
# The ASYNC edges from saveNote are written here (launcher convention, as in label_002 and label_010).
# No page edge is written from S_NOTEEDITOR to showCardTemplateEditor: its route is the cards-line listener
# NoteEditor$2.onClick (another batch), whose auto CALL edge reaches it.

# --- INTENT: launches from this batch (explicit components; INTENT check done for each) ---

e('NoteEditor.onOptionsItemSelected', 'NoteEditor.<init>', 'INTENT',
  'copy card or add card from card editor (edit mode): explicit Intent to NoteEditor with EXTRA_CALLER set to CALLER_CARDEDITOR; the copy adds the current field text, then startActivityForResultWithAnimation with REQUEST_ADD',
  env=None,
  needs_state=STATE_NOTE,
  evidence='SRC com/ichi2/anki/NoteEditor.java:839-848',
  note='MISSING GATE MG66: the copy, add-card, reset and reschedule items are shown only in edit mode (NoteEditor.java:804-809). Edit mode is not a STATE. STATE_NOTE is a necessary condition (an edited note exists), not the full gate. INTENT check: explicit component, no framework gate. The result returns through the RESULT edge S_NOTEEDITOR -> NoteEditor.onActivityResult below. confirmed_by SOURCE.')

e('NoteEditor.showCardTemplateEditor', 'CardTemplateEditor.<init>', 'INTENT',
  'open the card template editor from the cards line of the note editor: explicit Intent to CardTemplateEditor with modelId, and noteId when editing',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1001-1013; SRC res/layout/note_editor.xml:117-125',
  note='INTENT check: explicit component, no framework gate. The tap route is the click listener NoteEditor$2.onClick (NoteEditor.java:353-357, another batch), whose auto CALL edge reaches this method. The result returns through the RESULT edge S_CARDTEMPLATEEDITOR -> NoteEditor.onActivityResult below. confirmed_by SOURCE.')

e('NoteEditor.startMultimediaFieldEditor', 'MultimediaEditFieldActivity.<init>', 'INTENT',
  'edit one multimedia field: explicit Intent to MultimediaEditFieldActivity, then startActivityForResultWithoutAnimation with REQUEST_MULTIMEDIA_EDIT',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1235-1240',
  note='INTENT check: explicit component, no framework gate. The media-button routes (NoteEditor$11.onClick at NoteEditor.java:1141 and the popup items at 1159, 1165, 1172) belong to another batch. The result returns through the RESULT edge S_MULTIMEDIA_EDIT_FIELD -> NoteEditor.onActivityResult below. confirmed_by SOURCE.')

# --- RESULT: child editors return to NoteEditor.onActivityResult (framework dispatch, Activity.java:7265-7266) ---

e('S_NOTEEDITOR', 'NoteEditor.onActivityResult', 'RESULT',
  'a copy-card or add-card editor (another NoteEditor instance) finishes; REQUEST_ADD sets mChanged in the parent',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1018-1029, 848, 937-951; FW-SRC core/java/android/app/Activity.java:7265-7266; FW-SRC core/java/android/app/ActivityThread.java:4264-4265',
  note='Page edge; S_NOTEEDITOR is the child editor. The child returns RESULT_OK only when its mChanged is set (NoteEditor.java:937-951). confirmed_by SOURCE.')

e('S_CARDTEMPLATEEDITOR', 'NoteEditor.onActivityResult', 'RESULT',
  'the card template editor returns after the user edits the templates (REQUEST_TEMPLATE_EDIT); the parent reloads its cards',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1059-1063, 1001-1013; FW-SRC core/java/android/app/Activity.java:7265-7266',
  note='Page edge; S_CARDTEMPLATEEDITOR is the child. Launched by showCardTemplateEditor (INTENT edge above). The result handler sets mReloadRequired and calls updateCards (NoteEditor.java:1063). confirmed_by SOURCE.')

e('S_MULTIMEDIA_EDIT_FIELD', 'NoteEditor.onActivityResult', 'RESULT',
  'the multimedia field editor returns (REQUEST_MULTIMEDIA_EDIT); the field text or media is updated and saved',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1031-1057, 1235-1240; FW-SRC core/java/android/app/Activity.java:7265-7266',
  note='Page edge; S_MULTIMEDIA_EDIT_FIELD is the child. Launched by startMultimediaFieldEditor (INTENT edge above). env unset here; the gates of the child page belong to its own batch. confirmed_by SOURCE.')

# --- FRAMEWORK: callbacks the framework makes (no app caller) ---

e('S_NOTEEDITOR', 'NoteEditor.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework asks the editor for its options menu (Activity.onCreatePanelMenu calls onCreateOptionsMenu)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3390; SRC com/ichi2/anki/NoteEditor.java:801-802',
  note='Page edge; the framework is the caller. The edit-mode items are hidden or shown inside the method (NoteEditor.java:804-809); see MG66 on the menu edge. Precedent: DeckPicker.onCreate -> onCreateOptionsMenu. confirmed_by SOURCE.')

e('S_NOTEEDITOR', 'NoteEditor.onSaveInstanceState', 'FRAMEWORK',
  'the framework saves the editor state when the activity is stopped and not finishing (ActivityThread: not mFinished and saveState)',
  env=None,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:4023-4025; SRC com/ichi2/anki/NoteEditor.java:313-326',
  note='Page edge. MISSING GATE MG72: the not-finishing and saveState conditions are framework state with no STATE kind, so env and needs_state are unset. Precedent: DeckPicker.onPause -> onSaveInstanceState. confirmed_by SOURCE.')

e('NoteEditor.closeNoteEditor(int,Intent)', 'NoteEditor.onDestroy', 'FRAMEWORK',
  'the editor finishes (finishWithAnimation calls finish); the framework then destroys it and calls onDestroy (performDestroy)',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:960-969; SRC com/ichi2/anki/AnkiActivity.java:206-209; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='Framework edge. onDestroy is skipped by lc_chain (LC_NO_TRIGGER), so this edge and the one from onCollectionLoaded are its inbound routes. Precedent: DeckPicker.finishWithAnimation -> onDestroy. The hop from finish to performDestroy goes through ActivityThread and is INFERRED. confirmed_by SOURCE for the written edge.')

e('NoteEditor.onCollectionLoaded', 'NoteEditor.onDestroy', 'FRAMEWORK',
  'the editor finishes without animation inside onCollectionLoaded (CALLER_NOCALLER, an intent without source text, or an Aedict note added); the framework then destroys it and calls onDestroy',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:364-367, 405-411; SRC com/ichi2/anki/AnkiActivity.java:200-203; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='Framework edge; second inbound route for onDestroy. The finish calls are finishWithoutAnimation (AnkiActivity.java:200-203), which does not run closeNoteEditor. The hop from finish to performDestroy is INFERRED, as on the edge above. confirmed_by SOURCE for the written edge.')

# --- GUI: user input on the editor page (menu, Back key) ---

e('S_NOTEEDITOR', 'NoteEditor.onBackPressed', 'GUI',
  'press the Back key in the note editor (unsaved-changes check, then close)',
  gui=['press the Back key in the note editor'],
  env=None,
  evidence='FW-SRC core/java/android/view/KeyEvent.java:2715; FW-SRC core/java/android/app/Activity.java:2975-2981; SRC com/ichi2/anki/NoteEditor.java:786-789',
  note='Page edge. KeyEvent dispatch calls Activity.onKeyUp, which calls onBackPressed (Activity.java:2980). No env or needs_state gate. Precedent: S_CARDBROWSER -> CardBrowser.onBackPressed. confirmed_by SOURCE.')

e('S_NOTEEDITOR', 'NoteEditor.onOptionsItemSelected', 'GUI',
  'tap an action-bar item in the note editor: Save, the Up arrow, Copy card, Add card from card editor, Reset card progress or Reschedule card',
  gui=['tap an action-bar item in the note editor: Save, the Up arrow, Copy card, Add card from card editor, Reset card progress or Reschedule card'],
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3439-3452; SRC com/ichi2/anki/NoteEditor.java:826-880',
  note='Page edge. Activity.onMenuItemSelected calls onOptionsItemSelected (Activity.java:3450). MISSING GATE MG66: Copy card, Add card, Reset card progress and Reschedule card appear only in edit mode (NoteEditor.java:804-809); no STATE models edit mode, so needs_state is unset here. onOptionsItemSelected is skipped by lc_chain (LC_NO_TRIGGER), so this is its only inbound route. confirmed_by SOURCE.')

# --- ASYNC: saveNote launches the add-note DeckTask; the callbacks are NoteEditor$1 (another batch) ---

e('NoteEditor.saveNote', 'NoteEditor$1.onPreExecute', 'ASYNC',
  'the add-note task starts: DeckTask.onPreExecute calls the TaskListener (NoteEditor$1)',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:662, 681; SRC com/ichi2/async/DeckTask.java:129-134, 344-347; FW-SRC core/java/android/os/AsyncTask.java:648',
  note='MISSING GATE MG65: the task is launched only in add mode (mAddNote, NoteEditor.java:662 and 681). No STATE kind models a new note being added, so needs_state is unset. The listener belongs to another batch; this launcher writes the ASYNC edge. confirmed_by SOURCE.')

e('NoteEditor.saveNote', 'NoteEditor$1.onProgressUpdate', 'ASYNC',
  'the add-note task publishes the new note (progress count greater than zero); DeckTask.onProgressUpdate calls the TaskListener',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:198-204; SRC com/ichi2/async/DeckTask.java:352-355, 372-380; FW-SRC core/java/android/os/AsyncTask.java:714-715',
  note='MISSING GATE MG65 as on the onPreExecute edge (add mode only). The listener calls setNote() on success (NoteEditor.java:204). confirmed_by SOURCE.')

e('NoteEditor.saveNote', 'NoteEditor$1.onPostExecute', 'ASYNC',
  'the add-note task ends: on success the editor closes with the new note; on failure it closes with RESULT_DB_ERROR',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:250-271; SRC com/ichi2/async/DeckTask.java:360-362; FW-SRC core/java/android/os/AsyncTask.java:691-695',
  note='MISSING GATE MG65 as on the onPreExecute edge (add mode only). MISSING GATE MG67: the failure branch (closeNoteEditor(DeckPicker.RESULT_DB_ERROR), NoteEditor.java:271) needs a failed insert; no STATE models a database error, so needs_state is unset. confirmed_by SOURCE.')
