# AnkiDroid batch 081 (LABEL helper). libanki Card, part 1 of 2: 40 methods. The full row list is in
# graphs/AnkiDroid/parts/label_081.md. This part writes one UNREACHABLE entry (Card.getCol). The other 39 methods
# are REACHABLE through builder CALL edges (not written here). No e() edges are written in this part.

UNREACHABLE['Card.getCol'] = ('no_trigger_in_app',
  "Card.getCol() has no caller in src/main with a Card receiver. Its comment says Needed for tests. "
  "All 13 call sites of getCol() in src/main are on activity receivers, not on a Card: "
  "CompatV10.java:170; CardTemplateEditor.java:386, 451, 601, 609, 641, 662, 676, 697, 698; "
  "DialogHandler.java:94; CustomStudyDialog.java:148, 330. No class extends Card, so no app trigger reaches it.",
  'SRC com/ichi2/libanki/Card.java:604-607; SRC com/ichi2/compat/CompatV10.java:168-171; '
  'SRC com/ichi2/anki/CardTemplateEditor.java:384-387, 449-452, 599-610, 639-642, 660-663, 674-677, 695-699; '
  'SRC com/ichi2/anki/dialogs/DialogHandler.java:92-95; SRC com/ichi2/anki/dialogs/CustomStudyDialog.java:146-149, 328-331',
  'SOURCE')
