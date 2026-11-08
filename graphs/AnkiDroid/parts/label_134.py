# AnkiDroid batch 134 (LABEL helper): AbstractFlashcardViewer (32 methods), AbstractFlashcardViewer$1.handleMessage,
# and DeckOptions$DeckPreferenceHack$Editor (5 methods). Labels: 38 REACHABLE, no UNREACHABLE. putString and remConf are labelled in batch 028.
# Edges written here (both are cited to printed source; neither is a batch-134 method pair):
#  - DeckOptions.onCreate -> S_DECKOPTIONS ENTERS: page-entry fix. No ENTERS into S_DECKOPTIONS exists in graph_def.py or any parts/*.py.
#  - AbstractFlashcardViewer.answerCard -> AbstractFlashcardViewer$11.run ASYNC: coordinator request. The destination is batch 138's
#    method; label_138.py:17 has this edge only as a comment, so no duplicate.
# Constants used: STATE_DECK (graph_def.py:128). No new constants.

e('DeckOptions.onCreate', 'S_DECKOPTIONS', 'ENTERS',
  'the deck options preference screen is live once onCreate has loaded the deck and built the preference tree',
  needs_state=STATE_DECK,
  env=None,
  evidence='SRC com/ichi2/anki/DeckOptions.java:499-523',
  note='Page-entry edge from a method outside batch 134, because S_DECKOPTIONS had no ENTERS edge. Mirrors Reviewer.onCollectionLoaded -> S_REVIEWER (graph_def.py:11178). Without it, DeckPreferenceHack.edit, Editor.<init>, apply, commit, the putX methods and remConf have no graph route. If another part later adds the same ENTERS, keep one copy.')

e('AbstractFlashcardViewer.answerCard', 'AbstractFlashcardViewer$11.run', 'ASYNC',
  'answerCard posts the delayed removeChosenAnswerText runnable, which clears the chosen-answer dots after a short delay',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:1316; SRC com/ichi2/anki/AbstractFlashcardViewer.java:825-830',
  note='Handler.postDelayed at line 1316 posts removeChosenAnswerText, the anonymous Runnable field at 825. Anonymous-class numbering in source order gives $1 Handler (349), $4 flip listener (382), $5 select-ease listener (396), $11 at 825, $13 dialog (1248), $14 look-up listener (1418), $15 WebViewClient (1435). Written at coordinator request; the destination belongs to batch 138.')
