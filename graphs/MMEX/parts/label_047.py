# label_047.py: batch 047 (34 methods in 4 class groups): CurrencyService (24), CurrencyService$1 (2),
# CurrencyService_Factory (4), CurrencyService_MembersInjector (4).
# Result: 26 REACHABLE, 8 UNREACHABLE, 0 INCOMPLETE. Rows and printed lines: graphs/MMEX/parts/label_047.md.
# Grep evidence: graphs/MMEX/parts/label_047.grep.txt (sections A to C).
# Auto CALL records (auto_calls.json) are not rewritten here. This file writes:
#   - 1 non_standard CALL edge from getUsedCurrencies to the anonymous Comparator's compare (JDK sort, INFERRED),
#   - 8 UNREACHABLE entries (4 CurrencyService, 1 Factory, 3 MembersInjector),
#   - 19 sup pairs (D14a): auto CALL records whose caller is one of the 8 UNREACHABLE methods above.
# The DaggerMmxComponent edges that reach the Factory and MembersInjector methods are owned by the batch holding DaggerMmxComponent (not this batch).

# ================================================================== Collections.sort comparator (JDK, library not read: INFERRED)

e('CurrencyService.getUsedCurrencies', 'CurrencyService$1.compare', 'CALL',
  'getUsedCurrencies sorts the used currencies with the anonymous Comparator; the JDK sort calls compare on it',
  cls='non_standard', via='JDK Collections.sort(List, Comparator) calls Comparator.compare (library, INFERRED, not read)',
  evidence='SRC currency/CurrencyService.java:159-164 (new Comparator at 159, compare at 161-163, getName call at 162); auto_calls records CurrencyService.getUsedCurrencies -> CurrencyService$1.<init> (159) and CurrencyService$1.compare -> Currency.getName (162)')

# ================================================================== UNREACHABLE (batch 047)

UNREACHABLE['CurrencyService.getCurrency(String)'] = ('no_trigger_in_app',
  'No caller in the app: no auto CALL record has it as destination (label_047.grep.txt section C). The only literal call is in the unit-test helper DataHelpers.java:91 (src/test, not in the app graph). Its callee getIdForCode is also UNREACHABLE, so its auto CALL records are cut by sup below.',
  'SRC currency/CurrencyService.java:105-108; label_047.grep.txt sections A, C',
  'SOURCE')

UNREACHABLE['CurrencyService.getIdForCode'] = ('no_trigger_in_app',
  'Its only caller is getCurrency(String), which is UNREACHABLE (auto CALL at CurrencyService.java:106; no other record). Its outgoing auto CALL records are cut by sup below.',
  'SRC currency/CurrencyService.java:128-141; auto_calls record CurrencyService.getCurrency(String) -> CurrencyService.getIdForCode (106); label_047.grep.txt section C',
  'SOURCE')

UNREACHABLE['CurrencyService.getSymbolFor'] = ('no_trigger_in_app',
  'No caller in the app: no auto CALL record has it as destination; the only mention outside its own definition is the commented-out test line CurrencyServiceTests.java:77; the class directory names it only in CurrencyService.class (label_047.grep.txt sections A, B, C).',
  'SRC currency/CurrencyService.java:123-126; label_047.grep.txt sections A, B, C',
  'SOURCE')

UNREACHABLE['CurrencyService.getUnusedCurrencies'] = ('no_trigger_in_app',
  'Its only callers are in CurrencyRecyclerListFragment (CurrencyRecyclerListFragment.java:254 and 391), and that fragment is never created: CurrencyRecyclerListActivity has no start site (AndroidManifest.xml:359 has no intent-filter; the only Intent for it, MainActivity.java:644, is commented out). Batch 050 owns CurrencyRecyclerListFragment and must confirm there is no start site. If batch 050 finds one, change this entry and remove the eight sup pairs below.',
  'SRC currency/CurrencyService.java:169-184; recycler/CurrencyRecyclerListFragment.java:254, 391; recycler/CurrencyRecyclerListActivity.java:41; AndroidManifest.xml:359; MainActivity.java:644; label_047.grep.txt sections A, C',
  'SOURCE')

e('FormatUtilities_Factory.get', 'CurrencyService_Factory.get', 'CALL',
  'FormatUtilities_Factory.get calls currencyServiceProvider.get() at bytecode offset 25 (javax.inject.Provider, invokeinterface); the Provider is the CurrencyService_Factory instance built in DaggerMmxComponent',
  evidence='INFERRED generated FormatUtilities_Factory.class in app/build/intermediates/javac/debug/classes/com/money/manager/ex/core/: get offset 25 (offset as read in batch 055); the currencyServiceProvider Fieldref is in batch036_cp_scan.txt line 54; target is generated CurrencyService_Factory.class',
  cls='non_standard',
  via='javax.inject.Provider currencyServiceProvider (generated field), whose runtime class is CurrencyService_Factory')

UNREACHABLE['CurrencyService_MembersInjector.create'] = ('no_trigger_in_app',
  'No caller: no auto CALL record names it. DaggerMmxComponent injects CurrencyService by calling injectMRepository directly (DaggerMmxComponent.java:374), not through a MembersInjector instance. Its outgoing record to <init> is cut by sup below.',
  'generated: CurrencyService_MembersInjector.class in the class directory; auto_calls: no record has create as destination (grep.txt section C: 0 incoming); its only outgoing record is create -> <init> (CurrencyService_MembersInjector.java:21); DaggerMmxComponent.java:374 is the injectMRepository call, not create; label_047.grep.txt sections B, C',
  'INFERRED')

UNREACHABLE['CurrencyService_MembersInjector.<init>'] = ('no_trigger_in_app',
  'Its only caller is CurrencyService_MembersInjector.create, which is UNREACHABLE (auto CALL at CurrencyService_MembersInjector.java:21; no other record).',
  'auto_calls record CurrencyService_MembersInjector.create -> <init> (CurrencyService_MembersInjector.java:21); label_047.grep.txt section C',
  'INFERRED')

UNREACHABLE['CurrencyService_MembersInjector.injectMembers'] = ('no_trigger_in_app',
  'MembersInjector.injectMembers runs only through a MembersInjector<CurrencyService> instance, and none is created or held (create has no caller, and the component calls injectMRepository directly). No auto CALL record names it. Its outgoing record to injectMRepository (CurrencyService_MembersInjector.java:26) is cut by sup below.',
  'generated: CurrencyService_MembersInjector.class in the class directory; auto_calls record CurrencyService_MembersInjector.java:26; label_047.grep.txt sections B, C',
  'INFERRED')

# ================================================================== sup cuts (D14a): outgoing auto CALL records of the UNREACHABLE methods above

sup(('CurrencyService.getCurrency(String)', 'CurrencyService.getCurrency(Integer)'),
    ('CurrencyService.getCurrency(String)', 'CurrencyService.getIdForCode'),
    ('CurrencyService.getSymbolFor', 'Currency.getCode'),
    ('CurrencyService.getSymbolFor', 'CurrencyService.getCurrency(Integer)'),
    ('CurrencyService.getIdForCode', 'Currency.getCurrencyId'),
    ('CurrencyService.getIdForCode', 'CurrencyRepository.loadCurrency(String)'),
    ('CurrencyService.getIdForCode', 'CurrencyService.getRepository'),
    ('CurrencyService.getUnusedCurrencies', 'CurrencyService.getUsedCurrencies'),
    ('CurrencyService.getUnusedCurrencies', 'Currency.getCurrencyId'),
    ('CurrencyService.getUnusedCurrencies', 'CurrencyRepository.getAllColumns'),
    ('CurrencyService.getUnusedCurrencies', 'Select.<init>(String[])'),
    ('CurrencyService.getUnusedCurrencies', 'Select.where(String)'),
    ('CurrencyService.getUnusedCurrencies', 'Select.orderBy'),
    ('CurrencyService.getUnusedCurrencies', 'RepositoryBase.query(Class,Select)'),
    ('CurrencyService.getUnusedCurrencies', 'CurrencyService.getRepository'),
    ('CurrencyService_MembersInjector.create', 'CurrencyService_MembersInjector.<init>'),
    ('CurrencyService_MembersInjector.injectMembers', 'CurrencyService_MembersInjector.injectMRepository'))
