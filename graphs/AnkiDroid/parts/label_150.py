# AnkiDroid batch 150 (LABEL helper). 32 whole-class methods (scratch/batches_ai.tsv row 150; names in scratch/h150/methods.txt).
# All 32 were already labelled REACHABLE by other parts (overlap column in parts/label_150.md). They are not labelled again here.
# No UNREACHABLE entries: none of the 32 is provably never entered.
#
# Four e() edges below close route gaps that out/methods.csv reports as UNRESOLVED with incoming 0:
# Sched$1.compare, Sched$DeckDueTreeNode.compareTo, Template$1.compare (comparators and Comparable hooks dispatched by
# java.util.Collections.sort; JDK source not read) and StudyOptionsFragment.onDestroy (destroyed by FragmentManager on replace;
# support-library source not read). Checked before writing: no existing edge in graph_def.py or parts/*.py has any of the four as dst.

e('Sched._fillLrn', 'Sched$1.compare', 'CALL',
  'two or more learning cards are due and the learning queue is refilled',
  env=None,
  needs_state=STATE_CARDS,
  evidence='SRC com/ichi2/libanki/Sched.java:773-805 (query 783-788; Collections.sort at 793; anonymous Comparator 793-798; compare 795-797)',
  note='java.util.Collections.sort (JDK source not read: INFERRED) calls compare only for a list of two or more entries. The gate is two or more learning cards with queue = 1 and due < mDayCutoff, returned by the query at lines 786-788 (capped by mReportLimit). _fillLrn is called at Sched.java:814 (existing route). Precedent for a comparator dispatched by Collections.sort: Decks$1.compare (graph_def.py:9010).')

e('Sched._groupChildren', 'Sched$DeckDueTreeNode.compareTo', 'CALL',
  'the deck tree is built (deckDueTree) and the deck list has two or more entries',
  env=None,
  needs_state=STATE_DECK,
  evidence='SRC com/ichi2/libanki/Sched.java:432-433, 437-446, 2502, 2532-2551',
  note='Collections.sort(grps) at Sched.java:443 calls compareTo on the Comparable element type (JDK source not read: INFERRED). The JDK calls compareTo only for a list of two or more nodes, so the gate is one deck beyond the first (assumed: the Default deck is listed, not checked). The sort is reached from deckDueTree (Sched.java:432-433). Precedent: Stats$1.compare (graph_def.py:9323).')

e('Template.render_unescaped', 'Template$1.compare', 'CALL',
  'a field tag with two or more modifiers that is not itself a context key (a two-colon tag in a note type template)',
  env=None,
  needs_state=STATE_NOTE,
  evidence='SRC com/ichi2/libanki/template/Template.java:199-200, 209-218, 228-240 (Collections.sort at 229; compare at 233-238)',
  note='MG1022: the gate is a tag with two or more modifiers (mods has two or more entries, line 216). No stock template in src/main has such a tag (existing label note). Collections.reverse(mods) at line 228 and Collections.sort at line 229 call compare only for two or more entries (JDK source not read: INFERRED). needs_state is STATE_NOTE because a card with such a template renders only when a note exists. render_unescaped is called at Template.java:169 and 188 (existing route).')

e('DeckPicker.loadStudyOptionsFragment', 'StudyOptionsFragment.onDestroy', 'FRAMEWORK',
  'a second load replaces the StudyOptionsFragment that is still in the studyoptions container of the tablet layout',
  env=None,
  evidence='SRC com/ichi2/anki/DeckPicker.java:1651-1655, 365-367; SRC res/layout-xlarge/homescreen.xml (id studyoptions_fragment); SRC com/ichi2/anki/StudyOptionsFragment.java:195-202; FW-SRC core/java/android/app/FragmentManager.java:1407-1433; FW-SRC core/java/android/app/Fragment.java:2761-2768',
  note='ft.replace at DeckPicker.java:1654 removes the fragment already in that container, and the FragmentManager destroys it. Framework analog: FragmentManager.java:1407-1433 (moveToState) and Fragment.java:2768 (performDestroy calls onDestroy). DeckPicker uses the support-library FragmentManager (getSupportFragmentManager), whose source is not read, so the mechanism is INFERRED. The container id exists only in the xlarge layout (homescreen.xml) and is found at DeckPicker.java:365; mFragmented (367) is true only there. The activity-finish route to onDestroy is not written here (existing LIFECYCLE label; no edge for it).')
