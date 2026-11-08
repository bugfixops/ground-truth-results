# AnkiDroid batch 108 (LABEL helper). Syncer part: 35 methods (34 Syncer methods and Template$1.compare).
# The full row list is in graphs/AnkiDroid/parts/label_108.md.
# 31 methods are REACHABLE (no entries here). 4 methods are UNREACHABLE (no_trigger_in_app, entries below).
# No e() edges are written. The render_unescaped -> Template$1.compare edge (non_standard, via Collections.sort)
# belongs to the Template batch.

UNREACHABLE['Syncer.applyChanges'] = ('no_trigger_in_app', "No caller. Syncer is referenced only in Connection.java (lines 281, 288 and 289) and in Syncer.java. The only call with this name in Syncer.java is line 170, mServer.applyChanges(sch). Its receiver is the HttpSyncer field, so it resolves to HttpSyncer.applyChanges (HttpSyncer.java:327) and not to this method. Connection.java does not call it.", 'SRC com/ichi2/libanki/sync/Syncer.java:170, 275-281; SRC com/ichi2/libanki/sync/HttpSyncer.java:327; SRC com/ichi2/async/Connection.java:281-289', 'SOURCE')

UNREACHABLE['Syncer.finish()'] = ('no_trigger_in_app', "No caller. Nothing in Connection.java or Syncer.java calls the no-argument finish() (418-420). The finish calls at Syncer.java:212 and 909 are mServer.finish() on the HttpSyncer field and resolve to HttpSyncer.finish() (HttpSyncer.java:347). Line 419 calls finish(long), not this method.", 'SRC com/ichi2/libanki/sync/Syncer.java:212, 418-420, 909; SRC com/ichi2/libanki/sync/HttpSyncer.java:347; SRC com/ichi2/async/Connection.java:281-289', 'SOURCE')

UNREACHABLE['Syncer.start'] = ('no_trigger_in_app', "No caller. The only call with this name in Syncer.java is mServer.start(o) at line 157. It passes one argument and resolves to HttpSyncer.start(JSONObject) (HttpSyncer.java:332). This method takes three arguments, so line 157 cannot call it. Connection.java does not call it.", 'SRC com/ichi2/libanki/sync/Syncer.java:157, 622-629; SRC com/ichi2/libanki/sync/HttpSyncer.java:332; SRC com/ichi2/async/Connection.java:281-289', 'SOURCE')

UNREACHABLE['Syncer.sync()'] = ('no_trigger_in_app', "No caller. Syncer.sync() (79-81) has no call site outside itself (line 80 is the self-call sync(null)). Connection.java:288 calls client.sync(this) with one argument, which is the other overload sync(Connection) (84). DeckPicker.sync() (DeckPicker.java:1266-1268) is a different method on a different class.", 'SRC com/ichi2/libanki/sync/Syncer.java:79-81, 84; SRC com/ichi2/async/Connection.java:288; SRC com/ichi2/anki/DeckPicker.java:1266-1268', 'SOURCE')
