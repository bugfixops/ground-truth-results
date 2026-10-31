# AnkiDroid batch 136 (LABEL helper). LoadPronounciationActivity (20 methods) and TranslationActivity (20 methods).
# All 40 methods are labelled REACHABLE. The full row list (label, kind, reason, printed file:lines) is in
# graphs/AnkiDroid/parts/label_136.md. No UNREACHABLE entries are written here.
#
# Route dependency (not written here): every route into these two activities starts at the text editor page
# S_MULTIMEDIA_EDIT_FIELD (GUI edges BasicTextFieldController$2.onClick at graph_def.py:7383 and $3.onClick at 7396).
# That page has no inbound ENTERS edge yet. The ENTERS edge from MultimediaEditFieldActivity.onCreate belongs to batch 138.
# Until it exists, the build reports these methods as UNRESOLVED.
#
# Edges written here are page ENTERS edges whose source is a method of this batch (the DeckPicker.onCreate ->
# S_DECKPICKER pattern, graph_def.py:835). Edges already in graph_def.py and not repeated here:
# - LIFECYCLE <init> -> onCreate -> onPause (lc_chain, graph_def.py:282 and 291).
# - Page GUI and FRAMEWORK edges (graph_def.py:6265-6284, 6349-6393) and part 049 (S_DLG_PICK_STRING -> TranslationActivity.onClick).
# - INTENT edges into <init> (graph_def.py:7390 and 7416).
# Automatic CALL edges come from auto_calls.json and are not written here.

e('LoadPronounciationActivity.onCreate', 'S_LOAD_PRONOUNCIATION', 'ENTERS',
  'the pronunciation screen is created and shown (not a restore after shut-off)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:91-140',
  note='onCreate returns early at lines 96-98 (finishCancel) when the saved state has the shut-off flag written by onSaveInstanceState (lines 400-403). Otherwise the layout is set at line 102 and the controls are built at lines 103-137. The network check is in onLoadPronunciation (line 155), inside the page, so no gate is set here.')

e('TranslationActivity.onCreate', 'S_TRANSLATION', 'ENTERS',
  'the translation screen is created and shown (not a restore after shut-off)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:91-168',
  note='onCreate returns early at lines 96-98 (finishCancel) when the saved state has the shut-off flag written by onSaveInstanceState (lines 382-388). Otherwise the layout is set at line 102 and the controls are built at lines 104-166. The network check is in translate (line 197), inside the page, so no gate is set here.')

e('TranslationActivity.showPickTranslationDialog', 'S_DLG_PICK_STRING', 'ENTERS',
  'the Glosbe lookup returns ok with at least one translation: the translation pick list is shown',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:257-297',
  note='The pick list (PickStringDialogFragment, page S_DLG_PICK_STRING) is shown at line 297 only when the response is ok and parseJson returns at least one translation (lines 271-289). Otherwise returnFailure runs. The same page is also entered by the field picker edges (BasicTextFieldController$3.onClick at graph_def.py:7403 and $4.onClick at 7436), which are another batch. Page node shared; no gate is set here.')
