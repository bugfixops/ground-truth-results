# ================================================================== batch 061 (label_061): AccountTransaction (38 methods),
# AccountTransaction$$Parcelable.<clinit> and <init> (2 generated methods; the .java is not in the source root).
# Result: 38 REACHABLE, 2 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_061.md; grep evidence: graphs/MMEX/parts/label_061.grep.txt).
# No e() or GUI edges are written here (D7): every REACHABLE route runs through auto CALL records (auto_calls.json) from route nodes
# owned by other batches: CheckingTransactionEditActivity (onCreate, handleIntent, loadTransaction, saveData, saveTransaction,
# onSaveInstanceState, restoreInstanceState), EditTransactionCommonFunctions (initializeInputControls callees, validateData, the TextWatchers),
# MainActivity.populateScheduledTransactions, AccountTransactionRepository (load, insert, update) and RepositoryBase (first, query).
# The two Parcelable methods are entered by the auto CALL from AccountTransaction$$Parcelable$1.createFromParcel (batch 062) at
# AccountTransaction$$Parcelable.java:28; the FRAMEWORK edge into that creator belongs to batch 062 (D1).
# UNREACHABLE: AccountTransaction.<init>(ContentValues) and AccountTransaction.getFollowUpId (no caller, no bytecode reference).
# sup (D14a): the 2 auto CALL records whose caller is UNREACHABLE in this batch are cut (both match auto_calls.json).

# ================================================================== UNREACHABLE

UNREACHABLE['AccountTransaction.<init>(ContentValues)'] = ('no_trigger_in_app',
    'no caller. The only construction in app source is the no-argument new AccountTransaction() at AccountTransaction.java:57. RepositoryBase.first and RepositoryBase.query build entities with resultType.newInstance() (RepositoryBase.java:109, 134), which calls the no-argument constructor. No other build class both names AccountTransaction and holds the (Landroid/content/ContentValues;)V descriptor (grep evidence in label_061.grep.txt). No auto_calls.json record has this dst. Its one outgoing auto CALL (line 79, EntityBase.<init>(ContentValues)) is cut by sup below',
    'AccountTransaction.java:57, 78-80; RepositoryBase.java:109, 134', 'SOURCE')

UNREACHABLE['AccountTransaction.getFollowUpId'] = ('no_trigger_in_app',
    'no caller. The only mentions in app source are the getter declaration (line 179) and the call setFollowUpId(Constants.NOT_SET) in the no-argument constructor (line 75, a setter call). No auto_calls.json record has this dst, no build class other than AccountTransaction.class names getFollowUpId, and the generated wrapper does not reference it (grep evidence in label_061.grep.txt). Its one outgoing auto CALL (line 180, EntityBase.getInt) is cut by sup below',
    'AccountTransaction.java:75, 179-181', 'SOURCE')

# ================================================================== sup (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('AccountTransaction.<init>(ContentValues)', 'EntityBase.<init>(ContentValues)'),
    ('AccountTransaction.getFollowUpId', 'EntityBase.getInt'))
