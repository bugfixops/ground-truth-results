# AnkiDroid batch 100 (LABEL helper): libanki Stats (32 methods across Stats, Stats$1, Stats$ChartType) and Storage.
# The row list is in graphs/AnkiDroid/parts/label_100.md. Automatic bytecode CALL edges are not written here.
# Only one batch method is UNREACHABLE (Storage.<init>); the others are REACHABLE and need no entry here.

e('Stats.calculateBreakdown', 'Stats$1.compare', 'CALL',
  'The hourly breakdown chart sorts its rows with an anonymous Comparator (Stats$1). Collections.sort calls the compare method through library dispatch, so there is no bytecode CALL edge from calculateBreakdown to compare.',
  cls='non_standard',
  via=['library dispatch (java.util.Collections.sort invokes Comparator.compare on the anonymous Stats$1 instance)'],
  evidence='SRC com/ichi2/libanki/Stats.java:852-858; INFERRED java.util.Collections.sort calls Comparator.compare (java.util is not in fw_src)',
  note='No gate constant applies. The compare call happens only when the list has two or more rows (JDK behaviour, INFERRED).')

e('Stats.calculateDue(Context,AxisType)', 'AdvancedStatistics.runFilter', 'CALL',
  'The forecast entry point runs the advancedStatistics hook through Hooks.runFilter. The hook list holds AdvancedStatistics only when the preference advanced_statistics_enabled is true, so the hook runFilter runs only then.',
  cls='non_standard',
  via=['hook registry dispatch (Hooks.runFilter loops over the Hook objects registered under the key advancedStatistics)'],
  evidence='SRC com/ichi2/libanki/Stats.java:308-311; com/ichi2/libanki/hooks/Hooks.java:61-62, 138-150; com/ichi2/libanki/hooks/AdvancedStatistics.java:141-148',
  note='MISSING GATE MG943: the preference advanced_statistics_enabled (default false, Hooks.java:61) must be true for AdvancedStatistics to be installed. Without it, calculateDue(AxisType) at Stats.java:331 runs instead.')

UNREACHABLE['Storage.<init>'] = ('no_trigger_in_app',
  'Storage declares no constructor, so only the implicit default constructor exists. Nothing in the source roots constructs it: there is no new Storage expression, no subclass of Storage, and no Storage.class reference. Every use of Storage is a static call (Storage.Collection, Storage.addIndices), so no instance is ever created.',
  'com/ichi2/libanki/Storage.java:35, 40-41; com/ichi2/async/DeckTask.java:790', 'SOURCE')
