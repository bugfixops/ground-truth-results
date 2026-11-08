# AnkiDroid batch 048 (LABEL helper). MultimediaEditFieldActivity (25 methods) and PickStringDialogFragment (5 methods).
# The full row list is in graphs/AnkiDroid/parts/label_048.md.
#
# Route ownership: the LIFECYCLE edges for onCreate (<init> -> onCreate) and onCreateDialog (<init> -> onCreateDialog)
# come from lc_chain (graph_def.py:284-285, 287-288). The INTENT edge into <init> is label_012. The automatic CALL edges
# come from the builder and are not written here. The page edges below belong to this part because their destination is
# in this batch.
#
# Gates: MG422 (saved-state restore to finishCancel). The network checks map to ENV_NETWORK. The RECORD_AUDIO request
# maps to ENV_PERM_RECORD.

# --- Options menu, lifecycle and framework callbacks of the editor (lc_chain skips onDestroy and onOptionsItemSelected).
e('S_MULTIMEDIA_EDIT_FIELD', 'MultimediaEditFieldActivity.onCreateOptionsMenu', 'FRAMEWORK',
  'the framework builds the options menu of the editor (text, image, audio and done items)',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:149-157; FW-SRC core/java/android/app/Activity.java:3386-3390',
  note='Framework callback, not an app CALL: onCreatePanelMenu calls onCreateOptionsMenu (Activity.java:3388). No gate.')

e('S_MULTIMEDIA_EDIT_FIELD', 'MultimediaEditFieldActivity.onOptionsItemSelected', 'GUI',
  'tap an item of the editor options menu (to text, to image, to audio, or done)',
  env=None,
  gui=['tap an item of the editor options menu (to text, to image, to audio, or done)'],
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:160-192; SRC res/menu/activity_edit_text.xml:5, 11, 17, 23',
  note='Item ids: multimedia_edit_field_to_text, multimedia_edit_field_to_image, multimedia_edit_field_to_audio, multimedia_edit_field_done. Each to-field item is visible only when the field type differs (MultimediaEditFieldActivity.java:153-155). No gate.')

e('S_MULTIMEDIA_EDIT_FIELD', 'MultimediaEditFieldActivity.onDestroy', 'LIFECYCLE',
  'the editor finishes (done, cancel or back) and the framework destroys it',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:335-343, 112, 283; FW-SRC core/java/android/app/Activity.java:5526-5528, 7204-7208',
  note='lc_chain skips onDestroy (LC_NO_TRIGGER in graph_def.py), so this edge is written here. finish() (Activity.java:5526) leads to performDestroy (Activity.java:7204-7208) and then onDestroy. No gate.')

e('S_MULTIMEDIA_EDIT_FIELD', 'MultimediaEditFieldActivity.onSaveInstanceState', 'LIFECYCLE',
  'the user leaves the editor (home, task switch) and the framework saves its instance state',
  env=None,
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:351-355, 77-83; FW-SRC core/java/android/app/Activity.java:1565-1567',
  note='MISSING GATE MG422: the editor is restored after process death from this saved state (BUNDLE_KEY_SHUT_OFF true), and onCreate then calls finishCancel (MultimediaEditFieldActivity.java:77-83, an automatic CALL). No ENV or STATE kind covers process death. env and needs_state unset.')

# --- RECORD_AUDIO request of an audio field (recreateEditingUi, line 130) and its callback.
e('MultimediaEditFieldActivity.recreateEditingUi', 'MultimediaEditFieldActivity.onRequestPermissionsResult', 'FRAMEWORK',
  'the user answers the RECORD_AUDIO request that an audio field asked for; the system calls back',
  env=ENV_PERM_RECORD,
  evidence='SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:127-133, 322-327; FW-SRC core/java/android/app/Activity.java:4371-4379, 7259-7274, 7412-7419',
  note='The request is made only for an AudioField without the permission (MultimediaEditFieldActivity.java:128-131). The callback is dispatched by the framework (Activity.java:7270, 7419). ActivityCompat.requestPermissions is in the support library, not read: INFERRED.')

# --- Child results to the editor (RESULT edges; the destination onActivityResult is in this batch).
e('S_TRANSLATION', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'the translation activity returns a translation to the editor (REQUEST_CODE_TRANSLATE_GLOSBE); the text field is updated',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/anki/multimediacard/activity/TranslationActivity.java:196-200, 356-361; SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:286-290, 393-399; FW-SRC core/java/android/app/Activity.java:7259-7266',
  note='Page edge; the child is started by BasicTextFieldController.startTranslationWithGlosbe (BasicTextFieldController.java:393-399, another batch) with startActivityForResult on the editor. The network check is TranslationActivity.translate (line 197, Connection.isOnline), mapped to ENV_NETWORK. RESULT_OK is set by returnTheTranslation (line 361).')

e('S_LOAD_PRONOUNCIATION', 'MultimediaEditFieldActivity.onActivityResult', 'RESULT',
  'the pronunciation activity returns an mp3 file to the editor (REQUEST_CODE_PRONOUNCIATION); the audio field is set through handleFieldChanged',
  env=ENV_NETWORK,
  evidence='SRC com/ichi2/anki/multimediacard/activity/LoadPronounciationActivity.java:154-158, 349-372; SRC com/ichi2/anki/multimediacard/fields/BasicTextFieldController.java:136-138, 294-307; FW-SRC core/java/android/app/Activity.java:7259-7266',
  note='Page edge; the child is started by the pronounce button (BasicTextFieldController.java:136-138, another batch). The network check is LoadPronounciationActivity.onLoadPronunciation (line 155, Connection.isOnline), mapped to ENV_NETWORK. RESULT_OK is set in receiveMp3File (line 372). The controller then calls handleFieldChanged (BasicTextFieldController.java:307).')

# --- UNREACHABLE: createSpareMenu, gtxt and the four listeners exist only on the SDK_INT <= GINGERBREAD_MR1 branch of onCreate
# (MultimediaEditFieldActivity.java:101-105). That branch is not taken on API 27. The GINGERBREAD_MR1 value is not read
# (Build.java is absent from fw_src), so the claim is INFERRED.

UNREACHABLE['MultimediaEditFieldActivity.createSpareMenu'] = ('closed_by_api_level',
  'createSpareMenu is called only from onCreate (MultimediaEditFieldActivity.java:104), inside the branch SDK_INT <= VERSION_CODES.GINGERBREAD_MR1 (line 102). On API 27 that branch is not taken. The GINGERBREAD_MR1 value is not read (Build.java absent from fw_src): source not read.',
  'SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:101-105, 195',
  'INFERRED')

UNREACHABLE['MultimediaEditFieldActivity.gtxt'] = ('closed_by_api_level',
  'gtxt is called only from createSpareMenu (MultimediaEditFieldActivity.java:200, 210, 220, 230), and createSpareMenu is closed by the API branch at line 102. The GINGERBREAD_MR1 value is not read (Build.java absent from fw_src): source not read.',
  'SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:200, 210, 220, 230, 346-348',
  'INFERRED')

UNREACHABLE['MultimediaEditFieldActivity$1.<init>'] = ('closed_by_api_level',
  'The listener is created only in createSpareMenu (MultimediaEditFieldActivity.java:201), which runs only on the API branch at line 102. On API 27 that branch is not taken. The GINGERBREAD_MR1 value is not read: source not read.',
  'SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:101-105, 199-207',
  'INFERRED')

UNREACHABLE['MultimediaEditFieldActivity$1.onClick'] = ('closed_by_api_level',
  'The click reaches onClick only through the button that carries this listener (created in createSpareMenu, lines 199-206). That button is created only on the API branch at line 102, which is not taken on API 27. The GINGERBREAD_MR1 value is not read: source not read.',
  'SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:101-105, 199-207',
  'INFERRED')

UNREACHABLE['MultimediaEditFieldActivity$2.<init>'] = ('closed_by_api_level',
  'The listener is created only in createSpareMenu (MultimediaEditFieldActivity.java:211), which runs only on the API branch at line 102. On API 27 that branch is not taken. The GINGERBREAD_MR1 value is not read: source not read.',
  'SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:101-105, 209-217',
  'INFERRED')

UNREACHABLE['MultimediaEditFieldActivity$2.onClick'] = ('closed_by_api_level',
  'The click reaches onClick only through the button created in createSpareMenu (lines 209-216), which is created only on the API branch at line 102. The GINGERBREAD_MR1 value is not read: source not read.',
  'SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:101-105, 209-217',
  'INFERRED')

UNREACHABLE['MultimediaEditFieldActivity$3.<init>'] = ('closed_by_api_level',
  'The listener is created only in createSpareMenu (MultimediaEditFieldActivity.java:221), which runs only on the API branch at line 102. On API 27 that branch is not taken. The GINGERBREAD_MR1 value is not read: source not read.',
  'SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:101-105, 219-227',
  'INFERRED')

UNREACHABLE['MultimediaEditFieldActivity$3.onClick'] = ('closed_by_api_level',
  'The click reaches onClick only through the button created in createSpareMenu (lines 219-226), which is created only on the API branch at line 102. The GINGERBREAD_MR1 value is not read: source not read.',
  'SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:101-105, 219-227',
  'INFERRED')

UNREACHABLE['MultimediaEditFieldActivity$4.<init>'] = ('closed_by_api_level',
  'The listener is created only in createSpareMenu (MultimediaEditFieldActivity.java:231), which runs only on the API branch at line 102. On API 27 that branch is not taken. The GINGERBREAD_MR1 value is not read: source not read.',
  'SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:101-105, 229-237',
  'INFERRED')

UNREACHABLE['MultimediaEditFieldActivity$4.onClick'] = ('closed_by_api_level',
  'The click reaches onClick only through the button created in createSpareMenu (lines 229-236), which is created only on the API branch at line 102. The GINGERBREAD_MR1 value is not read: source not read.',
  'SRC com/ichi2/anki/multimediacard/activity/MultimediaEditFieldActivity.java:101-105, 229-237',
  'INFERRED')
