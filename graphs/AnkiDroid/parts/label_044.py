# AnkiDroid batch 044 (LABEL helper). Dialogs: MediaCheckDialog (with $1, $2, $3), ModelBrowserContextMenu,
# ModelEditorContextMenu, NoteEditorRescheduleCard (with $1), SimpleMessageDialog (with $1). 35 methods, all REACHABLE.
# The full row list is in graphs/AnkiDroid/parts/label_044.md.
#
# Route ownership:
# - Page edges (S_DLG_*) belong to the part that contains the destination, so they are written here.
# - Lifecycle edges from the <init> methods to onCreateDialog already exist in graph_def.py (lines 260-273); not repeated.
# - CALL edges (auto_calls.json, the builder's automatic edges) are not repeated here.
# - Shortcut overlap (not changed here): graph_def.py 1026-1033 has S_DLG_MEDIA_CHECK -> DeckPicker.mediaCheck and
#   S_DLG_MEDIA_CHECK -> DeckPicker.deleteUnused, which skip the callbacks MediaCheckDialog$1.onPositive and $2.onNegative.
#
# Gates: MG382 (results dialog shows unused media files), MG383 (results dialog shows no unused media files).
# Constants: ENV_STORAGE (the Check media menu item is enabled only when storage is mounted, DeckPicker.java:525-529),
# STATE_NOTE (the reschedule item is shown only when an existing note is edited, NoteEditor.java:803-808).

# --- MediaCheckDialog page (confirm dialog and results dialog share the page S_DLG_MEDIA_CHECK).
e('S_DLG_MEDIA_CHECK', 'MediaCheckDialog$1.onPositive', 'GUI',
  'the OK button of the confirm dialog (check media) is tapped and the media check starts',
  env=ENV_STORAGE,
  gui=['the OK button of the confirm dialog (check media) is tapped and the media check starts'],
  evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:67-73; SRC com/ichi2/anki/DeckPicker.java:525-529, 600-603, 1190-1191',
  note='The confirm dialog is opened from the Check media menu item, enabled only when storage is mounted (ENV_STORAGE). The next step, DeckPicker.mediaCheck, is an automatic CHA CALL (MediaCheckDialog.java:70). The button dispatch is the MaterialDialog library (not read: INFERRED).')

e('S_DLG_MEDIA_CHECK', 'MediaCheckDialog$1.onNegative', 'GUI',
  'the Cancel button of the confirm dialog is tapped and the dialogs are dismissed',
  env=ENV_STORAGE,
  gui=['the Cancel button of the confirm dialog is tapped and the dialogs are dismissed'],
  evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:76-79',
  note='The confirm dialog exists only when the menu item is enabled (ENV_STORAGE). The dismiss call (line 77-78) is not in auto_calls.json. The button dispatch is the MaterialDialog library (not read: INFERRED).')

e('S_DLG_MEDIA_CHECK', 'MediaCheckDialog$2.onPositive', 'GUI',
  'the OK button of the media check results dialog is tapped when unused media files exist (the dialog only dismisses)',
  gui=['the OK button of the media check results dialog is tapped when unused media files exist (the dialog only dismisses)'],
  evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:116-124',
  note='MISSING GATE MG382: the results dialog has unused media files (MediaCheckDialog.java:116-118). No predefined ENV or STATE kind covers the content of the media folder. env and needs_state unset.')

e('S_DLG_MEDIA_CHECK', 'MediaCheckDialog$2.onNegative', 'GUI',
  'the Delete unused button of the media check results dialog is tapped',
  gui=['the Delete unused button of the media check results dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:116-131',
  note='MISSING GATE MG382: the same condition as MediaCheckDialog$2.onPositive (unused media files exist). The callback calls DeckPicker.deleteUnused (automatic CHA CALL, line 128) and then dismisses the dialogs (line 129). The page shortcut in graph_def.py (lines 1030-1033) reaches DeckPicker.deleteUnused without this callback. env and needs_state unset.')

e('S_DLG_MEDIA_CHECK', 'MediaCheckDialog$3.onPositive', 'GUI',
  'the OK button of the media check results dialog is tapped when no unused media files were found',
  gui=['the OK button of the media check results dialog is tapped when no unused media files were found'],
  evidence='SRC com/ichi2/anki/dialogs/MediaCheckDialog.java:132-139',
  note='MISSING GATE MG383: the results dialog has no unused media files (the else branch, MediaCheckDialog.java:132). No predefined ENV or STATE kind covers this. env and needs_state unset.')

# --- SimpleMessageDialog page.
e('S_DLG_SIMPLE_MESSAGE', 'SimpleMessageDialog$1.onPositive', 'GUI',
  'the OK button of the simple message dialog is tapped',
  gui=['the OK button of the simple message dialog is tapped'],
  evidence='SRC com/ichi2/anki/dialogs/SimpleMessageDialog.java:40-47; SRC com/ichi2/anki/AnkiActivity.java:453-460',
  note='No gate. The callback calls AnkiActivity.dismissSimpleMessageDialog (automatic CHA CALL, SimpleMessageDialog.java:44). That method restarts DeckPicker only when reload is set (AnkiActivity.java:455-458).')

# --- NoteEditorRescheduleCard page.
e('S_DLG_RESCHEDULE_CARD', 'NoteEditorRescheduleCard$1.onInput', 'GUI',
  'a day count is typed in the reschedule dialog (the input callback)',
  needs_state=STATE_NOTE,
  gui=['a day count is typed in the reschedule dialog (the input callback)'],
  evidence='SRC com/ichi2/anki/dialogs/NoteEditorRescheduleCard.java:27-33; SRC com/ichi2/anki/NoteEditor.java:801-808, 871-874, 973-979',
  note='The menu item is shown only when the editor is not adding a note (NoteEditor.java:803-808), so an existing note exists (STATE_NOTE). The library calls InputCallback.onInput with the typed text (library not read: INFERRED). The callback calls NoteEditor.onRescheduleCard (automatic exact CALL, NoteEditorRescheduleCard.java:31). The input range (inputRange(1,4), line 26) is library validation (INFERRED).')
