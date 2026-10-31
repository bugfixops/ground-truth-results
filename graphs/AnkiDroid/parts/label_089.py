# AnkiDroid batch 089 (LABEL helper). Exporter constructors (2 methods), class Exporter in
# com/ichi2/libanki/AnkiPackageExporter.java:42-56. The row list is in graphs/AnkiDroid/parts/label_089.md.
# No e() edges: Exporter.<init>(Collection) is reached through the automatic super call in
# AnkiPackageExporter (line 299), and the export route (DeckPicker, ExportDialog, DeckTask) is owned by other batches.

UNREACHABLE['Exporter.<init>(Collection,Long)'] = ('no_trigger_in_app',
  'No call site exists in the source root. The only subclasses, AnkiExporter and AnkiPackageExporter, call the one-argument super(col) (AnkiPackageExporter.java:70, 299). A grep for new Exporter(, new AnkiExporter( and the two-argument super form finds none. The one construction of a subclass, new AnkiPackageExporter(col) at DeckTask.java:891, uses the one-argument form, and the deck id is passed later through setDid (DeckTask.java:894; AnkiPackageExporter.java:289-291), not through this constructor. A grep for the bare word Exporter finds only the declarations at AnkiPackageExporter.java:42, 47, 53 and 61.',
  'com/ichi2/libanki/AnkiPackageExporter.java:42-56, 61-70, 289-291, 296-299; com/ichi2/async/DeckTask.java:891, 894', 'SOURCE')
