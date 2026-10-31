# AnkiDroid batch 060 (LABEL helper). BasicTextFieldController (text editor of the multimedia field editor) and its
# listeners $1-$4, $3$1, the pick-dialog callback, the translation starters, plus FieldBase and FieldControllerBase.
# The full row list is in graphs/AnkiDroid/parts/label_060.md.
#
# Route ownership:
# - Automatic CALL edges (createUI -> createClearButton and the other create* methods, startTranslation* calls from the
#   dialog listeners, MultimediaEditFieldActivity -> FieldControllerBase setters, onDone, EFieldType.<clinit>) come from
#   auto_calls.json. They are not written here.
# - Edges written here: page edges from S_MULTIMEDIA_EDIT_FIELD and S_DLG_PICK_STRING into the listeners of this batch,
#   the INTENT edges from the say and translate paths, the ENTERS edges into the pick dialog, and the RESULT edge from the
#   ColorDict path (the source is in this batch).
#
# Gates: MG542 (clone button), MG543 (ColorDict installed). No predefined ENV_* or STATE_* constant fits, so env and
# needs_state are unset on the gated edges. Predefined constants used in this part: none.

# --- Text editor buttons (the page S_MULTIMEDIA_EDIT_FIELD is the text editor screen).
e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$1.onClick', 'GUI',
  'tap the clear button under the text box (built by createUI on every text editor)',
  env=None,
  gui=['tap the clear button under the text box (built by createUI on every text editor)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:83, 103-116; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:98, 116-146',
  note='createClearButton is called from createUI (line 83) with no condition. The listener sets the text box to an empty string (line 112).')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$2.onClick', 'GUI',
  'tap the say button (pronounce; built by createUI on every text editor)',
  env=None,
  gui=['tap the say button (pronounce; built by createUI on every text editor)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:93, 123-140',
  note='createPronounceButton is called from createUI (line 93) with no condition. Empty text shows a toast and returns (lines 131-134). Text starts LoadPronounciationActivity (edge below).')

e('BasicTextFieldController$2.onClick', 'LoadPronounciationActivity.<init>', 'INTENT',
  'the say button starts the pronunciation screen with the field text (non-empty text)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:136-138',
  note='Explicit intent to LoadPronounciationActivity with EXTRA_SOURCE, started with startActivityForResult. The network check is inside the child screen (page S_LOAD_PRONOUNCIATION, another batch), so no gate is set here. The RESULT edge S_LOAD_PRONOUNCIATION -> MultimediaEditFieldActivity.onActivityResult is already in graph_def.py.')

e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$3.onClick', 'GUI',
  'tap the translate button (built by createUI on every text editor)',
  env=None,
  gui=['tap the translate button (built by createUI on every text editor)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:92, 147-150',
  note='createTranslateButton is called from createUI (line 92) with no condition. Empty text shows a toast and returns (lines 156-159). Text with a space shows a warning toast and the flow goes on (lines 161-163).')

e('BasicTextFieldController$3.onClick', 'S_DLG_PICK_STRING', 'ENTERS',
  'non-empty text opens the translation source picker (Glosbe.com, and ColorDict unless a Chromebook)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:166, 168-173, 191; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='The picker is PickStringDialogFragment (page S_DLG_PICK_STRING), shown with the tag pick.translation.source (line 191). The ColorDict choice is listed only when CompatHelper.isChromebook() is false (lines 75-77).')

e('S_DLG_PICK_STRING', 'BasicTextFieldController$3$1.onClick', 'GUI',
  'pick a translation source in the picker (Glosbe.com or ColorDict)',
  env=None,
  gui=['pick a translation source in the picker (Glosbe.com or ColorDict)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:176-187; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='The anonymous listener $3$1 (line 176) calls startTranslationWithGlosbe (line 182) or startTranslationWithColorDict (line 184). Those two calls are automatic CALL edges and are not written here.')

e('BasicTextFieldController.startTranslationWithGlosbe', 'TranslationActivity.<init>', 'INTENT',
  'Glosbe.com chosen in the translation source picker: explicit intent to TranslationActivity with the field text, started for a result',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:393-398',
  note='Explicit component (TranslationActivity.class). The network check is in the child (TranslationActivity.translate, page S_TRANSLATION, another batch), so no gate is set here. The RESULT edge S_TRANSLATION -> MultimediaEditFieldActivity.onActivityResult is already in graph_def.py.')

e('BasicTextFieldController.startTranslationWithColorDict', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'ColorDict chosen and installed: the external picker returns to the editor, which forwards the result to the field controller',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:364-390; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:313-315',
  note='MISSING GATE MG543: ColorDict (an external app with no page node) must be installed. The check is isIntentAvailable (line 385); without the app the toast at line 386 shows and the method returns. No predefined ENV covers an app that AnkiDroid starts (ENV_OTHER_APP_INTENT is for apps that send intents to AnkiDroid). The Chromebook check (lines 75-77) also hides this choice. env and needs_state unset. The request code is REQUEST_CODE_TRANSLATE_COLORDICT (line 389).')

# --- Clone button (exists only when the note has another non-empty text field).
e('S_MULTIMEDIA_EDIT_FIELD', 'BasicTextFieldController$4.onClick', 'GUI',
  'tap the clone button (only when the note has another non-empty text field)',
  env=None,
  gui=['tap the clone button (only when the note has another non-empty text field)'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:82, 207-209, 246-256',
  note='MISSING GATE MG542: the clone button is built only when the note has more than one field (line 209) and at least one other non-empty TEXT field that is not this one (lines 216-243; return at 246-248). No predefined STATE or ENV fits (STATE_NOTE only says a note exists). env and needs_state unset. createCloneButton is called from createUI (line 82).')

e('BasicTextFieldController$4.onClick', 'S_DLG_PICK_STRING', 'ENTERS',
  'the clone source picker opens with the other non-empty text fields',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:256-266; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='MISSING GATE MG542 (inherited: the button exists only then). The choices are mPossibleClones (line 262), the listener is the controller (line 263), and the picker is shown with the tag pick.clone (line 266). env and needs_state unset.')

e('S_DLG_PICK_STRING', 'BasicTextFieldController.onClick', 'GUI',
  'pick a clone source: the field text is replaced with the chosen text',
  env=None,
  gui=['pick a clone source: the field text is replaced with the chosen text'],
  evidence='SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:263, 345-349; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:49',
  note='MISSING GATE MG542 (inherited from the clone button). The controller is the listener (line 263). onClick sets the text box to mPossibleClones[which] (line 348). env and needs_state unset.')

# --- UNREACHABLE: the identity guard in MultimediaEditableNote.setField is never true for a field the app passes in.
UNREACHABLE['FieldBase.getThisModified'] = (
    'branch_never_taken',
    'Only callers are the isModified methods of TextField, ImageField and AudioField. The one app call of isModified on a field is '
    'MultimediaEditableNote.setField line 108, which runs only inside the branch where the field passed in is the same object as the '
    'one already stored (line 107). Every app call of setField passes a newly created field or a field from the activity result '
    'extras (NoteEditor lines 1036-1039, NoteService lines 79-86, NoteFactory lines 19-33, NoteEditor lines 1157-1171). '
    'So the identity never holds, line 108 never runs, and getThisModified is never called.',
    'com/ichi2/anki/multimediacard/fields/FieldBase.java:36-38; com/ichi2/anki/multimediacard/fields/TextField.java:46-48; '
    'com/ichi2/anki/multimediacard/fields/ImageField.java:53-55; com/ichi2/anki/multimediacard/fields/AudioField.java:53-55; '
    'com/ichi2/anki/multimediacard/impl/MultimediaEditableNote.java:104-113; com/ichi2/anki/NoteEditor.java:1034-1039, 1157-1158, '
    '1163-1164, 1169-1171; com/ichi2/anki/servicelayer/NoteService.java:79-86; com/ichi2/anki/multimediacard/impl/NoteFactory.java:19-33',
    'SOURCE')
