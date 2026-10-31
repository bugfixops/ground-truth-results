# AnkiDroid batch 137 (LABEL helper). Reviewer (15 methods), Whiteboard (13 methods) and YAxis (12 methods).
# Source row: graphs/AnkiDroid/scratch/batches_ai.tsv, part 137. (scratch/batches/batch_137.txt lists other classes and was not used.)
# All 40 methods are labelled REACHABLE. The full row list (label, kind, reason, printed file:lines) is in
# graphs/AnkiDroid/parts/label_137.md. No UNREACHABLE entries are written here.
#
# Route gaps in out/ that the edges below close (every batch method is UNRESOLVED there without them):
# - S_REVIEWER has no inbound ENTERS edge. Written here: Reviewer.onCollectionLoaded -> S_REVIEWER.
# - AnkiActivity.onLoadFinished@Reviewer (receiver variant) has no inbound edge, so the loader route into
#   Reviewer.onCollectionLoaded is missing. Written here: ASYNC AbstractFlashcardViewer.onCreate -> Reviewer.onCollectionLoaded.
# - AbstractFlashcardViewer.onCreate@Reviewer (receiver variant) has no inbound edge, so its callees are blocked.
#   Written here: base-node CALL edges AbstractFlashcardViewer.onCreate -> Reviewer.restorePreferences and -> Reviewer.getContentViewAttr.
# - S_STATISTICS has no inbound ENTERS edge, and the YAxis chain runs through ChartView.onDraw from that page.
#   Written here: Statistics.onCreate -> S_STATISTICS (page edge outside the batch).
#
# Already in graph_def.py and not repeated here: S_REVIEWER GUI and FRAMEWORK edges (graph_def.py:1361-1444),
# Whiteboard.onDraw from S_REVIEWER (7002), S_STATISTICS -> ChartView.onDraw (7657), the Reviewer.<init> lifecycle chain.
# Automatic CALL edges come from auto_calls.json and are not written here.

e('AbstractFlashcardViewer.onCreate', 'Reviewer.onCollectionLoaded', 'ASYNC',
  'the collection finishes loading and the loader calls onCollectionLoaded on the Reviewer (AnkiActivity.onLoadFinished dispatch)',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:859; SRC com/ichi2/anki/AnkiActivity.java:255-262, 283-290; SRC com/ichi2/anki/Reviewer.java:96-98',
  note='The loader callback is androidx Loader, a library step: INFERRED, source not read. AnkiActivity.onLoadFinished has no inbound edge in out/, so the edge is written from the base onCreate, following the CardBrowser.onCreate -> CardBrowser.onCollectionLoaded ASYNC precedent (graph_def.py:1500-1510). Reviewer.java:96-97 is an @Override of AnkiActivity.onCollectionLoaded, so the virtual call at AnkiActivity.java:286 reaches the Reviewer method.')

e('Reviewer.onCollectionLoaded', 'S_REVIEWER', 'ENTERS',
  'the review screen is live once the collection is loaded: the cards and the controls are set up',
  env=None,
  evidence='SRC com/ichi2/anki/Reviewer.java:97-115; SRC com/ichi2/anki/AbstractFlashcardViewer.java:879-890',
  note='Page ENTERS from a method of this batch, following Previewer.onCollectionLoaded -> S_PREVIEWER (parts/label_036.py:151-155). Without it S_REVIEWER has no inbound edge, so every S_REVIEWER page edge (onCreateOptionsMenu, onKeyUp, onOptionsItemSelected, onWindowFocusChanged, Whiteboard.onDraw, Reviewer$1.onTouch and the AbstractFlashcardViewer page edges) stays UNRESOLVED.')

e('AbstractFlashcardViewer.onCreate', 'Reviewer.restorePreferences', 'CALL',
  'AbstractFlashcardViewer.onCreate calls restorePreferences(), which dispatches to the Reviewer override',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:849-855; SRC com/ichi2/anki/Reviewer.java:396-397',
  note='Virtual dispatch: Reviewer.java:396 overrides restorePreferences (super call at line 397). The auto edge from the variant AbstractFlashcardViewer.onCreate@Reviewer has no inbound edge in out/, so this base-node edge is the route.')

e('AbstractFlashcardViewer.onCreate', 'Reviewer.getContentViewAttr', 'CALL',
  'AbstractFlashcardViewer.onCreate calls getContentViewAttr() to choose the layout, which dispatches to the Reviewer override',
  env=None,
  evidence='SRC com/ichi2/anki/AbstractFlashcardViewer.java:855, 862-864; SRC com/ichi2/anki/Reviewer.java:82',
  note='Same reason as the restorePreferences edge above. Reviewer.java:82 overrides AbstractFlashcardViewer.getContentViewAttr(int).')

e('Statistics.onCreate', 'S_STATISTICS', 'ENTERS',
  'the statistics screen is created and its layout is set (activity_anki_stats)',
  env=None,
  evidence='SRC com/ichi2/anki/Statistics.java:81-88',
  note='Page edge whose source and destination are both outside batch 137, written under the page-edge exception: S_STATISTICS has no inbound edge in out/, and the YAxis route (ChartView.onDraw, FRAMEWORK, graph_def.py:7657) cannot be reached without it. Precedent: DeckPicker.onCreate -> S_DECKPICKER (graph_def.py:835). No S_STATISTICS ENTERS exists in graph_def.py or parts/*.py at the time of writing. If the Statistics batch writes the same edge, delete this one.')
