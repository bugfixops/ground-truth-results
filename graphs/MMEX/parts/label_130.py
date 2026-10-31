# ================================================================== batch 130 (label_130): EditTransactionCommonFunctions (methods 1-40 of 115); 40 methods
# Result: 39 REACHABLE, 1 UNREACHABLE (rows: graphs/MMEX/parts/label_130.md). Grep evidence: graphs/MMEX/parts/label_130.grep.txt.
# This file writes:
#   - 1 UNREACHABLE entry (kind no_trigger_in_app, SOURCE): hasAttachments (its only definition is at line 260-262; no caller anywhere),
#   - 1 sup cut (D14) for the auto CALL record out of the UNREACHABLE method: hasAttachments -> getAttachments (auto record line 261).
# No e() edge is written: every caller of the other 39 methods is either an auto CALL record (already in auto_calls.json, D7) or an edge owned by another batch
# (D1: edges are owned by the destination batch; AGENT_NOTES.md has no "Ownership rule (cross-batch edges)" section, so D1 is the rule used).
# Routes that are not auto CALL records (EVENT, GUI, ENTRY, LIFECYCLE framework steps) are in label_130.md only; their unprinted platform steps are marked INFERRED there.

# ---- UNREACHABLE: hasAttachments has no caller anywhere in the app source or the build

UNREACHABLE['EditTransactionCommonFunctions.hasAttachments'] = ('no_trigger_in_app',
    'Only definition in the app source (transactions/EditTransactionCommonFunctions.java:260-262, returns !getAttachments().isEmpty()); grep over the app source finds no caller (label_130.grep.txt hasAttachments grep); the javac debug class grep finds no reference (exit 1); auto_calls.json has no record with dst hasAttachments (n=0, label_130.grep.txt auto query). Its only outgoing record is to getAttachments at line 261, which is cut by sup (D14)',
    'transactions/EditTransactionCommonFunctions.java:260-262 (261); label_130.grep.txt (hasAttachments grep; javac debug classes grep; auto query n=0)',
    'SOURCE')

# ---- D14: the outgoing auto CALL record of the UNREACHABLE method (caller UNREACHABLE in this batch)

sup(('EditTransactionCommonFunctions.hasAttachments', 'EditTransactionCommonFunctions.getAttachments'))  # caller UNREACHABLE (D14); auto record line 261
