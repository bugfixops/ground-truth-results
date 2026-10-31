# ================================================================== batch 067 (label_067): Payee (9 methods)
# Result: 8 REACHABLE, 1 UNREACHABLE (rows and printed lines: graphs/MMEX/parts/label_067.md).
# No e() edges: every bytecode CALL into a Payee method is already an auto record (D7). The REACHABLE rows
# take their routes from the exported CheckingTransactionEditActivity INSERT and EDIT paths (owned by other batches).
# One sup pair (D14a): the auto CALL record whose caller is UNREACHABLE in this batch.
# No SCREENS and no grep file: the one UNREACHABLE claim is a SOURCE fact (the grep is quoted in the reason).

# ================================================================== UNREACHABLE: the ContentValues constructor

UNREACHABLE['Payee.<init>(ContentValues)'] = ('no_trigger_in_app',
    'no caller: no new Payee(...) with an argument exists in the app source (grep over src/main/java: 5 hits, all the no-arg new Payee() at Core.java:151, PayeeService.java:56 and :94, PayeeListFragment.java:206, PayeeReportFragment.java:302; src/test has one more, DataHelpers.java:61, which is not in the app); reflection creates entities with the no-arg constructor only (Class.newInstance at RepositoryBase.java:109 and :134, SqlRepositoryBase.java:84); no auto CALL record has it as dst. Its own auto CALL to EntityBase.<init>(ContentValues) is cut by the sup below',
    'domainmodel/Payee.java:37-39; datalayer/RepositoryBase.java:109, 134; datalayer/SqlRepositoryBase.java:84; auto_calls.json record Payee.java:38',
    'SOURCE')

# ================================================================== sup (D14a): auto CALL record whose caller is UNREACHABLE here

sup(('Payee.<init>(ContentValues)', 'EntityBase.<init>(ContentValues)'))
