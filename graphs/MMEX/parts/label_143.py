# ================================================================== batch 143 (label_143): 31 methods in four classes
# com.money.manager.ex.viewmodels.AccountTransactionDisplay (19), IncomeVsExpenseReportEntity (8),
# com.money.manager.ex.widget.AccountBillsWidgetProvider (2), AccountBillsWidgetService (2).
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_143.md (26 REACHABLE, 5 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_143.grep.txt.
# This file writes 2 e() edges (ENTRY and LIFECYCLE for the widget receiver), 0 gui() edges,
# 5 UNREACHABLE entries (3 getters with no caller, 2 widget service methods the framework never runs) and 4 sup pairs (D14a).
# The 19 AccountTransactionDisplay methods and the 5 IncomeVsExpenseReportEntity methods that are REACHABLE get their
# routes from auto CALL records (auto_calls.json, D7). Those records have callers in batches 012, 104, 105, 110 and 112,
# which are not merged, so the routes are interim (D8).
# The two sup pairs for getExpenses/getIncome/getTransfers cut the auto CALL records to EntityBase.getMoney; those records
# have an UNREACHABLE caller, so they are cut here (the same pattern as label_052.py).

# ---- widget receiver (AccountBillsWidgetProvider): manifest ENTRY, then the framework path to onUpdate

e('S_ENTRY', 'AccountBillsWidgetProvider.<init>', 'ENTRY',
  'the framework creates the widget receiver by class name because the manifest declares it exported with the APPWIDGET_UPDATE intent-filter; the framework then calls onReceive on that receiver',
  evidence='SRC AndroidManifest.xml:89-99; FW-SRC core/java/android/app/ActivityThread.java:3141-3166 (handleReceiver: loadClass(component).newInstance() at 3166), 3187 (receiver.onReceive); the matching of the intent-filter to the broadcast is not in fw_src: INFERRED, source not read')

e('AccountBillsWidgetProvider.<init>', 'AccountBillsWidgetProvider.onUpdate', 'LIFECYCLE',
  'the framework calls onReceive on the receiver it has just created; AppWidgetProvider.onReceive calls this.onUpdate when the action is ACTION_APPWIDGET_UPDATE',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:57-68 (onReceive; this.onUpdate at 66); FW-SRC core/java/android/app/ActivityThread.java:3187; SRC widget/AccountBillsWidgetProvider.java:40-77 (the override)')

# ---- UNREACHABLE: income report getters with no caller (source root)

UNREACHABLE['IncomeVsExpenseReportEntity.getExpenses'] = ('no_trigger_in_app',
    'no caller: the only occurrence of getExpenses in the app source is its declaration (grep Q3); auto_calls.json has no CALL record with it as dst; the Expenses column is loaded by loadFromCursor (line 50) and never read through this getter',
    'IncomeVsExpenseReportEntity.java:66-68, 50; label_143.grep.txt Q1, Q3, Q4', 'SOURCE')

UNREACHABLE['IncomeVsExpenseReportEntity.getIncome'] = ('no_trigger_in_app',
    'no caller: the only occurrence of getIncome in the app source is its declaration (grep Q3; HomeFragment.java:252 is a comment and BehaviourSettings.getIncomeExpensePeriod is a different method); auto_calls.json has no CALL record with it as dst; the Income column is loaded at line 49 and never read through this getter',
    'IncomeVsExpenseReportEntity.java:62-64, 49; label_143.grep.txt Q1, Q3, Q4', 'SOURCE')

UNREACHABLE['IncomeVsExpenseReportEntity.getTransfers'] = ('no_trigger_in_app',
    'no caller: the only occurrence of getTransfers in the app source is its declaration (grep Q3); auto_calls.json has no CALL record with it as dst; the Transfers column is loaded at line 51 and never read through this getter',
    'IncomeVsExpenseReportEntity.java:70-72, 51; label_143.grep.txt Q1, Q3, Q4', 'SOURCE')

# ---- UNREACHABLE: widget service (framework never binds it, see label_052 for the same chain)

UNREACHABLE['AccountBillsWidgetService.<init>'] = ('framework_never_calls',
    'the framework creates the service only when it binds it, through RemoteViewsService.onBind (fw_src RemoteViewsService.java:235-243). The bind is refused: AppWidgetServiceImpl.enforceServiceExistsAndRequiresBindRemoteViewsPermission rejects a service that does not declare BIND_REMOTEVIEWS (fw_src AppWidgetServiceImpl.java:1251, 3598-3612), and the manifest declares BIND_JOB_SERVICE for this service (AndroidManifest.xml:401-403). RemoteViewsAdapter catches the SecurityException (fw_src RemoteViewsAdapter.java:178, 184-188). The app has no other route into the class (no intent-filter). The client-side AppWidgetManager.bindRemoteViewsService is not in fw_src: INFERRED.',
    'AccountBillsWidgetService.java:22-23; AndroidManifest.xml:401-403; fw_src RemoteViewsService.java:235-243; fw_src RemoteViewsAdapter.java:176-188; fw_src AppWidgetServiceImpl.java:1251, 3598-3612', 'INFERRED')

UNREACHABLE['AccountBillsWidgetService.onGetViewFactory'] = ('framework_never_calls',
    'the only caller is RemoteViewsService.onBind (fw_src RemoteViewsService.java:241), which runs only when the framework binds the service; the bind is refused (see AccountBillsWidgetService.<init>), so onGetViewFactory never runs and AllAccountBillsViewFactory is never created by this path',
    'AccountBillsWidgetService.java:25-28; fw_src RemoteViewsService.java:235-243; fw_src AppWidgetServiceImpl.java:1251, 3598-3612', 'INFERRED')

# auto CALL records whose caller is UNREACHABLE in this batch (auto_calls.json), cut by sup (D14a)
sup(('IncomeVsExpenseReportEntity.getExpenses', 'EntityBase.getMoney'))
sup(('IncomeVsExpenseReportEntity.getIncome', 'EntityBase.getMoney'))
sup(('IncomeVsExpenseReportEntity.getTransfers', 'EntityBase.getMoney'))
sup(('AccountBillsWidgetService.onGetViewFactory', 'AllAccountBillsViewFactory.<init>'))
