# AnkiDroid batch 018 (LABEL helper). AnkiDroidWidgetSmall (the small widget receiver) and AnkiDroidWidgetSmall$UpdateService
# (the service that builds the widget view). 10 methods; the full row list is in graphs/AnkiDroid/parts/label_018.md.
#
# Route ownership: the S_ENTRY edges into the receiver (<clinit>, <init>, onEnabled, onDisabled) and into the mount
# receiver ($1.onReceive) are written here (destination in this part). AnkiDroidWidgetSmall.onUpdate and onReceive already
# have S_ENTRY edges in graph_def.py (lines 151-154); they are not written again.
# UpdateService.<init> is reached by startService in WidgetStatus.java:106-109 (inside WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute,
# batch 080). That INTENT edge is written by batch 080 (source part), not here. Its gate is STATE_SETTINGS (sSmallWidgetEnabled).
# The CALL edges onStart -> buildUpdate, buildUpdate -> <clinit>, buildUpdate -> $1.<init> and onEnabled/onDisabled -> AnkiDroidApp
# come from auto_calls.json and are not written here. The auto CALL $1.onReceive -> WidgetStatus.update (line 118) is not
# written here either: it has no guard for the second MEDIA_MOUNTED broadcast (lead for the orchestrator, see the SYSTEM edge note).
# Gates: MG122 (the last widget is removed, onDisabled), MG123 (the SD card is unmounted at the widget update, so the mount
# receiver is registered). ENV_WIDGET covers adding the widget and APPWIDGET_UPDATE, not removal.

# --- Widget receiver entries (S_ENTRY). The AppWidget host instantiates the receiver, then calls the callback.

e('S_ENTRY', 'AnkiDroidWidgetSmall.<clinit>', 'ENTRY',
  'the AppWidget host instantiates the small widget receiver (class initialisation runs before the first instance)',
  env=ENV_WIDGET,
  evidence='SRC AndroidManifest.xml:253-263; SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:40-41; FW-SRC core/java/android/app/ActivityThread.java:3141, 3166',
  note='INFERRED: the JVM runs the class initialiser when the framework instantiates the receiver (ActivityThread.handleReceiver, newInstance at line 3166); the class initialisation step is not in fw_src. The static fields at lines 40-41 make <clinit> a real method. The same method is also reached by the auto CALL buildUpdate -> <clinit> (auto_calls.json, line 110).')

e('S_ENTRY', 'AnkiDroidWidgetSmall.<init>', 'ENTRY',
  'the AppWidget host instantiates the small widget receiver',
  env=ENV_WIDGET,
  evidence='SRC AndroidManifest.xml:253-263; SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:38; FW-SRC core/java/android/app/ActivityThread.java:3166',
  note='The class has no explicit constructor, so this is the implicit default constructor. The framework calls it at ActivityThread.java:3166. The class initialisation edge above runs first.')

e('S_ENTRY', 'AnkiDroidWidgetSmall.onEnabled', 'ENTRY',
  'the user adds the first AnkiDroid small widget: the AppWidget service sends APPWIDGET_ENABLED and AppWidgetProvider.onReceive calls onEnabled',
  env=ENV_WIDGET,
  evidence='SRC AndroidManifest.xml:253-263; SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:53-58; FW-SRC core/java/android/appwidget/AppWidgetProvider.java:84-85, 159-167',
  note='INFERRED for the sender: the AppWidget service is not in fw_src, so the ENABLED broadcast and its delivery to this receiver are not verified. The dispatch to onEnabled is verified (AppWidgetProvider.java:84-85). Written as a direct S_ENTRY edge, the same pattern as the S_ENTRY -> onUpdate edge in graph_def.py. The route through AnkiDroidWidgetSmall.onReceive (line 70, super.onReceive) is owned by the onReceive part and is not written here. The edge writes the preference widgetSmallEnabled=true (line 57), which the STATE_SETTINGS gate on the startService route reads.')

e('S_ENTRY', 'AnkiDroidWidgetSmall.onDisabled', 'ENTRY',
  'the user removes the last AnkiDroid small widget from the home screen: the AppWidget service sends APPWIDGET_DISABLED and AppWidgetProvider.onReceive calls onDisabled',
  env=None,
  evidence='SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:61-67; FW-SRC core/java/android/appwidget/AppWidgetProvider.java:86-87, 159-167, 189',
  note='MISSING GATE MG122: the last widget instance is removed (AppWidgetProvider.java:159-167 says onDisabled runs when the last instance is deleted). ENV_WIDGET covers adding the widget and APPWIDGET_UPDATE only, and no predefined ENV or STATE covers widget removal. env and needs_state unset. The INFERRED sender note of onEnabled applies. The edge writes the preference widgetSmallEnabled=false (line 66).')

e('S_ENTRY', 'AnkiDroidWidgetSmall$UpdateService$1.onReceive', 'SYSTEM',
  'the SD card is mounted again (MEDIA_MOUNTED for a file volume) while this process still holds the mount receiver registered by an earlier widget update with the card unmounted',
  env=ENV_SDCARD_EVENT, needs_state=STATE_SESSION,
  evidence='SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:104-132; FW-SRC core/java/android/content/BroadcastReceiver.java:327',
  note='MISSING GATE MG123: the receiver is registered only when buildUpdate runs with the card unmounted (AnkiDroidWidgetSmall.java:104-110, the !mounted branch); no predefined ENV covers that condition. STATE_SESSION is the process-lifetime part (the static mMountReceiver field, line 40). The body needs two MEDIA_MOUNTED broadcasts: the first only sets remounted (line 124); the second calls WidgetStatus.update (line 118) and unregisters (line 121). The auto CALL edge to WidgetStatus.update does not carry the second-broadcast guard (lead for the orchestrator). Delivery of MEDIA_MOUNTED to a dynamic receiver is not in fw_src: INFERRED.')

# --- UpdateService lifecycle. The framework creates the service and delivers the start command (startService, WidgetStatus.java:106-109).

e('AnkiDroidWidgetSmall$UpdateService.<init>', 'AnkiDroidWidgetSmall$UpdateService.onStart', 'LIFECYCLE',
  'the framework creates the UpdateService and delivers the start command: onStartCommand calls onStart(Intent, int)',
  env=None,
  evidence='FW-SRC core/java/android/app/ActivityThread.java:3321, 3339, 3464-3474; FW-SRC core/java/android/app/Service.java:350, 504-506; SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:88',
  note='onCreate is not overridden, so the framework default runs (ActivityThread.java:3339). The start itself is the INTENT edge WidgetStatus$UpdateDeckStatusAsyncTask.onPostExecute -> AnkiDroidWidgetSmall$UpdateService.<init> (WidgetStatus.java:106-109), written by batch 080; its gate is STATE_SETTINGS (sSmallWidgetEnabled, WidgetStatus.java:106). env None here.')

# --- Widget tap (PendingIntent to the launcher activity) from buildUpdate.

e('AnkiDroidWidgetSmall$UpdateService.buildUpdate', 'IntentHandler.<init>', 'INTENT',
  'the user taps the widget: the PendingIntent (MAIN, LAUNCHER) starts IntentHandler, which the framework creates with its constructor',
  env=None,
  evidence='SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:164-169; SRC com/ichi2/anki/IntentHandler.java:36-38',
  note='env None, the same as the launcher entry (IntentHandler.onCreate, AndroidManifest.xml:81-89). The tap is an event on the widget host, not a predefined ENV. The route into buildUpdate is gated upstream (the startService edge with STATE_SETTINGS, then onStart). The PendingIntent delivery to the activity is not in fw_src: INFERRED.')

# --- Mount receiver registration. The builder does not follow REGISTER for reachability; the route is the SYSTEM edge above.

e('AnkiDroidWidgetSmall$UpdateService$1.<init>', 'AnkiDroidWidgetSmall$UpdateService$1.onReceive', 'REGISTER',
  'the mount receiver is registered with registerReceiver for MEDIA_MOUNTED on a file volume',
  env=None,
  evidence='SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:111-132',
  note='onReceive is in this part. The builder does not follow REGISTER for reachability; the route is the S_ENTRY -> AnkiDroidWidgetSmall$UpdateService$1.onReceive SYSTEM edge above. The <init> is called from buildUpdate (auto CALL, line 111).')

# --- UNREACHABLE entries.

UNREACHABLE['AnkiDroidWidgetSmall$UpdateService.onBind'] = (
    'no_trigger_in_app',
    "The service is started, never bound. onBind is reached only through ActivityThread.handleBindService (ActivityThread.java:3356-3366), which needs a bindService call for this component. The app has no such call: the only bindService-related text in src/main/java is unbindService (CustomTabActivityHelper.java:72). The manifest declares the service with no intent-filter and no exported attribute (AndroidManifest.xml:266), so no other app can bind to it either (the Android default is not exported when there is no intent-filter). onBind returns null (AnkiDroidWidgetSmall.java:177-180) and is never reached.",
    'SRC com/ichi2/widget/AnkiDroidWidgetSmall.java:177-180; SRC AndroidManifest.xml:266; SRC com/ichi2/compat/customtabs/CustomTabActivityHelper.java:72; FW-SRC core/java/android/app/ActivityThread.java:3356-3366; FW-SRC core/java/android/app/Service.java:549',
    'SOURCE')
