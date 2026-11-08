# AnkiDroid batch 014 (LABEL helper). NoteEditor note type listeners and the JSON name comparator:
# NoteEditor$SetNoteTypeListener (add mode), NoteEditor$EditNoteTypeListener (edit mode) and
# NoteEditor$JSONNameComparator. 8 methods; the full row list is in graphs/AnkiDroid/parts/label_014.md.
#
# Route ownership: NoteEditor.onCollectionLoaded (NoteEditor.java:331) belongs to batch_012. Its CALL edges to the
# three <init> methods come from auto_calls.json (NoteEditor.java:453, 500, 521) and are not written here.
# The edge NoteEditor.onCollectionLoaded -> NoteEditor$JSONNameComparator.compare (via java.util.Collections.sort,
# which is not in the dataset) is NOT written here; the part that holds onCollectionLoaded (batch_012) writes it.
# The edit-mode entries into NoteEditor.<init> are batch_011 (CardBrowser$7.onItemClick) and batch_019
# (AbstractFlashcardViewer.editCard); they are not written here.
# REGISTER edges from an <init> are written here with a note: the builder does not follow REGISTER for reachability,
# so the route is the S_NOTEEDITOR FRAMEWORK or GUI edge below.
# Gates: MG85 (add mode), MG86 (two or more note types or entries), MG87 (edit mode). env and needs_state are unset
# on the MG edges.

# --- SetNoteTypeListener (add mode). Set in onCollectionLoaded inside the mAddNote branch (NoteEditor.java:499-500).
e('NoteEditor$SetNoteTypeListener.<init>', 'NoteEditor$SetNoteTypeListener.onItemSelected', 'REGISTER',
  'the add-mode note type listener is set on the note type spinner',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:499-500',
  note='onItemSelected is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR FRAMEWORK edge below.')

e('NoteEditor$SetNoteTypeListener.<init>', 'NoteEditor$SetNoteTypeListener.onNothingSelected', 'REGISTER',
  'the add-mode note type listener is set on the note type spinner',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:499-500',
  note='onNothingSelected is in this part (UNREACHABLE below). The builder does not follow REGISTER for reachability.')

e('S_NOTEEDITOR', 'NoteEditor$SetNoteTypeListener.onItemSelected', 'FRAMEWORK',
  'the add-mode note editor opens: the framework lays out the note type spinner and fires onItemSelected for the selected note type',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:364-384, 434, 497-500; FW-SRC core/java/android/widget/Spinner.java:619-623, 681; FW-SRC core/java/android/widget/AdapterView.java:194, 204, 903-930, 932-935, 937-949, 1103-1108',
  note='MISSING GATE MG85: the note editor is in add mode (mAddNote is true; callers STUDYOPTIONS, DECKPICKER, REVIEWER_ADD, CARDBROWSER_ADD, CARDEDITOR and CARDEDITOR_INTENT_ADD, NoteEditor.java:380-415). No predefined ENV or STATE kind covers the caller mode. env and needs_state unset.')

e('S_NOTEEDITOR', 'NoteEditor$SetNoteTypeListener.onItemSelected', 'GUI',
  'pick another note type in the note type drop-down of the add-mode note editor',
  gui=['pick another note type in the note type drop-down of the add-mode note editor'],
  evidence='SRC com/ichi2/anki/NoteEditor.java:497-500, 1542-1554; FW-SRC core/java/android/widget/Spinner.java:1183-1190',
  note='MISSING GATE MG86: needs two or more note types in the collection (a pick that changes the selection needs a second item). Also the add-mode gate MG85 (see the FRAMEWORK edge above). env and needs_state unset.')

# --- EditNoteTypeListener (edit mode). Set in onCollectionLoaded in the else branch (NoteEditor.java:520-521).
e('NoteEditor$EditNoteTypeListener.<init>', 'NoteEditor$EditNoteTypeListener.onItemSelected', 'REGISTER',
  'the edit-mode note type listener is set on the note type spinner',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:520-521',
  note='onItemSelected is in this part. The builder does not follow REGISTER for reachability; the route is the S_NOTEEDITOR FRAMEWORK edge below.')

e('NoteEditor$EditNoteTypeListener.<init>', 'NoteEditor$EditNoteTypeListener.onNothingSelected', 'REGISTER',
  'the edit-mode note type listener is set on the note type spinner',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:520-521',
  note='onNothingSelected is in this part (UNREACHABLE below). The builder does not follow REGISTER for reachability.')

e('S_NOTEEDITOR', 'NoteEditor$EditNoteTypeListener.onItemSelected', 'FRAMEWORK',
  'the edit-mode note editor opens for an existing note: the framework lays out the note type spinner and fires onItemSelected for the note type of that note',
  env=None,
  evidence='SRC com/ichi2/anki/NoteEditor.java:370-394, 434, 497, 520-521, 1592-1594; FW-SRC core/java/android/widget/Spinner.java:619-623, 681; FW-SRC core/java/android/widget/AdapterView.java:194, 204, 903-930, 932-935, 937-949, 1103-1108',
  note='MISSING GATE MG87: the note editor is in edit mode (mAddNote is false; callers REVIEWER and CARDBROWSER_EDIT, NoteEditor.java:370-378 and 386-394). No predefined ENV or STATE kind covers the caller mode, and the open card is also required (the editor finishes when it is missing, NoteEditor.java:372-374 and 388-390), which no predefined STATE covers. env and needs_state unset.')

e('S_NOTEEDITOR', 'NoteEditor$EditNoteTypeListener.onItemSelected', 'GUI',
  'pick another note type in the note type drop-down of the edit-mode note editor',
  gui=['pick another note type in the note type drop-down of the edit-mode note editor'],
  evidence='SRC com/ichi2/anki/NoteEditor.java:520-521, 1592-1605; FW-SRC core/java/android/widget/Spinner.java:1183-1190',
  note='MISSING GATE MG86: needs two or more note types in the collection (a pick that changes the selection needs a second item). Also the edit-mode gate MG87 (see the FRAMEWORK edge above). env and needs_state unset.')

# --- onNothingSelected of both listeners (body '// Do Nothing').
UNREACHABLE['NoteEditor$SetNoteTypeListener.onNothingSelected'] = (
    'framework_never_calls',
    "The note type spinner gets its adapter once (NoteEditor.java:434) and its selection once (NoteEditor.java:497); the only other read is getSelectedItemPosition (NoteEditor.java:1447). AdapterView calls onNothingSelected only when the selected position is negative at a dispatch (fireOnSelected, AdapterView.java:937-949). A dispatch runs only when the selection changed (checkSelectionChanged, AdapterView.java:1103-1108). The selection starts at INVALID_POSITION (AdapterView.java:194, 204), so an empty adapter gives no dispatch (Spinner.java:637-645, and handleDataChanged leaves INVALID_POSITION equal to the old value at AdapterView.java:1086-1094). A non-empty adapter always gets a selectable position (handleDataChanged, AdapterView.java:1043-1085), so the position is never negative at a dispatch. The body is '// Do Nothing' (NoteEditor.java:1585-1588). The AbsSpinner setAdapter and setSelection steps are not in fw_src, so this is INFERRED.",
    'SRC com/ichi2/anki/NoteEditor.java:434, 497, 1447, 1585-1588; FW-SRC core/java/android/widget/AdapterView.java:194, 204, 937-949, 1043-1085, 1086-1094, 1103-1108; FW-SRC core/java/android/widget/Spinner.java:637-645',
    'INFERRED')

UNREACHABLE['NoteEditor$EditNoteTypeListener.onNothingSelected'] = (
    'framework_never_calls',
    "The same spinner serves edit mode: the adapter is set once (NoteEditor.java:434), the selection is set once (NoteEditor.java:497), the edit-mode listener is attached in the else branch (NoteEditor.java:520-521), and the only other read is getSelectedItemPosition (NoteEditor.java:1447). The framework argument is the same as for the add-mode listener: onNothingSelected needs a negative selected position at a dispatch (AdapterView.java:937-949), and a dispatch needs a change of the selection (AdapterView.java:1103-1108). An empty adapter leaves the selection at INVALID_POSITION with no change (AdapterView.java:194, 204, 1086-1094; Spinner.java:637-645), and a non-empty adapter always gets a selectable position (AdapterView.java:1043-1085). The body is '// Do Nothing' (NoteEditor.java:1645-1648). The AbsSpinner setAdapter and setSelection steps are not in fw_src, so this is INFERRED.",
    'SRC com/ichi2/anki/NoteEditor.java:434, 497, 520-521, 1447, 1645-1648; FW-SRC core/java/android/widget/AdapterView.java:194, 204, 937-949, 1043-1085, 1086-1094, 1103-1108; FW-SRC core/java/android/widget/Spinner.java:637-645',
    'INFERRED')
