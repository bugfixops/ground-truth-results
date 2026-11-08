# AnkiDroid batch 083 (LABEL helper). CardStats (com/ichi2/libanki/CardStats.java; the batch file says com.ichi2.anki).
# Methods: CardStats.<init> and CardStats.report. Both are UNREACHABLE (no_trigger_in_app). No e() edges in this part.
# Gates: none (no MG ids used). The outgoing calls of report are the builder's automatic CALL edges and are not repeated here.

# --- CardStats.<init>: the class declares no constructor; no code creates an instance (grep over src/main/java).
UNREACHABLE['CardStats.<init>'] = ('no_trigger_in_app',
  "CardStats declares no constructor, so its only constructor is the implicit default one. No code creates an instance: "
  "grep -rn CardStats over the source root (src/main/java) returns only the class declaration at CardStats.java:12, and no other "
  "file in the app folder names the class (the build output holds only its own compiled class). The class has only the static "
  "method report, which has no caller either (see CardStats.report). So the constructor is never run.",
  "SRC com/ichi2/libanki/CardStats.java:12; SRC com/ichi2/libanki/CardStats.java:14-123",
  'SOURCE')

# --- CardStats.report: the only method of the class (static, lines 14-123). No call site in the source root.
UNREACHABLE['CardStats.report'] = ('no_trigger_in_app',
  "report is the only method of CardStats and it is static. No call site exists: grep -rn CardStats over the source root "
  "returns only the class declaration at CardStats.java:12. A call from another class has to name CardStats (a qualified "
  "call, a static import or a subclass), and no such reference exists. The build output holds only the class's own compiled "
  "file. Nothing in the app reaches report from an entry point, so it never runs.",
  "SRC com/ichi2/libanki/CardStats.java:12; SRC com/ichi2/libanki/CardStats.java:14-123",
  'SOURCE')
