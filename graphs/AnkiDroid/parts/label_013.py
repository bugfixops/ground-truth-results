# AnkiDroid batch 013 (LABEL helper). NoteEditor part 2, 40 methods: NoteEditor.updateCards, updateDeckPosition,
# updateField, updateFieldsFromMap, updateTags; the anonymous listeners and callbacks NoteEditor$1 (DeckTask
# TaskListener), $2 to $4, $5 to $7 (ConfirmationDialog), $8 (SD card receiver), $9 and $10 (dialog callbacks),
# $11 and $11$1 (media button and popup), $12 and $12$1 (remap button and popup) and $13 (TextWatcher).
# The full row list is in graphs/AnkiDroid/parts/label_013.md.
#
# Route ownership: setNote(Note), setNote(), onCollectionLoaded, populateEditFields, initFieldEditText,
# setMMButtonListener, setRemapButtonListener, saveNote (the TASK_TYPE_ADD_FACT launch at NoteEditor.java:681),
# showTagsDialog, showCardTemplateEditor, startMultimediaFieldEditor, onOptionsItemSelected, onActivityResult,
# registerExternalStorageListener, closeCardEditorWithCheck, showDiscardChangesDialog's caller chain,
# changeNoteTypeWithErrorHandling and duplicateCheck belong to batch_012. The edit-type and set-type listeners
# (NoteEditor$EditNoteTypeListener, NoteEditor$SetNoteTypeListener), which reach updateFieldsFromMap, updateCards,
# updateDeckPosition and updateTags, belong to batch_014.
# The ASYNC edges from the saveNote launch to NoteEditor$1 are written by batch_012, not here. The edges from
# batch_012 methods into the S_DLG_CONFIRMATION and S_DLG_TAGS pages are written by batch_012.
# REGISTER edges from an <init> are written here with a note: the builder does not follow REGISTER for
# reachability, so the route is the page GUI or FRAMEWORK edge from S_NOTEEDITOR, S_DLG_CONFIRMATION or S_DLG_TAGS.
# No method in this batch launches an app activity directly: showCardTemplateEditor, showTagsDialog and
# startMultimediaFieldEditor (the Intent launches) are batch_012 methods, so no INTENT edge is written here.
# Gates: MG75 to MG81 (no predefined ENV or STATE kind covers the edit mode, the note type change, the remap gate,
# the unsaved-changes check, the deck count or the typing gate).
# NoteEditor$1.onCancelled is UNREACHABLE. If the DeckTask onCancelled dispatch draws an auto CALL edge to it, the
# builder warns (as for CardBrowser$13 to $15, build_018); the orchestrator's sup() handles that, not this part.

# --- Cards button listener ($2). Set in onCollectionLoaded (NoteEditor.java:353-359).
e('NoteEditor$2.<init>', 'NoteEditor$2.onClick', 'REGISTER',
  'the Cards button listener is set on the card templates text view',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:353-359',
  note='onClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$2.onClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$2.onClick', 'GUI',
  'tap the card templates text (Cards) in the note editor, which opens the card template editor',
  gui=['tap the card templates text (Cards) in the note editor, which opens the card template editor'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:353-359, 1001-1002; SRC res/layout/note_editor.xml:116-122',
  note='Page edge. No gate: the text view has no visibility attribute (note_editor.xml:116-122). The launch of CardTemplateEditor is in showCardTemplateEditor (batch_012), not here.')

# --- Deck spinner listener ($3). Set in onCollectionLoaded (NoteEditor.java:471-482).
e('NoteEditor$3.<init>', 'NoteEditor$3.onItemSelected', 'REGISTER',
  'the deck spinner listener is set on the note deck spinner',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:471-482',
  note='onItemSelected is in this part. The builder does not follow REGISTER for reachability; the routes are the S_NOTEEDITOR FRAMEWORK and GUI edges below.')

e('S_NOTEEDITOR', 'NoteEditor$3.onItemSelected', 'FRAMEWORK',
  'the note editor opens: the framework lays out the deck spinner and selects position 0, which fires onItemSelected',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:452-469, 471-476; FW-SRC core/java/android/widget/AdapterView.java:937-947, 1103-1108; FW-SRC core/java/android/widget/Spinner.java:637-648, 681',
  note='Page edge. The default selection after setAdapter (NoteEditor.java:469) is set in AbsSpinner, which is not in fw_src: INFERRED for that step. The GUI edge below is the alternative route.')

e('S_NOTEEDITOR', 'NoteEditor$3.onItemSelected', 'GUI',
  'pick another deck in the deck drop-down of the note editor',
  gui=['pick another deck in the deck drop-down of the note editor'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:452-462, 471-476',
  note='Page edge. MISSING GATE MG80: needs two or more entries in the deck list (NoteEditor.java:452-462); no predefined STATE kind is a count of decks. The deck list keeps every non-filtered deck (dyn 0), and the current deck in edit mode.')

# --- Tags button listener ($4). Set in onCollectionLoaded (NoteEditor.java:526-532).
e('NoteEditor$4.<init>', 'NoteEditor$4.onClick', 'REGISTER',
  'the Tags button listener is set on the tags button',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:526-532',
  note='onClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$4.onClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$4.onClick', 'GUI',
  'tap the Tags button in the note editor, which opens the tags dialog',
  gui=['tap the Tags button in the note editor, which opens the tags dialog'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:526-531, 983-999; SRC res/layout/note_editor.xml:85-90',
  note='Page edge. No gate: the tags button has no visibility attribute (note_editor.xml:85-90). showTagsDialog is batch_012.')

# --- Confirmation dialogs ($5, $6, $7). Each anonymous ConfirmationDialog is the dialog object itself; its OK
# calls confirm() (ConfirmationDialog.java:40-43). No REGISTER edge is needed for these three.
e('S_DLG_CONFIRMATION', 'NoteEditor$5.confirm', 'GUI',
  'change the note type of an edited note when the mapping would lose cards, then tap OK',
  gui=['change the note type of an edited note when the mapping would lose cards, then tap OK'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:684-698; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43',
  note='Page edge; the route into S_DLG_CONFIRMATION is saveNote (NoteEditor.java:688-698, batch_012). MISSING GATE MG76: the change needs an edited note in change-note-type mode, and no predefined STATE kind covers the note type change. The MaterialDialog OK dispatch to ConfirmationDialog is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'NoteEditor$6.confirm', 'GUI',
  'change the note type of an edited note when libanki needs the user to confirm a full sync, then tap OK',
  gui=['change the note type of an edited note when libanki needs the user to confirm a full sync, then tap OK'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:745-767; SRC com/ichi2/libanki/Collection.java:364-371; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43',
  note='Page edge; the route into S_DLG_CONFIRMATION is changeNoteTypeWithErrorHandling (batch_012). MISSING GATE MG76 plus the libanki check: modSchema(true) throws ConfirmModSchemaException only when the schema is not yet marked changed (Collection.java:364-371), which is a collection state with no predefined kind. The MaterialDialog OK dispatch is library code: INFERRED.')

e('S_DLG_CONFIRMATION', 'NoteEditor$7.confirm', 'GUI',
  'open the note editor on an existing note, tap the reset card progress item in the menu, then tap OK',
  gui=['open the note editor on an existing note, tap the reset card progress item in the menu, then tap OK'],
  needs_state=STATE_NOTE,
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:800-810, 851-869; SRC res/menu/note_editor.xml:17-20; SRC com/ichi2/anki/dialogs/ConfirmationDialog.java:40-43',
  note='Page edge. MISSING GATE MG75: the reset item is hidden in add mode (NoteEditor.java:803-809; the XML sets visible false at note_editor menu 17-20). STATE_NOTE is the closest predefined kind (an edited note exists). The route into S_DLG_CONFIRMATION is onOptionsItemSelected (batch_012). The MaterialDialog OK dispatch is library code: INFERRED.')

# --- SD card receiver ($8). Registered in registerExternalStorageListener (NoteEditor.java:890-902), which
# onCollectionLoaded calls at NoteEditor.java:340 (batch_012).
e('NoteEditor$8.<init>', 'NoteEditor$8.onReceive', 'REGISTER',
  'the MEDIA_EJECT receiver is registered while the note editor is open',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:890-902, 340',
  note='onReceive is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$8.onReceive SYSTEM edge below.')

e('S_NOTEEDITOR', 'NoteEditor$8.onReceive', 'SYSTEM',
  'the SD card is ejected while the note editor is open (ACTION_MEDIA_EJECT, delivered to SdCardReceiver, which re-broadcasts MEDIA_EJECT)',
  env=ENV_SDCARD_EVENT,
  evidence='SRC com/ichi2/anki/NoteEditor.java:892-902; SRC com/ichi2/anki/receiver/SdCardReceiver.java:42-47',
  note='Page edge; the destination is in this part. The first hop (system delivery of ACTION_MEDIA_EJECT to the dynamically registered receiver) is not verifiable from fw_src: INFERRED. The receiver calls finishWithoutAnimation (NoteEditor.java:895-896), not the save path.')

# --- Discard-changes dialog callback ($9). Built in showDiscardChangesDialog (NoteEditor.java:917-928).
e('NoteEditor$9.<init>', 'NoteEditor$9.onPositive', 'REGISTER',
  'the discard-changes dialog callback is set when the dialog is built',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:917-928',
  note='onPositive is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$9.onPositive GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$9.onPositive', 'GUI',
  'use the close action of the note editor while there are unsaved changes, then tap OK on the discard-changes dialog',
  gui=['use the close action of the note editor while there are unsaved changes, then tap OK on the discard-changes dialog'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:625-627, 907-911, 916-928',
  note='Page edge. MISSING GATE MG79: showDiscardChangesDialog runs only when hasUnsavedChanges() is true (NoteEditor.java:907-909). The close action is closeCardEditorWithCheck (batch_012). The MaterialDialog callback is library code: INFERRED.')

# --- Tags dialog listener ($10). Set in showTagsDialog (NoteEditor.java:989-997, batch_012 method).
e('NoteEditor$10.<init>', 'NoteEditor$10.onPositive', 'REGISTER',
  'the tags dialog listener is set on the dialog in showTagsDialog',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:989-997; SRC com/ichi2/anki/dialogs/TagsDialog.java:162-167',
  note='onPositive is in this part. The builder does not follow REGISTER for reachability; the route is the S_DLG_TAGS -> NoteEditor$10.onPositive GUI edge below.')

e('S_DLG_TAGS', 'NoteEditor$10.onPositive', 'GUI',
  'in the tags dialog, select tags and tap OK',
  gui=['in the tags dialog, select tags and tap OK'],
  env=None,
  evidence='SRC com/ichi2/anki/dialogs/TagsDialog.java:162-167; SRC com/ichi2/anki/NoteEditor.java:983-999',
  note='Page edge. The route into S_DLG_TAGS is showTagsDialog (batch_012). TagsDialog.java:164-166 calls the listener from app code; the MaterialDialog OK callback that reaches it is library code: INFERRED.')

# --- Media button ($11) and its popup ($11$1). setMMButtonListener is called only when editModelMode is false
# (NoteEditor.java:1116-1122), so both edges carry MG77.
e('NoteEditor$11.<init>', 'NoteEditor$11.onClick', 'REGISTER',
  'the media button listener is set on the media button of each field when not in change-note-type mode',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1116-1122, 1129-1131',
  note='onClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$11.onClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$11.onClick', 'GUI',
  'tap the media button next to a field in the note editor (not in change-note-type mode)',
  gui=['tap the media button next to a field in the note editor (not in change-note-type mode)'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1108-1122, 1129-1146',
  note='Page edge. MISSING GATE MG77: setMMButtonListener runs only when editModelMode is false (NoteEditor.java:1116-1122). A non-empty field starts the field editor (startMultimediaFieldEditor, batch_012); an empty field shows the popup.')

e('NoteEditor$11$1.<init>', 'NoteEditor$11$1.onMenuItemClick', 'REGISTER',
  'the popup menu listener is set on the media popup of an empty field',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1142-1148',
  note='onMenuItemClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$11$1.onMenuItemClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$11$1.onMenuItemClick', 'GUI',
  'tap the media button of an empty field, then choose audio, image or text in the popup menu',
  gui=['tap the media button of an empty field, then choose audio, image or text in the popup menu'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1142-1160',
  note='Page edge. MISSING GATE MG77 applies (the field is empty and the editor is not in change-note-type mode). The PopupMenu item dispatch is framework and library code: INFERRED.')

# --- Remap button ($12) and its popup ($12$1). Both need editModelMode and more than two fields (MG78).
e('NoteEditor$12.<init>', 'NoteEditor$12.onClick', 'REGISTER',
  'the remap button listener is set on the media button of a new field in change-note-type mode',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1112-1115, 1186-1189',
  note='onClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$12.onClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$12.onClick', 'GUI',
  'change the note type of an existing note to one with more than two fields, then tap the remap button of a new field',
  gui=['change the note type of an existing note to one with more than two fields, then tap the remap button of a new field'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1112-1115, 1186-1198, 1505-1508',
  note='Page edge. MISSING GATE MG78: editModelMode and allowFieldRemapping() (mEditorNote.items().length > 2, NoteEditor.java:1507). editModelMode is the argument of populateEditFields(fields, boolean) and is true only through updateFieldsFromMap (NoteEditor.java:1497), which the change-note-type listener calls (NoteEditor$EditNoteTypeListener, batch_014, line 1625). The PopupMenu dispatch is library code: INFERRED.')

e('NoteEditor$12$1.<init>', 'NoteEditor$12$1.onMenuItemClick', 'REGISTER',
  'the remap popup listener is set on the old-field popup',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1192-1199',
  note='onMenuItemClick is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR -> NoteEditor$12$1.onMenuItemClick GUI edge below.')

e('S_NOTEEDITOR', 'NoteEditor$12$1.onMenuItemClick', 'GUI',
  'after a remap button tap, pick an old field (or None) in the popup menu',
  gui=['after a remap button tap, pick an old field (or None) in the popup menu'],
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1186-1229',
  note='Page edge. MISSING GATE MG78 applies. The choice updates mModelChangeFieldMap and reloads the fields through updateFieldsFromMap (NoteEditor.java:1225). The popup dispatch is library code: INFERRED.')

# --- Field TextWatcher ($13). Added in initFieldEditText after editText.init (NoteEditor.java:1247, then 1253).
e('NoteEditor$13.<init>', 'NoteEditor$13.afterTextChanged', 'REGISTER',
  'the text watcher is added to each field EditText in initFieldEditText',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1247, 1253-1271',
  note='afterTextChanged is in this part. The builder does not follow REGISTER for reachability; the routes are the S_NOTEEDITOR FRAMEWORK edges below.')

e('NoteEditor$13.<init>', 'NoteEditor$13.beforeTextChanged', 'REGISTER',
  'the text watcher is added to each field EditText in initFieldEditText',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1247, 1253-1271',
  note='beforeTextChanged is in this part (empty body). The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR FRAMEWORK edge below.')

e('NoteEditor$13.<init>', 'NoteEditor$13.onTextChanged', 'REGISTER',
  'the text watcher is added to each field EditText in initFieldEditText',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:1247, 1253-1271',
  note='onTextChanged is in this part (empty body). The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR FRAMEWORK edge below.')

e('S_NOTEEDITOR', 'NoteEditor$13.afterTextChanged', 'FRAMEWORK',
  'type or delete text in a field of the note editor; the TextView dispatches the change to the watcher',
  env=None,
  evidence='FW-SRC core/java/android/widget/TextView.java:9375-9380; SRC com/ichi2/anki/NoteEditor.java:1253-1260',
  note='Page edge. MISSING GATE MG81: the field is enabled only when editModelMode is false (initFieldEditText enabled = !editModelMode, NoteEditor.java:1102, 1272). The watcher is added after init (1247, then 1253), so the cold-start init does not fire it: typing is the route.')

e('S_NOTEEDITOR', 'NoteEditor$13.beforeTextChanged', 'FRAMEWORK',
  'type or delete text in a field of the note editor; the TextView dispatches the change to the watcher',
  env=None,
  evidence='FW-SRC core/java/android/widget/TextView.java:9309-9314; SRC com/ichi2/anki/NoteEditor.java:1264-1265',
  note='Page edge. MISSING GATE MG81 applies (enabled field, typing). The body is empty, so the edge has no effect on state.')

e('S_NOTEEDITOR', 'NoteEditor$13.onTextChanged', 'FRAMEWORK',
  'type or delete text in a field of the note editor; the TextView dispatches the change to the watcher',
  env=None,
  evidence='FW-SRC core/java/android/widget/TextView.java:9359-9364; SRC com/ichi2/anki/NoteEditor.java:1269-1270',
  note='Page edge. MISSING GATE MG81 applies (enabled field, typing). The body is empty, so the edge has no effect on state.')

# --- UNREACHABLE entries.
UNREACHABLE['NoteEditor$1.onCancelled'] = (
    'no_trigger_in_app',
    "The add-note task (TASK_TYPE_ADD_FACT, launched by saveNote at NoteEditor.java:681) is never cancelled. The only cancel of a DeckTask is sLatestInstance inside the no-argument cancelTask() (DeckTask.java:172). That method is reached only from cancelTask(int) when the type matches (DeckTask.java:181-186), and the only callers of cancelTask(int) are CardBrowser SEARCH_CARDS and RENDER_BROWSER_QA (CardBrowser.java:528-529, 796-797, 1155). The ADD_FACT case is at DeckTask.java:243-244. AsyncTask runs onCancelled only after cancel() (AsyncTask.java:525-528, 691-698). The body is empty (NoteEditor.java:276-278).",
    'SRC com/ichi2/async/DeckTask.java:172, 181-186, 243-244; SRC com/ichi2/anki/CardBrowser.java:528-529, 796-797, 1155; SRC com/ichi2/anki/NoteEditor.java:276-278, 681; FW-SRC core/java/android/os/AsyncTask.java:525-528, 691-698',
    'SOURCE')

UNREACHABLE['NoteEditor$3.onNothingSelected'] = (
    'framework_never_calls',
    "The deck spinner adapter is built once from a static deck list and set once; nothing else sets an adapter or calls notifyDataSetChanged on it (NoteEditor.java:468-469). Both selection calls are guarded by a valid index (updateDeckPosition at NoteEditor.java:1385-1387; the edit-type listener at 1632-1634). AdapterView fires onNothingSelected only when the selected position is negative (fireOnSelected, AdapterView.java:941-947), and the position changes only through checkSelectionChanged (AdapterView.java:1103-1108). This path never moves the selection to a negative position. The framework dispatch is read from source, not run: INFERRED. The body is a comment only (NoteEditor.java:479-481).",
    'SRC com/ichi2/anki/NoteEditor.java:468-469, 479-481, 1385-1387; FW-SRC core/java/android/widget/AdapterView.java:941-947, 1103-1108',
    'INFERRED')
