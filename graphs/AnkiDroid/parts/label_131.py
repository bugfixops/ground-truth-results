# AnkiDroid batch 131 (LABEL helper, schema 2). DB, Decks and LaTeX: 40 methods, all REACHABLE.
# The full row list with source cites is in graphs/AnkiDroid/parts/label_131.md.
#
# Methods: DB.<clinit>, DB.<init>, DB$MyDbErrorHandler.<init>, DB.close, DB.commit, DB.execute(String),
# DB.execute(String,Object[]), DB.executeMany, DB.executeScript, DB.getCursorMethodName, DB.getDatabase,
# DB.getMod, DB.insert, DB.queryColumn, DB.queryLongScalar, DB.queryScalar(String),
# DB.queryScalar(String,String[]), DB.setMod, DB.update(String,ContentValues),
# DB.update(String,ContentValues,String,String[]), Decks.<clinit>, Decks.<init>, Decks.all, Decks.allConf,
# Decks.confForDid, Decks.flush, Decks.get(long), Decks.get(long,boolean), Decks.getConf, Decks.isDyn,
# Decks.load, Decks.name(long), Decks.name(long,boolean), Decks.save(JSONObject), LaTeX.<clinit>,
# LaTeX.<init>, LaTeX._imgLink, LaTeX._latexFromHtml, LaTeX.installHook, LaTeX.mungeQA.
#
# Route ownership:
# - The DB, Decks, LaTeX and MyDbErrorHandler constructors and the static initialisers run on collection open
#   (Storage.java:45-63; Collection.java:140-157). The Collection constructor calls are CALL edges that the builder
#   writes from auto_calls.json. They are not written here.
# - The DB and Decks write methods run inside Collection.save (Collection.java:257-268) and the delete-note,
#   undo and check-database paths in DeckTask. Those edges are automatic CALL edges, not written here.
# - LaTeX.mungeQA runs through the Hooks.runFilter("mungeQA") route (Collection.java:1010; Hooks.java:138-150).
#   The card-render route is in the rows of the .md. The edge is automatic and not written here.
# - No e() calls and no UNREACHABLE entries: every method above has a route in the standard configuration.
#
# Caveats recorded in the .md:
# - DeckAdapter.processNodes queryScalar (DeckAdapter.java:251) needs a second deck in the deck list.
# - LaTeX._imgLink and _latexFromHtml need a card field that carries a LaTeX tag (content condition).
# - Decks.<clinit> body is not decoded (javap is not available); the source has only constant String fields.
