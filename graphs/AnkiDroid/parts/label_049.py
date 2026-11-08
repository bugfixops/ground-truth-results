# AnkiDroid batch 049 (LABEL helper). TranslationActivity (20 methods), its listeners TranslationActivity$1 (2) and
# TranslationActivity$BackgroundPost (3), NotificationService (4) and KeepAliveService (3). The full row list is in
# graphs/AnkiDroid/parts/label_049.md.
#
# Route ownership:
# - The INTENT edges into TranslationActivity.<init> (BasicTextFieldController.startTranslationWithGlosbe, lines 393-398)
#   and into NotificationService.<init> (WidgetStatus.UpdateDeckStatusAsyncTask.onPostExecute, lines 111-115) belong to
#   those batches. Not written here.
# - The LIFECYCLE edges (graph_def.py lines 290-291 and 296-297) already exist. Not repeated.
# - Automatic CALL edges come from auto_calls.json. Not written here.
# - Edges whose source is a page (S_*) or a method of this batch are written here.
#
# Gates: MG432 (batch range MG432-MG441). Predefined constants used: ENV_NETWORK (Glosbe lookup, which is checked by
# Connection.isOnline; the constant text names AnkiWeb, flagged), STATE_SETTINGS (notification preference).

# --- Options menu of the translation screen (page S_TRANSLATION).
e('S_TRANSLATION', 'TranslationActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the translation screen builds its options menu (the action bar menu)',
  env=None,
  evidence='FW-SRC core/java/android/app/Activity.java:3386-3388; SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:171-176',
  note='The framework calls onCreatePanelMenu, which calls onCreateOptionsMenu (Activity.java:3388). The menu is inflated from R.menu.activity_translation (TranslationActivity.java:174). No gate.')

# --- Translate button under the two language spinners (page S_TRANSLATION).
e('S_TRANSLATION', 'TranslationActivity$1.onClick', 'GUI',
  'tap the translate button under the two language spinners',
  env=None,
  gui=['tap the translate button under the two language spinners'],
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:151-164',
  note='The listener is set in onCreate (TranslationActivity.java:153). It saves the two selected languages and calls translate (line 162). No gate here: translate checks the connection itself (line 197).')

# --- Pick list of the Glosbe results (page S_DLG_PICK_STRING; the list exists only after a Glosbe lookup).
e('S_DLG_PICK_STRING', 'TranslationActivity.onClick', 'GUI',
  'tap one translation in the pick list (the list opens after a successful Glosbe lookup)',
  env=ENV_NETWORK,
  gui=['tap one translation in the pick list (the list opens after a successful Glosbe lookup)'],
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:291-297, 391-395; SRC com/ichi2/anki/multimediacard/activity/PickStringDialogFragment.java:44-50',
  note='showPickTranslationDialog sets this activity as the listener (TranslationActivity.java:294). PickStringDialogFragment passes it to builder.setAdapter (PickStringDialogFragment.java:49), so a tap calls onClick(dialog, which). The list exists only after a Glosbe response, so the gate is ENV_NETWORK (the nearest predefined network kind; flagged). The body calls returnTheTranslation (automatic CALL, line 394).')

# --- Back key or cancel on the progress dialog (page S_TRANSLATION; the dialog exists only after the online check).
e('S_TRANSLATION', 'TranslationActivity.onCancel', 'GUI',
  'press back (or cancel) on the progress dialog while the Glosbe lookup runs',
  env=ENV_NETWORK,
  gui=['press back (or cancel) on the progress dialog while the Glosbe lookup runs'],
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:197-206, 398-401; FW-SRC core/java/android/app/Dialog.java:1363-1364',
  note='The progress dialog is shown only after the online check (TranslationActivity.java:197-203) and is cancelable with this activity as the OnCancelListener (lines 205-206). Dialog dispatches CANCEL to the listener (Dialog.java:1363-1364). The BACK key that cancels the dialog is not printed in fw_src: INFERRED. onCancel calls stopWorking (automatic CALL, line 400).')

# --- Lookup on a worker thread (method translate, which launches the task at line 212).
e('TranslationActivity.translate', 'TranslationActivity$BackgroundPost.doInBackground', 'ASYNC',
  'the Glosbe lookup starts on a worker thread (mTranslationLoadPost.execute)',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:196-217; FW-SRC core/java/android/os/AsyncTask.java:333',
  note='translate calls execute at line 212 only after the online check at line 197 passes (ENV_NETWORK). AsyncTask runs doInBackground on its worker thread (AsyncTask.java:333).')

e('TranslationActivity$BackgroundPost.doInBackground', 'TranslationActivity$BackgroundPost.onPostExecute', 'ASYNC',
  'the lookup result is delivered to onPostExecute on the UI thread',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:178-191; FW-SRC core/java/android/os/AsyncTask.java:339, 369, 691-695',
  note='AsyncTask.finish calls onPostExecute when the task is not cancelled (AsyncTask.java:695). No gate of its own: the launch edge carries ENV_NETWORK.')

# --- Save state when the activity stops (framework; page S_TRANSLATION).
e('S_TRANSLATION', 'TranslationActivity.onSaveInstanceState', 'FRAMEWORK',
  'the activity stops while it is not finishing, and the framework saves its state',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:382-388; FW-SRC core/java/android/app/ActivityThread.java:4023-4025',
  note='MISSING GATE MG432: the stop-with-save condition is framework state with no ENV or STATE kind, so env and needs_state are unset. The framework saves the state before stop (ActivityThread.java:4023-4025). The saved flag makes a later onCreate call finishCancel (TranslationActivity.java:94-99).')

# --- Result of the pick list: RESULT_OK with the translation (method returnTheTranslation).
e('TranslationActivity.returnTheTranslation', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'the translation returns RESULT_OK with the translated text; the field editor sets the field text',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:356-364; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:313-318; SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:285-290',
  note='setResult(RESULT_OK) with EXTRA_TRANSLATION (TranslationActivity.java:359-361), then finish. MultimediaEditFieldActivity.onActivityResult forwards to the field controller (MultimediaEditFieldActivity.java:315). The controller sets the text on RESULT_OK with the translation extra (BasicTextFieldController.java:286-290). Only the pick list reaches this method, so ENV_NETWORK.')

# --- Failed lookup: RESULT_CANCELED (method returnFailure).
e('TranslationActivity.returnFailure', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'a failed lookup returns RESULT_CANCELED; the field keeps its text',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:367-372; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:313-318; SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:285-286',
  note='setResult(RESULT_CANCELED) (TranslationActivity.java:369), then finish (line 371). The field controller takes only RESULT_OK (BasicTextFieldController.java:286), so the field text is not changed. Reached only after a Glosbe response (ENV_NETWORK).')

# --- Notification service start: onCreate then onStartCommand (framework; the start request comes from WidgetStatus).
e('NotificationService.onCreate', 'NotificationService.onStartCommand', 'FRAMEWORK',
  'the framework calls onStartCommand after onCreate for the start request sent by the widget status update',
  env=None,
  needs_state=STATE_SETTINGS,
  evidence='SRC com/ichi2/anki/services/NotificationService.java:46-54; SRC com/ichi2/widget/WidgetStatus.java:56, 111-115; FW-SRC core/java/android/app/ActivityThread.java:3339, 3464, 3474',
  note='The start request comes from WidgetStatus.UpdateDeckStatusAsyncTask.onPostExecute only when minimumCardsDueForNotification is below 1000000 (WidgetStatus.java:56, 111-115). That is the settings gate STATE_SETTINGS. The framework order (onCreate, then onStartCommand) is ActivityThread.java:3339 and 3474.')

# --- UNREACHABLE: the service has no intent-filter and no app code binds to it.
UNREACHABLE['NotificationService.onBind'] = ('framework_never_calls',
  ("The framework calls onBind only for a bind request (ActivityThread handleBindService, line 3356). No app code binds to a "
   "service: grep over src/main finds only unbindService (CustomTabActivityHelper.java:72), and the service has no "
   "intent-filter (manifest line 250). The app only starts this service (WidgetStatus lines 111-115). Service.onBind is "
   "abstract (Service.java:549)."),
  ('AndroidManifest.xml:250; com/ichi2/anki/services/NotificationService.java:92-95; '
   'com/ichi2/compat/customtabs/CustomTabActivityHelper.java:72; com/ichi2/widget/WidgetStatus.java:111-115; '
   'core/java/android/app/ActivityThread.java:3356; core/java/android/app/Service.java:549'),
  'SOURCE')

# --- UNREACHABLE: KeepAliveService is not declared in the manifest, so the framework cannot create or bind it.
UNREACHABLE['KeepAliveService.<clinit>'] = ('closed_by_configuration',
  ("The class is not declared in AndroidManifest.xml, so the framework cannot create or bind it. The only in-app reference "
   "is the class literal KeepAliveService.class.getCanonicalName() in CustomTabsHelper.addKeepAliveExtra (lines 49-52), "
   "called from CompatV16 (line 85). A class literal and getCanonicalName() do not run the static initializer, and nothing "
   "creates the class, so <clinit> never runs."),
  ('com/ichi2/compat/customtabs/KeepAliveService.java:25-26; com/ichi2/compat/customtabs/CustomTabsHelper.java:49-52; '
   'com/ichi2/compat/CompatV16.java:85; AndroidManifest.xml:244-255'),
  'SOURCE')

UNREACHABLE['KeepAliveService.<init>'] = ('closed_by_configuration',
  ("Default constructor. Same cause as <clinit>: no manifest declaration, so the framework cannot instantiate the service, "
   "and no app code creates it."),
  ('com/ichi2/compat/customtabs/KeepAliveService.java:25-31; AndroidManifest.xml:244-255'),
  'SOURCE')

UNREACHABLE['KeepAliveService.onBind'] = ('closed_by_configuration',
  ("Bind target that the Custom Tabs keep-alive extra names by class name only (CustomTabsHelper lines 49-52). Without a "
   "manifest declaration the activity manager cannot resolve the component in this package, so onBind is never called."),
  ('com/ichi2/compat/customtabs/KeepAliveService.java:28-31; com/ichi2/compat/customtabs/CustomTabsHelper.java:49-52; '
   'AndroidManifest.xml:244-255'),
  'SOURCE')
