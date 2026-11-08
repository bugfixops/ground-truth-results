# AnkiDroid batch 096 (LABEL helper): Sched part 2, 40 methods.
# The row list is in graphs/AnkiDroid/parts/label_096.md.
# No UNREACHABLE entries: all 40 methods have a route from an entry point.
# Only two e() edges: the reflective calls from Sched._walkingCount to the count functions
# that _resetNewCount and _resetRevCount register (no automatic edge exists for them).

e('Sched._walkingCount', 'Sched._cntFnNew', 'CALL',
  'reflective call: _walkingCount invokes the count function that _resetNewCount passes to it (Method.invoke)',
  cls='non_standard',
  via=['reflection (Sched.class.getDeclaredMethod + Method.invoke)'],
  env=None,
  evidence='SRC com/ichi2/libanki/Sched.java:337-353; SRC com/ichi2/libanki/Sched.java:564-565')

e('Sched._walkingCount', 'Sched._cntFnRev', 'CALL',
  'reflective call: _walkingCount invokes the count function that _resetRevCount passes to it (Method.invoke)',
  cls='non_standard',
  via=['reflection (Sched.class.getDeclaredMethod + Method.invoke)'],
  env=None,
  evidence='SRC com/ichi2/libanki/Sched.java:337-353; SRC com/ichi2/libanki/Sched.java:1225-1226')
