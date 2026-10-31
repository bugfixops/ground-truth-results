# AnkiDroid batch 095 (LABEL helper): libanki Sched part 1, 40 methods, all REACHABLE (no UNREACHABLE entries).
# The row list is in graphs/AnkiDroid/parts/label_095.md. Automatic bytecode CALL edges are not written here.

e('Sched._deckNewLimit(long,Method)', 'Sched._deckNewLimitSingle', 'CALL',
  'a new-card fetch (getCard, _getCard, _getNewCard, _fillNew) computes the deck new limit through _deckNewLimit(long), which passes null so the default Method _deckNewLimitSingle is invoked reflectively',
  cls='non_standard',
  via=['reflection (Sched.class.getDeclaredMethod + Method.invoke)'],
  evidence='SRC com/ichi2/libanki/Sched.java:695-717 (697-698, 706);com/ichi2/libanki/Sched.java:690-692 (691); com/ichi2/libanki/Sched.java:588-634 (597)',
  note='Reflective call: Method.invoke at line 706 on the default Method set at lines 697-698. No gate constant applies; env and needs_state are unset.')

e('Sched._deckNewLimit(long,Method)', 'Sched._deckRevLimitSingle', 'CALL',
  'a review-card fetch (_getRevCard, _fillRev) computes the deck review limit through _deckRevLimit(long), which passes the _deckRevLimitSingle Method object to _deckNewLimit(long,Method)',
  cls='non_standard',
  via=['reflection (Sched.class.getDeclaredMethod + Method.invoke)'],
  evidence='SRC com/ichi2/libanki/Sched.java:695-717 (706);com/ichi2/libanki/Sched.java:1195-1201 (1197); com/ichi2/libanki/Sched.java:1249-1312 (1258)',
  note='Reflective call: Method.invoke at line 706 on the Method built at line 1197. No gate constant applies; env and needs_state are unset.')

e('Sched._checkLeech', 'Leech$LeechHook.runHook', 'CALL',
  'a review card answered with ease 1 reaches the leech threshold while a reviewer activity is attached to the scheduler; Hooks.runHook("leech") calls the always-on LeechHook',
  cls='explicit',
  evidence='SRC com/ichi2/libanki/Sched.java:1365, 1702,1721-1723, 2487-2489; com/ichi2/libanki/hooks/Hooks.java:52, 114-121; com/ichi2/libanki/hooks/Leech.java:35, 60-62; com/ichi2/anki/Reviewer.java:115',
  note='MISSING GATE MG892: the leech hook runs only when Sched.mContextReference is non-null (set by Reviewer.setContext at Reviewer.java:115; Sched.java:2487-2489). No constant covers an activity context reference, so env and needs_state are unset.')
