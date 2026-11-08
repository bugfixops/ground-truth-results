# ================================================================== batch 129 (label_129): CheckingTransactionEditActivity_MembersInjector (4 methods), EditTransactionActivityConstants (1 method); 5 methods
# Result: 1 REACHABLE, 4 UNREACHABLE (rows: graphs/MMEX/parts/label_129.md). Grep evidence: graphs/MMEX/parts/label_129.grep.txt.
# This file writes:
#   - 4 UNREACHABLE entries (kind no_trigger_in_app): create, <init> and injectMembers of the generated MembersInjector (INFERRED), and EditTransactionActivityConstants.<init> (SOURCE),
#   - 2 sup cuts (D14) for the auto CALL records out of the UNREACHABLE methods: create -> <init> and injectMembers -> injectDatabase.
# No edge is written. The one REACHABLE method, injectDatabase, is reached only through auto CALL records (DaggerMmxComponent.injectCheckingTransactionEditActivity -> injectDatabase, D7), so the build finds it (D4).

# ---- UNREACHABLE: the generated MembersInjector factory, constructor and instance injector, and the constants class constructor

UNREACHABLE['CheckingTransactionEditActivity_MembersInjector.<init>'] = ('no_trigger_in_app',
    'Dagger-generated constructor (not in the source root) whose only caller record is CheckingTransactionEditActivity_MembersInjector.create (auto record line 22), and create has no caller (grep B2, C1); no class file other than CheckingTransactionEditActivity_MembersInjector.class references <init> (grep C1)',
    'CheckingTransactionEditActivity_MembersInjector.class bytecode line 22 (final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/transactions/); label_129.grep.txt B1, B2, C1',
    'INFERRED')

UNREACHABLE['CheckingTransactionEditActivity_MembersInjector.create'] = ('no_trigger_in_app',
    'Dagger-generated static factory (not in the source root) with no caller record in auto_calls.json (grep B2) and no Methodref to create in any of the 825 class files (grep C1); no app source names the MembersInjector (grep A1)',
    'CheckingTransactionEditActivity_MembersInjector.class bytecode line 22 (final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/transactions/); label_129.grep.txt A1, B2, C1',
    'INFERRED')

UNREACHABLE['CheckingTransactionEditActivity_MembersInjector.injectMembers'] = ('no_trigger_in_app',
    'Dagger-generated instance method (not in the source root) with no caller record in auto_calls.json for any receiver (grep B2, B3); its only Methodref is inside CheckingTransactionEditActivity_MembersInjector.class itself (grep C1), and the class is never instantiated (no Methodref to create or to <init> outside the class, grep C1), so no MembersInjector object reaches it; the component injects through injectDatabase directly (DaggerMmxComponent.class bytecode line 389)',
    'CheckingTransactionEditActivity_MembersInjector.class bytecode line 27 (final_java_only/MMEX/app/MMEX-#v2024.06.14/app/build/intermediates/javac/debug/classes/com/money/manager/ex/transactions/); label_129.grep.txt B1, B2, B3, C1',
    'INFERRED')

UNREACHABLE['EditTransactionActivityConstants.<init>'] = ('no_trigger_in_app',
    'Constants-only class (20 uncommented static final String fields, all literal, grep E4 and E6) with no explicit constructor (grep E1); no new EditTransactionActivityConstants in the source (grep A2); no class file in the build references EditTransactionActivityConstants at all, so no Methodref to <init> (grep C1); no auto_calls.json record has it as dst (grep B1)',
    'transactions/EditTransactionActivityConstants.java:23-48; label_129.grep.txt A2, B1, C1, E1, E4',
    'SOURCE')

# ---- D14: the outgoing auto CALL records of the UNREACHABLE methods (caller UNREACHABLE in this batch)

sup(('CheckingTransactionEditActivity_MembersInjector.create', 'CheckingTransactionEditActivity_MembersInjector.<init>'))  # caller UNREACHABLE (D14); auto record line 22
sup(('CheckingTransactionEditActivity_MembersInjector.injectMembers', 'CheckingTransactionEditActivity_MembersInjector.injectDatabase'))  # caller UNREACHABLE (D14); auto record line 27
