# AnkiDroid batch 047 (LABEL helper). LoadPronounciationActivity: 33 methods. The full row list is in
# graphs/AnkiDroid/parts/label_047.md. Page node: S_LOAD_PRONOUNCIATION. Gates: ENV_NETWORK (predefined; its text names
# AnkiWeb, the code check is Connection.isOnline, general connectivity). LIFECYCLE edges (graph_def.py:281-282) and
# automatic CALL edges are not written here.

e('S_LOAD_PRONOUNCIATION', 'LoadPronounciationActivity$1.onClick', 'GUI',
  'tap the Load pronunciation button (added to the layout at line 118)',
  env=None,
  gui=['tap the Load pronunciation button (added to the layout at line 118)'],
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:116-126',
  note='No gate on the tap. The online check is inside onLoadPronunciation (LoadPronounciationActivity.java:155), reached from this listener by an automatic CALL edge (line 123).')

e('S_LOAD_PRONOUNCIATION', 'LoadPronounciationActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the user opens the options menu (menu key or the action overflow)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:143-148; FW-SRC core/java/android/app/Activity.java:3386-3388; FW-SRC core/java/com/android/internal/policy/PhoneWindow.java:580, 631',
  note='PhoneWindow.preparePanel calls the callback onCreatePanelMenu, which calls onCreateOptionsMenu (Activity.java:3388). The menu resource is res/menu/activity_load_pronounciation.xml. No gate.')

e('S_LOAD_PRONOUNCIATION', 'LoadPronounciationActivity.onSaveInstanceState', 'FRAMEWORK',
  'the framework saves the screen state when the user leaves the screen',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:400-403; FW-SRC core/java/android/app/ActivityThread.java:4023-4025, 4672, 4713-4720',
  note='performStopActivityInner saves the state when the activity is not finishing (ActivityThread.java:4023-4025). The relaunch path (line 4672) is a second call site. No gate.')

e('S_LOAD_PRONOUNCIATION', 'LoadPronounciationActivity.onCancel', 'GUI',
  'the user presses back while the progress dialog is open',
  env=ENV_NETWORK,
  gui=['the user presses back while the progress dialog is open'],
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:155, 182-185, 442-456; SRC com/ichi2/async/Connection.java:475-483; FW-SRC core/java/android/app/Dialog.java:626-629, 650-652, 1231-1235, 1358-1364',
  note='The dialog is shown only after the online check at line 155 passes (Connection.isOnline). ENV_NETWORK text names AnkiWeb; the check is general connectivity, so this is the closest predefined constant.')

e('LoadPronounciationActivity.onLoadPronunciation', 'LoadPronounciationActivity$BackgroundPost.doInBackground', 'ASYNC',
  'translation page request, started after the online check',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:154-170, 199-213; SRC com/ichi2/async/Connection.java:475-483; FW-SRC core/java/android/os/AsyncTask.java:594-595',
  note='The gate is Connection.isOnline (line 155). ENV_NETWORK text names AnkiWeb; the check is general connectivity, so this is the closest predefined constant. The execute call is at line 170.')

e('LoadPronounciationActivity.processPostFinished', 'LoadPronounciationActivity$BackgroundPost.doInBackground', 'ASYNC',
  'pronunciation page request, started after the translation page gives a pronunciation link',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:288-306; FW-SRC core/java/android/os/AsyncTask.java:594-595',
  note='The request runs only when the translation result gives a page address (not "no" and not FAILED, lines 288-299), and the network is needed. ENV_NETWORK text names AnkiWeb; closest predefined constant.')

e('LoadPronounciationActivity$BackgroundPost.doInBackground', 'LoadPronounciationActivity$BackgroundPost.onPostExecute', 'ASYNC',
  'AsyncTask delivers the fetched page to onPostExecute on the UI thread',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:199-213, 232-238; FW-SRC core/java/android/os/AsyncTask.java:369-371, 691-696',
  note='Framework delivery (postResult, then finish calls onPostExecute). No gate of its own; the network gate is on the edge that starts doInBackground.')

e('LoadPronounciationActivity.processPostFinished', 'LoadPronounciationActivity$DownloadFileTask.doInBackground', 'ASYNC',
  'mp3 download, started after the pronunciation page gives an mp3 address',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:323-335, 251-253; SRC com/ichi2/anki/web/HttpFetcher.java:124-127, 134-166; FW-SRC core/java/android/os/AsyncTask.java:594-595',
  note='The gate is the network (HTTP GET, then POST when the GET fails, HttpFetcher.java:124-127). ENV_STORAGE is not used: the file is written to the app cache directory (HttpFetcher.java:134-166). ENV_NETWORK text names AnkiWeb; closest predefined constant.')

e('LoadPronounciationActivity$DownloadFileTask.doInBackground', 'LoadPronounciationActivity$DownloadFileTask.onPostExecute', 'ASYNC',
  'AsyncTask delivers the download result (file path or FAILED text) to onPostExecute',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:250-263; FW-SRC core/java/android/os/AsyncTask.java:369-371, 691-696',
  note='Framework delivery. No gate of its own.')

e('LoadPronounciationActivity.receiveMp3File', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'RESULT_OK with the mp3 path; the host activity forwards the result to the field controller',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:368-374; SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:312-318; SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:138, 294-296',
  note='The result carries a path only after the HTTP download succeeds (network). The receiver is assumed to be the host activity that started the screen through the field controller (BasicTextFieldController.java:138 uses mActivity; its constructor was not printed). ENV_NETWORK text names AnkiWeb; closest predefined constant.')

UNREACHABLE['LoadPronounciationActivity$2.onClick'] = ('no_trigger_in_app',
  'The Save button mSaveButton gets this listener in onCreate (line 130), but mSaveButton is never added to any view or window: in the source tree (src/main/java) its only uses are the declaration (line 81), creation (line 128), setText (line 129) and the listener (line 130). Without a view in the window, no touch or click reaches onClick.',
  'SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:81, 128-135',
  'SOURCE')
