# AnkiDroid batch 141 (LABEL helper): 40 methods in 7 classes (BasicAudioFieldController, DeckOptions,
# DrawableContainer, FilteredDeckOptions$DeckPreferenceHack$Editor, LegendDrawable, Lookup, MyAccount).
# Labels: 40 REACHABLE, 0 UNREACHABLE. Every method already has a row and route edges in an earlier part
# (overlap: label_058, 027, 112, 029, 113, 052, 035; chart route through label_065/066). Edges written here:
#  - FilteredDeckOptions.onCreate -> S_FILTEREDDECKOPTIONS ENTERS: page-entry fix. The src is outside batch 141
#    (its row is label_029.md:11), and no ENTERS into S_FILTEREDDECKOPTIONS exists in graph_def.py or any parts/*.py.
# Constants used: STATE_DECK (graph_def.py:128). No new constants.

e('FilteredDeckOptions.onCreate', 'S_FILTEREDDECKOPTIONS', 'ENTERS',
  'the filtered deck options screen is live once onCreate has loaded the filtered deck and built the preference tree',
  needs_state=STATE_DECK,
  env=None,
  evidence='SRC com/ichi2/anki/FilteredDeckOptions.java:351-400',
  note='Page-entry edge from a method outside batch 141, because S_FILTEREDDECKOPTIONS had no ENTERS edge (grep of graph_def.py and parts/*.py). The page GUI and SYSTEM edges at graph_def.py:3797-3827 and the Editor write chain at 3858-3893 have no entry without it. The screen is built only for a dyn deck (lines 369-381); otherwise finish() at 357 or 372. Mirrors label_134.py:10 (DeckOptions.onCreate -> S_DECKOPTIONS ENTERS). If another part adds the same ENTERS, keep one copy.')
