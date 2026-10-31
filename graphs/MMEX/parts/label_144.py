# ================================================================== batch 144 (label_144): com.money.manager.ex.widget (40 methods in 5 classes)
# AllAccountBillsViewFactory (12), ButtonAddTransactionWidgetProvider (2), SingleAccountWidget (16),
# SingleAccountWidgetConfigureActivity incl. $1 (8), SummaryWidgetProvider (2).
# Rows, printed lines and the reason for each label: graphs/MMEX/parts/label_144.md (27 REACHABLE, 13 UNREACHABLE, 0 INCOMPLETE).
# Grep and query evidence: graphs/MMEX/parts/label_144.grep.txt (sections S1-S19).
# This file writes 13 e() edges (ENTRY from S_ENTRY, LIFECYCLE from the receiver and activity <init>, FRAMEWORK for the configure listener), 0 gui() edges,
# 13 UNREACHABLE entries and 9 sup pairs (D14a).
# Key decision (orchestrator's question): AllAccountBillsViewFactory.onDataSetChanged is DEAD, so it is UNREACHABLE (case "dead").
#   Its only construction is AccountBillsWidgetService.onGetViewFactory (AccountBillsWidgetService.java:27; grep S1), which batch 143 labels UNREACHABLE.
#   The framework binds the service only through RemoteViewsAdapter.bind (RemoteViewsAdapter.java:178), and AppWidgetServiceImpl refuses a service
#   that lacks BIND_REMOTEVIEWS (AppWidgetServiceImpl.java:1251, 3608-3611); the manifest gives BIND_JOB_SERVICE (AndroidManifest.xml:403).
#   The SecurityException is caught (RemoteViewsAdapter.java:184-186), so onGetViewFactory and onDataSetChanged never run.
#   The live case does not apply, so batch 052's label for QueryAccountBills.getFilterAccountSelection stays framework_never_calls and does not change.
# Configure activity: REACHABLE through the exported APPWIDGET_CONFIGURE intent-filter (ENTRY with env other_app, as PayeeActivity in label_004).
#   The provider names no android:configure (widget_info_single_account.xml:28 is commented out), which closes only the framework's own host start; loadAccounts stays UNREACHABLE.
# Cross-batch: the 12 sup pairs cut auto records whose destinations belong to other batches (CurrencyService.<init>, CurrencyService.getCurrencyFormatted,
#   Dataset.getUri, QueryAccountBills.<init>, Account.getName, AccountService.getAccountList(), AccountService.<init>). Those destinations keep any other route.
# The existing graph INTENT edges from SingleAccountWidget.initializeNewTransactionCommand (graph_def.py:12127) and ButtonAddTransactionWidgetProvider.onUpdate
#   (graph_def.py:12132) to CheckingTransactionEditActivity.<init> are not duplicated here (grep S17).

# ---- widget receivers (manifest ENTRY, then the framework path to each callback)

e('S_ENTRY', 'SummaryWidgetProvider.<init>', 'ENTRY',
  'the framework creates the widget receiver by class name because the manifest declares it exported with the APPWIDGET_UPDATE intent-filter; the framework then calls onReceive on it',
  evidence='SRC AndroidManifest.xml:78-88 (receiver name 79, APPWIDGET_UPDATE 82); SRC widget/SummaryWidgetProvider.java:35 (class declaration, implicit constructor); FW-SRC core/java/android/app/ActivityThread.java:3141, 3166 (handleReceiver loads the class by name and creates it), 3187 (receiver.onReceive)')

e('SummaryWidgetProvider.<init>', 'SummaryWidgetProvider.onUpdate', 'LIFECYCLE',
  'the framework calls onReceive on the receiver it has just created; AppWidgetProvider.onReceive calls this.onUpdate for ACTION_APPWIDGET_UPDATE',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:66 (onUpdate dispatch); FW-SRC services/appwidget/java/com/android/server/appwidget/AppWidgetServiceImpl.java:2283-2286 (sendUpdateIntentLocked, setComponent 2286); SRC widget/SummaryWidgetProvider.java:38-39 (override)')

e('S_ENTRY', 'ButtonAddTransactionWidgetProvider.<init>', 'ENTRY',
  'the framework creates the widget receiver by class name because the manifest declares it exported with the APPWIDGET_UPDATE intent-filter; the framework then calls onReceive on it',
  evidence='SRC AndroidManifest.xml:67-77 (receiver name 68, APPWIDGET_UPDATE 71); SRC widget/ButtonAddTransactionWidgetProvider.java:30 (class declaration, implicit constructor); FW-SRC core/java/android/app/ActivityThread.java:3141, 3166, 3187')

e('ButtonAddTransactionWidgetProvider.<init>', 'ButtonAddTransactionWidgetProvider.onUpdate', 'LIFECYCLE',
  'the framework calls onReceive on the receiver it has just created; AppWidgetProvider.onReceive calls this.onUpdate for ACTION_APPWIDGET_UPDATE',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:66; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2283-2286 (setComponent 2286); SRC widget/ButtonAddTransactionWidgetProvider.java:31-32 (override)')

e('S_ENTRY', 'SingleAccountWidget.<init>', 'ENTRY',
  'the framework creates the widget receiver by class name because the manifest declares it exported with the APPWIDGET_UPDATE intent-filter; the framework then calls onReceive on it',
  evidence='SRC AndroidManifest.xml:114-124 (receiver name 115, APPWIDGET_UPDATE 118); SRC widget/SingleAccountWidget.java:48 (class declaration, implicit constructor); FW-SRC core/java/android/app/ActivityThread.java:3141, 3166, 3187')

e('SingleAccountWidget.<init>', 'SingleAccountWidget.onUpdate', 'LIFECYCLE',
  'AppWidgetProvider.onReceive calls this.onUpdate for ACTION_APPWIDGET_UPDATE',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:66; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2283-2286 (setComponent 2286); SRC widget/SingleAccountWidget.java:69-70 (override)')

e('SingleAccountWidget.<init>', 'SingleAccountWidget.onDeleted', 'LIFECYCLE',
  'AppWidgetProvider.onReceive calls this.onDeleted for ACTION_APPWIDGET_DELETED; the framework sends it with setComponent to this provider, so the manifest filter (APPWIDGET_UPDATE only) does not gate it',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:73; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2290-2292 (sendDeletedIntentLocked, setComponent 2292); SRC widget/SingleAccountWidget.java:78-79 (override)')

e('SingleAccountWidget.<init>', 'SingleAccountWidget.onEnabled', 'LIFECYCLE',
  'AppWidgetProvider.onReceive calls this.onEnabled for ACTION_APPWIDGET_ENABLED; the framework sends it with setComponent when the first widget of this provider is added',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:85; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2277-2279 (sendEnableIntentLocked, setComponent 2279); SRC widget/SingleAccountWidget.java:87-88 (override)')

e('SingleAccountWidget.<init>', 'SingleAccountWidget.onDisabled', 'LIFECYCLE',
  'AppWidgetProvider.onReceive calls this.onDisabled for ACTION_APPWIDGET_DISABLED; the framework sends it with setComponent when the last widget of this provider is removed',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:87; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2297-2299 (sendDisabledIntentLocked, setComponent 2299); SRC widget/SingleAccountWidget.java:92-93 (override)')

e('SingleAccountWidget.<init>', 'SingleAccountWidget.onAppWidgetOptionsChanged', 'LIFECYCLE',
  'AppWidgetProvider.onReceive calls this.onAppWidgetOptionsChanged for ACTION_APPWIDGET_OPTIONS_CHANGED; the framework sends it with setComponent, so the manifest filter (APPWIDGET_UPDATE only) does not gate it',
  evidence='FW-SRC core/java/android/appwidget/AppWidgetProvider.java:81 (dispatch); FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:2303-2305 (sendOptionsChangedIntentLocked, setComponent 2305); SRC widget/SingleAccountWidget.java:97-98 (override)')

# ---- configure activity: exported with the APPWIDGET_CONFIGURE intent-filter, so another app can start it

e('S_ENTRY', 'SingleAccountWidgetConfigureActivity.<init>', 'ENTRY',
  'another app sends an APPWIDGET_CONFIGURE intent to the exported SingleAccountWidgetConfigureActivity',
  env=env_text('outside package: another app sends an APPWIDGET_CONFIGURE intent to SingleAccountWidgetConfigureActivity (exported=true)', ('other_app',)),
  evidence='SRC AndroidManifest.xml:327-329 (exported=true; APPWIDGET_CONFIGURE intent-filter); SRC widget/SingleAccountWidgetConfigureActivity.java:50; FW-SRC core/java/android/app/ActivityThread.java:2665-2672')

e('SingleAccountWidgetConfigureActivity.<init>', 'SingleAccountWidgetConfigureActivity.onCreate', 'LIFECYCLE',
  'the framework calls onCreate right after the constructor',
  evidence='FW-SRC core/java/android/app/ActivityThread.java:2724-2731; SRC widget/SingleAccountWidgetConfigureActivity.java:54-55 (onCreate override)')

e('SingleAccountWidgetConfigureActivity.onCreate', 'SingleAccountWidgetConfigureActivity$1.onClick', 'FRAMEWORK',
  'onCreate sets the field listener on add_button (line 65); View.performClick calls it when the button is tapped',
  evidence='SRC widget/SingleAccountWidgetConfigureActivity.java:65 (setOnClickListener(mOnClickListener)), 86-87 (field and onClick); FW-SRC core/java/android/view/View.java:6294 (performClick)')

# ---- UNREACHABLE entries: (kind, reason, evidence, confirmed_by)

# AllAccountBillsViewFactory: the factory is built only by AccountBillsWidgetService.onGetViewFactory, which is UNREACHABLE (batch 143).

UNREACHABLE['AllAccountBillsViewFactory.<init>'] = ('framework_never_calls',
    'its only construction is AccountBillsWidgetService.onGetViewFactory (AccountBillsWidgetService.java:27), which is UNREACHABLE (batch 143): RemoteViewsService.onBind calls onGetViewFactory only after a bind that the framework refuses (see onDataSetChanged). No other new AllAccountBillsViewFactory exists in the app source (grep S1). Its auto CALL to CurrencyService.<init> (line 47) is cut by sup.',
    'AccountBillsWidgetService.java:26-27; AllAccountBillsViewFactory.java:43; grep S1, S2; FW-SRC core/java/android/widget/RemoteViewsService.java:241 (onGetViewFactory called from onBind)',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.getContext'] = ('no_trigger_in_app',
    'no code in the widget package calls getContext() (the only occurrence is the declaration), and the factory is never reached as an object (see <init>), so no caller can reach this getter.',
    'AllAccountBillsViewFactory.java:130; grep S7 (getContext() occurs only at line 130)',
    'SOURCE')

UNREACHABLE['AllAccountBillsViewFactory.getCount'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory that a bound RemoteViewsService creates, and that bind never happens (see onDataSetChanged). Its auto CALL to getCountInternal (line 53) is cut by sup.',
    'AllAccountBillsViewFactory.java:50-53; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8, S9',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.getCountInternal'] = ('no_trigger_in_app',
    'private; its only caller is getCount (line 53, the only call in the class, grep S7), which is UNREACHABLE (see getCount).',
    'AllAccountBillsViewFactory.java:53, 60; grep S7, S8',
    'SOURCE')

UNREACHABLE['AllAccountBillsViewFactory.getItemId'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged).',
    'AllAccountBillsViewFactory.java:68-69; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.getLoadingView'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged).',
    'AllAccountBillsViewFactory.java:73-74; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.getViewAt'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged). Its auto CALL to CurrencyService.getCurrencyFormatted (line 85) is cut by sup.',
    'AllAccountBillsViewFactory.java:78-79, 85; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8, S9',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.getViewTypeCount'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged).',
    'AllAccountBillsViewFactory.java:93-94; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.hasStableIds'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged).',
    'AllAccountBillsViewFactory.java:98-99; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.onCreate'] = ('framework_never_calls',
    'RemoteViewsFactory callback: RemoteViewsService.onBind calls factory.onCreate only after onGetViewFactory returns a factory (lines 241-243), and that path never runs (see onDataSetChanged). The body is empty.',
    'AllAccountBillsViewFactory.java:103-104; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8, S14',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.onDataSetChanged'] = ('framework_never_calls',
    'DEAD PATH (the case decided for this batch). The only factory instance is created in AccountBillsWidgetService.onGetViewFactory (AccountBillsWidgetService.java:27; grep S1). The framework calls onDataSetChanged only on an adapter bound through RemoteViewsAdapter.bind (RemoteViewsAdapter.java:178; the factory callback sites are 230 and 1156). The bind goes through AppWidgetServiceImpl, which requires the service to declare BIND_REMOTEVIEWS (enforce at AppWidgetServiceImpl.java:1251; check and throw at 3608-3611). AccountBillsWidgetService declares BIND_JOB_SERVICE (AndroidManifest.xml:403; grep S4), so the bind throws SecurityException, which RemoteViewsAdapter catches (lines 184-186). No bind happens, so onGetViewFactory, onCreate and onDataSetChanged never run. The sups cut its three auto CALLs: QueryAccountBills.getFilterAccountSelection (line 113, the batch 052 caller), Dataset.getUri (116) and QueryAccountBills.<init> (112).',
    'AllAccountBillsViewFactory.java:107-108, 112-116; AccountBillsWidgetService.java:26-27; AndroidManifest.xml:401-403; FW-SRC RemoteViewsAdapter.java:172-190 (bind 178, catch 184-186), 230, 1156; FW-SRC services/appwidget/.../AppWidgetServiceImpl.java:1209-1251 (enforce 1251), 3598-3611; grep S1, S4, S14, S14b',
    'INFERRED')

UNREACHABLE['AllAccountBillsViewFactory.onDestroy'] = ('framework_never_calls',
    'RemoteViewsFactory callback: the framework calls it only on a factory from a bound RemoteViewsService, and that bind never happens (see onDataSetChanged).',
    'AllAccountBillsViewFactory.java:123-124; FW-SRC core/java/android/widget/RemoteViewsService.java:241-243; grep S8',
    'INFERRED')

# SingleAccountWidgetConfigureActivity: only loadAccounts is UNREACHABLE; the rest of the class is REACHABLE through the ENTRY above.

UNREACHABLE['SingleAccountWidgetConfigureActivity.loadAccounts'] = ('no_trigger_in_app',
    'private; the only mention in the app source is the commented-out call at line 83 (todo), so it has no live caller. Its auto CALLs (lines 133, 134, 139) are cut by sup.',
    'SingleAccountWidgetConfigureActivity.java:131, 83; grep S6',
    'SOURCE')

# ---- sup pairs (D14a): auto CALL records whose caller is UNREACHABLE in this batch

sup(('AllAccountBillsViewFactory.onDataSetChanged', 'QueryAccountBills.getFilterAccountSelection'))  # the orchestrator's sup (dead case)
sup(('AllAccountBillsViewFactory.onDataSetChanged', 'Dataset.getUri'))
sup(('AllAccountBillsViewFactory.onDataSetChanged', 'QueryAccountBills.<init>'))
sup(('AllAccountBillsViewFactory.<init>', 'CurrencyService.<init>'))
sup(('AllAccountBillsViewFactory.getCount', 'AllAccountBillsViewFactory.getCountInternal'))
sup(('AllAccountBillsViewFactory.getViewAt', 'CurrencyService.getCurrencyFormatted'))
sup(('SingleAccountWidgetConfigureActivity.loadAccounts', 'Account.getName'))
sup(('SingleAccountWidgetConfigureActivity.loadAccounts', 'AccountService.getAccountList()'))
sup(('SingleAccountWidgetConfigureActivity.loadAccounts', 'AccountService.<init>'))
