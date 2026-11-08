# label_036.py: batch 036 (39 methods in 7 classes): ExportToCsvFile, FilterDatePeriods,
# FormatUtilities, FormatUtilities_Factory, FormatUtilities_MembersInjector, HttpMethods, InfoKeys.
# Evidence: graphs/MMEX/parts/label_036.md (table) and label_036.grep.txt (sections A-J).
#
# Edges: one CALL edge covers the Dagger Lazy hop into FormatUtilities_Factory.get (INFERRED).
# sup() cuts auto CALL edges whose caller cannot run (all 13 callers are UNREACHABLE in this batch
# or in batch 020/033, as the table rows say). Generated Dagger code is not in final_java_only, so
# the FormatUtilities_* UNREACHABLE rows are INFERRED.

e('CalculatorActivity.getFormattedAmount', 'FormatUtilities_Factory.get', 'CALL',
  'formatUtilitiesLazy.get() (Dagger Lazy<FormatUtilities> injected at CalculatorActivity.java:101) '
  'runs the factory provider FormatUtilities_Factory.get',
  cls='non_standard', via='Dagger Lazy<FormatUtilities>.get: DoubleCheck calls the factory provider (library behaviour, INFERRED; library and generated source not read)',
  evidence='INFERRED common/CalculatorActivity.java:101, 208; label_036.grep.txt E; generated code not in final_java_only')

sup(('AllDataListFragment.exportDataToCSVFile(String)', 'ExportToCsvFile.setPrefixName'))
sup(('AllDataListFragment.exportDataToCSVFile(String)', 'ExportToCsvFile.<init>'))
sup(('ExportToCsvFile.doInBackground', 'ExportToCsvFile.runTask'))
sup(('ExportToCsvFile.onPreExecute', 'ExportToCsvFile.getPrefixName'))
sup(('FilterDatePeriods.get', 'FilterDatePeriods.getCode'))
sup(('FilterDatePeriods.<clinit>', 'FilterDatePeriods.<init>'))
sup(('WebViewActivity.handleIntent', 'HttpMethods.<clinit>'))
sup(('FormatUtilities.getValueFormattedInBaseCurrency', 'FormatUtilities.format(Money,Currency)'))
sup(('FormatUtilities.getValueFormattedInBaseCurrency', 'CurrencyService.getBaseCurrency'))
sup(('FormatUtilities.getValueFormattedInBaseCurrency', 'FormatUtilities.getCurrencyService'))
sup(('FormatUtilities_MembersInjector.create', 'FormatUtilities_MembersInjector.<init>'))
sup(('FormatUtilities_MembersInjector.injectMembers', 'FormatUtilities_MembersInjector.injectCurrencyService'))
sup(('FormatUtilities_Factory.newFormatUtilities', 'FormatUtilities.<init>(MmexApplication)'))

UNREACHABLE['ExportToCsvFile.<init>'] = (
    'branch_never_taken',
    'only creator AllDataListFragment.exportDataToCSVFile(String) is UNREACHABLE in batch 020 (branch_never_taken)',
    'common/AllDataListFragment.java:474; graphs/MMEX/parts/label_020.md',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.doInBackground'] = (
    'framework_never_calls',
    'AsyncTask worker callback; runs only after execute(), whose only caller path is UNREACHABLE',
    'core/ExportToCsvFile.java:57; common/AllDataListFragment.java:476; FW-SRC core/java/android/os/AsyncTask.java:594-595',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.getPrefixName'] = (
    'framework_never_calls',
    'only caller onPreExecute; onPreExecute runs only from executeOnExecutor after execute(), which is UNREACHABLE',
    'core/ExportToCsvFile.java:93; FW-SRC core/java/android/os/AsyncTask.java:648',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.onPostExecute'] = (
    'framework_never_calls',
    'AsyncTask callback reached through finish after doInBackground, which never runs',
    'core/ExportToCsvFile.java:66; FW-SRC core/java/android/os/AsyncTask.java:695',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.onPreExecute'] = (
    'framework_never_calls',
    'AsyncTask callback reached only via executeOnExecutor after execute(), which is UNREACHABLE; no class file references it',
    'core/ExportToCsvFile.java:79; FW-SRC core/java/android/os/AsyncTask.java:648',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.runTask'] = (
    'framework_never_calls',
    'only caller doInBackground, which never runs',
    'core/ExportToCsvFile.java:60',
    'SOURCE')
UNREACHABLE['ExportToCsvFile.setPrefixName'] = (
    'branch_never_taken',
    'only caller exportDataToCSVFile(String) is UNREACHABLE in batch 020 (branch_never_taken)',
    'common/AllDataListFragment.java:475; graphs/MMEX/parts/label_020.md',
    'SOURCE')
UNREACHABLE['FilterDatePeriods.<clinit>'] = (
    'no_trigger_in_app',
    'enum static init; no class outside FilterDatePeriods.java uses the enum, so the first active use never happens',
    'core/FilterDatePeriods.java:25; label_036.grep.txt A, G',
    'SOURCE')
UNREACHABLE['FilterDatePeriods.<init>'] = (
    'no_trigger_in_app',
    'enum constructor, called only from <clinit>, which never runs',
    'core/FilterDatePeriods.java:39; label_036.grep.txt A',
    'SOURCE')
UNREACHABLE['FilterDatePeriods.contains'] = (
    'no_trigger_in_app',
    'no caller: no class file or auto record references it',
    'core/FilterDatePeriods.java:53; label_036.grep.txt G, H',
    'SOURCE')
UNREACHABLE['FilterDatePeriods.get'] = (
    'no_trigger_in_app',
    'no caller outside FilterDatePeriods.java',
    'core/FilterDatePeriods.java:28; label_036.grep.txt A',
    'SOURCE')
UNREACHABLE['FilterDatePeriods.getCode'] = (
    'no_trigger_in_app',
    'only caller get, which has no caller',
    'core/FilterDatePeriods.java:45; label_036.grep.txt A',
    'SOURCE')
UNREACHABLE['FormatUtilities.getValueFormattedInBaseCurrency'] = (
    'no_trigger_in_app',
    'no caller in app source; only a commented-out call in PriceEditModel.java:62',
    'core/FormatUtilities.java:305; investment/PriceEditModel.java:62; label_036.grep.txt E, G',
    'SOURCE')
UNREACHABLE['FormatUtilities_Factory.newFormatUtilities'] = (
    'no_trigger_in_app',
    'generated static helper with no caller; no class file or auto record references it',
    'auto_calls.json:16312-16313; label_036.grep.txt E, G',
    'INFERRED')
UNREACHABLE['FormatUtilities_MembersInjector.<init>'] = (
    'no_trigger_in_app',
    'generated constructor, called only from create, which has no caller',
    'auto_calls.json:16054-16055; batch036_cp_scan.txt line 61',
    'INFERRED')
UNREACHABLE['FormatUtilities_MembersInjector.create'] = (
    'no_trigger_in_app',
    'generated static factory helper with no caller; no class file references it',
    'auto_calls.json:16054-16055; label_036.grep.txt G',
    'INFERRED')
UNREACHABLE['FormatUtilities_MembersInjector.injectMembers'] = (
    'no_trigger_in_app',
    'generated entry point with no caller; Dagger calls injectCurrencyService directly',
    'auto_calls.json:16062-16063, 19136-19137; batch036_cp_scan.txt line 63',
    'INFERRED')
UNREACHABLE['HttpMethods.<clinit>'] = (
    'no_trigger_in_app',
    'enum init on first use HttpMethods.POST (WebViewActivity.java:144) in handleIntent, which is UNREACHABLE in batch 033',
    'common/WebViewActivity.java:144; auto_calls.json:37110-37111; graphs/MMEX/parts/label_033.md',
    'SOURCE')
UNREACHABLE['InfoKeys.<init>'] = (
    'no_trigger_in_app',
    'implicit constructor; no new InfoKeys in source and no class file references it',
    'core/InfoKeys.java:23; label_036.grep.txt C, G',
    'SOURCE')
