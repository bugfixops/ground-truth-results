# AnkiDroid batch 019 (LABEL helper). AbstractFlashcardViewer, part 1: 40 methods (scratch/batches/batch_019.txt).
# One row per method, judgment calls and spot checks: graphs/AnkiDroid/parts/label_019.md.
#
# Ownership: an edge belongs to the part that contains its source. The edges here have their source in this batch:
# editCard (the edit path into NoteEditor) and the DeckTask launch sites answerCard and dismiss. Their listeners
# (AbstractFlashcardViewer$8, declared at AbstractFlashcardViewer.java:484; AbstractFlashcardViewer$10, declared at
# AbstractFlashcardViewer.java:578) are in another part and are only named here.
# Auto CALL edges (graphs/AnkiDroid/auto_calls.json) are not re-added.
# Gate: STATE_CARDS on these edges (the study screen shows a card only when the deck has cards to study).
# MG132 to MG135 are missing gates. They are written in the .md rows only (env and needs_state unset there).

# --- editCard -> NoteEditor.<init> (edit mode). Required edge. Explicit intent, app to app: no framework gate.
e('AbstractFlashcardViewer.editCard', 'NoteEditor.<init>', 'INTENT',
  'the study screen opens the note editor in edit mode for the card on screen',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1183-1187',
  note='Edit mode: EXTRA_CALLER is CALLER_REVIEWER (AbstractFlashcardViewer.java:1185) and the card is kept in sEditorCard (AbstractFlashcardViewer.java:1186). NoteEditor reads it at NoteEditor.java:370-378 and finishes when it is null. The result returns through the EDIT_CURRENT_CARD branch of onActivityResult (AbstractFlashcardViewer.java:1081-1084), which is in another part. NoteEditor.<init> is labelled in the NoteEditor part.')

# --- answerCard launches DeckTask ANSWER_CARD with mAnswerCardHandler (AbstractFlashcardViewer$10).
e('AbstractFlashcardViewer.answerCard', 'AbstractFlashcardViewer$10.onPreExecute', 'ASYNC',
  'the answer task starts and calls the listener before its background work',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1320-1321, 578-585',
  note='The listener is declared at AbstractFlashcardViewer.java:578 in another part. onPreExecute calls blockControls (AbstractFlashcardViewer.java:584; auto CALL edge). The dispatch of the listener by the task is not read in this part: INFERRED.')

e('AbstractFlashcardViewer.answerCard', 'AbstractFlashcardViewer$10.onProgressUpdate', 'ASYNC',
  'the answer task publishes the next card and calls the listener',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1320-1321, 598-607; SRC com/ichi2/async/DeckTask.java:437, 457',
  note='DeckTask.doInBackgroundAnswerCard publishes the next card (DeckTask.java:457). The listener calls updateTypeAnswerInfo (AbstractFlashcardViewer.java:604) and displayCardQuestion (AbstractFlashcardViewer.java:607), both auto CALL edges. A null card means no more cards (AbstractFlashcardViewer.java:599-601).')

e('AbstractFlashcardViewer.answerCard', 'AbstractFlashcardViewer$10.onPostExecute', 'ASYNC',
  'the answer task finishes and calls the listener',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1320-1321, 631-641',
  note='onPostExecute closes the reviewer on failure (AbstractFlashcardViewer.java:634) and when no more cards are left (AbstractFlashcardViewer.java:640). Both calls are auto CALL edges to closeReviewer.')

# --- dismiss launches DeckTask DISMISS with mDismissCardHandler (AbstractFlashcardViewer$8).
e('AbstractFlashcardViewer.dismiss', 'AbstractFlashcardViewer$8.onPostExecute', 'ASYNC',
  'the dismiss task finishes and calls its listener',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:2825, 484, 497-502',
  note='The listener mDismissCardHandler is declared at AbstractFlashcardViewer.java:484 and is in another part. onPostExecute calls closeReviewer on failure (AbstractFlashcardViewer.java:499; auto CALL edge) and forwards the result to mAnswerCardHandler.onPostExecute (AbstractFlashcardViewer.java:501).')

# --- finishNoStorageAvailable: its only caller is onActivityResult for result code 202 (DeckPicker.RESULT_MEDIA_EJECTED).
UNREACHABLE['AbstractFlashcardViewer.finishNoStorageAvailable'] = (
    'no_trigger_in_app',
    "The only caller is onActivityResult, when resultCode equals DeckPicker.RESULT_MEDIA_EJECTED (202; AbstractFlashcardViewer.java:1067-1068). "
    "In the app's Java sources the constant is referenced at AbstractFlashcardViewer.java:1067 (the guard) and 1178 (the setResult inside this method, the only setter), "
    "at StudyOptionsFragment.java:401 and DeckPicker.java:637 (readers only), and at its definition DeckPicker.java:119. "
    "The literal 202 appears nowhere else, and finishNoStorageAvailable has no other caller. "
    "So this activity can receive 202 only from a child activity that already returns 202, and the only code that produces 202 is this method. "
    "The chain has no first step in the app. The framework passes a child's result code to the parent and does not create codes. confirmed_by SOURCE.",
    'SRC com/ichi2/anki/AbstractFlashcardViewer.java:1067-1068, 1177-1180; com/ichi2/anki/DeckPicker.java:119, 637; com/ichi2/anki/StudyOptionsFragment.java:401',
    'SOURCE')

# --- calculateDynamicFontSize: the only call is under if (mCurrentCard == null) in updateCard. Both callers of updateCard
# dereference or guard mCurrentCard before the call, so the branch is never taken.
UNREACHABLE['AbstractFlashcardViewer.calculateDynamicFontSize'] = (
    'branch_never_taken',
    "The only call is in updateCard under if (mCurrentCard == null) (AbstractFlashcardViewer.java:2063-2064). "
    "updateCard has two callers. displayCardQuestion dereferences mCurrentCard (AbstractFlashcardViewer.java:1922) before it calls updateCard (L1943). "
    "displayCardAnswer returns when mCurrentCard is null (L1995-1997) before it calls updateCard (L2028). "
    "So a null card would throw before updateCard runs, and the branch is never taken. "
    "The Reviewer and Previewer variants run the same inherited code. confirmed_by SOURCE.",
    'SRC com/ichi2/anki/AbstractFlashcardViewer.java:1922, 1943, 1995-1997, 2028, 2063-2064',
    'SOURCE')
