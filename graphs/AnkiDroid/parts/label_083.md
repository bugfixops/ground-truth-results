STATUS: RUNNING 17:49

Batch 083: CardStats, 2 methods (CardStats.<init>, CardStats.report). The batch file and the brief name com.ichi2.anki.CardStats, but the source file's package is com.ichi2.libanki (com/ichi2/libanki/CardStats.java, package line 1). Both methods are UNREACHABLE (no_trigger_in_app): no code in the app creates a CardStats or calls report. The only static method is report; the class declares no constructor. The outgoing calls of report are the builder's automatic CALL edges, so this part writes no e() edge. Entries are in graphs/AnkiDroid/parts/label_083.py.

| item | label | kind | reason | source |
|---|---|---|---|---|
| CardStats.<init> | UNREACHABLE | no_trigger_in_app | The class declares no constructor; its only member is the static method report (lines 14-123). No code creates an instance: grep -rn "CardStats" over the source root returns only the class declaration at line 12, and no other file in the app folder names the class (the build output holds only its own compiled class). Full argument in the UNREACHABLE entry of label_083.py. confirmed_by SOURCE. | com/ichi2/libanki/CardStats.java:12 |
| CardStats.report | UNREACHABLE | no_trigger_in_app | report is the class's only method (static, lines 14-123; it builds the card details HTML). No call site exists: grep -rn "CardStats" over the source root returns only the class declaration at line 12. A call from another class has to name CardStats (a qualified call, a static import or a subclass), and none exists. The build output holds only the class's own compiled file. Nothing in the app reaches report from an entry point. Full argument in the UNREACHABLE entry of label_083.py. confirmed_by SOURCE. | com/ichi2/libanki/CardStats.java:12; com/ichi2/libanki/CardStats.java:14-123 |

STATUS: DONE 17:51
